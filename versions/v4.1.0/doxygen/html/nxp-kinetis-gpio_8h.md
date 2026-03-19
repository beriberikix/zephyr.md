---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/nxp-kinetis-gpio_8h.html
original_path: doxygen/html/nxp-kinetis-gpio_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

nxp-kinetis-gpio.h File Reference

[Go to the source code of this file.](nxp-kinetis-gpio_8h_source.md)

| Macros | |
| --- | --- |
| GPIO drive strength flags | |
| The drive strength flags are a Zephyr specific extension of the standard GPIO flags specified by the Linux GPIO binding.  Only applicable for NXP Kinetis SoCs.  The interface supports two different drive strengths: DFLT - The lowest drive strength supported by the HW ALT - The highest drive strength supported by the HW | |
| #define | [KINETIS\_GPIO\_DS\_DFLT](#afc2673bf88bc72dda4effbf1d9d0015a)   (0x0U << KINETIS\_GPIO\_DS\_POS) |
|  | Default drive strength. |
| #define | [KINETIS\_GPIO\_DS\_ALT](#a1c4baa298474c0cdc731c4a5cf9f0364)   (0x3U << KINETIS\_GPIO\_DS\_POS) |
|  | Alternative drive strength. |

## Macro Definition Documentation

## [◆ ](#a1c4baa298474c0cdc731c4a5cf9f0364)KINETIS\_GPIO\_DS\_ALT

| #define KINETIS\_GPIO\_DS\_ALT   (0x3U << KINETIS\_GPIO\_DS\_POS) |
| --- |

Alternative drive strength.

## [◆ ](#afc2673bf88bc72dda4effbf1d9d0015a)KINETIS\_GPIO\_DS\_DFLT

| #define KINETIS\_GPIO\_DS\_DFLT   (0x0U << KINETIS\_GPIO\_DS\_POS) |
| --- |

Default drive strength.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [gpio](dir_9486826309e816a7a1c2256ae23b5ea4.md)
- [nxp-kinetis-gpio.h](nxp-kinetis-gpio_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
