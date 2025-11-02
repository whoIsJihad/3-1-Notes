# USART Baud Rate Registers (UBRR)

**Tags:** #microcontroller #atmega32 #usart #baudrate #registers

The **baud rate** is the speed of the serial communication, measured in bits per second (bps). Both the sender and receiver must be configured to the same baud rate to communicate successfully.

The ATmega32 uses a 12-bit register, `UBRR` (USART Baud Rate Register), to set this speed. Because the microcontroller is 8-bit, this 12-bit value is split across two registers:

- `UBRRH`: The high byte (contains the 4 most significant bits).
    
- `UBRRL`: The low byte (contains the 8 least significant bits).
    

### Calculating the `UBRR` Value

You calculate the required `UBRR` value based on the microcontroller's system clock frequency (`F_CPU`) and the desired `BAUD` rate.

The formula for normal speed mode is:

```
UBRR = (F_CPU / (16 * BAUD)) - 1
```

If you enable double speed mode by setting the `U2X` bit in `UCSRA`, the formula is:

```
UBRR = (F_CPU / (8 * BAUD)) - 1
```

#### Example Calculation

- **Goal**: 9600 bps baud rate.
    
- **System Clock**: 16 MHz (`F_CPU` = 16,000,000 Hz).
    
- **Mode**: Normal speed.
    

```
UBRR = (16000000 / (16 * 9600)) - 1
UBRR = (16000000 / 153600) - 1
UBRR = 104.16 - 1
UBRR = 103.16
```

Since `UBRR` must be an integer, you round to the nearest whole number: **103**.

You would then load this value into the registers:

- `UBRRH = 0;`
    
- `UBRRL = 103;`
    

> [!TIP] The ATmega32 datasheet contains pre-calculated tables of `UBRR` values for common clock speeds and baud rates, which helps you avoid calculation errors.

**Links**: [[USART Communication]], [[Programming the USART]]