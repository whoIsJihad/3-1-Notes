

This note covers the key proofs and problems from your notes on the axioms of probability, inclusion-exclusion, the Birthday and Matching problems, and the fundamentals of conditional probability (LTP, Bayes' Rule).

## Section 1: Proofs from the Axioms of Probability

These proofs are the fundamental building blocks. The goal is to prove them using _only_ the three axioms of probability.

### Proof 1: The Complement Rule

**Prove:** $P(A^c) = 1 - P(A)$

**Derivation:**

1. We know that the sample space $S$ can be partitioned into $A$ and its complement $A^c$.
    
2. Therefore, $S = A \cup A^c$.
    
3. By definition, $A$ and $A^c$ are disjoint (mutually exclusive).
    
4. From **Axiom 3** (Additivity for disjoint sets): $P(S) = P(A) + P(A^c)$.
    
5. From **Axiom 2** (Probability of sample space): $P(S) = 1$.
    
6. Substituting (5) into (4): $1 = P(A) + P(A^c)$.
    
7. Rearranging gives the result: $P(A^c) = 1 - P(A)$.
    

### Proof 2: Probability of the Empty Set

**Prove:** $P(\emptyset) = 0$

**Derivation:**

1. We can use the Complement Rule we just proved. The complement of the sample space $S$ is the empty set $\emptyset$.
    
2. So, $P(\emptyset) = P(S^c)$.
    
3. Using the Complement Rule: $P(S^c) = 1 - P(S)$.
    
4. Using **Axiom 2**: $P(S) = 1$.
    
5. Therefore: $P(\emptyset) = 1 - 1 = 0$.
    

### Proof 3: Monotonicity

**Prove:** If $A \subseteq B$, then $P(A) \le P(B)$. (If an event is a subset of another, its probability is smaller or equal).

**Derivation:**

1. If $A \subseteq B$, we can write $B$ as the union of two disjoint sets: $A$ and the part of $B$ that is not in $A$.
    
2. So, $B = A \cup (B \cap A^c)$.
    
3. These two sets, $A$ and $(B \cap A^c)$, are disjoint.
    
4. By **Axiom 3**: $P(B) = P(A) + P(B \cap A^c)$.
    
5. By **Axiom 1** (Non-negativity): $P(B \cap A^c) \ge 0$.
    
6. Therefore, $P(B) \ge P(A) + 0$, which means $P(B) \ge P(A)$.
    

### Proof 4: Inclusion-Exclusion (for 2 sets)

**Prove:** $P(A \cup B) = P(A) + P(B) - P(A \cap B)$

**Derivation:**

1. We can't use Axiom 3 directly on $A$ and $B$, as they are not necessarily disjoint. The strategy is to break $A \cup B$ into disjoint pieces.
    
2. $A \cup B$ can be written as the disjoint union: $A \cup B = A \cup (B \cap A^c)$.
    
3. By **Axiom 3**: $P(A \cup B) = P(A) + P(B \cap A^c)$.
    
4. Now let's look at $B$. We can also break $B$ into two disjoint pieces: $B = (B \cap A) \cup (B \cap A^c)$.
    
5. By **Axiom 3**: $P(B) = P(B \cap A) + P(B \cap A^c)$.
    
6. Rearranging (5), we get: $P(B \cap A^c) = P(B) - P(B \cap A)$.
    
7. Now, substitute this expression for $P(B \cap A^c)$ back into equation (3): $P(A \cup B) = P(A) + [ P(B) - P(B \cap A) ]$
    
8. This gives the result: $P(A \cup B) = P(A) + P(B) - P(A \cap B)$.
    

## Section 2: Principle of Inclusion-Exclusion (PIE) Problems

### Problem 5: The Matching Problem (de Montmort's Problem)

**Problem:** You have $n$ letters addressed to $n$ different people and $n$ pre-addressed envelopes. You randomly stuff one letter into each envelope. What is the probability that _at least one_ letter gets into the correct envelope?

**Derivation (This is a major proof!):**

1. This is a perfect problem for the Principle of Inclusion-Exclusion (PIE).
    
2. Let $A_i$ be the event that letter $i$ goes into the correct envelope (envelope $i$).
    
3. We want to find $P(\text{at least one match}) = P(A_1 \cup A_2 \cup \dots \cup A_n)$.
    
4. The PIE formula is: $P(\cup A_i) = \sum P(A_i) - \sum_{i<j} P(A_i \cap A_j) + \sum_{i<j<k} P(A_i \cap A_j \cap A_k) - \dots + (-1)^{n+1} P(A_1 \cap \dots \cap A_n)$
    
5. Let's calculate the terms. The total number of outcomes (permutations) is $n!$.
    
    - $S_1 = \sum P(A_i)$: $P(A_i)$ is the probability letter $i$ is correct. If letter $i$ is in envelope $i$, the other $n-1$ letters can be arranged in $(n-1)!$ ways. $P(A_i) = \frac{(n-1)!}{n!} = \frac{1}{n}$. There are $\binom{n}{1}$ terms in this sum, all equal. $S_1 = \binom{n}{1} \cdot \frac{1}{n} = n \cdot \frac{1}{n} = 1$.
        
    - $S_2 = \sum P(A_i \cap A_j)$: $P(A_i \cap A_j)$ is the prob. letters $i$ and $j$ are correct. The other $n-2$ letters can be arranged in $(n-2)!$ ways. $P(A_i \cap A_j) = \frac{(n-2)!}{n!}$. There are $\binom{n}{2}$ pairs, so $\binom{n}{2}$ terms in this sum. $S_2 = \binom{n}{2} \cdot \frac{(n-2)!}{n!} = \frac{n(n-1)}{2!} \cdot \frac{(n-2)!}{n!} = \frac{n!}{2!(n-2)!} \cdot \frac{(n-2)!}{n!} = \frac{1}{2!}$.
        
    - $S_k = \sum P(A_1 \cap \dots \cap A_k)$: By the same logic, $P(k \text{ specific letters are correct}) = \frac{(n-k)!}{n!}$. There are $\binom{n}{k}$ such terms. $S_k = \binom{n}{k} \cdot \frac{(n-k)!}{n!} = \frac{n!}{k!(n-k)!} \cdot \frac{(n-k)!}{n!} = \frac{1}{k!}$.
        
6. **Plug these back into the PIE formula:** $P(\cup A_i) = S_1 - S_2 + S_3 - S_4 + \dots + (-1)^{n+1} S_n$ $P(\cup A_i) = 1 - \frac{1}{2!} + \frac{1}{3!} - \frac{1}{4!} + \dots + (-1)^{n+1} \frac{1}{n!}$
    
7. **For large** $n$**:** This sum approaches the Taylor series for $1 - e^{-1}$. So, $P(\text{at least one match}) \approx 1 - 1/e \approx 0.632$.
    

### Proof 6: Boole's Inequality

**Prove:** $P(A_1 \cup A_2 \cup \dots \cup A_n) \le P(A_1) + P(A_2) + \dots + P(A_n)$

**Derivation (Proof by Induction):**

1. **Base Case (**$n=2$**):** We want to show $P(A_1 \cup A_2) \le P(A_1) + P(A_2)$. From the Inclusion-Exclusion proof (Proof 4), we know: $P(A_1 \cup A_2) = P(A_1) + P(A_2) - P(A_1 \cap A_2)$. By **Axiom 1**, $P(A_1 \cap A_2) \ge 0$. Therefore, $P(A_1 \cup A_2) \le P(A_1) + P(A_2)$. The base case holds.
    
2. **Inductive Step:** Assume the inequality holds for $n$ events (this is our inductive hypothesis). $P(\cup_{i=1}^n A_i) \le \sum_{i=1}^n P(A_i)$.
    
3. We must prove it holds for $n+1$ events: $P(\cup_{i=1}^{n+1} A_i) \le \sum_{i=1}^{n+1} P(A_i)$.
    
4. Let $B = \cup_{i=1}^n A_i$.
    
5. Then $P(\cup_{i=1}^{n+1} A_i) = P(B \cup A_{n+1})$.
    
6. Using our base case ($n=2$) on $B$ and $A_{n+1}$: $P(B \cup A_{n+1}) \le P(B) + P(A_{n+1})$.
    
7. Now, apply the inductive hypothesis to $P(B)$: $P(B) = P(\cup_{i=1}^n A_i) \le \sum_{i=1}^n P(A_i)$.
    
8. Substitute (7) into (6): $P(B \cup A_{n+1}) \le \left( \sum_{i=1}^n P(A_i) \right) + P(A_{n+1}) = \sum_{i=1}^{n+1} P(A_i)$.
    
9. This completes the proof.
    

## Section 3: Classic Probability Problems

### Problem 7: The Birthday Problem

**Problem:** In a room of $k$ people, what is the probability that at least two of them share a birthday? (Assume 365 days, all equally likely).

**Derivation:**

1. This is a classic "complement" problem. It's much easier to calculate the probability of the complement event, $P(\text{no matches})$.
    
2. $P(\text{at least one match}) = 1 - P(\text{no matches})$.
    
3. Let's find $P(\text{no matches})$.
    
4. **Total Outcomes:** The sample space size. Each of the $k$ people can have 1 of 365 birthdays. By the multiplication rule, $|S| = 365 \cdot 365 \cdot \dots \cdot 365 = 365^k$.
    
5. **Favorable Outcomes (No Matches):**
    
    - Person 1 can have any of 365 birthdays.
        
    - Person 2 must not match Person 1, so they have 364 choices.
        
    - Person 3 must not match 1 or 2, so they have 363 choices.
        
    - ...
        
    - Person $k$ has $(365 - k + 1)$ choices.
        
    - Total favorable outcomes = $365 \cdot 364 \cdot \dots \cdot (365-k+1)$. This is a permutation: $P(365, k) = \frac{365!}{(365-k)!}$.
        
6. **Calculate Probability:** $P(\text{no matches}) = \frac{\text{Favorable Outcomes}}{\text{Total Outcomes}} = \frac{365 \cdot 364 \cdot \dots \cdot (365-k+1)}{365^k}$ $P(\text{no matches}) = 1 \cdot \left(\frac{364}{365}\right) \cdot \left(\frac{363}{365}\right) \cdot \dots \cdot \left(\frac{365-k+1}{365}\right)$.
    
7. **Final Answer:** $P(\text{at least one match}) = 1 - \frac{365!}{(365-k)! \cdot 365^k}$. (The famous result is that for $k=23$, this probability becomes $> 0.5$).
    

## Section 4: Conditional Probability

### Proof 8: The Law of Total Probability (LTP)

**Prove:** Let $A_1, A_2, \dots, A_n$ be a partition of the sample space $S$ (disjoint and their union is $S$). For any event $B$, prove: $P(B) = \sum_{i=1}^n P(B|A_i)P(A_i)$

**Derivation:**

1. The sets $A_i$ partition $S$. Therefore, the sets $(B \cap A_i)$ partition $B$. That is, $B = (B \cap A_1) \cup (B \cap A_2) \cup \dots \cup (B \cap A_n)$.
    
2. Crucially, all the sets $(B \cap A_i)$ are disjoint (because the $A_i$ are disjoint).
    
3. By **Axiom 3** (Additivity for disjoint sets): $P(B) = P(B \cap A_1) + P(B \cap A_2) + \dots + P(B \cap A_n) = \sum_{i=1}^n P(B \cap A_i)$.
    
4. From the definition of conditional probability, we know $P(B \cap A_i) = P(B|A_i)P(A_i)$.
    
5. Substitute (4) into (3): $P(B) = \sum_{i=1}^n P(B|A_i)P(A_i)$. This completes the proof.
    

### Proof 9: Bayes' Rule

**Prove:** For any events $A$ and $B$ (with $P(B) > 0$), $P(A|B) = \frac{P(B|A)P(A)}{P(B)}$

**Derivation:**

1. Start with the definition of conditional probability for $P(A|B)$: (1) $P(A|B) = \frac{P(A \cap B)}{P(B)}$
    
2. Now write the definition for $P(B|A)$: (2) $P(B|A) = \frac{P(B \cap A)}{P(A)}$
    
3. Rearrange (2) to solve for $P(B \cap A)$, which is the same as $P(A \cap B)$: (3) $P(A \cap B) = P(B|A)P(A)$
    
4. Substitute the expression from (3) into the numerator of (1): $P(A|B) = \frac{P(B|A)P(A)}{P(B)}$. (Often, the denominator $P(B)$ is expanded using the Law of Total Probability).
    

### Problem 10: The "Two-Card Hand" (Ace of Spades Problem)

This is a classic problem that highlights the importance of defining your sample space.

**Problem:** You are dealt a 2-card hand from a standard 52-card deck. (a) What is the probability you have two aces, given that you _have at least one ace_? (b) What is the probability you have two aces, given that you _have the Ace of Spades_?

**Solution:** Let $E$ be the event "have two aces". The total number of 2-card hands is $\binom{52}{2} = 1326$. The number of ways to have two aces is $\binom{4}{2} = 6$. So, $P(E) = 6/1326$.

**(a) Given "at least one ace"** Let $F$ be the event "have at least one ace". We want $P(E|F) = \frac{P(E \cap F)}{P(F)}$.

- $E \cap F$: "Have two aces" AND "have at least one ace". This is just the event $E$, "have two aces". So $P(E \cap F) = P(E) = 6/1326$.
    
- $P(F)$: It's easiest to find $P(F^c)$ = "have no aces". $P(F^c) = \frac{\binom{48}{2}}{\binom{52}{2}} = \frac{1128}{1326}$. $P(F) = 1 - P(F^c) = 1 - 1128/1326 = \frac{198}{1326}$.
    
- **Answer (a):** $P(E|F) = \frac{6/1326}{198/1326} = \frac{6}{198} = \frac{1}{33}$.
    

**(b) Given "have the Ace of Spades"** Let $G$ be the event "have the Ace of Spades". We want $P(E|G) = \frac{P(E \cap G)}{P(G)}$.

- $E \cap G$: "Have two aces" AND "have the Ace of Spades". This means your hand is {Ace of Spades, one of the other 3 aces}. The number of ways for this is $\binom{1}{1} \times \binom{3}{1} = 3$. $P(E \cap G) = 3/1326$.
    
- $P(G)$: "Have the Ace of Spades". This means your hand is {Ace of Spades, one of the other 51 cards}. The number of ways for this is $\binom{1}{1} \times \binom{51}{1} = 51$. $P(G) = 51/1326$.
    
- **Answer (b):** $P(E|G) = \frac{3/1326}{51/1326} = \frac{3}{51} = \frac{1}{17}$.
    

**Key Takeaway:** $1/17 \neq 1/33$. Knowing _which_ ace you have provides more information and changes the probability.

### Proof 11: Independence and Complements

**Prove:** If $A$ and $B$ are independent events, then $A^c$ and $B^c$ are also independent.

**Derivation:**

1. **Goal:** We need to show that $P(A^c \cap B^c) = P(A^c)P(B^c)$.
    
2. Start with the left side, $P(A^c \cap B^c)$.
    
3. By De Morgan's Law: $A^c \cap B^c = (A \cup B)^c$.
    
4. So, $P(A^c \cap B^c) = P((A \cup B)^c)$.
    
5. By the Complement Rule (Proof 1): $P((A \cup B)^c) = 1 - P(A \cup B)$.
    
6. By Inclusion-Exclusion (Proof 4): $1 - [P(A) + P(B) - P(A \cap B)]$.
    
7. Distribute the negative sign: $1 - P(A) - P(B) + P(A \cap B)$.
    
8. **Use Independence:** Since $A$ and $B$ are independent, $P(A \cap B) = P(A)P(B)$.
    
9. Substitute this in: $1 - P(A) - P(B) + P(A)P(B)$.
    
10. **Factor the expression:** This is the key algebraic step. $(1 - P(A)) - P(B)(1 - P(A))$ $= (1 - P(A)) (1 - P(B))$
    
11. By the Complement Rule, $(1 - P(A)) = P(A^c)$ and $(1 - P(B)) = P(B^c)$.
    
12. Therefore, $P(A^c \cap B^c) = P(A^c)P(B^c)$. This proves $A^c$ and $B^c$ are independent.