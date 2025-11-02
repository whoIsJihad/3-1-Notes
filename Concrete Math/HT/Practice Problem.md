
---

# Probability Theory: Problem Set

## Part 1: Foundations of Probability

### 1.1 - Sample Space, Outcomes, and Events

**Problem:** An experiment consists of rolling two standard six-sided dice and recording the pair of numbers. Define the sample space. Then, define the event E = "the sum of the dice is 6".

**Solution:**

- Sample Space (S): The sample space consists of 36 ordered pairs:
    
    S = {(1,1), (1,2),..., (1,6), (2,1),..., (6,6)}.
    
- Event E: The event where the sum is 6 is the subset of outcomes:
    
    E = {(1,5), (2,4), (3,3), (4,2), (5,1)}.
    

### 1.2 - Naive Definition of Probability

**Problem:** A card is drawn from a standard 52-card deck. What is the probability that the card is a King?

**Solution:**

- **Sample Space (S)**: The set of all 52 cards. `|S| = 52`.
    
- **Event A**: "The card is a King." There are 4 Kings in the deck. `|A| = 4`.
    
- Using the naive definition:
    
    P(A) = |A| / |S| = 4 / 52 = 1 / 13.
    

### 1.3 - Axiomatic Definition of Probability

**Problem:** In a presidential election, candidates A and B have a 20% and 40% chance of winning, respectively. What is the probability that either A or B wins the election? (Assume only one candidate can win).

**Solution:**

- Let `W_A` be the event that A wins, and `W_B` be the event that B wins.
    
- We are given `P(W_A) = 0.20` and `P(W_B) = 0.40`.
    
- Since the events are disjoint (only one can win), we can use Axiom 3:
    
    P(W_A ∪ W_B) = P(W_A) + P(W_B) = 0.20 + 0.40 = 0.60.
    
- There is a 60% chance that either A or B will win.
    

### 1.4 - Properties of Probability

**Problem:** In a group of students, the probability that a student is taking a computer science course is 0.6. The probability that a student is taking a math course is 0.5. The probability that a student is taking both is 0.2. What is the probability that a randomly selected student is taking either a computer science course or a math course?

**Solution:**

- Let `C` be the event that a student is taking a computer science course. `P(C) = 0.6`.
    
- Let `M` be the event that a student is taking a math course. `P(M) = 0.5`.
    
- The event that a student is taking both is the intersection, `C ∩ M`. `P(C ∩ M) = 0.2`.
    
- We want to find the probability of the union, `P(C ∪ M)`.
    
- Using the Inclusion-Exclusion Principle:
    
    P(C ∪ M) = P(C) + P(M) - P(C ∩ M)
    
    P(C ∪ M) = 0.6 + 0.5 - 0.2 = 0.9.
    
- The probability that a student is taking at least one of the two courses is 0.9.
    

---

## Part 2: Counting and Combinatorics

### 2.1 - The Multiplication Rule

**Problem:** A standard license plate consists of 3 letters followed by 3 digits. How many different license plates can be made?

**Solution:**

- There are 6 positions (stages) to fill.
    
- For each of the first 3 positions, there are 26 choices (letters).
    
- For each of the last 3 positions, there are 10 choices (digits 0-9).
    
- Total license plates = `26 × 26 × 26 × 10 × 10 × 10 = 17,576,000`.
    

### 2.2 - Permutations and Combinations

**Problem:** A club has 23 members. How many ways can they pick a president and a vice-president? How many ways can they pick a 2-person committee?

**Solution:**

- President and VP: Order matters (President A, VP B is different from President B, VP A). This is a permutation.
    
    P(23, 2) = 23! / (23-2)! = 23 × 22 = 506 ways.
    
- 2-Person Committee: Order does not matter. This is a combination.
    
    C(23, 2) = 23! / (2! × 21!) = (23 × 22) / 2 = 253 ways.
    

### 2.3 - Sampling Tables (Stars and Bars)

**Problem:** You are buying three donuts from a shop that sells 5 types of donuts. How many different selections are possible?

**Solution:**

