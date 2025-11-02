# Interfacing LM35 Temperature Sensor

**Tags:** #microcontroller #sensor #temperature #lm35 #adc

The **LM35** is a popular analog temperature sensor. Its output voltage is directly proportional to the temperature in degrees Celsius, making it easy to use.

### LM35 Key Features

- **Linear Output**: The output voltage changes linearly with temperature.
    
- **Scale Factor**: **10 mV per degree Celsius** (10mV/∘C).
    
    - At 25∘C, the output is 25×10mV=250mV (or 0.25V).
        

### Circuit Connection

The connection is very simple:

1. Connect the LM35's **VCC pin** to 5V.
    
2. Connect the LM35's **GND pin** to Ground.
    
3. Connect the LM35's **Vout pin** to an ADC input channel (e.g., ADC0).
    

### Reading the Temperature with the ADC

The LM35's output voltage range (e.g., 0V to 1V for 0-100°C) is much smaller than the ADC's default 5V range. This results in poor resolution.

**Solution**: Use a lower reference voltage (VREF​) that is closer to the sensor's maximum output voltage. The ATmega32's internal **2.56V reference** is an excellent choice.

#### Calculation with 2.56V Reference

1. **Configure ADC**: Set [[ADMUX Register]] to use the internal 2.56V reference (`REFS1=1`, `REFS0=1`).
    
2. **Calculate Step Size**:
    
    ```
    Step Size = 2.56V / 1024 steps = 2.5mV / step
    ```
    
3. **Read ADC Value**: Perform a conversion and get the 10-bit digital result (`ADC_Value`).
    
4. **Convert to Voltage**:
    
    ```
    Input Voltage (in mV) = ADC_Value * 2.5mV
    ```
    
5. **Convert to Temperature**: Since Temperature in ∘C=Input Voltage (in mV)/10, the final formula simplifies to:
    
    ```
    Temp (°C) = (ADC_Value * 2.5) / 10 = ADC_Value / 4
    ```
    

This gives a very simple final formula: you can get the temperature in Celsius by reading the 10-bit ADC result and dividing it by 4 (or right-shifting by 2 bits: `result >> 2`).

**Links**: [[ATmega32 ADC]]