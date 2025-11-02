# Configuring and Using GPIO Pins

**Tags:** #microcontroller #atmega32 #IO #C-code

Here is the fundamental workflow for using GPIO pins in C for AVR microcontrollers.

### Setting a Port as Output

To send data out (e.g., to an LED), you must:

1. Configure the pin(s) as output by setting the corresponding `DDRx` bits to `1`.
    
2. Write the desired high/low state to the `PORTx` register.
    

```
// Example: Set all pins of Port D to output and turn them on
DDRD = 0xFF; 
PORTD = 0xFF;
```

### Setting a Port as Input

To read data from a sensor or a button:

1. Configure the pin(s) as input by setting the corresponding `DDRx` bits to `0`.
    
2. Read the state of the pins from the `PINx` register.
    

```
// Example: Read from Port A and display on Port B
DDRA = 0x00; // Set Port A as input
DDRB = 0xFF; // Set Port B as output

unsigned char input_data = PINA; // Read the state from Port A
PORTB = input_data; // Write that state to Port B
```

**Links**: [[ATmega32 I-O Registers]], [[AVR C Code Examples - I-O]]