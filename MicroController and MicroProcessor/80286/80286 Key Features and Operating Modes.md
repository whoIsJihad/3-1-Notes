
---

**Tags:** #80286 #cpu_architecture #real_mode #protected_mode

The 80286 introduced several major advancements over the 8086, most notably its on-chip memory management unit (MMU) and two distinct operating modes.

### Key Hardware Upgrades

- **Address Bus:** Expanded to **24 bits**, allowing the CPU to physically address up to **16 MB** of memory (a 16x increase over the 8086's 1 MB).
    
- **Virtual Memory:** Capable of managing up to **1 GB** of virtual memory for each task, a concept where the OS and hardware make the system seem like it has more memory than it physically does by swapping data to disk.
    
- **Clock Speed:** Available in faster clock speeds (8 MHz to 12.5 MHz), making it significantly faster than the 8086 even when running the same code.
    
- **Specialized Instructions:** Included new instructions designed specifically for operating systems to handle multitasking efficiently (e.g., a single instruction to manage a context switch).
    

### The Two Operating Modes

The 80286's most defining feature was its dual-mode personality, controlled at boot time.

#### 1. Real Address Mode

- **Purpose:** To provide 100% backward compatibility with the 8086.
    
- **Functionality:** In this mode, the 80286 behaves exactly like a very fast 8086.
    
    - It can only access the first **1 MB** of memory.
        
    - It uses the same `Segment:Offset` scheme to generate a 20-bit physical address.
        
    - All advanced memory protection and management features are **disabled**.
        
- **Compatibility:**
    
    - **Object Code Compatible:** An executable file (`.exe` or `.com`) compiled for an 8086 will run on an 80286 in Real Mode without modification.
        
    - **Source Code Compatible:** Assembly source code written for the 8086 can be re-assembled for the 80286.
        

#### 2. Protected Virtual Address Mode (Protected Mode)

- **Purpose:** To enable the new, advanced features of the CPU. This is the native mode of the 80286.
    
- **Functionality:**
    
    - **Full 16 MB Memory Access:** Can access the entire physical address space.
        
    - **Memory Management:** The on-chip MMU becomes active, translating logical addresses into physical addresses using a descriptor-based system.
        
    - **Memory Protection:** Enforces hardware-level protection, preventing one program from interfering with another program's memory or with the operating system itself. This is the cornerstone of a stable multitasking environment.
        

This dual-mode design was a critical, albeit complex, engineering decision that allowed the PC ecosystem to evolve while still running the vast library of existing DOS software.

**Links:** [[The Intel 80286(index)]]