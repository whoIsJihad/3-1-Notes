# Generating Delays in AVR C

**Tags:** #microcontroller #avr #delay #timing

Using simple `for` loops for delays is unreliable. The correct way is to use the built-in delay library.

### Steps for Accurate Delays:

1. **Define CPU Frequency**: You must tell the compiler your clock speed.
    
    ```
    #define F_CPU 1000000UL // 1MHz Clock Speed
    ```
    
2. **Include Delay Header**:
    
    ```
    #include <util/delay.h>
    ```
    
3. **Use Delay Functions**: Use functions like `_delay_ms()` and `_delay_us()`.
    

> [!WARNING] If `F_CPU` is set incorrectly, your timing will be wrong. A `_delay_ms(1000)` call could take 2 seconds if the clock is half the speed you defined.

**Links**: [[AVR C Code Examples - I-O]]