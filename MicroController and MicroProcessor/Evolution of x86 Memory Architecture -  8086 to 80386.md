
---

This document breaks down the fundamental differences in memory management between the Intel 8086, 80286, and 80386 processors. We'll focus on how each processor accesses physical memory and how the architecture evolved to support virtual memory and multitasking.

## Part 1: The 8086 — Real Mode (The Flat World)

The 8086 was the foundation. It operated in a single mode, later called "Real Mode," which was simple and direct, but offered no protection.

### Physical Memory & Addressing

- **Address Bus:** 20-bit
    
- **Maximum Physical Memory:** 2^20 bytes = **1 Megabyte (MB)**
    
- **How it Looks:** Imagine 1MB of RAM chips on a motherboard. The 8086 can address any byte within this space directly. There is **no concept of virtual memory**. What you address is what you get.
    
- **Physical Chips:** To get 1MB, manufacturers would use various combinations of RAM chips available at the time, like sixteen 64KB chips.
    

### The `segment:offset` Model

The 8086 has 16-bit registers, which can only address 2^16 = 64KB. To access the full 1MB, it uses a clever trick with segmentation. A logical address is composed of two 16-bit parts: a **segment** and an **offset**.

- **Segment Registers (CS, DS, SS, ES):** These registers hold a 16-bit segment value.
    
- **Offset:** This is a 16-bit value, often from a pointer register like IP (Instruction Pointer) or SI (Source Index).
    

The processor calculates the 20-bit physical address like this: **`Physical Address = (Segment * 16) + Offset`**

Multiplying the segment by 16 (or shifting it left by 4 bits) effectively gives you a 20-bit base address. The offset is then added to get the final location.

**How Memory "Looks" to a Program:** A program sees memory as a collection of 64KB segments. The OS sets up the segment registers (CS for Code, DS for Data, SS for Stack) to point to the base of these areas within the 1MB physical space. These segments can overlap.

### Multiprocessing on the 8086

There is **no hardware support for memory protection**.

- When one program is running, it can read or write to _anywhere_ in the 1MB of memory, including the operating system's code or the memory of other loaded programs (like Terminate-and-Stay-Resident programs in MS-DOS).
    
- A faulty program could easily crash the entire system.
    
- The memory layout is just one flat space shared by everything.
    

## Part 2: The 80286 — Protected Mode (Building Fences)

The 80286 introduced **Protected Mode**, a revolutionary change designed to support multitasking operating systems. It was backward-compatible and could still run in Real Mode.

### Physical and Virtual Memory

- **Address Bus:** 24-bit
    
- **Maximum Physical Memory:** 2^24 bytes = **16 MB**
    
- **Virtual Memory:** The 80286 introduced the concept of virtual memory. Each process could have its own virtual address space of up to **1 Gigabyte (GB)**. However, this was limited because all of it had to be mapped into the 16MB of physical RAM; there was no hardware support for swapping memory to disk (paging).
    

### Selectors, Descriptors, and Tables

This is where the terms you mentioned come in. The `segment:offset` model changes meaning in Protected Mode. The segment register no longer holds a base address; it holds a **Selector**.

1. **Selector:** A 16-bit value that acts as an _index_ into a lookup table. It "selects" an entry.
    
2. **Descriptor Table (GDT/LDT):** A table in memory that holds detailed information about each memory segment. There is one Global Descriptor Table (GDT) for the OS and can be many Local Descriptor Tables (LDTs), typically one per process.
    
3. **Descriptor:** An 8-byte entry in the table. The descriptor contains the actual **24-bit base address** of the segment, its size (**limit**), and crucial **access rights** (e.g., read-only, executable).
    

The address translation process is now indirect:

**`Selector -> Descriptor Table -> Descriptor (finds base address) + Offset = Physical Address`**

### Multiprocessing on the 80286

This new model is the key to memory protection.

- The OS sets up a separate LDT for each process.
    
- When Process A is running, its selectors can only point to entries in its own LDT. The hardware checks the descriptor's limit and access rights on every memory access.
    
- **Result:** Process A is physically prevented by the CPU from accessing memory belonging to Process B or the OS. If it tries, it causes a hardware exception (a "protection fault").
    

## Part 3: The 80386 — 32-bit & Paging (The Modern Blueprint)

The 80386 was a massive leap forward. It extended the architecture to 32 bits and, most importantly, added **paging**.

### Physical and Virtual Memory

- **Address Bus:** 32-bit
    
- **Maximum Physical Memory:** 2^32 bytes = **4 Gigabytes (GB)**
    
- **Virtual Memory:** Each process gets its own private **4 GB** virtual address space.
    
- **Key Innovation:** With paging, parts of this virtual space can be "paged out" to a hard disk, allowing programs to use much more memory than is physically available.
    

### Paging: The Final Layer of Abstraction

The 80386 still uses the segmentation model from the 80286, but it adds another translation layer _after_ it.

1. The `selector:offset` logic works as before, producing what is now called a **Linear Address**. In the 80386's flat memory model (used by modern OSes), the segment base is just 0, so the offset _is_ the linear address.
    
2. This 32-bit linear address is then processed by the **Paging Unit**.
    
3. The Paging Unit breaks the linear address space into fixed-size blocks called **pages** (typically 4KB). It uses **Page Tables** (managed by the OS) to map each virtual page to a physical **page frame** in RAM.
    

The full address translation is: **`Selector:Offset -> (Segmentation) -> Linear Address -> (Paging) -> Physical Address`**

### Multiprocessing on the 80386

Paging revolutionizes multitasking:

- Each process gets its own independent set of page tables, giving it a clean, private 4GB linear address space.
    
- A process's memory can be scattered all over physical RAM in non-contiguous 4KB chunks. The paging hardware handles the mapping, so the process still sees it as a single, contiguous block.
    
- The OS can swap unused pages to disk and load them back when needed, providing true virtual memory.
    

### Summary Comparison

|Feature|8086 (Real Mode)|80286 (Protected Mode)|80386 (32-bit Protected Mode)|
|---|---|---|---|
|**Address Bus**|20-bit|24-bit|32-bit|
|**Max Physical RAM**|1 MB|16 MB|4 GB|
|**Max Virtual Address Space**|None (1 MB Physical)|1 GB per task|4 GB per task (up to 64 TB with segmentation)|
|**Address Translation**|`(Segment * 16) + Offset`|`Selector -> Descriptor Table -> Base + Offset`|`Selector -> Linear Address -> Page Tables -> Physical`|
|**Memory Protection**|**No**|**Yes**, via Segment Limits & Rights|**Yes**, via Segments and Page-level permissions|
|**Key Innovation**|Segmented memory model|Protected Mode, Memory Protection|32-bit architecture, **Paging**|

This evolution from a simple, flat memory model to a protected, segmented, and finally paged virtual memory system is what made modern, stable multitasking operating systems like Linux and Windows possible.