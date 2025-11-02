### **Lecture 2, Part 6: Exponential Distribution and Failure/Lifetime**

This section uses the properties of continuous random variables to solve a common reliability problem, often seen in networking or hardware systems.

#### **The Setup: Independent Lifetimes**

Your notes use the example of two bulbs, but this applies to two routers, two processors, or any two components that can fail.

- **Component 1 (Bulb 1):** Lifetime is a random variable $X_1$.
    
- **Component 2 (Bulb 2):** Lifetime is a random variable $X_2$.
    
- **Key Property:** $X_1$ and $X_2$ are **independent** random variables (one failing doesn't affect the other).
    
- **Distribution:** Both are exponentially distributed. This is the **memoryless** continuous distribution—just like the Markov Chain is the memoryless discrete process.
    

#### **The Exponential Distribution**

The Exponential Distribution is used to model the time until an event occurs (e.g., component failure, packet arrival).

- **Rate Parameter ($\lambda$):** $\lambda$ is the average rate of events. In your notes:
    
    - Bulb 1 has mean $1/\lambda_1 = 5$ hrs, so $\lambda_1 = 1/5$ (rate of failure per hour).
        
    - Bulb 2 has mean $1/\lambda_2 = 10$ hrs, so $\lambda_2 = 1/10$.
        
- **PDF (Probability Density Function):** $f(x) = \lambda e^{-\lambda x}$, for $x \ge 0$.
    
- **CDF (Cumulative Distribution Function):** $F(x) = P(X \le x) = 1 - e^{-\lambda x}$.
    
- **Survival Function $P(X > x)$:** The probability that the component survives past time $x$. $P(X > x) = 1 - F(x) = e^{-\lambda x}$.
    

#### **The Question**

> What is the probability that Bulb 1 fails before Bulb 2?
> 
> $$P\{X_1 < X_2\}$$

#### **The Solution Method (Integration)**

We calculate this probability by integrating over all possible failure times $x$ for the first bulb ($X_1$), using the Law of Total Probability for continuous variables.

$$P\{X_1 < X_2\} = \int_{x=0}^{\infty} P\{X_1 < X_2 \text{ and } X_1 = x\} dx$$

Using the substitution: $P(A \text{ and } B) = P(B|A) P(A)$, where $P(A)$ is $f_1(x) dx$:

$$P\{X_1 < X_2\} = \int_{0}^{\infty} P\{X_2 > x | X_1 = x\} \cdot f_1(x) dx$$

1. **Due to Independence:** $P\{X_2 > x | X_1 = x\} = P\{X_2 > x\}$. The failure time of $X_2$ is independent of $X_1$'s failure time.
    
2. Substitute Survival Function $P(X_2 > x)$:
    
    $$P\{X_2 > x\} = e^{-\lambda_2 x}$$
    
3. Substitute $f_1(x)$:
    
    $$f_1(x) = \lambda_1 e^{-\lambda_1 x}$$
    

Plugging these back into the integral:

$$P\{X_1 < X_2\} = \int_{0}^{\infty} (e^{-\lambda_2 x}) \cdot (\lambda_1 e^{-\lambda_1 x}) dx$$

### **The Final Calculation**

Now we simplify the exponents:

$$P\{X_1 < X_2\} = \lambda_1 \int_{0}^{\infty} e^{-(\lambda_1 + \lambda_2)x} dx$$

This is a standard exponential integral of the form $\int e^{-ax} dx = -1/a \cdot e^{-ax}$.

Let $A = \lambda_1 + \lambda_2$.

$$P\{X_1 < X_2\} = \lambda_1 \left[ \frac{-1}{A} e^{-Ax} \right]_{0}^{\infty}$$

Substituting the limits:

$$P\{X_1 < X_2\} = \lambda_1 \left[ 0 - \frac{-1}{A} e^{-A \cdot 0} \right] = \lambda_1 \left[ \frac{1}{A} \right] \cdot 1$$

$$\mathbf{P\{X_1 < X_2\} = \frac{\lambda_1}{\lambda_1 + \lambda_2}}$$

#### **Conclusion (The Final Example)**

The probability that the first event occurs before the second is simply the rate of the first event divided by the sum of the rates. The higher the rate, the sooner the event is likely to happen.

Using your specific values: $\lambda_1 = 1/5$ and $\lambda_2 = 1/10$.

$$P\{X_1 < X_2\} = \frac{1/5}{1/5 + 1/10} = \frac{1/5}{3/10} = \frac{1}{5} \cdot \frac{10}{3} = \frac{2}{3}$$

**Interpretation:** Since Bulb 1 fails twice as fast as Bulb 2 (5 hours vs. 10 hours mean), it has a $2/3$ chance of failing first.

