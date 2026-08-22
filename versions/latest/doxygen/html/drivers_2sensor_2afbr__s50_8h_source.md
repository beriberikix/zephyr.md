---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/drivers_2sensor_2afbr__s50_8h_source.html
original_path: doxygen/html/drivers_2sensor_2afbr__s50_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

afbr\_s50.h

[Go to the documentation of this file.](drivers_2sensor_2afbr__s50_8h.md)

1/\*

2 \* Copyright (c) 2025 Croxel Inc.

3 \* Copyright (c) 2025 CogniPilot Foundation

4 \*

5 \* SPDX-License-Identifier: Apache-2.0

6 \*/

7

8#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_SENSOR\_AFBR\_S50\_H\_

9#define ZEPHYR\_INCLUDE\_DRIVERS\_SENSOR\_AFBR\_S50\_H\_

10

11#include <[zephyr/drivers/sensor.h](sensor_8h.md)>

12

13#ifdef \_\_cplusplus

14extern "C" {

15#endif

16

[ 18](drivers_2sensor_2afbr__s50_8h.md#a026e02d538d6e283b7b1136470e6e478)#define AFBR\_PIXEL\_INVALID\_VALUE 0x80000000

19

[ 23](drivers_2sensor_2afbr__s50_8h.md#a2be1db0094a49e8e59310b8c8137e54f)enum [sensor\_channel\_afbr\_s50](drivers_2sensor_2afbr__s50_8h.md#a2be1db0094a49e8e59310b8c8137e54f) {

[ 24](drivers_2sensor_2afbr__s50_8h.md#a2be1db0094a49e8e59310b8c8137e54fa46394738feb65f3bcc76ecd343448de7) [SENSOR\_CHAN\_AFBR\_S50\_PIXELS](drivers_2sensor_2afbr__s50_8h.md#a2be1db0094a49e8e59310b8c8137e54fa46394738feb65f3bcc76ecd343448de7) = [SENSOR\_CHAN\_PRIV\_START](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934ac1f260296289d93a13c5686ca11bdc12) + 1,

25};

26

27#ifdef \_\_cplusplus

28}

29#endif

30

31#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_SENSOR\_AFBR\_S50\_H\_ \*/

[sensor\_channel\_afbr\_s50](drivers_2sensor_2afbr__s50_8h.md#a2be1db0094a49e8e59310b8c8137e54f)

sensor\_channel\_afbr\_s50

Private sensor channel to obtain matrix of pixels with readings in meters.

**Definition** afbr\_s50.h:23

[SENSOR\_CHAN\_AFBR\_S50\_PIXELS](drivers_2sensor_2afbr__s50_8h.md#a2be1db0094a49e8e59310b8c8137e54fa46394738feb65f3bcc76ecd343448de7)

@ SENSOR\_CHAN\_AFBR\_S50\_PIXELS

**Definition** afbr\_s50.h:24

[SENSOR\_CHAN\_PRIV\_START](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934ac1f260296289d93a13c5686ca11bdc12)

@ SENSOR\_CHAN\_PRIV\_START

This and higher values are sensor specific.

**Definition** sensor.h:217

[sensor.h](sensor_8h.md)

Public APIs for the sensor driver.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [sensor](dir_b6423b3a8fc1c9278ff19cba182cfe6d.md)
- [afbr\_s50.h](drivers_2sensor_2afbr__s50_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
