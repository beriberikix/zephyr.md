---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/pinctrl-rzv2h_8h.html
original_path: doxygen/html/pinctrl-rzv2h_8h.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

pinctrl-rzv2h.h File Reference

[Go to the source code of this file.](pinctrl-rzv2h_8h_source.md)

| Macros | |
| --- | --- |
| #define | [PORT\_00](#a1b0292747e92dff43d6760d9e2258869)   0x0000 /\* IO port 0 \*/ |
| #define | [PORT\_01](#a9de415830a2b3484dd33d5d08258dde5)   0x0100 /\* IO port 1 \*/ |
| #define | [PORT\_02](#a7db623b2ec3816113a8f3fb07d5428ef)   0x0200 /\* IO port 2 \*/ |
| #define | [PORT\_03](#a71478a4563d986886410618bc130b0d9)   0x0300 /\* IO port 3 \*/ |
| #define | [PORT\_04](#aed73b97fc12615ac1dec9daad9537647)   0x0400 /\* IO port 4 \*/ |
| #define | [PORT\_05](#a590020a2e6577d74d89bdee0989812c4)   0x0500 /\* IO port 5 \*/ |
| #define | [PORT\_06](#ab2912aeb54c92971e0590ff3282e775b)   0x0600 /\* IO port 6 \*/ |
| #define | [PORT\_07](#acabb0398db58703c47e718f899018410)   0x0700 /\* IO port 7 \*/ |
| #define | [PORT\_08](#a5f4d0cfbea4e649fa0863d4a8d409c5e)   0x0800 /\* IO port 8 \*/ |
| #define | [PORT\_09](#a5e8d840d1a1bd421615b2cc90ce0b90f)   0x0900 /\* IO port 9 \*/ |
| #define | [PORT\_10](#a4c39a294d7b3a360c172b65151a5bfc8)   0x0A00 /\* IO port 10 \*/ |
| #define | [PORT\_11](#abeebf6334cb5240b09d97d35fc0128f3)   0x0B00 /\* IO port 11 \*/ |
| #define | [RZV\_PINMUX](#ace27a9fee40fcee657b3aff941b3ac6b)(port, pin, func) |
| #define | [BSP\_IO\_NMI](#a5a8b4d2cdc15f25cc0b58db97c539b2a)   0xFFFF0100 /\* NMI \*/ |
| #define | [BSP\_IO\_TMS\_SWDIO](#af06a8358900119f6b4c3d91e465ce22f)   0xFFFF0300 /\* TMS\_SWDIO \*/ |
| #define | [BSP\_IO\_TDO](#a318b423b2efc8ab1a3de0a8f9ab3eeca)   0xFFFF0302 /\* TDO \*/ |
| #define | [BSP\_IO\_WDTUDFCA](#ac2edcba3708e5888a80b390c1f55adb0)   0xFFFF0500 /\* WDTUDFCA \*/ |
| #define | [BSP\_IO\_WDTUDFCM](#a17ee049758d71222d20196df52b893b7)   0xFFFF0501 /\* WDTUDFCM \*/ |
| #define | [BSP\_IO\_SCIF\_RXD](#a471d8bb707e4a89559be0b5111b85db9)   0xFFFF0600 /\* SCIF\_RXD \*/ |
| #define | [BSP\_IO\_SCIF\_TXD](#a796a4aeccb790011b04612464f2cb4a8)   0xFFFF0601 /\* SCIF\_TXD \*/ |
| #define | [BSP\_IO\_XSPI0\_CKP](#a7fd026b6ffc6db6ccb085d600046ab50)   0xFFFF0700 /\* XSPI0\_CKP \*/ |
| #define | [BSP\_IO\_XSPI0\_CKN](#a6d2fa31046fc5e52deb6ebc62cea4688)   0xFFFF0701 /\* XSPI0\_CKN \*/ |
| #define | [BSP\_IO\_XSPI0\_CS0N](#a154ea1f0b0ff649fc61c3f64fa0bd69e)   0xFFFF0702 /\* XSPI0\_CS0N \*/ |
| #define | [BSP\_IO\_XSPI0\_DS](#af9862a3a0391b96398c6feeb266e454a)   0xFFFF0703 /\* XSPI0\_DS \*/ |
| #define | [BSP\_IO\_XSPI0\_RESET0N](#afb70b7ffeb25be4e91d5782699913fd1)   0xFFFF0704 /\* XSPI0\_RESET0N \*/ |
| #define | [BSP\_IO\_XSPI0\_RSTO0N](#aba5df3d7f44c4afc1e88d25cad744696)   0xFFFF0705 /\* XSPI0\_RSTO0N \*/ |
| #define | [BSP\_IO\_XSPI0\_INT0N](#a93da56bce0940882dcbec1217ab2528a)   0xFFFF0706 /\* XSPI0\_INT0N \*/ |
| #define | [BSP\_IO\_XSPI0\_ECS0N](#abb95c2dac4b836de5a2feed73360bbc7)   0xFFFF0707 /\* XSPI0\_ECS0N \*/ |
| #define | [BSP\_IO\_XSPI0\_IO0](#a4d2dfc310f6cddd4180f492afa424195)   0xFFFF0800 /\* XSPI0\_IO0 \*/ |
| #define | [BSP\_IO\_XSPI0\_IO1](#a508e71fd569e26596c6b67d3f1272960)   0xFFFF0801 /\* XSPI0\_IO1 \*/ |
| #define | [BSP\_IO\_XSPI0\_IO2](#a4dd807715c8b53fc9230285b7f9a27ce)   0xFFFF0802 /\* XSPI0\_IO2 \*/ |
| #define | [BSP\_IO\_XSPI0\_IO3](#a06e205e34bb3b58e82f8996f5fa2d149)   0xFFFF0803 /\* XSPI0\_IO3 \*/ |
| #define | [BSP\_IO\_XSPI0\_IO4](#a287a1b337f71412dcde0aba38a37f0bd)   0xFFFF0804 /\* XSPI0\_IO4 \*/ |
| #define | [BSP\_IO\_XSPI0\_IO5](#ad533760a2339c31dc4205b357b62cb0c)   0xFFFF0805 /\* XSPI0\_IO5 \*/ |
| #define | [BSP\_IO\_XSPI0\_IO6](#a5df9b361f9ea59a0bbbeca44a17199e9)   0xFFFF0806 /\* XSPI0\_IO6 \*/ |
| #define | [BSP\_IO\_XSPI0\_IO7](#aaa8a2e7aab31cfd5cec926270aeab322)   0xFFFF0807 /\* XSPI0\_IO7 \*/ |
| #define | [BSP\_IO\_SD0CLK](#aaa12b2c5e1e98e3c10274d74dd8b5355)   0xFFFF0900 /\* SD0CLK \*/ |
| #define | [BSP\_IO\_SD0CMD](#a7c2a7b6e2b4b7d59d70cad16bb1643f9)   0xFFFF0901 /\* SD0CMD \*/ |
| #define | [BSP\_IO\_SD0RSTN](#a36f139827da1deed0cda643110fc433c)   0xFFFF0902 /\* SD0RSTN \*/ |
| #define | [BSP\_IO\_SD0DAT0](#a00b9658c97f4ccb1c297a035ad23373b)   0xFFFF0A00 /\* SD0DAT0 \*/ |
| #define | [BSP\_IO\_SD0DAT1](#a4a30feece071a0aa2dcfb24e9a479f73)   0xFFFF0A01 /\* SD0DAT1 \*/ |
| #define | [BSP\_IO\_SD0DAT2](#adb6cf77200d6a1fd93f0f2a402d08b6e)   0xFFFF0A02 /\* SD0DAT2 \*/ |
| #define | [BSP\_IO\_SD0DAT3](#a0b4facd2f842db7c229512921db7a9cd)   0xFFFF0A03 /\* SD0DAT3 \*/ |
| #define | [BSP\_IO\_SD0DAT4](#a92fc90bf3dd81a609e2b970a0c6e58f4)   0xFFFF0A04 /\* SD0DAT4 \*/ |
| #define | [BSP\_IO\_SD0DAT5](#a5d08d8333c7059b4184431a2ad6dce00)   0xFFFF0A05 /\* SD0DAT5 \*/ |
| #define | [BSP\_IO\_SD0DAT6](#a1395add1e4783d3d16adf13e9c043329)   0xFFFF0A06 /\* SD0DAT6 \*/ |
| #define | [BSP\_IO\_SD0DAT7](#aad08493d9205abfd23c9f6318b3fadf9)   0xFFFF0A07 /\* SD0DAT7 \*/ |
| #define | [BSP\_IO\_SD1CLK](#ab78ba53890588fcecb5c969bb4528c2f)   0xFFFF0B00 /\* SD1CLK \*/ |
| #define | [BSP\_IO\_SD1CMD](#a53b15de62883dda6d2f19ac613bdc389)   0xFFFF0B01 /\* SD1CMD \*/ |
| #define | [BSP\_IO\_SD1DAT0](#ab34dd59d23acde42b9613c84c0d295e2)   0xFFFF0C00 /\* SD1DAT0 \*/ |
| #define | [BSP\_IO\_SD1DAT1](#a92ba6c595074ded1609365e5dbcb1a6c)   0xFFFF0C01 /\* SD1DAT1 \*/ |
| #define | [BSP\_IO\_SD1DAT2](#a88221cb800114c0f4fe6e8f98246ada0)   0xFFFF0C02 /\* SD1DAT2 \*/ |
| #define | [BSP\_IO\_SD1DAT3](#a32f2ab4b2678393032f582cc2abf2ef0)   0xFFFF0C03 /\* SD1DAT3 \*/ |
| #define | [BSP\_IO\_PCIE0\_RSTOUTB](#a8b035e432c4d35e80e18046c2965b21d)   0xFFFF0E00 /\* PCIE0\_RSTOUTB \*/ |
| #define | [BSP\_IO\_PCIE1\_RSTOUTB](#a99c0ba673dd1a5f776043196b3a5a984)   0xFFFF0E01 /\* PCIE1\_RSTOUTB \*/ |
| #define | [BSP\_IO\_ET0\_MDIO](#affb6069f81f4969760515ff6e6afb11c)   0xFFFF0F00 /\* ET0\_MDIO \*/ |
| #define | [BSP\_IO\_ET0\_MDC](#a9e70ca0c92cbcdca10c350c653ebd7a4)   0xFFFF0F01 /\* ET0\_MDC \*/ |
| #define | [BSP\_IO\_ET0\_RXCTL\_RXDV](#ad98aa0cf398a7a717e1bc4e74a1903ae)   0xFFFF1000 /\* ET0\_RXCTL\_RXDV \*/ |
| #define | [BSP\_IO\_ET0\_TXCTL\_TXEN](#a1ff3549a67af86d6e3f7b059a92a2afb)   0xFFFF1001 /\* ET0\_TXCTL\_TXEN \*/ |
| #define | [BSP\_IO\_ET0\_TXER](#a37987476f631345e932456c515be0640)   0xFFFF1002 /\* ET0\_TXER \*/ |
| #define | [BSP\_IO\_ET0\_RXER](#a4674592e231ba8d6f40eb394a60feb0f)   0xFFFF1003 /\* ET0\_RXER \*/ |
| #define | [BSP\_IO\_ET0\_RXC\_RXCLK](#a23526264c453ac5d6f24812eb21223c6)   0xFFFF1004 /\* ET0\_RXC\_RXCLK \*/ |
| #define | [BSP\_IO\_ET0\_TXC\_TXCLK](#a96ce0ec77d5903e518aac3bd0a185444)   0xFFFF1005 /\* ET0\_TXC\_TXCLK \*/ |
| #define | [BSP\_IO\_ET0\_CRS](#a63385ba25b44616f89ea5799a331f280)   0xFFFF1006 /\* ET0\_CRS \*/ |
| #define | [BSP\_IO\_ET0\_COL](#acf07d83bfab8122dae4038af1323f6de)   0xFFFF1007 /\* ET0\_COL \*/ |
| #define | [BSP\_IO\_ET0\_TXD0](#a4b602637a9544fa6a9d0078df0bdec75)   0xFFFF1100 /\* ET0\_TXD0 \*/ |
| #define | [BSP\_IO\_ET0\_TXD1](#ae6488452648a6a299a2c7769fefd62cb)   0xFFFF1101 /\* ET0\_TXD1 \*/ |
| #define | [BSP\_IO\_ET0\_TXD2](#a427e1641f737920d7e21cc672a44e15e)   0xFFFF1102 /\* ET0\_TXD2 \*/ |
| #define | [BSP\_IO\_ET0\_TXD3](#ab85a510df46ba7bfc34f6ac9763c570f)   0xFFFF1103 /\* ET0\_TXD3 \*/ |
| #define | [BSP\_IO\_ET0\_RXD0](#a258ab4720e4e79dbf89825f6ad9a8b64)   0xFFFF1104 /\* ET0\_RXD0 \*/ |
| #define | [BSP\_IO\_ET0\_RXD1](#a24752e5ec875f68c121cb6e11242f7ec)   0xFFFF1105 /\* ET0\_RXD1 \*/ |
| #define | [BSP\_IO\_ET0\_RXD2](#a599fb60443fe1616d80be533bdd94fb8)   0xFFFF1106 /\* ET0\_RXD2 \*/ |
| #define | [BSP\_IO\_ET0\_RXD3](#a8d8da7f1833fd91359378c44eb02d0a7)   0xFFFF1107 /\* ET0\_RXD3 \*/ |
| #define | [BSP\_IO\_ET1\_MDIO](#ac0117e2fb0c9dfdc2cc46a24324c6455)   0xFFFF1200 /\* ET1\_MDIO \*/ |
| #define | [BSP\_IO\_ET1\_MDC](#ae6d4060ae6fd6c05379be5d7edc8f2f0)   0xFFFF1201 /\* ET1\_MDC \*/ |
| #define | [BSP\_IO\_ET1\_RXCTL\_RXDV](#ac55eaa22c0834db36089216d261bcf7c)   0xFFFF1300 /\* ET1\_RXCTL\_RXDV \*/ |
| #define | [BSP\_IO\_ET1\_TXCTL\_TXEN](#a02c3411d7e0bb049d555f52ca9cb3f25)   0xFFFF1301 /\* ET1\_TXCTL\_TXEN \*/ |
| #define | [BSP\_IO\_ET1\_TXER](#a169635733406399a183046fec986cfbb)   0xFFFF1302 /\* ET1\_TXER \*/ |
| #define | [BSP\_IO\_ET1\_RXER](#ad1af1ded92a3d3e9b1e30b92961611f0)   0xFFFF1303 /\* ET1\_RXER \*/ |
| #define | [BSP\_IO\_ET1\_RXC\_RXCLK](#a8668737f90448aa6808f27159ee61419)   0xFFFF1304 /\* ET1\_RXC\_RXCLK \*/ |
| #define | [BSP\_IO\_ET1\_TXC\_TXCLK](#a37e6c627995f864631cfe90f516e937c)   0xFFFF1305 /\* ET1\_TXC\_TXCLK \*/ |
| #define | [BSP\_IO\_ET1\_CRS](#af3bcd5eed4d57df86fa85a28624d29b8)   0xFFFF1306 /\* ET1\_CRS \*/ |
| #define | [BSP\_IO\_ET1\_COL](#ab0efa2e81b694ed26776990f9518b957)   0xFFFF1307 /\* ET1\_COL \*/ |
| #define | [BSP\_IO\_ET1\_TXD0](#a11416ba84899fc19457cfb83f1b0aafa)   0xFFFF1400 /\* ET1\_TXD0 \*/ |
| #define | [BSP\_IO\_ET1\_TXD1](#ad7cc67151309c413bd542d957064b5c1)   0xFFFF1401 /\* ET1\_TXD1 \*/ |
| #define | [BSP\_IO\_ET1\_TXD2](#a4624d11a09f7120ef0ca1ff6ad18dfe7)   0xFFFF1402 /\* ET1\_TXD2 \*/ |
| #define | [BSP\_IO\_ET1\_TXD3](#a1472a2198a99a29571ad223cdd6b4026)   0xFFFF1403 /\* ET1\_TXD3 \*/ |
| #define | [BSP\_IO\_ET1\_RXD0](#a7c7254de0259532616470d19e7752092)   0xFFFF1404 /\* ET1\_RXD0 \*/ |
| #define | [BSP\_IO\_ET1\_RXD1](#a45f3b9373a5d693c7296c75c09b1d7b0)   0xFFFF1405 /\* ET1\_RXD1 \*/ |
| #define | [BSP\_IO\_ET1\_RXD2](#a2fa85dd0820d0544fe0bc2a69d3cf1d6)   0xFFFF1406 /\* ET1\_RXD2 \*/ |
| #define | [BSP\_IO\_ET1\_RXD3](#ac74ad60939668d2e07308a7ddc24f73c)   0xFFFF1407 /\* ET1\_RXD3 \*/ |
| #define | [RZV\_FILNUM\_4\_STAGE](#a474313de5067232584bb66a293cceef1)   0 |
| #define | [RZV\_FILNUM\_8\_STAGE](#ab51d90be14e4d81c38c4cfa620270b64)   1 |
| #define | [RZV\_FILNUM\_12\_STAGE](#ab3b284fd4bd5a16a2ea1d83116832cd2)   2 |
| #define | [RZV\_FILNUM\_16\_STAGE](#a12034f75c3817d20962999b9040caca6)   3 |
| #define | [RZV\_FILCLKSEL\_NOT\_DIV](#abac8582aa87640663955060639507ade)   0 |
| #define | [RZV\_FILCLKSEL\_DIV\_9000](#a43a5dfaf850006746e679e73a414e446)   1 |
| #define | [RZV\_FILCLKSEL\_DIV\_18000](#ad1e144b7c5bf2d735a74f4bf84a58561)   2 |
| #define | [RZV\_FILCLKSEL\_DIV\_36000](#a5cb812371774b2162d5b6f71d3422c19)   3 |
| #define | [RZV\_FILTER\_SET](#a038292c08044da9e82019e7aa73abf1c)(filnum, filclksel) |

