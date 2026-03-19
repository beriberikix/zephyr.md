---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/tsl2591_8h_source.html
original_path: doxygen/html/tsl2591_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

tsl2591.h

[Go to the documentation of this file.](tsl2591_8h.md)

1/\*

2 \* Copyright (c) 2023 Kurtis Dinelle

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

14

15#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_SENSOR\_TSL2591\_H\_

16#define ZEPHYR\_INCLUDE\_DRIVERS\_SENSOR\_TSL2591\_H\_

17

18#include <[zephyr/drivers/sensor.h](sensor_8h.md)>

19

20#ifdef \_\_cplusplus

21extern "C" {

22#endif

23

[ 24](tsl2591_8h.md#a683bdf5ef1219acd06189f46f9a5840b)enum [sensor\_attribute\_tsl2591](tsl2591_8h.md#a683bdf5ef1219acd06189f46f9a5840b) {

25 /\* Sensor ADC Gain Mode

26 \* Rather than set this value directly, can only be set to operate in one of four modes:

27 \*

28 \* TSL2591\_SENSOR\_GAIN\_LOW

29 \* TSL2591\_SENSOR\_GAIN\_MED

30 \* TSL2591\_SENSOR\_GAIN\_HIGH

31 \* TSL2591\_SENSOR\_GAIN\_MAX

32 \*

33 \* See datasheet for actual typical gain scales these modes correspond to.

34 \*/

[ 35](tsl2591_8h.md#a683bdf5ef1219acd06189f46f9a5840ba3016fceb8359cc1e6ef20a6e3dbf56b5) [SENSOR\_ATTR\_GAIN\_MODE](tsl2591_8h.md#a683bdf5ef1219acd06189f46f9a5840ba3016fceb8359cc1e6ef20a6e3dbf56b5) = [SENSOR\_ATTR\_PRIV\_START](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940bafb4b5859bc369f817f60eaa161bcefc3) + 1,

36

37 /\* Sensor ADC Integration Time (in ms)

38 \* Can only be set to one of six values:

39 \*

40 \* 100, 200, 300, 400, 500, or 600

41 \*/

[ 42](tsl2591_8h.md#a683bdf5ef1219acd06189f46f9a5840baeba46c663afa61df6d07ce3f90f2ec59) [SENSOR\_ATTR\_INTEGRATION\_TIME](tsl2540_8h.md#a9883d80dadfb4ea2b3362579f16ff2a7aeba46c663afa61df6d07ce3f90f2ec59),

43

44 /\* Sensor ALS Interrupt Persist Filter

45 \* Represents the number of consecutive sensor readings outside of a set threshold

46 \* before triggering an interrupt. Can only be set to one of sixteen values:

47 \*

48 \* 0, 1, 2, 3, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, or 60

49 \*

50 \* Setting this to 0 causes an interrupt to generate every ALS cycle,

51 \* regardless of threshold.

52 \* Setting this to 1 is equivalent to the no-persist interrupt mode.

53 \*/

[ 54](tsl2591_8h.md#a683bdf5ef1219acd06189f46f9a5840ba1d689501ee9f6619454ecc17201d4022) [SENSOR\_ATTR\_INT\_PERSIST](tsl2591_8h.md#a683bdf5ef1219acd06189f46f9a5840ba1d689501ee9f6619454ecc17201d4022)

55};

56

[ 57](tsl2591_8h.md#a1ee7e6e68817a10b7667bec7b52e01d8)enum [sensor\_gain\_tsl2591](tsl2591_8h.md#a1ee7e6e68817a10b7667bec7b52e01d8) {

[ 58](tsl2591_8h.md#a1ee7e6e68817a10b7667bec7b52e01d8a544da22b5e70425dc5d2c3f21683fd44) [TSL2591\_SENSOR\_GAIN\_LOW](tsl2591_8h.md#a1ee7e6e68817a10b7667bec7b52e01d8a544da22b5e70425dc5d2c3f21683fd44),

[ 59](tsl2591_8h.md#a1ee7e6e68817a10b7667bec7b52e01d8a14ed033d086566893a305e67a3e63be1) [TSL2591\_SENSOR\_GAIN\_MED](tsl2591_8h.md#a1ee7e6e68817a10b7667bec7b52e01d8a14ed033d086566893a305e67a3e63be1),

[ 60](tsl2591_8h.md#a1ee7e6e68817a10b7667bec7b52e01d8a439580991f302eb9f065d4d4cc093ea4) [TSL2591\_SENSOR\_GAIN\_HIGH](tsl2591_8h.md#a1ee7e6e68817a10b7667bec7b52e01d8a439580991f302eb9f065d4d4cc093ea4),

[ 61](tsl2591_8h.md#a1ee7e6e68817a10b7667bec7b52e01d8aed9cac2266a0e7172b1ac5c48a2d9f98) [TSL2591\_SENSOR\_GAIN\_MAX](tsl2591_8h.md#a1ee7e6e68817a10b7667bec7b52e01d8aed9cac2266a0e7172b1ac5c48a2d9f98)

62};

63

64#ifdef \_\_cplusplus

65}

66#endif

67

68#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_SENSOR\_TSL2591\_H\_ \*/

[SENSOR\_ATTR\_PRIV\_START](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940bafb4b5859bc369f817f60eaa161bcefc3)

@ SENSOR\_ATTR\_PRIV\_START

This and higher values are sensor specific.

**Definition** sensor.h:359

[sensor.h](sensor_8h.md)

Public APIs for the sensor driver.

[SENSOR\_ATTR\_INTEGRATION\_TIME](tsl2540_8h.md#a9883d80dadfb4ea2b3362579f16ff2a7aeba46c663afa61df6d07ce3f90f2ec59)

@ SENSOR\_ATTR\_INTEGRATION\_TIME

**Definition** tsl2540.h:26

[sensor\_gain\_tsl2591](tsl2591_8h.md#a1ee7e6e68817a10b7667bec7b52e01d8)

sensor\_gain\_tsl2591

**Definition** tsl2591.h:57

[TSL2591\_SENSOR\_GAIN\_MED](tsl2591_8h.md#a1ee7e6e68817a10b7667bec7b52e01d8a14ed033d086566893a305e67a3e63be1)

@ TSL2591\_SENSOR\_GAIN\_MED

**Definition** tsl2591.h:59

[TSL2591\_SENSOR\_GAIN\_HIGH](tsl2591_8h.md#a1ee7e6e68817a10b7667bec7b52e01d8a439580991f302eb9f065d4d4cc093ea4)

@ TSL2591\_SENSOR\_GAIN\_HIGH

**Definition** tsl2591.h:60

[TSL2591\_SENSOR\_GAIN\_LOW](tsl2591_8h.md#a1ee7e6e68817a10b7667bec7b52e01d8a544da22b5e70425dc5d2c3f21683fd44)

@ TSL2591\_SENSOR\_GAIN\_LOW

**Definition** tsl2591.h:58

[TSL2591\_SENSOR\_GAIN\_MAX](tsl2591_8h.md#a1ee7e6e68817a10b7667bec7b52e01d8aed9cac2266a0e7172b1ac5c48a2d9f98)

@ TSL2591\_SENSOR\_GAIN\_MAX

**Definition** tsl2591.h:61

[sensor\_attribute\_tsl2591](tsl2591_8h.md#a683bdf5ef1219acd06189f46f9a5840b)

sensor\_attribute\_tsl2591

**Definition** tsl2591.h:24

[SENSOR\_ATTR\_INT\_PERSIST](tsl2591_8h.md#a683bdf5ef1219acd06189f46f9a5840ba1d689501ee9f6619454ecc17201d4022)

@ SENSOR\_ATTR\_INT\_PERSIST

**Definition** tsl2591.h:54

[SENSOR\_ATTR\_GAIN\_MODE](tsl2591_8h.md#a683bdf5ef1219acd06189f46f9a5840ba3016fceb8359cc1e6ef20a6e3dbf56b5)

@ SENSOR\_ATTR\_GAIN\_MODE

**Definition** tsl2591.h:35

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [sensor](dir_b6423b3a8fc1c9278ff19cba182cfe6d.md)
- [tsl2591.h](tsl2591_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
