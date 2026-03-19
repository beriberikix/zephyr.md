---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structusbd__cctx__vendor__req.html
original_path: doxygen/html/structusbd__cctx__vendor__req.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

usbd\_cctx\_vendor\_req Struct Reference

[Connectivity](group__connectivity.md) » [USB](group__usb.md) » [USB device core API](group__usbd__api.md)

Vendor Requests Table.
[More...](#details)

`#include <[usbd.h](usbd_8h_source.md)>`

| Data Fields | |
| --- | --- |
| const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | [reqs](#a2ddf3ce0c1c0a6d788b7ef30cf8d67ea) |
|  | Array of vendor requests supported by the class. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [len](#a3b5e99bff9dbfa023a4e6a5b4a69abd0) |
|  | Length of the array. |

## Detailed Description

Vendor Requests Table.

## Field Documentation

## [◆ ](#a3b5e99bff9dbfa023a4e6a5b4a69abd0)len

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) usbd\_cctx\_vendor\_req::len |
| --- |

Length of the array.

## [◆ ](#a2ddf3ce0c1c0a6d788b7ef30cf8d67ea)reqs

| const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)\* usbd\_cctx\_vendor\_req::reqs |
| --- |

Array of vendor requests supported by the class.

---

The documentation for this struct was generated from the following file:

- zephyr/usb/[usbd.h](usbd_8h_source.md)

- [usbd\_cctx\_vendor\_req](structusbd__cctx__vendor__req.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
