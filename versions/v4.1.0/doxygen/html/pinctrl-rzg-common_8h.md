---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/pinctrl-rzg-common_8h.html
original_path: doxygen/html/pinctrl-rzg-common_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

pinctrl-rzg-common.h File Reference

[Go to the source code of this file.](pinctrl-rzg-common_8h_source.md)

| Macros | |
| --- | --- |
| #define | [PORT\_00](#a1b0292747e92dff43d6760d9e2258869)   0x0000 /\* IO port 0 \*/ |
| #define | [PORT\_01](#a9de415830a2b3484dd33d5d08258dde5)   0x1000 /\* IO port 1 \*/ |
| #define | [PORT\_02](#a7db623b2ec3816113a8f3fb07d5428ef)   0x1100 /\* IO port 2 \*/ |
| #define | [PORT\_03](#a71478a4563d986886410618bc130b0d9)   0x1200 /\* IO port 3 \*/ |
| #define | [PORT\_04](#aed73b97fc12615ac1dec9daad9537647)   0x1300 /\* IO port 4 \*/ |
| #define | [PORT\_05](#a590020a2e6577d74d89bdee0989812c4)   0x0100 /\* IO port 5 \*/ |
| #define | [PORT\_06](#ab2912aeb54c92971e0590ff3282e775b)   0x0200 /\* IO port 6 \*/ |
| #define | [PORT\_07](#acabb0398db58703c47e718f899018410)   0x1400 /\* IO port 7 \*/ |
| #define | [PORT\_08](#a5f4d0cfbea4e649fa0863d4a8d409c5e)   0x1500 /\* IO port 8 \*/ |
| #define | [PORT\_09](#a5e8d840d1a1bd421615b2cc90ce0b90f)   0x1600 /\* IO port 9 \*/ |
| #define | [PORT\_10](#a4c39a294d7b3a360c172b65151a5bfc8)   0x1700 /\* IO port 10 \*/ |
| #define | [PORT\_11](#abeebf6334cb5240b09d97d35fc0128f3)   0x0300 /\* IO port 11 \*/ |
| #define | [PORT\_12](#ae57c3ffa4df15481a9a219e16b011ef3)   0x0400 /\* IO port 12 \*/ |
| #define | [PORT\_13](#ae76dfcae2263b7d43d1ee23fa9548293)   0x0500 /\* IO port 13 \*/ |
| #define | [PORT\_14](#a9c8783d66b07c093c559a5fd74add129)   0x0600 /\* IO port 14 \*/ |
| #define | [PORT\_15](#aeb88886b16b5a8ea23147000fd9af3cc)   0x0700 /\* IO port 15 \*/ |
| #define | [PORT\_16](#aa9fff44f99e434f31b19ed55462b45d4)   0x0800 /\* IO port 16 \*/ |
| #define | [PORT\_17](#a8ce8fd8ca6cdbc375b70a0b7d53eb315)   0x0900 /\* IO port 17 \*/ |
| #define | [PORT\_18](#a51b6b92e7f3238a410526b67234f77d7)   0x0A00 /\* IO port 18 \*/ |
| #define | [RZG\_PINMUX](#a02f280ee325bc9e66e5566f8d6f3feec)(port, pin, func) |
| #define | [BSP\_IO\_NMI](#a5a8b4d2cdc15f25cc0b58db97c539b2a)   0xFFFF0000 /\* NMI \*/ |
| #define | [BSP\_IO\_TMS\_SWDIO](#af06a8358900119f6b4c3d91e465ce22f)   0xFFFF0100 /\* TMS\_SWDIO \*/ |
| #define | [BSP\_IO\_TDO](#a318b423b2efc8ab1a3de0a8f9ab3eeca)   0xFFFF0101 /\* TDO \*/ |
| #define | [BSP\_IO\_AUDIO\_CLK1](#acf9b257ce3e3a66bcfa8d4aca427c0bf)   0xFFFF0200 /\* AUDIO\_CLK1 \*/ |
| #define | [BSP\_IO\_AUDIO\_CLK2](#a98d349e2311d1571d490e26866871b16)   0xFFFF0201 /\* AUDIO\_CLK2 \*/ |
| #define | [BSP\_IO\_XSPI\_SPCLK](#ae349e2b4add4664859e2c87e7eb47e15)   0xFFFF0400 /\* XSPI\_SPCLK \*/ |
| #define | [BSP\_IO\_XSPI\_RESET\_N](#a1938aca3788d42e557a35c20517f9dd8)   0xFFFF0401 /\* XSPI\_RESET\_N \*/ |
| #define | [BSP\_IO\_XSPI\_WP\_N](#a73759a3f08a6b48278607de2f63cf523)   0xFFFF0402 /\* XSPI\_WP\_N \*/ |
| #define | [BSP\_IO\_XSPI\_DS](#a019fd571a275deaf0570c317b9a20b97)   0xFFFF0403 /\* XSPI\_DS \*/ |
| #define | [BSP\_IO\_XSPI\_CS0\_N](#a2356e340dbc38e7d62351b8996b40c1e)   0xFFFF0404 /\* XSPI\_CS0\_N \*/ |
| #define | [BSP\_IO\_XSPI\_CS1\_N](#a973dd3ba73dbb9b3c93d3f715c4dd6c0)   0xFFFF0405 /\* XSPI\_CS1\_N \*/ |
| #define | [BSP\_IO\_XSPI\_IO0](#a19da009b51eb3891a92ef39c13019567)   0xFFFF0500 /\* XSPI\_IO0 \*/ |
| #define | [BSP\_IO\_XSPI\_IO1](#a3ea0b2836c786211aa5643b7bce971c2)   0xFFFF0501 /\* XSPI\_IO1 \*/ |
| #define | [BSP\_IO\_XSPI\_IO2](#af0814f9594ef180d9dbb3e910118cb39)   0xFFFF0502 /\* XSPI\_IO2 \*/ |
| #define | [BSP\_IO\_XSPI\_IO3](#ae39cf1fdec8f1940030b962fd91895ec)   0xFFFF0503 /\* XSPI\_IO3 \*/ |
| #define | [BSP\_IO\_XSPI\_IO4](#ade455522c2e4df9f6a3d4335898c5a2e)   0xFFFF0504 /\* XSPI\_IO4 \*/ |
| #define | [BSP\_IO\_XSPI\_IO5](#afd88724051491fb938adc876ce9f8094)   0xFFFF0505 /\* XSPI\_IO5 \*/ |
| #define | [BSP\_IO\_XSPI\_IO6](#ae4047cb2b38a2388ac3ad4a73b438348)   0xFFFF0506 /\* XSPI\_IO6 \*/ |
| #define | [BSP\_IO\_XSPI\_IO7](#a0839e73ff018a83849befdf6c1fa9cbf)   0xFFFF0507 /\* XSPI\_IO7 \*/ |
| #define | [BSP\_IO\_WDTOVF\_PERROUT](#a7c1efa402066677442bffceaa874e002)   0xFFFF0600 /\* WDTOVF\_PERROUT \*/ |
| #define | [BSP\_IO\_I3C\_SDA](#a7ef3de361b4eaab1e199ac28454233cd)   0xFFFF0900 /\* I3C\_SDA \*/ |
| #define | [BSP\_IO\_I3C\_SCL](#a67faf3a17f6e0d6fc75671829942072d)   0xFFFF0901 /\* I3C\_SCL \*/ |
| #define | [BSP\_IO\_SD0\_CLK](#a99cac86447ae6b18e3e1601085623a60)   0xFFFF1000 /\* CD0\_CLK \*/ |
| #define | [BSP\_IO\_SD0\_CMD](#a2b904f716e2bf524351430155b8c7ddc)   0xFFFF1001 /\* CD0\_CMD \*/ |
| #define | [BSP\_IO\_SD0\_RST\_N](#ad61d120b88812e3c41a600414f553325)   0xFFFF1002 /\* CD0\_RST\_N \*/ |
| #define | [BSP\_IO\_SD0\_DATA0](#a1f4951bb275e24732e8487dffd5fe69a)   0xFFFF1100 /\* SD0\_DATA0 \*/ |
| #define | [BSP\_IO\_SD0\_DATA1](#a97428f756c92136fd0f3d34f520c760b)   0xFFFF1101 /\* SD0\_DATA1 \*/ |
| #define | [BSP\_IO\_SD0\_DATA2](#a77fab2fb18ce2a3d779d94b54e8d58d1)   0xFFFF1102 /\* SD0\_DATA2 \*/ |
| #define | [BSP\_IO\_SD0\_DATA3](#a8794e04fe7b7d3d895973cac59538095)   0xFFFF1103 /\* SD0\_DATA3 \*/ |
| #define | [BSP\_IO\_SD0\_DATA4](#a9398ade50c886958f0b51b41a9c4849b)   0xFFFF1104 /\* SD0\_DATA4 \*/ |
| #define | [BSP\_IO\_SD0\_DATA5](#ae127f16b4b223229c57375a20ad2a442)   0xFFFF1105 /\* SD0\_DATA5 \*/ |
| #define | [BSP\_IO\_SD0\_DATA6](#af64543688eccd90de6b9086ccd72e3fd)   0xFFFF1106 /\* SD0\_DATA6 \*/ |
| #define | [BSP\_IO\_SD0\_DATA7](#a1e39def829ae82ed38ddbd0f01d9b62f)   0xFFFF1107 /\* SD0\_DATA7 \*/ |
| #define | [BSP\_IO\_SD1\_CLK](#a21e34df07c258c73258ba42eeab62fee)   0xFFFF1200 /\* SD1\_CLK \*/ |
| #define | [BSP\_IO\_SD1\_CMD](#a03e82210e0063b35e7e3a877a6dbd17e)   0xFFFF1201 /\* SD1\_CMD \*/ |
| #define | [BSP\_IO\_SD1\_DATA0](#a8e6b818ecfdfbd9c8c571720711d35dd)   0xFFFF1300 /\* SD1\_DATA0 \*/ |
| #define | [BSP\_IO\_SD1\_DATA1](#a222474e671dc0196e027b741bfb6bef2)   0xFFFF1301 /\* SD1\_DATA1 \*/ |
| #define | [BSP\_IO\_SD1\_DATA2](#ab404c31fb4de4e9c80ffd9cd3d93b7ca)   0xFFFF1302 /\* SD1\_DATA2 \*/ |
| #define | [BSP\_IO\_SD1\_DATA3](#acb12cf7cf433e72dd141c6652be9d9af)   0xFFFF1303 /\* SD1\_DATA3 \*/ |
| #define | [RZG\_FILNUM\_4\_STAGE](#a410e1db2102a72b3222f3f87e9191b36)   0 |
| #define | [RZG\_FILNUM\_8\_STAGE](#a7ec85695dd35462b15784cf869e2ecdd)   1 |
| #define | [RZG\_FILNUM\_12\_STAGE](#a7fb5e17c2033f7de03440445de58497d)   2 |
| #define | [RZG\_FILNUM\_16\_STAGE](#a4c3d0f96e45fcff456391291544c2d7e)   3 |
| #define | [RZG\_FILCLKSEL\_NOT\_DIV](#aebf11f5c29f9d62a4bc6076430f5af74)   0 |
| #define | [RZG\_FILCLKSEL\_DIV\_9000](#a6fc19ace82becb78720423edd9a80f03)   1 |
| #define | [RZG\_FILCLKSEL\_DIV\_18000](#a82fe6b7f1ba59ab812683890fa2f0e7c)   2 |
| #define | [RZG\_FILCLKSEL\_DIV\_36000](#acecffc879cdcd14232b7cc2714e46e8f)   3 |
| #define | [RZG\_FILTER\_SET](#abe4747778068dd33b142d7a891ca901e)(filnum, filclksel) |

