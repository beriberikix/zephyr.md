---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/atmel-sam-gpio_8h.html
original_path: doxygen/html/atmel-sam-gpio_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

atmel-sam-gpio.h File Reference

[Go to the source code of this file.](atmel-sam-gpio_8h_source.md)

| Macros | |
| --- | --- |
| #define | [SAM\_GPIO\_DEBOUNCE](#a0747d762ffd1e5e91ac15baacb7680d7)   (1U << 8) |
|  | Enable GPIO pin debounce. |

## Macro Definition Documentation

## [◆ ](#a0747d762ffd1e5e91ac15baacb7680d7)SAM\_GPIO\_DEBOUNCE

| #define SAM\_GPIO\_DEBOUNCE   (1U << 8) |
| --- |

Enable GPIO pin debounce.

The debounce flag is a Zephyr specific extension of the standard GPIO flags specified by the Linux GPIO binding. Only applicable for Atmel SAM SoCs.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [gpio](dir_9486826309e816a7a1c2256ae23b5ea4.md)
- [atmel-sam-gpio.h](atmel-sam-gpio_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
