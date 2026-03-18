---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/stm32__clock_8h_source.html
original_path: doxygen/html/stm32__clock_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

stm32\_clock.h

[Go to the documentation of this file.](stm32__clock_8h.md)

1/\*

2 \* Copyright (c) 2017 Linaro Limited

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_STM32\_CLOCK\_H\_

7#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_STM32\_CLOCK\_H\_

8

9/\* clock bus references \*/

[ 10](stm32__clock_8h.md#a186de4b3566a20794e4483a9569abe3c)#define STM32\_CLOCK\_BUS\_AHB1 0

[ 11](stm32__clock_8h.md#a5e58ef1846c185b04bed598b26ee9205)#define STM32\_CLOCK\_BUS\_AHB2 1

[ 12](stm32__clock_8h.md#ac763945fc36124f9c978c423826faa95)#define STM32\_CLOCK\_BUS\_APB1 2

[ 13](stm32__clock_8h.md#adb7becb609763568b91303041c9cd4db)#define STM32\_CLOCK\_BUS\_APB2 3

[ 14](stm32__clock_8h.md#ad25510091b50e823c9860089a9f23deb)#define STM32\_CLOCK\_BUS\_APB1\_2 4

[ 15](stm32__clock_8h.md#afe5b12955e87bbfcee6107cc30e45566)#define STM32\_CLOCK\_BUS\_IOP 5

[ 16](stm32__clock_8h.md#ab2a3c819828eb0186ac3a3f15f4b4569)#define STM32\_CLOCK\_BUS\_AHB3 6

[ 17](stm32__clock_8h.md#a49bccabc3065f192086f16929a7b762d)#define STM32\_CLOCK\_BUS\_AHB4 7

[ 18](stm32__clock_8h.md#a623a8ba4dc47622dfbf76801f1582f58)#define STM32\_CLOCK\_BUS\_AHB5 8

[ 19](stm32__clock_8h.md#a19119341d73264f1f9f18f3fe64f7bd1)#define STM32\_CLOCK\_BUS\_AHB6 9

[ 20](stm32__clock_8h.md#af7165e22b71d1beaf0dd4f59d5b4db6d)#define STM32\_CLOCK\_BUS\_APB3 10

[ 21](stm32__clock_8h.md#a537105e6125ce3b95a2d69435f47dd51)#define STM32\_CLOCK\_BUS\_APB4 11

[ 22](stm32__clock_8h.md#a02ec780a692439efebf0bf8181bf7803)#define STM32\_CLOCK\_BUS\_APB5 12

[ 23](stm32__clock_8h.md#afe87230be68798e4db9e8595af3ff6db)#define STM32\_CLOCK\_BUS\_AXI 13

[ 24](stm32__clock_8h.md#a4c2bfe9e27dec9ea022d0fd6bb053609)#define STM32\_CLOCK\_BUS\_MLAHB 14

25

26#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_STM32\_CLOCK\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [clock](dir_6e9992ac75fd0b7a50e889108957c907.md)
- [stm32\_clock.h](stm32__clock_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
