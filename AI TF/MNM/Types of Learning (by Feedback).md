> **Sources:**
> 
> - `2. Learning-1.pptx.pdf` (Slides 5-8)
>     
> - `2.1 Learning from examples note nidhi.pdf` (Pages 5, 7-10)
>     

# Types of Learning (by Feedback)

Learning paradigms are most often categorized by the type of feedback the agent receives from its observations.

### 1. Supervised Learning

- **Feedback:** Explicit input-output pairs (i.e., **labeled data**). The agent is given the "right answer" for each example.
    
- **Task:** Learn a function $h$ that maps inputs $x$ to outputs $y$.
    
- **Example:** Given 1000 traffic reports (inputs) that are _already labeled_ as "Good" or "Bad" (outputs), learn to predict the label for a new, unseen report.
    
- This is the focus of [[Supervised Learning (Introduction)]].
    

### 2. Unsupervised Learning

- **Feedback:** **No explicit feedback** or labels. The agent only gets the inputs.
    
- **Task:** Learn patterns, structure, or "clusters" in the input data.
    
- **Example:** Given 1000 _unlabeled_ traffic reports, the agent might discover on its own that the data points seem to fall into two distinct groups, which we (as humans) might later identify as "Good" and "Bad" days.
    
- Also known as **clustering**.
    

### 3. Reinforcement Learning

- **Feedback:** **Rewards or punishments** (a scalar "reinforcement" signal) for actions taken. The feedback is often delayed.
    
- **Task:** Learn a "policy" (a strategy of which action to take in which state) to maximize a long-term cumulative reward.
    
- **Example:** A taxi-driving agent tries different routes. At the end of a trip, it gets a "tip" (reward). It learns to prefer actions (routes) that lead to higher tips over time.
    
- **Key Difference from Supervised:** In Supervised, you're told "the correct answer is B". In Reinforcement, you're told "you did action C, and that was -5 points." You're not told what the _best_ action was, only the value of the one you tried. (From `handwritten_notes.pdf`, Page 10)
    

### Other Types

- **[[Self-Supervised Learning]]:** A type of learning where the feedback is **internal**. The agent creates its own labels from the data.
    
    - **Example:** Large Language Models (LLMs). The agent takes a sentence, masks out a word, and tries to predict the masked word. The masked word _is_ the label, and it was generated from the data itself. (From `handwritten_notes.pdf`, Page 7)
        
- ** [[Semi-Supervised Learning (SSL)]]**: A mix of supervised and unsupervised. The agent receives a _small_ amount of labeled data and a _large_ amount of unlabeled data. (From `handwritten_notes.pdf`, Page 7)
    

### Check Your Understanding

1. Explain the key difference between the feedback in Supervised Learning and Reinforcement Learning.
    
2. Could you use Unsupervised Learning to predict a student's grade? Why or why not?
    
3. How is Self-Supervised Learning (like in LLMs) different from standard Supervised Learning?