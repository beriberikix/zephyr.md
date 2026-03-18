---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structusbd__contex.html
original_path: doxygen/html/structusbd__contex.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

usbd\_contex Struct Reference

[Connectivity](group__connectivity.md) » [USB](group__usb.md) » [USB device core API](group__usbd__api.md)

USB device support runtime context.
[More...](#details)

`#include <[usbd.h](usbd_8h_source.md)>`

| Data Fields | |
| --- | --- |
| const char \* | [name](#abba6950f90e08a227c5a124ba1cac794) |
|  | Name of the USB device. |
| struct [k\_mutex](structk__mutex.md) | [mutex](#ac833ce3afb9a9d86c90f35bc33ef617f) |
|  | Access mutex. |
| const struct [device](structdevice.md) \* | [dev](#abe1919c4098622f9a87f4b2d4caf1c3b) |
|  | Pointer to UDC device. |
| struct [usbd\_ch9\_data](structusbd__ch9__data.md) | [ch9\_data](#a7f0d2d526faa553e3f520a58639d271a) |
|  | Middle layer runtime data. |
| [sys\_dlist\_t](group__doubly-linked-list__apis.md#gaa03f9557215b486fee1039dd4c07e683) | [descriptors](#a4634c51ab958993e0d2c2cbb192cc105) |
|  | slist to manage descriptors like string, bos |
| [sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8) | [configs](#abc0473af6584cd4d4040af7d5f1b522b) |
|  | slist to manage device configurations |
| struct [usbd\_status](structusbd__status.md) | [status](#ae190c2f4e20e91e9ad75ff81012b47c2) |
|  | Status of the USB device support. |
| void \* | [desc](#ad2984b7bd687e2c753c1c7497044e9d0) |
|  | Pointer to device descriptor. |

## Detailed Description

USB device support runtime context.

Main structure that organizes all descriptors, configuration, and interfaces. An UDC device must be assigned to this structure.

## Field Documentation

## [◆ ](#a7f0d2d526faa553e3f520a58639d271a)ch9\_data

| struct [usbd\_ch9\_data](structusbd__ch9__data.md) usbd\_contex::ch9\_data |
| --- |

Middle layer runtime data.

## [◆ ](#abc0473af6584cd4d4040af7d5f1b522b)configs

| [sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8) usbd\_contex::configs |
| --- |

slist to manage device configurations

## [◆ ](#ad2984b7bd687e2c753c1c7497044e9d0)desc

| void\* usbd\_contex::desc |
| --- |

Pointer to device descriptor.

## [◆ ](#a4634c51ab958993e0d2c2cbb192cc105)descriptors

| [sys\_dlist\_t](group__doubly-linked-list__apis.md#gaa03f9557215b486fee1039dd4c07e683) usbd\_contex::descriptors |
| --- |

slist to manage descriptors like string, bos

## [◆ ](#abe1919c4098622f9a87f4b2d4caf1c3b)dev

| const struct [device](structdevice.md)\* usbd\_contex::dev |
| --- |

Pointer to UDC device.

## [◆ ](#ac833ce3afb9a9d86c90f35bc33ef617f)mutex

| struct [k\_mutex](structk__mutex.md) usbd\_contex::mutex |
| --- |

Access mutex.

## [◆ ](#abba6950f90e08a227c5a124ba1cac794)name

| const char\* usbd\_contex::name |
| --- |

Name of the USB device.

## [◆ ](#ae190c2f4e20e91e9ad75ff81012b47c2)status

| struct [usbd\_status](structusbd__status.md) usbd\_contex::status |
| --- |

Status of the USB device support.

---

The documentation for this struct was generated from the following file:

- zephyr/usb/[usbd.h](usbd_8h_source.md)

- [usbd\_contex](structusbd__contex.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
