---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/realtek-gpio_8h_source.html
original_path: doxygen/html/realtek-gpio_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

realtek-gpio.h

[Go to the documentation of this file.](realtek-gpio_8h.md)

1/\*

2 \* SPDX-License-Identifier: Apache-2.0

3 \*

4 \* Copyright (c) 2024 Realtek Semiconductor Corporation, SIBG-SD7

5 \* Author: Lin Yu-Cheng <lin\_yu\_cheng@realtek.com>

6 \*/

7

8#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_GPIO\_REALTEK\_GPIO\_H\_

9#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_GPIO\_REALTEK\_GPIO\_H\_

10

[ 12](realtek-gpio_8h.md#ae59327ac268671ea2e20014f17701529)#define RTS5912\_GPIO\_INDETEN BIT(8)

[ 14](realtek-gpio_8h.md#a9f3289747c68c46fa5d8f92ebe0e2283)#define RTS5912\_GPIO\_OUTDRV BIT(9)

[ 16](realtek-gpio_8h.md#aa5af355318f8b6a034b85ed418de6cdd)#define RTS5912\_GPIO\_SLEWRATE BIT(10)

[ 18](realtek-gpio_8h.md#ae65d41879bcb126213ac007808086cee)#define RTS5912\_GPIO\_SCHEN BIT(11)

19

[ 20](realtek-gpio_8h.md#a0381dff71143b0fadceaaade950340a3)#define RTS5912\_GPIO\_VOLTAGE\_POS 12

[ 21](realtek-gpio_8h.md#a9ab90e903840aec5172596492f12e6b5)#define RTS5912\_GPIO\_VOLTAGE\_MASK GENMASK(13, 12)

[ 23](realtek-gpio_8h.md#a91e7d587b96806b3f8403d3532d5a888)#define RTS5912\_GPIO\_VOLTAGE\_DEFAULT (0U << RTS5912\_GPIO\_VOLTAGE\_POS)

[ 25](realtek-gpio_8h.md#a83d8d0f0a827e770de9fe360fe566573)#define RTS5912\_GPIO\_VOLTAGE\_1V8 (1U << RTS5912\_GPIO\_VOLTAGE\_POS)

[ 27](realtek-gpio_8h.md#a24268d0667f7a2266e519c03e6a04395)#define RTS5912\_GPIO\_VOLTAGE\_3V3 (2U << RTS5912\_GPIO\_VOLTAGE\_POS)

[ 29](realtek-gpio_8h.md#a0ca327e5b979185b539f187eabcbc0be)#define RTS5912\_GPIO\_VOLTAGE\_5V0 (3U << RTS5912\_GPIO\_VOLTAGE\_POS)

30

[ 32](realtek-gpio_8h.md#acea96124332b298d7f413105ed2c430f)#define RTS5912\_GPIO\_MFCTRL\_POS 14

[ 33](realtek-gpio_8h.md#a661de5a3eb9f6b97f44735718c29dc43)#define RTS5912\_GPIO\_MFCTRL\_MASK GENMASK(15, 14)

[ 35](realtek-gpio_8h.md#a93faaacf50a46b2209231e7eae2da8b4)#define RTS5912\_GPIO\_MFCTRL\_0 (0U << RTS5912\_GPIO\_MFCTRL\_POS)

[ 36](realtek-gpio_8h.md#adf7208d3ffb32ee5f1d65deff41aaa74)#define RTS5912\_GPIO\_MFCTRL\_1 (1U << RTS5912\_GPIO\_MFCTRL\_POS)

[ 37](realtek-gpio_8h.md#ae492ac80b7741521601d6885d2f1b530)#define RTS5912\_GPIO\_MFCTRL\_2 (2U << RTS5912\_GPIO\_MFCTRL\_POS)

[ 38](realtek-gpio_8h.md#abf987c5c5f861c3d2ff57c664264acd0)#define RTS5912\_GPIO\_MFCTRL\_3 (3U << RTS5912\_GPIO\_MFCTRL\_POS)

[ 40](realtek-gpio_8h.md#a471603d5ffb1be381681a56d19b54757)#define RTS5912\_GPIO\_INTR\_MASK (1U << 21 | 1U << 22 | 1U << 24 | 1U << 25 | 1U << 26)

41

42#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_GPIO\_REALTEK\_GPIO\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [gpio](dir_9486826309e816a7a1c2256ae23b5ea4.md)
- [realtek-gpio.h](realtek-gpio_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
