**Tags:** #os #storage #hdd #hardware

# HDD Geometry

A hard disk drive is a mechanical device that stores data on rotating magnetic platters. Its physical structure directly impacts its performance.

### Core Components

- **Platter:** A circular, rigid disk coated with a magnetic material where data is stored. A drive can have multiple platters stacked on top of each other. Each platter has two surfaces.
    
- **Spindle:** The central motor that spins the platters at a constant, high speed (e.g., 7200 RPM).
    
- **Disk Head:** A tiny electromagnetic component that reads or writes data to a platter surface. There is one head per surface.
    
- **Disk Arm:** The mechanical arm that moves the heads in unison across the platters, from the center to the edge.
    

### Data Organization

- **Track:** A concentric circle on a platter surface where data is stored. Each platter has thousands of tracks.
    
- **Sector:** The smallest addressable unit of storage on a disk, typically 512 bytes. Each track is divided into a number of sectors.
    

A specific sector is located by its cylinder (a stack of tracks at the same position across all platters), head (which surface to use), and sector number on that track.

**Links:** [[Hard Disk Drives MOC]], [[HDD I_O Time Calculation]]