> **Sources:**
> 
> - `2.1 Learning from examples note nidhi.pdf` (Pages 33-34, 38-45)
>     

# Decision Trees

A **Decision Tree** is a [[Hypothesis Space|hypothesis space]] that represents a function as a tree. It is non-parametric and is excellent for classification tasks.

- **Internal Nodes:** Test a single **attribute** (feature).
    
- **Branches:** Correspond to the possible **values** of that attribute.
    
- **Leaf Nodes:** Assign a **classification** (e.g., "Yes" or "No").
    

## Example: The Restaurant Problem

This is a classic AI problem where an agent needs to decide: **"Will I wait for a table?" (Yes/No)**.

The agent has a set of **attributes** (features) to base its decision on:

1. `Alternate`: Is there an alternative restaurant nearby? (T/F)
    
2. `Bar`: Is there a comfortable bar area to wait in? (T/F)
    
3. `Fri/Sat`: Is it Friday or Saturday? (T/F)
    
4. `Hungry`: Am I hungry? (T/F)
    
5. `Patrons`: How many people are in the restaurant? (None, Some, Full)
    
6. `Price`: The price range ($, $$, $$$) ...and so on.
    

A simple (small) decision tree $h$ for this problem might be:

```
Patrons?
  |
  +-- None: No (Don't wait)
  |
  +-- Some: Yes (Wait)
  |
  +-- Full:
       |
       +-- Hungry?
            |
            +-- No: No (Don't wait)
            |
            +-- Yes:
                 |
                 +-- Alternate?
                      |
                      +-- No: Yes (Wait)
                      |
                      +-- Yes: No (Don't wait)
```

This tree represents a single logical function (hypothesis) from the [[Hypothesis Space]] of all possible decision trees.

## Expressiveness of Decision Trees

How expressive is the [[Hypothesis Space]] $\mathcal{H}$ of decision trees?

**A: A decision tree can represent** _**any**_ **Boolean function.**

### Proof / Derivation:

(From `handwritten_notes.pdf`, Page 41-44)

1. A **Boolean function** is any function that takes $n$ Boolean (T/F) inputs and returns a single Boolean (T/F) output.
    
2. Think of the **truth table** for a function with $n$ variables. How many rows does it have?
    
    - For $n=2$ (A, B), it has $2^2 = 4$ rows (00, 01, 10, 11).
        
    - For $n$ variables, it has $2^n$ **rows**.
        
3. Now, for each of those $2^n$ rows (which represent every possible combination of inputs), the function's output $F$ can be _either_ 0 or 1.
    
4. How many different functions can we make?
    
    - Row 1: 2 choices (0 or 1)
        
    - Row 2: 2 choices (0 or 1)
        
    - ...
        
    - Row $2^n$: 2 choices (0 or 1)
        
5. The total number of possible Boolean functions is $2 \times 2 \times ... \times 2$ ($2^n$ times), which is $2^{2^n}$.
    
6. A decision tree can be constructed to represent _any_ of these functions. One (inefficient) way is to build a tree that has one long path to a leaf for every "Yes" row in the truth table. This is the **Disjunctive Normal Form (DNF)**.
    
    - Example: $F = (A \land \neg B) \lor (\neg A \land B)$
        

This proves that the hypothesis space of decision trees is **fully expressive** for Boolean functions. This high expressiveness means they can overfit easily, which is why [[Occam's Razor]] (e.g., finding the _smallest_ tree) is crucial.

### Check Your Understanding

1. For $n=3$ boolean attributes, how many distinct boolean functions are there?
    
2. What is the problem with the high expressiveness of decision trees? How does this relate to [[Model Selection and Generalization (Bias-Variance)]]?
    
3. Draw a decision tree for the boolean function $F = A \land (B \lor C)$.