> **Sources:**
> 
> - `8. Learning-Theory-2-UT-GN.pdf` (Slides 13-15)
>     

# Mistake Bound Learning

**Mistake Bound Learning** is a theoretical framework for analyzing [[Online vs. Batch Learning|Online Learning]] algorithms.

Unlike [[PAC Learning (Probably Approximately Correct)|PAC learning]], which measures success with a probabilistic _error rate_ $\epsilon$, the Mistake Bound model measures success by a _deterministic count_ of the total number of mistakes an algorithm will _ever_ make.

## The Model

- The setup is the [[Online vs. Batch Learning|Online model]].
    
- Learning is a sequence of trials.
    
- The algorithm _only_ updates its hypothesis when it makes a mistake.
    
- **Goal:** Can we find a learning algorithm $A$ and a hypothesis space $\mathcal{H}$ such that $A$ is guaranteed to make a _finite_ number of mistakes, no matter what (even adversarial) sequence of examples it is shown?
    

## The Mistake Bound

A learning algorithm $A$ has a **Mistake Bound** $M$ if, for _any_ sequence of examples, it is guaranteed to make at most $M$ mistakes before it converges to a hypothesis $h$ that is consistent with all future examples.

This is a very strong guarantee. It's not probabilistic. It's an absolute upper bound on the number of times the algorithm will be wrong.

### Strength and Weakness

- **Strength:** This model makes **no assumptions** about the order or distribution of training examples. The data can be actively malicious, and the bound $M$ _still_ holds.
    
- **Weakness:** Because it makes no assumptions, it doesn't answer the PAC question: "After $N$ examples, how well will this do on _future_ data?" It only answers: "How many mistakes will it make _in total_?"
    

### Example: Learning Conjunctions (Halving Algorithm)

- **Problem:** Learn a conjunction from $\mathcal{H}_{\text{conj}}$ (like $x_1 \land \neg x_3 \land x_4$).
    
- **Algorithm:**
    
    1. Start with the most general hypothesis: $h = (x_1 \land \neg x_1 \land x_2 \land \neg x_2 \dots)$, which is always `False`. (A better way: start with $h$ = $x_1 \land \dots \land x_n$).
        
    2. When a **positive example** $x$ is seen:
        
        - If $h(x)$ is `False` (a **mistake**), update $h$ by removing any literal from $h$ that is _not_ in $x$.
            
    3. When a **negative example** $x$ is seen:
        
        - If $h(x)$ is `True` (a **mistake**), you have a problem (the simple algorithm breaks, but more complex ones can handle this).
            

The **Halving Algorithm** is a more general version of this. It maintains a set of _all_ consistent hypotheses. When it makes a mistake, it removes _all_ hypotheses that made that mistake. It can be proven that in the worst case, this algorithm will make at most $\log_2(|\mathcal{H}|)$ mistakes.

### Check Your Understanding

1. What is the key difference between the _goal_ of PAC learning and the _goal_ of Mistake Bound learning?
    
2. If an algorithm has a mistake bound of $M=10$, what does that mean?
    
3. Why is the Mistake Bound model considered "stronger" in its assumptions about data than the PAC model?