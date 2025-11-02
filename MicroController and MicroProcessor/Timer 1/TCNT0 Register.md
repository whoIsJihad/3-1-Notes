# TCNT0 Register

**Tags:** #microcontroller #avr #timers #registers #timer0

The **Timer/Counter0 Register (TCNT0)** is the core 8-bit counter for [[AVR Timer0]].

### Functionality

- It is an 8-bit read/write register.
    
- The value of TCNT0 increments with each tick of the timer clock (which is determined by the [[Timer Prescaler]] settings in [[TCCR0 Register]]).
    
- You can read the current value of TCNT0 at any time to see how many ticks have passed.
    
- You can also write a value to TCNT0 to start the count from a specific number other than 0. This is a common technique in [[Timer0 Normal Mode]] to achieve a specific delay period.
    

When the counter increments from 255 (0xFF) back to 0, a [[Timer Overflow]] event occurs, and the TOV0 flag in the [[TIFR Register]] is set.

**Links:** [[AVR Timer0]]