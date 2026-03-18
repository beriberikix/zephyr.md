---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/group__gpio__interface__nrf.html
original_path: doxygen/html/group__gpio__interface__nrf.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

nRF-specific GPIO Flags

[Device Driver APIs](group__io__interfaces.md) » [GPIO Driver APIs](group__gpio__interface.md)

nRF-specific GPIO Flags
[More...](#details)

| nRF GPIO drive flags | |
| --- | --- |
| nRF GPIO drive flags  Standard (S) or High (H) drive modes can be applied to both pin levels, 0 or   1. High drive mode will increase current capabilities of the pin (refer to each SoC reference manual).   When the pin is configured to operate in open-drain mode (wired-and), the drive mode can only be selected for the 0 level (1 is disconnected). Similarly, when the pin is configured to operate in open-source mode (wired-or), the drive mode can only be set for the 1 level (0 is disconnected).  The drive flags are encoded in the 8 upper bits of [gpio\_dt\_flags\_t](group__gpio__interface.md#gad435719dccdc37c05852960a7218fbd2 "gpio_dt_flags_t") as follows:   - Bit 8: Drive mode for '0' (0=Standard, 1=High) - Bit 9: Drive mode for '1' (0=Standard, 1=High) | |
| #define | [NRF\_GPIO\_DRIVE\_S0](#ga00ce8b0f371e41899b0379adc4647036)   (0U << 8U) |
|  | Standard drive for '0' (default, used with GPIO\_OPEN\_DRAIN). |
| #define | [NRF\_GPIO\_DRIVE\_H0](#gaa21a50e68b9018384dc7b409673cd047)   (1U << 8U) |
|  | High drive for '0' (used with GPIO\_OPEN\_DRAIN). |
| #define | [NRF\_GPIO\_DRIVE\_S1](#ga5909d23af54ccd8bea797e0f74871cb3)   (0U << 9U) |
|  | Standard drive for '1' (default, used with GPIO\_OPEN\_SOURCE). |
| #define | [NRF\_GPIO\_DRIVE\_H1](#ga8adac513c62dfc12b9f4d7272d73a99f)   (1U << 9U) |
|  | High drive for '1' (used with GPIO\_OPEN\_SOURCE). |
| #define | [NRF\_GPIO\_DRIVE\_S0S1](#ga0b03a6717cc2e5d57aba54379188a884)   ([NRF\_GPIO\_DRIVE\_S0](#ga00ce8b0f371e41899b0379adc4647036) | [NRF\_GPIO\_DRIVE\_S1](#ga5909d23af54ccd8bea797e0f74871cb3)) |
|  | Standard drive for '0' and '1' (default). |
| #define | [NRF\_GPIO\_DRIVE\_S0H1](#ga43697400db8d8cba4dd4bbaaae59a551)   ([NRF\_GPIO\_DRIVE\_S0](#ga00ce8b0f371e41899b0379adc4647036) | [NRF\_GPIO\_DRIVE\_H1](#ga8adac513c62dfc12b9f4d7272d73a99f)) |
|  | Standard drive for '0' and high for '1'. |
| #define | [NRF\_GPIO\_DRIVE\_H0S1](#ga4426bd906d7e2965f53e21a246ec0bbc)   ([NRF\_GPIO\_DRIVE\_H0](#gaa21a50e68b9018384dc7b409673cd047) | [NRF\_GPIO\_DRIVE\_S1](#ga5909d23af54ccd8bea797e0f74871cb3)) |
|  | High drive for '0' and standard for '1'. |
| #define | [NRF\_GPIO\_DRIVE\_H0H1](#ga905a8813a86d8cf1087a47eadc089987)   ([NRF\_GPIO\_DRIVE\_H0](#gaa21a50e68b9018384dc7b409673cd047) | [NRF\_GPIO\_DRIVE\_H1](#ga8adac513c62dfc12b9f4d7272d73a99f)) |
|  | High drive for '0' and '1'. |

## Detailed Description

nRF-specific GPIO Flags

## Macro Definition Documentation

## [◆ ](#gaa21a50e68b9018384dc7b409673cd047)NRF\_GPIO\_DRIVE\_H0

| #define NRF\_GPIO\_DRIVE\_H0   (1U << 8U) |
| --- |

`#include <[nordic-nrf-gpio.h](nordic-nrf-gpio_8h.md)>`

High drive for '0' (used with GPIO\_OPEN\_DRAIN).

## [◆ ](#ga905a8813a86d8cf1087a47eadc089987)NRF\_GPIO\_DRIVE\_H0H1

| #define NRF\_GPIO\_DRIVE\_H0H1   ([NRF\_GPIO\_DRIVE\_H0](#gaa21a50e68b9018384dc7b409673cd047) | [NRF\_GPIO\_DRIVE\_H1](#ga8adac513c62dfc12b9f4d7272d73a99f)) |
| --- |

`#include <[nordic-nrf-gpio.h](nordic-nrf-gpio_8h.md)>`

High drive for '0' and '1'.

## [◆ ](#ga4426bd906d7e2965f53e21a246ec0bbc)NRF\_GPIO\_DRIVE\_H0S1

| #define NRF\_GPIO\_DRIVE\_H0S1   ([NRF\_GPIO\_DRIVE\_H0](#gaa21a50e68b9018384dc7b409673cd047) | [NRF\_GPIO\_DRIVE\_S1](#ga5909d23af54ccd8bea797e0f74871cb3)) |
| --- |

`#include <[nordic-nrf-gpio.h](nordic-nrf-gpio_8h.md)>`

High drive for '0' and standard for '1'.

## [◆ ](#ga8adac513c62dfc12b9f4d7272d73a99f)NRF\_GPIO\_DRIVE\_H1

| #define NRF\_GPIO\_DRIVE\_H1   (1U << 9U) |
| --- |

`#include <[nordic-nrf-gpio.h](nordic-nrf-gpio_8h.md)>`

High drive for '1' (used with GPIO\_OPEN\_SOURCE).

## [◆ ](#ga00ce8b0f371e41899b0379adc4647036)NRF\_GPIO\_DRIVE\_S0

| #define NRF\_GPIO\_DRIVE\_S0   (0U << 8U) |
| --- |

`#include <[nordic-nrf-gpio.h](nordic-nrf-gpio_8h.md)>`

Standard drive for '0' (default, used with GPIO\_OPEN\_DRAIN).

## [◆ ](#ga43697400db8d8cba4dd4bbaaae59a551)NRF\_GPIO\_DRIVE\_S0H1

| #define NRF\_GPIO\_DRIVE\_S0H1   ([NRF\_GPIO\_DRIVE\_S0](#ga00ce8b0f371e41899b0379adc4647036) | [NRF\_GPIO\_DRIVE\_H1](#ga8adac513c62dfc12b9f4d7272d73a99f)) |
| --- |

`#include <[nordic-nrf-gpio.h](nordic-nrf-gpio_8h.md)>`

Standard drive for '0' and high for '1'.

## [◆ ](#ga0b03a6717cc2e5d57aba54379188a884)NRF\_GPIO\_DRIVE\_S0S1

| #define NRF\_GPIO\_DRIVE\_S0S1   ([NRF\_GPIO\_DRIVE\_S0](#ga00ce8b0f371e41899b0379adc4647036) | [NRF\_GPIO\_DRIVE\_S1](#ga5909d23af54ccd8bea797e0f74871cb3)) |
| --- |

`#include <[nordic-nrf-gpio.h](nordic-nrf-gpio_8h.md)>`

Standard drive for '0' and '1' (default).

## [◆ ](#ga5909d23af54ccd8bea797e0f74871cb3)NRF\_GPIO\_DRIVE\_S1

| #define NRF\_GPIO\_DRIVE\_S1   (0U << 9U) |
| --- |

`#include <[nordic-nrf-gpio.h](nordic-nrf-gpio_8h.md)>`

Standard drive for '1' (default, used with GPIO\_OPEN\_SOURCE).

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
