# ADCSRA Register (ADC Control and Status)

**Tags:** #microcontroller #atmega32 #adc #registers

The `ADCSRA` register is the primary control and status register for the ADC module.

### Register Bit Layout

| Bit      | 7    | 6    | 5     | 4    | 3    | 2     | 1     | 0     |
| -------- | ---- | ---- | ----- | ---- | ---- | ----- | ----- | ----- |
| **Name** | ADEN | ADSC | ADATE | ADIF | ADIE | ADPS2 | ADPS1 | ADPS0 |

### Bit Functions

#### ADEN: ADC Enable

- **`1`**: Enables the ADC. Must be set to use the ADC.
    
- **`0`**: Disables the ADC to save power.
    

#### ADSC: ADC Start Conversion

- Writing a **`1`** to this bit starts a single conversion.
    
- The hardware clears this bit to `0` when the conversion is complete.
    

#### ADATE: ADC Auto Trigger Enable

- **`1`**: Enables [[ADC Auto-Triggering]].
    
- **`0`**: Disables auto-triggering (manual start required).
    

#### ADIF: ADC Interrupt Flag

- This bit is **set to `1`** by hardware when a conversion completes.
    
- Clear it by writing a `1` to it.
    

#### ADIE: ADC Interrupt Enable

- **`1`**: Enables the ADC conversion complete interrupt.
    
- **`0`**: Disables the interrupt.
    

#### ADPS2..0: ADC Prescaler Select Bits

These three bits set the division factor between the system clock and the ADC clock. The ADC clock should ideally be between 50-200 kHz for maximum accuracy.

- **`010`**: Division factor of 4.
    
- **`111`**: Division factor of 128.
    

**Links**: [[ATmega32 ADC Registers]]