**Tags:** #os #storage #raid #raid0

# RAID Level 0: Striping

RAID 0 uses a technique called **striping** to spread data across multiple disks. Its sole purpose is to increase performance by parallelizing I/O operations. It offers no data redundancy.

### Data Layout and Chunk Size

Data is broken down into units called **chunks** (or stripe units), and these chunks are written across the disks in a round-robin fashion. The size of these chunks is a configurable parameter that impacts performance.

Consider a 4-disk array where the chunk size is one block (e.g., 4KB). The logical blocks of data would be laid out physically like this:

|Logical Block|Physical Location|
|---|---|
|Block 0|Disk 0|
|Block 1|Disk 1|
|Block 2|Disk 2|
|Block 3|Disk 3|
|Block 4|Disk 0|
|Block 5|Disk 1|
|...|...|

- **Small Chunk Size:** Encourages high parallelism for a single large file transfer, as the file's data is spread widely across all disks.
    
- **Large Chunk Size:** Allows for better parallelism across multiple independent requests, as different files or parts of files are more likely to reside on different disks.
    

### Performance Analysis

- **Capacity:** `N * B` (where `N` is the number of disks and `B` is the capacity of a single disk). The full capacity of all disks is available.
    
- **Reliability:** **None.** There is no redundancy. If any single disk in the array fails, the entire array is lost because fragments of every file are now missing.
    
- **Throughput:** Excellent for large I/O requests. When the OS requests a large amount of data (e.g., 16KB in the 4-disk example above), the RAID controller can issue parallel read/write commands to all four disks simultaneously. Each disk handles its portion of the request. This allows the theoretical throughput to be `N` times that of a single disk (`N * R` for random, `N * S` for sequential).
    
- **Latency:** For a single I/O request that is striped across multiple disks, the overall latency is determined by the slowest of the parallel operations. Each disk must perform its own seek and rotation before transferring its chunk. The total time for the request to complete is the time it takes for the last disk to finish its work.
    

```
T_I/O = max(T_I/O_disk0, T_I/O_disk1, ..., T_I/O_diskN-1)
```

**Links:** [[RAID MOC]], [[RAID Levels Comparison]]