## Macro Definition Documentation

## [◆ ](#acf9b257ce3e3a66bcfa8d4aca427c0bf)BSP\_IO\_AUDIO\_CLK1

| #define BSP\_IO\_AUDIO\_CLK1   0xFFFF0200 /\* AUDIO\_CLK1 \*/ |
| --- |

## [◆ ](#a98d349e2311d1571d490e26866871b16)BSP\_IO\_AUDIO\_CLK2

| #define BSP\_IO\_AUDIO\_CLK2   0xFFFF0201 /\* AUDIO\_CLK2 \*/ |
| --- |

## [◆ ](#a67faf3a17f6e0d6fc75671829942072d)BSP\_IO\_I3C\_SCL

| #define BSP\_IO\_I3C\_SCL   0xFFFF0901 /\* I3C\_SCL \*/ |
| --- |

## [◆ ](#a7ef3de361b4eaab1e199ac28454233cd)BSP\_IO\_I3C\_SDA

| #define BSP\_IO\_I3C\_SDA   0xFFFF0900 /\* I3C\_SDA \*/ |
| --- |

## [◆ ](#a5a8b4d2cdc15f25cc0b58db97c539b2a)BSP\_IO\_NMI

| #define BSP\_IO\_NMI   0xFFFF0000 /\* NMI \*/ |
| --- |

