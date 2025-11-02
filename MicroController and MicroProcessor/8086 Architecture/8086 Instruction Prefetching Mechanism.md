# 8086 Instruction Prefetching Mechanism

**Tags:** #pipelining #prefetching #8086 #biu #eu

The concept of prefetching is a simple yet powerful form of pipelining used by the 8086 to improve performance. The core idea is to **fetch instructions from memory in advance** so the Execution Unit (EU) doesn't have to wait for them.

### The 6-Byte Prefetch Queue

The Bus Interface Unit (BIU) contains a 6-byte First-In, First-Out (FIFO) queue. This queue acts as a buffer between main memory and the EU.

**The Parallel Process:**

1. **BIU's Role (The Fetcher):** The BIU's primary background task is to keep the prefetch queue as full as possible. Whenever the bus is not being used for other operations (like reading or writing data for the EU), the BIU initiates memory read machine cycles to fetch the next sequential instruction bytes from the code segment.
    
2. **EU's Role (The Executor):** In parallel, the EU pulls fully formed instructions from the front of the queue. The EU doesn't know or care about memory addresses; it simply consumes the instruction bytes provided by the BIU.
    

This concurrent operation decouples the fetching process from the execution process, allowing them to overlap and save time.

### Variable Instruction Length

A key challenge is that 8086 instructions are not all the same size. They can be anywhere from 1 to 6 bytes long.

- The 6-byte queue might hold one very long instruction, six 1-byte instructions, or any combination in between.
    
- The EU is responsible for determining how many bytes constitute the next complete instruction. It pulls 1, 2, 4, or more bytes from the queue as needed to form a single, valid instruction before executing it.
    

### When Fetching Pauses

The BIU does not fetch instructions under two conditions:

1. **The Queue is Full:** If the 6-byte queue is completely full, the BIU will wait until the EU consumes at least one byte before fetching again.
    
2. **A Jump Instruction Occurs:** If the EU executes a jump or call instruction, the entire contents of the prefetch queue become invalid. The queue is flushed (cleared), and the BIU is directed to start fetching from the new address specified by the jump instruction. This event is known as a **pipeline stall**.
    

**Links:** [[8086 Execution and Timing Index Page]], [[8086 Prefetching Strategy and Bus Utilization]]