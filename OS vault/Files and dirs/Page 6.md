
---

# **1️⃣ File Offset**

- **Offset** = current position in the file where the next read/write will start.
    
- Every open file (per open file table entry) has its **own offset**.
    
- Example:
    
    ```text
    fd = 3, offset = 0   # start of file
    read(fd, buffer, 6)  # reads "hello\n"
    offset -> 6          # automatically moves after read
    ```
    
- The offset **updates automatically** after each read or write.
    

---

# **2️⃣ Reading/Writing at a specific offset**

Sometimes you don’t want to read/write sequentially. Use:

```c
off_t lseek(int fd, off_t offset, int whence);
```

- `fd` → file descriptor
    
- `offset` → where you want to move
    
- `whence` → how offset is calculated:
    
    1. **SEEK_SET** → offset = specified value from start
        
    2. **SEEK_CUR** → offset = current offset + value
        
    3. **SEEK_END** → offset = file size + value
        
- Example:
    
    ```c
    lseek(fd, 200, SEEK_SET);  // move to byte 200
    read(fd, buffer, 50);      // read 50 bytes starting at byte 200
    ```
    

---

# **3️⃣ File Structure in Kernel**

From `struct file`:

```c
struct file {
    int ref;             // reference count
    char readable;       // 1 if readable
    char writable;       // 1 if writable
    struct inode *ip;    // pointer to inode
    uint off;            // current offset
};
```

- **ref** → how many descriptors point to this file table entry
    
- **ip** → inode, which has file metadata
    
- **off** → the file offset for next read/write
    

---

# ✅ **Key Points**

- Offset is **per open file table entry**, not per file descriptor.
    
- `read()`/`write()` automatically update the offset.
    
- `lseek()` allows random access.
    
- `struct file` is the kernel-level representation of the open file.
    

