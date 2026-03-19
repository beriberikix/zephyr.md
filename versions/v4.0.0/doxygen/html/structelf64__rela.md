---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structelf64__rela.html
original_path: doxygen/html/structelf64__rela.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

elf64\_rela Struct Reference

[Operating System Services](group__os__services.md) » [Linkable loadable extensions](group__llext__apis.md) » [ELF constants and data types](group__llext__elf.md)

Relocation entry for 64-bit ELFs with addend.
[More...](#details)

`#include <[elf.h](llext_2elf_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [elf64\_addr](group__llext__elf.md#ga42c555ace34b21c1773c9e59228e9929) | [r\_offset](#a5fd82462e8b9c0eeaf84a00bc2aae3a4) |
|  | Offset in the section to perform a relocation. |
| [elf64\_xword](group__llext__elf.md#ga68e4179ac3b1c52c28c6e3e5c2a1838a) | [r\_info](#aa58223032a48222e420b36b2fc5f27ab) |
|  | Information about the relocation, related symbol and type. |
| [elf64\_sxword](group__llext__elf.md#ga3e687a252b2bb6ed11ea9bc2fa6b728e) | [r\_addend](#a3eda7390faab39b1974174cc839cfb22) |
|  | Offset to be applied to the symbol address. |

## Detailed Description

Relocation entry for 64-bit ELFs with addend.

This structure stores information describing a relocation to be performed.

## Field Documentation

## [◆ ](#a3eda7390faab39b1974174cc839cfb22)r\_addend

| [elf64\_sxword](group__llext__elf.md#ga3e687a252b2bb6ed11ea9bc2fa6b728e) elf64\_rela::r\_addend |
| --- |

Offset to be applied to the symbol address.

## [◆ ](#aa58223032a48222e420b36b2fc5f27ab)r\_info

| [elf64\_xword](group__llext__elf.md#ga68e4179ac3b1c52c28c6e3e5c2a1838a) elf64\_rela::r\_info |
| --- |

Information about the relocation, related symbol and type.

## [◆ ](#a5fd82462e8b9c0eeaf84a00bc2aae3a4)r\_offset

| [elf64\_addr](group__llext__elf.md#ga42c555ace34b21c1773c9e59228e9929) elf64\_rela::r\_offset |
| --- |

Offset in the section to perform a relocation.

---

The documentation for this struct was generated from the following file:

- zephyr/llext/[elf.h](llext_2elf_8h_source.md)

- [elf64\_rela](structelf64__rela.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
