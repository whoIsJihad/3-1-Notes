# AVR Timer0

**Tags:** #microcontroller #avr #timers #timer0

Timer0 is a general-purpose 8-bit timer/counter module in the ATmega32. Being 8-bit means its main counter register, [[TCNT0 Register]], can hold values from 0 to 255.

### Key Features

- **8-Bit Counter:** The counter value is stored in the [[TCNT0 Register]].
    
- **Modes of Operation:** Supports Normal, CTC, and two types of PWM modes. See [[Timer0 Modes of Operation]].
    
- **Prescaler:** The clock source can be divided using a [[Timer Prescaler]] to achieve longer time delays.
    
- **Interrupt Sources:** Can generate interrupts on [[Timer Overflow]] and Compare Match events.
    

### Associated Registers

- **[[TCNT0 Register]]**: The main 8-bit counter register.
    
- **[[TCCR0 Register]]**: The control register used to configure mode, prescaler, etc.
    
- **`OCR0`**: The 8-bit Output Compare Register (used in CTC and PWM modes).
    
- **[[TIMSK Register]]**: Used to enable/disable Timer0 interrupts.
    
- **[[TIFR Register]]**: Contains the interrupt flags for Timer0 events.
    

**Links:** [[Timer 1/AVR Timers and Counters]]