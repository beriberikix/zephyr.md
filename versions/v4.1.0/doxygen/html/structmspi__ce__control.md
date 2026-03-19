---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structmspi__ce__control.html
original_path: doxygen/html/structmspi__ce__control.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mspi\_ce\_control Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [MSPI Driver APIs](group__mspi__interface.md) » [MSPI Transfer API](group__mspi__transfer__api.md)

MSPI Chip Select control structure.
[More...](#details)

`#include <[mspi.h](mspi_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [gpio\_dt\_spec](structgpio__dt__spec.md) | [gpio](#a1f1b6f5583abc08c8c7fae95e1a29a7a) |
|  | GPIO devicetree specification of CE GPIO. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [delay](#abc3e35be0b7b3f5c118b0d16033125ba) |
|  | Delay to wait. |

## Detailed Description

MSPI Chip Select control structure.

This can be used to control a CE line via a GPIO line, instead of using the controller inner CE logic.

## Field Documentation

## [◆ ](#abc3e35be0b7b3f5c118b0d16033125ba)delay

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mspi\_ce\_control::delay |
| --- |

Delay to wait.

In microseconds before starting the transmission and before releasing the CE line.

## [◆ ](#a1f1b6f5583abc08c8c7fae95e1a29a7a)gpio

| struct [gpio\_dt\_spec](structgpio__dt__spec.md) mspi\_ce\_control::gpio |
| --- |

GPIO devicetree specification of CE GPIO.

The device pointer can be set to NULL to fully inhibit CE control if necessary. The GPIO flags GPIO\_ACTIVE\_LOW/GPIO\_ACTIVE\_HIGH should be the same as in MSPI configuration.

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[mspi.h](mspi_8h_source.md)

- [mspi\_ce\_control](structmspi__ce__control.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
