# 📚 Detailed Analysis: The M/M/1/2 Bulk Service Queue (The "Bulk QS")

This model analyzes a system where customers arrive individually ($\lambda$), but the single server ($\mu$) processes and releases them in a **batch of two** ($k=2$). This is common in modeling resources like batch processors or automated systems that fill up before emptying.

## 1. System Dynamics and Transitions

The key distinction of the Bulk QS is that a service completion causes the system state to jump backward by two steps ($n \to n-2$).

### A. State-Dependent Flow Rates

|State ($n$)|Physical Status|Service Completion Transition|Service Rate ($\mu_n$)|
|---|---|---|---|
|$n \ge 2$|Two or more customers are present.|$n \to n-2$ (Bulk Departure)|$\mu$|
|$n=1$|Only one customer is present.|$1 \to 0$ (Single Departure)|$\mu$|
|$n=0$|System is empty.|N/A|0|

### B. The General Balance Equation

The steady-state probability $P_n$ must satisfy the principle that the flow of probability out of state $n$ equals the flow in. For the general state $\mathbf{n \ge 2}$:

$$\underbrace{(\lambda + \mu) P_{n}}_{\text{Rate OUT: Arrival + Bulk Service}} = \underbrace{\lambda P_{n-1}}_{\text{Flow IN from } n-1} + \underbrace{\mu P_{n+2}}_{\text{Flow IN from } n+2}$$

- The term $\mu P_{n+2}$ is the signature of bulk service: a flow into state $n$ occurs when the system completes service from a state with two more customers.
    

## 2. Derivation of the Characteristic Equation

We assume the solution follows the geometric form $\mathbf{P_{n} = \alpha^n P_{0}}$ and substitute this into the general balance equation.

### A. The Cubic Equation

Substituting and simplifying leads to the characteristic equation (which defines the possible values of the probability factor $\alpha$):

$$\mu \alpha^{3} - (\lambda + \mu) \alpha + \lambda = 0$$

### B. Factorization and Roots

The cubic equation is factored by noting that $\alpha = 1$ is always a root (since the row sum of the rate matrix is zero, setting $\lambda = (\lambda+\mu)\alpha - \mu\alpha^3$ must be true for the steady state):

$$\mathbf{(\alpha - 1)(\mu \alpha^2 + \mu \alpha - \lambda) = 0}$$

The roots are $\alpha = 1$ and the two roots of the quadratic equation. The valid root, which determines the system's behavior, is found using the quadratic formula and selecting the positive root:

$$\boxed{\alpha = \frac{-1 + \sqrt{1 + 4\lambda/\mu}}{2}}$$

## 3. The Critical Stability Condition

For the system to converge to a steady state ($\sum P_n = 1$), the factor $\alpha$ **must be less than 1** ($\alpha < 1$).

$$\frac{-1 + \sqrt{1 + 4\lambda/\mu}}{2} < 1$$

Solving this inequality yields the stability requirement:

$$\mathbf{\lambda < 2\mu}$$

- **Physical Interpretation:** The system's maximum service capacity is $2\mu$ (two customers served at rate $\mu$). For the queue to not grow indefinitely, the arrival rate ($\lambda$) must be less than this maximum clearance rate.
    

## 4. Final Solution and Metrics

### A. Steady-State Probabilities

The probability of the system being empty ($P_0$) is found by summing the geometric series and applying the normalization condition ($\sum P_n = 1$):

$$\boxed{P_{0} = \frac{\lambda(1-\alpha)}{\lambda + \mu(1-\alpha)}}$$

The general probability for $n \ge 2$ is $\mathbf{P_{n} = \alpha^n P_{0}}$.

### B. Average Number in Queue ($L_Q$)

The expected number of customers waiting is found by $L_Q = \sum n P_n$, which is calculated efficiently using the derivative trick for geometric series:

$$\mathbf{L_{Q}} = \frac{\lambda(1-\alpha)}{\lambda+\mu(1-\alpha)} \cdot \frac{\alpha}{(1-\alpha)^2}$$

### C. Time Metrics (Little's Law)

The average waiting time and total time in the system are derived directly from $L_Q$ and the arrival rate $\lambda$:

- **Average Waiting Time:** $W_{Q} = \frac{L_{Q}}{\lambda}$
    
- **Average Time in System:** $W = W_{Q} + \frac{1}{\mu}$
    

This detailed analysis covers all the steps for solving the Bulk QS. Do you have specific values for $\lambda$ and $\mu$ that you'd like to plug in, or would you like to see a similar detailed breakdown of the two-server **Open Network of Queues** (the final topic in your notes)?