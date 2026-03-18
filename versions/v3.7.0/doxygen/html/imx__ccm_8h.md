---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/imx__ccm_8h.html
original_path: doxygen/html/imx__ccm_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

imx\_ccm.h File Reference

[Go to the source code of this file.](imx__ccm_8h_source.md)

| Macros | |
| --- | --- |
| #define | [IMX\_CCM\_PERIPHERAL\_MASK](#aa31bf3cf51ff3af717f0d4037eeaa1c9)   0xFF00UL |
| #define | [IMX\_CCM\_INSTANCE\_MASK](#a30f30d268fb9aae738f27161e6028f73)   0x00FFUL |
| #define | [IMX\_CCM\_CORESYS\_CLK](#ab1e95e431d7486c814c969d0d9c57559)   0x0000UL |
| #define | [IMX\_CCM\_PLATFORM\_CLK](#afcda3a44b4029872bfa5d219f10dd506)   0x0100UL |
| #define | [IMX\_CCM\_BUS\_CLK](#a0f9e44ec176274d3792bb2dd3e21a28b)   0x0200UL |
| #define | [IMX\_CCM\_LPUART\_CLK](#a01fa41a7ad66c54b1c19455b6160bbc2)   0x0300UL |
| #define | [IMX\_CCM\_LPUART1\_CLK](#a96e62b5b478ee548a1e52b7189a73817)   0x0300UL |
| #define | [IMX\_CCM\_LPUART2\_CLK](#a46255999d02ae6161981374872e065cf)   0x0301UL |
| #define | [IMX\_CCM\_LPUART3\_CLK](#a6676eb59f3d665c2a9bba7aae24228ca)   0x0302UL |
| #define | [IMX\_CCM\_LPUART4\_CLK](#a9647111e5a5af6e8e67e059009490974)   0x0303UL |
| #define | [IMX\_CCM\_LPUART5\_CLK](#acd84397a25a81c7f315c7740049d570a)   0x0304UL |
| #define | [IMX\_CCM\_LPUART6\_CLK](#a3c6916f6ff4fae75dc51177e25d51642)   0x0305UL |
| #define | [IMX\_CCM\_LPUART7\_CLK](#a4f2f07925d50b73cdc218d1f99cedf98)   0x0306UL |
| #define | [IMX\_CCM\_LPUART8\_CLK](#a8db4fa3e674535ba490d89a52979cad0)   0x0307UL |
| #define | [IMX\_CCM\_LPI2C\_CLK](#ac970114caf03b14bf6d3f2ff04f548dc)   0x0400UL |
| #define | [IMX\_CCM\_LPSPI\_CLK](#a169487d4c020dee2492e36202fa39158)   0x0500UL |
| #define | [IMX\_CCM\_USDHC1\_CLK](#a3f07127852de7ae5516c376589f1f780)   0x0600UL |
| #define | [IMX\_CCM\_USDHC2\_CLK](#a4596ce38e656971ec5330dab452bd04c)   0x0601UL |
| #define | [IMX\_CCM\_EDMA\_CLK](#aa82ff051d04371deee96c754d93abb57)   0x0700UL |
| #define | [IMX\_CCM\_UART1\_CLK](#a62f00f098b8ee58612dd7cd5cc9da1e3)   0x0800UL |
| #define | [IMX\_CCM\_UART2\_CLK](#a87c6bd30a90ca0cfdba829ae3cef2323)   0x0801UL |
| #define | [IMX\_CCM\_UART3\_CLK](#aca209cf9c7038df4c53cb6ee930dfcd9)   0x0802UL |
| #define | [IMX\_CCM\_UART4\_CLK](#a87564f52751e46be9ca0cec40c197f24)   0x0803UL |
| #define | [IMX\_CCM\_CAN\_CLK](#aded96aef4768dd5f01d14a163cd7487d)   0x0900UL |
| #define | [IMX\_CCM\_GPT\_CLK](#aadc28bb4c97c89e86a8a437262a3afad)   0x0A00UL |
| #define | [IMX\_CCM\_SAI1\_CLK](#a398527cf42962caf290b9ce1e5d7f9ac)   0x0B00UL |
| #define | [IMX\_CCM\_SAI2\_CLK](#aae6ea492162692b3ae2dc6aed60cc08d)   0x0B01UL |
| #define | [IMX\_CCM\_SAI3\_CLK](#a28779c577a92d4806239fe6e254d1a84)   0x0B02UL |
| #define | [IMX\_CCM\_PWM\_CLK](#acbc9256c26bb1232c5ca0eb8bfe52c22)   0x0C00UL |
| #define | [IMX\_CCM\_QTMR\_CLK](#a0cc7a30460bef2b0e6772a91539203a8)   0x0D00UL |
| #define | [IMX\_CCM\_ENET\_CLK](#aaeff78179dff600c88c1d1986b3976cd)   0x0E00UL |
| #define | [IMX\_CCM\_ENET\_PLL](#a2a4beef16589b00f9aca825e7419e9ff)   0x0E01UL |
| #define | [IMX\_CCM\_FLEXSPI\_CLK](#a5f86bba59cc685682df75e66a5d64cea)   0x0F00UL |
| #define | [IMX\_CCM\_FLEXSPI2\_CLK](#aa471a61b4b453551839b29322ec21422)   0x0F01UL |
| #define | [IMX\_CCM\_PIT\_CLK](#a0089a79d220e999a846afc32a827aeb7)   0x1000UL |
| #define | [IMX\_CCM\_FLEXIO1\_CLK](#a56168563c208301c93c6d54cb06c3a34)   0x1100UL |
| #define | [IMX\_CCM\_FLEXIO2\_3\_CLK](#a2817b49a9d77b1f02f854967bf160405)   0x1101UL |
| #define | [IMX\_CCM\_ECSPI1\_CLK](#aeefeb9e8bb7220d1d838120086063558)   0x1200UL |
| #define | [IMX\_CCM\_ECSPI2\_CLK](#a6d45128aaafaf3b79458a274a5728c28)   0x1201UL |
| #define | [IMX\_CCM\_ECSPI3\_CLK](#a3ba94cb4e36f14ec278a23033d4a97a3)   0x1202UL |
| #define | [IMX\_CCM\_GPT\_IPG\_CLK](#a95422e9f72395bfd62899d2e5c35bf46)   0x1300UL |

