tags:

- cse/probability
    
- foundations
    
- combinatorics
    
- conditional-probability
    

# Probability Theory for Computer Science

## Table of Contents

### Part 1: Foundations of Probability

- Sample Space, Outcomes, and Events
    
- Naive Definition of Probability
    
- Axiomatic Definition of Probability
    
- Properties of Probability
    

### Part 2: Counting and Combinatorics

- The Multiplication Rule
    
- Permutations and Combinations
    
- Sampling Tables
    
- Story Proofs and Combinatorial Identities
    
- Vandermonde's Identity
    

### Part 3: Conditional Probability and Independence

- Conditional Probability
    
- The Law of Total Probability
    
- Bayes' Rule
    
- Independence of Events
    
- Principle of Inclusion-Exclusion
    

## Part 1: Foundations of Probability

### 1.1 - Sample Space, Outcomes, and Events

#tags: #probability #foundations #sample-space #events

#### Definitions

- **Experiment**: Any procedure that can be repeated and has a well-defined set of possible results (e.g., flipping a coin, measuring network latency).
    
- **Sample Space (**$\mathbf{S}$**)**: The set of all possible outcomes of an experiment.
    
- **Outcome**: A single element of the sample space $S$.
    
- **Event (**$\mathbf{A}$**)**: A **subset** of the sample space $S$. An event is said to have occurred if the outcome of the experiment is an element of the set $A$.
    

#### Example: Flipping a Coin Twice

- **Experiment**: Flipping a fair coin twice and recording the sequence.
    
- **Sample Space (**$S$**)**: $S = \{HH, HT, TH, TT\}$.
    
- **Event A**: "Getting at least one head." $A = \{HH, HT, TH\}$.
    
- **Event C**: "Getting two heads." $C = \{HH\}$.
    

### 1.2 - Naive Definition of Probability

#tags: #probability #foundations #naive-probability

#### The Naive Definition

The **Naive Definition of Probability** is used when every outcome in the sample space $S$ is **equally likely**.

The formula is:

$$P(A) = \frac{\text{Number of Favorable Outcomes}}{\text{Total Number of Outcomes}}$$

Using set notation, where $|A|$ is the cardinality of event $A$:

$$P(A) = \frac{|A|}{|S|}$$

#### Example: Flipping a Coin Twice

For the event $B$: "Getting exactly one tail," $B = \{HT, TH\}$.

$$P(B) = \frac{|B|}{|S|} = \frac{2}{4} = 0.5$$

#### Limitations of the Naive Definition

This definition fails if:

1. Outcomes are **not equally likely** (e.g., a biased coin).
    
2. The sample space $S$ is **infinite** (e.g., picking a random real number).
    

### 1.3 - Axiomatic Definition of Probability

#tags: #probability #foundations #axioms-of-probability

The **Axiomatic Definition** provides a formal foundation that is applicable regardless of whether outcomes are equally likely or if the sample space is infinite.

A probability function $P$, which maps an event $A$ to a real number $P(A)$, must satisfy three axioms:

##### Axiom 1: Non-Negativity

The probability of any event $A$ is non-negative.

$$P(A) \ge 0$$

##### Axiom 2: Normalization

The probability of the entire sample space $S$ is 1.

$$P(S) = 1$$

##### Axiom 3: Additivity for Disjoint Events

For any sequence of mutually exclusive (disjoint) events $A_1, A_2, A_3, \dots$ ($A_i \cap A_j = \emptyset$ for $i \ne j$):

$$P(A_1 \cup A_2 \cup A_3 \cup \dots) = P(A_1) + P(A_2) + P(A_3) + \dots$$

### 1.4 - Properties of Probability

#tags: #probability #foundations #probability-rules

#### Property 1: Probability of the Complement (Complement Rule)

The probability of an event $A$'s complement ($A^c$, the event that $A$ does not occur) is:

$$P(A^c) = 1 - P(A)$$

#### Property 2: Monotonicity

If event $A$ is a subset of event $B$ ($A \subseteq B$), then:

$$P(A) \le P(B)$$

#### Property 3: Inclusion-Exclusion for Two Events

