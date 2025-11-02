# ATmega32 Basic Input-Output

**Tags:** #microcontroller #atmega32 #embedded #IO

This note covers the fundamentals of configuring and using the General Purpose Input/Output (GPIO) pins on the ATmega32 microcontroller. Understanding I/O is the first step in interfacing the microcontroller with external components like LEDs, sensors, and buttons.

### Core Concepts

1.  **[[ATmega32 Architecture Overview]]**: A brief look at the features of the ATmega32.
2.  **[[ATmega32 I-O Ports]]**: How the physical pins are grouped into ports.
3.  **[[ATmega32 I-O Registers]]**: The three main registers (`DDRx`, `PORTx`, `PINx`) that control the ports.
4.  **[[Configuring and Using GPIO Pins]]**: Practical C code examples for setting pins as input or output.
5.  **[[Generating Delays in AVR C]]**: The importance of accurate delays for timing-sensitive operations.
6.  **[[Interfacing Push Buttons]]**: A guide on handling button inputs, including debouncing and pull-up resistors.

### Practical Code Examples

* [[AVR C Code Examples - I-O]]