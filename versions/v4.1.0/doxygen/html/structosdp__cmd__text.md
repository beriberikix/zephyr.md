---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structosdp__cmd__text.html
original_path: doxygen/html/structosdp__cmd__text.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

osdp\_cmd\_text Struct Reference

Command to manipulate any display units that the PD supports.
[More...](#details)

`#include <[osdp.h](osdp_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [reader](#a3fa3d0780aa98542a270f6bdb6f49737) |
|  | Reader number. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [control\_code](#a46fe3f66e01229e763a6f06bd8bdfab8) |
|  | Control code. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [temp\_time](#acde9abcb023eb77845af8ea0935e63fa) |
|  | Duration to display temporary text, in seconds. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [offset\_row](#a16f11f35eacb2876b09d148349b7ed3c) |
|  | Row to display the first character (1-indexed). |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [offset\_col](#a5e7b4c03b1649d8edbf53932ee90f7b3) |
|  | Column to display the first character (1-indexed). |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [length](#a4dcdd83d3b8d424533ca997111f5cd94) |
|  | Number of characters in the string. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [data](#a3a94fa8b18d18845b60476148e2b7325) [32] |
|  | The string to display. |

## Detailed Description

Command to manipulate any display units that the PD supports.

## Field Documentation

## [◆ ](#a46fe3f66e01229e763a6f06bd8bdfab8)control\_code

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) osdp\_cmd\_text::control\_code |
| --- |

Control code.

- 1 - permanent text, no wrap
- 2 - permanent text, with wrap
- 3 - temp text, no wrap
- 4 - temp text, with wrap

## [◆ ](#a3a94fa8b18d18845b60476148e2b7325)data

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) osdp\_cmd\_text::data[32] |
| --- |

The string to display.

## [◆ ](#a4dcdd83d3b8d424533ca997111f5cd94)length

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) osdp\_cmd\_text::length |
| --- |

Number of characters in the string.

## [◆ ](#a5e7b4c03b1649d8edbf53932ee90f7b3)offset\_col

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) osdp\_cmd\_text::offset\_col |
| --- |

Column to display the first character (1-indexed).

## [◆ ](#a16f11f35eacb2876b09d148349b7ed3c)offset\_row

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) osdp\_cmd\_text::offset\_row |
| --- |

Row to display the first character (1-indexed).

## [◆ ](#a3fa3d0780aa98542a270f6bdb6f49737)reader

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) osdp\_cmd\_text::reader |
| --- |

Reader number.

0 = First Reader, 1 = Second Reader, etc.

## [◆ ](#acde9abcb023eb77845af8ea0935e63fa)temp\_time

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) osdp\_cmd\_text::temp\_time |
| --- |

Duration to display temporary text, in seconds.

---

The documentation for this struct was generated from the following file:

- zephyr/mgmt/[osdp.h](osdp_8h_source.md)

- [osdp\_cmd\_text](structosdp__cmd__text.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
