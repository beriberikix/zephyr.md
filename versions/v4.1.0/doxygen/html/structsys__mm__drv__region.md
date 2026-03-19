---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structsys__mm__drv__region.html
original_path: doxygen/html/structsys__mm__drv__region.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

sys\_mm\_drv\_region Struct Reference

[Operating System Services](group__os__services.md) » [Memory Management](group__memory__management.md) » [Memory Management Driver APIs](group__mm__drv__apis.md)

Represents an available memory region.
[More...](#details)

`#include <[system_mm.h](system__mm_8h_source.md)>`

| Data Fields | |
| --- | --- |
| void \* | [addr](#a8dfa465f83cf5f6115094b6b5727f418) |
|  | Address of the memory region. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [size](#a5b48a908a5393fec377edcd3760c18ad) |
|  | Size of the memory region. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [attr](#a6838fe4bd4daab440152c4d666a4597d) |
|  | Driver defined attributes of the memory region. |

## Detailed Description

Represents an available memory region.

A memory region that can be used by allocators. Driver defined attributes can be used to guide the proper usage of each region.

## Field Documentation

## [◆ ](#a8dfa465f83cf5f6115094b6b5727f418)addr

| void\* sys\_mm\_drv\_region::addr |
| --- |

Address of the memory region.

## [◆ ](#a6838fe4bd4daab440152c4d666a4597d)attr

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) sys\_mm\_drv\_region::attr |
| --- |

Driver defined attributes of the memory region.

## [◆ ](#a5b48a908a5393fec377edcd3760c18ad)size

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) sys\_mm\_drv\_region::size |
| --- |

Size of the memory region.

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/mm/[system\_mm.h](system__mm_8h_source.md)

- [sys\_mm\_drv\_region](structsys__mm__drv__region.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
