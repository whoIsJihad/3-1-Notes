# Likelihood Weighting

_Source: `20. Uncertainty-5-BN-Sampling.pptx.pdf` (Pages 17-22)_

**Likelihood Weighting (LW)** is a more efficient way to answer conditional queries $P(Q|e)$. It was designed to solve the massive inefficiency problem of [[Rejection Sampling]].

The core idea: **Never reject a sample.** Instead, generate samples that are _consistent_ with the evidence, and then _weight_ them based on how likely they were.

## The Algorithm

To generate one _weighted sample_ given evidence $e$:

1. Initialize a `weight w = 1.0`.
    
2. Go through all variables $X_i$ in **topological order**.
    
3. **Case 1:** $X_i$ **is NOT an evidence variable.**
    
    - Sample $x_i$ from $P(X_i | Parents(X_i))$ just like in [[Prior Sampling]].
        
4. **Case 2:** $X_i$ **IS an evidence variable.**
    
    - **DO NOT SAMPLE!** _Fix_ the value of $X_i$ to be its evidence value $e_i$.
        
    - **Update the weight:** Multiply the current weight `w` by the probability of this evidence, given its sampled parents.
        
    - $w = w \times P(X_i = e_i | Parents(X_i))$
        
5. After iterating through all variables, you have a complete sample $(x_1, ..., x_n)$ and a final weight $w$. Return both.
    

**Example: Estimate** $P(C|+s, +w)$

- Evidence $e$ is $S=+s, W=+w$.
    
- **Sample 1:**
    
    1. `w = 1.0`
        
    2. **Sample `C`:** (Not evidence). Sample from $P(C)$. Get `+c`.
        
    3. **Sample `S`:** (IS evidence). **Fix** $S=+s$.
        
        - Update weight: $w = w \times P(S=+s | C=+c)$. Let's say this is 0.1.
            
        - `w` is now 0.1.
            
    4. **Sample `R`:** (Not evidence). Sample from $P(R | C=+c)$. Get `+r`.
        
    5. **Sample `W`:** (IS evidence). **Fix** $W=+w$.
        
        - Update weight: $w = w \times P(W=+w | S=+s, R=+r)$. Let's say this is 0.99.
            
        - `w` is now $0.1 \times 0.99 = 0.099$.
            
    
    - **Return Sample 1:** `(+c, +s, +r, +w)` with **weight = 0.099**.
        

## Usage

To estimate $P(C|+s, +w)$, you generate N weighted samples and then take a _weighted tally_.

1. Initialize two counters: `TotalWeight_C_True = 0`, `TotalWeight_C_False = 0`.
    
2. For each sample you generate:
    
    - If the sample has `C=+c`, add its weight to `TotalWeight_C_True`.
        
    - If the sample has `C=-c`, add its weight to `TotalWeight_C_False`.
        
3. **Normalize:**
    
    - $P(C=+c | +s, +w) \approx \frac{\text{TotalWeight}_C\_\text{True}}{\text{TotalWeight}_C\_\text{True} + \text{TotalWeight}_C\_\text{False}}$
        

## Limitation

- **Much better than rejection!**
    
- **Limitation (Page 22):** Evidence only influences _downstream_ variables. In our example, when we sampled `C`, we had no idea that the evidence `+s` and `+w` was coming. `C` was sampled from its _prior_ $P(C)$.
    
- If the evidence is "downstream" (an effect) and is very unlikely, this method will still generate many samples with tiny weights. This is more efficient, but not perfect. This "upstream" problem is solved by [[Gibbs Sampling]].
    

### ❓ Review Questions

1. What is the key difference in how Likelihood Weighting handles an evidence variable compared to Rejection Sampling?
    
2. What is the "upstream" problem? (i.e., why doesn't evidence influence the sampling of its ancestors?)