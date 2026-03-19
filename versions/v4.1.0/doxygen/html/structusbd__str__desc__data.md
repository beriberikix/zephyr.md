---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structusbd__str__desc__data.html
original_path: doxygen/html/structusbd__str__desc__data.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

usbd\_str\_desc\_data Struct Reference

[Connectivity](group__connectivity.md) » [USB](group__usb.md) » [USB device core API](group__usbd__api.md)

Used internally to keep descriptors in order.
[More...](#details)

`#include <[usbd.h](usbd_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [idx](#a0654953d15160cc19cad86a407f655cb) |
|  | Descriptor index, required for string descriptors. |
| enum usbd\_str\_desc\_utype | [utype](#a2e6dfc9cbbd44457113899db988a84ca): 8 |
|  | Descriptor usage type (not bDescriptorType). |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [ascii7](#ad4d7c291f95973d20ff522b8a5ef65a0): 1 |
|  | The string descriptor is in ASCII7 format. |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [use\_hwinfo](#a40459d114a339841e1f9c14b0d036fe8): 1 |
|  | Device stack obtains SerialNumber using the HWINFO API. |

## Detailed Description

Used internally to keep descriptors in order.

USBD string descriptor data

## Field Documentation

## [◆ ](#ad4d7c291f95973d20ff522b8a5ef65a0)ascii7

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int usbd\_str\_desc\_data::ascii7 |
| --- |

The string descriptor is in ASCII7 format.

## [◆ ](#a0654953d15160cc19cad86a407f655cb)idx

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) usbd\_str\_desc\_data::idx |
| --- |

Descriptor index, required for string descriptors.

## [◆ ](#a40459d114a339841e1f9c14b0d036fe8)use\_hwinfo

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int usbd\_str\_desc\_data::use\_hwinfo |
| --- |

Device stack obtains SerialNumber using the HWINFO API.

## [◆ ](#a2e6dfc9cbbd44457113899db988a84ca)utype

| enum usbd\_str\_desc\_utype usbd\_str\_desc\_data::utype |
| --- |

Descriptor usage type (not bDescriptorType).

---

The documentation for this struct was generated from the following file:

- zephyr/usb/[usbd.h](usbd_8h_source.md)

- [usbd\_str\_desc\_data](structusbd__str__desc__data.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
