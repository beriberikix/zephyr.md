---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structusbd__status.html
original_path: doxygen/html/structusbd__status.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

usbd\_status Struct Reference

[Connectivity](group__connectivity.md) » [USB](group__usb.md) » [USB device core API](group__usbd__api.md)

USB device support status.
[More...](#details)

`#include <[usbd.h](usbd_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [initialized](#a78de12245d08ecc71e09d5519fe0e857): 1 |
|  | USB device support is initialized. |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [enabled](#a2382fcb655fe51e0bcf83f85aa182ba3): 1 |
|  | USB device support is enabled. |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [suspended](#afb67cfda187e40229f842c93aa09f0ba): 1 |
|  | USB device is suspended. |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [rwup](#a113085892967cf7c9cb70131b320d61a): 1 |
|  | USB remote wake-up feature is enabled. |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [self\_powered](#ae4107cb4f379cce8c0472a98483705b8): 1 |
|  | USB device is self-powered. |
| enum [usbd\_speed](group__usbd__api.md#ga2f2da3d634530f08cd59d408c811ad71) | [speed](#a295009d25826732ba9eebd7735d93d23): 2 |
|  | USB device speed. |

## Detailed Description

USB device support status.

## Field Documentation

## [◆ ](#a2382fcb655fe51e0bcf83f85aa182ba3)enabled

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int usbd\_status::enabled |
| --- |

USB device support is enabled.

## [◆ ](#a78de12245d08ecc71e09d5519fe0e857)initialized

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int usbd\_status::initialized |
| --- |

USB device support is initialized.

## [◆ ](#a113085892967cf7c9cb70131b320d61a)rwup

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int usbd\_status::rwup |
| --- |

USB remote wake-up feature is enabled.

## [◆ ](#ae4107cb4f379cce8c0472a98483705b8)self\_powered

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int usbd\_status::self\_powered |
| --- |

USB device is self-powered.

## [◆ ](#a295009d25826732ba9eebd7735d93d23)speed

| enum [usbd\_speed](group__usbd__api.md#ga2f2da3d634530f08cd59d408c811ad71) usbd\_status::speed |
| --- |

USB device speed.

## [◆ ](#afb67cfda187e40229f842c93aa09f0ba)suspended

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int usbd\_status::suspended |
| --- |

USB device is suspended.

---

The documentation for this struct was generated from the following file:

- zephyr/usb/[usbd.h](usbd_8h_source.md)

- [usbd\_status](structusbd__status.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
