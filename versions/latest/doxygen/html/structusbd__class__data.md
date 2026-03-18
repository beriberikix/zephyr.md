---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structusbd__class__data.html
original_path: doxygen/html/structusbd__class__data.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

usbd\_class\_data Struct Reference

[Connectivity](group__connectivity.md) » [USB](group__usb.md) » [USB device core API](group__usbd__api.md)

USB device support class data.
[More...](#details)

`#include <[usbd.h](usbd_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [usbd\_contex](structusbd__contex.md) \* | [uds\_ctx](#af2560e7d2e9f4fcc70be0a13883594b1) |
|  | Pointer to USB device stack context structure. |
| void \* | [desc](#a5b63cc431c007291bf96196b0eefd6c2) |
|  | Pointer to a class implementation descriptor that should end with a nil descriptor (bLength = 0 and bDescriptorType = 0). |
| const struct [usbd\_cctx\_vendor\_req](structusbd__cctx__vendor__req.md) \* | [v\_reqs](#a32db83ecf80e1ac9e4d5deda54581deb) |
|  | Supported vendor request table, can be NULL. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [ep\_assigned](#ab60dc9c68368c5c918ea6d23eacfaf60) |
|  | Bitmap of all endpoints assigned to the instance. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [ep\_active](#aad3c8f52393d6135532d25ee8f42950e) |
|  | Bitmap of the enabled endpoints of the instance. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [iface\_bm](#ab41348dd230fa882efb8d39260447cb4) |
|  | Bitmap of the bInterfaceNumbers of the class instance. |
| [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) | [state](#a57718d5c32580352ad7bd49000d01d3b) |
|  | Variable to store the state of the class instance. |
| void \* | [priv](#a10bb5b9af6098fbbc86fd00ef54e84e1) |
|  | Pointer to private data. |

## Detailed Description

USB device support class data.

## Field Documentation

## [◆ ](#a5b63cc431c007291bf96196b0eefd6c2)desc

| void\* usbd\_class\_data::desc |
| --- |

Pointer to a class implementation descriptor that should end with a nil descriptor (bLength = 0 and bDescriptorType = 0).

## [◆ ](#aad3c8f52393d6135532d25ee8f42950e)ep\_active

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) usbd\_class\_data::ep\_active |
| --- |

Bitmap of the enabled endpoints of the instance.

The IN endpoints are mapped in the upper halfword.

## [◆ ](#ab60dc9c68368c5c918ea6d23eacfaf60)ep\_assigned

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) usbd\_class\_data::ep\_assigned |
| --- |

Bitmap of all endpoints assigned to the instance.

The IN endpoints are mapped in the upper halfword.

## [◆ ](#ab41348dd230fa882efb8d39260447cb4)iface\_bm

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) usbd\_class\_data::iface\_bm |
| --- |

Bitmap of the bInterfaceNumbers of the class instance.

## [◆ ](#a10bb5b9af6098fbbc86fd00ef54e84e1)priv

| void\* usbd\_class\_data::priv |
| --- |

Pointer to private data.

## [◆ ](#a57718d5c32580352ad7bd49000d01d3b)state

| [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) usbd\_class\_data::state |
| --- |

Variable to store the state of the class instance.

## [◆ ](#af2560e7d2e9f4fcc70be0a13883594b1)uds\_ctx

| struct [usbd\_contex](structusbd__contex.md)\* usbd\_class\_data::uds\_ctx |
| --- |

Pointer to USB device stack context structure.

## [◆ ](#a32db83ecf80e1ac9e4d5deda54581deb)v\_reqs

| const struct [usbd\_cctx\_vendor\_req](structusbd__cctx__vendor__req.md)\* usbd\_class\_data::v\_reqs |
| --- |

Supported vendor request table, can be NULL.

---

The documentation for this struct was generated from the following file:

- zephyr/usb/[usbd.h](usbd_8h_source.md)

- [usbd\_class\_data](structusbd__class__data.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
