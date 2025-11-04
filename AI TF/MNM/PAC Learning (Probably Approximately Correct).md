# Probably Approximately Correct (PAC) Learning

**Learning Theory** asks the fundamental questions:

1. How can we be sure $h$ will predict well on unseen inputs?
    
2. How do we know $h$ is close to $f$ if we don't know $f$?
    
3. How many examples $N$ do we need to get a good $h$?
    

**PAC Learning** provides a framework to answer this.

## Core Idea

Any hypothesis $h$ that is _consistent_ with a _sufficiently large_ set of training examples is **unlikely to be seriously wrong**. Such a hypothesis must be **Probably Approximately Correct (PAC)**.

- **Approximately Correct:** The generalization error is low. $error(h) <= \epsilon$ (for some small $\epsilon$).
    
- **Probably:** This holds with high probability $1 - \delta$ (for some small $\delta$).
    

## Sample Complexity

PAC learning allows us to calculate the number of examples $N$ (sample complexity) needed to guarantee this.

We want to ensure that the probability of a "bad" hypothesis (one with $error(h) > \epsilon$) being consistent with $N$ examples is very low (less than $\delta$).

The probability of _one_ bad hypothesis $h_b$ being consistent with $N$ examples is $\le (1 - \epsilon)^N$.

The probability of _any_ bad hypothesis in the hypothesis space $\mathcal{H}$ being consistent is: $P(\mathcal{H}_{bad} \text{ contains a consistent } h) \le |\mathcal{H}|(1 - \epsilon)^N$

We want this probability to be $\le \delta$. Using $1-\epsilon \le e^{-\epsilon}$, we can solve for $N$:

$$N \ge \frac{1}{\epsilon} \left( \ln\frac{1}{\delta} + \ln|\mathcal{H}| \right)$$

This key result shows that the number of examples needed (the **sample complexity**) grows logarithmically with the size of the hypothesis space, $|\mathcal{H}|$.

(From: _Learning Theory-1.pptx.pdf_)

**Links:**

- Back to: [[Machine Learning Index]]
    
- Related: [[Hypothesis Space]], [[Bayesian Learning (MAP)]]