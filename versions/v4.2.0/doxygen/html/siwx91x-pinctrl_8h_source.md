---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/siwx91x-pinctrl_8h_source.html
original_path: doxygen/html/siwx91x-pinctrl_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
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

[ 25](siwx91x-pinctrl_8h.md#a06a04fbcd9f9db43dd3b4c9be9ecc196)#define ADC\_TOPGPIO\_HP25 SIWX91X\_GPIO(14, 0xFF, 0, 1, 9, 0)

[ 26](siwx91x-pinctrl_8h.md#a1c85b141f986867590feab3e2971f83e)#define ADC\_TOPGPIO\_HP26 SIWX91X\_GPIO(14, 0xFF, 0, 1, 10, 0)

[ 27](siwx91x-pinctrl_8h.md#ab786befc793ba2dabbbc3c8abccdd81c)#define ADC\_TOPGPIO\_HP27 SIWX91X\_GPIO(14, 0xFF, 0, 1, 11, 0)

[ 28](siwx91x-pinctrl_8h.md#ac6f1ca16c8640f98a9d2eccafb282302)#define ADC\_TOPGPIO\_HP28 SIWX91X\_GPIO(14, 0xFF, 0, 1, 12, 0)

[ 29](siwx91x-pinctrl_8h.md#a919a3ea12132734ffbaa583eb814e70a)#define ADC\_TOPGPIO\_HP29 SIWX91X\_GPIO(14, 0xFF, 0, 1, 13, 0)

[ 30](siwx91x-pinctrl_8h.md#ac11f4dd52f4993a9ab70d16a50be47fa)#define ADC\_TOPGPIO\_HP30 SIWX91X\_GPIO(14, 0xFF, 0, 1, 14, 0)

31

[ 32](siwx91x-pinctrl_8h.md#ab03b635abc6f55d9824a6e0cf1a2c94e)#define AUXULP\_TRIG0\_HP11 SIWX91X\_GPIO(9, 5, 6, 0, 11, 5)

[ 33](siwx91x-pinctrl_8h.md#aad0ba7e32d1c8d4acbd6d2d1f4b288a0)#define AUXULP\_TRIG0\_HP30 SIWX91X\_GPIO(11, 5, 0, 1, 14, 11)

[ 34](siwx91x-pinctrl_8h.md#ae321eaa930b4bcdb847c6f0595e6f46f)#define AUXULP\_TRIG0\_HP49 SIWX91X\_GPIO(9, 5, 13, 3, 1, 11)

[ 35](siwx91x-pinctrl_8h.md#a945e911bffcedf2cd3e00b0394a990b1)#define AUXULP\_TRIG0\_ULP5 SIWX91X\_GPIO(0xFF, 5, 0xFF, 4, 0, 5)

[ 36](siwx91x-pinctrl_8h.md#a090807259f65186a27e1327fbf599829)#define AUXULP\_TRIG0\_ULP6 SIWX91X\_GPIO(0xFF, 10, 0xFF, 4, 0, 6)

[ 37](siwx91x-pinctrl_8h.md#ab92c286c8db594d8f607ce3ef09657b4)#define AUXULP\_TRIG0\_ULP11 SIWX91X\_GPIO(0xFF, 5, 0xFF, 4, 0, 11)

[ 38](siwx91x-pinctrl_8h.md#adf749c359174226e90d8a2ba64b4983c)#define AUXULP\_TRIG1\_ULP4 SIWX91X\_GPIO(0xFF, 5, 0xFF, 4, 0, 4)

[ 39](siwx91x-pinctrl_8h.md#a1d9a7c9bf69093de19cbdf10953e4c22)#define AUXULP\_TRIG1\_ULP7 SIWX91X\_GPIO(0xFF, 10, 0xFF, 4, 0, 7)

40

[ 41](siwx91x-pinctrl_8h.md#a835c36708762cd86818ce60b25384eb7)#define CLK\_I2SPLL\_HP27 SIWX91X\_GPIO(12, 0xFF, 0, 1, 11, 0)

[ 42](siwx91x-pinctrl_8h.md#aa4282adbc2f3da0006bde8511465bbff)#define CLK\_I2SPLL\_HP48 SIWX91X\_GPIO(10, 0xFF, 12, 3, 0, 0)

[ 43](siwx91x-pinctrl_8h.md#a000ce8a22cf34cb0bfbb6ae2e25e55bb)#define CLK\_I2SPLL\_HP54 SIWX91X\_GPIO(10, 0xFF, 18, 3, 6, 0)

[ 44](siwx91x-pinctrl_8h.md#a5d5b9c68af29a74c67fe4e002426d35c)#define CLK\_INTFPLL\_HP26 SIWX91X\_GPIO(12, 0xFF, 0, 1, 10, 0)

[ 45](siwx91x-pinctrl_8h.md#a7009a3f01b97860c58b29d0fc96f0df5)#define CLK\_INTFPLL\_HP47 SIWX91X\_GPIO(10, 0xFF, 11, 2, 15, 0)

[ 46](siwx91x-pinctrl_8h.md#a137db7b4fba3de386340ece21b67b3a2)#define CLK\_INTFPLL\_HP53 SIWX91X\_GPIO(10, 0xFF, 17, 3, 5, 0)

[ 47](siwx91x-pinctrl_8h.md#a679d7001a0e3864ccf0a879b5c4ccfc8)#define CLK\_MCUOUT\_HP11 SIWX91X\_GPIO(12, 0xFF, 6, 0, 11, 0)

[ 48](siwx91x-pinctrl_8h.md#a09924c650f824cca05e8b341ed9294ad)#define CLK\_MEMSREF\_HP50 SIWX91X\_GPIO(10, 0xFF, 14, 3, 2, 0)

[ 49](siwx91x-pinctrl_8h.md#afa68d89e38d316a3e729c371d8297bae)#define CLK\_MEMSREF\_HP56 SIWX91X\_GPIO(10, 0xFF, 20, 3, 8, 0)

[ 50](siwx91x-pinctrl_8h.md#aa413920e1935cc7bfb36235fa4055922)#define CLK\_OUT\_HP12 SIWX91X\_GPIO(8, 0xFF, 7, 0, 12, 0)

[ 51](siwx91x-pinctrl_8h.md#a32ffde4590651355db3a7411ed50d270)#define CLK\_OUT\_HP15 SIWX91X\_GPIO(8, 0xFF, 8, 0, 15, 0)

[ 52](siwx91x-pinctrl_8h.md#a880777fe8275592e91088d050512bff3)#define CLK\_PLLTESTMODE\_HP51 SIWX91X\_GPIO(10, 0xFF, 15, 3, 3, 0)

[ 53](siwx91x-pinctrl_8h.md#a92da5349a6b9ba8ea91ba8402bd685b2)#define CLK\_SOCPLL\_HP25 SIWX91X\_GPIO(12, 0xFF, 0, 1, 9, 0)

[ 54](siwx91x-pinctrl_8h.md#ad715b44d79cab97ac67f4ee4d7e3fd61)#define CLK\_SOCPLL\_HP46 SIWX91X\_GPIO(10, 0xFF, 10, 2, 14, 0)

[ 55](siwx91x-pinctrl_8h.md#ab0bda6530a625116653efc6ccdaf066e)#define CLK\_SOCPLL\_HP52 SIWX91X\_GPIO(10, 0xFF, 16, 3, 4, 0)

[ 56](siwx91x-pinctrl_8h.md#a898d24c287840df4a1d9b1f1d5bee3ca)#define CLK\_XTALONIN\_HP28 SIWX91X\_GPIO(12, 0xFF, 0, 1, 12, 0)

[ 57](siwx91x-pinctrl_8h.md#a5b9fea82548ee54a0a72cd10cad57b47)#define CLK\_XTALONIN\_HP57 SIWX91X\_GPIO(10, 0xFF, 21, 3, 9, 0)

58

[ 59](siwx91x-pinctrl_8h.md#aa4e79dc6178b13147dbeb10aaa6fbc6d)#define COMP1\_OUT\_HP8 SIWX91X\_GPIO(9, 5, 3, 0, 8, 2)

[ 60](siwx91x-pinctrl_8h.md#a67c405487bacc252498d58f92dd4e7f2)#define COMP1\_OUT\_HP28 SIWX91X\_GPIO(11, 5, 0, 1, 12, 9)

[ 61](siwx91x-pinctrl_8h.md#ad229716eda10b53eb40628b24bb84329)#define COMP1\_OUT\_HP47 SIWX91X\_GPIO(9, 5, 11, 2, 15, 9)

[ 62](siwx91x-pinctrl_8h.md#a5865a449e4957f10e35208b3a8a1e186)#define COMP1\_OUT\_ULP2 SIWX91X\_GPIO(0xFF, 5, 0xFF, 4, 0, 2)

[ 63](siwx91x-pinctrl_8h.md#a61a3d2a33b017f9b509e502fb14b5ac1)#define COMP1\_OUT\_ULP6 SIWX91X\_GPIO(0xFF, 9, 0xFF, 4, 0, 6)

[ 64](siwx91x-pinctrl_8h.md#a3de5ca3d0d7078a34cc53b5c5028d7c3)#define COMP2\_OUT\_ULP7 SIWX91X\_GPIO(0xFF, 9, 0xFF, 4, 0, 7)

65

[ 66](siwx91x-pinctrl_8h.md#a0d322c35cde263da2607b11c8dce74f1)#define GSPI\_CLK\_HP8 SIWX91X\_GPIO(4, 0xFF, 3, 0, 8, 0)

[ 67](siwx91x-pinctrl_8h.md#af45db40d737c46516891fc77bfd6991b)#define GSPI\_CLK\_HP25 SIWX91X\_GPIO(4, 0xFF, 0, 1, 9, 0)

[ 68](siwx91x-pinctrl_8h.md#a4adfba6b40f466fd220c52835338ff8f)#define GSPI\_CLK\_HP46 SIWX91X\_GPIO(4, 0xFF, 10, 2, 14, 0)

[ 69](siwx91x-pinctrl_8h.md#ab4e0b64c913aa9d1c5f9b8d7f7c564d1)#define GSPI\_CLK\_HP52 SIWX91X\_GPIO(4, 0xFF, 16, 3, 4, 0)

[ 70](siwx91x-pinctrl_8h.md#ada868d60b39f9ef5d58e3297b9569ebe)#define GSPI\_CS0\_HP9 SIWX91X\_GPIO(4, 0xFF, 4, 0, 9, 0)

[ 71](siwx91x-pinctrl_8h.md#a120041f6e17a7263e01a6cf9dbf97f55)#define GSPI\_CS0\_HP28 SIWX91X\_GPIO(4, 0xFF, 0, 1, 12, 0)

[ 72](siwx91x-pinctrl_8h.md#a9a136b1b51489fed94ebc601d1bce509)#define GSPI\_CS0\_HP49 SIWX91X\_GPIO(4, 0xFF, 13, 3, 1, 0)

[ 73](siwx91x-pinctrl_8h.md#aad59278f16c573afe6d988fec3e789ae)#define GSPI\_CS0\_HP53 SIWX91X\_GPIO(4, 0xFF, 17, 3, 5, 0)

[ 74](siwx91x-pinctrl_8h.md#a5fa623bbd9d1a30eec7af32587dd5ba1)#define GSPI\_CS1\_HP10 SIWX91X\_GPIO(4, 0xFF, 5, 0, 10, 0)

[ 75](siwx91x-pinctrl_8h.md#a5d6fc805d3e94783eb3eead3e46d3eb5)#define GSPI\_CS1\_HP29 SIWX91X\_GPIO(4, 0xFF, 0, 1, 13, 0)

[ 76](siwx91x-pinctrl_8h.md#a9fd3baadefec26d4e6532b3d22d6bfc6)#define GSPI\_CS1\_HP50 SIWX91X\_GPIO(4, 0xFF, 14, 3, 2, 0)

[ 77](siwx91x-pinctrl_8h.md#a9607f0a50a592087747f02d1dc6fe61e)#define GSPI\_CS1\_HP54 SIWX91X\_GPIO(4, 0xFF, 18, 3, 6, 0)

[ 78](siwx91x-pinctrl_8h.md#ad42cd6f9d902d0667f5a71ad2c7ead9a)#define GSPI\_CS2\_HP15 SIWX91X\_GPIO(4, 0xFF, 8, 0, 15, 0)

[ 79](siwx91x-pinctrl_8h.md#accbdbea1a397053ccc6a58d53ec8493c)#define GSPI\_CS2\_HP30 SIWX91X\_GPIO(4, 0xFF, 0, 1, 14, 0)

[ 80](siwx91x-pinctrl_8h.md#af7ff281165326d035233deb890fb9cb2)#define GSPI\_CS2\_HP51 SIWX91X\_GPIO(4, 0xFF, 15, 3, 3, 0)

[ 81](siwx91x-pinctrl_8h.md#a56ea3052bad2710a04055aa1306ef827)#define GSPI\_CS2\_HP55 SIWX91X\_GPIO(4, 0xFF, 19, 3, 7, 0)

[ 82](siwx91x-pinctrl_8h.md#a39e87f6b1067af1fd6eda77e0877c7dc)#define GSPI\_MISO\_HP11 SIWX91X\_GPIO(4, 0xFF, 6, 0, 11, 0)

[ 83](siwx91x-pinctrl_8h.md#ab9d92646ac5bfbd06eeab8727ce9f69c)#define GSPI\_MISO\_HP26 SIWX91X\_GPIO(4, 0xFF, 0, 1, 10, 0)

[ 84](siwx91x-pinctrl_8h.md#ace8e09dd531dab443c8e23567940c0c7)#define GSPI\_MISO\_HP47 SIWX91X\_GPIO(4, 0xFF, 11, 2, 15, 0)

[ 85](siwx91x-pinctrl_8h.md#ad922fdd48ef757e7ed84dc5ba0223b96)#define GSPI\_MISO\_HP56 SIWX91X\_GPIO(4, 0xFF, 20, 3, 8, 0)

[ 86](siwx91x-pinctrl_8h.md#a10573e8f0c7675c91a907c0f5e80a9cc)#define GSPI\_MOSI\_HP6 SIWX91X\_GPIO(12, 0xFF, 1, 0, 6, 0)

[ 87](siwx91x-pinctrl_8h.md#a4e70d4d9f4da18808231e1626a81aca4)#define GSPI\_MOSI\_HP12 SIWX91X\_GPIO(4, 0xFF, 7, 0, 12, 0)

[ 88](siwx91x-pinctrl_8h.md#a2ca232ad550d21add9adc2962a844b71)#define GSPI\_MOSI\_HP27 SIWX91X\_GPIO(4, 0xFF, 0, 1, 11, 0)

[ 89](siwx91x-pinctrl_8h.md#ad7925ac094c67ed0be2418d434869ac3)#define GSPI\_MOSI\_HP48 SIWX91X\_GPIO(4, 0xFF, 12, 3, 0, 0)

[ 90](siwx91x-pinctrl_8h.md#a80818466e12929450e71aec02cdd4c7b)#define GSPI\_MOSI\_HP57 SIWX91X\_GPIO(4, 0xFF, 21, 3, 9, 0)

91

[ 92](siwx91x-pinctrl_8h.md#a2ef351b47d12918bb4cea74c0e473db1)#define I2C0\_SCL\_HP7 SIWX91X\_GPIO(4, 0xFF, 2, 0, 7, 0)

[ 93](siwx91x-pinctrl_8h.md#ac8c62e3f52c598d1de82735a0809b0ad)#define I2C0\_SCL\_HP32 SIWX91X\_GPIO(11, 0xFF, 9, 2, 0, 0)

[ 94](siwx91x-pinctrl_8h.md#a820c81dfce3dff2287efa78305812b7f)#define I2C0\_SCL\_ULP1 SIWX91X\_GPIO(4, 6, 23, 4, 1, 1)

[ 95](siwx91x-pinctrl_8h.md#a480ff4a4f89b88de9c46001c7ad52aed)#define I2C0\_SCL\_ULP2 SIWX91X\_GPIO(4, 6, 24, 4, 2, 2)

[ 96](siwx91x-pinctrl_8h.md#a10e1bb6b59bfb1c4ca1932f9a4be1448)#define I2C0\_SCL\_ULP11 SIWX91X\_GPIO(4, 6, 33, 4, 11, 11)

[ 97](siwx91x-pinctrl_8h.md#a01c68c9f6c64829f15e5fe3e4fa4e7e7)#define I2C0\_SDA\_HP6 SIWX91X\_GPIO(4, 0xFF, 1, 0, 6, 0)

[ 98](siwx91x-pinctrl_8h.md#a9334871e0ff13605bf9fe104a8aa75f3)#define I2C0\_SDA\_HP31 SIWX91X\_GPIO(11, 0xFF, 9, 1, 15, 0)

[ 99](siwx91x-pinctrl_8h.md#a54e93e8958d5eb99c63ce1ad2cf17e75)#define I2C0\_SDA\_ULP0 SIWX91X\_GPIO(4, 6, 22, 4, 0, 0)

[ 100](siwx91x-pinctrl_8h.md#a3a53a6594da3d36f4c186864275cdb47)#define I2C0\_SDA\_ULP3 SIWX91X\_GPIO(4, 6, 25, 4, 3, 3)

[ 101](siwx91x-pinctrl_8h.md#a26710ae6de0a217c2d3af4cb7cc14b28)#define I2C0\_SDA\_ULP10 SIWX91X\_GPIO(4, 6, 32, 4, 10, 10)

102

[ 103](siwx91x-pinctrl_8h.md#aa5ba13c0b275c1d1fb28aed3fcd26f6a)#define I2C1\_SCL\_HP6 SIWX91X\_GPIO(5, 0xFF, 1, 0, 6, 0)

[ 104](siwx91x-pinctrl_8h.md#a24827fb9fdaa10b780a06c222062e522)#define I2C1\_SCL\_HP29 SIWX91X\_GPIO(5, 0xFF, 0, 1, 13, 0)

[ 105](siwx91x-pinctrl_8h.md#a936da856e3e3d0a8a67957c3e9a25519)#define I2C1\_SCL\_HP33 SIWX91X\_GPIO(11, 0xFF, 9, 2, 1, 0)

[ 106](siwx91x-pinctrl_8h.md#afe20556071663d815232b98293555fb7)#define I2C1\_SCL\_HP50 SIWX91X\_GPIO(5, 0xFF, 14, 3, 2, 0)

[ 107](siwx91x-pinctrl_8h.md#afdb3b18d7540906aca0a17187ce185b0)#define I2C1\_SCL\_HP54 SIWX91X\_GPIO(5, 0xFF, 18, 3, 6, 0)

[ 108](siwx91x-pinctrl_8h.md#aa79263584dd8d9ccd4ae7564cbb50fd7)#define I2C1\_SCL\_ULP0 SIWX91X\_GPIO(5, 6, 22, 4, 0, 0)

[ 109](siwx91x-pinctrl_8h.md#a1f40c8c4305f357477f61f2bee4177aa)#define I2C1\_SCL\_ULP2 SIWX91X\_GPIO(5, 6, 24, 4, 2, 2)

[ 110](siwx91x-pinctrl_8h.md#a34ac7a645ee7c80f1d291348bdaddb1b)#define I2C1\_SCL\_ULP6 SIWX91X\_GPIO(5, 6, 28, 4, 6, 6)

[ 111](siwx91x-pinctrl_8h.md#a7fdc374bc827cd67f954b638fb6ab03b)#define I2C1\_SDA\_HP7 SIWX91X\_GPIO(5, 0xFF, 2, 0, 7, 0)

[ 112](siwx91x-pinctrl_8h.md#a5d4d1af9ec0fab65e197d0f4ef9c4fc0)#define I2C1\_SDA\_HP30 SIWX91X\_GPIO(5, 0xFF, 0, 1, 14, 0)

[ 113](siwx91x-pinctrl_8h.md#aab52c1cbc805809cfe35199fb204867c)#define I2C1\_SDA\_HP34 SIWX91X\_GPIO(11, 0xFF, 9, 2, 2, 0)

[ 114](siwx91x-pinctrl_8h.md#a8889ee6d6d096a1b6790a71bb3f7db84)#define I2C1\_SDA\_HP51 SIWX91X\_GPIO(5, 0xFF, 15, 3, 3, 0)

[ 115](siwx91x-pinctrl_8h.md#a1aad71707a9c1adb14525b1809a97b31)#define I2C1\_SDA\_HP55 SIWX91X\_GPIO(5, 0xFF, 19, 3, 7, 0)

[ 116](siwx91x-pinctrl_8h.md#adc989b20626192997d54961dd616b3b2)#define I2C1\_SDA\_ULP1 SIWX91X\_GPIO(5, 6, 23, 4, 1, 1)

[ 117](siwx91x-pinctrl_8h.md#af66e09c1a67eeae142148952ffc620cb)#define I2C1\_SDA\_ULP3 SIWX91X\_GPIO(5, 6, 25, 4, 3, 3)

[ 118](siwx91x-pinctrl_8h.md#a187fb1dd9e7f233059c7602205112d62)#define I2C1\_SDA\_ULP7 SIWX91X\_GPIO(5, 6, 29, 4, 7, 7)

119

[ 120](siwx91x-pinctrl_8h.md#a7359e2ca7813b5abebd030d795e78706)#define I2S0\_CLK\_HP8 SIWX91X\_GPIO(7, 0xFF, 3, 0, 8, 0)

[ 121](siwx91x-pinctrl_8h.md#a5150fe8f89fdf656a051ba412f7ba9c3)#define I2S0\_CLK\_HP25 SIWX91X\_GPIO(7, 0xFF, 0, 1, 9, 0)

[ 122](siwx91x-pinctrl_8h.md#a0048da9c1376b56df1479b4689fe9de2)#define I2S0\_CLK\_HP46 SIWX91X\_GPIO(7, 0xFF, 10, 2, 14, 0)

[ 123](siwx91x-pinctrl_8h.md#aca6c330be2dc8f7b16abfa4b319cba5c)#define I2S0\_CLK\_HP52 SIWX91X\_GPIO(7, 0xFF, 16, 3, 4, 0)

[ 124](siwx91x-pinctrl_8h.md#a303d85325bbcc79992cfa1fda5cfae07)#define I2S0\_DIN0\_HP10 SIWX91X\_GPIO(7, 0xFF, 5, 0, 10, 0)

[ 125](siwx91x-pinctrl_8h.md#a2ac13eb02c917e2ca6a184bb3e9e38db)#define I2S0\_DIN0\_HP27 SIWX91X\_GPIO(7, 0xFF, 0, 1, 11, 0)

[ 126](siwx91x-pinctrl_8h.md#afb246a50f57470d46bb8a33a90be05ad)#define I2S0\_DIN0\_HP48 SIWX91X\_GPIO(7, 0xFF, 12, 3, 0, 0)

[ 127](siwx91x-pinctrl_8h.md#ac87ec8ad8ec8321d356d7678793851ab)#define I2S0\_DIN0\_HP56 SIWX91X\_GPIO(7, 0xFF, 20, 3, 8, 0)

[ 128](siwx91x-pinctrl_8h.md#a019d02d00ed9a9d254f3350e70577214)#define I2S0\_DIN1\_HP6 SIWX91X\_GPIO(7, 0xFF, 1, 0, 6, 0)

[ 129](siwx91x-pinctrl_8h.md#a8e6c2584e4f4c323fba1ddaf7c4271e6)#define I2S0\_DIN1\_HP29 SIWX91X\_GPIO(7, 0xFF, 0, 1, 13, 0)

[ 130](siwx91x-pinctrl_8h.md#a36408b9361281baa4b6df09e94da3d04)#define I2S0\_DIN1\_HP50 SIWX91X\_GPIO(7, 0xFF, 14, 3, 2, 0)

[ 131](siwx91x-pinctrl_8h.md#ad81fc920d9067bf3beaa1b42b1a819a6)#define I2S0\_DIN1\_HP54 SIWX91X\_GPIO(7, 0xFF, 18, 3, 6, 0)

[ 132](siwx91x-pinctrl_8h.md#aca53f49c7d835b65bcd2aefc344abe24)#define I2S0\_DOUT0\_HP11 SIWX91X\_GPIO(7, 0xFF, 6, 0, 11, 0)

[ 133](siwx91x-pinctrl_8h.md#a1f6afb833961353d943a469748a99bb3)#define I2S0\_DOUT0\_HP28 SIWX91X\_GPIO(7, 0xFF, 0, 1, 12, 0)

[ 134](siwx91x-pinctrl_8h.md#acac20029d1653abd303310ab5cfec88b)#define I2S0\_DOUT0\_HP49 SIWX91X\_GPIO(7, 0xFF, 13, 3, 1, 0)

[ 135](siwx91x-pinctrl_8h.md#aacd5f462222363c3ee0641ceaad3c9ac)#define I2S0\_DOUT0\_HP57 SIWX91X\_GPIO(7, 0xFF, 21, 3, 9, 0)

[ 136](siwx91x-pinctrl_8h.md#a9a165d304f050db860d42944f4288ec0)#define I2S0\_DOUT1\_HP7 SIWX91X\_GPIO(7, 0xFF, 2, 0, 7, 0)

[ 137](siwx91x-pinctrl_8h.md#a9b538a9b237871d89be0755a999a14aa)#define I2S0\_DOUT1\_HP29 SIWX91X\_GPIO(7, 0xFF, 0, 1, 14, 0)

[ 138](siwx91x-pinctrl_8h.md#ab6e059e2cb256557e26dedade8ce2aed)#define I2S0\_DOUT1\_HP51 SIWX91X\_GPIO(7, 0xFF, 15, 3, 3, 0)

[ 139](siwx91x-pinctrl_8h.md#abfe82c91355f572a5c4dc7dbb2e2f510)#define I2S0\_DOUT1\_HP55 SIWX91X\_GPIO(7, 0xFF, 19, 3, 7, 0)

[ 140](siwx91x-pinctrl_8h.md#a72f19d1ace618e6c2bae69c6a3f4c5f8)#define I2S0\_WS\_HP9 SIWX91X\_GPIO(7, 0xFF, 4, 0, 9, 0)

[ 141](siwx91x-pinctrl_8h.md#a614bbb3cbb8250a3f230806139dba0c9)#define I2S0\_WS\_HP26 SIWX91X\_GPIO(7, 0xFF, 0, 1, 10, 0)

[ 142](siwx91x-pinctrl_8h.md#a1b9f3a9dfbd36791be898036417e48bf)#define I2S0\_WS\_HP47 SIWX91X\_GPIO(7, 0xFF, 11, 2, 15, 0)

[ 143](siwx91x-pinctrl_8h.md#a63944069b8a3f30dc669f01dcc8c088c)#define I2S0\_WS\_HP53 SIWX91X\_GPIO(7, 0xFF, 17, 3, 5, 0)

144

[ 145](siwx91x-pinctrl_8h.md#a50e3d3f0baf17368823af4bf6a21dfb7)#define IR\_INPUT\_HP15 SIWX91X\_GPIO(9, 1, 8, 0, 15, 7)

[ 146](siwx91x-pinctrl_8h.md#acef80a4a997f5d5231e3f60856b864e1)#define IR\_INPUT\_HP26 SIWX91X\_GPIO(11, 1, 0, 1, 10, 7)

[ 147](siwx91x-pinctrl_8h.md#a5e4fc91a184b54b490bb615fdf3a25ab)#define IR\_INPUT\_HP29 SIWX91X\_GPIO(11, 4, 0, 1, 13, 10)

[ 148](siwx91x-pinctrl_8h.md#ac0035f0f87cbb64a9e0dbbadc61388e4)#define IR\_INPUT\_HP48 SIWX91X\_GPIO(9, 4, 12, 3, 0, 10)

[ 149](siwx91x-pinctrl_8h.md#a0d995f35796fc445efe7ebee649bdf2f)#define IR\_INPUT\_ULP4 SIWX91X\_GPIO(0xFF, 10, 0xFF, 4, 0, 4)

[ 150](siwx91x-pinctrl_8h.md#aadd97a3fa547212bd510340b3ab05c2d)#define IR\_INPUT\_ULP7 SIWX91X\_GPIO(0xFF, 1, 0xFF, 4, 0, 7)

[ 151](siwx91x-pinctrl_8h.md#a4c3793bc7cc985cf1f80aef136d18ce2)#define IR\_INPUT\_ULP10 SIWX91X\_GPIO(0xFF, 4, 0xFF, 4, 0, 10)

[ 152](siwx91x-pinctrl_8h.md#a2c041f872981f73b54ccf7af03aa8a36)#define IR\_OUTPUT\_HP11 SIWX91X\_GPIO(9, 1, 6, 0, 11, 5)

[ 153](siwx91x-pinctrl_8h.md#adb645e594a5654f35cbd3e852445e19b)#define IR\_OUTPUT\_ULP5 SIWX91X\_GPIO(0xFF, 1, 0xFF, 4, 0, 5)

154

[ 155](siwx91x-pinctrl_8h.md#a29207f055fc19e97082391195ef8cf78)#define PMU\_TEST1\_HP6 SIWX91X\_GPIO(8, 0xFF, 1, 0, 6, 0)

[ 156](siwx91x-pinctrl_8h.md#a87863eae390ce502e6c84ce7d1110874)#define PMU\_TEST1\_HP29 SIWX91X\_GPIO(8, 0xFF, 0, 1, 13, 0)

[ 157](siwx91x-pinctrl_8h.md#a01e9261c0bd8327120ae6da5686a6d3a)#define PMU\_TEST1\_HP30 SIWX91X\_GPIO(12, 0xFF, 0, 1, 14, 0)

[ 158](siwx91x-pinctrl_8h.md#a4055f713ecf4e2f57c49c57321fdff99)#define PMU\_TEST1\_ULP0 SIWX91X\_GPIO(13, 6, 22, 4, 0, 0)

[ 159](siwx91x-pinctrl_8h.md#a60de9f9f3085bee8341e118462a7fdcf)#define PMU\_TEST1\_ULP2 SIWX91X\_GPIO(10, 6, 24, 4, 2, 2)

[ 160](siwx91x-pinctrl_8h.md#ae687c8d547e498569a8b23f419216262)#define PMU\_TEST1\_ULP6 SIWX91X\_GPIO(12, 6, 28, 4, 6, 6)

[ 161](siwx91x-pinctrl_8h.md#a4cee250941565f3e3eb36b6d0a4e3364)#define PMU\_TEST1\_ULP10 SIWX91X\_GPIO(10, 6, 32, 4, 10, 10)

[ 162](siwx91x-pinctrl_8h.md#a928e861887b2162d1f000910d6454d53)#define PMU\_TEST2\_HP7 SIWX91X\_GPIO(8, 0xFF, 2, 0, 7, 0)

[ 163](siwx91x-pinctrl_8h.md#a49436320a6c491ae61450c6f71beec48)#define PMU\_TEST2\_HP30 SIWX91X\_GPIO(8, 0xFF, 0, 1, 14, 0)

[ 164](siwx91x-pinctrl_8h.md#ad3cdee5e821dc5b3c68e45ec4b49bfbe)#define PMU\_TEST2\_ULP1 SIWX91X\_GPIO(13, 6, 23, 4, 1, 1)

[ 165](siwx91x-pinctrl_8h.md#a9eae278334a605347f6e95e9250cc7e7)#define PMU\_TEST2\_ULP3 SIWX91X\_GPIO(10, 6, 25, 4, 3, 3)

[ 166](siwx91x-pinctrl_8h.md#a0510f2e9687d07fe386be8718198990c)#define PMU\_TEST2\_ULP7 SIWX91X\_GPIO(12, 6, 29, 4, 7, 7)

[ 167](siwx91x-pinctrl_8h.md#a810fcca28118ef6dff963923b9af34d9)#define PMU\_TEST2\_ULP11 SIWX91X\_GPIO(10, 6, 33, 4, 11, 11)

168

[ 169](siwx91x-pinctrl_8h.md#a676931253894b60c9d0f60a3c9a45380)#define PSRAM\_CLK\_HP46 SIWX91X\_GPIO(11, 0xFF, 10, 2, 14, 0)

[ 170](siwx91x-pinctrl_8h.md#a7a8e755805d8aef6a1c1202297527ceb)#define PSRAM\_CLK\_HP52 SIWX91X\_GPIO(12, 0xFF, 16, 3, 4, 0)

[ 171](siwx91x-pinctrl_8h.md#aa717c6eebeb0b80e410f405464a0e23a)#define PSRAM\_CSN0\_HP49 SIWX91X\_GPIO(11, 0xFF, 13, 3, 1, 0)

[ 172](siwx91x-pinctrl_8h.md#a1f0492fd0544bf8c1d01a534ee8b09dc)#define PSRAM\_CSN0\_HP55 SIWX91X\_GPIO(12, 0xFF, 19, 3, 7, 0)

[ 173](siwx91x-pinctrl_8h.md#a5160d8e3311dc7e81fc88035e30b1298)#define PSRAM\_CSN1\_HP53 SIWX91X\_GPIO(11, 0xFF, 17, 3, 5, 0)

[ 174](siwx91x-pinctrl_8h.md#a8505eee03f6dc307947fe9bba9cc868f)#define PSRAM\_D0\_HP47 SIWX91X\_GPIO(11, 0xFF, 11, 2, 15, 0)

[ 175](siwx91x-pinctrl_8h.md#a5d2e115dab81d01f2059f108ef43df66)#define PSRAM\_D0\_HP53 SIWX91X\_GPIO(12, 0xFF, 17, 3, 5, 0)

[ 176](siwx91x-pinctrl_8h.md#ae039ebfbbcb4f8d9c2941fad9cf21c25)#define PSRAM\_D1\_HP48 SIWX91X\_GPIO(11, 0xFF, 12, 3, 0, 0)

[ 177](siwx91x-pinctrl_8h.md#a660ebada1169b4d19a0876b985e04a06)#define PSRAM\_D1\_HP54 SIWX91X\_GPIO(12, 0xFF, 18, 3, 6, 0)

[ 178](siwx91x-pinctrl_8h.md#ab5bee0e001079fbd5fb0d974942aa598)#define PSRAM\_D2\_HP50 SIWX91X\_GPIO(11, 0xFF, 14, 3, 2, 0)

[ 179](siwx91x-pinctrl_8h.md#acaed40bf53fd610ef38615a15cc24774)#define PSRAM\_D2\_HP56 SIWX91X\_GPIO(12, 0xFF, 20, 3, 8, 0)

[ 180](siwx91x-pinctrl_8h.md#a19bf5beb8bca44b470e155431c0244a7)#define PSRAM\_D3\_HP51 SIWX91X\_GPIO(11, 0xFF, 15, 3, 3, 0)

[ 181](siwx91x-pinctrl_8h.md#a2630b64edaffea76cf3a071d31494c00)#define PSRAM\_D3\_HP57 SIWX91X\_GPIO(12, 0xFF, 21, 3, 9, 0)

[ 182](siwx91x-pinctrl_8h.md#ae3d2d17a5bd7b4c09c17cefe9febce73)#define PSRAM\_D4\_HP54 SIWX91X\_GPIO(11, 0xFF, 18, 3, 6, 0)

[ 183](siwx91x-pinctrl_8h.md#a1ca55c42f77714d9c1088b200dc9dc8f)#define PSRAM\_D5\_HP55 SIWX91X\_GPIO(11, 0xFF, 19, 3, 7, 0)

[ 184](siwx91x-pinctrl_8h.md#a9cb3582c88b3d07af732ebdcb239ba7b)#define PSRAM\_D6\_HP56 SIWX91X\_GPIO(11, 0xFF, 20, 3, 8, 0)

[ 185](siwx91x-pinctrl_8h.md#a9e255793e353deb52e77a03359580322)#define PSRAM\_D7\_HP57 SIWX91X\_GPIO(11, 0xFF, 21, 3, 9, 0)

186

[ 187](siwx91x-pinctrl_8h.md#ae04b42ec4c9f7b009a5a06a3ec01b35b)#define PWM\_0H\_HP7 SIWX91X\_GPIO(10, 0xFF, 2, 0, 7, 0)

[ 188](siwx91x-pinctrl_8h.md#a0fd1688f5f60e0a874ce283a18713e7a)#define PWM\_0H\_ULP1 SIWX91X\_GPIO(12, 6, 23, 4, 1, 1)

[ 189](siwx91x-pinctrl_8h.md#a38fdb4b305f7ae6afb490118d52ef9bc)#define PWM\_0L\_HP6 SIWX91X\_GPIO(10, 0xFF, 1, 0, 6, 0)

[ 190](siwx91x-pinctrl_8h.md#aa94e0a3dce4a99d76a019a0bf168e004)#define PWM\_0L\_ULP0 SIWX91X\_GPIO(12, 6, 22, 4, 0, 0)

[ 191](siwx91x-pinctrl_8h.md#acde3e8d6e27699ac4e8637813c6db6c9)#define PWM\_1H\_HP9 SIWX91X\_GPIO(10, 0xFF, 4, 0, 9, 0)

[ 192](siwx91x-pinctrl_8h.md#ad11994d9f6d4ee1aecc042f61f720b42)#define PWM\_1H\_ULP3 SIWX91X\_GPIO(8, 6, 25, 4, 3, 3)

[ 193](siwx91x-pinctrl_8h.md#aeb72ce214bbeac3fea2296177e436cf0)#define PWM\_1H\_ULP5 SIWX91X\_GPIO(12, 6, 27, 4, 5, 5)

[ 194](siwx91x-pinctrl_8h.md#ae5b9d0282a760965899a0c163f58423c)#define PWM\_1L\_HP8 SIWX91X\_GPIO(10, 0xFF, 3, 0, 8, 0)

[ 195](siwx91x-pinctrl_8h.md#a9e79d0a4b569d73d5ee7f65c1e2f20fc)#define PWM\_1L\_ULP2 SIWX91X\_GPIO(8, 6, 24, 4, 2, 2)

[ 196](siwx91x-pinctrl_8h.md#ab07ed6a6db4d9a7bdcb79d9d08635055)#define PWM\_1L\_ULP4 SIWX91X\_GPIO(12, 6, 26, 4, 4, 4)

[ 197](siwx91x-pinctrl_8h.md#a840701d4644973e31b0c49caa1fb52ce)#define PWM\_2H\_HP11 SIWX91X\_GPIO(10, 0xFF, 6, 0, 11, 0)

[ 198](siwx91x-pinctrl_8h.md#abf08c72c301bfd555f41e34b99f2076e)#define PWM\_2H\_ULP5 SIWX91X\_GPIO(8, 6, 27, 4, 5, 5)

[ 199](siwx91x-pinctrl_8h.md#a7c60a35ecb5f5dc6448a96b3e3c89baf)#define PWM\_2L\_HP10 SIWX91X\_GPIO(10, 0xFF, 5, 0, 10, 0)

[ 200](siwx91x-pinctrl_8h.md#ac8708b22008c4408a38456f7b8258328)#define PWM\_2L\_ULP4 SIWX91X\_GPIO(8, 6, 26, 4, 4, 4)

[ 201](siwx91x-pinctrl_8h.md#a507ec5bf9c637916ca37dee6de1d1a96)#define PWM\_3H\_HP15 SIWX91X\_GPIO(10, 0xFF, 8, 0, 15, 0)

[ 202](siwx91x-pinctrl_8h.md#aea69719dd1cfa3a94f9f3a30459b51ed)#define PWM\_3H\_ULP7 SIWX91X\_GPIO(8, 6, 29, 4, 7, 7)

[ 203](siwx91x-pinctrl_8h.md#ae8d79d461423e0353022eab80c3025c8)#define PWM\_3L\_HP12 SIWX91X\_GPIO(10, 0xFF, 7, 0, 12, 0)

[ 204](siwx91x-pinctrl_8h.md#ac6590ab64265b8c3bad3d30da7620604)#define PWM\_3L\_ULP6 SIWX91X\_GPIO(8, 6, 28, 4, 6, 6)

[ 205](siwx91x-pinctrl_8h.md#a4508139ab59dee416bd0aa7a53f2e2d5)#define PWM\_EXTTRIG0\_HP27 SIWX91X\_GPIO(10, 0xFF, 0, 1, 11, 0)

[ 206](siwx91x-pinctrl_8h.md#a92c8c16ef38b80853b297d31a6dd4964)#define PWM\_EXTTRIG0\_HP51 SIWX91X\_GPIO(8, 0xFF, 15, 3, 3, 0)

[ 207](siwx91x-pinctrl_8h.md#a65e5a78cc5cc390a802818a4f19ae8d4)#define PWM\_EXTTRIG0\_ULP6 SIWX91X\_GPIO(10, 6, 28, 4, 6, 6)

[ 208](siwx91x-pinctrl_8h.md#ac991e3bbd300bb3fb9b27a1d8d7fc5f2)#define PWM\_EXTTRIG0\_ULP11 SIWX91X\_GPIO(8, 6, 33, 4, 11, 11)

[ 209](siwx91x-pinctrl_8h.md#a0d191c0b60c2b836e3856a0e5c434649)#define PWM\_EXTTRIG1\_HP28 SIWX91X\_GPIO(10, 0xFF, 0, 1, 12, 0)

[ 210](siwx91x-pinctrl_8h.md#afb4d7dfd327df023d9e3268678d3313e)#define PWM\_EXTTRIG1\_HP54 SIWX91X\_GPIO(8, 0xFF, 18, 3, 6, 0)

[ 211](siwx91x-pinctrl_8h.md#a5d8597d305f1ac3b6f5ed8b5b85da936)#define PWM\_EXTTRIG1\_ULP7 SIWX91X\_GPIO(10, 6, 29, 4, 7, 7)

[ 212](siwx91x-pinctrl_8h.md#a0516ffe89d34afcebe7b594def541e37)#define PWM\_EXTTRIG2\_HP29 SIWX91X\_GPIO(10, 0xFF, 0, 1, 13, 0)

[ 213](siwx91x-pinctrl_8h.md#a7c46b667cc3ce330c6d75f79f97b764b)#define PWM\_EXTTRIG2\_HP55 SIWX91X\_GPIO(8, 0xFF, 19, 3, 7, 0)

[ 214](siwx91x-pinctrl_8h.md#a83421e64cf0f348be8cce195d0eb27c1)#define PWM\_EXTTRIG2\_ULP8 SIWX91X\_GPIO(10, 6, 30, 4, 8, 8)

[ 215](siwx91x-pinctrl_8h.md#a478e0230aa6373a816bfbf4c6ec5da96)#define PWM\_EXTTRIG3\_HP30 SIWX91X\_GPIO(10, 0xFF, 0, 1, 14, 0)

[ 216](siwx91x-pinctrl_8h.md#ac4b0686f2db1db395ff0ffba43e7e1b7)#define PWM\_EXTTRIG3\_HP50 SIWX91X\_GPIO(8, 0xFF, 14, 3, 2, 0)

[ 217](siwx91x-pinctrl_8h.md#a5c3cf988f7d14ecaca8e02734cb15eee)#define PWM\_EXTTRIG3\_ULP9 SIWX91X\_GPIO(10, 6, 31, 4, 9, 9)

[ 218](siwx91x-pinctrl_8h.md#a73af0f23d97c3f7c3466e29be238d2e9)#define PWM\_FAULTA\_HP25 SIWX91X\_GPIO(10, 0xFF, 0, 1, 9, 0)

[ 219](siwx91x-pinctrl_8h.md#a1be2559bbd5c14e4b8d02fae6d834db3)#define PWM\_FAULTA\_ULP4 SIWX91X\_GPIO(10, 6, 26, 4, 4, 4)

[ 220](siwx91x-pinctrl_8h.md#a898809d281a1451c860755372034ac14)#define PWM\_FAULTA\_ULP9 SIWX91X\_GPIO(8, 6, 31, 4, 9, 9)

[ 221](siwx91x-pinctrl_8h.md#a2d00f4de6aa3fe5ba797a8a50fd16751)#define PWM\_FAULTB\_HP26 SIWX91X\_GPIO(10, 0xFF, 0, 1, 10, 0)

[ 222](siwx91x-pinctrl_8h.md#ad631deeca8cc40fcc2df48ec50297c9f)#define PWM\_FAULTB\_ULP5 SIWX91X\_GPIO(10, 6, 27, 4, 5, 5)

[ 223](siwx91x-pinctrl_8h.md#a4bfb8e85f37893aceed66e457c34b9bd)#define PWM\_FAULTB\_ULP10 SIWX91X\_GPIO(8, 6, 32, 4, 10, 10)

[ 224](siwx91x-pinctrl_8h.md#a4f0903ae305c9bf1a9808b139a537a5d)#define PWM\_SLEEPEVENT\_ULP8 SIWX91X\_GPIO(8, 6, 30, 4, 8, 8)

225

[ 226](siwx91x-pinctrl_8h.md#ab648897fd2173a6306ea1f12581a5257)#define QEI\_DIR\_HP11 SIWX91X\_GPIO(5, 0xFF, 6, 0, 11, 0)

[ 227](siwx91x-pinctrl_8h.md#acc5868c473301e8556cddd9d867bd0fe)#define QEI\_DIR\_HP28 SIWX91X\_GPIO(5, 0xFF, 0, 1, 12, 0)

[ 228](siwx91x-pinctrl_8h.md#a7fcabffea8d0e7f0ca1d7b3b53c77554)#define QEI\_DIR\_HP34 SIWX91X\_GPIO(13, 0xFF, 9, 2, 2, 0)

[ 229](siwx91x-pinctrl_8h.md#ac0df08c2fad11c4d658d9f715d610bbe)#define QEI\_DIR\_HP49 SIWX91X\_GPIO(3, 0xFF, 13, 3, 1, 0)

[ 230](siwx91x-pinctrl_8h.md#aecd388fd3a1c7d76cbc3b058d333fbdc)#define QEI\_DIR\_HP57 SIWX91X\_GPIO(5, 0xFF, 21, 3, 9, 0)

[ 231](siwx91x-pinctrl_8h.md#a6be591b8ce2f422f66e10e7c1591e835)#define QEI\_DIR\_ULP3 SIWX91X\_GPIO(3, 6, 25, 4, 3, 3)

[ 232](siwx91x-pinctrl_8h.md#a0d53fec86fc5cd9aa5b094d0f6e8229b)#define QEI\_DIR\_ULP7 SIWX91X\_GPIO(3, 6, 29, 4, 7, 7)

[ 233](siwx91x-pinctrl_8h.md#a6bcd0fd50eb5acfbd616b96a041a8b40)#define QEI\_DIR\_ULP11 SIWX91X\_GPIO(3, 6, 33, 4, 11, 11)

[ 234](siwx91x-pinctrl_8h.md#a3023c95f055645c0c988b5578d7943eb)#define QEI\_IDX\_HP8 SIWX91X\_GPIO(5, 0xFF, 3, 0, 8, 0)

[ 235](siwx91x-pinctrl_8h.md#aca6d952fdb3eb1bd2c9fcd088770e482)#define QEI\_IDX\_HP31 SIWX91X\_GPIO(13, 0xFF, 9, 1, 15, 0)

[ 236](siwx91x-pinctrl_8h.md#a41c53b072b0975e7b39725a0cedd6b49)#define QEI\_IDX\_HP25 SIWX91X\_GPIO(5, 0xFF, 0, 1, 9, 0)

[ 237](siwx91x-pinctrl_8h.md#aa2f488c074c7133f4457594dc8f57000)#define QEI\_IDX\_HP46 SIWX91X\_GPIO(3, 0xFF, 10, 2, 14, 0)

[ 238](siwx91x-pinctrl_8h.md#a0637cea93d1c922d3540551a92b5e8d6)#define QEI\_IDX\_HP52 SIWX91X\_GPIO(5, 0xFF, 16, 3, 4, 0)

[ 239](siwx91x-pinctrl_8h.md#aa5571fa3facfca9e58accb575a8aa14b)#define QEI\_IDX\_ULP0 SIWX91X\_GPIO(3, 6, 22, 4, 0, 0)

[ 240](siwx91x-pinctrl_8h.md#a5e4085d82f00810d0d8a0c79bae2fb8b)#define QEI\_IDX\_ULP4 SIWX91X\_GPIO(3, 6, 26, 4, 4, 4)

[ 241](siwx91x-pinctrl_8h.md#ade023149f5a2daf2c21d2a5b8db31ebf)#define QEI\_IDX\_ULP8 SIWX91X\_GPIO(3, 6, 30, 4, 8, 8)

[ 242](siwx91x-pinctrl_8h.md#a7c2638ce5bd7fe1fc3aed00841ebf805)#define QEI\_PHA\_HP9 SIWX91X\_GPIO(5, 0xFF, 4, 0, 9, 0)

[ 243](siwx91x-pinctrl_8h.md#afd774767dbccf18955aa2acd8fe3f27c)#define QEI\_PHA\_HP26 SIWX91X\_GPIO(5, 0xFF, 0, 1, 10, 0)

[ 244](siwx91x-pinctrl_8h.md#a1e7b4deeddd4e6139fee6a55752cff49)#define QEI\_PHA\_HP32 SIWX91X\_GPIO(13, 0xFF, 9, 2, 0, 0)

[ 245](siwx91x-pinctrl_8h.md#a9442f432d1602296f6ca19c43f4e4e32)#define QEI\_PHA\_HP47 SIWX91X\_GPIO(3, 0xFF, 11, 2, 15, 0)

[ 246](siwx91x-pinctrl_8h.md#ab6729735aa0f81049c357142ce64a3fb)#define QEI\_PHA\_HP53 SIWX91X\_GPIO(5, 0xFF, 17, 3, 5, 0)

[ 247](siwx91x-pinctrl_8h.md#a02cd57249ab4cbe4ac6f50bf4ac4640d)#define QEI\_PHA\_ULP1 SIWX91X\_GPIO(3, 6, 23, 4, 1, 1)

[ 248](siwx91x-pinctrl_8h.md#a05d2c45f5f6f8e6caa749fa62f8952d2)#define QEI\_PHA\_ULP5 SIWX91X\_GPIO(3, 6, 27, 4, 5, 5)

[ 249](siwx91x-pinctrl_8h.md#a4e7d6e023c35e3c9afe66dea3c777f2f)#define QEI\_PHA\_ULP9 SIWX91X\_GPIO(3, 6, 31, 4, 9, 9)

[ 250](siwx91x-pinctrl_8h.md#aeb1bc91f700271730e3ef17a2c0f2713)#define QEI\_PHB\_HP10 SIWX91X\_GPIO(5, 0xFF, 5, 0, 10, 0)

[ 251](siwx91x-pinctrl_8h.md#a1df3d67f2727fb71a0639c352b397154)#define QEI\_PHB\_HP27 SIWX91X\_GPIO(5, 0xFF, 0, 1, 11, 0)

[ 252](siwx91x-pinctrl_8h.md#a46fa92c9b2cb1139dc6d436251d238c9)#define QEI\_PHB\_HP33 SIWX91X\_GPIO(13, 0xFF, 9, 2, 1, 0)

[ 253](siwx91x-pinctrl_8h.md#a19b95ea8cddcf086fc2ffe5a46d43f13)#define QEI\_PHB\_HP48 SIWX91X\_GPIO(3, 0xFF, 12, 3, 0, 0)

[ 254](siwx91x-pinctrl_8h.md#a8a2ebd9d12f75fd4fef28190c03c4e60)#define QEI\_PHB\_HP56 SIWX91X\_GPIO(5, 0xFF, 20, 3, 8, 0)

[ 255](siwx91x-pinctrl_8h.md#af323d2f63b6a1e26b9aa05a64c74ffbf)#define QEI\_PHB\_ULP2 SIWX91X\_GPIO(3, 6, 24, 4, 2, 2)

[ 256](siwx91x-pinctrl_8h.md#addcd05ab910922d7924bf01b643bec87)#define QEI\_PHB\_ULP6 SIWX91X\_GPIO(3, 6, 28, 4, 6, 6)

[ 257](siwx91x-pinctrl_8h.md#a2b7eafbd2fdae8fc813ebebbd912539b)#define QEI\_PHB\_ULP10 SIWX91X\_GPIO(3, 6, 32, 4, 10, 10)

258

[ 259](siwx91x-pinctrl_8h.md#a9c3d01a17c03a4a1facc7a06453e1cf9)#define QSPI\_CLK\_HP8 SIWX91X\_GPIO(11, 0xFF, 3, 0, 8, 0)

[ 260](siwx91x-pinctrl_8h.md#a7672e6df6d9de5ba6945492cf635ccb0)#define QSPI\_CLK\_HP46 SIWX91X\_GPIO(1, 0xFF, 10, 2, 14, 0)

[ 261](siwx91x-pinctrl_8h.md#a0f23032eac930624c7ec43e5be873ff5)#define QSPI\_CLK\_HP52 SIWX91X\_GPIO(9, 0xFF, 16, 3, 4, 0)

[ 262](siwx91x-pinctrl_8h.md#a821ba16d8ff315bad8999a6e6ec219a8)#define QSPI\_CSN0\_HP7 SIWX91X\_GPIO(11, 0xFF, 2, 0, 7, 0)

[ 263](siwx91x-pinctrl_8h.md#a96e4e990dd6f716ae41bbfb560b36b0e)#define QSPI\_CSN0\_HP49 SIWX91X\_GPIO(1, 0xFF, 13, 3, 1, 0)

[ 264](siwx91x-pinctrl_8h.md#a12adeb047d22f21a55a9c33d434f5876)#define QSPI\_CSN0\_HP55 SIWX91X\_GPIO(9, 0xFF, 19, 3, 7, 0)

[ 265](siwx91x-pinctrl_8h.md#ab67034dc6fe34b9cdf4b6623e06ce0b0)#define QSPI\_CSN1\_HP7 SIWX91X\_GPIO(12, 0xFF, 2, 0, 7, 0)

[ 266](siwx91x-pinctrl_8h.md#a41005274eb64b874b2bc57bf75de0ea2)#define QSPI\_CSN1\_HP53 SIWX91X\_GPIO(1, 0xFF, 17, 3, 5, 0)

[ 267](siwx91x-pinctrl_8h.md#a532ec03ed4eef5b2830ec449eed145dc)#define QSPI\_CSN9\_HP49 SIWX91X\_GPIO(10, 0xFF, 13, 3, 1, 0)

[ 268](siwx91x-pinctrl_8h.md#a776bb46ee650922c9d8d6bf0796cf2b9)#define QSPI\_D0\_HP6 SIWX91X\_GPIO(11, 0xFF, 1, 0, 6, 0)

[ 269](siwx91x-pinctrl_8h.md#a6a443443e9195422d2aefe95d62263c3)#define QSPI\_D0\_HP47 SIWX91X\_GPIO(1, 0xFF, 11, 2, 15, 0)

[ 270](siwx91x-pinctrl_8h.md#a29fe7871dbef16e0f98dea867e444c90)#define QSPI\_D0\_HP53 SIWX91X\_GPIO(9, 0xFF, 17, 3, 5, 0)

[ 271](siwx91x-pinctrl_8h.md#ac8616e792c4715d73899701b08aabdad)#define QSPI\_D1\_HP9 SIWX91X\_GPIO(11, 0xFF, 4, 0, 9, 0)

[ 272](siwx91x-pinctrl_8h.md#abdb757e9c432a11b30649f5a09a8c896)#define QSPI\_D1\_HP48 SIWX91X\_GPIO(1, 0xFF, 12, 3, 0, 0)

[ 273](siwx91x-pinctrl_8h.md#ab0dffa76350eeeb2d3eb9c0adbdb9088)#define QSPI\_D1\_HP54 SIWX91X\_GPIO(9, 0xFF, 18, 3, 6, 0)

[ 274](siwx91x-pinctrl_8h.md#aa32be2bfcdea9856c7c50606245cc74e)#define QSPI\_D2\_HP10 SIWX91X\_GPIO(11, 0xFF, 5, 0, 10, 0)

[ 275](siwx91x-pinctrl_8h.md#aee6e6ee41ebe13d44d0264f337d3db4f)#define QSPI\_D2\_HP50 SIWX91X\_GPIO(1, 0xFF, 14, 3, 2, 0)

[ 276](siwx91x-pinctrl_8h.md#a08c29c30a534bbb0f24d91d76f96f41a)#define QSPI\_D2\_HP56 SIWX91X\_GPIO(9, 0xFF, 20, 3, 8, 0)

[ 277](siwx91x-pinctrl_8h.md#a5c85e86968bbd77e4fa2797af059ff59)#define QSPI\_D3\_HP11 SIWX91X\_GPIO(11, 0xFF, 6, 0, 11, 0)

[ 278](siwx91x-pinctrl_8h.md#a966ce19ae5d27c19817c06dd865d643a)#define QSPI\_D3\_HP51 SIWX91X\_GPIO(1, 0xFF, 15, 3, 3, 0)

[ 279](siwx91x-pinctrl_8h.md#ae4a6bb7540deaa29fc63cfe9ac5b6650)#define QSPI\_D3\_HP57 SIWX91X\_GPIO(9, 0xFF, 21, 3, 9, 0)

[ 280](siwx91x-pinctrl_8h.md#ab02591e8fcb3a366d42b0507ebdd218b)#define QSPI\_D4\_HP54 SIWX91X\_GPIO(1, 0xFF, 18, 3, 6, 0)

[ 281](siwx91x-pinctrl_8h.md#a1a35413b75de975a97da3321a0c0072e)#define QSPI\_D5\_HP55 SIWX91X\_GPIO(1, 0xFF, 19, 3, 7, 0)

[ 282](siwx91x-pinctrl_8h.md#a4380587dc3fa09f5908edcd48fa26aa3)#define QSPI\_D6\_HP56 SIWX91X\_GPIO(1, 0xFF, 20, 3, 8, 0)

[ 283](siwx91x-pinctrl_8h.md#adad1d5fd641d6eaa11653eb7fa821b2e)#define QSPI\_D7\_HP57 SIWX91X\_GPIO(1, 0xFF, 21, 3, 9, 0)

284

[ 285](siwx91x-pinctrl_8h.md#aa062df96d3fd76dfde6eeb4e0a882278)#define SCT\_IN0\_HP25 SIWX91X\_GPIO(9, 0xFF, 0, 1, 9, 0)

[ 286](siwx91x-pinctrl_8h.md#a99b69d8a4f849a64b236986a2abc21c9)#define SCT\_IN0\_ULP0 SIWX91X\_GPIO(7, 6, 22, 4, 0, 0)

[ 287](siwx91x-pinctrl_8h.md#a3ab3d2e1f5a11a5386b700f03cf98b59)#define SCT\_IN0\_ULP4 SIWX91X\_GPIO(9, 6, 26, 4, 4, 4)

[ 288](siwx91x-pinctrl_8h.md#a129dc73d20f20394c4c30fbecd755cf5)#define SCT\_IN1\_HP26 SIWX91X\_GPIO(9, 0xFF, 0, 1, 10, 0)

[ 289](siwx91x-pinctrl_8h.md#a0795a0474012f940b032bf0c93a54283)#define SCT\_IN1\_ULP1 SIWX91X\_GPIO(7, 6, 23, 4, 1, 1)

[ 290](siwx91x-pinctrl_8h.md#aa543bccd5eaa129a2e71626bfb5a9e0e)#define SCT\_IN1\_ULP5 SIWX91X\_GPIO(9, 6, 27, 4, 5, 5)

[ 291](siwx91x-pinctrl_8h.md#ac120a628c9b6f2f55b99ab810e6575fb)#define SCT\_IN2\_HP27 SIWX91X\_GPIO(9, 0xFF, 0, 1, 11, 0)

[ 292](siwx91x-pinctrl_8h.md#a2d6b23ffe6db55ca5e76118dea7a14ea)#define SCT\_IN2\_ULP2 SIWX91X\_GPIO(7, 6, 24, 4, 2, 2)

[ 293](siwx91x-pinctrl_8h.md#aa9e34755ee740ce485048bc6edae12b1)#define SCT\_IN2\_ULP6 SIWX91X\_GPIO(9, 6, 28, 4, 6, 6)

[ 294](siwx91x-pinctrl_8h.md#a62b8aa7dd85b312896c126bc09daf4f0)#define SCT\_IN3\_HP28 SIWX91X\_GPIO(9, 0xFF, 0, 1, 12, 0)

[ 295](siwx91x-pinctrl_8h.md#a20d138a68cefaf8a5785def1553adf10)#define SCT\_IN3\_ULP3 SIWX91X\_GPIO(7, 6, 25, 4, 3, 3)

[ 296](siwx91x-pinctrl_8h.md#a9f850c61dbeb18c64e8d133cc37aee77)#define SCT\_IN3\_ULP7 SIWX91X\_GPIO(9, 6, 29, 4, 7, 7)

[ 297](siwx91x-pinctrl_8h.md#a487a88c8ad8a9c5cfa33639ea27ac5d2)#define SCT\_OUT0\_HP29 SIWX91X\_GPIO(9, 0xFF, 0, 1, 13, 0)

[ 298](siwx91x-pinctrl_8h.md#a31a6744e2a07d61f7aff3a64d29c6345)#define SCT\_OUT0\_ULP4 SIWX91X\_GPIO(7, 6, 26, 4, 4, 4)

[ 299](siwx91x-pinctrl_8h.md#a8d5e593bab255708bb5a34549dbc39ff)#define SCT\_OUT1\_HP30 SIWX91X\_GPIO(9, 0xFF, 0, 1, 14, 0)

[ 300](siwx91x-pinctrl_8h.md#aeee61408d7a9d0fb3ec2b099bf6b4925)#define SCT\_OUT1\_ULP5 SIWX91X\_GPIO(7, 6, 27, 4, 5, 5)

[ 301](siwx91x-pinctrl_8h.md#a896f7133bc09d5776b8fce43a919a582)#define SCT\_OUT2\_HP8 SIWX91X\_GPIO(12, 0xFF, 3, 0, 8, 0)

[ 302](siwx91x-pinctrl_8h.md#aceb19f98ff9d765be5ac4163c400b30f)#define SCT\_OUT2\_ULP6 SIWX91X\_GPIO(7, 6, 28, 4, 6, 6)

[ 303](siwx91x-pinctrl_8h.md#a23b5eb6cd7cb43df14db4f42a05d8b70)#define SCT\_OUT3\_HP9 SIWX91X\_GPIO(12, 0xFF, 4, 0, 9, 0)

[ 304](siwx91x-pinctrl_8h.md#a3d240479009ee2c1660006406a51e14b)#define SCT\_OUT3\_ULP7 SIWX91X\_GPIO(7, 6, 29, 4, 7, 7)

[ 305](siwx91x-pinctrl_8h.md#aa1ce9c940b0f1b1f85e8c0aa765afe58)#define SCT\_OUT4\_ULP4 SIWX91X\_GPIO(13, 6, 26, 4, 4, 4)

[ 306](siwx91x-pinctrl_8h.md#a56f04a2fdf3d596c09989bb7f2f4d711)#define SCT\_OUT4\_ULP8 SIWX91X\_GPIO(7, 6, 30, 4, 8, 8)

[ 307](siwx91x-pinctrl_8h.md#abddc79f260ecc7fb85878f5182f0b4b2)#define SCT\_OUT5\_ULP5 SIWX91X\_GPIO(13, 6, 27, 4, 5, 5)

[ 308](siwx91x-pinctrl_8h.md#a14ad4c709bf766e5568ec2214c29935d)#define SCT\_OUT5\_ULP9 SIWX91X\_GPIO(7, 6, 31, 4, 9, 9)

[ 309](siwx91x-pinctrl_8h.md#ab3ecf512e8c70db0f9a7a374d5c4ee61)#define SCT\_OUT6\_ULP6 SIWX91X\_GPIO(13, 6, 28, 4, 6, 6)

[ 310](siwx91x-pinctrl_8h.md#a9833d3691184034534dac5542141979c)#define SCT\_OUT6\_ULP10 SIWX91X\_GPIO(7, 6, 32, 4, 10, 10)

[ 311](siwx91x-pinctrl_8h.md#a58d91744df7f674a8d639efee6ada664)#define SCT\_OUT7\_ULP7 SIWX91X\_GPIO(13, 6, 29, 4, 7, 7)

[ 312](siwx91x-pinctrl_8h.md#a72096ef61c9b342223b90a4a2a2cad67)#define SCT\_OUT7\_ULP11 SIWX91X\_GPIO(7, 6, 33, 4, 11, 11)

313

[ 314](siwx91x-pinctrl_8h.md#a0832163dccdf4899e70bc54e1c1d76b9)#define SIO\_0\_HP6 SIWX91X\_GPIO(1, 0xFF, 1, 0, 6, 0)

[ 315](siwx91x-pinctrl_8h.md#a50c459097b961e8f0b8ebb4b0022ff24)#define SIO\_0\_HP25 SIWX91X\_GPIO(1, 0xFF, 0, 1, 9, 0)

[ 316](siwx91x-pinctrl_8h.md#ac962669966622a760066ae1d644cf16e)#define SIO\_0\_ULP0 SIWX91X\_GPIO(1, 6, 22, 4, 0, 0)

[ 317](siwx91x-pinctrl_8h.md#a9e2fbc5435e49df883f1cf0394ca5720)#define SIO\_0\_ULP8 SIWX91X\_GPIO(1, 6, 30, 4, 8, 8)

[ 318](siwx91x-pinctrl_8h.md#aeb287420b59b4085df40b2bc8c4a9bb8)#define SIO\_1\_HP7 SIWX91X\_GPIO(1, 0xFF, 2, 0, 7, 0)

[ 319](siwx91x-pinctrl_8h.md#ab1bffb41dcfd954d4110cdb091b5f1dd)#define SIO\_1\_HP26 SIWX91X\_GPIO(1, 0xFF, 0, 1, 10, 0)

[ 320](siwx91x-pinctrl_8h.md#ac6a3e01783137270cf5fa27b02c62c5c)#define SIO\_1\_ULP1 SIWX91X\_GPIO(1, 6, 23, 4, 1, 1)

[ 321](siwx91x-pinctrl_8h.md#ac75318d95fac4ae093072ed1f73e18c0)#define SIO\_1\_ULP9 SIWX91X\_GPIO(1, 6, 31, 4, 9, 9)

[ 322](siwx91x-pinctrl_8h.md#a09ae893ea29f226c66d823ea6d8e9dea)#define SIO\_2\_HP8 SIWX91X\_GPIO(1, 0xFF, 3, 0, 8, 0)

[ 323](siwx91x-pinctrl_8h.md#a89795f8bd3ae258fa3c0f1daf2521d55)#define SIO\_2\_HP27 SIWX91X\_GPIO(1, 0xFF, 0, 1, 11, 0)

[ 324](siwx91x-pinctrl_8h.md#accd43e63baf2ece7c3105e7b1179281f)#define SIO\_2\_ULP2 SIWX91X\_GPIO(1, 6, 24, 4, 2, 2)

[ 325](siwx91x-pinctrl_8h.md#ab203641292581774bcf3ea40e5c6f465)#define SIO\_2\_ULP10 SIWX91X\_GPIO(1, 6, 32, 4, 10, 10)

[ 326](siwx91x-pinctrl_8h.md#a3ee11e86b6d00fb603f8389a69ace17f)#define SIO\_3\_HP9 SIWX91X\_GPIO(1, 0xFF, 4, 0, 9, 0)

[ 327](siwx91x-pinctrl_8h.md#af40550b595f5f30ac0a6ae2335e6ec55)#define SIO\_3\_HP28 SIWX91X\_GPIO(1, 0xFF, 0, 1, 12, 0)

[ 328](siwx91x-pinctrl_8h.md#ae271fa5750acca3534ea22178fea6fc5)#define SIO\_3\_ULP3 SIWX91X\_GPIO(1, 6, 25, 4, 3, 3)

[ 329](siwx91x-pinctrl_8h.md#acafbbec57e7c4b952398106cb9a03ef7)#define SIO\_3\_ULP11 SIWX91X\_GPIO(1, 6, 33, 4, 11, 11)

[ 330](siwx91x-pinctrl_8h.md#acbe0ac06f6094ddc13e5ff98ecf9345d)#define SIO\_4\_HP10 SIWX91X\_GPIO(1, 0xFF, 5, 0, 10, 0)

[ 331](siwx91x-pinctrl_8h.md#a2abfaa99057e594bdd1b3ed640744114)#define SIO\_4\_HP29 SIWX91X\_GPIO(1, 0xFF, 0, 1, 13, 0)

[ 332](siwx91x-pinctrl_8h.md#ac0274ba6c1129339f49f087e9b503759)#define SIO\_4\_ULP4 SIWX91X\_GPIO(1, 6, 26, 4, 4, 4)

[ 333](siwx91x-pinctrl_8h.md#a6da8512e01689d6eff690f5ad538bc01)#define SIO\_5\_HP11 SIWX91X\_GPIO(1, 0xFF, 6, 0, 11, 0)

[ 334](siwx91x-pinctrl_8h.md#a81766e7a7df2e5f915517f2065750c7a)#define SIO\_5\_HP30 SIWX91X\_GPIO(1, 0xFF, 0, 1, 14, 0)

[ 335](siwx91x-pinctrl_8h.md#a07a673ae96d7332b5799d7e779180cc9)#define SIO\_5\_ULP5 SIWX91X\_GPIO(1, 6, 27, 4, 5, 5)

[ 336](siwx91x-pinctrl_8h.md#ab6d4f24470587604725bb9612d988b34)#define SIO\_6\_ULP6 SIWX91X\_GPIO(1, 6, 28, 4, 6, 6)

[ 337](siwx91x-pinctrl_8h.md#aa6a42c96535dd6934fa0bc4886ea00b7)#define SIO\_7\_HP15 SIWX91X\_GPIO(1, 0xFF, 8, 0, 15, 0)

[ 338](siwx91x-pinctrl_8h.md#a52635e4cce4a478134455ea5ee43c962)#define SIO\_7\_ULP7 SIWX91X\_GPIO(1, 6, 29, 4, 7, 7)

339

[ 340](siwx91x-pinctrl_8h.md#a0d8209a8fb54f5ef19bb86981b383c43)#define SSI\_CLK\_HP8 SIWX91X\_GPIO(3, 0xFF, 3, 0, 8, 0)

[ 341](siwx91x-pinctrl_8h.md#a77b8278e81edee91c96c990c2479144f)#define SSI\_CLK\_HP25 SIWX91X\_GPIO(3, 0xFF, 0, 1, 9, 0)

[ 342](siwx91x-pinctrl_8h.md#a166065c88ad7a8bf66d6ca7b51628a2f)#define SSI\_CLK\_HP52 SIWX91X\_GPIO(3, 0xFF, 16, 3, 4, 0)

[ 343](siwx91x-pinctrl_8h.md#ac29bdcb9b8693277b6b6e8950576b4d7)#define SSI\_CS0\_HP9 SIWX91X\_GPIO(3, 0xFF, 4, 0, 9, 0)

[ 344](siwx91x-pinctrl_8h.md#aa070abef007fb1355d3a151038c4b282)#define SSI\_CS0\_HP28 SIWX91X\_GPIO(3, 0xFF, 0, 1, 12, 0)

[ 345](siwx91x-pinctrl_8h.md#a9e28d21c0d469b33398b0c24936478bc)#define SSI\_CS0\_HP53 SIWX91X\_GPIO(3, 0xFF, 17, 3, 5, 0)

[ 346](siwx91x-pinctrl_8h.md#a2858feb71f44abd3b8e0a49d00fd5a03)#define SSI\_CS1\_HP10 SIWX91X\_GPIO(3, 0xFF, 5, 0, 10, 0)

[ 347](siwx91x-pinctrl_8h.md#a7b0f6b3e42fb8329ed491b5561aef908)#define SSI\_CS2\_HP15 SIWX91X\_GPIO(3, 0xFF, 8, 0, 15, 0)

[ 348](siwx91x-pinctrl_8h.md#a0c54f4dc5efdcc32a32dc79449f58ea1)#define SSI\_CS2\_HP50 SIWX91X\_GPIO(3, 0xFF, 14, 3, 2, 0)

[ 349](siwx91x-pinctrl_8h.md#aafdfc33c0bbe11b258479379ed42d486)#define SSI\_CS3\_HP51 SIWX91X\_GPIO(3, 0xFF, 15, 3, 3, 0)

[ 350](siwx91x-pinctrl_8h.md#ab65665cb7ad83803229e49b068615593)#define SSI\_DATA0\_HP11 SIWX91X\_GPIO(3, 0xFF, 6, 0, 11, 0)

[ 351](siwx91x-pinctrl_8h.md#a636c99a6026a8463ebd53ac63a270956)#define SSI\_DATA0\_HP26 SIWX91X\_GPIO(3, 0xFF, 0, 1, 10, 0)

[ 352](siwx91x-pinctrl_8h.md#ac204f25409e010a300cdbe48c6ad255b)#define SSI\_DATA0\_HP56 SIWX91X\_GPIO(3, 0xFF, 20, 3, 8, 0)

[ 353](siwx91x-pinctrl_8h.md#a3481b7ccfebdb2e679127a99b9410443)#define SSI\_DATA1\_HP10 SIWX91X\_GPIO(12, 0xFF, 5, 0, 10, 0)

[ 354](siwx91x-pinctrl_8h.md#a3ca3fd4c997fc966808b637bd5ce9cf5)#define SSI\_DATA1\_HP12 SIWX91X\_GPIO(3, 0xFF, 7, 0, 12, 0)

[ 355](siwx91x-pinctrl_8h.md#a755e7244b7708e5863da85b21891f0f6)#define SSI\_DATA1\_HP27 SIWX91X\_GPIO(3, 0xFF, 0, 1, 11, 0)

[ 356](siwx91x-pinctrl_8h.md#ace422b65e5eda30314e575c25633ff83)#define SSI\_DATA1\_HP57 SIWX91X\_GPIO(3, 0xFF, 21, 3, 9, 0)

[ 357](siwx91x-pinctrl_8h.md#a91b07b14b58117fe2cd6627a7a9831f8)#define SSI\_DATA2\_HP6 SIWX91X\_GPIO(3, 0xFF, 1, 0, 6, 0)

[ 358](siwx91x-pinctrl_8h.md#aed349cea226d2b4577aafb3f916cf921)#define SSI\_DATA2\_HP29 SIWX91X\_GPIO(3, 0xFF, 0, 1, 13, 0)

[ 359](siwx91x-pinctrl_8h.md#a46431de74f13595e9f143032b1e7816e)#define SSI\_DATA2\_HP54 SIWX91X\_GPIO(3, 0xFF, 18, 3, 6, 0)

[ 360](siwx91x-pinctrl_8h.md#ae03aa3be0edb0c5dcd4fbbb3c7d48038)#define SSI\_DATA3\_HP7 SIWX91X\_GPIO(3, 0xFF, 2, 0, 7, 0)

[ 361](siwx91x-pinctrl_8h.md#a5e711f668e3bf36c0068868019d91dfd)#define SSI\_DATA3\_HP30 SIWX91X\_GPIO(3, 0xFF, 0, 1, 14, 0)

[ 362](siwx91x-pinctrl_8h.md#a6a3f96e3b7129d2d1625da6ef7be0e52)#define SSI\_DATA3\_HP55 SIWX91X\_GPIO(3, 0xFF, 19, 3, 7, 0)

363

[ 364](siwx91x-pinctrl_8h.md#ad2741d1cf1901f68ab2825a2cade5712)#define SSIS\_CLK\_HP8 SIWX91X\_GPIO(8, 0xFF, 3, 0, 8, 0)

[ 365](siwx91x-pinctrl_8h.md#a246b34d2a347e66749a95f2865f40060)#define SSIS\_CLK\_HP26 SIWX91X\_GPIO(8, 0xFF, 0, 1, 10, 0)

[ 366](siwx91x-pinctrl_8h.md#a50d2c8019a3e7b2c7b2d9c62c092c239)#define SSIS\_CLK\_HP47 SIWX91X\_GPIO(8, 0xFF, 11, 2, 15, 0)

[ 367](siwx91x-pinctrl_8h.md#a8aaf5a65d4af6ad97b74eb4d280aa808)#define SSIS\_CLK\_HP52 SIWX91X\_GPIO(8, 0xFF, 16, 3, 4, 0)

[ 368](siwx91x-pinctrl_8h.md#a558f00dabc8270c6e3464311055c927c)#define SSIS\_CS\_HP9 SIWX91X\_GPIO(8, 0xFF, 4, 0, 9, 0)

[ 369](siwx91x-pinctrl_8h.md#a0ccfb2d0b256ae264aa2fab362240537)#define SSIS\_CS\_HP25 SIWX91X\_GPIO(8, 0xFF, 0, 1, 9, 0)

[ 370](siwx91x-pinctrl_8h.md#a33ddacd923544e99d56f12b00d3a58c4)#define SSIS\_CS\_HP46 SIWX91X\_GPIO(8, 0xFF, 10, 2, 14, 0)

[ 371](siwx91x-pinctrl_8h.md#af37723fe1fb0edfd1cef5334fa2286e0)#define SSIS\_CS\_HP53 SIWX91X\_GPIO(8, 0xFF, 17, 3, 5, 0)

[ 372](siwx91x-pinctrl_8h.md#af11a72c74fc5de2890ff29882a549c7d)#define SSIS\_MISO\_HP11 SIWX91X\_GPIO(8, 0xFF, 6, 0, 11, 0)

[ 373](siwx91x-pinctrl_8h.md#ac29849ee9448a7da3dc0dfd9584fe8e6)#define SSIS\_MISO\_HP28 SIWX91X\_GPIO(8, 0xFF, 0, 1, 12, 0)

[ 374](siwx91x-pinctrl_8h.md#af26a275bd867021c3c2fe617b2f90d56)#define SSIS\_MISO\_HP49 SIWX91X\_GPIO(8, 0xFF, 13, 3, 1, 0)

[ 375](siwx91x-pinctrl_8h.md#a303a10aa5fac51931f1fd2625476c250)#define SSIS\_MISO\_HP57 SIWX91X\_GPIO(8, 0xFF, 21, 3, 9, 0)

[ 376](siwx91x-pinctrl_8h.md#a09804ebbc7f861922372cca189f539c1)#define SSIS\_MOSI\_HP10 SIWX91X\_GPIO(8, 0xFF, 5, 0, 10, 0)

[ 377](siwx91x-pinctrl_8h.md#a0217b56cf5d51ef66de6aba1d2a7e75e)#define SSIS\_MOSI\_HP27 SIWX91X\_GPIO(8, 0xFF, 0, 1, 11, 0)

[ 378](siwx91x-pinctrl_8h.md#a4227e1213145f52cf732f237256f9606)#define SSIS\_MOSI\_HP48 SIWX91X\_GPIO(8, 0xFF, 12, 3, 0, 0)

[ 379](siwx91x-pinctrl_8h.md#acc3c25b45390c7e676d06717dc468251)#define SSIS\_MOSI\_HP56 SIWX91X\_GPIO(8, 0xFF, 20, 3, 8, 0)

380

[ 381](siwx91x-pinctrl_8h.md#a239d90024707952ed74238c3fc97608e)#define TIMER0\_HP7 SIWX91X\_GPIO(9, 5, 2, 0, 7, 1)

[ 382](siwx91x-pinctrl_8h.md#a49ae74d218db2a1132075c68c4574099)#define TIMER0\_HP27 SIWX91X\_GPIO(11, 5, 0, 1, 11, 8)

[ 383](siwx91x-pinctrl_8h.md#aa8a483b521b450670203463f7d8be032)#define TIMER0\_HP46 SIWX91X\_GPIO(9, 5, 10, 2, 14, 8)

[ 384](siwx91x-pinctrl_8h.md#a8043999b57da3920d59a3c61e68a26ae)#define TIMER0\_ULP4 SIWX91X\_GPIO(0xFF, 9, 0xFF, 4, 0, 4)

[ 385](siwx91x-pinctrl_8h.md#a412766982e02327695695d09968e4ee0)#define TIMER0\_ULP8 SIWX91X\_GPIO(0xFF, 5, 0xFF, 4, 0, 8)

386

[ 387](siwx91x-pinctrl_8h.md#a02a30a238516586b3e9f9d168edb855c)#define TIMER1\_HP15 SIWX91X\_GPIO(9, 5, 8, 0, 15, 7)

[ 388](siwx91x-pinctrl_8h.md#a99e02ee3b901fc1ee4d9ea1021f9c746)#define TIMER1\_HP26 SIWX91X\_GPIO(11, 5, 0, 1, 10, 7)

[ 389](siwx91x-pinctrl_8h.md#a99832252de48cc89d11c3e522ea44376)#define TIMER1\_ULP5 SIWX91X\_GPIO(0xFF, 9, 0xFF, 4, 0, 5)

[ 390](siwx91x-pinctrl_8h.md#aa1fb1deae2ad43558df04b772029957f)#define TIMER1\_ULP7 SIWX91X\_GPIO(0xFF, 5, 0xFF, 4, 0, 7)

391

[ 392](siwx91x-pinctrl_8h.md#aa778464dc8449625d49328f30c76e92e)#define TIMER2\_ULP1 SIWX91X\_GPIO(0xFF, 5, 0xFF, 4, 0, 1)

393

[ 394](siwx91x-pinctrl_8h.md#ad5d637f7c1e783f5bdd0f72d90a986cd)#define TRACE\_CLK\_HP7 SIWX91X\_GPIO(13, 0xFF, 2, 0, 7, 0)

[ 395](siwx91x-pinctrl_8h.md#aa4fe9698b15438987cee0d3c0d4ed193)#define TRACE\_CLK\_HP47 SIWX91X\_GPIO(6, 0xFF, 11, 2, 15, 0)

[ 396](siwx91x-pinctrl_8h.md#a9934d0e8efc26562ca6b28b3f5ece6e4)#define TRACE\_CLK\_HP53 SIWX91X\_GPIO(6, 0xFF, 17, 3, 5, 0)

[ 397](siwx91x-pinctrl_8h.md#ad942d16221a23fae94615aeda7acb650)#define TRACE\_CLKIN\_HP6 SIWX91X\_GPIO(13, 0xFF, 1, 0, 6, 0)

[ 398](siwx91x-pinctrl_8h.md#ab332137012b6fb95cf5d5eac07950296)#define TRACE\_CLKIN\_HP15 SIWX91X\_GPIO(6, 0xFF, 8, 0, 15, 0)

[ 399](siwx91x-pinctrl_8h.md#ae1259534ea8316ebe29436705e258f69)#define TRACE\_CLKIN\_HP46 SIWX91X\_GPIO(6, 0xFF, 10, 2, 14, 0)

[ 400](siwx91x-pinctrl_8h.md#a93a66a67b4b079b2d6ab0f64bccb5b7f)#define TRACE\_CLKIN\_HP52 SIWX91X\_GPIO(6, 0xFF, 16, 3, 4, 0)

[ 401](siwx91x-pinctrl_8h.md#a329ce75fc9014134a8684d7e384bb569)#define TRACE\_D0\_HP8 SIWX91X\_GPIO(13, 0xFF, 3, 0, 8, 0)

[ 402](siwx91x-pinctrl_8h.md#a25196d0c4d77efa6d1340aade4a7ab43)#define TRACE\_D0\_HP48 SIWX91X\_GPIO(6, 0xFF, 12, 3, 0, 0)

[ 403](siwx91x-pinctrl_8h.md#afa79f060e825009dcbf30c194cfd259a)#define TRACE\_D0\_HP54 SIWX91X\_GPIO(6, 0xFF, 18, 3, 6, 0)

[ 404](siwx91x-pinctrl_8h.md#a6ac2fd081f541973db09767923e5c994)#define TRACE\_D1\_HP9 SIWX91X\_GPIO(13, 0xFF, 4, 0, 9, 0)

[ 405](siwx91x-pinctrl_8h.md#ac26e1b82bb464c5e2d1d4ed606b83f4c)#define TRACE\_D1\_HP49 SIWX91X\_GPIO(6, 0xFF, 13, 3, 1, 0)

[ 406](siwx91x-pinctrl_8h.md#ab019d73a28e7fd218c301a7a16a8744c)#define TRACE\_D1\_HP55 SIWX91X\_GPIO(6, 0xFF, 19, 3, 7, 0)

[ 407](siwx91x-pinctrl_8h.md#a8b1bae5956611a7a7ea0b9479236eba8)#define TRACE\_D2\_HP10 SIWX91X\_GPIO(13, 0xFF, 5, 0, 10, 0)

[ 408](siwx91x-pinctrl_8h.md#aabaa120c9882567d5fcb51adf4bee1d6)#define TRACE\_D2\_HP50 SIWX91X\_GPIO(6, 0xFF, 14, 3, 2, 0)

[ 409](siwx91x-pinctrl_8h.md#af2e5c3c47489489a5bb89767683f0426)#define TRACE\_D2\_HP56 SIWX91X\_GPIO(6, 0xFF, 20, 3, 8, 0)

[ 410](siwx91x-pinctrl_8h.md#ae6e493f9ab1a119b3b0d51ae46a09abb)#define TRACE\_D3\_HP11 SIWX91X\_GPIO(13, 0xFF, 6, 0, 11, 0)

[ 411](siwx91x-pinctrl_8h.md#a72ec3566d71b12eeaaa00e196f0d04b2)#define TRACE\_D3\_HP51 SIWX91X\_GPIO(6, 0xFF, 15, 3, 3, 0)

[ 412](siwx91x-pinctrl_8h.md#a74a11c7d6068e66986c6410f63a87a12)#define TRACE\_D3\_HP57 SIWX91X\_GPIO(6, 0xFF, 21, 3, 9, 0)

413

[ 414](siwx91x-pinctrl_8h.md#a1514c950553999c21e0d43c2d6aefddf)#define UART0\_CLK\_HP8 SIWX91X\_GPIO(2, 0xFF, 3, 0, 8, 0)

[ 415](siwx91x-pinctrl_8h.md#a702cef077f6ec6ba684e0cccff48e2ee)#define UART0\_CLK\_HP25 SIWX91X\_GPIO(2, 0xFF, 0, 1, 9, 0)

[ 416](siwx91x-pinctrl_8h.md#a8d19011b7dfb8ecca987d95084f1ef43)#define UART0\_CLK\_HP52 SIWX91X\_GPIO(2, 0xFF, 16, 3, 4, 0)

[ 417](siwx91x-pinctrl_8h.md#a2df47af0f0a9b175663bfce524da6187)#define UART0\_CLK\_ULP0 SIWX91X\_GPIO(2, 6, 22, 4, 0, 0)

[ 418](siwx91x-pinctrl_8h.md#a873d1ee0fbe9c691bba5c72eb88989b6)#define UART0\_CTS\_HP6 SIWX91X\_GPIO(2, 0xFF, 1, 0, 6, 0)

[ 419](siwx91x-pinctrl_8h.md#a16193dab96a8006cf2766c5cb152a32c)#define UART0\_CTS\_HP26 SIWX91X\_GPIO(2, 0xFF, 0, 1, 10, 0)

[ 420](siwx91x-pinctrl_8h.md#ae56529f660d670b4b8d21417a6e09de2)#define UART0\_CTS\_HP56 SIWX91X\_GPIO(2, 0xFF, 20, 3, 8, 0)

[ 421](siwx91x-pinctrl_8h.md#a274238cb4dd58655ac8571d803e6bbb8)#define UART0\_CTS\_ULP6 SIWX91X\_GPIO(2, 6, 28, 4, 6, 6)

[ 422](siwx91x-pinctrl_8h.md#aafcfe3007f6c11254e06dd61c92b3f4e)#define UART0\_DCD\_HP12 SIWX91X\_GPIO(2, 0xFF, 7, 0, 12, 0)

[ 423](siwx91x-pinctrl_8h.md#a5b8c6daf4798492ddd1bd1f36fc2ad70)#define UART0\_DCD\_HP29 SIWX91X\_GPIO(12, 0xFF, 0, 1, 13, 0)

[ 424](siwx91x-pinctrl_8h.md#a09324d646d1b31f3ef1064dec42cd87b)#define UART0\_DSR\_HP11 SIWX91X\_GPIO(2, 0xFF, 6, 0, 11, 0)

[ 425](siwx91x-pinctrl_8h.md#ae156c04dd623cd446e9b0e2e233638f3)#define UART0\_DSR\_HP57 SIWX91X\_GPIO(2, 0xFF, 21, 3, 9, 0)

[ 426](siwx91x-pinctrl_8h.md#a3593158afb8848932439923fddb5c0ac)#define UART0\_DTR\_HP7 SIWX91X\_GPIO(2, 0xFF, 2, 0, 7, 0)

[ 427](siwx91x-pinctrl_8h.md#a19dead7b9533bed8693a6f730ad5fd91)#define UART0\_IRRX\_HP25 SIWX91X\_GPIO(13, 0xFF, 0, 1, 9, 0)

[ 428](siwx91x-pinctrl_8h.md#a9c2a4489ec8c0f9244485b4db066ca3f)#define UART0\_IRRX\_HP47 SIWX91X\_GPIO(2, 0xFF, 11, 2, 15, 0)

[ 429](siwx91x-pinctrl_8h.md#adf611f1df2303d5155e071ccc56d8c30)#define UART0\_IRRX\_ULP0 SIWX91X\_GPIO(11, 6, 22, 4, 0, 0)

[ 430](siwx91x-pinctrl_8h.md#a659bdb287f75f00c7c644ae554983860)#define UART0\_IRRX\_ULP7 SIWX91X\_GPIO(2, 6, 29, 4, 7, 7)

[ 431](siwx91x-pinctrl_8h.md#a96681675723bed89eef7ed2ff68324b2)#define UART0\_IRTX\_HP26 SIWX91X\_GPIO(13, 0xFF, 0, 1, 10, 0)

[ 432](siwx91x-pinctrl_8h.md#a5ada8867e27615e304abb89e8ed95b4a)#define UART0\_IRTX\_HP48 SIWX91X\_GPIO(2, 0xFF, 12, 3, 0, 0)

[ 433](siwx91x-pinctrl_8h.md#ab9422f6b18b7d95f257eea54708c0da6)#define UART0\_IRTX\_ULP1 SIWX91X\_GPIO(11, 6, 23, 4, 1, 1)

[ 434](siwx91x-pinctrl_8h.md#adbcb3a2ebb68225e265ac83d77755540)#define UART0\_IRTX\_ULP8 SIWX91X\_GPIO(2, 6, 30, 4, 8, 8)

[ 435](siwx91x-pinctrl_8h.md#ae5f8f182da81b3b8dd85c32be0219439)#define UART0\_RI\_HP27 SIWX91X\_GPIO(2, 0xFF, 0, 1, 11, 0)

[ 436](siwx91x-pinctrl_8h.md#a3938be42c21041a362aaec421751d9aa)#define UART0\_RI\_HP46 SIWX91X\_GPIO(2, 0xFF, 10, 2, 14, 0)

[ 437](siwx91x-pinctrl_8h.md#a64d2529c38303a82f24b01ed5ad05be0)#define UART0\_RI\_ULP4 SIWX91X\_GPIO(11, 6, 26, 4, 4, 4)

[ 438](siwx91x-pinctrl_8h.md#af607a3b3e6374ce5bd6311b657eed71e)#define UART0\_RS485DE\_HP29 SIWX91X\_GPIO(13, 0xFF, 0, 1, 13, 0)

[ 439](siwx91x-pinctrl_8h.md#a50b16324373e3e32370d570491a4f535)#define UART0\_RS485DE\_HP51 SIWX91X\_GPIO(2, 0xFF, 15, 3, 3, 0)

[ 440](siwx91x-pinctrl_8h.md#a02a8e7b5adfc32af7af4e5ba088ce0f7)#define UART0\_RS485DE\_ULP7 SIWX91X\_GPIO(11, 6, 29, 4, 7, 7)

[ 441](siwx91x-pinctrl_8h.md#a041682ac7bc0eaad6ef3b4e2e3ef3fc3)#define UART0\_RS485DE\_ULP11 SIWX91X\_GPIO(2, 6, 33, 4, 11, 11)

[ 442](siwx91x-pinctrl_8h.md#a777e97d29443a4a43d92c39ba2d6480b)#define UART0\_RS485EN\_HP27 SIWX91X\_GPIO(13, 0xFF, 0, 1, 11, 0)

[ 443](siwx91x-pinctrl_8h.md#aa5a0741a5fcb9e89f16dd286e4e4d1d1)#define UART0\_RS485EN\_HP49 SIWX91X\_GPIO(2, 0xFF, 13, 3, 1, 0)

[ 444](siwx91x-pinctrl_8h.md#a91f4ac4b0941ef7177ee9b4896d3ab51)#define UART0\_RS485EN\_ULP5 SIWX91X\_GPIO(11, 6, 27, 4, 5, 5)

[ 445](siwx91x-pinctrl_8h.md#a398e1bdbebdfae8177daa590b7a026ca)#define UART0\_RS485EN\_ULP9 SIWX91X\_GPIO(2, 6, 31, 4, 9, 9)

[ 446](siwx91x-pinctrl_8h.md#a3f359f67b459ed81e8db5fd786e7089a)#define UART0\_RS485RE\_HP28 SIWX91X\_GPIO(13, 0xFF, 0, 1, 12, 0)

[ 447](siwx91x-pinctrl_8h.md#a19efcf4ac776bbb3156508a1b580e2f3)#define UART0\_RS485RE\_HP50 SIWX91X\_GPIO(2, 0xFF, 14, 3, 2, 0)

[ 448](siwx91x-pinctrl_8h.md#a0704cd391bbb230d5a359ec1f8dfcb5c)#define UART0\_RS485RE\_ULP6 SIWX91X\_GPIO(11, 6, 28, 4, 6, 6)

[ 449](siwx91x-pinctrl_8h.md#a806d9ce45c9bdac84f82da94b2e61623)#define UART0\_RS485RE\_ULP10 SIWX91X\_GPIO(2, 6, 32, 4, 10, 10)

[ 450](siwx91x-pinctrl_8h.md#a5b04f93bc8455f7943a7dc71414f6fdd)#define UART0\_RTS\_HP9 SIWX91X\_GPIO(2, 0xFF, 4, 0, 9, 0)

[ 451](siwx91x-pinctrl_8h.md#af6180ba7e3498e1cb075cf84d08ac0c5)#define UART0\_RTS\_HP28 SIWX91X\_GPIO(2, 0xFF, 0, 1, 12, 0)

[ 452](siwx91x-pinctrl_8h.md#a0b18d3117184a53274c9455a1d2ba7d6)#define UART0\_RTS\_HP53 SIWX91X\_GPIO(2, 0xFF, 17, 3, 5, 0)

[ 453](siwx91x-pinctrl_8h.md#acdeb030914a38257f40ba31622a8e44f)#define UART0\_RTS\_ULP5 SIWX91X\_GPIO(2, 6, 27, 4, 5, 5)

[ 454](siwx91x-pinctrl_8h.md#aa12f9238e599d54cde0246c41ee7f216)#define UART0\_RX\_HP10 SIWX91X\_GPIO(2, 0xFF, 5, 0, 10, 0)

[ 455](siwx91x-pinctrl_8h.md#a5f034df81ac363d212da25a510fd8869)#define UART0\_RX\_HP29 SIWX91X\_GPIO(2, 0xFF, 0, 1, 13, 0)

[ 456](siwx91x-pinctrl_8h.md#a7c3b4144654fe9a24db90b57998e4cb4)#define UART0\_RX\_HP55 SIWX91X\_GPIO(2, 0xFF, 19, 3, 7, 0)

[ 457](siwx91x-pinctrl_8h.md#ae6d9c15cfc89ceb5d8ad3d2b5a7756c7)#define UART0\_RX\_ULP1 SIWX91X\_GPIO(2, 6, 23, 4, 1, 1)

[ 458](siwx91x-pinctrl_8h.md#a27cb5f1b5a7d5798fb219c3a6659acb6)#define UART0\_RX\_ULP6 SIWX91X\_GPIO(4, 6, 28, 4, 6, 6)

[ 459](siwx91x-pinctrl_8h.md#a310df59fe4dc6cf528b1bafe00c41c7a)#define UART0\_TX\_HP30 SIWX91X\_GPIO(2, 0xFF, 0, 1, 14, 0)

[ 460](siwx91x-pinctrl_8h.md#a913663cca98288505e45479c213ea0d0)#define UART0\_TX\_HP54 SIWX91X\_GPIO(2, 0xFF, 18, 3, 6, 0)

[ 461](siwx91x-pinctrl_8h.md#a4d763a3c1a9bf10f42187482c5a2ba34)#define UART0\_TX\_ULP4 SIWX91X\_GPIO(2, 6, 26, 4, 4, 4)

[ 462](siwx91x-pinctrl_8h.md#a8fd486e3b0c02b1f578a38e1d6c30a38)#define UART0\_TX\_ULP7 SIWX91X\_GPIO(4, 6, 29, 4, 7, 7)

463

[ 464](siwx91x-pinctrl_8h.md#a4ca4f60081c355860a6a10bfa428bc98)#define UART1\_CTS\_HP11 SIWX91X\_GPIO(6, 0xFF, 6, 0, 11, 0)

[ 465](siwx91x-pinctrl_8h.md#a1782fbe55aa8e6f8bd75da573c755223)#define UART1\_CTS\_HP32 SIWX91X\_GPIO(12, 0xFF, 9, 2, 0, 0)

[ 466](siwx91x-pinctrl_8h.md#a66ca158c30cc3087b3ae12824e86398f)#define UART1\_CTS\_HP51 SIWX91X\_GPIO(9, 0xFF, 15, 3, 3, 0)

[ 467](siwx91x-pinctrl_8h.md#aa8245d65007636996d67ca46d5c5a9fd)#define UART1\_CTS\_ULP1 SIWX91X\_GPIO(9, 6, 23, 4, 1, 1)

[ 468](siwx91x-pinctrl_8h.md#a281ee7fbfe1a8ee2814d0f6ba60e61f6)#define UART1\_CTS\_ULP7 SIWX91X\_GPIO(6, 6, 29, 4, 7, 7)

[ 469](siwx91x-pinctrl_8h.md#a7ddce4735336b046b99dcee26d4f90c3)#define UART1\_CTS\_ULP9 SIWX91X\_GPIO(9, 6, 31, 4, 9, 9)

[ 470](siwx91x-pinctrl_8h.md#aea42cf6a2a432628bf19d6a0529121bb)#define UART1\_RS485DE\_HP9 SIWX91X\_GPIO(6, 0xFF, 4, 0, 9, 0)

[ 471](siwx91x-pinctrl_8h.md#ad70a39337d9aab0d303aa47dc6706d01)#define UART1\_RS485DE\_ULP2 SIWX91X\_GPIO(6, 6, 24, 4, 2, 2)

[ 472](siwx91x-pinctrl_8h.md#ad04deb098006e6608ddee97489cb3eec)#define UART1\_RS485DE\_ULP11 SIWX91X\_GPIO(6, 6, 33, 4, 11, 11)

[ 473](siwx91x-pinctrl_8h.md#a949839fcdd556be94b8ffec9e32cb8d7)#define UART1\_RS485EN\_HP12 SIWX91X\_GPIO(6, 0xFF, 7, 0, 12, 0)

[ 474](siwx91x-pinctrl_8h.md#abd3dfcedbb2108b5097c769ade994f26)#define UART1\_RS485EN\_HP26 SIWX91X\_GPIO(6, 0xFF, 0, 1, 10, 0)

[ 475](siwx91x-pinctrl_8h.md#a8b90c76a3932164295fd126af60be1fd)#define UART1\_RS485EN\_ULP0 SIWX91X\_GPIO(6, 6, 22, 4, 0, 0)

[ 476](siwx91x-pinctrl_8h.md#a90f57369d21e5c139b73a07d377a8cf2)#define UART1\_RS485RE\_HP8 SIWX91X\_GPIO(6, 0xFF, 3, 0, 8, 0)

[ 477](siwx91x-pinctrl_8h.md#a8407e33974cd85b26ad17b6e489bef67)#define UART1\_RS485RE\_ULP1 SIWX91X\_GPIO(6, 6, 23, 4, 1, 1)

[ 478](siwx91x-pinctrl_8h.md#a310f189ae26d3412769346ea2f506a1b)#define UART1\_RS485RE\_ULP10 SIWX91X\_GPIO(6, 6, 32, 4, 10, 10)

[ 479](siwx91x-pinctrl_8h.md#abb746abdce4e30129782624ec53fffc8)#define UART1\_RTS\_HP10 SIWX91X\_GPIO(6, 0xFF, 5, 0, 10, 0)

[ 480](siwx91x-pinctrl_8h.md#a70a72361b31640d41a6e2412ac923c9d)#define UART1\_RTS\_HP27 SIWX91X\_GPIO(6, 0xFF, 0, 1, 11, 0)

[ 481](siwx91x-pinctrl_8h.md#a230298f5a4c4c180cf1940e3416b47f6)#define UART1\_RTS\_HP28 SIWX91X\_GPIO(6, 0xFF, 0, 1, 12, 0)

[ 482](siwx91x-pinctrl_8h.md#a88ddaa52e9b50c54136234aa558bdfb1)#define UART1\_RTS\_HP31 SIWX91X\_GPIO(12, 0xFF, 9, 1, 15, 0)

[ 483](siwx91x-pinctrl_8h.md#a6d7d1bcf7f58d024e5a99328b6150a63)#define UART1\_RTS\_HP50 SIWX91X\_GPIO(9, 0xFF, 14, 3, 2, 0)

[ 484](siwx91x-pinctrl_8h.md#a1f1b7f47f6b95d512f6f0a985e81946f)#define UART1\_RTS\_ULP0 SIWX91X\_GPIO(9, 6, 22, 4, 0, 0)

[ 485](siwx91x-pinctrl_8h.md#abf9c83a461eb53b37f46abf8c8d8d196)#define UART1\_RTS\_ULP6 SIWX91X\_GPIO(6, 6, 28, 4, 6, 6)

[ 486](siwx91x-pinctrl_8h.md#a4fb7d994478de8f966e5cc655d8e973d)#define UART1\_RTS\_ULP8 SIWX91X\_GPIO(9, 6, 30, 4, 8, 8)

[ 487](siwx91x-pinctrl_8h.md#a953fa739896ecddf271f7c3339fa6073)#define UART1\_RX\_HP6 SIWX91X\_GPIO(6, 0xFF, 1, 0, 6, 0)

[ 488](siwx91x-pinctrl_8h.md#a3592a61447450351c3d3c3a55a3bdace)#define UART1\_RX\_HP29 SIWX91X\_GPIO(6, 0xFF, 0, 1, 13, 0)

[ 489](siwx91x-pinctrl_8h.md#a5b5e71f38f9a796de10379f187ca7f15)#define UART1\_RX\_HP33 SIWX91X\_GPIO(12, 0xFF, 9, 2, 1, 0)

[ 490](siwx91x-pinctrl_8h.md#a87501d9f4180905852e78361fc0f426f)#define UART1\_RX\_ULP2 SIWX91X\_GPIO(9, 6, 24, 4, 1, 1)

[ 491](siwx91x-pinctrl_8h.md#a4fea2b8bd8a2d3eab03cace6b258b143)#define UART1\_RX\_ULP4 SIWX91X\_GPIO(6, 6, 26, 4, 4, 4)

[ 492](siwx91x-pinctrl_8h.md#ab707a4b932d6f09f162ae6d1567458d1)#define UART1\_RX\_ULP8 SIWX91X\_GPIO(6, 6, 30, 4, 8, 8)

[ 493](siwx91x-pinctrl_8h.md#ad3e21323e8a22d14b6aacd4357362a33)#define UART1\_RX\_ULP10 SIWX91X\_GPIO(9, 6, 32, 4, 10, 10)

[ 494](siwx91x-pinctrl_8h.md#ae40a1f641b32672f3e82ed37249d75af)#define UART1\_TX\_HP15 SIWX91X\_GPIO(2, 0xFF, 8, 0, 15, 0)

[ 495](siwx91x-pinctrl_8h.md#a67757e78eacd012fd699e6d212f20a54)#define UART1\_TX\_HP7 SIWX91X\_GPIO(6, 0xFF, 2, 0, 7, 0)

[ 496](siwx91x-pinctrl_8h.md#a64965fbfeb33a6ed5454093b4bffb27d)#define UART1\_TX\_HP30 SIWX91X\_GPIO(6, 0xFF, 0, 1, 14, 0)

[ 497](siwx91x-pinctrl_8h.md#acdf09abb21a7b70d6672291d7a84414c)#define UART1\_TX\_HP34 SIWX91X\_GPIO(12, 0xFF, 9, 2, 2, 0)

[ 498](siwx91x-pinctrl_8h.md#ae4b6add65671db28cc0647d21cff499d)#define UART1\_TX\_ULP3 SIWX91X\_GPIO(9, 6, 25, 4, 1, 1)

[ 499](siwx91x-pinctrl_8h.md#ac68f74cffa2daadef2c11ab076d8be97)#define UART1\_TX\_ULP5 SIWX91X\_GPIO(6, 6, 27, 4, 5, 5)

[ 500](siwx91x-pinctrl_8h.md#aa46a2a94478eb8551b21373bbce52824)#define UART1\_TX\_ULP9 SIWX91X\_GPIO(6, 6, 31, 4, 9, 9)

[ 501](siwx91x-pinctrl_8h.md#a243b96ad4d1fd865f1ddbdf5174b2a69)#define UART1\_TX\_ULP11 SIWX91X\_GPIO(9, 6, 33, 4, 11, 11)

502

[ 503](siwx91x-pinctrl_8h.md#a7275562850ca4f6089036c09eebf8c80)#define ULPI2C\_SCL\_HP11 SIWX91X\_GPIO(9, 4, 6, 0, 11, 5)

[ 504](siwx91x-pinctrl_8h.md#a38bcacc0080286a4373315a53d38e3b8)#define ULPI2C\_SCL\_HP15 SIWX91X\_GPIO(9, 4, 8, 0, 15, 7)

[ 505](siwx91x-pinctrl_8h.md#a6e76fdfeea3d20133c141d86d48edb16)#define ULPI2C\_SCL\_HP7 SIWX91X\_GPIO(9, 4, 2, 0, 7, 1)

[ 506](siwx91x-pinctrl_8h.md#a2afc4d25f6b760816fa8f9a959864231)#define ULPI2C\_SCL\_HP26 SIWX91X\_GPIO(11, 4, 0, 1, 10, 7)

[ 507](siwx91x-pinctrl_8h.md#aa2d6230cf2154aca73c36bdd7645ffb6)#define ULPI2C\_SCL\_HP27 SIWX91X\_GPIO(11, 4, 0, 1, 11, 8)

[ 508](siwx91x-pinctrl_8h.md#ac99c9cd0c12ba6effb933aebb04e366c)#define ULPI2C\_SCL\_HP46 SIWX91X\_GPIO(9, 4, 10, 2, 14, 8)

[ 509](siwx91x-pinctrl_8h.md#aad197f3c66cfafe58e1c220a1017e8ac)#define ULPI2C\_SCL\_ULP1 SIWX91X\_GPIO(0xFF, 4, 0xFF, 4, 0, 1)

[ 510](siwx91x-pinctrl_8h.md#a3e08531523a985f0dbb68528551dace3)#define ULPI2C\_SCL\_ULP5 SIWX91X\_GPIO(0xFF, 4, 0xFF, 4, 0, 5)

[ 511](siwx91x-pinctrl_8h.md#ae23c01c208d25b7adff61126cd8a9bb9)#define ULPI2C\_SCL\_ULP7 SIWX91X\_GPIO(0xFF, 4, 0xFF, 4, 0, 7)

[ 512](siwx91x-pinctrl_8h.md#aa09786d189d39bae438faaeac7e7ea40)#define ULPI2C\_SCL\_ULP8 SIWX91X\_GPIO(0xFF, 4, 0xFF, 4, 0, 8)

[ 513](siwx91x-pinctrl_8h.md#abd8259056eed0e5d70592f9fb8095729)#define ULPI2C\_SDA\_HP6 SIWX91X\_GPIO(9, 4, 1, 0, 6, 0)

[ 514](siwx91x-pinctrl_8h.md#ae0c5b9e4954a0e07a299e2b8ba36e6b7)#define ULPI2C\_SDA\_HP10 SIWX91X\_GPIO(9, 4, 5, 0, 10, 4)

[ 515](siwx91x-pinctrl_8h.md#a82b2a9b7bb330cfde26d1e111bfc47d7)#define ULPI2C\_SDA\_HP12 SIWX91X\_GPIO(9, 4, 7, 0, 12, 6)

[ 516](siwx91x-pinctrl_8h.md#afc9e45ece6272ec2f02dad394f17fc30)#define ULPI2C\_SDA\_HP25 SIWX91X\_GPIO(11, 4, 0, 1, 9, 6)

[ 517](siwx91x-pinctrl_8h.md#a883987f33b163bbc8fb28990795a9935)#define ULPI2C\_SDA\_HP28 SIWX91X\_GPIO(11, 4, 0, 1, 12, 9)

[ 518](siwx91x-pinctrl_8h.md#a803522e6dfd39e6f5233663ca18da82b)#define ULPI2C\_SDA\_HP30 SIWX91X\_GPIO(11, 4, 0, 1, 14, 11)

[ 519](siwx91x-pinctrl_8h.md#a81cbbbcb500051df8654b0150eb8d43d)#define ULPI2C\_SDA\_HP47 SIWX91X\_GPIO(9, 4, 11, 2, 15, 9)

[ 520](siwx91x-pinctrl_8h.md#a89150a67ce005b8c9e9b73aa0881bdce)#define ULPI2C\_SDA\_HP49 SIWX91X\_GPIO(9, 4, 13, 3, 1, 11)

[ 521](siwx91x-pinctrl_8h.md#a683eac0b53a4a91c74c576b4f55a14c7)#define ULPI2C\_SDA\_ULP0 SIWX91X\_GPIO(0xFF, 4, 0xFF, 4, 0, 0)

[ 522](siwx91x-pinctrl_8h.md#a93cb9256a344d3e3c9e99f52512ea496)#define ULPI2C\_SDA\_ULP4 SIWX91X\_GPIO(0xFF, 4, 0xFF, 4, 0, 4)

[ 523](siwx91x-pinctrl_8h.md#a2bd7f63711f414953c3028e2c46e8713)#define ULPI2C\_SDA\_ULP6 SIWX91X\_GPIO(0xFF, 4, 0xFF, 4, 0, 6)

[ 524](siwx91x-pinctrl_8h.md#ab7ea0a99e98ac51c77077d342944342d)#define ULPI2C\_SDA\_ULP9 SIWX91X\_GPIO(0xFF, 4, 0xFF, 4, 0, 9)

[ 525](siwx91x-pinctrl_8h.md#a13be1329e1ed09001541f213841fa388)#define ULPI2C\_SDA\_ULP11 SIWX91X\_GPIO(0xFF, 4, 0xFF, 4, 0, 11)

526

[ 527](siwx91x-pinctrl_8h.md#a85b6b3979b28967d77bce8f46484afb9)#define ULPI2S\_CLK\_HP15 SIWX91X\_GPIO(9, 2, 8, 0, 15, 7)

[ 528](siwx91x-pinctrl_8h.md#aa8fb24f7b22ddd58b12e72c3151061ce)#define ULPI2S\_CLK\_HP26 SIWX91X\_GPIO(11, 2, 0, 1, 10, 7)

[ 529](siwx91x-pinctrl_8h.md#adfb54219b4ab1a7587f515246b3fa755)#define ULPI2S\_CLK\_HP27 SIWX91X\_GPIO(11, 2, 0, 1, 11, 8)

[ 530](siwx91x-pinctrl_8h.md#a7750b3caaf5ebbb795da513cbebf8859)#define ULPI2S\_CLK\_HP46 SIWX91X\_GPIO(9, 2, 10, 2, 14, 8)

[ 531](siwx91x-pinctrl_8h.md#af052bd9fc2183d48ff37b2c5bebe7f49)#define ULPI2S\_CLK\_ULP7 SIWX91X\_GPIO(0xFF, 2, 0xFF, 4, 0, 7)

[ 532](siwx91x-pinctrl_8h.md#a4d5eb6ab5c39069f6dcadd1b0bf61b59)#define ULPI2S\_CLK\_ULP8 SIWX91X\_GPIO(0xFF, 2, 0xFF, 4, 0, 8)

[ 533](siwx91x-pinctrl_8h.md#a5664aa96cc1cf08181678d30c31e9349)#define ULPI2S\_DIN\_HP12 SIWX91X\_GPIO(9, 2, 7, 0, 12, 6)

[ 534](siwx91x-pinctrl_8h.md#ab555c9e9e0732372d353cd0ae0ebdd22)#define ULPI2S\_DIN\_HP6 SIWX91X\_GPIO(9, 2, 1, 0, 6, 0)

[ 535](siwx91x-pinctrl_8h.md#a721d372c3992adb29e36a111e3394228)#define ULPI2S\_DIN\_HP25 SIWX91X\_GPIO(11, 2, 0, 1, 9, 6)

[ 536](siwx91x-pinctrl_8h.md#af180c73151f01717b2f9aaecf2ed1efc)#define ULPI2S\_DIN\_HP28 SIWX91X\_GPIO(11, 2, 0, 1, 12, 9)

[ 537](siwx91x-pinctrl_8h.md#a7e072f27104474717da3dbc2e2399ce2)#define ULPI2S\_DIN\_HP47 SIWX91X\_GPIO(9, 2, 11, 2, 15, 9)

[ 538](siwx91x-pinctrl_8h.md#a97cbfeb16a7c46e12eae6891bc037acd)#define ULPI2S\_DIN\_ULP0 SIWX91X\_GPIO(0xFF, 2, 0xFF, 4, 0, 0)

[ 539](siwx91x-pinctrl_8h.md#aaf31db6c31214cc2c80cb309bdea5536)#define ULPI2S\_DIN\_ULP6 SIWX91X\_GPIO(0xFF, 2, 0xFF, 4, 0, 6)

[ 540](siwx91x-pinctrl_8h.md#ad2907e564c41e33f35c5d031b0405142)#define ULPI2S\_DIN\_ULP9 SIWX91X\_GPIO(0xFF, 2, 0xFF, 4, 0, 9)

[ 541](siwx91x-pinctrl_8h.md#a26ed645c0e1e4dd60a2ffaa670a30308)#define ULPI2S\_DOUT\_HP7 SIWX91X\_GPIO(9, 2, 2, 0, 7, 1)

[ 542](siwx91x-pinctrl_8h.md#aa2d709ee468354d27c23b443d72ae707)#define ULPI2S\_DOUT\_HP11 SIWX91X\_GPIO(9, 2, 6, 0, 11, 5)

[ 543](siwx91x-pinctrl_8h.md#a2d914f5db178a90759278e016ed3cd6b)#define ULPI2S\_DOUT\_HP30 SIWX91X\_GPIO(11, 2, 0, 1, 14, 11)

[ 544](siwx91x-pinctrl_8h.md#a5a77eb00dec4d187575081efceed70a0)#define ULPI2S\_DOUT\_HP49 SIWX91X\_GPIO(9, 2, 13, 3, 1, 11)

[ 545](siwx91x-pinctrl_8h.md#ab1a08eb6deb7154ef3b27aed5840f1c4)#define ULPI2S\_DOUT\_ULP1 SIWX91X\_GPIO(0xFF, 2, 0xFF, 4, 0, 1)

[ 546](siwx91x-pinctrl_8h.md#adb3fcaf4510f3e9e92d6b6938d5aa4b8)#define ULPI2S\_DOUT\_ULP5 SIWX91X\_GPIO(0xFF, 2, 0xFF, 4, 0, 5)

[ 547](siwx91x-pinctrl_8h.md#abf0c090bf283519422369f8cd6641155)#define ULPI2S\_DOUT\_ULP11 SIWX91X\_GPIO(0xFF, 2, 0xFF, 4, 0, 11)

[ 548](siwx91x-pinctrl_8h.md#ac54fc86fa7f49011d07fb39cdf074788)#define ULPI2S\_WS\_HP8 SIWX91X\_GPIO(9, 2, 3, 0, 8, 2)

[ 549](siwx91x-pinctrl_8h.md#abdc82667b8b9f52c5d7cd400ff539239)#define ULPI2S\_WS\_HP10 SIWX91X\_GPIO(9, 2, 5, 0, 10, 4)

[ 550](siwx91x-pinctrl_8h.md#af2fee1bd924e2cb917c7448a961c3de9)#define ULPI2S\_WS\_HP29 SIWX91X\_GPIO(11, 2, 0, 1, 13, 10)

[ 551](siwx91x-pinctrl_8h.md#a432d784fa10f64d474034b5f30e4849c)#define ULPI2S\_WS\_HP48 SIWX91X\_GPIO(9, 2, 12, 3, 0, 10)

[ 552](siwx91x-pinctrl_8h.md#a2a27e527e270fc114138715ce610f270)#define ULPI2S\_WS\_ULP2 SIWX91X\_GPIO(0xFF, 2, 0xFF, 4, 0, 2)

[ 553](siwx91x-pinctrl_8h.md#a914dbc1a9d523e19f639ef063aeb4dfe)#define ULPI2S\_WS\_ULP4 SIWX91X\_GPIO(0xFF, 2, 0xFF, 4, 0, 4)

[ 554](siwx91x-pinctrl_8h.md#a6990494758f0d836d985baf113547d44)#define ULPI2S\_WS\_ULP10 SIWX91X\_GPIO(0xFF, 2, 0xFF, 4, 0, 10)

555

[ 556](siwx91x-pinctrl_8h.md#aa4f4246951880a5d5b0f666e055fdd68)#define ULPSSI\_CLK\_HP6 SIWX91X\_GPIO(9, 1, 1, 0, 6, 0)

[ 557](siwx91x-pinctrl_8h.md#a13792f9c1d0b86e83e420ba40aabdd02)#define ULPSSI\_CLK\_HP27 SIWX91X\_GPIO(11, 1, 0, 1, 11, 8)

[ 558](siwx91x-pinctrl_8h.md#a973efb6759449cd13223fd679f795d50)#define ULPSSI\_CLK\_HP46 SIWX91X\_GPIO(9, 1, 10, 2, 14, 8)

[ 559](siwx91x-pinctrl_8h.md#a3933d5b6f5464e2a22f466797725f5be)#define ULPSSI\_CLK\_ULP0 SIWX91X\_GPIO(0xFF, 1, 0xFF, 4, 0, 0)

[ 560](siwx91x-pinctrl_8h.md#ae811c5ecd3838c77460fafb9a47dc218)#define ULPSSI\_CLK\_ULP4 SIWX91X\_GPIO(0xFF, 8, 0xFF, 4, 0, 4)

[ 561](siwx91x-pinctrl_8h.md#ac1d6aedfec07ef370da615708fa5c98b)#define ULPSSI\_CLK\_ULP8 SIWX91X\_GPIO(0xFF, 1, 0xFF, 4, 0, 8)

[ 562](siwx91x-pinctrl_8h.md#ae75cc90a153a1c90f7fbb0c7893558d0)#define ULPSSI\_CS0\_HP29 SIWX91X\_GPIO(11, 1, 0, 1, 13, 10)

[ 563](siwx91x-pinctrl_8h.md#adfc8f3cf729bb76128de18eabd7d877a)#define ULPSSI\_CS0\_HP48 SIWX91X\_GPIO(9, 1, 12, 3, 0, 10)

[ 564](siwx91x-pinctrl_8h.md#aa8a8db9123876f6228cf83ff617d7fbb)#define ULPSSI\_CS0\_ULP7 SIWX91X\_GPIO(0xFF, 8, 0xFF, 4, 0, 7)

[ 565](siwx91x-pinctrl_8h.md#ae696d20e5ada658753a81995c196343f)#define ULPSSI\_CS0\_ULP10 SIWX91X\_GPIO(0xFF, 1, 0xFF, 4, 0, 10)

[ 566](siwx91x-pinctrl_8h.md#ad1e8bb7ce27179dfadac4836b9a26924)#define ULPSSI\_CS1\_HP10 SIWX91X\_GPIO(9, 1, 5, 0, 10, 4)

[ 567](siwx91x-pinctrl_8h.md#abcb850de6adc5db558bb9cb8a45455a6)#define ULPSSI\_CS1\_ULP4 SIWX91X\_GPIO(0xFF, 1, 0xFF, 4, 0, 4)

[ 568](siwx91x-pinctrl_8h.md#aa53895ddaa78b38c7ea5b35d6f00c78f)#define ULPSSI\_CS2\_HP12 SIWX91X\_GPIO(9, 1, 7, 0, 12, 6)

[ 569](siwx91x-pinctrl_8h.md#ac537683d973832982d538a2e3a705f7c)#define ULPSSI\_CS2\_HP25 SIWX91X\_GPIO(11, 1, 0, 1, 9, 6)

[ 570](siwx91x-pinctrl_8h.md#a3ddbf1e40ddfb1844a7c486b3d47a8fe)#define ULPSSI\_CS2\_ULP6 SIWX91X\_GPIO(0xFF, 1, 0xFF, 4, 0, 6)

[ 571](siwx91x-pinctrl_8h.md#a00b7649bb95375d2a8632938c1ab2fd8)#define ULPSSI\_DIN\_HP8 SIWX91X\_GPIO(9, 1, 3, 0, 8, 2)

[ 572](siwx91x-pinctrl_8h.md#a9d01d993af06027e11d1a2c2abd1505a)#define ULPSSI\_DIN\_HP28 SIWX91X\_GPIO(11, 1, 0, 1, 12, 9)

[ 573](siwx91x-pinctrl_8h.md#a6ffab07aba4ddfa977a8865230c35309)#define ULPSSI\_DIN\_HP47 SIWX91X\_GPIO(9, 1, 11, 2, 15, 9)

[ 574](siwx91x-pinctrl_8h.md#a8a35f9ed548c01693de57b6647a55901)#define ULPSSI\_DIN\_ULP2 SIWX91X\_GPIO(0xFF, 1, 0xFF, 4, 0, 2)

[ 575](siwx91x-pinctrl_8h.md#a3737184b07cd6dfdef580a82b31ad13c)#define ULPSSI\_DIN\_ULP6 SIWX91X\_GPIO(0xFF, 8, 0xFF, 4, 0, 6)

[ 576](siwx91x-pinctrl_8h.md#a841bd6d9d7b267db55b85dbd63c29f19)#define ULPSSI\_DIN\_ULP9 SIWX91X\_GPIO(0xFF, 1, 0xFF, 4, 0, 9)

[ 577](siwx91x-pinctrl_8h.md#a7f72ea03a247002a88d22afa4d41f4eb)#define ULPSSI\_DOUT\_HP7 SIWX91X\_GPIO(9, 1, 2, 0, 7, 1)

[ 578](siwx91x-pinctrl_8h.md#ab90410cbd5d7feccc31c858dcea5ce24)#define ULPSSI\_DOUT\_HP30 SIWX91X\_GPIO(11, 1, 0, 1, 14, 11)

[ 579](siwx91x-pinctrl_8h.md#a5c0d9281a0eae7e3f71c7622f0fcb0ca)#define ULPSSI\_DOUT\_HP49 SIWX91X\_GPIO(9, 1, 13, 3, 1, 11)

[ 580](siwx91x-pinctrl_8h.md#a7c49826415618d0edb0bf9960ab1390a)#define ULPSSI\_DOUT\_ULP1 SIWX91X\_GPIO(0xFF, 1, 0xFF, 4, 0, 1)

[ 581](siwx91x-pinctrl_8h.md#a3936c932181d9601015bfcd9ddbd9230)#define ULPSSI\_DOUT\_ULP5 SIWX91X\_GPIO(0xFF, 8, 0xFF, 4, 0, 5)

[ 582](siwx91x-pinctrl_8h.md#ae74ef587f76251d995250141665e0691)#define ULPSSI\_DOUT\_ULP11 SIWX91X\_GPIO(0xFF, 1, 0xFF, 4, 0, 11)

583

[ 584](siwx91x-pinctrl_8h.md#a7be14c47047f63a0f72b9508fb45dcb8)#define ULPUART\_CTS\_HP7 SIWX91X\_GPIO(9, 3, 2, 0, 7, 1)

[ 585](siwx91x-pinctrl_8h.md#aa9a3840c4d145ad867c1e59cf988d74a)#define ULPUART\_CTS\_HP11 SIWX91X\_GPIO(9, 3, 6, 0, 11, 5)

[ 586](siwx91x-pinctrl_8h.md#a6fa2d64e1f638a6e0a7df29a4476da03)#define ULPUART\_CTS\_HP27 SIWX91X\_GPIO(11, 3, 0, 1, 11, 8)

[ 587](siwx91x-pinctrl_8h.md#a8ae6905ee86208cfc8910d8cff7423cf)#define ULPUART\_CTS\_HP46 SIWX91X\_GPIO(9, 3, 10, 2, 14, 8)

[ 588](siwx91x-pinctrl_8h.md#acecb9492723712365609fe03429ecc62)#define ULPUART\_CTS\_ULP1 SIWX91X\_GPIO(0xFF, 3, 0xFF, 4, 0, 1)

[ 589](siwx91x-pinctrl_8h.md#a47991853f93de832cb85dba3dd51d689)#define ULPUART\_CTS\_ULP5 SIWX91X\_GPIO(0xFF, 3, 0xFF, 4, 0, 5)

[ 590](siwx91x-pinctrl_8h.md#ad87a42b5cac9d4e3e1539963c0a153ac)#define ULPUART\_CTS\_ULP8 SIWX91X\_GPIO(0xFF, 3, 0xFF, 4, 0, 8)

[ 591](siwx91x-pinctrl_8h.md#a3aa724f39856848fe3616dc2c7e0f9d5)#define ULPUART\_RTS\_HP6 SIWX91X\_GPIO(9, 3, 1, 0, 6, 0)

[ 592](siwx91x-pinctrl_8h.md#ad25318e8c8da760aca964a06c8114f3e)#define ULPUART\_RTS\_HP10 SIWX91X\_GPIO(9, 3, 5, 0, 10, 4)

[ 593](siwx91x-pinctrl_8h.md#a45126e5a5d74c85e34beede737a6c266)#define ULPUART\_RTS\_HP29 SIWX91X\_GPIO(11, 3, 0, 1, 13, 10)

[ 594](siwx91x-pinctrl_8h.md#a0fd57249b5cdaa83d1a82d96f39bfcac)#define ULPUART\_RTS\_HP48 SIWX91X\_GPIO(9, 3, 12, 3, 0, 10)

[ 595](siwx91x-pinctrl_8h.md#a6d637af94f43cbfcfd001b174d89504e)#define ULPUART\_RTS\_ULP0 SIWX91X\_GPIO(0xFF, 3, 0xFF, 4, 0, 0)

[ 596](siwx91x-pinctrl_8h.md#a905bfb63ed0825940db94f2d0e339cae)#define ULPUART\_RTS\_ULP4 SIWX91X\_GPIO(0xFF, 3, 0xFF, 4, 0, 4)

[ 597](siwx91x-pinctrl_8h.md#aafec5377fdddad88eaa5f33a616e932a)#define ULPUART\_RTS\_ULP10 SIWX91X\_GPIO(0xFF, 3, 0xFF, 4, 0, 10)

[ 598](siwx91x-pinctrl_8h.md#a7e24d72b3f26b6a64d1182b223a679a5)#define ULPUART\_RX\_HP8 SIWX91X\_GPIO(9, 3, 3, 0, 8, 2)

[ 599](siwx91x-pinctrl_8h.md#a95f0434e7aa29f3f3b8870a8f56df169)#define ULPUART\_RX\_HP12 SIWX91X\_GPIO(9, 3, 7, 0, 12, 6)

[ 600](siwx91x-pinctrl_8h.md#a17fa934bc15ff31389466f0906291c95)#define ULPUART\_RX\_HP25 SIWX91X\_GPIO(11, 3, 0, 1, 9, 6)

[ 601](siwx91x-pinctrl_8h.md#afde64cb335752ffd591ddeb40f2d24b0)#define ULPUART\_RX\_HP28 SIWX91X\_GPIO(11, 3, 0, 1, 12, 9)

[ 602](siwx91x-pinctrl_8h.md#a497302eeb072e2573948fd36b246824e)#define ULPUART\_RX\_HP47 SIWX91X\_GPIO(9, 3, 11, 2, 15, 9)

[ 603](siwx91x-pinctrl_8h.md#a5c296e125433a81362d207042b30cb7e)#define ULPUART\_RX\_ULP2 SIWX91X\_GPIO(0xFF, 3, 0xFF, 4, 0, 2)

[ 604](siwx91x-pinctrl_8h.md#a1036c7686c6ae59e387bf0df9338d8f6)#define ULPUART\_RX\_ULP6 SIWX91X\_GPIO(0xFF, 3, 0xFF, 4, 0, 6)

[ 605](siwx91x-pinctrl_8h.md#a3b868b8418ed39e8251a6d5e06da25ec)#define ULPUART\_RX\_ULP9 SIWX91X\_GPIO(0xFF, 3, 0xFF, 4, 0, 9)

[ 606](siwx91x-pinctrl_8h.md#af7d1211f086a8be91e95e88e1bcee555)#define ULPUART\_TX\_HP15 SIWX91X\_GPIO(9, 3, 8, 0, 15, 7)

[ 607](siwx91x-pinctrl_8h.md#a02c5645af20a73c856a0e7dcbf30e45a)#define ULPUART\_TX\_HP26 SIWX91X\_GPIO(11, 3, 0, 1, 10, 7)

[ 608](siwx91x-pinctrl_8h.md#ace2f51ab67c116751656f1421bac3db9)#define ULPUART\_TX\_HP30 SIWX91X\_GPIO(11, 3, 0, 1, 14, 11)

[ 609](siwx91x-pinctrl_8h.md#a8974ff95ea2efd59e1f2d16a7322f75c)#define ULPUART\_TX\_HP49 SIWX91X\_GPIO(9, 3, 13, 3, 1, 11)

[ 610](siwx91x-pinctrl_8h.md#a306f5e9ad2e84cee1074067cd6bccb4f)#define ULPUART\_TX\_ULP7 SIWX91X\_GPIO(0xFF, 3, 0xFF, 4, 0, 7)

[ 611](siwx91x-pinctrl_8h.md#a11b4b4459ff2d94267bca669da7e17cc)#define ULPUART\_TX\_ULP11 SIWX91X\_GPIO(0xFF, 3, 0xFF, 4, 0, 11)

612

[ 613](siwx91x-pinctrl_8h.md#a02c45c292ebe276e4f41101d7440480f)#define UULP\_GPIO4\_ULP2 SIWX91X\_GPIO(0xFF, 4, 0xFF, 4, 0, 2)

[ 614](siwx91x-pinctrl_8h.md#a003329462614c9ff939c451c28a011bc)#define UULP\_TESTMODE0\_ULP7 SIWX91X\_GPIO(0xFF, 11, 0xFF, 4, 0, 7)

[ 615](siwx91x-pinctrl_8h.md#aa927ee96be06692b7fecb88eec152357)#define UULP\_TESTMODE0\_ULP9 SIWX91X\_GPIO(0xFF, 5, 0xFF, 4, 0, 9)

616

617/\* clang-format on \*/

618

619/\* The following definitions are duplicates of signals that are also

620 \* available on the same pins using other GPIO modes.

621 \* #define IR\_OUTPUT\_ULP5 SIWX91X\_GPIO(0xFF, 10, 0xFF, 4, 0, 5)

622 \* #define PMU\_TEST2\_HP30 SIWX91X\_GPIO(13, 0xFF, 0, 1, 14, 0)

623 \* #define PWM\_1H\_ULP1 SIWX91X\_GPIO(8, 6, 23, 4, 1, 1)

624 \* #define PWM\_1L\_ULP0 SIWX91X\_GPIO(8, 6, 22, 4, 0, 0)

625 \*/

626

627#endif /\* INCLUDE\_ZEPHYR\_DT\_BINDINGS\_PINCTRL\_SILABS\_SIWX91X\_PINCTRL\_H\_ \*/

[silabs-pinctrl-siwx91x.h](silabs-pinctrl-siwx91x_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [pinctrl](dir_2c6c4fbd167577104b7f1b7148586168.md)
- [silabs](dir_fa47ec1716313d52a64832478c9daea4.md)
- [siwx91x-pinctrl.h](siwx91x-pinctrl_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
