> **Sources:**
> 
> - `6. decision-trees-discussion nidhi.pdf` (Slides 14-33)
>     



We've seen in [[Model Selection and Generalization (Bias-Variance)]] that **overfitting** is a central problem in machine learning. It happens when a model is too complex and fits the _noise_ in the training data, rather than the true underlying pattern.

Decision trees are _extremely_ prone to overfitting. Because their [[Hypothesis Space]] is so expressive, the [[The ID3 Algorithm|ID3 algorithm]] can (and will) grow a tree that is 100% consistent with the training data, even if that data is noisy or contains irrelevant attributes.

## Example: Overfitting to Noise

(From `6. decision-trees-discussion nidhi.pdf`, Slide 27)

- **The Problem:** We're trying to learn a simple function like $Y = X_0$. All other attributes ($X_1, ..., X_n$) are irrelevant.
    
- **The Data:** The training data is _noisy_. The $Y$ values are randomly flipped with 25% probability.
    
- **The Result:**
    
    - The ID3 algorithm will achieve **100% training accuracy**. It will keep splitting on irrelevant attributes ($X_1, X_2$, etc.) to create complex rules that _perfectly_ model the _noise_ it saw in the training set.
        
    - The **test accuracy will be terrible** (around 62.5% in this example) because this complex, "memorized" tree does not generalize at all.
        
- This is the _definition_ of overfitting:
    
    - $error_{train}(h) \approx 0$
        
    - $error_{test}(h) >> 0$
        

As the graph from the lecture (Slide 30) shows, as the tree size (number of nodes) increases, training accuracy keeps going up, but test accuracy peaks and then _drops_.

## How to Avoid Overfitting

We need to stop the tree from becoming overly complex. There are two main strategies:

### 1. Pre-pruning (Early Stopping)

Stop growing the tree _before_ it becomes fully grown.

- **Method 1: Fix Depth:** Simply limit the tree to a maximum depth (e.g., `max_depth=5`). A tree with depth 1 is called a "decision stump."
    
- **Method 2: Use a Validation Set:** Split your training data into a `train_set` and a `validation_set`.
    
    - Grow the tree using `train_set`.
        
    - At each step, _before_ adding a new split, check if that split _improves_ the accuracy on the `validation_set`.
        
    - If the validation accuracy _decreases_, stop growing that branch (i.e., make it a leaf node with the majority vote).
        

### 2. Post-pruning (Pruning)

This is the more common and often more effective approach.

- **Step 1:** Grow the _full, overfit_ decision tree (the one with 100% training accuracy).
    
- **Step 2:** Use a `validation_set` to "prune" the tree back.
    
- **Algorithm (Reduced-Error Pruning):**
    
    - Start from the bottom of the tree.
        
    - For each internal node:
        
        1. _Temporarily_ "prune" it: remove the subtree below it and replace it with a leaf node (with the majority label of the examples that reached it).
            
        2. Measure the accuracy of this new, _simpler_ tree on the **validation set**.
            
        3. If the pruned tree's accuracy on the validation set is _the same or better_ than the original tree's, then **keep the prune**.
            
    - Repeat this process until no more prunes improve validation accuracy.
        

### Check Your Understanding

1. Why is a 100% accurate decision tree on the training data often a _bad_ sign?
    
2. What is the main difference between pre-pruning and post-pruning?
    
3. What is a "validation set" and what is its role in pruning? Why can't we just use the _test set_ for pruning? (Hint: Think about data leakage).