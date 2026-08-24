---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/ch32v00x-clocks_8h.html
original_path: doxygen/html/ch32v00x-clocks_8h.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ch32v00x-clocks.h File Reference

[Go to the source code of this file.](ch32v00x-clocks_8h_source.md)

| Macros | |
| --- | --- |
| #define | [CH32V00X\_HB\_PCENR\_OFFSET](#ae23b04c6f7dc288edd55ca371b0ac6ac)   0 |
| #define | [CH32V00X\_PB2\_PCENR\_OFFSET](#ac16a6b94e0d36222243acfe99bd576b1)   1 |
| #define | [CH32V00X\_PB1\_PCENR\_OFFSET](#a4de5424f7b84a7be9525d3baaf95b372)   2 |
| #define | [CH32V00X\_CLOCK\_CONFIG](#ab39a50912925831fd0f53da79caa1f3e)(bus, bit) |
| #define | [CH32V00X\_CLOCK\_DMA1](#a673a85e0807d525d0d896968e72476d7)   [CH32V00X\_CLOCK\_CONFIG](#ab39a50912925831fd0f53da79caa1f3e)(HB, 0) |
| #define | [CH32V00X\_CLOCK\_SRAM](#aea9e25b32bec97ba5c4d341a31523586)   [CH32V00X\_CLOCK\_CONFIG](#ab39a50912925831fd0f53da79caa1f3e)(HB, 2) |
| #define | [CH32V00X\_CLOCK\_AFIO](#adba8b05c326b5c50a5f46a4235347cd2)   [CH32V00X\_CLOCK\_CONFIG](#ab39a50912925831fd0f53da79caa1f3e)(PB2, 0) |
| #define | [CH32V00X\_CLOCK\_IOPA](#a6937d869f977cb90e519b2b92f98c120)   [CH32V00X\_CLOCK\_CONFIG](#ab39a50912925831fd0f53da79caa1f3e)(PB2, 2) |
| #define | [CH32V00X\_CLOCK\_IOPB](#a58487531bac2d11010fa719cc9b8bc5b)   [CH32V00X\_CLOCK\_CONFIG](#ab39a50912925831fd0f53da79caa1f3e)(PB2, 3) |
| #define | [CH32V00X\_CLOCK\_IOPC](#af66030ec198edaa564110cc3b0a6b889)   [CH32V00X\_CLOCK\_CONFIG](#ab39a50912925831fd0f53da79caa1f3e)(PB2, 4) |
| #define | [CH32V00X\_CLOCK\_IOPD](#aa2c9b9bc83471c7c0701685025ad45b9)   [CH32V00X\_CLOCK\_CONFIG](#ab39a50912925831fd0f53da79caa1f3e)(PB2, 5) |
| #define | [CH32V00X\_CLOCK\_ADC1](#a4ddfcf15d13a740f3917034aa6aee075)   [CH32V00X\_CLOCK\_CONFIG](#ab39a50912925831fd0f53da79caa1f3e)(PB2, 9) |
| #define | [CH32V00X\_CLOCK\_TIM1](#a35b5af6bc5e72b9360c923916cd2e0f1)   [CH32V00X\_CLOCK\_CONFIG](#ab39a50912925831fd0f53da79caa1f3e)(PB2, 11) |
| #define | [CH32V00X\_CLOCK\_SPI1](#a9ee9b0e633a4a50809c2d2d1d437dd2b)   [CH32V00X\_CLOCK\_CONFIG](#ab39a50912925831fd0f53da79caa1f3e)(PB2, 12) |
| #define | [CH32V00X\_CLOCK\_USART2](#a7d61b5360a6d66ee4ca2210f3e1d32f2)   [CH32V00X\_CLOCK\_CONFIG](#ab39a50912925831fd0f53da79caa1f3e)(PB2, 13) |
| #define | [CH32V00X\_CLOCK\_USART1](#af46cda54f5d666db759746a11909b148)   [CH32V00X\_CLOCK\_CONFIG](#ab39a50912925831fd0f53da79caa1f3e)(PB2, 14) |
| #define | [CH32V00X\_CLOCK\_TIM2](#a22cff65ee5b38ca47089ffa0916c8fda)   [CH32V00X\_CLOCK\_CONFIG](#ab39a50912925831fd0f53da79caa1f3e)(PB1, 0) |
| #define | [CH32V00X\_CLOCK\_TIM3](#a69c30a9fb4e812dff7c5d2b9834a012b)   [CH32V00X\_CLOCK\_CONFIG](#ab39a50912925831fd0f53da79caa1f3e)(PB1, 2) |
| #define | [CH32V00X\_CLOCK\_WWDG](#aa1b25307b070e0131c8d2883cc6daac2)   [CH32V00X\_CLOCK\_CONFIG](#ab39a50912925831fd0f53da79caa1f3e)(PB1, 11) |
| #define | [CH32V00X\_CLOCK\_I2C1](#a44898d60cab2a44b6f11f44dcc910faf)   [CH32V00X\_CLOCK\_CONFIG](#ab39a50912925831fd0f53da79caa1f3e)(PB1, 21) |
| #define | [CH32V00X\_CLOCK\_PWR](#ae70e92186311daf444e9b2a9c4891dcf)   [CH32V00X\_CLOCK\_CONFIG](#ab39a50912925831fd0f53da79caa1f3e)(PB1, 28) |

