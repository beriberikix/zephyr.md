---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structbt__vocs__register__param.html
original_path: doxygen/html/structbt__vocs__register__param.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_vocs\_register\_param Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Volume Offset Control Service (VOCS)](group__bt__vocs.md)

Structure for registering a Volume Offset Control Service instance.
[More...](#details)

`#include <[vocs.h](vocs_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [location](#a0572c60319c8984e2437e596584c46f5) |
|  | Audio Location bitmask. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [location\_writable](#a6919f965abfa1fec39a3c8e0f29c04f3) |
|  | Boolean to set whether the location is writable by clients. |
| [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) | [offset](#ac1c2475cd390f5acf840f92ea45c6d31) |
|  | Initial volume offset (-255 to 255). |
| char \* | [output\_desc](#a1f6baed09dc35b974d06f1426b671e05) |
|  | Initial audio output description. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [desc\_writable](#aace5987e890c8b4dbf3e01fa5c2a4432) |
|  | Boolean to set whether the description is writable by clients. |
| struct [bt\_vocs\_cb](structbt__vocs__cb.md) \* | [cb](#a306ad3c712bb5a5109f3afb4912d590b) |
|  | Pointer to the callback structure. |

## Detailed Description

Structure for registering a Volume Offset Control Service instance.

## Field Documentation

## [◆ ](#a306ad3c712bb5a5109f3afb4912d590b)cb

| struct [bt\_vocs\_cb](structbt__vocs__cb.md)\* bt\_vocs\_register\_param::cb |
| --- |

Pointer to the callback structure.

## [◆ ](#aace5987e890c8b4dbf3e01fa5c2a4432)desc\_writable

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) bt\_vocs\_register\_param::desc\_writable |
| --- |

Boolean to set whether the description is writable by clients.

## [◆ ](#a0572c60319c8984e2437e596584c46f5)location

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) bt\_vocs\_register\_param::location |
| --- |

Audio Location bitmask.

## [◆ ](#a6919f965abfa1fec39a3c8e0f29c04f3)location\_writable

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) bt\_vocs\_register\_param::location\_writable |
| --- |

Boolean to set whether the location is writable by clients.

## [◆ ](#ac1c2475cd390f5acf840f92ea45c6d31)offset

| [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) bt\_vocs\_register\_param::offset |
| --- |

Initial volume offset (-255 to 255).

## [◆ ](#a1f6baed09dc35b974d06f1426b671e05)output\_desc

| char\* bt\_vocs\_register\_param::output\_desc |
| --- |

Initial audio output description.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/audio/[vocs.h](vocs_8h_source.md)

- [bt\_vocs\_register\_param](structbt__vocs__register__param.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
