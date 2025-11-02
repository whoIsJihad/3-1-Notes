# 80386 Register Set: A Practical Guide

**Tags:** #80386 #registers #eax #data_types #assembly

The 80386's primary upgrade was its move to a full 32-bit architecture, and this is most visible in its register set. While the registers were expanded, they were designed in a clever way to maintain perfect compatibility with older 16-bit (8086/80286) and 8-bit code. Understanding this layered design is key to understanding how the processor works with different data sizes.

### The Core Concept: Layered Registers for Compatibility and Efficiency

Think of the main 32-bit registers as containers, with smaller containers nested inside them. The largest, 32-bit container is the native size for the 80386, but you can choose to work with the smaller, inner containers if you're dealing with smaller pieces of data.

Let's visualize this with `EAX`, the primary accumulator register.

- **`EAX` (Extended Accumulator Register):** This is the full **32-bit** register. You use it when you're working with 32-bit numbers (like an `int` or `long` in C++).
    
- **`AX` (Accumulator Register):** This is the **16-bit** lower half of `EAX`. It's the same `AX` register from the 8086/80286. You use it when working with 16-bit data (like a `short int` in C++).
    
- **`AH` and `AL` (Accumulator High/Low):** These are the two **8-bit** halves of `AX`. `AL` is the lowest 8 bits, and `AH` is the next 8 bits. You use them when working with single bytes (like a `char` in C++).
    

This structure applies to `EBX`, `ECX`, and `EDX` as well. The other general-purpose registers (`ESI`, `EDI`, `EBP`, `ESP`) are 32-bit but can also be accessed by their 16-bit names (`SI`, `DI`, `BP`, `SP`).

### Data Flow Simulation: Where Data Comes From and Goes

Data moves between memory and registers, or between registers themselves. The instruction you use (`MOV`) and the register you choose determine the size of the data being moved.

#### Simulation 1: Loading Data of Different Sizes from Memory

Let's assume we have these variables defined in our data segment:

```
.DATA
VAR_BYTE  DB 12h                  ; A single byte (like a char)
VAR_WORD  DW 1234h                ; A 16-bit word (like a short)
VAR_DWORD DD 12345678h            ; A 32-bit double word (like an int)
```

**Scenario A: Moving a byte** `MOV AL, VAR_BYTE`

- **Source:** The 1-byte value `12h` from the memory location `VAR_BYTE`.
    
- **Destination:** The 8-bit `AL` register.
    
- **Result:** `EAX` now looks like `xxxxxx12h`. The upper 24 bits of EAX are **unaffected**.
    

**Scenario B: Moving a word** `MOV AX, VAR_WORD`

- **Source:** The 2-byte value `1234h` from the memory location `VAR_WORD`.
    
- **Destination:** The 16-bit `AX` register.
    
- **Result:** `EAX` now looks like `xxxx1234h`. The upper 16 bits of EAX are **unaffected**. `AX` is now `1234h`, which means `AH` is `12h` and `AL` is `34h`.
    

**Scenario C: Moving a double word** `MOV EAX, VAR_DWORD`

- **Source:** The 4-byte value `12345678h` from memory.
    
- **Destination:** The full 32-bit `EAX` register.
    
- **Result:** `EAX` is now `12345678h`. The entire register is overwritten.
    

#### Simulation 2: How Modifying a Subdivision Affects the Whole

This is the most critical concept to grasp. The subdivisions are not separate registers; they are just different ways of accessing the _same physical piece of silicon_.

**Initial State:** `EAX` contains `11223344h`.

- `EAX = 11223344h`
    
- `AX = 3344h`
    
- `AH = 33h`
    
- `AL = 44h`
    

**Action 1: Change `AL`** Instruction: `MOV AL, 99h`

- **Result:** Only the lowest 8 bits are changed.
    
    - `EAX = 11223399h` (Notice the `44` became `99`)
        
    - `AX = 3399h`
        
    - `AH = 33h`
        
    - `AL = 99h`
        

