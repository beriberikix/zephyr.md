---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__gpio__interface__max32.html
original_path: doxygen/html/group__gpio__interface__max32.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

MAX32-specific GPIO Flags

[Device Driver APIs](group__io__interfaces.md) » [GPIO Driver APIs](group__gpio__interface.md)

MAX32-specific GPIO Flags.
[More...](#details)

| MAX32 GPIO drive flags | |
| --- | --- |
| MAX32 GPIO drive flags  The drive flags are encoded in the 8 upper bits of [gpio\_dt\_flags\_t](group__gpio__interface.md#gad435719dccdc37c05852960a7218fbd2 "gpio_dt_flags_t") as follows:   - Bit 8: GPIO Supply Voltage Select Selects the voltage rail used for the pin. 0: VDDIO 1: VDDIOH - Bit 9: GPIO Drive Strength Select, MAX32\_GPIO\_DRV\_STRENGTH\_0 = 1mA MAX32\_GPIO\_DRV\_STRENGTH\_1 = 2mA MAX32\_GPIO\_DRV\_STRENGTH\_2 = 4mA MAX32\_GPIO\_DRV\_STRENGTH\_3 = 8mA - Bit 10: Weak pull up selection, Weak Pullup to VDDIO (1MOhm) 0: Disable 1: Enable - Bit 11: Weak pull down selection, Weak Pulldown to VDDIOH (1MOhm) 0: Disable 1: Enable | |
| #define | [MAX32\_GPIO\_VSEL\_POS](#ga267d4548e80843b5b5678d2050cbef73)   (8U) |
|  | GPIO Voltage Select. |
| #define | [MAX32\_GPIO\_VSEL\_MASK](#ga57b502aa34453a1af1eb5103221c5bde)   (0x01U << [MAX32\_GPIO\_VSEL\_POS](#ga267d4548e80843b5b5678d2050cbef73)) |
| #define | [MAX32\_GPIO\_VSEL\_VDDIO](#ga476d2376c91da2a1cf1bdfd0a7a95198)   (0U << [MAX32\_GPIO\_VSEL\_POS](#ga267d4548e80843b5b5678d2050cbef73)) |
| #define | [MAX32\_GPIO\_VSEL\_VDDIOH](#ga964594ce9114dc57a9e50e416e948147)   (1U << [MAX32\_GPIO\_VSEL\_POS](#ga267d4548e80843b5b5678d2050cbef73)) |
| #define | [MAX32\_GPIO\_DRV\_STRENGTH\_POS](#ga8f42437e9d5cbc3bb2d9d58fee643bc5)   (9U) |
|  | GPIO Drive Strength Select. |
| #define | [MAX32\_GPIO\_DRV\_STRENGTH\_MASK](#gaefce80e7ae44c9f9397e3b4f02a59893)   (0x03U << [MAX32\_GPIO\_DRV\_STRENGTH\_POS](#ga8f42437e9d5cbc3bb2d9d58fee643bc5)) |
| #define | [MAX32\_GPIO\_DRV\_STRENGTH\_0](#gaf783f2b803f4772b5bf4c83f616b8a8a)   (0U << [MAX32\_GPIO\_DRV\_STRENGTH\_POS](#ga8f42437e9d5cbc3bb2d9d58fee643bc5)) |
| #define | [MAX32\_GPIO\_DRV\_STRENGTH\_1](#ga2e0abcd63dbbef23c2368be433c1909d)   (1U << [MAX32\_GPIO\_DRV\_STRENGTH\_POS](#ga8f42437e9d5cbc3bb2d9d58fee643bc5)) |
| #define | [MAX32\_GPIO\_DRV\_STRENGTH\_2](#gae7199008d9e034361d80355651128fdd)   (2U << [MAX32\_GPIO\_DRV\_STRENGTH\_POS](#ga8f42437e9d5cbc3bb2d9d58fee643bc5)) |
| #define | [MAX32\_GPIO\_DRV\_STRENGTH\_3](#gacf1c36bc17e552528ef20d4a8ae67f36)   (3U << [MAX32\_GPIO\_DRV\_STRENGTH\_POS](#ga8f42437e9d5cbc3bb2d9d58fee643bc5)) |
| #define | [MAX32\_GPIO\_WEAK\_PULL\_UP\_POS](#gad20918791adf470f4421a2cbc1c7beaf)   (10U) |
|  | GPIO bias weak pull up selection, to VDDIO (1MOhm). |
| #define | [MAX32\_GPIO\_WEAK\_PULL\_UP](#gac3a2881b03a0e130c0dc174a7aad5b04)   (1U << [MAX32\_GPIO\_WEAK\_PULL\_UP\_POS](#gad20918791adf470f4421a2cbc1c7beaf)) |
| #define | [MAX32\_GPIO\_WEAK\_PULL\_DOWN\_POS](#ga81dd2d4a0dbd87b5346c65e608f5ea45)   (11U) |
|  | GPIO bias weak pull down selection, to VDDIOH (1MOhm). |
| #define | [MAX32\_GPIO\_WEAK\_PULL\_DOWN](#gaa2a5bc76ccfd583c11ee5f18015871be)   (1U << [MAX32\_GPIO\_WEAK\_PULL\_DOWN\_POS](#ga81dd2d4a0dbd87b5346c65e608f5ea45)) |

## Detailed Description

MAX32-specific GPIO Flags.

## Macro Definition Documentation

## [◆ ](#gaf783f2b803f4772b5bf4c83f616b8a8a)MAX32\_GPIO\_DRV\_STRENGTH\_0

| #define MAX32\_GPIO\_DRV\_STRENGTH\_0   (0U << [MAX32\_GPIO\_DRV\_STRENGTH\_POS](#ga8f42437e9d5cbc3bb2d9d58fee643bc5)) |
| --- |

`#include <[adi-max32-gpio.h](adi-max32-gpio_8h.md)>`

## [◆ ](#ga2e0abcd63dbbef23c2368be433c1909d)MAX32\_GPIO\_DRV\_STRENGTH\_1

| #define MAX32\_GPIO\_DRV\_STRENGTH\_1   (1U << [MAX32\_GPIO\_DRV\_STRENGTH\_POS](#ga8f42437e9d5cbc3bb2d9d58fee643bc5)) |
| --- |

`#include <[adi-max32-gpio.h](adi-max32-gpio_8h.md)>`

## [◆ ](#gae7199008d9e034361d80355651128fdd)MAX32\_GPIO\_DRV\_STRENGTH\_2

| #define MAX32\_GPIO\_DRV\_STRENGTH\_2   (2U << [MAX32\_GPIO\_DRV\_STRENGTH\_POS](#ga8f42437e9d5cbc3bb2d9d58fee643bc5)) |
| --- |

`#include <[adi-max32-gpio.h](adi-max32-gpio_8h.md)>`

## [◆ ](#gacf1c36bc17e552528ef20d4a8ae67f36)MAX32\_GPIO\_DRV\_STRENGTH\_3

| #define MAX32\_GPIO\_DRV\_STRENGTH\_3   (3U << [MAX32\_GPIO\_DRV\_STRENGTH\_POS](#ga8f42437e9d5cbc3bb2d9d58fee643bc5)) |
| --- |

`#include <[adi-max32-gpio.h](adi-max32-gpio_8h.md)>`

## [◆ ](#gaefce80e7ae44c9f9397e3b4f02a59893)MAX32\_GPIO\_DRV\_STRENGTH\_MASK

| #define MAX32\_GPIO\_DRV\_STRENGTH\_MASK   (0x03U << [MAX32\_GPIO\_DRV\_STRENGTH\_POS](#ga8f42437e9d5cbc3bb2d9d58fee643bc5)) |
| --- |

`#include <[adi-max32-gpio.h](adi-max32-gpio_8h.md)>`

## [◆ ](#ga8f42437e9d5cbc3bb2d9d58fee643bc5)MAX32\_GPIO\_DRV\_STRENGTH\_POS

| #define MAX32\_GPIO\_DRV\_STRENGTH\_POS   (9U) |
| --- |

`#include <[adi-max32-gpio.h](adi-max32-gpio_8h.md)>`

GPIO Drive Strength Select.

## [◆ ](#ga57b502aa34453a1af1eb5103221c5bde)MAX32\_GPIO\_VSEL\_MASK

| #define MAX32\_GPIO\_VSEL\_MASK   (0x01U << [MAX32\_GPIO\_VSEL\_POS](#ga267d4548e80843b5b5678d2050cbef73)) |
| --- |

`#include <[adi-max32-gpio.h](adi-max32-gpio_8h.md)>`

## [◆ ](#ga267d4548e80843b5b5678d2050cbef73)MAX32\_GPIO\_VSEL\_POS

| #define MAX32\_GPIO\_VSEL\_POS   (8U) |
| --- |

`#include <[adi-max32-gpio.h](adi-max32-gpio_8h.md)>`

GPIO Voltage Select.

## [◆ ](#ga476d2376c91da2a1cf1bdfd0a7a95198)MAX32\_GPIO\_VSEL\_VDDIO

| #define MAX32\_GPIO\_VSEL\_VDDIO   (0U << [MAX32\_GPIO\_VSEL\_POS](#ga267d4548e80843b5b5678d2050cbef73)) |
| --- |

`#include <[adi-max32-gpio.h](adi-max32-gpio_8h.md)>`

## [◆ ](#ga964594ce9114dc57a9e50e416e948147)MAX32\_GPIO\_VSEL\_VDDIOH

| #define MAX32\_GPIO\_VSEL\_VDDIOH   (1U << [MAX32\_GPIO\_VSEL\_POS](#ga267d4548e80843b5b5678d2050cbef73)) |
| --- |

`#include <[adi-max32-gpio.h](adi-max32-gpio_8h.md)>`

## [◆ ](#gaa2a5bc76ccfd583c11ee5f18015871be)MAX32\_GPIO\_WEAK\_PULL\_DOWN

| #define MAX32\_GPIO\_WEAK\_PULL\_DOWN   (1U << [MAX32\_GPIO\_WEAK\_PULL\_DOWN\_POS](#ga81dd2d4a0dbd87b5346c65e608f5ea45)) |
| --- |

`#include <[adi-max32-gpio.h](adi-max32-gpio_8h.md)>`

## [◆ ](#ga81dd2d4a0dbd87b5346c65e608f5ea45)MAX32\_GPIO\_WEAK\_PULL\_DOWN\_POS

| #define MAX32\_GPIO\_WEAK\_PULL\_DOWN\_POS   (11U) |
| --- |

`#include <[adi-max32-gpio.h](adi-max32-gpio_8h.md)>`

GPIO bias weak pull down selection, to VDDIOH (1MOhm).

## [◆ ](#gac3a2881b03a0e130c0dc174a7aad5b04)MAX32\_GPIO\_WEAK\_PULL\_UP

| #define MAX32\_GPIO\_WEAK\_PULL\_UP   (1U << [MAX32\_GPIO\_WEAK\_PULL\_UP\_POS](#gad20918791adf470f4421a2cbc1c7beaf)) |
| --- |

`#include <[adi-max32-gpio.h](adi-max32-gpio_8h.md)>`

## [◆ ](#gad20918791adf470f4421a2cbc1c7beaf)MAX32\_GPIO\_WEAK\_PULL\_UP\_POS

| #define MAX32\_GPIO\_WEAK\_PULL\_UP\_POS   (10U) |
| --- |

`#include <[adi-max32-gpio.h](adi-max32-gpio_8h.md)>`

GPIO bias weak pull up selection, to VDDIO (1MOhm).

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
