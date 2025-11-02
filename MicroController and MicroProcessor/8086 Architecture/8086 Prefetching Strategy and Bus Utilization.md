# 8086 Prefetching Strategy and Bus Utilization

**Tags:** #pipelining #prefetching #bus #computer_architecture

The strategy of _when_ to fetch the next instruction bytes is a subtle but important performance consideration. The goal is to keep the Execution Unit (EU) busy without wasting the bandwidth of the data bus.

### The Core Problem

The 8086 has a **16-bit (2-byte) data bus**. This means in a single memory read machine cycle, it can fetch 2 bytes from memory. However, the prefetch logic in the original 8086 triggers a new fetch cycle whenever there is **one or more empty bytes** in its 6-byte queue. This creates a potential inefficiency.

### Scenario: The Trade-off

Let's analyze the situation described in the handwritten notes:

- **Bus Width:** 2 bytes (16-bit)
    
- **EU Action:** The EU consumes a 1-byte instruction from the queue.
    
- **Queue State:** The queue now has a 1-byte empty space.
    
- **BIU Trigger:** The BIU's logic sees an empty space and immediately initiates a new fetch cycle to fill it.
    

**The Inefficiency:** The BIU initiates a full memory read machine cycle, which is capable of fetching 2 bytes. However, because it only needs to fetch 1 byte to fill the queue again, the full potential of the 16-bit data bus is not utilized in this specific cycle. One half of the data bus (8 bits) is effectively unused.

### Why Not Wait for More Space?

One might ask: why not wait until at least 2 bytes are free in the queue before starting a fetch? This would guarantee full bus utilization.

**The Risk: EU Starvation** The danger with waiting is that the EU might become **starved**. Consider a sequence of fast, 1-byte instructions.

1. Queue has 2 bytes left.
    
2. EU executes a 1-byte instruction. (1 byte left)
    
3. EU executes another 1-byte instruction. (0 bytes left)
    

If the BIU had waited for a 2-byte space, the EU would now be idle, waiting for the BIU to complete a full fetch cycle. This **EU idle time** is far more detrimental to performance than a single cycle of bus underutilization.

### Conclusion

The 8086 designers chose a strategy that prioritizes **keeping the EU busy** over maximizing bus bandwidth on every single cycle. The logic is that an idle EU is the biggest performance loss. Therefore, it's better to trigger a fetch as soon as there is any space, even if it sometimes leads to an underutilized data bus. This design choice reflects a fundamental trade-off in computer architecture: latency vs. throughput.

**Links:** [[8086 Instruction Prefetching Mechanism]]