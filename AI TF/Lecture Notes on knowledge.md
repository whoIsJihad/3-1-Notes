# CSE 317: Lecture Notes on Knowledge

Here's a breakdown of the topics from your lecture slides (starting from Page 6).

### Course Outline (Part B) (Page 6)

- **Knowledge**
    
- Uncertainty
    
- Learning
    
- Natural Language Processing (NLP)
    
- Computer Vision (CV)
    
- Planning
    
- Recap
    

## 1. What are Knowledge-Based Agents? (Page 8)

The main idea here is to build AI agents that can _reason_.

To do this, they need some kind of internal representation of "knowledge." Think of it as a database of facts and rules.

We call this database a **Knowledge Base (KB)**.

These agents can then use this KB to operate, reason, and make decisions. We need a precise, mathematical way to handle this process.

### A Quick Reasoning Example (Page 9)

Let's say our Knowledge Base (KB) has these rules:

1. "If it didn't rain, Harry visited Hagrid today." ($\neg P \rightarrow Q$)
    
2. "Harry visited Hagrid or Dumbledore today, but not both." ($Q \lor R$ and $\neg(Q \land R)$)
    
3. "Harry visited Dumbledore today." ($R$)
    

From these facts, we can _reason_ or _infer_ new knowledge:

- From (2) and (3), we know Harry did _not_ visit Hagrid. ($\neg Q$)
    
- From (1), if $\neg Q$ is true, then $P$ must be true.
    
- **Conclusion:** It rained today. ($P$)
    

This new fact ($P$) was "hidden" in our knowledge base, and we used reasoning to find it.

## 2. Let's Talk About Logic (Page 10)

Logic is the formal system we use to represent and reason with knowledge.

- **Sentence:** A single assertion about the world. (Page 11)
    
    - _Example:_ "It is raining."
        

### Propositional Logic (Page 12)

This is the simplest form of logic.

- **Proposition Symbols:** These are symbols (like $P$, $Q$, $R$) that stand for a single, complete proposition. (Page 13)
    
    - $P$: "It is raining."
        
    - $Q$: "Abhishek is present."
        
- **Logical Connectives:** These let us build complex sentences from simple ones. (Page 14)
    
    - **Not (**$\neg$**):** Flips the truth value.
        
        - $\neg P$: "It is _not_ raining."
            
        - (See truth table on Page 15)
            
    - **And (**$\land$**):** True only if _both_ sides are true.
        
        - $P \land Q$: "It is raining _and_ Abhishek is present."
            
        - (See truth table on Page 16)
            
    - **Or (**$\lor$**):** True if _at least one_ side is true.
        
        - $P \lor Q$: "It is raining _or_ Abhishek is present."
            
        - (See truth table on Page 17)
            
    - **Implication (**$\rightarrow$**):** "If P, then Q."
        
        - This is only false in one case: when $P$ is true but $Q$ is false.
            
        - $P \rightarrow Q$: "If it is raining, then Abhishek is present."
            
        - (See truth table on Page 18)
            
    - **Biconditional (**$\leftrightarrow$**):** "P if and only if Q."
        
        - True only if both sides have the _same_ truth value (both true or both false).
            
        - (See truth table on Page 19)
            

**Note:** Propositional logic is useful, but it can't perfectly represent everything in the real world. (Page 19)

## 3. Models, Knowledge Bases, and Entailment

- **Model:** A "possible world." It's an assignment of a truth value (True/False) to every single proposition symbol. (Page 20)
    
    - _Example:_ If our only symbols are $P$ and $Q$, one possible model is $\{P = \text{true}, Q = \text{false}\}$. (Page 21)
        
- **Knowledge Base (KB):** A set of sentences that our agent "knows" to be true. (Page 22)
    
- **Entailment (**$\models$**):** This is a _crucial_ concept.
    
    > $\alpha \models \beta$ (read as "alpha entails beta")
    
    This means: **In every possible model where sentence** $\alpha$ **is true, sentence** $\beta$ **is** _**also**_ **true.** (Page 23)
    
    If your KB is $\alpha$, and it entails $\beta$, it means $\beta$ is a logical consequence of your KB. It might not be _explicitly_ written in the KB, but it's _implicitly_ true. (Page 24)
    
