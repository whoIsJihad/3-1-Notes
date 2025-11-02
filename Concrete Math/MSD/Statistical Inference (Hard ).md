# Detailed Study Guide: Core Statistical Inference and Probability (From Notes)

This guide covers the core concepts, practical examples, and derivations from your mathematical notes, structured for step-by-step learning.

## Part 1: Estimation and Confidence Intervals

### 1.1 Central Limit Theorem (CLT) and Standard Error

**Statement:** For $n$ independent and identically distributed (IID) random samples ($X_1, \dots, X_n$) from any distribution with mean $\mu$ and variance $\sigma^2$, the distribution of the sample mean ($\bar{X}_n$) approaches a Normal Distribution as $n \to \infty$.

$$\bar{X}_n \sim \mathcal{N} \left( \mu, \frac{\sigma^2}{n} \right)$$

- **Standard Error (SE):** The standard deviation of the sample mean's distribution.
    
    $$SE = \sqrt{\text{Var}(\bar{X}_n)} = \frac{\sigma}{\sqrt{n}}$$
    - **Approximation:** Since the population standard deviation ($\sigma$) is usually unknown, we approximate it using the sample standard deviation ($s$): $SE \approx \frac{s}{\sqrt{n}}$.
        

### 1.2 Confidence Interval (CI) Calculation

A CI is defined by: $\text{CI} = \text{Point Estimate} \pm \text{Margin of Error}$.

**Example from Notes: Employee Meeting Time**

- **Scenario:** A company selects $n=50$ employees.
    
- **Sample Mean (Point Estimate):** $\bar{x} = 8.3$ hours.
    
- **Sample Standard Deviation:** $s = 2.1$ hours.
    
- **Goal:** Find the 95% Confidence Interval for the true average time ($\mu$) spent in meetings.
    

**Step 1: Verify Assumptions**

- $n=50$, which is sufficiently large ($n>30$). By the CLT, we can assume $\bar{X}$ is normally distributed.
    
- The sample size ($50$) is less than $10\%$ of the population ($5000$ employees), so sampling without replacement is acceptable.
    

**Step 2: Calculate Standard Error (SE)**

$$SE = \frac{s}{\sqrt{n}} = \frac{2.1}{\sqrt{50}} \approx 0.3$$

**Step 3: Determine the Critical Value (**$Z^*$ **)** For a **95% Confidence Interval**, we need the $Z$-score that leaves $2.5\%$ ($\alpha/2$) in each tail.

$$P(|Z| < Z^*) = 0.95$$

The critical value is $Z^* = 1.96$.

**Step 4: Calculate the Margin of Error (ME)**

$$ME = Z^* \times SE = 1.96 \times 0.3 \approx 0.588$$

_(Note: The notes approximated  $Z^* = 2$ yielding $ME = 2 \times 0.3 = 0.6$)*.

**Step 5: Construct the CI**

$$\text{CI} = \bar{x} \pm ME$$$$\text{CI} = 8.3 \pm 0.6$$$$\text{CI} = (7.7, 8.9)$$

**Interpretation:** We are 95% confident that the true average time spent in meetings ($\mu$) is between $7.7$ **hours and** $8.9$ **hours**.

## Part 2: Hypothesis Testing

Hypothesis testing is a procedure to test a claim about a population parameter against observed data.

### 2.1 The Hypothesis Testing Framework

| Step                  | Description                                                             |
| --------------------- | ----------------------------------------------------------------------- |
| **1. Hypotheses**     | State $H_0$ (Null: no effect) and $H_A$ (Alternate: effect/difference). |
| **2. Test Statistic** | Calculate a value (like a $Z$-score or $t$-score) from the sample data. |
| **3. p-value**        | Calculate $P(\text{Data} \mid H_0 \text{ is true})$.                    |
| **4. Decision**       | Compare p-value to the significance level ($\alpha$).                   |

### 2.2 Example from Notes: Headline Guessing

**Scenario:** Can people guess fake headlines better than random guessing?

- $n=54$ trials.
    
- Observed success (correct identification) $X=22$.
    
- Random guessing probability is $P=1/7$.
    

**Step 1: State the Hypotheses**

- **Null Hypothesis (**$H_0$**):** People are guessing randomly.
    
    $$H_0: P = \frac{1}{7} \approx 0.142$$
- **Alternative Hypothesis (**$H_A$**):** People are better than random guessing (a one-tailed test).
    
    $$H_A: P > \frac{1}{7}$$

**Step 2: Determine the Test Statistic** The total number of correct identifications $X$ follows a **Binomial Distribution** under $H_0$.

$$X \sim \text{Bin}(n=54, P=1/7)$$

The observed success rate is $\frac{22}{54} \approx 40.7\%$.

**Step 3: Calculate the p-value** The p-value is the probability of observing 22 or _more_ successes, assuming $H_0$ is true.

$$\text{p-value} = P(X \ge 22 \mid H_0) = \sum_{k=22}^{54} \binom{54}{k} (\frac{1}{7})^{k} (\frac{6}{7})^{54-k}$$

**Result from Notes:**

$$\text{p-value} \approx 1.86 \times 10^{-6}$$

**Step 4: Make a Decision**

- Assuming a standard $\alpha = 0.05$.
    
- Since the $\text{p-value} (1.86 \times 10^{-6}) \ll 0.05$ (p-value is much smaller than $\alpha$).
    
- **Conclusion:** Reject $H_0$. There is strong evidence that people are identifying fake headlines better than random chance.
    

## Part 3: Maximum Likelihood Estimator (MLE) Derivations

The MLE seeks the parameter value that best explains the data.

### 3.1 MLE for Bernoulli Distribution Parameter ($p$)

- **Setup:** $X_1, \dots, X_n \sim \text{Bernoulli}(p)$. Let $S = \sum X_i$ be the total number of successes.
    
- **Single observation PDF:** $f(x; p) = p^x (1-p)^{1-x}$ (where $x \in \{0, 1\}$).
    

**1. Likelihood Function** $L_n(p)$

$$L_n(p) = \prod_{i=1}^{n} f(x_i; p) = \prod_{i=1}^{n} p^{x_i} (1-p)^{1-x_i}$$$$L_n(p) = p^{\sum x_i} (1-p)^{\sum (1-x_i)} = p^S (1-p)^{n-S}$$

**2. Log-Likelihood** $l_n(p)$

$$l_n(p) = \log L_n(p) = S \log(p) + (n-S) \log(1-p)$$

**3. Find the Maximum (Solve** $\frac{\partial l_n(p)}{\partial p} = 0$**)**

$$\frac{\partial l_n(p)}{\partial p} = \frac{S}{p} - \frac{n-S}{1-p} = 0$$$$\frac{S}{p} = \frac{n-S}{1-p}$$$$S(1-p) = p(n-S)$$$$S - Sp = np - Sp$$$$S = np$$$$\hat{p} = \frac{S}{n}$$

The MLE for the probability of success $p$ is the sample proportion of successes.

