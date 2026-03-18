---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/reset_2gd32f3x0_8h.html
original_path: doxygen/html/reset_2gd32f3x0_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

gd32f3x0.h File Reference

`#include "[gd32-common.h](gd32-common_8h_source.md)"`

[Go to the source code of this file.](reset_2gd32f3x0_8h_source.md)

| Macros | |
| --- | --- |
| Register offsets | |
| #define | [GD32\_APB2RST\_OFFSET](#ab3c4f1337d87a22178010c65d48d3d30)   0x0CU |
| #define | [GD32\_APB1RST\_OFFSET](#aa81c1cadc283f658cea5c611e75fef5e)   0x10U |
| #define | [GD32\_AHBRST\_OFFSET](#a848c40f9a0d2b60863f461273f0fa37e)   0x28U |
| #define | [GD32\_ADDAPB1RST\_OFFSET](#a9197e68ba74b9955a45ce4e720099e1a)   0xFCU |
| Clock enable/disable definitions for peripherals | |
| #define | [GD32\_RESET\_CFGCMP](#a02f94d0143c5ad76f2532d0b23e931d3)   [GD32\_RESET\_CONFIG](gd32-common_8h.md#a518d3150ddd85f37ae028ee744378594)(APB2RST, 0U) |
| #define | [GD32\_RESET\_ADC](#aec7a7c37bfacf340a8e73b4f63d9bb8f)   [GD32\_RESET\_CONFIG](gd32-common_8h.md#a518d3150ddd85f37ae028ee744378594)(APB2RST, 9U) |
| #define | [GD32\_RESET\_TIMER0](#a2a7fd67d22598a774386a49ded2a9c72)   [GD32\_RESET\_CONFIG](gd32-common_8h.md#a518d3150ddd85f37ae028ee744378594)(APB2RST, 11U) |
| #define | [GD32\_RESET\_SPI0](#a64f740c7f65d696deb5f617654be9c5d)   [GD32\_RESET\_CONFIG](gd32-common_8h.md#a518d3150ddd85f37ae028ee744378594)(APB2RST, 12U) |
| #define | [GD32\_RESET\_USART0](#a6a03a7368d1e153ddf89547962711d35)   [GD32\_RESET\_CONFIG](gd32-common_8h.md#a518d3150ddd85f37ae028ee744378594)(APB2RST, 14U) |
| #define | [GD32\_RESET\_TIMER14](#a2c23b5848b08dd9bb571408391764793)   [GD32\_RESET\_CONFIG](gd32-common_8h.md#a518d3150ddd85f37ae028ee744378594)(APB2RST, 16U) |
| #define | [GD32\_RESET\_TIMER15](#ae1f1c4a1aa517935b9f76bc136a76809)   [GD32\_RESET\_CONFIG](gd32-common_8h.md#a518d3150ddd85f37ae028ee744378594)(APB2RST, 17U) |
| #define | [GD32\_RESET\_TIMER16](#afe50a4990f8267250bd0b454ddfe2b73)   [GD32\_RESET\_CONFIG](gd32-common_8h.md#a518d3150ddd85f37ae028ee744378594)(APB2RST, 18U) |
| #define | [GD32\_RESET\_TIMER1](#a97beb7e8223a64c2fca25679a466f9e0)   [GD32\_RESET\_CONFIG](gd32-common_8h.md#a518d3150ddd85f37ae028ee744378594)(APB1RST, 0U) |
| #define | [GD32\_RESET\_TIMER2](#a113cfc98af5cb46151d0545cf54fe5aa)   [GD32\_RESET\_CONFIG](gd32-common_8h.md#a518d3150ddd85f37ae028ee744378594)(APB1RST, 1U) |
| #define | [GD32\_RESET\_TIMER5](#a532af4dda1790a9b56bb8c023a3d01b7)   [GD32\_RESET\_CONFIG](gd32-common_8h.md#a518d3150ddd85f37ae028ee744378594)(APB1RST, 4U) |
| #define | [GD32\_RESET\_TIMER13](#a012ec5ec4ff3dca4b788f9839be1c2f6)   [GD32\_RESET\_CONFIG](gd32-common_8h.md#a518d3150ddd85f37ae028ee744378594)(APB1RST, 8U) |
| #define | [GD32\_RESET\_WWDGT](#a8aac1c0ab090d8568076f6d8556e5c7a)   [GD32\_RESET\_CONFIG](gd32-common_8h.md#a518d3150ddd85f37ae028ee744378594)(APB1RST, 11U) |
| #define | [GD32\_RESET\_SPI1](#a27ae8979a4889e95867ed833d9843d07)   [GD32\_RESET\_CONFIG](gd32-common_8h.md#a518d3150ddd85f37ae028ee744378594)(APB1RST, 14U) |
| #define | [GD32\_RESET\_USART1](#aeb24e0ab9ae6be1c82593220c9719117)   [GD32\_RESET\_CONFIG](gd32-common_8h.md#a518d3150ddd85f37ae028ee744378594)(APB1RST, 17U) |
| #define | [GD32\_RESET\_PMU](#a02b6250ebdbfa5de5f39f49c6d81f1ef)   [GD32\_RESET\_CONFIG](gd32-common_8h.md#a518d3150ddd85f37ae028ee744378594)(APB1RST, 28U) |
| #define | [GD32\_RESET\_DAC](#a4db6ebe67389f81c9fa20bc7747df578)   [GD32\_RESET\_CONFIG](gd32-common_8h.md#a518d3150ddd85f37ae028ee744378594)(APB1RST, 29U) |
| #define | [GD32\_RESET\_CEC](#a52ce71d770c8c34904d6adafaf360c40)   [GD32\_RESET\_CONFIG](gd32-common_8h.md#a518d3150ddd85f37ae028ee744378594)(APB1RST, 30U) |
| #define | [GD32\_RESET\_USBFS](#afd49566055b04e1ad0c58397379d6fca)   [GD32\_RESET\_CONFIG](gd32-common_8h.md#a518d3150ddd85f37ae028ee744378594)(AHBRST, 12U) |
| #define | [GD32\_RESET\_GPIOA](#a3757cebbf6f3557b95ad38f58eeeec6f)   [GD32\_RESET\_CONFIG](gd32-common_8h.md#a518d3150ddd85f37ae028ee744378594)(AHBRST, 17U) |
| #define | [GD32\_RESET\_GPIOB](#af5961280a760bba841a7d9f2ba1b4e2f)   [GD32\_RESET\_CONFIG](gd32-common_8h.md#a518d3150ddd85f37ae028ee744378594)(AHBRST, 18U) |
| #define | [GD32\_RESET\_GPIOC](#a5a20c0f1febc4709b3038cb0c5ef55bc)   [GD32\_RESET\_CONFIG](gd32-common_8h.md#a518d3150ddd85f37ae028ee744378594)(AHBRST, 19U) |
| #define | [GD32\_RESET\_GPIOD](#ab9da13b274d377bdce3b3cce159c0cd4)   [GD32\_RESET\_CONFIG](gd32-common_8h.md#a518d3150ddd85f37ae028ee744378594)(AHBRST, 20U) |
| #define | [GD32\_RESET\_GPIOF](#a8cac628be929c7303ca2017b0e2a2798)   [GD32\_RESET\_CONFIG](gd32-common_8h.md#a518d3150ddd85f37ae028ee744378594)(AHBRST, 22U) |
| #define | [GD32\_RESET\_TSI](#ae81c4750d95cee3a16e9e7b08404b2ae)   [GD32\_RESET\_CONFIG](gd32-common_8h.md#a518d3150ddd85f37ae028ee744378594)(AHBRST, 24U) |
| #define | [GD32\_RESET\_CTC](#a595597cd5801d9255a07b0d3b87fb649)   [GD32\_RESET\_CONFIG](gd32-common_8h.md#a518d3150ddd85f37ae028ee744378594)(ADDAPB1RST, 27U) |

