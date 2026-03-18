---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/esp-pinctrl-common_8h.html
original_path: doxygen/html/esp-pinctrl-common_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

esp-pinctrl-common.h File Reference

`#include <[zephyr/dt-bindings/dt-util.h](dt-util_8h_source.md)>`

[Go to the source code of this file.](esp-pinctrl-common_8h_source.md)

| Macros | |
| --- | --- |
| #define | [ESP32\_PIN\_NUM\_SHIFT](#a14b1575596d4a3c7f349e140a206e7fc)   0U |
| #define | [ESP32\_PIN\_NUM\_MASK](#aff8c7306c9eb06955c069a08700b9602)   0x3FU |
| #define | [ESP32\_PIN\_SIGI\_MASK](#a0069fd5363ff598a903823729ac7b785)   0x1FFU |
| #define | [ESP32\_PIN\_SIGI\_SHIFT](#a457b5af6f423f5d743b81317f331f175)   6U |
| #define | [ESP32\_PIN\_SIGO\_MASK](#a97e539c13c42cabdb31c53dba9573bb8)   0x1FFU |
| #define | [ESP32\_PIN\_SIGO\_SHIFT](#ab7b2f3303e89bb59c9fc0aec216678fd)   15U |
| #define | [ESP\_SIG\_INVAL](#ae0d2e726ab8d90343e5c80e1d9b85ad8)   [ESP32\_PIN\_SIGI\_MASK](#a0069fd5363ff598a903823729ac7b785) |
| #define | [ESP32\_PINMUX](#a932ca0617135c66cc96fba696ac06e7e)(pin, sig\_i, sig\_o) |
| #define | [ESP32\_PIN\_BIAS\_SHIFT](#a47498f4ba429ddaedc5b2547888bfa00)   0U |
| #define | [ESP32\_PIN\_BIAS\_MASK](#a65d2b03b1a813cb4d2921c7cc8deec79)   0x3U |
| #define | [ESP32\_PIN\_DRV\_SHIFT](#abfdf0aa9a8a5116f3ca66e54e72552ac)   2U |
| #define | [ESP32\_PIN\_DRV\_MASK](#a4d05215be796ff091633a5f0de2a6748)   0x3U |
| #define | [ESP32\_PIN\_OUT\_SHIFT](#af20225f7ed095e083c3b7a2fa55a5313)   4U |
| #define | [ESP32\_PIN\_OUT\_MASK](#a0c806899f6fb854f50c3a88a40240691)   0x3U |
| #define | [ESP32\_PIN\_EN\_DIR\_SHIFT](#ada547ab4673154f6645f8d262196bf54)   6U |
| #define | [ESP32\_PIN\_EN\_DIR\_MASK](#a8941e50a06706315fcddfd327f10e7f2)   0x3U |
| #define | [ESP32\_NO\_PULL](#a843a0a112fd4aedae1620f0f0f02905c)   0x1 |
| #define | [ESP32\_PULL\_UP](#a13dba444526c095aa0a49dce05b1c161)   0x2 |
| #define | [ESP32\_PULL\_DOWN](#a5b49098dcea17780e9a9aedcd28ca562)   0x3 |
| #define | [ESP32\_PUSH\_PULL](#a02095f7bdbede933c2cb8990cd998570)   0x1 |
| #define | [ESP32\_OPEN\_DRAIN](#a567b521d9f62935c1d608941224eb4b0)   0x2 |
| #define | [ESP32\_PIN\_OUT\_HIGH](#a387522c15cab88fb55679561b6c23afe)   0x1 |
| #define | [ESP32\_PIN\_OUT\_LOW](#acedc77d7c4c6f60dc7e532045ea51702)   0x2 |
| #define | [ESP32\_PIN\_OUT\_EN](#a8678e26aae080bf67117515bac2256bc)   0x1 |
| #define | [ESP32\_PIN\_IN\_EN](#a173eddf7263f3323721d71c287cffced)   0x2 |
| #define | [ESP32\_NO\_PULL\_FLAG](#a8bb1e084e133c0ac847cd909e554d0dc)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| #define | [ESP32\_PULL\_UP\_FLAG](#a56386d98e542dacf1a8495f87818245d)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| #define | [ESP32\_PULL\_DOWN\_FLAG](#abbf4dd79f73d03949d23879f17957c68)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| #define | [ESP32\_PUSH\_PULL\_FLAG](#a74692459ddf10cf6ad3025082c5938e1)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
| #define | [ESP32\_OPEN\_DRAIN\_FLAG](#aaa112a5822fa5277ffcecf2b6a8e867b)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
| #define | [ESP32\_DIR\_INP\_FLAG](#a4edea1a8b44a94e4ddaa824d9ed386ac)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5) |
| #define | [ESP32\_DIR\_OUT\_FLAG](#a963fadb9794622bc4ad325d7033b0aa8)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6) |
| #define | [ESP32\_PIN\_OUT\_HIGH\_FLAG](#a05728ca8ec232cc7c681e7b8fc60250a)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7) |
| #define | [ESP32\_PIN\_OUT\_LOW\_FLAG](#ac5bc7889673a30b546c4c2044f71fc68)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(8) |
| #define | [ESP32\_PIN\_OUT\_EN\_FLAG](#a427e8a8be0caa57aa81879f0fcb965c6)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(9) |
| #define | [ESP32\_PIN\_IN\_EN\_FLAG](#a314dc3e3e178119062625bbcc1601caf)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(10) |

