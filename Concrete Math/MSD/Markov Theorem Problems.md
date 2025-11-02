


For a non-negative random variable $X$ (meaning $X \ge 0$) and any constant $a > 0$:

$$P(X \ge a) \le \frac{E[X]}{a}$$

---

### Problem 1: Server Response Time

The average response time ($E[X]$) for a query to a web server is **50 milliseconds (ms)**. Response time cannot be negative.

What is the upper bound on the probability that a query will take **at least 250 ms**?

**Solution 1:**

We are given:

- $X$ = Response Time (which is non-negative, $X \ge 0$)
    
- $E[X] = 50$ ms
    
- $a = 250$ ms
    

Using Markov's Inequality:

$$P(X \ge a) \le \frac{E[X]}{a}$$

$$P(X \ge 250) \le \frac{50}{250}$$

$$P(X \ge 250) \le \frac{1}{5} \text{ or } 0.2$$

**Conclusion:** There is at most a 20% chance that a query will take 250 ms or more.

---

### Problem 2: Exam Scores

The average score on a final exam was 70 out of 100 ($E[X] = 70$). Scores are non-negative.

a) Give an upper bound on the probability that a randomly chosen student scored at least 95.

b) What upper bound does the inequality give for the probability that a student scored at least 60?

**Solution 2:**

**Part (a):**

- $E[X] = 70$
    
- $a = 95$
    

$$P(X \ge 95) \le \frac{70}{95}$$

$$P(X \ge 95) \approx 0.737$$

**Conclusion (a):** There is at most a 73.7% chance that a student scored 95 or more.

**Part (b):**

- $E[X] = 70$
    
- $a = 60$
    

$$P(X \ge 60) \le \frac{70}{60}$$

$$P(X \ge 60) \le 1.167$$

**Conclusion (b):** The inequality states that the probability is less than or equal to 1.167. Since we already know that no probability can be greater than 1, this is an **uninformative bound**. Markov's Inequality is often loose and is only useful when $a$ is significantly larger than $E[X]$.

---

### Problem 3: Applying Markov to Variance (Advanced)

This problem shows how Markov's Inequality is the basis for **Chebyshev's Inequality**.

Let $X$ be _any_ random variable (not necessarily non-negative) with:

- Mean $E[X] = \mu = 10$
    
- Variance $\text{Var}(X) = \sigma^2 = 9$
    

Now, let's define a new random variable $Y$:

$$Y = (X - 10)^2$$

a) Is $Y$ a non-negative random variable?

b) What is the expected value of $Y$, $E[Y]$?

c) Use Markov's Inequality on $Y$ to find an upper bound for $P(Y \ge 36)$.

**Solution 3:**

a) Is $Y$ non-negative?

Yes. Since $Y$ is the result of a squared term, its value can never be negative. $Y = (X - 10)^2 \ge 0$.

b) What is $E[Y]$?

By the definition of variance:

$$\text{Var}(X) = E[(X - E[X])^2]$$

We are given $E[X] = 10$, so:

$$\text{Var}(X) = E[(X - 10)^2]$$

We defined $Y = (X - 10)^2$, therefore:

$$E[Y] = \text{Var}(X)$$

Given $\text{Var}(X) = 9$, we have $E[Y] = 9$.

c) Find the bound for $P(Y \ge 36)$.

We use Markov's Inequality on the non-negative variable $Y$:

- $Y$ is non-negative.
    
- $E[Y] = 9$
    
- $a = 36$
    

$$P(Y \ge 36) \le \frac{E[Y]}{36}$$

$$P(Y \ge 36) \le \frac{9}{36}$$

$$P(Y \ge 36) \le \frac{1}{4}$$

(Deeper Insight):

Notice that $P(Y \ge 36)$ is the same as $P((X - 10)^2 \ge 36)$.

This is the same as $P(|X - 10| \ge 6)$.

So, you just proved Chebyshev's Inequality for this specific case: $P(|X - \mu| \ge k\sigma) \le \frac{1}{k^2}$. (Here, $k=2$, since $6 = 2 \cdot \sigma = 2 \cdot 3$).