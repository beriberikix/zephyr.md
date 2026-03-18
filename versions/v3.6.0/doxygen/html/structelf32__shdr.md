---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structelf32__shdr.html
original_path: doxygen/html/structelf32__shdr.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

elf32\_shdr Struct Reference

[Operating System Services](group__os__services.md) » [Linkable loadable extensions](group__llext.md) » [ELF data types and defines](group__elf.md)

Section Header(32-bit).
[More...](#details)

`#include <[elf.h](elf_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [elf32\_word](group__elf.md#gac786571f50a02299b19c1a16d658ea72) | [sh\_name](#a397da5153b2f7605b1ff1de6aefa6d72) |
|  | Section header name index in section header string table. |
| [elf32\_word](group__elf.md#gac786571f50a02299b19c1a16d658ea72) | [sh\_type](#a575fd441213a3a2c01a2b9f8d76ae91a) |
|  | Section type. |
| [elf32\_word](group__elf.md#gac786571f50a02299b19c1a16d658ea72) | [sh\_flags](#a812f8d63ce30897a2aafc8eecca004af) |
|  | Section header attributes. |
| [elf32\_addr](group__elf.md#ga55f1dc601c95381307fddd5969969634) | [sh\_addr](#a2f5302ddbc6ae2e7adc9d0747029ac07) |
|  | Address of section in the image. |
| [elf32\_off](group__elf.md#gabb40eb5ffbe88010885da1c8c7b869e3) | [sh\_offset](#ac7185a5c368b86d7c5bde4261472d3ea) |
|  | Location of section in the ELF binary in bytes. |
| [elf32\_word](group__elf.md#gac786571f50a02299b19c1a16d658ea72) | [sh\_size](#a99ef99ad56321d429d78a0d51fa55bc5) |
|  | Section size in bytes. |
| [elf32\_word](group__elf.md#gac786571f50a02299b19c1a16d658ea72) | [sh\_link](#afc854954cb010c23281293399a58c200) |
|  | Section header table link index, depends on section type. |
| [elf32\_word](group__elf.md#gac786571f50a02299b19c1a16d658ea72) | [sh\_info](#aa01fa67d235a73d8f05a1082ff639825) |
|  | Section info, depends on section type. |
| [elf32\_word](group__elf.md#gac786571f50a02299b19c1a16d658ea72) | [sh\_addralign](#ab0d2f72391dd49af989bc4a96320e510) |
|  | Section address alignment. |
| [elf32\_word](group__elf.md#gac786571f50a02299b19c1a16d658ea72) | [sh\_entsize](#af97a639e2da493a81e104447e327b574) |
|  | Section contains table of fixed size entries sh\_entsize bytes large. |

## Detailed Description

Section Header(32-bit).

## Field Documentation

## [◆ ](#a2f5302ddbc6ae2e7adc9d0747029ac07)sh\_addr

| [elf32\_addr](group__elf.md#ga55f1dc601c95381307fddd5969969634) elf32\_shdr::sh\_addr |
| --- |

Address of section in the image.

## [◆ ](#ab0d2f72391dd49af989bc4a96320e510)sh\_addralign

| [elf32\_word](group__elf.md#gac786571f50a02299b19c1a16d658ea72) elf32\_shdr::sh\_addralign |
| --- |

Section address alignment.

## [◆ ](#af97a639e2da493a81e104447e327b574)sh\_entsize

| [elf32\_word](group__elf.md#gac786571f50a02299b19c1a16d658ea72) elf32\_shdr::sh\_entsize |
| --- |

Section contains table of fixed size entries sh\_entsize bytes large.

## [◆ ](#a812f8d63ce30897a2aafc8eecca004af)sh\_flags

| [elf32\_word](group__elf.md#gac786571f50a02299b19c1a16d658ea72) elf32\_shdr::sh\_flags |
| --- |

Section header attributes.

## [◆ ](#aa01fa67d235a73d8f05a1082ff639825)sh\_info

| [elf32\_word](group__elf.md#gac786571f50a02299b19c1a16d658ea72) elf32\_shdr::sh\_info |
| --- |

Section info, depends on section type.

## [◆ ](#afc854954cb010c23281293399a58c200)sh\_link

| [elf32\_word](group__elf.md#gac786571f50a02299b19c1a16d658ea72) elf32\_shdr::sh\_link |
| --- |

Section header table link index, depends on section type.

## [◆ ](#a397da5153b2f7605b1ff1de6aefa6d72)sh\_name

| [elf32\_word](group__elf.md#gac786571f50a02299b19c1a16d658ea72) elf32\_shdr::sh\_name |
| --- |

Section header name index in section header string table.

## [◆ ](#ac7185a5c368b86d7c5bde4261472d3ea)sh\_offset

| [elf32\_off](group__elf.md#gabb40eb5ffbe88010885da1c8c7b869e3) elf32\_shdr::sh\_offset |
| --- |

Location of section in the ELF binary in bytes.

## [◆ ](#a99ef99ad56321d429d78a0d51fa55bc5)sh\_size

| [elf32\_word](group__elf.md#gac786571f50a02299b19c1a16d658ea72) elf32\_shdr::sh\_size |
| --- |

Section size in bytes.

## [◆ ](#a575fd441213a3a2c01a2b9f8d76ae91a)sh\_type

| [elf32\_word](group__elf.md#gac786571f50a02299b19c1a16d658ea72) elf32\_shdr::sh\_type |
| --- |

Section type.

---

The documentation for this struct was generated from the following file:

- zephyr/llext/[elf.h](elf_8h_source.md)

- [elf32\_shdr](structelf32__shdr.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
