> **Sources:**
> 
> - `2. Learning-1.pptx.pdf` (Slide 19)
>     
> - `2.1 Learning from examples note nidhi.pdf` (Pages 19-20)
>     

# Occam's Razor

**Occam's Razor** is a philosophical and scientific principle that provides a powerful guide for [[Model Selection and Generalization (Bias-Variance)|model selection]].

> **The Principle:** "When faced with two hypotheses that explain the data equally well, always choose the simpler one."

(Originally, "Entities should not be multiplied beyond necessity.")

## Application in Machine Learning

How do we apply this?

- **Scenario:** Look at the data in Figure 18.1(a) (from `handwritten_notes.pdf`, Page 20). The points lie almost perfectly on a line.
    
- **Hypothesis 1 (Simple):** A linear function $h_1(x) = w_1x + w_0$. This $h_1$ is a _best-fit_ line and has a small amount of error on each point.
    
- **Hypothesis 2 (Complex):** A 7th-degree polynomial $h_2(x) = \sum_{i=0}^{7} w_i x^i$. This $h_2$ can be made to be _perfectly consistent_ (zero error) by wiggling to hit every single point. (See Figure 18.1(b) for an example).
    
- **The Problem:** Both hypotheses "explain the data well" (in fact, $h_2$ explains it _perfectly_). Which do we choose?
    
- **Occam's Razor Says:** Choose $h_1$, the linear function.
    
- **The Justification:** The complex hypothesis $h_2$ is almost certainly [[Model Selection and Generalization (Bias-Variance)|overfitting]] to the _noise_ in the data. The simpler hypothesis $h_1$ is far more likely to have captured the _true, underlying pattern_ and will therefore **generalize** better to new data.
    

Defining "simplicity" is not always easy, but in this case, a 1st-degree polynomial is clearly "simpler" than a 7th-degree one. This principle is a defense against overfitting.

This idea can be formalized mathematically using [[Bayesian Learning (MAP)]].

### Check Your Understanding

1. Why does Occam's Razor help prevent overfitting?
    
2. If a complex, 10th-degree polynomial and a simple, 2nd-degree polynomial _both_ have high generalization error on a dataset, can Occam's Razor help you choose? (Hint: Think about underfitting).
    
3. How might you define "simplicity" for a [[Decision Trees (and the Restaurant Problem)|Decision Tree]]?