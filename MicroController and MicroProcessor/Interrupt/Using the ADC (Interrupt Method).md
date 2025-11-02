# Using the ADC (Interrupt Method)

**Tags:** #microcontroller #atmega32 #adc #interrupts #C-code

The interrupt method is more efficient than [[Using the ADC (Polling Method)]] because it allows the CPU to perform other tasks while the ADC conversion is happening. When the conversion is complete, the ADC hardware automatically triggers an interrupt, causing a special function (the ISR) to run and handle the result.

### Steps for Interrupt-Driven ADC

1. **Configure the ADC**:
    
    - Set up [[ADMUX Register]] (reference, channel, etc.) as usual.
        
    - In [[ADCSRA Register]], enable the ADC (`ADEN=1`), set the prescaler, and most importantly, **enable the ADC interrupt** by setting `ADIE` to `1`.
        
2. **Enable Global Interrupts**:
    
    - Call the `sei();` function to enable interrupts globally.
        
3. **Create an Interrupt Service Routine (ISR)**:
    
    - Write a function with the `ISR(ADC_vect)` signature. This is the code that will automatically execute when a conversion finishes.
        
    - Inside the ISR, read the result from the data registers and store it in a `volatile` global variable.
        
4. **Start Conversion in Main Loop**:
    
    - In your `main()` function's loop, simply start a conversion by setting `ADSC=1`. The CPU is now free. The ISR will handle the result when it's ready.
        

### C Code Example

```
#include <avr/io.h>
#include <avr/interrupt.h>

// 'volatile' tells the compiler that this variable can be changed by an interrupt.
volatile unsigned char adc_result;

// Interrupt Service Routine for ADC Conversion Complete
ISR(ADC_vect) {
    // Step 3: Read the result inside the ISR
    adc_result = ADCH; 
}

int main(void) {
    DDRB = 0xFF; // Port B as output
    
    // Step 1: Configure ADC
    ADMUX = (1 << REFS0) | (1 << ADLAR); // AVCC ref, Left Adjust, ADC0
    // Enable ADC, Enable Interrupt, Prescaler=128
    ADCSRA = (1 << ADEN) | (1 << ADIE) | (1 << ADPS2) | (1 << ADPS1) | (1 << ADPS0); 

    // Step 2: Enable global interrupts
    sei(); 

    // Start the first conversion
    ADCSRA |= (1 << ADSC);

    while (1) {
        // The main loop can do other things.
        // Here, it just displays the latest result from the ISR.
        PORTB = adc_result;
    }
}
```

**Links**: [[ATmega32 ADC]]