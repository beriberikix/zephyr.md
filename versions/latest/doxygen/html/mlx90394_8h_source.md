---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/mlx90394_8h_source.html
original_path: doxygen/html/mlx90394_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mlx90394.h

[Go to the documentation of this file.](mlx90394_8h.md)

1/\*

2 \* Copyright (c) 2024 Florian Weber <Florian.Weber@live.de>

3 \* SPDX-License-Identifier: Apache-2.0

4 \*/

5

13

14#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_SENSOR\_MLX90394\_H\_

15#define ZEPHYR\_INCLUDE\_DRIVERS\_SENSOR\_MLX90394\_H\_

16

17#ifdef \_\_cplusplus

18extern "C" {

19#endif

20

21#include <[zephyr/drivers/sensor.h](sensor_8h.md)>

22

[ 23](mlx90394_8h.md#ad3f71775143081e44d323e3886617e3f)enum [mlx90394\_sensor\_attribute](mlx90394_8h.md#ad3f71775143081e44d323e3886617e3f) {

[ 24](mlx90394_8h.md#ad3f71775143081e44d323e3886617e3fa8d57f0f77e31edd3d9d1c3610f31ee93) [MLX90394\_SENSOR\_ATTR\_MAGN\_LOW\_NOISE](mlx90394_8h.md#ad3f71775143081e44d323e3886617e3fa8d57f0f77e31edd3d9d1c3610f31ee93) = [SENSOR\_ATTR\_PRIV\_START](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940bafb4b5859bc369f817f60eaa161bcefc3),

[ 25](mlx90394_8h.md#ad3f71775143081e44d323e3886617e3fa9b0e8eab5d12fa2bd32114d6453f1908) [MLX90394\_SENSOR\_ATTR\_MAGN\_FILTER\_XY](mlx90394_8h.md#ad3f71775143081e44d323e3886617e3fa9b0e8eab5d12fa2bd32114d6453f1908),

[ 26](mlx90394_8h.md#ad3f71775143081e44d323e3886617e3faa3f86f83470b4936876aa0b42a881228) [MLX90394\_SENSOR\_ATTR\_MAGN\_FILTER\_Z](mlx90394_8h.md#ad3f71775143081e44d323e3886617e3faa3f86f83470b4936876aa0b42a881228),

[ 27](mlx90394_8h.md#ad3f71775143081e44d323e3886617e3fa7c6e652d6f49f5aa6c4f7a56cb7427f0) [MLX90394\_SENSOR\_ATTR\_MAGN\_OSR](mlx90394_8h.md#ad3f71775143081e44d323e3886617e3fa7c6e652d6f49f5aa6c4f7a56cb7427f0),

[ 28](mlx90394_8h.md#ad3f71775143081e44d323e3886617e3fa4a594a201de0d6a147697f57797efa27) [MLX90394\_SENSOR\_ATTR\_TEMP\_FILTER](mlx90394_8h.md#ad3f71775143081e44d323e3886617e3fa4a594a201de0d6a147697f57797efa27),

[ 29](mlx90394_8h.md#ad3f71775143081e44d323e3886617e3fafcf90d5b6495cc754307a0b021b5cd0b) [MLX90394\_SENSOR\_ATTR\_TEMP\_OSR](mlx90394_8h.md#ad3f71775143081e44d323e3886617e3fafcf90d5b6495cc754307a0b021b5cd0b)

30};

31

32#ifdef \_\_cplusplus

33}

34#endif

35

36#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_SENSOR\_MLX90394\_H\_ \*/

[SENSOR\_ATTR\_PRIV\_START](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940bafb4b5859bc369f817f60eaa161bcefc3)

@ SENSOR\_ATTR\_PRIV\_START

This and higher values are sensor specific.

**Definition** sensor.h:368

[mlx90394\_sensor\_attribute](mlx90394_8h.md#ad3f71775143081e44d323e3886617e3f)

mlx90394\_sensor\_attribute

**Definition** mlx90394.h:23

[MLX90394\_SENSOR\_ATTR\_TEMP\_FILTER](mlx90394_8h.md#ad3f71775143081e44d323e3886617e3fa4a594a201de0d6a147697f57797efa27)

@ MLX90394\_SENSOR\_ATTR\_TEMP\_FILTER

**Definition** mlx90394.h:28

[MLX90394\_SENSOR\_ATTR\_MAGN\_OSR](mlx90394_8h.md#ad3f71775143081e44d323e3886617e3fa7c6e652d6f49f5aa6c4f7a56cb7427f0)

@ MLX90394\_SENSOR\_ATTR\_MAGN\_OSR

**Definition** mlx90394.h:27

[MLX90394\_SENSOR\_ATTR\_MAGN\_LOW\_NOISE](mlx90394_8h.md#ad3f71775143081e44d323e3886617e3fa8d57f0f77e31edd3d9d1c3610f31ee93)

@ MLX90394\_SENSOR\_ATTR\_MAGN\_LOW\_NOISE

**Definition** mlx90394.h:24

[MLX90394\_SENSOR\_ATTR\_MAGN\_FILTER\_XY](mlx90394_8h.md#ad3f71775143081e44d323e3886617e3fa9b0e8eab5d12fa2bd32114d6453f1908)

@ MLX90394\_SENSOR\_ATTR\_MAGN\_FILTER\_XY

**Definition** mlx90394.h:25

[MLX90394\_SENSOR\_ATTR\_MAGN\_FILTER\_Z](mlx90394_8h.md#ad3f71775143081e44d323e3886617e3faa3f86f83470b4936876aa0b42a881228)

@ MLX90394\_SENSOR\_ATTR\_MAGN\_FILTER\_Z

**Definition** mlx90394.h:26

[MLX90394\_SENSOR\_ATTR\_TEMP\_OSR](mlx90394_8h.md#ad3f71775143081e44d323e3886617e3fafcf90d5b6495cc754307a0b021b5cd0b)

@ MLX90394\_SENSOR\_ATTR\_TEMP\_OSR

**Definition** mlx90394.h:29

[sensor.h](sensor_8h.md)

Public APIs for the sensor driver.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [sensor](dir_b6423b3a8fc1c9278ff19cba182cfe6d.md)
- [mlx90394.h](mlx90394_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
