---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structgdb__mem__region.html
original_path: doxygen/html/structgdb__mem__region.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

gdb\_mem\_region Struct Reference

Describe one memory region.
[More...](#details)

`#include <[gdbstub.h](debug_2gdbstub_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | [start](#a463465123fd373996a857b38c71474b3) |
|  | Start address of a memory region. |
| [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | [end](#a16001ef766b3c5775c1d1b2c59575b74) |
|  | End address of a memory region. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [attributes](#ad8ae6acf6950428a9846a25fb0219eeb) |
|  | Memory region attributes. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [alignment](#aa714bde657eb3572367a924298dd927f) |
|  | Read/write alignment, 0 if using default alignment. |

## Detailed Description

Describe one memory region.

## Field Documentation

## [◆ ](#aa714bde657eb3572367a924298dd927f)alignment

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) gdb\_mem\_region::alignment |
| --- |

Read/write alignment, 0 if using default alignment.

## [◆ ](#ad8ae6acf6950428a9846a25fb0219eeb)attributes

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) gdb\_mem\_region::attributes |
| --- |

Memory region attributes.

## [◆ ](#a16001ef766b3c5775c1d1b2c59575b74)end

| [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) gdb\_mem\_region::end |
| --- |

End address of a memory region.

## [◆ ](#a463465123fd373996a857b38c71474b3)start

| [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) gdb\_mem\_region::start |
| --- |

Start address of a memory region.

---

The documentation for this struct was generated from the following file:

- zephyr/debug/[gdbstub.h](debug_2gdbstub_8h_source.md)

- [gdb\_mem\_region](structgdb__mem__region.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
