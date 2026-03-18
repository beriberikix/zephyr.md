---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/atomic__c_8h.html
original_path: doxygen/html/atomic__c_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

atomic\_c.h File Reference

[Go to the source code of this file.](atomic__c_8h_source.md)

| Functions | |
| --- | --- |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [atomic\_cas](#ab879da5aa1ffcc317adc664c016586f7) ([atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*target, [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) old\_value, [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) new\_value) |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [atomic\_ptr\_cas](#a98f03db5ef2b36ff3412506a7f6d9558) ([atomic\_ptr\_t](atomic__types_8h.md#acad6866fa4c844026cd9f8c3fb60ecd7) \*target, [atomic\_ptr\_val\_t](atomic__types_8h.md#a374deb49b6dab1420a835b01433eb2f4) old\_value, [atomic\_ptr\_val\_t](atomic__types_8h.md#a374deb49b6dab1420a835b01433eb2f4) new\_value) |
| [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) | [atomic\_add](#a518c07595daaca29a9e53071ed59c9c0) ([atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*target, [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) value) |
| [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) | [atomic\_sub](#a84ab58fd0a6dbbf1bf675722b5900bd7) ([atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*target, [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) value) |
| static [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) | [atomic\_inc](#a66487deb6817076501dd9160537fc06a) ([atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*target) |
| static [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) | [atomic\_dec](#a0adecd95c4d47987c404a31e87c1d5c5) ([atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*target) |
| [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) | [atomic\_get](#a33bb426a17535bd1022895a7e44b32fa) (const [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*target) |
| [atomic\_ptr\_val\_t](atomic__types_8h.md#a374deb49b6dab1420a835b01433eb2f4) | [atomic\_ptr\_get](#a250c4672ce7749261bdb8b2f0c767da2) (const [atomic\_ptr\_t](atomic__types_8h.md#acad6866fa4c844026cd9f8c3fb60ecd7) \*target) |
| [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) | [atomic\_set](#a5f0555245d8932c2e7f7e94575e1a095) ([atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*target, [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) value) |
| [atomic\_ptr\_val\_t](atomic__types_8h.md#a374deb49b6dab1420a835b01433eb2f4) | [atomic\_ptr\_set](#a3a57fd7f76f84e0f5800878b8f81fc35) ([atomic\_ptr\_t](atomic__types_8h.md#acad6866fa4c844026cd9f8c3fb60ecd7) \*target, [atomic\_ptr\_val\_t](atomic__types_8h.md#a374deb49b6dab1420a835b01433eb2f4) value) |
| static [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) | [atomic\_clear](#a45ccf5a7d636206f0673139ac393946f) ([atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*target) |
| static [atomic\_ptr\_val\_t](atomic__types_8h.md#a374deb49b6dab1420a835b01433eb2f4) | [atomic\_ptr\_clear](#a8b511a7b5bccc7bc6b6e13526f87c0f3) ([atomic\_ptr\_t](atomic__types_8h.md#acad6866fa4c844026cd9f8c3fb60ecd7) \*target) |
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

## [◆ ](#a45ccf5a7d636206f0673139ac393946f)atomic\_clear()

| | [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) atomic\_clear | ( | [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \* | *target* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a0adecd95c4d47987c404a31e87c1d5c5)atomic\_dec()

| | [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) atomic\_dec | ( | [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \* | *target* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a33bb426a17535bd1022895a7e44b32fa)atomic\_get()

| [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) atomic\_get | ( | const [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \* | *target* | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#a66487deb6817076501dd9160537fc06a)atomic\_inc()

| | [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) atomic\_inc | ( | [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \* | *target* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a3e954286e40de73e45598a00a0a2b864)atomic\_nand()

| [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) atomic\_nand | ( | [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \* | *target*, |
| --- | --- | --- | --- |
|  |  | [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) | *value* ) |

## [◆ ](#a1564a44a260e7d0d02e30ae045a99764)atomic\_or()

| [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) atomic\_or | ( | [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \* | *target*, |
| --- | --- | --- | --- |
|  |  | [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) | *value* ) |

## [◆ ](#a98f03db5ef2b36ff3412506a7f6d9558)atomic\_ptr\_cas()

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) atomic\_ptr\_cas | ( | [atomic\_ptr\_t](atomic__types_8h.md#acad6866fa4c844026cd9f8c3fb60ecd7) \* | *target*, |
| --- | --- | --- | --- |
|  |  | [atomic\_ptr\_val\_t](atomic__types_8h.md#a374deb49b6dab1420a835b01433eb2f4) | *old\_value*, |
|  |  | [atomic\_ptr\_val\_t](atomic__types_8h.md#a374deb49b6dab1420a835b01433eb2f4) | *new\_value* ) |

## [◆ ](#a8b511a7b5bccc7bc6b6e13526f87c0f3)atomic\_ptr\_clear()

| | [atomic\_ptr\_val\_t](atomic__types_8h.md#a374deb49b6dab1420a835b01433eb2f4) atomic\_ptr\_clear | ( | [atomic\_ptr\_t](atomic__types_8h.md#acad6866fa4c844026cd9f8c3fb60ecd7) \* | *target* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a250c4672ce7749261bdb8b2f0c767da2)atomic\_ptr\_get()

| [atomic\_ptr\_val\_t](atomic__types_8h.md#a374deb49b6dab1420a835b01433eb2f4) atomic\_ptr\_get | ( | const [atomic\_ptr\_t](atomic__types_8h.md#acad6866fa4c844026cd9f8c3fb60ecd7) \* | *target* | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#a3a57fd7f76f84e0f5800878b8f81fc35)atomic\_ptr\_set()

| [atomic\_ptr\_val\_t](atomic__types_8h.md#a374deb49b6dab1420a835b01433eb2f4) atomic\_ptr\_set | ( | [atomic\_ptr\_t](atomic__types_8h.md#acad6866fa4c844026cd9f8c3fb60ecd7) \* | *target*, |
| --- | --- | --- | --- |
|  |  | [atomic\_ptr\_val\_t](atomic__types_8h.md#a374deb49b6dab1420a835b01433eb2f4) | *value* ) |

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
- [atomic\_c.h](atomic__c_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
