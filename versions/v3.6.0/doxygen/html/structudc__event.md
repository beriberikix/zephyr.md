---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structudc__event.html
original_path: doxygen/html/structudc__event.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

udc\_event Struct Reference

USB device controller event.
[More...](#details)

`#include <[udc.h](udc_8h_source.md)>`

| Data Fields | |
| --- | --- |
| enum [udc\_event\_type](udc_8h.md#a03749f5acb64ff8cfddc3c0b6b81a040) | [type](#a3acfe5d21d16f6edfa24e9964b636434) |
|  | Event type. |
| union { |  |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [value](#ada24e0e920c39bc60a6c7fbbe54277f4) |  |
|  | Event value. [More...](#ada24e0e920c39bc60a6c7fbbe54277f4) |
| int   [status](#a0707d65716a4b1e6dd3132a0bb370770) |  |
|  | Event status value, if any. [More...](#a0707d65716a4b1e6dd3132a0bb370770) |
| struct [net\_buf](structnet__buf.md) \*   [buf](#ac1ff3bc9d629eb9b6c55602e7861e945) |  |
|  | Pointer to request used only for UDC\_EVT\_EP\_REQUEST. [More...](#ac1ff3bc9d629eb9b6c55602e7861e945) |
| }; |  |
| const struct [device](structdevice.md) \* | [dev](#a900404c46850d34cd7121eeedc2fce9d) |
|  | Pointer to device struct. |

## Detailed Description

USB device controller event.

Common structure for all events that originate from the UDC driver and are passed to higher layer using message queue and a callback ([udc\_event\_cb\_t](udc_8h.md#aa3ff247fd5234f65d91f84ebc38e384a "Callback to submit UDC event to higher layer.")) provided by higher layer during controller initialization (udc\_init).

## Field Documentation

## [◆ ](#afbb3dd119205d7f7aa5ef7f473746060)[union]

| union { ... } [udc\_event](structudc__event.md) |
| --- |

## [◆ ](#ac1ff3bc9d629eb9b6c55602e7861e945)buf

| struct [net\_buf](structnet__buf.md)\* udc\_event::buf |
| --- |

Pointer to request used only for UDC\_EVT\_EP\_REQUEST.

## [◆ ](#a900404c46850d34cd7121eeedc2fce9d)dev

| const struct [device](structdevice.md)\* udc\_event::dev |
| --- |

Pointer to device struct.

## [◆ ](#a0707d65716a4b1e6dd3132a0bb370770)status

| int udc\_event::status |
| --- |

Event status value, if any.

## [◆ ](#a3acfe5d21d16f6edfa24e9964b636434)type

| enum [udc\_event\_type](udc_8h.md#a03749f5acb64ff8cfddc3c0b6b81a040) udc\_event::type |
| --- |

Event type.

## [◆ ](#ada24e0e920c39bc60a6c7fbbe54277f4)value

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) udc\_event::value |
| --- |

Event value.

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/usb/[udc.h](udc_8h_source.md)

- [udc\_event](structudc__event.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
