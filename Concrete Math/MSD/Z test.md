# Comprehensive Z-Test Guide: All Types Explained

The **Z-test** is a hypothesis test used when the test statistic follows a **Standard Normal Distribution** ($\mathcal{N}(0, 1)$). This is reliable when your sample size is large ($n \ge 30$) or when the population standard deviation ($\sigma$) is known.

## Prerequisites and Core Formula

### When to use the Z-test

1. **Population Standard Deviation (**$\sigma$**) is Known:** Use the Z-test regardless of sample size $n$.
    
2. **Sample Size is Large (**$n \ge 30$**):** The **Central Limit Theorem (CLT)** guarantees that the sampling distribution will approximate the Normal distribution, allowing us to use the Z-test, even if we estimate $\sigma$ with the sample standard deviation ($S$).
    

### The General Z-Test Statistic

The test statistic is a measure of the distance (in standard error units) between what you observed in your sample and what $H_0$ claimed was true.

$$\mathbf{Z\text{-test statistic} = \frac{\text{Observed Sample Statistic} - \text{Hypothesized Population Parameter}}{\text{Standard Error (SE)}}}$$

## The Difference: One-Tailed vs. Two-Tailed Tests

The type of test you choose is dictated by your **Alternative Hypothesis (**$H_A$**)** and reflects the specific claim you are trying to find evidence for.

### One-Tailed Test (Directional)

Used when you are only looking for a difference in a **single direction** (e.g., performance is _better_ or _worse_).

|Type of Claim|Alternative Hypothesis ($H_A$)|P-Value Calculation|
|---|---|---|
|**Greater Than**|$H_A: \mu > \mu_0$|$P(Z > z_{\text{calc}})$|
|**Less Than**|$H_A: \mu < \mu_0$|$P(Z < z_{\text{calc}})$|

**Intuition:** The rejection region (area $\alpha$) is concentrated entirely in one tail.

### Two-Tailed Test (Non-Directional)

Used when you are only interested if the parameter is **different** (higher **or** lower). This is the default choice unless a direction is hypothesized.

