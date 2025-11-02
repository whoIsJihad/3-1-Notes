# AVR Timer2

**Tags:** #microcontroller #avr #timers #timer2 #rtc

Timer2 is another 8-bit timer in the ATmega32, similar in many ways to [[AVR Timer0]]. However, it has one critical feature that distinguishes it: the ability to run **asynchronously**.

### Key Features

- **8-Bit Counter:** Like Timer0, its counter (`TCNT2`) and compare register (`OCR2`) are 8-bit.
    
- **Standard Modes:** Supports Normal, CTC, Fast PWM, and Phase Correct PWM modes, similar to Timer0.
    
- **Asynchronous Operation:** This is the main advantage of Timer2. It can be clocked by an external low-frequency crystal (typically a 32.768 kHz watch crystal) connected to the TOSC1 and TOSC2 pins. This allows it to function as a **Real-Time Clock (RTC)** that keeps time accurately, even if the main system clock frequency changes or the device enters a low-power sleep mode where the main clock is stopped.
    

### Associated Registers

- **`TCNT2`**: The main 8-bit counter register.
    
- **[[TCCR2 Register]]**: The control register.
    
- **`OCR2`**: The 8-bit Output Compare Register.
    
- **[[ASSR Register]]**: **Asynchronous Status Register**. This register is unique to Timer2 and is used to enable and monitor the asynchronous operation mode.
    

When used as an RTC, the 32.768 kHz clock source combined with a prescaler of 128 results in exactly one timer overflow interrupt per second.

```
Clock Ticks per Second = 32768 / 128 = 256
Timer Overflow = 256 ticks
Result = 1 overflow per second
```

**Links:** [[Timer 1/AVR Timers and Counters]]