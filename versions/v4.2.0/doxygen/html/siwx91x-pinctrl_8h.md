---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/siwx91x-pinctrl_8h.html
original_path: doxygen/html/siwx91x-pinctrl_8h.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

siwx91x-pinctrl.h File Reference

`#include <[zephyr/dt-bindings/pinctrl/silabs-pinctrl-siwx91x.h](silabs-pinctrl-siwx91x_8h_source.md)>`

[Go to the source code of this file.](siwx91x-pinctrl_8h_source.md)

| Macros | |
| --- | --- |
| #define | [AGPIO\_ULP0](#a51b9722e0c1470e0692d913cd70ca33e)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(0xFF, 7, 0xFF, 4, 0, 0) |
| #define | [AGPIO\_ULP1](#a30b16a45f81323324e310d96777c6fd8)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(0xFF, 7, 0xFF, 4, 0, 1) |
| #define | [AGPIO\_ULP2](#a7189b132ac6420c926c8cf2eccab3c6b)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(0xFF, 7, 0xFF, 4, 0, 2) |
| #define | [AGPIO\_ULP4](#a0d43105668987a220c67393d4674515d)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(0xFF, 7, 0xFF, 4, 0, 4) |
| #define | [AGPIO\_ULP5](#a2a66cdafa849bf095ca1d6916001f441)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(0xFF, 7, 0xFF, 4, 0, 5) |
| #define | [AGPIO\_ULP6](#a60dfb206c49bc9005231c936e9393546)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(0xFF, 7, 0xFF, 4, 0, 6) |
| #define | [AGPIO\_ULP7](#a1ff255f96fa29e9a0c500967596ac57a)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(0xFF, 7, 0xFF, 4, 0, 7) |
| #define | [AGPIO\_ULP8](#a721b2b6550307530f7ab4068cc11631b)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(0xFF, 7, 0xFF, 4, 0, 8) |
| #define | [AGPIO\_ULP9](#a228d260414f49b06912a8694b31dc358)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(0xFF, 7, 0xFF, 4, 0, 9) |
| #define | [AGPIO\_ULP10](#a57855add105b9a5ac3df1600caf2d4bc)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(0xFF, 7, 0xFF, 4, 0, 10) |
| #define | [AGPIO\_ULP11](#a3e0ca1d417d8c455c275e5e67e071c6c)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(0xFF, 7, 0xFF, 4, 0, 11) |
| #define | [ADC\_TOPGPIO\_HP25](#a06a04fbcd9f9db43dd3b4c9be9ecc196)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(14, 0xFF, 0, 1, 9, 0) |
| #define | [ADC\_TOPGPIO\_HP26](#a1c85b141f986867590feab3e2971f83e)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(14, 0xFF, 0, 1, 10, 0) |
| #define | [ADC\_TOPGPIO\_HP27](#ab786befc793ba2dabbbc3c8abccdd81c)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(14, 0xFF, 0, 1, 11, 0) |
| #define | [ADC\_TOPGPIO\_HP28](#ac6f1ca16c8640f98a9d2eccafb282302)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(14, 0xFF, 0, 1, 12, 0) |
| #define | [ADC\_TOPGPIO\_HP29](#a919a3ea12132734ffbaa583eb814e70a)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(14, 0xFF, 0, 1, 13, 0) |
| #define | [ADC\_TOPGPIO\_HP30](#ac11f4dd52f4993a9ab70d16a50be47fa)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(14, 0xFF, 0, 1, 14, 0) |
| #define | [AUXULP\_TRIG0\_HP11](#ab03b635abc6f55d9824a6e0cf1a2c94e)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(9, 5, 6, 0, 11, 5) |
| #define | [AUXULP\_TRIG0\_HP30](#aad0ba7e32d1c8d4acbd6d2d1f4b288a0)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(11, 5, 0, 1, 14, 11) |
| #define | [AUXULP\_TRIG0\_HP49](#ae321eaa930b4bcdb847c6f0595e6f46f)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(9, 5, 13, 3, 1, 11) |
| #define | [AUXULP\_TRIG0\_ULP5](#a945e911bffcedf2cd3e00b0394a990b1)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(0xFF, 5, 0xFF, 4, 0, 5) |
| #define | [AUXULP\_TRIG0\_ULP6](#a090807259f65186a27e1327fbf599829)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(0xFF, 10, 0xFF, 4, 0, 6) |
| #define | [AUXULP\_TRIG0\_ULP11](#ab92c286c8db594d8f607ce3ef09657b4)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(0xFF, 5, 0xFF, 4, 0, 11) |
| #define | [AUXULP\_TRIG1\_ULP4](#adf749c359174226e90d8a2ba64b4983c)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(0xFF, 5, 0xFF, 4, 0, 4) |
| #define | [AUXULP\_TRIG1\_ULP7](#a1d9a7c9bf69093de19cbdf10953e4c22)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(0xFF, 10, 0xFF, 4, 0, 7) |
| #define | [CLK\_I2SPLL\_HP27](#a835c36708762cd86818ce60b25384eb7)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(12, 0xFF, 0, 1, 11, 0) |
| #define | [CLK\_I2SPLL\_HP48](#aa4282adbc2f3da0006bde8511465bbff)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(10, 0xFF, 12, 3, 0, 0) |
| #define | [CLK\_I2SPLL\_HP54](#a000ce8a22cf34cb0bfbb6ae2e25e55bb)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(10, 0xFF, 18, 3, 6, 0) |
| #define | [CLK\_INTFPLL\_HP26](#a5d5b9c68af29a74c67fe4e002426d35c)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(12, 0xFF, 0, 1, 10, 0) |
| #define | [CLK\_INTFPLL\_HP47](#a7009a3f01b97860c58b29d0fc96f0df5)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(10, 0xFF, 11, 2, 15, 0) |
| #define | [CLK\_INTFPLL\_HP53](#a137db7b4fba3de386340ece21b67b3a2)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(10, 0xFF, 17, 3, 5, 0) |
| #define | [CLK\_MCUOUT\_HP11](#a679d7001a0e3864ccf0a879b5c4ccfc8)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(12, 0xFF, 6, 0, 11, 0) |
| #define | [CLK\_MEMSREF\_HP50](#a09924c650f824cca05e8b341ed9294ad)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(10, 0xFF, 14, 3, 2, 0) |
| #define | [CLK\_MEMSREF\_HP56](#afa68d89e38d316a3e729c371d8297bae)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(10, 0xFF, 20, 3, 8, 0) |
| #define | [CLK\_OUT\_HP12](#aa413920e1935cc7bfb36235fa4055922)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(8, 0xFF, 7, 0, 12, 0) |
| #define | [CLK\_OUT\_HP15](#a32ffde4590651355db3a7411ed50d270)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(8, 0xFF, 8, 0, 15, 0) |
| #define | [CLK\_PLLTESTMODE\_HP51](#a880777fe8275592e91088d050512bff3)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(10, 0xFF, 15, 3, 3, 0) |
| #define | [CLK\_SOCPLL\_HP25](#a92da5349a6b9ba8ea91ba8402bd685b2)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(12, 0xFF, 0, 1, 9, 0) |
| #define | [CLK\_SOCPLL\_HP46](#ad715b44d79cab97ac67f4ee4d7e3fd61)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(10, 0xFF, 10, 2, 14, 0) |
| #define | [CLK\_SOCPLL\_HP52](#ab0bda6530a625116653efc6ccdaf066e)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(10, 0xFF, 16, 3, 4, 0) |
| #define | [CLK\_XTALONIN\_HP28](#a898d24c287840df4a1d9b1f1d5bee3ca)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(12, 0xFF, 0, 1, 12, 0) |
| #define | [CLK\_XTALONIN\_HP57](#a5b9fea82548ee54a0a72cd10cad57b47)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(10, 0xFF, 21, 3, 9, 0) |
| #define | [COMP1\_OUT\_HP8](#aa4e79dc6178b13147dbeb10aaa6fbc6d)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(9, 5, 3, 0, 8, 2) |
| #define | [COMP1\_OUT\_HP28](#a67c405487bacc252498d58f92dd4e7f2)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(11, 5, 0, 1, 12, 9) |
| #define | [COMP1\_OUT\_HP47](#ad229716eda10b53eb40628b24bb84329)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(9, 5, 11, 2, 15, 9) |
| #define | [COMP1\_OUT\_ULP2](#a5865a449e4957f10e35208b3a8a1e186)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(0xFF, 5, 0xFF, 4, 0, 2) |
| #define | [COMP1\_OUT\_ULP6](#a61a3d2a33b017f9b509e502fb14b5ac1)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(0xFF, 9, 0xFF, 4, 0, 6) |
| #define | [COMP2\_OUT\_ULP7](#a3de5ca3d0d7078a34cc53b5c5028d7c3)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(0xFF, 9, 0xFF, 4, 0, 7) |
| #define | [GSPI\_CLK\_HP8](#a0d322c35cde263da2607b11c8dce74f1)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(4, 0xFF, 3, 0, 8, 0) |
| #define | [GSPI\_CLK\_HP25](#af45db40d737c46516891fc77bfd6991b)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(4, 0xFF, 0, 1, 9, 0) |
| #define | [GSPI\_CLK\_HP46](#a4adfba6b40f466fd220c52835338ff8f)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(4, 0xFF, 10, 2, 14, 0) |
| #define | [GSPI\_CLK\_HP52](#ab4e0b64c913aa9d1c5f9b8d7f7c564d1)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(4, 0xFF, 16, 3, 4, 0) |
| #define | [GSPI\_CS0\_HP9](#ada868d60b39f9ef5d58e3297b9569ebe)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(4, 0xFF, 4, 0, 9, 0) |
| #define | [GSPI\_CS0\_HP28](#a120041f6e17a7263e01a6cf9dbf97f55)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(4, 0xFF, 0, 1, 12, 0) |
| #define | [GSPI\_CS0\_HP49](#a9a136b1b51489fed94ebc601d1bce509)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(4, 0xFF, 13, 3, 1, 0) |
| #define | [GSPI\_CS0\_HP53](#aad59278f16c573afe6d988fec3e789ae)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(4, 0xFF, 17, 3, 5, 0) |
| #define | [GSPI\_CS1\_HP10](#a5fa623bbd9d1a30eec7af32587dd5ba1)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(4, 0xFF, 5, 0, 10, 0) |
| #define | [GSPI\_CS1\_HP29](#a5d6fc805d3e94783eb3eead3e46d3eb5)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(4, 0xFF, 0, 1, 13, 0) |
| #define | [GSPI\_CS1\_HP50](#a9fd3baadefec26d4e6532b3d22d6bfc6)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(4, 0xFF, 14, 3, 2, 0) |
| #define | [GSPI\_CS1\_HP54](#a9607f0a50a592087747f02d1dc6fe61e)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(4, 0xFF, 18, 3, 6, 0) |
| #define | [GSPI\_CS2\_HP15](#ad42cd6f9d902d0667f5a71ad2c7ead9a)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(4, 0xFF, 8, 0, 15, 0) |
| #define | [GSPI\_CS2\_HP30](#accbdbea1a397053ccc6a58d53ec8493c)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(4, 0xFF, 0, 1, 14, 0) |
| #define | [GSPI\_CS2\_HP51](#af7ff281165326d035233deb890fb9cb2)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(4, 0xFF, 15, 3, 3, 0) |
| #define | [GSPI\_CS2\_HP55](#a56ea3052bad2710a04055aa1306ef827)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(4, 0xFF, 19, 3, 7, 0) |
| #define | [GSPI\_MISO\_HP11](#a39e87f6b1067af1fd6eda77e0877c7dc)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(4, 0xFF, 6, 0, 11, 0) |
| #define | [GSPI\_MISO\_HP26](#ab9d92646ac5bfbd06eeab8727ce9f69c)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(4, 0xFF, 0, 1, 10, 0) |
| #define | [GSPI\_MISO\_HP47](#ace8e09dd531dab443c8e23567940c0c7)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(4, 0xFF, 11, 2, 15, 0) |
| #define | [GSPI\_MISO\_HP56](#ad922fdd48ef757e7ed84dc5ba0223b96)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(4, 0xFF, 20, 3, 8, 0) |
| #define | [GSPI\_MOSI\_HP6](#a10573e8f0c7675c91a907c0f5e80a9cc)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(12, 0xFF, 1, 0, 6, 0) |
| #define | [GSPI\_MOSI\_HP12](#a4e70d4d9f4da18808231e1626a81aca4)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(4, 0xFF, 7, 0, 12, 0) |
| #define | [GSPI\_MOSI\_HP27](#a2ca232ad550d21add9adc2962a844b71)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(4, 0xFF, 0, 1, 11, 0) |
| #define | [GSPI\_MOSI\_HP48](#ad7925ac094c67ed0be2418d434869ac3)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(4, 0xFF, 12, 3, 0, 0) |
| #define | [GSPI\_MOSI\_HP57](#a80818466e12929450e71aec02cdd4c7b)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(4, 0xFF, 21, 3, 9, 0) |
| #define | [I2C0\_SCL\_HP7](#a2ef351b47d12918bb4cea74c0e473db1)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(4, 0xFF, 2, 0, 7, 0) |
| #define | [I2C0\_SCL\_HP32](#ac8c62e3f52c598d1de82735a0809b0ad)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(11, 0xFF, 9, 2, 0, 0) |
| #define | [I2C0\_SCL\_ULP1](#a820c81dfce3dff2287efa78305812b7f)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(4, 6, 23, 4, 1, 1) |
| #define | [I2C0\_SCL\_ULP2](#a480ff4a4f89b88de9c46001c7ad52aed)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(4, 6, 24, 4, 2, 2) |
| #define | [I2C0\_SCL\_ULP11](#a10e1bb6b59bfb1c4ca1932f9a4be1448)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(4, 6, 33, 4, 11, 11) |
| #define | [I2C0\_SDA\_HP6](#a01c68c9f6c64829f15e5fe3e4fa4e7e7)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(4, 0xFF, 1, 0, 6, 0) |
| #define | [I2C0\_SDA\_HP31](#a9334871e0ff13605bf9fe104a8aa75f3)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(11, 0xFF, 9, 1, 15, 0) |
| #define | [I2C0\_SDA\_ULP0](#a54e93e8958d5eb99c63ce1ad2cf17e75)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(4, 6, 22, 4, 0, 0) |
| #define | [I2C0\_SDA\_ULP3](#a3a53a6594da3d36f4c186864275cdb47)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(4, 6, 25, 4, 3, 3) |
| #define | [I2C0\_SDA\_ULP10](#a26710ae6de0a217c2d3af4cb7cc14b28)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(4, 6, 32, 4, 10, 10) |
| #define | [I2C1\_SCL\_HP6](#aa5ba13c0b275c1d1fb28aed3fcd26f6a)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(5, 0xFF, 1, 0, 6, 0) |
| #define | [I2C1\_SCL\_HP29](#a24827fb9fdaa10b780a06c222062e522)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(5, 0xFF, 0, 1, 13, 0) |
| #define | [I2C1\_SCL\_HP33](#a936da856e3e3d0a8a67957c3e9a25519)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(11, 0xFF, 9, 2, 1, 0) |
| #define | [I2C1\_SCL\_HP50](#afe20556071663d815232b98293555fb7)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(5, 0xFF, 14, 3, 2, 0) |
| #define | [I2C1\_SCL\_HP54](#afdb3b18d7540906aca0a17187ce185b0)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(5, 0xFF, 18, 3, 6, 0) |
| #define | [I2C1\_SCL\_ULP0](#aa79263584dd8d9ccd4ae7564cbb50fd7)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(5, 6, 22, 4, 0, 0) |
| #define | [I2C1\_SCL\_ULP2](#a1f40c8c4305f357477f61f2bee4177aa)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(5, 6, 24, 4, 2, 2) |
| #define | [I2C1\_SCL\_ULP6](#a34ac7a645ee7c80f1d291348bdaddb1b)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(5, 6, 28, 4, 6, 6) |
| #define | [I2C1\_SDA\_HP7](#a7fdc374bc827cd67f954b638fb6ab03b)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(5, 0xFF, 2, 0, 7, 0) |
| #define | [I2C1\_SDA\_HP30](#a5d4d1af9ec0fab65e197d0f4ef9c4fc0)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(5, 0xFF, 0, 1, 14, 0) |
| #define | [I2C1\_SDA\_HP34](#aab52c1cbc805809cfe35199fb204867c)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(11, 0xFF, 9, 2, 2, 0) |
| #define | [I2C1\_SDA\_HP51](#a8889ee6d6d096a1b6790a71bb3f7db84)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(5, 0xFF, 15, 3, 3, 0) |
| #define | [I2C1\_SDA\_HP55](#a1aad71707a9c1adb14525b1809a97b31)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(5, 0xFF, 19, 3, 7, 0) |
| #define | [I2C1\_SDA\_ULP1](#adc989b20626192997d54961dd616b3b2)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(5, 6, 23, 4, 1, 1) |
| #define | [I2C1\_SDA\_ULP3](#af66e09c1a67eeae142148952ffc620cb)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(5, 6, 25, 4, 3, 3) |
| #define | [I2C1\_SDA\_ULP7](#a187fb1dd9e7f233059c7602205112d62)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(5, 6, 29, 4, 7, 7) |
| #define | [I2S0\_CLK\_HP8](#a7359e2ca7813b5abebd030d795e78706)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(7, 0xFF, 3, 0, 8, 0) |
| #define | [I2S0\_CLK\_HP25](#a5150fe8f89fdf656a051ba412f7ba9c3)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(7, 0xFF, 0, 1, 9, 0) |
| #define | [I2S0\_CLK\_HP46](#a0048da9c1376b56df1479b4689fe9de2)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(7, 0xFF, 10, 2, 14, 0) |
| #define | [I2S0\_CLK\_HP52](#aca6c330be2dc8f7b16abfa4b319cba5c)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(7, 0xFF, 16, 3, 4, 0) |
| #define | [I2S0\_DIN0\_HP10](#a303d85325bbcc79992cfa1fda5cfae07)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(7, 0xFF, 5, 0, 10, 0) |
| #define | [I2S0\_DIN0\_HP27](#a2ac13eb02c917e2ca6a184bb3e9e38db)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(7, 0xFF, 0, 1, 11, 0) |
| #define | [I2S0\_DIN0\_HP48](#afb246a50f57470d46bb8a33a90be05ad)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(7, 0xFF, 12, 3, 0, 0) |
| #define | [I2S0\_DIN0\_HP56](#ac87ec8ad8ec8321d356d7678793851ab)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(7, 0xFF, 20, 3, 8, 0) |
| #define | [I2S0\_DIN1\_HP6](#a019d02d00ed9a9d254f3350e70577214)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(7, 0xFF, 1, 0, 6, 0) |
| #define | [I2S0\_DIN1\_HP29](#a8e6c2584e4f4c323fba1ddaf7c4271e6)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(7, 0xFF, 0, 1, 13, 0) |
| #define | [I2S0\_DIN1\_HP50](#a36408b9361281baa4b6df09e94da3d04)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(7, 0xFF, 14, 3, 2, 0) |
| #define | [I2S0\_DIN1\_HP54](#ad81fc920d9067bf3beaa1b42b1a819a6)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(7, 0xFF, 18, 3, 6, 0) |
| #define | [I2S0\_DOUT0\_HP11](#aca53f49c7d835b65bcd2aefc344abe24)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(7, 0xFF, 6, 0, 11, 0) |
| #define | [I2S0\_DOUT0\_HP28](#a1f6afb833961353d943a469748a99bb3)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(7, 0xFF, 0, 1, 12, 0) |
| #define | [I2S0\_DOUT0\_HP49](#acac20029d1653abd303310ab5cfec88b)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(7, 0xFF, 13, 3, 1, 0) |
| #define | [I2S0\_DOUT0\_HP57](#aacd5f462222363c3ee0641ceaad3c9ac)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(7, 0xFF, 21, 3, 9, 0) |
| #define | [I2S0\_DOUT1\_HP7](#a9a165d304f050db860d42944f4288ec0)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(7, 0xFF, 2, 0, 7, 0) |
| #define | [I2S0\_DOUT1\_HP29](#a9b538a9b237871d89be0755a999a14aa)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(7, 0xFF, 0, 1, 14, 0) |
| #define | [I2S0\_DOUT1\_HP51](#ab6e059e2cb256557e26dedade8ce2aed)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(7, 0xFF, 15, 3, 3, 0) |
| #define | [I2S0\_DOUT1\_HP55](#abfe82c91355f572a5c4dc7dbb2e2f510)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(7, 0xFF, 19, 3, 7, 0) |
| #define | [I2S0\_WS\_HP9](#a72f19d1ace618e6c2bae69c6a3f4c5f8)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(7, 0xFF, 4, 0, 9, 0) |
| #define | [I2S0\_WS\_HP26](#a614bbb3cbb8250a3f230806139dba0c9)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(7, 0xFF, 0, 1, 10, 0) |
| #define | [I2S0\_WS\_HP47](#a1b9f3a9dfbd36791be898036417e48bf)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(7, 0xFF, 11, 2, 15, 0) |
| #define | [I2S0\_WS\_HP53](#a63944069b8a3f30dc669f01dcc8c088c)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(7, 0xFF, 17, 3, 5, 0) |
| #define | [IR\_INPUT\_HP15](#a50e3d3f0baf17368823af4bf6a21dfb7)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(9, 1, 8, 0, 15, 7) |
| #define | [IR\_INPUT\_HP26](#acef80a4a997f5d5231e3f60856b864e1)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(11, 1, 0, 1, 10, 7) |
| #define | [IR\_INPUT\_HP29](#a5e4fc91a184b54b490bb615fdf3a25ab)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(11, 4, 0, 1, 13, 10) |
| #define | [IR\_INPUT\_HP48](#ac0035f0f87cbb64a9e0dbbadc61388e4)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(9, 4, 12, 3, 0, 10) |
| #define | [IR\_INPUT\_ULP4](#a0d995f35796fc445efe7ebee649bdf2f)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(0xFF, 10, 0xFF, 4, 0, 4) |
| #define | [IR\_INPUT\_ULP7](#aadd97a3fa547212bd510340b3ab05c2d)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(0xFF, 1, 0xFF, 4, 0, 7) |
| #define | [IR\_INPUT\_ULP10](#a4c3793bc7cc985cf1f80aef136d18ce2)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(0xFF, 4, 0xFF, 4, 0, 10) |
| #define | [IR\_OUTPUT\_HP11](#a2c041f872981f73b54ccf7af03aa8a36)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(9, 1, 6, 0, 11, 5) |
| #define | [IR\_OUTPUT\_ULP5](#adb645e594a5654f35cbd3e852445e19b)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(0xFF, 1, 0xFF, 4, 0, 5) |
| #define | [PMU\_TEST1\_HP6](#a29207f055fc19e97082391195ef8cf78)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(8, 0xFF, 1, 0, 6, 0) |
| #define | [PMU\_TEST1\_HP29](#a87863eae390ce502e6c84ce7d1110874)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(8, 0xFF, 0, 1, 13, 0) |
| #define | [PMU\_TEST1\_HP30](#a01e9261c0bd8327120ae6da5686a6d3a)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(12, 0xFF, 0, 1, 14, 0) |
| #define | [PMU\_TEST1\_ULP0](#a4055f713ecf4e2f57c49c57321fdff99)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(13, 6, 22, 4, 0, 0) |
| #define | [PMU\_TEST1\_ULP2](#a60de9f9f3085bee8341e118462a7fdcf)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(10, 6, 24, 4, 2, 2) |
| #define | [PMU\_TEST1\_ULP6](#ae687c8d547e498569a8b23f419216262)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(12, 6, 28, 4, 6, 6) |
| #define | [PMU\_TEST1\_ULP10](#a4cee250941565f3e3eb36b6d0a4e3364)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(10, 6, 32, 4, 10, 10) |
| #define | [PMU\_TEST2\_HP7](#a928e861887b2162d1f000910d6454d53)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(8, 0xFF, 2, 0, 7, 0) |
| #define | [PMU\_TEST2\_HP30](#a49436320a6c491ae61450c6f71beec48)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(8, 0xFF, 0, 1, 14, 0) |
| #define | [PMU\_TEST2\_ULP1](#ad3cdee5e821dc5b3c68e45ec4b49bfbe)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(13, 6, 23, 4, 1, 1) |
| #define | [PMU\_TEST2\_ULP3](#a9eae278334a605347f6e95e9250cc7e7)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(10, 6, 25, 4, 3, 3) |
| #define | [PMU\_TEST2\_ULP7](#a0510f2e9687d07fe386be8718198990c)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(12, 6, 29, 4, 7, 7) |
| #define | [PMU\_TEST2\_ULP11](#a810fcca28118ef6dff963923b9af34d9)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(10, 6, 33, 4, 11, 11) |
| #define | [PSRAM\_CLK\_HP46](#a676931253894b60c9d0f60a3c9a45380)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(11, 0xFF, 10, 2, 14, 0) |
| #define | [PSRAM\_CLK\_HP52](#a7a8e755805d8aef6a1c1202297527ceb)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(12, 0xFF, 16, 3, 4, 0) |
| #define | [PSRAM\_CSN0\_HP49](#aa717c6eebeb0b80e410f405464a0e23a)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(11, 0xFF, 13, 3, 1, 0) |
| #define | [PSRAM\_CSN0\_HP55](#a1f0492fd0544bf8c1d01a534ee8b09dc)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(12, 0xFF, 19, 3, 7, 0) |
| #define | [PSRAM\_CSN1\_HP53](#a5160d8e3311dc7e81fc88035e30b1298)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(11, 0xFF, 17, 3, 5, 0) |
| #define | [PSRAM\_D0\_HP47](#a8505eee03f6dc307947fe9bba9cc868f)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(11, 0xFF, 11, 2, 15, 0) |
| #define | [PSRAM\_D0\_HP53](#a5d2e115dab81d01f2059f108ef43df66)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(12, 0xFF, 17, 3, 5, 0) |
| #define | [PSRAM\_D1\_HP48](#ae039ebfbbcb4f8d9c2941fad9cf21c25)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(11, 0xFF, 12, 3, 0, 0) |
| #define | [PSRAM\_D1\_HP54](#a660ebada1169b4d19a0876b985e04a06)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(12, 0xFF, 18, 3, 6, 0) |
| #define | [PSRAM\_D2\_HP50](#ab5bee0e001079fbd5fb0d974942aa598)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(11, 0xFF, 14, 3, 2, 0) |
| #define | [PSRAM\_D2\_HP56](#acaed40bf53fd610ef38615a15cc24774)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(12, 0xFF, 20, 3, 8, 0) |
| #define | [PSRAM\_D3\_HP51](#a19bf5beb8bca44b470e155431c0244a7)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(11, 0xFF, 15, 3, 3, 0) |
| #define | [PSRAM\_D3\_HP57](#a2630b64edaffea76cf3a071d31494c00)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(12, 0xFF, 21, 3, 9, 0) |
| #define | [PSRAM\_D4\_HP54](#ae3d2d17a5bd7b4c09c17cefe9febce73)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(11, 0xFF, 18, 3, 6, 0) |
| #define | [PSRAM\_D5\_HP55](#a1ca55c42f77714d9c1088b200dc9dc8f)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(11, 0xFF, 19, 3, 7, 0) |
| #define | [PSRAM\_D6\_HP56](#a9cb3582c88b3d07af732ebdcb239ba7b)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(11, 0xFF, 20, 3, 8, 0) |
| #define | [PSRAM\_D7\_HP57](#a9e255793e353deb52e77a03359580322)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(11, 0xFF, 21, 3, 9, 0) |
| #define | [PWM\_0H\_HP7](#ae04b42ec4c9f7b009a5a06a3ec01b35b)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(10, 0xFF, 2, 0, 7, 0) |
| #define | [PWM\_0H\_ULP1](#a0fd1688f5f60e0a874ce283a18713e7a)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(12, 6, 23, 4, 1, 1) |
| #define | [PWM\_0L\_HP6](#a38fdb4b305f7ae6afb490118d52ef9bc)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(10, 0xFF, 1, 0, 6, 0) |
| #define | [PWM\_0L\_ULP0](#aa94e0a3dce4a99d76a019a0bf168e004)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(12, 6, 22, 4, 0, 0) |
| #define | [PWM\_1H\_HP9](#acde3e8d6e27699ac4e8637813c6db6c9)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(10, 0xFF, 4, 0, 9, 0) |
| #define | [PWM\_1H\_ULP3](#ad11994d9f6d4ee1aecc042f61f720b42)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(8, 6, 25, 4, 3, 3) |
| #define | [PWM\_1H\_ULP5](#aeb72ce214bbeac3fea2296177e436cf0)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(12, 6, 27, 4, 5, 5) |
| #define | [PWM\_1L\_HP8](#ae5b9d0282a760965899a0c163f58423c)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(10, 0xFF, 3, 0, 8, 0) |
| #define | [PWM\_1L\_ULP2](#a9e79d0a4b569d73d5ee7f65c1e2f20fc)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(8, 6, 24, 4, 2, 2) |
| #define | [PWM\_1L\_ULP4](#ab07ed6a6db4d9a7bdcb79d9d08635055)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(12, 6, 26, 4, 4, 4) |
| #define | [PWM\_2H\_HP11](#a840701d4644973e31b0c49caa1fb52ce)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(10, 0xFF, 6, 0, 11, 0) |
| #define | [PWM\_2H\_ULP5](#abf08c72c301bfd555f41e34b99f2076e)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(8, 6, 27, 4, 5, 5) |
| #define | [PWM\_2L\_HP10](#a7c60a35ecb5f5dc6448a96b3e3c89baf)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(10, 0xFF, 5, 0, 10, 0) |
| #define | [PWM\_2L\_ULP4](#ac8708b22008c4408a38456f7b8258328)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(8, 6, 26, 4, 4, 4) |
| #define | [PWM\_3H\_HP15](#a507ec5bf9c637916ca37dee6de1d1a96)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(10, 0xFF, 8, 0, 15, 0) |
| #define | [PWM\_3H\_ULP7](#aea69719dd1cfa3a94f9f3a30459b51ed)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(8, 6, 29, 4, 7, 7) |
| #define | [PWM\_3L\_HP12](#ae8d79d461423e0353022eab80c3025c8)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(10, 0xFF, 7, 0, 12, 0) |
| #define | [PWM\_3L\_ULP6](#ac6590ab64265b8c3bad3d30da7620604)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(8, 6, 28, 4, 6, 6) |
| #define | [PWM\_EXTTRIG0\_HP27](#a4508139ab59dee416bd0aa7a53f2e2d5)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(10, 0xFF, 0, 1, 11, 0) |
| #define | [PWM\_EXTTRIG0\_HP51](#a92c8c16ef38b80853b297d31a6dd4964)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(8, 0xFF, 15, 3, 3, 0) |
| #define | [PWM\_EXTTRIG0\_ULP6](#a65e5a78cc5cc390a802818a4f19ae8d4)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(10, 6, 28, 4, 6, 6) |
| #define | [PWM\_EXTTRIG0\_ULP11](#ac991e3bbd300bb3fb9b27a1d8d7fc5f2)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(8, 6, 33, 4, 11, 11) |
| #define | [PWM\_EXTTRIG1\_HP28](#a0d191c0b60c2b836e3856a0e5c434649)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(10, 0xFF, 0, 1, 12, 0) |
| #define | [PWM\_EXTTRIG1\_HP54](#afb4d7dfd327df023d9e3268678d3313e)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(8, 0xFF, 18, 3, 6, 0) |
| #define | [PWM\_EXTTRIG1\_ULP7](#a5d8597d305f1ac3b6f5ed8b5b85da936)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(10, 6, 29, 4, 7, 7) |
| #define | [PWM\_EXTTRIG2\_HP29](#a0516ffe89d34afcebe7b594def541e37)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(10, 0xFF, 0, 1, 13, 0) |
| #define | [PWM\_EXTTRIG2\_HP55](#a7c46b667cc3ce330c6d75f79f97b764b)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(8, 0xFF, 19, 3, 7, 0) |
| #define | [PWM\_EXTTRIG2\_ULP8](#a83421e64cf0f348be8cce195d0eb27c1)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(10, 6, 30, 4, 8, 8) |
| #define | [PWM\_EXTTRIG3\_HP30](#a478e0230aa6373a816bfbf4c6ec5da96)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(10, 0xFF, 0, 1, 14, 0) |
| #define | [PWM\_EXTTRIG3\_HP50](#ac4b0686f2db1db395ff0ffba43e7e1b7)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(8, 0xFF, 14, 3, 2, 0) |
| #define | [PWM\_EXTTRIG3\_ULP9](#a5c3cf988f7d14ecaca8e02734cb15eee)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(10, 6, 31, 4, 9, 9) |
| #define | [PWM\_FAULTA\_HP25](#a73af0f23d97c3f7c3466e29be238d2e9)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(10, 0xFF, 0, 1, 9, 0) |
| #define | [PWM\_FAULTA\_ULP4](#a1be2559bbd5c14e4b8d02fae6d834db3)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(10, 6, 26, 4, 4, 4) |
| #define | [PWM\_FAULTA\_ULP9](#a898809d281a1451c860755372034ac14)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(8, 6, 31, 4, 9, 9) |
| #define | [PWM\_FAULTB\_HP26](#a2d00f4de6aa3fe5ba797a8a50fd16751)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(10, 0xFF, 0, 1, 10, 0) |
| #define | [PWM\_FAULTB\_ULP5](#ad631deeca8cc40fcc2df48ec50297c9f)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(10, 6, 27, 4, 5, 5) |
| #define | [PWM\_FAULTB\_ULP10](#a4bfb8e85f37893aceed66e457c34b9bd)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(8, 6, 32, 4, 10, 10) |
| #define | [PWM\_SLEEPEVENT\_ULP8](#a4f0903ae305c9bf1a9808b139a537a5d)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(8, 6, 30, 4, 8, 8) |
| #define | [QEI\_DIR\_HP11](#ab648897fd2173a6306ea1f12581a5257)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(5, 0xFF, 6, 0, 11, 0) |
| #define | [QEI\_DIR\_HP28](#acc5868c473301e8556cddd9d867bd0fe)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(5, 0xFF, 0, 1, 12, 0) |
| #define | [QEI\_DIR\_HP34](#a7fcabffea8d0e7f0ca1d7b3b53c77554)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(13, 0xFF, 9, 2, 2, 0) |
| #define | [QEI\_DIR\_HP49](#ac0df08c2fad11c4d658d9f715d610bbe)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(3, 0xFF, 13, 3, 1, 0) |
| #define | [QEI\_DIR\_HP57](#aecd388fd3a1c7d76cbc3b058d333fbdc)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(5, 0xFF, 21, 3, 9, 0) |
| #define | [QEI\_DIR\_ULP3](#a6be591b8ce2f422f66e10e7c1591e835)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(3, 6, 25, 4, 3, 3) |
| #define | [QEI\_DIR\_ULP7](#a0d53fec86fc5cd9aa5b094d0f6e8229b)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(3, 6, 29, 4, 7, 7) |
| #define | [QEI\_DIR\_ULP11](#a6bcd0fd50eb5acfbd616b96a041a8b40)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(3, 6, 33, 4, 11, 11) |
| #define | [QEI\_IDX\_HP8](#a3023c95f055645c0c988b5578d7943eb)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(5, 0xFF, 3, 0, 8, 0) |
| #define | [QEI\_IDX\_HP31](#aca6d952fdb3eb1bd2c9fcd088770e482)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(13, 0xFF, 9, 1, 15, 0) |
| #define | [QEI\_IDX\_HP25](#a41c53b072b0975e7b39725a0cedd6b49)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(5, 0xFF, 0, 1, 9, 0) |
| #define | [QEI\_IDX\_HP46](#aa2f488c074c7133f4457594dc8f57000)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(3, 0xFF, 10, 2, 14, 0) |
| #define | [QEI\_IDX\_HP52](#a0637cea93d1c922d3540551a92b5e8d6)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(5, 0xFF, 16, 3, 4, 0) |
| #define | [QEI\_IDX\_ULP0](#aa5571fa3facfca9e58accb575a8aa14b)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(3, 6, 22, 4, 0, 0) |
| #define | [QEI\_IDX\_ULP4](#a5e4085d82f00810d0d8a0c79bae2fb8b)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(3, 6, 26, 4, 4, 4) |
| #define | [QEI\_IDX\_ULP8](#ade023149f5a2daf2c21d2a5b8db31ebf)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(3, 6, 30, 4, 8, 8) |
| #define | [QEI\_PHA\_HP9](#a7c2638ce5bd7fe1fc3aed00841ebf805)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(5, 0xFF, 4, 0, 9, 0) |
| #define | [QEI\_PHA\_HP26](#afd774767dbccf18955aa2acd8fe3f27c)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(5, 0xFF, 0, 1, 10, 0) |
| #define | [QEI\_PHA\_HP32](#a1e7b4deeddd4e6139fee6a55752cff49)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(13, 0xFF, 9, 2, 0, 0) |
| #define | [QEI\_PHA\_HP47](#a9442f432d1602296f6ca19c43f4e4e32)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(3, 0xFF, 11, 2, 15, 0) |
| #define | [QEI\_PHA\_HP53](#ab6729735aa0f81049c357142ce64a3fb)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(5, 0xFF, 17, 3, 5, 0) |
| #define | [QEI\_PHA\_ULP1](#a02cd57249ab4cbe4ac6f50bf4ac4640d)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(3, 6, 23, 4, 1, 1) |
| #define | [QEI\_PHA\_ULP5](#a05d2c45f5f6f8e6caa749fa62f8952d2)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(3, 6, 27, 4, 5, 5) |
| #define | [QEI\_PHA\_ULP9](#a4e7d6e023c35e3c9afe66dea3c777f2f)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(3, 6, 31, 4, 9, 9) |
| #define | [QEI\_PHB\_HP10](#aeb1bc91f700271730e3ef17a2c0f2713)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(5, 0xFF, 5, 0, 10, 0) |
| #define | [QEI\_PHB\_HP27](#a1df3d67f2727fb71a0639c352b397154)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(5, 0xFF, 0, 1, 11, 0) |
| #define | [QEI\_PHB\_HP33](#a46fa92c9b2cb1139dc6d436251d238c9)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(13, 0xFF, 9, 2, 1, 0) |
| #define | [QEI\_PHB\_HP48](#a19b95ea8cddcf086fc2ffe5a46d43f13)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(3, 0xFF, 12, 3, 0, 0) |
| #define | [QEI\_PHB\_HP56](#a8a2ebd9d12f75fd4fef28190c03c4e60)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(5, 0xFF, 20, 3, 8, 0) |
| #define | [QEI\_PHB\_ULP2](#af323d2f63b6a1e26b9aa05a64c74ffbf)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(3, 6, 24, 4, 2, 2) |
| #define | [QEI\_PHB\_ULP6](#addcd05ab910922d7924bf01b643bec87)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(3, 6, 28, 4, 6, 6) |
| #define | [QEI\_PHB\_ULP10](#a2b7eafbd2fdae8fc813ebebbd912539b)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(3, 6, 32, 4, 10, 10) |
| #define | [QSPI\_CLK\_HP8](#a9c3d01a17c03a4a1facc7a06453e1cf9)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(11, 0xFF, 3, 0, 8, 0) |
| #define | [QSPI\_CLK\_HP46](#a7672e6df6d9de5ba6945492cf635ccb0)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(1, 0xFF, 10, 2, 14, 0) |
| #define | [QSPI\_CLK\_HP52](#a0f23032eac930624c7ec43e5be873ff5)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(9, 0xFF, 16, 3, 4, 0) |
| #define | [QSPI\_CSN0\_HP7](#a821ba16d8ff315bad8999a6e6ec219a8)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(11, 0xFF, 2, 0, 7, 0) |
| #define | [QSPI\_CSN0\_HP49](#a96e4e990dd6f716ae41bbfb560b36b0e)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(1, 0xFF, 13, 3, 1, 0) |
| #define | [QSPI\_CSN0\_HP55](#a12adeb047d22f21a55a9c33d434f5876)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(9, 0xFF, 19, 3, 7, 0) |
| #define | [QSPI\_CSN1\_HP7](#ab67034dc6fe34b9cdf4b6623e06ce0b0)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(12, 0xFF, 2, 0, 7, 0) |
| #define | [QSPI\_CSN1\_HP53](#a41005274eb64b874b2bc57bf75de0ea2)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(1, 0xFF, 17, 3, 5, 0) |
| #define | [QSPI\_CSN9\_HP49](#a532ec03ed4eef5b2830ec449eed145dc)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(10, 0xFF, 13, 3, 1, 0) |
| #define | [QSPI\_D0\_HP6](#a776bb46ee650922c9d8d6bf0796cf2b9)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(11, 0xFF, 1, 0, 6, 0) |
| #define | [QSPI\_D0\_HP47](#a6a443443e9195422d2aefe95d62263c3)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(1, 0xFF, 11, 2, 15, 0) |
| #define | [QSPI\_D0\_HP53](#a29fe7871dbef16e0f98dea867e444c90)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(9, 0xFF, 17, 3, 5, 0) |
| #define | [QSPI\_D1\_HP9](#ac8616e792c4715d73899701b08aabdad)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(11, 0xFF, 4, 0, 9, 0) |
| #define | [QSPI\_D1\_HP48](#abdb757e9c432a11b30649f5a09a8c896)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(1, 0xFF, 12, 3, 0, 0) |
| #define | [QSPI\_D1\_HP54](#ab0dffa76350eeeb2d3eb9c0adbdb9088)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(9, 0xFF, 18, 3, 6, 0) |
| #define | [QSPI\_D2\_HP10](#aa32be2bfcdea9856c7c50606245cc74e)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(11, 0xFF, 5, 0, 10, 0) |
| #define | [QSPI\_D2\_HP50](#aee6e6ee41ebe13d44d0264f337d3db4f)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(1, 0xFF, 14, 3, 2, 0) |
| #define | [QSPI\_D2\_HP56](#a08c29c30a534bbb0f24d91d76f96f41a)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(9, 0xFF, 20, 3, 8, 0) |
| #define | [QSPI\_D3\_HP11](#a5c85e86968bbd77e4fa2797af059ff59)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(11, 0xFF, 6, 0, 11, 0) |
| #define | [QSPI\_D3\_HP51](#a966ce19ae5d27c19817c06dd865d643a)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(1, 0xFF, 15, 3, 3, 0) |
| #define | [QSPI\_D3\_HP57](#ae4a6bb7540deaa29fc63cfe9ac5b6650)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(9, 0xFF, 21, 3, 9, 0) |
| #define | [QSPI\_D4\_HP54](#ab02591e8fcb3a366d42b0507ebdd218b)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(1, 0xFF, 18, 3, 6, 0) |
| #define | [QSPI\_D5\_HP55](#a1a35413b75de975a97da3321a0c0072e)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(1, 0xFF, 19, 3, 7, 0) |
| #define | [QSPI\_D6\_HP56](#a4380587dc3fa09f5908edcd48fa26aa3)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(1, 0xFF, 20, 3, 8, 0) |
| #define | [QSPI\_D7\_HP57](#adad1d5fd641d6eaa11653eb7fa821b2e)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(1, 0xFF, 21, 3, 9, 0) |
| #define | [SCT\_IN0\_HP25](#aa062df96d3fd76dfde6eeb4e0a882278)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(9, 0xFF, 0, 1, 9, 0) |
| #define | [SCT\_IN0\_ULP0](#a99b69d8a4f849a64b236986a2abc21c9)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(7, 6, 22, 4, 0, 0) |
| #define | [SCT\_IN0\_ULP4](#a3ab3d2e1f5a11a5386b700f03cf98b59)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(9, 6, 26, 4, 4, 4) |
| #define | [SCT\_IN1\_HP26](#a129dc73d20f20394c4c30fbecd755cf5)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(9, 0xFF, 0, 1, 10, 0) |
| #define | [SCT\_IN1\_ULP1](#a0795a0474012f940b032bf0c93a54283)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(7, 6, 23, 4, 1, 1) |
| #define | [SCT\_IN1\_ULP5](#aa543bccd5eaa129a2e71626bfb5a9e0e)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(9, 6, 27, 4, 5, 5) |
| #define | [SCT\_IN2\_HP27](#ac120a628c9b6f2f55b99ab810e6575fb)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(9, 0xFF, 0, 1, 11, 0) |
| #define | [SCT\_IN2\_ULP2](#a2d6b23ffe6db55ca5e76118dea7a14ea)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(7, 6, 24, 4, 2, 2) |
| #define | [SCT\_IN2\_ULP6](#aa9e34755ee740ce485048bc6edae12b1)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(9, 6, 28, 4, 6, 6) |
| #define | [SCT\_IN3\_HP28](#a62b8aa7dd85b312896c126bc09daf4f0)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(9, 0xFF, 0, 1, 12, 0) |
| #define | [SCT\_IN3\_ULP3](#a20d138a68cefaf8a5785def1553adf10)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(7, 6, 25, 4, 3, 3) |
| #define | [SCT\_IN3\_ULP7](#a9f850c61dbeb18c64e8d133cc37aee77)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(9, 6, 29, 4, 7, 7) |
| #define | [SCT\_OUT0\_HP29](#a487a88c8ad8a9c5cfa33639ea27ac5d2)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(9, 0xFF, 0, 1, 13, 0) |
| #define | [SCT\_OUT0\_ULP4](#a31a6744e2a07d61f7aff3a64d29c6345)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(7, 6, 26, 4, 4, 4) |
| #define | [SCT\_OUT1\_HP30](#a8d5e593bab255708bb5a34549dbc39ff)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(9, 0xFF, 0, 1, 14, 0) |
| #define | [SCT\_OUT1\_ULP5](#aeee61408d7a9d0fb3ec2b099bf6b4925)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(7, 6, 27, 4, 5, 5) |
| #define | [SCT\_OUT2\_HP8](#a896f7133bc09d5776b8fce43a919a582)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(12, 0xFF, 3, 0, 8, 0) |
| #define | [SCT\_OUT2\_ULP6](#aceb19f98ff9d765be5ac4163c400b30f)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(7, 6, 28, 4, 6, 6) |
| #define | [SCT\_OUT3\_HP9](#a23b5eb6cd7cb43df14db4f42a05d8b70)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(12, 0xFF, 4, 0, 9, 0) |
| #define | [SCT\_OUT3\_ULP7](#a3d240479009ee2c1660006406a51e14b)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(7, 6, 29, 4, 7, 7) |
| #define | [SCT\_OUT4\_ULP4](#aa1ce9c940b0f1b1f85e8c0aa765afe58)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(13, 6, 26, 4, 4, 4) |
| #define | [SCT\_OUT4\_ULP8](#a56f04a2fdf3d596c09989bb7f2f4d711)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(7, 6, 30, 4, 8, 8) |
| #define | [SCT\_OUT5\_ULP5](#abddc79f260ecc7fb85878f5182f0b4b2)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(13, 6, 27, 4, 5, 5) |
| #define | [SCT\_OUT5\_ULP9](#a14ad4c709bf766e5568ec2214c29935d)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(7, 6, 31, 4, 9, 9) |
| #define | [SCT\_OUT6\_ULP6](#ab3ecf512e8c70db0f9a7a374d5c4ee61)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(13, 6, 28, 4, 6, 6) |
| #define | [SCT\_OUT6\_ULP10](#a9833d3691184034534dac5542141979c)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(7, 6, 32, 4, 10, 10) |
| #define | [SCT\_OUT7\_ULP7](#a58d91744df7f674a8d639efee6ada664)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(13, 6, 29, 4, 7, 7) |
| #define | [SCT\_OUT7\_ULP11](#a72096ef61c9b342223b90a4a2a2cad67)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(7, 6, 33, 4, 11, 11) |
| #define | [SIO\_0\_HP6](#a0832163dccdf4899e70bc54e1c1d76b9)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(1, 0xFF, 1, 0, 6, 0) |
| #define | [SIO\_0\_HP25](#a50c459097b961e8f0b8ebb4b0022ff24)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(1, 0xFF, 0, 1, 9, 0) |
| #define | [SIO\_0\_ULP0](#ac962669966622a760066ae1d644cf16e)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(1, 6, 22, 4, 0, 0) |
| #define | [SIO\_0\_ULP8](#a9e2fbc5435e49df883f1cf0394ca5720)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(1, 6, 30, 4, 8, 8) |
| #define | [SIO\_1\_HP7](#aeb287420b59b4085df40b2bc8c4a9bb8)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(1, 0xFF, 2, 0, 7, 0) |
| #define | [SIO\_1\_HP26](#ab1bffb41dcfd954d4110cdb091b5f1dd)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(1, 0xFF, 0, 1, 10, 0) |
| #define | [SIO\_1\_ULP1](#ac6a3e01783137270cf5fa27b02c62c5c)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(1, 6, 23, 4, 1, 1) |
| #define | [SIO\_1\_ULP9](#ac75318d95fac4ae093072ed1f73e18c0)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(1, 6, 31, 4, 9, 9) |
| #define | [SIO\_2\_HP8](#a09ae893ea29f226c66d823ea6d8e9dea)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(1, 0xFF, 3, 0, 8, 0) |
| #define | [SIO\_2\_HP27](#a89795f8bd3ae258fa3c0f1daf2521d55)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(1, 0xFF, 0, 1, 11, 0) |
| #define | [SIO\_2\_ULP2](#accd43e63baf2ece7c3105e7b1179281f)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(1, 6, 24, 4, 2, 2) |
| #define | [SIO\_2\_ULP10](#ab203641292581774bcf3ea40e5c6f465)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(1, 6, 32, 4, 10, 10) |
| #define | [SIO\_3\_HP9](#a3ee11e86b6d00fb603f8389a69ace17f)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(1, 0xFF, 4, 0, 9, 0) |
| #define | [SIO\_3\_HP28](#af40550b595f5f30ac0a6ae2335e6ec55)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(1, 0xFF, 0, 1, 12, 0) |
| #define | [SIO\_3\_ULP3](#ae271fa5750acca3534ea22178fea6fc5)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(1, 6, 25, 4, 3, 3) |
| #define | [SIO\_3\_ULP11](#acafbbec57e7c4b952398106cb9a03ef7)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(1, 6, 33, 4, 11, 11) |
| #define | [SIO\_4\_HP10](#acbe0ac06f6094ddc13e5ff98ecf9345d)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(1, 0xFF, 5, 0, 10, 0) |
| #define | [SIO\_4\_HP29](#a2abfaa99057e594bdd1b3ed640744114)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(1, 0xFF, 0, 1, 13, 0) |
| #define | [SIO\_4\_ULP4](#ac0274ba6c1129339f49f087e9b503759)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(1, 6, 26, 4, 4, 4) |
| #define | [SIO\_5\_HP11](#a6da8512e01689d6eff690f5ad538bc01)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(1, 0xFF, 6, 0, 11, 0) |
| #define | [SIO\_5\_HP30](#a81766e7a7df2e5f915517f2065750c7a)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(1, 0xFF, 0, 1, 14, 0) |
| #define | [SIO\_5\_ULP5](#a07a673ae96d7332b5799d7e779180cc9)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(1, 6, 27, 4, 5, 5) |
| #define | [SIO\_6\_ULP6](#ab6d4f24470587604725bb9612d988b34)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(1, 6, 28, 4, 6, 6) |
| #define | [SIO\_7\_HP15](#aa6a42c96535dd6934fa0bc4886ea00b7)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(1, 0xFF, 8, 0, 15, 0) |
| #define | [SIO\_7\_ULP7](#a52635e4cce4a478134455ea5ee43c962)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(1, 6, 29, 4, 7, 7) |
| #define | [SSI\_CLK\_HP8](#a0d8209a8fb54f5ef19bb86981b383c43)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(3, 0xFF, 3, 0, 8, 0) |
| #define | [SSI\_CLK\_HP25](#a77b8278e81edee91c96c990c2479144f)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(3, 0xFF, 0, 1, 9, 0) |
| #define | [SSI\_CLK\_HP52](#a166065c88ad7a8bf66d6ca7b51628a2f)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(3, 0xFF, 16, 3, 4, 0) |
| #define | [SSI\_CS0\_HP9](#ac29bdcb9b8693277b6b6e8950576b4d7)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(3, 0xFF, 4, 0, 9, 0) |
| #define | [SSI\_CS0\_HP28](#aa070abef007fb1355d3a151038c4b282)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(3, 0xFF, 0, 1, 12, 0) |
| #define | [SSI\_CS0\_HP53](#a9e28d21c0d469b33398b0c24936478bc)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(3, 0xFF, 17, 3, 5, 0) |
| #define | [SSI\_CS1\_HP10](#a2858feb71f44abd3b8e0a49d00fd5a03)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(3, 0xFF, 5, 0, 10, 0) |
| #define | [SSI\_CS2\_HP15](#a7b0f6b3e42fb8329ed491b5561aef908)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(3, 0xFF, 8, 0, 15, 0) |
| #define | [SSI\_CS2\_HP50](#a0c54f4dc5efdcc32a32dc79449f58ea1)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(3, 0xFF, 14, 3, 2, 0) |
| #define | [SSI\_CS3\_HP51](#aafdfc33c0bbe11b258479379ed42d486)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(3, 0xFF, 15, 3, 3, 0) |
| #define | [SSI\_DATA0\_HP11](#ab65665cb7ad83803229e49b068615593)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(3, 0xFF, 6, 0, 11, 0) |
| #define | [SSI\_DATA0\_HP26](#a636c99a6026a8463ebd53ac63a270956)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(3, 0xFF, 0, 1, 10, 0) |
| #define | [SSI\_DATA0\_HP56](#ac204f25409e010a300cdbe48c6ad255b)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(3, 0xFF, 20, 3, 8, 0) |
| #define | [SSI\_DATA1\_HP10](#a3481b7ccfebdb2e679127a99b9410443)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(12, 0xFF, 5, 0, 10, 0) |
| #define | [SSI\_DATA1\_HP12](#a3ca3fd4c997fc966808b637bd5ce9cf5)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(3, 0xFF, 7, 0, 12, 0) |
| #define | [SSI\_DATA1\_HP27](#a755e7244b7708e5863da85b21891f0f6)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(3, 0xFF, 0, 1, 11, 0) |
| #define | [SSI\_DATA1\_HP57](#ace422b65e5eda30314e575c25633ff83)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(3, 0xFF, 21, 3, 9, 0) |
| #define | [SSI\_DATA2\_HP6](#a91b07b14b58117fe2cd6627a7a9831f8)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(3, 0xFF, 1, 0, 6, 0) |
| #define | [SSI\_DATA2\_HP29](#aed349cea226d2b4577aafb3f916cf921)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(3, 0xFF, 0, 1, 13, 0) |
| #define | [SSI\_DATA2\_HP54](#a46431de74f13595e9f143032b1e7816e)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(3, 0xFF, 18, 3, 6, 0) |
| #define | [SSI\_DATA3\_HP7](#ae03aa3be0edb0c5dcd4fbbb3c7d48038)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(3, 0xFF, 2, 0, 7, 0) |
| #define | [SSI\_DATA3\_HP30](#a5e711f668e3bf36c0068868019d91dfd)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(3, 0xFF, 0, 1, 14, 0) |
| #define | [SSI\_DATA3\_HP55](#a6a3f96e3b7129d2d1625da6ef7be0e52)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(3, 0xFF, 19, 3, 7, 0) |
| #define | [SSIS\_CLK\_HP8](#ad2741d1cf1901f68ab2825a2cade5712)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(8, 0xFF, 3, 0, 8, 0) |
| #define | [SSIS\_CLK\_HP26](#a246b34d2a347e66749a95f2865f40060)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(8, 0xFF, 0, 1, 10, 0) |
| #define | [SSIS\_CLK\_HP47](#a50d2c8019a3e7b2c7b2d9c62c092c239)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(8, 0xFF, 11, 2, 15, 0) |
| #define | [SSIS\_CLK\_HP52](#a8aaf5a65d4af6ad97b74eb4d280aa808)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(8, 0xFF, 16, 3, 4, 0) |
| #define | [SSIS\_CS\_HP9](#a558f00dabc8270c6e3464311055c927c)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(8, 0xFF, 4, 0, 9, 0) |
| #define | [SSIS\_CS\_HP25](#a0ccfb2d0b256ae264aa2fab362240537)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(8, 0xFF, 0, 1, 9, 0) |
| #define | [SSIS\_CS\_HP46](#a33ddacd923544e99d56f12b00d3a58c4)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(8, 0xFF, 10, 2, 14, 0) |
| #define | [SSIS\_CS\_HP53](#af37723fe1fb0edfd1cef5334fa2286e0)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(8, 0xFF, 17, 3, 5, 0) |
| #define | [SSIS\_MISO\_HP11](#af11a72c74fc5de2890ff29882a549c7d)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(8, 0xFF, 6, 0, 11, 0) |
| #define | [SSIS\_MISO\_HP28](#ac29849ee9448a7da3dc0dfd9584fe8e6)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(8, 0xFF, 0, 1, 12, 0) |
| #define | [SSIS\_MISO\_HP49](#af26a275bd867021c3c2fe617b2f90d56)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(8, 0xFF, 13, 3, 1, 0) |
| #define | [SSIS\_MISO\_HP57](#a303a10aa5fac51931f1fd2625476c250)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(8, 0xFF, 21, 3, 9, 0) |
| #define | [SSIS\_MOSI\_HP10](#a09804ebbc7f861922372cca189f539c1)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(8, 0xFF, 5, 0, 10, 0) |
| #define | [SSIS\_MOSI\_HP27](#a0217b56cf5d51ef66de6aba1d2a7e75e)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(8, 0xFF, 0, 1, 11, 0) |
| #define | [SSIS\_MOSI\_HP48](#a4227e1213145f52cf732f237256f9606)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(8, 0xFF, 12, 3, 0, 0) |
| #define | [SSIS\_MOSI\_HP56](#acc3c25b45390c7e676d06717dc468251)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(8, 0xFF, 20, 3, 8, 0) |
| #define | [TIMER0\_HP7](#a239d90024707952ed74238c3fc97608e)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(9, 5, 2, 0, 7, 1) |
| #define | [TIMER0\_HP27](#a49ae74d218db2a1132075c68c4574099)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(11, 5, 0, 1, 11, 8) |
| #define | [TIMER0\_HP46](#aa8a483b521b450670203463f7d8be032)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(9, 5, 10, 2, 14, 8) |
| #define | [TIMER0\_ULP4](#a8043999b57da3920d59a3c61e68a26ae)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(0xFF, 9, 0xFF, 4, 0, 4) |
| #define | [TIMER0\_ULP8](#a412766982e02327695695d09968e4ee0)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(0xFF, 5, 0xFF, 4, 0, 8) |
| #define | [TIMER1\_HP15](#a02a30a238516586b3e9f9d168edb855c)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(9, 5, 8, 0, 15, 7) |
| #define | [TIMER1\_HP26](#a99e02ee3b901fc1ee4d9ea1021f9c746)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(11, 5, 0, 1, 10, 7) |
| #define | [TIMER1\_ULP5](#a99832252de48cc89d11c3e522ea44376)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(0xFF, 9, 0xFF, 4, 0, 5) |
| #define | [TIMER1\_ULP7](#aa1fb1deae2ad43558df04b772029957f)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(0xFF, 5, 0xFF, 4, 0, 7) |
| #define | [TIMER2\_ULP1](#aa778464dc8449625d49328f30c76e92e)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(0xFF, 5, 0xFF, 4, 0, 1) |
| #define | [TRACE\_CLK\_HP7](#ad5d637f7c1e783f5bdd0f72d90a986cd)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(13, 0xFF, 2, 0, 7, 0) |
| #define | [TRACE\_CLK\_HP47](#aa4fe9698b15438987cee0d3c0d4ed193)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(6, 0xFF, 11, 2, 15, 0) |
| #define | [TRACE\_CLK\_HP53](#a9934d0e8efc26562ca6b28b3f5ece6e4)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(6, 0xFF, 17, 3, 5, 0) |
| #define | [TRACE\_CLKIN\_HP6](#ad942d16221a23fae94615aeda7acb650)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(13, 0xFF, 1, 0, 6, 0) |
| #define | [TRACE\_CLKIN\_HP15](#ab332137012b6fb95cf5d5eac07950296)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(6, 0xFF, 8, 0, 15, 0) |
| #define | [TRACE\_CLKIN\_HP46](#ae1259534ea8316ebe29436705e258f69)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(6, 0xFF, 10, 2, 14, 0) |
| #define | [TRACE\_CLKIN\_HP52](#a93a66a67b4b079b2d6ab0f64bccb5b7f)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(6, 0xFF, 16, 3, 4, 0) |
| #define | [TRACE\_D0\_HP8](#a329ce75fc9014134a8684d7e384bb569)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(13, 0xFF, 3, 0, 8, 0) |
| #define | [TRACE\_D0\_HP48](#a25196d0c4d77efa6d1340aade4a7ab43)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(6, 0xFF, 12, 3, 0, 0) |
| #define | [TRACE\_D0\_HP54](#afa79f060e825009dcbf30c194cfd259a)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(6, 0xFF, 18, 3, 6, 0) |
| #define | [TRACE\_D1\_HP9](#a6ac2fd081f541973db09767923e5c994)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(13, 0xFF, 4, 0, 9, 0) |
| #define | [TRACE\_D1\_HP49](#ac26e1b82bb464c5e2d1d4ed606b83f4c)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(6, 0xFF, 13, 3, 1, 0) |
| #define | [TRACE\_D1\_HP55](#ab019d73a28e7fd218c301a7a16a8744c)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(6, 0xFF, 19, 3, 7, 0) |
| #define | [TRACE\_D2\_HP10](#a8b1bae5956611a7a7ea0b9479236eba8)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(13, 0xFF, 5, 0, 10, 0) |
| #define | [TRACE\_D2\_HP50](#aabaa120c9882567d5fcb51adf4bee1d6)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(6, 0xFF, 14, 3, 2, 0) |
| #define | [TRACE\_D2\_HP56](#af2e5c3c47489489a5bb89767683f0426)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(6, 0xFF, 20, 3, 8, 0) |
| #define | [TRACE\_D3\_HP11](#ae6e493f9ab1a119b3b0d51ae46a09abb)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(13, 0xFF, 6, 0, 11, 0) |
| #define | [TRACE\_D3\_HP51](#a72ec3566d71b12eeaaa00e196f0d04b2)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(6, 0xFF, 15, 3, 3, 0) |
| #define | [TRACE\_D3\_HP57](#a74a11c7d6068e66986c6410f63a87a12)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(6, 0xFF, 21, 3, 9, 0) |
| #define | [UART0\_CLK\_HP8](#a1514c950553999c21e0d43c2d6aefddf)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(2, 0xFF, 3, 0, 8, 0) |
| #define | [UART0\_CLK\_HP25](#a702cef077f6ec6ba684e0cccff48e2ee)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(2, 0xFF, 0, 1, 9, 0) |
| #define | [UART0\_CLK\_HP52](#a8d19011b7dfb8ecca987d95084f1ef43)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(2, 0xFF, 16, 3, 4, 0) |
| #define | [UART0\_CLK\_ULP0](#a2df47af0f0a9b175663bfce524da6187)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(2, 6, 22, 4, 0, 0) |
| #define | [UART0\_CTS\_HP6](#a873d1ee0fbe9c691bba5c72eb88989b6)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(2, 0xFF, 1, 0, 6, 0) |
| #define | [UART0\_CTS\_HP26](#a16193dab96a8006cf2766c5cb152a32c)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(2, 0xFF, 0, 1, 10, 0) |
| #define | [UART0\_CTS\_HP56](#ae56529f660d670b4b8d21417a6e09de2)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(2, 0xFF, 20, 3, 8, 0) |
| #define | [UART0\_CTS\_ULP6](#a274238cb4dd58655ac8571d803e6bbb8)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(2, 6, 28, 4, 6, 6) |
| #define | [UART0\_DCD\_HP12](#aafcfe3007f6c11254e06dd61c92b3f4e)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(2, 0xFF, 7, 0, 12, 0) |
| #define | [UART0\_DCD\_HP29](#a5b8c6daf4798492ddd1bd1f36fc2ad70)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(12, 0xFF, 0, 1, 13, 0) |
| #define | [UART0\_DSR\_HP11](#a09324d646d1b31f3ef1064dec42cd87b)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(2, 0xFF, 6, 0, 11, 0) |
| #define | [UART0\_DSR\_HP57](#ae156c04dd623cd446e9b0e2e233638f3)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(2, 0xFF, 21, 3, 9, 0) |
| #define | [UART0\_DTR\_HP7](#a3593158afb8848932439923fddb5c0ac)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(2, 0xFF, 2, 0, 7, 0) |
| #define | [UART0\_IRRX\_HP25](#a19dead7b9533bed8693a6f730ad5fd91)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(13, 0xFF, 0, 1, 9, 0) |
| #define | [UART0\_IRRX\_HP47](#a9c2a4489ec8c0f9244485b4db066ca3f)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(2, 0xFF, 11, 2, 15, 0) |
| #define | [UART0\_IRRX\_ULP0](#adf611f1df2303d5155e071ccc56d8c30)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(11, 6, 22, 4, 0, 0) |
| #define | [UART0\_IRRX\_ULP7](#a659bdb287f75f00c7c644ae554983860)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(2, 6, 29, 4, 7, 7) |
| #define | [UART0\_IRTX\_HP26](#a96681675723bed89eef7ed2ff68324b2)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(13, 0xFF, 0, 1, 10, 0) |
| #define | [UART0\_IRTX\_HP48](#a5ada8867e27615e304abb89e8ed95b4a)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(2, 0xFF, 12, 3, 0, 0) |
| #define | [UART0\_IRTX\_ULP1](#ab9422f6b18b7d95f257eea54708c0da6)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(11, 6, 23, 4, 1, 1) |
| #define | [UART0\_IRTX\_ULP8](#adbcb3a2ebb68225e265ac83d77755540)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(2, 6, 30, 4, 8, 8) |
| #define | [UART0\_RI\_HP27](#ae5f8f182da81b3b8dd85c32be0219439)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(2, 0xFF, 0, 1, 11, 0) |
| #define | [UART0\_RI\_HP46](#a3938be42c21041a362aaec421751d9aa)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(2, 0xFF, 10, 2, 14, 0) |
| #define | [UART0\_RI\_ULP4](#a64d2529c38303a82f24b01ed5ad05be0)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(11, 6, 26, 4, 4, 4) |
| #define | [UART0\_RS485DE\_HP29](#af607a3b3e6374ce5bd6311b657eed71e)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(13, 0xFF, 0, 1, 13, 0) |
| #define | [UART0\_RS485DE\_HP51](#a50b16324373e3e32370d570491a4f535)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(2, 0xFF, 15, 3, 3, 0) |
| #define | [UART0\_RS485DE\_ULP7](#a02a8e7b5adfc32af7af4e5ba088ce0f7)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(11, 6, 29, 4, 7, 7) |
| #define | [UART0\_RS485DE\_ULP11](#a041682ac7bc0eaad6ef3b4e2e3ef3fc3)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(2, 6, 33, 4, 11, 11) |
| #define | [UART0\_RS485EN\_HP27](#a777e97d29443a4a43d92c39ba2d6480b)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(13, 0xFF, 0, 1, 11, 0) |
| #define | [UART0\_RS485EN\_HP49](#aa5a0741a5fcb9e89f16dd286e4e4d1d1)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(2, 0xFF, 13, 3, 1, 0) |
| #define | [UART0\_RS485EN\_ULP5](#a91f4ac4b0941ef7177ee9b4896d3ab51)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(11, 6, 27, 4, 5, 5) |
| #define | [UART0\_RS485EN\_ULP9](#a398e1bdbebdfae8177daa590b7a026ca)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(2, 6, 31, 4, 9, 9) |
| #define | [UART0\_RS485RE\_HP28](#a3f359f67b459ed81e8db5fd786e7089a)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(13, 0xFF, 0, 1, 12, 0) |
| #define | [UART0\_RS485RE\_HP50](#a19efcf4ac776bbb3156508a1b580e2f3)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(2, 0xFF, 14, 3, 2, 0) |
| #define | [UART0\_RS485RE\_ULP6](#a0704cd391bbb230d5a359ec1f8dfcb5c)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(11, 6, 28, 4, 6, 6) |
| #define | [UART0\_RS485RE\_ULP10](#a806d9ce45c9bdac84f82da94b2e61623)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(2, 6, 32, 4, 10, 10) |
| #define | [UART0\_RTS\_HP9](#a5b04f93bc8455f7943a7dc71414f6fdd)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(2, 0xFF, 4, 0, 9, 0) |
| #define | [UART0\_RTS\_HP28](#af6180ba7e3498e1cb075cf84d08ac0c5)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(2, 0xFF, 0, 1, 12, 0) |
| #define | [UART0\_RTS\_HP53](#a0b18d3117184a53274c9455a1d2ba7d6)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(2, 0xFF, 17, 3, 5, 0) |
| #define | [UART0\_RTS\_ULP5](#acdeb030914a38257f40ba31622a8e44f)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(2, 6, 27, 4, 5, 5) |
| #define | [UART0\_RX\_HP10](#aa12f9238e599d54cde0246c41ee7f216)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(2, 0xFF, 5, 0, 10, 0) |
| #define | [UART0\_RX\_HP29](#a5f034df81ac363d212da25a510fd8869)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(2, 0xFF, 0, 1, 13, 0) |
| #define | [UART0\_RX\_HP55](#a7c3b4144654fe9a24db90b57998e4cb4)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(2, 0xFF, 19, 3, 7, 0) |
| #define | [UART0\_RX\_ULP1](#ae6d9c15cfc89ceb5d8ad3d2b5a7756c7)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(2, 6, 23, 4, 1, 1) |
| #define | [UART0\_RX\_ULP6](#a27cb5f1b5a7d5798fb219c3a6659acb6)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(4, 6, 28, 4, 6, 6) |
| #define | [UART0\_TX\_HP30](#a310df59fe4dc6cf528b1bafe00c41c7a)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(2, 0xFF, 0, 1, 14, 0) |
| #define | [UART0\_TX\_HP54](#a913663cca98288505e45479c213ea0d0)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(2, 0xFF, 18, 3, 6, 0) |
| #define | [UART0\_TX\_ULP4](#a4d763a3c1a9bf10f42187482c5a2ba34)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(2, 6, 26, 4, 4, 4) |
| #define | [UART0\_TX\_ULP7](#a8fd486e3b0c02b1f578a38e1d6c30a38)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(4, 6, 29, 4, 7, 7) |
| #define | [UART1\_CTS\_HP11](#a4ca4f60081c355860a6a10bfa428bc98)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(6, 0xFF, 6, 0, 11, 0) |
| #define | [UART1\_CTS\_HP32](#a1782fbe55aa8e6f8bd75da573c755223)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(12, 0xFF, 9, 2, 0, 0) |
| #define | [UART1\_CTS\_HP51](#a66ca158c30cc3087b3ae12824e86398f)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(9, 0xFF, 15, 3, 3, 0) |
| #define | [UART1\_CTS\_ULP1](#aa8245d65007636996d67ca46d5c5a9fd)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(9, 6, 23, 4, 1, 1) |
| #define | [UART1\_CTS\_ULP7](#a281ee7fbfe1a8ee2814d0f6ba60e61f6)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(6, 6, 29, 4, 7, 7) |
| #define | [UART1\_CTS\_ULP9](#a7ddce4735336b046b99dcee26d4f90c3)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(9, 6, 31, 4, 9, 9) |
| #define | [UART1\_RS485DE\_HP9](#aea42cf6a2a432628bf19d6a0529121bb)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(6, 0xFF, 4, 0, 9, 0) |
| #define | [UART1\_RS485DE\_ULP2](#ad70a39337d9aab0d303aa47dc6706d01)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(6, 6, 24, 4, 2, 2) |
| #define | [UART1\_RS485DE\_ULP11](#ad04deb098006e6608ddee97489cb3eec)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(6, 6, 33, 4, 11, 11) |
| #define | [UART1\_RS485EN\_HP12](#a949839fcdd556be94b8ffec9e32cb8d7)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(6, 0xFF, 7, 0, 12, 0) |
| #define | [UART1\_RS485EN\_HP26](#abd3dfcedbb2108b5097c769ade994f26)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(6, 0xFF, 0, 1, 10, 0) |
| #define | [UART1\_RS485EN\_ULP0](#a8b90c76a3932164295fd126af60be1fd)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(6, 6, 22, 4, 0, 0) |
| #define | [UART1\_RS485RE\_HP8](#a90f57369d21e5c139b73a07d377a8cf2)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(6, 0xFF, 3, 0, 8, 0) |
| #define | [UART1\_RS485RE\_ULP1](#a8407e33974cd85b26ad17b6e489bef67)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(6, 6, 23, 4, 1, 1) |
| #define | [UART1\_RS485RE\_ULP10](#a310f189ae26d3412769346ea2f506a1b)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(6, 6, 32, 4, 10, 10) |
| #define | [UART1\_RTS\_HP10](#abb746abdce4e30129782624ec53fffc8)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(6, 0xFF, 5, 0, 10, 0) |
| #define | [UART1\_RTS\_HP27](#a70a72361b31640d41a6e2412ac923c9d)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(6, 0xFF, 0, 1, 11, 0) |
| #define | [UART1\_RTS\_HP28](#a230298f5a4c4c180cf1940e3416b47f6)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(6, 0xFF, 0, 1, 12, 0) |
| #define | [UART1\_RTS\_HP31](#a88ddaa52e9b50c54136234aa558bdfb1)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(12, 0xFF, 9, 1, 15, 0) |
| #define | [UART1\_RTS\_HP50](#a6d7d1bcf7f58d024e5a99328b6150a63)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(9, 0xFF, 14, 3, 2, 0) |
| #define | [UART1\_RTS\_ULP0](#a1f1b7f47f6b95d512f6f0a985e81946f)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(9, 6, 22, 4, 0, 0) |
| #define | [UART1\_RTS\_ULP6](#abf9c83a461eb53b37f46abf8c8d8d196)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(6, 6, 28, 4, 6, 6) |
| #define | [UART1\_RTS\_ULP8](#a4fb7d994478de8f966e5cc655d8e973d)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(9, 6, 30, 4, 8, 8) |
| #define | [UART1\_RX\_HP6](#a953fa739896ecddf271f7c3339fa6073)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(6, 0xFF, 1, 0, 6, 0) |
| #define | [UART1\_RX\_HP29](#a3592a61447450351c3d3c3a55a3bdace)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(6, 0xFF, 0, 1, 13, 0) |
| #define | [UART1\_RX\_HP33](#a5b5e71f38f9a796de10379f187ca7f15)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(12, 0xFF, 9, 2, 1, 0) |
| #define | [UART1\_RX\_ULP2](#a87501d9f4180905852e78361fc0f426f)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(9, 6, 24, 4, 1, 1) |
| #define | [UART1\_RX\_ULP4](#a4fea2b8bd8a2d3eab03cace6b258b143)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(6, 6, 26, 4, 4, 4) |
| #define | [UART1\_RX\_ULP8](#ab707a4b932d6f09f162ae6d1567458d1)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(6, 6, 30, 4, 8, 8) |
| #define | [UART1\_RX\_ULP10](#ad3e21323e8a22d14b6aacd4357362a33)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(9, 6, 32, 4, 10, 10) |
| #define | [UART1\_TX\_HP15](#ae40a1f641b32672f3e82ed37249d75af)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(2, 0xFF, 8, 0, 15, 0) |
| #define | [UART1\_TX\_HP7](#a67757e78eacd012fd699e6d212f20a54)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(6, 0xFF, 2, 0, 7, 0) |
| #define | [UART1\_TX\_HP30](#a64965fbfeb33a6ed5454093b4bffb27d)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(6, 0xFF, 0, 1, 14, 0) |
| #define | [UART1\_TX\_HP34](#acdf09abb21a7b70d6672291d7a84414c)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(12, 0xFF, 9, 2, 2, 0) |
| #define | [UART1\_TX\_ULP3](#ae4b6add65671db28cc0647d21cff499d)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(9, 6, 25, 4, 1, 1) |
| #define | [UART1\_TX\_ULP5](#ac68f74cffa2daadef2c11ab076d8be97)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(6, 6, 27, 4, 5, 5) |
| #define | [UART1\_TX\_ULP9](#aa46a2a94478eb8551b21373bbce52824)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(6, 6, 31, 4, 9, 9) |
| #define | [UART1\_TX\_ULP11](#a243b96ad4d1fd865f1ddbdf5174b2a69)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(9, 6, 33, 4, 11, 11) |
| #define | [ULPI2C\_SCL\_HP11](#a7275562850ca4f6089036c09eebf8c80)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(9, 4, 6, 0, 11, 5) |
| #define | [ULPI2C\_SCL\_HP15](#a38bcacc0080286a4373315a53d38e3b8)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(9, 4, 8, 0, 15, 7) |
| #define | [ULPI2C\_SCL\_HP7](#a6e76fdfeea3d20133c141d86d48edb16)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(9, 4, 2, 0, 7, 1) |
| #define | [ULPI2C\_SCL\_HP26](#a2afc4d25f6b760816fa8f9a959864231)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(11, 4, 0, 1, 10, 7) |
| #define | [ULPI2C\_SCL\_HP27](#aa2d6230cf2154aca73c36bdd7645ffb6)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(11, 4, 0, 1, 11, 8) |
| #define | [ULPI2C\_SCL\_HP46](#ac99c9cd0c12ba6effb933aebb04e366c)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(9, 4, 10, 2, 14, 8) |
| #define | [ULPI2C\_SCL\_ULP1](#aad197f3c66cfafe58e1c220a1017e8ac)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(0xFF, 4, 0xFF, 4, 0, 1) |
| #define | [ULPI2C\_SCL\_ULP5](#a3e08531523a985f0dbb68528551dace3)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(0xFF, 4, 0xFF, 4, 0, 5) |
| #define | [ULPI2C\_SCL\_ULP7](#ae23c01c208d25b7adff61126cd8a9bb9)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(0xFF, 4, 0xFF, 4, 0, 7) |
| #define | [ULPI2C\_SCL\_ULP8](#aa09786d189d39bae438faaeac7e7ea40)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(0xFF, 4, 0xFF, 4, 0, 8) |
| #define | [ULPI2C\_SDA\_HP6](#abd8259056eed0e5d70592f9fb8095729)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(9, 4, 1, 0, 6, 0) |
| #define | [ULPI2C\_SDA\_HP10](#ae0c5b9e4954a0e07a299e2b8ba36e6b7)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(9, 4, 5, 0, 10, 4) |
| #define | [ULPI2C\_SDA\_HP12](#a82b2a9b7bb330cfde26d1e111bfc47d7)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(9, 4, 7, 0, 12, 6) |
| #define | [ULPI2C\_SDA\_HP25](#afc9e45ece6272ec2f02dad394f17fc30)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(11, 4, 0, 1, 9, 6) |
| #define | [ULPI2C\_SDA\_HP28](#a883987f33b163bbc8fb28990795a9935)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(11, 4, 0, 1, 12, 9) |
| #define | [ULPI2C\_SDA\_HP30](#a803522e6dfd39e6f5233663ca18da82b)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(11, 4, 0, 1, 14, 11) |
| #define | [ULPI2C\_SDA\_HP47](#a81cbbbcb500051df8654b0150eb8d43d)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(9, 4, 11, 2, 15, 9) |
| #define | [ULPI2C\_SDA\_HP49](#a89150a67ce005b8c9e9b73aa0881bdce)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(9, 4, 13, 3, 1, 11) |
| #define | [ULPI2C\_SDA\_ULP0](#a683eac0b53a4a91c74c576b4f55a14c7)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(0xFF, 4, 0xFF, 4, 0, 0) |
| #define | [ULPI2C\_SDA\_ULP4](#a93cb9256a344d3e3c9e99f52512ea496)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(0xFF, 4, 0xFF, 4, 0, 4) |
| #define | [ULPI2C\_SDA\_ULP6](#a2bd7f63711f414953c3028e2c46e8713)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(0xFF, 4, 0xFF, 4, 0, 6) |
| #define | [ULPI2C\_SDA\_ULP9](#ab7ea0a99e98ac51c77077d342944342d)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(0xFF, 4, 0xFF, 4, 0, 9) |
| #define | [ULPI2C\_SDA\_ULP11](#a13be1329e1ed09001541f213841fa388)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(0xFF, 4, 0xFF, 4, 0, 11) |
| #define | [ULPI2S\_CLK\_HP15](#a85b6b3979b28967d77bce8f46484afb9)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(9, 2, 8, 0, 15, 7) |
| #define | [ULPI2S\_CLK\_HP26](#aa8fb24f7b22ddd58b12e72c3151061ce)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(11, 2, 0, 1, 10, 7) |
| #define | [ULPI2S\_CLK\_HP27](#adfb54219b4ab1a7587f515246b3fa755)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(11, 2, 0, 1, 11, 8) |
| #define | [ULPI2S\_CLK\_HP46](#a7750b3caaf5ebbb795da513cbebf8859)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(9, 2, 10, 2, 14, 8) |
| #define | [ULPI2S\_CLK\_ULP7](#af052bd9fc2183d48ff37b2c5bebe7f49)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(0xFF, 2, 0xFF, 4, 0, 7) |
| #define | [ULPI2S\_CLK\_ULP8](#a4d5eb6ab5c39069f6dcadd1b0bf61b59)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(0xFF, 2, 0xFF, 4, 0, 8) |
| #define | [ULPI2S\_DIN\_HP12](#a5664aa96cc1cf08181678d30c31e9349)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(9, 2, 7, 0, 12, 6) |
| #define | [ULPI2S\_DIN\_HP6](#ab555c9e9e0732372d353cd0ae0ebdd22)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(9, 2, 1, 0, 6, 0) |
| #define | [ULPI2S\_DIN\_HP25](#a721d372c3992adb29e36a111e3394228)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(11, 2, 0, 1, 9, 6) |
| #define | [ULPI2S\_DIN\_HP28](#af180c73151f01717b2f9aaecf2ed1efc)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(11, 2, 0, 1, 12, 9) |
| #define | [ULPI2S\_DIN\_HP47](#a7e072f27104474717da3dbc2e2399ce2)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(9, 2, 11, 2, 15, 9) |
| #define | [ULPI2S\_DIN\_ULP0](#a97cbfeb16a7c46e12eae6891bc037acd)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(0xFF, 2, 0xFF, 4, 0, 0) |
| #define | [ULPI2S\_DIN\_ULP6](#aaf31db6c31214cc2c80cb309bdea5536)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(0xFF, 2, 0xFF, 4, 0, 6) |
| #define | [ULPI2S\_DIN\_ULP9](#ad2907e564c41e33f35c5d031b0405142)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(0xFF, 2, 0xFF, 4, 0, 9) |
| #define | [ULPI2S\_DOUT\_HP7](#a26ed645c0e1e4dd60a2ffaa670a30308)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(9, 2, 2, 0, 7, 1) |
| #define | [ULPI2S\_DOUT\_HP11](#aa2d709ee468354d27c23b443d72ae707)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(9, 2, 6, 0, 11, 5) |
| #define | [ULPI2S\_DOUT\_HP30](#a2d914f5db178a90759278e016ed3cd6b)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(11, 2, 0, 1, 14, 11) |
| #define | [ULPI2S\_DOUT\_HP49](#a5a77eb00dec4d187575081efceed70a0)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(9, 2, 13, 3, 1, 11) |
| #define | [ULPI2S\_DOUT\_ULP1](#ab1a08eb6deb7154ef3b27aed5840f1c4)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(0xFF, 2, 0xFF, 4, 0, 1) |
| #define | [ULPI2S\_DOUT\_ULP5](#adb3fcaf4510f3e9e92d6b6938d5aa4b8)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(0xFF, 2, 0xFF, 4, 0, 5) |
| #define | [ULPI2S\_DOUT\_ULP11](#abf0c090bf283519422369f8cd6641155)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(0xFF, 2, 0xFF, 4, 0, 11) |
| #define | [ULPI2S\_WS\_HP8](#ac54fc86fa7f49011d07fb39cdf074788)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(9, 2, 3, 0, 8, 2) |
| #define | [ULPI2S\_WS\_HP10](#abdc82667b8b9f52c5d7cd400ff539239)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(9, 2, 5, 0, 10, 4) |
| #define | [ULPI2S\_WS\_HP29](#af2fee1bd924e2cb917c7448a961c3de9)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(11, 2, 0, 1, 13, 10) |
| #define | [ULPI2S\_WS\_HP48](#a432d784fa10f64d474034b5f30e4849c)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(9, 2, 12, 3, 0, 10) |
| #define | [ULPI2S\_WS\_ULP2](#a2a27e527e270fc114138715ce610f270)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(0xFF, 2, 0xFF, 4, 0, 2) |
| #define | [ULPI2S\_WS\_ULP4](#a914dbc1a9d523e19f639ef063aeb4dfe)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(0xFF, 2, 0xFF, 4, 0, 4) |
| #define | [ULPI2S\_WS\_ULP10](#a6990494758f0d836d985baf113547d44)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(0xFF, 2, 0xFF, 4, 0, 10) |
| #define | [ULPSSI\_CLK\_HP6](#aa4f4246951880a5d5b0f666e055fdd68)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(9, 1, 1, 0, 6, 0) |
| #define | [ULPSSI\_CLK\_HP27](#a13792f9c1d0b86e83e420ba40aabdd02)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(11, 1, 0, 1, 11, 8) |
| #define | [ULPSSI\_CLK\_HP46](#a973efb6759449cd13223fd679f795d50)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(9, 1, 10, 2, 14, 8) |
| #define | [ULPSSI\_CLK\_ULP0](#a3933d5b6f5464e2a22f466797725f5be)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(0xFF, 1, 0xFF, 4, 0, 0) |
| #define | [ULPSSI\_CLK\_ULP4](#ae811c5ecd3838c77460fafb9a47dc218)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(0xFF, 8, 0xFF, 4, 0, 4) |
| #define | [ULPSSI\_CLK\_ULP8](#ac1d6aedfec07ef370da615708fa5c98b)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(0xFF, 1, 0xFF, 4, 0, 8) |
| #define | [ULPSSI\_CS0\_HP29](#ae75cc90a153a1c90f7fbb0c7893558d0)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(11, 1, 0, 1, 13, 10) |
| #define | [ULPSSI\_CS0\_HP48](#adfc8f3cf729bb76128de18eabd7d877a)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(9, 1, 12, 3, 0, 10) |
| #define | [ULPSSI\_CS0\_ULP7](#aa8a8db9123876f6228cf83ff617d7fbb)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(0xFF, 8, 0xFF, 4, 0, 7) |
| #define | [ULPSSI\_CS0\_ULP10](#ae696d20e5ada658753a81995c196343f)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(0xFF, 1, 0xFF, 4, 0, 10) |
| #define | [ULPSSI\_CS1\_HP10](#ad1e8bb7ce27179dfadac4836b9a26924)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(9, 1, 5, 0, 10, 4) |
| #define | [ULPSSI\_CS1\_ULP4](#abcb850de6adc5db558bb9cb8a45455a6)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(0xFF, 1, 0xFF, 4, 0, 4) |
| #define | [ULPSSI\_CS2\_HP12](#aa53895ddaa78b38c7ea5b35d6f00c78f)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(9, 1, 7, 0, 12, 6) |
| #define | [ULPSSI\_CS2\_HP25](#ac537683d973832982d538a2e3a705f7c)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(11, 1, 0, 1, 9, 6) |
| #define | [ULPSSI\_CS2\_ULP6](#a3ddbf1e40ddfb1844a7c486b3d47a8fe)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(0xFF, 1, 0xFF, 4, 0, 6) |
| #define | [ULPSSI\_DIN\_HP8](#a00b7649bb95375d2a8632938c1ab2fd8)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(9, 1, 3, 0, 8, 2) |
| #define | [ULPSSI\_DIN\_HP28](#a9d01d993af06027e11d1a2c2abd1505a)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(11, 1, 0, 1, 12, 9) |
| #define | [ULPSSI\_DIN\_HP47](#a6ffab07aba4ddfa977a8865230c35309)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(9, 1, 11, 2, 15, 9) |
| #define | [ULPSSI\_DIN\_ULP2](#a8a35f9ed548c01693de57b6647a55901)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(0xFF, 1, 0xFF, 4, 0, 2) |
| #define | [ULPSSI\_DIN\_ULP6](#a3737184b07cd6dfdef580a82b31ad13c)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(0xFF, 8, 0xFF, 4, 0, 6) |
| #define | [ULPSSI\_DIN\_ULP9](#a841bd6d9d7b267db55b85dbd63c29f19)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(0xFF, 1, 0xFF, 4, 0, 9) |
| #define | [ULPSSI\_DOUT\_HP7](#a7f72ea03a247002a88d22afa4d41f4eb)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(9, 1, 2, 0, 7, 1) |
| #define | [ULPSSI\_DOUT\_HP30](#ab90410cbd5d7feccc31c858dcea5ce24)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(11, 1, 0, 1, 14, 11) |
| #define | [ULPSSI\_DOUT\_HP49](#a5c0d9281a0eae7e3f71c7622f0fcb0ca)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(9, 1, 13, 3, 1, 11) |
| #define | [ULPSSI\_DOUT\_ULP1](#a7c49826415618d0edb0bf9960ab1390a)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(0xFF, 1, 0xFF, 4, 0, 1) |
| #define | [ULPSSI\_DOUT\_ULP5](#a3936c932181d9601015bfcd9ddbd9230)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(0xFF, 8, 0xFF, 4, 0, 5) |
| #define | [ULPSSI\_DOUT\_ULP11](#ae74ef587f76251d995250141665e0691)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(0xFF, 1, 0xFF, 4, 0, 11) |
| #define | [ULPUART\_CTS\_HP7](#a7be14c47047f63a0f72b9508fb45dcb8)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(9, 3, 2, 0, 7, 1) |
| #define | [ULPUART\_CTS\_HP11](#aa9a3840c4d145ad867c1e59cf988d74a)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(9, 3, 6, 0, 11, 5) |
| #define | [ULPUART\_CTS\_HP27](#a6fa2d64e1f638a6e0a7df29a4476da03)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(11, 3, 0, 1, 11, 8) |
| #define | [ULPUART\_CTS\_HP46](#a8ae6905ee86208cfc8910d8cff7423cf)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(9, 3, 10, 2, 14, 8) |
| #define | [ULPUART\_CTS\_ULP1](#acecb9492723712365609fe03429ecc62)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(0xFF, 3, 0xFF, 4, 0, 1) |
| #define | [ULPUART\_CTS\_ULP5](#a47991853f93de832cb85dba3dd51d689)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(0xFF, 3, 0xFF, 4, 0, 5) |
| #define | [ULPUART\_CTS\_ULP8](#ad87a42b5cac9d4e3e1539963c0a153ac)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(0xFF, 3, 0xFF, 4, 0, 8) |
| #define | [ULPUART\_RTS\_HP6](#a3aa724f39856848fe3616dc2c7e0f9d5)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(9, 3, 1, 0, 6, 0) |
| #define | [ULPUART\_RTS\_HP10](#ad25318e8c8da760aca964a06c8114f3e)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(9, 3, 5, 0, 10, 4) |
| #define | [ULPUART\_RTS\_HP29](#a45126e5a5d74c85e34beede737a6c266)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(11, 3, 0, 1, 13, 10) |
| #define | [ULPUART\_RTS\_HP48](#a0fd57249b5cdaa83d1a82d96f39bfcac)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(9, 3, 12, 3, 0, 10) |
| #define | [ULPUART\_RTS\_ULP0](#a6d637af94f43cbfcfd001b174d89504e)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(0xFF, 3, 0xFF, 4, 0, 0) |
| #define | [ULPUART\_RTS\_ULP4](#a905bfb63ed0825940db94f2d0e339cae)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(0xFF, 3, 0xFF, 4, 0, 4) |
| #define | [ULPUART\_RTS\_ULP10](#aafec5377fdddad88eaa5f33a616e932a)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(0xFF, 3, 0xFF, 4, 0, 10) |
| #define | [ULPUART\_RX\_HP8](#a7e24d72b3f26b6a64d1182b223a679a5)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(9, 3, 3, 0, 8, 2) |
| #define | [ULPUART\_RX\_HP12](#a95f0434e7aa29f3f3b8870a8f56df169)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(9, 3, 7, 0, 12, 6) |
| #define | [ULPUART\_RX\_HP25](#a17fa934bc15ff31389466f0906291c95)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(11, 3, 0, 1, 9, 6) |
| #define | [ULPUART\_RX\_HP28](#afde64cb335752ffd591ddeb40f2d24b0)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(11, 3, 0, 1, 12, 9) |
| #define | [ULPUART\_RX\_HP47](#a497302eeb072e2573948fd36b246824e)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(9, 3, 11, 2, 15, 9) |
| #define | [ULPUART\_RX\_ULP2](#a5c296e125433a81362d207042b30cb7e)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(0xFF, 3, 0xFF, 4, 0, 2) |
| #define | [ULPUART\_RX\_ULP6](#a1036c7686c6ae59e387bf0df9338d8f6)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(0xFF, 3, 0xFF, 4, 0, 6) |
| #define | [ULPUART\_RX\_ULP9](#a3b868b8418ed39e8251a6d5e06da25ec)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(0xFF, 3, 0xFF, 4, 0, 9) |
| #define | [ULPUART\_TX\_HP15](#af7d1211f086a8be91e95e88e1bcee555)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(9, 3, 8, 0, 15, 7) |
| #define | [ULPUART\_TX\_HP26](#a02c5645af20a73c856a0e7dcbf30e45a)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(11, 3, 0, 1, 10, 7) |
| #define | [ULPUART\_TX\_HP30](#ace2f51ab67c116751656f1421bac3db9)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(11, 3, 0, 1, 14, 11) |
| #define | [ULPUART\_TX\_HP49](#a8974ff95ea2efd59e1f2d16a7322f75c)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(9, 3, 13, 3, 1, 11) |
| #define | [ULPUART\_TX\_ULP7](#a306f5e9ad2e84cee1074067cd6bccb4f)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(0xFF, 3, 0xFF, 4, 0, 7) |
| #define | [ULPUART\_TX\_ULP11](#a11b4b4459ff2d94267bca669da7e17cc)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(0xFF, 3, 0xFF, 4, 0, 11) |
| #define | [UULP\_GPIO4\_ULP2](#a02c45c292ebe276e4f41101d7440480f)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(0xFF, 4, 0xFF, 4, 0, 2) |
| #define | [UULP\_TESTMODE0\_ULP7](#a003329462614c9ff939c451c28a011bc)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(0xFF, 11, 0xFF, 4, 0, 7) |
| #define | [UULP\_TESTMODE0\_ULP9](#aa927ee96be06692b7fecb88eec152357)   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(0xFF, 5, 0xFF, 4, 0, 9) |

