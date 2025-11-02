# Basic Sampling from a Distribution

_Source: `20. Uncertainty-5-BN-Sampling.pptx.pdf` (Page 7)_

Before we can sample from a whole network, we need to know how to sample from a single probability table.

Let's say we have a simple distribution for a variable `C` (Color):

|C|P(C)|
|---|---|
|red|0.6|
|green|0.1|
|blue|0.3|

How do we write a program that "randomly" picks a color according to these probabilities?

## The Algorithm

We can use a uniform random number generator (like `random()` in Python), which gives a number `u` between 0.0 and 1.0.

1. **Get sample `u`** from a uniform distribution over [0, 1).
    
2. **Convert `u` to an outcome** by mapping it to a sub-interval. We "stack" the probabilities to create intervals from 0 to 1:
    
    - `red`: [0.0, 0.6) --- (size 0.6)
        
    - `green`: [0.6, 0.7) --- (size 0.1)
        
    - `blue`: [0.7, 1.0) --- (size 0.3)
        
3. **Check which interval `u` falls into:**
    
    - If $0.0 \le u < 0.6 \rightarrow$ return `red`
        
    - If $0.6 \le u < 0.7 \rightarrow$ return `green`
        
    - If $0.7 \le u < 1.0 \rightarrow$ return `blue`
        

**Example:** If `random()` returns `u = 0.83`, that falls in the `[0.7, 1.0)` interval, so our sample is `blue`.

This technique is the building block for all the [[Prior Sampling]] methods.

### ❓ Review Questions

1. If $P(A) = 0.2$ and $P(\neg A) = 0.8$, what intervals would you use to sample for A?
    
2. If `random()` returns `u = 0.19`, what would the outcome be for the `C` (Color) example?