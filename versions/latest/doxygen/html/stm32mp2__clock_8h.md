---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/stm32mp2__clock_8h.html
original_path: doxygen/html/stm32mp2__clock_8h.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

stm32mp2\_clock.h File Reference

`#include "[stm32_common_clocks.h](stm32__common__clocks_8h_source.md)"`

[Go to the source code of this file.](stm32mp2__clock_8h_source.md)

| Macros | |
| --- | --- |
| #define | [STM32\_CLOCK](#aeeec56ab8e50a43ce21a4dd459ac6c9a)(per, bit) |
|  | Pack RCC clock register offset and bit in two 32-bit values as expected for the Device Tree clocks property on STM32. |
| #define | [STM32\_CLK](#aab77790587d5ff8d674beb25744a88ba)   1U |
| #define | [STM32\_LP\_CLK](#ae40a5105c1bf99aafd76f18d6957bc31)   2U |
| #define | [STM32\_CLOCK\_PERIPH\_GPIOA](#a32bd45297022be14ed15c9772e8109f2)   0x52C |
| #define | [STM32\_CLOCK\_PERIPH\_GPIOB](#a32c6487ed7e24c991684f81f441f8d5d)   0x530 |
| #define | [STM32\_CLOCK\_PERIPH\_GPIOC](#a3f2632c2cbff8cef0f93b8608ea1ae23)   0x534 |
| #define | [STM32\_CLOCK\_PERIPH\_GPIOD](#a046f94e729a2cb3671b6d079f2fb11b7)   0x538 |
| #define | [STM32\_CLOCK\_PERIPH\_GPIOE](#a3ad0bcfa60a4c8871e999969372e4e6f)   0x53C |
| #define | [STM32\_CLOCK\_PERIPH\_GPIOF](#aea08b708537234ca0f93966fcae019d3)   0x540 |
| #define | [STM32\_CLOCK\_PERIPH\_GPIOG](#a2a1ac886c2d4dfa4f85c9d264533131a)   0x544 |
| #define | [STM32\_CLOCK\_PERIPH\_GPIOH](#a52ffbf383d9153016a5535e4f00b0d06)   0x548 |
| #define | [STM32\_CLOCK\_PERIPH\_GPIOI](#a87f8c3eae6c75c1ae6db2039ff453a26)   0x54C |
| #define | [STM32\_CLOCK\_PERIPH\_GPIOJ](#ace35dbc8b0b11f7f455c068d554d583a)   0x550 |
| #define | [STM32\_CLOCK\_PERIPH\_GPIOK](#a2d841fc534ad733d599d4e7ad5982017)   0x554 |
| #define | [STM32\_CLOCK\_PERIPH\_GPIOZ](#ac7426ba0e6460abdeadf3fdc2905186e)   0x558 |
| #define | [STM32\_CLOCK\_PERIPH\_USART1](#a8189f9b07fd040c68981348ebd110bcf)   0x77C |
| #define | [STM32\_CLOCK\_PERIPH\_USART2](#a0cb50b85d43bf4d4d582fe50d2a22330)   0x780 |
| #define | [STM32\_CLOCK\_PERIPH\_USART3](#a4e9105d91ff080466c92b81c613ac9cc)   0x784 |
| #define | [STM32\_CLOCK\_PERIPH\_UART4](#a6a82f04d122f939ca9c8598864a3d23b)   0x788 |
| #define | [STM32\_CLOCK\_PERIPH\_UART5](#a256ed97cebef2d9791352ccab17375ec)   0x78C |
| #define | [STM32\_CLOCK\_PERIPH\_USART6](#af10a9a7ee696c6eae472ba3d10f5ae12)   0x790 |
| #define | [STM32\_CLOCK\_PERIPH\_UART7](#a29ab77f27485310a2de90462f849ee0f)   0x794 |
| #define | [STM32\_CLOCK\_PERIPH\_UART8](#aab6dbf39e99478695f9218c41e24d107)   0x798 |
| #define | [STM32\_CLOCK\_PERIPH\_UART9](#a8b0fd98a958ae01c8f329a68b24025af)   0x79C |
| #define | [STM32\_CLOCK\_PERIPH\_MIN](#a6d218dbd7c0503dbd31a87eb446b8905)   [STM32\_CLOCK\_PERIPH\_GPIOA](#a32bd45297022be14ed15c9772e8109f2) |
| #define | [STM32\_CLOCK\_PERIPH\_MAX](#a57cecbd32ea98f98d52e348c7930dd1f)   [STM32\_CLOCK\_PERIPH\_UART9](#a8b0fd98a958ae01c8f329a68b24025af) |

## Macro Definition Documentation

## [◆ ](#aab77790587d5ff8d674beb25744a88ba)STM32\_CLK

| #define STM32\_CLK   1U |
| --- |

## [◆ ](#aeeec56ab8e50a43ce21a4dd459ac6c9a)STM32\_CLOCK

| #define STM32\_CLOCK | ( |  | *per*, |
| --- | --- | --- | --- |
|  |  |  | *bit* ) |

**Value:**

