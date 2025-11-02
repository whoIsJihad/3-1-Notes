
You've reviewed the classic Monty Hall, Simpson's Paradox, and Gambler's Ruin problems. This note contains _novel variations_ on those problems to test your mastery of the underlying concepts: conditional probability, the Law of Total Probability (LTP), confounding variables, and recurrence relations.

## Section 1: Variation on Conditional Probability (Monty Hall)

The Monty Hall problem is all about how new information (which door Monty opens) changes the probabilities. This problem, a classic in its own right, explores a similar, subtle distinction.

### Problem 1: The "Two-Child Problem" Variations

This problem has two parts. Assume the probability of having a boy or a girl is $1/2$, and the genders of the two children are independent.

**(a)** A parent tells you, "I have two children, and **at least one of them is a boy**." What is the probability that both children are boys?

**(b)** A parent tells you, "I have two children, and **my older child is a boy**." What is the probability that both children are boys?

### Solution 1:

The key to both parts is to correctly identify the sample space _after_ you receive the information.

Let the sample space of two children be $S = \{BB, BG, GB, GG\}$, where "BG" means the older is a boy and the younger is a girl. Each outcome has a probability of $1/4$.

Let $A$ be the event "both children are boys" = $\{BB\}$.

**(a) Given "at least one of them is a boy"**

1. Let $F$ be the event "at least one child is a boy".
    
2. The set of outcomes for $F$ is $\{BB, BG, GB\}$. This is our new, reduced sample space.
    
3. We want to find $P(A|F) = \frac{P(A \cap F)}{P(F)}$.
    
4. $A \cap F$: The event "both are boys" AND "at least one is a boy" is just $\{BB\}$. So $P(A \cap F) = P(A) = 1/4$.
    
5. $P(F)$: The probability of the reduced sample space is $P(BB) + P(BG) + P(GB) = 1/4 + 1/4 + 1/4 = 3/4$.
    
6. **Answer (a):** $P(A|F) = \frac{1/4}{3/4} = \mathbf{1/3}$.
    

**(b) Given "my older child is a boy"**

1. Let $G$ be the event "the older child is a boy".
    
2. The set of outcomes for $G$ is $\{BB, BG\}$. This is our new, reduced sample space.
    
3. We want to find $P(A|G) = \frac{P(A \cap G)}{P(G)}$.
    
4. $A \cap G$: The event "both are boys" AND "the older is a boy" is just $\{BB\}$. So $P(A \cap G) = P(A) = 1/4$.
    
5. $P(G)$: The probability of this reduced sample space is $P(BB) + P(BG) = 1/4 + 1/4 = 2/4 = 1/2$.
    
6. **Answer (b):** $P(A|G) = \frac{1/4}{1/2} = \mathbf{1/2}$.
    

**Key Takeaway:** The information "my older child is a boy" (b) is _more specific_ than "at least one is a boy" (a). It eliminated the {GG} case _and_ the {GB} case, whereas (a) only eliminated the {GG} case. More information changes the denominator and thus the probability.

## Section 2: Variation on Simpson's Paradox

Simpson's Paradox (the surgeon problem) shows how a confounding variable (difficulty of surgery) can reverse a trend. Here is the exact same paradox in a different context.

### Problem 2: The Batting Average Paradox

Two baseball players, Player A and Player B, have the following stats against Left-Handed (LHP) and Right-Handed (RHP) pitchers.

||Player A|Player B|
|---|---|---|
|**vs LHP**|100 hits / 400 at-bats (**0.250**)|20 hits / 100 at-bats (0.200)|
|**vs RHP**|60 hits / 100 at-bats (**0.600**)|250 hits / 500 at-bats (0.500)|

**(a)** Which player is the better hitter against Left-Handed pitchers? **(b)** Which player is the better hitter against Right-Handed pitchers? **(c)** Which player has the better _overall_ batting average?

### Solution 2:

**(a) vs LHP:** Player A has a batting average of 0.250. Player B has 0.200. **Player A is better vs. LHP.**

**(b) vs RHP:** Player A has a batting average of 0.600. Player B has 0.500. **Player A is better vs. RHP.**

**(c) Overall:**

- **Player A Total:** (100 hits + 60 hits) / (400 at-bats + 100 at-bats) = 160 / 500 **Player A Overall Avg = 0.320**
    
- **Player B Total:** (20 hits + 250 hits) / (100 at-bats + 500 at-bats) = 270 / 600 **Player B Overall Avg = 0.450**
    

