# Timer0 CTC Mode

**Tags:** #microcontroller #avr #timers #timer0

CTC stands for **Clear Timer on Compare Match**. This mode provides more flexibility in generating specific time delays or frequencies compared to [[Timer0 Normal Mode]].

### How it Works

1. The **WGM01** bit in [[TCCR0 Register]] is set to 1, and **WGM00** is set to 0.
    
2. A target value is loaded into the **Output Compare Register (OCR0)**.
    
3. The [[TCNT0]] register starts counting from 0 upwards.
    
4. When the value of `TCNT0` becomes equal to the value in `OCR0`, a **compare match** occurs.
    
5. On the very next timer clock cycle, `TCNT0` is automatically cleared to 0.
    
6. When the compare match occurs, the **Output Compare Flag (OCF0)** in the [[TIFR Register]] is set.
    
7. If the **Output Compare Interrupt Enable (OCIE0)** bit in [[TIMSK Register]] is set, an interrupt is triggered.
    

The maximum count value is determined by `OCR0`, not fixed at 255. This allows for precise control over the timer's period.

### Frequency Calculation

The frequency of the generated waveform (if using OC0 pin to toggle) is given by:

```
F_oc0 = F_clk_I/O / (2 * N * (1 + OCR0))
```

Where `N` is the prescaler factor.

**Links:** [[Timer0 Modes of Operation]], [[Timer Interrupts]]