

**Tags:** #8086 #addressing_modes #stack #control_flow

In addition to data addressing, the 8086 has specialized addressing rules for program control flow (`JMP`, `CALL`) and stack operations (`PUSH`, `POP`). The instruction itself implies which segment register to use, simplifying the process.

### Program Memory Addressing Modes

These modes are used by `JMP` (Jump) and `CALL` (Call Procedure) instructions to change the flow of execution by modifying the `CS` and `IP` registers.

- **Direct Program Addressing:**
    
    - The target address is encoded directly into the instruction.
        
    - **Example:** `JMP 1000:2000H`
        
    - **How it works:** This is a **far jump**. The CPU directly loads `1000H` into `CS` and `2000H` into `IP`.
        
- **Relative Program Addressing:**
    
    - A signed 8-bit or 16-bit displacement is encoded in the instruction. This displacement is added to the _current_ `IP`.
        
    - **Example:** `JMP SHORT_LABEL`
        
    - **How it works:** This is a **near jump**. The assembler calculates the distance from the current instruction to `SHORT_LABEL`. The CPU adds this distance to `IP`. `CS` is not changed. This makes the code relocatable.
        
- **Indirect Program Addressing:**
    
    - The instruction points to a register or memory location that _contains_ the target address.
        
    - **Example 1:** `JMP AX`
        
        - The CPU copies the 16-bit value from `AX` directly into `IP`.
            
    - **Example 2:** `JMP WORD PTR [SI]`
        
        - The CPU calculates the memory address `DS:SI`, reads the 16-bit word from that location, and loads that word into `IP`.
            

### Stack Memory Addressing Mode

Stack operations always use the Stack Segment (`SS`) register by default. The `SP` (Stack Pointer) register holds the offset to the "top" of the stack.

- **Example:** `PUSH AX`
    
- **How it works:** The 8086 does not need an address specified in the instruction. The `PUSH` opcode implies the following actions:
    
    1. Decrement `SP` by 2 (the stack grows downwards in memory).
        
    2. Calculate the physical address `SS:SP`.
        
    3. Write the 16-bit contents of the `AX` register to that memory location.
        

A `POP` operation does the reverse: it reads the value from `SS:SP` and then increments `SP` by 2. This implicit use of `SS:SP` is a unique addressing mode dedicated to the stack.

**Links:** [[8086 Instruction Encoding and Addressing Modes]]