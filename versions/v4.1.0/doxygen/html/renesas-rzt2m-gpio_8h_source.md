---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/renesas-rzt2m-gpio_8h_source.html
original_path: doxygen/html/renesas-rzt2m-gpio_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

renesas-rzt2m-gpio.h

[Go to the documentation of this file.](renesas-rzt2m-gpio_8h.md)

1/\*

2 \* Copyright (c) 2023 Antmicro <www.antmicro.com>

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_GPIO\_RENESAS\_RZT2M\_H\_

8#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_GPIO\_RENESAS\_RZT2M\_H\_

9#include <[zephyr/sys/util.h](sys_2util_8h.md)>

10

[ 11](renesas-rzt2m-gpio_8h.md#a8fdc883e48d39eb950e47c8a7433630f)#define RZT2M\_GPIO\_DRIVE\_OFFSET 8

[ 12](renesas-rzt2m-gpio_8h.md#a16ed0517a7b43d606ea0849ebb2d96a7)#define RZT2M\_GPIO\_DRIVE\_MASK GENMASK(RZT2M\_GPIO\_DRIVE\_OFFSET + 2, RZT2M\_GPIO\_DRIVE\_OFFSET)

13

[ 17](renesas-rzt2m-gpio_8h.md#a0e2542438d2c829d6509399314a01682)#define RZT2M\_GPIO\_DRIVE\_LOW (0U << RZT2M\_GPIO\_DRIVE\_OFFSET)

[ 18](renesas-rzt2m-gpio_8h.md#a683f1d1fc91e508793141734caaef335)#define RZT2M\_GPIO\_DRIVE\_MIDDLE (1U << RZT2M\_GPIO\_DRIVE\_OFFSET)

[ 19](renesas-rzt2m-gpio_8h.md#a814748063a20fe7d971e19d6e296eb59)#define RZT2M\_GPIO\_DRIVE\_HIGH (2U << RZT2M\_GPIO\_DRIVE\_OFFSET)

[ 20](renesas-rzt2m-gpio_8h.md#a2b60d89adec85b941aa8d7963233aafb)#define RZT2M\_GPIO\_DRIVE\_ULTRA\_HIGH (3U << RZT2M\_GPIO\_DRIVE\_OFFSET)

21

[ 22](renesas-rzt2m-gpio_8h.md#a0536626285ce7ba19c1a8baf57365902)#define RZT2M\_GPIO\_SCHMITT\_TRIGGER\_OFFSET 10

[ 23](renesas-rzt2m-gpio_8h.md#a5650f1078ef92c15174bf2ce8c7e6f08)#define RZT2M\_GPIO\_SCHMITT\_TRIGGER\_MASK BIT(RZT2M\_GPIO\_SCHMITT\_TRIGGER\_OFFSET)

24

[ 28](renesas-rzt2m-gpio_8h.md#ac2d2e1cef0fa53eb0ce6f7dcb32cb4ef)#define RZT2M\_GPIO\_SCHMITT\_TRIGGER BIT(RZT2M\_GPIO\_SCHMITT\_TRIGGER\_OFFSET)

29

[ 30](renesas-rzt2m-gpio_8h.md#a4f3e3fb225e921d3405c189b87980a16)#define RZT2M\_GPIO\_SLEW\_RATE\_OFFSET 11

[ 31](renesas-rzt2m-gpio_8h.md#a595d6e02f3fd2168deb2fe06f6d00f7d)#define RZT2M\_GPIO\_SLEW\_RATE\_MASK BIT(RZT2M\_GPIO\_SLEW\_RATE\_OFFSET)

32

[ 36](renesas-rzt2m-gpio_8h.md#a2f754f8752b7c42ee89286725b2be4bb)#define RZT2M\_GPIO\_SLEW\_RATE\_SLOW 0U

[ 37](renesas-rzt2m-gpio_8h.md#a752db650514faa34a43bf14a70746dac)#define RZT2M\_GPIO\_SLEW\_RATE\_FAST BIT(RZT2M\_GPIO\_SLEW\_RATE\_OFFSET)

38

39#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_GPIO\_RENESAS\_RZT2M\_H\_ \*/

[util.h](sys_2util_8h.md)

Misc utilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [gpio](dir_9486826309e816a7a1c2256ae23b5ea4.md)
- [renesas-rzt2m-gpio.h](renesas-rzt2m-gpio_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
