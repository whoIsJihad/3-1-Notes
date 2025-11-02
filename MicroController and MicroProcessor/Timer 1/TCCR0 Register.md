# TCCR0 Register (Timer/Counter0 Control Register)

**Tags:** #microcontroller #avr #timers #registers #timer0

TCCR0 is the main 8-bit control register for [[AVR Timer0]]. It is used to configure the timer's mode of operation and select the clock source via the [[Timer Prescaler]].

### Bit Configuration

|Bit|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|---|
|**Name**|FOC0|WGM00|COM01|COM00|WGM01|CS02|CS01|CS00|
|**Read/Write**|W|R/W|R/W|R/W|R/W|R/W|R/W|R/W|
|**Initial Value**|0|0|0|0|0|0|0|0|

### Bit Descriptions

|Bits|Name|Description|
|---|---|---|
|7|**FOC0**|**Force Output Compare:** In non-PWM modes, writing a 1 to this bit forces an immediate compare match on the OC0 pin.|
|6, 3|**WGM01:00**|**Waveform Generation Mode:** These two bits combine to select the timer's mode of operation. See [[Timer0 Modes of Operation]].|
|5:4|**COM01:00**|**Compare Match Output Mode:** Controls the behavior of the OC0 pin (PB3) when a compare match occurs. Used for PWM generation or toggling an output pin.|
|2:0|**CS02:00**|**Clock Select:** These three bits select the clock source for the timer, which determines its counting speed. See [[Timer Prescaler]].|

**Links:** [[AVR Timer0]], [[Timer0 Modes of Operation]]