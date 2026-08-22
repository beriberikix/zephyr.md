---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/pinctrl-rzv-common_8h_source.html
original_path: doxygen/html/pinctrl-rzv-common_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

pinctrl-rzv-common.h

[Go to the documentation of this file.](pinctrl-rzv-common_8h.md)

1/\*

2 \* Copyright (c) 2025 Renesas Electronics Corporation

3 \* SPDX-License-Identifier: Apache-2.0

4 \*/

5

6#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_PINCTRL\_RENESAS\_PINCTRL\_RZV\_COMMON\_H\_

7#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_PINCTRL\_RENESAS\_PINCTRL\_RZV\_COMMON\_H\_

8

9/\* Superset list of all possible IO ports. \*/

[ 10](pinctrl-rzv-common_8h.md#a1b0292747e92dff43d6760d9e2258869)#define PORT\_00 0x0000 /\* IO port 0 \*/

[ 11](pinctrl-rzv-common_8h.md#a9de415830a2b3484dd33d5d08258dde5)#define PORT\_01 0x0100 /\* IO port 1 \*/

[ 12](pinctrl-rzv-common_8h.md#a7db623b2ec3816113a8f3fb07d5428ef)#define PORT\_02 0x0200 /\* IO port 2 \*/

[ 13](pinctrl-rzv-common_8h.md#a71478a4563d986886410618bc130b0d9)#define PORT\_03 0x0300 /\* IO port 3 \*/

[ 14](pinctrl-rzv-common_8h.md#aed73b97fc12615ac1dec9daad9537647)#define PORT\_04 0x0400 /\* IO port 4 \*/

[ 15](pinctrl-rzv-common_8h.md#a590020a2e6577d74d89bdee0989812c4)#define PORT\_05 0x0500 /\* IO port 5 \*/

[ 16](pinctrl-rzv-common_8h.md#ab2912aeb54c92971e0590ff3282e775b)#define PORT\_06 0x0600 /\* IO port 6 \*/

[ 17](pinctrl-rzv-common_8h.md#acabb0398db58703c47e718f899018410)#define PORT\_07 0x0700 /\* IO port 7 \*/

[ 18](pinctrl-rzv-common_8h.md#a5f4d0cfbea4e649fa0863d4a8d409c5e)#define PORT\_08 0x0800 /\* IO port 8 \*/

[ 19](pinctrl-rzv-common_8h.md#a5e8d840d1a1bd421615b2cc90ce0b90f)#define PORT\_09 0x0900 /\* IO port 9 \*/

[ 20](pinctrl-rzv-common_8h.md#a4c39a294d7b3a360c172b65151a5bfc8)#define PORT\_10 0x0A00 /\* IO port 10 \*/

[ 21](pinctrl-rzv-common_8h.md#abeebf6334cb5240b09d97d35fc0128f3)#define PORT\_11 0x0B00 /\* IO port 11 \*/

[ 22](pinctrl-rzv-common_8h.md#ae57c3ffa4df15481a9a219e16b011ef3)#define PORT\_12 0x0C00 /\* IO port 12 \*/

[ 23](pinctrl-rzv-common_8h.md#ae76dfcae2263b7d43d1ee23fa9548293)#define PORT\_13 0x0D00 /\* IO port 13 \*/

[ 24](pinctrl-rzv-common_8h.md#a9c8783d66b07c093c559a5fd74add129)#define PORT\_14 0x0E00 /\* IO port 14 \*/

[ 25](pinctrl-rzv-common_8h.md#aeb88886b16b5a8ea23147000fd9af3cc)#define PORT\_15 0x0F00 /\* IO port 15 \*/

[ 26](pinctrl-rzv-common_8h.md#aa9fff44f99e434f31b19ed55462b45d4)#define PORT\_16 0x1000 /\* IO port 16 \*/

[ 27](pinctrl-rzv-common_8h.md#a8ce8fd8ca6cdbc375b70a0b7d53eb315)#define PORT\_17 0x1100 /\* IO port 17 \*/

[ 28](pinctrl-rzv-common_8h.md#a51b6b92e7f3238a410526b67234f77d7)#define PORT\_18 0x1200 /\* IO port 18 \*/

[ 29](pinctrl-rzv-common_8h.md#a0c1b97684b0bbb0326a187117bcf78ae)#define PORT\_19 0x1300 /\* IO port 19 \*/

[ 30](pinctrl-rzv-common_8h.md#a87d7fd3777b47baab0317a96ee874842)#define PORT\_20 0x1400 /\* IO port 20 \*/

[ 31](pinctrl-rzv-common_8h.md#acc227be3abe2efbeed63891d0e4ad3db)#define PORT\_21 0x1500 /\* IO port 21 \*/

[ 32](pinctrl-rzv-common_8h.md#aefb67b06965dd6320a246fc0529917ad)#define PORT\_22 0x1600 /\* IO port 22 \*/

[ 33](pinctrl-rzv-common_8h.md#a1d7f17a633496267b4d19fc8fa89dbb5)#define PORT\_23 0x1700 /\* IO port 23 \*/

[ 34](pinctrl-rzv-common_8h.md#affbf09e2b0a16edd6b6201909ee99394)#define PORT\_24 0x1800 /\* IO port 24 \*/

[ 35](pinctrl-rzv-common_8h.md#a8294aaccee0f492317c516e0650aa3ae)#define PORT\_25 0x1900 /\* IO port 25 \*/

[ 36](pinctrl-rzv-common_8h.md#ae05ca0fe949f27b5a7fb9ab591236eb5)#define PORT\_26 0x1A00 /\* IO port 26 \*/

[ 37](pinctrl-rzv-common_8h.md#a75bd2e1d9ec1ca727e1bff3089817a0f)#define PORT\_27 0x1B00 /\* IO port 27 \*/

[ 38](pinctrl-rzv-common_8h.md#aa57eff6bf891ecc8486ebcd1213291a7)#define PORT\_28 0x1C00 /\* IO port 28 \*/

[ 39](pinctrl-rzv-common_8h.md#a657ec3a12bd94f98baf3b7f7636e335b)#define PORT\_29 0x1D00 /\* IO port 29 \*/

[ 40](pinctrl-rzv-common_8h.md#a5d994c54f5e3a93a713eb1af0c775dda)#define PORT\_30 0x1E00 /\* IO port 30 \*/

[ 41](pinctrl-rzv-common_8h.md#a634e9ea57181bc83b3be1c2473e8df13)#define PORT\_31 0x1F00 /\* IO port 31 \*/

[ 42](pinctrl-rzv-common_8h.md#af0e97abbfe0607d2bbd6b0bf9ddbc0ef)#define PORT\_32 0x2000 /\* IO port 32 \*/

[ 43](pinctrl-rzv-common_8h.md#a424a163455e7b6cc0faca5d3ca7f00f4)#define PORT\_33 0x2100 /\* IO port 33 \*/

[ 44](pinctrl-rzv-common_8h.md#ac1b44b6dee31ebd6b8ac5bad56446a02)#define PORT\_34 0x2200 /\* IO port 34 \*/

[ 45](pinctrl-rzv-common_8h.md#a78c202a4d3882450b41d1c60df530658)#define PORT\_35 0x2300 /\* IO port 35 \*/

[ 46](pinctrl-rzv-common_8h.md#a47eb175dba955fec4cbf79a9b0efa973)#define PORT\_36 0x2400 /\* IO port 36 \*/

[ 47](pinctrl-rzv-common_8h.md#a5a3debc2962b08963f39c38d2be12ae6)#define PORT\_37 0x2500 /\* IO port 37 \*/

[ 48](pinctrl-rzv-common_8h.md#ac6c0f7e21c278e0c099d59998a2bdcb8)#define PORT\_38 0x2600 /\* IO port 38 \*/

[ 49](pinctrl-rzv-common_8h.md#a9ff2297ec7bd05f237457c42e48f7004)#define PORT\_39 0x2700 /\* IO port 39 \*/

[ 50](pinctrl-rzv-common_8h.md#a8186d359fb55d84806c1b85a2fad74c1)#define PORT\_40 0x2800 /\* IO port 40 \*/

[ 51](pinctrl-rzv-common_8h.md#a4cc4764d4ec08a7307b6c2cd9e3d3349)#define PORT\_41 0x2900 /\* IO port 41 \*/

[ 52](pinctrl-rzv-common_8h.md#ad653c357ac0b8df98e078c404be7c9b0)#define PORT\_42 0x2A00 /\* IO port 42 \*/

[ 53](pinctrl-rzv-common_8h.md#aa4e56f114bdcde46fe218174e28d2fe6)#define PORT\_43 0x2B00 /\* IO port 43 \*/

[ 54](pinctrl-rzv-common_8h.md#a743edbe771261c90cec0bf967df1cf7a)#define PORT\_44 0x2C00 /\* IO port 44 \*/

[ 55](pinctrl-rzv-common_8h.md#a8fbd69bd13ac505784fc35dcd30e5ed0)#define PORT\_45 0x2D00 /\* IO port 45 \*/

[ 56](pinctrl-rzv-common_8h.md#a556d96f490fe864f3c01b0518299561f)#define PORT\_46 0x2E00 /\* IO port 46 \*/

[ 57](pinctrl-rzv-common_8h.md#aba995dc5260ba8341ac90de822901f99)#define PORT\_47 0x2F00 /\* IO port 47 \*/

[ 58](pinctrl-rzv-common_8h.md#ac81eae40ea61b31e1bfcdac2bcede298)#define PORT\_48 0x3000 /\* IO port 48 \*/

59

60/\*

61 \* Create the value contain port/pin/function information

62 \*

63 \* port: port number BSP\_IO\_PORT\_00..BSP\_IO\_PORT\_48

64 \* pin: pin number

65 \* func: pin function

66 \*/

[ 67](pinctrl-rzv-common_8h.md#ace27a9fee40fcee657b3aff941b3ac6b)#define RZV\_PINMUX(port, pin, func) (port | pin | (func << 4))

68

69/\* Special purpose port \*/

[ 70](pinctrl-rzv-common_8h.md#a5a8b4d2cdc15f25cc0b58db97c539b2a)#define BSP\_IO\_NMI 0xFFFF0100 /\* NMI \*/

71

[ 72](pinctrl-rzv-common_8h.md#af06a8358900119f6b4c3d91e465ce22f)#define BSP\_IO\_TMS\_SWDIO 0xFFFF0200 /\* TMS\_SWDIO \*/

73

[ 74](pinctrl-rzv-common_8h.md#a318b423b2efc8ab1a3de0a8f9ab3eeca)#define BSP\_IO\_TDO 0xFFFF0300 /\* TDO \*/

75

[ 76](pinctrl-rzv-common_8h.md#acf9b257ce3e3a66bcfa8d4aca427c0bf)#define BSP\_IO\_AUDIO\_CLK1 0xFFFF0400 /\* AUDIO\_CLK1 \*/

[ 77](pinctrl-rzv-common_8h.md#a98d349e2311d1571d490e26866871b16)#define BSP\_IO\_AUDIO\_CLK2 0xFFFF0401 /\* AUDIO\_CLK2 \*/

78

[ 79](pinctrl-rzv-common_8h.md#a99cac86447ae6b18e3e1601085623a60)#define BSP\_IO\_SD0\_CLK 0xFFFF0600 /\* SD0\_CLK \*/

[ 80](pinctrl-rzv-common_8h.md#a2b904f716e2bf524351430155b8c7ddc)#define BSP\_IO\_SD0\_CMD 0xFFFF0601 /\* SD0\_CMD \*/

[ 81](pinctrl-rzv-common_8h.md#ad61d120b88812e3c41a600414f553325)#define BSP\_IO\_SD0\_RST\_N 0xFFFF0602 /\* SD0\_RST\_N \*/

82

[ 83](pinctrl-rzv-common_8h.md#a1f4951bb275e24732e8487dffd5fe69a)#define BSP\_IO\_SD0\_DATA0 0xFFFF0700 /\* SD0\_DATA0 \*/

[ 84](pinctrl-rzv-common_8h.md#a97428f756c92136fd0f3d34f520c760b)#define BSP\_IO\_SD0\_DATA1 0xFFFF0701 /\* SD0\_DATA1 \*/

[ 85](pinctrl-rzv-common_8h.md#a77fab2fb18ce2a3d779d94b54e8d58d1)#define BSP\_IO\_SD0\_DATA2 0xFFFF0702 /\* SD0\_DATA2 \*/

[ 86](pinctrl-rzv-common_8h.md#a8794e04fe7b7d3d895973cac59538095)#define BSP\_IO\_SD0\_DATA3 0xFFFF0703 /\* SD0\_DATA3 \*/

[ 87](pinctrl-rzv-common_8h.md#a9398ade50c886958f0b51b41a9c4849b)#define BSP\_IO\_SD0\_DATA4 0xFFFF0704 /\* SD0\_DATA4 \*/

[ 88](pinctrl-rzv-common_8h.md#ae127f16b4b223229c57375a20ad2a442)#define BSP\_IO\_SD0\_DATA5 0xFFFF0705 /\* SD0\_DATA5 \*/

[ 89](pinctrl-rzv-common_8h.md#af64543688eccd90de6b9086ccd72e3fd)#define BSP\_IO\_SD0\_DATA6 0xFFFF0706 /\* SD0\_DATA6 \*/

[ 90](pinctrl-rzv-common_8h.md#a1e39def829ae82ed38ddbd0f01d9b62f)#define BSP\_IO\_SD0\_DATA7 0xFFFF0707 /\* SD0\_DATA7 \*/

91

[ 92](pinctrl-rzv-common_8h.md#a21e34df07c258c73258ba42eeab62fee)#define BSP\_IO\_SD1\_CLK 0xFFFF0800 /\* SD1\_CLK \*/

[ 93](pinctrl-rzv-common_8h.md#a03e82210e0063b35e7e3a877a6dbd17e)#define BSP\_IO\_SD1\_CMD 0xFFFF0801 /\* SD1\_CMD \*/

94

[ 95](pinctrl-rzv-common_8h.md#a8e6b818ecfdfbd9c8c571720711d35dd)#define BSP\_IO\_SD1\_DATA0 0xFFFF0900 /\* SD1\_DATA0 \*/

[ 96](pinctrl-rzv-common_8h.md#a222474e671dc0196e027b741bfb6bef2)#define BSP\_IO\_SD1\_DATA1 0xFFFF0901 /\* SD1\_DATA1 \*/

[ 97](pinctrl-rzv-common_8h.md#ab404c31fb4de4e9c80ffd9cd3d93b7ca)#define BSP\_IO\_SD1\_DATA2 0xFFFF0902 /\* SD1\_DATA2 \*/

[ 98](pinctrl-rzv-common_8h.md#acb12cf7cf433e72dd141c6652be9d9af)#define BSP\_IO\_SD1\_DATA3 0xFFFF0903 /\* SD1\_DATA3 \*/

99

[ 100](pinctrl-rzv-common_8h.md#aaa8265b3c46500752b85644e535692a2)#define BSP\_IO\_QSPI0\_SPCLK 0xFFFF0A00 /\* QSPI0\_SPCLK \*/

[ 101](pinctrl-rzv-common_8h.md#acb67188a7f35bc9af5ff4a9f3630842e)#define BSP\_IO\_QSPI0\_IO0 0xFFFF0A01 /\* QSPI0\_IO0 \*/

[ 102](pinctrl-rzv-common_8h.md#a01f1b79e7f366a6a8ad84e5ec37b4158)#define BSP\_IO\_QSPI0\_IO1 0xFFFF0A02 /\* QSPI0\_IO1 \*/

[ 103](pinctrl-rzv-common_8h.md#a98e28074dd38b49185c7dca7d7903b1d)#define BSP\_IO\_QSPI0\_IO2 0xFFFF0A03 /\* QSPI0\_IO2 \*/

[ 104](pinctrl-rzv-common_8h.md#a12283abd104711dbb9cc2bfe406f0703)#define BSP\_IO\_QSPI0\_IO3 0xFFFF0A04 /\* QSPI0\_IO3 \*/

[ 105](pinctrl-rzv-common_8h.md#acd80bf931fcadaebf996edb2bf76e9e3)#define BSP\_IO\_QSPI0\_SSL 0xFFFF0A05 /\* QSPI0\_SSL \*/

106

[ 107](pinctrl-rzv-common_8h.md#ab79be1e7eed598b1d9f09ce0bed7c625)#define BSP\_IO\_QSPI1\_SPCLK 0xFFFF0B00 /\* QSPI1\_SPCLK \*/

[ 108](pinctrl-rzv-common_8h.md#a225d50a8d0e6a40f10bc8fd28abc10db)#define BSP\_IO\_QSPI1\_IO0 0xFFFF0B01 /\* QSPI1\_IO0 \*/

[ 109](pinctrl-rzv-common_8h.md#ae926d4d471542c3b0593545acb9f2d1f)#define BSP\_IO\_QSPI1\_IO1 0xFFFF0B02 /\* QSPI1\_IO1 \*/

[ 110](pinctrl-rzv-common_8h.md#a4c6591684fc2d2b6f99cc229f5eea5f8)#define BSP\_IO\_QSPI1\_IO2 0xFFFF0B03 /\* QSPI1\_IO2 \*/

[ 111](pinctrl-rzv-common_8h.md#af3f0e39940012676f28d55d0c4959b63)#define BSP\_IO\_QSPI1\_IO3 0xFFFF0B04 /\* QSPI1\_IO3 \*/

[ 112](pinctrl-rzv-common_8h.md#a8ee3034ed36e82ee6968a037efed0b61)#define BSP\_IO\_QSPI1\_SSL 0xFFFF0B05 /\* QSPI1\_SSL \*/

113

[ 114](pinctrl-rzv-common_8h.md#ab6a44158744e5cad8124f4da291159dc)#define BSP\_IO\_QSPI\_RESET\_N 0xFFFF0C00 /\* QSPI\_RESET\_N \*/

[ 115](pinctrl-rzv-common_8h.md#abf8e87c6fdcd8241324c66b443668251)#define BSP\_IO\_QSPI\_WP\_N 0xFFFF0C01 /\* QSPI\_WP\_N \*/

[ 116](pinctrl-rzv-common_8h.md#aff4a128a9accbf9da0becf0afbca47cc)#define BSP\_IO\_QSPI\_INT\_N 0xFFFF0C02 /\* QSPI\_INT\_N \*/

117

[ 118](pinctrl-rzv-common_8h.md#ad2e37f140ebdb92bb4ee94f6a8032737)#define BSP\_IO\_WDTOVF\_PERROUT\_N 0xFFFF0D00 /\* WDTOVF\_PERROUT\_N \*/

119

[ 120](pinctrl-rzv-common_8h.md#abf5f96c4d40bddcef43d534d7ea6fdaa)#define BSP\_IO\_RIIC0\_SDA 0xFFFF0E00 /\* RIIC0\_SDA \*/

[ 121](pinctrl-rzv-common_8h.md#a20256eab52e96328dab53ff66037d35b)#define BSP\_IO\_RIIC0\_SCL 0xFFFF0E01 /\* RIIC0\_SCL \*/

[ 122](pinctrl-rzv-common_8h.md#adc37073529eb331cf8cc80185abf5f92)#define BSP\_IO\_RIIC1\_SDA 0xFFFF0E02 /\* RIIC1\_SDA \*/

[ 123](pinctrl-rzv-common_8h.md#ae1c7843f96e83c7aebb77512036aa20c)#define BSP\_IO\_RIIC1\_SCL 0xFFFF0E03 /\* RIIC1\_SCL \*/

124

125/\* FILNUM \*/

[ 126](pinctrl-rzv-common_8h.md#a474313de5067232584bb66a293cceef1)#define RZV\_FILNUM\_4\_STAGE 0

[ 127](pinctrl-rzv-common_8h.md#ab51d90be14e4d81c38c4cfa620270b64)#define RZV\_FILNUM\_8\_STAGE 1

[ 128](pinctrl-rzv-common_8h.md#ab3b284fd4bd5a16a2ea1d83116832cd2)#define RZV\_FILNUM\_12\_STAGE 2

[ 129](pinctrl-rzv-common_8h.md#a12034f75c3817d20962999b9040caca6)#define RZV\_FILNUM\_16\_STAGE 3

130

131/\* FILCLKSEL \*/

[ 132](pinctrl-rzv-common_8h.md#abac8582aa87640663955060639507ade)#define RZV\_FILCLKSEL\_NOT\_DIV 0

[ 133](pinctrl-rzv-common_8h.md#a43a5dfaf850006746e679e73a414e446)#define RZV\_FILCLKSEL\_DIV\_9000 1

[ 134](pinctrl-rzv-common_8h.md#ad1e144b7c5bf2d735a74f4bf84a58561)#define RZV\_FILCLKSEL\_DIV\_18000 2

[ 135](pinctrl-rzv-common_8h.md#a5cb812371774b2162d5b6f71d3422c19)#define RZV\_FILCLKSEL\_DIV\_36000 3

136

[ 137](pinctrl-rzv-common_8h.md#a038292c08044da9e82019e7aa73abf1c)#define RZV\_FILTER\_SET(filnum, filclksel) (((filnum) & 0x3) << 0x2) | (filclksel & 0x3)

138

139#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_PINCTRL\_RENESAS\_PINCTRL\_RZV\_COMMON\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [pinctrl](dir_2c6c4fbd167577104b7f1b7148586168.md)
- [renesas](dir_17f48eb154be6cea623223db5de209e7.md)
- [pinctrl-rzv-common.h](pinctrl-rzv-common_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
