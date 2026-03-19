---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/stm32l1__clock_8h_source.html
original_path: doxygen/html/stm32l1__clock_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

stm32l1\_clock.h

[Go to the documentation of this file.](stm32l1__clock_8h.md)

1/\*

2 \* Copyright (c) 2022 Linaro Limited

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_STM32L1\_CLOCK\_H\_

7#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_STM32L1\_CLOCK\_H\_

8

9#include "[stm32\_common\_clocks.h](stm32__common__clocks_8h.md)"

10

[ 12](stm32l1__clock_8h.md#a186de4b3566a20794e4483a9569abe3c)#define STM32\_CLOCK\_BUS\_AHB1 0x01c

[ 13](stm32l1__clock_8h.md#adb7becb609763568b91303041c9cd4db)#define STM32\_CLOCK\_BUS\_APB2 0x020

[ 14](stm32l1__clock_8h.md#ac763945fc36124f9c978c423826faa95)#define STM32\_CLOCK\_BUS\_APB1 0x024

15

[ 16](stm32l1__clock_8h.md#acc0577552371fcda95685f6424ecb4b2)#define STM32\_PERIPH\_BUS\_MIN STM32\_CLOCK\_BUS\_AHB1

[ 17](stm32l1__clock_8h.md#a561265772438ab8995251760c7f3dc30)#define STM32\_PERIPH\_BUS\_MAX STM32\_CLOCK\_BUS\_APB1

18

20/\* RM0038.pdf, §6.3.14 Control/status register (RCC\_CSR) \*/

21

23/\* defined in stm32\_common\_clocks.h \*/

25/\* Low speed clocks defined in stm32\_common\_clocks.h \*/

[ 26](stm32l1__clock_8h.md#aa7e82706a146d0f40dc7e9755b3be9a6)#define STM32\_SRC\_HSE (STM32\_SRC\_LSI + 1)

[ 27](stm32l1__clock_8h.md#a7bc1dd03186b763b407a044ddffb4ab2)#define STM32\_SRC\_HSI (STM32\_SRC\_HSE + 1)

28

[ 29](stm32l1__clock_8h.md#a33d66849c63db64784317260b06ceb24)#define STM32\_CLOCK\_REG\_MASK 0xFFU

[ 30](stm32l1__clock_8h.md#a2e73bdb1691751ffd616a5c4e2762423)#define STM32\_CLOCK\_REG\_SHIFT 0U

[ 31](stm32l1__clock_8h.md#af3001a7541ea4df9e4948fd559352f60)#define STM32\_CLOCK\_SHIFT\_MASK 0x1FU

[ 32](stm32l1__clock_8h.md#a147846b77bd51e42c85bea5aca50ad4f)#define STM32\_CLOCK\_SHIFT\_SHIFT 8U

[ 33](stm32l1__clock_8h.md#a63ecbd205c0dd6cb3eab7bcbfdce38b9)#define STM32\_CLOCK\_MASK\_MASK 0x7U

[ 34](stm32l1__clock_8h.md#abfdb31d824fc5c6cf809a1dcff022b5d)#define STM32\_CLOCK\_MASK\_SHIFT 13U

[ 35](stm32l1__clock_8h.md#a6b4f80c7dbd047ca1ebac0b233ad1d1b)#define STM32\_CLOCK\_VAL\_MASK 0x7U

[ 36](stm32l1__clock_8h.md#adf2ca8c7f707b82b7ec4820dfc32929a)#define STM32\_CLOCK\_VAL\_SHIFT 16U

37

[ 51](stm32l1__clock_8h.md#a13a09d4e73c5f6485cbbb541c9e81c35)#define STM32\_DOMAIN\_CLOCK(val, mask, shift, reg) \

52 ((((reg) & STM32\_CLOCK\_REG\_MASK) << STM32\_CLOCK\_REG\_SHIFT) | \

53 (((shift) & STM32\_CLOCK\_SHIFT\_MASK) << STM32\_CLOCK\_SHIFT\_SHIFT) | \

54 (((mask) & STM32\_CLOCK\_MASK\_MASK) << STM32\_CLOCK\_MASK\_SHIFT) | \

55 (((val) & STM32\_CLOCK\_VAL\_MASK) << STM32\_CLOCK\_VAL\_SHIFT))

56

[ 58](stm32l1__clock_8h.md#a16c4f3ac8a8c6255620516b3a32b7a70)#define CSR\_REG 0x34

59

[ 60](stm32l1__clock_8h.md#a4836377699efa295c56d340e150695b0)#define RTC\_SEL(val) STM32\_DOMAIN\_CLOCK(val, 3, 16, CSR\_REG)

61

62#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_STM32L1\_CLOCK\_H\_ \*/

[stm32\_common\_clocks.h](stm32__common__clocks_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [clock](dir_6e9992ac75fd0b7a50e889108957c907.md)
- [stm32l1\_clock.h](stm32l1__clock_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
