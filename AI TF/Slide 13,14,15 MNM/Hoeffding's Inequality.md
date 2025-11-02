# Hoeffding's Inequality

_Source: `13. Learning-Theory-7-PAC-AGN.pdf` (Pages 23-27, 32)_

**Hoeffding's Inequality** (a "tail bound") is a statistical tool that gives an upper bound on how much the _empirical mean_ of a set of random variables can differ from its _true expected value_.

In machine learning, we use it to connect **training error** (an empirical mean) to **generalization error** (the true mean).

## The Inequality

Let's say we have $m$ independent trials (e.g., $m$ coin flips, or $m$ training examples).

- $\overline{p}$ is the **empirical mean** (e.g., fraction of heads we saw, or $err_S(h)$).
    
- $p$ is the **true mean** (e.g., the coin's actual bias, or $err_D(h)$).
    

Hoeffding's inequality states that the probability of the empirical mean being "far" from the true mean by more than $\epsilon$ is:

> $P[p > \overline{p} + \epsilon] \le e^{-2m\epsilon^2}$ $P[|p - \overline{p}| > \epsilon] \le 2e^{-2m\epsilon^2}$ (a two-sided version)

This tells us that the probability of our estimate being wildly wrong **decreases exponentially** as our number of samples, $m$, increases.

## Application to Agnostic Learning

For a _single, fixed hypothesis_ $h$, we can set:

- $\overline{p} = err_S(h)$ (training error over $m$ samples)
    
- $p = err_D(h)$ (true generalization error)
    

This gives us the bound for _one_ hypothesis: $P[err_D(h) > err_S(h) + \epsilon] \le e^{-2m\epsilon^2}$

To get the bound for our _entire_ hypothesis space $H$, we use a **Union Bound** to say the probability of _any_ $h \in H$ being bad is at most $|H|$ times this amount, which leads to the full [[Agnostic Learning]] bound.

### ❓ Review Questions

1. In simple terms, what does Hoeffding's Inequality tell us about sample size ($m$)?
    
2. Why can't we just use the single-hypothesis bound $P[...] \le e^{-2m\epsilon^2}$ for our final learning bound? Why do we need the $|H|$ term?