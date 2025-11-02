# 80386 Key Features and Architecture

**Tags:** #80386 #architecture #32bit

The Intel 80386 was a monumental upgrade over the 80286, designed specifically to address its predecessor's limitations and to provide a robust platform for next-generation operating systems.

### Core Improvements Over the 80286

- **True 32-bit Architecture:**
    
    - **32-bit General-Purpose Registers:** All registers were extended to 32 bits (e.g., `AX` became `EAX`).
        
    - **32-bit Data Bus:** The 80386DX could transfer 4 bytes of data in a single bus cycle, doubling the throughput of the 80286.
        
    - **32-bit Address Bus:** With 32 address lines, the 80386DX could directly address 2^32 bytes, or **4 GB** of physical memory, a massive increase from the 16 MB of the 80286.
        
- **Vastly Superior Memory Management:**
    
    - **Large Segment Sizes:** The 64 KB segment limit was removed. Segments could now be up to **4 GB** in size.
        
    - **Paging:** Introduced an optional second layer of address translation, allowing for modern virtual memory implementations.
        
- **New Operating Mode:**
    
    - **Virtual 86 Mode:** Allowed the processor to run 8086 programs in a safe, protected environment _within_ Protected Mode. This was crucial for multitasking legacy DOS applications under a modern OS. It solved the 80286's "stuck in protected mode" problem.
        

### The 80386 Internal Architecture

The 80386's architecture is more parallelized than its predecessors, breaking tasks into specialized units that can work simultaneously.

The chip is logically divided into three main sections:

1. **Central Processing Unit (CPU):**
    
    - **Instruction Unit (IU):** Fetches instruction bytes from the BIU's prefetch queue, decodes them, and places up to 3 decoded instructions into a queue for the Execution Unit.
        
    - **Execution Unit (EU):** Contains the 32-bit general-purpose registers and the ALU. It executes the decoded instructions.
        
2. **Memory Management Unit (MMU):** This is the most significant enhancement.
    
    - **Segmentation Unit (SU):** Performs the first stage of address translation, converting a logical (`Selector:Offset`) address into a 32-bit **linear address**. It contains the descriptor cache registers.
        
    - **Paging Unit (PU):** Performs the optional second stage of translation, converting the **linear address** from the SU into the final **physical address** that goes out on the address bus.
        
3. **Bus Interface Unit (BIU):** Manages the physical interface to the external data and address buses, including instruction prefetching into a 16-byte queue.
    

This highly pipelined and parallel design allowed the 80386 to achieve a much higher instruction throughput than previous generations.

**Links:** [[The Intel 80386 - Dawn of 32-bit Computing]]