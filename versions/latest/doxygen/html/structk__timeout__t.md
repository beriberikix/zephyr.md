---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structk__timeout__t.html
original_path: doxygen/html/structk__timeout__t.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

k\_timeout\_t Struct Reference

[Kernel APIs](group__kernel__apis.md) » [System Clock APIs](group__clock__apis.md)

Kernel timeout type.
[More...](#details)

`#include <[sys_clock.h](include_2zephyr_2sys__clock_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [k\_ticks\_t](group__clock__apis.md#ga9832cb0adc2d1866420e5c370a0863e2) | [ticks](#a492605d3a8c76f0ce2ef129b9f4d40fa) |

## Detailed Description

Kernel timeout type.

Timeout arguments presented to kernel APIs are stored in this opaque type, which is capable of representing times in various formats and units. It should be constructed from application data using one of the macros defined for this purpose (e.g. [K\_MSEC()](group__clock__apis.md#ga302af954e87b10a9b731f1ad07775e9f "Generate timeout delay from milliseconds."), K\_TIMEOUT\_ABS\_TICKS(), etc...), or be one of the two constants K\_NO\_WAIT or K\_FOREVER. Applications should not inspect the internal data once constructed. Timeout values may be compared for equality with the [K\_TIMEOUT\_EQ()](group__clock__apis.md#ga9abf00b34e16ab7ad0883603b6778b1b "Compare timeouts for equality.") macro.

## Field Documentation

## [◆ ](#a492605d3a8c76f0ce2ef129b9f4d40fa)ticks

| [k\_ticks\_t](group__clock__apis.md#ga9832cb0adc2d1866420e5c370a0863e2) k\_timeout\_t::ticks |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/[sys\_clock.h](include_2zephyr_2sys__clock_8h_source.md)

- [k\_timeout\_t](structk__timeout__t.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
