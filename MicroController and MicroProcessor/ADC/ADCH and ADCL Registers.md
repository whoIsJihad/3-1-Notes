# ADCH and ADCL Registers

**Tags:** #microcontroller #atmega32 #adc #registers

The 10-bit result of an ADC conversion is stored across two 8-bit registers: `ADCH` (High Byte) and `ADCL` (Low Byte). How the 10 bits are arranged depends on the **ADLAR** bit in the [[ADMUX Register]].

### Right-Adjusted Result (ADLAR = 0)

This is the default setting, used when you need the full 10-bit precision.

|Register|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|---|
|**ADCH**|0|0|0|0|0|0|Bit9|Bit8|
|**ADCL**|Bit7|Bit6|Bit5|Bit4|Bit3|Bit2|Bit1|Bit0|

> [!IMPORTANT] **Read ADCL First!** When reading a 10-bit right-adjusted result, you **must** read `ADCL` before you read `ADCH`. Reading `ADCL` locks both data registers, preventing them from being updated by a new conversion until `ADCH` is also read. This ensures that both bytes belong to the same conversion result.

In C, you can simply read the special 16-bit name `ADC` and the compiler handles the correct read order: `unsigned int result = ADC;`.

### Left-Adjusted Result (ADLAR = 1)

This setting is used for convenience when you only need 8 bits of precision.

|Register|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|---|
|**ADCH**|Bit9|Bit8|Bit7|Bit6|Bit5|Bit4|Bit3|Bit2|
|**ADCL**|Bit1|Bit0|0|0|0|0|0|0|

In this mode, you can simply read `ADCH` to get the 8 most significant bits of the result, which is often sufficient and much faster.

**Links**: [[ATmega32 ADC Registers]]