## Macro Definition Documentation

## [◆ ](#acf07d83bfab8122dae4038af1323f6de)BSP\_IO\_ET0\_COL

| #define BSP\_IO\_ET0\_COL   0xFFFF1007 /\* ET0\_COL \*/ |
| --- |

## [◆ ](#a63385ba25b44616f89ea5799a331f280)BSP\_IO\_ET0\_CRS

| #define BSP\_IO\_ET0\_CRS   0xFFFF1006 /\* ET0\_CRS \*/ |
| --- |

## [◆ ](#a9e70ca0c92cbcdca10c350c653ebd7a4)BSP\_IO\_ET0\_MDC

| #define BSP\_IO\_ET0\_MDC   0xFFFF0F01 /\* ET0\_MDC \*/ |
| --- |

## [◆ ](#affb6069f81f4969760515ff6e6afb11c)BSP\_IO\_ET0\_MDIO

| #define BSP\_IO\_ET0\_MDIO   0xFFFF0F00 /\* ET0\_MDIO \*/ |
| --- |

## [◆ ](#a23526264c453ac5d6f24812eb21223c6)BSP\_IO\_ET0\_RXC\_RXCLK

| #define BSP\_IO\_ET0\_RXC\_RXCLK   0xFFFF1004 /\* ET0\_RXC\_RXCLK \*/ |
| --- |

