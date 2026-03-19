---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/sensor_2mcux__acmp_8h_source.html
original_path: doxygen/html/sensor_2mcux__acmp_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mcux\_acmp.h

[Go to the documentation of this file.](sensor_2mcux__acmp_8h.md)

1/\*

2 \* Copyright (c) 2020 Vestas Wind Systems A/S

3 \* Copyright 2022, 2024 NXP

4 \*

5 \* SPDX-License-Identifier: Apache-2.0

6 \*/

7

12

13#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_SENSOR\_MCUX\_ACMP\_H\_

14#define ZEPHYR\_INCLUDE\_DRIVERS\_SENSOR\_MCUX\_ACMP\_H\_

15

16#ifdef \_\_cplusplus

17extern "C" {

18#endif

19

20#include <[zephyr/drivers/sensor.h](sensor_8h.md)>

21

22#if defined(FSL\_FEATURE\_ACMP\_HAS\_C1\_INPSEL\_BIT) && (FSL\_FEATURE\_ACMP\_HAS\_C1\_INPSEL\_BIT == 1U)

23#define MCUX\_ACMP\_HAS\_INPSEL 1

24#else

[ 25](sensor_2mcux__acmp_8h.md#a25badb86c21dac89b1fdf3462726e487)#define MCUX\_ACMP\_HAS\_INPSEL 0

26#endif

27

28#if defined(FSL\_FEATURE\_ACMP\_HAS\_C1\_INNSEL\_BIT) && (FSL\_FEATURE\_ACMP\_HAS\_C1\_INNSEL\_BIT == 1U)

29#define MCUX\_ACMP\_HAS\_INNSEL 1

30#else

[ 31](sensor_2mcux__acmp_8h.md#a7d2ec98ad2d468666974905de3593852)#define MCUX\_ACMP\_HAS\_INNSEL 0

32#endif

33

34#if defined(FSL\_FEATURE\_ACMP\_HAS\_C0\_OFFSET\_BIT) && (FSL\_FEATURE\_ACMP\_HAS\_C0\_OFFSET\_BIT == 1U)

35#define MCUX\_ACMP\_HAS\_OFFSET 1

36#else

[ 37](sensor_2mcux__acmp_8h.md#a600499ad6c1ab652febb864c90c17574)#define MCUX\_ACMP\_HAS\_OFFSET 0

38#endif

39

40#if defined(FSL\_FEATURE\_ACMP\_HAS\_C3\_REG) && (FSL\_FEATURE\_ACMP\_HAS\_C3\_REG != 0U)

41#define MCUX\_ACMP\_HAS\_DISCRETE\_MODE 1

42#else

[ 43](sensor_2mcux__acmp_8h.md#ab8101cc404679700315d6a4fea729e24)#define MCUX\_ACMP\_HAS\_DISCRETE\_MODE 0

44#endif

45

46#if defined(FSL\_FEATURE\_ACMP\_HAS\_C0\_HYSTCTR\_BIT) && (FSL\_FEATURE\_ACMP\_HAS\_C0\_HYSTCTR\_BIT == 1U)

47#define MCUX\_ACMP\_HAS\_HYSTCTR 1

48#else

[ 49](sensor_2mcux__acmp_8h.md#ab2efc4cf8c2b85a7b8616faadaeee583)#define MCUX\_ACMP\_HAS\_HYSTCTR 0

50#endif

51

[ 52](sensor_2mcux__acmp_8h.md#a017d1a028479db7f49a1327814fe72da)enum [sensor\_channel\_mcux\_acmp](sensor_2mcux__acmp_8h.md#a017d1a028479db7f49a1327814fe72da) {

[ 54](sensor_2mcux__acmp_8h.md#a017d1a028479db7f49a1327814fe72daa249515617e8c5017591017dcc076614d) [SENSOR\_CHAN\_MCUX\_ACMP\_OUTPUT](sensor_2mcux__acmp_8h.md#a017d1a028479db7f49a1327814fe72daa249515617e8c5017591017dcc076614d) = [SENSOR\_CHAN\_PRIV\_START](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934ac1f260296289d93a13c5686ca11bdc12),

55};

56

[ 57](sensor_2mcux__acmp_8h.md#af10919d10852c60efa9fb8d3fa56c829)enum [sensor\_trigger\_type\_mcux\_acmp](sensor_2mcux__acmp_8h.md#af10919d10852c60efa9fb8d3fa56c829) {

[ 59](sensor_2mcux__acmp_8h.md#af10919d10852c60efa9fb8d3fa56c829a808392257cdee8941e5cbafe480e4697) [SENSOR\_TRIG\_MCUX\_ACMP\_OUTPUT\_RISING](sensor_2mcux__acmp_8h.md#af10919d10852c60efa9fb8d3fa56c829a808392257cdee8941e5cbafe480e4697) = [SENSOR\_TRIG\_PRIV\_START](group__sensor__interface.md#gga08215279400e8c9eb05ce4e4f0898ffda5e1a94f21fee67ee98296153ea640921),

[ 61](sensor_2mcux__acmp_8h.md#af10919d10852c60efa9fb8d3fa56c829a6e0dd402df6647c13d0312cea7d4972d) [SENSOR\_TRIG\_MCUX\_ACMP\_OUTPUT\_FALLING](sensor_2mcux__acmp_8h.md#af10919d10852c60efa9fb8d3fa56c829a6e0dd402df6647c13d0312cea7d4972d),

62};

63

[ 64](sensor_2mcux__acmp_8h.md#a1e7a45b41695dede14a6b432ceb36daf)enum [sensor\_attribute\_mcux\_acmp](sensor_2mcux__acmp_8h.md#a1e7a45b41695dede14a6b432ceb36daf) {

[ 66](sensor_2mcux__acmp_8h.md#a1e7a45b41695dede14a6b432ceb36dafa2775a96b5738be33bead0d429edeb250) [SENSOR\_ATTR\_MCUX\_ACMP\_OFFSET\_LEVEL](sensor_2mcux__acmp_8h.md#a1e7a45b41695dede14a6b432ceb36dafa2775a96b5738be33bead0d429edeb250) = [SENSOR\_ATTR\_COMMON\_COUNT](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940ba99ceedef81217614ada0c8a469f91eb8),

[ 68](sensor_2mcux__acmp_8h.md#a1e7a45b41695dede14a6b432ceb36dafaf1f98be88dedc82ac02d8ac363a8e30c) [SENSOR\_ATTR\_MCUX\_ACMP\_HYSTERESIS\_LEVEL](sensor_2mcux__acmp_8h.md#a1e7a45b41695dede14a6b432ceb36dafaf1f98be88dedc82ac02d8ac363a8e30c),

[ 73](sensor_2mcux__acmp_8h.md#a1e7a45b41695dede14a6b432ceb36dafaef555e4535128d33d66a31041758b361) [SENSOR\_ATTR\_MCUX\_ACMP\_DAC\_VOLTAGE\_REFERENCE](sensor_2mcux__acmp_8h.md#a1e7a45b41695dede14a6b432ceb36dafaef555e4535128d33d66a31041758b361),

[ 75](sensor_2mcux__acmp_8h.md#a1e7a45b41695dede14a6b432ceb36dafa5b0fc158891b4f5da15d22cf46b8038d) [SENSOR\_ATTR\_MCUX\_ACMP\_DAC\_VALUE](sensor_2mcux__acmp_8h.md#a1e7a45b41695dede14a6b432ceb36dafa5b0fc158891b4f5da15d22cf46b8038d),

[ 77](sensor_2mcux__acmp_8h.md#a1e7a45b41695dede14a6b432ceb36dafa94b2b5d9ea4809c533f4c4f02f4f0000) [SENSOR\_ATTR\_MCUX\_ACMP\_POSITIVE\_PORT\_INPUT](sensor_2mcux__acmp_8h.md#a1e7a45b41695dede14a6b432ceb36dafa94b2b5d9ea4809c533f4c4f02f4f0000),

[ 79](sensor_2mcux__acmp_8h.md#a1e7a45b41695dede14a6b432ceb36dafab865cc40646af2eb05f0400e6d89c1a2) [SENSOR\_ATTR\_MCUX\_ACMP\_POSITIVE\_MUX\_INPUT](sensor_2mcux__acmp_8h.md#a1e7a45b41695dede14a6b432ceb36dafab865cc40646af2eb05f0400e6d89c1a2),

[ 81](sensor_2mcux__acmp_8h.md#a1e7a45b41695dede14a6b432ceb36dafa224855d60b92abd37e7418b7f73bbee6) [SENSOR\_ATTR\_MCUX\_ACMP\_NEGATIVE\_PORT\_INPUT](sensor_2mcux__acmp_8h.md#a1e7a45b41695dede14a6b432ceb36dafa224855d60b92abd37e7418b7f73bbee6),

[ 83](sensor_2mcux__acmp_8h.md#a1e7a45b41695dede14a6b432ceb36dafac3713c38d4654d0a9dd68f711d0c348b) [SENSOR\_ATTR\_MCUX\_ACMP\_NEGATIVE\_MUX\_INPUT](sensor_2mcux__acmp_8h.md#a1e7a45b41695dede14a6b432ceb36dafac3713c38d4654d0a9dd68f711d0c348b),

84#if MCUX\_ACMP\_HAS\_DISCRETE\_MODE

86 SENSOR\_ATTR\_MCUX\_ACMP\_POSITIVE\_DISCRETE\_MODE,

88 SENSOR\_ATTR\_MCUX\_ACMP\_NEGATIVE\_DISCRETE\_MODE,

90 SENSOR\_ATTR\_MCUX\_ACMP\_DISCRETE\_CLOCK,

92 SENSOR\_ATTR\_MCUX\_ACMP\_DISCRETE\_ENABLE\_RESISTOR\_DIVIDER,

94 SENSOR\_ATTR\_MCUX\_ACMP\_DISCRETE\_SAMPLE\_TIME,

96 SENSOR\_ATTR\_MCUX\_ACMP\_DISCRETE\_PHASE1\_TIME,

98 SENSOR\_ATTR\_MCUX\_ACMP\_DISCRETE\_PHASE2\_TIME,

99#endif

100};

101

102#ifdef \_\_cplusplus

103}

104#endif

105

106#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_SENSOR\_MCUX\_ACMP\_H\_ \*/

[SENSOR\_TRIG\_PRIV\_START](group__sensor__interface.md#gga08215279400e8c9eb05ce4e4f0898ffda5e1a94f21fee67ee98296153ea640921)

@ SENSOR\_TRIG\_PRIV\_START

This and higher values are sensor specific.

**Definition** sensor.h:284

[SENSOR\_ATTR\_COMMON\_COUNT](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940ba99ceedef81217614ada0c8a469f91eb8)

@ SENSOR\_ATTR\_COMMON\_COUNT

Number of all common sensor attributes.

**Definition** sensor.h:362

[SENSOR\_CHAN\_PRIV\_START](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934ac1f260296289d93a13c5686ca11bdc12)

@ SENSOR\_CHAN\_PRIV\_START

This and higher values are sensor specific.

**Definition** sensor.h:217

[sensor\_channel\_mcux\_acmp](sensor_2mcux__acmp_8h.md#a017d1a028479db7f49a1327814fe72da)

sensor\_channel\_mcux\_acmp

**Definition** mcux\_acmp.h:52

[SENSOR\_CHAN\_MCUX\_ACMP\_OUTPUT](sensor_2mcux__acmp_8h.md#a017d1a028479db7f49a1327814fe72daa249515617e8c5017591017dcc076614d)

@ SENSOR\_CHAN\_MCUX\_ACMP\_OUTPUT

Analog Comparator Output.

**Definition** mcux\_acmp.h:54

[sensor\_attribute\_mcux\_acmp](sensor_2mcux__acmp_8h.md#a1e7a45b41695dede14a6b432ceb36daf)

sensor\_attribute\_mcux\_acmp

**Definition** mcux\_acmp.h:64

[SENSOR\_ATTR\_MCUX\_ACMP\_NEGATIVE\_PORT\_INPUT](sensor_2mcux__acmp_8h.md#a1e7a45b41695dede14a6b432ceb36dafa224855d60b92abd37e7418b7f73bbee6)

@ SENSOR\_ATTR\_MCUX\_ACMP\_NEGATIVE\_PORT\_INPUT

Analog Comparator negative port input.

**Definition** mcux\_acmp.h:81

[SENSOR\_ATTR\_MCUX\_ACMP\_OFFSET\_LEVEL](sensor_2mcux__acmp_8h.md#a1e7a45b41695dede14a6b432ceb36dafa2775a96b5738be33bead0d429edeb250)

@ SENSOR\_ATTR\_MCUX\_ACMP\_OFFSET\_LEVEL

Analog Comparator hard block offset.

**Definition** mcux\_acmp.h:66

[SENSOR\_ATTR\_MCUX\_ACMP\_DAC\_VALUE](sensor_2mcux__acmp_8h.md#a1e7a45b41695dede14a6b432ceb36dafa5b0fc158891b4f5da15d22cf46b8038d)

@ SENSOR\_ATTR\_MCUX\_ACMP\_DAC\_VALUE

Analog Comparator Digital-to-Analog Converter value.

**Definition** mcux\_acmp.h:75

[SENSOR\_ATTR\_MCUX\_ACMP\_POSITIVE\_PORT\_INPUT](sensor_2mcux__acmp_8h.md#a1e7a45b41695dede14a6b432ceb36dafa94b2b5d9ea4809c533f4c4f02f4f0000)

@ SENSOR\_ATTR\_MCUX\_ACMP\_POSITIVE\_PORT\_INPUT

Analog Comparator positive port input.

**Definition** mcux\_acmp.h:77

[SENSOR\_ATTR\_MCUX\_ACMP\_POSITIVE\_MUX\_INPUT](sensor_2mcux__acmp_8h.md#a1e7a45b41695dede14a6b432ceb36dafab865cc40646af2eb05f0400e6d89c1a2)

@ SENSOR\_ATTR\_MCUX\_ACMP\_POSITIVE\_MUX\_INPUT

Analog Comparator positive mux input.

**Definition** mcux\_acmp.h:79

[SENSOR\_ATTR\_MCUX\_ACMP\_NEGATIVE\_MUX\_INPUT](sensor_2mcux__acmp_8h.md#a1e7a45b41695dede14a6b432ceb36dafac3713c38d4654d0a9dd68f711d0c348b)

@ SENSOR\_ATTR\_MCUX\_ACMP\_NEGATIVE\_MUX\_INPUT

Analog Comparator negative mux input.

**Definition** mcux\_acmp.h:83

[SENSOR\_ATTR\_MCUX\_ACMP\_DAC\_VOLTAGE\_REFERENCE](sensor_2mcux__acmp_8h.md#a1e7a45b41695dede14a6b432ceb36dafaef555e4535128d33d66a31041758b361)

@ SENSOR\_ATTR\_MCUX\_ACMP\_DAC\_VOLTAGE\_REFERENCE

Analog Comparator Digital-to-Analog Converter voltage reference source.

**Definition** mcux\_acmp.h:73

[SENSOR\_ATTR\_MCUX\_ACMP\_HYSTERESIS\_LEVEL](sensor_2mcux__acmp_8h.md#a1e7a45b41695dede14a6b432ceb36dafaf1f98be88dedc82ac02d8ac363a8e30c)

@ SENSOR\_ATTR\_MCUX\_ACMP\_HYSTERESIS\_LEVEL

Analog Comparator hysteresis level.

**Definition** mcux\_acmp.h:68

[sensor\_trigger\_type\_mcux\_acmp](sensor_2mcux__acmp_8h.md#af10919d10852c60efa9fb8d3fa56c829)

sensor\_trigger\_type\_mcux\_acmp

**Definition** mcux\_acmp.h:57

[SENSOR\_TRIG\_MCUX\_ACMP\_OUTPUT\_FALLING](sensor_2mcux__acmp_8h.md#af10919d10852c60efa9fb8d3fa56c829a6e0dd402df6647c13d0312cea7d4972d)

@ SENSOR\_TRIG\_MCUX\_ACMP\_OUTPUT\_FALLING

Analog Comparator Output falling event trigger.

**Definition** mcux\_acmp.h:61

[SENSOR\_TRIG\_MCUX\_ACMP\_OUTPUT\_RISING](sensor_2mcux__acmp_8h.md#af10919d10852c60efa9fb8d3fa56c829a808392257cdee8941e5cbafe480e4697)

@ SENSOR\_TRIG\_MCUX\_ACMP\_OUTPUT\_RISING

Analog Comparator Output rising event trigger.

**Definition** mcux\_acmp.h:59

[sensor.h](sensor_8h.md)

Public APIs for the sensor driver.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [sensor](dir_b6423b3a8fc1c9278ff19cba182cfe6d.md)
- [mcux\_acmp.h](sensor_2mcux__acmp_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
