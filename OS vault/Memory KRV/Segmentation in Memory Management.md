# Segmentation in Memory Management

**Tags:** #os #memory-management #segmentation #virtual-memory #hardware

**Segmentation** is a memory management technique where the virtual address space of a process is not a single, contiguous entity, but a collection of logically separate address spaces called **segments**. Each segment corresponds to a logical unit of the program, such as code, stack, and heap.

This approach offers a more flexible model than simple base-and-bounds, as it allows the logical segments of an address space to be placed non-contiguously in physical memory, which helps in handling sparse address spaces efficiently.

### Address Translation with Segmentation

To translate a virtual address to a physical address, the hardware needs to know which segment the address belongs to and what the offset within that segment is.

- **Virtual Address Structure**: The virtual address is split into two parts: a **segment identifier** and an **offset** within that segment.
    
- **Hardware Registers**: For each segment, the hardware maintains a pair of registers: a **base** register (containing the starting physical address of the segment) and a **bounds** (or limit) register (containing the size of the segment).
    

The translation process is as follows:

1. Extract the segment identifier from the virtual address.
    
2. Use the identifier to find the corresponding base and bounds registers for that segment.
    
3. Extract the offset from the virtual address.
    
4. **Check for violation**: The hardware checks if `offset >= bounds`. If it is, a protection fault (segmentation fault) is triggered.
    
5. If the check passes, the physical address is calculated as: `Physical Address = base + offset`.
    

#### Example Translation

Consider a system with the following segment table: | Segment | Base | Size (Bounds) | | :------ | :---- | :------------ | | Code | 32K | 2K | | Heap | 34K | 2K | | Stack | 28K | 2K |

- **Translating Virtual Address `100` (in code segment):**
    
    - The address is in the code segment (let's assume virtual addresses 0-2K are code).
        
    - Offset = `100`.
        
    - Check: `100 < 2048`. The check passes.
        
    - Physical Address = `32768 + 100` = `32868`.
        
- **Translating Virtual Address `4200` (in heap segment):**
    
    - The heap segment starts at virtual address 4K (`4096`).
        
    - Offset = `4200 - 4096` = `104`.
        
    - Check: `104 < 2048`. The check passes.
        
    - Physical Address = `34816 + 104` = `34920`.
        

### The Problem of External Fragmentation

While segmentation solves the problem of internal fragmentation within the address space, it introduces a significant new problem: **external fragmentation**.

Over time, as segments are allocated and freed, the free space in physical memory gets broken up into small, non-contiguous holes. Eventually, the system may have enough total free memory to satisfy a request for a new segment, but it cannot be allocated because no single free block is large enough.

The only solution to external fragmentation is **compaction**. This involves stopping all running processes and having the OS move the allocated segments together in physical memory to consolidate the free holes into one large block. Compaction is an extremely heavyweight and costly operation, making it impractical for most modern systems.