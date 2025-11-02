# Rejection Sampling

_Source: `20. Uncertainty-5-BN-Sampling.pptx.pdf` (Pages 14-16, 18)_

**Rejection Sampling** is a simple way to use [[Prior Sampling]] to answer _conditional_ probability queries, like $P(Q|e)$ (e.g., $P(\text{Cloudy} | \text{Sprinkler}=+s)$).

## The Algorithm

To estimate $P(Q|e)$:

1. Generate a complete sample $(x_1, ..., x_n)$ using **[[Prior Sampling]]**.
    
2. **Check Consistency:** Look at the sample. Does it match your evidence $e$?
    
    - **If YES:** The sample is consistent. Keep it.
        
    - **If NO:** The sample is inconsistent. **Reject** it (throw it away).
        
3. Repeat this process N times (note: you may have to run the sampler _more_ than N times to _keep_ N samples).
    
4. To get your final answer, use the counts from the **kept samples only**.
    

**Example: Estimate** $P(C|+s)$

1. Generate 5 samples using Prior Sampling:
    
    - `+c, -s, +r, +w` $\rightarrow$ **Reject** (evidence $S$ is not $+s$)
        
    - `+c, +s, +r, +w` $\rightarrow$ **Keep**
        
    - `-c, +s, +r, -w` $\rightarrow$ **Keep**
        
    - `+c, -s, +r, +w` $\rightarrow$ **Reject**
        
    - `-c, -s, -r, +w` $\rightarrow$ **Reject**
        
2. **Analyze Kept Samples:** We kept 2 samples: `(+c, +s, ...)` and `(-c, +s, ...)`.
    
3. **Estimate:** Among our kept samples, we have 1 `+c` and 1 `-c`.
    
    - Our estimate is $P(C|+s) \approx \langle 0.5, 0.5 \rangle$.
        

## Problem with Rejection Sampling

- **It is consistent** (it will converge to the true probability in the limit).
    
- **THE BIG PROBLEM:** It is **extremely inefficient** if the evidence $e$ is rare.
    
    - Imagine we want to estimate $P(\text{Burglary} | \text{Alarm}=+a)$ and $P(\text{Alarm}=+a)$ is 0.001.
        
    - You would generate, on average, 1000 samples just to _keep one_.
        
    - This is a massive waste of computational resources, as 99.9% of your work is thrown away.
        

This inefficiency is solved by [[Likelihood Weighting]].

### ❓ Review Questions

1. What is the _only_ difference between Rejection Sampling and Prior Sampling?
    
2. When does Rejection Sampling perform _very poorly_, and why?