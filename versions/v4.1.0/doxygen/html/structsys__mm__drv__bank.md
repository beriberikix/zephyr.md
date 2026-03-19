---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structsys__mm__drv__bank.html
original_path: doxygen/html/structsys__mm__drv__bank.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

sys\_mm\_drv\_bank Struct Reference

[Operating System Services](group__os__services.md) » [Memory Management](group__memory__management.md) » [Memory Banks Driver APIs](group__mm__drv__bank__apis.md)

Information about memory banks.
[More...](#details)

`#include <[mm_drv_bank.h](mm__drv__bank_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [unmapped\_pages](#a8fd91db4f69c273b2d26bb770292cd83) |
|  | Number of unmapped pages. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [mapped\_pages](#a2e84b41e42b801825aa694e569e8ad6c) |
|  | Number of mapped pages. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [max\_mapped\_pages](#a69f4b9f6a7fed6403e7271a4ecbe5ad1) |
|  | Maximum number of mapped pages since last counter reset. |

## Detailed Description

Information about memory banks.

## Field Documentation

## [◆ ](#a2e84b41e42b801825aa694e569e8ad6c)mapped\_pages

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) sys\_mm\_drv\_bank::mapped\_pages |
| --- |

Number of mapped pages.

## [◆ ](#a69f4b9f6a7fed6403e7271a4ecbe5ad1)max\_mapped\_pages

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) sys\_mm\_drv\_bank::max\_mapped\_pages |
| --- |

Maximum number of mapped pages since last counter reset.

## [◆ ](#a8fd91db4f69c273b2d26bb770292cd83)unmapped\_pages

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) sys\_mm\_drv\_bank::unmapped\_pages |
| --- |

Number of unmapped pages.

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/mm/[mm\_drv\_bank.h](mm__drv__bank_8h_source.md)

- [sys\_mm\_drv\_bank](structsys__mm__drv__bank.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
