# Prior Sampling

_Source: `20. Uncertainty-5-BN-Sampling.pptx.pdf` (Pages 9-13)_

**Prior Sampling** is the most basic way to generate a complete sample from a Bayesian Network. It generates samples from the _full joint distribution_ ($P(X_1, ..., X_n)$).

The name "Prior" comes from the fact that we are sampling _without_ any evidence.

## The Algorithm

To generate one full sample (e.g., an assignment for `Cloudy, Sprinkler, Rain, WetGrass`):

1. Start with the nodes at the top of the network (those with no parents).
    
2. Go through all variables $X_i$ in **topological order** (parents before children).
    
3. For each variable $X_i$, sample a value $x_i$ from its conditional probability table, $P(X_i | Parents(X_i))$.
    
    - (You use the [[Basic Sampling from a Distribution|basic sampling method]] for this).
        
    - The values for the `Parents(X_i)` are known because you already sampled them in previous steps.
        
4. The final set of values $(x_1, x_2, ..., x_n)$ is one complete sample.
    

**Example (C,S,R,W Network):**

1. **Sample `C` (Cloudy):** Sample from $P(C)$. Let's say we get `+c` (e.g., $P(C)=<0.5, 0.5>$ and our `u` was 0.4).
    
2. **Sample `S` (Sprinkler):** Sample from $P(S|C=+c)$. Let's say we get `-s` (e.g., $P(S|+c)=<0.1, 0.9>$ and our `u` was 0.8).
    
3. **Sample `R` (Rain):** Sample from $P(R|C=+c)$. Let's say we get `+r` (e.g., $P(R|+c)=<0.8, 0.2>$ and our `u` was 0.3).
    
4. **Sample `W` (WetGrass):** Sample from $P(W|S=-s, R=+r)$. Let's say we get `+w` (e.g., $P(W|-s, +r)=<0.9, 0.1>$ and our `u` was 0.2).
    

**Our first sample is:** `(+c, -s, +r, +w)`. We repeat this N times to get N samples.

## Properties

- **Consistent:** The probability of this procedure generating a specific sample, $S_{PS}(x_1...x_n)$, is exactly the true joint probability, $P(x_1...x_n)$. This is a very useful property.
    
- **Usage:** To estimate any probability $P(W)$, we just count the samples.
    
    - If we generate 5 samples and 4 have `+w` and 1 has `-w`, we estimate $P(W) \approx \langle 0.8, 0.2 \rangle$.
        
    - As $N \rightarrow \infty$, this estimate converges to the true probability.
        

**Limitation:** This method is great for _prior_ probabilities (like $P(W)$), but it's not directly designed to answer _conditional_ queries (like $P(C|+w)$). This leads to [[Rejection Sampling]].

### ❓ Review Questions

1. Why is it essential to sample in topological order? What would happen if you tried to sample `WetGrass` first?
    
2. If you use Prior Sampling, how do you estimate $P(Rain = \text{true})$?