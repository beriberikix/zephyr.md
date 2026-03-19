---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structllext__load__param.html
original_path: doxygen/html/structllext__load__param.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
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
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)(\* | [section\_detached](#af3d61fa83c93361e4c5292b078d51a93) )(const [elf\_shdr\_t](group__llext__elf.md#gab3695edd628cf868dc4f0d618f86bcbd) \*shdr) |
|  | Extensions can implement custom ELF sections to be loaded in specific memory regions, detached from other sections of compatible types. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [keep\_section\_info](#ae8e62920c8f47e7d2bcf7b7309058fb7) |
|  | Keep the ELF section data in memory after loading the extension. |

## Detailed Description

Advanced llext\_load parameters.

This structure contains advanced parameters for [llext\_load](group__llext__apis.md#ga0a4c3db30bc3ec7aa8a9b0e076af7157 "llext_load").

## Field Documentation

## [◆ ](#ae8e62920c8f47e7d2bcf7b7309058fb7)keep\_section\_info

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) llext\_load\_param::keep\_section\_info |
| --- |

Keep the ELF section data in memory after loading the extension.

This is needed to use some of the functions in [ELF inspection APIs](group__llext__inspect__apis.md "ELF inspection APIs").

Note
:   Related memory must be freed by [llext\_free\_inspection\_data](group__llext__apis.md#ga54f3aaed749e8c6bad6fbecb1622ab06 "llext_free_inspection_data") before the extension can be unloaded via [llext\_unload](group__llext__apis.md#gad3df7ed4d436846504c0047166eb929e "llext_unload").

## [◆ ](#a5e9fdb238b8a706155a873e82e35393d)pre\_located

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) llext\_load\_param::pre\_located |
| --- |

Use the virtual symbol addresses from the ELF, not addresses within the memory buffer, when calculating relocation targets.

It also means, that the application will take care to place the extension at those pre-defined addresses, so the LLEXT core doesn't have to do any allocation and copying internally.

## [◆ ](#a3c1683b0baafc636af18df3808d08031)relocate\_local

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) llext\_load\_param::relocate\_local |
| --- |

Perform local relocation.

## [◆ ](#af3d61fa83c93361e4c5292b078d51a93)section\_detached

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)(\* llext\_load\_param::section\_detached) (const [elf\_shdr\_t](group__llext__elf.md#gab3695edd628cf868dc4f0d618f86bcbd) \*shdr) |
| --- |

Extensions can implement custom ELF sections to be loaded in specific memory regions, detached from other sections of compatible types.

This optional callback checks whether a section should be detached.

---

The documentation for this struct was generated from the following file:

- zephyr/llext/[llext.h](llext_8h_source.md)

- [llext\_load\_param](structllext__load__param.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
