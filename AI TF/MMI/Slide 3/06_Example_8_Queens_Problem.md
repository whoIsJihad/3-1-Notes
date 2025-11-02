# ♟️ Example: N-Queens Problem (N=8)

**Problem:** Place 8 non-attacking queens on an $8 \times 8$ board (no two queens share a row, column, or diagonal).

## Two Problem Formulation Approaches

The definition of **State** determines the size and complexity of the search space.

|Component|**Formulation 1 (Less Efficient)**|**Formulation 2 (Constrained/Better)**|
|---|---|---|
|**States**|Any arrangement of $n \le 8$ queens on the board.|Arrangement of $n \le 8$ queens in leftmost $n$ columns, one per column, **s.t. no queen attacks any other yet**.|
|**Initial State**|No queens on the board.|No queens on the board.|
|**Actions**|Add a queen to any empty square.|Add a queen to the **leftmost empty square** that is not attacked by existing queens.|
|**Goal Test**|8 queens on the board, none attacked.|8 queens on the board, none attacked.|
|**Approach Note**|Requires a larger search space.|Incorporates constraints into the _state_ definition, dramatically reducing the search space.|
