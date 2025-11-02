### ✅ Page 1 Summary

This page just gives the **topic** of the presentation:

- It’s about **Operating Systems**
    
- More specifically, **Files and Directories**
    

Nothing to explain here—just the title slide.

---

### ✅ Page 2 Concepts Breakdown

#### What is a File?

- A **file** is just a **linear array of bytes**.
    
- It doesn’t care about meaning—could be text, image, code—OS treats everything as bytes.
    
- Each file has a **low-level name** called an **inode number** (unique identity inside the file system).
    

✅ So: **Human sees filename** like `report.txt`,  
OS sees **inode number** like `inode 42`.

---

#### What is a Directory?

- A **directory is also a file**.
    
- It **maps human-readable names** → **inode numbers**.
    
- Contains a **list of pairs**:
    
    ```
    <filename, inode number>
    ```
    

✅ So directories are basically **lookup tables** for files.

---

### ✅ Key Ideas So Far

|Concept|Meaning|
|---|---|
|File|Just a sequence of bytes|
|Inode Number|Unique ID of a file in disk|
|Directory|File that maps name → inode|

---
