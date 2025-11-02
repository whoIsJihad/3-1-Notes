# ADC Fundamentals

**Tags:** #adc #analog #digital #electronics

An ADC converts a continuous analog voltage into a discrete digital value through two main steps: **Sampling** and **Quantization**.

### 1. Sampling

Sampling is the process of measuring the analog signal's voltage at regular, discrete points in time. The rate at which these samples are taken is the **sampling frequency**.

### 2. Quantization

Quantization is the process of approximating the continuous voltage of each sample to the nearest discrete level that the ADC can represent. The accuracy of this approximation depends on the ADC's **resolution**.

### Key ADC Parameters

#### Resolution

- **Definition**: The number of bits the ADC uses to represent the analog signal. A higher resolution means more discrete levels and a more accurate representation.
    
- **Example**: An 8-bit ADC has 28=256 levels. The ATmega32's 10-bit ADC has 210=1024 levels.
    

#### Reference Voltage (VREF​)

- **Definition**: The maximum voltage the ADC can measure. Any input voltage equal to or greater than VREF​ will result in the maximum digital value (e.g., 1023 for a 10-bit ADC).
    

#### Step Size

- **Definition**: The smallest change in analog voltage that the ADC can detect. It is the voltage difference between two adjacent digital levels.
    
- **Formula**: $$ \text{Step Size} = \frac{V_{REF}}{2^n} $$ where 'n' is the resolution in bits.
    

#### Quantization Error

- **Definition**: The inherent error introduced during quantization because the ADC is approximating a continuous value with a discrete one. This error is typically up to ±0.5 times the step size and can be minimized by increasing the ADC's resolution.
    

**Links**: [[ATmega32 ADC]], [[ATmega32 ADC Features]]