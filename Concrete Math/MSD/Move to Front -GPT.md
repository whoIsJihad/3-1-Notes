
---

## Move-to-Front (MTF) Model — Obsidian-Friendly Version

### 1️⃣ Move-to-Front Rule

$$  
\text{When an item } e_i \text{ is requested, move it instantly to the front of the list.}  
$$

Example:

$$  
[A, B, C, D] \xrightarrow{\text{request C}} [C, A, B, D]  
$$

---

### 2️⃣ Goal: Expected position of next requested item

$$  
E[\text{Position of next requested item}]  
$$

---

### 3️⃣ Setup

$$  
\text{List: } e_1, e_2, \dots, e_n  
$$

$$  
P_i = \text{probability of requesting } e_i, \quad \sum_{i=1}^{n} P_i = 1  
$$

---

### 4️⃣ Formula for expected position

$$  
E[\text{Position of requested element}] = \sum_{i=1}^{n} P_i , E[\text{Position of } e_i]  
$$

---

### 5️⃣ Position of a single element

$$  
\text{Position of } e_i = 1 + \sum_{j \neq i} I_j  
$$

Where

$$  
I_j =  
\begin{cases}  
1 & \text{if } e_j \text{ is before } e_i \  
0 & \text{otherwise}  
\end{cases}  
$$

---

### 6️⃣ Expected position using indicators

$$  
E[\text{Position of } e_i] = 1 + \sum_{j \neq i} E[I_j] = 1 + \sum_{j \neq i} P(e_j \text{ is before } e_i)  
$$

---

### 7️⃣ Steady-state probability

$$  
P(e_j \text{ precedes } e_i) = \frac{P_j}{P_i + P_j}  
$$

---

### 8️⃣ Expected position of a single element

$$  
E[\text{Position of } e_i] = 1 + \sum_{j \neq i} \frac{P_j}{P_i + P_j}  
$$

---

### 9️⃣ Expected position of requested element

$$  
E[\text{Position of requested}] = \sum_{i=1}^{n} P_i \left( 1 + \sum_{j \neq i} \frac{P_j}{P_i + P_j} \right)  
$$

---

### 10️⃣ Simplified formula

$$  
E[\text{Position of requested}] = 1 + \sum_{i=1}^{n} \sum_{j \neq i} \frac{P_i P_j}{P_i + P_j} = 1 + 2 \sum_{i<j} \frac{P_i P_j}{P_i + P_j}  
$$

---

### 11️⃣ Example: 3 elements

|Element|Probability|
|---|---|
|A|0.6|
|B|0.3|
|C|0.1|

Pairs: (A,B), (A,C), (B,C)

$$  
E[\text{Position}] = 1 + 2 \left( \frac{0.6 \cdot 0.3}{0.6+0.3} + \frac{0.6 \cdot 0.1}{0.6+0.1} + \frac{0.3 \cdot 0.1}{0.3+0.1} \right)  
$$

$$  
E[\text{Position}] = 1 + 2 (0.20 + 0.0857 + 0.075) \approx 1.7214  
$$

---

### 12️⃣ Intuition

$$  
\text{Popular items (high } P_i) \text{ stay near the front → lower positions.}  
$$

$$  
\text{Rare items (low } P_i) \text{ fall behind → higher positions.}  
$$

$$  
\text{If all items equally likely: expected position } \approx \frac{n+1}{2}  
$$
