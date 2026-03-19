---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/npm2100__vbat_8h_source.html
original_path: doxygen/html/npm2100__vbat_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

npm2100\_vbat.h

[Go to the documentation of this file.](npm2100__vbat_8h.md)

1/\*

2 \* Copyright (c) 2024 Nordic Semiconductor ASA

3 \* SPDX-License-Identifier: Apache-2.0

4 \*/

5

6#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_SENSOR\_NPM2100\_VBAT\_H\_

7#define ZEPHYR\_INCLUDE\_DRIVERS\_SENSOR\_NPM2100\_VBAT\_H\_

8

9#include <[zephyr/drivers/sensor.h](sensor_8h.md)>

10

11/\* NPM2100 vbat specific channels \*/

[ 12](npm2100__vbat_8h.md#ad07cbdadaca3c654f3a27a54f74b30e7)enum [sensor\_channel\_npm2100\_vbat](npm2100__vbat_8h.md#ad07cbdadaca3c654f3a27a54f74b30e7) {

[ 13](npm2100__vbat_8h.md#ad07cbdadaca3c654f3a27a54f74b30e7ab2556cfe11bce37125a1b2c734acc368) [SENSOR\_CHAN\_NPM2100\_VBAT\_STATUS](npm2100__vbat_8h.md#ad07cbdadaca3c654f3a27a54f74b30e7ab2556cfe11bce37125a1b2c734acc368) = [SENSOR\_CHAN\_PRIV\_START](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934ac1f260296289d93a13c5686ca11bdc12),

[ 14](npm2100__vbat_8h.md#ad07cbdadaca3c654f3a27a54f74b30e7a5b291484fb7cf4978bd7607081ccbd4a) [SENSOR\_CHAN\_NPM2100\_VOLT\_DROOP](npm2100__vbat_8h.md#ad07cbdadaca3c654f3a27a54f74b30e7a5b291484fb7cf4978bd7607081ccbd4a),

[ 15](npm2100__vbat_8h.md#ad07cbdadaca3c654f3a27a54f74b30e7afa85e0dbca574d95493578cac8bff834) [SENSOR\_CHAN\_NPM2100\_DPS\_COUNT](npm2100__vbat_8h.md#ad07cbdadaca3c654f3a27a54f74b30e7afa85e0dbca574d95493578cac8bff834),

[ 16](npm2100__vbat_8h.md#ad07cbdadaca3c654f3a27a54f74b30e7a95abddd9aabcf283728d0fbd32834623) [SENSOR\_CHAN\_NPM2100\_DPS\_TIMER](npm2100__vbat_8h.md#ad07cbdadaca3c654f3a27a54f74b30e7a95abddd9aabcf283728d0fbd32834623),

[ 17](npm2100__vbat_8h.md#ad07cbdadaca3c654f3a27a54f74b30e7ae722a338b422b8310d0c999ef510cb49) [SENSOR\_CHAN\_NPM2100\_DPS\_DURATION](npm2100__vbat_8h.md#ad07cbdadaca3c654f3a27a54f74b30e7ae722a338b422b8310d0c999ef510cb49),

18};

19

20/\* NPM2100 vbat specific attributes \*/

[ 21](npm2100__vbat_8h.md#a0c9921cfee8de69b35666e1ab276196e)enum [sensor\_attr\_npm2100\_vbat](npm2100__vbat_8h.md#a0c9921cfee8de69b35666e1ab276196e) {

[ 22](npm2100__vbat_8h.md#a0c9921cfee8de69b35666e1ab276196ea6523499d40a42c85a2d316b74859ba1d) [SENSOR\_ATTR\_NPM2100\_ADC\_DELAY](npm2100__vbat_8h.md#a0c9921cfee8de69b35666e1ab276196ea6523499d40a42c85a2d316b74859ba1d) = [SENSOR\_ATTR\_PRIV\_START](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940bafb4b5859bc369f817f60eaa161bcefc3),

23};

24

25#endif

[SENSOR\_ATTR\_PRIV\_START](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940bafb4b5859bc369f817f60eaa161bcefc3)

@ SENSOR\_ATTR\_PRIV\_START

This and higher values are sensor specific.

**Definition** sensor.h:368

[SENSOR\_CHAN\_PRIV\_START](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934ac1f260296289d93a13c5686ca11bdc12)

@ SENSOR\_CHAN\_PRIV\_START

This and higher values are sensor specific.

**Definition** sensor.h:217

[sensor\_attr\_npm2100\_vbat](npm2100__vbat_8h.md#a0c9921cfee8de69b35666e1ab276196e)

sensor\_attr\_npm2100\_vbat

**Definition** npm2100\_vbat.h:21

[SENSOR\_ATTR\_NPM2100\_ADC\_DELAY](npm2100__vbat_8h.md#a0c9921cfee8de69b35666e1ab276196ea6523499d40a42c85a2d316b74859ba1d)

@ SENSOR\_ATTR\_NPM2100\_ADC\_DELAY

**Definition** npm2100\_vbat.h:22

[sensor\_channel\_npm2100\_vbat](npm2100__vbat_8h.md#ad07cbdadaca3c654f3a27a54f74b30e7)

sensor\_channel\_npm2100\_vbat

**Definition** npm2100\_vbat.h:12

[SENSOR\_CHAN\_NPM2100\_VOLT\_DROOP](npm2100__vbat_8h.md#ad07cbdadaca3c654f3a27a54f74b30e7a5b291484fb7cf4978bd7607081ccbd4a)

@ SENSOR\_CHAN\_NPM2100\_VOLT\_DROOP

**Definition** npm2100\_vbat.h:14

[SENSOR\_CHAN\_NPM2100\_DPS\_TIMER](npm2100__vbat_8h.md#ad07cbdadaca3c654f3a27a54f74b30e7a95abddd9aabcf283728d0fbd32834623)

@ SENSOR\_CHAN\_NPM2100\_DPS\_TIMER

**Definition** npm2100\_vbat.h:16

[SENSOR\_CHAN\_NPM2100\_VBAT\_STATUS](npm2100__vbat_8h.md#ad07cbdadaca3c654f3a27a54f74b30e7ab2556cfe11bce37125a1b2c734acc368)

@ SENSOR\_CHAN\_NPM2100\_VBAT\_STATUS

**Definition** npm2100\_vbat.h:13

[SENSOR\_CHAN\_NPM2100\_DPS\_DURATION](npm2100__vbat_8h.md#ad07cbdadaca3c654f3a27a54f74b30e7ae722a338b422b8310d0c999ef510cb49)

@ SENSOR\_CHAN\_NPM2100\_DPS\_DURATION

**Definition** npm2100\_vbat.h:17

[SENSOR\_CHAN\_NPM2100\_DPS\_COUNT](npm2100__vbat_8h.md#ad07cbdadaca3c654f3a27a54f74b30e7afa85e0dbca574d95493578cac8bff834)

@ SENSOR\_CHAN\_NPM2100\_DPS\_COUNT

**Definition** npm2100\_vbat.h:15

[sensor.h](sensor_8h.md)

Public APIs for the sensor driver.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [sensor](dir_b6423b3a8fc1c9278ff19cba182cfe6d.md)
- [npm2100\_vbat.h](npm2100__vbat_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
