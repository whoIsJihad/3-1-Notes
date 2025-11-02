# 8086 Maximum Mode Operation

**Tags:** #8086 #hardware #maximum_mode #multiprocessing #bus_controller

When `MN/MX` (Pin 33) is grounded, the 8086 enters Maximum Mode. This mode is an advanced configuration designed for high-performance, complex systems that require more than one processor. The most common use case was pairing the 8086 CPU with an **8087 math coprocessor** to offload floating-point calculations.

In this mode, the 8086's role changes. Instead of managing the intricate details of every bus transaction, it delegates the generation of all bus control signals to a dedicated external chip: the **8288 Bus Controller**. This is a key design principle: by offloading bus management, the 8086 frees up pins and internal logic to coordinate and synchronize its actions with other processors on the bus.

### The 8086-8288 Partnership

Think of this as a manager-assistant relationship.

- **8086 (Manager):** Decides _what_ needs to be done (e.g., "I need to read from memory"). It communicates this high-level intent via a 3-bit **status code** on pins `S2`, `S1`, and `S0`.
    
- **8288 (Assistant):** Monitors the status code and handles the low-level details. It translates the 8086's command into the precise electrical signals needed to control the bus (e.g., asserting `MRDC` - Memory Read Command, `ALE` - Address Latch Enable, etc.).
    

### Maximum Mode Pin Functions (Pins 24-31)

The functions of these eight pins are completely redefined to enable multi-processor coordination.

|Pin|Name|I/O|Function & Connection Simulation|
|---|---|---|---|
|26-28|`S2`, `S1`, `S0`|Out|**Status Signals:** These three pins form a 3-bit status bus. At the beginning of every bus cycle, the 8086 outputs a code that tells the 8288 what type of action is about to occur. For example, a code of `101` indicates a "Code Access Read," meaning an instruction fetch.|
|24-25|`QS1`, `QS0`|Out|**Queue Status:** These two pins provide real-time, external visibility into the 8086's internal 6-byte instruction prefetch queue. A coprocessor like the 8087 constantly "snoops" these lines to synchronize its own execution with the 8086's instruction stream. This is a foundational mechanism for parallel execution.|
|30-31|`RQ/GT1`, `RQ/GT0`|I/O|**Request/Grant:** These are bidirectional lines that replace the simpler `HOLD`/`HLDA` mechanism. Another processor requests the bus by sending a pulse on this line. The 8086 grants control by sending a pulse back on the same line. `RQ/GT0` has a higher priority. This handshake protocol is more robust for systems with multiple potential bus masters.|
|29|`LOCK`|Out|**Lock Bus:** An active-low signal that can be asserted by prefixing an instruction with the `LOCK` prefix. This is a critical signal for concurrent programming. It tells the bus controller not to grant the bus to any other processor until the locked instruction completes. This is the hardware foundation for implementing atomic operations like "test-and-set" for semaphores and mutexes, preventing race conditions.|

### 8288 Bus Controller Decoding

The 8288 constantly monitors `S2`, `S1`, `S0` and generates the corresponding system control signals. This table shows the core translation it performs:

|`S2`|`S1`|`S0`|Bus Cycle Indicated by 8086|8288 Command Generated|
|---|---|---|---|---|
|0|0|0|Interrupt Acknowledge|`INTA` (Interrupt Acknowledge)|
|0|0|1|I/O Read|`IORC` (I/O Read Command)|
|0|1|0|I/O Write|`IOWC` (I/O Write Command)|
|0|1|1|Halt|None (Bus is passive)|
|1|0|0|Code (Instruction) Access Read|`MRDC` (Memory Read Command)|
|1|0|1|Memory Read|`MRDC` (Memory Read Command)|
|1|1|0|Memory Write|`MWTC` (Memory Write Command)|
|1|1|1|Passive / Inactive|None (Bus is passive)|

**Links:** [[8086 Pin Configuration and Operating Modes]]