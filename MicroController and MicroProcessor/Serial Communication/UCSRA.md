# UCSRA – USART Control and Status Register A

The **UCSRA** is one of the three primary registers controlling the USART peripheral on the ATmega32. Its main function is to hold **status flags** for communication and report any **errors** that occur during the receive process. Understanding this register is crucial for implementing both polled and interrupt-driven serial communication routines.
This Note mentions buffering in ATmega32. To know more about those go to  [[ USART Data Buffering Explained (ATmega32)]]
## Detailed Context of Each Bit

| Bit   | Name | Type        | Context and Utility in ATmega32 Programming                                                                                                                                                                                                                                                                                                                                                                                                     |
| ----- | ---- | ----------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **7** | RXC  | Status Flag | **Receive Complete Flag** (Read-Only). **Set to 1 by hardware** when a complete data frame (including stop bits) has been successfully received, processed, and the 8-bit data character is waiting in the **Receive Buffer** (which is accessed via the UDR register). **Utility:** This is the primary flag used to check for incoming data in a polling routine: `while (!(UCSRA & (1<<RXC)));`                                              |
| **6** | TXC  | Status Flag | **Transmit Complete Flag** (Read/Write). **Set to 1 by hardware** when the entire contents of the transmit **Shift Register** (data bits, start bit, parity, and stop bit(s)) have been shifted out onto the TXD pin. **Utility:** Signals that the transmitter is truly idle. It must be **cleared manually by writing a '1' to it**, or it is cleared automatically if a TXC interrupt is enabled and the ISR is executed.                    |
| **5** | UDRE | Status Flag | **USART Data Register Empty Flag** (Read-Only). **Set to 1 by hardware** when the **Transmit Buffer** is empty and ready to accept the next data byte from the CPU. **Utility:** This flag manages the double-buffering. Your transmit function _must_ wait for UDRE to be '1' before writing to the UDR to ensure the previous byte is safely in the Shift Register and to prevent data overrun/loss.                                          |
| **4** | FE   | Error Flag  | **Frame Error Flag** (Read-Only). **Set to 1 by hardware** if the receiver detects an invalid stop bit in the incoming data frame (i.e., the expected logic '1' stop bit was read as a logic '0'). **Context:** This typically indicates a synchronization problem, usually due to a severe baud rate mismatch or excessive noise on the line. It is checked after RXC is set and is **cleared automatically** when the UDR is read.            |
| **3** | DOR  | Error Flag  | **Data OverRun Flag** (Read-Only). **Set to 1 by hardware** if a new character is received and transferred into the Receive Buffer **before** the CPU had read the previous character from that buffer. **Context:** This signals a buffer overflow. The old, unread data is lost and overwritten by the new data. It means your software is too slow to handle the incoming data stream. It is **cleared automatically** when the UDR is read. |
| **2** | PE   | Error Flag  | **Parity Error Flag** (Read-Only). **Set to 1 by hardware** if parity checking is enabled, and the received parity bit does not match the expected parity calculated by the receiver. **Context:** This signals that the data was likely corrupted during transmission due to noise or external interference. It is checked after RXC is set and is **cleared automatically** when the UDR is read.                                             |
| **1** | U2X  | Control Bit | **Double Transmission Speed** (Read/Write). When set to **1**, it changes the Baud Rate Generator's division factor from 16 to 8 (in asynchronous mode), effectively **doubling the baud rate** for any given value loaded into the UBRR register. **Context:** Allows for higher communication speeds, but reduces the sampling margin, making the communication less tolerant to baud rate errors.                                            |
| **0** | MPCM | Control Bit | **Multi-processor Communication Mode** (Read/Write). When set to **1**, the USART receiver will ignore all incoming frames unless the ninth data bit (if 9-bit framing is used) or an address marker is present. **Context:** Used to set up a network where a host communicates selectively with multiple slave microcontrollers on a single serial bus.                                                                                       |

## Application Summary

The UCSRA register is indispensable for writing robust, industrial-quality communication code. The RXC and UDRE flags are your primary tools for managing the flow of data using polling, while the FE, DOR, and PE flags are used to implement necessary error checking routines to ensure the integrity of the data your microcontroller receives.

---

# USART Communication Simulation: ATmega32 to PC/Bluetooth Module

This simulation models the exchange of a single character ('A', ASCII 65 or 0x41) between two devices operating at 9600 bps.

## Hardware Setup (Device Interconnection)

The USART uses a dedicated pair of pins for full-duplex communication:

|Device 1 (ATmega32)|Connection Type|Device 2 (PC/Bluetooth Module)|
|---|---|---|
|**TXD (PD1)**|Transmits data|**RXD**|
|**RXD (PD0)**|Receives data|**TXD**|
|**GND**|Common ground reference|**GND**|

**Crucial Point:** The Transmitter of one device _must_ be connected to the Receiver of the other device (Cross-wired connection).

## Simulation Scenario: Sending Character 'A' (0x41)

**Configuration:** 9600 bps, 8 data bits, No Parity, 1 Stop Bit (8N1).

### Step 1: ATmega32 Transmits 'A' (0x41)

The binary representation of 'A' is 01000001. Since data is sent **LSB first**, the transmission order of the data bits will be 10000010.

|Time (Baud Cycles)|Bit|Logic State|TXD Line Voltage|UCSRA Flag Activity|Description|
|---|---|---|---|---|---|
|**Idle**|-|HIGH ('1')|VCC​ (High)|UDRE is '1'|Line is idle. CPU writes `0x41` to UDR. UDRE clears to '0'.|
|1|**Start Bit**|LOW ('0')|0V (Low)|-|Signals the receiver to synchronize and start sampling.|
|2-9|**Data Bits**|10000010|Varies|-|0x41 is sent LSB first (1,0,0,0,0,0,1,0).|
|10|**Stop Bit**|HIGH ('1')|VCC​ (High)|-|Signals the end of the frame.|
|11|**Idle**|HIGH ('1')|VCC​ (High)|TXC sets to '1'|The transmission is complete. CPU can now clear TXC or the interrupt fires.|

### Step 2: Receiving Device Processes 'A' (0x41)

The receiving device is constantly sampling its RXD line.

|Time (Baud Cycles)|Action|Receiver Status|UCSRA Flag Activity (on Receiver)|Error Check Status|
|---|---|---|---|---|
|1|**Start Bit Detected**|Synchronizing clock.|-|-|
|2-9|**Data Sampling**|Bits 10000010 are sampled and assembled.|-|-|
|10|**Stop Bit Sampled**|Checks for HIGH ('1') state.|FE is checked (If LOW, FE sets to '1').|No error (assuming HIGH).|
|11|**Data Transfer**|Assembled character 0x41 is moved to Receive Buffer.|RXC sets to '1'. PE / DOR checked.|No Parity error (N/A) or OverRun.|
|**CPU Read**|Program executes `UDR = usart_receive();`|Data 0x41 is read.|RXC, FE, DOR, PE all **clear to '0'**.|-|

## Error Checking and UCSRA Utility

The simulation highlights why the error flags in UCSRA are critical:

- **Frame Error (**FE**):** If the Stop Bit (Time 10) was sampled as a '0', the FE flag would be set. The FE flag _must_ be checked _before_ reading the UDR to ensure the incoming data is reliable.
    
- **Data OverRun (**DOR**):** If the CPU fails to read the UDR (and clear RXC) before the next Start Bit arrives and the next frame is complete, the DOR flag will be set, and the first character is lost. This is a common issue when polling is used in a complex, slow main loop.
Links :
- [[USART Control and Status Registers (UCSRA, B, C)]]
- [[Serial Communication in ATmega32]]