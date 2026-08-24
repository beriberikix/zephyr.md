---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/paj7620_8h_source.html
original_path: doxygen/html/paj7620_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

paj7620.h

[Go to the documentation of this file.](paj7620_8h.md)

1/\*

2 \* Copyright (c) 2025 Paul Timke <ptimkec@live.com>

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

14

15#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_SENSOR\_PAJ7620\_H\_

16#define ZEPHYR\_INCLUDE\_DRIVERS\_SENSOR\_PAJ7620\_H\_

17

18#ifdef \_\_cplusplus

19extern "C"

20{

21#endif /\* \_\_cplusplus \*/

22

23#include <[zephyr/drivers/sensor.h](sensor_8h.md)>

24

[ 25](paj7620_8h.md#aa63753ca7c5f4bc1f478fc72fa3c320f)#define PAJ7620\_FLAG\_GES\_UP BIT(0)

[ 26](paj7620_8h.md#a492ae48e3a532d921422c1e9a7ef7e2e)#define PAJ7620\_FLAG\_GES\_DOWN BIT(1)

[ 27](paj7620_8h.md#ae61616e99b14af9949eb65d7aa09187e)#define PAJ7620\_FLAG\_GES\_LEFT BIT(2)

[ 28](paj7620_8h.md#a99ad889dfebad0ae277f5bea821a5551)#define PAJ7620\_FLAG\_GES\_RIGHT BIT(3)

[ 29](paj7620_8h.md#aeb6cd5bb1f28cae139daf6cddf344d00)#define PAJ7620\_FLAG\_GES\_FORWARD BIT(4)

[ 30](paj7620_8h.md#a564c0b02bb0b4606e6b58bb030ac765f)#define PAJ7620\_FLAG\_GES\_BACKWARD BIT(5)

[ 31](paj7620_8h.md#a80db26a635c1af0ea0cbf79b841c37af)#define PAJ7620\_FLAG\_GES\_CLOCKWISE BIT(6)

[ 32](paj7620_8h.md#aa992028736388f241425c9d210f43213)#define PAJ7620\_FLAG\_GES\_COUNTERCLOCKWISE BIT(7)

[ 33](paj7620_8h.md#a17c3e6864957600d440263f5861b8598)#define PAJ7620\_FLAG\_GES\_WAVE BIT(8)

34

[ 35](paj7620_8h.md#aee838947e01367f4a31b54798ca8231b)enum [sensor\_channel\_paj7620](paj7620_8h.md#aee838947e01367f4a31b54798ca8231b) {

[ 42](paj7620_8h.md#aee838947e01367f4a31b54798ca8231ba6d3555eeca40737b0cc96e731d9374d2) [SENSOR\_CHAN\_PAJ7620\_GESTURES](paj7620_8h.md#aee838947e01367f4a31b54798ca8231ba6d3555eeca40737b0cc96e731d9374d2) = [SENSOR\_CHAN\_PRIV\_START](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934ac1f260296289d93a13c5686ca11bdc12)

43};

44

45#ifdef \_\_cplusplus

46}

47#endif /\* \_\_cplusplus \*/

48

49#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_SENSOR\_PAJ7620\_H\_ \*/

[SENSOR\_CHAN\_PRIV\_START](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934ac1f260296289d93a13c5686ca11bdc12)

@ SENSOR\_CHAN\_PRIV\_START

This and higher values are sensor specific.

**Definition** sensor.h:217

[sensor\_channel\_paj7620](paj7620_8h.md#aee838947e01367f4a31b54798ca8231b)

sensor\_channel\_paj7620

**Definition** paj7620.h:35

[SENSOR\_CHAN\_PAJ7620\_GESTURES](paj7620_8h.md#aee838947e01367f4a31b54798ca8231ba6d3555eeca40737b0cc96e731d9374d2)

@ SENSOR\_CHAN\_PAJ7620\_GESTURES

This channel will contain gesture data as a bitmask where each set bit represents a detected gesture.

**Definition** paj7620.h:42

[sensor.h](sensor_8h.md)

Public APIs for the sensor driver.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [sensor](dir_b6423b3a8fc1c9278ff19cba182cfe6d.md)
- [paj7620.h](paj7620_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
