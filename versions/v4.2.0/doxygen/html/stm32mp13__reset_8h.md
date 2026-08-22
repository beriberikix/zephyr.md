---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/stm32mp13__reset_8h.html
original_path: doxygen/html/stm32mp13__reset_8h.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

stm32mp13\_reset.h File Reference

[Go to the source code of this file.](stm32mp13__reset_8h_source.md)

| Macros | |
| --- | --- |
| #define | [STM32\_RESET](#a6a12a4b8c042157a88ddf7da442c137c)(bus, bit) |
|  | Pack RCC register offset and bit in one 32-bit value. |
| #define | [STM32\_RESET\_BUS\_AHB2\_SET](#ab55f5575ee21b073d480395a59ead008)   0x6D0 |
| #define | [STM32\_RESET\_BUS\_AHB2\_CLR](#a7624b08ee69d98c86a1bc09ee9cba910)   0x6D4 |
| #define | [STM32\_RESET\_BUS\_AHB4\_SET](#a232e3956b0266c47949ea93337046315)   0x6E0 |
| #define | [STM32\_RESET\_BUS\_AHB4\_CLR](#aea45c9c2df4e1952aa97d420e0f885c2)   0x6E4 |
| #define | [STM32\_RESET\_BUS\_AHB5\_SET](#a7f5e567e3833461b873f805399b36fd7)   0x6E8 |
| #define | [STM32\_RESET\_BUS\_AHB5\_CLR](#af6c335ddd329320a44f189e841bcd1db)   0x6EC |
| #define | [STM32\_RESET\_BUS\_AHB6\_SET](#a8e75f619e66099d98e0c8efc44fe27be)   0x6F0 |
| #define | [STM32\_RESET\_BUS\_AHB6\_CLR](#aa9326e6f5d2fd8e87fe42d3d78b39e6a)   0x6F4 |
| #define | [STM32\_RESET\_BUS\_APB1\_SET](#a25217083a2dac628893634d856215315)   0x6A0 |
| #define | [STM32\_RESET\_BUS\_APB1\_CLR](#ac01f123c6ec7e850f7ae7ade030ece5a)   0x6A4 |
| #define | [STM32\_RESET\_BUS\_APB2\_SET](#a303a9edc6f689e409eaac1637380f561)   0x6A8 |
| #define | [STM32\_RESET\_BUS\_APB2\_CLR](#ad1dd0a98cd9aeef7b6ce6a5e164a9ee2)   0x6AC |
| #define | [STM32\_RESET\_BUS\_APB3\_SET](#ad87c6a0a7730c8538b146e538b725df8)   0x6B0 |
| #define | [STM32\_RESET\_BUS\_APB3\_CLR](#a84b57afe9b2978342adc977c5b133e57)   0x6B4 |
| #define | [STM32\_RESET\_BUS\_APB4\_SET](#a3dbf1e7f6c3abde92f99f7a65988466c)   0x6B8 |
| #define | [STM32\_RESET\_BUS\_APB4\_CLR](#a0aeb9e8176ec287c167ce97894a43b8c)   0x6BC |
| #define | [STM32\_RESET\_BUS\_APB5\_SET](#a67fb91104add3dc7f46046ecff6f7981)   0x6C0 |
| #define | [STM32\_RESET\_BUS\_APB5\_CLR](#a266c4038446770233340b8713b5a0489)   0x6C4 |
| #define | [STM32\_RESET\_BUS\_APB6\_SET](#ab04635f4571ba5014421a4355d8ef61b)   0x6C8 |
| #define | [STM32\_RESET\_BUS\_APB6\_CLR](#ab404c5a753bd9307734e37445c1e07e4)   0x6CC |

## Macro Definition Documentation

## [◆ ](#a6a12a4b8c042157a88ddf7da442c137c)STM32\_RESET

| #define STM32\_RESET | ( |  | *bus*, |
| --- | --- | --- | --- |
|  |  |  | *bit* ) |

**Value:**

