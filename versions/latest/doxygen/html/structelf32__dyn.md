---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structelf32__dyn.html
original_path: doxygen/html/structelf32__dyn.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

elf32\_dyn Struct Reference

[Operating System Services](group__os__services.md) » [Linkable loadable extensions](group__llext.md) » [ELF data types and defines](group__elf.md)

Dynamic section entry(32-bit).
[More...](#details)

`#include <[elf.h](elf_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [elf32\_sword](group__elf.md#ga1325c85290908b89a9c2b9bdd1aa2efd) | [d\_tag](#a1c0a994db5257e6a72cdb15812709eff) |
| union { |  |
| [elf32\_word](group__elf.md#gac786571f50a02299b19c1a16d658ea72)   [d\_val](#a593bd41b6aca445668b4b46290acbb1c) |  |
| [elf32\_addr](group__elf.md#ga55f1dc601c95381307fddd5969969634)   [d\_ptr](#a53a74cdb1500123dd136c3df2c594201) |  |
| } | [d\_un](#ad8d323d152cfefa5a1f4b6b1520dfea2) |

## Detailed Description

Dynamic section entry(32-bit).

## Field Documentation

## [◆ ](#a53a74cdb1500123dd136c3df2c594201)d\_ptr

| [elf32\_addr](group__elf.md#ga55f1dc601c95381307fddd5969969634) elf32\_dyn::d\_ptr |
| --- |

## [◆ ](#a1c0a994db5257e6a72cdb15812709eff)d\_tag

| [elf32\_sword](group__elf.md#ga1325c85290908b89a9c2b9bdd1aa2efd) elf32\_dyn::d\_tag |
| --- |

## [◆ ](#ad8d323d152cfefa5a1f4b6b1520dfea2)[union]

| union { ... } elf32\_dyn::d\_un |
| --- |

## [◆ ](#a593bd41b6aca445668b4b46290acbb1c)d\_val

| [elf32\_word](group__elf.md#gac786571f50a02299b19c1a16d658ea72) elf32\_dyn::d\_val |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/llext/[elf.h](elf_8h_source.md)

- [elf32\_dyn](structelf32__dyn.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
