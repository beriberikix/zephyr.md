---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/lm95234_8h_source.html
original_path: doxygen/html/lm95234_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

lm95234.h

[Go to the documentation of this file.](lm95234_8h.md)

1/\*

2 \* Copyright (c) 2024, Calian Advanced Technologies

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_SENSOR\_LM95234\_H\_

8#define ZEPHYR\_INCLUDE\_DRIVERS\_SENSOR\_LM95234\_H\_

9

10#include <[zephyr/drivers/sensor.h](sensor_8h.md)>

11

[ 12](lm95234_8h.md#ac9be5b7dd4705d9a2de2ca102943637d)enum [sensor\_channel\_lm95234](lm95234_8h.md#ac9be5b7dd4705d9a2de2ca102943637d) {

13 /\* External temperature inputs \*/

[ 14](lm95234_8h.md#ac9be5b7dd4705d9a2de2ca102943637dae4c495a1c560dc22899d5fbfdbfe3818) [SENSOR\_CHAN\_LM95234\_REMOTE\_TEMP\_1](lm95234_8h.md#ac9be5b7dd4705d9a2de2ca102943637dae4c495a1c560dc22899d5fbfdbfe3818) = [SENSOR\_CHAN\_PRIV\_START](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934ac1f260296289d93a13c5686ca11bdc12),

[ 15](lm95234_8h.md#ac9be5b7dd4705d9a2de2ca102943637da11ccf81167550f39556fb0bfbed7e214) [SENSOR\_CHAN\_LM95234\_REMOTE\_TEMP\_2](lm95234_8h.md#ac9be5b7dd4705d9a2de2ca102943637da11ccf81167550f39556fb0bfbed7e214),

[ 16](lm95234_8h.md#ac9be5b7dd4705d9a2de2ca102943637da7256e03d9f0e5177af20880193348d4a) [SENSOR\_CHAN\_LM95234\_REMOTE\_TEMP\_3](lm95234_8h.md#ac9be5b7dd4705d9a2de2ca102943637da7256e03d9f0e5177af20880193348d4a),

[ 17](lm95234_8h.md#ac9be5b7dd4705d9a2de2ca102943637da395619c35328ae6fbc2d7b8d3517a2b8) [SENSOR\_CHAN\_LM95234\_REMOTE\_TEMP\_4](lm95234_8h.md#ac9be5b7dd4705d9a2de2ca102943637da395619c35328ae6fbc2d7b8d3517a2b8)

18};

19

20#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_SENSOR\_LM95234\_H\_ \*/

[SENSOR\_CHAN\_PRIV\_START](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934ac1f260296289d93a13c5686ca11bdc12)

@ SENSOR\_CHAN\_PRIV\_START

This and higher values are sensor specific.

**Definition** sensor.h:208

[sensor\_channel\_lm95234](lm95234_8h.md#ac9be5b7dd4705d9a2de2ca102943637d)

sensor\_channel\_lm95234

**Definition** lm95234.h:12

[SENSOR\_CHAN\_LM95234\_REMOTE\_TEMP\_2](lm95234_8h.md#ac9be5b7dd4705d9a2de2ca102943637da11ccf81167550f39556fb0bfbed7e214)

@ SENSOR\_CHAN\_LM95234\_REMOTE\_TEMP\_2

**Definition** lm95234.h:15

[SENSOR\_CHAN\_LM95234\_REMOTE\_TEMP\_4](lm95234_8h.md#ac9be5b7dd4705d9a2de2ca102943637da395619c35328ae6fbc2d7b8d3517a2b8)

@ SENSOR\_CHAN\_LM95234\_REMOTE\_TEMP\_4

**Definition** lm95234.h:17

[SENSOR\_CHAN\_LM95234\_REMOTE\_TEMP\_3](lm95234_8h.md#ac9be5b7dd4705d9a2de2ca102943637da7256e03d9f0e5177af20880193348d4a)

@ SENSOR\_CHAN\_LM95234\_REMOTE\_TEMP\_3

**Definition** lm95234.h:16

[SENSOR\_CHAN\_LM95234\_REMOTE\_TEMP\_1](lm95234_8h.md#ac9be5b7dd4705d9a2de2ca102943637dae4c495a1c560dc22899d5fbfdbfe3818)

@ SENSOR\_CHAN\_LM95234\_REMOTE\_TEMP\_1

**Definition** lm95234.h:14

[sensor.h](sensor_8h.md)

Public APIs for the sensor driver.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [sensor](dir_b6423b3a8fc1c9278ff19cba182cfe6d.md)
- [lm95234.h](lm95234_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
