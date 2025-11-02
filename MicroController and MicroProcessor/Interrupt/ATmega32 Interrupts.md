# ATmega32 Interrupts

**Tags:** #microcontroller #atmega32 #interrupts #embedded

An interrupt is a hardware signal sent to the CPU that temporarily stops (interrupts) the main program to execute a special, high-priority function called an **Interrupt Service Routine (ISR)**. After the ISR is complete, the main program resumes exactly where it left off.

This mechanism is fundamental to efficient embedded systems programming, allowing the microcontroller to respond to events in real-time without wasting CPU cycles.

### Core Concepts

1. **[[Polling vs Interrupts]]**: The fundamental difference between checking for an event and being notified by it.
    
2. **[[Interrupt Execution Flow]]**: The step-by-step process the CPU follows when an interrupt occurs.
    
3. **[[ATmega32 Interrupt Vector Table]]**: A reference for all available interrupt sources and their priorities.
    
4. **[[Programming Interrupts in C]]**: The essential steps and syntax for writing interrupt-driven code.
    
5. **[[External Interrupts]]**: How to respond to events from external hardware like buttons or sensors.
    
6. **[[Interrupt Control Registers]]**: Detailed breakdown of the registers used to configure interrupts.
    
7. **[[The volatile Keyword]]**: A critical concept for sharing data between the main program and an ISR.
    

### Practical Code

- **[[C Code Examples - Interrupts]]**: A collection of code snippets for implementing interrupts.