## Macro Definition Documentation

## [◆ ](#a0f9e44ec176274d3792bb2dd3e21a28b)IMX\_CCM\_BUS\_CLK

| #define IMX\_CCM\_BUS\_CLK   0x0200UL |
| --- |

## [◆ ](#aded96aef4768dd5f01d14a163cd7487d)IMX\_CCM\_CAN\_CLK

| #define IMX\_CCM\_CAN\_CLK   0x0900UL |
| --- |

## [◆ ](#ab1e95e431d7486c814c969d0d9c57559)IMX\_CCM\_CORESYS\_CLK

| #define IMX\_CCM\_CORESYS\_CLK   0x0000UL |
| --- |

## [◆ ](#aeefeb9e8bb7220d1d838120086063558)IMX\_CCM\_ECSPI1\_CLK

| #define IMX\_CCM\_ECSPI1\_CLK   0x1200UL |
| --- |

## [◆ ](#a6d45128aaafaf3b79458a274a5728c28)IMX\_CCM\_ECSPI2\_CLK

| #define IMX\_CCM\_ECSPI2\_CLK   0x1201UL |
| --- |

## [◆ ](#a3ba94cb4e36f14ec278a23033d4a97a3)IMX\_CCM\_ECSPI3\_CLK

| #define IMX\_CCM\_ECSPI3\_CLK   0x1202UL |
| --- |

## [◆ ](#aa82ff051d04371deee96c754d93abb57)IMX\_CCM\_EDMA\_CLK

