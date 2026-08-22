---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/pinctrl-rza-common_8h.html
original_path: doxygen/html/pinctrl-rza-common_8h.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

pinctrl-rza-common.h File Reference

[Go to the source code of this file.](pinctrl-rza-common_8h_source.md)

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
| #define | [PORT\_12](#ae57c3ffa4df15481a9a219e16b011ef3)   0x0C00 /\* IO port 12 \*/ |
| #define | [PORT\_13](#ae76dfcae2263b7d43d1ee23fa9548293)   0x0D00 /\* IO port 13 \*/ |
| #define | [PORT\_14](#a9c8783d66b07c093c559a5fd74add129)   0x0E00 /\* IO port 14 \*/ |
| #define | [PORT\_15](#aeb88886b16b5a8ea23147000fd9af3cc)   0x0F00 /\* IO port 15 \*/ |
| #define | [PORT\_16](#aa9fff44f99e434f31b19ed55462b45d4)   0x1000 /\* IO port 16 \*/ |
| #define | [PORT\_17](#a8ce8fd8ca6cdbc375b70a0b7d53eb315)   0x1100 /\* IO port 17 \*/ |
| #define | [PORT\_18](#a51b6b92e7f3238a410526b67234f77d7)   0x1200 /\* IO port 18 \*/ |
| #define | [RZA\_PINMUX](#aad0f3d9e2b289afca587d9897ad35210)(port, pin, func) |
| #define | [BSP\_IO\_NMI](#a5a8b4d2cdc15f25cc0b58db97c539b2a)   0xFFFF0100 /\* NMI \*/ |
| #define | [BSP\_IO\_TMS\_SWDIO](#af06a8358900119f6b4c3d91e465ce22f)   0xFFFF0200 /\* TMS\_SWDIO \*/ |
| #define | [BSP\_IO\_TDO](#a318b423b2efc8ab1a3de0a8f9ab3eeca)   0xFFFF0300 /\* TDO \*/ |
| #define | [BSP\_IO\_AUDIO\_CLK1](#acf9b257ce3e3a66bcfa8d4aca427c0bf)   0xFFFF0400 /\* AUDIO\_CLK1 \*/ |
| #define | [BSP\_IO\_AUDIO\_CLK2](#a98d349e2311d1571d490e26866871b16)   0xFFFF0401 /\* AUDIO\_CLK2 \*/ |
| #define | [BSP\_IO\_SD0\_CLK](#a99cac86447ae6b18e3e1601085623a60)   0xFFFF0600 /\* CD0\_CLK \*/ |
| #define | [BSP\_IO\_SD0\_CMD](#a2b904f716e2bf524351430155b8c7ddc)   0xFFFF0601 /\* CD0\_CMD \*/ |
| #define | [BSP\_IO\_SD0\_RST\_N](#ad61d120b88812e3c41a600414f553325)   0xFFFF0602 /\* CD0\_RST\_N \*/ |
| #define | [BSP\_IO\_SD0\_DATA0](#a1f4951bb275e24732e8487dffd5fe69a)   0xFFFF0700 /\* SD0\_DATA0 \*/ |
| #define | [BSP\_IO\_SD0\_DATA1](#a97428f756c92136fd0f3d34f520c760b)   0xFFFF0701 /\* SD0\_DATA1 \*/ |
| #define | [BSP\_IO\_SD0\_DATA2](#a77fab2fb18ce2a3d779d94b54e8d58d1)   0xFFFF0702 /\* SD0\_DATA2 \*/ |
| #define | [BSP\_IO\_SD0\_DATA3](#a8794e04fe7b7d3d895973cac59538095)   0xFFFF0703 /\* SD0\_DATA3 \*/ |
| #define | [BSP\_IO\_SD0\_DATA4](#a9398ade50c886958f0b51b41a9c4849b)   0xFFFF0704 /\* SD0\_DATA4 \*/ |
| #define | [BSP\_IO\_SD0\_DATA5](#ae127f16b4b223229c57375a20ad2a442)   0xFFFF0705 /\* SD0\_DATA5 \*/ |
| #define | [BSP\_IO\_SD0\_DATA6](#af64543688eccd90de6b9086ccd72e3fd)   0xFFFF0706 /\* SD0\_DATA6 \*/ |
| #define | [BSP\_IO\_SD0\_DATA7](#a1e39def829ae82ed38ddbd0f01d9b62f)   0xFFFF0707 /\* SD0\_DATA7 \*/ |
| #define | [BSP\_IO\_SD1\_CLK](#a21e34df07c258c73258ba42eeab62fee)   0xFFFF0800 /\* SD1\_CLK \*/ |
| #define | [BSP\_IO\_SD1\_CMD](#a03e82210e0063b35e7e3a877a6dbd17e)   0xFFFF0801 /\* SD1\_CMD \*/ |
| #define | [BSP\_IO\_SD1\_DATA0](#a8e6b818ecfdfbd9c8c571720711d35dd)   0xFFFF0900 /\* SD1\_DATA0 \*/ |
| #define | [BSP\_IO\_SD1\_DATA1](#a222474e671dc0196e027b741bfb6bef2)   0xFFFF0901 /\* SD1\_DATA1 \*/ |
| #define | [BSP\_IO\_SD1\_DATA2](#ab404c31fb4de4e9c80ffd9cd3d93b7ca)   0xFFFF0902 /\* SD1\_DATA2 \*/ |
| #define | [BSP\_IO\_SD1\_DATA3](#acb12cf7cf433e72dd141c6652be9d9af)   0xFFFF0903 /\* SD1\_DATA3 \*/ |
| #define | [BSP\_IO\_QSPI0\_SPCLK](#aaa8265b3c46500752b85644e535692a2)   0xFFFF0A00 /\* QSPI0\_SPCLK \*/ |
| #define | [BSP\_IO\_QSPI0\_IO0](#acb67188a7f35bc9af5ff4a9f3630842e)   0xFFFF0A01 /\* QSPI0\_IO0 \*/ |
| #define | [BSP\_IO\_QSPI0\_IO1](#a01f1b79e7f366a6a8ad84e5ec37b4158)   0xFFFF0A02 /\* QSPI0\_IO1 \*/ |
| #define | [BSP\_IO\_QSPI0\_IO2](#a98e28074dd38b49185c7dca7d7903b1d)   0xFFFF0A03 /\* QSPI0\_IO2 \*/ |
| #define | [BSP\_IO\_QSPI0\_IO3](#a12283abd104711dbb9cc2bfe406f0703)   0xFFFF0A04 /\* QSPI0\_IO3 \*/ |
| #define | [BSP\_IO\_QSPI0\_SSL](#acd80bf931fcadaebf996edb2bf76e9e3)   0xFFFF0A05 /\* QSPI0\_SSL \*/ |
| #define | [BSP\_IO\_OM\_CS1\_N](#a87a74fe5e54dba6dbd6f454ae1f7e2d8)   0xFFFF0B00 /\* OM\_CS1\_N \*/ |
| #define | [BSP\_IO\_OM\_DQS](#ac7bf1cf7d1da17c05ef2fe2e1c34de4f)   0xFFFF0B01 /\* OM\_DQS \*/ |
| #define | [BSP\_IO\_OM\_SIO4](#ab788db0c971af9be7fe2c7c08b1168b0)   0xFFFF0B02 /\* OM\_SIO4 \*/ |
| #define | [BSP\_IO\_OM\_SIO5](#a516b19addd1e2efa9377aea01b005dcb)   0xFFFF0B03 /\* OM\_SIO5 \*/ |
| #define | [BSP\_IO\_OM\_SIO6](#a3758f58970281eb6ae17fb4ed216e787)   0xFFFF0B04 /\* OM\_SIO6 \*/ |
| #define | [BSP\_IO\_OM\_SIO7](#ac51dbcdecce7d39a8d2e81f6100e9370)   0xFFFF0B05 /\* OM\_SIO7 \*/ |
| #define | [BSP\_IO\_QSPI\_RESET\_N](#ab6a44158744e5cad8124f4da291159dc)   0xFFFF0C00 /\* QSPI\_RESET\_N \*/ |
| #define | [BSP\_IO\_QSPI\_WP\_N](#abf8e87c6fdcd8241324c66b443668251)   0xFFFF0C01 /\* QSPI\_WP\_N \*/ |
| #define | [BSP\_IO\_WDTOVF\_PERROUT\_N](#ad2e37f140ebdb92bb4ee94f6a8032737)   0xFFFF0D00 /\* WDTOVF\_PERROUT\_N \*/ |
| #define | [BSP\_IO\_RIIC0\_SDA](#abf5f96c4d40bddcef43d534d7ea6fdaa)   0xFFFF0E00 /\* RIIC0\_SDA \*/ |
| #define | [BSP\_IO\_RIIC0\_SCL](#a20256eab52e96328dab53ff66037d35b)   0xFFFF0E01 /\* RIIC0\_SCL \*/ |
| #define | [BSP\_IO\_RIIC1\_SDA](#adc37073529eb331cf8cc80185abf5f92)   0xFFFF0E02 /\* RIIC1\_SDA \*/ |
| #define | [BSP\_IO\_RIIC1\_SCL](#ae1c7843f96e83c7aebb77512036aa20c)   0xFFFF0E03 /\* RIIC1\_SCL \*/ |
| #define | [RZA\_FILNUM\_4\_STAGE](#ae2fb4f96b6b50ad80a433780e422db2f)   0 |
| #define | [RZA\_FILNUM\_8\_STAGE](#a9e4ed308e81c23c7d70a70f3708b3392)   1 |
| #define | [RZA\_FILNUM\_12\_STAGE](#a6d57d4270438ff5b6cc72111e6d03562)   2 |
| #define | [RZA\_FILNUM\_16\_STAGE](#a9a82059d12af7f931f051a304113735e)   3 |
| #define | [RZA\_FILCLKSEL\_NOT\_DIV](#ab5bb0119588fa51a96489d03a62c4b83)   0 |
| #define | [RZA\_FILCLKSEL\_DIV\_9000](#a6d987d1bb9a03f28abf5980f0a45ceb4)   1 |
| #define | [RZA\_FILCLKSEL\_DIV\_18000](#a9fe6a4f870d9260c13f055245b3d22cb)   2 |
| #define | [RZA\_FILCLKSEL\_DIV\_36000](#a24aeabb3038f110c9d4a76df150987ef)   3 |
| #define | [RZA\_FILTER\_SET](#acb3f592d302bb7ee67914ade80a3fb44)(filnum, filclksel) |

