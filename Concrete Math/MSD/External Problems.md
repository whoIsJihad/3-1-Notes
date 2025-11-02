


## Problem

The number of customers entering a store in a given day, $X$, has an expected value $E[X] = 100$ and a standard deviation $\sigma_X = 10$.

Use Chebyshev's inequality to find a lower bound for the probability that the number of customers is between $80$ and $120$ (i.e., $P(80 < X < 120)$).

## Solution

We are looking for $P(80 < X < 120)$, which is equivalent to $P(|X - \mu| < 20)$.

1. **Identify Parameters:**
    
    - Mean: $\mu = 100$
        
    - Standard Deviation: $\sigma = 10$
        
    - Variance: $\sigma^2 = 100$
        
    - Distance from mean: $t = 20$
        
2. **Apply Chebyshev's Inequality to the complement event:**
    
    $$P(|X - \mu| \ge t) \le \frac{\sigma^2}{t^2}$$$$P(|X - 100| \ge 20) \le \frac{10^2}{20^2}$$$$P(|X - 100| \ge 20) \le \frac{100}{400} = 0.25$$
3. **Find the lower bound for the desired probability:**
    
    $$P(80 < X < 120) = 1 - P(|X - 100| \ge 20)$$$$P(80 < X < 120) \ge 1 - 0.25$$$$P(80 < X < 120) \ge 0.75$$

### Result

The probability that the number of customers is between $80$ and $120$ is at least $75\%$.