---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/ene-kb106x-gpio_8h_source.html
original_path: doxygen/html/ene-kb106x-gpio_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ene-kb106x-gpio.h

[Go to the documentation of this file.](ene-kb106x-gpio_8h.md)

1/\*

2 \* Copyright (c) 2025 ENE Technology Inc.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_GPIO\_ENE\_KB106X\_GPIO\_H\_

7#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_GPIO\_ENE\_KB106X\_GPIO\_H\_

8

18

20#define ENE\_GPIO\_VOLTAGE\_POS 8

21#define ENE\_GPIO\_VOLTAGE\_MASK (1U << ENE\_GPIO\_VOLTAGE\_POS)

22

23#define ENE\_GPIO\_DRIVING\_POS 9

24#define ENE\_GPIO\_DRIVING\_MASK (1U << ENE\_GPIO\_DRIVING\_POS)

26

[ 28](ene-kb106x-gpio_8h.md#a9f09adacf5a53ad88eb129aace5fc769)#define ENE\_GPIO\_VOLTAGE\_DEFAULT (0U << ENE\_GPIO\_VOLTAGE\_POS)

[ 30](ene-kb106x-gpio_8h.md#a514da2fb72995d3d891d52d802b0c33b)#define ENE\_GPIO\_VOLTAGE\_1P8 (1U << ENE\_GPIO\_VOLTAGE\_POS)

31

[ 33](ene-kb106x-gpio_8h.md#a95fcfd50fc67206cea5d561124388e2d)#define ENE\_GPIO\_DRIVING\_DEFAULT (0U << ENE\_GPIO\_DRIVING\_POS)

[ 35](ene-kb106x-gpio_8h.md#a1f22235e59a9196da91ff2fa3be4c608)#define ENE\_GPIO\_DRIVING\_16MA (1U << ENE\_GPIO\_DRIVING\_POS)

36

38

39#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_GPIO\_ENE\_KB106X\_GPIO\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [gpio](dir_9486826309e816a7a1c2256ae23b5ea4.md)
- [ene-kb106x-gpio.h](ene-kb106x-gpio_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
