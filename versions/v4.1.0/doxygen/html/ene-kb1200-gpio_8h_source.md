---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/ene-kb1200-gpio_8h_source.html
original_path: doxygen/html/ene-kb1200-gpio_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ene-kb1200-gpio.h

[Go to the documentation of this file.](ene-kb1200-gpio_8h.md)

1/\*

2 \* Copyright (c) 2024 ENE Technology Inc.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_GPIO\_ENE\_KB1200\_GPIO\_H\_

7#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_GPIO\_ENE\_KB1200\_GPIO\_H\_

8

18

20#define KB1200\_GPIO\_VOLTAGE\_POS 8

21#define KB1200\_GPIO\_VOLTAGE\_MASK (1U << KB1200\_GPIO\_VOLTAGE\_POS)

22

23#define KB1200\_GPIO\_DRIVING\_POS 9

24#define KB1200\_GPIO\_DRIVING\_MASK (1U << KB1200\_GPIO\_DRIVING\_POS)

26

[ 28](ene-kb1200-gpio_8h.md#ac4d6a2febad81ac12ea70df48b66daa8)#define KB1200\_GPIO\_VOLTAGE\_DEFAULT (0U << KB1200\_GPIO\_VOLTAGE\_POS)

[ 30](ene-kb1200-gpio_8h.md#a97289e46577a8e5a206d91824750c9fc)#define KB1200\_GPIO\_VOLTAGE\_1P8 (1U << KB1200\_GPIO\_VOLTAGE\_POS)

31

[ 33](ene-kb1200-gpio_8h.md#a19eaa0c7a6564e0de3505846ae536f7d)#define KB1200\_GPIO\_DRIVING\_DEFAULT (0U << KB1200\_GPIO\_DRIVING\_POS)

[ 35](ene-kb1200-gpio_8h.md#a55a268c4cc8feed539006571dc7efce3)#define KB1200\_GPIO\_DRIVING\_16MA (1U << KB1200\_GPIO\_DRIVING\_POS)

36

37

39

40#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_GPIO\_ENE\_KB1200\_GPIO\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [gpio](dir_9486826309e816a7a1c2256ae23b5ea4.md)
- [ene-kb1200-gpio.h](ene-kb1200-gpio_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
