---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structelf32__sym.html
original_path: doxygen/html/structelf32__sym.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

elf32\_sym Struct Reference

[Operating System Services](group__os__services.md) » [Linkable loadable extensions](group__llext__apis.md) » [ELF constants and data types](group__llext__elf.md)

Symbol table entry(32-bit).
[More...](#details)

`#include <[elf.h](elf_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [elf32\_word](group__llext__elf.md#gac786571f50a02299b19c1a16d658ea72) | [st\_name](#a14545ec8738f87d6ac8da1d4a601d024) |
|  | Name of the symbol as an index into the symbol string table. |
| [elf32\_addr](group__llext__elf.md#ga55f1dc601c95381307fddd5969969634) | [st\_value](#a39b94d141bae73d0c1d8f6df5695ea2d) |
|  | Value or location of the symbol. |
| [elf32\_word](group__llext__elf.md#gac786571f50a02299b19c1a16d658ea72) | [st\_size](#aef3af325acfa8080431f06de9267c662) |
|  | Size of the symbol. |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) char | [st\_info](#aeef86f71df370cf183e2d03afe4d8812) |
|  | Symbol binding and type information. |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) char | [st\_other](#a5ce8408912eda365e2e3246f81f98360) |
|  | Symbol visibility. |
| [elf32\_half](group__llext__elf.md#ga141d58f50804ef53e0d9bd13fcb36424) | [st\_shndx](#a03dbc7e19d4f2f9aac76bf99d218658b) |
|  | Symbols related section given by section header index. |

## Detailed Description

Symbol table entry(32-bit).

## Field Documentation

## [◆ ](#aeef86f71df370cf183e2d03afe4d8812)st\_info

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) char elf32\_sym::st\_info |
| --- |

Symbol binding and type information.

## [◆ ](#a14545ec8738f87d6ac8da1d4a601d024)st\_name

| [elf32\_word](group__llext__elf.md#gac786571f50a02299b19c1a16d658ea72) elf32\_sym::st\_name |
| --- |

Name of the symbol as an index into the symbol string table.

## [◆ ](#a5ce8408912eda365e2e3246f81f98360)st\_other

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) char elf32\_sym::st\_other |
| --- |

Symbol visibility.

## [◆ ](#a03dbc7e19d4f2f9aac76bf99d218658b)st\_shndx

| [elf32\_half](group__llext__elf.md#ga141d58f50804ef53e0d9bd13fcb36424) elf32\_sym::st\_shndx |
| --- |

Symbols related section given by section header index.

## [◆ ](#aef3af325acfa8080431f06de9267c662)st\_size

| [elf32\_word](group__llext__elf.md#gac786571f50a02299b19c1a16d658ea72) elf32\_sym::st\_size |
| --- |

Size of the symbol.

## [◆ ](#a39b94d141bae73d0c1d8f6df5695ea2d)st\_value

| [elf32\_addr](group__llext__elf.md#ga55f1dc601c95381307fddd5969969634) elf32\_sym::st\_value |
| --- |

Value or location of the symbol.

---

The documentation for this struct was generated from the following file:

- zephyr/llext/[elf.h](elf_8h_source.md)

- [elf32\_sym](structelf32__sym.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
