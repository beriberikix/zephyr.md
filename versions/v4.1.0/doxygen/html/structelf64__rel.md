---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structelf64__rel.html
original_path: doxygen/html/structelf64__rel.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

elf64\_rel Struct Reference

[Operating System Services](group__os__services.md) » [Linkable loadable extensions](group__llext__apis.md) » [ELF constants and data types](group__llext__elf.md)

Relocation entry for 64-bit ELFs.
[More...](#details)

`#include <[elf.h](llext_2elf_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [elf64\_addr](group__llext__elf.md#ga42c555ace34b21c1773c9e59228e9929) | [r\_offset](#a4fdfdc207826e470ba8affcdf149acc9) |
|  | Offset in the section to perform a relocation. |
| [elf64\_xword](group__llext__elf.md#ga68e4179ac3b1c52c28c6e3e5c2a1838a) | [r\_info](#aa861a3f29f7bd9a78d527de69baba00c) |
|  | Information about the relocation, related symbol and type. |

## Detailed Description

Relocation entry for 64-bit ELFs.

This structure stores information describing a relocation to be performed. Additional information about the relocation is stored at the location pointed to by [r\_offset](#a4fdfdc207826e470ba8affcdf149acc9).

## Field Documentation

## [◆ ](#aa861a3f29f7bd9a78d527de69baba00c)r\_info

| [elf64\_xword](group__llext__elf.md#ga68e4179ac3b1c52c28c6e3e5c2a1838a) elf64\_rel::r\_info |
| --- |

Information about the relocation, related symbol and type.

## [◆ ](#a4fdfdc207826e470ba8affcdf149acc9)r\_offset

| [elf64\_addr](group__llext__elf.md#ga42c555ace34b21c1773c9e59228e9929) elf64\_rel::r\_offset |
| --- |

Offset in the section to perform a relocation.

---

The documentation for this struct was generated from the following file:

- zephyr/llext/[elf.h](llext_2elf_8h_source.md)

- [elf64\_rel](structelf64__rel.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
