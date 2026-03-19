---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/ene-kb1200-gpio_8h.html
original_path: doxygen/html/ene-kb1200-gpio_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ene-kb1200-gpio.h File Reference

[Go to the source code of this file.](ene-kb1200-gpio_8h_source.md)

| Macros | |
| --- | --- |
| GPIO pin voltage flags | |
| The voltage and driving flags are a Zephyr specific extension of the standard GPIO flags specified by the Linux GPIO binding for use with the ENE KB1200 SoC.  Note: Bits 15 down to 8 are reserved for SoC specific flags. | |
| #define | [KB1200\_GPIO\_VOLTAGE\_DEFAULT](#ac4d6a2febad81ac12ea70df48b66daa8)   (0U << KB1200\_GPIO\_VOLTAGE\_POS) |
|  | Set pin at the default voltage level (3.3V). |
| #define | [KB1200\_GPIO\_VOLTAGE\_1P8](#a97289e46577a8e5a206d91824750c9fc)   (1U << KB1200\_GPIO\_VOLTAGE\_POS) |
|  | Set pin voltage level at 1.8 V. |
| #define | [KB1200\_GPIO\_DRIVING\_DEFAULT](#a19eaa0c7a6564e0de3505846ae536f7d)   (0U << KB1200\_GPIO\_DRIVING\_POS) |
|  | Set pin at the default driving current (4mA). |
| #define | [KB1200\_GPIO\_DRIVING\_16MA](#a55a268c4cc8feed539006571dc7efce3)   (1U << KB1200\_GPIO\_DRIVING\_POS) |
|  | Set pin driving current at 16mA. |

## Macro Definition Documentation

## [◆ ](#a55a268c4cc8feed539006571dc7efce3)KB1200\_GPIO\_DRIVING\_16MA

| #define KB1200\_GPIO\_DRIVING\_16MA   (1U << KB1200\_GPIO\_DRIVING\_POS) |
| --- |

Set pin driving current at 16mA.

## [◆ ](#a19eaa0c7a6564e0de3505846ae536f7d)KB1200\_GPIO\_DRIVING\_DEFAULT

| #define KB1200\_GPIO\_DRIVING\_DEFAULT   (0U << KB1200\_GPIO\_DRIVING\_POS) |
| --- |

Set pin at the default driving current (4mA).

## [◆ ](#a97289e46577a8e5a206d91824750c9fc)KB1200\_GPIO\_VOLTAGE\_1P8

| #define KB1200\_GPIO\_VOLTAGE\_1P8   (1U << KB1200\_GPIO\_VOLTAGE\_POS) |
| --- |

Set pin voltage level at 1.8 V.

## [◆ ](#ac4d6a2febad81ac12ea70df48b66daa8)KB1200\_GPIO\_VOLTAGE\_DEFAULT

| #define KB1200\_GPIO\_VOLTAGE\_DEFAULT   (0U << KB1200\_GPIO\_VOLTAGE\_POS) |
| --- |

Set pin at the default voltage level (3.3V).

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [gpio](dir_9486826309e816a7a1c2256ae23b5ea4.md)
- [ene-kb1200-gpio.h](ene-kb1200-gpio_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
