# 💾 RAID (Redundant Array of Independent Disks) Deep Dive

Welcome! We are going to break down the mechanics of Parallel Disk Arrays, focusing on how different RAID levels use striping and parity to manipulate performance, capacity, and reliability.

In the world of RAID, we always start with $N$ physical disks, where each disk has a capacity of $B$ data blocks.

## Core Evaluation Metrics

We evaluate every RAID level on three core metrics:

|Metric|Definition|Computational Variable|
|---|---|---|
|**Capacity**|How much usable space is available to the client.|Measured in terms of $N$ and $B$.|
|**Reliability**|The number of simultaneous disk faults the array can tolerate before data is lost.|A simple integer count (e.g., 0, 1).|
|**Performance**|The speed of Read/Write operations.|$R$ (Random I/O), $S$ (Sequential I/O).|

_**Note on Performance Variables:**_

- $\mathbf{R}$: The throughput (operations/second) of a single disk for **Random I/O** (e.g., a disk read/write that requires seeking a new track).
    
- $\mathbf{S}$: The throughput (MB/s) of a single disk for **Sequential I/O** (e.g., reading a large continuous block of data).
    

## 1. RAID Level 0: Striping (The Speed Demon)

RAID 0 is pure performance optimization. It spreads data across all disks without any redundancy.

### ⚙️ Mechanism:

Blocks are spread across the $N$ disks in a round-robin fashion (striped). For instance, Block 0 is on Disk 0, Block 1 on Disk 1, Block 2 on Disk 2, and so on.

### 🧮 Computational Breakdown

|Metric|Formula|Explanation|
|---|---|---|
|**Capacity**|$\mathbf{N \times B}$|Since **no** space is used for redundancy, you get the entire sum of all disk capacities.|
|**Reliability**|$\mathbf{0}$|If _any_ single disk fails, the entire dataset is incomplete, and the whole array fails. There is no fault tolerance.|
|**Performance (R/S)**|$\mathbf{N \times R}$, $\mathbf{N \times S}$|Since the data for a single large file is physically distributed, $N$ disks can perform I/O **in parallel** for that one request, linearly multiplying the speed of a single disk.|

### 💡 Computational Note: Chunk Size

The "chunk size" (the size of the block being striped across the disks) is a critical design choice:

- **Small Chunk:** Maximizes **intra-file parallelism**. More disks read the same file simultaneously, which is great for single, large file I/O. However, it increases the total time spent seeking and positioning the head.
    
- **Large Chunk:** Minimizes the overhead of seeking (positioning time) because I/O is more sequential on each disk, but it reduces the parallelism for that single file.
    

## 2. RAID Level 1: Mirroring (The Safe Bet)

RAID 1 focuses on maximum safety by duplicating data. It is the definition of "paranoid storage."

### ⚙️ Mechanism:

Every data block is exactly duplicated (mirrored) onto a separate disk. Block $D_i$ is on Disk $A$ **AND** Disk $B$. This typically requires an even number of disks ($N/2$ pairs).

### 🧮 Computational Breakdown

|Metric|Formula|Explanation|
|---|---|---|
|**Capacity**|$\mathbf{N \times B / 2}$|Exactly half the space is dedicated to the mirror copy, meaning $50\%$ of your physical space is lost to redundancy.|
|**Reliability**|$\mathbf{1}$ (guaranteed) to $\mathbf{N/2}$ (best case)|You can definitely tolerate **one** failure. In the best-case scenario (if the failed disks are all the mirror copies, and none are original data partners), you could tolerate up to $N/2$ failures.|
|**Random Read**|$\mathbf{N \times R}$|This is where mirroring shines! A read request can be serviced by either the original block or the mirror copy. Since all $N$ disks contain data, you can potentially run $N$ concurrent read requests in parallel.|
|**Random Write**|$\mathbf{(N/2) \times R}$|A single logical write operation **must** be written to two physical locations. This overhead means the effective throughput is limited by the $N/2$ data/mirror pairs, making writes slower than reads.|

## 3. RAID Level 4: Dedicated Parity (The Bottleneck)

