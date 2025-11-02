# A Course in Probability and Statistics


---

## Part I: The Language of Chance - Foundational Probability

### 1.1 - The Idea of Probability

Probability theory is the mathematical framework for quantifying uncertainty. It provides a set of tools to model and reason about random phenomena, transforming ambiguity into precise, quantitative statements. The study of probability began with the analysis of games of chance, but its principles have since become indispensable across a vast array of scientific and engineering disciplines.1

#### Applications Across Disciplines

The universal applicability of probabilistic reasoning is one of its most powerful features. It is not merely a branch of mathematics but a fundamental framework for reasoning in any domain where perfect knowledge is absent.

- **Economics and Machine Learning**: In these fields, probability is used to model complex systems, make predictions under uncertainty, and design algorithms that learn from data. For example, a machine learning model might assign a probability to a given email being spam.1
    
- **Law and History**: Probability theory is used to assess the authenticity and reliability of evidence. A famous example is the Mosteller-Wallace study of the Federalist Papers. By analyzing the frequency of certain words, they used Bayesian statistical methods to determine the authorship of disputed essays with a high degree of certainty. This demonstrates that probability is a tool for formalizing inference and reasoning, even in the humanities.1
    

#### Historical Context

The formal study of probability was initiated in the 17th century by mathematicians Blaise Pascal and Pierre de Fermat, who corresponded about problems related to games of chance. Their work laid the groundwork for a systematic theory of randomness. Later, figures like Isaac Newton contributed to its development, solidifying its place as a cornerstone of modern science.1

### 1.2 - Sample Spaces and Events

To formalize the study of probability, we must first define its fundamental components: the experiment, the sample space, and the event.

#### Core Definitions

- **Experiment**: A procedure or process that yields an uncertain outcome. Examples include flipping a coin, rolling a die, or measuring the response time of a server.1
    
- **Sample Space ($S$)**: The set of all possible outcomes of an experiment. The sample space must be exhaustive (it includes all possibilities) and its elements must be mutually exclusive (no two outcomes can occur simultaneously).1
    
- **Event ($A$)**: Any subset of the sample space ($A \subseteq S$). An event represents the specific outcome or set of outcomes whose probability we wish to compute.1
    

**Example: Coin Flips**

- **Experiment**: Flip a fair coin twice.
    
- **Sample Space ($S$)**: The set of all four possible outcomes is $S = \{HH, HT, TH, TT\}$.
    
- **Event ($A$)**: We might be interested in the event "getting at least one head." This corresponds to the subset $A = \{HH, HT, TH\}$.1
    

#### The Naive Definition of Probability

For a large class of simple problems, probability can be calculated using an intuitive definition.

Definition: If an experiment has a finite sample space $S$ in which all outcomes are equally likely, then the probability of an event $A$ is given by:

$$P(A) = \frac{\text{Number of outcomes in } A}{\text{Total number of outcomes in } S} = \frac{|A|}{|S|}$$

This is often stated as the ratio of "favourable outcomes" to "total outcomes".1

**Example: Coin Flips**

Using the experiment of flipping a fair coin twice, let's find the probability of the event $A$ = "getting exactly one head."

- The sample space is $S = \{HH, HT, TH, TT\}$, so $|S| = 4$.
    
- The event is $A = \{HT, TH\}$, so $|A| = 2$.
    
- Assuming a fair coin, all four outcomes are equally likely.
    
- Therefore, $P(A) = \frac{2}{4} = \frac{1}{2}$.
    

#### Limitations of the Naive Definition

The term "naive" is a deliberate signal that this definition, while useful, is built on a fragile assumption: that all outcomes are equally likely. This assumption breaks down in many real-world scenarios 1:

1. **Biased Outcomes**: If the coin were biased (e.g., weighted to favor heads), the outcomes $HH, HT, TH, TT$ would no longer have equal probabilities. The naive formula would yield an incorrect result.
    
2. **Infinite Sample Spaces**: If the experiment is "measure the time until a server fails," the sample space is the set of all non-negative real numbers, which is infinite. The concept of "counting" the number of outcomes becomes meaningless.
    

These limitations create the intellectual need for a more robust and general framework for probability, which is provided by the Axioms of Probability. The naive definition should be seen as an important but limited special case.

#### Practice Problems and Solutions

**Problem 1**: A coin is thrown 3 times. What is the probability that at least one head is obtained? 3

- **Solution**:
    
    - The sample space for 3 coin tosses is $S = \{HHH, HHT, HTH, THH, TTH, THT, HTT, TTT\}$. The total number of outcomes is $|S| = 2^3 = 8$.
        
    - The event of "at least one head" includes all outcomes except for TTT.
        
    - The number of favourable outcomes is 7.
        
    - The probability is $P(\text{at least one head}) = \frac{7}{8}$.
        
    - **Alternative Method (using the complement)**: The complement of "at least one head" is "no heads," which is the event $\{TTT\}$. The probability of this event is $\frac{1}{8}$. Therefore, $P(\text{at least one head}) = 1 - P(\text{no heads}) = 1 - \frac{1}{8} = \frac{7}{8}$.
        

**Problem 2**: What is the probability of getting a sum of 7 when two dice are thrown? 3

- **Solution**:
    
    - When two dice are thrown, the total number of outcomes in the sample space is $6 \times 6 = 36$.
        
    - The favourable outcomes (pairs that sum to 7) are: $(1, 6), (6, 1), (2, 5), (5, 2), (3, 4), (4, 3)$.
        
    - There are 6 favourable outcomes.
        
    - The probability is $P(\text{sum is 7}) = \frac{6}{36} = \frac{1}{6}$.
        

**Problem 3**: From a pack of 52 cards, what is the probability of drawing an ace or a king? 4

- **Solution**:
    
    - The total number of outcomes is 52.
        
    - In a standard deck, there are 4 aces and 4 kings.
        
    - The number of favourable outcomes is $4 (\text{aces}) + 4 (\text{kings}) = 8$.
        
    - The probability is $P(\text{ace or king}) = \frac{8}{52} = \frac{2}{13}$.
        

### 1.3 - Axioms of Probability

To overcome the limitations of the naive definition, modern probability theory is built upon a small set of axioms, first formalized by Andrey Kolmogorov in the 1930s. These axioms do not tell us _how_ to assign probabilities; rather, they provide the rules that any valid probability assignment must follow.1

This approach reframes the problem from simply counting outcomes to defining a consistent system of "measure" for subsets of the sample space. This generalization is the key that unlocks the full power of probability theory, allowing it to handle continuous spaces, biased outcomes, and other complex scenarios where simple counting fails.

#### The Axioms of Probability

A probability space consists of a sample space $S$ and a probability function $P$ that takes an event $A \subseteq S$ as input and returns a real number $P(A)$ such that the following axioms hold 1:

1. **Non-Negativity**: For any event $A$, $P(A) \ge 0$.
    
2. **Normalization**: The probability of the entire sample space is 1, i.e., $P(S) = 1$.
    
3. Additivity for Disjoint Events: For any sequence of disjoint (mutually exclusive) events $A_1, A_2, \dots$ (meaning $A_i \cap A_j = \emptyset$ for $i \neq j$), the probability of their union is the sum of their individual probabilities:
    
    $$P\left(\bigcup_{n=1}^{\infty} A_n\right) = \sum_{n=1}^{\infty} P(A_n)$$
    

#### Key Properties Derived from the Axioms

These three simple axioms are sufficient to derive all the fundamental rules of probability. These rules form a consistent "algebra of probability."

**Property 1: Probability of the Impossible Event**

The probability of the empty set (an impossible event) is 0.

$P(\emptyset) = 0$.1

**Property 2: The Complement Rule**

For any event $A$, the probability that $A$ does not occur, denoted $P(A^c)$, is given by:

$$P(A^c) = 1 - P(A)$$

Proof: The events $A$ and $A^c$ are disjoint and their union is the entire sample space, $A \cup A^c = S$. By Axiom 3, $P(A \cup A^c) = P(A) + P(A^c)$. By Axiom 2, $P(S) = 1$. Therefore, $P(A) + P(A^c) = 1$, which rearranges to the rule.1

