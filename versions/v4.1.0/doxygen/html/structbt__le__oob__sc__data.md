---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structbt__le__oob__sc__data.html
original_path: doxygen/html/structbt__le__oob__sc__data.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_le\_oob\_sc\_data Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Generic Access Profile (GAP)](group__bt__gap.md)

LE Secure Connections pairing Out of Band data.
[More...](#details)

`#include <[bluetooth.h](bluetooth_2bluetooth_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [r](#afa64bcc048d0e8709e262e2848a39d2c) [16] |
|  | Random Number. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [c](#a9bd93f1e9e41e241d0f84ae16ae47ba1) [16] |
|  | Confirm Value. |

## Detailed Description

LE Secure Connections pairing Out of Band data.

## Field Documentation

## [◆ ](#a9bd93f1e9e41e241d0f84ae16ae47ba1)c

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_le\_oob\_sc\_data::c[16] |
| --- |

Confirm Value.

## [◆ ](#afa64bcc048d0e8709e262e2848a39d2c)r

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_le\_oob\_sc\_data::r[16] |
| --- |

Random Number.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[bluetooth.h](bluetooth_2bluetooth_8h_source.md)

- [bt\_le\_oob\_sc\_data](structbt__le__oob__sc__data.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
