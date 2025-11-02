# Game Playing: Alpha-Beta Pruning

Welcome to the deep dive on **Alpha-Beta (**$\alpha-\beta$**) Pruning**! In the [[Game Playing - The Minimax Algorithm]] note, we established the Minimax algorithm, which finds the optimal move by assuming the opponent also plays optimally.

The big problem? Minimax searches the _entire_ game tree (to a given depth), which has a time complexity of $O(b^m)$. This is just too slow.

Alpha-Beta Pruning is an optimization that _dramatically_ speeds up this search by "pruning" away large sections of the tree that we can prove are irrelevant.

**The best part:** $\alpha-\beta$ **pruning is guaranteed to return the exact same value as Minimax. It's not an approximation.**

## The Core Idea: Don't Explore Bad Branches

Imagine you're the **MAX** player. You're exploring your first move, `A1`. You go down that branch and find that, after MIN plays optimally, the outcome is a score of **+10**. This is now your best-so-far option.

Now, you start exploring your second move, `A2`. This leads to a MIN node.

- MIN explores its first reply, `B1`, which leads to a score of **+5**.
    
- MIN (being MIN) provisionally says, "Okay, my best outcome so far is +5."
    
- MIN then explores its second reply, `B2`, which leads to a score of **+2**.
    
- MIN says, "Great! +2 is even better (lower) for me than +5."
    
- MIN then explores its third reply, `B3`, which leads to a score of **-100**.
    
- MIN says, "Excellent! -100 is my best option so far."
    

At this point, you, the **MAX** player, can **stop** MIN from exploring any more moves (like `B4`, `B5`, etc.).

**Why?** Because you know that if you play move `A2`, MIN will _at best_ force an outcome of -100 (and maybe even worse if it finds a better move). But you _already_ have move `A1` which guarantees you a +10. You will _never_ choose move `A2`.

It doesn't matter what MIN finds in `B4` or `B5`. That entire branch of the tree is now irrelevant. You can **prune** it.

## Defining Alpha ($\alpha$) and Beta ($\beta$)

Alpha-Beta Pruning formalizes this by keeping track of two values as it traverses the tree:

- $\alpha$ **(Alpha): The "MAX" value.**
    
    - This is the **best** (highest) value that the **MAX** player has found _so far_ on the path from the root.
        
    - This is the _worst-case-scenario_ for MAX. MAX is guaranteed to get _at least_ $\alpha$.
        
    - $\alpha$ starts at $-\infty$. It can only ever increase.
        
- $\beta$ **(Beta): The "MIN" value.**
    
    - This is the **best** (lowest) value that the **MIN** player has found _so far_ on the path from the root.
        
    - This is the _worst-case-scenario_ for MIN. MIN is guaranteed to get _at most_ $\beta$.
        
    - $\beta$ starts at $+\infty$. It can only ever decrease.
        

### The Pruning Conditions

Pruning happens when these two values "cross over." The search at any node is stopped as soon as $\alpha \ge \beta$.

1. **Alpha Pruning (in a MAX node):**
    
    - A MAX node is exploring its children. Each child (a MIN node) returns a value.
        
    - As MAX gets these values, it updates its own value `v` and its `α` (since `α` is the best-so-far for MAX).
        
    - If at any point `v` becomes greater than or equal to `β` (the best value MIN can get _higher up_ the tree), this MAX node can **stop** exploring.
        
    - **Why?** The MIN player _above_ this node will _never_ let the game come here, because this node guarantees a _worse_ (higher) outcome for MIN than what MIN already has ($\beta$).
        
2. **Beta Pruning (in a MIN node):**
    
    - A MIN node is exploring its children (MAX nodes).
        
    - As MIN gets values, it updates its own value `v` and its `β` (since `β` is the best-so-far for MIN).
        
    - If at any point `v` becomes less than or equal to `α` (the best value MAX can get _higher up_ the tree), this MIN node can **stop** exploring.
        
    - **Why?** The MAX player _above_ this node will _never_ choose this move, because this node guarantees a _worse_ (lower) outcome for MAX than what MAX already has ($\alpha$).
        

## Why Move Ordering is CRITICAL

Alpha-Beta Pruning works, but its _efficiency_ depends entirely on **move ordering**.

- **Worst Case:** If you explore the _worst_ moves first, $\alpha$ and $\beta$ will barely change. You'll end up pruning nothing and still have an $O(b^m)$ complexity, just like regular Minimax.
    
- **Best Case ("Perfect Ordering"):** If a heuristic or prior knowledge lets you explore the _best_ move first from every node, you will get the _maximum_ number of prunes.
    
- **Complexity with Perfect Ordering:** The time complexity drops to $O(b^{m/2})$.
    

This is a _massive_ improvement. It means that in the same amount of time, you can search **twice as deep** as you could with regular Minimax. This is, quite literally, the difference between a terrible chess AI and a pretty good one.

## Practical Problems (The "Gotchas")

Alpha-Beta Pruning is great, but it's not magic. It's still limited by the _depth_ of its search, which leads to two famous problems:

1. **Non-Quiescence:** Your evaluation function might be wrong if you stop searching in the middle of a "hot" sequence (like a queen capture). Your AI might stop at depth 8, think it's up by 9 points (a queen), but fail to see that at depth 9, the opponent recaptures.
    
    - **Solution:** Use a **Quiescence Search**—if the state is "non-quiescent" (e.g., a capture is in progress), search a few extra plys deep until the board "calms down."
        
2. **The Horizon Effect:** A _bad_ event (like losing a queen) is inevitable. The AI can't stop it. But by making a series of useless "delaying" moves, it can "push" the bad event _just past_ its maximum search depth (its "horizon"). It _thinks_ it avoided the disaster, but really it just delayed it and likely made its position worse.