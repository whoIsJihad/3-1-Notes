**Tags:** #os #io #hardware #drivers

# The Canonical I/O Device

To manage the vast variety of hardware, the OS abstracts a device into a "canonical" or standard model. This model has two parts:

1. **Hardware Interface:** The set of registers that the OS can read from and write to. This is how the OS controls the device.
    
2. **Internals:** The device-specific implementation (e.g., microcontroller, memory, custom chips). The OS does not interact with this directly; it's abstracted away by the interface.
    

### The Hardware Interface

The interface typically consists of three key registers:

- **Status Register:** A read-only register that indicates the current state of the device (e.g., BUSY, READY, ERROR).
    
- **Command Register:** A write-only register used to tell the device to perform a specific task (e.g., READ_SECTOR, WRITE_SECTOR).
    
- **Data Register:** Used to transfer data to or from the device.
    

By reading and writing to these memory-mapped addresses, the OS can control any device that conforms to this model.

**Links:** [[I_O Devices MOC]], [[Communicating with Devices]]