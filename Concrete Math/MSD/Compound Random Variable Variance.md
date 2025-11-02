# Variance of a Compound Random Variable

Tags: #probability #variance #conditioning

This note derives the formula for the variance of a sum of a random number of random variables, $T = \sum_{i=1}^{N} X_i$. This is a direct application of the **Law of Total Variance** (also known as Eve's Law):

$$Var(T) = E[Var(T | N)] + Var(E[T | N])$$

We assume $N$ and all $X_i$ are independent, and the $X_i$ are i.i.d. with mean $E[X]$ and variance $Var(X)$.

## Derivation

From [[Compound Random Variable Expectation]], we know $E[T | N] = N E[X]$.

Let's calculate the two components of the Law of Total Variance.

**Component 1:** $Var(E[T | N])$

$$Var(E[T | N]) = Var(N E[X])$$

Since $E[X]$ is a constant, $Var(c \cdot Y) = c^2 Var(Y)$.

$$Var(E[T | N]) = (E[X])^2 Var(N)$$

**Component 2:** $E[Var(T | N)]$ First, we find the inner term, $Var(T | N=n)$:

$$Var(T | N=n) = Var\left(\sum_{i=1}^{n} X_i \bigg| N=n\right) = Var\left(\sum_{i=1}^{n} X_i\right)$$

Because the $X_i$ are i.i.d., the variance of their sum is the sum of their variances:

$$Var\left(\sum_{i=1}^{n} X_i\right) = \sum_{i=1}^{n} Var(X_i) = n Var(X)$$

Therefore, the conditional variance is $Var(T | N) = N Var(X)$.

Now, we take the expectation of this result:

$$E[Var(T | N)] = E[N Var(X)] = E[N] Var(X)$$

**Putting It Together**

$$Var(T) = E[Var(T | N)] + Var(E[T | N])$$$$Var\left(\sum_{i=1}^{N} X_i\right) = E[N] Var(X) + (E[X])^2 Var(N)$$

_(Note: The PDF [cite: PDF Page 2] uses an alternative derivation by first computing_ $E[T^2]$ _but arrives at the same correct result.)_

## Additional Solved Problem (External)

- **Problem:** Using the same setup from the problem in [[Compound Random Variable Expectation]]:
    
    - Number of customers $N \sim \text{Poisson}(\lambda=20)$.
        
    - Burgers per customer $X_i \sim \text{Geometric}(p=0.5)$.
        
    - Find the **variance** of the total number of Super Burgers $T = \sum_{i=1}^{N} X_i$ sold in that hour.
        
- **Solution:**
    
    1. **Identify the four required values:** $E[N]$, $Var(N)$, $E[X]$, and $Var(X)$.
        
    2. **Find** $N$ **statistics:** $N \sim \text{Poisson}(\lambda=20)$.
        
        - $E[N] = \lambda = 20$.
            
        - A key property of the Poisson distribution is $Var(N) = \lambda$. So, $Var(N) = 20$.
            
    3. **Find** $X$ **statistics:** $X_i \sim \text{Geometric}(p=0.5)$.
        
        - $E[X] = 1/p = 1 / 0.5 = 2$.
            
        - The variance of a geometric($p$) distribution (starting from $k=1$) is $Var(X) = (1-p) / p^2$.
            
        - $Var(X) = (1 - 0.5) / (0.5)^2 = 0.5 / 0.25 = 2$.
            
    4. **Apply the formula for** $Var(T)$**:**
        
        - $Var(T) = E[N] Var(X) + (E[X])^2 Var(N)$
            
        - $Var(T) = (20 \times 2) + (2^2 \times 20)$
            
        - $Var(T) = 40 + (4 \times 20)$
            
        - $Var(T) = 40 + 80 = 120$.
            
    
    - **Answer:** The variance of the total burgers sold is 120.