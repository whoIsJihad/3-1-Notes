# Serial Communication Fundamentals

**Tags:** #serial #communication #theory #embedded

Understanding the basic concepts of data transfer is key to using any serial protocol.

### Serial vs. Parallel Communication

- **Parallel**: Sends multiple bits of data at once over multiple wires. It's very fast for short distances but expensive and complex for long distances due to the number of wires and potential for signal timing issues (skew).
    
- **Serial**: Sends data one single bit at a time over one wire. It's more cost-effective and reliable over longer distances, making it the standard for most device-to-device communication.
    

### Synchronous vs. Asynchronous Communication

This defines how the sender and receiver stay in sync.

- **Synchronous**: The sender and receiver share a common clock signal on a separate wire. The receiver knows exactly when to read the data line based on the clock ticks provided by the sender. This is generally faster and more reliable.
    
    - _Example_: [[SPI Communication]]
        
- **Asynchronous**: There is no shared clock signal. Instead, the sender and receiver must agree on a timing rate (the **baud rate**) beforehand. The data is "framed" with special **start** and **stop** bits that tell the receiver when a new piece of data begins and ends, allowing it to synchronize for a short period.
    
    - _Example_: [[USART Communication]]
        

### Data Framing (for Asynchronous Communication)

To ensure the receiver can understand the data without a shared clock, each chunk of data (usually a byte) is wrapped in a "frame."

- **Idle State**: The communication line is held at a high voltage level when no data is being sent.
    
- **Start Bit**: A single low bit that signals the start of a new frame.
    
- **Data Bits**: The actual data (typically 5 to 9 bits), sent from Least Significant Bit (LSB) to Most Significant Bit (MSB).
    
- **Parity Bit (Optional)**: An extra bit used for simple error checking.
    
- **Stop Bit(s)**: One or two high bits that signal the end of the frame and return the line to the idle state.
    

The receiver detects the falling edge of the start bit and then samples the data line at the agreed-upon baud rate to read the data bits.

**Links**: [[Serial Communication in ATmega32]]