## Macro Definition Documentation

## [◆ ](#a4edea1a8b44a94e4ddaa824d9ed386ac)ESP32\_DIR\_INP\_FLAG

| #define ESP32\_DIR\_INP\_FLAG   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5) |
| --- |

## [◆ ](#a963fadb9794622bc4ad325d7033b0aa8)ESP32\_DIR\_OUT\_FLAG

| #define ESP32\_DIR\_OUT\_FLAG   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6) |
| --- |

## [◆ ](#a843a0a112fd4aedae1620f0f0f02905c)ESP32\_NO\_PULL

| #define ESP32\_NO\_PULL   0x1 |
| --- |

## [◆ ](#a8bb1e084e133c0ac847cd909e554d0dc)ESP32\_NO\_PULL\_FLAG

| #define ESP32\_NO\_PULL\_FLAG   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

## [◆ ](#a567b521d9f62935c1d608941224eb4b0)ESP32\_OPEN\_DRAIN

| #define ESP32\_OPEN\_DRAIN   0x2 |
| --- |

## [◆ ](#aaa112a5822fa5277ffcecf2b6a8e867b)ESP32\_OPEN\_DRAIN\_FLAG

| #define ESP32\_OPEN\_DRAIN\_FLAG   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
| --- |

## [◆ ](#a65d2b03b1a813cb4d2921c7cc8deec79)ESP32\_PIN\_BIAS\_MASK

| #define ESP32\_PIN\_BIAS\_MASK   0x3U |
| --- |

## [◆ ](#a47498f4ba429ddaedc5b2547888bfa00)ESP32\_PIN\_BIAS\_SHIFT

| #define ESP32\_PIN\_BIAS\_SHIFT   0U |
| --- |

## [◆ ](#a4d05215be796ff091633a5f0de2a6748)ESP32\_PIN\_DRV\_MASK

| #define ESP32\_PIN\_DRV\_MASK   0x3U |
| --- |

## [◆ ](#abfdf0aa9a8a5116f3ca66e54e72552ac)ESP32\_PIN\_DRV\_SHIFT

| #define ESP32\_PIN\_DRV\_SHIFT   2U |
| --- |

## [◆ ](#a8941e50a06706315fcddfd327f10e7f2)ESP32\_PIN\_EN\_DIR\_MASK

| #define ESP32\_PIN\_EN\_DIR\_MASK   0x3U |
| --- |

