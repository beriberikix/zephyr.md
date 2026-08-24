---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/nxp-imx-igpio_8h.html
original_path: doxygen/html/nxp-imx-igpio_8h.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

nxp-imx-igpio.h File Reference

[Go to the source code of this file.](nxp-imx-igpio_8h_source.md)

| Macros | |
| --- | --- |
| GPIO pull strength flags | |
| The pull strength flags are a Zephyr specific extension of the standard GPIO flags specified by the Linux GPIO binding.  Only applicable for NXP IMX SoCs.  The interface supports two different pull strengths: WEAK - The lowest pull strength supported by the HW STRONG - The highest pull strength supported by the HW | |
| #define | [NXP\_IGPIO\_PULL\_WEAK](#a0cdc8d4cade4e2411fa3686a5375a276)   (0x0U << NXP\_IGPIO\_PULL\_STRENGTH\_POS) |
|  | pull up/down strengths (only applies to CONFIG\_SOC\_SERIES\_IMXRT10XX) |
| #define | [NXP\_IGPIO\_PULL\_STRONG](#a59c07b2a497ed2f8659d456986cc0702)   (0x1U << NXP\_IGPIO\_PULL\_STRENGTH\_POS) |

## Macro Definition Documentation

## [◆ ](#a59c07b2a497ed2f8659d456986cc0702)NXP\_IGPIO\_PULL\_STRONG

| #define NXP\_IGPIO\_PULL\_STRONG   (0x1U << NXP\_IGPIO\_PULL\_STRENGTH\_POS) |
| --- |

## [◆ ](#a0cdc8d4cade4e2411fa3686a5375a276)NXP\_IGPIO\_PULL\_WEAK

| #define NXP\_IGPIO\_PULL\_WEAK   (0x0U << NXP\_IGPIO\_PULL\_STRENGTH\_POS) |
| --- |

pull up/down strengths (only applies to CONFIG\_SOC\_SERIES\_IMXRT10XX)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [gpio](dir_9486826309e816a7a1c2256ae23b5ea4.md)
- [nxp-imx-igpio.h](nxp-imx-igpio_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
