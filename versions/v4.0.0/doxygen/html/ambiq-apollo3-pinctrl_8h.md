---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/ambiq-apollo3-pinctrl_8h.html
original_path: doxygen/html/ambiq-apollo3-pinctrl_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ambiq-apollo3-pinctrl.h File Reference

[Go to the source code of this file.](ambiq-apollo3-pinctrl_8h_source.md)

| Macros | |
| --- | --- |
| #define | [APOLLO3\_ALT\_FUNC\_POS](#aec76f3cfd2a609e60eabf5628f5ee698)   0 |
| #define | [APOLLO3\_ALT\_FUNC\_MASK](#aa00706366b69ceb3628404acb54d08c3)   0xf |
| #define | [APOLLO3\_PIN\_NUM\_POS](#a31b09dab4803a326db645412cf2d7acd)   4 |
| #define | [APOLLO3\_PIN\_NUM\_MASK](#a71eb3e43677ab0f8c9abd0fc61aafaab)   0x7f |
| #define | [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(pin\_num, alt\_func) |
| #define | [SLSCL\_P0](#a3a72f1023828af4b3766cc0714c404b2)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(0, 0) |
| #define | [SLSCK\_P0](#ae72cb1519562643c48a8ffff88dc9d00)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(0, 1) |
| #define | [CLKOUT\_P0](#a95fca27e19b245305579cbad18962f00)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(0, 2) |
| #define | [GPIO\_P0](#ada3eedfe2cf44d8f0f1c21d10fc7c81a)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(0, 3) |
| #define | [MSPI0\_4\_P0](#ac619aa033a346a49cd8e1c501831c852)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(0, 5) |
| #define | [NCE0\_P0](#a2f7a5ec8bae150c5d845a85d65991107)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(0, 7) |
| #define | [SLSDAWIR3\_P1](#ae5b84a6fa44069d704c6c87113bef6e7)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(1, 0) |
| #define | [SLMOSI\_P1](#a4fd87e65fcf8776a98224ca1d468b0ad)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(1, 1) |
| #define | [UART0TX\_P1](#aa237cfc2d6eda1c3ddf349b5a3330898)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(1, 2) |
| #define | [GPIO\_P1](#af7a3fb155e6285875e885d5a6344041d)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(1, 3) |
| #define | [MSPI0\_5\_P1](#a75d2d20c972028ad79e046b31df7aaca)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(1, 5) |
| #define | [NCE1\_P1](#aad38da06e56246b4ed48ddbf43f1aaca)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(1, 7) |
| #define | [UART1RX\_P2](#a3795e6445756b68c436b6d0fb1c7813b)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(2, 0) |
| #define | [SLMISO\_P2](#a06beb22570d100e28198606d21909a6c)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(2, 1) |
| #define | [UART0RX\_P2](#aeb4da21d8f3fdb747865ff6b6a7ea49e)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(2, 2) |
| #define | [GPIO\_P2](#aea5b197be9a863a6db90cb9d42b8a9f2)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(2, 3) |
| #define | [MSPI0\_6\_P2](#a112ffcf686debe615f04a1fc3c20ceab)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(2, 5) |
| #define | [NCE2\_P2](#a41c7834b7cc3a8f2f75021ec9ebedf6a)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(2, 7) |
| #define | [UA0RTS\_P3](#ae5123e7f8df58cc8ca300bc955a855d3)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(3, 0) |
| #define | [SLNCE\_P3](#a42fc82a09d814a6774ee02b1b0228cd8)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(3, 1) |
| #define | [NCE3\_P3](#a49fa96fac299d83fe34b116fc2e8d586)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(3, 2) |
| #define | [GPIO\_P3](#af4024d1ac41ed0426ca701ea851dcd82)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(3, 3) |
| #define | [MSPI0\_7\_P3](#a5e93b8d0e2c70144bfaa034aa6dea0d8)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(3, 5) |
| #define | [TRIG1\_P3](#a2afa9eb9453ab24b55280c9680e8bca7)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(3, 6) |
| #define | [I2SWCLK\_P3](#a2b3c5edbedf68592bfa84e0df9905396)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(3, 7) |
| #define | [UA0CTS\_P4](#a7c15b0f583db4314e7b315e553e6ec89)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(4, 0) |
| #define | [SLINT\_P4](#a29c616828e653cb4f0cecaca1f0bc8f1)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(4, 1) |
| #define | [NCE4\_P4](#a3019076e21641ad28be64b29a4b2c671)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(4, 2) |
| #define | [GPIO\_P4](#aea71dd1d14466cec98ab057ece573f75)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(4, 3) |
| #define | [UART1RX\_P4](#a6c0d9abe0eabefce033125e3d1519e56)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(4, 5) |
| #define | [CTIM17\_P4](#ae3a25bc2296db097c9d774e801f146ef)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(4, 6) |
| #define | [MSPI0\_2\_P4](#a6395a199be7a3ef0d69976a41253282d)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(4, 7) |
| #define | [M0SCL\_P5](#a89285a703eabc9b9cc9c962dd7f8856c)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(5, 0) |
| #define | [M0SCK\_P5](#abf59b5c6ff03c8a2652d3bc72b872295)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(5, 1) |
| #define | [UA0RTS\_P5](#a9af295a6b30a9ebfa26d89187a765817)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(5, 2) |
| #define | [GPIO\_P5](#a8b6393ba023af44294a82048f4d7b7fb)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(5, 3) |
| #define | [CT8\_P5](#a8427da089d2101bd9fc10ce6f1933aa8)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(5, 7) |
| #define | [M0SDAWIR3\_P6](#a70ecddbefb03c277a58ab1f8c6f4972c)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(6, 0) |
| #define | [M0MISO\_P6](#a01e0417e4c10476d720baa251bf37f41)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(6, 1) |
| #define | [UA0CTS\_P6](#a0ec1a55c1287c1b4524670c836aa3610)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(6, 2) |
| #define | [GPIO\_P6](#ab92e5b2728491c7718e22490337a877c)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(6, 3) |
| #define | [CTIM10\_P6](#a00a0fc70b33db841fd0551b7c262253e)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(6, 5) |
| #define | [I2SDAT\_P6](#ae3de66bb2e7fd0e635de7945543bfb07)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(6, 7) |
| #define | [NCE7\_P7](#ac34242faa4992e4acc075a36264d7187)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(7, 0) |
| #define | [M0MOSI\_P7](#aa8d862944d509743683a67127dfa38bd)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(7, 1) |
| #define | [CLKOUT\_P7](#a44e6475e1fcd9fbb522a48dea35e8599)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(7, 2) |
| #define | [GPIO\_P7](#a56c293ec75689c3c233d7a0ad4d7428e)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(7, 3) |
| #define | [TRIG0\_P7](#a00614cfc545401d5e8cb9f1e51848571)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(7, 4) |
| #define | [UART0TX\_P7](#af0fd57799f26a1157516475c639e453b)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(7, 5) |
| #define | [CTIM19\_P7](#af38d97658c4bd9cbb45e822331999a0d)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(7, 7) |
| #define | [M1SCL\_P8](#a78f6a3daba1c3af73d6f56e201716c9d)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(8, 0) |
| #define | [M1SCK\_P8](#aeca27870849b7a78edc8fe37b9966f23)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(8, 1) |
| #define | [NCE8\_P8](#a6c400fdb4e2e68a5a28f2aade3509822)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(8, 2) |
| #define | [GPIO\_P8](#a98e2e72127f9d8302c72d588b005ad43)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(8, 3) |
| #define | [SCCCLK\_P8](#a656853201d5b7b94a3019767ec187d0c)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(8, 4) |
| #define | [UART1TX\_P8](#a9d932772131c6c1cd418e026d27975fc)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(8, 6) |
| #define | [M1SDAWIR3\_P9](#a8a5ee0496cfaf6fe7c0475459ab7ee23)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(9, 0) |
| #define | [M1MISO\_P9](#a044f3f8861bdfe85899102c4a51dd663)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(9, 1) |
| #define | [NCE9\_P9](#aa92d1c97c14770e3e29a271706d76a28)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(9, 2) |
| #define | [GPIO\_P9](#a62ba7982361959a0ff4013c825611344)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(9, 3) |
| #define | [SCCIO\_P9](#a0def8b127d3740da2bb3ae2b44d0095c)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(9, 4) |
| #define | [UART1RX\_P9](#a6c829d8791c5ef247418f022d37abe26)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(9, 6) |
| #define | [UART1TX\_P10](#abcb9b4ed6c81f79f0d2d3f96c0907489)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(10, 0) |
| #define | [M1MOSI\_P10](#aa99ecc3b8b3e072f245f3779564d9b35)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(10, 1) |
| #define | [NCE10\_P10](#aad947baa0652e59cb21735eae01eca09)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(10, 2) |
| #define | [GPIO\_P10](#aeae1f6c04e5fc3c420c3c2311e91c0fb)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(10, 3) |
| #define | [PDMCLK\_P10](#a432af451cbdf1a8e0137e61def76d525)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(10, 4) |
| #define | [UA1RTS\_P10](#ab98a61028f7a8b5e45841dc3d5ab0672)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(10, 6) |
| #define | [ADCSE2\_P11](#a0af7147f664fc0c56acdfc63e76558bc)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(11, 0) |
| #define | [NCE11\_P11](#ab635978b874de8fbe6f96506b06ae5f1)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(11, 1) |
| #define | [CTIM31\_P11](#a994df6ba3173398db50c15364d07ede5)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(11, 2) |
| #define | [GPIO\_P11](#a1e2a5bd418526ffe665b93088178edc3)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(11, 3) |
| #define | [SLINT\_P11](#acab95c4dfc69402cb93aa80cb368a8ed)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(11, 4) |
| #define | [UA1CTS\_P11](#a0c85b60521c7052487e84b4eb1031be1)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(11, 5) |
| #define | [UART0RX\_P11](#aff7e0941ffab586464b6a42edf32cf84)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(11, 6) |
| #define | [PDMDATA\_P11](#a4a9e07c73a2062220944fac15bc9976c)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(11, 7) |
| #define | [ADCD0NSE9\_P12](#a994b602fed3f5de352a97b9cc9c62607)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(12, 0) |
| #define | [NCE12\_P12](#aeeea37f1af4c943883760c8e273f26a1)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(12, 1) |
| #define | [CT0\_P12](#a9b2a8b0d84975b39cc2fdfb3b3f5c2c0)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(12, 2) |
| #define | [GPIO\_P12](#a2b368e24e962e0bdb34a68dc81a9e929)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(12, 3) |
| #define | [PDMCLK\_P12](#a839ddc0937ffa9b306f491f263ac5ede)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(12, 5) |
| #define | [UA0CTS\_P12](#ab5ce9319d6fc8bdb1496be5f2f015358)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(12, 6) |
| #define | [UART1TX\_P12](#ae86cb0f42ab5ae4105b89838173e7c4f)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(12, 7) |
| #define | [ADCD0PSE8\_P13](#a5c9489a135b6531852d4ebdfc5154f22)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(13, 0) |
| #define | [NCE13\_P13](#a03383f0fcb11b35cac08703aa51cdb56)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(13, 1) |
| #define | [CTIM2\_P13](#a0299d3d82238065f28ea9d60e28e56a0)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(13, 2) |
| #define | [GPIO\_P13](#a9519265fbdd9fb2adfe818baa0ef933f)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(13, 3) |
| #define | [I2SBCLK\_P13](#a9a93f8cb9a71278914a878651ab787c6)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(13, 4) |
| #define | [UA0RTS\_P13](#accb8206aa72638560dfb39d1225d21c3)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(13, 6) |
| #define | [UART1RX\_P13](#a497320f365bff8a29dcb080c154bdc2b)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(13, 7) |
| #define | [ADCD1P\_P14](#a116b6aa61f2ad957c6e205c73b447a1e)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(14, 0) |
| #define | [NCE14\_P14](#a39f9f5d31b34dd21c12439c0a9fd032f)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(14, 1) |
| #define | [UART1TX\_P14](#a95761d7f9fde43b6e1fe1d25ef9d9717)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(14, 2) |
| #define | [GPIO\_P14](#af24f89fe6d38c0db5d7f774e07228678)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(14, 3) |
| #define | [PDMCLK\_P14](#aacd23325f76bea9db0c004775953572d)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(14, 4) |
| #define | [SWDCK\_P14](#af6db4faf2bc7ec69d646e556f3475c6b)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(14, 6) |
| #define | [XT32KHz\_P14](#ad6896d2b4627a39b85ce426e045d55f9)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(14, 7) |
| #define | [ADCD1N\_P15](#ad4979ef8e737edc9304425cbff550802)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(15, 0) |
| #define | [NCE15\_P15](#ab6136185e31fbbb173391d77723de46a)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(15, 1) |
| #define | [UART1RX\_P15](#a077ccd27c6322be3ea942342545ac957)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(15, 2) |
| #define | [GPIO\_P15](#a9147a6e2b351214ab5fe7e5d4f6355d7)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(15, 3) |
| #define | [PDMDATA\_P15](#ae98b714215455ad42b61c940d47a5658)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(15, 4) |
| #define | [SWDIO\_P15](#ac7018578ab5232a026d00f93005cd1d2)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(15, 6) |
| #define | [SWO\_P15](#a335a3b83d4115419e3f752ba6cc6c3c2)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(15, 7) |
| #define | [ADCSE0\_P16](#add33549cde84fd881439b438becb5e33)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(16, 0) |
| #define | [NCE16\_P16](#a5da8200119b0e8a2e6fec1097896edd1)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(16, 1) |
| #define | [TRIG0\_P16](#a7fb00b38e52d1115ce542b0f00b80ac7)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(16, 2) |
| #define | [GPIO\_P16](#a9c21bf7bc952df6b78d19f89f3638833)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(16, 3) |
| #define | [SCCRST\_P16](#a8e59ac2cee69f18f8c23e71e34779d5f)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(16, 4) |
| #define | [CMPIN0\_P16](#a9c9cee6bc621a36d67af82a83ce108b9)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(16, 5) |
| #define | [UART0TX\_P16](#a26f7e4ec8471988685bab0fa0f666af7)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(16, 6) |
| #define | [UA1RTS\_P16](#a5f8c363f21f1a089c1d560a9b975ac41)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(16, 7) |
| #define | [CMPRF1\_P17](#a1269137afa8563480745e3fdf730580b)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(17, 0) |
| #define | [NCE17\_P17](#ab89d7eb6aa6e611a3a95cc1ee913731c)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(17, 1) |
| #define | [TRIG1\_P17](#a3c59efbb8cf2245b113f8d4a5119b7c6)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(17, 2) |
| #define | [GPIO\_P17](#a6a5de6dce7def318bec4f73dd614ec22)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(17, 3) |
| #define | [SCCCLK\_P17](#a532591d82e99327eec3d5ecaf71fd234)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(17, 4) |
| #define | [UART0RX\_P17](#a67731a70bfa50b5a9ac8ff30e1343fba)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(17, 6) |
| #define | [UA1CTS\_P17](#a199a40fbe31c452461f0ba88e2dfc559)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(17, 7) |
| #define | [CMPIN1\_P18](#a7cd80fe3c550eaeb4430512efcc2a296)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(18, 0) |
| #define | [NCE18\_P18](#a566a450bf9afa441315c83bf4d0ce580)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(18, 1) |
| #define | [CTIM4\_P18](#a2255e19add36a65e7f37d7747afbc28b)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(18, 2) |
| #define | [GPIO\_P18](#a8b325ebb0010179509a1a32450ea72af)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(18, 3) |
| #define | [UA0RTS\_P18](#a4c2b318d489aa88d6da183c55d3dbfcf)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(18, 4) |
| #define | [UART1TX\_P18](#a7ef056832ac3d027fdc236914194ab9f)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(18, 6) |
| #define | [SCCIO\_P18](#a3c89b132043f8dabd531955c7f3b67a5)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(18, 7) |
| #define | [CMPRF0\_P19](#a11c7be341b9acbe096a9966044dae194)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(19, 0) |
| #define | [NCE19\_P19](#af9d50128143543f345b8db2d2e3e0918)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(19, 1) |
| #define | [CTIM6\_P19](#a7bebc4982a8d3d917996bdc1348c8b1f)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(19, 2) |
| #define | [GPIO\_P19](#afcadccc574cc0d3c7820ba6b0511612e)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(19, 3) |
| #define | [SCCCLK\_P19](#a5e41d1a7b81ac2349f2b6dece08850a4)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(19, 4) |
| #define | [UART1RX\_P19](#a15b80792320cbe15fd715dbf880bd8a6)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(19, 6) |
| #define | [I2SBCLK\_P19](#ad189a78fbe82f542553e26fe7f06c8b8)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(19, 7) |
| #define | [SWDCK\_P20](#a3885c97e098dfed018491c67065e696c)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(20, 0) |
| #define | [NCE20\_P20](#a8c4f0230a390d43b9a408ec438b5dbe6)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(20, 1) |
| #define | [GPIO\_P20](#afcd63445d3ccf972c95c365f95e30039)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(20, 3) |
| #define | [UART0TX\_P20](#af9acded122c3567a0f7fae29561351e5)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(20, 4) |
| #define | [UART1TX\_P20](#a8d38e7930ecd6a6b51e0da8bdf0b5792)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(20, 5) |
| #define | [I2SBCLK\_P20](#aa16dc261b7d94bbb13919e779208beb1)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(20, 6) |
| #define | [UA1RTS\_P20](#a01a5858ec4972916023b83541ea9a17e)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(20, 7) |
| #define | [SWDIO\_P21](#a184cab7037772c8ca8ecc296ea9c7e48)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(21, 0) |
| #define | [NCE21\_P21](#a3a7292f75cecf7ac798212bbfef2ff3a)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(21, 1) |
| #define | [GPIO\_P21](#a03d53f3d221401ff02a702ef2c8e05c1)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(21, 3) |
| #define | [UART0RX\_P21](#ae642493fcee53d0fe7a2af91e1cac307)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(21, 4) |
| #define | [UART1RX\_P21](#a883993c1c111a42deb3b227ecd38317c)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(21, 5) |
| #define | [SCCRST\_P21](#a8de11c1add0069e7af62e5bbc3b55dbd)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(21, 6) |
| #define | [UA1CTS\_P21](#a8149767283ba99d3fbf7c73ca017a565)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(21, 7) |
| #define | [UART0TX\_P22](#ad7370389dba6304d21d5f95d57dca5dc)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(22, 0) |
| #define | [NCE22\_P22](#a775bbd5124031418e8f5b723e99ac9ab)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(22, 1) |
| #define | [CTIM12\_P22](#ab83b616320654dd99bb1b137f2fc07be)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(22, 2) |
| #define | [GPIO\_P22](#ad0b28de3a514755dfa6b00fe82579f3d)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(22, 3) |
| #define | [PDMCLK\_P22](#ad1b1036bf8cb0807af04662b1c6a9f8f)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(22, 4) |
| #define | [MSPI0\_0\_P22](#a48cbb6097909f658d824a0267cddb6c6)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(22, 6) |
| #define | [SWO\_P22](#af2e7742c9a96fe5ac1a2de402bd5f72f)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(22, 7) |
| #define | [UART0RX\_P23](#aee79208585ea908eac11cadf34078045)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(23, 0) |
| #define | [NCE23\_P23](#a0a52f7e779022ce90fe4d7ce7b200f6d)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(23, 1) |
| #define | [CTIM14\_P23](#a884a5c14156ff1f62b63f70aaf55a380)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(23, 2) |
| #define | [GPIO\_P23](#a8742762c7c46596977c17898e55f7df0)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(23, 3) |
| #define | [I2SWCLK\_P23](#a038809d35e405118dcd792db6cfd078c)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(23, 4) |
| #define | [CMPOUT\_P23](#a2f0b3b3267958512978997e66001a86b)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(23, 5) |
| #define | [MSPI0\_3\_P23](#a1adc0116ed82c440f4fe64116a021917)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(23, 6) |
| #define | [UART1TX\_P24](#a640da7cf413db9c5ad8f8c49b7208539)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(24, 0) |
| #define | [NCE24\_P24](#aef5c8fe782ba1f615e0ea35d44a942ce)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(24, 1) |
| #define | [MSPI0\_8\_P24](#ab9a27639f83bfc5f2851ad34abad3efe)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(24, 2) |
| #define | [GPIO\_P24](#a38b0fad90fac621ae3056e0890e5db18)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(24, 3) |
| #define | [UA0CTS\_P24](#a2f9bcf5acd23826869291e4ae956ee91)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(24, 4) |
| #define | [CTIM21\_P24](#a5e3b689232d21c05e42043c61f6e7445)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(24, 5) |
| #define | [XT32KHz\_P24](#aca95921548c6549fa9b40d0584389037)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(24, 6) |
| #define | [SWO\_P24](#acc4f37955d3cc5567dddb283275cd791)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(24, 7) |
| #define | [UART1RX\_P25](#a986d17fc832de865df075504f12f2749)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(25, 0) |
| #define | [NCE25\_P25](#a6c08788db3454db63bc8e5bca88b61a1)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(25, 1) |
| #define | [CTIM1\_P25](#ad871e333e8d90dccce7c7c874da74da2)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(25, 2) |
| #define | [GPIO\_P25](#a70eeb3da2737dc1f88ef0d6b033ba31b)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(25, 3) |
| #define | [M2SDAWIR3\_P25](#aae0817f4cc4c65301171000cb7c0eb88)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(25, 4) |
| #define | [M2MISO\_P25](#a0c695ae4458de77501c1ba4c1a13191b)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(25, 5) |
| #define | [NCE26\_P26](#a498a5dcaa37b5a972e8eea27c29617ef)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(26, 1) |
| #define | [CTIM3\_P26](#a631c65202c1c83b33c67e105516550f1)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(26, 2) |
| #define | [GPIO\_P26](#a70cc23730a6021ba52d4b46466bf7ec8)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(26, 3) |
| #define | [SCCRST\_P26](#a645b6c6e3f318aa5ac4fa619a835cd59)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(26, 4) |
| #define | [MSPI0\_1\_P26](#a9c61cc82c741aa4023a607fbe8fa89c7)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(26, 5) |
| #define | [UART0TX\_P26](#a0a5809f404cde8111cfdfa67b5975607)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(26, 6) |
| #define | [UA1CTS\_P26](#ab57497d2c1a2802d788f940456afc86d)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(26, 7) |
| #define | [UART0RX\_P27](#ac18a31df22a6076cd39c0f34e82794a0)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(27, 0) |
| #define | [NCE27\_P27](#a4b0b9c08da925a4a55bf9cd8342e275d)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(27, 1) |
| #define | [CTIM5\_P27](#a254e70755e2142d57322a9e19e972f01)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(27, 2) |
| #define | [GPIO\_P27](#a9e3eb9ba4f0604f735fc0da2298dc150)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(27, 3) |
| #define | [M2SCL\_P27](#ad82dc28ee23bdcc6bcdd3761bb359ab7)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(27, 4) |
| #define | [M2SCK\_P27](#a371cb048e98d35cab6196193d0c00d4e)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(27, 5) |
| #define | [I2SWCLK\_P28](#a97a46946f5659dfae1a97dfe56832719)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(28, 0) |
| #define | [NCE28\_P28](#ac975e39671e4884de16995b831c3bc52)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(28, 1) |
| #define | [CTIM7\_P28](#af89b558743b480da082df15fd2bcecd3)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(28, 2) |
| #define | [GPIO\_P28](#a6f6f8847e0069b5fefc4a6a54851c99b)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(28, 3) |
| #define | [M2MOSI\_P28](#aad8910b77ff0ffc62ce7b15f49da3bac)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(28, 5) |
| #define | [UART0TX\_P28](#a351989945b5403624c7d4fa53a44ab86)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(28, 6) |
| #define | [ADCSE1\_P29](#aa3f68e46605f8425448a99ba37eadcb9)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(29, 0) |
| #define | [NCE29\_P29](#ac7c4f18c7b072968ce9048bb9057356c)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(29, 1) |
| #define | [CTIM9\_P29](#a21f4d326b3928de4948b4d2dc41c3368)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(29, 2) |
| #define | [GPIO\_P29](#a0c8d4306be59368e181736d98c9d6b4b)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(29, 3) |
| #define | [UA0CTS\_P29](#ae0f8b8eac04505e31e3a54101a6d7cfa)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(29, 4) |
| #define | [UA1CTS\_P29](#a9072e7364c227042f9232c48b6b6b9c2)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(29, 5) |
| #define | [UART0RX\_P29](#a97be8cedd244e53e809d38cdeb4933c3)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(29, 6) |
| #define | [PDMDATA\_P29](#a7447bed11900ad2fc0c1fdec80c633f5)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(29, 7) |
| #define | [NCE30\_P30](#a6d9a17fecc9e2687ede485e719c5e616)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(30, 1) |
| #define | [CTIM11\_P30](#af85f87414b52aa3573a268d527d25d92)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(30, 2) |
| #define | [GPIO\_P30](#a96753b0a1e5a99e644c3bf21aee043b9)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(30, 3) |
| #define | [UART0TX\_P30](#aa507368219464308827240872d0eab11)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(30, 4) |
| #define | [UA1RTS\_P30](#a0d65684ea5cbc9fd0e75f1f849117a27)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(30, 5) |
| #define | [BLEIF\_SCK\_P30](#ac4b587d22482a3b110431d4a6644c696)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(30, 6) |
| #define | [I2SDAT\_P30](#a4eabbfc370ca2db0afd7ceb14769ba21)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(30, 7) |
| #define | [ADCSE3\_P31](#a6e98f43cdc78b15346036a660fa28e5c)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(31, 0) |
| #define | [NCE31\_P31](#aa1001078fb5a05925a8b02e6ecca70c5)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(31, 1) |
| #define | [CTIM13\_P31](#acb9e32510b851f3aebd23decaf2264a7)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(31, 2) |
| #define | [GPIO\_P31](#a2d700f518a2e57f3741c50e0403c471a)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(31, 3) |
| #define | [UART0RX\_P31](#a7e23355beb26a376895e08aac26dea57)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(31, 4) |
| #define | [SCCCLK\_P31](#a6cd0038a5d5bfa4008eae6666323e3a2)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(31, 5) |
| #define | [BLEIF\_MISO\_P31](#a3514181206232492ae6962e386509638)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(31, 6) |
| #define | [UA1RTS\_P31](#ad7a6b728d49d7ae25431e80cf56aab1b)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(31, 7) |
| #define | [ADCSE4\_P32](#a3a527375ccd62e5f8a761f1942adbcc8)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(32, 0) |
| #define | [NCE32\_P32](#afb0f804646a6e3557dd4341eb7d72a74)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(32, 1) |
| #define | [CTIM15\_P32](#acb4d0ec1f842052abd81149b33e8b087)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(32, 2) |
| #define | [GPIO\_P32](#a2a97e46858bf930945c2e03effcc035e)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(32, 3) |
| #define | [SCCIO\_P32](#a0562630e3ed7a89a28ea8e9d877a25b5)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(32, 4) |
| #define | [BLEIF\_MOSI\_P32](#a944132c6051ac94d56bc0124c24fff9d)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(32, 6) |
| #define | [UA1CTS\_P32](#a6d5db72517c101eea3a3aca07b716869)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(32, 7) |
| #define | [ADCSE5\_P33](#ac774e90f430510b182a016ba09661ed0)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(33, 0) |
| #define | [NCE33\_P33](#aa91f920fb637bf393393bac80a9e49ba)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(33, 1) |
| #define | [XT32KHz\_P33](#a40417407993ffd2e917262ae286e0b8d)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(33, 2) |
| #define | [GPIO\_P33](#aa9c2e434db6bed47b117a0764e28889e)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(33, 3) |
| #define | [BLEIF\_CSN\_P33](#a00ad9846bf598e2cec9752afa48417da)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(33, 4) |
| #define | [UA0CTS\_P33](#a5f64c8ebf5a704ad48dbf12ce595f504)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(33, 5) |
| #define | [CTIM23\_P33](#a4f4778e38e9719f89985ac4cdf98f344)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(33, 6) |
| #define | [SWO\_P33](#ae998e2b505d3b112532b1b58fd298d01)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(33, 7) |
| #define | [ADCSE6\_P34](#a5ee25464af430f33bcb61e9ae711d9a3)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(34, 0) |
| #define | [NCE34\_P34](#a4f042898a506cccce60699375b16bf85)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(34, 1) |
| #define | [UA1RTS\_P34](#a6a490d5a195593605844d2883373ab33)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(34, 2) |
| #define | [GPIO\_P34](#a0b5e8a841aa9e129351ec258cd5849f2)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(34, 3) |
| #define | [CMPRF2\_P34](#a1a9ea33ae1493df327e34a7480e04141)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(34, 4) |
| #define | [UA0RTS\_P34](#af821710452cee65f18e7d9d21f16be5e)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(34, 5) |
| #define | [UART0RX\_P34](#ae54604f59f12de3bd10dc115e256b69a)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(34, 6) |
| #define | [PDMDATA\_P34](#a3288f0cd1140d15ca20840fffe78daaa)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(34, 7) |
| #define | [ADCSE7\_P35](#ae609e68dba89b9c84fc3e6a4a3e29e67)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(35, 0) |
| #define | [NCE35\_P35](#ad2cdd6497fb562ea4738beb637e044d1)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(35, 1) |
| #define | [UART1TX\_P35](#abfd3f2f30a9a90790dbc58666f8e4ea3)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(35, 2) |
| #define | [GPIO\_P35](#a26e70a3f976c854799b2451f085ca761)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(35, 3) |
| #define | [I2SDAT\_P35](#a5f25fda5e336dcdd5d97a0cf9778ee53)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(35, 4) |
| #define | [CTIM27\_P35](#a3f69161303bc2a76473db22a109aa651)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(35, 5) |
| #define | [UA0RTS\_P35](#a5b92e6ee90a413909f63c838283f7777)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(35, 6) |
| #define | [BLEIF\_STATUS\_P35](#a8fa21604c6dd1dcdc7ad5d74dfb2afaf)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(35, 7) |
| #define | [TRIG1\_P36](#a3595cef3917f8dbb33c495fa3dd129d9)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(36, 0) |
| #define | [NCE36\_P36](#aae112b0ebd7c6f448b1ce24b772910a4)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(36, 1) |
| #define | [UART1RX\_P36](#abe283e2a79b535f5afb8c82ebba32fce)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(36, 2) |
| #define | [GPIO\_P36](#a3050173d1ff33494b4b047fd11aff68d)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(36, 3) |
| #define | [XT32KHz\_P36](#a48be8de8a03a7a27a7848c64adb97665)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(36, 4) |
| #define | [UA1CTS\_P36](#a1b3e74a2c7e43f142fdc02b096236733)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(36, 5) |
| #define | [UA0CTS\_P36](#a6a6bf8ffd195353bbccb43904442db80)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(36, 6) |
| #define | [PDMDATA\_P36](#aaf12889bb6f7de1a92c0d10147c921bf)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(36, 7) |
| #define | [TRIG2\_P37](#a1bf06e0a3c6234f2c594939d658de1de)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(37, 0) |
| #define | [NCE37\_P37](#a736adccb71d5a32e0519cbd8c89d6b77)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(37, 1) |
| #define | [UA0RTS\_P37](#a3b0abd07adcc2cd6b6764f715cd21cd5)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(37, 2) |
| #define | [GPIO\_P37](#a5895dbfee43e62831294b162bde44b9e)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(37, 3) |
| #define | [SCCIO\_P37](#ab0f35ce206392abf106f6b0e702664c1)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(37, 4) |
| #define | [UART1TX\_P37](#af51f177fc9f7208bcf5815a478d29978)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(37, 5) |
| #define | [PDMCLK\_P37](#a2dc471687b4110dc079f5d896f7fe2e2)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(37, 6) |
| #define | [CTIM29\_P37](#a3dd5aac8ad93fe07b4ab74c35269dba6)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(37, 7) |
| #define | [TRIG3\_P38](#a2d5a132e305dbb9cc38b4f062ab2a5a1)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(38, 0) |
| #define | [NCE38\_P38](#a7eb51c6fb1bdaabcd854928f0fc53365)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(38, 1) |
| #define | [UA0CTS\_P38](#aa49ea18a61d8190908b5556c6298e6fa)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(38, 2) |
| #define | [GPIO\_P38](#a8786cdf36cc244ccb754406e7091dc31)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(38, 3) |
| #define | [M3MOSI\_P38](#a1d5ee7db62801b7f7ba60c4e81daffcf)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(38, 5) |
| #define | [UART1RX\_P38](#a41cec431ed8db8d5286149552695caaf)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(38, 6) |
| #define | [UART0TX\_P39](#a3ed9a495f050ab7486aadc5867539a59)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(39, 0) |
| #define | [UART1TX\_P39](#ae99c8956963caaa4d16d5b3f1c1bb9ce)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(39, 1) |
| #define | [CTIM25\_P39](#a6c33f4bc8b739c173b92d185884aaa4b)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(39, 2) |
| #define | [GPIO\_P39](#a5a4c89d2f63802373c28dc64010cd6c8)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(39, 3) |
| #define | [M4SCL\_P39](#a8a962334908f406e82ac843741b0c837)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(39, 4) |
| #define | [M4SCK\_P39](#a76c405ee75ccbd3e6ba7016c25ad09ad)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(39, 5) |
| #define | [UART0RX\_P40](#a175181dfaf1f6fff4ef61181d450b0f3)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(40, 0) |
| #define | [UART1RX\_P40](#ab6fb2d741ae9ca9492959e8b04d2ab8c)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(40, 1) |
| #define | [TRIG0\_P40](#a4d41b8f7fd97fcae660bf35bf562f4b8)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(40, 2) |
| #define | [GPIO\_P40](#a388d84a144f3522f0fa9a6d5f860219c)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(40, 3) |
| #define | [M4SDAWIR3\_P40](#a9632c0a042f4bb66a728d0b830c40367)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(40, 4) |
| #define | [M4MISO\_P40](#a3355068431b201477fc0dd1a4f87df68)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(40, 5) |
| #define | [NCE41\_P41](#aaaf74f87cd67b25b654c92e58311d818)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(41, 0) |
| #define | [BLEIF\_IRQ\_P41](#a008c508f2483e318e52d3d6bf20f0a1a)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(41, 1) |
| #define | [SWO\_P41](#a7d5cbbcd03000b54af3d06566fd3b659)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(41, 2) |
| #define | [GPIO\_P41](#a8c96f8b549c1d2739c024137286035e1)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(41, 3) |
| #define | [I2SWCLK\_P41](#a1b3a9948d8a90649b505fcb684fe523d)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(41, 4) |
| #define | [UA1RTS\_P41](#a09961d9c0667f515d82a7c53e972a48d)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(41, 5) |
| #define | [UART0TX\_P41](#a2b7dc7334200258b20a08422ea361f70)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(41, 6) |
| #define | [UA0RTS\_P41](#aff53cdfb5a9f567fea668005ef248f8a)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(41, 7) |
| #define | [UART1TX\_P42](#a6705e001463f646a7f26ff4cb316c634)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(42, 0) |
| #define | [NCE42\_P42](#ae5399f9d5357e096d59283bfea4fd6ee)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(42, 1) |
| #define | [CTIM16\_P42](#a1474daf0d4841a34626d23ce9cd7b545)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(42, 2) |
| #define | [GPIO\_P42](#ad2ddbd7fd0001abfcf1416caa9f56496)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(42, 3) |
| #define | [M3SCL\_P42](#a7be4191ad1020cf880616188964f0a89)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(42, 4) |
| #define | [M3SCK\_P42](#a0a924f11185e5c0c0cc58161efdefcf9)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(42, 5) |
| #define | [UART1RX\_P43](#acd68b66375a1cd525670f9f0b3ea9213)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(43, 0) |
| #define | [NCE43\_P43](#a93e018507d62174c89e7fa137dde36cd)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(43, 1) |
| #define | [CTIM18\_P43](#ab1b1fb6876a080a75501fce8190c7820)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(43, 2) |
| #define | [GPIO\_P43](#aab2f5553d3ce7da8f585c493f82da02f)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(43, 3) |
| #define | [M3SDAWIR3\_P43](#a2ea30abd4885c0ca0933d9898b5926d1)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(43, 4) |
| #define | [M3MISO\_P43](#abd8970c9e4ec21d8cb6199f26817a491)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(43, 5) |
| #define | [UA1RTS\_P44](#a46baf1010c95eee1dc0011c1864c4796)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(44, 0) |
| #define | [NCE44\_P44](#a3ed79603ebbdb77c08f3d793c0f361d7)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(44, 1) |
| #define | [CTIM20\_P44](#a181b829366db1077513b25ba65ea1841)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(44, 2) |
| #define | [GPIO\_P44](#accbd9b4f6fa257af91af9a533ba856ea)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(44, 3) |
| #define | [M4MOSI\_P44](#a11ea4c9cd1f25fc2aba92f5d4ef7b206)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(44, 5) |
| #define | [UART0TX\_P44](#a51592b8b7e152dbb622ef0a330862341)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(44, 6) |
| #define | [UA1CTS\_P45](#a944d829a81b45cf99560241e9b19154d)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(45, 0) |
| #define | [NCE45\_P45](#a8b9c9c5513d7098d3772bf031eefdc34)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(45, 1) |
| #define | [CTIM22\_P45](#aa1d5c972c6278777fabc856a5f6ff9d3)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(45, 2) |
| #define | [GPIO\_P45](#afda67e6b2d71c41df2c9384829780eaf)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(45, 3) |
| #define | [I2SDAT\_P45](#af628f20a4932e8140b14eb3b4c07b913)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(45, 4) |
| #define | [PDMDATA\_P45](#ac3d93a44f8fa496120aff6de06813fcc)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(45, 5) |
| #define | [UART0RX\_P45](#af7673ee93e7a84ad6e16846d98de6464)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(45, 6) |
| #define | [SWO\_P45](#ab1907bebf4d3e6951994035f697ed321)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(45, 7) |
| #define | [I2SBCLK\_P46](#a09604ed08062afbbd82ef684a27b196d)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(46, 0) |
| #define | [NCE46\_P46](#a5b0e939354b2c232bdc48a3dcb9a1607)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(46, 1) |
| #define | [CTIM24\_P46](#a72d372c5f5358c9af85d6802dc317f6e)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(46, 2) |
| #define | [GPIO\_P46](#af5d342a38a441738d343eeef58c1cdb3)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(46, 3) |
| #define | [SCCRST\_P46](#add5fa4e696047cb893bb829416ee2afd)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(46, 4) |
| #define | [PDMCLK\_P46](#a60677b54a72e30bfd0c04de7ff9217a7)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(46, 5) |
| #define | [UART1TX\_P46](#afe121783dfe5a9958c15ae0883b83cfb)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(46, 6) |
| #define | [SWO\_P46](#a17e7362e03a87627fff5643989fcca00)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(46, 7) |
| #define | [XT32KHz\_P47](#a55e6549b3ba1beca7ae1db93b7f809ee)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(47, 0) |
| #define | [NCE47\_P47](#a1f411d730489dee140ae375049d449fd)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(47, 1) |
| #define | [CTIM26\_P47](#a0bb0b6007b81b87f0e5a633d962957e5)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(47, 2) |
| #define | [GPIO\_P47](#a1eb20e4fdae76831bf870bff406c346e)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(47, 3) |
| #define | [M5MOSI\_P47](#aece153beaf82657c8de3ecd17ea62757)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(47, 5) |
| #define | [UART1RX\_P47](#a45c38170a7a3b57c6576ebfa6f52b35c)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(47, 6) |
| #define | [UART0TX\_P48](#aaaafe03305c7bafe3020c6c50e56d3dd)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(48, 0) |
| #define | [NCE48\_P48](#ad2333f40db7fb9ecfbd1392e9554ffa3)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(48, 1) |
| #define | [CTIM28\_P48](#a070d0cbdfdd6525c2d1e61197af52c61)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(48, 2) |
| #define | [GPIO\_P48](#af730366def18c0d1bf2e4c00fe3c1ab8)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(48, 3) |
| #define | [M5SCL\_P48](#a11a7466d3e7ced79092085f5704fa4d8)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(48, 4) |
| #define | [M5SCK\_P48](#a448e33923f0e23281b0d4ef733199b5c)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(48, 5) |
| #define | [UART0RX\_P49](#a70696ef3a46aa08391bdf4d3ebc9aa3f)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(49, 0) |
| #define | [NCE49\_P49](#a339781c28180de2027fc9295189463e1)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(49, 1) |
| #define | [CTIM30\_P49](#adce81e86454552afd05cf0144a16a9f4)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(49, 2) |
| #define | [GPIO\_P49](#a4b290382e034342af84424e34cb6d297)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(49, 3) |
| #define | [M5SDAWIR3\_P49](#ad1fede78430cc3626bddb9fab7b257cf)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(49, 4) |
| #define | [M5MISO\_P49](#a9393e54fe2a906feb32275d905db7465)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(49, 5) |
| #define | [SWO\_P50](#a056b770b0d92b72bd3c33a957683c790)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(50, 0) |
| #define | [NCE50\_P50](#ab7492256a637deef5ea4943b4b701110)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(50, 1) |
| #define | [CT0\_P50](#aa825c015fb5592a56455e0fbd277ed6e)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(50, 2) |
| #define | [GPIO\_P50](#a44de537cf2f84b012dc099c000d47eee)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(50, 3) |
| #define | [UART0TX\_P50](#ab967379871f5d5e937c536b0af767154)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(50, 4) |
| #define | [UART0RX\_P50](#a6277bab84473fecc433b54e6a29b3c40)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(50, 5) |
| #define | [UART1TX\_P50](#a79377784abe4f92663d3fb9bf878921a)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(50, 6) |
| #define | [UART1RX\_P50](#ae64fb321a2fb963c1f0e1771b6f5f8f0)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(50, 7) |
| #define | [MSPI1\_0\_P51](#a9569a86b721653e4303b538d858362ff)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(51, 0) |
| #define | [NCE51\_P51](#aeca26feeace6bc79995c2e619b1a9c18)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(51, 1) |
| #define | [CTIM1\_P51](#a4eefe29a2117733367a1883f4c7a233c)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(51, 2) |
| #define | [GPIO\_P51](#a78a6a9fa2e9eb9ba6ff803a5810de263)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(51, 3) |
| #define | [MSPI1\_1\_P52](#ac6b4ad9a963294d75262c1e94b8abf8f)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(52, 0) |
| #define | [NCE52\_P52](#ae86416562248f70f8fddcbfda85a3ae3)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(52, 1) |
| #define | [CTIM2\_P52](#a826d6ddcd51c2468767bc70583608c29)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(52, 2) |
| #define | [GPIO\_P52](#aa8fc5cd8e841cc12ee97736b5d5b2637)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(52, 3) |
| #define | [MSPI1\_2\_P53](#ac4d5baf17923790039150886151f7dec)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(53, 0) |
| #define | [NCE53\_P53](#aae0ee7affb647cfd3d54d168868ef485)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(53, 1) |
| #define | [CTIM3\_P53](#a183d8e6c6bd4579d0feae2c3c67e2e61)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(53, 2) |
| #define | [GPIO\_P53](#aa41e6f073ae876d1486552a07ace93a3)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(53, 3) |
| #define | [MSPI1\_3\_P54](#a8234fa9ff3afbc23fa0f895f0076835c)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(54, 0) |
| #define | [NCE54\_P54](#a6318a96c1367922e5ecd0f682d432630)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(54, 1) |
| #define | [CTIM4\_P54](#ae8b5cb40219aec3a11f0251a39a06a9d)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(54, 2) |
| #define | [GPIO\_P54](#a8b614afb4941fbe9036fa20421a55820)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(54, 3) |
| #define | [MSPI1\_4\_P55](#abcb127632e19c63b97bd01f6a2de8e9a)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(55, 0) |
| #define | [NCE55\_P55](#ad5438399e3ff56c263631991b09dd460)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(55, 1) |
| #define | [CTIM5\_P55](#a516c0fb62d563ceca86131539f09f131)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(55, 2) |
| #define | [GPIO\_P55](#a2fcffaace9255d9e639de6c2596603c8)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(55, 3) |
| #define | [MSPI1\_5\_P56](#a95e11921d5164ad709ab5cdad5f1a58c)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(56, 0) |
| #define | [NCE56\_P56](#ad8e09cff85610b1bfb03403771360685)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(56, 1) |
| #define | [CTIM6\_P56](#ae00988c0a4632e534f2252622bd48759)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(56, 2) |
| #define | [GPIO\_P56](#ad9c517c0112a8c8634b9ad46ee32dd45)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(56, 3) |
| #define | [MSPI1\_6\_P57](#a8831303ca7109996c6446350e384392d)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(57, 0) |
| #define | [NCE57\_P57](#a98fb369e6acd52cc5aae8e6730ed9758)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(57, 1) |
| #define | [CTIM7\_P57](#ac2e6c19821053ab44d79a352d48ca1f8)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(57, 2) |
| #define | [GPIO\_P57](#a83be188c573c4f64966aae37f47caf5b)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(57, 3) |
| #define | [MSPI1\_7\_P58](#ab61ac243ccd5f0a1d1fdec4b8d45b6dc)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(58, 0) |
| #define | [NCE58\_P58](#aac11c1a52fc64f3c2684b4323e28bdb4)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(58, 1) |
| #define | [CTIM8\_P58](#a505da5511b9f77bc9623595b80b9e7d6)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(58, 2) |
| #define | [GPIO\_P58](#a876dd6e6770f3c605b06c61e9a6640ac)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(58, 3) |
| #define | [MSPI1\_8\_P59](#ae74279d568a99727bd00816f856f2bec)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(59, 0) |
| #define | [NCE59\_P59](#ab437cea609c7b3dbdec00e17f674ee6c)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(59, 1) |
| #define | [CTIM9\_P59](#adc616fdbce3f49c78d01d5ffb9245ada)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(59, 2) |
| #define | [GPIO\_P59](#ab5b877868310ab0269c468edcac715f7)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(59, 3) |
| #define | [MSPI1\_9\_P60](#acbdd8675b5c6094213377db4d57b5c76)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(60, 0) |
| #define | [NCE60\_P60](#af5a0f373987f9e093d0be1e96fc422e0)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(60, 1) |
| #define | [CTIM10\_P60](#a15c4eccf0f0de2c64285b4ad06258a3a)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(60, 2) |
| #define | [GPIO\_P60](#ac3a637135617760fba12cf98aeb107c2)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(60, 3) |
| #define | [SWO\_P61](#af6865d7d7b0939fee8634025753ad0ac)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(61, 0) |
| #define | [NCE61\_P61](#ab5911745a6c23c3a7ded39e214324a1b)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(61, 1) |
| #define | [CTIM11\_P61](#a53cb8cd389fd7d9323122949b9642088)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(61, 2) |
| #define | [GPIO\_P61](#a5cc6477cb81b8e732013eee58ce0183d)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(61, 3) |
| #define | [UART0TX\_P61](#a13169414a9db1d2d918fd8a1ac6e328e)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(61, 4) |
| #define | [UART0RX\_P61](#a5ef06f1ca2d2d28e87846add941a6a01)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(61, 5) |
| #define | [UART1TX\_P61](#a4b046371e9d9717fbc966b890d231dc4)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(61, 6) |
| #define | [UART1RX\_P61](#a8ba999d652f37a9cec7f09ec48bb1efd)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(61, 7) |
| #define | [SWO\_P62](#ac3477b8ba498f9d6ce303c891fc92102)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(62, 0) |
| #define | [NCE62\_P62](#acff3d4c76b5032bc61e0757224cf5c30)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(62, 1) |
| #define | [CTIM12\_P62](#a2ac80f7683a1da305ab0fa6a76a4e366)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(62, 2) |
| #define | [GPIO\_P62](#ad8ad98d7206b4d60e9a785270cb6bebd)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(62, 3) |
| #define | [UA0CTS\_P62](#a17a8866677f47e6edc86a3873c09d606)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(62, 4) |
| #define | [UA0RTS\_P62](#a3330f5f0766f022c8d4f215395ef1f8f)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(62, 5) |
| #define | [UA1CTS\_P62](#a5619b10dd987655fd0f8b470832dd617)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(62, 6) |
| #define | [UA1RTS\_P62](#ac844f507a7ad999a2ce9a749667d43ec)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(62, 7) |
| #define | [SWO\_P63](#ad1a604f4d60d6ffc7182e7655073bd11)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(63, 0) |
| #define | [NCE63\_P63](#acd4dd1d3133002f0c60426e542702dd3)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(63, 1) |
| #define | [CTIM13\_P63](#a896899eb01c3da31320937430cf965e9)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(63, 2) |
| #define | [GPIO\_P63](#a9e7881322451f9c064a827bd26c16aa0)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(63, 3) |
| #define | [UA0CTS\_P63](#aad6095bc6dc59c8cfb0a1c19d937d573)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(63, 4) |
| #define | [UA0RTS\_P63](#ab0422d143c7ddf4dd7fce671af815bb9)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(63, 5) |
| #define | [UA1CTS\_P63](#a0d8dd2d9de57fd25bb59d31be03014ec)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(63, 6) |
| #define | [UA1RTS\_P63](#a362e069b94a6ea0b5bb1f5b64aef473f)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(63, 7) |
| #define | [MSPI2\_0\_P64](#a47ffd6951b155ac3b80a5f4ac5057e8b)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(64, 0) |
| #define | [NCE64\_P64](#af279b091bf1b2e9854cb240fb07d7411)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(64, 1) |
| #define | [CTIM14\_P64](#a539c301c87081cafff14c9a0902e90de)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(64, 2) |
| #define | [GPIO\_P64](#ac031a8b0e6fe953a329bccae5138864c)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(64, 3) |
| #define | [MSPI2\_1\_P65](#a267fef799fd16097688aa7a777fb5194)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(65, 0) |
| #define | [NCE65\_P65](#a4913e8e909a5f53078ec4f73eda5c112)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(65, 1) |
| #define | [CTIM15\_P65](#a9a0bb2452ab886f75da833f8c546bef0)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(65, 2) |
| #define | [GPIO\_P65](#ae9af3264c78732b1bc79b552d68dfa6a)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(65, 3) |
| #define | [MSPI2\_2\_P66](#a4dcf9f729fb234071170c7116620bdbc)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(66, 0) |
| #define | [NCE66\_P66](#acff679577d81e687a56906eebf769bf6)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(66, 1) |
| #define | [CTIM16\_P66](#a365f841a97880964c986c808afe50cbf)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(66, 2) |
| #define | [GPIO\_P66](#ac82bb9747100752447c61e008d0aed46)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(66, 3) |
| #define | [MSPI2\_3\_P67](#a13cbb5730534690db2ce73c739bce161)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(67, 0) |
| #define | [NCE67\_P67](#a94cc174e483db8110ca76fff12629c6d)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(67, 1) |
| #define | [CTIM17\_P67](#a192693e602f7328d20fcaeb7a80e2b16)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(67, 2) |
| #define | [GPIO\_P67](#aa9a6029306499ec2cccbb76899488bf3)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(67, 3) |
| #define | [MSPI2\_4\_P68](#adcca1198343f7a85b2f87b1917cfc6c0)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(68, 0) |
| #define | [NCE68\_P68](#a43db97f86803b04b80140c3c12f096d5)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(68, 1) |
| #define | [CTIM18\_P68](#a1db22d617bacc5856a42e817d3aab57a)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(68, 2) |
| #define | [GPIO\_P68](#a3e315d2425fb95945b68e7c4e2fe954a)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(68, 3) |
| #define | [SWO\_P69](#a5fa4920fa2af91403279165ec14471c3)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(69, 0) |
| #define | [NCE69\_P69](#a8e86b1f165b06bde1344f2a0591591f6)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(69, 1) |
| #define | [CTIM19\_P69](#a25a3df1f226d95466f44b45fccfa9239)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(69, 2) |
| #define | [GPIO\_P69](#a5602b2af723fb7fe3bf1121b0577c2e7)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(69, 3) |
| #define | [UART0TX\_P69](#a1ae2ba2a91ba842284fd6cbb156def04)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(69, 4) |
| #define | [UART0RX\_P69](#ac0aec58a68e82e74ff74d31889ba6eda)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(69, 5) |
| #define | [UART1TX\_P69](#a147d9681b5a8ca2b3cb1a9ed805762fd)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(69, 6) |
| #define | [UART1RX\_P69](#a6d3cf67ebe5a1f059fd47110357a7e4e)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(69, 7) |
| #define | [SWO\_P70](#ae840ad7da2d8d0741a885d60b108c6f6)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(70, 0) |
| #define | [NCE70\_P70](#a154b9a05cda9e8a41f84f82417a60d81)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(70, 1) |
| #define | [CTIM20\_P70](#aadd1d390b428c5f7b8196efc46743ea4)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(70, 2) |
| #define | [GPIO\_P70](#af1f938f04fe3670874c371bfff680c41)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(70, 3) |
| #define | [UART0TX\_P70](#a62f156b398182c31da9377c3f417623f)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(70, 4) |
| #define | [UART0RX\_P70](#a086d2fe9f77498d1fee5ad62570a41a1)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(70, 5) |
| #define | [UART1TX\_P70](#a12a07be7ada04c8db5456f26e384c4d5)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(70, 6) |
| #define | [UART1RX\_P70](#aad95c312dadb461f7926ab6f01374ed7)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(70, 7) |
| #define | [SWO\_P71](#a5b05a881450d820175599526bca285e7)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(71, 0) |
| #define | [NCE71\_P71](#a04df6aa292fc65e77cc4de70b36d3d95)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(71, 1) |
| #define | [CTIM21\_P71](#a772105d2fea38c937834c65896d8c3cd)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(71, 2) |
| #define | [GPIO\_P71](#a88cfa6b114b0efb7bfeec35a4110727d)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(71, 3) |
| #define | [UART0TX\_P71](#afee0c790c7e8f4dd235d8489ac5c4107)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(71, 4) |
| #define | [UART0RX\_P71](#ae8e2a290af35da4c5d4d882eaa3aa8cd)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(71, 5) |
| #define | [UART1TX\_P71](#a75527d755c741c22f55d12e35f5aef13)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(71, 6) |
| #define | [UART1RX\_P71](#a6a2d312670202739632148c973559135)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(71, 7) |
| #define | [SWO\_P72](#aeeb7f033753b1196ff4acb716be4e782)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(72, 0) |
| #define | [NCE72\_P72](#a89192a0beda2cecdd53e4fd7174302e5)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(72, 1) |
| #define | [CTIM22\_P72](#ac8555a20407cf149854f388bee54f4e0)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(72, 2) |
| #define | [GPIO\_P72](#adcf84a78ff2d8532d87482678ba2df80)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(72, 3) |
| #define | [UART0TX\_P72](#ae68adb841018f98375b7022e370aba0c)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(72, 4) |
| #define | [UART0RX\_P72](#a6720bbe266f8a2d54929325ee19c3b23)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(72, 5) |
| #define | [UART1TX\_P72](#a315caa38da59dbbea5e94f08194ba614)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(72, 6) |
| #define | [UART1RX\_P72](#ae0e923c68bbdf2d2a929c34f580f4fd4)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(72, 7) |
| #define | [SWO\_P73](#a9a2b1491dd870b395c181ecd48d136c0)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(73, 0) |
| #define | [NCE73\_P73](#a86228f8d9adc8065f76ca1f0af512d50)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(73, 1) |
| #define | [CTIM23\_P73](#a74b8d5f54ada101a6a29e2c2b17c3a90)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(73, 2) |
| #define | [GPIO\_P73](#a284f44425e1437643fad644c5f538b09)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(73, 3) |
| #define | [UA0CTS\_P73](#af8cca7cdb1b7794250c131fce4e0dc54)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(73, 4) |
| #define | [UA0RTS\_P73](#afc2a1cd4bc96170933509a26828ca200)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(73, 5) |
| #define | [UA1CTS\_P73](#a76e95ea07d5a29cb8bf391ceeda6b177)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(73, 6) |
| #define | [UA1RTS\_P73](#abcc0c2177d3ebab6aef372b39aeff6cb)   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(73, 7) |

