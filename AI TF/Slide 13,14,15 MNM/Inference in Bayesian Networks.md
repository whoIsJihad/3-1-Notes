# Inference in Bayesian Networks

_Source: `15. CSE317...pdf` (Page 6, 31, 32)_

**Inference** is the process of using our [[Bayesian Networks (BN)|Bayesian Network]] to answer questions (queries) based on observed **evidence**. We want to determine the probability of **unobserved variables**.

## Types of Inference

- **Causal Inference**: Reasoning from cause to effect.
    
    - _Example_: "What is the probability of the grass being wet, _given_ it is raining?" ($P(GrassWet | Raining)$).
        
- **Diagnostic Inference**: Reasoning from effect to cause.
    
    - _Example_: "What is the probability of rain, _given_ the grass is wet?" ($P(Rain | GrassWet)$).
        

## Exact Inference

The most common task is to compute the posterior distribution of a **query variable** ($X$) given some **evidence variables** ($e$).

- **Example Query**: "What is the probability of a `Burglary`, _given_ that `JohnCalls` and `MaryCalls` are both true?"
    
- **Notation**: $P(Burglary | j, m)$ or $P(B | j, m)$.
    

To answer this, we use the definition of conditional probability: $P(B | j, m) = \frac{P(B, j, m)}{P(j, m)}$

The $P(j, m)$ in the denominator is a normalizing constant, often written as $\alpha$. $P(B | j, m) = \alpha P(B, j, m)$

The real problem is computing $P(B, j, m)$. To do this, we must consider all the variables we _didn't_ observe, known as the **hidden variables** (in this case, `Alarm` and `Earthquake`).

We "sum out" (or marginalize) these hidden variables from the [[Full Joint Distribution from a BN|full joint distribution]]: $P(B, j, m) = \sum_{a} \sum_{e} P(B, j, m, a, e)$

Using the BN chain rule, this becomes: $P(B, j, m) = \sum_{a} \sum_{e} P(j|a) P(m|a) P(a|B, e) P(B) P(e)$

This "sum of products" is the core calculation.

- **Naive Approach**: This is very expensive. If we have $k$ boolean hidden variables, we'd have to compute $2^k$ terms. This is "intractable" or exponential.
    
- **Efficient Approach**: We can improve this by "moving the sums inside" the expression to avoid re-computing work. This is the central idea behind the [[Variable Elimination Algorithm]].
    

### ❓ Review Questions

1. What is the difference between causal and diagnostic inference? Give an example of each.
    
2. What is a "hidden variable" in the context of a query? Why do we need to "sum them out"?