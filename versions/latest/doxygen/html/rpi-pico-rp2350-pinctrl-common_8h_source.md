---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/rpi-pico-rp2350-pinctrl-common_8h_source.html
original_path: doxygen/html/rpi-pico-rp2350-pinctrl-common_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

rpi-pico-rp2350-pinctrl-common.h

[Go to the documentation of this file.](rpi-pico-rp2350-pinctrl-common_8h.md)

1/\*

2 \* Copyright (c) 2024, Andrew Featherstone

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_PINCTRL\_RPI\_PICO\_RP2350\_PINCTRL\_COMMON\_H\_

8#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_PINCTRL\_RPI\_PICO\_RP2350\_PINCTRL\_COMMON\_H\_

9

[ 10](rpi-pico-rp2350-pinctrl-common_8h.md#a9356f0d59e815aa7eb68a9a0d28a98b5)#define RP2\_PINCTRL\_GPIO\_FUNC\_HSTX 0

11

[ 12](rpi-pico-rp2350-pinctrl-common_8h.md#a6e5aa7d27adbb2a89b344b01ac36512b)#define RP2\_PINCTRL\_GPIO\_FUNC\_PIO2 8

[ 13](rpi-pico-rp2350-pinctrl-common_8h.md#ae8dbbdfe35ec98d85c37a26567f6c5a6)#define RP2\_PINCTRL\_GPIO\_FUNC\_GPCK 9

[ 14](rpi-pico-rp2350-pinctrl-common_8h.md#aaebc20e84ac500bf54912993a85c59e0)#define RP2\_PINCTRL\_GPIO\_FUNC\_USB 10

[ 15](rpi-pico-rp2350-pinctrl-common_8h.md#a61926376a0b0e9272ba5bd2169744ef7)#define RP2\_PINCTRL\_GPIO\_FUNC\_UART\_AUX 11

[ 16](rpi-pico-rp2350-pinctrl-common_8h.md#ad63060076f6b9b29d5c8fcb3bbda2e3a)#define RP2\_PINCTRL\_GPIO\_FUNC\_NULL 0x1f

17

18#include "[rpi-pico-pinctrl-common.h](rpi-pico-pinctrl-common_8h.md)"

19

[ 20](rpi-pico-rp2350-pinctrl-common_8h.md#a8559508cb0debc4e04a816b50af86f12)#define PIO2\_P0 RP2XXX\_PINMUX(0, RP2\_PINCTRL\_GPIO\_FUNC\_PIO2)

[ 21](rpi-pico-rp2350-pinctrl-common_8h.md#a736ee8c4ff78693b55ac4e9a9fe2e3ab)#define PIO2\_P1 RP2XXX\_PINMUX(1, RP2\_PINCTRL\_GPIO\_FUNC\_PIO2)

[ 22](rpi-pico-rp2350-pinctrl-common_8h.md#af2a0255ca9ae93a5679f04c572cebc4d)#define PIO2\_P2 RP2XXX\_PINMUX(2, RP2\_PINCTRL\_GPIO\_FUNC\_PIO2)

[ 23](rpi-pico-rp2350-pinctrl-common_8h.md#ab5e8cade65cbec3c9d392f7c309310a4)#define PIO2\_P3 RP2XXX\_PINMUX(3, RP2\_PINCTRL\_GPIO\_FUNC\_PIO2)

[ 24](rpi-pico-rp2350-pinctrl-common_8h.md#a3bb02a3be6aad05d8b3f4cd188ec78ea)#define PIO2\_P4 RP2XXX\_PINMUX(4, RP2\_PINCTRL\_GPIO\_FUNC\_PIO2)

[ 25](rpi-pico-rp2350-pinctrl-common_8h.md#a356e7433370fc0cf19f27dbe1b99e6a9)#define PIO2\_P5 RP2XXX\_PINMUX(5, RP2\_PINCTRL\_GPIO\_FUNC\_PIO2)

[ 26](rpi-pico-rp2350-pinctrl-common_8h.md#a15a05df5727387cc0eb1171ce5c86635)#define PIO2\_P6 RP2XXX\_PINMUX(6, RP2\_PINCTRL\_GPIO\_FUNC\_PIO2)

[ 27](rpi-pico-rp2350-pinctrl-common_8h.md#a5da2e5d62747a5333c52000c0a279042)#define PIO2\_P7 RP2XXX\_PINMUX(7, RP2\_PINCTRL\_GPIO\_FUNC\_PIO2)

[ 28](rpi-pico-rp2350-pinctrl-common_8h.md#a6f94a2ff7b2d9476ce45d2a6073cc151)#define PIO2\_P8 RP2XXX\_PINMUX(8, RP2\_PINCTRL\_GPIO\_FUNC\_PIO2)

[ 29](rpi-pico-rp2350-pinctrl-common_8h.md#ae8838e48954b858f444ed5b5ea77ee74)#define PIO2\_P9 RP2XXX\_PINMUX(9, RP2\_PINCTRL\_GPIO\_FUNC\_PIO2)

[ 30](rpi-pico-rp2350-pinctrl-common_8h.md#adbb6688fa5097081e0c9cdae05ffee37)#define PIO2\_P10 RP2XXX\_PINMUX(10, RP2\_PINCTRL\_GPIO\_FUNC\_PIO2)

[ 31](rpi-pico-rp2350-pinctrl-common_8h.md#abd74a085f06175b26352b7bff599e474)#define PIO2\_P11 RP2XXX\_PINMUX(11, RP2\_PINCTRL\_GPIO\_FUNC\_PIO2)

[ 32](rpi-pico-rp2350-pinctrl-common_8h.md#ab50f43a9cdc4188bd4fe6283b54fd96b)#define PIO2\_P12 RP2XXX\_PINMUX(12, RP2\_PINCTRL\_GPIO\_FUNC\_PIO2)

[ 33](rpi-pico-rp2350-pinctrl-common_8h.md#ad2eae3755d33545cc3c9d10c45e5b1ee)#define PIO2\_P13 RP2XXX\_PINMUX(13, RP2\_PINCTRL\_GPIO\_FUNC\_PIO2)

[ 34](rpi-pico-rp2350-pinctrl-common_8h.md#aec89765ee6656136c8cfad3e95ff14cf)#define PIO2\_P14 RP2XXX\_PINMUX(14, RP2\_PINCTRL\_GPIO\_FUNC\_PIO2)

[ 35](rpi-pico-rp2350-pinctrl-common_8h.md#a8e0e42c71a0d397af25d5eab4c7daeb2)#define PIO2\_P15 RP2XXX\_PINMUX(15, RP2\_PINCTRL\_GPIO\_FUNC\_PIO2)

[ 36](rpi-pico-rp2350-pinctrl-common_8h.md#ab51769f63d73879ff30e034f056059a3)#define PIO2\_P16 RP2XXX\_PINMUX(16, RP2\_PINCTRL\_GPIO\_FUNC\_PIO2)

[ 37](rpi-pico-rp2350-pinctrl-common_8h.md#a0931ff05755d0c7a9d8a40924c73f238)#define PIO2\_P17 RP2XXX\_PINMUX(17, RP2\_PINCTRL\_GPIO\_FUNC\_PIO2)

[ 38](rpi-pico-rp2350-pinctrl-common_8h.md#a03d3745986563ca99da80dd20f97af6e)#define PIO2\_P18 RP2XXX\_PINMUX(18, RP2\_PINCTRL\_GPIO\_FUNC\_PIO2)

[ 39](rpi-pico-rp2350-pinctrl-common_8h.md#a3664c5d5a386d36b62745dce42426228)#define PIO2\_P19 RP2XXX\_PINMUX(19, RP2\_PINCTRL\_GPIO\_FUNC\_PIO2)

[ 40](rpi-pico-rp2350-pinctrl-common_8h.md#a85f903911017ccdeeff3cb6536028859)#define PIO2\_P20 RP2XXX\_PINMUX(20, RP2\_PINCTRL\_GPIO\_FUNC\_PIO2)

[ 41](rpi-pico-rp2350-pinctrl-common_8h.md#ac2e81c1b956d496d873e79c03080b901)#define PIO2\_P21 RP2XXX\_PINMUX(21, RP2\_PINCTRL\_GPIO\_FUNC\_PIO2)

[ 42](rpi-pico-rp2350-pinctrl-common_8h.md#a55beacae2f94b13d854450145b8eb5c4)#define PIO2\_P22 RP2XXX\_PINMUX(22, RP2\_PINCTRL\_GPIO\_FUNC\_PIO2)

[ 43](rpi-pico-rp2350-pinctrl-common_8h.md#adc73d1fce25749efd90b5cd62917e7b6)#define PIO2\_P23 RP2XXX\_PINMUX(23, RP2\_PINCTRL\_GPIO\_FUNC\_PIO2)

[ 44](rpi-pico-rp2350-pinctrl-common_8h.md#af25edc9d42c1799f21da502739c6d97b)#define PIO2\_P24 RP2XXX\_PINMUX(24, RP2\_PINCTRL\_GPIO\_FUNC\_PIO2)

[ 45](rpi-pico-rp2350-pinctrl-common_8h.md#adb6fc8cab22214d2351db9c63cf523fa)#define PIO2\_P25 RP2XXX\_PINMUX(25, RP2\_PINCTRL\_GPIO\_FUNC\_PIO2)

[ 46](rpi-pico-rp2350-pinctrl-common_8h.md#a62a678054fc16ad09f963061916043ac)#define PIO2\_P26 RP2XXX\_PINMUX(26, RP2\_PINCTRL\_GPIO\_FUNC\_PIO2)

[ 47](rpi-pico-rp2350-pinctrl-common_8h.md#aabd4cc26e3ff80a6cd5124eb30cf8ac6)#define PIO2\_P27 RP2XXX\_PINMUX(27, RP2\_PINCTRL\_GPIO\_FUNC\_PIO2)

[ 48](rpi-pico-rp2350-pinctrl-common_8h.md#a235c8059662bbe774ad99621b3e83eab)#define PIO2\_P28 RP2XXX\_PINMUX(28, RP2\_PINCTRL\_GPIO\_FUNC\_PIO2)

[ 49](rpi-pico-rp2350-pinctrl-common_8h.md#ae10bd76b9a0b970eb5404ceb6aa99067)#define PIO2\_P29 RP2XXX\_PINMUX(29, RP2\_PINCTRL\_GPIO\_FUNC\_PIO2)

50

[ 51](rpi-pico-rp2350-pinctrl-common_8h.md#a5ac3e74f8eb74d8fce8394ef4dbde545)#define GPIN0\_P12 RP2XXX\_PINMUX(20, RP2\_PINCTRL\_GPIO\_FUNC\_GPCK)

[ 52](rpi-pico-rp2350-pinctrl-common_8h.md#a6ad89760a21cfec86df4b9761366a155)#define GPIN1\_P14 RP2XXX\_PINMUX(22, RP2\_PINCTRL\_GPIO\_FUNC\_GPCK)

[ 53](rpi-pico-rp2350-pinctrl-common_8h.md#a33b8d8a9ae7341c4addace139b5c1542)#define GPOUT0\_P13 RP2XXX\_PINMUX(21, RP2\_PINCTRL\_GPIO\_FUNC\_GPCK)

[ 54](rpi-pico-rp2350-pinctrl-common_8h.md#aa7041407a501b27c7854f9a3a2237f6d)#define GPOUT1\_P15 RP2XXX\_PINMUX(23, RP2\_PINCTRL\_GPIO\_FUNC\_GPCK)

55

[ 56](rpi-pico-rp2350-pinctrl-common_8h.md#aa77797c465257324967c7bf9e004dc04)#define UART0\_TX\_P2 RP2XXX\_PINMUX(2, RP2\_PINCTRL\_GPIO\_FUNC\_UART\_ALT)

[ 57](rpi-pico-rp2350-pinctrl-common_8h.md#ae5a05856601d96143e08a66e0d53fa7d)#define UART0\_RX\_P3 RP2XXX\_PINMUX(3, RP2\_PINCTRL\_GPIO\_FUNC\_UART\_ALT)

[ 58](rpi-pico-rp2350-pinctrl-common_8h.md#a7ad92e7b37042ee3b6cb328eaca0df79)#define UART1\_TX\_P6 RP2XXX\_PINMUX(6, RP2\_PINCTRL\_GPIO\_FUNC\_UART\_ALT)

[ 59](rpi-pico-rp2350-pinctrl-common_8h.md#a1bb4adcf4ab38aa0d375e221b0433fbc)#define UART1\_RX\_P7 RP2XXX\_PINMUX(7, RP2\_PINCTRL\_GPIO\_FUNC\_UART\_ALT)

[ 60](rpi-pico-rp2350-pinctrl-common_8h.md#ac88b63b2814a7d8284fa0863f0b86e5f)#define UART1\_TX\_P10 RP2XXX\_PINMUX(10, RP2\_PINCTRL\_GPIO\_FUNC\_UART\_ALT)

[ 61](rpi-pico-rp2350-pinctrl-common_8h.md#aadaef835ee545bff537bcf1701da0bcd)#define UART1\_RX\_P11 RP2XXX\_PINMUX(11, RP2\_PINCTRL\_GPIO\_FUNC\_UART\_ALT)

[ 62](rpi-pico-rp2350-pinctrl-common_8h.md#ad783e5789e82a9e2a80eea9df84a46e4)#define UART0\_TX\_P14 RP2XXX\_PINMUX(14, RP2\_PINCTRL\_GPIO\_FUNC\_UART\_ALT)

[ 63](rpi-pico-rp2350-pinctrl-common_8h.md#a8a84487c71609d2e81160ab27461c96c)#define UART0\_RX\_P15 RP2XXX\_PINMUX(15, RP2\_PINCTRL\_GPIO\_FUNC\_UART\_ALT)

[ 64](rpi-pico-rp2350-pinctrl-common_8h.md#af245566b22b9d3420095c4372b782575)#define UART0\_TX\_P18 RP2XXX\_PINMUX(18, RP2\_PINCTRL\_GPIO\_FUNC\_UART\_ALT)

[ 65](rpi-pico-rp2350-pinctrl-common_8h.md#a49e48627df1b5b84a41174e9df454672)#define UART0\_RX\_P19 RP2XXX\_PINMUX(19, RP2\_PINCTRL\_GPIO\_FUNC\_UART\_ALT)

[ 66](rpi-pico-rp2350-pinctrl-common_8h.md#a6056a04a0594f3fc5dbada14d3610c2c)#define UART1\_TX\_P22 RP2XXX\_PINMUX(22, RP2\_PINCTRL\_GPIO\_FUNC\_UART\_ALT)

[ 67](rpi-pico-rp2350-pinctrl-common_8h.md#af6690f7651fcb2c56880afad32e5b288)#define UART1\_RX\_P23 RP2XXX\_PINMUX(23, RP2\_PINCTRL\_GPIO\_FUNC\_UART\_ALT)

[ 68](rpi-pico-rp2350-pinctrl-common_8h.md#add2ad43ac7a7c1e08db710b0fdca896b)#define UART1\_TX\_P26 RP2XXX\_PINMUX(26, RP2\_PINCTRL\_GPIO\_FUNC\_UART\_ALT)

[ 69](rpi-pico-rp2350-pinctrl-common_8h.md#a4f3a8d5a85a2b2b31f4d857e2fe15d5f)#define UART1\_RX\_P27 RP2XXX\_PINMUX(27, RP2\_PINCTRL\_GPIO\_FUNC\_UART\_ALT)

70

71#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_PINCTRL\_RPI\_PICO\_RP2350\_PINCTRL\_COMMON\_H\_ \*/

[rpi-pico-pinctrl-common.h](rpi-pico-pinctrl-common_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [pinctrl](dir_2c6c4fbd167577104b7f1b7148586168.md)
- [rpi-pico-rp2350-pinctrl-common.h](rpi-pico-rp2350-pinctrl-common_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
