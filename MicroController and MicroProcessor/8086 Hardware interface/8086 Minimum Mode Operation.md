# 8086 Minimum Mode Operation

**Tags:** #8086 #hardware #minimum_mode

When `MN/MX` (Pin 33) is connected to +5V, the 8086 enters Minimum Mode. In this configuration, the processor is the sole master of the bus and generates all the necessary control signals internally. This is the most straightforward way to build an 8086-based system.

The key characteristic of this mode is the function assigned to pins 24 through 31.

### Minimum Mode Pin Functions (Pins 24-31)

|Pin|Name|I/O|Function & Connection Simulation|
|---|---|---|---|
|24|`INTA`|Out|**Interrupt Acknowledge:** When the CPU acknowledges an interrupt request from the `INTR` pin, it performs two `INTA` cycles. It pulses this line LOW to signal to the interrupting device (like an 8259 PIC) that it should place an interrupt vector number onto the data bus.|
|25|`ALE`|Out|**Address Latch Enable:** This is a critical de-multiplexing signal. It pulses HIGH at the start of a bus cycle (T1 state) to indicate that the `AD0-AD15` and `A16-A19` lines contain a valid address. This signal is used to trigger an external latch to "catch" and hold the address for the rest of the cycle.|
|26|`DEN`|Out|**Data Enable:** This signal goes LOW when the data bus is active. It is used to enable external data bus transceivers/buffers (like the 8286), which are needed to drive the data signals in a larger system. It effectively turns the data bus "on."|
|27|`DT/R`|Out|**Data Transmit/Receive:** This signal specifies the direction of data flow on the bus. When HIGH (`Transmit`), the CPU is writing data to memory/IO. When LOW (`Receive`), the CPU is reading data from memory/IO. It controls the direction of the external data bus transceivers.|
|28|`M/IO`|Out|**Memory/IO Select:** This is a fundamental signal that tells other components whether the address on the address bus is for a memory location (`M/IO` = HIGH) or an I/O port (`M/IO` = LOW).|
|29|`WR`|Out|**Write:** This is an active-low signal. The CPU pulls this line LOW to indicate that it is writing data to a memory or I/O location. The data on the data bus is considered valid at the rising edge of the `WR` signal.|
|30|`HOLD`|In|**Hold Request:** An input from another potential bus master (like a DMA controller). When a device pulls `HOLD` HIGH, it is requesting control of the system bus.|
|31|`HLDA`|Out|**Hold Acknowledge:** The 8086's response to a `HOLD` request. After the current bus cycle is complete, the CPU will float its buses and signal `HLDA` HIGH, indicating that the other device can now take control of the bus.|
### The HOLD and HLDA Handshake 🤝

|Pin|Name|Type|Function|
|---|---|---|---|
|**30**|**HOLD**|Input|**Hold Request:** This pin is an input to the 8086 from another potential **bus master** (e.g., a DMA controller). When this device needs to control the bus, it pulls the HOLD line **HIGH**, requesting that the CPU surrender control of the system bus.|
|**31**|**HLDA**|Output|**Hold Acknowledge:** This is the 8086's response. Once the 8086 receives the HOLD request, it will **finish the current bus cycle** it is executing. After the cycle is complete, the CPU **floats its buses** (makes them high-impedance) and signals HLDA **HIGH**, indicating that the requesting device can now take over the Address, Data, and Control lines.|

**Links:** [[8086 Pin Configuration and Operating Modes]], [[Simulating an 8086 Memory Read Cycle]]