RAID 4 introduces **Parity** ($\mathbf{P}$) using the XOR function. This gives fault tolerance without the $50\%$ capacity loss of RAID 1.

### ⚙️ Mechanism:

Data is striped across $N-1$ disks, and **one entire disk** is reserved exclusively for storing the XOR parity block for each stripe.

- The Parity block $P_i$ is computed as: $P_i = D_{0,i} \oplus D_{1,i} \oplus D_{2,i} \oplus \dots \oplus D_{N-2, i}$.
    
- If any one disk fails, the lost data can be reconstructed using the property of XOR: $\mathbf{\text{Lost Data} = \text{All Other Blocks } \oplus P}$.
    

### 🧮 Computational Breakdown

|Metric|Formula|Explanation|
|---|---|---|
|**Capacity**|$\mathbf{(N - 1) \times B}$|You only lose the space of one disk (the parity disk), which is a much better trade-off than RAID 1.|
|**Reliability**|$\mathbf{1}$|The array can tolerate the failure of **any single disk** (data or parity) because the XOR calculation allows for reconstruction.|
|**Sequential Write**|$\mathbf{(N-1) \times S}$|Excellent. When writing a large amount of data (a "full stripe write"), the new parity block $P_{\text{new}}$ is easily computed, and all $N$ disks can be written to in parallel.|

### 🛑 The Small Write Problem (The Killer Flaw)

This is the Achilles' heel of RAID 4. A single **Random Write** is extremely inefficient, creating a major bottleneck on the single dedicated parity disk.

**Why? A single logical small write requires 4 physical I/O operations (the "4 I/O Penalty"):**

1. **Read** the old data block ($D_{\text{old}}$) from its disk. (1 I/O)
    
2. **Read** the old parity block ($P_{\text{old}}$) from the dedicated parity disk. (1 I/O)
    
3. **Compute** the new parity: $P_{\text{new}} = P_{\text{old}} \oplus D_{\text{old}} \oplus D_{\text{new}}$. (CPU step)
    
4. **Write** the new data block ($D_{\text{new}}$) to its disk. (1 I/O)
    
5. **Write** the new parity block ($P_{\text{new}}$) to the dedicated parity disk. (1 I/O)
    

The problem is that I/Os 2 and 5 **always** hit the same dedicated parity disk. This single disk has to handle two I/O operations for _every single write_ in the entire array.

- **Random Write Throughput (RAID 4):** Limited to $\mathbf{R/2}$.
    
- The dedicated parity disk becomes the ultimate bottleneck, severely limiting the array's ability to handle concurrent small writes.
    

## 4. RAID Level 5: Rotated Parity (The Real-World Workhorse)

RAID 5 takes the efficiency of RAID 4's capacity/reliability and fixes the bottleneck problem. This level is the most common choice for general-purpose server storage.

### ⚙️ Mechanism:

The only difference from RAID 4 is that the parity blocks ($\mathbf{P}$) are **rotated** (distributed) across all $N$ drives in the array, instead of being on a single dedicated disk.

### 🧮 Computational Breakdown

|Metric|Formula|Explanation|
|---|---|---|
|**Capacity**|$\mathbf{(N - 1) \times B}$|Same capacity efficiency as RAID 4.|
|**Reliability**|$\mathbf{1}$|Same fault tolerance as RAID 4.|
|**Random Write**|$\mathbf{(N \times R)/4}$|**Solved Bottleneck!**|

### ✅ Why it Solves the Bottleneck

A small write in RAID 5 still has the **4 I/O penalty**, but critically, the two parity I/Os (Read $P_{\text{old}}$ and Write $P_{\text{new}}$) are **not** always hitting the same disk.

Because the parity is distributed, if $N$ different small write requests happen simultaneously, the resulting $4 \times N$ I/Os will be scattered across all $N$ disks. This allows all $N$ disks to work concurrently, effectively utilizing the entire array's bandwidth and scaling the throughput by $N$.

This brilliant mechanical change eliminates the single-disk bottleneck, making RAID 5 the ideal balance of performance, capacity, and reliability.