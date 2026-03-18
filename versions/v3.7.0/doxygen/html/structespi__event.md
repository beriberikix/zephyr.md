---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structespi__event.html
original_path: doxygen/html/structespi__event.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

espi\_event Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [ESPI Driver APIs](group__espi__interface.md)

eSPI event
[More...](#details)

`#include <[espi.h](espi_8h_source.md)>`

| Data Fields | |
| --- | --- |
| enum [espi\_bus\_event](group__espi__interface.md#ga36ac3fbf9813f78bad90f047e1eb1128) | [evt\_type](#acac75eb1d2b384aa337a5240825b635f) |
|  | Event type. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [evt\_details](#aea36925bd3f599c1481c9cc867795c33) |
|  | Additional details for bus event type. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [evt\_data](#aa0491cbed5bec091721dfa14898b7277) |
|  | Data associated to the event. |

## Detailed Description

eSPI event

## Field Documentation

## [◆ ](#aa0491cbed5bec091721dfa14898b7277)evt\_data

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) espi\_event::evt\_data |
| --- |

Data associated to the event.

## [◆ ](#aea36925bd3f599c1481c9cc867795c33)evt\_details

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) espi\_event::evt\_details |
| --- |

Additional details for bus event type.

## [◆ ](#acac75eb1d2b384aa337a5240825b635f)evt\_type

| enum [espi\_bus\_event](group__espi__interface.md#ga36ac3fbf9813f78bad90f047e1eb1128) espi\_event::evt\_type |
| --- |

Event type.

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[espi.h](espi_8h_source.md)

- [espi\_event](structespi__event.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