**The Paradox:** Player A is a better hitter in _both_ specific situations (vs LHP and vs RHP), but Player B has a _much better_ overall average (0.450 > 0.320).

**Explanation (The Confounding Variable):** This is Simpson's Paradox. The confounding variable is the **number of at-bats** against each type of pitcher.

- Player A's overall average is dominated by his 400 at-bats against LHP, which is his _worse_ category (0.250).
    
- Player B's overall average is dominated by his 500 at-bats against RHP, which is his _better_ category (0.500).
    

Essentially, Player B got to "pad his stats" in the situation he was good at, while Player A spent most of his time in the situation he was bad at. This drags A's average down and pulls B's average up, reversing the trend.

## Section 3: Variation on Gambler's Ruin

The Gambler's Ruin problem (finding $P_i$) is solved with a recurrence relation based on LTP. This problem uses the _exact same setup_ to find a different quantity: the **expected duration** of the game.

### Problem 3: Expected Duration of Gambler's Ruin (Fair Game)

A gambler starts with $i$ dollars. On each bet, she wins 1 dollar or loses 1 dollar.  with equal probability (p=q=1/2). The game stops when she reaches $N$ dollars or  0 dollar . Let $E_i$ be the **expected number of bets** the game will last, starting from $i$ dollars.

Find $E_i$.

### Solution 3 (Proof by Recurrence):

**1. Set up the Recurrence using LTP for Expectation:** Let $E_i$ be the expected duration starting from $i$. We condition on the first bet.

- After the first bet (which takes 1 unit of time), she is either at state $i+1$ (with prob. 1/2) or state $i-1$ (with prob. 1/2).
    
- If she is at $i+1$, the _remaining_ expected duration is $E_{i+1}$.
    
- If she is at $i-1$, the _remaining_ expected duration is $E_{i-1}$.
    
- Therefore, by the Law of Total Expectation: $E_i = 1 + \frac{1}{2} E_{i+1} + \frac{1}{2} E_{i-1}$ (for $0 < i < N$) (The "1" is crucial: it's the one bet we just made).
    

**2. Define Boundary Conditions:**

- $E_0 = 0$ (If you start at $0, the game has already ended. Duration is 0).
    
- $E_N = 0$ (If you start at $N, the game has already ended. Duration is 0).
    

**3. Solve the Recurrence:** This is a _non-homogeneous_ difference equation. The solution is the sum of a homogeneous solution and a particular solution ($E_i = E_i^{(h)} + E_i^{(p)}$).

- **Homogeneous Part:** $E_i = \frac{1}{2} E_{i+1} + \frac{1}{2} E_{i-1}$. We solved this for the Gambler's Ruin probability: it's an arithmetic progression. $E_i^{(h)} = A + Bi$.
    
- **Particular Part:** We need a particular solution for $E_i = 1 + \frac{1}{2} E_{i+1} + \frac{1}{2} E_{i-1}$. The homogeneous solution is linear, so let's guess a quadratic: $E_i^{(p)} = Ci^2$. Plug this guess into the recurrence: $Ci^2 = 1 + \frac{1}{2} C(i+1)^2 + \frac{1}{2} C(i-1)^2$ $Ci^2 = 1 + \frac{1}{2} C(i^2 + 2i + 1) + \frac{1}{2} C(i^2 - 2i + 1)$ $Ci^2 = 1 + \frac{1}{2}Ci^2 + Ci + \frac{1}{2}C + \frac{1}{2}Ci^2 - Ci + \frac{1}{2}C$ $Ci^2 = 1 + (Ci^2) + (C)$ $0 = 1 + C \implies C = -1$.
    
- So, our particular solution is $E_i^{(p)} = -i^2$.
    

**4. Find the General Solution:**

- The full solution is $E_i = E_i^{(h)} + E_i^{(p)} = A + Bi - i^2$.
    
- Now, use the boundary conditions to find $A$ and $B$.
    
- $E_0 = 0 \implies 0 = A + B(0) - 0^2 \implies A = 0$.
    
- $E_N = 0 \implies 0 = A + B(N) - N^2$ $0 = 0 + BN - N^2$ $BN = N^2 \implies B = N$.
    

**5. Final Answer:**

- Substitute $A=0$ and $B=N$ back into the general solution: $E_i = Ni - i^2 = i(N-i)$
    

**Key Takeaway:** The exact same LTP/Recurrence setup from the original problem can be modified (by adding the "1" for the current step) to solve for expected duration. The math (solving the recurrence) is slightly different but follows the same principles.