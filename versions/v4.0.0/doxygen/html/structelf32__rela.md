---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structelf32__rela.html
original_path: doxygen/html/structelf32__rela.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

elf32\_rela Struct Reference

[Operating System Services](group__os__services.md) » [Linkable loadable extensions](group__llext__apis.md) » [ELF constants and data types](group__llext__elf.md)

Relocation entry for 32-bit ELFs with addend.
[More...](#details)

`#include <[elf.h](llext_2elf_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [elf32\_addr](group__llext__elf.md#ga55f1dc601c95381307fddd5969969634) | [r\_offset](#a4ef1961410f1b9ffea15615e03b3917b) |
|  | Offset in the section to perform a relocation. |
| [elf32\_word](group__llext__elf.md#gac786571f50a02299b19c1a16d658ea72) | [r\_info](#a4c3494d4b7abfec309895dff1891a466) |
|  | Information about the relocation, related symbol and type. |
| [elf32\_sword](group__llext__elf.md#ga1325c85290908b89a9c2b9bdd1aa2efd) | [r\_addend](#a37fce330c497dba2ca15c69cc58b83b8) |
|  | Offset to be applied to the symbol address. |

## Detailed Description

Relocation entry for 32-bit ELFs with addend.

This structure stores information describing a relocation to be performed.

## Field Documentation

## [◆ ](#a37fce330c497dba2ca15c69cc58b83b8)r\_addend

| [elf32\_sword](group__llext__elf.md#ga1325c85290908b89a9c2b9bdd1aa2efd) elf32\_rela::r\_addend |
| --- |

Offset to be applied to the symbol address.

## [◆ ](#a4c3494d4b7abfec309895dff1891a466)r\_info

| [elf32\_word](group__llext__elf.md#gac786571f50a02299b19c1a16d658ea72) elf32\_rela::r\_info |
| --- |

Information about the relocation, related symbol and type.

## [◆ ](#a4ef1961410f1b9ffea15615e03b3917b)r\_offset

| [elf32\_addr](group__llext__elf.md#ga55f1dc601c95381307fddd5969969634) elf32\_rela::r\_offset |
| --- |

Offset in the section to perform a relocation.

---

The documentation for this struct was generated from the following file:

- zephyr/llext/[elf.h](llext_2elf_8h_source.md)

- [elf32\_rela](structelf32__rela.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
