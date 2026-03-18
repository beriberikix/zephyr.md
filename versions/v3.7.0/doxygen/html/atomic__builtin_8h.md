---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/atomic__builtin_8h.html
original_path: doxygen/html/atomic__builtin_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

atomic\_builtin.h File Reference

`#include <[stdbool.h](stdbool_8h_source.md)>`  
`#include <stddef.h>`  
`#include <[zephyr/sys/atomic_types.h](atomic__types_8h_source.md)>`

[Go to the source code of this file.](atomic__builtin_8h_source.md)

| Functions | |
| --- | --- |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [atomic\_cas](#a6a4a6dea8c56d6a78bc57d87a1f79450) ([atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*target, [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) old\_value, [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) new\_value) |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [atomic\_ptr\_cas](#a1ee94308793379944e8e28371e1d135b) ([atomic\_ptr\_t](atomic__types_8h.md#acad6866fa4c844026cd9f8c3fb60ecd7) \*target, [atomic\_ptr\_val\_t](atomic__types_8h.md#a374deb49b6dab1420a835b01433eb2f4) old\_value, [atomic\_ptr\_val\_t](atomic__types_8h.md#a374deb49b6dab1420a835b01433eb2f4) new\_value) |
| static [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) | [atomic\_add](#aed809d451c08b151dd8e20db3f12926a) ([atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*target, [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) value) |
| static [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) | [atomic\_sub](#a1283fcb168cc85f65dfcdf973bf47cbb) ([atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*target, [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) value) |
| static [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) | [atomic\_inc](#a66487deb6817076501dd9160537fc06a) ([atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*target) |
| static [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) | [atomic\_dec](#a0adecd95c4d47987c404a31e87c1d5c5) ([atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*target) |
| static [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) | [atomic\_get](#adfe62ad2c8d64b0545b9e31f936bb79b) (const [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*target) |
| static [atomic\_ptr\_val\_t](atomic__types_8h.md#a374deb49b6dab1420a835b01433eb2f4) | [atomic\_ptr\_get](#a8efb153bce3bee1616852bda40d12ce5) (const [atomic\_ptr\_t](atomic__types_8h.md#acad6866fa4c844026cd9f8c3fb60ecd7) \*target) |
| static [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) | [atomic\_set](#a51f73cb439192f354f36b19018d88a13) ([atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*target, [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) value) |
| static [atomic\_ptr\_val\_t](atomic__types_8h.md#a374deb49b6dab1420a835b01433eb2f4) | [atomic\_ptr\_set](#aa4e97fffda847d0d53b53d79819359a8) ([atomic\_ptr\_t](atomic__types_8h.md#acad6866fa4c844026cd9f8c3fb60ecd7) \*target, [atomic\_ptr\_val\_t](atomic__types_8h.md#a374deb49b6dab1420a835b01433eb2f4) value) |
| static [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) | [atomic\_clear](#a45ccf5a7d636206f0673139ac393946f) ([atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*target) |
| static [atomic\_ptr\_val\_t](atomic__types_8h.md#a374deb49b6dab1420a835b01433eb2f4) | [atomic\_ptr\_clear](#a8b511a7b5bccc7bc6b6e13526f87c0f3) ([atomic\_ptr\_t](atomic__types_8h.md#acad6866fa4c844026cd9f8c3fb60ecd7) \*target) |
| static [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) | [atomic\_or](#ac96691d8703907941e81849b5aea42b4) ([atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*target, [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) value) |
| static [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) | [atomic\_xor](#a189eb9d39c3945194e64cdc55ae98deb) ([atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*target, [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) value) |
| static [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) | [atomic\_and](#ace9913fc4e103b5a1f27d29e8c12c41c) ([atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*target, [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) value) |
| static [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) | [atomic\_nand](#aa04dbd054869e89ef234eb35be41798a) ([atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*target, [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) value) |

## Function Documentation

## [◆ ](#aed809d451c08b151dd8e20db3f12926a)atomic\_add()

| | [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) atomic\_add | ( | [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \* | *target*, | | --- | --- | --- | --- | |  |  | [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) | *value* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#ace9913fc4e103b5a1f27d29e8c12c41c)atomic\_and()

| | [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) atomic\_and | ( | [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \* | *target*, | | --- | --- | --- | --- | |  |  | [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) | *value* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a6a4a6dea8c56d6a78bc57d87a1f79450)atomic\_cas()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) atomic\_cas | ( | [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \* | *target*, | | --- | --- | --- | --- | |  |  | [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) | *old\_value*, | |  |  | [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) | *new\_value* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a45ccf5a7d636206f0673139ac393946f)atomic\_clear()

| | [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) atomic\_clear | ( | [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \* | *target* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a0adecd95c4d47987c404a31e87c1d5c5)atomic\_dec()

| | [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) atomic\_dec | ( | [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \* | *target* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#adfe62ad2c8d64b0545b9e31f936bb79b)atomic\_get()

| | [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) atomic\_get | ( | const [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \* | *target* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a66487deb6817076501dd9160537fc06a)atomic\_inc()

| | [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) atomic\_inc | ( | [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \* | *target* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#aa04dbd054869e89ef234eb35be41798a)atomic\_nand()

| | [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) atomic\_nand | ( | [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \* | *target*, | | --- | --- | --- | --- | |  |  | [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) | *value* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#ac96691d8703907941e81849b5aea42b4)atomic\_or()

| | [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) atomic\_or | ( | [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \* | *target*, | | --- | --- | --- | --- | |  |  | [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) | *value* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a1ee94308793379944e8e28371e1d135b)atomic\_ptr\_cas()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) atomic\_ptr\_cas | ( | [atomic\_ptr\_t](atomic__types_8h.md#acad6866fa4c844026cd9f8c3fb60ecd7) \* | *target*, | | --- | --- | --- | --- | |  |  | [atomic\_ptr\_val\_t](atomic__types_8h.md#a374deb49b6dab1420a835b01433eb2f4) | *old\_value*, | |  |  | [atomic\_ptr\_val\_t](atomic__types_8h.md#a374deb49b6dab1420a835b01433eb2f4) | *new\_value* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a8b511a7b5bccc7bc6b6e13526f87c0f3)atomic\_ptr\_clear()

| | [atomic\_ptr\_val\_t](atomic__types_8h.md#a374deb49b6dab1420a835b01433eb2f4) atomic\_ptr\_clear | ( | [atomic\_ptr\_t](atomic__types_8h.md#acad6866fa4c844026cd9f8c3fb60ecd7) \* | *target* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a8efb153bce3bee1616852bda40d12ce5)atomic\_ptr\_get()

| | [atomic\_ptr\_val\_t](atomic__types_8h.md#a374deb49b6dab1420a835b01433eb2f4) atomic\_ptr\_get | ( | const [atomic\_ptr\_t](atomic__types_8h.md#acad6866fa4c844026cd9f8c3fb60ecd7) \* | *target* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#aa4e97fffda847d0d53b53d79819359a8)atomic\_ptr\_set()

| | [atomic\_ptr\_val\_t](atomic__types_8h.md#a374deb49b6dab1420a835b01433eb2f4) atomic\_ptr\_set | ( | [atomic\_ptr\_t](atomic__types_8h.md#acad6866fa4c844026cd9f8c3fb60ecd7) \* | *target*, | | --- | --- | --- | --- | |  |  | [atomic\_ptr\_val\_t](atomic__types_8h.md#a374deb49b6dab1420a835b01433eb2f4) | *value* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a51f73cb439192f354f36b19018d88a13)atomic\_set()

| | [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) atomic\_set | ( | [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \* | *target*, | | --- | --- | --- | --- | |  |  | [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) | *value* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a1283fcb168cc85f65dfcdf973bf47cbb)atomic\_sub()

| | [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) atomic\_sub | ( | [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \* | *target*, | | --- | --- | --- | --- | |  |  | [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) | *value* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a189eb9d39c3945194e64cdc55ae98deb)atomic\_xor()

| | [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) atomic\_xor | ( | [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \* | *target*, | | --- | --- | --- | --- | |  |  | [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) | *value* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [sys](dir_85ec07b7ac0b888617bae1400221d199.md)
- [atomic\_builtin.h](atomic__builtin_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