## [◆ ](#ad98aa0cf398a7a717e1bc4e74a1903ae)BSP\_IO\_ET0\_RXCTL\_RXDV

| #define BSP\_IO\_ET0\_RXCTL\_RXDV   0xFFFF1000 /\* ET0\_RXCTL\_RXDV \*/ |
| --- |

## [◆ ](#a258ab4720e4e79dbf89825f6ad9a8b64)BSP\_IO\_ET0\_RXD0

| #define BSP\_IO\_ET0\_RXD0   0xFFFF1104 /\* ET0\_RXD0 \*/ |
| --- |

## [◆ ](#a24752e5ec875f68c121cb6e11242f7ec)BSP\_IO\_ET0\_RXD1

| #define BSP\_IO\_ET0\_RXD1   0xFFFF1105 /\* ET0\_RXD1 \*/ |
| --- |

## [◆ ](#a599fb60443fe1616d80be533bdd94fb8)BSP\_IO\_ET0\_RXD2

| #define BSP\_IO\_ET0\_RXD2   0xFFFF1106 /\* ET0\_RXD2 \*/ |
| --- |

## [◆ ](#a8d8da7f1833fd91359378c44eb02d0a7)BSP\_IO\_ET0\_RXD3

| #define BSP\_IO\_ET0\_RXD3   0xFFFF1107 /\* ET0\_RXD3 \*/ |
| --- |

