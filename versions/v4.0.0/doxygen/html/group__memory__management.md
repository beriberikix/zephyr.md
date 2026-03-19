---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/group__memory__management.html
original_path: doxygen/html/group__memory__management.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Memory Management

[Operating System Services](group__os__services.md)

Memory Management.
[More...](#details)

| Topics | |
| --- | --- |
|  | [Memory Banks Driver APIs](group__mm__drv__bank__apis.md) |
|  | Memory Banks Driver APIs. |
|  | [Memory Blocks APIs](group__mem__blocks__apis.md) |
|  | [Memory Management Driver APIs](group__mm__drv__apis.md) |
|  | Memory Management Driver APIs. |

| Functions | |
| --- | --- |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [sys\_mm\_is\_phys\_addr\_in\_range](#gaef71defc60c1d898d5ece56c6826a2e1) ([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) phys) |
|  | Check if a physical address is within range of physical memory. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [sys\_mm\_is\_virt\_addr\_in\_range](#ga1a4b707eae142c8f871a198b865e3d16) (void \*virt) |
|  | Check if a virtual address is within range of virtual memory. |

## Detailed Description

Memory Management.

## Function Documentation

## [◆ ](#gaef71defc60c1d898d5ece56c6826a2e1)sys\_mm\_is\_phys\_addr\_in\_range()

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) sys\_mm\_is\_phys\_addr\_in\_range | ( | [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | *phys* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[mem_manage.h](mem__manage_8h.md)>`

Check if a physical address is within range of physical memory.

This checks if the physical address (`virt`) is within permissible range, e.g. between :kconfig:option:CONFIG\_SRAM\_BASE\_ADDRESS and (:kconfig:option:CONFIG\_SRAM\_BASE\_ADDRESS + :kconfig:option:CONFIG\_SRAM\_SIZE).

Note
:   Only used if :kconfig:option:CONFIG\_KERNEL\_VM\_USE\_CUSTOM\_MEM\_RANGE\_CHECK is enabled.

Parameters
:   | phys | Physical address to be checked. |
    | --- | --- |

Returns
:   True if physical address is within range, false if not.

## [◆ ](#ga1a4b707eae142c8f871a198b865e3d16)sys\_mm\_is\_virt\_addr\_in\_range()

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) sys\_mm\_is\_virt\_addr\_in\_range | ( | void \* | *virt* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[mem_manage.h](mem__manage_8h.md)>`

Check if a virtual address is within range of virtual memory.

This checks if the virtual address (`virt`) is within permissible range, e.g. between :kconfig:option:CONFIG\_KERNEL\_VM\_BASE and (:kconfig:option:CONFIG\_KERNEL\_VM\_BASE + :kconfig:option:CONFIG\_KERNEL\_VM\_SIZE).

Note
:   Only used if :kconfig:option:CONFIG\_KERNEL\_VM\_USE\_CUSTOM\_MEM\_RANGE\_CHECK is enabled.

Parameters
:   | virt | Virtual address to be checked. |
    | --- | --- |

Returns
:   True if virtual address is within range, false if not.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