## Macro Definition Documentation

## [◆ ](#a4ddfcf15d13a740f3917034aa6aee075)CH32V00X\_CLOCK\_ADC1

| #define CH32V00X\_CLOCK\_ADC1   [CH32V00X\_CLOCK\_CONFIG](#ab39a50912925831fd0f53da79caa1f3e)(PB2, 9) |
| --- |

## [◆ ](#adba8b05c326b5c50a5f46a4235347cd2)CH32V00X\_CLOCK\_AFIO

| #define CH32V00X\_CLOCK\_AFIO   [CH32V00X\_CLOCK\_CONFIG](#ab39a50912925831fd0f53da79caa1f3e)(PB2, 0) |
| --- |

## [◆ ](#ab39a50912925831fd0f53da79caa1f3e)CH32V00X\_CLOCK\_CONFIG

| #define CH32V00X\_CLOCK\_CONFIG | ( |  | *bus*, |
| --- | --- | --- | --- |
|  |  |  | *bit* ) |

**Value:**

(((CH32V00X\_##bus##\_PCENR\_OFFSET) << 5) | (bit))

## [◆ ](#a673a85e0807d525d0d896968e72476d7)CH32V00X\_CLOCK\_DMA1

| #define CH32V00X\_CLOCK\_DMA1   [CH32V00X\_CLOCK\_CONFIG](#ab39a50912925831fd0f53da79caa1f3e)(HB, 0) |
| --- |

## [◆ ](#a44898d60cab2a44b6f11f44dcc910faf)CH32V00X\_CLOCK\_I2C1

| #define CH32V00X\_CLOCK\_I2C1   [CH32V00X\_CLOCK\_CONFIG](#ab39a50912925831fd0f53da79caa1f3e)(PB1, 21) |
| --- |

## [◆ ](#a6937d869f977cb90e519b2b92f98c120)CH32V00X\_CLOCK\_IOPA

| #define CH32V00X\_CLOCK\_IOPA   [CH32V00X\_CLOCK\_CONFIG](#ab39a50912925831fd0f53da79caa1f3e)(PB2, 2) |
| --- |

## [◆ ](#a58487531bac2d11010fa719cc9b8bc5b)CH32V00X\_CLOCK\_IOPB

| #define CH32V00X\_CLOCK\_IOPB   [CH32V00X\_CLOCK\_CONFIG](#ab39a50912925831fd0f53da79caa1f3e)(PB2, 3) |
| --- |

## [◆ ](#af66030ec198edaa564110cc3b0a6b889)CH32V00X\_CLOCK\_IOPC

| #define CH32V00X\_CLOCK\_IOPC   [CH32V00X\_CLOCK\_CONFIG](#ab39a50912925831fd0f53da79caa1f3e)(PB2, 4) |
| --- |

## [◆ ](#aa2c9b9bc83471c7c0701685025ad45b9)CH32V00X\_CLOCK\_IOPD

| #define CH32V00X\_CLOCK\_IOPD   [CH32V00X\_CLOCK\_CONFIG](#ab39a50912925831fd0f53da79caa1f3e)(PB2, 5) |
| --- |

## [◆ ](#ae70e92186311daf444e9b2a9c4891dcf)CH32V00X\_CLOCK\_PWR

| #define CH32V00X\_CLOCK\_PWR   [CH32V00X\_CLOCK\_CONFIG](#ab39a50912925831fd0f53da79caa1f3e)(PB1, 28) |
| --- |

## [◆ ](#a9ee9b0e633a4a50809c2d2d1d437dd2b)CH32V00X\_CLOCK\_SPI1

| #define CH32V00X\_CLOCK\_SPI1   [CH32V00X\_CLOCK\_CONFIG](#ab39a50912925831fd0f53da79caa1f3e)(PB2, 12) |
| --- |

## [◆ ](#aea9e25b32bec97ba5c4d341a31523586)CH32V00X\_CLOCK\_SRAM

| #define CH32V00X\_CLOCK\_SRAM   [CH32V00X\_CLOCK\_CONFIG](#ab39a50912925831fd0f53da79caa1f3e)(HB, 2) |
| --- |

## [◆ ](#a35b5af6bc5e72b9360c923916cd2e0f1)CH32V00X\_CLOCK\_TIM1

| #define CH32V00X\_CLOCK\_TIM1   [CH32V00X\_CLOCK\_CONFIG](#ab39a50912925831fd0f53da79caa1f3e)(PB2, 11) |
| --- |

## [◆ ](#a22cff65ee5b38ca47089ffa0916c8fda)CH32V00X\_CLOCK\_TIM2

| #define CH32V00X\_CLOCK\_TIM2   [CH32V00X\_CLOCK\_CONFIG](#ab39a50912925831fd0f53da79caa1f3e)(PB1, 0) |
| --- |

## [◆ ](#a69c30a9fb4e812dff7c5d2b9834a012b)CH32V00X\_CLOCK\_TIM3

| #define CH32V00X\_CLOCK\_TIM3   [CH32V00X\_CLOCK\_CONFIG](#ab39a50912925831fd0f53da79caa1f3e)(PB1, 2) |
| --- |

## [◆ ](#af46cda54f5d666db759746a11909b148)CH32V00X\_CLOCK\_USART1

| #define CH32V00X\_CLOCK\_USART1   [CH32V00X\_CLOCK\_CONFIG](#ab39a50912925831fd0f53da79caa1f3e)(PB2, 14) |
| --- |

## [◆ ](#a7d61b5360a6d66ee4ca2210f3e1d32f2)CH32V00X\_CLOCK\_USART2

| #define CH32V00X\_CLOCK\_USART2   [CH32V00X\_CLOCK\_CONFIG](#ab39a50912925831fd0f53da79caa1f3e)(PB2, 13) |
| --- |

## [◆ ](#aa1b25307b070e0131c8d2883cc6daac2)CH32V00X\_CLOCK\_WWDG

| #define CH32V00X\_CLOCK\_WWDG   [CH32V00X\_CLOCK\_CONFIG](#ab39a50912925831fd0f53da79caa1f3e)(PB1, 11) |
| --- |

## [◆ ](#ae23b04c6f7dc288edd55ca371b0ac6ac)CH32V00X\_HB\_PCENR\_OFFSET

| #define CH32V00X\_HB\_PCENR\_OFFSET   0 |
| --- |

## [◆ ](#a4de5424f7b84a7be9525d3baaf95b372)CH32V00X\_PB1\_PCENR\_OFFSET

| #define CH32V00X\_PB1\_PCENR\_OFFSET   2 |
| --- |

## [◆ ](#ac16a6b94e0d36222243acfe99bd576b1)CH32V00X\_PB2\_PCENR\_OFFSET

| #define CH32V00X\_PB2\_PCENR\_OFFSET   1 |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [clock](dir_6e9992ac75fd0b7a50e889108957c907.md)
- [ch32v00x-clocks.h](ch32v00x-clocks_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
