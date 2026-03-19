---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/ambiq-apollo3-pinctrl_8h_source.html
original_path: doxygen/html/ambiq-apollo3-pinctrl_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ambiq-apollo3-pinctrl.h

[Go to the documentation of this file.](ambiq-apollo3-pinctrl_8h.md)

1/\*

2 \* Copyright (c) 2023 Ambiq Micro Inc. <www.ambiq.com>

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef \_\_APOLLO3\_PINCTRL\_H\_\_

8#define \_\_APOLLO3\_PINCTRL\_H\_\_

9

[ 10](ambiq-apollo3-pinctrl_8h.md#aec76f3cfd2a609e60eabf5628f5ee698)#define APOLLO3\_ALT\_FUNC\_POS 0

[ 11](ambiq-apollo3-pinctrl_8h.md#aa00706366b69ceb3628404acb54d08c3)#define APOLLO3\_ALT\_FUNC\_MASK 0xf

12

[ 13](ambiq-apollo3-pinctrl_8h.md#a31b09dab4803a326db645412cf2d7acd)#define APOLLO3\_PIN\_NUM\_POS 4

[ 14](ambiq-apollo3-pinctrl_8h.md#a71eb3e43677ab0f8c9abd0fc61aafaab)#define APOLLO3\_PIN\_NUM\_MASK 0x7f

15

[ 16](ambiq-apollo3-pinctrl_8h.md#a2e4e01a3d50c6ced0a21d65877b0cdb2)#define APOLLO3\_PINMUX(pin\_num, alt\_func) \

17 (pin\_num << APOLLO3\_PIN\_NUM\_POS | alt\_func << APOLLO3\_ALT\_FUNC\_POS)

18

[ 19](ambiq-apollo3-pinctrl_8h.md#a3a72f1023828af4b3766cc0714c404b2)#define SLSCL\_P0 APOLLO3\_PINMUX(0, 0)

[ 20](ambiq-apollo3-pinctrl_8h.md#ae72cb1519562643c48a8ffff88dc9d00)#define SLSCK\_P0 APOLLO3\_PINMUX(0, 1)

[ 21](ambiq-apollo3-pinctrl_8h.md#a95fca27e19b245305579cbad18962f00)#define CLKOUT\_P0 APOLLO3\_PINMUX(0, 2)

[ 22](ambiq-apollo3-pinctrl_8h.md#ada3eedfe2cf44d8f0f1c21d10fc7c81a)#define GPIO\_P0 APOLLO3\_PINMUX(0, 3)

[ 23](ambiq-apollo3-pinctrl_8h.md#ac619aa033a346a49cd8e1c501831c852)#define MSPI0\_4\_P0 APOLLO3\_PINMUX(0, 5)

[ 24](ambiq-apollo3-pinctrl_8h.md#a2f7a5ec8bae150c5d845a85d65991107)#define NCE0\_P0 APOLLO3\_PINMUX(0, 7)

[ 25](ambiq-apollo3-pinctrl_8h.md#ae5b84a6fa44069d704c6c87113bef6e7)#define SLSDAWIR3\_P1 APOLLO3\_PINMUX(1, 0)

[ 26](ambiq-apollo3-pinctrl_8h.md#a4fd87e65fcf8776a98224ca1d468b0ad)#define SLMOSI\_P1 APOLLO3\_PINMUX(1, 1)

[ 27](ambiq-apollo3-pinctrl_8h.md#aa237cfc2d6eda1c3ddf349b5a3330898)#define UART0TX\_P1 APOLLO3\_PINMUX(1, 2)

[ 28](ambiq-apollo3-pinctrl_8h.md#af7a3fb155e6285875e885d5a6344041d)#define GPIO\_P1 APOLLO3\_PINMUX(1, 3)

[ 29](ambiq-apollo3-pinctrl_8h.md#a75d2d20c972028ad79e046b31df7aaca)#define MSPI0\_5\_P1 APOLLO3\_PINMUX(1, 5)

[ 30](ambiq-apollo3-pinctrl_8h.md#aad38da06e56246b4ed48ddbf43f1aaca)#define NCE1\_P1 APOLLO3\_PINMUX(1, 7)

[ 31](ambiq-apollo3-pinctrl_8h.md#a3795e6445756b68c436b6d0fb1c7813b)#define UART1RX\_P2 APOLLO3\_PINMUX(2, 0)

[ 32](ambiq-apollo3-pinctrl_8h.md#a06beb22570d100e28198606d21909a6c)#define SLMISO\_P2 APOLLO3\_PINMUX(2, 1)

[ 33](ambiq-apollo3-pinctrl_8h.md#aeb4da21d8f3fdb747865ff6b6a7ea49e)#define UART0RX\_P2 APOLLO3\_PINMUX(2, 2)

[ 34](ambiq-apollo3-pinctrl_8h.md#aea5b197be9a863a6db90cb9d42b8a9f2)#define GPIO\_P2 APOLLO3\_PINMUX(2, 3)

[ 35](ambiq-apollo3-pinctrl_8h.md#a112ffcf686debe615f04a1fc3c20ceab)#define MSPI0\_6\_P2 APOLLO3\_PINMUX(2, 5)

[ 36](ambiq-apollo3-pinctrl_8h.md#a41c7834b7cc3a8f2f75021ec9ebedf6a)#define NCE2\_P2 APOLLO3\_PINMUX(2, 7)

[ 37](ambiq-apollo3-pinctrl_8h.md#ae5123e7f8df58cc8ca300bc955a855d3)#define UA0RTS\_P3 APOLLO3\_PINMUX(3, 0)

[ 38](ambiq-apollo3-pinctrl_8h.md#a42fc82a09d814a6774ee02b1b0228cd8)#define SLNCE\_P3 APOLLO3\_PINMUX(3, 1)

[ 39](ambiq-apollo3-pinctrl_8h.md#a49fa96fac299d83fe34b116fc2e8d586)#define NCE3\_P3 APOLLO3\_PINMUX(3, 2)

[ 40](ambiq-apollo3-pinctrl_8h.md#af4024d1ac41ed0426ca701ea851dcd82)#define GPIO\_P3 APOLLO3\_PINMUX(3, 3)

[ 41](ambiq-apollo3-pinctrl_8h.md#a5e93b8d0e2c70144bfaa034aa6dea0d8)#define MSPI0\_7\_P3 APOLLO3\_PINMUX(3, 5)

[ 42](ambiq-apollo3-pinctrl_8h.md#a2afa9eb9453ab24b55280c9680e8bca7)#define TRIG1\_P3 APOLLO3\_PINMUX(3, 6)

[ 43](ambiq-apollo3-pinctrl_8h.md#a2b3c5edbedf68592bfa84e0df9905396)#define I2SWCLK\_P3 APOLLO3\_PINMUX(3, 7)

[ 44](ambiq-apollo3-pinctrl_8h.md#a7c15b0f583db4314e7b315e553e6ec89)#define UA0CTS\_P4 APOLLO3\_PINMUX(4, 0)

[ 45](ambiq-apollo3-pinctrl_8h.md#a29c616828e653cb4f0cecaca1f0bc8f1)#define SLINT\_P4 APOLLO3\_PINMUX(4, 1)

[ 46](ambiq-apollo3-pinctrl_8h.md#a3019076e21641ad28be64b29a4b2c671)#define NCE4\_P4 APOLLO3\_PINMUX(4, 2)

[ 47](ambiq-apollo3-pinctrl_8h.md#aea71dd1d14466cec98ab057ece573f75)#define GPIO\_P4 APOLLO3\_PINMUX(4, 3)

[ 48](ambiq-apollo3-pinctrl_8h.md#a6c0d9abe0eabefce033125e3d1519e56)#define UART1RX\_P4 APOLLO3\_PINMUX(4, 5)

[ 49](ambiq-apollo3-pinctrl_8h.md#ae3a25bc2296db097c9d774e801f146ef)#define CTIM17\_P4 APOLLO3\_PINMUX(4, 6)

[ 50](ambiq-apollo3-pinctrl_8h.md#a6395a199be7a3ef0d69976a41253282d)#define MSPI0\_2\_P4 APOLLO3\_PINMUX(4, 7)

[ 51](ambiq-apollo3-pinctrl_8h.md#a89285a703eabc9b9cc9c962dd7f8856c)#define M0SCL\_P5 APOLLO3\_PINMUX(5, 0)

[ 52](ambiq-apollo3-pinctrl_8h.md#abf59b5c6ff03c8a2652d3bc72b872295)#define M0SCK\_P5 APOLLO3\_PINMUX(5, 1)

[ 53](ambiq-apollo3-pinctrl_8h.md#a9af295a6b30a9ebfa26d89187a765817)#define UA0RTS\_P5 APOLLO3\_PINMUX(5, 2)

[ 54](ambiq-apollo3-pinctrl_8h.md#a8b6393ba023af44294a82048f4d7b7fb)#define GPIO\_P5 APOLLO3\_PINMUX(5, 3)

[ 55](ambiq-apollo3-pinctrl_8h.md#a8427da089d2101bd9fc10ce6f1933aa8)#define CT8\_P5 APOLLO3\_PINMUX(5, 7)

[ 56](ambiq-apollo3-pinctrl_8h.md#a70ecddbefb03c277a58ab1f8c6f4972c)#define M0SDAWIR3\_P6 APOLLO3\_PINMUX(6, 0)

[ 57](ambiq-apollo3-pinctrl_8h.md#a01e0417e4c10476d720baa251bf37f41)#define M0MISO\_P6 APOLLO3\_PINMUX(6, 1)

[ 58](ambiq-apollo3-pinctrl_8h.md#a0ec1a55c1287c1b4524670c836aa3610)#define UA0CTS\_P6 APOLLO3\_PINMUX(6, 2)

[ 59](ambiq-apollo3-pinctrl_8h.md#ab92e5b2728491c7718e22490337a877c)#define GPIO\_P6 APOLLO3\_PINMUX(6, 3)

[ 60](ambiq-apollo3-pinctrl_8h.md#a00a0fc70b33db841fd0551b7c262253e)#define CTIM10\_P6 APOLLO3\_PINMUX(6, 5)

[ 61](ambiq-apollo3-pinctrl_8h.md#ae3de66bb2e7fd0e635de7945543bfb07)#define I2SDAT\_P6 APOLLO3\_PINMUX(6, 7)

[ 62](ambiq-apollo3-pinctrl_8h.md#ac34242faa4992e4acc075a36264d7187)#define NCE7\_P7 APOLLO3\_PINMUX(7, 0)

[ 63](ambiq-apollo3-pinctrl_8h.md#aa8d862944d509743683a67127dfa38bd)#define M0MOSI\_P7 APOLLO3\_PINMUX(7, 1)

[ 64](ambiq-apollo3-pinctrl_8h.md#a44e6475e1fcd9fbb522a48dea35e8599)#define CLKOUT\_P7 APOLLO3\_PINMUX(7, 2)

[ 65](ambiq-apollo3-pinctrl_8h.md#a56c293ec75689c3c233d7a0ad4d7428e)#define GPIO\_P7 APOLLO3\_PINMUX(7, 3)

[ 66](ambiq-apollo3-pinctrl_8h.md#a00614cfc545401d5e8cb9f1e51848571)#define TRIG0\_P7 APOLLO3\_PINMUX(7, 4)

[ 67](ambiq-apollo3-pinctrl_8h.md#af0fd57799f26a1157516475c639e453b)#define UART0TX\_P7 APOLLO3\_PINMUX(7, 5)

[ 68](ambiq-apollo3-pinctrl_8h.md#af38d97658c4bd9cbb45e822331999a0d)#define CTIM19\_P7 APOLLO3\_PINMUX(7, 7)

[ 69](ambiq-apollo3-pinctrl_8h.md#a78f6a3daba1c3af73d6f56e201716c9d)#define M1SCL\_P8 APOLLO3\_PINMUX(8, 0)

[ 70](ambiq-apollo3-pinctrl_8h.md#aeca27870849b7a78edc8fe37b9966f23)#define M1SCK\_P8 APOLLO3\_PINMUX(8, 1)

[ 71](ambiq-apollo3-pinctrl_8h.md#a6c400fdb4e2e68a5a28f2aade3509822)#define NCE8\_P8 APOLLO3\_PINMUX(8, 2)

[ 72](ambiq-apollo3-pinctrl_8h.md#a98e2e72127f9d8302c72d588b005ad43)#define GPIO\_P8 APOLLO3\_PINMUX(8, 3)

[ 73](ambiq-apollo3-pinctrl_8h.md#a656853201d5b7b94a3019767ec187d0c)#define SCCCLK\_P8 APOLLO3\_PINMUX(8, 4)

[ 74](ambiq-apollo3-pinctrl_8h.md#a9d932772131c6c1cd418e026d27975fc)#define UART1TX\_P8 APOLLO3\_PINMUX(8, 6)

[ 75](ambiq-apollo3-pinctrl_8h.md#a8a5ee0496cfaf6fe7c0475459ab7ee23)#define M1SDAWIR3\_P9 APOLLO3\_PINMUX(9, 0)

[ 76](ambiq-apollo3-pinctrl_8h.md#a044f3f8861bdfe85899102c4a51dd663)#define M1MISO\_P9 APOLLO3\_PINMUX(9, 1)

[ 77](ambiq-apollo3-pinctrl_8h.md#aa92d1c97c14770e3e29a271706d76a28)#define NCE9\_P9 APOLLO3\_PINMUX(9, 2)

[ 78](ambiq-apollo3-pinctrl_8h.md#a62ba7982361959a0ff4013c825611344)#define GPIO\_P9 APOLLO3\_PINMUX(9, 3)

[ 79](ambiq-apollo3-pinctrl_8h.md#a0def8b127d3740da2bb3ae2b44d0095c)#define SCCIO\_P9 APOLLO3\_PINMUX(9, 4)

[ 80](ambiq-apollo3-pinctrl_8h.md#a6c829d8791c5ef247418f022d37abe26)#define UART1RX\_P9 APOLLO3\_PINMUX(9, 6)

[ 81](ambiq-apollo3-pinctrl_8h.md#abcb9b4ed6c81f79f0d2d3f96c0907489)#define UART1TX\_P10 APOLLO3\_PINMUX(10, 0)

[ 82](ambiq-apollo3-pinctrl_8h.md#aa99ecc3b8b3e072f245f3779564d9b35)#define M1MOSI\_P10 APOLLO3\_PINMUX(10, 1)

[ 83](ambiq-apollo3-pinctrl_8h.md#aad947baa0652e59cb21735eae01eca09)#define NCE10\_P10 APOLLO3\_PINMUX(10, 2)

[ 84](ambiq-apollo3-pinctrl_8h.md#aeae1f6c04e5fc3c420c3c2311e91c0fb)#define GPIO\_P10 APOLLO3\_PINMUX(10, 3)

[ 85](ambiq-apollo3-pinctrl_8h.md#a432af451cbdf1a8e0137e61def76d525)#define PDMCLK\_P10 APOLLO3\_PINMUX(10, 4)

[ 86](ambiq-apollo3-pinctrl_8h.md#ab98a61028f7a8b5e45841dc3d5ab0672)#define UA1RTS\_P10 APOLLO3\_PINMUX(10, 6)

[ 87](ambiq-apollo3-pinctrl_8h.md#a0af7147f664fc0c56acdfc63e76558bc)#define ADCSE2\_P11 APOLLO3\_PINMUX(11, 0)

[ 88](ambiq-apollo3-pinctrl_8h.md#ab635978b874de8fbe6f96506b06ae5f1)#define NCE11\_P11 APOLLO3\_PINMUX(11, 1)

[ 89](ambiq-apollo3-pinctrl_8h.md#a994df6ba3173398db50c15364d07ede5)#define CTIM31\_P11 APOLLO3\_PINMUX(11, 2)

[ 90](ambiq-apollo3-pinctrl_8h.md#a1e2a5bd418526ffe665b93088178edc3)#define GPIO\_P11 APOLLO3\_PINMUX(11, 3)

[ 91](ambiq-apollo3-pinctrl_8h.md#acab95c4dfc69402cb93aa80cb368a8ed)#define SLINT\_P11 APOLLO3\_PINMUX(11, 4)

[ 92](ambiq-apollo3-pinctrl_8h.md#a0c85b60521c7052487e84b4eb1031be1)#define UA1CTS\_P11 APOLLO3\_PINMUX(11, 5)

[ 93](ambiq-apollo3-pinctrl_8h.md#aff7e0941ffab586464b6a42edf32cf84)#define UART0RX\_P11 APOLLO3\_PINMUX(11, 6)

[ 94](ambiq-apollo3-pinctrl_8h.md#a4a9e07c73a2062220944fac15bc9976c)#define PDMDATA\_P11 APOLLO3\_PINMUX(11, 7)

[ 95](ambiq-apollo3-pinctrl_8h.md#a994b602fed3f5de352a97b9cc9c62607)#define ADCD0NSE9\_P12 APOLLO3\_PINMUX(12, 0)

[ 96](ambiq-apollo3-pinctrl_8h.md#aeeea37f1af4c943883760c8e273f26a1)#define NCE12\_P12 APOLLO3\_PINMUX(12, 1)

[ 97](ambiq-apollo3-pinctrl_8h.md#a9b2a8b0d84975b39cc2fdfb3b3f5c2c0)#define CT0\_P12 APOLLO3\_PINMUX(12, 2)

[ 98](ambiq-apollo3-pinctrl_8h.md#a2b368e24e962e0bdb34a68dc81a9e929)#define GPIO\_P12 APOLLO3\_PINMUX(12, 3)

[ 99](ambiq-apollo3-pinctrl_8h.md#a839ddc0937ffa9b306f491f263ac5ede)#define PDMCLK\_P12 APOLLO3\_PINMUX(12, 5)

[ 100](ambiq-apollo3-pinctrl_8h.md#ab5ce9319d6fc8bdb1496be5f2f015358)#define UA0CTS\_P12 APOLLO3\_PINMUX(12, 6)

[ 101](ambiq-apollo3-pinctrl_8h.md#ae86cb0f42ab5ae4105b89838173e7c4f)#define UART1TX\_P12 APOLLO3\_PINMUX(12, 7)

[ 102](ambiq-apollo3-pinctrl_8h.md#a5c9489a135b6531852d4ebdfc5154f22)#define ADCD0PSE8\_P13 APOLLO3\_PINMUX(13, 0)

[ 103](ambiq-apollo3-pinctrl_8h.md#a03383f0fcb11b35cac08703aa51cdb56)#define NCE13\_P13 APOLLO3\_PINMUX(13, 1)

[ 104](ambiq-apollo3-pinctrl_8h.md#a0299d3d82238065f28ea9d60e28e56a0)#define CTIM2\_P13 APOLLO3\_PINMUX(13, 2)

[ 105](ambiq-apollo3-pinctrl_8h.md#a9519265fbdd9fb2adfe818baa0ef933f)#define GPIO\_P13 APOLLO3\_PINMUX(13, 3)

[ 106](ambiq-apollo3-pinctrl_8h.md#a9a93f8cb9a71278914a878651ab787c6)#define I2SBCLK\_P13 APOLLO3\_PINMUX(13, 4)

[ 107](ambiq-apollo3-pinctrl_8h.md#accb8206aa72638560dfb39d1225d21c3)#define UA0RTS\_P13 APOLLO3\_PINMUX(13, 6)

[ 108](ambiq-apollo3-pinctrl_8h.md#a497320f365bff8a29dcb080c154bdc2b)#define UART1RX\_P13 APOLLO3\_PINMUX(13, 7)

[ 109](ambiq-apollo3-pinctrl_8h.md#a116b6aa61f2ad957c6e205c73b447a1e)#define ADCD1P\_P14 APOLLO3\_PINMUX(14, 0)

[ 110](ambiq-apollo3-pinctrl_8h.md#a39f9f5d31b34dd21c12439c0a9fd032f)#define NCE14\_P14 APOLLO3\_PINMUX(14, 1)

[ 111](ambiq-apollo3-pinctrl_8h.md#a95761d7f9fde43b6e1fe1d25ef9d9717)#define UART1TX\_P14 APOLLO3\_PINMUX(14, 2)

[ 112](ambiq-apollo3-pinctrl_8h.md#af24f89fe6d38c0db5d7f774e07228678)#define GPIO\_P14 APOLLO3\_PINMUX(14, 3)

[ 113](ambiq-apollo3-pinctrl_8h.md#aacd23325f76bea9db0c004775953572d)#define PDMCLK\_P14 APOLLO3\_PINMUX(14, 4)

[ 114](ambiq-apollo3-pinctrl_8h.md#af6db4faf2bc7ec69d646e556f3475c6b)#define SWDCK\_P14 APOLLO3\_PINMUX(14, 6)

[ 115](ambiq-apollo3-pinctrl_8h.md#ad6896d2b4627a39b85ce426e045d55f9)#define XT32KHz\_P14 APOLLO3\_PINMUX(14, 7)

[ 116](ambiq-apollo3-pinctrl_8h.md#ad4979ef8e737edc9304425cbff550802)#define ADCD1N\_P15 APOLLO3\_PINMUX(15, 0)

[ 117](ambiq-apollo3-pinctrl_8h.md#ab6136185e31fbbb173391d77723de46a)#define NCE15\_P15 APOLLO3\_PINMUX(15, 1)

[ 118](ambiq-apollo3-pinctrl_8h.md#a077ccd27c6322be3ea942342545ac957)#define UART1RX\_P15 APOLLO3\_PINMUX(15, 2)

[ 119](ambiq-apollo3-pinctrl_8h.md#a9147a6e2b351214ab5fe7e5d4f6355d7)#define GPIO\_P15 APOLLO3\_PINMUX(15, 3)

[ 120](ambiq-apollo3-pinctrl_8h.md#ae98b714215455ad42b61c940d47a5658)#define PDMDATA\_P15 APOLLO3\_PINMUX(15, 4)

[ 121](ambiq-apollo3-pinctrl_8h.md#ac7018578ab5232a026d00f93005cd1d2)#define SWDIO\_P15 APOLLO3\_PINMUX(15, 6)

[ 122](ambiq-apollo3-pinctrl_8h.md#a335a3b83d4115419e3f752ba6cc6c3c2)#define SWO\_P15 APOLLO3\_PINMUX(15, 7)

[ 123](ambiq-apollo3-pinctrl_8h.md#add33549cde84fd881439b438becb5e33)#define ADCSE0\_P16 APOLLO3\_PINMUX(16, 0)

[ 124](ambiq-apollo3-pinctrl_8h.md#a5da8200119b0e8a2e6fec1097896edd1)#define NCE16\_P16 APOLLO3\_PINMUX(16, 1)

[ 125](ambiq-apollo3-pinctrl_8h.md#a7fb00b38e52d1115ce542b0f00b80ac7)#define TRIG0\_P16 APOLLO3\_PINMUX(16, 2)

[ 126](ambiq-apollo3-pinctrl_8h.md#a9c21bf7bc952df6b78d19f89f3638833)#define GPIO\_P16 APOLLO3\_PINMUX(16, 3)

[ 127](ambiq-apollo3-pinctrl_8h.md#a8e59ac2cee69f18f8c23e71e34779d5f)#define SCCRST\_P16 APOLLO3\_PINMUX(16, 4)

[ 128](ambiq-apollo3-pinctrl_8h.md#a9c9cee6bc621a36d67af82a83ce108b9)#define CMPIN0\_P16 APOLLO3\_PINMUX(16, 5)

[ 129](ambiq-apollo3-pinctrl_8h.md#a26f7e4ec8471988685bab0fa0f666af7)#define UART0TX\_P16 APOLLO3\_PINMUX(16, 6)

[ 130](ambiq-apollo3-pinctrl_8h.md#a5f8c363f21f1a089c1d560a9b975ac41)#define UA1RTS\_P16 APOLLO3\_PINMUX(16, 7)

[ 131](ambiq-apollo3-pinctrl_8h.md#a1269137afa8563480745e3fdf730580b)#define CMPRF1\_P17 APOLLO3\_PINMUX(17, 0)

[ 132](ambiq-apollo3-pinctrl_8h.md#ab89d7eb6aa6e611a3a95cc1ee913731c)#define NCE17\_P17 APOLLO3\_PINMUX(17, 1)

[ 133](ambiq-apollo3-pinctrl_8h.md#a3c59efbb8cf2245b113f8d4a5119b7c6)#define TRIG1\_P17 APOLLO3\_PINMUX(17, 2)

[ 134](ambiq-apollo3-pinctrl_8h.md#a6a5de6dce7def318bec4f73dd614ec22)#define GPIO\_P17 APOLLO3\_PINMUX(17, 3)

[ 135](ambiq-apollo3-pinctrl_8h.md#a532591d82e99327eec3d5ecaf71fd234)#define SCCCLK\_P17 APOLLO3\_PINMUX(17, 4)

[ 136](ambiq-apollo3-pinctrl_8h.md#a67731a70bfa50b5a9ac8ff30e1343fba)#define UART0RX\_P17 APOLLO3\_PINMUX(17, 6)

[ 137](ambiq-apollo3-pinctrl_8h.md#a199a40fbe31c452461f0ba88e2dfc559)#define UA1CTS\_P17 APOLLO3\_PINMUX(17, 7)

[ 138](ambiq-apollo3-pinctrl_8h.md#a7cd80fe3c550eaeb4430512efcc2a296)#define CMPIN1\_P18 APOLLO3\_PINMUX(18, 0)

[ 139](ambiq-apollo3-pinctrl_8h.md#a566a450bf9afa441315c83bf4d0ce580)#define NCE18\_P18 APOLLO3\_PINMUX(18, 1)

[ 140](ambiq-apollo3-pinctrl_8h.md#a2255e19add36a65e7f37d7747afbc28b)#define CTIM4\_P18 APOLLO3\_PINMUX(18, 2)

[ 141](ambiq-apollo3-pinctrl_8h.md#a8b325ebb0010179509a1a32450ea72af)#define GPIO\_P18 APOLLO3\_PINMUX(18, 3)

[ 142](ambiq-apollo3-pinctrl_8h.md#a4c2b318d489aa88d6da183c55d3dbfcf)#define UA0RTS\_P18 APOLLO3\_PINMUX(18, 4)

[ 143](ambiq-apollo3-pinctrl_8h.md#a7ef056832ac3d027fdc236914194ab9f)#define UART1TX\_P18 APOLLO3\_PINMUX(18, 6)

[ 144](ambiq-apollo3-pinctrl_8h.md#a3c89b132043f8dabd531955c7f3b67a5)#define SCCIO\_P18 APOLLO3\_PINMUX(18, 7)

[ 145](ambiq-apollo3-pinctrl_8h.md#a11c7be341b9acbe096a9966044dae194)#define CMPRF0\_P19 APOLLO3\_PINMUX(19, 0)

[ 146](ambiq-apollo3-pinctrl_8h.md#af9d50128143543f345b8db2d2e3e0918)#define NCE19\_P19 APOLLO3\_PINMUX(19, 1)

[ 147](ambiq-apollo3-pinctrl_8h.md#a7bebc4982a8d3d917996bdc1348c8b1f)#define CTIM6\_P19 APOLLO3\_PINMUX(19, 2)

[ 148](ambiq-apollo3-pinctrl_8h.md#afcadccc574cc0d3c7820ba6b0511612e)#define GPIO\_P19 APOLLO3\_PINMUX(19, 3)

[ 149](ambiq-apollo3-pinctrl_8h.md#a5e41d1a7b81ac2349f2b6dece08850a4)#define SCCCLK\_P19 APOLLO3\_PINMUX(19, 4)

[ 150](ambiq-apollo3-pinctrl_8h.md#a15b80792320cbe15fd715dbf880bd8a6)#define UART1RX\_P19 APOLLO3\_PINMUX(19, 6)

[ 151](ambiq-apollo3-pinctrl_8h.md#ad189a78fbe82f542553e26fe7f06c8b8)#define I2SBCLK\_P19 APOLLO3\_PINMUX(19, 7)

[ 152](ambiq-apollo3-pinctrl_8h.md#a3885c97e098dfed018491c67065e696c)#define SWDCK\_P20 APOLLO3\_PINMUX(20, 0)

[ 153](ambiq-apollo3-pinctrl_8h.md#a8c4f0230a390d43b9a408ec438b5dbe6)#define NCE20\_P20 APOLLO3\_PINMUX(20, 1)

[ 154](ambiq-apollo3-pinctrl_8h.md#afcd63445d3ccf972c95c365f95e30039)#define GPIO\_P20 APOLLO3\_PINMUX(20, 3)

[ 155](ambiq-apollo3-pinctrl_8h.md#af9acded122c3567a0f7fae29561351e5)#define UART0TX\_P20 APOLLO3\_PINMUX(20, 4)

[ 156](ambiq-apollo3-pinctrl_8h.md#a8d38e7930ecd6a6b51e0da8bdf0b5792)#define UART1TX\_P20 APOLLO3\_PINMUX(20, 5)

[ 157](ambiq-apollo3-pinctrl_8h.md#aa16dc261b7d94bbb13919e779208beb1)#define I2SBCLK\_P20 APOLLO3\_PINMUX(20, 6)

[ 158](ambiq-apollo3-pinctrl_8h.md#a01a5858ec4972916023b83541ea9a17e)#define UA1RTS\_P20 APOLLO3\_PINMUX(20, 7)

[ 159](ambiq-apollo3-pinctrl_8h.md#a184cab7037772c8ca8ecc296ea9c7e48)#define SWDIO\_P21 APOLLO3\_PINMUX(21, 0)

[ 160](ambiq-apollo3-pinctrl_8h.md#a3a7292f75cecf7ac798212bbfef2ff3a)#define NCE21\_P21 APOLLO3\_PINMUX(21, 1)

[ 161](ambiq-apollo3-pinctrl_8h.md#a03d53f3d221401ff02a702ef2c8e05c1)#define GPIO\_P21 APOLLO3\_PINMUX(21, 3)

[ 162](ambiq-apollo3-pinctrl_8h.md#ae642493fcee53d0fe7a2af91e1cac307)#define UART0RX\_P21 APOLLO3\_PINMUX(21, 4)

[ 163](ambiq-apollo3-pinctrl_8h.md#a883993c1c111a42deb3b227ecd38317c)#define UART1RX\_P21 APOLLO3\_PINMUX(21, 5)

[ 164](ambiq-apollo3-pinctrl_8h.md#a8de11c1add0069e7af62e5bbc3b55dbd)#define SCCRST\_P21 APOLLO3\_PINMUX(21, 6)

[ 165](ambiq-apollo3-pinctrl_8h.md#a8149767283ba99d3fbf7c73ca017a565)#define UA1CTS\_P21 APOLLO3\_PINMUX(21, 7)

[ 166](ambiq-apollo3-pinctrl_8h.md#ad7370389dba6304d21d5f95d57dca5dc)#define UART0TX\_P22 APOLLO3\_PINMUX(22, 0)

[ 167](ambiq-apollo3-pinctrl_8h.md#a775bbd5124031418e8f5b723e99ac9ab)#define NCE22\_P22 APOLLO3\_PINMUX(22, 1)

[ 168](ambiq-apollo3-pinctrl_8h.md#ab83b616320654dd99bb1b137f2fc07be)#define CTIM12\_P22 APOLLO3\_PINMUX(22, 2)

[ 169](ambiq-apollo3-pinctrl_8h.md#ad0b28de3a514755dfa6b00fe82579f3d)#define GPIO\_P22 APOLLO3\_PINMUX(22, 3)

[ 170](ambiq-apollo3-pinctrl_8h.md#ad1b1036bf8cb0807af04662b1c6a9f8f)#define PDMCLK\_P22 APOLLO3\_PINMUX(22, 4)

[ 171](ambiq-apollo3-pinctrl_8h.md#a48cbb6097909f658d824a0267cddb6c6)#define MSPI0\_0\_P22 APOLLO3\_PINMUX(22, 6)

[ 172](ambiq-apollo3-pinctrl_8h.md#af2e7742c9a96fe5ac1a2de402bd5f72f)#define SWO\_P22 APOLLO3\_PINMUX(22, 7)

[ 173](ambiq-apollo3-pinctrl_8h.md#aee79208585ea908eac11cadf34078045)#define UART0RX\_P23 APOLLO3\_PINMUX(23, 0)

[ 174](ambiq-apollo3-pinctrl_8h.md#a0a52f7e779022ce90fe4d7ce7b200f6d)#define NCE23\_P23 APOLLO3\_PINMUX(23, 1)

[ 175](ambiq-apollo3-pinctrl_8h.md#a884a5c14156ff1f62b63f70aaf55a380)#define CTIM14\_P23 APOLLO3\_PINMUX(23, 2)

[ 176](ambiq-apollo3-pinctrl_8h.md#a8742762c7c46596977c17898e55f7df0)#define GPIO\_P23 APOLLO3\_PINMUX(23, 3)

[ 177](ambiq-apollo3-pinctrl_8h.md#a038809d35e405118dcd792db6cfd078c)#define I2SWCLK\_P23 APOLLO3\_PINMUX(23, 4)

[ 178](ambiq-apollo3-pinctrl_8h.md#a2f0b3b3267958512978997e66001a86b)#define CMPOUT\_P23 APOLLO3\_PINMUX(23, 5)

[ 179](ambiq-apollo3-pinctrl_8h.md#a1adc0116ed82c440f4fe64116a021917)#define MSPI0\_3\_P23 APOLLO3\_PINMUX(23, 6)

[ 180](ambiq-apollo3-pinctrl_8h.md#a640da7cf413db9c5ad8f8c49b7208539)#define UART1TX\_P24 APOLLO3\_PINMUX(24, 0)

[ 181](ambiq-apollo3-pinctrl_8h.md#aef5c8fe782ba1f615e0ea35d44a942ce)#define NCE24\_P24 APOLLO3\_PINMUX(24, 1)

[ 182](ambiq-apollo3-pinctrl_8h.md#ab9a27639f83bfc5f2851ad34abad3efe)#define MSPI0\_8\_P24 APOLLO3\_PINMUX(24, 2)

[ 183](ambiq-apollo3-pinctrl_8h.md#a38b0fad90fac621ae3056e0890e5db18)#define GPIO\_P24 APOLLO3\_PINMUX(24, 3)

[ 184](ambiq-apollo3-pinctrl_8h.md#a2f9bcf5acd23826869291e4ae956ee91)#define UA0CTS\_P24 APOLLO3\_PINMUX(24, 4)

[ 185](ambiq-apollo3-pinctrl_8h.md#a5e3b689232d21c05e42043c61f6e7445)#define CTIM21\_P24 APOLLO3\_PINMUX(24, 5)

[ 186](ambiq-apollo3-pinctrl_8h.md#aca95921548c6549fa9b40d0584389037)#define XT32KHz\_P24 APOLLO3\_PINMUX(24, 6)

[ 187](ambiq-apollo3-pinctrl_8h.md#acc4f37955d3cc5567dddb283275cd791)#define SWO\_P24 APOLLO3\_PINMUX(24, 7)

[ 188](ambiq-apollo3-pinctrl_8h.md#a986d17fc832de865df075504f12f2749)#define UART1RX\_P25 APOLLO3\_PINMUX(25, 0)

[ 189](ambiq-apollo3-pinctrl_8h.md#a6c08788db3454db63bc8e5bca88b61a1)#define NCE25\_P25 APOLLO3\_PINMUX(25, 1)

[ 190](ambiq-apollo3-pinctrl_8h.md#ad871e333e8d90dccce7c7c874da74da2)#define CTIM1\_P25 APOLLO3\_PINMUX(25, 2)

[ 191](ambiq-apollo3-pinctrl_8h.md#a70eeb3da2737dc1f88ef0d6b033ba31b)#define GPIO\_P25 APOLLO3\_PINMUX(25, 3)

[ 192](ambiq-apollo3-pinctrl_8h.md#aae0817f4cc4c65301171000cb7c0eb88)#define M2SDAWIR3\_P25 APOLLO3\_PINMUX(25, 4)

[ 193](ambiq-apollo3-pinctrl_8h.md#a0c695ae4458de77501c1ba4c1a13191b)#define M2MISO\_P25 APOLLO3\_PINMUX(25, 5)

[ 194](ambiq-apollo3-pinctrl_8h.md#a498a5dcaa37b5a972e8eea27c29617ef)#define NCE26\_P26 APOLLO3\_PINMUX(26, 1)

[ 195](ambiq-apollo3-pinctrl_8h.md#a631c65202c1c83b33c67e105516550f1)#define CTIM3\_P26 APOLLO3\_PINMUX(26, 2)

[ 196](ambiq-apollo3-pinctrl_8h.md#a70cc23730a6021ba52d4b46466bf7ec8)#define GPIO\_P26 APOLLO3\_PINMUX(26, 3)

[ 197](ambiq-apollo3-pinctrl_8h.md#a645b6c6e3f318aa5ac4fa619a835cd59)#define SCCRST\_P26 APOLLO3\_PINMUX(26, 4)

[ 198](ambiq-apollo3-pinctrl_8h.md#a9c61cc82c741aa4023a607fbe8fa89c7)#define MSPI0\_1\_P26 APOLLO3\_PINMUX(26, 5)

[ 199](ambiq-apollo3-pinctrl_8h.md#a0a5809f404cde8111cfdfa67b5975607)#define UART0TX\_P26 APOLLO3\_PINMUX(26, 6)

[ 200](ambiq-apollo3-pinctrl_8h.md#ab57497d2c1a2802d788f940456afc86d)#define UA1CTS\_P26 APOLLO3\_PINMUX(26, 7)

[ 201](ambiq-apollo3-pinctrl_8h.md#ac18a31df22a6076cd39c0f34e82794a0)#define UART0RX\_P27 APOLLO3\_PINMUX(27, 0)

[ 202](ambiq-apollo3-pinctrl_8h.md#a4b0b9c08da925a4a55bf9cd8342e275d)#define NCE27\_P27 APOLLO3\_PINMUX(27, 1)

[ 203](ambiq-apollo3-pinctrl_8h.md#a254e70755e2142d57322a9e19e972f01)#define CTIM5\_P27 APOLLO3\_PINMUX(27, 2)

[ 204](ambiq-apollo3-pinctrl_8h.md#a9e3eb9ba4f0604f735fc0da2298dc150)#define GPIO\_P27 APOLLO3\_PINMUX(27, 3)

[ 205](ambiq-apollo3-pinctrl_8h.md#ad82dc28ee23bdcc6bcdd3761bb359ab7)#define M2SCL\_P27 APOLLO3\_PINMUX(27, 4)

[ 206](ambiq-apollo3-pinctrl_8h.md#a371cb048e98d35cab6196193d0c00d4e)#define M2SCK\_P27 APOLLO3\_PINMUX(27, 5)

[ 207](ambiq-apollo3-pinctrl_8h.md#a97a46946f5659dfae1a97dfe56832719)#define I2SWCLK\_P28 APOLLO3\_PINMUX(28, 0)

[ 208](ambiq-apollo3-pinctrl_8h.md#ac975e39671e4884de16995b831c3bc52)#define NCE28\_P28 APOLLO3\_PINMUX(28, 1)

[ 209](ambiq-apollo3-pinctrl_8h.md#af89b558743b480da082df15fd2bcecd3)#define CTIM7\_P28 APOLLO3\_PINMUX(28, 2)

[ 210](ambiq-apollo3-pinctrl_8h.md#a6f6f8847e0069b5fefc4a6a54851c99b)#define GPIO\_P28 APOLLO3\_PINMUX(28, 3)

[ 211](ambiq-apollo3-pinctrl_8h.md#aad8910b77ff0ffc62ce7b15f49da3bac)#define M2MOSI\_P28 APOLLO3\_PINMUX(28, 5)

[ 212](ambiq-apollo3-pinctrl_8h.md#a351989945b5403624c7d4fa53a44ab86)#define UART0TX\_P28 APOLLO3\_PINMUX(28, 6)

[ 213](ambiq-apollo3-pinctrl_8h.md#aa3f68e46605f8425448a99ba37eadcb9)#define ADCSE1\_P29 APOLLO3\_PINMUX(29, 0)

[ 214](ambiq-apollo3-pinctrl_8h.md#ac7c4f18c7b072968ce9048bb9057356c)#define NCE29\_P29 APOLLO3\_PINMUX(29, 1)

[ 215](ambiq-apollo3-pinctrl_8h.md#a21f4d326b3928de4948b4d2dc41c3368)#define CTIM9\_P29 APOLLO3\_PINMUX(29, 2)

[ 216](ambiq-apollo3-pinctrl_8h.md#a0c8d4306be59368e181736d98c9d6b4b)#define GPIO\_P29 APOLLO3\_PINMUX(29, 3)

[ 217](ambiq-apollo3-pinctrl_8h.md#ae0f8b8eac04505e31e3a54101a6d7cfa)#define UA0CTS\_P29 APOLLO3\_PINMUX(29, 4)

[ 218](ambiq-apollo3-pinctrl_8h.md#a9072e7364c227042f9232c48b6b6b9c2)#define UA1CTS\_P29 APOLLO3\_PINMUX(29, 5)

[ 219](ambiq-apollo3-pinctrl_8h.md#a97be8cedd244e53e809d38cdeb4933c3)#define UART0RX\_P29 APOLLO3\_PINMUX(29, 6)

[ 220](ambiq-apollo3-pinctrl_8h.md#a7447bed11900ad2fc0c1fdec80c633f5)#define PDMDATA\_P29 APOLLO3\_PINMUX(29, 7)

[ 221](ambiq-apollo3-pinctrl_8h.md#a6d9a17fecc9e2687ede485e719c5e616)#define NCE30\_P30 APOLLO3\_PINMUX(30, 1)

[ 222](ambiq-apollo3-pinctrl_8h.md#af85f87414b52aa3573a268d527d25d92)#define CTIM11\_P30 APOLLO3\_PINMUX(30, 2)

[ 223](ambiq-apollo3-pinctrl_8h.md#a96753b0a1e5a99e644c3bf21aee043b9)#define GPIO\_P30 APOLLO3\_PINMUX(30, 3)

[ 224](ambiq-apollo3-pinctrl_8h.md#aa507368219464308827240872d0eab11)#define UART0TX\_P30 APOLLO3\_PINMUX(30, 4)

[ 225](ambiq-apollo3-pinctrl_8h.md#a0d65684ea5cbc9fd0e75f1f849117a27)#define UA1RTS\_P30 APOLLO3\_PINMUX(30, 5)

[ 226](ambiq-apollo3-pinctrl_8h.md#ac4b587d22482a3b110431d4a6644c696)#define BLEIF\_SCK\_P30 APOLLO3\_PINMUX(30, 6)

[ 227](ambiq-apollo3-pinctrl_8h.md#a4eabbfc370ca2db0afd7ceb14769ba21)#define I2SDAT\_P30 APOLLO3\_PINMUX(30, 7)

[ 228](ambiq-apollo3-pinctrl_8h.md#a6e98f43cdc78b15346036a660fa28e5c)#define ADCSE3\_P31 APOLLO3\_PINMUX(31, 0)

[ 229](ambiq-apollo3-pinctrl_8h.md#aa1001078fb5a05925a8b02e6ecca70c5)#define NCE31\_P31 APOLLO3\_PINMUX(31, 1)

[ 230](ambiq-apollo3-pinctrl_8h.md#acb9e32510b851f3aebd23decaf2264a7)#define CTIM13\_P31 APOLLO3\_PINMUX(31, 2)

[ 231](ambiq-apollo3-pinctrl_8h.md#a2d700f518a2e57f3741c50e0403c471a)#define GPIO\_P31 APOLLO3\_PINMUX(31, 3)

[ 232](ambiq-apollo3-pinctrl_8h.md#a7e23355beb26a376895e08aac26dea57)#define UART0RX\_P31 APOLLO3\_PINMUX(31, 4)

[ 233](ambiq-apollo3-pinctrl_8h.md#a6cd0038a5d5bfa4008eae6666323e3a2)#define SCCCLK\_P31 APOLLO3\_PINMUX(31, 5)

[ 234](ambiq-apollo3-pinctrl_8h.md#a3514181206232492ae6962e386509638)#define BLEIF\_MISO\_P31 APOLLO3\_PINMUX(31, 6)

[ 235](ambiq-apollo3-pinctrl_8h.md#ad7a6b728d49d7ae25431e80cf56aab1b)#define UA1RTS\_P31 APOLLO3\_PINMUX(31, 7)

[ 236](ambiq-apollo3-pinctrl_8h.md#a3a527375ccd62e5f8a761f1942adbcc8)#define ADCSE4\_P32 APOLLO3\_PINMUX(32, 0)

[ 237](ambiq-apollo3-pinctrl_8h.md#afb0f804646a6e3557dd4341eb7d72a74)#define NCE32\_P32 APOLLO3\_PINMUX(32, 1)

[ 238](ambiq-apollo3-pinctrl_8h.md#acb4d0ec1f842052abd81149b33e8b087)#define CTIM15\_P32 APOLLO3\_PINMUX(32, 2)

[ 239](ambiq-apollo3-pinctrl_8h.md#a2a97e46858bf930945c2e03effcc035e)#define GPIO\_P32 APOLLO3\_PINMUX(32, 3)

[ 240](ambiq-apollo3-pinctrl_8h.md#a0562630e3ed7a89a28ea8e9d877a25b5)#define SCCIO\_P32 APOLLO3\_PINMUX(32, 4)

[ 241](ambiq-apollo3-pinctrl_8h.md#a944132c6051ac94d56bc0124c24fff9d)#define BLEIF\_MOSI\_P32 APOLLO3\_PINMUX(32, 6)

[ 242](ambiq-apollo3-pinctrl_8h.md#a6d5db72517c101eea3a3aca07b716869)#define UA1CTS\_P32 APOLLO3\_PINMUX(32, 7)

[ 243](ambiq-apollo3-pinctrl_8h.md#ac774e90f430510b182a016ba09661ed0)#define ADCSE5\_P33 APOLLO3\_PINMUX(33, 0)

[ 244](ambiq-apollo3-pinctrl_8h.md#aa91f920fb637bf393393bac80a9e49ba)#define NCE33\_P33 APOLLO3\_PINMUX(33, 1)

[ 245](ambiq-apollo3-pinctrl_8h.md#a40417407993ffd2e917262ae286e0b8d)#define XT32KHz\_P33 APOLLO3\_PINMUX(33, 2)

[ 246](ambiq-apollo3-pinctrl_8h.md#aa9c2e434db6bed47b117a0764e28889e)#define GPIO\_P33 APOLLO3\_PINMUX(33, 3)

[ 247](ambiq-apollo3-pinctrl_8h.md#a00ad9846bf598e2cec9752afa48417da)#define BLEIF\_CSN\_P33 APOLLO3\_PINMUX(33, 4)

[ 248](ambiq-apollo3-pinctrl_8h.md#a5f64c8ebf5a704ad48dbf12ce595f504)#define UA0CTS\_P33 APOLLO3\_PINMUX(33, 5)

[ 249](ambiq-apollo3-pinctrl_8h.md#a4f4778e38e9719f89985ac4cdf98f344)#define CTIM23\_P33 APOLLO3\_PINMUX(33, 6)

[ 250](ambiq-apollo3-pinctrl_8h.md#ae998e2b505d3b112532b1b58fd298d01)#define SWO\_P33 APOLLO3\_PINMUX(33, 7)

[ 251](ambiq-apollo3-pinctrl_8h.md#a5ee25464af430f33bcb61e9ae711d9a3)#define ADCSE6\_P34 APOLLO3\_PINMUX(34, 0)

[ 252](ambiq-apollo3-pinctrl_8h.md#a4f042898a506cccce60699375b16bf85)#define NCE34\_P34 APOLLO3\_PINMUX(34, 1)

[ 253](ambiq-apollo3-pinctrl_8h.md#a6a490d5a195593605844d2883373ab33)#define UA1RTS\_P34 APOLLO3\_PINMUX(34, 2)

[ 254](ambiq-apollo3-pinctrl_8h.md#a0b5e8a841aa9e129351ec258cd5849f2)#define GPIO\_P34 APOLLO3\_PINMUX(34, 3)

[ 255](ambiq-apollo3-pinctrl_8h.md#a1a9ea33ae1493df327e34a7480e04141)#define CMPRF2\_P34 APOLLO3\_PINMUX(34, 4)

[ 256](ambiq-apollo3-pinctrl_8h.md#af821710452cee65f18e7d9d21f16be5e)#define UA0RTS\_P34 APOLLO3\_PINMUX(34, 5)

[ 257](ambiq-apollo3-pinctrl_8h.md#ae54604f59f12de3bd10dc115e256b69a)#define UART0RX\_P34 APOLLO3\_PINMUX(34, 6)

[ 258](ambiq-apollo3-pinctrl_8h.md#a3288f0cd1140d15ca20840fffe78daaa)#define PDMDATA\_P34 APOLLO3\_PINMUX(34, 7)

[ 259](ambiq-apollo3-pinctrl_8h.md#ae609e68dba89b9c84fc3e6a4a3e29e67)#define ADCSE7\_P35 APOLLO3\_PINMUX(35, 0)

[ 260](ambiq-apollo3-pinctrl_8h.md#ad2cdd6497fb562ea4738beb637e044d1)#define NCE35\_P35 APOLLO3\_PINMUX(35, 1)

[ 261](ambiq-apollo3-pinctrl_8h.md#abfd3f2f30a9a90790dbc58666f8e4ea3)#define UART1TX\_P35 APOLLO3\_PINMUX(35, 2)

[ 262](ambiq-apollo3-pinctrl_8h.md#a26e70a3f976c854799b2451f085ca761)#define GPIO\_P35 APOLLO3\_PINMUX(35, 3)

[ 263](ambiq-apollo3-pinctrl_8h.md#a5f25fda5e336dcdd5d97a0cf9778ee53)#define I2SDAT\_P35 APOLLO3\_PINMUX(35, 4)

[ 264](ambiq-apollo3-pinctrl_8h.md#a3f69161303bc2a76473db22a109aa651)#define CTIM27\_P35 APOLLO3\_PINMUX(35, 5)

[ 265](ambiq-apollo3-pinctrl_8h.md#a5b92e6ee90a413909f63c838283f7777)#define UA0RTS\_P35 APOLLO3\_PINMUX(35, 6)

[ 266](ambiq-apollo3-pinctrl_8h.md#a8fa21604c6dd1dcdc7ad5d74dfb2afaf)#define BLEIF\_STATUS\_P35 APOLLO3\_PINMUX(35, 7)

[ 267](ambiq-apollo3-pinctrl_8h.md#a3595cef3917f8dbb33c495fa3dd129d9)#define TRIG1\_P36 APOLLO3\_PINMUX(36, 0)

[ 268](ambiq-apollo3-pinctrl_8h.md#aae112b0ebd7c6f448b1ce24b772910a4)#define NCE36\_P36 APOLLO3\_PINMUX(36, 1)

[ 269](ambiq-apollo3-pinctrl_8h.md#abe283e2a79b535f5afb8c82ebba32fce)#define UART1RX\_P36 APOLLO3\_PINMUX(36, 2)

[ 270](ambiq-apollo3-pinctrl_8h.md#a3050173d1ff33494b4b047fd11aff68d)#define GPIO\_P36 APOLLO3\_PINMUX(36, 3)

[ 271](ambiq-apollo3-pinctrl_8h.md#a48be8de8a03a7a27a7848c64adb97665)#define XT32KHz\_P36 APOLLO3\_PINMUX(36, 4)

[ 272](ambiq-apollo3-pinctrl_8h.md#a1b3e74a2c7e43f142fdc02b096236733)#define UA1CTS\_P36 APOLLO3\_PINMUX(36, 5)

[ 273](ambiq-apollo3-pinctrl_8h.md#a6a6bf8ffd195353bbccb43904442db80)#define UA0CTS\_P36 APOLLO3\_PINMUX(36, 6)

[ 274](ambiq-apollo3-pinctrl_8h.md#aaf12889bb6f7de1a92c0d10147c921bf)#define PDMDATA\_P36 APOLLO3\_PINMUX(36, 7)

[ 275](ambiq-apollo3-pinctrl_8h.md#a1bf06e0a3c6234f2c594939d658de1de)#define TRIG2\_P37 APOLLO3\_PINMUX(37, 0)

[ 276](ambiq-apollo3-pinctrl_8h.md#a736adccb71d5a32e0519cbd8c89d6b77)#define NCE37\_P37 APOLLO3\_PINMUX(37, 1)

[ 277](ambiq-apollo3-pinctrl_8h.md#a3b0abd07adcc2cd6b6764f715cd21cd5)#define UA0RTS\_P37 APOLLO3\_PINMUX(37, 2)

[ 278](ambiq-apollo3-pinctrl_8h.md#a5895dbfee43e62831294b162bde44b9e)#define GPIO\_P37 APOLLO3\_PINMUX(37, 3)

[ 279](ambiq-apollo3-pinctrl_8h.md#ab0f35ce206392abf106f6b0e702664c1)#define SCCIO\_P37 APOLLO3\_PINMUX(37, 4)

[ 280](ambiq-apollo3-pinctrl_8h.md#af51f177fc9f7208bcf5815a478d29978)#define UART1TX\_P37 APOLLO3\_PINMUX(37, 5)

[ 281](ambiq-apollo3-pinctrl_8h.md#a2dc471687b4110dc079f5d896f7fe2e2)#define PDMCLK\_P37 APOLLO3\_PINMUX(37, 6)

[ 282](ambiq-apollo3-pinctrl_8h.md#a3dd5aac8ad93fe07b4ab74c35269dba6)#define CTIM29\_P37 APOLLO3\_PINMUX(37, 7)

[ 283](ambiq-apollo3-pinctrl_8h.md#a2d5a132e305dbb9cc38b4f062ab2a5a1)#define TRIG3\_P38 APOLLO3\_PINMUX(38, 0)

[ 284](ambiq-apollo3-pinctrl_8h.md#a7eb51c6fb1bdaabcd854928f0fc53365)#define NCE38\_P38 APOLLO3\_PINMUX(38, 1)

[ 285](ambiq-apollo3-pinctrl_8h.md#aa49ea18a61d8190908b5556c6298e6fa)#define UA0CTS\_P38 APOLLO3\_PINMUX(38, 2)

[ 286](ambiq-apollo3-pinctrl_8h.md#a8786cdf36cc244ccb754406e7091dc31)#define GPIO\_P38 APOLLO3\_PINMUX(38, 3)

[ 287](ambiq-apollo3-pinctrl_8h.md#a1d5ee7db62801b7f7ba60c4e81daffcf)#define M3MOSI\_P38 APOLLO3\_PINMUX(38, 5)

[ 288](ambiq-apollo3-pinctrl_8h.md#a41cec431ed8db8d5286149552695caaf)#define UART1RX\_P38 APOLLO3\_PINMUX(38, 6)

[ 289](ambiq-apollo3-pinctrl_8h.md#a3ed9a495f050ab7486aadc5867539a59)#define UART0TX\_P39 APOLLO3\_PINMUX(39, 0)

[ 290](ambiq-apollo3-pinctrl_8h.md#ae99c8956963caaa4d16d5b3f1c1bb9ce)#define UART1TX\_P39 APOLLO3\_PINMUX(39, 1)

[ 291](ambiq-apollo3-pinctrl_8h.md#a6c33f4bc8b739c173b92d185884aaa4b)#define CTIM25\_P39 APOLLO3\_PINMUX(39, 2)

[ 292](ambiq-apollo3-pinctrl_8h.md#a5a4c89d2f63802373c28dc64010cd6c8)#define GPIO\_P39 APOLLO3\_PINMUX(39, 3)

[ 293](ambiq-apollo3-pinctrl_8h.md#a8a962334908f406e82ac843741b0c837)#define M4SCL\_P39 APOLLO3\_PINMUX(39, 4)

[ 294](ambiq-apollo3-pinctrl_8h.md#a76c405ee75ccbd3e6ba7016c25ad09ad)#define M4SCK\_P39 APOLLO3\_PINMUX(39, 5)

[ 295](ambiq-apollo3-pinctrl_8h.md#a175181dfaf1f6fff4ef61181d450b0f3)#define UART0RX\_P40 APOLLO3\_PINMUX(40, 0)

[ 296](ambiq-apollo3-pinctrl_8h.md#ab6fb2d741ae9ca9492959e8b04d2ab8c)#define UART1RX\_P40 APOLLO3\_PINMUX(40, 1)

[ 297](ambiq-apollo3-pinctrl_8h.md#a4d41b8f7fd97fcae660bf35bf562f4b8)#define TRIG0\_P40 APOLLO3\_PINMUX(40, 2)

[ 298](ambiq-apollo3-pinctrl_8h.md#a388d84a144f3522f0fa9a6d5f860219c)#define GPIO\_P40 APOLLO3\_PINMUX(40, 3)

[ 299](ambiq-apollo3-pinctrl_8h.md#a9632c0a042f4bb66a728d0b830c40367)#define M4SDAWIR3\_P40 APOLLO3\_PINMUX(40, 4)

[ 300](ambiq-apollo3-pinctrl_8h.md#a3355068431b201477fc0dd1a4f87df68)#define M4MISO\_P40 APOLLO3\_PINMUX(40, 5)

[ 301](ambiq-apollo3-pinctrl_8h.md#aaaf74f87cd67b25b654c92e58311d818)#define NCE41\_P41 APOLLO3\_PINMUX(41, 0)

[ 302](ambiq-apollo3-pinctrl_8h.md#a008c508f2483e318e52d3d6bf20f0a1a)#define BLEIF\_IRQ\_P41 APOLLO3\_PINMUX(41, 1)

[ 303](ambiq-apollo3-pinctrl_8h.md#a7d5cbbcd03000b54af3d06566fd3b659)#define SWO\_P41 APOLLO3\_PINMUX(41, 2)

[ 304](ambiq-apollo3-pinctrl_8h.md#a8c96f8b549c1d2739c024137286035e1)#define GPIO\_P41 APOLLO3\_PINMUX(41, 3)

[ 305](ambiq-apollo3-pinctrl_8h.md#a1b3a9948d8a90649b505fcb684fe523d)#define I2SWCLK\_P41 APOLLO3\_PINMUX(41, 4)

[ 306](ambiq-apollo3-pinctrl_8h.md#a09961d9c0667f515d82a7c53e972a48d)#define UA1RTS\_P41 APOLLO3\_PINMUX(41, 5)

[ 307](ambiq-apollo3-pinctrl_8h.md#a2b7dc7334200258b20a08422ea361f70)#define UART0TX\_P41 APOLLO3\_PINMUX(41, 6)

[ 308](ambiq-apollo3-pinctrl_8h.md#aff53cdfb5a9f567fea668005ef248f8a)#define UA0RTS\_P41 APOLLO3\_PINMUX(41, 7)

[ 309](ambiq-apollo3-pinctrl_8h.md#a6705e001463f646a7f26ff4cb316c634)#define UART1TX\_P42 APOLLO3\_PINMUX(42, 0)

[ 310](ambiq-apollo3-pinctrl_8h.md#ae5399f9d5357e096d59283bfea4fd6ee)#define NCE42\_P42 APOLLO3\_PINMUX(42, 1)

[ 311](ambiq-apollo3-pinctrl_8h.md#a1474daf0d4841a34626d23ce9cd7b545)#define CTIM16\_P42 APOLLO3\_PINMUX(42, 2)

[ 312](ambiq-apollo3-pinctrl_8h.md#ad2ddbd7fd0001abfcf1416caa9f56496)#define GPIO\_P42 APOLLO3\_PINMUX(42, 3)

[ 313](ambiq-apollo3-pinctrl_8h.md#a7be4191ad1020cf880616188964f0a89)#define M3SCL\_P42 APOLLO3\_PINMUX(42, 4)

[ 314](ambiq-apollo3-pinctrl_8h.md#a0a924f11185e5c0c0cc58161efdefcf9)#define M3SCK\_P42 APOLLO3\_PINMUX(42, 5)

[ 315](ambiq-apollo3-pinctrl_8h.md#acd68b66375a1cd525670f9f0b3ea9213)#define UART1RX\_P43 APOLLO3\_PINMUX(43, 0)

[ 316](ambiq-apollo3-pinctrl_8h.md#a93e018507d62174c89e7fa137dde36cd)#define NCE43\_P43 APOLLO3\_PINMUX(43, 1)

[ 317](ambiq-apollo3-pinctrl_8h.md#ab1b1fb6876a080a75501fce8190c7820)#define CTIM18\_P43 APOLLO3\_PINMUX(43, 2)

[ 318](ambiq-apollo3-pinctrl_8h.md#aab2f5553d3ce7da8f585c493f82da02f)#define GPIO\_P43 APOLLO3\_PINMUX(43, 3)

[ 319](ambiq-apollo3-pinctrl_8h.md#a2ea30abd4885c0ca0933d9898b5926d1)#define M3SDAWIR3\_P43 APOLLO3\_PINMUX(43, 4)

[ 320](ambiq-apollo3-pinctrl_8h.md#abd8970c9e4ec21d8cb6199f26817a491)#define M3MISO\_P43 APOLLO3\_PINMUX(43, 5)

[ 321](ambiq-apollo3-pinctrl_8h.md#a46baf1010c95eee1dc0011c1864c4796)#define UA1RTS\_P44 APOLLO3\_PINMUX(44, 0)

[ 322](ambiq-apollo3-pinctrl_8h.md#a3ed79603ebbdb77c08f3d793c0f361d7)#define NCE44\_P44 APOLLO3\_PINMUX(44, 1)

[ 323](ambiq-apollo3-pinctrl_8h.md#a181b829366db1077513b25ba65ea1841)#define CTIM20\_P44 APOLLO3\_PINMUX(44, 2)

[ 324](ambiq-apollo3-pinctrl_8h.md#accbd9b4f6fa257af91af9a533ba856ea)#define GPIO\_P44 APOLLO3\_PINMUX(44, 3)

[ 325](ambiq-apollo3-pinctrl_8h.md#a11ea4c9cd1f25fc2aba92f5d4ef7b206)#define M4MOSI\_P44 APOLLO3\_PINMUX(44, 5)

[ 326](ambiq-apollo3-pinctrl_8h.md#a51592b8b7e152dbb622ef0a330862341)#define UART0TX\_P44 APOLLO3\_PINMUX(44, 6)

[ 327](ambiq-apollo3-pinctrl_8h.md#a944d829a81b45cf99560241e9b19154d)#define UA1CTS\_P45 APOLLO3\_PINMUX(45, 0)

[ 328](ambiq-apollo3-pinctrl_8h.md#a8b9c9c5513d7098d3772bf031eefdc34)#define NCE45\_P45 APOLLO3\_PINMUX(45, 1)

[ 329](ambiq-apollo3-pinctrl_8h.md#aa1d5c972c6278777fabc856a5f6ff9d3)#define CTIM22\_P45 APOLLO3\_PINMUX(45, 2)

[ 330](ambiq-apollo3-pinctrl_8h.md#afda67e6b2d71c41df2c9384829780eaf)#define GPIO\_P45 APOLLO3\_PINMUX(45, 3)

[ 331](ambiq-apollo3-pinctrl_8h.md#af628f20a4932e8140b14eb3b4c07b913)#define I2SDAT\_P45 APOLLO3\_PINMUX(45, 4)

[ 332](ambiq-apollo3-pinctrl_8h.md#ac3d93a44f8fa496120aff6de06813fcc)#define PDMDATA\_P45 APOLLO3\_PINMUX(45, 5)

[ 333](ambiq-apollo3-pinctrl_8h.md#af7673ee93e7a84ad6e16846d98de6464)#define UART0RX\_P45 APOLLO3\_PINMUX(45, 6)

[ 334](ambiq-apollo3-pinctrl_8h.md#ab1907bebf4d3e6951994035f697ed321)#define SWO\_P45 APOLLO3\_PINMUX(45, 7)

[ 335](ambiq-apollo3-pinctrl_8h.md#a09604ed08062afbbd82ef684a27b196d)#define I2SBCLK\_P46 APOLLO3\_PINMUX(46, 0)

[ 336](ambiq-apollo3-pinctrl_8h.md#a5b0e939354b2c232bdc48a3dcb9a1607)#define NCE46\_P46 APOLLO3\_PINMUX(46, 1)

[ 337](ambiq-apollo3-pinctrl_8h.md#a72d372c5f5358c9af85d6802dc317f6e)#define CTIM24\_P46 APOLLO3\_PINMUX(46, 2)

[ 338](ambiq-apollo3-pinctrl_8h.md#af5d342a38a441738d343eeef58c1cdb3)#define GPIO\_P46 APOLLO3\_PINMUX(46, 3)

[ 339](ambiq-apollo3-pinctrl_8h.md#add5fa4e696047cb893bb829416ee2afd)#define SCCRST\_P46 APOLLO3\_PINMUX(46, 4)

[ 340](ambiq-apollo3-pinctrl_8h.md#a60677b54a72e30bfd0c04de7ff9217a7)#define PDMCLK\_P46 APOLLO3\_PINMUX(46, 5)

[ 341](ambiq-apollo3-pinctrl_8h.md#afe121783dfe5a9958c15ae0883b83cfb)#define UART1TX\_P46 APOLLO3\_PINMUX(46, 6)

[ 342](ambiq-apollo3-pinctrl_8h.md#a17e7362e03a87627fff5643989fcca00)#define SWO\_P46 APOLLO3\_PINMUX(46, 7)

[ 343](ambiq-apollo3-pinctrl_8h.md#a55e6549b3ba1beca7ae1db93b7f809ee)#define XT32KHz\_P47 APOLLO3\_PINMUX(47, 0)

[ 344](ambiq-apollo3-pinctrl_8h.md#a1f411d730489dee140ae375049d449fd)#define NCE47\_P47 APOLLO3\_PINMUX(47, 1)

[ 345](ambiq-apollo3-pinctrl_8h.md#a0bb0b6007b81b87f0e5a633d962957e5)#define CTIM26\_P47 APOLLO3\_PINMUX(47, 2)

[ 346](ambiq-apollo3-pinctrl_8h.md#a1eb20e4fdae76831bf870bff406c346e)#define GPIO\_P47 APOLLO3\_PINMUX(47, 3)

[ 347](ambiq-apollo3-pinctrl_8h.md#aece153beaf82657c8de3ecd17ea62757)#define M5MOSI\_P47 APOLLO3\_PINMUX(47, 5)

[ 348](ambiq-apollo3-pinctrl_8h.md#a45c38170a7a3b57c6576ebfa6f52b35c)#define UART1RX\_P47 APOLLO3\_PINMUX(47, 6)

[ 349](ambiq-apollo3-pinctrl_8h.md#aaaafe03305c7bafe3020c6c50e56d3dd)#define UART0TX\_P48 APOLLO3\_PINMUX(48, 0)

[ 350](ambiq-apollo3-pinctrl_8h.md#ad2333f40db7fb9ecfbd1392e9554ffa3)#define NCE48\_P48 APOLLO3\_PINMUX(48, 1)

[ 351](ambiq-apollo3-pinctrl_8h.md#a070d0cbdfdd6525c2d1e61197af52c61)#define CTIM28\_P48 APOLLO3\_PINMUX(48, 2)

[ 352](ambiq-apollo3-pinctrl_8h.md#af730366def18c0d1bf2e4c00fe3c1ab8)#define GPIO\_P48 APOLLO3\_PINMUX(48, 3)

[ 353](ambiq-apollo3-pinctrl_8h.md#a11a7466d3e7ced79092085f5704fa4d8)#define M5SCL\_P48 APOLLO3\_PINMUX(48, 4)

[ 354](ambiq-apollo3-pinctrl_8h.md#a448e33923f0e23281b0d4ef733199b5c)#define M5SCK\_P48 APOLLO3\_PINMUX(48, 5)

[ 355](ambiq-apollo3-pinctrl_8h.md#a70696ef3a46aa08391bdf4d3ebc9aa3f)#define UART0RX\_P49 APOLLO3\_PINMUX(49, 0)

[ 356](ambiq-apollo3-pinctrl_8h.md#a339781c28180de2027fc9295189463e1)#define NCE49\_P49 APOLLO3\_PINMUX(49, 1)

[ 357](ambiq-apollo3-pinctrl_8h.md#adce81e86454552afd05cf0144a16a9f4)#define CTIM30\_P49 APOLLO3\_PINMUX(49, 2)

[ 358](ambiq-apollo3-pinctrl_8h.md#a4b290382e034342af84424e34cb6d297)#define GPIO\_P49 APOLLO3\_PINMUX(49, 3)

[ 359](ambiq-apollo3-pinctrl_8h.md#ad1fede78430cc3626bddb9fab7b257cf)#define M5SDAWIR3\_P49 APOLLO3\_PINMUX(49, 4)

[ 360](ambiq-apollo3-pinctrl_8h.md#a9393e54fe2a906feb32275d905db7465)#define M5MISO\_P49 APOLLO3\_PINMUX(49, 5)

[ 361](ambiq-apollo3-pinctrl_8h.md#a056b770b0d92b72bd3c33a957683c790)#define SWO\_P50 APOLLO3\_PINMUX(50, 0)

[ 362](ambiq-apollo3-pinctrl_8h.md#ab7492256a637deef5ea4943b4b701110)#define NCE50\_P50 APOLLO3\_PINMUX(50, 1)

[ 363](ambiq-apollo3-pinctrl_8h.md#aa825c015fb5592a56455e0fbd277ed6e)#define CT0\_P50 APOLLO3\_PINMUX(50, 2)

[ 364](ambiq-apollo3-pinctrl_8h.md#a44de537cf2f84b012dc099c000d47eee)#define GPIO\_P50 APOLLO3\_PINMUX(50, 3)

[ 365](ambiq-apollo3-pinctrl_8h.md#ab967379871f5d5e937c536b0af767154)#define UART0TX\_P50 APOLLO3\_PINMUX(50, 4)

[ 366](ambiq-apollo3-pinctrl_8h.md#a6277bab84473fecc433b54e6a29b3c40)#define UART0RX\_P50 APOLLO3\_PINMUX(50, 5)

[ 367](ambiq-apollo3-pinctrl_8h.md#a79377784abe4f92663d3fb9bf878921a)#define UART1TX\_P50 APOLLO3\_PINMUX(50, 6)

[ 368](ambiq-apollo3-pinctrl_8h.md#ae64fb321a2fb963c1f0e1771b6f5f8f0)#define UART1RX\_P50 APOLLO3\_PINMUX(50, 7)

[ 369](ambiq-apollo3-pinctrl_8h.md#a9569a86b721653e4303b538d858362ff)#define MSPI1\_0\_P51 APOLLO3\_PINMUX(51, 0)

[ 370](ambiq-apollo3-pinctrl_8h.md#aeca26feeace6bc79995c2e619b1a9c18)#define NCE51\_P51 APOLLO3\_PINMUX(51, 1)

[ 371](ambiq-apollo3-pinctrl_8h.md#a4eefe29a2117733367a1883f4c7a233c)#define CTIM1\_P51 APOLLO3\_PINMUX(51, 2)

[ 372](ambiq-apollo3-pinctrl_8h.md#a78a6a9fa2e9eb9ba6ff803a5810de263)#define GPIO\_P51 APOLLO3\_PINMUX(51, 3)

[ 373](ambiq-apollo3-pinctrl_8h.md#ac6b4ad9a963294d75262c1e94b8abf8f)#define MSPI1\_1\_P52 APOLLO3\_PINMUX(52, 0)

[ 374](ambiq-apollo3-pinctrl_8h.md#ae86416562248f70f8fddcbfda85a3ae3)#define NCE52\_P52 APOLLO3\_PINMUX(52, 1)

[ 375](ambiq-apollo3-pinctrl_8h.md#a826d6ddcd51c2468767bc70583608c29)#define CTIM2\_P52 APOLLO3\_PINMUX(52, 2)

[ 376](ambiq-apollo3-pinctrl_8h.md#aa8fc5cd8e841cc12ee97736b5d5b2637)#define GPIO\_P52 APOLLO3\_PINMUX(52, 3)

[ 377](ambiq-apollo3-pinctrl_8h.md#ac4d5baf17923790039150886151f7dec)#define MSPI1\_2\_P53 APOLLO3\_PINMUX(53, 0)

[ 378](ambiq-apollo3-pinctrl_8h.md#aae0ee7affb647cfd3d54d168868ef485)#define NCE53\_P53 APOLLO3\_PINMUX(53, 1)

[ 379](ambiq-apollo3-pinctrl_8h.md#a183d8e6c6bd4579d0feae2c3c67e2e61)#define CTIM3\_P53 APOLLO3\_PINMUX(53, 2)

[ 380](ambiq-apollo3-pinctrl_8h.md#aa41e6f073ae876d1486552a07ace93a3)#define GPIO\_P53 APOLLO3\_PINMUX(53, 3)

[ 381](ambiq-apollo3-pinctrl_8h.md#a8234fa9ff3afbc23fa0f895f0076835c)#define MSPI1\_3\_P54 APOLLO3\_PINMUX(54, 0)

[ 382](ambiq-apollo3-pinctrl_8h.md#a6318a96c1367922e5ecd0f682d432630)#define NCE54\_P54 APOLLO3\_PINMUX(54, 1)

[ 383](ambiq-apollo3-pinctrl_8h.md#ae8b5cb40219aec3a11f0251a39a06a9d)#define CTIM4\_P54 APOLLO3\_PINMUX(54, 2)

[ 384](ambiq-apollo3-pinctrl_8h.md#a8b614afb4941fbe9036fa20421a55820)#define GPIO\_P54 APOLLO3\_PINMUX(54, 3)

[ 385](ambiq-apollo3-pinctrl_8h.md#abcb127632e19c63b97bd01f6a2de8e9a)#define MSPI1\_4\_P55 APOLLO3\_PINMUX(55, 0)

[ 386](ambiq-apollo3-pinctrl_8h.md#ad5438399e3ff56c263631991b09dd460)#define NCE55\_P55 APOLLO3\_PINMUX(55, 1)

[ 387](ambiq-apollo3-pinctrl_8h.md#a516c0fb62d563ceca86131539f09f131)#define CTIM5\_P55 APOLLO3\_PINMUX(55, 2)

[ 388](ambiq-apollo3-pinctrl_8h.md#a2fcffaace9255d9e639de6c2596603c8)#define GPIO\_P55 APOLLO3\_PINMUX(55, 3)

[ 389](ambiq-apollo3-pinctrl_8h.md#a95e11921d5164ad709ab5cdad5f1a58c)#define MSPI1\_5\_P56 APOLLO3\_PINMUX(56, 0)

[ 390](ambiq-apollo3-pinctrl_8h.md#ad8e09cff85610b1bfb03403771360685)#define NCE56\_P56 APOLLO3\_PINMUX(56, 1)

[ 391](ambiq-apollo3-pinctrl_8h.md#ae00988c0a4632e534f2252622bd48759)#define CTIM6\_P56 APOLLO3\_PINMUX(56, 2)

[ 392](ambiq-apollo3-pinctrl_8h.md#ad9c517c0112a8c8634b9ad46ee32dd45)#define GPIO\_P56 APOLLO3\_PINMUX(56, 3)

[ 393](ambiq-apollo3-pinctrl_8h.md#a8831303ca7109996c6446350e384392d)#define MSPI1\_6\_P57 APOLLO3\_PINMUX(57, 0)

[ 394](ambiq-apollo3-pinctrl_8h.md#a98fb369e6acd52cc5aae8e6730ed9758)#define NCE57\_P57 APOLLO3\_PINMUX(57, 1)

[ 395](ambiq-apollo3-pinctrl_8h.md#ac2e6c19821053ab44d79a352d48ca1f8)#define CTIM7\_P57 APOLLO3\_PINMUX(57, 2)

[ 396](ambiq-apollo3-pinctrl_8h.md#a83be188c573c4f64966aae37f47caf5b)#define GPIO\_P57 APOLLO3\_PINMUX(57, 3)

[ 397](ambiq-apollo3-pinctrl_8h.md#ab61ac243ccd5f0a1d1fdec4b8d45b6dc)#define MSPI1\_7\_P58 APOLLO3\_PINMUX(58, 0)

[ 398](ambiq-apollo3-pinctrl_8h.md#aac11c1a52fc64f3c2684b4323e28bdb4)#define NCE58\_P58 APOLLO3\_PINMUX(58, 1)

[ 399](ambiq-apollo3-pinctrl_8h.md#a505da5511b9f77bc9623595b80b9e7d6)#define CTIM8\_P58 APOLLO3\_PINMUX(58, 2)

[ 400](ambiq-apollo3-pinctrl_8h.md#a876dd6e6770f3c605b06c61e9a6640ac)#define GPIO\_P58 APOLLO3\_PINMUX(58, 3)

[ 401](ambiq-apollo3-pinctrl_8h.md#ae74279d568a99727bd00816f856f2bec)#define MSPI1\_8\_P59 APOLLO3\_PINMUX(59, 0)

[ 402](ambiq-apollo3-pinctrl_8h.md#ab437cea609c7b3dbdec00e17f674ee6c)#define NCE59\_P59 APOLLO3\_PINMUX(59, 1)

[ 403](ambiq-apollo3-pinctrl_8h.md#adc616fdbce3f49c78d01d5ffb9245ada)#define CTIM9\_P59 APOLLO3\_PINMUX(59, 2)

[ 404](ambiq-apollo3-pinctrl_8h.md#ab5b877868310ab0269c468edcac715f7)#define GPIO\_P59 APOLLO3\_PINMUX(59, 3)

[ 405](ambiq-apollo3-pinctrl_8h.md#acbdd8675b5c6094213377db4d57b5c76)#define MSPI1\_9\_P60 APOLLO3\_PINMUX(60, 0)

[ 406](ambiq-apollo3-pinctrl_8h.md#af5a0f373987f9e093d0be1e96fc422e0)#define NCE60\_P60 APOLLO3\_PINMUX(60, 1)

[ 407](ambiq-apollo3-pinctrl_8h.md#a15c4eccf0f0de2c64285b4ad06258a3a)#define CTIM10\_P60 APOLLO3\_PINMUX(60, 2)

[ 408](ambiq-apollo3-pinctrl_8h.md#ac3a637135617760fba12cf98aeb107c2)#define GPIO\_P60 APOLLO3\_PINMUX(60, 3)

[ 409](ambiq-apollo3-pinctrl_8h.md#af6865d7d7b0939fee8634025753ad0ac)#define SWO\_P61 APOLLO3\_PINMUX(61, 0)

[ 410](ambiq-apollo3-pinctrl_8h.md#ab5911745a6c23c3a7ded39e214324a1b)#define NCE61\_P61 APOLLO3\_PINMUX(61, 1)

[ 411](ambiq-apollo3-pinctrl_8h.md#a53cb8cd389fd7d9323122949b9642088)#define CTIM11\_P61 APOLLO3\_PINMUX(61, 2)

[ 412](ambiq-apollo3-pinctrl_8h.md#a5cc6477cb81b8e732013eee58ce0183d)#define GPIO\_P61 APOLLO3\_PINMUX(61, 3)

[ 413](ambiq-apollo3-pinctrl_8h.md#a13169414a9db1d2d918fd8a1ac6e328e)#define UART0TX\_P61 APOLLO3\_PINMUX(61, 4)

[ 414](ambiq-apollo3-pinctrl_8h.md#a5ef06f1ca2d2d28e87846add941a6a01)#define UART0RX\_P61 APOLLO3\_PINMUX(61, 5)

[ 415](ambiq-apollo3-pinctrl_8h.md#a4b046371e9d9717fbc966b890d231dc4)#define UART1TX\_P61 APOLLO3\_PINMUX(61, 6)

[ 416](ambiq-apollo3-pinctrl_8h.md#a8ba999d652f37a9cec7f09ec48bb1efd)#define UART1RX\_P61 APOLLO3\_PINMUX(61, 7)

[ 417](ambiq-apollo3-pinctrl_8h.md#ac3477b8ba498f9d6ce303c891fc92102)#define SWO\_P62 APOLLO3\_PINMUX(62, 0)

[ 418](ambiq-apollo3-pinctrl_8h.md#acff3d4c76b5032bc61e0757224cf5c30)#define NCE62\_P62 APOLLO3\_PINMUX(62, 1)

[ 419](ambiq-apollo3-pinctrl_8h.md#a2ac80f7683a1da305ab0fa6a76a4e366)#define CTIM12\_P62 APOLLO3\_PINMUX(62, 2)

[ 420](ambiq-apollo3-pinctrl_8h.md#ad8ad98d7206b4d60e9a785270cb6bebd)#define GPIO\_P62 APOLLO3\_PINMUX(62, 3)

[ 421](ambiq-apollo3-pinctrl_8h.md#a17a8866677f47e6edc86a3873c09d606)#define UA0CTS\_P62 APOLLO3\_PINMUX(62, 4)

[ 422](ambiq-apollo3-pinctrl_8h.md#a3330f5f0766f022c8d4f215395ef1f8f)#define UA0RTS\_P62 APOLLO3\_PINMUX(62, 5)

[ 423](ambiq-apollo3-pinctrl_8h.md#a5619b10dd987655fd0f8b470832dd617)#define UA1CTS\_P62 APOLLO3\_PINMUX(62, 6)

[ 424](ambiq-apollo3-pinctrl_8h.md#ac844f507a7ad999a2ce9a749667d43ec)#define UA1RTS\_P62 APOLLO3\_PINMUX(62, 7)

[ 425](ambiq-apollo3-pinctrl_8h.md#ad1a604f4d60d6ffc7182e7655073bd11)#define SWO\_P63 APOLLO3\_PINMUX(63, 0)

[ 426](ambiq-apollo3-pinctrl_8h.md#acd4dd1d3133002f0c60426e542702dd3)#define NCE63\_P63 APOLLO3\_PINMUX(63, 1)

[ 427](ambiq-apollo3-pinctrl_8h.md#a896899eb01c3da31320937430cf965e9)#define CTIM13\_P63 APOLLO3\_PINMUX(63, 2)

[ 428](ambiq-apollo3-pinctrl_8h.md#a9e7881322451f9c064a827bd26c16aa0)#define GPIO\_P63 APOLLO3\_PINMUX(63, 3)

[ 429](ambiq-apollo3-pinctrl_8h.md#aad6095bc6dc59c8cfb0a1c19d937d573)#define UA0CTS\_P63 APOLLO3\_PINMUX(63, 4)

[ 430](ambiq-apollo3-pinctrl_8h.md#ab0422d143c7ddf4dd7fce671af815bb9)#define UA0RTS\_P63 APOLLO3\_PINMUX(63, 5)

[ 431](ambiq-apollo3-pinctrl_8h.md#a0d8dd2d9de57fd25bb59d31be03014ec)#define UA1CTS\_P63 APOLLO3\_PINMUX(63, 6)

[ 432](ambiq-apollo3-pinctrl_8h.md#a362e069b94a6ea0b5bb1f5b64aef473f)#define UA1RTS\_P63 APOLLO3\_PINMUX(63, 7)

[ 433](ambiq-apollo3-pinctrl_8h.md#a47ffd6951b155ac3b80a5f4ac5057e8b)#define MSPI2\_0\_P64 APOLLO3\_PINMUX(64, 0)

[ 434](ambiq-apollo3-pinctrl_8h.md#af279b091bf1b2e9854cb240fb07d7411)#define NCE64\_P64 APOLLO3\_PINMUX(64, 1)

[ 435](ambiq-apollo3-pinctrl_8h.md#a539c301c87081cafff14c9a0902e90de)#define CTIM14\_P64 APOLLO3\_PINMUX(64, 2)

[ 436](ambiq-apollo3-pinctrl_8h.md#ac031a8b0e6fe953a329bccae5138864c)#define GPIO\_P64 APOLLO3\_PINMUX(64, 3)

[ 437](ambiq-apollo3-pinctrl_8h.md#a267fef799fd16097688aa7a777fb5194)#define MSPI2\_1\_P65 APOLLO3\_PINMUX(65, 0)

[ 438](ambiq-apollo3-pinctrl_8h.md#a4913e8e909a5f53078ec4f73eda5c112)#define NCE65\_P65 APOLLO3\_PINMUX(65, 1)

[ 439](ambiq-apollo3-pinctrl_8h.md#a9a0bb2452ab886f75da833f8c546bef0)#define CTIM15\_P65 APOLLO3\_PINMUX(65, 2)

[ 440](ambiq-apollo3-pinctrl_8h.md#ae9af3264c78732b1bc79b552d68dfa6a)#define GPIO\_P65 APOLLO3\_PINMUX(65, 3)

[ 441](ambiq-apollo3-pinctrl_8h.md#a4dcf9f729fb234071170c7116620bdbc)#define MSPI2\_2\_P66 APOLLO3\_PINMUX(66, 0)

[ 442](ambiq-apollo3-pinctrl_8h.md#acff679577d81e687a56906eebf769bf6)#define NCE66\_P66 APOLLO3\_PINMUX(66, 1)

[ 443](ambiq-apollo3-pinctrl_8h.md#a365f841a97880964c986c808afe50cbf)#define CTIM16\_P66 APOLLO3\_PINMUX(66, 2)

[ 444](ambiq-apollo3-pinctrl_8h.md#ac82bb9747100752447c61e008d0aed46)#define GPIO\_P66 APOLLO3\_PINMUX(66, 3)

[ 445](ambiq-apollo3-pinctrl_8h.md#a13cbb5730534690db2ce73c739bce161)#define MSPI2\_3\_P67 APOLLO3\_PINMUX(67, 0)

[ 446](ambiq-apollo3-pinctrl_8h.md#a94cc174e483db8110ca76fff12629c6d)#define NCE67\_P67 APOLLO3\_PINMUX(67, 1)

[ 447](ambiq-apollo3-pinctrl_8h.md#a192693e602f7328d20fcaeb7a80e2b16)#define CTIM17\_P67 APOLLO3\_PINMUX(67, 2)

[ 448](ambiq-apollo3-pinctrl_8h.md#aa9a6029306499ec2cccbb76899488bf3)#define GPIO\_P67 APOLLO3\_PINMUX(67, 3)

[ 449](ambiq-apollo3-pinctrl_8h.md#adcca1198343f7a85b2f87b1917cfc6c0)#define MSPI2\_4\_P68 APOLLO3\_PINMUX(68, 0)

[ 450](ambiq-apollo3-pinctrl_8h.md#a43db97f86803b04b80140c3c12f096d5)#define NCE68\_P68 APOLLO3\_PINMUX(68, 1)

[ 451](ambiq-apollo3-pinctrl_8h.md#a1db22d617bacc5856a42e817d3aab57a)#define CTIM18\_P68 APOLLO3\_PINMUX(68, 2)

[ 452](ambiq-apollo3-pinctrl_8h.md#a3e315d2425fb95945b68e7c4e2fe954a)#define GPIO\_P68 APOLLO3\_PINMUX(68, 3)

[ 453](ambiq-apollo3-pinctrl_8h.md#a5fa4920fa2af91403279165ec14471c3)#define SWO\_P69 APOLLO3\_PINMUX(69, 0)

[ 454](ambiq-apollo3-pinctrl_8h.md#a8e86b1f165b06bde1344f2a0591591f6)#define NCE69\_P69 APOLLO3\_PINMUX(69, 1)

[ 455](ambiq-apollo3-pinctrl_8h.md#a25a3df1f226d95466f44b45fccfa9239)#define CTIM19\_P69 APOLLO3\_PINMUX(69, 2)

[ 456](ambiq-apollo3-pinctrl_8h.md#a5602b2af723fb7fe3bf1121b0577c2e7)#define GPIO\_P69 APOLLO3\_PINMUX(69, 3)

[ 457](ambiq-apollo3-pinctrl_8h.md#a1ae2ba2a91ba842284fd6cbb156def04)#define UART0TX\_P69 APOLLO3\_PINMUX(69, 4)

[ 458](ambiq-apollo3-pinctrl_8h.md#ac0aec58a68e82e74ff74d31889ba6eda)#define UART0RX\_P69 APOLLO3\_PINMUX(69, 5)

[ 459](ambiq-apollo3-pinctrl_8h.md#a147d9681b5a8ca2b3cb1a9ed805762fd)#define UART1TX\_P69 APOLLO3\_PINMUX(69, 6)

[ 460](ambiq-apollo3-pinctrl_8h.md#a6d3cf67ebe5a1f059fd47110357a7e4e)#define UART1RX\_P69 APOLLO3\_PINMUX(69, 7)

[ 461](ambiq-apollo3-pinctrl_8h.md#ae840ad7da2d8d0741a885d60b108c6f6)#define SWO\_P70 APOLLO3\_PINMUX(70, 0)

[ 462](ambiq-apollo3-pinctrl_8h.md#a154b9a05cda9e8a41f84f82417a60d81)#define NCE70\_P70 APOLLO3\_PINMUX(70, 1)

[ 463](ambiq-apollo3-pinctrl_8h.md#aadd1d390b428c5f7b8196efc46743ea4)#define CTIM20\_P70 APOLLO3\_PINMUX(70, 2)

[ 464](ambiq-apollo3-pinctrl_8h.md#af1f938f04fe3670874c371bfff680c41)#define GPIO\_P70 APOLLO3\_PINMUX(70, 3)

[ 465](ambiq-apollo3-pinctrl_8h.md#a62f156b398182c31da9377c3f417623f)#define UART0TX\_P70 APOLLO3\_PINMUX(70, 4)

[ 466](ambiq-apollo3-pinctrl_8h.md#a086d2fe9f77498d1fee5ad62570a41a1)#define UART0RX\_P70 APOLLO3\_PINMUX(70, 5)

[ 467](ambiq-apollo3-pinctrl_8h.md#a12a07be7ada04c8db5456f26e384c4d5)#define UART1TX\_P70 APOLLO3\_PINMUX(70, 6)

[ 468](ambiq-apollo3-pinctrl_8h.md#aad95c312dadb461f7926ab6f01374ed7)#define UART1RX\_P70 APOLLO3\_PINMUX(70, 7)

[ 469](ambiq-apollo3-pinctrl_8h.md#a5b05a881450d820175599526bca285e7)#define SWO\_P71 APOLLO3\_PINMUX(71, 0)

[ 470](ambiq-apollo3-pinctrl_8h.md#a04df6aa292fc65e77cc4de70b36d3d95)#define NCE71\_P71 APOLLO3\_PINMUX(71, 1)

[ 471](ambiq-apollo3-pinctrl_8h.md#a772105d2fea38c937834c65896d8c3cd)#define CTIM21\_P71 APOLLO3\_PINMUX(71, 2)

[ 472](ambiq-apollo3-pinctrl_8h.md#a88cfa6b114b0efb7bfeec35a4110727d)#define GPIO\_P71 APOLLO3\_PINMUX(71, 3)

[ 473](ambiq-apollo3-pinctrl_8h.md#afee0c790c7e8f4dd235d8489ac5c4107)#define UART0TX\_P71 APOLLO3\_PINMUX(71, 4)

[ 474](ambiq-apollo3-pinctrl_8h.md#ae8e2a290af35da4c5d4d882eaa3aa8cd)#define UART0RX\_P71 APOLLO3\_PINMUX(71, 5)

[ 475](ambiq-apollo3-pinctrl_8h.md#a75527d755c741c22f55d12e35f5aef13)#define UART1TX\_P71 APOLLO3\_PINMUX(71, 6)

[ 476](ambiq-apollo3-pinctrl_8h.md#a6a2d312670202739632148c973559135)#define UART1RX\_P71 APOLLO3\_PINMUX(71, 7)

[ 477](ambiq-apollo3-pinctrl_8h.md#aeeb7f033753b1196ff4acb716be4e782)#define SWO\_P72 APOLLO3\_PINMUX(72, 0)

[ 478](ambiq-apollo3-pinctrl_8h.md#a89192a0beda2cecdd53e4fd7174302e5)#define NCE72\_P72 APOLLO3\_PINMUX(72, 1)

[ 479](ambiq-apollo3-pinctrl_8h.md#ac8555a20407cf149854f388bee54f4e0)#define CTIM22\_P72 APOLLO3\_PINMUX(72, 2)

[ 480](ambiq-apollo3-pinctrl_8h.md#adcf84a78ff2d8532d87482678ba2df80)#define GPIO\_P72 APOLLO3\_PINMUX(72, 3)

[ 481](ambiq-apollo3-pinctrl_8h.md#ae68adb841018f98375b7022e370aba0c)#define UART0TX\_P72 APOLLO3\_PINMUX(72, 4)

[ 482](ambiq-apollo3-pinctrl_8h.md#a6720bbe266f8a2d54929325ee19c3b23)#define UART0RX\_P72 APOLLO3\_PINMUX(72, 5)

[ 483](ambiq-apollo3-pinctrl_8h.md#a315caa38da59dbbea5e94f08194ba614)#define UART1TX\_P72 APOLLO3\_PINMUX(72, 6)

[ 484](ambiq-apollo3-pinctrl_8h.md#ae0e923c68bbdf2d2a929c34f580f4fd4)#define UART1RX\_P72 APOLLO3\_PINMUX(72, 7)

[ 485](ambiq-apollo3-pinctrl_8h.md#a9a2b1491dd870b395c181ecd48d136c0)#define SWO\_P73 APOLLO3\_PINMUX(73, 0)

[ 486](ambiq-apollo3-pinctrl_8h.md#a86228f8d9adc8065f76ca1f0af512d50)#define NCE73\_P73 APOLLO3\_PINMUX(73, 1)

[ 487](ambiq-apollo3-pinctrl_8h.md#a74b8d5f54ada101a6a29e2c2b17c3a90)#define CTIM23\_P73 APOLLO3\_PINMUX(73, 2)

[ 488](ambiq-apollo3-pinctrl_8h.md#a284f44425e1437643fad644c5f538b09)#define GPIO\_P73 APOLLO3\_PINMUX(73, 3)

[ 489](ambiq-apollo3-pinctrl_8h.md#af8cca7cdb1b7794250c131fce4e0dc54)#define UA0CTS\_P73 APOLLO3\_PINMUX(73, 4)

[ 490](ambiq-apollo3-pinctrl_8h.md#afc2a1cd4bc96170933509a26828ca200)#define UA0RTS\_P73 APOLLO3\_PINMUX(73, 5)

[ 491](ambiq-apollo3-pinctrl_8h.md#a76e95ea07d5a29cb8bf391ceeda6b177)#define UA1CTS\_P73 APOLLO3\_PINMUX(73, 6)

[ 492](ambiq-apollo3-pinctrl_8h.md#abcc0c2177d3ebab6aef372b39aeff6cb)#define UA1RTS\_P73 APOLLO3\_PINMUX(73, 7)

493

494#endif /\* \_\_APOLLO3\_PINCTRL\_H\_\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [pinctrl](dir_2c6c4fbd167577104b7f1b7148586168.md)
- [ambiq-apollo3-pinctrl.h](ambiq-apollo3-pinctrl_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
