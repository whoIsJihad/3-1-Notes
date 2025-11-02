# External Interrupts (INT0, INT1, INT2)

**Tags:** #microcontroller #atmega32 #interrupts #hardware

External interrupts are triggered by a change in the voltage level on specific input pins. They are commonly used to detect events from external hardware like push buttons, sensor outputs, or signals from other devices.

The ATmega32 has three external interrupt pins:

- **INT0**: Mapped to pin **PD2**
    
- **INT1**: Mapped to pin **PD3**
    
- **INT2**: Mapped to pin **PB2**
    

### Configuring an External Interrupt

To use an external interrupt, you need to configure two main aspects: the trigger condition and the enable state.

#### 1. Specifying the Trigger Event

You must define what kind of signal change will trigger the interrupt. This is configured in the [[Interrupt Control Registers]], specifically:

- **`MCUCR` (MCU Control Register)** for INT0 and INT1.
    
- **`MCUCSR` (MCU Control and Status Register)** for INT2.
    

The available trigger options for INT0 and INT1 are:

- **Low Level**: The interrupt triggers continuously as long as the pin is held low.
    
- **Any Logical Change**: Triggers on both rising and falling edges.
    
- **Falling Edge**: Triggers only when the signal goes from high to low. **(Most common for buttons)**
    
- **Rising Edge**: Triggers only when the signal goes from low to high.
    

INT2 only supports rising or falling edge triggers.

#### 2. Enabling the Interrupt

After setting the trigger condition, you must enable the specific interrupt by setting the corresponding bit in the **`GICR` (General Interrupt Control Register)**.

- Set the `INT0` bit to enable External Interrupt 0.
    
- Set the `INT1` bit to enable External Interrupt 1.
    
- Set the `INT2` bit to enable External Interrupt 2.
    

Finally, remember to enable global interrupts with `sei()` to allow the interrupt to be processed.

**Links**: [[Programming Interrupts in C]], [[Interrupt Control Registers]]