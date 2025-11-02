### Hard Links (`link()`)

- **Definition:** A hard link is an additional name for an existing file.
    
- **Key Idea:** Multiple filenames can refer to the **same inode**.
    
- **Constraints:**
    
    1. Cannot link directories.
        
    2. Cannot link across different filesystems/partitions.
        

---

### How Hard Links Work

1. **Create inode**
    
    - Each file has an inode that stores metadata: size, permissions, block pointers, etc.
        
2. **Associate a human-readable name**
    
    - `link("file", "file2")` creates a new name `file2` pointing to the same inode as `file`.
        
3. **Add to directory**
    
    - The new name is stored in the directory as a `<name, inode>` pair.
        
4. **Reference count**
    
    - The inode keeps a **link count**: number of names pointing to it.
        
    - File is only deleted when the count drops to zero.
        

---

### Example

```bash
prompt> echo hello > file      # create file
prompt> cat file
hello

prompt> ln file file2           # create hard link
prompt> cat file2
hello

prompt> ls -i file file2
67158084 file
67158084 file2  # same inode number
```

- Both `file` and `file2` point to inode `67158084`.
    
- Any changes to one are reflected in the other.
    

---

### Removing Hard Links (`unlink()`)

1. **Remove a name**
    
    - `unlink("file")` deletes the directory entry, **not the inode** yet.
        
2. **Decrease inode link count**
    
    - If count > 0, inode still exists; file content is preserved.
        
3. **Delete file only when count = 0**
    
    - Once no names point to the inode, OS frees the inode and associated blocks.
        

---

### Example of unlinking multiple hard links

```bash
ln file file2        # link count becomes 2
ln file2 file3       # link count becomes 3
rm file              # link count decreases to 2
rm file2             # link count decreases to 1
rm file3             # link count decreases to 0, file content removed
```

---

### Symbolic Links (`ln -s`)

- **Definition:** A symbolic link (or symlink) is a **special file that stores a path** to another file or directory.
    
- **Key differences from hard links:**
    
    1. Can point to directories.
        
    2. Can cross filesystem boundaries.
        
    3. The symlink is a separate inode from the target file.
        

---

### How Symbolic Links Work

1. **Create a symlink:**
    
    ```bash
    ln -s target_file link_name
    ```
    
    - `link_name` is the symlink.
        
    - Contains the path to `target_file`.
        
2. **Accessing a symlink:**
    
    - When you `cat link_name` or open it, the OS resolves the path to `target_file`.
        
    - If `target_file` is deleted, the symlink becomes **dangling**.
        

---

### Example

```bash
prompt> echo hello > file       # original file
prompt> ln -s file file2        # symbolic link
prompt> cat file2
hello
```

- `file2` points to `file` but is a different inode.
    
- Listing with `ls -al` shows:
    

```text
-rw-r----- 1 remzi remzi 6 May 3 19:10 file      # regular file
lrwxrwxrwx 1 remzi remzi 4 May 3 19:10 file2 -> file  # symbolic link
```

---

### Dangling Symbolic Link

```bash
prompt> rm file
prompt> cat file2
cat: file2: No such file or directory
```

- The symlink still exists but points to a file that no longer exists.
    

---

Symbolic links are **lightweight references** to files or directories, whereas hard links are **additional names for the same inode**.