## [◆ ](#a4674592e231ba8d6f40eb394a60feb0f)BSP\_IO\_ET0\_RXER

| #define BSP\_IO\_ET0\_RXER   0xFFFF1003 /\* ET0\_RXER \*/ |
| --- |

## [◆ ](#a96ce0ec77d5903e518aac3bd0a185444)BSP\_IO\_ET0\_TXC\_TXCLK

| #define BSP\_IO\_ET0\_TXC\_TXCLK   0xFFFF1005 /\* ET0\_TXC\_TXCLK \*/ |
| --- |

## [◆ ](#a1ff3549a67af86d6e3f7b059a92a2afb)BSP\_IO\_ET0\_TXCTL\_TXEN

| #define BSP\_IO\_ET0\_TXCTL\_TXEN   0xFFFF1001 /\* ET0\_TXCTL\_TXEN \*/ |
| --- |

## [◆ ](#a4b602637a9544fa6a9d0078df0bdec75)BSP\_IO\_ET0\_TXD0

| #define BSP\_IO\_ET0\_TXD0   0xFFFF1100 /\* ET0\_TXD0 \*/ |
| --- |

## [◆ ](#ae6488452648a6a299a2c7769fefd62cb)BSP\_IO\_ET0\_TXD1

| #define BSP\_IO\_ET0\_TXD1   0xFFFF1101 /\* ET0\_TXD1 \*/ |
| --- |