## Macro Definition Documentation

## [◆ ](#a994b602fed3f5de352a97b9cc9c62607)ADCD0NSE9\_P12

| #define ADCD0NSE9\_P12   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(12, 0) |
| --- |

## [◆ ](#a5c9489a135b6531852d4ebdfc5154f22)ADCD0PSE8\_P13

| #define ADCD0PSE8\_P13   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(13, 0) |
| --- |

## [◆ ](#ad4979ef8e737edc9304425cbff550802)ADCD1N\_P15

| #define ADCD1N\_P15   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(15, 0) |
| --- |

## [◆ ](#a116b6aa61f2ad957c6e205c73b447a1e)ADCD1P\_P14

| #define ADCD1P\_P14   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(14, 0) |
| --- |

## [◆ ](#add33549cde84fd881439b438becb5e33)ADCSE0\_P16

| #define ADCSE0\_P16   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(16, 0) |
| --- |

## [◆ ](#aa3f68e46605f8425448a99ba37eadcb9)ADCSE1\_P29

| #define ADCSE1\_P29   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(29, 0) |
| --- |

## [◆ ](#a0af7147f664fc0c56acdfc63e76558bc)ADCSE2\_P11

| #define ADCSE2\_P11   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(11, 0) |
| --- |

## [◆ ](#a6e98f43cdc78b15346036a660fa28e5c)ADCSE3\_P31

