# Types of 8086 Interrupts

**Tags:** #interrupts #hardware_interrupts #software_interrupts #exceptions

In the 8086 architecture, an interrupt can be triggered from one of three distinct sources. Each type serves a different purpose, from handling external hardware to managing software errors.

### 1. Hardware Interrupts

These are asynchronous events triggered by an external device signaling the CPU through its physical pins.

- **Trigger:** An external hardware device (like a timer chip, keyboard controller, or network card) sends an electrical signal to one of the CPU's interrupt pins.
    
- **CPU Pins:**
    
    - **`INTR` (Interrupt Request):** This is for **maskable** interrupts. A maskable interrupt can be temporarily ignored (or "masked") by the software if the CPU is performing a critical task. This is controlled by the `IF` (Interrupt Flag) in the `FLAGS` register. If `IF=0`, the CPU will ignore signals on the `INTR` pin.
        
    - **`NMI` (Non-Maskable Interrupt):** This is for high-priority, critical events that **cannot be ignored**. Signals on the `NMI` pin will always be serviced, regardless of the state of the `IF` flag. This is typically reserved for emergencies like a power failure warning or a memory parity error.
        

### 2. Software Interrupts

These are synchronous events triggered explicitly by an instruction within a program.

- **Trigger:** The program executes the `INT <interrupt_number>` instruction. For example, `INT 21H` is the famous DOS API interrupt.
    
- **Purpose:** Software interrupts are the primary mechanism for a user program to request services from the operating system. Instead of giving a program direct access to hardware (which would be unsafe), the OS provides a set of services (like "read a file" or "print to screen") accessible via software interrupts. This is the foundation of a **system call**.
    

### 3. Predefined Interrupts (Exceptions)

These are synchronous events triggered automatically by the CPU's hardware when an error condition occurs during the execution of an instruction.

- **Trigger:** An error detected by the CPU itself.
    
- **Purpose:** To handle runtime errors. The CPU has dedicated interrupt numbers for specific problems.
    
- **Examples:**
    
    - **Type 0: Divide Error.** Occurs if the result of a `DIV` or `IDIV` instruction is too large to fit in the destination register, or if you attempt to divide by zero.
        
    - **Type 4: Overflow.** Occurs if the `INTO` (Interrupt on Overflow) instruction is executed while the Overflow Flag (`OF`) is set.
        

The key difference is timing: **Hardware interrupts are unpredictable** and can happen at any time. **Software interrupts and exceptions are predictable**; they happen in direct response to the code being executed.

**Links:** [[8086 Interrupts and System Control (Index)]]