
**Tags:** #os #memory-management #virtual-memory #swapping #page-replacement #algorithms #map-of-content

When a page fault occurs and there are no free physical frames, the OS must select a page currently in memory to evict. This decision is made by a **page replacement policy**. The goal is to choose a victim page in a way that minimizes the future page fault rate, thereby maximizing performance.

The effectiveness of any policy is highly dependent on the memory access patterns of the running programs, specifically their **temporal and spatial locality**.

### Core Policies and Concepts

- [[The Optimal (OPT) Replacement Policy]]
    
- [[Simple Policies - FIFO and Random]]
    
- [[Using History - The LRU Policy]]
    
- [[Approximating LRU -  The Clock Algorithm]]
    
- [[Advanced Swapping Concepts]]