## Macro Definition Documentation

## [◆ ](#a9197e68ba74b9955a45ce4e720099e1a)GD32\_ADDAPB1RST\_OFFSET

| #define GD32\_ADDAPB1RST\_OFFSET   0xFCU |
| --- |

## [◆ ](#a848c40f9a0d2b60863f461273f0fa37e)GD32\_AHBRST\_OFFSET

| #define GD32\_AHBRST\_OFFSET   0x28U |
| --- |

## [◆ ](#aa81c1cadc283f658cea5c611e75fef5e)GD32\_APB1RST\_OFFSET

| #define GD32\_APB1RST\_OFFSET   0x10U |
| --- |

## [◆ ](#ab3c4f1337d87a22178010c65d48d3d30)GD32\_APB2RST\_OFFSET

| #define GD32\_APB2RST\_OFFSET   0x0CU |
| --- |

## [◆ ](#aec7a7c37bfacf340a8e73b4f63d9bb8f)GD32\_RESET\_ADC

| #define GD32\_RESET\_ADC   [GD32\_RESET\_CONFIG](gd32-common_8h.md#a518d3150ddd85f37ae028ee744378594)(APB2RST, 9U) |
| --- |

## [◆ ](#a52ce71d770c8c34904d6adafaf360c40)GD32\_RESET\_CEC

