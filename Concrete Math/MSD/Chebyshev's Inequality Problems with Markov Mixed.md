
These problems will require you to decide which inequality is appropriate, compare the bounds they give, or use them to find a missing piece of information.

**Reminder of the Theorems:**

1. Markov's Inequality: For a non-negative random variable $X$ and any $a > 0$:
    
    $$P(X \ge a) \le \frac{E[X]}{a}$$
    
2. Chebyshev's Inequality: For any random variable $X$ with mean $\mu$ and finite variance $\sigma^2$, and any $k > 0$:
    
    $$P(|X - \mu| \ge k\sigma) \le \frac{1}{k^2}$$
    
    - Alternative Form (often more useful): For any $a > 0$:
        
        $$P(|X - \mu| \ge a) \le \frac{\sigma^2}{a^2}$$
        

---

## Problem 1: The Tighter Bound

A factory's server processes financial transactions. The processing time $X$ is a non-negative random variable.

- The average processing time is $E[X] = 20$ ms.
    
- The variance of the processing time is $\text{Var}(X) = 4$ ms$^2$.
    

Find an upper bound for the probability that a transaction takes 30 ms or more (i.e., $P(X \ge 30)$) using:

a) Markov's Inequality.

b) Chebyshev's Inequality.

c) Which bound is "tighter" (i.e., gives a smaller, more informative number)?

### Solution 1:

a) Markov's Inequality:

We use $E[X] = 20$ and $a = 30$.

$$P(X \ge 30) \le \frac{E[X]}{a} = \frac{20}{30} = \frac{2}{3} \approx 0.667$$

b) Chebyshev's Inequality:

We have $\mu = 20$ and $\sigma^2 = 4$.

We want $P(X \ge 30)$. This is a "one-sided" probability.

Chebyshev gives a "two-sided" bound: $P(|X - 20| \ge a)$.

Let's find the bound for $P(|X - 20| \ge 10)$. (Since $30 - 20 = 10$).

Using the alternate form with $a = 10$:

$$P(|X - 20| \ge 10) \le \frac{\sigma^2}{a^2} = \frac{4}{10^2} = \frac{4}{100} = 0.04$$

Now, we must relate the one-sided probability to the two-sided one:

$$P(|X - 20| \ge 10) = P(X - 20 \ge 10) + P(X - 20 \le -10)$$

$$P(|X - 20| \ge 10) = P(X \ge 30) + P(X \le 10)$$

Since both probabilities $P(X \ge 30)$ and $P(X \le 10)$ are non-negative:

$$P(X \ge 30) \le P(X \ge 30) + P(X \le 10) = P(|X - 20| \ge 10)$$

Therefore, the bound for the two-sided event also applies to the one-sided event:

$$P(X \ge 30) \le 0.04$$

**c) Conclusion:**

- Markov's bound: 0.667 (or 66.7%)
    
- Chebyshev's bound: 0.04 (or 4%)
    

Chebyshev's bound is **much tighter**. This is because it uses the **variance**, which tells us the data is tightly clustered around the mean. Markov only uses the mean and ignores this crucial information.

---

## Problem 2: How Many Samples?

You are flipping a coin with an unknown probability of heads, $p$. You want to estimate $p$ by flipping the coin $n$ times and calculating the sample mean $\bar{X}_n$ (the proportion of heads).

You don't know $p$, but you know that for _any_ coin, the variance of a single flip, $\text{Var}(X_i)$, is at most **0.25**. (This maximum occurs when $p=0.5$).

Using Chebyshev's Inequality, what is the **minimum number of flips $n$** required to guarantee that the sample mean $\bar{X}_n$ is within **0.1** of the true mean $p$ with at least **99%** probability?

In other words, find the smallest $n$ such that $P(|\bar{X}_n - p| \le 0.1) \ge 0.99$.

### Solution 2:

1. Re-frame the problem:

We want $P(|\bar{X}_n - p| \le 0.1) \ge 0.99$.

This is the opposite of what Chebyshev bounds. Let's flip it:

We want $P(|\bar{X}_n - p| > 0.1) \le 1 - 0.99 = 0.01$.

(Note: $P(|\bar{X}_n - p| \ge 0.1)$ is what Chebyshev bounds, and $> 0.1$ is close enough for this bound).

**2. Find the properties of the Sample Mean $\bar{X}_n$:**

- $E[\bar{X}_n] = p$ (this is our $\mu$)
    
- $\text{Var}(\bar{X}_n) = \frac{\text{Var}(X_i)}{n}$. We use the worst-case variance: $\text{Var}(\bar{X}_n) \le \frac{0.25}{n}$. (This is our $\sigma^2$).
    

3. Apply Chebyshev's Inequality:

We want to bound $P(|\bar{X}_n - p| \ge 0.1)$.

- $\mu = p$
    
- $\sigma^2 = 0.25 / n$
    
- $a = 0.1$
    

$$P(|\bar{X}_n - p| \ge 0.1) \le \frac{\sigma^2}{a^2} = \frac{0.25 / n}{(0.1)^2}$$

$$P(|\bar{X}_n - p| \ge 0.1) \le \frac{0.25 / n}{0.01}$$

$$P(|\bar{X}_n - p| \ge 0.1) \le \frac{25}{n}$$

4. Solve for $n$:

We need this probability to be $\le 0.01$.

$$\frac{25}{n} \le 0.01$$

$$25 \le 0.01 \cdot n$$

$$n \ge \frac{25}{0.01}$$

$$n \ge 2500$$

**Conclusion:** You must flip the coin at least **2,500 times** to guarantee (via Chebyshev) that your estimate is within 0.1 of the true mean with 99% probability.

---

## Problem 3: Impossible Data

A researcher is studying the number of bugs $X$ in a new software module (which must be $\ge 0$). They tell you two things about their data:

1. The average number of bugs found was $E[X] = 5$.
    
2. From their dataset, they observed that the probability of finding 20 or more bugs was $P(X \ge 20) = 0.3$.
    

Can both of these statements be true at the same time? Use an inequality to justify your answer.

### Solution 3:

We have a non-negative random variable $X$, so we can use Markov's Inequality.

- $E[X] = 5$
    
- $a = 20$
    

Let's calculate the maximum possible probability for $P(X \ge 20)$:

$$P(X \ge 20) \le \frac{E[X]}{a} = \frac{5}{20} = 0.25$$

Conclusion:

Markov's Inequality guarantees that the probability of finding 20 or more bugs cannot be more than 0.25 (or 25%).

The researcher claims the observed probability is 0.3 (or 30%).

This is a **contradiction**. The researcher's two statements cannot both be true. Either their calculated average is wrong, or their observed probability is wrong.