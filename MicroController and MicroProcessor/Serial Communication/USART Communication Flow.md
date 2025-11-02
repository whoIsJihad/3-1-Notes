# USART Communication

Tags: #microcontroller #atmega32 #usart #art #serial

The **Universal Synchronous and Asynchronous Receiver and Transmitter (USART)** is the ATmega32's primary communication peripheral. It provides a highly flexible, hardware-managed solution for serial data exchange. While capable of synchronous mode, its most common use is in **asynchronous mode**, typically referred to as **UART**.

It serves as the interface for the microcontroller to exchange data with external devices such as PCs (via USB/Serial adapters), GPS modules, or Bluetooth modules.

## Key Features

- **Full-Duplex:** Capable of simultaneous data transmission and reception using separate dedicated registers and I/O pins.
    
- **Pins:**
    
    - **RXD** (Receive Data) on pin PD0.
        
    - **TXD** (Transmit Data) on pin PD1.
        
- **Configurable Framing:** The user defines the structure of the data unit, including data size (5-9 bits), parity control (none, even, or odd), and stop bits (1 or 2).
    
- **Baud Rate Generation:** Achieved via the **UBRR** register and an internal generator, which creates the precise clock timing required for sequential bit transfer.
    
- **Interrupt Support:** Offers interrupts on key events, crucial for efficient, non-blocking code: Transmit Complete, Transmit Buffer Empty, and Receive Complete.
    

## Detailed Narrative: How the USART Frame Sending Works

The USART on the ATmega32 is a specialized hardware state machine designed to manage the sequential, bit-by-bit transfer of data without direct CPU intervention after the initial byte is written.

### Phase 1: Initialization and Synchronization (The Foundation)

Accurate communication relies entirely on timing, which is established first:

1. **Baud Rate Calculation:** A UBRR value is calculated based on your desired communication speed (baud rate, e.g., 9600 bps) and your main microcontroller clock frequency (fCPU​).
    
2. **UBRR Register Programming:** This value is loaded into the **UBRR (USART Baud Rate Register)**. This register configures an internal **Baud Rate Generator**.
    
3. **Baud Rate Generator:** This generator creates the precise clock signal that dictates the _rate_ at which each single bit is shifted out. This timing must be nearly identical on both the sending and receiving devices.
    
4. **Framing Configuration:** In the UCSRC register, you define the structure of the frame: data size (UCSZ0:2), parity mode (UPM0:1), and the number of stop bits (USBS).
    

### Phase 2: Data Transfer and Double Buffering

This process moves the data from your software into the specialized hardware buffers.

1. **The Write Command:** Your C program executes a command to write the data byte (e.g., `0x41` for 'A') to the data register:
    
    ```
    UDR = 'A'; 
    ```
    
2. **Internal Transfer:** The data immediately moves from the UDR (which acts as an input/output gateway) into a hidden internal register called the **Transmit Buffer Register**.
    
3. UDRE **Flag Set (Transmit Buffer Empty):** As soon as the data leaves the UDR for the Transmit Buffer, the **UDRE (USART Data Register Empty) flag** in the UCSRA register is set to '1'. This is the CPU's signal that it can safely load the _next_ byte of data without causing an overflow or delaying the current transmission. This **double-buffering** allows for efficient, high-speed data streaming.
    

### Phase 3: Hardware Frame Assembly and Serialization (The 'Sending Frame Stuff')

The data moves from the Transmit Buffer Register into the **Transmit Shift Register**. This shift register is the core component that converts the 8-bit parallel data into a sequential, one-bit-at-a-time stream.

The hardware logic automatically constructs the complete serial frame:

1. **Idle State:** Before transmission, the TXD line rests in the logical **HIGH** state (logic '1').
    
2. **Start Bit (1 Bit, Logic '0'):** The first action is pulling the TXD line LOW (logic '0') for exactly one Baud Rate Generator clock cycle. This abrupt HIGH-to-LOW transition signals to the receiver: **"A new data byte is beginning now."**
    
3. **Data Bits (5-9 Bits):** The actual user data byte is shifted out, following the Start Bit. By convention, the **Least Significant Bit (LSB)** is always sent first.
    
4. **Parity Bit (0 or 1 Bit):** If parity is enabled, the hardware calculates and inserts this bit to ensure the total number of '1's (including the parity bit) matches the configured scheme (Even or Odd).
    
5. **Stop Bit(s) (1 or 2 Bits, Logic '1'):** The final bit(s) are sent as a transition back to the logical **HIGH** state (logic '1'). This signals the **end of the frame** and returns the line to the necessary idle state.
    

### Phase 4: Signalling Completion to the CPU

1. TXC **Flag Set (Transmit Complete):** When the very last **Stop Bit** has been entirely shifted out of the TXD pin, the **TXC (Transmit Complete) flag** in the UCSRA register is set to '1'.
    
2. **Interrupt Handling:** If the TXCIE bit in UCSRB is set, this flag triggers an interrupt, notifying the CPU that the entire operation is finished and the Shift Register is totally clear.
    

## Registers

The USART is controlled by a set of dedicated registers:

- **USART Control and Status Registers (UCSRA,B,C)**: Used to enable the peripheral, set operating modes, configure framing, enable interrupts, and monitor status flags (UDRE,TXC,RXC).
    
- **USART Baud Rate Registers (UBRR)**: Used to store the value necessary to program the Baud Rate Generator.
    
- Links:
  - [[Serial Communication in ATmega32]]
  - [[Asynchronous Data Recovery]]
