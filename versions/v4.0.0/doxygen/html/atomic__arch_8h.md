---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/atomic__arch_8h.html
original_path: doxygen/html/atomic__arch_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

atomic\_arch.h File Reference

`#include <[stdbool.h](stdbool_8h_source.md)>`  
`#include <[zephyr/sys/atomic_types.h](atomic__types_8h_source.md)>`

[Go to the source code of this file.](atomic__arch_8h_source.md)

| Functions | |
| --- | --- |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [atomic\_cas](#ab879da5aa1ffcc317adc664c016586f7) ([atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*target, [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) old\_value, [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) new\_value) |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [atomic\_ptr\_cas](#adb8b37f84beeb5c8ab46faa0c7f6cf33) ([atomic\_ptr\_t](atomic__types_8h.md#acad6866fa4c844026cd9f8c3fb60ecd7) \*target, void \*old\_value, void \*new\_value) |
| [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) | [atomic\_add](#a518c07595daaca29a9e53071ed59c9c0) ([atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*target, [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) value) |
| [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) | [atomic\_sub](#a84ab58fd0a6dbbf1bf675722b5900bd7) ([atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*target, [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) value) |
| [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) | [atomic\_inc](#aae47a9cbe5a6534967b417f602b37ac2) ([atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*target) |
| [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) | [atomic\_dec](#ac260f0efbd970717eae4ac3bb493a0c4) ([atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*target) |
| [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) | [atomic\_get](#a33bb426a17535bd1022895a7e44b32fa) (const [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*target) |
| void \* | [atomic\_ptr\_get](#a11a456c5b154bed43c4fc8859b5f6547) (const [atomic\_ptr\_t](atomic__types_8h.md#acad6866fa4c844026cd9f8c3fb60ecd7) \*target) |
| [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) | [atomic\_set](#a5f0555245d8932c2e7f7e94575e1a095) ([atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*target, [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) value) |
| void \* | [atomic\_ptr\_set](#aaaeac347d3727fee6b85efb289285cb4) ([atomic\_ptr\_t](atomic__types_8h.md#acad6866fa4c844026cd9f8c3fb60ecd7) \*target, void \*value) |
| [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) | [atomic\_clear](#a879b5f540c25fd09f1b84563e3dc8a91) ([atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*target) |
| void \* | [atomic\_ptr\_clear](#a7dca81028baa3f371ef487d683745762) ([atomic\_ptr\_t](atomic__types_8h.md#acad6866fa4c844026cd9f8c3fb60ecd7) \*target) |
| [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) | [atomic\_or](#a1564a44a260e7d0d02e30ae045a99764) ([atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*target, [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) value) |
| [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) | [atomic\_xor](#a18592bcf38d667fb9b428f81ea691bd4) ([atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*target, [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) value) |
| [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) | [atomic\_and](#a4bc1f6a6f5d98eef742b4541d235811d) ([atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*target, [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) value) |
| [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) | [atomic\_nand](#a3e954286e40de73e45598a00a0a2b864) ([atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*target, [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) value) |

## Function Documentation

## [◆ ](#a518c07595daaca29a9e53071ed59c9c0)atomic\_add()

| [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) atomic\_add | ( | [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \* | *target*, |
| --- | --- | --- | --- |
|  |  | [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) | *value* ) |

## [◆ ](#a4bc1f6a6f5d98eef742b4541d235811d)atomic\_and()

| [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) atomic\_and | ( | [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \* | *target*, |
| --- | --- | --- | --- |
|  |  | [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) | *value* ) |

## [◆ ](#ab879da5aa1ffcc317adc664c016586f7)atomic\_cas()

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) atomic\_cas | ( | [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \* | *target*, |
| --- | --- | --- | --- |
|  |  | [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) | *old\_value*, |
|  |  | [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) | *new\_value* ) |

## [◆ ](#a879b5f540c25fd09f1b84563e3dc8a91)atomic\_clear()

| [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) atomic\_clear | ( | [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \* | *target* | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#ac260f0efbd970717eae4ac3bb493a0c4)atomic\_dec()

| [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) atomic\_dec | ( | [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \* | *target* | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#a33bb426a17535bd1022895a7e44b32fa)atomic\_get()

| [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) atomic\_get | ( | const [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \* | *target* | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#aae47a9cbe5a6534967b417f602b37ac2)atomic\_inc()

| [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) atomic\_inc | ( | [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \* | *target* | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#a3e954286e40de73e45598a00a0a2b864)atomic\_nand()

| [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) atomic\_nand | ( | [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \* | *target*, |
| --- | --- | --- | --- |
|  |  | [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) | *value* ) |

## [◆ ](#a1564a44a260e7d0d02e30ae045a99764)atomic\_or()

| [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) atomic\_or | ( | [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \* | *target*, |
| --- | --- | --- | --- |
|  |  | [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) | *value* ) |

## [◆ ](#adb8b37f84beeb5c8ab46faa0c7f6cf33)atomic\_ptr\_cas()

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) atomic\_ptr\_cas | ( | [atomic\_ptr\_t](atomic__types_8h.md#acad6866fa4c844026cd9f8c3fb60ecd7) \* | *target*, |
| --- | --- | --- | --- |
|  |  | void \* | *old\_value*, |
|  |  | void \* | *new\_value* ) |

## [◆ ](#a7dca81028baa3f371ef487d683745762)atomic\_ptr\_clear()

| void \* atomic\_ptr\_clear | ( | [atomic\_ptr\_t](atomic__types_8h.md#acad6866fa4c844026cd9f8c3fb60ecd7) \* | *target* | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#a11a456c5b154bed43c4fc8859b5f6547)atomic\_ptr\_get()

| void \* atomic\_ptr\_get | ( | const [atomic\_ptr\_t](atomic__types_8h.md#acad6866fa4c844026cd9f8c3fb60ecd7) \* | *target* | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#aaaeac347d3727fee6b85efb289285cb4)atomic\_ptr\_set()

| void \* atomic\_ptr\_set | ( | [atomic\_ptr\_t](atomic__types_8h.md#acad6866fa4c844026cd9f8c3fb60ecd7) \* | *target*, |
| --- | --- | --- | --- |
|  |  | void \* | *value* ) |

## [◆ ](#a5f0555245d8932c2e7f7e94575e1a095)atomic\_set()

| [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) atomic\_set | ( | [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \* | *target*, |
| --- | --- | --- | --- |
|  |  | [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) | *value* ) |

## [◆ ](#a84ab58fd0a6dbbf1bf675722b5900bd7)atomic\_sub()

| [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) atomic\_sub | ( | [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \* | *target*, |
| --- | --- | --- | --- |
|  |  | [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) | *value* ) |

## [◆ ](#a18592bcf38d667fb9b428f81ea691bd4)atomic\_xor()

| [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) atomic\_xor | ( | [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \* | *target*, |
| --- | --- | --- | --- |
|  |  | [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) | *value* ) |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [sys](dir_85ec07b7ac0b888617bae1400221d199.md)
- [atomic\_arch.h](atomic__arch_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
