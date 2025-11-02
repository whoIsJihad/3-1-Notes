

**Tags:** #microprocessor #intel #architecture #x86 #cse_core

Welcome to the study notes for the Intel 8086 microprocessor. 

These notes break down the architecture into small, manageable topics. We'll start with the high-level features and then dive into the details of its internal units, how it handles memory, and what each register does.

### Core Architectural Concepts

- [[8086 Key Features]] - A beginner-friendly overview of what makes the 8086 tick.
    
- [[8086 Internal Architecture - BIU and EU]] - The "two brains" concept that allows the 8086 to work faster.
    
- [[8086 Instruction Cycle and Pipelining]] - How the 8086 fetches and executes instructions efficiently.
    
- [[8086 Memory Organization]] - The trickiest part: how a 16-bit CPU addresses 1MB of memory using segments and banks.
    

### Processor Registers

- [[8086 Execution Unit (EU) Registers]] - The "workhorse" registers that handle data and calculations (AX, BX, etc.).
    
- [[8086 Flags Register]] - The special register that keeps track of the results of operations (like was it zero? was there a carry?).
    
- [[8086 Bus Interface Unit (BIU) Registers]] - The "addressing" registers that tell the CPU where to find code and data in memory (CS, IP, etc.).
    

### Hardware and Operation

- [[8086 Pin Diagram and Operating Modes]] - A look at the physical pins and the two main modes of operation (Minimum and Maximum).