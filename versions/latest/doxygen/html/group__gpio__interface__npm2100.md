---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__gpio__interface__npm2100.html
original_path: doxygen/html/group__gpio__interface__npm2100.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

nPM2100-specific GPIO Flags

[Device Driver APIs](group__io__interfaces.md) » [GPIO Driver APIs](group__gpio__interface.md)

nPM2100-specific GPIO Flags
[More...](#details)

| nPM2100 GPIO drive strength flags | |
| --- | --- |
| nPM2100 GPIO drive strength flags | |
| #define | [NPM2100\_GPIO\_DRIVE\_NORMAL](#gaaba391246c0041ce40cf9a9826cc2dbd)   (0U << 8U) |
|  | Normal drive. |
| #define | [NPM2100\_GPIO\_DRIVE\_HIGH](#ga281cd37a16ba12b56850ea98d9b543d5)   (1U << 8U) |
|  | High drive. |

| nPM2100 GPIO debounce flags | |
| --- | --- |
| nPM2100 GPIO debounce flags | |
| #define | [NPM2100\_GPIO\_DEBOUNCE\_OFF](#ga79471e04dd5ed29a8a819403ab6d83d0)   (0U << 9U) |
|  | Normal drive. |
| #define | [NPM2100\_GPIO\_DEBOUNCE\_ON](#ga4b1336ed15dc7ed906d1aa69fddff33d)   (1U << 9U) |
|  | High drive. |

## Detailed Description

nPM2100-specific GPIO Flags

The drive flags are encoded in the 8 upper bits of [gpio\_dt\_flags\_t](group__gpio__interface.md#gad435719dccdc37c05852960a7218fbd2 "gpio_dt_flags_t") as follows:

- Bit 8: Drive strength (0=1mA, 1=6mA)
- Bit 9: Debounce (0=OFF, 1=ON)

## Macro Definition Documentation

## [◆ ](#ga79471e04dd5ed29a8a819403ab6d83d0)NPM2100\_GPIO\_DEBOUNCE\_OFF

| #define NPM2100\_GPIO\_DEBOUNCE\_OFF   (0U << 9U) |
| --- |

`#include <[nordic-npm2100-gpio.h](nordic-npm2100-gpio_8h.md)>`

Normal drive.

## [◆ ](#ga4b1336ed15dc7ed906d1aa69fddff33d)NPM2100\_GPIO\_DEBOUNCE\_ON

| #define NPM2100\_GPIO\_DEBOUNCE\_ON   (1U << 9U) |
| --- |

`#include <[nordic-npm2100-gpio.h](nordic-npm2100-gpio_8h.md)>`

High drive.

## [◆ ](#ga281cd37a16ba12b56850ea98d9b543d5)NPM2100\_GPIO\_DRIVE\_HIGH

| #define NPM2100\_GPIO\_DRIVE\_HIGH   (1U << 8U) |
| --- |

`#include <[nordic-npm2100-gpio.h](nordic-npm2100-gpio_8h.md)>`

High drive.

## [◆ ](#gaaba391246c0041ce40cf9a9826cc2dbd)NPM2100\_GPIO\_DRIVE\_NORMAL

| #define NPM2100\_GPIO\_DRIVE\_NORMAL   (0U << 8U) |
| --- |

`#include <[nordic-npm2100-gpio.h](nordic-npm2100-gpio_8h.md)>`

Normal drive.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
