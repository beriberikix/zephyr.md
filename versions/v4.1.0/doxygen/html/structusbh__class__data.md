---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structusbh__class__data.html
original_path: doxygen/html/structusbh__class__data.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

usbh\_class\_data Struct Reference

[Connectivity](group__connectivity.md) » [USB](group__usb.md) » [USB Host Core API](group__usb__host__core__api.md)

USB host class data and class instance API.
[More...](#details)

`#include <[usbh.h](usbh_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [usbh\_code\_triple](structusbh__code__triple.md) | [code](#a3db5ee91a0ecb31f12bb46e6f93d1291) |
|  | Class code supported by this instance. |
| int(\* | [request](#a0818ed7ce3c9a1444140158dcd276927) )(struct [usbh\_contex](structusbh__contex.md) \*const uhs\_ctx, struct [uhc\_transfer](structuhc__transfer.md) \*const xfer, int err) |
|  | Initialization of the class implementation. |
| int(\* | [connected](#a6c2fbedf9882e4a7d8e5b65aa3fe1734) )(struct [usbh\_contex](structusbh__contex.md) \*const uhs\_ctx) |
|  | Device connected handler. |
| int(\* | [removed](#ad80163e078fd59b29a45f24a6c7df8e5) )(struct [usbh\_contex](structusbh__contex.md) \*const uhs\_ctx) |
|  | Device removed handler. |
| int(\* | [rwup](#a167b3103b6bc3bb9ab4ffbca0e9ad9d4) )(struct [usbh\_contex](structusbh__contex.md) \*const uhs\_ctx) |
|  | Bus remote wakeup handler. |
| int(\* | [suspended](#abf773a53750a44d418cef64b1e14dabe) )(struct [usbh\_contex](structusbh__contex.md) \*const uhs\_ctx) |
|  | Bus suspended handler. |
| int(\* | [resumed](#aa23cbff522562c4974ade761474c65d7) )(struct [usbh\_contex](structusbh__contex.md) \*const uhs\_ctx) |
|  | Bus resumed handler. |

## Detailed Description

USB host class data and class instance API.

## Field Documentation

## [◆ ](#a3db5ee91a0ecb31f12bb46e6f93d1291)code

| struct [usbh\_code\_triple](structusbh__code__triple.md) usbh\_class\_data::code |
| --- |

Class code supported by this instance.

## [◆ ](#a6c2fbedf9882e4a7d8e5b65aa3fe1734)connected

| int(\* usbh\_class\_data::connected) (struct [usbh\_contex](structusbh__contex.md) \*const uhs\_ctx) |
| --- |

Device connected handler.

## [◆ ](#ad80163e078fd59b29a45f24a6c7df8e5)removed

| int(\* usbh\_class\_data::removed) (struct [usbh\_contex](structusbh__contex.md) \*const uhs\_ctx) |
| --- |

Device removed handler.

## [◆ ](#a0818ed7ce3c9a1444140158dcd276927)request

| int(\* usbh\_class\_data::request) (struct [usbh\_contex](structusbh__contex.md) \*const uhs\_ctx, struct [uhc\_transfer](structuhc__transfer.md) \*const xfer, int err) |
| --- |

Initialization of the class implementation.

Request completion event handler

## [◆ ](#aa23cbff522562c4974ade761474c65d7)resumed

| int(\* usbh\_class\_data::resumed) (struct [usbh\_contex](structusbh__contex.md) \*const uhs\_ctx) |
| --- |

Bus resumed handler.

## [◆ ](#a167b3103b6bc3bb9ab4ffbca0e9ad9d4)rwup

| int(\* usbh\_class\_data::rwup) (struct [usbh\_contex](structusbh__contex.md) \*const uhs\_ctx) |
| --- |

Bus remote wakeup handler.

## [◆ ](#abf773a53750a44d418cef64b1e14dabe)suspended

| int(\* usbh\_class\_data::suspended) (struct [usbh\_contex](structusbh__contex.md) \*const uhs\_ctx) |
| --- |

Bus suspended handler.

---

The documentation for this struct was generated from the following file:

- zephyr/usb/[usbh.h](usbh_8h_source.md)

- [usbh\_class\_data](structusbh__class__data.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
