---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structusbh__contex.html
original_path: doxygen/html/structusbh__contex.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

usbh\_contex Struct Reference

[Connectivity](group__connectivity.md) » [USB](group__usb.md) » [USB Host Core API](group__usb__host__core__api.md)

USB host support runtime context.
[More...](#details)

`#include <[usbh.h](usbh_8h_source.md)>`

| Data Fields | |
| --- | --- |
| const char \* | [name](#aa2e6c8e95ddf1942fda07ed6bf49b8a9) |
|  | Name of the USB device. |
| struct [k\_mutex](structk__mutex.md) | [mutex](#aa8264dd792ac5c9e99f35c182d80e7f8) |
|  | Access mutex. |
| const struct [device](structdevice.md) \* | [dev](#a08fd4b998cc4db5781caeb62f06a5028) |
|  | Pointer to UHC device struct. |
| [sys\_dlist\_t](group__doubly-linked-list__apis.md#gaa03f9557215b486fee1039dd4c07e683) | [peripherals](#a4cc8b4d571e6c74f65cdf9889e68b0f7) |
|  | peripheral list |

## Detailed Description

USB host support runtime context.

## Field Documentation

## [◆ ](#a08fd4b998cc4db5781caeb62f06a5028)dev

| const struct [device](structdevice.md)\* usbh\_contex::dev |
| --- |

Pointer to UHC device struct.

## [◆ ](#aa8264dd792ac5c9e99f35c182d80e7f8)mutex

| struct [k\_mutex](structk__mutex.md) usbh\_contex::mutex |
| --- |

Access mutex.

## [◆ ](#aa2e6c8e95ddf1942fda07ed6bf49b8a9)name

| const char\* usbh\_contex::name |
| --- |

Name of the USB device.

## [◆ ](#a4cc8b4d571e6c74f65cdf9889e68b0f7)peripherals

| [sys\_dlist\_t](group__doubly-linked-list__apis.md#gaa03f9557215b486fee1039dd4c07e683) usbh\_contex::peripherals |
| --- |

peripheral list

---

The documentation for this struct was generated from the following file:

- zephyr/usb/[usbh.h](usbh_8h_source.md)

- [usbh\_contex](structusbh__contex.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
