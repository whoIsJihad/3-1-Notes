When you create a directory, the OS treats it like a **special kind of file** that stores **directory entries** instead of regular data. Page 15 goes into `mkdir()` and how directories are structured.

---

### `mkdir()` system call

```bash
mkdir("foo", 0777)
```

- **Purpose:** Create a new directory named `foo`.
    
- **Mode `0777`:** Sets initial permissions (read/write/execute for user, group, others).
    

---

### What happens internally

1. **Allocate a new inode**
    
    - The inode tracks metadata for the directory: type, permissions, timestamps, etc.
        
    - The inode doesn’t yet know about the directory’s contents.
        
2. **Create entries for `.` and `..`**
    
    - **`.`** → points to the directory itself (`foo`).
        
    - **`..`** → points to the parent directory (`current directory`).
        
    - These entries are essential for navigation and path resolution.
        
3. **Insert the directory into the parent**
    
    - A new entry in the parent directory points to this new inode with the name `foo`.
        
    - Now the directory exists in the filesystem tree.
        

---

### `ls -al` output example

```text
total 8
drwxr-x--- 2 roo root    6 Apr 30 16:17 ./      # current directory
drwxr-x--- 26 root root 4096 Apr 30 16:17 ../     # parent directory
```

- `.` has 2 links: itself and the parent reference.
    
- `..` links back to the parent.
    
- The size for directories may appear small because it stores **just these entries**.
    

---

### `strace mkdir foo` example

```text
mkdir("foo", 0777) = 0
```

- Shows the system call executed.
    
- Return `0` → success.
    
- OS has allocated inode, created `.` and `..`, and added the entry in the parent.
    

---

### Key points:

- Directories are **files with a structure** for storing filenames + inode mappings.
    
- Empty directories always have **`.` and `..`**.
    
- Creation involves **inode allocation + entry insertion**.
    
- Permissions and ownership are set at creation.
    
