# Shattering: A Deeper Explanation

_Source: `14. Learning-Theory-8-PAC-VC.pdf` (Pages 21-22, 33, 37)_ _Related: [[Computational Learning Theory (CLT)]], [[Infinite Hypothesis Spaces]], [[VC Dimension (VCD)]]_

The concept of "shattering" is the most important tool we have to measure the "power" or "expressiveness" of a [[Infinite Hypothesis Spaces|hypothesis space H that is infinite]].

The main question it answers is: **"How complex is my set of classifiers?"**

A simple $H$ (like a 1D interval) can't classify many patterns, while a complex $H$ (like a neural network) can. Shattering gives us a formal number for this.

## The Core Idea: An Adversarial Game

Think of "shattering" as a game you play against an adversary.

- **Your** $H$: This is your "family of functions" or "set of all possible classifiers" you are using. For example, $H$ could be "the set of all possible straight lines in 2D."
    
- **The Game**:
    
    1. You pick a number of points, $k$. Let's say $k=3$.
        
    2. You place $k=3$ points _anywhere you want_ on the plane.
        
    3. Your adversary's turn: They look at your 3 points and try to find an "impossible" labeling. They can choose _any_ of the $2^k$ (so $2^3 = 8$) possible ways to label those points `+` or `-`.
        
    4. Your turn: You look at the adversary's labeling. You win if you can find _at least one_ function $h$ in your set $H$ (at least one straight line) that perfectly separates the points _exactly as the adversary labeled them_.
        
- **Shattering**: If you can win against _every single labeling_ your adversary throws at you (all 8 labelings for $k=3$), then you can say **your** $H$ **shatters** $k=3$ **points**.
    

If the adversary can find just _one_ labeling that _none_ of your functions in $H$ can match, you lose. Your $H$ **does not** shatter $k$ points.

## Detailed Examples

Let's trace this game.

### Example 1: $H$ = 1D Intervals `[0, a)`

Your classifiers can only label points from 0 up to some value `a` as positive (`+`). Everything else is negative (`-`).

**Game 1:** $k=1$ **point**

1. You place 1 point, $p_1$ (e.g., at $x=5$).
    
2. Adversary has $2^1 = 2$ labelings:
    
    - **Labeling A: `{p_1 = +}`**: You win. Pick $a=6$. Your function `[0, 6)` labels $p_1$ as `+`.
        
    - **Labeling B: `{p_1 = -}`**: You win. Pick $a=4$. Your function `[0, 4)` labels $p_1$ as `-`.
        
3. **Result**: You can match all $2^1$ labelings. $H$ **shatters 1 point.**
    

**Game 2:** $k=2$ **points**

1. You place 2 points, $p_1$ and $p_2$ (e.g., at $x=5$ and $x=8$).
    
2. Adversary has $2^2 = 4$ labelings:
    
    - **Labeling A: `{p_1 = +, p_2 = +}`**: You win. Pick $a=9$. `[0, 9)` covers both.
        
    - **Labeling B: `{p_1 = -, p_2 = -}`**: You win. Pick $a=4$. `[0, 4)` covers neither.
        
    - **Labeling C: `{p_1 = -, p_2 = +}`**: You win. Pick $a=7$. `[0, 7)` covers $p_2$ but not $p_1$.
        
    - **Labeling D: `{p_1 = +, p_2 = -}`**: **You lose!** This is impossible. To make $p_1$ positive, `a` must be $> 5$. But if $a > 5$, $p_2$ (which is at 8) _must_ also be positive. You have no function $h \in H$ that can create this labeling.
        
3. **Result**: You failed on one labeling. $H$ **does not shatter 2 points.**
    

### Example 2: $H$ = 2D Linear Classifiers (Lines)

**Game 1 & 2:** $k=1$**,** $k=2$ **points**

- It's easy to see $H$ can shatter 1 point and 2 points. You can always draw a line to match any of the 2 or 4 labelings.
    

**Game 3:** $k=3$ **points**

1. You place 3 points. **Crucially, you get to choose the placement.** You are smart, so you **do not** put them in a straight line. You place them in a triangle.
    
2. Adversary has $2^3 = 8$ labelings. Let's check them:
    
    - `{+, +, +}` or `{-, -, -}`: Easy. Put all 3 points on one side of a line.
        
    - `{+, -, -}`: Easy. Draw a line that separates the one `+` from the two `-`.
        
    - `{+, +, -}`: Easy. Draw a line that separates the two `+` from the one `-`.
        
    - (All 8 combinations are possible by just "cutting off" one vertex or one edge of the triangle).
        
3. **Result**: Because you found _one configuration_ (a triangle) where you can match all 8 labelings, $H$ **shatters 3 points.**
    

_Side Note_: What if you had placed 3 points in a line? Then you _would_ lose. The adversary could pick the labeling `{+, -, +}`. You can't draw a single line to get this. But that's okay! The rule is "if there _exists_ a set of $k$ points you can shatter," not "you must be able to shatter _every_ set of $k$ points."

**Game 4:** $k=4$ **points**

1. You place 4 points. Now, the burden of proof is on the adversary. You must show that _no matter where you place the 4 points_, the adversary can _always_ find a labeling that stumps you.
    
2. **Case A: You place points as a "convex hull" (like a square).**
    
    - Adversary chooses the **XOR labeling**: `(+ - + -)` on the corners.
        
    - **You lose.** It is impossible to draw one straight line to separate these.
        
3. **Case B: You place 3 points as a triangle and 1 point in the middle.**
    
    - Adversary chooses: `{+, +, +}` for the outer triangle and `{-}` for the inner point.
        
    - **You lose.** Any line that encloses the 3 `+` points _must_ also enclose the `-` point.
        
4. **Result**: No matter how you place 4 points, there is _always_ at least one labeling that a line cannot create. $H$ **does not shatter 4 points.**
    

## What This All Means

- "Shattering" is the test for expressiveness.
    
- The **VC Dimension** is simply the _count_ of the largest number of points your $H$ _can_ shatter.
    
- For 1D intervals `[0, a)`, the largest set it can shatter is 1. So, $VC(H) = 1$.
    
- For 2D lines, the largest set it can shatter is 3. So, $VC(H) = 3$.
    

This $VC(H)$ value is the number that replaces $ln(|H|)$ in our [[Sample Complexity with VC Dimension|sample complexity bounds]], allowing us to finally analyze infinite hypothesis spaces.

### ❓ Review Questions

1. In the "adversarial game," who wins if the adversary finds just one "impossible" labeling for a set of $k$ points?
    
2. To prove $VC(H) = d$, you have to show two things. What are they? (Hint: one is about $d$ points, one is about $d+1$ points).
    
3. Based on the game, what do you think the VC dimension of $H$ = "all circles centered at the origin" would be? How many points can it shatter?