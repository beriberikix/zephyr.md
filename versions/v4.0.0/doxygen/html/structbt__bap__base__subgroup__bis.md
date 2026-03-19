---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structbt__bap__base__subgroup__bis.html
original_path: doxygen/html/structbt__bap__base__subgroup__bis.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_bap\_base\_subgroup\_bis Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Basic Audio Profile](group__bt__bap.md) » [BAP Broadcast APIs](group__bt__bap__broadcast.md)

BIS structure for each BIS in a Broadcast Audio Source Endpoint (BASE) subgroup.
[More...](#details)

`#include <[bap.h](bap_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [index](#ad0f5dff3150c36b1625f1f6f206d41d2) |
|  | Unique index of the BIS. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [data\_len](#ac4132c798c04c0f93c944dc91891221e) |
|  | Codec Specific Data length. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | [data](#aa53f22b29e447822e8bb36d9245bfc77) |
|  | Codec Specific Data. |

## Detailed Description

BIS structure for each BIS in a Broadcast Audio Source Endpoint (BASE) subgroup.

## Field Documentation

## [◆ ](#aa53f22b29e447822e8bb36d9245bfc77)data

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)\* bt\_bap\_base\_subgroup\_bis::data |
| --- |

Codec Specific Data.

## [◆ ](#ac4132c798c04c0f93c944dc91891221e)data\_len

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_bap\_base\_subgroup\_bis::data\_len |
| --- |

Codec Specific Data length.

## [◆ ](#ad0f5dff3150c36b1625f1f6f206d41d2)index

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_bap\_base\_subgroup\_bis::index |
| --- |

Unique index of the BIS.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/audio/[bap.h](bap_8h_source.md)

- [bt\_bap\_base\_subgroup\_bis](structbt__bap__base__subgroup__bis.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
