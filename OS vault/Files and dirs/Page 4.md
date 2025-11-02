
## **1️⃣ `open()` system call**

```c
int fd = open("foo", O_CREAT|O_WRONLY|O_TRUNC, S_IRUSR|S_IWUSR);
```

This is not just a simple function call — the OS is doing a lot under the hood:

1. **Look for the file** `"foo"` in the directory:
    
    - The OS uses the **directory structure** to check if `"foo"` exists.
        
    - If **O_CREAT** is set and the file does **not exist**, the OS:
        
        - Allocates a **new inode** (a data structure storing file metadata like size, owner, permissions, and pointers to blocks on disk).
            
        - Creates a new entry in the **parent directory**, linking `"foo"` → new inode number.
            
2. **Apply the flags**:
    
    - **O_WRONLY** → open file in write-only mode.
        
    - **O_TRUNC** → if the file exists, clear its content (set file size to 0).  
        Internally, the OS frees the previously allocated blocks and updates the inode’s size to 0.
        
3. **Set file permissions**:
    
    - `S_IRUSR | S_IWUSR` → sets **read/write permission for owner**.
        
    - The OS stores this in the inode `st_mode` field (like `0644` or `0600`).
        

---

## **2️⃣ File descriptor (fd)**

- `fd` is a **small integer**, unique per process, used to reference an **open file**.
    
- The OS maintains a **file descriptor table** inside the process structure:
    

```c
struct proc {
    ...
    struct file *ofile[NOFILE]; // pointer array to open file structures
    ...
};
```

Here’s what happens:

1. **Allocate an entry** in `ofile[]`:
    
    - Find the **first empty slot** (next available integer).
        
    - Point it to a **struct file** in the **system-wide file table** (ftable in xv6).
        
2. **struct file** contains:
    

```c
struct file {
    int ref;          // reference count: how many fd’s point to this file
    char readable;    // is file readable?
    char writable;    // is file writable?
    struct inode *ip; // pointer to the inode
    uint off;         // current file offset
};
```

- `ref` → ensures that if multiple fds point to the same file (dup, fork), the system knows when it’s safe to free resources.
    
- `off` → keeps track of **current position for reading/writing** (file pointer).
    

---

## **3️⃣ How fd interacts with the OS**

1. When you do `write(fd, buf, size)`:
    
    - The OS uses `fd` → `ofile[fd]` → `struct file` → inode.
        
    - It writes data to the blocks on disk starting from `off`.
        
    - Updates `off` after write.
        
2. When you do `read(fd, buf, size)`:
    
    - The OS reads from the file starting at `off`.
        
    - Updates `off` after read.
        

So **fd abstracts all the low-level details** (inode, disk blocks, offsets) into a simple integer for the programmer.

---

## ✅ Key takeaways from Page 4

1. **`open()`** is not just opening a file; it may create it, truncate it, and set permissions.
    
2. **File descriptor (`fd`)** is a process-level handle to access the file.
    
3. The OS internally maintains:
    
    - **Per-process table** (`ofile[]`)
        
    - **System-wide file table** (`struct file ftable`)
        
    - **Inode metadata** pointing to the actual disk blocks.
        

For deeper analysis read  [[ Page 4 deeper analysis ]]