---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structllext__load__param.html
original_path: doxygen/html/structllext__load__param.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

llext\_load\_param Struct Reference

[Operating System Services](group__os__services.md) » [Linkable loadable extensions](group__llext__apis.md)

Advanced llext\_load parameters.
[More...](#details)

`#include <[llext.h](llext_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [relocate\_local](#a3c1683b0baafc636af18df3808d08031) |
|  | Perform local relocation. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [pre\_located](#a5e9fdb238b8a706155a873e82e35393d) |
|  | Use the virtual symbol addresses from the ELF, not addresses within the memory buffer, when calculating relocation targets. |

## Detailed Description

Advanced llext\_load parameters.

This structure contains advanced parameters for [llext\_load](group__llext__apis.md#ga93c7d7f8987bd25e3dc486943785c8a1 "llext_load").

## Field Documentation

## [◆ ](#a5e9fdb238b8a706155a873e82e35393d)pre\_located

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) llext\_load\_param::pre\_located |
| --- |

Use the virtual symbol addresses from the ELF, not addresses within the memory buffer, when calculating relocation targets.

## [◆ ](#a3c1683b0baafc636af18df3808d08031)relocate\_local

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) llext\_load\_param::relocate\_local |
| --- |

Perform local relocation.

---

The documentation for this struct was generated from the following file:

- zephyr/llext/[llext.h](llext_8h_source.md)

- [llext\_load\_param](structllext__load__param.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
