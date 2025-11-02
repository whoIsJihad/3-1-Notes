# Interfacing Push Buttons

**Tags:** #microcontroller #button #input #debouncing #pull-up

Connecting a button requires handling two physical issues: **floating inputs** and **switch bouncing**.

### 1. The Floating Input Problem

When a switch is open, the input pin is not connected to any defined voltage. This **floating state** can cause random readings.

**Solution**: Use **Pull-up Resistors** to give the pin a default HIGH state. The ATmega32 has internal pull-up resistors you can enable in software.

1. Set the pin as input (`DDRx` bit = `0`).
    
2. Write a `1` to the corresponding bit in the `PORTx` register.
    

### 2. The Switch Bouncing Problem

When pressed, a button's mechanical contacts bounce rapidly, creating multiple signals from a single press.

**Solution**: **Debouncing**. The easiest method is a software delay. After detecting a press, wait a few milliseconds for the bouncing to stop before acting on the input.

**Links**: [[AVR C Code Examples - I-O]], [[ATmega32 Basic I-O]]