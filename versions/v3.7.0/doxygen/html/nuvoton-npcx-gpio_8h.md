---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/nuvoton-npcx-gpio_8h.html
original_path: doxygen/html/nuvoton-npcx-gpio_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

nuvoton-npcx-gpio.h File Reference

[Go to the source code of this file.](nuvoton-npcx-gpio_8h_source.md)

| Macros | |
| --- | --- |
| GPIO pin voltage flags | |
| The voltage flags are a Zephyr specific extension of the standard GPIO flags specified by the Linux GPIO binding for use with the Nuvoton NPCX SoCs. | |
| #define | [NPCX\_GPIO\_VOLTAGE\_DEFAULT](#a92bcad554a75078ab25a13c59075cdff)   (0U << NPCX\_GPIO\_VOLTAGE\_POS) |
|  | Set pin at the default voltage level (3.3V). |
| #define | [NPCX\_GPIO\_VOLTAGE\_1P8](#a21a9db9e72ea60be4a01c65113693fcb)   (1U << NPCX\_GPIO\_VOLTAGE\_POS) |
|  | Set pin voltage level at 1.8 V. |

## Macro Definition Documentation

## [◆ ](#a21a9db9e72ea60be4a01c65113693fcb)NPCX\_GPIO\_VOLTAGE\_1P8

| #define NPCX\_GPIO\_VOLTAGE\_1P8   (1U << NPCX\_GPIO\_VOLTAGE\_POS) |
| --- |

Set pin voltage level at 1.8 V.

## [◆ ](#a92bcad554a75078ab25a13c59075cdff)NPCX\_GPIO\_VOLTAGE\_DEFAULT

| #define NPCX\_GPIO\_VOLTAGE\_DEFAULT   (0U << NPCX\_GPIO\_VOLTAGE\_POS) |
| --- |

Set pin at the default voltage level (3.3V).

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [gpio](dir_9486826309e816a7a1c2256ae23b5ea4.md)
- [nuvoton-npcx-gpio.h](nuvoton-npcx-gpio_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