**Property 3: The Subset Rule**

If event $A$ is a subset of event $B$ ($A \subseteq B$), then the probability of $A$ is less than or equal to the probability of $B$.

$$P(A) \le P(B)$$

Proof: We can write $B$ as the disjoint union of $A$ and the part of $B$ that is not in $A$, i.e., $B = A \cup (B \cap A^c)$. By Axiom 3, $P(B) = P(A) + P(B \cap A^c)$. Since all probabilities are non-negative (Axiom 1), $P(B \cap A^c) \ge 0$. Therefore, $P(B) \ge P(A)$.1

**Property 4: The Inclusion-Exclusion Principle**

For any two events $A$ and $B$, the probability of their union is:

$$P(A \cup B) = P(A) + P(B) - P(A \cap B)$$

The subtraction of $P(A \cap B)$ is necessary to correct for the fact that simply adding $P(A)$ and $P(B)$ double-counts the outcomes present in their intersection.1

This principle can be generalized to three or more events. For three events $A, B, C$:

$$P(A \cup B \cup C) = P(A) + P(B) + P(C) - P(A \cap B) - P(A \cap C) - P(B \cap C) + P(A \cap B \cap C)$$

#### Practice Problems and Solutions

**Problem 1**: Three dice are rolled together. What is the probability of getting at least one '4'? 3

- **Solution**:
    
    - Directly calculating the probability of getting one '4', two '4's, or three '4's is complicated. It is much simpler to use the Complement Rule.
        
    - Let $A$ be the event of getting at least one '4'.
        
    - The complement event, $A^c$, is getting _no_ '4's on any of the three dice.
        
    - For a single die, the probability of not rolling a '4' is $\frac{5}{6}$.
        
    - Since the three rolls are independent, the probability of not rolling a '4' on all three is:
        
        $$P(A^c) = \frac{5}{6} \times \frac{5}{6} \times \frac{5}{6} = \left(\frac{5}{6}\right)^3 = \frac{125}{216}$$
        
    - Using the complement rule, the probability of getting at least one '4' is:
        
        $$P(A) = 1 - P(A^c) = 1 - \frac{125}{216} = \frac{91}{216}$$
        

**Problem 2**: Given $P(A)=0.4$, $P(B)=0.6$ and $P(A \cup B)=0.8$. What is the value of $P(A \cap B)$? 5

- **Solution**:
    
    - This is a direct application of the Inclusion-Exclusion Principle for two events: $P(A \cup B) = P(A) + P(B) - P(A \cap B)$.
        
    - We can rearrange the formula to solve for $P(A \cap B)$:
        
        $$P(A \cap B) = P(A) + P(B) - P(A \cup B)$$
        
    - Plugging in the given values:
        
        $$P(A \cap B) = 0.4 + 0.6 - 0.8 = 0.2$$
        

---

## Part II: The Art of Counting - Combinatorics

### 2.1 - The Multiplication Rule

The Multiplication Rule, also known as the Fundamental Counting Principle, is the most basic and essential tool in combinatorics. It allows us to calculate the total number of outcomes for a multi-stage experiment by breaking it down into a sequence of simpler steps.6

#### Definition

If an experiment can be described as a sequence of $r$ stages, and:

- There are $n_1$ possible outcomes for the first stage.
    
- For each of these outcomes, there are $n_2$ possible outcomes for the second stage.
    
- ...
    
- For each of the outcomes of the first $r-1$ stages, there are $n_r$ possible outcomes for the $r$-th stage.
    

Then the total number of possible outcomes for the entire experiment is the product:

$$N = n_1 \times n_2 \times \dots \times n_r$$

6

**Example: Ice Cream Choices**

- **Experiment**: Choose an ice cream.
    
- **Stage 1**: Choose a flavor. There are 3 options (e.g., vanilla, chocolate, strawberry). So, $n_1 = 3$.
    
- **Stage 2**: Choose a serving type. There are 2 options (e.g., cone, cup). So, $n_2 = 2$.
    
- **Total Outcomes**: The total number of different ice cream combinations is $N = n_1 \times n_2 = 3 \times 2 = 6$.1
    

#### Application to Computer Science: State Space Size

The multiplication rule is the primary tool for determining the size of the "state space" in many computational problems. The state space is the set of all possible configurations a system can be in. Understanding its size is often the first step in analyzing a problem's complexity.

- **Password Security**: Consider an 8-character password where each character can be an uppercase letter, a lowercase letter, or a digit. The number of choices for each character is $26 + 26 + 10 = 62$. Using the multiplication rule, the total number of possible passwords is $62^8$. This large state space is what makes a brute-force attack computationally infeasible.
    
- **Algorithm Analysis**: In algorithms that explore a set of possibilities, the state space represents all possible configurations. The multiplication rule helps quantify the size of this space, which directly relates to the algorithm's time complexity.
    

#### Practice Problems and Solutions

**Problem 1**: A person owns 4 pairs of pants, 8 shirts, 2 pairs of shoes, and 1 jacket. How many different outfits can they wear to school if they must wear one of each item? 7

- **Solution**:
    
    - This is a 4-stage experiment.
        
    - Stage 1 (Pants): 4 choices.
        
    - Stage 2 (Shirts): 8 choices.
        
    - Stage 3 (Shoes): 2 choices.
        
    - Stage 4 (Jacket): 1 choice.
        
    - Total Outfits = $4 \times 8 \times 2 \times 1 = 64$.
        
    - The person can wear 64 different outfits.
        

Problem 2: How many three-letter “words” can be made from the 4 letters “FGHI” if:

a) Repetition of letters is allowed.

b) Repetition of letters is not allowed. 7

- **Solution**:
    
    - **a) Repetition Allowed**: This is a 3-stage experiment. For each position in the word, there are 4 choices.
        
        - Total words = $4 \times 4 \times 4 = 4^3 = 64$.
            
    - **b) Repetition Not Allowed**: The number of choices decreases at each stage.
        
        - Stage 1 (First letter): 4 choices.
            
        - Stage 2 (Second letter): 3 remaining choices.
            
        - Stage 3 (Third letter): 2 remaining choices.
            
        - Total words = $4 \times 3 \times 2 = 24$.
            

**Problem 3**: Suppose a password must be chosen with a lower-case letter first, a digit second, and an upper-case letter third. How many ways are there to do this? 6

- **Solution**:
    
    - This is a 3-stage experiment with specific constraints at each stage.
        
    - Stage 1 (Lower-case letter): 26 choices.
        
    - Stage 2 (Digit): 10 choices (0-9).
        
    - Stage 3 (Upper-case letter): 26 choices.
        
    - Total passwords = $26 \times 10 \times 26 = 6760$.
        

### 2.2 - Permutations and Combinations (Sampling Tables)

Many counting problems can be framed as "choosing $k$ objects from a set of $n$ objects." To solve these problems systematically, we must answer two key questions about the sampling process:

1. **Does the order of selection matter?** (Is `AB` different from `BA`?)
    
2. **Is replacement allowed?** (Can the same object be chosen more than once?)
    

The answers to these questions determine which formula to use. The real skill is translating a word problem into the correct combinatorial model.

#### The Four Scenarios of Sampling

The two questions create four distinct scenarios, which can be organized into a "sampling table" for clarity.1

||**Order Matters (Permutations)**|**Order Does Not Matter (Combinations)**|
|---|---|---|
|**With Replacement**|$n^k$|$\binom{n+k-1}{k}$|
|**Without Replacement**|$P(n,k) = \frac{n!}{(n-k)!}$|$C(n,k) = \binom{n}{k} = \frac{n!}{k!(n-k)!}$|

Let's examine each case.

1. Order Matters, With Replacement

This is a direct application of the multiplication rule. For each of the $k$ selections, we have $n$ choices.

- **Formula**: $n^k$
    
- **Example**: How many 3-digit PINs can be formed using digits 0-9? Here $n=10, k=3$. The answer is $10^3 = 1000$.
    

2. Order Matters, Without Replacement (Permutations)

The number of choices decreases with each selection.

