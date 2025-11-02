# ATmega32 Analog-to-Digital Converter (ADC)

**Tags:** #microcontroller #atmega32 #adc #analog #embedded

Microcontrollers are digital devices that only understand high and low voltage levels (binary). However, the real world is full of analog signals with continuous values, like temperature, pressure, and sound from sensors.

The **Analog-to-Digital Converter (ADC)** is the crucial hardware module that bridges this gap. It measures an analog voltage and converts it into a digital number that the microcontroller can process. The ATmega32 has a powerful, built-in ADC.

### Core Concepts

1. **[[ADC Fundamentals]]**: How an ADC works through sampling and quantization. Explains key terms like resolution, reference voltage, and step size.
    
2. **[[ATmega32 ADC Features]]**: A summary of the specific capabilities of the ADC inside the ATmega32.
    
3. **[[ATmega32 ADC Registers]]**: An overview of the main registers used to control the ADC.
    
4. **[[Using the ADC (Polling Method)]]**: The basic, step-by-step method for performing a conversion and reading the result.
    
5. **[[Using the ADC (Interrupt Method)]]**: A more efficient method that allows the CPU to perform other tasks while a conversion is in progress.
    
6. **[[ADC Auto-Triggering]]**: An advanced technique for starting ADC conversions automatically based on events, like a timer, for precise sampling.
    

### Practical Application

- **[[Interfacing LM35 Temperature Sensor]]**: A common example showing how to read a real-world sensor.