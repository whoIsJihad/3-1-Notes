
# **1️⃣ Three main tables when you open a file**

When a process opens a file, there are **three levels of “tables” involved**:

|Table|Where it is|What it stores|How many copies exist?|
|---|---|---|---|
|**File Descriptor Table (per process)**|Inside each process (`struct proc`)|Array of integers (`fd`) pointing to **system-wide open file entries**|One per process|
|**System-wide Open File Table (global, kernel)**|In kernel (`struct file ftable` in xv6)|Array of `struct file`, each contains: pointer to inode, current file offset, ref count, readable/writable flags|One global table for all open files|
|**Inode Table (global, kernel)**|In kernel|Metadata of files: size, block pointers, permissions, timestamps, ref count|One per file on disk|

---

# **2️⃣ How they link together**

Let’s open a file called `"foo"`.

```
Process A       System-wide Open File Table       Inode Table
-----------     -------------------------       -----------
fd=3  ---->    struct file (ref=1, off=0)  ----> inode of "foo"
fd=4  ---->    struct file (ref=1, off=0)  ----> inode of "bar"
```

### Step by step:

1. **Process A calls**:
    

```c
int fd = open("foo", O_CREAT|O_WRONLY|O_TRUNC, S_IRUSR|S_IWUSR);
```

2. OS checks **directory**:
    
    - Does `"foo"` exist?
        
    - If not, create an **inode** for `"foo"`.
        
3. OS creates an entry in **system-wide open file table**:
    

```c
struct file {
    int ref = 1;          // how many fds are pointing here
    char readable = 0;
    char writable = 1;
    struct inode *ip = inode_of_foo;
    uint off = 0;
};
```

4. OS assigns a **file descriptor** in **process A’s table**:
    

```c
proc->ofile[3] = pointer_to(struct file of "foo");
```

5. Now process A can **read/write using fd=3**, which updates `off` inside **system-wide file table**.
    

---

# **3️⃣ What happens with dup() or fork()?**

- **dup()** duplicates a file descriptor:
    

```c
int fd2 = dup(fd);
```

- Both `fd` and `fd2` in the **process table** point to the **same system-wide open file table entry**.
    
- **ref count** in `struct file` increases.
    
- **fork()**:
    
    - Child gets a **copy of parent’s file descriptor table**.
        
    - Both tables point to the **same system-wide open file entries**.
        

---

# **4️⃣ Visualizing the flow**

```
+----------------+       +---------------------+       +---------------+
| Process A fd[] | ----> | system-wide ftable  | ----> | inode of "foo"|
| 0 -> stdin     |       | fd3: off=0, ref=1  |       | size, perms   |
| 1 -> stdout    |       | fd4: off=0, ref=1  |       | block pointers|
| 2 -> stderr    |       | ...                 |       | ...           |
| 3 -> "foo"     |       +---------------------+       +---------------+
+----------------+
```

- **fd table** → maps integer → `struct file`.
    
- **system-wide open file table** → maps `struct file` → inode + offset.
    
- **inode table** → stores actual metadata and disk block info.
    

---

✅ **Key points to remember**

1. **File descriptor table** → per-process, contains **integers** (fd).
    
2. **Open file table** → global, contains **state of open files** (offset, permissions, reference count).
    
3. **Inode table** → global, contains **file metadata**.
    
4. **Offset is stored in the open file table**, not in fd table or inode.
    
5. **ref count** in open file table = number of fds pointing to it.
    
6. **inode ref count** = number of hard links to the file.
    

---