## Macro Definition Documentation

## [◆ ](#a06a04fbcd9f9db43dd3b4c9be9ecc196)ADC\_TOPGPIO\_HP25

| #define ADC\_TOPGPIO\_HP25   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(14, 0xFF, 0, 1, 9, 0) |
| --- |

## [◆ ](#a1c85b141f986867590feab3e2971f83e)ADC\_TOPGPIO\_HP26

| #define ADC\_TOPGPIO\_HP26   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(14, 0xFF, 0, 1, 10, 0) |
| --- |

## [◆ ](#ab786befc793ba2dabbbc3c8abccdd81c)ADC\_TOPGPIO\_HP27

| #define ADC\_TOPGPIO\_HP27   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(14, 0xFF, 0, 1, 11, 0) |
| --- |

## [◆ ](#ac6f1ca16c8640f98a9d2eccafb282302)ADC\_TOPGPIO\_HP28

| #define ADC\_TOPGPIO\_HP28   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(14, 0xFF, 0, 1, 12, 0) |
| --- |

## [◆ ](#a919a3ea12132734ffbaa583eb814e70a)ADC\_TOPGPIO\_HP29

| #define ADC\_TOPGPIO\_HP29   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(14, 0xFF, 0, 1, 13, 0) |
| --- |

## [◆ ](#ac11f4dd52f4993a9ab70d16a50be47fa)ADC\_TOPGPIO\_HP30