## Macro Definition Documentation

## [◆ ](#acf9b257ce3e3a66bcfa8d4aca427c0bf)BSP\_IO\_AUDIO\_CLK1

| #define BSP\_IO\_AUDIO\_CLK1   0xFFFF0400 /\* AUDIO\_CLK1 \*/ |
| --- |

## [◆ ](#a98d349e2311d1571d490e26866871b16)BSP\_IO\_AUDIO\_CLK2

| #define BSP\_IO\_AUDIO\_CLK2   0xFFFF0401 /\* AUDIO\_CLK2 \*/ |
| --- |

## [◆ ](#a5a8b4d2cdc15f25cc0b58db97c539b2a)BSP\_IO\_NMI

| #define BSP\_IO\_NMI   0xFFFF0100 /\* NMI \*/ |
| --- |

## [◆ ](#a87a74fe5e54dba6dbd6f454ae1f7e2d8)BSP\_IO\_OM\_CS1\_N

| #define BSP\_IO\_OM\_CS1\_N   0xFFFF0B00 /\* OM\_CS1\_N \*/ |
| --- |

## [◆ ](#ac7bf1cf7d1da17c05ef2fe2e1c34de4f)BSP\_IO\_OM\_DQS

| #define BSP\_IO\_OM\_DQS   0xFFFF0B01 /\* OM\_DQS \*/ |
| --- |