## [◆ ](#a427e1641f737920d7e21cc672a44e15e)BSP\_IO\_ET0\_TXD2

| #define BSP\_IO\_ET0\_TXD2   0xFFFF1102 /\* ET0\_TXD2 \*/ |
| --- |

## [◆ ](#ab85a510df46ba7bfc34f6ac9763c570f)BSP\_IO\_ET0\_TXD3

| #define BSP\_IO\_ET0\_TXD3   0xFFFF1103 /\* ET0\_TXD3 \*/ |
| --- |

## [◆ ](#a37987476f631345e932456c515be0640)BSP\_IO\_ET0\_TXER

| #define BSP\_IO\_ET0\_TXER   0xFFFF1002 /\* ET0\_TXER \*/ |
| --- |

## [◆ ](#ab0efa2e81b694ed26776990f9518b957)BSP\_IO\_ET1\_COL

| #define BSP\_IO\_ET1\_COL   0xFFFF1307 /\* ET1\_COL \*/ |
| --- |

## [◆ ](#af3bcd5eed4d57df86fa85a28624d29b8)BSP\_IO\_ET1\_CRS

| #define BSP\_IO\_ET1\_CRS   0xFFFF1306 /\* ET1\_CRS \*/ |
| --- |

## [◆ ](#ae6d4060ae6fd6c05379be5d7edc8f2f0)BSP\_IO\_ET1\_MDC

| #define BSP\_IO\_ET1\_MDC   0xFFFF1201 /\* ET1\_MDC \*/ |
| --- |

## [◆ ](#ac0117e2fb0c9dfdc2cc46a24324c6455)BSP\_IO\_ET1\_MDIO

| #define BSP\_IO\_ET1\_MDIO   0xFFFF1200 /\* ET1\_MDIO \*/ |
| --- |

## [◆ ](#a8668737f90448aa6808f27159ee61419)BSP\_IO\_ET1\_RXC\_RXCLK

| #define BSP\_IO\_ET1\_RXC\_RXCLK   0xFFFF1304 /\* ET1\_RXC\_RXCLK \*/ |
| --- |

## [◆ ](#ac55eaa22c0834db36089216d261bcf7c)BSP\_IO\_ET1\_RXCTL\_RXDV

| #define BSP\_IO\_ET1\_RXCTL\_RXDV   0xFFFF1300 /\* ET1\_RXCTL\_RXDV \*/ |
| --- |

## [◆ ](#a7c7254de0259532616470d19e7752092)BSP\_IO\_ET1\_RXD0

| #define BSP\_IO\_ET1\_RXD0   0xFFFF1404 /\* ET1\_RXD0 \*/ |
| --- |

## [◆ ](#a45f3b9373a5d693c7296c75c09b1d7b0)BSP\_IO\_ET1\_RXD1

| #define BSP\_IO\_ET1\_RXD1   0xFFFF1405 /\* ET1\_RXD1 \*/ |
| --- |

## [◆ ](#a2fa85dd0820d0544fe0bc2a69d3cf1d6)BSP\_IO\_ET1\_RXD2

| #define BSP\_IO\_ET1\_RXD2   0xFFFF1406 /\* ET1\_RXD2 \*/ |
| --- |

## [◆ ](#ac74ad60939668d2e07308a7ddc24f73c)BSP\_IO\_ET1\_RXD3

| #define BSP\_IO\_ET1\_RXD3   0xFFFF1407 /\* ET1\_RXD3 \*/ |
| --- |

## [◆ ](#ad1af1ded92a3d3e9b1e30b92961611f0)BSP\_IO\_ET1\_RXER

| #define BSP\_IO\_ET1\_RXER   0xFFFF1303 /\* ET1\_RXER \*/ |
| --- |

## [◆ ](#a37e6c627995f864631cfe90f516e937c)BSP\_IO\_ET1\_TXC\_TXCLK

| #define BSP\_IO\_ET1\_TXC\_TXCLK   0xFFFF1305 /\* ET1\_TXC\_TXCLK \*/ |
| --- |

## [◆ ](#a02c3411d7e0bb049d555f52ca9cb3f25)BSP\_IO\_ET1\_TXCTL\_TXEN

| #define BSP\_IO\_ET1\_TXCTL\_TXEN   0xFFFF1301 /\* ET1\_TXCTL\_TXEN \*/ |
| --- |

## [◆ ](#a11416ba84899fc19457cfb83f1b0aafa)BSP\_IO\_ET1\_TXD0

| #define BSP\_IO\_ET1\_TXD0   0xFFFF1400 /\* ET1\_TXD0 \*/ |
| --- |

## [◆ ](#ad7cc67151309c413bd542d957064b5c1)BSP\_IO\_ET1\_TXD1

| #define BSP\_IO\_ET1\_TXD1   0xFFFF1401 /\* ET1\_TXD1 \*/ |
| --- |

