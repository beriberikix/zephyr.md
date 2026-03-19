---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/drivers_2sensor_2tmag5273_8h_source.html
original_path: doxygen/html/drivers_2sensor_2tmag5273_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

tmag5273.h

[Go to the documentation of this file.](drivers_2sensor_2tmag5273_8h.md)

1/\*

2 \* Copyright (c) 2016 Intel Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_SENSOR\_TMAG5273\_H\_

8#define ZEPHYR\_INCLUDE\_DRIVERS\_SENSOR\_TMAG5273\_H\_

9

10#ifdef \_\_cplusplus

11extern "C" {

12#endif

13

14#include <[zephyr/drivers/sensor.h](sensor_8h.md)>

15

16/\* --- Additional TMAG5273 definitions \*/

17

[ 19](drivers_2sensor_2tmag5273_8h.md#a3d91dbb6bc6d7dc90ed889651bc34827)enum [tmag5273\_sensor\_channel](drivers_2sensor_2tmag5273_8h.md#a3d91dbb6bc6d7dc90ed889651bc34827) {

[ 23](drivers_2sensor_2tmag5273_8h.md#a3d91dbb6bc6d7dc90ed889651bc34827a72c52112337e191ab9ce906aecdff92d) [TMAG5273\_CHAN\_MAGNITUDE](drivers_2sensor_2tmag5273_8h.md#a3d91dbb6bc6d7dc90ed889651bc34827a72c52112337e191ab9ce906aecdff92d) = [SENSOR\_CHAN\_PRIV\_START](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934ac1f260296289d93a13c5686ca11bdc12),

24

[ 28](drivers_2sensor_2tmag5273_8h.md#a3d91dbb6bc6d7dc90ed889651bc34827a601dad57092c442da3a0a184737d8003) [TMAG5273\_CHAN\_MAGNITUDE\_MSB](drivers_2sensor_2tmag5273_8h.md#a3d91dbb6bc6d7dc90ed889651bc34827a601dad57092c442da3a0a184737d8003),

29

[ 33](drivers_2sensor_2tmag5273_8h.md#a3d91dbb6bc6d7dc90ed889651bc34827a2c4ff267102871c1d23353bbb6b30dbc) [TMAG5273\_CHAN\_ANGLE\_MAGNITUDE](drivers_2sensor_2tmag5273_8h.md#a3d91dbb6bc6d7dc90ed889651bc34827a2c4ff267102871c1d23353bbb6b30dbc),

34};

35

[ 37](drivers_2sensor_2tmag5273_8h.md#a6fadcd6cd3b5fbc9281d27f37bdfe0a2)enum [tmag5273\_attribute](drivers_2sensor_2tmag5273_8h.md#a6fadcd6cd3b5fbc9281d27f37bdfe0a2) {

[ 48](drivers_2sensor_2tmag5273_8h.md#a6fadcd6cd3b5fbc9281d27f37bdfe0a2af59c66f9794efa1afa7d7461a134d3d3) [TMAG5273\_ATTR\_ANGLE\_MAG\_AXIS](drivers_2sensor_2tmag5273_8h.md#a6fadcd6cd3b5fbc9281d27f37bdfe0a2af59c66f9794efa1afa7d7461a134d3d3) = [SENSOR\_ATTR\_PRIV\_START](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940bafb4b5859bc369f817f60eaa161bcefc3),

49};

50

54

[ 55](drivers_2sensor_2tmag5273_8h.md#a6426061b7a7f444ba7f4d87477144bf0)#define TMAG5273\_ANGLE\_CALC\_NONE 0

[ 56](drivers_2sensor_2tmag5273_8h.md#ac93519e03635876d3b693a0b4a11904a)#define TMAG5273\_ANGLE\_CALC\_XY 1

[ 57](drivers_2sensor_2tmag5273_8h.md#a863266f03d298268103d394eb37bbac9)#define TMAG5273\_ANGLE\_CALC\_YZ 2

[ 58](drivers_2sensor_2tmag5273_8h.md#a84e780517b8fec1845fd145dd0b16f0c)#define TMAG5273\_ANGLE\_CALC\_XZ 3

59

60#ifdef \_\_cplusplus

61}

62#endif

63

64#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_SENSOR\_TMAG5273\_H\_ \*/

[tmag5273\_sensor\_channel](drivers_2sensor_2tmag5273_8h.md#a3d91dbb6bc6d7dc90ed889651bc34827)

tmag5273\_sensor\_channel

Additional channels supported by the TMAG5273.

**Definition** tmag5273.h:19

[TMAG5273\_CHAN\_ANGLE\_MAGNITUDE](drivers_2sensor_2tmag5273_8h.md#a3d91dbb6bc6d7dc90ed889651bc34827a2c4ff267102871c1d23353bbb6b30dbc)

@ TMAG5273\_CHAN\_ANGLE\_MAGNITUDE

Angle result in deg, magnitude result in Gs and magnitude MSB between two axis.

**Definition** tmag5273.h:33

[TMAG5273\_CHAN\_MAGNITUDE\_MSB](drivers_2sensor_2tmag5273_8h.md#a3d91dbb6bc6d7dc90ed889651bc34827a601dad57092c442da3a0a184737d8003)

@ TMAG5273\_CHAN\_MAGNITUDE\_MSB

Magnitude measurement MSB as returned by the sensor.

**Definition** tmag5273.h:28

[TMAG5273\_CHAN\_MAGNITUDE](drivers_2sensor_2tmag5273_8h.md#a3d91dbb6bc6d7dc90ed889651bc34827a72c52112337e191ab9ce906aecdff92d)

@ TMAG5273\_CHAN\_MAGNITUDE

Magnitude measurement result between two axis in Gs.

**Definition** tmag5273.h:23

[tmag5273\_attribute](drivers_2sensor_2tmag5273_8h.md#a6fadcd6cd3b5fbc9281d27f37bdfe0a2)

tmag5273\_attribute

Additional attributes supported by the TMAG5273.

**Definition** tmag5273.h:37

[TMAG5273\_ATTR\_ANGLE\_MAG\_AXIS](drivers_2sensor_2tmag5273_8h.md#a6fadcd6cd3b5fbc9281d27f37bdfe0a2af59c66f9794efa1afa7d7461a134d3d3)

@ TMAG5273\_ATTR\_ANGLE\_MAG\_AXIS

Define axis relation measurements.

**Definition** tmag5273.h:48

[SENSOR\_ATTR\_PRIV\_START](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940bafb4b5859bc369f817f60eaa161bcefc3)

@ SENSOR\_ATTR\_PRIV\_START

This and higher values are sensor specific.

**Definition** sensor.h:359

[SENSOR\_CHAN\_PRIV\_START](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934ac1f260296289d93a13c5686ca11bdc12)

@ SENSOR\_CHAN\_PRIV\_START

This and higher values are sensor specific.

**Definition** sensor.h:208

[sensor.h](sensor_8h.md)

Public APIs for the sensor driver.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [sensor](dir_b6423b3a8fc1c9278ff19cba182cfe6d.md)
- [tmag5273.h](drivers_2sensor_2tmag5273_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
