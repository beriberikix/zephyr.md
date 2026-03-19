---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/sht4x_8h_source.html
original_path: doxygen/html/sht4x_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

sht4x.h

[Go to the documentation of this file.](sht4x_8h.md)

1/\*

2 \* Copyright (c) 2021, Leonard Pollak

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

15

16#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_SENSOR\_SHT4X\_H\_

17#define ZEPHYR\_INCLUDE\_DRIVERS\_SENSOR\_SHT4X\_H\_

18

19#ifdef \_\_cplusplus

20extern "C" {

21#endif

22

23#include <[zephyr/drivers/sensor.h](sensor_8h.md)>

24

25/\* Maximum temperature above which the heater should not be used \*/

[ 26](sht4x_8h.md#af10d0155ec46d5b5152251d02f7578ee)#define SHT4X\_HEATER\_MAX\_TEMP 65

27

[ 28](sht4x_8h.md#a4191e02c97b8130a1c96d47c0939d535)enum [sensor\_attribute\_sht4x](sht4x_8h.md#a4191e02c97b8130a1c96d47c0939d535) {

29 /\* Heater Power: 0, 1, 2 -> high, med, low \*/

[ 30](sht4x_8h.md#a4191e02c97b8130a1c96d47c0939d535ad18746a0cddc2713d63b0b6ce70f5052) [SENSOR\_ATTR\_SHT4X\_HEATER\_POWER](sht4x_8h.md#a4191e02c97b8130a1c96d47c0939d535ad18746a0cddc2713d63b0b6ce70f5052) = [SENSOR\_ATTR\_PRIV\_START](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940bafb4b5859bc369f817f60eaa161bcefc3),

31 /\* Heater Duration: 0, 1 -> long, short \*/

[ 32](sht4x_8h.md#a4191e02c97b8130a1c96d47c0939d535a1812fd253d281025c8d4155f58e9cbd6) [SENSOR\_ATTR\_SHT4X\_HEATER\_DURATION](sht4x_8h.md#a4191e02c97b8130a1c96d47c0939d535a1812fd253d281025c8d4155f58e9cbd6)

33};

34

[ 44](sht4x_8h.md#af2539064f44eb3981cb40a3c2f7a0eb8)int [sht4x\_fetch\_with\_heater](sht4x_8h.md#af2539064f44eb3981cb40a3c2f7a0eb8)(const struct [device](structdevice.md) \*dev);

45

46#ifdef \_\_cplusplus

47}

48#endif

49

50#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_SENSOR\_SHT4X\_H\_ \*/

[SENSOR\_ATTR\_PRIV\_START](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940bafb4b5859bc369f817f60eaa161bcefc3)

@ SENSOR\_ATTR\_PRIV\_START

This and higher values are sensor specific.

**Definition** sensor.h:359

[sensor.h](sensor_8h.md)

Public APIs for the sensor driver.

[sensor\_attribute\_sht4x](sht4x_8h.md#a4191e02c97b8130a1c96d47c0939d535)

sensor\_attribute\_sht4x

**Definition** sht4x.h:28

[SENSOR\_ATTR\_SHT4X\_HEATER\_DURATION](sht4x_8h.md#a4191e02c97b8130a1c96d47c0939d535a1812fd253d281025c8d4155f58e9cbd6)

@ SENSOR\_ATTR\_SHT4X\_HEATER\_DURATION

**Definition** sht4x.h:32

[SENSOR\_ATTR\_SHT4X\_HEATER\_POWER](sht4x_8h.md#a4191e02c97b8130a1c96d47c0939d535ad18746a0cddc2713d63b0b6ce70f5052)

@ SENSOR\_ATTR\_SHT4X\_HEATER\_POWER

**Definition** sht4x.h:30

[sht4x\_fetch\_with\_heater](sht4x_8h.md#af2539064f44eb3981cb40a3c2f7a0eb8)

int sht4x\_fetch\_with\_heater(const struct device \*dev)

Fetches data using the on-chip heater.

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:412

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [sensor](dir_b6423b3a8fc1c9278ff19cba182cfe6d.md)
- [sht4x.h](sht4x_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
