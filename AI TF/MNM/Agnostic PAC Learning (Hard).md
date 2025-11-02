> **Sources:**
> 
> - `13. Learning-Theory-7-PAC-AGN.pdf` (Slides 7-50)
>     

Here is an Easier version : [[Agnostic PAC Learning (Easy)]]

The standard [[PAC Learnability (The Formal Definition)|PAC model]] makes a very strong assumption called **realizability**: that the true function $f$ is _inside_ our hypothesis space $H$ (i.e., $f \in H$).

This implies that there _exists_ a hypothesis $h \in H$ with $err_D(h) = 0$, and that it's possible to achieve $err_S(h) = 0$ on the training set.

**Agnostic Learning** is a more realistic and general model that **drops the realizability assumption.**

## The Agnostic Model

- We are "agnostic" about whether $f \in H$. We assume it's probably _not_.
    
- The data may also be _noisy_.
    
- **Consequence:** We can no longer find a _consistent_ hypothesis ($err_S(h) = 0$).
    
- **New Goal:** Instead of finding a _consistent_ $h$, our goal is to find the $h \in H$ that simply has the **lowest empirical error** $err_S(h)$.
    
- **New Question:** We can find the $h$ that is _best_ on the training set $S$. But how do we guarantee that its _true error_ $err_D(h)$ is also low? We need to bound the _difference_ between them.
    

## Generalization Bound for Agnostic Learning

We want to bound how far $err_D(h)$ can be from $err_S(h)$. For this, we use a powerful statistical tool: **Hoeffding's Inequality** (a tail bound).

### Hoeffding's Inequality

Hoeffding's Inequality gives us a bound on how much an _empirical mean_ (from $m$ samples) can differ from the _true mean_ of a random variable.

- **Analogy:** Tossing a coin $m$ times.
    
    - $\overline{p}$ = empirical mean (e.g., `num_heads / m`)
        
    - $p$ = true mean (the coin's true bias, e.g., 0.5)
        
    - Hoeffding's tells us $P(p > \overline{p} + \epsilon) \le e^{-2m\epsilon^2}$.
        
    - The probability that our _observed_ average is "unluckily" much lower than the _true_ average decreases exponentially with the number of samples $m$.
        

### Applying to Learning

We can treat the error of a hypothesis as a coin toss:

- For one hypothesis $h$:
    
    - $err_S(h)$ is the _empirical mean_ of the error (our $\overline{p}$).
        
    - $err_D(h)$ is the _true mean_ of the error (our $p$).
        
- From Hoeffding's, for a _single, fixed_ hypothesis $h$:
    
    $$P(err_D(h) > err_S(h) + \epsilon) \le e^{-2m\epsilon^2}$$

But our learner _searches_ through _all_ hypotheses in $H$. We need to know the probability that _any_ $h \in H$ "fools" us.

- Using the Union Bound (like we did in [[PAC Learning and Occam's Razor]]):
    
    $$P(\exists h \in H \text{ such that } err_D(h) > err_S(h) + \epsilon) \le |H| e^{-2m\epsilon^2}$$

### The Agnostic Sample Complexity Bound

This is the "bad event" we want to avoid. We set this failure probability to be $\le \delta$:

$$|H| e^{-2m\epsilon^2} \le \delta$$

Now, we solve for $m$ (the number of samples needed):

- $e^{-2m\epsilon^2} \le \delta / |H|$
    
- $-2m\epsilon^2 \le \ln(\delta / |H|)$
    
- $2m\epsilon^2 \ge - \ln(\delta / |H|) = \ln(|H| / \delta)$
    
- $m \ge \frac{1}{2\epsilon^2} \left( \ln|H| + \ln(1/\delta) \right)$
    

This is the **sample complexity bound for Agnostic PAC Learning**.

## Agnostic vs. Realizable (Occam) Bound

- **Realizable PAC (Occam's Bound):**
    
    $$m \ge \frac{1}{\epsilon} \left( \ln|H| + \ln(1/\delta) \right)$$
    - Guarantees $err_D(h) \le \epsilon$.
        
- **Agnostic PAC (Hoeffding's Bound):**
    
    $$m \ge \frac{1}{2\epsilon^2} \left( \ln|H| + \ln(1/\delta) \right)$$
    - Guarantees $err_D(h) \le err_S(h_{best}) + \epsilon$.
        
    - This is a "relative" bound. It says our _true error_ will be close to the _best possible training error_.
        

Notice the Agnostic bound depends on $1/\epsilon^2$ instead of $1/\epsilon$. This means we need _significantly more data_ to get the same $\epsilon$ guarantee in the Agnostic model, which makes sense because we're working in a much harder, more realistic setting.

### Check Your Understanding

1. What is the "realizability" assumption? Why is it unrealistic?
    
2. What is the new goal of a learner in the Agnostic model (since it can't find a 0-error hypothesis)?
    
3. What statistical inequality is used to derive the Agnostic bound?
    
4. What is the key difference in the final sample complexity bound for Agnostic learning compared to the standard (realizable) PAC bound? What does this imply about the number of samples needed?