---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structi3c__ibi__payload.html
original_path: doxygen/html/structi3c__ibi__payload.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

i3c\_ibi\_payload Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [I3C Interface](group__i3c__interface.md) » [I3C In-Band Interrupts](group__i3c__ibi.md)

Structure of payload buffer for IBI.
[More...](#details)

`#include <[ibi.h](ibi_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [payload\_len](#aad4208fcdfef0bc9fb67c86ee1d302de) |
|  | Length of available data in the payload buffer. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [payload](#ab869cf38c7a9677fda3ecf48cd358355) [0] |
|  | Pointer to byte array as payload buffer. |

## Detailed Description

Structure of payload buffer for IBI.

This is used for the IBI callback.

## Field Documentation

## [◆ ](#ab869cf38c7a9677fda3ecf48cd358355)payload

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) i3c\_ibi\_payload::payload[0] |
| --- |

Pointer to byte array as payload buffer.

## [◆ ](#aad4208fcdfef0bc9fb67c86ee1d302de)payload\_len

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) i3c\_ibi\_payload::payload\_len |
| --- |

Length of available data in the payload buffer.

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/i3c/[ibi.h](ibi_8h_source.md)

- [i3c\_ibi\_payload](structi3c__ibi__payload.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
