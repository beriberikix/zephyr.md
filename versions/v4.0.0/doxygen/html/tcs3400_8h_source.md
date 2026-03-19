---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/tcs3400_8h_source.html
original_path: doxygen/html/tcs3400_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

tcs3400.h

[Go to the documentation of this file.](tcs3400_8h.md)

1/\*

2 \* Copyright 2023 Google LLC

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_SENSOR\_TCS3400\_H\_

8#define ZEPHYR\_INCLUDE\_DRIVERS\_SENSOR\_TCS3400\_H\_

9

10#include <[zephyr/drivers/sensor.h](sensor_8h.md)>

11

[ 12](tcs3400_8h.md#a694cb550a836f91650fc2322ef0e74ff)enum [sensor\_attribute\_tcs3400](tcs3400_8h.md#a694cb550a836f91650fc2322ef0e74ff) {

[ 14](tcs3400_8h.md#a694cb550a836f91650fc2322ef0e74ffaf1c0d7ae5e4ace15109fe137d27a726e) [SENSOR\_ATTR\_TCS3400\_INTEGRATION\_CYCLES](tcs3400_8h.md#a694cb550a836f91650fc2322ef0e74ffaf1c0d7ae5e4ace15109fe137d27a726e) = [SENSOR\_ATTR\_PRIV\_START](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940bafb4b5859bc369f817f60eaa161bcefc3),

15};

16

17#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_SENSOR\_TCS3400\_H\_ \*/

[SENSOR\_ATTR\_PRIV\_START](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940bafb4b5859bc369f817f60eaa161bcefc3)

@ SENSOR\_ATTR\_PRIV\_START

This and higher values are sensor specific.

**Definition** sensor.h:359

[sensor.h](sensor_8h.md)

Public APIs for the sensor driver.

[sensor\_attribute\_tcs3400](tcs3400_8h.md#a694cb550a836f91650fc2322ef0e74ff)

sensor\_attribute\_tcs3400

**Definition** tcs3400.h:12

[SENSOR\_ATTR\_TCS3400\_INTEGRATION\_CYCLES](tcs3400_8h.md#a694cb550a836f91650fc2322ef0e74ffaf1c0d7ae5e4ace15109fe137d27a726e)

@ SENSOR\_ATTR\_TCS3400\_INTEGRATION\_CYCLES

RGBC Integration Cycles.

**Definition** tcs3400.h:14

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [sensor](dir_b6423b3a8fc1c9278ff19cba182cfe6d.md)
- [tcs3400.h](tcs3400_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
