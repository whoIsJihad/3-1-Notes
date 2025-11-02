# 8086 Execution and Timing

**Tags:** #microprocessor #8086 #pipelining #cpu_timing #computer_architecture

This set of notes dives into the specifics of how the Intel 8086 processor executes instructions, focusing on the concepts of timing and pipelining. Understanding this is key to seeing how architecture directly impacts performance.

We will break down the abstract idea of an "instruction cycle" into its concrete components—machine cycles and clock states—and explore the mechanics of the 8086's famous prefetch queue. This connects the processor's internal structure to real-world performance considerations.

### Core Concepts

- [[8086 BIU and EU Register Division]] - A clear breakdown of which registers belong to the Bus Interface Unit versus the Execution Unit.
    
- [[8086 CPU Timing Cycles Explained]] - Defining and differentiating the key timing concepts: Clock Cycle, T-State, Machine Cycle, and Instruction Cycle.
    
- [[8086 Instruction Prefetching Mechanism]] - A detailed look at how the 6-byte prefetch queue works to speed up execution.
    
- [[8086 Prefetching Strategy and Bus Utilization]] - An analysis of the trade-offs involved in keeping the prefetch queue full without wasting bus bandwidth.
- [[8086 Bus Architecture and Multiplexing]] - A look at the 16-bit data bus, 20-bit address bus, and the technique of multiplexing.
    
- [[Determining Physical Memory Size]] - How the address bus width dictates the total addressable memory.
    
- [[The Mismatch Problem - Bus Width vs Register Size]] - Analyzing the performance issues when data bus and register sizes don't align.
    
- [[Solving the Mismatch - Memory Banking]] - Intel's clever solution to efficiently use a 16-bit data bus with 8-bit memory.