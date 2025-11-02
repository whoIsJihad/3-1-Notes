# Agnostic Learning

_Source: `13. Learning-Theory-7-PAC-AGN.pdf` (Pages 9, 11-14, 42, 50)_

**Agnostic Learning** is a more realistic and general model of learning. It gets its name because the learner is "agnostic" about whether the true function is in the hypothesis space.

- **Assumption (Relaxed)**: We **drop the realizability assumption**. The true function $f$ _may or may not be_ in our hypothesis space $H$ ($f \notin H$ is possible).
    
- **Why?** The true concept might be too complex for our chosen model (e.g., trying to learn a complex, non-linear boundary using only a linear classifier).
    
- **Learner's Strategy**: Because $f$ might not be in $H$, we are **not guaranteed** to find a hypothesis with zero training error.
    
- **New Goal**: The learner's goal is to find the hypothesis $h \in H$ that has the **lowest possible training error**, $err_S(h)$.
    

## Generalization Bound

We can no longer just bound $err_D(h)$. Instead, we want to know: "How far apart can the true error $err_D(h)$ be from the training error $err_S(h)$?"

Using [[Hoeffding's Inequality]] and a union bound over all hypotheses in $H$, we get this probabilistic bound: $P[\exists h \in H \text{ s.t. } err_D(h) > err_S(h) + \epsilon] \le |H|e^{-2m\epsilon^2}$

## Agnostic Sample Complexity

We want this "bad event" probability to be small, i.e., $\le \delta$. $|H|e^{-2m\epsilon^2} \le \delta$

Solving for $m$, we get the sample complexity for agnostic learning:

> $m \ge \frac{1}{2\epsilon^2} (ln(|H|) + ln(\frac{1}{\delta}))$

### Comparison to Realizable (Occam's) Bound

- **Realizable**: $m \propto \frac{1}{\epsilon}$
    
- **Agnostic**: $m \propto \frac{1}{\epsilon^2}$
    

The agnostic bound requires _quadratically_ more samples with respect to $\epsilon$. This is the "price" we pay for not knowing if the true function is in our hypothesis space.

### ❓ Review Questions

1. What is the main assumption that Agnostic Learning relaxes, compared to the standard PAC model?
    
2. Why is the learner's goal in agnostic learning to "minimize training error" instead of "find a consistent hypothesis"?
    
3. What is the key difference in the sample complexity bounds ($m$) between the realizable and agnostic models?