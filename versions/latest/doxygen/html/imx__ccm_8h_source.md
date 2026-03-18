---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/imx__ccm_8h_source.html
original_path: doxygen/html/imx__ccm_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

imx\_ccm.h

[Go to the documentation of this file.](imx__ccm_8h.md)

1/\*

2 \* Copyright (c) 2017-2022, NXP

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_IMX\_CCM\_H\_

8#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_IMX\_CCM\_H\_

9

10/\*

11 \* Define 16 bits clock ID: 0xXXXX

12 \* The highest 8 bits is Peripheral ID

13 \* The lowest 8 bits is Instance ID

14 \*/

[ 15](imx__ccm_8h.md#aa31bf3cf51ff3af717f0d4037eeaa1c9)#define IMX\_CCM\_PERIPHERAL\_MASK 0xFF00UL

[ 16](imx__ccm_8h.md#a30f30d268fb9aae738f27161e6028f73)#define IMX\_CCM\_INSTANCE\_MASK 0x00FFUL

17

[ 18](imx__ccm_8h.md#ab1e95e431d7486c814c969d0d9c57559)#define IMX\_CCM\_CORESYS\_CLK 0x0000UL

[ 19](imx__ccm_8h.md#afcda3a44b4029872bfa5d219f10dd506)#define IMX\_CCM\_PLATFORM\_CLK 0x0100UL

[ 20](imx__ccm_8h.md#a0f9e44ec176274d3792bb2dd3e21a28b)#define IMX\_CCM\_BUS\_CLK 0x0200UL

21

[ 22](imx__ccm_8h.md#a01fa41a7ad66c54b1c19455b6160bbc2)#define IMX\_CCM\_LPUART\_CLK 0x0300UL

[ 23](imx__ccm_8h.md#a96e62b5b478ee548a1e52b7189a73817)#define IMX\_CCM\_LPUART1\_CLK 0x0300UL

[ 24](imx__ccm_8h.md#a46255999d02ae6161981374872e065cf)#define IMX\_CCM\_LPUART2\_CLK 0x0301UL

[ 25](imx__ccm_8h.md#a6676eb59f3d665c2a9bba7aae24228ca)#define IMX\_CCM\_LPUART3\_CLK 0x0302UL

[ 26](imx__ccm_8h.md#a9647111e5a5af6e8e67e059009490974)#define IMX\_CCM\_LPUART4\_CLK 0x0303UL

[ 27](imx__ccm_8h.md#acd84397a25a81c7f315c7740049d570a)#define IMX\_CCM\_LPUART5\_CLK 0x0304UL

[ 28](imx__ccm_8h.md#a3c6916f6ff4fae75dc51177e25d51642)#define IMX\_CCM\_LPUART6\_CLK 0x0305UL

[ 29](imx__ccm_8h.md#a4f2f07925d50b73cdc218d1f99cedf98)#define IMX\_CCM\_LPUART7\_CLK 0x0306UL

[ 30](imx__ccm_8h.md#a8db4fa3e674535ba490d89a52979cad0)#define IMX\_CCM\_LPUART8\_CLK 0x0307UL

31

[ 32](imx__ccm_8h.md#ac970114caf03b14bf6d3f2ff04f548dc)#define IMX\_CCM\_LPI2C\_CLK 0x0400UL

33

[ 34](imx__ccm_8h.md#a169487d4c020dee2492e36202fa39158)#define IMX\_CCM\_LPSPI\_CLK 0x0500UL

35

[ 36](imx__ccm_8h.md#a3f07127852de7ae5516c376589f1f780)#define IMX\_CCM\_USDHC1\_CLK 0x0600UL

[ 37](imx__ccm_8h.md#a4596ce38e656971ec5330dab452bd04c)#define IMX\_CCM\_USDHC2\_CLK 0x0601UL

38

[ 39](imx__ccm_8h.md#aa82ff051d04371deee96c754d93abb57)#define IMX\_CCM\_EDMA\_CLK 0x0700UL

40

[ 41](imx__ccm_8h.md#a62f00f098b8ee58612dd7cd5cc9da1e3)#define IMX\_CCM\_UART1\_CLK 0x0800UL

[ 42](imx__ccm_8h.md#a87c6bd30a90ca0cfdba829ae3cef2323)#define IMX\_CCM\_UART2\_CLK 0x0801UL

[ 43](imx__ccm_8h.md#aca209cf9c7038df4c53cb6ee930dfcd9)#define IMX\_CCM\_UART3\_CLK 0x0802UL

[ 44](imx__ccm_8h.md#a87564f52751e46be9ca0cec40c197f24)#define IMX\_CCM\_UART4\_CLK 0x0803UL

45

[ 46](imx__ccm_8h.md#aded96aef4768dd5f01d14a163cd7487d)#define IMX\_CCM\_CAN\_CLK 0x0900UL

47

[ 48](imx__ccm_8h.md#aadc28bb4c97c89e86a8a437262a3afad)#define IMX\_CCM\_GPT\_CLK 0x0A00UL

49

[ 50](imx__ccm_8h.md#a398527cf42962caf290b9ce1e5d7f9ac)#define IMX\_CCM\_SAI1\_CLK 0x0B00UL

[ 51](imx__ccm_8h.md#aae6ea492162692b3ae2dc6aed60cc08d)#define IMX\_CCM\_SAI2\_CLK 0x0B01UL

[ 52](imx__ccm_8h.md#a28779c577a92d4806239fe6e254d1a84)#define IMX\_CCM\_SAI3\_CLK 0x0B02UL

53

[ 54](imx__ccm_8h.md#acbc9256c26bb1232c5ca0eb8bfe52c22)#define IMX\_CCM\_PWM\_CLK 0x0C00UL

55

[ 56](imx__ccm_8h.md#a0cc7a30460bef2b0e6772a91539203a8)#define IMX\_CCM\_QTMR\_CLK 0x0D00UL

57

[ 58](imx__ccm_8h.md#aaeff78179dff600c88c1d1986b3976cd)#define IMX\_CCM\_ENET\_CLK 0x0E00UL

[ 59](imx__ccm_8h.md#a2a4beef16589b00f9aca825e7419e9ff)#define IMX\_CCM\_ENET\_PLL 0x0E01UL

60

[ 61](imx__ccm_8h.md#a5f86bba59cc685682df75e66a5d64cea)#define IMX\_CCM\_FLEXSPI\_CLK 0x0F00UL

[ 62](imx__ccm_8h.md#aa471a61b4b453551839b29322ec21422)#define IMX\_CCM\_FLEXSPI2\_CLK 0x0F01UL

63

64#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_IMX\_CCM\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [clock](dir_6e9992ac75fd0b7a50e889108957c907.md)
- [imx\_ccm.h](imx__ccm_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
