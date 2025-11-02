

## Practice Problems: RVs, Expectation, Variance (L7-14)

### The Problem List

#### Section 1: Foundations (Bernoulli, Binomial, Expectation)

1. **Proof: Expectation of a Bernoulli(p) RV.**
    
2. **Proof: Expectation of a Binomial(n, p) RV using Linearity.**
    
3. **Proof: Expectation of a Binomial(n, p) RV using the PMF.** (The "hard way").
    
4. **Problem (Indicators):** You flip 10 fair coins. What is the expected number of "HH" (two heads in a row)? (Note: Flips 1-2, 2-3, ..., 9-10 are 9 "opportunities").
    
5. **Problem (Indicators):** A permutation of the numbers $\{1, 2, \dots, n\}$ is chosen. An element $i$ is a "fixed point" if it is in the $i$-th position. What is the expected number of fixed points?
    
6. **Proof: Expectation of a Geometric(p) RV using Conditioning.** (The "clever way").
    
7. **Proof: Expectation of a Negative Binomial(r, p) RV.**
    
8. **Problem (Hypergeometric):** A committee of 5 people is chosen from a group of 10 men and 8 women. What is the expected number of women on the committee?
    
9. **Problem (St. Petersburg Paradox):** A game costs $C$ dollars to play. A fair coin is flipped until it lands Heads. If it takes $k$ flips, you win $2^k$ dollars. What is the "fair" price $C$ to play this game (i.e., what is the expected payout)?
    

#### Section 2: Variance & Poisson

10. **Proof: The "Variance Shortcut" $Var(X) = E[X^2] - (E[X])^2$.**
    
11. **Proof: Variance of a Bernoulli(p) RV.**
    
12. **Proof: Variance of a Binomial(n, p) RV.**
    
13. **Proof: Expectation of a Poisson($\lambda$) RV.**
    
14. **Proof: Variance of a Poisson($\lambda$) RV.** (Requires the $E[X(X-1)]$ trick).
    
15. **Problem (Poisson Approx.):** A 500-page book has 1000 typos. What is the approximate probability that a randomly selected page has _at least_ 3 typos?
    
16. **Problem (Variance):** Let $X \sim Bin(100, 1/2)$. Find the (approximate) probability that $X$ falls within one standard deviation of its mean.
    

#### Section 3: Continuous Variables (Uniform, Exponential, Normal)

17. **Proof: Expectation and Variance of a Uniform(a, b) RV.**
    
18. **Proof: The Memoryless Property of the Exponential Distribution.**
    
19. **Problem (Exponential):** The time between buses arriving at a stop is $Expo(\lambda=1/10)$ (i.e., an average of 10 minutes between buses). If you arrive at the stop at a random time, what is the expected time you have to wait for the next bus?
    
20. **Problem (Normal):** A r.v. $X$ is $N(\mu=10, \sigma^2=9)$. Find $P(X > 13)$.
    
21. **Problem (Normal):** Let $Z_1, Z_2$ be i.i.d. $N(0, 1)$ r.v.s. What is the distribution of $Y = 3Z_1 - 2Z_2$?
    
22. **Problem (LOTUS):** Let $U \sim Unif(0, 1)$. Find $E[e^U]$.
    

---

---

## Detailed Solutions

### Section 1: Foundations (Bernoulli, Binomial, Expectation)

#### 1. Proof: Expectation of a Bernoulli(p) RV

- **Def:** Let $X \sim Bern(p)$. $X=1$ with probability $p$ and $X=0$ with probability $q=(1-p)$.
    
- **Expectation:** $E[X] = \sum x \cdot P(X=x)$
    
- $E[X] = (1 \cdot P(X=1)) + (0 \cdot P(X=0))$
    
- $E[X] = (1 \cdot p) + (0 \cdot q) = \mathbf{p}$.
    

#### 2. Proof: Expectation of a Binomial(n, p) RV using Linearity

- **Story:** A Binomial RV $X \sim Bin(n, p)$ counts the number of successes in $n$ independent Bernoulli trials.
    
