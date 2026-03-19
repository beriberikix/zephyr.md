---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/icm42x70_8h_source.html
original_path: doxygen/html/icm42x70_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

icm42x70.h

[Go to the documentation of this file.](icm42x70_8h.md)

1/\*

2 \* Copyright (c) 2024 TDK Invensense

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_SENSOR\_ICM42X70\_H\_

8#define ZEPHYR\_INCLUDE\_DRIVERS\_SENSOR\_ICM42X70\_H\_

9

10#include <[zephyr/drivers/sensor.h](sensor_8h.md)>

11

19

[ 21](icm42x70_8h.md#a5a8bd646a5b720e9da448328a11d3176)#define ICM42X70\_LOW\_NOISE\_MODE (0)

[ 22](icm42x70_8h.md#a7318cc972040290000b6f95ccb8a37a3)#define ICM42X70\_LOW\_POWER\_MODE (1)

23

[ 42](icm42x70_8h.md#a7acfb5a8d5ccd2ea53d994fc46ac3a6b)enum [sensor\_attribute\_icm42x70](icm42x70_8h.md#a7acfb5a8d5ccd2ea53d994fc46ac3a6b) {

44

[ 46](icm42x70_8h.md#a7acfb5a8d5ccd2ea53d994fc46ac3a6babf09c4a7c9f18b6f0ac7273282cbc48c) [SENSOR\_ATTR\_BW\_FILTER\_LPF](icm42x70_8h.md#a7acfb5a8d5ccd2ea53d994fc46ac3a6babf09c4a7c9f18b6f0ac7273282cbc48c) = [SENSOR\_ATTR\_PRIV\_START](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940bafb4b5859bc369f817f60eaa161bcefc3),

[ 48](icm42x70_8h.md#a7acfb5a8d5ccd2ea53d994fc46ac3a6ba8a469c0e9236ce771ad4165670d3842d) [SENSOR\_ATTR\_AVERAGING](icm42x70_8h.md#a7acfb5a8d5ccd2ea53d994fc46ac3a6ba8a469c0e9236ce771ad4165670d3842d),

49};

50#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_SENSOR\_ICM42X70\_H\_ \*/

[SENSOR\_ATTR\_PRIV\_START](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940bafb4b5859bc369f817f60eaa161bcefc3)

@ SENSOR\_ATTR\_PRIV\_START

This and higher values are sensor specific.

**Definition** sensor.h:368

[sensor\_attribute\_icm42x70](icm42x70_8h.md#a7acfb5a8d5ccd2ea53d994fc46ac3a6b)

sensor\_attribute\_icm42x70

Extended sensor attributes for ICM42X70 MEMS sensor.

**Definition** icm42x70.h:42

[SENSOR\_ATTR\_AVERAGING](icm42x70_8h.md#a7acfb5a8d5ccd2ea53d994fc46ac3a6ba8a469c0e9236ce771ad4165670d3842d)

@ SENSOR\_ATTR\_AVERAGING

Averaging configuration.

**Definition** icm42x70.h:48

[SENSOR\_ATTR\_BW\_FILTER\_LPF](icm42x70_8h.md#a7acfb5a8d5ccd2ea53d994fc46ac3a6babf09c4a7c9f18b6f0ac7273282cbc48c)

@ SENSOR\_ATTR\_BW\_FILTER\_LPF

BW filtering.

**Definition** icm42x70.h:46

[sensor.h](sensor_8h.md)

Public APIs for the sensor driver.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [sensor](dir_b6423b3a8fc1c9278ff19cba182cfe6d.md)
- [icm42x70.h](icm42x70_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