| #define IMX\_CCM\_EDMA\_CLK   0x0700UL |
| --- |

## [◆ ](#aaeff78179dff600c88c1d1986b3976cd)IMX\_CCM\_ENET\_CLK

| #define IMX\_CCM\_ENET\_CLK   0x0E00UL |
| --- |

## [◆ ](#a2a4beef16589b00f9aca825e7419e9ff)IMX\_CCM\_ENET\_PLL

| #define IMX\_CCM\_ENET\_PLL   0x0E01UL |
| --- |

## [◆ ](#a56168563c208301c93c6d54cb06c3a34)IMX\_CCM\_FLEXIO1\_CLK

| #define IMX\_CCM\_FLEXIO1\_CLK   0x1100UL |
| --- |

## [◆ ](#a2817b49a9d77b1f02f854967bf160405)IMX\_CCM\_FLEXIO2\_3\_CLK

| #define IMX\_CCM\_FLEXIO2\_3\_CLK   0x1101UL |
| --- |

## [◆ ](#aa471a61b4b453551839b29322ec21422)IMX\_CCM\_FLEXSPI2\_CLK

| #define IMX\_CCM\_FLEXSPI2\_CLK   0x0F01UL |
| --- |

## [◆ ](#a5f86bba59cc685682df75e66a5d64cea)IMX\_CCM\_FLEXSPI\_CLK

| #define IMX\_CCM\_FLEXSPI\_CLK   0x0F00UL |
| --- |

## [◆ ](#aadc28bb4c97c89e86a8a437262a3afad)IMX\_CCM\_GPT\_CLK

| #define IMX\_CCM\_GPT\_CLK   0x0A00UL |
| --- |

## [◆ ](#a95422e9f72395bfd62899d2e5c35bf46)IMX\_CCM\_GPT\_IPG\_CLK

| #define IMX\_CCM\_GPT\_IPG\_CLK   0x1300UL |
| --- |

## [◆ ](#a30f30d268fb9aae738f27161e6028f73)IMX\_CCM\_INSTANCE\_MASK

| #define IMX\_CCM\_INSTANCE\_MASK   0x00FFUL |
| --- |

## [◆ ](#ac970114caf03b14bf6d3f2ff04f548dc)IMX\_CCM\_LPI2C\_CLK

| #define IMX\_CCM\_LPI2C\_CLK   0x0400UL |
| --- |

## [◆ ](#a169487d4c020dee2492e36202fa39158)IMX\_CCM\_LPSPI\_CLK

| #define IMX\_CCM\_LPSPI\_CLK   0x0500UL |
| --- |

## [◆ ](#a96e62b5b478ee548a1e52b7189a73817)IMX\_CCM\_LPUART1\_CLK

| #define IMX\_CCM\_LPUART1\_CLK   0x0300UL |
| --- |

## [◆ ](#a46255999d02ae6161981374872e065cf)IMX\_CCM\_LPUART2\_CLK

| #define IMX\_CCM\_LPUART2\_CLK   0x0301UL |
| --- |

## [◆ ](#a6676eb59f3d665c2a9bba7aae24228ca)IMX\_CCM\_LPUART3\_CLK

| #define IMX\_CCM\_LPUART3\_CLK   0x0302UL |
| --- |

## [◆ ](#a9647111e5a5af6e8e67e059009490974)IMX\_CCM\_LPUART4\_CLK

| #define IMX\_CCM\_LPUART4\_CLK   0x0303UL |
| --- |

## [◆ ](#acd84397a25a81c7f315c7740049d570a)IMX\_CCM\_LPUART5\_CLK

| #define IMX\_CCM\_LPUART5\_CLK   0x0304UL |
| --- |

## [◆ ](#a3c6916f6ff4fae75dc51177e25d51642)IMX\_CCM\_LPUART6\_CLK

| #define IMX\_CCM\_LPUART6\_CLK   0x0305UL |
| --- |