| #define ADC\_TOPGPIO\_HP30   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(14, 0xFF, 0, 1, 14, 0) |
| --- |

## [◆ ](#a51b9722e0c1470e0692d913cd70ca33e)AGPIO\_ULP0

| #define AGPIO\_ULP0   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(0xFF, 7, 0xFF, 4, 0, 0) |
| --- |

## [◆ ](#a30b16a45f81323324e310d96777c6fd8)AGPIO\_ULP1

| #define AGPIO\_ULP1   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(0xFF, 7, 0xFF, 4, 0, 1) |
| --- |

## [◆ ](#a57855add105b9a5ac3df1600caf2d4bc)AGPIO\_ULP10

| #define AGPIO\_ULP10   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(0xFF, 7, 0xFF, 4, 0, 10) |
| --- |

## [◆ ](#a3e0ca1d417d8c455c275e5e67e071c6c)AGPIO\_ULP11

| #define AGPIO\_ULP11   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(0xFF, 7, 0xFF, 4, 0, 11) |
| --- |

## [◆ ](#a7189b132ac6420c926c8cf2eccab3c6b)AGPIO\_ULP2

| #define AGPIO\_ULP2   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(0xFF, 7, 0xFF, 4, 0, 2) |
| --- |

## [◆ ](#a0d43105668987a220c67393d4674515d)AGPIO\_ULP4

