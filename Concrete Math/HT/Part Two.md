## Part 4: Famous Problems and Paradoxes

### 4.1 - The Birthday Problem

#tags: #probability #paradox #birthday-problem

#### The Problem

What is the minimum number of people needed in a room so that $P(\text{at least two share a birthday}) > 50\%$?

#### The Complement Approach

It's easier to calculate the probability of the complement: **"no two people share a birthday"** ($P(A^c)$).

$$P(\text{at least one match}) = 1 - P(\text{no match})$$

#### Calculation for $k$ People

The probability of no match for $k$ people (out of 365 days) is:

$$P(\text{no match}) = \frac{365 \times 364 \times \dots \times (365 - k + 1)}{365^k}$$

This can be written using permutations:

$$P(\text{no match}) = \frac{P(365, k)}{365^k}$$

|**Number of People (**$k$**)**|**Probability of a Match**|
|---|---|
|10|11.7%|
|20|41.1%|
|**23**|**50.7%**|
|30|70.6%|
|50|97.0%|

The threshold is crossed at $k=23$.

### 4.2 - The Monty Hall Problem

#tags: #probability #paradox #monty-hall

#### The Problem

You pick one of three doors. The host (who knows where the car is) opens one of the other doors to reveal a goat. Should you **stick** with your original choice or **switch** to the remaining unopened door?

#### The Answer

**You should always switch.** Switching doubles your probability of winning the car from $1/3$ to $2/3$.

#### Explanation using Conditional Probability

Assume you pick Door #1, and the host opens Door #3 ($H_3$).

- $C_i$: Car is behind Door $i$. $P(C_1) = P(C_2) = P(C_3) = 1/3$.
    
