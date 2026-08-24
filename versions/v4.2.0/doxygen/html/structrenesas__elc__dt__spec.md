---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/structrenesas__elc__dt__spec.html
original_path: doxygen/html/structrenesas__elc__dt__spec.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

renesas\_elc\_dt\_spec Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [Miscellaneous Drivers APIs](group__misc__interfaces.md) » [Renesas ELC driver APIs](group__renesas__elc__interface.md)

Container for Renesas ELC information specified in devicetree.
[More...](#details)

`#include <[zephyr/drivers/misc/interconn/renesas_elc/renesas_elc.h](renesas__elc_8h_source.md)>`

| Data Fields | |
| --- | --- |
| const struct [device](structdevice.md) \* | [dev](#ae759c1c19bd7c69d14165a12331f3df4) |
|  | Renesas ELC device instance. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [peripheral](#a7b20982a91e3bb944c7aaf94b6fd33dd) |
|  | Renesas ELC peripheral ID. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [event](#a9004b468890e2901b4316e9f2fa648ea) |
|  | Renesas ELC event ID. |

## Detailed Description

Container for Renesas ELC information specified in devicetree.

This type contains a pointer to a Renesas ELC device, along with the peripheral ID and event ID used to configure a link between peripherals via the Event Link Controller.

This structure is typically initialized using devicetree macros that parse phandle-array properties referencing ELC instances.

## Field Documentation

## [◆ ](#ae759c1c19bd7c69d14165a12331f3df4)dev

| const struct [device](structdevice.md)\* renesas\_elc\_dt\_spec::dev |
| --- |

Renesas ELC device instance.

## [◆ ](#a9004b468890e2901b4316e9f2fa648ea)event

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) renesas\_elc\_dt\_spec::event |
| --- |

Renesas ELC event ID.

## [◆ ](#a7b20982a91e3bb944c7aaf94b6fd33dd)peripheral

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) renesas\_elc\_dt\_spec::peripheral |
| --- |

Renesas ELC peripheral ID.

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/misc/interconn/renesas\_elc/[renesas\_elc.h](renesas__elc_8h_source.md)

- [renesas\_elc\_dt\_spec](structrenesas__elc__dt__spec.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
