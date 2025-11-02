
**Tags:** #interrupts #isr #stack #context_switch

When an 8086 CPU receives an interrupt request that it decides to service, it doesn't immediately jump to the handler code. First, it performs a precise, un-interruptible sequence of hardware-level actions to ensure that it can safely return to the interrupted program later. This entire process is a foundational form of a **context switch**.

Here is a step-by-step simulation of what the hardware does:

**Pre-condition:** The CPU is running a main program. An interrupt signal arrives (e.g., from the keyboard controller via the `INTR` pin). The CPU finishes its current instruction and decides to service the interrupt.

### The CPU's Automatic Hardware Sequence

**Step 1: Save the `FLAGS` Register** The current state of the `FLAGS` register is critical. It holds the results of the last comparison (`ZF`), the sign of the last arithmetic operation (`SF`), etc. To ensure this context isn't lost, the CPU pushes the entire `FLAGS` register onto the stack.

- `SP` is decremented by 2.
    
- The 16-bit `FLAGS` register is written to the memory location `SS:SP`.
    

**Step 2: Clear `IF` and `TF` Flags** To prevent other, less important interrupts from interrupting the _current_ interrupt handler, the CPU automatically clears the `IF` (Interrupt Flag). This masks subsequent `INTR` requests. It also clears the `TF` (Trap Flag) to disable single-step mode within the ISR.

- This ensures the Interrupt Service Routine (ISR) can run without being disturbed.
    

**Step 3: Save the Return Address (`CS` and `IP`)** The CPU must save the location of the _next_ instruction it was about to execute in the main program. It does this by pushing the `CS` (Code Segment) and `IP` (Instruction Pointer) registers onto the stack.

- `SP` is decremented by 2; `CS` is pushed.
    
- `SP` is decremented by 2; `IP` is pushed.
    

**Step 4: Fetch the ISR Address** The CPU now needs to find the address of the handler routine for this specific interrupt. It gets this address from the **Interrupt Vector Table (IVT)**. For an interrupt of type `n`, the CPU reads the 4-byte address stored at physical memory location `n * 4`.

**Step 5: Jump to the ISR** The CPU loads the fetched address into its `CS` and `IP` registers. This action causes an "indirect far jump," immediately transferring control to the beginning of the Interrupt Service Routine.

### Inside the Interrupt Service Routine (ISR) - Software's Responsibility

Now the software takes over. A well-behaved ISR must perform the following:

**Step 6: Save the General-Purpose Registers (Software)** The automatic hardware sequence only saves `FLAGS`, `CS`, and `IP`. The ISR will likely use registers like `AX`, `BX`, etc., which would overwrite the values from the main program. Therefore, the first thing an ISR must do is `PUSH` any registers it plans to modify.

**Step 7: Service the Interrupt** This is the main body of the ISR, where it performs the work required by the event (e.g., reads the key code from the keyboard port, moves data from the network card into a buffer).

**Step 8: Restore the General-Purpose Registers (Software)** Before returning, the ISR must `POP` the registers it saved in Step 6, in the reverse order. This restores the main program's register context perfectly.

### Returning from the Interrupt

**Step 9: Execute `IRET`** The ISR ends with a special `IRET` (Interrupt Return) instruction. `IRET` tells the CPU to reverse the initial hardware sequence:

- It pops the `IP` from the stack.
    
- It pops the `CS` from the stack.
    
- It pops the `FLAGS` register from the stack.
    

Because the old `FLAGS` (with `IF=1`) is restored, interrupts are automatically re-enabled. The CPU is now back in the main program, at the exact instruction after the one that was interrupted, with all its registers and flags intact, as if nothing ever happened.

**Links:** [[8086 Interrupts and System Control (Index)]]