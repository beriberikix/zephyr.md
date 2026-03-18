---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/ite-it8xxx2-gpio_8h_source.html
original_path: doxygen/html/ite-it8xxx2-gpio_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ite-it8xxx2-gpio.h

[Go to the documentation of this file.](ite-it8xxx2-gpio_8h.md)

1/\*

2 \* Copyright (c) 2022 Vestas Wind Systems A/S

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_GPIO\_ITE\_IT8XXX2\_GPIO\_H\_

7#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_GPIO\_ITE\_IT8XXX2\_GPIO\_H\_

8

17

19#define IT8XXX2\_GPIO\_VOLTAGE\_POS 11

20#define IT8XXX2\_GPIO\_VOLTAGE\_MASK (3U << IT8XXX2\_GPIO\_VOLTAGE\_POS)

22

[ 24](ite-it8xxx2-gpio_8h.md#ac65596dfb83850449186a54a915373d8)#define IT8XXX2\_GPIO\_VOLTAGE\_DEFAULT (0U << IT8XXX2\_GPIO\_VOLTAGE\_POS)

[ 26](ite-it8xxx2-gpio_8h.md#ae6592bbcc1426357a96d0308367d74a9)#define IT8XXX2\_GPIO\_VOLTAGE\_1P8 (1U << IT8XXX2\_GPIO\_VOLTAGE\_POS)

[ 28](ite-it8xxx2-gpio_8h.md#a0961ededa9521d8987b57cd8b8401474)#define IT8XXX2\_GPIO\_VOLTAGE\_3P3 (2U << IT8XXX2\_GPIO\_VOLTAGE\_POS)

[ 30](ite-it8xxx2-gpio_8h.md#a058087db025d461980583d2ad38aa0c2)#define IT8XXX2\_GPIO\_VOLTAGE\_5P0 (3U << IT8XXX2\_GPIO\_VOLTAGE\_POS)

31

33

34#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_GPIO\_ITE\_IT8XXX2\_GPIO\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [gpio](dir_9486826309e816a7a1c2256ae23b5ea4.md)
- [ite-it8xxx2-gpio.h](ite-it8xxx2-gpio_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
