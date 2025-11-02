> **Sources:**
> 
> - `2. Learning-1.pptx.pdf` (Slides 9-11)
>     
> - `2.1 Learning from examples note nidhi.pdf` (Page 11)
>     

# Supervised Learning (Introduction)

**Supervised Learning** is the task of learning a function from labeled training data.

## Formal Task

We are given a training set of $N$ example input-output pairs:

$$D = \{ (x_1, y_1), (x_2, y_2), ..., (x_N, y_N) \}$$

We assume that there is an **unknown true function** $f$ that generated these labels, i.e., $y_j = f(x_j)$ (plus or minus some noise).

**Goal:** Discover a **hypothesis function** $h$ that "approximates" the true function $f$ as closely as possible.

- This function $h$ is also called the _approximator_, _predictor_, or _model_.
    
- We want $h$ to be a good approximation not just for the data we've seen, but also for _new, unseen data_. This is called **generalization**.
    

## Problem Types

Supervised learning is typically broken into two main problem types based on the _output_ $y$:

1. **Classification:**
    
    - The output $y$ belongs to a **finite, categorical set**.
        
    - The inputs $x$ are often called **features** (or attributes), and the output $y$ is called a **class** (or label).
        
    - **Examples:**
        
        - `DayType = {rainy, cloudy, sunny}`
            
        - `Spam = {True, False}`
            
        - `Digit = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}`
            
2. **Regression:**
    
    - The output $y$ is a **continuous numerical value**.
        
    - **Examples:**
        
        - `Temperature = 23.5`
            
        - `StockPrice = 150.75`
            
        - `TrafficSpeed = 45.2 km/h`
            

The set of all possible functions $h$ that our algorithm is allowed to search through is called the [[Hypothesis Space]].

### Check Your Understanding

1. What is the "true function $f$"? Can we ever know it perfectly?
    
2. Is predicting the _letter grade_ (A, B, C, D, F) for a student a classification or regression task? What about predicting their _exact percentage score_ (e.g., 87.5%)?
    
3. What is the ultimate goal of learning $h$? Is it to be 100% correct on the training data?