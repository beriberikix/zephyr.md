---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/sensor_2mcux__acmp_8h.html
original_path: doxygen/html/sensor_2mcux__acmp_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mcux\_acmp.h File Reference

Extended public API for the NXP MCUX Analog Comparator (ACMP).
[More...](#details)

`#include <[zephyr/drivers/sensor.h](sensor_8h_source.md)>`

[Go to the source code of this file.](sensor_2mcux__acmp_8h_source.md)

| Macros | |
| --- | --- |
| #define | [MCUX\_ACMP\_HAS\_INPSEL](#a25badb86c21dac89b1fdf3462726e487)   0 |
| #define | [MCUX\_ACMP\_HAS\_INNSEL](#a7d2ec98ad2d468666974905de3593852)   0 |
| #define | [MCUX\_ACMP\_HAS\_OFFSET](#a600499ad6c1ab652febb864c90c17574)   0 |
| #define | [MCUX\_ACMP\_HAS\_DISCRETE\_MODE](#ab8101cc404679700315d6a4fea729e24)   0 |
| #define | [MCUX\_ACMP\_HAS\_HYSTCTR](#ab2efc4cf8c2b85a7b8616faadaeee583)   0 |

| Enumerations | |
| --- | --- |
| enum | [sensor\_channel\_mcux\_acmp](#a017d1a028479db7f49a1327814fe72da) { [SENSOR\_CHAN\_MCUX\_ACMP\_OUTPUT](#a017d1a028479db7f49a1327814fe72daa249515617e8c5017591017dcc076614d) = SENSOR\_CHAN\_PRIV\_START } |
| enum | [sensor\_trigger\_type\_mcux\_acmp](#af10919d10852c60efa9fb8d3fa56c829) { [SENSOR\_TRIG\_MCUX\_ACMP\_OUTPUT\_RISING](#af10919d10852c60efa9fb8d3fa56c829a808392257cdee8941e5cbafe480e4697) = SENSOR\_TRIG\_PRIV\_START , [SENSOR\_TRIG\_MCUX\_ACMP\_OUTPUT\_FALLING](#af10919d10852c60efa9fb8d3fa56c829a6e0dd402df6647c13d0312cea7d4972d) } |
| enum | [sensor\_attribute\_mcux\_acmp](#a1e7a45b41695dede14a6b432ceb36daf) {     [SENSOR\_ATTR\_MCUX\_ACMP\_OFFSET\_LEVEL](#a1e7a45b41695dede14a6b432ceb36dafa2775a96b5738be33bead0d429edeb250) = SENSOR\_ATTR\_COMMON\_COUNT , [SENSOR\_ATTR\_MCUX\_ACMP\_HYSTERESIS\_LEVEL](#a1e7a45b41695dede14a6b432ceb36dafaf1f98be88dedc82ac02d8ac363a8e30c) , [SENSOR\_ATTR\_MCUX\_ACMP\_DAC\_VOLTAGE\_REFERENCE](#a1e7a45b41695dede14a6b432ceb36dafaef555e4535128d33d66a31041758b361) , [SENSOR\_ATTR\_MCUX\_ACMP\_DAC\_VALUE](#a1e7a45b41695dede14a6b432ceb36dafa5b0fc158891b4f5da15d22cf46b8038d) ,     [SENSOR\_ATTR\_MCUX\_ACMP\_POSITIVE\_PORT\_INPUT](#a1e7a45b41695dede14a6b432ceb36dafa94b2b5d9ea4809c533f4c4f02f4f0000) , [SENSOR\_ATTR\_MCUX\_ACMP\_POSITIVE\_MUX\_INPUT](#a1e7a45b41695dede14a6b432ceb36dafab865cc40646af2eb05f0400e6d89c1a2) , [SENSOR\_ATTR\_MCUX\_ACMP\_NEGATIVE\_PORT\_INPUT](#a1e7a45b41695dede14a6b432ceb36dafa224855d60b92abd37e7418b7f73bbee6) , [SENSOR\_ATTR\_MCUX\_ACMP\_NEGATIVE\_MUX\_INPUT](#a1e7a45b41695dede14a6b432ceb36dafac3713c38d4654d0a9dd68f711d0c348b)   } |

## Detailed Description

Extended public API for the NXP MCUX Analog Comparator (ACMP).

## Macro Definition Documentation

## [◆ ](#ab8101cc404679700315d6a4fea729e24)MCUX\_ACMP\_HAS\_DISCRETE\_MODE

| #define MCUX\_ACMP\_HAS\_DISCRETE\_MODE   0 |
| --- |

## [◆ ](#ab2efc4cf8c2b85a7b8616faadaeee583)MCUX\_ACMP\_HAS\_HYSTCTR

| #define MCUX\_ACMP\_HAS\_HYSTCTR   0 |
| --- |

## [◆ ](#a7d2ec98ad2d468666974905de3593852)MCUX\_ACMP\_HAS\_INNSEL

| #define MCUX\_ACMP\_HAS\_INNSEL   0 |
| --- |

## [◆ ](#a25badb86c21dac89b1fdf3462726e487)MCUX\_ACMP\_HAS\_INPSEL

| #define MCUX\_ACMP\_HAS\_INPSEL   0 |
| --- |

## [◆ ](#a600499ad6c1ab652febb864c90c17574)MCUX\_ACMP\_HAS\_OFFSET

| #define MCUX\_ACMP\_HAS\_OFFSET   0 |
| --- |

## Enumeration Type Documentation

## [◆ ](#a1e7a45b41695dede14a6b432ceb36daf)sensor\_attribute\_mcux\_acmp

| enum [sensor\_attribute\_mcux\_acmp](#a1e7a45b41695dede14a6b432ceb36daf) |
| --- |

| Enumerator | |
| --- | --- |
| SENSOR\_ATTR\_MCUX\_ACMP\_OFFSET\_LEVEL | Analog Comparator hard block offset. |
| SENSOR\_ATTR\_MCUX\_ACMP\_HYSTERESIS\_LEVEL | Analog Comparator hysteresis level. |
| SENSOR\_ATTR\_MCUX\_ACMP\_DAC\_VOLTAGE\_REFERENCE | Analog Comparator Digital-to-Analog Converter voltage reference source. |
| SENSOR\_ATTR\_MCUX\_ACMP\_DAC\_VALUE | Analog Comparator Digital-to-Analog Converter value. |
| SENSOR\_ATTR\_MCUX\_ACMP\_POSITIVE\_PORT\_INPUT | Analog Comparator positive port input. |
| SENSOR\_ATTR\_MCUX\_ACMP\_POSITIVE\_MUX\_INPUT | Analog Comparator positive mux input. |
| SENSOR\_ATTR\_MCUX\_ACMP\_NEGATIVE\_PORT\_INPUT | Analog Comparator negative port input. |
| SENSOR\_ATTR\_MCUX\_ACMP\_NEGATIVE\_MUX\_INPUT | Analog Comparator negative mux input. |

## [◆ ](#a017d1a028479db7f49a1327814fe72da)sensor\_channel\_mcux\_acmp

| enum [sensor\_channel\_mcux\_acmp](#a017d1a028479db7f49a1327814fe72da) |
| --- |

| Enumerator | |
| --- | --- |
| SENSOR\_CHAN\_MCUX\_ACMP\_OUTPUT | Analog Comparator Output. |

## [◆ ](#af10919d10852c60efa9fb8d3fa56c829)sensor\_trigger\_type\_mcux\_acmp

| enum [sensor\_trigger\_type\_mcux\_acmp](#af10919d10852c60efa9fb8d3fa56c829) |
| --- |

| Enumerator | |
| --- | --- |
| SENSOR\_TRIG\_MCUX\_ACMP\_OUTPUT\_RISING | Analog Comparator Output rising event trigger. |
| SENSOR\_TRIG\_MCUX\_ACMP\_OUTPUT\_FALLING | Analog Comparator Output falling event trigger. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [sensor](dir_b6423b3a8fc1c9278ff19cba182cfe6d.md)
- [mcux\_acmp.h](sensor_2mcux__acmp_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
