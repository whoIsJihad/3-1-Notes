> **Sources:**
> 
> - `5. Learning-2-UT-DT-LN.pdf` (Slides 7-25, 70-71)
>     
> - `6. decision-trees-discussion nidhi.pdf` (Slide 2)
>     


In our [[Decision Trees (and the Restaurant Problem)]] note, we saw _what_ a decision tree is. The **ID3 (Iterative Dichotomiser 3)** algorithm, developed by Ross Quinlan, is the classic algorithm that tells us _how to build_ one.

Our goal, guided by [[Occam's Razor]], is to find the _smallest_ decision tree that is consistent with the training data.

- **The Problem:** Finding the _minimal_ decision tree is NP-hard.
    
- **The Solution:** ID3 uses a **greedy, top-down, heuristic search**.
    
    - **Top-down:** It starts at the root and recursively builds the tree downwards.
        
    - **Greedy:** At each node, it picks the "best" attribute to split on _at that moment_ and never backtracks.
        
    - **Heuristic:** The "best" attribute is chosen using a heuristic called **Information Gain**, which we'll explore in [[Information Theory (Entropy and Information Gain)]].
        

## The ID3 Algorithm (Pseudocode)

`ID3(S, Attributes)`:

- `S`: The set of labeled training examples at the current node.
    
- `Attributes`: The set of attributes _still available_ to be tested.
    

1. **Base Case 1 (Pure Set):** If all examples in `S` have the _same label_ (e.g., all "Yes"):
    
    - Return a new **leaf node** with that label.
        
2. **Base Case 2 (No Attributes Left):** If `Attributes` is empty:
    
    - Return a new **leaf node** with the _most common label_ in `S` (this is called the majority vote).
        
3. **Recursive Step:**
    
    - Find the attribute `A` from `Attributes` that "best classifies" `S`.
        
        - "Best" = the attribute with the highest **Information Gain**.
            
    - Create a new **root node** for the tree and label it with `A`.
        
    - **For each** possible value `v` that attribute `A` can take:
        
        - Add a new branch from the root node for the test `A = v`.
            
        - Let `S_v` be the _subset_ of examples in `S` where `A = v`.
            
        - **Handle Empty Subsets:** If `S_v` is empty (no examples have this value):
            
            - Add a leaf node with the _majority label_ from the parent set `S`. (This is a practical step for handling unseen data).
                
        - **Recurse:** Else (if `S_v` is not empty):
            
            - Call `ID3(S_v, Attributes - {A})` and attach the resulting subtree to this branch.
                
4. Return the newly created root node.
    

### Check Your Understanding

1. Why is the ID3 algorithm considered "greedy"? What is a potential downside of this greedy approach?
    
2. What are the two main base cases that stop the recursion?
    
3. In the recursive step, why do we pass `Attributes - {A}` instead of just `Attributes` into the next call?