- We are choosing `k=3` donuts from `n=5` types.
    
- The order in which you choose the donuts does not matter.
    
- You can choose the same type more than once (replacement is allowed).
    
- This is the "Unordered, With Replacement" case (Stars and Bars).
    
- Number of ways = `(n+k-1 choose k) = (5+3-1 choose 3) = (7 choose 3) = 35`.
    

### 2.4 - Story Proofs and Combinatorial Identities

**Problem:** Give a story proof for Pascal's Identity: `(n choose k) + (n choose k-1) = (n+1 choose k)`.

Solution:

Story: Imagine a group of n+1 people, with one person pre-designated as "the president." We want to form a committee of k people.

- **RHS Argument**: The number of ways to choose a `k`-person committee from `n+1` people is, by definition, `(n+1 choose k)`.
    
- **LHS Argument**: We can count this in two disjoint cases:
    
    1. **The president is on the committee**: We must choose the remaining `k-1` members from the other `n` people. There are `(n choose k-1)` ways.
        
    2. **The president is NOT on the committee**: We must choose all `k` members from the other `n` people. There are `(n choose k)` ways.
        
- The total number of ways is the sum of these two cases: `(n choose k) + (n choose k-1)`.
    

Since both sides count the same thing, the identity is proven.

### 2.5 - Vandermonde's Identity

**Problem:** Prove the identity `(2n choose n) = Σ (from r=0 to n) [ (n choose r)² ]` using a story proof.

Solution:

This is a special case of Vandermonde's Identity where m=n and k=n.

Story:

Imagine a group of 2n people, consisting of n men and n women. We want to form a committee of n people.

- **LHS Argument**: The total number of ways to choose `n` people from `2n` is `(2n choose n)`.
    
- **RHS Argument**: Let's count by considering the number of men on the committee. If we choose `r` men, we must choose `n-r` women.
    
    - The number of ways to choose `r` men from `n` is `(n choose r)`.
        
    - The number of ways to choose `n-r` women from `n` is `(n choose n-r)`.
        
    - By the symmetry identity, `(n choose n-r) = (n choose r)`.
        
    - So, the number of ways to form a committee with `r` men is `(n choose r) × (n choose r) = (n choose r)²`.
        
    - Summing over all possible values of `r` (from 0 to `n`) gives the total number of ways: `Σ (from r=0 to n) [ (n choose r)² ]`.
        

Since both sides count the same thing, the identity holds.

---

## Part 3: Conditional Probability and Independence

### 3.1 - Conditional Probability

**Problem:** A family has two children. Given that at least one of the children is a boy, what is the probability that both children are boys? 1

**Solution:**

- **Sample Space (S)**: `{BB, BG, GB, GG}`.
    
- **Event A**: "Both children are boys." `A = {BB}`. `P(A) = 1/4`.
    
- **Event B**: "At least one child is a boy." `B = {BB, BG, GB}`. `P(B) = 3/4`.
    
- **Intersection (A ∩ B)**: `{BB}`. `P(A ∩ B) = 1/4`.
    
- `P(A|B) = P(A ∩ B) / P(B) = (1/4) / (3/4) = 1/3`.
    

### 3.2 - The Law of Total Probability

**Problem:** An automobile manufacturer has three factories: A, B, and C. They produce 50%, 30%, and 20% of a specific car model, respectively. 30% of cars from factory A are white, 40% from B are white, and 25% from C are white. If a car is selected at random, what is the probability that it is white? 2

**Solution:**

- Let `W` be the event "car is white". Let `A`, `B`, `C` be the events "car from factory A, B, C".
    
- `P(A)=0.50`, `P(B)=0.30`, `P(C)=0.20`.
    
- `P(W|A)=0.30`, `P(W|B)=0.40`, `P(W|C)=0.25`.
    
- Using the Law of Total Probability:
    
    P(W) = P(W|A)P(A) + P(W|B)P(B) + P(W|C)P(C)
    
    P(W) = (0.30)(0.50) + (0.40)(0.30) + (0.25)(0.20)
    
    P(W) = 0.15 + 0.12 + 0.05 = 0.32.
    
