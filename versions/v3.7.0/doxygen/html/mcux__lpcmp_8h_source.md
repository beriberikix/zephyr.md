---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/mcux__lpcmp_8h_source.html
original_path: doxygen/html/mcux__lpcmp_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mcux\_lpcmp.h

[Go to the documentation of this file.](mcux__lpcmp_8h.md)

1/\*

2 \* Copyright (c) 2020 Vestas Wind Systems A/S

3 \* Copyright 2024 NXP

4 \*

5 \* SPDX-License-Identifier: Apache-2.0

6 \*/

7

12

13#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_SENSOR\_MCUX\_LPCMP\_H\_

14#define ZEPHYR\_INCLUDE\_DRIVERS\_SENSOR\_MCUX\_LPCMP\_H\_

15

16#ifdef \_\_cplusplus

17extern "C" {

18#endif

19

20#include <[zephyr/drivers/sensor.h](sensor_8h.md)>

21

[ 25](mcux__lpcmp_8h.md#a0afc296fa89b7bdd31105574f459fb5a)enum [sensor\_channel\_mcux\_lpcmp](mcux__lpcmp_8h.md#a0afc296fa89b7bdd31105574f459fb5a) {

[ 27](mcux__lpcmp_8h.md#a0afc296fa89b7bdd31105574f459fb5aad1561ee6f508b72ad743971d60bb9d87) [SENSOR\_CHAN\_MCUX\_LPCMP\_OUTPUT](mcux__lpcmp_8h.md#a0afc296fa89b7bdd31105574f459fb5aad1561ee6f508b72ad743971d60bb9d87) = [SENSOR\_CHAN\_PRIV\_START](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934ac1f260296289d93a13c5686ca11bdc12),

28};

29

[ 33](mcux__lpcmp_8h.md#ad86c67639b0a919fd5ea0b5b6a3d4cd6)enum [sensor\_trigger\_type\_mcux\_lpcmp](mcux__lpcmp_8h.md#ad86c67639b0a919fd5ea0b5b6a3d4cd6) {

[ 35](mcux__lpcmp_8h.md#ad86c67639b0a919fd5ea0b5b6a3d4cd6a8a221bd8580a353cd4edf38a3c217e7e) [SENSOR\_TRIG\_MCUX\_LPCMP\_OUTPUT\_RISING](mcux__lpcmp_8h.md#ad86c67639b0a919fd5ea0b5b6a3d4cd6a8a221bd8580a353cd4edf38a3c217e7e) = [SENSOR\_TRIG\_PRIV\_START](group__sensor__interface.md#gga08215279400e8c9eb05ce4e4f0898ffda5e1a94f21fee67ee98296153ea640921),

[ 37](mcux__lpcmp_8h.md#ad86c67639b0a919fd5ea0b5b6a3d4cd6a002b0d7bd234a6bece9b8baae411f1e9) [SENSOR\_TRIG\_MCUX\_LPCMP\_OUTPUT\_FALLING](mcux__lpcmp_8h.md#ad86c67639b0a919fd5ea0b5b6a3d4cd6a002b0d7bd234a6bece9b8baae411f1e9),

38};

39

[ 43](mcux__lpcmp_8h.md#a8104360e57e8d294fb6bd02812fcc03e)enum [sensor\_attribute\_mcux\_lpcmp](mcux__lpcmp_8h.md#a8104360e57e8d294fb6bd02812fcc03e) {

[ 45](mcux__lpcmp_8h.md#a8104360e57e8d294fb6bd02812fcc03ea595f556e4cefb69c33cf94e9e0cb8eab) [SENSOR\_ATTR\_MCUX\_LPCMP\_POSITIVE\_MUX\_INPUT](mcux__lpcmp_8h.md#a8104360e57e8d294fb6bd02812fcc03ea595f556e4cefb69c33cf94e9e0cb8eab) = [SENSOR\_ATTR\_COMMON\_COUNT](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940ba99ceedef81217614ada0c8a469f91eb8),

[ 47](mcux__lpcmp_8h.md#a8104360e57e8d294fb6bd02812fcc03ea121200848c3ec07ced3979af7e186e52) [SENSOR\_ATTR\_MCUX\_LPCMP\_NEGATIVE\_MUX\_INPUT](mcux__lpcmp_8h.md#a8104360e57e8d294fb6bd02812fcc03ea121200848c3ec07ced3979af7e186e52),

48

[ 54](mcux__lpcmp_8h.md#a8104360e57e8d294fb6bd02812fcc03ea5a50fc0d49b328f0475e145877922dd7) [SENSOR\_ATTR\_MCUX\_LPCMP\_DAC\_ENABLE](mcux__lpcmp_8h.md#a8104360e57e8d294fb6bd02812fcc03ea5a50fc0d49b328f0475e145877922dd7),

[ 60](mcux__lpcmp_8h.md#a8104360e57e8d294fb6bd02812fcc03ea0e0d40713788ceede8492bca750c9574) [SENSOR\_ATTR\_MCUX\_LPCMP\_DAC\_HIGH\_POWER\_MODE\_ENABLE](mcux__lpcmp_8h.md#a8104360e57e8d294fb6bd02812fcc03ea0e0d40713788ceede8492bca750c9574),

[ 62](mcux__lpcmp_8h.md#a8104360e57e8d294fb6bd02812fcc03ea5eb0fe730a64c50ca6bfec6b99090b01) [SENSOR\_ATTR\_MCUX\_LPCMP\_DAC\_REFERENCE\_VOLTAGE\_SOURCE](mcux__lpcmp_8h.md#a8104360e57e8d294fb6bd02812fcc03ea5eb0fe730a64c50ca6bfec6b99090b01),

[ 64](mcux__lpcmp_8h.md#a8104360e57e8d294fb6bd02812fcc03eabaf75089237d3f692504b7b491bddbd9) [SENSOR\_ATTR\_MCUX\_LPCMP\_DAC\_OUTPUT\_VOLTAGE](mcux__lpcmp_8h.md#a8104360e57e8d294fb6bd02812fcc03eabaf75089237d3f692504b7b491bddbd9),

65

[ 67](mcux__lpcmp_8h.md#a8104360e57e8d294fb6bd02812fcc03ea63ae262c76b0def09bebf9f760558d66) [SENSOR\_ATTR\_MCUX\_LPCMP\_SAMPLE\_ENABLE](mcux__lpcmp_8h.md#a8104360e57e8d294fb6bd02812fcc03ea63ae262c76b0def09bebf9f760558d66),

[ 69](mcux__lpcmp_8h.md#a8104360e57e8d294fb6bd02812fcc03ea853df07e6a142095a6f64024f7bb9e03) [SENSOR\_ATTR\_MCUX\_LPCMP\_FILTER\_COUNT](mcux__lpcmp_8h.md#a8104360e57e8d294fb6bd02812fcc03ea853df07e6a142095a6f64024f7bb9e03),

[ 71](mcux__lpcmp_8h.md#a8104360e57e8d294fb6bd02812fcc03ea19a4a2f184cbb2c32300dd2eb436e4fa) [SENSOR\_ATTR\_MCUX\_LPCMP\_FILTER\_PERIOD](mcux__lpcmp_8h.md#a8104360e57e8d294fb6bd02812fcc03ea19a4a2f184cbb2c32300dd2eb436e4fa),

72

[ 74](mcux__lpcmp_8h.md#a8104360e57e8d294fb6bd02812fcc03ea788ac8f0f9bbfd215601090d0653b12e) [SENSOR\_ATTR\_MCUX\_LPCMP\_COUTA\_WINDOW\_ENABLE](mcux__lpcmp_8h.md#a8104360e57e8d294fb6bd02812fcc03ea788ac8f0f9bbfd215601090d0653b12e),

[ 76](mcux__lpcmp_8h.md#a8104360e57e8d294fb6bd02812fcc03ea620c4eabae0fc9bfaaf2999a4c4b22cf) [SENSOR\_ATTR\_MCUX\_LPCMP\_COUTA\_WINDOW\_SIGNAL\_INVERT\_ENABLE](mcux__lpcmp_8h.md#a8104360e57e8d294fb6bd02812fcc03ea620c4eabae0fc9bfaaf2999a4c4b22cf),

[ 83](mcux__lpcmp_8h.md#a8104360e57e8d294fb6bd02812fcc03ea8189889b48c2cd89feb78fc84d33805a) [SENSOR\_ATTR\_MCUX\_LPCMP\_COUTA\_SIGNAL](mcux__lpcmp_8h.md#a8104360e57e8d294fb6bd02812fcc03ea8189889b48c2cd89feb78fc84d33805a),

[ 91](mcux__lpcmp_8h.md#a8104360e57e8d294fb6bd02812fcc03ea0b7d5ec19095284f15e55a3054e849b4) [SENSOR\_ATTR\_MCUX\_LPCMP\_COUT\_EVENT\_TO\_CLOSE\_WINDOW](mcux__lpcmp_8h.md#a8104360e57e8d294fb6bd02812fcc03ea0b7d5ec19095284f15e55a3054e849b4)

92};

93

94#ifdef \_\_cplusplus

95}

96#endif

97

98#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_SENSOR\_MCUX\_LPCMP\_H\_ \*/

[SENSOR\_TRIG\_PRIV\_START](group__sensor__interface.md#gga08215279400e8c9eb05ce4e4f0898ffda5e1a94f21fee67ee98296153ea640921)

@ SENSOR\_TRIG\_PRIV\_START

This and higher values are sensor specific.

**Definition** sensor.h:275

[SENSOR\_ATTR\_COMMON\_COUNT](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940ba99ceedef81217614ada0c8a469f91eb8)

@ SENSOR\_ATTR\_COMMON\_COUNT

Number of all common sensor attributes.

**Definition** sensor.h:350

[SENSOR\_CHAN\_PRIV\_START](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934ac1f260296289d93a13c5686ca11bdc12)

@ SENSOR\_CHAN\_PRIV\_START

This and higher values are sensor specific.

**Definition** sensor.h:208

[sensor\_channel\_mcux\_lpcmp](mcux__lpcmp_8h.md#a0afc296fa89b7bdd31105574f459fb5a)

sensor\_channel\_mcux\_lpcmp

lpcmp channels.

**Definition** mcux\_lpcmp.h:25

[SENSOR\_CHAN\_MCUX\_LPCMP\_OUTPUT](mcux__lpcmp_8h.md#a0afc296fa89b7bdd31105574f459fb5aad1561ee6f508b72ad743971d60bb9d87)

@ SENSOR\_CHAN\_MCUX\_LPCMP\_OUTPUT

LPCMP output.

**Definition** mcux\_lpcmp.h:27

[sensor\_attribute\_mcux\_lpcmp](mcux__lpcmp_8h.md#a8104360e57e8d294fb6bd02812fcc03e)

sensor\_attribute\_mcux\_lpcmp

lpcmp attribute types.

**Definition** mcux\_lpcmp.h:43

[SENSOR\_ATTR\_MCUX\_LPCMP\_COUT\_EVENT\_TO\_CLOSE\_WINDOW](mcux__lpcmp_8h.md#a8104360e57e8d294fb6bd02812fcc03ea0b7d5ec19095284f15e55a3054e849b4)

@ SENSOR\_ATTR\_MCUX\_LPCMP\_COUT\_EVENT\_TO\_CLOSE\_WINDOW

LPCMP COUT event to close an active window: xx0b: COUT event cannot close an active window 001b: COUT...

**Definition** mcux\_lpcmp.h:91

[SENSOR\_ATTR\_MCUX\_LPCMP\_DAC\_HIGH\_POWER\_MODE\_ENABLE](mcux__lpcmp_8h.md#a8104360e57e8d294fb6bd02812fcc03ea0e0d40713788ceede8492bca750c9574)

@ SENSOR\_ATTR\_MCUX\_LPCMP\_DAC\_HIGH\_POWER\_MODE\_ENABLE

LPCMP internal DAC high power mode disabled.

**Definition** mcux\_lpcmp.h:60

[SENSOR\_ATTR\_MCUX\_LPCMP\_NEGATIVE\_MUX\_INPUT](mcux__lpcmp_8h.md#a8104360e57e8d294fb6bd02812fcc03ea121200848c3ec07ced3979af7e186e52)

@ SENSOR\_ATTR\_MCUX\_LPCMP\_NEGATIVE\_MUX\_INPUT

LPCMP negative input mux.

**Definition** mcux\_lpcmp.h:47

[SENSOR\_ATTR\_MCUX\_LPCMP\_FILTER\_PERIOD](mcux__lpcmp_8h.md#a8104360e57e8d294fb6bd02812fcc03ea19a4a2f184cbb2c32300dd2eb436e4fa)

@ SENSOR\_ATTR\_MCUX\_LPCMP\_FILTER\_PERIOD

LPCMP internal filter sample period.

**Definition** mcux\_lpcmp.h:71

[SENSOR\_ATTR\_MCUX\_LPCMP\_POSITIVE\_MUX\_INPUT](mcux__lpcmp_8h.md#a8104360e57e8d294fb6bd02812fcc03ea595f556e4cefb69c33cf94e9e0cb8eab)

@ SENSOR\_ATTR\_MCUX\_LPCMP\_POSITIVE\_MUX\_INPUT

LPCMP positive input mux.

**Definition** mcux\_lpcmp.h:45

[SENSOR\_ATTR\_MCUX\_LPCMP\_DAC\_ENABLE](mcux__lpcmp_8h.md#a8104360e57e8d294fb6bd02812fcc03ea5a50fc0d49b328f0475e145877922dd7)

@ SENSOR\_ATTR\_MCUX\_LPCMP\_DAC\_ENABLE

LPCMP internal DAC enable.

**Definition** mcux\_lpcmp.h:54

[SENSOR\_ATTR\_MCUX\_LPCMP\_DAC\_REFERENCE\_VOLTAGE\_SOURCE](mcux__lpcmp_8h.md#a8104360e57e8d294fb6bd02812fcc03ea5eb0fe730a64c50ca6bfec6b99090b01)

@ SENSOR\_ATTR\_MCUX\_LPCMP\_DAC\_REFERENCE\_VOLTAGE\_SOURCE

LPCMP internal DAC voltage reference source.

**Definition** mcux\_lpcmp.h:62

[SENSOR\_ATTR\_MCUX\_LPCMP\_COUTA\_WINDOW\_SIGNAL\_INVERT\_ENABLE](mcux__lpcmp_8h.md#a8104360e57e8d294fb6bd02812fcc03ea620c4eabae0fc9bfaaf2999a4c4b22cf)

@ SENSOR\_ATTR\_MCUX\_LPCMP\_COUTA\_WINDOW\_SIGNAL\_INVERT\_ENABLE

LPCMP window signal invert.

**Definition** mcux\_lpcmp.h:76

[SENSOR\_ATTR\_MCUX\_LPCMP\_SAMPLE\_ENABLE](mcux__lpcmp_8h.md#a8104360e57e8d294fb6bd02812fcc03ea63ae262c76b0def09bebf9f760558d66)

@ SENSOR\_ATTR\_MCUX\_LPCMP\_SAMPLE\_ENABLE

LPCMP internal filter sample enable.

**Definition** mcux\_lpcmp.h:67

[SENSOR\_ATTR\_MCUX\_LPCMP\_COUTA\_WINDOW\_ENABLE](mcux__lpcmp_8h.md#a8104360e57e8d294fb6bd02812fcc03ea788ac8f0f9bbfd215601090d0653b12e)

@ SENSOR\_ATTR\_MCUX\_LPCMP\_COUTA\_WINDOW\_ENABLE

LPCMP window signal invert.

**Definition** mcux\_lpcmp.h:74

[SENSOR\_ATTR\_MCUX\_LPCMP\_COUTA\_SIGNAL](mcux__lpcmp_8h.md#a8104360e57e8d294fb6bd02812fcc03ea8189889b48c2cd89feb78fc84d33805a)

@ SENSOR\_ATTR\_MCUX\_LPCMP\_COUTA\_SIGNAL

LPCMP COUTA signal value when a window is closed: 00b: latched 01b: set to low 11b: set to high.

**Definition** mcux\_lpcmp.h:83

[SENSOR\_ATTR\_MCUX\_LPCMP\_FILTER\_COUNT](mcux__lpcmp_8h.md#a8104360e57e8d294fb6bd02812fcc03ea853df07e6a142095a6f64024f7bb9e03)

@ SENSOR\_ATTR\_MCUX\_LPCMP\_FILTER\_COUNT

LPCMP internal filter sample count.

**Definition** mcux\_lpcmp.h:69

[SENSOR\_ATTR\_MCUX\_LPCMP\_DAC\_OUTPUT\_VOLTAGE](mcux__lpcmp_8h.md#a8104360e57e8d294fb6bd02812fcc03eabaf75089237d3f692504b7b491bddbd9)

@ SENSOR\_ATTR\_MCUX\_LPCMP\_DAC\_OUTPUT\_VOLTAGE

LPCMP internal DAC output voltage value.

**Definition** mcux\_lpcmp.h:64

[sensor\_trigger\_type\_mcux\_lpcmp](mcux__lpcmp_8h.md#ad86c67639b0a919fd5ea0b5b6a3d4cd6)

sensor\_trigger\_type\_mcux\_lpcmp

lpcmp trigger types.

**Definition** mcux\_lpcmp.h:33

[SENSOR\_TRIG\_MCUX\_LPCMP\_OUTPUT\_FALLING](mcux__lpcmp_8h.md#ad86c67639b0a919fd5ea0b5b6a3d4cd6a002b0d7bd234a6bece9b8baae411f1e9)

@ SENSOR\_TRIG\_MCUX\_LPCMP\_OUTPUT\_FALLING

LPCMP output falling event trigger.

**Definition** mcux\_lpcmp.h:37

[SENSOR\_TRIG\_MCUX\_LPCMP\_OUTPUT\_RISING](mcux__lpcmp_8h.md#ad86c67639b0a919fd5ea0b5b6a3d4cd6a8a221bd8580a353cd4edf38a3c217e7e)

@ SENSOR\_TRIG\_MCUX\_LPCMP\_OUTPUT\_RISING

LPCMP output rising event trigger.

**Definition** mcux\_lpcmp.h:35

[sensor.h](sensor_8h.md)

Public APIs for the sensor driver.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [sensor](dir_b6423b3a8fc1c9278ff19cba182cfe6d.md)
- [mcux\_lpcmp.h](mcux__lpcmp_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
