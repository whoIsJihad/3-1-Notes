# Concrete Mathematics: Core Concepts and Distributions

This document provides a structured overview of the fundamental topics in probability and discrete/continuous mathematics, based on the course material.

## 1. Probability Fundamentals

### Basic Definitions and Rules

- **Probability Space:** A set of all possible outcomes ($\mathcal{S}$) and a probability function ($P$).
    
- **Naive Probability:** $P(A) = \frac{\text{\# Favorable Outcomes}}{\text{\# Total Outcomes}}$ (Assumes equally likely outcomes).
    
- **Axioms:** $P(\phi) = 0$, $P(\mathcal{S}) = 1$, and **Countable Additivity** for disjoint events: $P(\bigcup A_n) = \sum P(A_n)$.
    
- **Properties:**
    
    - **Complement:** $P(A^c) = 1 - P(A)$
        
    - **Monotonicity:** If $A \subseteq B$, then $P(A) \le P(B)$
        
    - **Inclusion-Exclusion (2 Events):** $P(A \cup B) = P(A) + P(B) - P(A \cap B)$
        

### Conditional Probability and Independence

- **Definition:** $P(A|B) = \frac{P(A \cap B)}{P(B)}$, for $P(B) > 0$.
    
- **Independence:** Events $A$ and $B$ are independent if $P(A \cap B) = P(A)P(B)$.
    
- **Bayes' Rule:** $P(A|B) = \frac{P(B|A)P(A)}{P(B)}$
    
- **Law of Total Probability:** For a partition $\{A_i\}$ of $\mathcal{S}$, $P(B) = \sum P(B|A_i)P(A_i)$.
    
- **Conditional Independence:** $P(A \cap B|C) = P(A|C)P(B|C)$.
    

## 2. Counting and Combinatorics

### Fundamental Counting Principles

- **Multiplication Rule:** If there are $n_1$ outcomes for experiment 1 and $n_2$ outcomes for experiment 2, there are $n_1 \cdot n_2$ total outcomes.
    
- **Sampling Table:** Ways to choose $K$ objects from $N$:
    

|Order|Replacement|Formula|Description|
|---|---|---|---|
|Y|Y|$N^K$|Ordered sequence with repeats|
|Y|N|$\frac{N!}{(N-K)!}$|Permutation|
|N|N|$\binom{N}{K}$|Combination|
|N|Y|$\binom{N+K-1}{K}$|Stars and Bars (Indistinguishable objects in distinguishable boxes)|

### Key Identities and Proofs

- **Basic Identity:** $\binom{n}{k} = \binom{n}{n-k}$
    
- **Vandermonde's Identity (Story Proof):**
    
    $$\sum_{j=0}^{k}\binom{m}{j}\binom{n}{k-j} = \binom{m+n}{k}$$

## 3. Discrete Random Variables and Distributions

|Distribution|Story / Definition|PMF ($P(X=k)$)|Expectation ($E[X]$)|Variance ($\text{Var}[X]$)|MGF ($M(t)$)|
|---|---|---|---|---|---|
|**Bernoulli (**$p$**)**|$X=1$ for success, $0$ for failure.|$p^k q^{1-k}$|$p$|$pq$|$pe^t + q$|
|**Binomial (**$n, p$**)**|# successes in $n$ independent trials.|$\binom{n}{k}p^k q^{n-k}$|$np$|$npq$|$(pe^t + q)^n$|
|**Geometric (**$p$**)**|# failures before 1st success.|$q^k p$|$\frac{q}{p}$|$\frac{q}{p^2}$|$\frac{p}{1-qe^t}$|
|**Neg. Binomial (**$r, p$**)**|# failures before $r$-th success.|$\binom{n+r-1}{r-1}p^r q^{n}$|$\frac{rq}{p}$|$\frac{rq}{p^2}$|$\left(\frac{p}{1-qe^t}\right)^r$|
|**Poisson (**$\lambda$**)**|# of rare events (rate $\lambda$).|$\frac{e^{-\lambda} \lambda^k}{k!}$|$\lambda$|$\lambda$|$e^{\lambda(e^t - 1)}$|
|**Hypergeometric**|# of type $w$ in a sample of $n$ (no replacement).|$\frac{\binom{w}{k}\binom{b}{n-k}}{\binom{b+w}{n}}$|(Complex)|(Complex)|(N/A)|
|**Multinomial**|Counts of $k$ outcomes in $n$ trials with probabilities $\vec{P}$.|$\frac{n!}{n_1! \ldots n_k!} p_1^{n_1} \ldots p_k^{n_k}$|$E[X_j] = np_j$|$\text{Var}[X_j] = np_j q_j$|(Complex)|

### Key Discrete Concepts

- **Indicator R.V. (**$I_A$**):** $E[I_A] = P(A)$. Critical for finding expected values by linearity.
    
- **Poisson Approximation:** For Binomial with large $n$ and small $p$, $\text{Bin}(n, p) \approx \text{Pois}(\lambda)$ where $\lambda = np$.
    
- **Sum of Poissons:** If $X \sim \text{Pois}(\lambda)$ and $Y \sim \text{Pois}(\mu)$ are independent, $X+Y \sim \text{Pois}(\lambda+\mu)$.
    

## 4. Continuous Random Variables and Distributions

### General Continuous Concepts

- **PDF (**$f(x)$**):** Probability Density Function. $P(a \le X \le b) = \int_a^b f(x)dx$.
    
- **CDF (**$F(x)$**):** $F(x) = \int_{-\infty}^x f(t)dt$. $f(x) = F'(x)$.
    
- **LOTUS (Expectation):** $E[g(X)] = \int_{-\infty}^\infty g(x)f(x)dx$.
    

|Distribution|Domain|PDF ($f(x)$)|CDF ($F(x)$)|Expectation ($E[X]$)|Variance ($\text{Var}[X]$)|
|---|---|---|---|---|---|
|**Uniform (**$a, b$**)**|$[a, b]$|$\frac{1}{b-a}$|$\frac{x-a}{b-a}$|$\frac{a+b}{2}$|$\frac{(b-a)^2}{12}$|
|**Exponential (**$\lambda$**)**|$x > 0$|$\lambda e^{-\lambda x}$|$1 - e^{-\lambda x}$|$\frac{1}{\lambda}$|$\frac{1}{\lambda^2}$|
|**Standard Normal**|$(-\infty, \infty)$|$\frac{1}{\sqrt{2\pi}} e^{-z^2/2}$|$\Phi(z)$|$0$|$1$|
|**Normal (**$\mu, \sigma^2$**)**|$(-\infty, \infty)$|$\frac{1}{\sigma}f_Z\left(\frac{x-\mu}{\sigma}\right)$|$\Phi\left(\frac{x-\mu}{\sigma}\right)$|$\mu$|$\sigma^2$|

### Key Continuous Concepts

- **Memoryless Property (Exponential):** $P(X \ge s+t | X \ge s) = P(X \ge t)$. The remaining waiting time is independent of how long you've already waited.
    
- **Standardization (Normal):** If $X \sim N(\mu, \sigma^2)$, then $Z = \frac{X-\mu}{\sigma} \sim N(0, 1)$.
    
- **Sum of Normals:** If $X \sim N(\mu_1, \sigma_1^2)$ and $Y \sim N(\mu_2, \sigma_2^2)$ are independent, then $X+Y \sim N(\mu_1+\mu_2, \sigma_1^2+\sigma_2^2)$.
    

## 5. Joint Distributions

- **Marginals (Continuous):** $f_X(x) = \int_{-\infty}^{\infty} f_{X,Y}(x, y)dy$.
    
- **Independence (Continuous):** $X$ and $Y$ are independent if $f_{X,Y}(x, y) = f_X(x)f_Y(y)$.
    
- **Conditional PDF:** $f_{Y|X}(y|x) = \frac{f_{X,Y}(x, y)}{f_X(x)}$.
    
- **MGF Property:** If $X$ and $Y$ are independent, $M_{X+Y}(t) = M_X(t)M_Y(t)$.
    
- **Variance of Sum:** $Var(X+Y) = Var(X) + Var(Y)$ (only if $X, Y$ are independent).