## [◆ ](#a4624d11a09f7120ef0ca1ff6ad18dfe7)BSP\_IO\_ET1\_TXD2

| #define BSP\_IO\_ET1\_TXD2   0xFFFF1402 /\* ET1\_TXD2 \*/ |
| --- |

## [◆ ](#a1472a2198a99a29571ad223cdd6b4026)BSP\_IO\_ET1\_TXD3

| #define BSP\_IO\_ET1\_TXD3   0xFFFF1403 /\* ET1\_TXD3 \*/ |
| --- |

## [◆ ](#a169635733406399a183046fec986cfbb)BSP\_IO\_ET1\_TXER

| #define BSP\_IO\_ET1\_TXER   0xFFFF1302 /\* ET1\_TXER \*/ |
| --- |

## [◆ ](#a5a8b4d2cdc15f25cc0b58db97c539b2a)BSP\_IO\_NMI

| #define BSP\_IO\_NMI   0xFFFF0100 /\* NMI \*/ |
| --- |

## [◆ ](#a8b035e432c4d35e80e18046c2965b21d)BSP\_IO\_PCIE0\_RSTOUTB

| #define BSP\_IO\_PCIE0\_RSTOUTB   0xFFFF0E00 /\* PCIE0\_RSTOUTB \*/ |
| --- |

## [◆ ](#a99c0ba673dd1a5f776043196b3a5a984)BSP\_IO\_PCIE1\_RSTOUTB

| #define BSP\_IO\_PCIE1\_RSTOUTB   0xFFFF0E01 /\* PCIE1\_RSTOUTB \*/ |
| --- |

## [◆ ](#a471d8bb707e4a89559be0b5111b85db9)BSP\_IO\_SCIF\_RXD

| #define BSP\_IO\_SCIF\_RXD   0xFFFF0600 /\* SCIF\_RXD \*/ |
| --- |

## [◆ ](#a796a4aeccb790011b04612464f2cb4a8)BSP\_IO\_SCIF\_TXD

| #define BSP\_IO\_SCIF\_TXD   0xFFFF0601 /\* SCIF\_TXD \*/ |
| --- |

## [◆ ](#aaa12b2c5e1e98e3c10274d74dd8b5355)BSP\_IO\_SD0CLK

| #define BSP\_IO\_SD0CLK   0xFFFF0900 /\* SD0CLK \*/ |
| --- |

## [◆ ](#a7c2a7b6e2b4b7d59d70cad16bb1643f9)BSP\_IO\_SD0CMD

| #define BSP\_IO\_SD0CMD   0xFFFF0901 /\* SD0CMD \*/ |
| --- |

## [◆ ](#a00b9658c97f4ccb1c297a035ad23373b)BSP\_IO\_SD0DAT0

| #define BSP\_IO\_SD0DAT0   0xFFFF0A00 /\* SD0DAT0 \*/ |
| --- |

## [◆ ](#a4a30feece071a0aa2dcfb24e9a479f73)BSP\_IO\_SD0DAT1

| #define BSP\_IO\_SD0DAT1   0xFFFF0A01 /\* SD0DAT1 \*/ |
| --- |

## [◆ ](#adb6cf77200d6a1fd93f0f2a402d08b6e)BSP\_IO\_SD0DAT2

| #define BSP\_IO\_SD0DAT2   0xFFFF0A02 /\* SD0DAT2 \*/ |
| --- |

## [◆ ](#a0b4facd2f842db7c229512921db7a9cd)BSP\_IO\_SD0DAT3

| #define BSP\_IO\_SD0DAT3   0xFFFF0A03 /\* SD0DAT3 \*/ |
| --- |

## [◆ ](#a92fc90bf3dd81a609e2b970a0c6e58f4)BSP\_IO\_SD0DAT4

| #define BSP\_IO\_SD0DAT4   0xFFFF0A04 /\* SD0DAT4 \*/ |
| --- |

## [◆ ](#a5d08d8333c7059b4184431a2ad6dce00)BSP\_IO\_SD0DAT5

| #define BSP\_IO\_SD0DAT5   0xFFFF0A05 /\* SD0DAT5 \*/ |
| --- |

## [◆ ](#a1395add1e4783d3d16adf13e9c043329)BSP\_IO\_SD0DAT6

| #define BSP\_IO\_SD0DAT6   0xFFFF0A06 /\* SD0DAT6 \*/ |
| --- |

## [◆ ](#aad08493d9205abfd23c9f6318b3fadf9)BSP\_IO\_SD0DAT7

| #define BSP\_IO\_SD0DAT7   0xFFFF0A07 /\* SD0DAT7 \*/ |
| --- |

## [◆ ](#a36f139827da1deed0cda643110fc433c)BSP\_IO\_SD0RSTN

| #define BSP\_IO\_SD0RSTN   0xFFFF0902 /\* SD0RSTN \*/ |
| --- |

## [◆ ](#ab78ba53890588fcecb5c969bb4528c2f)BSP\_IO\_SD1CLK

| #define BSP\_IO\_SD1CLK   0xFFFF0B00 /\* SD1CLK \*/ |
| --- |

## [◆ ](#a53b15de62883dda6d2f19ac613bdc389)BSP\_IO\_SD1CMD

| #define BSP\_IO\_SD1CMD   0xFFFF0B01 /\* SD1CMD \*/ |
| --- |

## [◆ ](#ab34dd59d23acde42b9613c84c0d295e2)BSP\_IO\_SD1DAT0

