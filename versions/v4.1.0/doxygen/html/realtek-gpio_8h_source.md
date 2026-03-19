---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/realtek-gpio_8h_source.html
original_path: doxygen/html/realtek-gpio_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
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

[ 11](realtek-gpio_8h.md#a0381dff71143b0fadceaaade950340a3)#define RTS5912\_GPIO\_VOLTAGE\_POS 11

[ 12](realtek-gpio_8h.md#a9ab90e903840aec5172596492f12e6b5)#define RTS5912\_GPIO\_VOLTAGE\_MASK (3U << RTS5912\_GPIO\_VOLTAGE\_POS)

13

[ 15](realtek-gpio_8h.md#a91e7d587b96806b3f8403d3532d5a888)#define RTS5912\_GPIO\_VOLTAGE\_DEFAULT (0U << RTS5912\_GPIO\_VOLTAGE\_POS)

[ 17](realtek-gpio_8h.md#a83d8d0f0a827e770de9fe360fe566573)#define RTS5912\_GPIO\_VOLTAGE\_1V8 (1U << RTS5912\_GPIO\_VOLTAGE\_POS)

[ 19](realtek-gpio_8h.md#a24268d0667f7a2266e519c03e6a04395)#define RTS5912\_GPIO\_VOLTAGE\_3V3 (2U << RTS5912\_GPIO\_VOLTAGE\_POS)

[ 21](realtek-gpio_8h.md#a0ca327e5b979185b539f187eabcbc0be)#define RTS5912\_GPIO\_VOLTAGE\_5V0 (3U << RTS5912\_GPIO\_VOLTAGE\_POS)

22

23#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_GPIO\_REALTEK\_GPIO\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [gpio](dir_9486826309e816a7a1c2256ae23b5ea4.md)
- [realtek-gpio.h](realtek-gpio_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