## [◆ ](#a99cac86447ae6b18e3e1601085623a60)BSP\_IO\_SD0\_CLK

| #define BSP\_IO\_SD0\_CLK   0xFFFF1000 /\* CD0\_CLK \*/ |
| --- |

## [◆ ](#a2b904f716e2bf524351430155b8c7ddc)BSP\_IO\_SD0\_CMD

| #define BSP\_IO\_SD0\_CMD   0xFFFF1001 /\* CD0\_CMD \*/ |
| --- |

## [◆ ](#a1f4951bb275e24732e8487dffd5fe69a)BSP\_IO\_SD0\_DATA0

| #define BSP\_IO\_SD0\_DATA0   0xFFFF1100 /\* SD0\_DATA0 \*/ |
| --- |

## [◆ ](#a97428f756c92136fd0f3d34f520c760b)BSP\_IO\_SD0\_DATA1

| #define BSP\_IO\_SD0\_DATA1   0xFFFF1101 /\* SD0\_DATA1 \*/ |
| --- |

## [◆ ](#a77fab2fb18ce2a3d779d94b54e8d58d1)BSP\_IO\_SD0\_DATA2

| #define BSP\_IO\_SD0\_DATA2   0xFFFF1102 /\* SD0\_DATA2 \*/ |
| --- |

