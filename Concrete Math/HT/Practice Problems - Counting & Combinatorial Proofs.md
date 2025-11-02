

## Section 1: Standard Counting Problems

These problems apply the multiplication rule, combinations, permutations, "stars and bars," and the principle of inclusion-exclusion.

### Problem 1: The Versatile Committee

A department has 10 junior faculty and 8 senior faculty. A committee of 5 people must be formed. How many ways can this be done if:

a) There are no restrictions? b) The committee must have exactly 3 junior faculty and 2 senior faculty? c) The committee must have _at least_ one senior faculty member?

### Solution 1:

This is a classic combinations problem.

**a) No restrictions:** We are simply choosing 5 people from the total group of $10 + 8 = 18$ people.

- **Answer:** $\binom{18}{5} = \frac{18!}{5!13!} = 8,568$ ways.
    

**b) Exactly 3 junior and 2 senior:** We break this down using the multiplication rule:

1. Choose 3 junior faculty from 10: $\binom{10}{3}$
    
2. Choose 2 senior faculty from 8: $\binom{8}{2}$
    

- **Answer:** $\binom{10}{3} \times \binom{8}{2} = \left(\frac{10 \cdot 9 \cdot 8}{3 \cdot 2 \cdot 1}\right) \times \left(\frac{8 \cdot 7}{2 \cdot 1}\right) = 120 \times 28 = 3,360$ ways.
    

**c) At least one senior faculty:** This is a perfect case for using the **complement**.

- Total ways (from part a): $\binom{18}{5} = 8,568$
    
- The "bad" case (the complement) is having _zero_ senior faculty. This means all 5 members must be chosen from the 10 junior faculty.
    
- Ways for "bad" case: $\binom{10}{5} = \frac{10 \cdot 9 \cdot 8 \cdot 7 \cdot 6}{5 \cdot 4 \cdot 3 \cdot 2 \cdot 1} = 252$ ways.
    
- **Answer:** (Total ways) - (Bad ways) = $8,568 - 252 = 8,316$ ways.
    

### Problem 2: Distributing Identical Items (Stars and Bars)

A quant analyst has 20 identical units of a resource (e.g., 20 thousand dollars) to distribute among 4 different investment funds (A, B, C, D).

a) How many ways can the resource be allocated if any fund can receive any amount (including zero)? b) How many ways can the resource be allocated if _each_ fund must receive at least 2 units?

### Solution 2:

This is a classic "stars and bars" problem. We are placing $n=20$ identical items ("stars") into $k=4$ distinguishable bins ("funds"). The formula is $\binom{n+k-1}{k-1}$.

**a) No restrictions:** Here $n=20$ and $k=4$.

- We have 20 "stars" (resource units) and need $k-1 = 3$ "bars" to separate the 4 funds.
    
- We are arranging 23 items in a line and choosing where to put the 3 bars.
    
- **Answer:** $\binom{20+4-1}{4-1} = \binom{23}{3} = \frac{23 \cdot 22 \cdot 21}{3 \cdot 2 \cdot 1} = 1,771$ ways.
    

**b) Each fund must receive at least 2 units:** The best strategy here is to **pre-allocate** the required amount.

1. First, give 2 units to Fund A, 2 to B, 2 to C, and 2 to D. This uses up $4 \times 2 = 8$ units.
    
2. Now we have $20 - 8 = 12$ units of the resource left to distribute.
    
3. We can distribute these 12 remaining units among the 4 funds with _no restrictions_.
    
4. This is a new stars and bars problem with $n=12$ and $k=4$.
    

- **Answer:** $\binom{12+4-1}{4-1} = \binom{15}{3} = \frac{15 \cdot 14 \cdot 13}{3 \cdot 2 \cdot 1} = 455$ ways.
    

### Problem 3: Principle of Inclusion-Exclusion (PIE)

How many integers between 1 and 1000 (inclusive) are divisible by 2, 3, or 5?