**Action 2: Now, change `AX`** Instruction: `MOV AX, 00BBh`

- **Result:** The entire lower 16 bits are overwritten. The upper 16 bits of `EAX` are untouched.
    
    - `EAX = 112200BBh` (Notice the `3399` was completely replaced)
        
    - `AX = 00BBh`
        
    - `AH = 00h`
        
    - `AL = BBh`
        

**Action 3: Finally, load `EAX`** Instruction: `MOV EAX, 0`

- **Result:** The entire 32-bit register is overwritten with zeros.
    
    - `EAX = 00000000h`
        
    - `AX = 0000h`
        
    - `AH = 00h`
        
    - `AL = 00h`
        

### System and Control Registers: The OS-Hardware Interface

The 80386 introduced a powerful new set of registers that are not used for general programming but are critical for the operating system to manage the processor's advanced features. These are accessible only from the highest privilege level (Ring 0), ensuring that only the OS kernel can modify the fundamental state of the machine.

#### Control Registers (CR0, CR1, CR2, CR3)

These registers control the processor's core operating mode and memory management features.

|Register|Name|In-Depth Purpose & OS Connection|
|---|---|---|
|**`CR0`**|Control Register 0|This is the master switchboard. It contains several bit flags, the two most important being: - **`PE` (Protection Enable, bit 0):** Setting this bit switches the CPU from Real Mode to **Protected Mode**. - **`PG` (Paging Enable, bit 31):** Setting this bit (while in Protected Mode) turns on the **Paging Unit**. This is the final step in enabling a modern virtual memory system. The OS carefully sets this bit during the boot process.|
|**`CR1`**|_(Reserved)_|This register is unused in the 80386 and was reserved for future processors.|
|**`CR2`**|Page-Fault Linear Address|When a **page fault** occurs (i.e., the Paging Unit can't find a valid mapping for a linear address), the CPU hardware automatically saves the full 32-bit linear address that caused the fault into `CR2`. **OS Connection:** The OS's page fault handler reads `CR2` to know which page it needs to load from the disk into a physical frame. This is a direct hardware assist for implementing demand paging, a core concept from your OS course.|
|**`CR3`**|Page Directory Base Register (PDBR)|This register holds the 32-bit **physical base address** of the Page Directory for the currently running task. **OS Connection:** When the OS performs a **context switch** from one process to another, one of its key jobs is to load the `CR3` register with the physical address of the _next process's_ Page Directory. This single action instantly remaps the entire 4 GB virtual address space, a fundamental step in process isolation.|

#### System Address Registers

These registers tell the CPU where to find the critical memory management data structures (the descriptor tables). They function like their 80286 counterparts but are now capable of holding full 32-bit base addresses.

|Register|Name|Purpose|
|---|---|---|
|**`GDTR`**|Global Descriptor Table Register|Holds the 32-bit linear base address and 16-bit limit for the GDT.|
|**`IDTR`**|Interrupt Descriptor Table Register|Holds the 32-bit linear base address and 16-bit limit for the IDT.|
|**`LDTR`**|Local Descriptor Table Register|Holds a 16-bit **selector** that points to the LDT's descriptor within the GDT.|
|**`TR`**|Task Register|Holds a 16-bit **selector** that points to the current Task State Segment (TSS) descriptor in the GDT, which is crucial for hardware-assisted multitasking.|

#### Debug Registers (DR0-DR7)

A significant enhancement for developers. While software debuggers use `INT 3` (breakpoint interrupts), these hardware registers allow for much more powerful debugging.

- `DR0-DR3`: Can hold linear addresses for breakpoints.
    
- `DR7` (Debug Control): Configures the type of breakpoint. You can set it to trigger not just on instruction execution, but on **data write** or even **data read/write** at a specific address. This is invaluable for finding memory corruption bugs where a variable is being changed unexpectedly.
    
- `DR6` (Debug Status): Reports which breakpoint condition was met.
    

**Links:** [[The Intel 80386 - Dawn of 32-bit Computing]]