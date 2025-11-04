

---


---

## **1. Introduction**

A **Log-Structured File System (LFS)** is a type of file system designed for **high write performance**. Instead of updating files and metadata in place, LFS treats the disk as a **sequential log**, appending all changes to the end of the log.

**Key motivations:**

- Reduce random writes (especially important for disks where seeks are expensive)
    
- Simplify crash recovery
    
- Make writes atomic and efficient
    

---

## **2. Core Concepts**

### 2.1 Disk as a Log

- The disk is seen as a **chronological log of segments**.
    
- **Segments**: Large contiguous blocks (e.g., 1–10 MB) containing:
    
    - File data
        
    - Updated inodes (file metadata)
        
    - Parts of the **inode map (imap)**
        
    - Summary block and checksums
        
- Segments are written **sequentially**, one after another:
    

```
[Segment 1] → [Segment 2] → [Segment 3] → ... → [Segment N]
```

- Each segment contains pointers or links to the next, maintaining **chronology**.
    

---

### 2.2 Inode Map (Imap)

- Each inode has an **inode number**, which maps to its **disk block location**.
    
- Instead of updating inode locations in place, LFS stores **imap pieces in segments**.
    
- The **CR (Checkpoint Region)** keeps track of the **latest pointers to these imap pieces**.
    

---

### 2.3 Checkpoint Regions (CR)

- **Two fixed locations on disk**: CR-A and CR-B
    
- Only these regions are **permanently fixed**; the rest of the disk is log-only.
    
- Each CR contains:
    
    - Timestamp (start + end)
        
    - Pointer to the latest segment
        
    - Pointers to imap pieces
        
- **Alternating writes** to CR-A and CR-B ensure that at least one valid checkpoint always exists.
    

---

## **3. Writing Data in LFS**

When a new file is written:

1. Data and inode updates are first stored in **memory buffers**.
    
2. When enough data accumulates, it is **written sequentially as a new segment** on disk.
    
3. After finishing a segment, LFS **writes a new checkpoint** to record:
    
    - Latest segment
        
    - Updated imap locations
        
    - Any superblock info
        

> Memory stores **temporary buffers** and the **in-memory imap**; disk stores **segments**, **CRs**, and **imap pieces**.

---

## **4. Crash Recovery in LFS**

Crashes can happen at any time (power failure, kernel panic). LFS uses a **carefully designed recovery process** to restore a consistent filesystem.

---

### 4.1 The Problem

- If a crash occurs while writing a segment (e.g., Segment 11), only part of it may reach disk.
    
- Without recovery, the filesystem can become **inconsistent**, with partially written data.
    

---

### 4.2 Crash Recovery: Step-by-Step

#### **Step 1: Locate Last Consistent Checkpoint**

1. On reboot, read **CR-A and CR-B**.
    
2. Compare **start and end timestamps** in each CR.
    
3. Select the **latest CR with matching timestamps** → valid checkpoint.
    
4. This CR points to:
    
    - Last fully written segment (e.g., Segment 10)
        
    - Imap pieces on disk
        

---

#### **Step 2: Load In-Memory Imap**

- Use pointers in the valid CR to **load imap pieces into memory**.
    
- The in-memory imap now reflects **the last guaranteed consistent state**.
    

---

#### **Step 3: Roll Forward Through Log Segments**

- Scan disk **sequentially from the next segment after the checkpoint** (Segment 11 onward).
    
- For each segment:
    
    1. Check **checksum / summary block** for integrity.
        
    2. If segment is fully valid:
        
        - Apply inodes and imap updates to **in-memory imap**.
            
    3. If segment is partially written or corrupted:
        
        - Stop scanning
            
        - Discard this segment and anything beyond it
            
- This ensures **minimal data loss** and avoids including corrupted writes.
    

---

#### **Step 4: Finalize Recovery**

- After the roll-forward scan:
    
    - The in-memory imap contains the **latest consistent state**.
        
- Write a **new checkpoint** to CR-A or CR-B (alternating):
    
    - Pointers to imap
        
    - Latest fully written segment
        
- File system is now **consistent and clean**.
    

---

### 4.3 Where Data Lives

|Component|Disk|Memory|
|---|---|---|
|Segments|Full persistent blocks|Only current write buffer (temporary)|
|Checkpoint Region|Fixed positions (CR-A, CR-B)|Only for reading and validation during recovery|
|Inode Map (imap)|Pieces in segments|Full in-memory table (rebuilt from CR + roll-forward)|
|File Writes|Sequentially appended segments|Buffered before flush|

---

### 4.4 Safety Mechanism: Timestamps

- CR write uses **start + body + end timestamps**.
    
- Matching timestamps → checkpoint **valid**
    
- Mismatch → checkpoint **ignored**, fallback to the other CR
    
- Ensures atomic updates without requiring journaling
    

---

### 4.5 Key Points to Remember

- **Disk is append-only log:** sequential segments + fixed CRs
    
- **Memory stores:** in-memory imap + temporary write buffers
    
- **Multiple segments** exist on **disk**, not in memory
    
- **Crash recovery**:
    
    - Find valid CR → load imap → roll forward → rebuild state → write new CR
        
- **Partial writes** are never trusted; scan stops at first corrupted segment
    

---

## **5. Visual Mental Model**

```
Disk:

CR-A (old)    Segment 1 → Segment 2 → ... → Segment 10 → Segment 11 (partial)
CR-B (latest) → points to Segment 10

Memory after recovery:

[in-memory imap] ← rebuilt from CR-B + valid segments
[current write buffer] ← new file writes before flush
```

---

## **6. Summary**

1. LFS treats **disk as a sequential log**, improving write efficiency.
    
2. **Checkpoints (CR-A, CR-B)** anchor the filesystem with pointers to the last fully written segment and inode map.
    
3. **Segments** store file data, inode updates, and imap pieces.
    
4. **Recovery after crash**:
    
    - Pick latest valid CR
        
    - Load in-memory imap
        
    - Scan forward (roll-forward) only valid segments
        
    - Ignore partial/corrupted segments
        
    - Write new checkpoint
        

> **Core Idea:** Start from last safe checkpoint + sequentially roll forward → guarantees consistency and minimal data loss.

---
