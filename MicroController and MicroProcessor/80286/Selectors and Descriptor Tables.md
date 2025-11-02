# Selectors and Descriptor Tables

**Tags:** #80286 #protected_mode #memory_management

In Protected Mode, the simple `Segment:Offset` addressing of the 8086 is replaced by a more powerful, three-part logical address: **`Selector:Offset`**. The segment registers (`CS`, `DS`, etc.) no longer hold the base address of a segment. Instead, they hold a 16-bit **Selector**.

### The Role of the Selector

A Selector is an "index" that tells the CPU where to find the _real_ information about a memory segment. It doesn't describe the segment itself, but rather points to an entry in a data structure called a **Descriptor Table**.

A 16-bit selector is composed of three parts:

- **Index (13 bits):** Specifies the entry number (from 0 to 8191) within the descriptor table.
    
- **`TI` (Table Indicator - 1 bit):**
    
    - `TI = 0`: Use the **Global Descriptor Table (GDT)**.
        
    - `TI = 1`: Use the **Local Descriptor Table (LDT)**.
        
- **`RPL` (Requested Privilege Level - 2 bits):** Specifies the privilege level the program is _requesting_ for this memory access. The CPU compares this to its own current privilege level and the segment's privilege level to enforce protection.
    

### Descriptor Tables: The Map of Memory

A Descriptor Table is a data structure in memory, created and managed by the operating system. It acts as the central map defining all memory segments available to the system. Each entry in the table is an 8-byte **Descriptor**.

The 80286 uses two main types of descriptor tables:

1. **Global Descriptor Table (GDT):**
    
    - There is **only one** GDT in the entire system.
        
    - It holds descriptors that are global to all programs ("tasks"). This typically includes segments for the OS kernel, video memory, and other system-wide resources.
        
    - The physical memory address and size of the GDT are stored in a special CPU register called the **`GDTR` (Global Descriptor Table Register)**.
        
2. **Local Descriptor Table (LDT):**
    
    - Each **task or process** can have its own LDT.
        
    - It holds descriptors that are private to that specific program, such as its own code, data, and stack segments.
        
    - This provides isolation: one program cannot see or access the segments defined in another program's LDT.
        
    - The current LDT is pointed to by another special register, the **`LDTR`**.
        

### The Address Translation Process

When you execute an instruction like `MOV AX, [SI]`, the CPU's Address Unit (MMU) performs the following steps automatically in hardware:

1. It takes the **Selector** from the `DS` register.
    
2. It checks the `TI` bit to determine whether to use the GDT or the LDT.
    
3. It reads the base address of the chosen table from the `GDTR` or `LDTR`.
    
4. It uses the **Index** from the selector to locate the correct 8-byte **Descriptor** within that table.
    
5. It reads the base address, limit, and access rights from the descriptor.
    
6. It performs security checks (e.g., privilege levels, checking if the `Offset` from `SI` is within the segment's limit).
    
7. If all checks pass, it adds the **Base Address** from the descriptor to the **Offset** from `SI` to form the final 24-bit physical address.
    

This indirect, table-based lookup is the core mechanism of protected mode addressing.

- **Links:** [[The Intel 80286(index)]]
- Deep Dive Link : [[A deeper dive into Selector and Descriptor]]
- 
		