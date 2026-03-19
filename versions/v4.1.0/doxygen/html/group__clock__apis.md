---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__clock__apis.html
original_path: doxygen/html/group__clock__apis.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

System Clock APIs

[Kernel APIs](group__kernel__apis.md)

System Clock APIs.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [k\_timeout\_t](structk__timeout__t.md) |
|  | Kernel timeout type. [More...](structk__timeout__t.md#details) |
| struct | [k\_timepoint\_t](structk__timepoint__t.md) |
|  | Kernel timepoint type. [More...](structk__timepoint__t.md#details) |

| Macros | |
| --- | --- |
| #define | [K\_NO\_WAIT](#ga3d9541cfe2e8395af66d186efa77362f)   Z\_TIMEOUT\_NO\_WAIT |
|  | Generate null timeout delay. |
| #define | [K\_NSEC](#gae2f3a80170afc5fbce0337cdf5a4ce4c)(t) |
|  | Generate timeout delay from nanoseconds. |
| #define | [K\_USEC](#ga91198e325210ec052a8308e642058c0b)(t) |
|  | Generate timeout delay from microseconds. |
| #define | [K\_CYC](#gab41f59fd2b724cb1279e4f6821154b33)(t) |
|  | Generate timeout delay from cycles. |
| #define | [K\_TICKS](#gaeda983960bd25f1dba7a386ad720e395)(t) |
|  | Generate timeout delay from system ticks. |
| #define | [K\_MSEC](#ga302af954e87b10a9b731f1ad07775e9f)(ms) |
|  | Generate timeout delay from milliseconds. |
| #define | [K\_SECONDS](#gadc361472aea59267f6ea38f5e7c7ca2a)([s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d)) |
|  | Generate timeout delay from seconds. |
| #define | [K\_MINUTES](#gaef02f20d4d2ebfc9aa29acae01bd3698)(m) |
|  | Generate timeout delay from minutes. |
| #define | [K\_HOURS](#gaa9e0cd890db28965b66d4bc5d719a91f)(h) |
|  | Generate timeout delay from hours. |
| #define | [K\_FOREVER](#ga0bb4b83f0222193b21a8910311bab0ca)   Z\_FOREVER |
|  | Generate infinite timeout delay. |
| #define | [K\_TICKS\_FOREVER](#ga66e180b3d8940c30786a1d972cbd6d8d)   (([k\_ticks\_t](#ga9832cb0adc2d1866420e5c370a0863e2)) -1) |
| #define | [K\_TIMEOUT\_EQ](#ga9abf00b34e16ab7ad0883603b6778b1b)(a, b) |
|  | Compare timeouts for equality. |
| #define | [NSEC\_PER\_USEC](#ga2180f263d149841a7c1fde663edb84c5)   1000U |
|  | number of nanoseconds per microsecond |
| #define | [NSEC\_PER\_MSEC](#gad16e9029e202d2dfb4cfae8f09131f8f)   1000000U |
|  | number of nanoseconds per millisecond |
| #define | [USEC\_PER\_MSEC](#ga2d66311052e2bddf914610fb7345ff27)   1000U |
|  | number of microseconds per millisecond |
| #define | [MSEC\_PER\_SEC](#ga222f9dff749accf8de62bc4b52c7bdcd)   1000U |
|  | number of milliseconds per second |
| #define | [SEC\_PER\_MIN](#gac47b302f1b8d2a7a9c035c417247be76)   60U |
|  | number of seconds per minute |
| #define | [SEC\_PER\_HOUR](#ga2d540510d5860d7f190d13124956bc57)   3600U |
|  | number of seconds per hour |
| #define | [SEC\_PER\_DAY](#ga3aaee30ddedb3f6675aac341a66e39e2)   86400U |
|  | number of seconds per day |
| #define | [MIN\_PER\_HOUR](#gaa6094c8f66b81269ce912804b796d2c7)   60U |
|  | number of minutes per hour |
| #define | [HOUR\_PER\_DAY](#gafcbf34dc5c48a91fe5f6efe4c1bae745)   24U |
|  | number of hours per day |
| #define | [USEC\_PER\_SEC](#ga6a69d6cbdab5f24c2e66959293f210c1)   (([USEC\_PER\_MSEC](#ga2d66311052e2bddf914610fb7345ff27)) \* ([MSEC\_PER\_SEC](#ga222f9dff749accf8de62bc4b52c7bdcd))) |
|  | number of microseconds per second |
| #define | [NSEC\_PER\_SEC](#ga0501e82515b2bdf36453c4cc80f5e0cc)   (([NSEC\_PER\_USEC](#ga2180f263d149841a7c1fde663edb84c5)) \* ([USEC\_PER\_MSEC](#ga2d66311052e2bddf914610fb7345ff27)) \* ([MSEC\_PER\_SEC](#ga222f9dff749accf8de62bc4b52c7bdcd))) |
|  | number of nanoseconds per second |
| #define | [SYS\_CLOCK\_HW\_CYCLES\_TO\_NS\_AVG](#ga59d9bd47b0caa662f0e289cf3df83a82)(X, NCYCLES) |
|  | SYS\_CLOCK\_HW\_CYCLES\_TO\_NS\_AVG converts CPU clock cycles to nanoseconds and calculates the average cycle time. |

| Typedefs | |
| --- | --- |
| typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [k\_ticks\_t](#ga9832cb0adc2d1866420e5c370a0863e2) |
|  | Tick precision used in timeout APIs. |

| Functions | |
| --- | --- |
| void | [sys\_clock\_set\_timeout](#ga747c1f4a99a3bc48e7ec65d7bc5e4767) ([int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) ticks, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) idle) |
|  | Set system clock timeout. |
| void | [sys\_clock\_idle\_exit](#ga6ca2139000b8c75b1ed2c6c1f672ff79) (void) |
|  | Timer idle exit notification. |
| void | [sys\_clock\_announce](#gaa7d3b1bdb8d15c907aaafea3b96ac2b5) ([int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) ticks) |
|  | Announce time progress to the kernel. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [sys\_clock\_elapsed](#gaa9b6d8eebc69d2808beb0580d974bb84) (void) |
|  | Ticks elapsed since last [sys\_clock\_announce()](#gaa7d3b1bdb8d15c907aaafea3b96ac2b5) call. |
| void | [sys\_clock\_disable](#ga49c900ab49a72c347d0aefb14aecb550) (void) |
|  | Disable system timer. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [sys\_clock\_cycle\_get\_32](#ga42dcd1878309a82246dbfa26510f868a) (void) |
|  | Hardware cycle counter. |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [sys\_clock\_cycle\_get\_64](#ga25328a181bd0229ef5110c15e8452fc1) (void) |
|  | 64 bit hardware cycle counter |
| [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) | [k\_uptime\_ticks](#ga8f143af2ee4ad42d9f7817ef161cbd13) (void) |
|  | Get system uptime, in system ticks. |
| static [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) | [k\_uptime\_get](#gae3e992cd3257c23d5b26d765fcbb2b69) (void) |
|  | Get system uptime. |
| static [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [k\_uptime\_get\_32](#ga9253cfb7b46af4d8994349323ce9872b) (void) |
|  | Get system uptime (32-bit version). |
| static [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [k\_uptime\_seconds](#gae082928ea608a8b180b4cb3a79d21a24) (void) |
|  | Get system uptime in seconds. |
| static [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) | [k\_uptime\_delta](#gad748b2fe83b36884dc087b4af367de80) ([int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) \*reftime) |
|  | Get elapsed time. |
| static [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [k\_cycle\_get\_32](#ga208687de625e0036558343b4e66143d3) (void) |
|  | Read the hardware clock. |
| static [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [k\_cycle\_get\_64](#gae09f509d02bf75a7b45d2800d823bb3a) (void) |
|  | Read the 64-bit hardware clock. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [sys\_clock\_tick\_get\_32](#ga38f64e34c3f5b179e1f65d96911823cd) (void) |
|  | Return the lower part of the current system tick count. |
| [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) | [sys\_clock\_tick\_get](#ga53e768db46e328e433848c62739c82e0) (void) |
|  | Return the current system tick count. |
| [k\_timepoint\_t](structk__timepoint__t.md) | [sys\_timepoint\_calc](#ga509cf4599c1f162c97540743e8c21d33) ([k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Calculate a timepoint value. |
| [k\_timeout\_t](structk__timeout__t.md) | [sys\_timepoint\_timeout](#ga6f6d06ef8c13e2fa54c63831fc00ecaa) ([k\_timepoint\_t](structk__timepoint__t.md) timepoint) |
|  | Remaining time to given timepoint. |
| static int | [sys\_timepoint\_cmp](#gaba264a00149527cd70aea717f3b3a998) ([k\_timepoint\_t](structk__timepoint__t.md) a, [k\_timepoint\_t](structk__timepoint__t.md) b) |
|  | Compare two timepoint values. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [sys\_timepoint\_expired](#ga87d0d7a0f7bcdcc8c4909962eac12985) ([k\_timepoint\_t](structk__timepoint__t.md) timepoint) |
|  | Indicates if timepoint is expired. |

## Detailed Description

System Clock APIs.

## Macro Definition Documentation

## [◆ ](#gafcbf34dc5c48a91fe5f6efe4c1bae745)HOUR\_PER\_DAY

| #define HOUR\_PER\_DAY   24U |
| --- |

`#include <[sys_clock.h](sys__clock_8h.md)>`

number of hours per day

## [◆ ](#gab41f59fd2b724cb1279e4f6821154b33)K\_CYC

| #define K\_CYC | ( |  | *t* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[kernel.h](kernel_8h.md)>`

**Value:**

Z\_TIMEOUT\_CYC(t)

Generate timeout delay from cycles.

This macro generates a timeout delay that instructs a kernel API to wait up to *t* cycles to perform the requested operation.

Parameters
:   | t | Duration in cycles. |
    | --- | --- |

Returns
:   Timeout delay value.

## [◆ ](#ga0bb4b83f0222193b21a8910311bab0ca)K\_FOREVER

| #define K\_FOREVER   Z\_FOREVER |
| --- |

`#include <[kernel.h](kernel_8h.md)>`

Generate infinite timeout delay.

This macro generates a timeout delay that instructs a kernel API to wait as long as necessary to perform the requested operation.

Returns
:   Timeout delay value.

## [◆ ](#gaa9e0cd890db28965b66d4bc5d719a91f)K\_HOURS

| #define K\_HOURS | ( |  | *h* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[kernel.h](kernel_8h.md)>`

**Value:**

[K\_MINUTES](#gaef02f20d4d2ebfc9aa29acae01bd3698)((h) \* 60)

[K\_MINUTES](#gaef02f20d4d2ebfc9aa29acae01bd3698)

#define K\_MINUTES(m)

Generate timeout delay from minutes.

**Definition** kernel.h:1445

Generate timeout delay from hours.

This macro generates a timeout delay that instructs a kernel API to wait up to *h* hours to perform the requested operation.

Parameters
:   | h | Duration in hours. |
    | --- | --- |

Returns
:   Timeout delay value.

## [◆ ](#gaef02f20d4d2ebfc9aa29acae01bd3698)K\_MINUTES

| #define K\_MINUTES | ( |  | *m* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[kernel.h](kernel_8h.md)>`

**Value:**

[K\_SECONDS](#gadc361472aea59267f6ea38f5e7c7ca2a)((m) \* 60)

[K\_SECONDS](#gadc361472aea59267f6ea38f5e7c7ca2a)

#define K\_SECONDS(s)

Generate timeout delay from seconds.

**Definition** kernel.h:1433

Generate timeout delay from minutes.

This macro generates a timeout delay that instructs a kernel API to wait up to *m* minutes to perform the requested operation.

Parameters
:   | m | Duration in minutes. |
    | --- | --- |

Returns
:   Timeout delay value.

## [◆ ](#ga302af954e87b10a9b731f1ad07775e9f)K\_MSEC

| #define K\_MSEC | ( |  | *ms* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[kernel.h](kernel_8h.md)>`

**Value:**

Z\_TIMEOUT\_MS(ms)

Generate timeout delay from milliseconds.

This macro generates a timeout delay that instructs a kernel API to wait up to *ms* milliseconds to perform the requested operation.

Parameters
:   | ms | Duration in milliseconds. |
    | --- | --- |

Returns
:   Timeout delay value.

## [◆ ](#ga3d9541cfe2e8395af66d186efa77362f)K\_NO\_WAIT

| #define K\_NO\_WAIT   Z\_TIMEOUT\_NO\_WAIT |
| --- |

`#include <[kernel.h](kernel_8h.md)>`

Generate null timeout delay.

This macro generates a timeout delay that instructs a kernel API not to wait if the requested operation cannot be performed immediately.

Returns
:   Timeout delay value.

## [◆ ](#gae2f3a80170afc5fbce0337cdf5a4ce4c)K\_NSEC

| #define K\_NSEC | ( |  | *t* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[kernel.h](kernel_8h.md)>`

**Value:**

Z\_TIMEOUT\_NS(t)

Generate timeout delay from nanoseconds.

This macro generates a timeout delay that instructs a kernel API to wait up to *t* nanoseconds to perform the requested operation. Note that timer precision is limited to the tick rate, not the requested value.

Parameters
:   | t | Duration in nanoseconds. |
    | --- | --- |

Returns
:   Timeout delay value.

## [◆ ](#gadc361472aea59267f6ea38f5e7c7ca2a)K\_SECONDS

| #define K\_SECONDS | ( |  | *[s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d)* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[kernel.h](kernel_8h.md)>`

**Value:**

[K\_MSEC](#ga302af954e87b10a9b731f1ad07775e9f)(([s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d)) \* [MSEC\_PER\_SEC](#ga222f9dff749accf8de62bc4b52c7bdcd))

[s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d)

irp nz macro MOVR cc s mov cc s endm endr irp aw macro LDR aa s

**Definition** asm-macro-32-bit-gnu.h:17

[MSEC\_PER\_SEC](#ga222f9dff749accf8de62bc4b52c7bdcd)

#define MSEC\_PER\_SEC

number of milliseconds per second

**Definition** sys\_clock.h:92

[K\_MSEC](#ga302af954e87b10a9b731f1ad07775e9f)

#define K\_MSEC(ms)

Generate timeout delay from milliseconds.

**Definition** kernel.h:1421

Generate timeout delay from seconds.

This macro generates a timeout delay that instructs a kernel API to wait up to *s* seconds to perform the requested operation.

Parameters
:   | [s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d) | Duration in seconds. |
    | --- | --- |

Returns
:   Timeout delay value.

## [◆ ](#gaeda983960bd25f1dba7a386ad720e395)K\_TICKS

| #define K\_TICKS | ( |  | *t* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[kernel.h](kernel_8h.md)>`

**Value:**

Z\_TIMEOUT\_TICKS(t)

Generate timeout delay from system ticks.

This macro generates a timeout delay that instructs a kernel API to wait up to *t* ticks to perform the requested operation.

Parameters
:   | t | Duration in system ticks. |
    | --- | --- |

Returns
:   Timeout delay value.

## [◆ ](#ga66e180b3d8940c30786a1d972cbd6d8d)K\_TICKS\_FOREVER

| #define K\_TICKS\_FOREVER   (([k\_ticks\_t](#ga9832cb0adc2d1866420e5c370a0863e2)) -1) |
| --- |

`#include <[sys_clock.h](sys__clock_8h.md)>`

## [◆ ](#ga9abf00b34e16ab7ad0883603b6778b1b)K\_TIMEOUT\_EQ

| #define K\_TIMEOUT\_EQ | ( |  | *a*, |
| --- | --- | --- | --- |
|  |  |  | *b* ) |

`#include <[sys_clock.h](sys__clock_8h.md)>`

**Value:**

((a).ticks == (b).ticks)

Compare timeouts for equality.

The [k\_timeout\_t](structk__timeout__t.md "Kernel timeout type.") object is an opaque struct that should not be inspected by application code. This macro exists so that users can test timeout objects for equality with known constants (e.g. K\_NO\_WAIT and K\_FOREVER) when implementing their own APIs in terms of Zephyr timeout constants.

Returns
:   True if the timeout objects are identical

## [◆ ](#ga91198e325210ec052a8308e642058c0b)K\_USEC

| #define K\_USEC | ( |  | *t* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[kernel.h](kernel_8h.md)>`

**Value:**

Z\_TIMEOUT\_US(t)

Generate timeout delay from microseconds.

This macro generates a timeout delay that instructs a kernel API to wait up to *t* microseconds to perform the requested operation. Note that timer precision is limited to the tick rate, not the requested value.

Parameters
:   | t | Duration in microseconds. |
    | --- | --- |

Returns
:   Timeout delay value.

## [◆ ](#gaa6094c8f66b81269ce912804b796d2c7)MIN\_PER\_HOUR

| #define MIN\_PER\_HOUR   60U |
| --- |

`#include <[sys_clock.h](sys__clock_8h.md)>`

number of minutes per hour

## [◆ ](#ga222f9dff749accf8de62bc4b52c7bdcd)MSEC\_PER\_SEC

| #define MSEC\_PER\_SEC   1000U |
| --- |

`#include <[sys_clock.h](sys__clock_8h.md)>`

number of milliseconds per second

## [◆ ](#gad16e9029e202d2dfb4cfae8f09131f8f)NSEC\_PER\_MSEC

| #define NSEC\_PER\_MSEC   1000000U |
| --- |

`#include <[sys_clock.h](sys__clock_8h.md)>`

number of nanoseconds per millisecond

## [◆ ](#ga0501e82515b2bdf36453c4cc80f5e0cc)NSEC\_PER\_SEC

| #define NSEC\_PER\_SEC   (([NSEC\_PER\_USEC](#ga2180f263d149841a7c1fde663edb84c5)) \* ([USEC\_PER\_MSEC](#ga2d66311052e2bddf914610fb7345ff27)) \* ([MSEC\_PER\_SEC](#ga222f9dff749accf8de62bc4b52c7bdcd))) |
| --- |

`#include <[sys_clock.h](sys__clock_8h.md)>`

number of nanoseconds per second

## [◆ ](#ga2180f263d149841a7c1fde663edb84c5)NSEC\_PER\_USEC

| #define NSEC\_PER\_USEC   1000U |
| --- |

`#include <[sys_clock.h](sys__clock_8h.md)>`

number of nanoseconds per microsecond

## [◆ ](#ga3aaee30ddedb3f6675aac341a66e39e2)SEC\_PER\_DAY

| #define SEC\_PER\_DAY   86400U |
| --- |

`#include <[sys_clock.h](sys__clock_8h.md)>`

number of seconds per day

## [◆ ](#ga2d540510d5860d7f190d13124956bc57)SEC\_PER\_HOUR

| #define SEC\_PER\_HOUR   3600U |
| --- |

`#include <[sys_clock.h](sys__clock_8h.md)>`

number of seconds per hour

## [◆ ](#gac47b302f1b8d2a7a9c035c417247be76)SEC\_PER\_MIN

| #define SEC\_PER\_MIN   60U |
| --- |

`#include <[sys_clock.h](sys__clock_8h.md)>`

number of seconds per minute

## [◆ ](#ga59d9bd47b0caa662f0e289cf3df83a82)SYS\_CLOCK\_HW\_CYCLES\_TO\_NS\_AVG

| #define SYS\_CLOCK\_HW\_CYCLES\_TO\_NS\_AVG | ( |  | *X*, |
| --- | --- | --- | --- |
|  |  |  | *NCYCLES* ) |

`#include <[sys_clock.h](sys__clock_8h.md)>`

**Value:**

([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f))([k\_cyc\_to\_ns\_floor64](group__timeutil__unit__apis.md#ga665d5fc98ffe8bd1cf78ca994f58724a)(X) / NCYCLES)

[k\_cyc\_to\_ns\_floor64](group__timeutil__unit__apis.md#ga665d5fc98ffe8bd1cf78ca994f58724a)

#define k\_cyc\_to\_ns\_floor64(t)

Convert hardware cycles to nanoseconds.

**Definition** time\_units.h:1435

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

SYS\_CLOCK\_HW\_CYCLES\_TO\_NS\_AVG converts CPU clock cycles to nanoseconds and calculates the average cycle time.

## [◆ ](#ga2d66311052e2bddf914610fb7345ff27)USEC\_PER\_MSEC

| #define USEC\_PER\_MSEC   1000U |
| --- |

`#include <[sys_clock.h](sys__clock_8h.md)>`

number of microseconds per millisecond

## [◆ ](#ga6a69d6cbdab5f24c2e66959293f210c1)USEC\_PER\_SEC

| #define USEC\_PER\_SEC   (([USEC\_PER\_MSEC](#ga2d66311052e2bddf914610fb7345ff27)) \* ([MSEC\_PER\_SEC](#ga222f9dff749accf8de62bc4b52c7bdcd))) |
| --- |

`#include <[sys_clock.h](sys__clock_8h.md)>`

number of microseconds per second

## Typedef Documentation

## [◆ ](#ga9832cb0adc2d1866420e5c370a0863e2)k\_ticks\_t

| typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [k\_ticks\_t](#ga9832cb0adc2d1866420e5c370a0863e2) |
| --- |

`#include <[sys_clock.h](sys__clock_8h.md)>`

Tick precision used in timeout APIs.

This type defines the word size of the timeout values used in [k\_timeout\_t](structk__timeout__t.md "Kernel timeout type.") objects, and thus defines an upper bound on maximum timeout length (or equivalently minimum tick duration). Note that this does not affect the size of the system uptime counter, which is always a 64 bit count of ticks.

## Function Documentation

## [◆ ](#ga208687de625e0036558343b4e66143d3)k\_cycle\_get\_32()

| | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) k\_cycle\_get\_32 | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[kernel.h](kernel_8h.md)>`

Read the hardware clock.

This routine returns the current time, as measured by the system's hardware clock.

Returns
:   Current hardware clock up-counter (in cycles).

## [◆ ](#gae09f509d02bf75a7b45d2800d823bb3a)k\_cycle\_get\_64()

| | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) k\_cycle\_get\_64 | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[kernel.h](kernel_8h.md)>`

Read the 64-bit hardware clock.

This routine returns the current time in 64-bits, as measured by the system's hardware clock, if available.

See also
:   CONFIG\_TIMER\_HAS\_64BIT\_CYCLE\_COUNTER

Returns
:   Current hardware clock up-counter (in cycles).

## [◆ ](#gad748b2fe83b36884dc087b4af367de80)k\_uptime\_delta()

| | [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) k\_uptime\_delta | ( | [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) \* | *reftime* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[kernel.h](kernel_8h.md)>`

Get elapsed time.

This routine computes the elapsed time between the current system uptime and an earlier reference time, in milliseconds.

Parameters
:   | reftime | Pointer to a reference time, which is updated to the current uptime upon return. |
    | --- | --- |

Returns
:   Elapsed time.

## [◆ ](#gae3e992cd3257c23d5b26d765fcbb2b69)k\_uptime\_get()

| | [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) k\_uptime\_get | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[kernel.h](kernel_8h.md)>`

Get system uptime.

This routine returns the elapsed time since the system booted, in milliseconds.

Note
:   While this function returns time in milliseconds, it does not mean it has millisecond resolution. The actual resolution depends on `CONFIG_SYS_CLOCK_TICKS_PER_SEC` config option.

Returns
:   Current uptime in milliseconds.

## [◆ ](#ga9253cfb7b46af4d8994349323ce9872b)k\_uptime\_get\_32()

| | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) k\_uptime\_get\_32 | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[kernel.h](kernel_8h.md)>`

Get system uptime (32-bit version).

This routine returns the lower 32 bits of the system uptime in milliseconds.

Because correct conversion requires full precision of the system clock there is no benefit to using this over [k\_uptime\_get()](#gae3e992cd3257c23d5b26d765fcbb2b69) unless you know the application will never run long enough for the system clock to approach 2^32 ticks. Calls to this function may involve interrupt blocking and 64-bit math.

Note
:   While this function returns time in milliseconds, it does not mean it has millisecond resolution. The actual resolution depends on `CONFIG_SYS_CLOCK_TICKS_PER_SEC` config option

Returns
:   The low 32 bits of the current uptime, in milliseconds.

## [◆ ](#gae082928ea608a8b180b4cb3a79d21a24)k\_uptime\_seconds()

| | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) k\_uptime\_seconds | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[kernel.h](kernel_8h.md)>`

Get system uptime in seconds.

This routine returns the elapsed time since the system booted, in seconds.

Returns
:   Current uptime in seconds.

## [◆ ](#ga8f143af2ee4ad42d9f7817ef161cbd13)k\_uptime\_ticks()

| [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) k\_uptime\_ticks | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[kernel.h](kernel_8h.md)>`

Get system uptime, in system ticks.

This routine returns the elapsed time since the system booted, in ticks (c.f. `CONFIG_SYS_CLOCK_TICKS_PER_SEC`), which is the fundamental unit of resolution of kernel timekeeping.

Returns
:   Current uptime in ticks.

## [◆ ](#gaa7d3b1bdb8d15c907aaafea3b96ac2b5)sys\_clock\_announce()

| void sys\_clock\_announce | ( | [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) | *ticks* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[system_timer.h](system__timer_8h.md)>`

Announce time progress to the kernel.

Informs the kernel that the specified number of ticks have elapsed since the last call to [sys\_clock\_announce()](#gaa7d3b1bdb8d15c907aaafea3b96ac2b5) (or system startup for the first call). The timer driver is expected to delivery these announcements as close as practical (subject to hardware and latency limitations) to tick boundaries.

Parameters
:   | ticks | Elapsed time, in ticks |
    | --- | --- |

## [◆ ](#ga42dcd1878309a82246dbfa26510f868a)sys\_clock\_cycle\_get\_32()

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) sys\_clock\_cycle\_get\_32 | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[system_timer.h](system__timer_8h.md)>`

Hardware cycle counter.

Timer drivers are generally responsible for the system cycle counter as well as the tick announcements. This function is generally called out of the architecture layer (

See also
:   [arch\_k\_cycle\_get\_32()](arc_2v2_2misc_8h.md#a9ee9f897ec750957de45bf8d43349d5e)) to implement the cycle counter, though the user-facing API is owned by the architecture, not the driver. The rate must match CONFIG\_SYS\_CLOCK\_HW\_CYCLES\_PER\_SEC.

Note
:   If the counter clock is large enough for this to wrap its full range within a few seconds (i.e. CONFIG\_SYS\_CLOCK\_HW\_CYCLES\_PER\_SEC is greater than 50Mhz) then it is recommended to also implement [sys\_clock\_cycle\_get\_64()](#ga25328a181bd0229ef5110c15e8452fc1).

Returns
:   The current cycle time. This should count up monotonically through the full 32 bit space, wrapping at 0xffffffff. Hardware with fewer bits of precision in the timer is expected to synthesize a 32 bit count.

## [◆ ](#ga25328a181bd0229ef5110c15e8452fc1)sys\_clock\_cycle\_get\_64()

| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) sys\_clock\_cycle\_get\_64 | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[system_timer.h](system__timer_8h.md)>`

64 bit hardware cycle counter

As for [sys\_clock\_cycle\_get\_32()](#ga42dcd1878309a82246dbfa26510f868a), but with a 64 bit return value. Not all hardware has 64 bit counters. This function need be implemented only if CONFIG\_TIMER\_HAS\_64BIT\_CYCLE\_COUNTER is set.

Note
:   If the counter clock is large enough for [sys\_clock\_cycle\_get\_32()](#ga42dcd1878309a82246dbfa26510f868a) to wrap its full range within a few seconds (i.e. CONFIG\_SYS\_CLOCK\_HW\_CYCLES\_PER\_SEC is greater than 50Mhz) then it is recommended to implement this API.

Returns
:   The current cycle time. This should count up monotonically through the full 64 bit space, wrapping at 2^64-1. Hardware with fewer bits of precision in the timer is generally not expected to implement this API.

## [◆ ](#ga49c900ab49a72c347d0aefb14aecb550)sys\_clock\_disable()

| void sys\_clock\_disable | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[system_timer.h](system__timer_8h.md)>`

Disable system timer.

Note
:   Not all system timer drivers has the capability of being disabled. The config `CONFIG_SYSTEM_TIMER_HAS_DISABLE_SUPPORT` can be used to check if the system timer has the capability of being disabled.

## [◆ ](#gaa9b6d8eebc69d2808beb0580d974bb84)sys\_clock\_elapsed()

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) sys\_clock\_elapsed | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[system_timer.h](system__timer_8h.md)>`

Ticks elapsed since last [sys\_clock\_announce()](#gaa7d3b1bdb8d15c907aaafea3b96ac2b5) call.

Queries the clock driver for the current time elapsed since the last call to [sys\_clock\_announce()](#gaa7d3b1bdb8d15c907aaafea3b96ac2b5) was made. The kernel will call this with appropriate locking, the driver needs only provide an instantaneous answer.

## [◆ ](#ga6ca2139000b8c75b1ed2c6c1f672ff79)sys\_clock\_idle\_exit()

| void sys\_clock\_idle\_exit | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[system_timer.h](system__timer_8h.md)>`

Timer idle exit notification.

This notifies the timer driver that the system is exiting the idle and allows it to do whatever bookkeeping is needed to restore timer operation and compute elapsed ticks.

Note
:   Legacy timer drivers also use this opportunity to call back into [sys\_clock\_announce()](#gaa7d3b1bdb8d15c907aaafea3b96ac2b5) to notify the kernel of expired ticks. This is allowed for compatibility, but not recommended. The kernel will figure that out on its own.

## [◆ ](#ga747c1f4a99a3bc48e7ec65d7bc5e4767)sys\_clock\_set\_timeout()

| void sys\_clock\_set\_timeout | ( | [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) | *ticks*, |
| --- | --- | --- | --- |
|  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *idle* ) |

`#include <[system_timer.h](system__timer_8h.md)>`

Set system clock timeout.

Informs the system clock driver that the next needed call to [sys\_clock\_announce()](#gaa7d3b1bdb8d15c907aaafea3b96ac2b5) will not be until the specified number of ticks from the current time have elapsed. Note that spurious calls to [sys\_clock\_announce()](#gaa7d3b1bdb8d15c907aaafea3b96ac2b5) are allowed (i.e. it's legal to announce every tick and implement this function as a noop), the requirement is that one tick announcement should occur within one tick BEFORE the specified expiration (that is, passing ticks==1 means "announce
the next tick", this convention was chosen to match legacy usage). Similarly a ticks value of zero (or even negative) is legal and treated identically: it simply indicates the kernel would like the next tick announcement as soon as possible.

Note that ticks can also be passed the special value K\_TICKS\_FOREVER, indicating that no future timer interrupts are expected or required and that the system is permitted to enter an indefinite sleep even if this could cause rollover of the internal counter (i.e. the system uptime counter is allowed to be wrong

Note also that it is conventional for the kernel to pass INT\_MAX for ticks if it wants to preserve the uptime tick count but doesn't have a specific event to await. The intent here is that the driver will schedule any needed timeout as far into the future as possible. For the specific case of INT\_MAX, the next call to [sys\_clock\_announce()](#gaa7d3b1bdb8d15c907aaafea3b96ac2b5) may occur at any point in the future, not just at INT\_MAX ticks. But the correspondence between the announced ticks and real-world time must be correct.

A final note about SMP: note that the call to [sys\_clock\_set\_timeout()](#ga747c1f4a99a3bc48e7ec65d7bc5e4767) is made on any CPU, and reflects the next timeout desired globally. The resulting calls(s) to [sys\_clock\_announce()](#gaa7d3b1bdb8d15c907aaafea3b96ac2b5) must be properly serialized by the driver such that a given tick is announced exactly once across the system. The kernel does not (cannot, really) attempt to serialize things by "assigning" timeouts to specific CPUs.

Parameters
:   | ticks | Timeout in tick units |
    | --- | --- |
    | idle | Hint to the driver that the system is about to enter the idle state immediately after setting the timeout |

## [◆ ](#ga53e768db46e328e433848c62739c82e0)sys\_clock\_tick\_get()

| [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) sys\_clock\_tick\_get | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[sys_clock.h](sys__clock_8h.md)>`

Return the current system tick count.

Returns
:   the current system tick count

## [◆ ](#ga38f64e34c3f5b179e1f65d96911823cd)sys\_clock\_tick\_get\_32()

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) sys\_clock\_tick\_get\_32 | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[sys_clock.h](sys__clock_8h.md)>`

Return the lower part of the current system tick count.

Returns
:   the current system tick count

## [◆ ](#ga509cf4599c1f162c97540743e8c21d33)sys\_timepoint\_calc()

| [k\_timepoint\_t](structk__timepoint__t.md) sys\_timepoint\_calc | ( | [k\_timeout\_t](structk__timeout__t.md) | *timeout* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[sys_clock.h](sys__clock_8h.md)>`

Calculate a timepoint value.

Returns a timepoint corresponding to the expiration (relative to an unlocked "now"!) of a timeout object. When used correctly, this should be called once, synchronously with the user passing a new timeout value. It should not be used iteratively to adjust a timeout (see [sys\_timepoint\_timeout()](#ga6f6d06ef8c13e2fa54c63831fc00ecaa) for that purpose).

Parameters
:   | timeout | Timeout value relative to current time (may also be [K\_FOREVER](#ga0bb4b83f0222193b21a8910311bab0ca) or [K\_NO\_WAIT](#ga3d9541cfe2e8395af66d186efa77362f)). |
    | --- | --- |

Return values
:   | Timepoint | value corresponding to given timeout |
    | --- | --- |

See also
:   [sys\_timepoint\_timeout()](#ga6f6d06ef8c13e2fa54c63831fc00ecaa)
:   [sys\_timepoint\_expired()](#ga87d0d7a0f7bcdcc8c4909962eac12985)

## [◆ ](#gaba264a00149527cd70aea717f3b3a998)sys\_timepoint\_cmp()

| | int sys\_timepoint\_cmp | ( | [k\_timepoint\_t](structk__timepoint__t.md) | *a*, | | --- | --- | --- | --- | |  |  | [k\_timepoint\_t](structk__timepoint__t.md) | *b* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[sys_clock.h](sys__clock_8h.md)>`

Compare two timepoint values.

This function is used to compare two timepoint values.

Parameters
:   | a | Timepoint to compare |
    | --- | --- |
    | b | Timepoint to compare against. |

Returns
:   zero if both timepoints are the same. Negative value if timepoint *a* is before timepoint *b*, positive otherwise.

## [◆ ](#ga87d0d7a0f7bcdcc8c4909962eac12985)sys\_timepoint\_expired()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) sys\_timepoint\_expired | ( | [k\_timepoint\_t](structk__timepoint__t.md) | *timepoint* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[sys_clock.h](sys__clock_8h.md)>`

Indicates if timepoint is expired.

Parameters
:   | timepoint | Timepoint to evaluate |
    | --- | --- |

Return values
:   | [true](stdbool_8h.md#a41f9c5fb8b08eb5dc3edce4dcb37fee7) | if the timepoint is in the past, false otherwise |
    | --- | --- |

See also
:   [sys\_timepoint\_calc()](#ga509cf4599c1f162c97540743e8c21d33)

## [◆ ](#ga6f6d06ef8c13e2fa54c63831fc00ecaa)sys\_timepoint\_timeout()

| [k\_timeout\_t](structk__timeout__t.md) sys\_timepoint\_timeout | ( | [k\_timepoint\_t](structk__timepoint__t.md) | *timepoint* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[sys_clock.h](sys__clock_8h.md)>`

Remaining time to given timepoint.

Returns the timeout interval between current time and provided timepoint. If the timepoint is now in the past or if it was created with [K\_NO\_WAIT](#ga3d9541cfe2e8395af66d186efa77362f) then [K\_NO\_WAIT](#ga3d9541cfe2e8395af66d186efa77362f) is returned. If it was created with [K\_FOREVER](#ga0bb4b83f0222193b21a8910311bab0ca) then [K\_FOREVER](#ga0bb4b83f0222193b21a8910311bab0ca) is returned.

Parameters
:   | timepoint | Timepoint for which a timeout value is wanted. |
    | --- | --- |

Return values
:   | Corresponding | timeout value. |
    | --- | --- |

See also
:   [sys\_timepoint\_calc()](#ga509cf4599c1f162c97540743e8c21d33)

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
