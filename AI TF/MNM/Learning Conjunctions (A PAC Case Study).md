> **Sources:**
> 
> - `8. Learning-Theory-2-UT-GN.pdf` (Slides 9-12)
>     

# Learning Conjunctions (A PAC Case Study)

This note explores a concrete example of [[PAC Learning (Probably Approximately Correct)]] to build intuition about how our learned hypothesis $h$ can differ from the true function $f$ and still be "good enough."

## The Scenario

- **Instance Space** $X$**:** $n$-bit boolean vectors (e.g., $n=100$).
    
- **True Function** $f$**:** A hidden conjunction. Let's say the _true function_ is: $f = x_2 \land x_3 \land x_4 \land x_5 \land x_{100}$
    
- **Hypothesis Space** $\mathcal{H}$**:** The set of all possible conjunctions on $n$ variables.
    
- **Learning Algorithm:** An "elimination" algorithm. We start with the most specific hypothesis $h = (x_1 \land \neg x_1 \land x_2 \land \neg x_2 ...)$ and broaden it by removing literals that contradict positive examples. A simpler way: start with $h$ containing all literals, and remove any literal that is `False` in a positive example.
    
    - A common algorithm: Start with $h = (x_1 \land x_2 \land \dots \land x_n)$. When you see a positive example, remove any $x_i$ from $h$ that was 0 in that example.
        

## The Training Data

We get a batch of random examples, labeled by $f$:

- $<(1, 1, 1, 1, 1, 1, ..., 1, 1), 1>$
    
- $<(1, 1, 1, 0, 0, 0, ..., 0, 0), 0>$
    
- $<(1, 1, 1, 1, 1, 0, ..., 0, 1), 1>$
    
- $<(1, 0, 1, 1, 1, 0, ..., 0, 1), 0>$
    
- ...
    

Notice a pattern? In all the positive examples we've seen, $x_1$ _happens_ to be 1. Our elimination algorithm, which only sees positive examples like:

- $<(**1**, 1, 1, 1, 1, ..., 1)> \to +1$
    
- $<(**1**, 1, 1, 1, 1, ..., 1)> \to +1$
    

...will _never_ have a reason to remove $x_1$ from its conjunction.

## The Result

- **True Function:** $f = x_2 \land x_3 \land x_4 \land x_5 \land x_{100}$
    
- **Learned Hypothesis:** $h = x_1 \land x_2 \land x_3 \land x_4 \land x_5 \land x_{100}$
    

Our learned hypothesis $h$ is **wrong**. It's _more specific_ than the true function $f$. It includes the irrelevant variable $x_1$.

**Is this a failure?**

- In one sense, yes. We didn't find $f$.
    
- In the PAC sense, **probably not**.
    

The only time $h$ and $f$ will disagree is on an example $x$ where:

- $x_1 = 0$
    
- ...and $x_2, x_3, x_4, x_5, x_{100}$ are _all_ 1.
    

The reason we _learned_ this wrong $h$ is that we _never saw_ an example like that. The PAC argument is that if such examples are **rare** (have a low probability $Pr(x)$ in the data distribution $D$), then the error we make on them will be small.

Our hypothesis $h$ is "probably" (with high confidence $1-\delta$) "approximately correct" (with small error $\epsilon$) because the "region of disagreement" is very small. We never saw a positive example with $x_1=0$, so the probability of such an example appearing in the future is likely low (or at least, bounded).

### Check Your Understanding

1. In this scenario, is $h$ consistent with all the training data?
    
2. Describe, in plain English, the _only_ kind of example on which $h$ and $f$ will disagree.
    
3. How does this example build intuition for the "Probably" part of PAC learning?