---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/imx__ccm__rev2_8h.html
original_path: doxygen/html/imx__ccm__rev2_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

imx\_ccm\_rev2.h File Reference

[Go to the source code of this file.](imx__ccm__rev2_8h_source.md)

| Macros | |
| --- | --- |
| #define | [IMX\_CCM\_PERIPHERAL\_MASK](#aa31bf3cf51ff3af717f0d4037eeaa1c9)   0xFF00UL |
| #define | [IMX\_CCM\_INSTANCE\_MASK](#a30f30d268fb9aae738f27161e6028f73)   0xFFUL |
| #define | [IMX\_CCM\_CORESYS\_CLK](#ab1e95e431d7486c814c969d0d9c57559)   0 |
| #define | [IMX\_CCM\_PLATFORM\_CLK](#afcda3a44b4029872bfa5d219f10dd506)   0x1UL |
| #define | [IMX\_CCM\_BUS\_CLK](#a0f9e44ec176274d3792bb2dd3e21a28b)   0x2UL |
| #define | [IMX\_CCM\_LPUART\_CLK](#a01fa41a7ad66c54b1c19455b6160bbc2)   0x300UL |
| #define | [IMX\_CCM\_LPUART1\_CLK](#a96e62b5b478ee548a1e52b7189a73817)   0x300UL |
| #define | [IMX\_CCM\_LPUART2\_CLK](#a46255999d02ae6161981374872e065cf)   0x301UL |
| #define | [IMX\_CCM\_LPUART3\_CLK](#a6676eb59f3d665c2a9bba7aae24228ca)   0x302UL |
| #define | [IMX\_CCM\_LPUART4\_CLK](#a9647111e5a5af6e8e67e059009490974)   0x303UL |
| #define | [IMX\_CCM\_LPUART5\_CLK](#acd84397a25a81c7f315c7740049d570a)   0x304UL |
| #define | [IMX\_CCM\_LPUART6\_CLK](#a3c6916f6ff4fae75dc51177e25d51642)   0x305UL |
| #define | [IMX\_CCM\_LPUART7\_CLK](#a4f2f07925d50b73cdc218d1f99cedf98)   0x306UL |
| #define | [IMX\_CCM\_LPUART8\_CLK](#a8db4fa3e674535ba490d89a52979cad0)   0x307UL |
| #define | [IMX\_CCM\_LPUART9\_CLK](#a0a6f1a1a8141d825058fd5a2c2ca3914)   0x308UL |
| #define | [IMX\_CCM\_LPUART10\_CLK](#a24307153d0dbf07b908ab1876ae1a4bc)   0x309UL |
| #define | [IMX\_CCM\_LPUART11\_CLK](#af539f30a7a6cd9ee4aba7f2415b5b3e6)   0x30aUL |
| #define | [IMX\_CCM\_LPUART12\_CLK](#a68c212e56058fd3f59c8bb7bd7f25984)   0x30bUL |
| #define | [IMX\_CCM\_LPI2C\_CLK](#ac970114caf03b14bf6d3f2ff04f548dc)   0x400UL |
| #define | [IMX\_CCM\_LPI2C1\_CLK](#a0868c0eeb69b0e67d6e2d022a9e55035)   0x400UL |
| #define | [IMX\_CCM\_LPI2C2\_CLK](#a1a684ee49ada9866d61df70c8757bbf6)   0x401UL |
| #define | [IMX\_CCM\_LPI2C3\_CLK](#a5d809939798eacedbbf59f38a57fb5ba)   0x402UL |
| #define | [IMX\_CCM\_LPI2C4\_CLK](#aac755270370e533fb3f78e471f0efac7)   0x403UL |
| #define | [IMX\_CCM\_LPI2C5\_CLK](#a4a73ff0aa1615dfc1171689dbb76636b)   0x404UL |
| #define | [IMX\_CCM\_LPI2C6\_CLK](#a61d52e2b71b0eef06d76c8261df4ac1b)   0x405UL |
| #define | [IMX\_CCM\_LPI2C7\_CLK](#a002cc9eac38583fca551917c1a1fa299)   0x406UL |
| #define | [IMX\_CCM\_LPI2C8\_CLK](#ae7cecaf7c7b40bbc2654c3417ac729cc)   0x407UL |
| #define | [IMX\_CCM\_LPSPI\_CLK](#a169487d4c020dee2492e36202fa39158)   0x500UL |
| #define | [IMX\_CCM\_LPSPI1\_CLK](#aaa28d51204ece1b636cfb18ae1c40c36)   0x500UL |
| #define | [IMX\_CCM\_LPSPI2\_CLK](#af9033f72e88c27d5b423201a23ac8a31)   0x501UL |
| #define | [IMX\_CCM\_LPSPI3\_CLK](#a95f654b51e3b94c4f031734761b7db28)   0x502UL |
| #define | [IMX\_CCM\_LPSPI4\_CLK](#a7ef7e62f3bc8b4dc6033628bb54d9f48)   0x503UL |
| #define | [IMX\_CCM\_LPSPI5\_CLK](#ab77afa02a9375dac8d5241db2f6dcb1e)   0x504UL |
| #define | [IMX\_CCM\_LPSPI6\_CLK](#aeaef0fae23329ccf26957f53414bb50e)   0x505UL |
| #define | [IMX\_CCM\_LPSPI7\_CLK](#a6d0905600641bf75064eb4c595e8137f)   0x506UL |
| #define | [IMX\_CCM\_LPSPI8\_CLK](#a29897a97b6c47d61bc7e05785b54ea50)   0x507UL |
| #define | [IMX\_CCM\_USDHC1\_CLK](#a3f07127852de7ae5516c376589f1f780)   0x600UL |
| #define | [IMX\_CCM\_USDHC2\_CLK](#a4596ce38e656971ec5330dab452bd04c)   0x601UL |
| #define | [IMX\_CCM\_EDMA\_CLK](#aa82ff051d04371deee96c754d93abb57)   0x700UL |
| #define | [IMX\_CCM\_EDMA\_LPSR\_CLK](#a6bd4f0c4c8fa888f986dedce8e0fc950)   0x701UL |
| #define | [IMX\_CCM\_PWM\_CLK](#acbc9256c26bb1232c5ca0eb8bfe52c22)   0x800UL |
| #define | [IMX\_CCM\_CAN\_CLK](#aded96aef4768dd5f01d14a163cd7487d)   0x900UL |
| #define | [IMX\_CCM\_CAN1\_CLK](#a8b4a233a49bf6b078b2b0b51883a49c7)   0x900UL |
| #define | [IMX\_CCM\_CAN2\_CLK](#ae82e9c205254fb85adaedc423cfc7e27)   0x901UL |
| #define | [IMX\_CCM\_CAN3\_CLK](#a16a7e40f69be4d33dd9a9e6aeff03d5e)   0x902UL |
| #define | [IMX\_CCM\_GPT\_CLK](#aadc28bb4c97c89e86a8a437262a3afad)   0x1000UL |
| #define | [IMX\_CCM\_GPT1\_CLK](#a63ddd8dcc8dca4c5a206348d67c0b57d)   0x1000UL |
| #define | [IMX\_CCM\_GPT2\_CLK](#a8fafcbbe14088a3372e681d0f4071ac3)   0x1001UL |
| #define | [IMX\_CCM\_GPT3\_CLK](#a08cba39dbed192509df1e404d49625d0)   0x1002UL |
| #define | [IMX\_CCM\_GPT4\_CLK](#a454f61392489e49a6534b1c115e6e868)   0x1003UL |
| #define | [IMX\_CCM\_GPT5\_CLK](#a491b53b9f223744586578ea0c1db987f)   0x1004UL |
| #define | [IMX\_CCM\_GPT6\_CLK](#a5892393e285e3cb1b9fcb5a65e29b66e)   0x1005UL |
| #define | [IMX\_CCM\_SAI1\_CLK](#a398527cf42962caf290b9ce1e5d7f9ac)   0x2000UL |
| #define | [IMX\_CCM\_SAI2\_CLK](#aae6ea492162692b3ae2dc6aed60cc08d)   0x2001UL |
| #define | [IMX\_CCM\_SAI3\_CLK](#a28779c577a92d4806239fe6e254d1a84)   0x2002UL |
| #define | [IMX\_CCM\_SAI4\_CLK](#a598ae9134610f955e78e46a37c063098)   0x2003UL |
| #define | [IMX\_CCM\_ENET\_CLK](#aaeff78179dff600c88c1d1986b3976cd)   0x3000UL |
| #define | [IMX\_CCM\_ENET\_PLL](#a2a4beef16589b00f9aca825e7419e9ff)   0x3001UL |
| #define | [IMX\_CCM\_FLEXSPI\_CLK](#a5f86bba59cc685682df75e66a5d64cea)   0x4000UL |
| #define | [IMX\_CCM\_FLEXSPI2\_CLK](#aa471a61b4b453551839b29322ec21422)   0x4001UL |