For any two events $A$ and $B$, the probability of their union is:

$$P(A \cup B) = P(A) + P(B) - P(A \cap B)$$

**Practice Problem Solution:** Let $C$ be Computer Science and $M$ be Math. $P(C)=0.6$, $P(M)=0.5$, $P(C \cap M)=0.2$.

$$P(C \cup M) = 0.6 + 0.5 - 0.2 = 0.9$$

## Part 2: Counting and Combinatorics

### 2.1 - The Multiplication Rule

#tags: #probability #combinatorics #counting #multiplication-rule

#### The Multiplication Rule of Counting

If an experiment has $r$ sequential stages, and the $i$-th stage has $n_i$ possible outcomes, the total number of outcomes is the product:

$$\text{Total Outcomes} = n_1 \cdot n_2 \cdot n_3 \cdot \dots \cdot n_r$$

#### Example: Full House in Poker

The number of ways to form a Full House (3 of one rank, 2 of another) is:

$$\text{Total Full Houses} = \binom{13}{1} \cdot \binom{4}{3} \cdot \binom{12}{1} \cdot \binom{4}{2} = 13 \cdot 4 \cdot 12 \cdot 6 = 3744$$

### 2.2 - Permutations and Combinations

#tags: #probability #combinatorics #counting #permutations #combinations

#### Permutations: Order Matters

The number of permutations of $k$ objects chosen from $n$ distinct objects is $P(n, k)$:

$$P(n, k) = \frac{n!}{(n-k)!}$$

#### Combinations: Order Does Not Matter

The number of combinations of $k$ objects chosen from $n$ distinct objects is $C(n, k)$ or $\binom{n}{k}$:

$$\binom{n}{k} = \frac{n!}{k! (n-k)!}$$

#### Relationship

$$P(n, k) = \binom{n}{k} \cdot k!$$

### 2.3 - Sampling Tables

#tags: #probability #combinatorics #counting #sampling

The "Fourfold Way" for choosing $k$ objects from $n$:

|**Order Matters?**|**Replacement?**|**Description**|**Formula**|
|---|---|---|---|
|Yes|Yes|Ordered, with replacement|$n^k$|
|Yes|No|Ordered, without replacement (Permutation)|$P(n, k)$|
|No|Yes|Unordered, with replacement (Stars and Bars)|$\binom{n+k-1}{k}$|
|No|No|Unordered, without replacement (Combination)|$\binom{n}{k}$|

### 2.4 - Story Proofs and Combinatorial Identities

#tags: #probability #combinatorics #proofs #story-proofs

A **Story Proof** proves an identity by showing that both sides count the same set of objects.

##### Identity 1: The Symmetry Identity

$$\binom{n}{k} = \binom{n}{n-k}$$

_Story_: Choosing $k$ people for a committee (LHS) is the same as choosing $n-k$ people to exclude from the committee (RHS).

##### Identity 2: The Committee-President Identity

$$k \cdot \binom{n}{k} = n \cdot \binom{n-1}{k-1}$$

_Story_: The total number of ways to choose a $k$-person committee with one designated president.

### 2.5 - Vandermonde's Identity

#tags: #probability #combinatorics #proofs #story-proofs #vandermonde-identity

#### Vandermonde's Identity

For non-negative integers $m$, $n$, and $k$:

$$\binom{m+n}{k} = \sum_{j=0}^{k} \binom{m}{j} \binom{n}{k-j}$$

_Story_: The number of ways to choose a committee of $k$ people from $m$ men and $n$ women (LHS) is equal to the sum of choosing $j$ men and $k-j$ women, for all possible values of $j$ (RHS).

## Part 3: Conditional Probability and Independence

### 3.1 - Conditional Probability

#tags: #probability #conditional-probability

#### Definition of Conditional Probability

The probability of event $A$ occurring, given that event $B$ has already occurred ($P(B) > 0$):

$$P(A \mid B) = \frac{P(A \cap B)}{P(B)}$$

#### The Multiplication Rule (Chain Rule)

$$P(A \cap B) = P(A \mid B) \cdot P(B)$$

