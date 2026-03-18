---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/qdec__mcux_8h_source.html
original_path: doxygen/html/qdec__mcux_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

qdec\_mcux.h

[Go to the documentation of this file.](qdec__mcux_8h.md)

1/\*

2 \* Copyright (c) 2022, Prevas A/S

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_SENSOR\_QDEC\_MCUX\_H\_

8#define ZEPHYR\_INCLUDE\_DRIVERS\_SENSOR\_QDEC\_MCUX\_H\_

9

10#include <[zephyr/drivers/sensor.h](sensor_8h.md)>

11

[ 12](qdec__mcux_8h.md#a93f4f84af3e5a42381e9152750c46286)enum [sensor\_attribute\_qdec\_mcux](qdec__mcux_8h.md#a93f4f84af3e5a42381e9152750c46286) {

13 /\* Number of counts per revolution \*/

[ 14](qdec__mcux_8h.md#a93f4f84af3e5a42381e9152750c46286adeea574ce5fbed87ca34dc26860428b2) [SENSOR\_ATTR\_QDEC\_MOD\_VAL](qdec__mcux_8h.md#a93f4f84af3e5a42381e9152750c46286adeea574ce5fbed87ca34dc26860428b2) = [SENSOR\_ATTR\_PRIV\_START](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940bafb4b5859bc369f817f60eaa161bcefc3),

15 /\* Single phase counting \*/

[ 16](qdec__mcux_8h.md#a93f4f84af3e5a42381e9152750c46286afac8fcee81dcca4ce5f5717b09a18cb4) [SENSOR\_ATTR\_QDEC\_ENABLE\_SINGLE\_PHASE](qdec__mcux_8h.md#a93f4f84af3e5a42381e9152750c46286afac8fcee81dcca4ce5f5717b09a18cb4),

17};

18

19#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_SENSOR\_QDEC\_MCUX\_H\_ \*/

[SENSOR\_ATTR\_PRIV\_START](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940bafb4b5859bc369f817f60eaa161bcefc3)

@ SENSOR\_ATTR\_PRIV\_START

This and higher values are sensor specific.

**Definition** sensor.h:356

[sensor\_attribute\_qdec\_mcux](qdec__mcux_8h.md#a93f4f84af3e5a42381e9152750c46286)

sensor\_attribute\_qdec\_mcux

**Definition** qdec\_mcux.h:12

[SENSOR\_ATTR\_QDEC\_MOD\_VAL](qdec__mcux_8h.md#a93f4f84af3e5a42381e9152750c46286adeea574ce5fbed87ca34dc26860428b2)

@ SENSOR\_ATTR\_QDEC\_MOD\_VAL

**Definition** qdec\_mcux.h:14

[SENSOR\_ATTR\_QDEC\_ENABLE\_SINGLE\_PHASE](qdec__mcux_8h.md#a93f4f84af3e5a42381e9152750c46286afac8fcee81dcca4ce5f5717b09a18cb4)

@ SENSOR\_ATTR\_QDEC\_ENABLE\_SINGLE\_PHASE

**Definition** qdec\_mcux.h:16

[sensor.h](sensor_8h.md)

Public APIs for the sensor driver.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [sensor](dir_b6423b3a8fc1c9278ff19cba182cfe6d.md)
- [qdec\_mcux.h](qdec__mcux_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
