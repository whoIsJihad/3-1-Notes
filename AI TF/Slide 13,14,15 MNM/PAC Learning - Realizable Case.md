# PAC Learning - Realizable Case (Occam's Razor)

_Source: `13. Learning-Theory-7-PAC-AGN.pdf` (Page 5, 50)_

This is the standard **Probably Approximately Correct (PAC)** learning model. It operates under a key assumption called **realizability**.

- **Assumption**: The true target function $f$ is _guaranteed_ to be one of the functions in our hypothesis space $H$ (i.e., $f \in H$).
    
- **Learner's Strategy**: Because $f \in H$, it is always possible to find at least one hypothesis $h \in H$ that is **consistent** with all training examples (i.e., has a training error $err_S(h) = 0$).
    
- **The Question**: If we find a consistent $h$, what is the probability that it's "bad" (i.e., has a high _true_ error $err_D(h) > \epsilon$)?
    

## Occam's Razor Bound

This model leads to a sample complexity bound, often called the "Occam's Razor" bound:

> To guarantee that any consistent hypothesis $h$ will have a true error $err_D(h) < \epsilon$ with probability at least $1 - \delta$, we need:
> 
> $m > \frac{1}{\epsilon} (ln(|H|) + ln(\frac{1}{\delta}))$

### Interpretation

- $m$: The number of training examples needed.
    
- $\epsilon$ **(Approximately)**: The maximum _true error_ we are willing to tolerate.
    
- $\delta$ **(Probably)**: The maximum probability that we will be "unlucky" and get a bad sample, leading to a bad $h$.
    
- $ln(|H|)$: The complexity of the hypothesis space. A larger space (more possible functions) requires _more_ data to find the right one.
    

This bound is compared against the [[Agnostic Learning]] bound, which is for the non-realizable case.

### ❓ Review Questions

1. What is the "realizability assumption"?
    
2. If you have two hypothesis spaces, $H_1$ with 100 functions and $H_2$ with 10,000 functions, which one will require more samples according to this bound, and why?
    
3. What happens to this bound if your hypothesis space $H$ is infinite?