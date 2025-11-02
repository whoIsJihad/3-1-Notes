# Four Approaches to AI (Acting and Thinking)

AI research can be broadly classified into four goals, which focus either on internal thought processes or external behavior, and whether they model humans or an ideal standard of rationality.

|Focus|Thinking (Internal)|Acting (External)|
|---|---|---|
|**Human Models**|**1. Thinking Humanly (Cognitive Modeling)**|**2. Acting Humanly (Turing Test)**|
|**Ideal/Rational Models**|**3. Thinking Rationally (Laws of Thought)**|**4. Acting Rationally (Rational Agent)**|

### 1. Thinking Humanly (Cognitive Science)

- **Goal:** To understand how the human mind works (reverse-engineering it) by comparing computer models to human experimental data (e.g., how people solve problems, remember, or predict).
    
- **Limitation:** Human behavior is not always rational (e.g., insurance decisions). The "hardware" (brain) is fundamentally different from a computer program.
    

### 2. Acting Humanly (The Turing Test)

- **Concept:** Proposed by **Alan Turing** in 1950 (The Imitation Game). If a human interrogator cannot distinguish between a machine and a human through text-based conversation, the machine is considered intelligent.
    
- **Requirements for Success:** An AI system attempting this needs capabilities in:
    
    - Natural Language Processing (NLP)
        
    - Knowledge Representation
        
    - Automated Reasoning
        
    - Machine Learning
        

### 3. Thinking Rationally (Laws of Thought)

- **Concept:** Using logic to represent facts about the world and employing logical inference (like a theorem-prover) as the basis for reasoning.
    
- **Limitation:** Pure logic cannot easily account for **uncertainty** in the world (e.g., in vision or speech systems), nor can it easily represent goals, costs, and utilities required for real-world decision-making.
    

### 4. Acting Rationally (The Rational Agent)

- **Concept:** The modern focus of AI. An **agent** is anything that perceives its environment and acts upon it. A rational agent selects the action that maximizes its **utility** (the gain to the agent) or **expected utility** if there is uncertainty.
    
- **Emphasis:** **Autonomous agents** that behave rationally, on average over time, within their computational limitations (**bounded rationality**).
    

_The Rational Agent view is the primary focus of modern AI (the "engineering" approach). This approach requires key capabilities which are detailed here: [[06 - Components of Intelligence (Perception, Reasoning, Learning)]]_