# Timer Overflow

**Tags:** #microcontroller #avr #timers #interrupts

Timer Overflow occurs when the timer's counter register increments past its maximum possible value and wraps around to zero.

- For an 8-bit timer (like [[AVR Timer0]]), the maximum value is 255 (0xFF). It overflows when it goes from 255 to 0.
    
- For a 16-bit timer (like [[AVR Timer1]]), the maximum value is 65535 (0xFFFF). It overflows when it goes from 65535 to 0.
    

When an overflow happens, the **Timer Overflow Flag (TOV)** for that specific timer is set to 1 in the [[TIFR Register]]. If the corresponding **Timer Overflow Interrupt Enable (TOIE)** bit is set in the [[TIMSK Register]], a Timer Overflow interrupt will be triggered, and the program will jump to the corresponding Interrupt Service Routine (ISR).

### Calculating Overflow Time

The time it takes for a timer to overflow can be calculated based on the CPU frequency, the prescaler value, and the timer's resolution (bit-width).

The time for one timer tick is:

```
Tick Time = Prescaler / CPU Frequency
```

The number of ticks for a full overflow is `2^n`, where `n` is the number of bits in the timer.

The total time to overflow is:

```
Time to Overflow = (2^n) * Tick Time
Time to Overflow = (2^n) * (Prescaler / CPU Frequency)
```

For example, for an 8-bit timer (`n=8`) with a 1MHz CPU clock and a 64 prescaler:

```
Tick Time = 64 / 1,000,000 Hz = 64 us
Steps for Overflow = 2^8 = 256
Time to Overflow = 256 * 64 us = 16,384 us = 16.384 ms
```

**Links:** [[Timer Interrupts]], [[TIFR Register]], [[TIMSK Register]]