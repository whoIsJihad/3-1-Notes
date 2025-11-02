# TCCR1A Register (Timer/Counter1 Control Register A)

**Tags:** #microcontroller #avr #timers #registers #timer1

TCCR1A is one of two control registers for [[AVR Timer1]]. It is primarily concerned with configuring the **Compare Output Mode** and the lower two bits of the **Waveform Generation Mode**.

### Bit Configuration

|Bit|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|---|
|**Name**|COM1A1|COM1A0|COM1B1|COM1B0|FOC1A|FOC1B|WGM11|WGM10|
|**Read/Write**|R/W|R/W|R/W|R/W|W|W|R/W|R/W|
|**Initial**|0|0|0|0|0|0|0|0|

### Bit Descriptions

|Bits|Name|Description|
|---|---|---|
|7:6|**COM1A1:0**|**Compare Output Mode for Channel A:** Controls the behavior of the OC1A pin. The effects depend on the selected WGM mode.|
|5:4|**COM1B1:0**|**Compare Output Mode for Channel B:** Controls the behavior of the OC1B pin. The effects depend on the selected WGM mode.|
|3|**FOC1A**|**Force Output Compare for Channel A:** Forces an immediate compare match on channel A (in non-PWM modes).|
|2|**FOC1B**|**Force Output Compare for Channel B:** Forces an immediate compare match on channel B (in non-PWM modes).|
|1:0|**WGM11:10**|**Waveform Generation Mode:** These are the lower two bits of the 4-bit WGM setting. They combine with bits WGM13:12 in [[TCCR1B Register]] to select the final mode.|

**Links:** [[AVR Timer1]], [[TCCR1B Register]], [[Timer1 Modes of Operation]]