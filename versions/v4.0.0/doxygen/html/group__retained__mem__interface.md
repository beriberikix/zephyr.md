---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/group__retained__mem__interface.html
original_path: doxygen/html/group__retained__mem__interface.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Retained memory driver interface

[Device Driver APIs](group__io__interfaces.md)

Retained memory driver interface.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [retained\_mem\_driver\_api](structretained__mem__driver__api.md) |
|  | Retained memory driver API API which can be used by a device to store data in a retained memory area. [More...](structretained__mem__driver__api.md#details) |

| Typedefs | |
| --- | --- |
| typedef [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118)(\* | [retained\_mem\_size\_api](#ga684490184eedc8d3f56b25d7b6e50a06)) (const struct [device](structdevice.md) \*dev) |
|  | Callback API to get size of retained memory area. |
| typedef int(\* | [retained\_mem\_read\_api](#ga3831f3ec0e0de7957cc6ce7da0cfbe58)) (const struct [device](structdevice.md) \*dev, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) offset, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buffer, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
|  | Callback API to read from retained memory area. |
| typedef int(\* | [retained\_mem\_write\_api](#gaf6e43d230b1a606e90f3a236aeff1909)) (const struct [device](structdevice.md) \*dev, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) offset, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buffer, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
|  | Callback API to write to retained memory area. |
| typedef int(\* | [retained\_mem\_clear\_api](#ga3fde220eceb8a45a7a42cfbb1930e27d)) (const struct [device](structdevice.md) \*dev) |
|  | Callback API to clear retained memory area (reset all data to 0x00). |

| Functions | |
| --- | --- |
| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) | [retained\_mem\_size](#gaa0b4b6db4c96054a709f803880f3091a) (const struct [device](structdevice.md) \*dev) |
|  | Returns the size of the retained memory area. |
| int | [retained\_mem\_read](#ga47fba21400c1f7019e7bd0e8f10662b3) (const struct [device](structdevice.md) \*dev, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) offset, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buffer, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
|  | Reads data from the Retained memory area. |
| int | [retained\_mem\_write](#ga1976ac945eb7c09b8dd6121926af0c6a) (const struct [device](structdevice.md) \*dev, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) offset, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buffer, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
|  | Writes data to the Retained memory area - underlying data does not need to be cleared prior to writing. |
| int | [retained\_mem\_clear](#ga5962d863c21cd91e259bf47abf2154d7) (const struct [device](structdevice.md) \*dev) |
|  | Clears data in the retained memory area by setting it to 0x00. |

## Detailed Description

Retained memory driver interface.

Since
:   3.4

Version
:   0.8.0

## Typedef Documentation

## [◆ ](#ga3fde220eceb8a45a7a42cfbb1930e27d)retained\_mem\_clear\_api

| typedef int(\* retained\_mem\_clear\_api) (const struct [device](structdevice.md) \*dev) |
| --- |

`#include <[retained_mem.h](retained__mem_8h.md)>`

Callback API to clear retained memory area (reset all data to 0x00).

See [retained\_mem\_clear()](#ga5962d863c21cd91e259bf47abf2154d7) for argument description.

## [◆ ](#ga3831f3ec0e0de7957cc6ce7da0cfbe58)retained\_mem\_read\_api

| typedef int(\* retained\_mem\_read\_api) (const struct [device](structdevice.md) \*dev, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) offset, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buffer, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
| --- |

`#include <[retained_mem.h](retained__mem_8h.md)>`

Callback API to read from retained memory area.

See [retained\_mem\_read()](#ga47fba21400c1f7019e7bd0e8f10662b3) for argument description.

## [◆ ](#ga684490184eedc8d3f56b25d7b6e50a06)retained\_mem\_size\_api

| typedef [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118)(\* retained\_mem\_size\_api) (const struct [device](structdevice.md) \*dev) |
| --- |

`#include <[retained_mem.h](retained__mem_8h.md)>`

Callback API to get size of retained memory area.

See [retained\_mem\_size()](#gaa0b4b6db4c96054a709f803880f3091a) for argument description.

## [◆ ](#gaf6e43d230b1a606e90f3a236aeff1909)retained\_mem\_write\_api

| typedef int(\* retained\_mem\_write\_api) (const struct [device](structdevice.md) \*dev, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) offset, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buffer, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
| --- |

`#include <[retained_mem.h](retained__mem_8h.md)>`

Callback API to write to retained memory area.

See [retained\_mem\_write()](#ga1976ac945eb7c09b8dd6121926af0c6a) for argument description.

## Function Documentation

## [◆ ](#ga5962d863c21cd91e259bf47abf2154d7)retained\_mem\_clear()

| int retained\_mem\_clear | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[retained_mem.h](retained__mem_8h.md)>`

Clears data in the retained memory area by setting it to 0x00.

Parameters
:   | dev | Retained memory device to use. |
    | --- | --- |

Return values
:   | 0 | on success else negative errno code. |
    | --- | --- |

## [◆ ](#ga47fba21400c1f7019e7bd0e8f10662b3)retained\_mem\_read()

| int retained\_mem\_read | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) | *offset*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *buffer*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *size* ) |

`#include <[retained_mem.h](retained__mem_8h.md)>`

Reads data from the Retained memory area.

Parameters
:   | dev | Retained memory device to use. |
    | --- | --- |
    | offset | Offset to read data from. |
    | buffer | Buffer to store read data in. |
    | size | Size of data to read. |

Return values
:   | 0 | on success else negative errno code. |
    | --- | --- |

## [◆ ](#gaa0b4b6db4c96054a709f803880f3091a)retained\_mem\_size()

| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) retained\_mem\_size | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[retained_mem.h](retained__mem_8h.md)>`

Returns the size of the retained memory area.

Parameters
:   | dev | Retained memory device to use. |
    | --- | --- |

Return values
:   | Positive | value indicating size in bytes on success, else negative errno code. |
    | --- | --- |

## [◆ ](#ga1976ac945eb7c09b8dd6121926af0c6a)retained\_mem\_write()

| int retained\_mem\_write | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) | *offset*, |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *buffer*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *size* ) |

`#include <[retained_mem.h](retained__mem_8h.md)>`

Writes data to the Retained memory area - underlying data does not need to be cleared prior to writing.

Parameters
:   | dev | Retained memory device to use. |
    | --- | --- |
    | offset | Offset to write data to. |
    | buffer | Data to write. |
    | size | Size of data to be written. |

Return values
:   | 0 | on success else negative errno code. |
    | --- | --- |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