## [◆ ](#a4f2f07925d50b73cdc218d1f99cedf98)IMX\_CCM\_LPUART7\_CLK

| #define IMX\_CCM\_LPUART7\_CLK   0x0306UL |
| --- |

## [◆ ](#a8db4fa3e674535ba490d89a52979cad0)IMX\_CCM\_LPUART8\_CLK

| #define IMX\_CCM\_LPUART8\_CLK   0x0307UL |
| --- |

## [◆ ](#a01fa41a7ad66c54b1c19455b6160bbc2)IMX\_CCM\_LPUART\_CLK

| #define IMX\_CCM\_LPUART\_CLK   0x0300UL |
| --- |

## [◆ ](#aa31bf3cf51ff3af717f0d4037eeaa1c9)IMX\_CCM\_PERIPHERAL\_MASK

| #define IMX\_CCM\_PERIPHERAL\_MASK   0xFF00UL |
| --- |

## [◆ ](#a0089a79d220e999a846afc32a827aeb7)IMX\_CCM\_PIT\_CLK

| #define IMX\_CCM\_PIT\_CLK   0x1000UL |
| --- |

## [◆ ](#afcda3a44b4029872bfa5d219f10dd506)IMX\_CCM\_PLATFORM\_CLK

| #define IMX\_CCM\_PLATFORM\_CLK   0x0100UL |
| --- |

## [◆ ](#acbc9256c26bb1232c5ca0eb8bfe52c22)IMX\_CCM\_PWM\_CLK

| #define IMX\_CCM\_PWM\_CLK   0x0C00UL |
| --- |

## [◆ ](#a0cc7a30460bef2b0e6772a91539203a8)IMX\_CCM\_QTMR\_CLK

| #define IMX\_CCM\_QTMR\_CLK   0x0D00UL |
| --- |

## [◆ ](#a398527cf42962caf290b9ce1e5d7f9ac)IMX\_CCM\_SAI1\_CLK

| #define IMX\_CCM\_SAI1\_CLK   0x0B00UL |
| --- |

## [◆ ](#aae6ea492162692b3ae2dc6aed60cc08d)IMX\_CCM\_SAI2\_CLK

| #define IMX\_CCM\_SAI2\_CLK   0x0B01UL |
| --- |

## [◆ ](#a28779c577a92d4806239fe6e254d1a84)IMX\_CCM\_SAI3\_CLK

| #define IMX\_CCM\_SAI3\_CLK   0x0B02UL |
| --- |

## [◆ ](#a62f00f098b8ee58612dd7cd5cc9da1e3)IMX\_CCM\_UART1\_CLK

| #define IMX\_CCM\_UART1\_CLK   0x0800UL |
| --- |

## [◆ ](#a87c6bd30a90ca0cfdba829ae3cef2323)IMX\_CCM\_UART2\_CLK

| #define IMX\_CCM\_UART2\_CLK   0x0801UL |
| --- |

## [◆ ](#aca209cf9c7038df4c53cb6ee930dfcd9)IMX\_CCM\_UART3\_CLK

| #define IMX\_CCM\_UART3\_CLK   0x0802UL |
| --- |

## [◆ ](#a87564f52751e46be9ca0cec40c197f24)IMX\_CCM\_UART4\_CLK

| #define IMX\_CCM\_UART4\_CLK   0x0803UL |
| --- |

## [◆ ](#a3f07127852de7ae5516c376589f1f780)IMX\_CCM\_USDHC1\_CLK

| #define IMX\_CCM\_USDHC1\_CLK   0x0600UL |
| --- |

## [◆ ](#a4596ce38e656971ec5330dab452bd04c)IMX\_CCM\_USDHC2\_CLK

| #define IMX\_CCM\_USDHC2\_CLK   0x0601UL |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [clock](dir_6e9992ac75fd0b7a50e889108957c907.md)
- [imx\_ccm.h](imx__ccm_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
