# 80386 Register Set

**Tags:** #80386 #registers #eax

The 80386 extended the register set of the 80286 to a full 32 bits, providing significantly more power and flexibility. The new 32-bit registers are known as **extended registers** and are prefixed with an 'E'.

### General-Purpose Registers

The eight general-purpose registers were extended to 32 bits. Crucially, they maintained backward compatibility by allowing access to their 16-bit and 8-bit subdivisions.

|32-bit (Extended)|16-bit (Standard)|8-bit High|8-bit Low|Primary Use|
|---|---|---|---|---|
|**EAX**|`AX`|`AH`|`AL`|Accumulator for arithmetic|
|**EBX**|`BX`|`BH`|`BL`|Base register for memory addressing|
|**ECX**|`CX`|`CH`|`CL`|Counter for loops and strings|
|**EDX**|`DX`|`DH`|`DL`|Data/I/O, used with EAX for 64-bit ops|
|**ESI**|`SI`|-|-|Source Index for memory/strings|
|**EDI**|`DI`|-|-|Destination Index for memory/strings|
|**EBP**|`BP`|-|-|Base Pointer for stack frame access|
|**ESP**|`SP`|-|-|Stack Pointer|

### Segment Registers

The six segment registers remained 16-bit, as they hold **Selectors**, not addresses. Two new data segment registers were added for extra flexibility.

- `CS` (Code Segment)
    
- `DS` (Data Segment)
    
- `SS` (Stack Segment)
    
- `ES` (Extra Segment)
    
- **`FS` (New Data Segment)**
    
- **`GS` (New Data Segment)**
    

### Instruction Pointer and Flags

- **EIP (Extended Instruction Pointer):** A 32-bit register that holds the offset of the next instruction to be executed.
    
- **EFLAGS (Extended Flags Register):** A 32-bit register. It contains all the 80286 flags plus new flags for advanced features:
    
    - **`VM` (Virtual 86 Mode):** When set, enables Virtual 86 Mode.
        
    - **`RF` (Resume Flag):** Used for debugging to control breakpoint resumption.
        

### System and Control Registers

The 80386 introduced several new registers, accessible only at the highest privilege level (Ring 0), for managing the system's state.

- **Control Registers (`CR0`-`CR3`):**
    
    - `CR0`: Contains global system flags, including the **`PE` (Protection Enable)** bit and the crucial **`PG` (Paging Enable)** bit.
        
    - `CR2`: Stores the linear address that caused the last **page fault**.
        
    - `CR3`: Holds the physical base address of the **Page Directory** for the current task. Also known as the Page Directory Base Register (PDBR).
        
- **Debug Registers (`DR0`-`DR7`):** Provided hardware support for advanced debugging, allowing breakpoints on data access, not just code execution.
    
- **System Address Registers:** `GDTR`, `LDTR`, `IDTR`, `TR` (same function as in 80286, but now able to handle 32-bit base addresses).
    

**Links:** [[The Intel 80386 - Dawn of 32-bit Computing]]

For a deeper dive read -  [[80386 Register Set - A Practical Guide]] 