- **Formula**: $P(n,k) = n \times (n-1) \times \dots \times (n-k+1) = \frac{n!}{(n-k)!}$
    
- **Example**: How many ways can we award Gold, Silver, and Bronze medals to 3 athletes from a group of 10? Order matters. $P(10,3) = 10 \times 9 \times 8 = 720$.
    

3. Order Does Not Matter, Without Replacement (Combinations)

This is the most common scenario in probability problems. We start with the number of permutations, $P(n,k)$, and then divide by $k!$ to correct for overcounting, since any arrangement of the same $k$ objects is considered the same outcome.

- **Formula**: $C(n,k) = \binom{n}{k} = \frac{P(n,k)}{k!} = \frac{n!}{k!(n-k)!}$
    
- **Example**: How many ways can we choose a committee of 3 people from a group of 10? Order does not matter. $\binom{10}{3} = \frac{10 \times 9 \times 8}{3 \times 2 \times 1} = 120$.
    

4. Order Does Not Matter, With Replacement (Stars and Bars)

This case is solved using a technique called "Stars and Bars." Imagine we want to choose $k$ items from $n$ categories. We can represent the $k$ items as "stars" ($\star$) and separate the $n$ categories with $n-1$ "bars" ($|$). The problem becomes equivalent to arranging $k$ stars and $n-1$ bars in a sequence of $n+k-1$ positions.

- **Formula**: $\binom{n+k-1}{k}$
    
- **Example**: An ice cream shop has 5 flavors ($n=5$). How many ways can you choose 3 scoops ($k=3$)? You can have multiple scoops of the same flavor. This is equivalent to arranging 3 stars and $5-1=4$ bars. The answer is $\binom{5+3-1}{3} = \binom{7}{3} = 35$.1
    

#### Example: Probability of a Full House

Calculating the probability of a "full house" (3 cards of one kind, 2 cards of another) in a 5-card poker hand is a classic application of combinations.1

- Sample Space: The total number of 5-card hands from a 52-card deck. Order does not matter.
    
    $$|S| = \binom{52}{5} = 2,598,960$$
    
- **Event Space (Full House)**: We model the structure of a full house as a sequence of choices.
    
    1. **Choose the rank for the triple** (e.g., Aces, Kings): $\binom{13}{1}$ ways.
        
    2. **Choose the 3 suits for that rank**: $\binom{4}{3}$ ways.
        
    3. **Choose the rank for the pair**: From the remaining 12 ranks. $\binom{12}{1}$ ways.
        
    4. **Choose the 2 suits for that rank**: $\binom{4}{2}$ ways.
        
    
    - By the multiplication rule, the total number of full houses is:
        
        $$|A| = \binom{13}{1} \binom{4}{3} \binom{12}{1} \binom{4}{2} = 13 \times 4 \times 12 \times 6 = 3,744$$
        
- Probability:
    
    $$P(\text{Full House}) = \frac{|A|}{|S|} = \frac{3,744}{2,598,960} \approx 0.00144$$
    

#### Practice Problems and Solutions

**Problem 1**: A jury pool consists of 27 people. How many different ways can 11 people be chosen to serve on a jury and one additional person be chosen to serve as the jury foreman? 7

- **Solution**: This is a two-step counting problem.
    
    - Step 1: Choose the 11 jurors. The order does not matter, so this is a combination.
        
        $$C(27, 11) = \frac{27!}{11!(27-11)!} = 13,037,895$$
        
    - Step 2: Choose the jury foreman. After the jurors are chosen, 16 people remain. We need to choose 1.
        
        $$C(16, 1) = 16$$
        
    - Total Ways: Using the multiplication principle, the total number of ways is:
        
        $$13,037,895 \times 16 = 208,606,320$$
        

**Problem 2**: In how many ways can 20 basketball players be divided into 4 teams of 5? 8

- **Solution**:
    
    - This problem involves partitioning a set into equal-sized subsets.
        
    - Choose 5 players for the first team: $\binom{20}{5}$ ways.
        
    - Choose 5 players for the second team from the remaining 15: $\binom{15}{5}$ ways.
        
    - Choose 5 players for the third team from the remaining 10: $\binom{10}{5}$ ways.
        
    - The last 5 players form the fourth team: $\binom{5}{5}$ ways.
        
    - The product is $\binom{20}{5}\binom{15}{5}\binom{10}{5}\binom{5}{5} = \frac{20!}{(5!)^4}$.
        
    - However, since the teams are not labeled, we have overcounted. There are $4!$ ways to arrange the 4 teams, so we must divide by $4!$.
        
    - Total ways = $\frac{1}{4!} \frac{20!}{(5!)^4}$.
        

**Problem 3**: A jar contains 10 red balls and 20 blue balls. If 5 balls are randomly sampled without replacement, what is the probability of obtaining two red and three blue balls? 8

- **Solution**:
    
    - This is a hypergeometric probability problem, which uses combinations.
        
    - Total number of ways to sample 5 balls from 30: $|S| = \binom{30}{5}$.
        
    - Number of ways to choose 2 red balls from 10: $\binom{10}{2}$.
        
    - Number of ways to choose 3 blue balls from 20: $\binom{20}{3}$.
        
    - The number of favourable outcomes is $|A| = \binom{10}{2} \times \binom{20}{3}$.
        
    - The probability is:
        
        $$P(\text{2 red, 3 blue}) = \frac{\binom{10}{2} \binom{20}{3}}{\binom{30}{5}} = \frac{45 \times 1140}{142506} \approx 0.36$$
        

### 2.3 - Story Proofs and Combinatorial Identities

A "story proof" is an intuitive technique for proving combinatorial identities. Instead of algebraic manipulation, a story proof demonstrates that both sides of an equation are simply two different ways of counting the same quantity.

#### Identity 1: The Committee Argument

$$\binom{n}{k} = \binom{n}{n-k}$$

- **Story Proof**:
    
    - **Story**: We want to form a committee of $k$ people from a group of $n$ people.
        
    - **LHS Counting**: The left-hand side, $\binom{n}{k}$, counts the number of ways to choose the $k$ people who will be **on** the committee.
        
    - **RHS Counting**: The right-hand side, $\binom{n}{n-k}$, counts the number of ways to choose the $n-k$ people who will be **left off** the committee.
        
    - **Conclusion**: Choosing who is on the committee is the exact same decision as choosing who is not. Therefore, both sides are counting the same thing.1
        

#### Identity 2: The President/Captain Argument

$$k\binom{n}{k} = n\binom{n-1}{k-1}$$

- **Story Proof**:
    
    - **Story**: We want to form a committee of $k$ people from a group of $n$ people, and then designate one member as its president.
        
    - **LHS Counting (Committee first, then President)**:
        
        1. Choose the $k$ members of the committee: $\binom{n}{k}$ ways.
            
        2. Choose one of the $k$ members to be president: $k$ ways.
            
        3. Total ways: $k\binom{n}{k}$.
            
    - **RHS Counting (President first, then Committee)**:
        
        1. Choose the president from the $n$ people: $n$ ways.
            
        2. Choose the remaining $k-1$ members from the remaining $n-1$ people: $\binom{n-1}{k-1}$ ways.
            
        3. Total ways: $n\binom{n-1}{k-1}$.
            
    - **Conclusion**: Since both procedures count the same final outcome, the two expressions must be equal.1
        

#### Identity 3: Vandermonde's Identity

$$\binom{m+n}{k} = \sum_{j=0}^{k} \binom{m}{j}\binom{n}{k-j}$$

- **Story Proof**:
    
    - **Story**: We want to form a committee of $k$ people from a group of $m$ men and $n$ women.
        
    - **LHS Counting**: The left-hand side, $\binom{m+n}{k}$, counts the total number of ways to choose the committee directly from the entire group of $m+n$ people.
        
    - **RHS Counting (Partitioning by number of men)**: We can break the problem down into disjoint cases based on the number of men, $j$, on the committee.
        
        - For a committee to have exactly $j$ men, we must choose $j$ men from $m$ ($\binom{m}{j}$ ways) and the remaining $k-j$ women from $n$ ($\binom{n}{k-j}$ ways).
            
        - The number of ways to form a committee with exactly $j$ men is $\binom{m}{j}\binom{n}{k-j}$.
            
        - To get the total, we sum over all possible values of $j$: $\sum_{j=0}^{k} \binom{m}{j}\binom{n}{k-j}$.
            
    - **Conclusion**: The LHS counts the total in one step. The RHS counts the same total by breaking it into non-overlapping subproblems. Therefore, the identity is true.1
        

