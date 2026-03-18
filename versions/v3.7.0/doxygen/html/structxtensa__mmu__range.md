---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structxtensa__mmu__range.html
original_path: doxygen/html/structxtensa__mmu__range.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

xtensa\_mmu\_range Struct Reference

[Xtensa APIs](group__xtensa__apis.md) » [Xtensa Memory Management Unit (MMU) APIs](group__xtensa__mmu__apis.md)

Struct used to map a memory region.
[More...](#details)

`#include <[xtensa_mmu.h](xtensa__mmu_8h_source.md)>`

| Data Fields | |
| --- | --- |
| const char \* | [name](#add09f00df98ae5c63084824dc070ef09) |
|  | Name of the memory region. |
| const [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [start](#ac525faa02c8886265e4118ce7cd80744) |
|  | Start address of the memory region. |
| const [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [end](#abc812bf633710dee5a8dcb19c522ad3f) |
|  | End address of the memory region. |
| const [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [attrs](#ac0ff0bdc3091d2bd8d1b48b8a383a9a5) |
|  | Attributes for the memory region. |

## Detailed Description

Struct used to map a memory region.

## Field Documentation

## [◆ ](#ac0ff0bdc3091d2bd8d1b48b8a383a9a5)attrs

| const [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) xtensa\_mmu\_range::attrs |
| --- |

Attributes for the memory region.

## [◆ ](#abc812bf633710dee5a8dcb19c522ad3f)end

| const [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) xtensa\_mmu\_range::end |
| --- |

End address of the memory region.

## [◆ ](#add09f00df98ae5c63084824dc070ef09)name

| const char\* xtensa\_mmu\_range::name |
| --- |

Name of the memory region.

## [◆ ](#ac525faa02c8886265e4118ce7cd80744)start

| const [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) xtensa\_mmu\_range::start |
| --- |

Start address of the memory region.

---

The documentation for this struct was generated from the following file:

- zephyr/arch/xtensa/[xtensa\_mmu.h](xtensa__mmu_8h_source.md)

- [xtensa\_mmu\_range](structxtensa__mmu__range.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
