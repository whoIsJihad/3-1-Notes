> **Sources:**
> 
> - `2. Learning-1.pptx.pdf` (Slides 12-15, 22)
>     
> - `2.1 Learning from examples note nidhi.pdf` (Pages 11-13, 15, 31-32)
>     

# Hypothesis Space ($\mathcal{H}$)

The **Hypothesis Space (**$\mathcal{H}$**)** is the set of all possible functions (hypotheses) that the learning algorithm is allowed to choose from to approximate the true function $f$.

The choice of $\mathcal{H}$ is one of the most important decisions a machine learning engineer makes.

- **Example 1:** If we are doing **Linear Regression**, $\mathcal{H}$ is the set of all possible linear functions $h(x) = w_1x + w_0$. The learning algorithm's job is to find the best parameters $(w_1, w_0)$ from this infinite space.
    
- **Example 2:** If we are fitting a 12-degree polynomial, $\mathcal{H}$ is the set of all functions $h(x) = \sum_{i=0}^{12} w_i x^i$.
    
- **Example 3:** For [[Decision Trees (and the Restaurant Problem)|Decision Trees]], $\mathcal{H}$ is the set of all possible trees we can build using the given attributes.
    

## How to Choose a Hypothesis Space?

- **Prior Knowledge:** If we have a good reason to believe the underlying relationship is linear (e.g., from physics), we should choose a linear $\mathcal{H}$.
    
- **Exploratory Data Analysis (EDA):** We can visualize the data (histograms, scatter plots) to get a feel for its shape. If a scatter plot looks like a line, we'd start with a linear $\mathcal{H}$.
    

## Consistency vs. Best-Fit

Once we have our data $D$ and hypothesis space $\mathcal{H}$, what makes a "good" $h$?

- **Consistent Hypothesis:** A hypothesis $h$ is **consistent** with the data if it perfectly matches every example: $h(x_i) = y_i$ for all $(x_i, y_i) \in D$. This is often the goal in (noiseless) classification.
    
- **Best-Fit Hypothesis:** In regression (or noisy classification), a perfectly consistent $h$ might not exist or might be undesirable (see [[Model Selection and Generalization (Bias-Variance)|Overfitting]]). Instead, we seek a $h$ that is **"closest"** to the data, e.g., one that minimizes the sum of squared errors.
    

## Expressiveness

- **Expressiveness** (or "capacity") describes how rich, complex, or flexible a hypothesis space is. It measures how many different functions $\mathcal{H}$ can represent.
    
- A linear model (`h(x) = w_1x + w_0`) has **low expressiveness**. It can _only_ represent lines.
    
- A deep neural network has **very high expressiveness**. It can approximate almost any continuous function.
    

### The Expressiveness vs. Complexity Trade-off

This is a fundamental trade-off in machine learning. (From `handwritten_notes.pdf`, Page 32)

- **Pro (Good Approximation):** A more expressive $\mathcal{H}$ is more likely to contain a function $h$ that is a good approximation of the (potentially complex) true function $f$.
    
- **Con (High Complexity):**
    
    1. **Search Problem:** Finding the "best" $h$ in a huge space is computationally harder.
        
    2. **Overfitting Problem:** A highly expressive $\mathcal{H}$ is more likely to produce a hypothesis that fits the _noise_ in the training data, leading to poor generalization. This is explored in [[Model Selection and Generalization (Bias-Variance)]].
        

### Check Your Understanding

1. Explain what $\mathcal{H}$ would be for a 3rd-degree polynomial regressor.
    
2. Look at Figure 18.1(a) in the slides (a set of points on a line). Is a 7th-degree polynomial _consistent_ with this data? Is it a _good_ hypothesis? Why or why not? (Hint: See [[Occam's Razor]])
    
3. Why don't we always use the most expressive hypothesis space possible, like a giant neural network?