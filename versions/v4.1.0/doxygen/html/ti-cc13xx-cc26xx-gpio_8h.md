---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/ti-cc13xx-cc26xx-gpio_8h.html
original_path: doxygen/html/ti-cc13xx-cc26xx-gpio_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ti-cc13xx-cc26xx-gpio.h File Reference

[Go to the source code of this file.](ti-cc13xx-cc26xx-gpio_8h_source.md)

| Macros | |
| --- | --- |
| #define | [CC13XX\_CC26XX\_GPIO\_DEBOUNCE](#a7fd876bbceee04263d760146333d3b56)   (1U << 8) |
|  | Enable GPIO pin debounce. |
| GPIO drive strength flags | |
| The drive strength flags are a Zephyr specific extension of the standard GPIO flags specified by the Linux GPIO binding.  Only applicable for Texas Instruments CC13xx/CC26xx SoCs.  The interface supports two different drive strengths: DFLT - The lowest drive strength supported by the HW ALT - The highest drive strength supported by the HW | |
| #define | [CC13XX\_CC26XX\_GPIO\_DS\_DFLT](#a038b78d724a2344c100e99ef66fa4613)   (0x0U << CC13XX\_CC26XX\_GPIO\_DS\_POS) |
|  | Default drive strength. |
| #define | [CC13XX\_CC26XX\_GPIO\_DS\_ALT](#a287f8063ecbc0672818d7b813b37e855)   (0x3U << CC13XX\_CC26XX\_GPIO\_DS\_POS) |
|  | Alternative drive strength. |

## Macro Definition Documentation

## [◆ ](#a7fd876bbceee04263d760146333d3b56)CC13XX\_CC26XX\_GPIO\_DEBOUNCE

| #define CC13XX\_CC26XX\_GPIO\_DEBOUNCE   (1U << 8) |
| --- |

Enable GPIO pin debounce.

The debounce flag is a Zephyr specific extension of the standard GPIO flags specified by the Linux GPIO binding. Only applicable for Texas Instruments CC1xx/CC26xx SoCs.

## [◆ ](#a287f8063ecbc0672818d7b813b37e855)CC13XX\_CC26XX\_GPIO\_DS\_ALT

| #define CC13XX\_CC26XX\_GPIO\_DS\_ALT   (0x3U << CC13XX\_CC26XX\_GPIO\_DS\_POS) |
| --- |

Alternative drive strength.

## [◆ ](#a038b78d724a2344c100e99ef66fa4613)CC13XX\_CC26XX\_GPIO\_DS\_DFLT

| #define CC13XX\_CC26XX\_GPIO\_DS\_DFLT   (0x0U << CC13XX\_CC26XX\_GPIO\_DS\_POS) |
| --- |

Default drive strength.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [gpio](dir_9486826309e816a7a1c2256ae23b5ea4.md)
- [ti-cc13xx-cc26xx-gpio.h](ti-cc13xx-cc26xx-gpio_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
