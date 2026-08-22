---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/ite-it51xxx-clock_8h_source.html
original_path: doxygen/html/ite-it51xxx-clock_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ite-it51xxx-clock.h

[Go to the documentation of this file.](ite-it51xxx-clock_8h.md)

1/\*

2 \* Copyright (c) 2025 ITE Corporation. All Rights Reserved.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_IT51XXX\_CLOCK\_H\_

8#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_IT51XXX\_CLOCK\_H\_

9

10/\* Clock control \*/

[ 11](ite-it51xxx-clock_8h.md#a50ec398357ea3a58376e768d57563cf4)#define IT51XXX\_ECPM\_CGCTRL2R\_OFF 0x02

[ 12](ite-it51xxx-clock_8h.md#a8336ba78dfcd5156764552427b71be72)#define IT51XXX\_ECPM\_CGCTRL3R\_OFF 0x05

[ 13](ite-it51xxx-clock_8h.md#a300b7fa3c4c6f22c5722de88c4c31e41)#define IT51XXX\_ECPM\_CGCTRL4R\_OFF 0x09

14

15/\* Clock PLL frequency \*/

[ 16](ite-it51xxx-clock_8h.md#a99dc8631a4f3e85fef982ec2700e5883)#define PLL\_18400\_KHZ 0

[ 17](ite-it51xxx-clock_8h.md#a73327488e054d4ebd806733da1a79bd2)#define PLL\_32300\_KHZ 1

[ 18](ite-it51xxx-clock_8h.md#a527993cd11257946f4f6f2df7d799ebe)#define PLL\_64500\_KHZ 2

[ 19](ite-it51xxx-clock_8h.md#aa323c215c942c9ff9378c693faefb4d9)#define PLL\_48000\_KHZ 3

20

21#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_IT51XXX\_CLOCK\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [clock](dir_6e9992ac75fd0b7a50e889108957c907.md)
- [ite-it51xxx-clock.h](ite-it51xxx-clock_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