---

## Part III: Reasoning with Uncertainty - Conditional Probability

### 3.1 - Conditional Probability and Independence

Conditional probability is the probability of an event occurring, given that another event has already occurred. It allows us to update our beliefs in the face of new evidence.9

#### Definition of Conditional Probability

The conditional probability of event $A$ given event $B$ is denoted $P(A|B)$ and is defined as:

$$P(A|B) = \frac{P(A \cap B)}{P(B)}, \quad \text{provided } P(B) > 0$$

9

**Intuition**: Conditioning on event $B$ shrinks our universe of possible outcomes from the entire sample space $S$ to just the set $B$. We then re-normalize the probabilities within this new space by dividing by $P(B)$.1

#### The Chain Rule

By rearranging the definition, we get the Chain Rule for probabilities:

$$P(A \cap B) = P(A|B)P(B) = P(B|A)P(A)$$This extends to multiple events:

$$P(A_1 \cap \dots \cap A_n) = P(A_1)P(A_2|A_1) \dots P(A_n|A_1 \cap \dots \cap A_{n-1})$$

1

#### Independence

Two events $A$ and $B$ are **independent** if the occurrence of one does not provide any information about the other.

Formal Definition: Events $A$ and $B$ are independent if:

$$P(A \cap B) = P(A)P(B)$$If $P(B) > 0$, this is equivalent to stating $P(A|B) = P(A)$.1

#### Example: 2-Card Hand

**Experiment**: Draw a random 2-card hand from a 52-card deck.1

- **Case 1**: Find $P(\text{both aces} | \text{have at least one ace})$.
    
    - Let $A$ be "both aces" and $B$ be "have at least one ace." We want $P(A|B) = \frac{P(A)}{P(B)}$.
        
    - $P(A) = \frac{\binom{4}{2}}{\binom{52}{2}}$.
        
    - $P(B) = 1 - P(\text{no aces}) = 1 - \frac{\binom{48}{2}}{\binom{52}{2}}$.
        
    - $P(A|B) = \frac{\binom{4}{2}}{\binom{52}{2} - \binom{48}{2}} = \frac{6}{1326 - 1128} = \frac{6}{198} = \frac{1}{33}$.
        
- **Case 2**: Find $P(\text{both aces} | \text{have the ace of spades})$.
    
    - Let $A$ be "both aces" and $C$ be "have the ace of spades." We want $P(A|C) = \frac{P(A \cap C)}{P(C)}$.
        
    - $P(A \cap C) = P(\text{AS + another ace}) = \frac{\binom{1}{1}\binom{3}{1}}{\binom{52}{2}} = \frac{3}{1326}$.
        
    - $P(C) = P(\text{AS + any other card}) = \frac{\binom{1}{1}\binom{51}{1}}{\binom{52}{2}} = \frac{51}{1326}$.
        
    - $P(A|C) = \frac{3/1326}{51/1326} = \frac{3}{51} = \frac{1}{17}$.
        

The probability nearly doubles because the information "have the ace of spades" is much more specific than "have at least one ace".1

#### Practice Problems and Solutions

**Problem 1**: A family has 2 children. Given that one of the children is a boy, what is the probability that the other child is also a boy? 10

- **Solution**:
    
    - The sample space is $S = \{BB, BG, GB, GG\}$.
        
    - Let $A$ be the event "both children are boys": $A = \{BB\}$.
        
    - Let $B$ be the event "one of the children is a boy": $B = \{BB, BG, GB\}$.
        
    - We want to find $P(A|B) = \frac{P(A \cap B)}{P(B)}$.
        
    - $P(A \cap B) = P(\{BB\}) = \frac{1}{4}$.
        
    - $P(B) = P(\{BB, BG, GB\}) = \frac{3}{4}$.
        
    - $P(A|B) = \frac{1/4}{3/4} = \frac{1}{3}$.
        

**Problem 2**: In a survey, 60% of people read a Hindi newspaper, 40% read an English newspaper, and 20% read both. If a person is chosen at random and they already read an English newspaper, find the probability that they also read a Hindi newspaper. 11

- **Solution**:
    
    - Let $H$ be the event that a person reads a Hindi newspaper, $P(H) = 0.60$.
        
    - Let $E$ be the event that a person reads an English newspaper, $P(E) = 0.40$.
        
    - We are given $P(H \cap E) = 0.20$.
        
    - We want to find $P(H|E)$.
        
    - Using the formula:
        
        $$P(H|E) = \frac{P(H \cap E)}{P(E)} = \frac{0.20}{0.40} = 0.5$$
        

### 3.2 - The Law of Total Probability

The Law of Total Probability (LTP) is a "divide and conquer" rule for calculating the probability of an event by breaking the problem down into smaller pieces.

#### The Law

Let $A_1, A_2, \dots, A_n$ be a partition of the sample space $S$ (mutually exclusive and exhaustive events). For any event $B$, the Law of Total Probability states:

$$P(B) = \sum_{i=1}^{n} P(B|A_i)P(A_i)$$

**Intuition**: To find the overall probability of $B$, we can take a weighted average of its conditional probabilities across all possible scenarios ($A_i$), where the weight for each scenario is the probability of that scenario occurring, $P(A_i)$.

#### The Foundation for Bayes' Rule

The LTP is the computational engine for Bayes' Rule. It provides the mechanism for calculating the denominator, $P(B)$, which represents the total probability of observing the evidence.

$$P(A_i|B) = \frac{P(B|A_i)P(A_i)}{P(B)} = \frac{P(B|A_i)P(A_i)}{\sum_{j=1}^{n} P(B|A_j)P(A_j)}$$

#### Practice Problems and Solutions

**Problem 1**: A magician places 4 ordinary quarters (Fair) and 1 double-headed quarter (DH) into a box. If you select a coin from the box at random and toss it, what is the probability that it lands heads? 12

- **Solution**:
    
    - Let $H$ be the event of heads. We partition by the type of coin selected: $F$ (fair) and $DH$ (double-headed).
        
    - **Priors**: $P(F) = \frac{4}{5}$, $P(DH) = \frac{1}{5}$.
        
    - **Likelihoods**: $P(H|F) = \frac{1}{2}$, $P(H|DH) = 1$.
        
    - Apply LTP:
        
        $$P(H) = P(H|F)P(F) + P(H|DH)P(DH)$$
        
        $$P(H) = (\frac{1}{2})(\frac{4}{5}) + (1)(\frac{1}{5}) = \frac{4}{10} + \frac{2}{10} = \frac{6}{10} = 0.6$$
        

**Problem 2**: Suppose we discard the top card from a shuffled 52-card deck without looking at it. What is the probability that the second card is a diamond? 12

- **Solution**:
    
    - Let $D_2$ be the event that the second card is a diamond. We partition based on the first card, $D_1$ (diamond) or $D_1^c$ (not a diamond).
        
    - **Priors**: $P(D_1) = \frac{13}{52} = \frac{1}{4}$, $P(D_1^c) = \frac{39}{52} = \frac{3}{4}$.
        
    - **Conditional Probabilities**:
        
        - $P(D_2|D_1)$: If the first was a diamond, 12 diamonds remain in 51 cards. $P(D_2|D_1) = \frac{12}{51}$.
            
        - $P(D_2|D_1^c)$: If the first was not a diamond, 13 diamonds remain in 51 cards. $P(D_2|D_1^c) = \frac{13}{51}$.
            
    - Apply LTP:
        
        $$P(D_2) = P(D_2|D_1)P(D_1) + P(D_2|D_1^c)P(D_1^c)$$
        
        $$P(D_2) = \left(\frac{12}{51}\right)\left(\frac{1}{4}\right) + \left(\frac{13}{51}\right)\left(\frac{3}{4}\right) = \frac{12+39}{204} = \frac{51}{204} = \frac{1}{4}$$
        

