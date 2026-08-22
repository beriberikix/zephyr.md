---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/modem_2ubx_2keys_8h.html
original_path: doxygen/html/modem_2ubx_2keys_8h.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

keys.h File Reference

[Go to the source code of this file.](modem_2ubx_2keys_8h_source.md)

| Enumerations | |
| --- | --- |
| enum | [ubx\_keys\_msg\_out](#aa9a0c17a62bdac457f3d7e960da9be78) {     [UBX\_KEY\_MSG\_OUT\_NMEA\_GGA\_UART1](#aa9a0c17a62bdac457f3d7e960da9be78a7ffb40fb28aaaa57b2fd965ce0c053e4) = 0x209100bb , [UBX\_KEY\_MSG\_OUT\_NMEA\_RMC\_UART1](#aa9a0c17a62bdac457f3d7e960da9be78ab4b47920933c4cb459f4b156c5d4066d) = 0x209100ac , [UBX\_KEY\_MSG\_OUT\_NMEA\_GSV\_UART1](#aa9a0c17a62bdac457f3d7e960da9be78a336a72a618136c1ee1b4608525ec1d13) = 0x209100c5 , [UBX\_KEY\_MSG\_OUT\_NMEA\_DTM\_UART1](#aa9a0c17a62bdac457f3d7e960da9be78ab5fe1c71c3f8b1ccd69e705668862fb5) = 0x209100a7 ,     [UBX\_KEY\_MSG\_OUT\_NMEA\_GBS\_UART1](#aa9a0c17a62bdac457f3d7e960da9be78a65d2e8ce96656bbc9cbd611dc553d9da) = 0x209100de , [UBX\_KEY\_MSG\_OUT\_NMEA\_GLL\_UART1](#aa9a0c17a62bdac457f3d7e960da9be78a7dd5de001be05acf6d4a47c4b649159b) = 0x209100ca , [UBX\_KEY\_MSG\_OUT\_NMEA\_GNS\_UART1](#aa9a0c17a62bdac457f3d7e960da9be78a2d160c79ca993743606b777a8198e16d) = 0x209100b6 , [UBX\_KEY\_MSG\_OUT\_NMEA\_GRS\_UART1](#aa9a0c17a62bdac457f3d7e960da9be78a9eb4f86da492bdab944b46699dc99488) = 0x209100cf ,     [UBX\_KEY\_MSG\_OUT\_NMEA\_GSA\_UART1](#aa9a0c17a62bdac457f3d7e960da9be78aff548ffd79eaffb73532efb820431f73) = 0x209100c0 , [UBX\_KEY\_MSG\_OUT\_NMEA\_GST\_UART1](#aa9a0c17a62bdac457f3d7e960da9be78a0538bba8ebfdbe1392c9efec0ccb1e71) = 0x209100d4 , [UBX\_KEY\_MSG\_OUT\_NMEA\_VTG\_UART1](#aa9a0c17a62bdac457f3d7e960da9be78a192177b57cc58ed258f39794ef1abc32) = 0x209100b1 , [UBX\_KEY\_MSG\_OUT\_NMEA\_VLW\_UART1](#aa9a0c17a62bdac457f3d7e960da9be78aee92e43d1c84b3cd729173b81f3a2f5d) = 0x209100e8 ,     [UBX\_KEY\_MSG\_OUT\_NMEA\_ZDA\_UART1](#aa9a0c17a62bdac457f3d7e960da9be78aefbae40d03e2976f8de982a4d58ca787) = 0x209100d9 , [UBX\_KEY\_MSG\_OUT\_UBX\_NAV\_PVT\_UART1](#aa9a0c17a62bdac457f3d7e960da9be78a0037d074be499163225d38bde68f8284) = 0x20910007 , [UBX\_KEY\_MSG\_OUT\_UBX\_NAV\_SAT\_UART1](#aa9a0c17a62bdac457f3d7e960da9be78ac988266ee549c2824ff121f3c9471344) = 0x20910016   } |
| enum | [ubx\_keys\_rate](#a581a2003a265c9c8105fa5f0df74f5b2) { [UBX\_KEY\_RATE\_MEAS](#a581a2003a265c9c8105fa5f0df74f5b2a779c6c882b5d77d721372354e3f663d7) = 0x30210001 , [UBX\_KEY\_RATE\_NAV](#a581a2003a265c9c8105fa5f0df74f5b2a42d94a342b5ccebb9f567a607ca10df5) = 0x30210002 } |
| enum | [ubx\_keys\_nav\_cfg](#ad806f9ced89f2f3338e5d14116cdb2df) { [UBX\_KEY\_NAV\_CFG\_FIX\_MODE](#ad806f9ced89f2f3338e5d14116cdb2dfa584a0b3c407fd7f8c8100ebeb4b12566) = 0x20110011 , [UBX\_KEY\_NAV\_CFG\_DYN\_MODEL](#ad806f9ced89f2f3338e5d14116cdb2dfa0adf8300b051ffd90e13d04087f95ccf) = 0x20110021 } |

## Enumeration Type Documentation

## [◆ ](#aa9a0c17a62bdac457f3d7e960da9be78)ubx\_keys\_msg\_out

| enum [ubx\_keys\_msg\_out](#aa9a0c17a62bdac457f3d7e960da9be78) |
| --- |

| Enumerator | |
| --- | --- |
| UBX\_KEY\_MSG\_OUT\_NMEA\_GGA\_UART1 |  |
| UBX\_KEY\_MSG\_OUT\_NMEA\_RMC\_UART1 |  |
| UBX\_KEY\_MSG\_OUT\_NMEA\_GSV\_UART1 |  |
| UBX\_KEY\_MSG\_OUT\_NMEA\_DTM\_UART1 |  |
| UBX\_KEY\_MSG\_OUT\_NMEA\_GBS\_UART1 |  |
| UBX\_KEY\_MSG\_OUT\_NMEA\_GLL\_UART1 |  |
| UBX\_KEY\_MSG\_OUT\_NMEA\_GNS\_UART1 |  |
| UBX\_KEY\_MSG\_OUT\_NMEA\_GRS\_UART1 |  |
| UBX\_KEY\_MSG\_OUT\_NMEA\_GSA\_UART1 |  |
| UBX\_KEY\_MSG\_OUT\_NMEA\_GST\_UART1 |  |
| UBX\_KEY\_MSG\_OUT\_NMEA\_VTG\_UART1 |  |
| UBX\_KEY\_MSG\_OUT\_NMEA\_VLW\_UART1 |  |
| UBX\_KEY\_MSG\_OUT\_NMEA\_ZDA\_UART1 |  |
| UBX\_KEY\_MSG\_OUT\_UBX\_NAV\_PVT\_UART1 |  |
| UBX\_KEY\_MSG\_OUT\_UBX\_NAV\_SAT\_UART1 |  |

## [◆ ](#ad806f9ced89f2f3338e5d14116cdb2df)ubx\_keys\_nav\_cfg

| enum [ubx\_keys\_nav\_cfg](#ad806f9ced89f2f3338e5d14116cdb2df) |
| --- |

| Enumerator | |
| --- | --- |
| UBX\_KEY\_NAV\_CFG\_FIX\_MODE |  |
| UBX\_KEY\_NAV\_CFG\_DYN\_MODEL |  |

## [◆ ](#a581a2003a265c9c8105fa5f0df74f5b2)ubx\_keys\_rate

| enum [ubx\_keys\_rate](#a581a2003a265c9c8105fa5f0df74f5b2) |
| --- |

| Enumerator | |
| --- | --- |
| UBX\_KEY\_RATE\_MEAS |  |
| UBX\_KEY\_RATE\_NAV |  |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [modem](dir_a816d481c0f951d2967bb275acf5f3dd.md)
- [ubx](dir_0a499179f9adf90767e72c7eb481b4fc.md)
- [keys.h](modem_2ubx_2keys_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
