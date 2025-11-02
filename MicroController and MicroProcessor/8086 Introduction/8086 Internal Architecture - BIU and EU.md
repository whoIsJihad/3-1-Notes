# 8086 Internal Architecture - BIU and EU

**Tags:** #microprocessor #8086 #architecture #BIU #EU

The key to the 8086's efficiency is its internal division into two separate, semi-independent units that work in parallel: the **Bus Interface Unit (BIU)** and the **Execution Unit (EU)**. 

### Bus Interface Unit (BIU)

The BIU is the 8086's connection to the outside world. It handles all memory and I/O operations.

**Its Main Jobs:**

1. **Address Calculation:** Calculates the 20-bit physical memory addresses. This is its most complex task.
    
2. **Instruction Fetching:** Reads instructions from memory and stores them in the 6-byte prefetch queue. It tries to keep this queue as full as possible.
    
3. **Bus Management:** Manages the address and data buses for reading and writing data to memory or I/O ports.
    

The BIU contains the "addressing" registers: the [[8086 Bus Interface Unit (BIU) Registers|Segment Registers (CS, DS, SS, ES)]] and the [[8086 Bus Interface Unit (BIU) Registers|Instruction Pointer (IP)]].

### Execution Unit (EU)

The EU is the "brain" of the operation. It's responsible for decoding and executing the instructions.

**Its Main Jobs:**

1. **Instruction Decoding:** It pulls instructions one by one from the front of the BIU's prefetch queue.
    
2. **Execution:** It uses its Arithmetic Logic Unit (ALU) to perform the operations specified by the instruction (e.g., addition, subtraction, logical AND, etc.).
    
3. **Data Handling:** It manages the general-purpose registers and the flags register.
    

The EU has no direct connection to the system buses. If it needs to read data from memory or write a result back, it makes a request to the BIU, which then performs the operation. This division of labor is what enables [[8086 Instruction Cycle and Pipelining]].

**Links:** [[8086 Microprocessor Architecture]], [[8086 Instruction Cycle and Pipelining]]