- The probability of selecting a white car is 32%.
    

### 3.3 - Bayes' Rule

**Problem:** A factory produces bolts using three machines: A, B, and C. Machine A produces 25% of the bolts, B produces 35%, and C produces 40%. The defect rates for each machine are 5%, 4%, and 2%, respectively. A bolt is chosen at random and found to be defective. What is the probability that it came from machine A? 3

**Solution:**

- Let `D` be the event "bolt is defective."
    
- Let `A`, `B`, `C` be the events "bolt is from machine A, B, C."
    
- We want to find `P(A|D)`.
    
- **Given Probabilities**:
    
    - `P(A)=0.25`, `P(B)=0.35`, `P(C)=0.40`.
        
    - `P(D|A)=0.05`, `P(D|B)=0.04`, `P(D|C)=0.02`.
        
- Find P(D) using Law of Total Probability:
    
    P(D) = P(D|A)P(A) + P(D|B)P(B) + P(D|C)P(C)
    
    = (0.05)(0.25) + (0.04)(0.35) + (0.02)(0.40) = 0.0345.
    
- Apply Bayes' Rule:
    
    P(A|D) = (P(D|A) × P(A)) / P(D)
    
    = (0.05 × 0.25) / 0.0345 = 0.0125 / 0.0345 ≈ 0.362.
    
- The probability that the defective bolt came from machine A is approximately 36.2%.
    

### 3.4 - Independence of Events

**Problem:** A fair coin is tossed twice. Let A be the event "first toss is heads" and B be the event "second toss is heads". Are A and B independent?

**Solution:**

- `P(A) = P({HH, HT}) = 1/2`.
    
- `P(B) = P({HH, TH}) = 1/2`.
    
- `A ∩ B` is the event "both tosses are heads", which is `{HH}`. `P(A ∩ B) = 1/4`.
    
- Check the condition: `P(A) × P(B) = (1/2) × (1/2) = 1/4`.
    
- Since `P(A ∩ B) = P(A) × P(B)`, the events are independent.
    

### 3.5 - Principle of Inclusion-Exclusion

**Problem:** Pick an integer from 1 to 1000 at random. What is the probability that it is divisible by 12 or 15?

**Solution:**

- Let `A₁₂` be the event "divisible by 12" and `A₁₅` be the event "divisible by 15". We want `P(A₁₂ ∪ A₁₅)`.
    
- The number of integers divisible by `r` is `floor(1000/r)`.
    
- `P(A₁₂) = floor(1000/12) / 1000 = 83 / 1000`.
    
- `P(A₁₅) = floor(1000/15) / 1000 = 66 / 1000`.
    
- The intersection `A₁₂ ∩ A₁₅` is the event "divisible by both 12 and 15", which means divisible by their least common multiple, `lcm(12, 15) = 60`.
    
- `P(A₁₂ ∩ A₁₅) = P(A₆₀) = floor(1000/60) / 1000 = 16 / 1000`.
    
- Using Inclusion-Exclusion:
    
    P(A₁₂ ∪ A₁₅) = P(A₁₂) + P(A₁₅) - P(A₁₂ ∩ A₁₅)
    
    = 83/1000 + 66/1000 - 16/1000 = 133/1000 = 0.133.
    

---

## Part 5: Random Variables

### 5.2 - Probability Mass Function (PMF)

**Problem:** Find the probability distribution of the random variable describing the number of heads that turn up when a coin is flipped twice.

**Solution:**

- Let X be the number of heads. The possible values are 0, 1, and 2.
    
- `P(X = 0) = P(TT) = 1/4`
    
- `P(X = 1) = P(TH) + P(HT) = 1/2`
    
- `P(X = 2) = P(HH) = 1/4`
    
- The PMF can be represented in a table:
    

|**x**|**P(X = x)**|
|---|---|
|0|1/4|
|1|1/2|
|2|1/4|

### 5.3 - Cumulative Distribution Function (CDF)