## [◆ ](#ada547ab4673154f6645f8d262196bf54)ESP32\_PIN\_EN\_DIR\_SHIFT

| #define ESP32\_PIN\_EN\_DIR\_SHIFT   6U |
| --- |

## [◆ ](#a173eddf7263f3323721d71c287cffced)ESP32\_PIN\_IN\_EN

| #define ESP32\_PIN\_IN\_EN   0x2 |
| --- |

## [◆ ](#a314dc3e3e178119062625bbcc1601caf)ESP32\_PIN\_IN\_EN\_FLAG

| #define ESP32\_PIN\_IN\_EN\_FLAG   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(10) |
| --- |

## [◆ ](#aff8c7306c9eb06955c069a08700b9602)ESP32\_PIN\_NUM\_MASK

| #define ESP32\_PIN\_NUM\_MASK   0x3FU |
| --- |

## [◆ ](#a14b1575596d4a3c7f349e140a206e7fc)ESP32\_PIN\_NUM\_SHIFT

| #define ESP32\_PIN\_NUM\_SHIFT   0U |
| --- |

## [◆ ](#a8678e26aae080bf67117515bac2256bc)ESP32\_PIN\_OUT\_EN

| #define ESP32\_PIN\_OUT\_EN   0x1 |
| --- |

## [◆ ](#a427e8a8be0caa57aa81879f0fcb965c6)ESP32\_PIN\_OUT\_EN\_FLAG

| #define ESP32\_PIN\_OUT\_EN\_FLAG   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(9) |
| --- |

## [◆ ](#a387522c15cab88fb55679561b6c23afe)ESP32\_PIN\_OUT\_HIGH

| #define ESP32\_PIN\_OUT\_HIGH   0x1 |
| --- |

## [◆ ](#a05728ca8ec232cc7c681e7b8fc60250a)ESP32\_PIN\_OUT\_HIGH\_FLAG

| #define ESP32\_PIN\_OUT\_HIGH\_FLAG   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7) |
| --- |

## [◆ ](#acedc77d7c4c6f60dc7e532045ea51702)ESP32\_PIN\_OUT\_LOW

| #define ESP32\_PIN\_OUT\_LOW   0x2 |
| --- |

## [◆ ](#ac5bc7889673a30b546c4c2044f71fc68)ESP32\_PIN\_OUT\_LOW\_FLAG

| #define ESP32\_PIN\_OUT\_LOW\_FLAG   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(8) |
| --- |

## [◆ ](#a0c806899f6fb854f50c3a88a40240691)ESP32\_PIN\_OUT\_MASK

| #define ESP32\_PIN\_OUT\_MASK   0x3U |
| --- |

## [◆ ](#af20225f7ed095e083c3b7a2fa55a5313)ESP32\_PIN\_OUT\_SHIFT

| #define ESP32\_PIN\_OUT\_SHIFT   4U |
| --- |

## [◆ ](#a0069fd5363ff598a903823729ac7b785)ESP32\_PIN\_SIGI\_MASK

| #define ESP32\_PIN\_SIGI\_MASK   0x1FFU |
| --- |

## [◆ ](#a457b5af6f423f5d743b81317f331f175)ESP32\_PIN\_SIGI\_SHIFT

| #define ESP32\_PIN\_SIGI\_SHIFT   6U |
| --- |

## [◆ ](#a97e539c13c42cabdb31c53dba9573bb8)ESP32\_PIN\_SIGO\_MASK

| #define ESP32\_PIN\_SIGO\_MASK   0x1FFU |
| --- |

## [◆ ](#ab7b2f3303e89bb59c9fc0aec216678fd)ESP32\_PIN\_SIGO\_SHIFT

| #define ESP32\_PIN\_SIGO\_SHIFT   15U |
| --- |

## [◆ ](#a932ca0617135c66cc96fba696ac06e7e)ESP32\_PINMUX