| #define GD32\_RESET\_CEC   [GD32\_RESET\_CONFIG](gd32-common_8h.md#a518d3150ddd85f37ae028ee744378594)(APB1RST, 30U) |
| --- |

## [◆ ](#a02f94d0143c5ad76f2532d0b23e931d3)GD32\_RESET\_CFGCMP

| #define GD32\_RESET\_CFGCMP   [GD32\_RESET\_CONFIG](gd32-common_8h.md#a518d3150ddd85f37ae028ee744378594)(APB2RST, 0U) |
| --- |

## [◆ ](#a595597cd5801d9255a07b0d3b87fb649)GD32\_RESET\_CTC

| #define GD32\_RESET\_CTC   [GD32\_RESET\_CONFIG](gd32-common_8h.md#a518d3150ddd85f37ae028ee744378594)(ADDAPB1RST, 27U) |
| --- |

## [◆ ](#a4db6ebe67389f81c9fa20bc7747df578)GD32\_RESET\_DAC

| #define GD32\_RESET\_DAC   [GD32\_RESET\_CONFIG](gd32-common_8h.md#a518d3150ddd85f37ae028ee744378594)(APB1RST, 29U) |
| --- |

## [◆ ](#a3757cebbf6f3557b95ad38f58eeeec6f)GD32\_RESET\_GPIOA

| #define GD32\_RESET\_GPIOA   [GD32\_RESET\_CONFIG](gd32-common_8h.md#a518d3150ddd85f37ae028ee744378594)(AHBRST, 17U) |
| --- |

## [◆ ](#af5961280a760bba841a7d9f2ba1b4e2f)GD32\_RESET\_GPIOB

| #define GD32\_RESET\_GPIOB   [GD32\_RESET\_CONFIG](gd32-common_8h.md#a518d3150ddd85f37ae028ee744378594)(AHBRST, 18U) |
| --- |

## [◆ ](#a5a20c0f1febc4709b3038cb0c5ef55bc)GD32\_RESET\_GPIOC

| #define GD32\_RESET\_GPIOC   [GD32\_RESET\_CONFIG](gd32-common_8h.md#a518d3150ddd85f37ae028ee744378594)(AHBRST, 19U) |
| --- |

## [◆ ](#ab9da13b274d377bdce3b3cce159c0cd4)GD32\_RESET\_GPIOD

| #define GD32\_RESET\_GPIOD   [GD32\_RESET\_CONFIG](gd32-common_8h.md#a518d3150ddd85f37ae028ee744378594)(AHBRST, 20U) |
| --- |

## [◆ ](#a8cac628be929c7303ca2017b0e2a2798)GD32\_RESET\_GPIOF

| #define GD32\_RESET\_GPIOF   [GD32\_RESET\_CONFIG](gd32-common_8h.md#a518d3150ddd85f37ae028ee744378594)(AHBRST, 22U) |
| --- |

## [◆ ](#a02b6250ebdbfa5de5f39f49c6d81f1ef)GD32\_RESET\_PMU

| #define GD32\_RESET\_PMU   [GD32\_RESET\_CONFIG](gd32-common_8h.md#a518d3150ddd85f37ae028ee744378594)(APB1RST, 28U) |
| --- |

## [◆ ](#a64f740c7f65d696deb5f617654be9c5d)GD32\_RESET\_SPI0

| #define GD32\_RESET\_SPI0   [GD32\_RESET\_CONFIG](gd32-common_8h.md#a518d3150ddd85f37ae028ee744378594)(APB2RST, 12U) |
| --- |

## [◆ ](#a27ae8979a4889e95867ed833d9843d07)GD32\_RESET\_SPI1

| #define GD32\_RESET\_SPI1   [GD32\_RESET\_CONFIG](gd32-common_8h.md#a518d3150ddd85f37ae028ee744378594)(APB1RST, 14U) |
| --- |

