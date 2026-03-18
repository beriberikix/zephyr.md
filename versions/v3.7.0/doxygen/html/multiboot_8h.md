---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/multiboot_8h.html
original_path: doxygen/html/multiboot_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

multiboot.h File Reference

`#include <[stdint.h](stdint_8h_source.md)>`

[Go to the source code of this file.](multiboot_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [multiboot\_info](structmultiboot__info.md) |
| struct | [multiboot\_mmap](structmultiboot__mmap.md) |

| Macros | |
| --- | --- |
| #define | [MULTIBOOT\_BOOT\_TYPE](#a06ef275439d876f323a821b67e6b4113)   1 |
| #define | [MULTIBOOT\_MMAP\_RAM](#acd771d326981efd04d4127e9c4199cff)   1 /\* available RAM \*/ |
| #define | [MULTIBOOT\_MMAP\_ACPI](#a132865c50004f3dfeb97d665990c843d)   3 /\* reserved for ACPI \*/ |
| #define | [MULTIBOOT\_MMAP\_NVS](#a6a9dd86351aefc0f8adef49a43427cbf)   4 /\* ACPI non-volatile \*/ |
| #define | [MULTIBOOT\_MMAP\_DEFECTIVE](#a6191e5ddf1f87ea3cccc5a232d74c74d)   5 /\* defective RAM module \*/ |
| #define | [MULTIBOOT\_HEADER\_MAGIC](#ab36ad4b4a42c58aac4ad1f2ba13054e9)   0x1BADB002 |
| #define | [MULTIBOOT\_EAX\_MAGIC](#a48040d17caa533b48233cf00f8dc7ba2)   0x2BADB002 |
| #define | [MULTIBOOT\_HEADER\_FLAG\_MEM](#a848a1462fa2f8907c8574136f5410b24)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) /\* want mem\_/mmap\_\* info \*/ |
| #define | [MULTIBOOT\_HEADER\_FLAG\_FB](#ab615ba7169d9c368345342b256a322d2)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) /\* want fb\_\* info \*/ |
| #define | [MULTIBOOT\_HEADER\_FLAGS](#a5447ae8b3b45c8ed17ad61c267250992)   [MULTIBOOT\_HEADER\_FLAG\_MEM](#a848a1462fa2f8907c8574136f5410b24) |
| #define | [MULTIBOOT\_INFO\_FLAGS\_MEM](#aac0e678a709bed9459227996d582f2de)   (1 << 0) /\* mem\_\* valid \*/ |
| #define | [MULTIBOOT\_INFO\_FLAGS\_MMAP](#a1795eb5882e173fd014eb8bdeb4e69bc)   (1 << 6) /\* mmap\_\* valid \*/ |
| #define | [MULTIBOOT\_INFO\_FLAGS\_FB](#ad6aeb1c2eacec3b04818f77d0deeeaf6)   (1 << 12) /\* fb\_\* valid \*/ |
| #define | [MULTIBOOT\_INFO\_FB\_TYPE\_RGB](#a418e7db9b4bfbe3a9a563e8030cf50ed)   1 |

| Variables | |
| --- | --- |
| struct multiboot\_info | [multiboot\_info](#a596cbe9e737c9acca4328e2e03186896) |

## Macro Definition Documentation

## [◆ ](#a06ef275439d876f323a821b67e6b4113)MULTIBOOT\_BOOT\_TYPE

| #define MULTIBOOT\_BOOT\_TYPE   1 |
| --- |

## [◆ ](#a48040d17caa533b48233cf00f8dc7ba2)MULTIBOOT\_EAX\_MAGIC

| #define MULTIBOOT\_EAX\_MAGIC   0x2BADB002 |
| --- |

## [◆ ](#ab615ba7169d9c368345342b256a322d2)MULTIBOOT\_HEADER\_FLAG\_FB

| #define MULTIBOOT\_HEADER\_FLAG\_FB   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) /\* want fb\_\* info \*/ |
| --- |

## [◆ ](#a848a1462fa2f8907c8574136f5410b24)MULTIBOOT\_HEADER\_FLAG\_MEM

| #define MULTIBOOT\_HEADER\_FLAG\_MEM   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) /\* want mem\_/mmap\_\* info \*/ |
| --- |

## [◆ ](#a5447ae8b3b45c8ed17ad61c267250992)MULTIBOOT\_HEADER\_FLAGS

| #define MULTIBOOT\_HEADER\_FLAGS   [MULTIBOOT\_HEADER\_FLAG\_MEM](#a848a1462fa2f8907c8574136f5410b24) |
| --- |

## [◆ ](#ab36ad4b4a42c58aac4ad1f2ba13054e9)MULTIBOOT\_HEADER\_MAGIC

| #define MULTIBOOT\_HEADER\_MAGIC   0x1BADB002 |
| --- |

## [◆ ](#a418e7db9b4bfbe3a9a563e8030cf50ed)MULTIBOOT\_INFO\_FB\_TYPE\_RGB

| #define MULTIBOOT\_INFO\_FB\_TYPE\_RGB   1 |
| --- |

## [◆ ](#ad6aeb1c2eacec3b04818f77d0deeeaf6)MULTIBOOT\_INFO\_FLAGS\_FB

| #define MULTIBOOT\_INFO\_FLAGS\_FB   (1 << 12) /\* fb\_\* valid \*/ |
| --- |

## [◆ ](#aac0e678a709bed9459227996d582f2de)MULTIBOOT\_INFO\_FLAGS\_MEM

| #define MULTIBOOT\_INFO\_FLAGS\_MEM   (1 << 0) /\* mem\_\* valid \*/ |
| --- |

## [◆ ](#a1795eb5882e173fd014eb8bdeb4e69bc)MULTIBOOT\_INFO\_FLAGS\_MMAP

| #define MULTIBOOT\_INFO\_FLAGS\_MMAP   (1 << 6) /\* mmap\_\* valid \*/ |
| --- |

## [◆ ](#a132865c50004f3dfeb97d665990c843d)MULTIBOOT\_MMAP\_ACPI

| #define MULTIBOOT\_MMAP\_ACPI   3 /\* reserved for ACPI \*/ |
| --- |

## [◆ ](#a6191e5ddf1f87ea3cccc5a232d74c74d)MULTIBOOT\_MMAP\_DEFECTIVE

| #define MULTIBOOT\_MMAP\_DEFECTIVE   5 /\* defective RAM module \*/ |
| --- |

## [◆ ](#a6a9dd86351aefc0f8adef49a43427cbf)MULTIBOOT\_MMAP\_NVS

| #define MULTIBOOT\_MMAP\_NVS   4 /\* ACPI non-volatile \*/ |
| --- |

## [◆ ](#acd771d326981efd04d4127e9c4199cff)MULTIBOOT\_MMAP\_RAM

| #define MULTIBOOT\_MMAP\_RAM   1 /\* available RAM \*/ |
| --- |

## Variable Documentation

## [◆ ](#a596cbe9e737c9acca4328e2e03186896)multiboot\_info

| | struct multiboot\_info multiboot\_info | | --- | | extern |
| --- | --- | --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [x86](dir_0c2b2a40388d14bf987ab4c9c60eb89c.md)
- [multiboot.h](multiboot_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
