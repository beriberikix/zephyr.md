---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/nrf__clock__control_8h.html
original_path: doxygen/html/nrf__clock__control_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

nrf\_clock\_control.h File Reference

`#include <[zephyr/device.h](device_8h_source.md)>`  
`#include <hal/nrf_clock.h>`  
`#include <[zephyr/sys/onoff.h](onoff_8h_source.md)>`  
`#include <[zephyr/drivers/clock_control.h](clock__control_8h_source.md)>`

[Go to the source code of this file.](nrf__clock__control_8h_source.md)

| Macros | |
| --- | --- |
| #define | [CLOCK\_CONTROL\_NRF\_SUBSYS\_HF](#a1ecdf70d00c6792cadbe541dc52f167c)   (([clock\_control\_subsys\_t](group__clock__control__interface.md#gaa7d3935eaaf18902801a7d94859483db))[CLOCK\_CONTROL\_NRF\_TYPE\_HFCLK](#ab64ed97e8dc26da602e521309a300494ab72ac85df0cde71e7de9b96967eff37f)) |
| #define | [CLOCK\_CONTROL\_NRF\_SUBSYS\_LF](#a05ef5b77d85a77907083f9b873519cfd)   (([clock\_control\_subsys\_t](group__clock__control__interface.md#gaa7d3935eaaf18902801a7d94859483db))[CLOCK\_CONTROL\_NRF\_TYPE\_LFCLK](#ab64ed97e8dc26da602e521309a300494ad21d1fb9a5167a0b3374c1969ff6caf4)) |
| #define | [CLOCK\_CONTROL\_NRF\_SUBSYS\_HF192M](#a3c37235f76338ddfd66c05a470a919e1)   (([clock\_control\_subsys\_t](group__clock__control__interface.md#gaa7d3935eaaf18902801a7d94859483db))CLOCK\_CONTROL\_NRF\_TYPE\_HFCLK192M) |
| #define | [CLOCK\_CONTROL\_NRF\_SUBSYS\_HFAUDIO](#a27e5bdc4901fd86dd29d12a4bc5409f2)   (([clock\_control\_subsys\_t](group__clock__control__interface.md#gaa7d3935eaaf18902801a7d94859483db))CLOCK\_CONTROL\_NRF\_TYPE\_HFCLKAUDIO) |

| Enumerations | |
| --- | --- |
| enum | [clock\_control\_nrf\_type](#ab64ed97e8dc26da602e521309a300494) { [CLOCK\_CONTROL\_NRF\_TYPE\_HFCLK](#ab64ed97e8dc26da602e521309a300494ab72ac85df0cde71e7de9b96967eff37f) , [CLOCK\_CONTROL\_NRF\_TYPE\_LFCLK](#ab64ed97e8dc26da602e521309a300494ad21d1fb9a5167a0b3374c1969ff6caf4) , [CLOCK\_CONTROL\_NRF\_TYPE\_COUNT](#ab64ed97e8dc26da602e521309a300494a9ad0884bcc0d37d5f178c1a905f36ccc) } |
|  | Clocks handled by the CLOCK peripheral. [More...](#ab64ed97e8dc26da602e521309a300494) |
| enum | [nrf\_lfclk\_start\_mode](#aadc162ec2c250d17572546d74a08ee7d) { [CLOCK\_CONTROL\_NRF\_LF\_START\_NOWAIT](#aadc162ec2c250d17572546d74a08ee7dab4eb3c0c8038403f218a0147df6cdbec) , [CLOCK\_CONTROL\_NRF\_LF\_START\_AVAILABLE](#aadc162ec2c250d17572546d74a08ee7da92be9b702c66df1a2bfd95560f1278df) , [CLOCK\_CONTROL\_NRF\_LF\_START\_STABLE](#aadc162ec2c250d17572546d74a08ee7da949ac21a6fe976280b5fcc967608a8f4) } |
|  | LF clock start modes. [More...](#aadc162ec2c250d17572546d74a08ee7d) |

## Macro Definition Documentation

## [◆ ](#a1ecdf70d00c6792cadbe541dc52f167c)CLOCK\_CONTROL\_NRF\_SUBSYS\_HF

| #define CLOCK\_CONTROL\_NRF\_SUBSYS\_HF   (([clock\_control\_subsys\_t](group__clock__control__interface.md#gaa7d3935eaaf18902801a7d94859483db))[CLOCK\_CONTROL\_NRF\_TYPE\_HFCLK](#ab64ed97e8dc26da602e521309a300494ab72ac85df0cde71e7de9b96967eff37f)) |
| --- |

## [◆ ](#a3c37235f76338ddfd66c05a470a919e1)CLOCK\_CONTROL\_NRF\_SUBSYS\_HF192M

| #define CLOCK\_CONTROL\_NRF\_SUBSYS\_HF192M   (([clock\_control\_subsys\_t](group__clock__control__interface.md#gaa7d3935eaaf18902801a7d94859483db))CLOCK\_CONTROL\_NRF\_TYPE\_HFCLK192M) |
| --- |

## [◆ ](#a27e5bdc4901fd86dd29d12a4bc5409f2)CLOCK\_CONTROL\_NRF\_SUBSYS\_HFAUDIO

| #define CLOCK\_CONTROL\_NRF\_SUBSYS\_HFAUDIO   (([clock\_control\_subsys\_t](group__clock__control__interface.md#gaa7d3935eaaf18902801a7d94859483db))CLOCK\_CONTROL\_NRF\_TYPE\_HFCLKAUDIO) |
| --- |

## [◆ ](#a05ef5b77d85a77907083f9b873519cfd)CLOCK\_CONTROL\_NRF\_SUBSYS\_LF

| #define CLOCK\_CONTROL\_NRF\_SUBSYS\_LF   (([clock\_control\_subsys\_t](group__clock__control__interface.md#gaa7d3935eaaf18902801a7d94859483db))[CLOCK\_CONTROL\_NRF\_TYPE\_LFCLK](#ab64ed97e8dc26da602e521309a300494ad21d1fb9a5167a0b3374c1969ff6caf4)) |
| --- |

## Enumeration Type Documentation

## [◆ ](#ab64ed97e8dc26da602e521309a300494)clock\_control\_nrf\_type

| enum [clock\_control\_nrf\_type](#ab64ed97e8dc26da602e521309a300494) |
| --- |

Clocks handled by the CLOCK peripheral.

Enum shall be used as a sys argument in [clock\_control](group__clock__control__interface.md#ga459b95cb726892b95537d15273413099) API.

| Enumerator | |
| --- | --- |
| CLOCK\_CONTROL\_NRF\_TYPE\_HFCLK |  |
| CLOCK\_CONTROL\_NRF\_TYPE\_LFCLK |  |
| CLOCK\_CONTROL\_NRF\_TYPE\_COUNT |  |

## [◆ ](#aadc162ec2c250d17572546d74a08ee7d)nrf\_lfclk\_start\_mode

| enum [nrf\_lfclk\_start\_mode](#aadc162ec2c250d17572546d74a08ee7d) |
| --- |

LF clock start modes.

| Enumerator | |
| --- | --- |
| CLOCK\_CONTROL\_NRF\_LF\_START\_NOWAIT |  |
| CLOCK\_CONTROL\_NRF\_LF\_START\_AVAILABLE |  |
| CLOCK\_CONTROL\_NRF\_LF\_START\_STABLE |  |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [clock\_control](dir_a984f062cf5261c2619127147b7cc64c.md)
- [nrf\_clock\_control.h](nrf__clock__control_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
