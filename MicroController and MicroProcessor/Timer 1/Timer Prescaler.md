# Timer Prescaler

**Tags:** #microcontroller #avr #timers #clock

A prescaler is a circuit that divides the main system clock frequency (Fclk_I/O​) to produce a slower clock signal for the timer/counter. This allows the timer to count at a lower rate, extending the maximum time delay it can generate before an overflow occurs.

The timer clock source is selected using the **Clock Select (CS)** bits in the Timer/Counter Control Register (e.g., [[TCCR0 Register]], [[TCCR1B Register]]).

By setting these bits, you can choose to either stop the timer, use the system clock directly, or use the system clock divided by a specific factor (8, 64, 256, or 1024).

### Example: Timer0 Clock Select (CS02:0) in TCCR0

|CS02|CS01|CS00|Description|
|---|---|---|---|
|0|0|0|No clock source (Timer/Counter stopped).|
|0|0|1|clk_I/O / 1 (No prescaling)|
|0|1|0|clk_I/O / 8|
|0|1|1|clk_I/O / 64|
|1|0|0|clk_I/O / 256|
|1|0|1|clk_I/O / 1024|
|1|1|0|External clock source on T0 pin. Falling edge.|
|1|1|1|External clock source on T0 pin. Rising edge.|

Choosing a larger prescaler value increases the time period of a single timer tick, thus increasing the total time until an [[Timer Overflow]].

**Links:** [[Timer 1/AVR Timers and Counters]]