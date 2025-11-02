When you remove a file, the OS doesn’t just delete the bytes immediately—it updates its internal structures. Page 14 explains this using `rm` and `unlink()`.

---

### Example:

```bash
prompt> strace rm foo
...
unlink("foo")
...
prompt>
```

---

### Breakdown:

1. **`rm` command**
    
    - User-level command to remove a file.
        
    - Behind the scenes, it calls the **`unlink()` system call**.
        
2. **`unlink("foo")`**
    
    - Removes the **link between the filename `foo` and its inode**.
        
    - It doesn’t immediately erase the content; it just decrements the inode’s **link count**.
        
3. **Reference count check**
    
    - If multiple hard links point to the same inode, removing one filename **doesn’t delete the data**—just reduces the count by 1.
        
    - Only when the link count reaches **0** and no process has the file open, the inode and data blocks are freed.
        
4. **`strace` output**
    
    - Shows exactly which system calls are executed when `rm` runs.
        
    - Confirms that the **actual work is done by `unlink()`**, not by `rm` itself.
        

---

### Key points:

- Removing a file is about **unlinking the name from the inode**, not wiping the disk immediately.
    
- This is why if a file is still **open by some process**, its content can remain accessible until all descriptors are closed.
    
- You can have **dangling file descriptors** pointing to deleted files; the data persists until the last reference is gone.
    

---
