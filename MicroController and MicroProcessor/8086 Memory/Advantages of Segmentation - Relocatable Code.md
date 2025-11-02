# Advantages of Segmentation - Relocatable Code

**Tags:** #8086 #segmentation #operating_systems #memory_management

While the `Segment:Offset` addressing scheme might seem complex, it provided a groundbreaking advantage for its time: the ability to create **relocatable programs**. This was a foundational concept for the development of modern multitasking operating systems.

### What is a Relocatable Program?

A relocatable program is a piece of code that can be loaded into **any available area of physical memory** and run correctly without needing to be recompiled.

- **The Problem Before Segmentation:** In simpler systems, a program was compiled to run at a fixed physical address (e.g., `2000H`). If that memory area was already in use by another program, it couldn't be loaded.
    
- **The Segmentation Solution:** With segmentation, all memory accesses within the program are relative to the start of its segments (using offsets). The jumps, function calls, and variable accesses are all defined by their 16-bit offset. When the operating system loads the program, it simply finds a free 64 KB block of memory, points the `CS` and `DS` registers to the start of that block, and the program runs perfectly.
    

### The Power of Relocation

Imagine a simple OS switching between two processes, A and B.

1. Process A is running. Its code starts at physical address `10000H`, so its `CS` is `1000H`.
    
2. The OS needs to switch to Process B. It saves all of Process A's registers.
    
3. The OS had previously loaded Process B's code into memory starting at `48000H`.
    
4. To run Process B, the OS simply loads `4800H` into the `CS` register (along with B's other saved registers).
    
5. All of Process B's internal code jumps and data accesses (e.g., "jump 16 bytes forward") work perfectly, because they are relative to the new `CS` value.
    

The program code itself never has to change. Only the values in the segment registers need to be updated by the OS to "relocate" the program's entire logical address space.

### Redundancy in Addressing

A side effect of this scheme is that a single physical address can be represented by many different `Segment:Offset` pairs. Specifically, there are **4096** (`2^12`) unique logical addresses for every physical address. While this seems redundant, it adds flexibility, as the OS has many choices for segment start points when placing a program in memory.

**Links:** [[8086 Logical Memory and Segmentation]]