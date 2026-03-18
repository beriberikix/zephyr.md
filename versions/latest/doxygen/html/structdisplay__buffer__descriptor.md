---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structdisplay__buffer__descriptor.html
original_path: doxygen/html/structdisplay__buffer__descriptor.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

display\_buffer\_descriptor Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [Display Interface](group__display__interface.md)

Structure to describe display data buffer layout.
[More...](#details)

`#include <[display.h](display_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [buf\_size](#aee9f34a6944b8e28622ab06d6907d40a) |
|  | Data buffer size in bytes. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [width](#aa35cf372266199308211d28dae789be3) |
|  | Data buffer row width in pixels. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [height](#a572c6560903553b6853360fd29631b95) |
|  | Data buffer column height in pixels. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [pitch](#a00d7d8da4e61f404ad353b9a8f49b2eb) |
|  | Number of pixels between consecutive rows in the data buffer. |

## Detailed Description

Structure to describe display data buffer layout.

## Field Documentation

## [◆ ](#aee9f34a6944b8e28622ab06d6907d40a)buf\_size

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) display\_buffer\_descriptor::buf\_size |
| --- |

Data buffer size in bytes.

## [◆ ](#a572c6560903553b6853360fd29631b95)height

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) display\_buffer\_descriptor::height |
| --- |

Data buffer column height in pixels.

## [◆ ](#a00d7d8da4e61f404ad353b9a8f49b2eb)pitch

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) display\_buffer\_descriptor::pitch |
| --- |

Number of pixels between consecutive rows in the data buffer.

## [◆ ](#aa35cf372266199308211d28dae789be3)width

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) display\_buffer\_descriptor::width |
| --- |

Data buffer row width in pixels.

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[display.h](display_8h_source.md)

- [display\_buffer\_descriptor](structdisplay__buffer__descriptor.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
