---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/pinctrl-rzv2h_8h_source.html
original_path: doxygen/html/pinctrl-rzv2h_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

pinctrl-rzv2h.h

[Go to the documentation of this file.](pinctrl-rzv2h_8h.md)

1/\*

2 \* Copyright (c) 2025 Renesas Electronics Corporation

3 \* SPDX-License-Identifier: Apache-2.0

4 \*/

5

6#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_PINCTRL\_RENESAS\_PINCTRL\_RZV2H\_H\_

7#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_PINCTRL\_RENESAS\_PINCTRL\_RZV2H\_H\_

8

9/\* Superset list of all possible IO ports. \*/

[ 10](pinctrl-rzv2h_8h.md#a1b0292747e92dff43d6760d9e2258869)#define PORT\_00 0x0000 /\* IO port 0 \*/

[ 11](pinctrl-rzv2h_8h.md#a9de415830a2b3484dd33d5d08258dde5)#define PORT\_01 0x0100 /\* IO port 1 \*/

[ 12](pinctrl-rzv2h_8h.md#a7db623b2ec3816113a8f3fb07d5428ef)#define PORT\_02 0x0200 /\* IO port 2 \*/

[ 13](pinctrl-rzv2h_8h.md#a71478a4563d986886410618bc130b0d9)#define PORT\_03 0x0300 /\* IO port 3 \*/

[ 14](pinctrl-rzv2h_8h.md#aed73b97fc12615ac1dec9daad9537647)#define PORT\_04 0x0400 /\* IO port 4 \*/

[ 15](pinctrl-rzv2h_8h.md#a590020a2e6577d74d89bdee0989812c4)#define PORT\_05 0x0500 /\* IO port 5 \*/

[ 16](pinctrl-rzv2h_8h.md#ab2912aeb54c92971e0590ff3282e775b)#define PORT\_06 0x0600 /\* IO port 6 \*/

[ 17](pinctrl-rzv2h_8h.md#acabb0398db58703c47e718f899018410)#define PORT\_07 0x0700 /\* IO port 7 \*/

[ 18](pinctrl-rzv2h_8h.md#a5f4d0cfbea4e649fa0863d4a8d409c5e)#define PORT\_08 0x0800 /\* IO port 8 \*/

[ 19](pinctrl-rzv2h_8h.md#a5e8d840d1a1bd421615b2cc90ce0b90f)#define PORT\_09 0x0900 /\* IO port 9 \*/

[ 20](pinctrl-rzv2h_8h.md#a4c39a294d7b3a360c172b65151a5bfc8)#define PORT\_10 0x0A00 /\* IO port 10 \*/

[ 21](pinctrl-rzv2h_8h.md#abeebf6334cb5240b09d97d35fc0128f3)#define PORT\_11 0x0B00 /\* IO port 11 \*/

22

23/\*

24 \* Create the value contain port/pin/function information

25 \*

26 \* port: port number BSP\_IO\_PORT\_00..BSP\_IO\_PORT\_11

27 \* pin: pin number

28 \* func: pin function

29 \*/

[ 30](pinctrl-rzv2h_8h.md#ace27a9fee40fcee657b3aff941b3ac6b)#define RZV\_PINMUX(port, pin, func) (port | pin | (func << 4))

31

32/\* Special purpose port \*/

[ 33](pinctrl-rzv2h_8h.md#a5a8b4d2cdc15f25cc0b58db97c539b2a)#define BSP\_IO\_NMI 0xFFFF0100 /\* NMI \*/

34

[ 35](pinctrl-rzv2h_8h.md#af06a8358900119f6b4c3d91e465ce22f)#define BSP\_IO\_TMS\_SWDIO 0xFFFF0300 /\* TMS\_SWDIO \*/

36

[ 37](pinctrl-rzv2h_8h.md#a318b423b2efc8ab1a3de0a8f9ab3eeca)#define BSP\_IO\_TDO 0xFFFF0302 /\* TDO \*/

38

[ 39](pinctrl-rzv2h_8h.md#ac2edcba3708e5888a80b390c1f55adb0)#define BSP\_IO\_WDTUDFCA 0xFFFF0500 /\* WDTUDFCA \*/

[ 40](pinctrl-rzv2h_8h.md#a17ee049758d71222d20196df52b893b7)#define BSP\_IO\_WDTUDFCM 0xFFFF0501 /\* WDTUDFCM \*/

41

[ 42](pinctrl-rzv2h_8h.md#a471d8bb707e4a89559be0b5111b85db9)#define BSP\_IO\_SCIF\_RXD 0xFFFF0600 /\* SCIF\_RXD \*/

[ 43](pinctrl-rzv2h_8h.md#a796a4aeccb790011b04612464f2cb4a8)#define BSP\_IO\_SCIF\_TXD 0xFFFF0601 /\* SCIF\_TXD \*/

44

[ 45](pinctrl-rzv2h_8h.md#a7fd026b6ffc6db6ccb085d600046ab50)#define BSP\_IO\_XSPI0\_CKP 0xFFFF0700 /\* XSPI0\_CKP \*/

[ 46](pinctrl-rzv2h_8h.md#a6d2fa31046fc5e52deb6ebc62cea4688)#define BSP\_IO\_XSPI0\_CKN 0xFFFF0701 /\* XSPI0\_CKN \*/

[ 47](pinctrl-rzv2h_8h.md#a154ea1f0b0ff649fc61c3f64fa0bd69e)#define BSP\_IO\_XSPI0\_CS0N 0xFFFF0702 /\* XSPI0\_CS0N \*/

[ 48](pinctrl-rzv2h_8h.md#af9862a3a0391b96398c6feeb266e454a)#define BSP\_IO\_XSPI0\_DS 0xFFFF0703 /\* XSPI0\_DS \*/

[ 49](pinctrl-rzv2h_8h.md#afb70b7ffeb25be4e91d5782699913fd1)#define BSP\_IO\_XSPI0\_RESET0N 0xFFFF0704 /\* XSPI0\_RESET0N \*/

[ 50](pinctrl-rzv2h_8h.md#aba5df3d7f44c4afc1e88d25cad744696)#define BSP\_IO\_XSPI0\_RSTO0N 0xFFFF0705 /\* XSPI0\_RSTO0N \*/

[ 51](pinctrl-rzv2h_8h.md#a93da56bce0940882dcbec1217ab2528a)#define BSP\_IO\_XSPI0\_INT0N 0xFFFF0706 /\* XSPI0\_INT0N \*/

[ 52](pinctrl-rzv2h_8h.md#abb95c2dac4b836de5a2feed73360bbc7)#define BSP\_IO\_XSPI0\_ECS0N 0xFFFF0707 /\* XSPI0\_ECS0N \*/

53

[ 54](pinctrl-rzv2h_8h.md#a4d2dfc310f6cddd4180f492afa424195)#define BSP\_IO\_XSPI0\_IO0 0xFFFF0800 /\* XSPI0\_IO0 \*/

[ 55](pinctrl-rzv2h_8h.md#a508e71fd569e26596c6b67d3f1272960)#define BSP\_IO\_XSPI0\_IO1 0xFFFF0801 /\* XSPI0\_IO1 \*/

[ 56](pinctrl-rzv2h_8h.md#a4dd807715c8b53fc9230285b7f9a27ce)#define BSP\_IO\_XSPI0\_IO2 0xFFFF0802 /\* XSPI0\_IO2 \*/

[ 57](pinctrl-rzv2h_8h.md#a06e205e34bb3b58e82f8996f5fa2d149)#define BSP\_IO\_XSPI0\_IO3 0xFFFF0803 /\* XSPI0\_IO3 \*/

[ 58](pinctrl-rzv2h_8h.md#a287a1b337f71412dcde0aba38a37f0bd)#define BSP\_IO\_XSPI0\_IO4 0xFFFF0804 /\* XSPI0\_IO4 \*/

[ 59](pinctrl-rzv2h_8h.md#ad533760a2339c31dc4205b357b62cb0c)#define BSP\_IO\_XSPI0\_IO5 0xFFFF0805 /\* XSPI0\_IO5 \*/

[ 60](pinctrl-rzv2h_8h.md#a5df9b361f9ea59a0bbbeca44a17199e9)#define BSP\_IO\_XSPI0\_IO6 0xFFFF0806 /\* XSPI0\_IO6 \*/

[ 61](pinctrl-rzv2h_8h.md#aaa8a2e7aab31cfd5cec926270aeab322)#define BSP\_IO\_XSPI0\_IO7 0xFFFF0807 /\* XSPI0\_IO7 \*/

62

[ 63](pinctrl-rzv2h_8h.md#aaa12b2c5e1e98e3c10274d74dd8b5355)#define BSP\_IO\_SD0CLK 0xFFFF0900 /\* SD0CLK \*/

[ 64](pinctrl-rzv2h_8h.md#a7c2a7b6e2b4b7d59d70cad16bb1643f9)#define BSP\_IO\_SD0CMD 0xFFFF0901 /\* SD0CMD \*/

[ 65](pinctrl-rzv2h_8h.md#a36f139827da1deed0cda643110fc433c)#define BSP\_IO\_SD0RSTN 0xFFFF0902 /\* SD0RSTN \*/

66

[ 67](pinctrl-rzv2h_8h.md#a00b9658c97f4ccb1c297a035ad23373b)#define BSP\_IO\_SD0DAT0 0xFFFF0A00 /\* SD0DAT0 \*/

[ 68](pinctrl-rzv2h_8h.md#a4a30feece071a0aa2dcfb24e9a479f73)#define BSP\_IO\_SD0DAT1 0xFFFF0A01 /\* SD0DAT1 \*/

[ 69](pinctrl-rzv2h_8h.md#adb6cf77200d6a1fd93f0f2a402d08b6e)#define BSP\_IO\_SD0DAT2 0xFFFF0A02 /\* SD0DAT2 \*/

[ 70](pinctrl-rzv2h_8h.md#a0b4facd2f842db7c229512921db7a9cd)#define BSP\_IO\_SD0DAT3 0xFFFF0A03 /\* SD0DAT3 \*/

[ 71](pinctrl-rzv2h_8h.md#a92fc90bf3dd81a609e2b970a0c6e58f4)#define BSP\_IO\_SD0DAT4 0xFFFF0A04 /\* SD0DAT4 \*/

[ 72](pinctrl-rzv2h_8h.md#a5d08d8333c7059b4184431a2ad6dce00)#define BSP\_IO\_SD0DAT5 0xFFFF0A05 /\* SD0DAT5 \*/

[ 73](pinctrl-rzv2h_8h.md#a1395add1e4783d3d16adf13e9c043329)#define BSP\_IO\_SD0DAT6 0xFFFF0A06 /\* SD0DAT6 \*/

[ 74](pinctrl-rzv2h_8h.md#aad08493d9205abfd23c9f6318b3fadf9)#define BSP\_IO\_SD0DAT7 0xFFFF0A07 /\* SD0DAT7 \*/

75

[ 76](pinctrl-rzv2h_8h.md#ab78ba53890588fcecb5c969bb4528c2f)#define BSP\_IO\_SD1CLK 0xFFFF0B00 /\* SD1CLK \*/

[ 77](pinctrl-rzv2h_8h.md#a53b15de62883dda6d2f19ac613bdc389)#define BSP\_IO\_SD1CMD 0xFFFF0B01 /\* SD1CMD \*/

78

[ 79](pinctrl-rzv2h_8h.md#ab34dd59d23acde42b9613c84c0d295e2)#define BSP\_IO\_SD1DAT0 0xFFFF0C00 /\* SD1DAT0 \*/

[ 80](pinctrl-rzv2h_8h.md#a92ba6c595074ded1609365e5dbcb1a6c)#define BSP\_IO\_SD1DAT1 0xFFFF0C01 /\* SD1DAT1 \*/

[ 81](pinctrl-rzv2h_8h.md#a88221cb800114c0f4fe6e8f98246ada0)#define BSP\_IO\_SD1DAT2 0xFFFF0C02 /\* SD1DAT2 \*/

[ 82](pinctrl-rzv2h_8h.md#a32f2ab4b2678393032f582cc2abf2ef0)#define BSP\_IO\_SD1DAT3 0xFFFF0C03 /\* SD1DAT3 \*/

83

[ 84](pinctrl-rzv2h_8h.md#a8b035e432c4d35e80e18046c2965b21d)#define BSP\_IO\_PCIE0\_RSTOUTB 0xFFFF0E00 /\* PCIE0\_RSTOUTB \*/

[ 85](pinctrl-rzv2h_8h.md#a99c0ba673dd1a5f776043196b3a5a984)#define BSP\_IO\_PCIE1\_RSTOUTB 0xFFFF0E01 /\* PCIE1\_RSTOUTB \*/

86

[ 87](pinctrl-rzv2h_8h.md#affb6069f81f4969760515ff6e6afb11c)#define BSP\_IO\_ET0\_MDIO 0xFFFF0F00 /\* ET0\_MDIO \*/

[ 88](pinctrl-rzv2h_8h.md#a9e70ca0c92cbcdca10c350c653ebd7a4)#define BSP\_IO\_ET0\_MDC 0xFFFF0F01 /\* ET0\_MDC \*/

89

[ 90](pinctrl-rzv2h_8h.md#ad98aa0cf398a7a717e1bc4e74a1903ae)#define BSP\_IO\_ET0\_RXCTL\_RXDV 0xFFFF1000 /\* ET0\_RXCTL\_RXDV \*/

[ 91](pinctrl-rzv2h_8h.md#a1ff3549a67af86d6e3f7b059a92a2afb)#define BSP\_IO\_ET0\_TXCTL\_TXEN 0xFFFF1001 /\* ET0\_TXCTL\_TXEN \*/

[ 92](pinctrl-rzv2h_8h.md#a37987476f631345e932456c515be0640)#define BSP\_IO\_ET0\_TXER 0xFFFF1002 /\* ET0\_TXER \*/

[ 93](pinctrl-rzv2h_8h.md#a4674592e231ba8d6f40eb394a60feb0f)#define BSP\_IO\_ET0\_RXER 0xFFFF1003 /\* ET0\_RXER \*/

[ 94](pinctrl-rzv2h_8h.md#a23526264c453ac5d6f24812eb21223c6)#define BSP\_IO\_ET0\_RXC\_RXCLK 0xFFFF1004 /\* ET0\_RXC\_RXCLK \*/

[ 95](pinctrl-rzv2h_8h.md#a96ce0ec77d5903e518aac3bd0a185444)#define BSP\_IO\_ET0\_TXC\_TXCLK 0xFFFF1005 /\* ET0\_TXC\_TXCLK \*/

[ 96](pinctrl-rzv2h_8h.md#a63385ba25b44616f89ea5799a331f280)#define BSP\_IO\_ET0\_CRS 0xFFFF1006 /\* ET0\_CRS \*/

[ 97](pinctrl-rzv2h_8h.md#acf07d83bfab8122dae4038af1323f6de)#define BSP\_IO\_ET0\_COL 0xFFFF1007 /\* ET0\_COL \*/

98

[ 99](pinctrl-rzv2h_8h.md#a4b602637a9544fa6a9d0078df0bdec75)#define BSP\_IO\_ET0\_TXD0 0xFFFF1100 /\* ET0\_TXD0 \*/

[ 100](pinctrl-rzv2h_8h.md#ae6488452648a6a299a2c7769fefd62cb)#define BSP\_IO\_ET0\_TXD1 0xFFFF1101 /\* ET0\_TXD1 \*/

[ 101](pinctrl-rzv2h_8h.md#a427e1641f737920d7e21cc672a44e15e)#define BSP\_IO\_ET0\_TXD2 0xFFFF1102 /\* ET0\_TXD2 \*/

[ 102](pinctrl-rzv2h_8h.md#ab85a510df46ba7bfc34f6ac9763c570f)#define BSP\_IO\_ET0\_TXD3 0xFFFF1103 /\* ET0\_TXD3 \*/

[ 103](pinctrl-rzv2h_8h.md#a258ab4720e4e79dbf89825f6ad9a8b64)#define BSP\_IO\_ET0\_RXD0 0xFFFF1104 /\* ET0\_RXD0 \*/

[ 104](pinctrl-rzv2h_8h.md#a24752e5ec875f68c121cb6e11242f7ec)#define BSP\_IO\_ET0\_RXD1 0xFFFF1105 /\* ET0\_RXD1 \*/

[ 105](pinctrl-rzv2h_8h.md#a599fb60443fe1616d80be533bdd94fb8)#define BSP\_IO\_ET0\_RXD2 0xFFFF1106 /\* ET0\_RXD2 \*/

[ 106](pinctrl-rzv2h_8h.md#a8d8da7f1833fd91359378c44eb02d0a7)#define BSP\_IO\_ET0\_RXD3 0xFFFF1107 /\* ET0\_RXD3 \*/

107

[ 108](pinctrl-rzv2h_8h.md#ac0117e2fb0c9dfdc2cc46a24324c6455)#define BSP\_IO\_ET1\_MDIO 0xFFFF1200 /\* ET1\_MDIO \*/

[ 109](pinctrl-rzv2h_8h.md#ae6d4060ae6fd6c05379be5d7edc8f2f0)#define BSP\_IO\_ET1\_MDC 0xFFFF1201 /\* ET1\_MDC \*/

110

[ 111](pinctrl-rzv2h_8h.md#ac55eaa22c0834db36089216d261bcf7c)#define BSP\_IO\_ET1\_RXCTL\_RXDV 0xFFFF1300 /\* ET1\_RXCTL\_RXDV \*/

[ 112](pinctrl-rzv2h_8h.md#a02c3411d7e0bb049d555f52ca9cb3f25)#define BSP\_IO\_ET1\_TXCTL\_TXEN 0xFFFF1301 /\* ET1\_TXCTL\_TXEN \*/

[ 113](pinctrl-rzv2h_8h.md#a169635733406399a183046fec986cfbb)#define BSP\_IO\_ET1\_TXER 0xFFFF1302 /\* ET1\_TXER \*/

[ 114](pinctrl-rzv2h_8h.md#ad1af1ded92a3d3e9b1e30b92961611f0)#define BSP\_IO\_ET1\_RXER 0xFFFF1303 /\* ET1\_RXER \*/

[ 115](pinctrl-rzv2h_8h.md#a8668737f90448aa6808f27159ee61419)#define BSP\_IO\_ET1\_RXC\_RXCLK 0xFFFF1304 /\* ET1\_RXC\_RXCLK \*/

[ 116](pinctrl-rzv2h_8h.md#a37e6c627995f864631cfe90f516e937c)#define BSP\_IO\_ET1\_TXC\_TXCLK 0xFFFF1305 /\* ET1\_TXC\_TXCLK \*/

[ 117](pinctrl-rzv2h_8h.md#af3bcd5eed4d57df86fa85a28624d29b8)#define BSP\_IO\_ET1\_CRS 0xFFFF1306 /\* ET1\_CRS \*/

[ 118](pinctrl-rzv2h_8h.md#ab0efa2e81b694ed26776990f9518b957)#define BSP\_IO\_ET1\_COL 0xFFFF1307 /\* ET1\_COL \*/

119

[ 120](pinctrl-rzv2h_8h.md#a11416ba84899fc19457cfb83f1b0aafa)#define BSP\_IO\_ET1\_TXD0 0xFFFF1400 /\* ET1\_TXD0 \*/

[ 121](pinctrl-rzv2h_8h.md#ad7cc67151309c413bd542d957064b5c1)#define BSP\_IO\_ET1\_TXD1 0xFFFF1401 /\* ET1\_TXD1 \*/

[ 122](pinctrl-rzv2h_8h.md#a4624d11a09f7120ef0ca1ff6ad18dfe7)#define BSP\_IO\_ET1\_TXD2 0xFFFF1402 /\* ET1\_TXD2 \*/

[ 123](pinctrl-rzv2h_8h.md#a1472a2198a99a29571ad223cdd6b4026)#define BSP\_IO\_ET1\_TXD3 0xFFFF1403 /\* ET1\_TXD3 \*/

[ 124](pinctrl-rzv2h_8h.md#a7c7254de0259532616470d19e7752092)#define BSP\_IO\_ET1\_RXD0 0xFFFF1404 /\* ET1\_RXD0 \*/

[ 125](pinctrl-rzv2h_8h.md#a45f3b9373a5d693c7296c75c09b1d7b0)#define BSP\_IO\_ET1\_RXD1 0xFFFF1405 /\* ET1\_RXD1 \*/

[ 126](pinctrl-rzv2h_8h.md#a2fa85dd0820d0544fe0bc2a69d3cf1d6)#define BSP\_IO\_ET1\_RXD2 0xFFFF1406 /\* ET1\_RXD2 \*/

[ 127](pinctrl-rzv2h_8h.md#ac74ad60939668d2e07308a7ddc24f73c)#define BSP\_IO\_ET1\_RXD3 0xFFFF1407 /\* ET1\_RXD3 \*/

128

129/\* FILNUM \*/

[ 130](pinctrl-rzv2h_8h.md#a474313de5067232584bb66a293cceef1)#define RZV\_FILNUM\_4\_STAGE 0

[ 131](pinctrl-rzv2h_8h.md#ab51d90be14e4d81c38c4cfa620270b64)#define RZV\_FILNUM\_8\_STAGE 1

[ 132](pinctrl-rzv2h_8h.md#ab3b284fd4bd5a16a2ea1d83116832cd2)#define RZV\_FILNUM\_12\_STAGE 2

[ 133](pinctrl-rzv2h_8h.md#a12034f75c3817d20962999b9040caca6)#define RZV\_FILNUM\_16\_STAGE 3

134

135/\* FILCLKSEL \*/

[ 136](pinctrl-rzv2h_8h.md#abac8582aa87640663955060639507ade)#define RZV\_FILCLKSEL\_NOT\_DIV 0

[ 137](pinctrl-rzv2h_8h.md#a43a5dfaf850006746e679e73a414e446)#define RZV\_FILCLKSEL\_DIV\_9000 1

[ 138](pinctrl-rzv2h_8h.md#ad1e144b7c5bf2d735a74f4bf84a58561)#define RZV\_FILCLKSEL\_DIV\_18000 2

[ 139](pinctrl-rzv2h_8h.md#a5cb812371774b2162d5b6f71d3422c19)#define RZV\_FILCLKSEL\_DIV\_36000 3

140

[ 141](pinctrl-rzv2h_8h.md#a038292c08044da9e82019e7aa73abf1c)#define RZV\_FILTER\_SET(filnum, filclksel) (((filnum) & 0x3) << 0x2) | (filclksel & 0x3)

142

143#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_PINCTRL\_RENESAS\_PINCTRL\_RZV2H\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [pinctrl](dir_2c6c4fbd167577104b7f1b7148586168.md)
- [renesas](dir_17f48eb154be6cea623223db5de209e7.md)
- [pinctrl-rzv2h.h](pinctrl-rzv2h_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
