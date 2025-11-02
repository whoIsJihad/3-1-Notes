

# 04 - Continuous Time Processes (Poisson, Birth-Death)

## Poisson Process

A counting process $\{N(t), t \ge 0\}$ with rate $\lambda > 0$ where the number of events $N(t)$ in any interval of length $t$ is Poisson distributed.

- **Poisson Distribution:**
    
    $$P\{ N(t+s) - N(s) = n \} = e^{-\lambda t} \frac{(\lambda t)^n}{n!}$$
    
    The expectation is $E[N(t)] = \lambda t$.
    

### Distribution of Inter-Arrival Times ($T_i$)

The inter-arrival time follows an **Exponential Distribution** with mean $1/\lambda$.

$$P\{ T_i > t \} = P\{ N(t) = 0 \} = e^{-\lambda t}$$

**Probability Comparison of Exponential RVs:** If $X_1 \sim \text{Exp}(\lambda_1)$ and $X_2 \sim \text{Exp}(\lambda_2)$ are independent:

$$P\{ X_1 < X_2 \} = \frac{\lambda_1}{\lambda_1 + \lambda_2}$$

## Birth and Death Model (B&D)

A continuous-time Markov chain with birth rate $\lambda_n$ (for $n \to n+1$) and death rate $\mu_n$ (for $n \to n-1$).

The transition probabilities $P_{i, j}$ for the embedded discrete-time chain are:

$$P_{n, n+1} = \frac{\lambda_n}{\lambda_n + \mu_n}$$$$P_{n, n-1} = \frac{\mu_n}{\lambda_n + \mu_n} \quad (\text{for } n > 0)$$

## Kolmogorov's Equations

The equations for the rate of change of transition probabilities $P_{ij}(t)$, where $q_{ij} = v_i P_{ij}$ is the total rate of transition from $i$ to $j$ and $v_i = \sum_j q_{ij}$ is the total rate of leaving state $i$.

- **Forward Equation (Source** $i$ **fixed):**
    
    $$P_{ij}'(t) = \sum_{k \neq j} P_{ik}(t) q_{kj} - v_j P_{ij}(t)$$

## Limiting Probabilities (Stationary Distribution)

For a B&D process, the stationary distribution $P_n$ is found by setting **Rate In = Rate Out** for each state, which yields the recursive relation:

$$\lambda_n P_n = \mu_{n+1} P_{n+1}$$

The general solution for $P_n$ is:

$$P_n = P_0 \cdot \prod_{i=0}^{n-1} \frac{\lambda_i}{\mu_{i+1}} \quad (\text{for } n \ge 1)$$

Where the normalization condition $\sum_{n=0}^{\infty} P_n = 1$ gives $P_0$:

$$\frac{1}{P_0} = 1 + \sum_{n=1}^{\infty} \left( \prod_{i=0}^{n-1} \frac{\lambda_i}{\mu_{i+1}} \right)$$

**Example: Job Shop** $P_n$ For $M$ machines, 1 serviceman, $\lambda_n = (M-n)\lambda$ and $\mu_n = \mu$, the solution simplifies to:

$$P_n = P_0 \cdot \left(\frac{\lambda}{\mu}\right)^n \frac{M!}{(M-n)!}$$