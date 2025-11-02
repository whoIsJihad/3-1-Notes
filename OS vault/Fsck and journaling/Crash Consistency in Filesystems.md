
**Tags:** #operatingsystems #filesystems #crashconsistency #fsck #journaling #storage

## The Core Problem: The Consistent-Update Problem

Filesystems store their critical data structures (inodes, bitmaps, directories, data blocks) on persistent storage like an SSD or HDD. Any operation, even something as simple as appending a character to a file, requires multiple, separate writes to update these structures.

The fundamental problem is that a system can crash (e.g., power loss) at any point. If a crash occurs _in the middle_ of a multi-write operation, the on-disk structures can be left in a corrupted, **inconsistent state**.

### Anatomy of an Update: Appending a Data Block

Let's analyze the writes required to append a single data block (`Db`) to an existing file. This requires updating three distinct structures on disk:

1. **The Data Bitmap (`B`):** To allocate a new block, a bit in the data bitmap must be flipped from `0` (free) to `1` (used). Let's call the new version `B[v2]`.
    
2. **The Inode (`I`):** The file's inode must be updated to point to the new data block (`Db`) and its size must be increased. Let's call this `I[v2]`.
    
3. **The Data Block (`Db`):** The actual user data must be written to the newly allocated block.
    

These three writes (`B[v2]`, `I[v2]`, `Db`) form a single logical operation, but they are three distinct physical I/Os.

### [[#Crash Scenarios|Crash Scenarios]]

If a crash happens, the order and completeness of these writes determine the type of corruption.

**Case 1: Only one write succeeds**

- **Only `Db` succeeds:** The user's data is on disk, but no metadata points to it. It's a **lost update**. The block will be overwritten later.
    
- **Only `I[v2]` succeeds:** The inode now points to a garbage data block (since `Db` was never written) and claims a block that the bitmap thinks is free. This is a critical **consistency problem**.
    
- **Only `B[v2]` succeeds:** The data bitmap marks a block as used, but no inode points to it. This is a **space leak**—the block is lost to the filesystem forever.
    

**Case 2: Two of three writes succeed**

- **`I[v2]` and `B[v2]` succeed, but `Db` fails:** The filesystem metadata is consistent (the inode points to a block that the bitmap agrees is allocated), but the block contains garbage. The user reads corrupted data.
    
- **`I[v2]` and `Db` succeed, but `B[v2]` fails:** **Inconsistent**. The inode points to a data block that the bitmap still considers free. The block will eventually be allocated to another file, leading to two files sharing the same block.
    
- **`B[v2]` and `Db` succeed, but `I[v2]` fails:** **Inconsistent**. A data block is marked as used and contains data, but no file's inode points to it. This is another form of a space leak.
    

## Solution 1: FSCK (File System Checker)

The first approach to this problem was not prevention, but post-crash repair.

#fsck is a tool that runs on boot after a crash. It scans the _entire_ disk to find and fix inconsistencies.

### What `fsck` Checks:

- **Superblock:** Verifies that the superblock's metadata (e.g., total filesystem size) is sane.
    
- **Free Blocks:** It performs a full traversal of the filesystem starting from the root directory, noting every block that is reachable. It then compares this list of live blocks to the data bitmap.
    
    - If a block is marked `used` in the bitmap but wasn't found in the traversal, `fsck` marks it `free` (fixing a space leak).
        
    - If a block is `reachable` but marked `free` in the bitmap, `fsck` marks it `used` (fixing inconsistency).
        
- **Inode State:** Checks each inode for corruption, valid types, etc.
    
- **Inode Links:** Recalculates the reference count (`nlink`) for every inode by scanning all directories and compares it to the stored value. Corrects mismatches.
    
- **Duplicates & Bad Pointers:** Detects if two different inodes point to the same data block or if an inode points to a block outside the valid data region.
    
- **Directory Checks:** Ensures `.` and `..` are correct and that directories do not have multiple hard links.
    

**Drawback:** `fsck` is extremely slow. On modern large disks, a full scan can take hours. It scales `O(size-of-disk-volume)`, which is unacceptable for fast reboots.

## Solution 2: Journaling (Write-Ahead Logging)

This is the modern, preventative approach. The core idea is simple:

