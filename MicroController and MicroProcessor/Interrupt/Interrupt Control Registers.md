

**Tags:** #microcontroller #atmega32 #interrupts #registers #reference

Several registers are used to configure and control the interrupt system on the ATmega32.

### GICR – General Interrupt Control Register

This register is used to enable the external interrupts INT0, INT1, and INT2.

|Bit|7|6|5|...|
|---|---|---|---|---|
|**Name**|INT1|INT0|INT2|...|
|**Function**|Set to `1` to enable External Interrupt 1.|Set to `1` to enable External Interrupt 0.|Set to `1` to enable External Interrupt 2.|...|

### MCUCR – MCU Control Register

This register controls the trigger sensitivity for external interrupts INT0 and INT1.

|Bits|Name|Description|
|---|---|---|
|3, 2|`ISC11`, `ISC10`|**Interrupt Sense Control for INT1** `00`: Low-level trigger `01`: Any logical change trigger `10`: Falling-edge trigger `11`: Rising-edge trigger|
|1, 0|`ISC01`, `ISC00`|**Interrupt Sense Control for INT0** `00`: Low-level trigger `01`: Any logical change trigger `10`: Falling-edge trigger `11`: Rising-edge trigger|

### MCUCSR – MCU Control and Status Register

This register controls the trigger sensitivity for external interrupt INT2.

|Bit|6|
|---|---|
|**Name**|`ISC2`|
|**Function**|**Interrupt Sense Control for INT2** `0`: Falling-edge trigger `1`: Rising-edge trigger|

### SREG – Status Register

This is the main CPU status register. The `I` bit is the master switch for all maskable interrupts.

|Bit|7|
|---|---|
|**Name**|`I`|
|**Function**|**Global Interrupt Enable** `1`: All interrupts are enabled. `0`: All interrupts are disabled. The `sei()` macro sets this bit, and the `cli()` macro clears it.|

**Links**: [[ATmega32 Interrupts]], [[External Interrupts]]