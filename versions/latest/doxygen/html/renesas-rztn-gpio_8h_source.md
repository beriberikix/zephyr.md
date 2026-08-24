---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/renesas-rztn-gpio_8h_source.html
original_path: doxygen/html/renesas-rztn-gpio_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

renesas-rztn-gpio.h

[Go to the documentation of this file.](renesas-rztn-gpio_8h.md)

1/\*

2 \* Copyright (c) 2025 Renesas Electronics Corporation

3 \* SPDX-License-Identifier: Apache-2.0

4 \*/

5

6#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_GPIO\_RENESAS\_RZTN\_GPIO\_H\_

7#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_GPIO\_RENESAS\_RZTN\_GPIO\_H\_

8

9/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*RZTN\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*/

10

26

27/\* GPIO DRCTL register \*/

[ 28](renesas-rztn-gpio_8h.md#a398f7ed2fd6c066ab26045493681af0f)#define RZTN\_GPIO\_DRCTL\_SHIFT 8U

[ 29](renesas-rztn-gpio_8h.md#a5ab9e01109972081f1979e0c02984629)#define RZTN\_GPIO\_SCHMITT\_TRIG\_SHIFT 4U

[ 30](renesas-rztn-gpio_8h.md#a8f596a5b412bc8a744a762e0cfc31b9d)#define RZTN\_GPIO\_SLEW\_RATE\_SHIFT 5U

[ 31](renesas-rztn-gpio_8h.md#a74666258b9d1c0bc26c00cc30bbfb489)#define RZTN\_GPIO\_DRCTL\_SET(drive\_ability, schmitt\_trig, slew\_rate) \

32 (((drive\_ability) | ((schmitt\_trig) << RZTN\_GPIO\_SCHMITT\_TRIG\_SHIFT) | \

33 ((slew\_rate) << RZTN\_GPIO\_SLEW\_RATE\_SHIFT)) \

34 << RZTN\_GPIO\_DRCTL\_SHIFT)

35

36/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*/

37

38#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_GPIO\_RENESAS\_RZTN\_GPIO\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [gpio](dir_9486826309e816a7a1c2256ae23b5ea4.md)
- [renesas-rztn-gpio.h](renesas-rztn-gpio_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
