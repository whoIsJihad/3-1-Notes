**Tags:** #os #io #hardware #architecture


A typical computer's I/O architecture is built around a hierarchy of buses that connect the CPU, memory, and various peripheral devices.

### Prototypical System Architecture

- **CPU:** The central processing unit.
    
- **Memory Bus:** A high-speed, proprietary bus that connects the CPU directly to main memory (RAM).
    
- **General I/O Bus:** A standardized bus, like PCI, that connects high-speed devices to the system.
    
- **Peripheral I/O Bus:** Slower buses, like USB, SATA, or SCSI, that connect a wide range of external devices. These buses connect to the General I/O Bus.
    

The OS must be able to manage communication across this hierarchy to control devices.

**Links:** [[I_O Devices MOC]]