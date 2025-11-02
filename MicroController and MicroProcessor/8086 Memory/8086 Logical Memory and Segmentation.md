# 8086 Logical Memory and Segmentation

**Tags:** #8086 #memory #segmentation #addressing #operating_systems

While the physical memory is a banked 1MB space, a programmer using the 8086 does not think about physical addresses like `12345H`. Instead, they interact with a **logical address space** defined by a powerful concept called **segmentation**.

### The Core Problem and Solution

- **Problem:** The 8086 is a 16-bit CPU. All its internal address-handling registers (like the Instruction Pointer and general-purpose registers) are only 16 bits wide. A 16-bit register can only access 2^16 = 65,536 bytes (64 KB) of memory. How can it possibly access its full 1MB (2^20 bytes) address space?
    
- **Solution:** Segmentation. The 1MB memory is divided into overlapping logical **segments**. A programmer can access any location in memory by defining two 16-bit values:
    
    1. **Segment Address:** A 16-bit value that defines the **starting point** of a 64 KB memory block. This is stored in a dedicated **Segment Register** (CS, DS, SS, ES).
        
    2. **Offset Address:** A 16-bit value that specifies the **distance from the start** of that segment to the target memory location. This is often stored in a general-purpose register or pointer register (e.g., IP, BX, SI).
        

This `Segment:Offset` pair forms the complete logical address.

### The Paragraph Boundary Rule

A segment doesn't start at just any random byte. The segment start address is determined by the value in a segment register. Because of how the hardware calculates the physical address (by shifting the segment value), a new segment can only begin every 16 bytes. This 16-byte boundary is known as a **paragraph**.

This means a segment can start at `00000H`, `00010H`, `00020H`, etc., but **not** at an address like `00018H`.

**Links:** [[Calculating Physical Addresses]], [[Advantages of Segmentation - Relocatable Code]]