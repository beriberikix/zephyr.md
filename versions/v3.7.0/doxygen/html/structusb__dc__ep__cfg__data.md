---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structusb__dc__ep__cfg__data.html
original_path: doxygen/html/structusb__dc__ep__cfg__data.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

usb\_dc\_ep\_cfg\_data Struct Reference

[USB Device Controller API](group____usb__device__controller__api.md)

USB Endpoint Configuration.
[More...](#details)

`#include <[usb_dc.h](usb__dc_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [ep\_addr](#aba57a59450c93db5935e2ca08c94aa8b) |
|  | The number associated with the EP in the device configuration structure IN EP = 0x80 | <endpoint number> OUT EP = 0x00 | <endpoint number>. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [ep\_mps](#a497bc16439e98415f383a680a0c4d008) |
|  | Endpoint max packet size. |
| enum [usb\_dc\_ep\_transfer\_type](group____usb__device__controller__api.md#gaca68e4a7c3c0a984d1df23794cfa7d87) | [ep\_type](#a689682e1df951fd2fd492dda5e03cf08) |
|  | Endpoint Transfer Type. |

## Detailed Description

USB Endpoint Configuration.

Structure containing the USB endpoint configuration.

## Field Documentation

## [◆ ](#aba57a59450c93db5935e2ca08c94aa8b)ep\_addr

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) usb\_dc\_ep\_cfg\_data::ep\_addr |
| --- |

The number associated with the EP in the device configuration structure IN EP = 0x80 | <endpoint number> OUT EP = 0x00 | <endpoint number>.

## [◆ ](#a497bc16439e98415f383a680a0c4d008)ep\_mps

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) usb\_dc\_ep\_cfg\_data::ep\_mps |
| --- |

Endpoint max packet size.

## [◆ ](#a689682e1df951fd2fd492dda5e03cf08)ep\_type

| enum [usb\_dc\_ep\_transfer\_type](group____usb__device__controller__api.md#gaca68e4a7c3c0a984d1df23794cfa7d87) usb\_dc\_ep\_cfg\_data::ep\_type |
| --- |

Endpoint Transfer Type.

May be Bulk, Interrupt, Control or Isochronous

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/usb/[usb\_dc.h](usb__dc_8h_source.md)

- [usb\_dc\_ep\_cfg\_data](structusb__dc__ep__cfg__data.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