## Macro Definition Documentation

## [◆ ](#a0f9e44ec176274d3792bb2dd3e21a28b)IMX\_CCM\_BUS\_CLK

| #define IMX\_CCM\_BUS\_CLK   0x2UL |
| --- |

## [◆ ](#a8b4a233a49bf6b078b2b0b51883a49c7)IMX\_CCM\_CAN1\_CLK

| #define IMX\_CCM\_CAN1\_CLK   0x900UL |
| --- |

## [◆ ](#ae82e9c205254fb85adaedc423cfc7e27)IMX\_CCM\_CAN2\_CLK

| #define IMX\_CCM\_CAN2\_CLK   0x901UL |
| --- |

## [◆ ](#a16a7e40f69be4d33dd9a9e6aeff03d5e)IMX\_CCM\_CAN3\_CLK

| #define IMX\_CCM\_CAN3\_CLK   0x902UL |
| --- |

## [◆ ](#aded96aef4768dd5f01d14a163cd7487d)IMX\_CCM\_CAN\_CLK

| #define IMX\_CCM\_CAN\_CLK   0x900UL |
| --- |

## [◆ ](#ab1e95e431d7486c814c969d0d9c57559)IMX\_CCM\_CORESYS\_CLK

| #define IMX\_CCM\_CORESYS\_CLK   0 |
| --- |

