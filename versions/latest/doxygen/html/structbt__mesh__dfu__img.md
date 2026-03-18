---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structbt__mesh__dfu__img.html
original_path: doxygen/html/structbt__mesh__dfu__img.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_mesh\_dfu\_img Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Mesh](group__bt__mesh.md) » [Bluetooth Mesh Device Firmware Update](group__bt__mesh__dfu.md)

DFU image instance.
[More...](#details)

`#include <[dfu.h](dfu_8h_source.md)>`

| Data Fields | |
| --- | --- |
| const void \* | [fwid](#aa4d91e47dd4c20939d8ef8ada0b86f83) |
|  | Firmware ID. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [fwid\_len](#a97e17c59a0528462d554d6bbe78858da) |
|  | Length of the firmware ID. |
| const char \* | [uri](#a578b2932efb07a3e4eb80043902cc7a0) |
|  | Update URI, or NULL. |

## Detailed Description

DFU image instance.

Each DFU image represents a single updatable firmware image.

## Field Documentation

## [◆ ](#aa4d91e47dd4c20939d8ef8ada0b86f83)fwid

| const void\* bt\_mesh\_dfu\_img::fwid |
| --- |

Firmware ID.

## [◆ ](#a97e17c59a0528462d554d6bbe78858da)fwid\_len

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) bt\_mesh\_dfu\_img::fwid\_len |
| --- |

Length of the firmware ID.

## [◆ ](#a578b2932efb07a3e4eb80043902cc7a0)uri

| const char\* bt\_mesh\_dfu\_img::uri |
| --- |

Update URI, or NULL.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/mesh/[dfu.h](dfu_8h_source.md)

- [bt\_mesh\_dfu\_img](structbt__mesh__dfu__img.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
