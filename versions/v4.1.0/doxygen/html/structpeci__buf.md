---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structpeci__buf.html
original_path: doxygen/html/structpeci__buf.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

peci\_buf Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [PECI Interface](group__peci__interface.md)

PECI buffer structure.
[More...](#details)

`#include <[peci.h](peci_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | [buf](#aca55975957106666161da358b7f85db6) |
|  | Valid pointer on a data buffer, or NULL otherwise. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [len](#a8e3fd0ef3f9141113214b89bb589a5e9) |
|  | Length of the data buffer expected to be received without considering the frame check sequence byte. |

## Detailed Description

PECI buffer structure.

## Field Documentation

## [◆ ](#aca55975957106666161da358b7f85db6)buf

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)\* peci\_buf::buf |
| --- |

Valid pointer on a data buffer, or NULL otherwise.

## [◆ ](#a8e3fd0ef3f9141113214b89bb589a5e9)len

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) peci\_buf::len |
| --- |

Length of the data buffer expected to be received without considering the frame check sequence byte.

Note
:   Frame check sequence byte is added into rx buffer: need to allocate an additional byte for this in rx buffer.

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[peci.h](peci_8h_source.md)

- [peci\_buf](structpeci__buf.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
