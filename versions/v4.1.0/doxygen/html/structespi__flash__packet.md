---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structespi__flash__packet.html
original_path: doxygen/html/structespi__flash__packet.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

espi\_flash\_packet Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [ESPI Driver APIs](group__espi__interface.md)

eSPI flash transactions packet format
[More...](#details)

`#include <[espi.h](espi_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | [buf](#a22244bc4063618707eea571f170bdfde) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [flash\_addr](#ac638c0b5d0d98e15ab66850afc394cec) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [len](#adade51336ae37a519c06b12bf19fc86d) |

## Detailed Description

eSPI flash transactions packet format

## Field Documentation

## [◆ ](#a22244bc4063618707eea571f170bdfde)buf

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)\* espi\_flash\_packet::buf |
| --- |

## [◆ ](#ac638c0b5d0d98e15ab66850afc394cec)flash\_addr

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) espi\_flash\_packet::flash\_addr |
| --- |

## [◆ ](#adade51336ae37a519c06b12bf19fc86d)len

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) espi\_flash\_packet::len |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[espi.h](espi_8h_source.md)

- [espi\_flash\_packet](structespi__flash__packet.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
