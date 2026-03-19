---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structusbd__class__data.html
original_path: doxygen/html/structusbd__class__data.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
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
| const char \* | [name](#ad251371b0e401fb2bffd6aaa1ff49063) |
|  | Name of the USB device class instance. |
| struct [usbd\_context](structusbd__context.md) \* | [uds\_ctx](#a111a803092fd389a500fb99bfc71b29a) |
|  | Pointer to USB device stack context structure. |
| const struct [usbd\_class\_api](structusbd__class__api.md) \* | [api](#a9109af3e25c499d4ef1f0746bf6a20cc) |
|  | Pointer to device support class API. |
| const struct [usbd\_cctx\_vendor\_req](structusbd__cctx__vendor__req.md) \* | [v\_reqs](#a32db83ecf80e1ac9e4d5deda54581deb) |
|  | Supported vendor request table, can be NULL. |
| void \* | [priv](#a10bb5b9af6098fbbc86fd00ef54e84e1) |
|  | Pointer to private data. |

## Detailed Description

USB device support class data.

## Field Documentation

## [◆ ](#a9109af3e25c499d4ef1f0746bf6a20cc)api

| const struct [usbd\_class\_api](structusbd__class__api.md)\* usbd\_class\_data::api |
| --- |

Pointer to device support class API.

## [◆ ](#ad251371b0e401fb2bffd6aaa1ff49063)name

| const char\* usbd\_class\_data::name |
| --- |

Name of the USB device class instance.

## [◆ ](#a10bb5b9af6098fbbc86fd00ef54e84e1)priv

| void\* usbd\_class\_data::priv |
| --- |

Pointer to private data.

## [◆ ](#a111a803092fd389a500fb99bfc71b29a)uds\_ctx

| struct [usbd\_context](structusbd__context.md)\* usbd\_class\_data::uds\_ctx |
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
