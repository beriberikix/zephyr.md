---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/vl53l0x_8h_source.html
original_path: doxygen/html/vl53l0x_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

vl53l0x.h

[Go to the documentation of this file.](vl53l0x_8h.md)

1/\*

2 \* Copyright (c) 2024 Michal Piekos

3 \* SPDX-License-Identifier: Apache-2.0

4 \*/

5

23

24#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_SENSOR\_VL53L0X\_H\_

25#define ZEPHYR\_INCLUDE\_DRIVERS\_SENSOR\_VL53L0X\_H\_

26

27#include <[zephyr/drivers/sensor.h](sensor_8h.md)>

28

29/\* VL53L0x specific channels \*/

[ 30](vl53l0x_8h.md#aca3102e6b764e2a96732648325a93690)enum [sensor\_channel\_vl53l0x](vl53l0x_8h.md#aca3102e6b764e2a96732648325a93690) {

[ 31](vl53l0x_8h.md#aca3102e6b764e2a96732648325a93690adfefa5c75f3cfcceecb3dd8b8b6a9161) [SENSOR\_CHAN\_VL53L0X\_RANGE\_DMAX](vl53l0x_8h.md#aca3102e6b764e2a96732648325a93690adfefa5c75f3cfcceecb3dd8b8b6a9161) = [SENSOR\_CHAN\_PRIV\_START](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934ac1f260296289d93a13c5686ca11bdc12),

[ 32](vl53l0x_8h.md#aca3102e6b764e2a96732648325a93690a1d9c4833c2a652401636f0d8813d8172) [SENSOR\_CHAN\_VL53L0X\_SIGNAL\_RATE\_RTN\_CPS](vl53l0x_8h.md#aca3102e6b764e2a96732648325a93690a1d9c4833c2a652401636f0d8813d8172),

[ 33](vl53l0x_8h.md#aca3102e6b764e2a96732648325a93690afd56fa358ea21be22bf54565afbd6a0e) [SENSOR\_CHAN\_VL53L0X\_AMBIENT\_RATE\_RTN\_CPS](vl53l0x_8h.md#aca3102e6b764e2a96732648325a93690afd56fa358ea21be22bf54565afbd6a0e),

[ 34](vl53l0x_8h.md#aca3102e6b764e2a96732648325a93690a4a2dd2048c64daa0e80f15f39f008c19) [SENSOR\_CHAN\_VL53L0X\_EFFECTIVE\_SPAD\_RTN\_COUNT](vl53l0x_8h.md#aca3102e6b764e2a96732648325a93690a4a2dd2048c64daa0e80f15f39f008c19),

[ 35](vl53l0x_8h.md#aca3102e6b764e2a96732648325a93690a6463303c2528d76f165614d8cb79c75b) [SENSOR\_CHAN\_VL53L0X\_RANGE\_STATUS](vl53l0x_8h.md#aca3102e6b764e2a96732648325a93690a6463303c2528d76f165614d8cb79c75b),

36};

37

38/\* VL53L0x meas status values \*/

[ 39](vl53l0x_8h.md#ac0ba15e7b164d53a46f88eb3807d015d)#define VL53L0X\_RANGE\_STATUS\_RANGE\_VALID (0)

[ 40](vl53l0x_8h.md#a4b96413c5d9569b0f8037a4613b220a7)#define VL53L0X\_RANGE\_STATUS\_SIGMA\_FAIL (1)

[ 41](vl53l0x_8h.md#af7317fa7071929096d3413b60f620ea1)#define VL53L0X\_RANGE\_STATUS\_SIGNAL\_FAIL (2)

[ 42](vl53l0x_8h.md#a96dd67966d2d8b4d2eb16a5ac8b9724e)#define VL53L0X\_RANGE\_STATUS\_MIN\_RANGE\_FAIL (3)

[ 43](vl53l0x_8h.md#a4d4565e46665ca56a5143b1868aabbda)#define VL53L0X\_RANGE\_STATUS\_PHASE\_FAIL (4)

[ 44](vl53l0x_8h.md#a6c7cbe25fbf1603f37d53fb81bc606df)#define VL53L0X\_RANGE\_STATUS\_HARDWARE\_FAIL (5)

[ 45](vl53l0x_8h.md#a78056dcc0a8aa02321a4acf8c23bd5d1)#define VL53L0X\_RANGE\_STATUS\_NO\_UPDATE (255)

46

47#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_SENSOR\_VL53L0X\_H\_ \*/

[SENSOR\_CHAN\_PRIV\_START](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934ac1f260296289d93a13c5686ca11bdc12)

@ SENSOR\_CHAN\_PRIV\_START

This and higher values are sensor specific.

**Definition** sensor.h:217

[sensor.h](sensor_8h.md)

Public APIs for the sensor driver.

[sensor\_channel\_vl53l0x](vl53l0x_8h.md#aca3102e6b764e2a96732648325a93690)

sensor\_channel\_vl53l0x

**Definition** vl53l0x.h:30

[SENSOR\_CHAN\_VL53L0X\_SIGNAL\_RATE\_RTN\_CPS](vl53l0x_8h.md#aca3102e6b764e2a96732648325a93690a1d9c4833c2a652401636f0d8813d8172)

@ SENSOR\_CHAN\_VL53L0X\_SIGNAL\_RATE\_RTN\_CPS

**Definition** vl53l0x.h:32

[SENSOR\_CHAN\_VL53L0X\_EFFECTIVE\_SPAD\_RTN\_COUNT](vl53l0x_8h.md#aca3102e6b764e2a96732648325a93690a4a2dd2048c64daa0e80f15f39f008c19)

@ SENSOR\_CHAN\_VL53L0X\_EFFECTIVE\_SPAD\_RTN\_COUNT

**Definition** vl53l0x.h:34

[SENSOR\_CHAN\_VL53L0X\_RANGE\_STATUS](vl53l0x_8h.md#aca3102e6b764e2a96732648325a93690a6463303c2528d76f165614d8cb79c75b)

@ SENSOR\_CHAN\_VL53L0X\_RANGE\_STATUS

**Definition** vl53l0x.h:35

[SENSOR\_CHAN\_VL53L0X\_RANGE\_DMAX](vl53l0x_8h.md#aca3102e6b764e2a96732648325a93690adfefa5c75f3cfcceecb3dd8b8b6a9161)

@ SENSOR\_CHAN\_VL53L0X\_RANGE\_DMAX

**Definition** vl53l0x.h:31

[SENSOR\_CHAN\_VL53L0X\_AMBIENT\_RATE\_RTN\_CPS](vl53l0x_8h.md#aca3102e6b764e2a96732648325a93690afd56fa358ea21be22bf54565afbd6a0e)

@ SENSOR\_CHAN\_VL53L0X\_AMBIENT\_RATE\_RTN\_CPS

**Definition** vl53l0x.h:33

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [sensor](dir_b6423b3a8fc1c9278ff19cba182cfe6d.md)
- [vl53l0x.h](vl53l0x_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