### 3.3 - Bayes' Rule and Inferential Thinking

Bayes' Rule is a formula for updating our beliefs about a hypothesis in light of new evidence. It allows us to "invert" conditional probabilities from $P(\text{evidence}|\text{hypothesis})$ to $P(\text{hypothesis}|\text{evidence})$.2

#### The Rule and Its Components

$$P(A|B) = \frac{P(B|A)P(A)}{P(B)}$$

2

- $P(A)$: **Prior Probability**. Our initial belief in hypothesis $A$.
    
- $P(B|A)$: **Likelihood**. The probability of observing evidence $B$, assuming $A$ is true.
    
- $P(B)$: **Marginal Likelihood**. The total probability of observing the evidence $B$.
    
- $P(A|B)$: **Posterior Probability**. Our updated belief in $A$ after observing $B$.
    

#### Example: Medical Diagnosis

- **Scenario**: A disease affects 1% of the population. A test is 95% accurate (95% true positive rate, 5% false positive rate).1
    
- **Question**: If a person tests positive, what is the probability they have the disease?
    
- **Solution**:
    
    - **Events**: $D$: has the disease. $T$: tests positive.
        
    - **Probabilities**:
        
        - **Prior**: $P(D) = 0.01$.
            
        - **Likelihoods**: $P(T|D) = 0.95$, $P(T|D^c) = 0.05$.
            
    - **Goal**: Find the posterior, $P(D|T)$.
        
    - Apply Bayes' Rule:
        
        $$P(D|T) = \frac{P(T|D)P(D)}{P(T)}$$
        
    - Calculate $P(T)$ using LTP:
        
        $$P(T) = P(T|D)P(D) + P(T|D^c)P(D^c) = (0.95)(0.01) + (0.05)(0.99) = 0.059$$
        
    - Calculate Posterior:
        
        $$P(D|T) = \frac{0.0095}{0.059} \approx 0.161$$
        
    - **Conclusion**: Even with a positive test, there is only a 16.1% chance of having the disease. The low prior probability has a massive influence.1
        

#### Practice Problems and Solutions

**Problem 1**: In a factory, three machines A, B, and C produce 25%, 35%, and 40% of the bolts. Of their output, 5%, 4%, and 2% are defective. A bolt is chosen at random and found to be defective. What is the probability it was produced by machine B? 13

- **Solution**:
    
    - **Events**: $B_1, B_2, B_3$: Bolt from machine A, B, C. $E$: Bolt is defective.
        
    - **Priors**: $P(B_1) = 0.25$, $P(B_2) = 0.35$, $P(B_3) = 0.40$.
        
    - **Likelihoods**: $P(E|B_1) = 0.05$, $P(E|B_2) = 0.04$, $P(E|B_3) = 0.02$.
        
    - **Goal**: Find $P(B_2|E)$.
        
    - Apply Bayes' Rule:
        
        $$P(B_2|E) = \frac{P(E|B_2)P(B_2)}{P(E|B_1)P(B_1) + P(E|B_2)P(B_2) + P(E|B_3)P(B_3)}$$
        
        $$P(B_2|E) = \frac{(0.04)(0.35)}{(0.05)(0.25) + (0.04)(0.35) + (0.02)(0.40)} = \frac{0.014}{0.0345} \approx 0.4058$$
        

**Problem 2**: A man is known to speak the truth 3 out of 4 times. He throws a die and reports that it is a six. Find the probability that it is actually a six. 13

- **Solution**:
    
    - **Events**: $E_1$: A six is rolled. $E_2$: A six is not rolled. $E$: The man reports a six.
        
    - **Priors**: $P(E_1) = \frac{1}{6}$, $P(E_2) = \frac{5}{6}$.
        
    - **Likelihoods**: $P(E|E_1) = P(\text{speaks truth}) = \frac{3}{4}$. $P(E|E_2) = P(\text{lies}) = \frac{1}{4}$.
        
    - **Goal**: Find $P(E_1|E)$.
        
    - Apply Bayes' Rule:
        
        $$P(E_1|E) = \frac{P(E|E_1)P(E_1)}{P(E|E_1)P(E_1) + P(E|E_2)P(E_2)}$$
        
        $$P(E_1|E) = \frac{(\frac{3}{4})(\frac{1}{6})}{(\frac{3}{4})(\frac{1}{6}) + (\frac{1}{4})(\frac{5}{6})} = \frac{3/24}{8/24} = \frac{3}{8}$$
        

### 3.4 - Key Applications (Birthday Problem, de Montmort's Problem)

#### The Birthday Problem

**Problem**: In a room of $k$ people, what is the probability that at least two of them share the same birthday?

The result is counter-intuitive: the probability exceeds 50% with just 23 people.1

Solution: The Power of the Complement

It is far easier to calculate the probability of the complement event: no two people share a birthday.

1. **Define Complement**: Let $A^c$ be the event that all $k$ people have different birthdays.
    
2. **Total Outcomes**: The total number of birthday assignments is $|S| = 365^k$.
    
3. **Favorable Outcomes for Complement**: To ensure no matches, we sample without replacement: $|A^c| = 365 \times 364 \times \dots \times (365-k+1)$.
    
4. Calculate Probabilities:
    
    $$P(A^c) = \frac{365 \times 364 \times \dots \times (365-k+1)}{365^k}$$
    
    $$P(A) = 1 - P(A^c)$$
    
    For $k=23$, $P(A) \approx 0.507$.1
    

#### de Montmort's Matching Problem (Derangements)

**Problem**: Suppose you have $n$ cards, numbered 1 to $n$. After shuffling, what is the probability that at least one card is in its "natural" position (card $i$ is in spot $i$)? 1

**Solution: Inclusion-Exclusion and Approximation**

1. **Define Events**: Let $A_i$ be the event that card $i$ is in the $i$-th position. We want to find $P(\bigcup_{i=1}^{n} A_i)$.
    
2. Apply Inclusion-Exclusion:
    
    $$P(\bigcup A_i) = \sum P(A_i) - \sum P(A_i \cap A_j) + \dots$$
    
3. **Calculate Intersection Probabilities**: The total number of permutations is $n!$.
    
    - $P(A_i) = \frac{(n-1)!}{n!} = \frac{1}{n}$.
        
    - $P(A_i \cap A_j) = \frac{(n-2)!}{n!}$.
        
    - The sum of the first group of terms is $\binom{n}{1} \frac{1}{n} = 1$.
        
    - The sum of the second group of terms is $\binom{n}{2} \frac{(n-2)!}{n!} = \frac{1}{2!}$.
        
4. The Resulting Series: The probability of at least one match is:
    
    $$P(\text{at least one match}) = 1 - \frac{1}{2!} + \frac{1}{3!} - \dots + (-1)^{n+1} \frac{1}{n!}$$
    
    This is the truncated Taylor series for $1 - e^{-1}$. For large $n$, this value is approximately $1 - e^{-1} \approx 0.632$.1
    

### 3.5 - Famous Paradoxes (Monty Hall, Simpson's Paradox)

#### The Monty Hall Problem

**Scenario**: You pick one of three doors (one has a car, two have goats). The host, who knows where the car is, opens another door to reveal a goat. He asks if you want to switch to the other unopened door.1

**The Correct Answer**: You should always switch. Switching doubles your probability of winning from $\frac{1}{3}$ to $\frac{2}{3}$.10

**Formal Solution**:

- **Sticking**: You only win if your initial guess was correct. The probability of this is $\frac{1}{3}$.
    
- **Switching**: You win if your initial guess was _incorrect_. The probability of this is $\frac{2}{3}$. If your initial guess was wrong, the host is forced to open the only other goat door, leaving the car behind the door you can switch to. Therefore, switching is the winning strategy with probability $\frac{2}{3}$.1
    

#### Simpson's Paradox