> Before you perform the actual, dangerous multi-part write, first write a private note in a safe place (the "log" or "journal") describing exactly what you intend to do.

This is **Write-Ahead Logging**.

The filesystem reserves a contiguous area on the disk for this log. All updates happen in two stages:

1. **Journal Write:** Write the entire transaction to the log.
    
2. **Checkpoint:** Write the changes from the log to their final locations in the main filesystem.
    

### A) Data Journaling

This is the simplest form. It logs _everything_—both metadata and data.

**The Transaction:** An update is bundled into a transaction, which is written sequentially to the log.

```
// A single transaction in the log
struct transaction {
  block TxB;  // Transaction Begin block, with a transaction ID (TID)
  block I[v2]; // The new version of the inode
  block B[v2]; // The new version of the data bitmap
  block Db;   // The new user data block
  block TxE;  // Transaction End block, with the same TID
};
```

**The Process & Crash Recovery:**

1. **Journal Write:** Write `TxB`, `I[v2]`, `B[v2]`, and `Db` to the log.
    
2. **Journal Commit:** _After_ the previous writes are confirmed on disk, write `TxE` to the log. The `TxE` block acts as the atomic commit point.
    
3. **Checkpoint:** Write `I[v2]`, `B[v2]`, and `Db` to their final locations in the filesystem.
    

**Recovery:** After a crash, the OS recovery tool scans the journal.

- If it finds a transaction with a `TxB` but no matching `TxE`, the crash happened before the commit. The partial transaction is ignored.
    
- If it finds a complete transaction (`TxB` and `TxE`), the crash may have happened before the checkpoint. The recovery tool simply **replays** the transaction, copying the blocks from the log to their final locations. This guarantees consistency.
    

**The benefit:** Recovery is now `O(size-of-log)`, not `O(size-of-disk)`, making it incredibly fast.

### B) Metadata Journaling (Ordered Journaling)

Data journaling is safe but inefficient because it writes all user data **twice** (once to the log, once to the final location). #metadatajournaling is a critical optimization.

The idea is to log _only the metadata_ but strictly control the order of operations.

**The Process:**

1. **Data Write:** Write the user data block (`Db`) to its final on-disk location. **Wait for this to complete.**
    
2. **Journal Metadata Write:** Write the transaction (`TxB`, `I[v2]`, `B[v2]`) to the log.
    
3. **Journal Commit:** Write the `TxE` block to the log.
    
4. **Checkpoint Metadata:** Write the metadata (`I[v2]`, `B[v2]`) to their final locations.
    

This avoids the double data write. If a crash occurs after step 1 but before step 3, the user data is on disk but no metadata points to it (a lost update, which is acceptable). If a crash occurs after step 3, recovery replays the metadata log, which then correctly points to the already-written user data.

### The Tricky Case for Metadata Journaling: Block Reuse

A subtle bug can occur with block reuse. Consider this sequence:

1. **Tx1:** A file `foo` is deleted. Its inode and data block (say, block #1000) are freed. The transaction to update the bitmaps is written to the journal. The checkpoint has _not_ happened yet.
    
2. **Tx2:** A new file `bar` is created. The filesystem, seeing that block #1000 is free _in memory_, re-allocates it for `bar`'s data. This new transaction is also written to the journal.
    
3. **CRASH!**
    

**Recovery:** The OS replays the log.

1. It replays `Tx1`, which updates the _final_ bitmap to mark block #1000 as free.
    
2. It replays `Tx2`, which updates the inode for `bar` to point to block #1000, and updates the _final_ bitmap to mark #1000 as used. _So far, so good. But what if the order was different? Or what if a previous transaction involving block #1000 wasn't checkpointed?_ The slide's example is even more direct: an old transaction `Tx1` in the log points `I[foo]` to block `1000`. Later, `foo` is deleted and `foobar` is created, reusing block `1000`. If `Tx1` is replayed after the crash, it will incorrectly make `foo` point to `foobar`'s data, causing corruption.
    

**Solution: Revoke Records.** When a block is freed, the filesystem can write a special **revoke record** to the journal. During recovery, before replaying any transaction, the OS checks the revoke records. If a transaction tries to modify a block that has been revoked, that part of the transaction is skipped.