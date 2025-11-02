# AVR Timers and Counters

**Tags:** #microcontroller #avr #timers #index

Timers and counters are fundamental peripherals in AVR microcontrollers like the ATmega32. They are essentially hardware counters that can increment or decrement their value on each clock cycle. This capability allows for precise timing of events, generation of waveforms (like PWM), and measuring the duration of external events without consuming CPU cycles in busy-wait loops.

The ATmega32 has three timers:

- **Timer0:** An 8-bit timer.
    
- **Timer1:** A 16-bit timer with more advanced features.
    
- **Timer2:** An 8-bit timer that can run asynchronously from the system clock, making it suitable for real-time clock applications.
    

### Core Concepts

- [[Timer Prescaler]]
    
- [[Timer Overflow]]
    
- [[Timer Interrupts]]
    

### Timer/Counter 0 (8-bit)

- [[AVR Timer0]]
    
- [[TCNT0 Register]]
    
- [[TCCR0 Register]]
    
- [[Timer0 Modes of Operation]]
    

### Timer/Counter 1 (16-bit)

- [[AVR Timer1]]
    
- [[TCNT1 Register]]
    
- [[TCCR1A Register]]
    
- [[TCCR1B Register]]
    
- [[OCR1A and OCR1B Registers]]
    
- [[ICR1 Register]]
    
- [[Timer1 Modes of Operation]]
    
- [[Input Capture Mode]]
    

### Timer/Counter 2 (8-bit Asynchronous)

- [[AVR Timer2]]
    
- [[TCCR2 Register]]
    
- [[ASSR Register]]
    

### General Purpose Timer Registers

- [[TIMSK Register]]
    
- [[TIFR Register]]