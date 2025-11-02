# USART Communication

**Tags:** #microcontroller #atmega32 #usart #uart #serial

The **Universal Synchronous and Asynchronous Receiver and Transmitter (USART)** is a highly flexible serial communication peripheral on the ATmega32. While it supports synchronous mode, it is most commonly used in asynchronous mode, often referred to as **UART**.

It's the primary method for communicating with a computer's serial monitor or with other devices like GPS modules or Bluetooth modules.

### Key Features

- **Full-Duplex**: Can send and receive data at the same time using two wires.
    
- **Pins**:
    
    - `RXD` (Receive Data) on pin **PD0**.
        
    - `TXD` (Transmit Data) on pin **PD1**.
        
- **Configurable Framing**: You can program the number of data bits (5-9), parity (none, even, or odd), and number of stop bits (1 or 2).
    
- **Baud Rate Generation**: A programmable baud rate generator allows you to set the communication speed to match the other device.
    
- **Interrupt Support**: Can generate interrupts on transmit complete, transmit buffer empty, and receive complete events.
    

### How it Works

To send data, your program writes a byte to the **UDR (USART Data Register)**. The USART hardware then automatically adds the start bit, parity bit, and stop bit(s) and shifts the entire frame out on the `TXD` pin one bit at a time.

To receive data, the hardware monitors the `RXD` pin. When it detects a valid frame, it strips the start/stop bits, checks the parity, and places the received data byte into the `UDR` for your program to read.

### Registers

The USART is controlled by a set of registers:

- [[USART Control and Status Registers (UCSRA, B, C)]]
    
- [[USART Baud Rate Registers (UBRR)]]
    

**Links**: [[Serial Communication in ATmega32]]