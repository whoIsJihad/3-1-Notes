> **Sources:**
> 
> - `8. Learning-Theory-2-UT-GN.pdf` (Slides 40-44)
>     

# Online vs. Batch Learning

The learning _model_—how the agent receives and processes data—is a fundamental design choice. The two main models are Batch and Online.

## 1. Batch Learning (PAC Model)

- **Data Model:** The learner is given a _full set_ (a "batch") of training examples $S$, all at once.
    
- **Distribution:** Assumes all examples in $S$ are drawn **i.i.d.** (independent and identically distributed) from a fixed, unknown distribution $D$.
    
- **Learning Process:**
    
    1. The algorithm trains on the _entire_ set $S$.
        
    2. It produces a _single, final_ hypothesis $h$.
        
    3. This $h$ is then "deployed to the wild" to make predictions on new data (which is also assumed to be from $D$).
        
- **Goal:** To find a hypothesis $h$ that has a low **True Error** $err_D(h)$.
    
- **Theory:** This is the model used by [[PAC Learning (Probably Approximately Correct)]].
    

## 2. Online Learning (Mistake-Bound Model)

- **Data Model:** The learner receives data _one example at a time_, in a sequence.
    
- **Distribution:** Makes **no assumptions** about the distribution or order of examples. The examples could be chosen by an adversary trying to make the learner fail.
    
- **Learning Process:** This is a continuous loop:
    
    1. The learner sees a single example $x_t$.
        
    2. The learner _makes a prediction_ $\hat{y}_t$ using its _current_ hypothesis $h_t$.
        
    3. The learner is shown the _true label_ $y_t$.
        
    4. If the prediction was wrong ($\hat{y}_t \neq y_t$), the learner _makes a mistake_ and _updates_ its hypothesis to $h_{t+1}$.
        
    5. If the prediction was correct, the learner does nothing.
        
- **Goal:** To bound the _total number of mistakes_ the learner will ever make in its lifetime.
    
- **Theory:** This is the model used by [[Mistake Bound Learning]].
    

## Summary of Differences

|Feature|Batch Learning (PAC)|Online Learning (Mistake-Bound)|
|---|---|---|
|**Data Presentation**|Full "batch" $S$ given at once.|One example at a time, in a sequence.|
|**Data Distribution**|**Assumes i.i.d.** from a fixed $D$.|**No assumptions.** Can be adversarial.|
|**Learning Process**|Trains once on $S$, outputs one $h$.|Learns in trials. Updates $h$ on mistakes.|
|**Primary Goal**|Low **True Error** $err_D(h)$ on new data.|Low **Total Number of Mistakes** over time.|

### Check YourUnderstanding

1. If you are training a spam filter that must update every time you mark an email as "spam," which learning model are you using?
    
2. Why is the i.i.d. assumption so important for Batch (PAC) learning?
    
3. Which model, Online or Batch, makes a stronger assumption about the data?