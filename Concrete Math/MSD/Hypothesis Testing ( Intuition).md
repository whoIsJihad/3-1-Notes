

---

## Hypothesis Testing: The Core Logic

The entire purpose of hypothesis testing is to quantify **how surprised** you should be by your data.

### Step 1: The Assumption (The "Null World")

Before you start any calculation, you must make an assumption. This assumption is the **Null Hypothesis ($H_0$)**.

- $H_0$ is the **status quo**. It states that nothing interesting or unusual is happening. (e.g., The average ping time is 50ms. The new CPU is not faster than the old one.)
    

**The Calculation's Foundation:** All subsequent calculations are performed under the assumption that $H_0$ is **$100\%$ TRUE**.

### Step 2: Defining "Normal" (The Bell Curve)

If $H_0$ is true, what would a typical result look like?

Due to the Central Limit Theorem, when we take a sample, the distribution of our test results (like the sample average) is always a **bell curve**.

- **The Center ($\mu_0$):** The center of this bell curve is defined by the value claimed in $H_0$. (If $H_0$ says the average is 50ms, the center of the curve is 50ms).
    
- **The Spread ($\sigma$):** The spread (Standard Error) is calculated based on the sample size and known variance.
    

This curve is the visual map of the **Null World**—it shows all the **normal** results and the **rare** results

