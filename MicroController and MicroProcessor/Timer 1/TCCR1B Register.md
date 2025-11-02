# TCCR1B Register (Timer/Counter1 Control Register B)

**Tags:** #microcontroller #avr #timers #registers #timer1

TCCR1B is the second of two control registers for [[AVR Timer1]]. It is used for configuring the **Clock Source (Prescaler)**, the **Input Capture Edge Selection**, and the upper two bits of the **Waveform Generation Mode**.

### Bit Configuration

|Bit|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|---|
|**Name**|ICNC1|ICES1|-|WGM13|WGM12|CS12|CS11|CS10|
|**Read/Write**|R/W|R/W|R|R/W|R/W|R/W|R/W|R/W|
|**Initial**|0|0|0|0|0|0|0|0|

### Bit Descriptions

|Bits|Name|Description|
|---|---|---|
|7|**ICNC1**|**Input Capture Noise Canceler:** If set, this enables a noise canceling circuit for the [[Input Capture Mode]], which introduces a 4-clock-cycle delay.|
|6|**ICES1**|**Input Capture Edge Select:** Selects the trigger edge for the input capture event. 1 = Rising edge, 0 = Falling edge.|
|4:3|**WGM13:12**|**Waveform Generation Mode:** These are the upper two bits of the 4-bit WGM setting. They combine with bits WGM11:10 in [[TCCR1A Register]] to select the final mode.|
|2:0|**CS12:10**|**Clock Select:** These three bits select the clock source for Timer1, which determines its counting speed. See [[Timer Prescaler]].|

**Links:** [[AVR Timer1]], [[TCCR1A Register]], [[Input Capture Mode]]