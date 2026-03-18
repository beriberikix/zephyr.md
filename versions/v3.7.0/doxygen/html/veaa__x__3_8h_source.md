---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/veaa__x__3_8h_source.html
original_path: doxygen/html/veaa__x__3_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

veaa\_x\_3.h

[Go to the documentation of this file.](veaa__x__3_8h.md)

1/\*

2 \* Copyright (c) 2024, Vitrolife A/S

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_SENSOR\_VEAA\_X\_3\_H\_

8#define ZEPHYR\_INCLUDE\_DRIVERS\_SENSOR\_VEAA\_X\_3\_H\_

9

10#ifdef \_\_cplusplus

11extern "C" {

12#endif

13

14#include <[zephyr/drivers/sensor.h](sensor_8h.md)>

15

[ 16](veaa__x__3_8h.md#a0766ed6ec5cca998f67ae8061ee9e862)enum [sensor\_attribute\_veaa\_x\_3](veaa__x__3_8h.md#a0766ed6ec5cca998f67ae8061ee9e862) {

17 /\* Set pressure setpoint value in kPa. \*/

[ 18](veaa__x__3_8h.md#a0766ed6ec5cca998f67ae8061ee9e862a9c7fbc183c05b73e5345677b8cd69bd3) [SENSOR\_ATTR\_VEAA\_X\_3\_SETPOINT](veaa__x__3_8h.md#a0766ed6ec5cca998f67ae8061ee9e862a9c7fbc183c05b73e5345677b8cd69bd3) = [SENSOR\_ATTR\_PRIV\_START](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940bafb4b5859bc369f817f60eaa161bcefc3),

19 /\* Supported pressure range in kPa. val1 is minimum and val2 is maximum \*/

[ 20](veaa__x__3_8h.md#a0766ed6ec5cca998f67ae8061ee9e862ae783f1639cec9875927dcc7157b292bc) [SENSOR\_ATTR\_VEAA\_X\_3\_RANGE](veaa__x__3_8h.md#a0766ed6ec5cca998f67ae8061ee9e862ae783f1639cec9875927dcc7157b292bc),

21};

22

23#ifdef \_\_cplusplus

24}

25#endif

26

27#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_SENSOR\_VEAA\_X\_3\_H\_ \*/

[SENSOR\_ATTR\_PRIV\_START](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940bafb4b5859bc369f817f60eaa161bcefc3)

@ SENSOR\_ATTR\_PRIV\_START

This and higher values are sensor specific.

**Definition** sensor.h:356

[sensor.h](sensor_8h.md)

Public APIs for the sensor driver.

[sensor\_attribute\_veaa\_x\_3](veaa__x__3_8h.md#a0766ed6ec5cca998f67ae8061ee9e862)

sensor\_attribute\_veaa\_x\_3

**Definition** veaa\_x\_3.h:16

[SENSOR\_ATTR\_VEAA\_X\_3\_SETPOINT](veaa__x__3_8h.md#a0766ed6ec5cca998f67ae8061ee9e862a9c7fbc183c05b73e5345677b8cd69bd3)

@ SENSOR\_ATTR\_VEAA\_X\_3\_SETPOINT

**Definition** veaa\_x\_3.h:18

[SENSOR\_ATTR\_VEAA\_X\_3\_RANGE](veaa__x__3_8h.md#a0766ed6ec5cca998f67ae8061ee9e862ae783f1639cec9875927dcc7157b292bc)

@ SENSOR\_ATTR\_VEAA\_X\_3\_RANGE

**Definition** veaa\_x\_3.h:20

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [sensor](dir_b6423b3a8fc1c9278ff19cba182cfe6d.md)
- [veaa\_x\_3.h](veaa__x__3_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
