# Full Joint Distribution from a Bayesian Network

_Source: `15. CSE317...pdf` (Pages 23-26, 29)_

A [[Bayesian Networks (BN)|Bayesian Network]] is a powerful tool because it provides a compact way to represent the **full joint probability distribution** (FJD) over all variables in the network.

If you have the FJD, you can, in principle, answer _any_ probabilistic query about the variables.

## The Chain Rule for BNs

Normally, the chain rule of probability would be: $P(x_1, ..., x_n) = P(x_n | x_{n-1}, ..., x_1) \times ... \times P(x_1)$

But because of the [[Conditional Independence in BNs|conditional independence assumptions]] in a BN, this simplifies dramatically. The probability of any node $x_i$ given _all_ its predecessors is just the probability of $x_i$ given its **parents**.

This gives us the **BN Chain Rule**:

> $P(x_1, ..., x_n) = \prod_{i=1}^{n} P(x_i | Parents(X_i))$

This means the full joint distribution is simply the **product of all the individual (conditional) probabilities** from the [[Conditional Probability Tables (CPT)|CPTs]] of each node.

## Example: Calculating a Full Joint Probability

Let's calculate the probability of a specific event from the Burglary-Alarm network:

- **Query**: What is the probability that the alarm sounds ($a$), there is no burglary ($\neg b$), there is no earthquake ($\neg e$), and both John ($j$) and Mary ($m$) call?
    
- **We need to compute**: $P(j, m, a, \neg b, \neg e)$.
    

Using the BN Chain Rule, we just multiply the corresponding CPT entries: $P(j, m, a, \neg b, \neg e) = P(j|a) \times P(m|a) \times P(a|\neg b, \neg e) \times P(\neg b) \times P(\neg e)$

- **Step 1:** $P(j|a)$: John calls given alarm is true. (e.g., 0.90)
    
- **Step 2:** $P(m|a)$: Mary calls given alarm is true. (e.g., 0.70)
    
- **Step 3:** $P(a|\neg b, \neg e)$: Alarm given no burglary and no earthquake. (e.g., 0.001)
    
- **Step 4:** $P(\neg b)$: No burglary. (e.g., $1 - 0.001 = 0.999$)
    
- **Step 5:** $P(\neg e)$: No earthquake. (e.g., $1 - 0.002 = 0.998$)
    

**Result**: $0.90 \times 0.70 \times 0.001 \times 0.999 \times 0.998 \approx 0.000628$

### ❓ Review Questions

1. Why is the BN Chain Rule so much simpler than the standard chain rule of probability?
    
2. Write out the BN Chain Rule expression for $P(Rain, Sprinkler, \neg GrassWet)$ based on the network on page 5.