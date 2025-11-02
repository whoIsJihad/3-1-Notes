> **Sources:**
> 
> - `2. Learning-1.pptx.pdf` (Slides 16-17)
>     
> - `2.1 Learning from examples note nidhi.pdf` (Pages 16-17)
>     

# Model Selection and Generalization (The Bias-Variance Trade-off)

The ultimate goal of learning is **Generalization**: how well our hypothesis $h$ performs on new, unseen examples (the **test set**).

- **Training Error:** The error (or loss) our hypothesis $h$ makes on the **training set**.
    
- **Generalization Error:** The _expected_ error $h$ will make on the **test set**. This is what we _really_ care about.
    

Finding a model with low generalization error requires balancing two competing forces: **bias** and **variance**.

### 1. Underfitting (High Bias)

- **What it is:** The model is **too simple** to capture the underlying pattern in the data. The [[Hypothesis Space]] $\mathcal{H}$ might not even contain a good approximation of the true function $f$.
    
- **Example:** Trying to fit a straight line (linear model) to data that is clearly U-shaped (quadratic).
    
- **Symptoms:**
    
    - **High Training Error**
        
    - **High Generalization Error**
        
- This model has **high bias** (it's "biased" towards a simple, wrong shape) and **low variance** (it doesn't change much even if you give it different training sets, because it's going to be wrong in the same way every time).
    

### 2. Overfitting (High Variance)

- **What it is:** The model is **too complex** and has started to fit the _random noise_ in the training data, not just the underlying signal.
    
- **Example:** Using a 12th-degree polynomial to fit 13 data points. The line will wiggle and weave to hit every single point _exactly_, but it will be wildly wrong for any new point in between. (From `handwritten_notes.pdf`, Page 15, 17)
    
- **Symptoms:**
    
    - **Very Low Training Error** (it has "memorized" the training set)
        
    - **Very High Generalization Error** (it fails to predict new data)
        
- This model has **low bias** (it's flexible enough to fit the training data perfectly) and **high variance** (the specific shape of the wiggles depends _heavily_ on the _exact_ training points it saw).
    

### The "Sweet Spot"

As shown in the graph (from `Learning-1.pptx.pdf`, Slide 17), the goal is to find the **optimal capacity** (model complexity) where the total generalization error (the sum of bias and variance) is at its minimum. This is often _not_ the point where training error is zero.

### Check Your Understanding

1. Draw the bias-variance trade-off graph and label the underfitting zone, overfitting zone, bias, variance, training error, and generalization error curves.
    
2. If your model has 99.9% accuracy on the training set but 50% accuracy on the test set, what problem are you suffering from?
    
3. Why does a simple model (like a linear one) typically have high bias but low variance?