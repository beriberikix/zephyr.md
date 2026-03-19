---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/sensor_2tle9104_8h_source.html
original_path: doxygen/html/sensor_2tle9104_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

tle9104.h

[Go to the documentation of this file.](sensor_2tle9104_8h.md)

1/\*

2 \* Copyright (c) 2024 SILA Embedded Solutions GmbH

3 \* SPDX-License-Identifier: Apache-2.0

4 \*/

5

6#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_SENSOR\_TLE9104\_H\_

7#define ZEPHYR\_INCLUDE\_DRIVERS\_SENSOR\_TLE9104\_H\_

8

9#include <[zephyr/drivers/sensor.h](sensor_8h.md)>

10

[ 11](sensor_2tle9104_8h.md#a24f1803a4c7ab65b58e76f200e2bd62e)enum [sensor\_channel\_tle9104](sensor_2tle9104_8h.md#a24f1803a4c7ab65b58e76f200e2bd62e) {

[ 13](sensor_2tle9104_8h.md#a24f1803a4c7ab65b58e76f200e2bd62ea0b1bb727075f758b96fe1b07b94d6002) [SENSOR\_CHAN\_TLE9104\_OPEN\_LOAD](sensor_2tle9104_8h.md#a24f1803a4c7ab65b58e76f200e2bd62ea0b1bb727075f758b96fe1b07b94d6002) = [SENSOR\_ATTR\_PRIV\_START](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940bafb4b5859bc369f817f60eaa161bcefc3),

[ 15](sensor_2tle9104_8h.md#a24f1803a4c7ab65b58e76f200e2bd62ea12ea98989e21cd00c983ede2b4dd28f2) [SENSOR\_CHAN\_TLE9104\_OVER\_CURRENT](sensor_2tle9104_8h.md#a24f1803a4c7ab65b58e76f200e2bd62ea12ea98989e21cd00c983ede2b4dd28f2),

16};

17

18#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_SENSOR\_TLE9104\_H\_ \*/

[SENSOR\_ATTR\_PRIV\_START](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940bafb4b5859bc369f817f60eaa161bcefc3)

@ SENSOR\_ATTR\_PRIV\_START

This and higher values are sensor specific.

**Definition** sensor.h:368

[sensor\_channel\_tle9104](sensor_2tle9104_8h.md#a24f1803a4c7ab65b58e76f200e2bd62e)

sensor\_channel\_tle9104

**Definition** tle9104.h:11

[SENSOR\_CHAN\_TLE9104\_OPEN\_LOAD](sensor_2tle9104_8h.md#a24f1803a4c7ab65b58e76f200e2bd62ea0b1bb727075f758b96fe1b07b94d6002)

@ SENSOR\_CHAN\_TLE9104\_OPEN\_LOAD

Open load detected, boolean with one bit per output.

**Definition** tle9104.h:13

[SENSOR\_CHAN\_TLE9104\_OVER\_CURRENT](sensor_2tle9104_8h.md#a24f1803a4c7ab65b58e76f200e2bd62ea12ea98989e21cd00c983ede2b4dd28f2)

@ SENSOR\_CHAN\_TLE9104\_OVER\_CURRENT

Over current detected, boolean with one bit per output.

**Definition** tle9104.h:15

[sensor.h](sensor_8h.md)

Public APIs for the sensor driver.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [sensor](dir_b6423b3a8fc1c9278ff19cba182cfe6d.md)
- [tle9104.h](sensor_2tle9104_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
