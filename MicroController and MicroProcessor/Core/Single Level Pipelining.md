# Single Level Pipelining

Tags: pipelining, cpu, performance, risc

Pipelining is a technique where multiple instructions are overlapped in execution. The [[ATmega32 Architecture|ATmega32]] uses a single-level pipeline.

- While one instruction is being executed, the next instruction is simultaneously being fetched from program memory.
    
- This allows the microcontroller to complete one instruction per clock cycle on average.
    
- For example, in clock cycle T2, while the 1st instruction is executing, the 2nd instruction is being fetched.