## [◆ ](#a8794e04fe7b7d3d895973cac59538095)BSP\_IO\_SD0\_DATA3

| #define BSP\_IO\_SD0\_DATA3   0xFFFF1103 /\* SD0\_DATA3 \*/ |
| --- |

## [◆ ](#a9398ade50c886958f0b51b41a9c4849b)BSP\_IO\_SD0\_DATA4

| #define BSP\_IO\_SD0\_DATA4   0xFFFF1104 /\* SD0\_DATA4 \*/ |
| --- |

## [◆ ](#ae127f16b4b223229c57375a20ad2a442)BSP\_IO\_SD0\_DATA5

| #define BSP\_IO\_SD0\_DATA5   0xFFFF1105 /\* SD0\_DATA5 \*/ |
| --- |

## [◆ ](#af64543688eccd90de6b9086ccd72e3fd)BSP\_IO\_SD0\_DATA6

| #define BSP\_IO\_SD0\_DATA6   0xFFFF1106 /\* SD0\_DATA6 \*/ |
| --- |

## [◆ ](#a1e39def829ae82ed38ddbd0f01d9b62f)BSP\_IO\_SD0\_DATA7

| #define BSP\_IO\_SD0\_DATA7   0xFFFF1107 /\* SD0\_DATA7 \*/ |
| --- |

## [◆ ](#ad61d120b88812e3c41a600414f553325)BSP\_IO\_SD0\_RST\_N

| #define BSP\_IO\_SD0\_RST\_N   0xFFFF1002 /\* CD0\_RST\_N \*/ |
| --- |