| #define AGPIO\_ULP4   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(0xFF, 7, 0xFF, 4, 0, 4) |
| --- |

## [◆ ](#a2a66cdafa849bf095ca1d6916001f441)AGPIO\_ULP5

| #define AGPIO\_ULP5   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(0xFF, 7, 0xFF, 4, 0, 5) |
| --- |

## [◆ ](#a60dfb206c49bc9005231c936e9393546)AGPIO\_ULP6

| #define AGPIO\_ULP6   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(0xFF, 7, 0xFF, 4, 0, 6) |
| --- |

## [◆ ](#a1ff255f96fa29e9a0c500967596ac57a)AGPIO\_ULP7

| #define AGPIO\_ULP7   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(0xFF, 7, 0xFF, 4, 0, 7) |
| --- |

## [◆ ](#a721b2b6550307530f7ab4068cc11631b)AGPIO\_ULP8

| #define AGPIO\_ULP8   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(0xFF, 7, 0xFF, 4, 0, 8) |
| --- |

## [◆ ](#a228d260414f49b06912a8694b31dc358)AGPIO\_ULP9

| #define AGPIO\_ULP9   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(0xFF, 7, 0xFF, 4, 0, 9) |
| --- |

## [◆ ](#ab03b635abc6f55d9824a6e0cf1a2c94e)AUXULP\_TRIG0\_HP11

| #define AUXULP\_TRIG0\_HP11   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(9, 5, 6, 0, 11, 5) |
| --- |

## [◆ ](#aad0ba7e32d1c8d4acbd6d2d1f4b288a0)AUXULP\_TRIG0\_HP30

| #define AUXULP\_TRIG0\_HP30   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(11, 5, 0, 1, 14, 11) |
| --- |

## [◆ ](#ae321eaa930b4bcdb847c6f0595e6f46f)AUXULP\_TRIG0\_HP49

| #define AUXULP\_TRIG0\_HP49   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(9, 5, 13, 3, 1, 11) |
| --- |

## [◆ ](#ab92c286c8db594d8f607ce3ef09657b4)AUXULP\_TRIG0\_ULP11

| #define AUXULP\_TRIG0\_ULP11   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(0xFF, 5, 0xFF, 4, 0, 11) |
| --- |

## [◆ ](#a945e911bffcedf2cd3e00b0394a990b1)AUXULP\_TRIG0\_ULP5

| #define AUXULP\_TRIG0\_ULP5   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(0xFF, 5, 0xFF, 4, 0, 5) |
| --- |

## [◆ ](#a090807259f65186a27e1327fbf599829)AUXULP\_TRIG0\_ULP6

| #define AUXULP\_TRIG0\_ULP6   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(0xFF, 10, 0xFF, 4, 0, 6) |
| --- |

## [◆ ](#adf749c359174226e90d8a2ba64b4983c)AUXULP\_TRIG1\_ULP4

| #define AUXULP\_TRIG1\_ULP4   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(0xFF, 5, 0xFF, 4, 0, 4) |
| --- |

## [◆ ](#a1d9a7c9bf69093de19cbdf10953e4c22)AUXULP\_TRIG1\_ULP7

| #define AUXULP\_TRIG1\_ULP7   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(0xFF, 10, 0xFF, 4, 0, 7) |
| --- |

## [◆ ](#a835c36708762cd86818ce60b25384eb7)CLK\_I2SPLL\_HP27

| #define CLK\_I2SPLL\_HP27   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(12, 0xFF, 0, 1, 11, 0) |
| --- |

## [◆ ](#aa4282adbc2f3da0006bde8511465bbff)CLK\_I2SPLL\_HP48

| #define CLK\_I2SPLL\_HP48   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(10, 0xFF, 12, 3, 0, 0) |
| --- |

## [◆ ](#a000ce8a22cf34cb0bfbb6ae2e25e55bb)CLK\_I2SPLL\_HP54

| #define CLK\_I2SPLL\_HP54   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(10, 0xFF, 18, 3, 6, 0) |
| --- |

## [◆ ](#a5d5b9c68af29a74c67fe4e002426d35c)CLK\_INTFPLL\_HP26

| #define CLK\_INTFPLL\_HP26   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(12, 0xFF, 0, 1, 10, 0) |
| --- |

## [◆ ](#a7009a3f01b97860c58b29d0fc96f0df5)CLK\_INTFPLL\_HP47

| #define CLK\_INTFPLL\_HP47   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(10, 0xFF, 11, 2, 15, 0) |
| --- |

## [◆ ](#a137db7b4fba3de386340ece21b67b3a2)CLK\_INTFPLL\_HP53

| #define CLK\_INTFPLL\_HP53   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(10, 0xFF, 17, 3, 5, 0) |
| --- |

## [◆ ](#a679d7001a0e3864ccf0a879b5c4ccfc8)CLK\_MCUOUT\_HP11

| #define CLK\_MCUOUT\_HP11   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(12, 0xFF, 6, 0, 11, 0) |
| --- |

## [◆ ](#a09924c650f824cca05e8b341ed9294ad)CLK\_MEMSREF\_HP50

| #define CLK\_MEMSREF\_HP50   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(10, 0xFF, 14, 3, 2, 0) |
| --- |

## [◆ ](#afa68d89e38d316a3e729c371d8297bae)CLK\_MEMSREF\_HP56

| #define CLK\_MEMSREF\_HP56   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(10, 0xFF, 20, 3, 8, 0) |
| --- |

## [◆ ](#aa413920e1935cc7bfb36235fa4055922)CLK\_OUT\_HP12

| #define CLK\_OUT\_HP12   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(8, 0xFF, 7, 0, 12, 0) |
| --- |

## [◆ ](#a32ffde4590651355db3a7411ed50d270)CLK\_OUT\_HP15

| #define CLK\_OUT\_HP15   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(8, 0xFF, 8, 0, 15, 0) |
| --- |

## [◆ ](#a880777fe8275592e91088d050512bff3)CLK\_PLLTESTMODE\_HP51

| #define CLK\_PLLTESTMODE\_HP51   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(10, 0xFF, 15, 3, 3, 0) |
| --- |

## [◆ ](#a92da5349a6b9ba8ea91ba8402bd685b2)CLK\_SOCPLL\_HP25

| #define CLK\_SOCPLL\_HP25   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(12, 0xFF, 0, 1, 9, 0) |
| --- |

## [◆ ](#ad715b44d79cab97ac67f4ee4d7e3fd61)CLK\_SOCPLL\_HP46

| #define CLK\_SOCPLL\_HP46   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(10, 0xFF, 10, 2, 14, 0) |
| --- |

## [◆ ](#ab0bda6530a625116653efc6ccdaf066e)CLK\_SOCPLL\_HP52

| #define CLK\_SOCPLL\_HP52   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(10, 0xFF, 16, 3, 4, 0) |
| --- |

## [◆ ](#a898d24c287840df4a1d9b1f1d5bee3ca)CLK\_XTALONIN\_HP28

| #define CLK\_XTALONIN\_HP28   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(12, 0xFF, 0, 1, 12, 0) |
| --- |

## [◆ ](#a5b9fea82548ee54a0a72cd10cad57b47)CLK\_XTALONIN\_HP57

| #define CLK\_XTALONIN\_HP57   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(10, 0xFF, 21, 3, 9, 0) |
| --- |

## [◆ ](#a67c405487bacc252498d58f92dd4e7f2)COMP1\_OUT\_HP28

| #define COMP1\_OUT\_HP28   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(11, 5, 0, 1, 12, 9) |
| --- |

## [◆ ](#ad229716eda10b53eb40628b24bb84329)COMP1\_OUT\_HP47

| #define COMP1\_OUT\_HP47   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(9, 5, 11, 2, 15, 9) |
| --- |

## [◆ ](#aa4e79dc6178b13147dbeb10aaa6fbc6d)COMP1\_OUT\_HP8

| #define COMP1\_OUT\_HP8   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(9, 5, 3, 0, 8, 2) |
| --- |

## [◆ ](#a5865a449e4957f10e35208b3a8a1e186)COMP1\_OUT\_ULP2

| #define COMP1\_OUT\_ULP2   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(0xFF, 5, 0xFF, 4, 0, 2) |
| --- |

## [◆ ](#a61a3d2a33b017f9b509e502fb14b5ac1)COMP1\_OUT\_ULP6

| #define COMP1\_OUT\_ULP6   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(0xFF, 9, 0xFF, 4, 0, 6) |
| --- |

## [◆ ](#a3de5ca3d0d7078a34cc53b5c5028d7c3)COMP2\_OUT\_ULP7

| #define COMP2\_OUT\_ULP7   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(0xFF, 9, 0xFF, 4, 0, 7) |
| --- |

## [◆ ](#af45db40d737c46516891fc77bfd6991b)GSPI\_CLK\_HP25

| #define GSPI\_CLK\_HP25   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(4, 0xFF, 0, 1, 9, 0) |
| --- |

## [◆ ](#a4adfba6b40f466fd220c52835338ff8f)GSPI\_CLK\_HP46

| #define GSPI\_CLK\_HP46   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(4, 0xFF, 10, 2, 14, 0) |
| --- |

## [◆ ](#ab4e0b64c913aa9d1c5f9b8d7f7c564d1)GSPI\_CLK\_HP52

| #define GSPI\_CLK\_HP52   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(4, 0xFF, 16, 3, 4, 0) |
| --- |

## [◆ ](#a0d322c35cde263da2607b11c8dce74f1)GSPI\_CLK\_HP8

| #define GSPI\_CLK\_HP8   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(4, 0xFF, 3, 0, 8, 0) |
| --- |

## [◆ ](#a120041f6e17a7263e01a6cf9dbf97f55)GSPI\_CS0\_HP28

| #define GSPI\_CS0\_HP28   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(4, 0xFF, 0, 1, 12, 0) |
| --- |

## [◆ ](#a9a136b1b51489fed94ebc601d1bce509)GSPI\_CS0\_HP49

| #define GSPI\_CS0\_HP49   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(4, 0xFF, 13, 3, 1, 0) |
| --- |

## [◆ ](#aad59278f16c573afe6d988fec3e789ae)GSPI\_CS0\_HP53

| #define GSPI\_CS0\_HP53   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(4, 0xFF, 17, 3, 5, 0) |
| --- |

## [◆ ](#ada868d60b39f9ef5d58e3297b9569ebe)GSPI\_CS0\_HP9

| #define GSPI\_CS0\_HP9   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(4, 0xFF, 4, 0, 9, 0) |
| --- |

## [◆ ](#a5fa623bbd9d1a30eec7af32587dd5ba1)GSPI\_CS1\_HP10

| #define GSPI\_CS1\_HP10   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(4, 0xFF, 5, 0, 10, 0) |
| --- |

## [◆ ](#a5d6fc805d3e94783eb3eead3e46d3eb5)GSPI\_CS1\_HP29

| #define GSPI\_CS1\_HP29   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(4, 0xFF, 0, 1, 13, 0) |
| --- |

## [◆ ](#a9fd3baadefec26d4e6532b3d22d6bfc6)GSPI\_CS1\_HP50

| #define GSPI\_CS1\_HP50   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(4, 0xFF, 14, 3, 2, 0) |
| --- |

## [◆ ](#a9607f0a50a592087747f02d1dc6fe61e)GSPI\_CS1\_HP54

| #define GSPI\_CS1\_HP54   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(4, 0xFF, 18, 3, 6, 0) |
| --- |

## [◆ ](#ad42cd6f9d902d0667f5a71ad2c7ead9a)GSPI\_CS2\_HP15

| #define GSPI\_CS2\_HP15   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(4, 0xFF, 8, 0, 15, 0) |
| --- |

## [◆ ](#accbdbea1a397053ccc6a58d53ec8493c)GSPI\_CS2\_HP30

| #define GSPI\_CS2\_HP30   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(4, 0xFF, 0, 1, 14, 0) |
| --- |

## [◆ ](#af7ff281165326d035233deb890fb9cb2)GSPI\_CS2\_HP51

| #define GSPI\_CS2\_HP51   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(4, 0xFF, 15, 3, 3, 0) |
| --- |

## [◆ ](#a56ea3052bad2710a04055aa1306ef827)GSPI\_CS2\_HP55

| #define GSPI\_CS2\_HP55   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(4, 0xFF, 19, 3, 7, 0) |
| --- |

## [◆ ](#a39e87f6b1067af1fd6eda77e0877c7dc)GSPI\_MISO\_HP11

| #define GSPI\_MISO\_HP11   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(4, 0xFF, 6, 0, 11, 0) |
| --- |

## [◆ ](#ab9d92646ac5bfbd06eeab8727ce9f69c)GSPI\_MISO\_HP26

| #define GSPI\_MISO\_HP26   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(4, 0xFF, 0, 1, 10, 0) |
| --- |

## [◆ ](#ace8e09dd531dab443c8e23567940c0c7)GSPI\_MISO\_HP47

| #define GSPI\_MISO\_HP47   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(4, 0xFF, 11, 2, 15, 0) |
| --- |

## [◆ ](#ad922fdd48ef757e7ed84dc5ba0223b96)GSPI\_MISO\_HP56

| #define GSPI\_MISO\_HP56   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(4, 0xFF, 20, 3, 8, 0) |
| --- |

## [◆ ](#a4e70d4d9f4da18808231e1626a81aca4)GSPI\_MOSI\_HP12

| #define GSPI\_MOSI\_HP12   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(4, 0xFF, 7, 0, 12, 0) |
| --- |

## [◆ ](#a2ca232ad550d21add9adc2962a844b71)GSPI\_MOSI\_HP27

| #define GSPI\_MOSI\_HP27   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(4, 0xFF, 0, 1, 11, 0) |
| --- |

## [◆ ](#ad7925ac094c67ed0be2418d434869ac3)GSPI\_MOSI\_HP48

| #define GSPI\_MOSI\_HP48   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(4, 0xFF, 12, 3, 0, 0) |
| --- |

## [◆ ](#a80818466e12929450e71aec02cdd4c7b)GSPI\_MOSI\_HP57

| #define GSPI\_MOSI\_HP57   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(4, 0xFF, 21, 3, 9, 0) |
| --- |

## [◆ ](#a10573e8f0c7675c91a907c0f5e80a9cc)GSPI\_MOSI\_HP6

| #define GSPI\_MOSI\_HP6   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(12, 0xFF, 1, 0, 6, 0) |
| --- |

## [◆ ](#ac8c62e3f52c598d1de82735a0809b0ad)I2C0\_SCL\_HP32

| #define I2C0\_SCL\_HP32   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(11, 0xFF, 9, 2, 0, 0) |
| --- |

## [◆ ](#a2ef351b47d12918bb4cea74c0e473db1)I2C0\_SCL\_HP7

| #define I2C0\_SCL\_HP7   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(4, 0xFF, 2, 0, 7, 0) |
| --- |

## [◆ ](#a820c81dfce3dff2287efa78305812b7f)I2C0\_SCL\_ULP1

| #define I2C0\_SCL\_ULP1   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(4, 6, 23, 4, 1, 1) |
| --- |