Simpson's Paradox is a phenomenon where a trend that appears in different groups of data reverses when these groups are combined. It is a warning about the dangers of drawing conclusions from aggregated data without understanding potential confounding variables.1

Example: Surgeon Success Rates

Two surgeons, Dr. Hibbert and Dr. Nick, perform easy and hard surgeries 1:

||**Dr. Hibbert**|**Dr. Nick**|
|---|---|---|
|**Hard Surgery**|**77%** Success (70/90)|**50%** Success (5/10)|
|**Easy Surgery**|**100%** Success (10/10)|**90%** Success (81/90)|

Dr. Hibbert is better at both individual surgery types.

Now, let's aggregate the data:

||**Dr. Hibbert**|**Dr. Nick**|
|---|---|---|
|**Overall**|80/100 = **80%**|86/100 = **86%**|

**The Paradox**: Dr. Nick has a better overall success rate.

**Explanation**: The confounding variable is the difficulty of the surgery. Dr. Hibbert, the specialist, took on a much harder caseload (90 hard surgeries vs. 10 for Dr. Nick). His overall average was dragged down by the inherently lower success rate of difficult surgeries, even though he was the better surgeon at both.1

---

## Part IV: Quantifying Randomness - Random Variables

### 4.1 - Introduction to Random Variables

A **random variable** (R.V.) is a function that maps each outcome in the sample space to a real number. It is a numerical summary of an aspect of the experiment.1

**Example: Coin Flips**

- **Experiment**: Flip a coin three times.
    
- **Sample Space**: $S = \{HHH, HHT, \dots, TTT\}$.
    
- **Random Variable**: Let $X$ be "the number of heads".
    
- **Mapping**: $X(HHH) = 3$, $X(HHT) = 2$, $X(TTT) = 0$, etc..1
    

The event "$X=2$" is now a shorthand for the set of outcomes $\{HHT, HTH, THH\}$.

#### Types of Random Variables

1. **Discrete Random Variable**: Can take on a finite or countably infinite number of distinct values (e.g., number of heads, result of a die roll).
    
2. **Continuous Random Variable**: Can take on any value within a given range (e.g., height, temperature).
    

### 4.2 - Probability Mass Function (PMF) for Discrete R.V.s

For a discrete random variable, the **Probability Mass Function (PMF)** gives the probability that the R.V. is exactly equal to some value.1

**Definition**: $p_X(x) = P(X=x)$

A valid PMF must satisfy:

1. $p_X(x) \ge 0$ for all $x$.
    
2. $\sum_{x} p_X(x) = 1$.
    

Example: Sum of Two Dice

Let $Y$ be the sum of two dice. The PMF is:

|**Sum (y)**|**2**|**3**|**4**|**5**|**6**|**7**|**8**|**9**|**10**|**11**|**12**|
|---|---|---|---|---|---|---|---|---|---|---|---|
|$p_Y(y)$|$1/36$|$2/36$|$3/36$|$4/36$|$5/36$|$6/36$|$5/36$|$4/36$|$3/36$|$2/36$|$1/36$|

### 4.3 - Cumulative Distribution Function (CDF)

The **Cumulative Distribution Function (CDF)** is a universal tool for describing the distribution of _any_ random variable.

**Definition**: $F_X(x) = P(X \le x)$ 1

#### Properties of a CDF

1. **Non-decreasing**: If $a < b$, then $F(a) \le F(b)$.
    
2. **Limits**: $\lim_{x \to -\infty} F(x) = 0$ and $\lim_{x \to \infty} F(x) = 1$.
    
3. **Right-Continuous**.
    

For a discrete R.V., the CDF is a step function. For a continuous R.V., the CDF is a continuous function, and its derivative is the PDF: $f(x) = F'(x)$.1

The CDF allows calculation of probabilities over intervals: $P(a < X \le b) = F_X(b) - F_X(a)$.1

### 4.4 - Expectation (The Fundamental Bridge)

The **expectation** (or expected value) of a random variable is its long-run average value, a weighted average of all possible values.1

**Definition**:

- **Discrete**: $E[X] = \sum_{x} x \cdot P(X=x)$
    
- **Continuous**: $E[X] = \int_{-\infty}^{\infty} x \cdot f_X(x) \,dx$
    

#### The Fundamental Bridge

An indicator random variable $I_A$ for an event $A$ is 1 if A occurs and 0 otherwise. Its expectation is:

$$E[I_A] = 1 \cdot P(A) + 0 \cdot P(A^c) = P(A)$$

This result, $E[I_A] = P(A)$, is the Fundamental Bridge, connecting probability and expectation.1

#### Linearity of Expectation

For any two random variables $X$ and $Y$, and any constant $c$:

1. $E = E[X] + E$
    
2. $E[cX] = cE[X]$
    

Crucially, additivity holds **even if $X$ and $Y$ are dependent**. This allows us to solve for the expectation of a complex R.V. by breaking it into a sum of simpler ones.1

Example: Expected Aces in a Poker Hand

What is the expected number of aces in a 5-card hand?

- **Solution using Linearity**:
    
    1. Let $X$ be the total number of aces. Let $X_i$ be the indicator that the $i$-th card is an ace. Then $X = X_1 + X_2 + X_3 + X_4 + X_5$.
        
    2. By linearity, $E[X] = \sum_{i=1}^{5} E[X_i]$.
        
    3. The probability that any single card is an ace is $\frac{4}{52} = \frac{1}{13}$. So, $E[X_i] = \frac{1}{13}$ for all $i$.
        
    4. $E[X] = 5 \times \frac{1}{13} = \frac{5}{13}$.1
        

### 4.5 - Variance and Standard Deviation

**Variance** measures the spread or dispersion of a distribution. It is the expected value of the squared deviation from the mean.1

**Definition**: $Var(X) = E\left[(X - E[X])^2\right]$

**Computational Formula**: $Var(X) = E[X^2] - (E[X])^2$ 1

The Standard Deviation is the square root of the variance, returning the measure of spread to the original units.

Definition: $SD(X) = \sqrt{Var(X)}$ 1

#### Properties of Variance

Let $a, b$ be constants.

1. $Var(aX+b) = a^2 Var(X)$
    
2. If $X$ and $Y$ are **independent**, then $Var(X+Y) = Var(X) + Var(Y)$. Unlike expectation, variance is not always linear.1
    

#### Practice Problem and Solution

**Problem**: A discrete R.V. $X$ has PMF: $P(X=0)=0.2$, $P(X=1)=0.5$, $P(X=2)=0.3$. Find the mean, variance, and standard deviation.

- **Solution**:
    
    - **Mean**: $E[X] = (0)(0.2) + (1)(0.5) + (2)(0.3) = 1.1$.
        
    - **Second Moment**: $E[X^2] = (0^2)(0.2) + (1^2)(0.5) + (2^2)(0.3) = 1.7$.
        
    - **Variance**: $Var(X) = E[X^2] - (E[X])^2 = 1.7 - (1.1)^2 = 0.49$.
        
    - **Standard Deviation**: $SD(X) = \sqrt{0.49} = 0.7$.
        

### 4.6 - Moment Generating Functions (MGFs)

The **Moment Generating Function (MGF)** is a powerful tool used to analyze probability distributions. It simplifies the calculation of moments and the analysis of sums of independent random variables.

**Definition**: $M_X(t) = E[e^{tX}]$ 

#### Key Properties of MGFs

1. Generating Moments: The $n$-th moment can be found by taking the $n$-th derivative of the MGF and evaluating at $t=0$.
    
    $$E[X^n] = M_X^{(n)}(0)$$
    
2. **Uniqueness**: If two random variables have the same MGF, they have the same distribution.14
    
3. Sums of Independent R.V.s: If $X$ and $Y$ are independent, the MGF of their sum is the product of their MGFs.
    
    $$M_{X+Y}(t) = M_X(t) M_Y(t)$$
    
    
    

#### Example: Sum of Poissons is Poisson

**Problem**: Let $X \sim Pois(\lambda)$ and $Y \sim Pois(\mu)$ be independent. Show that $Z = X+Y \sim Pois(\lambda+\mu)$.

