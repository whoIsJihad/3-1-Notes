**Tags:** #os #io #interrupts #cpu

# Device Interaction: Interrupts

Interrupts are a more efficient way for the OS to handle I/O operations, especially with slower devices. Instead of polling, the CPU can switch to other tasks and be notified by the device when the I/O is complete.

### Protocol Flow

1. **Issue Request:** The OS issues a request (e.g., read from disk) to the device.
    
2. **Sleep:** The OS puts the requesting process to sleep and context-switches to another ready process. The CPU is now doing useful work instead of waiting.
    
3. **Device Work:** The device performs the requested operation.
    
4. **Interrupt:** When the operation is complete, the device hardware sends an interrupt signal to the CPU.
    
5. **Handle Interrupt:** The CPU finishes its current instruction, saves its context, and jumps to a pre-defined Interrupt Service Routine (ISR).
    
6. **Wake Process:** The ISR handles the interrupt (e.g., moves data) and wakes up the sleeping process, making it eligible to run again.
    

### Analysis

- **Pros:** Greatly improves CPU utilization. The CPU can execute other processes while the slow I/O device is working.
    
- **Cons:** Incurs overhead from context switching and interrupt handling. If a device is extremely fast, the cost of the interrupt handling might be greater than the time saved. For very fast devices, [[Device Interaction - Polling|Polling]] can sometimes be more efficient.
    

**Links:** [[I_O Devices MOC]], [[Device Interaction - DMA (Direct Memory Access)]]