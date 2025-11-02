### Deleting Directories (`rmdir()`)

- **Purpose:** Remove a directory from the filesystem.
    
- **Requirement:** The directory must be **empty** before deletion.
    

---

### How it works

1. **Check if directory is empty**
    
    - Only contains `.` (itself) and `..` (parent).
        
    - If other files/subdirectories exist, `rmdir()` fails.
        
2. **Remove directory entry**
    
    - OS deletes the mapping from the parent directory.
        
3. **Free inode and blocks**
    
    - The inode of the directory is released.
        

---

### Example

```bash
prompt> ls -al
drwxr-x--- 2 root root 4096 Apr 30 16:17 ./     # current dir
drwxr-x--- 26 root root 4096 Apr 30 16:17 ../   # parent dir

prompt> strace mkdir foo
mkdir("foo", 0777) = 0   # directory created
```

- `mkdir()` creates a directory with entries `.` and `..`.
    
- `rmdir()` can only remove it if nothing else is inside.
    

---

### Key Points

- Directories are **special files** with their own structure.
    
- You **cannot remove non-empty directories** with `rmdir()`.
    
- For non-empty directories, recursive deletion is required (e.g., `rm -r`).
    

---

Next we can go into **Hard Links** and how files can have multiple names pointing to the same inode. Do you want me to continue?