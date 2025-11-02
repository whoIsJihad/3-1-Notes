# 🤖 Approximate Inference in BNs

_Source: `20. Uncertainty-5-BN-Sampling.pptx.pdf` (Pages 3-6)_

In the last topic, we learned about **Exact Inference** using **Variable Elimination**.

## The Problem with Exact Inference

While Variable Elimination is powerful, it has a major weakness: its worst-case complexity is exponential.

- As shown in the 3-SAT to Bayes' Net conversion (Page 4), inference in Bayesian networks is **NP-hard**.
    
- This means that for large, complex networks (like many real-world problems), calculating an exact answer is computationally intractable. It could take an impossibly long time.
    

## The Solution: Approximate Inference

If we can't get the _perfect_ answer, we can often get a _very good_ answer by using **sampling**.

**Sampling** is like running a repeated simulation. Instead of calculating the exact probability, we _generate_ a large number of "example worlds" (samples) based on the network's probabilities. We then estimate the probability of an event by just counting how many times it happened in our samples.

**Why sample?**

1. **Inference:** Getting one sample is _much_ faster than running Variable Elimination. We trade 100% accuracy for a massive speed-up.
    
2. **Learning:** Sometimes we get samples from a real-world process _before_ we even know the probabilities (this is a different topic).
    

This module will cover four main types of sampling for inference:

- [[Prior Sampling]]
    
- [[Rejection Sampling]]
    
- [[Likelihood Weighting]]
    
- [[Gibbs Sampling]]
    

### ❓ Review Questions

1. Why don't we just use Variable Elimination for every Bayesian Network?
    
2. What is the basic idea of approximate inference? What are we "trading" for speed?