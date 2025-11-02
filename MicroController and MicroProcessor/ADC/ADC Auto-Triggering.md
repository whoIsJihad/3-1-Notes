# ADC Auto-Triggering

**Tags:** #microcontroller #atmega32 #adc #timers

**Auto-triggering** allows you to start an ADC conversion automatically when a specific hardware event occurs, such as a timer overflowing. This is extremely useful for capturing data at a precise, constant sampling rate (e.g., for audio or signal processing) without manual intervention from the CPU.

### How it Works

1. **Enable Auto-Triggering**: Set the `ADATE` (ADC Auto Trigger Enable) bit in the [[ADCSRA Register]] to `1`.
    
2. **Select the Trigger Source**: Set the `ADTS2..0` bits in the **SFIOR** (Special Function IO Register) to choose the event that will trigger the conversion. Common sources include:
    
    - **Free Running Mode**: A new conversion starts immediately after the previous one finishes.
        
    - **Timer/Counter Compare Match**: A conversion starts when a timer's count matches the value in its `OCR` register. This is ideal for precise frequency control.
        
    - **Timer/Counter Overflow**: A conversion starts when a timer counts to its maximum value and overflows.
        
3. **Start the First Conversion**: You still need to start the _first_ conversion manually by setting `ADSC = 1`. After that, the selected trigger source will start all subsequent conversions automatically.
    

### Example: Sampling at a Precise Frequency

To sample a signal at exactly 20 kHz, you need a new sample every 50 µs.

- **Method**: Use Timer0 in CTC (Clear Timer on Compare Match) mode.
    
- **Setup**:
    
    1. Configure Timer0 to generate a compare match event every 50 µs.
        
    2. Set `ADATE = 1` in `ADCSRA`.
        
    3. Set the `ADTS` bits in `SFIOR` to select "Timer/Counter0 Compare Match" as the trigger source.
        
    4. Configure and enable the ADC, preferably with an interrupt to handle the results efficiently.
        

This setup ensures that the hardware handles the precise timing, freeing the CPU from managing the sampling process.

**Links**: [[ATmega32 ADC]]