### Solution 3:

We are looking for $|A \cup B \cup C|$, where:

- $A$ = set of integers divisible by 2
    
- $B$ = set of integers divisible by 3
    
- $C$ = set of integers divisible by 5
    

We use the PIE formula: $|A \cup B \cup C| = |A| + |B| + |C| - (|A \cap B| + |A \cap C| + |B \cap C|) + |A \cap B \cap C|$

1. **Find the single set sizes (using the floor function** $\lfloor \cdot \rfloor$**):**
    
    - $|A| = \lfloor 1000/2 \rfloor = 500$
        
    - $|B| = \lfloor 1000/3 \rfloor = 333$
        
    - $|C| = \lfloor 1000/5 \rfloor = 200$
        
2. **Find the two-way intersections:**
    
    - $|A \cap B|$ (div by 2 and 3) = div by 6 $\implies \lfloor 1000/6 \rfloor = 166$
        
    - $|A \cap C|$ (div by 2 and 5) = div by 10 $\implies \lfloor 1000/10 \rfloor = 100$
        
    - $|B \cap C|$ (div by 3 and 5) = div by 15 $\implies \lfloor 1000/15 \rfloor = 66$
        
3. **Find the three-way intersection:**
    
    - $|A \cap B \cap C|$ (div by 2, 3, and 5) = div by 30 $\implies \lfloor 1000/30 \rfloor = 33$
        
4. **Apply the formula:**
    
    - $(500 + 333 + 200) - (166 + 100 + 66) + 33$
        
    - $= 1033 - 332 + 33$
        
    - $= 701 + 33 = 734$
        

- **Answer:** There are 734 such integers.
    

## Section 2: Story Proof (Combinatorial Proof) Problems

For these, you must show that two expressions are equal by arguing that both sides count the _same thing_ in two different ways.

### Problem 4: Pascal's Identity

Provide a story proof for the identity:

$$\binom{n}{k} = \binom{n-1}{k-1} + \binom{n-1}{k}$$

### Solution 4:

- **Story Setup:** We want to count the number of ways to form a committee of $k$ people from a group of $n$ people.
    
- **LHS (Left-Hand Side):** $\binom{n}{k}$. This is the very definition of choosing a $k$-person committee from $n$ people.
    
- **RHS (Right-Hand Side):** $\binom{n-1}{k-1} + \binom{n-1}{k}$. Let's count the same thing by conditioning on one specific person, let's call her **Alice**.
    
    - When we form the committee, there are exactly two possibilities: either Alice is on the committee, or she is not.
        
    - **Case 1: Alice IS on the committee.**
        
        - If Alice is on the committee, we have already filled 1 of our $k$ spots. We now must choose the remaining $k-1$ members from the remaining $n-1$ people (everyone _except_ Alice).
            
        - The number of ways to do this is $\binom{n-1}{k-1}$.
            
    - **Case 2: Alice IS NOT on the committee.**
        
        - If Alice is not on the committee, we still need to choose all $k$ members. We must choose them from the $n-1$ people who are _not_ Alice.
            
        - The number of ways to do this is $\binom{n-1}{k}$.
            
- **Conclusion:** Since these two cases are mutually exclusive (Alice is either in or out) and they cover all possibilities, the sum of the ways for each case must equal the total number of ways to form the committee.
    
- Therefore, $\binom{n}{k} = \binom{n-1}{k-1} + \binom{n-1}{k}$.
    

### Problem 5: Sum of Squares Identity

Provide a story proof for the identity:

$$\sum_{k=0}^{n} \binom{n}{k}^2 = \binom{2n}{n}$$

### Solution 5:

- **Hint:** First, rewrite the identity using the fact that $\binom{n}{k} = \binom{n}{n-k}$.
    
    $$\sum_{k=0}^{n} \binom{n}{k} \binom{n}{n-k} = \binom{2n}{n}$$
    
    (This is a special case of Vandermonde's Identity, which was in your notes!)
    
- **Story Setup:** We want to count the number of ways to form a committee of $n$ people from a group of $2n$ people.
    
- **LHS (Left-Hand Side):** $\binom{2n}{n}$. This is the definition of choosing $n$ people from a group of $2n$.
    
- **RHS (Right-Hand Side):** $\sum_{k=0}^{n} \binom{n}{k} \binom{n}{n-k}$. Let's count the same thing by splitting the $2n$ people into two distinct groups: $n$ men and $n$ women.
    
    - To form our $n$-person committee, we can choose $k$ men and the rest, $n-k$, must be women.
        
    - Let's iterate over all possible values of $k$ (the number of men we choose), from $k=0$ up to $k=n$.
        
    - **Case for a specific** $k$**:**
        
        1. Choose $k$ men from the $n$ available men: $\binom{n}{k}$ ways.
            
        2. Choose $n-k$ women from the $n$ available women: $\binom{n}{n-k}$ ways.
            
        
        - The total ways for this specific $k$ is $\binom{n}{k} \binom{n}{n-k}$.
            
    - **Summing the cases:** To get the _total_ number of ways, we must sum this over all possible values of $k$: $\sum_{k=0}^{n} \binom{n}{k} \binom{n}{n-k}$.
        
- **Conclusion:** Both sides count the exact same thing (choosing $n$ people from $2n$), just in different ways.
    
- Therefore, $\sum_{k=0}^{n} \binom{n}{k}^2 = \binom{2n}{n}$.
    

### Problem 6: The Hockey-Stick Identity

Provide a story proof for the identity (for $n \ge k$):

$$\sum_{i=k}^{n} \binom{i}{k} = \binom{n+1}{k+1}$$

(This is called the "Hockey-Stick" identity because of the pattern it forms in Pascal's Triangle).

### Solution 6:

- **Story Setup:** We want to count the number of ways to choose a subset (a committee) of $k+1$ numbers from the set of $n+1$ integers $\{1, 2, \dots, n, n+1\}$.
    
- **RHS (Right-Hand Side):** $\binom{n+1}{k+1}$. This is the definition of choosing $k+1$ items from $n+1$ available items.
    
- **LHS (Left-Hand Side):** $\sum_{i=k}^{n} \binom{i}{k}$. Let's count the same thing by conditioning on the **largest number** chosen for our committee.
    
    - Let the largest number we choose be $j$.
        
    - Since we must choose $k+1$ numbers, the largest number $j$ must be at least $k+1$.
        
    - Also, the largest number $j$ can be at most $n+1$.
        
    - So, $j$ can range from $k+1$ to $n+1$.
        
    - **Case for a specific** $j$**:**
        
        - Let's say the largest number we choose is $j$. We have now chosen 1 number (the number $j$ itself).
            
        - We still need to choose the _other_ $k$ members of the committee.
            
        - Since $j$ is the largest, these $k$ members must be chosen from the numbers smaller than $j$, which are $\{1, 2, \dots, j-1\}$.
            
        - There are $j-1$ numbers to choose from.
            
        - The number of ways to do this is $\binom{j-1}{k}$.
            
    - **Summing the cases:** To get the total, we sum over all possible values for $j$: $\sum_{j=k+1}^{n+1} \binom{j-1}{k}$.
        
    - This sum looks slightly different, but let's change the index. Let $i = j-1$.
        
        - When $j=k+1$, $i=k$.
            
        - When $j=n+1$, $i=n$.
            
    - Substituting $i$ gives us the exact expression from the LHS: $\sum_{i=k}^{n} \binom{i}{k}$.
        
- **Conclusion:** Both sides count the number of ways to choose $k+1$ numbers from $\{1, 2, \dots, n+1\}$.
    
- Therefore, $\sum_{i=k}^{n} \binom{i}{k} = \binom{n+1}{k+1}$.