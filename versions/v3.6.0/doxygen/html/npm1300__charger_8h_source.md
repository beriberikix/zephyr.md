---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/npm1300__charger_8h_source.html
original_path: doxygen/html/npm1300__charger_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
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

15};

16

17#endif

[SENSOR\_CHAN\_PRIV\_START](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934ac1f260296289d93a13c5686ca11bdc12)

@ SENSOR\_CHAN\_PRIV\_START

This and higher values are sensor specific.

**Definition** sensor.h:202

[sensor\_channel\_npm1300\_charger](npm1300__charger_8h.md#a73310bf3cac43b2c78e102870fa4e2cd)

sensor\_channel\_npm1300\_charger

**Definition** npm1300\_charger.h:12

[SENSOR\_CHAN\_NPM1300\_CHARGER\_STATUS](npm1300__charger_8h.md#a73310bf3cac43b2c78e102870fa4e2cdaa4bb47c54305e518df185479c9b0a754)

@ SENSOR\_CHAN\_NPM1300\_CHARGER\_STATUS

**Definition** npm1300\_charger.h:13

[SENSOR\_CHAN\_NPM1300\_CHARGER\_ERROR](npm1300__charger_8h.md#a73310bf3cac43b2c78e102870fa4e2cdab69ad4aa4cf63404fa089c3841d467cd)

@ SENSOR\_CHAN\_NPM1300\_CHARGER\_ERROR

**Definition** npm1300\_charger.h:14

[sensor.h](sensor_8h.md)

Public APIs for the sensor driver.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [sensor](dir_b6423b3a8fc1c9278ff19cba182cfe6d.md)
- [npm1300\_charger.h](npm1300__charger_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
