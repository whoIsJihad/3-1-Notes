# TWI Communication (I2C)

**Tags:** #microcontroller #atmega32 #twi #i2c #serial

The **Two-Wire Interface (TWI)** is the ATmega32's implementation of the popular **I²C (Inter-Integrated Circuit)** communication protocol. It's a synchronous, multi-master, multi-slave bus that is ideal for connecting multiple devices together using just two wires.

### Key Features

- **Two Wires**:
    
    - `SCL` (Serial Clock) on pin **PC0**: The clock line, always driven by the current bus master.
        
    - `SDA` (Serial Data) on pin **PC1**: The bidirectional data line.
        
- **Addressing**: Each device (slave) on the TWI bus has a unique 7-bit address. This allows the master to communicate with a specific device out of many on the same two wires. Up to 128 devices can share the bus.
    
- **Master-Slave Architecture**: One device (the master, usually your ATmega32) initiates and controls all communication.
    

### How it Works

1. **Start Condition**: The master initiates communication by pulling the `SDA` line low while the `SCL` line is high.
    
2. **Address Frame**: The master sends the 7-bit address of the slave it wants to talk to, followed by a read/write bit (`0` for write, `1` for read).
    
3. **Acknowledge (ACK)**: The addressed slave, recognizing its address, pulls the `SDA` line low for one clock cycle to acknowledge the master. All other slaves ignore the rest of the transaction.
    
4. **Data Frames**: The master and slave exchange data bytes, with the receiver sending an `ACK` bit after each byte.
    
5. **Stop Condition**: When the communication is finished, the master generates a stop condition by releasing the `SDA` line to go high while the `SCL` line is high.
    

TWI is more complex to program at a low level than USART or SPI, but it is extremely powerful for building systems with multiple sensors or I/O expanders.

**Links**: [[Serial Communication in ATmega32]]