|Type of Claim|Alternative Hypothesis ($H_A$)|P-Value Calculation|
|---|---|---|
|**Not Equal To**|$H_A: \mu \ne \mu_0$|$2 \times P(|

**Intuition:** The rejection region is split equally between the two tails ($\alpha/2$ in each tail).

## Type 1: One-Sample Z-Test for the Mean

Tests if a single sample mean ($\bar{X}$) is different from a hypothesized population mean ($\mu_0$).

### Formula

$$Z = \frac{\bar{X} - \mu_0}{\text{SE}} \quad \text{where} \quad \text{SE} = \frac{\sigma}{\sqrt{n}} \approx \frac{S}{\sqrt{n}}$$

### Example: Website Load Time

**Scenario:** $H_0: \mu = 2.5$ seconds. Sample $n=100$. Observed $\bar{X}=2.3$s, $S=0.8$s. Test if the mean is significantly **less than** $2.5$s ($\alpha=0.05$).

1. **Hypotheses:** $H_0: \mu = 2.5$ vs $H_A: \mu < 2.5$ (**One-tailed**).
    
2. **SE:** $0.8 / \sqrt{100} = 0.08$.
    
3. **Z-Statistic:** $Z = (2.3 - 2.5) / 0.08 = \mathbf{-2.50}$.
    
4. **P-value & Decision:**
    
    - $P(Z < -2.50) \approx 0.0062$.
        
    - Since $0.0062 < 0.05$, **Reject** $H_0$. (It is significantly less.)
        

## Type 2: Two-Sample Z-Test for Means

Compares the means of two independent groups ($\mu_1$ and $\mu_2$).

### Formula

$H_0: \mu_1 - \mu_2 = 0$. The test uses the difference in sample means ($\bar{X}_1 - \bar{X}_2$) and a combined standard error.

$$Z = \frac{(\bar{X}_1 - \bar{X}_2) - 0}{\text{SE}_{\bar{X}_1 - \bar{X}_2}} \quad \text{where} \quad \text{SE}_{\bar{X}_1 - \bar{X}_2} = \sqrt{\frac{S_1^2}{n_1} + \frac{S_2^2}{n_2}}$$

### Example: Comparing Two Algorithms

**Scenario:** Test if Algorithm A is significantly **faster** than Algorithm B ($\mu_A < \mu_B$).

- $n_A=50, \bar{X}_A=12.1, S_A=1.5$.
    
- $n_B=60, \bar{X}_B=12.8, S_B=1.2$. ($\alpha=0.01$).
    

1. **Hypotheses:** $H_0: \mu_A = \mu_B$ vs $H_A: \mu_A < \mu_B$ (**One-tailed**).
    
2. $\text{SE}_{\text{diff}}$**:** $\sqrt{(1.5^2/50) + (1.2^2/60)} \approx 0.2627$.
    
3. **Z-Statistic:** $Z = (12.1 - 12.8) / 0.2627 \approx \mathbf{-2.66}$.
    
4. **P-value & Decision:**
    
    - $P(Z < -2.66) \approx 0.0039$.
        
    - Since $0.0039 < 0.01$, **Reject** $H_0$. (Algorithm A is significantly faster.)
        

## Type 3: One-Sample Z-Test for Proportions

Tests hypotheses about a single population **proportion** ($P$, e.g., error rate).

### Formula

The standard error is based on the hypothesized proportion ($P_0$) from $H_0$.

$$Z = \frac{\hat{P} - P_0}{\text{SE}_{\hat{P}}} \quad \text{where} \quad \text{SE}_{\hat{P}} = \sqrt{\frac{P_0 (1 - P_0)}{n}}$$

### Example: Hardware Defect Rate

**Scenario:** Manufacturer claims defect rate $P=0.03$. Test $n=400$ units, find 18 defects ($\hat{P}=0.045$). Test if the claim is wrong ($\alpha=0.05$).

1. **Hypotheses:** $H_0: P = 0.03$ vs $H_A: P \ne 0.03$ (**Two-tailed**).
    
2. **SE:** $\sqrt{(0.03 \times 0.97) / 400} \approx 0.0085$.
    
3. **Z-Statistic:** $Z = (0.045 - 0.03) / 0.0085 \approx \mathbf{1.76}$.
    
4. **P-value & Decision:**
    
    - Two-tailed $P$: $2 \times P(Z > 1.76) \approx 0.0784$.
        
    - Since $0.0784 > 0.05$, **Fail to Reject** $H_0$. (The difference is not significant.)
        

## Type 4: Two-Sample Z-Test for Proportions (A/B Testing)

Compares two independent sample proportions ($\hat{P}_1$ and $\hat{P}_2$), crucial for A/B testing a conversion rate, click-through rate, or model success rate.

### Formula

$H_0: P_1 - P_2 = 0$. Since we assume $P_1 = P_2$ under $H_0$, we must use a **pooled proportion** ($\hat{P}_c$) for the standard error calculation.

$$Z = \frac{(\hat{P}_1 - \hat{P}_2) - 0}{\text{SE}_{\text{Pooled}}}$$$$\text{where } \hat{P}_c = \frac{X_1 + X_2}{n_1 + n_2} \quad \text{ and } \quad \text{SE}_{\text{Pooled}} = \sqrt{\hat{P}_c (1 - \hat{P}_c) \left(\frac{1}{n_1} + \frac{1}{n_2}\right)}$$

($X_i$ is the number of successes, $X_i = n_i \hat{P}_i$).

### Example: A/B Test for Click-Through Rate (CTR)

**Scenario:** We compare two button designs, A and B, for a click-through rate (CTR).

- **Design A:** $n_A = 1000$ views, $X_A = 120$ clicks ($\hat{P}_A = 0.12$).
    
- **Design B:** $n_B = 1500$ views, $X_B = 150$ clicks ($\hat{P}_B = 0.10$). Test if Design A has a significantly **higher** CTR than Design B ($\alpha=0.05$).
    

1. **Hypotheses:** $H_0: P_A = P_B$ vs $H_A: P_A > P_B$ (**One-tailed**).
    
2. **Calculate Pooled Proportion (**$\hat{P}_c$**):**
    
    $$\hat{P}_c = \frac{120 + 150}{1000 + 1500} = \frac{270}{2500} = 0.108$$
3. **Calculate** $\text{SE}_{\text{Pooled}}$**:**
    
    $$\text{SE}_{\text{Pooled}} = \sqrt{0.108 \times 0.892 \times \left(\frac{1}{1000} + \frac{1}{1500}\right)} \approx \sqrt{0.0001602} \approx \mathbf{0.01266}$$
4. **Calculate Z-Statistic:**
    
    $$Z = \frac{0.12 - 0.10}{0.01266} = \frac{0.02}{0.01266} \approx \mathbf{1.58}$$
5. **P-value & Decision:**
    
    - $P(Z > 1.58) \approx 0.0571$.
        
    - Since $0.0571 > \alpha (0.05)$, we **Fail to Reject** $H_0$.
        
    - **Conclusion:** Design A's observed CTR is slightly higher, but the difference is not statistically significant at the $5\%$ level. We cannot conclude that Design A is truly better.