- $P(H_3 \mid C_1) = 1/2$ (Host randomly opens #2 or #3).
    
- $P(H_3 \mid C_2) = 1$ (Host must open #3).
    
- $P(H_3 \mid C_3) = 0$ (Host cannot open #3).
    

Using Bayes' Rule (with $P(H_3) = 1/2$ by LOTP):

- **Probability of Staying:**
    
    $$P(C_1 \mid H_3) = \frac{P(H_3 \mid C_1) P(C_1)}{P(H_3)} = \frac{(1/2) \cdot (1/3)}{1/2} = \frac{1}{3}$$
- **Probability of Switching:**
    
    $$P(C_2 \mid H_3) = \frac{P(H_3 \mid C_2) P(C_2)}{P(H_3)} = \frac{1 \cdot (1/3)}{1/2} = \frac{2}{3}$$

### 4.3 - Simpson's Paradox

#tags: #statistics #paradox #simpsons-paradox

#### The Paradox

**Simpson's Paradox** occurs when a trend observed within subgroups of data disappears or reverses when the groups are combined.

#### Example: Medical Drug Trial

|**Treatment**|**Heart Surgery Success Rate**|**Bandage Success Rate**|
|---|---|---|
|**Dr. Hibbert**|70/90 = **77%**|10/10 = **100%**|
|**Dr. Nick**|5/20 = 25%|81/90 = 90%|

- **Conclusion by Subgroup**: Dr. Hibbert is better in both categories.
    
- **Combined Aggregates (as presented in the original text):** Dr. Hibbert (80 successes / 100 patients = 80%) vs. Dr. Nick (81 successes / 100 patients = **81%**).
    
- **Paradoxical Reversal:** Dr. Hibbert is better in every subgroup, but Dr. Nick is better overall.
    

#### Explanation

The paradox is caused by a **lurking variable** (procedure difficulty) that is unequally distributed between the groups. Dr. Hibbert was assigned a disproportionately high number of difficult cases, skewing his overall average downwards.

### 4.4 - Gambler's Ruin

#tags: #probability #random-walk #gamblers-ruin

#### The Problem

Player A starts with $i$ dollars, Player B with $N-i$. Player A wins $1 with probability $p$, and loses $1 with probability $q=1-p$. What is $P_i$, the probability that A wins the total $N$ dollars before losing everything?

#### The Recurrence Relation

$P_i$ is the probability that A wins starting with $i$ dollars.

$$P_i = p \cdot P_{i+1} + q \cdot P_{i-1} \quad \text{for } 1 \le i \le N-1$$

**Boundary Conditions:** $P_0 = 0$ (A is ruined), $P_N = 1$ (A wins).

#### The Solution

##### Case 1: Fair Game ($p = q = 1/2$)

The probability of A winning is their initial share of the total capital.

$$P_i = \frac{i}{N}$$

##### Case 2: Unfair Game ($p \ne 1/2$)

The solution involves the ratio $\rho = q/p$:

$$P_i = \frac{1 - \rho^i}{1 - \rho^N} \quad \text{where } \rho = \frac{q}{p}$$

### 4.5 - St. Petersburg Paradox

#tags: #probability #paradox #expected-value #st-petersburg

#### The Game

A fair coin is tossed until the first head appears on the $k$-th toss. The payout is $Y = 2^k$ dollars. $P(X=k) = (1/2)^k$.

#### The Paradox: Infinite Expected Value

The expected payout $E[Y]$ is infinite:

$$E[Y] = \sum_{k=1}^{\infty} (\text{Payout for } k \text{ flips}) \times P(k \text{ flips})$$$$E[Y] = \sum_{k=1}^{\infty} 2^k \cdot \left(\frac{1}{2}\right)^k = \sum_{k=1}^{\infty} 1 = \infty$$

#### Explanations and Resolutions

The paradox (that a rational person would pay an infinite amount) is resolved by:

1. **Diminishing Marginal Utility**: The subjective value of money grows slower than the dollar amount (e.g., logarithmically).
    
2. **Finite Resources**: Any real-world house has a finite bankroll, capping the maximum payout and resulting in a finite expected value.
    

## Part 5: Random Variables

### 5.1 - Definition of a Random Variable

#tags: #probability #random-variables

A **Random Variable (**$\mathbf{X}$**)** is a function that maps outcomes from a sample space $S$ to the set of real numbers ($\mathbb{R}$). It assigns a numerical value to the outcome of a random experiment.

- **Discrete Random Variables**: Take on a finite or countably infinite number of distinct values (e.g., number of heads).
    
- **Continuous Random Variables**: Can take on any value within a given range (e.g., temperature).
    

### 5.2 - Probability Mass Function (PMF)

#tags: #probability #random-variables #pmf

The **Probability Mass Function (PMF)** gives the probability that a **discrete** random variable $X$ is exactly equal to some value $x$.

$$\mathbf{p(x) = P(X = x)}$$

#### Properties of a PMF

1. Non-negativity: $p(x) \ge 0$ for all $x$.
    
2. Normalization: $\sum_{x} p(x) = 1$.
    

### 5.3 - Cumulative Distribution Function (CDF)

#tags: #probability #random-variables #cdf

The **Cumulative Distribution Function (CDF)** gives the probability that a random variable $X$ is less than or equal to some value $x$. It is defined for both discrete and continuous variables.

$$\mathbf{F(x) = P(X \le x)}$$

#### Relationship between PMF, PDF, and CDF

- **Discrete**: $P(a < X \le b) = F(b) - F(a)$.
    
- **Continuous**: The Probability Density Function (PDF) $f(x)$ is the derivative of the CDF, $f(x) = F'(x)$.
    

### 5.4 - Expectation (Expected Value)

#tags: #probability #random-variables #expectation

The **Expected Value (**$\mathbf{E[X]}$ **or** $\mu$**)** is the long-run average value of the random variable.

**Definition for a Discrete Random Variable:**

$$E[X] = \sum_{x} x \cdot P(X=x)$$

**Law of the Unconscious Statistician (LOTUS):** To find the expectation of a function $g(X)$:

$$E[g(X)] = \sum_{x} g(x) \cdot P(X=x)$$

(For continuous, replace the sum with an integral).

### 5.5 - Variance and Standard Deviation

#tags: #probability #random-variables #variance

The **Variance (**$\mathbf{\operatorname{Var}(X)}$ **or** $\sigma^2$**)** measures the spread of the distribution around the mean.

**Definition:**

$$\operatorname{Var}(X) = E\left[ (X - E[X])^2 \right]$$

**Computational Formula:**

$$\operatorname{Var}(X) = E[X^2] - [E[X]]^2$$

**Standard Deviation (**$\mathbf{\operatorname{SD}(X)}$ **or** $\sigma$**):**

$$\operatorname{SD}(X) = \sqrt{\operatorname{Var}(X)}$$

#### Properties of Variance

1. $\operatorname{Var}(a) = 0$
    
2. $\operatorname{Var}(X + b) = \operatorname{Var}(X)$
    
3. $\operatorname{Var}(aX) = a^2 \cdot \operatorname{Var}(X)$
    
4. If $X$ and $Y$ are **independent**: $\operatorname{Var}(X + Y) = \operatorname{Var}(X) + \operatorname{Var}(Y)$.
    

### 5.6 - Linearity of Expectation

#tags: #probability #random-variables #expectation #linearity

**Linearity of Expectation** states that the expected value of a sum of random variables is the sum of their individual expected values, regardless of whether the variables are independent or not.

$$\mathbf{E[X + Y] = E[X] + E[Y]}$$$$\mathbf{E[c X] = c \cdot E[X]}$$

**Example: Expectation of a Binomial Distribution** If $X \sim \operatorname{Bin}(n, p)$, and $X = \sum_{i=1}^n X_i$ where $X_i$ are independent Bernoulli trials with $E[X_i] = p$:

$$E[X] = E\left[\sum_{i=1}^n X_i\right] = \sum_{i=1}^n E[X_i] = \sum_{i=1}^n p = np$$

### 5.7 - Indicator Random Variables

#tags: #probability #random-variables #indicator-variables

An **Indicator Random Variable (**$\mathbf{I_A}$**)** takes the value $1$ if event $A$ occurs, and $0$ otherwise.

#### The Fundamental Bridge

The expectation of an indicator variable is the probability of the event it indicates:

$$\mathbf{E[I_A] = P(A)}$$

#### Application: The Hat-Check Problem

Let $X_i$ be the indicator that man $i$ gets his own hat back, so $E[X_i] = P(\text{match}) = 1/n$. The expected number of matches $E[X]$ is:

$$E[X] = E\left[\sum_{i=1}^n X_i\right] = \sum_{i=1}^n E[X_i] = \sum_{i=1}^n \frac{1}{n} = n \cdot \frac{1}{n} = 1$$

The expected number of matches is always 1, regardless of $n$.

### 5.8 - Moment Generating Functions (MGF)

#tags: #probability #random-variables #mgf

The **Moment Generating Function (MGF)** $M(t)$ of a random variable $X$ is defined as:

$$\mathbf{M(t) = E[e^{tX}]}$$

#### Key Properties of MGFs

1. **Generating Moments**: The $n$-th derivative of the MGF, evaluated at $t=0$, gives the $n$-th moment $E[X^n]$.
    
    $$M^{(n)}(0) = E[X^n]$$
    - $E[X] = M'(0)$
        
    - $E[X^2] = M''(0)$
        
2. **Sums of Independent RVs**: If $X$ and $Y$ are independent, the MGF of their sum is the product of their MGFs:
    
    $$M_{X+Y}(t) = M_X(t) \cdot M_Y(t)$$

#### Example: MGF of a Poisson Distribution

For $X \sim \operatorname{Pois}(\lambda)$:

$$M(t) = e^{\lambda(e^t - 1)}$$

This is used to prove that the sum of two independent Poisson variables $X \sim \operatorname{Pois}(\lambda)$ and $Y \sim \operatorname{Pois}(\mu)$ is also Poisson:

$$M_{X+Y}(t) = M_X(t) \cdot M_Y(t) = e^{\lambda(e^t-1)} \cdot e^{\mu(e^t-1)} = e^{(\lambda+\mu)(e^t-1)}$$

Therefore, $X+Y \sim \operatorname{Pois}(\lambda+\mu)$.