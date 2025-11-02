# ICR1 Register (Input Capture Register 1)

**Tags:** #microcontroller #avr #timers #registers #timer1

The ICR1 register is a 16-bit register associated with [[AVR Timer1]] that has a dual purpose. It is composed of **ICR1H** and **ICR1L**.

### 1. Input Capture Function

This is its primary role. When an event occurs on the Input Capture Pin (ICP1, which is PD6), the current value of the [[TCNT1]] counter is automatically copied into the ICR1 register. This allows for precise measurement of the time between external events. See [[Input Capture Mode]] for more details.

### 2. TOP Value Definition

In some of the advanced [[Timer1 Modes of Operation]] (specifically certain PWM modes), the ICR1 register can be used to define the **TOP** value of the counter. In these modes, the timer will count up to the value stored in ICR1 and then reverse direction or reset. This provides a way to generate PWM signals with a specific, adjustable frequency, as the TOP value (which defines the period) is independent of the `OCR1A`/`B` registers (which define the duty cycle).

Using ICR1 to set the TOP value is more flexible than using OCR1A for the same purpose, as it leaves both OCR1A and OCR1B free to be used purely for generating PWM duty cycles.

**Links:** [[AVR Timer1]], [[Input Capture Mode]]