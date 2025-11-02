> **Sources:**
> 
> - `2. Learning-1.pptx.pdf` (Slides 20-21)
>     
> - `2.1 Learning from examples note nidhi.pdf` (Pages 26-29)
>     

# Bayesian Learning (MAP)

Instead of just finding _a_ consistent hypothesis (which might be complex and overfit), Bayesian learning provides a way to find the **most probable hypothesis** $h^*$ given the data $D$.

This connects directly to [[Occam's Razor]] by formalizing the idea of "simplicity."

## The Goal: Maximum A Posteriori (MAP)

We want to find the hypothesis $h^*$ that maximizes the **posterior probability**:

$$h^* = \text{argmax}_{h \in \mathcal{H}} P(h | D)$$

(Read as: "Find the $h$ that is most probable, _given_ that we have observed the data $D$.")

## The Derivation

We use **Bayes' Rule** to transform this into something we can actually calculate:

$$P(h | D) = \frac{P(D | h) P(h)}{P(D)}$$

So, our optimization becomes:

$$h^* = \text{argmax}_{h \in \mathcal{H}} \left( \frac{P(D | h) P(h)}{P(D)} \right)$$

Since we are maximizing over $h$, the term $P(D)$ (the probability of the data) is just a constant. We can drop it from the `argmax`:

$$h^* = \text{argmax}_{h \in \mathcal{H}} \underbrace{P(D | h)}_{\text{Likelihood}} \underbrace{P(h)}_{\text{Prior}}$$

## Likelihood vs. Prior

This equation gives us the beautiful trade-off at the heart of modern machine learning:

1. $P(D | h)$ **(Likelihood):**
    
    - "What is the probability of seeing this data $D$, _assuming_ $h$ is the true function?"
        
    - This term favors **goodness-of-fit**. A hypothesis $h$ that fits the data perfectly (i.e., is **consistent**) will have a high likelihood. This term, by itself, would favor complex, overfit models.
        
2. $P(h)$ **(Prior):**
    
    - "What is the probability of $h$ _before_ we've seen any data?"
        
    - This is our **prior belief** about the hypothesis.
        
    - This is how we formally implement **[[Occam's Razor]]**! We can assign a _higher prior probability_ $P(h)$ to "simpler" hypotheses (e.g., linear models) and a _very low prior probability_ to "complex" hypotheses (e.g., 12th-degree polynomials).
        

A **MAP** hypothesis thus balances fitting the data well (high likelihood) with being simple (high prior).

### Check Your Understanding

1. Explain the role of the Likelihood $P(D|h)$ and the Prior $P(h)$ in your own words.
    
2. If you set a uniform prior (i.e., $P(h)$ is the same for all $h$), what does the MAP objective simplify to? (This is called **Maximum Likelihood Estimation (MLE)**).
    
3. How does a low $P(h)$ for complex models help prevent overfitting?