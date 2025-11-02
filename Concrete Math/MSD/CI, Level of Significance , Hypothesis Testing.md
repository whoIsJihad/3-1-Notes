
---

## 1. Confidence Intervals (CI)

A **Confidence Interval** is an estimated range of values that is likely to contain the true value of an unknown population parameter (like the population mean, $\mu$).

### What it Means:

Instead of saying, "The average height of all BUET students is exactly 170 cm" (which is probably wrong), a CI allows you to say, "**I am 95% confident that the true average height is between 168 cm and 172 cm.**"

### Key Components:

- **Point Estimate:** The single best guess for the parameter (e.g., the **sample mean** $\bar{X}$).
    
- **Margin of Error:** The $\pm$ amount added to and subtracted from the point estimate to create the interval.
    
- **Confidence Level ($1 - \alpha$):** This is the probability that the procedure used to calculate the interval will produce an interval that contains the true parameter. Common levels are 90%, 95%, or 99%.
    

### The Interpretation (The Tricky Part):

If you repeatedly take many random samples and calculate a **95% CI** for each sample, approximately 95% of those calculated intervals will contain the true population mean $\mu$.

**Crucially, it is NOT the probability that the true mean is in _this specific_ interval.** The true mean is a fixed value; it's either in your interval or it's not. The confidence is in the _method_ used to generate the interval.

---

## 2. Level of Significance ($\alpha$)

The **Level of Significance** (denoted by the Greek letter $\alpha$, _alpha_) is directly related to the confidence level and is central to hypothesis testing.

### What it Means:

The level of significance is the **maximum probability of rejecting a true null hypothesis** (making a **Type I Error**).

- If you choose $\alpha = 0.05$ (the most common value), you are accepting a 5% risk of incorrectly concluding there is an effect or difference when, in reality, there is none.
    

### Connection to CI:

$$\text{Confidence Level} = 1 - \alpha$$

- A **95% Confidence Interval** corresponds to a **Level of Significance** ($\alpha$) of **0.05**.
    
- A **99% Confidence Interval** corresponds to a **Level of Significance** ($\alpha$) of **0.01**.
    

Think of $\alpha$ as your **"bar for proof."** If the probability of your results occurring by chance is lower than $\alpha$, you conclude the results are significant.

---

## 3. Hypothesis Testing

**Hypothesis Testing** is a formal procedure for using sample data to decide between two competing claims (hypotheses) about a population.

This is the entire engine for making decisions in research and data analysis.

### Step-by-Step Procedure:

### Step 1: State the Hypotheses

You always set up two opposing statements:

- **Null Hypothesis ($H_0$):** The statement of **no effect**, **no difference**, or **no change**. (The status quo assumption, e.g., $\mu = 170$ cm).
    
- **Alternative Hypothesis ($H_a$ or $H_1$):** The statement that is accepted if the evidence suggests the null hypothesis is false. (e.g., $\mu \ne 170$ cm).
    

### Step 2: Choose the Level of Significance ($\alpha$)

Set your acceptable risk level (e.g., $\alpha = 0.05$).

### Step 3: Calculate the Test Statistic

You crunch the sample data to get a single number (**Test Statistic**), which measures how many standard errors your sample result ($\bar{X}$) is away from the value stated in $H_0$. (This could be a $Z$-score, a $t$-score, etc.)

### Step 4: Find the p-value

The **p-value** (or _probability value_) is the core of the test.

- **Definition:** The p-value is the probability of observing a test statistic **as extreme as**, or **more extreme than**, the one calculated from your sample **IF the Null Hypothesis ($H_0$) were actually true.**
    

### Step 5: Make a Decision

You compare the p-value to the level of significance ($\alpha$):

- **If p-value $\le \alpha$:** This means the observed data is very unlikely to have happened by chance if $H_0$ were true. You **reject the null hypothesis ($H_0$)** and conclude the alternative hypothesis ($H_a$) is supported. (The result is **statistically significant**).
    
- **If p-value $> \alpha$:** This means the data is reasonably likely to have occurred even if $H_0$ is true. You **fail to reject the null hypothesis ($H_0$)**. (This does **not** mean $H_0$ is true; it just means you don't have enough evidence to reject it).
    

---

### Example Summary:

Imagine testing if a new network optimization algorithm is faster than the old one (average time $\mu_{old}$).

1. **Hypotheses:** $H_0: \mu_{new} = \mu_{old}$ (No difference) vs. $H_a: \mu_{new} < \mu_{old}$ (New is faster).
    
2. **$\alpha$:** You set $\alpha = 0.05$.
    
3. **Data:** You run the new algorithm 50 times and get $\bar{X}_{new}$.
    
4. **p-value:** You calculate the p-value is $0.01$.
    
5. **Decision:** Since **$0.01 \le 0.05$** (p-value $\le \alpha$), you **reject $H_0$**. You conclude there is statistically significant evidence that the new algorithm is indeed faster. 🎉