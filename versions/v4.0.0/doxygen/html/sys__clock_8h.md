---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/sys__clock_8h.html
original_path: doxygen/html/sys__clock_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

sys\_clock.h File Reference

Variables needed for system clock.
[More...](#details)

`#include <[zephyr/sys/util.h](sys_2util_8h_source.md)>`  
`#include <[zephyr/sys/dlist.h](dlist_8h_source.md)>`  
`#include <[zephyr/toolchain.h](toolchain_8h_source.md)>`  
`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`  
`#include <[zephyr/sys/time_units.h](time__units_8h_source.md)>`

[Go to the source code of this file.](sys__clock_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [k\_timeout\_t](structk__timeout__t.md) |
|  | Kernel timeout type. [More...](structk__timeout__t.md#details) |
| struct | [k\_timepoint\_t](structk__timepoint__t.md) |
|  | Kernel timepoint type. [More...](structk__timepoint__t.md#details) |

| Macros | |
| --- | --- |
| #define | [K\_TICKS\_FOREVER](group__clock__apis.md#ga66e180b3d8940c30786a1d972cbd6d8d)   (([k\_ticks\_t](group__clock__apis.md#ga9832cb0adc2d1866420e5c370a0863e2)) -1) |
| #define | [K\_TIMEOUT\_EQ](group__clock__apis.md#ga9abf00b34e16ab7ad0883603b6778b1b)(a, b) |
|  | Compare timeouts for equality. |
| #define | [NSEC\_PER\_USEC](group__clock__apis.md#ga2180f263d149841a7c1fde663edb84c5)   1000U |
|  | number of nanoseconds per micorsecond |
| #define | [NSEC\_PER\_MSEC](group__clock__apis.md#gad16e9029e202d2dfb4cfae8f09131f8f)   1000000U |
|  | number of nanoseconds per millisecond |
| #define | [USEC\_PER\_MSEC](group__clock__apis.md#ga2d66311052e2bddf914610fb7345ff27)   1000U |
|  | number of microseconds per millisecond |
| #define | [MSEC\_PER\_SEC](group__clock__apis.md#ga222f9dff749accf8de62bc4b52c7bdcd)   1000U |
|  | number of milliseconds per second |
| #define | [SEC\_PER\_MIN](group__clock__apis.md#gac47b302f1b8d2a7a9c035c417247be76)   60U |
|  | number of seconds per minute |
| #define | [MIN\_PER\_HOUR](group__clock__apis.md#gaa6094c8f66b81269ce912804b796d2c7)   60U |
|  | number of minutes per hour |
| #define | [HOUR\_PER\_DAY](group__clock__apis.md#gafcbf34dc5c48a91fe5f6efe4c1bae745)   24U |
|  | number of hours per day |
| #define | [USEC\_PER\_SEC](group__clock__apis.md#ga6a69d6cbdab5f24c2e66959293f210c1)   (([USEC\_PER\_MSEC](group__clock__apis.md#ga2d66311052e2bddf914610fb7345ff27)) \* ([MSEC\_PER\_SEC](group__clock__apis.md#ga222f9dff749accf8de62bc4b52c7bdcd))) |
|  | number of microseconds per second |
| #define | [NSEC\_PER\_SEC](group__clock__apis.md#ga0501e82515b2bdf36453c4cc80f5e0cc)   (([NSEC\_PER\_USEC](group__clock__apis.md#ga2180f263d149841a7c1fde663edb84c5)) \* ([USEC\_PER\_MSEC](group__clock__apis.md#ga2d66311052e2bddf914610fb7345ff27)) \* ([MSEC\_PER\_SEC](group__clock__apis.md#ga222f9dff749accf8de62bc4b52c7bdcd))) |
|  | number of nanoseconds per second |
| #define | [SYS\_CLOCK\_HW\_CYCLES\_TO\_NS\_AVG](group__clock__apis.md#ga59d9bd47b0caa662f0e289cf3df83a82)(X, NCYCLES) |
|  | SYS\_CLOCK\_HW\_CYCLES\_TO\_NS\_AVG converts CPU clock cycles to nanoseconds and calculates the average cycle time. |

| Typedefs | |
| --- | --- |
| typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [k\_ticks\_t](group__clock__apis.md#ga9832cb0adc2d1866420e5c370a0863e2) |
|  | Tick precision used in timeout APIs. |

| Functions | |
| --- | --- |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [sys\_clock\_tick\_get\_32](group__clock__apis.md#ga38f64e34c3f5b179e1f65d96911823cd) (void) |
|  | Return the lower part of the current system tick count. |
| [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) | [sys\_clock\_tick\_get](group__clock__apis.md#ga53e768db46e328e433848c62739c82e0) (void) |
|  | Return the current system tick count. |
| [k\_timepoint\_t](structk__timepoint__t.md) | [sys\_timepoint\_calc](group__clock__apis.md#ga509cf4599c1f162c97540743e8c21d33) ([k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Calculate a timepoint value. |
| [k\_timeout\_t](structk__timeout__t.md) | [sys\_timepoint\_timeout](group__clock__apis.md#ga6f6d06ef8c13e2fa54c63831fc00ecaa) ([k\_timepoint\_t](structk__timepoint__t.md) timepoint) |
|  | Remaining time to given timepoint. |
| static int | [sys\_timepoint\_cmp](group__clock__apis.md#gaba264a00149527cd70aea717f3b3a998) ([k\_timepoint\_t](structk__timepoint__t.md) a, [k\_timepoint\_t](structk__timepoint__t.md) b) |
|  | Compare two timepoint values. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [sys\_timepoint\_expired](group__clock__apis.md#ga87d0d7a0f7bcdcc8c4909962eac12985) ([k\_timepoint\_t](structk__timepoint__t.md) timepoint) |
|  | Indicates if timepoint is expired. |

## Detailed Description

Variables needed for system clock.

Declare variables used by both system timer device driver and kernel components that use timer functionality.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [sys\_clock.h](sys__clock_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
