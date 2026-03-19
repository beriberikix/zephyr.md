---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/pinctrl-r8a77961_8h_source.html
original_path: doxygen/html/pinctrl-r8a77961_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

pinctrl-r8a77961.h

[Go to the documentation of this file.](pinctrl-r8a77961_8h.md)

1/\*

2 \* Copyright (c) 2021 IoT.bzh

3 \* Copyright (c) 2023-2024 EPAM Systems

4 \*

5 \* SPDX-License-Identifier: Apache-2.0

6 \*/

7#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_PINCTRL\_RENESAS\_PINCTRL\_R8A77961\_H\_

8#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_PINCTRL\_RENESAS\_PINCTRL\_R8A77961\_H\_

9

10#include "[pinctrl-rcar-common.h](pinctrl-rcar-common_8h.md)"

11

12/\* Pins declaration \*/

[ 13](pinctrl-r8a77961_8h.md#a61ae8c246db04e2ac956ccf175b217c6)#define PIN\_NONE -1

[ 14](pinctrl-r8a77961_8h.md#abc8ccae9fc19948429c16d09ee3fae0d)#define PIN\_D0 RCAR\_GP\_PIN(0, 0)

[ 15](pinctrl-r8a77961_8h.md#a744f3ba3909505a1fac25934b9dc9d37)#define PIN\_D1 RCAR\_GP\_PIN(0, 1)

[ 16](pinctrl-r8a77961_8h.md#ac2cafd248e396fa37e5a45ff84dc5653)#define PIN\_D2 RCAR\_GP\_PIN(0, 2)

[ 17](pinctrl-r8a77961_8h.md#a48857997ca2522562f4a68fe9b818a44)#define PIN\_D3 RCAR\_GP\_PIN(0, 3)

[ 18](pinctrl-r8a77961_8h.md#a7d43c81e95b17b24c58423ee546648d6)#define PIN\_D4 RCAR\_GP\_PIN(0, 4)

[ 19](pinctrl-r8a77961_8h.md#a4a9e1c206912eb8b451f92ef3de70103)#define PIN\_D5 RCAR\_GP\_PIN(0, 5)

[ 20](pinctrl-r8a77961_8h.md#aade120add55df7120080c17812b9aed4)#define PIN\_D6 RCAR\_GP\_PIN(0, 6)

[ 21](pinctrl-r8a77961_8h.md#a07b5ac045e5a43186827d1255b3a063e)#define PIN\_D7 RCAR\_GP\_PIN(0, 7)

[ 22](pinctrl-r8a77961_8h.md#a14be9e492250b7ded1c59713c47be2fc)#define PIN\_D8 RCAR\_GP\_PIN(0, 8)

[ 23](pinctrl-r8a77961_8h.md#af5b9672b382f24cb3adf6bc52301c49d)#define PIN\_D9 RCAR\_GP\_PIN(0, 9)

[ 24](pinctrl-r8a77961_8h.md#a4724ccf2ae2b09e7e95d0da6ba8b2873)#define PIN\_D10 RCAR\_GP\_PIN(0, 10)

[ 25](pinctrl-r8a77961_8h.md#ac856af59c2f4e029aeb8713d07fb28f1)#define PIN\_D11 RCAR\_GP\_PIN(0, 11)

[ 26](pinctrl-r8a77961_8h.md#a36d0b9ab3a8ac62a041227bfaa51bdf1)#define PIN\_D12 RCAR\_GP\_PIN(0, 12)

[ 27](pinctrl-r8a77961_8h.md#aee414179fe341ad8167490099a669dc5)#define PIN\_D13 RCAR\_GP\_PIN(0, 13)

[ 28](pinctrl-r8a77961_8h.md#a10493aca9f30693fb3abb9f981b9a1d6)#define PIN\_D14 RCAR\_GP\_PIN(0, 14)

[ 29](pinctrl-r8a77961_8h.md#a224278de977ca666931b600349cac37e)#define PIN\_D15 RCAR\_GP\_PIN(0, 15)

[ 30](pinctrl-r8a77961_8h.md#ad3a64360b1623d5314cbb8999cb86f99)#define PIN\_A0 RCAR\_GP\_PIN(1, 0)

[ 31](pinctrl-r8a77961_8h.md#aceb8d227e063cc486808d5d41735a050)#define PIN\_A1 RCAR\_GP\_PIN(1, 1)

[ 32](pinctrl-r8a77961_8h.md#aa181f8521480dfcc1eb2688075701a4c)#define PIN\_A2 RCAR\_GP\_PIN(1, 2)

[ 33](pinctrl-r8a77961_8h.md#a933cca5ab119d5e74639e7ac5d120d8a)#define PIN\_A3 RCAR\_GP\_PIN(1, 3)

[ 34](pinctrl-r8a77961_8h.md#aea5f553ed9a6c4dac77e9c77d0cd0391)#define PIN\_A4 RCAR\_GP\_PIN(1, 4)

[ 35](pinctrl-r8a77961_8h.md#ab78a92a8cba92ec5664599083bcb2f52)#define PIN\_A5 RCAR\_GP\_PIN(1, 5)

[ 36](pinctrl-r8a77961_8h.md#afc06e9c4314680dcb8900c88079a954f)#define PIN\_A6 RCAR\_GP\_PIN(1, 6)

[ 37](pinctrl-r8a77961_8h.md#a027cabbaecdcdfdc68fbd92f8e1922ac)#define PIN\_A7 RCAR\_GP\_PIN(1, 7)

[ 38](pinctrl-r8a77961_8h.md#a77c84e33cd974a2c18b6efebdcf61937)#define PIN\_A8 RCAR\_GP\_PIN(1, 8)

[ 39](pinctrl-r8a77961_8h.md#a15bd44dc7fe5f12a0fad7797195e10d3)#define PIN\_A9 RCAR\_GP\_PIN(1, 9)

[ 40](pinctrl-r8a77961_8h.md#ae71b3cbb8bb3790bb239b532cee6d846)#define PIN\_A10 RCAR\_GP\_PIN(1, 10)

[ 41](pinctrl-r8a77961_8h.md#a5fbecbe19c0d6f772954fb390b20bd83)#define PIN\_A11 RCAR\_GP\_PIN(1, 11)

[ 42](pinctrl-r8a77961_8h.md#aafd03acf36a5aa964c65776a1ee2b378)#define PIN\_A12 RCAR\_GP\_PIN(1, 12)

[ 43](pinctrl-r8a77961_8h.md#a6b79058f8c28f6ed700333ed3cc4ba88)#define PIN\_A13 RCAR\_GP\_PIN(1, 13)

[ 44](pinctrl-r8a77961_8h.md#a2367dd922a04bb7fb172cf598cc934df)#define PIN\_A14 RCAR\_GP\_PIN(1, 14)

[ 45](pinctrl-r8a77961_8h.md#af16ed9214e71da7bf4c189d4adf4643f)#define PIN\_A15 RCAR\_GP\_PIN(1, 15)

[ 46](pinctrl-r8a77961_8h.md#a9b67e23e3456a2c9420ab3672b6e99ba)#define PIN\_A16 RCAR\_GP\_PIN(1, 16)

[ 47](pinctrl-r8a77961_8h.md#a2383aab15791b3f2af6f26806c256bbd)#define PIN\_A17 RCAR\_GP\_PIN(1, 17)

[ 48](pinctrl-r8a77961_8h.md#a50b04e06a058289e25de224e8226c432)#define PIN\_A18 RCAR\_GP\_PIN(1, 18)

[ 49](pinctrl-r8a77961_8h.md#ae1e920e080352f3d5a6366aaae1f05f7)#define PIN\_A19 RCAR\_GP\_PIN(1, 19)

[ 50](pinctrl-r8a77961_8h.md#ab27daa8385509b31d8199da5fa883f39)#define PIN\_CS0 RCAR\_GP\_PIN(1, 20)

[ 51](pinctrl-r8a77961_8h.md#a9f780a2fc93919987682f32716b3bc2d)#define PIN\_CS1 RCAR\_GP\_PIN(1, 21)

[ 52](pinctrl-r8a77961_8h.md#a75d37cecb8d5d0bb10b06d2e37547352)#define PIN\_BS RCAR\_GP\_PIN(1, 22)

[ 53](pinctrl-r8a77961_8h.md#aa9f23567c42d6b5f2007556262951f35)#define PIN\_RD RCAR\_GP\_PIN(1, 23)

[ 54](pinctrl-r8a77961_8h.md#af09ff2d839d2554555373e1d6ad630c6)#define PIN\_RD\_WR RCAR\_GP\_PIN(1, 24)

[ 55](pinctrl-r8a77961_8h.md#a704955f76ffd701ed62e8a7050b1d7e3)#define PIN\_WE0 RCAR\_GP\_PIN(1, 25)

[ 56](pinctrl-r8a77961_8h.md#a2185dcd8599f6535bdc2c8c92c32e872)#define PIN\_WE1 RCAR\_GP\_PIN(1, 26)

[ 57](pinctrl-r8a77961_8h.md#a4203b2c74c570fd56eeffb2e3a947492)#define PIN\_EX\_WAIT0 RCAR\_GP\_PIN(1, 27)

[ 58](pinctrl-r8a77961_8h.md#a4cca65a97f5bcaf5c9a3daf0fd1f3a26)#define PIN\_CLKOUT RCAR\_GP\_PIN(1, 28)

[ 59](pinctrl-r8a77961_8h.md#a99ed780c4dd8d2e01c5ff66064306abf)#define PIN\_IRQ0 RCAR\_GP\_PIN(2, 0)

[ 60](pinctrl-r8a77961_8h.md#a14204df3192ece77fc1b651c6625bc30)#define PIN\_IRQ1 RCAR\_GP\_PIN(2, 1)

[ 61](pinctrl-r8a77961_8h.md#a6506051b7159eb6245d67a289ed548d1)#define PIN\_IRQ2 RCAR\_GP\_PIN(2, 2)

[ 62](pinctrl-r8a77961_8h.md#a6e11e3ba86f107ad6f95cfd2cc922cf5)#define PIN\_IRQ3 RCAR\_GP\_PIN(2, 3)

[ 63](pinctrl-r8a77961_8h.md#aed22c7cddb8d42cc7085eb40d8625976)#define PIN\_IRQ4 RCAR\_GP\_PIN(2, 4)

[ 64](pinctrl-r8a77961_8h.md#a2299ca5a0c282a8b331678aab6a1775b)#define PIN\_IRQ5 RCAR\_GP\_PIN(2, 5)

[ 65](pinctrl-r8a77961_8h.md#a1c1008c3c50acff2e7c46557c8320fcb)#define PIN\_PWM0 RCAR\_GP\_PIN(2, 6)

[ 66](pinctrl-r8a77961_8h.md#a23c5ab09665d4bd5c7e73ea897a3844e)#define PIN\_PWM1\_A RCAR\_GP\_PIN(2, 7)

[ 67](pinctrl-r8a77961_8h.md#aa8a2b196c51a15819c933251b61fb177)#define PIN\_PWM2\_A RCAR\_GP\_PIN(2, 8)

[ 68](pinctrl-r8a77961_8h.md#abdfcd1b409db550e9d855d81b65ec590)#define PIN\_AVB\_MDC RCAR\_GP\_PIN(2, 9)

[ 69](pinctrl-r8a77961_8h.md#af003a8ef9bec1a03797cd4818d4a1ccb)#define PIN\_AVB\_MAGIC RCAR\_GP\_PIN(2, 10)

[ 70](pinctrl-r8a77961_8h.md#a9ae0a7a1d08f94e7fde1dd967c39b118)#define PIN\_AVB\_PHY\_INT RCAR\_GP\_PIN(2, 11)

[ 71](pinctrl-r8a77961_8h.md#ad443b12368ea8a283e897095998e1984)#define PIN\_AVB\_LINK RCAR\_GP\_PIN(2, 12)

[ 72](pinctrl-r8a77961_8h.md#a94288a2ce9a77a00ceaf4d9801ed1911)#define PIN\_AVB\_AVTP\_MATCH\_A RCAR\_GP\_PIN(2, 13)

[ 73](pinctrl-r8a77961_8h.md#adb23d84548c9f2975fb4895fa9a195f0)#define PIN\_AVB\_AVTP\_CAPTURE\_A RCAR\_GP\_PIN(2, 14)

[ 74](pinctrl-r8a77961_8h.md#a9d19d7f5e5999cff224df0f2dbcf5e5a)#define PIN\_SD0\_CLK RCAR\_GP\_PIN(3, 0)

[ 75](pinctrl-r8a77961_8h.md#a83a34e8961aabdc22d2a9bae3b03ad08)#define PIN\_SD0\_CMD RCAR\_GP\_PIN(3, 1)

[ 76](pinctrl-r8a77961_8h.md#a5ae360d9210474bcff84f656f3948f72)#define PIN\_SD0\_DATA0 RCAR\_GP\_PIN(3, 2)

[ 77](pinctrl-r8a77961_8h.md#a1881ab8e61d6f878f29b608deb0505d4)#define PIN\_SD0\_DATA1 RCAR\_GP\_PIN(3, 3)

[ 78](pinctrl-r8a77961_8h.md#a310d4722e362453561d7acacf782306b)#define PIN\_SD0\_DATA2 RCAR\_GP\_PIN(3, 4)

[ 79](pinctrl-r8a77961_8h.md#ab4f9a2603e6a13616f9711415959fde0)#define PIN\_SD0\_DATA3 RCAR\_GP\_PIN(3, 5)

[ 80](pinctrl-r8a77961_8h.md#a02cb9d6acabda91eaaef7b0a691b2b99)#define PIN\_SD1\_CLK RCAR\_GP\_PIN(3, 6)

[ 81](pinctrl-r8a77961_8h.md#ac468f899d052bc342a25d80358c1a4d4)#define PIN\_SD1\_CMD RCAR\_GP\_PIN(3, 7)

[ 82](pinctrl-r8a77961_8h.md#a28e1004c169a40387ad45215f9ea4d8f)#define PIN\_SD1\_DATA0 RCAR\_GP\_PIN(3, 8)

[ 83](pinctrl-r8a77961_8h.md#a8ef57ae45bd6b9460184d101f20c6ef0)#define PIN\_SD1\_DATA1 RCAR\_GP\_PIN(3, 9)

[ 84](pinctrl-r8a77961_8h.md#a1397bd3c2b618f6f5fcebb18a19a4072)#define PIN\_SD1\_DATA2 RCAR\_GP\_PIN(3, 10)

[ 85](pinctrl-r8a77961_8h.md#a886bf58616d323a7267a5c04339d7fba)#define PIN\_SD1\_DATA3 RCAR\_GP\_PIN(3, 11)

[ 86](pinctrl-r8a77961_8h.md#a803f5ff3e1f046d9020403c74188ee68)#define PIN\_SD0\_CD RCAR\_GP\_PIN(3, 12)

[ 87](pinctrl-r8a77961_8h.md#a6716be03dcd77fbb58e2633a6cfdcf8d)#define PIN\_SD0\_WP RCAR\_GP\_PIN(3, 13)

[ 88](pinctrl-r8a77961_8h.md#af0894972a37b87c0ac1fc6d4fb5a5e32)#define PIN\_SD1\_CD RCAR\_GP\_PIN(3, 14)

[ 89](pinctrl-r8a77961_8h.md#ae51dc75ff2098b33993bf32b3f9cc88c)#define PIN\_SD1\_WP RCAR\_GP\_PIN(3, 15)

[ 90](pinctrl-r8a77961_8h.md#a89f29aaee07e33195930c442446c0d45)#define PIN\_SD2\_CLK RCAR\_GP\_PIN(4, 0)

[ 91](pinctrl-r8a77961_8h.md#ac51dd59c00afeda80a8d2926317d309d)#define PIN\_SD2\_CMD RCAR\_GP\_PIN(4, 1)

[ 92](pinctrl-r8a77961_8h.md#a281deecd34ce02ae68e5ff6a2d471104)#define PIN\_SD2\_DATA0 RCAR\_GP\_PIN(4, 2)

[ 93](pinctrl-r8a77961_8h.md#a8982cea5c3de77b7f5b107e19bc668a8)#define PIN\_SD2\_DATA1 RCAR\_GP\_PIN(4, 3)

[ 94](pinctrl-r8a77961_8h.md#aa2236dad12d9be7a0441437d09cd4d13)#define PIN\_SD2\_DATA2 RCAR\_GP\_PIN(4, 4)

[ 95](pinctrl-r8a77961_8h.md#afc4f1a8655fceee48e5ddd5e54461942)#define PIN\_SD2\_DATA3 RCAR\_GP\_PIN(4, 5)

[ 96](pinctrl-r8a77961_8h.md#a5eecf0f15b5eefe1f462efa5bbaeba72)#define PIN\_SD2\_DS RCAR\_GP\_PIN(4, 6)

[ 97](pinctrl-r8a77961_8h.md#abe218411e9a47a116ab13205cd564211)#define PIN\_SD3\_CLK RCAR\_GP\_PIN(4, 7)

[ 98](pinctrl-r8a77961_8h.md#a1cae9fc15220519e3f69f2c1b613e2c2)#define PIN\_SD3\_CMD RCAR\_GP\_PIN(4, 8)

[ 99](pinctrl-r8a77961_8h.md#a413c125c77fb61a578fc2ad15f6e7c58)#define PIN\_SD3\_DATA0 RCAR\_GP\_PIN(4, 9)

[ 100](pinctrl-r8a77961_8h.md#aff3052402811c024f401fd20d1711c15)#define PIN\_SD3\_DATA1 RCAR\_GP\_PIN(4, 10)

[ 101](pinctrl-r8a77961_8h.md#a8c2f5f99f99d9712068b9f030d4bcfbb)#define PIN\_SD3\_DATA2 RCAR\_GP\_PIN(4, 11)

[ 102](pinctrl-r8a77961_8h.md#a0dde513760c3f51a132595cb115bd8d7)#define PIN\_SD3\_DATA3 RCAR\_GP\_PIN(4, 12)

[ 103](pinctrl-r8a77961_8h.md#afb26ab3d47ade897128f6fbf813194ce)#define PIN\_SD3\_DATA4 RCAR\_GP\_PIN(4, 13)

[ 104](pinctrl-r8a77961_8h.md#a208de44c488e295d9273b7aedcf9e8d1)#define PIN\_SD3\_DATA5 RCAR\_GP\_PIN(4, 14)

[ 105](pinctrl-r8a77961_8h.md#afbdd386ea39f7ea9fa385cf745275ac9)#define PIN\_SD3\_DATA6 RCAR\_GP\_PIN(4, 15)

[ 106](pinctrl-r8a77961_8h.md#a909dc2a05f2b88445369671a0847a852)#define PIN\_SD3\_DATA7 RCAR\_GP\_PIN(4, 16)

[ 107](pinctrl-r8a77961_8h.md#adde84de73e6374d40047ef3de995090e)#define PIN\_SD3\_DS RCAR\_GP\_PIN(4, 17)

[ 108](pinctrl-r8a77961_8h.md#a8a51b481e5ddab9dd843411171383b0c)#define PIN\_SCK0 RCAR\_GP\_PIN(5, 0)

[ 109](pinctrl-r8a77961_8h.md#a6844ffe71c9cb20c6b4fe67289b58f40)#define PIN\_RX0 RCAR\_GP\_PIN(5, 1)

[ 110](pinctrl-r8a77961_8h.md#a6c8efa60d2db765b46d88aa2a6df0318)#define PIN\_TX0 RCAR\_GP\_PIN(5, 2)

[ 111](pinctrl-r8a77961_8h.md#a4d8db9b07c77aaa2e053d817821e8050)#define PIN\_CTS0 RCAR\_GP\_PIN(5, 3)

[ 112](pinctrl-r8a77961_8h.md#a7e97fda5ad4a399ef712d771eb958060)#define PIN\_RTS0 RCAR\_GP\_PIN(5, 4)

[ 113](pinctrl-r8a77961_8h.md#a8fae8bb9a94036b14869560d63a8e0cd)#define PIN\_RX1\_A RCAR\_GP\_PIN(5, 5)

[ 114](pinctrl-r8a77961_8h.md#a47732ee4975ee1d921531c2232ebc7e3)#define PIN\_TX1\_A RCAR\_GP\_PIN(5, 6)

[ 115](pinctrl-r8a77961_8h.md#a99963d73735685b06cb9ab518d1dd419)#define PIN\_CTS1 RCAR\_GP\_PIN(5, 7)

[ 116](pinctrl-r8a77961_8h.md#a3fbafb9ee7b223fcf431c57e1357b350)#define PIN\_RTS1 RCAR\_GP\_PIN(5, 8)

[ 117](pinctrl-r8a77961_8h.md#ae973e37bb5ed85a1d5291ca726761caf)#define PIN\_SCK2 RCAR\_GP\_PIN(5, 9)

[ 118](pinctrl-r8a77961_8h.md#a7a01627dcec544bd7e3e01d4996acea8)#define PIN\_TX2\_A RCAR\_GP\_PIN(5, 10)

[ 119](pinctrl-r8a77961_8h.md#a125cf5d4f3c7289781ff48f749769678)#define PIN\_RX2\_A RCAR\_GP\_PIN(5, 11)

[ 120](pinctrl-r8a77961_8h.md#aae52ed4df2cbea0bad32c9386fe043b2)#define PIN\_HSCK0 RCAR\_GP\_PIN(5, 12)

[ 121](pinctrl-r8a77961_8h.md#a7155ba5d8ae93665a43b2ebe82d5603b)#define PIN\_HRX0 RCAR\_GP\_PIN(5, 13)

[ 122](pinctrl-r8a77961_8h.md#ae18a748003b0c3b29355e9ad5f2dc9c9)#define PIN\_HTX0 RCAR\_GP\_PIN(5, 14)

[ 123](pinctrl-r8a77961_8h.md#a74c6eaecc9af7ebbf37fff26cbc12eb3)#define PIN\_HCTS0 RCAR\_GP\_PIN(5, 15)

[ 124](pinctrl-r8a77961_8h.md#a567c97ce30b559a2d30cd24266e3c3d1)#define PIN\_HRTS0 RCAR\_GP\_PIN(5, 16)

[ 125](pinctrl-r8a77961_8h.md#a69ed37349d43d4214adce06f067265d6)#define PIN\_MSIOF0\_SCK RCAR\_GP\_PIN(5, 17)

[ 126](pinctrl-r8a77961_8h.md#a53dcd276122e302a448058c662d4db4d)#define PIN\_MSIOF0\_SYNC RCAR\_GP\_PIN(5, 18)

[ 127](pinctrl-r8a77961_8h.md#a2b31a8f747dd87216ecea5cbc94d1896)#define PIN\_MSIOF0\_SS1 RCAR\_GP\_PIN(5, 19)

[ 128](pinctrl-r8a77961_8h.md#a4d27c592b780f5f4d5c87e1e4f2c0d4b)#define PIN\_MSIOF0\_TXD RCAR\_GP\_PIN(5, 20)

[ 129](pinctrl-r8a77961_8h.md#a98b300e3af1451c327da1f89c5deb38e)#define PIN\_MSIOF0\_SS2 RCAR\_GP\_PIN(5, 21)

[ 130](pinctrl-r8a77961_8h.md#a924265fb5625164c8798e5e9e22a44c4)#define PIN\_MSIOF0\_RXD RCAR\_GP\_PIN(5, 22)

[ 131](pinctrl-r8a77961_8h.md#a81dc2cffe38e06e89d610a5eafc206e0)#define PIN\_MLB\_CLK RCAR\_GP\_PIN(5, 23)

[ 132](pinctrl-r8a77961_8h.md#a5b294dd2b759e98e5130b486d0eea021)#define PIN\_MLB\_SIG RCAR\_GP\_PIN(5, 24)

[ 133](pinctrl-r8a77961_8h.md#ada68381b1ed6de34ba652010e39aafc8)#define PIN\_MLB\_DAT RCAR\_GP\_PIN(5, 25)

[ 134](pinctrl-r8a77961_8h.md#a6d54c481921d36f60ac1af4f495bdc07)#define PIN\_SSI\_SCK01239 RCAR\_GP\_PIN(6, 0)

[ 135](pinctrl-r8a77961_8h.md#a0a121980ac5ceeb64591e72db0d9e1cf)#define PIN\_SSI\_WS01239 RCAR\_GP\_PIN(6, 1)

[ 136](pinctrl-r8a77961_8h.md#a6078f603b889afeb73a772855dfb5a4c)#define PIN\_SSI\_SDATA0 RCAR\_GP\_PIN(6, 2)

[ 137](pinctrl-r8a77961_8h.md#a102c39209f580a1f6192cb4c1254b354)#define PIN\_SSI\_SDATA1\_A RCAR\_GP\_PIN(6, 3)

[ 138](pinctrl-r8a77961_8h.md#a978845ec92e3a57cbf27cb5ec09adbbd)#define PIN\_SSI\_SDATA2\_A RCAR\_GP\_PIN(6, 4)

[ 139](pinctrl-r8a77961_8h.md#aefc99d25bc7ff095d1f2972529e312b4)#define PIN\_SSI\_SCK349 RCAR\_GP\_PIN(6, 5)

[ 140](pinctrl-r8a77961_8h.md#a2d2f3b388126c5db727e626ef8f6c068)#define PIN\_SSI\_WS349 RCAR\_GP\_PIN(6, 6)

[ 141](pinctrl-r8a77961_8h.md#a7c3e5c79134918932d98413261efc402)#define PIN\_SSI\_SDATA3 RCAR\_GP\_PIN(6, 7)

[ 142](pinctrl-r8a77961_8h.md#a8fa53278e99dd7664f28c288f222a734)#define PIN\_SSI\_SCK4 RCAR\_GP\_PIN(6, 8)

[ 143](pinctrl-r8a77961_8h.md#aff860ee76ee1274617ed34097ee47652)#define PIN\_SSI\_WS4 RCAR\_GP\_PIN(6, 9)

[ 144](pinctrl-r8a77961_8h.md#a3653e3795525ad30bf0e74147907f6f0)#define PIN\_SSI\_SDAT\_A4 RCAR\_GP\_PIN(6, 10)

[ 145](pinctrl-r8a77961_8h.md#a96da792ca0d23d407bc2ad229ec0de9d)#define PIN\_SSI\_SCK5 RCAR\_GP\_PIN(6, 11)

[ 146](pinctrl-r8a77961_8h.md#a2772c00e1bef9c9482199a7bee683d83)#define PIN\_SSI\_WS5 RCAR\_GP\_PIN(6, 12)

[ 147](pinctrl-r8a77961_8h.md#a57b4a83f012c72ca8072814a122888e1)#define PIN\_SSI\_SDAT\_A5 RCAR\_GP\_PIN(6, 13)

[ 148](pinctrl-r8a77961_8h.md#a7e86fd4cb29c5df8afa24607ee3e06f7)#define PIN\_SSI\_SCK6 RCAR\_GP\_PIN(6, 14)

[ 149](pinctrl-r8a77961_8h.md#a0b21b978f936aebbd5d432f709617b30)#define PIN\_SSI\_WS6 RCAR\_GP\_PIN(6, 15)

[ 150](pinctrl-r8a77961_8h.md#a247d2b3cb0cef55d368addb64e06cd42)#define PIN\_SSI\_SDATA6 RCAR\_GP\_PIN(6, 16)

[ 151](pinctrl-r8a77961_8h.md#a590c95e1771fd891676283f423ed5e03)#define PIN\_SSI\_SCK78 RCAR\_GP\_PIN(6, 17)

[ 152](pinctrl-r8a77961_8h.md#acf53532ed166812e47a66d1a39494b81)#define PIN\_WS78 RCAR\_GP\_PIN(6, 18)

[ 153](pinctrl-r8a77961_8h.md#a58ea91538e81e14e90c6efcc22ec61bb)#define PIN\_SSI\_SDATA7 RCAR\_GP\_PIN(6, 19)

[ 154](pinctrl-r8a77961_8h.md#a91e92accedf177aadc2a12aefafa2919)#define PIN\_SSI\_SDATA8 RCAR\_GP\_PIN(6, 20)

[ 155](pinctrl-r8a77961_8h.md#a98d0dbb8f1d7f0715865da6bd2140b87)#define PIN\_SSI\_SDATA9\_A RCAR\_GP\_PIN(6, 21)

[ 156](pinctrl-r8a77961_8h.md#ab769e688da3ed814b297d9d11be2a1b5)#define PIN\_AUDIO\_CLKA\_A RCAR\_GP\_PIN(6, 22)

[ 157](pinctrl-r8a77961_8h.md#ab6310583a9b165384eb2cbe991d81e6d)#define PIN\_AUDIO\_CLKB\_B RCAR\_GP\_PIN(6, 23)

[ 158](pinctrl-r8a77961_8h.md#a4e7870bedeb53c5b365b0852443096a5)#define PIN\_USB0\_PWEN RCAR\_GP\_PIN(6, 24)

[ 159](pinctrl-r8a77961_8h.md#a4c9649c55384e8d5a21b85c9272b856c)#define PIN\_USB0\_OVC RCAR\_GP\_PIN(6, 25)

[ 160](pinctrl-r8a77961_8h.md#adba27ce24a153cc5778ecd4b818ca409)#define PIN\_USB1\_PWEN RCAR\_GP\_PIN(6, 26)

[ 161](pinctrl-r8a77961_8h.md#a51ba07350d0d7eea0fad3a09f16db9ac)#define PIN\_USB1\_OVC RCAR\_GP\_PIN(6, 27)

[ 162](pinctrl-r8a77961_8h.md#aa8f56410e68ed99aeedfd558ed02433c)#define PIN\_USB30\_PWEN RCAR\_GP\_PIN(6, 28)

[ 163](pinctrl-r8a77961_8h.md#a4c0ce69fdff288c0c215e6ff2a8d72d4)#define PIN\_USB30\_OVC RCAR\_GP\_PIN(6, 29)

[ 164](pinctrl-r8a77961_8h.md#a58b56d2ecc9b41467fa81967d670edc4)#define PIN\_USB2\_CH3\_PWEN RCAR\_GP\_PIN(6, 30)

[ 165](pinctrl-r8a77961_8h.md#a3ad41e8129a9da767a6a2658c549d7c7)#define PIN\_USB2\_CH3\_OVC RCAR\_GP\_PIN(6, 31)

[ 166](pinctrl-r8a77961_8h.md#abfc15e473f5c229dca52f566e4b87e5e)#define PIN\_AVS1 RCAR\_GP\_PIN(7, 0)

[ 167](pinctrl-r8a77961_8h.md#a216f7426206fd56b7f6f662cab767aac)#define PIN\_AVS2 RCAR\_GP\_PIN(7, 1)

[ 168](pinctrl-r8a77961_8h.md#a1b09d08830d56d764fb2cfde7c96782b)#define PIN\_GP7\_02 RCAR\_GP\_PIN(7, 2)

[ 169](pinctrl-r8a77961_8h.md#aa2aace9171336314ffa2c872520ecb6a)#define PIN\_GP7\_03 RCAR\_GP\_PIN(7, 3)

[ 170](pinctrl-r8a77961_8h.md#ac587b286b860a5deb1b8b0bf83f337f4)#define PIN\_ASEBRK RCAR\_NOGP\_PIN(1)

[ 171](pinctrl-r8a77961_8h.md#a79b77b44546535da290cc4b2d71c172c)#define PIN\_AVB\_MDIO RCAR\_NOGP\_PIN(2)

[ 172](pinctrl-r8a77961_8h.md#a15fd25a7d2511343905615148c87e7af)#define PIN\_AVB\_RD0 RCAR\_NOGP\_PIN(3)

[ 173](pinctrl-r8a77961_8h.md#a3ec0a2ae4f1078810fb3dfa0ade96a63)#define PIN\_AVB\_RD1 RCAR\_NOGP\_PIN(4)

[ 174](pinctrl-r8a77961_8h.md#a2aecd24ac82fcbc95438bb3fa8034018)#define PIN\_AVB\_RD2 RCAR\_NOGP\_PIN(5)

[ 175](pinctrl-r8a77961_8h.md#aed1de27f27743065c3ec64b6b48a4853)#define PIN\_AVB\_RD3 RCAR\_NOGP\_PIN(6)

[ 176](pinctrl-r8a77961_8h.md#aa5baa13e17b08d18d929b239ee4b763a)#define PIN\_AVB\_RXC RCAR\_NOGP\_PIN(7)

[ 177](pinctrl-r8a77961_8h.md#adc887804f241bfda36573ac8a0cce17d)#define PIN\_AVB\_RX\_CTL RCAR\_NOGP\_PIN(8)

[ 178](pinctrl-r8a77961_8h.md#a8dc3c1eb84a0837002f7137e90d9888d)#define PIN\_AVB\_TD0 RCAR\_NOGP\_PIN(9)

[ 179](pinctrl-r8a77961_8h.md#a94ac37e4d395a31035210f8147ae4814)#define PIN\_AVB\_TD1 RCAR\_NOGP\_PIN(10)

[ 180](pinctrl-r8a77961_8h.md#ad2fd61d41ba6d50f608d08117a5584ad)#define PIN\_AVB\_TD2 RCAR\_NOGP\_PIN(11)

[ 181](pinctrl-r8a77961_8h.md#a88d85fbdce86edf97bebee0b798b2be3)#define PIN\_AVB\_TD3 RCAR\_NOGP\_PIN(12)

[ 182](pinctrl-r8a77961_8h.md#aa61cff259c70f66c888c2e5778d7404e)#define PIN\_AVB\_TXC RCAR\_NOGP\_PIN(13)

[ 183](pinctrl-r8a77961_8h.md#a4d21579590bdab4011c5204beb9d4e18)#define PIN\_AVB\_TXCREFCLK RCAR\_NOGP\_PIN(14)

[ 184](pinctrl-r8a77961_8h.md#a1554e797ce2f32a7493a5b8a1a240456)#define PIN\_AVB\_TX\_CTL RCAR\_NOGP\_PIN(15)

[ 185](pinctrl-r8a77961_8h.md#ae33fac6af1df44ca8abd45e7e79f2c63)#define PIN\_DU\_DOTCLKIN0 RCAR\_NOGP\_PIN(16)

[ 186](pinctrl-r8a77961_8h.md#a94bf6ca4033fe66a2672cf12148555d4)#define PIN\_DU\_DOTCLKIN1 RCAR\_NOGP\_PIN(17)

[ 187](pinctrl-r8a77961_8h.md#af72da78654122e3aa1f3a6b15e75d848)#define PIN\_DU\_DOTCLKIN2 RCAR\_NOGP\_PIN(18)

[ 188](pinctrl-r8a77961_8h.md#ac0cd161630d20e8dab640929b7d35394)#define PIN\_DU\_DOTCLKIN3 RCAR\_NOGP\_PIN(19)

[ 189](pinctrl-r8a77961_8h.md#a6d32086bf8ce48fe37720085eae1c192)#define PIN\_EXTALR RCAR\_NOGP\_PIN(20)

[ 190](pinctrl-r8a77961_8h.md#a7787d69f9cb488adfff055505a8fa7cd)#define PIN\_FSCLKST\_N RCAR\_NOGP\_PIN(21)

[ 191](pinctrl-r8a77961_8h.md#a7091d7ec112804caaa64df25c016ebac)#define PIN\_MLB\_REF RCAR\_NOGP\_PIN(22)

[ 192](pinctrl-r8a77961_8h.md#a52517b00d68de0da0589802ccf40e6a9)#define PIN\_PRESETOUT\_N RCAR\_NOGP\_PIN(23)

[ 193](pinctrl-r8a77961_8h.md#ae8e8f603407a3db8830e7c0f6156c647)#define PIN\_QSPI0\_IO2 RCAR\_NOGP\_PIN(24)

[ 194](pinctrl-r8a77961_8h.md#ab0ef23683d3b80c9710a82340d779566)#define PIN\_QSPI0\_IO3 RCAR\_NOGP\_PIN(25)

[ 195](pinctrl-r8a77961_8h.md#a8a4db281c1d7eeb4a8b683e579b0ab4e)#define PIN\_QSPI0\_MISO\_IO1 RCAR\_NOGP\_PIN(26)

[ 196](pinctrl-r8a77961_8h.md#a49c45fe433bb57486cb1ded9c3fbf275)#define PIN\_QSPI0\_MOSI\_IO0 RCAR\_NOGP\_PIN(27)

[ 197](pinctrl-r8a77961_8h.md#a68c69e86d4457a5d637d64ef75bdfd85)#define PIN\_QSPI0\_SPCLK RCAR\_NOGP\_PIN(28)

[ 198](pinctrl-r8a77961_8h.md#a147f808337f1bbe0917f1a8ce1ca419d)#define PIN\_QSPI0\_SSL RCAR\_NOGP\_PIN(29)

[ 199](pinctrl-r8a77961_8h.md#ad28db9650b74336e2b7d2a724894a706)#define PIN\_QSPI1\_IO2 RCAR\_NOGP\_PIN(30)

[ 200](pinctrl-r8a77961_8h.md#a9c9ae11c6c6c6ac9c9c1b19a94d1b6fd)#define PIN\_QSPI1\_IO3 RCAR\_NOGP\_PIN(31)

[ 201](pinctrl-r8a77961_8h.md#ab5e70699dc556ff6d30df1618924a928)#define PIN\_QSPI1\_MISO\_IO1 RCAR\_NOGP\_PIN(32)

[ 202](pinctrl-r8a77961_8h.md#aaa596198d60346c91822c8b52fbf44c7)#define PIN\_QSPI1\_MOSI\_IO0 RCAR\_NOGP\_PIN(33)

[ 203](pinctrl-r8a77961_8h.md#aa6b8aad6a047b3173abb358c345e557c)#define PIN\_QSPI1\_SPCLK RCAR\_NOGP\_PIN(34)

[ 204](pinctrl-r8a77961_8h.md#a2d81e5fdef8cb97a4cf2d18c68325746)#define PIN\_QSPI1\_SSL RCAR\_NOGP\_PIN(35)

[ 205](pinctrl-r8a77961_8h.md#ae445f51a0031da7deb1a5e279c7f55f6)#define PIN\_RPC\_INT\_N RCAR\_NOGP\_PIN(36)

[ 206](pinctrl-r8a77961_8h.md#a0f73d041e18bfeedd28f98ba895272ed)#define PIN\_RPC\_RESET\_N RCAR\_NOGP\_PIN(37)

[ 207](pinctrl-r8a77961_8h.md#a3f139531d8d50cfc031b2163fe16e885)#define PIN\_RPC\_WP\_N RCAR\_NOGP\_PIN(38)

[ 208](pinctrl-r8a77961_8h.md#add84722750f76c77b70b9fb01dabfad2)#define PIN\_TCK RCAR\_NOGP\_PIN(39)

[ 209](pinctrl-r8a77961_8h.md#a4efe421134cc83f239f425a724e4b23c)#define PIN\_TDI RCAR\_NOGP\_PIN(40)

[ 210](pinctrl-r8a77961_8h.md#aa39124029fd35dacb54b272251d698c6)#define PIN\_TDO RCAR\_NOGP\_PIN(41)

[ 211](pinctrl-r8a77961_8h.md#a45867e53ab8e918075929ec92ae5272c)#define PIN\_TMS RCAR\_NOGP\_PIN(42)

[ 212](pinctrl-r8a77961_8h.md#a126c60fcd625162ef4d70e7727685d26)#define PIN\_TRST\_N RCAR\_NOGP\_PIN(43)

213

214/\* Pinmux function declarations \*/

[ 215](pinctrl-r8a77961_8h.md#a8cb8c553af7600dbd909d01ab5c7a6de)#define FUNC\_AVB\_MDC IPSR(0, 0, 0)

[ 216](pinctrl-r8a77961_8h.md#ab8e76fa8279be0a908290638cc449a3e)#define FUNC\_MSIOD2\_SS2\_C IPSR(0, 0, 2)

[ 217](pinctrl-r8a77961_8h.md#ac244da14394848a7b3f7cd274f89524a)#define FUNC\_AVB\_MAGIC IPSR(0, 4, 0)

[ 218](pinctrl-r8a77961_8h.md#a2a72fbd36ae4e60b59413c7b8495af84)#define FUNC\_MSIOF2\_SS1\_C IPSR(0, 4, 2)

[ 219](pinctrl-r8a77961_8h.md#a97726adc65b27ea6ed7177088f66eae6)#define FUNC\_SCK4\_A IPSR(0, 4, 3)

[ 220](pinctrl-r8a77961_8h.md#a3a86cdcbe72ce563801f588180495849)#define FUNC\_AVB\_PHY\_INT IPSR(0, 8, 0)

[ 221](pinctrl-r8a77961_8h.md#af7d2a0d1772d1bf439d0eecdd7664106)#define FUNC\_MSIOF2\_SYNC\_C IPSR(0, 8, 2)

[ 222](pinctrl-r8a77961_8h.md#a8b3230538863ee4ebeb76ad483cc0efa)#define FUNC\_RX4\_A IPSR(0, 8, 3)

[ 223](pinctrl-r8a77961_8h.md#a0d056e171712db4b25ef4ad554d5ac2d)#define FUNC\_AVB\_LINK IPSR(0, 12, 0)

[ 224](pinctrl-r8a77961_8h.md#afc4a5b013d2a1af93245ff554b49ea22)#define FUNC\_MSIOF2\_SCK\_C IPSR(0, 12, 2)

[ 225](pinctrl-r8a77961_8h.md#ac0709f7b5686e08a17722374db278729)#define FUNC\_TX4\_A IPSR(0, 12, 3)

[ 226](pinctrl-r8a77961_8h.md#ad1b9f11c539b53c269a58ac103e70fc0)#define FUNC\_AVB\_AVTP\_MATCH\_A IPSR(0, 16, 0)

[ 227](pinctrl-r8a77961_8h.md#a86078928d71cf463beefe9bac9b33381)#define FUNC\_MSIOF2\_RXD\_C IPSR(0, 16, 2)

[ 228](pinctrl-r8a77961_8h.md#ac07f5f9572ed9ff47c9866c35c108898)#define FUNC\_CTS4\_N\_A IPSR(0, 16, 3)

[ 229](pinctrl-r8a77961_8h.md#a3f6a63b6669f48422dd4966afcbbfae1)#define FUNC\_AVB\_AVTP\_CAPTURE\_A IPSR(0, 20, 0)

[ 230](pinctrl-r8a77961_8h.md#aeb589d2864b213ddebeadcc727354062)#define FUNC\_MSIOF2\_TXD\_C IPSR(0, 20, 2)

[ 231](pinctrl-r8a77961_8h.md#a300b6c07d4ad8d32e0d7e72147714693)#define FUNC\_RTS4\_N\_A IPSR(0, 20, 3)

[ 232](pinctrl-r8a77961_8h.md#a8093a0a22fe179ba8542a89a013fb573)#define FUNC\_IRQ0 IPSR(0, 24, 0)

[ 233](pinctrl-r8a77961_8h.md#af78734e7e8276b95c92e9195c6a929c4)#define FUNC\_QPOLB IPSR(0, 24, 1)

[ 234](pinctrl-r8a77961_8h.md#acba06c3c73b9e768663f6c93ee829727)#define FUNC\_DU\_CDE IPSR(0, 24, 3)

[ 235](pinctrl-r8a77961_8h.md#aaba9aa3d0c999662763bbc65d05438c2)#define FUNC\_VI4\_DATA0\_B IPSR(0, 24, 4)

[ 236](pinctrl-r8a77961_8h.md#a6e1b31db11cb1fc72561dd8228860a33)#define FUNC\_CAN0\_TX\_B IPSR(0, 24, 5)

[ 237](pinctrl-r8a77961_8h.md#a89a5020e373c10afd1954214ff5efdaf)#define FUNC\_CANFD0\_TX\_B IPSR(0, 24, 6)

[ 238](pinctrl-r8a77961_8h.md#a40aa687fd090e167a98dd326e5879dea)#define FUNC\_MSIOF3\_SS2\_E IPSR(0, 24, 7)

[ 239](pinctrl-r8a77961_8h.md#ab175aaaa927f86b485c6589f1949a66d)#define FUNC\_IRQ1 IPSR(0, 28, 0)

[ 240](pinctrl-r8a77961_8h.md#a89cac8e75009b3bddfccd0b225541878)#define FUNC\_QPOLA IPSR(0, 28, 1)

[ 241](pinctrl-r8a77961_8h.md#a504af26cbe100bdbe4c6f041e075c2b2)#define FUNC\_DU\_DISP IPSR(0, 28, 3)

[ 242](pinctrl-r8a77961_8h.md#a12465a4e03bfe9e2b76bb7ca4c33b5fc)#define FUNC\_VI4\_DATA1\_B IPSR(0, 28, 4)

[ 243](pinctrl-r8a77961_8h.md#adf89230f71dfa7c3a8ba6c219c25913c)#define FUNC\_CAN0\_RX\_B IPSR(0, 28, 5)

[ 244](pinctrl-r8a77961_8h.md#abdfd9d73f8783b1f7ff97923be947583)#define FUNC\_CANFD0\_RX\_B IPSR(0, 28, 6)

[ 245](pinctrl-r8a77961_8h.md#a4947ec3c7ba94666af77da453d90e385)#define FUNC\_MSIOF3\_SS1\_E IPSR(0, 28, 7)

[ 246](pinctrl-r8a77961_8h.md#a3637e038ae0080707f61877f978e304e)#define FUNC\_IRQ2 IPSR(1, 0, 0)

[ 247](pinctrl-r8a77961_8h.md#afb126719d2e1c00cf882fa519c565c77)#define FUNC\_QCPV\_QDE IPSR(1, 0, 1)

[ 248](pinctrl-r8a77961_8h.md#a5c8a5fb58318274f7970319ffbf1419b)#define FUNC\_DU\_EXODDF\_DU\_ODDF\_DISP\_CDE IPSR(1, 0, 3)

[ 249](pinctrl-r8a77961_8h.md#aff02a5ec02f121a28a36f4abd906e742)#define FUNC\_VI4\_DATA2\_B IPSR(1, 0, 4)

[ 250](pinctrl-r8a77961_8h.md#a13464f9b218c812d53bc04af820df86d)#define FUNC\_MSIOF3\_SYNC\_E IPSR(1, 0, 7)

[ 251](pinctrl-r8a77961_8h.md#a4347a63dd029edf8c931661d34f2813e)#define FUNC\_PWM3\_B IPSR(1, 0, 9)

[ 252](pinctrl-r8a77961_8h.md#a463e1089b96456cdf50231bf43129ad1)#define FUNC\_IRQ3 IPSR(1, 4, 0)

[ 253](pinctrl-r8a77961_8h.md#abe3adee16afe20a4fe1383c1d4c9ad1d)#define FUNC\_QSTVB\_QVE IPSR(1, 4, 1)

[ 254](pinctrl-r8a77961_8h.md#a626c57ac8786e14c5f30bd34f82fd451)#define FUNC\_DU\_DOTCLKOUT1 IPSR(1, 4, 3)

[ 255](pinctrl-r8a77961_8h.md#a420e82a45f6009b5ec1a1273f4bc5b74)#define FUNC\_VI4\_DATA3\_B IPSR(1, 4, 4)

[ 256](pinctrl-r8a77961_8h.md#a0511b32ffd1713055f59f24d84f30bc5)#define FUNC\_MSIOF3\_SCK\_E IPSR(1, 4, 7)

[ 257](pinctrl-r8a77961_8h.md#a4ce69f8164e8360607622a394bd12962)#define FUNC\_PWM4\_B IPSR(1, 4, 9)

[ 258](pinctrl-r8a77961_8h.md#a1e7493f35e9cbbf98922470ea8c88b6e)#define FUNC\_IRQ4 IPSR(1, 8, 0)

[ 259](pinctrl-r8a77961_8h.md#ab27b4fef25fe67597148f5a88bbe85c8)#define FUNC\_QSTH\_QHS IPSR(1, 8, 1)

[ 260](pinctrl-r8a77961_8h.md#a52221d98bbb97edf990ddea8df74399d)#define FUNC\_DU\_EXHSYNC\_DU\_HSYNC IPSR(1, 8, 3)

[ 261](pinctrl-r8a77961_8h.md#a862a31966514b6974fc32654848497d5)#define FUNC\_VI4\_DATA4\_B IPSR(1, 8, 4)

[ 262](pinctrl-r8a77961_8h.md#a021f02706eeb72d546b14a70047e3f0b)#define FUNC\_MSIOF3\_RXD\_E IPSR(1, 8, 7)

[ 263](pinctrl-r8a77961_8h.md#abf39cc6fed04dc47b0efa5995c62d928)#define FUNC\_PWM5\_B IPSR(1, 8, 9)

[ 264](pinctrl-r8a77961_8h.md#afa85b0631ba88f21389f0e39be80c35e)#define FUNC\_IRQ5 IPSR(1, 12, 0)

[ 265](pinctrl-r8a77961_8h.md#a8addea117115dffbc96abc8d6fd4fe42)#define FUNC\_QSTB\_QHE IPSR(1, 12, 1)

[ 266](pinctrl-r8a77961_8h.md#a1780d804f2e972d4c85b57e6f99dca61)#define FUNC\_DU\_EXVSYNC\_DU\_VSYNC IPSR(1, 12, 3)

[ 267](pinctrl-r8a77961_8h.md#a399d334e3bd3a9d6c7cc7a6ba35149f8)#define FUNC\_VI4\_DATA5\_B IPSR(1, 12, 4)

[ 268](pinctrl-r8a77961_8h.md#af3101110adff7103f3c254b302faa183)#define FUNC\_MSIOF3\_TXD\_E IPSR(1, 12, 7)

[ 269](pinctrl-r8a77961_8h.md#a9ac63f58237960ce739f5018befa3d2a)#define FUNC\_PWM6\_B IPSR(1, 12, 9)

[ 270](pinctrl-r8a77961_8h.md#a2e7656d8ce93e6ab330b317c16854aef)#define FUNC\_PWM0 IPSR(1, 16, 0)

[ 271](pinctrl-r8a77961_8h.md#aeca681e3f6834473c6d906a035eccee4)#define FUNC\_AVB\_AVTP\_PPS IPSR(1, 16, 1)

[ 272](pinctrl-r8a77961_8h.md#a3d07b590cf133c8b59d7c886f38480ea)#define FUNC\_VI4\_DATA6\_B IPSR(1, 16, 4)

[ 273](pinctrl-r8a77961_8h.md#a6d7c2b804bbc1a328953bbf1be71781f)#define FUNC\_IECLK\_B IPSR(1, 16, 9)

[ 274](pinctrl-r8a77961_8h.md#adf1bf8c2fcc769f431d7df7efcccae0d)#define FUNC\_PWM1\_A IPSR(1, 20, 0)

[ 275](pinctrl-r8a77961_8h.md#aace3bd2975ac2c946265ea00a0580c5c)#define FUNC\_HRX3\_D IPSR(1, 20, 3)

[ 276](pinctrl-r8a77961_8h.md#a16d47e8441f89006025c6b9b7e6c6ad6)#define FUNC\_VI4\_DATA7\_B IPSR(1, 20, 4)

[ 277](pinctrl-r8a77961_8h.md#aa7cc54dcf5bd0f60a08977f8b34f22ca)#define FUNC\_IERX\_B IPSR(1, 20, 9)

[ 278](pinctrl-r8a77961_8h.md#a80a0b0c820485bd387f8346ea56ca525)#define FUNC\_PWM2\_A IPSR(1, 24, 0)

[ 279](pinctrl-r8a77961_8h.md#a8e765a498e3133fbcd82c384b1e97aea)#define FUNC\_HTX3\_D IPSR(1, 24, 3)

[ 280](pinctrl-r8a77961_8h.md#a6bb53529302c02da87d96749017725c3)#define FUNC\_IETX\_B IPSR(1, 24, 9)

[ 281](pinctrl-r8a77961_8h.md#a82542c8e14d074784474230333c4511a)#define FUNC\_A0 IPSR(1, 28, 0)

[ 282](pinctrl-r8a77961_8h.md#aee9e9432d4be69632a54cc11a10a7d9f)#define FUNC\_LCDOUT16 IPSR(1, 28, 1)

[ 283](pinctrl-r8a77961_8h.md#a95f48da02bd9dfec58caf6439da03d98)#define FUNC\_MSIOF3\_SYNC\_B IPSR(1, 28, 2)

[ 284](pinctrl-r8a77961_8h.md#aa2d4b5219c2385853056ccef30c4e60f)#define FUNC\_VI4\_DATA8 IPSR(1, 28, 4)

[ 285](pinctrl-r8a77961_8h.md#a24ba94d5461c1d2988c2cea027fbb667)#define FUNC\_DU\_DB0 IPSR(1, 28, 6)

[ 286](pinctrl-r8a77961_8h.md#a60c5129d8b820a3f0b91be32eb3eae6c)#define FUNC\_PWM3\_A IPSR(1, 28, 9)

[ 287](pinctrl-r8a77961_8h.md#a245bc010d62232c00c747c0af6158ad3)#define FUNC\_A1 IPSR(2, 0, 0)

[ 288](pinctrl-r8a77961_8h.md#a802505ae44609702f3a5b94673c7a19d)#define FUNC\_LCDOUT17 IPSR(2, 0, 1)

[ 289](pinctrl-r8a77961_8h.md#a4d03c5588de4ba7ee8f627303636f8d3)#define FUNC\_MSIOF3\_TXD\_B IPSR(2, 0, 2)

[ 290](pinctrl-r8a77961_8h.md#a0d5db26065fb1e107bb47ff952722dfd)#define FUNC\_VI4\_DATA9 IPSR(2, 0, 4)

[ 291](pinctrl-r8a77961_8h.md#a69676443cc56c845274f8d58da5c40dc)#define FUNC\_DU\_DB1 IPSR(2, 0, 6)

[ 292](pinctrl-r8a77961_8h.md#ad9528c1d4e7d1f6cdbcabbf317687b79)#define FUNC\_PWM4\_A IPSR(2, 0, 9)

[ 293](pinctrl-r8a77961_8h.md#a50bab7ab18f8a1c7bbfc147486b7a35c)#define FUNC\_A2 IPSR(2, 4, 0)

[ 294](pinctrl-r8a77961_8h.md#afce1503c4cb8688f315e936801246556)#define FUNC\_LCDOUT18 IPSR(2, 4, 1)

[ 295](pinctrl-r8a77961_8h.md#af4e24ae32949438e8dc4459705753ce1)#define FUNC\_MSIOF3\_SCK\_B IPSR(2, 4, 2)

[ 296](pinctrl-r8a77961_8h.md#aa08f2d8e8da50c579ab058c25c3ec8fb)#define FUNC\_VI4\_DATA10 IPSR(2, 4, 4)

[ 297](pinctrl-r8a77961_8h.md#a2355563188a47a0ac72b88292b9a5833)#define FUNC\_DU\_DB2 IPSR(2, 4, 6)

[ 298](pinctrl-r8a77961_8h.md#a3f60563fe20677176b7b393dd465437e)#define FUNC\_PWM5\_A IPSR(2, 4, 9)

[ 299](pinctrl-r8a77961_8h.md#ac1d0223b38b7ddf9b6e17cee4d409eca)#define FUNC\_A3 IPSR(2, 8, 0)

[ 300](pinctrl-r8a77961_8h.md#a78045005190ca1f8e06ae2dea0671440)#define FUNC\_LCDOUT19 IPSR(2, 8, 1)

[ 301](pinctrl-r8a77961_8h.md#afaac12bf2d23eebf05b7f8b8a8b25a75)#define FUNC\_MSIOF3\_RXD\_B IPSR(2, 8, 2)

[ 302](pinctrl-r8a77961_8h.md#a8d3868bf1cb6425d05b836ac134ca098)#define FUNC\_VI4\_DATA11 IPSR(2, 8, 4)

[ 303](pinctrl-r8a77961_8h.md#acfb7686323805425b79b5ff4b4730e04)#define FUNC\_DU\_DB3 IPSR(2, 8, 6)

[ 304](pinctrl-r8a77961_8h.md#a40dba50f3a36cf461c4e43621b6e34dc)#define FUNC\_PWM6\_A IPSR(2, 8, 9)

[ 305](pinctrl-r8a77961_8h.md#a8ccb9f2342e02f6b9eae1e1262b7f99e)#define FUNC\_A4 IPSR(2, 12, 0)

[ 306](pinctrl-r8a77961_8h.md#a70b0f12bed5be8e2fac91b38938fe69b)#define FUNC\_LCDOUT20 IPSR(2, 12, 1)

[ 307](pinctrl-r8a77961_8h.md#ae9043fbb2f20864ed39a6d316134bb21)#define FUNC\_MSIOF3\_SS1\_B IPSR(2, 12, 2)

[ 308](pinctrl-r8a77961_8h.md#a31c32aec54a46da1790d01e6f06a5f83)#define FUNC\_VI4\_DATA12 IPSR(2, 12, 4)

[ 309](pinctrl-r8a77961_8h.md#aeb0c85e9d17bfa6fa585f2e14169380d)#define FUNC\_VI5\_DATA12 IPSR(2, 12, 5)

[ 310](pinctrl-r8a77961_8h.md#a7a95bfd9aab4d4cb77fb21625a4d642b)#define FUNC\_DU\_DB4 IPSR(2, 12, 6)

[ 311](pinctrl-r8a77961_8h.md#ac8bd5e9889d4f157211dbfaebf983ad0)#define FUNC\_A5 IPSR(2, 16, 0)

[ 312](pinctrl-r8a77961_8h.md#a6cc1f5d26ddab09988f44104fb7373f9)#define FUNC\_LCDOUT21 IPSR(2, 16, 1)

[ 313](pinctrl-r8a77961_8h.md#a613168edac605e88fb45c34170e15e4f)#define FUNC\_MSIOF3\_SS2\_B IPSR(2, 16, 2)

[ 314](pinctrl-r8a77961_8h.md#adb92e0ecd2a664705188fd53a1eec22b)#define FUNC\_SCK4\_B IPSR(2, 16, 3)

[ 315](pinctrl-r8a77961_8h.md#a12b4bd22a73e8b671eda333e06a2b3d9)#define FUNC\_VI4\_DATA13 IPSR(2, 16, 4)

[ 316](pinctrl-r8a77961_8h.md#a237d2b1fe4d386998bd8f720a13823b7)#define FUNC\_VI5\_DATA13 IPSR(2, 16, 5)

[ 317](pinctrl-r8a77961_8h.md#ab4e179859ce500ce75911d45d8fda5d6)#define FUNC\_DU\_DB5 IPSR(2, 16, 6)

[ 318](pinctrl-r8a77961_8h.md#a5dc930bcfa7f880963f033264e09b36e)#define FUNC\_A6 IPSR(2, 20, 0)

[ 319](pinctrl-r8a77961_8h.md#a6cc1828bb9e279bdf416566026b570c2)#define FUNC\_LCDOUT22 IPSR(2, 20, 1)

[ 320](pinctrl-r8a77961_8h.md#ac69047539e8fefb746cf7cfcebdb4238)#define FUNC\_MSIOF2\_SS1\_A IPSR(2, 20, 2)

[ 321](pinctrl-r8a77961_8h.md#a7989e51885bec3ffd5a6b9cf03932fbd)#define FUNC\_RX4\_B IPSR(2, 20, 3)

[ 322](pinctrl-r8a77961_8h.md#ad6cc6695cdf8ef774999de06e7c0028b)#define FUNC\_VI4\_DATA14 IPSR(2, 20, 4)

[ 323](pinctrl-r8a77961_8h.md#aff8d59f720ad146c36a12dd54dfdd9c9)#define FUNC\_VI5\_DATA14 IPSR(2, 20, 5)

[ 324](pinctrl-r8a77961_8h.md#aed8322e2218d56b3c24d307137c678bc)#define FUNC\_DU\_DB6 IPSR(2, 20, 6)

[ 325](pinctrl-r8a77961_8h.md#adff4911dd202d5a673bccca6a7dd7e74)#define FUNC\_A7 IPSR(2, 24, 0)

[ 326](pinctrl-r8a77961_8h.md#ab70d01b1d336c9330345835315721ede)#define FUNC\_LCDOUT23 IPSR(2, 24, 1)

[ 327](pinctrl-r8a77961_8h.md#a3bd7e5c250d6f94dce34d278711aa046)#define FUNC\_MSIOF2\_SS2\_A IPSR(2, 24, 2)

[ 328](pinctrl-r8a77961_8h.md#aebb64925720074f52fb2a954aa3d000c)#define FUNC\_TX4\_B IPSR(2, 24, 3)

[ 329](pinctrl-r8a77961_8h.md#ab269f4cd00dd5723dfcfa65f4d68c845)#define FUNC\_VI4\_DATA15 IPSR(2, 24, 4)

[ 330](pinctrl-r8a77961_8h.md#ad6af0e1a134b03a6dcbe493f8d0514ce)#define FUNC\_VI5\_DATA15 IPSR(2, 24, 5)

[ 331](pinctrl-r8a77961_8h.md#a06cc24e514d629832ba069117db10585)#define FUNC\_DU\_DB7 IPSR(2, 24, 6)

[ 332](pinctrl-r8a77961_8h.md#a4bb11c5350434c63fd21d4243baccdf3)#define FUNC\_A8 IPSR(2, 28, 0)

[ 333](pinctrl-r8a77961_8h.md#aa7225989b97a62a788a6134d00fcb2ae)#define FUNC\_RX3\_B IPSR(2, 28, 1)

[ 334](pinctrl-r8a77961_8h.md#abe98d3b906e428ce607c6f3147894f72)#define FUNC\_MSIOF2\_SYNC\_A IPSR(2, 28, 2)

[ 335](pinctrl-r8a77961_8h.md#a3c6d53835985babbd853cae780e1b64b)#define FUNC\_HRX4\_B IPSR(2, 28, 3)

[ 336](pinctrl-r8a77961_8h.md#ad46f14e79672c028abb2c26d419c103a)#define FUNC\_SDA6\_A IPSR(2, 28, 7)

[ 337](pinctrl-r8a77961_8h.md#a1a8e16c11629f33340be866e86c36d8e)#define FUNC\_AVB\_AVTP\_MATCH\_B IPSR(2, 28, 8)

[ 338](pinctrl-r8a77961_8h.md#ae5751cdf768e48665fc46e4c21be7506)#define FUNC\_PWM1\_B IPSR(2, 28, 9)

[ 339](pinctrl-r8a77961_8h.md#a231fc0ab2c304948a72eb65da6a1bd11)#define FUNC\_A9 IPSR(3, 0, 0)

[ 340](pinctrl-r8a77961_8h.md#a687a959420be7cb68a62249b68fa62a9)#define FUNC\_MSIOF2\_SCK\_A IPSR(3, 0, 2)

[ 341](pinctrl-r8a77961_8h.md#a7b9218b44f0419c7a7d0887029cadf21)#define FUNC\_CTS4\_N\_B IPSR(3, 0, 3)

[ 342](pinctrl-r8a77961_8h.md#aab83c50e2b99c93e141679a4228b208d)#define FUNC\_VI5\_VSYNC\_N IPSR(3, 0, 5)

[ 343](pinctrl-r8a77961_8h.md#a52e5d5c37bdbfa753285708d144b33b2)#define FUNC\_A10 IPSR(3, 4, 0)

[ 344](pinctrl-r8a77961_8h.md#af11dcff07630407ad2d444d32eb7c5a8)#define FUNC\_MSIOF2\_RXD\_A IPSR(3, 4, 2)

[ 345](pinctrl-r8a77961_8h.md#a90f38b71bea67ef2449470e205e1b554)#define FUNC\_RTS4\_N\_B IPSR(3, 4, 3)

[ 346](pinctrl-r8a77961_8h.md#ad233da2ead299c2cdf470646058ea747)#define FUNC\_VI5\_HSYNC\_N IPSR(3, 4, 5)

[ 347](pinctrl-r8a77961_8h.md#a6f7fe20b20915fa395b273ecae73432e)#define FUNC\_A11 IPSR(3, 8, 0)

[ 348](pinctrl-r8a77961_8h.md#aa4813d235e6ca910d6b10457b9a7c5ed)#define FUNC\_TX3\_B IPSR(3, 8, 1)

[ 349](pinctrl-r8a77961_8h.md#aa4d83c335cedd408bcf6d5d4a8a19404)#define FUNC\_MSIOF2\_TXD\_A IPSR(3, 8, 2)

[ 350](pinctrl-r8a77961_8h.md#ac705b7f93897952a4ec9e7e3b1e48b59)#define FUNC\_HTX4\_B IPSR(3, 8, 3)

[ 351](pinctrl-r8a77961_8h.md#af901e818787a6adcc6e8a859a22938e1)#define FUNC\_HSCK4 IPSR(3, 8, 4)

[ 352](pinctrl-r8a77961_8h.md#af24855a9f8f61a297aa1d4619ee9b0c7)#define FUNC\_VI5\_FIELD IPSR(3, 8, 5)

[ 353](pinctrl-r8a77961_8h.md#acd71f8485509266570e33401bc4d90df)#define FUNC\_SCL6\_A IPSR(3, 8, 7)

[ 354](pinctrl-r8a77961_8h.md#aa2ed9d87e3e81a85e175ff7ee0836669)#define FUNC\_AVB\_AVTP\_CAPTURE\_B IPSR(3, 8, 8)

[ 355](pinctrl-r8a77961_8h.md#aac29c6c3fa8d7b74a2ab021cac5c26bf)#define FUNC\_PWM2\_B IPSR(3, 8, 9)

[ 356](pinctrl-r8a77961_8h.md#a47eafef4138a18ef06fadfb1fea708a2)#define FUNC\_A12 IPSR(3, 12, 0)

[ 357](pinctrl-r8a77961_8h.md#a8ba33cf94b25f4c5a2bb8e50ba92a2da)#define FUNC\_LCDOUT12 IPSR(3, 12, 1)

[ 358](pinctrl-r8a77961_8h.md#a4a696ba0b59041845d05a42f959b4d40)#define FUNC\_MSIOF3\_SCK\_C IPSR(3, 12, 2)

[ 359](pinctrl-r8a77961_8h.md#a1d025549119571eb8e2385f28821a83f)#define FUNC\_HRX4\_A IPSR(3, 12, 4)

[ 360](pinctrl-r8a77961_8h.md#a29f6af7113d5ba63d2eeb07c6f0635cb)#define FUNC\_VI5\_DATA8 IPSR(3, 12, 5)

[ 361](pinctrl-r8a77961_8h.md#a00a437bb83036a71e00f9c1cb1ead453)#define FUNC\_DU\_DG4 IPSR(3, 12, 6)

[ 362](pinctrl-r8a77961_8h.md#a49f2b1fe01e478371f3503da8f781696)#define FUNC\_A13 IPSR(3, 16, 0)

[ 363](pinctrl-r8a77961_8h.md#a67c0be5b1a325586e7dd3404d87e04a3)#define FUNC\_LCDOUT13 IPSR(3, 16, 1)

[ 364](pinctrl-r8a77961_8h.md#adb3dd8b79f3e1efbdeb511599417fe9d)#define FUNC\_MSIOF3\_SYNC\_C IPSR(3, 16, 2)

[ 365](pinctrl-r8a77961_8h.md#a1b7922d705a5d87c167954c337ad5d2f)#define FUNC\_HTX4\_A IPSR(3, 16, 4)

[ 366](pinctrl-r8a77961_8h.md#af3a1d8e07e5ab258a591c2311f2b2f4f)#define FUNC\_VI5\_DATA9 IPSR(3, 16, 5)

[ 367](pinctrl-r8a77961_8h.md#a7e50dcb999fa583663b1d840ff072f11)#define FUNC\_DU\_DG5 IPSR(3, 16, 6)

[ 368](pinctrl-r8a77961_8h.md#ab15884b5fc4f1dbffed97a77b91b833e)#define FUNC\_A14 IPSR(3, 20, 0)

[ 369](pinctrl-r8a77961_8h.md#a3efe2e9ccf6f5140c0665a319e97a7aa)#define FUNC\_LCDOUT14 IPSR(3, 20, 1)

[ 370](pinctrl-r8a77961_8h.md#a7af767ef0b452ad4957b2d0bcfa405b5)#define FUNC\_MSIOF3\_RXD\_C IPSR(3, 20, 2)

[ 371](pinctrl-r8a77961_8h.md#a1c54400528911a15e85505511e391189)#define FUNC\_HCTS4\_N IPSR(3, 20, 4)

[ 372](pinctrl-r8a77961_8h.md#a4db40e98f4409e2db36f9c697a5093e3)#define FUNC\_VI5\_DATA10 IPSR(3, 20, 5)

[ 373](pinctrl-r8a77961_8h.md#a4128a892c50ce1a913e2d9fa45a5a56d)#define FUNC\_DU\_DG6 IPSR(3, 20, 6)

[ 374](pinctrl-r8a77961_8h.md#af1e4298daf54deea2a2ae606813f33b9)#define FUNC\_A15 IPSR(3, 24, 0)

[ 375](pinctrl-r8a77961_8h.md#a39d3a253bc42560f3c932db1310b65ab)#define FUNC\_LCDOUT15 IPSR(3, 24, 1)

[ 376](pinctrl-r8a77961_8h.md#ae572e9d262c03cc33e804c2a86e3d8d9)#define FUNC\_MSIOF3\_TXD\_C IPSR(3, 24, 2)

[ 377](pinctrl-r8a77961_8h.md#aa10fe06f0af251d8a1519c47095a4463)#define FUNC\_HRTS4\_N IPSR(3, 24, 4)

[ 378](pinctrl-r8a77961_8h.md#a14ea2008fa7d992adda32ce6fc1ca29b)#define FUNC\_VI5\_DATA11 IPSR(3, 24, 5)

[ 379](pinctrl-r8a77961_8h.md#a7fa2c8809d292effb401a0ce607d0613)#define FUNC\_DU\_DG7 IPSR(3, 24, 6)

[ 380](pinctrl-r8a77961_8h.md#a55c475273d4c855aaffe092b316713c2)#define FUNC\_A16 IPSR(3, 28, 0)

[ 381](pinctrl-r8a77961_8h.md#aaf59b2c7e3e28bfaeb40f79bdc482d5f)#define FUNC\_LCDOUT8 IPSR(3, 28, 1)

[ 382](pinctrl-r8a77961_8h.md#ac280cc353c96cf2988b39f2f25944321)#define FUNC\_VI4\_FIELD IPSR(3, 28, 4)

[ 383](pinctrl-r8a77961_8h.md#ae7091485342a527fd1f1cc1207a4f29e)#define FUNC\_DU\_DG0 IPSR(3, 28, 6)

[ 384](pinctrl-r8a77961_8h.md#a76999e500295773619f04e09fd468abd)#define FUNC\_A17 IPSR(4, 0, 0)

[ 385](pinctrl-r8a77961_8h.md#a75f6705fc49c3aa3a45382ff0ac4ef21)#define FUNC\_LCDOUT9 IPSR(4, 0, 1)

[ 386](pinctrl-r8a77961_8h.md#a76a940ca03e3fd95c6978f60a5084656)#define FUNC\_VI4\_VSYNC\_N IPSR(4, 0, 4)

[ 387](pinctrl-r8a77961_8h.md#aaf5e343aa22c463947e37bd9887cd966)#define FUNC\_DU\_DG1 IPSR(4, 0, 6)

[ 388](pinctrl-r8a77961_8h.md#a840cdd648fb5c50818bcb7dfcf74d6a8)#define FUNC\_A18 IPSR(4, 4, 0)

[ 389](pinctrl-r8a77961_8h.md#a5210651e6115574c0c734b7d79421096)#define FUNC\_LCDOUT10 IPSR(4, 4, 1)

[ 390](pinctrl-r8a77961_8h.md#a323368ddb2386feca222cc704f5f2156)#define FUNC\_VI4\_HSYNC\_N IPSR(4, 4, 4)

[ 391](pinctrl-r8a77961_8h.md#a8f43c1146335c531ce652a639f27dd59)#define FUNC\_DU\_DG2 IPSR(4, 4, 6)

[ 392](pinctrl-r8a77961_8h.md#a87d1f115c57b5a7621b0cf169fa9ac1f)#define FUNC\_A19 IPSR(4, 8, 0)

[ 393](pinctrl-r8a77961_8h.md#a8cb08d5f379cb73273297353310ca961)#define FUNC\_LCDOUT11 IPSR(4, 8, 1)

[ 394](pinctrl-r8a77961_8h.md#ae70f1798943a6f8f6695eebf188ece6f)#define FUNC\_VI4\_CLKENB IPSR(4, 8, 4)

[ 395](pinctrl-r8a77961_8h.md#af0dc163e7750fa5c3a448aac4713f7fa)#define FUNC\_DU\_DG3 IPSR(4, 8, 6)

[ 396](pinctrl-r8a77961_8h.md#a8cde0ac9b631893bcfe0722127c9b6ac)#define FUNC\_CS0\_N IPSR(4, 12, 0)

[ 397](pinctrl-r8a77961_8h.md#a634c538e8c3706cfd73d0b10ee0c1f5a)#define FUNC\_VI5\_CLKENB IPSR(4, 12, 5)

[ 398](pinctrl-r8a77961_8h.md#a1676aec73c9eb9d01bb2e0fd175d4e76)#define FUNC\_CS1\_N IPSR(4, 16, 0)

[ 399](pinctrl-r8a77961_8h.md#a20c2b74fbf418bb8b4160b58ae3824b2)#define FUNC\_VI5\_CLK IPSR(4, 16, 5)

[ 400](pinctrl-r8a77961_8h.md#a254b39378270d49e720f6a33575095c1)#define FUNC\_EX\_WAIT0\_B IPSR(4, 16, 7)

[ 401](pinctrl-r8a77961_8h.md#afb40386f732c7051fdc4bbee033810db)#define FUNC\_BS\_N IPSR(4, 20, 0)

[ 402](pinctrl-r8a77961_8h.md#ad95cd1d8336e4baed27891dcac28198b)#define FUNC\_QSTVA\_QVS IPSR(4, 20, 1)

[ 403](pinctrl-r8a77961_8h.md#a960facf51198a79699fe4067e956a46e)#define FUNC\_MSIOF3\_SCK\_D IPSR(4, 20, 2)

[ 404](pinctrl-r8a77961_8h.md#aef23d90678d28a442690cf64f7d9f658)#define FUNC\_SCK3 IPSR(4, 20, 3)

[ 405](pinctrl-r8a77961_8h.md#ab969df1d788a635cabbe5cc64e1cea61)#define FUNC\_HSCK3 IPSR(4, 20, 4)

[ 406](pinctrl-r8a77961_8h.md#a7496205fb69cbe95aadfaf7f3638f2a0)#define FUNC\_CAN1\_TX IPSR(4, 20, 8)

[ 407](pinctrl-r8a77961_8h.md#a6df9e59065b1730b5469c0657e3fb275)#define FUNC\_CANFD1\_TX IPSR(4, 20, 9)

[ 408](pinctrl-r8a77961_8h.md#a078d910c8be24dff803f3a25518eea1e)#define FUNC\_IETX\_A IPSR(4, 20, 0xA)

[ 409](pinctrl-r8a77961_8h.md#aef6490f09653c1cd65bc102d7597662b)#define FUNC\_RD\_N IPSR(4, 24, 0)

[ 410](pinctrl-r8a77961_8h.md#a0f78c18694edd20bc50eb132135fcfaa)#define FUNC\_MSIOF3\_SYNC\_D IPSR(4, 24, 2)

[ 411](pinctrl-r8a77961_8h.md#aae70a216a009d1202107cf691d6fa93f)#define FUNC\_RX3\_A IPSR(4, 24, 3)

[ 412](pinctrl-r8a77961_8h.md#a1f7dd6c7f50c928fd078b57f729262be)#define FUNC\_HRX3\_A IPSR(4, 24, 4)

[ 413](pinctrl-r8a77961_8h.md#ac753d0b083514de79b72428057a65e59)#define FUNC\_CAN0\_TX\_A IPSR(4, 24, 8)

[ 414](pinctrl-r8a77961_8h.md#a25d4915e92ff65926ede2801a8e69b10)#define FUNC\_CANFD0\_TX\_A IPSR(4, 24, 9)

[ 415](pinctrl-r8a77961_8h.md#aba7e68580cfce09c9c5e724c2f9d3a6a)#define FUNC\_RD\_WR\_N IPSR(4, 28, 0)

[ 416](pinctrl-r8a77961_8h.md#a487ac120c076bf5eadd3b5831ebcf91d)#define FUNC\_MSIOF3\_RXD\_D IPSR(4, 28, 2)

[ 417](pinctrl-r8a77961_8h.md#ac7a7b4e4e253bc25ae30efb2cc2ce34c)#define FUNC\_TX3\_A IPSR(4, 28, 3)

[ 418](pinctrl-r8a77961_8h.md#acf9dcc98af73e0f4250008c6776acb3c)#define FUNC\_HTX3\_A IPSR(4, 28, 4)

[ 419](pinctrl-r8a77961_8h.md#ab08d7c965972403cfa342725431fba7c)#define FUNC\_CAN0\_RX\_A IPSR(4, 28, 8)

[ 420](pinctrl-r8a77961_8h.md#abcc1ff95fa5c23389768011f7c6ab9e2)#define FUNC\_CANFD0\_RX\_A IPSR(4, 28, 9)

[ 421](pinctrl-r8a77961_8h.md#a8072fe9c7db7dfc7be6c254138542644)#define FUNC\_WE0\_N IPSR(5, 0, 0)

[ 422](pinctrl-r8a77961_8h.md#ac5c486b7a48ae907670f2658fc878629)#define FUNC\_MSIOF3\_TXD\_D IPSR(5, 0, 2)

[ 423](pinctrl-r8a77961_8h.md#a0f2117dc4381a92aadb82e812196a770)#define FUNC\_CTS3\_N IPSR(5, 0, 3)

[ 424](pinctrl-r8a77961_8h.md#aaa64b22be712661c25699263604cd57a)#define FUNC\_HCTS3\_N IPSR(5, 0, 4)

[ 425](pinctrl-r8a77961_8h.md#a531baf1d9465e773284447626930f091)#define FUNC\_SCL6\_B IPSR(5, 0, 7)

[ 426](pinctrl-r8a77961_8h.md#afcac264ad3a3695fb90d5ff284613c4b)#define FUNC\_CAN\_CLK IPSR(5, 0, 8)

[ 427](pinctrl-r8a77961_8h.md#a8d8688c8d2cd93e729c402eb519f1e8f)#define FUNC\_IECLK\_A IPSR(5, 0, 0xA)

[ 428](pinctrl-r8a77961_8h.md#afa6c55e88640bc528d7eea1cffc5b4f8)#define FUNC\_WE1\_N IPSR(5, 4, 0)

[ 429](pinctrl-r8a77961_8h.md#afbb53e4ace9d99ac0b70f7db81a2d60d)#define FUNC\_MSIOF3\_SS1\_D IPSR(5, 4, 2)

[ 430](pinctrl-r8a77961_8h.md#a62ad79fc0395e1919d66d7aeeb4c5198)#define FUNC\_RTS3\_N IPSR(5, 4, 3)

[ 431](pinctrl-r8a77961_8h.md#a91636ed706ff199ac7e5b6a6c2f300be)#define FUNC\_HRTS3\_N IPSR(5, 4, 4)

[ 432](pinctrl-r8a77961_8h.md#af34d2a869c3c86df14e7c0c574aa916d)#define FUNC\_SDA6\_B IPSR(5, 4, 7)

[ 433](pinctrl-r8a77961_8h.md#aff6508bc4dc9db56e0f0e05f172800d7)#define FUNC\_CAN1\_RX IPSR(5, 4, 8)

[ 434](pinctrl-r8a77961_8h.md#a0923a3e7753142d0ae437cb61a46f6b0)#define FUNC\_CANFD1\_RX IPSR(5, 4, 9)

[ 435](pinctrl-r8a77961_8h.md#aeb96347071db82ad693f2a4fcccd4228)#define FUNC\_IERX\_A IPSR(5, 4, 0xA)

[ 436](pinctrl-r8a77961_8h.md#a15aced10e5e2d6617677b94f0ebb9f75)#define FUNC\_EX\_WAIT0\_A IPSR(5, 8, 0)

[ 437](pinctrl-r8a77961_8h.md#ad4e2dafe96d3f75602e655920bc22012)#define FUNC\_QCLK IPSR(5, 8, 1)

[ 438](pinctrl-r8a77961_8h.md#a411f032723ec601041937d8904ae6f97)#define FUNC\_VI4\_CLK IPSR(5, 8, 4)

[ 439](pinctrl-r8a77961_8h.md#a3a31bdb5aeda7b4ce7ce01937c65b3ef)#define FUNC\_DU\_DOTCLKOUT0 IPSR(5, 8, 6)

[ 440](pinctrl-r8a77961_8h.md#a2d1deebc5fe3ef4b31476af49ca1db44)#define FUNC\_D0 IPSR(5, 12, 0)

[ 441](pinctrl-r8a77961_8h.md#a31664cb207adbf0bf9d870fc2a5773d8)#define FUNC\_MSIOF2\_SS1\_B IPSR(5, 12, 1)

[ 442](pinctrl-r8a77961_8h.md#abe228b3ed2eb46324a46edba1b0331e6)#define FUNC\_MSIOF3\_SCK\_A IPSR(5, 12, 2)

[ 443](pinctrl-r8a77961_8h.md#a6d59268c6578463443f631db065de12d)#define FUNC\_VI4\_DATA16 IPSR(5, 12, 4)

[ 444](pinctrl-r8a77961_8h.md#a849ed594a1343818a638b66d8b9d39fe)#define FUNC\_VI5\_DATA0 IPSR(5, 12, 5)

[ 445](pinctrl-r8a77961_8h.md#a0fcdac7069e4bc49b8ad5cf5148b2603)#define FUNC\_D1 IPSR(5, 16, 0)

[ 446](pinctrl-r8a77961_8h.md#aa4fe4dafe50244d8a93729adfe91df6f)#define FUNC\_MSIOF2\_SS2\_B IPSR(5, 16, 1)

[ 447](pinctrl-r8a77961_8h.md#a1b0e4a819c50e5fcbb73ef3297ef8bde)#define FUNC\_MSIOF3\_SYNC\_A IPSR(5, 16, 2)

[ 448](pinctrl-r8a77961_8h.md#a9c38f513dde33d22d3ef7e3b34dcfc04)#define FUNC\_VI4\_DATA17 IPSR(5, 16, 4)

[ 449](pinctrl-r8a77961_8h.md#a7fdca412d085fdc6dd6e73bfbfc1ca84)#define FUNC\_VI5\_DATA1 IPSR(5, 16, 5)

[ 450](pinctrl-r8a77961_8h.md#ad337d8e45ef06fecd25b66b709979675)#define FUNC\_D2 IPSR(5, 20, 0)

[ 451](pinctrl-r8a77961_8h.md#ac444d6fe8baddf8fd6d85310952d7aea)#define FUNC\_MSIOF3\_RXD\_A IPSR(5, 20, 2)

[ 452](pinctrl-r8a77961_8h.md#a333e10a0e489f5021d4b000afb9241cc)#define FUNC\_VI4\_DATA18 IPSR(5, 20, 4)

[ 453](pinctrl-r8a77961_8h.md#a56bdc751bad891043d8f2c6fc65bc46c)#define FUNC\_VI5\_DATA2 IPSR(5, 20, 5)

[ 454](pinctrl-r8a77961_8h.md#ac9d81add637e91947e61e2efe35f63b7)#define FUNC\_D3 IPSR(5, 24, 0)

[ 455](pinctrl-r8a77961_8h.md#a14a3e25e28796010cd70e4cc626360e6)#define FUNC\_MSIOF3\_TXD\_A IPSR(5, 24, 2)

[ 456](pinctrl-r8a77961_8h.md#a41d49db3b6ea100d5ce857d3e439e456)#define FUNC\_VI4\_DATA19 IPSR(5, 24, 4)

[ 457](pinctrl-r8a77961_8h.md#a12e8dfbc73bff78f9c8ec8e58d9fe440)#define FUNC\_VI5\_DATA3 IPSR(5, 24, 5)

[ 458](pinctrl-r8a77961_8h.md#a60578df45743c03b12dc7886bcac10fa)#define FUNC\_D4 IPSR(5, 28, 0)

[ 459](pinctrl-r8a77961_8h.md#ae602cb0fe3f883f9c6bda3bd85e09f07)#define FUNC\_MSIOF2\_SCK\_B IPSR(5, 28, 1)

[ 460](pinctrl-r8a77961_8h.md#af4d109e98894ef25b6f48f3eb98c6b3a)#define FUNC\_VI4\_DATA20 IPSR(5, 28, 4)

[ 461](pinctrl-r8a77961_8h.md#ac3d07dadff77bc677b5cefb36997f405)#define FUNC\_VI5\_DATA4 IPSR(5, 28, 5)

[ 462](pinctrl-r8a77961_8h.md#a0ff8af5076a31afd9214925805d5cef2)#define FUNC\_D5 IPSR(6, 0, 0)

[ 463](pinctrl-r8a77961_8h.md#ae01d42e73dc8c1630ef03873abe7aaa4)#define FUNC\_MSIOF2\_SYNC\_B IPSR(6, 0, 1)

[ 464](pinctrl-r8a77961_8h.md#a20defc343c13e1f4215233da336fab9e)#define FUNC\_VI4\_DATA21 IPSR(6, 0, 4)

[ 465](pinctrl-r8a77961_8h.md#ad26830b329e947de00322f53fe03738c)#define FUNC\_VI5\_DATA5 IPSR(6, 0, 5)

[ 466](pinctrl-r8a77961_8h.md#a76ae501b6f362684bcf785d492920daa)#define FUNC\_D6 IPSR(6, 4, 0)

[ 467](pinctrl-r8a77961_8h.md#ab78baa9c8cedac67eb58011a68f22dc0)#define FUNC\_MSIOF2\_RXD\_B IPSR(6, 4, 1)

[ 468](pinctrl-r8a77961_8h.md#a8aff327852c0ec2aace89df69e9a387e)#define FUNC\_VI4\_DATA22 IPSR(6, 4, 4)

[ 469](pinctrl-r8a77961_8h.md#a651eb6a9713efef76fc77c2d33f9f1d8)#define FUNC\_VI5\_DATA6 IPSR(6, 4, 5)

[ 470](pinctrl-r8a77961_8h.md#aa7484c93f9b3371163e5f9d3f3e0642b)#define FUNC\_D7 IPSR(6, 8, 0)

[ 471](pinctrl-r8a77961_8h.md#ae408a769e3362b129b2da7e088d8af22)#define FUNC\_MSIOF2\_TXD\_B IPSR(6, 8, 1)

[ 472](pinctrl-r8a77961_8h.md#a96a57ad6d17f2d1c822a62ef8c82de7c)#define FUNC\_VI4\_DATA23 IPSR(6, 8, 4)

[ 473](pinctrl-r8a77961_8h.md#a8e83a42b240fb601258d024b72a3bd5f)#define FUNC\_VI5\_DATA7 IPSR(6, 8, 5)

[ 474](pinctrl-r8a77961_8h.md#ae8cf489b64a6963a7179a039b2e550b7)#define FUNC\_D8 IPSR(6, 12, 0)

[ 475](pinctrl-r8a77961_8h.md#a499f06773f2d0f22703ade47e5f717c6)#define FUNC\_LCDOUT0 IPSR(6, 12, 1)

[ 476](pinctrl-r8a77961_8h.md#a156f621d1aa9b17e64b5d73f5d6d5ade)#define FUNC\_MSIOF2\_SCK\_D IPSR(6, 12, 2)

[ 477](pinctrl-r8a77961_8h.md#abd4c3d9a2a87272d9c9d9f4755a7f116)#define FUNC\_SCK4\_C IPSR(6, 12, 3)

[ 478](pinctrl-r8a77961_8h.md#aac8e704e75a2da6114163b0e96c2e72c)#define FUNC\_VI4\_DATA0\_A IPSR(6, 12, 4)

[ 479](pinctrl-r8a77961_8h.md#a7e02bc084477e90e46d2bc281d2bdfce)#define FUNC\_DU\_DR0 IPSR(6, 12, 6)

[ 480](pinctrl-r8a77961_8h.md#a5eda7294acd39ff14382b3a037de745e)#define FUNC\_D9 IPSR(6, 16, 0)

[ 481](pinctrl-r8a77961_8h.md#a96d047187167adc0d7db3fb0c7f0e624)#define FUNC\_LCDOUT1 IPSR(6, 16, 1)

[ 482](pinctrl-r8a77961_8h.md#aad51a791aebaa7b076a35fa09ebc6c61)#define FUNC\_MSIOF2\_SYNC\_D IPSR(6, 16, 2)

[ 483](pinctrl-r8a77961_8h.md#a1486a4e3a502d8d70c3fc65d1fa5b158)#define FUNC\_VI4\_DATA1\_A IPSR(6, 16, 4)

[ 484](pinctrl-r8a77961_8h.md#aab9c01d802c415677cf02247733e3a37)#define FUNC\_DU\_DR1 IPSR(6, 16, 6)

[ 485](pinctrl-r8a77961_8h.md#a836969d11e5b3bbc77b8cd4b06f4ce06)#define FUNC\_D10 IPSR(6, 20, 0)

[ 486](pinctrl-r8a77961_8h.md#a2be9f3074dd1748725ed83e540bd40b4)#define FUNC\_LCDOUT2 IPSR(6, 20, 1)

[ 487](pinctrl-r8a77961_8h.md#a8df343c2007a7a30c70040eee3c72042)#define FUNC\_MSIOF2\_RXD\_D IPSR(6, 20, 2)

[ 488](pinctrl-r8a77961_8h.md#a5133668f3f8e06d33af0c0382c0574de)#define FUNC\_HRX3\_B IPSR(6, 20, 3)

[ 489](pinctrl-r8a77961_8h.md#ad4d09d3eb74ae91362dc82e395153c6e)#define FUNC\_VI4\_DATA2\_A IPSR(6, 20, 4)

[ 490](pinctrl-r8a77961_8h.md#a5d7371bfdbd31213ecb4c64d91ef475f)#define FUNC\_CTS4\_N\_C IPSR(6, 20, 5)

[ 491](pinctrl-r8a77961_8h.md#ad80ffdba699a98b4bc26f029001ba69b)#define FUNC\_DU\_DR2 IPSR(6, 20, 6)

[ 492](pinctrl-r8a77961_8h.md#ae44e703460dc282696160dfccc3dadce)#define FUNC\_D11 IPSR(6, 24, 0)

[ 493](pinctrl-r8a77961_8h.md#a509974319e07851767369b1efb2069cc)#define FUNC\_LCDOUT3 IPSR(6, 24, 1)

[ 494](pinctrl-r8a77961_8h.md#ac143028798f992f5aea32f1ea2ed9d67)#define FUNC\_MSIOF2\_TXD\_D IPSR(6, 24, 2)

[ 495](pinctrl-r8a77961_8h.md#add9eb35321d8faae38851a8754d44f2f)#define FUNC\_HTX3\_B IPSR(6, 24, 3)

[ 496](pinctrl-r8a77961_8h.md#a9d7a88c5dac303c3b2fb47f56f50c89a)#define FUNC\_VI4\_DATA3\_A IPSR(6, 24, 4)

[ 497](pinctrl-r8a77961_8h.md#acec80240e99dca2c70b012b2e2bde99d)#define FUNC\_RTS4\_N\_C IPSR(6, 24, 5)

[ 498](pinctrl-r8a77961_8h.md#aa3d151458fb4943038164caec5e9f415)#define FUNC\_DU\_DR3 IPSR(6, 24, 6)

[ 499](pinctrl-r8a77961_8h.md#a80029f62925702c281718e463dac17da)#define FUNC\_D12 IPSR(6, 28, 0)

[ 500](pinctrl-r8a77961_8h.md#ab2cc319229a46f036185010fde5dc5a1)#define FUNC\_LCDOUT4 IPSR(6, 28, 1)

[ 501](pinctrl-r8a77961_8h.md#af9d33720093b0c6f3c59fb434c2c57ac)#define FUNC\_MSIOF2\_SS1\_D IPSR(6, 28, 2)

[ 502](pinctrl-r8a77961_8h.md#a31e7f0d7f484a7afe6ce36572f1bf356)#define FUNC\_RX4\_C IPSR(6, 28, 3)

[ 503](pinctrl-r8a77961_8h.md#aa5c1e437361247b5b59fa664ea24680e)#define FUNC\_VI4\_DATA4\_A IPSR(6, 28, 4)

[ 504](pinctrl-r8a77961_8h.md#a106727d9435e00b0f3bfbfe392983425)#define FUNC\_DU\_DR4 IPSR(6, 28, 6)

[ 505](pinctrl-r8a77961_8h.md#a86b99a7ee58714f10c6d7fa3504d657f)#define FUNC\_D13 IPSR(7, 0, 0)

[ 506](pinctrl-r8a77961_8h.md#a9971bc6c1bd31c60db8bc1b24b06c095)#define FUNC\_LCDOUT5 IPSR(7, 0, 1)

[ 507](pinctrl-r8a77961_8h.md#ac8780dc1cfbd5613a12e73961f938cad)#define FUNC\_MSIOF2\_SS2\_D IPSR(7, 0, 2)

[ 508](pinctrl-r8a77961_8h.md#a381e12a638afd15fa7fda53027a862f7)#define FUNC\_TX4\_C IPSR(7, 0, 3)

[ 509](pinctrl-r8a77961_8h.md#a42905e476454dc3b76b962bb4a5ab2b7)#define FUNC\_VI4\_DATA5\_A IPSR(7, 0, 4)

[ 510](pinctrl-r8a77961_8h.md#aac107fddecb2d4b28af35c336ae82ba9)#define FUNC\_DU\_DR5 IPSR(7, 0, 6)

[ 511](pinctrl-r8a77961_8h.md#a1f1e1bdad6842c3b119f087cf6518112)#define FUNC\_D14 IPSR(7, 4, 0)

[ 512](pinctrl-r8a77961_8h.md#a24efeacb66b35f64a67c625fe510314e)#define FUNC\_LCDOUT6 IPSR(7, 4, 1)

[ 513](pinctrl-r8a77961_8h.md#a6449c4d858fddd7c4b20588414839284)#define FUNC\_MSIOF3\_SS1\_A IPSR(7, 4, 2)

[ 514](pinctrl-r8a77961_8h.md#afd900770c0458318fdeee2cecc17837d)#define FUNC\_HRX3\_C IPSR(7, 4, 3)

[ 515](pinctrl-r8a77961_8h.md#ad77c31890bb60aa88e7b61dea7046cf9)#define FUNC\_VI4\_DATA6\_A IPSR(7, 4, 4)

[ 516](pinctrl-r8a77961_8h.md#ab91d5ec267eea290fed15d0c58f3b148)#define FUNC\_DU\_DR6 IPSR(7, 4, 6)

[ 517](pinctrl-r8a77961_8h.md#afecefef5d4086e1589c46ec2499972f0)#define FUNC\_SCL6\_C IPSR(7, 4, 7)

[ 518](pinctrl-r8a77961_8h.md#a6ddcecb483a28cef738e5ccc0c9aa57c)#define FUNC\_D15 IPSR(7, 8, 0)

[ 519](pinctrl-r8a77961_8h.md#a05d2ec39e0618f08ec913e4cc82e9b97)#define FUNC\_LCDOUT7 IPSR(7, 8, 1)

[ 520](pinctrl-r8a77961_8h.md#a8b2e22b9a72bda5808161e2e00c8b7d0)#define FUNC\_MSIOF3\_SS2\_A IPSR(7, 8, 2)

[ 521](pinctrl-r8a77961_8h.md#a623caa2e478d6e0da6dd150b3dc6c530)#define FUNC\_HTX3\_C IPSR(7, 8, 3)

[ 522](pinctrl-r8a77961_8h.md#ad615085b7331b6778a512d24798b6c8f)#define FUNC\_VI4\_DATA7\_A IPSR(7, 8, 4)

[ 523](pinctrl-r8a77961_8h.md#ab8d64aa2dd319091ebb5d334f89cf51e)#define FUNC\_DU\_DR7 IPSR(7, 8, 6)

[ 524](pinctrl-r8a77961_8h.md#adc2d830c257016250e4ed42da7647cb6)#define FUNC\_SDA6\_C IPSR(7, 8, 7)

[ 525](pinctrl-r8a77961_8h.md#a5ce6a833bb0ad61190df883918cfdb90)#define FUNC\_SD0\_CLK IPSR(7, 16, 0)

[ 526](pinctrl-r8a77961_8h.md#aa7d63d84e5c661c454423acac263bc48)#define FUNC\_MSIOF1\_SCK\_E IPSR(7, 16, 2)

[ 527](pinctrl-r8a77961_8h.md#a0a2a9cd354c50ddab62374856dbe17a8)#define FUNC\_STP\_OPWM\_0\_B IPSR(7, 16, 6)

[ 528](pinctrl-r8a77961_8h.md#af9797ea2cd593d5d977be6b159576295)#define FUNC\_SD0\_CMD IPSR(7, 20, 0)

[ 529](pinctrl-r8a77961_8h.md#a1d6b239aa7be51e46e5961965deedc62)#define FUNC\_MSIOF1\_SYNC\_E IPSR(7, 20, 2)

[ 530](pinctrl-r8a77961_8h.md#afff27c6f53eca0f5048e94935634b5f4)#define FUNC\_STP\_IVCXO27\_0\_B IPSR(7, 20, 6)

[ 531](pinctrl-r8a77961_8h.md#abcf11d2e31a515ebb0694e7d16e2c187)#define FUNC\_SD0\_DAT0 IPSR(7, 24, 0)

[ 532](pinctrl-r8a77961_8h.md#a22c246c82a1be13ba57c2c3c6bc09f5c)#define FUNC\_MSIOF1\_RXD\_E IPSR(7, 24, 2)

[ 533](pinctrl-r8a77961_8h.md#a7b75e994d1fa353e8500fd66702c2583)#define FUNC\_TS\_SCK0\_B IPSR(7, 24, 5)

[ 534](pinctrl-r8a77961_8h.md#a00dc7ab443cbd3c897c155e2f2896ec8)#define FUNC\_STP\_ISCLK\_0\_B IPSR(7, 24, 6)

[ 535](pinctrl-r8a77961_8h.md#a5c694af48f26214df863de31b91266ff)#define FUNC\_SD0\_DAT1 IPSR(7, 28, 0)

[ 536](pinctrl-r8a77961_8h.md#a298ae3272a7c17e39ad9f9f8d6b276d0)#define FUNC\_MSIOF1\_TXD\_E IPSR(7, 28, 2)

[ 537](pinctrl-r8a77961_8h.md#abea46ac3a484f76b12cf88a923e497f3)#define FUNC\_TS\_SPSYNC0\_B IPSR(7, 28, 5)

[ 538](pinctrl-r8a77961_8h.md#a1018c641163c16d43be6ff3ffdc33646)#define FUNC\_STP\_ISSYNC\_0\_B IPSR(7, 28, 6)

[ 539](pinctrl-r8a77961_8h.md#ad4a067fdab442ccac531e74fb19e9f53)#define FUNC\_SD0\_DAT2 IPSR(8, 0, 0)

[ 540](pinctrl-r8a77961_8h.md#a4eefd68d32859d5846c3c705b27da6c5)#define FUNC\_MSIOF1\_SS1\_E IPSR(8, 0, 2)

[ 541](pinctrl-r8a77961_8h.md#ad8823000db8fcbae8810203da03d5b86)#define FUNC\_TS\_SDAT0\_B IPSR(8, 0, 5)

[ 542](pinctrl-r8a77961_8h.md#a41b22fe7771c1c8f45363dc6a73e8a42)#define FUNC\_STP\_ISD\_0\_B IPSR(8, 0, 6)

[ 543](pinctrl-r8a77961_8h.md#aa3102eee3d55a85934f8e2c8a623130a)#define FUNC\_SD0\_DAT3 IPSR(8, 4, 0)

[ 544](pinctrl-r8a77961_8h.md#acba5b78e251f9b5fc07a90e8395f8663)#define FUNC\_MSIOF1\_SS2\_E IPSR(8, 4, 2)

[ 545](pinctrl-r8a77961_8h.md#a42fc33b2a243f3c0f63eaf3ee9dfb6d0)#define FUNC\_TS\_SDEN0\_B IPSR(8, 4, 5)

[ 546](pinctrl-r8a77961_8h.md#aa00e32649237db7e63602056729ab6df)#define FUNC\_STP\_ISEN\_0\_B IPSR(8, 4, 6)

[ 547](pinctrl-r8a77961_8h.md#a81cf49d2922e723432c8076e65638fe2)#define FUNC\_SD1\_CLK IPSR(8, 8, 0)

[ 548](pinctrl-r8a77961_8h.md#ad52cf46f6ed3f28ede10db0fbaca140c)#define FUNC\_MSIOF1\_SCK\_G IPSR(8, 8, 2)

[ 549](pinctrl-r8a77961_8h.md#aed1f7bb7ad6d6c04b6cfc8640369d681)#define FUNC\_SIM0\_CLK\_A IPSR(8, 8, 5)

[ 550](pinctrl-r8a77961_8h.md#a4d6984780c71b7fb7910101abe09c271)#define FUNC\_SD1\_CMD IPSR(8, 12, 0)

[ 551](pinctrl-r8a77961_8h.md#abfdd06db0064f6ff8e75c0d39be88d53)#define FUNC\_MSIOF1\_SYNC\_G IPSR(8, 12, 2)

[ 552](pinctrl-r8a77961_8h.md#a59a213a423b381ae044cadaaedcb72cf)#define FUNC\_NFCE\_N\_B IPSR(8, 12, 3)

[ 553](pinctrl-r8a77961_8h.md#aff217229a6fb0cea947197687f557f5d)#define FUNC\_SIM0\_D\_A IPSR(8, 12, 5)

[ 554](pinctrl-r8a77961_8h.md#a074a830e395a1741662b651c75b3d978)#define FUNC\_STP\_IVCXO27\_1\_B IPSR(8, 12, 6)

[ 555](pinctrl-r8a77961_8h.md#a568164086138248b2fdf66a2e43022dd)#define FUNC\_SD1\_DAT0 IPSR(8, 16, 0)

[ 556](pinctrl-r8a77961_8h.md#a4df55f6f90dd4bce5705ac24e9cc0600)#define FUNC\_SD2\_DAT4 IPSR(8, 16, 1)

[ 557](pinctrl-r8a77961_8h.md#a1790467dae781acf8106f1925e85a4cd)#define FUNC\_MSIOF1\_RXD\_G IPSR(8, 16, 2)

[ 558](pinctrl-r8a77961_8h.md#a4935d55523a7f6c6a9366d544207f73f)#define FUNC\_NFWP\_N\_B IPSR(8, 16, 3)

[ 559](pinctrl-r8a77961_8h.md#a3a6b37eb65a935b465c09cc1ae7d6bee)#define FUNC\_TS\_SCK1\_B IPSR(8, 16, 5)

[ 560](pinctrl-r8a77961_8h.md#a449b05708ed25741d595b1592672e71b)#define FUNC\_STP\_ISCLK\_1\_B IPSR(8, 16, 6)

[ 561](pinctrl-r8a77961_8h.md#a51c01c73de6ebc9a98d4faadb1c63bad)#define FUNC\_SD1\_DAT1 IPSR(8, 20, 0)

[ 562](pinctrl-r8a77961_8h.md#ab37ea755a87ec6f89e93911184c1cd0c)#define FUNC\_SD2\_DAT5 IPSR(8, 20, 1)

[ 563](pinctrl-r8a77961_8h.md#a4e6724b602c5d50b473af10c6baf5ee1)#define FUNC\_MSIOF1\_TXD\_G IPSR(8, 20, 2)

[ 564](pinctrl-r8a77961_8h.md#ab9a1ef1ed64e90861fcc7e6d2ffbb013)#define FUNC\_NFDATA14\_B IPSR(8, 20, 3)

[ 565](pinctrl-r8a77961_8h.md#a572de7fe0f1e2063a7bb5c50e80017af)#define FUNC\_TS\_SPSYNC1\_B IPSR(8, 20, 5)

[ 566](pinctrl-r8a77961_8h.md#a822d3d2361978094c5a27a67a51d83c3)#define FUNC\_STP\_ISSYNC\_1\_B IPSR(8, 20, 6)

[ 567](pinctrl-r8a77961_8h.md#a28015798be631661be2162ec8656248d)#define FUNC\_SD1\_DAT2 IPSR(8, 24, 0)

[ 568](pinctrl-r8a77961_8h.md#af2768c877d254505756e9af28bd23f62)#define FUNC\_SD2\_DAT6 IPSR(8, 24, 1)

[ 569](pinctrl-r8a77961_8h.md#a53b974c835306b20ebd2e0a6ac243b00)#define FUNC\_MSIOF1\_SS1\_G IPSR(8, 24, 2)

[ 570](pinctrl-r8a77961_8h.md#a9da526458c15b9f84462c1381435d8b0)#define FUNC\_NFDATA15\_B IPSR(8, 24, 3)

[ 571](pinctrl-r8a77961_8h.md#ab6daf6131eed84ccb63a45ecb941d2f4)#define FUNC\_TS\_SDAT1\_B IPSR(8, 24, 5)

[ 572](pinctrl-r8a77961_8h.md#a72d8688fc4514a3b4c01468cfc9b0419)#define FUNC\_STP\_ISD\_1\_B IPSR(8, 24, 6)

[ 573](pinctrl-r8a77961_8h.md#a4aaa9d8004912c1bd864937cbfe6e91c)#define FUNC\_SD1\_DAT3 IPSR(8, 28, 0)

[ 574](pinctrl-r8a77961_8h.md#a01f47facca05a3c385ba51e869cd803c)#define FUNC\_SD2\_DAT7 IPSR(8, 28, 1)

[ 575](pinctrl-r8a77961_8h.md#a0d294ac32f95d46a09ec89869b3a7229)#define FUNC\_MSIOF1\_SS2\_G IPSR(8, 28, 2)

[ 576](pinctrl-r8a77961_8h.md#a01bca90dc8d8a55fea7011ca0258ce01)#define FUNC\_NFRB\_N\_B IPSR(8, 28, 3)

[ 577](pinctrl-r8a77961_8h.md#a6ed9fa7def367511acb4b0a1bb289994)#define FUNC\_TS\_SDEN1\_B IPSR(8, 28, 5)

[ 578](pinctrl-r8a77961_8h.md#a187245ec1beadda70e7ddc9aef7de224)#define FUNC\_STP\_ISEN\_1\_B IPSR(8, 28, 6)

[ 579](pinctrl-r8a77961_8h.md#a6c2348ea9cf186dbccd49c1a2abd0da7)#define FUNC\_SD2\_CLK IPSR(9, 0, 0)

[ 580](pinctrl-r8a77961_8h.md#aa75fb9cad0769e73f5a9d92706e0b57c)#define FUNC\_NFDATA8 IPSR(9, 0, 2)

[ 581](pinctrl-r8a77961_8h.md#a88f0024cde0d50a32807dd8cdf5b4389)#define FUNC\_SD2\_CMD IPSR(9, 4, 0)

[ 582](pinctrl-r8a77961_8h.md#a38026e9cf5fabef142e294c4ccc326af)#define FUNC\_NFDATA9 IPSR(9, 4, 2)

[ 583](pinctrl-r8a77961_8h.md#a3ea4683d67ce0b2d06822f16cbd3b59c)#define FUNC\_SD2\_DAT0 IPSR(9, 8, 0)

[ 584](pinctrl-r8a77961_8h.md#a3e3c0ec8fb1b4e063276d69438c0d9b3)#define FUNC\_NFDATA10 IPSR(9, 8, 2)

[ 585](pinctrl-r8a77961_8h.md#a8473ad838931442919e5b591c8f95796)#define FUNC\_SD2\_DAT1 IPSR(9, 12, 0)

[ 586](pinctrl-r8a77961_8h.md#a3ef4346ab4a365ca2b6b9d3bf1b3a8f9)#define FUNC\_NFDATA11 IPSR(9, 12, 2)

[ 587](pinctrl-r8a77961_8h.md#acf0ab8033fac1d5758f6a5c753a32b33)#define FUNC\_SD2\_DAT2 IPSR(9, 16, 0)

[ 588](pinctrl-r8a77961_8h.md#a00451be62be296abd1c0fd34aac91976)#define FUNC\_NFDATA12 IPSR(9, 16, 2)

[ 589](pinctrl-r8a77961_8h.md#a9210845a41b5832f681fbc4cb2aa5ff6)#define FUNC\_SD2\_DAT3 IPSR(9, 20, 0)

[ 590](pinctrl-r8a77961_8h.md#a63139070e028a7f1cd75e5869f2dd078)#define FUNC\_NFDATA13 IPSR(9, 20, 2)

[ 591](pinctrl-r8a77961_8h.md#af5c3ef672078bb8a0bf237c05e35ee0f)#define FUNC\_SD2\_DS IPSR(9, 24, 0)

[ 592](pinctrl-r8a77961_8h.md#aab40cdb6a52a6ad25fe535f5bbcc33ab)#define FUNC\_NFALE IPSR(9, 24, 2)

[ 593](pinctrl-r8a77961_8h.md#a8c59452a7b2dbbf5b4737a8081f49be4)#define FUNC\_SD3\_CLK IPSR(9, 28, 0)

[ 594](pinctrl-r8a77961_8h.md#a60f1c00b80304992f1e92f07aa25e5b7)#define FUNC\_NFWE\_N IPSR(9, 28, 2)

[ 595](pinctrl-r8a77961_8h.md#a5f3c66f2700f82bbfbd22ac6800f1f59)#define FUNC\_SD3\_CMD IPSR(10, 0, 0)

[ 596](pinctrl-r8a77961_8h.md#a0d401a83e0d895463742196aea73db57)#define FUNC\_NFRE\_N IPSR(10, 0, 2)

[ 597](pinctrl-r8a77961_8h.md#a3cca6cc972949389b8db8a4150c0bb87)#define FUNC\_SD3\_DAT0 IPSR(10, 4, 0)

[ 598](pinctrl-r8a77961_8h.md#ac43f5c7d8fd28c70ed2aff2898cba4fa)#define FUNC\_NFDATA0 IPSR(10, 4, 2)

[ 599](pinctrl-r8a77961_8h.md#af8ef78275bb0d057a4ec922a415d843b)#define FUNC\_SD3\_DAT1 IPSR(10, 8, 0)

[ 600](pinctrl-r8a77961_8h.md#a4cee4e5eef2987ab7c25590e7d5bfa7d)#define FUNC\_NFDATA1 IPSR(10, 8, 2)

[ 601](pinctrl-r8a77961_8h.md#a94622685e54b4a633ec28ce1782af300)#define FUNC\_SD3\_DAT2 IPSR(10, 12, 0)

[ 602](pinctrl-r8a77961_8h.md#a197598111c222dd62cc626c1cd52c07e)#define FUNC\_NFDATA2 IPSR(10, 12, 2)

[ 603](pinctrl-r8a77961_8h.md#a89dc6f9c809b77d44566add576def4c2)#define FUNC\_SD3\_DAT3 IPSR(10, 16, 0)

[ 604](pinctrl-r8a77961_8h.md#a405de0858ed7ac41aad88441d670537a)#define FUNC\_NFDATA3 IPSR(10, 16, 2)

[ 605](pinctrl-r8a77961_8h.md#af6e3d20c2bffdbaa334aecf57fec3a8f)#define FUNC\_SD3\_DAT4 IPSR(10, 20, 0)

[ 606](pinctrl-r8a77961_8h.md#a66c9aeb2657b3e386c8db786e6cea798)#define FUNC\_SD2\_CD\_A IPSR(10, 20, 1)

[ 607](pinctrl-r8a77961_8h.md#aa06b77bdd65ae89135f99d6e0cf1308b)#define FUNC\_NFDATA4 IPSR(10, 20, 2)

[ 608](pinctrl-r8a77961_8h.md#a4f524dd2bda183bbe0d4a39b730c65d5)#define FUNC\_SD3\_DAT5 IPSR(10, 24, 0)

[ 609](pinctrl-r8a77961_8h.md#af2f2c5b456eaa714b42c418dde1f7985)#define FUNC\_SD2\_WP\_A IPSR(10, 24, 1)

[ 610](pinctrl-r8a77961_8h.md#a4a4fddb783808d3379a78d93a37dc4ff)#define FUNC\_NFDATA5 IPSR(10, 24, 2)

[ 611](pinctrl-r8a77961_8h.md#ad39374a725b9d136cc7ccfd1a8e40998)#define FUNC\_SD3\_DAT6 IPSR(10, 28, 0)

[ 612](pinctrl-r8a77961_8h.md#a21f1bae5fb412a38bd89d689f6faba0a)#define FUNC\_SD3\_CD IPSR(10, 28, 1)

[ 613](pinctrl-r8a77961_8h.md#ab00503240193a91e657cb52b21129d5a)#define FUNC\_NFDATA6 IPSR(10, 28, 2)

[ 614](pinctrl-r8a77961_8h.md#a19a39341ce73e57f2f24d7eef0903459)#define FUNC\_SD3\_DAT7 IPSR(11, 0, 0)

[ 615](pinctrl-r8a77961_8h.md#adf1a84bb24f42fc4054c037dca07ebb5)#define FUNC\_SD3\_WP IPSR(11, 0, 1)

[ 616](pinctrl-r8a77961_8h.md#af475622c4e00ae88a31aabac8a213093)#define FUNC\_NFDATA7 IPSR(11, 0, 2)

[ 617](pinctrl-r8a77961_8h.md#a5fb555e0e8b52101cbd9c3140910fa12)#define FUNC\_SD3\_DS IPSR(11, 4, 0)

[ 618](pinctrl-r8a77961_8h.md#acd0ff50b357acc89f4d865b7180e3800)#define FUNC\_NFCLE IPSR(11, 4, 2)

[ 619](pinctrl-r8a77961_8h.md#a46273200ef710e6b425b1510c34b62eb)#define FUNC\_SD0\_CD IPSR(11, 8, 0)

[ 620](pinctrl-r8a77961_8h.md#af055a03ceed32918f429197eda8e55dd)#define FUNC\_NFDATA14\_A IPSR(11, 8, 2)

[ 621](pinctrl-r8a77961_8h.md#a102f0613163ae4e958e7b6a27b36d337)#define FUNC\_SCL2\_B IPSR(11, 8, 4)

[ 622](pinctrl-r8a77961_8h.md#a5c9e2d08fcc1cf94841c1ce9862c8f96)#define FUNC\_SIM0\_RST\_A IPSR(11, 8, 5)

[ 623](pinctrl-r8a77961_8h.md#a690ab7efdc5833adfa278b9bb84d3fb5)#define FUNC\_SD0\_WP IPSR(11, 12, 0)

[ 624](pinctrl-r8a77961_8h.md#af8dbbce2ab1fcdff3d1f00f9b04da0b4)#define FUNC\_NFDATA15\_A IPSR(11, 12, 2)

[ 625](pinctrl-r8a77961_8h.md#a7bcd1921c9693d3483495d9d3755cdaa)#define FUNC\_SDA2\_B IPSR(11, 12, 4)

[ 626](pinctrl-r8a77961_8h.md#a0f9556feb59f6c796cf6c32f737e1c31)#define FUNC\_SD1\_CD IPSR(11, 16, 0)

[ 627](pinctrl-r8a77961_8h.md#a6a2243b94ed8d60c181d8b22e6978d3f)#define FUNC\_NFRB\_N\_A IPSR(11, 16, 2)

[ 628](pinctrl-r8a77961_8h.md#a3ddc5a30ad38ac49678f19b4a92110be)#define FUNC\_SIM0\_CLK\_B IPSR(11, 16, 5)

[ 629](pinctrl-r8a77961_8h.md#a7ac7926422eb6e6b31ec445538f324ad)#define FUNC\_SD1\_WP IPSR(11, 20, 0)

[ 630](pinctrl-r8a77961_8h.md#aceaaf1e9a31be1b0b318a3ee220c78ba)#define FUNC\_NFCE\_N\_A IPSR(11, 20, 2)

[ 631](pinctrl-r8a77961_8h.md#a3663e3168a25f74e83ba04b265e1cc08)#define FUNC\_SIM0\_D\_B IPSR(11, 20, 5)

[ 632](pinctrl-r8a77961_8h.md#a2564af7b243f9cfdff885c89b55a03f1)#define FUNC\_SCK0 IPSR(11, 24, 0)

[ 633](pinctrl-r8a77961_8h.md#a677bdd32be9d61d51d2a2235f39064c4)#define FUNC\_HSCK1\_B IPSR(11, 24, 1)

[ 634](pinctrl-r8a77961_8h.md#a401f518fee38e0d5f1a7314772bfb7fb)#define FUNC\_MSIOF1\_SS2\_B IPSR(11, 24, 2)

[ 635](pinctrl-r8a77961_8h.md#ad08fb28f8fb91e598d4931d5ec6a5701)#define FUNC\_AUDIO\_CLKC\_B IPSR(11, 24, 3)

[ 636](pinctrl-r8a77961_8h.md#abbd1a6e30abf435ae15e14a0755abe1f)#define FUNC\_SDA2\_A IPSR(11, 24, 4)

[ 637](pinctrl-r8a77961_8h.md#a5a0394b730437a5bec0618ab40fd08e6)#define FUNC\_SIM0\_RST\_B IPSR(11, 24, 5)

[ 638](pinctrl-r8a77961_8h.md#a6606053622b00b6adf8743db2380cc61)#define FUNC\_STP\_OPWM\_0\_C IPSR(11, 24, 6)

[ 639](pinctrl-r8a77961_8h.md#aacf2c06be4bb39c3e67a3cef73254995)#define FUNC\_RIF0\_CLK\_B IPSR(11, 24, 7)

[ 640](pinctrl-r8a77961_8h.md#a75da942275c274a3e9d9e10e6d31237a)#define FUNC\_ADICHS2 IPSR(11, 24, 9)

[ 641](pinctrl-r8a77961_8h.md#a0edda1044b36296ddff8a4fd87e6c9b9)#define FUNC\_SCK5\_B IPSR(11, 24, 0xA)

[ 642](pinctrl-r8a77961_8h.md#aa9a2dc363e864c2e72f727a1cf8cbbd4)#define FUNC\_RX0 IPSR(11, 28, 0)

[ 643](pinctrl-r8a77961_8h.md#a119b3c1d0df573627ef9c822b8d22a6d)#define FUNC\_HRX1\_B IPSR(11, 28, 1)

[ 644](pinctrl-r8a77961_8h.md#ad14f0816a5618717bc02fbfe2974dda0)#define FUNC\_TS\_SCK0\_C IPSR(11, 28, 5)

[ 645](pinctrl-r8a77961_8h.md#acc60b4221cf578a08a2acafdb3a878be)#define FUNC\_STP\_ISCLK\_0\_C IPSR(11, 28, 6)

[ 646](pinctrl-r8a77961_8h.md#a4514f516a7747f76bcdabf1cac1c8445)#define FUNC\_RIF0\_D0\_B IPSR(11, 28, 7)

[ 647](pinctrl-r8a77961_8h.md#ad75b08ecf2acef89e349615d95652ebd)#define FUNC\_TX0 IPSR(12, 0, 0)

[ 648](pinctrl-r8a77961_8h.md#af8d16ecd2fd546616b7ac85929d9ef7e)#define FUNC\_HTX1\_B IPSR(12, 0, 1)

[ 649](pinctrl-r8a77961_8h.md#ac03a428e45b4e7f5ffa967e0927f2052)#define FUNC\_TS\_SPSYNC0\_C IPSR(12, 0, 5)

[ 650](pinctrl-r8a77961_8h.md#ad18b6c5368203a6144b15aad19042a53)#define FUNC\_STP\_ISSYNC\_0\_C IPSR(12, 0, 6)

[ 651](pinctrl-r8a77961_8h.md#a03650cb69a2e8fb7b36e8e60a635fb48)#define FUNC\_RIF0\_D1\_B IPSR(12, 0, 7)

[ 652](pinctrl-r8a77961_8h.md#a0a614b349eaee8271652cbe9735d841f)#define FUNC\_CTS0\_N IPSR(12, 4, 0)

[ 653](pinctrl-r8a77961_8h.md#a4c208127c425d02f65ca8931fb69eaf3)#define FUNC\_HCTS1\_N\_B IPSR(12, 4, 1)

[ 654](pinctrl-r8a77961_8h.md#a98dc1e096939658961f4c80420865072)#define FUNC\_MSIOF1\_SYNC\_B IPSR(12, 4, 2)

[ 655](pinctrl-r8a77961_8h.md#a0556fc5553c4b8bf12f6805d3023a906)#define FUNC\_TS\_SPSYNC1\_C IPSR(12, 4, 5)

[ 656](pinctrl-r8a77961_8h.md#af19fd8394dc2c380a381f27d72a18723)#define FUNC\_STP\_ISSYNC\_1\_C IPSR(12, 4, 6)

[ 657](pinctrl-r8a77961_8h.md#abc3637835e9612be2593559ae154a70b)#define FUNC\_RIF1\_SYNC\_B IPSR(12, 4, 7)

[ 658](pinctrl-r8a77961_8h.md#a065b2bc52a846c954f1df5076a07117d)#define FUNC\_AUDIO\_CLKOUT\_C IPSR(12, 4, 8)

[ 659](pinctrl-r8a77961_8h.md#a4d4bbc25c20aa136a6f8127b35b50bf1)#define FUNC\_ADICS\_SAMP IPSR(12, 4, 9)

[ 660](pinctrl-r8a77961_8h.md#ab3ec1e3ba367b62f5c166d49d77b93b8)#define FUNC\_RTS0\_N IPSR(12, 8, 0)

[ 661](pinctrl-r8a77961_8h.md#ab07b47015dbca00e4ccf29da055ffb7b)#define FUNC\_HRTS1\_N\_B IPSR(12, 8, 1)

[ 662](pinctrl-r8a77961_8h.md#a14afcb3b8d78cd76d534f07fc8318fd9)#define FUNC\_MSIOF1\_SS1\_B IPSR(12, 8, 2)

[ 663](pinctrl-r8a77961_8h.md#ac1418c5dc12b70a8c286d7ebeb42db15)#define FUNC\_AUDIO\_CLKA\_B IPSR(12, 8, 3)

[ 664](pinctrl-r8a77961_8h.md#a9a9098f10df27abd21de90d53f5f0c80)#define FUNC\_SCL2\_A IPSR(12, 8, 4)

[ 665](pinctrl-r8a77961_8h.md#a8e3c6305f8db3276387c317d661e8ab1)#define FUNC\_STP\_IVCXO27\_1\_C IPSR(12, 8, 6)

[ 666](pinctrl-r8a77961_8h.md#a8f509e3621c518376b775f56631163c1)#define FUNC\_RIF0\_SYNC\_B IPSR(12, 8, 7)

[ 667](pinctrl-r8a77961_8h.md#ac1fb7c6a16aa2352ed13e346f83f1aa0)#define FUNC\_ADICHS1 IPSR(12, 8, 9)

[ 668](pinctrl-r8a77961_8h.md#a8b141542b34fa86aa7acdabd4ac42442)#define FUNC\_RX1\_A IPSR(12, 12, 0)

[ 669](pinctrl-r8a77961_8h.md#a890fe166485ea320caee59a6eedb26c5)#define FUNC\_HRX1\_A IPSR(12, 12, 1)

[ 670](pinctrl-r8a77961_8h.md#a4ff13274201a7d47102faf5e19068a18)#define FUNC\_TS\_SDAT0\_C IPSR(12, 12, 5)

[ 671](pinctrl-r8a77961_8h.md#a6fe2c986144fdd8c7d3d93b02434a306)#define FUNC\_STP\_ISD\_0\_C IPSR(12, 12, 6)

[ 672](pinctrl-r8a77961_8h.md#a0d60d958883235bda47567cee2bf658c)#define FUNC\_RIF1\_CLK\_C IPSR(12, 12, 7)

[ 673](pinctrl-r8a77961_8h.md#a040f0c1548ff587def91382c78dd9aed)#define FUNC\_TX1\_A IPSR(12, 16, 0)

[ 674](pinctrl-r8a77961_8h.md#a06ece2070817ace07434c0ac8cea9b37)#define FUNC\_HTX1\_A IPSR(12, 16, 1)

[ 675](pinctrl-r8a77961_8h.md#ae909a4a29deff8e9a2e274f568edd2a4)#define FUNC\_TS\_SDEN0\_C IPSR(12, 16, 5)

[ 676](pinctrl-r8a77961_8h.md#a55618f0f33c247ef9da93258c2f4d70e)#define FUNC\_STP\_ISEN\_0\_C IPSR(12, 16, 6)

[ 677](pinctrl-r8a77961_8h.md#a13db898e1fbffe49208da6a54acabcc1)#define FUNC\_RIF1\_D0\_C IPSR(12, 16, 7)

[ 678](pinctrl-r8a77961_8h.md#afb5bcac1912aef8f7580b9c68830bc25)#define FUNC\_CTS1\_N IPSR(12, 20, 0)

[ 679](pinctrl-r8a77961_8h.md#a71b55b6f4c39fecb48c691d375642f01)#define FUNC\_HCTS1\_N\_A IPSR(12, 20, 1)

[ 680](pinctrl-r8a77961_8h.md#ac34514acc673aa57266045d1dec60eb3)#define FUNC\_MSIOF1\_RXD\_B IPSR(12, 20, 2)

[ 681](pinctrl-r8a77961_8h.md#ad7b8a22c7ac0a9fb538b0033a1f85528)#define FUNC\_TS\_SDEN1\_C IPSR(12, 20, 5)

[ 682](pinctrl-r8a77961_8h.md#a928da73a9d157bc748f44673116e5eb7)#define FUNC\_STP\_ISEN\_1\_C IPSR(12, 20, 6)

[ 683](pinctrl-r8a77961_8h.md#a5b18ad16b6ee0be361b7d9a78a69751e)#define FUNC\_RIF1\_D0\_B IPSR(12, 20, 7)

[ 684](pinctrl-r8a77961_8h.md#a558086f7a4a5072947ccd0fd6a897c59)#define FUNC\_ADIDATA IPSR(12, 20, 9)

[ 685](pinctrl-r8a77961_8h.md#a429d41290ac7e1e8d02f6c05b32f7376)#define FUNC\_RTS1\_N IPSR(12, 24, 0)

[ 686](pinctrl-r8a77961_8h.md#ae4982b48bb77189d9665d028adbb40c4)#define FUNC\_HRTS1\_N\_A IPSR(12, 24, 1)

[ 687](pinctrl-r8a77961_8h.md#a3651e9a7988daf9964f90f5406d3b5c0)#define FUNC\_MSIOF1\_TXD\_B IPSR(12, 24, 2)

[ 688](pinctrl-r8a77961_8h.md#a07f765fa47a4323f8d50d9603e1d6fc7)#define FUNC\_TS\_SDAT1\_C IPSR(12, 24, 5)

[ 689](pinctrl-r8a77961_8h.md#afa17b4ad5c868fea3a46e959e94c7659)#define FUNC\_STP\_ISD\_1\_C IPSR(12, 24, 6)

[ 690](pinctrl-r8a77961_8h.md#a2ba5f747555e2ad4da3e3fe66b6e43a8)#define FUNC\_RIF1\_D1\_B IPSR(12, 24, 7)

[ 691](pinctrl-r8a77961_8h.md#adc0d2fd70babcc390525ce2e9d82dd3f)#define FUNC\_ADICHS0 IPSR(12, 24, 9)

[ 692](pinctrl-r8a77961_8h.md#ada76529c4589e617040ffb3472bb5803)#define FUNC\_SCK2 IPSR(12, 28, 0)

[ 693](pinctrl-r8a77961_8h.md#a2538871b0e89bd1f5a854a4604273cdb)#define FUNC\_SCIF\_CLK\_B IPSR(12, 28, 1)

[ 694](pinctrl-r8a77961_8h.md#a3e0d3d6323a6732cc1c8b5b4b4a0da01)#define FUNC\_MSIOF1\_SCK\_B IPSR(12, 28, 2)

[ 695](pinctrl-r8a77961_8h.md#a867ae7dd6ffccdee697fbe37a51436f1)#define FUNC\_TS\_SCK1\_C IPSR(12, 28, 5)

[ 696](pinctrl-r8a77961_8h.md#ab7b0efc3821a45185a8a3978f2d8d3c8)#define FUNC\_STP\_ISCLK\_1\_C IPSR(12, 28, 6)

[ 697](pinctrl-r8a77961_8h.md#a68742f24d1f7ce86417c0afd2f518e40)#define FUNC\_RIF1\_CLK\_B IPSR(12, 28, 7)

[ 698](pinctrl-r8a77961_8h.md#a98792fd3ab6cdf3f81031ac4925ae1da)#define FUNC\_ADICLK IPSR(12, 28, 9)

[ 699](pinctrl-r8a77961_8h.md#a8dd586d735e01762fab43e1cfc847258)#define FUNC\_TX2\_A IPSR(13, 0, 0)

[ 700](pinctrl-r8a77961_8h.md#aa7e62f7d5eb84bf5c5490ad292fb616d)#define FUNC\_SD2\_CD\_B IPSR(13, 0, 3)

[ 701](pinctrl-r8a77961_8h.md#a5949d85265a12a29b98fc855d4a6deff)#define FUNC\_SCL1\_A IPSR(13, 0, 4)

[ 702](pinctrl-r8a77961_8h.md#aadcd6be9f111baace15f05d53d1496ac)#define FUNC\_FMCLK\_A IPSR(13, 0, 6)

[ 703](pinctrl-r8a77961_8h.md#a79ad479484a7f5dd1a085170904d90e9)#define FUNC\_RIF1\_D1\_C IPSR(13, 0, 7)

[ 704](pinctrl-r8a77961_8h.md#a091671cae9d30223ef178dfb16ca3327)#define FUNC\_FSO\_CFE\_0\_N IPSR(13, 0, 9)

[ 705](pinctrl-r8a77961_8h.md#acc7ae012c901aafa196d7e39637985d6)#define FUNC\_RX2\_A IPSR(13, 4, 0)

[ 706](pinctrl-r8a77961_8h.md#aaa1589026a2e23785fd1fc73abadf52c)#define FUNC\_SD2\_WP\_B IPSR(13, 4, 3)

[ 707](pinctrl-r8a77961_8h.md#ae018f2b706c282c468474a719c077023)#define FUNC\_SDA1\_A IPSR(13, 4, 4)

[ 708](pinctrl-r8a77961_8h.md#aa8700820e2f174ad0b740ab69438c666)#define FUNC\_FMIN\_A IPSR(13, 4, 6)

[ 709](pinctrl-r8a77961_8h.md#ad45ec10a00b1172aa9d8739dc97a6671)#define FUNC\_RIF1\_SYNC\_C IPSR(13, 4, 7)

[ 710](pinctrl-r8a77961_8h.md#a11eb7d49603f2e314a32d976560e96af)#define FUNC\_FSO\_CFE\_1\_N IPSR(13, 4, 9)

[ 711](pinctrl-r8a77961_8h.md#ac34dcbc3b29209202c8814557d95ea55)#define FUNC\_HSCK0 IPSR(13, 8, 0)

[ 712](pinctrl-r8a77961_8h.md#af2b037008078be1f771b6cd5aa538384)#define FUNC\_MSIOF1\_SCK\_D IPSR(13, 8, 2)

[ 713](pinctrl-r8a77961_8h.md#ab901d7df925a704392273e29d80e1a4f)#define FUNC\_AUDIO\_CLKB\_A IPSR(13, 8, 3)

[ 714](pinctrl-r8a77961_8h.md#a8adc459ea6548473b47c8b9e6385bfaf)#define FUNC\_SSI\_SDATA1\_B IPSR(13, 8, 4)

[ 715](pinctrl-r8a77961_8h.md#a72b147cff219957a46ef1a6da37cb888)#define FUNC\_TS\_SCK0\_D IPSR(13, 8, 5)

[ 716](pinctrl-r8a77961_8h.md#a90e645ca029a715d84b99f88c9c27d07)#define FUNC\_STP\_ISCLK\_0\_D IPSR(13, 8, 6)

[ 717](pinctrl-r8a77961_8h.md#aae4fdd7f005fe84075b6573d39073f76)#define FUNC\_RIF0\_CLK\_C IPSR(13, 8, 7)

[ 718](pinctrl-r8a77961_8h.md#a705543f16aa06b3bf298acdbd54a6039)#define FUNC\_RX5\_B IPSR(13, 8, 0xA)

[ 719](pinctrl-r8a77961_8h.md#a0083d7f84d9cd9a43bce4ead53660e10)#define FUNC\_HRX0 IPSR(13, 12, 0)

[ 720](pinctrl-r8a77961_8h.md#a4cebf553fa65201321a8f6340a3f3a53)#define FUNC\_MSIOF1\_RXD\_D IPSR(13, 12, 2)

[ 721](pinctrl-r8a77961_8h.md#a8e2b6fe9963f8aaedb60f7b054b2ac5b)#define FUNC\_SSI\_SDATA2\_B IPSR(13, 12, 4)

[ 722](pinctrl-r8a77961_8h.md#a070631f6e8c31f9d99fced078bb7601c)#define FUNC\_TS\_SDEN0\_D IPSR(13, 12, 5)

[ 723](pinctrl-r8a77961_8h.md#a1b477695fa5c82ae361da0f9e0e9d07e)#define FUNC\_STP\_ISEN\_0\_D IPSR(13, 12, 6)

[ 724](pinctrl-r8a77961_8h.md#a120598854bf315210a7a64ad86ab1eca)#define FUNC\_RIF0\_D0\_C IPSR(13, 12, 7)

[ 725](pinctrl-r8a77961_8h.md#a05b9319c6c2228449a956a3377ccff44)#define FUNC\_HTX0 IPSR(13, 16, 0)

[ 726](pinctrl-r8a77961_8h.md#ab70d6c9e381842e988b7c0acafafa139)#define FUNC\_MSIOF1\_TXD\_D IPSR(13, 16, 2)

[ 727](pinctrl-r8a77961_8h.md#adb00bf6f3c1431b2fc9ba34ca91cccaf)#define FUNC\_SSI\_SDATA9\_B IPSR(13, 16, 4)

[ 728](pinctrl-r8a77961_8h.md#a14d07146241bdbe2ca2a0a428c20b384)#define FUNC\_TS\_SDAT0\_D IPSR(13, 16, 5)

[ 729](pinctrl-r8a77961_8h.md#abce1e0f528ef1153b3d57838412a2f2e)#define FUNC\_STP\_ISD\_0\_D IPSR(13, 16, 6)

[ 730](pinctrl-r8a77961_8h.md#ac67878f8a8d433e80fe7bf010b9eef5b)#define FUNC\_RIF0\_D1\_C IPSR(13, 16, 7)

[ 731](pinctrl-r8a77961_8h.md#a7739b47f4b7b6fbbfc6a86a70bdbcb4d)#define FUNC\_HCTS0\_N IPSR(13, 20, 0)

[ 732](pinctrl-r8a77961_8h.md#a0904f49c2a6f72b71c4aa0cd362d27f6)#define FUNC\_RX2\_B IPSR(13, 20, 1)

[ 733](pinctrl-r8a77961_8h.md#ab2c77dc18f2f127e20ffd37ccd85509d)#define FUNC\_MSIOF1\_SYNC\_D IPSR(13, 20, 2)

[ 734](pinctrl-r8a77961_8h.md#ab8da1a42f4612c97de251d4c8fd180f0)#define FUNC\_SSI\_SCK9\_A IPSR(13, 20, 4)

[ 735](pinctrl-r8a77961_8h.md#ac54cba7f9d82edc19cfafc9ca9b8efe1)#define FUNC\_TS\_SPSYNC0\_D IPSR(13, 20, 5)

[ 736](pinctrl-r8a77961_8h.md#a687e646fa84845f198790a3759829bee)#define FUNC\_STP\_ISSYNC\_0\_D IPSR(13, 20, 6)

[ 737](pinctrl-r8a77961_8h.md#a4c30734e7662e8282f453e0f1355b17f)#define FUNC\_RIF0\_SYNC\_C IPSR(13, 20, 7)

[ 738](pinctrl-r8a77961_8h.md#a508b09530e0d045c440dcbfb1e73aa04)#define FUNC\_AUDIO\_CLKOUT1\_A IPSR(13, 20, 8)

[ 739](pinctrl-r8a77961_8h.md#a71382cd3a87fa52b3ccb8609fdbe6a06)#define FUNC\_HRTS0\_N IPSR(13, 24, 0)

[ 740](pinctrl-r8a77961_8h.md#a79cf69aef49b03f6138399ef7768539b)#define FUNC\_TX2\_B IPSR(13, 24, 1)

[ 741](pinctrl-r8a77961_8h.md#a8557a9c17858699b361948e1f0dab020)#define FUNC\_MSIOF1\_SS1\_D IPSR(13, 24, 2)

[ 742](pinctrl-r8a77961_8h.md#a514e9c6aa47f0d62c684fa78cebef275)#define FUNC\_SSI\_WS9\_A IPSR(13, 24, 4)

[ 743](pinctrl-r8a77961_8h.md#afffc81cfc5c21ec5602c4b343685151b)#define FUNC\_STP\_IVCXO27\_0\_D IPSR(13, 24, 6)

[ 744](pinctrl-r8a77961_8h.md#ad7a5cd120a6cd2e0e7b73b67ee1b92a5)#define FUNC\_BPFCLK\_A IPSR(13, 24, 7)

[ 745](pinctrl-r8a77961_8h.md#a34df0ebecca84013b145b66322dc79ec)#define FUNC\_AUDIO\_CLKOUT2\_A IPSR(13, 24, 8)

[ 746](pinctrl-r8a77961_8h.md#a694da81cb9ea8a3810117bdb2d3305c9)#define FUNC\_MSIOF0\_SYNC IPSR(13, 28, 0)

[ 747](pinctrl-r8a77961_8h.md#ae6a3b9af263ccce548f01c6852af7a93)#define FUNC\_AUDIO\_CLKOUT\_A IPSR(13, 28, 8)

[ 748](pinctrl-r8a77961_8h.md#a792d793a2cc17ef8b98dca4d7cf49910)#define FUNC\_TX5\_B IPSR(13, 28, 0xA)

[ 749](pinctrl-r8a77961_8h.md#adbe974f7c7e42e8edb066aa9162e4135)#define FUNC\_BPFCLK\_D IPSR(13, 28, 0xD)

[ 750](pinctrl-r8a77961_8h.md#a3af1cd4a0b729bcf95bd8648be9e8b76)#define FUNC\_MSIOF0\_SS1 IPSR(14, 0, 0)

[ 751](pinctrl-r8a77961_8h.md#af42374b168a632c8de7c6ac51341d962)#define FUNC\_RX5\_A IPSR(14, 0, 1)

[ 752](pinctrl-r8a77961_8h.md#a100a1e37748810c86c28a19dfe3941a7)#define FUNC\_NFWP\_N\_A IPSR(14, 0, 2)

[ 753](pinctrl-r8a77961_8h.md#a5db096667076c69691c3cb6325290276)#define FUNC\_AUDIO\_CLKA\_C IPSR(14, 0, 3)

[ 754](pinctrl-r8a77961_8h.md#a98161ffa537954f46380a334a313bf6a)#define FUNC\_SSI\_SCK2\_A IPSR(14, 0, 4)

[ 755](pinctrl-r8a77961_8h.md#a2b8ffc23381e22eabfae990b55d7a140)#define FUNC\_STP\_IVCXO27\_0\_C IPSR(14, 0, 6)

[ 756](pinctrl-r8a77961_8h.md#a23332ca95f1bd83372acfe48c1966707)#define FUNC\_AUDIO\_CLKOUT3\_A IPSR(14, 0, 8)

[ 757](pinctrl-r8a77961_8h.md#a72b2371a3ee1c41281dc1866bb12b181)#define FUNC\_TCLK1\_B IPSR(14, 0, 0xA)

[ 758](pinctrl-r8a77961_8h.md#a8a36e419e0beb0bbb418e6e63b51d42a)#define FUNC\_MSIOF0\_SS2 IPSR(14, 4, 0)

[ 759](pinctrl-r8a77961_8h.md#a19e0f00b4ff46aa5167baf824889f2f4)#define FUNC\_TX5\_A IPSR(14, 4, 1)

[ 760](pinctrl-r8a77961_8h.md#acdbde14f76ae1264ae544880006ba552)#define FUNC\_MSIOF1\_SS2\_D IPSR(14, 4, 2)

[ 761](pinctrl-r8a77961_8h.md#a5f4b703e2cd614f5c243ef67d856a471)#define FUNC\_AUDIO\_CLKC\_A IPSR(14, 4, 3)

[ 762](pinctrl-r8a77961_8h.md#a6d1a8afe99b82f1dcb0ba614dfa24632)#define FUNC\_SSI\_WS2\_A IPSR(14, 4, 4)

[ 763](pinctrl-r8a77961_8h.md#ae4b34d32b308e886ddac94684c6227e7)#define FUNC\_STP\_OPWM\_0\_D IPSR(14, 4, 6)

[ 764](pinctrl-r8a77961_8h.md#ae72ce327404e7dce1a7fb060bbff6738)#define FUNC\_AUDIO\_CLKOUT\_D IPSR(14, 4, 8)

[ 765](pinctrl-r8a77961_8h.md#a63e3878e003f9b9c4f8161b8dcfa8750)#define FUNC\_SPEEDIN\_B IPSR(14, 4, 0xA)

[ 766](pinctrl-r8a77961_8h.md#a37e1e91cede71b2a42a35f30bacf2ccd)#define FUNC\_MLB\_CLK IPSR(14, 8, 0)

[ 767](pinctrl-r8a77961_8h.md#a9aabcace005dd0b3a2b4960a3b6676e6)#define FUNC\_MSIOF1\_SCK\_F IPSR(14, 8, 2)

[ 768](pinctrl-r8a77961_8h.md#aa08dfd62485579dba6598571d598a6f5)#define FUNC\_SCL1\_B IPSR(14, 8, 4)

[ 769](pinctrl-r8a77961_8h.md#ae029f4927c03c4e31b2b407e55386f4e)#define FUNC\_MLB\_SIG IPSR(14, 12, 0)

[ 770](pinctrl-r8a77961_8h.md#a3a251942056277de7918739e22a16873)#define FUNC\_RX1\_B IPSR(14, 12, 1)

[ 771](pinctrl-r8a77961_8h.md#a972bbe81781be958a82da226877d7e58)#define FUNC\_MSIOF1\_SYNC\_F IPSR(14, 12, 2)

[ 772](pinctrl-r8a77961_8h.md#a82af0c0eebf51f218e4c2318692ac465)#define FUNC\_SDA1\_B IPSR(14, 12, 4)

[ 773](pinctrl-r8a77961_8h.md#a874380b58402dd24b432381db9d16af6)#define FUNC\_MLB\_DAT IPSR(14, 16, 0)

[ 774](pinctrl-r8a77961_8h.md#a5212faa58c212f84f53a773be0e24a1c)#define FUNC\_TX1\_B IPSR(14, 16, 1)

[ 775](pinctrl-r8a77961_8h.md#aa3c5ce7f3634eb0dca44bd5051564ca4)#define FUNC\_MSIOF1\_RXD\_F IPSR(14, 16, 2)

[ 776](pinctrl-r8a77961_8h.md#a7d9075279fa65192d318bfe8cff071dc)#define FUNC\_SSI\_SCK01239 IPSR(14, 20, 0)

[ 777](pinctrl-r8a77961_8h.md#a2799a2c8383216440aab77bbc347972b)#define FUNC\_MSIOF1\_TXD\_F IPSR(14, 20, 2)

[ 778](pinctrl-r8a77961_8h.md#a83f081f9d27278db218292a5939593af)#define FUNC\_SSI\_WS01239 IPSR(14, 24, 0)

[ 779](pinctrl-r8a77961_8h.md#a46dc91f8edad812de8212482fe53ba51)#define FUNC\_MSIOF1\_SS1\_F IPSR(14, 24, 2)

[ 780](pinctrl-r8a77961_8h.md#af2d48d55c26a49b26c3bac1a270b0fb1)#define FUNC\_SSI\_SDATA0 IPSR(14, 28, 0)

[ 781](pinctrl-r8a77961_8h.md#a85e61d898d0f8cdff113eaeac31176d4)#define FUNC\_MSIOF1\_SS2\_F IPSR(14, 28, 2)

[ 782](pinctrl-r8a77961_8h.md#af942efd772d4edb7a6fd2b700c0064da)#define FUNC\_SSI\_SDATA1\_A IPSR(15, 0, 0)

[ 783](pinctrl-r8a77961_8h.md#ab8ee795f62f736383502f11bc9746709)#define FUNC\_SSI\_SDATA2\_A IPSR(15, 4, 0)

[ 784](pinctrl-r8a77961_8h.md#a7769afa60ec0ad66b4c28be3961152d2)#define FUNC\_SSI\_SCK1\_B IPSR(15, 4, 4)

[ 785](pinctrl-r8a77961_8h.md#a186d5a3738cf0cd72a55b18b4d17704e)#define FUNC\_SSI\_SCK349 IPSR(15, 8, 0)

[ 786](pinctrl-r8a77961_8h.md#a105f68b2f6ca839498bf9b53880964c1)#define FUNC\_MSIOF1\_SS1\_A IPSR(15, 8, 2)

[ 787](pinctrl-r8a77961_8h.md#aca7e74974acfcbf0d76b20be7874c943)#define FUNC\_STP\_OPWM\_0\_A IPSR(15, 8, 6)

[ 788](pinctrl-r8a77961_8h.md#a94c562aaf95a9e7542ce18d75d7f5d37)#define FUNC\_SSI\_WS349 IPSR(15, 12, 0)

[ 789](pinctrl-r8a77961_8h.md#aaf784de2a9762248693a1b4cd3d374ee)#define FUNC\_HCTS2\_N\_A IPSR(15, 12, 1)

[ 790](pinctrl-r8a77961_8h.md#a9c2a4494d56a2d538e57652bea40ca49)#define FUNC\_MSIOF1\_SS2\_A IPSR(15, 12, 2)

[ 791](pinctrl-r8a77961_8h.md#a0e3b4ebd09ac38c29773b21b71b9a36b)#define FUNC\_STP\_IVCXO27\_0\_A IPSR(15, 12, 6)

[ 792](pinctrl-r8a77961_8h.md#a577d3531a6b40647586f68607575432e)#define FUNC\_SSI\_SDATA3 IPSR(15, 16, 0)

[ 793](pinctrl-r8a77961_8h.md#a3b2cceba1894cf0e446a4d406d31932c)#define FUNC\_HRTS2\_N\_A IPSR(15, 16, 1)

[ 794](pinctrl-r8a77961_8h.md#a172d73fc1938a2c9b076cb9f935e40f6)#define FUNC\_MSIOF1\_TXD\_A IPSR(15, 16, 2)

[ 795](pinctrl-r8a77961_8h.md#a7d40750d3b804aba0fa4a303369c497b)#define FUNC\_TS\_SCK0\_A IPSR(15, 16, 5)

[ 796](pinctrl-r8a77961_8h.md#a20264efe63eb7f434cbcb9cea2417398)#define FUNC\_STP\_ISCLK\_0\_A IPSR(15, 16, 6)

[ 797](pinctrl-r8a77961_8h.md#a9ef164c6cb3ea167e53631524289d259)#define FUNC\_RIF0\_D1\_A IPSR(15, 16, 7)

[ 798](pinctrl-r8a77961_8h.md#aa992fd63f07df080844e0462c0e0e6df)#define FUNC\_RIF2\_D0\_A IPSR(15, 16, 8)

[ 799](pinctrl-r8a77961_8h.md#ae8e9d25b1d8bd4f112b921b840c7215f)#define FUNC\_SSI\_SCK4 IPSR(15, 20, 0)

[ 800](pinctrl-r8a77961_8h.md#ac39536275fa16d0235b34454b83bdfd0)#define FUNC\_HRX2\_A IPSR(15, 20, 1)

[ 801](pinctrl-r8a77961_8h.md#a99b373cfb93066dc74504716e878b0ba)#define FUNC\_MSIOF1\_SCK\_A IPSR(15, 20, 2)

[ 802](pinctrl-r8a77961_8h.md#a33c2fec05bc1276a9a6c7a3b2f0db7d0)#define FUNC\_TS\_SDAT0\_A IPSR(15, 20, 5)

[ 803](pinctrl-r8a77961_8h.md#a528eada079f91f0aa7acdb283adba6ba)#define FUNC\_STP\_ISD\_0\_A IPSR(15, 20, 6)

[ 804](pinctrl-r8a77961_8h.md#a65caf5a7291af2210fd06594d5bb1259)#define FUNC\_RIF0\_CLK\_A IPSR(15, 20, 7)

[ 805](pinctrl-r8a77961_8h.md#a49eba56503db70ae24fad1427ab635f4)#define FUNC\_RIF2\_CLK\_A IPSR(15, 20, 8)

[ 806](pinctrl-r8a77961_8h.md#a6b34ddd4dd81c8c61382893343da227a)#define FUNC\_SSI\_WS4 IPSR(15, 24, 0)

[ 807](pinctrl-r8a77961_8h.md#ab3f10e6bc834ba33aff8b4ae1a437053)#define FUNC\_HTX2\_A IPSR(15, 24, 1)

[ 808](pinctrl-r8a77961_8h.md#aeb2327cf6150b6c46c374e91c56ba4e6)#define FUNC\_MSIOF1\_SYNC\_A IPSR(15, 24, 2)

[ 809](pinctrl-r8a77961_8h.md#aaa5bec25b24cfc6a9970a75faf16ef29)#define FUNC\_TS\_SDEN0\_A IPSR(15, 24, 5)

[ 810](pinctrl-r8a77961_8h.md#a482bb4038fc9866d06a32b210f4822d6)#define FUNC\_STP\_ISEN\_0\_A IPSR(15, 24, 6)

[ 811](pinctrl-r8a77961_8h.md#ae3555bf348a4185af292a2132b5bfebc)#define FUNC\_RIF0\_SYNC\_A IPSR(15, 24, 7)

[ 812](pinctrl-r8a77961_8h.md#aa7150f12a62429f148319d98f60f8918)#define FUNC\_RIF2\_SYNC\_A IPSR(15, 24, 8)

[ 813](pinctrl-r8a77961_8h.md#a1f222c51cfaf3698315d80d34b941c7f)#define FUNC\_SSI\_SDATA4 IPSR(15, 28, 0)

[ 814](pinctrl-r8a77961_8h.md#ae59e04ffe4797066cc74720d65520b30)#define FUNC\_HSCK2\_A IPSR(15, 28, 1)

[ 815](pinctrl-r8a77961_8h.md#a1046445636c10c76a89dab688108ed27)#define FUNC\_MSIOF1\_RXD\_A IPSR(15, 28, 2)

[ 816](pinctrl-r8a77961_8h.md#ad76845bbd819acf441d1bb320180f4e6)#define FUNC\_TS\_SPSYNC0\_A IPSR(15, 28, 5)

[ 817](pinctrl-r8a77961_8h.md#a8c7b231c52e63820070a6ebbc0331f82)#define FUNC\_STP\_ISSYNC\_0\_A IPSR(15, 28, 6)

[ 818](pinctrl-r8a77961_8h.md#ad9e4fc1cb6e6cfb8472d70034568555a)#define FUNC\_RIF0\_D0\_A IPSR(15, 28, 7)

[ 819](pinctrl-r8a77961_8h.md#a5346b11132bef8fba573026069aa87dd)#define FUNC\_RIF2\_D1\_A IPSR(15, 28, 8)

[ 820](pinctrl-r8a77961_8h.md#a4aa4d7fc234250ef59be067e85226252)#define FUNC\_SSI\_SCK6 IPSR(16, 0, 0)

[ 821](pinctrl-r8a77961_8h.md#ac7f25d71411f2655b7de41ae1635bdce)#define FUNC\_SIM0\_RST\_D IPSR(16, 0, 3)

[ 822](pinctrl-r8a77961_8h.md#a395f4eb5d8b7b251a244e55e94d358d2)#define FUNC\_SSI\_WS6 IPSR(16, 4, 0)

[ 823](pinctrl-r8a77961_8h.md#a9cd82f6419aee93deb17044927a3c6a7)#define FUNC\_SIM0\_D\_D IPSR(16, 4, 3)

[ 824](pinctrl-r8a77961_8h.md#ab6cd84c4f51952c1d5bf0638d6efcb54)#define FUNC\_SSI\_SDATA6 IPSR(16, 8, 0)

[ 825](pinctrl-r8a77961_8h.md#a2b6f502f174c652e33dca17170956e03)#define FUNC\_SIM0\_CLK\_D IPSR(16, 8, 3)

[ 826](pinctrl-r8a77961_8h.md#aeea3c42dfbed6da031d10fb38959990c)#define FUNC\_SSI\_SCK78 IPSR(16, 12, 0)

[ 827](pinctrl-r8a77961_8h.md#a14a8d3acf001bc94bb57516e367eff6a)#define FUNC\_HRX2\_B IPSR(16, 12, 1)

[ 828](pinctrl-r8a77961_8h.md#abc8d0066f8fd48a47f7e8c61259f6be8)#define FUNC\_MSIOF1\_SCK\_C IPSR(16, 12, 2)

[ 829](pinctrl-r8a77961_8h.md#a330cbd69b4cae7498b72b9942eb1f5f4)#define FUNC\_TS\_SCK1\_A IPSR(16, 12, 5)

[ 830](pinctrl-r8a77961_8h.md#aa10a5ac77601308d1d4fd352a5ec79c5)#define FUNC\_STP\_ISCLK\_1\_A IPSR(16, 12, 6)

[ 831](pinctrl-r8a77961_8h.md#a5e44566b1586d48edd40a7e6422740ee)#define FUNC\_RIF1\_CLK\_A IPSR(16, 12, 7)

[ 832](pinctrl-r8a77961_8h.md#ad9d395c716d06374b9b4c85531225a9a)#define FUNC\_RIF3\_CLK\_A IPSR(16, 12, 8)

[ 833](pinctrl-r8a77961_8h.md#a8b6c5b559c782dee5c87d529aaebcad9)#define FUNC\_SSI\_WS78 IPSR(16, 16, 0)

[ 834](pinctrl-r8a77961_8h.md#a16efce64e078a1cb1eaa2ed75ae5be45)#define FUNC\_HTX2\_B IPSR(16, 16, 1)

[ 835](pinctrl-r8a77961_8h.md#a74fa9f2ae7d621671b8f5ce62a769c34)#define FUNC\_MSIOF1\_SYNC\_C IPSR(16, 16, 2)

[ 836](pinctrl-r8a77961_8h.md#a2bc34e789379cdfdf58ef265e8bd2e8b)#define FUNC\_TS\_SDAT1\_A IPSR(16, 16, 5)

[ 837](pinctrl-r8a77961_8h.md#a164f55c4303266ea47f4080c04ba283f)#define FUNC\_STP\_ISD\_1\_A IPSR(16, 16, 6)

[ 838](pinctrl-r8a77961_8h.md#aaf6d113b1f30a8b551da6b07285c98c3)#define FUNC\_RIF1\_SYNC\_A IPSR(16, 16, 7)

[ 839](pinctrl-r8a77961_8h.md#ad308c866c7620014c2aa0546cc463436)#define FUNC\_RIF3\_SYNC\_A IPSR(16, 16, 8)

[ 840](pinctrl-r8a77961_8h.md#a44426619b3e122622faa3459b7d93513)#define FUNC\_SSI\_SDATA7 IPSR(16, 20, 0)

[ 841](pinctrl-r8a77961_8h.md#a007accd768da805f14f91f1744ab9682)#define FUNC\_HCTS2\_N\_B IPSR(16, 20, 1)

[ 842](pinctrl-r8a77961_8h.md#ac75f4f72100208d4c89bd0951d0f5f4e)#define FUNC\_MSIOF1\_RXD\_C IPSR(16, 20, 2)

[ 843](pinctrl-r8a77961_8h.md#ad1e7f8bd5eacff55e9de74038be03e55)#define FUNC\_TS\_SDEN1\_A IPSR(16, 20, 5)

[ 844](pinctrl-r8a77961_8h.md#a523f40355ad0b68149a5723bd05a0f0b)#define FUNC\_STP\_ISEN\_1\_A IPSR(16, 20, 6)

[ 845](pinctrl-r8a77961_8h.md#a74df07d826ed9ca69c49c80352e08829)#define FUNC\_RIF1\_D0\_A IPSR(16, 20, 7)

[ 846](pinctrl-r8a77961_8h.md#a2593f75c4aa2329933024d2db4b49866)#define FUNC\_RIF3\_D0\_A IPSR(16, 20, 8)

[ 847](pinctrl-r8a77961_8h.md#a86eaedf92ad0e0b462d7526418363e83)#define FUNC\_TCLK2\_A IPSR(16, 20, 0xA)

[ 848](pinctrl-r8a77961_8h.md#af8d5474f83c7873b2f283d870b6c9de7)#define FUNC\_SSI\_SDATA8 IPSR(16, 24, 0)

[ 849](pinctrl-r8a77961_8h.md#ac172b5f55fe8ca296577288d806b5793)#define FUNC\_HRTS2\_N\_B IPSR(16, 24, 1)

[ 850](pinctrl-r8a77961_8h.md#a136b8af9ae878242a30be3e5cd99a555)#define FUNC\_MSIOF1\_TXD\_C IPSR(16, 24, 2)

[ 851](pinctrl-r8a77961_8h.md#a4632ab165e48aaf8337401d2ad8c3691)#define FUNC\_TS\_SPSYNC1\_A IPSR(16, 24, 5)

[ 852](pinctrl-r8a77961_8h.md#a1ed880222e956679fbfd752fb73e69b1)#define FUNC\_STP\_ISSYNC\_1\_A IPSR(16, 24, 6)

[ 853](pinctrl-r8a77961_8h.md#a532cb5696338d3860dba8e0a6953e69a)#define FUNC\_RIF1\_D1\_A IPSR(16, 24, 7)

[ 854](pinctrl-r8a77961_8h.md#a1fca77c30e546f12c2ccc77d28571cc7)#define FUNC\_RIF3\_D1\_A IPSR(16, 24, 8)

[ 855](pinctrl-r8a77961_8h.md#ab145c0178edbeea477da0d270e123eb5)#define FUNC\_SSI\_SDATA9\_A IPSR(16, 28, 0)

[ 856](pinctrl-r8a77961_8h.md#a18a1030c76d8e602ef9d8be730433088)#define FUNC\_HSCK2\_B IPSR(16, 28, 1)

[ 857](pinctrl-r8a77961_8h.md#a443b1d610edd41b8be2d34a42dcf6892)#define FUNC\_MSIOF1\_SS1\_C IPSR(16, 28, 2)

[ 858](pinctrl-r8a77961_8h.md#ad2dd7ebb3146f5778b4e85c8a512e81b)#define FUNC\_HSCK1\_A IPSR(16, 28, 3)

[ 859](pinctrl-r8a77961_8h.md#a356549f6687efb7e0a932b792ace58e9)#define FUNC\_SSI\_WS1\_B IPSR(16, 28, 4)

[ 860](pinctrl-r8a77961_8h.md#a2e2564694ce3d9bab2ca634110babd12)#define FUNC\_SCK1 IPSR(16, 28, 5)

[ 861](pinctrl-r8a77961_8h.md#ae91f26231d6566ebff97fc87eddf109c)#define FUNC\_STP\_IVCXO27\_1\_A IPSR(16, 28, 6)

[ 862](pinctrl-r8a77961_8h.md#a5e75e00efb9f74904f6c547b299691ee)#define FUNC\_SCK5\_A IPSR(16, 28, 7)

[ 863](pinctrl-r8a77961_8h.md#a0f3c0c219174dbe62cb7e01984b9ee90)#define FUNC\_AUDIO\_CLKA\_A IPSR(17, 0, 0)

[ 864](pinctrl-r8a77961_8h.md#a0218f2cc8549ad7c3af73314fc26a01b)#define FUNC\_AUDIO\_CLKB\_B IPSR(17, 4, 0)

[ 865](pinctrl-r8a77961_8h.md#af8bba41585000cc8fa914b90453d6364)#define FUNC\_SCIF\_CLK\_A IPSR(17, 4, 1)

[ 866](pinctrl-r8a77961_8h.md#a652c8f51992655021a7296a78a80d1d5)#define FUNC\_STP\_IVCXO27\_1\_D IPSR(17, 4, 6)

[ 867](pinctrl-r8a77961_8h.md#a6d82afc82785cdb20738f482452365c7)#define FUNC\_REMOCON\_A IPSR(17, 4, 7)

[ 868](pinctrl-r8a77961_8h.md#a91a2649ff614550dffde6131a03c098b)#define FUNC\_TCLK1\_A IPSR(17, 4, 0xA)

[ 869](pinctrl-r8a77961_8h.md#a2ad6bc4a1fbad1f738f876f640c94452)#define FUNC\_USB0\_PWEN IPSR(17, 8, 0)

[ 870](pinctrl-r8a77961_8h.md#ad83b311b03381529834262e59f448818)#define FUNC\_SIM0\_RST\_C IPSR(17, 8, 3)

[ 871](pinctrl-r8a77961_8h.md#ace4e01486ee6c2952f9ae90280a4994f)#define FUNC\_TS\_SCK1\_D IPSR(17, 8, 5)

[ 872](pinctrl-r8a77961_8h.md#adc7404f86cffed470117045b8f9d6806)#define FUNC\_STP\_ISCLK\_1\_D IPSR(17, 8, 6)

[ 873](pinctrl-r8a77961_8h.md#a54ee5608a35cf64778f182f099965b01)#define FUNC\_BPFCLK\_B IPSR(17, 8, 7)

[ 874](pinctrl-r8a77961_8h.md#a36bf9c8fa6d6b766b0f07e2e5f7a7a36)#define FUNC\_RIF3\_CLK\_B IPSR(17, 8, 8)

[ 875](pinctrl-r8a77961_8h.md#aadacafaf74810f438be78c5c682b2e7e)#define FUNC\_HSCK2\_C IPSR(17, 8, 0xD)

[ 876](pinctrl-r8a77961_8h.md#a8e84feedd35ff46ac7a7ff6ae3ccdc74)#define FUNC\_USB0\_OVC IPSR(17, 12, 0)

[ 877](pinctrl-r8a77961_8h.md#a4db57453d4f62461002c3e16dc72d9c4)#define FUNC\_SIM0\_D\_C IPSR(17, 12, 3)

[ 878](pinctrl-r8a77961_8h.md#a927e0277129fa92062331f48c5a07766)#define FUNC\_TS\_SDAT1\_D IPSR(17, 12, 5)

[ 879](pinctrl-r8a77961_8h.md#a39e3d8524aac4933067dec9908255191)#define FUNC\_STP\_ISD\_1\_D IPSR(17, 12, 6)

[ 880](pinctrl-r8a77961_8h.md#a8f50711741c30e25a56f8ec529c58096)#define FUNC\_RIF3\_SYNC\_B IPSR(17, 12, 8)

[ 881](pinctrl-r8a77961_8h.md#aff5c7980410d88ceb52811a470f04696)#define FUNC\_HRX2\_C IPSR(17, 12, 0xD)

[ 882](pinctrl-r8a77961_8h.md#a70aba76cb9298ed814fea851cdd1d1bb)#define FUNC\_USB1\_PWEN IPSR(17, 16, 0)

[ 883](pinctrl-r8a77961_8h.md#a680f170811abb36d8c6b303f21bf337d)#define FUNC\_SIM0\_CLK\_C IPSR(17, 16, 3)

[ 884](pinctrl-r8a77961_8h.md#ac76da41355f368ac49e12c88774acdfb)#define FUNC\_SSI\_SCK1\_A IPSR(17, 16, 4)

[ 885](pinctrl-r8a77961_8h.md#afaf56e567b680ef37064f15228afc7f9)#define FUNC\_TS\_SCK0\_E IPSR(17, 16, 5)

[ 886](pinctrl-r8a77961_8h.md#a25d8bb75b9dd0d1fff8678cdf7cde0c0)#define FUNC\_STP\_ISCLK\_0\_E IPSR(17, 16, 6)

[ 887](pinctrl-r8a77961_8h.md#a5db07d195fd5311c11119f92951ac448)#define FUNC\_FMCLK\_B IPSR(17, 16, 7)

[ 888](pinctrl-r8a77961_8h.md#a55b709f6ed2044b54f29e4aedbd6bf87)#define FUNC\_RIF2\_CLK\_B IPSR(17, 16, 8)

[ 889](pinctrl-r8a77961_8h.md#a19c6ffa7c592123ede9860fec0297cf3)#define FUNC\_SPEEDIN\_A IPSR(17, 16, 0xA)

[ 890](pinctrl-r8a77961_8h.md#abb152a0d8c2b811ff22e5bac3552e507)#define FUNC\_HTX2\_C IPSR(17, 16, 0xD)

[ 891](pinctrl-r8a77961_8h.md#ad5ff7b0885922c169f5dd7b9b9667409)#define FUNC\_USB1\_OVC IPSR(17, 20, 0)

[ 892](pinctrl-r8a77961_8h.md#a89fdb8687ce418834780990c2c4cba28)#define FUNC\_MSIOF1\_SS2\_C IPSR(17, 20, 2)

[ 893](pinctrl-r8a77961_8h.md#a438f7a36efa57893617d818b64b4c817)#define FUNC\_SSI\_WS1\_A IPSR(17, 20, 4)

[ 894](pinctrl-r8a77961_8h.md#a38d85b25232b3ea336522cbe2a1adb5c)#define FUNC\_TS\_SDAT0\_E IPSR(17, 20, 5)

[ 895](pinctrl-r8a77961_8h.md#a9d9e4a6cb2a5a7bf725398dbcb2294c1)#define FUNC\_STP\_ISD\_0\_E IPSR(17, 20, 6)

[ 896](pinctrl-r8a77961_8h.md#a133d0c48a1844b69c02352734bcf2ddb)#define FUNC\_FMIN\_B IPSR(17, 20, 7)

[ 897](pinctrl-r8a77961_8h.md#afdecccde4a408314026836f8847f3f65)#define FUNC\_RIF2\_SYNC\_B IPSR(17, 20, 8)

[ 898](pinctrl-r8a77961_8h.md#a1928d1c592b31d0ffad9c93fafd7d7da)#define FUNC\_REMOCON\_B IPSR(17, 20, 0xA)

[ 899](pinctrl-r8a77961_8h.md#afec2be8a3787edb3cc09be0461e32d3d)#define FUNC\_HCTS2\_N\_C IPSR(17, 20, 0xD)

[ 900](pinctrl-r8a77961_8h.md#ad4f36d150345071cb7e55c96a4c35810)#define FUNC\_USB30\_PWEN IPSR(17, 24, 0)

[ 901](pinctrl-r8a77961_8h.md#a9d58a687f948ee8ce8cc0dbe74bd6426)#define FUNC\_AUDIO\_CLKOUT\_B IPSR(17, 24, 3)

[ 902](pinctrl-r8a77961_8h.md#a702c5f8ae709d3440e191a78f2714947)#define FUNC\_SSI\_SCK2\_B IPSR(17, 24, 4)

[ 903](pinctrl-r8a77961_8h.md#ab5acab8cf00bf9f1b75792d2687079c5)#define FUNC\_TS\_SDEN1\_D IPSR(17, 24, 5)

[ 904](pinctrl-r8a77961_8h.md#a9f5b75ad3bd4c163b8929537c8dcfbcb)#define FUNC\_STP\_ISEN\_1\_D IPSR(17, 24, 6)

[ 905](pinctrl-r8a77961_8h.md#a73e6a447ed044f347768151fffec428e)#define FUNC\_STP\_OPWM\_0\_E IPSR(17, 24, 7)

[ 906](pinctrl-r8a77961_8h.md#aaeaa3542fb4cf00d1c7d78593d3603f1)#define FUNC\_RIF3\_D0\_B IPSR(17, 24, 8)

[ 907](pinctrl-r8a77961_8h.md#a6c43ebda6d2de9f4aa61f7a903399587)#define FUNC\_TCLK2\_B IPSR(17, 24, 0xA)

[ 908](pinctrl-r8a77961_8h.md#a0764368273d9d31cbdb3f54ee4ea626f)#define FUNC\_TPU0TO0 IPSR(17, 24, 0xB)

[ 909](pinctrl-r8a77961_8h.md#a1b02d4d9f6b642c157fdda06d7a5c98b)#define FUNC\_BPFCLK\_C IPSR(17, 24, 0xC)

[ 910](pinctrl-r8a77961_8h.md#a6dd3342a41ab070e2292f630fbe2ff98)#define FUNC\_HRTS2\_N\_C IPSR(17, 24, 0xD)

[ 911](pinctrl-r8a77961_8h.md#a10c621a3f26372a15f0d8c2caf6964c2)#define FUNC\_USB30\_OVC IPSR(17, 28, 0)

[ 912](pinctrl-r8a77961_8h.md#a29fe28383dee8cef5e79fc5207eadc5b)#define FUNC\_AUDIO\_CLKOUT1\_B IPSR(17, 28, 3)

[ 913](pinctrl-r8a77961_8h.md#aa085020c8670f9787d1c0ba53b35d813)#define FUNC\_SSI\_WS2\_B IPSR(17, 28, 4)

[ 914](pinctrl-r8a77961_8h.md#a2b4ccb683b7812f678473d0d9b3e321f)#define FUNC\_TS\_SPSYNC1\_D IPSR(17, 28, 5)

[ 915](pinctrl-r8a77961_8h.md#a3ff6b215ff4ba07d8be62c17b3fe7c46)#define FUNC\_STP\_ISSYNC\_1\_D IPSR(17, 28, 6)

[ 916](pinctrl-r8a77961_8h.md#ac6df932b9cccce6181a22ad7ab544fbf)#define FUNC\_STP\_IVCXO27\_0\_E IPSR(17, 28, 7)

[ 917](pinctrl-r8a77961_8h.md#a6c936d9270693ee8675fff1ad025c262)#define FUNC\_RIF3\_D1\_B IPSR(17, 28, 8)

[ 918](pinctrl-r8a77961_8h.md#a1efbdc6c16737656222606bb2a0e5f8d)#define FUNC\_FSO\_TOE\_N IPSR(17, 28, 0xA)

[ 919](pinctrl-r8a77961_8h.md#a5e63de377e97906812266f8e48e1822c)#define FUNC\_TPU0TO1 IPSR(17, 28, 0xB)

[ 920](pinctrl-r8a77961_8h.md#a852cb439b8659ea3ad85e24436d3705e)#define FUNC\_GP6\_30 IPSR(18, 0, 0)

[ 921](pinctrl-r8a77961_8h.md#a9a0ba05de996a89ca76c42ddac24d3f7)#define FUNC\_AUDIO\_CLKOUT2\_B IPSR(18, 0, 3)

[ 922](pinctrl-r8a77961_8h.md#a65aec08cf24ec781d93d8ca08d5ff08d)#define FUNC\_SSI\_SCK9\_B IPSR(18, 0, 4)

[ 923](pinctrl-r8a77961_8h.md#a157133a37ceeb9da75195b4f6b9afb9a)#define FUNC\_TS\_SDEN0\_E IPSR(18, 0, 5)

[ 924](pinctrl-r8a77961_8h.md#a4c53c04a27012097fd741c9c9275b8f3)#define FUNC\_STP\_ISEN\_0\_E IPSR(18, 0, 6)

[ 925](pinctrl-r8a77961_8h.md#aaa3e9397cbe99406364ef9bb921ca8b4)#define FUNC\_RIF2\_D0\_B IPSR(18, 0, 8)

[ 926](pinctrl-r8a77961_8h.md#a8e3200e828055bf687c40e78f1c0eeb2)#define FUNC\_TPU0TO2 IPSR(18, 0, 0xB)

[ 927](pinctrl-r8a77961_8h.md#ac8f120eed8601812e75476028b75749b)#define FUNC\_FMCLK\_C IPSR(18, 0, 0xC)

[ 928](pinctrl-r8a77961_8h.md#abd6de6083bf9117f0a4a1feab8279cd4)#define FUNC\_FMCLK\_D IPSR(18, 0, 0xD)

[ 929](pinctrl-r8a77961_8h.md#a97ac25103ad9f2a6bcd3423608ec07ca)#define FUNC\_GP6\_31 IPSR(18, 4, 0)

[ 930](pinctrl-r8a77961_8h.md#a493dbe0287354725df869360a4afd362)#define FUNC\_AUDIO\_CLKOUT3\_B IPSR(18, 4, 3)

[ 931](pinctrl-r8a77961_8h.md#aa8bb9e730874ea96b113ae6f3bc684c4)#define FUNC\_SSI\_WS9\_B IPSR(18, 4, 4)

[ 932](pinctrl-r8a77961_8h.md#a5d4ba16a51c1aa124ea4dc859262c2f2)#define FUNC\_TS\_SPSYNC0\_E IPSR(18, 4, 5)

[ 933](pinctrl-r8a77961_8h.md#a1921e1cfee91b3f7e63c6271ed967412)#define FUNC\_STP\_ISSYNC\_0\_E IPSR(18, 4, 6)

[ 934](pinctrl-r8a77961_8h.md#a4bf075b2c690c89a12463c61a1a7d7b6)#define FUNC\_RIF2\_D1\_B IPSR(18, 4, 8)

[ 935](pinctrl-r8a77961_8h.md#a758a67db1bc73aed85e678b7e6981634)#define FUNC\_TPU0TO3 IPSR(18, 4, 0xB)

[ 936](pinctrl-r8a77961_8h.md#a87ee3540ac671709d6c64a9c53afaccc)#define FUNC\_FMIN\_C IPSR(18, 4, 0xC)

[ 937](pinctrl-r8a77961_8h.md#a9cc0ec3abec58c01e5f6f6ecf290ff18)#define FUNC\_FMIN\_D IPSR(18, 4, 0xD)

938

939#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_PINCTRL\_RENESAS\_PINCTRL\_R8A77961\_H\_ \*/

[pinctrl-rcar-common.h](pinctrl-rcar-common_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [pinctrl](dir_2c6c4fbd167577104b7f1b7148586168.md)
- [renesas](dir_17f48eb154be6cea623223db5de209e7.md)
- [pinctrl-r8a77961.h](pinctrl-r8a77961_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
