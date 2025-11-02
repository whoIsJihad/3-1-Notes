> **Sources:**
> 
> - `12. Learning-Theory-6-PAC-NEG-POS.pdf` (Slides 4-26)
>     
> 
> **(This is a detailed rewrite of the previous note, which was too dense.)**

# PAC Learnability of Concept Classes

This note answers the question: "Which types of functions are _actually_ learnable?"

From the [[PAC Learning (Probably Approximately Correct)]], we know a class of functions (a "concept class," $C$) is efficiently learnable if it has two properties:

1. **Polynomial Sample Complexity:** We only need a polynomial (not exponential) number of training examples.
    
2. **Polynomial Time Complexity:** We can _find_ the hypothesis in polynomial time.
    

This note focuses on the first point: **Sample Complexity**.

## The Core Test: $\ln|\mathcal{H}|$

From [[PAC Learning and Occam's Razor]], we have our sample complexity bound:

$$m > \frac{1}{\epsilon} \left( \ln|\mathcal{H}| + \ln\frac{1}{\delta} \right)$$

Here, $m$ is the number of examples we need, and $n$ is the number of features (e.g., `Patrons`, `Hungry`, etc.).

This formula gives us a simple test:

- If the term $\ln|\mathcal{H}|$ (the log of the hypothesis space size) is **polynomial** in $n$, then the whole formula for $m$ is polynomial. The class **is** information-theoretically PAC-learnable.
    
- If $\ln|\mathcal{H}|$ is **exponential** in $n$, then $m$ will be exponential. The class is **NOT** PAC-learnable. We'd need an impossible amount of data.
    

Let's apply this test to the concept classes from the lecture.

## Case 1: General Conjunctions

- **What is it?** A function that is a conjunction (AND) of literals. Each feature can be included positively ($x_1$), negatively ($\neg x_1$), or not at all.
    
    - _Example:_ $f = x_1 \land \neg x_3 \land x_5$
        
- **Step 1: Find the size of the hypothesis space,** $|\mathcal{H}|$
    
    - For the first feature ($x_1$), we have 3 choices: include $x_1$, include $\neg x_1$, or include nothing.
        
    - For the second feature ($x_2$), we also have 3 choices.
        
    - ...
        
    - For the $n$-th feature ($x_n$), we have 3 choices.
        
    - The total number of possible functions is $3 \times 3 \times \dots \times 3$ ($n$ times).
        
    - $|\mathcal{H}| = 3^n$
        
- **Step 2: Take the log,** $\ln|\mathcal{H}|$
    
    - $\ln|\mathcal{H}| = \ln(3^n) = n \ln(3)$
        
- **Step 3: Analyze the result**
    
    - $n \ln(3)$ is a function that is **linear** in $n$ (it's $O(n)$).
        
    - $O(n)$ is **polynomial**.
        
- **Conclusion:** General conjunctions are **PAC-learnable**.
    
    - **Concrete Example (from slide 7):** If we have $n=10$ features, want $\epsilon=0.1$ (90% accuracy), and $\delta=0.05$ (95% confidence):
        
        - $m > \frac{1}{0.1} \left( \ln(1/0.05) + 10 \ln(3) \right)$
            
        - $m > 10 \times (2.996 + 10.986) \approx 10 \times (13.982) \approx 140$ examples.
            
    - This is a tiny, perfectly reasonable number of examples. If $n=100$, it's $\approx 1129$ examples, which is still very feasible.
        

## Case 2: 3-CNF (The Tricky One)

- **What is it?** A function in Conjunctive Normal Form, where each _clause_ (the part in parentheses) has at most 3 _literals_.
    
    - _Example:_ $f = (x_1 \lor \neg x_2 \lor x_3) \land (x_2 \lor x_4)$
        
- **Step 1: Find the size of the hypothesis space,** $|\mathcal{H}|$
    
    - This is tricky. Let's build it from the ground up.
        
    - **A. Find all possible "building blocks" (all unique 3-clauses):**
        
        - We have $n$ features, which means $2n$ possible _literals_ (e.g., $x_1, \neg x_1, x_2, \neg x_2, \dots$).
            
        - A 3-clause is made by choosing 3 of these literals.
            
        - The number of ways to _choose 3 literals_ is $\binom{2n}{3} = \frac{(2n)(2n-1)(2n-2)}{6}$.
            
        - We don't need the exact number, just the _order_. This is $O(n^3)$. (The slide uses a simpler upper bound of $(2n)^3$, which is also $O(n^3)$).
            
        - So, there are $k = O(n^3)$ possible, unique 3-clauses we _could_ use.
            
    - **B. Find all possible functions:**
        
        - A 3-CNF function is a _conjunction_ of these building blocks (e.g., `clause_1 AND clause_5 AND clause_82`).
            
        - This is the same as picking a _subset_ of all possible $k$ clauses.
            
        - If there are $k$ possible clauses, the number of subsets is $2^k$.
            
        - $|\mathcal{H}| = 2^k = 2^{O(n^3)}$
            
- **Step 2: Take the log,** $\ln|\mathcal{H}|$
    
    - $\ln|\mathcal{H}| = \ln(2^{O(n^3)}) = O(n^3) \ln(2)$
        
- **Step 3: Analyze the result**
    
    - The size $O(n^3)$ is **polynomial** in $n$.
        
- **Conclusion:** 3-CNF **is** PAC-learnable (from a sample complexity standpoint).
    

## Case 3: General Boolean Functions

- **What is it?** _Any possible function_ you can define on $n$ Boolean inputs. This is the hypothesis space for a full-sized Decision Tree or a complete truth table.
    
- **Step 1: Find the size of the hypothesis space,** $|\mathcal{H}|$
    
    - Let's use the truth table method.
        
    - A truth table for $n$ features has $2^n$ **rows**.
        
    - For _each row_, the function can output either `0` or `1` (2 choices).
        
    - The total number of functions is $2 \times 2 \times \dots \times 2$ ($2^n$ times).
        
    - $|\mathcal{H}| = 2^{2^n}$
        
- **Step 2: Take the log,** $\ln|\mathcal{H}|$
    
    - $\ln|\mathcal{H}| = \ln(2^{2^n}) = 2^n \ln(2)$
        
- **Step 3: Analyze the result**
    
    - The size $O(2^n)$ is **exponential** in $n$.
        
- **Conclusion:** The class of all Boolean functions is **NOT PAC-learnable**.
    
    - This is an **Information-Theoretic Negative Result**. It means that no matter what algorithm you use, you simply _cannot_ get enough information from a polynomial-sized sample to find the right function. The search space is just too big.
        

### Check Your Understanding

1. What is the "one-line test" for whether a concept class is _information-theoretically_ PAC-learnable?
    
2. Walk through the 3 choices for a single variable in a General Conjunction. What are they?
    
3. Explain _why_ the number of 3-CNF functions is $2^{O(n^3)}$. Where do the two exponents come from?
    
4. Why is "General Boolean Functions" an example of an _information-theoretic_ negative result?