---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structusbh__contex.html
original_path: doxygen/html/structusbh__contex.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
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
| [sys\_dlist\_t](group__doubly-linked-list__apis.md#gaa03f9557215b486fee1039dd4c07e683) | [udevs](#a30e96d30cf7f28d62ef307f06bc2926e) |
|  | USB device list. |
| struct [usb\_device](structusb__device.md) \* | [root](#a4be8845621fb52b2bd2b5e3185e13942) |
|  | USB root device. |
| struct sys\_bitarray \* | [addr\_ba](#af1d14fcef132c7ed9cdbcf7fdc3ae509) |
|  | Allocated device addresses bit array. |

## Detailed Description

USB host support runtime context.

## Field Documentation

## [◆ ](#af1d14fcef132c7ed9cdbcf7fdc3ae509)addr\_ba

| struct sys\_bitarray\* usbh\_contex::addr\_ba |
| --- |

Allocated device addresses bit array.

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

## [◆ ](#a4be8845621fb52b2bd2b5e3185e13942)root

| struct [usb\_device](structusb__device.md)\* usbh\_contex::root |
| --- |

USB root device.

## [◆ ](#a30e96d30cf7f28d62ef307f06bc2926e)udevs

| [sys\_dlist\_t](group__doubly-linked-list__apis.md#gaa03f9557215b486fee1039dd4c07e683) usbh\_contex::udevs |
| --- |

USB device list.

---

The documentation for this struct was generated from the following file:

- zephyr/usb/[usbh.h](usbh_8h_source.md)

- [usbh\_contex](structusbh__contex.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
