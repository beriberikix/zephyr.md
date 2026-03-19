---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/stm32-pinctrl-common_8h.html
original_path: doxygen/html/stm32-pinctrl-common_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

stm32-pinctrl-common.h File Reference

[Go to the source code of this file.](stm32-pinctrl-common_8h_source.md)

| Macros | |
| --- | --- |
| #define | [STM32\_PORTA](#a031a76d5d56cbb86e5c5dffad52732b5)   0 /\* IO port A \*/ |
|  | numerical IDs for IO ports |
| #define | [STM32\_PORTB](#ab5be546a1dccb589e6be842575829019)   1 /\* .. \*/ |
| #define | [STM32\_PORTC](#ac56b63d53a5c187035e4386bdb5e6ffa)   2 |
| #define | [STM32\_PORTD](#a866773d51364d1821245a910c03e8686)   3 |
| #define | [STM32\_PORTE](#a1402c542481316eedd39e3cda89410bf)   4 |
| #define | [STM32\_PORTF](#aac43eb483c2b7b744c216b9e2cf62770)   5 |
| #define | [STM32\_PORTG](#ac4464e020843f97772036ae27da7abd5)   6 |
| #define | [STM32\_PORTH](#a744d089635ebefd4bfb65b673699256a)   7 |
| #define | [STM32\_PORTI](#ab11184138506e9df5e93a10f28f45d63)   8 |
| #define | [STM32\_PORTJ](#a0ea163478aef753a739f96f9bf448d8b)   9 |
| #define | [STM32\_PORTK](#a057f431270f633fedc990bb971ce6a05)   10 /\* IO port K \*/ |
| #define | [STM32\_PORTM](#a19abb84f712b1899d8aaadfad34301bd)   12 /\* IO port M (0xC) \*/ |
| #define | [STM32\_PORTN](#ac354044c6615887e456a65a0aa5e226c)   13 |
| #define | [STM32\_PORTO](#ac363d8900ccc9a9e7b022c8f558b53f7)   14 |
| #define | [STM32\_PORTP](#a2bc75591bd6f3010c0b58b66bead967d)   15 /\* IO port P (0xF) \*/ |
| #define | [STM32\_PORTQ](#abba293dc8f52c5ef4329037eb499fecf)   16 /\* IO port Q (0x10) \*/ |
| #define | [STM32\_PORTS\_MAX](#a615b26e8931dfb9ed75e49368eac572d)   ([STM32\_PORTQ](#abba293dc8f52c5ef4329037eb499fecf) + 1) |
| #define | [STM32PIN](#ae496c0ca2dc170f1443b6e35db2a2d1e)(\_port, \_pin) |
|  | helper macro to encode an IO port pin in a numerical format |

## Macro Definition Documentation

## [◆ ](#a031a76d5d56cbb86e5c5dffad52732b5)STM32\_PORTA

| #define STM32\_PORTA   0 /\* IO port A \*/ |
| --- |

numerical IDs for IO ports

## [◆ ](#ab5be546a1dccb589e6be842575829019)STM32\_PORTB

| #define STM32\_PORTB   1 /\* .. \*/ |
| --- |

## [◆ ](#ac56b63d53a5c187035e4386bdb5e6ffa)STM32\_PORTC

| #define STM32\_PORTC   2 |
| --- |

## [◆ ](#a866773d51364d1821245a910c03e8686)STM32\_PORTD

| #define STM32\_PORTD   3 |
| --- |

## [◆ ](#a1402c542481316eedd39e3cda89410bf)STM32\_PORTE

| #define STM32\_PORTE   4 |
| --- |

## [◆ ](#aac43eb483c2b7b744c216b9e2cf62770)STM32\_PORTF

| #define STM32\_PORTF   5 |
| --- |

## [◆ ](#ac4464e020843f97772036ae27da7abd5)STM32\_PORTG

| #define STM32\_PORTG   6 |
| --- |

## [◆ ](#a744d089635ebefd4bfb65b673699256a)STM32\_PORTH

| #define STM32\_PORTH   7 |
| --- |

## [◆ ](#ab11184138506e9df5e93a10f28f45d63)STM32\_PORTI

| #define STM32\_PORTI   8 |
| --- |

## [◆ ](#a0ea163478aef753a739f96f9bf448d8b)STM32\_PORTJ

| #define STM32\_PORTJ   9 |
| --- |

## [◆ ](#a057f431270f633fedc990bb971ce6a05)STM32\_PORTK

| #define STM32\_PORTK   10 /\* IO port K \*/ |
| --- |

## [◆ ](#a19abb84f712b1899d8aaadfad34301bd)STM32\_PORTM

| #define STM32\_PORTM   12 /\* IO port M (0xC) \*/ |
| --- |

## [◆ ](#ac354044c6615887e456a65a0aa5e226c)STM32\_PORTN

| #define STM32\_PORTN   13 |
| --- |

## [◆ ](#ac363d8900ccc9a9e7b022c8f558b53f7)STM32\_PORTO

| #define STM32\_PORTO   14 |
| --- |

## [◆ ](#a2bc75591bd6f3010c0b58b66bead967d)STM32\_PORTP

| #define STM32\_PORTP   15 /\* IO port P (0xF) \*/ |
| --- |

## [◆ ](#abba293dc8f52c5ef4329037eb499fecf)STM32\_PORTQ

| #define STM32\_PORTQ   16 /\* IO port Q (0x10) \*/ |
| --- |

## [◆ ](#a615b26e8931dfb9ed75e49368eac572d)STM32\_PORTS\_MAX

| #define STM32\_PORTS\_MAX   ([STM32\_PORTQ](#abba293dc8f52c5ef4329037eb499fecf) + 1) |
| --- |

## [◆ ](#ae496c0ca2dc170f1443b6e35db2a2d1e)STM32PIN

| #define STM32PIN | ( |  | *\_port*, |
| --- | --- | --- | --- |
|  |  |  | *\_pin* ) |

**Value:**

(\_port << 4 | \_pin)

helper macro to encode an IO port pin in a numerical format

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [pinctrl](dir_2c6c4fbd167577104b7f1b7148586168.md)
- [stm32-pinctrl-common.h](stm32-pinctrl-common_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
