# Inverted Page Tables

**Tags:** #os #memory-management #paging #alternative-design

An **inverted page table** is a radical departure from the traditional per-process page table design. Instead of having a page table for each process that maps its virtual pages, the system maintains a **single, global inverted page table** with one entry for every **physical frame** in memory.

Each entry in the inverted page table stores the `(Process ID, Virtual Page Number)` that currently occupies that physical frame.

### Address Translation with an Inverted Page Table

Because the table is indexed by physical frame number, a normal lookup is no longer possible. To translate a virtual address `(PID, VPN, offset)`:

1. The system must **search** the entire inverted page table for an entry that matches the current process's `(PID, VPN)`.
    
2. If a match is found at index `i` in the table, then the physical frame number is `i`.
    
3. The physical address is then constructed as `(i << OFFSET_BITS) | offset`.
    

### The Search Problem

The primary drawback of this approach is that a linear search through a potentially massive table on every memory access is prohibitively slow. To make this practical, a high-performance hash table is typically used.

- The `(PID, VPN)` is hashed to find a potential location in the hash table.
    
- The hash table contains pointers to entries in the inverted page table.
    
- Collisions are handled with standard techniques like chaining.
    

Even with a hash table, the translation process is more complex and often slower than the direct lookups possible with multi-level page tables, especially when hash collisions occur.

### Advantages and Disadvantages

- **Advantage: Extreme Space Savings.** The size of the inverted page table is proportional to the amount of physical memory in the system, _not_ the combined size of all virtual address spaces. For a system with many processes, this can result in a dramatic reduction in memory overhead.
    
- **Disadvantage: Slow and Complex Lookups.** The search process is inherently slower than the direct array indexing of traditional page tables. Implementing features like page sharing between processes also becomes more complicated.
    

Due to these trade-offs, inverted page tables are less common in general-purpose operating systems like Linux and Windows, which favor the performance and flexibility of [[Multi-Level Page Tables]].