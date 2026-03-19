---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/retained__mem_8h.html
original_path: doxygen/html/retained__mem_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

retained\_mem.h File Reference

Public API for retained memory drivers.
[More...](#details)

`#include <[stdint.h](stdint_8h_source.md)>`  
`#include <stddef.h>`  
`#include <[sys/types.h](lib_2libc_2minimal_2include_2sys_2types_8h_source.md)>`  
`#include <[zephyr/kernel.h](kernel_8h_source.md)>`  
`#include <[zephyr/device.h](device_8h_source.md)>`  
`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`  
`#include <[zephyr/sys/math_extras.h](math__extras_8h_source.md)>`  
`#include <zephyr/syscalls/retained_mem.h>`

[Go to the source code of this file.](retained__mem_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [retained\_mem\_driver\_api](structretained__mem__driver__api.md) |
|  | Retained memory driver API API which can be used by a device to store data in a retained memory area. [More...](structretained__mem__driver__api.md#details) |

| Typedefs | |
| --- | --- |
| typedef [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118)(\* | [retained\_mem\_size\_api](group__retained__mem__interface.md#ga684490184eedc8d3f56b25d7b6e50a06)) (const struct [device](structdevice.md) \*dev) |
|  | Callback API to get size of retained memory area. |
| typedef int(\* | [retained\_mem\_read\_api](group__retained__mem__interface.md#ga3831f3ec0e0de7957cc6ce7da0cfbe58)) (const struct [device](structdevice.md) \*dev, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) offset, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buffer, [size\_t](#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
|  | Callback API to read from retained memory area. |
| typedef int(\* | [retained\_mem\_write\_api](group__retained__mem__interface.md#gaf6e43d230b1a606e90f3a236aeff1909)) (const struct [device](structdevice.md) \*dev, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) offset, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buffer, [size\_t](#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
|  | Callback API to write to retained memory area. |
| typedef int(\* | [retained\_mem\_clear\_api](group__retained__mem__interface.md#ga3fde220eceb8a45a7a42cfbb1930e27d)) (const struct [device](structdevice.md) \*dev) |
|  | Callback API to clear retained memory area (reset all data to 0x00). |

| Functions | |
| --- | --- |
|  | [sizeof](#a8c945f5e523f7f88fe4d09bfe304240e) ([size\_t](#a36713c339c3c5ec6d6bd481480bdb6f9))) |
| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) | [retained\_mem\_size](group__retained__mem__interface.md#gaa0b4b6db4c96054a709f803880f3091a) (const struct [device](structdevice.md) \*dev) |
|  | Returns the size of the retained memory area. |
| int | [retained\_mem\_read](group__retained__mem__interface.md#ga47fba21400c1f7019e7bd0e8f10662b3) (const struct [device](structdevice.md) \*dev, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) offset, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buffer, [size\_t](#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
|  | Reads data from the Retained memory area. |
| int | [retained\_mem\_write](group__retained__mem__interface.md#ga1976ac945eb7c09b8dd6121926af0c6a) (const struct [device](structdevice.md) \*dev, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) offset, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buffer, [size\_t](#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
|  | Writes data to the Retained memory area - underlying data does not need to be cleared prior to writing. |
| int | [retained\_mem\_clear](group__retained__mem__interface.md#ga5962d863c21cd91e259bf47abf2154d7) (const struct [device](structdevice.md) \*dev) |
|  | Clears data in the retained memory area by setting it to 0x00. |

| Variables | |
| --- | --- |
| Size of [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) must be equal or less than size of | [size\_t](#a36713c339c3c5ec6d6bd481480bdb6f9) |

## Detailed Description

Public API for retained memory drivers.

## Function Documentation

## [◆ ](#a8c945f5e523f7f88fe4d09bfe304240e)sizeof()

| sizeof | ( | [size\_t](#a36713c339c3c5ec6d6bd481480bdb6f9) |  | ) |  |
| --- | --- | --- | --- | --- | --- |

## Variable Documentation

## [◆ ](#a36713c339c3c5ec6d6bd481480bdb6f9)size\_t

| Size of [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) must be equal or less than size of size\_t |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [retained\_mem.h](retained__mem_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
