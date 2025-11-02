# Input Capture Mode

**Tags:** #microcontroller #avr #timers #timer1

Input Capture is a powerful feature of [[AVR Timer1]] that allows the microcontroller to record the exact time an external event occurs without CPU intervention.

### How it Works

1. An external signal is applied to the **Input Capture Pin (ICP1)**, which is located on pin PD6 of the ATmega32.
    
2. The **Input Capture Edge Select (ICES1)** bit in [[TCCR1B Register]] is configured to trigger on either a rising (1) or falling (0) edge of this signal.
    
3. When the selected edge is detected on the ICP1 pin, two things happen simultaneously in hardware:
    
    - The current 16-bit value of the timer, [[TCNT1]], is copied into the **Input Capture Register ([[ICR1 Register]])**.
        
    - The **Input Capture Flag (ICF1)** is set in the [[TIFR Register]].
        
4. If the **Input Capture Interrupt Enable (TICIE1)** bit in [[TIMSK Register]] is set, an interrupt is triggered.
    

### Application

This feature is extremely useful for measuring properties of external signals, such as:

- **Frequency:** Measure the time between two consecutive rising edges. The difference between two ICR1 captures gives the period, and frequency is the reciprocal of the period.
    
- **Pulse Width:** Capture the time on a rising edge, then reconfigure for a falling edge and capture the time again. The difference is the width of the high pulse.
    

An optional **Noise Canceler (ICNC1 bit in TCCR1B)** can be enabled to filter out short glitches on the input pin.

**Links:** [[AVR Timer1]], [[TCCR1B Register]], [[ICR1 Register]]