# ATmega32 ADC Features

**Tags:** #microcontroller #atmega32 #adc

The ADC module on the ATmega32 has several key features that make it flexible for various applications.

### Key Hardware Features

- **Resolution**: **10-bit**. This means it can represent an analog voltage using 210=1024 discrete levels (from 0 to 1023).
    
- **Input Channels**: **8 multiplexed channels** (ADC0 through ADC7) are available on **PORTA**. The ADC can only convert one channel at a time.
    
- **Reference Voltage (**VREF​**)**: The voltage reference is configurable. You can use:
    
    - An external voltage applied to the **AREF** pin.
        
    - The main supply voltage **AVCC** (typically 5V).
        
    - An internal, calibrated **2.56V** reference.
        
- **Conversion Time**: A single ADC conversion takes **13 ADC clock cycles**.
    
- **ADC Clock (Prescaler)**: The ADC has its own clock, which is derived from the main system clock by a **prescaler**. The prescaler divides the system clock by a factor (from 2 to 128) to generate a suitable ADC clock speed (ideally 50-200 kHz for max accuracy).
    

### Result Storage

The 10-bit digital result is stored in two 8-bit registers: **ADCH** and **ADCL**. You can configure how the 10 bits are arranged in these 16 available bits using the ADLAR bit.

**Links**: [[ATmega32 ADC]], [[ADC Fundamentals]], [[ATmega32 ADC Registers]]