## [◆ ](#a21e34df07c258c73258ba42eeab62fee)BSP\_IO\_SD1\_CLK

| #define BSP\_IO\_SD1\_CLK   0xFFFF1200 /\* SD1\_CLK \*/ |
| --- |

## [◆ ](#a03e82210e0063b35e7e3a877a6dbd17e)BSP\_IO\_SD1\_CMD

| #define BSP\_IO\_SD1\_CMD   0xFFFF1201 /\* SD1\_CMD \*/ |
| --- |

## [◆ ](#a8e6b818ecfdfbd9c8c571720711d35dd)BSP\_IO\_SD1\_DATA0

| #define BSP\_IO\_SD1\_DATA0   0xFFFF1300 /\* SD1\_DATA0 \*/ |
| --- |

## [◆ ](#a222474e671dc0196e027b741bfb6bef2)BSP\_IO\_SD1\_DATA1

| #define BSP\_IO\_SD1\_DATA1   0xFFFF1301 /\* SD1\_DATA1 \*/ |
| --- |

## [◆ ](#ab404c31fb4de4e9c80ffd9cd3d93b7ca)BSP\_IO\_SD1\_DATA2

| #define BSP\_IO\_SD1\_DATA2   0xFFFF1302 /\* SD1\_DATA2 \*/ |
| --- |

## [◆ ](#acb12cf7cf433e72dd141c6652be9d9af)BSP\_IO\_SD1\_DATA3

| #define BSP\_IO\_SD1\_DATA3   0xFFFF1303 /\* SD1\_DATA3 \*/ |
| --- |

## [◆ ](#a318b423b2efc8ab1a3de0a8f9ab3eeca)BSP\_IO\_TDO

| #define BSP\_IO\_TDO   0xFFFF0101 /\* TDO \*/ |
| --- |

## [◆ ](#af06a8358900119f6b4c3d91e465ce22f)BSP\_IO\_TMS\_SWDIO

| #define BSP\_IO\_TMS\_SWDIO   0xFFFF0100 /\* TMS\_SWDIO \*/ |
| --- |

## [◆ ](#a7c1efa402066677442bffceaa874e002)BSP\_IO\_WDTOVF\_PERROUT

| #define BSP\_IO\_WDTOVF\_PERROUT   0xFFFF0600 /\* WDTOVF\_PERROUT \*/ |
| --- |

## [◆ ](#a2356e340dbc38e7d62351b8996b40c1e)BSP\_IO\_XSPI\_CS0\_N

| #define BSP\_IO\_XSPI\_CS0\_N   0xFFFF0404 /\* XSPI\_CS0\_N \*/ |
| --- |

## [◆ ](#a973dd3ba73dbb9b3c93d3f715c4dd6c0)BSP\_IO\_XSPI\_CS1\_N

| #define BSP\_IO\_XSPI\_CS1\_N   0xFFFF0405 /\* XSPI\_CS1\_N \*/ |
| --- |

## [◆ ](#a019fd571a275deaf0570c317b9a20b97)BSP\_IO\_XSPI\_DS

| #define BSP\_IO\_XSPI\_DS   0xFFFF0403 /\* XSPI\_DS \*/ |
| --- |

## [◆ ](#a19da009b51eb3891a92ef39c13019567)BSP\_IO\_XSPI\_IO0

| #define BSP\_IO\_XSPI\_IO0   0xFFFF0500 /\* XSPI\_IO0 \*/ |
| --- |

## [◆ ](#a3ea0b2836c786211aa5643b7bce971c2)BSP\_IO\_XSPI\_IO1

| #define BSP\_IO\_XSPI\_IO1   0xFFFF0501 /\* XSPI\_IO1 \*/ |
| --- |

## [◆ ](#af0814f9594ef180d9dbb3e910118cb39)BSP\_IO\_XSPI\_IO2

| #define BSP\_IO\_XSPI\_IO2   0xFFFF0502 /\* XSPI\_IO2 \*/ |
| --- |

## [◆ ](#ae39cf1fdec8f1940030b962fd91895ec)BSP\_IO\_XSPI\_IO3

