> **Sources:**
> 
> - `6. decision-trees-discussion nidhi.pdf` (Slides 7-13)
>     


The basic [[The ID3 Algorithm|ID3 algorithm]] assumes all attributes are discrete, Boolean, and _present_. Real-world data is almost never this clean. Here are the "tips and tricks" for handling messy data.

## 1. Handling Non-Boolean (Continuous) Attributes

- **Problem:** What if an attribute is `Temperature = 85.2`? We can't make a branch for every possible number.
    
- **Solution (Discretization):** We create a new, _Boolean_ attribute by picking a **threshold**.
    
    1. Sort all the unique values for `Temperature` in the training set (e.g., 60, 70, 72, 80, 90).
        
    2. Identify candidate split points (e.g., the midpoints: 65, 71, 76, 85).
        
    3. For each candidate threshold `T` (e.g., `T=71`), calculate the Information Gain of the new Boolean attribute `Temperature > 71?`.
        
    4. Choose the threshold `T` that gives the **maximum Information Gain**.
        
    5. This new Boolean attribute (`Temperature > 71?`) is then treated like any other attribute in the ID3 algorithm.
        

## 2. Handling Non-Boolean (Multi-Valued) Attributes

- **Problem:** What about an attribute like `Type = {French, Italian, Thai, Burger}`?
    
- **Solution 1 (Multi-way Split):** This is what we did in the "Play Tennis" example with `Outlook = {Sunny, Overcast, Rain}`. We create one branch for each value.
    
    - **Problem:** This method _biases_ the Information Gain heuristic. An attribute with many values (e.g., `CustomerID`) will have a very high information gain _just because_ it splits the data into tiny, pure sets (often with only one example each). This leads to overfitting.
        
- **Solution 2 (Binary Splits):** Convert the attribute into a set of Boolean attributes.
    
    - e.g., `IsTypeFrench?`, `IsTypeItalian?`, etc.
        
    - Or, you can test groupings: `Type \in {French, Italian}?`
        
    - This is more robust and avoids the bias of multi-way splits.
        

## 3. Handling Missing Feature Values

- **Problem:** An example is missing a value (e.g., `Day 8, Humidity = ???`). How do we handle this?
    

### At Training Time (when building the tree):

- **Solution 1 (Most Common Value):** Replace `???` with the most common value for `Humidity` from the _entire_ training set (e.g., "High").
    
- **Solution 2 (Most Common Value** _**by Class**_**):** A bit smarter. Look at the example's label (e.g., "No"). Replace `???` with the most common `Humidity` value _for all "No" examples_ (e.g., "High").
    
- **Solution 3 (Fractional Counts):** The most robust way. Don't pick one value. Instead, "split" the example probabilistically.
    
    - If 5/14 examples are "Sunny" and 9/14 are "Rainy", send 5/14ths of this example down the "Sunny" branch and 9/14ths down the "Rainy" branch when calculating gain.
        

### At Test Time (when classifying a new example):

- **Problem:** A new example comes in with `Humidity = ???`. We can't send it down a branch.
    
- **Solution:** Use the same methods as in training.
    
    - e.g., Assign the _most common value_ ("High") and proceed down that one path.
        
    - Or, probabilistically: send the example down _all_ paths, but weight the results. If 70% of training data had "High" humidity and 30% had "Normal", send it down both. If the "High" path gives "No" and the "Normal" path gives "Yes", the final answer is a weighted average (e.g., 70% "No", 30% "Yes").
        

### Check Your Understanding

1. How do you choose the _best_ threshold for a continuous attribute like `Temperature`?
    
2. What is the main problem with using Information Gain on attributes with many unique values (like `EmployeeID`)?
    
3. An example is missing its `Wind` value. Its label is "PlayTennis=Yes". In the training set, "Yes" examples have `Wind=Weak` 6 times and `Wind=Strong` 3 times. Using "Most Common Value by Class", what value would you fill in?