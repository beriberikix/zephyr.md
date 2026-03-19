---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/max17055_8h_source.html
original_path: doxygen/html/max17055_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

max17055.h

[Go to the documentation of this file.](max17055_8h.md)

1/\*

2 \* Copyright 2022 Google LLC

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_SENSOR\_MAX17055\_H\_

8#define ZEPHYR\_INCLUDE\_DRIVERS\_SENSOR\_MAX17055\_H\_

9

10#include <[zephyr/drivers/sensor.h](sensor_8h.md)>

11

[ 12](max17055_8h.md#a90757f7b4a0078adedc2907787bb42cd)enum [sensor\_channel\_max17055](max17055_8h.md#a90757f7b4a0078adedc2907787bb42cd) {

[ 14](max17055_8h.md#a90757f7b4a0078adedc2907787bb42cda5be3af0c504d700bf1f9ea848a8c9613) [SENSOR\_CHAN\_MAX17055\_VFOCV](max17055_8h.md#a90757f7b4a0078adedc2907787bb42cda5be3af0c504d700bf1f9ea848a8c9613) = [SENSOR\_CHAN\_PRIV\_START](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934ac1f260296289d93a13c5686ca11bdc12),

15};

16

17#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_SENSOR\_MAX17055\_H\_ \*/

[SENSOR\_CHAN\_PRIV\_START](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934ac1f260296289d93a13c5686ca11bdc12)

@ SENSOR\_CHAN\_PRIV\_START

This and higher values are sensor specific.

**Definition** sensor.h:208

[sensor\_channel\_max17055](max17055_8h.md#a90757f7b4a0078adedc2907787bb42cd)

sensor\_channel\_max17055

**Definition** max17055.h:12

[SENSOR\_CHAN\_MAX17055\_VFOCV](max17055_8h.md#a90757f7b4a0078adedc2907787bb42cda5be3af0c504d700bf1f9ea848a8c9613)

@ SENSOR\_CHAN\_MAX17055\_VFOCV

Battery Open Circuit Voltage.

**Definition** max17055.h:14

[sensor.h](sensor_8h.md)

Public APIs for the sensor driver.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [sensor](dir_b6423b3a8fc1c9278ff19cba182cfe6d.md)
- [max17055.h](max17055_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
