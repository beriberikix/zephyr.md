---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/stm32mp2__reset_8h.html
original_path: doxygen/html/stm32mp2__reset_8h.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

stm32mp2\_reset.h File Reference

[Go to the source code of this file.](stm32mp2__reset_8h_source.md)

| Macros | |
| --- | --- |
| #define | [STM32\_RESET](#a47abaeb040742e28fdb98aac76d5bc38)(per, bit) |
|  | Pack RCC register offset and bit in one 32-bit value. |
| #define | [STM32\_RST](#a1eee43a8d6b28956f35c394a1917b363)   0U |
| #define | [STM32\_RESET\_PERIPH\_USART1](#a43b84745610e5dbdea3cfb253dc07b1c)   0x77C |
| #define | [STM32\_RESET\_PERIPH\_USART2](#a6a85d397faeb4b9dbcba84b82cb46312)   0x780 |
| #define | [STM32\_RESET\_PERIPH\_USART3](#a97840fd9714543ef1702c08f330a8aa8)   0x784 |
| #define | [STM32\_RESET\_PERIPH\_UART4](#a300d2fa9b0d1f3e45fa6602c8961294a)   0x788 |
| #define | [STM32\_RESET\_PERIPH\_UART5](#a027d34aecea80dba893a640ec8fe7c7f)   0x78C |
| #define | [STM32\_RESET\_PERIPH\_USART6](#a8a5634c095db0805d72bab6013df0fdb)   0x790 |
| #define | [STM32\_RESET\_PERIPH\_UART7](#aed8be264b66a3722b3c2145aa000a13f)   0x794 |
| #define | [STM32\_RESET\_PERIPH\_UART8](#a8cd02f97af1db57427c652132b9dc065)   0x798 |
| #define | [STM32\_RESET\_PERIPH\_UART9](#aeb438be7b039d1d301273bd557f6d3ae)   0x79C |

## Macro Definition Documentation

## [◆ ](#a47abaeb040742e28fdb98aac76d5bc38)STM32\_RESET

| #define STM32\_RESET | ( |  | *per*, |
| --- | --- | --- | --- |
|  |  |  | *bit* ) |

**Value:**

(((STM32\_RESET\_PERIPH\_##per##) << 5U) | (bit))

Pack RCC register offset and bit in one 32-bit value.

5 LSBs are used to keep bit number in 32-bit RCC register. Next 12 bits are used to keep RCC register offset. Remaining bits are unused.

Parameters
:   | per | STM32 peripheral name |
    | --- | --- |
    | bit | Reset bit |

## [◆ ](#a300d2fa9b0d1f3e45fa6602c8961294a)STM32\_RESET\_PERIPH\_UART4

| #define STM32\_RESET\_PERIPH\_UART4   0x788 |
| --- |

## [◆ ](#a027d34aecea80dba893a640ec8fe7c7f)STM32\_RESET\_PERIPH\_UART5

| #define STM32\_RESET\_PERIPH\_UART5   0x78C |
| --- |

## [◆ ](#aed8be264b66a3722b3c2145aa000a13f)STM32\_RESET\_PERIPH\_UART7

| #define STM32\_RESET\_PERIPH\_UART7   0x794 |
| --- |

## [◆ ](#a8cd02f97af1db57427c652132b9dc065)STM32\_RESET\_PERIPH\_UART8

| #define STM32\_RESET\_PERIPH\_UART8   0x798 |
| --- |

## [◆ ](#aeb438be7b039d1d301273bd557f6d3ae)STM32\_RESET\_PERIPH\_UART9

| #define STM32\_RESET\_PERIPH\_UART9   0x79C |
| --- |

## [◆ ](#a43b84745610e5dbdea3cfb253dc07b1c)STM32\_RESET\_PERIPH\_USART1

| #define STM32\_RESET\_PERIPH\_USART1   0x77C |
| --- |

## [◆ ](#a6a85d397faeb4b9dbcba84b82cb46312)STM32\_RESET\_PERIPH\_USART2

| #define STM32\_RESET\_PERIPH\_USART2   0x780 |
| --- |

## [◆ ](#a97840fd9714543ef1702c08f330a8aa8)STM32\_RESET\_PERIPH\_USART3

| #define STM32\_RESET\_PERIPH\_USART3   0x784 |
| --- |

## [◆ ](#a8a5634c095db0805d72bab6013df0fdb)STM32\_RESET\_PERIPH\_USART6

| #define STM32\_RESET\_PERIPH\_USART6   0x790 |
| --- |

## [◆ ](#a1eee43a8d6b28956f35c394a1917b363)STM32\_RST

| #define STM32\_RST   0U |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [reset](dir_10e63a26bda611813cb588c12a3608a6.md)
- [stm32mp2\_reset.h](stm32mp2__reset_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
