---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/tdk__apex_8h.html
original_path: doxygen/html/tdk__apex_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

tdk\_apex.h File Reference

Extended public API for TDK MEMS sensor.
[More...](#details)

`#include <[zephyr/drivers/sensor.h](sensor_8h_source.md)>`

[Go to the source code of this file.](tdk__apex_8h_source.md)

| Macros | |
| --- | --- |
| #define | [TDK\_APEX\_PEDOMETER](#a0dd9a01a81c985de9a3a1edd1d9f84a6)   (1) |
|  | TDK APEX features. |
| #define | [TDK\_APEX\_TILT](#aa635dbac54613d9f389b0e45de63d274)   (2) |
| #define | [TDK\_APEX\_SMD](#a5ebd1faf982dd9a4b5b13bda71927afb)   (3) |
| #define | [TDK\_APEX\_WOM](#adad62736e0caaa3e2d01a810ef180b8a)   (4) |

| Enumerations | |
| --- | --- |
| enum | [sensor\_channel\_tdk\_apex](#a944436d98a2aea1f93977a2d0738d959) { [SENSOR\_CHAN\_APEX\_MOTION](#a944436d98a2aea1f93977a2d0738d959a5181bce02684391a151723bbd7f86af5) = SENSOR\_CHAN\_PRIV\_START } |
|  | Extended sensor channel for TDK MEMS supportintg APEX features. [More...](#a944436d98a2aea1f93977a2d0738d959) |

## Detailed Description

Extended public API for TDK MEMS sensor.

Some capabilities and operational requirements for this sensor cannot be expressed within the sensor driver abstraction.

## Macro Definition Documentation

## [◆ ](#a0dd9a01a81c985de9a3a1edd1d9f84a6)TDK\_APEX\_PEDOMETER

| #define TDK\_APEX\_PEDOMETER   (1) |
| --- |

TDK APEX features.

## [◆ ](#a5ebd1faf982dd9a4b5b13bda71927afb)TDK\_APEX\_SMD

| #define TDK\_APEX\_SMD   (3) |
| --- |

## [◆ ](#aa635dbac54613d9f389b0e45de63d274)TDK\_APEX\_TILT

| #define TDK\_APEX\_TILT   (2) |
| --- |

## [◆ ](#adad62736e0caaa3e2d01a810ef180b8a)TDK\_APEX\_WOM

| #define TDK\_APEX\_WOM   (4) |
| --- |

## Enumeration Type Documentation

## [◆ ](#a944436d98a2aea1f93977a2d0738d959)sensor\_channel\_tdk\_apex

| enum [sensor\_channel\_tdk\_apex](#a944436d98a2aea1f93977a2d0738d959) |
| --- |

Extended sensor channel for TDK MEMS supportintg APEX features.

This exposes sensor channel for the TDK MEMS which can be used for getting the APEX features data.

The APEX (Advanced Pedometer and Event Detection – neXt gen) features of TDK MEMS consist of: \*\* Pedometer: Tracks step count. \*\* Tilt Detection: Detect the Tilt angle exceeds 35 degrees. \*\* Wake on Motion (WoM): Detects motion when accelerometer samples exceed a programmable threshold. This motion event can be used to enable device operation from sleep mode. \*\* Significant Motion Detector (SMD): Detects significant motion based on accelerometer data.

| Enumerator | |
| --- | --- |
| SENSOR\_CHAN\_APEX\_MOTION | APEX features. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [sensor](dir_b6423b3a8fc1c9278ff19cba182cfe6d.md)
- [tdk\_apex.h](tdk__apex_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
