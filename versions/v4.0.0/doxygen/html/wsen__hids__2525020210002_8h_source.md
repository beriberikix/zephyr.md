---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/wsen__hids__2525020210002_8h_source.html
original_path: doxygen/html/wsen__hids__2525020210002_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

wsen\_hids\_2525020210002.h

[Go to the documentation of this file.](wsen__hids__2525020210002_8h.md)

1/\*

2 \* Copyright (c) 2024 Würth Elektronik eiSos GmbH & Co. KG

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

12

13#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_SENSOR\_WSEN\_HIDS\_2525020210002\_H\_

14#define ZEPHYR\_INCLUDE\_DRIVERS\_SENSOR\_WSEN\_HIDS\_2525020210002\_H\_

15

16#ifdef \_\_cplusplus

17extern "C" {

18#endif

19

20#include <[zephyr/drivers/sensor.h](sensor_8h.md)>

21

[ 22](wsen__hids__2525020210002_8h.md#aac9a11a8c10c720779a31b56b59dda47)enum [sensor\_attribute\_wsen\_hids\_2525020210002](wsen__hids__2525020210002_8h.md#aac9a11a8c10c720779a31b56b59dda47) {

[ 23](wsen__hids__2525020210002_8h.md#aac9a11a8c10c720779a31b56b59dda47ab3cc193216192e9c3bb349c8cdb6955a) [SENSOR\_ATTR\_WSEN\_HIDS\_2525020210002\_PRECISION](wsen__hids__2525020210002_8h.md#aac9a11a8c10c720779a31b56b59dda47ab3cc193216192e9c3bb349c8cdb6955a) = [SENSOR\_ATTR\_PRIV\_START](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940bafb4b5859bc369f817f60eaa161bcefc3),

[ 24](wsen__hids__2525020210002_8h.md#aac9a11a8c10c720779a31b56b59dda47a4a256cd71be3c93fa1efa5eb6c4e11dd) [SENSOR\_ATTR\_WSEN\_HIDS\_2525020210002\_HEATER](wsen__hids__2525020210002_8h.md#aac9a11a8c10c720779a31b56b59dda47a4a256cd71be3c93fa1efa5eb6c4e11dd)

25};

26

[ 27](wsen__hids__2525020210002_8h.md#a5cbc99af974e11d6a0095139c9d53745)typedef enum {

[ 28](wsen__hids__2525020210002_8h.md#a5cbc99af974e11d6a0095139c9d53745a34a2ff586fb0eb69e5dca23672f8c214) [hids\_2525020210002\_precision\_Low](wsen__hids__2525020210002_8h.md#a5cbc99af974e11d6a0095139c9d53745a34a2ff586fb0eb69e5dca23672f8c214) = 0x0,

[ 29](wsen__hids__2525020210002_8h.md#a5cbc99af974e11d6a0095139c9d53745aa5c2cf7ca07538112d21a9cb7872e524) [hids\_2525020210002\_precision\_Medium](wsen__hids__2525020210002_8h.md#a5cbc99af974e11d6a0095139c9d53745aa5c2cf7ca07538112d21a9cb7872e524) = 0x1,

[ 30](wsen__hids__2525020210002_8h.md#a5cbc99af974e11d6a0095139c9d53745ae3ba827aa8733b0e376f9e61967d5df7) [hids\_2525020210002\_precision\_High](wsen__hids__2525020210002_8h.md#a5cbc99af974e11d6a0095139c9d53745ae3ba827aa8733b0e376f9e61967d5df7) = 0x2

31} [hids\_2525020210002\_precision\_t](wsen__hids__2525020210002_8h.md#a5cbc99af974e11d6a0095139c9d53745);

32

[ 33](wsen__hids__2525020210002_8h.md#a043e3bd14c15c3a9a2bacc1e78f7f317)typedef enum {

[ 34](wsen__hids__2525020210002_8h.md#a043e3bd14c15c3a9a2bacc1e78f7f317aea95bf7ef0fa2430b6aad668b6b244d7) [hids\_2525020210002\_heater\_Off](wsen__hids__2525020210002_8h.md#a043e3bd14c15c3a9a2bacc1e78f7f317aea95bf7ef0fa2430b6aad668b6b244d7) = 0x0,

[ 35](wsen__hids__2525020210002_8h.md#a043e3bd14c15c3a9a2bacc1e78f7f317a15b9a389d72e7d338d7e8cf8c171ff35) [hids\_2525020210002\_heater\_On\_200mW\_1s](wsen__hids__2525020210002_8h.md#a043e3bd14c15c3a9a2bacc1e78f7f317a15b9a389d72e7d338d7e8cf8c171ff35) = 0x1,

[ 36](wsen__hids__2525020210002_8h.md#a043e3bd14c15c3a9a2bacc1e78f7f317a030f5cad08959fdc084ba943ac392a48) [hids\_2525020210002\_heater\_On\_200mW\_100ms](wsen__hids__2525020210002_8h.md#a043e3bd14c15c3a9a2bacc1e78f7f317a030f5cad08959fdc084ba943ac392a48) = 0x2,

[ 37](wsen__hids__2525020210002_8h.md#a043e3bd14c15c3a9a2bacc1e78f7f317aa0e704349b9568e5fd4bbd60156c64be) [hids\_2525020210002\_heater\_On\_110mW\_1s](wsen__hids__2525020210002_8h.md#a043e3bd14c15c3a9a2bacc1e78f7f317aa0e704349b9568e5fd4bbd60156c64be) = 0x3,

[ 38](wsen__hids__2525020210002_8h.md#a043e3bd14c15c3a9a2bacc1e78f7f317a38b108fbe099aaaf48f7a11e81b119bc) [hids\_2525020210002\_heater\_On\_110mW\_100ms](wsen__hids__2525020210002_8h.md#a043e3bd14c15c3a9a2bacc1e78f7f317a38b108fbe099aaaf48f7a11e81b119bc) = 0x4,

[ 39](wsen__hids__2525020210002_8h.md#a043e3bd14c15c3a9a2bacc1e78f7f317aa713ff24dde4522352ac7bf636b7d7c3) [hids\_2525020210002\_heater\_On\_20mW\_1s](wsen__hids__2525020210002_8h.md#a043e3bd14c15c3a9a2bacc1e78f7f317aa713ff24dde4522352ac7bf636b7d7c3) = 0x5,

[ 40](wsen__hids__2525020210002_8h.md#a043e3bd14c15c3a9a2bacc1e78f7f317a2500b161f1b08b26f68b2f9e5ac6098d) [hids\_2525020210002\_heater\_On\_20mW\_100ms](wsen__hids__2525020210002_8h.md#a043e3bd14c15c3a9a2bacc1e78f7f317a2500b161f1b08b26f68b2f9e5ac6098d) = 0x6,

41} [hids\_2525020210002\_heater\_t](wsen__hids__2525020210002_8h.md#a043e3bd14c15c3a9a2bacc1e78f7f317);

42

43#ifdef \_\_cplusplus

44}

45#endif

46

47#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_SENSOR\_WSEN\_HIDS\_2525020210002\_H\_ \*/

[SENSOR\_ATTR\_PRIV\_START](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940bafb4b5859bc369f817f60eaa161bcefc3)

@ SENSOR\_ATTR\_PRIV\_START

This and higher values are sensor specific.

**Definition** sensor.h:359

[sensor.h](sensor_8h.md)

Public APIs for the sensor driver.

[hids\_2525020210002\_heater\_t](wsen__hids__2525020210002_8h.md#a043e3bd14c15c3a9a2bacc1e78f7f317)

hids\_2525020210002\_heater\_t

**Definition** wsen\_hids\_2525020210002.h:33

[hids\_2525020210002\_heater\_On\_200mW\_100ms](wsen__hids__2525020210002_8h.md#a043e3bd14c15c3a9a2bacc1e78f7f317a030f5cad08959fdc084ba943ac392a48)

@ hids\_2525020210002\_heater\_On\_200mW\_100ms

**Definition** wsen\_hids\_2525020210002.h:36

[hids\_2525020210002\_heater\_On\_200mW\_1s](wsen__hids__2525020210002_8h.md#a043e3bd14c15c3a9a2bacc1e78f7f317a15b9a389d72e7d338d7e8cf8c171ff35)

@ hids\_2525020210002\_heater\_On\_200mW\_1s

**Definition** wsen\_hids\_2525020210002.h:35

[hids\_2525020210002\_heater\_On\_20mW\_100ms](wsen__hids__2525020210002_8h.md#a043e3bd14c15c3a9a2bacc1e78f7f317a2500b161f1b08b26f68b2f9e5ac6098d)

@ hids\_2525020210002\_heater\_On\_20mW\_100ms

**Definition** wsen\_hids\_2525020210002.h:40

[hids\_2525020210002\_heater\_On\_110mW\_100ms](wsen__hids__2525020210002_8h.md#a043e3bd14c15c3a9a2bacc1e78f7f317a38b108fbe099aaaf48f7a11e81b119bc)

@ hids\_2525020210002\_heater\_On\_110mW\_100ms

**Definition** wsen\_hids\_2525020210002.h:38

[hids\_2525020210002\_heater\_On\_110mW\_1s](wsen__hids__2525020210002_8h.md#a043e3bd14c15c3a9a2bacc1e78f7f317aa0e704349b9568e5fd4bbd60156c64be)

@ hids\_2525020210002\_heater\_On\_110mW\_1s

**Definition** wsen\_hids\_2525020210002.h:37

[hids\_2525020210002\_heater\_On\_20mW\_1s](wsen__hids__2525020210002_8h.md#a043e3bd14c15c3a9a2bacc1e78f7f317aa713ff24dde4522352ac7bf636b7d7c3)

@ hids\_2525020210002\_heater\_On\_20mW\_1s

**Definition** wsen\_hids\_2525020210002.h:39

[hids\_2525020210002\_heater\_Off](wsen__hids__2525020210002_8h.md#a043e3bd14c15c3a9a2bacc1e78f7f317aea95bf7ef0fa2430b6aad668b6b244d7)

@ hids\_2525020210002\_heater\_Off

**Definition** wsen\_hids\_2525020210002.h:34

[hids\_2525020210002\_precision\_t](wsen__hids__2525020210002_8h.md#a5cbc99af974e11d6a0095139c9d53745)

hids\_2525020210002\_precision\_t

**Definition** wsen\_hids\_2525020210002.h:27

[hids\_2525020210002\_precision\_Low](wsen__hids__2525020210002_8h.md#a5cbc99af974e11d6a0095139c9d53745a34a2ff586fb0eb69e5dca23672f8c214)

@ hids\_2525020210002\_precision\_Low

**Definition** wsen\_hids\_2525020210002.h:28

[hids\_2525020210002\_precision\_Medium](wsen__hids__2525020210002_8h.md#a5cbc99af974e11d6a0095139c9d53745aa5c2cf7ca07538112d21a9cb7872e524)

@ hids\_2525020210002\_precision\_Medium

**Definition** wsen\_hids\_2525020210002.h:29

[hids\_2525020210002\_precision\_High](wsen__hids__2525020210002_8h.md#a5cbc99af974e11d6a0095139c9d53745ae3ba827aa8733b0e376f9e61967d5df7)

@ hids\_2525020210002\_precision\_High

**Definition** wsen\_hids\_2525020210002.h:30

[sensor\_attribute\_wsen\_hids\_2525020210002](wsen__hids__2525020210002_8h.md#aac9a11a8c10c720779a31b56b59dda47)

sensor\_attribute\_wsen\_hids\_2525020210002

**Definition** wsen\_hids\_2525020210002.h:22

[SENSOR\_ATTR\_WSEN\_HIDS\_2525020210002\_HEATER](wsen__hids__2525020210002_8h.md#aac9a11a8c10c720779a31b56b59dda47a4a256cd71be3c93fa1efa5eb6c4e11dd)

@ SENSOR\_ATTR\_WSEN\_HIDS\_2525020210002\_HEATER

**Definition** wsen\_hids\_2525020210002.h:24

[SENSOR\_ATTR\_WSEN\_HIDS\_2525020210002\_PRECISION](wsen__hids__2525020210002_8h.md#aac9a11a8c10c720779a31b56b59dda47ab3cc193216192e9c3bb349c8cdb6955a)

@ SENSOR\_ATTR\_WSEN\_HIDS\_2525020210002\_PRECISION

**Definition** wsen\_hids\_2525020210002.h:23

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [sensor](dir_b6423b3a8fc1c9278ff19cba182cfe6d.md)
- [wsen\_hids\_2525020210002.h](wsen__hids__2525020210002_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
