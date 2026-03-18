---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__gpio__interface__npm6001.html
original_path: doxygen/html/group__gpio__interface__npm6001.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

nPM6001-specific GPIO Flags

[Device Driver APIs](group__io__interfaces.md) » [GPIO Driver APIs](group__gpio__interface.md)

nPM6001-specific GPIO Flags
[More...](#details)

| nPM6001 GPIO drive strength flags | |
| --- | --- |
| nPM6001 GPIO drive strength flags | |
| #define | [NPM6001\_GPIO\_DRIVE\_NORMAL](#gaa127d582ea7095b4d7a435ee5ea427c9)   (0U << 8U) |
|  | Normal drive. |
| #define | [NPM6001\_GPIO\_DRIVE\_HIGH](#ga097b6c75d981ad5ecf38a2133d076178)   (1U << 8U) |
|  | High drive. |
| #define | [NPM6001\_GPIO\_SENSE\_SCHMITT](#ga3cde51b59da0f8bf4693ef18b9ee8a30)   (0U << 9U) |
|  | Schmitt trigger input type. |
| #define | [NPM6001\_GPIO\_SENSE\_CMOS](#ga98c66bc1cf5a8c0f83b82c830a817fa2)   (1U << 9U) |
|  | CMOS input type. |

## Detailed Description

nPM6001-specific GPIO Flags

The drive flags are encoded in the 8 upper bits of [gpio\_dt\_flags\_t](group__gpio__interface.md#gad435719dccdc37c05852960a7218fbd2 "gpio_dt_flags_t") as follows:

- Bit 8: Drive strength (0=NORMAL, 1=HIGH)
- Bit 9: Input type (0=SCHMITT, 1=CMOS)

## Macro Definition Documentation

## [◆ ](#ga097b6c75d981ad5ecf38a2133d076178)NPM6001\_GPIO\_DRIVE\_HIGH

| #define NPM6001\_GPIO\_DRIVE\_HIGH   (1U << 8U) |
| --- |

`#include <[nordic-npm6001-gpio.h](nordic-npm6001-gpio_8h.md)>`

High drive.

## [◆ ](#gaa127d582ea7095b4d7a435ee5ea427c9)NPM6001\_GPIO\_DRIVE\_NORMAL

| #define NPM6001\_GPIO\_DRIVE\_NORMAL   (0U << 8U) |
| --- |

`#include <[nordic-npm6001-gpio.h](nordic-npm6001-gpio_8h.md)>`

Normal drive.

## [◆ ](#ga98c66bc1cf5a8c0f83b82c830a817fa2)NPM6001\_GPIO\_SENSE\_CMOS

| #define NPM6001\_GPIO\_SENSE\_CMOS   (1U << 9U) |
| --- |

`#include <[nordic-npm6001-gpio.h](nordic-npm6001-gpio_8h.md)>`

CMOS input type.

## [◆ ](#ga3cde51b59da0f8bf4693ef18b9ee8a30)NPM6001\_GPIO\_SENSE\_SCHMITT

| #define NPM6001\_GPIO\_SENSE\_SCHMITT   (0U << 9U) |
| --- |

`#include <[nordic-npm6001-gpio.h](nordic-npm6001-gpio_8h.md)>`

Schmitt trigger input type.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
