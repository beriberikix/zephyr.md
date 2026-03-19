---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/tsl2540_8h_source.html
original_path: doxygen/html/tsl2540_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

tsl2540.h

[Go to the documentation of this file.](tsl2540_8h.md)

1/\*

2 \* Copyright (c) 2022 T-Mobile USA, Inc.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

14

15#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_SENSOR\_TSL2540\_H\_

16#define ZEPHYR\_INCLUDE\_DRIVERS\_SENSOR\_TSL2540\_H\_

17

18#include <[zephyr/drivers/sensor.h](sensor_8h.md)>

19

20#ifdef \_\_cplusplus

21extern "C" {

22#endif

23

[ 24](tsl2540_8h.md#a9883d80dadfb4ea2b3362579f16ff2a7)enum [sensor\_attribute\_tsl2540](tsl2540_8h.md#a9883d80dadfb4ea2b3362579f16ff2a7) {

25 /\* Sensor Integration Time (in ms) \*/

[ 26](tsl2540_8h.md#a9883d80dadfb4ea2b3362579f16ff2a7aeba46c663afa61df6d07ce3f90f2ec59) [SENSOR\_ATTR\_INTEGRATION\_TIME](tsl2540_8h.md#a9883d80dadfb4ea2b3362579f16ff2a7aeba46c663afa61df6d07ce3f90f2ec59) = [SENSOR\_ATTR\_PRIV\_START](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940bafb4b5859bc369f817f60eaa161bcefc3) + 1,

27 /\* Sensor ALS interrupt persistence filters \*/

[ 28](tsl2540_8h.md#a9883d80dadfb4ea2b3362579f16ff2a7aa54ec0288bcccb2b2e6421f4b72f79f3) [SENSOR\_ATTR\_INT\_APERS](tsl2540_8h.md#a9883d80dadfb4ea2b3362579f16ff2a7aa54ec0288bcccb2b2e6421f4b72f79f3),

29 /\* Shutdown the sensor \*/

[ 30](tsl2540_8h.md#a9883d80dadfb4ea2b3362579f16ff2a7af93ed8b682d02741d4a0c3a30c43c54b) [SENSOR\_ATTR\_TSL2540\_SHUTDOWN\_MODE](tsl2540_8h.md#a9883d80dadfb4ea2b3362579f16ff2a7af93ed8b682d02741d4a0c3a30c43c54b),

31 /\* Turn on continuous conversion \*/

[ 32](tsl2540_8h.md#a9883d80dadfb4ea2b3362579f16ff2a7acd384fa1b346065f061d48ac5acfa5c5) [SENSOR\_ATTR\_TSL2540\_CONTINUOUS\_MODE](tsl2540_8h.md#a9883d80dadfb4ea2b3362579f16ff2a7acd384fa1b346065f061d48ac5acfa5c5),

33 /\* Turn on continuous conversion without wait \*/

[ 34](tsl2540_8h.md#a9883d80dadfb4ea2b3362579f16ff2a7af1d695bedc5680aa3ed3194442419cac) [SENSOR\_ATTR\_TSL2540\_CONTINUOUS\_NO\_WAIT\_MODE](tsl2540_8h.md#a9883d80dadfb4ea2b3362579f16ff2a7af1d695bedc5680aa3ed3194442419cac),

35};

36

[ 37](tsl2540_8h.md#af3d41ccc17abc24a7d10d950f19f45e9)enum [sensor\_gain\_tsl2540](tsl2540_8h.md#af3d41ccc17abc24a7d10d950f19f45e9) {

[ 38](tsl2540_8h.md#af3d41ccc17abc24a7d10d950f19f45e9a2f573c66b903ebce339e0fb55bbc7ce1) [TSL2540\_SENSOR\_GAIN\_1\_2](tsl2540_8h.md#af3d41ccc17abc24a7d10d950f19f45e9a2f573c66b903ebce339e0fb55bbc7ce1),

[ 39](tsl2540_8h.md#af3d41ccc17abc24a7d10d950f19f45e9a2885634c5618ccb0c90389951cf394cb) [TSL2540\_SENSOR\_GAIN\_1](tsl2540_8h.md#af3d41ccc17abc24a7d10d950f19f45e9a2885634c5618ccb0c90389951cf394cb),

[ 40](tsl2540_8h.md#af3d41ccc17abc24a7d10d950f19f45e9a4bda1e9f1384f0ef751ee8f9a0061d42) [TSL2540\_SENSOR\_GAIN\_4](tsl2540_8h.md#af3d41ccc17abc24a7d10d950f19f45e9a4bda1e9f1384f0ef751ee8f9a0061d42),

[ 41](tsl2540_8h.md#af3d41ccc17abc24a7d10d950f19f45e9ab874914e285c574ac4cfe9c358d9c66e) [TSL2540\_SENSOR\_GAIN\_16](tsl2540_8h.md#af3d41ccc17abc24a7d10d950f19f45e9ab874914e285c574ac4cfe9c358d9c66e),

[ 42](tsl2540_8h.md#af3d41ccc17abc24a7d10d950f19f45e9a459c02cbca3e4109695fe646d128fc7f) [TSL2540\_SENSOR\_GAIN\_64](tsl2540_8h.md#af3d41ccc17abc24a7d10d950f19f45e9a459c02cbca3e4109695fe646d128fc7f),

[ 43](tsl2540_8h.md#af3d41ccc17abc24a7d10d950f19f45e9aee855aff34d1544549bc554faccfa948) [TSL2540\_SENSOR\_GAIN\_128](tsl2540_8h.md#af3d41ccc17abc24a7d10d950f19f45e9aee855aff34d1544549bc554faccfa948),

44};

45

46#ifdef \_\_cplusplus

47}

48#endif

49

50#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_SENSOR\_TSL2540\_H\_ \*/

[SENSOR\_ATTR\_PRIV\_START](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940bafb4b5859bc369f817f60eaa161bcefc3)

@ SENSOR\_ATTR\_PRIV\_START

This and higher values are sensor specific.

**Definition** sensor.h:359

[sensor.h](sensor_8h.md)

Public APIs for the sensor driver.

[sensor\_attribute\_tsl2540](tsl2540_8h.md#a9883d80dadfb4ea2b3362579f16ff2a7)

sensor\_attribute\_tsl2540

**Definition** tsl2540.h:24

[SENSOR\_ATTR\_INT\_APERS](tsl2540_8h.md#a9883d80dadfb4ea2b3362579f16ff2a7aa54ec0288bcccb2b2e6421f4b72f79f3)

@ SENSOR\_ATTR\_INT\_APERS

**Definition** tsl2540.h:28

[SENSOR\_ATTR\_TSL2540\_CONTINUOUS\_MODE](tsl2540_8h.md#a9883d80dadfb4ea2b3362579f16ff2a7acd384fa1b346065f061d48ac5acfa5c5)

@ SENSOR\_ATTR\_TSL2540\_CONTINUOUS\_MODE

**Definition** tsl2540.h:32

[SENSOR\_ATTR\_INTEGRATION\_TIME](tsl2540_8h.md#a9883d80dadfb4ea2b3362579f16ff2a7aeba46c663afa61df6d07ce3f90f2ec59)

@ SENSOR\_ATTR\_INTEGRATION\_TIME

**Definition** tsl2540.h:26

[SENSOR\_ATTR\_TSL2540\_CONTINUOUS\_NO\_WAIT\_MODE](tsl2540_8h.md#a9883d80dadfb4ea2b3362579f16ff2a7af1d695bedc5680aa3ed3194442419cac)

@ SENSOR\_ATTR\_TSL2540\_CONTINUOUS\_NO\_WAIT\_MODE

**Definition** tsl2540.h:34

[SENSOR\_ATTR\_TSL2540\_SHUTDOWN\_MODE](tsl2540_8h.md#a9883d80dadfb4ea2b3362579f16ff2a7af93ed8b682d02741d4a0c3a30c43c54b)

@ SENSOR\_ATTR\_TSL2540\_SHUTDOWN\_MODE

**Definition** tsl2540.h:30

[sensor\_gain\_tsl2540](tsl2540_8h.md#af3d41ccc17abc24a7d10d950f19f45e9)

sensor\_gain\_tsl2540

**Definition** tsl2540.h:37

[TSL2540\_SENSOR\_GAIN\_1](tsl2540_8h.md#af3d41ccc17abc24a7d10d950f19f45e9a2885634c5618ccb0c90389951cf394cb)

@ TSL2540\_SENSOR\_GAIN\_1

**Definition** tsl2540.h:39

[TSL2540\_SENSOR\_GAIN\_1\_2](tsl2540_8h.md#af3d41ccc17abc24a7d10d950f19f45e9a2f573c66b903ebce339e0fb55bbc7ce1)

@ TSL2540\_SENSOR\_GAIN\_1\_2

**Definition** tsl2540.h:38

[TSL2540\_SENSOR\_GAIN\_64](tsl2540_8h.md#af3d41ccc17abc24a7d10d950f19f45e9a459c02cbca3e4109695fe646d128fc7f)

@ TSL2540\_SENSOR\_GAIN\_64

**Definition** tsl2540.h:42

[TSL2540\_SENSOR\_GAIN\_4](tsl2540_8h.md#af3d41ccc17abc24a7d10d950f19f45e9a4bda1e9f1384f0ef751ee8f9a0061d42)

@ TSL2540\_SENSOR\_GAIN\_4

**Definition** tsl2540.h:40

[TSL2540\_SENSOR\_GAIN\_16](tsl2540_8h.md#af3d41ccc17abc24a7d10d950f19f45e9ab874914e285c574ac4cfe9c358d9c66e)

@ TSL2540\_SENSOR\_GAIN\_16

**Definition** tsl2540.h:41

[TSL2540\_SENSOR\_GAIN\_128](tsl2540_8h.md#af3d41ccc17abc24a7d10d950f19f45e9aee855aff34d1544549bc554faccfa948)

@ TSL2540\_SENSOR\_GAIN\_128

**Definition** tsl2540.h:43

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [sensor](dir_b6423b3a8fc1c9278ff19cba182cfe6d.md)
- [tsl2540.h](tsl2540_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
