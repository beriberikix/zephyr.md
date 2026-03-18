---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structrtc__time.html
original_path: doxygen/html/structrtc__time.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

rtc\_time Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [RTC Interface](group__rtc__interface.md)

Structure for storing date and time values with sub-second precision.
[More...](#details)

`#include <[rtc.h](rtc_8h_source.md)>`

| Data Fields | |
| --- | --- |
| int | [tm\_sec](#aed2640702991b684601d1771847bb50f) |
|  | Seconds [0, 59]. |
| int | [tm\_min](#a927b7e67b64708f671c1fe9409e9d794) |
|  | Minutes [0, 59]. |
| int | [tm\_hour](#aee14d277ac0339f587f4b946be53dc09) |
|  | Hours [0, 23]. |
| int | [tm\_mday](#af56ccbce4cca252d2ab0d7516cc5e2db) |
|  | Day of the month [1, 31]. |
| int | [tm\_mon](#aa17515d6d722d1e6e4427a129c8de9f8) |
|  | Month [0, 11]. |
| int | [tm\_year](#ad3fcf9be156258688742a511e8b36277) |
|  | Year - 1900. |
| int | [tm\_wday](#ac44442e37e069314e2b6bae0f0747f49) |
|  | Day of the week [0, 6] (Sunday = 0) (Unknown = -1). |
| int | [tm\_yday](#a5a7837a78fb662831fa3186377d63375) |
|  | Day of the year [0, 365] (Unknown = -1). |
| int | [tm\_isdst](#aa26da32caecabf386e9a204937d9f786) |
|  | Daylight saving time flag [-1] (Unknown = -1). |
| int | [tm\_nsec](#a876a66e76c713ead7c5eb2cc65d141ed) |
|  | Nanoseconds [0, 999999999] (Unknown = 0). |

## Detailed Description

Structure for storing date and time values with sub-second precision.

The structure is 1-1 mapped to the struct tm for the members `tm_sec` to `tm_isdst` making it compatible with the standard time library.

Note
:   Use [rtc\_time\_to\_tm()](group__rtc__interface.md#gac2bb774a4b512f76c35a0a6723a7c807 "rtc_time_to_tm()") to safely cast from a [rtc\_time](structrtc__time.md "rtc_time") pointer to a [tm](structtm.md "tm") pointer.

## Field Documentation

## [◆ ](#aee14d277ac0339f587f4b946be53dc09)tm\_hour

| int rtc\_time::tm\_hour |
| --- |

Hours [0, 23].

## [◆ ](#aa26da32caecabf386e9a204937d9f786)tm\_isdst

| int rtc\_time::tm\_isdst |
| --- |

Daylight saving time flag [-1] (Unknown = -1).

## [◆ ](#af56ccbce4cca252d2ab0d7516cc5e2db)tm\_mday

| int rtc\_time::tm\_mday |
| --- |

Day of the month [1, 31].

## [◆ ](#a927b7e67b64708f671c1fe9409e9d794)tm\_min

| int rtc\_time::tm\_min |
| --- |

Minutes [0, 59].

## [◆ ](#aa17515d6d722d1e6e4427a129c8de9f8)tm\_mon

| int rtc\_time::tm\_mon |
| --- |

Month [0, 11].

## [◆ ](#a876a66e76c713ead7c5eb2cc65d141ed)tm\_nsec

| int rtc\_time::tm\_nsec |
| --- |

Nanoseconds [0, 999999999] (Unknown = 0).

## [◆ ](#aed2640702991b684601d1771847bb50f)tm\_sec

| int rtc\_time::tm\_sec |
| --- |

Seconds [0, 59].

## [◆ ](#ac44442e37e069314e2b6bae0f0747f49)tm\_wday

| int rtc\_time::tm\_wday |
| --- |

Day of the week [0, 6] (Sunday = 0) (Unknown = -1).

## [◆ ](#a5a7837a78fb662831fa3186377d63375)tm\_yday

| int rtc\_time::tm\_yday |
| --- |

Day of the year [0, 365] (Unknown = -1).

## [◆ ](#ad3fcf9be156258688742a511e8b36277)tm\_year

| int rtc\_time::tm\_year |
| --- |

Year - 1900.

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[rtc.h](rtc_8h_source.md)

- [rtc\_time](structrtc__time.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
