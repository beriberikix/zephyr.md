---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structusbd__msg.html
original_path: doxygen/html/structusbd__msg.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

usbd\_msg Struct Reference

[Connectivity](group__connectivity.md) » [USB](group__usb.md) » [USB device core API](group__usbd__msg__api.md)

USB device message.
[More...](#details)

`#include <[usbd_msg.h](usbd__msg_8h_source.md)>`

| Data Fields | |
| --- | --- |
| enum [usbd\_msg\_type](group__usbd__msg__api.md#gaa9163408c0006825575a919322f25f56) | [type](#a37b6c815edc24c8aed291fac7c765abe) |
|  | Message type. |
| union { |  |
| int   [status](#ad3cc8990c42917871981f2f810a2d7e7) |  |
| const struct [device](structdevice.md) \*   [dev](#ab75e8dfe889902f536367c0ef15410f8) |  |
| }; |  |
|  | Message status, value or data. |

## Detailed Description

USB device message.

## Field Documentation

## [◆ ](#acd43f383745512c420f108eef37e64bf)[union]

| union { ... } [usbd\_msg](structusbd__msg.md) |
| --- |

Message status, value or data.

## [◆ ](#ab75e8dfe889902f536367c0ef15410f8)dev

| const struct [device](structdevice.md)\* usbd\_msg::dev |
| --- |

## [◆ ](#ad3cc8990c42917871981f2f810a2d7e7)status

| int usbd\_msg::status |
| --- |

## [◆ ](#a37b6c815edc24c8aed291fac7c765abe)type

| enum [usbd\_msg\_type](group__usbd__msg__api.md#gaa9163408c0006825575a919322f25f56) usbd\_msg::type |
| --- |

Message type.

---

The documentation for this struct was generated from the following file:

- zephyr/usb/[usbd\_msg.h](usbd__msg_8h_source.md)

- [usbd\_msg](structusbd__msg.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
