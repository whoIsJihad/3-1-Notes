# 📘 Queueing Theory — From Birth–Death Processes to the M/M/1 Model

## **Part 1 — Introduction to Queueing Theory**

### 🌱 What Is Queueing Theory?

Queueing theory is the **mathematical study of waiting lines.**

It appears whenever **demand temporarily exceeds resources** — for example:

- People waiting at a checkout
    
- Data packets waiting in a router buffer
    
- Cars waiting at a toll booth
    

It helps us answer:

> “How long will customers wait, and how busy is my server?”

### ⚙️ The Four Key Metrics

We measure the performance of a queue with four average quantities:

|Symbol|Meaning|Description|
|---|---|---|
|$L$|Average number **in the system**|Waiting + being served|
|$L_Q$|Average number **in the queue**|Only waiting|
|$W$|Average **time in the system**|Arrival $\to$ departure|
|$W_Q$|Average **waiting time**|Arrival $\to$ start of service|

They’re all interrelated.

### 🔑 Little’s Law — The Master Relationship

Little’s Law connects the _average number_ of customers and the _average time_ they spend.

$$L = \lambda W$$

and for the queue only:

$$L_Q = \lambda W_Q$$

where:

- $\lambda$ = average **arrival rate** (customers per unit time)
    
- $W$ = average **time in system**
    
- $L$ = average **number in system**
    

### 🧠 Intuitive Meaning

If, on average,

- $\lambda = 5$ people/minute
    
- each stays $W = 2$ minutes,
    

then:

$$L = 5 \times 2 = 10$$

$\to$ On average, 10 people are in the system.

## **Part 2 — Probabilities and the PASTA Property**

To describe how the queue behaves, we define three probability types:

|Symbol|Meaning|Description|
|---|---|---|
|$P_n$|Steady-state probability|Fraction of **time** system has $n$ customers|
|$a_n$|Arrival probability|Fraction of **arrivals** that see $n$ customers|
|$d_n$|Departure probability|Fraction of **departures** leaving $n$ customers|

### ✨ The PASTA Property

If **arrivals are Poisson**, then:

$$P_n = a_n$$

This means **“Poisson Arrivals See Time Averages” (PASTA)** — what an arriving customer observes equals the true long-run state of the system.

## **Part 3 — The M/M/1 Queue**

### 🔹 What “M/M/1” Means

This is the simplest queueing model, written in **Kendall-Lee notation**:

|Symbol|Meaning|Interpretation|
|---|---|---|
|**M**|“Memoryless” inter-arrival times $\to$ **Poisson arrivals**|Arrivals are random and independent|
|**M**|“Memoryless” service times $\to$ **Exponential distribution**|Service time is random, but with an average rate|
|**1**|Single server|One service channel|

So:

> **M/M/1 = Poisson arrivals + Exponential service + 1 server**

### ⚙️ As a Birth–Death Process

In a **Birth–Death process**:

- **Birth = Arrival of a new customer**
    
    $$\lambda_n = \lambda \quad \text{for all } n \ge 0$$
- **Death = Completion of a service**
    
    $$\mu_n = \mu \quad \text{for all } n \ge 1$$

|State ($n$)|Description|Arrival rate|Departure rate|
|---|---|---|---|
|0|Empty|$\lambda$|—|
|1|1 person|$\lambda$|$\mu$|
|2|2 people|$\lambda$|$\mu$|
|$\dots$|$\dots$|$\lambda$|$\mu$|

## **Solving the M/M/1 Model**

### Step 1 — General Steady-State Formula

From Birth–Death process theory:

$$P_n = P_0 \times \frac{\lambda_{n-1}\lambda_{n-2}\dots\lambda_0}{\mu_n\mu_{n-1}\dots\mu_1}$$

Plug in $\lambda_n = \lambda$ and $\mu_n = \mu$:

$$P_n = P_0 \left(\frac{\lambda}{\mu}\right)^n$$

### Step 2 — Define **Traffic Intensity**

Let:

$$\rho = \frac{\lambda}{\mu}$$

called **traffic intensity** or **utilization** (fraction of time server is busy).

Then:

$$P_n = P_0 \rho^n$$

### Step 3 — Find $P_0$ Using Normalization

All probabilities must sum to 1:

$$\sum_{n=0}^{\infty} P_n = 1$$

Substitute $P_n = P_0 \rho^n$:

$$P_0 \sum_{n=0}^{\infty} \rho^n = P_0 \frac{1}{1-\rho} = 1$$

So:

$$P_0 = 1 - \rho$$

> $P_0$ = probability the system is empty. This series converges **only if** $\rho < 1$ (i.e. $\lambda < \mu$) — the **stability condition**.

### Step 4 — Final Solution

$$\boxed{P_n = (1 - \rho)\rho^n}, \quad n = 0,1,2,\dots$$

## **Performance Metrics**

Now we find $L, W, L_Q, W_Q$.

### ① Average number in system ($L$)

$$L = \sum_{n=0}^{\infty} nP_n = (1-\rho)\sum_{n=0}^{\infty} n\rho^n$$

We use the known identity for the summation:

$$\sum_{n=0}^{\infty} n x^n = \frac{x}{(1-x)^2}, \quad \text{for } |x|<1$$

Hence:

$$L = (1-\rho)\frac{\rho}{(1-\rho)^2} = \frac{\rho}{1-\rho}$$

Or equivalently:

$$L = \frac{\lambda}{\mu - \lambda}$$

### ② Average time in system ($W$)

Using Little’s Law ($L = \lambda W$):

$$W = \frac{L}{\lambda} = \frac{1}{\lambda} \left( \frac{\lambda}{\mu - \lambda} \right) = \frac{1}{\mu - \lambda}$$

### ③ Average waiting time in queue ($W_Q$)

Total time = waiting + service time:

$$W = W_Q + E[S]$$

Since service time is exponential with rate $\mu$:

$$E[S] = \frac{1}{\mu}$$

Therefore:

$$W_Q = W - \frac{1}{\mu}$$

Simplify:

$$W_Q = \frac{1}{\mu - \lambda} - \frac{1}{\mu} = \frac{\mu - (\mu - \lambda)}{\mu(\mu - \lambda)} = \frac{\lambda}{\mu(\mu - \lambda)}$$

### ④ Average number waiting in queue ($L_Q$)

Again using Little’s Law ($L_Q = \lambda W_Q$):

$$L_Q = \lambda \left(\frac{\lambda}{\mu(\mu - \lambda)}\right) = \frac{\lambda^2}{\mu(\mu - \lambda)}$$

## **Summary Table**

|Metric|Formula|Interpretation|
|---|---|---|
|$P_n$|$(1 - \rho)\rho^n$|Probability of $n$ customers in system|
|$P_0$|$1 - \rho$|Probability system is empty|
|$L$|$\frac{\rho}{1 - \rho} = \frac{\lambda}{\mu - \lambda}$|Avg. number in system|
|$W$|$\frac{1}{\mu - \lambda}$|Avg. time in system|
|$L_Q$|$\frac{\lambda^2}{\mu(\mu - \lambda)}$|Avg. number waiting|
|$W_Q$|$\frac{\lambda}{\mu(\mu - \lambda)}$|Avg. waiting time|
|Stability|$\rho < 1$|Arrival rate must be < service rate|

### 🧠 Intuitive Recap

- $\rho$ tells you how _busy_ the system is. If it’s close to 1, expect long waits.
    
- When $\lambda \to \mu$, queues grow rapidly.
    
- The M/M/1 model forms the **foundation** for all advanced queue types: M/M/c (multiple servers), M/M/1/K (limited capacity), etc.