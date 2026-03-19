---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structreset__dt__spec.html
original_path: doxygen/html/structreset__dt__spec.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

reset\_dt\_spec Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [Reset Controller Interface](group__reset__controller__interface.md)

Reset controller device configuration.
[More...](#details)

`#include <[reset.h](drivers_2reset_8h_source.md)>`

| Data Fields | |
| --- | --- |
| const struct [device](structdevice.md) \* | [dev](#ab5adeaabc9b0f78f856b1ce3ab8c3889) |
|  | Reset controller device. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [id](#afdafd2a7b827e180dd6021de9c0dba7a) |
|  | Reset line. |

## Detailed Description

Reset controller device configuration.

## Field Documentation

## [◆ ](#ab5adeaabc9b0f78f856b1ce3ab8c3889)dev

| const struct [device](structdevice.md)\* reset\_dt\_spec::dev |
| --- |

Reset controller device.

## [◆ ](#afdafd2a7b827e180dd6021de9c0dba7a)id

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) reset\_dt\_spec::id |
| --- |

Reset line.

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[reset.h](drivers_2reset_8h_source.md)

- [reset\_dt\_spec](structreset__dt__spec.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
