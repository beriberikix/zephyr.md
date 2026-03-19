---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__rtc__interface.html
original_path: doxygen/html/group__rtc__interface.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

RTC Interface

[Device Driver APIs](group__io__interfaces.md)

RTC Interface.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [rtc\_time](structrtc__time.md) |
|  | Structure for storing date and time values with sub-second precision. [More...](structrtc__time.md#details) |

| Typedefs | |
| --- | --- |
| typedef void(\* | [rtc\_update\_callback](#ga99e4869ee85507befc7e7cf129b45b07)) (const struct [device](structdevice.md) \*dev, void \*user\_data) |
|  | RTC update event callback. |
| typedef void(\* | [rtc\_alarm\_callback](#ga8fc3b6037a95e97b686875beff9a581d)) (const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) id, void \*user\_data) |
|  | RTC alarm triggered callback. |

| Functions | |
| --- | --- |
| int | [rtc\_set\_time](#ga52982b434c740e86aa5f3e35e9bee4a7) (const struct [device](structdevice.md) \*dev, const struct [rtc\_time](structrtc__time.md) \*timeptr) |
|  | API for setting RTC time. |
| int | [rtc\_get\_time](#ga208321104a1cdb39173317e6911aea87) (const struct [device](structdevice.md) \*dev, struct [rtc\_time](structrtc__time.md) \*timeptr) |
|  | API for getting RTC time. |

| RTC Interface Alarm | |
| --- | --- |
| int | [rtc\_alarm\_get\_supported\_fields](#ga62f8ece98065b9bd892908e2f0b1f9bb) (const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) id, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*mask) |
|  | API for getting the supported fields of the RTC alarm time. |
| int | [rtc\_alarm\_set\_time](#ga1fc9f0ec9642dfbf742ea541a20bdad5) (const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) id, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mask, const struct [rtc\_time](structrtc__time.md) \*timeptr) |
|  | API for setting RTC alarm time. |
| int | [rtc\_alarm\_get\_time](#gacba4edcec86ccbea5cd676924840c47a) (const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) id, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*mask, struct [rtc\_time](structrtc__time.md) \*timeptr) |
|  | API for getting RTC alarm time. |
| int | [rtc\_alarm\_is\_pending](#ga531c379c437a91df44a45e95063700e8) (const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) id) |
|  | API for testing if RTC alarm is pending. |
| int | [rtc\_alarm\_set\_callback](#ga77ccb9e6bd32e97016e01729d95074b6) (const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) id, [rtc\_alarm\_callback](#ga8fc3b6037a95e97b686875beff9a581d) callback, void \*user\_data) |
|  | API for setting alarm callback. |

| RTC Interface Update | |
| --- | --- |
| int | [rtc\_update\_set\_callback](#gad9a48c4e7a05ee20c0edc96c348c9a45) (const struct [device](structdevice.md) \*dev, [rtc\_update\_callback](#ga99e4869ee85507befc7e7cf129b45b07) callback, void \*user\_data) |
|  | API for setting update callback. |

| RTC Interface Calibration | |
| --- | --- |
| int | [rtc\_set\_calibration](#ga13395c6b38e06bcda23cc0e9c299c445) (const struct [device](structdevice.md) \*dev, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) calibration) |
|  | API for setting RTC calibration. |
| int | [rtc\_get\_calibration](#gab29bc6bcea5eb71e03d3e6181d4bec2f) (const struct [device](structdevice.md) \*dev, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) \*calibration) |
|  | API for getting RTC calibration. |

| RTC Interface Helpers | |
| --- | --- |
| static struct [tm](structtm.md) \* | [rtc\_time\_to\_tm](#gac2bb774a4b512f76c35a0a6723a7c807) (struct [rtc\_time](structrtc__time.md) \*timeptr) |
|  | Convenience function for safely casting a [rtc\_time](structrtc__time.md "rtc_time") pointer to a [tm](structtm.md "tm") pointer. |
| static [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) | [rtc\_calibration\_from\_frequency](#gacca437e504026d800aa481b870291fda) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) frequency) |
|  | Determine required calibration to 1 Hertz from frequency. |

| RTC Alarm Time Mask | |
| --- | --- |
| Mask for alarm time fields to enable when setting alarm time | |
| #define | [RTC\_ALARM\_TIME\_MASK\_SECOND](#gaae487761ea0c904f5715748dab5b03db)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| #define | [RTC\_ALARM\_TIME\_MASK\_MINUTE](#ga72eb18edb7399ce82fa4693e1301fa94)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| #define | [RTC\_ALARM\_TIME\_MASK\_HOUR](#ga31c1ba78aebf43d539aed3ed107a8132)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| #define | [RTC\_ALARM\_TIME\_MASK\_MONTHDAY](#ga08fa103b0055eecd4b887973f06beed7)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
| #define | [RTC\_ALARM\_TIME\_MASK\_MONTH](#ga2233ee12335b762b728d47afa6c72d02)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
| #define | [RTC\_ALARM\_TIME\_MASK\_YEAR](#ga2d4baf31c5ba6703ebe64dbd212883ee)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5) |
| #define | [RTC\_ALARM\_TIME\_MASK\_WEEKDAY](#ga8e3cb85959d06f9b8603142156556ca3)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6) |
| #define | [RTC\_ALARM\_TIME\_MASK\_YEARDAY](#gad72da3fb8be2c5726bab837fcb97a67e)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7) |
| #define | [RTC\_ALARM\_TIME\_MASK\_NSEC](#gaf8efe72ee6c332b21827317dde6b9766)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(8) |

## Detailed Description

RTC Interface.

Since
:   3.4

Version
:   0.1.0

## Macro Definition Documentation

## [◆ ](#ga31c1ba78aebf43d539aed3ed107a8132)RTC\_ALARM\_TIME\_MASK\_HOUR

| #define RTC\_ALARM\_TIME\_MASK\_HOUR   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| --- |

`#include <[rtc.h](rtc_8h.md)>`

## [◆ ](#ga72eb18edb7399ce82fa4693e1301fa94)RTC\_ALARM\_TIME\_MASK\_MINUTE

| #define RTC\_ALARM\_TIME\_MASK\_MINUTE   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| --- |

`#include <[rtc.h](rtc_8h.md)>`

## [◆ ](#ga2233ee12335b762b728d47afa6c72d02)RTC\_ALARM\_TIME\_MASK\_MONTH

| #define RTC\_ALARM\_TIME\_MASK\_MONTH   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
| --- |

`#include <[rtc.h](rtc_8h.md)>`

## [◆ ](#ga08fa103b0055eecd4b887973f06beed7)RTC\_ALARM\_TIME\_MASK\_MONTHDAY

| #define RTC\_ALARM\_TIME\_MASK\_MONTHDAY   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
| --- |

`#include <[rtc.h](rtc_8h.md)>`

## [◆ ](#gaf8efe72ee6c332b21827317dde6b9766)RTC\_ALARM\_TIME\_MASK\_NSEC

| #define RTC\_ALARM\_TIME\_MASK\_NSEC   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(8) |
| --- |

`#include <[rtc.h](rtc_8h.md)>`

## [◆ ](#gaae487761ea0c904f5715748dab5b03db)RTC\_ALARM\_TIME\_MASK\_SECOND

| #define RTC\_ALARM\_TIME\_MASK\_SECOND   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

`#include <[rtc.h](rtc_8h.md)>`

## [◆ ](#ga8e3cb85959d06f9b8603142156556ca3)RTC\_ALARM\_TIME\_MASK\_WEEKDAY

| #define RTC\_ALARM\_TIME\_MASK\_WEEKDAY   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6) |
| --- |

`#include <[rtc.h](rtc_8h.md)>`

## [◆ ](#ga2d4baf31c5ba6703ebe64dbd212883ee)RTC\_ALARM\_TIME\_MASK\_YEAR

| #define RTC\_ALARM\_TIME\_MASK\_YEAR   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5) |
| --- |

`#include <[rtc.h](rtc_8h.md)>`

## [◆ ](#gad72da3fb8be2c5726bab837fcb97a67e)RTC\_ALARM\_TIME\_MASK\_YEARDAY

| #define RTC\_ALARM\_TIME\_MASK\_YEARDAY   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7) |
| --- |

`#include <[rtc.h](rtc_8h.md)>`

## Typedef Documentation

## [◆ ](#ga8fc3b6037a95e97b686875beff9a581d)rtc\_alarm\_callback

| typedef void(\* rtc\_alarm\_callback) (const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) id, void \*user\_data) |
| --- |

`#include <[rtc.h](rtc_8h.md)>`

RTC alarm triggered callback.

Parameters
:   | dev | Device instance invoking the handler |
    | --- | --- |
    | id | Alarm id |
    | user\_data | Optional user data passed with the alarm configuration |

## [◆ ](#ga99e4869ee85507befc7e7cf129b45b07)rtc\_update\_callback

| typedef void(\* rtc\_update\_callback) (const struct [device](structdevice.md) \*dev, void \*user\_data) |
| --- |

`#include <[rtc.h](rtc_8h.md)>`

RTC update event callback.

Parameters
:   | dev | Device instance invoking the handler |
    | --- | --- |
    | user\_data | Optional user data provided when update irq callback is set |

## Function Documentation

## [◆ ](#ga62f8ece98065b9bd892908e2f0b1f9bb)rtc\_alarm\_get\_supported\_fields()

| int rtc\_alarm\_get\_supported\_fields | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *id*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \* | *mask* ) |

`#include <[rtc.h](rtc_8h.md)>`

API for getting the supported fields of the RTC alarm time.

Parameters
:   | dev | Device instance |
    | --- | --- |
    | id | Id of the alarm |
    | mask | Mask of fields in the alarm time which are supported |

Note
:   Bits in the mask param are defined here [RTC\_ALARM\_TIME\_MASK](#RTC_ALARM_TIME_MASK).

Returns
:   0 if successful
:   -EINVAL if id is out of range or time is invalid
:   -ENOTSUP if API is not supported by hardware
:   -errno code if failure

## [◆ ](#gacba4edcec86ccbea5cd676924840c47a)rtc\_alarm\_get\_time()

| int rtc\_alarm\_get\_time | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *id*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \* | *mask*, |
|  |  | struct [rtc\_time](structrtc__time.md) \* | *timeptr* ) |

`#include <[rtc.h](rtc_8h.md)>`

API for getting RTC alarm time.

Parameters
:   | dev | Device instance |
    | --- | --- |
    | id | Id of the alarm |
    | mask | Destination for mask of fields which are enabled in the alarm time |
    | timeptr | Destination for the alarm time |

Note
:   Bits in the mask param are defined here [RTC\_ALARM\_TIME\_MASK](#RTC_ALARM_TIME_MASK)

Returns
:   0 if successful
:   -EINVAL if id is out of range
:   -ENOTSUP if API is not supported by hardware
:   -errno code if failure

## [◆ ](#ga531c379c437a91df44a45e95063700e8)rtc\_alarm\_is\_pending()

| int rtc\_alarm\_is\_pending | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *id* ) |

`#include <[rtc.h](rtc_8h.md)>`

API for testing if RTC alarm is pending.

Test whether or not the alarm with id is pending. If the alarm is pending, the pending status is cleared.

Parameters
:   | dev | Device instance |
    | --- | --- |
    | id | Id of the alarm to test |

Returns
:   1 if alarm was pending
:   0 if alarm was not pending
:   -EINVAL if id is out of range
:   -ENOTSUP if API is not supported by hardware
:   -errno code if failure

## [◆ ](#ga77ccb9e6bd32e97016e01729d95074b6)rtc\_alarm\_set\_callback()

| int rtc\_alarm\_set\_callback | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *id*, |
|  |  | [rtc\_alarm\_callback](#ga8fc3b6037a95e97b686875beff9a581d) | *callback*, |
|  |  | void \* | *user\_data* ) |

`#include <[rtc.h](rtc_8h.md)>`

API for setting alarm callback.

Setting the alarm callback for an alarm, will enable the alarm callback. When the callback for an alarm is enabled, the alarm triggered event will invoke the callback, after which the alarm pending status will be cleared automatically. The alarm will remain enabled until manually disabled using [rtc\_alarm\_set\_time()](#ga1fc9f0ec9642dfbf742ea541a20bdad5).

To disable the alarm callback for an alarm, the `callback` and `user_data` parameters must be set to NULL. When the alarm callback for an alarm is disabled, the alarm triggered event will set the alarm status to "pending". To check if the alarm status is "pending", use [rtc\_alarm\_is\_pending()](#ga531c379c437a91df44a45e95063700e8).

Parameters
:   | dev | Device instance |
    | --- | --- |
    | id | Id of the alarm for which the callback shall be set |
    | callback | Callback called when alarm occurs |
    | user\_data | Optional user data passed to callback |

Returns
:   0 if successful
:   -EINVAL if id is out of range
:   -ENOTSUP if API is not supported by hardware
:   -errno code if failure

## [◆ ](#ga1fc9f0ec9642dfbf742ea541a20bdad5)rtc\_alarm\_set\_time()

| int rtc\_alarm\_set\_time | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *id*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *mask*, |
|  |  | const struct [rtc\_time](structrtc__time.md) \* | *timeptr* ) |

`#include <[rtc.h](rtc_8h.md)>`

API for setting RTC alarm time.

To enable an RTC alarm, one or more fields of the RTC alarm time must be enabled. The mask designates which fields of the RTC alarm time to enable. If the mask parameter is 0, the alarm will be disabled. The RTC alarm will trigger when all enabled fields of the alarm time match the RTC time.

Parameters
:   | dev | Device instance |
    | --- | --- |
    | id | Id of the alarm |
    | mask | Mask of fields in the alarm time to enable |
    | timeptr | The alarm time to set |

Note
:   The timeptr param may be NULL if the mask param is 0
:   Only the enabled fields in the timeptr param need to be configured
:   Bits in the mask param are defined here [RTC\_ALARM\_TIME\_MASK](#RTC_ALARM_TIME_MASK)

Returns
:   0 if successful
:   -EINVAL if id is out of range or time is invalid
:   -ENOTSUP if API is not supported by hardware
:   -errno code if failure

## [◆ ](#gacca437e504026d800aa481b870291fda)rtc\_calibration\_from\_frequency()

| | [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) rtc\_calibration\_from\_frequency | ( | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *frequency* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[rtc.h](rtc_8h.md)>`

Determine required calibration to 1 Hertz from frequency.

Parameters
:   | frequency | Frequency of the RTC in nano Hertz |
    | --- | --- |

Returns
:   The required calibration in parts per billion

## [◆ ](#gab29bc6bcea5eb71e03d3e6181d4bec2f)rtc\_get\_calibration()

| int rtc\_get\_calibration | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) \* | *calibration* ) |

`#include <[rtc.h](rtc_8h.md)>`

API for getting RTC calibration.

Parameters
:   | dev | Device instance |
    | --- | --- |
    | calibration | Destination for calibration in parts per billion |

Returns
:   0 if successful
:   -ENOTSUP if API is not supported by hardware
:   -errno code if failure

## [◆ ](#ga208321104a1cdb39173317e6911aea87)rtc\_get\_time()

| int rtc\_get\_time | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | struct [rtc\_time](structrtc__time.md) \* | *timeptr* ) |

`#include <[rtc.h](rtc_8h.md)>`

API for getting RTC time.

Parameters
:   | dev | Device instance |
    | --- | --- |
    | timeptr | Destination for the time |

Returns
:   0 if successful
:   -ENODATA if RTC time has not been set
:   -errno code if failure

## [◆ ](#ga13395c6b38e06bcda23cc0e9c299c445)rtc\_set\_calibration()

| int rtc\_set\_calibration | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) | *calibration* ) |

`#include <[rtc.h](rtc_8h.md)>`

API for setting RTC calibration.

Calibration is applied to the RTC clock input. A positive calibration value will increase the frequency of the RTC clock, a negative value will decrease the frequency of the RTC clock.

See also
:   [rtc\_calibration\_from\_frequency()](#gacca437e504026d800aa481b870291fda)

Parameters
:   | dev | Device instance |
    | --- | --- |
    | calibration | Calibration to set in parts per billion |

Returns
:   0 if successful
:   -EINVAL if calibration is out of range
:   -ENOTSUP if API is not supported by hardware
:   -errno code if failure

## [◆ ](#ga52982b434c740e86aa5f3e35e9bee4a7)rtc\_set\_time()

| int rtc\_set\_time | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | const struct [rtc\_time](structrtc__time.md) \* | *timeptr* ) |

`#include <[rtc.h](rtc_8h.md)>`

API for setting RTC time.

Parameters
:   | dev | Device instance |
    | --- | --- |
    | timeptr | The time to set |

Returns
:   0 if successful
:   -EINVAL if RTC time is invalid or exceeds hardware capabilities
:   -errno code if failure

## [◆ ](#gac2bb774a4b512f76c35a0a6723a7c807)rtc\_time\_to\_tm()

| | struct [tm](structtm.md) \* rtc\_time\_to\_tm | ( | struct [rtc\_time](structrtc__time.md) \* | *timeptr* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[rtc.h](rtc_8h.md)>`

Convenience function for safely casting a [rtc\_time](structrtc__time.md "rtc_time") pointer to a [tm](structtm.md "tm") pointer.

## [◆ ](#gad9a48c4e7a05ee20c0edc96c348c9a45)rtc\_update\_set\_callback()

| int rtc\_update\_set\_callback | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [rtc\_update\_callback](#ga99e4869ee85507befc7e7cf129b45b07) | *callback*, |
|  |  | void \* | *user\_data* ) |

`#include <[rtc.h](rtc_8h.md)>`

API for setting update callback.

Setting the update callback will enable the update callback. The update callback will be invoked every time the RTC clock is updated by 1 second. It can be used to synchronize the RTC clock with other clock sources.

To disable the update callback for the RTC clock, the `callback` and `user_data` parameters must be set to NULL.

Parameters
:   | dev | Device instance |
    | --- | --- |
    | callback | Callback called when update occurs |
    | user\_data | Optional user data passed to callback |

Returns
:   0 if successful
:   -ENOTSUP if API is not supported by hardware
:   -errno code if failure

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
