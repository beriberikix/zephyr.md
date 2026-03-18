---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structxtensa__mpu__range.html
original_path: doxygen/html/structxtensa__mpu__range.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

xtensa\_mpu\_range Struct Reference

[Xtensa APIs](group__xtensa__apis.md) » [Xtensa Memory Protection Unit (MPU) APIs](group__xtensa__mpu__apis.md)

Struct to describe a memory region [start, end).
[More...](#details)

`#include <[mpu.h](xtensa_2mpu_8h_source.md)>`

| Data Fields | |
| --- | --- |
| const [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | [start](#a3b24cd5cc1e5674193e7c1c20db2e66c) |
|  | Start address (inclusive) of the memory region. |
| const [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | [end](#a52444106e5fb335079ca1ed5428b1711) |
|  | End address (exclusive) of the memory region. |
| const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [access\_rights](#a21f446bdde0d194d3d4012342e49d151):4 |
|  | Access rights for the memory region. |
| const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [memory\_type](#a98cbc6ec1cb0b3440e8d58e12020cd1e):9 |
|  | Memory type for the region. |

## Detailed Description

Struct to describe a memory region [start, end).

## Field Documentation

## [◆ ](#a21f446bdde0d194d3d4012342e49d151)access\_rights

| const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) xtensa\_mpu\_range::access\_rights |
| --- |

Access rights for the memory region.

## [◆ ](#a52444106e5fb335079ca1ed5428b1711)end

| const [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) xtensa\_mpu\_range::end |
| --- |

End address (exclusive) of the memory region.

Use 0xFFFFFFFF for the end of memory.

## [◆ ](#a98cbc6ec1cb0b3440e8d58e12020cd1e)memory\_type

| const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) xtensa\_mpu\_range::memory\_type |
| --- |

Memory type for the region.

Refer to the Xtensa Instruction Set Architecture (ISA) manual for general description, and the processor manual for processor specific information.

## [◆ ](#a3b24cd5cc1e5674193e7c1c20db2e66c)start

| const [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) xtensa\_mpu\_range::start |
| --- |

Start address (inclusive) of the memory region.

---

The documentation for this struct was generated from the following file:

- zephyr/arch/xtensa/[mpu.h](xtensa_2mpu_8h_source.md)

- [xtensa\_mpu\_range](structxtensa__mpu__range.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
