---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structi3c__config__controller.html
original_path: doxygen/html/structi3c__config__controller.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

i3c\_config\_controller Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [I3C Interface](group__i3c__interface.md)

Configuration parameters for I3C hardware to act as controller.
[More...](#details)

`#include <[i3c.h](i3c_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [is\_secondary](#ac0d0190b6a31499097fc34eda3e27a36) |
|  | True if the controller is to be the secondary controller of the bus. |
| struct { |  |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [i3c](#ab1dfb88ea8fab83c4aa3a884fa66084b) |  |
|  | SCL frequency (in Hz) for I3C transfers. [More...](#ab1dfb88ea8fab83c4aa3a884fa66084b) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [i2c](#acd01843427b6cf53c9965885455c1dbd) |  |
|  | SCL frequency (in Hz) for I2C transfers. [More...](#acd01843427b6cf53c9965885455c1dbd) |
| } | [scl](#aebab80b194bf7c35e15edb0466d97e1b) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [supported\_hdr](#abb0eb210bc07911b5648eb490a92c00d) |
|  | Bit mask of supported HDR modes (0 - 7). |

## Detailed Description

Configuration parameters for I3C hardware to act as controller.

## Field Documentation

## [◆ ](#acd01843427b6cf53c9965885455c1dbd)i2c

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) i3c\_config\_controller::i2c |
| --- |

SCL frequency (in Hz) for I2C transfers.

## [◆ ](#ab1dfb88ea8fab83c4aa3a884fa66084b)i3c

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) i3c\_config\_controller::i3c |
| --- |

SCL frequency (in Hz) for I3C transfers.

## [◆ ](#ac0d0190b6a31499097fc34eda3e27a36)is\_secondary

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) i3c\_config\_controller::is\_secondary |
| --- |

True if the controller is to be the secondary controller of the bus.

False to be the primary controller.

## [◆ ](#aebab80b194bf7c35e15edb0466d97e1b)[struct]

| struct { ... } i3c\_config\_controller::scl |
| --- |

## [◆ ](#abb0eb210bc07911b5648eb490a92c00d)supported\_hdr

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) i3c\_config\_controller::supported\_hdr |
| --- |

Bit mask of supported HDR modes (0 - 7).

This can be used to enable or disable HDR mode supported by the hardware at runtime.

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[i3c.h](i3c_8h_source.md)

- [i3c\_config\_controller](structi3c__config__controller.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
