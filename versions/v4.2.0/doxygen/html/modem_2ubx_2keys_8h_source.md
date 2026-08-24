---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/modem_2ubx_2keys_8h_source.html
original_path: doxygen/html/modem_2ubx_2keys_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

keys.h

[Go to the documentation of this file.](modem_2ubx_2keys_8h.md)

1/\*

2 \* Copyright (c) 2025 Croxel Inc.

3 \* Copyright (c) 2025 CogniPilot Foundation

4 \*

5 \* SPDX-License-Identifier: Apache-2.0

6 \*/

7

8#ifndef ZEPHYR\_MODEM\_UBX\_KEYS\_

9#define ZEPHYR\_MODEM\_UBX\_KEYS\_

10

[ 11](modem_2ubx_2keys_8h.md#aa9a0c17a62bdac457f3d7e960da9be78)enum [ubx\_keys\_msg\_out](modem_2ubx_2keys_8h.md#aa9a0c17a62bdac457f3d7e960da9be78) {

[ 12](modem_2ubx_2keys_8h.md#aa9a0c17a62bdac457f3d7e960da9be78a7ffb40fb28aaaa57b2fd965ce0c053e4) [UBX\_KEY\_MSG\_OUT\_NMEA\_GGA\_UART1](modem_2ubx_2keys_8h.md#aa9a0c17a62bdac457f3d7e960da9be78a7ffb40fb28aaaa57b2fd965ce0c053e4) = 0x209100bb,

[ 13](modem_2ubx_2keys_8h.md#aa9a0c17a62bdac457f3d7e960da9be78ab4b47920933c4cb459f4b156c5d4066d) [UBX\_KEY\_MSG\_OUT\_NMEA\_RMC\_UART1](modem_2ubx_2keys_8h.md#aa9a0c17a62bdac457f3d7e960da9be78ab4b47920933c4cb459f4b156c5d4066d) = 0x209100ac,

[ 14](modem_2ubx_2keys_8h.md#aa9a0c17a62bdac457f3d7e960da9be78a336a72a618136c1ee1b4608525ec1d13) [UBX\_KEY\_MSG\_OUT\_NMEA\_GSV\_UART1](modem_2ubx_2keys_8h.md#aa9a0c17a62bdac457f3d7e960da9be78a336a72a618136c1ee1b4608525ec1d13) = 0x209100c5,

[ 15](modem_2ubx_2keys_8h.md#aa9a0c17a62bdac457f3d7e960da9be78ab5fe1c71c3f8b1ccd69e705668862fb5) [UBX\_KEY\_MSG\_OUT\_NMEA\_DTM\_UART1](modem_2ubx_2keys_8h.md#aa9a0c17a62bdac457f3d7e960da9be78ab5fe1c71c3f8b1ccd69e705668862fb5) = 0x209100a7,

[ 16](modem_2ubx_2keys_8h.md#aa9a0c17a62bdac457f3d7e960da9be78a65d2e8ce96656bbc9cbd611dc553d9da) [UBX\_KEY\_MSG\_OUT\_NMEA\_GBS\_UART1](modem_2ubx_2keys_8h.md#aa9a0c17a62bdac457f3d7e960da9be78a65d2e8ce96656bbc9cbd611dc553d9da) = 0x209100de,

[ 17](modem_2ubx_2keys_8h.md#aa9a0c17a62bdac457f3d7e960da9be78a7dd5de001be05acf6d4a47c4b649159b) [UBX\_KEY\_MSG\_OUT\_NMEA\_GLL\_UART1](modem_2ubx_2keys_8h.md#aa9a0c17a62bdac457f3d7e960da9be78a7dd5de001be05acf6d4a47c4b649159b) = 0x209100ca,

[ 18](modem_2ubx_2keys_8h.md#aa9a0c17a62bdac457f3d7e960da9be78a2d160c79ca993743606b777a8198e16d) [UBX\_KEY\_MSG\_OUT\_NMEA\_GNS\_UART1](modem_2ubx_2keys_8h.md#aa9a0c17a62bdac457f3d7e960da9be78a2d160c79ca993743606b777a8198e16d) = 0x209100b6,

[ 19](modem_2ubx_2keys_8h.md#aa9a0c17a62bdac457f3d7e960da9be78a9eb4f86da492bdab944b46699dc99488) [UBX\_KEY\_MSG\_OUT\_NMEA\_GRS\_UART1](modem_2ubx_2keys_8h.md#aa9a0c17a62bdac457f3d7e960da9be78a9eb4f86da492bdab944b46699dc99488) = 0x209100cf,

[ 20](modem_2ubx_2keys_8h.md#aa9a0c17a62bdac457f3d7e960da9be78aff548ffd79eaffb73532efb820431f73) [UBX\_KEY\_MSG\_OUT\_NMEA\_GSA\_UART1](modem_2ubx_2keys_8h.md#aa9a0c17a62bdac457f3d7e960da9be78aff548ffd79eaffb73532efb820431f73) = 0x209100c0,

[ 21](modem_2ubx_2keys_8h.md#aa9a0c17a62bdac457f3d7e960da9be78a0538bba8ebfdbe1392c9efec0ccb1e71) [UBX\_KEY\_MSG\_OUT\_NMEA\_GST\_UART1](modem_2ubx_2keys_8h.md#aa9a0c17a62bdac457f3d7e960da9be78a0538bba8ebfdbe1392c9efec0ccb1e71) = 0x209100d4,

[ 22](modem_2ubx_2keys_8h.md#aa9a0c17a62bdac457f3d7e960da9be78a192177b57cc58ed258f39794ef1abc32) [UBX\_KEY\_MSG\_OUT\_NMEA\_VTG\_UART1](modem_2ubx_2keys_8h.md#aa9a0c17a62bdac457f3d7e960da9be78a192177b57cc58ed258f39794ef1abc32) = 0x209100b1,

[ 23](modem_2ubx_2keys_8h.md#aa9a0c17a62bdac457f3d7e960da9be78aee92e43d1c84b3cd729173b81f3a2f5d) [UBX\_KEY\_MSG\_OUT\_NMEA\_VLW\_UART1](modem_2ubx_2keys_8h.md#aa9a0c17a62bdac457f3d7e960da9be78aee92e43d1c84b3cd729173b81f3a2f5d) = 0x209100e8,

[ 24](modem_2ubx_2keys_8h.md#aa9a0c17a62bdac457f3d7e960da9be78aefbae40d03e2976f8de982a4d58ca787) [UBX\_KEY\_MSG\_OUT\_NMEA\_ZDA\_UART1](modem_2ubx_2keys_8h.md#aa9a0c17a62bdac457f3d7e960da9be78aefbae40d03e2976f8de982a4d58ca787) = 0x209100d9,

[ 25](modem_2ubx_2keys_8h.md#aa9a0c17a62bdac457f3d7e960da9be78a0037d074be499163225d38bde68f8284) [UBX\_KEY\_MSG\_OUT\_UBX\_NAV\_PVT\_UART1](modem_2ubx_2keys_8h.md#aa9a0c17a62bdac457f3d7e960da9be78a0037d074be499163225d38bde68f8284) = 0x20910007,

[ 26](modem_2ubx_2keys_8h.md#aa9a0c17a62bdac457f3d7e960da9be78ac988266ee549c2824ff121f3c9471344) [UBX\_KEY\_MSG\_OUT\_UBX\_NAV\_SAT\_UART1](modem_2ubx_2keys_8h.md#aa9a0c17a62bdac457f3d7e960da9be78ac988266ee549c2824ff121f3c9471344) = 0x20910016,

27};

28

[ 29](modem_2ubx_2keys_8h.md#a581a2003a265c9c8105fa5f0df74f5b2)enum [ubx\_keys\_rate](modem_2ubx_2keys_8h.md#a581a2003a265c9c8105fa5f0df74f5b2) {

[ 30](modem_2ubx_2keys_8h.md#a581a2003a265c9c8105fa5f0df74f5b2a779c6c882b5d77d721372354e3f663d7) [UBX\_KEY\_RATE\_MEAS](modem_2ubx_2keys_8h.md#a581a2003a265c9c8105fa5f0df74f5b2a779c6c882b5d77d721372354e3f663d7) = 0x30210001,

[ 31](modem_2ubx_2keys_8h.md#a581a2003a265c9c8105fa5f0df74f5b2a42d94a342b5ccebb9f567a607ca10df5) [UBX\_KEY\_RATE\_NAV](modem_2ubx_2keys_8h.md#a581a2003a265c9c8105fa5f0df74f5b2a42d94a342b5ccebb9f567a607ca10df5) = 0x30210002,

32};

33

[ 34](modem_2ubx_2keys_8h.md#ad806f9ced89f2f3338e5d14116cdb2df)enum [ubx\_keys\_nav\_cfg](modem_2ubx_2keys_8h.md#ad806f9ced89f2f3338e5d14116cdb2df) {

[ 35](modem_2ubx_2keys_8h.md#ad806f9ced89f2f3338e5d14116cdb2dfa584a0b3c407fd7f8c8100ebeb4b12566) [UBX\_KEY\_NAV\_CFG\_FIX\_MODE](modem_2ubx_2keys_8h.md#ad806f9ced89f2f3338e5d14116cdb2dfa584a0b3c407fd7f8c8100ebeb4b12566) = 0x20110011,

[ 36](modem_2ubx_2keys_8h.md#ad806f9ced89f2f3338e5d14116cdb2dfa0adf8300b051ffd90e13d04087f95ccf) [UBX\_KEY\_NAV\_CFG\_DYN\_MODEL](modem_2ubx_2keys_8h.md#ad806f9ced89f2f3338e5d14116cdb2dfa0adf8300b051ffd90e13d04087f95ccf) = 0x20110021,

37};

38

39#endif /\* ZEPHYR\_MODEM\_UBX\_KEYS\_ \*/

[ubx\_keys\_rate](modem_2ubx_2keys_8h.md#a581a2003a265c9c8105fa5f0df74f5b2)

ubx\_keys\_rate

**Definition** keys.h:29

[UBX\_KEY\_RATE\_NAV](modem_2ubx_2keys_8h.md#a581a2003a265c9c8105fa5f0df74f5b2a42d94a342b5ccebb9f567a607ca10df5)

@ UBX\_KEY\_RATE\_NAV

**Definition** keys.h:31

[UBX\_KEY\_RATE\_MEAS](modem_2ubx_2keys_8h.md#a581a2003a265c9c8105fa5f0df74f5b2a779c6c882b5d77d721372354e3f663d7)

@ UBX\_KEY\_RATE\_MEAS

**Definition** keys.h:30

[ubx\_keys\_msg\_out](modem_2ubx_2keys_8h.md#aa9a0c17a62bdac457f3d7e960da9be78)

ubx\_keys\_msg\_out

**Definition** keys.h:11

[UBX\_KEY\_MSG\_OUT\_UBX\_NAV\_PVT\_UART1](modem_2ubx_2keys_8h.md#aa9a0c17a62bdac457f3d7e960da9be78a0037d074be499163225d38bde68f8284)

@ UBX\_KEY\_MSG\_OUT\_UBX\_NAV\_PVT\_UART1

**Definition** keys.h:25

[UBX\_KEY\_MSG\_OUT\_NMEA\_GST\_UART1](modem_2ubx_2keys_8h.md#aa9a0c17a62bdac457f3d7e960da9be78a0538bba8ebfdbe1392c9efec0ccb1e71)

@ UBX\_KEY\_MSG\_OUT\_NMEA\_GST\_UART1

**Definition** keys.h:21

[UBX\_KEY\_MSG\_OUT\_NMEA\_VTG\_UART1](modem_2ubx_2keys_8h.md#aa9a0c17a62bdac457f3d7e960da9be78a192177b57cc58ed258f39794ef1abc32)

@ UBX\_KEY\_MSG\_OUT\_NMEA\_VTG\_UART1

**Definition** keys.h:22

[UBX\_KEY\_MSG\_OUT\_NMEA\_GNS\_UART1](modem_2ubx_2keys_8h.md#aa9a0c17a62bdac457f3d7e960da9be78a2d160c79ca993743606b777a8198e16d)

@ UBX\_KEY\_MSG\_OUT\_NMEA\_GNS\_UART1

**Definition** keys.h:18

[UBX\_KEY\_MSG\_OUT\_NMEA\_GSV\_UART1](modem_2ubx_2keys_8h.md#aa9a0c17a62bdac457f3d7e960da9be78a336a72a618136c1ee1b4608525ec1d13)

@ UBX\_KEY\_MSG\_OUT\_NMEA\_GSV\_UART1

**Definition** keys.h:14

[UBX\_KEY\_MSG\_OUT\_NMEA\_GBS\_UART1](modem_2ubx_2keys_8h.md#aa9a0c17a62bdac457f3d7e960da9be78a65d2e8ce96656bbc9cbd611dc553d9da)

@ UBX\_KEY\_MSG\_OUT\_NMEA\_GBS\_UART1

**Definition** keys.h:16

[UBX\_KEY\_MSG\_OUT\_NMEA\_GLL\_UART1](modem_2ubx_2keys_8h.md#aa9a0c17a62bdac457f3d7e960da9be78a7dd5de001be05acf6d4a47c4b649159b)

@ UBX\_KEY\_MSG\_OUT\_NMEA\_GLL\_UART1

**Definition** keys.h:17

[UBX\_KEY\_MSG\_OUT\_NMEA\_GGA\_UART1](modem_2ubx_2keys_8h.md#aa9a0c17a62bdac457f3d7e960da9be78a7ffb40fb28aaaa57b2fd965ce0c053e4)

@ UBX\_KEY\_MSG\_OUT\_NMEA\_GGA\_UART1

**Definition** keys.h:12

[UBX\_KEY\_MSG\_OUT\_NMEA\_GRS\_UART1](modem_2ubx_2keys_8h.md#aa9a0c17a62bdac457f3d7e960da9be78a9eb4f86da492bdab944b46699dc99488)

@ UBX\_KEY\_MSG\_OUT\_NMEA\_GRS\_UART1

**Definition** keys.h:19

[UBX\_KEY\_MSG\_OUT\_NMEA\_RMC\_UART1](modem_2ubx_2keys_8h.md#aa9a0c17a62bdac457f3d7e960da9be78ab4b47920933c4cb459f4b156c5d4066d)

@ UBX\_KEY\_MSG\_OUT\_NMEA\_RMC\_UART1

**Definition** keys.h:13

[UBX\_KEY\_MSG\_OUT\_NMEA\_DTM\_UART1](modem_2ubx_2keys_8h.md#aa9a0c17a62bdac457f3d7e960da9be78ab5fe1c71c3f8b1ccd69e705668862fb5)

@ UBX\_KEY\_MSG\_OUT\_NMEA\_DTM\_UART1

**Definition** keys.h:15

[UBX\_KEY\_MSG\_OUT\_UBX\_NAV\_SAT\_UART1](modem_2ubx_2keys_8h.md#aa9a0c17a62bdac457f3d7e960da9be78ac988266ee549c2824ff121f3c9471344)

@ UBX\_KEY\_MSG\_OUT\_UBX\_NAV\_SAT\_UART1

**Definition** keys.h:26

[UBX\_KEY\_MSG\_OUT\_NMEA\_VLW\_UART1](modem_2ubx_2keys_8h.md#aa9a0c17a62bdac457f3d7e960da9be78aee92e43d1c84b3cd729173b81f3a2f5d)

@ UBX\_KEY\_MSG\_OUT\_NMEA\_VLW\_UART1

**Definition** keys.h:23

[UBX\_KEY\_MSG\_OUT\_NMEA\_ZDA\_UART1](modem_2ubx_2keys_8h.md#aa9a0c17a62bdac457f3d7e960da9be78aefbae40d03e2976f8de982a4d58ca787)

@ UBX\_KEY\_MSG\_OUT\_NMEA\_ZDA\_UART1

**Definition** keys.h:24

[UBX\_KEY\_MSG\_OUT\_NMEA\_GSA\_UART1](modem_2ubx_2keys_8h.md#aa9a0c17a62bdac457f3d7e960da9be78aff548ffd79eaffb73532efb820431f73)

@ UBX\_KEY\_MSG\_OUT\_NMEA\_GSA\_UART1

**Definition** keys.h:20

[ubx\_keys\_nav\_cfg](modem_2ubx_2keys_8h.md#ad806f9ced89f2f3338e5d14116cdb2df)

ubx\_keys\_nav\_cfg

**Definition** keys.h:34

[UBX\_KEY\_NAV\_CFG\_DYN\_MODEL](modem_2ubx_2keys_8h.md#ad806f9ced89f2f3338e5d14116cdb2dfa0adf8300b051ffd90e13d04087f95ccf)

@ UBX\_KEY\_NAV\_CFG\_DYN\_MODEL

**Definition** keys.h:36

[UBX\_KEY\_NAV\_CFG\_FIX\_MODE](modem_2ubx_2keys_8h.md#ad806f9ced89f2f3338e5d14116cdb2dfa584a0b3c407fd7f8c8100ebeb4b12566)

@ UBX\_KEY\_NAV\_CFG\_FIX\_MODE

**Definition** keys.h:35

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [modem](dir_a816d481c0f951d2967bb275acf5f3dd.md)
- [ubx](dir_0a499179f9adf90767e72c7eb481b4fc.md)
- [keys.h](modem_2ubx_2keys_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
