
---


**Tags:** #80286 #protected_mode #memory_management #os_concepts

If a Selector is the "table of contents entry," then the **Descriptor** is the full page of information that entry points to. A Descriptor is an 8-byte (64-bit) data structure in memory that gives the CPU the complete "ID card" for a memory segment. It contains three critical pieces of information: where the segment starts, how big it is, and the rules for accessing it.

### The Visual Layout of an 80286 Descriptor

The 64 bits of a descriptor are not arranged arbitrarily. The CPU hardware is wired to expect specific information at specific byte offsets. Understanding this physical layout is key.

|Byte Offset|Bits 15-8 (High Byte)|Bits 7-0 (Low Byte)|Purpose|
|---|---|---|---|
|**0 and 1**|`Limit (L15-L8)`|`Limit (L7-L0)`|The 16-bit **Segment Limit** (size).|
|**2 and 3**|`Base (B15-B8)`|`Base (B7-B0)`|The lower 16 bits of the **Base Address**.|
|**4**|`Base (B23-B16)`|_Unused_|The upper 8 bits of the **Base Address**.|
|**5**|`Access Rights Byte`|_See breakdown below_|The 8-bit **Access Rights** flags.|
|**6 and 7**|`00000000`|`00000000`|Reserved for future processors (like the 80386).|

### Detailed Field Explanations

#### 1. Base Address (24 bits)

- **Purpose:** This defines the 24-bit physical starting address of the memory segment in the 16 MB address space.
    
- **Key Improvement:** Unlike the 8086, where segments had to start on a 16-byte boundary, the 80286's segments can start at **any byte address**. This provides much greater flexibility for the operating system's memory manager.
    

#### 2. Segment Limit (16 bits)

- **Purpose:** This defines the size of the segment. The value is the offset of the last accessible byte. A limit of `0000h` means a 1-byte segment, and `FFFFh` means a 64 KB segment.
    
- **The "Protection" in Protected Mode:** This field is the hardware basis for **bounds checking**. Before any memory access, the CPU's MMU compares the requested offset (e.g., the value in `SI`) against this limit. If `Offset > Limit`, the CPU immediately triggers a **General Protection Fault**, stopping the instruction and handing control to the OS. This hardware check is what prevents a program from reading or writing past its allocated memory, a common source of crashes and security vulnerabilities (like buffer overflows).
    

### 3. The Access Rights Byte: The Rulebook

This single byte is the heart of the 80286's protection mechanism. It's a collection of bit flags that tell the CPU the segment's type and who is allowed to do what with it.

|Bit|Name|Description|
|---|---|---|
|**7**|**P**|**Present**|
|**6-5**|**DPL**|**Descriptor Privilege Level**|
|**4**|**S**|**Segment Type**|
|**3**|**E**|**Executable**|
|**2**|**ED/C**|**Expansion Direction / Conforming**|
|**1**|**W/R**|**Writable / Readable**|
|**0**|**A**|**Accessed**|

#### Detailed Bit Breakdown

|Bit|Name|Function and OS Connection|
|---|---|---|
|**7**|**P (Present)**|**`1`**: The segment is currently in physical RAM. **`0`**: The segment is _not_ in RAM (it has been "paged out" or "swapped" to the hard disk). **OS Connection:** This is the fundamental hardware flag for implementing **virtual memory**. If the CPU tries to access a segment with `P=0`, it triggers a "Segment Not Present" fault. The OS's fault handler can then load the required data from the disk back into RAM, set `P=1`, and resume the program.|
|**6-5**|**DPL (Descriptor Privilege Level)**|A 2-bit value defining the segment's privilege "ring". **`00`**: Ring 0 (Highest privilege - for OS Kernel) **`01`**: Ring 1 **`10`**: Ring 2 **`11`**: Ring 3 (Lowest privilege - for Applications) **OS Connection:** This is the hardware enforcement of protection rings. A program running in Ring 3 cannot access a data segment with a DPL of `00`.|
|**4**|**S (Segment Type)**|**`1`**: An **Application Segment** (Code or Data/Stack). This is what programs use. **`0`**: A **System Segment** (e.g., a descriptor for an LDT or a Task State Segment). These are used by the OS and hardware for management tasks.|
|**3**|**E (Executable)**|**`1`**: This is a **Code Segment**. The CPU is allowed to fetch and execute instructions from it. **`0`**: This is a **Data/Stack Segment**. The CPU is _not_ allowed to execute instructions from it. **OS Connection:** This provides hardware-level prevention against executing data, a security feature known as Data Execution Prevention (DEP) or W^X.|
|**2**|**ED (Expansion Direction)** _if E=0 (Data)_|**`0`**: The segment expands **upwards**. An offset must be `Offset <= Limit`. This is used for normal data. **`1`**: The segment expands **downwards**. An offset must be `Offset > Limit`. This is used for stacks, which grow from high memory addresses to low ones.|
|**2**|**C (Conforming)** _if E=1 (Code)_|**`0`**: A standard code segment. It can only be called by code at the _same_ privilege level. **`1`**: A **conforming** code segment. It can be called by code from a _less_ privileged level, but it continues to run at the caller's (lesser) privilege level. Used for shared library functions that don't need kernel access.|
|**1**|**W (Writable)** _if E=0 (Data)_|**`1`**: The data segment is **writable**. **`0`**: The data segment is **read-only**. The hardware will fault if a write is attempted.|
|**1**|**R (Readable)** _if E=1 (Code)_|**`1`**: The code segment is **readable**. This allows constants to be stored alongside code. **`0`**: The code segment is **execute-only**. Any attempt to read from it (e.g., `MOV AX, [instruction_label]`) will fail.|
|**0**|**A (Accessed)**|**`0`**: The segment has not been accessed. **`1`**: The CPU sets this bit automatically whenever the segment is loaded into a segment register. **OS Connection:** The OS can periodically scan the descriptor tables and clear all the `A` bits. By checking later which bits have|