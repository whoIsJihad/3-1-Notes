# Chance Games

Not all games are purely deterministic. **Chance games** (or stochastic games) involve an element of randomness, like dice rolls (Backgammon) or card draws (Poker).

To handle this, we introduce **Chance Nodes** into the game tree, in addition to MAX and MIN nodes.

## Expected Minimax

We can't use the standard [[Minimax Algorithm]] because we don't know what the outcome of a chance node will be. Instead, we calculate the **expected value** by averaging the values of all possible outcomes, weighted by their probability.

`EXPECTED-MINIMAX-VALUE(n)` =

- `UTILITY(n)` if `n` is a terminal node
    
- `max(EXPECTED-MINIMAX-VALUE(s))` if `n` is a MAX node
    
- `min(EXPECTED-MINIMAX-VALUE(s))` if `n` is a MIN node
    
- $\sum_{s} P(s) \times \text{EXPECTED-MINIMAX-VALUE}(s)$ if `n` is a Chance node
    

For example, if a dice roll has two possible outcomes (s1, s2), each with 50% probability (P=0.5): `Value(n) = 0.5 * Value(s1) + 0.5 * Value(s2)`

**Links:**

- Back to: [[Adversarial Search Index]]