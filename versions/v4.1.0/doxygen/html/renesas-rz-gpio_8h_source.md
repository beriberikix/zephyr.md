---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/renesas-rz-gpio_8h_source.html
original_path: doxygen/html/renesas-rz-gpio_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

renesas-rz-gpio.h

[Go to the documentation of this file.](renesas-rz-gpio_8h.md)

1/\*

2 \* Copyright (c) 2024 Renesas Electronics Corporation

3 \* SPDX-License-Identifier: Apache-2.0

4 \*/

5

6#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_GPIO\_RENESAS\_RZ\_GPIO\_H\_

7#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_GPIO\_RENESAS\_RZ\_GPIO\_H\_

8

9/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*RZG3S\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*/

10

27

28/\* GPIO drive IOLH \*/

[ 29](renesas-rz-gpio_8h.md#a50350917566913f95cdc02a843bdbb0f)#define RZG3S\_GPIO\_IOLH\_SHIFT 7U

[ 30](renesas-rz-gpio_8h.md#ac52f50ae237947ab33ee0490ef7cefa2)#define RZG3S\_GPIO\_IOLH\_SET(iolh\_val) (iolh\_val << RZG3S\_GPIO\_IOLH\_SHIFT)

31

32/\* GPIO filter \*/

[ 33](renesas-rz-gpio_8h.md#a0cb876606c6b3540026074f8ebdf12b5)#define RZG3S\_GPIO\_FILTER\_SHIFT 9U

[ 34](renesas-rz-gpio_8h.md#a8780a0482bc050ad51ba807f2de8bb34)#define RZG3S\_GPIO\_FILNUM\_SHIFT 1U

[ 35](renesas-rz-gpio_8h.md#a203b3330bbf774fa6b892c9d5e2d3421)#define RZG3S\_GPIO\_FILCLKSEL\_SHIFT 3U

[ 36](renesas-rz-gpio_8h.md#a618c746bd23b346a7c9edda84e3d75e1)#define RZG3S\_GPIO\_FILTER\_SET(fillonoff, filnum, filclksel) \

37 (((fillonoff) | ((filnum) << RZG3S\_GPIO\_FILNUM\_SHIFT) | \

38 ((filclksel) << RZG3S\_GPIO\_FILCLKSEL\_SHIFT)) \

39 << RZG3S\_GPIO\_FILTER\_SHIFT)

40

41/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*/

42

43#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_GPIO\_RENESAS\_RZ\_GPIO\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [gpio](dir_9486826309e816a7a1c2256ae23b5ea4.md)
- [renesas-rz-gpio.h](renesas-rz-gpio_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
