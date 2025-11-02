# 👟 Shoe Shine Shop: Blocked Tandem Queue Model Summary

This model analyzes two serial servers (S1 and S2) with **zero buffer space** between them. S1 is an M/M/1 queue, but its service is stopped (blocked) if S2 is busy.

## 1. State Space Definition

The system is defined by a 2D state $(n_1, n_2)$, where $n_1$ is the status of Server 1 and $n_2$ is the status of Server 2.

|State $(n_1, n_2)$|Physical Description|Total Customers ($n$)|
|---|---|---|
|$(0, 0)$|S1 Empty, S2 Empty|0|
|$(1, 0)$|S1 Serving, S2 Empty|1|
|$(0, 1)$|S1 Empty, S2 Serving|1|
|$(1, 1)$|S1 Serving, S2 Serving|2|
|$(b, 1)$|S1 **Blocked** (Finished service but waiting for S2), S2 Serving|2|

## 2. Transition Diagram and Rates (Flows)
![[Pasted image 20251027003930.png]]
The diagram defines all possible flows between states. Note the special flow out of the blocked state $(b, 1)$.

|Flow (From $\to$ To)|Rate|Event|Key Rule Involved|
|---|---|---|---|
|$(0, 0) \to (1, 0)$|$\lambda$|Arrival|System goes from empty to S1 serving.|
|$(1, 0) \to (0, 0)$|$\mu_1$|S1 Completion|Customer moves to empty S2 and **departs immediately** (Model Simplification).|
|$(0, 1) \to (0, 0)$|$\mu_2$|S2 Completion|S2 customer departs, leaving the system empty.|
|$(0, 1) \to (1, 1)$|$\lambda$|Arrival|New customer goes to empty S1; S2 remains busy.|
|$(1, 1) \to (b, 1)$|$\mu_1$|**S1 Completion** $\to$ **BLOCK**|S1 finishes, S2 is busy, so S1's customer is stuck.|
|$(b, 1) \to (0, 0)$|$\mu_2$|**S2 Completion** $\to$ **UNBLOCK**|S2 finishes, releasing the entire system (due to simplification).|

## 3. Global Balance Equations (Rate IN = Rate OUT)

These equations must be solved simultaneously, along with the normalization equation $\sum P_{i, j} = 1$, to find the steady-state probabilities $P_{i, j}$.

### State $(0, 0)$

$$\lambda P_{0, 0} = \mu_1 P_{1, 0} + \mu_2 P_{0, 1} + \mu_2 P_{b, 1}$$

### State $(1, 0)$

$$(\lambda + \mu_1) P_{1, 0} = \lambda P_{0, 0}$$

### State $(0, 1)$

$$(\lambda + \mu_2) P_{0, 1} = \mu_2 P_{1, 1}$$

### State $(1, 1)$

$$(\mu_1 + \mu_2) P_{1, 1} = \lambda P_{1, 0} + \lambda P_{0, 1}$$

### State $(b, 1)$

$$\mu_2 P_{b, 1} = \mu_1 P_{1, 1}$$

## 4. Performance Metrics

### Average Number of Customers ($L$)

$L$ is calculated by summing the probability of each state multiplied by the number of customers in that state:

$$L = 1 \cdot (P_{1, 0} + P_{0, 1}) + 2 \cdot (P_{1, 1} + P_{b, 1})$$

### Effective Arrival Rate ($\lambda_a$)

In this specific model, an arrival is only accepted if S1 is completely empty ($n_1=0$).

$$\lambda_a = \lambda (P_{0, 0} + P_{0, 1})$$

### Average Time in System ($W$)

Found using Little's Law:

$$W = \frac{L}{\lambda_a}$$

### Rate of Blocking ($\lambda_b$)

This is the rate at which the actual blocking event occurs (flow into state $(b, 1)$):

$$\lambda_b = \mu_1 P_{1, 1}$$

### Blocking Probability ($\Pi_b$)

The probability that an accepted customer is blocked (Ratio of blocked events to accepted customers):

$$\Pi_b = \frac{\lambda_b}{\lambda_a} = \frac{\mu_1 P_{1, 1}}{\lambda (P_{0, 0} + P_{0, 1})}$$