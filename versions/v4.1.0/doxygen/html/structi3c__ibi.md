---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structi3c__ibi.html
original_path: doxygen/html/structi3c__ibi.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

i3c\_ibi Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [I3C Interface](group__i3c__interface.md) » [I3C In-Band Interrupts](group__i3c__ibi.md)

Struct for IBI request.
[More...](#details)

`#include <[ibi.h](ibi_8h_source.md)>`

| Data Fields | |
| --- | --- |
| enum [i3c\_ibi\_type](group__i3c__ibi.md#gaf4be72fc9c862d996d860c0b7fbc862b) | [ibi\_type](#a88b0ccd636c042ca929412c42a05bc25) |
|  | Type of IBI. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | [payload](#a584e3298059e412d7d3671a451ecc117) |
|  | Pointer to payload of IBI. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [payload\_len](#aa51b8214d4a0708861ac9617f844043f) |
|  | Length in bytes of the IBI payload. |

## Detailed Description

Struct for IBI request.

## Field Documentation

## [◆ ](#a88b0ccd636c042ca929412c42a05bc25)ibi\_type

| enum [i3c\_ibi\_type](group__i3c__ibi.md#gaf4be72fc9c862d996d860c0b7fbc862b) i3c\_ibi::ibi\_type |
| --- |

Type of IBI.

## [◆ ](#a584e3298059e412d7d3671a451ecc117)payload

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)\* i3c\_ibi::payload |
| --- |

Pointer to payload of IBI.

## [◆ ](#aa51b8214d4a0708861ac9617f844043f)payload\_len

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) i3c\_ibi::payload\_len |
| --- |

Length in bytes of the IBI payload.

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/i3c/[ibi.h](ibi_8h_source.md)

- [i3c\_ibi](structi3c__ibi.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
