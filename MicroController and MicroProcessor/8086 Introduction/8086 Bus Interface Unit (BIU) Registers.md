# 8086 Bus Interface Unit (BIU) Registers

**Tags:** #microprocessor #8086 #registers #BIU #segmentation

The Bus Interface Unit (BIU) contains the registers that are dedicated to memory addressing. They are essential for implementing the [[8086 Memory Organization|segmented memory model]]. A programmer can't perform arithmetic on these registers; their only job is to point to locations in memory.

### Segment Registers

There are four 16-bit segment registers. Each one defines the starting address of a 64KB memory segment. A program can have four distinct segments active at any one time.

- **`CS` (Code Segment):** This is the most important segment register. It points to the base of the 64KB segment that contains the program instructions currently being executed. Its value is combined with the `IP` register to find the next instruction.
    
- **`DS` (Data Segment):** Points to the base of the segment where program variables and data are typically stored. Most memory access instructions default to using the `DS` register.
    
- **`SS` (Stack Segment):** Points to the base of the segment used for the program's stack. All stack operations (like `PUSH`, `POP`, `CALL`, `RET`) implicitly use the `SS` register in their address calculations, along with `SP` or `BP`.
    
- **`ES` (Extra Segment):** An additional data segment pointer. It's primarily used by string instructions (`MOVS`, `CMPS`) to point to the destination memory location.
    

### Instruction Pointer (IP)

- **`IP` (Instruction Pointer):** This 16-bit register is the "offset" part of the `CS:IP` pair. It always holds the address of the _next instruction to be fetched_ relative to the start of the current Code Segment.
    
- You cannot directly modify the `IP` with a `MOV` instruction. Its value is changed automatically as instructions are executed, or explicitly by control-flow instructions like `JMP`, `CALL`, and `RET`.
    

The `CS:IP` combination is fundamental to how the 8086 executes a program. `CS` sets the 64KB "page" of code, and `IP` points to the specific line on that page.

**Links:** [[8086 Memory Organization]], [[8086 Internal Architecture - BIU and EU]]