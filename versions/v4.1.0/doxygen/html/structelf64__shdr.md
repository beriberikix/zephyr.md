---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structelf64__shdr.html
original_path: doxygen/html/structelf64__shdr.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

elf64\_shdr Struct Reference

[Operating System Services](group__os__services.md) » [Linkable loadable extensions](group__llext__apis.md) » [ELF constants and data types](group__llext__elf.md)

Section Header(64-bit).
[More...](#details)

`#include <[elf.h](llext_2elf_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [elf64\_word](group__llext__elf.md#gaabf3a740e51b02fbaf40bedfba35e476) | [sh\_name](#af58da5c7c3e7712c51396eb937e1e783) |
|  | Section header name index in section header string table. |
| [elf64\_word](group__llext__elf.md#gaabf3a740e51b02fbaf40bedfba35e476) | [sh\_type](#adf7c73f78f13d52220246e1ae6f99129) |
|  | Section type. |
| [elf64\_xword](group__llext__elf.md#ga68e4179ac3b1c52c28c6e3e5c2a1838a) | [sh\_flags](#abd91eb8261ee67e50232e3682dc43267) |
|  | Section header attributes. |
| [elf64\_addr](group__llext__elf.md#ga42c555ace34b21c1773c9e59228e9929) | [sh\_addr](#a58c125037ae69e35f1f18c3e7aeef222) |
|  | Address of section in the image. |
| [elf64\_off](group__llext__elf.md#ga7f982d835a34713a84907873f9e058a9) | [sh\_offset](#a855b2f814e5b1127f3766ae44b1ded10) |
|  | Location of section in the ELF binary in bytes. |
| [elf64\_xword](group__llext__elf.md#ga68e4179ac3b1c52c28c6e3e5c2a1838a) | [sh\_size](#a283192781f8777274e0ed155b8caa52b) |
|  | Section size in bytes. |
| [elf64\_word](group__llext__elf.md#gaabf3a740e51b02fbaf40bedfba35e476) | [sh\_link](#a437c734872924c69bf3ea02723bfb50c) |
|  | Section header table link index, depends on section type. |
| [elf64\_word](group__llext__elf.md#gaabf3a740e51b02fbaf40bedfba35e476) | [sh\_info](#ab2d5b6d2b41c4b956917d2206b804335) |
|  | Section info, depends on section type. |
| [elf64\_xword](group__llext__elf.md#ga68e4179ac3b1c52c28c6e3e5c2a1838a) | [sh\_addralign](#a978b62673b2b26f9d6333f0a3ccd7cb2) |
|  | Section address alignment. |
| [elf64\_xword](group__llext__elf.md#ga68e4179ac3b1c52c28c6e3e5c2a1838a) | [sh\_entsize](#a41f5b8340cd4cb90b14cba348684d73b) |
|  | Section contains table of fixed size entries sh\_entsize bytes large. |

## Detailed Description

Section Header(64-bit).

## Field Documentation

## [◆ ](#a58c125037ae69e35f1f18c3e7aeef222)sh\_addr

| [elf64\_addr](group__llext__elf.md#ga42c555ace34b21c1773c9e59228e9929) elf64\_shdr::sh\_addr |
| --- |

Address of section in the image.

## [◆ ](#a978b62673b2b26f9d6333f0a3ccd7cb2)sh\_addralign

| [elf64\_xword](group__llext__elf.md#ga68e4179ac3b1c52c28c6e3e5c2a1838a) elf64\_shdr::sh\_addralign |
| --- |

Section address alignment.

## [◆ ](#a41f5b8340cd4cb90b14cba348684d73b)sh\_entsize

| [elf64\_xword](group__llext__elf.md#ga68e4179ac3b1c52c28c6e3e5c2a1838a) elf64\_shdr::sh\_entsize |
| --- |

Section contains table of fixed size entries sh\_entsize bytes large.

## [◆ ](#abd91eb8261ee67e50232e3682dc43267)sh\_flags

| [elf64\_xword](group__llext__elf.md#ga68e4179ac3b1c52c28c6e3e5c2a1838a) elf64\_shdr::sh\_flags |
| --- |

Section header attributes.

## [◆ ](#ab2d5b6d2b41c4b956917d2206b804335)sh\_info

| [elf64\_word](group__llext__elf.md#gaabf3a740e51b02fbaf40bedfba35e476) elf64\_shdr::sh\_info |
| --- |

Section info, depends on section type.

## [◆ ](#a437c734872924c69bf3ea02723bfb50c)sh\_link

| [elf64\_word](group__llext__elf.md#gaabf3a740e51b02fbaf40bedfba35e476) elf64\_shdr::sh\_link |
| --- |

Section header table link index, depends on section type.

## [◆ ](#af58da5c7c3e7712c51396eb937e1e783)sh\_name

| [elf64\_word](group__llext__elf.md#gaabf3a740e51b02fbaf40bedfba35e476) elf64\_shdr::sh\_name |
| --- |

Section header name index in section header string table.

## [◆ ](#a855b2f814e5b1127f3766ae44b1ded10)sh\_offset

| [elf64\_off](group__llext__elf.md#ga7f982d835a34713a84907873f9e058a9) elf64\_shdr::sh\_offset |
| --- |

Location of section in the ELF binary in bytes.

## [◆ ](#a283192781f8777274e0ed155b8caa52b)sh\_size

| [elf64\_xword](group__llext__elf.md#ga68e4179ac3b1c52c28c6e3e5c2a1838a) elf64\_shdr::sh\_size |
| --- |

Section size in bytes.

## [◆ ](#adf7c73f78f13d52220246e1ae6f99129)sh\_type

| [elf64\_word](group__llext__elf.md#gaabf3a740e51b02fbaf40bedfba35e476) elf64\_shdr::sh\_type |
| --- |

Section type.

---

The documentation for this struct was generated from the following file:

- zephyr/llext/[elf.h](llext_2elf_8h_source.md)

- [elf64\_shdr](structelf64__shdr.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
