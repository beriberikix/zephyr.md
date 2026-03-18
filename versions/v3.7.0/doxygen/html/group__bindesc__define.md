---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/group__bindesc__define.html
original_path: doxygen/html/group__bindesc__define.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Bindesc Define

[Operating System Services](group__os__services.md)

Binary Descriptor Definition.
[More...](#details)

| Macros | |
| --- | --- |
| #define | [BINDESC\_ID\_APP\_VERSION\_STRING](#ga8521a2005ed6ad5bdbd6ad27a0e26cfc)   0x800 |
|  | The app version string such as "1.2.3". |
| #define | [BINDESC\_ID\_APP\_VERSION\_MAJOR](#ga94f405178c0139626718b143e6f22734)   0x801 |
|  | The app version major such as 1. |
| #define | [BINDESC\_ID\_APP\_VERSION\_MINOR](#gaab4f7cdf7ea4f766be1fa7779eef1bdb)   0x802 |
|  | The app version minor such as 2. |
| #define | [BINDESC\_ID\_APP\_VERSION\_PATCHLEVEL](#ga90eb8f252c3484103eee18dbb1aabdc6)   0x803 |
|  | The app version patchlevel such as 3. |
| #define | [BINDESC\_ID\_APP\_VERSION\_NUMBER](#ga66b25585ff23de9906814ddecb4ac4ea)   0x804 |
|  | The app version number such as 0x10203. |
| #define | [BINDESC\_ID\_KERNEL\_VERSION\_STRING](#ga35fdf13eb11dd4eeca1bf2dc57782777)   0x900 |
|  | The kernel version string such as "3.4.0". |
| #define | [BINDESC\_ID\_KERNEL\_VERSION\_MAJOR](#gabd5e9193c56495faa19f299371a02fd0)   0x901 |
|  | The kernel version major such as 3. |
| #define | [BINDESC\_ID\_KERNEL\_VERSION\_MINOR](#ga9ab56a8cef01c648a313bb4e5b7983e4)   0x902 |
|  | The kernel version minor such as 4. |
| #define | [BINDESC\_ID\_KERNEL\_VERSION\_PATCHLEVEL](#ga2ef91c2cd49d61c9f3e95ac5292e6983)   0x903 |
|  | The kernel version patchlevel such as 0. |
| #define | [BINDESC\_ID\_KERNEL\_VERSION\_NUMBER](#gad2c5489eaa1a191a49ffd409462b1af4)   0x904 |
|  | The kernel version number such as 0x30400. |
| #define | [BINDESC\_ID\_BUILD\_TIME\_YEAR](#ga21fbd3ff6a408febdaf0f1a1f19f0fa3)   0xa00 |
|  | The year the image was compiled in. |
| #define | [BINDESC\_ID\_BUILD\_TIME\_MONTH](#ga8e68f8226d05415c040f6fb74bada6fc)   0xa01 |
|  | The month of the year the image was compiled in. |
| #define | [BINDESC\_ID\_BUILD\_TIME\_DAY](#ga5710e218f4f10e5049d039b17a376d0b)   0xa02 |
|  | The day of the month the image was compiled in. |
| #define | [BINDESC\_ID\_BUILD\_TIME\_HOUR](#gaeed1651e0d025ff74092a88b6d57e408)   0xa03 |
|  | The hour of the day the image was compiled in. |
| #define | [BINDESC\_ID\_BUILD\_TIME\_MINUTE](#ga67f679968aeea5517e02da6e5e67d73e)   0xa04 |
|  | The minute the image was compiled in. |
| #define | [BINDESC\_ID\_BUILD\_TIME\_SECOND](#gacdff70f58c8098e23611327c1264a7dd)   0xa05 |
|  | The second the image was compiled in. |
| #define | [BINDESC\_ID\_BUILD\_TIME\_UNIX](#gab0eefe2d83294d6ebe4ca6299f05d785)   0xa06 |
|  | The UNIX time (seconds since midnight of 1970/01/01) the image was compiled in. |
| #define | [BINDESC\_ID\_BUILD\_DATE\_TIME\_STRING](#gad8803e832ed0a42fd7033e277f8d8362)   0xa07 |
|  | The date and time of compilation such as "2023/02/05 00:07:04". |
| #define | [BINDESC\_ID\_BUILD\_DATE\_STRING](#ga8bf6d98fb9495f2cca6b0403dffd0752)   0xa08 |
|  | The date of compilation such as "2023/02/05". |
| #define | [BINDESC\_ID\_BUILD\_TIME\_STRING](#gac4f75b876a81072e14bb39e3fb1c1f8a)   0xa09 |
|  | The time of compilation such as "00:07:04". |
| #define | [BINDESC\_ID\_HOST\_NAME](#ga4cc66094d33709d9738b49e181a6eec3)   0xb00 |
|  | The name of the host that compiled the image. |
| #define | [BINDESC\_ID\_C\_COMPILER\_NAME](#ga51b3fdd47d3dd94101134523c4dca144)   0xb01 |
|  | The C compiler name. |
| #define | [BINDESC\_ID\_C\_COMPILER\_VERSION](#gac4c6c9576b31cb2c26b085537648552b)   0xb02 |
|  | The C compiler version. |
| #define | [BINDESC\_ID\_CXX\_COMPILER\_NAME](#ga6f198590afdb2524b587e0194598b8eb)   0xb03 |
|  | The C++ compiler name. |
| #define | [BINDESC\_ID\_CXX\_COMPILER\_VERSION](#ga7ec0430daae1f99bdeeae6a636a263d8)   0xb04 |
|  | The C++ compiler version. |
| #define | [BINDESC\_TAG\_DESCRIPTORS\_END](#gac12b3cbf6d132fb54bbf702fd581373f)   BINDESC\_TAG(DESCRIPTORS\_END, 0x0fff) |

## Detailed Description

Binary Descriptor Definition.

## Macro Definition Documentation

## [◆ ](#ga94f405178c0139626718b143e6f22734)BINDESC\_ID\_APP\_VERSION\_MAJOR

| #define BINDESC\_ID\_APP\_VERSION\_MAJOR   0x801 |
| --- |

`#include <[bindesc.h](bindesc_8h.md)>`

The app version major such as 1.

## [◆ ](#gaab4f7cdf7ea4f766be1fa7779eef1bdb)BINDESC\_ID\_APP\_VERSION\_MINOR

| #define BINDESC\_ID\_APP\_VERSION\_MINOR   0x802 |
| --- |

`#include <[bindesc.h](bindesc_8h.md)>`

The app version minor such as 2.

## [◆ ](#ga66b25585ff23de9906814ddecb4ac4ea)BINDESC\_ID\_APP\_VERSION\_NUMBER

| #define BINDESC\_ID\_APP\_VERSION\_NUMBER   0x804 |
| --- |

`#include <[bindesc.h](bindesc_8h.md)>`

The app version number such as 0x10203.

## [◆ ](#ga90eb8f252c3484103eee18dbb1aabdc6)BINDESC\_ID\_APP\_VERSION\_PATCHLEVEL

| #define BINDESC\_ID\_APP\_VERSION\_PATCHLEVEL   0x803 |
| --- |

`#include <[bindesc.h](bindesc_8h.md)>`

The app version patchlevel such as 3.

## [◆ ](#ga8521a2005ed6ad5bdbd6ad27a0e26cfc)BINDESC\_ID\_APP\_VERSION\_STRING

| #define BINDESC\_ID\_APP\_VERSION\_STRING   0x800 |
| --- |

`#include <[bindesc.h](bindesc_8h.md)>`

The app version string such as "1.2.3".

## [◆ ](#ga8bf6d98fb9495f2cca6b0403dffd0752)BINDESC\_ID\_BUILD\_DATE\_STRING

| #define BINDESC\_ID\_BUILD\_DATE\_STRING   0xa08 |
| --- |

`#include <[bindesc.h](bindesc_8h.md)>`

The date of compilation such as "2023/02/05".

## [◆ ](#gad8803e832ed0a42fd7033e277f8d8362)BINDESC\_ID\_BUILD\_DATE\_TIME\_STRING

| #define BINDESC\_ID\_BUILD\_DATE\_TIME\_STRING   0xa07 |
| --- |

`#include <[bindesc.h](bindesc_8h.md)>`

The date and time of compilation such as "2023/02/05 00:07:04".

## [◆ ](#ga5710e218f4f10e5049d039b17a376d0b)BINDESC\_ID\_BUILD\_TIME\_DAY

| #define BINDESC\_ID\_BUILD\_TIME\_DAY   0xa02 |
| --- |

`#include <[bindesc.h](bindesc_8h.md)>`

The day of the month the image was compiled in.

## [◆ ](#gaeed1651e0d025ff74092a88b6d57e408)BINDESC\_ID\_BUILD\_TIME\_HOUR

| #define BINDESC\_ID\_BUILD\_TIME\_HOUR   0xa03 |
| --- |

`#include <[bindesc.h](bindesc_8h.md)>`

The hour of the day the image was compiled in.

## [◆ ](#ga67f679968aeea5517e02da6e5e67d73e)BINDESC\_ID\_BUILD\_TIME\_MINUTE

| #define BINDESC\_ID\_BUILD\_TIME\_MINUTE   0xa04 |
| --- |

`#include <[bindesc.h](bindesc_8h.md)>`

The minute the image was compiled in.

## [◆ ](#ga8e68f8226d05415c040f6fb74bada6fc)BINDESC\_ID\_BUILD\_TIME\_MONTH

| #define BINDESC\_ID\_BUILD\_TIME\_MONTH   0xa01 |
| --- |

`#include <[bindesc.h](bindesc_8h.md)>`

The month of the year the image was compiled in.

## [◆ ](#gacdff70f58c8098e23611327c1264a7dd)BINDESC\_ID\_BUILD\_TIME\_SECOND

| #define BINDESC\_ID\_BUILD\_TIME\_SECOND   0xa05 |
| --- |

`#include <[bindesc.h](bindesc_8h.md)>`

The second the image was compiled in.

## [◆ ](#gac4f75b876a81072e14bb39e3fb1c1f8a)BINDESC\_ID\_BUILD\_TIME\_STRING

| #define BINDESC\_ID\_BUILD\_TIME\_STRING   0xa09 |
| --- |

`#include <[bindesc.h](bindesc_8h.md)>`

The time of compilation such as "00:07:04".

## [◆ ](#gab0eefe2d83294d6ebe4ca6299f05d785)BINDESC\_ID\_BUILD\_TIME\_UNIX

| #define BINDESC\_ID\_BUILD\_TIME\_UNIX   0xa06 |
| --- |

`#include <[bindesc.h](bindesc_8h.md)>`

The UNIX time (seconds since midnight of 1970/01/01) the image was compiled in.

## [◆ ](#ga21fbd3ff6a408febdaf0f1a1f19f0fa3)BINDESC\_ID\_BUILD\_TIME\_YEAR

| #define BINDESC\_ID\_BUILD\_TIME\_YEAR   0xa00 |
| --- |

`#include <[bindesc.h](bindesc_8h.md)>`

The year the image was compiled in.

## [◆ ](#ga51b3fdd47d3dd94101134523c4dca144)BINDESC\_ID\_C\_COMPILER\_NAME

| #define BINDESC\_ID\_C\_COMPILER\_NAME   0xb01 |
| --- |

`#include <[bindesc.h](bindesc_8h.md)>`

The C compiler name.

## [◆ ](#gac4c6c9576b31cb2c26b085537648552b)BINDESC\_ID\_C\_COMPILER\_VERSION

| #define BINDESC\_ID\_C\_COMPILER\_VERSION   0xb02 |
| --- |

`#include <[bindesc.h](bindesc_8h.md)>`

The C compiler version.

## [◆ ](#ga6f198590afdb2524b587e0194598b8eb)BINDESC\_ID\_CXX\_COMPILER\_NAME

| #define BINDESC\_ID\_CXX\_COMPILER\_NAME   0xb03 |
| --- |

`#include <[bindesc.h](bindesc_8h.md)>`

The C++ compiler name.

## [◆ ](#ga7ec0430daae1f99bdeeae6a636a263d8)BINDESC\_ID\_CXX\_COMPILER\_VERSION

| #define BINDESC\_ID\_CXX\_COMPILER\_VERSION   0xb04 |
| --- |

`#include <[bindesc.h](bindesc_8h.md)>`

The C++ compiler version.

## [◆ ](#ga4cc66094d33709d9738b49e181a6eec3)BINDESC\_ID\_HOST\_NAME

| #define BINDESC\_ID\_HOST\_NAME   0xb00 |
| --- |

`#include <[bindesc.h](bindesc_8h.md)>`

The name of the host that compiled the image.

## [◆ ](#gabd5e9193c56495faa19f299371a02fd0)BINDESC\_ID\_KERNEL\_VERSION\_MAJOR

| #define BINDESC\_ID\_KERNEL\_VERSION\_MAJOR   0x901 |
| --- |

`#include <[bindesc.h](bindesc_8h.md)>`

The kernel version major such as 3.

## [◆ ](#ga9ab56a8cef01c648a313bb4e5b7983e4)BINDESC\_ID\_KERNEL\_VERSION\_MINOR

| #define BINDESC\_ID\_KERNEL\_VERSION\_MINOR   0x902 |
| --- |

`#include <[bindesc.h](bindesc_8h.md)>`

The kernel version minor such as 4.

## [◆ ](#gad2c5489eaa1a191a49ffd409462b1af4)BINDESC\_ID\_KERNEL\_VERSION\_NUMBER

| #define BINDESC\_ID\_KERNEL\_VERSION\_NUMBER   0x904 |
| --- |

`#include <[bindesc.h](bindesc_8h.md)>`

The kernel version number such as 0x30400.

## [◆ ](#ga2ef91c2cd49d61c9f3e95ac5292e6983)BINDESC\_ID\_KERNEL\_VERSION\_PATCHLEVEL

| #define BINDESC\_ID\_KERNEL\_VERSION\_PATCHLEVEL   0x903 |
| --- |

`#include <[bindesc.h](bindesc_8h.md)>`

The kernel version patchlevel such as 0.

## [◆ ](#ga35fdf13eb11dd4eeca1bf2dc57782777)BINDESC\_ID\_KERNEL\_VERSION\_STRING

| #define BINDESC\_ID\_KERNEL\_VERSION\_STRING   0x900 |
| --- |

`#include <[bindesc.h](bindesc_8h.md)>`

The kernel version string such as "3.4.0".

## [◆ ](#gac12b3cbf6d132fb54bbf702fd581373f)BINDESC\_TAG\_DESCRIPTORS\_END

| #define BINDESC\_TAG\_DESCRIPTORS\_END   BINDESC\_TAG(DESCRIPTORS\_END, 0x0fff) |
| --- |

`#include <[bindesc.h](bindesc_8h.md)>`

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
