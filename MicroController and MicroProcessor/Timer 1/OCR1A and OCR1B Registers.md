# OCR1A and OCR1B Registers

**Tags:** #microcontroller #avr #timers #registers #timer1

[[AVR Timer1]] features two independent 16-bit **Output Compare Registers**: OCR1A and OCR1B.

- **OCR1A** is composed of `OCR1AH` and `OCR1AL`.
    
- **OCR1B** is composed of `OCR1BH` and `OCR1BL`.
    

### Functionality

These registers are used to store a value that is continuously compared against the main counter register, [[TCNT1]]. When `TCNT1`'s value equals the value in `OCR1A` or `OCR1B`, a **compare match** event occurs.

This event can be used to:

1. **Trigger an Interrupt:** If the corresponding interrupt enable bit (OCIE1A or OCIE1B) is set in [[TIMSK Register]], a compare match interrupt is generated.
    
2. **Manipulate an Output Pin:** The OC1A (PD5) and OC1B (PD4) pins can be configured to automatically set, clear, or toggle on a compare match. This is the basis for PWM generation.
    
3. **Define the Timer's TOP Value:** In certain [[Timer1 Modes of Operation]] (like many CTC and PWM modes), either `OCR1A` or the [[ICR1 Register]] can be used to define the TOP value that the counter counts up to, instead of the fixed maximum of 65535.
    

Accessing these 16-bit registers follows the same high-byte/low-byte procedure as the [[TCNT1 Register]].

**Links:** [[AVR Timer1]], [[Timer Interrupts]]