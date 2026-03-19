---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structelf32__rel.html
original_path: doxygen/html/structelf32__rel.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

elf32\_rel Struct Reference

[Operating System Services](group__os__services.md) » [Linkable loadable extensions](group__llext__apis.md) » [ELF constants and data types](group__llext__elf.md)

Relocation entry for 32-bit ELFs.
[More...](#details)

`#include <[elf.h](llext_2elf_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [elf32\_addr](group__llext__elf.md#ga55f1dc601c95381307fddd5969969634) | [r\_offset](#a2bea1d7ef2a0c148cd9ae21386721f40) |
|  | Offset in the section to perform a relocation. |
| [elf32\_word](group__llext__elf.md#gac786571f50a02299b19c1a16d658ea72) | [r\_info](#ac93ab16d071b87719651f517893bba97) |
|  | Information about the relocation, related symbol and type. |

## Detailed Description

Relocation entry for 32-bit ELFs.

This structure stores information describing a relocation to be performed. Additional information about the relocation is stored at the location pointed to by [r\_offset](#a2bea1d7ef2a0c148cd9ae21386721f40).

## Field Documentation

## [◆ ](#ac93ab16d071b87719651f517893bba97)r\_info

| [elf32\_word](group__llext__elf.md#gac786571f50a02299b19c1a16d658ea72) elf32\_rel::r\_info |
| --- |

Information about the relocation, related symbol and type.

## [◆ ](#a2bea1d7ef2a0c148cd9ae21386721f40)r\_offset

| [elf32\_addr](group__llext__elf.md#ga55f1dc601c95381307fddd5969969634) elf32\_rel::r\_offset |
| --- |

Offset in the section to perform a relocation.

---

The documentation for this struct was generated from the following file:

- zephyr/llext/[elf.h](llext_2elf_8h_source.md)

- [elf32\_rel](structelf32__rel.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
