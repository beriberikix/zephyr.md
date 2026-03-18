---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/mcux__lpcmp_8h.html
original_path: doxygen/html/mcux__lpcmp_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mcux\_lpcmp.h File Reference

Data structure for the NXP MCUX low-power analog comparator (LPCMP).
[More...](#details)

`#include <[zephyr/drivers/sensor.h](sensor_8h_source.md)>`

[Go to the source code of this file.](mcux__lpcmp_8h_source.md)

| Enumerations | |
| --- | --- |
| enum | [sensor\_channel\_mcux\_lpcmp](#a0afc296fa89b7bdd31105574f459fb5a) { [SENSOR\_CHAN\_MCUX\_LPCMP\_OUTPUT](#a0afc296fa89b7bdd31105574f459fb5aad1561ee6f508b72ad743971d60bb9d87) = SENSOR\_CHAN\_PRIV\_START } |
|  | lpcmp channels. [More...](#a0afc296fa89b7bdd31105574f459fb5a) |
| enum | [sensor\_trigger\_type\_mcux\_lpcmp](#ad86c67639b0a919fd5ea0b5b6a3d4cd6) { [SENSOR\_TRIG\_MCUX\_LPCMP\_OUTPUT\_RISING](#ad86c67639b0a919fd5ea0b5b6a3d4cd6a8a221bd8580a353cd4edf38a3c217e7e) = SENSOR\_TRIG\_PRIV\_START , [SENSOR\_TRIG\_MCUX\_LPCMP\_OUTPUT\_FALLING](#ad86c67639b0a919fd5ea0b5b6a3d4cd6a002b0d7bd234a6bece9b8baae411f1e9) } |
|  | lpcmp trigger types. [More...](#ad86c67639b0a919fd5ea0b5b6a3d4cd6) |
| enum | [sensor\_attribute\_mcux\_lpcmp](#a8104360e57e8d294fb6bd02812fcc03e) {     [SENSOR\_ATTR\_MCUX\_LPCMP\_POSITIVE\_MUX\_INPUT](#a8104360e57e8d294fb6bd02812fcc03ea595f556e4cefb69c33cf94e9e0cb8eab) = SENSOR\_ATTR\_COMMON\_COUNT , [SENSOR\_ATTR\_MCUX\_LPCMP\_NEGATIVE\_MUX\_INPUT](#a8104360e57e8d294fb6bd02812fcc03ea121200848c3ec07ced3979af7e186e52) , [SENSOR\_ATTR\_MCUX\_LPCMP\_DAC\_ENABLE](#a8104360e57e8d294fb6bd02812fcc03ea5a50fc0d49b328f0475e145877922dd7) , [SENSOR\_ATTR\_MCUX\_LPCMP\_DAC\_HIGH\_POWER\_MODE\_ENABLE](#a8104360e57e8d294fb6bd02812fcc03ea0e0d40713788ceede8492bca750c9574) ,     [SENSOR\_ATTR\_MCUX\_LPCMP\_DAC\_REFERENCE\_VOLTAGE\_SOURCE](#a8104360e57e8d294fb6bd02812fcc03ea5eb0fe730a64c50ca6bfec6b99090b01) , [SENSOR\_ATTR\_MCUX\_LPCMP\_DAC\_OUTPUT\_VOLTAGE](#a8104360e57e8d294fb6bd02812fcc03eabaf75089237d3f692504b7b491bddbd9) , [SENSOR\_ATTR\_MCUX\_LPCMP\_SAMPLE\_ENABLE](#a8104360e57e8d294fb6bd02812fcc03ea63ae262c76b0def09bebf9f760558d66) , [SENSOR\_ATTR\_MCUX\_LPCMP\_FILTER\_COUNT](#a8104360e57e8d294fb6bd02812fcc03ea853df07e6a142095a6f64024f7bb9e03) ,     [SENSOR\_ATTR\_MCUX\_LPCMP\_FILTER\_PERIOD](#a8104360e57e8d294fb6bd02812fcc03ea19a4a2f184cbb2c32300dd2eb436e4fa) , [SENSOR\_ATTR\_MCUX\_LPCMP\_COUTA\_WINDOW\_ENABLE](#a8104360e57e8d294fb6bd02812fcc03ea788ac8f0f9bbfd215601090d0653b12e) , [SENSOR\_ATTR\_MCUX\_LPCMP\_COUTA\_WINDOW\_SIGNAL\_INVERT\_ENABLE](#a8104360e57e8d294fb6bd02812fcc03ea620c4eabae0fc9bfaaf2999a4c4b22cf) , [SENSOR\_ATTR\_MCUX\_LPCMP\_COUTA\_SIGNAL](#a8104360e57e8d294fb6bd02812fcc03ea8189889b48c2cd89feb78fc84d33805a) ,     [SENSOR\_ATTR\_MCUX\_LPCMP\_COUT\_EVENT\_TO\_CLOSE\_WINDOW](#a8104360e57e8d294fb6bd02812fcc03ea0b7d5ec19095284f15e55a3054e849b4)   } |
|  | lpcmp attribute types. [More...](#a8104360e57e8d294fb6bd02812fcc03e) |

## Detailed Description

Data structure for the NXP MCUX low-power analog comparator (LPCMP).

## Enumeration Type Documentation

## [◆ ](#a8104360e57e8d294fb6bd02812fcc03e)sensor\_attribute\_mcux\_lpcmp

| enum [sensor\_attribute\_mcux\_lpcmp](#a8104360e57e8d294fb6bd02812fcc03e) |
| --- |

lpcmp attribute types.

| Enumerator | |
| --- | --- |
| SENSOR\_ATTR\_MCUX\_LPCMP\_POSITIVE\_MUX\_INPUT | LPCMP positive input mux. |
| SENSOR\_ATTR\_MCUX\_LPCMP\_NEGATIVE\_MUX\_INPUT | LPCMP negative input mux. |
| SENSOR\_ATTR\_MCUX\_LPCMP\_DAC\_ENABLE | LPCMP internal DAC enable.  0b: disable 1b: enable |
| SENSOR\_ATTR\_MCUX\_LPCMP\_DAC\_HIGH\_POWER\_MODE\_ENABLE | LPCMP internal DAC high power mode disabled.  0b: disable 1b: enable |
| SENSOR\_ATTR\_MCUX\_LPCMP\_DAC\_REFERENCE\_VOLTAGE\_SOURCE | LPCMP internal DAC voltage reference source. |
| SENSOR\_ATTR\_MCUX\_LPCMP\_DAC\_OUTPUT\_VOLTAGE | LPCMP internal DAC output voltage value. |
| SENSOR\_ATTR\_MCUX\_LPCMP\_SAMPLE\_ENABLE | LPCMP internal filter sample enable. |
| SENSOR\_ATTR\_MCUX\_LPCMP\_FILTER\_COUNT | LPCMP internal filter sample count. |
| SENSOR\_ATTR\_MCUX\_LPCMP\_FILTER\_PERIOD | LPCMP internal filter sample period. |
| SENSOR\_ATTR\_MCUX\_LPCMP\_COUTA\_WINDOW\_ENABLE | LPCMP window signal invert. |
| SENSOR\_ATTR\_MCUX\_LPCMP\_COUTA\_WINDOW\_SIGNAL\_INVERT\_ENABLE | LPCMP window signal invert. |
| SENSOR\_ATTR\_MCUX\_LPCMP\_COUTA\_SIGNAL | LPCMP COUTA signal value when a window is closed: 00b: latched 01b: set to low 11b: set to high. |
| SENSOR\_ATTR\_MCUX\_LPCMP\_COUT\_EVENT\_TO\_CLOSE\_WINDOW | LPCMP COUT event to close an active window: xx0b: COUT event cannot close an active window 001b: COUT rising edge event close an active window 011b: COUT falling edge event close an active window 1x1b: COUT both edges event close an active window. |

## [◆ ](#a0afc296fa89b7bdd31105574f459fb5a)sensor\_channel\_mcux\_lpcmp

| enum [sensor\_channel\_mcux\_lpcmp](#a0afc296fa89b7bdd31105574f459fb5a) |
| --- |

lpcmp channels.

| Enumerator | |
| --- | --- |
| SENSOR\_CHAN\_MCUX\_LPCMP\_OUTPUT | LPCMP output. |

## [◆ ](#ad86c67639b0a919fd5ea0b5b6a3d4cd6)sensor\_trigger\_type\_mcux\_lpcmp

| enum [sensor\_trigger\_type\_mcux\_lpcmp](#ad86c67639b0a919fd5ea0b5b6a3d4cd6) |
| --- |

lpcmp trigger types.

| Enumerator | |
| --- | --- |
| SENSOR\_TRIG\_MCUX\_LPCMP\_OUTPUT\_RISING | LPCMP output rising event trigger. |
| SENSOR\_TRIG\_MCUX\_LPCMP\_OUTPUT\_FALLING | LPCMP output falling event trigger. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [sensor](dir_b6423b3a8fc1c9278ff19cba182cfe6d.md)
- [mcux\_lpcmp.h](mcux__lpcmp_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