| #define BSP\_IO\_XSPI\_IO3   0xFFFF0503 /\* XSPI\_IO3 \*/ |
| --- |

## [◆ ](#ade455522c2e4df9f6a3d4335898c5a2e)BSP\_IO\_XSPI\_IO4

| #define BSP\_IO\_XSPI\_IO4   0xFFFF0504 /\* XSPI\_IO4 \*/ |
| --- |

## [◆ ](#afd88724051491fb938adc876ce9f8094)BSP\_IO\_XSPI\_IO5

| #define BSP\_IO\_XSPI\_IO5   0xFFFF0505 /\* XSPI\_IO5 \*/ |
| --- |

## [◆ ](#ae4047cb2b38a2388ac3ad4a73b438348)BSP\_IO\_XSPI\_IO6

| #define BSP\_IO\_XSPI\_IO6   0xFFFF0506 /\* XSPI\_IO6 \*/ |
| --- |

## [◆ ](#a0839e73ff018a83849befdf6c1fa9cbf)BSP\_IO\_XSPI\_IO7

| #define BSP\_IO\_XSPI\_IO7   0xFFFF0507 /\* XSPI\_IO7 \*/ |
| --- |

## [◆ ](#a1938aca3788d42e557a35c20517f9dd8)BSP\_IO\_XSPI\_RESET\_N

| #define BSP\_IO\_XSPI\_RESET\_N   0xFFFF0401 /\* XSPI\_RESET\_N \*/ |
| --- |

## [◆ ](#ae349e2b4add4664859e2c87e7eb47e15)BSP\_IO\_XSPI\_SPCLK

| #define BSP\_IO\_XSPI\_SPCLK   0xFFFF0400 /\* XSPI\_SPCLK \*/ |
| --- |

## [◆ ](#a73759a3f08a6b48278607de2f63cf523)BSP\_IO\_XSPI\_WP\_N

| #define BSP\_IO\_XSPI\_WP\_N   0xFFFF0402 /\* XSPI\_WP\_N \*/ |
| --- |

## [◆ ](#a1b0292747e92dff43d6760d9e2258869)PORT\_00

| #define PORT\_00   0x0000 /\* IO port 0 \*/ |
| --- |

## [◆ ](#a9de415830a2b3484dd33d5d08258dde5)PORT\_01

| #define PORT\_01   0x1000 /\* IO port 1 \*/ |
| --- |

## [◆ ](#a7db623b2ec3816113a8f3fb07d5428ef)PORT\_02

| #define PORT\_02   0x1100 /\* IO port 2 \*/ |
| --- |

## [◆ ](#a71478a4563d986886410618bc130b0d9)PORT\_03

| #define PORT\_03   0x1200 /\* IO port 3 \*/ |
| --- |

## [◆ ](#aed73b97fc12615ac1dec9daad9537647)PORT\_04

| #define PORT\_04   0x1300 /\* IO port 4 \*/ |
| --- |

## [◆ ](#a590020a2e6577d74d89bdee0989812c4)PORT\_05

| #define PORT\_05   0x0100 /\* IO port 5 \*/ |
| --- |

## [◆ ](#ab2912aeb54c92971e0590ff3282e775b)PORT\_06

| #define PORT\_06   0x0200 /\* IO port 6 \*/ |
| --- |

## [◆ ](#acabb0398db58703c47e718f899018410)PORT\_07

| #define PORT\_07   0x1400 /\* IO port 7 \*/ |
| --- |

## [◆ ](#a5f4d0cfbea4e649fa0863d4a8d409c5e)PORT\_08

| #define PORT\_08   0x1500 /\* IO port 8 \*/ |
| --- |

## [◆ ](#a5e8d840d1a1bd421615b2cc90ce0b90f)PORT\_09

| #define PORT\_09   0x1600 /\* IO port 9 \*/ |
| --- |

## [◆ ](#a4c39a294d7b3a360c172b65151a5bfc8)PORT\_10

| #define PORT\_10   0x1700 /\* IO port 10 \*/ |
| --- |

