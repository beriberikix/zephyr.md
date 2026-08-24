---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/ene-kb106x-gpio_8h.html
original_path: doxygen/html/ene-kb106x-gpio_8h.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ene-kb106x-gpio.h File Reference

[Go to the source code of this file.](ene-kb106x-gpio_8h_source.md)

| Macros | |
| --- | --- |
| GPIO pin voltage flags | |
| The voltage flags are a Zephyr specific extension of the standard GPIO flags specified by the Linux GPIO binding for use with the ENE KB106x SoCs.  Note: Bits 15 down to 8 are reserved for SoC specific flags. | |
| #define | [ENE\_GPIO\_VOLTAGE\_DEFAULT](#a9f09adacf5a53ad88eb129aace5fc769)   (0U << ENE\_GPIO\_VOLTAGE\_POS) |
|  | Set pin at the default voltage level (3.3V). |
| #define | [ENE\_GPIO\_VOLTAGE\_1P8](#a514da2fb72995d3d891d52d802b0c33b)   (1U << ENE\_GPIO\_VOLTAGE\_POS) |
|  | Set pin voltage level at 1.8 V. |
| #define | [ENE\_GPIO\_DRIVING\_DEFAULT](#a95fcfd50fc67206cea5d561124388e2d)   (0U << ENE\_GPIO\_DRIVING\_POS) |
|  | Set pin at the default driving current (4mA). |
| #define | [ENE\_GPIO\_DRIVING\_16MA](#a1f22235e59a9196da91ff2fa3be4c608)   (1U << ENE\_GPIO\_DRIVING\_POS) |
|  | Set pin driving current at 16mA. |

## Macro Definition Documentation

## [◆ ](#a1f22235e59a9196da91ff2fa3be4c608)ENE\_GPIO\_DRIVING\_16MA

| #define ENE\_GPIO\_DRIVING\_16MA   (1U << ENE\_GPIO\_DRIVING\_POS) |
| --- |

Set pin driving current at 16mA.

## [◆ ](#a95fcfd50fc67206cea5d561124388e2d)ENE\_GPIO\_DRIVING\_DEFAULT

| #define ENE\_GPIO\_DRIVING\_DEFAULT   (0U << ENE\_GPIO\_DRIVING\_POS) |
| --- |

Set pin at the default driving current (4mA).

## [◆ ](#a514da2fb72995d3d891d52d802b0c33b)ENE\_GPIO\_VOLTAGE\_1P8

| #define ENE\_GPIO\_VOLTAGE\_1P8   (1U << ENE\_GPIO\_VOLTAGE\_POS) |
| --- |

Set pin voltage level at 1.8 V.

## [◆ ](#a9f09adacf5a53ad88eb129aace5fc769)ENE\_GPIO\_VOLTAGE\_DEFAULT

| #define ENE\_GPIO\_VOLTAGE\_DEFAULT   (0U << ENE\_GPIO\_VOLTAGE\_POS) |
| --- |

Set pin at the default voltage level (3.3V).

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [gpio](dir_9486826309e816a7a1c2256ae23b5ea4.md)
- [ene-kb106x-gpio.h](ene-kb106x-gpio_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