- **Solution**:
    
    1. The MGF of a Poisson($\lambda$) R.V. is $M_X(t) = e^{\lambda(e^t - 1)}$.1
        
    2. Using the sum property:
        
        $$M_Z(t) = M_X(t)M_Y(t) = e^{\lambda(e^t - 1)} \cdot e^{\mu(e^t - 1)} = e^{(\lambda+\mu)(e^t - 1)}$$
        
    3. We recognize this as the MGF of a Poisson R.V. with parameter $\lambda+\mu$. By the uniqueness property, the proof is complete.1
        

#### Practice Problem and Solution

**Problem**: Suppose the MGF for $X$ is $M(t) = \frac{e^t}{3 - 2e^t}$. Determine the mean and variance of $X$. 15

- **Solution**:
    
    - Rewrite the MGF: $M(t) = \frac{\frac{1}{3}e^t}{1 - \frac{2}{3}e^t}$.
        
    - This is the MGF of a Geometric distribution counting trials until the first success, with success probability $p=\frac{1}{3}$.
        
    - The known formulas for the mean and variance of this Geometric($p$) R.V. are:
        
        - Mean: $\mu = \frac{1}{p} = \frac{1}{1/3} = 3$.
            
        - Variance: $\sigma^2 = \frac{1-p}{p^2} = \frac{2/3}{(1/3)^2} = 6$.
            

---

## Part V: Common Scenarios - Named Distributions

### Discrete Distributions

#### 5.1 - Bernoulli Distribution

The Bernoulli distribution models a single trial with exactly two outcomes: "success" (1) and "failure" (0).16 It is the building block for the Binomial distribution.

- **Story**: A single coin flip, a single pass/fail test.
    
- **PMF**: $P(X=1) = p$, $P(X=0) = 1-p$.
    
- **Mean**: $E[X] = p$
    
- **Variance**: $Var(X) = p(1-p)$
    

#### 5.2 - Binomial Distribution

The Binomial distribution models the number of successes in a fixed number, $n$, of independent Bernoulli trials.19

- **Story**: The number of heads in 10 coin flips; the number of defective items in a sample of 20 (with replacement).
    
- **PMF**: $P(X=k) = \binom{n}{k} p^k (1-p)^{n-k}$ for $k \in \{0, 1, \dots, n\}$
    
- **Mean**: $E[X] = np$.
    
- **Variance**: $Var(X) = np(1-p)$.
    

**Practice Problem**: A basketball player takes 4 independent free throws with a probability of 0.7 of success on each shot. What is the probability of exactly 3 successes? 19

- Solution: This is a binomial experiment with $n=4, p=0.7$.
    
    $$P(X=3) = \binom{4}{3} (0.7)^3 (0.3)^1 = 4 \cdot (0.343) \cdot (0.3) = 0.4116$$
    

#### 5.3 - Geometric and Negative Binomial Distributions

These distributions model the waiting time for successes in a series of Bernoulli trials.

Geometric Distribution

Models the number of trials required to achieve the first success.1

- **Story**: Flipping a coin until the first head appears.
    
- **PMF** (for $Y$ = number of failures _before_ 1st success): $P(Y=k) = (1-p)^k p$ for $k \in \{0, 1, \dots\}$.
    
- **Mean**: $E = \frac{1-p}{p}$.
    
- **Variance**: $Var(Y) = \frac{1-p}{p^2}$.
    
- **Memoryless Property**: The Geometric is the only discrete memoryless distribution. $P(X > s+t | X > s) = P(X > t)$.
    

Negative Binomial Distribution

Generalizes the Geometric to model the number of failures before the r-th success.1

- **Story**: Testing components until the 5th defective one is found.
    
- **PMF** (for $X$ = number of failures before $r$-th success): $P(X=n) = \binom{n+r-1}{r-1} p^r (1-p)^n$.
    
- **Mean**: $E[X] = \frac{r(1-p)}{p}$
    
- **Variance**: $Var(X) = \frac{r(1-p)}{p^2}$
    

**Practice Problem (Geometric)**: A basketball player makes a free throw with probability 0.60. What is the probability that the player's first successful shot is on their third attempt? 26

- Solution: This means 2 failures followed by 1 success.
    
    $P(X=3) = (1-0.60)^{3-1}(0.60) = (0.40)^2(0.60) = 0.096$.
    

#### 5.4 - Hypergeometric Distribution

The Hypergeometric distribution models the number of successes in a sample of size $n$ drawn **without replacement** from a finite population of size $N$ containing $M$ successes.1

- **Story**: Drawing a hand of cards from a deck; quality control sampling from a batch of parts.
    
- **PMF**: $P(X=k) = \frac{\binom{M}{k}\binom{N-M}{n-k}}{\binom{N}{n}}$.
    
- **Mean**: $E[X] = n \frac{M}{N}$
    

**Practice Problem**: A lot of 100 fuses contains 20 defective fuses. 5 fuses are chosen at random for inspection. What is the probability that all 5 are accepted (i.e., non-defective)? 

- **Solution**: We want the probability of choosing 5 non-defective fuses from the 80 available, and 0 defective fuses from the 20 available.
    
    - $N=100$, $M=80$ (success = non-defective), $n=5$, $k=5$.
        
    - $P(X=5) = \frac{\binom{80}{5}\binom{20}{0}}{\binom{100}{5}} \approx 0.32$.
        

#### 5.5 - Poisson Distribution

The Poisson distribution models the number of events occurring in a fixed interval of time or space, given a constant average rate and independence of events.

- **Story**: Number of emails arriving in an hour; number of earthquakes in a year.
    
- **PMF**: $P(X=k) = \frac{e^{-\lambda}\lambda^k}{k!}$ for $k \in \{0, 1, \dots\}$, where $\lambda$ is the average rate.
    
- **Mean**: $E[X] = \lambda$
    
- **Variance**: $Var(X) = \lambda$
    
- **Poisson Approximation to Binomial**: If $n$ is large and $p$ is small, a $Bin(n,p)$ distribution can be approximated by a $Pois(\lambda=np)$ distribution.1
    

**Practice Problem**: Traffic accidents at an intersection follow a Poisson distribution with an average rate of 1.4 per week. What is the probability of exactly 3 accidents next week? 

- Solution: Here, $\lambda = 1.4$ and we want $P(X=3)$.
    
    $$P(X=3) = \frac{e^{-1.4}(1.4)^3}{3!} \approx 0.1128$$
    

### Continuous Distributions

#### 5.6 - Uniform Distribution

A continuous random variable that can take any value within a given interval $[a, b]$, with all values being equally likely.34

- **Story**: A random number generator producing a value between 0 and 1.
    
- **PDF**: $f(x) = \frac{1}{b-a}$ for $x \in [a, b]$, and 0 otherwise.
    
- **Mean**: $E[X] = \frac{a+b}{2}$.
    
- **Variance**: $Var(X) = \frac{(b-a)^2}{12}$.
    

**Practice Problem**: The waiting time at a bus stop is uniformly distributed between 1 and 12 minutes. What is the probability that a rider waits 8 minutes or less? 37

- **Solution**: We want $P(X \le 8)$.
    
    - The PDF is $f(x) = \frac{1}{12-1} = \frac{1}{11}$ for $x \in [1, 2]$.
        
    - $P(X \le 8) = \int_{1}^{8} \frac{1}{11} dx = \frac{1}{11} [x]_1^8 = \frac{8-1}{11} = \frac{7}{11} \approx 0.6364$.
        

#### 5.7 - Exponential Distribution

The Exponential distribution models the waiting time between events in a Poisson process. It is the continuous analogue of the Geometric distribution and is memoryless.1

- **Story**: Time until the next phone call arrives; lifetime of an electronic component.
    
- **PDF**: $f(x) = \lambda e^{-\lambda x}$ for $x \ge 0$
    
- **Mean**: $E[X] = \frac{1}{\lambda}$
    
- **Variance**: $Var(X) = \frac{1}{\lambda^2}$
    
- **Memoryless Property**: $P(X > s+t | X > s) = P(X > t)$. The past waiting time does not affect the future waiting time distribution.1
    

