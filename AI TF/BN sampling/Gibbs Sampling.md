# Gibbs Sampling

_Source: `20. Uncertainty-5-BN-Sampling.pptx.pdf` (Pages 23-27)_

**Gibbs Sampling** is a very different and powerful sampling technique. It is a type of **Markov Chain Monte Carlo (MCMC)** method.

It's designed to solve the "upstream" problem of [[Likelihood Weighting]]. In Gibbs, _all_ variables (upstream and downstream) are influenced by the evidence.

## The Algorithm

Instead of generating many samples "from scratch," Gibbs starts with _one_ complete sample and _iteratively improves it_.

To estimate $P(Q|e)$:

1. **Initialize:**
    
    - Fix all evidence variables $E$ to their known values $e$.
        
    - Initialize all _other_ (non-evidence) variables $X_i$ to _random_ values.
        
    - This gives you one complete, initial "state" or sample: $(x_1, ..., x_n)$.
        
2. **Iterate (Repeat N times):**
    
    - Pick one _non-evidence_ variable $X_i$ to resample (e.g., $S$).
        
    - "Erase" its current value.
        
    - **Resample** a new value for $X_i$ from its conditional distribution _given all other variables in the network_.
        
    - $P(X_i | x_1, ..., x_{i-1}, x_{i+1}, ..., x_n, e)$
        
    - This distribution is $P(X_i | \text{all other variables})$, which simplifies to $P(X_i | \text{Markov Blanket of } X_i)$. (See [[Markov Blanket]]).
        
    - Update the state with this new value for $X_i$.
        
    - Repeat this for all other non-evidence variables. One full pass is one "iteration."
        
3. **Collect Samples:**
    
    - After a "burn-in" period (e.g., the first 100 iterations) to let the state stabilize, you start collecting samples.
        
    - You can save the _entire state_ after each iteration (or every 10 iterations) as one sample.
        

**Example: Estimate** $P(S|+r)$

1. **Initialize:** Fix `R=+r`. Set `C`, `S`, `W` randomly.
    
    - State 0: `C=+c`, `S=+s`, `R=+r`, `W=-w`
        
2. **Iteration 1:**
    
    - Pick `C`. Resample `C` from $P(C | S=+s, R=+r, W=-w)$. Let's say we get `+c`. State is unchanged.
        
    - Pick `S`. Resample `S` from $P(S | C=+c, R=+r, W=-w)$. Let's say we get `-s`.
        
        - State 1: `C=+c`, `S=-s`, `R=+r`, `W=-w`
            
    - Pick `W`. Resample `W` from $P(W | C=+c, S=-s, R=+r)$. Let's say we get `+w`.
        
        - State 2: `C=+c`, `S=-s`, `R=+r`, `W=+w`
            
3. **Iteration 2:**
    
    - Pick `C`. Resample `C` from $P(C | S=-s, R=+r, W=+w)$. ...and so on.
        

After a burn-in (e.g., 100 iterations), you start recording the value of `S` at each step. If you record 1000 states, and 300 of them have `S=+s` and 700 have `S=-s`, you estimate $P(S=+s|+r) \approx 0.3$.

## Properties

- This procedure is **consistent**. In the limit, the samples you collect are drawn from the true posterior distribution $P(Q|e)$.
    
- It correctly handles the "upstream" problem because when you resample `C`, you are conditioning on its children `S` and `R` (which might be evidence, or influenced by evidence).
    

### ❓ Review Questions

1. What is the main difference between Gibbs and the other sampling methods (Prior, Rejection, LW)? (Hint: starting point, number of samples).
    
2. What is a "burn-in" period and why is it needed?
    
3. What does it mean to "resample" a variable?