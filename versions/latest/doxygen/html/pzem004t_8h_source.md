---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/pzem004t_8h_source.html
original_path: doxygen/html/pzem004t_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

pzem004t.h

[Go to the documentation of this file.](pzem004t_8h.md)

1/\*

2 \* Copyright (c) 2025 Srishtik Bhandarkar

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_SENSOR\_PZEM004T\_H\_

8#define ZEPHYR\_INCLUDE\_DRIVERS\_SENSOR\_PZEM004T\_H\_

9

10#include <[zephyr/drivers/sensor.h](sensor_8h.md)>

11

12/\* PZEM004T specific channels \*/

[ 13](pzem004t_8h.md#ae89669c0c9353578730abddbf89317c8)enum [sensor\_channel\_pzem004t](pzem004t_8h.md#ae89669c0c9353578730abddbf89317c8) {

14 /\* Energy corresponds to active power accumulated over time.

15 \* Units: 1Wh (Watt-hours)

16 \*/

[ 17](pzem004t_8h.md#ae89669c0c9353578730abddbf89317c8a93ae8e1b50fd213580f3542f8af8d678) [SENSOR\_CHAN\_PZEM004T\_ENERGY](pzem004t_8h.md#ae89669c0c9353578730abddbf89317c8a93ae8e1b50fd213580f3542f8af8d678) = [SENSOR\_CHAN\_PRIV\_START](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934ac1f260296289d93a13c5686ca11bdc12),

18 /\* Power factor is defined as ratio of real power to apparent power 0. 01 resolution.

19 \* Unit: No unit

20 \*/

[ 21](pzem004t_8h.md#ae89669c0c9353578730abddbf89317c8af4816399cbd0a3498dccd171a74895d2) [SENSOR\_CHAN\_PZEM004T\_POWER\_FACTOR](pzem004t_8h.md#ae89669c0c9353578730abddbf89317c8af4816399cbd0a3498dccd171a74895d2),

22 /\* Alarm status is 0xFF when current active power is greater than power alarm threshold.

23 \* 0x00 when current power is less than power alarm threshold.

24 \* Unit: No unit

25 \*/

[ 26](pzem004t_8h.md#ae89669c0c9353578730abddbf89317c8ac71d41aebb26977781fd9dca39b43352) [SENSOR\_CHAN\_PZEM004T\_ALARM\_STATUS](pzem004t_8h.md#ae89669c0c9353578730abddbf89317c8ac71d41aebb26977781fd9dca39b43352),

27 /\* Active Power above which the power alarm threshold is set.

28 \* Unit: 1W (Watts)

29 \*/

[ 30](pzem004t_8h.md#ae89669c0c9353578730abddbf89317c8a268e403bacb31a68888ad5a527a87f4b) [SENSOR\_CHAN\_PZEM004T\_POWER\_ALARM\_THRESHOLD](pzem004t_8h.md#ae89669c0c9353578730abddbf89317c8a268e403bacb31a68888ad5a527a87f4b),

31 /\* Unique Modbus address of each pzem004t device on the modbus. Only use this

32 \* to set individual modbus address by connecteing each device individually.

33 \*/

[ 34](pzem004t_8h.md#ae89669c0c9353578730abddbf89317c8ab45e14abf577f9913f6d2c62b8c42efc) [SENSOR\_CHAN\_PZEM004T\_MODBUS\_RTU\_ADDRESS](pzem004t_8h.md#ae89669c0c9353578730abddbf89317c8ab45e14abf577f9913f6d2c62b8c42efc),

35 /\* Channel used to set the Modbus address of pzem004t device for the device instance.

36 \* This does not set the modbus address of the device. It is used to set the

37 \* modbus address of the device instance only for the driver.

38 \*/

[ 39](pzem004t_8h.md#ae89669c0c9353578730abddbf89317c8a416600d86b5821fa0d0b7980327193ee) [SENSOR\_CHAN\_PZEM004T\_ADDRESS\_INST\_SET](pzem004t_8h.md#ae89669c0c9353578730abddbf89317c8a416600d86b5821fa0d0b7980327193ee),

40 /\* Channel used to reset the Energy counter of the pzem004t sensor. Please enable

41 \* the CONFIG\_PZEM004T\_ENABLE\_RESET\_ENERGY option in prj.conf in application to

42 \* use the channel.

43 \*/

[ 44](pzem004t_8h.md#ae89669c0c9353578730abddbf89317c8a2c4c10ab296093f4422261ec7df12902) [SENSOR\_CHAN\_PZEM004T\_RESET\_ENERGY](pzem004t_8h.md#ae89669c0c9353578730abddbf89317c8a2c4c10ab296093f4422261ec7df12902),

45};

46

[ 47](pzem004t_8h.md#a33c78de1fb354c14fc0438a06f494a79)enum [sensor\_attribute\_pzem004t](pzem004t_8h.md#a33c78de1fb354c14fc0438a06f494a79) {

48 /\* Active Power above which the power alarm threshold is set.

49 \* Unit: 1W (Watts)

50 \*/

[ 51](pzem004t_8h.md#a33c78de1fb354c14fc0438a06f494a79ae295849a8604ce5dbf1b69a5aa72108b) [SENSOR\_ATTR\_PZEM004T\_POWER\_ALARM\_THRESHOLD](pzem004t_8h.md#a33c78de1fb354c14fc0438a06f494a79ae295849a8604ce5dbf1b69a5aa72108b) = [SENSOR\_ATTR\_PRIV\_START](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940bafb4b5859bc369f817f60eaa161bcefc3),

52 /\* Unique Modbus address of each pzem004t device on the modbus. Only use this

53 \* to set individual modbus address by connecteing each device individually.

54 \*/

[ 55](pzem004t_8h.md#a33c78de1fb354c14fc0438a06f494a79ad785a07dc2bfcb54ca672d6f8a09c7e7) [SENSOR\_ATTR\_PZEM004T\_MODBUS\_RTU\_ADDRESS](pzem004t_8h.md#a33c78de1fb354c14fc0438a06f494a79ad785a07dc2bfcb54ca672d6f8a09c7e7),

56 /\* Attribute used to set the Modbus address of pzem004t device for the device instance.

57 \* This does not set the modbus address of the device. It is used to set the

58 \* modbus address of the device instance only for the driver.

59 \*/

[ 60](pzem004t_8h.md#a33c78de1fb354c14fc0438a06f494a79a4653bc9656221e9359c820d618acd937) [SENSOR\_ATTR\_PZEM004T\_ADDRESS\_INST\_SET](pzem004t_8h.md#a33c78de1fb354c14fc0438a06f494a79a4653bc9656221e9359c820d618acd937),

61 /\* Attribute used to reset the Energy counter of the pzem004t sensor. Please enable

62 \* the CONFIG\_PZEM004T\_ENABLE\_RESET\_ENERGY option in prj.conf in appplicationtn

63 \* use the channel.

64 \*/

[ 65](pzem004t_8h.md#a33c78de1fb354c14fc0438a06f494a79a674c0ad21c9adcc62f078f69b36fea01) [SENSOR\_ATTR\_PZEM004T\_RESET\_ENERGY](pzem004t_8h.md#a33c78de1fb354c14fc0438a06f494a79a674c0ad21c9adcc62f078f69b36fea01),

66};

67

68#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_SENSOR\_PZEM004T\_H\_ \*/

[SENSOR\_ATTR\_PRIV\_START](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940bafb4b5859bc369f817f60eaa161bcefc3)

@ SENSOR\_ATTR\_PRIV\_START

This and higher values are sensor specific.

**Definition** sensor.h:372

[SENSOR\_CHAN\_PRIV\_START](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934ac1f260296289d93a13c5686ca11bdc12)

@ SENSOR\_CHAN\_PRIV\_START

This and higher values are sensor specific.

**Definition** sensor.h:217

[sensor\_attribute\_pzem004t](pzem004t_8h.md#a33c78de1fb354c14fc0438a06f494a79)

sensor\_attribute\_pzem004t

**Definition** pzem004t.h:47

[SENSOR\_ATTR\_PZEM004T\_ADDRESS\_INST\_SET](pzem004t_8h.md#a33c78de1fb354c14fc0438a06f494a79a4653bc9656221e9359c820d618acd937)

@ SENSOR\_ATTR\_PZEM004T\_ADDRESS\_INST\_SET

**Definition** pzem004t.h:60

[SENSOR\_ATTR\_PZEM004T\_RESET\_ENERGY](pzem004t_8h.md#a33c78de1fb354c14fc0438a06f494a79a674c0ad21c9adcc62f078f69b36fea01)

@ SENSOR\_ATTR\_PZEM004T\_RESET\_ENERGY

**Definition** pzem004t.h:65

[SENSOR\_ATTR\_PZEM004T\_MODBUS\_RTU\_ADDRESS](pzem004t_8h.md#a33c78de1fb354c14fc0438a06f494a79ad785a07dc2bfcb54ca672d6f8a09c7e7)

@ SENSOR\_ATTR\_PZEM004T\_MODBUS\_RTU\_ADDRESS

**Definition** pzem004t.h:55

[SENSOR\_ATTR\_PZEM004T\_POWER\_ALARM\_THRESHOLD](pzem004t_8h.md#a33c78de1fb354c14fc0438a06f494a79ae295849a8604ce5dbf1b69a5aa72108b)

@ SENSOR\_ATTR\_PZEM004T\_POWER\_ALARM\_THRESHOLD

**Definition** pzem004t.h:51

[sensor\_channel\_pzem004t](pzem004t_8h.md#ae89669c0c9353578730abddbf89317c8)

sensor\_channel\_pzem004t

**Definition** pzem004t.h:13

[SENSOR\_CHAN\_PZEM004T\_POWER\_ALARM\_THRESHOLD](pzem004t_8h.md#ae89669c0c9353578730abddbf89317c8a268e403bacb31a68888ad5a527a87f4b)

@ SENSOR\_CHAN\_PZEM004T\_POWER\_ALARM\_THRESHOLD

**Definition** pzem004t.h:30

[SENSOR\_CHAN\_PZEM004T\_RESET\_ENERGY](pzem004t_8h.md#ae89669c0c9353578730abddbf89317c8a2c4c10ab296093f4422261ec7df12902)

@ SENSOR\_CHAN\_PZEM004T\_RESET\_ENERGY

**Definition** pzem004t.h:44

[SENSOR\_CHAN\_PZEM004T\_ADDRESS\_INST\_SET](pzem004t_8h.md#ae89669c0c9353578730abddbf89317c8a416600d86b5821fa0d0b7980327193ee)

@ SENSOR\_CHAN\_PZEM004T\_ADDRESS\_INST\_SET

**Definition** pzem004t.h:39

[SENSOR\_CHAN\_PZEM004T\_ENERGY](pzem004t_8h.md#ae89669c0c9353578730abddbf89317c8a93ae8e1b50fd213580f3542f8af8d678)

@ SENSOR\_CHAN\_PZEM004T\_ENERGY

**Definition** pzem004t.h:17

[SENSOR\_CHAN\_PZEM004T\_MODBUS\_RTU\_ADDRESS](pzem004t_8h.md#ae89669c0c9353578730abddbf89317c8ab45e14abf577f9913f6d2c62b8c42efc)

@ SENSOR\_CHAN\_PZEM004T\_MODBUS\_RTU\_ADDRESS

**Definition** pzem004t.h:34

[SENSOR\_CHAN\_PZEM004T\_ALARM\_STATUS](pzem004t_8h.md#ae89669c0c9353578730abddbf89317c8ac71d41aebb26977781fd9dca39b43352)

@ SENSOR\_CHAN\_PZEM004T\_ALARM\_STATUS

**Definition** pzem004t.h:26

[SENSOR\_CHAN\_PZEM004T\_POWER\_FACTOR](pzem004t_8h.md#ae89669c0c9353578730abddbf89317c8af4816399cbd0a3498dccd171a74895d2)

@ SENSOR\_CHAN\_PZEM004T\_POWER\_FACTOR

**Definition** pzem004t.h:21

[sensor.h](sensor_8h.md)

Public APIs for the sensor driver.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [sensor](dir_b6423b3a8fc1c9278ff19cba182cfe6d.md)
- [pzem004t.h](pzem004t_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
