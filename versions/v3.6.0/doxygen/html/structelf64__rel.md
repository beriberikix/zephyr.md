---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structelf64__rel.html
original_path: doxygen/html/structelf64__rel.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

elf64\_rel Struct Reference

[Operating System Services](group__os__services.md) » [Linkable loadable extensions](group__llext.md) » [ELF data types and defines](group__elf.md)

Relocation entry for 64-bit ELFs.
[More...](#details)

`#include <[elf.h](elf_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [elf64\_addr](group__elf.md#ga42c555ace34b21c1773c9e59228e9929) | [r\_offset](#a4fdfdc207826e470ba8affcdf149acc9) |
|  | Offset in section to perform a relocation. |
| [elf64\_xword](group__elf.md#ga68e4179ac3b1c52c28c6e3e5c2a1838a) | [r\_info](#aa861a3f29f7bd9a78d527de69baba00c) |
|  | Information about relocation, related symbol and type. |

## Detailed Description

Relocation entry for 64-bit ELFs.

## Field Documentation

## [◆ ](#aa861a3f29f7bd9a78d527de69baba00c)r\_info

| [elf64\_xword](group__elf.md#ga68e4179ac3b1c52c28c6e3e5c2a1838a) elf64\_rel::r\_info |
| --- |

Information about relocation, related symbol and type.

## [◆ ](#a4fdfdc207826e470ba8affcdf149acc9)r\_offset

| [elf64\_addr](group__elf.md#ga42c555ace34b21c1773c9e59228e9929) elf64\_rel::r\_offset |
| --- |

Offset in section to perform a relocation.

---

The documentation for this struct was generated from the following file:

- zephyr/llext/[elf.h](elf_8h_source.md)

- [elf64\_rel](structelf64__rel.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
