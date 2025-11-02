# Timer0 Normal Mode

**Tags:** #microcontroller #avr #timers #timer0

Normal Mode is the simplest mode of operation for [[AVR Timer0]].

### How it Works

1. The **WGM01** and **WGM00** bits in [[TCCR0 Register]] are both set to 0.
    
2. The [[TCNT0]] register starts counting from 0 upwards.
    
3. When the count reaches 255 (0xFF), the next clock tick causes it to wrap around to 0.
    
4. At the exact moment of wrapping around, the **Timer Overflow Flag (TOV0)** in the [[TIFR Register]] is set.
    
5. If the **Timer Overflow Interrupt Enable (TOIE0)** bit in [[TIMSK Register]] is set, a timer overflow interrupt is triggered.
    

This mode is commonly used to generate fixed time delays by using the overflow interrupt.

### Example C Code

This code configures Timer0 to overflow and trigger an interrupt, which then toggles an LED on PORTC pin 0.

```
#include <avr/io.h>
#include <avr/interrupt.h>

int main(void) {
    DDRC |= (1 << PC0); // Set PC0 as an output

    // Configure Timer0 in Normal Mode
    TCCR0 = (1 << CS02) | (1 << CS00); // Set prescaler to 1024
    // TCNT0 is 0 by default

    TIMSK |= (1 << TOIE0); // Enable Timer0 Overflow interrupt

    sei(); // Enable global interrupts

    while (1) {
        // Main loop does nothing, all work is in the ISR
    }
}

// Interrupt Service Routine for Timer0 Overflow
ISR(TIMER0_OVF_vect) {
    PORTC ^= (1 << PC0); // Toggle the LED
}
```

**Links:** [[Timer0 Modes of Operation]], [[Timer Overflow]]