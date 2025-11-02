


# **1️⃣ Example from the slides**

Commands:

```bash
prompt> echo hello > foo      # save "hello" into file foo
prompt> cat foo                # display contents of foo
prompt> strace cat foo         # see what cat is doing
```

---

# **2️⃣ What’s happening under the hood**

### **Step A: `open()`**

```c
open("foo", O_RDONLY|O_LARGEFILE)  => returns 3
```

- `"foo"` is opened for reading.
    
- **3** is the **file descriptor** assigned in the process’s fd table.
    
- File descriptor **3** points to a **system-wide open file table entry** with:
    
    - inode pointer → points to `"foo"`’s inode
        
    - current offset = 0
        
    - readable = 1, writable = 0
        
    - ref count = 1
        

---

### **Step B: `read()`**

```c
read(3, buffer, 4096)  => returns 6
```

- Reads 6 bytes (`"hello\n"`) from file into **buffer**.
    
- Updates **offset** in the system-wide open file table for fd 3: offset = 6.
    
- Returns the number of bytes read (6).
    

---

### **Step C: `write()`**

```c
write(1, buffer, 6)  => returns 6
```

- Writes the 6 bytes from **buffer** to **stdout** (fd 1).
    
- Fd 1 → standard output, handled by OS.
    

---

### **Step D: `read()` again**

```c
read(3, buffer, 4096)  => returns 0
```

- Offset = 6, file size = 6 → EOF reached.
    
- Returns 0 → no more bytes to read.
    

---

# **3️⃣ Key Concepts**

1. **File descriptor (`fd`)** → integer in process table.
    
2. **Open file table** → stores:
    
    - **current offset** (where next read/write happens)
        
    - permissions (readable/writable)
        
    - pointer to inode
        
3. **Offset moves automatically** after each read/write.
    
4. **strace** shows the exact system calls:
    
    - `open()` → returns fd
        
    - `read()` → copies bytes into buffer
        
    - `write()` → outputs bytes to stdout
        

---

# **4️⃣ How this connects to page 4 tables**

- File descriptor table (per process) → fd 3 points to open file table entry.
    
- Open file table → stores **current offset**, **pointer to inode**, **ref count**.
    
- Inode → contains file metadata (size, blocks, timestamps).
    

****

