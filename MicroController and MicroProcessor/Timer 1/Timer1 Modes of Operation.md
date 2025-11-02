# Timer1 Modes of Operation

**Tags:** #microcontroller #avr #timers #timer1

[[AVR Timer1]] has a much larger selection of operating modes than the 8-bit timers. These modes are selected by the four **Waveform Generation Mode (WGM13:10)** bits, which are split between the [[TCCR1A Register]] and [[TCCR1B Register]].

### Key Modes

Some of the most commonly used modes include:

- **Normal Mode:** Counts from 0 to 65535 (MAX) and overflows.
    
- **CTC (Clear Timer on Compare Match):** The counter resets to 0 when [[TCNT1]] matches either `OCR1A` or [[ICR1 Register]]. This is used for generating specific frequencies.
    
- **Fast PWM:** Single-slope PWM generation. The TOP value can be fixed (e.g., 8-bit, 9-bit, 10-bit) or variable (defined by `ICR1` or `OCR1A`). This allows for flexible control over both PWM frequency and resolution.
    
- **Phase Correct PWM:** Dual-slope (up/down counting) PWM generation. Similar to Fast PWM, the TOP value can be fixed or variable. This produces symmetrical waveforms ideal for motor control.
    
- **Phase and Frequency Correct PWM:** A variation of Phase Correct PWM where the TOP value is defined by `ICR1`. The `OCR1x` registers are only updated at the bottom of the counting cycle, avoiding certain types of glitches.
    
- **[[Input Capture Mode]]**: Not a WGM mode itself, but a feature that works in conjunction with other modes to measure external signal timings.
    

The datasheet provides a complete table (Table 48 in the ATmega32 datasheet) detailing all 16 mode configurations. The choice of mode depends entirely on the application's requirements for timing, frequency generation, or signal modulation.

**Links:** [[AVR Timer1]], [[TCCR1A Register]], [[TCCR1B Register]]