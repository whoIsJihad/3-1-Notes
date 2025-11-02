**Tags:** #os #storage #raid #raid4 #parity

# RAID Level 4: Dedicated Parity

RAID 4 improves on the space inefficiency of mirroring by using a **parity** block for redundancy. Data is striped across `N-1` disks, and a single, dedicated disk stores the parity information for each stripe.

### Data Layout and Parity Calculation

Parity is calculated using a bitwise XOR operation. For a given stripe, the parity block is the XOR sum of all the data blocks in that stripe.

`Parity_Block = Block0 XOR Block1 XOR Block2 XOR ... XOR BlockN-2`

|Disk 0 (Data)|Disk 1 (Data)|Disk 2 (Data)|Disk 3 (Parity)|
|---|---|---|---|
|Block 0|Block 1|Block 2|P0 = B0^B1^B2|
|Block 3|Block 4|Block 5|P1 = B3^B4^B5|
|...|...|...|...|

**Reliability:** If any single disk fails, its data can be reconstructed. For example, if Disk 1 fails, its contents can be calculated by XORing the remaining data and the parity: `Block1_reconstructed = Block0 XOR Block2 XOR P0`.

### Performance Analysis: The Small Write Problem

- **Capacity:** `(N - 1) * B`. One disk's worth of capacity is used for parity.
    
- **Reads:** Performance is good. The `N-1` data disks can service read requests in parallel. The parity disk is not involved in reads. Throughput is `(N-1) * R` or `(N-1) * S`.
    
- **Full-Stripe Writes:** If a write operation is large enough to cover all data disks in a stripe (e.g., writing new B0, B1, and B2), performance is good. The controller calculates the new parity `P0_new = B0_new ^ B1_new ^ B2_new` and writes all `N` blocks in parallel.
    
- **Small Writes (The Bottleneck):** For small random writes that update only a single block (e.g., updating B1 to B1_new), the controller cannot just write the new data. It must also update the parity correctly. This requires a **read-modify-write** procedure:
    
    1. **Read** the old data block (`B1_old`).
        
    2. **Read** the old parity block (`P0_old`).
        
    3. **Write** the new data block (`B1_new`).
        
    4. **Write** the new parity block (`P0_new`), which is calculated as `(B1_new XOR B1_old) XOR P0_old`.
        

This sequence turns one logical write into **four physical I/O operations** (2 reads, 2 writes). Furthermore, since all parity updates must go to the **single dedicated parity disk**, it becomes a severe performance bottleneck for random write workloads. The latency is roughly double that of a single disk I/O, and throughput is abysmal (`R/2`).

**Links:** [[RAID MOC]], [[RAID Level 5 - Rotated Parity]]