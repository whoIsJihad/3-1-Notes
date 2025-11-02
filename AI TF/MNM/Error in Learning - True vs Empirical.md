> **Sources:**
> 
> - `8. Learning-Theory-2-UT-GN.pdf` (Slides 33-38)
>     

# Error in Learning: True vs. Empirical

To formalize [[Model Selection and Generalization (Bias-Variance)|overfitting]] and understand [[PAC Learning (Probably Approximately Correct)|PAC learning]], we must distinguish between two different types of error.

We assume all examples (training and future) are drawn from a fixed, unknown **data distribution** $D$ over the instance space $X$.

## 1. True Error (or Generalization Error)

$err_D(h)$

- **Definition:** The **True Error** of a hypothesis $h$ is the probability that it will misclassify a _new, future example_ $x$ drawn randomly from the _entire distribution_ $D$.
    
- **Formula:** $err_D(h) = Pr_{x \sim D}[h(x) \neq f(x)]$
    
- **What it means:** This is the _real_ error we care about. It measures how well our hypothesis $h$ generalizes to the world.
    
- **The Problem:** We can _never_ know the true error, because we don't have access to the full distribution $D$ (or the true function $f$). We can only _estimate_ it.
    

In this diagram, the instance space is $X$. The true function $f$ labels the blue circle as positive. Our hypothesis $h$ labels the light-blue-faded circle as positive. The **True Error** $err_D(h)$ is the probability of an example falling into the two crescent-moon-shaped "disagreement" regions (the symmetric difference).

## 2. Empirical Error (or Training Error)

$err_S(h)$

- **Definition:** The **Empirical Error** of a hypothesis $h$ is the fraction of examples _in the training set_ $S$ that it misclassifies.
    
- **Formula:** $err_S(h) = \frac{1}{|S|} \sum_{x \in S} [h(x) \neq f(x)]$
    
- **What it means:** This is the error we can _actually measure_. It tells us how well our hypothesis fits the data we _have_. We often drive this error to 0.
    

## The Formal Definition of Overfitting

(From `8. Learning-Theory-2-UT-GN.pdf`, Slide 38)

With these two definitions, we can now formally define overfitting.

A hypothesis $h$ is **overfitting** the training data if there is _another_ hypothesis $h'$ such that:

1. $err_S(h) < err_S(h')$ (Our hypothesis $h$ has a _lower_ training error than $h'$).
    
2. $err_D(h) > err_D(h')$ (Our hypothesis $h$ has a _higher_ true generalization error than $h'$).
    

In simple terms: $h$ **"looks" better on the training data, but is "actually" worse in the real world.** This is the central problem that techniques like [[Decision Trees: Overfitting and Pruning|pruning]] and [[Occam's Razor]] are designed to solve.

### Check Your Understanding

1. Why can we never calculate the True Error $err_D(h)$?
    
2. If a model $h$ gets 100% accuracy on the training set, what is its Empirical Error $err_S(h)$?
    
3. Does $err_S(h) = 0$ _guarantee_ that $err_D(h) = 0$? Why or why not?