![Image of a Normal distribution bell curve](https://encrypted-tbn3.gstatic.com/licensed-image?q=tbn:ANd9GcTbZ2gl7DiCPPoMMF28CAhMaqs4XloxCkO00Jp0xLW4F6Tn8HQa8oXFa3Vc_gT98mTNBYwYc4LLoj_xtZanMqaE_rBSEHBvQhsbDUtQNXp_7oZIZQE)

Shutterstock

.

### Step 3: Finding Your Evidence (The Test Statistic)

You collected data and got a result (e.g., you measured the average ping time as 48ms).

- **Test Statistic:** This is the calculation that measures **how many standard deviations** your result is away from the center ($\mu_0$). It tells you where your observed data falls on the Null World map.
    

$$\text{Test Statistic (e.g., Z-score)} = \frac{\text{Your Observed Result} - \text{Null Claim} (H_0)}{\text{Standard Error}}$$

### Step 4: The p-value (The Measure of Surprise)

Once you find your Test Statistic (e.g., $Z = 5.6$), you calculate the **p-value**.

- **What is the p-value?** It is the **probability** of observing a result **as extreme as or more extreme than yours**, _if the Null World were true._
    
- **Visualization:** It is the **area in the tail(s)** of the bell curve, starting from your Test Statistic and moving outward.
    
    - **Small p-value:** Your data is in a very thin, unlikely part of the curve. **You should be very surprised.**
        
    - **Large p-value:** Your data is right in the middle, a very common outcome. **You should not be surprised.**
        

### Step 5: The Decision (The Threshold)

You need a benchmark to decide if the surprise is big enough to matter. This is the **Level of Significance ($\alpha$)**.

- **$\alpha$:** This is your **rejection threshold**, usually set at $0.05$ (5%). It's the maximum risk you accept of making a mistake.
    

**The Rule:**

- **If p-value $\le \alpha$ (e.g., $0.0001 \le 0.05$):** Your data is so rare in the Null World that it is easier to conclude **the Null World does not exist**. You **REJECT $H_0$**.
    
- **If p-value $> \alpha$ (e.g., $0.30 > 0.05$):** Your data is common in the Null World. You **FAIL TO REJECT $H_0$** (meaning, you don't have enough proof to say $H_0$ is wrong).



---

## Hardcore Numerical Example: Testing a New CPU

**SCENARIO:** You are a systems engineer. The average idle temperature of your server rack is known to be **$50^\circ\text{C}$** with a standard deviation ($\sigma$) of **$4^\circ\text{C}$**. Your Null Hypothesis ($H_0$) is that the temperature has not changed.

You install new cooling fans and measure the temperature 16 times ($n=16$). The average temperature of your 16 samples is $\mathbf{52.5^\circ\text{C}}$.

**QUESTION:** Did the new fans increase the temperature? Use a significance level of $\mathbf{\alpha = 0.05}$ (5%).

---

### Step 1: Define Hypotheses and Context

|**Term**|**Value**|**Meaning**|
|---|---|---|
|**$H_0$**|$\mu = 50$|**Null Hypothesis:** The true average temperature is still $50^\circ\text{C}$.|
|**$H_A$**|$\mu > 50$|**Alternative Hypothesis:** The true average temperature has **increased** (one-tailed test).|
|**$\mu_0$**|$50$|The assumed population mean (the center of our curve).|
|**$\sigma$**|$4$|The known population standard deviation.|
|**$n$**|$16$|The number of samples taken.|
|**$\bar{x}$**|$52.5$|Your observed sample average.|
|**$\alpha$**|$0.05$|Your rejection threshold (5%).|

### Step 2: Calculate the Standard Error (SE)

This tells us the expected **spread** of our sample averages if $H_0$ is true.

$$\text{SE} = \frac{\sigma}{\sqrt{n}} = \frac{4}{\sqrt{16}} = \frac{4}{4} = \mathbf{1.0}$$

- **Meaning:** If $H_0$ is true, the sample average ($\bar{x}$) will vary by about $\mathbf{1.0}$ degree.
    

### Step 3: Calculate the Test Statistic (The Z-score)

The Z-score tells us **how many standard errors** your observed sample average ($\bar{x}=52.5$) is away from the assumed mean ($\mu_0=50$).

$$\mathbf{Z} = \frac{\bar{x} - \mu_0}{\text{SE}} = \frac{52.5 - 50}{1.0} = \mathbf{2.5}$$

- **Meaning:** Your observed average of $52.5^\circ\text{C}$ is **$2.5$ standard errors** higher than the expected average of $50^\circ\text{C}$.
    

### Step 4: Find the p-value

The p-value is the probability of getting a Z-score of $2.5$ or higher, assuming $H_0$ is true. We look this up in a Z-table (Standard Normal Distribution Table).

- **Z-Table Lookup:** The area to the left of $Z=2.5$ is $0.9938$.
    
- **p-value (Area to the Right):** $P(Z \ge 2.5) = 1.0 - 0.9938 = \mathbf{0.0062}$
    
- **Meaning:** If the true temperature is $50^\circ\text{C}$, there is only a **$0.62\%$ chance** of randomly measuring an average temperature of $52.5^\circ\text{C}$ or higher.
    

### Step 5: Decision

We compare the calculated p-value to the set significance level $\alpha$.

|**Calculated p-value**|**Threshold α**|**Comparison**|**Decision**|
|---|---|---|---|
|$\mathbf{0.0062}$|$\mathbf{0.05}$|$0.0062 \le 0.05$|**Reject $H_0$**|

- **Conclusion:** Because the probability of seeing our data ($0.0062$) is less than our acceptable risk ($0.05$), we conclude that the data provides strong evidence against the Null Hypothesis. **We reject the claim that $\mu=50$ and conclude that the fans have increased the temperature.**
    

---

## The Graph's Practical Role

The graph is just a picture of Step 4/Step 5.

1. **Center:** $\mu=50$.
    
2. **Your Result:** $Z=2.5$ is far to the right.
    
3. **Your Risk:** The $\alpha=0.05$ zone starts at $Z=1.645$. (If your result is higher than 1.645, you reject.)
    
4. **Comparison:** Your result ($Z=2.5$) is clearly past the rejection line ($Z=1.645$). Your shaded p-value area ($0.0062$) is much smaller than the rejection zone ($0.05$).
    

The calculation **$0.0062 \le 0.05$** is the only thing that matters, and the graph illustrates why you did the calculation.