| #define BSP\_IO\_SD1DAT0   0xFFFF0C00 /\* SD1DAT0 \*/ |
| --- |

## [◆ ](#a92ba6c595074ded1609365e5dbcb1a6c)BSP\_IO\_SD1DAT1

| #define BSP\_IO\_SD1DAT1   0xFFFF0C01 /\* SD1DAT1 \*/ |
| --- |

## [◆ ](#a88221cb800114c0f4fe6e8f98246ada0)BSP\_IO\_SD1DAT2

| #define BSP\_IO\_SD1DAT2   0xFFFF0C02 /\* SD1DAT2 \*/ |
| --- |

## [◆ ](#a32f2ab4b2678393032f582cc2abf2ef0)BSP\_IO\_SD1DAT3

| #define BSP\_IO\_SD1DAT3   0xFFFF0C03 /\* SD1DAT3 \*/ |
| --- |

## [◆ ](#a318b423b2efc8ab1a3de0a8f9ab3eeca)BSP\_IO\_TDO

| #define BSP\_IO\_TDO   0xFFFF0302 /\* TDO \*/ |
| --- |

## [◆ ](#af06a8358900119f6b4c3d91e465ce22f)BSP\_IO\_TMS\_SWDIO

| #define BSP\_IO\_TMS\_SWDIO   0xFFFF0300 /\* TMS\_SWDIO \*/ |
| --- |

## [◆ ](#ac2edcba3708e5888a80b390c1f55adb0)BSP\_IO\_WDTUDFCA

| #define BSP\_IO\_WDTUDFCA   0xFFFF0500 /\* WDTUDFCA \*/ |
| --- |

## [◆ ](#a17ee049758d71222d20196df52b893b7)BSP\_IO\_WDTUDFCM

| #define BSP\_IO\_WDTUDFCM   0xFFFF0501 /\* WDTUDFCM \*/ |
| --- |

## [◆ ](#a6d2fa31046fc5e52deb6ebc62cea4688)BSP\_IO\_XSPI0\_CKN

| #define BSP\_IO\_XSPI0\_CKN   0xFFFF0701 /\* XSPI0\_CKN \*/ |
| --- |

## [◆ ](#a7fd026b6ffc6db6ccb085d600046ab50)BSP\_IO\_XSPI0\_CKP

| #define BSP\_IO\_XSPI0\_CKP   0xFFFF0700 /\* XSPI0\_CKP \*/ |
| --- |

## [◆ ](#a154ea1f0b0ff649fc61c3f64fa0bd69e)BSP\_IO\_XSPI0\_CS0N

| #define BSP\_IO\_XSPI0\_CS0N   0xFFFF0702 /\* XSPI0\_CS0N \*/ |
| --- |

## [◆ ](#af9862a3a0391b96398c6feeb266e454a)BSP\_IO\_XSPI0\_DS

| #define BSP\_IO\_XSPI0\_DS   0xFFFF0703 /\* XSPI0\_DS \*/ |
| --- |

## [◆ ](#abb95c2dac4b836de5a2feed73360bbc7)BSP\_IO\_XSPI0\_ECS0N

| #define BSP\_IO\_XSPI0\_ECS0N   0xFFFF0707 /\* XSPI0\_ECS0N \*/ |
| --- |

## [◆ ](#a93da56bce0940882dcbec1217ab2528a)BSP\_IO\_XSPI0\_INT0N

| #define BSP\_IO\_XSPI0\_INT0N   0xFFFF0706 /\* XSPI0\_INT0N \*/ |
| --- |

## [◆ ](#a4d2dfc310f6cddd4180f492afa424195)BSP\_IO\_XSPI0\_IO0

| #define BSP\_IO\_XSPI0\_IO0   0xFFFF0800 /\* XSPI0\_IO0 \*/ |
| --- |

## [◆ ](#a508e71fd569e26596c6b67d3f1272960)BSP\_IO\_XSPI0\_IO1

| #define BSP\_IO\_XSPI0\_IO1   0xFFFF0801 /\* XSPI0\_IO1 \*/ |
| --- |

## [◆ ](#a4dd807715c8b53fc9230285b7f9a27ce)BSP\_IO\_XSPI0\_IO2

| #define BSP\_IO\_XSPI0\_IO2   0xFFFF0802 /\* XSPI0\_IO2 \*/ |
| --- |

## [◆ ](#a06e205e34bb3b58e82f8996f5fa2d149)BSP\_IO\_XSPI0\_IO3

| #define BSP\_IO\_XSPI0\_IO3   0xFFFF0803 /\* XSPI0\_IO3 \*/ |
| --- |

## [◆ ](#a287a1b337f71412dcde0aba38a37f0bd)BSP\_IO\_XSPI0\_IO4

| #define BSP\_IO\_XSPI0\_IO4   0xFFFF0804 /\* XSPI0\_IO4 \*/ |
| --- |

## [◆ ](#ad533760a2339c31dc4205b357b62cb0c)BSP\_IO\_XSPI0\_IO5

| #define BSP\_IO\_XSPI0\_IO5   0xFFFF0805 /\* XSPI0\_IO5 \*/ |
| --- |

## [◆ ](#a5df9b361f9ea59a0bbbeca44a17199e9)BSP\_IO\_XSPI0\_IO6

| #define BSP\_IO\_XSPI0\_IO6   0xFFFF0806 /\* XSPI0\_IO6 \*/ |
| --- |

## [◆ ](#aaa8a2e7aab31cfd5cec926270aeab322)BSP\_IO\_XSPI0\_IO7