- **Inference:** The _process_ of deriving new sentences (like $\beta$) from old ones (like $\alpha$). This is the "reasoning" part. (Page 25)
    

## 4. Inference Algorithms: How Do We Prove Things?

The big question is: **Does** $KB \models \alpha$**?** (Does our knowledge base entail this new fact $\alpha$?) (Page 28)

### Method 1: Model Checking (Page 29)

This is the "brute-force" algorithm.

1. Enumerate every single possible model (every combination of True/False for all symbols).
    
2. Check all models where the $KB$ is true.
    
3. In _all_ of those models, check if $\alpha$ is _also_ true.
    
4. If yes, then $KB \models \alpha$.
    
5. If you find even _one_ model where the $KB$ is true but $\alpha$ is false, then the entailment does _not_ hold.
    

(See the example with P, Q, R on Pages 31-33. We find all rows in the truth table where KB is true and check if the query $R$ is also true in those rows.)

### Knowledge Engineering in Practice (Pages 34-43)

This is the process of "engineering" a real-world problem into a formal logic representation.

- **Example: The game "Clue"** (Page 35)
    
    - We can define proposition symbols for every fact, like `Col.Mustard`, `Kitchen`, `Knife`.
        
    - We can then build a KB with rules like `(Mustard \lor Plum \lor Scarlet)` (it was one of them) and `\neg Plum` (a card we hold).
        
- **Example: Logic Puzzles** (Page 41)
    
    - We can solve puzzles (like the Harry Potter houses puzzle) by defining symbols (`GilderoyGryffindor`, `PomonaSlytherin`) and adding the puzzle's rules to our KB.
        

### Method 2: Using Inference Rules (Page 45)

Model checking is slow (it gets exponentially large). A smarter way is to use **Inference Rules**, which are patterns of logic that let us derive new sentences directly.

- **Modus Ponens:** (Page 46-47)
    
    - If you know $A \rightarrow B$ (If A, then B)
        
    - And you know $A$ (A is true)
        
    - You can infer $B$.
        
- **And Elimination:** (Page 48-49)
    
    - If you know $A \land B$ (A and B are true)
        
    - You can infer $A$ (or $B$).
        
