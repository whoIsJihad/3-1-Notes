# Using History: The LRU Policy

**Tags:** #os #memory-management #page-replacement #algorithms #lru #locality

Policies like [[Simple Policies - FIFO and Random]]  ignore the access history of pages. More intelligent algorithms leverage the principle of **locality** to make better eviction decisions. The most famous of these is Least Recently Used (LRU).

### The Principle of Locality

- **Temporal Locality:** If a program accesses a memory location, it is likely to access that same location again soon.
    
- **Spatial Locality:** If a program accesses a memory location, it is likely to access nearby memory locations soon.
    

Paging naturally benefits from spatial locality (accessing data within the same page). Replacement policies primarily try to exploit **temporal locality**.

### Least Recently Used (LRU)

LRU is based on the assumption that pages that have not been used for a while are unlikely to be used in the near future.

**The Policy:** On a page fault, evict the page that has been accessed **least recently**.

#### Example Trace

Consider a cache with 3 slots and the reference string: `0, 1, 2, 0, 1, 3, 0, 3, 1, 2, 1` _(We track recency from right-to-left: most recent is on the right)_

| Access | Hit/Miss | Evict | Cache State (Oldest -> Newest) | Comment                                            |
| ------ | -------- | ----- | ------------------------------ | -------------------------------------------------- |
| **0**  | Miss     |       | `0`                            |                                                    |
| **1**  | Miss     |       | `0, 1`                         |                                                    |
| **2**  | Miss     |       | `0, 1, 2`                      | `0` is LRU.                                        |
| **0**  | Hit      |       | `1, 2, 0`                      | `0` is now MRU. `1` is LRU.                        |
| **1**  | Hit      |       | `2, 0, 1`                      | `1` is now MRU. `2` is LRU.                        |
| **3**  | Miss     | `2`   | `0, 1, 3`                      | `2` was the LRU page, so it's evicted. `3` is MRU. |
| **0**  | Hit      |       | `1, 3, 0`                      | `0` is now MRU. `1` is LRU.                        |
| **3**  | Hit      |       | `1, 0, 3`                      | `3` is now MRU. `1` is LRU.                        |
| **1**  | Hit      |       | `0, 3, 1`                      | `1` is now MRU. `0` is LRU.                        |
| **2**  | Miss     | `0`   | `3, 1, 2`                      | `0` was the LRU page, so it's evicted. `2` is MRU. |
| **1**  | Hit      |       | `3, 2, 1`                      | `1` is now MRU. `3` is LRU.                        |

**Result:** 7 hits, 5 misses. Excellent performance, equal to [[The Optimal (OPT) Replacement Policy|OPT]] on this particular trace.

### The Implementation Challenge

While LRU performs very well, a perfect implementation is costly. To find the _exact_ least-recently-used page, the OS would have to perform work on **every memory reference**:

1. On every access, it would need to update some data structure (e.g., a timestamp or a linked list) to record that the page was just used.
    
2. On a page fault, it would have to scan this data structure to find the page with the oldest timestamp or at the tail of the list.
    

This overhead on every memory access is too high for practical systems. Therefore, real-world operating systems use algorithms that **approximate** LRU, such as the [[Approximating LRU: The Clock Algorithm|Clock Algorithm]].