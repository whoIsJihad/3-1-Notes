
---


**Tags:** #80286 #protected_mode #operating_systems #memory_management

**Protected Mode** is the native, powerful operating state of the 80286. It fundamentally changes how the CPU accesses memory, moving from a simple, direct addressing scheme to a sophisticated, indirect one managed by the hardware. Its name comes from its primary purpose: to **protect** the operating system from user applications, and to protect user applications from each other.

### Why Was Protected Mode Necessary? The Problems of Real Mode

The 8086's Real Mode had critical limitations that made it unsuitable for building a robust multitasking operating system:

1. **No Memory Protection:** Any program could write to any memory location. A buggy application could easily overwrite the operating system's memory, crashing the entire machine. This is why a single bad program in MS-DOS could force a reboot.
    
2. **Limited Memory (1 MB):** The `Segment:Offset` scheme was physically limited to 1 MB of RAM, which was quickly becoming insufficient.
    
3. **No Privilege Levels:** All code, whether it was the OS kernel or a simple application, ran with the same privileges. An application could execute hardware instructions (like `HLT` to halt the CPU) and compromise system stability.
    

### The Solutions Offered by Protected Mode

Protected Mode solves these problems by introducing a layer of hardware-enforced rules for memory access. The CPU's on-chip **Memory Management Unit (MMU)** becomes the gatekeeper for every memory request.

1. **Memory Protection:** The CPU checks every memory access to ensure it is valid.
    
    - **Segment Limits:** A program cannot access memory outside of its allocated segments. An attempt to do so results in a **protection fault** (an exception handled by the OS) instead of corrupting memory.
        
    - **Access Rights:** Segments can be marked as read-only, or as code-only (not writable). This prevents common bugs like accidentally overwriting program instructions.
        
2. **Extended Memory Access:** The new addressing mechanism can generate 24-bit physical addresses, allowing access to the full **16 MB** of physical RAM.
    
3. **Privilege Levels:** The hardware enforces a "ring" protection model. The OS kernel runs at the most privileged level (Ring 0), while applications run at a less privileged level (e.g., Ring 3). Critical instructions and memory areas are only accessible to code running at higher privilege levels.
    

Instead of directly pointing to memory, the segment registers in Protected Mode hold a special value called a **Selector**. This selector doesn't point to memory itself, but rather to an entry in a data structure called a **Descriptor Table**, which is the core of this new memory model.

**Links:** [[The Intel 80286(index)]]