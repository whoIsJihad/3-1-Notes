
Now that we have the probability $P_n$, we can calculate the expected performance measures. The challenge here is calculating the sum for $L$.

## 1. Average Number of Customers in System ($L$)

The average number of customers, $L$, is the expected value of the number of customers, $n$:

$$L = \sum_{n=0}^{N} n P_n$$

Substituting $P_n = P_0 \rho^n$:

$$L = P_0 \sum_{n=0}^{N} n \rho^n$$

This summation $\sum_{n=0}^{N} n \rho^n$ is what requires the differentiation trick.

### The Differentiation Trick

Let $S(x) = \sum_{n=0}^{N} x^n$. We know the closed form for this geometric series:

$$S(x) = \frac{1 - x^{N+1}}{1 - x}$$

Now, differentiate $S(x)$ with respect to $x$:

$$\frac{d}{dx} S(x) = \frac{d}{dx} \sum_{n=0}^{N} x^n = \sum_{n=0}^{N} n x^{n-1}$$

To get the desired sum, $\sum_{n=0}^{N} n x^n$, we multiply by $x$:

$$x \frac{d}{dx} S(x) = x \sum_{n=0}^{N} n x^{n-1} = \sum_{n=0}^{N} n x^n$$

So, we calculate: $L = P_0 \left[ \rho \frac{d}{d\rho} \left( \frac{1 - \rho^{N+1}}{1 - \rho} \right) \right]$.

### Final Formula for $L$ ($\rho \ne 1$)

After performing the differentiation and substituting the values (as hinted in your notes), the average number of customers $L$ simplifies to:

$$\boxed{L = \frac{\rho}{1 - \rho} - \frac{(N+1)\rho^{N+1}}{1 - \rho^{N+1}}}$$

_Alternatively, the formula can be written as (as derived in your notes):_

$$L = \frac{\rho}{1-\rho} \cdot \left[ \frac{1 - (N+1)\rho^N + N\rho^{N+1}}{1 - \rho^{N+1}} \right]$$

## 2. Average Time in System ($W$)

For any general queueing system, we use Little's Law: $W = \frac{L}{\lambda_a}$, where $\lambda_a$ is the **effective arrival rate**.

### The Effective Arrival Rate ($\lambda_a$)

Since customers are lost when the system is full (in state $N$), the effective arrival rate is $\lambda$ times the probability that the system is **not** full:

$$\lambda_a = \lambda (1 - P_N)$$

Substituting $P_N$:

$$\lambda_a = \lambda \left[ 1 - \rho^N \left( \frac{1 - \rho}{1 - \rho^{N+1}} \right) \right]$$

This is $\lambda$ multiplied by the probability that an arrival actually enters the system.

### Final Formula for $W$

Now we apply Little's Law:

$$W = \frac{L}{\lambda_a}$$

Due to the complexity of the $L$ and $\lambda_a$ terms, the formula is usually left in this fractional form, or by using the relationship $W = W_Q + 1/\mu$ to find $W_Q$.

### Average Waiting Time in Queue ($W_Q$)

$$W_Q = W - \frac{1}{\mu}$$

### Average Number in Queue ($L_Q$)

Using Little's Law for the queue:

$$L_Q = \lambda_a W_Q$$