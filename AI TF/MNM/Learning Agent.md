> **Sources:**
> 
> - `2. Learning-1.pptx.pdf` (Slides 2-4)
>     
> - `2.1 Learning from examples note nidhi.pdf` (Pages 3-5, 35)
>     

# The Learning Agent

## Definition

An agent is **learning** if it improves its performance on future tasks after making observations about the world.

- Learning is essentially about building or refining an underlying model of the world.
    
- We know an agent is learning if its performance (e.g., scoring a goal, predicting traffic) gets better.
    

## Learning Processes

1. **Inductive Learning (Specific** $\to$ **General):**
    
    - This is the most common form of machine learning.
        
    - The agent learns a general rule or function by observing a set of specific input-output examples.
        
    - **Example:** Observing many days of traffic data (specific examples) to create a general model (rule) that predicts "Good" or "Bad" traffic days. (From `handwritten_notes.pdf`, Page 4)
        
2. **Deductive Learning (General** $\to$ **Specific/Efficient):**
    
    - The agent uses existing general knowledge to deduce new, more efficient rules or specific facts.
        
    - **Example:** If the agent knows "All humans are mortal" ($A \to B$) and "Socrates is a human" ($B \to C$), it can deduce "Socrates is mortal" ($A \to C$). This is reasoning, not learning from new data. (From `handwritten_notes.pdf`, Page 4, 35)
        

## Learning Modes

- **Online Learning:** The agent learns continuously as it receives new data over time. This is common for agents that operate in real-time. (From `Learning-1.pptx.pdf` Slide 3)
    
- **Offline Learning:** The agent is given a complete, pre-observed set of data. It learns "once" from this batch of data and is then deployed with a static model. (From `Learning-1.pptx.pdf` Slide 3)
    

## Components of a Learning Agent

A learning agent isn't just one thing. It has several components, and any of them can be the target of learning:

- **Actions:** Learning which actions are good (e.g., in [[Reinforcement Learning]]).
    
- **Utility Functions:** Learning how "good" a particular state is (e.g., learning a board evaluation function in chess).
    
- **Environments:** Learning the rules of the world (e.g., learning `P(state' | state, action)`).
    
- **Representation:** Learning how to represent knowledge efficiently. (From `Learning-1.pptx.pdf` Slide 4)
    

### Check Your Understanding

1. Explain the core difference between Inductive and Deductive learning using an example.
    
2. A chess-playing AI plays 1 million games against itself and saves the results. It then trains a model on this entire dataset _before_ being released to the public. Is this an example of Online or Offline learning? Why?
    
3. What does it mean for an agent to "learn its utility function"?