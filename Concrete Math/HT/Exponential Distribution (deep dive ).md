## Lecture Note: The Exponential Distribution

### Part 1: The Theory (Easy to Grasp)

**1. The Core Idea: The "Waiting Time" Distribution**

At its simplest, the Exponential distribution answers the question: **"How long do I have to wait until the _next_ event happens?"**

Think about events happening randomly over time, but at a consistent _average rate_.

- How long until the next customer arrives at a store?
    
- How long until the next radioactive particle decays?
    
- How long until the next bus arrives (assuming they arrive randomly)?
    
- How long until a lightbulb (which can fail at any random moment) burns out?
    

The _process_ of these events happening is a **Poisson Process**.

- A **Poisson** RV counts _how many_ events happen in a fixed time. (e.g., "3 customers arrived _in one hour_").
    
- An **Exponential** RV measures the _time until_ the next event. (e.g., "The _wait_ for the next customer was 0.4 hours").
    

**2. The Link to Poisson (The "Proof")**

This is the key to understanding it. Let $T$ be the waiting time for the next event. Let $N(t)$ be the _number_ of events that happen in $t$ units of time. $N(t)$ follows a Poisson distribution with parameter $\lambda t$, where $\lambda$ is the average _rate_ of events.

The event "waiting time is more than $t$" ($T > t$) is the _exact same_ as the event "zero events happened in time $t$" ($N(t) = 0$).

- $P(T > t) = P(N(t) = 0)$
    
- From the Poisson PMF, $P(N(t) = k) = \frac{e^{-\lambda t} (\lambda t)^k}{k!}$
    
- So, $P(N(t) = 0) = \frac{e^{-\lambda t} (\lambda t)^0}{0!} = e^{-\lambda t}$
    
- Therefore, $\mathbf{P(T > t) = e^{-\lambda t}}$.
    

This $P(T > t)$ is called the **Survival Function**, and it's the most useful formula.

**3. The Key Formulas**

If $T \sim Expo(\lambda)$:

- **Parameter ($\lambda$):** The **rate** of events. (e.g., $\lambda = 5$ customers/hour).
    
- **Survival (Survival Function):** $\mathbf{P(T > t) = e^{-\lambda t}}$
    
- **CDF (Cumulative Distribution):** $\mathbf{F(t) = P(T \le t)} = 1 - P(T > t) = \mathbf{1 - e^{-\lambda t}}$
    
- **PDF (Probability Density):** $f(t) = F'(t) = \frac{d}{dt}(1 - e^{-\lambda t}) = \mathbf{\lambda e^{-\lambda t}}$
    

**4. Key Properties**

- **Expectation (Mean):** $E[T] = \mathbf{1/\lambda}$
    
    - _Intuition:_ If the rate $\lambda$ is 5 customers/hour, the average _wait_ $E[T]$ is 1/5 of an hour (12 minutes). This makes perfect sense.
        
- **Variance:** $Var(T) = \mathbf{1/\lambda^2}$
    
    - Standard Deviation: $SD(T) = \sqrt{1/\lambda^2} = 1/\lambda$. The mean and the standard deviation are the same!
        
- **The Memoryless Property (This is the big one!)**
    
    - **Formally:** $P(T > s+t \mid T > s) = P(T > t)$
        
    - **In English:** "The probability that you have to wait an _additional_ $t$ minutes, _given_ that you've already waited $s$ minutes, is the _exact same_ as the probability of waiting $t$ minutes from the start."
        
    - **Intuition:** The distribution "forgets" how long it has been waiting. The process doesn't get "tired" or "overdue." A 10-minute-old lightbulb has the same future lifetime distribution as a brand-new one. A bus stop where buses arrive according to this process is never "due" for a bus.
        
    - Proof (using the survival function):
        
        $P(T > s+t \mid T > s) = \frac{P(T > s+t \text{ and } T > s)}{P(T > s)}$
        
        $= \frac{P(T > s+t)}{P(T > s)} = \frac{e^{-\lambda(s+t)}}{e^{-\lambda s}} = \frac{e^{-\lambda s} e^{-\lambda t}}{e^{-\lambda s}} = e^{-\lambda t} = P(T > t)$.
        

---

### Part 2: 10 Practice Problems (Increasing Difficulty)

#### Difficulty 1: Basic Calculations

