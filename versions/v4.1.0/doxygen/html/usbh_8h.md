---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/usbh_8h.html
original_path: doxygen/html/usbh_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

usbh.h File Reference

New experimental USB device stack APIs and structures.
[More...](#details)

`#include <[stdint.h](stdint_8h_source.md)>`  
`#include <[zephyr/device.h](device_8h_source.md)>`  
`#include <[zephyr/net_buf.h](net__buf_8h_source.md)>`  
`#include <[zephyr/sys/dlist.h](dlist_8h_source.md)>`  
`#include <[zephyr/sys/bitarray.h](bitarray_8h_source.md)>`  
`#include <[zephyr/drivers/usb/uhc.h](uhc_8h_source.md)>`  
`#include <[zephyr/sys/iterable_sections.h](sys_2iterable__sections_8h_source.md)>`

[Go to the source code of this file.](usbh_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [usbh\_contex](structusbh__contex.md) |
|  | USB host support runtime context. [More...](structusbh__contex.md#details) |
| struct | [usbh\_code\_triple](structusbh__code__triple.md) |
|  | USB Class Code triple. [More...](structusbh__code__triple.md#details) |
| struct | [usbh\_class\_data](structusbh__class__data.md) |
|  | USB host class data and class instance API. [More...](structusbh__class__data.md#details) |

| Macros | |
| --- | --- |
| #define | [USBH\_CONTROLLER\_DEFINE](group__usb__host__core__api.md#ga0a8885f9c6e8371ccc02ce191d010010)(device\_name, uhc\_dev) |
| #define | [USBH\_DEFINE\_CLASS](group__usb__host__core__api.md#ga21693790725ac6df7033e2edf67cfa29)(name) |

| Functions | |
| --- | --- |
| int | [usbh\_init](group__usb__host__core__api.md#gaaacb8627f0aae8f8965f923d1d1c786e) (struct [usbh\_contex](structusbh__contex.md) \*uhs\_ctx) |
|  | Initialize the USB host support;. |
| int | [usbh\_enable](group__usb__host__core__api.md#gab77ebba887ffd903de530a587e177a86) (struct [usbh\_contex](structusbh__contex.md) \*uhs\_ctx) |
|  | Enable the USB host support and class instances. |
| int | [usbh\_disable](group__usb__host__core__api.md#ga96ef9b1614874a1ed0e4c9f75bf815ec) (struct [usbh\_contex](structusbh__contex.md) \*uhs\_ctx) |
|  | Disable the USB host support. |
| int | [usbh\_shutdown](group__usb__host__core__api.md#ga4b2581d4e2c5350486ddb8483cd83de9) (struct [usbh\_contex](structusbh__contex.md) \*const uhs\_ctx) |
|  | Shutdown the USB host support. |

## Detailed Description

New experimental USB device stack APIs and structures.

This file contains the USB device stack APIs and structures.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [usb](dir_d8285a9da4e2f530d10dd4c17d446a84.md)
- [usbh.h](usbh_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