## [◆ ](#a10e1bb6b59bfb1c4ca1932f9a4be1448)I2C0\_SCL\_ULP11

| #define I2C0\_SCL\_ULP11   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(4, 6, 33, 4, 11, 11) |
| --- |

## [◆ ](#a480ff4a4f89b88de9c46001c7ad52aed)I2C0\_SCL\_ULP2

| #define I2C0\_SCL\_ULP2   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(4, 6, 24, 4, 2, 2) |
| --- |

## [◆ ](#a9334871e0ff13605bf9fe104a8aa75f3)I2C0\_SDA\_HP31

| #define I2C0\_SDA\_HP31   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(11, 0xFF, 9, 1, 15, 0) |
| --- |

## [◆ ](#a01c68c9f6c64829f15e5fe3e4fa4e7e7)I2C0\_SDA\_HP6

| #define I2C0\_SDA\_HP6   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(4, 0xFF, 1, 0, 6, 0) |
| --- |

## [◆ ](#a54e93e8958d5eb99c63ce1ad2cf17e75)I2C0\_SDA\_ULP0

| #define I2C0\_SDA\_ULP0   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(4, 6, 22, 4, 0, 0) |
| --- |

## [◆ ](#a26710ae6de0a217c2d3af4cb7cc14b28)I2C0\_SDA\_ULP10

| #define I2C0\_SDA\_ULP10   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(4, 6, 32, 4, 10, 10) |
| --- |

## [◆ ](#a3a53a6594da3d36f4c186864275cdb47)I2C0\_SDA\_ULP3

| #define I2C0\_SDA\_ULP3   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(4, 6, 25, 4, 3, 3) |
| --- |

## [◆ ](#a24827fb9fdaa10b780a06c222062e522)I2C1\_SCL\_HP29

| #define I2C1\_SCL\_HP29   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(5, 0xFF, 0, 1, 13, 0) |
| --- |

## [◆ ](#a936da856e3e3d0a8a67957c3e9a25519)I2C1\_SCL\_HP33

| #define I2C1\_SCL\_HP33   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(11, 0xFF, 9, 2, 1, 0) |
| --- |

## [◆ ](#afe20556071663d815232b98293555fb7)I2C1\_SCL\_HP50

| #define I2C1\_SCL\_HP50   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(5, 0xFF, 14, 3, 2, 0) |
| --- |

## [◆ ](#afdb3b18d7540906aca0a17187ce185b0)I2C1\_SCL\_HP54

| #define I2C1\_SCL\_HP54   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(5, 0xFF, 18, 3, 6, 0) |
| --- |

## [◆ ](#aa5ba13c0b275c1d1fb28aed3fcd26f6a)I2C1\_SCL\_HP6

| #define I2C1\_SCL\_HP6   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(5, 0xFF, 1, 0, 6, 0) |
| --- |

## [◆ ](#aa79263584dd8d9ccd4ae7564cbb50fd7)I2C1\_SCL\_ULP0

| #define I2C1\_SCL\_ULP0   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(5, 6, 22, 4, 0, 0) |
| --- |

## [◆ ](#a1f40c8c4305f357477f61f2bee4177aa)I2C1\_SCL\_ULP2

| #define I2C1\_SCL\_ULP2   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(5, 6, 24, 4, 2, 2) |
| --- |

## [◆ ](#a34ac7a645ee7c80f1d291348bdaddb1b)I2C1\_SCL\_ULP6

| #define I2C1\_SCL\_ULP6   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(5, 6, 28, 4, 6, 6) |
| --- |

## [◆ ](#a5d4d1af9ec0fab65e197d0f4ef9c4fc0)I2C1\_SDA\_HP30

| #define I2C1\_SDA\_HP30   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(5, 0xFF, 0, 1, 14, 0) |
| --- |

## [◆ ](#aab52c1cbc805809cfe35199fb204867c)I2C1\_SDA\_HP34

| #define I2C1\_SDA\_HP34   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(11, 0xFF, 9, 2, 2, 0) |
| --- |

## [◆ ](#a8889ee6d6d096a1b6790a71bb3f7db84)I2C1\_SDA\_HP51

| #define I2C1\_SDA\_HP51   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(5, 0xFF, 15, 3, 3, 0) |
| --- |

## [◆ ](#a1aad71707a9c1adb14525b1809a97b31)I2C1\_SDA\_HP55

| #define I2C1\_SDA\_HP55   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(5, 0xFF, 19, 3, 7, 0) |
| --- |

## [◆ ](#a7fdc374bc827cd67f954b638fb6ab03b)I2C1\_SDA\_HP7

| #define I2C1\_SDA\_HP7   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(5, 0xFF, 2, 0, 7, 0) |
| --- |

## [◆ ](#adc989b20626192997d54961dd616b3b2)I2C1\_SDA\_ULP1

| #define I2C1\_SDA\_ULP1   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(5, 6, 23, 4, 1, 1) |
| --- |

## [◆ ](#af66e09c1a67eeae142148952ffc620cb)I2C1\_SDA\_ULP3

| #define I2C1\_SDA\_ULP3   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(5, 6, 25, 4, 3, 3) |
| --- |

## [◆ ](#a187fb1dd9e7f233059c7602205112d62)I2C1\_SDA\_ULP7

| #define I2C1\_SDA\_ULP7   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(5, 6, 29, 4, 7, 7) |
| --- |

## [◆ ](#a5150fe8f89fdf656a051ba412f7ba9c3)I2S0\_CLK\_HP25

| #define I2S0\_CLK\_HP25   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(7, 0xFF, 0, 1, 9, 0) |
| --- |

## [◆ ](#a0048da9c1376b56df1479b4689fe9de2)I2S0\_CLK\_HP46

| #define I2S0\_CLK\_HP46   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(7, 0xFF, 10, 2, 14, 0) |
| --- |

## [◆ ](#aca6c330be2dc8f7b16abfa4b319cba5c)I2S0\_CLK\_HP52

| #define I2S0\_CLK\_HP52   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(7, 0xFF, 16, 3, 4, 0) |
| --- |

## [◆ ](#a7359e2ca7813b5abebd030d795e78706)I2S0\_CLK\_HP8

| #define I2S0\_CLK\_HP8   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(7, 0xFF, 3, 0, 8, 0) |
| --- |

## [◆ ](#a303d85325bbcc79992cfa1fda5cfae07)I2S0\_DIN0\_HP10

| #define I2S0\_DIN0\_HP10   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(7, 0xFF, 5, 0, 10, 0) |
| --- |

## [◆ ](#a2ac13eb02c917e2ca6a184bb3e9e38db)I2S0\_DIN0\_HP27

| #define I2S0\_DIN0\_HP27   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(7, 0xFF, 0, 1, 11, 0) |
| --- |

## [◆ ](#afb246a50f57470d46bb8a33a90be05ad)I2S0\_DIN0\_HP48

| #define I2S0\_DIN0\_HP48   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(7, 0xFF, 12, 3, 0, 0) |
| --- |

## [◆ ](#ac87ec8ad8ec8321d356d7678793851ab)I2S0\_DIN0\_HP56

| #define I2S0\_DIN0\_HP56   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(7, 0xFF, 20, 3, 8, 0) |
| --- |

## [◆ ](#a8e6c2584e4f4c323fba1ddaf7c4271e6)I2S0\_DIN1\_HP29

| #define I2S0\_DIN1\_HP29   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(7, 0xFF, 0, 1, 13, 0) |
| --- |

## [◆ ](#a36408b9361281baa4b6df09e94da3d04)I2S0\_DIN1\_HP50

| #define I2S0\_DIN1\_HP50   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(7, 0xFF, 14, 3, 2, 0) |
| --- |

## [◆ ](#ad81fc920d9067bf3beaa1b42b1a819a6)I2S0\_DIN1\_HP54

| #define I2S0\_DIN1\_HP54   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(7, 0xFF, 18, 3, 6, 0) |
| --- |

## [◆ ](#a019d02d00ed9a9d254f3350e70577214)I2S0\_DIN1\_HP6

| #define I2S0\_DIN1\_HP6   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(7, 0xFF, 1, 0, 6, 0) |
| --- |

## [◆ ](#aca53f49c7d835b65bcd2aefc344abe24)I2S0\_DOUT0\_HP11

| #define I2S0\_DOUT0\_HP11   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(7, 0xFF, 6, 0, 11, 0) |
| --- |

## [◆ ](#a1f6afb833961353d943a469748a99bb3)I2S0\_DOUT0\_HP28

| #define I2S0\_DOUT0\_HP28   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(7, 0xFF, 0, 1, 12, 0) |
| --- |

## [◆ ](#acac20029d1653abd303310ab5cfec88b)I2S0\_DOUT0\_HP49

| #define I2S0\_DOUT0\_HP49   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(7, 0xFF, 13, 3, 1, 0) |
| --- |

## [◆ ](#aacd5f462222363c3ee0641ceaad3c9ac)I2S0\_DOUT0\_HP57

| #define I2S0\_DOUT0\_HP57   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(7, 0xFF, 21, 3, 9, 0) |
| --- |

## [◆ ](#a9b538a9b237871d89be0755a999a14aa)I2S0\_DOUT1\_HP29

| #define I2S0\_DOUT1\_HP29   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(7, 0xFF, 0, 1, 14, 0) |
| --- |

## [◆ ](#ab6e059e2cb256557e26dedade8ce2aed)I2S0\_DOUT1\_HP51

| #define I2S0\_DOUT1\_HP51   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(7, 0xFF, 15, 3, 3, 0) |
| --- |

## [◆ ](#abfe82c91355f572a5c4dc7dbb2e2f510)I2S0\_DOUT1\_HP55

| #define I2S0\_DOUT1\_HP55   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(7, 0xFF, 19, 3, 7, 0) |
| --- |

## [◆ ](#a9a165d304f050db860d42944f4288ec0)I2S0\_DOUT1\_HP7

| #define I2S0\_DOUT1\_HP7   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(7, 0xFF, 2, 0, 7, 0) |
| --- |

## [◆ ](#a614bbb3cbb8250a3f230806139dba0c9)I2S0\_WS\_HP26

| #define I2S0\_WS\_HP26   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(7, 0xFF, 0, 1, 10, 0) |
| --- |

## [◆ ](#a1b9f3a9dfbd36791be898036417e48bf)I2S0\_WS\_HP47

| #define I2S0\_WS\_HP47   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(7, 0xFF, 11, 2, 15, 0) |
| --- |

## [◆ ](#a63944069b8a3f30dc669f01dcc8c088c)I2S0\_WS\_HP53

| #define I2S0\_WS\_HP53   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(7, 0xFF, 17, 3, 5, 0) |
| --- |

## [◆ ](#a72f19d1ace618e6c2bae69c6a3f4c5f8)I2S0\_WS\_HP9

| #define I2S0\_WS\_HP9   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(7, 0xFF, 4, 0, 9, 0) |
| --- |

## [◆ ](#a50e3d3f0baf17368823af4bf6a21dfb7)IR\_INPUT\_HP15

| #define IR\_INPUT\_HP15   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(9, 1, 8, 0, 15, 7) |
| --- |

## [◆ ](#acef80a4a997f5d5231e3f60856b864e1)IR\_INPUT\_HP26

| #define IR\_INPUT\_HP26   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(11, 1, 0, 1, 10, 7) |
| --- |

## [◆ ](#a5e4fc91a184b54b490bb615fdf3a25ab)IR\_INPUT\_HP29

| #define IR\_INPUT\_HP29   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(11, 4, 0, 1, 13, 10) |
| --- |

## [◆ ](#ac0035f0f87cbb64a9e0dbbadc61388e4)IR\_INPUT\_HP48

| #define IR\_INPUT\_HP48   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(9, 4, 12, 3, 0, 10) |
| --- |

## [◆ ](#a4c3793bc7cc985cf1f80aef136d18ce2)IR\_INPUT\_ULP10

| #define IR\_INPUT\_ULP10   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(0xFF, 4, 0xFF, 4, 0, 10) |
| --- |

## [◆ ](#a0d995f35796fc445efe7ebee649bdf2f)IR\_INPUT\_ULP4

| #define IR\_INPUT\_ULP4   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(0xFF, 10, 0xFF, 4, 0, 4) |
| --- |

## [◆ ](#aadd97a3fa547212bd510340b3ab05c2d)IR\_INPUT\_ULP7

| #define IR\_INPUT\_ULP7   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(0xFF, 1, 0xFF, 4, 0, 7) |
| --- |

## [◆ ](#a2c041f872981f73b54ccf7af03aa8a36)IR\_OUTPUT\_HP11

| #define IR\_OUTPUT\_HP11   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(9, 1, 6, 0, 11, 5) |
| --- |

## [◆ ](#adb645e594a5654f35cbd3e852445e19b)IR\_OUTPUT\_ULP5

| #define IR\_OUTPUT\_ULP5   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(0xFF, 1, 0xFF, 4, 0, 5) |
| --- |

## [◆ ](#a87863eae390ce502e6c84ce7d1110874)PMU\_TEST1\_HP29

| #define PMU\_TEST1\_HP29   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(8, 0xFF, 0, 1, 13, 0) |
| --- |

## [◆ ](#a01e9261c0bd8327120ae6da5686a6d3a)PMU\_TEST1\_HP30

| #define PMU\_TEST1\_HP30   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(12, 0xFF, 0, 1, 14, 0) |
| --- |

## [◆ ](#a29207f055fc19e97082391195ef8cf78)PMU\_TEST1\_HP6

| #define PMU\_TEST1\_HP6   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(8, 0xFF, 1, 0, 6, 0) |
| --- |

## [◆ ](#a4055f713ecf4e2f57c49c57321fdff99)PMU\_TEST1\_ULP0

| #define PMU\_TEST1\_ULP0   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(13, 6, 22, 4, 0, 0) |
| --- |

## [◆ ](#a4cee250941565f3e3eb36b6d0a4e3364)PMU\_TEST1\_ULP10

| #define PMU\_TEST1\_ULP10   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(10, 6, 32, 4, 10, 10) |
| --- |

## [◆ ](#a60de9f9f3085bee8341e118462a7fdcf)PMU\_TEST1\_ULP2

| #define PMU\_TEST1\_ULP2   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(10, 6, 24, 4, 2, 2) |
| --- |

## [◆ ](#ae687c8d547e498569a8b23f419216262)PMU\_TEST1\_ULP6

| #define PMU\_TEST1\_ULP6   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(12, 6, 28, 4, 6, 6) |
| --- |

## [◆ ](#a49436320a6c491ae61450c6f71beec48)PMU\_TEST2\_HP30

| #define PMU\_TEST2\_HP30   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(8, 0xFF, 0, 1, 14, 0) |
| --- |

## [◆ ](#a928e861887b2162d1f000910d6454d53)PMU\_TEST2\_HP7

| #define PMU\_TEST2\_HP7   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(8, 0xFF, 2, 0, 7, 0) |
| --- |

## [◆ ](#ad3cdee5e821dc5b3c68e45ec4b49bfbe)PMU\_TEST2\_ULP1

| #define PMU\_TEST2\_ULP1   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(13, 6, 23, 4, 1, 1) |
| --- |

## [◆ ](#a810fcca28118ef6dff963923b9af34d9)PMU\_TEST2\_ULP11

| #define PMU\_TEST2\_ULP11   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(10, 6, 33, 4, 11, 11) |
| --- |

## [◆ ](#a9eae278334a605347f6e95e9250cc7e7)PMU\_TEST2\_ULP3

| #define PMU\_TEST2\_ULP3   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(10, 6, 25, 4, 3, 3) |
| --- |

## [◆ ](#a0510f2e9687d07fe386be8718198990c)PMU\_TEST2\_ULP7

| #define PMU\_TEST2\_ULP7   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(12, 6, 29, 4, 7, 7) |
| --- |

## [◆ ](#a676931253894b60c9d0f60a3c9a45380)PSRAM\_CLK\_HP46

| #define PSRAM\_CLK\_HP46   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(11, 0xFF, 10, 2, 14, 0) |
| --- |

## [◆ ](#a7a8e755805d8aef6a1c1202297527ceb)PSRAM\_CLK\_HP52

| #define PSRAM\_CLK\_HP52   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(12, 0xFF, 16, 3, 4, 0) |
| --- |

## [◆ ](#aa717c6eebeb0b80e410f405464a0e23a)PSRAM\_CSN0\_HP49

| #define PSRAM\_CSN0\_HP49   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(11, 0xFF, 13, 3, 1, 0) |
| --- |

## [◆ ](#a1f0492fd0544bf8c1d01a534ee8b09dc)PSRAM\_CSN0\_HP55

| #define PSRAM\_CSN0\_HP55   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(12, 0xFF, 19, 3, 7, 0) |
| --- |

## [◆ ](#a5160d8e3311dc7e81fc88035e30b1298)PSRAM\_CSN1\_HP53

| #define PSRAM\_CSN1\_HP53   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(11, 0xFF, 17, 3, 5, 0) |
| --- |

## [◆ ](#a8505eee03f6dc307947fe9bba9cc868f)PSRAM\_D0\_HP47

| #define PSRAM\_D0\_HP47   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(11, 0xFF, 11, 2, 15, 0) |
| --- |

## [◆ ](#a5d2e115dab81d01f2059f108ef43df66)PSRAM\_D0\_HP53

| #define PSRAM\_D0\_HP53   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(12, 0xFF, 17, 3, 5, 0) |
| --- |

## [◆ ](#ae039ebfbbcb4f8d9c2941fad9cf21c25)PSRAM\_D1\_HP48

| #define PSRAM\_D1\_HP48   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(11, 0xFF, 12, 3, 0, 0) |
| --- |

## [◆ ](#a660ebada1169b4d19a0876b985e04a06)PSRAM\_D1\_HP54

| #define PSRAM\_D1\_HP54   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(12, 0xFF, 18, 3, 6, 0) |
| --- |

## [◆ ](#ab5bee0e001079fbd5fb0d974942aa598)PSRAM\_D2\_HP50

| #define PSRAM\_D2\_HP50   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(11, 0xFF, 14, 3, 2, 0) |
| --- |

## [◆ ](#acaed40bf53fd610ef38615a15cc24774)PSRAM\_D2\_HP56

| #define PSRAM\_D2\_HP56   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(12, 0xFF, 20, 3, 8, 0) |
| --- |

## [◆ ](#a19bf5beb8bca44b470e155431c0244a7)PSRAM\_D3\_HP51

| #define PSRAM\_D3\_HP51   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(11, 0xFF, 15, 3, 3, 0) |
| --- |

## [◆ ](#a2630b64edaffea76cf3a071d31494c00)PSRAM\_D3\_HP57

| #define PSRAM\_D3\_HP57   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(12, 0xFF, 21, 3, 9, 0) |
| --- |

## [◆ ](#ae3d2d17a5bd7b4c09c17cefe9febce73)PSRAM\_D4\_HP54

| #define PSRAM\_D4\_HP54   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(11, 0xFF, 18, 3, 6, 0) |
| --- |

## [◆ ](#a1ca55c42f77714d9c1088b200dc9dc8f)PSRAM\_D5\_HP55

| #define PSRAM\_D5\_HP55   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(11, 0xFF, 19, 3, 7, 0) |
| --- |

## [◆ ](#a9cb3582c88b3d07af732ebdcb239ba7b)PSRAM\_D6\_HP56

| #define PSRAM\_D6\_HP56   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(11, 0xFF, 20, 3, 8, 0) |
| --- |

## [◆ ](#a9e255793e353deb52e77a03359580322)PSRAM\_D7\_HP57

| #define PSRAM\_D7\_HP57   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(11, 0xFF, 21, 3, 9, 0) |
| --- |

## [◆ ](#ae04b42ec4c9f7b009a5a06a3ec01b35b)PWM\_0H\_HP7

| #define PWM\_0H\_HP7   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(10, 0xFF, 2, 0, 7, 0) |
| --- |

## [◆ ](#a0fd1688f5f60e0a874ce283a18713e7a)PWM\_0H\_ULP1

| #define PWM\_0H\_ULP1   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(12, 6, 23, 4, 1, 1) |
| --- |

## [◆ ](#a38fdb4b305f7ae6afb490118d52ef9bc)PWM\_0L\_HP6

| #define PWM\_0L\_HP6   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(10, 0xFF, 1, 0, 6, 0) |
| --- |

## [◆ ](#aa94e0a3dce4a99d76a019a0bf168e004)PWM\_0L\_ULP0

| #define PWM\_0L\_ULP0   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(12, 6, 22, 4, 0, 0) |
| --- |

## [◆ ](#acde3e8d6e27699ac4e8637813c6db6c9)PWM\_1H\_HP9

| #define PWM\_1H\_HP9   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(10, 0xFF, 4, 0, 9, 0) |
| --- |

## [◆ ](#ad11994d9f6d4ee1aecc042f61f720b42)PWM\_1H\_ULP3

| #define PWM\_1H\_ULP3   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(8, 6, 25, 4, 3, 3) |
| --- |

## [◆ ](#aeb72ce214bbeac3fea2296177e436cf0)PWM\_1H\_ULP5

| #define PWM\_1H\_ULP5   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(12, 6, 27, 4, 5, 5) |
| --- |

## [◆ ](#ae5b9d0282a760965899a0c163f58423c)PWM\_1L\_HP8

| #define PWM\_1L\_HP8   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(10, 0xFF, 3, 0, 8, 0) |
| --- |

## [◆ ](#a9e79d0a4b569d73d5ee7f65c1e2f20fc)PWM\_1L\_ULP2

| #define PWM\_1L\_ULP2   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(8, 6, 24, 4, 2, 2) |
| --- |

## [◆ ](#ab07ed6a6db4d9a7bdcb79d9d08635055)PWM\_1L\_ULP4

| #define PWM\_1L\_ULP4   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(12, 6, 26, 4, 4, 4) |
| --- |

## [◆ ](#a840701d4644973e31b0c49caa1fb52ce)PWM\_2H\_HP11

| #define PWM\_2H\_HP11   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(10, 0xFF, 6, 0, 11, 0) |
| --- |

## [◆ ](#abf08c72c301bfd555f41e34b99f2076e)PWM\_2H\_ULP5

| #define PWM\_2H\_ULP5   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(8, 6, 27, 4, 5, 5) |
| --- |

## [◆ ](#a7c60a35ecb5f5dc6448a96b3e3c89baf)PWM\_2L\_HP10

| #define PWM\_2L\_HP10   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(10, 0xFF, 5, 0, 10, 0) |
| --- |

## [◆ ](#ac8708b22008c4408a38456f7b8258328)PWM\_2L\_ULP4

| #define PWM\_2L\_ULP4   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(8, 6, 26, 4, 4, 4) |
| --- |

## [◆ ](#a507ec5bf9c637916ca37dee6de1d1a96)PWM\_3H\_HP15

| #define PWM\_3H\_HP15   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(10, 0xFF, 8, 0, 15, 0) |
| --- |

## [◆ ](#aea69719dd1cfa3a94f9f3a30459b51ed)PWM\_3H\_ULP7

| #define PWM\_3H\_ULP7   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(8, 6, 29, 4, 7, 7) |
| --- |

## [◆ ](#ae8d79d461423e0353022eab80c3025c8)PWM\_3L\_HP12

| #define PWM\_3L\_HP12   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(10, 0xFF, 7, 0, 12, 0) |
| --- |

## [◆ ](#ac6590ab64265b8c3bad3d30da7620604)PWM\_3L\_ULP6

| #define PWM\_3L\_ULP6   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(8, 6, 28, 4, 6, 6) |
| --- |

## [◆ ](#a4508139ab59dee416bd0aa7a53f2e2d5)PWM\_EXTTRIG0\_HP27

| #define PWM\_EXTTRIG0\_HP27   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(10, 0xFF, 0, 1, 11, 0) |
| --- |

## [◆ ](#a92c8c16ef38b80853b297d31a6dd4964)PWM\_EXTTRIG0\_HP51

| #define PWM\_EXTTRIG0\_HP51   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(8, 0xFF, 15, 3, 3, 0) |
| --- |

## [◆ ](#ac991e3bbd300bb3fb9b27a1d8d7fc5f2)PWM\_EXTTRIG0\_ULP11

| #define PWM\_EXTTRIG0\_ULP11   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(8, 6, 33, 4, 11, 11) |
| --- |

## [◆ ](#a65e5a78cc5cc390a802818a4f19ae8d4)PWM\_EXTTRIG0\_ULP6

| #define PWM\_EXTTRIG0\_ULP6   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(10, 6, 28, 4, 6, 6) |
| --- |

## [◆ ](#a0d191c0b60c2b836e3856a0e5c434649)PWM\_EXTTRIG1\_HP28

| #define PWM\_EXTTRIG1\_HP28   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(10, 0xFF, 0, 1, 12, 0) |
| --- |

## [◆ ](#afb4d7dfd327df023d9e3268678d3313e)PWM\_EXTTRIG1\_HP54

| #define PWM\_EXTTRIG1\_HP54   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(8, 0xFF, 18, 3, 6, 0) |
| --- |

## [◆ ](#a5d8597d305f1ac3b6f5ed8b5b85da936)PWM\_EXTTRIG1\_ULP7

| #define PWM\_EXTTRIG1\_ULP7   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(10, 6, 29, 4, 7, 7) |
| --- |

## [◆ ](#a0516ffe89d34afcebe7b594def541e37)PWM\_EXTTRIG2\_HP29

| #define PWM\_EXTTRIG2\_HP29   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(10, 0xFF, 0, 1, 13, 0) |
| --- |

## [◆ ](#a7c46b667cc3ce330c6d75f79f97b764b)PWM\_EXTTRIG2\_HP55

| #define PWM\_EXTTRIG2\_HP55   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(8, 0xFF, 19, 3, 7, 0) |
| --- |

## [◆ ](#a83421e64cf0f348be8cce195d0eb27c1)PWM\_EXTTRIG2\_ULP8

| #define PWM\_EXTTRIG2\_ULP8   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(10, 6, 30, 4, 8, 8) |
| --- |

## [◆ ](#a478e0230aa6373a816bfbf4c6ec5da96)PWM\_EXTTRIG3\_HP30

| #define PWM\_EXTTRIG3\_HP30   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(10, 0xFF, 0, 1, 14, 0) |
| --- |

## [◆ ](#ac4b0686f2db1db395ff0ffba43e7e1b7)PWM\_EXTTRIG3\_HP50

| #define PWM\_EXTTRIG3\_HP50   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(8, 0xFF, 14, 3, 2, 0) |
| --- |

## [◆ ](#a5c3cf988f7d14ecaca8e02734cb15eee)PWM\_EXTTRIG3\_ULP9

| #define PWM\_EXTTRIG3\_ULP9   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(10, 6, 31, 4, 9, 9) |
| --- |

## [◆ ](#a73af0f23d97c3f7c3466e29be238d2e9)PWM\_FAULTA\_HP25

| #define PWM\_FAULTA\_HP25   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(10, 0xFF, 0, 1, 9, 0) |
| --- |

## [◆ ](#a1be2559bbd5c14e4b8d02fae6d834db3)PWM\_FAULTA\_ULP4

| #define PWM\_FAULTA\_ULP4   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(10, 6, 26, 4, 4, 4) |
| --- |

## [◆ ](#a898809d281a1451c860755372034ac14)PWM\_FAULTA\_ULP9

| #define PWM\_FAULTA\_ULP9   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(8, 6, 31, 4, 9, 9) |
| --- |

## [◆ ](#a2d00f4de6aa3fe5ba797a8a50fd16751)PWM\_FAULTB\_HP26

| #define PWM\_FAULTB\_HP26   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(10, 0xFF, 0, 1, 10, 0) |
| --- |

## [◆ ](#a4bfb8e85f37893aceed66e457c34b9bd)PWM\_FAULTB\_ULP10

| #define PWM\_FAULTB\_ULP10   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(8, 6, 32, 4, 10, 10) |
| --- |

## [◆ ](#ad631deeca8cc40fcc2df48ec50297c9f)PWM\_FAULTB\_ULP5

| #define PWM\_FAULTB\_ULP5   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(10, 6, 27, 4, 5, 5) |
| --- |

## [◆ ](#a4f0903ae305c9bf1a9808b139a537a5d)PWM\_SLEEPEVENT\_ULP8

| #define PWM\_SLEEPEVENT\_ULP8   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(8, 6, 30, 4, 8, 8) |
| --- |

