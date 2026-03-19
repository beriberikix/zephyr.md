---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/sensor_2bd8lb600fs_8h_source.html
original_path: doxygen/html/sensor_2bd8lb600fs_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bd8lb600fs.h

[Go to the documentation of this file.](sensor_2bd8lb600fs_8h.md)

1/\*

2 \* Copyright (c) 2024 SILA Embedded Solutions GmbH

3 \* SPDX-License-Identifier: Apache-2.0

4 \*/

5

6#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_SENSOR\_BD8LB600FS\_H\_

7#define ZEPHYR\_INCLUDE\_DRIVERS\_SENSOR\_BD8LB600FS\_H\_

8

9#include <[zephyr/drivers/sensor.h](sensor_8h.md)>

10

[ 11](sensor_2bd8lb600fs_8h.md#aaeae18fce2525ea91a9e02566ab455ea)enum [sensor\_channel\_bd8lb600fs](sensor_2bd8lb600fs_8h.md#aaeae18fce2525ea91a9e02566ab455ea) {

[ 16](sensor_2bd8lb600fs_8h.md#aaeae18fce2525ea91a9e02566ab455eaa13ecf27f56653ee4e9d2b7a115a68587) [SENSOR\_CHAN\_BD8LB600FS\_OPEN\_LOAD](sensor_2bd8lb600fs_8h.md#aaeae18fce2525ea91a9e02566ab455eaa13ecf27f56653ee4e9d2b7a115a68587) = [SENSOR\_ATTR\_PRIV\_START](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940bafb4b5859bc369f817f60eaa161bcefc3),

[ 21](sensor_2bd8lb600fs_8h.md#aaeae18fce2525ea91a9e02566ab455eaad9d0c933554c3ca6667508ea32fda3de) [SENSOR\_CHAN\_BD8LB600FS\_OVER\_CURRENT\_OR\_THERMAL\_SHUTDOWN](sensor_2bd8lb600fs_8h.md#aaeae18fce2525ea91a9e02566ab455eaad9d0c933554c3ca6667508ea32fda3de),

22};

23

24#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_SENSOR\_BD8LB600FS\_H\_ \*/

[SENSOR\_ATTR\_PRIV\_START](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940bafb4b5859bc369f817f60eaa161bcefc3)

@ SENSOR\_ATTR\_PRIV\_START

This and higher values are sensor specific.

**Definition** sensor.h:359

[sensor\_channel\_bd8lb600fs](sensor_2bd8lb600fs_8h.md#aaeae18fce2525ea91a9e02566ab455ea)

sensor\_channel\_bd8lb600fs

**Definition** bd8lb600fs.h:11

[SENSOR\_CHAN\_BD8LB600FS\_OPEN\_LOAD](sensor_2bd8lb600fs_8h.md#aaeae18fce2525ea91a9e02566ab455eaa13ecf27f56653ee4e9d2b7a115a68587)

@ SENSOR\_CHAN\_BD8LB600FS\_OPEN\_LOAD

Open load detected, boolean with one bit per output.

**Definition** bd8lb600fs.h:16

[SENSOR\_CHAN\_BD8LB600FS\_OVER\_CURRENT\_OR\_THERMAL\_SHUTDOWN](sensor_2bd8lb600fs_8h.md#aaeae18fce2525ea91a9e02566ab455eaad9d0c933554c3ca6667508ea32fda3de)

@ SENSOR\_CHAN\_BD8LB600FS\_OVER\_CURRENT\_OR\_THERMAL\_SHUTDOWN

Over current protection or thermal shutdown, boolean with one bit per output.

**Definition** bd8lb600fs.h:21

[sensor.h](sensor_8h.md)

Public APIs for the sensor driver.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [sensor](dir_b6423b3a8fc1c9278ff19cba182cfe6d.md)
- [bd8lb600fs.h](sensor_2bd8lb600fs_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