**Problem 1:** The time between calls at a call center is exponentially distributed with a rate of $\lambda = 4$ calls per minute. If a call just ended, what is the probability that the next call arrives within 15 seconds?

**Problem 2:** A radioactive particle has a decay time $T$ that is exponentially distributed. The average (mean) decay time is 500 years. What is the probability that a particle survives for _at least_ 1000 years?

#### Difficulty 2: Using Properties

Problem 3: On a certain website, the time between user clicks is $T \sim Expo(0.2)$, where time is in seconds.

(a) What is the expected time between clicks?

(b) What is the standard deviation of the time between clicks?

**Problem 4 (The Classic Bus Problem):** Buses arrive at a stop according to an exponential distribution with an average of 10 minutes between arrivals. You arrive at the stop. You have already waited 5 minutes and no bus has come. What is the expected _additional_ time you have to wait for the next bus?

#### Difficulty 3: More Complex Scenarios

Problem 5: Let $T$ be an exponential random variable. You are told that $P(T > 3) = 0.25$.

(a) Find $\lambda$.

(b) Using this $\lambda$, find $P(T > 6)$.

(c) Without finding $\lambda$, find $P(T > 6 \mid T > 3)$.

Problem 6 (Minimum of Exponentials): This is a key property. If $T_1 \sim Expo(\lambda_1)$ and $T_2 \sim Expo(\lambda_2)$ are independent, their minimum $T_{\min} = \min(T_1, T_2)$ is also exponential.

Find the distribution of $T_{\min}$. (Hint: Find $P(T_{\min} > t)$).

Problem 7: You have two servers, A and B, processing jobs. Server A's processing time is $T_A \sim Expo(2)$ (jobs/min) and Server B's is $T_B \sim Expo(3)$ (jobs/min). A new job is sent to both servers simultaneously.

(a) What is the probability that Server A finishes first?

(b) What is the expected time until the job is first completed (by either server)?

#### Difficulty 4: Linking to Other Distributions

**Problem 8:** Customers arrive at a bank in a Poisson process at a rate of $\lambda = 12$ customers per hour. What is the probability that you have to wait _more than_ 10 minutes for the next customer?

Problem 9 (Sum of Exponentials - Gamma): If $T_1, T_2, \dots, T_k$ are i.i.d. $Expo(\lambda)$ random variables, their sum $S_k = T_1 + \dots + T_k$ represents the waiting time for the k-th event. This is a Gamma distribution.

(a) What is $E[S_k]$?

(b) If $\lambda = 12$ customers/hour, what is the expected time to wait for the 5th customer?

#### Difficulty 5: Tricky Conditional Probability

**Problem 10:** Let $T \sim Expo(1/3)$. Find $P(T > 8 \mid T > 5 \text{ and } T < 12)$.

---

### Part 3: Solutions

1. Solution (15 sec = 0.25 min):

$T \sim Expo(4)$. We want $P(T \le 0.25)$.

$P(T \le 0.25) = 1 - e^{-\lambda t} = 1 - e^{-4 \cdot 0.25} = 1 - e^{-1} \approx 1 - 0.3678 = \mathbf{0.6322}$.

2. Solution (Mean = 500 years):

$E[T] = 1/\lambda = 500$, so $\lambda = 1/500$.

We want $P(T > 1000)$.

$P(T > 1000) = e^{-\lambda t} = e^{-(1/500) \cdot 1000} = e^{-2} \approx \mathbf{0.1353}$.

(This is $P(T > 2 \cdot E[T])$).

3. Solution:

(a) $E[T] = 1/\lambda = 1/0.2 = \mathbf{5 \text{ seconds}}$.

(b) $SD(T) = 1/\lambda = \mathbf{5 \text{ seconds}}$.

4. Solution:

Because of the Memoryless Property, the fact that you've already waited 5 minutes is irrelevant to the future waiting time. The expected additional wait is the same as the original expected wait.

$E[W] = 1/\lambda = \mathbf{10 \text{ minutes}}$.

5. Solution:

(a) $P(T > 3) = e^{-\lambda \cdot 3} = 0.25$.

$\ln(e^{-3\lambda}) = \ln(0.25) \implies -3\lambda = \ln(0.25) \implies \lambda = -\ln(0.25)/3 \approx 1.386/3 = \mathbf{0.462}$.