## [◆ ](#ab648897fd2173a6306ea1f12581a5257)QEI\_DIR\_HP11

| #define QEI\_DIR\_HP11   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(5, 0xFF, 6, 0, 11, 0) |
| --- |

## [◆ ](#acc5868c473301e8556cddd9d867bd0fe)QEI\_DIR\_HP28

| #define QEI\_DIR\_HP28   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(5, 0xFF, 0, 1, 12, 0) |
| --- |

## [◆ ](#a7fcabffea8d0e7f0ca1d7b3b53c77554)QEI\_DIR\_HP34

| #define QEI\_DIR\_HP34   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(13, 0xFF, 9, 2, 2, 0) |
| --- |

## [◆ ](#ac0df08c2fad11c4d658d9f715d610bbe)QEI\_DIR\_HP49

| #define QEI\_DIR\_HP49   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(3, 0xFF, 13, 3, 1, 0) |
| --- |

## [◆ ](#aecd388fd3a1c7d76cbc3b058d333fbdc)QEI\_DIR\_HP57

| #define QEI\_DIR\_HP57   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(5, 0xFF, 21, 3, 9, 0) |
| --- |

## [◆ ](#a6bcd0fd50eb5acfbd616b96a041a8b40)QEI\_DIR\_ULP11

| #define QEI\_DIR\_ULP11   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(3, 6, 33, 4, 11, 11) |
| --- |

## [◆ ](#a6be591b8ce2f422f66e10e7c1591e835)QEI\_DIR\_ULP3

| #define QEI\_DIR\_ULP3   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(3, 6, 25, 4, 3, 3) |
| --- |

## [◆ ](#a0d53fec86fc5cd9aa5b094d0f6e8229b)QEI\_DIR\_ULP7

| #define QEI\_DIR\_ULP7   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(3, 6, 29, 4, 7, 7) |
| --- |

## [◆ ](#a41c53b072b0975e7b39725a0cedd6b49)QEI\_IDX\_HP25

| #define QEI\_IDX\_HP25   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(5, 0xFF, 0, 1, 9, 0) |
| --- |

## [◆ ](#aca6d952fdb3eb1bd2c9fcd088770e482)QEI\_IDX\_HP31

| #define QEI\_IDX\_HP31   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(13, 0xFF, 9, 1, 15, 0) |
| --- |

## [◆ ](#aa2f488c074c7133f4457594dc8f57000)QEI\_IDX\_HP46

| #define QEI\_IDX\_HP46   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(3, 0xFF, 10, 2, 14, 0) |
| --- |

## [◆ ](#a0637cea93d1c922d3540551a92b5e8d6)QEI\_IDX\_HP52

| #define QEI\_IDX\_HP52   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(5, 0xFF, 16, 3, 4, 0) |
| --- |

## [◆ ](#a3023c95f055645c0c988b5578d7943eb)QEI\_IDX\_HP8

| #define QEI\_IDX\_HP8   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(5, 0xFF, 3, 0, 8, 0) |
| --- |

## [◆ ](#aa5571fa3facfca9e58accb575a8aa14b)QEI\_IDX\_ULP0

| #define QEI\_IDX\_ULP0   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(3, 6, 22, 4, 0, 0) |
| --- |

## [◆ ](#a5e4085d82f00810d0d8a0c79bae2fb8b)QEI\_IDX\_ULP4

| #define QEI\_IDX\_ULP4   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(3, 6, 26, 4, 4, 4) |
| --- |

## [◆ ](#ade023149f5a2daf2c21d2a5b8db31ebf)QEI\_IDX\_ULP8

| #define QEI\_IDX\_ULP8   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(3, 6, 30, 4, 8, 8) |
| --- |

## [◆ ](#afd774767dbccf18955aa2acd8fe3f27c)QEI\_PHA\_HP26

| #define QEI\_PHA\_HP26   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(5, 0xFF, 0, 1, 10, 0) |
| --- |

## [◆ ](#a1e7b4deeddd4e6139fee6a55752cff49)QEI\_PHA\_HP32

| #define QEI\_PHA\_HP32   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(13, 0xFF, 9, 2, 0, 0) |
| --- |

## [◆ ](#a9442f432d1602296f6ca19c43f4e4e32)QEI\_PHA\_HP47

| #define QEI\_PHA\_HP47   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(3, 0xFF, 11, 2, 15, 0) |
| --- |

## [◆ ](#ab6729735aa0f81049c357142ce64a3fb)QEI\_PHA\_HP53

| #define QEI\_PHA\_HP53   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(5, 0xFF, 17, 3, 5, 0) |
| --- |

## [◆ ](#a7c2638ce5bd7fe1fc3aed00841ebf805)QEI\_PHA\_HP9

| #define QEI\_PHA\_HP9   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(5, 0xFF, 4, 0, 9, 0) |
| --- |

## [◆ ](#a02cd57249ab4cbe4ac6f50bf4ac4640d)QEI\_PHA\_ULP1

| #define QEI\_PHA\_ULP1   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(3, 6, 23, 4, 1, 1) |
| --- |

## [◆ ](#a05d2c45f5f6f8e6caa749fa62f8952d2)QEI\_PHA\_ULP5

| #define QEI\_PHA\_ULP5   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(3, 6, 27, 4, 5, 5) |
| --- |

## [◆ ](#a4e7d6e023c35e3c9afe66dea3c777f2f)QEI\_PHA\_ULP9

| #define QEI\_PHA\_ULP9   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(3, 6, 31, 4, 9, 9) |
| --- |

## [◆ ](#aeb1bc91f700271730e3ef17a2c0f2713)QEI\_PHB\_HP10

| #define QEI\_PHB\_HP10   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(5, 0xFF, 5, 0, 10, 0) |
| --- |

## [◆ ](#a1df3d67f2727fb71a0639c352b397154)QEI\_PHB\_HP27

| #define QEI\_PHB\_HP27   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(5, 0xFF, 0, 1, 11, 0) |
| --- |

## [◆ ](#a46fa92c9b2cb1139dc6d436251d238c9)QEI\_PHB\_HP33

| #define QEI\_PHB\_HP33   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(13, 0xFF, 9, 2, 1, 0) |
| --- |

## [◆ ](#a19b95ea8cddcf086fc2ffe5a46d43f13)QEI\_PHB\_HP48

| #define QEI\_PHB\_HP48   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(3, 0xFF, 12, 3, 0, 0) |
| --- |

## [◆ ](#a8a2ebd9d12f75fd4fef28190c03c4e60)QEI\_PHB\_HP56

| #define QEI\_PHB\_HP56   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(5, 0xFF, 20, 3, 8, 0) |
| --- |

## [◆ ](#a2b7eafbd2fdae8fc813ebebbd912539b)QEI\_PHB\_ULP10

| #define QEI\_PHB\_ULP10   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(3, 6, 32, 4, 10, 10) |
| --- |

## [◆ ](#af323d2f63b6a1e26b9aa05a64c74ffbf)QEI\_PHB\_ULP2

| #define QEI\_PHB\_ULP2   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(3, 6, 24, 4, 2, 2) |
| --- |

## [◆ ](#addcd05ab910922d7924bf01b643bec87)QEI\_PHB\_ULP6

| #define QEI\_PHB\_ULP6   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(3, 6, 28, 4, 6, 6) |
| --- |

## [◆ ](#a7672e6df6d9de5ba6945492cf635ccb0)QSPI\_CLK\_HP46

| #define QSPI\_CLK\_HP46   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(1, 0xFF, 10, 2, 14, 0) |
| --- |

## [◆ ](#a0f23032eac930624c7ec43e5be873ff5)QSPI\_CLK\_HP52

| #define QSPI\_CLK\_HP52   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(9, 0xFF, 16, 3, 4, 0) |
| --- |

## [◆ ](#a9c3d01a17c03a4a1facc7a06453e1cf9)QSPI\_CLK\_HP8

| #define QSPI\_CLK\_HP8   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(11, 0xFF, 3, 0, 8, 0) |
| --- |

## [◆ ](#a96e4e990dd6f716ae41bbfb560b36b0e)QSPI\_CSN0\_HP49

| #define QSPI\_CSN0\_HP49   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(1, 0xFF, 13, 3, 1, 0) |
| --- |

## [◆ ](#a12adeb047d22f21a55a9c33d434f5876)QSPI\_CSN0\_HP55

| #define QSPI\_CSN0\_HP55   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(9, 0xFF, 19, 3, 7, 0) |
| --- |

## [◆ ](#a821ba16d8ff315bad8999a6e6ec219a8)QSPI\_CSN0\_HP7

| #define QSPI\_CSN0\_HP7   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(11, 0xFF, 2, 0, 7, 0) |
| --- |

## [◆ ](#a41005274eb64b874b2bc57bf75de0ea2)QSPI\_CSN1\_HP53

| #define QSPI\_CSN1\_HP53   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(1, 0xFF, 17, 3, 5, 0) |
| --- |

## [◆ ](#ab67034dc6fe34b9cdf4b6623e06ce0b0)QSPI\_CSN1\_HP7

| #define QSPI\_CSN1\_HP7   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(12, 0xFF, 2, 0, 7, 0) |
| --- |

## [◆ ](#a532ec03ed4eef5b2830ec449eed145dc)QSPI\_CSN9\_HP49

| #define QSPI\_CSN9\_HP49   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(10, 0xFF, 13, 3, 1, 0) |
| --- |

## [◆ ](#a6a443443e9195422d2aefe95d62263c3)QSPI\_D0\_HP47

| #define QSPI\_D0\_HP47   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(1, 0xFF, 11, 2, 15, 0) |
| --- |

## [◆ ](#a29fe7871dbef16e0f98dea867e444c90)QSPI\_D0\_HP53

| #define QSPI\_D0\_HP53   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(9, 0xFF, 17, 3, 5, 0) |
| --- |

## [◆ ](#a776bb46ee650922c9d8d6bf0796cf2b9)QSPI\_D0\_HP6

| #define QSPI\_D0\_HP6   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(11, 0xFF, 1, 0, 6, 0) |
| --- |

## [◆ ](#abdb757e9c432a11b30649f5a09a8c896)QSPI\_D1\_HP48

| #define QSPI\_D1\_HP48   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(1, 0xFF, 12, 3, 0, 0) |
| --- |

## [◆ ](#ab0dffa76350eeeb2d3eb9c0adbdb9088)QSPI\_D1\_HP54

| #define QSPI\_D1\_HP54   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(9, 0xFF, 18, 3, 6, 0) |
| --- |

## [◆ ](#ac8616e792c4715d73899701b08aabdad)QSPI\_D1\_HP9

| #define QSPI\_D1\_HP9   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(11, 0xFF, 4, 0, 9, 0) |
| --- |

## [◆ ](#aa32be2bfcdea9856c7c50606245cc74e)QSPI\_D2\_HP10

| #define QSPI\_D2\_HP10   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(11, 0xFF, 5, 0, 10, 0) |
| --- |

## [◆ ](#aee6e6ee41ebe13d44d0264f337d3db4f)QSPI\_D2\_HP50

| #define QSPI\_D2\_HP50   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(1, 0xFF, 14, 3, 2, 0) |
| --- |

## [◆ ](#a08c29c30a534bbb0f24d91d76f96f41a)QSPI\_D2\_HP56

| #define QSPI\_D2\_HP56   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(9, 0xFF, 20, 3, 8, 0) |
| --- |

## [◆ ](#a5c85e86968bbd77e4fa2797af059ff59)QSPI\_D3\_HP11

| #define QSPI\_D3\_HP11   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(11, 0xFF, 6, 0, 11, 0) |
| --- |

## [◆ ](#a966ce19ae5d27c19817c06dd865d643a)QSPI\_D3\_HP51

| #define QSPI\_D3\_HP51   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(1, 0xFF, 15, 3, 3, 0) |
| --- |

## [◆ ](#ae4a6bb7540deaa29fc63cfe9ac5b6650)QSPI\_D3\_HP57

| #define QSPI\_D3\_HP57   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(9, 0xFF, 21, 3, 9, 0) |
| --- |

## [◆ ](#ab02591e8fcb3a366d42b0507ebdd218b)QSPI\_D4\_HP54

| #define QSPI\_D4\_HP54   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(1, 0xFF, 18, 3, 6, 0) |
| --- |

## [◆ ](#a1a35413b75de975a97da3321a0c0072e)QSPI\_D5\_HP55

| #define QSPI\_D5\_HP55   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(1, 0xFF, 19, 3, 7, 0) |
| --- |

## [◆ ](#a4380587dc3fa09f5908edcd48fa26aa3)QSPI\_D6\_HP56

| #define QSPI\_D6\_HP56   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(1, 0xFF, 20, 3, 8, 0) |
| --- |

## [◆ ](#adad1d5fd641d6eaa11653eb7fa821b2e)QSPI\_D7\_HP57

| #define QSPI\_D7\_HP57   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(1, 0xFF, 21, 3, 9, 0) |
| --- |

## [◆ ](#aa062df96d3fd76dfde6eeb4e0a882278)SCT\_IN0\_HP25

| #define SCT\_IN0\_HP25   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(9, 0xFF, 0, 1, 9, 0) |
| --- |

## [◆ ](#a99b69d8a4f849a64b236986a2abc21c9)SCT\_IN0\_ULP0

| #define SCT\_IN0\_ULP0   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(7, 6, 22, 4, 0, 0) |
| --- |

## [◆ ](#a3ab3d2e1f5a11a5386b700f03cf98b59)SCT\_IN0\_ULP4

| #define SCT\_IN0\_ULP4   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(9, 6, 26, 4, 4, 4) |
| --- |

## [◆ ](#a129dc73d20f20394c4c30fbecd755cf5)SCT\_IN1\_HP26

| #define SCT\_IN1\_HP26   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(9, 0xFF, 0, 1, 10, 0) |
| --- |

## [◆ ](#a0795a0474012f940b032bf0c93a54283)SCT\_IN1\_ULP1

| #define SCT\_IN1\_ULP1   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(7, 6, 23, 4, 1, 1) |
| --- |

## [◆ ](#aa543bccd5eaa129a2e71626bfb5a9e0e)SCT\_IN1\_ULP5

| #define SCT\_IN1\_ULP5   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(9, 6, 27, 4, 5, 5) |
| --- |

## [◆ ](#ac120a628c9b6f2f55b99ab810e6575fb)SCT\_IN2\_HP27

| #define SCT\_IN2\_HP27   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(9, 0xFF, 0, 1, 11, 0) |
| --- |

## [◆ ](#a2d6b23ffe6db55ca5e76118dea7a14ea)SCT\_IN2\_ULP2

| #define SCT\_IN2\_ULP2   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(7, 6, 24, 4, 2, 2) |
| --- |

## [◆ ](#aa9e34755ee740ce485048bc6edae12b1)SCT\_IN2\_ULP6

| #define SCT\_IN2\_ULP6   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(9, 6, 28, 4, 6, 6) |
| --- |

## [◆ ](#a62b8aa7dd85b312896c126bc09daf4f0)SCT\_IN3\_HP28

| #define SCT\_IN3\_HP28   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(9, 0xFF, 0, 1, 12, 0) |
| --- |

## [◆ ](#a20d138a68cefaf8a5785def1553adf10)SCT\_IN3\_ULP3

| #define SCT\_IN3\_ULP3   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(7, 6, 25, 4, 3, 3) |
| --- |

## [◆ ](#a9f850c61dbeb18c64e8d133cc37aee77)SCT\_IN3\_ULP7

| #define SCT\_IN3\_ULP7   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(9, 6, 29, 4, 7, 7) |
| --- |

## [◆ ](#a487a88c8ad8a9c5cfa33639ea27ac5d2)SCT\_OUT0\_HP29

| #define SCT\_OUT0\_HP29   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(9, 0xFF, 0, 1, 13, 0) |
| --- |

## [◆ ](#a31a6744e2a07d61f7aff3a64d29c6345)SCT\_OUT0\_ULP4

| #define SCT\_OUT0\_ULP4   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(7, 6, 26, 4, 4, 4) |
| --- |

## [◆ ](#a8d5e593bab255708bb5a34549dbc39ff)SCT\_OUT1\_HP30

| #define SCT\_OUT1\_HP30   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(9, 0xFF, 0, 1, 14, 0) |
| --- |

## [◆ ](#aeee61408d7a9d0fb3ec2b099bf6b4925)SCT\_OUT1\_ULP5

| #define SCT\_OUT1\_ULP5   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(7, 6, 27, 4, 5, 5) |
| --- |

## [◆ ](#a896f7133bc09d5776b8fce43a919a582)SCT\_OUT2\_HP8

| #define SCT\_OUT2\_HP8   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(12, 0xFF, 3, 0, 8, 0) |
| --- |

## [◆ ](#aceb19f98ff9d765be5ac4163c400b30f)SCT\_OUT2\_ULP6

| #define SCT\_OUT2\_ULP6   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(7, 6, 28, 4, 6, 6) |
| --- |

## [◆ ](#a23b5eb6cd7cb43df14db4f42a05d8b70)SCT\_OUT3\_HP9

| #define SCT\_OUT3\_HP9   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(12, 0xFF, 4, 0, 9, 0) |
| --- |

## [◆ ](#a3d240479009ee2c1660006406a51e14b)SCT\_OUT3\_ULP7

| #define SCT\_OUT3\_ULP7   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(7, 6, 29, 4, 7, 7) |
| --- |

## [◆ ](#aa1ce9c940b0f1b1f85e8c0aa765afe58)SCT\_OUT4\_ULP4

| #define SCT\_OUT4\_ULP4   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(13, 6, 26, 4, 4, 4) |
| --- |

## [◆ ](#a56f04a2fdf3d596c09989bb7f2f4d711)SCT\_OUT4\_ULP8

| #define SCT\_OUT4\_ULP8   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(7, 6, 30, 4, 8, 8) |
| --- |

## [◆ ](#abddc79f260ecc7fb85878f5182f0b4b2)SCT\_OUT5\_ULP5

| #define SCT\_OUT5\_ULP5   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(13, 6, 27, 4, 5, 5) |
| --- |

## [◆ ](#a14ad4c709bf766e5568ec2214c29935d)SCT\_OUT5\_ULP9

| #define SCT\_OUT5\_ULP9   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(7, 6, 31, 4, 9, 9) |
| --- |

## [◆ ](#a9833d3691184034534dac5542141979c)SCT\_OUT6\_ULP10

| #define SCT\_OUT6\_ULP10   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(7, 6, 32, 4, 10, 10) |
| --- |

## [◆ ](#ab3ecf512e8c70db0f9a7a374d5c4ee61)SCT\_OUT6\_ULP6

| #define SCT\_OUT6\_ULP6   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(13, 6, 28, 4, 6, 6) |
| --- |

## [◆ ](#a72096ef61c9b342223b90a4a2a2cad67)SCT\_OUT7\_ULP11

| #define SCT\_OUT7\_ULP11   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(7, 6, 33, 4, 11, 11) |
| --- |

## [◆ ](#a58d91744df7f674a8d639efee6ada664)SCT\_OUT7\_ULP7

| #define SCT\_OUT7\_ULP7   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(13, 6, 29, 4, 7, 7) |
| --- |

## [◆ ](#a50c459097b961e8f0b8ebb4b0022ff24)SIO\_0\_HP25

| #define SIO\_0\_HP25   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(1, 0xFF, 0, 1, 9, 0) |
| --- |

## [◆ ](#a0832163dccdf4899e70bc54e1c1d76b9)SIO\_0\_HP6

| #define SIO\_0\_HP6   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(1, 0xFF, 1, 0, 6, 0) |
| --- |

## [◆ ](#ac962669966622a760066ae1d644cf16e)SIO\_0\_ULP0

| #define SIO\_0\_ULP0   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(1, 6, 22, 4, 0, 0) |
| --- |

## [◆ ](#a9e2fbc5435e49df883f1cf0394ca5720)SIO\_0\_ULP8

| #define SIO\_0\_ULP8   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(1, 6, 30, 4, 8, 8) |
| --- |

## [◆ ](#ab1bffb41dcfd954d4110cdb091b5f1dd)SIO\_1\_HP26

| #define SIO\_1\_HP26   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(1, 0xFF, 0, 1, 10, 0) |
| --- |

## [◆ ](#aeb287420b59b4085df40b2bc8c4a9bb8)SIO\_1\_HP7

| #define SIO\_1\_HP7   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(1, 0xFF, 2, 0, 7, 0) |
| --- |

## [◆ ](#ac6a3e01783137270cf5fa27b02c62c5c)SIO\_1\_ULP1

| #define SIO\_1\_ULP1   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(1, 6, 23, 4, 1, 1) |
| --- |

## [◆ ](#ac75318d95fac4ae093072ed1f73e18c0)SIO\_1\_ULP9

| #define SIO\_1\_ULP9   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(1, 6, 31, 4, 9, 9) |
| --- |

## [◆ ](#a89795f8bd3ae258fa3c0f1daf2521d55)SIO\_2\_HP27

| #define SIO\_2\_HP27   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(1, 0xFF, 0, 1, 11, 0) |
| --- |

## [◆ ](#a09ae893ea29f226c66d823ea6d8e9dea)SIO\_2\_HP8

| #define SIO\_2\_HP8   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(1, 0xFF, 3, 0, 8, 0) |
| --- |

## [◆ ](#ab203641292581774bcf3ea40e5c6f465)SIO\_2\_ULP10

| #define SIO\_2\_ULP10   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(1, 6, 32, 4, 10, 10) |
| --- |

## [◆ ](#accd43e63baf2ece7c3105e7b1179281f)SIO\_2\_ULP2

| #define SIO\_2\_ULP2   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(1, 6, 24, 4, 2, 2) |
| --- |

## [◆ ](#af40550b595f5f30ac0a6ae2335e6ec55)SIO\_3\_HP28

| #define SIO\_3\_HP28   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(1, 0xFF, 0, 1, 12, 0) |
| --- |

## [◆ ](#a3ee11e86b6d00fb603f8389a69ace17f)SIO\_3\_HP9

| #define SIO\_3\_HP9   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(1, 0xFF, 4, 0, 9, 0) |
| --- |

## [◆ ](#acafbbec57e7c4b952398106cb9a03ef7)SIO\_3\_ULP11

| #define SIO\_3\_ULP11   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(1, 6, 33, 4, 11, 11) |
| --- |

## [◆ ](#ae271fa5750acca3534ea22178fea6fc5)SIO\_3\_ULP3

| #define SIO\_3\_ULP3   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(1, 6, 25, 4, 3, 3) |
| --- |

## [◆ ](#acbe0ac06f6094ddc13e5ff98ecf9345d)SIO\_4\_HP10

| #define SIO\_4\_HP10   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(1, 0xFF, 5, 0, 10, 0) |
| --- |

## [◆ ](#a2abfaa99057e594bdd1b3ed640744114)SIO\_4\_HP29

| #define SIO\_4\_HP29   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(1, 0xFF, 0, 1, 13, 0) |
| --- |

## [◆ ](#ac0274ba6c1129339f49f087e9b503759)SIO\_4\_ULP4

| #define SIO\_4\_ULP4   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(1, 6, 26, 4, 4, 4) |
| --- |

## [◆ ](#a6da8512e01689d6eff690f5ad538bc01)SIO\_5\_HP11

| #define SIO\_5\_HP11   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(1, 0xFF, 6, 0, 11, 0) |
| --- |

## [◆ ](#a81766e7a7df2e5f915517f2065750c7a)SIO\_5\_HP30

| #define SIO\_5\_HP30   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(1, 0xFF, 0, 1, 14, 0) |
| --- |

## [◆ ](#a07a673ae96d7332b5799d7e779180cc9)SIO\_5\_ULP5

| #define SIO\_5\_ULP5   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(1, 6, 27, 4, 5, 5) |
| --- |

## [◆ ](#ab6d4f24470587604725bb9612d988b34)SIO\_6\_ULP6

| #define SIO\_6\_ULP6   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(1, 6, 28, 4, 6, 6) |
| --- |

## [◆ ](#aa6a42c96535dd6934fa0bc4886ea00b7)SIO\_7\_HP15

| #define SIO\_7\_HP15   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(1, 0xFF, 8, 0, 15, 0) |
| --- |

## [◆ ](#a52635e4cce4a478134455ea5ee43c962)SIO\_7\_ULP7

| #define SIO\_7\_ULP7   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(1, 6, 29, 4, 7, 7) |
| --- |

## [◆ ](#a77b8278e81edee91c96c990c2479144f)SSI\_CLK\_HP25

| #define SSI\_CLK\_HP25   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(3, 0xFF, 0, 1, 9, 0) |
| --- |

## [◆ ](#a166065c88ad7a8bf66d6ca7b51628a2f)SSI\_CLK\_HP52

| #define SSI\_CLK\_HP52   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(3, 0xFF, 16, 3, 4, 0) |
| --- |

## [◆ ](#a0d8209a8fb54f5ef19bb86981b383c43)SSI\_CLK\_HP8

| #define SSI\_CLK\_HP8   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(3, 0xFF, 3, 0, 8, 0) |
| --- |

## [◆ ](#aa070abef007fb1355d3a151038c4b282)SSI\_CS0\_HP28

| #define SSI\_CS0\_HP28   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(3, 0xFF, 0, 1, 12, 0) |
| --- |

## [◆ ](#a9e28d21c0d469b33398b0c24936478bc)SSI\_CS0\_HP53

| #define SSI\_CS0\_HP53   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(3, 0xFF, 17, 3, 5, 0) |
| --- |

## [◆ ](#ac29bdcb9b8693277b6b6e8950576b4d7)SSI\_CS0\_HP9

| #define SSI\_CS0\_HP9   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(3, 0xFF, 4, 0, 9, 0) |
| --- |

## [◆ ](#a2858feb71f44abd3b8e0a49d00fd5a03)SSI\_CS1\_HP10

| #define SSI\_CS1\_HP10   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(3, 0xFF, 5, 0, 10, 0) |
| --- |

## [◆ ](#a7b0f6b3e42fb8329ed491b5561aef908)SSI\_CS2\_HP15

| #define SSI\_CS2\_HP15   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(3, 0xFF, 8, 0, 15, 0) |
| --- |

## [◆ ](#a0c54f4dc5efdcc32a32dc79449f58ea1)SSI\_CS2\_HP50

| #define SSI\_CS2\_HP50   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(3, 0xFF, 14, 3, 2, 0) |
| --- |

## [◆ ](#aafdfc33c0bbe11b258479379ed42d486)SSI\_CS3\_HP51

| #define SSI\_CS3\_HP51   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(3, 0xFF, 15, 3, 3, 0) |
| --- |

## [◆ ](#ab65665cb7ad83803229e49b068615593)SSI\_DATA0\_HP11

| #define SSI\_DATA0\_HP11   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(3, 0xFF, 6, 0, 11, 0) |
| --- |

## [◆ ](#a636c99a6026a8463ebd53ac63a270956)SSI\_DATA0\_HP26

| #define SSI\_DATA0\_HP26   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(3, 0xFF, 0, 1, 10, 0) |
| --- |

## [◆ ](#ac204f25409e010a300cdbe48c6ad255b)SSI\_DATA0\_HP56

| #define SSI\_DATA0\_HP56   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(3, 0xFF, 20, 3, 8, 0) |
| --- |

## [◆ ](#a3481b7ccfebdb2e679127a99b9410443)SSI\_DATA1\_HP10

| #define SSI\_DATA1\_HP10   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(12, 0xFF, 5, 0, 10, 0) |
| --- |

## [◆ ](#a3ca3fd4c997fc966808b637bd5ce9cf5)SSI\_DATA1\_HP12

| #define SSI\_DATA1\_HP12   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(3, 0xFF, 7, 0, 12, 0) |
| --- |

## [◆ ](#a755e7244b7708e5863da85b21891f0f6)SSI\_DATA1\_HP27

| #define SSI\_DATA1\_HP27   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(3, 0xFF, 0, 1, 11, 0) |
| --- |

## [◆ ](#ace422b65e5eda30314e575c25633ff83)SSI\_DATA1\_HP57

| #define SSI\_DATA1\_HP57   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(3, 0xFF, 21, 3, 9, 0) |
| --- |

## [◆ ](#aed349cea226d2b4577aafb3f916cf921)SSI\_DATA2\_HP29

