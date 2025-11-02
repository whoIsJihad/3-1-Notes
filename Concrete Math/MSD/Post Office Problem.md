

---

## Section A: The Post Office Problem (Expected Time)

The goal is to find the total average time $E[T]$ you spend in the post office.

### **Step 1: The Setup (What is happening?)**

Imagine you walk into the post office.

- **The Situation:** There are two clerks (Clerk 1 and Clerk 2). Both are busy with other customers. .
    
- **Your Action:** Since no one is waiting, you stand ready to go to whichever clerk finishes their current customer first.
    
- **Service Time ($S$):** Your own service time, once you get a clerk, is also a random duration.
    

We define two crucial random variables:

- $R_1$: The **remaining time** until Clerk 1 is free.
    
- $R_2$: The **remaining time** until Clerk 2 is free.
    

### **Step 2: The Magic Assumption (Exponential and Memoryless)**

The entire problem hinges on this assumption: **All service times are Exponentially Distributed.**

- **Simple Meaning:** The time a service takes is random, but its probability follows a specific rule.
    
- **Crucial Rule (Memoryless Property):** If a service has already been going on for 5 minutes, the **remaining time ($R_i$)** is completely independent of those past 5 minutes. It's like the clock just reset.
    

Result of Memoryless Property:

$R_1$ and $R_2$ are independent, random variables with rates $\lambda_1$ and $\lambda_2$.

### **Step 3: Breaking Down Your Total Time $T$**

Your total time $T$ is the sum of two sequential events:

$$T = \underbrace{(\text{Time spent waiting for a clerk})}_{\text{Waiting Time}} + \underbrace{(\text{Time spent being served})}_{\text{Service Time}}$$

### **Step 4: The Law of Total Expectation (Splitting the Problem)**

Since you might get Clerk 1 OR Clerk 2, we calculate the expected time based on which event happens first. This uses the Law of Total Expectation:

$$E[T] = E[T \text{ if } R_1 < R_2] \cdot P\{R_1 < R_2\} + E[T \text{ if } R_2 \le R_1] \cdot P\{R_2 \le R_1\}$$

#### **Part 4a: Probability of Finishing First**

Since $R_1$ and $R_2$ are independent exponentials, the probability of one finishing before the other is simple (as covered in the last lecture):

$$P\{R_1 < R_2\} = \frac{\lambda_1}{\lambda_1 + \lambda_2}$$

$$P\{R_2 \le R_1\} = \frac{\lambda_2}{\lambda_1 + \lambda_2}$$

#### **Part 4b: Expected Time in Case 1 (Clerk 1 finishes first: $R_1 < R_2$)}

Here, you get Clerk 1.

$$E[T|R_1 < R_2] = \underbrace{E[\text{Waiting Time}]}_{\text{A}} + \underbrace{E[\text{Your Service Time}]}_{\text{B}}$$

- **A. Expected Waiting Time:** Your waiting time is exactly the time until the **first event occurs**, which is $\min(R_1, R_2)$.
    
    - The minimum of $R_1 \sim \text{Exp}(\lambda_1)$ and $R_2 \sim \text{Exp}(\lambda_2)$ is $M \sim \text{Exp}(\lambda_1 + \lambda_2)$.
        
    - Therefore, the expected waiting time is the mean of $M$:
        
        $$E[\min(R_1, R_2)] = \frac{1}{\lambda_1 + \lambda_2}$$
        
- B. Expected Service Time ($E[S]$): Your service is with Clerk 1, whose mean service time is $1/\lambda_1$.
    
    $$E[S] = \frac{1}{\lambda_1}$$
    

$$\mathbf{E[T|R_1 < R_2] = \frac{1}{\lambda_1 + \lambda_2} + \frac{1}{\lambda_1}}$$

#### **Part 4c: Expected Time in Case 2 (Clerk 2 finishes first: $R_2 \le R_1$)}

Symmetrically, you get Clerk 2 (mean service $1/\lambda_2$), but the waiting time remains the same:

$$\mathbf{E[T|R_2 \le R_1] = \frac{1}{\lambda_1 + \lambda_2} + \frac{1}{\lambda_2}}$$

### **Step 5: Final Calculation (The Weighted Sum)**

Now we combine everything (the step-by-step algebra you had in your notes):

$$E[T] = \left(\frac{1}{\lambda_1 + \lambda_2} + \frac{1}{\lambda_1}\right) \frac{\lambda_1}{\lambda_1 + \lambda_2} + \left(\frac{1}{\lambda_1 + \lambda_2} + \frac{1}{\lambda_2}\right) \frac{\lambda_2}{\lambda_1 + \lambda_2}$$