- Indicators: We can write $X$ as the sum of $n$ indicator variables:
    
    $X = I_1 + I_2 + \dots + I_n$
    
    where $I_j = 1$ if the $j$-th trial is a success, and $I_j=0$ otherwise.
    
- **Expectation of Indicators:** From (1), we know $E[I_j] = p$ for all $j$.
    
- **Linearity of Expectation:** $E[X] = E[I_1 + I_2 + \dots + I_n]$
    
- $E[X] = E[I_1] + E[I_2] + \dots + E[I_n]$
    
- $E[X] = p + p + \dots + p$ ($n$ times)
    
- $E[X] = \mathbf{np}$. (This is so much easier than the PMF way!)
    

#### 3. Proof: Expectation of a Binomial(n, p) RV using the PMF

- **Def:** $P(X=k) = \binom{n}{k} p^k q^{n-k}$
    
- **Expectation:** $E[X] = \sum_{k=0}^{n} k \cdot P(X=k) = \sum_{k=0}^{n} k \cdot \binom{n}{k} p^k q^{n-k}$
    
- The $k=0$ term is 0, so we start the sum at $k=1$:
    
    $E[X] = \sum_{k=1}^{n} k \cdot \frac{n!}{k!(n-k)!} p^k q^{n-k}$
    
- Identity Trick: $k \cdot \frac{n!}{k!} = k \cdot \frac{n \cdot (n-1)!}{k \cdot (k-1)!} = n \cdot \frac{(n-1)!}{(k-1)!}$
    
    $E[X] = \sum_{k=1}^{n} n \cdot \frac{(n-1)!}{(k-1)!(n-k)!} p^k q^{n-k}$
    
- Pull $n$ and $p$ outside the sum:
    
    $E[X] = np \sum_{k=1}^{n} \frac{(n-1)!}{(k-1)!(n-k)!} p^{k-1} q^{n-k}$
    
- Change of Variables: Let $j = k-1$. When $k=1, j=0$. When $k=n, j=n-1$.
    
    Also, $n-k = n-(j+1) = (n-1)-j$.
    
    $E[X] = np \sum_{j=0}^{n-1} \frac{(n-1)!}{j!((n-1)-j)!} p^j q^{(n-1)-j}$
    
- The term inside the sum is just the PMF of a $Bin(n-1, p)$ distribution!
    
    $E[X] = np \sum_{j=0}^{n-1} P(Y=j)$ where $Y \sim Bin(n-1, p)$.
    
- The sum of all probabilities in a PMF is 1.
    
    $E[X] = np \cdot (1) = \mathbf{np}$.
    

#### 4. Problem (Indicators): Expected number of "HH" in 10 flips

- We have 10 flips: $F_1, F_2, \dots, F_{10}$.
    
- We are looking for "HH" pairs. There are 9 possible pairs:
    
    $(F_1, F_2), (F_2, F_3), \dots, (F_9, F_{10})$
    
- Let $X$ = total number of "HH" pairs.
    
- Let $I_j$ be an indicator for the $j$-th pair being "HH". (for $j=1 \dots 9$)
    
    $I_j = 1$ if $F_j=H$ and $F_{j+1}=H$. $I_j=0$ otherwise.
    
- $X = I_1 + I_2 + \dots + I_9$.
    
- By Linearity: $E[X] = \sum_{j=1}^{9} E[I_j]$.
    
- $E[I_j] = P(I_j=1) = P(F_j=H \text{ and } F_{j+1}=H)$
    
- Since flips are independent: $P(F_j=H) \cdot P(F_{j+1}=H) = (1/2) \cdot (1/2) = 1/4$.
    
- $E[X] = \sum_{j=1}^{9} (1/4) = 9 \cdot (1/4) = \mathbf{2.25}$.
    

#### 5. Problem (Indicators): Expected fixed points in a permutation

- Let $X$ = total number of fixed points.
    
- Let $P$ be a random permutation of $\{1, \dots, n\}$.
    
- Let $I_j$ be an indicator that position $j$ is a fixed point.
    
    $I_j = 1$ if $P(j) = j$. $I_j=0$ otherwise.
    
