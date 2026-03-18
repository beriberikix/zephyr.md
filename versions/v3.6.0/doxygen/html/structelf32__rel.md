---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structelf32__rel.html
original_path: doxygen/html/structelf32__rel.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

elf32\_rel Struct Reference

[Operating System Services](group__os__services.md) » [Linkable loadable extensions](group__llext.md) » [ELF data types and defines](group__elf.md)

Relocation entry for 32-bit ELFs.
[More...](#details)

`#include <[elf.h](elf_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [elf32\_addr](group__elf.md#ga55f1dc601c95381307fddd5969969634) | [r\_offset](#a2bea1d7ef2a0c148cd9ae21386721f40) |
|  | Offset in the section to perform a relocation. |
| [elf32\_word](group__elf.md#gac786571f50a02299b19c1a16d658ea72) | [r\_info](#ac93ab16d071b87719651f517893bba97) |
|  | Information about the relocation, related symbol and type. |

## Detailed Description

Relocation entry for 32-bit ELFs.

## Field Documentation

## [◆ ](#ac93ab16d071b87719651f517893bba97)r\_info

| [elf32\_word](group__elf.md#gac786571f50a02299b19c1a16d658ea72) elf32\_rel::r\_info |
| --- |

Information about the relocation, related symbol and type.

## [◆ ](#a2bea1d7ef2a0c148cd9ae21386721f40)r\_offset

| [elf32\_addr](group__elf.md#ga55f1dc601c95381307fddd5969969634) elf32\_rel::r\_offset |
| --- |

Offset in the section to perform a relocation.

---

The documentation for this struct was generated from the following file:

- zephyr/llext/[elf.h](elf_8h_source.md)

- [elf32\_rel](structelf32__rel.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
