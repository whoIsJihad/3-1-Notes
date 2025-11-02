# UCSRC: USART Control and Status Register C - Defining the Frame
Link: - [[USART Control and Status Registers (UCSRA, B, C)]]

The **UCSRC (USART Control and Status Register C)** is the configuration register responsible for defining the physical structure (or "framing") of the serial data. This includes setting the communication mode (synchronous/asynchronous), character size, parity, and stop bits.

## 1. Register Access Caveat: The Shared Address

Before using UCSRC, you must address a unique hardware limitation in the ATmega32 architecture:

- **Shared Address:** The UCSRC register shares the same memory address location as the UBRRH **(USART Baud Rate Register High)** byte.
    
- **The** URSEL **Solution:** To tell the compiler (and the hardware) which register you intend to write to, you use the URSEL (Register Select) bit.
    

|Bit|Name|Role|Practical Application|
|---|---|---|---|
|**7**|URSEL|**Register Select**|**Must be set to '1' to write to** UCSRC. If set to '0', the write operation targets UBRRH instead.|

### C Code Example (The Critical Setup Step)

When setting up UCSRC, you _must_ logically OR the URSEL bit with all your other configuration settings:

```
// Example: Setting 8-bit data, No Parity, 1 Stop Bit, Asynchronous Mode
// 1. Start by setting URSEL to ensure we write to UCSRC
unsigned char ucsrc_config = (1 << URSEL); 

// 2. Add other settings (UMSEL=0, UPM1:0=00, USBS=0, UCSZ1:0=11)
// 8-bit data requires UCSZ1:0 = 11 (bit 1 and 2 of UCSRC)
ucsrc_config |= (1 << UCSZ0) | (1 << UCSZ1); 

// Write the configuration
UCSRC = ucsrc_config; 
```

## 2. Communication Mode and Clock Polarity

|Bit|Name|Setting|Function|
|---|---|---|---|
|**6**|UMSEL|**0 = Asynchronous**|**(Standard UART)** Data transmission relies solely on the internal Baud Rate Generator. The most common mode.|
|||**1 = Synchronous**|Data is transmitted and received using an external clock signal on the XCK pin. Used for high-speed, tightly synchronized communication.|
|**0**|UCPOL|**Clock Polarity**|**Only used in Synchronous Mode (**UMSEL=1**).** Defines the clock edge used for sampling the data (rising or falling).|

## 3. Data Frame Configuration (Framing)

These bits define the structure of the data frame, which is critical for interoperability with other devices (like a PC's serial monitor or a Bluetooth module).

### A. Character Size (Data Bits)

The character size (number of data bits) is determined by a combination of three bits: UCSZ1:0 in UCSRC and UCSZ2 in UCSRB.

|Bits (UCSZ2:0)|Character Size|UCSZ1:0 (in UCSRC)|Common Use|
|---|---|---|---|
|000|5-bit|00|Legacy systems.|
|011|**8-bit**|**11**|**Standard/Default.** Used for ASCII characters.|
|111|9-bit|11|Used for address marking in multi-processor mode.|

### B. Parity Mode (Error Checking)

Parity is a simple error-checking method that adds one extra bit to the frame.

|Bits (UPM1:0)|Parity Mode|Function|
|---|---|---|
|**00**|**Disabled**|**Default.** No parity bit is added to the frame.|
|**10**|**Even Parity**|The transmitter sets the parity bit such that the total number of '1's in the data bits + parity bit is an even number.|
|**11**|**Odd Parity**|The transmitter sets the parity bit such that the total number of '1's in the data bits + parity bit is an odd number.|

### C. Stop Bit Select

The Stop Bit marks the end of the frame and returns the TXD line to the idle (HIGH) state.

|Bit (USBS)|Stop Bits|Common Use|
|---|---|---|
|**0**|**1 Stop Bit**|**Standard/Default.**|
|**1**|**2 Stop Bits**|Used for reliable data transmission, giving the receiver more time to process the byte.|
