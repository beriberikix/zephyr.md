---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/rtc_8h.html
original_path: doxygen/html/rtc_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

rtc.h File Reference

Public real time clock driver API.
[More...](#details)

`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`  
`#include <[zephyr/device.h](device_8h_source.md)>`  
`#include <[errno.h](errno_8h_source.md)>`  
`#include <syscalls/rtc.h>`

[Go to the source code of this file.](rtc_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [rtc\_time](structrtc__time.md) |
|  | Structure for storing date and time values with sub-second precision. [More...](structrtc__time.md#details) |

| Macros | |
| --- | --- |
| RTC Alarm Time Mask | |
| Mask for alarm time fields to enable when setting alarm time | |
| #define | [RTC\_ALARM\_TIME\_MASK\_SECOND](group__rtc__interface.md#gaae487761ea0c904f5715748dab5b03db)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| #define | [RTC\_ALARM\_TIME\_MASK\_MINUTE](group__rtc__interface.md#ga72eb18edb7399ce82fa4693e1301fa94)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| #define | [RTC\_ALARM\_TIME\_MASK\_HOUR](group__rtc__interface.md#ga31c1ba78aebf43d539aed3ed107a8132)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| #define | [RTC\_ALARM\_TIME\_MASK\_MONTHDAY](group__rtc__interface.md#ga08fa103b0055eecd4b887973f06beed7)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
| #define | [RTC\_ALARM\_TIME\_MASK\_MONTH](group__rtc__interface.md#ga2233ee12335b762b728d47afa6c72d02)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
| #define | [RTC\_ALARM\_TIME\_MASK\_YEAR](group__rtc__interface.md#ga2d4baf31c5ba6703ebe64dbd212883ee)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5) |
| #define | [RTC\_ALARM\_TIME\_MASK\_WEEKDAY](group__rtc__interface.md#ga8e3cb85959d06f9b8603142156556ca3)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6) |
| #define | [RTC\_ALARM\_TIME\_MASK\_YEARDAY](group__rtc__interface.md#gad72da3fb8be2c5726bab837fcb97a67e)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7) |
| #define | [RTC\_ALARM\_TIME\_MASK\_NSEC](group__rtc__interface.md#gaf8efe72ee6c332b21827317dde6b9766)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(8) |

| Typedefs | |
| --- | --- |
| typedef void(\* | [rtc\_update\_callback](group__rtc__interface.md#ga99e4869ee85507befc7e7cf129b45b07)) (const struct [device](structdevice.md) \*dev, void \*user\_data) |
|  | RTC update event callback. |
| typedef void(\* | [rtc\_alarm\_callback](group__rtc__interface.md#ga8fc3b6037a95e97b686875beff9a581d)) (const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) id, void \*user\_data) |
|  | RTC alarm triggered callback. |

| Functions | |
| --- | --- |
| int | [rtc\_set\_time](group__rtc__interface.md#ga52982b434c740e86aa5f3e35e9bee4a7) (const struct [device](structdevice.md) \*dev, const struct [rtc\_time](structrtc__time.md) \*timeptr) |
|  | API for setting RTC time. |
| int | [rtc\_get\_time](group__rtc__interface.md#ga208321104a1cdb39173317e6911aea87) (const struct [device](structdevice.md) \*dev, struct [rtc\_time](structrtc__time.md) \*timeptr) |
|  | API for getting RTC time. |
| RTC Interface Alarm | |
| int | [rtc\_alarm\_get\_supported\_fields](group__rtc__interface.md#ga62f8ece98065b9bd892908e2f0b1f9bb) (const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) id, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*mask) |
|  | API for getting the supported fields of the RTC alarm time. |
| int | [rtc\_alarm\_set\_time](group__rtc__interface.md#ga1fc9f0ec9642dfbf742ea541a20bdad5) (const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) id, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mask, const struct [rtc\_time](structrtc__time.md) \*timeptr) |
|  | API for setting RTC alarm time. |
| int | [rtc\_alarm\_get\_time](group__rtc__interface.md#gacba4edcec86ccbea5cd676924840c47a) (const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) id, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*mask, struct [rtc\_time](structrtc__time.md) \*timeptr) |
|  | API for getting RTC alarm time. |
| int | [rtc\_alarm\_is\_pending](group__rtc__interface.md#ga531c379c437a91df44a45e95063700e8) (const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) id) |
|  | API for testing if RTC alarm is pending. |
| int | [rtc\_alarm\_set\_callback](group__rtc__interface.md#ga77ccb9e6bd32e97016e01729d95074b6) (const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) id, [rtc\_alarm\_callback](group__rtc__interface.md#ga8fc3b6037a95e97b686875beff9a581d) callback, void \*user\_data) |
|  | API for setting alarm callback. |
| RTC Interface Update | |
| int | [rtc\_update\_set\_callback](group__rtc__interface.md#gad9a48c4e7a05ee20c0edc96c348c9a45) (const struct [device](structdevice.md) \*dev, [rtc\_update\_callback](group__rtc__interface.md#ga99e4869ee85507befc7e7cf129b45b07) callback, void \*user\_data) |
|  | API for setting update callback. |
| RTC Interface Calibration | |
| int | [rtc\_set\_calibration](group__rtc__interface.md#ga13395c6b38e06bcda23cc0e9c299c445) (const struct [device](structdevice.md) \*dev, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) calibration) |
|  | API for setting RTC calibration. |
| int | [rtc\_get\_calibration](group__rtc__interface.md#gab29bc6bcea5eb71e03d3e6181d4bec2f) (const struct [device](structdevice.md) \*dev, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) \*calibration) |
|  | API for getting RTC calibration. |
| RTC Interface Helpers | |
| static struct [tm](structtm.md) \* | [rtc\_time\_to\_tm](group__rtc__interface.md#gac2bb774a4b512f76c35a0a6723a7c807) (struct [rtc\_time](structrtc__time.md) \*timeptr) |
|  | Convenience function for safely casting a [rtc\_time](structrtc__time.md "rtc_time") pointer to a [tm](structtm.md "tm") pointer. |

## Detailed Description

Public real time clock driver API.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [rtc.h](rtc_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
