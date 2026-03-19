---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structelf64__sym.html
original_path: doxygen/html/structelf64__sym.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

elf64\_sym Struct Reference

[Operating System Services](group__os__services.md) » [Linkable loadable extensions](group__llext__apis.md) » [ELF constants and data types](group__llext__elf.md)

Symbol table entry(64-bit).
[More...](#details)

`#include <[elf.h](llext_2elf_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [elf64\_word](group__llext__elf.md#gaabf3a740e51b02fbaf40bedfba35e476) | [st\_name](#aee1394841b7752ed58b47da46f83c0a5) |
|  | Name of the symbol as an index into the symbol string table. |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) char | [st\_info](#a48d593f11ef3d04b1f5d46f92aaa9839) |
|  | Symbol binding and type information. |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) char | [st\_other](#a47a54908caddb43875d6a167bec370c7) |
|  | Symbol visibility. |
| [elf64\_half](group__llext__elf.md#ga3358e1392fd861af8a7c8248519717a0) | [st\_shndx](#a285d9d47f979f7c0a3ae9ed18408d191) |
|  | Symbols related section given by section header index. |
| [elf64\_addr](group__llext__elf.md#ga42c555ace34b21c1773c9e59228e9929) | [st\_value](#a3037b0fbaf250e2e711ed5ad6b39fc88) |
|  | Value or location of the symbol. |
| [elf64\_xword](group__llext__elf.md#ga68e4179ac3b1c52c28c6e3e5c2a1838a) | [st\_size](#a73ba49c8bee2c11229f48756dccea886) |
|  | Size of the symbol. |

## Detailed Description

Symbol table entry(64-bit).

## Field Documentation

## [◆ ](#a48d593f11ef3d04b1f5d46f92aaa9839)st\_info

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) char elf64\_sym::st\_info |
| --- |

Symbol binding and type information.

## [◆ ](#aee1394841b7752ed58b47da46f83c0a5)st\_name

| [elf64\_word](group__llext__elf.md#gaabf3a740e51b02fbaf40bedfba35e476) elf64\_sym::st\_name |
| --- |

Name of the symbol as an index into the symbol string table.

## [◆ ](#a47a54908caddb43875d6a167bec370c7)st\_other

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) char elf64\_sym::st\_other |
| --- |

Symbol visibility.

## [◆ ](#a285d9d47f979f7c0a3ae9ed18408d191)st\_shndx

| [elf64\_half](group__llext__elf.md#ga3358e1392fd861af8a7c8248519717a0) elf64\_sym::st\_shndx |
| --- |

Symbols related section given by section header index.

## [◆ ](#a73ba49c8bee2c11229f48756dccea886)st\_size

| [elf64\_xword](group__llext__elf.md#ga68e4179ac3b1c52c28c6e3e5c2a1838a) elf64\_sym::st\_size |
| --- |

Size of the symbol.

## [◆ ](#a3037b0fbaf250e2e711ed5ad6b39fc88)st\_value

| [elf64\_addr](group__llext__elf.md#ga42c555ace34b21c1773c9e59228e9929) elf64\_sym::st\_value |
| --- |

Value or location of the symbol.

---

The documentation for this struct was generated from the following file:

- zephyr/llext/[elf.h](llext_2elf_8h_source.md)

- [elf64\_sym](structelf64__sym.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
