---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/sensor_2max31790_8h_source.html
original_path: doxygen/html/sensor_2max31790_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

max31790.h

[Go to the documentation of this file.](sensor_2max31790_8h.md)

1/\*

2 \* Copyright (c) 2024 SILA Embedded Solutions GmbH

3 \* SPDX-License-Identifier: Apache-2.0

4 \*/

5

6#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_SENSOR\_MAX31790\_H\_

7#define ZEPHYR\_INCLUDE\_DRIVERS\_SENSOR\_MAX31790\_H\_

8

9#include <[zephyr/drivers/sensor.h](sensor_8h.md)>

10

11/\* MAX31790 specific channels \*/

[ 12](sensor_2max31790_8h.md#a078f3f8c11a5239101cde9fd81afc19d)enum [sensor\_channel\_max31790](sensor_2max31790_8h.md#a078f3f8c11a5239101cde9fd81afc19d) {

[ 13](sensor_2max31790_8h.md#a078f3f8c11a5239101cde9fd81afc19da037d3928c2c3288567feb9b78661d2da) [SENSOR\_CHAN\_MAX31790\_FAN\_FAULT](sensor_2max31790_8h.md#a078f3f8c11a5239101cde9fd81afc19da037d3928c2c3288567feb9b78661d2da) = [SENSOR\_CHAN\_PRIV\_START](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934ac1f260296289d93a13c5686ca11bdc12),

14};

15

16#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_SENSOR\_MAX31790\_H\_ \*/

[SENSOR\_CHAN\_PRIV\_START](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934ac1f260296289d93a13c5686ca11bdc12)

@ SENSOR\_CHAN\_PRIV\_START

This and higher values are sensor specific.

**Definition** sensor.h:217

[sensor\_channel\_max31790](sensor_2max31790_8h.md#a078f3f8c11a5239101cde9fd81afc19d)

sensor\_channel\_max31790

**Definition** max31790.h:12

[SENSOR\_CHAN\_MAX31790\_FAN\_FAULT](sensor_2max31790_8h.md#a078f3f8c11a5239101cde9fd81afc19da037d3928c2c3288567feb9b78661d2da)

@ SENSOR\_CHAN\_MAX31790\_FAN\_FAULT

**Definition** max31790.h:13

[sensor.h](sensor_8h.md)

Public APIs for the sensor driver.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [sensor](dir_b6423b3a8fc1c9278ff19cba182cfe6d.md)
- [max31790.h](sensor_2max31790_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