(STM32\_CLOCK\_PERIPH\_##per) (1 << bit)

Pack RCC clock register offset and bit in two 32-bit values as expected for the Device Tree clocks property on STM32.

Parameters
:   | per | STM32 Peripheral name (expands to STM32\_CLOCK\_PERIPH\_{PER}) |
    | --- | --- |
    | bit | Clock bit |

## [◆ ](#a32bd45297022be14ed15c9772e8109f2)STM32\_CLOCK\_PERIPH\_GPIOA

| #define STM32\_CLOCK\_PERIPH\_GPIOA   0x52C |
| --- |

## [◆ ](#a32c6487ed7e24c991684f81f441f8d5d)STM32\_CLOCK\_PERIPH\_GPIOB

| #define STM32\_CLOCK\_PERIPH\_GPIOB   0x530 |
| --- |

## [◆ ](#a3f2632c2cbff8cef0f93b8608ea1ae23)STM32\_CLOCK\_PERIPH\_GPIOC

| #define STM32\_CLOCK\_PERIPH\_GPIOC   0x534 |
| --- |

## [◆ ](#a046f94e729a2cb3671b6d079f2fb11b7)STM32\_CLOCK\_PERIPH\_GPIOD

| #define STM32\_CLOCK\_PERIPH\_GPIOD   0x538 |
| --- |

## [◆ ](#a3ad0bcfa60a4c8871e999969372e4e6f)STM32\_CLOCK\_PERIPH\_GPIOE

| #define STM32\_CLOCK\_PERIPH\_GPIOE   0x53C |
| --- |

## [◆ ](#aea08b708537234ca0f93966fcae019d3)STM32\_CLOCK\_PERIPH\_GPIOF

| #define STM32\_CLOCK\_PERIPH\_GPIOF   0x540 |
| --- |

## [◆ ](#a2a1ac886c2d4dfa4f85c9d264533131a)STM32\_CLOCK\_PERIPH\_GPIOG

| #define STM32\_CLOCK\_PERIPH\_GPIOG   0x544 |
| --- |

## [◆ ](#a52ffbf383d9153016a5535e4f00b0d06)STM32\_CLOCK\_PERIPH\_GPIOH

| #define STM32\_CLOCK\_PERIPH\_GPIOH   0x548 |
| --- |

## [◆ ](#a87f8c3eae6c75c1ae6db2039ff453a26)STM32\_CLOCK\_PERIPH\_GPIOI

| #define STM32\_CLOCK\_PERIPH\_GPIOI   0x54C |
| --- |

## [◆ ](#ace35dbc8b0b11f7f455c068d554d583a)STM32\_CLOCK\_PERIPH\_GPIOJ

| #define STM32\_CLOCK\_PERIPH\_GPIOJ   0x550 |
| --- |

## [◆ ](#a2d841fc534ad733d599d4e7ad5982017)STM32\_CLOCK\_PERIPH\_GPIOK

| #define STM32\_CLOCK\_PERIPH\_GPIOK   0x554 |
| --- |

## [◆ ](#ac7426ba0e6460abdeadf3fdc2905186e)STM32\_CLOCK\_PERIPH\_GPIOZ

| #define STM32\_CLOCK\_PERIPH\_GPIOZ   0x558 |
| --- |

## [◆ ](#a57cecbd32ea98f98d52e348c7930dd1f)STM32\_CLOCK\_PERIPH\_MAX

| #define STM32\_CLOCK\_PERIPH\_MAX   [STM32\_CLOCK\_PERIPH\_UART9](#a8b0fd98a958ae01c8f329a68b24025af) |
| --- |

## [◆ ](#a6d218dbd7c0503dbd31a87eb446b8905)STM32\_CLOCK\_PERIPH\_MIN

| #define STM32\_CLOCK\_PERIPH\_MIN   [STM32\_CLOCK\_PERIPH\_GPIOA](#a32bd45297022be14ed15c9772e8109f2) |
| --- |

## [◆ ](#a6a82f04d122f939ca9c8598864a3d23b)STM32\_CLOCK\_PERIPH\_UART4

| #define STM32\_CLOCK\_PERIPH\_UART4   0x788 |
| --- |

## [◆ ](#a256ed97cebef2d9791352ccab17375ec)STM32\_CLOCK\_PERIPH\_UART5

| #define STM32\_CLOCK\_PERIPH\_UART5   0x78C |
| --- |

## [◆ ](#a29ab77f27485310a2de90462f849ee0f)STM32\_CLOCK\_PERIPH\_UART7

| #define STM32\_CLOCK\_PERIPH\_UART7   0x794 |
| --- |

## [◆ ](#aab6dbf39e99478695f9218c41e24d107)STM32\_CLOCK\_PERIPH\_UART8

| #define STM32\_CLOCK\_PERIPH\_UART8   0x798 |
| --- |

## [◆ ](#a8b0fd98a958ae01c8f329a68b24025af)STM32\_CLOCK\_PERIPH\_UART9

| #define STM32\_CLOCK\_PERIPH\_UART9   0x79C |
| --- |

## [◆ ](#a8189f9b07fd040c68981348ebd110bcf)STM32\_CLOCK\_PERIPH\_USART1

| #define STM32\_CLOCK\_PERIPH\_USART1   0x77C |
| --- |

## [◆ ](#a0cb50b85d43bf4d4d582fe50d2a22330)STM32\_CLOCK\_PERIPH\_USART2

| #define STM32\_CLOCK\_PERIPH\_USART2   0x780 |
| --- |

## [◆ ](#a4e9105d91ff080466c92b81c613ac9cc)STM32\_CLOCK\_PERIPH\_USART3

| #define STM32\_CLOCK\_PERIPH\_USART3   0x784 |
| --- |

## [◆ ](#af10a9a7ee696c6eae472ba3d10f5ae12)STM32\_CLOCK\_PERIPH\_USART6

| #define STM32\_CLOCK\_PERIPH\_USART6   0x790 |
| --- |

## [◆ ](#ae40a5105c1bf99aafd76f18d6957bc31)STM32\_LP\_CLK

| #define STM32\_LP\_CLK   2U |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [clock](dir_6e9992ac75fd0b7a50e889108957c907.md)
- [stm32mp2\_clock.h](stm32mp2__clock_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
