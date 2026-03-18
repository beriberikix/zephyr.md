---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structelf64__dyn.html
original_path: doxygen/html/structelf64__dyn.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

elf64\_dyn Struct Reference

[Operating System Services](group__os__services.md) » [Linkable loadable extensions](group__llext.md) » [ELF data types and defines](group__elf.md)

Dynamic section entry(64-bit).
[More...](#details)

`#include <[elf.h](elf_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [elf64\_sxword](group__elf.md#ga3e687a252b2bb6ed11ea9bc2fa6b728e) | [d\_tag](#a4f979530607b3152c84c5de7ca9b1f41) |
| union { |  |
| [elf64\_xword](group__elf.md#ga68e4179ac3b1c52c28c6e3e5c2a1838a)   [d\_val](#aefa41bed97c09ada1764a59cd636d310) |  |
| [elf64\_addr](group__elf.md#ga42c555ace34b21c1773c9e59228e9929)   [d\_ptr](#ab04f45d6dafdd1ab969452ee9f8f27f8) |  |
| } | [d\_un](#aab165fb0951d92439cd9f3f39a6ea247) |

## Detailed Description

Dynamic section entry(64-bit).

## Field Documentation

## [◆ ](#ab04f45d6dafdd1ab969452ee9f8f27f8)d\_ptr

| [elf64\_addr](group__elf.md#ga42c555ace34b21c1773c9e59228e9929) elf64\_dyn::d\_ptr |
| --- |

## [◆ ](#a4f979530607b3152c84c5de7ca9b1f41)d\_tag

| [elf64\_sxword](group__elf.md#ga3e687a252b2bb6ed11ea9bc2fa6b728e) elf64\_dyn::d\_tag |
| --- |

## [◆ ](#aab165fb0951d92439cd9f3f39a6ea247)[union]

| union { ... } elf64\_dyn::d\_un |
| --- |

## [◆ ](#aefa41bed97c09ada1764a59cd636d310)d\_val

| [elf64\_xword](group__elf.md#ga68e4179ac3b1c52c28c6e3e5c2a1838a) elf64\_dyn::d\_val |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/llext/[elf.h](elf_8h_source.md)

- [elf64\_dyn](structelf64__dyn.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
