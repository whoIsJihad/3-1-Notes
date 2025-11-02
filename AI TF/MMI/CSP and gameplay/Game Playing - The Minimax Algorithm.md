# Game Playing: The Minimax Algorithm

Hello again! Now we're diving into the world of **adversarial search**, which is just a formal way of saying "game playing." This is all about making optimal decisions when you have an opponent who is _also_ trying to make optimal decisions.

This note covers the "what" and "why" of game playing, focusing on the foundational **Minimax** algorithm. For the essential optimization that makes this practical, see the companion note: [[Game Playing - Alpha-Beta Pruning]].

## What Kind of "Game" Are We Talking About?

In AI, "game" has a specific meaning. We're not talking about games with randomness, hidden information, or multiple teams. The classic AI game is a:

- **2-Player:** Just you and one opponent (e.g., Chess, Tic-Tac-Toe).
    
- **Zero-Sum:** Your win is your opponent's loss, and vice-versa. There's a fixed amount of "utility" (like +1 for a win, -1 for a loss), and you're fighting over it.
    
- **Discrete & Finite:** There's a limited, countable number of states and moves.
    
- **Deterministic:** There's no luck involved (no dice rolls, no card shuffling).
    
- **Perfect Information:** Both players can see the entire game state. Nothing is hidden (unlike in Poker or Scrabble, where you can't see the opponent's hand/tiles).
    

## Formalizing the Game

To solve a game, we first have to represent it. We use a **Game Tree**.

- **States (**$S$**):** The set of all possible board configurations (including whose turn it is).
    
- **Initial State (**$I$**):** The board at the start of the game.
    
- **Successors (Succs):** A function that takes a state and returns all possible _next_ states (i.e., all legal moves from the current state).
    
- **Terminal States (**$T$**):** The set of states where the game is over (e.g., win, lose, draw).
    
- **Utility Function (**$V$**):** A function that maps a _terminal state_ to a number. By convention, this number is the value _for Player A (our AI)_.
    
    - Example: In Tic-Tac-Toe, $V(s)$ could be:
        
        - `+1` if Player A (MAX) wins.
            
        - `-1` if Player B (MIN) wins.
            
        - `0` for a draw.
            

## The Minimax Algorithm

If we have this game tree, how do we find the best move? We use **Minimax**.

The core idea is to assume your opponent will _always_ play optimally to defeat you.

- We call our AI the **MAX** player, because its goal is to **maximize** the final utility.
    
- We call the opponent the **MIN** player, because their goal is to **minimize** the final utility.
    

The algorithm works by "backing up" values from the terminal states (the leaves of the tree) all the way to the root.

1. **Utility:** At each terminal state (leaf node), apply the utility function $V(s)$.
    
2. **MIN Nodes:** At a MIN node (opponent's turn), it will choose the move that leads to the state with the **minimum** value. So, the value of a MIN node is the `min()` of all its children's values.
    
3. **MAX Nodes:** At a MAX node (our turn), we will choose the move that leads to the state with the **maximum** value. So, the value of a MAX node is the `max()` of all its children's values.
    

You start at the bottom and propagate the values up: `max()`, then `min()`, then `max()`, all the way to the top. The final value at the root is the "minimax value" of the game—the best-achievable outcome for MAX, assuming MIN plays perfectly.

### Minimax Pseudocode

Here's how you'd implement this recursively (using Depth-First Search).

```
/* * This function is called by the AI to decide its move.
 * It returns the *action* that leads to the best outcome.
 */
function MINIMAX-DECISION(state) returns an action
    // We want the action 'a' that maximizes the value of the *next* state,
    // which will be evaluated by MIN.
    return the action 'a' in SUCCESSORS(state) that maximizes MIN-VALUE(RESULT(state, a))

/* * Calculates the best (maximum) utility for the MAX player
 */
function MAX-VALUE(state) returns a utility value
    if TERMINAL-TEST(state) then return UTILITY(state)
    
    v = -∞  // Initialize to negative infinity
    for each action 'a' in SUCCESSORS(state) do
        v = MAX(v, MIN-VALUE(RESULT(state, a)))
    return v

/* * Calculates the best (minimum) utility for the MIN player
 */
function MIN-VALUE(state) returns a utility value
    if TERMINAL-TEST(state) then return UTILITY(state)
    
    v = +∞  // Initialize to positive infinity
    for each action 'a' in SUCCESSORS(state) do
        v = MAX(v, MAX-VALUE(RESULT(state, a)))
    return v
```

## The Problem: It's Too Slow!

Minimax performs a _complete_ depth-first search of the game tree.

- If the branching factor (avg. moves) is $b$ and the depth is $m$, the time complexity is $O(b^m)$.
    
- For Chess: $b \approx 35$, $m \approx 100$. This is... not feasible.
    
- This is why we can't solve Chess, only "search" a few moves deep.
    

This leads us to two things:

1. **Depth-Bounded Search:** We stop the search after a certain depth (e.g., 8 moves).
    
2. **Evaluation Function:** Since we're not reaching a _terminal state_, we can't use the `UTILITY` function. Instead, we use an `EVAL` function that _estimates_ the utility of a non-terminal state (e.g., based on material advantage in Chess).
    

But even with a depth limit, $O(b^m)$ is too slow. We need a way to search _smarter_.

**Next up:** The optimization that makes Minimax practical.

[[Game Playing - Alpha-Beta Pruning]]