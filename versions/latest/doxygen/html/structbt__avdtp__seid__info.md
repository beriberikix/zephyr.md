---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structbt__avdtp__seid__info.html
original_path: doxygen/html/structbt__avdtp__seid__info.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_avdtp\_seid\_info Struct Reference

AVDTP SEID Information.
[More...](#details)

`#include <[avdtp.h](avdtp_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [id](#a56f008e3e3fddcab2a67a21c10116a3f):6 |
|  | Stream End Point ID. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [inuse](#acb3914f52ee4decef0649fb8eb859487):1 |
|  | End Point usage status. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [rfa0](#afb8ec9e677ffcb0a6354b82bf3d473c9):1 |
|  | Reserved. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [media\_type](#a5f8e4fa4000cc21032b2f5996c07dc57):4 |
|  | Media-type of the End Point. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [tsep](#a0241167057783c20110fc23c002f4b4d):1 |
|  | TSEP of the End Point. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [rfa1](#a9a29e533600151e233b49342874bb8fa):3 |
|  | Reserved. |

## Detailed Description

AVDTP SEID Information.

## Field Documentation

## [◆ ](#a56f008e3e3fddcab2a67a21c10116a3f)id

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_avdtp\_seid\_info::id |
| --- |

Stream End Point ID.

## [◆ ](#acb3914f52ee4decef0649fb8eb859487)inuse

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_avdtp\_seid\_info::inuse |
| --- |

End Point usage status.

## [◆ ](#a5f8e4fa4000cc21032b2f5996c07dc57)media\_type

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_avdtp\_seid\_info::media\_type |
| --- |

Media-type of the End Point.

## [◆ ](#afb8ec9e677ffcb0a6354b82bf3d473c9)rfa0

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_avdtp\_seid\_info::rfa0 |
| --- |

Reserved.

## [◆ ](#a9a29e533600151e233b49342874bb8fa)rfa1

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_avdtp\_seid\_info::rfa1 |
| --- |

Reserved.

## [◆ ](#a0241167057783c20110fc23c002f4b4d)tsep

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_avdtp\_seid\_info::tsep |
| --- |

TSEP of the End Point.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[avdtp.h](avdtp_8h_source.md)

- [bt\_avdtp\_seid\_info](structbt__avdtp__seid__info.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