| #define ESP32\_PINMUX | ( |  | *pin*, |
| --- | --- | --- | --- |
|  |  |  | *sig\_i*, |
|  |  |  | *sig\_o* ) |

**Value:**

(((pin & [ESP32\_PIN\_NUM\_MASK](#aff8c7306c9eb06955c069a08700b9602)) << [ESP32\_PIN\_NUM\_SHIFT](#a14b1575596d4a3c7f349e140a206e7fc)) | \

((sig\_i & [ESP32\_PIN\_SIGI\_MASK](#a0069fd5363ff598a903823729ac7b785)) << [ESP32\_PIN\_SIGI\_SHIFT](#a457b5af6f423f5d743b81317f331f175)) | \

((sig\_o & [ESP32\_PIN\_SIGO\_MASK](#a97e539c13c42cabdb31c53dba9573bb8)) << [ESP32\_PIN\_SIGO\_SHIFT](#ab7b2f3303e89bb59c9fc0aec216678fd)))

[ESP32\_PIN\_SIGI\_MASK](#a0069fd5363ff598a903823729ac7b785)

#define ESP32\_PIN\_SIGI\_MASK

**Definition** esp-pinctrl-common.h:20

[ESP32\_PIN\_NUM\_SHIFT](#a14b1575596d4a3c7f349e140a206e7fc)

#define ESP32\_PIN\_NUM\_SHIFT

**Definition** esp-pinctrl-common.h:12

[ESP32\_PIN\_SIGI\_SHIFT](#a457b5af6f423f5d743b81317f331f175)

#define ESP32\_PIN\_SIGI\_SHIFT

**Definition** esp-pinctrl-common.h:21

[ESP32\_PIN\_SIGO\_MASK](#a97e539c13c42cabdb31c53dba9573bb8)

#define ESP32\_PIN\_SIGO\_MASK

**Definition** esp-pinctrl-common.h:22

[ESP32\_PIN\_SIGO\_SHIFT](#ab7b2f3303e89bb59c9fc0aec216678fd)

#define ESP32\_PIN\_SIGO\_SHIFT

**Definition** esp-pinctrl-common.h:23

[ESP32\_PIN\_NUM\_MASK](#aff8c7306c9eb06955c069a08700b9602)

#define ESP32\_PIN\_NUM\_MASK

**Definition** esp-pinctrl-common.h:13

## [◆ ](#a5b49098dcea17780e9a9aedcd28ca562)ESP32\_PULL\_DOWN

| #define ESP32\_PULL\_DOWN   0x3 |
| --- |

## [◆ ](#abbf4dd79f73d03949d23879f17957c68)ESP32\_PULL\_DOWN\_FLAG

| #define ESP32\_PULL\_DOWN\_FLAG   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| --- |

## [◆ ](#a13dba444526c095aa0a49dce05b1c161)ESP32\_PULL\_UP

| #define ESP32\_PULL\_UP   0x2 |
| --- |

## [◆ ](#a56386d98e542dacf1a8495f87818245d)ESP32\_PULL\_UP\_FLAG

| #define ESP32\_PULL\_UP\_FLAG   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| --- |

## [◆ ](#a02095f7bdbede933c2cb8990cd998570)ESP32\_PUSH\_PULL

| #define ESP32\_PUSH\_PULL   0x1 |
| --- |

## [◆ ](#a74692459ddf10cf6ad3025082c5938e1)ESP32\_PUSH\_PULL\_FLAG

| #define ESP32\_PUSH\_PULL\_FLAG   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
| --- |

## [◆ ](#ae0d2e726ab8d90343e5c80e1d9b85ad8)ESP\_SIG\_INVAL

| #define ESP\_SIG\_INVAL   [ESP32\_PIN\_SIGI\_MASK](#a0069fd5363ff598a903823729ac7b785) |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [pinctrl](dir_2c6c4fbd167577104b7f1b7148586168.md)
- [esp-pinctrl-common.h](esp-pinctrl-common_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
