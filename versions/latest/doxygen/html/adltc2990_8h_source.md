---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/adltc2990_8h_source.html
original_path: doxygen/html/adltc2990_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

adltc2990.h

[Go to the documentation of this file.](adltc2990_8h.md)

1/\*

2 \* SPDX-FileCopyrightText: Copyright (c) 2024 Jilay Sandeep Pandya

3 \* SPDX-License-Identifier: Apache-2.0

4 \*/

5

6#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_SENSOR\_ADLTC2990\_H\_

7#define ZEPHYR\_INCLUDE\_DRIVERS\_SENSOR\_ADLTC2990\_H\_

8

9#include <[stdbool.h](stdbool_8h.md)>

10

11#include <[zephyr/device.h](device_8h.md)>

12

[ 13](adltc2990_8h.md#a2bb0bc14920f8645b371c194148e8d21)enum [adltc2990\_acquisition\_format](adltc2990_8h.md#a2bb0bc14920f8645b371c194148e8d21) {

[ 14](adltc2990_8h.md#a2bb0bc14920f8645b371c194148e8d21a1dd5299deae992e0aa45231873180415) [ADLTC2990\_REPEATED\_ACQUISITION](adltc2990_8h.md#a2bb0bc14920f8645b371c194148e8d21a1dd5299deae992e0aa45231873180415),

[ 15](adltc2990_8h.md#a2bb0bc14920f8645b371c194148e8d21a24e4c7d8197707dbae839f08ff1fc870) [ADLTC2990\_SINGLE\_SHOT\_ACQUISITION](adltc2990_8h.md#a2bb0bc14920f8645b371c194148e8d21a24e4c7d8197707dbae839f08ff1fc870),

16};

17

[ 27](adltc2990_8h.md#ae6b634f7ff028d3c4a954c111bcbc4d2)int [adltc2990\_is\_busy](adltc2990_8h.md#ae6b634f7ff028d3c4a954c111bcbc4d2)(const struct [device](structdevice.md) \*dev, bool \*is\_busy);

28

[ 38](adltc2990_8h.md#a1952f17894be82e3b09065f79168edde)int [adltc2990\_trigger\_measurement](adltc2990_8h.md#a1952f17894be82e3b09065f79168edde)(const struct [device](structdevice.md) \*dev,

39 enum [adltc2990\_acquisition\_format](adltc2990_8h.md#a2bb0bc14920f8645b371c194148e8d21) format);

40

41#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_SENSOR\_ADLTC2990\_H\_ \*/

[adltc2990\_trigger\_measurement](adltc2990_8h.md#a1952f17894be82e3b09065f79168edde)

int adltc2990\_trigger\_measurement(const struct device \*dev, enum adltc2990\_acquisition\_format format)

Trigger the adltc2990 to start a measurement.

[adltc2990\_acquisition\_format](adltc2990_8h.md#a2bb0bc14920f8645b371c194148e8d21)

adltc2990\_acquisition\_format

**Definition** adltc2990.h:13

[ADLTC2990\_REPEATED\_ACQUISITION](adltc2990_8h.md#a2bb0bc14920f8645b371c194148e8d21a1dd5299deae992e0aa45231873180415)

@ ADLTC2990\_REPEATED\_ACQUISITION

**Definition** adltc2990.h:14

[ADLTC2990\_SINGLE\_SHOT\_ACQUISITION](adltc2990_8h.md#a2bb0bc14920f8645b371c194148e8d21a24e4c7d8197707dbae839f08ff1fc870)

@ ADLTC2990\_SINGLE\_SHOT\_ACQUISITION

**Definition** adltc2990.h:15

[adltc2990\_is\_busy](adltc2990_8h.md#ae6b634f7ff028d3c4a954c111bcbc4d2)

int adltc2990\_is\_busy(const struct device \*dev, bool \*is\_busy)

check if adtlc2990 is busy doing conversion

[device.h](device_8h.md)

[stdbool.h](stdbool_8h.md)

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:453

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [sensor](dir_b6423b3a8fc1c9278ff19cba182cfe6d.md)
- [adltc2990.h](adltc2990_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