## [◆ ](#a2a7fd67d22598a774386a49ded2a9c72)GD32\_RESET\_TIMER0

| #define GD32\_RESET\_TIMER0   [GD32\_RESET\_CONFIG](gd32-common_8h.md#a518d3150ddd85f37ae028ee744378594)(APB2RST, 11U) |
| --- |

## [◆ ](#a97beb7e8223a64c2fca25679a466f9e0)GD32\_RESET\_TIMER1

| #define GD32\_RESET\_TIMER1   [GD32\_RESET\_CONFIG](gd32-common_8h.md#a518d3150ddd85f37ae028ee744378594)(APB1RST, 0U) |
| --- |

## [◆ ](#a012ec5ec4ff3dca4b788f9839be1c2f6)GD32\_RESET\_TIMER13

| #define GD32\_RESET\_TIMER13   [GD32\_RESET\_CONFIG](gd32-common_8h.md#a518d3150ddd85f37ae028ee744378594)(APB1RST, 8U) |
| --- |

## [◆ ](#a2c23b5848b08dd9bb571408391764793)GD32\_RESET\_TIMER14

| #define GD32\_RESET\_TIMER14   [GD32\_RESET\_CONFIG](gd32-common_8h.md#a518d3150ddd85f37ae028ee744378594)(APB2RST, 16U) |
| --- |

## [◆ ](#ae1f1c4a1aa517935b9f76bc136a76809)GD32\_RESET\_TIMER15

| #define GD32\_RESET\_TIMER15   [GD32\_RESET\_CONFIG](gd32-common_8h.md#a518d3150ddd85f37ae028ee744378594)(APB2RST, 17U) |
| --- |

## [◆ ](#afe50a4990f8267250bd0b454ddfe2b73)GD32\_RESET\_TIMER16

| #define GD32\_RESET\_TIMER16   [GD32\_RESET\_CONFIG](gd32-common_8h.md#a518d3150ddd85f37ae028ee744378594)(APB2RST, 18U) |
| --- |

## [◆ ](#a113cfc98af5cb46151d0545cf54fe5aa)GD32\_RESET\_TIMER2

| #define GD32\_RESET\_TIMER2   [GD32\_RESET\_CONFIG](gd32-common_8h.md#a518d3150ddd85f37ae028ee744378594)(APB1RST, 1U) |
| --- |

## [◆ ](#a532af4dda1790a9b56bb8c023a3d01b7)GD32\_RESET\_TIMER5

| #define GD32\_RESET\_TIMER5   [GD32\_RESET\_CONFIG](gd32-common_8h.md#a518d3150ddd85f37ae028ee744378594)(APB1RST, 4U) |
| --- |

## [◆ ](#ae81c4750d95cee3a16e9e7b08404b2ae)GD32\_RESET\_TSI

| #define GD32\_RESET\_TSI   [GD32\_RESET\_CONFIG](gd32-common_8h.md#a518d3150ddd85f37ae028ee744378594)(AHBRST, 24U) |
| --- |

## [◆ ](#a6a03a7368d1e153ddf89547962711d35)GD32\_RESET\_USART0

| #define GD32\_RESET\_USART0   [GD32\_RESET\_CONFIG](gd32-common_8h.md#a518d3150ddd85f37ae028ee744378594)(APB2RST, 14U) |
| --- |

## [◆ ](#aeb24e0ab9ae6be1c82593220c9719117)GD32\_RESET\_USART1

| #define GD32\_RESET\_USART1   [GD32\_RESET\_CONFIG](gd32-common_8h.md#a518d3150ddd85f37ae028ee744378594)(APB1RST, 17U) |
| --- |

## [◆ ](#afd49566055b04e1ad0c58397379d6fca)GD32\_RESET\_USBFS

| #define GD32\_RESET\_USBFS   [GD32\_RESET\_CONFIG](gd32-common_8h.md#a518d3150ddd85f37ae028ee744378594)(AHBRST, 12U) |
| --- |

## [◆ ](#a8aac1c0ab090d8568076f6d8556e5c7a)GD32\_RESET\_WWDGT

| #define GD32\_RESET\_WWDGT   [GD32\_RESET\_CONFIG](gd32-common_8h.md#a518d3150ddd85f37ae028ee744378594)(APB1RST, 11U) |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [reset](dir_10e63a26bda611813cb588c12a3608a6.md)
- [gd32f3x0.h](reset_2gd32f3x0_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
