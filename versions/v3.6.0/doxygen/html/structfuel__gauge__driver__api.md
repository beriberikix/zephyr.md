---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structfuel__gauge__driver__api.html
original_path: doxygen/html/structfuel__gauge__driver__api.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

fuel\_gauge\_driver\_api Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [Fuel Gauge Interface](group__fuel__gauge__interface.md)

`#include <[fuel_gauge.h](fuel__gauge_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [fuel\_gauge\_get\_property\_t](group__fuel__gauge__interface.md#gaed940ae925236ad2f25cf05d78304568) | [get\_property](#ab729a85c69e561f1ca0aca9f8eb22d91) |
|  | Note: Historically this API allowed drivers to implement a custom multi-get/set property function, this was added so drivers could potentially optimize batch read with their specific chip. |
| [fuel\_gauge\_set\_property\_t](group__fuel__gauge__interface.md#gae87a20a20f4f1fbb74d72afb2bcee4c9) | [set\_property](#a74815d3bb721452bfd3e35cd1221b223) |
| [fuel\_gauge\_get\_buffer\_property\_t](group__fuel__gauge__interface.md#gaf8843b8ba9ff3102ac4d6c0fa2cb3f69) | [get\_buffer\_property](#ad12c13461173177d1c81846a85a3f570) |
| [fuel\_gauge\_battery\_cutoff\_t](group__fuel__gauge__interface.md#ga698c8f84da7d1cbe7db1fc024e2388b7) | [battery\_cutoff](#a406816c19022eea26f0fd61fb21d234c) |

## Field Documentation

## [◆ ](#a406816c19022eea26f0fd61fb21d234c)battery\_cutoff

| [fuel\_gauge\_battery\_cutoff\_t](group__fuel__gauge__interface.md#ga698c8f84da7d1cbe7db1fc024e2388b7) fuel\_gauge\_driver\_api::battery\_cutoff |
| --- |

## [◆ ](#ad12c13461173177d1c81846a85a3f570)get\_buffer\_property

| [fuel\_gauge\_get\_buffer\_property\_t](group__fuel__gauge__interface.md#gaf8843b8ba9ff3102ac4d6c0fa2cb3f69) fuel\_gauge\_driver\_api::get\_buffer\_property |
| --- |

## [◆ ](#ab729a85c69e561f1ca0aca9f8eb22d91)get\_property

| [fuel\_gauge\_get\_property\_t](group__fuel__gauge__interface.md#gaed940ae925236ad2f25cf05d78304568) fuel\_gauge\_driver\_api::get\_property |
| --- |

Note: Historically this API allowed drivers to implement a custom multi-get/set property function, this was added so drivers could potentially optimize batch read with their specific chip.

However, it was removed because of no existing concrete case upstream. If this need is demonstrated, we can add this back in as an API field.

## [◆ ](#a74815d3bb721452bfd3e35cd1221b223)set\_property

| [fuel\_gauge\_set\_property\_t](group__fuel__gauge__interface.md#gae87a20a20f4f1fbb74d72afb2bcee4c9) fuel\_gauge\_driver\_api::set\_property |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[fuel\_gauge.h](fuel__gauge_8h_source.md)

- [fuel\_gauge\_driver\_api](structfuel__gauge__driver__api.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
