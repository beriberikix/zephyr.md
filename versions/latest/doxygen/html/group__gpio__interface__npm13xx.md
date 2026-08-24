---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/group__gpio__interface__npm13xx.html
original_path: doxygen/html/group__gpio__interface__npm13xx.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

nPM13xx-specific GPIO Flags

[Device Driver APIs](group__io__interfaces.md) » [GPIO Driver APIs](group__gpio__interface.md)

nPM13xx-specific GPIO Flags
[More...](#details)

| nPM13xx GPIO drive strength flags | |
| --- | --- |
| nPM13xx GPIO drive strength flags | |
| #define | [NPM13XX\_GPIO\_DRIVE\_1MA](#ga6a747e318dbdecb394e6c97055cf7d3b)   (0U << 8U) |
|  | 1mA drive |
| #define | [NPM13XX\_GPIO\_DRIVE\_6MA](#ga29c65d6c81acd6c6474a8d5463d30312)   (1U << 8U) |
|  | 6mA drive |

| nPM13xx GPIO debounce flags | |
| --- | --- |
| nPM13xx GPIO debounce flags | |
| #define | [NPM13XX\_GPIO\_DEBOUNCE\_OFF](#ga94b628f01bd35ef5a8c4be5810853d8a)   (0U << 9U) |
|  | Normal drive. |
| #define | [NPM13XX\_GPIO\_DEBOUNCE\_ON](#ga37203fc635db945392c25ba5eddb42ad)   (1U << 9U) |
|  | High drive. |

| nPM13xx GPIO watchdog reset flags | |
| --- | --- |
| nPM13xx GPIO watchdog reset flags | |
| #define | [NPM13XX\_GPIO\_WDT\_RESET\_OFF](#ga7e835aa905fce6b9bd88f6c113ad8fbd)   (0U << 10U) |
|  | Off. |
| #define | [NPM13XX\_GPIO\_WDT\_RESET\_ON](#gac17073bd2d8bda878c0cf7307276efcb)   (1U << 10U) |
|  | On. |

| nPM13xx GPIO power loss warning flags | |
| --- | --- |
| nPM13xx GPIO power loss warning flags | |
| #define | [NPM13XX\_GPIO\_PWRLOSSWARN\_OFF](#ga8aa4cab9a6961ca60a14e1cae448376e)   (0U << 11U) |
|  | Off. |
| #define | [NPM13XX\_GPIO\_PWRLOSSWARN\_ON](#gae774196d9a4258da3d849899de5b744b)   (1U << 11U) |
|  | On. |

## Detailed Description

nPM13xx-specific GPIO Flags

The drive flags are encoded in the 8 upper bits of [gpio\_dt\_flags\_t](group__gpio__interface.md#gad435719dccdc37c05852960a7218fbd2 "gpio_dt_flags_t") as follows:

- Bit 8: Drive strength (0=1mA, 1=6mA)
- Bit 9: Debounce (0=OFF, 1=ON)
- Bit 10: Watchdog reset (0=OFF, 1=ON)
- Bit 11: Power loss warning (0=OFF, 1=ON)

## Macro Definition Documentation

## [◆ ](#ga94b628f01bd35ef5a8c4be5810853d8a)NPM13XX\_GPIO\_DEBOUNCE\_OFF

| #define NPM13XX\_GPIO\_DEBOUNCE\_OFF   (0U << 9U) |
| --- |

`#include <[zephyr/dt-bindings/gpio/nordic-npm13xx-gpio.h](nordic-npm13xx-gpio_8h.md)>`

Normal drive.

## [◆ ](#ga37203fc635db945392c25ba5eddb42ad)NPM13XX\_GPIO\_DEBOUNCE\_ON

| #define NPM13XX\_GPIO\_DEBOUNCE\_ON   (1U << 9U) |
| --- |

`#include <[zephyr/dt-bindings/gpio/nordic-npm13xx-gpio.h](nordic-npm13xx-gpio_8h.md)>`

High drive.

## [◆ ](#ga6a747e318dbdecb394e6c97055cf7d3b)NPM13XX\_GPIO\_DRIVE\_1MA

| #define NPM13XX\_GPIO\_DRIVE\_1MA   (0U << 8U) |
| --- |

`#include <[zephyr/dt-bindings/gpio/nordic-npm13xx-gpio.h](nordic-npm13xx-gpio_8h.md)>`

1mA drive

## [◆ ](#ga29c65d6c81acd6c6474a8d5463d30312)NPM13XX\_GPIO\_DRIVE\_6MA

| #define NPM13XX\_GPIO\_DRIVE\_6MA   (1U << 8U) |
| --- |

`#include <[zephyr/dt-bindings/gpio/nordic-npm13xx-gpio.h](nordic-npm13xx-gpio_8h.md)>`

6mA drive

## [◆ ](#ga8aa4cab9a6961ca60a14e1cae448376e)NPM13XX\_GPIO\_PWRLOSSWARN\_OFF

| #define NPM13XX\_GPIO\_PWRLOSSWARN\_OFF   (0U << 11U) |
| --- |

`#include <[zephyr/dt-bindings/gpio/nordic-npm13xx-gpio.h](nordic-npm13xx-gpio_8h.md)>`

Off.

## [◆ ](#gae774196d9a4258da3d849899de5b744b)NPM13XX\_GPIO\_PWRLOSSWARN\_ON

| #define NPM13XX\_GPIO\_PWRLOSSWARN\_ON   (1U << 11U) |
| --- |

`#include <[zephyr/dt-bindings/gpio/nordic-npm13xx-gpio.h](nordic-npm13xx-gpio_8h.md)>`

On.

## [◆ ](#ga7e835aa905fce6b9bd88f6c113ad8fbd)NPM13XX\_GPIO\_WDT\_RESET\_OFF

| #define NPM13XX\_GPIO\_WDT\_RESET\_OFF   (0U << 10U) |
| --- |

`#include <[zephyr/dt-bindings/gpio/nordic-npm13xx-gpio.h](nordic-npm13xx-gpio_8h.md)>`

Off.

## [◆ ](#gac17073bd2d8bda878c0cf7307276efcb)NPM13XX\_GPIO\_WDT\_RESET\_ON

| #define NPM13XX\_GPIO\_WDT\_RESET\_ON   (1U << 10U) |
| --- |

`#include <[zephyr/dt-bindings/gpio/nordic-npm13xx-gpio.h](nordic-npm13xx-gpio_8h.md)>`

On.

- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