## [◆ ](#aa82ff051d04371deee96c754d93abb57)IMX\_CCM\_EDMA\_CLK

| #define IMX\_CCM\_EDMA\_CLK   0x700UL |
| --- |

## [◆ ](#a6bd4f0c4c8fa888f986dedce8e0fc950)IMX\_CCM\_EDMA\_LPSR\_CLK

| #define IMX\_CCM\_EDMA\_LPSR\_CLK   0x701UL |
| --- |

## [◆ ](#aaeff78179dff600c88c1d1986b3976cd)IMX\_CCM\_ENET\_CLK

| #define IMX\_CCM\_ENET\_CLK   0x3000UL |
| --- |

## [◆ ](#a2a4beef16589b00f9aca825e7419e9ff)IMX\_CCM\_ENET\_PLL

| #define IMX\_CCM\_ENET\_PLL   0x3001UL |
| --- |

## [◆ ](#aa471a61b4b453551839b29322ec21422)IMX\_CCM\_FLEXSPI2\_CLK

| #define IMX\_CCM\_FLEXSPI2\_CLK   0x4001UL |
| --- |

## [◆ ](#a5f86bba59cc685682df75e66a5d64cea)IMX\_CCM\_FLEXSPI\_CLK

| #define IMX\_CCM\_FLEXSPI\_CLK   0x4000UL |
| --- |

## [◆ ](#a63ddd8dcc8dca4c5a206348d67c0b57d)IMX\_CCM\_GPT1\_CLK

| #define IMX\_CCM\_GPT1\_CLK   0x1000UL |
| --- |

## [◆ ](#a8fafcbbe14088a3372e681d0f4071ac3)IMX\_CCM\_GPT2\_CLK

| #define IMX\_CCM\_GPT2\_CLK   0x1001UL |
| --- |

## [◆ ](#a08cba39dbed192509df1e404d49625d0)IMX\_CCM\_GPT3\_CLK

| #define IMX\_CCM\_GPT3\_CLK   0x1002UL |
| --- |

## [◆ ](#a454f61392489e49a6534b1c115e6e868)IMX\_CCM\_GPT4\_CLK

| #define IMX\_CCM\_GPT4\_CLK   0x1003UL |
| --- |

## [◆ ](#a491b53b9f223744586578ea0c1db987f)IMX\_CCM\_GPT5\_CLK

| #define IMX\_CCM\_GPT5\_CLK   0x1004UL |
| --- |

## [◆ ](#a5892393e285e3cb1b9fcb5a65e29b66e)IMX\_CCM\_GPT6\_CLK

| #define IMX\_CCM\_GPT6\_CLK   0x1005UL |
| --- |

## [◆ ](#aadc28bb4c97c89e86a8a437262a3afad)IMX\_CCM\_GPT\_CLK

| #define IMX\_CCM\_GPT\_CLK   0x1000UL |
| --- |

## [◆ ](#a30f30d268fb9aae738f27161e6028f73)IMX\_CCM\_INSTANCE\_MASK

| #define IMX\_CCM\_INSTANCE\_MASK   0xFFUL |
| --- |

