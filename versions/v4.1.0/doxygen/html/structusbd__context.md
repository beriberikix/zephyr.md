---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structusbd__context.html
original_path: doxygen/html/structusbd__context.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

usbd\_context Struct Reference

[Connectivity](group__connectivity.md) » [USB](group__usb.md) » [USB device core API](group__usbd__api.md)

USB device support runtime context.
[More...](#details)

`#include <[usbd.h](usbd_8h_source.md)>`

| Data Fields | |
| --- | --- |
| const char \* | [name](#ade73c224b256007bf2d68bd1205ceb6e) |
|  | Name of the USB device. |
| struct [k\_mutex](structk__mutex.md) | [mutex](#a8ff2a4303b73db67eeabdd999736b3a6) |
|  | Access mutex. |
| const struct [device](structdevice.md) \* | [dev](#a52c2cc6118b46fbcbc7a495df61f6b6c) |
|  | Pointer to UDC device. |
| [usbd\_msg\_cb\_t](group__usbd__api.md#ga2cd074cefff922b0816de37935d9646e) | [msg\_cb](#a300ab0384b3d4e7f3d7d188a27a78be3) |
|  | Notification message recipient callback. |
| struct [usbd\_ch9\_data](structusbd__ch9__data.md) | [ch9\_data](#a4fb1545ec02e7d38766cee9940edc1eb) |
|  | Middle layer runtime data. |
| [sys\_dlist\_t](group__doubly-linked-list__apis.md#gaa03f9557215b486fee1039dd4c07e683) | [descriptors](#adf8dd86f2784cc69ce6da314adc00b72) |
|  | slist to manage descriptors like string, BOS |
| [sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8) | [fs\_configs](#a8c7d153a73859dd8ba25265f059f7495) |
|  | slist to manage Full-Speed device configurations |
| [sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8) | [hs\_configs](#a4a6bd413d06328ffa5db089e35157376) |
|  | slist to manage High-Speed device configurations |
| [sys\_dlist\_t](group__doubly-linked-list__apis.md#gaa03f9557215b486fee1039dd4c07e683) | [vreqs](#a6b463c6c01230bc68c50ba5bb5550e99) |
|  | dlist to manage vendor requests with recipient device |
| struct [usbd\_status](structusbd__status.md) | [status](#a3acad44126b6c3d56823ef7408332087) |
|  | Status of the USB device support. |
| void \* | [fs\_desc](#a193420cc196f115cbd6947b10d542ee5) |
|  | Pointer to Full-Speed device descriptor. |
| void \* | [hs\_desc](#a250e2f82c7239ce81b104b6ef3c16857) |
|  | Pointer to High-Speed device descriptor. |

## Detailed Description

USB device support runtime context.

Main structure that organizes all descriptors, configuration, and interfaces. An UDC device must be assigned to this structure.

## Field Documentation

## [◆ ](#a4fb1545ec02e7d38766cee9940edc1eb)ch9\_data

| struct [usbd\_ch9\_data](structusbd__ch9__data.md) usbd\_context::ch9\_data |
| --- |

Middle layer runtime data.

## [◆ ](#adf8dd86f2784cc69ce6da314adc00b72)descriptors

| [sys\_dlist\_t](group__doubly-linked-list__apis.md#gaa03f9557215b486fee1039dd4c07e683) usbd\_context::descriptors |
| --- |

slist to manage descriptors like string, BOS

## [◆ ](#a52c2cc6118b46fbcbc7a495df61f6b6c)dev

| const struct [device](structdevice.md)\* usbd\_context::dev |
| --- |

Pointer to UDC device.

## [◆ ](#a8c7d153a73859dd8ba25265f059f7495)fs\_configs

| [sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8) usbd\_context::fs\_configs |
| --- |

slist to manage Full-Speed device configurations

## [◆ ](#a193420cc196f115cbd6947b10d542ee5)fs\_desc

| void\* usbd\_context::fs\_desc |
| --- |

Pointer to Full-Speed device descriptor.

## [◆ ](#a4a6bd413d06328ffa5db089e35157376)hs\_configs

| [sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8) usbd\_context::hs\_configs |
| --- |

slist to manage High-Speed device configurations

## [◆ ](#a250e2f82c7239ce81b104b6ef3c16857)hs\_desc

| void\* usbd\_context::hs\_desc |
| --- |

Pointer to High-Speed device descriptor.

## [◆ ](#a300ab0384b3d4e7f3d7d188a27a78be3)msg\_cb

| [usbd\_msg\_cb\_t](group__usbd__api.md#ga2cd074cefff922b0816de37935d9646e) usbd\_context::msg\_cb |
| --- |

Notification message recipient callback.

## [◆ ](#a8ff2a4303b73db67eeabdd999736b3a6)mutex

| struct [k\_mutex](structk__mutex.md) usbd\_context::mutex |
| --- |

Access mutex.

## [◆ ](#ade73c224b256007bf2d68bd1205ceb6e)name

| const char\* usbd\_context::name |
| --- |

Name of the USB device.

## [◆ ](#a3acad44126b6c3d56823ef7408332087)status

| struct [usbd\_status](structusbd__status.md) usbd\_context::status |
| --- |

Status of the USB device support.

## [◆ ](#a6b463c6c01230bc68c50ba5bb5550e99)vreqs

| [sys\_dlist\_t](group__doubly-linked-list__apis.md#gaa03f9557215b486fee1039dd4c07e683) usbd\_context::vreqs |
| --- |

dlist to manage vendor requests with recipient device

---

The documentation for this struct was generated from the following file:

- zephyr/usb/[usbd.h](usbd_8h_source.md)

- [usbd\_context](structusbd__context.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