## [◆ ](#ab788db0c971af9be7fe2c7c08b1168b0)BSP\_IO\_OM\_SIO4

| #define BSP\_IO\_OM\_SIO4   0xFFFF0B02 /\* OM\_SIO4 \*/ |
| --- |

## [◆ ](#a516b19addd1e2efa9377aea01b005dcb)BSP\_IO\_OM\_SIO5

| #define BSP\_IO\_OM\_SIO5   0xFFFF0B03 /\* OM\_SIO5 \*/ |
| --- |

## [◆ ](#a3758f58970281eb6ae17fb4ed216e787)BSP\_IO\_OM\_SIO6

| #define BSP\_IO\_OM\_SIO6   0xFFFF0B04 /\* OM\_SIO6 \*/ |
| --- |

## [◆ ](#ac51dbcdecce7d39a8d2e81f6100e9370)BSP\_IO\_OM\_SIO7

| #define BSP\_IO\_OM\_SIO7   0xFFFF0B05 /\* OM\_SIO7 \*/ |
| --- |

## [◆ ](#acb67188a7f35bc9af5ff4a9f3630842e)BSP\_IO\_QSPI0\_IO0

| #define BSP\_IO\_QSPI0\_IO0   0xFFFF0A01 /\* QSPI0\_IO0 \*/ |
| --- |

