
**Tags:** #80386 #paging #virtual_memory #mmu #os_concepts

**Paging** is arguably the most important feature introduced in the 80386. It is a second, optional layer of address translation that sits _after_ the segmentation unit. While segmentation divides the logical address space into a few large, variable-sized blocks, paging divides it into many small, fixed-size blocks called **pages**.

This mechanism is the hardware foundation for modern **virtual memory** systems.

### Why Was Paging Needed? The Problem with Segmentation Alone

Segmentation is powerful, but it has a major drawback: **external fragmentation**. Over time, as variable-sized segments are loaded and unloaded from RAM, the free memory gets chopped up into small, non-contiguous holes. You might have 500 MB of total free RAM, but if it's in 1 MB chunks, you can't load a 2 MB segment.

Swapping large, variable-sized segments to and from a hard disk is also very slow and inefficient.

### The Paging Solution: Fixed-Size Blocks

Paging solves these problems by adding a layer of indirection.

- The **linear address space** (the output of the segmentation unit) is divided into fixed-size blocks of **4 KB**, called **pages**.
    
- Physical RAM is also divided into fixed-size blocks of **4 KB**, called **page frames**.
    

The job of the **Paging Unit (PU)** is to map any given logical page to any available physical page frame.

**The Key Advantage:** A contiguous 1 MB block of linear address space (e.g., a video buffer) does not need to occupy a contiguous 1 MB block of physical RAM. The Paging Unit can map its 256 constituent pages to 256 different page frames scattered all over physical memory. This completely eliminates the external fragmentation problem.

### The Two-Level Page Table Structure

To keep track of these mappings for a 4 GB address space, the 80386 uses a two-level table structure stored in memory:

1. **Page Directory:** A single table of 1024 entries. This is the top-level index. The physical address of this directory is stored in the `CR3` control register. Each entry in the Page Directory points to a Page Table.
    
2. **Page Tables:** There can be up to 1024 Page Tables. Each Page Table contains 1024 entries. Each entry in a Page Table points to a 4 KB page frame in physical RAM.
    

### Enabling Paging

Paging is controlled by a single bit: the **`PG` bit (bit 31) in the `CR0` control register**.

- If `PG = 0`, paging is disabled. The linear address from the segmentation unit is used directly as the physical address.
    
- If `PG = 1`, paging is enabled. The linear address must go through the two-level page table translation to find the final physical address.
    

This design gives the OS the flexibility to use a simple segmented model or a powerful, modern paged virtual memory system.

**Links:** [[The Intel 80386 - Dawn of 32-bit Computing]]