| #define SSI\_DATA2\_HP29   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(3, 0xFF, 0, 1, 13, 0) |
| --- |

## [◆ ](#a46431de74f13595e9f143032b1e7816e)SSI\_DATA2\_HP54

| #define SSI\_DATA2\_HP54   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(3, 0xFF, 18, 3, 6, 0) |
| --- |

## [◆ ](#a91b07b14b58117fe2cd6627a7a9831f8)SSI\_DATA2\_HP6

| #define SSI\_DATA2\_HP6   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(3, 0xFF, 1, 0, 6, 0) |
| --- |

## [◆ ](#a5e711f668e3bf36c0068868019d91dfd)SSI\_DATA3\_HP30

| #define SSI\_DATA3\_HP30   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(3, 0xFF, 0, 1, 14, 0) |
| --- |

## [◆ ](#a6a3f96e3b7129d2d1625da6ef7be0e52)SSI\_DATA3\_HP55

| #define SSI\_DATA3\_HP55   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(3, 0xFF, 19, 3, 7, 0) |
| --- |

## [◆ ](#ae03aa3be0edb0c5dcd4fbbb3c7d48038)SSI\_DATA3\_HP7

| #define SSI\_DATA3\_HP7   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(3, 0xFF, 2, 0, 7, 0) |
| --- |

## [◆ ](#a246b34d2a347e66749a95f2865f40060)SSIS\_CLK\_HP26

| #define SSIS\_CLK\_HP26   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(8, 0xFF, 0, 1, 10, 0) |
| --- |

## [◆ ](#a50d2c8019a3e7b2c7b2d9c62c092c239)SSIS\_CLK\_HP47

| #define SSIS\_CLK\_HP47   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(8, 0xFF, 11, 2, 15, 0) |
| --- |

## [◆ ](#a8aaf5a65d4af6ad97b74eb4d280aa808)SSIS\_CLK\_HP52

| #define SSIS\_CLK\_HP52   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(8, 0xFF, 16, 3, 4, 0) |
| --- |

## [◆ ](#ad2741d1cf1901f68ab2825a2cade5712)SSIS\_CLK\_HP8

| #define SSIS\_CLK\_HP8   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(8, 0xFF, 3, 0, 8, 0) |
| --- |

## [◆ ](#a0ccfb2d0b256ae264aa2fab362240537)SSIS\_CS\_HP25

| #define SSIS\_CS\_HP25   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(8, 0xFF, 0, 1, 9, 0) |
| --- |

## [◆ ](#a33ddacd923544e99d56f12b00d3a58c4)SSIS\_CS\_HP46

| #define SSIS\_CS\_HP46   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(8, 0xFF, 10, 2, 14, 0) |
| --- |

## [◆ ](#af37723fe1fb0edfd1cef5334fa2286e0)SSIS\_CS\_HP53

| #define SSIS\_CS\_HP53   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(8, 0xFF, 17, 3, 5, 0) |
| --- |

## [◆ ](#a558f00dabc8270c6e3464311055c927c)SSIS\_CS\_HP9

| #define SSIS\_CS\_HP9   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(8, 0xFF, 4, 0, 9, 0) |
| --- |

## [◆ ](#af11a72c74fc5de2890ff29882a549c7d)SSIS\_MISO\_HP11

| #define SSIS\_MISO\_HP11   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(8, 0xFF, 6, 0, 11, 0) |
| --- |

## [◆ ](#ac29849ee9448a7da3dc0dfd9584fe8e6)SSIS\_MISO\_HP28

| #define SSIS\_MISO\_HP28   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(8, 0xFF, 0, 1, 12, 0) |
| --- |

## [◆ ](#af26a275bd867021c3c2fe617b2f90d56)SSIS\_MISO\_HP49

| #define SSIS\_MISO\_HP49   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(8, 0xFF, 13, 3, 1, 0) |
| --- |

## [◆ ](#a303a10aa5fac51931f1fd2625476c250)SSIS\_MISO\_HP57

| #define SSIS\_MISO\_HP57   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(8, 0xFF, 21, 3, 9, 0) |
| --- |

## [◆ ](#a09804ebbc7f861922372cca189f539c1)SSIS\_MOSI\_HP10

| #define SSIS\_MOSI\_HP10   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(8, 0xFF, 5, 0, 10, 0) |
| --- |

## [◆ ](#a0217b56cf5d51ef66de6aba1d2a7e75e)SSIS\_MOSI\_HP27

| #define SSIS\_MOSI\_HP27   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(8, 0xFF, 0, 1, 11, 0) |
| --- |

## [◆ ](#a4227e1213145f52cf732f237256f9606)SSIS\_MOSI\_HP48

| #define SSIS\_MOSI\_HP48   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(8, 0xFF, 12, 3, 0, 0) |
| --- |

## [◆ ](#acc3c25b45390c7e676d06717dc468251)SSIS\_MOSI\_HP56

| #define SSIS\_MOSI\_HP56   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(8, 0xFF, 20, 3, 8, 0) |
| --- |

## [◆ ](#a49ae74d218db2a1132075c68c4574099)TIMER0\_HP27

| #define TIMER0\_HP27   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(11, 5, 0, 1, 11, 8) |
| --- |

## [◆ ](#aa8a483b521b450670203463f7d8be032)TIMER0\_HP46

| #define TIMER0\_HP46   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(9, 5, 10, 2, 14, 8) |
| --- |

## [◆ ](#a239d90024707952ed74238c3fc97608e)TIMER0\_HP7

| #define TIMER0\_HP7   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(9, 5, 2, 0, 7, 1) |
| --- |

## [◆ ](#a8043999b57da3920d59a3c61e68a26ae)TIMER0\_ULP4

| #define TIMER0\_ULP4   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(0xFF, 9, 0xFF, 4, 0, 4) |
| --- |

## [◆ ](#a412766982e02327695695d09968e4ee0)TIMER0\_ULP8

| #define TIMER0\_ULP8   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(0xFF, 5, 0xFF, 4, 0, 8) |
| --- |

## [◆ ](#a02a30a238516586b3e9f9d168edb855c)TIMER1\_HP15

| #define TIMER1\_HP15   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(9, 5, 8, 0, 15, 7) |
| --- |

## [◆ ](#a99e02ee3b901fc1ee4d9ea1021f9c746)TIMER1\_HP26

| #define TIMER1\_HP26   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(11, 5, 0, 1, 10, 7) |
| --- |

## [◆ ](#a99832252de48cc89d11c3e522ea44376)TIMER1\_ULP5

| #define TIMER1\_ULP5   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(0xFF, 9, 0xFF, 4, 0, 5) |
| --- |

## [◆ ](#aa1fb1deae2ad43558df04b772029957f)TIMER1\_ULP7

| #define TIMER1\_ULP7   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(0xFF, 5, 0xFF, 4, 0, 7) |
| --- |

## [◆ ](#aa778464dc8449625d49328f30c76e92e)TIMER2\_ULP1

| #define TIMER2\_ULP1   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(0xFF, 5, 0xFF, 4, 0, 1) |
| --- |

## [◆ ](#aa4fe9698b15438987cee0d3c0d4ed193)TRACE\_CLK\_HP47

| #define TRACE\_CLK\_HP47   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(6, 0xFF, 11, 2, 15, 0) |
| --- |

## [◆ ](#a9934d0e8efc26562ca6b28b3f5ece6e4)TRACE\_CLK\_HP53

| #define TRACE\_CLK\_HP53   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(6, 0xFF, 17, 3, 5, 0) |
| --- |

## [◆ ](#ad5d637f7c1e783f5bdd0f72d90a986cd)TRACE\_CLK\_HP7

| #define TRACE\_CLK\_HP7   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(13, 0xFF, 2, 0, 7, 0) |
| --- |

## [◆ ](#ab332137012b6fb95cf5d5eac07950296)TRACE\_CLKIN\_HP15

| #define TRACE\_CLKIN\_HP15   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(6, 0xFF, 8, 0, 15, 0) |
| --- |

## [◆ ](#ae1259534ea8316ebe29436705e258f69)TRACE\_CLKIN\_HP46

| #define TRACE\_CLKIN\_HP46   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(6, 0xFF, 10, 2, 14, 0) |
| --- |

## [◆ ](#a93a66a67b4b079b2d6ab0f64bccb5b7f)TRACE\_CLKIN\_HP52

| #define TRACE\_CLKIN\_HP52   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(6, 0xFF, 16, 3, 4, 0) |
| --- |

## [◆ ](#ad942d16221a23fae94615aeda7acb650)TRACE\_CLKIN\_HP6

| #define TRACE\_CLKIN\_HP6   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(13, 0xFF, 1, 0, 6, 0) |
| --- |

## [◆ ](#a25196d0c4d77efa6d1340aade4a7ab43)TRACE\_D0\_HP48

| #define TRACE\_D0\_HP48   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(6, 0xFF, 12, 3, 0, 0) |
| --- |

## [◆ ](#afa79f060e825009dcbf30c194cfd259a)TRACE\_D0\_HP54

| #define TRACE\_D0\_HP54   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(6, 0xFF, 18, 3, 6, 0) |
| --- |

## [◆ ](#a329ce75fc9014134a8684d7e384bb569)TRACE\_D0\_HP8

| #define TRACE\_D0\_HP8   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(13, 0xFF, 3, 0, 8, 0) |
| --- |

## [◆ ](#ac26e1b82bb464c5e2d1d4ed606b83f4c)TRACE\_D1\_HP49

| #define TRACE\_D1\_HP49   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(6, 0xFF, 13, 3, 1, 0) |
| --- |

## [◆ ](#ab019d73a28e7fd218c301a7a16a8744c)TRACE\_D1\_HP55

| #define TRACE\_D1\_HP55   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(6, 0xFF, 19, 3, 7, 0) |
| --- |

## [◆ ](#a6ac2fd081f541973db09767923e5c994)TRACE\_D1\_HP9

| #define TRACE\_D1\_HP9   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(13, 0xFF, 4, 0, 9, 0) |
| --- |

## [◆ ](#a8b1bae5956611a7a7ea0b9479236eba8)TRACE\_D2\_HP10

| #define TRACE\_D2\_HP10   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(13, 0xFF, 5, 0, 10, 0) |
| --- |

## [◆ ](#aabaa120c9882567d5fcb51adf4bee1d6)TRACE\_D2\_HP50

| #define TRACE\_D2\_HP50   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(6, 0xFF, 14, 3, 2, 0) |
| --- |

## [◆ ](#af2e5c3c47489489a5bb89767683f0426)TRACE\_D2\_HP56

| #define TRACE\_D2\_HP56   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(6, 0xFF, 20, 3, 8, 0) |
| --- |

## [◆ ](#ae6e493f9ab1a119b3b0d51ae46a09abb)TRACE\_D3\_HP11

| #define TRACE\_D3\_HP11   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(13, 0xFF, 6, 0, 11, 0) |
| --- |

## [◆ ](#a72ec3566d71b12eeaaa00e196f0d04b2)TRACE\_D3\_HP51

| #define TRACE\_D3\_HP51   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(6, 0xFF, 15, 3, 3, 0) |
| --- |

## [◆ ](#a74a11c7d6068e66986c6410f63a87a12)TRACE\_D3\_HP57

| #define TRACE\_D3\_HP57   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(6, 0xFF, 21, 3, 9, 0) |
| --- |

## [◆ ](#a702cef077f6ec6ba684e0cccff48e2ee)UART0\_CLK\_HP25

| #define UART0\_CLK\_HP25   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(2, 0xFF, 0, 1, 9, 0) |
| --- |

## [◆ ](#a8d19011b7dfb8ecca987d95084f1ef43)UART0\_CLK\_HP52

| #define UART0\_CLK\_HP52   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(2, 0xFF, 16, 3, 4, 0) |
| --- |

## [◆ ](#a1514c950553999c21e0d43c2d6aefddf)UART0\_CLK\_HP8

| #define UART0\_CLK\_HP8   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(2, 0xFF, 3, 0, 8, 0) |
| --- |

## [◆ ](#a2df47af0f0a9b175663bfce524da6187)UART0\_CLK\_ULP0

| #define UART0\_CLK\_ULP0   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(2, 6, 22, 4, 0, 0) |
| --- |

## [◆ ](#a16193dab96a8006cf2766c5cb152a32c)UART0\_CTS\_HP26

| #define UART0\_CTS\_HP26   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(2, 0xFF, 0, 1, 10, 0) |
| --- |

## [◆ ](#ae56529f660d670b4b8d21417a6e09de2)UART0\_CTS\_HP56

| #define UART0\_CTS\_HP56   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(2, 0xFF, 20, 3, 8, 0) |
| --- |

## [◆ ](#a873d1ee0fbe9c691bba5c72eb88989b6)UART0\_CTS\_HP6

| #define UART0\_CTS\_HP6   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(2, 0xFF, 1, 0, 6, 0) |
| --- |

## [◆ ](#a274238cb4dd58655ac8571d803e6bbb8)UART0\_CTS\_ULP6

| #define UART0\_CTS\_ULP6   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(2, 6, 28, 4, 6, 6) |
| --- |

## [◆ ](#aafcfe3007f6c11254e06dd61c92b3f4e)UART0\_DCD\_HP12

| #define UART0\_DCD\_HP12   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(2, 0xFF, 7, 0, 12, 0) |
| --- |

## [◆ ](#a5b8c6daf4798492ddd1bd1f36fc2ad70)UART0\_DCD\_HP29

| #define UART0\_DCD\_HP29   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(12, 0xFF, 0, 1, 13, 0) |
| --- |

## [◆ ](#a09324d646d1b31f3ef1064dec42cd87b)UART0\_DSR\_HP11

| #define UART0\_DSR\_HP11   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(2, 0xFF, 6, 0, 11, 0) |
| --- |

## [◆ ](#ae156c04dd623cd446e9b0e2e233638f3)UART0\_DSR\_HP57

| #define UART0\_DSR\_HP57   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(2, 0xFF, 21, 3, 9, 0) |
| --- |

## [◆ ](#a3593158afb8848932439923fddb5c0ac)UART0\_DTR\_HP7

| #define UART0\_DTR\_HP7   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(2, 0xFF, 2, 0, 7, 0) |
| --- |

## [◆ ](#a19dead7b9533bed8693a6f730ad5fd91)UART0\_IRRX\_HP25

| #define UART0\_IRRX\_HP25   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(13, 0xFF, 0, 1, 9, 0) |
| --- |

## [◆ ](#a9c2a4489ec8c0f9244485b4db066ca3f)UART0\_IRRX\_HP47

| #define UART0\_IRRX\_HP47   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(2, 0xFF, 11, 2, 15, 0) |
| --- |

## [◆ ](#adf611f1df2303d5155e071ccc56d8c30)UART0\_IRRX\_ULP0

| #define UART0\_IRRX\_ULP0   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(11, 6, 22, 4, 0, 0) |
| --- |

## [◆ ](#a659bdb287f75f00c7c644ae554983860)UART0\_IRRX\_ULP7

| #define UART0\_IRRX\_ULP7   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(2, 6, 29, 4, 7, 7) |
| --- |

## [◆ ](#a96681675723bed89eef7ed2ff68324b2)UART0\_IRTX\_HP26

| #define UART0\_IRTX\_HP26   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(13, 0xFF, 0, 1, 10, 0) |
| --- |

## [◆ ](#a5ada8867e27615e304abb89e8ed95b4a)UART0\_IRTX\_HP48

| #define UART0\_IRTX\_HP48   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(2, 0xFF, 12, 3, 0, 0) |
| --- |

## [◆ ](#ab9422f6b18b7d95f257eea54708c0da6)UART0\_IRTX\_ULP1

| #define UART0\_IRTX\_ULP1   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(11, 6, 23, 4, 1, 1) |
| --- |

## [◆ ](#adbcb3a2ebb68225e265ac83d77755540)UART0\_IRTX\_ULP8

| #define UART0\_IRTX\_ULP8   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(2, 6, 30, 4, 8, 8) |
| --- |

## [◆ ](#ae5f8f182da81b3b8dd85c32be0219439)UART0\_RI\_HP27

| #define UART0\_RI\_HP27   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(2, 0xFF, 0, 1, 11, 0) |
| --- |

## [◆ ](#a3938be42c21041a362aaec421751d9aa)UART0\_RI\_HP46

| #define UART0\_RI\_HP46   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(2, 0xFF, 10, 2, 14, 0) |
| --- |

## [◆ ](#a64d2529c38303a82f24b01ed5ad05be0)UART0\_RI\_ULP4

| #define UART0\_RI\_ULP4   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(11, 6, 26, 4, 4, 4) |
| --- |

## [◆ ](#af607a3b3e6374ce5bd6311b657eed71e)UART0\_RS485DE\_HP29

| #define UART0\_RS485DE\_HP29   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(13, 0xFF, 0, 1, 13, 0) |
| --- |

## [◆ ](#a50b16324373e3e32370d570491a4f535)UART0\_RS485DE\_HP51

| #define UART0\_RS485DE\_HP51   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(2, 0xFF, 15, 3, 3, 0) |
| --- |

## [◆ ](#a041682ac7bc0eaad6ef3b4e2e3ef3fc3)UART0\_RS485DE\_ULP11

| #define UART0\_RS485DE\_ULP11   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(2, 6, 33, 4, 11, 11) |
| --- |

## [◆ ](#a02a8e7b5adfc32af7af4e5ba088ce0f7)UART0\_RS485DE\_ULP7

| #define UART0\_RS485DE\_ULP7   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(11, 6, 29, 4, 7, 7) |
| --- |

## [◆ ](#a777e97d29443a4a43d92c39ba2d6480b)UART0\_RS485EN\_HP27

| #define UART0\_RS485EN\_HP27   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(13, 0xFF, 0, 1, 11, 0) |
| --- |

## [◆ ](#aa5a0741a5fcb9e89f16dd286e4e4d1d1)UART0\_RS485EN\_HP49

| #define UART0\_RS485EN\_HP49   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(2, 0xFF, 13, 3, 1, 0) |
| --- |

## [◆ ](#a91f4ac4b0941ef7177ee9b4896d3ab51)UART0\_RS485EN\_ULP5

| #define UART0\_RS485EN\_ULP5   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(11, 6, 27, 4, 5, 5) |
| --- |

## [◆ ](#a398e1bdbebdfae8177daa590b7a026ca)UART0\_RS485EN\_ULP9

| #define UART0\_RS485EN\_ULP9   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(2, 6, 31, 4, 9, 9) |
| --- |

## [◆ ](#a3f359f67b459ed81e8db5fd786e7089a)UART0\_RS485RE\_HP28

| #define UART0\_RS485RE\_HP28   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(13, 0xFF, 0, 1, 12, 0) |
| --- |

## [◆ ](#a19efcf4ac776bbb3156508a1b580e2f3)UART0\_RS485RE\_HP50

| #define UART0\_RS485RE\_HP50   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(2, 0xFF, 14, 3, 2, 0) |
| --- |

## [◆ ](#a806d9ce45c9bdac84f82da94b2e61623)UART0\_RS485RE\_ULP10

| #define UART0\_RS485RE\_ULP10   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(2, 6, 32, 4, 10, 10) |
| --- |

## [◆ ](#a0704cd391bbb230d5a359ec1f8dfcb5c)UART0\_RS485RE\_ULP6

| #define UART0\_RS485RE\_ULP6   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(11, 6, 28, 4, 6, 6) |
| --- |

## [◆ ](#af6180ba7e3498e1cb075cf84d08ac0c5)UART0\_RTS\_HP28

| #define UART0\_RTS\_HP28   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(2, 0xFF, 0, 1, 12, 0) |
| --- |

## [◆ ](#a0b18d3117184a53274c9455a1d2ba7d6)UART0\_RTS\_HP53

| #define UART0\_RTS\_HP53   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(2, 0xFF, 17, 3, 5, 0) |
| --- |

## [◆ ](#a5b04f93bc8455f7943a7dc71414f6fdd)UART0\_RTS\_HP9

| #define UART0\_RTS\_HP9   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(2, 0xFF, 4, 0, 9, 0) |
| --- |

## [◆ ](#acdeb030914a38257f40ba31622a8e44f)UART0\_RTS\_ULP5

| #define UART0\_RTS\_ULP5   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(2, 6, 27, 4, 5, 5) |
| --- |

## [◆ ](#aa12f9238e599d54cde0246c41ee7f216)UART0\_RX\_HP10

| #define UART0\_RX\_HP10   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(2, 0xFF, 5, 0, 10, 0) |
| --- |

## [◆ ](#a5f034df81ac363d212da25a510fd8869)UART0\_RX\_HP29

| #define UART0\_RX\_HP29   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(2, 0xFF, 0, 1, 13, 0) |
| --- |

## [◆ ](#a7c3b4144654fe9a24db90b57998e4cb4)UART0\_RX\_HP55

| #define UART0\_RX\_HP55   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(2, 0xFF, 19, 3, 7, 0) |
| --- |

## [◆ ](#ae6d9c15cfc89ceb5d8ad3d2b5a7756c7)UART0\_RX\_ULP1

| #define UART0\_RX\_ULP1   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(2, 6, 23, 4, 1, 1) |
| --- |

## [◆ ](#a27cb5f1b5a7d5798fb219c3a6659acb6)UART0\_RX\_ULP6

| #define UART0\_RX\_ULP6   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(4, 6, 28, 4, 6, 6) |
| --- |

## [◆ ](#a310df59fe4dc6cf528b1bafe00c41c7a)UART0\_TX\_HP30

| #define UART0\_TX\_HP30   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(2, 0xFF, 0, 1, 14, 0) |
| --- |

## [◆ ](#a913663cca98288505e45479c213ea0d0)UART0\_TX\_HP54

| #define UART0\_TX\_HP54   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(2, 0xFF, 18, 3, 6, 0) |
| --- |

## [◆ ](#a4d763a3c1a9bf10f42187482c5a2ba34)UART0\_TX\_ULP4

| #define UART0\_TX\_ULP4   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(2, 6, 26, 4, 4, 4) |
| --- |

## [◆ ](#a8fd486e3b0c02b1f578a38e1d6c30a38)UART0\_TX\_ULP7

| #define UART0\_TX\_ULP7   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(4, 6, 29, 4, 7, 7) |
| --- |

## [◆ ](#a4ca4f60081c355860a6a10bfa428bc98)UART1\_CTS\_HP11

| #define UART1\_CTS\_HP11   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(6, 0xFF, 6, 0, 11, 0) |
| --- |

## [◆ ](#a1782fbe55aa8e6f8bd75da573c755223)UART1\_CTS\_HP32

| #define UART1\_CTS\_HP32   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(12, 0xFF, 9, 2, 0, 0) |
| --- |

## [◆ ](#a66ca158c30cc3087b3ae12824e86398f)UART1\_CTS\_HP51

| #define UART1\_CTS\_HP51   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(9, 0xFF, 15, 3, 3, 0) |
| --- |

## [◆ ](#aa8245d65007636996d67ca46d5c5a9fd)UART1\_CTS\_ULP1

| #define UART1\_CTS\_ULP1   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(9, 6, 23, 4, 1, 1) |
| --- |

## [◆ ](#a281ee7fbfe1a8ee2814d0f6ba60e61f6)UART1\_CTS\_ULP7

| #define UART1\_CTS\_ULP7   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(6, 6, 29, 4, 7, 7) |
| --- |

## [◆ ](#a7ddce4735336b046b99dcee26d4f90c3)UART1\_CTS\_ULP9

| #define UART1\_CTS\_ULP9   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(9, 6, 31, 4, 9, 9) |
| --- |

## [◆ ](#aea42cf6a2a432628bf19d6a0529121bb)UART1\_RS485DE\_HP9

| #define UART1\_RS485DE\_HP9   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(6, 0xFF, 4, 0, 9, 0) |
| --- |

## [◆ ](#ad04deb098006e6608ddee97489cb3eec)UART1\_RS485DE\_ULP11

| #define UART1\_RS485DE\_ULP11   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(6, 6, 33, 4, 11, 11) |
| --- |

## [◆ ](#ad70a39337d9aab0d303aa47dc6706d01)UART1\_RS485DE\_ULP2

| #define UART1\_RS485DE\_ULP2   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(6, 6, 24, 4, 2, 2) |
| --- |

## [◆ ](#a949839fcdd556be94b8ffec9e32cb8d7)UART1\_RS485EN\_HP12

| #define UART1\_RS485EN\_HP12   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(6, 0xFF, 7, 0, 12, 0) |
| --- |

## [◆ ](#abd3dfcedbb2108b5097c769ade994f26)UART1\_RS485EN\_HP26

| #define UART1\_RS485EN\_HP26   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(6, 0xFF, 0, 1, 10, 0) |
| --- |

## [◆ ](#a8b90c76a3932164295fd126af60be1fd)UART1\_RS485EN\_ULP0

| #define UART1\_RS485EN\_ULP0   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(6, 6, 22, 4, 0, 0) |
| --- |

## [◆ ](#a90f57369d21e5c139b73a07d377a8cf2)UART1\_RS485RE\_HP8

| #define UART1\_RS485RE\_HP8   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(6, 0xFF, 3, 0, 8, 0) |
| --- |

## [◆ ](#a8407e33974cd85b26ad17b6e489bef67)UART1\_RS485RE\_ULP1

| #define UART1\_RS485RE\_ULP1   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(6, 6, 23, 4, 1, 1) |
| --- |

## [◆ ](#a310f189ae26d3412769346ea2f506a1b)UART1\_RS485RE\_ULP10

| #define UART1\_RS485RE\_ULP10   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(6, 6, 32, 4, 10, 10) |
| --- |

## [◆ ](#abb746abdce4e30129782624ec53fffc8)UART1\_RTS\_HP10

| #define UART1\_RTS\_HP10   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(6, 0xFF, 5, 0, 10, 0) |
| --- |

## [◆ ](#a70a72361b31640d41a6e2412ac923c9d)UART1\_RTS\_HP27

| #define UART1\_RTS\_HP27   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(6, 0xFF, 0, 1, 11, 0) |
| --- |

## [◆ ](#a230298f5a4c4c180cf1940e3416b47f6)UART1\_RTS\_HP28

| #define UART1\_RTS\_HP28   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(6, 0xFF, 0, 1, 12, 0) |
| --- |

## [◆ ](#a88ddaa52e9b50c54136234aa558bdfb1)UART1\_RTS\_HP31

| #define UART1\_RTS\_HP31   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(12, 0xFF, 9, 1, 15, 0) |
| --- |

## [◆ ](#a6d7d1bcf7f58d024e5a99328b6150a63)UART1\_RTS\_HP50

| #define UART1\_RTS\_HP50   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(9, 0xFF, 14, 3, 2, 0) |
| --- |

## [◆ ](#a1f1b7f47f6b95d512f6f0a985e81946f)UART1\_RTS\_ULP0

| #define UART1\_RTS\_ULP0   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(9, 6, 22, 4, 0, 0) |
| --- |

## [◆ ](#abf9c83a461eb53b37f46abf8c8d8d196)UART1\_RTS\_ULP6

| #define UART1\_RTS\_ULP6   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(6, 6, 28, 4, 6, 6) |
| --- |

## [◆ ](#a4fb7d994478de8f966e5cc655d8e973d)UART1\_RTS\_ULP8

| #define UART1\_RTS\_ULP8   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(9, 6, 30, 4, 8, 8) |
| --- |

## [◆ ](#a3592a61447450351c3d3c3a55a3bdace)UART1\_RX\_HP29

| #define UART1\_RX\_HP29   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(6, 0xFF, 0, 1, 13, 0) |
| --- |

## [◆ ](#a5b5e71f38f9a796de10379f187ca7f15)UART1\_RX\_HP33

| #define UART1\_RX\_HP33   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(12, 0xFF, 9, 2, 1, 0) |
| --- |

## [◆ ](#a953fa739896ecddf271f7c3339fa6073)UART1\_RX\_HP6

| #define UART1\_RX\_HP6   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(6, 0xFF, 1, 0, 6, 0) |
| --- |

## [◆ ](#ad3e21323e8a22d14b6aacd4357362a33)UART1\_RX\_ULP10

| #define UART1\_RX\_ULP10   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(9, 6, 32, 4, 10, 10) |
| --- |

## [◆ ](#a87501d9f4180905852e78361fc0f426f)UART1\_RX\_ULP2

