---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structusbd__class__node.html
original_path: doxygen/html/structusbd__class__node.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

usbd\_class\_node Struct Reference

[Connectivity](group__connectivity.md) » [USB](group__usb.md) » [USB device core API](group__usbd__api.md)

`#include <[usbd.h](usbd_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) | [node](#a1bdbe525e21ac5ea6eff30f6159a4406) |
|  | Node information for the slist. |
| const char \* | [name](#a06682f9e64f391985b08c5d884903992) |
|  | Name of the USB device class instance. |
| const struct [usbd\_class\_api](structusbd__class__api.md) \* | [api](#a276df79bf269b19875f1c497a36392fb) |
|  | Pointer to device support class API. |
| struct [usbd\_class\_data](structusbd__class__data.md) \* | [data](#a53916906d5efce1eeb4024a7b3662553) |
|  | Pointer to USB device support class data. |

## Field Documentation

## [◆ ](#a276df79bf269b19875f1c497a36392fb)api

| const struct [usbd\_class\_api](structusbd__class__api.md)\* usbd\_class\_node::api |
| --- |

Pointer to device support class API.

## [◆ ](#a53916906d5efce1eeb4024a7b3662553)data

| struct [usbd\_class\_data](structusbd__class__data.md)\* usbd\_class\_node::data |
| --- |

Pointer to USB device support class data.

## [◆ ](#a06682f9e64f391985b08c5d884903992)name

| const char\* usbd\_class\_node::name |
| --- |

Name of the USB device class instance.

## [◆ ](#a1bdbe525e21ac5ea6eff30f6159a4406)node

| [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) usbd\_class\_node::node |
| --- |

Node information for the slist.

---

The documentation for this struct was generated from the following file:

- zephyr/usb/[usbd.h](usbd_8h_source.md)

- [usbd\_class\_node](structusbd__class__node.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
