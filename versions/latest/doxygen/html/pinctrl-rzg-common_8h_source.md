---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/pinctrl-rzg-common_8h_source.html
original_path: doxygen/html/pinctrl-rzg-common_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

pinctrl-rzg-common.h

[Go to the documentation of this file.](pinctrl-rzg-common_8h.md)

1/\*

2 \* Copyright (c) 2024 Renesas Electronics Corporation

3 \* SPDX-License-Identifier: Apache-2.0

4 \*/

5

6#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_PINCTRL\_RENESAS\_PINCTRL\_RZG\_COMMON\_H\_

7#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_PINCTRL\_RENESAS\_PINCTRL\_RZG\_COMMON\_H\_

8

9/\* Superset list of all possible IO ports. \*/

[ 10](pinctrl-rzg-common_8h.md#a1b0292747e92dff43d6760d9e2258869)#define PORT\_00 0x0000 /\* IO port 0 \*/

[ 11](pinctrl-rzg-common_8h.md#a9de415830a2b3484dd33d5d08258dde5)#define PORT\_01 0x1000 /\* IO port 1 \*/

[ 12](pinctrl-rzg-common_8h.md#a7db623b2ec3816113a8f3fb07d5428ef)#define PORT\_02 0x1100 /\* IO port 2 \*/

[ 13](pinctrl-rzg-common_8h.md#a71478a4563d986886410618bc130b0d9)#define PORT\_03 0x1200 /\* IO port 3 \*/

[ 14](pinctrl-rzg-common_8h.md#aed73b97fc12615ac1dec9daad9537647)#define PORT\_04 0x1300 /\* IO port 4 \*/

[ 15](pinctrl-rzg-common_8h.md#a590020a2e6577d74d89bdee0989812c4)#define PORT\_05 0x0100 /\* IO port 5 \*/

[ 16](pinctrl-rzg-common_8h.md#ab2912aeb54c92971e0590ff3282e775b)#define PORT\_06 0x0200 /\* IO port 6 \*/

[ 17](pinctrl-rzg-common_8h.md#acabb0398db58703c47e718f899018410)#define PORT\_07 0x1400 /\* IO port 7 \*/

[ 18](pinctrl-rzg-common_8h.md#a5f4d0cfbea4e649fa0863d4a8d409c5e)#define PORT\_08 0x1500 /\* IO port 8 \*/

[ 19](pinctrl-rzg-common_8h.md#a5e8d840d1a1bd421615b2cc90ce0b90f)#define PORT\_09 0x1600 /\* IO port 9 \*/

[ 20](pinctrl-rzg-common_8h.md#a4c39a294d7b3a360c172b65151a5bfc8)#define PORT\_10 0x1700 /\* IO port 10 \*/

[ 21](pinctrl-rzg-common_8h.md#abeebf6334cb5240b09d97d35fc0128f3)#define PORT\_11 0x0300 /\* IO port 11 \*/

[ 22](pinctrl-rzg-common_8h.md#ae57c3ffa4df15481a9a219e16b011ef3)#define PORT\_12 0x0400 /\* IO port 12 \*/

[ 23](pinctrl-rzg-common_8h.md#ae76dfcae2263b7d43d1ee23fa9548293)#define PORT\_13 0x0500 /\* IO port 13 \*/

[ 24](pinctrl-rzg-common_8h.md#a9c8783d66b07c093c559a5fd74add129)#define PORT\_14 0x0600 /\* IO port 14 \*/

[ 25](pinctrl-rzg-common_8h.md#aeb88886b16b5a8ea23147000fd9af3cc)#define PORT\_15 0x0700 /\* IO port 15 \*/

[ 26](pinctrl-rzg-common_8h.md#aa9fff44f99e434f31b19ed55462b45d4)#define PORT\_16 0x0800 /\* IO port 16 \*/

[ 27](pinctrl-rzg-common_8h.md#a8ce8fd8ca6cdbc375b70a0b7d53eb315)#define PORT\_17 0x0900 /\* IO port 17 \*/

[ 28](pinctrl-rzg-common_8h.md#a51b6b92e7f3238a410526b67234f77d7)#define PORT\_18 0x0A00 /\* IO port 18 \*/

29

30/\*

31 \* Create the value contain port/pin/function information

32 \*

33 \* port: port number BSP\_IO\_PORT\_00..BSP\_IO\_PORT\_18

34 \* pin: pin number

35 \* func: pin function

36 \*/

[ 37](pinctrl-rzg-common_8h.md#a02f280ee325bc9e66e5566f8d6f3feec)#define RZG\_PINMUX(port, pin, func) (port | pin | (func << 4))

38

39/\* Special purpose port \*/

[ 40](pinctrl-rzg-common_8h.md#a5a8b4d2cdc15f25cc0b58db97c539b2a)#define BSP\_IO\_NMI 0xFFFF0000 /\* NMI \*/

41

[ 42](pinctrl-rzg-common_8h.md#af06a8358900119f6b4c3d91e465ce22f)#define BSP\_IO\_TMS\_SWDIO 0xFFFF0100 /\* TMS\_SWDIO \*/

[ 43](pinctrl-rzg-common_8h.md#a318b423b2efc8ab1a3de0a8f9ab3eeca)#define BSP\_IO\_TDO 0xFFFF0101 /\* TDO \*/

44

[ 45](pinctrl-rzg-common_8h.md#acf9b257ce3e3a66bcfa8d4aca427c0bf)#define BSP\_IO\_AUDIO\_CLK1 0xFFFF0200 /\* AUDIO\_CLK1 \*/

[ 46](pinctrl-rzg-common_8h.md#a98d349e2311d1571d490e26866871b16)#define BSP\_IO\_AUDIO\_CLK2 0xFFFF0201 /\* AUDIO\_CLK2 \*/

47

[ 48](pinctrl-rzg-common_8h.md#ae349e2b4add4664859e2c87e7eb47e15)#define BSP\_IO\_XSPI\_SPCLK 0xFFFF0400 /\* XSPI\_SPCLK \*/

[ 49](pinctrl-rzg-common_8h.md#a1938aca3788d42e557a35c20517f9dd8)#define BSP\_IO\_XSPI\_RESET\_N 0xFFFF0401 /\* XSPI\_RESET\_N \*/

[ 50](pinctrl-rzg-common_8h.md#a73759a3f08a6b48278607de2f63cf523)#define BSP\_IO\_XSPI\_WP\_N 0xFFFF0402 /\* XSPI\_WP\_N \*/

[ 51](pinctrl-rzg-common_8h.md#a019fd571a275deaf0570c317b9a20b97)#define BSP\_IO\_XSPI\_DS 0xFFFF0403 /\* XSPI\_DS \*/

[ 52](pinctrl-rzg-common_8h.md#a2356e340dbc38e7d62351b8996b40c1e)#define BSP\_IO\_XSPI\_CS0\_N 0xFFFF0404 /\* XSPI\_CS0\_N \*/

[ 53](pinctrl-rzg-common_8h.md#a973dd3ba73dbb9b3c93d3f715c4dd6c0)#define BSP\_IO\_XSPI\_CS1\_N 0xFFFF0405 /\* XSPI\_CS1\_N \*/

54

[ 55](pinctrl-rzg-common_8h.md#a19da009b51eb3891a92ef39c13019567)#define BSP\_IO\_XSPI\_IO0 0xFFFF0500 /\* XSPI\_IO0 \*/

[ 56](pinctrl-rzg-common_8h.md#a3ea0b2836c786211aa5643b7bce971c2)#define BSP\_IO\_XSPI\_IO1 0xFFFF0501 /\* XSPI\_IO1 \*/

[ 57](pinctrl-rzg-common_8h.md#af0814f9594ef180d9dbb3e910118cb39)#define BSP\_IO\_XSPI\_IO2 0xFFFF0502 /\* XSPI\_IO2 \*/

[ 58](pinctrl-rzg-common_8h.md#ae39cf1fdec8f1940030b962fd91895ec)#define BSP\_IO\_XSPI\_IO3 0xFFFF0503 /\* XSPI\_IO3 \*/

[ 59](pinctrl-rzg-common_8h.md#ade455522c2e4df9f6a3d4335898c5a2e)#define BSP\_IO\_XSPI\_IO4 0xFFFF0504 /\* XSPI\_IO4 \*/

[ 60](pinctrl-rzg-common_8h.md#afd88724051491fb938adc876ce9f8094)#define BSP\_IO\_XSPI\_IO5 0xFFFF0505 /\* XSPI\_IO5 \*/

[ 61](pinctrl-rzg-common_8h.md#ae4047cb2b38a2388ac3ad4a73b438348)#define BSP\_IO\_XSPI\_IO6 0xFFFF0506 /\* XSPI\_IO6 \*/

[ 62](pinctrl-rzg-common_8h.md#a0839e73ff018a83849befdf6c1fa9cbf)#define BSP\_IO\_XSPI\_IO7 0xFFFF0507 /\* XSPI\_IO7 \*/

63

[ 64](pinctrl-rzg-common_8h.md#a7c1efa402066677442bffceaa874e002)#define BSP\_IO\_WDTOVF\_PERROUT 0xFFFF0600 /\* WDTOVF\_PERROUT \*/

65

[ 66](pinctrl-rzg-common_8h.md#a7ef3de361b4eaab1e199ac28454233cd)#define BSP\_IO\_I3C\_SDA 0xFFFF0900 /\* I3C\_SDA \*/

[ 67](pinctrl-rzg-common_8h.md#a67faf3a17f6e0d6fc75671829942072d)#define BSP\_IO\_I3C\_SCL 0xFFFF0901 /\* I3C\_SCL \*/

68

[ 69](pinctrl-rzg-common_8h.md#a99cac86447ae6b18e3e1601085623a60)#define BSP\_IO\_SD0\_CLK 0xFFFF1000 /\* CD0\_CLK \*/

[ 70](pinctrl-rzg-common_8h.md#a2b904f716e2bf524351430155b8c7ddc)#define BSP\_IO\_SD0\_CMD 0xFFFF1001 /\* CD0\_CMD \*/

[ 71](pinctrl-rzg-common_8h.md#ad61d120b88812e3c41a600414f553325)#define BSP\_IO\_SD0\_RST\_N 0xFFFF1002 /\* CD0\_RST\_N \*/

72

[ 73](pinctrl-rzg-common_8h.md#a1f4951bb275e24732e8487dffd5fe69a)#define BSP\_IO\_SD0\_DATA0 0xFFFF1100 /\* SD0\_DATA0 \*/

[ 74](pinctrl-rzg-common_8h.md#a97428f756c92136fd0f3d34f520c760b)#define BSP\_IO\_SD0\_DATA1 0xFFFF1101 /\* SD0\_DATA1 \*/

[ 75](pinctrl-rzg-common_8h.md#a77fab2fb18ce2a3d779d94b54e8d58d1)#define BSP\_IO\_SD0\_DATA2 0xFFFF1102 /\* SD0\_DATA2 \*/

[ 76](pinctrl-rzg-common_8h.md#a8794e04fe7b7d3d895973cac59538095)#define BSP\_IO\_SD0\_DATA3 0xFFFF1103 /\* SD0\_DATA3 \*/

[ 77](pinctrl-rzg-common_8h.md#a9398ade50c886958f0b51b41a9c4849b)#define BSP\_IO\_SD0\_DATA4 0xFFFF1104 /\* SD0\_DATA4 \*/

[ 78](pinctrl-rzg-common_8h.md#ae127f16b4b223229c57375a20ad2a442)#define BSP\_IO\_SD0\_DATA5 0xFFFF1105 /\* SD0\_DATA5 \*/

[ 79](pinctrl-rzg-common_8h.md#af64543688eccd90de6b9086ccd72e3fd)#define BSP\_IO\_SD0\_DATA6 0xFFFF1106 /\* SD0\_DATA6 \*/

[ 80](pinctrl-rzg-common_8h.md#a1e39def829ae82ed38ddbd0f01d9b62f)#define BSP\_IO\_SD0\_DATA7 0xFFFF1107 /\* SD0\_DATA7 \*/

81

[ 82](pinctrl-rzg-common_8h.md#a21e34df07c258c73258ba42eeab62fee)#define BSP\_IO\_SD1\_CLK 0xFFFF1200 /\* SD1\_CLK \*/

[ 83](pinctrl-rzg-common_8h.md#a03e82210e0063b35e7e3a877a6dbd17e)#define BSP\_IO\_SD1\_CMD 0xFFFF1201 /\* SD1\_CMD \*/

84

[ 85](pinctrl-rzg-common_8h.md#a8e6b818ecfdfbd9c8c571720711d35dd)#define BSP\_IO\_SD1\_DATA0 0xFFFF1300 /\* SD1\_DATA0 \*/

[ 86](pinctrl-rzg-common_8h.md#a222474e671dc0196e027b741bfb6bef2)#define BSP\_IO\_SD1\_DATA1 0xFFFF1301 /\* SD1\_DATA1 \*/

[ 87](pinctrl-rzg-common_8h.md#ab404c31fb4de4e9c80ffd9cd3d93b7ca)#define BSP\_IO\_SD1\_DATA2 0xFFFF1302 /\* SD1\_DATA2 \*/

[ 88](pinctrl-rzg-common_8h.md#acb12cf7cf433e72dd141c6652be9d9af)#define BSP\_IO\_SD1\_DATA3 0xFFFF1303 /\* SD1\_DATA3 \*/

89

90/\*FILNUM\*/

[ 91](pinctrl-rzg-common_8h.md#a410e1db2102a72b3222f3f87e9191b36)#define RZG\_FILNUM\_4\_STAGE 0

[ 92](pinctrl-rzg-common_8h.md#a7ec85695dd35462b15784cf869e2ecdd)#define RZG\_FILNUM\_8\_STAGE 1

[ 93](pinctrl-rzg-common_8h.md#a7fb5e17c2033f7de03440445de58497d)#define RZG\_FILNUM\_12\_STAGE 2

[ 94](pinctrl-rzg-common_8h.md#a4c3d0f96e45fcff456391291544c2d7e)#define RZG\_FILNUM\_16\_STAGE 3

95

96/\*FILCLKSEL\*/

[ 97](pinctrl-rzg-common_8h.md#aebf11f5c29f9d62a4bc6076430f5af74)#define RZG\_FILCLKSEL\_NOT\_DIV 0

[ 98](pinctrl-rzg-common_8h.md#a6fc19ace82becb78720423edd9a80f03)#define RZG\_FILCLKSEL\_DIV\_9000 1

[ 99](pinctrl-rzg-common_8h.md#a82fe6b7f1ba59ab812683890fa2f0e7c)#define RZG\_FILCLKSEL\_DIV\_18000 2

[ 100](pinctrl-rzg-common_8h.md#acecffc879cdcd14232b7cc2714e46e8f)#define RZG\_FILCLKSEL\_DIV\_36000 3

101

[ 102](pinctrl-rzg-common_8h.md#abe4747778068dd33b142d7a891ca901e)#define RZG\_FILTER\_SET(filnum, filclksel) (((filnum) & 0x3) << 0x2) | (filclksel & 0x3)

103

104#endif /\*ZEPHYR\_INCLUDE\_DT\_BINDINGS\_PINCTRL\_RENESAS\_PINCTRL\_RZG\_COMMON\_H\_\*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [pinctrl](dir_2c6c4fbd167577104b7f1b7148586168.md)
- [renesas](dir_17f48eb154be6cea623223db5de209e7.md)
- [pinctrl-rzg-common.h](pinctrl-rzg-common_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
