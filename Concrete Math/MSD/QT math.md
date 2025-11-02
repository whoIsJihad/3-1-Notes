# Part 3: Solved Example (The M/M/1 Queue)

This file combines the theory from Part 1 with the application from Part 2 to solve the most common queueing model.

## 1. What is the M/M/1 Model?

This is the simplest, most fundamental queueing model. The name is a code (Kendall-Lee notation):

- **M / M / 1**: The first **"M"** stands for **"Memoryless"**. This means arrivals are a **Poisson Process**, so inter-arrival times are exponential.
    
- **M / M / 1**: The second **"M"** also stands for **"Memoryless"**. This means **service times are exponential**.
    
- **M / M / 1**: The **"1"** means there is a **single server**.
    

## 2. M/M/1 as a Birth-Death Process

This is the key connection! An M/M/1 queue is just a _specific case_ of the general Birth-Death process from Part 1.

- **"Birth" = Customer Arrival.** The arrival rate is Poisson with a _constant_ rate $\lambda$. It doesn't matter how many people are already in the queue.
    
    - $\lambda_n = \lambda$ **for all** $n \ge 0$
        
- **"Death" = Customer Departure.** The service rate is exponential with a _constant_ rate $\mu$. The server works at this rate as long as _someone is there_ ($n \ge 1$).
    
    - $\mu_n = \mu$ **for all** $n \ge 1$
        

## 3. Solving the M/M/1 Queue (Finding $P_n$)

We now plug _these specific rates_ into our _general formulas_ from Part 1.

#### Step 1: Use the General Product-Form Solution

The general formula was: $P_n = P_0 \times \frac{\lambda_{n-1} \lambda_{n-2} \dots \lambda_0}{\mu_n \mu_{n-1} \dots \mu_1}$

Let's plug in $\lambda_n = \lambda$ and $\mu_n = \mu$:

$$P_n = P_0 \times \frac{\overbrace{\lambda \cdot \lambda \dots \lambda}^{n \text{ times}}}{\underbrace{\mu \cdot \mu \dots \mu}_{n \text{ times}}}$$$$P_n = P_0 \left(\frac{\lambda}{\mu}\right)^n$$

#### Step 2: Define Traffic Intensity ($\rho$)

We define a new variable, $\rho$ **(rho)**, called **traffic intensity** or **utilization**.

$$\rho = \frac{\lambda}{\mu}$$

So our solution becomes: $P_n = P_0 \rho^n$

#### Step 3: Find $P_0$ (Normalization)

All probabilities must sum to 1:

$$\sum_{n=0}^{\infty} P_n = \sum_{n=0}^{\infty} P_0 \rho^n = P_0 \sum_{n=0}^{\infty} \rho^n = 1$$

This is a **geometric series**.

- **Stability Condition:** This series _only_ converges if $\rho < 1$ (meaning $\lambda < \mu$). Your arrival rate _must_ be less than your service rate, or the queue will grow to infinity.
    
- **The Sum:** The formula for this sum is $\frac{1}{1-\rho}$.
    
- **Solve for** $P_0$**:**
    
    $$P_0 \left( \frac{1}{1-\rho} \right) = 1 \implies P_0 = 1 - \rho$$
    
    This is the probability the system is empty!
    

#### Step 4: The Final Solution for $P_n$

Substitute $P_0$ back into our equation:

$$P_n = (1-\rho) \rho^n$$

## 4. Finding the M/M/1 Metrics ($L, W, L_Q, W_Q$)

Now we can find all our key metrics.

1. **Find** $L$ **(Average number in system):** $L$ is the expected value, $L = \sum_{n=0}^{\infty} n P_n$. $L = \sum_{n=0}^{\infty} n (1-\rho)\rho^n = (1-\rho) \sum_{n=0}^{\infty} n \rho^n$ Using the standard series formula $\sum n x^n = \frac{x}{(1-x)^2}$: $L = (1-\rho) \left[ \frac{\rho}{(1-\rho)^2} \right] = \frac{\rho}{1-\rho}$
    
    - $L = \frac{\rho}{1-\rho} = \frac{\lambda}{\mu - \lambda}$
        
2. **Find** $W$ **(Average time in system):** We use Little's Law (from Part 2): $L = \lambda W$. $W = \frac{L}{\lambda} = \frac{\lambda / (\mu - \lambda)}{\lambda}$
    
    - $W = \frac{1}{\mu - \lambda}$
        
3. **Find** $W_Q$ **(Average time in queue):** Total time in system ($W$) is just waiting time ($W_Q$) + service time ($E[S]$).
    
    - $W = W_Q + E[S]$
        
    - Since service is exponential with rate $\mu$, the average service time $E[S] = 1/\mu$.
        
    - $W_Q = W - E[S] = \frac{1}{\mu - \lambda} - \frac{1}{\mu}$
        
    - Finding a common denominator: $W_Q = \frac{\mu - (\mu - \lambda)}{\mu(\mu - \lambda)}$
        
    - $W_Q = \frac{\lambda}{\mu(\mu - \lambda)}$
        
4. **Find** $L_Q$ **(Average number in queue):** We use Little's Law again: $L_Q = \lambda W_Q$.
    
    - $L_Q = \lambda \left( \frac{\lambda}{\mu(\mu - \lambda)} \right) = \frac{\lambda^2}{\mu(\mu - \lambda)}$
        

_PS: That "Job Shop" example from your first set of notes is just another Birth-Death process, but with different rates:_ $\lambda_n = (M-n)\lambda$ _and_ $\mu_n = \mu$_. We would solve it using the same general formulas from Part 1._