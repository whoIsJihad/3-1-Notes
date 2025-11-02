

_Source: `14. Learning-Theory-8-PAC-VC.pdf` (Pages 75, 76, 77)_

Once we have the [[VC Dimension (VCD)|VC Dimension]], we can substitute it into our PAC bounds, effectively replacing the $ln(|H|)$ term. This finally gives us sample complexity bounds that work for [[Infinite Hypothesis Spaces]].

The $VC(H)$ behaves _like_ $log(|H|)$ for the purposes of these bounds.

## 1. Bound for Realizable Case (Consistent Learners)

This is the new "Occam's Razor" bound for infinite $H$.

> Given a sample $D$ with $m$ examples, if a learner finds a consistent $h \in H$:
> 
> If $m > \frac{1}{\epsilon} (8 VC(H) log(\frac{13}{\epsilon}) + 4 log(\frac{2}{\delta}))$
> 
> Then with probability at least $1-\delta$, $h$ has $err_D(h) < \epsilon$.

The key takeaway is that the number of samples $m$ grows **linearly with** $VC(H)$.

## 2. Bound for Agnostic Learning

This is the new bound for the [[Agnostic Learning|agnostic]] case.

> With $m$ examples, with probability at least $1-\delta$, _any_ hypothesis $h \in H$ will have its true error bounded by:
> 
> $err_D(h) \le err_S(H) + \sqrt{\frac{VC(H)(ln(\frac{2m}{VC(H)})+1) + ln(\frac{4}{\delta})}{m}}$

### Interpretation

- $err_D(h)$: The true generalization error.
    
- $err_S(h)$: The observed training error.
    
- **The** $\sqrt{...}$ **term**: This is the "complexity penalty" or "generalization gap." It's the amount by which our training error might be "lying" to us.
    

This bound shows that as our **sample size (**$m$**) increases**, the gap between true error and training error shrinks (proportional to $\frac{1}{\sqrt{m}}$).

Crucially, if a hypothesis space $H$ has an **infinite VC Dimension** (like 1-Nearest-Neighbor), these bounds become meaningless (they go to infinity). An infinite VC dimension means the hypothesis space is **not PAC-learnable**.

### ❓ Review Questions

1. In the new sample complexity bounds, what term does $VC(H)$ replace from the original bounds for finite spaces?
    
2. In the agnostic bound, what happens to the "generalization gap" as $m$ (sample size) gets very large?
    
3. What does it mean if $VC(H) = \infty$? Is this good or bad?