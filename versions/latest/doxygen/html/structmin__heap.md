---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/structmin__heap.html
original_path: doxygen/html/structmin__heap.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

min\_heap Struct Reference

[Utilities](group__utilities.md) » [Data Structure APIs](group__datastructure__apis.md) » [Min-Heap service](group__min__heap__apis.md)

min-heap data structure with user-provided comparator.
[More...](#details)

`#include <[zephyr/sys/min_heap.h](min__heap_8h_source.md)>`

| Data Fields | |
| --- | --- |
| void \* | [storage](#a6e4bb0c9a3687938a8630f7cc93b728b) |
|  | Raw pointer to contiguous memory for elements. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [capacity](#afb0062bd8818c9184cd8469a3f95dc6d) |
|  | Maximum number of elements. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [elem\_size](#ab9d4b3b1a91fecef152576a47a1a0b10) |
|  | Size of each element. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [size](#a74824c3cda1d0e85f1712d9d9182922d) |
|  | Current elements count. |
| [min\_heap\_cmp\_t](group__min__heap__apis.md#ga638b9c8b6023ec281b1adcb9ca6ba814) | [cmp](#a1cde8c1bad1239b7a78b51c79b8f608d) |
|  | Comparator function. |

## Detailed Description

min-heap data structure with user-provided comparator.

## Field Documentation

## [◆ ](#afb0062bd8818c9184cd8469a3f95dc6d)capacity

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) min\_heap::capacity |
| --- |

Maximum number of elements.

## [◆ ](#a1cde8c1bad1239b7a78b51c79b8f608d)cmp

| [min\_heap\_cmp\_t](group__min__heap__apis.md#ga638b9c8b6023ec281b1adcb9ca6ba814) min\_heap::cmp |
| --- |

Comparator function.

## [◆ ](#ab9d4b3b1a91fecef152576a47a1a0b10)elem\_size

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) min\_heap::elem\_size |
| --- |

Size of each element.

## [◆ ](#a74824c3cda1d0e85f1712d9d9182922d)size

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) min\_heap::size |
| --- |

Current elements count.

## [◆ ](#a6e4bb0c9a3687938a8630f7cc93b728b)storage

| void\* min\_heap::storage |
| --- |

Raw pointer to contiguous memory for elements.

---

The documentation for this struct was generated from the following file:

- zephyr/sys/[min\_heap.h](min__heap_8h_source.md)

- [min\_heap](structmin__heap.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
