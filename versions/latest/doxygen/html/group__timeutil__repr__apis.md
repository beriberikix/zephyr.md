---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/group__timeutil__repr__apis.html
original_path: doxygen/html/group__timeutil__repr__apis.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Time Representation APIs

[Utilities](group__utilities.md) » [Time Utility APIs](group__timeutil__apis.md)

| Macros | |
| --- | --- |
| #define | [TIME\_UTILS\_BASE\_YEAR](#gaa61359e3ffe7df1994a9265a66834385)   1900 |

| Functions | |
| --- | --- |
| [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) | [timeutil\_timegm64](#gac4d2957df896a77eb317e10318adf481) (const struct [tm](structtm.md) \*[tm](structtm.md)) |
|  | Convert broken-down time to a POSIX epoch offset in seconds. |
| static void | [timespec\_from\_timeout](#gab9b5ccdfd7abeaf7a05ebf273cb4d022) ([k\_timeout\_t](structk__timeout__t.md) timeout, struct [timespec](structtimespec.md) \*ts) |
|  | Convert a kernel timeout to a timespec. |
| static [k\_timeout\_t](structk__timeout__t.md) | [timespec\_to\_timeout](#gac4262e7e4ebc2af52d21a18744d50169) (const struct [timespec](structtimespec.md) \*ts) |
|  | Convert a timespec to a kernel timeout. |

## Detailed Description

## Macro Definition Documentation

## [◆ ](#gaa61359e3ffe7df1994a9265a66834385)TIME\_UTILS\_BASE\_YEAR

| #define TIME\_UTILS\_BASE\_YEAR   1900 |
| --- |

`#include <[zephyr/sys/timeutil.h](timeutil_8h.md)>`

## Function Documentation

## [◆ ](#gab9b5ccdfd7abeaf7a05ebf273cb4d022)timespec\_from\_timeout()

| | void timespec\_from\_timeout | ( | [k\_timeout\_t](structk__timeout__t.md) | *timeout*, | | --- | --- | --- | --- | |  |  | struct [timespec](structtimespec.md) \* | *ts* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[zephyr/sys/timeutil.h](timeutil_8h.md)>`

Convert a kernel timeout to a timespec.

This function converts time durations expressed as Zephyr [k\_timeout\_t](structk__timeout__t.md "k_timeout_t") objects to struct [timespec](structtimespec.md) objects.

Parameters
:   |  | timeout | the kernel timeout to convert |
    | --- | --- | --- |
    | [out] | ts | the timespec to store the result |

## [◆ ](#gac4262e7e4ebc2af52d21a18744d50169)timespec\_to\_timeout()

| | [k\_timeout\_t](structk__timeout__t.md) timespec\_to\_timeout | ( | const struct [timespec](structtimespec.md) \* | *ts* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[zephyr/sys/timeutil.h](timeutil_8h.md)>`

Convert a timespec to a kernel timeout.

This function converts durations expressed as a struct [timespec](structtimespec.md) to Zephyr [k\_timeout\_t](structk__timeout__t.md "k_timeout_t") objects.

Given that the range of a struct [timespec](structtimespec.md) is much larger than the range of [k\_timeout\_t](structk__timeout__t.md "k_timeout_t"), and also given that the functions are only intended to be used to convert time durations (which are always positive), the function will saturate to [K\_NO\_WAIT](group__clock__apis.md#ga3d9541cfe2e8395af66d186efa77362f "K_NO_WAIT") if the tv\_sec field of *ts* is negative.

Similarly, if the duration is too large to fit in [k\_timeout\_t](structk__timeout__t.md "k_timeout_t"), the function will saturate to [K\_FOREVER](group__clock__apis.md#ga0bb4b83f0222193b21a8910311bab0ca "K_FOREVER").

Parameters
:   | ts | the timespec to convert |
    | --- | --- |

Returns
:   the kernel timeout

## [◆ ](#gac4d2957df896a77eb317e10318adf481)timeutil\_timegm64()

| [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) timeutil\_timegm64 | ( | const struct [tm](structtm.md) \* | *tm* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[zephyr/sys/timeutil.h](timeutil_8h.md)>`

Convert broken-down time to a POSIX epoch offset in seconds.

Parameters
:   | [tm](structtm.md) | pointer to broken down time. |
    | --- | --- |

Returns
:   the corresponding time in the POSIX epoch time scale.

See also
:   [http://man7.org/linux/man-pages/man3/timegm.3.html](http://man7.org/linux/man-pages/man3/timegm.3.html)

- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
