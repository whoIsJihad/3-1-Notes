
---

## 1. **Files and Directories**

- **File:** A linear array of bytes stored on disk. Each file has an **inode number**, which is a low-level identifier for the file in the filesystem.
    
- **Directory:** A mapping of human-readable filenames to inode numbers. Think of a directory as a **table** linking `filename -> inode`.
    
- **Directory tree example:**
    

```text
/
├── foo/
│   └── bar.txt
└── bar/
    └── foo/
        └── bar.txt
```

- Valid files: `/foo/bar.txt`, `/bar/foo/bar.txt`
    
- Valid directories: `/`, `/foo`, `/bar`, `/bar/bar`, `/bar/foo`
    

---

## 2. **Creating Files**

- Use the `open()` system call with the `O_CREAT` flag.
    
- Example:
    

```c
int fd = open("foo", O_CREAT | O_WRONLY | O_TRUNC, S_IRUSR | S_IWUSR);
```

**Flags:**

- `O_CREAT`: Create file if it doesn’t exist
    
- `O_WRONLY`: Open for write-only
    
- `O_TRUNC`: Set file size to zero if it already exists
    
- Returns a **file descriptor (FD)**, an integer used to refer to the file in later operations.
    

---

## 3. **File Descriptor Table & Open File Table**

There are **three important levels of file tracking**:

1. **Process-level File Descriptor Table (FDT):**
    
    - Each process has its own array of integers, each pointing to an entry in the **system-wide open file table (OFT)**.
        
    - Example: `fd = 3` points to OFT entry #10.
        
2. **System-wide Open File Table (OFT):**
    
    - Stores information about **open files system-wide**, e.g., pointer to inode, current offset, flags, reference count.
        
    - Multiple FDs can point to the same OFT entry (via `dup()`), sharing offsets.
        
3. **Inode Table:**
    
    - Stores metadata about the file: size, permissions, block addresses, link count, timestamps.
        
    - Shared by all OFT entries pointing to the same file on disk.
        

**Multiple opens example:**

```text
fd1 = open("file", O_RDONLY);  // FD1 -> OFT entry #10
fd2 = open("file", O_RDONLY);  // FD2 -> OFT entry #11
```

- Two OFT entries exist, each with its own **offset**, but both point to the same inode.
    

**Using `dup()`:**

```c
int fd2 = dup(fd1);
```

- FD2 now points to **the same OFT entry** as FD1.
    
- **Shared offset:** Reading/writing via FD1 moves the offset for FD2 too.
    

---

## 4. **Reading and Writing Files**

- **read(fd, buffer, n):** Reads `n` bytes from FD, updates FD offset.
    
- **write(fd, buffer, n):** Writes `n` bytes to FD, updates FD offset.
    
- **lseek(fd, offset, whence):** Move file offset explicitly.
    

`whence` options:

- `SEEK_SET`: Offset from beginning of file
    
- `SEEK_CUR`: Offset from current position
    
- `SEEK_END`: Offset from end of file
    

**Example simulation:**

```c
fd = open("file", O_RDONLY); // FD=3
lseek(fd, 200, SEEK_SET);    // move to byte 200
read(fd, buffer, 50);        // reads 50 bytes from byte 200
close(fd);
```

---

## 5. **File Persistence (`fsync`)**

- Normally, `write()` may only update **memory buffers**, not disk immediately.
    
- Some applications (DBMS) need **guaranteed disk write**.
    
- `fsync(fd)` forces the file’s buffered data to disk.
    

**Temporary file + rename pattern (common in editors):**

```c
int fd = open("file.txt.tmp", O_WRONLY | O_CREAT | O_TRUNC);
write(fd, buffer, size);
fsync(fd);               // ensure disk write
close(fd);
rename("file.txt.tmp", "file.txt");  // atomic swap
```

- Guarantees: Either old or new file exists, never partial write.
    

---

## 6. **Renaming Files**

- `rename(oldname, newname)` is **atomic**.
    
- Swaps the old name to new name instantly at the filesystem level.
    

---

## 7. **Getting File Information**

- `stat(filename, &statbuf)` retrieves **metadata** about a file.
    

**Metadata includes:**

- `st_dev`: device ID
    
- `st_ino`: inode number
    
- `st_mode`: permissions
    
- `st_nlink`: number of hard links
    
- `st_uid`, `st_gid`: owner and group
    
- `st_size`: file size
    
- `st_atime`, `st_mtime`, `st_ctime`: access, modification, status change times
    

---

## 8. **Removing Files**

- `unlink(filename)` removes a **name from a directory**.
    
- Checks inode reference count:
    
    - If reference count > 1 (hard links exist), only removes the link.
        
    - If count = 0, frees inode and file blocks.
        

---

## 9. **Directories**

- `mkdir(name, mode)` creates an empty directory.
    
- Empty directory contains two entries: `.` (itself) and `..` (parent).
    
- `readdir()` reads directory entries (not `read()`).
    
- `rmdir(name)` deletes a directory; only works if empty.
    

---

## 10. **Hard Links**

- `ln oldfile newfile` creates **another name for the same inode**.
    
- Both names share inode and data blocks.
    
- Example:
    

```text
file (inode 100)
ln file file2  // file2 -> inode 100
```

- Both have `inode 100`, changes to one are seen in the other.
    
- Removing a hard link decreases inode reference count; inode deleted only when count = 0.
    

---

## 11. **Symbolic Links**

- Special file containing **path to another file**.
    
- `ln -s target linkname` creates symlink.
    
- Symlinks can point to directories, cross filesystems, but can **break** if target is deleted.
    

Example:

```bash
echo hello > file
ln -s file file2
cat file2   # prints "hello"
rm file
cat file2   # fails: "No such file or directory"
```

- Unlike hard links, symlinks are independent inodes.
    

---

## 12. **Summary of File Management Operations**

|Operation|System Call|Notes|
|---|---|---|
|Create file|`open(O_CREAT)`|Returns FD|
|Read/Write|`read()`, `write()`|Uses FD, updates offset|
|Move within file|`lseek()`|SEEK_SET/CUR/END|
|Sync|`fsync()`|Force write to disk|
|Rename|`rename()`|Atomic swap|
|Delete|`unlink()`, `rmdir()`|Unlink decreases inode ref count|
|Create directory|`mkdir()`|Contains `.` and `..`|
|Read directory|`readdir()`|Directory-specific syscall|
|Hard link|`link()`|Multiple names for same inode|
|Symbolic link|`ln -s`|File pointing to path|

---

This connects **everything**: low-level inode storage, system-wide open file table, process FDs, offsets, read/write, fsync, renaming, directories, and links (hard + symbolic).

You can now **visualize file operations as three layers**:

1. **Process FD Table:** integers used by your program
    
2. **System-wide Open File Table:** tracks offset, flags, shared by FDs
    
3. **Inode Table on disk:** actual metadata and blocks
    