- **Double Negation Elimination:** (Page 50-51)
    
    - If you know $\neg(\neg A)$ (It's not true that A is not true)
        
    - You can infer $A$.
        
- **Implication Elimination:** (Page 52-53)
    
    - $A \rightarrow B$ is logically equivalent to $\neg A \lor B$.
        
    - "If it's raining, I'm inside" is the same as "It's not raining, or I'm inside."
        
- **Biconditional Elimination:** (Page 54-55)
    
    - $A \leftrightarrow B$ is equivalent to $(A \rightarrow B) \land (B \rightarrow A)$.
        
- **De Morgan's Law:** (Page 56-59)
    
    - $\neg(A \land B)$ is equivalent to $\neg A \lor \neg B$.
        
    - $\neg(A \lor B)$ is equivalent to $\neg A \land \neg B$.
        
- **Distributive Property:** (Page 60-61)
    
    - $A \land (B \lor C)$ is equivalent to $(A \land B) \lor (A \land C)$.
        
    - $A \lor (B \land C)$ is equivalent to $(A \lor B) \land (A \lor C)$.
        

We can treat inference as a **search problem** (Page 62):

- **Initial State:** Your starting KB.
    
- **Actions:** Apply an inference rule to sentences in your KB.
    
- **Transition Model:** Add the newly inferred sentence to your KB.
    
- **Goal Test:** See if the sentence you're trying to prove is now in your KB.
    

## 5. The Resolution Algorithm (Page 64)

Resolution is a single, powerful inference rule that is _complete_ (it can prove anything that is provable).

It works on sentences in a specific format: **Conjunctive Normal Form (CNF)**.

- **Core Idea:** (Page 65, 69)
    
    > If you have $(P \lor Q)$ And you have $(\neg P \lor R)$ You can resolve them to get $(Q \lor R)$.
    
    You're essentially "canceling out" the $P$ and $\neg P$.
    
- **Clause:** A disjunction of literals (literals are just $P$ or $\neg P$).
    
    - _Example:_ $(P \lor \neg Q \lor R)$ is a clause. (Page 71)
        
- **Conjunctive Normal Form (CNF):** A logical sentence that is a _conjunction_ of _clauses_.
    
    - _Example:_ $(A \lor B) \land (\neg B \lor C) \land (\neg C)$
        
    - This is just a big "AND" of a bunch of "ORs." (Page 72)
        

We can convert _any_ sentence in propositional logic into CNF using the inference rules we learned earlier (like Implication Elimination and De Morgan's Law). (Page 73)

### Inference by Resolution (Page 81)

Here's the algorithm. It's a proof by contradiction.

To prove: $KB \models \alpha$

1. Create a new, temporary KB: $(KB \land \neg\alpha)$.
    
    - (You add the _negation_ of what you want to prove to the KB).
        
2. Convert this entire temporary KB into CNF. You'll have a set of clauses.
    
3. Repeatedly apply the resolution rule to any two clauses that can be resolved.
    
4. Add the new "resolved" clause back into your set.
    
5. **If you ever produce the "empty clause" `()`** (which means `False`), you have found a contradiction!
    
6. This contradiction proves that your assumption $\neg\alpha$ was wrong.
    
7. Therefore, $KB \models \alpha$ must be true.
    

If you can't add any new clauses and you never found the empty clause, then the entailment does not hold. (Page 83)

(See the step-by-step example on Pages 84-94, which proves that $(A \lor B) \land (\neg B \lor C) \land (\neg C)$ entails $A$.)

## 6. First-Order Logic (FOL) (Page 95)

Propositional logic is limited. We can't talk about "all" or "some" things. We need a more expressive logic.

- **Propositional Logic:** `MinervaGryffindor`, `MinervaHufflepuff`... (We need a new symbol for every single fact). (Page 96)
    
- **First-Order Logic:** (Page 97)
    
    - **Constant Symbols:** Stand for objects (e.g., `Minerva`, `Gryffindor`).
        
    - **Predicate Symbols:** Stand for relations or properties (e.g., `Person`, `House`, `BelongsTo`).
        

Now we can write sentences like:

- `Person(Minerva)`
    
- `House(Gryffindor)`
    
- `BelongsTo(Minerva, Gryffindor)` (Page 98)
    

### Quantifiers

This is the most powerful part of FOL.

- **Universal Quantification (**$\forall$**): "For all..."** (Page 100)
    
    > $\forall x. (\text{BelongsTo}(x, \text{Gryffindor}) \rightarrow \neg \text{BelongsTo}(x, \text{Hufflepuff}))$
    
    - _Translation:_ "For all $x$, if $x$ belongs to Gryffindor, then $x$ does not belong to Hufflepuff."
        
- **Existential Quantification (**$\exists$**): "There exists..."** (Page 102)
    
    > $\exists x. (\text{House}(x) \land \text{BelongsTo}(\text{Minerva}, x))$
    
    - _Translation:_ "There exists some $x$ such that $x$ is a House _and_ Minerva belongs to $x$." (i.e., "Minerva belongs to a house.")
        

### FOL, CNF, and Resolution (Pages 104-123)

The great thing is that our **Resolution** algorithm still works for FOL!

The process is just more complex:

1. We still convert all sentences to CNF. This is harder in FOL and involves:
    
    - Eliminating implications ($\rightarrow$)
        
    - Moving negations ($\neg$) inwards
        
    - **Skolemization:** A process to eliminate existential quantifiers ($\exists$) by replacing them with special constants or functions. (Page 105)
        
    - Dropping all universal quantifiers ($\forall$) (since it's all in CNF).
        
2. Once we have a set of clauses (just like before), we can use Resolution to find contradictions.
    

The "Colonel West" problem (Pages 109-115) is a famous example showing how you can translate a real-world story into FOL, convert it to CNF, and use resolution to prove that "Colonel West is a criminal."