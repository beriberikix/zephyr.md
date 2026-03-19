---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structespi__request__packet.html
original_path: doxygen/html/structespi__request__packet.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

espi\_request\_packet Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [ESPI Driver APIs](group__espi__interface.md)

eSPI peripheral request packet format
[More...](#details)

`#include <[espi.h](espi_8h_source.md)>`

| Data Fields | |
| --- | --- |
| enum [espi\_cycle\_type](group__espi__interface.md#ga3e52615f244d7fa8ccda495ab8ec8a5b) | [cycle\_type](#a9b474155dfa0c74d0bd55e4b831b383a) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [tag](#a22a0111e338827125eaf79ce8516b744) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [len](#ae8b7dc12b04f469b5689ad27cc4f0643) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [address](#a4ac2d50786fdc4c4bd8da88bde28f77d) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | [data](#a6f808763faf949ff7ef83d68fb71e7ba) |

## Detailed Description

eSPI peripheral request packet format

## Field Documentation

## [◆ ](#a4ac2d50786fdc4c4bd8da88bde28f77d)address

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) espi\_request\_packet::address |
| --- |

## [◆ ](#a9b474155dfa0c74d0bd55e4b831b383a)cycle\_type

| enum [espi\_cycle\_type](group__espi__interface.md#ga3e52615f244d7fa8ccda495ab8ec8a5b) espi\_request\_packet::cycle\_type |
| --- |

## [◆ ](#a6f808763faf949ff7ef83d68fb71e7ba)data

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)\* espi\_request\_packet::data |
| --- |

## [◆ ](#ae8b7dc12b04f469b5689ad27cc4f0643)len

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) espi\_request\_packet::len |
| --- |

## [◆ ](#a22a0111e338827125eaf79ce8516b744)tag

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) espi\_request\_packet::tag |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[espi.h](espi_8h_source.md)

- [espi\_request\_packet](structespi__request__packet.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