## [◆ ](#a01f1b79e7f366a6a8ad84e5ec37b4158)BSP\_IO\_QSPI0\_IO1

| #define BSP\_IO\_QSPI0\_IO1   0xFFFF0A02 /\* QSPI0\_IO1 \*/ |
| --- |

## [◆ ](#a98e28074dd38b49185c7dca7d7903b1d)BSP\_IO\_QSPI0\_IO2

| #define BSP\_IO\_QSPI0\_IO2   0xFFFF0A03 /\* QSPI0\_IO2 \*/ |
| --- |

## [◆ ](#a12283abd104711dbb9cc2bfe406f0703)BSP\_IO\_QSPI0\_IO3

| #define BSP\_IO\_QSPI0\_IO3   0xFFFF0A04 /\* QSPI0\_IO3 \*/ |
| --- |

## [◆ ](#aaa8265b3c46500752b85644e535692a2)BSP\_IO\_QSPI0\_SPCLK

| #define BSP\_IO\_QSPI0\_SPCLK   0xFFFF0A00 /\* QSPI0\_SPCLK \*/ |
| --- |

## [◆ ](#acd80bf931fcadaebf996edb2bf76e9e3)BSP\_IO\_QSPI0\_SSL

| #define BSP\_IO\_QSPI0\_SSL   0xFFFF0A05 /\* QSPI0\_SSL \*/ |
| --- |

## [◆ ](#ab6a44158744e5cad8124f4da291159dc)BSP\_IO\_QSPI\_RESET\_N

| #define BSP\_IO\_QSPI\_RESET\_N   0xFFFF0C00 /\* QSPI\_RESET\_N \*/ |
| --- |

## [◆ ](#abf8e87c6fdcd8241324c66b443668251)BSP\_IO\_QSPI\_WP\_N

| #define BSP\_IO\_QSPI\_WP\_N   0xFFFF0C01 /\* QSPI\_WP\_N \*/ |
| --- |

## [◆ ](#a20256eab52e96328dab53ff66037d35b)BSP\_IO\_RIIC0\_SCL

| #define BSP\_IO\_RIIC0\_SCL   0xFFFF0E01 /\* RIIC0\_SCL \*/ |
| --- |

## [◆ ](#abf5f96c4d40bddcef43d534d7ea6fdaa)BSP\_IO\_RIIC0\_SDA

| #define BSP\_IO\_RIIC0\_SDA   0xFFFF0E00 /\* RIIC0\_SDA \*/ |
| --- |

## [◆ ](#ae1c7843f96e83c7aebb77512036aa20c)BSP\_IO\_RIIC1\_SCL

| #define BSP\_IO\_RIIC1\_SCL   0xFFFF0E03 /\* RIIC1\_SCL \*/ |
| --- |

## [◆ ](#adc37073529eb331cf8cc80185abf5f92)BSP\_IO\_RIIC1\_SDA

| #define BSP\_IO\_RIIC1\_SDA   0xFFFF0E02 /\* RIIC1\_SDA \*/ |
| --- |

## [◆ ](#a99cac86447ae6b18e3e1601085623a60)BSP\_IO\_SD0\_CLK

| #define BSP\_IO\_SD0\_CLK   0xFFFF0600 /\* CD0\_CLK \*/ |
| --- |

## [◆ ](#a2b904f716e2bf524351430155b8c7ddc)BSP\_IO\_SD0\_CMD

| #define BSP\_IO\_SD0\_CMD   0xFFFF0601 /\* CD0\_CMD \*/ |
| --- |

## [◆ ](#a1f4951bb275e24732e8487dffd5fe69a)BSP\_IO\_SD0\_DATA0

