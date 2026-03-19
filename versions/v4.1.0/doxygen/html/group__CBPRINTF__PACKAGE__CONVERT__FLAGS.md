---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__CBPRINTF__PACKAGE__CONVERT__FLAGS.html
original_path: doxygen/html/group__CBPRINTF__PACKAGE__CONVERT__FLAGS.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Package convert flags

[Utilities](group__utilities.md) » [Formatted Output APIs](group__cbprintf__apis.md)

| Macros | |
| --- | --- |
| #define | [CBPRINTF\_PACKAGE\_CONVERT\_RO\_STR](#ga9802b700abd5d3cd7cef0e0cbcceb3e7)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
|  | Append read-only strings from source package to destination package. |
| #define | [CBPRINTF\_PACKAGE\_CONVERT\_RW\_STR](#ga983c65ed8afb356a29fa2736f9de7b39)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
|  | Append read-write strings from source package to destination package. |
| #define | [CBPRINTF\_PACKAGE\_CONVERT\_KEEP\_RO\_STR](#ga582ebea3e0d18285840bf277c5382da6)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
|  | Keep read-only location indexes in the package. |
| #define | [CBPRINTF\_PACKAGE\_CONVERT\_PTR\_CHECK](#ga370563f835488868020effcd48b23b90)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
|  | Check format string if p argument was treated as s in the package. |

## Detailed Description

## Macro Definition Documentation

## [◆ ](#ga582ebea3e0d18285840bf277c5382da6)CBPRINTF\_PACKAGE\_CONVERT\_KEEP\_RO\_STR

| #define CBPRINTF\_PACKAGE\_CONVERT\_KEEP\_RO\_STR   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| --- |

`#include <[cbprintf.h](cbprintf_8h.md)>`

Keep read-only location indexes in the package.

If it is set read-only string pointers are kept in the package after copy. If not set they are discarded.

## [◆ ](#ga370563f835488868020effcd48b23b90)CBPRINTF\_PACKAGE\_CONVERT\_PTR\_CHECK

| #define CBPRINTF\_PACKAGE\_CONVERT\_PTR\_CHECK   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
| --- |

`#include <[cbprintf.h](cbprintf_8h.md)>`

Check format string if p argument was treated as s in the package.

Static packaging is done based only on types of arguments used for a format string. Without looking into format specifiers present in the string. Because of that if (unsigned) char pointer is used for p it will be considered as a string location and during conversion an attempt to append a string to a package may be performed. This can lead to misbehavior, in the best case package will be bigger and in the worst case memory fault or security violation may occur.

When this flag is set, format string will be checked to detect cases when string candidate is a pointer used for p and string appending from unexpected location is avoided. Additionally, an log warning is generated to encourage user to cast such argument to void \*. It is recommended because there are configurations where string is not accessible and inspection cannot be done. In those cases there are no means to detect such cases.

## [◆ ](#ga9802b700abd5d3cd7cef0e0cbcceb3e7)CBPRINTF\_PACKAGE\_CONVERT\_RO\_STR

| #define CBPRINTF\_PACKAGE\_CONVERT\_RO\_STR   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

`#include <[cbprintf.h](cbprintf_8h.md)>`

Append read-only strings from source package to destination package.

If package was created with [CBPRINTF\_PACKAGE\_ADD\_RO\_STR\_POS](group__CBPRINTF__PACKAGE__FLAGS.md#ga406facc18bf99afe16d453253d042dbb "CBPRINTF_PACKAGE_ADD_RO_STR_POS") or [CBPRINTF\_PACKAGE\_ADD\_RW\_STR\_POS](group__CBPRINTF__PACKAGE__FLAGS.md#gac6ac59dda3a1a8a4572c1012b4adcbaa "CBPRINTF_PACKAGE_ADD_RW_STR_POS") it contains arrays of indexes where string address can be found in the package. When flag is set, read-only strings are copied into destination package. Address of strings indicated as read-write are also checked and if determined to be read-only they are also copied.

## [◆ ](#ga983c65ed8afb356a29fa2736f9de7b39)CBPRINTF\_PACKAGE\_CONVERT\_RW\_STR

| #define CBPRINTF\_PACKAGE\_CONVERT\_RW\_STR   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| --- |

`#include <[cbprintf.h](cbprintf_8h.md)>`

Append read-write strings from source package to destination package.

If package was created with [CBPRINTF\_PACKAGE\_ADD\_RW\_STR\_POS](group__CBPRINTF__PACKAGE__FLAGS.md#gac6ac59dda3a1a8a4572c1012b4adcbaa "CBPRINTF_PACKAGE_ADD_RW_STR_POS") it contains arrays of indexes where string address can be found in the package. When flag is set, list of read-write strings is examined and if they are not determined to be read-only, they are copied into the destination package. If [CBPRINTF\_PACKAGE\_CONVERT\_RO\_STR](#ga9802b700abd5d3cd7cef0e0cbcceb3e7) is not set, remaining string locations are considered as pointing to read-only location and they are copy to the package if [CBPRINTF\_PACKAGE\_CONVERT\_KEEP\_RO\_STR](#ga582ebea3e0d18285840bf277c5382da6) is set.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
