# TCCR2 Register (Timer/Counter2 Control Register)

**Tags:** #microcontroller #avr #timers #registers #timer2

TCCR2 is the control register for [[AVR Timer2]]. Its structure and function are nearly identical to the [[TCCR0 Register]].

### Bit Configuration

|Bit|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|---|
|**Name**|FOC2|WGM20|COM21|COM20|WGM21|CS22|CS21|CS20|
|**Read/Write**|W|R/W|R/W|R/W|R/W|R/W|R/W|R/W|
|**Initial Value**|0|0|0|0|0|0|0|0|

### Bit Descriptions

|Bits|Name|Description|
|---|---|---|
|7|**FOC2**|**Force Output Compare:** In non-PWM modes, forces an immediate compare match.|
|6, 3|**WGM21:20**|**Waveform Generation Mode:** Selects between Normal, CTC, Fast PWM, and Phase Correct PWM modes.|
|5:4|**COM21:20**|**Compare Match Output Mode:** Controls the behavior of the OC2 pin (PD7).|
|2:0|**CS22:20**|**Clock Select:** Selects the clock source. For Timer2, this includes additional prescaler options for the asynchronous 32.768 kHz clock.|

To use Timer2 in its unique asynchronous mode, the `AS2` bit in the [[ASSR Register]] must be set.

**Links:** [[AVR Timer2]], [[ASSR Register]]