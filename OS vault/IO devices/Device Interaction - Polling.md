**Tags:** #os #io #polling #cpu

# Device Interaction: Polling

Polling, also known as Programmed I/O (PIO), is the simplest method for an OS to interact with a device. The CPU repeatedly checks the device's status register in a tight loop, waiting for it to become ready.

### Protocol Flow

1. **Loop:** The CPU continuously reads the status register.
    
2. **Wait:** It waits until the BUSY bit in the register is cleared.
    
3. **Transfer:** Once the device is ready, the CPU writes data to the data register.
    
4. **Command:** The CPU writes a command to the command register to start the operation.
    
5. **Wait Again:** The CPU polls the status register again, waiting for the device to finish the command.
    

### Example Code

```
// Wait for device to be ready
while (STATUS_REGISTER == BUSY) {
    // do nothing
}

// Send data and command
DATA_REGISTER = data;
COMMAND_REGISTER = SOME_COMMAND;

// Wait for device to complete the command
while (STATUS_REGISTER == BUSY) {
    // do nothing
}
```

### Analysis

- **Pros:** Very simple to implement and understand.
    
- **Cons:** Extremely inefficient. The CPU is stuck in a busy-wait loop, consuming 100% of its time while doing no useful work. This is especially wasteful for slow devices.
    

**Links:** [[I_O Devices MOC]], [[Device Interaction - Interrupts]]