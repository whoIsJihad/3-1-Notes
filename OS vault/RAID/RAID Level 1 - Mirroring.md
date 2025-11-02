**Tags:** #os #storage #raid #raid1

# RAID Level 1: Mirroring

RAID 1 provides high data reliability by using **mirroring**. For every block of data written, an identical copy is stored on a separate, dedicated disk. This creates mirrored pairs of disks.

### Data Layout

The layout is a direct one-to-one copy. The array is typically built with an even number of disks, forming `N/2` pairs.

- A write to logical Block 0 results in a physical write to **both** Disk 0 and Disk 1.
    
- A write to logical Block 1 results in a physical write to **both** Disk 2 and Disk 3. ...and so on.
    

### Performance Analysis

- **Capacity:** `(N / 2) * B`. Exactly half the total physical disk capacity is available for storage; the other half is used for the redundant mirror copy.
    
- **Reliability:** High. The array can tolerate at least one disk failure. It can survive up to `N/2` failures, as long as no two failed disks belong to the same mirrored pair. If both Disk 0 and Disk 1 fail, the data for their logical blocks is lost.
    
- **Latency:**
    
    - **Read:** The latency is that of a single disk I/O. The controller can service the read from either disk in the pair, allowing it to choose the one with the head closer to the target track (shorter seek) or the one that is currently idle.
        
    - **Write:** A logical write requires two physical writes. These are issued in parallel, but the operation is not complete until both have finished. Therefore, the latency is `max(T_I/O_diskA, T_I/O_diskB)`.
        
- **Throughput:**
    
    - **Write:** Since two disks are occupied for every one logical write, the write throughput is `(N / 2) * R` for random writes and `(N / 2) * S` for sequential.
        
    - **Read:** Throughput can be excellent. Because any disk in a pair can service a read, the controller can satisfy multiple read requests in parallel across the entire array. For example, it can read from Disk 0 and Disk 3 simultaneously to service two different requests. This allows the theoretical read throughput to reach `N * R`.
        

**Links:** [[RAID MOC]], [[RAID Levels Comparison]]