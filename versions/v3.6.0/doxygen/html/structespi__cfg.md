---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structespi__cfg.html
original_path: doxygen/html/structespi__cfg.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

espi\_cfg Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [ESPI Driver APIs](group__espi__interface.md)

eSPI bus configuration parameters
[More...](#details)

`#include <[espi.h](espi_8h_source.md)>`

| Data Fields | |
| --- | --- |
| enum [espi\_io\_mode](group__espi__interface.md#ga0d7c61f1f4ec611d0c8a67ba73e2b4f0) | [io\_caps](#a75175c60a31c3a88c83772b99c2a5c34) |
|  | Supported I/O mode. |
| enum [espi\_channel](group__espi__interface.md#gafaa3f7d54503c901ab23bd79a7f8a755) | [channel\_caps](#abb24c88ecc977d8116973d44a7e7cb94) |
|  | Supported channels. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [max\_freq](#aed88dd6fc8028a7c281260e7fa29ce21) |
|  | Maximum supported frequency in MHz. |

## Detailed Description

eSPI bus configuration parameters

## Field Documentation

## [◆ ](#abb24c88ecc977d8116973d44a7e7cb94)channel\_caps

| enum [espi\_channel](group__espi__interface.md#gafaa3f7d54503c901ab23bd79a7f8a755) espi\_cfg::channel\_caps |
| --- |

Supported channels.

## [◆ ](#a75175c60a31c3a88c83772b99c2a5c34)io\_caps

| enum [espi\_io\_mode](group__espi__interface.md#ga0d7c61f1f4ec611d0c8a67ba73e2b4f0) espi\_cfg::io\_caps |
| --- |

Supported I/O mode.

## [◆ ](#aed88dd6fc8028a7c281260e7fa29ce21)max\_freq

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) espi\_cfg::max\_freq |
| --- |

Maximum supported frequency in MHz.

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[espi.h](espi_8h_source.md)

- [espi\_cfg](structespi__cfg.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
