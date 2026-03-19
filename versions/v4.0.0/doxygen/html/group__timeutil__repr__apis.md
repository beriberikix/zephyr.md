---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/group__timeutil__repr__apis.html
original_path: doxygen/html/group__timeutil__repr__apis.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
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

## Detailed Description

## Macro Definition Documentation

## [◆ ](#gaa61359e3ffe7df1994a9265a66834385)TIME\_UTILS\_BASE\_YEAR

| #define TIME\_UTILS\_BASE\_YEAR   1900 |
| --- |

`#include <[timeutil.h](timeutil_8h.md)>`

## Function Documentation

## [◆ ](#gac4d2957df896a77eb317e10318adf481)timeutil\_timegm64()

| [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) timeutil\_timegm64 | ( | const struct [tm](structtm.md) \* | *tm* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[timeutil.h](timeutil_8h.md)>`

Convert broken-down time to a POSIX epoch offset in seconds.

Parameters
:   | [tm](structtm.md) | pointer to broken down time. |
    | --- | --- |

Returns
:   the corresponding time in the POSIX epoch time scale.

See also
:   [http://man7.org/linux/man-pages/man3/timegm.3.html](http://man7.org/linux/man-pages/man3/timegm.3.html)

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
