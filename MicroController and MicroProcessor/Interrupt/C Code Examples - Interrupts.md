# C Code Examples - Interrupts

**Tags:** #microcontroller #avr #C-code #interrupts #snippets

Here are practical C code examples for setting up external interrupts on an ATmega32.

### Example 1: Toggle PORTB on Falling Edge of INT1

This program will flip all the bits on PORTB every time the signal on pin PD3 (INT1) goes from high to low. This is a classic example of handling a button press.

```
#include <avr/io.h>
#include <avr/interrupt.h>

// Step 2: Write the ISR for the INT1 vector
ISR(INT1_vect) {
    // Toggle all bits on PORTB
    PORTB = ~PORTB;
}

int main(void) {
    // Set PORTB as output
    DDRB = 0xFF;
    // Set an initial value for PORTB
    PORTB = 0x55; // 01010101 in binary
    
    // PD3 (INT1) is an input by default, but it's good practice
    // to enable its pull-up resistor if connected to a button to ground.
    PORTD |= (1 << PD3);

    // Step 3: Configure INT1 to trigger on a falling edge
    // Set ISC11=1 and ISC10=0 in MCUCR
    MCUCR |= (1 << ISC11);
    MCUCR &= ~(1 << ISC10);

    // Step 4: Enable the INT1 interrupt in GICR
    GICR |= (1 << INT1);

    // Step 5: Enable global interrupts
    sei();

    // The main loop can be empty or do other tasks.
    // The CPU will automatically handle the interrupt.
    while (1) {
        // Low-priority tasks can go here
    }
}
```

**Links**: [[ATmega32 Interrupts]], [[External Interrupts]]