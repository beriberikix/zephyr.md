---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/drivers_2sensor_2it8xxx2__vcmp_8h_source.html
original_path: doxygen/html/drivers_2sensor_2it8xxx2__vcmp_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

it8xxx2\_vcmp.h

[Go to the documentation of this file.](drivers_2sensor_2it8xxx2__vcmp_8h.md)

1/\*

2 \* Copyright (c) 2022 ITE Technology Corporation.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_SENSOR\_IT8XXX2\_VCMP\_H\_

8#define ZEPHYR\_INCLUDE\_DRIVERS\_SENSOR\_IT8XXX2\_VCMP\_H\_

9

10#ifdef \_\_cplusplus

11extern "C" {

12#endif

13

14#include <[zephyr/drivers/sensor.h](sensor_8h.md)>

15

[ 16](drivers_2sensor_2it8xxx2__vcmp_8h.md#acd4ae03345c06203e80ad4f535098165)enum [it8xxx2\_vcmp\_sensor\_attribute](drivers_2sensor_2it8xxx2__vcmp_8h.md#acd4ae03345c06203e80ad4f535098165) {

[ 17](drivers_2sensor_2it8xxx2__vcmp_8h.md#acd4ae03345c06203e80ad4f535098165a8a66a89764bff1e455273a02da29903d) [SENSOR\_ATTR\_LOWER\_VOLTAGE\_THRESH](adc__cmp__npcx_8h.md#a87c321b131ecec52103cc63b22c0018aa8a66a89764bff1e455273a02da29903d) = [SENSOR\_ATTR\_PRIV\_START](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940bafb4b5859bc369f817f60eaa161bcefc3),

[ 18](drivers_2sensor_2it8xxx2__vcmp_8h.md#acd4ae03345c06203e80ad4f535098165aaaadca90015c5516321259b8921cedc3) [SENSOR\_ATTR\_UPPER\_VOLTAGE\_THRESH](adc__cmp__npcx_8h.md#a87c321b131ecec52103cc63b22c0018aaaaadca90015c5516321259b8921cedc3),

19};

20

21#ifdef \_\_cplusplus

22}

23#endif

24

25#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_SENSOR\_IT8XXX2\_VCMP\_H\_ \*/

[SENSOR\_ATTR\_LOWER\_VOLTAGE\_THRESH](adc__cmp__npcx_8h.md#a87c321b131ecec52103cc63b22c0018aa8a66a89764bff1e455273a02da29903d)

@ SENSOR\_ATTR\_LOWER\_VOLTAGE\_THRESH

**Definition** adc\_cmp\_npcx.h:27

[SENSOR\_ATTR\_UPPER\_VOLTAGE\_THRESH](adc__cmp__npcx_8h.md#a87c321b131ecec52103cc63b22c0018aaaaadca90015c5516321259b8921cedc3)

@ SENSOR\_ATTR\_UPPER\_VOLTAGE\_THRESH

**Definition** adc\_cmp\_npcx.h:28

[it8xxx2\_vcmp\_sensor\_attribute](drivers_2sensor_2it8xxx2__vcmp_8h.md#acd4ae03345c06203e80ad4f535098165)

it8xxx2\_vcmp\_sensor\_attribute

**Definition** it8xxx2\_vcmp.h:16

[SENSOR\_ATTR\_PRIV\_START](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940bafb4b5859bc369f817f60eaa161bcefc3)

@ SENSOR\_ATTR\_PRIV\_START

This and higher values are sensor specific.

**Definition** sensor.h:356

[sensor.h](sensor_8h.md)

Public APIs for the sensor driver.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [sensor](dir_b6423b3a8fc1c9278ff19cba182cfe6d.md)
- [it8xxx2\_vcmp.h](drivers_2sensor_2it8xxx2__vcmp_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
