---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/numicro-gpio_8h.html
original_path: doxygen/html/numicro-gpio_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

numicro-gpio.h File Reference

[Go to the source code of this file.](numicro-gpio_8h_source.md)

| Macros | |
| --- | --- |
| #define | [NUMICRO\_GPIO\_INPUT\_DEBOUNCE](#a81afdc677d616d7da3340c1b81e51a7c)   (1U << 8) |
|  | Enable GPIO pin debounce. |
| #define | [NUMICRO\_GPIO\_INPUT\_SCHMITT](#a21e7cae6ea58a6ce04487e9083d00556)   (1U << 9) |
|  | Enable Schmitt trigger on input. |

## Macro Definition Documentation

## [◆ ](#a81afdc677d616d7da3340c1b81e51a7c)NUMICRO\_GPIO\_INPUT\_DEBOUNCE

| #define NUMICRO\_GPIO\_INPUT\_DEBOUNCE   (1U << 8) |
| --- |

Enable GPIO pin debounce.

The debounce flag is a Zephyr specific extension of the standard GPIO flags specified by the Linux GPIO binding. Only applicable for Nuvoton NuMicro SoCs.

## [◆ ](#a21e7cae6ea58a6ce04487e9083d00556)NUMICRO\_GPIO\_INPUT\_SCHMITT

| #define NUMICRO\_GPIO\_INPUT\_SCHMITT   (1U << 9) |
| --- |

Enable Schmitt trigger on input.

The Schmitt trigger flag is a Zephyr specific extension of the standard GPIO flags specified by the Linux GPIO binding. Only applicable for Nuvoton NuMicro SoCs.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [gpio](dir_9486826309e816a7a1c2256ae23b5ea4.md)
- [numicro-gpio.h](numicro-gpio_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
