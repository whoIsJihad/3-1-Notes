# Polling vs. Interrupts

**Tags:** #microcontroller #interrupts #polling #efficiency

When a microcontroller needs to interact with an external device (like a button or sensor), there are two primary methods for detecting when an event has occurred: **polling** and **interrupts**.

### Polling

Polling is the process of continuously checking the status of a device in a loop to see if it needs service.

```
while (1) {
    // Is the button pressed?
    if (is_button_pressed()) {
        // Service the button press
        handle_button();
    }
    // Continue with other tasks...
}
```

- **Pros**:
    
    - Simple to understand and implement.
        
- **Cons**:
    
    - **Highly Inefficient**: The CPU wastes a significant amount of time repeatedly checking for an event that rarely happens.
        
    - **Poor Scalability**: It becomes very complex and slow to poll multiple devices simultaneously.
        
    - **Poor Responsiveness**: There can be a delay between when an event occurs and when the CPU gets around to checking for it.
        

### Interrupts

An interrupt is a hardware-driven approach. The CPU doesn't check for an event; the external device notifies the CPU when it needs attention by sending an interrupt signal.

- **Pros**:
    
    - **Highly Efficient**: The CPU can perform other tasks and only spends time servicing the device when absolutely necessary. No CPU cycles are wasted.
        
    - **Excellent Responsiveness**: The CPU reacts to the event immediately.
        
    - **Priority Management**: The hardware defines a priority for each interrupt, ensuring that more critical events are handled first.
        
- **Cons**:
    
    - Slightly more complex to set up initially.
        
    - Can introduce difficult-to-debug issues if ISRs are not written carefully (e.g., race conditions).
        

For nearly all real-time applications, **interrupts are the superior and standard method**.

**Links**: [[ATmega32 Interrupts]], [[Interrupt Execution Flow]]