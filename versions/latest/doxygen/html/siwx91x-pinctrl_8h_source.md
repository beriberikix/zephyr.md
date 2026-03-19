---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/siwx91x-pinctrl_8h_source.html
original_path: doxygen/html/siwx91x-pinctrl_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

siwx91x-pinctrl.h

[Go to the documentation of this file.](siwx91x-pinctrl_8h.md)

1/\*

2 \* Copyright (c) 2024 Silicon Laboratories Inc.

3 \* SPDX-License-Identifier: Apache-2.0

4 \*/

5

6#ifndef INCLUDE\_ZEPHYR\_DT\_BINDINGS\_PINCTRL\_SILABS\_SIWX91X\_PINCTRL\_H\_

7#define INCLUDE\_ZEPHYR\_DT\_BINDINGS\_PINCTRL\_SILABS\_SIWX91X\_PINCTRL\_H\_

8

9#include <[zephyr/dt-bindings/pinctrl/silabs-pinctrl-siwx91x.h](silabs-pinctrl-siwx91x_8h.md)>

10

11/\* clang-format off \*/

12

[ 13](siwx91x-pinctrl_8h.md#a51b9722e0c1470e0692d913cd70ca33e)#define AGPIO\_ULP0 SIWX91X\_GPIO(0xFF, 7, 0xFF, 4, 0, 0)

[ 14](siwx91x-pinctrl_8h.md#a30b16a45f81323324e310d96777c6fd8)#define AGPIO\_ULP1 SIWX91X\_GPIO(0xFF, 7, 0xFF, 4, 0, 1)

[ 15](siwx91x-pinctrl_8h.md#a7189b132ac6420c926c8cf2eccab3c6b)#define AGPIO\_ULP2 SIWX91X\_GPIO(0xFF, 7, 0xFF, 4, 0, 2)

[ 16](siwx91x-pinctrl_8h.md#a0d43105668987a220c67393d4674515d)#define AGPIO\_ULP4 SIWX91X\_GPIO(0xFF, 7, 0xFF, 4, 0, 4)

[ 17](siwx91x-pinctrl_8h.md#a2a66cdafa849bf095ca1d6916001f441)#define AGPIO\_ULP5 SIWX91X\_GPIO(0xFF, 7, 0xFF, 4, 0, 5)

[ 18](siwx91x-pinctrl_8h.md#a60dfb206c49bc9005231c936e9393546)#define AGPIO\_ULP6 SIWX91X\_GPIO(0xFF, 7, 0xFF, 4, 0, 6)

[ 19](siwx91x-pinctrl_8h.md#a1ff255f96fa29e9a0c500967596ac57a)#define AGPIO\_ULP7 SIWX91X\_GPIO(0xFF, 7, 0xFF, 4, 0, 7)

[ 20](siwx91x-pinctrl_8h.md#a721b2b6550307530f7ab4068cc11631b)#define AGPIO\_ULP8 SIWX91X\_GPIO(0xFF, 7, 0xFF, 4, 0, 8)

[ 21](siwx91x-pinctrl_8h.md#a228d260414f49b06912a8694b31dc358)#define AGPIO\_ULP9 SIWX91X\_GPIO(0xFF, 7, 0xFF, 4, 0, 9)

[ 22](siwx91x-pinctrl_8h.md#a57855add105b9a5ac3df1600caf2d4bc)#define AGPIO\_ULP10 SIWX91X\_GPIO(0xFF, 7, 0xFF, 4, 0, 10)

[ 23](siwx91x-pinctrl_8h.md#a3e0ca1d417d8c455c275e5e67e071c6c)#define AGPIO\_ULP11 SIWX91X\_GPIO(0xFF, 7, 0xFF, 4, 0, 11)

24

[ 25](siwx91x-pinctrl_8h.md#ac83c2b9578f8d4db50b6f9835e97c89c)#define AUXULP\_TRIG0\_PA11 SIWX91X\_GPIO(9, 5, 6, 0, 11, 5)

[ 26](siwx91x-pinctrl_8h.md#a977eba19833f3c6c6f68928bd0245561)#define AUXULP\_TRIG0\_PB14 SIWX91X\_GPIO(11, 5, 0, 1, 14, 11)

[ 27](siwx91x-pinctrl_8h.md#af810b90802642faa0a47c06edf8811bb)#define AUXULP\_TRIG0\_PD1 SIWX91X\_GPIO(9, 5, 13, 3, 1, 11)

[ 28](siwx91x-pinctrl_8h.md#a945e911bffcedf2cd3e00b0394a990b1)#define AUXULP\_TRIG0\_ULP5 SIWX91X\_GPIO(0xFF, 5, 0xFF, 4, 0, 5)

[ 29](siwx91x-pinctrl_8h.md#a090807259f65186a27e1327fbf599829)#define AUXULP\_TRIG0\_ULP6 SIWX91X\_GPIO(0xFF, 10, 0xFF, 4, 0, 6)

[ 30](siwx91x-pinctrl_8h.md#ab92c286c8db594d8f607ce3ef09657b4)#define AUXULP\_TRIG0\_ULP11 SIWX91X\_GPIO(0xFF, 5, 0xFF, 4, 0, 11)

[ 31](siwx91x-pinctrl_8h.md#adf749c359174226e90d8a2ba64b4983c)#define AUXULP\_TRIG1\_ULP4 SIWX91X\_GPIO(0xFF, 5, 0xFF, 4, 0, 4)

[ 32](siwx91x-pinctrl_8h.md#a1d9a7c9bf69093de19cbdf10953e4c22)#define AUXULP\_TRIG1\_ULP7 SIWX91X\_GPIO(0xFF, 10, 0xFF, 4, 0, 7)

33

[ 34](siwx91x-pinctrl_8h.md#ad5dfd9e198bbb4772a3d286d17a341e7)#define CLK\_I2SPLL\_PB11 SIWX91X\_GPIO(12, 0xFF, 0, 1, 11, 0)

[ 35](siwx91x-pinctrl_8h.md#a830f9845431977f325fc116a75a3844f)#define CLK\_I2SPLL\_PD0 SIWX91X\_GPIO(10, 0xFF, 12, 3, 0, 0)

[ 36](siwx91x-pinctrl_8h.md#a6e1955e42b99df902112835bd8a951bd)#define CLK\_I2SPLL\_PD6 SIWX91X\_GPIO(10, 0xFF, 18, 3, 6, 0)

[ 37](siwx91x-pinctrl_8h.md#ac9ca91f40cf89a9c8e46edc73e533907)#define CLK\_INTFPLL\_PB10 SIWX91X\_GPIO(12, 0xFF, 0, 1, 10, 0)

[ 38](siwx91x-pinctrl_8h.md#a09f586cb666c27fd8257161bfc788cc7)#define CLK\_INTFPLL\_PC15 SIWX91X\_GPIO(10, 0xFF, 11, 2, 15, 0)

[ 39](siwx91x-pinctrl_8h.md#a1f01120307e8a205241131e17f3c77ff)#define CLK\_INTFPLL\_PD5 SIWX91X\_GPIO(10, 0xFF, 17, 3, 5, 0)

[ 40](siwx91x-pinctrl_8h.md#a58ae669b7c40a4987f866c2cafc594f0)#define CLK\_MCUOUT\_PA11 SIWX91X\_GPIO(12, 0xFF, 6, 0, 11, 0)

[ 41](siwx91x-pinctrl_8h.md#ab7691d8319d385202b09388f9829d1d3)#define CLK\_MEMSREF\_PD2 SIWX91X\_GPIO(10, 0xFF, 14, 3, 2, 0)

[ 42](siwx91x-pinctrl_8h.md#a685bf647b5c806f222296a78362a1895)#define CLK\_MEMSREF\_PD8 SIWX91X\_GPIO(10, 0xFF, 20, 3, 8, 0)

[ 43](siwx91x-pinctrl_8h.md#a7949991a56b3078d6dbce92a3057fa5b)#define CLK\_OUT\_PA12 SIWX91X\_GPIO(8, 0xFF, 7, 0, 12, 0)

[ 44](siwx91x-pinctrl_8h.md#a2dd8446bd13ac559b9c120938afce8f0)#define CLK\_OUT\_PA15 SIWX91X\_GPIO(8, 0xFF, 8, 0, 15, 0)

[ 45](siwx91x-pinctrl_8h.md#a5b24098404ae7ca1b5fc7c3f2e1ea0b6)#define CLK\_PLLTESTMODE\_PD3 SIWX91X\_GPIO(10, 0xFF, 15, 3, 3, 0)

[ 46](siwx91x-pinctrl_8h.md#a54f5bee82f71ebd038f053328ecb98dc)#define CLK\_SOCPLL\_PB9 SIWX91X\_GPIO(12, 0xFF, 0, 1, 9, 0)

[ 47](siwx91x-pinctrl_8h.md#a5c1b4e0d5f7767d46651f2835a5409e9)#define CLK\_SOCPLL\_PC14 SIWX91X\_GPIO(10, 0xFF, 10, 2, 14, 0)

[ 48](siwx91x-pinctrl_8h.md#a9435cb6c927d3b45239f00c6881e00ff)#define CLK\_SOCPLL\_PD4 SIWX91X\_GPIO(10, 0xFF, 16, 3, 4, 0)

[ 49](siwx91x-pinctrl_8h.md#a62aba090db9ff8c4914a5adbcfd2c30a)#define CLK\_XTALONIN\_PB12 SIWX91X\_GPIO(12, 0xFF, 0, 1, 12, 0)

[ 50](siwx91x-pinctrl_8h.md#ad3a9196e0b0fb6e8686dc8ca322fefdd)#define CLK\_XTALONIN\_PD9 SIWX91X\_GPIO(10, 0xFF, 21, 3, 9, 0)

51

[ 52](siwx91x-pinctrl_8h.md#a314f4122f4de99444225fe5111910405)#define COMP1\_OUT\_PA8 SIWX91X\_GPIO(9, 5, 3, 0, 8, 2)

[ 53](siwx91x-pinctrl_8h.md#a16ba0bb6449b2b12ab43516b5923a660)#define COMP1\_OUT\_PB12 SIWX91X\_GPIO(11, 5, 0, 1, 12, 9)

[ 54](siwx91x-pinctrl_8h.md#ae6f4fe6677f66e058ce30bbd914e7f90)#define COMP1\_OUT\_PC15 SIWX91X\_GPIO(9, 5, 11, 2, 15, 9)

[ 55](siwx91x-pinctrl_8h.md#a5865a449e4957f10e35208b3a8a1e186)#define COMP1\_OUT\_ULP2 SIWX91X\_GPIO(0xFF, 5, 0xFF, 4, 0, 2)

[ 56](siwx91x-pinctrl_8h.md#a61a3d2a33b017f9b509e502fb14b5ac1)#define COMP1\_OUT\_ULP6 SIWX91X\_GPIO(0xFF, 9, 0xFF, 4, 0, 6)

[ 57](siwx91x-pinctrl_8h.md#a3de5ca3d0d7078a34cc53b5c5028d7c3)#define COMP2\_OUT\_ULP7 SIWX91X\_GPIO(0xFF, 9, 0xFF, 4, 0, 7)

58

[ 59](siwx91x-pinctrl_8h.md#a1300af1a59dd0ad3c556e1d32d81b268)#define GSPI\_CLK\_PA8 SIWX91X\_GPIO(4, 0xFF, 3, 0, 8, 0)

[ 60](siwx91x-pinctrl_8h.md#a7e99d5be166044642e27ff164c119467)#define GSPI\_CLK\_PB9 SIWX91X\_GPIO(4, 0xFF, 0, 1, 9, 0)

[ 61](siwx91x-pinctrl_8h.md#a0ddcced5522deef44c1fa0c028a1e732)#define GSPI\_CLK\_PC14 SIWX91X\_GPIO(4, 0xFF, 10, 2, 14, 0)

[ 62](siwx91x-pinctrl_8h.md#a3e3cce6828e4437cb3a68aeaf4a96ede)#define GSPI\_CLK\_PD4 SIWX91X\_GPIO(4, 0xFF, 16, 3, 4, 0)

[ 63](siwx91x-pinctrl_8h.md#a130b74b957dea8d20f3491ee96ad3342)#define GSPI\_CS0\_PA9 SIWX91X\_GPIO(4, 0xFF, 4, 0, 9, 0)

[ 64](siwx91x-pinctrl_8h.md#ab33b09217c881842dc225c02cf233cff)#define GSPI\_CS0\_PB12 SIWX91X\_GPIO(4, 0xFF, 0, 1, 12, 0)

[ 65](siwx91x-pinctrl_8h.md#aa95a75d4a0ddd513649b62bb066e0cc8)#define GSPI\_CS0\_PD1 SIWX91X\_GPIO(4, 0xFF, 13, 3, 1, 0)

[ 66](siwx91x-pinctrl_8h.md#ae15c04be2dd7a94f2fc679e17591a36d)#define GSPI\_CS0\_PD5 SIWX91X\_GPIO(4, 0xFF, 17, 3, 5, 0)

[ 67](siwx91x-pinctrl_8h.md#a9626ba5699c744a56a5965a6fdccc1dd)#define GSPI\_CS1\_PA10 SIWX91X\_GPIO(4, 0xFF, 5, 0, 10, 0)

[ 68](siwx91x-pinctrl_8h.md#ac48502b47be7f938a4f1406966d83492)#define GSPI\_CS1\_PB13 SIWX91X\_GPIO(4, 0xFF, 0, 1, 13, 0)

[ 69](siwx91x-pinctrl_8h.md#a9749ac7bb889d98d4ccd86319245c3c5)#define GSPI\_CS1\_PD2 SIWX91X\_GPIO(4, 0xFF, 14, 3, 2, 0)

[ 70](siwx91x-pinctrl_8h.md#a377c8739a609be9474b8e3b86c5badb8)#define GSPI\_CS1\_PD6 SIWX91X\_GPIO(4, 0xFF, 18, 3, 6, 0)

[ 71](siwx91x-pinctrl_8h.md#a57eda435423312d32b02b2a12a2a5e6a)#define GSPI\_CS2\_PA15 SIWX91X\_GPIO(4, 0xFF, 8, 0, 15, 0)

[ 72](siwx91x-pinctrl_8h.md#aa27854ad8c8f02fe59735b3940c28777)#define GSPI\_CS2\_PB14 SIWX91X\_GPIO(4, 0xFF, 0, 1, 14, 0)

[ 73](siwx91x-pinctrl_8h.md#ab027da2065d70da0adb1c80f6e15989d)#define GSPI\_CS2\_PD3 SIWX91X\_GPIO(4, 0xFF, 15, 3, 3, 0)

[ 74](siwx91x-pinctrl_8h.md#a659a95c1646ecd988b13c08341b19e2f)#define GSPI\_CS2\_PD7 SIWX91X\_GPIO(4, 0xFF, 19, 3, 7, 0)

[ 75](siwx91x-pinctrl_8h.md#ad9b796572ef70fc452095f180f585e8b)#define GSPI\_MISO\_PA11 SIWX91X\_GPIO(4, 0xFF, 6, 0, 11, 0)

[ 76](siwx91x-pinctrl_8h.md#aa6108694e7024270e662aff038077042)#define GSPI\_MISO\_PB10 SIWX91X\_GPIO(4, 0xFF, 0, 1, 10, 0)

[ 77](siwx91x-pinctrl_8h.md#a1e718b4545756cbc7bfba856143b8fcc)#define GSPI\_MISO\_PC15 SIWX91X\_GPIO(4, 0xFF, 11, 2, 15, 0)

[ 78](siwx91x-pinctrl_8h.md#a718e762af2c34426e2d7ee4f72756f45)#define GSPI\_MISO\_PD8 SIWX91X\_GPIO(4, 0xFF, 20, 3, 8, 0)

[ 79](siwx91x-pinctrl_8h.md#a08416fd6338ce4d19785ab0ca9f2aa3b)#define GSPI\_MOSI\_PA6 SIWX91X\_GPIO(12, 0xFF, 1, 0, 6, 0)

[ 80](siwx91x-pinctrl_8h.md#a7f949a5bc695e384399d28530fcf6367)#define GSPI\_MOSI\_PA12 SIWX91X\_GPIO(4, 0xFF, 7, 0, 12, 0)

[ 81](siwx91x-pinctrl_8h.md#a104a987c882ea4b8a39aabb754aa6a35)#define GSPI\_MOSI\_PB11 SIWX91X\_GPIO(4, 0xFF, 0, 1, 11, 0)

[ 82](siwx91x-pinctrl_8h.md#ab79328776b43a327d10ba5460fb03a14)#define GSPI\_MOSI\_PD0 SIWX91X\_GPIO(4, 0xFF, 12, 3, 0, 0)

[ 83](siwx91x-pinctrl_8h.md#a40ad31aa287c91df537f1caa595cb4f7)#define GSPI\_MOSI\_PD9 SIWX91X\_GPIO(4, 0xFF, 21, 3, 9, 0)

84

[ 85](siwx91x-pinctrl_8h.md#a843a8a1e536a19115dad9b821e09fc35)#define I2C0\_SCL\_PA7 SIWX91X\_GPIO(4, 0xFF, 2, 0, 7, 0)

[ 86](siwx91x-pinctrl_8h.md#afda900994567b6303959e4f666fceaf1)#define I2C0\_SCL\_PC0 SIWX91X\_GPIO(11, 0xFF, 9, 2, 0, 0)

[ 87](siwx91x-pinctrl_8h.md#a820c81dfce3dff2287efa78305812b7f)#define I2C0\_SCL\_ULP1 SIWX91X\_GPIO(4, 6, 23, 4, 1, 1)

[ 88](siwx91x-pinctrl_8h.md#a480ff4a4f89b88de9c46001c7ad52aed)#define I2C0\_SCL\_ULP2 SIWX91X\_GPIO(4, 6, 24, 4, 2, 2)

[ 89](siwx91x-pinctrl_8h.md#a10e1bb6b59bfb1c4ca1932f9a4be1448)#define I2C0\_SCL\_ULP11 SIWX91X\_GPIO(4, 6, 33, 4, 11, 11)

[ 90](siwx91x-pinctrl_8h.md#a0c5573f60342f026d0553797a636a488)#define I2C0\_SDA\_PA6 SIWX91X\_GPIO(4, 0xFF, 1, 0, 6, 0)

[ 91](siwx91x-pinctrl_8h.md#a0a0bc14e167d0408fbe657fa644c9671)#define I2C0\_SDA\_PB15 SIWX91X\_GPIO(11, 0xFF, 9, 1, 15, 0)

[ 92](siwx91x-pinctrl_8h.md#a54e93e8958d5eb99c63ce1ad2cf17e75)#define I2C0\_SDA\_ULP0 SIWX91X\_GPIO(4, 6, 22, 4, 0, 0)

[ 93](siwx91x-pinctrl_8h.md#a3a53a6594da3d36f4c186864275cdb47)#define I2C0\_SDA\_ULP3 SIWX91X\_GPIO(4, 6, 25, 4, 3, 3)

[ 94](siwx91x-pinctrl_8h.md#a26710ae6de0a217c2d3af4cb7cc14b28)#define I2C0\_SDA\_ULP10 SIWX91X\_GPIO(4, 6, 32, 4, 10, 10)

95

[ 96](siwx91x-pinctrl_8h.md#a284d801054db9426e439b9da5751470d)#define I2C1\_SCL\_PA6 SIWX91X\_GPIO(5, 0xFF, 1, 0, 6, 0)

[ 97](siwx91x-pinctrl_8h.md#a4c7903ca830414690e5a997c41e0b41c)#define I2C1\_SCL\_PB13 SIWX91X\_GPIO(5, 0xFF, 0, 1, 13, 0)

[ 98](siwx91x-pinctrl_8h.md#ad327d495abfaa2bb7ae3344a163f052f)#define I2C1\_SCL\_PC1 SIWX91X\_GPIO(11, 0xFF, 9, 2, 1, 0)

[ 99](siwx91x-pinctrl_8h.md#a7eb71571b0e15669fb353a0bd65f2c72)#define I2C1\_SCL\_PD2 SIWX91X\_GPIO(5, 0xFF, 14, 3, 2, 0)

[ 100](siwx91x-pinctrl_8h.md#ad391773dd3aceaa659dc4d7534c850d2)#define I2C1\_SCL\_PD6 SIWX91X\_GPIO(5, 0xFF, 18, 3, 6, 0)

[ 101](siwx91x-pinctrl_8h.md#aa79263584dd8d9ccd4ae7564cbb50fd7)#define I2C1\_SCL\_ULP0 SIWX91X\_GPIO(5, 6, 22, 4, 0, 0)

[ 102](siwx91x-pinctrl_8h.md#a1f40c8c4305f357477f61f2bee4177aa)#define I2C1\_SCL\_ULP2 SIWX91X\_GPIO(5, 6, 24, 4, 2, 2)

[ 103](siwx91x-pinctrl_8h.md#a34ac7a645ee7c80f1d291348bdaddb1b)#define I2C1\_SCL\_ULP6 SIWX91X\_GPIO(5, 6, 28, 4, 6, 6)

[ 104](siwx91x-pinctrl_8h.md#a8f48385a7b4ee0bc5ce9befb666df611)#define I2C1\_SDA\_PA7 SIWX91X\_GPIO(5, 0xFF, 2, 0, 7, 0)

[ 105](siwx91x-pinctrl_8h.md#aad8f6af7378207d92fd107d223289b91)#define I2C1\_SDA\_PB14 SIWX91X\_GPIO(5, 0xFF, 0, 1, 14, 0)

[ 106](siwx91x-pinctrl_8h.md#af3ba02992276ed2088a6652b695d270d)#define I2C1\_SDA\_PC2 SIWX91X\_GPIO(11, 0xFF, 9, 2, 2, 0)

[ 107](siwx91x-pinctrl_8h.md#a77b0c5734afd5123fd3ae520f10a8da8)#define I2C1\_SDA\_PD3 SIWX91X\_GPIO(5, 0xFF, 15, 3, 3, 0)

[ 108](siwx91x-pinctrl_8h.md#af8a91c084318e2934db326dee1baaa36)#define I2C1\_SDA\_PD7 SIWX91X\_GPIO(5, 0xFF, 19, 3, 7, 0)

[ 109](siwx91x-pinctrl_8h.md#adc989b20626192997d54961dd616b3b2)#define I2C1\_SDA\_ULP1 SIWX91X\_GPIO(5, 6, 23, 4, 1, 1)

[ 110](siwx91x-pinctrl_8h.md#af66e09c1a67eeae142148952ffc620cb)#define I2C1\_SDA\_ULP3 SIWX91X\_GPIO(5, 6, 25, 4, 3, 3)

[ 111](siwx91x-pinctrl_8h.md#a187fb1dd9e7f233059c7602205112d62)#define I2C1\_SDA\_ULP7 SIWX91X\_GPIO(5, 6, 29, 4, 7, 7)

112

[ 113](siwx91x-pinctrl_8h.md#a2f6c3d36662578e109bb825eac6e1782)#define I2S0\_CLK\_PA8 SIWX91X\_GPIO(7, 0xFF, 3, 0, 8, 0)

[ 114](siwx91x-pinctrl_8h.md#a97571813242b8e4231d5d7eb65f65f6b)#define I2S0\_CLK\_PB9 SIWX91X\_GPIO(7, 0xFF, 0, 1, 9, 0)

[ 115](siwx91x-pinctrl_8h.md#a898415db8ffedbd3c66238be5664cde2)#define I2S0\_CLK\_PC14 SIWX91X\_GPIO(7, 0xFF, 10, 2, 14, 0)

[ 116](siwx91x-pinctrl_8h.md#a4bc4e36471daeb3e94c42d004e9e2034)#define I2S0\_CLK\_PD4 SIWX91X\_GPIO(7, 0xFF, 16, 3, 4, 0)

[ 117](siwx91x-pinctrl_8h.md#addc8601653dd7d28e5b5e7cf36bd9d08)#define I2S0\_DIN0\_PA10 SIWX91X\_GPIO(7, 0xFF, 5, 0, 10, 0)

[ 118](siwx91x-pinctrl_8h.md#a8c4ff10eb41b1977ed6eb891cd2ac892)#define I2S0\_DIN0\_PB11 SIWX91X\_GPIO(7, 0xFF, 0, 1, 11, 0)

[ 119](siwx91x-pinctrl_8h.md#a7efd8d45e0f8b5d01ef6b9dc2fca1e86)#define I2S0\_DIN0\_PD0 SIWX91X\_GPIO(7, 0xFF, 12, 3, 0, 0)

[ 120](siwx91x-pinctrl_8h.md#af83cda4dd90f3cb1ea2bef943c370c60)#define I2S0\_DIN0\_PD8 SIWX91X\_GPIO(7, 0xFF, 20, 3, 8, 0)

[ 121](siwx91x-pinctrl_8h.md#ab72219b605a2a595ed0977e55af6d57b)#define I2S0\_DIN1\_PA6 SIWX91X\_GPIO(7, 0xFF, 1, 0, 6, 0)

[ 122](siwx91x-pinctrl_8h.md#a7060b6e3a6f9080d54e85925cb89674b)#define I2S0\_DIN1\_PB13 SIWX91X\_GPIO(7, 0xFF, 0, 1, 13, 0)

[ 123](siwx91x-pinctrl_8h.md#a86393f3e7d343f9012042811e0c65233)#define I2S0\_DIN1\_PD2 SIWX91X\_GPIO(7, 0xFF, 14, 3, 2, 0)

[ 124](siwx91x-pinctrl_8h.md#abd0a05def8b059a2c357c960409e51c2)#define I2S0\_DIN1\_PD6 SIWX91X\_GPIO(7, 0xFF, 18, 3, 6, 0)

[ 125](siwx91x-pinctrl_8h.md#abffc60933f8b319a1a410ac2b198bf3d)#define I2S0\_DOUT0\_PA11 SIWX91X\_GPIO(7, 0xFF, 6, 0, 11, 0)

[ 126](siwx91x-pinctrl_8h.md#a33dbe2b76dfbb7b699cb06c93b85b1db)#define I2S0\_DOUT0\_PB12 SIWX91X\_GPIO(7, 0xFF, 0, 1, 12, 0)

[ 127](siwx91x-pinctrl_8h.md#a580ae7bf72656ab844f18f68be43f5fa)#define I2S0\_DOUT0\_PD1 SIWX91X\_GPIO(7, 0xFF, 13, 3, 1, 0)

[ 128](siwx91x-pinctrl_8h.md#ab0596323387158c95aa848d6bfb4535d)#define I2S0\_DOUT0\_PD9 SIWX91X\_GPIO(7, 0xFF, 21, 3, 9, 0)

[ 129](siwx91x-pinctrl_8h.md#a8ff6efe876472943d0762741a187dc55)#define I2S0\_DOUT1\_PA7 SIWX91X\_GPIO(7, 0xFF, 2, 0, 7, 0)

[ 130](siwx91x-pinctrl_8h.md#a9c617b2d8b50358c7942666d0d270eca)#define I2S0\_DOUT1\_PB13 SIWX91X\_GPIO(7, 0xFF, 0, 1, 14, 0)

[ 131](siwx91x-pinctrl_8h.md#abc115fb0093c0b7ad7f28c77ac303365)#define I2S0\_DOUT1\_PD3 SIWX91X\_GPIO(7, 0xFF, 15, 3, 3, 0)

[ 132](siwx91x-pinctrl_8h.md#ac6a2d2d61586fa5977e2abfdb28c8139)#define I2S0\_DOUT1\_PD7 SIWX91X\_GPIO(7, 0xFF, 19, 3, 7, 0)

[ 133](siwx91x-pinctrl_8h.md#afd55745b07c0d616b61bcb9cc76954a6)#define I2S0\_WS\_PA9 SIWX91X\_GPIO(7, 0xFF, 4, 0, 9, 0)

[ 134](siwx91x-pinctrl_8h.md#a7212b0840c7c7a981ca580c00fdc46b2)#define I2S0\_WS\_PB10 SIWX91X\_GPIO(7, 0xFF, 0, 1, 10, 0)

[ 135](siwx91x-pinctrl_8h.md#a6beaa237e25b31870635f72beddae60a)#define I2S0\_WS\_PC15 SIWX91X\_GPIO(7, 0xFF, 11, 2, 15, 0)

[ 136](siwx91x-pinctrl_8h.md#aa991356f01f1b28195087a12b2c355b1)#define I2S0\_WS\_PD5 SIWX91X\_GPIO(7, 0xFF, 17, 3, 5, 0)

137

[ 138](siwx91x-pinctrl_8h.md#aa3a4e7ba7797a8ed887898c506a561c4)#define IR\_INPUT\_PA15 SIWX91X\_GPIO(9, 1, 8, 0, 15, 7)

[ 139](siwx91x-pinctrl_8h.md#afce4949efe81a6e2bd615930e1653627)#define IR\_INPUT\_PB10 SIWX91X\_GPIO(11, 1, 0, 1, 10, 7)

[ 140](siwx91x-pinctrl_8h.md#a7849ff55b05a4974d54ae77058117d31)#define IR\_INPUT\_PB13 SIWX91X\_GPIO(11, 4, 0, 1, 13, 10)

[ 141](siwx91x-pinctrl_8h.md#a783673ec44db6d55f6461e016745577a)#define IR\_INPUT\_PD0 SIWX91X\_GPIO(9, 4, 12, 3, 0, 10)

[ 142](siwx91x-pinctrl_8h.md#a0d995f35796fc445efe7ebee649bdf2f)#define IR\_INPUT\_ULP4 SIWX91X\_GPIO(0xFF, 10, 0xFF, 4, 0, 4)

[ 143](siwx91x-pinctrl_8h.md#aadd97a3fa547212bd510340b3ab05c2d)#define IR\_INPUT\_ULP7 SIWX91X\_GPIO(0xFF, 1, 0xFF, 4, 0, 7)

[ 144](siwx91x-pinctrl_8h.md#a4c3793bc7cc985cf1f80aef136d18ce2)#define IR\_INPUT\_ULP10 SIWX91X\_GPIO(0xFF, 4, 0xFF, 4, 0, 10)

[ 145](siwx91x-pinctrl_8h.md#a3c20f9e92c86f43ff6d11d06003575f2)#define IR\_OUTPUT\_PA11 SIWX91X\_GPIO(9, 1, 6, 0, 11, 5)

[ 146](siwx91x-pinctrl_8h.md#adb645e594a5654f35cbd3e852445e19b)#define IR\_OUTPUT\_ULP5 SIWX91X\_GPIO(0xFF, 1, 0xFF, 4, 0, 5)

147

[ 148](siwx91x-pinctrl_8h.md#ab31495e57399add2389a06b047f6f825)#define PMU\_TEST1\_PA6 SIWX91X\_GPIO(8, 0xFF, 1, 0, 6, 0)

[ 149](siwx91x-pinctrl_8h.md#a1ebe19b9b16457666b639fd0e25b30b4)#define PMU\_TEST1\_PB13 SIWX91X\_GPIO(8, 0xFF, 0, 1, 13, 0)

[ 150](siwx91x-pinctrl_8h.md#a41779d3165b31ebf9ecb8cb4ca037be6)#define PMU\_TEST1\_PB14 SIWX91X\_GPIO(12, 0xFF, 0, 1, 14, 0)

[ 151](siwx91x-pinctrl_8h.md#a4055f713ecf4e2f57c49c57321fdff99)#define PMU\_TEST1\_ULP0 SIWX91X\_GPIO(13, 6, 22, 4, 0, 0)

[ 152](siwx91x-pinctrl_8h.md#a60de9f9f3085bee8341e118462a7fdcf)#define PMU\_TEST1\_ULP2 SIWX91X\_GPIO(10, 6, 24, 4, 2, 2)

[ 153](siwx91x-pinctrl_8h.md#ae687c8d547e498569a8b23f419216262)#define PMU\_TEST1\_ULP6 SIWX91X\_GPIO(12, 6, 28, 4, 6, 6)

[ 154](siwx91x-pinctrl_8h.md#a4cee250941565f3e3eb36b6d0a4e3364)#define PMU\_TEST1\_ULP10 SIWX91X\_GPIO(10, 6, 32, 4, 10, 10)

[ 155](siwx91x-pinctrl_8h.md#abbc697fb4246a3a5fc6b1282799f597d)#define PMU\_TEST2\_PA7 SIWX91X\_GPIO(8, 0xFF, 2, 0, 7, 0)

[ 156](siwx91x-pinctrl_8h.md#ad9727c58b703671e1b743796af11c76f)#define PMU\_TEST2\_PB14 SIWX91X\_GPIO(8, 0xFF, 0, 1, 14, 0)

[ 157](siwx91x-pinctrl_8h.md#ad3cdee5e821dc5b3c68e45ec4b49bfbe)#define PMU\_TEST2\_ULP1 SIWX91X\_GPIO(13, 6, 23, 4, 1, 1)

[ 158](siwx91x-pinctrl_8h.md#a9eae278334a605347f6e95e9250cc7e7)#define PMU\_TEST2\_ULP3 SIWX91X\_GPIO(10, 6, 25, 4, 3, 3)

[ 159](siwx91x-pinctrl_8h.md#a0510f2e9687d07fe386be8718198990c)#define PMU\_TEST2\_ULP7 SIWX91X\_GPIO(12, 6, 29, 4, 7, 7)

[ 160](siwx91x-pinctrl_8h.md#a810fcca28118ef6dff963923b9af34d9)#define PMU\_TEST2\_ULP11 SIWX91X\_GPIO(10, 6, 33, 4, 11, 11)

161

[ 162](siwx91x-pinctrl_8h.md#a8a0b414ea88a316f87fafaeeabd342c0)#define PSRAM\_CLK\_PC14 SIWX91X\_GPIO(11, 0xFF, 10, 2, 14, 0)

[ 163](siwx91x-pinctrl_8h.md#a132dda706d00bcf37398d20d476e4b8b)#define PSRAM\_CLK\_PD4 SIWX91X\_GPIO(12, 0xFF, 16, 3, 4, 0)

[ 164](siwx91x-pinctrl_8h.md#a5586f0ff8a62717e06f55214dfa91ed3)#define PSRAM\_CSN0\_PD1 SIWX91X\_GPIO(11, 0xFF, 13, 3, 1, 0)

[ 165](siwx91x-pinctrl_8h.md#a4db365fa4ef7468b21c567840b70cb5a)#define PSRAM\_CSN0\_PD7 SIWX91X\_GPIO(12, 0xFF, 19, 3, 7, 0)

[ 166](siwx91x-pinctrl_8h.md#a81a9f7387e370d96e459318255a59f53)#define PSRAM\_CSN1\_PD5 SIWX91X\_GPIO(11, 0xFF, 17, 3, 5, 0)

[ 167](siwx91x-pinctrl_8h.md#af73ccedf7341424eb2be6a063193bad3)#define PSRAM\_D0\_PC15 SIWX91X\_GPIO(11, 0xFF, 11, 2, 15, 0)

[ 168](siwx91x-pinctrl_8h.md#ab69da07d2cbd1bf3883edce6caa364a6)#define PSRAM\_D0\_PD5 SIWX91X\_GPIO(12, 0xFF, 17, 3, 5, 0)

[ 169](siwx91x-pinctrl_8h.md#a4f99f7ba4e3753ab3f2e42414afb808a)#define PSRAM\_D1\_PD0 SIWX91X\_GPIO(11, 0xFF, 12, 3, 0, 0)

[ 170](siwx91x-pinctrl_8h.md#a6ee363292bf76d896eb54486baec9d35)#define PSRAM\_D1\_PD6 SIWX91X\_GPIO(12, 0xFF, 18, 3, 6, 0)

[ 171](siwx91x-pinctrl_8h.md#ae955ae59f89119f1a338d2a7edf1bf4f)#define PSRAM\_D2\_PD2 SIWX91X\_GPIO(11, 0xFF, 14, 3, 2, 0)

[ 172](siwx91x-pinctrl_8h.md#a44b73a4e807137aba144b090fe53f5e8)#define PSRAM\_D2\_PD8 SIWX91X\_GPIO(12, 0xFF, 20, 3, 8, 0)

[ 173](siwx91x-pinctrl_8h.md#ad9c347f86dbb34edb2972aa2f1363a4e)#define PSRAM\_D3\_PD3 SIWX91X\_GPIO(11, 0xFF, 15, 3, 3, 0)

[ 174](siwx91x-pinctrl_8h.md#a8263e2451bab49cc8470372949e5e80b)#define PSRAM\_D3\_PD9 SIWX91X\_GPIO(12, 0xFF, 21, 3, 9, 0)

[ 175](siwx91x-pinctrl_8h.md#a19735dded6e686be4102c94388494863)#define PSRAM\_D4\_PD6 SIWX91X\_GPIO(11, 0xFF, 18, 3, 6, 0)

[ 176](siwx91x-pinctrl_8h.md#aebadedeab23ab87842144bf605dfc275)#define PSRAM\_D5\_PD7 SIWX91X\_GPIO(11, 0xFF, 19, 3, 7, 0)

[ 177](siwx91x-pinctrl_8h.md#a86104348f1b9ab055359de402db4c3d7)#define PSRAM\_D6\_PD8 SIWX91X\_GPIO(11, 0xFF, 20, 3, 8, 0)

[ 178](siwx91x-pinctrl_8h.md#a6d749aeed541a8883acb852a2a7c6acb)#define PSRAM\_D7\_PD9 SIWX91X\_GPIO(11, 0xFF, 21, 3, 9, 0)

179

[ 180](siwx91x-pinctrl_8h.md#ac090b3b61ad792689a2fc48d8e43af03)#define PWM\_1H\_PA7 SIWX91X\_GPIO(10, 0xFF, 2, 0, 7, 0)

[ 181](siwx91x-pinctrl_8h.md#a630ec4cefb7359d15a36c4a1134ab636)#define PWM\_1H\_ULP1 SIWX91X\_GPIO(12, 6, 23, 4, 1, 1)

[ 182](siwx91x-pinctrl_8h.md#a27ce9daabeec74cce9aaeaa69777348c)#define PWM\_1L\_PA6 SIWX91X\_GPIO(10, 0xFF, 1, 0, 6, 0)

[ 183](siwx91x-pinctrl_8h.md#a61eae9cf8f585a2990f7067cb6619b4a)#define PWM\_1L\_ULP0 SIWX91X\_GPIO(12, 6, 22, 4, 0, 0)

[ 184](siwx91x-pinctrl_8h.md#ae17700c8b8340cf07c6366c14ee3d01c)#define PWM\_2H\_PA9 SIWX91X\_GPIO(10, 0xFF, 4, 0, 9, 0)

[ 185](siwx91x-pinctrl_8h.md#a66884ae3158f869bdf7e4e1d1dae10eb)#define PWM\_2H\_ULP3 SIWX91X\_GPIO(8, 6, 25, 4, 3, 3)

[ 186](siwx91x-pinctrl_8h.md#abf08c72c301bfd555f41e34b99f2076e)#define PWM\_2H\_ULP5 SIWX91X\_GPIO(12, 6, 27, 4, 5, 5)

[ 187](siwx91x-pinctrl_8h.md#afcb3174ce28fd069d90861d00defe992)#define PWM\_2L\_PA8 SIWX91X\_GPIO(10, 0xFF, 3, 0, 8, 0)

[ 188](siwx91x-pinctrl_8h.md#a65fe159ea9b1427a355fb332af129f14)#define PWM\_2L\_ULP2 SIWX91X\_GPIO(8, 6, 24, 4, 2, 2)

[ 189](siwx91x-pinctrl_8h.md#ac8708b22008c4408a38456f7b8258328)#define PWM\_2L\_ULP4 SIWX91X\_GPIO(12, 6, 26, 4, 4, 4)

[ 190](siwx91x-pinctrl_8h.md#a9662f00af65973258e9a98ac0b9e18a0)#define PWM\_3H\_PA11 SIWX91X\_GPIO(10, 0xFF, 6, 0, 11, 0)

[ 191](siwx91x-pinctrl_8h.md#a06cd7beccdd8bfaeaad10dce0aa8db03)#define PWM\_3H\_ULP5 SIWX91X\_GPIO(8, 6, 27, 4, 5, 5)

[ 192](siwx91x-pinctrl_8h.md#a3dd6cf2b9074ec02fd886d6ab8d4ea4c)#define PWM\_3L\_PA10 SIWX91X\_GPIO(10, 0xFF, 5, 0, 10, 0)

[ 193](siwx91x-pinctrl_8h.md#aba2dcc0b4ebec0dccdff1af957309066)#define PWM\_3L\_ULP4 SIWX91X\_GPIO(8, 6, 26, 4, 4, 4)

[ 194](siwx91x-pinctrl_8h.md#ac134df7ccba4624b613b3142c42dbbe4)#define PWM\_4H\_PA15 SIWX91X\_GPIO(10, 0xFF, 8, 0, 15, 0)

[ 195](siwx91x-pinctrl_8h.md#a70ed321c11ee1781a15458f9fefbc70a)#define PWM\_4H\_ULP7 SIWX91X\_GPIO(8, 6, 29, 4, 7, 7)

[ 196](siwx91x-pinctrl_8h.md#a7825839d7da0495866efc75546ba8af9)#define PWM\_4L\_PA12 SIWX91X\_GPIO(10, 0xFF, 7, 0, 12, 0)

[ 197](siwx91x-pinctrl_8h.md#a817ac5253d020277a66f631649340587)#define PWM\_4L\_ULP6 SIWX91X\_GPIO(8, 6, 28, 4, 6, 6)

[ 198](siwx91x-pinctrl_8h.md#a5daf0e15fc8cdf3ac39ab82546a498dc)#define PWM\_EXTTRIG1\_PB11 SIWX91X\_GPIO(10, 0xFF, 0, 1, 11, 0)

[ 199](siwx91x-pinctrl_8h.md#a789d65fc45c20682c3fef06270c2ebcc)#define PWM\_EXTTRIG1\_PD3 SIWX91X\_GPIO(8, 0xFF, 15, 3, 3, 0)

[ 200](siwx91x-pinctrl_8h.md#af8b0f205794d8aa23e4e3befecdc4e60)#define PWM\_EXTTRIG1\_ULP6 SIWX91X\_GPIO(10, 6, 28, 4, 6, 6)

[ 201](siwx91x-pinctrl_8h.md#a9bf84673800f4bda297596990775120b)#define PWM\_EXTTRIG1\_ULP11 SIWX91X\_GPIO(8, 6, 33, 4, 11, 11)

[ 202](siwx91x-pinctrl_8h.md#a750a5aae34aa7596dbfd1416d5f0974f)#define PWM\_EXTTRIG2\_PB12 SIWX91X\_GPIO(10, 0xFF, 0, 1, 12, 0)

[ 203](siwx91x-pinctrl_8h.md#a18078aa0c4cd86d814e9daa25dfd5d8f)#define PWM\_EXTTRIG2\_PD6 SIWX91X\_GPIO(8, 0xFF, 18, 3, 6, 0)

[ 204](siwx91x-pinctrl_8h.md#acb9a77a0695c53748a3108765202aa01)#define PWM\_EXTTRIG2\_ULP7 SIWX91X\_GPIO(10, 6, 29, 4, 7, 7)

[ 205](siwx91x-pinctrl_8h.md#accfea9cdf3bf894d97f01d99964c6d85)#define PWM\_EXTTRIG3\_PB13 SIWX91X\_GPIO(10, 0xFF, 0, 1, 13, 0)

[ 206](siwx91x-pinctrl_8h.md#a7a82ec4a0f68af8dba90a6caabaaca51)#define PWM\_EXTTRIG3\_PD7 SIWX91X\_GPIO(8, 0xFF, 19, 3, 7, 0)

[ 207](siwx91x-pinctrl_8h.md#af6a89549fc2fc6d1ba1ccd2bb6a3390e)#define PWM\_EXTTRIG3\_ULP8 SIWX91X\_GPIO(10, 6, 30, 4, 8, 8)

[ 208](siwx91x-pinctrl_8h.md#a42bacec667bd31bb4861af39ddbc48a8)#define PWM\_EXTTRIG4\_PB14 SIWX91X\_GPIO(10, 0xFF, 0, 1, 14, 0)

[ 209](siwx91x-pinctrl_8h.md#a3d3275c7f4aecddef09d0edd4253c638)#define PWM\_EXTTRIG4\_PD2 SIWX91X\_GPIO(8, 0xFF, 14, 3, 2, 0)

[ 210](siwx91x-pinctrl_8h.md#aa4e1418e9226b34ac556f374694db689)#define PWM\_EXTTRIG4\_ULP9 SIWX91X\_GPIO(10, 6, 31, 4, 9, 9)

[ 211](siwx91x-pinctrl_8h.md#a91a12aaaab3fbbb863f8d7e631735a61)#define PWM\_FAULTA\_PB9 SIWX91X\_GPIO(10, 0xFF, 0, 1, 9, 0)

[ 212](siwx91x-pinctrl_8h.md#a1be2559bbd5c14e4b8d02fae6d834db3)#define PWM\_FAULTA\_ULP4 SIWX91X\_GPIO(10, 6, 26, 4, 4, 4)

[ 213](siwx91x-pinctrl_8h.md#a898809d281a1451c860755372034ac14)#define PWM\_FAULTA\_ULP9 SIWX91X\_GPIO(8, 6, 31, 4, 9, 9)

[ 214](siwx91x-pinctrl_8h.md#ae4235cbf5a68687eebdefed5de68d383)#define PWM\_FAULTB\_PB10 SIWX91X\_GPIO(10, 0xFF, 0, 1, 10, 0)

[ 215](siwx91x-pinctrl_8h.md#ad631deeca8cc40fcc2df48ec50297c9f)#define PWM\_FAULTB\_ULP5 SIWX91X\_GPIO(10, 6, 27, 4, 5, 5)

[ 216](siwx91x-pinctrl_8h.md#a4bfb8e85f37893aceed66e457c34b9bd)#define PWM\_FAULTB\_ULP10 SIWX91X\_GPIO(8, 6, 32, 4, 10, 10)

[ 217](siwx91x-pinctrl_8h.md#a4f0903ae305c9bf1a9808b139a537a5d)#define PWM\_SLEEPEVENT\_ULP8 SIWX91X\_GPIO(8, 6, 30, 4, 8, 8)

218

[ 219](siwx91x-pinctrl_8h.md#ac212850e52f0103098017a467444c35c)#define QEI\_DIR\_PA11 SIWX91X\_GPIO(5, 0xFF, 6, 0, 11, 0)

[ 220](siwx91x-pinctrl_8h.md#aad151581b78fe894b7cc517d80e23bd2)#define QEI\_DIR\_PB12 SIWX91X\_GPIO(5, 0xFF, 0, 1, 12, 0)

[ 221](siwx91x-pinctrl_8h.md#a0671890b46ea10a6d8e26030eb54f9ee)#define QEI\_DIR\_PC2 SIWX91X\_GPIO(13, 0xFF, 9, 2, 2, 0)

[ 222](siwx91x-pinctrl_8h.md#ab5f649c37016091c451238c5f004f530)#define QEI\_DIR\_PD1 SIWX91X\_GPIO(3, 0xFF, 13, 3, 1, 0)

[ 223](siwx91x-pinctrl_8h.md#afff421072b5e7b3ff8ae8563ed6a3b49)#define QEI\_DIR\_PD9 SIWX91X\_GPIO(5, 0xFF, 21, 3, 9, 0)

[ 224](siwx91x-pinctrl_8h.md#a6be591b8ce2f422f66e10e7c1591e835)#define QEI\_DIR\_ULP3 SIWX91X\_GPIO(3, 6, 25, 4, 3, 3)

[ 225](siwx91x-pinctrl_8h.md#a0d53fec86fc5cd9aa5b094d0f6e8229b)#define QEI\_DIR\_ULP7 SIWX91X\_GPIO(3, 6, 29, 4, 7, 7)

[ 226](siwx91x-pinctrl_8h.md#a6bcd0fd50eb5acfbd616b96a041a8b40)#define QEI\_DIR\_ULP11 SIWX91X\_GPIO(3, 6, 33, 4, 11, 11)

[ 227](siwx91x-pinctrl_8h.md#a0fccfc009742a9cb952064ea09f11f45)#define QEI\_IDX\_PA8 SIWX91X\_GPIO(5, 0xFF, 3, 0, 8, 0)

[ 228](siwx91x-pinctrl_8h.md#a9cb2d4852a19d19e2e4694498f35466b)#define QEI\_IDX\_PB15 SIWX91X\_GPIO(13, 0xFF, 9, 1, 15, 0)

[ 229](siwx91x-pinctrl_8h.md#ad701cbeee3f3eb5fa06c548bcc45130e)#define QEI\_IDX\_PB9 SIWX91X\_GPIO(5, 0xFF, 0, 1, 9, 0)

[ 230](siwx91x-pinctrl_8h.md#a0acdeab84f404f6be790c63399d96d24)#define QEI\_IDX\_PC14 SIWX91X\_GPIO(3, 0xFF, 10, 2, 14, 0)

[ 231](siwx91x-pinctrl_8h.md#ac97f9482c77fcff95a3bd830f8fd6eea)#define QEI\_IDX\_PD4 SIWX91X\_GPIO(5, 0xFF, 16, 3, 4, 0)

[ 232](siwx91x-pinctrl_8h.md#aa5571fa3facfca9e58accb575a8aa14b)#define QEI\_IDX\_ULP0 SIWX91X\_GPIO(3, 6, 22, 4, 0, 0)

[ 233](siwx91x-pinctrl_8h.md#a5e4085d82f00810d0d8a0c79bae2fb8b)#define QEI\_IDX\_ULP4 SIWX91X\_GPIO(3, 6, 26, 4, 4, 4)

[ 234](siwx91x-pinctrl_8h.md#ade023149f5a2daf2c21d2a5b8db31ebf)#define QEI\_IDX\_ULP8 SIWX91X\_GPIO(3, 6, 30, 4, 8, 8)

[ 235](siwx91x-pinctrl_8h.md#a569877d717e03939e782f0850017ff7b)#define QEI\_PHA\_PA9 SIWX91X\_GPIO(5, 0xFF, 4, 0, 9, 0)

[ 236](siwx91x-pinctrl_8h.md#ad1dadc24862d40766c6bb6c3d37eda25)#define QEI\_PHA\_PB10 SIWX91X\_GPIO(5, 0xFF, 0, 1, 10, 0)

[ 237](siwx91x-pinctrl_8h.md#afe674d8febc82de54be9a541728a08c2)#define QEI\_PHA\_PC0 SIWX91X\_GPIO(13, 0xFF, 9, 2, 0, 0)

[ 238](siwx91x-pinctrl_8h.md#a2eb9564e6ef78f72ec065eb23be498e7)#define QEI\_PHA\_PC15 SIWX91X\_GPIO(3, 0xFF, 11, 2, 15, 0)

[ 239](siwx91x-pinctrl_8h.md#a574253b2f0253e1d93af18257b362f91)#define QEI\_PHA\_PD5 SIWX91X\_GPIO(5, 0xFF, 17, 3, 5, 0)

[ 240](siwx91x-pinctrl_8h.md#a02cd57249ab4cbe4ac6f50bf4ac4640d)#define QEI\_PHA\_ULP1 SIWX91X\_GPIO(3, 6, 23, 4, 1, 1)

[ 241](siwx91x-pinctrl_8h.md#a05d2c45f5f6f8e6caa749fa62f8952d2)#define QEI\_PHA\_ULP5 SIWX91X\_GPIO(3, 6, 27, 4, 5, 5)

[ 242](siwx91x-pinctrl_8h.md#a4e7d6e023c35e3c9afe66dea3c777f2f)#define QEI\_PHA\_ULP9 SIWX91X\_GPIO(3, 6, 31, 4, 9, 9)

[ 243](siwx91x-pinctrl_8h.md#ae1dc98ac945251534ae61b66ad1c0c8f)#define QEI\_PHB\_PA10 SIWX91X\_GPIO(5, 0xFF, 5, 0, 10, 0)

[ 244](siwx91x-pinctrl_8h.md#a2146c2841119c7b81321a687023ad738)#define QEI\_PHB\_PB11 SIWX91X\_GPIO(5, 0xFF, 0, 1, 11, 0)

[ 245](siwx91x-pinctrl_8h.md#a8f0ca387064938589676f025821fd3db)#define QEI\_PHB\_PC1 SIWX91X\_GPIO(13, 0xFF, 9, 2, 1, 0)

[ 246](siwx91x-pinctrl_8h.md#afc68cf53acf16eae32cc0e38757dab71)#define QEI\_PHB\_PD0 SIWX91X\_GPIO(3, 0xFF, 12, 3, 0, 0)

[ 247](siwx91x-pinctrl_8h.md#a658c951797ebc11423b6d06c6e9ea732)#define QEI\_PHB\_PD8 SIWX91X\_GPIO(5, 0xFF, 20, 3, 8, 0)

[ 248](siwx91x-pinctrl_8h.md#af323d2f63b6a1e26b9aa05a64c74ffbf)#define QEI\_PHB\_ULP2 SIWX91X\_GPIO(3, 6, 24, 4, 2, 2)

[ 249](siwx91x-pinctrl_8h.md#addcd05ab910922d7924bf01b643bec87)#define QEI\_PHB\_ULP6 SIWX91X\_GPIO(3, 6, 28, 4, 6, 6)

[ 250](siwx91x-pinctrl_8h.md#a2b7eafbd2fdae8fc813ebebbd912539b)#define QEI\_PHB\_ULP10 SIWX91X\_GPIO(3, 6, 32, 4, 10, 10)

251

[ 252](siwx91x-pinctrl_8h.md#a633e8141bb1feddf1decdeba91334e1e)#define QSPI\_CLK\_PA8 SIWX91X\_GPIO(11, 0xFF, 3, 0, 8, 0)

[ 253](siwx91x-pinctrl_8h.md#ac5dac4a90ee677e2845998d33ee91f27)#define QSPI\_CLK\_PC14 SIWX91X\_GPIO(1, 0xFF, 10, 2, 14, 0)

[ 254](siwx91x-pinctrl_8h.md#a4449d3df85a589e5e9ef9385ab8a7a41)#define QSPI\_CLK\_PD4 SIWX91X\_GPIO(9, 0xFF, 16, 3, 4, 0)

[ 255](siwx91x-pinctrl_8h.md#ab4f5c4b7ae07bf4a13c2d76c0b2932c8)#define QSPI\_CSN0\_PA7 SIWX91X\_GPIO(11, 0xFF, 2, 0, 7, 0)

[ 256](siwx91x-pinctrl_8h.md#a414c83c18295ef0f22f9df2992fdbb61)#define QSPI\_CSN0\_PD1 SIWX91X\_GPIO(1, 0xFF, 13, 3, 1, 0)

[ 257](siwx91x-pinctrl_8h.md#adb95a17f82a82d1c3ef552681e42978a)#define QSPI\_CSN0\_PD7 SIWX91X\_GPIO(9, 0xFF, 19, 3, 7, 0)

[ 258](siwx91x-pinctrl_8h.md#afaf0d9dd99eea0ee67f4746426c6d28d)#define QSPI\_CSN1\_PA7 SIWX91X\_GPIO(12, 0xFF, 2, 0, 7, 0)

[ 259](siwx91x-pinctrl_8h.md#a1e386c007addc69a254bdee78c362b8a)#define QSPI\_CSN1\_PD5 SIWX91X\_GPIO(1, 0xFF, 17, 3, 5, 0)

[ 260](siwx91x-pinctrl_8h.md#a3ce29c8cf549277eb26b456ec37bb668)#define QSPI\_CSN9\_PD1 SIWX91X\_GPIO(10, 0xFF, 13, 3, 1, 0)

[ 261](siwx91x-pinctrl_8h.md#a1ca5b18a10a91fe99027a7bb6d93e7c9)#define QSPI\_D0\_PA6 SIWX91X\_GPIO(11, 0xFF, 1, 0, 6, 0)

[ 262](siwx91x-pinctrl_8h.md#ab0ae659323d63123c729fa91f96f7005)#define QSPI\_D0\_PC15 SIWX91X\_GPIO(1, 0xFF, 11, 2, 15, 0)

[ 263](siwx91x-pinctrl_8h.md#ad3d60da33459ddcd3ea799d9042c48e6)#define QSPI\_D0\_PD5 SIWX91X\_GPIO(9, 0xFF, 17, 3, 5, 0)

[ 264](siwx91x-pinctrl_8h.md#adf50c45730aa83c564f1f3cf21aed277)#define QSPI\_D1\_PA9 SIWX91X\_GPIO(11, 0xFF, 4, 0, 9, 0)

[ 265](siwx91x-pinctrl_8h.md#a0d68a0d43f14f05e991259f48c7dc47f)#define QSPI\_D1\_PD0 SIWX91X\_GPIO(1, 0xFF, 12, 3, 0, 0)

[ 266](siwx91x-pinctrl_8h.md#aa35f97b4e2df7b4a41f8b36de845bffb)#define QSPI\_D1\_PD6 SIWX91X\_GPIO(9, 0xFF, 18, 3, 6, 0)

[ 267](siwx91x-pinctrl_8h.md#ac2f103b446d30be35b60e25174068d23)#define QSPI\_D2\_PA10 SIWX91X\_GPIO(11, 0xFF, 5, 0, 10, 0)

[ 268](siwx91x-pinctrl_8h.md#abeaca0e093f3681df47b15a1ed66fdd4)#define QSPI\_D2\_PD2 SIWX91X\_GPIO(1, 0xFF, 14, 3, 2, 0)

[ 269](siwx91x-pinctrl_8h.md#a3193b526e56bb7c814538f55d59f9a74)#define QSPI\_D2\_PD8 SIWX91X\_GPIO(9, 0xFF, 20, 3, 8, 0)

[ 270](siwx91x-pinctrl_8h.md#ace7f5ce16e790faa39efe698f0a2f45e)#define QSPI\_D3\_PA11 SIWX91X\_GPIO(11, 0xFF, 6, 0, 11, 0)

[ 271](siwx91x-pinctrl_8h.md#aa7fcdba14e3c4a7495f014176a8d52c1)#define QSPI\_D3\_PD3 SIWX91X\_GPIO(1, 0xFF, 15, 3, 3, 0)

[ 272](siwx91x-pinctrl_8h.md#a77463eb3366a96afb3465ae299d04043)#define QSPI\_D3\_PD9 SIWX91X\_GPIO(9, 0xFF, 21, 3, 9, 0)

[ 273](siwx91x-pinctrl_8h.md#ad614a9ad62cf0fd2f675bdb2e0c84d94)#define QSPI\_D4\_PD6 SIWX91X\_GPIO(1, 0xFF, 18, 3, 6, 0)

[ 274](siwx91x-pinctrl_8h.md#a5762a504ac0b9476306ac07ec06b9a5a)#define QSPI\_D5\_PD7 SIWX91X\_GPIO(1, 0xFF, 19, 3, 7, 0)

[ 275](siwx91x-pinctrl_8h.md#af355ef7ae1a4dcc569a26b4b6eff1226)#define QSPI\_D6\_PD8 SIWX91X\_GPIO(1, 0xFF, 20, 3, 8, 0)

[ 276](siwx91x-pinctrl_8h.md#affe6070baa603f65d26180bf5147934b)#define QSPI\_D7\_PD9 SIWX91X\_GPIO(1, 0xFF, 21, 3, 9, 0)

277

[ 278](siwx91x-pinctrl_8h.md#af6b3953942baf7d7bac7a18ad7583afb)#define SCT\_IN0\_PB9 SIWX91X\_GPIO(9, 0xFF, 0, 1, 9, 0)

[ 279](siwx91x-pinctrl_8h.md#a99b69d8a4f849a64b236986a2abc21c9)#define SCT\_IN0\_ULP0 SIWX91X\_GPIO(7, 6, 22, 4, 0, 0)

[ 280](siwx91x-pinctrl_8h.md#a3ab3d2e1f5a11a5386b700f03cf98b59)#define SCT\_IN0\_ULP4 SIWX91X\_GPIO(9, 6, 26, 4, 4, 4)

[ 281](siwx91x-pinctrl_8h.md#a2090c58ab61d8d0dacefa1cae48a3889)#define SCT\_IN1\_PB10 SIWX91X\_GPIO(9, 0xFF, 0, 1, 10, 0)

[ 282](siwx91x-pinctrl_8h.md#a0795a0474012f940b032bf0c93a54283)#define SCT\_IN1\_ULP1 SIWX91X\_GPIO(7, 6, 23, 4, 1, 1)

[ 283](siwx91x-pinctrl_8h.md#aa543bccd5eaa129a2e71626bfb5a9e0e)#define SCT\_IN1\_ULP5 SIWX91X\_GPIO(9, 6, 27, 4, 5, 5)

[ 284](siwx91x-pinctrl_8h.md#abe6e13dda586ae36d86f33d228f570ef)#define SCT\_IN2\_PB11 SIWX91X\_GPIO(9, 0xFF, 0, 1, 11, 0)

[ 285](siwx91x-pinctrl_8h.md#a2d6b23ffe6db55ca5e76118dea7a14ea)#define SCT\_IN2\_ULP2 SIWX91X\_GPIO(7, 6, 24, 4, 2, 2)

[ 286](siwx91x-pinctrl_8h.md#aa9e34755ee740ce485048bc6edae12b1)#define SCT\_IN2\_ULP6 SIWX91X\_GPIO(9, 6, 28, 4, 6, 6)

[ 287](siwx91x-pinctrl_8h.md#a4ec739fce87299a7c22a286ba2c83aa0)#define SCT\_IN3\_PB12 SIWX91X\_GPIO(9, 0xFF, 0, 1, 12, 0)

[ 288](siwx91x-pinctrl_8h.md#a20d138a68cefaf8a5785def1553adf10)#define SCT\_IN3\_ULP3 SIWX91X\_GPIO(7, 6, 25, 4, 3, 3)

[ 289](siwx91x-pinctrl_8h.md#a9f850c61dbeb18c64e8d133cc37aee77)#define SCT\_IN3\_ULP7 SIWX91X\_GPIO(9, 6, 29, 4, 7, 7)

[ 290](siwx91x-pinctrl_8h.md#af55aacabe3ef0f727eefb8dbe5811250)#define SCT\_OUT0\_PB13 SIWX91X\_GPIO(9, 0xFF, 0, 1, 13, 0)

[ 291](siwx91x-pinctrl_8h.md#a31a6744e2a07d61f7aff3a64d29c6345)#define SCT\_OUT0\_ULP4 SIWX91X\_GPIO(7, 6, 26, 4, 4, 4)

[ 292](siwx91x-pinctrl_8h.md#a2a50717c79f6831681bbc46095835af2)#define SCT\_OUT1\_PB14 SIWX91X\_GPIO(9, 0xFF, 0, 1, 14, 0)

[ 293](siwx91x-pinctrl_8h.md#aeee61408d7a9d0fb3ec2b099bf6b4925)#define SCT\_OUT1\_ULP5 SIWX91X\_GPIO(7, 6, 27, 4, 5, 5)

[ 294](siwx91x-pinctrl_8h.md#a23da2c3994e6cd53cfdf9978b88ee4d8)#define SCT\_OUT2\_PA8 SIWX91X\_GPIO(12, 0xFF, 3, 0, 8, 0)

[ 295](siwx91x-pinctrl_8h.md#aceb19f98ff9d765be5ac4163c400b30f)#define SCT\_OUT2\_ULP6 SIWX91X\_GPIO(7, 6, 28, 4, 6, 6)

[ 296](siwx91x-pinctrl_8h.md#a981668af789d77a02292e7b83ce144d4)#define SCT\_OUT3\_PA9 SIWX91X\_GPIO(12, 0xFF, 4, 0, 9, 0)

[ 297](siwx91x-pinctrl_8h.md#a3d240479009ee2c1660006406a51e14b)#define SCT\_OUT3\_ULP7 SIWX91X\_GPIO(7, 6, 29, 4, 7, 7)

[ 298](siwx91x-pinctrl_8h.md#aa1ce9c940b0f1b1f85e8c0aa765afe58)#define SCT\_OUT4\_ULP4 SIWX91X\_GPIO(13, 6, 26, 4, 4, 4)

[ 299](siwx91x-pinctrl_8h.md#a56f04a2fdf3d596c09989bb7f2f4d711)#define SCT\_OUT4\_ULP8 SIWX91X\_GPIO(7, 6, 30, 4, 8, 8)

[ 300](siwx91x-pinctrl_8h.md#abddc79f260ecc7fb85878f5182f0b4b2)#define SCT\_OUT5\_ULP5 SIWX91X\_GPIO(13, 6, 27, 4, 5, 5)

[ 301](siwx91x-pinctrl_8h.md#a14ad4c709bf766e5568ec2214c29935d)#define SCT\_OUT5\_ULP9 SIWX91X\_GPIO(7, 6, 31, 4, 9, 9)

[ 302](siwx91x-pinctrl_8h.md#ab3ecf512e8c70db0f9a7a374d5c4ee61)#define SCT\_OUT6\_ULP6 SIWX91X\_GPIO(13, 6, 28, 4, 6, 6)

[ 303](siwx91x-pinctrl_8h.md#a9833d3691184034534dac5542141979c)#define SCT\_OUT6\_ULP10 SIWX91X\_GPIO(7, 6, 32, 4, 10, 10)

[ 304](siwx91x-pinctrl_8h.md#a58d91744df7f674a8d639efee6ada664)#define SCT\_OUT7\_ULP7 SIWX91X\_GPIO(13, 6, 29, 4, 7, 7)

[ 305](siwx91x-pinctrl_8h.md#a72096ef61c9b342223b90a4a2a2cad67)#define SCT\_OUT7\_ULP11 SIWX91X\_GPIO(7, 6, 33, 4, 11, 11)

306

[ 307](siwx91x-pinctrl_8h.md#abd7f240fc6b5a58d5f2cf38e0c5620f1)#define SIO\_0\_PA6 SIWX91X\_GPIO(1, 0xFF, 1, 0, 6, 0)

[ 308](siwx91x-pinctrl_8h.md#a9f885bb2113d305967ebbebc3231605c)#define SIO\_0\_PB9 SIWX91X\_GPIO(1, 0xFF, 0, 1, 9, 0)

[ 309](siwx91x-pinctrl_8h.md#ac962669966622a760066ae1d644cf16e)#define SIO\_0\_ULP0 SIWX91X\_GPIO(1, 6, 22, 4, 0, 0)

[ 310](siwx91x-pinctrl_8h.md#a9e2fbc5435e49df883f1cf0394ca5720)#define SIO\_0\_ULP8 SIWX91X\_GPIO(1, 6, 30, 4, 8, 8)

[ 311](siwx91x-pinctrl_8h.md#ab423874b7b55c600ed6ef1826081272f)#define SIO\_1\_PA7 SIWX91X\_GPIO(1, 0xFF, 2, 0, 7, 0)

[ 312](siwx91x-pinctrl_8h.md#ab5cfd5200b404a4cb25e36250900d82f)#define SIO\_1\_PB10 SIWX91X\_GPIO(1, 0xFF, 0, 1, 10, 0)

[ 313](siwx91x-pinctrl_8h.md#ac6a3e01783137270cf5fa27b02c62c5c)#define SIO\_1\_ULP1 SIWX91X\_GPIO(1, 6, 23, 4, 1, 1)

[ 314](siwx91x-pinctrl_8h.md#ac75318d95fac4ae093072ed1f73e18c0)#define SIO\_1\_ULP9 SIWX91X\_GPIO(1, 6, 31, 4, 9, 9)

[ 315](siwx91x-pinctrl_8h.md#a631a7a50a7e52d343d6d3439137f749c)#define SIO\_2\_PA8 SIWX91X\_GPIO(1, 0xFF, 3, 0, 8, 0)

[ 316](siwx91x-pinctrl_8h.md#a567abdc9e3650ef3b243f617e280d5a1)#define SIO\_2\_PB11 SIWX91X\_GPIO(1, 0xFF, 0, 1, 11, 0)

[ 317](siwx91x-pinctrl_8h.md#accd43e63baf2ece7c3105e7b1179281f)#define SIO\_2\_ULP2 SIWX91X\_GPIO(1, 6, 24, 4, 2, 2)

[ 318](siwx91x-pinctrl_8h.md#ab203641292581774bcf3ea40e5c6f465)#define SIO\_2\_ULP10 SIWX91X\_GPIO(1, 6, 32, 4, 10, 10)

[ 319](siwx91x-pinctrl_8h.md#a157b52888424fa35112d0cd60fc56c1f)#define SIO\_3\_PA9 SIWX91X\_GPIO(1, 0xFF, 4, 0, 9, 0)

[ 320](siwx91x-pinctrl_8h.md#a5cbdacf4354500f7dfa8b9542f12aee7)#define SIO\_3\_PB12 SIWX91X\_GPIO(1, 0xFF, 0, 1, 12, 0)

[ 321](siwx91x-pinctrl_8h.md#ae271fa5750acca3534ea22178fea6fc5)#define SIO\_3\_ULP3 SIWX91X\_GPIO(1, 6, 25, 4, 3, 3)

[ 322](siwx91x-pinctrl_8h.md#acafbbec57e7c4b952398106cb9a03ef7)#define SIO\_3\_ULP11 SIWX91X\_GPIO(1, 6, 33, 4, 11, 11)

[ 323](siwx91x-pinctrl_8h.md#a8f2887fdb2e650b6437973bfd930fcca)#define SIO\_4\_PA10 SIWX91X\_GPIO(1, 0xFF, 5, 0, 10, 0)

[ 324](siwx91x-pinctrl_8h.md#ab4b34023754b21b59e6927fc6ba69b3a)#define SIO\_4\_PB13 SIWX91X\_GPIO(1, 0xFF, 0, 1, 13, 0)

[ 325](siwx91x-pinctrl_8h.md#ac0274ba6c1129339f49f087e9b503759)#define SIO\_4\_ULP4 SIWX91X\_GPIO(1, 6, 26, 4, 4, 4)

[ 326](siwx91x-pinctrl_8h.md#a20ad4f9eb06945cab3b92ed5fa195328)#define SIO\_5\_PA11 SIWX91X\_GPIO(1, 0xFF, 6, 0, 11, 0)

[ 327](siwx91x-pinctrl_8h.md#a1a41ab27d7862f6ab974c45eec81468b)#define SIO\_5\_PB14 SIWX91X\_GPIO(1, 0xFF, 0, 1, 14, 0)

[ 328](siwx91x-pinctrl_8h.md#a07a673ae96d7332b5799d7e779180cc9)#define SIO\_5\_ULP5 SIWX91X\_GPIO(1, 6, 27, 4, 5, 5)

[ 329](siwx91x-pinctrl_8h.md#ab6d4f24470587604725bb9612d988b34)#define SIO\_6\_ULP6 SIWX91X\_GPIO(1, 6, 28, 4, 6, 6)

[ 330](siwx91x-pinctrl_8h.md#aa9385597a4cd79160425eefd7872545f)#define SIO\_7\_PA15 SIWX91X\_GPIO(1, 0xFF, 8, 0, 15, 0)

[ 331](siwx91x-pinctrl_8h.md#a52635e4cce4a478134455ea5ee43c962)#define SIO\_7\_ULP7 SIWX91X\_GPIO(1, 6, 29, 4, 7, 7)

332

[ 333](siwx91x-pinctrl_8h.md#af1247675c38bb4e436d2cb88655c9d08)#define SSI\_CLK\_PA8 SIWX91X\_GPIO(3, 0xFF, 3, 0, 8, 0)

[ 334](siwx91x-pinctrl_8h.md#a7ad9e0ec1ca287249eeee64542b2c65c)#define SSI\_CLK\_PB9 SIWX91X\_GPIO(3, 0xFF, 0, 1, 9, 0)

[ 335](siwx91x-pinctrl_8h.md#a870697f96c8feecba5a5f3e67b6cc9b7)#define SSI\_CLK\_PD4 SIWX91X\_GPIO(3, 0xFF, 16, 3, 4, 0)

[ 336](siwx91x-pinctrl_8h.md#a82d5167d005f0d0c576272be7a0d991c)#define SSI\_CS0\_PA9 SIWX91X\_GPIO(3, 0xFF, 4, 0, 9, 0)

[ 337](siwx91x-pinctrl_8h.md#aff75ba830cd83e5ff9a73bb5decc399a)#define SSI\_CS0\_PB12 SIWX91X\_GPIO(3, 0xFF, 0, 1, 12, 0)

[ 338](siwx91x-pinctrl_8h.md#a11cdae0cbf92ad4384ccfeb3a6d966f2)#define SSI\_CS0\_PD5 SIWX91X\_GPIO(3, 0xFF, 17, 3, 5, 0)

[ 339](siwx91x-pinctrl_8h.md#a8605c0bf9d7c26f67c634ad883531e84)#define SSI\_CS1\_PA10 SIWX91X\_GPIO(3, 0xFF, 5, 0, 10, 0)

[ 340](siwx91x-pinctrl_8h.md#ae7922b6b676ad7a97336b6df4f8afa67)#define SSI\_CS2\_PA15 SIWX91X\_GPIO(3, 0xFF, 8, 0, 15, 0)

[ 341](siwx91x-pinctrl_8h.md#af67e11e779cb8186533a9eb261b766a1)#define SSI\_CS2\_PD2 SIWX91X\_GPIO(3, 0xFF, 14, 3, 2, 0)

[ 342](siwx91x-pinctrl_8h.md#a45f048b3c99f09138e373b6a51ad015c)#define SSI\_CS3\_PD3 SIWX91X\_GPIO(3, 0xFF, 15, 3, 3, 0)

[ 343](siwx91x-pinctrl_8h.md#afc574383056afbc3e274866956b5c054)#define SSI\_DATA0\_PA11 SIWX91X\_GPIO(3, 0xFF, 6, 0, 11, 0)

[ 344](siwx91x-pinctrl_8h.md#a17e181b456f6ddfddc113a944a0e18a5)#define SSI\_DATA0\_PB10 SIWX91X\_GPIO(3, 0xFF, 0, 1, 10, 0)

[ 345](siwx91x-pinctrl_8h.md#ab70bd927a56993a4f33e4ba9ab6584aa)#define SSI\_DATA0\_PD8 SIWX91X\_GPIO(3, 0xFF, 20, 3, 8, 0)

[ 346](siwx91x-pinctrl_8h.md#a3136aba807e9ae4046e7332d662d665b)#define SSI\_DATA1\_PA10 SIWX91X\_GPIO(12, 0xFF, 5, 0, 10, 0)

[ 347](siwx91x-pinctrl_8h.md#ae8bab0e24e8a83652f1ba3d6601ee82f)#define SSI\_DATA1\_PA12 SIWX91X\_GPIO(3, 0xFF, 7, 0, 12, 0)

[ 348](siwx91x-pinctrl_8h.md#a8b29028c602b6cf6b2eb871fce03faaf)#define SSI\_DATA1\_PB11 SIWX91X\_GPIO(3, 0xFF, 0, 1, 11, 0)

[ 349](siwx91x-pinctrl_8h.md#a4da565ff535bfc74e28645c4e907999f)#define SSI\_DATA1\_PD9 SIWX91X\_GPIO(3, 0xFF, 21, 3, 9, 0)

[ 350](siwx91x-pinctrl_8h.md#afb9b05eb91afb26a1efd24a0bcefa884)#define SSI\_DATA2\_PA6 SIWX91X\_GPIO(3, 0xFF, 1, 0, 6, 0)

[ 351](siwx91x-pinctrl_8h.md#a5a2ae3a3d82b60b119db1f639007b911)#define SSI\_DATA2\_PB13 SIWX91X\_GPIO(3, 0xFF, 0, 1, 13, 0)

[ 352](siwx91x-pinctrl_8h.md#a6828f8f39c565a9bb8a46da1c6981b49)#define SSI\_DATA2\_PD6 SIWX91X\_GPIO(3, 0xFF, 18, 3, 6, 0)

[ 353](siwx91x-pinctrl_8h.md#a0b3e87321b12727b6b4539c7c09f70c8)#define SSI\_DATA3\_PA7 SIWX91X\_GPIO(3, 0xFF, 2, 0, 7, 0)

[ 354](siwx91x-pinctrl_8h.md#aa341c51d2aa108793138c965e6c29160)#define SSI\_DATA3\_PB14 SIWX91X\_GPIO(3, 0xFF, 0, 1, 14, 0)

[ 355](siwx91x-pinctrl_8h.md#a3fc5e833e2d7d3d042990a3b243cb16c)#define SSI\_DATA3\_PD7 SIWX91X\_GPIO(3, 0xFF, 19, 3, 7, 0)

356

[ 357](siwx91x-pinctrl_8h.md#a818278555d17f4ede79a73680a96d65f)#define SSIS\_CLK\_PA8 SIWX91X\_GPIO(8, 0xFF, 3, 0, 8, 0)

[ 358](siwx91x-pinctrl_8h.md#a2ccee4a24cf3d570c05f5fef55e39103)#define SSIS\_CLK\_PB10 SIWX91X\_GPIO(8, 0xFF, 0, 1, 10, 0)

[ 359](siwx91x-pinctrl_8h.md#a968c482ec688d8355968dabdb8a378f1)#define SSIS\_CLK\_PC15 SIWX91X\_GPIO(8, 0xFF, 11, 2, 15, 0)

[ 360](siwx91x-pinctrl_8h.md#abc818b5d2a4dd17f260421698e9fcfca)#define SSIS\_CLK\_PD4 SIWX91X\_GPIO(8, 0xFF, 16, 3, 4, 0)

[ 361](siwx91x-pinctrl_8h.md#ad7957f99b75ff1d68169a1562e724e37)#define SSIS\_CS\_PA9 SIWX91X\_GPIO(8, 0xFF, 4, 0, 9, 0)

[ 362](siwx91x-pinctrl_8h.md#ab17f0dc6fcd1be261fb7435879447ac6)#define SSIS\_CS\_PB9 SIWX91X\_GPIO(8, 0xFF, 0, 1, 9, 0)

[ 363](siwx91x-pinctrl_8h.md#a46a158dbda75df58f11e0afc39c5ca53)#define SSIS\_CS\_PC14 SIWX91X\_GPIO(8, 0xFF, 10, 2, 14, 0)

[ 364](siwx91x-pinctrl_8h.md#ab0c12069b4d9c2920f6c902ad3486bea)#define SSIS\_CS\_PD5 SIWX91X\_GPIO(8, 0xFF, 17, 3, 5, 0)

[ 365](siwx91x-pinctrl_8h.md#abc67462a716e77b787344ae5f8b57b81)#define SSIS\_MISO\_PA11 SIWX91X\_GPIO(8, 0xFF, 6, 0, 11, 0)

[ 366](siwx91x-pinctrl_8h.md#af83040c393f37177b0458c5d321f9044)#define SSIS\_MISO\_PB12 SIWX91X\_GPIO(8, 0xFF, 0, 1, 12, 0)

[ 367](siwx91x-pinctrl_8h.md#a2bb0c36da9d9f6c5f3afa244435278d5)#define SSIS\_MISO\_PD1 SIWX91X\_GPIO(8, 0xFF, 13, 3, 1, 0)

[ 368](siwx91x-pinctrl_8h.md#ada16d9e1a87b9f841957d9a3d5937c01)#define SSIS\_MISO\_PD9 SIWX91X\_GPIO(8, 0xFF, 21, 3, 9, 0)

[ 369](siwx91x-pinctrl_8h.md#a2e78220a86b3228582def750e7df9205)#define SSIS\_MOSI\_PA10 SIWX91X\_GPIO(8, 0xFF, 5, 0, 10, 0)

[ 370](siwx91x-pinctrl_8h.md#afc975917e6df3e935e9b70c294f6a878)#define SSIS\_MOSI\_PB11 SIWX91X\_GPIO(8, 0xFF, 0, 1, 11, 0)

[ 371](siwx91x-pinctrl_8h.md#ad2fe30aa1865c5cd33a243521a9ad46e)#define SSIS\_MOSI\_PD0 SIWX91X\_GPIO(8, 0xFF, 12, 3, 0, 0)

[ 372](siwx91x-pinctrl_8h.md#aceb1bad6deb76524fc6b3df7490d13f8)#define SSIS\_MOSI\_PD8 SIWX91X\_GPIO(8, 0xFF, 20, 3, 8, 0)

373

[ 374](siwx91x-pinctrl_8h.md#af7bffdadd491984d9b6cac97f1dfd3e8)#define TIMER0\_PA7 SIWX91X\_GPIO(9, 5, 2, 0, 7, 1)

[ 375](siwx91x-pinctrl_8h.md#a78bc689f7b9610f29f5ab83f629b1513)#define TIMER0\_PB11 SIWX91X\_GPIO(11, 5, 0, 1, 11, 8)

[ 376](siwx91x-pinctrl_8h.md#ae92b290d7fc89236507141c300917e90)#define TIMER0\_PC14 SIWX91X\_GPIO(9, 5, 10, 2, 14, 8)

[ 377](siwx91x-pinctrl_8h.md#a8043999b57da3920d59a3c61e68a26ae)#define TIMER0\_ULP4 SIWX91X\_GPIO(0xFF, 9, 0xFF, 4, 0, 4)

[ 378](siwx91x-pinctrl_8h.md#a412766982e02327695695d09968e4ee0)#define TIMER0\_ULP8 SIWX91X\_GPIO(0xFF, 5, 0xFF, 4, 0, 8)

379

[ 380](siwx91x-pinctrl_8h.md#ae8f4fc879de28591840ba818ffe7220f)#define TIMER1\_PA15 SIWX91X\_GPIO(9, 5, 8, 0, 15, 7)

[ 381](siwx91x-pinctrl_8h.md#aa83eaf9d471dfc441a698ded97d75671)#define TIMER1\_PB10 SIWX91X\_GPIO(11, 5, 0, 1, 10, 7)

[ 382](siwx91x-pinctrl_8h.md#a99832252de48cc89d11c3e522ea44376)#define TIMER1\_ULP5 SIWX91X\_GPIO(0xFF, 9, 0xFF, 4, 0, 5)

[ 383](siwx91x-pinctrl_8h.md#aa1fb1deae2ad43558df04b772029957f)#define TIMER1\_ULP7 SIWX91X\_GPIO(0xFF, 5, 0xFF, 4, 0, 7)

384

[ 385](siwx91x-pinctrl_8h.md#aa778464dc8449625d49328f30c76e92e)#define TIMER2\_ULP1 SIWX91X\_GPIO(0xFF, 5, 0xFF, 4, 0, 1)

386

[ 387](siwx91x-pinctrl_8h.md#af0a0a31333bf0ebdc1d2d16341001fda)#define TRACE\_CLK\_PA7 SIWX91X\_GPIO(13, 0xFF, 2, 0, 7, 0)

[ 388](siwx91x-pinctrl_8h.md#a52b1bda898ac2bca0807c531e0544ff6)#define TRACE\_CLK\_PC15 SIWX91X\_GPIO(6, 0xFF, 11, 2, 15, 0)

[ 389](siwx91x-pinctrl_8h.md#a6c0a2853a3b39f2aeb7f60cbb6b38646)#define TRACE\_CLK\_PD5 SIWX91X\_GPIO(6, 0xFF, 17, 3, 5, 0)

[ 390](siwx91x-pinctrl_8h.md#a9c5c8569a1d4d720bceec4d7cf6b9050)#define TRACE\_CLKIN\_PA6 SIWX91X\_GPIO(13, 0xFF, 1, 0, 6, 0)

[ 391](siwx91x-pinctrl_8h.md#a588fb12454a12f0f09e300b5f5038d57)#define TRACE\_CLKIN\_PA15 SIWX91X\_GPIO(6, 0xFF, 8, 0, 15, 0)

[ 392](siwx91x-pinctrl_8h.md#add8f25d772c07882a42840f49591d661)#define TRACE\_CLKIN\_PC14 SIWX91X\_GPIO(6, 0xFF, 10, 2, 14, 0)

[ 393](siwx91x-pinctrl_8h.md#a852139c034764bee8b394e325a3b0746)#define TRACE\_CLKIN\_PD4 SIWX91X\_GPIO(6, 0xFF, 16, 3, 4, 0)

[ 394](siwx91x-pinctrl_8h.md#ab3c72d853a06d3d05438c6b481b6d294)#define TRACE\_D0\_PA8 SIWX91X\_GPIO(13, 0xFF, 3, 0, 8, 0)

[ 395](siwx91x-pinctrl_8h.md#aa4af7f1f9c48d4e498906593f097ab17)#define TRACE\_D0\_PD0 SIWX91X\_GPIO(6, 0xFF, 12, 3, 0, 0)

[ 396](siwx91x-pinctrl_8h.md#a1d65dc9e77137cc569e13ba513ab038e)#define TRACE\_D0\_PD6 SIWX91X\_GPIO(6, 0xFF, 18, 3, 6, 0)

[ 397](siwx91x-pinctrl_8h.md#a6d856fb1f6b7482344d84d74fa1a41de)#define TRACE\_D1\_PA9 SIWX91X\_GPIO(13, 0xFF, 4, 0, 9, 0)

[ 398](siwx91x-pinctrl_8h.md#a836e1e15c86a625a47bd48ab6e257356)#define TRACE\_D1\_PD1 SIWX91X\_GPIO(6, 0xFF, 13, 3, 1, 0)

[ 399](siwx91x-pinctrl_8h.md#acd7d2c12a3df9e397ebac33ab9afde53)#define TRACE\_D1\_PD7 SIWX91X\_GPIO(6, 0xFF, 19, 3, 7, 0)

[ 400](siwx91x-pinctrl_8h.md#a5b36f56857e36038341ad69aa867afd5)#define TRACE\_D2\_PA10 SIWX91X\_GPIO(13, 0xFF, 5, 0, 10, 0)

[ 401](siwx91x-pinctrl_8h.md#a12202d51512a2c21fe7052143ed5c153)#define TRACE\_D2\_PD2 SIWX91X\_GPIO(6, 0xFF, 14, 3, 2, 0)

[ 402](siwx91x-pinctrl_8h.md#ac656df05900e217a003cfd7b2113fa4c)#define TRACE\_D2\_PD8 SIWX91X\_GPIO(6, 0xFF, 20, 3, 8, 0)

[ 403](siwx91x-pinctrl_8h.md#a334d33b8e1edf2c9c107fc3c8f52ed03)#define TRACE\_D3\_PA11 SIWX91X\_GPIO(13, 0xFF, 6, 0, 11, 0)

[ 404](siwx91x-pinctrl_8h.md#ae31d82feb91d430378d74796d537f3a5)#define TRACE\_D3\_PD3 SIWX91X\_GPIO(6, 0xFF, 15, 3, 3, 0)

[ 405](siwx91x-pinctrl_8h.md#a3658e3eb2161a47461e541a143565028)#define TRACE\_D3\_PD9 SIWX91X\_GPIO(6, 0xFF, 21, 3, 9, 0)

406

[ 407](siwx91x-pinctrl_8h.md#af07db6e9c3de31079d415f4ad0aeb8f9)#define UART1\_CLK\_PA8 SIWX91X\_GPIO(2, 0xFF, 3, 0, 8, 0)

[ 408](siwx91x-pinctrl_8h.md#a47d93bec7d539b0e4516d9ed367f5b34)#define UART1\_CLK\_PB9 SIWX91X\_GPIO(2, 0xFF, 0, 1, 9, 0)

[ 409](siwx91x-pinctrl_8h.md#a97b6dafd5b8dac0ad0939516758242a1)#define UART1\_CLK\_PD4 SIWX91X\_GPIO(2, 0xFF, 16, 3, 4, 0)

[ 410](siwx91x-pinctrl_8h.md#a38ee598df89abdbc5a0872b0dfcd60cd)#define UART1\_CLK\_ULP0 SIWX91X\_GPIO(2, 6, 22, 4, 0, 0)

[ 411](siwx91x-pinctrl_8h.md#a5573980a3c2e25f4a698aec22c9b5204)#define UART1\_CTS\_PA6 SIWX91X\_GPIO(2, 0xFF, 1, 0, 6, 0)

[ 412](siwx91x-pinctrl_8h.md#ad1fdd94f23b4da8903ec16a2e7fced33)#define UART1\_CTS\_PB10 SIWX91X\_GPIO(2, 0xFF, 0, 1, 10, 0)

[ 413](siwx91x-pinctrl_8h.md#ad50e6e6a3bc44b72c29292e806d2c2a4)#define UART1\_CTS\_PD8 SIWX91X\_GPIO(2, 0xFF, 20, 3, 8, 0)

[ 414](siwx91x-pinctrl_8h.md#a0f6b857a7760c87893da932d2489d164)#define UART1\_CTS\_ULP6 SIWX91X\_GPIO(2, 6, 28, 4, 6, 6)

[ 415](siwx91x-pinctrl_8h.md#ac8c7dff7a79463b3acfede75b4629025)#define UART1\_DCD\_PA12 SIWX91X\_GPIO(2, 0xFF, 7, 0, 12, 0)

[ 416](siwx91x-pinctrl_8h.md#a0696a8aa32ec1c9329c4155dc8738bf9)#define UART1\_DCD\_PB13 SIWX91X\_GPIO(12, 0xFF, 0, 1, 13, 0)

[ 417](siwx91x-pinctrl_8h.md#a18cf489faf44ec367c6098c3fadef1ef)#define UART1\_DSR\_PA11 SIWX91X\_GPIO(2, 0xFF, 6, 0, 11, 0)

[ 418](siwx91x-pinctrl_8h.md#a136ffa30c72fa3aa46648ee87354de76)#define UART1\_DSR\_PD9 SIWX91X\_GPIO(2, 0xFF, 21, 3, 9, 0)

[ 419](siwx91x-pinctrl_8h.md#a2006115d5dc18b7560139627763874a0)#define UART1\_DTR\_PA7 SIWX91X\_GPIO(2, 0xFF, 2, 0, 7, 0)

[ 420](siwx91x-pinctrl_8h.md#a452209d8b5ae5c51bcb383b13b36c7b0)#define UART1\_IRRX\_PB9 SIWX91X\_GPIO(13, 0xFF, 0, 1, 9, 0)

[ 421](siwx91x-pinctrl_8h.md#ac168bc0d00a756c66f49e0b5030dbac4)#define UART1\_IRRX\_PC15 SIWX91X\_GPIO(2, 0xFF, 11, 2, 15, 0)

[ 422](siwx91x-pinctrl_8h.md#acd1625a2cabaafb2598c9566f9b83ccb)#define UART1\_IRRX\_ULP0 SIWX91X\_GPIO(11, 6, 22, 4, 0, 0)

[ 423](siwx91x-pinctrl_8h.md#ab984ffe938ecf7c5e04c474a2c616355)#define UART1\_IRRX\_ULP7 SIWX91X\_GPIO(2, 6, 29, 4, 7, 7)

[ 424](siwx91x-pinctrl_8h.md#a13705354f7564f454e07d228944cc246)#define UART1\_IRTX\_PB10 SIWX91X\_GPIO(13, 0xFF, 0, 1, 10, 0)

[ 425](siwx91x-pinctrl_8h.md#a0e81f143d5f44ccafb17ce97cc3599a0)#define UART1\_IRTX\_PD0 SIWX91X\_GPIO(2, 0xFF, 12, 3, 0, 0)

[ 426](siwx91x-pinctrl_8h.md#a64802a19ac4c37fbcbc35a5aa8db40a3)#define UART1\_IRTX\_ULP1 SIWX91X\_GPIO(11, 6, 23, 4, 1, 1)

[ 427](siwx91x-pinctrl_8h.md#a9fb51eb9b73a1878cc39879d20a9b263)#define UART1\_IRTX\_ULP8 SIWX91X\_GPIO(2, 6, 30, 4, 8, 8)

[ 428](siwx91x-pinctrl_8h.md#a30aa9e28372f86b4e89581ddaede5c62)#define UART1\_RI\_PB11 SIWX91X\_GPIO(2, 0xFF, 0, 1, 11, 0)

[ 429](siwx91x-pinctrl_8h.md#a4facf170ae2b2d990b1aee12c721f316)#define UART1\_RI\_PC14 SIWX91X\_GPIO(2, 0xFF, 10, 2, 14, 0)

[ 430](siwx91x-pinctrl_8h.md#a81b56ff9b9e188fc6c221fb98769993b)#define UART1\_RI\_ULP4 SIWX91X\_GPIO(11, 6, 26, 4, 4, 4)

[ 431](siwx91x-pinctrl_8h.md#ace587c70d24e0c6aab94f214889b8f51)#define UART1\_RS485DE\_PB13 SIWX91X\_GPIO(13, 0xFF, 0, 1, 13, 0)

[ 432](siwx91x-pinctrl_8h.md#aa56bf7af02473be2176c87ffef21c2cb)#define UART1\_RS485DE\_PD3 SIWX91X\_GPIO(2, 0xFF, 15, 3, 3, 0)

[ 433](siwx91x-pinctrl_8h.md#a3805f665734e294e4379708ea7623e91)#define UART1\_RS485DE\_ULP7 SIWX91X\_GPIO(11, 6, 29, 4, 7, 7)

[ 434](siwx91x-pinctrl_8h.md#ad04deb098006e6608ddee97489cb3eec)#define UART1\_RS485DE\_ULP11 SIWX91X\_GPIO(2, 6, 33, 4, 11, 11)

[ 435](siwx91x-pinctrl_8h.md#a27f6a89b10a3e6177c2b2319073dc97d)#define UART1\_RS485EN\_PB11 SIWX91X\_GPIO(13, 0xFF, 0, 1, 11, 0)

[ 436](siwx91x-pinctrl_8h.md#a685c05e6cb782a705fa4a4d124fa73a7)#define UART1\_RS485EN\_PD1 SIWX91X\_GPIO(2, 0xFF, 13, 3, 1, 0)

[ 437](siwx91x-pinctrl_8h.md#a91087baa78c19010c59f22feeaacc03d)#define UART1\_RS485EN\_ULP5 SIWX91X\_GPIO(11, 6, 27, 4, 5, 5)

[ 438](siwx91x-pinctrl_8h.md#a1a86fd0c995af4260a4f171e49dce834)#define UART1\_RS485EN\_ULP9 SIWX91X\_GPIO(2, 6, 31, 4, 9, 9)

[ 439](siwx91x-pinctrl_8h.md#a2767859606aa7c3c6dcc37b1801d5fce)#define UART1\_RS485RE\_PB12 SIWX91X\_GPIO(13, 0xFF, 0, 1, 12, 0)

[ 440](siwx91x-pinctrl_8h.md#a2fea463140a034be3e613030ae623a8a)#define UART1\_RS485RE\_PD2 SIWX91X\_GPIO(2, 0xFF, 14, 3, 2, 0)

[ 441](siwx91x-pinctrl_8h.md#af6a331fb4f771ad7bbcd546856358b38)#define UART1\_RS485RE\_ULP6 SIWX91X\_GPIO(11, 6, 28, 4, 6, 6)

[ 442](siwx91x-pinctrl_8h.md#a310f189ae26d3412769346ea2f506a1b)#define UART1\_RS485RE\_ULP10 SIWX91X\_GPIO(2, 6, 32, 4, 10, 10)

[ 443](siwx91x-pinctrl_8h.md#ab41d801f1040754da3a5bf45702e9258)#define UART1\_RTS\_PA9 SIWX91X\_GPIO(2, 0xFF, 4, 0, 9, 0)

[ 444](siwx91x-pinctrl_8h.md#a88155b4669cb09a6c5db01a82648db1d)#define UART1\_RTS\_PB12 SIWX91X\_GPIO(2, 0xFF, 0, 1, 12, 0)

[ 445](siwx91x-pinctrl_8h.md#af6a6388df4239908fef460d6ced7d024)#define UART1\_RTS\_PD5 SIWX91X\_GPIO(2, 0xFF, 17, 3, 5, 0)

[ 446](siwx91x-pinctrl_8h.md#a8d4d11aa96d1c3f7415c6194cb8d8c53)#define UART1\_RTS\_ULP5 SIWX91X\_GPIO(2, 6, 27, 4, 5, 5)

[ 447](siwx91x-pinctrl_8h.md#a05b30678220039c10623424e5ab9dd47)#define UART1\_RX\_PA10 SIWX91X\_GPIO(2, 0xFF, 5, 0, 10, 0)

[ 448](siwx91x-pinctrl_8h.md#a173a0fbd8896e39380c1510aad2a3388)#define UART1\_RX\_PB13 SIWX91X\_GPIO(2, 0xFF, 0, 1, 13, 0)

[ 449](siwx91x-pinctrl_8h.md#a49bf06fbd8ee3a16a6199ce4ad10f732)#define UART1\_RX\_PD7 SIWX91X\_GPIO(2, 0xFF, 19, 3, 7, 0)

[ 450](siwx91x-pinctrl_8h.md#a1064f4e90dae26a86fd121f76755296b)#define UART1\_RX\_ULP1 SIWX91X\_GPIO(2, 6, 23, 4, 1, 1)

[ 451](siwx91x-pinctrl_8h.md#ae2199084377f8225fc05cfc8420c17ad)#define UART1\_RX\_ULP6 SIWX91X\_GPIO(4, 6, 28, 4, 6, 6)

[ 452](siwx91x-pinctrl_8h.md#a1c0c8c109c18c32ae56ffc44279dd1c5)#define UART1\_TX\_PB14 SIWX91X\_GPIO(2, 0xFF, 0, 1, 14, 0)

[ 453](siwx91x-pinctrl_8h.md#a844dfca50c06900c9ae2c7e7eba7d3cb)#define UART1\_TX\_PD6 SIWX91X\_GPIO(2, 0xFF, 18, 3, 6, 0)

[ 454](siwx91x-pinctrl_8h.md#ad6d8130cc4ca0a4f1a7d49f7745c50b8)#define UART1\_TX\_ULP4 SIWX91X\_GPIO(2, 6, 26, 4, 4, 4)

[ 455](siwx91x-pinctrl_8h.md#a5081a97c3d46970a166d8cea4ed87b0c)#define UART1\_TX\_ULP7 SIWX91X\_GPIO(4, 6, 29, 4, 7, 7)

456

[ 457](siwx91x-pinctrl_8h.md#aac5451317b2ec4f5889dbd56ed214ac7)#define UART2\_CTS\_PA11 SIWX91X\_GPIO(6, 0xFF, 6, 0, 11, 0)

[ 458](siwx91x-pinctrl_8h.md#aebff17768b6fc31f5d3358ba90cc6e56)#define UART2\_CTS\_PC0 SIWX91X\_GPIO(12, 0xFF, 9, 2, 0, 0)

[ 459](siwx91x-pinctrl_8h.md#af40d324d56a7c12a5995ee99bdeb98e9)#define UART2\_CTS\_PD3 SIWX91X\_GPIO(9, 0xFF, 15, 3, 3, 0)

[ 460](siwx91x-pinctrl_8h.md#ad490b2bbb5df3e7f7f8a4135fb3171a5)#define UART2\_CTS\_ULP1 SIWX91X\_GPIO(9, 6, 23, 4, 1, 1)

[ 461](siwx91x-pinctrl_8h.md#a98c0ce3e9f5f15639ab9c4337faab7fd)#define UART2\_CTS\_ULP7 SIWX91X\_GPIO(6, 6, 29, 4, 7, 7)

[ 462](siwx91x-pinctrl_8h.md#a40273fbece21b7e56a7674117b7f2998)#define UART2\_CTS\_ULP9 SIWX91X\_GPIO(9, 6, 31, 4, 9, 9)

[ 463](siwx91x-pinctrl_8h.md#ad574f258135ff1db0b2d8a595e3b3a67)#define UART2\_RS485DE\_PA9 SIWX91X\_GPIO(6, 0xFF, 4, 0, 9, 0)

[ 464](siwx91x-pinctrl_8h.md#aabe642e5aaa5dceecf63cffa506ce379)#define UART2\_RS485DE\_ULP2 SIWX91X\_GPIO(6, 6, 24, 4, 2, 2)

[ 465](siwx91x-pinctrl_8h.md#ab8c524cdfc7ccbe4dd41ac9bcc5bfb6e)#define UART2\_RS485DE\_ULP11 SIWX91X\_GPIO(6, 6, 33, 4, 11, 11)

[ 466](siwx91x-pinctrl_8h.md#ab47b6e4fe7075dc02a984454cf0f97fa)#define UART2\_RS485EN\_PA12 SIWX91X\_GPIO(6, 0xFF, 7, 0, 12, 0)

[ 467](siwx91x-pinctrl_8h.md#a479b6c5ba2c20f3ac6a9775ed460d72e)#define UART2\_RS485EN\_PB10 SIWX91X\_GPIO(6, 0xFF, 0, 1, 10, 0)

[ 468](siwx91x-pinctrl_8h.md#a0336854b0ac5ad22df1fcfe6f7344226)#define UART2\_RS485EN\_ULP0 SIWX91X\_GPIO(6, 6, 22, 4, 0, 0)

[ 469](siwx91x-pinctrl_8h.md#afb113efec9436a67872d6177cdcef954)#define UART2\_RS485RE\_PA8 SIWX91X\_GPIO(6, 0xFF, 3, 0, 8, 0)

[ 470](siwx91x-pinctrl_8h.md#a0e9206e188314e22661ce18e3032be85)#define UART2\_RS485RE\_ULP1 SIWX91X\_GPIO(6, 6, 23, 4, 1, 1)

[ 471](siwx91x-pinctrl_8h.md#a699848283d311fb6bec81716c9f28b76)#define UART2\_RS485RE\_ULP10 SIWX91X\_GPIO(6, 6, 32, 4, 10, 10)

[ 472](siwx91x-pinctrl_8h.md#a83e1df774173660f198c82c4dc33720e)#define UART2\_RTS\_PA10 SIWX91X\_GPIO(6, 0xFF, 5, 0, 10, 0)

[ 473](siwx91x-pinctrl_8h.md#a7e9720fcc3aaf3ded2894834e5eb291c)#define UART2\_RTS\_PB11 SIWX91X\_GPIO(6, 0xFF, 0, 1, 11, 0)

[ 474](siwx91x-pinctrl_8h.md#af0fb6a047012f3143e05b0d3bf5f3598)#define UART2\_RTS\_PB12 SIWX91X\_GPIO(6, 0xFF, 0, 1, 12, 0)

[ 475](siwx91x-pinctrl_8h.md#aaafd084748ff7ec90ed0cb5a46e44e6c)#define UART2\_RTS\_PB15 SIWX91X\_GPIO(12, 0xFF, 9, 1, 15, 0)

[ 476](siwx91x-pinctrl_8h.md#a3a20ad907ce1457249b4f1925a80f0d9)#define UART2\_RTS\_PD2 SIWX91X\_GPIO(9, 0xFF, 14, 3, 2, 0)

[ 477](siwx91x-pinctrl_8h.md#a283d27d1fad7642c8316e287c081ca8f)#define UART2\_RTS\_ULP0 SIWX91X\_GPIO(9, 6, 22, 4, 0, 0)

[ 478](siwx91x-pinctrl_8h.md#a4c6322e843a9cd2e3ff439f0a9a36eb0)#define UART2\_RTS\_ULP6 SIWX91X\_GPIO(6, 6, 28, 4, 6, 6)

[ 479](siwx91x-pinctrl_8h.md#ab14937f5ca5d826c2a010f7ad144c86b)#define UART2\_RTS\_ULP8 SIWX91X\_GPIO(9, 6, 30, 4, 8, 8)

[ 480](siwx91x-pinctrl_8h.md#a39c4e61d4a02c02458fbcd83d4978e83)#define UART2\_RX\_PA6 SIWX91X\_GPIO(6, 0xFF, 1, 0, 6, 0)

[ 481](siwx91x-pinctrl_8h.md#a94654ba57257f6262083ab5faed1ad8c)#define UART2\_RX\_PB13 SIWX91X\_GPIO(6, 0xFF, 0, 1, 13, 0)

[ 482](siwx91x-pinctrl_8h.md#aac270922762d6eecc99dd1fc0d284336)#define UART2\_RX\_PC1 SIWX91X\_GPIO(12, 0xFF, 9, 2, 1, 0)

[ 483](siwx91x-pinctrl_8h.md#ab3ad529fa97f026bb4354f6db678d43f)#define UART2\_RX\_ULP2 SIWX91X\_GPIO(9, 6, 24, 4, 1, 1)

[ 484](siwx91x-pinctrl_8h.md#aa760999ca12fa36a267005f41fdd6079)#define UART2\_RX\_ULP4 SIWX91X\_GPIO(6, 6, 26, 4, 4, 4)

[ 485](siwx91x-pinctrl_8h.md#a1394d2f9a3a680750d286299e3ca4a62)#define UART2\_RX\_ULP8 SIWX91X\_GPIO(6, 6, 30, 4, 8, 8)

[ 486](siwx91x-pinctrl_8h.md#a7516ce82618533f9ca2b7be817b730dc)#define UART2\_RX\_ULP10 SIWX91X\_GPIO(9, 6, 32, 4, 10, 10)

[ 487](siwx91x-pinctrl_8h.md#aa644b917b29439282fe20d16a7fe5bc0)#define UART2\_TX\_PA15 SIWX91X\_GPIO(2, 0xFF, 8, 0, 15, 0)

[ 488](siwx91x-pinctrl_8h.md#ab7144f765aec4dd58cadd42efadb2e12)#define UART2\_TX\_PA7 SIWX91X\_GPIO(6, 0xFF, 2, 0, 7, 0)

[ 489](siwx91x-pinctrl_8h.md#ac02b84423d672c2e1e48b2044dde817e)#define UART2\_TX\_PB14 SIWX91X\_GPIO(6, 0xFF, 0, 1, 14, 0)

[ 490](siwx91x-pinctrl_8h.md#af08e91e041bd986e99f2dba2920d98a1)#define UART2\_TX\_PC2 SIWX91X\_GPIO(12, 0xFF, 9, 2, 2, 0)

[ 491](siwx91x-pinctrl_8h.md#a1d31aacda675c6bd86bcb97cdce4ddea)#define UART2\_TX\_ULP3 SIWX91X\_GPIO(9, 6, 25, 4, 1, 1)

[ 492](siwx91x-pinctrl_8h.md#af71131f65d76b90e2390375020b5ba92)#define UART2\_TX\_ULP5 SIWX91X\_GPIO(6, 6, 27, 4, 5, 5)

[ 493](siwx91x-pinctrl_8h.md#a8e5f9ce89a22ddeccf645c2d19294bed)#define UART2\_TX\_ULP9 SIWX91X\_GPIO(6, 6, 31, 4, 9, 9)

[ 494](siwx91x-pinctrl_8h.md#aafc0a9f4413548552fffb85078e8fff3)#define UART2\_TX\_ULP11 SIWX91X\_GPIO(9, 6, 33, 4, 11, 11)

495

[ 496](siwx91x-pinctrl_8h.md#a39dae086da46be97e3078e3c82516175)#define ULPI2C\_SCL\_PA11 SIWX91X\_GPIO(9, 4, 6, 0, 11, 5)

[ 497](siwx91x-pinctrl_8h.md#a1df8709fadb70b36fa67ff4d1853aaef)#define ULPI2C\_SCL\_PA15 SIWX91X\_GPIO(9, 4, 8, 0, 15, 7)

[ 498](siwx91x-pinctrl_8h.md#add0f9393eb8e22b4e8e24c3673cc7377)#define ULPI2C\_SCL\_PA7 SIWX91X\_GPIO(9, 4, 2, 0, 7, 1)

[ 499](siwx91x-pinctrl_8h.md#a2f86d8b390fdcde5303b9c09a5e3e6d0)#define ULPI2C\_SCL\_PB10 SIWX91X\_GPIO(11, 4, 0, 1, 10, 7)

[ 500](siwx91x-pinctrl_8h.md#aa1f13822efae65128336b62b551dc78b)#define ULPI2C\_SCL\_PB11 SIWX91X\_GPIO(11, 4, 0, 1, 11, 8)

[ 501](siwx91x-pinctrl_8h.md#aeb11daa893bfbf1fe0ca04ad44e9f81f)#define ULPI2C\_SCL\_PC14 SIWX91X\_GPIO(9, 4, 10, 2, 14, 8)

[ 502](siwx91x-pinctrl_8h.md#aad197f3c66cfafe58e1c220a1017e8ac)#define ULPI2C\_SCL\_ULP1 SIWX91X\_GPIO(0xFF, 4, 0xFF, 4, 0, 1)

[ 503](siwx91x-pinctrl_8h.md#a3e08531523a985f0dbb68528551dace3)#define ULPI2C\_SCL\_ULP5 SIWX91X\_GPIO(0xFF, 4, 0xFF, 4, 0, 5)

[ 504](siwx91x-pinctrl_8h.md#ae23c01c208d25b7adff61126cd8a9bb9)#define ULPI2C\_SCL\_ULP7 SIWX91X\_GPIO(0xFF, 4, 0xFF, 4, 0, 7)

[ 505](siwx91x-pinctrl_8h.md#aa09786d189d39bae438faaeac7e7ea40)#define ULPI2C\_SCL\_ULP8 SIWX91X\_GPIO(0xFF, 4, 0xFF, 4, 0, 8)

[ 506](siwx91x-pinctrl_8h.md#af51f33d98c03ec5ef0b698587964ffdc)#define ULPI2C\_SDA\_PA6 SIWX91X\_GPIO(9, 4, 1, 0, 6, 0)

[ 507](siwx91x-pinctrl_8h.md#a1da79bff1ac03e9ddc46f4a944811448)#define ULPI2C\_SDA\_PA10 SIWX91X\_GPIO(9, 4, 5, 0, 10, 4)

[ 508](siwx91x-pinctrl_8h.md#a36585cdb68118eca6d3c58426cfad7fb)#define ULPI2C\_SDA\_PA12 SIWX91X\_GPIO(9, 4, 7, 0, 12, 6)

[ 509](siwx91x-pinctrl_8h.md#a13290c124ef3b3c6de2c1c21cc67e5a1)#define ULPI2C\_SDA\_PB9 SIWX91X\_GPIO(11, 4, 0, 1, 9, 6)

[ 510](siwx91x-pinctrl_8h.md#aaf4d086ed8396ac32e0471eca16d46cb)#define ULPI2C\_SDA\_PB12 SIWX91X\_GPIO(11, 4, 0, 1, 12, 9)

[ 511](siwx91x-pinctrl_8h.md#a94e3d4b225262962dd3738063e0fdae5)#define ULPI2C\_SDA\_PB14 SIWX91X\_GPIO(11, 4, 0, 1, 14, 11)

[ 512](siwx91x-pinctrl_8h.md#a9b8ed3fda4610401b659b401f91dfc9c)#define ULPI2C\_SDA\_PC15 SIWX91X\_GPIO(9, 4, 11, 2, 15, 9)

[ 513](siwx91x-pinctrl_8h.md#a3daddf6d96fd3ed8bd1deb929f765753)#define ULPI2C\_SDA\_PD1 SIWX91X\_GPIO(9, 4, 13, 3, 1, 11)

[ 514](siwx91x-pinctrl_8h.md#a683eac0b53a4a91c74c576b4f55a14c7)#define ULPI2C\_SDA\_ULP0 SIWX91X\_GPIO(0xFF, 4, 0xFF, 4, 0, 0)

[ 515](siwx91x-pinctrl_8h.md#a93cb9256a344d3e3c9e99f52512ea496)#define ULPI2C\_SDA\_ULP4 SIWX91X\_GPIO(0xFF, 4, 0xFF, 4, 0, 4)

[ 516](siwx91x-pinctrl_8h.md#a2bd7f63711f414953c3028e2c46e8713)#define ULPI2C\_SDA\_ULP6 SIWX91X\_GPIO(0xFF, 4, 0xFF, 4, 0, 6)

[ 517](siwx91x-pinctrl_8h.md#ab7ea0a99e98ac51c77077d342944342d)#define ULPI2C\_SDA\_ULP9 SIWX91X\_GPIO(0xFF, 4, 0xFF, 4, 0, 9)

[ 518](siwx91x-pinctrl_8h.md#a13be1329e1ed09001541f213841fa388)#define ULPI2C\_SDA\_ULP11 SIWX91X\_GPIO(0xFF, 4, 0xFF, 4, 0, 11)

519

[ 520](siwx91x-pinctrl_8h.md#acee499373da65ddab9e77442d312cd1e)#define ULPI2S\_CLK\_PA15 SIWX91X\_GPIO(9, 2, 8, 0, 15, 7)

[ 521](siwx91x-pinctrl_8h.md#ae750873ad84b404245b3a51c0096c468)#define ULPI2S\_CLK\_PB10 SIWX91X\_GPIO(11, 2, 0, 1, 10, 7)

[ 522](siwx91x-pinctrl_8h.md#a31913d264d0c43772cb967c836de75b6)#define ULPI2S\_CLK\_PB11 SIWX91X\_GPIO(11, 2, 0, 1, 11, 8)

[ 523](siwx91x-pinctrl_8h.md#a6c0035b9b825dbfe7cad3ac69dacfa50)#define ULPI2S\_CLK\_PC14 SIWX91X\_GPIO(9, 2, 10, 2, 14, 8)

[ 524](siwx91x-pinctrl_8h.md#af052bd9fc2183d48ff37b2c5bebe7f49)#define ULPI2S\_CLK\_ULP7 SIWX91X\_GPIO(0xFF, 2, 0xFF, 4, 0, 7)

[ 525](siwx91x-pinctrl_8h.md#a4d5eb6ab5c39069f6dcadd1b0bf61b59)#define ULPI2S\_CLK\_ULP8 SIWX91X\_GPIO(0xFF, 2, 0xFF, 4, 0, 8)

[ 526](siwx91x-pinctrl_8h.md#a5ad84aa1d0e4392951ea240925be0c80)#define ULPI2S\_DIN\_PA12 SIWX91X\_GPIO(9, 2, 7, 0, 12, 6)

[ 527](siwx91x-pinctrl_8h.md#a23e5c6841c9ef739812c7976ee7fe676)#define ULPI2S\_DIN\_PA6 SIWX91X\_GPIO(9, 2, 1, 0, 6, 0)

[ 528](siwx91x-pinctrl_8h.md#ac8c4bc0db055aae7f23d8c812595b0df)#define ULPI2S\_DIN\_PB9 SIWX91X\_GPIO(11, 2, 0, 1, 9, 6)

[ 529](siwx91x-pinctrl_8h.md#a49ba76efa4ac590f14e01c74f88b7258)#define ULPI2S\_DIN\_PB12 SIWX91X\_GPIO(11, 2, 0, 1, 12, 9)

[ 530](siwx91x-pinctrl_8h.md#a27376bff37852b4ccb412ca245748603)#define ULPI2S\_DIN\_PC15 SIWX91X\_GPIO(9, 2, 11, 2, 15, 9)

[ 531](siwx91x-pinctrl_8h.md#a97cbfeb16a7c46e12eae6891bc037acd)#define ULPI2S\_DIN\_ULP0 SIWX91X\_GPIO(0xFF, 2, 0xFF, 4, 0, 0)

[ 532](siwx91x-pinctrl_8h.md#aaf31db6c31214cc2c80cb309bdea5536)#define ULPI2S\_DIN\_ULP6 SIWX91X\_GPIO(0xFF, 2, 0xFF, 4, 0, 6)

[ 533](siwx91x-pinctrl_8h.md#ad2907e564c41e33f35c5d031b0405142)#define ULPI2S\_DIN\_ULP9 SIWX91X\_GPIO(0xFF, 2, 0xFF, 4, 0, 9)

[ 534](siwx91x-pinctrl_8h.md#a037b5a6c49a22926d22036065cba691f)#define ULPI2S\_DOUT\_PA7 SIWX91X\_GPIO(9, 2, 2, 0, 7, 1)

[ 535](siwx91x-pinctrl_8h.md#ada4743e53bf880176b49b7a9f7ea349c)#define ULPI2S\_DOUT\_PA11 SIWX91X\_GPIO(9, 2, 6, 0, 11, 5)

[ 536](siwx91x-pinctrl_8h.md#a1ad42ff0f6534663525ba85de482e26b)#define ULPI2S\_DOUT\_PB14 SIWX91X\_GPIO(11, 2, 0, 1, 14, 11)

[ 537](siwx91x-pinctrl_8h.md#aa100e33fa7343e145cb045caf46e11cb)#define ULPI2S\_DOUT\_PD1 SIWX91X\_GPIO(9, 2, 13, 3, 1, 11)

[ 538](siwx91x-pinctrl_8h.md#ab1a08eb6deb7154ef3b27aed5840f1c4)#define ULPI2S\_DOUT\_ULP1 SIWX91X\_GPIO(0xFF, 2, 0xFF, 4, 0, 1)

[ 539](siwx91x-pinctrl_8h.md#adb3fcaf4510f3e9e92d6b6938d5aa4b8)#define ULPI2S\_DOUT\_ULP5 SIWX91X\_GPIO(0xFF, 2, 0xFF, 4, 0, 5)

[ 540](siwx91x-pinctrl_8h.md#abf0c090bf283519422369f8cd6641155)#define ULPI2S\_DOUT\_ULP11 SIWX91X\_GPIO(0xFF, 2, 0xFF, 4, 0, 11)

[ 541](siwx91x-pinctrl_8h.md#a83e911f1451838534a149399c7478523)#define ULPI2S\_WS\_PA8 SIWX91X\_GPIO(9, 2, 3, 0, 8, 2)

[ 542](siwx91x-pinctrl_8h.md#aef2b6d091de86f951d895c2a3866307c)#define ULPI2S\_WS\_PA10 SIWX91X\_GPIO(9, 2, 5, 0, 10, 4)

[ 543](siwx91x-pinctrl_8h.md#a4ce87c401b2b76d9c9ef4e55667727f1)#define ULPI2S\_WS\_PB13 SIWX91X\_GPIO(11, 2, 0, 1, 13, 10)

[ 544](siwx91x-pinctrl_8h.md#ab430cb1429290f1714edcea8eff5401e)#define ULPI2S\_WS\_PD0 SIWX91X\_GPIO(9, 2, 12, 3, 0, 10)

[ 545](siwx91x-pinctrl_8h.md#a2a27e527e270fc114138715ce610f270)#define ULPI2S\_WS\_ULP2 SIWX91X\_GPIO(0xFF, 2, 0xFF, 4, 0, 2)

[ 546](siwx91x-pinctrl_8h.md#a914dbc1a9d523e19f639ef063aeb4dfe)#define ULPI2S\_WS\_ULP4 SIWX91X\_GPIO(0xFF, 2, 0xFF, 4, 0, 4)

[ 547](siwx91x-pinctrl_8h.md#a6990494758f0d836d985baf113547d44)#define ULPI2S\_WS\_ULP10 SIWX91X\_GPIO(0xFF, 2, 0xFF, 4, 0, 10)

548

[ 549](siwx91x-pinctrl_8h.md#ab67e998c1f4e90cf37c4d2fb51efb3ec)#define ULPSSI\_CLK\_PA6 SIWX91X\_GPIO(9, 1, 1, 0, 6, 0)

[ 550](siwx91x-pinctrl_8h.md#ad4d72e2973e10a5e24ad346e420add99)#define ULPSSI\_CLK\_PB11 SIWX91X\_GPIO(11, 1, 0, 1, 11, 8)

[ 551](siwx91x-pinctrl_8h.md#a8b098c13ead38441af6e03fdafefc75f)#define ULPSSI\_CLK\_PC14 SIWX91X\_GPIO(9, 1, 10, 2, 14, 8)

[ 552](siwx91x-pinctrl_8h.md#a3933d5b6f5464e2a22f466797725f5be)#define ULPSSI\_CLK\_ULP0 SIWX91X\_GPIO(0xFF, 1, 0xFF, 4, 0, 0)

[ 553](siwx91x-pinctrl_8h.md#ae811c5ecd3838c77460fafb9a47dc218)#define ULPSSI\_CLK\_ULP4 SIWX91X\_GPIO(0xFF, 8, 0xFF, 4, 0, 4)

[ 554](siwx91x-pinctrl_8h.md#ac1d6aedfec07ef370da615708fa5c98b)#define ULPSSI\_CLK\_ULP8 SIWX91X\_GPIO(0xFF, 1, 0xFF, 4, 0, 8)

[ 555](siwx91x-pinctrl_8h.md#a68ebe0e8328c9480a71a0f579e62730d)#define ULPSSI\_CS0\_PB13 SIWX91X\_GPIO(11, 1, 0, 1, 13, 10)

[ 556](siwx91x-pinctrl_8h.md#a5db74abc60ccc8e9d2f8458c2041d14a)#define ULPSSI\_CS0\_PD0 SIWX91X\_GPIO(9, 1, 12, 3, 0, 10)

[ 557](siwx91x-pinctrl_8h.md#aa8a8db9123876f6228cf83ff617d7fbb)#define ULPSSI\_CS0\_ULP7 SIWX91X\_GPIO(0xFF, 8, 0xFF, 4, 0, 7)

[ 558](siwx91x-pinctrl_8h.md#ae696d20e5ada658753a81995c196343f)#define ULPSSI\_CS0\_ULP10 SIWX91X\_GPIO(0xFF, 1, 0xFF, 4, 0, 10)

[ 559](siwx91x-pinctrl_8h.md#adbcc70df1b5e6ac6ed49b763dcb425ac)#define ULPSSI\_CS1\_PA10 SIWX91X\_GPIO(9, 1, 5, 0, 10, 4)

[ 560](siwx91x-pinctrl_8h.md#abcb850de6adc5db558bb9cb8a45455a6)#define ULPSSI\_CS1\_ULP4 SIWX91X\_GPIO(0xFF, 1, 0xFF, 4, 0, 4)

[ 561](siwx91x-pinctrl_8h.md#a64c23ccaf75e3e95a01631c64909fe5d)#define ULPSSI\_CS2\_PA12 SIWX91X\_GPIO(9, 1, 7, 0, 12, 6)

[ 562](siwx91x-pinctrl_8h.md#a517cb778af3ba2075498d0954f2b7baa)#define ULPSSI\_CS2\_PB9 SIWX91X\_GPIO(11, 1, 0, 1, 9, 6)

[ 563](siwx91x-pinctrl_8h.md#a3ddbf1e40ddfb1844a7c486b3d47a8fe)#define ULPSSI\_CS2\_ULP6 SIWX91X\_GPIO(0xFF, 1, 0xFF, 4, 0, 6)

[ 564](siwx91x-pinctrl_8h.md#a9b87925fffe06cd1d6a45bb9ca616206)#define ULPSSI\_DIN\_PA8 SIWX91X\_GPIO(9, 1, 3, 0, 8, 2)

[ 565](siwx91x-pinctrl_8h.md#aed755a9b7ca0f18144bf2b7ebbc9ec0e)#define ULPSSI\_DIN\_PB12 SIWX91X\_GPIO(11, 1, 0, 1, 12, 9)

[ 566](siwx91x-pinctrl_8h.md#a15babcff48e4a7ea9c15dbc107967bb1)#define ULPSSI\_DIN\_PC15 SIWX91X\_GPIO(9, 1, 11, 2, 15, 9)

[ 567](siwx91x-pinctrl_8h.md#a8a35f9ed548c01693de57b6647a55901)#define ULPSSI\_DIN\_ULP2 SIWX91X\_GPIO(0xFF, 1, 0xFF, 4, 0, 2)

[ 568](siwx91x-pinctrl_8h.md#a3737184b07cd6dfdef580a82b31ad13c)#define ULPSSI\_DIN\_ULP6 SIWX91X\_GPIO(0xFF, 8, 0xFF, 4, 0, 6)

[ 569](siwx91x-pinctrl_8h.md#a841bd6d9d7b267db55b85dbd63c29f19)#define ULPSSI\_DIN\_ULP9 SIWX91X\_GPIO(0xFF, 1, 0xFF, 4, 0, 9)

[ 570](siwx91x-pinctrl_8h.md#aca614b9427fd8199381f95d9eefd837f)#define ULPSSI\_DOUT\_PA7 SIWX91X\_GPIO(9, 1, 2, 0, 7, 1)

[ 571](siwx91x-pinctrl_8h.md#a979cc782fa4dcec1b2433931cf4c1e19)#define ULPSSI\_DOUT\_PB14 SIWX91X\_GPIO(11, 1, 0, 1, 14, 11)

[ 572](siwx91x-pinctrl_8h.md#aba1271a2cbd1b752f0ede3ee1b189248)#define ULPSSI\_DOUT\_PD1 SIWX91X\_GPIO(9, 1, 13, 3, 1, 11)

[ 573](siwx91x-pinctrl_8h.md#a7c49826415618d0edb0bf9960ab1390a)#define ULPSSI\_DOUT\_ULP1 SIWX91X\_GPIO(0xFF, 1, 0xFF, 4, 0, 1)

[ 574](siwx91x-pinctrl_8h.md#a3936c932181d9601015bfcd9ddbd9230)#define ULPSSI\_DOUT\_ULP5 SIWX91X\_GPIO(0xFF, 8, 0xFF, 4, 0, 5)

[ 575](siwx91x-pinctrl_8h.md#ae74ef587f76251d995250141665e0691)#define ULPSSI\_DOUT\_ULP11 SIWX91X\_GPIO(0xFF, 1, 0xFF, 4, 0, 11)

576

[ 577](siwx91x-pinctrl_8h.md#a0ed063f4b131388db88b333756b06808)#define ULPUART\_CTS\_PA7 SIWX91X\_GPIO(9, 3, 2, 0, 7, 1)

[ 578](siwx91x-pinctrl_8h.md#aa90657e0b4facbdaf8bee33186a3fd36)#define ULPUART\_CTS\_PA11 SIWX91X\_GPIO(9, 3, 6, 0, 11, 5)

[ 579](siwx91x-pinctrl_8h.md#a2e64111ab707cda699e7fbdada08f043)#define ULPUART\_CTS\_PB11 SIWX91X\_GPIO(11, 3, 0, 1, 11, 8)

[ 580](siwx91x-pinctrl_8h.md#ac963c8a203696c8a5eb30c4c802b242b)#define ULPUART\_CTS\_PC14 SIWX91X\_GPIO(9, 3, 10, 2, 14, 8)

[ 581](siwx91x-pinctrl_8h.md#acecb9492723712365609fe03429ecc62)#define ULPUART\_CTS\_ULP1 SIWX91X\_GPIO(0xFF, 3, 0xFF, 4, 0, 1)

[ 582](siwx91x-pinctrl_8h.md#a47991853f93de832cb85dba3dd51d689)#define ULPUART\_CTS\_ULP5 SIWX91X\_GPIO(0xFF, 3, 0xFF, 4, 0, 5)

[ 583](siwx91x-pinctrl_8h.md#ad87a42b5cac9d4e3e1539963c0a153ac)#define ULPUART\_CTS\_ULP8 SIWX91X\_GPIO(0xFF, 3, 0xFF, 4, 0, 8)

[ 584](siwx91x-pinctrl_8h.md#a294b8be88448128fe571f27b90d1fce2)#define ULPUART\_RTS\_PA6 SIWX91X\_GPIO(9, 3, 1, 0, 6, 0)

[ 585](siwx91x-pinctrl_8h.md#ae0930a91d0e55478a49361ff65b2f3cc)#define ULPUART\_RTS\_PA10 SIWX91X\_GPIO(9, 3, 5, 0, 10, 4)

[ 586](siwx91x-pinctrl_8h.md#a88c6a41e4846725b4557f1bb089adedb)#define ULPUART\_RTS\_PB13 SIWX91X\_GPIO(11, 3, 0, 1, 13, 10)

[ 587](siwx91x-pinctrl_8h.md#a0568003b61a32b6dadb5fe30b8edc985)#define ULPUART\_RTS\_PD0 SIWX91X\_GPIO(9, 3, 12, 3, 0, 10)

[ 588](siwx91x-pinctrl_8h.md#a6d637af94f43cbfcfd001b174d89504e)#define ULPUART\_RTS\_ULP0 SIWX91X\_GPIO(0xFF, 3, 0xFF, 4, 0, 0)

[ 589](siwx91x-pinctrl_8h.md#a905bfb63ed0825940db94f2d0e339cae)#define ULPUART\_RTS\_ULP4 SIWX91X\_GPIO(0xFF, 3, 0xFF, 4, 0, 4)

[ 590](siwx91x-pinctrl_8h.md#aafec5377fdddad88eaa5f33a616e932a)#define ULPUART\_RTS\_ULP10 SIWX91X\_GPIO(0xFF, 3, 0xFF, 4, 0, 10)

[ 591](siwx91x-pinctrl_8h.md#aeec10f85f14d8e9eb14c7bbd554d3deb)#define ULPUART\_RX\_PA8 SIWX91X\_GPIO(9, 3, 3, 0, 8, 2)

[ 592](siwx91x-pinctrl_8h.md#a47ff2fe3c3c669137e044e68e10f1e22)#define ULPUART\_RX\_PA12 SIWX91X\_GPIO(9, 3, 7, 0, 12, 6)

[ 593](siwx91x-pinctrl_8h.md#af7e7533272261fb52f29672d856bb78b)#define ULPUART\_RX\_PB9 SIWX91X\_GPIO(11, 3, 0, 1, 9, 6)

[ 594](siwx91x-pinctrl_8h.md#a0e7049eec99583a1a00725cdb2553be4)#define ULPUART\_RX\_PB12 SIWX91X\_GPIO(11, 3, 0, 1, 12, 9)

[ 595](siwx91x-pinctrl_8h.md#ae127c05aa9401ca90e626635b7645938)#define ULPUART\_RX\_PC15 SIWX91X\_GPIO(9, 3, 11, 2, 15, 9)

[ 596](siwx91x-pinctrl_8h.md#a5c296e125433a81362d207042b30cb7e)#define ULPUART\_RX\_ULP2 SIWX91X\_GPIO(0xFF, 3, 0xFF, 4, 0, 2)

[ 597](siwx91x-pinctrl_8h.md#a1036c7686c6ae59e387bf0df9338d8f6)#define ULPUART\_RX\_ULP6 SIWX91X\_GPIO(0xFF, 3, 0xFF, 4, 0, 6)

[ 598](siwx91x-pinctrl_8h.md#a3b868b8418ed39e8251a6d5e06da25ec)#define ULPUART\_RX\_ULP9 SIWX91X\_GPIO(0xFF, 3, 0xFF, 4, 0, 9)

[ 599](siwx91x-pinctrl_8h.md#a1e84b688037c2f705d70defdaffbc46a)#define ULPUART\_TX\_PA15 SIWX91X\_GPIO(9, 3, 8, 0, 15, 7)

[ 600](siwx91x-pinctrl_8h.md#a7cddc0cc77bf04fce6eac6174dfe45bf)#define ULPUART\_TX\_PB10 SIWX91X\_GPIO(11, 3, 0, 1, 10, 7)

[ 601](siwx91x-pinctrl_8h.md#a109bfbe4a758ba74ce6c3b376a3a50c6)#define ULPUART\_TX\_PB14 SIWX91X\_GPIO(11, 3, 0, 1, 14, 11)

[ 602](siwx91x-pinctrl_8h.md#a8802f354500cf3f55c7e8f8dff898d0c)#define ULPUART\_TX\_PD1 SIWX91X\_GPIO(9, 3, 13, 3, 1, 11)

[ 603](siwx91x-pinctrl_8h.md#a306f5e9ad2e84cee1074067cd6bccb4f)#define ULPUART\_TX\_ULP7 SIWX91X\_GPIO(0xFF, 3, 0xFF, 4, 0, 7)

[ 604](siwx91x-pinctrl_8h.md#a11b4b4459ff2d94267bca669da7e17cc)#define ULPUART\_TX\_ULP11 SIWX91X\_GPIO(0xFF, 3, 0xFF, 4, 0, 11)

605

[ 606](siwx91x-pinctrl_8h.md#a02c45c292ebe276e4f41101d7440480f)#define UULP\_GPIO4\_ULP2 SIWX91X\_GPIO(0xFF, 4, 0xFF, 4, 0, 2)

[ 607](siwx91x-pinctrl_8h.md#a003329462614c9ff939c451c28a011bc)#define UULP\_TESTMODE0\_ULP7 SIWX91X\_GPIO(0xFF, 11, 0xFF, 4, 0, 7)

[ 608](siwx91x-pinctrl_8h.md#aa927ee96be06692b7fecb88eec152357)#define UULP\_TESTMODE0\_ULP9 SIWX91X\_GPIO(0xFF, 5, 0xFF, 4, 0, 9)

609

610/\* clang-format on \*/

611

612/\* The following definitions are duplicates of signals that are also

613 \* available on the same pins using other GPIO modes.

614 \* #define IR\_OUTPUT\_ULP5 SIWX91X\_GPIO(0xFF, 10, 0xFF, 4, 0, 5)

615 \* #define PMU\_TEST2\_PB14 SIWX91X\_GPIO(13, 0xFF, 0, 1, 14, 0)

616 \* #define PWM\_1H\_ULP1 SIWX91X\_GPIO(8, 6, 23, 4, 1, 1)

617 \* #define PWM\_1L\_ULP0 SIWX91X\_GPIO(8, 6, 22, 4, 0, 0)

618 \*/

619

620#endif /\* INCLUDE\_ZEPHYR\_DT\_BINDINGS\_PINCTRL\_SILABS\_SIWX91X\_PINCTRL\_H\_ \*/

[silabs-pinctrl-siwx91x.h](silabs-pinctrl-siwx91x_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [pinctrl](dir_2c6c4fbd167577104b7f1b7148586168.md)
- [silabs](dir_fa47ec1716313d52a64832478c9daea4.md)
- [siwx91x-pinctrl.h](siwx91x-pinctrl_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
