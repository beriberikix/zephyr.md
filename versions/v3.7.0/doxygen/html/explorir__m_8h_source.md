---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/explorir__m_8h_source.html
original_path: doxygen/html/explorir__m_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

explorir\_m.h

[Go to the documentation of this file.](explorir__m_8h.md)

1/\*

2 \* Copyright (c) 2023, Vitrolife A/S

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_SENSOR\_EXPLORIR\_M\_H\_

8#define ZEPHYR\_INCLUDE\_DRIVERS\_SENSOR\_EXPLORIR\_M\_H\_

9

10#ifdef \_\_cplusplus

11extern "C" {

12#endif

13

14#include <[zephyr/drivers/sensor.h](sensor_8h.md)>

15

[ 16](explorir__m_8h.md#ae381791648801463bad62c98b551a7c4)enum [sensor\_attribute\_explorir\_m](explorir__m_8h.md#ae381791648801463bad62c98b551a7c4) {

17 /\* Sensor integrated low-pass filter. Values 16, 32, 64, and 128 is allowed \*/

[ 18](explorir__m_8h.md#ae381791648801463bad62c98b551a7c4a5ecbe0b20ab67018a78efa779d216c24) [SENSOR\_ATTR\_EXPLORIR\_M\_FILTER](explorir__m_8h.md#ae381791648801463bad62c98b551a7c4a5ecbe0b20ab67018a78efa779d216c24) = [SENSOR\_ATTR\_PRIV\_START](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940bafb4b5859bc369f817f60eaa161bcefc3),

19};

20

21#ifdef \_\_cplusplus

22}

23#endif

24

25#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_SENSOR\_EXPLORIR\_M\_H\_ \*/

[sensor\_attribute\_explorir\_m](explorir__m_8h.md#ae381791648801463bad62c98b551a7c4)

sensor\_attribute\_explorir\_m

**Definition** explorir\_m.h:16

[SENSOR\_ATTR\_EXPLORIR\_M\_FILTER](explorir__m_8h.md#ae381791648801463bad62c98b551a7c4a5ecbe0b20ab67018a78efa779d216c24)

@ SENSOR\_ATTR\_EXPLORIR\_M\_FILTER

**Definition** explorir\_m.h:18

[SENSOR\_ATTR\_PRIV\_START](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940bafb4b5859bc369f817f60eaa161bcefc3)

@ SENSOR\_ATTR\_PRIV\_START

This and higher values are sensor specific.

**Definition** sensor.h:356

[sensor.h](sensor_8h.md)

Public APIs for the sensor driver.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [sensor](dir_b6423b3a8fc1c9278ff19cba182cfe6d.md)
- [explorir\_m.h](explorir__m_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
