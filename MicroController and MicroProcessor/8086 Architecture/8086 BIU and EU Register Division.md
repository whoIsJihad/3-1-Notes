# 8086 BIU and EU Register Division

**Tags:** #microprocessor #8086 #registers #biu #eu

To understand how the 8086 achieves parallelism, it's essential to know how its internal registers are divided between the Bus Interface Unit (BIU) and the Execution Unit (EU). Each unit has its own set of registers tailored to its specific function.

### Execution Unit (EU) Registers

The EU contains the registers related to data manipulation and program logic. These are the registers that programmers interact with most directly for arithmetic, logic, and data movement.

- **General-Purpose Registers:** `AX`, `BX`, `CX`, `DX`
    
- **Index and Pointer Registers:** `SP`, `BP`, `SI`, `DI`
    
- **Flags Register:** The `FLAGS` register that holds the status of operations.
    

Essentially, any register whose primary purpose is to hold data for processing resides in the EU.

### Bus Interface Unit (BIU) Registers

The BIU is responsible for all interactions with the memory, so its registers are dedicated to addressing. The BIU calculates the 20-bit physical address and manages the bus cycles.

- **Segment Registers:** `CS` (Code Segment), `DS` (Data Segment), `SS` (Stack Segment), `ES` (Extra Segment). Their primary job is to hold the base addresses of memory segments.
    
- **Instruction Pointer (IP):** The `IP` register holds the offset for the next instruction to be fetched within the code segment.
    

This separation is logical: the BIU handles the "where" (memory addresses), and the EU handles the "what" (data operations). The EU tells the BIU what address it needs to access, and the BIU handles the entire process of fetching or writing the data.

**Links:** [[8086 Execution and Timing Index Page]], [[8086 CPU Timing Cycles Explained]]