# Interrupt Execution

Tags: interrupt, cpu, os_concepts

An interrupt is a signal to the processor indicating an event that needs immediate attention.

- When an interrupt occurs, the ATmega32 completes the currently executing instruction.
    
- The response takes a minimum of four clock cycles.
    
- During this time, the Program Counter (PC) is pushed onto the stack.
    
- The processor then jumps to the specific interrupt vector address to execute the interrupt handling routine.
    
- A return from an interrupt also takes four clock cycles, during which the PC is popped from the stack.
