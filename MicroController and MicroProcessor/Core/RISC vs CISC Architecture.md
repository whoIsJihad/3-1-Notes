# RISC vs CISC Architecture

Tags: risc, cisc, architecture, cpu, isa

There are two major philosophies for designing instruction set architectures:

**RISC (Reduced Instruction Set Computer):**

- Emphasis on software.
    
- Uses a smaller set of simple, single-clock instructions.
    
- Operations are typically register-to-register, requiring explicit "LOAD" and "STORE" instructions to access memory.
    
- Results in larger code sizes but has a lower cycles-per-second count, making it faster for many operations.
    
- Spends more transistors on memory registers.
    
- The [[ATmega32 Architecture|ATmega32]] uses a RISC architecture.
    

**CISC (Complex Instruction Set Computer):**

- Emphasis on hardware.
    
- Includes multi-clock, complex instructions that can perform several low-level operations at once.
    
- Allows for memory-to-memory operations where "LOAD" and "STORE" are incorporated into instructions.
    
- Results in smaller code sizes but has a high cycles-per-second count.
    
- Uses transistors for storing the complex instructions.
    
- The [[8086 Architecture|8086]] is an example of a CISC architecture.