| #define BSP\_IO\_SD0\_DATA0   0xFFFF0700 /\* SD0\_DATA0 \*/ |
| --- |

## [◆ ](#a97428f756c92136fd0f3d34f520c760b)BSP\_IO\_SD0\_DATA1

| #define BSP\_IO\_SD0\_DATA1   0xFFFF0701 /\* SD0\_DATA1 \*/ |
| --- |

## [◆ ](#a77fab2fb18ce2a3d779d94b54e8d58d1)BSP\_IO\_SD0\_DATA2

| #define BSP\_IO\_SD0\_DATA2   0xFFFF0702 /\* SD0\_DATA2 \*/ |
| --- |

## [◆ ](#a8794e04fe7b7d3d895973cac59538095)BSP\_IO\_SD0\_DATA3

| #define BSP\_IO\_SD0\_DATA3   0xFFFF0703 /\* SD0\_DATA3 \*/ |
| --- |

## [◆ ](#a9398ade50c886958f0b51b41a9c4849b)BSP\_IO\_SD0\_DATA4

| #define BSP\_IO\_SD0\_DATA4   0xFFFF0704 /\* SD0\_DATA4 \*/ |
| --- |

## [◆ ](#ae127f16b4b223229c57375a20ad2a442)BSP\_IO\_SD0\_DATA5

| #define BSP\_IO\_SD0\_DATA5   0xFFFF0705 /\* SD0\_DATA5 \*/ |
| --- |

## [◆ ](#af64543688eccd90de6b9086ccd72e3fd)BSP\_IO\_SD0\_DATA6

| #define BSP\_IO\_SD0\_DATA6   0xFFFF0706 /\* SD0\_DATA6 \*/ |
| --- |

## [◆ ](#a1e39def829ae82ed38ddbd0f01d9b62f)BSP\_IO\_SD0\_DATA7

| #define BSP\_IO\_SD0\_DATA7   0xFFFF0707 /\* SD0\_DATA7 \*/ |
| --- |

## [◆ ](#ad61d120b88812e3c41a600414f553325)BSP\_IO\_SD0\_RST\_N

| #define BSP\_IO\_SD0\_RST\_N   0xFFFF0602 /\* CD0\_RST\_N \*/ |
| --- |

## [◆ ](#a21e34df07c258c73258ba42eeab62fee)BSP\_IO\_SD1\_CLK

| #define BSP\_IO\_SD1\_CLK   0xFFFF0800 /\* SD1\_CLK \*/ |
| --- |

## [◆ ](#a03e82210e0063b35e7e3a877a6dbd17e)BSP\_IO\_SD1\_CMD

| #define BSP\_IO\_SD1\_CMD   0xFFFF0801 /\* SD1\_CMD \*/ |
| --- |

## [◆ ](#a8e6b818ecfdfbd9c8c571720711d35dd)BSP\_IO\_SD1\_DATA0

| #define BSP\_IO\_SD1\_DATA0   0xFFFF0900 /\* SD1\_DATA0 \*/ |
| --- |

## [◆ ](#a222474e671dc0196e027b741bfb6bef2)BSP\_IO\_SD1\_DATA1

| #define BSP\_IO\_SD1\_DATA1   0xFFFF0901 /\* SD1\_DATA1 \*/ |
| --- |

## [◆ ](#ab404c31fb4de4e9c80ffd9cd3d93b7ca)BSP\_IO\_SD1\_DATA2

| #define BSP\_IO\_SD1\_DATA2   0xFFFF0902 /\* SD1\_DATA2 \*/ |
| --- |

## [◆ ](#acb12cf7cf433e72dd141c6652be9d9af)BSP\_IO\_SD1\_DATA3

| #define BSP\_IO\_SD1\_DATA3   0xFFFF0903 /\* SD1\_DATA3 \*/ |
| --- |

## [◆ ](#a318b423b2efc8ab1a3de0a8f9ab3eeca)BSP\_IO\_TDO

| #define BSP\_IO\_TDO   0xFFFF0300 /\* TDO \*/ |
| --- |

## [◆ ](#af06a8358900119f6b4c3d91e465ce22f)BSP\_IO\_TMS\_SWDIO

| #define BSP\_IO\_TMS\_SWDIO   0xFFFF0200 /\* TMS\_SWDIO \*/ |
| --- |

