---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/tdk__apex_8h_source.html
original_path: doxygen/html/tdk__apex_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

tdk\_apex.h

[Go to the documentation of this file.](tdk__apex_8h.md)

1/\*

2 \* Copyright (c) 2024 TDK Invensense

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_SENSOR\_TDK\_APEX\_H\_

8#define ZEPHYR\_INCLUDE\_DRIVERS\_SENSOR\_TDK\_APEX\_H\_

9

10#include <[zephyr/drivers/sensor.h](sensor_8h.md)>

11

19

[ 21](tdk__apex_8h.md#a0dd9a01a81c985de9a3a1edd1d9f84a6)#define TDK\_APEX\_PEDOMETER (1)

[ 22](tdk__apex_8h.md#aa635dbac54613d9f389b0e45de63d274)#define TDK\_APEX\_TILT (2)

[ 23](tdk__apex_8h.md#a5ebd1faf982dd9a4b5b13bda71927afb)#define TDK\_APEX\_SMD (3)

[ 24](tdk__apex_8h.md#adad62736e0caaa3e2d01a810ef180b8a)#define TDK\_APEX\_WOM (4)

25

[ 42](tdk__apex_8h.md#a944436d98a2aea1f93977a2d0738d959)enum [sensor\_channel\_tdk\_apex](tdk__apex_8h.md#a944436d98a2aea1f93977a2d0738d959) {

43

[ 45](tdk__apex_8h.md#a944436d98a2aea1f93977a2d0738d959a5181bce02684391a151723bbd7f86af5) [SENSOR\_CHAN\_APEX\_MOTION](tdk__apex_8h.md#a944436d98a2aea1f93977a2d0738d959a5181bce02684391a151723bbd7f86af5) = [SENSOR\_CHAN\_PRIV\_START](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934ac1f260296289d93a13c5686ca11bdc12),

46};

47#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_SENSOR\_TDK\_APEX\_H\_ \*/

[SENSOR\_CHAN\_PRIV\_START](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934ac1f260296289d93a13c5686ca11bdc12)

@ SENSOR\_CHAN\_PRIV\_START

This and higher values are sensor specific.

**Definition** sensor.h:217

[sensor.h](sensor_8h.md)

Public APIs for the sensor driver.

[sensor\_channel\_tdk\_apex](tdk__apex_8h.md#a944436d98a2aea1f93977a2d0738d959)

sensor\_channel\_tdk\_apex

Extended sensor channel for TDK MEMS supportintg APEX features.

**Definition** tdk\_apex.h:42

[SENSOR\_CHAN\_APEX\_MOTION](tdk__apex_8h.md#a944436d98a2aea1f93977a2d0738d959a5181bce02684391a151723bbd7f86af5)

@ SENSOR\_CHAN\_APEX\_MOTION

APEX features.

**Definition** tdk\_apex.h:45

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [sensor](dir_b6423b3a8fc1c9278ff19cba182cfe6d.md)
- [tdk\_apex.h](tdk__apex_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
