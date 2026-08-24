---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/pinctrl-rzt-common_8h_source.html
original_path: doxygen/html/pinctrl-rzt-common_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

pinctrl-rzt-common.h

[Go to the documentation of this file.](pinctrl-rzt-common_8h.md)

1/\*

2 \* Copyright (c) 2025 Renesas Electronics Corporation

3 \* SPDX-License-Identifier: Apache-2.0

4 \*/

5

6#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_PINCTRL\_RENESAS\_PINCTRL\_RZT\_COMMON\_H\_

7#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_PINCTRL\_RENESAS\_PINCTRL\_RZT\_COMMON\_H\_

8

9/\* Superset list of all possible IO ports. \*/

[ 10](pinctrl-rzt-common_8h.md#a1b0292747e92dff43d6760d9e2258869)#define PORT\_00 0x0000 /\* IO port 0 \*/

[ 11](pinctrl-rzt-common_8h.md#a9de415830a2b3484dd33d5d08258dde5)#define PORT\_01 0x0100 /\* IO port 1 \*/

[ 12](pinctrl-rzt-common_8h.md#a7db623b2ec3816113a8f3fb07d5428ef)#define PORT\_02 0x0200 /\* IO port 2 \*/

[ 13](pinctrl-rzt-common_8h.md#a71478a4563d986886410618bc130b0d9)#define PORT\_03 0x0300 /\* IO port 3 \*/

[ 14](pinctrl-rzt-common_8h.md#aed73b97fc12615ac1dec9daad9537647)#define PORT\_04 0x0400 /\* IO port 4 \*/

[ 15](pinctrl-rzt-common_8h.md#a590020a2e6577d74d89bdee0989812c4)#define PORT\_05 0x0500 /\* IO port 5 \*/

[ 16](pinctrl-rzt-common_8h.md#ab2912aeb54c92971e0590ff3282e775b)#define PORT\_06 0x0600 /\* IO port 6 \*/

[ 17](pinctrl-rzt-common_8h.md#acabb0398db58703c47e718f899018410)#define PORT\_07 0x0700 /\* IO port 7 \*/

[ 18](pinctrl-rzt-common_8h.md#a5f4d0cfbea4e649fa0863d4a8d409c5e)#define PORT\_08 0x0800 /\* IO port 8 \*/

[ 19](pinctrl-rzt-common_8h.md#a5e8d840d1a1bd421615b2cc90ce0b90f)#define PORT\_09 0x0900 /\* IO port 9 \*/

[ 20](pinctrl-rzt-common_8h.md#a4c39a294d7b3a360c172b65151a5bfc8)#define PORT\_10 0x0A00 /\* IO port 10 \*/

[ 21](pinctrl-rzt-common_8h.md#abeebf6334cb5240b09d97d35fc0128f3)#define PORT\_11 0x0B00 /\* IO port 11 \*/

[ 22](pinctrl-rzt-common_8h.md#ae57c3ffa4df15481a9a219e16b011ef3)#define PORT\_12 0x0C00 /\* IO port 12 \*/

[ 23](pinctrl-rzt-common_8h.md#ae76dfcae2263b7d43d1ee23fa9548293)#define PORT\_13 0x0D00 /\* IO port 13 \*/

[ 24](pinctrl-rzt-common_8h.md#a9c8783d66b07c093c559a5fd74add129)#define PORT\_14 0x0E00 /\* IO port 14 \*/

[ 25](pinctrl-rzt-common_8h.md#aeb88886b16b5a8ea23147000fd9af3cc)#define PORT\_15 0x0F00 /\* IO port 15 \*/

[ 26](pinctrl-rzt-common_8h.md#aa9fff44f99e434f31b19ed55462b45d4)#define PORT\_16 0x1000 /\* IO port 16 \*/

[ 27](pinctrl-rzt-common_8h.md#a8ce8fd8ca6cdbc375b70a0b7d53eb315)#define PORT\_17 0x1100 /\* IO port 17 \*/

[ 28](pinctrl-rzt-common_8h.md#a51b6b92e7f3238a410526b67234f77d7)#define PORT\_18 0x1200 /\* IO port 18 \*/

[ 29](pinctrl-rzt-common_8h.md#a0c1b97684b0bbb0326a187117bcf78ae)#define PORT\_19 0x1300 /\* IO port 19 \*/

[ 30](pinctrl-rzt-common_8h.md#a87d7fd3777b47baab0317a96ee874842)#define PORT\_20 0x1400 /\* IO port 20 \*/

[ 31](pinctrl-rzt-common_8h.md#acc227be3abe2efbeed63891d0e4ad3db)#define PORT\_21 0x1500 /\* IO port 21 \*/

[ 32](pinctrl-rzt-common_8h.md#aefb67b06965dd6320a246fc0529917ad)#define PORT\_22 0x1600 /\* IO port 22 \*/

[ 33](pinctrl-rzt-common_8h.md#a1d7f17a633496267b4d19fc8fa89dbb5)#define PORT\_23 0x1700 /\* IO port 23 \*/

[ 34](pinctrl-rzt-common_8h.md#affbf09e2b0a16edd6b6201909ee99394)#define PORT\_24 0x1800 /\* IO port 24 \*/

35

36/\*

37 \* Create the value contain port/pin/function information

38 \*

39 \* port: port number BSP\_IO\_PORT\_00..BSP\_IO\_PORT\_24

40 \* pin: pin number

41 \* func: pin function

42 \*/

[ 43](pinctrl-rzt-common_8h.md#a1a49267479570ac585e3c98c68aa4239)#define RZT\_PINMUX(port, pin, func) (port | pin | (func << 4))

44

45#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_PINCTRL\_RENESAS\_PINCTRL\_RZT\_COMMON\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [pinctrl](dir_2c6c4fbd167577104b7f1b7148586168.md)
- [renesas](dir_17f48eb154be6cea623223db5de209e7.md)
- [pinctrl-rzt-common.h](pinctrl-rzt-common_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
