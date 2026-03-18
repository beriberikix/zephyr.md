---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structsdio__func.html
original_path: doxygen/html/structsdio__func.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

sdio\_func Struct Reference

SDIO function definition.
[More...](#details)

`#include <[sd.h](sd_8h_source.md)>`

| Data Fields | |
| --- | --- |
| enum [sdio\_func\_num](sd__spec_8h.md#a3a542344967c5c1912bde216559e7cd6) | [num](#a3bc320f1ca7268344b848a998ace615c) |
|  | Function number. |
| struct [sd\_card](structsd__card.md) \* | [card](#a7387979362ba892c013a7a69e004d96b) |
|  | Card this function is present on. |
| struct [sdio\_cis](structsdio__cis.md) | [cis](#af83e71e628841b8acf70130261a97060) |
|  | CIS tuple data for this function. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [block\_size](#aa4ad13eb77f656020b38f6cf165e2965) |
|  | Current block size for this function. |

## Detailed Description

SDIO function definition.

SDIO function definition. Used to store function information per each SDIO function

## Field Documentation

## [◆ ](#aa4ad13eb77f656020b38f6cf165e2965)block\_size

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) sdio\_func::block\_size |
| --- |

Current block size for this function.

## [◆ ](#a7387979362ba892c013a7a69e004d96b)card

| struct [sd\_card](structsd__card.md)\* sdio\_func::card |
| --- |

Card this function is present on.

## [◆ ](#af83e71e628841b8acf70130261a97060)cis

| struct [sdio\_cis](structsdio__cis.md) sdio\_func::cis |
| --- |

CIS tuple data for this function.

## [◆ ](#a3bc320f1ca7268344b848a998ace615c)num

| enum [sdio\_func\_num](sd__spec_8h.md#a3a542344967c5c1912bde216559e7cd6) sdio\_func::num |
| --- |

Function number.

---

The documentation for this struct was generated from the following file:

- zephyr/sd/[sd.h](sd_8h_source.md)

- [sdio\_func](structsdio__func.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
