# ADMUX Register (ADC Multiplexer Selection)

**Tags:** #microcontroller #atmega32 #adc #registers

The `ADMUX` register is used to set up the analog input side of the ADC, including the voltage reference, input channel, and data alignment.

### Register Bit Layout

|Bit|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|---|
|**Name**|REFS1|REFS0|ADLAR|MUX4|MUX3|MUX2|MUX1|MUX0|

### Bit Functions

#### REFS1, REFS0: Reference Selection Bits

These two bits select the voltage reference (VREF​) for the ADC.

- **`00`**: External voltage on AREF pin.
    
- **`01`**: **AVCC** (typically 5V). **This is the most common setting**.
    
- **`11`**: Internal **2.56V** reference.
    

#### ADLAR: ADC Left Adjust Result

This bit controls how the 10-bit ADC result is stored in the [[ADCH and ADCL Registers]].

- **`0` (default)**: **Right-adjusted**. Useful when you need the full 10-bit precision.
    
- **`1`**: **Left-adjusted**. Convenient for 8-bit precision, as you can just read `ADCH`.
    

#### MUX4..0: Analog Channel Selection Bits

These five bits select which of the 8 analog input pins (ADC0-ADC7) is connected to the ADC.

- **`00000`**: Selects ADC0.
    
- **`00001`**: Selects ADC1, and so on.
    

**Links**: [[ATmega32 ADC Registers]]