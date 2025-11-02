

# **File Descriptors and Offsets (Page 8)**

When a process opens a file, several layers of structures are involved in Linux/Unix:

---

## **1️⃣ File Descriptor (FD) Table (Per Process)**

- Every process has its own **file descriptor table**.
    
- Think of it as a **mapping from small integers (fd)** to **entries in the global open file table (OFT)**.
    
- Example:
    

|fd|Points to OFT Entry|
|---|---|
|0|stdin|
|1|stdout|
|2|stderr|
|3|OFT[0]|

- The **fd** is used by system calls like `read(fd, ...)`, `write(fd, ...)`.
    

---

## **2️⃣ Global Open File Table (OFT, System-wide)**

- Contains entries for **all files currently open by any process**.
    
- Each entry stores:
    
    - Pointer to **inode** (file metadata)
        
    - **Current offset** — position in the file for next read/write
        
    - Reference counts (how many FDs point here)
        
- Example:
    

|OFT Entry|File (inode)|Current Offset|
|---|---|---|
|0|file.txt|0|

- Multiple FDs **from the same or different processes** can point to the same OFT entry if they are **duplicated**, otherwise each `open()` creates a new OFT entry.
    

---

## **3️⃣ Opening the same file twice**

Suppose a process does:

```c
fd1 = open("file.txt", O_RDONLY);
fd2 = open("file.txt", O_RDONLY);
```

- **fd1 → OFT[0]**
    
- **fd2 → OFT[1]**
    
- Both OFT entries point to **the same inode**, but each OFT has **its own offset**.
    

|OFT Entry|File (inode)|Current Offset|
|---|---|---|
|0|file.txt|0|
|1|file.txt|0|

- **Independent offsets** → reading from fd1 **does not affect fd2’s offset**.
    

---

## **4️⃣ Using `lseek()`**

- System call:
    

```c
off_t lseek(int fd, off_t offset, int whence);
```

- Changes the **offset** of the OFT entry **for that fd**.
    

Example trace:

|System Call|Return Code|Current Offset|
|---|---|---|
|`fd = open("file", O_RDONLY)`|3|0|
|`lseek(fd, 200, SEEK_SET)`|200|200|
|`read(fd, buffer, 50)`|50|250|
|`close(fd)`|0|–|

- After `lseek`, the next `read` starts **from the new offset**.
    

---

## **5️⃣ Key Rules**

1. **Each process has its own FD table.**
    
2. **OFT entry stores file inode + current offset.**
    
3. **Multiple opens create multiple OFT entries** (offsets independent).
    
4. **The `read()`/`write()` system calls update the offset in the OFT entry.**
    

---

✅ **Summary (Page 8)**

- Opening a file gives a **fd**, pointing to **OFT entry**, which points to **inode**.
    
- `lseek()` moves the offset for that OFT entry.
    
- Multiple opens = multiple OFT entries → independent offsets.
    

---

# **Single Open vs Multiple Opens**

### **Scenario 1: Single open**

```c
fd = open("file", O_RDONLY);
read(fd, buffer, 100);
read(fd, buffer, 100);
close(fd);
```

**Explanation (from the tables):**

|System Call|Return Code|Current Offset|
|---|---|---|
|open("file", O_RDONLY)|3|0|
|read(fd, buffer, 100)|100|100|
|read(fd, buffer, 100)|100|200|
|read(fd, buffer, 100)|100|300|
|read(fd, buffer, 100)|0|300|
|close(fd)|0|–|

- **fd = 3** → file descriptor in **process FD table**.
    
- **OFT entry** contains offset 0 initially.
    
- Each `read()` increments the offset in **the OFT entry**.
    
- **Only one OFT entry** exists because the file was opened **once**.
    

---

### **Scenario 2: Two opens of the same file**

```c
fd1 = open("file", O_RDONLY);
fd2 = open("file", O_RDONLY);
read(fd1, buffer1, 100);
read(fd2, buffer2, 100);
close(fd1);
close(fd2);
```

**Explanation (from the table):**

|FD|OFT Entry|Current Offset|
|---|---|---|
|fd1|OFT[10]|0 → 100|
|fd2|OFT[11]|0 → 100|

- **fd1** → process FD table points to **OFT[10]**
    
- **fd2** → process FD table points to **OFT[11]**
    
- Each open creates a **separate OFT entry**, even though both point to **the same inode**.
    
- **Offsets are independent**:
    
    - Reading `fd1` increments offset in OFT[10] only.
        
    - Reading `fd2` increments offset in OFT[11] only.
        

---

### ✅ **Key Takeaways**

1. **Single open** → one OFT entry → offset shared by that FD.
    
2. **Multiple opens** → multiple OFT entries → offsets are independent.
    
3. **dup(fd)** → new FD points to the **same OFT entry** → offset shared.
    
4. **fork()** → child shares OFT entries with parent → offsets are shared.
    

---
