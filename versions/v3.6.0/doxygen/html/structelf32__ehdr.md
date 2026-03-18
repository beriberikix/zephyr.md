---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structelf32__ehdr.html
original_path: doxygen/html/structelf32__ehdr.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

elf32\_ehdr Struct Reference

[Operating System Services](group__os__services.md) » [Linkable loadable extensions](group__llext.md) » [ELF data types and defines](group__elf.md)

ELF Header(32-bit).
[More...](#details)

`#include <[elf.h](elf_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) char | [e\_ident](#acef0ea640d4fd75562b7412eaf8e2226) [16] |
|  | Magic string identifying ELF binary. |
| [elf32\_half](group__elf.md#ga141d58f50804ef53e0d9bd13fcb36424) | [e\_type](#ae26a4d5cc90917ec13689060695833e5) |
|  | Type of ELF. |
| [elf32\_half](group__elf.md#ga141d58f50804ef53e0d9bd13fcb36424) | [e\_machine](#a09a134b6c6b711458673ddc8601af4c5) |
|  | Machine type. |
| [elf32\_word](group__elf.md#gac786571f50a02299b19c1a16d658ea72) | [e\_version](#a4f73aa6711f379fb70a483e99d47f108) |
|  | Object file version. |
| [elf32\_addr](group__elf.md#ga55f1dc601c95381307fddd5969969634) | [e\_entry](#a2322a1ac85ac7962cd05152588f8bf8f) |
|  | Virtual address of entry. |
| [elf32\_off](group__elf.md#gabb40eb5ffbe88010885da1c8c7b869e3) | [e\_phoff](#af25dd95c6c2b2e8aeecdfb130ed4bfc6) |
|  | Program header table offset. |
| [elf32\_off](group__elf.md#gabb40eb5ffbe88010885da1c8c7b869e3) | [e\_shoff](#a085432a071a923e4fe1d3a4a3dfa665b) |
|  | Section header table offset. |
| [elf32\_word](group__elf.md#gac786571f50a02299b19c1a16d658ea72) | [e\_flags](#a1533636f5162a1f5a6e501a4129a5954) |
|  | Processor specific flags. |
| [elf32\_half](group__elf.md#ga141d58f50804ef53e0d9bd13fcb36424) | [e\_ehsize](#a33698f57f4f73a4f7659633fc11114fb) |
|  | ELF header size. |
| [elf32\_half](group__elf.md#ga141d58f50804ef53e0d9bd13fcb36424) | [e\_phentsize](#a0deea8c06b17aff924a86adf23206dd7) |
|  | Program header count. |
| [elf32\_half](group__elf.md#ga141d58f50804ef53e0d9bd13fcb36424) | [e\_phnum](#a24ad42f294e548d54ff91ae9de5bb729) |
|  | Program header count. |
| [elf32\_half](group__elf.md#ga141d58f50804ef53e0d9bd13fcb36424) | [e\_shentsize](#a2b8ae6d098c44146579dbe4c8e2d11c8) |
|  | Section header size. |
| [elf32\_half](group__elf.md#ga141d58f50804ef53e0d9bd13fcb36424) | [e\_shnum](#a5f795d38ed810bad582d88c35b474cbf) |
|  | Section header count. |
| [elf32\_half](group__elf.md#ga141d58f50804ef53e0d9bd13fcb36424) | [e\_shstrndx](#a4537e3831f136b81a7a0d6260ad497a6) |
|  | Section header containing section header string table. |

## Detailed Description

ELF Header(32-bit).

## Field Documentation

## [◆ ](#a33698f57f4f73a4f7659633fc11114fb)e\_ehsize

| [elf32\_half](group__elf.md#ga141d58f50804ef53e0d9bd13fcb36424) elf32\_ehdr::e\_ehsize |
| --- |

ELF header size.

## [◆ ](#a2322a1ac85ac7962cd05152588f8bf8f)e\_entry

| [elf32\_addr](group__elf.md#ga55f1dc601c95381307fddd5969969634) elf32\_ehdr::e\_entry |
| --- |

Virtual address of entry.

## [◆ ](#a1533636f5162a1f5a6e501a4129a5954)e\_flags

| [elf32\_word](group__elf.md#gac786571f50a02299b19c1a16d658ea72) elf32\_ehdr::e\_flags |
| --- |

Processor specific flags.

## [◆ ](#acef0ea640d4fd75562b7412eaf8e2226)e\_ident

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) char elf32\_ehdr::e\_ident[16] |
| --- |

Magic string identifying ELF binary.

## [◆ ](#a09a134b6c6b711458673ddc8601af4c5)e\_machine

| [elf32\_half](group__elf.md#ga141d58f50804ef53e0d9bd13fcb36424) elf32\_ehdr::e\_machine |
| --- |

Machine type.

## [◆ ](#a0deea8c06b17aff924a86adf23206dd7)e\_phentsize

| [elf32\_half](group__elf.md#ga141d58f50804ef53e0d9bd13fcb36424) elf32\_ehdr::e\_phentsize |
| --- |

Program header count.

## [◆ ](#a24ad42f294e548d54ff91ae9de5bb729)e\_phnum

| [elf32\_half](group__elf.md#ga141d58f50804ef53e0d9bd13fcb36424) elf32\_ehdr::e\_phnum |
| --- |

Program header count.

## [◆ ](#af25dd95c6c2b2e8aeecdfb130ed4bfc6)e\_phoff

| [elf32\_off](group__elf.md#gabb40eb5ffbe88010885da1c8c7b869e3) elf32\_ehdr::e\_phoff |
| --- |

Program header table offset.

## [◆ ](#a2b8ae6d098c44146579dbe4c8e2d11c8)e\_shentsize

| [elf32\_half](group__elf.md#ga141d58f50804ef53e0d9bd13fcb36424) elf32\_ehdr::e\_shentsize |
| --- |

Section header size.

## [◆ ](#a5f795d38ed810bad582d88c35b474cbf)e\_shnum

| [elf32\_half](group__elf.md#ga141d58f50804ef53e0d9bd13fcb36424) elf32\_ehdr::e\_shnum |
| --- |

Section header count.

## [◆ ](#a085432a071a923e4fe1d3a4a3dfa665b)e\_shoff

| [elf32\_off](group__elf.md#gabb40eb5ffbe88010885da1c8c7b869e3) elf32\_ehdr::e\_shoff |
| --- |

Section header table offset.

## [◆ ](#a4537e3831f136b81a7a0d6260ad497a6)e\_shstrndx

| [elf32\_half](group__elf.md#ga141d58f50804ef53e0d9bd13fcb36424) elf32\_ehdr::e\_shstrndx |
| --- |

Section header containing section header string table.

## [◆ ](#ae26a4d5cc90917ec13689060695833e5)e\_type

| [elf32\_half](group__elf.md#ga141d58f50804ef53e0d9bd13fcb36424) elf32\_ehdr::e\_type |
| --- |

Type of ELF.

## [◆ ](#a4f73aa6711f379fb70a483e99d47f108)e\_version

| [elf32\_word](group__elf.md#gac786571f50a02299b19c1a16d658ea72) elf32\_ehdr::e\_version |
| --- |

Object file version.

---

The documentation for this struct was generated from the following file:

- zephyr/llext/[elf.h](elf_8h_source.md)

- [elf32\_ehdr](structelf32__ehdr.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
