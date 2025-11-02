**Tags:** #os #storage #raid #comparison

# RAID Levels Comparison

This table provides a summary of the trade-offs between the most common RAID levels. Understanding the I/O mechanics behind these numbers is key to choosing the right level for a given workload.

`N` = number of disks, `S` = sequential throughput of one disk, `R` = random throughput of one disk, `D` = latency of one disk I/O.

|Feature|RAID 0 (Striping)|RAID 1 (Mirroring)|RAID 4 (Dedicated Parity)|RAID 5 (Rotated Parity)|
|---|---|---|---|---|
|**Capacity**|`N`|`N / 2`|`N - 1`|`N - 1`|
|**Reliability**|0 Faults|1 Fault (up to N/2)|1 Fault|1 Fault|
|**Sequential Read**|`N * S`|`(N / 2) * S`|`(N - 1) * S`|`(N - 1) * S`|
|**Sequential Write**|`N * S`|`(N / 2) * S`|`(N - 1) * S`|`(N - 1) * S`|
|**Random Read**|`N * R`|`N * R`|`(N - 1) * R`|`N * R`|
|**Random Write**|`N * R`|`(N / 2) * R`|**`R / 2` (Bottleneck)**|`(N / 4) * R`|
|**Latency (Write)**|`D`|`D`|`2 * D` (Read-Modify-Write)|`2 * D` (Read-Modify-Write)|

**Links:** [[RAID MOC]]