| #define ADCSE3\_P31   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(31, 0) |
| --- |

## [◆ ](#a3a527375ccd62e5f8a761f1942adbcc8)ADCSE4\_P32

| #define ADCSE4\_P32   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(32, 0) |
| --- |

## [◆ ](#ac774e90f430510b182a016ba09661ed0)ADCSE5\_P33

| #define ADCSE5\_P33   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(33, 0) |
| --- |

## [◆ ](#a5ee25464af430f33bcb61e9ae711d9a3)ADCSE6\_P34

| #define ADCSE6\_P34   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(34, 0) |
| --- |

## [◆ ](#ae609e68dba89b9c84fc3e6a4a3e29e67)ADCSE7\_P35

| #define ADCSE7\_P35   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(35, 0) |
| --- |

## [◆ ](#aa00706366b69ceb3628404acb54d08c3)APOLLO3\_ALT\_FUNC\_MASK

| #define APOLLO3\_ALT\_FUNC\_MASK   0xf |
| --- |

## [◆ ](#aec76f3cfd2a609e60eabf5628f5ee698)APOLLO3\_ALT\_FUNC\_POS

| #define APOLLO3\_ALT\_FUNC\_POS   0 |
| --- |

## [◆ ](#a71eb3e43677ab0f8c9abd0fc61aafaab)APOLLO3\_PIN\_NUM\_MASK

