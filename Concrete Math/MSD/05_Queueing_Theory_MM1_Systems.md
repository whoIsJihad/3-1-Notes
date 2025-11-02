
# 05 - Queueing Theory (M/M/1, Little's Law)

## Queueing Metrics

|Metric|Symbol|
|---|---|
|**Average Customers in System**|$L$|
|**Average Customers in Queue**|$L_Q$|
|**Average Time in System**|$W$|
|**Average Time in Queue**|$W_Q$|
|**Traffic Intensity**|$\rho = \lambda / \mu$|

## Little's Formula (Basic Cost Identity)

Little's Formula holds for almost any queueing system in steady state:

- **System:** $L = \lambda_a W$
    
- **Queue:** $L_Q = \lambda_a W_Q$ Where $\lambda_a$ is the **actual arrival rate** into the system.
    

## M/M/1 Queue (Infinite Capacity)

A single-server queue with Poisson arrivals ($\lambda$) and Exponential service times ($\mu$). Stable if $\rho = \lambda/\mu < 1$.

### Steady-State Probabilities ($P_n$)

The probability of having $n$ customers in the system:

$$P_n = (1 - \rho) \rho^n \quad (\text{for } n \ge 0)$$

### Performance Measures

|Metric|Formula|
|---|---|
|**Average Customers in System (**$L$**)**|$$L = \frac{\lambda}{\mu - \lambda} = \frac{\rho}{1 - \rho}$$|
|**Average Time in System (**$W$**)**|$$W = \frac{1}{\mu - \lambda} = \frac{1}{\mu (1 - \rho)}$$|

## M/M/1 Queue (Finite Capacity $N$)

The system can hold at most $N$ customers.

### Steady-State Probabilities ($P_n$)

For $\rho = \lambda/\mu \ne 1$:

$$P_0 = \frac{1 - \rho}{1 - \rho^{N+1}}$$$$P_n = \rho^n P_0 \quad (\text{for } 0 \le n \le N)$$

### Performance Measures

The **Actual Arrival Rate** must account for lost customers ($P_N$ is the probability the system is full):

$$\lambda_a = \lambda (1 - P_N)$$$$W = \frac{L}{\lambda_a}$$

## Bulk Service Queue

A server that can handle multiple customers (e.g., 2) at once. The stationary probabilities $P_n$ often follow a geometric form $P_n = \alpha^n P_0$ for $n \ge 1$.

The value of $\alpha$ is found as the root ($\alpha < 1$) of a characteristic equation derived from the balance equations. For a bulk-service-of-2 system:

$$\mu \alpha^3 - (\lambda + \mu) \alpha + \lambda = 0$$

The stability condition is $\lambda < 2\mu$.