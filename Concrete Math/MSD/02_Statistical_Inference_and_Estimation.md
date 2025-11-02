
    

# 02 - Statistical Inference, Testing, and Estimation

## Models and Foundational Theorems

### Parametric vs. Non-Parametric Models

- **Parametric Model:** A set of distributions $\mathcal{F}$ that can be characterized by a **finite** number of parameters $\theta$.
    
    - Example: Normal distribution $\mathcal{F} = \{f(x; \mu, \sigma^2) : \mu \in \mathbb{R}, \sigma^2 > 0\}$. $\theta = (\mu, \sigma^2)$.
        
- **Non-Parametric Model:** Cannot be parameterized by a finite number of parameters (e.g., $k$-nearest neighbor).
    

### Law of Large Numbers (LLN) and Central Limit Theorem (CLT)

Let $X_1, X_2, \dots, X_n$ be IID (Independent and Identically Distributed) samples with $\mu = E[X_i]$ and $\sigma^2 = \operatorname{Var}(X_i)$. Let $\bar{X}_n = \frac{1}{n} \sum_{i=1}^n X_i$.

- **Weak Law of Large Numbers (WLLN):** $\bar{X}_n \to \mu$ in probability as $n \to \infty$.
    
- **Central Limit Theorem (CLT):** The distribution of the sample mean $\bar{X}_n$ approaches a normal distribution as $n \to \infty$.
    
    $$\bar{X}_n \sim N\left(\mu, \frac{\sigma^2}{n}\right)$$

## Confidence Intervals (CI)

A CI for a parameter $\theta$ is an interval $C_n = (a, b)$ such that $P_{\theta}(\theta \in C_n) \ge 1 - \alpha$. $(1 - \alpha)$ is the coverage.

**Example: Estimating Average Meeting Hours**

- Standard Error:
    
    $$\text{SE} \approx \frac{S}{\sqrt{n}}$$
- **Confidence Interval:**
    
    $$\text{CI} = \text{Point Estimate} \pm Z^* \cdot \text{SE}$$
    
    For a 95% CI, $Z^* \approx 1.96$.
    

## Hypothesis Testing

1. **Null Hypothesis (**$H_0$**):** The default theory (e.g., $\mu=8$).
    
2. **Alternative Hypothesis (**$H_A$**):** What we test for (e.g., $\mu \neq 8$).
    
3. **Test Statistic (Z-score for large** $n$**):**
    
    $$Z = \frac{\bar{x} - \mu_0}{\text{SE}}$$
4. **P-value:** The probability of observing a test statistic value as extreme as, or more extreme than, the one actually observed, _assuming_ $H_0$ _is true_.
    

| Truth $\to$ Decision $\downarrow$ | Fail to Reject $H_0$        | Reject $H_0$                |
| --------------------------------- | --------------------------- | --------------------------- |
| $H_0$ **True**                    | Correct Decision            | **Type I Error** ($\alpha$) |
| $H_A$ **True**                    | **Type II Error** ($\beta$) | Correct Decision            |
To know more about these read [[CI, Level of Significance , Hypothesis Testing]]
## Bootstrapping (Non-Parametric Estimation)

Bootstrapping is a technique for estimating the distribution of a statistic by re-sampling the observed data _with replacement_.

**Estimate SE:**

$$\text{SE}_{\text{bootstrap}} = \sqrt{\frac{1}{B-1} \sum_{b=1}^{B} (\theta^{*b} - \bar{\theta}^{*})^2}$$

## Maximum Likelihood Estimation (MLE)

The MLE, $\hat{\Theta}_n$, is the value of the parameter $\theta$ that maximizes the **Likelihood Function** $L_n(\theta)$.

- **Likelihood Function:**
    
    $$L_n(\theta) = \prod_{i=1}^{n} f(x_i ; \theta)$$
- **Log-Likelihood Function:**
    
    $$l_n(\theta) = \ln(L_n(\theta))$$

**Example: MLE for Bernoulli** $P$

- $X_i \sim \text{Bernoulli}(P)$. The probability mass function is $f(x; P) = P^x (1-P)^{1-x}$.
    
- Let $S = \sum X_i$ be the number of successes.
    
- **Log-Likelihood:**
    
    $$l_n(P) = S \cdot \ln(P) + (n - S) \cdot \ln(1-P)$$
- **Finding MLE (**$\hat{P}$**):**
    
    $$\frac{d}{dP} [l_n(P)] = \frac{S}{P} - \frac{n - S}{1-P} = 0$$
    
    Solving for $P$ gives the MLE: $\hat{P} = S/n = \bar{X}_n$.