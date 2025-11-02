# ATmega32 ADC Registers

**Tags:** #microcontroller #atmega32 #adc #registers

To use the ADC on the ATmega32, you need to configure and interact with three primary register groups.

### 1. [[ADMUX Register]] (ADC Multiplexer Selection Register)

- **Purpose**: This register is used to select the **reference voltage**, the **analog input channel**, and the **data alignment** of the result in the data registers.
    

### 2. [[ADCSRA Register]] (ADC Control and Status Register A)

- **Purpose**: This is the main control register. It's used to **enable the ADC**, **start a conversion**, set the **ADC clock prescaler**, and manage **interrupts**.
    

### 3. [[ADCH and ADCL Registers]] (ADC Data Registers)

- **Purpose**: These two 8-bit registers work together as a single 16-bit space to store the **10-bit digital result** of the conversion.
    

### 4. SFIOR Register (Special Function IO Register)

- This register is used for more advanced features, primarily to select the source for [[ADC Auto-Triggering]].
    

By setting the bits in these registers, you gain full control over the ADC's operation.

**Links**: [[ATmega32 ADC]], [[ATmega32 ADC Features]]