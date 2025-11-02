**Tags:** #os #storage #raid #raid5 #parity

# RAID Level 5: Rotated Parity

RAID 5 is the logical evolution of [[RAID Level 4 - Dedicated Parity|RAID 4]], designed specifically to solve its **small write problem**. It uses the same XOR-based parity for redundancy but eliminates the dedicated parity disk by distributing, or **rotating**, the parity blocks across all drives in the array.

### Data Layout

The parity block for each stripe is placed on a different disk. This rotation ensures that the I/O load for small writes is spread evenly across the entire array.

|Disk 0|Disk 1|Disk 2|Disk 3|
|---|---|---|---|
|Block 0|Block 1|Block 2|**P0**|
|Block 3|Block 4|**P1**|Block 5|
|Block 6|**P2**|Block 7|Block 8|
|**P3**|Block 9|Block 10|Block 11|

### Performance Analysis

- **Capacity:** `(N - 1) * B`. Same as RAID 4.
    
- **Reliability:** Tolerates the failure of any single disk. Data reconstruction works the same way as in RAID 4.
    
- **Reads:** Performance is excellent. Since data and parity are spread across all disks, all `N` drives can participate in servicing read requests in parallel, giving a theoretical throughput of `N * R`.
    
- **Writes:**
    
    - The **read-modify-write** penalty still exists for a single small write. It still takes four physical I/Os to complete one logical write.
        
    - **The key improvement is the removal of the bottleneck.** Because the parity is distributed, multiple independent small writes can be processed in parallel. A write to Block 1 (updating P0 on Disk 3) can happen concurrently with a write to Block 5 (updating P1 on Disk 2).
        
    - This distribution allows the random write throughput to scale with the number of disks, achieving a theoretical `(N * R) / 4`. While still penalized compared to RAID 0 or RAID 1, it's a massive improvement over RAID 4's `R/2`.
        

**Links:** [[RAID MOC]], [[RAID Level 4 - Dedicated Parity]], [[RAID Levels Comparison]]