## [◆ ](#ad2e37f140ebdb92bb4ee94f6a8032737)BSP\_IO\_WDTOVF\_PERROUT\_N

| #define BSP\_IO\_WDTOVF\_PERROUT\_N   0xFFFF0D00 /\* WDTOVF\_PERROUT\_N \*/ |
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

## [◆ ](#ae57c3ffa4df15481a9a219e16b011ef3)PORT\_12

| #define PORT\_12   0x0C00 /\* IO port 12 \*/ |
| --- |

## [◆ ](#ae76dfcae2263b7d43d1ee23fa9548293)PORT\_13

| #define PORT\_13   0x0D00 /\* IO port 13 \*/ |
| --- |

## [◆ ](#a9c8783d66b07c093c559a5fd74add129)PORT\_14

| #define PORT\_14   0x0E00 /\* IO port 14 \*/ |
| --- |

## [◆ ](#aeb88886b16b5a8ea23147000fd9af3cc)PORT\_15

| #define PORT\_15   0x0F00 /\* IO port 15 \*/ |
| --- |

## [◆ ](#aa9fff44f99e434f31b19ed55462b45d4)PORT\_16

| #define PORT\_16   0x1000 /\* IO port 16 \*/ |
| --- |

## [◆ ](#a8ce8fd8ca6cdbc375b70a0b7d53eb315)PORT\_17

| #define PORT\_17   0x1100 /\* IO port 17 \*/ |
| --- |

## [◆ ](#a51b6b92e7f3238a410526b67234f77d7)PORT\_18

| #define PORT\_18   0x1200 /\* IO port 18 \*/ |
| --- |

## [◆ ](#a9fe6a4f870d9260c13f055245b3d22cb)RZA\_FILCLKSEL\_DIV\_18000

| #define RZA\_FILCLKSEL\_DIV\_18000   2 |
| --- |

## [◆ ](#a24aeabb3038f110c9d4a76df150987ef)RZA\_FILCLKSEL\_DIV\_36000

| #define RZA\_FILCLKSEL\_DIV\_36000   3 |
| --- |

## [◆ ](#a6d987d1bb9a03f28abf5980f0a45ceb4)RZA\_FILCLKSEL\_DIV\_9000

| #define RZA\_FILCLKSEL\_DIV\_9000   1 |
| --- |

## [◆ ](#ab5bb0119588fa51a96489d03a62c4b83)RZA\_FILCLKSEL\_NOT\_DIV

| #define RZA\_FILCLKSEL\_NOT\_DIV   0 |
| --- |

## [◆ ](#a6d57d4270438ff5b6cc72111e6d03562)RZA\_FILNUM\_12\_STAGE

| #define RZA\_FILNUM\_12\_STAGE   2 |
| --- |

## [◆ ](#a9a82059d12af7f931f051a304113735e)RZA\_FILNUM\_16\_STAGE

| #define RZA\_FILNUM\_16\_STAGE   3 |
| --- |

## [◆ ](#ae2fb4f96b6b50ad80a433780e422db2f)RZA\_FILNUM\_4\_STAGE

| #define RZA\_FILNUM\_4\_STAGE   0 |
| --- |

## [◆ ](#a9e4ed308e81c23c7d70a70f3708b3392)RZA\_FILNUM\_8\_STAGE

| #define RZA\_FILNUM\_8\_STAGE   1 |
| --- |

## [◆ ](#acb3f592d302bb7ee67914ade80a3fb44)RZA\_FILTER\_SET

| #define RZA\_FILTER\_SET | ( |  | *filnum*, |
| --- | --- | --- | --- |
|  |  |  | *filclksel* ) |

**Value:**

(((filnum) & 0x3) << 0x2) | (filclksel & 0x3)

## [◆ ](#aad0f3d9e2b289afca587d9897ad35210)RZA\_PINMUX

| #define RZA\_PINMUX | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin*, |
|  |  |  | *func* ) |

**Value:**

(port | pin | (func << 4))

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [pinctrl](dir_2c6c4fbd167577104b7f1b7148586168.md)
- [renesas](dir_17f48eb154be6cea623223db5de209e7.md)
- [pinctrl-rza-common.h](pinctrl-rza-common_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
