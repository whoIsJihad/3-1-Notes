# Procedures and the CALL/RET Pattern

**Tags:** #assembly #functions #stack #control_flow

A **procedure** (also known as a subroutine or function) is a named block of code that can be executed from different points in a program. Using procedures is the key to writing modular, reusable, and organized assembly code. The stack is the mechanism that makes procedures possible.

### Defining a Procedure

You define a procedure using the `PROC` and `ENDP` assembler directives.

```
procedure_name  PROC
    ; Body of the procedure goes here
    ...
    RET   ; Return to the caller
procedure_name  ENDP
```

- The `RET` (Return) instruction is essential for ending the procedure and giving control back to the code that called it.
    

### The `CALL` and `RET` Instructions

This pair of instructions manages the entire procedure-call mechanism.

- **`CALL procedure_name`**
    
    - **Action:** This instruction performs two critical steps:
        
        1. It automatically **pushes the return address** onto the stack. The return address is the address of the very next instruction _after_ the `CALL`.
            
        2. It performs an unconditional jump to the first instruction of the procedure.
            
- **`RET` (Return)**
    
    - **Action:** This instruction does the reverse:
        
        1. It automatically **pops the return address** from the top of the stack.
            
        2. It loads this address into the `IP` (Instruction Pointer), causing execution to resume right after the original `CALL`.
            

**Simulation of `CALL` and `RET`:**

1. **Before `CALL`:** The `IP` points to the `CALL MY_PROC` instruction at address `0100h`. The instruction after it is at `0103h`. The stack pointer `SP` is at `0200h`.
    
2. **During `CALL`:** The CPU pushes the return address (`0103h`) onto the stack. `SP` becomes `01FEh`. The CPU then jumps to `MY_PROC`, loading its starting address into `IP`.
    
3. **Inside the Procedure:** The procedure's code executes.
    
4. **During `RET`:** The CPU pops the value `0103h` from the stack into `IP`. `SP` goes back to `0200h`.
    
5. **After `RET`:** Execution has now seamlessly resumed at address `0103h`, right where it left off.
    

This automatic saving and restoring of the return address on the stack is what allows us to call a procedure from anywhere and always return to the correct place.

**Links:** [[Advanced Assembly Concepts]]