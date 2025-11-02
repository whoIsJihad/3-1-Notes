

**Tags:** #avr #timers #hardware #prescaler #interrupts

At its core, a hardware timer is a simple concept built from a few key components. Let's use Timer1 as our example.

### 1. The Counter Register (`TCNT1`)

- **What it is:** The heart of the timer. `TCNT1` (Timer/Counter 1) is a 16-bit register that automatically increments with every "tick" it receives.
    
- **How it works:** You can read `TCNT1` at any time to see how many ticks have passed. You can also write a value to it to start counting from a specific number. Its value constantly increases until it reaches its maximum value.
    

### 2. Overflow and the `TOV1` Flag

- **What is Overflow?** Since `TCNT1` is a 16-bit register, it can hold a maximum value of 65535 (`0xFFFF`). When it is at `0xFFFF` and receives one more tick, it cannot become 65536. Instead, it "overflows" and wraps around back to `0x0000`.
    
- **The `TOV1` Flag:** This wrap-around event is the most important event in basic timer operation. When the overflow happens, the hardware automatically sets a special flag bit called `TOV1` (Timer Overflow 1) in the `TIFR` (Timer Interrupt Flag Register).
    
- **How we use it:** We can either manually check this flag in a loop (polling) or, more efficiently, configure the timer to trigger an **interrupt** whenever the `TOV1` flag is set.
    

### 3. The Clock Source and the Prescaler

The speed at which `TCNT1` increments is determined by its clock source, which is typically derived from the microcontroller's main system clock (e.g., 1 MHz by default on an ATmega32).

- **The Problem:** A 1 MHz clock means `TCNT1` would increment every 1 microsecond. At this speed, it would overflow in just `65536 * 1µs = 65.536 ms`. This is too fast for many applications. We need a way to slow down the counting.
    
- **The Solution: The Prescaler.** The prescaler is a hardware circuit that acts as a clock divider. It takes the main system clock as input and outputs a slower clock for the timer.
    
- **How it works:** You can configure the prescaler to divide the system clock by a set factor. For Timer1, the options are 1, 8, 64, 256, or 1024.
    

**Simulation: Calculating the Tick Rate**

Let's see how the prescaler affects the timer's speed, assuming a 1 MHz system clock (which has a period of 1 µs).

|Prescaler Setting|Clock Division|`TCNT1` Increment Frequency|Time per Tick|Time to Overflow (65536 ticks)|
|---|---|---|---|---|
|**1 (No Prescaling)**|1 MHz / 1|1 MHz|1 µs|65.5 ms|
|**8**|1 MHz / 8|125 kHz|8 µs|524.3 ms|
|**64**|1 MHz / 64|15.625 kHz|64 µs|4.19 s|
|**256**|1 MHz / 256|3.906 kHz|256 µs|16.7 s|
|**1024**|1 MHz / 1024|~976 Hz|1024 µs|67.1 s|

By selecting the appropriate prescaler, you can tune the timer's resolution and range to fit your specific application, from measuring very short events to creating delays of nearly a minute.

**Links:** [[AVR Timers and Counters]]