# Moment Generating Functions (MGFs)

## 1. What is a Moment Generating Function?

The Moment Generating Function (MGF) is a mathematical tool used to simplify the calculation of the moments of a random variable (RV). For a random variable $X$, its MGF, denoted $M_X(t)$, is defined as the expected value of $e^{tX}$, where $t$ is a real-valued variable.

### Formal Definition

For a random variable $X$:

$$M_X(t) = E[e^{tX}]$$

- If $X$ is **discrete** (with PMF $P(X=x)$):
    
    $$M_X(t) = \sum_{x} e^{tx} P(X=x)$$
- If $X$ is **continuous** (with PDF $f(x)$):
    
    $$M_X(t) = \int_{-\infty}^{\infty} e^{tx} f(x) dx$$

The MGF only exists if this expected value is finite for $t$ in some open interval around $t=0$ (i.e., $|t| < h$ for some $h>0$).

## 2. The Core Intuition: The Power of Taylor Series

The magic of the MGF lies in its connection to the Taylor series expansion of $e^{tX}$ around $t=0$:

$$e^{tX} = 1 + (tX) + \frac{(tX)^2}{2!} + \frac{(tX)^3}{3!} + \dots + \frac{(tX)^k}{k!} + \dots$$

Now, if we take the expected value of both sides (since $E$ is a linear operator):

$$E[e^{tX}] = E\Big[1 + tX + \frac{t^2 X^2}{2!} + \frac{t^3 X^3}{3!} + \dots\Big]$$$$M_X(t) = E[1] + t E[X] + \frac{t^2}{2!} E[X^2] + \frac{t^3}{3!} E[X^3] + \dots + \frac{t^k}{k!} E[X^k] + \dots$$

Notice the coefficients of $t^k/k!$ are exactly the moments $E[X^k]$.

### Extracting Moments

The $k$-th moment of $X$ is found by taking the $k$-th derivative of the MGF with respect to $t$ and then setting $t=0$:

$$\frac{d^k}{dt^k} M_X(t) \Big|_{t=0} = E[X^k]$$

**Specifically:**

1. **Mean (**$E[X]$**):**
    
    $$E[X] = M'_X(0) = \frac{d}{dt} M_X(t) \Big|_{t=0}$$
2. **Second Moment (**$E[X^2]$**):**
    
    $$E[X^2] = M''_X(0) = \frac{d^2}{dt^2} M_X(t) \Big|_{t=0}$$
