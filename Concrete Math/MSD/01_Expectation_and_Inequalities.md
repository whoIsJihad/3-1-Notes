

# 01 - Expectation, Moments, and Core Inequalities

## Expectation and Conditional Expectation

### Basic Definitions

- **Discrete RV:**
    
    $$E[X] = \sum_{x} x P(X=x)$$
- **Continuous RV:**
    
    $$E[X] = \int_{-\infty}^{\infty} x f_{X}(x) dx$$
- **Conditional Expectation:**
    
    $$E[X | Y=y] = \sum_{x} x P(X=x | Y=y)$$

### Properties of Conditional Expectation

1. **Taking Out What's Known:**
    
    $$E[Y h(X) | X] = h(X) E[Y | X]$$
2. **Independence:** $E[Y|X] = E[Y]$, if $X$ and $Y$ are independent.
    
3. **Law of Iterated Expectation (LOIE) / Adam's Law:**
    
    $$E[ E[Y | X] ] = E[Y]$$

### Example: Miner's Trap (LOIE)

A miner is in a trap with three doors. Each door is chosen with probability $1/3$.

- **D1:** Safely exits in 2 hours.
    
- **D2:** Loops back after 3 hours. (Time spent: $3 + E[X]$)
    
- **D3:** Loops back after 5 hours. (Time spent: $5 + E[X]$) Let $X$ be the time until escape, and $Y$ be the chosen door.
    

$$E[X] = E[X|Y=1]P(Y=1) + E[X|Y=2]P(Y=2) + E[X|Y=3]P(Y=3)$$$$E[X] = (2) \cdot \frac{1}{3} + (3 + E[X]) \cdot \frac{1}{3} + (5 + E[X]) \cdot \frac{1}{3}$$$$3 E[X] = 2 + 3 + E[X] + 5 + E[X]$$$$E[X] = 10 \text{ hours}$$

## Covariance and Correlation

- **Variance:**
    
    $$\operatorname{Var}(X) = E[(X - E[X])^2] = E[X^2] - (E[X])^2$$
- **Covariance:** Measures the joint variability of two RVs.
    
    $$\operatorname{Cov}(X, Y) = E[(X - E[X])(Y - E[Y])] = E[XY] - E[X]E[Y]$$
    
    If $X$ and $Y$ are independent, $\operatorname{Cov}(X, Y) = 0$.
    
- **Correlation:**
    
    $$\operatorname{Corr}(X, Y) = \frac{\operatorname{Cov}(X, Y)}{\sqrt{\operatorname{Var}(X)\operatorname{Var}(Y)}}$$
    
    The correlation coefficient $\rho$ satisfies $|\operatorname{Corr}(X, Y)| \le 1$.
    

## Probability Inequalities

### 1. Markov's Inequality

For a non-negative random variable $X$, and any $t > 0$:

$$P(X > t) \le \frac{E[X]}{t}$$

**Example:** If the mean age ($\mu$) of a group is 40, $P(X > 80) \le 40 / 80 = 0.5$.
For more Markov Related Problem , read [[Markov Theorem Problems]]

### 2. Chebyshev's Inequality

Let $\mu = E[X]$ and $\sigma^2 = \operatorname{Var}(X)$. For any $t > 0$:

$$P(|X - \mu| \ge t) \le \frac{\sigma^2}{t^2}$$

In terms of standard deviations ($t = k\sigma$):

$$P(|X - \mu| \ge k\sigma) \le \frac{1}{k^2}$$

**Example (Neural Network Predictor):** Let $\bar{X}_n$ be the observed error rate from $n$ test cases. $E[\bar{X}_n] = p$ and $\operatorname{Var}(\bar{X}_n) = p(1-p)/n$. Using the inequality with $\epsilon > 0$:

$$P(|\bar{X}_n - p| > \epsilon) \le \frac{\operatorname{Var}(\bar{X}_n)}{\epsilon^2} = \frac{p(1-p)}{n\epsilon^2}$$

Since $p(1-p) \le 1/4$:

$$P(|\bar{X}_n - p| > \epsilon) \le \frac{1}{4n\epsilon^2}$$

For more Chebyshev Related Problem (Mixed with Markov)read [[ Chebyshev's Inequality Problems with Markov Mixed]]
### 3. Cauchy-Schwarz Inequality

If $X$ and $Y$ have finite variances:

$$|E[XY]| \le \sqrt{E[X^2]E[Y^2]}$$

When applied to centered RVs ($X'=X-E[X], Y'=Y-E[Y]$):

$$|\operatorname{Cov}(X, Y)| \le \sqrt{\operatorname{Var}(X)\operatorname{Var}(Y)}$$

### 4. Jensen's Inequality

If $g$ is a **convex function** (e.g., $x^2$, $e^x$):

$$E[g(X)] \ge g(E[X])$$

If $g$ is a **concave function** (e.g., $\ln x$, $\sqrt{x}$):

$$E[g(X)] \le g(E[X])$$

**Example:** $E[\ln X] \le \ln(E[X])$.