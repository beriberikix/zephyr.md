---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/group__gpio__interface__npm1300.html
original_path: doxygen/html/group__gpio__interface__npm1300.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

nPM1300-specific GPIO Flags

[Device Driver APIs](group__io__interfaces.md) » [GPIO Driver APIs](group__gpio__interface.md)

nPM1300-specific GPIO Flags
[More...](#details)

| nPM1300 GPIO drive strength flags | |
| --- | --- |
| nPM1300 GPIO drive strength flags | |
| #define | [NPM1300\_GPIO\_DRIVE\_1MA](#ga722f82469c3c9cd88ab50c6bb75e9645)   (0U << 8U) |
|  | 1mA drive |
| #define | [NPM1300\_GPIO\_DRIVE\_6MA](#ga8b8b6263b00bf56fc9d486f8d542d56d)   (1U << 8U) |
|  | 6mA drive |

| nPM1300 GPIO debounce flags | |
| --- | --- |
| nPM1300 GPIO debounce flags | |
| #define | [NPM1300\_GPIO\_DEBOUNCE\_OFF](#gaacaf730223621e60b83f47680d132b73)   (0U << 9U) |
|  | Normal drive. |
| #define | [NPM1300\_GPIO\_DEBOUNCE\_ON](#ga668319bb806733e3ded7026b76e8461d)   (1U << 9U) |
|  | High drive. |

| nPM1300 GPIO watchdog reset flags | |
| --- | --- |
| nPM1300 GPIO watchdog reset flags | |
| #define | [NPM1300\_GPIO\_WDT\_RESET\_OFF](#gad8117ab46f3c11c72f200ef36d99571e)   (0U << 10U) |
|  | Off. |
| #define | [NPM1300\_GPIO\_WDT\_RESET\_ON](#ga34d42db564731b044d43d7732d872510)   (1U << 10U) |
|  | On. |

| nPM1300 GPIO power loss warning flags | |
| --- | --- |
| nPM1300 GPIO power loss warning flags | |
| #define | [NPM1300\_GPIO\_PWRLOSSWARN\_OFF](#ga982a2ede317e91f66d1ba8924d5f0d03)   (0U << 11U) |
|  | Off. |
| #define | [NPM1300\_GPIO\_PWRLOSSWARN\_ON](#ga20d4345e30291bee82b6a63f0a1f8d40)   (1U << 11U) |
|  | On. |

## Detailed Description

nPM1300-specific GPIO Flags

The drive flags are encoded in the 8 upper bits of [gpio\_dt\_flags\_t](group__gpio__interface.md#gad435719dccdc37c05852960a7218fbd2 "gpio_dt_flags_t") as follows:

- Bit 8: Drive strength (0=1mA, 1=6mA)
- Bit 9: Debounce (0=OFF, 1=ON)
- Bit 10: Watchdog reset (0=OFF, 1=ON)
- Bit 11: Power loss warning (0=OFF, 1=ON)

## Macro Definition Documentation

## [◆ ](#gaacaf730223621e60b83f47680d132b73)NPM1300\_GPIO\_DEBOUNCE\_OFF

| #define NPM1300\_GPIO\_DEBOUNCE\_OFF   (0U << 9U) |
| --- |

`#include <[nordic-npm1300-gpio.h](nordic-npm1300-gpio_8h.md)>`

Normal drive.

## [◆ ](#ga668319bb806733e3ded7026b76e8461d)NPM1300\_GPIO\_DEBOUNCE\_ON

| #define NPM1300\_GPIO\_DEBOUNCE\_ON   (1U << 9U) |
| --- |

`#include <[nordic-npm1300-gpio.h](nordic-npm1300-gpio_8h.md)>`

High drive.

## [◆ ](#ga722f82469c3c9cd88ab50c6bb75e9645)NPM1300\_GPIO\_DRIVE\_1MA

| #define NPM1300\_GPIO\_DRIVE\_1MA   (0U << 8U) |
| --- |

`#include <[nordic-npm1300-gpio.h](nordic-npm1300-gpio_8h.md)>`

1mA drive

## [◆ ](#ga8b8b6263b00bf56fc9d486f8d542d56d)NPM1300\_GPIO\_DRIVE\_6MA

| #define NPM1300\_GPIO\_DRIVE\_6MA   (1U << 8U) |
| --- |

`#include <[nordic-npm1300-gpio.h](nordic-npm1300-gpio_8h.md)>`

6mA drive

## [◆ ](#ga982a2ede317e91f66d1ba8924d5f0d03)NPM1300\_GPIO\_PWRLOSSWARN\_OFF

| #define NPM1300\_GPIO\_PWRLOSSWARN\_OFF   (0U << 11U) |
| --- |

`#include <[nordic-npm1300-gpio.h](nordic-npm1300-gpio_8h.md)>`

Off.

## [◆ ](#ga20d4345e30291bee82b6a63f0a1f8d40)NPM1300\_GPIO\_PWRLOSSWARN\_ON

| #define NPM1300\_GPIO\_PWRLOSSWARN\_ON   (1U << 11U) |
| --- |

`#include <[nordic-npm1300-gpio.h](nordic-npm1300-gpio_8h.md)>`

On.

## [◆ ](#gad8117ab46f3c11c72f200ef36d99571e)NPM1300\_GPIO\_WDT\_RESET\_OFF

| #define NPM1300\_GPIO\_WDT\_RESET\_OFF   (0U << 10U) |
| --- |

`#include <[nordic-npm1300-gpio.h](nordic-npm1300-gpio_8h.md)>`

Off.

## [◆ ](#ga34d42db564731b044d43d7732d872510)NPM1300\_GPIO\_WDT\_RESET\_ON

| #define NPM1300\_GPIO\_WDT\_RESET\_ON   (1U << 10U) |
| --- |

`#include <[nordic-npm1300-gpio.h](nordic-npm1300-gpio_8h.md)>`

On.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
