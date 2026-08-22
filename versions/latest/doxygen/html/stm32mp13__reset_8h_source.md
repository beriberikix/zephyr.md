---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/stm32mp13__reset_8h_source.html
original_path: doxygen/html/stm32mp13__reset_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

stm32mp13\_reset.h

[Go to the documentation of this file.](stm32mp13__reset_8h.md)

1/\*

2 \* Copyright (c) 2025 STMicroelectronics

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_RESET\_STM32MP13\_RESET\_H\_

8#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_RESET\_STM32MP13\_RESET\_H\_

9

[ 20](stm32mp13__reset_8h.md#a6a12a4b8c042157a88ddf7da442c137c)#define STM32\_RESET(bus, bit) \

21 (((STM32\_RESET\_BUS\_##bus##\_CLR) << 17U) | ((STM32\_RESET\_BUS\_##bus##\_SET) << 5U) | (bit))

22

23/\* RCC bus reset register offset \*/

[ 24](stm32mp13__reset_8h.md#ab55f5575ee21b073d480395a59ead008)#define STM32\_RESET\_BUS\_AHB2\_SET 0x6D0

[ 25](stm32mp13__reset_8h.md#a7624b08ee69d98c86a1bc09ee9cba910)#define STM32\_RESET\_BUS\_AHB2\_CLR 0x6D4

[ 26](stm32mp13__reset_8h.md#a232e3956b0266c47949ea93337046315)#define STM32\_RESET\_BUS\_AHB4\_SET 0x6E0

[ 27](stm32mp13__reset_8h.md#aea45c9c2df4e1952aa97d420e0f885c2)#define STM32\_RESET\_BUS\_AHB4\_CLR 0x6E4

[ 28](stm32mp13__reset_8h.md#a7f5e567e3833461b873f805399b36fd7)#define STM32\_RESET\_BUS\_AHB5\_SET 0x6E8

[ 29](stm32mp13__reset_8h.md#af6c335ddd329320a44f189e841bcd1db)#define STM32\_RESET\_BUS\_AHB5\_CLR 0x6EC

[ 30](stm32mp13__reset_8h.md#a8e75f619e66099d98e0c8efc44fe27be)#define STM32\_RESET\_BUS\_AHB6\_SET 0x6F0

[ 31](stm32mp13__reset_8h.md#aa9326e6f5d2fd8e87fe42d3d78b39e6a)#define STM32\_RESET\_BUS\_AHB6\_CLR 0x6F4

[ 32](stm32mp13__reset_8h.md#a25217083a2dac628893634d856215315)#define STM32\_RESET\_BUS\_APB1\_SET 0x6A0

[ 33](stm32mp13__reset_8h.md#ac01f123c6ec7e850f7ae7ade030ece5a)#define STM32\_RESET\_BUS\_APB1\_CLR 0x6A4

[ 34](stm32mp13__reset_8h.md#a303a9edc6f689e409eaac1637380f561)#define STM32\_RESET\_BUS\_APB2\_SET 0x6A8

[ 35](stm32mp13__reset_8h.md#ad1dd0a98cd9aeef7b6ce6a5e164a9ee2)#define STM32\_RESET\_BUS\_APB2\_CLR 0x6AC

[ 36](stm32mp13__reset_8h.md#ad87c6a0a7730c8538b146e538b725df8)#define STM32\_RESET\_BUS\_APB3\_SET 0x6B0

[ 37](stm32mp13__reset_8h.md#a84b57afe9b2978342adc977c5b133e57)#define STM32\_RESET\_BUS\_APB3\_CLR 0x6B4

[ 38](stm32mp13__reset_8h.md#a3dbf1e7f6c3abde92f99f7a65988466c)#define STM32\_RESET\_BUS\_APB4\_SET 0x6B8

[ 39](stm32mp13__reset_8h.md#a0aeb9e8176ec287c167ce97894a43b8c)#define STM32\_RESET\_BUS\_APB4\_CLR 0x6BC

[ 40](stm32mp13__reset_8h.md#a67fb91104add3dc7f46046ecff6f7981)#define STM32\_RESET\_BUS\_APB5\_SET 0x6C0

[ 41](stm32mp13__reset_8h.md#a266c4038446770233340b8713b5a0489)#define STM32\_RESET\_BUS\_APB5\_CLR 0x6C4

[ 42](stm32mp13__reset_8h.md#ab04635f4571ba5014421a4355d8ef61b)#define STM32\_RESET\_BUS\_APB6\_SET 0x6C8

[ 43](stm32mp13__reset_8h.md#ab404c5a753bd9307734e37445c1e07e4)#define STM32\_RESET\_BUS\_APB6\_CLR 0x6CC

44

45#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_RESET\_STM32MP13\_RESET\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [reset](dir_10e63a26bda611813cb588c12a3608a6.md)
- [stm32mp13\_reset.h](stm32mp13__reset_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