- $X = I_1 + I_2 + \dots + I_n$.
    
- By Linearity: $E[X] = \sum_{j=1}^{n} E[I_j]$.
    
- $E[I_j] = P(I_j=1) = P(P(j)=j)$.
    
- For a random permutation, what's the probability the $j$-th element is $j$? There are $n$ possible numbers it could be, all equally likely.
    
- $P(P(j)=j) = 1/n$.
    
- $E[X] = \sum_{j=1}^{n} (1/n) = n \cdot (1/n) = \mathbf{1}$.
    
- **Takeaway:** On average, _any_ random permutation has exactly 1 fixed point, regardless of $n$. This is a very cool result!
    

#### 6. Proof: Expectation of a Geometric(p) RV using Conditioning

- **Def:** $X \sim Geo(p)$. $X$ is the number of trials until the first success.
    
- Let $c = E[X]$. We want to find $c$.
    
- **Condition on the first trial:**
    
    - **Case 1 (Success):** With probability $p$, the first trial is a success. The game stops. $X=1$.
        
    - **Case 2 (Failure):** With probability $q=(1-p)$, the first trial is a failure. We have wasted 1 trial, and we are back to the start, still waiting for the first success. The _remaining_ expected trials is just $c$. So the total trials in this case is $(1+c)$.
        
- Law of Total Expectation:
    
    $E[X] = E[X | \text{1st is Success}] \cdot p + E[X | \text{1st is Failure}] \cdot q$
    
    $c = (1) \cdot p + (1+c) \cdot q$
    
    
    $c = p + q + cq$

    $c = (p+q) + cq$

    $c = 1 + cq$

    $c - cq = 1$
    
    $c(1-q) = 1$
    
    $c(p) = 1 \implies c = \mathbf{1/p}$.
    

#### 7. Proof: Expectation of a Negative Binomial(r, p) RV

- **Story:** $X \sim NegBin(r, p)$ is the total number of trials to get $r$ successes.
    
- **Indicators (or, sum of RVs):** We can think of $X$ as the sum of $r$ independent Geometric RVs.
    
    - $X_1$ = trials to get the 1st success. $X_1 \sim Geo(p)$.
        
    - $X_2$ = _additional_ trials to get the 2nd success (after the 1st). $X_2 \sim Geo(p)$.
        
    - ...
        
    - $X_r$ = _additional_ trials to get the $r$-th success (after the $r-1$-th). $X_r \sim Geo(p)$.
        
- $X = X_1 + X_2 + \dots + X_r$.
    
- Linearity of Expectation:
    
    $E[X] = E[X_1] + E[X_2] + \dots + E[X_r]$
    
    $E[X] = (1/p) + (1/p) + \dots + (1/p)$ ($r$ times)
    
    $E[X] = \mathbf{r/p}$.
    

#### 8. Problem (Hypergeometric): Expected women on committee

- **Setup:** $N=18$ people total. $K=8$ women. $n=5$ chosen for committee.
    
- Let $X$ = number of women on the committee. $X \sim HyperGeo(n=5, K=8, N=18)$.
    
- We _could_ use the Hypergeometric PMF, but it's terrible. Let's use indicators.
    
- Let $I_j$ be an indicator for the $j$-th person on the committee being a woman.
    
    Wait, that's hard. Let's try a different set of indicators.
    
- Let's label the 18 people: $W_1, \dots, W_8$ (women) and $M_1, \dots, M_{10}$ (men).
    
- Let $I_j$ be an indicator that $W_j$ (the $j$-th woman) is on the committee. (for $j=1 \dots 8$)
    
