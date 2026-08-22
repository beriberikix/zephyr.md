---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/group__timeutil__timespec__apis.html
original_path: doxygen/html/group__timeutil__timespec__apis.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Timespec Utility APIs

[Utilities](group__utilities.md) » [Time Utility APIs](group__timeutil__apis.md)

| Functions | |
| --- | --- |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [timespec\_is\_valid](#ga2426889e703021e8b6f8a0ccab885bb6) (const struct [timespec](structtimespec.md) \*ts) |
|  | Check if a timespec is valid. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [timespec\_normalize](#ga4a0d4891eb6aef6543b1992566729f6c) (struct [timespec](structtimespec.md) \*ts) |
|  | Normalize a timespec so that the tv\_nsec field is in valid range. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [timespec\_add](#ga81026756e417d086b4f53306d04c8d10) (struct [timespec](structtimespec.md) \*a, const struct [timespec](structtimespec.md) \*b) |
|  | Add one timespec to another. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [timespec\_negate](#ga38216267ef6ca24e2b05d77104f5837a) (struct [timespec](structtimespec.md) \*ts) |
|  | Negate a timespec object. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [timespec\_sub](#gae0511602aea1fecc0b204e28ae91e7d0) (struct [timespec](structtimespec.md) \*a, const struct [timespec](structtimespec.md) \*b) |
|  | Subtract one timespec from another. |
| static int | [timespec\_compare](#gafa281a298f8b2f011875bb00094260fc) (const struct [timespec](structtimespec.md) \*a, const struct [timespec](structtimespec.md) \*b) |
|  | Compare two timespec objects. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [timespec\_equal](#gaedc15d71f9eee8e243c070a3e07d919f) (const struct [timespec](structtimespec.md) \*a, const struct [timespec](structtimespec.md) \*b) |
|  | Check if two timespec objects are equal. |

## Detailed Description

## Function Documentation

## [◆ ](#ga81026756e417d086b4f53306d04c8d10)timespec\_add()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) timespec\_add | ( | struct [timespec](structtimespec.md) \* | *a*, | | --- | --- | --- | --- | |  |  | const struct [timespec](structtimespec.md) \* | *b* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[zephyr/sys/timeutil.h](timeutil_8h.md)>`

Add one timespec to another.

This function sums the two timespecs pointed to by `a` and `b` and stores the result in the timespce pointed to by `a`.

If the operation would result in integer overflow, return value is [false](stdbool_8h.md#a65e9886d74aaee76545e83dd09011727).

Note
:   `a` and `b` must be non-[NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4) and normalized.

Parameters
:   | a | the timespec which is added to |
    | --- | --- |
    | b | the timespec to be added |

Returns
:   [true](stdbool_8h.md#a41f9c5fb8b08eb5dc3edce4dcb37fee7) if the operation was successful, otherwise [false](stdbool_8h.md#a65e9886d74aaee76545e83dd09011727).

## [◆ ](#gafa281a298f8b2f011875bb00094260fc)timespec\_compare()

| | int timespec\_compare | ( | const struct [timespec](structtimespec.md) \* | *a*, | | --- | --- | --- | --- | |  |  | const struct [timespec](structtimespec.md) \* | *b* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[zephyr/sys/timeutil.h](timeutil_8h.md)>`

Compare two timespec objects.

This function compares two timespec objects pointed to by `a` and `b`.

Note
:   `a` and `b` must be non-[NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4) and normalized.

Parameters
:   | a | the first timespec to compare |
    | --- | --- |
    | b | the second timespec to compare |

Returns
:   -1, 0, or +1 if *a* is less than, equal to, or greater than *b*, respectively.

## [◆ ](#gaedc15d71f9eee8e243c070a3e07d919f)timespec\_equal()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) timespec\_equal | ( | const struct [timespec](structtimespec.md) \* | *a*, | | --- | --- | --- | --- | |  |  | const struct [timespec](structtimespec.md) \* | *b* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[zephyr/sys/timeutil.h](timeutil_8h.md)>`

Check if two timespec objects are equal.

This function checks if the two timespec objects pointed to by `a` and `b` are equal.

Note
:   `a` and `b` must be non-[NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4) are not required to be normalized.

Parameters
:   | a | the first timespec to compare |
    | --- | --- |
    | b | the second timespec to compare |

Returns
:   true if the two timespec objects are equal, otherwise false.

## [◆ ](#ga2426889e703021e8b6f8a0ccab885bb6)timespec\_is\_valid()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) timespec\_is\_valid | ( | const struct [timespec](structtimespec.md) \* | *ts* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[zephyr/sys/timeutil.h](timeutil_8h.md)>`

Check if a timespec is valid.

Check if a timespec is valid (i.e. normalized) by ensuring that the tv\_nsec field is in the range [0, NSEC\_PER\_SEC-1].

Note
:   `ts` must not be [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4).

Parameters
:   | ts | the timespec to check |
    | --- | --- |

Returns
:   [true](stdbool_8h.md#a41f9c5fb8b08eb5dc3edce4dcb37fee7) if the timespec is valid, otherwise [false](stdbool_8h.md#a65e9886d74aaee76545e83dd09011727).

## [◆ ](#ga38216267ef6ca24e2b05d77104f5837a)timespec\_negate()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) timespec\_negate | ( | struct [timespec](structtimespec.md) \* | *ts* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[zephyr/sys/timeutil.h](timeutil_8h.md)>`

Negate a timespec object.

Negate the timespec object pointed to by `ts` and store the result in the same memory location.

If the operation would result in integer overflow, return value is [false](stdbool_8h.md#a65e9886d74aaee76545e83dd09011727).

Parameters
:   | ts | The timespec object to negate. |
    | --- | --- |

Returns
:   [true](stdbool_8h.md#a41f9c5fb8b08eb5dc3edce4dcb37fee7) of the operation is successful, otherwise [false](stdbool_8h.md#a65e9886d74aaee76545e83dd09011727).

## [◆ ](#ga4a0d4891eb6aef6543b1992566729f6c)timespec\_normalize()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) timespec\_normalize | ( | struct [timespec](structtimespec.md) \* | *ts* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[zephyr/sys/timeutil.h](timeutil_8h.md)>`

Normalize a timespec so that the tv\_nsec field is in valid range.

Normalize a timespec by adjusting the tv\_sec and tv\_nsec fields so that the tv\_nsec field is in the range [0, NSEC\_PER\_SEC-1]. This is achieved by converting nanoseconds to seconds and accumulating seconds in either the positive direction when tv\_nsec > [NSEC\_PER\_SEC](group__clock__apis.md#ga0501e82515b2bdf36453c4cc80f5e0cc "number of nanoseconds per second"), or in the negative direction when tv\_nsec < 0.

In pseudocode, normalization can be done as follows:

if ts.tv\_nsec >= NSEC\_PER\_SEC:

sec = ts.tv\_nsec / NSEC\_PER\_SEC

ts.tv\_sec += sec

ts.tv\_nsec -= sec \* NSEC\_PER\_SEC

elif ts.tv\_nsec < 0:

# div\_round\_up(abs(ts->tv\_nsec), NSEC\_PER\_SEC)

sec = (NSEC\_PER\_SEC - ts.tv\_nsec - 1) / NSEC\_PER\_SEC

ts.tv\_sec -= sec;

ts.tv\_nsec += sec \* NSEC\_PER\_SEC;

Note
:   There are two cases where the normalization can result in integer overflow. These can be extrapolated to not simply overflowing the tv\_sec field by one second, but also by any realizable multiple of [NSEC\_PER\_SEC](group__clock__apis.md#ga0501e82515b2bdf36453c4cc80f5e0cc "number of nanoseconds per second").

1. When tv\_nsec is negative and tv\_sec is already most negative.
2. When tv\_nsec is greater-or-equal to [NSEC\_PER\_SEC](group__clock__apis.md#ga0501e82515b2bdf36453c4cc80f5e0cc "number of nanoseconds per second") and tv\_sec is already most positive.

If the operation would result in integer overflow, return value is [false](stdbool_8h.md#a65e9886d74aaee76545e83dd09011727).

Note
:   `ts` must be non-[NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4).

Parameters
:   | ts | the timespec to be normalized |
    | --- | --- |

Returns
:   [true](stdbool_8h.md#a41f9c5fb8b08eb5dc3edce4dcb37fee7) if the operation completes successfully, otherwise [false](stdbool_8h.md#a65e9886d74aaee76545e83dd09011727).

## [◆ ](#gae0511602aea1fecc0b204e28ae91e7d0)timespec\_sub()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) timespec\_sub | ( | struct [timespec](structtimespec.md) \* | *a*, | | --- | --- | --- | --- | |  |  | const struct [timespec](structtimespec.md) \* | *b* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[zephyr/sys/timeutil.h](timeutil_8h.md)>`

Subtract one timespec from another.

This function subtracts the timespec pointed to by `b` from the timespec pointed to by `a` and stores the result in the timespce pointed to by `a`.

If the operation would result in integer overflow, return value is [false](stdbool_8h.md#a65e9886d74aaee76545e83dd09011727).

Note
:   `a` and `b` must be non-[NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4).

Parameters
:   | a | the timespec which is subtracted from |
    | --- | --- |
    | b | the timespec to be subtracted |

Returns
:   [true](stdbool_8h.md#a41f9c5fb8b08eb5dc3edce4dcb37fee7) if the operation is successful, otherwise [false](stdbool_8h.md#a65e9886d74aaee76545e83dd09011727).

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