## [◆ ](#abeebf6334cb5240b09d97d35fc0128f3)PORT\_11

| #define PORT\_11   0x0300 /\* IO port 11 \*/ |
| --- |

## [◆ ](#ae57c3ffa4df15481a9a219e16b011ef3)PORT\_12

| #define PORT\_12   0x0400 /\* IO port 12 \*/ |
| --- |

## [◆ ](#ae76dfcae2263b7d43d1ee23fa9548293)PORT\_13

| #define PORT\_13   0x0500 /\* IO port 13 \*/ |
| --- |

## [◆ ](#a9c8783d66b07c093c559a5fd74add129)PORT\_14

| #define PORT\_14   0x0600 /\* IO port 14 \*/ |
| --- |

## [◆ ](#aeb88886b16b5a8ea23147000fd9af3cc)PORT\_15

| #define PORT\_15   0x0700 /\* IO port 15 \*/ |
| --- |

## [◆ ](#aa9fff44f99e434f31b19ed55462b45d4)PORT\_16

| #define PORT\_16   0x0800 /\* IO port 16 \*/ |
| --- |

## [◆ ](#a8ce8fd8ca6cdbc375b70a0b7d53eb315)PORT\_17

| #define PORT\_17   0x0900 /\* IO port 17 \*/ |
| --- |

## [◆ ](#a51b6b92e7f3238a410526b67234f77d7)PORT\_18

| #define PORT\_18   0x0A00 /\* IO port 18 \*/ |
| --- |

## [◆ ](#a82fe6b7f1ba59ab812683890fa2f0e7c)RZG\_FILCLKSEL\_DIV\_18000

| #define RZG\_FILCLKSEL\_DIV\_18000   2 |
| --- |

## [◆ ](#acecffc879cdcd14232b7cc2714e46e8f)RZG\_FILCLKSEL\_DIV\_36000

| #define RZG\_FILCLKSEL\_DIV\_36000   3 |
| --- |

## [◆ ](#a6fc19ace82becb78720423edd9a80f03)RZG\_FILCLKSEL\_DIV\_9000

| #define RZG\_FILCLKSEL\_DIV\_9000   1 |
| --- |

## [◆ ](#aebf11f5c29f9d62a4bc6076430f5af74)RZG\_FILCLKSEL\_NOT\_DIV

| #define RZG\_FILCLKSEL\_NOT\_DIV   0 |
| --- |

## [◆ ](#a7fb5e17c2033f7de03440445de58497d)RZG\_FILNUM\_12\_STAGE

| #define RZG\_FILNUM\_12\_STAGE   2 |
| --- |

## [◆ ](#a4c3d0f96e45fcff456391291544c2d7e)RZG\_FILNUM\_16\_STAGE

| #define RZG\_FILNUM\_16\_STAGE   3 |
| --- |

## [◆ ](#a410e1db2102a72b3222f3f87e9191b36)RZG\_FILNUM\_4\_STAGE

| #define RZG\_FILNUM\_4\_STAGE   0 |
| --- |

## [◆ ](#a7ec85695dd35462b15784cf869e2ecdd)RZG\_FILNUM\_8\_STAGE

| #define RZG\_FILNUM\_8\_STAGE   1 |
| --- |

## [◆ ](#abe4747778068dd33b142d7a891ca901e)RZG\_FILTER\_SET

| #define RZG\_FILTER\_SET | ( |  | *filnum*, |
| --- | --- | --- | --- |
|  |  |  | *filclksel* ) |

**Value:**

(((filnum) & 0x3) << 0x2) | (filclksel & 0x3)

## [◆ ](#a02f280ee325bc9e66e5566f8d6f3feec)RZG\_PINMUX

| #define RZG\_PINMUX | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin*, |
|  |  |  | *func* ) |

**Value:**

(port | pin | (func << 4))

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [pinctrl](dir_2c6c4fbd167577104b7f1b7148586168.md)
- [renesas](dir_17f48eb154be6cea623223db5de209e7.md)
- [pinctrl-rzg-common.h](pinctrl-rzg-common_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