## [◆ ](#a0868c0eeb69b0e67d6e2d022a9e55035)IMX\_CCM\_LPI2C1\_CLK

| #define IMX\_CCM\_LPI2C1\_CLK   0x400UL |
| --- |

## [◆ ](#a1a684ee49ada9866d61df70c8757bbf6)IMX\_CCM\_LPI2C2\_CLK

| #define IMX\_CCM\_LPI2C2\_CLK   0x401UL |
| --- |

## [◆ ](#a5d809939798eacedbbf59f38a57fb5ba)IMX\_CCM\_LPI2C3\_CLK

| #define IMX\_CCM\_LPI2C3\_CLK   0x402UL |
| --- |

## [◆ ](#aac755270370e533fb3f78e471f0efac7)IMX\_CCM\_LPI2C4\_CLK

| #define IMX\_CCM\_LPI2C4\_CLK   0x403UL |
| --- |

## [◆ ](#a4a73ff0aa1615dfc1171689dbb76636b)IMX\_CCM\_LPI2C5\_CLK

| #define IMX\_CCM\_LPI2C5\_CLK   0x404UL |
| --- |

## [◆ ](#a61d52e2b71b0eef06d76c8261df4ac1b)IMX\_CCM\_LPI2C6\_CLK

| #define IMX\_CCM\_LPI2C6\_CLK   0x405UL |
| --- |

## [◆ ](#a002cc9eac38583fca551917c1a1fa299)IMX\_CCM\_LPI2C7\_CLK

| #define IMX\_CCM\_LPI2C7\_CLK   0x406UL |
| --- |

## [◆ ](#ae7cecaf7c7b40bbc2654c3417ac729cc)IMX\_CCM\_LPI2C8\_CLK

| #define IMX\_CCM\_LPI2C8\_CLK   0x407UL |
| --- |

## [◆ ](#ac970114caf03b14bf6d3f2ff04f548dc)IMX\_CCM\_LPI2C\_CLK

| #define IMX\_CCM\_LPI2C\_CLK   0x400UL |
| --- |

## [◆ ](#aaa28d51204ece1b636cfb18ae1c40c36)IMX\_CCM\_LPSPI1\_CLK

| #define IMX\_CCM\_LPSPI1\_CLK   0x500UL |
| --- |

## [◆ ](#af9033f72e88c27d5b423201a23ac8a31)IMX\_CCM\_LPSPI2\_CLK

| #define IMX\_CCM\_LPSPI2\_CLK   0x501UL |
| --- |

## [◆ ](#a95f654b51e3b94c4f031734761b7db28)IMX\_CCM\_LPSPI3\_CLK

| #define IMX\_CCM\_LPSPI3\_CLK   0x502UL |
| --- |

## [◆ ](#a7ef7e62f3bc8b4dc6033628bb54d9f48)IMX\_CCM\_LPSPI4\_CLK

| #define IMX\_CCM\_LPSPI4\_CLK   0x503UL |
| --- |

## [◆ ](#ab77afa02a9375dac8d5241db2f6dcb1e)IMX\_CCM\_LPSPI5\_CLK

| #define IMX\_CCM\_LPSPI5\_CLK   0x504UL |
| --- |

## [◆ ](#aeaef0fae23329ccf26957f53414bb50e)IMX\_CCM\_LPSPI6\_CLK

| #define IMX\_CCM\_LPSPI6\_CLK   0x505UL |
| --- |

## [◆ ](#a6d0905600641bf75064eb4c595e8137f)IMX\_CCM\_LPSPI7\_CLK

| #define IMX\_CCM\_LPSPI7\_CLK   0x506UL |
| --- |

## [◆ ](#a29897a97b6c47d61bc7e05785b54ea50)IMX\_CCM\_LPSPI8\_CLK

| #define IMX\_CCM\_LPSPI8\_CLK   0x507UL |
| --- |

## [◆ ](#a169487d4c020dee2492e36202fa39158)IMX\_CCM\_LPSPI\_CLK

| #define IMX\_CCM\_LPSPI\_CLK   0x500UL |
| --- |

## [◆ ](#a24307153d0dbf07b908ab1876ae1a4bc)IMX\_CCM\_LPUART10\_CLK

| #define IMX\_CCM\_LPUART10\_CLK   0x309UL |
| --- |

## [◆ ](#af539f30a7a6cd9ee4aba7f2415b5b3e6)IMX\_CCM\_LPUART11\_CLK

| #define IMX\_CCM\_LPUART11\_CLK   0x30aUL |
| --- |

