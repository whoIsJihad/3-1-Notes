**Tags:** #os #io #dma #hardware

# Device Interaction: DMA (Direct Memory Access)

Even with [[Device Interaction - Interrupts|interrupts]], the CPU is still responsible for the tedious task of copying large chunks of data byte-by-byte from memory to the device's data register (or vice versa). This can overburden the CPU.

**Direct Memory Access (DMA)** solves this by introducing a special hardware component, the **DMA controller**, which handles these large data transfers without involving the CPU.

### Protocol Flow

1. **Setup:** The CPU configures the DMA controller. It provides:
    
    - The source memory address.
        
    - The destination I/O device address.
        
    - The number of bytes to transfer.
        
2. **Transfer:** The CPU is now free to perform other tasks. The DMA controller takes over the memory bus and performs the data transfer directly between main memory and the device.
    
3. **Interrupt:** Once the entire block of data has been transferred, the DMA controller sends an interrupt to the CPU.
    
4. **Completion:** The CPU's interrupt handler acknowledges the completion, and the I/O operation (e.g., writing the data to disk) can now begin.
    

### Analysis

- **Pros:** Frees the CPU from the low-level work of data copying, dramatically improving system performance for bulk data transfers.
    
- **Cons:** Requires dedicated DMA hardware.
    

**Links:** [[I_O Devices MOC]], [[Device Interaction - Interrupts]]