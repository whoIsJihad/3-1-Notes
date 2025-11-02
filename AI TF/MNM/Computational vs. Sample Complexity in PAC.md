> **Sources:**
> 
> - `12. Learning-Theory-6-PAC-NEG-POS.pdf` (Slides 27-44)
>     


A concept class $C$ is **efficiently PAC-learnable** only if it meets _two_ criteria:

1. **Polynomial Sample Complexity (Information-Theoretic):**
    
    - Can we _learn_ the concept from a polynomial number of examples?
        
    - This is the test we saw in [[PAC Learnability of Concept Classes]]: Is $\ln|\mathcal{H}|$ polynomial in $n$?
        
2. **Polynomial Time Complexity (Computational):**
    
    - Can we _run the algorithm_ and _find_ the hypothesis $h$ in polynomial time?
        
    - Even if there _is_ enough information ($m$ is polynomial), it's useless if finding the consistent $h$ would take exponential time (e.g., is NP-hard).
        

This distinction leads to "Negative Results" in PAC learning, where a class can be learnable in theory (sample complexity) but not in practice (computational complexity).

## Example: k-term-DNF

- **Description:** A disjunction of _at most k_ conjunctive terms.
    
    - e.g., for $k=2$: $(x_1 \land \neg x_2) \lor (x_3 \land x_4)$
        
- **Sample Complexity:**
    
    - Like 3-CNF, the hypothesis space size $|H|$ is $O(2^{n^k})$.
        
    - $\ln|H|$ is $O(n^k)$, which is **polynomial** (for a fixed $k$).
        
    - **Conclusion:** k-term-DNF _is_ information-theoretically PAC-learnable. We _can_ gather enough data to learn it.
        
- **Computational Complexity:**
    
    - **Problem:** Finding the _smallest_ k-term-DNF hypothesis $h$ that is _consistent_ with a training set $S$ is **NP-hard**.
        
    - This means no known algorithm can _find_ the hypothesis in polynomial time.
        
    - **Conclusion:** k-term-DNF is **NOT efficiently PAC-learnable** due to computational complexity.
        

## Negative Learnability Results

This gives us two ways a concept class can be "unlearnable":

1. **Information-Theoretic (Sample Complexity is Bad):**
    
    - The class is too rich/expressive. $\ln|H|$ is exponential, so we'd need an exponential amount of data.
        
    - **Examples:**
        
        - Arbitrary Boolean Functions (Decision Trees)
            
        - Deterministic Finite Automata (DFA)
            
        - Context Free Grammars (CFG)
            
2. **Complexity-Theoretic (Computational Complexity is Bad):**
    
    - The class has polynomial sample complexity, but _finding_ the consistent hypothesis is NP-hard.
        
    - **Examples:**
        
        - k-term-DNF
            
        - k-clause-CNF
            
        - Neural Networks (finding the consistent weights is hard)
            

## The "More Expressive Hypothesis Space" Trick

This leads to a clever solution (from slide 36):

- **Goal:** We want to learn $C = \text{k-term-DNF}$.
    
- **Problem:** Finding a consistent $h$ _in_ $C$ is NP-hard.
    
- **Solution:** We can learn $C$ using a _different, more expressive_ hypothesis space $H = \text{k-CNF}$.
    
    - It's a fact that any k-term-DNF can be re-written as a k-CNF. So, $C \subset H$.
        
    - We know $\ln|H_{k-CNF}|$ is polynomial (from the previous note).
        
    - Critically, there _is_ a polynomial-time algorithm for finding a consistent $h \in H_{k-CNF}$.
        
- **Result:** We can efficiently PAC-learn $C$ by searching in the _larger_ space $H$. This highlights the importance of choosing the right representation ($H$) for your problem ($C$).
    

### Check Your Understanding

1. What are the two requirements for a class to be _efficiently_ PAC-learnable?
    
2. k-term-DNF is not efficiently PAC-learnable. Is this because of an information-theoretic or computational-theoretic problem?
    
3. Why is the class of all Boolean functions not PAC-learnable?
    
4. How can using a _more_ expressive hypothesis space $H$ sometimes make learning _easier_ (more efficient)?