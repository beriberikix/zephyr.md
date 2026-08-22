---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/renesas-rz-gpio_8h_source.html
original_path: doxygen/html/renesas-rz-gpio_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

renesas-rz-gpio.h

[Go to the documentation of this file.](renesas-rz-gpio_8h.md)

1/\*

2 \* Copyright (c) 2024-2025 Renesas Electronics Corporation

3 \* SPDX-License-Identifier: Apache-2.0

4 \*/

5

6#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_GPIO\_RENESAS\_RZ\_GPIO\_H\_

7#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_GPIO\_RENESAS\_RZ\_GPIO\_H\_

8

9/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*RZ/A,G,V\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*/

10

27

28/\* GPIO drive IOLH \*/

[ 29](renesas-rz-gpio_8h.md#afacb3123f587a2129cd1ed472ce2b3e5)#define RZ\_GPIO\_IOLH\_SHIFT 8U

[ 30](renesas-rz-gpio_8h.md#a6916bb2358989ef5498e1c87209dd995)#define RZ\_GPIO\_IOLH\_SET(iolh\_val) (iolh\_val << RZ\_GPIO\_IOLH\_SHIFT)

31

32/\* GPIO filter \*/

[ 33](renesas-rz-gpio_8h.md#aa309713f69b69a9650496f6238380c6d)#define RZ\_GPIO\_FILTER\_SHIFT 10U

[ 34](renesas-rz-gpio_8h.md#a1f1f1a0433c86dc7f50b368bd258a107)#define RZ\_GPIO\_FILNUM\_SHIFT 1U

[ 35](renesas-rz-gpio_8h.md#abcdbf6cf77765df961496a3698f9102d)#define RZ\_GPIO\_FILCLKSEL\_SHIFT 3U

[ 36](renesas-rz-gpio_8h.md#aa905a388dc0ca8b9c532620be7029b8e)#define RZ\_GPIO\_FILTER\_SET(fillonoff, filnum, filclksel) \

37 (((fillonoff) | ((filnum) << RZ\_GPIO\_FILNUM\_SHIFT) | \

38 ((filclksel) << RZ\_GPIO\_FILCLKSEL\_SHIFT)) \

39 << RZ\_GPIO\_FILTER\_SHIFT)

40

41/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*/

42

43#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_GPIO\_RENESAS\_RZ\_GPIO\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [gpio](dir_9486826309e816a7a1c2256ae23b5ea4.md)
- [renesas-rz-gpio.h](renesas-rz-gpio_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
