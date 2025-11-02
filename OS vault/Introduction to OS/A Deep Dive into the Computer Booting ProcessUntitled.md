
**Tags:** #os #booting #deep-dive #bios #uefi #grub #linux #systemd

The process of booting a computer is a remarkable sequence of events that takes a machine from a powered-off, inert state to a fully functional operating system. This note provides a detailed, step-by-step examination of this process, covering both legacy (BIOS) and modern (UEFI) systems, with a specific focus on how a Linux distribution like Ubuntu comes to life.

### Phase 1: The Silicon - Power and the CPU

The journey begins the moment you press the power button.

1. **Power On:** The Power Supply Unit (PSU) begins its work, and once it stabilizes, it sends a "Power Good" signal to the motherboard.
    
2. **CPU Reset:** This signal releases the CPU's reset line. The CPU's registers are cleared, and its program counter is loaded with a hardcoded, fixed memory address known as the **reset vector**.
    
3. **Firmware Execution:** The reset vector points to the starting location of the system's firmware, which is stored on a non-volatile flash ROM chip on the motherboard. This firmware is either BIOS or UEFI.
    

### Phase 2: Firmware Initialization - BIOS vs. UEFI

The firmware's job is to initialize the hardware and hand off control to the next stage of the boot process.

#### The Legacy Way: BIOS and the MBR

BIOS (Basic Input/Output System) is the original firmware standard.

1. **POST (Power-On Self-Test):** The BIOS first runs a series of diagnostic checks on the essential hardware components: CPU, RAM, storage controllers, and keyboard. You might hear a series of beeps if there's a critical error here.
    
2. **Hardware Initialization:** The BIOS detects and initializes the system's hardware, making it available for use.
    
3. **Boot Device Selection:** The BIOS consults its configuration, stored in a battery-backed memory chip called CMOS, to determine the boot device order (e.g., USB, Hard Drive, Network).
    
4. **MBR Handoff:** The BIOS reads the first 512 bytes from the selected boot device. This block is the **Master Boot Record (MBR)**. It loads this 512-byte block into a fixed location in RAM and jumps execution to it. At this point, the BIOS's job is complete. The MBR is now in control.
    

#### The Modern Way: UEFI and the EFI System Partition (ESP)

UEFI (Unified Extensible Firmware Interface) is the modern successor to BIOS, overcoming many of its limitations.

1. **UEFI Initialization:** Similar to BIOS, UEFI performs hardware initialization. However, it's a far more sophisticated environment, often with a graphical interface, networking capabilities, and its own drivers.
    
2. **Locating the ESP:** Instead of looking for an MBR, UEFI understands partition tables (like GPT, which allows for much larger disks). It looks for a special, FAT32-formatted partition called the **EFI System Partition (ESP)**.
    
3. **Executing the Boot Loader:** The ESP contains boot loader applications as `.efi` files, organized by vendor. UEFI consults its own boot manager settings (stored in NVRAM) to know which `.efi` file to execute. For Ubuntu, this might be `/EFI/ubuntu/grubx64.efi`. UEFI directly loads and runs this file. This is a much cleaner handoff than the MBR method.
    

### Phase 3: The Bootloader - GRUB 2

The MBR or UEFI application is just the first stage. Its job is to load a more powerful, second-stage bootloader. For nearly all Linux distributions, this is **GRUB 2** (GRand Unified Bootloader).

GRUB is critical because it understands filesystems (like ext4, Btrfs, etc.). This allows it to do more than just load a single block from a disk.

1. **Loading Configuration:** GRUB loads its configuration file, `/boot/grub/grub.cfg`. This file contains the menu entries you see when you boot (e.g., "Ubuntu", "Advanced options for Ubuntu", "Windows Boot Manager").
    
2. **Displaying the Menu:** GRUB presents this menu, allowing the user to select an operating system or a specific kernel version.
    
