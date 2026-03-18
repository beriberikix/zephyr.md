---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structbt__mesh__dfu__slot.html
original_path: doxygen/html/structbt__mesh__dfu__slot.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_mesh\_dfu\_slot Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Mesh](group__bt__mesh.md) » [Bluetooth Mesh Device Firmware Update](group__bt__mesh__dfu.md)

DFU image slot for DFU distribution.
[More...](#details)

`#include <[dfu.h](dfu_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [size](#a3f6258793af506b639dd384562fc4a20) |
|  | Size of the firmware in bytes. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [fwid\_len](#a47ab534d52e931155dfc7cf4e2444999) |
|  | Length of the firmware ID. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [metadata\_len](#af3e056bf835365afda82f3ec8342d926) |
|  | Length of the metadata. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [fwid](#a9ab5db428c7d57803d6bbc5f26f9c7bb) [0] |
|  | Firmware ID. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [metadata](#aa554bde6cdffa419ada8ea7410118947) [0] |
|  | Metadata. |

## Detailed Description

DFU image slot for DFU distribution.

## Field Documentation

## [◆ ](#a9ab5db428c7d57803d6bbc5f26f9c7bb)fwid

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_mesh\_dfu\_slot::fwid[0] |
| --- |

Firmware ID.

## [◆ ](#a47ab534d52e931155dfc7cf4e2444999)fwid\_len

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) bt\_mesh\_dfu\_slot::fwid\_len |
| --- |

Length of the firmware ID.

## [◆ ](#aa554bde6cdffa419ada8ea7410118947)metadata

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_mesh\_dfu\_slot::metadata[0] |
| --- |

Metadata.

## [◆ ](#af3e056bf835365afda82f3ec8342d926)metadata\_len

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) bt\_mesh\_dfu\_slot::metadata\_len |
| --- |

Length of the metadata.

## [◆ ](#a3f6258793af506b639dd384562fc4a20)size

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) bt\_mesh\_dfu\_slot::size |
| --- |

Size of the firmware in bytes.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/mesh/[dfu.h](dfu_8h_source.md)

- [bt\_mesh\_dfu\_slot](structbt__mesh__dfu__slot.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
