# MAP and ML Hypotheses in Bayesian Learning

Tags: #machine_learning #bayesian #MAP #ML #AIMA
Easier Version by GPT [[MAP and ML Hypotheses (Easier)]]
This note covers the concepts of Maximum A Posteriori (MAP) and Maximum Likelihood (ML) hypotheses, often used in Bayesian learning, as mentioned in the AIMA text [cite: PDF Page 5].

## Bayes' Theorem

The foundation for this is Bayes' Theorem, which relates the posterior probability of a hypothesis $H$ given data $D$ to its prior probability and the likelihood of the data.

$$P(H|D) = \frac{P(D|H) P(H)}{P(D)}$$

Where:

- $P(H|D)$ is the **posterior probability**: what we believe about $H$ _after_ seeing the data $D$.
    
- $P(D|H)$ is the **likelihood**: the probability of observing data $D$ if hypothesis $H$ were true.
    
- $P(H)$ is the **prior probability**: what we believed about $H$ _before_ seeing any data.
    
- $P(D)$ is the evidence, which is a normalizing constant. It is the same for all hypotheses.
    

## MAP (Maximum A Posteriori) Hypothesis

The MAP hypothesis, $h_{MAP}$, is the hypothesis $h_i$ from a set of hypotheses that is most probable _given_ the data $d$.

$$h_{MAP} = \arg\max_{h_i} P(h_i | d)$$

Using Bayes' theorem, we can rewrite this:

$$h_{MAP} = \arg\max_{h_i} \frac{P(d | h_i) P(h_i)}{P(d)}$$

Since $P(d)$ is a constant for all $h_i$, we can remove it from the maximization:

$$h_{MAP} = \arg\max_{h_i} P(d | h_i) P(h_i)$$

The MAP hypothesis balances two factors:

1. $P(d | h_i)$ **(Likelihood):** How well the hypothesis _explains_ the data. This ensures the hypothesis is **consistent** with the data.
    
2. $P(h_i)$ **(Prior):** Our prior belief in the hypothesis. This allows us to incorporate **Occam's Razor** by assigning a higher $P(h_i)$ to simpler hypotheses. The trade-off is that an overly simple hypothesis might not predict well.
    

## ML (Maximum Likelihood) Hypothesis

The ML hypothesis, $h_{ML}$, is the hypothesis $h_i$ that _maximizes_ the likelihood of the data.

$$h_{ML} = \arg\max_{h_i} P(d | h_i)$$

This is a special case of MAP. If we assume a **uniform prior** (i.e., we believe all hypotheses $h_i$ are equally likely _before_ seeing the data, $P(h_i) = P(h_j)$ for all $i, j$), then the $P(h_i)$ term is a constant and can be dropped from the MAP calculation, leaving just the ML calculation.

For a dataset $d$ with $N$ i.i.d. samples $d_j$, the likelihood is the product of the individual likelihoods:

$$P(d | h) = \prod_{j=1}^{N} P(d_j | h)$$

## Example from Lecture (Parameter Learning) [cite: PDF Page 6]

This example sets up a parameter learning problem. We have two types of candy bags, Cherry and Lime. The _parameters_ (our hypothesis $h_{\theta}$) are the probabilities of drawing a red or green candy from each type of bag.

Let $\theta_1$ be the probability of a red candy from a Cherry bag:

- $P(W=\text{red} | \text{Bag}=\text{cherry}) = \theta_1$
    
- $P(W=\text{green} | \text{Bag}=\text{cherry}) = 1 - \theta_1$
    

Let $\theta_2$ be the probability of a red candy from a Lime bag:

- $P(W=\text{red} | \text{Bag}=\text{lime}) = \theta_2$
    
- $P(W=\text{green} | \text{Bag}=\text{lime}) = 1 - \theta_2$
    

Given a set of observations (e.g., "5 red candies and 2 green from a Cherry bag"), we could use ML to find the value of $\theta_1$ that makes these observations most likely.

## Additional Solved Problem (External)

- **Problem:** You flip a coin 10 times and observe 7 Heads (H) and 3 Tails (T). Let the hypothesis $h_{\theta}$ be that the coin has a probability $\theta$ of landing Heads ($P(H) = \theta$). What is the Maximum Likelihood (ML) estimate for $\theta$?
    
- **Solution:**
    
    1. **Define the Likelihood** $P(d | h_{\theta})$**:** The data $d$ is (7H, 3T). The probability of any specific sequence with 7H and 3T (e.g., HHTHTHHHHT) is $\theta^7 (1-\theta)^3$.
        
    2. **Formulate the Likelihood Function** $L(\theta)$**:** The number of such sequences is given by the binomial coefficient $\binom{10}{7}$.
        
        - $L(\theta) = P(d | \theta) = \binom{10}{7} \theta^7 (1-\theta)^3$.
            
    3. **Find the** $\theta$ **that maximizes** $L(\theta)$**:** We want to find $\arg\max_{\theta} L(\theta)$.
        
    4. **Use Log-Likelihood:** It's easier to maximize the log-likelihood, $\ln(L(\theta))$, since the $\arg\max$ will be the same.
        
        - $\ln(L(\theta)) = \ln\left(\binom{10}{7}\right) + 7 \ln(\theta) + 3 \ln(1-\theta)$.
            
    5. **Take the derivative with respect to** $\theta$ **and set to 0:**
        
        - $\frac{d}{d\theta} \ln(L(\theta)) = 0 + \frac{7}{\theta} + \frac{3}{1-\theta} \cdot (-1) = \frac{7}{\theta} - \frac{3}{1-\theta}$.
            
        - Set to 0: $\frac{7}{\theta} = \frac{3}{1-\theta}$.
            
        - $7(1-\theta) = 3\theta$.
            
        - $7 - 7\theta = 3\theta$.
            
        - $7 = 10\theta$.
            
        - $\theta = 7/10 = 0.7$.
            
    
    - **Answer:** The Maximum Likelihood estimate for $\theta$ is $0.7$, which intuitively matches the observed data (7 heads in 10 flips).