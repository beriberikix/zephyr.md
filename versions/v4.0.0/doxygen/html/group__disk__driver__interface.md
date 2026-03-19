---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/group__disk__driver__interface.html
original_path: doxygen/html/group__disk__driver__interface.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Disk Driver Interface

[Device Driver APIs](group__io__interfaces.md)

Disk Driver Interface.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [disk\_info](structdisk__info.md) |
|  | Disk info. [More...](structdisk__info.md#details) |
| struct | [disk\_operations](structdisk__operations.md) |
|  | Disk operations. [More...](structdisk__operations.md#details) |

| Macros | |
| --- | --- |
| #define | [DISK\_IOCTL\_GET\_SECTOR\_COUNT](#ga7e75d3121989e64a8c6e218409e8fe95)   1 |
|  | Possible Cmd Codes for disk\_ioctl(). |
| #define | [DISK\_IOCTL\_GET\_SECTOR\_SIZE](#ga03dcb39dd5be7144d8f6ae76b7415e9a)   2 |
|  | Get the size of a disk SECTOR in bytes. |
| #define | [DISK\_IOCTL\_RESERVED](#ga7ffc5d075a4e8d6eb659ee4ea73e62a0)   3 |
|  | reserved. |
| #define | [DISK\_IOCTL\_GET\_ERASE\_BLOCK\_SZ](#ga2444e2a2884f9e0d6dd93aedc5d654ac)   4 |
|  | How many sectors constitute a FLASH Erase block. |
| #define | [DISK\_IOCTL\_CTRL\_SYNC](#ga656aaa245cc142f3ff82a003bb307d62)   5 |
|  | Commit any cached read/writes to disk. |
| #define | [DISK\_IOCTL\_CTRL\_INIT](#ga9def34b23915a3ce6c9a8a746d3d1372)   6 |
|  | Initialize the disk. |
| #define | [DISK\_IOCTL\_CTRL\_DEINIT](#gaf13b377592baace863070fee450bd5be)   7 |
|  | Deinitialize the disk. |
| #define | [DISK\_STATUS\_OK](#gae1730a7bf4ca0210bc8eefe3b590623a)   0x00 |
|  | Possible return bitmasks for disk\_status(). |
| #define | [DISK\_STATUS\_UNINIT](#ga533eb718a946ba60e0ad6e0e4fd4f75a)   0x01 |
|  | Disk status uninitialized. |
| #define | [DISK\_STATUS\_NOMEDIA](#ga1c70c8182b3497f606091f19c142be59)   0x02 |
|  | Disk status no media. |
| #define | [DISK\_STATUS\_WR\_PROTECT](#ga0a5ba8f4be6241f62a969ea56c26f7e3)   0x04 |
|  | Disk status write protected. |

| Functions | |
| --- | --- |
| int | [disk\_access\_register](#gaa11586a0b8ae6f2f0c142cec0df0c5fa) (struct [disk\_info](structdisk__info.md) \*disk) |
|  | Register disk. |
| int | [disk\_access\_unregister](#gada802c6be65186009162a25f391dfb71) (struct [disk\_info](structdisk__info.md) \*disk) |
|  | Unregister disk. |

## Detailed Description

Disk Driver Interface.

Since
:   1.6

Version
:   1.0.0

## Macro Definition Documentation

## [◆ ](#gaf13b377592baace863070fee450bd5be)DISK\_IOCTL\_CTRL\_DEINIT

| #define DISK\_IOCTL\_CTRL\_DEINIT   7 |
| --- |

`#include <[disk.h](disk_8h.md)>`

Deinitialize the disk.

This IOCTL can be used to de-initialize the disk, enabling it to be removed from the system if the disk is hot-pluggable. Disk usage is reference counted, so for a given disk the [DISK\_IOCTL\_CTRL\_DEINIT](#gaf13b377592baace863070fee450bd5be) IOCTL must be issued as many times as the [DISK\_IOCTL\_CTRL\_INIT](#ga9def34b23915a3ce6c9a8a746d3d1372) IOCTL was issued in order to de-initialize it.

This macro optionally accepts a pointer to a boolean as the buf parameter, which if true indicates the disk should be forcibly stopped, ignoring all reference counts. The disk driver must report success if a forced stop is requested, but this operation is inherently unsafe.

## [◆ ](#ga9def34b23915a3ce6c9a8a746d3d1372)DISK\_IOCTL\_CTRL\_INIT

| #define DISK\_IOCTL\_CTRL\_INIT   6 |
| --- |

`#include <[disk.h](disk_8h.md)>`

Initialize the disk.

This IOCTL must be issued before the disk can be used for I/O. It is reference counted, so only the first successful invocation of this macro on an uninitialized disk will initialize the IO device

## [◆ ](#ga656aaa245cc142f3ff82a003bb307d62)DISK\_IOCTL\_CTRL\_SYNC

| #define DISK\_IOCTL\_CTRL\_SYNC   5 |
| --- |

`#include <[disk.h](disk_8h.md)>`

Commit any cached read/writes to disk.

## [◆ ](#ga2444e2a2884f9e0d6dd93aedc5d654ac)DISK\_IOCTL\_GET\_ERASE\_BLOCK\_SZ

| #define DISK\_IOCTL\_GET\_ERASE\_BLOCK\_SZ   4 |
| --- |

`#include <[disk.h](disk_8h.md)>`

How many sectors constitute a FLASH Erase block.

## [◆ ](#ga7e75d3121989e64a8c6e218409e8fe95)DISK\_IOCTL\_GET\_SECTOR\_COUNT

| #define DISK\_IOCTL\_GET\_SECTOR\_COUNT   1 |
| --- |

`#include <[disk.h](disk_8h.md)>`

Possible Cmd Codes for disk\_ioctl().

Get the number of sectors in the disk

## [◆ ](#ga03dcb39dd5be7144d8f6ae76b7415e9a)DISK\_IOCTL\_GET\_SECTOR\_SIZE

| #define DISK\_IOCTL\_GET\_SECTOR\_SIZE   2 |
| --- |

`#include <[disk.h](disk_8h.md)>`

Get the size of a disk SECTOR in bytes.

## [◆ ](#ga7ffc5d075a4e8d6eb659ee4ea73e62a0)DISK\_IOCTL\_RESERVED

| #define DISK\_IOCTL\_RESERVED   3 |
| --- |

`#include <[disk.h](disk_8h.md)>`

reserved.

It used to be DISK\_IOCTL\_GET\_DISK\_SIZE

## [◆ ](#ga1c70c8182b3497f606091f19c142be59)DISK\_STATUS\_NOMEDIA

| #define DISK\_STATUS\_NOMEDIA   0x02 |
| --- |

`#include <[disk.h](disk_8h.md)>`

Disk status no media.

## [◆ ](#gae1730a7bf4ca0210bc8eefe3b590623a)DISK\_STATUS\_OK

| #define DISK\_STATUS\_OK   0x00 |
| --- |

`#include <[disk.h](disk_8h.md)>`

Possible return bitmasks for disk\_status().

Disk status okay

## [◆ ](#ga533eb718a946ba60e0ad6e0e4fd4f75a)DISK\_STATUS\_UNINIT

| #define DISK\_STATUS\_UNINIT   0x01 |
| --- |

`#include <[disk.h](disk_8h.md)>`

Disk status uninitialized.

## [◆ ](#ga0a5ba8f4be6241f62a969ea56c26f7e3)DISK\_STATUS\_WR\_PROTECT

| #define DISK\_STATUS\_WR\_PROTECT   0x04 |
| --- |

`#include <[disk.h](disk_8h.md)>`

Disk status write protected.

## Function Documentation

## [◆ ](#gaa11586a0b8ae6f2f0c142cec0df0c5fa)disk\_access\_register()

| int disk\_access\_register | ( | struct [disk\_info](structdisk__info.md) \* | *disk* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[disk.h](disk_8h.md)>`

Register disk.

Parameters
:   | [in] | disk | Pointer to the disk info structure |
    | --- | --- | --- |

Returns
:   0 on success, negative errno code on fail

## [◆ ](#gada802c6be65186009162a25f391dfb71)disk\_access\_unregister()

| int disk\_access\_unregister | ( | struct [disk\_info](structdisk__info.md) \* | *disk* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[disk.h](disk_8h.md)>`

Unregister disk.

Parameters
:   | [in] | disk | Pointer to the disk info structure |
    | --- | --- | --- |

Returns
:   0 on success, negative errno code on fail

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
