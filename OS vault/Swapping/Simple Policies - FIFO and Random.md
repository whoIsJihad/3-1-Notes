# Simple Policies: FIFO and Random

**Tags:** #os #memory-management #page-replacement #algorithms #fifo #random

Before exploring more complex, history-based algorithms, it's useful to understand two of the simplest page replacement policies: First-In, First-Out (FIFO) and Random.

### First-In, First-Out (FIFO)

This policy treats the memory cache as a simple queue. The page that was brought in first is the first one to be evicted, regardless of how recently or frequently it has been used.

**The Policy:** On a page fault, evict the page that has been in memory the longest.

#### Corrected Example Trace

Let's re-run the simulation correctly. We'll track the cache as a queue where new pages are added to the end, and the page at the front is the oldest.

Reference string: `0, 1, 2, 0, 1, 3, 0, 3, 1, 2, 1` Cache size: 3

| Access | Hit/Miss | Evict | Cache State (Front -> End) | Comment                                                                        |
| ------ | -------- | ----- | -------------------------- | ------------------------------------------------------------------------------ |
| **0**  | Miss     |       | `0`                        | 0 is added.                                                                    |
| **1**  | Miss     |       | `0, 1`                     | 1 is added.                                                                    |
| **2**  | Miss     |       | `0, 1, 2`                  | 2 is added. Cache is full. `0` is at the front (oldest).                       |
| **0**  | Hit      |       | `0, 1, 2`                  | No change.                                                                     |
| **1**  | Hit      |       | `0, 1, 2`                  | No change.                                                                     |
| **3**  | Miss     | `0`   | `1, 2, 3`                  | `0` is evicted from the front. `3` is added to the end. `1` is now the oldest. |
| **0**  | Miss     | `1`   | `2, 3, 0`                  | `1` is evicted from the front. `0` is added to the end. `2` is now the oldest. |
| **3**  | Hit      |       | `2, 3, 0`                  | No change.                                                                     |
| **1**  | Miss     | `2`   | `3, 0, 1`                  | `2` is evicted from the front. `1` is added to the end. `3` is now the oldest. |
| **2**  | Miss     | `3`   | `0, 1, 2`                  | `3` is evicted from the front. `2` is added to the end. `0` is now the oldest. |
| **1**  | Hit      |       | `0, 1, 2`                  | No change.                                                                     |

**Result:** 4 hits, 7 misses.

This corrected trace accurately reflects the algorithm's behavior. Even though page 0 and 1 were hit after being loaded, FIFO's strict ordering causes them to be evicted later, leading to subsequent misses.

#### Belady's Anomaly

FIFO suffers from a counter-intuitive problem known as **Belady's Anomaly**: for certain access patterns, **increasing the number of available cache slots can actually decrease the hit rate**. This is because the algorithm's state can be shifted in such a way that it makes worse eviction decisions in the future. This behavior makes FIFO a poor choice for most systems.

### Random Policy

This policy relies on simplicity and luck rather than a complex heuristic.

**The Policy:** On a page fault, evict a random page from memory.

**Analysis:**

- **Pros:** Very simple and fast to implement. It doesn't need to track page age or access history.
    
- **Cons:** Performance is unpredictable. It might get lucky and evict a page that won't be used for a long time (emulating OPT), or it might get unlucky and immediately evict a "hot" (frequently used) page. Over many runs, its performance is generally better than FIFO but worse than history-based approaches like LRU.