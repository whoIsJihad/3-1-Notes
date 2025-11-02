# Review: Distribution of Inter-Arrival Time (Poisson Processes)

This document explains the concepts and formulas on Page 1 of your lecture notes L10, which establishes the fundamental link between **counting events (Poisson)** and **waiting time (Exponential)**.

## 1. Core Definitions

| Variable | Description            | Meaning in Simple Terms                                                     |
| -------- | ---------------------- | --------------------------------------------------------------------------- |
| $N(t)$   | Counting Process       | The **total number** of events that have occurred by time $t$.              |
| $S_n$    | Time of $n^{th}$ Event | The **total time** from $t=0$ until the $n^{th}$ event occurs.              |
| $T_i$    | Inter-Arrival Time     | The **waiting time** between the $(i-1)^{th}$ event and the $i^{th}$ event. |

**Relationship:** The time of the $n^{th}$ event is the sum of all waiting times: $S_n = T_1 + T_2 + \dots + T_n$.

## 2. Derivation of the Exponential Distribution

The core mathematical derivation proves that the waiting time, $T_i$, is an Exponential Random Variable.

### A. Equating Waiting Time to Zero Count

We start by finding the probability that the waiting time $T_1$ is greater than some duration $t$.

$$P\{T_1 > t\} = P\{N(t) = 0\}$$

**Logic:** For the waiting time $T_1$ to be longer than $t$, it must logically mean that **zero events** occurred in the entire time interval $(0, t]$.

### B. Using the Poisson Formula

The probability of $N(t)=0$ is found using the Poisson Probability Mass Function (PMF), where $n=0$:

$$P\{N(t) = 0\} = e^{-\lambda t} \frac{(\lambda t)^0}{0!} = e^{-\lambda t}$$

### C. Conclusion (Survival Function)

Since $P\{T_1 > t\} = e^{-\lambda t}$, the waiting time $T_1$ follows the **Exponential Distribution** with rate $\lambda$.

$$\text{Mean Inter-Arrival Time} = E[T_1] = \frac{1}{\lambda}$$

## 3. The Memoryless Property of Inter-Arrival Times

This part verifies that the waiting times are independent, which relies on the memoryless nature of the Poisson Process.

The equation is:

$$P\{T_2 > t | T_1 = s\} = e^{-\lambda t}$$

**Interpretation:**

- **Left Side (With History):** Probability of waiting an extra time $t$, _given_ the previous wait was $s$.
    
- **Right Side (Fresh Start):** Probability of waiting time $t$, _starting from zero_.
    

**The Rule:** The **Independent Increments** property of the Poisson process means the history ($T_1=s$) is irrelevant. The process resets after every event.

**Result:** All inter-arrival times ($T_1, T_2, T_3, \dots$) are **independent** and **identically distributed** $\text{Exp}(\lambda)$ random variables.

## 4. Example Applications (Migration)

**Scenario:** People migrate at a Poisson rate $\lambda=1$ per day.

### A. Expected Time until the $10^{th}$ Person ($E[S_{10}]$)

This is the sum of the expected values of 10 independent Exponential random variables.

$$E[S_{10}] = 10 \cdot E[T_i] = 10 \cdot \frac{1}{\lambda}$$

**Calculation:** $E[S_{10}] = 10 \cdot \frac{1}{1} = 10 \text{ days}$

### B. Probability that the Waiting Time $T_{11}$ Exceeds 2 Days

This uses the Exponential Survival Function for a single waiting period.

$$P\{T_{11} > 2\} = e^{-\lambda t} = e^{-(1) \cdot 2}$$

**Calculation:** $P\{T_{11} > 2\} = e^{-2} \approx 0.135$

