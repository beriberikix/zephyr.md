---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/npm13xx__charger_8h_source.html
original_path: doxygen/html/npm13xx__charger_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

npm13xx\_charger.h

[Go to the documentation of this file.](npm13xx__charger_8h.md)

1/\*

2 \* Copyright (c) 2023 Nordic Semiconductor ASA

3 \* SPDX-License-Identifier: Apache-2.0

4 \*/

5

6#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_SENSOR\_NPM13XX\_CHARGER\_H\_

7#define ZEPHYR\_INCLUDE\_DRIVERS\_SENSOR\_NPM13XX\_CHARGER\_H\_

8

9#include <[zephyr/drivers/sensor.h](sensor_8h.md)>

10

11/\* NPM13XX charger specific channels \*/

[ 12](npm13xx__charger_8h.md#a3b5c9edfeb25c77685d67babdc4c5299)enum [sensor\_channel\_npm13xx\_charger](npm13xx__charger_8h.md#a3b5c9edfeb25c77685d67babdc4c5299) {

[ 13](npm13xx__charger_8h.md#a3b5c9edfeb25c77685d67babdc4c5299abb7d0a263602d5a4e7fddf5b7fa44946) [SENSOR\_CHAN\_NPM13XX\_CHARGER\_STATUS](npm13xx__charger_8h.md#a3b5c9edfeb25c77685d67babdc4c5299abb7d0a263602d5a4e7fddf5b7fa44946) = [SENSOR\_CHAN\_PRIV\_START](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934ac1f260296289d93a13c5686ca11bdc12),

[ 14](npm13xx__charger_8h.md#a3b5c9edfeb25c77685d67babdc4c5299a68daf03ea54b12dba3bd2cac5d5f142b) [SENSOR\_CHAN\_NPM13XX\_CHARGER\_ERROR](npm13xx__charger_8h.md#a3b5c9edfeb25c77685d67babdc4c5299a68daf03ea54b12dba3bd2cac5d5f142b),

[ 15](npm13xx__charger_8h.md#a3b5c9edfeb25c77685d67babdc4c5299aa070958a66af182e1db9c49a6a41c8c2) [SENSOR\_CHAN\_NPM13XX\_CHARGER\_VBUS\_STATUS](npm13xx__charger_8h.md#a3b5c9edfeb25c77685d67babdc4c5299aa070958a66af182e1db9c49a6a41c8c2),

16};

17

18/\* NPM13XX charger specific attributes \*/

[ 19](npm13xx__charger_8h.md#add553da0fb80ee2cfb6a5b009a1d6058)enum [sensor\_attribute\_npm13xx\_charger](npm13xx__charger_8h.md#add553da0fb80ee2cfb6a5b009a1d6058) {

[ 20](npm13xx__charger_8h.md#add553da0fb80ee2cfb6a5b009a1d6058ac65dd6d01c5995c1f0514daaded1c283) [SENSOR\_ATTR\_NPM13XX\_CHARGER\_VBUS\_PRESENT](npm13xx__charger_8h.md#add553da0fb80ee2cfb6a5b009a1d6058ac65dd6d01c5995c1f0514daaded1c283) = [SENSOR\_ATTR\_PRIV\_START](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940bafb4b5859bc369f817f60eaa161bcefc3),

[ 21](npm13xx__charger_8h.md#add553da0fb80ee2cfb6a5b009a1d6058a3faad43b78763a2520e9a87baf38265b) [SENSOR\_ATTR\_NPM13XX\_CHARGER\_VBUS\_CUR\_LIMIT](npm13xx__charger_8h.md#add553da0fb80ee2cfb6a5b009a1d6058a3faad43b78763a2520e9a87baf38265b),

[ 22](npm13xx__charger_8h.md#add553da0fb80ee2cfb6a5b009a1d6058a5674d4ecc2377640a42fc78fef60c0ab) [SENSOR\_ATTR\_NPM13XX\_CHARGER\_VBUS\_OVERVLT\_PROT](npm13xx__charger_8h.md#add553da0fb80ee2cfb6a5b009a1d6058a5674d4ecc2377640a42fc78fef60c0ab),

[ 23](npm13xx__charger_8h.md#add553da0fb80ee2cfb6a5b009a1d6058addc2f6fbe32fd3bdadeb6c5d3aa00a08) [SENSOR\_ATTR\_NPM13XX\_CHARGER\_VBUS\_UNDERVLT](npm13xx__charger_8h.md#add553da0fb80ee2cfb6a5b009a1d6058addc2f6fbe32fd3bdadeb6c5d3aa00a08),

[ 24](npm13xx__charger_8h.md#add553da0fb80ee2cfb6a5b009a1d6058a7e1153a7eeb8e02925d0ee57c79b8a31) [SENSOR\_ATTR\_NPM13XX\_CHARGER\_VBUS\_SUSPENDED](npm13xx__charger_8h.md#add553da0fb80ee2cfb6a5b009a1d6058a7e1153a7eeb8e02925d0ee57c79b8a31),

[ 25](npm13xx__charger_8h.md#add553da0fb80ee2cfb6a5b009a1d6058abb429313846ec7adbf09d84b5385e2bc) [SENSOR\_ATTR\_NPM13XX\_CHARGER\_VBUS\_BUSOUT](npm13xx__charger_8h.md#add553da0fb80ee2cfb6a5b009a1d6058abb429313846ec7adbf09d84b5385e2bc),

26};

27

28#endif

[SENSOR\_ATTR\_PRIV\_START](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940bafb4b5859bc369f817f60eaa161bcefc3)

@ SENSOR\_ATTR\_PRIV\_START

This and higher values are sensor specific.

**Definition** sensor.h:372

[SENSOR\_CHAN\_PRIV\_START](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934ac1f260296289d93a13c5686ca11bdc12)

@ SENSOR\_CHAN\_PRIV\_START

This and higher values are sensor specific.

**Definition** sensor.h:217

[sensor\_channel\_npm13xx\_charger](npm13xx__charger_8h.md#a3b5c9edfeb25c77685d67babdc4c5299)

sensor\_channel\_npm13xx\_charger

**Definition** npm13xx\_charger.h:12

[SENSOR\_CHAN\_NPM13XX\_CHARGER\_ERROR](npm13xx__charger_8h.md#a3b5c9edfeb25c77685d67babdc4c5299a68daf03ea54b12dba3bd2cac5d5f142b)

@ SENSOR\_CHAN\_NPM13XX\_CHARGER\_ERROR

**Definition** npm13xx\_charger.h:14

[SENSOR\_CHAN\_NPM13XX\_CHARGER\_VBUS\_STATUS](npm13xx__charger_8h.md#a3b5c9edfeb25c77685d67babdc4c5299aa070958a66af182e1db9c49a6a41c8c2)

@ SENSOR\_CHAN\_NPM13XX\_CHARGER\_VBUS\_STATUS

**Definition** npm13xx\_charger.h:15

[SENSOR\_CHAN\_NPM13XX\_CHARGER\_STATUS](npm13xx__charger_8h.md#a3b5c9edfeb25c77685d67babdc4c5299abb7d0a263602d5a4e7fddf5b7fa44946)

@ SENSOR\_CHAN\_NPM13XX\_CHARGER\_STATUS

**Definition** npm13xx\_charger.h:13

[sensor\_attribute\_npm13xx\_charger](npm13xx__charger_8h.md#add553da0fb80ee2cfb6a5b009a1d6058)

sensor\_attribute\_npm13xx\_charger

**Definition** npm13xx\_charger.h:19

[SENSOR\_ATTR\_NPM13XX\_CHARGER\_VBUS\_CUR\_LIMIT](npm13xx__charger_8h.md#add553da0fb80ee2cfb6a5b009a1d6058a3faad43b78763a2520e9a87baf38265b)

@ SENSOR\_ATTR\_NPM13XX\_CHARGER\_VBUS\_CUR\_LIMIT

**Definition** npm13xx\_charger.h:21

[SENSOR\_ATTR\_NPM13XX\_CHARGER\_VBUS\_OVERVLT\_PROT](npm13xx__charger_8h.md#add553da0fb80ee2cfb6a5b009a1d6058a5674d4ecc2377640a42fc78fef60c0ab)

@ SENSOR\_ATTR\_NPM13XX\_CHARGER\_VBUS\_OVERVLT\_PROT

**Definition** npm13xx\_charger.h:22

[SENSOR\_ATTR\_NPM13XX\_CHARGER\_VBUS\_SUSPENDED](npm13xx__charger_8h.md#add553da0fb80ee2cfb6a5b009a1d6058a7e1153a7eeb8e02925d0ee57c79b8a31)

@ SENSOR\_ATTR\_NPM13XX\_CHARGER\_VBUS\_SUSPENDED

**Definition** npm13xx\_charger.h:24

[SENSOR\_ATTR\_NPM13XX\_CHARGER\_VBUS\_BUSOUT](npm13xx__charger_8h.md#add553da0fb80ee2cfb6a5b009a1d6058abb429313846ec7adbf09d84b5385e2bc)

@ SENSOR\_ATTR\_NPM13XX\_CHARGER\_VBUS\_BUSOUT

**Definition** npm13xx\_charger.h:25

[SENSOR\_ATTR\_NPM13XX\_CHARGER\_VBUS\_PRESENT](npm13xx__charger_8h.md#add553da0fb80ee2cfb6a5b009a1d6058ac65dd6d01c5995c1f0514daaded1c283)

@ SENSOR\_ATTR\_NPM13XX\_CHARGER\_VBUS\_PRESENT

**Definition** npm13xx\_charger.h:20

[SENSOR\_ATTR\_NPM13XX\_CHARGER\_VBUS\_UNDERVLT](npm13xx__charger_8h.md#add553da0fb80ee2cfb6a5b009a1d6058addc2f6fbe32fd3bdadeb6c5d3aa00a08)

@ SENSOR\_ATTR\_NPM13XX\_CHARGER\_VBUS\_UNDERVLT

**Definition** npm13xx\_charger.h:23

[sensor.h](sensor_8h.md)

Public APIs for the sensor driver.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [sensor](dir_b6423b3a8fc1c9278ff19cba182cfe6d.md)
- [npm13xx\_charger.h](npm13xx__charger_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