| #define BSP\_IO\_XSPI0\_IO7   0xFFFF0807 /\* XSPI0\_IO7 \*/ |
| --- |

## [◆ ](#afb70b7ffeb25be4e91d5782699913fd1)BSP\_IO\_XSPI0\_RESET0N

| #define BSP\_IO\_XSPI0\_RESET0N   0xFFFF0704 /\* XSPI0\_RESET0N \*/ |
| --- |

## [◆ ](#aba5df3d7f44c4afc1e88d25cad744696)BSP\_IO\_XSPI0\_RSTO0N

| #define BSP\_IO\_XSPI0\_RSTO0N   0xFFFF0705 /\* XSPI0\_RSTO0N \*/ |
| --- |

## [◆ ](#a1b0292747e92dff43d6760d9e2258869)PORT\_00

| #define PORT\_00   0x0000 /\* IO port 0 \*/ |
| --- |

## [◆ ](#a9de415830a2b3484dd33d5d08258dde5)PORT\_01

| #define PORT\_01   0x0100 /\* IO port 1 \*/ |
| --- |

## [◆ ](#a7db623b2ec3816113a8f3fb07d5428ef)PORT\_02

| #define PORT\_02   0x0200 /\* IO port 2 \*/ |
| --- |

## [◆ ](#a71478a4563d986886410618bc130b0d9)PORT\_03

| #define PORT\_03   0x0300 /\* IO port 3 \*/ |
| --- |

## [◆ ](#aed73b97fc12615ac1dec9daad9537647)PORT\_04

| #define PORT\_04   0x0400 /\* IO port 4 \*/ |
| --- |

## [◆ ](#a590020a2e6577d74d89bdee0989812c4)PORT\_05

| #define PORT\_05   0x0500 /\* IO port 5 \*/ |
| --- |

## [◆ ](#ab2912aeb54c92971e0590ff3282e775b)PORT\_06

| #define PORT\_06   0x0600 /\* IO port 6 \*/ |
| --- |

## [◆ ](#acabb0398db58703c47e718f899018410)PORT\_07

| #define PORT\_07   0x0700 /\* IO port 7 \*/ |
| --- |

## [◆ ](#a5f4d0cfbea4e649fa0863d4a8d409c5e)PORT\_08

| #define PORT\_08   0x0800 /\* IO port 8 \*/ |
| --- |

## [◆ ](#a5e8d840d1a1bd421615b2cc90ce0b90f)PORT\_09

| #define PORT\_09   0x0900 /\* IO port 9 \*/ |
| --- |

## [◆ ](#a4c39a294d7b3a360c172b65151a5bfc8)PORT\_10

| #define PORT\_10   0x0A00 /\* IO port 10 \*/ |
| --- |

## [◆ ](#abeebf6334cb5240b09d97d35fc0128f3)PORT\_11

| #define PORT\_11   0x0B00 /\* IO port 11 \*/ |
| --- |

## [◆ ](#ad1e144b7c5bf2d735a74f4bf84a58561)RZV\_FILCLKSEL\_DIV\_18000

| #define RZV\_FILCLKSEL\_DIV\_18000   2 |
| --- |

## [◆ ](#a5cb812371774b2162d5b6f71d3422c19)RZV\_FILCLKSEL\_DIV\_36000

| #define RZV\_FILCLKSEL\_DIV\_36000   3 |
| --- |

## [◆ ](#a43a5dfaf850006746e679e73a414e446)RZV\_FILCLKSEL\_DIV\_9000

| #define RZV\_FILCLKSEL\_DIV\_9000   1 |
| --- |

## [◆ ](#abac8582aa87640663955060639507ade)RZV\_FILCLKSEL\_NOT\_DIV

| #define RZV\_FILCLKSEL\_NOT\_DIV   0 |
| --- |

## [◆ ](#ab3b284fd4bd5a16a2ea1d83116832cd2)RZV\_FILNUM\_12\_STAGE

| #define RZV\_FILNUM\_12\_STAGE   2 |
| --- |

## [◆ ](#a12034f75c3817d20962999b9040caca6)RZV\_FILNUM\_16\_STAGE

| #define RZV\_FILNUM\_16\_STAGE   3 |
| --- |

## [◆ ](#a474313de5067232584bb66a293cceef1)RZV\_FILNUM\_4\_STAGE

| #define RZV\_FILNUM\_4\_STAGE   0 |
| --- |

## [◆ ](#ab51d90be14e4d81c38c4cfa620270b64)RZV\_FILNUM\_8\_STAGE

| #define RZV\_FILNUM\_8\_STAGE   1 |
| --- |

## [◆ ](#a038292c08044da9e82019e7aa73abf1c)RZV\_FILTER\_SET

| #define RZV\_FILTER\_SET | ( |  | *filnum*, |
| --- | --- | --- | --- |
|  |  |  | *filclksel* ) |

**Value:**

(((filnum) & 0x3) << 0x2) | (filclksel & 0x3)

## [◆ ](#ace27a9fee40fcee657b3aff941b3ac6b)RZV\_PINMUX

| #define RZV\_PINMUX | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin*, |
|  |  |  | *func* ) |

**Value:**

(port | pin | (func << 4))

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [pinctrl](dir_2c6c4fbd167577104b7f1b7148586168.md)
- [renesas](dir_17f48eb154be6cea623223db5de209e7.md)
- [pinctrl-rzv2h.h](pinctrl-rzv2h_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
