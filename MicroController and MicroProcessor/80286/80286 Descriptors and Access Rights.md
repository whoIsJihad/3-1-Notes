# 80286 Descriptors and Access Rights

**Tags:** #80286 #protected_mode #memory_management

A **Descriptor** is an 8-byte (64-bit) data structure that defines a single memory segment in Protected Mode. It contains all the information the CPU's Memory Management Unit (MMU) needs to access and protect that segment.

An 80286 descriptor is composed of three main parts:

1. **Base Address (24 bits):**
    
    - This specifies the 24-bit physical starting address of the memory segment.
        
    - Unlike in Real Mode where segments must start on a 16-byte "paragraph" boundary, in Protected Mode a segment can start at **any byte address** in the 16 MB memory space.
        
2. **Limit (16 bits):**
    
    - This specifies the size of the segment. The limit is a 16-bit value, so a segment can be anywhere from 1 byte to 65,536 bytes (64 KB) in size.
        
    - The CPU uses this value for bounds checking. If a program tries to access memory using an offset that is greater than the limit, the CPU will generate a protection fault. This is the hardware mechanism that prevents buffer overflows from corrupting adjacent memory.
        
3. **Access Rights Byte (8 bits):**
    
    - This byte is a collection of flags that defines the type of segment and the rules for accessing it. It is the heart of the 80286's protection mechanism.
        

### Decoding the Access Rights Byte

- **`P` (Present - bit 7):** If `P=1`, the segment is currently present in physical RAM. If `P=0`, the segment is not in RAM (it may have been swapped to disk by the OS). Accessing a non-present segment triggers a fault, which the OS can use to implement virtual memory.
    
- **`DPL` (Descriptor Privilege Level - bits 5-6):** A 2-bit field specifying the privilege level (`00` to `11`) of the segment itself. A program can only access a segment if its Current Privilege Level (CPL) is more or equally privileged as the DPL.
    
- **`S` (Segment Type - bit 4):** Differentiates between system segments (`S=0`, e.g., descriptor tables themselves) and application segments (`S=1`, for code and data).
    
- **`E` (Executable - bit 3):**
    
    - If `E=1`, this is a **Code Segment**.
        
    - If `E=0`, this is a **Data Segment** (which includes stacks).
        
- **`R/W` (Readable/Writable - bit 1):**
    
    - For a **Data Segment** (`E=0`): If `W=1`, the segment is writable. If `W=0`, it's read-only.
        
    - For a **Code Segment** (`E=1`): If `R=1`, the code segment can be read (allowing constants to be stored with code). If `R=0`, it is execute-only.
        
- **`A` (Accessed - bit 0):** The CPU automatically sets this bit to `1` whenever the segment is accessed. The OS can periodically clear this bit to track which segments are actively being used, which is useful for memory management algorithms (like deciding which pages to swap out).
    

These hardware-enforced rules allow an operating system to build a secure environment where programs are isolated and system integrity is maintained.

---
For further info about this note read [[80286 Descriptors and Access Rights (A Deep Dive)]]
**Links:** [[The Intel 80286 - Bridge to Modern Computing]]