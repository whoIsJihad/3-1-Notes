# Programming Interrupts in C for AVR

**Tags:** #microcontroller #avr #C-code #interrupts

Programming interrupts in C for an ATmega microcontroller follows a consistent, five-step process.

### The 5 Steps to Enable an Interrupt

1. **Include the Interrupt Header**: This file contains the necessary definitions for interrupts, including the `ISR()` macro and vector names.
    
    ```
    #include <avr/interrupt.h>
    ```
    
2. **Write the Interrupt Service Routine (ISR)**: This is the function that will be executed automatically when the interrupt occurs. The name of the interrupt vector (e.g., `INT1_vect`, `ADC_vect`) must match the one from the [[ATmega32 Interrupt Vector Table]].
    
    ```
    ISR(INT1_vect) {
        // Code to execute when INT1 occurs
        // Keep this code as short and fast as possible!
    }
    ```
    
3. **Configure the Interrupt Trigger**: Set the bits in the specific control registers to define what event triggers the interrupt. For [[External Interrupts]], this means configuring `MCUCR` to trigger on a rising edge, falling edge, or low level. For other peripherals like timers or the ADC, you configure their respective control registers.
    
4. **Enable the Specific Interrupt**: Set the enable bit for the specific interrupt source. For external interrupts, this is done in the `GICR` register. For other peripherals, this is usually a bit in their control register (e.g., `ADIE` in `ADCSRA` for the ADC).
    
5. **Enable Global Interrupts**: This is the master switch. You must set the Global Interrupt Enable bit in the Status Register (`SREG`). The easiest way to do this is with the `sei()` macro. No interrupts will fire until this is called.
    
    ```
    sei(); // Set Global Interrupt Enable
    ```
    

After these five steps, the microcontroller is ready to respond to the configured interrupt. The main loop can then be used for lower-priority tasks or can even be empty (`while(1);`).

**Links**: [[ATmega32 Interrupts]], [[Interrupt Control Registers]], [[The volatile Keyword]]