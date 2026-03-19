---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structmb__image.html
original_path: doxygen/html/structmb__image.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mb\_image Struct Reference

[Third-party](group__third__party.md) » [BBC micro:bit display APIs](group__mb__display.md)

Representation of a BBC micro:bit display image.
[More...](#details)

`#include <[mb_display.h](mb__display_8h_source.md)>`

| Data Fields | |
| --- | --- |
| union { |  |
| struct { |  |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)   [c1](#a044fee7be7fb1e5b3e2c2dab74011d9a):1 |  |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)   [c2](#ad7eb096bb15a0bb8378bae32804fe6c6):1 |  |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)   [c3](#a88455e59017a73533e727671019f6ea0):1 |  |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)   [c4](#a506e5ac82c7229ba7e89f67de8fbcbe2):1 |  |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)   [c5](#a2af8f97c0ddc8cf463cf83a483e3025b):1 |  |
| }   [r](#a93ec1bb1c0cdc09de75d00976bd23eeb) [5] |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)   [row](#a158f0bdbb7d135da0dcf5c6b997d0ff5) [5] |  |
| }; |  |

## Detailed Description

Representation of a BBC micro:bit display image.

This struct should normally not be used directly, rather created using the [MB\_IMAGE()](group__mb__display.md#ga529a5650acaf699b23b4b4234127cf2c "Generate an image object from a given array rows/columns.") macro.

## Field Documentation

## [◆ ](#ad557daa0c80ebb2e3c314ecf1da234c5)[union]

| union { ... } [mb\_image](structmb__image.md) |
| --- |

## [◆ ](#a044fee7be7fb1e5b3e2c2dab74011d9a)c1

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) mb\_image::c1 |
| --- |

## [◆ ](#ad7eb096bb15a0bb8378bae32804fe6c6)c2

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) mb\_image::c2 |
| --- |

## [◆ ](#a88455e59017a73533e727671019f6ea0)c3

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) mb\_image::c3 |
| --- |

## [◆ ](#a506e5ac82c7229ba7e89f67de8fbcbe2)c4

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) mb\_image::c4 |
| --- |

## [◆ ](#a2af8f97c0ddc8cf463cf83a483e3025b)c5

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) mb\_image::c5 |
| --- |

## [◆ ](#a93ec1bb1c0cdc09de75d00976bd23eeb)[struct]

| struct { ... } mb\_image::r[5] |
| --- |

## [◆ ](#a158f0bdbb7d135da0dcf5c6b997d0ff5)row

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) mb\_image::row[5] |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/display/[mb\_display.h](mb__display_8h_source.md)

- [mb\_image](structmb__image.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
