---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/nuvoton-npcx-gpio_8h_source.html
original_path: doxygen/html/nuvoton-npcx-gpio_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

nuvoton-npcx-gpio.h

[Go to the documentation of this file.](nuvoton-npcx-gpio_8h.md)

1/\*

2 \* Copyright (c) 2022 Nordic Semiconductor ASA

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_GPIO\_NUVOTON\_NPCX\_GPIO\_H\_

7#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_GPIO\_NUVOTON\_NPCX\_GPIO\_H\_

8

17

19#define NPCX\_GPIO\_VOLTAGE\_POS 11

20#define NPCX\_GPIO\_VOLTAGE\_MASK (1U << NPCX\_GPIO\_VOLTAGE\_POS)

22

[ 24](nuvoton-npcx-gpio_8h.md#a92bcad554a75078ab25a13c59075cdff)#define NPCX\_GPIO\_VOLTAGE\_DEFAULT (0U << NPCX\_GPIO\_VOLTAGE\_POS)

[ 26](nuvoton-npcx-gpio_8h.md#a21a9db9e72ea60be4a01c65113693fcb)#define NPCX\_GPIO\_VOLTAGE\_1P8 (1U << NPCX\_GPIO\_VOLTAGE\_POS)

27

29

30#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_GPIO\_NUVOTON\_NPCX\_GPIO\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [gpio](dir_9486826309e816a7a1c2256ae23b5ea4.md)
- [nuvoton-npcx-gpio.h](nuvoton-npcx-gpio_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
