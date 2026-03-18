---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/fcx__mldx5_8h_source.html
original_path: doxygen/html/fcx__mldx5_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

fcx\_mldx5.h

[Go to the documentation of this file.](fcx__mldx5_8h.md)

1/\*

2 \* Copyright (c) 2024, Vitrolife A/S

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_SENSOR\_FCX\_MLDX5\_H\_

8#define ZEPHYR\_INCLUDE\_DRIVERS\_SENSOR\_FCX\_MLDX5\_H\_

9

10#ifdef \_\_cplusplus

11extern "C" {

12#endif

13

14#include <[zephyr/drivers/sensor.h](sensor_8h.md)>

15

[ 16](fcx__mldx5_8h.md#a61852fad03f2a92a59a20cdc7bbbdd49)enum [sensor\_attribute\_fcx\_mldx5](fcx__mldx5_8h.md#a61852fad03f2a92a59a20cdc7bbbdd49) {

[ 17](fcx__mldx5_8h.md#a61852fad03f2a92a59a20cdc7bbbdd49aac5a09e1192a54d29275ba7f3c9d52b7) [SENSOR\_ATTR\_FCX\_MLDX5\_STATUS](fcx__mldx5_8h.md#a61852fad03f2a92a59a20cdc7bbbdd49aac5a09e1192a54d29275ba7f3c9d52b7) = [SENSOR\_ATTR\_PRIV\_START](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940bafb4b5859bc369f817f60eaa161bcefc3),

[ 18](fcx__mldx5_8h.md#a61852fad03f2a92a59a20cdc7bbbdd49a59ad17024844d8904168256f8f153585) [SENSOR\_ATTR\_FCX\_MLDX5\_RESET](fcx__mldx5_8h.md#a61852fad03f2a92a59a20cdc7bbbdd49a59ad17024844d8904168256f8f153585),

19};

20

[ 21](fcx__mldx5_8h.md#a413367eb7215e5c3e509e3cd039d37b1)enum [fcx\_mldx5\_status](fcx__mldx5_8h.md#a413367eb7215e5c3e509e3cd039d37b1) {

[ 22](fcx__mldx5_8h.md#a413367eb7215e5c3e509e3cd039d37b1adb1e1c971bfaaeecc7d376291f021a00) [FCX\_MLDX5\_STATUS\_STANDBY](fcx__mldx5_8h.md#a413367eb7215e5c3e509e3cd039d37b1adb1e1c971bfaaeecc7d376291f021a00) = 2,

[ 23](fcx__mldx5_8h.md#a413367eb7215e5c3e509e3cd039d37b1a9e08ae3cedf51bbeaccbd390990a6ad4) [FCX\_MLDX5\_STATUS\_RAMP\_UP](fcx__mldx5_8h.md#a413367eb7215e5c3e509e3cd039d37b1a9e08ae3cedf51bbeaccbd390990a6ad4) = 3,

[ 24](fcx__mldx5_8h.md#a413367eb7215e5c3e509e3cd039d37b1a002a770d06574829304afba178f8a179) [FCX\_MLDX5\_STATUS\_RUN](fcx__mldx5_8h.md#a413367eb7215e5c3e509e3cd039d37b1a002a770d06574829304afba178f8a179) = 4,

[ 25](fcx__mldx5_8h.md#a413367eb7215e5c3e509e3cd039d37b1a94945852b893160875764c9d34915540) [FCX\_MLDX5\_STATUS\_ERROR](fcx__mldx5_8h.md#a413367eb7215e5c3e509e3cd039d37b1a94945852b893160875764c9d34915540) = 5,

26 /\* Unknown is not sent by the sensor \*/

[ 27](fcx__mldx5_8h.md#a413367eb7215e5c3e509e3cd039d37b1aa9ec19b887f79f85bf7d61d824698ca7) [FCX\_MLDX5\_STATUS\_UNKNOWN](fcx__mldx5_8h.md#a413367eb7215e5c3e509e3cd039d37b1aa9ec19b887f79f85bf7d61d824698ca7),

28};

29

30#ifdef \_\_cplusplus

31}

32#endif

33

34#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_SENSOR\_FCX\_MLDX5\_H\_ \*/

[fcx\_mldx5\_status](fcx__mldx5_8h.md#a413367eb7215e5c3e509e3cd039d37b1)

fcx\_mldx5\_status

**Definition** fcx\_mldx5.h:21

[FCX\_MLDX5\_STATUS\_RUN](fcx__mldx5_8h.md#a413367eb7215e5c3e509e3cd039d37b1a002a770d06574829304afba178f8a179)

@ FCX\_MLDX5\_STATUS\_RUN

**Definition** fcx\_mldx5.h:24

[FCX\_MLDX5\_STATUS\_ERROR](fcx__mldx5_8h.md#a413367eb7215e5c3e509e3cd039d37b1a94945852b893160875764c9d34915540)

@ FCX\_MLDX5\_STATUS\_ERROR

**Definition** fcx\_mldx5.h:25

[FCX\_MLDX5\_STATUS\_RAMP\_UP](fcx__mldx5_8h.md#a413367eb7215e5c3e509e3cd039d37b1a9e08ae3cedf51bbeaccbd390990a6ad4)

@ FCX\_MLDX5\_STATUS\_RAMP\_UP

**Definition** fcx\_mldx5.h:23

[FCX\_MLDX5\_STATUS\_UNKNOWN](fcx__mldx5_8h.md#a413367eb7215e5c3e509e3cd039d37b1aa9ec19b887f79f85bf7d61d824698ca7)

@ FCX\_MLDX5\_STATUS\_UNKNOWN

**Definition** fcx\_mldx5.h:27

[FCX\_MLDX5\_STATUS\_STANDBY](fcx__mldx5_8h.md#a413367eb7215e5c3e509e3cd039d37b1adb1e1c971bfaaeecc7d376291f021a00)

@ FCX\_MLDX5\_STATUS\_STANDBY

**Definition** fcx\_mldx5.h:22

[sensor\_attribute\_fcx\_mldx5](fcx__mldx5_8h.md#a61852fad03f2a92a59a20cdc7bbbdd49)

sensor\_attribute\_fcx\_mldx5

**Definition** fcx\_mldx5.h:16

[SENSOR\_ATTR\_FCX\_MLDX5\_RESET](fcx__mldx5_8h.md#a61852fad03f2a92a59a20cdc7bbbdd49a59ad17024844d8904168256f8f153585)

@ SENSOR\_ATTR\_FCX\_MLDX5\_RESET

**Definition** fcx\_mldx5.h:18

[SENSOR\_ATTR\_FCX\_MLDX5\_STATUS](fcx__mldx5_8h.md#a61852fad03f2a92a59a20cdc7bbbdd49aac5a09e1192a54d29275ba7f3c9d52b7)

@ SENSOR\_ATTR\_FCX\_MLDX5\_STATUS

**Definition** fcx\_mldx5.h:17

[SENSOR\_ATTR\_PRIV\_START](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940bafb4b5859bc369f817f60eaa161bcefc3)

@ SENSOR\_ATTR\_PRIV\_START

This and higher values are sensor specific.

**Definition** sensor.h:356

[sensor.h](sensor_8h.md)

Public APIs for the sensor driver.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [sensor](dir_b6423b3a8fc1c9278ff19cba182cfe6d.md)
- [fcx\_mldx5.h](fcx__mldx5_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
