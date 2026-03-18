---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/disk_8h.html
original_path: doxygen/html/disk_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

disk.h File Reference

Disk Driver Interface.
[More...](#details)

`#include <[zephyr/kernel.h](kernel_8h_source.md)>`  
`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`  
`#include <[zephyr/sys/dlist.h](dlist_8h_source.md)>`

[Go to the source code of this file.](disk_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [disk\_info](structdisk__info.md) |
|  | Disk info. [More...](structdisk__info.md#details) |
| struct | [disk\_operations](structdisk__operations.md) |
|  | Disk operations. [More...](structdisk__operations.md#details) |

| Macros | |
| --- | --- |
| #define | [DISK\_IOCTL\_GET\_SECTOR\_COUNT](group__disk__driver__interface.md#ga7e75d3121989e64a8c6e218409e8fe95)   1 |
|  | Possible Cmd Codes for disk\_ioctl(). |
| #define | [DISK\_IOCTL\_GET\_SECTOR\_SIZE](group__disk__driver__interface.md#ga03dcb39dd5be7144d8f6ae76b7415e9a)   2 |
|  | Get the size of a disk SECTOR in bytes. |
| #define | [DISK\_IOCTL\_RESERVED](group__disk__driver__interface.md#ga7ffc5d075a4e8d6eb659ee4ea73e62a0)   3 |
|  | reserved. |
| #define | [DISK\_IOCTL\_GET\_ERASE\_BLOCK\_SZ](group__disk__driver__interface.md#ga2444e2a2884f9e0d6dd93aedc5d654ac)   4 |
|  | How many sectors constitute a FLASH Erase block. |
| #define | [DISK\_IOCTL\_CTRL\_SYNC](group__disk__driver__interface.md#ga656aaa245cc142f3ff82a003bb307d62)   5 |
|  | Commit any cached read/writes to disk. |
| #define | [DISK\_IOCTL\_CTRL\_INIT](group__disk__driver__interface.md#ga9def34b23915a3ce6c9a8a746d3d1372)   6 |
|  | Initialize the disk. |
| #define | [DISK\_IOCTL\_CTRL\_DEINIT](group__disk__driver__interface.md#gaf13b377592baace863070fee450bd5be)   7 |
|  | Deinitialize the disk. |
| #define | [DISK\_STATUS\_OK](group__disk__driver__interface.md#gae1730a7bf4ca0210bc8eefe3b590623a)   0x00 |
|  | Possible return bitmasks for disk\_status(). |
| #define | [DISK\_STATUS\_UNINIT](group__disk__driver__interface.md#ga533eb718a946ba60e0ad6e0e4fd4f75a)   0x01 |
|  | Disk status uninitialized. |
| #define | [DISK\_STATUS\_NOMEDIA](group__disk__driver__interface.md#ga1c70c8182b3497f606091f19c142be59)   0x02 |
|  | Disk status no media. |
| #define | [DISK\_STATUS\_WR\_PROTECT](group__disk__driver__interface.md#ga0a5ba8f4be6241f62a969ea56c26f7e3)   0x04 |
|  | Disk status write protected. |

| Functions | |
| --- | --- |
| int | [disk\_access\_register](group__disk__driver__interface.md#gaa11586a0b8ae6f2f0c142cec0df0c5fa) (struct [disk\_info](structdisk__info.md) \*disk) |
|  | Register disk. |
| int | [disk\_access\_unregister](group__disk__driver__interface.md#gada802c6be65186009162a25f391dfb71) (struct [disk\_info](structdisk__info.md) \*disk) |
|  | Unregister disk. |

## Detailed Description

Disk Driver Interface.

This file contains interface for disk access. Apart from disks, various other storage media like Flash and RAM disks may implement this interface to be used by various higher layers(consumers) like USB Mass storage and Filesystems.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [disk.h](disk_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
