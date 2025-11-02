# UCSRB: The Core Control Register for ATmega32 USART

**Tags:** #microcontroller #atmega32 #usart #registers
The **UCSRB (USART Control and Status Register B)** is the most crucial register for enabling and controlling the functionality of the USART peripheral. Unlike UCSRA (which primarily reports status), UCSRB contains the **master switches** for enabling the Transmitter, the Receiver, and all associated Interrupts.

## 1. Hardware Enablement Bits (RXEN and TXEN)

These two bits are the power switches for the serial communication pins (PD0 and PD1). They must be set to '1' before any data transfer can happen.

|Bit|Name|Role|Practical Application (C Code)|
|---|---|---|---|
|**4**|RXEN|**Receiver Enable**|Set to '1' to enable the USART receiver hardware. This allows the chip to monitor the RXD pin (PD0) for incoming data frames.|
|**3**|TXEN|**Transmitter Enable**|Set to '1' to enable the USART transmitter hardware. This allows the chip to drive the TXD pin (PD1) with the outgoing serial signal.|

### C Code Setup Example (Enabling Both)

To make a device capable of two-way (full-duplex) communication, you must set both bits simultaneously during initialization:

```
// Enable both Receiver (RXEN) and Transmitter (TXEN)
UCSRB = (1 << RXEN) | (1 << TXEN);
```

## 2. Interrupt Enable Bits (The Non-Blocking Solution)

The top three bits of UCSRB enable the interrupt functionality for the USART. This is the professional way to handle serial communication, allowing the CPU to avoid the resource-wasting **busy-wait** loops you observed in the simulations (Simulation C).

|Bit|Name|Corresponding Flag (in UCSRA)|Function and CPU Efficiency|
|---|---|---|---|
|**7**|RXCIE|RXC|**Receive Complete Interrupt Enable.** When RXC=1, this bit causes the CPU to pause its current task and jump to the RXC Interrupt Service Routine (ISR) to read the new character. **Eliminates polling for incoming data.**|
|**6**|TXCIE|TXC|**Transmit Complete Interrupt Enable.** When TXC=1, this bit signals that the entire Q2 shift register is done. **Useful for signaling the end of a multi-byte transmission.**|
|**5**|UDRIE|UDRE|**UDR Empty Interrupt Enable.** When UDRE=1, this bit signals that the Q1 buffer is empty. **Crucial for efficient data streaming.** The ISR feeds the _next_ character into Q1 (UDR) the moment space becomes available.|

### C Code: The Power of UDRIE (Interrupt-Driven Transmission)

Instead of the inefficient polling loop: `while (!(UCSRA & (1 << UDRE)));`, a robust embedded system uses UDRIE to stream data.

#### Initialization (Enabling the Interrupts)

In the initialization routine, you enable the global interrupts (SREG) and the specific UDRIE bit:

```
// Enable Global Interrupts
sei(); // or set the I-bit in SREG

// Enable both Receiver and Transmitter
// AND enable the UDR Empty Interrupt (UDRIE)
UCSRB = (1 << RXEN) | (1 << TXEN) | (1 << UDRIE);
```

#### The Transmit ISR (Feeding the Pipeline)

When the hardware sets UDRE=1 (signaling Q1 is empty), the following ISR is executed:

```
// The Interrupt Service Routine for UDR Empty
ISR(USART_UDRE_vect) {
    static char data_to_send[] = "Hello World!";
    static int index = 0;

    if (index < sizeof(data_to_send) - 1) {
        // 1. Write the next byte to UDR
        UDR = data_to_send[index++];
        
        // 2. Hardware automatically clears the interrupt flag (UDRE)
        // and starts the process all over again.
    } else {
        // Stop the interrupt when the message is complete
        UCSRB &= ~(1 << UDRIE); 
    }
}
```

This interrupt-driven approach ensures the CPU is only interrupted for a few micro-seconds to load the next byte, spending the rest of its time on other, more critical tasks (like controlling motors or reading sensors).

## 3. Data Size and 9-bit Mode

The lower bits of UCSRB are used to define the size of the data frame, specifically enabling support for 9-bit characters (used in some legacy or multi-processor protocols).

|Bit|Register|Role|
|---|---|---|
|**2**|UCSZ2|**Character Size Bit 2.** This bit is the MSB (Most Significant Bit) of the character size setting, which works in conjunction with UCSZ1:0 in the UCSRC register.|
|**1**|RXB8|**9th Received Data Bit.** When 9-bit mode is enabled, this read-only bit holds the 9th bit of the last received character.|
|**0**|TXB8|**9th Transmitted Data Bit.** When 9-bit mode is enabled, the program must write the 9th bit of the data to this register immediately before writing the main 8 bits to UDR.|