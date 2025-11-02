# Timer0 Fast PWM Mode

**Tags:** #microcontroller #avr #timers #timer0 #pwm

Fast PWM (Pulse Width Modulation) mode is used to generate a high-frequency PWM signal.

### How it Works

1. The **WGM01** and **WGM00** bits in [[TCCR0 Register]] are both set to 1.
    
2. The timer counts from 0 up to 255 (MAX).
    
3. Unlike other modes, the timer is **never cleared** in the middle of a cycle. It always completes the full 0-255 cycle.
    
4. The **Output Compare Register (OCR0)** holds the duty cycle value.
    
5. The behavior of the OC0 output pin depends on the **COM01:00** bits in `TCCR0`:
    
    - **Non-inverting mode (COM01=1, COM00=0):** The output (OC0) is cleared (set to LOW) when `TCNT0` matches `OCR0`. The output is set (to HIGH) when `TCNT0` wraps around from 255 to 0. The pulse is HIGH from the start of the period until the compare match.
        
    - **Inverting mode (COM01=1, COM00=1):** The output (OC0) is set (to HIGH) when `TCNT0` matches `OCR0`. The output is cleared (to LOW) when `TCNT0` wraps around from 255 to 0.
        

This is called "fast" PWM because it performs a single-slope count (only counts up), resulting in a higher maximum frequency than [[Timer0 Phase Correct PWM Mode]].

**Links:** [[Timer0 Modes of Operation]]