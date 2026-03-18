---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structelf64__phdr.html
original_path: doxygen/html/structelf64__phdr.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

elf64\_phdr Struct Reference

[Operating System Services](group__os__services.md) » [Linkable loadable extensions](group__llext.md) » [ELF data types and defines](group__elf.md)

Program header(64-bit).
[More...](#details)

`#include <[elf.h](elf_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [elf64\_word](group__elf.md#gaabf3a740e51b02fbaf40bedfba35e476) | [p\_type](#a5230942d825583ca57c2bc1922d90efb) |
| [elf64\_off](group__elf.md#ga7f982d835a34713a84907873f9e058a9) | [p\_offset](#afd9bb2cb730c024731c4403eb4cc849e) |
| [elf64\_addr](group__elf.md#ga42c555ace34b21c1773c9e59228e9929) | [p\_vaddr](#a4ae86302877fd29baabd5712a31a7804) |
| [elf64\_addr](group__elf.md#ga42c555ace34b21c1773c9e59228e9929) | [p\_paddr](#a974097eeed423213d7568c742b4fb691) |
| [elf64\_xword](group__elf.md#ga68e4179ac3b1c52c28c6e3e5c2a1838a) | [p\_filesz](#a39783d6505c9e8ee660486d73909807a) |
| [elf64\_xword](group__elf.md#ga68e4179ac3b1c52c28c6e3e5c2a1838a) | [p\_memsz](#addb156fc4919b43cb63863f40a11595b) |
| [elf64\_word](group__elf.md#gaabf3a740e51b02fbaf40bedfba35e476) | [p\_flags](#abf65a3fdb555b51b0779713441554506) |
| [elf64\_xword](group__elf.md#ga68e4179ac3b1c52c28c6e3e5c2a1838a) | [p\_align](#ad941df3941ab694d7950ef91b1ffface) |

## Detailed Description

Program header(64-bit).

## Field Documentation

## [◆ ](#ad941df3941ab694d7950ef91b1ffface)p\_align

| [elf64\_xword](group__elf.md#ga68e4179ac3b1c52c28c6e3e5c2a1838a) elf64\_phdr::p\_align |
| --- |

## [◆ ](#a39783d6505c9e8ee660486d73909807a)p\_filesz

| [elf64\_xword](group__elf.md#ga68e4179ac3b1c52c28c6e3e5c2a1838a) elf64\_phdr::p\_filesz |
| --- |

## [◆ ](#abf65a3fdb555b51b0779713441554506)p\_flags

| [elf64\_word](group__elf.md#gaabf3a740e51b02fbaf40bedfba35e476) elf64\_phdr::p\_flags |
| --- |

## [◆ ](#addb156fc4919b43cb63863f40a11595b)p\_memsz

| [elf64\_xword](group__elf.md#ga68e4179ac3b1c52c28c6e3e5c2a1838a) elf64\_phdr::p\_memsz |
| --- |

## [◆ ](#afd9bb2cb730c024731c4403eb4cc849e)p\_offset

| [elf64\_off](group__elf.md#ga7f982d835a34713a84907873f9e058a9) elf64\_phdr::p\_offset |
| --- |

## [◆ ](#a974097eeed423213d7568c742b4fb691)p\_paddr

| [elf64\_addr](group__elf.md#ga42c555ace34b21c1773c9e59228e9929) elf64\_phdr::p\_paddr |
| --- |

## [◆ ](#a5230942d825583ca57c2bc1922d90efb)p\_type

| [elf64\_word](group__elf.md#gaabf3a740e51b02fbaf40bedfba35e476) elf64\_phdr::p\_type |
| --- |

## [◆ ](#a4ae86302877fd29baabd5712a31a7804)p\_vaddr

| [elf64\_addr](group__elf.md#ga42c555ace34b21c1773c9e59228e9929) elf64\_phdr::p\_vaddr |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/llext/[elf.h](elf_8h_source.md)

- [elf64\_phdr](structelf64__phdr.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