For multiple events:

$$P(A_1 \cap A_2 \cap \dots \cap A_n) = P(A_1) \cdot P(A_2 \mid A_1) \cdot P(A_3 \mid A_1 \cap A_2) \cdot \dots$$

#### Practice Problem Solution (Family with Two Children)

$A$: Both boys ($\{BB\}$). $B$: At least one boy ($\{BB, BG, GB\}$).

$$P(A \mid B) = \frac{P(A \cap B)}{P(B)} = \frac{P(\{BB\})}{P(\{BB, BG, GB\})} = \frac{1/4}{3/4} = \frac{1}{3}$$

### 3.2 - The Law of Total Probability

#tags: #probability #conditional-probability #law-of-total-probability

#### The Law of Total Probability (LOTP)

If $A_1, A_2, \dots, A_n$ is a partition of the sample space, then for any event $B$:

$$P(B) = P(B \mid A_1) P(A_1) + P(B \mid A_2) P(A_2) + \dots + P(B \mid A_n) P(A_n)$$

#### Example: Defective Bolts from a Factory

Let $D$ be the defective event, and $A, B, C$ be the machine events.

$$P(D) = P(D \mid A) P(A) + P(D \mid B) P(B) + P(D \mid C) P(C)$$$$P(D) = (0.05 \cdot 0.25) + (0.04 \cdot 0.35) + (0.02 \cdot 0.40) = 0.0345$$

### 3.3 - Bayes' Rule

#tags: #probability #conditional-probability #bayes-rule #inference

#### Bayes' Rule

Describes how to update the probability of a hypothesis ($A$) based on new evidence ($B$):

$$P(A \mid B) = \frac{P(B \mid A) P(A)}{P(B)}$$

- $\mathbf{P(A)}$: Prior
    
- $\mathbf{P(B \mid A)}$: Likelihood
    
- $\mathbf{P(A \mid B)}$: Posterior
    

#### Example: Medical Diagnosis

If $P(D)=0.01$ and $P(T \mid D)=0.95$, and $P(T)=0.0590$ (calculated by LOTP):

$$P(D \mid T) = \frac{P(T \mid D) P(D)}{P(T)} = \frac{0.95 \cdot 0.01}{0.0590} \approx 0.161$$

### 3.4 - Independence of Events

#tags: #probability #independence

#### Independence of Events

Two events, $A$ and $B$, are **independent** if the occurrence of one does not affect the probability of the other.

**Formal Definition (Joint Probability):** $A$ and $B$ are independent if:

$$P(A \cap B) = P(A) \cdot P(B)$$

**Formal Definition (Conditional Probability):** $A$ and $B$ are independent if:

$$P(A \mid B) = P(A)$$

### 3.5 - Principle of Inclusion-Exclusion

#tags: #probability #combinatorics #inclusion-exclusion

#### The Principle of Inclusion-Exclusion

The formula to find the probability of the union of multiple sets by alternating between adding single probabilities and subtracting intersections.

**Formula for Three Events:**

$$\begin{aligned} P(A \cup B \cup C) &= P(A) + P(B) + P(C) \\ &\quad - (P(A \cap B) + P(A \cap C) + P(B \cap C)) \\ &\quad + P(A \cap B \cap C) \end{aligned}$$

**General Formula:**

$$P\left(\bigcup_{i=1}^{n} A_i\right) = \sum_{i} P(A_i) - \sum_{i<j} P(A_i \cap A_j) + \sum_{i<j<k} P(A_i \cap A_j \cap A_k) - \dots + (-1)^{n+1} P\left(\bigcap_{i=1}^{n} A_i\right)$$

#### Application: De Montmort's Matching Problem

The probability that at least one card is in its natural position after shuffling $n$ cards is:

$$P(\text{at least one match}) = \sum_{k=1}^{n} (-1)^{k+1} \frac{1}{k!} = 1 - \frac{1}{2!} + \frac{1}{3!} - \dots + (-1)^{n+1} \frac{1}{n!}$$

This value approaches $1 - \frac{1}{e} \approx 0.632$ as $n \to \infty$.