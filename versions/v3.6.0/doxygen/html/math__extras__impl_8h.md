---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/math__extras__impl_8h.html
original_path: doxygen/html/math__extras__impl_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

math\_extras\_impl.h File Reference

Inline implementation of functions declared in [math\_extras.h](math__extras_8h.md).
[More...](#details)

`#include <[zephyr/toolchain.h](toolchain_8h_source.md)>`

[Go to the source code of this file.](math__extras__impl_8h_source.md)

| Macros | |
| --- | --- |
| #define | [use\_builtin](#a64a27aae3fe9b5182e18f3bf424eb7f5)(x) |

| Functions | |
| --- | --- |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [u16\_add\_overflow](#a62d018abdf97551665cab7486b5a519a) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) a, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) b, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*result) |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [u32\_add\_overflow](#a3f36aa272f5595d78c6e8219b2c4dbfb) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) a, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) b, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*result) |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [u64\_add\_overflow](#af98ec1d8b1c00e30382eed01853e3307) ([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) a, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) b, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*result) |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [size\_add\_overflow](#a7aaec179564038b540aaf4ab3c9a666d) ([size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) a, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) b, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \*result) |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [u16\_mul\_overflow](#a292df7083a9da5525cda13e2546e81ba) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) a, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) b, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*result) |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [u32\_mul\_overflow](#a427e8cd4fcafab244576994acc9b960f) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) a, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) b, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*result) |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [u64\_mul\_overflow](#a366f6606874071677bf9079647d9abce) ([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) a, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) b, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*result) |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [size\_mul\_overflow](#a790b24a5d239afcc08d9e4f66c25ea56) ([size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) a, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) b, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \*result) |
| static int | [u32\_count\_leading\_zeros](#a97e8d8a40a45899ab7e5ce718342536b) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) x) |
| static int | [u64\_count\_leading\_zeros](#af5f31e98f2f675a0b4cc54b7fba6f56c) ([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) x) |
| static int | [u32\_count\_trailing\_zeros](#a4cb313f98c3fd3b00d6f4db74a9a0076) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) x) |
| static int | [u64\_count\_trailing\_zeros](#a300356629c0388d37958ef026180ea4d) ([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) x) |

## Detailed Description

Inline implementation of functions declared in [math\_extras.h](math__extras_8h.md).

## Macro Definition Documentation

## [◆ ](#a64a27aae3fe9b5182e18f3bf424eb7f5)use\_builtin

| #define use\_builtin | ( |  | *x* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[HAS\_BUILTIN](toolchain_8h.md#a474a719388efd0578c7c98a0961e23dd)(x)

[HAS\_BUILTIN](toolchain_8h.md#a474a719388efd0578c7c98a0961e23dd)

#define HAS\_BUILTIN(x)

Check if the compiler supports the built-in function x.

**Definition** toolchain.h:33

## Function Documentation

## [◆ ](#a7aaec179564038b540aaf4ab3c9a666d)size\_add\_overflow()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) size\_add\_overflow | ( | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *a*, | | --- | --- | --- | --- | |  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *b*, | |  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \* | *result* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a790b24a5d239afcc08d9e4f66c25ea56)size\_mul\_overflow()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) size\_mul\_overflow | ( | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *a*, | | --- | --- | --- | --- | |  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *b*, | |  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \* | *result* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a62d018abdf97551665cab7486b5a519a)u16\_add\_overflow()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) u16\_add\_overflow | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *a*, | | --- | --- | --- | --- | |  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *b*, | |  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \* | *result* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a292df7083a9da5525cda13e2546e81ba)u16\_mul\_overflow()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) u16\_mul\_overflow | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *a*, | | --- | --- | --- | --- | |  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *b*, | |  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \* | *result* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a3f36aa272f5595d78c6e8219b2c4dbfb)u32\_add\_overflow()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) u32\_add\_overflow | ( | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *a*, | | --- | --- | --- | --- | |  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *b*, | |  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \* | *result* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a97e8d8a40a45899ab7e5ce718342536b)u32\_count\_leading\_zeros()

| | int u32\_count\_leading\_zeros | ( | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *x* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a4cb313f98c3fd3b00d6f4db74a9a0076)u32\_count\_trailing\_zeros()

| | int u32\_count\_trailing\_zeros | ( | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *x* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a427e8cd4fcafab244576994acc9b960f)u32\_mul\_overflow()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) u32\_mul\_overflow | ( | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *a*, | | --- | --- | --- | --- | |  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *b*, | |  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \* | *result* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#af98ec1d8b1c00e30382eed01853e3307)u64\_add\_overflow()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) u64\_add\_overflow | ( | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *a*, | | --- | --- | --- | --- | |  |  | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *b*, | |  |  | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \* | *result* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#af5f31e98f2f675a0b4cc54b7fba6f56c)u64\_count\_leading\_zeros()

| | int u64\_count\_leading\_zeros | ( | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *x* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a300356629c0388d37958ef026180ea4d)u64\_count\_trailing\_zeros()

| | int u64\_count\_trailing\_zeros | ( | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *x* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a366f6606874071677bf9079647d9abce)u64\_mul\_overflow()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) u64\_mul\_overflow | ( | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *a*, | | --- | --- | --- | --- | |  |  | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *b*, | |  |  | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \* | *result* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [sys](dir_85ec07b7ac0b888617bae1400221d199.md)
- [math\_extras\_impl.h](math__extras__impl_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