**Problem:** Let X be a discrete random variable with the pmf `f(x) = (5-x)/10` for `x = 1, 2, 3, 4`. Find the CDF of X.

Solution:

The CDF is F(t) = P(X ≤ t).

- For `t < 1`, `F(t) = 0`.
    
- For `1 ≤ t < 2`, `F(t) = P(X=1) = (5-1)/10 = 4/10`.
    
- For `2 ≤ t < 3`, `F(t) = P(X=1) + P(X=2) = 4/10 + (5-2)/10 = 7/10`.
    
- For `3 ≤ t < 4`, `F(t) = P(X≤2) + P(X=3) = 7/10 + (5-3)/10 = 9/10`.
    
- For `t ≥ 4`, `F(t) = P(X≤3) + P(X=4) = 9/10 + (5-4)/10 = 1`.
    

### 5.4 - Expectation (Expected Value)

**Problem:** By investing in a particular stock, a person can make a profit in one year of $4000 with probability 0.3 or take a loss of $1000 with probability 0.7. What is this person's expected gain? 4

**Solution:**

- Let X be the gain. The possible values are `x₁ = 4000` and `x₂ = -1000`.
    
- The probabilities are `P(X=x₁) = 0.3` and `P(X=x₂) = 0.7`.
    
- The expected value is `E(X) = Σ [x × P(X=x)]`.
    
- `E(X) = (4000)(0.3) + (-1000)(0.7) = 1200 - 700 = $500`.
    
- The person's expected gain is $500.
    

### 5.5 - Variance and Standard Deviation

**Problem:** Find the variance and standard deviation of the following scores on an exam: 92, 95, 85, 80, 75, 50.

**Solution:**

1. Find the mean (μ):
    
    μ = (92+95+85+80+75+50) / 6 = 477 / 6 = 79.5.
    
2. **Find the squared deviations from the mean**:
    
    - (92 - 79.5)² = 12.5² = 156.25
        
    - (95 - 79.5)² = 15.5² = 240.25
        
    - (85 - 79.5)² = 5.5² = 30.25
        
    - (80 - 79.5)² = 0.5² = 0.25
        
    - (75 - 79.5)² = (-4.5)² = 20.25
        
    - (50 - 79.5)² = (-29.5)² = 870.25
        
3. Sum the squared deviations:
    
    Sum = 156.25 + 240.25 + 30.25 + 0.25 + 20.25 + 870.25 = 1317.5.
    
4. Calculate the variance (σ²) by dividing by n-1:
    
    σ² = 1317.5 / (6-1) = 1317.5 / 5 = 263.5.
    
5. Calculate the standard deviation (σ):
    
    σ = √263.5 ≈ 16.23.
    

### 5.7 - Indicator Random Variables

**Problem:** `n` men check their hats at a party. The hats are shuffled, and each man receives one back at random. What is the expected number of men who get their own hat back?

**Solution:**

- Let `X` be the total number of men who get their own hat back. We want to find `E(X)`.
    
- Define n indicator random variables, Xᵢ, for each man i:
    
    Xᵢ = 1 if man i gets his own hat back.
    
    Xᵢ = 0 otherwise.
    
- The total number of matches `X` is the sum: `X = X₁ + X₂ +... + Xₙ`.
    
- By Linearity of Expectation, `E(X) = E(X₁) + E(X₂) +... + E(Xₙ)`.
    
- The expectation of each indicator is the probability of the event: `E(Xᵢ) = P(man i gets his own hat)`.
    
- Since all `n` hats are distributed randomly, `P(man i gets his own hat) = 1/n`.
    
- So, `E(Xᵢ) = 1/n` for all `i`.
    
- Substitute this back into the sum:
    
    E(X) = (1/n) + (1/n) +... + (1/n) (n times)
    
    = n × (1/n) = 1.
    
- The expected number of men who get their own hat back is 1.
    

### 5.8 - Moment Generating Functions (MGF)

**Problem:** Suppose that the Moment generating function for X is `M(t) = ( (1 + 2eᵗ)/3 ) × ( (1 + 3eᵗ)/4 )`. What is the probability P(X = 1)? 5

