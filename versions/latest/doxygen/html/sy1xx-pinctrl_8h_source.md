---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/sy1xx-pinctrl_8h_source.html
original_path: doxygen/html/sy1xx-pinctrl_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

sy1xx-pinctrl.h

[Go to the documentation of this file.](sy1xx-pinctrl_8h.md)

1/\*

2 \* SPDX-License-Identifier: Apache-2.0

3 \* Copyright (c) 2024 sensry.io

4 \*/

5

6#ifndef \_ZEPHYR\_DT\_BINDINGS\_PINCTRL\_SY1XX\_PINCTRL\_

7#define \_ZEPHYR\_DT\_BINDINGS\_PINCTRL\_SY1XX\_PINCTRL\_

8

[ 9](sy1xx-pinctrl_8h.md#ad75005e085a8960d58f6d092b36a3457)#define SY1XX\_PAD(pad) (pad \* 8)

10

[ 11](sy1xx-pinctrl_8h.md#adc483e38c6c02d891a22b9bf84935b56)#define SY1XX\_UART0\_PAD\_CFG0 0x0020

[ 12](sy1xx-pinctrl_8h.md#a055d907bbf5efca0c1aa99ebd22702ed)#define SY1XX\_UART1\_PAD\_CFG0 0x0024

[ 13](sy1xx-pinctrl_8h.md#add2c72f1fbe994a823a20ca3201edafe)#define SY1XX\_UART2\_PAD\_CFG0 0x0028

14

[ 15](sy1xx-pinctrl_8h.md#a404e66d6cf88171347e3db0c3717157a)#define SY1XX\_SPI0\_PAD\_CFG0 0x002c

[ 16](sy1xx-pinctrl_8h.md#ae18b46685cdfd24b547632490ff10072)#define SY1XX\_SPI0\_PAD\_CFG1 0x0030

17

[ 18](sy1xx-pinctrl_8h.md#a9bf78b4c068d29050c35c26a55fbc20c)#define SY1XX\_SPI1\_PAD\_CFG0 0x0034

[ 19](sy1xx-pinctrl_8h.md#af4cf0968a02d32f9ac353a7326cc87f6)#define SY1XX\_SPI1\_PAD\_CFG1 0x0038

20

[ 21](sy1xx-pinctrl_8h.md#a6eecae08e7eec2034789a71b59e993ae)#define SY1XX\_SPI2\_PAD\_CFG0 0x003c

[ 22](sy1xx-pinctrl_8h.md#aadd9f2a4ae588a04d9fb6ecdd0e23814)#define SY1XX\_SPI2\_PAD\_CFG1 0x0040

23

[ 24](sy1xx-pinctrl_8h.md#a76f73bbaf1481d2635ef98eb3059cbcc)#define SY1XX\_SPI3\_PAD\_CFG0 0x0044

[ 25](sy1xx-pinctrl_8h.md#ab2806c2b057c0e3fbf067f51a2c44f1a)#define SY1XX\_SPI3\_PAD\_CFG1 0x0048

26

[ 27](sy1xx-pinctrl_8h.md#ab2fa82fdb2937f3609fa750cde52e31a)#define SY1XX\_SPI4\_PAD\_CFG0 0x004c

[ 28](sy1xx-pinctrl_8h.md#a8e75504deacf337c617a53edca490e0e)#define SY1XX\_SPI4\_PAD\_CFG1 0x0050

29

[ 30](sy1xx-pinctrl_8h.md#ac7d17056cdeceb0e829ad72a06ef9d09)#define SY1XX\_SPI5\_PAD\_CFG0 0x0054

[ 31](sy1xx-pinctrl_8h.md#a958f75d6c7419e2a9dba1c6577852696)#define SY1XX\_SPI5\_PAD\_CFG1 0x0058

32

[ 33](sy1xx-pinctrl_8h.md#a4b2305ff3b154e1d3c0daf811059043f)#define SY1XX\_SPI6\_PAD\_CFG0 0x005c

[ 34](sy1xx-pinctrl_8h.md#a8e0105c1d92748e3e51c333be3b919b0)#define SY1XX\_SPI6\_PAD\_CFG1 0x0060

35

[ 36](sy1xx-pinctrl_8h.md#a01bf7ff6920aca87fcda6b2a5136d989)#define SY1XX\_I2C0\_PAD\_CFG0 0x0100

[ 37](sy1xx-pinctrl_8h.md#ae7b8ecc3c5082bbddd99f9de460c8537)#define SY1XX\_I2C1\_PAD\_CFG0 0x0104

[ 38](sy1xx-pinctrl_8h.md#a35a4e2514b7237892e772e4d9f0e5c0d)#define SY1XX\_I2C2\_PAD\_CFG0 0x0108

[ 39](sy1xx-pinctrl_8h.md#a1b911fab051ea7108e0c273f5a491bde)#define SY1XX\_I2C3\_PAD\_CFG0 0x010c

40

[ 41](sy1xx-pinctrl_8h.md#ab4c601da01a0e39445cf963e07ac29e0)#define SY1XX\_GPIO0\_PAD\_CFG0 0x0110

[ 42](sy1xx-pinctrl_8h.md#a5159756f8ea829e08ba3b5a4533c7fc0)#define SY1XX\_GPIO0\_PAD\_CFG1 0x0114

[ 43](sy1xx-pinctrl_8h.md#a57de6bad22780defb68c4ee449450c36)#define SY1XX\_GPIO0\_PAD\_CFG2 0x0118

[ 44](sy1xx-pinctrl_8h.md#ac6fa6736e2d16b2a8f7fdebb335b5105)#define SY1XX\_GPIO0\_PAD\_CFG3 0x011c

[ 45](sy1xx-pinctrl_8h.md#a5da7b457738900d954c54d00e05ba187)#define SY1XX\_GPIO0\_PAD\_CFG4 0x0120

[ 46](sy1xx-pinctrl_8h.md#a3891aced0a6f74c1756916dba97bcfcb)#define SY1XX\_GPIO0\_PAD\_CFG5 0x0124

[ 47](sy1xx-pinctrl_8h.md#ae1e986b4c50e8cfb0b8e0a98ef1baea9)#define SY1XX\_GPIO0\_PAD\_CFG6 0x0128

[ 48](sy1xx-pinctrl_8h.md#a4135e0f0c3d9c4157e9c253fdc739cf4)#define SY1XX\_GPIO0\_PAD\_CFG7 0x012c

49

[ 50](sy1xx-pinctrl_8h.md#a13cce7da530425788383e11b9f35b5ce)#define SY1XX\_RGMII0\_PAD\_CFG0 0x0130

[ 51](sy1xx-pinctrl_8h.md#a06f53391cd6d71e86fa0736c089660b8)#define SY1XX\_RGMII0\_PAD\_CFG1 0x0134

[ 52](sy1xx-pinctrl_8h.md#a2a57254b422b7248d3d1f7fa56fa3ffe)#define SY1XX\_RGMII0\_PAD\_CFG2 0x0138

[ 53](sy1xx-pinctrl_8h.md#a2d1d2134971e68e70e23fe42f9f316d3)#define SY1XX\_RGMII0\_PAD\_CFG3 0x013c

54

[ 55](sy1xx-pinctrl_8h.md#a7853e14b27de17f111a1a7edc94b6a67)#define SY1XX\_CAN0\_PAD\_CFG0 0x0140

56

[ 57](sy1xx-pinctrl_8h.md#a92ed448d69e0232a2a16e364c8482d96)#define SY1XX\_I2S0\_PAD\_CFG0 0x0144

[ 58](sy1xx-pinctrl_8h.md#a55234d106fcfe72c40dc8e6bf7026c76)#define SY1XX\_I2S1\_PAD\_CFG0 0x0148

[ 59](sy1xx-pinctrl_8h.md#a2a9de099a9542907ed1ee1f79b52d98a)#define SY1XX\_I2S2\_PAD\_CFG0 0x014c

[ 60](sy1xx-pinctrl_8h.md#aeeec7f5df0f5a63c45e078d4eb11f3a0)#define SY1XX\_I2S3\_PAD\_CFG0 0x0150

61

[ 62](sy1xx-pinctrl_8h.md#a9a3d3cbbc4be0098c258b20c2dd70d6e)#define SY1XX\_HBUS0\_PAD\_CFG0 0x0154

[ 63](sy1xx-pinctrl_8h.md#a9eac3698c460c2b97ca180af2327bdf4)#define SY1XX\_HBUS0\_PAD\_CFG1 0x0158

[ 64](sy1xx-pinctrl_8h.md#a0ced8b047437b1b00b135f87557d46bd)#define SY1XX\_HBUS0\_PAD\_CFG2 0x015c

[ 65](sy1xx-pinctrl_8h.md#a2dca17d2f18be0dfe9146740c6e8fec3)#define SY1XX\_HBUS0\_PAD\_CFG3 0x0160

66

[ 67](sy1xx-pinctrl_8h.md#a901d32212b2702f2d1a12e6627c805fe)#define SY1XX\_QSPI0\_PAD\_CFG0 0x0164

[ 68](sy1xx-pinctrl_8h.md#aa473544922299dfa761d8594ddb7cedc)#define SY1XX\_QSPI0\_PAD\_CFG1 0x0168

69

70#endif /\* \_ZEPHYR\_DT\_BINDINGS\_PINCTRL\_SY1XX\_PINCTRL\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [pinctrl](dir_2c6c4fbd167577104b7f1b7148586168.md)
- [sy1xx-pinctrl.h](sy1xx-pinctrl_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
