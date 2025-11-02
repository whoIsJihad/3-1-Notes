# Serial Communication in ATmega32

**Tags:** #microcontroller #atmega32 #serial #communication #embedded

Serial communication is a fundamental process where data is sent one bit at a time over a single wire or channel. This is essential for a microcontroller to communicate with a PC, sensors, and other microcontrollers, especially over long distances where using fewer wires is critical.

The ATmega32 has three built-in hardware modules for handling different types of serial communication.

### Core Concepts

- **[[Serial Communication Fundamentals]]**: Explains the basics: serial vs. parallel, synchronous vs. asynchronous, and how data is framed.
    

### ATmega32 Serial Protocols

1. **[[USART Communication]]**: The most common protocol for PC-to-microcontroller communication. It's highly flexible and can operate in both synchronous and asynchronous modes.
    
2. **[[SPI Communication]]**: A faster, synchronous protocol ideal for communicating with peripheral devices like SD cards, displays, and sensors over short distances.
    
3. **[[TWI Communication (I2C)]]**: A two-wire protocol designed for connecting multiple devices (like sensors and memory chips) on a shared bus, where each device has a unique address.
    

### How to Add Images

- [[How to Add Images in Obsidian]]