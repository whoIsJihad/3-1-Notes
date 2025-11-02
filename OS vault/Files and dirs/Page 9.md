

---

# **Page 9 – File Descriptors: fork(), dup(), and fsync()**

---

## **1. Child Process Inherits File Descriptor Table (fork)**

When a process calls `fork()`:

- The **child process** gets a **copy of the parent's file descriptor table (FD table)**.
    
- Each FD in the child points to the **same open file table (OFT) entry** as the parent.
    
- **Implication:**
    
    - Both parent and child share **offsets, open mode, etc.**.
        
    - Example:
        
        ```c
        int fd = open("file.txt", O_RDONLY);
        pid_t pid = fork();
        ```
        
        - `fd` exists in both parent and child.
            
        - Reading from `fd` in parent **changes the offset** seen by the child, because they share the **OFT entry**.
            
- This is important for **pipes, files, sockets**, etc., because the child can continue using the same open file state.
    

---

## **2. Duplicating a File Descriptor (dup)**

`dup()` creates a **new file descriptor** that points to the **same OFT entry** as the original FD.

### **Example from Page 9:**

```c
int main(int argc, char *argv[]) {
  int fd = open("README", O_RDONLY);
  assert(fd >= 0);
  
  int fd2 = dup(fd);
  // now fd and fd2 can be used interchangeably
  return 0;
}
```

### **Key Points:**

- `fd` and `fd2` **point to the same OFT entry**.
    
- **Offset is shared**:
    
    - If you `read(fd, ...)`, the offset advances.
        
    - Reading from `fd2` continues from the **same offset**.
        
- **Why useful:**
    
    - Redirect output (`dup2`)
        
    - Share open files between processes
        
    - Maintain consistent file state across multiple descriptors
        

---

## **3. Persistency and fsync()**

Normally, a write to a file:

1. Writes data to the **kernel buffer (page cache)**.
    
2. The data is **eventually written to disk** asynchronously.
    

This **delays durability**, which is fine for most apps. But for applications like **databases**, you need **guaranteed persistence**.

### **fsync()**

```c
fsync(fd);
```

- Forces the **kernel to flush all buffered data** for the given FD to the **disk immediately**.
    
- Guarantees **durability**.
    

**Why this matters:**

- Example: A DBMS updating a transaction log. If the system crashes **before the buffer flushes**, you lose the update unless you `fsync()`.
    
- Without `fsync()`, writes may remain in memory and not survive a crash.
    

### **Steps for durable file write:**

1. `write(fd, buffer, size)` → writes to kernel buffer.
    
2. `fsync(fd)` → flush buffer to disk.
    
3. (Optional) `fsync()` on the **directory** → ensures directory metadata (inode update) is written too.
    

---

### **Summary – Page 9 Concepts**

1. **fork()**
    
    - Child inherits parent's FD table
        
    - FD points to the same OFT entry → offsets shared
        
2. **dup()**
    
    - Creates a new FD pointing to the **same OFT entry**
        
    - Offsets are shared between old and new FD
        
3. **fsync()**
    
    - Flushes file data **immediately to disk**
        
    - Ensures **durability** for critical applications
        

---

This page essentially explains **how file descriptors behave across processes**, and the difference between **sharing FD state (fork/dup)** vs **sharing file content (OFT and inode)**.
