
---


**Tags:** #ai #ml #learning #semi-supervised

Semi-Supervised Learning is a **bridge between supervised and unsupervised learning**. It is used when:

- You have **a small labeled dataset** (expensive to obtain).
    
- You have **a large unlabeled dataset** (cheap and abundant).
    
- Goal: Build a model that **learns better than using only the labeled data**.
    

---

## 1. Key Idea

- **Labeled data:** provides a rough guide for the model.
    
- **Unlabeled data:** reveals the structure of the input space (clusters, patterns).
    
- **Assumption:** Similar data points are likely to have the same label (cluster/smoothness assumption).
    

**Example:**

- Labeled: 10 cat/dog images
    
- Unlabeled: 500 more images
    
- SSL uses the 10 labeled images to start learning, then predicts labels on the 500 unlabeled images, gradually improving itself.
    

---

## 2. Main Mechanism — Self-Training / Pseudo-Labeling

1. **Train initial model** on small labeled set.
    
2. **Predict labels** for unlabeled data.
    
3. **Select high-confidence predictions** (e.g., probability > 90%).
    
4. **Add these pseudo-labeled examples** to the labeled set.
    
5. **Retrain model** on expanded labeled set.
    
6. Repeat until the model reaches satisfactory performance or most data is labeled.
    

**Intuition:** The model “teaches itself” using the unlabeled data, while the initial labeled data provides guidance.

---

## 3. Handling Risks

- **Error propagation:** Wrong pseudo-labels can degrade performance.
    
- **Mitigation:** Only use **high-confidence predictions** to expand the labeled set.
    
- Advanced methods:
    
    - **Co-Training:** Two models with different “views” label each other’s data.
        
    - **Graph-Based Label Propagation:** Represent data as a graph; labels spread from labeled to unlabeled nodes along similarity edges.
        

---

## 4. Assumptions Behind SSL

1. **Smoothness Assumption:** Close points in feature space likely share the same label.
    
2. **Cluster Assumption:** Data forms clusters; decision boundaries should avoid high-density regions.
    
3. **Manifold Assumption:** High-dimensional data lies on a lower-dimensional manifold; labels vary smoothly along it.
    

---

## 5. Real-World Examples

|Domain|Labeled Data|Unlabeled Data|SSL Use Case|
|---|---|---|---|
|Medical Imaging|100 labeled X-rays|5000 unlabeled X-rays|Detect diseases|
|Spam Detection|200 labeled emails|50,000 unlabeled emails|Build spam filters efficiently|
|Speech Recognition|1 hour transcribed audio|100 hours raw audio|Train automatic speech recognition|
|Web Page Classification|100 labeled pages|10,000 unlabeled pages|Classify topic/category|

---

## 6. Summary

- SSL = “learn from a few teachers (labeled data) + observing the crowd (unlabeled data).”
    
- Key benefit: Achieves **better accuracy than small labeled set alone**.
    
- Key risk: Mislabeling unlabeled data can propagate errors → requires confidence-based selection or advanced methods.
    
- **Big takeaway:** Semi-Supervised Learning is **practical when labeled data is scarce but unlabeled data is abundant**, using structure in the data to improve learning efficiently.
    
