# 80386 Operating Modes

**Tags:** #80386 #operating_modes #real_mode #protected_mode #virtual_86_mode

The 80386 supports three distinct modes of operation, allowing it to run everything from legacy DOS programs to modern, fully protected multitasking operating systems.

### 1. Real Address Mode

- **Purpose:** To provide 100% backward compatibility with the 8086 and 8088.
    
- **Functionality:** When the 80386 is powered on or reset, it starts in Real Mode. In this mode, it behaves like a very fast 8086, but with access to 32-bit registers.
    
- **Memory Addressing:** Uses the classic `Segment:Offset` scheme to generate a 20-bit physical address. The memory space is limited to **1 MB**.
    
- **Protection:** There is no memory protection. Any program can write to any memory location.
    

### 2. Protected Mode

- **Purpose:** This is the native, fully-featured mode of the 80386.
    
- **Functionality:** It enables all the advanced features of the processor, including memory protection, paging, and multitasking.
    
- **Memory Addressing:** Uses the `Selector:Offset` model. The CPU can access its entire **4 GB** physical address space. Segments can be up to 4 GB in size.
    
- **Key Features:**
    
    - **Segmentation:** Provides memory isolation between tasks.
        
    - **Paging (Optional):** Provides virtual memory, allowing the OS to map a large logical address space onto a smaller physical RAM.
        
    - **Privilege Levels:** Enforces four privilege rings (0-3) to protect the OS from application code.
        

### 3. Virtual 86 Mode (VM86)

- **Purpose:** To solve the biggest limitation of the 80286: its inability to easily run Real Mode programs once in Protected Mode. VM86 mode allows an 8086 program to run as a **task** _within_ the Protected Mode environment.
    
- **Functionality:** A program running in VM86 mode thinks it is on a standard 8086. It uses `Segment:Offset` addressing and is limited to 1 MB of memory.
    
- **The "Virtual" Trick:** The OS can use the **Paging Unit** to map this 1 MB virtual space anywhere within the 80386's 4 GB physical memory. This allows the OS to run multiple DOS applications simultaneously, each believing it has exclusive access to the first megabyte of memory, while in reality they are safely isolated from each other and from the OS kernel.
    
- **Protection:** If a VM86 program tries to access hardware directly or execute a privileged instruction, it triggers a fault. This "traps" the operation, handing control back to the Protected Mode OS, which can then decide whether to permit, deny, or emulate the action.
    

This ability to switch seamlessly between modes and to virtualize the real-mode environment was the key that allowed operating systems like Windows 3.x and OS/2 to provide backward compatibility while building a modern, protected foundation.

**Links:** [[The Intel 80386 - Dawn of 32-bit Computing]]