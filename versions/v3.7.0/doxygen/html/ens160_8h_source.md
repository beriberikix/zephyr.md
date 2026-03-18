---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/ens160_8h_source.html
original_path: doxygen/html/ens160_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ens160.h

[Go to the documentation of this file.](ens160_8h.md)

1/\*

2 \* Copyright (c) 2024 Gustavo Silva

3 \* SPDX-License-Identifier: Apache-2.0

4 \*/

5

6#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_SENSOR\_ENS160\_H\_

7#define ZEPHYR\_INCLUDE\_DRIVERS\_SENSOR\_ENS160\_H\_

8

9#ifdef \_\_cplusplus

10extern "C" {

11#endif

12

13#include <[zephyr/drivers/sensor.h](sensor_8h.md)>

14

15/\* Channel for Air Quality Index \*/

[ 16](ens160_8h.md#a8d2ba05aa65d222313abb94ea4fbc0a5)enum [sensor\_channel\_ens160](ens160_8h.md#a8d2ba05aa65d222313abb94ea4fbc0a5) {

[ 17](ens160_8h.md#a8d2ba05aa65d222313abb94ea4fbc0a5ac57da55fa36fe09123bba287ea6fef56) [SENSOR\_CHAN\_ENS160\_AQI](ens160_8h.md#a8d2ba05aa65d222313abb94ea4fbc0a5ac57da55fa36fe09123bba287ea6fef56) = [SENSOR\_CHAN\_PRIV\_START](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934ac1f260296289d93a13c5686ca11bdc12),

18};

19

[ 20](ens160_8h.md#a8005c12c1132ce8b76bd571035a37836)enum [sensor\_attribute\_ens160](ens160_8h.md#a8005c12c1132ce8b76bd571035a37836) {

[ 21](ens160_8h.md#a8005c12c1132ce8b76bd571035a37836a09b24e7aae253d6e4ee71fd57e0347be) [SENSOR\_ATTR\_ENS160\_TEMP](ens160_8h.md#a8005c12c1132ce8b76bd571035a37836a09b24e7aae253d6e4ee71fd57e0347be) = [SENSOR\_ATTR\_PRIV\_START](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940bafb4b5859bc369f817f60eaa161bcefc3),

[ 22](ens160_8h.md#a8005c12c1132ce8b76bd571035a37836a23a397dcaad8efe37bc66aa54bfd3608) [SENSOR\_ATTR\_ENS160\_RH](ens160_8h.md#a8005c12c1132ce8b76bd571035a37836a23a397dcaad8efe37bc66aa54bfd3608),

23};

24

25#ifdef \_\_cplusplus

26}

27#endif

28

29#endif

[sensor\_attribute\_ens160](ens160_8h.md#a8005c12c1132ce8b76bd571035a37836)

sensor\_attribute\_ens160

**Definition** ens160.h:20

[SENSOR\_ATTR\_ENS160\_TEMP](ens160_8h.md#a8005c12c1132ce8b76bd571035a37836a09b24e7aae253d6e4ee71fd57e0347be)

@ SENSOR\_ATTR\_ENS160\_TEMP

**Definition** ens160.h:21

[SENSOR\_ATTR\_ENS160\_RH](ens160_8h.md#a8005c12c1132ce8b76bd571035a37836a23a397dcaad8efe37bc66aa54bfd3608)

@ SENSOR\_ATTR\_ENS160\_RH

**Definition** ens160.h:22

[sensor\_channel\_ens160](ens160_8h.md#a8d2ba05aa65d222313abb94ea4fbc0a5)

sensor\_channel\_ens160

**Definition** ens160.h:16

[SENSOR\_CHAN\_ENS160\_AQI](ens160_8h.md#a8d2ba05aa65d222313abb94ea4fbc0a5ac57da55fa36fe09123bba287ea6fef56)

@ SENSOR\_CHAN\_ENS160\_AQI

**Definition** ens160.h:17

[SENSOR\_ATTR\_PRIV\_START](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940bafb4b5859bc369f817f60eaa161bcefc3)

@ SENSOR\_ATTR\_PRIV\_START

This and higher values are sensor specific.

**Definition** sensor.h:356

[SENSOR\_CHAN\_PRIV\_START](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934ac1f260296289d93a13c5686ca11bdc12)

@ SENSOR\_CHAN\_PRIV\_START

This and higher values are sensor specific.

**Definition** sensor.h:208

[sensor.h](sensor_8h.md)

Public APIs for the sensor driver.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [sensor](dir_b6423b3a8fc1c9278ff19cba182cfe6d.md)
- [ens160.h](ens160_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
