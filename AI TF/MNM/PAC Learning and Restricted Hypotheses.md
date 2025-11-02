> **Sources:**
> 
> - `7.1 Intro to learning handnote-nidhi.pdf` (Pages 9-13)
>     
> - `1. Learning Theory-1.pptx.pdf` (Slide 19)
>     


In our [[PAC Learning (Probably Approximately Correct)]] note, we derived the **sample complexity** required to PAC-learn a hypothesis $h$:

$$N \ge \frac{1}{\epsilon} \left( \ln|\mathcal{H}| + \ln\frac{1}{\delta} \right)$$

This formula is great, but it has a _massive_ practical problem.

## The Problem: The Curse of Expressiveness

- As we found in [[Decision Trees (and the Restaurant Problem)]], the hypothesis space $\mathcal{H}_{DT}$ for Boolean decision trees is _huge_.
    
- For $n$ attributes, $|\mathcal{H}_{DT}| \ge 2^{2^n}$ (it's actually larger).
    
- If we plug this into the sample complexity formula:
    
    - $\ln|\mathcal{H}_{DT}| = \ln(2^{2^n}) = 2^n \ln(2)$
        
- This means our sample complexity $N$ grows **exponentially** with the number of attributes $n$.
    
- **Conclusion:** The class of _all possible decision trees_ is **not efficiently PAC-learnable**. Just knowing $h$ is consistent isn't enough, because there are too many _other_ consistent hypotheses that could be wrong.
    

## The Solution: Restrict the Hypothesis Space

(From `1. Learning Theory-1.pptx.pdf`, Slide 19) The only way to make learning efficient is to use our _prior knowledge_ or [[Occam's Razor]] to **restrict** $\mathcal{H}$ to a smaller, "learnable" subset of functions.

## Example: $\mathcal{H} = \text{Conjunctions of Literals}$


Let's _not_ allow all possible trees. Let's decide (based on prior knowledge) that the true function $f$ is probably just a **conjunction of literals** (an "AND" statement).

- **Examples of** $h$ **in this** $\mathcal{Such}$**:**
    
    - $h_1 = (x_1 \land x_2 \land x_3)$
        
    - $h_2 = (\neg x_1 \land x_4)$
        
    - $h_3 = (x_2)$
        

**How big is this new, restricted** $\mathcal{H}$**?**

- For each variable $x_i$ (out of $n$ total variables), we have 3 choices:
    
    1. Include it positively (e.g., $x_i$)
        
    2. Include it negatively (e.g., $\neg x_i$)
        
    3. Don't include it in the conjunction at all.
        
- Therefore, the total size of this hypothesis space is $|\mathcal{H}_{\text{conj}}| = 3 \times 3 \times \dots \times 3 = 3^n$.
    

**What is the new sample complexity?**

- Let's plug $|\mathcal{H}_{\text{conj}}| = 3^n$ into the PAC formula:
    
    - $N \ge \frac{1}{\epsilon} \left( \ln(3^n) + \ln\frac{1}{\delta} \right)$
        
    - $N \ge \frac{1}{\epsilon} \left( n \ln 3 + \ln\frac{1}{\delta} \right)$
        
- **The Result:** The sample complexity $N$ is now **linear** in $n$ (the number of attributes).
    
- **Conclusion:** The class of "conjunctions" **is efficiently PAC-learnable**.
    

This is the theoretical justification for why we prefer _simpler models_. By restricting $\mathcal{H}$ (e.g., using a linear model instead of a neural net, or a small tree instead of a large one), we dramatically reduce the number of examples needed to find a hypothesis that will _probably generalize_.

### Check Your Understanding

1. Why is the class of _all_ Boolean functions not efficiently PAC-learnable?
    
2. What does restricting $\mathcal{H}$ mean? Give an example.
    
3. Why does restricting $\mathcal{H}$ from $2^{2^n}$ to $3^n$ make such a huge difference in the sample complexity $N$?