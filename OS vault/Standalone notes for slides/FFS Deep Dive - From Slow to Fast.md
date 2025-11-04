
The original UNIX File System (like VSFS) was simple, but it treated the disk like RAM (random-access), which led to terrible performance by scattering file blocks everywhere. The Fast File System (FFS), developed at Berkeley, solved this by becoming **"disk-aware."**

## Part 1: The FFS Optimization

### 1. The Core Idea: Locality

FFS recognized that on a mechanical disk, **seek time** (moving the disk head) is the ultimate enemy.

The solution is **Locality**: keep related files (or a file's own data blocks) physically close to each other on the disk to minimize disk head travel.

### 2. Solution: Cylinder Groups (The Neighborhoods)

To enforce locality, FFS partitioned the physical disk into several **Cylinder Groups** (or Block Groups, as they're called in modern systems like `ext4`).

- **Structure:** Each group is a self-contained, mini-file system. It has its own copy of the Superblock (for redundancy), its own Inode Bitmap, its own Data Bitmap, its own chunk of Inodes, and its own Data blocks.
    
- **Goal:** Restrict file I/O to _within_ a single group whenever possible. Accessing files in the same group means the disk head only makes short, fast movements instead of long, slow seeks across the whole disk platter.
    

### 3. Allocation Policies: "Keep Related Stuff Together"

FFS uses smart heuristics (practical rules) to decide where to put new data:

|Policy|Goal|How it's Allocated|
|---|---|---|
|**Directory Placement**|Balance load.|New directories are placed in a group that has a high number of **free Inodes** (meaning lots of room for new files) and a low number of existing directories.|
|**File Placement**|Keep children near parents.|The Inode _and_ its initial data blocks are placed in the **same Cylinder Group as the parent directory's Inode**. This is the key: it keeps all files in a single directory physically close together.|
|**Pre-allocation**|Optimize sequential reading.|When a file is created, the FS reserves a **contiguous chunk** of blocks (e.g., 8 blocks) instead of just one. This ensures that reading the beginning of the file is extremely fast (minimal seeking).|

### 4. The Large File Exception

Large files are a special case. If you put a massive 500MB file all in one Cylinder Group, it would hog all the data blocks, pushing out all the _other_ small files that _should_ be in that directory (like source code files, configs, etc.). This would destroy locality for everything else.

- **The Compromise:** Large files are intentionally spread across different groups to distribute the load.
    
- **The Rule (Example):** The **first 12 direct blocks** (which hold the first 48KB of the file, assuming 4KB blocks) are placed in the **same group as the Inode**. This gives you good locality for the start of the file. All subsequent blocks (managed by indirect pointers) are placed in **other, separate groups**. This balances fast startup reading with good load distribution for the rest of the disk.
    

## Part 2: Cheating the Disk (Caching & Buffering)

Even FFS is painfully slow compared to RAM. These memory techniques are used to hide that latency from the user.

### Caching (Making Reads Invisible)

- **What it is:** Storing copies of disk blocks (especially Inodes and Directory Data) in fast memory (DRAM).
    
- **Static vs. Dynamic:** Early systems used a **fixed-size cache** (wasteful!). Modern systems (like Linux, Windows, macOS) use a **dynamic unified page cache** where memory is shared between the file system and application memory, adjusting size on demand.
    
- **Benefit:** Turns dozens of slow I/O reads (e.g., resolving a long path like `/usr/local/bin/python`) into instant cache hits. The disk is never even touched.
    

### Write Buffering (Laziness is a Virtue)

- **What it is:** Holding disk updates (writes) in memory buffers and delaying the _actual_ write to the disk (e.g., for 5-30 seconds).
    
- **Benefits:**
    
    1. **Batching:** Merge multiple writes to the same metadata block (e.g., writing to the Inode Bitmap for two new files) into a single physical I/O.
        
    2. **Scheduling:** Re-order the pending writes to minimize disk head movement (e.g., write block 10, then 12, then 15, even if they were requested in a different order).
        
    3. **Avoiding Writes:** If a file is created and then deleted _before_ the buffer is flushed (e.g., a temporary compile file), the I/O is cancelled entirely and never happens.
        
- **The Trade-Off:** **Data Reliability.** This is the big one. If the system crashes (power loss) while updates are still in the memory buffer, that data is lost and the file system state can become inconsistent. This critical problem is exactly why **Journaling** file systems (like `ext3`, `ext4`, `NTFS`) were invented—to make buffered writes safe.
    

This covers the core logic of FFS and the memory tricks that make it (and its descendants) usable in the real world.