| #define APOLLO3\_PIN\_NUM\_MASK   0x7f |
| --- |

## [◆ ](#a31b09dab4803a326db645412cf2d7acd)APOLLO3\_PIN\_NUM\_POS

| #define APOLLO3\_PIN\_NUM\_POS   4 |
| --- |

## [◆ ](#a2e4e01a3d50c6ced0a21d65877b0cdb2)APOLLO3\_PINMUX

| #define APOLLO3\_PINMUX | ( |  | *pin\_num*, |
| --- | --- | --- | --- |
|  |  |  | *alt\_func* ) |

**Value:**

(pin\_num << [APOLLO3\_PIN\_NUM\_POS](#a31b09dab4803a326db645412cf2d7acd) | alt\_func << [APOLLO3\_ALT\_FUNC\_POS](#aec76f3cfd2a609e60eabf5628f5ee698))

[APOLLO3\_PIN\_NUM\_POS](#a31b09dab4803a326db645412cf2d7acd)

#define APOLLO3\_PIN\_NUM\_POS

**Definition** ambiq-apollo3-pinctrl.h:13

[APOLLO3\_ALT\_FUNC\_POS](#aec76f3cfd2a609e60eabf5628f5ee698)

#define APOLLO3\_ALT\_FUNC\_POS

**Definition** ambiq-apollo3-pinctrl.h:10

## [◆ ](#a00ad9846bf598e2cec9752afa48417da)BLEIF\_CSN\_P33

| #define BLEIF\_CSN\_P33   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(33, 4) |
| --- |

## [◆ ](#a008c508f2483e318e52d3d6bf20f0a1a)BLEIF\_IRQ\_P41

| #define BLEIF\_IRQ\_P41   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(41, 1) |
| --- |

## [◆ ](#a3514181206232492ae6962e386509638)BLEIF\_MISO\_P31

| #define BLEIF\_MISO\_P31   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(31, 6) |
| --- |

## [◆ ](#a944132c6051ac94d56bc0124c24fff9d)BLEIF\_MOSI\_P32

| #define BLEIF\_MOSI\_P32   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(32, 6) |
| --- |

## [◆ ](#ac4b587d22482a3b110431d4a6644c696)BLEIF\_SCK\_P30

| #define BLEIF\_SCK\_P30   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(30, 6) |
| --- |

## [◆ ](#a8fa21604c6dd1dcdc7ad5d74dfb2afaf)BLEIF\_STATUS\_P35

| #define BLEIF\_STATUS\_P35   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(35, 7) |
| --- |

## [◆ ](#a95fca27e19b245305579cbad18962f00)CLKOUT\_P0

| #define CLKOUT\_P0   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(0, 2) |
| --- |

## [◆ ](#a44e6475e1fcd9fbb522a48dea35e8599)CLKOUT\_P7

| #define CLKOUT\_P7   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(7, 2) |
| --- |

## [◆ ](#a9c9cee6bc621a36d67af82a83ce108b9)CMPIN0\_P16

| #define CMPIN0\_P16   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(16, 5) |
| --- |

## [◆ ](#a7cd80fe3c550eaeb4430512efcc2a296)CMPIN1\_P18

| #define CMPIN1\_P18   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(18, 0) |
| --- |

## [◆ ](#a2f0b3b3267958512978997e66001a86b)CMPOUT\_P23

| #define CMPOUT\_P23   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(23, 5) |
| --- |

## [◆ ](#a11c7be341b9acbe096a9966044dae194)CMPRF0\_P19

| #define CMPRF0\_P19   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(19, 0) |
| --- |

## [◆ ](#a1269137afa8563480745e3fdf730580b)CMPRF1\_P17

| #define CMPRF1\_P17   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(17, 0) |
| --- |

## [◆ ](#a1a9ea33ae1493df327e34a7480e04141)CMPRF2\_P34

| #define CMPRF2\_P34   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(34, 4) |
| --- |

## [◆ ](#a9b2a8b0d84975b39cc2fdfb3b3f5c2c0)CT0\_P12

| #define CT0\_P12   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(12, 2) |
| --- |

## [◆ ](#aa825c015fb5592a56455e0fbd277ed6e)CT0\_P50

| #define CT0\_P50   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(50, 2) |
| --- |

## [◆ ](#a8427da089d2101bd9fc10ce6f1933aa8)CT8\_P5

| #define CT8\_P5   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(5, 7) |
| --- |

## [◆ ](#a00a0fc70b33db841fd0551b7c262253e)CTIM10\_P6

| #define CTIM10\_P6   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(6, 5) |
| --- |

## [◆ ](#a15c4eccf0f0de2c64285b4ad06258a3a)CTIM10\_P60

| #define CTIM10\_P60   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(60, 2) |
| --- |

## [◆ ](#af85f87414b52aa3573a268d527d25d92)CTIM11\_P30

| #define CTIM11\_P30   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(30, 2) |
| --- |

## [◆ ](#a53cb8cd389fd7d9323122949b9642088)CTIM11\_P61

| #define CTIM11\_P61   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(61, 2) |
| --- |

## [◆ ](#ab83b616320654dd99bb1b137f2fc07be)CTIM12\_P22

| #define CTIM12\_P22   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(22, 2) |
| --- |

## [◆ ](#a2ac80f7683a1da305ab0fa6a76a4e366)CTIM12\_P62

| #define CTIM12\_P62   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(62, 2) |
| --- |

## [◆ ](#acb9e32510b851f3aebd23decaf2264a7)CTIM13\_P31

| #define CTIM13\_P31   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(31, 2) |
| --- |

## [◆ ](#a896899eb01c3da31320937430cf965e9)CTIM13\_P63

| #define CTIM13\_P63   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(63, 2) |
| --- |

## [◆ ](#a884a5c14156ff1f62b63f70aaf55a380)CTIM14\_P23

| #define CTIM14\_P23   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(23, 2) |
| --- |

## [◆ ](#a539c301c87081cafff14c9a0902e90de)CTIM14\_P64

| #define CTIM14\_P64   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(64, 2) |
| --- |

## [◆ ](#acb4d0ec1f842052abd81149b33e8b087)CTIM15\_P32

| #define CTIM15\_P32   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(32, 2) |
| --- |

## [◆ ](#a9a0bb2452ab886f75da833f8c546bef0)CTIM15\_P65

| #define CTIM15\_P65   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(65, 2) |
| --- |

## [◆ ](#a1474daf0d4841a34626d23ce9cd7b545)CTIM16\_P42

| #define CTIM16\_P42   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(42, 2) |
| --- |

## [◆ ](#a365f841a97880964c986c808afe50cbf)CTIM16\_P66

| #define CTIM16\_P66   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(66, 2) |
| --- |

## [◆ ](#ae3a25bc2296db097c9d774e801f146ef)CTIM17\_P4

| #define CTIM17\_P4   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(4, 6) |
| --- |

## [◆ ](#a192693e602f7328d20fcaeb7a80e2b16)CTIM17\_P67

| #define CTIM17\_P67   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(67, 2) |
| --- |

## [◆ ](#ab1b1fb6876a080a75501fce8190c7820)CTIM18\_P43

| #define CTIM18\_P43   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(43, 2) |
| --- |

## [◆ ](#a1db22d617bacc5856a42e817d3aab57a)CTIM18\_P68

| #define CTIM18\_P68   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(68, 2) |
| --- |

## [◆ ](#a25a3df1f226d95466f44b45fccfa9239)CTIM19\_P69

| #define CTIM19\_P69   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(69, 2) |
| --- |

## [◆ ](#af38d97658c4bd9cbb45e822331999a0d)CTIM19\_P7

| #define CTIM19\_P7   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(7, 7) |
| --- |

## [◆ ](#ad871e333e8d90dccce7c7c874da74da2)CTIM1\_P25

| #define CTIM1\_P25   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(25, 2) |
| --- |

## [◆ ](#a4eefe29a2117733367a1883f4c7a233c)CTIM1\_P51

| #define CTIM1\_P51   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(51, 2) |
| --- |

## [◆ ](#a181b829366db1077513b25ba65ea1841)CTIM20\_P44

| #define CTIM20\_P44   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(44, 2) |
| --- |

## [◆ ](#aadd1d390b428c5f7b8196efc46743ea4)CTIM20\_P70

| #define CTIM20\_P70   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(70, 2) |
| --- |

## [◆ ](#a5e3b689232d21c05e42043c61f6e7445)CTIM21\_P24

| #define CTIM21\_P24   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(24, 5) |
| --- |

## [◆ ](#a772105d2fea38c937834c65896d8c3cd)CTIM21\_P71

| #define CTIM21\_P71   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(71, 2) |
| --- |

## [◆ ](#aa1d5c972c6278777fabc856a5f6ff9d3)CTIM22\_P45

| #define CTIM22\_P45   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(45, 2) |
| --- |

## [◆ ](#ac8555a20407cf149854f388bee54f4e0)CTIM22\_P72

| #define CTIM22\_P72   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(72, 2) |
| --- |

## [◆ ](#a4f4778e38e9719f89985ac4cdf98f344)CTIM23\_P33

| #define CTIM23\_P33   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(33, 6) |
| --- |

## [◆ ](#a74b8d5f54ada101a6a29e2c2b17c3a90)CTIM23\_P73

| #define CTIM23\_P73   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(73, 2) |
| --- |

## [◆ ](#a72d372c5f5358c9af85d6802dc317f6e)CTIM24\_P46

| #define CTIM24\_P46   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(46, 2) |
| --- |

## [◆ ](#a6c33f4bc8b739c173b92d185884aaa4b)CTIM25\_P39

| #define CTIM25\_P39   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(39, 2) |
| --- |

## [◆ ](#a0bb0b6007b81b87f0e5a633d962957e5)CTIM26\_P47

| #define CTIM26\_P47   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(47, 2) |
| --- |

## [◆ ](#a3f69161303bc2a76473db22a109aa651)CTIM27\_P35

| #define CTIM27\_P35   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(35, 5) |
| --- |

## [◆ ](#a070d0cbdfdd6525c2d1e61197af52c61)CTIM28\_P48

| #define CTIM28\_P48   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(48, 2) |
| --- |

## [◆ ](#a3dd5aac8ad93fe07b4ab74c35269dba6)CTIM29\_P37

| #define CTIM29\_P37   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(37, 7) |
| --- |

## [◆ ](#a0299d3d82238065f28ea9d60e28e56a0)CTIM2\_P13

| #define CTIM2\_P13   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(13, 2) |
| --- |

## [◆ ](#a826d6ddcd51c2468767bc70583608c29)CTIM2\_P52

| #define CTIM2\_P52   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(52, 2) |
| --- |

## [◆ ](#adce81e86454552afd05cf0144a16a9f4)CTIM30\_P49

| #define CTIM30\_P49   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(49, 2) |
| --- |

## [◆ ](#a994df6ba3173398db50c15364d07ede5)CTIM31\_P11

| #define CTIM31\_P11   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(11, 2) |
| --- |

## [◆ ](#a631c65202c1c83b33c67e105516550f1)CTIM3\_P26

| #define CTIM3\_P26   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(26, 2) |
| --- |

## [◆ ](#a183d8e6c6bd4579d0feae2c3c67e2e61)CTIM3\_P53

| #define CTIM3\_P53   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(53, 2) |
| --- |

## [◆ ](#a2255e19add36a65e7f37d7747afbc28b)CTIM4\_P18

| #define CTIM4\_P18   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(18, 2) |
| --- |

## [◆ ](#ae8b5cb40219aec3a11f0251a39a06a9d)CTIM4\_P54

| #define CTIM4\_P54   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(54, 2) |
| --- |

## [◆ ](#a254e70755e2142d57322a9e19e972f01)CTIM5\_P27

| #define CTIM5\_P27   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(27, 2) |
| --- |

## [◆ ](#a516c0fb62d563ceca86131539f09f131)CTIM5\_P55

| #define CTIM5\_P55   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(55, 2) |
| --- |

## [◆ ](#a7bebc4982a8d3d917996bdc1348c8b1f)CTIM6\_P19

| #define CTIM6\_P19   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(19, 2) |
| --- |

## [◆ ](#ae00988c0a4632e534f2252622bd48759)CTIM6\_P56

| #define CTIM6\_P56   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(56, 2) |
| --- |

## [◆ ](#af89b558743b480da082df15fd2bcecd3)CTIM7\_P28

| #define CTIM7\_P28   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(28, 2) |
| --- |

## [◆ ](#ac2e6c19821053ab44d79a352d48ca1f8)CTIM7\_P57

| #define CTIM7\_P57   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(57, 2) |
| --- |

## [◆ ](#a505da5511b9f77bc9623595b80b9e7d6)CTIM8\_P58

| #define CTIM8\_P58   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(58, 2) |
| --- |

## [◆ ](#a21f4d326b3928de4948b4d2dc41c3368)CTIM9\_P29

| #define CTIM9\_P29   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(29, 2) |
| --- |

## [◆ ](#adc616fdbce3f49c78d01d5ffb9245ada)CTIM9\_P59

| #define CTIM9\_P59   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(59, 2) |
| --- |

## [◆ ](#ada3eedfe2cf44d8f0f1c21d10fc7c81a)GPIO\_P0

| #define GPIO\_P0   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(0, 3) |
| --- |

## [◆ ](#af7a3fb155e6285875e885d5a6344041d)GPIO\_P1

| #define GPIO\_P1   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(1, 3) |
| --- |

## [◆ ](#aeae1f6c04e5fc3c420c3c2311e91c0fb)GPIO\_P10

| #define GPIO\_P10   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(10, 3) |
| --- |

## [◆ ](#a1e2a5bd418526ffe665b93088178edc3)GPIO\_P11

| #define GPIO\_P11   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(11, 3) |
| --- |

## [◆ ](#a2b368e24e962e0bdb34a68dc81a9e929)GPIO\_P12

| #define GPIO\_P12   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(12, 3) |
| --- |

## [◆ ](#a9519265fbdd9fb2adfe818baa0ef933f)GPIO\_P13

| #define GPIO\_P13   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(13, 3) |
| --- |

## [◆ ](#af24f89fe6d38c0db5d7f774e07228678)GPIO\_P14

| #define GPIO\_P14   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(14, 3) |
| --- |

## [◆ ](#a9147a6e2b351214ab5fe7e5d4f6355d7)GPIO\_P15

| #define GPIO\_P15   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(15, 3) |
| --- |

## [◆ ](#a9c21bf7bc952df6b78d19f89f3638833)GPIO\_P16

| #define GPIO\_P16   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(16, 3) |
| --- |

## [◆ ](#a6a5de6dce7def318bec4f73dd614ec22)GPIO\_P17

| #define GPIO\_P17   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(17, 3) |
| --- |

## [◆ ](#a8b325ebb0010179509a1a32450ea72af)GPIO\_P18

| #define GPIO\_P18   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(18, 3) |
| --- |

## [◆ ](#afcadccc574cc0d3c7820ba6b0511612e)GPIO\_P19

| #define GPIO\_P19   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(19, 3) |
| --- |

## [◆ ](#aea5b197be9a863a6db90cb9d42b8a9f2)GPIO\_P2

| #define GPIO\_P2   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(2, 3) |
| --- |

## [◆ ](#afcd63445d3ccf972c95c365f95e30039)GPIO\_P20

| #define GPIO\_P20   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(20, 3) |
| --- |

## [◆ ](#a03d53f3d221401ff02a702ef2c8e05c1)GPIO\_P21

| #define GPIO\_P21   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(21, 3) |
| --- |

## [◆ ](#ad0b28de3a514755dfa6b00fe82579f3d)GPIO\_P22

| #define GPIO\_P22   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(22, 3) |
| --- |

## [◆ ](#a8742762c7c46596977c17898e55f7df0)GPIO\_P23

| #define GPIO\_P23   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(23, 3) |
| --- |

## [◆ ](#a38b0fad90fac621ae3056e0890e5db18)GPIO\_P24

| #define GPIO\_P24   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(24, 3) |
| --- |

## [◆ ](#a70eeb3da2737dc1f88ef0d6b033ba31b)GPIO\_P25

| #define GPIO\_P25   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(25, 3) |
| --- |

## [◆ ](#a70cc23730a6021ba52d4b46466bf7ec8)GPIO\_P26

| #define GPIO\_P26   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(26, 3) |
| --- |

## [◆ ](#a9e3eb9ba4f0604f735fc0da2298dc150)GPIO\_P27

| #define GPIO\_P27   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(27, 3) |
| --- |

## [◆ ](#a6f6f8847e0069b5fefc4a6a54851c99b)GPIO\_P28

| #define GPIO\_P28   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(28, 3) |
| --- |

## [◆ ](#a0c8d4306be59368e181736d98c9d6b4b)GPIO\_P29

| #define GPIO\_P29   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(29, 3) |
| --- |

## [◆ ](#af4024d1ac41ed0426ca701ea851dcd82)GPIO\_P3

| #define GPIO\_P3   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(3, 3) |
| --- |

## [◆ ](#a96753b0a1e5a99e644c3bf21aee043b9)GPIO\_P30

| #define GPIO\_P30   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(30, 3) |
| --- |

## [◆ ](#a2d700f518a2e57f3741c50e0403c471a)GPIO\_P31

| #define GPIO\_P31   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(31, 3) |
| --- |

## [◆ ](#a2a97e46858bf930945c2e03effcc035e)GPIO\_P32

| #define GPIO\_P32   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(32, 3) |
| --- |

## [◆ ](#aa9c2e434db6bed47b117a0764e28889e)GPIO\_P33

| #define GPIO\_P33   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(33, 3) |
| --- |

## [◆ ](#a0b5e8a841aa9e129351ec258cd5849f2)GPIO\_P34

| #define GPIO\_P34   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(34, 3) |
| --- |

## [◆ ](#a26e70a3f976c854799b2451f085ca761)GPIO\_P35

| #define GPIO\_P35   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(35, 3) |
| --- |

## [◆ ](#a3050173d1ff33494b4b047fd11aff68d)GPIO\_P36

| #define GPIO\_P36   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(36, 3) |
| --- |

## [◆ ](#a5895dbfee43e62831294b162bde44b9e)GPIO\_P37

| #define GPIO\_P37   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(37, 3) |
| --- |

## [◆ ](#a8786cdf36cc244ccb754406e7091dc31)GPIO\_P38

| #define GPIO\_P38   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(38, 3) |
| --- |

## [◆ ](#a5a4c89d2f63802373c28dc64010cd6c8)GPIO\_P39

| #define GPIO\_P39   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(39, 3) |
| --- |

## [◆ ](#aea71dd1d14466cec98ab057ece573f75)GPIO\_P4

| #define GPIO\_P4   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(4, 3) |
| --- |

## [◆ ](#a388d84a144f3522f0fa9a6d5f860219c)GPIO\_P40

| #define GPIO\_P40   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(40, 3) |
| --- |

## [◆ ](#a8c96f8b549c1d2739c024137286035e1)GPIO\_P41

| #define GPIO\_P41   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(41, 3) |
| --- |

## [◆ ](#ad2ddbd7fd0001abfcf1416caa9f56496)GPIO\_P42

| #define GPIO\_P42   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(42, 3) |
| --- |

## [◆ ](#aab2f5553d3ce7da8f585c493f82da02f)GPIO\_P43

| #define GPIO\_P43   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(43, 3) |
| --- |

## [◆ ](#accbd9b4f6fa257af91af9a533ba856ea)GPIO\_P44

| #define GPIO\_P44   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(44, 3) |
| --- |

## [◆ ](#afda67e6b2d71c41df2c9384829780eaf)GPIO\_P45

| #define GPIO\_P45   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(45, 3) |
| --- |

## [◆ ](#af5d342a38a441738d343eeef58c1cdb3)GPIO\_P46

| #define GPIO\_P46   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(46, 3) |
| --- |

## [◆ ](#a1eb20e4fdae76831bf870bff406c346e)GPIO\_P47

| #define GPIO\_P47   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(47, 3) |
| --- |

## [◆ ](#af730366def18c0d1bf2e4c00fe3c1ab8)GPIO\_P48

| #define GPIO\_P48   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(48, 3) |
| --- |

## [◆ ](#a4b290382e034342af84424e34cb6d297)GPIO\_P49

| #define GPIO\_P49   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(49, 3) |
| --- |

## [◆ ](#a8b6393ba023af44294a82048f4d7b7fb)GPIO\_P5

| #define GPIO\_P5   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(5, 3) |
| --- |

## [◆ ](#a44de537cf2f84b012dc099c000d47eee)GPIO\_P50

| #define GPIO\_P50   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(50, 3) |
| --- |

## [◆ ](#a78a6a9fa2e9eb9ba6ff803a5810de263)GPIO\_P51

| #define GPIO\_P51   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(51, 3) |
| --- |

## [◆ ](#aa8fc5cd8e841cc12ee97736b5d5b2637)GPIO\_P52

| #define GPIO\_P52   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(52, 3) |
| --- |

## [◆ ](#aa41e6f073ae876d1486552a07ace93a3)GPIO\_P53

| #define GPIO\_P53   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(53, 3) |
| --- |

## [◆ ](#a8b614afb4941fbe9036fa20421a55820)GPIO\_P54

| #define GPIO\_P54   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(54, 3) |
| --- |

## [◆ ](#a2fcffaace9255d9e639de6c2596603c8)GPIO\_P55

| #define GPIO\_P55   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(55, 3) |
| --- |

## [◆ ](#ad9c517c0112a8c8634b9ad46ee32dd45)GPIO\_P56

| #define GPIO\_P56   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(56, 3) |
| --- |

## [◆ ](#a83be188c573c4f64966aae37f47caf5b)GPIO\_P57

| #define GPIO\_P57   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(57, 3) |
| --- |

## [◆ ](#a876dd6e6770f3c605b06c61e9a6640ac)GPIO\_P58

| #define GPIO\_P58   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(58, 3) |
| --- |

## [◆ ](#ab5b877868310ab0269c468edcac715f7)GPIO\_P59

| #define GPIO\_P59   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(59, 3) |
| --- |

## [◆ ](#ab92e5b2728491c7718e22490337a877c)GPIO\_P6

| #define GPIO\_P6   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(6, 3) |
| --- |

## [◆ ](#ac3a637135617760fba12cf98aeb107c2)GPIO\_P60

| #define GPIO\_P60   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(60, 3) |
| --- |

## [◆ ](#a5cc6477cb81b8e732013eee58ce0183d)GPIO\_P61

| #define GPIO\_P61   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(61, 3) |
| --- |

## [◆ ](#ad8ad98d7206b4d60e9a785270cb6bebd)GPIO\_P62

| #define GPIO\_P62   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(62, 3) |
| --- |

## [◆ ](#a9e7881322451f9c064a827bd26c16aa0)GPIO\_P63

| #define GPIO\_P63   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(63, 3) |
| --- |

## [◆ ](#ac031a8b0e6fe953a329bccae5138864c)GPIO\_P64

| #define GPIO\_P64   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(64, 3) |
| --- |

## [◆ ](#ae9af3264c78732b1bc79b552d68dfa6a)GPIO\_P65

| #define GPIO\_P65   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(65, 3) |
| --- |

## [◆ ](#ac82bb9747100752447c61e008d0aed46)GPIO\_P66

| #define GPIO\_P66   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(66, 3) |
| --- |

## [◆ ](#aa9a6029306499ec2cccbb76899488bf3)GPIO\_P67

| #define GPIO\_P67   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(67, 3) |
| --- |

## [◆ ](#a3e315d2425fb95945b68e7c4e2fe954a)GPIO\_P68

| #define GPIO\_P68   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(68, 3) |
| --- |

## [◆ ](#a5602b2af723fb7fe3bf1121b0577c2e7)GPIO\_P69

| #define GPIO\_P69   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(69, 3) |
| --- |

## [◆ ](#a56c293ec75689c3c233d7a0ad4d7428e)GPIO\_P7

| #define GPIO\_P7   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(7, 3) |
| --- |

## [◆ ](#af1f938f04fe3670874c371bfff680c41)GPIO\_P70

| #define GPIO\_P70   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(70, 3) |
| --- |

## [◆ ](#a88cfa6b114b0efb7bfeec35a4110727d)GPIO\_P71

| #define GPIO\_P71   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(71, 3) |
| --- |

## [◆ ](#adcf84a78ff2d8532d87482678ba2df80)GPIO\_P72

| #define GPIO\_P72   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(72, 3) |
| --- |

## [◆ ](#a284f44425e1437643fad644c5f538b09)GPIO\_P73

| #define GPIO\_P73   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(73, 3) |
| --- |

## [◆ ](#a98e2e72127f9d8302c72d588b005ad43)GPIO\_P8

| #define GPIO\_P8   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(8, 3) |
| --- |

## [◆ ](#a62ba7982361959a0ff4013c825611344)GPIO\_P9

| #define GPIO\_P9   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(9, 3) |
| --- |

## [◆ ](#a9a93f8cb9a71278914a878651ab787c6)I2SBCLK\_P13

| #define I2SBCLK\_P13   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(13, 4) |
| --- |

## [◆ ](#ad189a78fbe82f542553e26fe7f06c8b8)I2SBCLK\_P19

| #define I2SBCLK\_P19   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(19, 7) |
| --- |

## [◆ ](#aa16dc261b7d94bbb13919e779208beb1)I2SBCLK\_P20

| #define I2SBCLK\_P20   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(20, 6) |
| --- |

## [◆ ](#a09604ed08062afbbd82ef684a27b196d)I2SBCLK\_P46

| #define I2SBCLK\_P46   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(46, 0) |
| --- |

## [◆ ](#a4eabbfc370ca2db0afd7ceb14769ba21)I2SDAT\_P30

| #define I2SDAT\_P30   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(30, 7) |
| --- |

## [◆ ](#a5f25fda5e336dcdd5d97a0cf9778ee53)I2SDAT\_P35

| #define I2SDAT\_P35   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(35, 4) |
| --- |

## [◆ ](#af628f20a4932e8140b14eb3b4c07b913)I2SDAT\_P45

| #define I2SDAT\_P45   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(45, 4) |
| --- |

## [◆ ](#ae3de66bb2e7fd0e635de7945543bfb07)I2SDAT\_P6

| #define I2SDAT\_P6   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(6, 7) |
| --- |

## [◆ ](#a038809d35e405118dcd792db6cfd078c)I2SWCLK\_P23

| #define I2SWCLK\_P23   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(23, 4) |
| --- |

## [◆ ](#a97a46946f5659dfae1a97dfe56832719)I2SWCLK\_P28

| #define I2SWCLK\_P28   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(28, 0) |
| --- |

## [◆ ](#a2b3c5edbedf68592bfa84e0df9905396)I2SWCLK\_P3

| #define I2SWCLK\_P3   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(3, 7) |
| --- |

## [◆ ](#a1b3a9948d8a90649b505fcb684fe523d)I2SWCLK\_P41

| #define I2SWCLK\_P41   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(41, 4) |
| --- |

## [◆ ](#a01e0417e4c10476d720baa251bf37f41)M0MISO\_P6

| #define M0MISO\_P6   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(6, 1) |
| --- |

## [◆ ](#aa8d862944d509743683a67127dfa38bd)M0MOSI\_P7

| #define M0MOSI\_P7   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(7, 1) |
| --- |

## [◆ ](#abf59b5c6ff03c8a2652d3bc72b872295)M0SCK\_P5

| #define M0SCK\_P5   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(5, 1) |
| --- |

## [◆ ](#a89285a703eabc9b9cc9c962dd7f8856c)M0SCL\_P5

| #define M0SCL\_P5   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(5, 0) |
| --- |

## [◆ ](#a70ecddbefb03c277a58ab1f8c6f4972c)M0SDAWIR3\_P6

| #define M0SDAWIR3\_P6   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(6, 0) |
| --- |

## [◆ ](#a044f3f8861bdfe85899102c4a51dd663)M1MISO\_P9

| #define M1MISO\_P9   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(9, 1) |
| --- |

## [◆ ](#aa99ecc3b8b3e072f245f3779564d9b35)M1MOSI\_P10

| #define M1MOSI\_P10   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(10, 1) |
| --- |

## [◆ ](#aeca27870849b7a78edc8fe37b9966f23)M1SCK\_P8

| #define M1SCK\_P8   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(8, 1) |
| --- |

## [◆ ](#a78f6a3daba1c3af73d6f56e201716c9d)M1SCL\_P8

| #define M1SCL\_P8   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(8, 0) |
| --- |

## [◆ ](#a8a5ee0496cfaf6fe7c0475459ab7ee23)M1SDAWIR3\_P9

| #define M1SDAWIR3\_P9   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(9, 0) |
| --- |

## [◆ ](#a0c695ae4458de77501c1ba4c1a13191b)M2MISO\_P25

| #define M2MISO\_P25   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(25, 5) |
| --- |

## [◆ ](#aad8910b77ff0ffc62ce7b15f49da3bac)M2MOSI\_P28

| #define M2MOSI\_P28   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(28, 5) |
| --- |

## [◆ ](#a371cb048e98d35cab6196193d0c00d4e)M2SCK\_P27

| #define M2SCK\_P27   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(27, 5) |
| --- |

## [◆ ](#ad82dc28ee23bdcc6bcdd3761bb359ab7)M2SCL\_P27

| #define M2SCL\_P27   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(27, 4) |
| --- |

## [◆ ](#aae0817f4cc4c65301171000cb7c0eb88)M2SDAWIR3\_P25

| #define M2SDAWIR3\_P25   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(25, 4) |
| --- |

## [◆ ](#abd8970c9e4ec21d8cb6199f26817a491)M3MISO\_P43

| #define M3MISO\_P43   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(43, 5) |
| --- |

## [◆ ](#a1d5ee7db62801b7f7ba60c4e81daffcf)M3MOSI\_P38

| #define M3MOSI\_P38   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(38, 5) |
| --- |

## [◆ ](#a0a924f11185e5c0c0cc58161efdefcf9)M3SCK\_P42

| #define M3SCK\_P42   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(42, 5) |
| --- |

## [◆ ](#a7be4191ad1020cf880616188964f0a89)M3SCL\_P42

| #define M3SCL\_P42   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(42, 4) |
| --- |

## [◆ ](#a2ea30abd4885c0ca0933d9898b5926d1)M3SDAWIR3\_P43

| #define M3SDAWIR3\_P43   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(43, 4) |
| --- |

## [◆ ](#a3355068431b201477fc0dd1a4f87df68)M4MISO\_P40

| #define M4MISO\_P40   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(40, 5) |
| --- |

## [◆ ](#a11ea4c9cd1f25fc2aba92f5d4ef7b206)M4MOSI\_P44

| #define M4MOSI\_P44   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(44, 5) |
| --- |

## [◆ ](#a76c405ee75ccbd3e6ba7016c25ad09ad)M4SCK\_P39

| #define M4SCK\_P39   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(39, 5) |
| --- |

## [◆ ](#a8a962334908f406e82ac843741b0c837)M4SCL\_P39

| #define M4SCL\_P39   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(39, 4) |
| --- |

## [◆ ](#a9632c0a042f4bb66a728d0b830c40367)M4SDAWIR3\_P40

| #define M4SDAWIR3\_P40   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(40, 4) |
| --- |

## [◆ ](#a9393e54fe2a906feb32275d905db7465)M5MISO\_P49

| #define M5MISO\_P49   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(49, 5) |
| --- |

## [◆ ](#aece153beaf82657c8de3ecd17ea62757)M5MOSI\_P47

| #define M5MOSI\_P47   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(47, 5) |
| --- |

## [◆ ](#a448e33923f0e23281b0d4ef733199b5c)M5SCK\_P48

| #define M5SCK\_P48   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(48, 5) |
| --- |

## [◆ ](#a11a7466d3e7ced79092085f5704fa4d8)M5SCL\_P48

| #define M5SCL\_P48   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(48, 4) |
| --- |

## [◆ ](#ad1fede78430cc3626bddb9fab7b257cf)M5SDAWIR3\_P49

| #define M5SDAWIR3\_P49   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(49, 4) |
| --- |

## [◆ ](#a48cbb6097909f658d824a0267cddb6c6)MSPI0\_0\_P22

| #define MSPI0\_0\_P22   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(22, 6) |
| --- |

## [◆ ](#a9c61cc82c741aa4023a607fbe8fa89c7)MSPI0\_1\_P26

| #define MSPI0\_1\_P26   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(26, 5) |
| --- |

## [◆ ](#a6395a199be7a3ef0d69976a41253282d)MSPI0\_2\_P4

| #define MSPI0\_2\_P4   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(4, 7) |
| --- |

## [◆ ](#a1adc0116ed82c440f4fe64116a021917)MSPI0\_3\_P23

| #define MSPI0\_3\_P23   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(23, 6) |
| --- |

## [◆ ](#ac619aa033a346a49cd8e1c501831c852)MSPI0\_4\_P0

| #define MSPI0\_4\_P0   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(0, 5) |
| --- |

## [◆ ](#a75d2d20c972028ad79e046b31df7aaca)MSPI0\_5\_P1

| #define MSPI0\_5\_P1   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(1, 5) |
| --- |

## [◆ ](#a112ffcf686debe615f04a1fc3c20ceab)MSPI0\_6\_P2

| #define MSPI0\_6\_P2   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(2, 5) |
| --- |

## [◆ ](#a5e93b8d0e2c70144bfaa034aa6dea0d8)MSPI0\_7\_P3

| #define MSPI0\_7\_P3   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(3, 5) |
| --- |

## [◆ ](#ab9a27639f83bfc5f2851ad34abad3efe)MSPI0\_8\_P24

| #define MSPI0\_8\_P24   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(24, 2) |
| --- |

## [◆ ](#a9569a86b721653e4303b538d858362ff)MSPI1\_0\_P51

| #define MSPI1\_0\_P51   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(51, 0) |
| --- |

## [◆ ](#ac6b4ad9a963294d75262c1e94b8abf8f)MSPI1\_1\_P52

| #define MSPI1\_1\_P52   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(52, 0) |
| --- |

## [◆ ](#ac4d5baf17923790039150886151f7dec)MSPI1\_2\_P53

| #define MSPI1\_2\_P53   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(53, 0) |
| --- |

## [◆ ](#a8234fa9ff3afbc23fa0f895f0076835c)MSPI1\_3\_P54

| #define MSPI1\_3\_P54   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(54, 0) |
| --- |

## [◆ ](#abcb127632e19c63b97bd01f6a2de8e9a)MSPI1\_4\_P55

| #define MSPI1\_4\_P55   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(55, 0) |
| --- |

## [◆ ](#a95e11921d5164ad709ab5cdad5f1a58c)MSPI1\_5\_P56

| #define MSPI1\_5\_P56   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(56, 0) |
| --- |

## [◆ ](#a8831303ca7109996c6446350e384392d)MSPI1\_6\_P57

| #define MSPI1\_6\_P57   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(57, 0) |
| --- |

## [◆ ](#ab61ac243ccd5f0a1d1fdec4b8d45b6dc)MSPI1\_7\_P58

| #define MSPI1\_7\_P58   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(58, 0) |
| --- |

## [◆ ](#ae74279d568a99727bd00816f856f2bec)MSPI1\_8\_P59

| #define MSPI1\_8\_P59   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(59, 0) |
| --- |

## [◆ ](#acbdd8675b5c6094213377db4d57b5c76)MSPI1\_9\_P60

| #define MSPI1\_9\_P60   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(60, 0) |
| --- |

## [◆ ](#a47ffd6951b155ac3b80a5f4ac5057e8b)MSPI2\_0\_P64

| #define MSPI2\_0\_P64   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(64, 0) |
| --- |

## [◆ ](#a267fef799fd16097688aa7a777fb5194)MSPI2\_1\_P65

| #define MSPI2\_1\_P65   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(65, 0) |
| --- |

## [◆ ](#a4dcf9f729fb234071170c7116620bdbc)MSPI2\_2\_P66

| #define MSPI2\_2\_P66   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(66, 0) |
| --- |

## [◆ ](#a13cbb5730534690db2ce73c739bce161)MSPI2\_3\_P67

| #define MSPI2\_3\_P67   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(67, 0) |
| --- |

## [◆ ](#adcca1198343f7a85b2f87b1917cfc6c0)MSPI2\_4\_P68

| #define MSPI2\_4\_P68   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(68, 0) |
| --- |

## [◆ ](#a2f7a5ec8bae150c5d845a85d65991107)NCE0\_P0

| #define NCE0\_P0   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(0, 7) |
| --- |

## [◆ ](#aad947baa0652e59cb21735eae01eca09)NCE10\_P10

| #define NCE10\_P10   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(10, 2) |
| --- |

## [◆ ](#ab635978b874de8fbe6f96506b06ae5f1)NCE11\_P11

| #define NCE11\_P11   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(11, 1) |
| --- |

## [◆ ](#aeeea37f1af4c943883760c8e273f26a1)NCE12\_P12

| #define NCE12\_P12   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(12, 1) |
| --- |

## [◆ ](#a03383f0fcb11b35cac08703aa51cdb56)NCE13\_P13

| #define NCE13\_P13   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(13, 1) |
| --- |

## [◆ ](#a39f9f5d31b34dd21c12439c0a9fd032f)NCE14\_P14

| #define NCE14\_P14   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(14, 1) |
| --- |

## [◆ ](#ab6136185e31fbbb173391d77723de46a)NCE15\_P15

| #define NCE15\_P15   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(15, 1) |
| --- |

## [◆ ](#a5da8200119b0e8a2e6fec1097896edd1)NCE16\_P16

| #define NCE16\_P16   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(16, 1) |
| --- |

## [◆ ](#ab89d7eb6aa6e611a3a95cc1ee913731c)NCE17\_P17

| #define NCE17\_P17   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(17, 1) |
| --- |

## [◆ ](#a566a450bf9afa441315c83bf4d0ce580)NCE18\_P18

| #define NCE18\_P18   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(18, 1) |
| --- |

## [◆ ](#af9d50128143543f345b8db2d2e3e0918)NCE19\_P19

| #define NCE19\_P19   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(19, 1) |
| --- |

## [◆ ](#aad38da06e56246b4ed48ddbf43f1aaca)NCE1\_P1

| #define NCE1\_P1   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(1, 7) |
| --- |

## [◆ ](#a8c4f0230a390d43b9a408ec438b5dbe6)NCE20\_P20

| #define NCE20\_P20   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(20, 1) |
| --- |

## [◆ ](#a3a7292f75cecf7ac798212bbfef2ff3a)NCE21\_P21

| #define NCE21\_P21   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(21, 1) |
| --- |

## [◆ ](#a775bbd5124031418e8f5b723e99ac9ab)NCE22\_P22

| #define NCE22\_P22   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(22, 1) |
| --- |

## [◆ ](#a0a52f7e779022ce90fe4d7ce7b200f6d)NCE23\_P23

| #define NCE23\_P23   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(23, 1) |
| --- |

## [◆ ](#aef5c8fe782ba1f615e0ea35d44a942ce)NCE24\_P24

| #define NCE24\_P24   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(24, 1) |
| --- |

## [◆ ](#a6c08788db3454db63bc8e5bca88b61a1)NCE25\_P25

| #define NCE25\_P25   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(25, 1) |
| --- |

## [◆ ](#a498a5dcaa37b5a972e8eea27c29617ef)NCE26\_P26

| #define NCE26\_P26   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(26, 1) |
| --- |

## [◆ ](#a4b0b9c08da925a4a55bf9cd8342e275d)NCE27\_P27

| #define NCE27\_P27   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(27, 1) |
| --- |

## [◆ ](#ac975e39671e4884de16995b831c3bc52)NCE28\_P28

| #define NCE28\_P28   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(28, 1) |
| --- |

## [◆ ](#ac7c4f18c7b072968ce9048bb9057356c)NCE29\_P29

| #define NCE29\_P29   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(29, 1) |
| --- |

## [◆ ](#a41c7834b7cc3a8f2f75021ec9ebedf6a)NCE2\_P2

| #define NCE2\_P2   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(2, 7) |
| --- |

## [◆ ](#a6d9a17fecc9e2687ede485e719c5e616)NCE30\_P30

| #define NCE30\_P30   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(30, 1) |
| --- |

## [◆ ](#aa1001078fb5a05925a8b02e6ecca70c5)NCE31\_P31

| #define NCE31\_P31   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(31, 1) |
| --- |

## [◆ ](#afb0f804646a6e3557dd4341eb7d72a74)NCE32\_P32

| #define NCE32\_P32   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(32, 1) |
| --- |

## [◆ ](#aa91f920fb637bf393393bac80a9e49ba)NCE33\_P33

| #define NCE33\_P33   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(33, 1) |
| --- |

## [◆ ](#a4f042898a506cccce60699375b16bf85)NCE34\_P34

| #define NCE34\_P34   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(34, 1) |
| --- |

## [◆ ](#ad2cdd6497fb562ea4738beb637e044d1)NCE35\_P35

| #define NCE35\_P35   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(35, 1) |
| --- |

## [◆ ](#aae112b0ebd7c6f448b1ce24b772910a4)NCE36\_P36

| #define NCE36\_P36   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(36, 1) |
| --- |

## [◆ ](#a736adccb71d5a32e0519cbd8c89d6b77)NCE37\_P37

| #define NCE37\_P37   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(37, 1) |
| --- |

## [◆ ](#a7eb51c6fb1bdaabcd854928f0fc53365)NCE38\_P38

| #define NCE38\_P38   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(38, 1) |
| --- |

## [◆ ](#a49fa96fac299d83fe34b116fc2e8d586)NCE3\_P3

| #define NCE3\_P3   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(3, 2) |
| --- |

## [◆ ](#aaaf74f87cd67b25b654c92e58311d818)NCE41\_P41

| #define NCE41\_P41   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(41, 0) |
| --- |

## [◆ ](#ae5399f9d5357e096d59283bfea4fd6ee)NCE42\_P42

| #define NCE42\_P42   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(42, 1) |
| --- |

## [◆ ](#a93e018507d62174c89e7fa137dde36cd)NCE43\_P43

| #define NCE43\_P43   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(43, 1) |
| --- |

## [◆ ](#a3ed79603ebbdb77c08f3d793c0f361d7)NCE44\_P44

| #define NCE44\_P44   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(44, 1) |
| --- |

## [◆ ](#a8b9c9c5513d7098d3772bf031eefdc34)NCE45\_P45

| #define NCE45\_P45   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(45, 1) |
| --- |

## [◆ ](#a5b0e939354b2c232bdc48a3dcb9a1607)NCE46\_P46

| #define NCE46\_P46   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(46, 1) |
| --- |

## [◆ ](#a1f411d730489dee140ae375049d449fd)NCE47\_P47

| #define NCE47\_P47   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(47, 1) |
| --- |

## [◆ ](#ad2333f40db7fb9ecfbd1392e9554ffa3)NCE48\_P48

| #define NCE48\_P48   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(48, 1) |
| --- |

## [◆ ](#a339781c28180de2027fc9295189463e1)NCE49\_P49

| #define NCE49\_P49   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(49, 1) |
| --- |

## [◆ ](#a3019076e21641ad28be64b29a4b2c671)NCE4\_P4

| #define NCE4\_P4   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(4, 2) |
| --- |

## [◆ ](#ab7492256a637deef5ea4943b4b701110)NCE50\_P50

| #define NCE50\_P50   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(50, 1) |
| --- |

## [◆ ](#aeca26feeace6bc79995c2e619b1a9c18)NCE51\_P51

| #define NCE51\_P51   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(51, 1) |
| --- |

## [◆ ](#ae86416562248f70f8fddcbfda85a3ae3)NCE52\_P52

| #define NCE52\_P52   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(52, 1) |
| --- |

## [◆ ](#aae0ee7affb647cfd3d54d168868ef485)NCE53\_P53

| #define NCE53\_P53   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(53, 1) |
| --- |

## [◆ ](#a6318a96c1367922e5ecd0f682d432630)NCE54\_P54

| #define NCE54\_P54   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(54, 1) |
| --- |

## [◆ ](#ad5438399e3ff56c263631991b09dd460)NCE55\_P55

| #define NCE55\_P55   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(55, 1) |
| --- |

## [◆ ](#ad8e09cff85610b1bfb03403771360685)NCE56\_P56

| #define NCE56\_P56   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(56, 1) |
| --- |

## [◆ ](#a98fb369e6acd52cc5aae8e6730ed9758)NCE57\_P57

| #define NCE57\_P57   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(57, 1) |
| --- |

## [◆ ](#aac11c1a52fc64f3c2684b4323e28bdb4)NCE58\_P58

| #define NCE58\_P58   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(58, 1) |
| --- |

## [◆ ](#ab437cea609c7b3dbdec00e17f674ee6c)NCE59\_P59

| #define NCE59\_P59   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(59, 1) |
| --- |

## [◆ ](#af5a0f373987f9e093d0be1e96fc422e0)NCE60\_P60

| #define NCE60\_P60   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(60, 1) |
| --- |

## [◆ ](#ab5911745a6c23c3a7ded39e214324a1b)NCE61\_P61

| #define NCE61\_P61   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(61, 1) |
| --- |

## [◆ ](#acff3d4c76b5032bc61e0757224cf5c30)NCE62\_P62

| #define NCE62\_P62   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(62, 1) |
| --- |

## [◆ ](#acd4dd1d3133002f0c60426e542702dd3)NCE63\_P63

| #define NCE63\_P63   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(63, 1) |
| --- |

## [◆ ](#af279b091bf1b2e9854cb240fb07d7411)NCE64\_P64

| #define NCE64\_P64   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(64, 1) |
| --- |

## [◆ ](#a4913e8e909a5f53078ec4f73eda5c112)NCE65\_P65

| #define NCE65\_P65   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(65, 1) |
| --- |

## [◆ ](#acff679577d81e687a56906eebf769bf6)NCE66\_P66

| #define NCE66\_P66   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(66, 1) |
| --- |

## [◆ ](#a94cc174e483db8110ca76fff12629c6d)NCE67\_P67

| #define NCE67\_P67   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(67, 1) |
| --- |

## [◆ ](#a43db97f86803b04b80140c3c12f096d5)NCE68\_P68

| #define NCE68\_P68   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(68, 1) |
| --- |

## [◆ ](#a8e86b1f165b06bde1344f2a0591591f6)NCE69\_P69

| #define NCE69\_P69   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(69, 1) |
| --- |

## [◆ ](#a154b9a05cda9e8a41f84f82417a60d81)NCE70\_P70

| #define NCE70\_P70   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(70, 1) |
| --- |

## [◆ ](#a04df6aa292fc65e77cc4de70b36d3d95)NCE71\_P71

| #define NCE71\_P71   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(71, 1) |
| --- |

## [◆ ](#a89192a0beda2cecdd53e4fd7174302e5)NCE72\_P72

| #define NCE72\_P72   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(72, 1) |
| --- |

## [◆ ](#a86228f8d9adc8065f76ca1f0af512d50)NCE73\_P73

| #define NCE73\_P73   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(73, 1) |
| --- |

## [◆ ](#ac34242faa4992e4acc075a36264d7187)NCE7\_P7

| #define NCE7\_P7   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(7, 0) |
| --- |

## [◆ ](#a6c400fdb4e2e68a5a28f2aade3509822)NCE8\_P8

| #define NCE8\_P8   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(8, 2) |
| --- |

## [◆ ](#aa92d1c97c14770e3e29a271706d76a28)NCE9\_P9

| #define NCE9\_P9   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(9, 2) |
| --- |

## [◆ ](#a432af451cbdf1a8e0137e61def76d525)PDMCLK\_P10

| #define PDMCLK\_P10   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(10, 4) |
| --- |

## [◆ ](#a839ddc0937ffa9b306f491f263ac5ede)PDMCLK\_P12

| #define PDMCLK\_P12   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(12, 5) |
| --- |

## [◆ ](#aacd23325f76bea9db0c004775953572d)PDMCLK\_P14

| #define PDMCLK\_P14   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(14, 4) |
| --- |

## [◆ ](#ad1b1036bf8cb0807af04662b1c6a9f8f)PDMCLK\_P22

| #define PDMCLK\_P22   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(22, 4) |
| --- |

## [◆ ](#a2dc471687b4110dc079f5d896f7fe2e2)PDMCLK\_P37

| #define PDMCLK\_P37   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(37, 6) |
| --- |

## [◆ ](#a60677b54a72e30bfd0c04de7ff9217a7)PDMCLK\_P46

| #define PDMCLK\_P46   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(46, 5) |
| --- |

## [◆ ](#a4a9e07c73a2062220944fac15bc9976c)PDMDATA\_P11

| #define PDMDATA\_P11   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(11, 7) |
| --- |

## [◆ ](#ae98b714215455ad42b61c940d47a5658)PDMDATA\_P15

| #define PDMDATA\_P15   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(15, 4) |
| --- |

## [◆ ](#a7447bed11900ad2fc0c1fdec80c633f5)PDMDATA\_P29

| #define PDMDATA\_P29   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(29, 7) |
| --- |

## [◆ ](#a3288f0cd1140d15ca20840fffe78daaa)PDMDATA\_P34

| #define PDMDATA\_P34   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(34, 7) |
| --- |

## [◆ ](#aaf12889bb6f7de1a92c0d10147c921bf)PDMDATA\_P36

| #define PDMDATA\_P36   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(36, 7) |
| --- |

## [◆ ](#ac3d93a44f8fa496120aff6de06813fcc)PDMDATA\_P45

| #define PDMDATA\_P45   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(45, 5) |
| --- |

## [◆ ](#a532591d82e99327eec3d5ecaf71fd234)SCCCLK\_P17

| #define SCCCLK\_P17   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(17, 4) |
| --- |

## [◆ ](#a5e41d1a7b81ac2349f2b6dece08850a4)SCCCLK\_P19

| #define SCCCLK\_P19   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(19, 4) |
| --- |

## [◆ ](#a6cd0038a5d5bfa4008eae6666323e3a2)SCCCLK\_P31

| #define SCCCLK\_P31   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(31, 5) |
| --- |

## [◆ ](#a656853201d5b7b94a3019767ec187d0c)SCCCLK\_P8

| #define SCCCLK\_P8   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(8, 4) |
| --- |

## [◆ ](#a3c89b132043f8dabd531955c7f3b67a5)SCCIO\_P18

| #define SCCIO\_P18   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(18, 7) |
| --- |

## [◆ ](#a0562630e3ed7a89a28ea8e9d877a25b5)SCCIO\_P32

| #define SCCIO\_P32   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(32, 4) |
| --- |

## [◆ ](#ab0f35ce206392abf106f6b0e702664c1)SCCIO\_P37

| #define SCCIO\_P37   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(37, 4) |
| --- |

## [◆ ](#a0def8b127d3740da2bb3ae2b44d0095c)SCCIO\_P9

| #define SCCIO\_P9   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(9, 4) |
| --- |

## [◆ ](#a8e59ac2cee69f18f8c23e71e34779d5f)SCCRST\_P16

| #define SCCRST\_P16   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(16, 4) |
| --- |

## [◆ ](#a8de11c1add0069e7af62e5bbc3b55dbd)SCCRST\_P21

| #define SCCRST\_P21   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(21, 6) |
| --- |

## [◆ ](#a645b6c6e3f318aa5ac4fa619a835cd59)SCCRST\_P26

| #define SCCRST\_P26   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(26, 4) |
| --- |

## [◆ ](#add5fa4e696047cb893bb829416ee2afd)SCCRST\_P46

| #define SCCRST\_P46   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(46, 4) |
| --- |

## [◆ ](#acab95c4dfc69402cb93aa80cb368a8ed)SLINT\_P11

| #define SLINT\_P11   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(11, 4) |
| --- |

## [◆ ](#a29c616828e653cb4f0cecaca1f0bc8f1)SLINT\_P4

| #define SLINT\_P4   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(4, 1) |
| --- |

## [◆ ](#a06beb22570d100e28198606d21909a6c)SLMISO\_P2

| #define SLMISO\_P2   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(2, 1) |
| --- |

## [◆ ](#a4fd87e65fcf8776a98224ca1d468b0ad)SLMOSI\_P1

| #define SLMOSI\_P1   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(1, 1) |
| --- |

## [◆ ](#a42fc82a09d814a6774ee02b1b0228cd8)SLNCE\_P3

| #define SLNCE\_P3   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(3, 1) |
| --- |

## [◆ ](#ae72cb1519562643c48a8ffff88dc9d00)SLSCK\_P0

| #define SLSCK\_P0   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(0, 1) |
| --- |

## [◆ ](#a3a72f1023828af4b3766cc0714c404b2)SLSCL\_P0

| #define SLSCL\_P0   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(0, 0) |
| --- |

## [◆ ](#ae5b84a6fa44069d704c6c87113bef6e7)SLSDAWIR3\_P1

| #define SLSDAWIR3\_P1   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(1, 0) |
| --- |

## [◆ ](#af6db4faf2bc7ec69d646e556f3475c6b)SWDCK\_P14

| #define SWDCK\_P14   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(14, 6) |
| --- |

## [◆ ](#a3885c97e098dfed018491c67065e696c)SWDCK\_P20

| #define SWDCK\_P20   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(20, 0) |
| --- |

## [◆ ](#ac7018578ab5232a026d00f93005cd1d2)SWDIO\_P15

| #define SWDIO\_P15   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(15, 6) |
| --- |

## [◆ ](#a184cab7037772c8ca8ecc296ea9c7e48)SWDIO\_P21

| #define SWDIO\_P21   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(21, 0) |
| --- |

## [◆ ](#a335a3b83d4115419e3f752ba6cc6c3c2)SWO\_P15

| #define SWO\_P15   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(15, 7) |
| --- |

## [◆ ](#af2e7742c9a96fe5ac1a2de402bd5f72f)SWO\_P22

| #define SWO\_P22   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(22, 7) |
| --- |

## [◆ ](#acc4f37955d3cc5567dddb283275cd791)SWO\_P24

| #define SWO\_P24   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(24, 7) |
| --- |

## [◆ ](#ae998e2b505d3b112532b1b58fd298d01)SWO\_P33

| #define SWO\_P33   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(33, 7) |
| --- |

## [◆ ](#a7d5cbbcd03000b54af3d06566fd3b659)SWO\_P41

| #define SWO\_P41   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(41, 2) |
| --- |

## [◆ ](#ab1907bebf4d3e6951994035f697ed321)SWO\_P45

| #define SWO\_P45   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(45, 7) |
| --- |

## [◆ ](#a17e7362e03a87627fff5643989fcca00)SWO\_P46

| #define SWO\_P46   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(46, 7) |
| --- |

## [◆ ](#a056b770b0d92b72bd3c33a957683c790)SWO\_P50

| #define SWO\_P50   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(50, 0) |
| --- |

## [◆ ](#af6865d7d7b0939fee8634025753ad0ac)SWO\_P61

| #define SWO\_P61   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(61, 0) |
| --- |

## [◆ ](#ac3477b8ba498f9d6ce303c891fc92102)SWO\_P62

| #define SWO\_P62   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(62, 0) |
| --- |

## [◆ ](#ad1a604f4d60d6ffc7182e7655073bd11)SWO\_P63

| #define SWO\_P63   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(63, 0) |
| --- |

## [◆ ](#a5fa4920fa2af91403279165ec14471c3)SWO\_P69

| #define SWO\_P69   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(69, 0) |
| --- |

## [◆ ](#ae840ad7da2d8d0741a885d60b108c6f6)SWO\_P70

| #define SWO\_P70   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(70, 0) |
| --- |

## [◆ ](#a5b05a881450d820175599526bca285e7)SWO\_P71

| #define SWO\_P71   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(71, 0) |
| --- |

## [◆ ](#aeeb7f033753b1196ff4acb716be4e782)SWO\_P72

| #define SWO\_P72   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(72, 0) |
| --- |

## [◆ ](#a9a2b1491dd870b395c181ecd48d136c0)SWO\_P73

| #define SWO\_P73   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(73, 0) |
| --- |

## [◆ ](#a7fb00b38e52d1115ce542b0f00b80ac7)TRIG0\_P16

| #define TRIG0\_P16   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(16, 2) |
| --- |

## [◆ ](#a4d41b8f7fd97fcae660bf35bf562f4b8)TRIG0\_P40

| #define TRIG0\_P40   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(40, 2) |
| --- |

## [◆ ](#a00614cfc545401d5e8cb9f1e51848571)TRIG0\_P7

| #define TRIG0\_P7   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(7, 4) |
| --- |

## [◆ ](#a3c59efbb8cf2245b113f8d4a5119b7c6)TRIG1\_P17

| #define TRIG1\_P17   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(17, 2) |
| --- |

## [◆ ](#a2afa9eb9453ab24b55280c9680e8bca7)TRIG1\_P3

| #define TRIG1\_P3   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(3, 6) |
| --- |

## [◆ ](#a3595cef3917f8dbb33c495fa3dd129d9)TRIG1\_P36

| #define TRIG1\_P36   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(36, 0) |
| --- |

## [◆ ](#a1bf06e0a3c6234f2c594939d658de1de)TRIG2\_P37

| #define TRIG2\_P37   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(37, 0) |
| --- |

## [◆ ](#a2d5a132e305dbb9cc38b4f062ab2a5a1)TRIG3\_P38

| #define TRIG3\_P38   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(38, 0) |
| --- |

## [◆ ](#ab5ce9319d6fc8bdb1496be5f2f015358)UA0CTS\_P12

| #define UA0CTS\_P12   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(12, 6) |
| --- |

## [◆ ](#a2f9bcf5acd23826869291e4ae956ee91)UA0CTS\_P24

| #define UA0CTS\_P24   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(24, 4) |
| --- |

## [◆ ](#ae0f8b8eac04505e31e3a54101a6d7cfa)UA0CTS\_P29

| #define UA0CTS\_P29   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(29, 4) |
| --- |

## [◆ ](#a5f64c8ebf5a704ad48dbf12ce595f504)UA0CTS\_P33

| #define UA0CTS\_P33   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(33, 5) |
| --- |

## [◆ ](#a6a6bf8ffd195353bbccb43904442db80)UA0CTS\_P36

| #define UA0CTS\_P36   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(36, 6) |
| --- |

## [◆ ](#aa49ea18a61d8190908b5556c6298e6fa)UA0CTS\_P38

| #define UA0CTS\_P38   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(38, 2) |
| --- |

## [◆ ](#a7c15b0f583db4314e7b315e553e6ec89)UA0CTS\_P4

| #define UA0CTS\_P4   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(4, 0) |
| --- |

## [◆ ](#a0ec1a55c1287c1b4524670c836aa3610)UA0CTS\_P6

| #define UA0CTS\_P6   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(6, 2) |
| --- |

## [◆ ](#a17a8866677f47e6edc86a3873c09d606)UA0CTS\_P62

| #define UA0CTS\_P62   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(62, 4) |
| --- |

## [◆ ](#aad6095bc6dc59c8cfb0a1c19d937d573)UA0CTS\_P63

| #define UA0CTS\_P63   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(63, 4) |
| --- |

## [◆ ](#af8cca7cdb1b7794250c131fce4e0dc54)UA0CTS\_P73

| #define UA0CTS\_P73   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(73, 4) |
| --- |

## [◆ ](#accb8206aa72638560dfb39d1225d21c3)UA0RTS\_P13

| #define UA0RTS\_P13   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(13, 6) |
| --- |

## [◆ ](#a4c2b318d489aa88d6da183c55d3dbfcf)UA0RTS\_P18

| #define UA0RTS\_P18   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(18, 4) |
| --- |

## [◆ ](#ae5123e7f8df58cc8ca300bc955a855d3)UA0RTS\_P3

| #define UA0RTS\_P3   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(3, 0) |
| --- |

## [◆ ](#af821710452cee65f18e7d9d21f16be5e)UA0RTS\_P34

| #define UA0RTS\_P34   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(34, 5) |
| --- |

## [◆ ](#a5b92e6ee90a413909f63c838283f7777)UA0RTS\_P35

| #define UA0RTS\_P35   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(35, 6) |
| --- |

## [◆ ](#a3b0abd07adcc2cd6b6764f715cd21cd5)UA0RTS\_P37

| #define UA0RTS\_P37   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(37, 2) |
| --- |

## [◆ ](#aff53cdfb5a9f567fea668005ef248f8a)UA0RTS\_P41

| #define UA0RTS\_P41   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(41, 7) |
| --- |

## [◆ ](#a9af295a6b30a9ebfa26d89187a765817)UA0RTS\_P5

| #define UA0RTS\_P5   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(5, 2) |
| --- |

## [◆ ](#a3330f5f0766f022c8d4f215395ef1f8f)UA0RTS\_P62

| #define UA0RTS\_P62   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(62, 5) |
| --- |

## [◆ ](#ab0422d143c7ddf4dd7fce671af815bb9)UA0RTS\_P63

| #define UA0RTS\_P63   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(63, 5) |
| --- |

## [◆ ](#afc2a1cd4bc96170933509a26828ca200)UA0RTS\_P73

| #define UA0RTS\_P73   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(73, 5) |
| --- |

## [◆ ](#a0c85b60521c7052487e84b4eb1031be1)UA1CTS\_P11

| #define UA1CTS\_P11   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(11, 5) |
| --- |

## [◆ ](#a199a40fbe31c452461f0ba88e2dfc559)UA1CTS\_P17

| #define UA1CTS\_P17   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(17, 7) |
| --- |

## [◆ ](#a8149767283ba99d3fbf7c73ca017a565)UA1CTS\_P21

| #define UA1CTS\_P21   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(21, 7) |
| --- |

## [◆ ](#ab57497d2c1a2802d788f940456afc86d)UA1CTS\_P26

| #define UA1CTS\_P26   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(26, 7) |
| --- |

## [◆ ](#a9072e7364c227042f9232c48b6b6b9c2)UA1CTS\_P29

| #define UA1CTS\_P29   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(29, 5) |
| --- |

## [◆ ](#a6d5db72517c101eea3a3aca07b716869)UA1CTS\_P32

| #define UA1CTS\_P32   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(32, 7) |
| --- |

## [◆ ](#a1b3e74a2c7e43f142fdc02b096236733)UA1CTS\_P36

| #define UA1CTS\_P36   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(36, 5) |
| --- |

## [◆ ](#a944d829a81b45cf99560241e9b19154d)UA1CTS\_P45

| #define UA1CTS\_P45   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(45, 0) |
| --- |

## [◆ ](#a5619b10dd987655fd0f8b470832dd617)UA1CTS\_P62

| #define UA1CTS\_P62   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(62, 6) |
| --- |

## [◆ ](#a0d8dd2d9de57fd25bb59d31be03014ec)UA1CTS\_P63

| #define UA1CTS\_P63   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(63, 6) |
| --- |

## [◆ ](#a76e95ea07d5a29cb8bf391ceeda6b177)UA1CTS\_P73

| #define UA1CTS\_P73   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(73, 6) |
| --- |

## [◆ ](#ab98a61028f7a8b5e45841dc3d5ab0672)UA1RTS\_P10

| #define UA1RTS\_P10   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(10, 6) |
| --- |

## [◆ ](#a5f8c363f21f1a089c1d560a9b975ac41)UA1RTS\_P16

| #define UA1RTS\_P16   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(16, 7) |
| --- |

## [◆ ](#a01a5858ec4972916023b83541ea9a17e)UA1RTS\_P20

| #define UA1RTS\_P20   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(20, 7) |
| --- |

## [◆ ](#a0d65684ea5cbc9fd0e75f1f849117a27)UA1RTS\_P30

| #define UA1RTS\_P30   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(30, 5) |
| --- |

## [◆ ](#ad7a6b728d49d7ae25431e80cf56aab1b)UA1RTS\_P31

| #define UA1RTS\_P31   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(31, 7) |
| --- |

## [◆ ](#a6a490d5a195593605844d2883373ab33)UA1RTS\_P34

| #define UA1RTS\_P34   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(34, 2) |
| --- |

## [◆ ](#a09961d9c0667f515d82a7c53e972a48d)UA1RTS\_P41

| #define UA1RTS\_P41   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(41, 5) |
| --- |

## [◆ ](#a46baf1010c95eee1dc0011c1864c4796)UA1RTS\_P44

| #define UA1RTS\_P44   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(44, 0) |
| --- |

## [◆ ](#ac844f507a7ad999a2ce9a749667d43ec)UA1RTS\_P62

| #define UA1RTS\_P62   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(62, 7) |
| --- |

## [◆ ](#a362e069b94a6ea0b5bb1f5b64aef473f)UA1RTS\_P63

| #define UA1RTS\_P63   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(63, 7) |
| --- |

## [◆ ](#abcc0c2177d3ebab6aef372b39aeff6cb)UA1RTS\_P73

| #define UA1RTS\_P73   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(73, 7) |
| --- |

## [◆ ](#aff7e0941ffab586464b6a42edf32cf84)UART0RX\_P11

| #define UART0RX\_P11   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(11, 6) |
| --- |

## [◆ ](#a67731a70bfa50b5a9ac8ff30e1343fba)UART0RX\_P17

| #define UART0RX\_P17   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(17, 6) |
| --- |

## [◆ ](#aeb4da21d8f3fdb747865ff6b6a7ea49e)UART0RX\_P2

| #define UART0RX\_P2   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(2, 2) |
| --- |

## [◆ ](#ae642493fcee53d0fe7a2af91e1cac307)UART0RX\_P21

| #define UART0RX\_P21   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(21, 4) |
| --- |

## [◆ ](#aee79208585ea908eac11cadf34078045)UART0RX\_P23

| #define UART0RX\_P23   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(23, 0) |
| --- |

## [◆ ](#ac18a31df22a6076cd39c0f34e82794a0)UART0RX\_P27

| #define UART0RX\_P27   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(27, 0) |
| --- |

## [◆ ](#a97be8cedd244e53e809d38cdeb4933c3)UART0RX\_P29

| #define UART0RX\_P29   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(29, 6) |
| --- |

## [◆ ](#a7e23355beb26a376895e08aac26dea57)UART0RX\_P31

| #define UART0RX\_P31   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(31, 4) |
| --- |

## [◆ ](#ae54604f59f12de3bd10dc115e256b69a)UART0RX\_P34

| #define UART0RX\_P34   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(34, 6) |
| --- |

## [◆ ](#a175181dfaf1f6fff4ef61181d450b0f3)UART0RX\_P40

| #define UART0RX\_P40   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(40, 0) |
| --- |

## [◆ ](#af7673ee93e7a84ad6e16846d98de6464)UART0RX\_P45

| #define UART0RX\_P45   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(45, 6) |
| --- |

## [◆ ](#a70696ef3a46aa08391bdf4d3ebc9aa3f)UART0RX\_P49

| #define UART0RX\_P49   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(49, 0) |
| --- |

## [◆ ](#a6277bab84473fecc433b54e6a29b3c40)UART0RX\_P50

| #define UART0RX\_P50   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(50, 5) |
| --- |

## [◆ ](#a5ef06f1ca2d2d28e87846add941a6a01)UART0RX\_P61

| #define UART0RX\_P61   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(61, 5) |
| --- |

## [◆ ](#ac0aec58a68e82e74ff74d31889ba6eda)UART0RX\_P69

| #define UART0RX\_P69   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(69, 5) |
| --- |

## [◆ ](#a086d2fe9f77498d1fee5ad62570a41a1)UART0RX\_P70

| #define UART0RX\_P70   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(70, 5) |
| --- |

## [◆ ](#ae8e2a290af35da4c5d4d882eaa3aa8cd)UART0RX\_P71

| #define UART0RX\_P71   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(71, 5) |
| --- |

## [◆ ](#a6720bbe266f8a2d54929325ee19c3b23)UART0RX\_P72

| #define UART0RX\_P72   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(72, 5) |
| --- |

## [◆ ](#aa237cfc2d6eda1c3ddf349b5a3330898)UART0TX\_P1

| #define UART0TX\_P1   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(1, 2) |
| --- |

## [◆ ](#a26f7e4ec8471988685bab0fa0f666af7)UART0TX\_P16

| #define UART0TX\_P16   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(16, 6) |
| --- |

## [◆ ](#af9acded122c3567a0f7fae29561351e5)UART0TX\_P20

| #define UART0TX\_P20   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(20, 4) |
| --- |

## [◆ ](#ad7370389dba6304d21d5f95d57dca5dc)UART0TX\_P22

| #define UART0TX\_P22   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(22, 0) |
| --- |

## [◆ ](#a0a5809f404cde8111cfdfa67b5975607)UART0TX\_P26

| #define UART0TX\_P26   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(26, 6) |
| --- |

## [◆ ](#a351989945b5403624c7d4fa53a44ab86)UART0TX\_P28

| #define UART0TX\_P28   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(28, 6) |
| --- |

## [◆ ](#aa507368219464308827240872d0eab11)UART0TX\_P30

| #define UART0TX\_P30   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(30, 4) |
| --- |

## [◆ ](#a3ed9a495f050ab7486aadc5867539a59)UART0TX\_P39

| #define UART0TX\_P39   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(39, 0) |
| --- |

## [◆ ](#a2b7dc7334200258b20a08422ea361f70)UART0TX\_P41

| #define UART0TX\_P41   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(41, 6) |
| --- |

## [◆ ](#a51592b8b7e152dbb622ef0a330862341)UART0TX\_P44

| #define UART0TX\_P44   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(44, 6) |
| --- |

## [◆ ](#aaaafe03305c7bafe3020c6c50e56d3dd)UART0TX\_P48

| #define UART0TX\_P48   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(48, 0) |
| --- |

## [◆ ](#ab967379871f5d5e937c536b0af767154)UART0TX\_P50

| #define UART0TX\_P50   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(50, 4) |
| --- |

## [◆ ](#a13169414a9db1d2d918fd8a1ac6e328e)UART0TX\_P61

| #define UART0TX\_P61   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(61, 4) |
| --- |

## [◆ ](#a1ae2ba2a91ba842284fd6cbb156def04)UART0TX\_P69

| #define UART0TX\_P69   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(69, 4) |
| --- |

## [◆ ](#af0fd57799f26a1157516475c639e453b)UART0TX\_P7

| #define UART0TX\_P7   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(7, 5) |
| --- |

## [◆ ](#a62f156b398182c31da9377c3f417623f)UART0TX\_P70

| #define UART0TX\_P70   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(70, 4) |
| --- |

## [◆ ](#afee0c790c7e8f4dd235d8489ac5c4107)UART0TX\_P71

| #define UART0TX\_P71   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(71, 4) |
| --- |

## [◆ ](#ae68adb841018f98375b7022e370aba0c)UART0TX\_P72

| #define UART0TX\_P72   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(72, 4) |
| --- |

## [◆ ](#a497320f365bff8a29dcb080c154bdc2b)UART1RX\_P13

| #define UART1RX\_P13   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(13, 7) |
| --- |

## [◆ ](#a077ccd27c6322be3ea942342545ac957)UART1RX\_P15

| #define UART1RX\_P15   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(15, 2) |
| --- |

## [◆ ](#a15b80792320cbe15fd715dbf880bd8a6)UART1RX\_P19

| #define UART1RX\_P19   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(19, 6) |
| --- |

## [◆ ](#a3795e6445756b68c436b6d0fb1c7813b)UART1RX\_P2

| #define UART1RX\_P2   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(2, 0) |
| --- |

## [◆ ](#a883993c1c111a42deb3b227ecd38317c)UART1RX\_P21

| #define UART1RX\_P21   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(21, 5) |
| --- |

## [◆ ](#a986d17fc832de865df075504f12f2749)UART1RX\_P25

| #define UART1RX\_P25   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(25, 0) |
| --- |

## [◆ ](#abe283e2a79b535f5afb8c82ebba32fce)UART1RX\_P36

| #define UART1RX\_P36   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(36, 2) |
| --- |

## [◆ ](#a41cec431ed8db8d5286149552695caaf)UART1RX\_P38

| #define UART1RX\_P38   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(38, 6) |
| --- |

## [◆ ](#a6c0d9abe0eabefce033125e3d1519e56)UART1RX\_P4

| #define UART1RX\_P4   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(4, 5) |
| --- |

## [◆ ](#ab6fb2d741ae9ca9492959e8b04d2ab8c)UART1RX\_P40

| #define UART1RX\_P40   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(40, 1) |
| --- |

## [◆ ](#acd68b66375a1cd525670f9f0b3ea9213)UART1RX\_P43

| #define UART1RX\_P43   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(43, 0) |
| --- |

## [◆ ](#a45c38170a7a3b57c6576ebfa6f52b35c)UART1RX\_P47

| #define UART1RX\_P47   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(47, 6) |
| --- |

## [◆ ](#ae64fb321a2fb963c1f0e1771b6f5f8f0)UART1RX\_P50

| #define UART1RX\_P50   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(50, 7) |
| --- |

## [◆ ](#a8ba999d652f37a9cec7f09ec48bb1efd)UART1RX\_P61

| #define UART1RX\_P61   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(61, 7) |
| --- |

## [◆ ](#a6d3cf67ebe5a1f059fd47110357a7e4e)UART1RX\_P69

| #define UART1RX\_P69   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(69, 7) |
| --- |

## [◆ ](#aad95c312dadb461f7926ab6f01374ed7)UART1RX\_P70

| #define UART1RX\_P70   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(70, 7) |
| --- |

## [◆ ](#a6a2d312670202739632148c973559135)UART1RX\_P71

| #define UART1RX\_P71   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(71, 7) |
| --- |

## [◆ ](#ae0e923c68bbdf2d2a929c34f580f4fd4)UART1RX\_P72

| #define UART1RX\_P72   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(72, 7) |
| --- |

## [◆ ](#a6c829d8791c5ef247418f022d37abe26)UART1RX\_P9

| #define UART1RX\_P9   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(9, 6) |
| --- |

## [◆ ](#abcb9b4ed6c81f79f0d2d3f96c0907489)UART1TX\_P10

| #define UART1TX\_P10   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(10, 0) |
| --- |

## [◆ ](#ae86cb0f42ab5ae4105b89838173e7c4f)UART1TX\_P12

| #define UART1TX\_P12   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(12, 7) |
| --- |

## [◆ ](#a95761d7f9fde43b6e1fe1d25ef9d9717)UART1TX\_P14

| #define UART1TX\_P14   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(14, 2) |
| --- |

## [◆ ](#a7ef056832ac3d027fdc236914194ab9f)UART1TX\_P18

| #define UART1TX\_P18   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(18, 6) |
| --- |

## [◆ ](#a8d38e7930ecd6a6b51e0da8bdf0b5792)UART1TX\_P20

| #define UART1TX\_P20   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(20, 5) |
| --- |

## [◆ ](#a640da7cf413db9c5ad8f8c49b7208539)UART1TX\_P24

| #define UART1TX\_P24   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(24, 0) |
| --- |

## [◆ ](#abfd3f2f30a9a90790dbc58666f8e4ea3)UART1TX\_P35

| #define UART1TX\_P35   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(35, 2) |
| --- |

## [◆ ](#af51f177fc9f7208bcf5815a478d29978)UART1TX\_P37

| #define UART1TX\_P37   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(37, 5) |
| --- |

## [◆ ](#ae99c8956963caaa4d16d5b3f1c1bb9ce)UART1TX\_P39

| #define UART1TX\_P39   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(39, 1) |
| --- |

## [◆ ](#a6705e001463f646a7f26ff4cb316c634)UART1TX\_P42

| #define UART1TX\_P42   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(42, 0) |
| --- |

## [◆ ](#afe121783dfe5a9958c15ae0883b83cfb)UART1TX\_P46

| #define UART1TX\_P46   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(46, 6) |
| --- |

## [◆ ](#a79377784abe4f92663d3fb9bf878921a)UART1TX\_P50

| #define UART1TX\_P50   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(50, 6) |
| --- |

## [◆ ](#a4b046371e9d9717fbc966b890d231dc4)UART1TX\_P61

| #define UART1TX\_P61   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(61, 6) |
| --- |

## [◆ ](#a147d9681b5a8ca2b3cb1a9ed805762fd)UART1TX\_P69

| #define UART1TX\_P69   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(69, 6) |
| --- |

## [◆ ](#a12a07be7ada04c8db5456f26e384c4d5)UART1TX\_P70

| #define UART1TX\_P70   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(70, 6) |
| --- |

## [◆ ](#a75527d755c741c22f55d12e35f5aef13)UART1TX\_P71

| #define UART1TX\_P71   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(71, 6) |
| --- |

## [◆ ](#a315caa38da59dbbea5e94f08194ba614)UART1TX\_P72

| #define UART1TX\_P72   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(72, 6) |
| --- |

## [◆ ](#a9d932772131c6c1cd418e026d27975fc)UART1TX\_P8

| #define UART1TX\_P8   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(8, 6) |
| --- |

## [◆ ](#ad6896d2b4627a39b85ce426e045d55f9)XT32KHz\_P14

| #define XT32KHz\_P14   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(14, 7) |
| --- |

## [◆ ](#aca95921548c6549fa9b40d0584389037)XT32KHz\_P24

| #define XT32KHz\_P24   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(24, 6) |
| --- |

## [◆ ](#a40417407993ffd2e917262ae286e0b8d)XT32KHz\_P33

| #define XT32KHz\_P33   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(33, 2) |
| --- |

## [◆ ](#a48be8de8a03a7a27a7848c64adb97665)XT32KHz\_P36

| #define XT32KHz\_P36   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(36, 4) |
| --- |

## [◆ ](#a55e6549b3ba1beca7ae1db93b7f809ee)XT32KHz\_P47

| #define XT32KHz\_P47   [APOLLO3\_PINMUX](#a2e4e01a3d50c6ced0a21d65877b0cdb2)(47, 0) |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [pinctrl](dir_2c6c4fbd167577104b7f1b7148586168.md)
- [ambiq-apollo3-pinctrl.h](ambiq-apollo3-pinctrl_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