**Solution:**

- The MGF is defined as `M(t) = E[eᵗˣ] = Σ eᵗˣ P(X=x)`.
    
- We can expand the product for M(t):
    
    M(t) = (1/12) × (1 + 2eᵗ)(1 + 3eᵗ)
    
    M(t) = (1/12) × (1 + 3eᵗ + 2eᵗ + 6e²ᵗ)
    
    M(t) = (1/12) + (5/12)eᵗ + (6/12)e²ᵗ
    
    M(t) = (1/12)e⁰ᵗ + (5/12)e¹ᵗ + (1/2)e²ᵗ.
    
- By comparing this to the definition `Σ eᵗˣ P(X=x)`, we can see the coefficients of the `eᵗˣ` terms correspond to the probabilities `P(X=x)`.
    
- The coefficient of `e¹ᵗ` is `P(X=1)`.
    
- Therefore, `P(X=1) = 5/12`.
    

---

## Part 6: Discrete Distributions

### 6.1 - Bernoulli Distribution

**Problem:** 20% of a population has a particular disease. Let X=1 if a person has the disease and X=0 otherwise. Find the mean and standard deviation of X.

**Solution:**

- This is a Bernoulli trial with `p = 0.20`.
    
- **Mean**: `E(X) = p = 0.20`.
    
- **Variance**: `Var(X) = p(1-p) = 0.20(0.80) = 0.16`.
    
- **Standard Deviation**: `SD(X) = √0.16 = 0.4`.
    

### 6.2 - Binomial Distribution

**Problem:** A fair coin is tossed 6 times. What is the probability of getting at least 5 heads? 6

**Solution:**

- This is a binomial distribution with `n=6` and `p=0.5`.
    
- "At least 5 heads" means `P(X=5) + P(X=6)`.
    
- `P(X=5) = (6 choose 5) × (0.5)⁵ × (0.5)¹ = 6 × (0.5)⁶`.
    
- `P(X=6) = (6 choose 6) × (0.5)⁶ × (0.5)⁰ = 1 × (0.5)⁶`.
    
- `P(X ≥ 5) = 6 × (0.5)⁶ + 1 × (0.5)⁶ = 7 × (0.5)⁶ = 7 / 64 ≈ 0.109`.
    

### 6.3 - Geometric Distribution

**Problem:** An oil company has a 20% chance of striking oil on any given exploratory well. What is the probability that the first strike comes on the third well drilled?

**Solution:**

- This is a geometric distribution with `p = 0.20`. We want `P(X=3)`.
    
- This means 2 failures followed by 1 success.
    
- `P(X=3) = (1-0.2)² × (0.2) = (0.8)² × 0.2 = 0.64 × 0.2 = 0.128`.
    

### 6.4 - Negative Binomial Distribution

**Problem:** Using the oil well scenario (20% success rate), what is the probability that the third strike comes on the seventh well drilled?

**Solution:**

- This is a negative binomial distribution with `r=3` successes and `p=0.20`. We want `P(X=7)`.
    
- This means that in the first `k-1=6` trials, there must be `r-1=2` successes. The 7th trial must be the 3rd success.
    
- `P(X=7) = (6 choose 2) × (0.2)³ × (0.8)⁴ = 15 × 0.008 × 0.4096 ≈ 0.049`.
    

### 6.5 - Hypergeometric Distribution

**Problem:** A deck of cards has 20 cards: 6 red and 14 black. 5 cards are drawn randomly without replacement. What is the probability that exactly 4 red cards are drawn? 7

**Solution:**

- This is a hypergeometric problem.
    
- Population size `N=20`.
    
- Number of successes in population `K=6` (red cards).
    
- Sample size `n=5`.
    
- Number of successes in sample `k=4`.
    
- P(X=4) = [ (6 choose 4) × (14 choose 1) ] / (20 choose 5)
    
    = (15 × 14) / 15504 = 210 / 15504 ≈ 0.0135.
    

### 6.6 - Poisson Distribution

