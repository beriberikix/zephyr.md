---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structk__mem__partition.html
original_path: doxygen/html/structk__mem__partition.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

k\_mem\_partition Struct Reference

[Kernel APIs](group__kernel__apis.md) » [Memory domain APIs](group__mem__domain__apis.md)

Memory Partition.
[More...](#details)

`#include <[mem_domain.h](mem__domain_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | [start](#a654d19bfd6a1154f410ac6f3c481c5b7) |
|  | start address of memory partition |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [size](#ab3cb68302158f3dced41dbff4cbb226c) |
|  | size of memory partition |
| [k\_mem\_partition\_attr\_t](structk__mem__partition__attr__t.md) | [attr](#ada951ba1ec9429c98c16761e3093eedb) |
|  | attribute of memory partition |

## Detailed Description

Memory Partition.

A memory partition is a region of memory in the linear address space with a specific access policy.

The alignment of the starting address, and the alignment of the size value may have varying requirements based on the capabilities of the underlying memory management hardware; arbitrary values are unlikely to work.

## Field Documentation

## [◆ ](#ada951ba1ec9429c98c16761e3093eedb)attr

| [k\_mem\_partition\_attr\_t](structk__mem__partition__attr__t.md) k\_mem\_partition::attr |
| --- |

attribute of memory partition

## [◆ ](#ab3cb68302158f3dced41dbff4cbb226c)size

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) k\_mem\_partition::size |
| --- |

size of memory partition

## [◆ ](#a654d19bfd6a1154f410ac6f3c481c5b7)start

| [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) k\_mem\_partition::start |
| --- |

start address of memory partition

---

The documentation for this struct was generated from the following file:

- zephyr/app\_memory/[mem\_domain.h](mem__domain_8h_source.md)

- [k\_mem\_partition](structk__mem__partition.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