3. **Variance (**$\operatorname{Var}(X)$**):**
    
    $$\operatorname{Var}(X) = E[X^2] - (E[X])^2 = M''_X(0) - (M'_X(0))^2$$

## 3. Example 1: Bernoulli Distribution

Let $X$ be a Bernoulli random variable, $X \sim \text{Bernoulli}(p)$, where $P(X=1) = p$ and $P(X=0) = 1-p$.

### A. Deriving $M_X(t)$

Using the discrete MGF definition:

$$M_X(t) = \sum_{x=0}^{1} e^{tx} P(X=x)$$$$M_X(t) = e^{t(0)} P(X=0) + e^{t(1)} P(X=1)$$$$M_X(t) = 1 \cdot (1-p) + e^t \cdot p$$$$\mathbf{M_X(t) = (1-p) + p e^t}$$

### B. Finding Moments

1. **First Derivative (for** $E[X]$**):**
    
    $$M'_X(t) = \frac{d}{dt} [(1-p) + p e^t] = p e^t$$$$E[X] = M'_X(0) = p e^0 = p \cdot 1 = \mathbf{p}.$$
2. **Second Derivative (for** $E[X^2]$**):**
    
    $$M''_X(t) = \frac{d}{dt} [p e^t] = p e^t$$$$E[X^2] = M''_X(0) = p e^0 = \mathbf{p}.$$
3. **Variance (**$\operatorname{Var}(X)$**):**
    
    $$\operatorname{Var}(X) = E[X^2] - (E[X])^2$$$$\operatorname{Var}(X) = p - p^2 = \mathbf{p(1-p)}.$$

The MGF makes calculating these familiar results extremely fast!

## 4. Example 2: Normal Distribution

Let $X \sim \mathcal{N}(\mu, \sigma^2)$. The derivation for the MGF is quite involved (using the technique similar to the one in your Canvas), so we'll state the result and demonstrate its use.

### A. The MGF of $X \sim \mathcal{N}(\mu, \sigma^2)$

$$\mathbf{M_X(t) = \exp\Big(\mu t + \frac{1}{2}\sigma^2 t^2\Big)}$$

### B. Finding Moments

1. **First Derivative (for** $E[X]$**):** We use the Chain Rule, letting $g(t) = \mu t + \frac{1}{2}\sigma^2 t^2$. Then $M_X(t) = e^{g(t)}$.
    
    $$M'_X(t) = e^{g(t)} \cdot g'(t)$$$$M'_X(t) = \exp\Big(\mu t + \frac{1}{2}\sigma^2 t^2\Big) \cdot (\mu + \sigma^2 t)$$
    
    Now, set $t=0$:
    
    $$E[X] = M'_X(0) = \exp(0) \cdot (\mu + 0) = 1 \cdot \mu = \mathbf{\mu}.$$
2. **Second Derivative (for** $E[X^2]$**):** We use the Product Rule on $M'_X(t) = \underbrace{\exp(g(t))}_{\text{Function 1}} \cdot \underbrace{(\mu + \sigma^2 t)}_{\text{Function 2}}$:
    
    $$M''_X(t) = \frac{d}{dt} (\text{Func 1}) \cdot (\text{Func 2}) + (\text{Func 1}) \cdot \frac{d}{dt} (\text{Func 2})$$$$M''_X(t) = \Big(M'_X(t)\Big) \cdot (\mu + \sigma^2 t) + M_X(t) \cdot (\sigma^2)$$
    
    Now, set $t=0$. Recall $M_X(0)=1$ and $M'_X(0)=\mu$.
    
    $$E[X^2] = M''_X(0) = \Big(M'_X(0)\Big) \cdot (\mu + 0) + M_X(0) \cdot (\sigma^2)$$$$E[X^2] = (\mu) \cdot (\mu) + (1) \cdot (\sigma^2) = \mathbf{\mu^2 + \sigma^2}.$$
3. **Variance (**$\operatorname{Var}(X)$**):**
    
    $$\operatorname{Var}(X) = E[X^2] - (E[X])^2$$$$\operatorname{Var}(X) = (\mu^2 + \sigma^2) - (\mu)^2 = \mathbf{\sigma^2}.$$

This confirms the familiar mean and variance of the Normal distribution much faster than direct integration!

## 5. Most Powerful Property: Sums of Independent RVs

The most revolutionary use of the MGF is how it handles the sum of independent random variables.

Let $X_1, X_2, \dots, X_n$ be **independent** random variables, and let $Y = X_1 + X_2 + \dots + X_n$.

The MGF of the sum $Y$ is the **product** of the MGFs of the individual components:

$$\mathbf{M_Y(t) = M_{X_1}(t) \cdot M_{X_2}(t) \cdot \dots \cdot M_{X_n}(t)}$$

This is incredibly useful because multiplying is easier than convolution (the traditional way to find the distribution of a sum).

### Example: Sum of Normals

Let $X_1 \sim \mathcal{N}(\mu_1, \sigma_1^2)$ and $X_2 \sim \mathcal{N}(\mu_2, \sigma_2^2)$ be independent. Let $Y = X_1 + X_2$.

1. **MGF of Y:**
    
    $$M_Y(t) = M_{X_1}(t) \cdot M_{X_2}(t)$$$$M_Y(t) = \exp\Big(\mu_1 t + \frac{1}{2}\sigma_1^2 t^2\Big) \cdot \exp\Big(\mu_2 t + \frac{1}{2}\sigma_2^2 t^2\Big)$$$$M_Y(t) = \exp\Big(\mu_1 t + \mu_2 t + \frac{1}{2}\sigma_1^2 t^2 + \frac{1}{2}\sigma_2^2 t^2\Big)$$$$M_Y(t) = \exp\Big((\mu_1 + \mu_2) t + \frac{1}{2}(\sigma_1^2 + \sigma_2^2) t^2\Big)$$
2. **Identifying the Distribution:** The resulting MGF, $M_Y(t)$, has the exact functional form of a Normal distribution MGF: $\exp(\mu' t + \frac{1}{2}(\sigma')^2 t^2)$.
    
    By comparison, we conclude that $Y$ is also Normally distributed:
    
    $$\mathbf{Y \sim \mathcal{N}(\mu_1 + \mu_2, \sigma_1^2 + \sigma_2^2)}$$

This property is what makes MGFs a foundational tool for proving key theorems like the Central Limit Theorem. 