| #define UART1\_RX\_ULP2   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(9, 6, 24, 4, 1, 1) |
| --- |

## [◆ ](#a4fea2b8bd8a2d3eab03cace6b258b143)UART1\_RX\_ULP4

| #define UART1\_RX\_ULP4   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(6, 6, 26, 4, 4, 4) |
| --- |

## [◆ ](#ab707a4b932d6f09f162ae6d1567458d1)UART1\_RX\_ULP8

| #define UART1\_RX\_ULP8   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(6, 6, 30, 4, 8, 8) |
| --- |

## [◆ ](#ae40a1f641b32672f3e82ed37249d75af)UART1\_TX\_HP15

| #define UART1\_TX\_HP15   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(2, 0xFF, 8, 0, 15, 0) |
| --- |

## [◆ ](#a64965fbfeb33a6ed5454093b4bffb27d)UART1\_TX\_HP30

| #define UART1\_TX\_HP30   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(6, 0xFF, 0, 1, 14, 0) |
| --- |

## [◆ ](#acdf09abb21a7b70d6672291d7a84414c)UART1\_TX\_HP34

| #define UART1\_TX\_HP34   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(12, 0xFF, 9, 2, 2, 0) |
| --- |

## [◆ ](#a67757e78eacd012fd699e6d212f20a54)UART1\_TX\_HP7

| #define UART1\_TX\_HP7   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(6, 0xFF, 2, 0, 7, 0) |
| --- |

## [◆ ](#a243b96ad4d1fd865f1ddbdf5174b2a69)UART1\_TX\_ULP11

| #define UART1\_TX\_ULP11   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(9, 6, 33, 4, 11, 11) |
| --- |

## [◆ ](#ae4b6add65671db28cc0647d21cff499d)UART1\_TX\_ULP3

| #define UART1\_TX\_ULP3   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(9, 6, 25, 4, 1, 1) |
| --- |

## [◆ ](#ac68f74cffa2daadef2c11ab076d8be97)UART1\_TX\_ULP5

| #define UART1\_TX\_ULP5   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(6, 6, 27, 4, 5, 5) |
| --- |

## [◆ ](#aa46a2a94478eb8551b21373bbce52824)UART1\_TX\_ULP9

| #define UART1\_TX\_ULP9   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(6, 6, 31, 4, 9, 9) |
| --- |

## [◆ ](#a7275562850ca4f6089036c09eebf8c80)ULPI2C\_SCL\_HP11

| #define ULPI2C\_SCL\_HP11   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(9, 4, 6, 0, 11, 5) |
| --- |

## [◆ ](#a38bcacc0080286a4373315a53d38e3b8)ULPI2C\_SCL\_HP15

| #define ULPI2C\_SCL\_HP15   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(9, 4, 8, 0, 15, 7) |
| --- |

## [◆ ](#a2afc4d25f6b760816fa8f9a959864231)ULPI2C\_SCL\_HP26

| #define ULPI2C\_SCL\_HP26   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(11, 4, 0, 1, 10, 7) |
| --- |

## [◆ ](#aa2d6230cf2154aca73c36bdd7645ffb6)ULPI2C\_SCL\_HP27

| #define ULPI2C\_SCL\_HP27   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(11, 4, 0, 1, 11, 8) |
| --- |

## [◆ ](#ac99c9cd0c12ba6effb933aebb04e366c)ULPI2C\_SCL\_HP46

| #define ULPI2C\_SCL\_HP46   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(9, 4, 10, 2, 14, 8) |
| --- |

## [◆ ](#a6e76fdfeea3d20133c141d86d48edb16)ULPI2C\_SCL\_HP7

| #define ULPI2C\_SCL\_HP7   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(9, 4, 2, 0, 7, 1) |
| --- |

## [◆ ](#aad197f3c66cfafe58e1c220a1017e8ac)ULPI2C\_SCL\_ULP1

| #define ULPI2C\_SCL\_ULP1   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(0xFF, 4, 0xFF, 4, 0, 1) |
| --- |

## [◆ ](#a3e08531523a985f0dbb68528551dace3)ULPI2C\_SCL\_ULP5

| #define ULPI2C\_SCL\_ULP5   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(0xFF, 4, 0xFF, 4, 0, 5) |
| --- |

## [◆ ](#ae23c01c208d25b7adff61126cd8a9bb9)ULPI2C\_SCL\_ULP7

| #define ULPI2C\_SCL\_ULP7   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(0xFF, 4, 0xFF, 4, 0, 7) |
| --- |

## [◆ ](#aa09786d189d39bae438faaeac7e7ea40)ULPI2C\_SCL\_ULP8

| #define ULPI2C\_SCL\_ULP8   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(0xFF, 4, 0xFF, 4, 0, 8) |
| --- |

## [◆ ](#ae0c5b9e4954a0e07a299e2b8ba36e6b7)ULPI2C\_SDA\_HP10

| #define ULPI2C\_SDA\_HP10   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(9, 4, 5, 0, 10, 4) |
| --- |

## [◆ ](#a82b2a9b7bb330cfde26d1e111bfc47d7)ULPI2C\_SDA\_HP12

| #define ULPI2C\_SDA\_HP12   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(9, 4, 7, 0, 12, 6) |
| --- |

## [◆ ](#afc9e45ece6272ec2f02dad394f17fc30)ULPI2C\_SDA\_HP25

| #define ULPI2C\_SDA\_HP25   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(11, 4, 0, 1, 9, 6) |
| --- |

## [◆ ](#a883987f33b163bbc8fb28990795a9935)ULPI2C\_SDA\_HP28

| #define ULPI2C\_SDA\_HP28   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(11, 4, 0, 1, 12, 9) |
| --- |

## [◆ ](#a803522e6dfd39e6f5233663ca18da82b)ULPI2C\_SDA\_HP30

| #define ULPI2C\_SDA\_HP30   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(11, 4, 0, 1, 14, 11) |
| --- |

## [◆ ](#a81cbbbcb500051df8654b0150eb8d43d)ULPI2C\_SDA\_HP47

| #define ULPI2C\_SDA\_HP47   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(9, 4, 11, 2, 15, 9) |
| --- |

## [◆ ](#a89150a67ce005b8c9e9b73aa0881bdce)ULPI2C\_SDA\_HP49

| #define ULPI2C\_SDA\_HP49   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(9, 4, 13, 3, 1, 11) |
| --- |

## [◆ ](#abd8259056eed0e5d70592f9fb8095729)ULPI2C\_SDA\_HP6

| #define ULPI2C\_SDA\_HP6   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(9, 4, 1, 0, 6, 0) |
| --- |

## [◆ ](#a683eac0b53a4a91c74c576b4f55a14c7)ULPI2C\_SDA\_ULP0

| #define ULPI2C\_SDA\_ULP0   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(0xFF, 4, 0xFF, 4, 0, 0) |
| --- |

## [◆ ](#a13be1329e1ed09001541f213841fa388)ULPI2C\_SDA\_ULP11

| #define ULPI2C\_SDA\_ULP11   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(0xFF, 4, 0xFF, 4, 0, 11) |
| --- |

## [◆ ](#a93cb9256a344d3e3c9e99f52512ea496)ULPI2C\_SDA\_ULP4

| #define ULPI2C\_SDA\_ULP4   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(0xFF, 4, 0xFF, 4, 0, 4) |
| --- |

## [◆ ](#a2bd7f63711f414953c3028e2c46e8713)ULPI2C\_SDA\_ULP6

| #define ULPI2C\_SDA\_ULP6   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(0xFF, 4, 0xFF, 4, 0, 6) |
| --- |

## [◆ ](#ab7ea0a99e98ac51c77077d342944342d)ULPI2C\_SDA\_ULP9

| #define ULPI2C\_SDA\_ULP9   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(0xFF, 4, 0xFF, 4, 0, 9) |
| --- |

## [◆ ](#a85b6b3979b28967d77bce8f46484afb9)ULPI2S\_CLK\_HP15

| #define ULPI2S\_CLK\_HP15   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(9, 2, 8, 0, 15, 7) |
| --- |

## [◆ ](#aa8fb24f7b22ddd58b12e72c3151061ce)ULPI2S\_CLK\_HP26

| #define ULPI2S\_CLK\_HP26   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(11, 2, 0, 1, 10, 7) |
| --- |

## [◆ ](#adfb54219b4ab1a7587f515246b3fa755)ULPI2S\_CLK\_HP27

| #define ULPI2S\_CLK\_HP27   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(11, 2, 0, 1, 11, 8) |
| --- |

## [◆ ](#a7750b3caaf5ebbb795da513cbebf8859)ULPI2S\_CLK\_HP46

| #define ULPI2S\_CLK\_HP46   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(9, 2, 10, 2, 14, 8) |
| --- |

## [◆ ](#af052bd9fc2183d48ff37b2c5bebe7f49)ULPI2S\_CLK\_ULP7

| #define ULPI2S\_CLK\_ULP7   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(0xFF, 2, 0xFF, 4, 0, 7) |
| --- |

## [◆ ](#a4d5eb6ab5c39069f6dcadd1b0bf61b59)ULPI2S\_CLK\_ULP8

| #define ULPI2S\_CLK\_ULP8   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(0xFF, 2, 0xFF, 4, 0, 8) |
| --- |

## [◆ ](#a5664aa96cc1cf08181678d30c31e9349)ULPI2S\_DIN\_HP12

| #define ULPI2S\_DIN\_HP12   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(9, 2, 7, 0, 12, 6) |
| --- |

## [◆ ](#a721d372c3992adb29e36a111e3394228)ULPI2S\_DIN\_HP25

| #define ULPI2S\_DIN\_HP25   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(11, 2, 0, 1, 9, 6) |
| --- |

## [◆ ](#af180c73151f01717b2f9aaecf2ed1efc)ULPI2S\_DIN\_HP28

| #define ULPI2S\_DIN\_HP28   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(11, 2, 0, 1, 12, 9) |
| --- |

## [◆ ](#a7e072f27104474717da3dbc2e2399ce2)ULPI2S\_DIN\_HP47

| #define ULPI2S\_DIN\_HP47   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(9, 2, 11, 2, 15, 9) |
| --- |

## [◆ ](#ab555c9e9e0732372d353cd0ae0ebdd22)ULPI2S\_DIN\_HP6

| #define ULPI2S\_DIN\_HP6   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(9, 2, 1, 0, 6, 0) |
| --- |

## [◆ ](#a97cbfeb16a7c46e12eae6891bc037acd)ULPI2S\_DIN\_ULP0

| #define ULPI2S\_DIN\_ULP0   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(0xFF, 2, 0xFF, 4, 0, 0) |
| --- |

## [◆ ](#aaf31db6c31214cc2c80cb309bdea5536)ULPI2S\_DIN\_ULP6

| #define ULPI2S\_DIN\_ULP6   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(0xFF, 2, 0xFF, 4, 0, 6) |
| --- |

## [◆ ](#ad2907e564c41e33f35c5d031b0405142)ULPI2S\_DIN\_ULP9

| #define ULPI2S\_DIN\_ULP9   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(0xFF, 2, 0xFF, 4, 0, 9) |
| --- |

## [◆ ](#aa2d709ee468354d27c23b443d72ae707)ULPI2S\_DOUT\_HP11

| #define ULPI2S\_DOUT\_HP11   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(9, 2, 6, 0, 11, 5) |
| --- |

## [◆ ](#a2d914f5db178a90759278e016ed3cd6b)ULPI2S\_DOUT\_HP30

| #define ULPI2S\_DOUT\_HP30   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(11, 2, 0, 1, 14, 11) |
| --- |

## [◆ ](#a5a77eb00dec4d187575081efceed70a0)ULPI2S\_DOUT\_HP49

| #define ULPI2S\_DOUT\_HP49   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(9, 2, 13, 3, 1, 11) |
| --- |

## [◆ ](#a26ed645c0e1e4dd60a2ffaa670a30308)ULPI2S\_DOUT\_HP7

| #define ULPI2S\_DOUT\_HP7   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(9, 2, 2, 0, 7, 1) |
| --- |

## [◆ ](#ab1a08eb6deb7154ef3b27aed5840f1c4)ULPI2S\_DOUT\_ULP1

| #define ULPI2S\_DOUT\_ULP1   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(0xFF, 2, 0xFF, 4, 0, 1) |
| --- |

## [◆ ](#abf0c090bf283519422369f8cd6641155)ULPI2S\_DOUT\_ULP11

| #define ULPI2S\_DOUT\_ULP11   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(0xFF, 2, 0xFF, 4, 0, 11) |
| --- |

## [◆ ](#adb3fcaf4510f3e9e92d6b6938d5aa4b8)ULPI2S\_DOUT\_ULP5

| #define ULPI2S\_DOUT\_ULP5   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(0xFF, 2, 0xFF, 4, 0, 5) |
| --- |

## [◆ ](#abdc82667b8b9f52c5d7cd400ff539239)ULPI2S\_WS\_HP10

| #define ULPI2S\_WS\_HP10   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(9, 2, 5, 0, 10, 4) |
| --- |

## [◆ ](#af2fee1bd924e2cb917c7448a961c3de9)ULPI2S\_WS\_HP29

| #define ULPI2S\_WS\_HP29   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(11, 2, 0, 1, 13, 10) |
| --- |

## [◆ ](#a432d784fa10f64d474034b5f30e4849c)ULPI2S\_WS\_HP48

| #define ULPI2S\_WS\_HP48   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(9, 2, 12, 3, 0, 10) |
| --- |

## [◆ ](#ac54fc86fa7f49011d07fb39cdf074788)ULPI2S\_WS\_HP8

| #define ULPI2S\_WS\_HP8   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(9, 2, 3, 0, 8, 2) |
| --- |

## [◆ ](#a6990494758f0d836d985baf113547d44)ULPI2S\_WS\_ULP10

| #define ULPI2S\_WS\_ULP10   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(0xFF, 2, 0xFF, 4, 0, 10) |
| --- |

## [◆ ](#a2a27e527e270fc114138715ce610f270)ULPI2S\_WS\_ULP2

| #define ULPI2S\_WS\_ULP2   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(0xFF, 2, 0xFF, 4, 0, 2) |
| --- |

## [◆ ](#a914dbc1a9d523e19f639ef063aeb4dfe)ULPI2S\_WS\_ULP4

| #define ULPI2S\_WS\_ULP4   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(0xFF, 2, 0xFF, 4, 0, 4) |
| --- |

## [◆ ](#a13792f9c1d0b86e83e420ba40aabdd02)ULPSSI\_CLK\_HP27

| #define ULPSSI\_CLK\_HP27   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(11, 1, 0, 1, 11, 8) |
| --- |

## [◆ ](#a973efb6759449cd13223fd679f795d50)ULPSSI\_CLK\_HP46

| #define ULPSSI\_CLK\_HP46   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(9, 1, 10, 2, 14, 8) |
| --- |

## [◆ ](#aa4f4246951880a5d5b0f666e055fdd68)ULPSSI\_CLK\_HP6

| #define ULPSSI\_CLK\_HP6   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(9, 1, 1, 0, 6, 0) |
| --- |

## [◆ ](#a3933d5b6f5464e2a22f466797725f5be)ULPSSI\_CLK\_ULP0

| #define ULPSSI\_CLK\_ULP0   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(0xFF, 1, 0xFF, 4, 0, 0) |
| --- |

## [◆ ](#ae811c5ecd3838c77460fafb9a47dc218)ULPSSI\_CLK\_ULP4

| #define ULPSSI\_CLK\_ULP4   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(0xFF, 8, 0xFF, 4, 0, 4) |
| --- |

## [◆ ](#ac1d6aedfec07ef370da615708fa5c98b)ULPSSI\_CLK\_ULP8

| #define ULPSSI\_CLK\_ULP8   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(0xFF, 1, 0xFF, 4, 0, 8) |
| --- |

## [◆ ](#ae75cc90a153a1c90f7fbb0c7893558d0)ULPSSI\_CS0\_HP29

| #define ULPSSI\_CS0\_HP29   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(11, 1, 0, 1, 13, 10) |
| --- |

## [◆ ](#adfc8f3cf729bb76128de18eabd7d877a)ULPSSI\_CS0\_HP48

| #define ULPSSI\_CS0\_HP48   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(9, 1, 12, 3, 0, 10) |
| --- |

## [◆ ](#ae696d20e5ada658753a81995c196343f)ULPSSI\_CS0\_ULP10

| #define ULPSSI\_CS0\_ULP10   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(0xFF, 1, 0xFF, 4, 0, 10) |
| --- |

## [◆ ](#aa8a8db9123876f6228cf83ff617d7fbb)ULPSSI\_CS0\_ULP7

| #define ULPSSI\_CS0\_ULP7   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(0xFF, 8, 0xFF, 4, 0, 7) |
| --- |

## [◆ ](#ad1e8bb7ce27179dfadac4836b9a26924)ULPSSI\_CS1\_HP10

| #define ULPSSI\_CS1\_HP10   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(9, 1, 5, 0, 10, 4) |
| --- |

## [◆ ](#abcb850de6adc5db558bb9cb8a45455a6)ULPSSI\_CS1\_ULP4

| #define ULPSSI\_CS1\_ULP4   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(0xFF, 1, 0xFF, 4, 0, 4) |
| --- |

## [◆ ](#aa53895ddaa78b38c7ea5b35d6f00c78f)ULPSSI\_CS2\_HP12

| #define ULPSSI\_CS2\_HP12   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(9, 1, 7, 0, 12, 6) |
| --- |

## [◆ ](#ac537683d973832982d538a2e3a705f7c)ULPSSI\_CS2\_HP25

| #define ULPSSI\_CS2\_HP25   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(11, 1, 0, 1, 9, 6) |
| --- |

## [◆ ](#a3ddbf1e40ddfb1844a7c486b3d47a8fe)ULPSSI\_CS2\_ULP6

| #define ULPSSI\_CS2\_ULP6   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(0xFF, 1, 0xFF, 4, 0, 6) |
| --- |

## [◆ ](#a9d01d993af06027e11d1a2c2abd1505a)ULPSSI\_DIN\_HP28

| #define ULPSSI\_DIN\_HP28   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(11, 1, 0, 1, 12, 9) |
| --- |

## [◆ ](#a6ffab07aba4ddfa977a8865230c35309)ULPSSI\_DIN\_HP47

| #define ULPSSI\_DIN\_HP47   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(9, 1, 11, 2, 15, 9) |
| --- |

## [◆ ](#a00b7649bb95375d2a8632938c1ab2fd8)ULPSSI\_DIN\_HP8

| #define ULPSSI\_DIN\_HP8   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(9, 1, 3, 0, 8, 2) |
| --- |

## [◆ ](#a8a35f9ed548c01693de57b6647a55901)ULPSSI\_DIN\_ULP2

| #define ULPSSI\_DIN\_ULP2   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(0xFF, 1, 0xFF, 4, 0, 2) |
| --- |

## [◆ ](#a3737184b07cd6dfdef580a82b31ad13c)ULPSSI\_DIN\_ULP6

| #define ULPSSI\_DIN\_ULP6   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(0xFF, 8, 0xFF, 4, 0, 6) |
| --- |

## [◆ ](#a841bd6d9d7b267db55b85dbd63c29f19)ULPSSI\_DIN\_ULP9

| #define ULPSSI\_DIN\_ULP9   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(0xFF, 1, 0xFF, 4, 0, 9) |
| --- |

## [◆ ](#ab90410cbd5d7feccc31c858dcea5ce24)ULPSSI\_DOUT\_HP30

| #define ULPSSI\_DOUT\_HP30   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(11, 1, 0, 1, 14, 11) |
| --- |

## [◆ ](#a5c0d9281a0eae7e3f71c7622f0fcb0ca)ULPSSI\_DOUT\_HP49

| #define ULPSSI\_DOUT\_HP49   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(9, 1, 13, 3, 1, 11) |
| --- |

## [◆ ](#a7f72ea03a247002a88d22afa4d41f4eb)ULPSSI\_DOUT\_HP7

| #define ULPSSI\_DOUT\_HP7   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(9, 1, 2, 0, 7, 1) |
| --- |

## [◆ ](#a7c49826415618d0edb0bf9960ab1390a)ULPSSI\_DOUT\_ULP1

| #define ULPSSI\_DOUT\_ULP1   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(0xFF, 1, 0xFF, 4, 0, 1) |
| --- |

## [◆ ](#ae74ef587f76251d995250141665e0691)ULPSSI\_DOUT\_ULP11

| #define ULPSSI\_DOUT\_ULP11   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(0xFF, 1, 0xFF, 4, 0, 11) |
| --- |

## [◆ ](#a3936c932181d9601015bfcd9ddbd9230)ULPSSI\_DOUT\_ULP5

| #define ULPSSI\_DOUT\_ULP5   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(0xFF, 8, 0xFF, 4, 0, 5) |
| --- |

## [◆ ](#aa9a3840c4d145ad867c1e59cf988d74a)ULPUART\_CTS\_HP11

| #define ULPUART\_CTS\_HP11   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(9, 3, 6, 0, 11, 5) |
| --- |

## [◆ ](#a6fa2d64e1f638a6e0a7df29a4476da03)ULPUART\_CTS\_HP27

| #define ULPUART\_CTS\_HP27   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(11, 3, 0, 1, 11, 8) |
| --- |

## [◆ ](#a8ae6905ee86208cfc8910d8cff7423cf)ULPUART\_CTS\_HP46

| #define ULPUART\_CTS\_HP46   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(9, 3, 10, 2, 14, 8) |
| --- |

## [◆ ](#a7be14c47047f63a0f72b9508fb45dcb8)ULPUART\_CTS\_HP7

| #define ULPUART\_CTS\_HP7   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(9, 3, 2, 0, 7, 1) |
| --- |

## [◆ ](#acecb9492723712365609fe03429ecc62)ULPUART\_CTS\_ULP1

| #define ULPUART\_CTS\_ULP1   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(0xFF, 3, 0xFF, 4, 0, 1) |
| --- |

## [◆ ](#a47991853f93de832cb85dba3dd51d689)ULPUART\_CTS\_ULP5

| #define ULPUART\_CTS\_ULP5   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(0xFF, 3, 0xFF, 4, 0, 5) |
| --- |

## [◆ ](#ad87a42b5cac9d4e3e1539963c0a153ac)ULPUART\_CTS\_ULP8

| #define ULPUART\_CTS\_ULP8   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(0xFF, 3, 0xFF, 4, 0, 8) |
| --- |

## [◆ ](#ad25318e8c8da760aca964a06c8114f3e)ULPUART\_RTS\_HP10

| #define ULPUART\_RTS\_HP10   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(9, 3, 5, 0, 10, 4) |
| --- |

## [◆ ](#a45126e5a5d74c85e34beede737a6c266)ULPUART\_RTS\_HP29

| #define ULPUART\_RTS\_HP29   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(11, 3, 0, 1, 13, 10) |
| --- |

## [◆ ](#a0fd57249b5cdaa83d1a82d96f39bfcac)ULPUART\_RTS\_HP48

| #define ULPUART\_RTS\_HP48   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(9, 3, 12, 3, 0, 10) |
| --- |

## [◆ ](#a3aa724f39856848fe3616dc2c7e0f9d5)ULPUART\_RTS\_HP6

| #define ULPUART\_RTS\_HP6   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(9, 3, 1, 0, 6, 0) |
| --- |

## [◆ ](#a6d637af94f43cbfcfd001b174d89504e)ULPUART\_RTS\_ULP0

| #define ULPUART\_RTS\_ULP0   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(0xFF, 3, 0xFF, 4, 0, 0) |
| --- |

## [◆ ](#aafec5377fdddad88eaa5f33a616e932a)ULPUART\_RTS\_ULP10

| #define ULPUART\_RTS\_ULP10   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(0xFF, 3, 0xFF, 4, 0, 10) |
| --- |

## [◆ ](#a905bfb63ed0825940db94f2d0e339cae)ULPUART\_RTS\_ULP4

| #define ULPUART\_RTS\_ULP4   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(0xFF, 3, 0xFF, 4, 0, 4) |
| --- |

## [◆ ](#a95f0434e7aa29f3f3b8870a8f56df169)ULPUART\_RX\_HP12

| #define ULPUART\_RX\_HP12   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(9, 3, 7, 0, 12, 6) |
| --- |

## [◆ ](#a17fa934bc15ff31389466f0906291c95)ULPUART\_RX\_HP25

| #define ULPUART\_RX\_HP25   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(11, 3, 0, 1, 9, 6) |
| --- |

## [◆ ](#afde64cb335752ffd591ddeb40f2d24b0)ULPUART\_RX\_HP28

| #define ULPUART\_RX\_HP28   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(11, 3, 0, 1, 12, 9) |
| --- |

## [◆ ](#a497302eeb072e2573948fd36b246824e)ULPUART\_RX\_HP47

| #define ULPUART\_RX\_HP47   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(9, 3, 11, 2, 15, 9) |
| --- |

## [◆ ](#a7e24d72b3f26b6a64d1182b223a679a5)ULPUART\_RX\_HP8

| #define ULPUART\_RX\_HP8   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(9, 3, 3, 0, 8, 2) |
| --- |

## [◆ ](#a5c296e125433a81362d207042b30cb7e)ULPUART\_RX\_ULP2

| #define ULPUART\_RX\_ULP2   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(0xFF, 3, 0xFF, 4, 0, 2) |
| --- |

## [◆ ](#a1036c7686c6ae59e387bf0df9338d8f6)ULPUART\_RX\_ULP6

| #define ULPUART\_RX\_ULP6   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(0xFF, 3, 0xFF, 4, 0, 6) |
| --- |

## [◆ ](#a3b868b8418ed39e8251a6d5e06da25ec)ULPUART\_RX\_ULP9

| #define ULPUART\_RX\_ULP9   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(0xFF, 3, 0xFF, 4, 0, 9) |
| --- |

## [◆ ](#af7d1211f086a8be91e95e88e1bcee555)ULPUART\_TX\_HP15

| #define ULPUART\_TX\_HP15   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(9, 3, 8, 0, 15, 7) |
| --- |

## [◆ ](#a02c5645af20a73c856a0e7dcbf30e45a)ULPUART\_TX\_HP26

| #define ULPUART\_TX\_HP26   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(11, 3, 0, 1, 10, 7) |
| --- |

## [◆ ](#ace2f51ab67c116751656f1421bac3db9)ULPUART\_TX\_HP30

| #define ULPUART\_TX\_HP30   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(11, 3, 0, 1, 14, 11) |
| --- |

## [◆ ](#a8974ff95ea2efd59e1f2d16a7322f75c)ULPUART\_TX\_HP49

| #define ULPUART\_TX\_HP49   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(9, 3, 13, 3, 1, 11) |
| --- |

## [◆ ](#a11b4b4459ff2d94267bca669da7e17cc)ULPUART\_TX\_ULP11

| #define ULPUART\_TX\_ULP11   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(0xFF, 3, 0xFF, 4, 0, 11) |
| --- |

## [◆ ](#a306f5e9ad2e84cee1074067cd6bccb4f)ULPUART\_TX\_ULP7

| #define ULPUART\_TX\_ULP7   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(0xFF, 3, 0xFF, 4, 0, 7) |
| --- |

## [◆ ](#a02c45c292ebe276e4f41101d7440480f)UULP\_GPIO4\_ULP2

| #define UULP\_GPIO4\_ULP2   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(0xFF, 4, 0xFF, 4, 0, 2) |
| --- |

## [◆ ](#a003329462614c9ff939c451c28a011bc)UULP\_TESTMODE0\_ULP7

| #define UULP\_TESTMODE0\_ULP7   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(0xFF, 11, 0xFF, 4, 0, 7) |
| --- |

## [◆ ](#aa927ee96be06692b7fecb88eec152357)UULP\_TESTMODE0\_ULP9

| #define UULP\_TESTMODE0\_ULP9   [SIWX91X\_GPIO](silabs-pinctrl-siwx91x_8h.md#a34a2f79af3f9aa9c434bb25c0c711d97)(0xFF, 5, 0xFF, 4, 0, 9) |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [pinctrl](dir_2c6c4fbd167577104b7f1b7148586168.md)
- [silabs](dir_fa47ec1716313d52a64832478c9daea4.md)
- [siwx91x-pinctrl.h](siwx91x-pinctrl_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
