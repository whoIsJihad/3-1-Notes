# AVR C Code Examples - I/O

**Tags:** #microcontroller #avr #C-code #snippets

### 1. Blink an LED

Toggles pin PB0 on and off.

```
#define F_CPU 1000000UL
#include <avr/io.h>
#include <util/delay.h>

int main(void) {
    DDRB = 0b00000001;
    while(1) {
        PORTB = 0b00000001;
        _delay_ms(500);
        PORTB = 0b00000000;
        _delay_ms(500);
    }
}
```

### 2. Animate 8 LEDs

Shifts a single lit LED across Port B.

```
#define F_CPU 1000000UL
#include <avr/io.h>
#include <util/delay.h>

int main(void) {
    unsigned char c = 0x01;
    DDRB = 0xFF;
    while(1) {
        PORTB = c;
        _delay_ms(200);
        c = c << 1;
        if (c == 0) {
            c = 0x01;
        }
    }
}
```

### 3. Simple Counter with Push Button

Increments a counter on PORTB when a button on PA0 is pressed.

```
#define F_CPU 1000000UL
#include <avr/io.h>
#include <util/delay.h>

int main(void) {
    unsigned char count = 0;
    // Set PA0 as input with pull-up resistor enabled
    DDRA = 0xFE; 
    PORTA = 0x01;
    
    // Set Port B as output
    DDRB = 0xFF;
    PORTB = count;

    while(1) {
        // Check if button on PA0 is pressed (reads LOW)
        if (!(PINA & 0x01)) {
            _delay_ms(50); // Debounce delay
            
            // Check again to confirm press
            if (!(PINA & 0x01)) {
                count++;
                PORTB = count;
                // Wait until button is released
                while(!(PINA & 0x01));
            }
        }
    }
}
```