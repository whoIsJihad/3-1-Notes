# Dedicated 8086 Interrupts (Types 0-4)

**Tags:** #interrupts #exceptions #debugging

Intel reserved the first five interrupt types (0 through 4) for specific, predefined functions. These are triggered automatically by the hardware or through special instructions to handle common errors and debugging tasks.

### Type 0: Divide Error

- **Trigger:** This exception occurs automatically when the CPU detects an error during a `DIV` (unsigned divide) or `IDIV` (signed divide) instruction.
    
- **Conditions:**
    
    1. The divisor is zero.
        
    2. The resulting quotient is too large to fit in the destination register (`AL` for byte division, `AX` for word division).
        
- **Purpose:** Prevents a mathematically invalid operation from producing a garbage result and continuing. The default ISR for this interrupt typically terminates the program with a "Divide Error" message.
    

### Type 1: Single-Step (Trap)

- **Trigger:** This interrupt occurs automatically after _every_ instruction executes, but only if the **Trap Flag (`TF`)** in the `FLAGS` register is set to `1`.
    
- **Purpose:** This is the hardware foundation for **debuggers**. When a debugger "single-steps" through code, it sets the `TF`. After each instruction, the Type 1 interrupt is triggered, and the ISR (which is part of the debugger) gets control. The debugger can then inspect registers and memory, display the state to the user, and wait for the command to execute the next instruction.
    
- **Automatic Reset:** The CPU automatically clears the `TF` when it enters the Type 1 ISR, so the ISR itself doesn't run in single-step mode.
    

### Type 2: Non-Maskable Interrupt (NMI)

- **Trigger:** This interrupt is triggered by a rising edge signal on the CPU's physical `NMI` pin.
    
- **Characteristics:**
    
    - **Non-Maskable:** It cannot be disabled by clearing the `IF` flag. It has a higher priority than the `INTR` pin.
        
    - **Critical Events:** It is reserved for catastrophic hardware failures or events that must be handled immediately.
        
- **Use Case:** The classic example is a "power-fail" circuit. If the main power is about to fail, a capacitor can hold enough charge to send a signal to the `NMI` pin. The NMI's ISR would then have a few milliseconds to save critical data from RAM to a non-volatile medium before the system shuts down.
    

### Type 3: Breakpoint

- **Trigger:** This is a software interrupt triggered by executing the special one-byte `INT 3` instruction.
    
- **Purpose:** This is the other key feature for **debuggers**. When you set a "breakpoint" in your code, the debugger replaces the instruction at that location in memory with the `INT 3` opcode (`CCh`). When the program runs, it executes normally until it hits the `INT 3` instruction. This triggers the Type 3 interrupt, transferring control back to the debugger's ISR, which then stops execution and gives control to the user. To resume, the debugger replaces the original instruction and continues.
    

### Type 4: Overflow

- **Trigger:** This is a software interrupt triggered by executing the `INTO` (Interrupt on Overflow) instruction, but _only if_ the **Overflow Flag (`OF`)** is set to `1`.
    
- **Purpose:** Provides a way to explicitly handle signed arithmetic overflow. After performing a signed addition or subtraction, you can place an `INTO` instruction. If the operation resulted in an overflow (`OF=1`), the `INTO` will trigger the Type 4 ISR to handle the error. If there was no overflow (`OF=0`), the `INTO` instruction does nothing.
    

#### Interrupt Priority

If multiple interrupts are requested at the same time, the 8086 services them according to a fixed priority:

1. **Highest:** Exceptions (like Divide Error), `INT n`, `INTO`
    
2. `NMI`
    
3. `INTR`
    
4. **Lowest:** Single-Step (Trap)
    

**Links:** [[8086 Interrupts and System Control (Index)]]