(b) $P(T > 6) = e^{-\lambda \cdot 6} = e^{-3\lambda \cdot 2} = (e^{-3\lambda})^2 = (0.25)^2 = \mathbf{0.0625}$.

(c) By the memoryless property: $P(T > 6 \mid T > 3) = P(T > 3+3 \mid T > 3) = P(T > 3) = \mathbf{0.25}$.

6. Solution (Minima):

We find the survival function $P(T_{\min} > t)$.

$T_{\min} > t$ means both $T_1$ and $T_2$ must be greater than $t$.

$P(T_{\min} > t) = P(T_1 > t \text{ and } T_2 > t)$

Since they are independent:

$P(T_{\min} > t) = P(T_1 > t) \cdot P(T_2 > t)$

$P(T_{\min} > t) = (e^{-\lambda_1 t}) \cdot (e^{-\lambda_2 t}) = e^{-(\lambda_1 + \lambda_2)t}$

This is the survival function for an Exponential distribution with rate $(\lambda_1 + \lambda_2)$.

Answer: $T_{\min} \sim \mathbf{Expo(\lambda_1 + \lambda_2)}$.

7. Solution:

(a) $T_A \sim Expo(2)$, $T_B \sim Expo(3)$. Server A finishes first if $T_A < T_B$. This is a standard result. The probability $P(T_A < T_B) = \frac{\lambda_A}{\lambda_A + \lambda_B}$.

$P(T_A < T_B) = \frac{2}{2+3} = \mathbf{2/5 \text{ or } 40\%}$.

(b) The time until the first completion is $T_{\min} = \min(T_A, T_B)$.

From (6), $T_{\min} \sim Expo(\lambda_A + \lambda_B) \sim Expo(2+3) \sim Expo(5)$.

$E[T_{\min}] = 1/(\lambda_A + \lambda_B) = 1/5 = \mathbf{0.2 \text{ minutes}}$ (or 12 seconds).

8. Solution:

This is a Poisson/Exponential link. $\lambda = 12$ customers/hour.

The waiting time $T$ for the next customer is $T \sim Expo(12)$.

We want the probability $P(T > 10 \text{ minutes})$.

Units must match! $\lambda = 12$/hour. $t = 10 \text{ min} = 1/6 \text{ hour}$.

$P(T > 1/6) = e^{-\lambda t} = e^{-12 \cdot (1/6)} = e^{-2} \approx \mathbf{0.1353}$.

9. Solution:

(a) $S_k = T_1 + \dots + T_k$. By Linearity of Expectation:

$E[S_k] = E[T_1] + \dots + E[T_k] = (1/\lambda) + \dots + (1/\lambda) = \mathbf{k/\lambda}$.

(b) We want the expected time for the 5th customer, $E[S_5]$.

$k=5$, $\lambda=12$/hour.

$E[S_5] = 5 / 12$ hours.

$(5/12) \cdot 60 \text{ min} = \mathbf{25 \text{ minutes}}$.

10. Solution:

This is tricky. The memoryless property doesn't apply directly because of the $T < 12$ condition. We must use the definition of conditional probability.

Let $A = (T > 8)$, $B = (T > 5 \text{ and } T < 12)$. We want $P(A \mid B) = \frac{P(A \cap B)}{P(B)}$.

$\lambda = 1/3$.

- Numerator ($A \cap B$): $P( (T > 8) \text{ and } (T > 5 \text{ and } T < 12) )$
    
    This simplifies to $P(8 < T < 12)$.
    
    $P(8 < T < 12) = F(12) - F(8) = (1 - e^{-12/3}) - (1 - e^{-8/3}) = e^{-8/3} - e^{-4}$.
    
- Denominator ($B$): $P(5 < T < 12)$
    
    $P(5 < T < 12) = F(12) - F(5) = (1 - e^{-12/3}) - (1 - e^{-5/3}) = e^{-5/3} - e^{-4}$.
    
- Answer:
    
    $P(A \mid B) = \frac{e^{-8/3} - e^{-4}}{e^{-5/3} - e^{-4}}$.
    
    (We can simplify this by $e^{-4} = e^{-12/3}$)
    
    $P(A \mid B) = \frac{e^{-8/3} - e^{-12/3}}{e^{-5/3} - e^{-12/3}}$.