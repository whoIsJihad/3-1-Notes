> **Sources:**
> 
> - `5. Learning-2-UT-DT-LN.pdf` (Slides 37-69)
>     

# Information Theory (Entropy and Information Gain)

[[The ID3 Algorithm]] needs a way to pick the "best" attribute at each step. "Best" means the attribute that does the best job of splitting the examples into "pure" sets (i.e., sets that are all "Yes" or all "No").

Information theory, founded by Claude Shannon, gives us a mathematical way to measure "purity" or "uncertainty." This measure is called **Entropy**.

## Entropy (A Measure of Impurity)

**Entropy** $H(S)$ of a set of examples $S$ is a measure of its uncertainty. High entropy means high uncertainty (a mixed set), and low entropy means low uncertainty (a pure set).

For a binary classification problem (e.g., "Yes" / "No" or "+"/ "-"), let:

- $p_+$ be the proportion of positive examples in $S$
    
- $p_-$ be the proportion of negative examples in $S$
    

The entropy of $S$ is calculated as:

$$H(S) = -p_+ \log_2(p_+) - p_- \log_2(p_-)$$

(Note: We define $0 \log_2(0) = 0$)

### Key Entropy Values:

- **Maximum Entropy (H=1):** The set is maximally "impure" or uncertain. This happens when the examples are evenly split.
    
    - Example: $S = \{7 \text{ Yes}, 7 \text{ No}\}$. $p_+ = 0.5$, $p_- = 0.5$.
        
    - $H(S) = -0.5 \log_2(0.5) - 0.5 \log_2(0.5) = -0.5(-1) - 0.5(-1) = 0.5 + 0.5 = 1$.
        
- **Minimum Entropy (H=0):** The set is perfectly "pure" or certain. All examples have the same label.
    
    - Example: $S = \{14 \text{ Yes}, 0 \text{ No}\}$. $p_+ = 1$, $p_- = 0$.
        
    - $H(S) = -1 \log_2(1) - 0 \log_2(0) = -1(0) - 0 = 0$.
        

## Information Gain (The Attribute-Picking Heuristic)

**Information Gain** $Gain(S, A)$ measures the _expected reduction in entropy_ we get by splitting the set $S$ on attribute $A$.

We pick the attribute with the **highest information gain**.

$$Gain(S, A) = \underbrace{H(S)}_{\text{Entropy before split}} - \underbrace{\sum_{v \in Values(A)} \frac{|S_v|}{|S|} H(S_v)}_{\text{Weighted average entropy after split}}$$

Where:

- `Values(A)`: The set of all possible values for attribute $A$ (e.g., `{Sunny, Overcast, Rain}`).
    
- `S_v`: The subset of examples in $S$ where attribute $A$ has value `v` (e.g., all "Sunny" examples).
    
- `|S_v| / |S|`: The weight of the $v$-th subset (what fraction of examples have this value).
    

### Example: "Play Tennis" (Total S = {9+, 5-})

- **Entropy before split:** $H(S) = -(9/14) \log_2(9/14) - (5/14) \log_2(5/14) \approx \mathbf{0.940}$
    
- **Test Attribute "Wind" (Values: {Weak, Strong}):**
    
    - $S_{Weak} = \{6+, 2-\}$. $H(S_{Weak}) = -(6/8)\log_2(6/8) - (2/8)\log_2(2/8) \approx 0.811$
        
    - $S_{Strong} = \{3+, 3-\}$. $H(S_{Strong}) = -(3/6)\log_2(3/6) - (3/6)\log_2(3/6) = 1.0$
        
    - **Gain(S, Wind)** = $0.940 - \left[ \frac{8}{14} H(S_{Weak}) + \frac{6}{14} H(S_{Strong}) \right]$ = $0.940 - [ (8/14)(0.811) + (6/14)(1.0) ]$ = $0.940 - [ 0.463 + 0.429 ] = 0.940 - 0.892 = \mathbf{0.048}$
        
- **Test Attribute "Outlook" (Values: {Sunny, Overcast, Rain}):**
    
    - $S_{Sunny} = \{2+, 3-\}$. $H(S_{Sunny}) \approx 0.971$
        
    - $S_{Overcast} = \{4+, 0-\}$. $H(S_{Overcast}) = 0.0$
        
    - $S_{Rain} = \{3+, 2-\}$. $H(S_{Rain}) \approx 0.971$
        
    - **Gain(S, Outlook)** = $0.940 - \left[ \frac{5}{14} H(S_{Sunny}) + \frac{4}{14} H(S_{Overcast}) + \frac{5}{14} H(S_{Rain}) \right]$ = $0.940 - [ (5/14)(0.971) + (4/14)(0) + (5/14)(0.971) ]$ = $0.940 - [ 0.347 + 0 + 0.347 ] = 0.940 - 0.694 = \mathbf{0.246}$
        

**Conclusion:** $Gain(S, \text{Outlook}) > Gain(S, \text{Wind})$. Therefore, the ID3 algorithm _greedily chooses "Outlook"_ as the root node.

### Check Your Understanding

1. What does an Entropy of 0 mean? What about an Entropy of 1?
    
2. If you have a set $S = \{15 \text{ Yes}, 5 \text{ No}\}$, would its entropy be closer to 0 or 1? Why?
    
3. Why is Information Gain a "greedy" heuristic?