**Practice Problem**: The number of miles a car can run before its battery wears out is exponentially distributed with an average of 10,000 miles. The owner needs to take a 5000-mile trip. What is the probability they can complete the trip? 39

- **Solution**: Due to the memoryless property, it doesn't matter how many miles are already on the battery.
    
    - The mean is $\mu = \frac{1}{\lambda} = 10000$.
        
    - We want $P(X > 5000)$. The survival function is $P(X > k) = e^{-\lambda k} = e^{-k/\mu}$.
        
    - $P(X > 5000) = e^{-5000/10000} = e^{-0.5} \approx 0.6065$.
        

#### 5.8 - Normal Distribution

The Normal (or Gaussian) distribution is a symmetric, bell-shaped curve that is ubiquitous in statistics, largely due to the Central Limit Theorem, which states that the sum of many independent random variables will tend to be normally distributed.1

- **PDF** (for Standard Normal $Z \sim N(0,1)$): $f(z) = \frac{1}{\sqrt{2\pi}} e^{-z^2/2}$
    
- A general Normal R.V. $X \sim N(\mu, \sigma^2)$ can be standardized: $Z = \frac{X-\mu}{\sigma}$.
    
- **Mean**: $E[X] = \mu$
    
- **Variance**: $Var(X) = \sigma^2$
    

**Practice Problem**: The annual salaries of teachers are normally distributed with a mean of $51,000 and a standard deviation of $6,000. Find the probability that a randomly selected teacher's salary is between $42,000 and $65,000. 40

- **Solution**: We need to convert the $X$ values to Z-scores.
    
    - For $x = 42000$, $z = \frac{42000 - 51000}{6000} = -1.5$.
        
    - For $x = 65000$, $z = \frac{65000 - 51000}{6000} \approx 2.33$.
        
    - We need to find $P(-1.5 < Z < 2.33)$. Using a standard normal table or calculator:
        
        $$P(-1.5 < Z < 2.33) = P(Z < 2.33) - P(Z < -1.5) \approx 0.9901 - 0.0668 = 0.9233$$
        

---

## Part VI: Multiple Dimensions - Joint Distributions

### 6.1 - Joint, Marginal, and Conditional Distributions

When dealing with multiple random variables, we use joint distributions to describe their behavior together.

- **Joint PMF/PDF**: Describes the probability of two or more R.V.s taking on specific values or falling in a specific region. For discrete R.V.s, $p_{X,Y}(x,y) = P(X=x, Y=y)$. For continuous R.V.s, $P((X,Y) \in A) = \iint_A f_{X,Y}(x,y) dx dy$.
    
- **Marginal PMF/PDF**: The distribution of a single variable, obtained by summing or integrating the joint distribution over all possible values of the other variable(s).
    
    - Discrete: $p_X(x) = \sum_y p_{X,Y}(x,y)$
        
    - Continuous: $f_X(x) = \int_{-\infty}^{\infty} f_{X,Y}(x,y) dy$
        
- **Independence**: Two R.V.s $X$ and $Y$ are independent if their joint distribution is the product of their marginal distributions: $p_{X,Y}(x,y) = p_X(x)p_Y(y)$ or $f_{X,Y}(x,y) = f_X(x)f_Y(y)$
    
- Conditional PMF/PDF: The distribution of one variable given that another has taken a specific value.
    
    $$f_{Y|X}(y|x) = \frac{f_{X,Y}(x,y)}{f_X(x)}$$
    

**Practice Problem**: Given the joint PMF in the table, find the marginal PMF of X and determine if X and Y are independent.

||**Y=0**|**Y=1**|
|---|---|---|
|**X=0**|1/2|0|
|**X=1**|1/4|1/4|

- **Solution**:
    
    - **Marginal PMF of X**: Sum across the rows.
        
        - $P(X=0) = P(X=0, Y=0) + P(X=0, Y=1) = 1/2 + 0 = 1/2$.
            
        - $P(X=1) = P(X=1, Y=0) + P(X=1, Y=1) = 1/4 + 1/4 = 1/2$.
            
    - **Marginal PMF of Y**: Sum down the columns.
        
        - $P(Y=0) = 1/2 + 1/4 = 3/4$.
            
        - $P(Y=1) = 0 + 1/4 = 1/4$.
            
    - **Independence Check**: We check if $P(X=x, Y=y) = P(X=x)P(Y=y)$ for all pairs.
        
        - Consider $(X=0, Y=0)$: $P(X=0, Y=0) = 1/2$.
            
        - $P(X=0)P(Y=0) = (1/2)(3/4) = 3/8$.
            
        - Since $1/2 \neq 3/8$, the random variables X and Y are **dependent**.
            

### 6.2 - Multinomial Distribution

The Multinomial distribution is a generalization of the Binomial distribution for experiments with more than two possible outcomes.

- **Story**: An experiment with $n$ independent trials, where each trial can result in one of $k$ distinct outcomes with probabilities $p_1, p_2, \dots, p_k$ such that $\sum p_i = 1$.
    
- Joint PMF: The probability of observing $n_1$ outcomes of type 1, $n_2$ of type 2,..., and $n_k$ of type k (where $\sum n_i = n$) is:
    
    $$P(X_1=n_1, \dots, X_k=n_k) = \frac{n!}{n_1! n_2! \dots n_k!} p_1^{n_1} p_2^{n_2} \dots p_k^{n_k}$$
    
- **Marginals**: Each individual count $X_i$ follows a Binomial distribution, $X_i \sim Bin(n, p_i)$
    


- **Solution**:
    
    - $n=4$ trials. The outcomes are Red, Green, Blue.
        
    - Probabilities: $p_R = 0.2$, $p_G = 0.3$, $p_B = 0.5$.
        
    - Desired counts: $n_R=0$, $n_G=2$, $n_B=2$.
        
    - Using the PMF:
        
        $$P(n_R=0, n_G=2, n_B=2) = \frac{4!}{0! 2! 2!} (0.2)^0 (0.3)^2 (0.5)^2$$
        
        $$= 6 \cdot 1 \cdot 0.09 \cdot 0.25 = 0.135$$
        

---

## Appendix

### Gambler's Ruin Problem

Two gamblers, A and B, start with $i$ and $N-i$ dollars, respectively. They play a series of rounds, betting $1 on each. In each round, A wins with probability $p$ and B wins with probability $q=1-p$. The game ends when one player is bankrupt. What is the probability that A wins the entire game? 

This is a classic 1D random walk problem with absorbing barriers at 0 and N.

- Recurrence Relation: Let $p_i$ be the probability that A wins starting with $i$ dollars. By conditioning on the first step, we get:
    
    $$p_i = p \cdot p_{i+1} + q \cdot p_{i-1}$$
    
    with boundary conditions $p_0 = 0$ and $p_N = 1$.
    
- **Solution**:
    
    - If $p \neq q$ (biased coin), the solution is:
        
        $$p_i = \frac{1 - (q/p)^i}{1 - (q/p)^N}$$
        
    - If $p = q = 1/2$ (fair coin), the solution simplifies to:
        
        $$p_i = \frac{i}{N}$$
        
        This shows that with a fair coin, your initial stake proportion is your probability of winning.
        

### St. Petersburg Paradox

This paradox highlights a situation where the expected value of a game is infinite, yet most people would only be willing to pay a small finite amount to play it.\

- **The Game**: A fair coin is flipped until it lands on heads. If this takes $k$ flips, the player receives a payout of $2^k$ dollars.
    
- **The Paradox**: What is the expected payout of this game?
    
    - The probability of the game ending in $k$ flips (k-1 tails, then 1 head) is $(\frac{1}{2})^k$.
        
    - The expected payout is the sum of (payout $\times$ probability) over all possible outcomes:
        
        $$E[\text{Payout}] = \sum_{k=1}^{\infty} 2^k \cdot \left(\frac{1}{2}\right)^k = \sum_{k=1}^{\infty} 1 = 1+1+1+\dots = \infty$$
        
        The infinite expected value suggests one should be willing to pay any amount to play, which contradicts rational behavior.