**Tags:** #os #io #drivers #abstraction

# Device Driver Abstraction

A single operating system needs to support a wide variety of devices (SCSI disks, IDE disks, USB drives, etc.), each with its own unique register layout and command set. It would be impractical to write the entire file system to understand every single type of device.

To solve this, the OS uses a layer of **abstraction**. A **device driver** is a specific piece of software that understands how to communicate with one particular type of device or a family of devices (e.g., an IDE driver).

### Role of the Driver

- **Encapsulation:** The driver encapsulates the device-specific details.
    
- **Standard Interface:** It presents a standard, high-level interface to the rest of the OS (e.g., `read_block`, `write_block`).
    
- **Translation:** It translates these generic commands into the specific sequence of register reads and writes that the hardware requires.
    

This allows the file system to simply request `write_block(5, data)` without needing to know if the underlying hardware is IDE, SCSI, or a USB stick.

**Links:** [[I_O Devices MOC]], [[IDE Device Driver Protocol]]