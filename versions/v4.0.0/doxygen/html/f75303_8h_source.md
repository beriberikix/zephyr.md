---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/f75303_8h_source.html
original_path: doxygen/html/f75303_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

f75303.h

[Go to the documentation of this file.](f75303_8h.md)

1/\*

2 \* Copyright (c) 2023 Google LLC

3 \* SPDX-License-Identifier: Apache-2.0

4 \*/

5

6#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_SENSOR\_F75303\_H\_

7#define ZEPHYR\_INCLUDE\_DRIVERS\_SENSOR\_F75303\_H\_

8

9#include <[zephyr/drivers/sensor.h](sensor_8h.md)>

10

11/\* F75303 specific channels \*/

[ 12](f75303_8h.md#a96dae361266d76f2b8e1c67fbbd1025c)enum [sensor\_channel\_f75303](f75303_8h.md#a96dae361266d76f2b8e1c67fbbd1025c) {

[ 13](f75303_8h.md#a96dae361266d76f2b8e1c67fbbd1025cabf376a5e557c00e29195e443fa56aa1a) [SENSOR\_CHAN\_F75303\_REMOTE1](f75303_8h.md#a96dae361266d76f2b8e1c67fbbd1025cabf376a5e557c00e29195e443fa56aa1a) = [SENSOR\_CHAN\_PRIV\_START](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934ac1f260296289d93a13c5686ca11bdc12),

[ 14](f75303_8h.md#a96dae361266d76f2b8e1c67fbbd1025caebf674588c51c5390c9e35a8252d8464) [SENSOR\_CHAN\_F75303\_REMOTE2](f75303_8h.md#a96dae361266d76f2b8e1c67fbbd1025caebf674588c51c5390c9e35a8252d8464),

15};

16

17#endif

[sensor\_channel\_f75303](f75303_8h.md#a96dae361266d76f2b8e1c67fbbd1025c)

sensor\_channel\_f75303

**Definition** f75303.h:12

[SENSOR\_CHAN\_F75303\_REMOTE1](f75303_8h.md#a96dae361266d76f2b8e1c67fbbd1025cabf376a5e557c00e29195e443fa56aa1a)

@ SENSOR\_CHAN\_F75303\_REMOTE1

**Definition** f75303.h:13

[SENSOR\_CHAN\_F75303\_REMOTE2](f75303_8h.md#a96dae361266d76f2b8e1c67fbbd1025caebf674588c51c5390c9e35a8252d8464)

@ SENSOR\_CHAN\_F75303\_REMOTE2

**Definition** f75303.h:14

[SENSOR\_CHAN\_PRIV\_START](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934ac1f260296289d93a13c5686ca11bdc12)

@ SENSOR\_CHAN\_PRIV\_START

This and higher values are sensor specific.

**Definition** sensor.h:208

[sensor.h](sensor_8h.md)

Public APIs for the sensor driver.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [sensor](dir_b6423b3a8fc1c9278ff19cba182cfe6d.md)
- [f75303.h](f75303_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
