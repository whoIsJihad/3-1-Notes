# TIMSK Register (Timer/Counter Interrupt Mask Register)

**Tags:** #microcontroller #avr #timers #registers #interrupts

The TIMSK register is used to **enable or disable** the various interrupts associated with the timers. Setting a bit to 1 enables the corresponding interrupt, while 0 disables it.

### Bit Configuration

|Bit|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|---|
|**Name**|OCIE2|TOIE2|TICIE1|OCIE1A|OCIE1B|TOIE1|OCIE0|TOIE0|
|**Read/Write**|R/W|R/W|R/W|R/W|R/W|R/W|R/W|R/W|
|**Initial Value**|0|0|0|0|0|0|0|0|

### Bit Descriptions

|Bit|Name|Description|Related Timer|
|---|---|---|---|
|7|**OCIE2**|Timer/Counter2 Output Compare Match Interrupt Enable|[[AVR Timer2]]|
|6|**TOIE2**|Timer/Counter2 Overflow Interrupt Enable|[[AVR Timer2]]|
|5|**TICIE1**|Timer/Counter1 Input Capture Interrupt Enable|[[AVR Timer1]], [[Input Capture Mode]]|
|4|**OCIE1A**|Timer/Counter1 Output Compare A Match Interrupt Enable|[[AVR Timer1]]|
|3|**OCIE1B**|Timer/Counter1 Output Compare B Match Interrupt Enable|[[AVR Timer1]]|
|2|**TOIE1**|Timer/Counter1 Overflow Interrupt Enable|[[AVR Timer1]]|
|1|**OCIE0**|Timer/Counter0 Output Compare Match Interrupt Enable|[[AVR Timer0]]|
|0|**TOIE0**|Timer/Counter0 Overflow Interrupt Enable|[[AVR Timer0]]|

To use any of these interrupts, the global interrupt flag must also be enabled by calling the `sei()` instruction.

**Links:** [[Timer Interrupts]], [[TIFR Register]]