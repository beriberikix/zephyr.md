---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/pat9136_8h_source.html
original_path: doxygen/html/pat9136_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

pat9136.h

[Go to the documentation of this file.](pat9136_8h.md)

1/\*

2 \* Copyright (c) 2025 Croxel Inc.

3 \* Copyright (c) 2025 CogniPilot Foundation

4 \*

5 \* SPDX-License-Identifier: Apache-2.0

6 \*/

7

8#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_SENSOR\_PAT9136\_H\_

9#define ZEPHYR\_INCLUDE\_DRIVERS\_SENSOR\_PAT9136\_H\_

10

11#include <[zephyr/drivers/sensor.h](sensor_8h.md)>

12

13#ifdef \_\_cplusplus

14extern "C" {

15#endif

16

[ 22](pat9136_8h.md#a6e9d013c0dc687f05c27dc907bb56c65)enum [sensor\_channel\_pat9136](pat9136_8h.md#a6e9d013c0dc687f05c27dc907bb56c65) {

[ 24](pat9136_8h.md#a6e9d013c0dc687f05c27dc907bb56c65a9ba6c90758d4c7565e0aa785da00c953) [SENSOR\_CHAN\_POS\_DX\_MM](pat9136_8h.md#a6e9d013c0dc687f05c27dc907bb56c65a9ba6c90758d4c7565e0aa785da00c953) = [SENSOR\_CHAN\_PRIV\_START](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934ac1f260296289d93a13c5686ca11bdc12) + 1,

[ 26](pat9136_8h.md#a6e9d013c0dc687f05c27dc907bb56c65a12172a3b5c7d79da0f5ee8305c7837ba) [SENSOR\_CHAN\_POS\_DY\_MM](pat9136_8h.md#a6e9d013c0dc687f05c27dc907bb56c65a12172a3b5c7d79da0f5ee8305c7837ba),

[ 31](pat9136_8h.md#a6e9d013c0dc687f05c27dc907bb56c65aa0b2726e0262199b579c5bb66d542e70) [SENSOR\_CHAN\_POS\_DXYZ\_MM](pat9136_8h.md#a6e9d013c0dc687f05c27dc907bb56c65aa0b2726e0262199b579c5bb66d542e70) = [SENSOR\_CHAN\_POS\_DY\_MM](pat9136_8h.md#a6e9d013c0dc687f05c27dc907bb56c65a12172a3b5c7d79da0f5ee8305c7837ba) + 2,

32};

33

34#ifdef \_\_cplusplus

35}

36#endif

37

38#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_SENSOR\_PAT9136\_H\_ \*/

[SENSOR\_CHAN\_PRIV\_START](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934ac1f260296289d93a13c5686ca11bdc12)

@ SENSOR\_CHAN\_PRIV\_START

This and higher values are sensor specific.

**Definition** sensor.h:217

[sensor\_channel\_pat9136](pat9136_8h.md#a6e9d013c0dc687f05c27dc907bb56c65)

sensor\_channel\_pat9136

This sensor does have the ability to provide DXY in meaningful units, and since the standard channels...

**Definition** pat9136.h:22

[SENSOR\_CHAN\_POS\_DY\_MM](pat9136_8h.md#a6e9d013c0dc687f05c27dc907bb56c65a12172a3b5c7d79da0f5ee8305c7837ba)

@ SENSOR\_CHAN\_POS\_DY\_MM

Position change on the Y axis, in millimeters.

**Definition** pat9136.h:26

[SENSOR\_CHAN\_POS\_DX\_MM](pat9136_8h.md#a6e9d013c0dc687f05c27dc907bb56c65a9ba6c90758d4c7565e0aa785da00c953)

@ SENSOR\_CHAN\_POS\_DX\_MM

Position change on the X axis, in millimeters.

**Definition** pat9136.h:24

[SENSOR\_CHAN\_POS\_DXYZ\_MM](pat9136_8h.md#a6e9d013c0dc687f05c27dc907bb56c65aa0b2726e0262199b579c5bb66d542e70)

@ SENSOR\_CHAN\_POS\_DXYZ\_MM

Position change on the X, Y and Z axis, in millimeters.

**Definition** pat9136.h:31

[sensor.h](sensor_8h.md)

Public APIs for the sensor driver.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [sensor](dir_b6423b3a8fc1c9278ff19cba182cfe6d.md)
- [pat9136.h](pat9136_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
