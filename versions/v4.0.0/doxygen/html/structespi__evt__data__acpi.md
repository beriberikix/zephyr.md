---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structespi__evt__data__acpi.html
original_path: doxygen/html/structespi__evt__data__acpi.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

espi\_evt\_data\_acpi Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [ESPI Driver APIs](group__espi__interface.md)

Bit field definition of evt\_data in struct [espi\_event](structespi__event.md "eSPI event") for ACPI.
[More...](#details)

`#include <[espi.h](espi_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [type](#aa5d1e0b548e9be6b65daf67316df8bfe):8 |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [data](#a8fb3633a97b1af7618b391539f576c6f):8 |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [reserved](#acb291c371bb201d0ceb739fca7e22d3b):16 |

## Detailed Description

Bit field definition of evt\_data in struct [espi\_event](structespi__event.md "eSPI event") for ACPI.

## Field Documentation

## [◆ ](#a8fb3633a97b1af7618b391539f576c6f)data

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) espi\_evt\_data\_acpi::data |
| --- |

## [◆ ](#acb291c371bb201d0ceb739fca7e22d3b)reserved

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) espi\_evt\_data\_acpi::reserved |
| --- |

## [◆ ](#aa5d1e0b548e9be6b65daf67316df8bfe)type

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) espi\_evt\_data\_acpi::type |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[espi.h](espi_8h_source.md)

- [espi\_evt\_data\_acpi](structespi__evt__data__acpi.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