(((STM32\_RESET\_BUS\_##bus##\_CLR) << 17U) | ((STM32\_RESET\_BUS\_##bus##\_SET) << 5U) | (bit))

Pack RCC register offset and bit in one 32-bit value.

bits[4..0] stores the reset controller bit in 32bit RCC register bits[16..5] stores the reset controller set register offset from RCC base bits[28..17] stores the reset controller clear register offset from RCC base

Parameters
:   | bus | STM32 bus name |
    | --- | --- |
    | bit | Reset bit |

## [◆ ](#a7624b08ee69d98c86a1bc09ee9cba910)STM32\_RESET\_BUS\_AHB2\_CLR

| #define STM32\_RESET\_BUS\_AHB2\_CLR   0x6D4 |
| --- |

## [◆ ](#ab55f5575ee21b073d480395a59ead008)STM32\_RESET\_BUS\_AHB2\_SET

| #define STM32\_RESET\_BUS\_AHB2\_SET   0x6D0 |
| --- |

## [◆ ](#aea45c9c2df4e1952aa97d420e0f885c2)STM32\_RESET\_BUS\_AHB4\_CLR

| #define STM32\_RESET\_BUS\_AHB4\_CLR   0x6E4 |
| --- |

## [◆ ](#a232e3956b0266c47949ea93337046315)STM32\_RESET\_BUS\_AHB4\_SET

| #define STM32\_RESET\_BUS\_AHB4\_SET   0x6E0 |
| --- |

## [◆ ](#af6c335ddd329320a44f189e841bcd1db)STM32\_RESET\_BUS\_AHB5\_CLR

| #define STM32\_RESET\_BUS\_AHB5\_CLR   0x6EC |
| --- |

## [◆ ](#a7f5e567e3833461b873f805399b36fd7)STM32\_RESET\_BUS\_AHB5\_SET

| #define STM32\_RESET\_BUS\_AHB5\_SET   0x6E8 |
| --- |

## [◆ ](#aa9326e6f5d2fd8e87fe42d3d78b39e6a)STM32\_RESET\_BUS\_AHB6\_CLR

| #define STM32\_RESET\_BUS\_AHB6\_CLR   0x6F4 |
| --- |

## [◆ ](#a8e75f619e66099d98e0c8efc44fe27be)STM32\_RESET\_BUS\_AHB6\_SET

| #define STM32\_RESET\_BUS\_AHB6\_SET   0x6F0 |
| --- |

## [◆ ](#ac01f123c6ec7e850f7ae7ade030ece5a)STM32\_RESET\_BUS\_APB1\_CLR

| #define STM32\_RESET\_BUS\_APB1\_CLR   0x6A4 |
| --- |

## [◆ ](#a25217083a2dac628893634d856215315)STM32\_RESET\_BUS\_APB1\_SET

| #define STM32\_RESET\_BUS\_APB1\_SET   0x6A0 |
| --- |

## [◆ ](#ad1dd0a98cd9aeef7b6ce6a5e164a9ee2)STM32\_RESET\_BUS\_APB2\_CLR

| #define STM32\_RESET\_BUS\_APB2\_CLR   0x6AC |
| --- |

## [◆ ](#a303a9edc6f689e409eaac1637380f561)STM32\_RESET\_BUS\_APB2\_SET

| #define STM32\_RESET\_BUS\_APB2\_SET   0x6A8 |
| --- |

## [◆ ](#a84b57afe9b2978342adc977c5b133e57)STM32\_RESET\_BUS\_APB3\_CLR

| #define STM32\_RESET\_BUS\_APB3\_CLR   0x6B4 |
| --- |

## [◆ ](#ad87c6a0a7730c8538b146e538b725df8)STM32\_RESET\_BUS\_APB3\_SET

| #define STM32\_RESET\_BUS\_APB3\_SET   0x6B0 |
| --- |

## [◆ ](#a0aeb9e8176ec287c167ce97894a43b8c)STM32\_RESET\_BUS\_APB4\_CLR

| #define STM32\_RESET\_BUS\_APB4\_CLR   0x6BC |
| --- |

## [◆ ](#a3dbf1e7f6c3abde92f99f7a65988466c)STM32\_RESET\_BUS\_APB4\_SET

| #define STM32\_RESET\_BUS\_APB4\_SET   0x6B8 |
| --- |

## [◆ ](#a266c4038446770233340b8713b5a0489)STM32\_RESET\_BUS\_APB5\_CLR

| #define STM32\_RESET\_BUS\_APB5\_CLR   0x6C4 |
| --- |

## [◆ ](#a67fb91104add3dc7f46046ecff6f7981)STM32\_RESET\_BUS\_APB5\_SET

| #define STM32\_RESET\_BUS\_APB5\_SET   0x6C0 |
| --- |

## [◆ ](#ab404c5a753bd9307734e37445c1e07e4)STM32\_RESET\_BUS\_APB6\_CLR

| #define STM32\_RESET\_BUS\_APB6\_CLR   0x6CC |
| --- |

## [◆ ](#ab04635f4571ba5014421a4355d8ef61b)STM32\_RESET\_BUS\_APB6\_SET

| #define STM32\_RESET\_BUS\_APB6\_SET   0x6C8 |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [reset](dir_10e63a26bda611813cb588c12a3608a6.md)
- [stm32mp13\_reset.h](stm32mp13__reset_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
