---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structespi__saf__packet.html
original_path: doxygen/html/structespi__saf__packet.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

espi\_saf\_packet Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [ESPI Driver APIs](group__espi__interface.md)

eSPI SAF transaction packet format
[More...](#details)

`#include <[espi_saf.h](espi__saf_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [flash\_addr](#a8ee8a45b3490746f893f6b17fb96b815) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | [buf](#a00bfcab9fe2b928be3ea3485c5e91401) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [len](#af88017b76b64b77c95d9684981f48482) |

## Detailed Description

eSPI SAF transaction packet format

## Field Documentation

## [◆ ](#a00bfcab9fe2b928be3ea3485c5e91401)buf

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)\* espi\_saf\_packet::buf |
| --- |

## [◆ ](#a8ee8a45b3490746f893f6b17fb96b815)flash\_addr

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) espi\_saf\_packet::flash\_addr |
| --- |

## [◆ ](#af88017b76b64b77c95d9684981f48482)len

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) espi\_saf\_packet::len |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[espi\_saf.h](espi__saf_8h_source.md)

- [espi\_saf\_packet](structespi__saf__packet.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
