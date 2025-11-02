# ATmega32 Interrupt Vector Table (IVT)

**Tags:** #microcontroller #atmega32 #interrupts #reference

The Interrupt Vector Table (IVT) is a specific area in the program memory that acts as a lookup table for all interrupt sources. Each interrupt has a predefined "vector" or address. When an interrupt occurs, the CPU hardware automatically jumps to this address to find the code it needs to execute.

### Priority

Interrupts are prioritized based on their position in the table. **A lower vector number means a higher priority**. For example, `INT0_vect` (Vector No. 2) has a higher priority than `INT1_vect` (Vector No. 3). If both interrupts occur at the same time, the one with the higher priority will be serviced first.

### ATmega32 IVT (Partial List)

|Vector No.|Vector Name|Description|
|---|---|---|
|1|`RESET_vect`|Reset|
|2|`INT0_vect`|External Interrupt Request 0|
|3|`INT1_vect`|External Interrupt Request 1|
|4|`TIMER2_COMP_vect`|Timer/Counter2 Compare Match|
|5|`TIMER2_OVF_vect`|Timer/Counter2 Overflow|
|6|`TIMER1_CAPT_vect`|Timer/Counter1 Capture Event|
|7|`TIMER1_COMPA_vect`|Timer/Counter1 Compare Match A|
|9|`TIMER1_OVF_vect`|Timer/Counter1 Overflow|
|10|`TIMER0_OVF_vect`|Timer/Counter0 Overflow|
|15|`ADC_vect`|ADC Conversion Complete|
|19|`INT2_vect`|External Interrupt Request 2|
|20|`TIMER0_COMP_vect`|Timer/Counter0 Compare Match|

The `Vector Name` is the specific identifier you use when writing an ISR in C for that interrupt source.

**Links**: [[ATmega32 Interrupts]], [[Programming Interrupts in C]]