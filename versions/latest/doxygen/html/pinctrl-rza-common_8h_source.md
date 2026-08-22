---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/pinctrl-rza-common_8h_source.html
original_path: doxygen/html/pinctrl-rza-common_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

pinctrl-rza-common.h

[Go to the documentation of this file.](pinctrl-rza-common_8h.md)

1/\*

2 \* Copyright (c) 2025 Renesas Electronics Corporation

3 \* SPDX-License-Identifier: Apache-2.0

4 \*/

5

6#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_PINCTRL\_RENESAS\_PINCTRL\_RZA\_COMMON\_H\_

7#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_PINCTRL\_RENESAS\_PINCTRL\_RZA\_COMMON\_H\_

8

9/\* Superset list of all possible IO ports. \*/

[ 10](pinctrl-rza-common_8h.md#a1b0292747e92dff43d6760d9e2258869)#define PORT\_00 0x0000 /\* IO port 0 \*/

[ 11](pinctrl-rza-common_8h.md#a9de415830a2b3484dd33d5d08258dde5)#define PORT\_01 0x0100 /\* IO port 1 \*/

[ 12](pinctrl-rza-common_8h.md#a7db623b2ec3816113a8f3fb07d5428ef)#define PORT\_02 0x0200 /\* IO port 2 \*/

[ 13](pinctrl-rza-common_8h.md#a71478a4563d986886410618bc130b0d9)#define PORT\_03 0x0300 /\* IO port 3 \*/

[ 14](pinctrl-rza-common_8h.md#aed73b97fc12615ac1dec9daad9537647)#define PORT\_04 0x0400 /\* IO port 4 \*/

[ 15](pinctrl-rza-common_8h.md#a590020a2e6577d74d89bdee0989812c4)#define PORT\_05 0x0500 /\* IO port 5 \*/

[ 16](pinctrl-rza-common_8h.md#ab2912aeb54c92971e0590ff3282e775b)#define PORT\_06 0x0600 /\* IO port 6 \*/

[ 17](pinctrl-rza-common_8h.md#acabb0398db58703c47e718f899018410)#define PORT\_07 0x0700 /\* IO port 7 \*/

[ 18](pinctrl-rza-common_8h.md#a5f4d0cfbea4e649fa0863d4a8d409c5e)#define PORT\_08 0x0800 /\* IO port 8 \*/

[ 19](pinctrl-rza-common_8h.md#a5e8d840d1a1bd421615b2cc90ce0b90f)#define PORT\_09 0x0900 /\* IO port 9 \*/

[ 20](pinctrl-rza-common_8h.md#a4c39a294d7b3a360c172b65151a5bfc8)#define PORT\_10 0x0A00 /\* IO port 10 \*/

[ 21](pinctrl-rza-common_8h.md#abeebf6334cb5240b09d97d35fc0128f3)#define PORT\_11 0x0B00 /\* IO port 11 \*/

[ 22](pinctrl-rza-common_8h.md#ae57c3ffa4df15481a9a219e16b011ef3)#define PORT\_12 0x0C00 /\* IO port 12 \*/

[ 23](pinctrl-rza-common_8h.md#ae76dfcae2263b7d43d1ee23fa9548293)#define PORT\_13 0x0D00 /\* IO port 13 \*/

[ 24](pinctrl-rza-common_8h.md#a9c8783d66b07c093c559a5fd74add129)#define PORT\_14 0x0E00 /\* IO port 14 \*/

[ 25](pinctrl-rza-common_8h.md#aeb88886b16b5a8ea23147000fd9af3cc)#define PORT\_15 0x0F00 /\* IO port 15 \*/

[ 26](pinctrl-rza-common_8h.md#aa9fff44f99e434f31b19ed55462b45d4)#define PORT\_16 0x1000 /\* IO port 16 \*/

[ 27](pinctrl-rza-common_8h.md#a8ce8fd8ca6cdbc375b70a0b7d53eb315)#define PORT\_17 0x1100 /\* IO port 17 \*/

[ 28](pinctrl-rza-common_8h.md#a51b6b92e7f3238a410526b67234f77d7)#define PORT\_18 0x1200 /\* IO port 18 \*/

29

30/\*

31 \* Create the value contain port/pin/function information

32 \*

33 \* port: port number BSP\_IO\_PORT\_00..BSP\_IO\_PORT\_18

34 \* pin: pin number

35 \* func: pin function

36 \*/

[ 37](pinctrl-rza-common_8h.md#aad0f3d9e2b289afca587d9897ad35210)#define RZA\_PINMUX(port, pin, func) (port | pin | (func << 4))

38

39/\* Special purpose port \*/

[ 40](pinctrl-rza-common_8h.md#a5a8b4d2cdc15f25cc0b58db97c539b2a)#define BSP\_IO\_NMI 0xFFFF0100 /\* NMI \*/

41

[ 42](pinctrl-rza-common_8h.md#af06a8358900119f6b4c3d91e465ce22f)#define BSP\_IO\_TMS\_SWDIO 0xFFFF0200 /\* TMS\_SWDIO \*/

43

[ 44](pinctrl-rza-common_8h.md#a318b423b2efc8ab1a3de0a8f9ab3eeca)#define BSP\_IO\_TDO 0xFFFF0300 /\* TDO \*/

45

[ 46](pinctrl-rza-common_8h.md#acf9b257ce3e3a66bcfa8d4aca427c0bf)#define BSP\_IO\_AUDIO\_CLK1 0xFFFF0400 /\* AUDIO\_CLK1 \*/

[ 47](pinctrl-rza-common_8h.md#a98d349e2311d1571d490e26866871b16)#define BSP\_IO\_AUDIO\_CLK2 0xFFFF0401 /\* AUDIO\_CLK2 \*/

48

[ 49](pinctrl-rza-common_8h.md#a99cac86447ae6b18e3e1601085623a60)#define BSP\_IO\_SD0\_CLK 0xFFFF0600 /\* CD0\_CLK \*/

[ 50](pinctrl-rza-common_8h.md#a2b904f716e2bf524351430155b8c7ddc)#define BSP\_IO\_SD0\_CMD 0xFFFF0601 /\* CD0\_CMD \*/

[ 51](pinctrl-rza-common_8h.md#ad61d120b88812e3c41a600414f553325)#define BSP\_IO\_SD0\_RST\_N 0xFFFF0602 /\* CD0\_RST\_N \*/

52

[ 53](pinctrl-rza-common_8h.md#a1f4951bb275e24732e8487dffd5fe69a)#define BSP\_IO\_SD0\_DATA0 0xFFFF0700 /\* SD0\_DATA0 \*/

[ 54](pinctrl-rza-common_8h.md#a97428f756c92136fd0f3d34f520c760b)#define BSP\_IO\_SD0\_DATA1 0xFFFF0701 /\* SD0\_DATA1 \*/

[ 55](pinctrl-rza-common_8h.md#a77fab2fb18ce2a3d779d94b54e8d58d1)#define BSP\_IO\_SD0\_DATA2 0xFFFF0702 /\* SD0\_DATA2 \*/

[ 56](pinctrl-rza-common_8h.md#a8794e04fe7b7d3d895973cac59538095)#define BSP\_IO\_SD0\_DATA3 0xFFFF0703 /\* SD0\_DATA3 \*/

[ 57](pinctrl-rza-common_8h.md#a9398ade50c886958f0b51b41a9c4849b)#define BSP\_IO\_SD0\_DATA4 0xFFFF0704 /\* SD0\_DATA4 \*/

[ 58](pinctrl-rza-common_8h.md#ae127f16b4b223229c57375a20ad2a442)#define BSP\_IO\_SD0\_DATA5 0xFFFF0705 /\* SD0\_DATA5 \*/

[ 59](pinctrl-rza-common_8h.md#af64543688eccd90de6b9086ccd72e3fd)#define BSP\_IO\_SD0\_DATA6 0xFFFF0706 /\* SD0\_DATA6 \*/

[ 60](pinctrl-rza-common_8h.md#a1e39def829ae82ed38ddbd0f01d9b62f)#define BSP\_IO\_SD0\_DATA7 0xFFFF0707 /\* SD0\_DATA7 \*/

61

[ 62](pinctrl-rza-common_8h.md#a21e34df07c258c73258ba42eeab62fee)#define BSP\_IO\_SD1\_CLK 0xFFFF0800 /\* SD1\_CLK \*/

[ 63](pinctrl-rza-common_8h.md#a03e82210e0063b35e7e3a877a6dbd17e)#define BSP\_IO\_SD1\_CMD 0xFFFF0801 /\* SD1\_CMD \*/

64

[ 65](pinctrl-rza-common_8h.md#a8e6b818ecfdfbd9c8c571720711d35dd)#define BSP\_IO\_SD1\_DATA0 0xFFFF0900 /\* SD1\_DATA0 \*/

[ 66](pinctrl-rza-common_8h.md#a222474e671dc0196e027b741bfb6bef2)#define BSP\_IO\_SD1\_DATA1 0xFFFF0901 /\* SD1\_DATA1 \*/

[ 67](pinctrl-rza-common_8h.md#ab404c31fb4de4e9c80ffd9cd3d93b7ca)#define BSP\_IO\_SD1\_DATA2 0xFFFF0902 /\* SD1\_DATA2 \*/

[ 68](pinctrl-rza-common_8h.md#acb12cf7cf433e72dd141c6652be9d9af)#define BSP\_IO\_SD1\_DATA3 0xFFFF0903 /\* SD1\_DATA3 \*/

69

[ 70](pinctrl-rza-common_8h.md#aaa8265b3c46500752b85644e535692a2)#define BSP\_IO\_QSPI0\_SPCLK 0xFFFF0A00 /\* QSPI0\_SPCLK \*/

[ 71](pinctrl-rza-common_8h.md#acb67188a7f35bc9af5ff4a9f3630842e)#define BSP\_IO\_QSPI0\_IO0 0xFFFF0A01 /\* QSPI0\_IO0 \*/

[ 72](pinctrl-rza-common_8h.md#a01f1b79e7f366a6a8ad84e5ec37b4158)#define BSP\_IO\_QSPI0\_IO1 0xFFFF0A02 /\* QSPI0\_IO1 \*/

[ 73](pinctrl-rza-common_8h.md#a98e28074dd38b49185c7dca7d7903b1d)#define BSP\_IO\_QSPI0\_IO2 0xFFFF0A03 /\* QSPI0\_IO2 \*/

[ 74](pinctrl-rza-common_8h.md#a12283abd104711dbb9cc2bfe406f0703)#define BSP\_IO\_QSPI0\_IO3 0xFFFF0A04 /\* QSPI0\_IO3 \*/

[ 75](pinctrl-rza-common_8h.md#acd80bf931fcadaebf996edb2bf76e9e3)#define BSP\_IO\_QSPI0\_SSL 0xFFFF0A05 /\* QSPI0\_SSL \*/

76

[ 77](pinctrl-rza-common_8h.md#a87a74fe5e54dba6dbd6f454ae1f7e2d8)#define BSP\_IO\_OM\_CS1\_N 0xFFFF0B00 /\* OM\_CS1\_N \*/

[ 78](pinctrl-rza-common_8h.md#ac7bf1cf7d1da17c05ef2fe2e1c34de4f)#define BSP\_IO\_OM\_DQS 0xFFFF0B01 /\* OM\_DQS \*/

[ 79](pinctrl-rza-common_8h.md#ab788db0c971af9be7fe2c7c08b1168b0)#define BSP\_IO\_OM\_SIO4 0xFFFF0B02 /\* OM\_SIO4 \*/

[ 80](pinctrl-rza-common_8h.md#a516b19addd1e2efa9377aea01b005dcb)#define BSP\_IO\_OM\_SIO5 0xFFFF0B03 /\* OM\_SIO5 \*/

[ 81](pinctrl-rza-common_8h.md#a3758f58970281eb6ae17fb4ed216e787)#define BSP\_IO\_OM\_SIO6 0xFFFF0B04 /\* OM\_SIO6 \*/

[ 82](pinctrl-rza-common_8h.md#ac51dbcdecce7d39a8d2e81f6100e9370)#define BSP\_IO\_OM\_SIO7 0xFFFF0B05 /\* OM\_SIO7 \*/

83

[ 84](pinctrl-rza-common_8h.md#ab6a44158744e5cad8124f4da291159dc)#define BSP\_IO\_QSPI\_RESET\_N 0xFFFF0C00 /\* QSPI\_RESET\_N \*/

[ 85](pinctrl-rza-common_8h.md#abf8e87c6fdcd8241324c66b443668251)#define BSP\_IO\_QSPI\_WP\_N 0xFFFF0C01 /\* QSPI\_WP\_N \*/

86

[ 87](pinctrl-rza-common_8h.md#ad2e37f140ebdb92bb4ee94f6a8032737)#define BSP\_IO\_WDTOVF\_PERROUT\_N 0xFFFF0D00 /\* WDTOVF\_PERROUT\_N \*/

88

[ 89](pinctrl-rza-common_8h.md#abf5f96c4d40bddcef43d534d7ea6fdaa)#define BSP\_IO\_RIIC0\_SDA 0xFFFF0E00 /\* RIIC0\_SDA \*/

[ 90](pinctrl-rza-common_8h.md#a20256eab52e96328dab53ff66037d35b)#define BSP\_IO\_RIIC0\_SCL 0xFFFF0E01 /\* RIIC0\_SCL \*/

[ 91](pinctrl-rza-common_8h.md#adc37073529eb331cf8cc80185abf5f92)#define BSP\_IO\_RIIC1\_SDA 0xFFFF0E02 /\* RIIC1\_SDA \*/

[ 92](pinctrl-rza-common_8h.md#ae1c7843f96e83c7aebb77512036aa20c)#define BSP\_IO\_RIIC1\_SCL 0xFFFF0E03 /\* RIIC1\_SCL \*/

93

94/\* FILNUM \*/

[ 95](pinctrl-rza-common_8h.md#ae2fb4f96b6b50ad80a433780e422db2f)#define RZA\_FILNUM\_4\_STAGE 0

[ 96](pinctrl-rza-common_8h.md#a9e4ed308e81c23c7d70a70f3708b3392)#define RZA\_FILNUM\_8\_STAGE 1

[ 97](pinctrl-rza-common_8h.md#a6d57d4270438ff5b6cc72111e6d03562)#define RZA\_FILNUM\_12\_STAGE 2

[ 98](pinctrl-rza-common_8h.md#a9a82059d12af7f931f051a304113735e)#define RZA\_FILNUM\_16\_STAGE 3

99

100/\* FILCLKSEL \*/

[ 101](pinctrl-rza-common_8h.md#ab5bb0119588fa51a96489d03a62c4b83)#define RZA\_FILCLKSEL\_NOT\_DIV 0

[ 102](pinctrl-rza-common_8h.md#a6d987d1bb9a03f28abf5980f0a45ceb4)#define RZA\_FILCLKSEL\_DIV\_9000 1

[ 103](pinctrl-rza-common_8h.md#a9fe6a4f870d9260c13f055245b3d22cb)#define RZA\_FILCLKSEL\_DIV\_18000 2

[ 104](pinctrl-rza-common_8h.md#a24aeabb3038f110c9d4a76df150987ef)#define RZA\_FILCLKSEL\_DIV\_36000 3

105

[ 106](pinctrl-rza-common_8h.md#acb3f592d302bb7ee67914ade80a3fb44)#define RZA\_FILTER\_SET(filnum, filclksel) (((filnum) & 0x3) << 0x2) | (filclksel & 0x3)

107

108#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_PINCTRL\_RENESAS\_PINCTRL\_RZA\_COMMON\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [pinctrl](dir_2c6c4fbd167577104b7f1b7148586168.md)
- [renesas](dir_17f48eb154be6cea623223db5de209e7.md)
- [pinctrl-rza-common.h](pinctrl-rza-common_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
