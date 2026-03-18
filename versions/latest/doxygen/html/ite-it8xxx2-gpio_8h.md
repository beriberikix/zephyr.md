---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/ite-it8xxx2-gpio_8h.html
original_path: doxygen/html/ite-it8xxx2-gpio_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ite-it8xxx2-gpio.h File Reference

[Go to the source code of this file.](ite-it8xxx2-gpio_8h_source.md)

| Macros | |
| --- | --- |
| GPIO pin voltage flags | |
| The voltage flags are a Zephyr specific extension of the standard GPIO flags specified by the Linux GPIO binding for use with the ITE IT8xxx2 SoCs. | |
| #define | [IT8XXX2\_GPIO\_VOLTAGE\_DEFAULT](#ac65596dfb83850449186a54a915373d8)   (0U << IT8XXX2\_GPIO\_VOLTAGE\_POS) |
|  | Set pin at the default voltage level. |
| #define | [IT8XXX2\_GPIO\_VOLTAGE\_1P8](#ae6592bbcc1426357a96d0308367d74a9)   (1U << IT8XXX2\_GPIO\_VOLTAGE\_POS) |
|  | Set pin voltage level at 1.8 V. |
| #define | [IT8XXX2\_GPIO\_VOLTAGE\_3P3](#a0961ededa9521d8987b57cd8b8401474)   (2U << IT8XXX2\_GPIO\_VOLTAGE\_POS) |
|  | Set pin voltage level at 3.3 V. |
| #define | [IT8XXX2\_GPIO\_VOLTAGE\_5P0](#a058087db025d461980583d2ad38aa0c2)   (3U << IT8XXX2\_GPIO\_VOLTAGE\_POS) |
|  | Set pin voltage level at 5.0 V. |

## Macro Definition Documentation

## [◆ ](#ae6592bbcc1426357a96d0308367d74a9)IT8XXX2\_GPIO\_VOLTAGE\_1P8

| #define IT8XXX2\_GPIO\_VOLTAGE\_1P8   (1U << IT8XXX2\_GPIO\_VOLTAGE\_POS) |
| --- |

Set pin voltage level at 1.8 V.

## [◆ ](#a0961ededa9521d8987b57cd8b8401474)IT8XXX2\_GPIO\_VOLTAGE\_3P3

| #define IT8XXX2\_GPIO\_VOLTAGE\_3P3   (2U << IT8XXX2\_GPIO\_VOLTAGE\_POS) |
| --- |

Set pin voltage level at 3.3 V.

## [◆ ](#a058087db025d461980583d2ad38aa0c2)IT8XXX2\_GPIO\_VOLTAGE\_5P0

| #define IT8XXX2\_GPIO\_VOLTAGE\_5P0   (3U << IT8XXX2\_GPIO\_VOLTAGE\_POS) |
| --- |

Set pin voltage level at 5.0 V.

## [◆ ](#ac65596dfb83850449186a54a915373d8)IT8XXX2\_GPIO\_VOLTAGE\_DEFAULT

| #define IT8XXX2\_GPIO\_VOLTAGE\_DEFAULT   (0U << IT8XXX2\_GPIO\_VOLTAGE\_POS) |
| --- |

Set pin at the default voltage level.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [gpio](dir_9486826309e816a7a1c2256ae23b5ea4.md)
- [ite-it8xxx2-gpio.h](ite-it8xxx2-gpio_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
