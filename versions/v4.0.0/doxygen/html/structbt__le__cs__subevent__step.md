---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structbt__le__cs__subevent__step.html
original_path: doxygen/html/structbt__le__cs__subevent__step.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_le\_cs\_subevent\_step Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Channel Sounding (CS)](group__bt__le__cs.md)

Subevent result step.
[More...](#details)

`#include <[cs.h](cs_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [mode](#a82103efe7c897abdf5bbb9c0a23cfba4) |
|  | CS step mode. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [channel](#a54b47ddae09d8ab3f57124f71c4efbca) |
|  | CS step channel index. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [data\_len](#a32d2c13c5513220cf1cd7a13fb18c501) |
|  | Length of role- and mode-specific information being reported. |
| const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | [data](#a46494728a82c6d50f6acd8f88e1a0842) |
|  | Pointer to role- and mode-specific information. |

## Detailed Description

Subevent result step.

## Field Documentation

## [◆ ](#a54b47ddae09d8ab3f57124f71c4efbca)channel

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_le\_cs\_subevent\_step::channel |
| --- |

CS step channel index.

## [◆ ](#a46494728a82c6d50f6acd8f88e1a0842)data

| const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)\* bt\_le\_cs\_subevent\_step::data |
| --- |

Pointer to role- and mode-specific information.

## [◆ ](#a32d2c13c5513220cf1cd7a13fb18c501)data\_len

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_le\_cs\_subevent\_step::data\_len |
| --- |

Length of role- and mode-specific information being reported.

## [◆ ](#a82103efe7c897abdf5bbb9c0a23cfba4)mode

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_le\_cs\_subevent\_step::mode |
| --- |

CS step mode.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[cs.h](cs_8h_source.md)

- [bt\_le\_cs\_subevent\_step](structbt__le__cs__subevent__step.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
