This note covers the **Maximum A Posteriori (MAP)** and **Maximum Likelihood (ML)** hypotheses in Bayesian learning.

## 1️⃣ Bayes’ Theorem

Bayes’ Theorem is the foundation. It tells us **how to update our belief** about a hypothesis after seeing data:

$$P(H \mid D) = \frac{P(D \mid H) P(H)}{P(D)}$$

**Intuition:**

- The posterior is a combination of **what you believed before** (prior) and **what the data suggests** (likelihood).
    
- MAP and ML are different ways to pick the “best hypothesis” using this formula.
    

## 2️⃣ Maximum A Posteriori (MAP) Hypothesis

The MAP hypothesis is the one that is **most probable after seeing the data**:

$$h_{MAP} = \arg\max_{h_i} P(h_i \mid D)$$

Using Bayes’ Theorem:

$$h_{MAP} = \arg\max_{h_i} \frac{P(D \mid h_i) , P(h_i)}{P(D)}$$

Since $(P(D))$ is the same for all hypotheses, we can drop it:

$$h_{MAP} = \arg\max_{h_i} P(D \mid h_i) , P(h_i)$$

### Intuition:

- $(P(D \mid h_i))$ = How well the hypothesis explains the data (likelihood).
    
- $(P(h_i))$ = How plausible the hypothesis was **before seeing any data** (prior).
    
- MAP = “Pick the hypothesis that balances **fit to data** and **prior belief**.”
    

## 3️⃣ Maximum Likelihood (ML) Hypothesis

The ML hypothesis **ignores the prior** and only looks at the data:

$$h_{ML} = \arg\max_{h_i} P(D \mid h_i)$$

### Relationship between MAP and ML:

- MAP reduces to ML if the prior is **uniform**, meaning we initially believe all hypotheses are equally likely:
    

$$P(h_i) = P(h_j) \quad \forall i, j$$

- ML is just MAP without any bias from prior beliefs.
    

## 4️⃣ Likelihood for Multiple Observations

If we have $(N)$ independent observations $(D = {d_1, d_2, \dots, d_N})$, the likelihood is:

$$P(D \mid h) = \prod_{j=1}^{N} P(d_j \mid h)$$

- Because the samples are independent, the total likelihood is the product of individual likelihoods.
    
- Log-likelihood is often used in practice:
    

$$\ln P(D \mid h) = \sum_{j=1}^{N} \ln P(d_j \mid h)$$

- Maximizing log-likelihood is equivalent to maximizing likelihood but easier to compute.
    

## 5️⃣ Intuitive Explanation

- **ML** = purely “data-driven”: Which hypothesis would **most likely produce the data I saw**?
    
- **MAP** = “data + prior belief”: Which hypothesis is **most likely given the data and what I already believed**?
    

**Key idea:**

- Small datasets → MAP leans on prior more.
    
- Large datasets → ML and MAP often converge because the data dominates.
    

## 6️⃣ Parameter Learning Example: Candy Bags

Suppose we have **two types of candy bags**: Cherry and Lime. Each bag has a probability of giving a red or green candy. Our goal is to **estimate the probabilities** from observed candies.

Let:

$$\theta_1 = P(\text{red} \mid \text{Cherry bag}), \quad \theta_2 = P(\text{red} \mid \text{Lime bag})$$

Then:

$$\begin{aligned} P(\text{green} \mid \text{Cherry}) &= 1 - \theta_1 \\ P(\text{green} \mid \text{Lime}) &= 1 - \theta_2 \end{aligned}$$

**Example observation:** 5 red candies, 2 green candies from a Cherry bag.

- **ML estimate for** $(\theta_1)$: Find the value of $(\theta_1)$ that maximizes the probability of seeing this data.
    

$$L(\theta_1) = \theta_1^5 (1-\theta_1)^2$$

- Maximize $(L(\theta_1))$ by taking derivative:
    

$$\frac{d}{d\theta_1} \ln L(\theta_1) = \frac{5}{\theta_1} - \frac{2}{1-\theta_1} = 0$$

- Solve:
    

$$5(1-\theta_1) = 2 \theta_1 \implies 5 - 5\theta_1 = 2 \theta_1 \implies 5 = 7\theta_1 \implies \theta_1 = \frac{5}{7} \approx 0.714$$

- **Interpretation:** The ML estimate says $(\theta_1 \approx 0.714)$, meaning 71.4% chance of drawing a red candy from a Cherry bag.
    

## 7️⃣ Coin Flip Example

Flip a coin 10 times: observe 7 heads and 3 tails. Hypothesis: coin has probability $(\theta)$ of heads.

- **Likelihood function**:
    

$$L(\theta) = \binom{10}{7} \theta^7 (1-\theta)^3$$

- **Log-likelihood**:
    

$$\ln L(\theta) = \ln \binom{10}{7} + 7 \ln \theta + 3 \ln (1-\theta)$$

- **Derivative**:
    

$$\frac{d}{d\theta} \ln L(\theta) = \frac{7}{\theta} - \frac{3}{1-\theta} = 0$$

- Solve:
    

$$7(1-\theta) = 3\theta \implies 7 - 7\theta = 3\theta \implies 7 = 10\theta \implies \theta = 0.7$$

- **Answer:** ML estimate of $(\theta = 0.7)$. Makes sense: 7 heads in 10 flips → 70% probability.
    

✅ **Summary Intuition**

|Concept|Formula|Intuition||
|---|---|---|---|
|Maximum Likelihood (ML)|$(h_{ML} = \arg\max_h P(D \mid h))$|Pick hypothesis that best fits the data only||
|Maximum A Posteriori (MAP)|$(h_{MAP} = \arg\max_h P(D \mid h) P(h))$|Pick hypothesis that fits the data **and** prior belief||
|Prior|$(P(h))$|Your initial belief about hypotheses before seeing data||
|Likelihood|$(P(D \mid h))$|How consistent the data is with the hypothesis||