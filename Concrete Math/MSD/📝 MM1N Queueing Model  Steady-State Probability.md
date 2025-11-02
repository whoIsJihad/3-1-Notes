
The **M/M/1/N** model is a single-server system with a finite maximum capacity, $N$. If a customer arrives when the system already has $N$ customers, they are **blocked** (lost from the system) and do not join the queue.

## 1. Defining the System Parameters

The system behaves exactly like a standard M/M/1 model, except for the boundary at $N$:

|Parameter|Value|Description|
|---|---|---|
|**Arrival Rate (**$\lambda_n$**)**|$\lambda$ for $n < N$|The arrival rate is constant as long as there is capacity.|
|**Arrival Rate (**$\lambda_N$**)**|$0$ for $n = N$|Arrivals are blocked when the system is full.|
|**Service Rate (**$\mu_n$**)**|$\mu$ for $n \ge 1$|The service rate is constant.|
|**State Space**|$n = 0, 1, \dots, N$|The maximum number of customers in the system is $N$.|

## 2. Setting up the Global Balance Equations

For any Birth–Death process (which M/M/1/N is), the rate of flow _into_ a state must equal the rate of flow _out_ of that state. We find the limiting probability $P_n$ (the probability of having $n$ customers in the system).

### Case 1: State $n=0$ (Empty System)

Rate Out of $0$ = Rate Into $0$

$$\lambda P_0 = \mu P_1$$

This equation means: The rate of an arrival ($\lambda$) when the system is empty ($P_0$) must equal the rate of a service completion ($\mu$) that leaves the system empty ($P_1$).

### Case 2: States $1 \le n \le N-1$ (Normal Operation)

Rate Out of $n$ = Rate Into $n$

$$(\lambda + \mu) P_n = \lambda P_{n-1} + \mu P_{n+1}$$

This is the general balance equation:

- **Rate Out:** $\lambda$ (for an arrival) $+\mu$ (for a departure)
    
- **Rate Into:** An arrival from state $n-1$ ($\lambda P_{n-1}$) + A departure from state $n+1$ ($\mu P_{n+1}$)
    

### Case 3: State $n=N$ (Full Capacity)

Rate Out of $N$ = Rate Into $N$

$$\mu P_N = \lambda P_{N-1}$$

- **Rate Out:** Only a departure ($\mu$) can happen from state $N$.
    
- **Rate Into:** Only an arrival ($\lambda$) from state $N-1$ can reach state $N$. (Since $\lambda_N = 0$, no one leaves $N$ for $N+1$).
    

## 3. Solving for $P_n$

We use the general balance equation recursively, starting from $P_1$.

From $n=0$:

$$P_1 = \frac{\lambda}{\mu} P_0 = \rho P_0$$

where $\rho = \frac{\lambda}{\mu}$ is the traffic intensity.

For $n=1$: Substitute $P_1 = \rho P_0$ into the general equation:

$$(\lambda + \mu) P_1 = \lambda P_0 + \mu P_2$$$$\mu P_2 = (\lambda + \mu) (\rho P_0) - \lambda P_0$$$$\mu P_2 = (\lambda\rho P_0 + \mu\rho P_0) - \lambda P_0$$

Since $\lambda = \rho\mu$:

$$\mu P_2 = (\rho(\rho\mu) P_0 + \mu\rho P_0) - \rho\mu P_0$$$$\mu P_2 = \mu\rho^2 P_0 + \mu\rho P_0 - \mu\rho P_0$$$$\mu P_2 = \mu\rho^2 P_0 \quad \Rightarrow \quad P_2 = \rho^2 P_0$$

By induction, we find that for any state $n$ up to $N$:

$$\boxed{P_n = \rho^n P_0, \quad \text{for } 0 \le n \le N}$$

## 4. Normalizing to Find $P_0$

The sum of all probabilities must equal $1$:

$$\sum_{n=0}^{N} P_n = 1$$$$\sum_{n=0}^{N} \rho^n P_0 = 1$$$$P_0 \sum_{n=0}^{N} \rho^n = 1$$

This is a geometric series with $N+1$ terms.

### Case A: When $\rho \ne 1$ ($\lambda \ne \mu$)

The sum of a finite geometric series is $\sum_{n=0}^{N} x^n = \frac{1 - x^{N+1}}{1 - x}$.

$$P_0 \left( \frac{1 - \rho^{N+1}}{1 - \rho} \right) = 1$$$$\boxed{P_0 = \frac{1 - \rho}{1 - \rho^{N+1}}}$$

Substituting $P_0$ back gives the final formula for $P_n$:

$$P_n = \rho^n \left( \frac{1 - \rho}{1 - \rho^{N+1}} \right), \quad \text{for } 0 \le n \le N$$

### Case B: When $\rho = 1$ ($\lambda = \mu$)

If $\rho = 1$, the terms of the summation are all $1$.

$$P_0 \sum_{n=0}^{N} 1^n = P_0 (N+1) = 1$$$$P_n = P_0 = \frac{1}{N+1}, \quad \text{for } 0 \le n \le N$$

In this case, the probability of being in any state is equally likely.