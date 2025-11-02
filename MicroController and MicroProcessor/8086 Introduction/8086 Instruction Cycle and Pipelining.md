# 8086 Instruction Cycle and Pipelining

**Tags:** #microprocessor #8086 #pipelining #prefetching

The 8086's architecture allows it to overlap the instruction fetch and execution stages, a concept known as pipelining. This makes the processor much more efficient than older designs.

### Understanding Time in a CPU

To grasp this, let's define the units of time:

- **Clock Cycle:** The smallest, most fundamental unit of time, determined by the system's clock frequency (e.g., at 5 MHz, one clock cycle is 200 nanoseconds). Every action in the CPU is synchronized to this clock pulse.
    
- **Machine Cycle:** The sequence of steps (composed of multiple clock cycles) needed to perform a single, basic bus operation, like one memory read or one memory write.
    
- **Instruction Cycle:** The total time required to process one entire instruction, from start to finish. This is made up of three main phases: fetch, decode, and execute, and may require several machine cycles.
    

### How Pipelining Works in the 8086

In a non-pipelined processor, the cycle is strictly sequential: `Fetch -> Decode -> Execute -> Fetch -> ...`. The CPU's execution logic sits idle during the fetch phase.

The 8086 improves this with its two-stage pipeline using the BIU and EU:

1. **The BIU's Role:** The Bus Interface Unit is constantly looking ahead. As long as there's space in its 6-byte instruction queue, it performs "fetch" machine cycles to pull in instruction bytes from memory.
    
2. **The EU's Role:** At the same time, the Execution Unit pulls completed instructions from the queue, decodes them, and executes them.
    

As long as the program is running sequentially, the EU almost always has an instruction ready and waiting for it in the queue. It doesn't have to halt and wait for a slow memory access to complete.

### When the Pipeline Breaks: Jumps and Branches

This smooth flow is interrupted when the program doesn't execute sequentially. This happens with `JMP` (jump) or `CALL` (call a function) instructions.

1. The EU executes the jump instruction.
    
2. Suddenly, the instructions that the BIU has already pre-fetched into the queue are wrong—they are from the old, sequential path.
    
3. The entire queue must be **flushed** (cleared out).
    
4. The BIU has to start fetching again from the new memory address specified by the jump instruction.
    

This "pipeline stall" introduces a small delay, but for most programs, the overall speedup from pipelining is significant.

**Links:** [[8086 Internal Architecture - BIU and EU]]