3. **Loading the Kernel and Initrd:** Once an option is selected (or the timeout expires), GRUB performs two crucial actions:
    
    - It loads the Linux **kernel** file (e.g., `/boot/vmlinuz-5.15.0-48-generic`) into memory.
        
    - It loads the **Initial RAM Disk** file (`/boot/initrd.img-5.15.0-48-generic`) into another part of memory.
        
4. **Handoff to Kernel:** GRUB passes control to the loaded kernel, providing it with information like the location of the root filesystem and the `initrd` image.
    

### Phase 4: Kernel Initialization

The kernel is now in memory, but the system is not yet usable.

1. **Self-Decompression:** The `vmlinuz` file is a compressed kernel image. The first thing it does is decompress itself in place in memory and then continues execution.
    
2. **The Initial RAM Disk (`initrd`):** The kernel needs drivers to access the real storage devices (e.g., SATA, NVMe drivers). But these drivers are files on the disk it can't yet read! The `initrd` solves this chicken-and-egg problem. It's a temporary, in-memory root filesystem that contains a minimal set of tools and the crucial kernel modules (drivers) needed to mount the _real_ root filesystem.
    
3. **Pivoting the Root:** The kernel executes a program from the `initrd` that loads the necessary drivers. Once the kernel can see the main hard drive, it "pivots root"—it unmounts the temporary `initrd` and mounts the actual root filesystem (e.g., `/dev/sda2`) on `/`.
    
4. **Starting the `init` Process:** The kernel's final job in the boot process is to start the very first user-space process, `/sbin/init`, which is assigned **Process ID (PID) 1**.
    

### Phase 5: The `init` System - systemd

On all modern Linux systems, `/sbin/init` is a symbolic link to **`systemd`**. This is the parent process of all other processes on the system.

1. **Reading Configuration:** `systemd` reads its "unit" files from directories like `/etc/systemd/system/`. These units define services, mount points, devices, and targets.
    
2. **Parallel Service Start-up:** `systemd` analyzes the dependencies between units and starts system services in parallel to speed up the boot time. This includes crucial services like networking, device management (`udev`), and logging.
    
3. **Reaching a Target:** `systemd` works towards a "target" (analogous to a runlevel in older systems). For a desktop system, this is usually the `graphical.target`.
    
4. **Starting the Display Manager:** To reach the graphical target, `systemd` starts the display manager (e.g., GDM3 for GNOME, LightDM for others).
    
5. **Login Screen:** The display manager presents the graphical login screen. The boot process is now complete. The system is fully operational and is waiting for a user to log in.
    

### Simulation: Booting an Ubuntu Desktop (UEFI)

1. **Power On**: You press the power button.
    
2. **UEFI Firmware**: The motherboard's UEFI firmware initializes.
    
3. **POST**: Hardware checks pass.
    
4. **Boot Manager**: UEFI reads its boot order and finds the "ubuntu" entry.
    
5. **Load GRUB**: UEFI executes `/boot/efi/EFI/ubuntu/grubx64.efi` from the ESP.
    
6. **GRUB Menu**: The GRUB boot menu is displayed on the screen.
    
7. **Kernel Load**: After a 5-second timeout, GRUB loads `/boot/vmlinuz-...` and `/boot/initrd.img-...` into RAM.
    
8. **Kernel Takes Over**: GRUB passes control to the kernel.
    
9. **Initrd Phase**: The kernel uses the `initrd` to load the `nvme` or `ahci_pci` driver.
    
10. **Root Mount**: With the driver loaded, the kernel mounts your root partition (e.g., `/dev/nvme0n1p2`) on `/`.
    
11. **`systemd` Starts**: The kernel executes `/sbin/init` (which is `systemd`) as PID 1.
    
12. **Services Launch**: `systemd` starts network-manager, bluetooth, udev, and dozens of other background services in parallel.
    
13. **Login Screen Appears**: `systemd` starts the `gdm3.service`, and the graphical login screen is displayed. You can now enter your password.