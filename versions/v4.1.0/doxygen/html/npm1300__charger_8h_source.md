---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/npm1300__charger_8h_source.html
original_path: doxygen/html/npm1300__charger_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

npm1300\_charger.h

[Go to the documentation of this file.](npm1300__charger_8h.md)

1/\*

2 \* Copyright (c) 2023 Nordic Semiconductor ASA

3 \* SPDX-License-Identifier: Apache-2.0

4 \*/

5

6#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_SENSOR\_NPM1300\_CHARGER\_H\_

7#define ZEPHYR\_INCLUDE\_DRIVERS\_SENSOR\_NPM1300\_CHARGER\_H\_

8

9#include <[zephyr/drivers/sensor.h](sensor_8h.md)>

10

11/\* NPM1300 charger specific channels \*/

[ 12](npm1300__charger_8h.md#a73310bf3cac43b2c78e102870fa4e2cd)enum [sensor\_channel\_npm1300\_charger](npm1300__charger_8h.md#a73310bf3cac43b2c78e102870fa4e2cd) {

[ 13](npm1300__charger_8h.md#a73310bf3cac43b2c78e102870fa4e2cdaa4bb47c54305e518df185479c9b0a754) [SENSOR\_CHAN\_NPM1300\_CHARGER\_STATUS](npm1300__charger_8h.md#a73310bf3cac43b2c78e102870fa4e2cdaa4bb47c54305e518df185479c9b0a754) = [SENSOR\_CHAN\_PRIV\_START](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934ac1f260296289d93a13c5686ca11bdc12),

[ 14](npm1300__charger_8h.md#a73310bf3cac43b2c78e102870fa4e2cdab69ad4aa4cf63404fa089c3841d467cd) [SENSOR\_CHAN\_NPM1300\_CHARGER\_ERROR](npm1300__charger_8h.md#a73310bf3cac43b2c78e102870fa4e2cdab69ad4aa4cf63404fa089c3841d467cd),

[ 15](npm1300__charger_8h.md#a73310bf3cac43b2c78e102870fa4e2cda8c513a56e2bca5b71dbed04fd7031654) [SENSOR\_CHAN\_NPM1300\_CHARGER\_VBUS\_STATUS](npm1300__charger_8h.md#a73310bf3cac43b2c78e102870fa4e2cda8c513a56e2bca5b71dbed04fd7031654),

16};

17

18/\* NPM1300 charger specific attributes \*/

[ 19](npm1300__charger_8h.md#a96aa415750e25972820646b0e7ab047a)enum [sensor\_attribute\_npm1300\_charger](npm1300__charger_8h.md#a96aa415750e25972820646b0e7ab047a) {

[ 20](npm1300__charger_8h.md#a96aa415750e25972820646b0e7ab047aa916cbce1aedfbcbc6346ec76e0922c86) [SENSOR\_ATTR\_NPM1300\_CHARGER\_VBUS\_PRESENT](npm1300__charger_8h.md#a96aa415750e25972820646b0e7ab047aa916cbce1aedfbcbc6346ec76e0922c86) = [SENSOR\_ATTR\_PRIV\_START](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940bafb4b5859bc369f817f60eaa161bcefc3),

[ 21](npm1300__charger_8h.md#a96aa415750e25972820646b0e7ab047aab472912d3d4fcc9463f902c956fb9db5) [SENSOR\_ATTR\_NPM1300\_CHARGER\_VBUS\_CUR\_LIMIT](npm1300__charger_8h.md#a96aa415750e25972820646b0e7ab047aab472912d3d4fcc9463f902c956fb9db5),

[ 22](npm1300__charger_8h.md#a96aa415750e25972820646b0e7ab047aae6d164241e1a2026a7d701a4a8c6702b) [SENSOR\_ATTR\_NPM1300\_CHARGER\_VBUS\_OVERVLT\_PROT](npm1300__charger_8h.md#a96aa415750e25972820646b0e7ab047aae6d164241e1a2026a7d701a4a8c6702b),

[ 23](npm1300__charger_8h.md#a96aa415750e25972820646b0e7ab047aaec86b45dadb7ebbb72beb9902ce38a4c) [SENSOR\_ATTR\_NPM1300\_CHARGER\_VBUS\_UNDERVLT](npm1300__charger_8h.md#a96aa415750e25972820646b0e7ab047aaec86b45dadb7ebbb72beb9902ce38a4c),

[ 24](npm1300__charger_8h.md#a96aa415750e25972820646b0e7ab047aa017aa3135de4423399293b0d0aaa5fa8) [SENSOR\_ATTR\_NPM1300\_CHARGER\_VBUS\_SUSPENDED](npm1300__charger_8h.md#a96aa415750e25972820646b0e7ab047aa017aa3135de4423399293b0d0aaa5fa8),

[ 25](npm1300__charger_8h.md#a96aa415750e25972820646b0e7ab047aa00ff7be4030563abc57a8470d8849504) [SENSOR\_ATTR\_NPM1300\_CHARGER\_VBUS\_BUSOUT](npm1300__charger_8h.md#a96aa415750e25972820646b0e7ab047aa00ff7be4030563abc57a8470d8849504),

26};

27

28#endif

[SENSOR\_ATTR\_PRIV\_START](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940bafb4b5859bc369f817f60eaa161bcefc3)

@ SENSOR\_ATTR\_PRIV\_START

This and higher values are sensor specific.

**Definition** sensor.h:368

[SENSOR\_CHAN\_PRIV\_START](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934ac1f260296289d93a13c5686ca11bdc12)

@ SENSOR\_CHAN\_PRIV\_START

This and higher values are sensor specific.

**Definition** sensor.h:217

[sensor\_channel\_npm1300\_charger](npm1300__charger_8h.md#a73310bf3cac43b2c78e102870fa4e2cd)

sensor\_channel\_npm1300\_charger

**Definition** npm1300\_charger.h:12

[SENSOR\_CHAN\_NPM1300\_CHARGER\_VBUS\_STATUS](npm1300__charger_8h.md#a73310bf3cac43b2c78e102870fa4e2cda8c513a56e2bca5b71dbed04fd7031654)

@ SENSOR\_CHAN\_NPM1300\_CHARGER\_VBUS\_STATUS

**Definition** npm1300\_charger.h:15

[SENSOR\_CHAN\_NPM1300\_CHARGER\_STATUS](npm1300__charger_8h.md#a73310bf3cac43b2c78e102870fa4e2cdaa4bb47c54305e518df185479c9b0a754)

@ SENSOR\_CHAN\_NPM1300\_CHARGER\_STATUS

**Definition** npm1300\_charger.h:13

[SENSOR\_CHAN\_NPM1300\_CHARGER\_ERROR](npm1300__charger_8h.md#a73310bf3cac43b2c78e102870fa4e2cdab69ad4aa4cf63404fa089c3841d467cd)

@ SENSOR\_CHAN\_NPM1300\_CHARGER\_ERROR

**Definition** npm1300\_charger.h:14

[sensor\_attribute\_npm1300\_charger](npm1300__charger_8h.md#a96aa415750e25972820646b0e7ab047a)

sensor\_attribute\_npm1300\_charger

**Definition** npm1300\_charger.h:19

[SENSOR\_ATTR\_NPM1300\_CHARGER\_VBUS\_BUSOUT](npm1300__charger_8h.md#a96aa415750e25972820646b0e7ab047aa00ff7be4030563abc57a8470d8849504)

@ SENSOR\_ATTR\_NPM1300\_CHARGER\_VBUS\_BUSOUT

**Definition** npm1300\_charger.h:25

[SENSOR\_ATTR\_NPM1300\_CHARGER\_VBUS\_SUSPENDED](npm1300__charger_8h.md#a96aa415750e25972820646b0e7ab047aa017aa3135de4423399293b0d0aaa5fa8)

@ SENSOR\_ATTR\_NPM1300\_CHARGER\_VBUS\_SUSPENDED

**Definition** npm1300\_charger.h:24

[SENSOR\_ATTR\_NPM1300\_CHARGER\_VBUS\_PRESENT](npm1300__charger_8h.md#a96aa415750e25972820646b0e7ab047aa916cbce1aedfbcbc6346ec76e0922c86)

@ SENSOR\_ATTR\_NPM1300\_CHARGER\_VBUS\_PRESENT

**Definition** npm1300\_charger.h:20

[SENSOR\_ATTR\_NPM1300\_CHARGER\_VBUS\_CUR\_LIMIT](npm1300__charger_8h.md#a96aa415750e25972820646b0e7ab047aab472912d3d4fcc9463f902c956fb9db5)

@ SENSOR\_ATTR\_NPM1300\_CHARGER\_VBUS\_CUR\_LIMIT

**Definition** npm1300\_charger.h:21

[SENSOR\_ATTR\_NPM1300\_CHARGER\_VBUS\_OVERVLT\_PROT](npm1300__charger_8h.md#a96aa415750e25972820646b0e7ab047aae6d164241e1a2026a7d701a4a8c6702b)

@ SENSOR\_ATTR\_NPM1300\_CHARGER\_VBUS\_OVERVLT\_PROT

**Definition** npm1300\_charger.h:22

[SENSOR\_ATTR\_NPM1300\_CHARGER\_VBUS\_UNDERVLT](npm1300__charger_8h.md#a96aa415750e25972820646b0e7ab047aaec86b45dadb7ebbb72beb9902ce38a4c)

@ SENSOR\_ATTR\_NPM1300\_CHARGER\_VBUS\_UNDERVLT

**Definition** npm1300\_charger.h:23

[sensor.h](sensor_8h.md)

Public APIs for the sensor driver.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [sensor](dir_b6423b3a8fc1c9278ff19cba182cfe6d.md)
- [npm1300\_charger.h](npm1300__charger_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
