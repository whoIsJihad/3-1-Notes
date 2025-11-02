# Interrupts in Computing

**Tags:** #interrupts #cpu #os #computer_architecture

An interrupt is a signal sent to the CPU from either a hardware device or a software program, indicating an event that needs immediate attention. It is the primary mechanism for devices to communicate with the CPU without the CPU having to constantly poll them.

### The Purpose of Interrupts

Imagine a CPU needing to get input from a keyboard. Without interrupts, the CPU would have to use a method called **polling**: `"Is there a key press? No. Is there a key press now? No.  How about now? No..."` This is incredibly inefficient and wastes countless CPU cycles that could be used for other tasks.

Interrupts solve this problem. The CPU can continue executing its main program, and the keyboard controller will only send an interrupt signal when a key is actually pressed.

### The Interrupt Handling Process

1. **Interrupt Request:** A device sends an interrupt signal to the CPU's interrupt request (IRQ) pin.
    
2. **Acknowledge and Pause:** If interrupts are enabled (via the `IF` flag), the CPU finishes its current instruction and then pauses the main program. It saves its current state (the value of the Program Counter and other registers) onto the stack.
    
3. **Identify the Source:** The CPU identifies which device sent the interrupt.
    
4. **Execute the ISR:** The CPU jumps to a specific piece of code called an **Interrupt Service Routine (ISR)**, which is a pre-defined function for handling that particular interrupt (e.g., an ISR for the keyboard would read the key-press data).
    
5. **Resume:** Once the ISR is complete, the CPU restores its previous state from the stack and resumes executing the main program exactly where it left off.
    

This mechanism allows the CPU to efficiently manage multiple I/O devices and events without wasting time, and it is a fundamental concept in both computer architecture and operating systems.

**Links:** [[The Central Processing Unit (CPU) Explained]]