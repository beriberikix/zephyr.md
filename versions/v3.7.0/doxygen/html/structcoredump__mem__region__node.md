---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structcoredump__mem__region__node.html
original_path: doxygen/html/structcoredump__mem__region__node.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

coredump\_mem\_region\_node Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [Coredump pseudo-device driver APIs](group__coredump__device__interface.md)

Structure describing a region in memory that may be stored in core dump at the time it is generated.
[More...](#details)

`#include <[coredump.h](drivers_2coredump_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) | [node](#a41fb46fe6748ee9d4a2a4b8cd2230000) |
|  | Node of single-linked list, do not modify. |
| [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | [start](#a997c7ba19516bdb6f9a97ee55f488454) |
|  | Address of start of memory region. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [size](#a85ebc1035439aff3a6a534ddd091c26e) |
|  | Size of memory region. |

## Detailed Description

Structure describing a region in memory that may be stored in core dump at the time it is generated.

Instances of this are passed to the [coredump\_device\_register\_memory()](group__coredump__device__interface.md#ga14ccecab2b077a32a0bc3bf4ec5df909 "Register a region of memory to be stored in core dump at the time it is generated.") and [coredump\_device\_unregister\_memory()](group__coredump__device__interface.md#gafd4e43696175eeb3ad1a2894df945530 "Unregister a region of memory to be stored in core dump at the time it is generated.") functions to indicate addition and removal of memory regions to be captured

## Field Documentation

## [◆ ](#a41fb46fe6748ee9d4a2a4b8cd2230000)node

| [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) coredump\_mem\_region\_node::node |
| --- |

Node of single-linked list, do not modify.

## [◆ ](#a85ebc1035439aff3a6a534ddd091c26e)size

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) coredump\_mem\_region\_node::size |
| --- |

Size of memory region.

## [◆ ](#a997c7ba19516bdb6f9a97ee55f488454)start

| [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) coredump\_mem\_region\_node::start |
| --- |

Address of start of memory region.

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[coredump.h](drivers_2coredump_8h_source.md)

- [coredump\_mem\_region\_node](structcoredump__mem__region__node.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