1. Split the Terms: Separate the waiting time part from the service time part:
    
    $$E[T] = \underbrace{\frac{\lambda_1}{(\lambda_1 + \lambda_2)^2} + \frac{\lambda_2}{(\lambda_1 + \lambda_2)^2}}_{\text{Waiting Time Terms}} + \underbrace{\frac{1}{\lambda_1} \frac{\lambda_1}{\lambda_1 + \lambda_2} + \frac{1}{\lambda_2} \frac{\lambda_2}{\lambda_1 + \lambda_2}}_{\text{Service Time Terms}}$$
    
2. Simplify the Waiting Time Terms (The Denominators are the same):
    
    $$\text{Waiting Time} = \frac{\lambda_1 + \lambda_2}{(\lambda_1 + \lambda_2)^2} = \frac{1}{\lambda_1 + \lambda_2}$$
    
3. Simplify the Service Time Terms (The $\lambda_i$ terms cancel out):
    
    $$\text{Service Time} = \frac{1}{\lambda_1 + \lambda_2} + \frac{1}{\lambda_1 + \lambda_2} = \frac{2}{\lambda_1 + \lambda_2}$$
    
4. Final Result:
    
    $$E[T] = \frac{1}{\lambda_1 + \lambda_2} + \frac{2}{\lambda_1 + \lambda_2} = \mathbf{\frac{3}{\lambda_1 + \lambda_2}}$$
    

---

## Section B: Counting Processes and the Poisson Process

This second part of the lecture defines a new kind of continuous-time stochastic process, which is fundamental to modeling event arrivals (like network packets, server requests, or failures).

### **Step 6: What is a Counting Process?**

A **Counting Process** $N(t)$ simply counts the total number of events that have occurred up to time $t$.

- **$N(t)$:** Total number of events by time $t$.
    

#### **Properties (As noted in your document)**

1. **Starts at 0:** $N(0) \ge 0$. (Usually $N(0)=0$, meaning no events before time starts).
    
2. **Integer Valued:** $N(t)$ must be an integer (you can't have 1.5 events).
    
3. **Non-decreasing:** If $s < t$, then $N(s) \le N(t)$. (The count can't go down).
    
4. **Interval Count:** $N(t) - N(s)$ is the number of events in the time interval $(s, t]$.
    

**Example:** The number of people entering a mall by time $t$.

### **Step 7: Key Conditions for a Special Counting Process**

Two additional conditions turn a simple Counting Process into something more useful for modeling systems:

#### **A. Independent Increment**

The number of events that occur in one time interval must be **independent** of the number of events that occur in any separate (disjoint) time interval.

- _Example:_ The number of network packets arriving between $t=10$ and $t=11$ is independent of the number of packets arriving between $t=15$ and $t=20$.
    
- _Your Note:_ $N(10)$ is independent of $N(15) - N(10)$. (The count up to $t=10$ is independent of the count from $t=10$ to $t=15$).
    

#### **B. Stationary Increment**

The probability distribution of the number of events in an interval depends **only on the length** of the time interval, not on when the interval starts.

- _Example:_ The probability of getting 5 server requests between 9:00 AM and 10:00 AM is the same as the probability of getting 5 requests between 3:00 PM and 4:00 PM (if the interval length is 1 hour).
    
- _Your Note:_ This means there can be no "peak time, down time" because the distribution must be the same for all time $s$.
    

### **Step 8: The Poisson Process**

A Counting Process that satisfies all the conditions from Steps 6 and 7 (plus $N(0)=0$) is called a **Poisson Process** with rate $\lambda$. This is the single most important counting process in engineering.

#### **Properties of the Poisson Process**

1. **$N(0)=0$** (Starts empty).
    
2. **Independent Increments.**
    
3. **Stationary Increments.**
    

#### **The Distribution**

The defining characteristic is its distribution:

- **Event Count is Poisson Distributed:** The number of events $N(t) - N(s)$ that occur in any time interval of length $t$ is a Poisson random variable with parameter $\lambda t$.
    

$$P\{N(t+s) - N(s) = n\} = e^{-\lambda t} \frac{(\lambda t)^n}{n!}$$

- $E[N(t)] = \lambda t$: The expected number of events in a period of length $t$ is simply the rate $\lambda$ times the length $t$.
    

#### **The Connection to Exponential**

- **The Number of Events** (Count, $N(t)$) is **Poisson Distributed**.
    
- **The Time Between Events** (Inter-arrival time) is **Exponentially Distributed**.
    

These two concepts are mathematically linked: the Exponential Distribution generates the time stamps for the events counted by the Poisson Distribution.

