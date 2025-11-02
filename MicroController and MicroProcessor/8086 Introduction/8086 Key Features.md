# 8086 Key Features

**Tags:** #microprocessor #intel #8086

The Intel 8086 was a major leap forward from the 8-bit processors that came before it. Here’s a breakdown of its defining features, explained in a more accessible way.

### Core Specifications

- **A True 16-bit Processor:** This is its most important feature. It means:
    
    - Its internal registers can hold 16 bits of data.
        
    - Its Arithmetic Logic Unit (ALU) can perform calculations on 16-bit numbers in a single operation.
        
    - Its data bus is 16 bits wide, meaning it can transfer 2 bytes of data to or from memory at once. This made it much faster than 8-bit processors which had to do two memory accesses to get the same amount of data.
        
- **20-bit Address Bus:** While the processor itself is 16-bit, it has a 20-bit address bus. This allows it to physically connect to and access `2^20` unique memory locations.
    
    ```
    2^20 bytes = 1,048,576 bytes = 1 Megabyte (MB)
    ```
    
    This was a huge amount of memory for its time. How a 16-bit CPU generates a 20-bit address is a key part of its design, explained in [[8086 Memory Organization]].
    
- **Instruction Prefetch Queue:** The 8086 has a small, 6-byte internal memory queue. It proactively fetches the next few instructions from memory _before_ they are actually needed. This simple form of pipelining speeds up execution because the processor doesn't have to wait for memory access as often. See [[8086 Instruction Cycle and Pipelining]] for more details.
    
- **Multiplexed Pins:** To fit all its functionality into a 40-pin chip, the 8086 uses multiplexed pins. This means some pins serve dual purposes. For example, the same set of pins are used for both the address and data bus at different times in a machine cycle. This is a clever engineering trick to reduce the physical size and complexity of the chip.
    

**Links:** [[8086 Microprocessor Architecture]]