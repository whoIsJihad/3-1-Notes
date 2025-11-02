

**Tags:** #8086 #interrupts #os_concepts #system_calls #hardware_interface

An **interrupt** is a signal to the CPU that indicates an event requiring immediate attention. When an interrupt occurs, the processor pauses its current task, saves its state, and transfers execution to a special handler routine called an **Interrupt Service Routine (ISR)**. Once the ISR is complete, the CPU resumes the original task exactly where it left off.

This mechanism is the foundation for all modern event-driven computing. It's how a computer can respond to unpredictable external events (like a mouse click) while still efficiently executing its main programs. It allows the CPU to move from a wasteful "polling" model (constantly asking "Did anything happen yet?") to a highly efficient "interrupt-driven" model ("Wake me up when something happens.").

Understanding interrupts is critical for bridging the gap between hardware and operating systems.

### Core Concepts

- [[The Need for Interrupts - Polling vs. Interrupt-Driven I O]]: Why interrupts are a more efficient solution for communication.
    
- [[Types of 8086 Interrupts]]: Exploring the three sources of interrupts: hardware, software, and exceptions.
    
- [[The Interrupt Handling Process]]: A step-by-step simulation of what the CPU does when an interrupt occurs.
    
- [[The Interrupt Vector Table (IVT)]]: The critical data structure that maps interrupt numbers to their handlers.
    
- [[Dedicated 8086 Interrupts (Types 0-4)]]: A deep dive into the predefined interrupts for common errors and debugging.