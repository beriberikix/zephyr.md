---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/drivers_2sensor_2icm42688_8h_source.html
original_path: doxygen/html/drivers_2sensor_2icm42688_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

icm42688.h

[Go to the documentation of this file.](drivers_2sensor_2icm42688_8h.md)

1/\*

2 \* Copyright The Zephyr Project Contributors

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_SENSOR\_ICM42688\_H\_

8#define ZEPHYR\_INCLUDE\_DRIVERS\_SENSOR\_ICM42688\_H\_

9

10#include <[zephyr/drivers/sensor.h](sensor_8h.md)>

11

18

[ 19](drivers_2sensor_2icm42688_8h.md#a3c5c9d8d18ea8c8aef23e6699149d28a)#define ICM42688\_PIN9\_FUNCTION\_INT2 0

[ 20](drivers_2sensor_2icm42688_8h.md#aae84cb7bf1ce1ceb097ed91e4a452be5)#define ICM42688\_PIN9\_FUNCTION\_FSYNC 1

[ 21](drivers_2sensor_2icm42688_8h.md#a68600f859f297e76e3b6b0f2c89ca089)#define ICM42688\_PIN9\_FUNCTION\_CLKIN 2

22

[ 28](drivers_2sensor_2icm42688_8h.md#a75e9a515047a6fb3ce41dbdf50fdf944)enum [sensor\_attribute\_icm42688](drivers_2sensor_2icm42688_8h.md#a75e9a515047a6fb3ce41dbdf50fdf944) {

[ 29](drivers_2sensor_2icm42688_8h.md#a75e9a515047a6fb3ce41dbdf50fdf944a080aef04033d9986025bc1964c5e6af4) [SENSOR\_ATTR\_ICM42688\_PIN9\_FUNCTION](drivers_2sensor_2icm42688_8h.md#a75e9a515047a6fb3ce41dbdf50fdf944a080aef04033d9986025bc1964c5e6af4) = [SENSOR\_ATTR\_PRIV\_START](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940bafb4b5859bc369f817f60eaa161bcefc3)

30};

31

32#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_SENSOR\_ICM42688\_H\_ \*/

[sensor\_attribute\_icm42688](drivers_2sensor_2icm42688_8h.md#a75e9a515047a6fb3ce41dbdf50fdf944)

sensor\_attribute\_icm42688

Extended sensor attributes for ICM42688.

**Definition** icm42688.h:28

[SENSOR\_ATTR\_ICM42688\_PIN9\_FUNCTION](drivers_2sensor_2icm42688_8h.md#a75e9a515047a6fb3ce41dbdf50fdf944a080aef04033d9986025bc1964c5e6af4)

@ SENSOR\_ATTR\_ICM42688\_PIN9\_FUNCTION

**Definition** icm42688.h:29

[SENSOR\_ATTR\_PRIV\_START](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940bafb4b5859bc369f817f60eaa161bcefc3)

@ SENSOR\_ATTR\_PRIV\_START

This and higher values are sensor specific.

**Definition** sensor.h:372

[sensor.h](sensor_8h.md)

Public APIs for the sensor driver.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [sensor](dir_b6423b3a8fc1c9278ff19cba182cfe6d.md)
- [icm42688.h](drivers_2sensor_2icm42688_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
