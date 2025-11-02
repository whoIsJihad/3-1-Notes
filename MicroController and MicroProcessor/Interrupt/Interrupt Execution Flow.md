# Interrupt Execution Flow

**Tags:** #microcontroller #cpu #architecture #interrupts

When an interrupt signal is received and acknowledged by the CPU, it follows a precise hardware-controlled sequence to handle the event without losing its place in the main program. This process is similar to a hardware-enforced function call.

### The Step-by-Step Sequence

1. **Finish Current Instruction**: The CPU completes the single machine instruction it is currently executing. It does not stop in the middle of an instruction.
    
2. **Acknowledge Interrupt**: The CPU acknowledges the signal from the interrupting device.
    
3. **Save Context**: The CPU automatically pushes the current address of the Program Counter (PC) onto the stack. This saves the location of the next instruction in the main program. It may also save the status register (`SREG`).
    
4. **Load ISR Address**: The CPU looks up the fixed address for the specific interrupt source in the **[[ATmega32 Interrupt Vector Table]]** and loads that address into the Program Counter.
    
5. **Execute ISR**: The CPU jumps to the address of the Interrupt Service Routine (ISR) and begins executing the code within it.
    
6. **Restore Context**: When the ISR is finished, it executes a special `RETI` (Return from Interrupt) instruction. This instruction automatically pops the original address from the stack back into the Program Counter.
    
7. **Resume Normal Execution**: The CPU continues executing the main program from the exact point it was interrupted.
    

This entire process ensures that the main program is unaware it was ever paused, allowing for seamless and efficient event handling.

**Links**: [[ATmega32 Interrupts]], [[Programming Interrupts in C]]