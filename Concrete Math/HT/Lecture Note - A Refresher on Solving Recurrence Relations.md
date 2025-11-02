
## 1. What is a Recurrence Relation?

A recurrence relation is just an equation that defines a sequence based on its preceding terms.

- **Example 1 (Fibonacci):** $F_n = F_{n-1} + F_{n-2}$, with $F_0=0, F_1=1$.
    
- **Example 2 (Gambler's Ruin):** $P_i = p \cdot P_{i+1} + q \cdot P_{i-1}$.
    

Finding a "closed-form" solution means finding a formula for the $n$-th term that _doesn't_ depend on previous terms (e.g., $a_n = 2^n$).

The two main types we care about are **Linear Homogeneous** and **Linear Non-Homogeneous**.

## 2. Method 1: Linear Homogeneous Relations

This is the simplest type. It has the form: $a_n = c_1 a_{n-1} + c_2 a_{n-2} + \dots + c_k a_{n-k}$ (It's "homogeneous" because all terms involve the sequence $a_i$. There's no extra "stuff" like $+1$ or $+n$).

**The Strategy: The Characteristic Equation**

1. **Guess a solution:** We guess a solution of the form $a_n = r^n$ for some constant $r$.
    
2. **Substitute the guess:** $r^n = c_1 r^{n-1} + c_2 r^{n-2}$
    
3. **Divide** by $r^{n-2}$ to get the **characteristic equation**: $r^2 = c_1 r + c_2 \implies \mathbf{r^2 - c_1 r - c_2 = 0}$
    
4. **Find the roots** ($r_1, r_2$) of this quadratic. The general solution depends on these roots.
    

### Case 1: Two Distinct Roots ($r_1 \neq r_2$)

The general solution is: $a_n = A(r_1)^n + B(r_2)^n$ You find the constants $A$ and $B$ using your base cases (e.g., $a_0$ and $a_1$).

**Example: Fibonacci Sequence**

- Recurrence: $F_n = F_{n-1} + F_{n-2}$
    
- Characteristic Eq: $r^2 - r - 1 = 0$
    
- Roots (by quadratic formula): $r_1 = \frac{1+\sqrt{5}}{2}$ ($\phi$, the golden ratio), $r_2 = \frac{1-\sqrt{5}}{2}$.
    
- General Solution: $F_n = A \left( \frac{1+\sqrt{5}}{2} \right)^n + B \left( \frac{1-\sqrt{5}}{2} \right)^n$
    
- Using $F_0=0$ and $F_1=1$, you can solve for $A$ and $B$ to get the famous Binet's formula.
    

### Case 2: One Repeated Root ($r_1 = r_2 = r$)

If you get a repeated root (e.g., $r^2 - 4r + 4 = 0 \implies (r-2)^2=0$), the solution $a_n = A r^n$ isn't general enough. The full solution is: $a_n = (A + Bn) r^n$ (If the root was repeated 3 times, it would be $(A + Bn + Cn^2)r^n$, and so on).

**Example:** $a_n = 6 a_{n-1} - 9 a_{n-2}$

- Characteristic Eq: $r^2 - 6r + 9 = 0 \implies (r-3)^2 = 0$.
    
- Root: $r=3$ (multiplicity 2).
    
- General Solution: $a_n = (A + Bn) 3^n$.
    

## 3. Method 2: Linear Non-Homogeneous Relations

This is the type we saw in the "Expected Duration" problem. It has an "extra part" $f(n)$ that doesn't depend on the sequence $a_i$. $a_n = c_1 a_{n-1} + \dots + c_k a_{n-k} + \mathbf{f(n)}$

**The Strategy: Two-Part Solution**

The general solution is the sum of two parts: $a_n = a_n^{(h)} + a_n^{(p)}$

1. $\mathbf{a_n^{(h)}}$: The **Homogeneous Solution**. You find this by setting $f(n)=0$ and solving the homogeneous version using **Method 1**.
    
2. $\mathbf{a_n^{(p)}}$: The **Particular Solution**. This is an educated "guess" that has the same form as $f(n)$.
    

**How to Guess the Particular Solution** $a_n^{(p)}$

|If $f(n)$ looks like...|Your Guess for $a_n^{(p)}$ is...|
|---|---|
|A constant (e.g., $f(n)=5$)|A constant: $C$|
|A polynomial (e.g., $f(n)=2n+3$)|A general polynomial of same degree: $C_1 n + C_0$|
|A polynomial (e.g., $f(n)=4n^2$)|$C_2 n^2 + C_1 n + C_0$|
|An exponential (e.g., $f(n)=5 \cdot 3^n$)|A multiple of that exponential: $C \cdot 3^n$|

### The **BIG CAVEAT**: What if the guess conflicts with the homogeneous solution?

This is the most important (and most forgotten) rule.

**If your guess for** $a_n^{(p)}$ **is already part of your homogeneous solution** $a_n^{(h)}$**, you must multiply your guess by** $n$ **until it is no longer a solution.**

**Example: The Gambler's Ruin Duration**

- Recurrence: $E_i = 1 + \frac{1}{2} E_{i+1} + \frac{1}{2} E_{i-1}$
    
- Rearranged: $E_{i+1} = 2E_i - E_{i-1} - 2$. (Let's use $n$ instead of $i$ for clarity: $a_n = 2a_{n-1} - a_{n-2} - 2$)
    

1. **Homogeneous Part:** $a_n^{(h)}$
    
    - Solve $a_n = 2a_{n-1} - a_{n-2}$.
        
    - Char. Eq: $r^2 - 2r + 1 = 0 \implies (r-1)^2 = 0$.
        
    - Root: $r=1$ (a repeated root!).
        
    - Homogeneous Solution: $a_n^{(h)} = (A + Bn) \cdot 1^n = \mathbf{A + Bn}$.
        
2. **Particular Part:** $a_n^{(p)}$
    
    - The non-homogeneous part is $f(n) = -2$ (a constant, or polynomial of degree 0).
        
    - **First Guess:** Try $a_n^{(p)} = C$ (a constant).
        
    - **Check for Conflict:** Is $C$ part of $a_n^{(h)}$? Yes. $a_n^{(h)} = A + Bn$. The $A$ term is a constant. This is a conflict.
        
    - **Second Guess:** Multiply by $n$. Try $a_n^{(p)} = Cn$.
        
    - **Check for Conflict:** Is $Cn$ part of $a_n^{(h)}$? Yes. $a_n^{(h)} = A + Bn$. The $Bn$ term is a linear term. This is also a conflict.
        
    - **Third Guess:** Multiply by $n$ again. Try $a_n^{(p)} = \mathbf{Cn^2}$.
        
    - **Check for Conflict:** Is $Cn^2$ part of $a_n^{(h)}$? No. $a_n^{(h)}$ only has constant and linear terms. This guess is valid!
        
3. **Solve for** $C$**:**
    
    - Plug $a_n^{(p)} = Cn^2$ back into the _full_ recurrence: $a_n = 2a_{n-1} - a_{n-2} - 2$.
        
    - $Cn^2 = 2 \cdot C(n-1)^2 - C(n-2)^2 - 2$
        
    - $Cn^2 = 2C(n^2 - 2n + 1) - C(n^2 - 4n + 4) - 2$
        
    - $Cn^2 = 2Cn^2 - 4Cn + 2C - Cn^2 + 4Cn - 4C - 2$
        
    - $Cn^2 = (2C - C)n^2 + (-4C + 4C)n + (2C - 4C) - 2$
        
    - $Cn^2 = Cn^2 + 0n - 2C - 2$
        
    - $0 = -2C - 2 \implies 2C = -2 \implies \mathbf{C = -1}$.
        
    - So, our particular solution is $a_n^{(p)} = -n^2$.
        
4. **Final General Solution:**
    
    - $a_n = a_n^{(h)} + a_n^{(p)} = A + Bn - n^2$.
        
    - (Or using $i$: $E_i = A + Bi - i^2$).
        
    - This is _exactly_ the solution we arrived at in the previous note. We then used the boundary conditions $E_0=0$ and $E_N=0$ to find $A=0$ and $B=N$, giving the final answer $E_i = Ni - i^2$.
        

## 4. Method 3: Iteration (Unrolling)

Sometimes, the easiest way is to just "unroll" the recurrence and look for a pattern. This is less formal but great for simple relations.

**Example:** $T(n) = T(n-1) + 3$, with $T(0) = 2$.

- $T(n) = (T(n-2) + 3) + 3 = T(n-2) + 2 \cdot 3$
    
- $T(n) = (T(n-3) + 3) + 2 \cdot 3 = T(n-3) + 3 \cdot 3$
    
- ...
    
- $T(n) = T(n-k) + k \cdot 3$
    
- We want to get to our base case $T(0)$, so let $k=n$.
    
- $T(n) = T(n-n) + n \cdot 3 = T(0) + 3n$
    
- $T(n) = 2 + 3n$. (Closed form!)
    

This should be a good summary of the techniques you've seen before. Let me know if you'd like to try a new practice problem using this!