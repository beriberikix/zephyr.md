---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structdisk__info.html
original_path: doxygen/html/structdisk__info.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

disk\_info Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [Disk Driver Interface](group__disk__driver__interface.md)

Disk info.
[More...](#details)

`#include <[disk.h](disk_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98) | [node](#ab3413d8809d5181c671e1890a4662ba2) |
|  | Internally used list node. |
| const char \* | [name](#ac8ce763ca2514e4c4f4f8e0e04547ed3) |
|  | Disk name. |
| const struct [disk\_operations](structdisk__operations.md) \* | [ops](#a329a571f988718fd4737b8974d4f7ada) |
|  | Disk operations. |
| const struct [device](structdevice.md) \* | [dev](#ae316915bd577f22dc9d353fc4b2f04bb) |
|  | Device associated to this disk. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [refcnt](#accc0a618e4d939543f6ffc553b45e3b2) |
|  | Internally used disk reference count. |

## Detailed Description

Disk info.

## Field Documentation

## [◆ ](#ae316915bd577f22dc9d353fc4b2f04bb)dev

| const struct [device](structdevice.md)\* disk\_info::dev |
| --- |

Device associated to this disk.

## [◆ ](#ac8ce763ca2514e4c4f4f8e0e04547ed3)name

| const char\* disk\_info::name |
| --- |

Disk name.

## [◆ ](#ab3413d8809d5181c671e1890a4662ba2)node

| [sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98) disk\_info::node |
| --- |

Internally used list node.

## [◆ ](#a329a571f988718fd4737b8974d4f7ada)ops

| const struct [disk\_operations](structdisk__operations.md)\* disk\_info::ops |
| --- |

Disk operations.

## [◆ ](#accc0a618e4d939543f6ffc553b45e3b2)refcnt

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) disk\_info::refcnt |
| --- |

Internally used disk reference count.

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[disk.h](disk_8h_source.md)

- [disk\_info](structdisk__info.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
