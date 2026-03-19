---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/esp-pinctrl-common_8h_source.html
original_path: doxygen/html/esp-pinctrl-common_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

esp-pinctrl-common.h

[Go to the documentation of this file.](esp-pinctrl-common_8h.md)

1/\*

2 \* Copyright (c) 2022 Espressif Systems (Shanghai) Co., Ltd.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_PINCTRL\_ESP\_PINCTRL\_COMMON\_H\_

8#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_PINCTRL\_ESP\_PINCTRL\_COMMON\_H\_

9

10#include <[zephyr/dt-bindings/dt-util.h](dt-util_8h.md)>

11

[ 12](esp-pinctrl-common_8h.md#a14b1575596d4a3c7f349e140a206e7fc)#define ESP32\_PIN\_NUM\_SHIFT 0U

[ 13](esp-pinctrl-common_8h.md#aff8c7306c9eb06955c069a08700b9602)#define ESP32\_PIN\_NUM\_MASK 0x3FU

14

15/\*

16 \* Definitions used to extract I/O

17 \* signal indexes used by the GPIO

18 \* matrix signal routing mechanism

19 \*/

[ 20](esp-pinctrl-common_8h.md#a0069fd5363ff598a903823729ac7b785)#define ESP32\_PIN\_SIGI\_MASK 0x1FFU

[ 21](esp-pinctrl-common_8h.md#a457b5af6f423f5d743b81317f331f175)#define ESP32\_PIN\_SIGI\_SHIFT 6U

[ 22](esp-pinctrl-common_8h.md#a97e539c13c42cabdb31c53dba9573bb8)#define ESP32\_PIN\_SIGO\_MASK 0x1FFU

[ 23](esp-pinctrl-common_8h.md#ab7b2f3303e89bb59c9fc0aec216678fd)#define ESP32\_PIN\_SIGO\_SHIFT 15U

[ 24](esp-pinctrl-common_8h.md#ae0d2e726ab8d90343e5c80e1d9b85ad8)#define ESP\_SIG\_INVAL ESP32\_PIN\_SIGI\_MASK

25

[ 26](esp-pinctrl-common_8h.md#a932ca0617135c66cc96fba696ac06e7e)#define ESP32\_PINMUX(pin, sig\_i, sig\_o) \

27 (((pin & ESP32\_PIN\_NUM\_MASK) << ESP32\_PIN\_NUM\_SHIFT) | \

28 ((sig\_i & ESP32\_PIN\_SIGI\_MASK) << ESP32\_PIN\_SIGI\_SHIFT) | \

29 ((sig\_o & ESP32\_PIN\_SIGO\_MASK) << ESP32\_PIN\_SIGO\_SHIFT))

30

31/\*

32 \* Definitions used to extract pin

33 \* properties: bias, drive and

34 \* initial pin level

35 \*/

[ 36](esp-pinctrl-common_8h.md#a47498f4ba429ddaedc5b2547888bfa00)#define ESP32\_PIN\_BIAS\_SHIFT 0U

[ 37](esp-pinctrl-common_8h.md#a65d2b03b1a813cb4d2921c7cc8deec79)#define ESP32\_PIN\_BIAS\_MASK 0x3U

[ 38](esp-pinctrl-common_8h.md#abfdf0aa9a8a5116f3ca66e54e72552ac)#define ESP32\_PIN\_DRV\_SHIFT 2U

[ 39](esp-pinctrl-common_8h.md#a4d05215be796ff091633a5f0de2a6748)#define ESP32\_PIN\_DRV\_MASK 0x3U

[ 40](esp-pinctrl-common_8h.md#af20225f7ed095e083c3b7a2fa55a5313)#define ESP32\_PIN\_OUT\_SHIFT 4U

[ 41](esp-pinctrl-common_8h.md#a0c806899f6fb854f50c3a88a40240691)#define ESP32\_PIN\_OUT\_MASK 0x3U

[ 42](esp-pinctrl-common_8h.md#ada547ab4673154f6645f8d262196bf54)#define ESP32\_PIN\_EN\_DIR\_SHIFT 6U

[ 43](esp-pinctrl-common_8h.md#a8941e50a06706315fcddfd327f10e7f2)#define ESP32\_PIN\_EN\_DIR\_MASK 0x3U

44

45/\* Bias definitions \*/

[ 46](esp-pinctrl-common_8h.md#a843a0a112fd4aedae1620f0f0f02905c)#define ESP32\_NO\_PULL 0x1

[ 47](esp-pinctrl-common_8h.md#a13dba444526c095aa0a49dce05b1c161)#define ESP32\_PULL\_UP 0x2

[ 48](esp-pinctrl-common_8h.md#a5b49098dcea17780e9a9aedcd28ca562)#define ESP32\_PULL\_DOWN 0x3

49

50/\* Pin drive definitions \*/

[ 51](esp-pinctrl-common_8h.md#a02095f7bdbede933c2cb8990cd998570)#define ESP32\_PUSH\_PULL 0x1

[ 52](esp-pinctrl-common_8h.md#a567b521d9f62935c1d608941224eb4b0)#define ESP32\_OPEN\_DRAIN 0x2

53

54/\*

55 \* An output pin can be initialized

56 \* to either high or low

57 \*/

[ 58](esp-pinctrl-common_8h.md#a387522c15cab88fb55679561b6c23afe)#define ESP32\_PIN\_OUT\_HIGH 0x1

[ 59](esp-pinctrl-common_8h.md#acedc77d7c4c6f60dc7e532045ea51702)#define ESP32\_PIN\_OUT\_LOW 0x2

60

61/\*

62 \* Enable input or output on pin

63 \* regardless of its direction

64 \*/

[ 65](esp-pinctrl-common_8h.md#a8678e26aae080bf67117515bac2256bc)#define ESP32\_PIN\_OUT\_EN 0x1

[ 66](esp-pinctrl-common_8h.md#a173eddf7263f3323721d71c287cffced)#define ESP32\_PIN\_IN\_EN 0x2

67

68/\*

69 \* These flags are used by the pinctrl

70 \* driver, based on the DTS properties

71 \* assigned to a specific pin state

72 \*/

[ 73](esp-pinctrl-common_8h.md#a8bb1e084e133c0ac847cd909e554d0dc)#define ESP32\_NO\_PULL\_FLAG BIT(0)

[ 74](esp-pinctrl-common_8h.md#a56386d98e542dacf1a8495f87818245d)#define ESP32\_PULL\_UP\_FLAG BIT(1)

[ 75](esp-pinctrl-common_8h.md#abbf4dd79f73d03949d23879f17957c68)#define ESP32\_PULL\_DOWN\_FLAG BIT(2)

[ 76](esp-pinctrl-common_8h.md#a74692459ddf10cf6ad3025082c5938e1)#define ESP32\_PUSH\_PULL\_FLAG BIT(3)

[ 77](esp-pinctrl-common_8h.md#aaa112a5822fa5277ffcecf2b6a8e867b)#define ESP32\_OPEN\_DRAIN\_FLAG BIT(4)

[ 78](esp-pinctrl-common_8h.md#a4edea1a8b44a94e4ddaa824d9ed386ac)#define ESP32\_DIR\_INP\_FLAG BIT(5)

[ 79](esp-pinctrl-common_8h.md#a963fadb9794622bc4ad325d7033b0aa8)#define ESP32\_DIR\_OUT\_FLAG BIT(6)

[ 80](esp-pinctrl-common_8h.md#a05728ca8ec232cc7c681e7b8fc60250a)#define ESP32\_PIN\_OUT\_HIGH\_FLAG BIT(7)

[ 81](esp-pinctrl-common_8h.md#ac5bc7889673a30b546c4c2044f71fc68)#define ESP32\_PIN\_OUT\_LOW\_FLAG BIT(8)

[ 82](esp-pinctrl-common_8h.md#a427e8a8be0caa57aa81879f0fcb965c6)#define ESP32\_PIN\_OUT\_EN\_FLAG BIT(9)

[ 83](esp-pinctrl-common_8h.md#a314dc3e3e178119062625bbcc1601caf)#define ESP32\_PIN\_IN\_EN\_FLAG BIT(10)

84

85#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_PINCTRL\_ESP\_PINCTRL\_COMMON\_H\_ \*/

[dt-util.h](dt-util_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [pinctrl](dir_2c6c4fbd167577104b7f1b7148586168.md)
- [esp-pinctrl-common.h](esp-pinctrl-common_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
