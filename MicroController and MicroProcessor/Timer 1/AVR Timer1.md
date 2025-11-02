# AVR Timer1

**Tags:** #microcontroller #avr #timers #timer1

Timer1 is the most powerful and flexible of the three timers on the ATmega32. It is a **16-bit timer**, meaning its counter can hold values from 0 to 65535.

### Key Features

- **16-Bit Resolution:** The counter value is stored across two 8-bit registers, collectively known as [[TCNT1 Register]]. This allows for much longer time periods and higher precision than the 8-bit timers.
    
- **Dual Compare Units:** It has two independent Output Compare units, A and B, associated with the [[OCR1A and OCR1B Registers]].
    
- **Input Capture Unit:** A hardware feature to capture the timer's value on an external event. See [[Input Capture Mode]].
    
- **Advanced PWM Modes:** Supports a wider variety of more complex PWM modes compared to Timer0.
    
- **16-bit Registers:** Control, compare, and counter registers are 16-bit, accessed as high and low byte pairs (e.g., TCCR1A/B, TCNT1H/L).
    

### Associated Registers

- **[[TCNT1 Register]]**: The main 16-bit counter.
    
- **[[TCCR1A Register]] & [[TCCR1B Register]]**: A pair of registers that control the timer's mode and prescaler.
    
- **[[OCR1A and OCR1B Registers]]**: Two 16-bit Output Compare Registers.
    
- **[[ICR1 Register]]**: The 16-bit Input Capture Register.
    
- **[[TIMSK Register]]**: Used to enable/disable Timer1 interrupts.
    
- **[[TIFR Register]]**: Contains the interrupt flags for Timer1 events.
    

**Links:** [[Timer 1/AVR Timers and Counters]]