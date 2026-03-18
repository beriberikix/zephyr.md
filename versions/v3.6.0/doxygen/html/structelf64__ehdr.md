---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structelf64__ehdr.html
original_path: doxygen/html/structelf64__ehdr.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

elf64\_ehdr Struct Reference

[Operating System Services](group__os__services.md) » [Linkable loadable extensions](group__llext.md) » [ELF data types and defines](group__elf.md)

ELF Header(64-bit).
[More...](#details)

`#include <[elf.h](elf_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) char | [e\_ident](#acfc6d7c908c9a9864cca2eb0e5a2c023) [16] |
|  | Magic string identifying ELF binary. |
| [elf64\_half](group__elf.md#ga3358e1392fd861af8a7c8248519717a0) | [e\_type](#aa30814b4908ab8f0008f8b6a68686127) |
|  | Type of ELF. |
| [elf64\_half](group__elf.md#ga3358e1392fd861af8a7c8248519717a0) | [e\_machine](#ac1c3b8c0f2b01d0edf07c0e3d1d8220b) |
|  | Machine type. |
| [elf64\_word](group__elf.md#gaabf3a740e51b02fbaf40bedfba35e476) | [e\_version](#a8d406a8c636ad09b96af62001b9b1785) |
|  | Object file version. |
| [elf64\_addr](group__elf.md#ga42c555ace34b21c1773c9e59228e9929) | [e\_entry](#a26fa9b30280c40d71227cd8dc68cc042) |
|  | Virtual address of entry. |
| [elf64\_off](group__elf.md#ga7f982d835a34713a84907873f9e058a9) | [e\_phoff](#ab41df1d736aabf7b810339d579e51663) |
|  | Program header table offset. |
| [elf64\_off](group__elf.md#ga7f982d835a34713a84907873f9e058a9) | [e\_shoff](#a3566424cae4237c11dc781929e9d2396) |
|  | Section header table offset. |
| [elf64\_word](group__elf.md#gaabf3a740e51b02fbaf40bedfba35e476) | [e\_flags](#a7bdfcb1ae2d8dc7b6ba95e24e7e72ba9) |
|  | Processor specific flags. |
| [elf64\_half](group__elf.md#ga3358e1392fd861af8a7c8248519717a0) | [e\_ehsize](#a7ee0e5959ca93262320c545a4ab11649) |
|  | ELF header size. |
| [elf64\_half](group__elf.md#ga3358e1392fd861af8a7c8248519717a0) | [e\_phentsize](#a688f9d25b4f2678f0e9a313a8c8cf074) |
|  | Program header size. |
| [elf64\_half](group__elf.md#ga3358e1392fd861af8a7c8248519717a0) | [e\_phnum](#a4a3b62575f891b59851b36f478e95c32) |
|  | Program header count. |
| [elf64\_half](group__elf.md#ga3358e1392fd861af8a7c8248519717a0) | [e\_shentsize](#a419a672788fb33eaffc5f7eb7c9f9acd) |
|  | Section header size. |
| [elf64\_half](group__elf.md#ga3358e1392fd861af8a7c8248519717a0) | [e\_shnum](#ad46c9c2047e61617d5d52394e9c42d65) |
|  | Section header count. |
| [elf64\_half](group__elf.md#ga3358e1392fd861af8a7c8248519717a0) | [e\_shstrndx](#a6214fd0ea2f0d3e8151a304d5c4302b2) |
|  | Section header containing section header string table. |

## Detailed Description

ELF Header(64-bit).

## Field Documentation

## [◆ ](#a7ee0e5959ca93262320c545a4ab11649)e\_ehsize

| [elf64\_half](group__elf.md#ga3358e1392fd861af8a7c8248519717a0) elf64\_ehdr::e\_ehsize |
| --- |

ELF header size.

## [◆ ](#a26fa9b30280c40d71227cd8dc68cc042)e\_entry

| [elf64\_addr](group__elf.md#ga42c555ace34b21c1773c9e59228e9929) elf64\_ehdr::e\_entry |
| --- |

Virtual address of entry.

## [◆ ](#a7bdfcb1ae2d8dc7b6ba95e24e7e72ba9)e\_flags

| [elf64\_word](group__elf.md#gaabf3a740e51b02fbaf40bedfba35e476) elf64\_ehdr::e\_flags |
| --- |

Processor specific flags.

## [◆ ](#acfc6d7c908c9a9864cca2eb0e5a2c023)e\_ident

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) char elf64\_ehdr::e\_ident[16] |
| --- |

Magic string identifying ELF binary.

## [◆ ](#ac1c3b8c0f2b01d0edf07c0e3d1d8220b)e\_machine

| [elf64\_half](group__elf.md#ga3358e1392fd861af8a7c8248519717a0) elf64\_ehdr::e\_machine |
| --- |

Machine type.

## [◆ ](#a688f9d25b4f2678f0e9a313a8c8cf074)e\_phentsize

| [elf64\_half](group__elf.md#ga3358e1392fd861af8a7c8248519717a0) elf64\_ehdr::e\_phentsize |
| --- |

Program header size.

## [◆ ](#a4a3b62575f891b59851b36f478e95c32)e\_phnum

| [elf64\_half](group__elf.md#ga3358e1392fd861af8a7c8248519717a0) elf64\_ehdr::e\_phnum |
| --- |

Program header count.

## [◆ ](#ab41df1d736aabf7b810339d579e51663)e\_phoff

| [elf64\_off](group__elf.md#ga7f982d835a34713a84907873f9e058a9) elf64\_ehdr::e\_phoff |
| --- |

Program header table offset.

## [◆ ](#a419a672788fb33eaffc5f7eb7c9f9acd)e\_shentsize

| [elf64\_half](group__elf.md#ga3358e1392fd861af8a7c8248519717a0) elf64\_ehdr::e\_shentsize |
| --- |

Section header size.

## [◆ ](#ad46c9c2047e61617d5d52394e9c42d65)e\_shnum

| [elf64\_half](group__elf.md#ga3358e1392fd861af8a7c8248519717a0) elf64\_ehdr::e\_shnum |
| --- |

Section header count.

## [◆ ](#a3566424cae4237c11dc781929e9d2396)e\_shoff

| [elf64\_off](group__elf.md#ga7f982d835a34713a84907873f9e058a9) elf64\_ehdr::e\_shoff |
| --- |

Section header table offset.

## [◆ ](#a6214fd0ea2f0d3e8151a304d5c4302b2)e\_shstrndx

| [elf64\_half](group__elf.md#ga3358e1392fd861af8a7c8248519717a0) elf64\_ehdr::e\_shstrndx |
| --- |

Section header containing section header string table.

## [◆ ](#aa30814b4908ab8f0008f8b6a68686127)e\_type

| [elf64\_half](group__elf.md#ga3358e1392fd861af8a7c8248519717a0) elf64\_ehdr::e\_type |
| --- |

Type of ELF.

## [◆ ](#a8d406a8c636ad09b96af62001b9b1785)e\_version

| [elf64\_word](group__elf.md#gaabf3a740e51b02fbaf40bedfba35e476) elf64\_ehdr::e\_version |
| --- |

Object file version.

---

The documentation for this struct was generated from the following file:

- zephyr/llext/[elf.h](elf_8h_source.md)

- [elf64\_ehdr](structelf64__ehdr.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