- $X = I_1 + I_2 + \dots + I_8$. (The total # of women on the committee is the sum of these indicators).
    
- **Linearity:** $E[X] = \sum_{j=1}^{8} E[I_j]$.
    
- **Expectation:** $E[I_j] = P(I_j=1) = P(\text{Woman } j \text{ is on the committee})$.
    
- What's the probability Woman $j$ is chosen? She is 1 person. There are $\binom{18}{5}$ total committees.
    
- Number of committees _with_ Woman $j$ is $\binom{1}{1} \cdot \binom{17}{4}$ (we pick her, and 4 others from the remaining 17).
    
- $P(I_j=1) = \frac{\binom{17}{4}}{\binom{18}{5}} = \frac{17! \cdot 5! \cdot 13!}{4! \cdot 13! \cdot 18!} = \frac{17! \cdot 5 \cdot 4! \cdot 13!}{4! \cdot 13! \cdot 18 \cdot 17!} = \frac{5}{18}$.
    
- **Intuition check:** A random person has a $5/18$ chance of being on a 5-person committee. This makes sense.
    
- **Final Answer:** $E[X] = \sum_{j=1}^{8} (5/18) = 8 \cdot (5/18) = 40/18 = \mathbf{20/9} \approx 2.22$.
    

#### 9. Problem (St. Petersburg Paradox):

- Let $Y$ be the payout. $Y = 2^k$ with probability $P(X=k)$, where $X$ is the number of flips.
    
- $P(X=k)$ means $k-1$ tails, then 1 head. $P(X=k) = (1/2)^{k-1} \cdot (1/2) = (1/2)^k$.
    
- **Expectation:** $E[Y] = \sum_{k=1}^{\infty} y_k \cdot P(X=k)$
    
- $E[Y] = \sum_{k=1}^{\infty} 2^k \cdot (1/2)^k = \sum_{k=1}^{\infty} 1$
    
- $E[Y] = 1 + 1 + 1 + \dots = \mathbf{\infty}$.
    
- **Conclusion:** The expected payout is infinite. Therefore, theoretically, any finite price $C$ is "fair" (you'd be +EV). This paradox shows a limitation of using _only_ expected value to make decisions, as no rational person would pay $1,000,000 to play this game.
    

---

### Section 2: Variance & Poisson

#### 10. Proof: The "Variance Shortcut" $Var(X) = E[X^2] - (E[X])^2$

- **Def:** $Var(X) = E[(X - \mu)^2]$, where $\mu = E[X]$.
    
- Expand the square:
    
    $Var(X) = E[X^2 - 2\mu X + \mu^2]$
    
- Linearity of Expectation:
    
    $Var(X) = E[X^2] - E[2\mu X] + E[\mu^2]$
    
- Constants come out: $2\mu$ and $\mu^2$ are constants, not random variables.
    
    $Var(X) = E[X^2] - 2\mu E[X] + \mu^2$
    
- Substitute $E[X] = \mu$:
    
    $Var(X) = E[X^2] - 2\mu (\mu) + \mu^2$
    
    $Var(X) = E[X^2] - 2\mu^2 + \mu^2$
    
    $Var(X) = E[X^2] - \mu^2$
    
- **Final:** $Var(X) = \mathbf{E[X^2] - (E[X])^2}$.
    

#### 11. Proof: Variance of a Bernoulli(p) RV

- Let $X \sim Bern(p)$. We know $E[X] = p$.
    
- We need $E[X^2]$.
    
- $E[X^2] = \sum x^2 \cdot P(X=x) = (1^2 \cdot p) + (0^2 \cdot q) = 1 \cdot p + 0 = p$.
    
- **Shortcut:** $Var(X) = E[X^2] - (E[X])^2$
    
- $Var(X) = p - p^2 = p(1-p) = \mathbf{pq}$.
    

#### 12. Proof: Variance of a Binomial(n, p) RV

- **Method:** Use $X = I_1 + \dots + I_n$ where $I_j$ are i.i.d. $Bern(p)$ trials.
    
- **Variance of a Sum:** For _independent_ RVs, $Var(X_1 + \dots + X_n) = Var(X_1) + \dots + Var(X_n)$.
    
- $Var(X) = Var(I_1 + \dots + I_n)$
    
- $Var(X) = Var(I_1) + \dots + Var(I_n)$
    
- From (11), we know $Var(I_j) = pq$ for all $j$.
    
- $Var(X) = pq + pq + \dots + pq$ ($n$ times)
    
- $Var(X) = \mathbf{npq}$.
    

#### 13. Proof: Expectation of a Poisson($\lambda$) RV

- **Def:** $P(X=k) = \frac{e^{-\lambda} \lambda^k}{k!}$ for $k=0, 1, 2, \dots$
    
- **Expectation:** $E[X] = \sum_{k=0}^{\infty} k \cdot \frac{e^{-\lambda} \lambda^k}{k!}$
    
- The $k=0$ term is 0.
    
    $E[X] = \sum_{k=1}^{\infty} k \cdot \frac{e^{-\lambda} \lambda^k}{k!}$
    
- Identity Trick: $k/k! = k/(k \cdot (k-1)!) = 1/(k-1)!$
    
    $E[X] = \sum_{k=1}^{\infty} \frac{e^{-\lambda} \lambda^k}{(k-1)!}$
    
- Pull $e^{-\lambda}$ and $\lambda$ outside:
    
    $E[X] = \lambda e^{-\lambda} \sum_{k=1}^{\infty} \frac{\lambda^{k-1}}{(k-1)!}$
    
- Change of Variables: Let $j = k-1$. When $k=1, j=0$.
    
    $E[X] = \lambda e^{-\lambda} \sum_{j=0}^{\infty} \frac{\lambda^j}{j!}$
    
- The sum is the Taylor series for $e^\lambda$.
    
    $E[X] = \lambda e^{-\lambda} (e^\lambda) = \mathbf{\lambda}$.
    

#### 14. Proof: Variance of a Poisson($\lambda$) RV

- We know $E[X] = \lambda$. We need $E[X^2]$.
    
- It's hard to find $E[X^2]$ directly. Let's find $E[X(X-1)]$ first.
    
- $E[X(X-1)] = \sum_{k=0}^{\infty} k(k-1) \cdot \frac{e^{-\lambda} \lambda^k}{k!}$
    
- The $k=0$ and $k=1$ terms are 0.
    
    $E[X(X-1)] = \sum_{k=2}^{\infty} k(k-1) \cdot \frac{e^{-\lambda} \lambda^k}{k!}$
    
- Identity Trick: $k(k-1)/k! = k(k-1)/(k \cdot (k-1) \cdot (k-2)!) = 1/(k-2)!$
    
    $E[X(X-1)] = \sum_{k=2}^{\infty} \frac{e^{-\lambda} \lambda^k}{(k-2)!}$
    
- Pull $e^{-\lambda}$ and $\lambda^2$ outside:
    
    $E[X(X-1)] = \lambda^2 e^{-\lambda} \sum_{k=2}^{\infty} \frac{\lambda^{k-2}}{(k-2)!}$
    
- Change of Variables: Let $j = k-2$. When $k=2, j=0$.
    
    $E[X(X-1)] = \lambda^2 e^{-\lambda} \sum_{j=0}^{\infty} \frac{\lambda^j}{j!} = \lambda^2 e^{-\lambda} (e^\lambda) = \lambda^2$.
    
- Now, $E[X(X-1)] = E[X^2 - X] = E[X^2] - E[X]$.
    
- $E[X^2] = E[X(X-1)] + E[X] = \lambda^2 + \lambda$.
    
- Variance: $Var(X) = E[X^2] - (E[X])^2$
    
    $Var(X) = (\lambda^2 + \lambda) - (\lambda)^2 = \mathbf{\lambda}$.
    

#### 15. Problem (Poisson Approx.): Typos in a book

- This is a Binomial problem: $n=1000$ (typos), $p=1/500$ (prob. a given typo lands on our page).
    
- This is a "rare event" scenario. We can approximate with Poisson.
    
- Let $X$ = # of typos on our page.
    
- $\lambda = np = 1000 \cdot (1/500) = 2$.
    
- So, $X \sim Pois(\lambda=2)$.
    
- We want $P(X \ge 3)$. It's easier to find the complement.
    
- $P(X \ge 3) = 1 - P(X < 3) = 1 - [P(X=0) + P(X=1) + P(X=2)]$
    
- $P(X=0) = \frac{e^{-2} 2^0}{0!} = e^{-2}$
    
- $P(X=1) = \frac{e^{-2} 2^1}{1!} = 2e^{-2}$
    
- $P(X=2) = \frac{e^{-2} 2^2}{2!} = \frac{4e^{-2}}{2} = 2e^{-2}$
    
- $P(X \ge 3) = 1 - (e^{-2} + 2e^{-2} + 2e^{-2}) = 1 - 5e^{-2}$.
    
- Using $e^{-2} \approx 0.135$:
    
    $P(X \ge 3) \approx 1 - 5(0.135) = 1 - 0.675 = \mathbf{0.325}$.
    

#### 16. Problem (Variance): $X \sim Bin(100, 1/2)$

- **Mean:** $E[X] = np = 100 \cdot (1/2) = 50$.
    
- **Variance:** $Var(X) = npq = 100 \cdot (1/2) \cdot (1/2) = 25$.
    
- **Standard Deviation:** $SD(X) = \sqrt{Var(X)} = \sqrt{25} = 5$.
    
- One SD from mean: We want the probability $X$ is between $(\mu - \sigma)$ and $(\mu + \sigma)$.
    
    $P(50 - 5 \le X \le 50 + 5) = P(45 \le X \le 55)$.
    
- This is a Binomial sum. But since $n$ is large, we can use the **Normal Approximation**.
    
- $X \approx N(\mu=50, \sigma^2=25)$.
    
- We are _already_ asked for the range $\mu \pm 1\sigma$.
    
- For _any_ Normal distribution, the probability of being within 1 SD of the mean is $\approx \mathbf{0.68}$.
    
- (This is the "68-95-99.7" rule. The problem is just asking for the "68" part.)
    

---

### Section 3: Continuous Variables (Uniform, Exponential, Normal)

#### 17. Proof: Expectation and Variance of a Uniform(a, b) RV

- **Def:** $f(x) = \frac{1}{b-a}$ for $x \in [a, b]$, and $0$ otherwise.
    
- Expectation: $E[X] = \int_{-\infty}^{\infty} x f(x) dx = \int_a^b x \cdot \frac{1}{b-a} dx$
    
    $E[X] = \frac{1}{b-a} \left[ \frac{1}{2}x^2 \right]_a^b = \frac{1}{b-a} \cdot \frac{1}{2} (b^2 - a^2)$
    
    $E[X] = \frac{1}{2(b-a)} (b-a)(b+a) = \frac{\mathbf{b+a}}{\mathbf{2}}$. (The midpoint, as expected).
    
- Variance: First, find $E[X^2]$.
    
    $E[X^2] = \int_a^b x^2 \cdot \frac{1}{b-a} dx = \frac{1}{b-a} \left[ \frac{1}{3}x^3 \right]_a^b$
    
    $E[X^2] = \frac{1}{3(b-a)} (b^3 - a^3) = \frac{1}{3(b-a)} (b-a)(b^2 + ab + a^2) = \frac{b^2 + ab + a^2}{3}$.
    
- $Var(X) = E[X^2] - (E[X])^2$
    
    $Var(X) = \frac{b^2 + ab + a^2}{3} - \left( \frac{b+a}{2} \right)^2$
    
    $Var(X) = \frac{b^2 + ab + a^2}{3} - \frac{b^2 + 2ab + a^2}{4}$
    
    Find common denominator (12):
    
    $Var(X) = \frac{4(b^2 + ab + a^2) - 3(b^2 + 2ab + a^2)}{12}$
    
    $Var(X) = \frac{4b^2 + 4ab + 4a^2 - 3b^2 - 6ab - 3a^2}{12}$
    
    $Var(X) = \frac{b^2 - 2ab + a^2}{12} = \frac{\mathbf{(b-a)^2}}{\mathbf{12}}$.
    

#### 18. Proof: The Memoryless Property of the Exponential Distribution

- Def: $X \sim Expo(\lambda)$. CDF: $P(X \le t) = 1 - e^{-\lambda t}$.
    
    Survival function: $P(X > t) = e^{-\lambda t}$.
    
- **Goal:** Prove $P(X > s+t | X > s) = P(X > t)$.
    
- LHS: By def. of conditional probability:
    
    $P(X > s+t | X > s) = \frac{P( (X > s+t) \cap (X > s) )}{P(X > s)}$
    
- If $X > s+t$, it is automatically also $> s$. So the intersection is just $X > s+t$.
    
    $LHS = \frac{P(X > s+t)}{P(X > s)}$
    
- Plug in the survival function:
    
    $LHS = \frac{e^{-\lambda(s+t)}}{e^{-\lambda s}} = \frac{e^{-\lambda s} e^{-\lambda t}}{e^{-\lambda s}} = e^{-\lambda t}$
    
- **RHS:** $P(X > t) = e^{-\lambda t}$.
    
- Since $LHS = RHS$, the property is proven.
    

#### 19. Problem (Exponential): Bus waiting time

- Let $T$ = time between buses. $T \sim Expo(1/10)$.
    
- Let $W$ = your waiting time.
    
- Because of the **Memoryless Property**, it doesn't matter how long it has been since the _last_ bus. The time until the _next_ bus always has the same $Expo(1/10)$ distribution.
    
- Therefore, your waiting time $W$ also has an $Expo(1/10)$ distribution.
    
- **Answer:** $E[W] = 1/\lambda = 1/(1/10) = \mathbf{10 \text{ minutes}}$.
    

#### 20. Problem (Normal): $X \sim N(10, 9)$

- $X \sim N(\mu=10, \sigma^2=9) \implies \sigma = 3$.
    
- We want $P(X > 13)$. We **standardize** $X$ to $Z \sim N(0, 1)$.
    
- $Z = \frac{X - \mu}{\sigma} = \frac{X - 10}{3}$.
    
- $P(X > 13) = P\left( \frac{X - 10}{3} > \frac{13 - 10}{3} \right)$
    
- $P(X > 13) = P(Z > 3/3) = P(Z > 1)$.
    
- $P(Z > 1) = 1 - P(Z \le 1)$.
    
- Using a $Z$-table, $P(Z \le 1) \approx 0.8413$.
    
- **Answer:** $P(X > 13) = 1 - 0.8413 = \mathbf{0.1587}$.
    

#### 21. Problem (Normal): Linear combination of Normals

- Let $Z_1 \sim N(0, 1)$ and $Z_2 \sim N(0, 1)$ (i.i.d.).
    
- We want the distribution of $Y = 3Z_1 - 2Z_2$.
    
- Rule: A linear combination of independent Normal RVs is also a Normal RV.
    
    $Y \sim N(\mu_Y, \sigma^2_Y)$.
    
- Find $E[Y]$:
    
    $E[Y] = E[3Z_1 - 2Z_2] = 3E[Z_1] - 2E[Z_2]$
    
    $E[Y] = 3(0) - 2(0) = 0$. So $\mu_Y = 0$.
    
- Find $Var(Y)$:
    
    $Var(Y) = Var(3Z_1 - 2Z_2)$
    
    $Var(Y) = Var(3Z_1) + Var(-2Z_2)$ (since they are independent)
    
    $Var(Y) = 3^2 Var(Z_1) + (-2)^2 Var(Z_2)$
    
    $Var(Y) = 9 \cdot Var(Z_1) + 4 \cdot Var(Z_2)$
    
    $Var(Y) = 9(1) + 4(1) = 13$. So $\sigma^2_Y = 13$.
    
- **Answer:** $Y \sim \mathbf{N(0, 13)}$.
    

#### 22. Problem (LOTUS): $U \sim Unif(0, 1)$

- LOTUS (Law of the Unconscious Statistician):
    
    $E[g(X)] = \int_{-\infty}^{\infty} g(x) f_X(x) dx$
    
- Here, $X=U$, $g(U) = e^U$, and $f_U(x) = 1$ for $x \in [0, 1]$.
    
- $E[e^U] = \int_0^1 e^u \cdot 1 du$
    
- $E[e^U] = \left[ e^u \right]_0^1 = e^1 - e^0 = \mathbf{e - 1}$.