## [◆ ](#a68c212e56058fd3f59c8bb7bd7f25984)IMX\_CCM\_LPUART12\_CLK

| #define IMX\_CCM\_LPUART12\_CLK   0x30bUL |
| --- |

## [◆ ](#a96e62b5b478ee548a1e52b7189a73817)IMX\_CCM\_LPUART1\_CLK

| #define IMX\_CCM\_LPUART1\_CLK   0x300UL |
| --- |

## [◆ ](#a46255999d02ae6161981374872e065cf)IMX\_CCM\_LPUART2\_CLK

| #define IMX\_CCM\_LPUART2\_CLK   0x301UL |
| --- |

## [◆ ](#a6676eb59f3d665c2a9bba7aae24228ca)IMX\_CCM\_LPUART3\_CLK

| #define IMX\_CCM\_LPUART3\_CLK   0x302UL |
| --- |

## [◆ ](#a9647111e5a5af6e8e67e059009490974)IMX\_CCM\_LPUART4\_CLK

| #define IMX\_CCM\_LPUART4\_CLK   0x303UL |
| --- |

## [◆ ](#acd84397a25a81c7f315c7740049d570a)IMX\_CCM\_LPUART5\_CLK

| #define IMX\_CCM\_LPUART5\_CLK   0x304UL |
| --- |

## [◆ ](#a3c6916f6ff4fae75dc51177e25d51642)IMX\_CCM\_LPUART6\_CLK

| #define IMX\_CCM\_LPUART6\_CLK   0x305UL |
| --- |

## [◆ ](#a4f2f07925d50b73cdc218d1f99cedf98)IMX\_CCM\_LPUART7\_CLK

| #define IMX\_CCM\_LPUART7\_CLK   0x306UL |
| --- |

## [◆ ](#a8db4fa3e674535ba490d89a52979cad0)IMX\_CCM\_LPUART8\_CLK

| #define IMX\_CCM\_LPUART8\_CLK   0x307UL |
| --- |

## [◆ ](#a0a6f1a1a8141d825058fd5a2c2ca3914)IMX\_CCM\_LPUART9\_CLK

| #define IMX\_CCM\_LPUART9\_CLK   0x308UL |
| --- |

## [◆ ](#a01fa41a7ad66c54b1c19455b6160bbc2)IMX\_CCM\_LPUART\_CLK

| #define IMX\_CCM\_LPUART\_CLK   0x300UL |
| --- |

## [◆ ](#aa31bf3cf51ff3af717f0d4037eeaa1c9)IMX\_CCM\_PERIPHERAL\_MASK

| #define IMX\_CCM\_PERIPHERAL\_MASK   0xFF00UL |
| --- |

## [◆ ](#afcda3a44b4029872bfa5d219f10dd506)IMX\_CCM\_PLATFORM\_CLK

| #define IMX\_CCM\_PLATFORM\_CLK   0x1UL |
| --- |

## [◆ ](#acbc9256c26bb1232c5ca0eb8bfe52c22)IMX\_CCM\_PWM\_CLK

| #define IMX\_CCM\_PWM\_CLK   0x800UL |
| --- |

## [◆ ](#a398527cf42962caf290b9ce1e5d7f9ac)IMX\_CCM\_SAI1\_CLK

| #define IMX\_CCM\_SAI1\_CLK   0x2000UL |
| --- |

## [◆ ](#aae6ea492162692b3ae2dc6aed60cc08d)IMX\_CCM\_SAI2\_CLK

| #define IMX\_CCM\_SAI2\_CLK   0x2001UL |
| --- |

## [◆ ](#a28779c577a92d4806239fe6e254d1a84)IMX\_CCM\_SAI3\_CLK

| #define IMX\_CCM\_SAI3\_CLK   0x2002UL |
| --- |

## [◆ ](#a598ae9134610f955e78e46a37c063098)IMX\_CCM\_SAI4\_CLK

| #define IMX\_CCM\_SAI4\_CLK   0x2003UL |
| --- |

## [◆ ](#a3f07127852de7ae5516c376589f1f780)IMX\_CCM\_USDHC1\_CLK

| #define IMX\_CCM\_USDHC1\_CLK   0x600UL |
| --- |

## [◆ ](#a4596ce38e656971ec5330dab452bd04c)IMX\_CCM\_USDHC2\_CLK

| #define IMX\_CCM\_USDHC2\_CLK   0x601UL |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [clock](dir_6e9992ac75fd0b7a50e889108957c907.md)
- [imx\_ccm\_rev2.h](imx__ccm__rev2_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
