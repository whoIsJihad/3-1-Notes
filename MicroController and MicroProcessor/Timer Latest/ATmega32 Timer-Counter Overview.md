# ATmega32 Timer/Counter Overview

**Tags:** #atmega32 #timers #pwm #embedded

The ATmega32 microcontroller comes equipped with three powerful and flexible hardware timers, each with slightly different capabilities. Understanding their differences is key to choosing the right tool for the job.

All timers share common functionalities like generating delays (Normal Mode), creating PWM signals, and counting external events.

|Feature|Timer0|Timer1|Timer2|
|---|---|---|---|
|**Size**|**8-bit**|**16-bit**|**8-bit**|
|**Counter Register**|`TCNT0`|`TCNT1`|`TCNT2`|
|**Max Count Value**|255 (0xFF)|65535 (0xFFFF)|255 (0xFF)|
|**Prescaler Options**|1, 8, 64, 256, 1024|1, 8, 64, 256, 1024|1, 8, 32, 64, 128, 256, 1024|
|**Output Compare Channels**|1 (`OCR0`)|2 (`OCR1A`, `OCR1B`)|1 (`OCR2`)|
|**Special Feature**|-|**Input Capture Unit**|Asynchronous Operation|
|**Primary Use Case**|Basic delays, simple PWM.|High-resolution timing, complex PWM, frequency/period measurement.|Real-time clock (RTC) functions.|

### Key Differences Explained

- **Size (8-bit vs. 16-bit):** This is the most important distinction.
    
    - An **8-bit timer** (Timer0, Timer2) can only count from 0 to 255. It overflows very quickly, making it suitable for short delays or generating high-frequency PWM.
        
    - A **16-bit timer** (Timer1) can count from 0 to 65535. This allows it to measure much longer time intervals before overflowing, making it ideal for creating long, precise delays without needing a software counter to track many overflows.
        
- **Input Capture Unit (Timer1 Only):** This is a powerful feature unique to Timer1 on the ATmega32. It allows the timer to automatically record its current count value (`TCNT1`) into a special register (`ICR1`) when an external event occurs on the `ICP1` pin. This is the hardware mechanism for precisely measuring the period or pulse width of an external signal.
    
- **Asynchronous Operation (Timer2 Only):** Timer2 can be clocked from an external "watch" crystal (32.768 kHz) instead of the main system clock. This allows it to function as a **Real-Time Clock (RTC)**, keeping accurate track of time even if the main CPU is put into a deep sleep mode to save power.
    

For most general-purpose and high-precision timing tasks covered in these notes, **Timer1 is the most capable and versatile option.**

**Links:** [[AVR Timers and Counters]]