**Problem:** The average number of calculators sold on Amazon is 3.5 per hour. Find the probability that in a given hour, Amazon will sell exactly 3 calculators.8

**Solution:**

- This is a Poisson distribution with `λ = 3.5`. We want `P(X=3)`.
    
- P(X=3) = (e⁻³·⁵ × 3.5³) / 3!
    
    = (0.0302 × 42.875) / 6 ≈ 0.216.
    

---

## Part 7: Continuous Distributions

### 7.2 - Uniform Distribution

**Problem:** The amount of time a person must wait for a bus is uniformly distributed between 0 and 15 minutes. What is the probability that a person waits fewer than 12.5 minutes? 9

**Solution:**

- Here, `a=0` and `b=15`. The PDF is `f(x) = 1/15` for `0 ≤ x ≤ 15`.
    
- We want `P(X < 12.5)`.
    
- P(X < 12.5) = ∫ (from 0 to 12.5) [1/15] dx = [x/15] (from 0 to 12.5)
    
    = 12.5 / 15 ≈ 0.8333.
    

### 7.3 - Normal Distribution

**Problem:** First-year salaries of graduates are normally distributed with a mean `μ = $60,000` and standard deviation `σ = $15,000`. Find the probability of a randomly selected graduate earning less than $45,000.10

**Solution:**

- We need to find `P(X < 45000)`.
    
- First, standardize the value:
    
    Z = (45000 - 60000) / 15000 = -1.0.
    
- We need to find `P(Z < -1.0)`.
    
- Using a standard normal (Z) table or calculator, the area to the left of -1.0 is approximately 0.1587.
    
- There is about a 15.9% chance of a graduate earning less than $45,000.
    

### 7.4 - Exponential Distribution

**Problem:** The lifetime of a lightbulb (in years) is an `Exp(λ=0.3)` random variable. What is the probability that the lightbulb lasts more than 2 years? 11

**Solution:**

- We want `P(X > 2)`.
    
- P(X > 2) = ∫ (from 2 to ∞) [0.3e⁻⁰·³ˣ] dx
    
    = [-e⁻⁰·³ˣ] (from 2 to ∞)
    
    = 0 - (-e⁻⁰·³⁽²⁾) = e⁻⁰·⁶ ≈ 0.5488.
    
- There is about a 54.9% chance the bulb lasts more than 2 years.
    

---

## Part 8: Joint, Marginal, and Conditional Distributions

### 8.2 - Marginal Distributions

**Problem:** Given the following joint PMF, find the marginal distribution of X.12


## Joint Probability Distribution $P(X, Y)$

This table represents the probabilities for the discrete random variables $X$ and $Y$.

||**Y=0**|**Y=1**|
|---|---|---|
|**X=0**|$1/3$|$1/6$|
|**X=1**|$1/3$|$1/6$|
**Solution:**

- `P(X=0) = P(X=0, Y=0) + P(X=0, Y=1) = 1/3 + 1/6 = 1/2`.
    
- `P(X=1) = P(X=1, Y=0) + P(X=1, Y=1) = 1/3 + 1/6 = 1/2`.
    
- The marginal distribution of X is `P(X=0) = 1/2` and `P(X=1) = 1/2`.
    

### 8.5 - Covariance and Correlation

**Problem:** Let X and Y be independent random variables with variances `Var(X) = 5` and `Var(Y) = 3`. Find the variance of the random variable `Z = -2X + 4Y - 3`.4

**Solution:**

- We use the properties of variance.
    
- `Var(Z) = Var(-2X + 4Y - 3)`
    
- `Var(Z) = Var(-2X + 4Y)` (Shifting by a constant does not change variance).
    
- Since X and Y are independent, `Var(A+B) = Var(A) + Var(B)`.
    
- `Var(Z) = Var(-2X) + Var(4Y)`
    
- Using the property Var(aX) = a²Var(X):
    
    Var(Z) = (-2)²Var(X) + (4)²Var(Y)
    
    Var(Z) = 4 × Var(X) + 16 × Var(Y)
    
    Var(Z) = 4 × 5 + 16 × 3 = 20 + 48 = 68.