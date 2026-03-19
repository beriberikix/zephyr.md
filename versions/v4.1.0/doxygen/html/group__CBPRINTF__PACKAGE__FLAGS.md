---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__CBPRINTF__PACKAGE__FLAGS.html
original_path: doxygen/html/group__CBPRINTF__PACKAGE__FLAGS.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Package flags

[Utilities](group__utilities.md) » [Formatted Output APIs](group__cbprintf__apis.md)

| Macros | |
| --- | --- |
| #define | [CBPRINTF\_PACKAGE\_CONST\_CHAR\_RO](#ga6c16ab0b5d98012ffb00942e85d859b3)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
|  | Assume that const char pointer is pointing to read only (constant) strings. |
| #define | [CBPRINTF\_PACKAGE\_ADD\_RO\_STR\_POS](#ga406facc18bf99afe16d453253d042dbb)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
|  | Append locations (within the package) of read-only string pointers. |
| #define | [CBPRINTF\_PACKAGE\_ADD\_RW\_STR\_POS](#gac6ac59dda3a1a8a4572c1012b4adcbaa)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
|  | Append locations (within the package) of read-write string pointers. |
| #define | [CBPRINTF\_PACKAGE\_FIRST\_RO\_STR\_CNT](#ga26b5e05198f6609049c54e439b78cf3c)(n) |
|  | Indicate that `n` first string format arguments are char pointers to read-only location. |
| #define | [CBPRINTF\_PACKAGE\_ADD\_STRING\_IDXS](#ga95b0b7f91303781b8bad610f7cac3fa3)   ([CBPRINTF\_PACKAGE\_ADD\_RO\_STR\_POS](#ga406facc18bf99afe16d453253d042dbb) | [CBPRINTF\_PACKAGE\_CONST\_CHAR\_RO](#ga6c16ab0b5d98012ffb00942e85d859b3)) |
|  | Append indexes of read-only string arguments in the package. |
| #define | [CBPRINTF\_PACKAGE\_ARGS\_ARE\_TAGGED](#gaa8edaf31e7acfb7cb113afa873efa126)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6) |
|  | Indicate the incoming arguments are tagged. |

## Detailed Description

## Macro Definition Documentation

## [◆ ](#ga406facc18bf99afe16d453253d042dbb)CBPRINTF\_PACKAGE\_ADD\_RO\_STR\_POS

| #define CBPRINTF\_PACKAGE\_ADD\_RO\_STR\_POS   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| --- |

`#include <[cbprintf.h](cbprintf_8h.md)>`

Append locations (within the package) of read-only string pointers.

## [◆ ](#gac6ac59dda3a1a8a4572c1012b4adcbaa)CBPRINTF\_PACKAGE\_ADD\_RW\_STR\_POS

| #define CBPRINTF\_PACKAGE\_ADD\_RW\_STR\_POS   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| --- |

`#include <[cbprintf.h](cbprintf_8h.md)>`

Append locations (within the package) of read-write string pointers.

When this flag is not used then read-write strings are appended to the package.

## [◆ ](#ga95b0b7f91303781b8bad610f7cac3fa3)CBPRINTF\_PACKAGE\_ADD\_STRING\_IDXS

| #define CBPRINTF\_PACKAGE\_ADD\_STRING\_IDXS   ([CBPRINTF\_PACKAGE\_ADD\_RO\_STR\_POS](#ga406facc18bf99afe16d453253d042dbb) | [CBPRINTF\_PACKAGE\_CONST\_CHAR\_RO](#ga6c16ab0b5d98012ffb00942e85d859b3)) |
| --- |

`#include <[cbprintf.h](cbprintf_8h.md)>`

Append indexes of read-only string arguments in the package.

When used, package contains locations of read-only string arguments. Package with that information can be converted to fully self-contain package using [cbprintf\_fsc\_package](group__cbprintf__apis.md#ga66fcefde504d543eb9114bc2fff230d2 "cbprintf_fsc_package").

## [◆ ](#gaa8edaf31e7acfb7cb113afa873efa126)CBPRINTF\_PACKAGE\_ARGS\_ARE\_TAGGED

| #define CBPRINTF\_PACKAGE\_ARGS\_ARE\_TAGGED   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6) |
| --- |

`#include <[cbprintf.h](cbprintf_8h.md)>`

Indicate the incoming arguments are tagged.

When set, this indicates that the incoming arguments are tagged, and need to be processed accordingly.

## [◆ ](#ga6c16ab0b5d98012ffb00942e85d859b3)CBPRINTF\_PACKAGE\_CONST\_CHAR\_RO

| #define CBPRINTF\_PACKAGE\_CONST\_CHAR\_RO   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

`#include <[cbprintf.h](cbprintf_8h.md)>`

Assume that const char pointer is pointing to read only (constant) strings.

Flag is valid only for [CBPRINTF\_STATIC\_PACKAGE](group__cbprintf__apis.md#ga1ac0f7d0956fc96a9d850d2fef928285 "CBPRINTF_STATIC_PACKAGE").

## [◆ ](#ga26b5e05198f6609049c54e439b78cf3c)CBPRINTF\_PACKAGE\_FIRST\_RO\_STR\_CNT

| #define CBPRINTF\_PACKAGE\_FIRST\_RO\_STR\_CNT | ( |  | *n* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[cbprintf.h](cbprintf_8h.md)>`

**Value:**

(n << Z\_CBPRINTF\_PACKAGE\_FIRST\_RO\_STR\_OFFSET)

Indicate that `n` first string format arguments are char pointers to read-only location.

Runtime algorithm (address analysis) is skipped for those strings.

Parameters
:   | n | Number of string arguments considered as read-only. |
    | --- | --- |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
