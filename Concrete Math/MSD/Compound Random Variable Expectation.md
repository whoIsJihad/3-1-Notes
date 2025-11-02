# Expectation of a Compound Random Variable

Tags:  #probability  #expectation  #WaldsIdentity

This note derives the formula for the expected value of a sum of a random number of random variables.

Let $N$ be a random variable representing a count (e.g., number of events). Let $X_1, X_2, \dots$ be a sequence of i.i.d. (independent and identically distributed) random variables, which are also independent of $N$. Let $E[X]$ be the common expectation for all $X_i$.

We want to find the expectation of the total sum $T = \sum_{i=1}^{N} X_i$. This is also known as a **compound random variable**.

## Derivation (Wald's Identity)

We use the Law of Total Expectation (also called "conditioning on $N$"):

$$E[T] = E\left[\sum_{i=1}^{N} X_i\right] = E\left[ E\left[ \sum_{i=1}^{N} X_i \bigg| N \right] \right]$$

First, let's solve the inner expectation by treating $N$ as a constant $n$:

$$E\left[ \sum_{i=1}^{N} X_i \bigg| N=n \right] = E\left[ \sum_{i=1}^{n} X_i \bigg| N=n \right]$$

Because the $X_i$ are independent of $N$, this simplifies to:

$$E\left[ \sum_{i=1}^{n} X_i \right] = \sum_{i=1}^{n} E[X_i] = n E[X]$$

This means the conditional expectation is a new random variable:

$$E[T | N] = N E[X]$$

Now, substitute this back into the outer expectation:

$$E[T] = E[ N E[X] ]$$

Since $E[X]$ is a constant, we can pull it out:

$$E\left[\sum_{i=1}^{N} X_i\right] = E[N] E[X]$$

## Example from Lecture [cite: PDF Page 1]

- **Problem:** $N$ is the number of car accidents in a week. $X_i$ is the number of injuries in the $i$-th accident. What is the expected total number of injuries per week?
    
- **Solution:**
    
    - Total Injuries $T = \sum_{i=1}^{N} X_i$.
        
    - Using the derived formula, $E[T] = E[N] E[X]$.
        
    - (e.g., If the expected number of accidents is $E[N]=3$ and the expected number of injuries per accident is $E[X]=1.5$, the expected total injuries are $E[T] = 3 \times 1.5 = 4.5$).
        

## Additional Solved Problem (External)

- **Problem:** A popular fast-food restaurant finds that the number of customers $N$ arriving in a given hour is a Poisson random variable with a mean $\lambda = 20$. Each customer $i$ independently orders a quantity $X_i$ of "Super Burgers," where $X_i$ follows a geometric distribution with a success probability $p = 0.5$ (i.e., $P(X_i=k) = (0.5)^k$ for $k=1, 2, \dots$). What is the expected total number of Super Burgers sold in that hour?
    
- **Solution:**
    
    1. **Identify the variables:**
        
        - $N \sim \text{Poisson}(\lambda=20)$. The number of customers.
            
        - $X_i \sim \text{Geometric}(p=0.5)$. The number of burgers for customer $i$.
            
        - We need $T = \sum_{i=1}^{N} X_i$.
            
    2. **Find the expectations** $E[N]$ **and** $E[X]$**:**
        
        - The expectation of a Poisson($\lambda$) variable is $E[N] = \lambda$. So, $E[N] = 20$.
            
        - The expectation of a geometric($p$) variable (starting from $k=1$) is $E[X] = 1/p$. So, $E[X] = 1 / 0.5 = 2$.
            
    3. **Apply Wald's Identity:**
        
        - $E[T] = E[N] E[X]$
            
        - $E[T] = 20 \times 2 = 40$.
            
    
    - **Answer:** The expected total number of Super Burgers sold is 40.