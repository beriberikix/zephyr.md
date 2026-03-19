---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/snps-designware-gpio_8h.html
original_path: doxygen/html/snps-designware-gpio_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

snps-designware-gpio.h File Reference

[Go to the source code of this file.](snps-designware-gpio_8h_source.md)

| Macros | |
| --- | --- |
| #define | [DW\_GPIO\_DEBOUNCE](#a696fec562551fe17259140fe16cdcc1d)   (1U << 8) |
|  | Enable GPIO pin debounce. |

## Macro Definition Documentation

## [◆ ](#a696fec562551fe17259140fe16cdcc1d)DW\_GPIO\_DEBOUNCE

| #define DW\_GPIO\_DEBOUNCE   (1U << 8) |
| --- |

Enable GPIO pin debounce.

The debounce flag is a Zephyr specific extension of the standard GPIO flags specified by the Linux GPIO binding. Only applicable for SNPS DesignWare GPIO controllers.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [gpio](dir_9486826309e816a7a1c2256ae23b5ea4.md)
- [snps-designware-gpio.h](snps-designware-gpio_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
