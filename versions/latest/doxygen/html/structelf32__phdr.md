---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structelf32__phdr.html
original_path: doxygen/html/structelf32__phdr.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

elf32\_phdr Struct Reference

[Operating System Services](group__os__services.md) » [Linkable loadable extensions](group__llext.md) » [ELF data types and defines](group__elf.md)

Program header(32-bit).
[More...](#details)

`#include <[elf.h](elf_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [elf32\_word](group__elf.md#gac786571f50a02299b19c1a16d658ea72) | [p\_type](#a7f6e96874bcf813a547508d169dfa261) |
| [elf32\_off](group__elf.md#gabb40eb5ffbe88010885da1c8c7b869e3) | [p\_offset](#a60f1e33f2cfbe98f30b2c54d4c2d600c) |
| [elf32\_addr](group__elf.md#ga55f1dc601c95381307fddd5969969634) | [p\_vaddr](#a68f5b0b94ef5fb7e736281c095fe7fd0) |
| [elf32\_addr](group__elf.md#ga55f1dc601c95381307fddd5969969634) | [p\_paddr](#a45f3a2a88d3687cd226a08f71880f354) |
| [elf32\_word](group__elf.md#gac786571f50a02299b19c1a16d658ea72) | [p\_filesz](#adb3bfd1ab37779c07390c80eb8b24ae1) |
| [elf32\_word](group__elf.md#gac786571f50a02299b19c1a16d658ea72) | [p\_memsz](#a550a36141d4a3342eacd6a92dfc34cd6) |
| [elf32\_word](group__elf.md#gac786571f50a02299b19c1a16d658ea72) | [p\_flags](#a38c17e479fe8c9e32e666ac5405e9c95) |
| [elf32\_word](group__elf.md#gac786571f50a02299b19c1a16d658ea72) | [p\_align](#a7339bec0031f197689cc9370ef1b42ef) |

## Detailed Description

Program header(32-bit).

## Field Documentation

## [◆ ](#a7339bec0031f197689cc9370ef1b42ef)p\_align

| [elf32\_word](group__elf.md#gac786571f50a02299b19c1a16d658ea72) elf32\_phdr::p\_align |
| --- |

## [◆ ](#adb3bfd1ab37779c07390c80eb8b24ae1)p\_filesz

| [elf32\_word](group__elf.md#gac786571f50a02299b19c1a16d658ea72) elf32\_phdr::p\_filesz |
| --- |

## [◆ ](#a38c17e479fe8c9e32e666ac5405e9c95)p\_flags

| [elf32\_word](group__elf.md#gac786571f50a02299b19c1a16d658ea72) elf32\_phdr::p\_flags |
| --- |

## [◆ ](#a550a36141d4a3342eacd6a92dfc34cd6)p\_memsz

| [elf32\_word](group__elf.md#gac786571f50a02299b19c1a16d658ea72) elf32\_phdr::p\_memsz |
| --- |

## [◆ ](#a60f1e33f2cfbe98f30b2c54d4c2d600c)p\_offset

| [elf32\_off](group__elf.md#gabb40eb5ffbe88010885da1c8c7b869e3) elf32\_phdr::p\_offset |
| --- |

## [◆ ](#a45f3a2a88d3687cd226a08f71880f354)p\_paddr

| [elf32\_addr](group__elf.md#ga55f1dc601c95381307fddd5969969634) elf32\_phdr::p\_paddr |
| --- |

## [◆ ](#a7f6e96874bcf813a547508d169dfa261)p\_type

| [elf32\_word](group__elf.md#gac786571f50a02299b19c1a16d658ea72) elf32\_phdr::p\_type |
| --- |

## [◆ ](#a68f5b0b94ef5fb7e736281c095fe7fd0)p\_vaddr

| [elf32\_addr](group__elf.md#ga55f1dc601c95381307fddd5969969634) elf32\_phdr::p\_vaddr |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/llext/[elf.h](elf_8h_source.md)

- [elf32\_phdr](structelf32__phdr.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
