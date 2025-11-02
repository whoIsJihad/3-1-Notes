# Timer0 Modes of Operation

**Tags:** #microcontroller #avr #timers #timer0

[[AVR Timer0]] can operate in one of four modes, which are selected by the **Waveform Generation Mode (WGM01:00)** bits in the [[TCCR0 Register]].

|WGM01|WGM00|Mode|
|---|---|---|
|0|0|[[Timer0 Normal Mode]]|
|0|1|[[Timer0 Phase Correct PWM Mode]]|
|1|0|[[Timer0 CTC Mode]]|
|1|1|[[Timer0 Fast PWM Mode]]|

### Summary of Modes

- **Normal Mode:** The counter counts up from 0 to 255 and then overflows. The primary event is the [[Timer Overflow]].
    
- **CTC (Clear Timer on Compare Match) Mode:** The counter counts up until its value matches the value in the `OCR0` register. When they match, the counter is cleared to 0. This allows for more precise frequency generation.
    
- **Fast PWM Mode:** Used for generating Pulse Width Modulation signals. It's "fast" because it only counts upwards (single-slope operation).
    
- **Phase Correct PWM Mode:** A more precise PWM mode that counts up to MAX and then down to 0 (dual-slope operation). This produces a symmetrical PWM waveform, which is better for applications like motor control.
    

**Links:** [[AVR Timer0]], [[TCCR0 Register]]