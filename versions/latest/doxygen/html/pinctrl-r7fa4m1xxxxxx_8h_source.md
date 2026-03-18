---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/pinctrl-r7fa4m1xxxxxx_8h_source.html
original_path: doxygen/html/pinctrl-r7fa4m1xxxxxx_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

pinctrl-r7fa4m1xxxxxx.h

[Go to the documentation of this file.](pinctrl-r7fa4m1xxxxxx_8h.md)

1/\*

2 \* Copyright (c) 2023 TOKITA Hiroshi <tokita.hiroshi@fujitsu.com>

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_DT\_BINDINGS\_PINCTRL\_RENESAS\_PINCTRL\_R7FA4M1XXXXXX\_H\_

8#define ZEPHYR\_DT\_BINDINGS\_PINCTRL\_RENESAS\_PINCTRL\_R7FA4M1XXXXXX\_H\_

9

10#include <[zephyr/dt-bindings/pinctrl/renesas/pinctrl-ra-common.h](pinctrl-ra-common_8h.md)>

11

[ 12](pinctrl-r7fa4m1xxxxxx_8h.md#ae842db00a916bca58722bf9463d4d714)#define P000\_AMP0P RA\_PINCFG\_\_40(0, 0, 0x02, RA\_PINCFG\_FUNC | RA\_PINCFG\_ANALOG)

[ 13](pinctrl-r7fa4m1xxxxxx_8h.md#a4e0d0026b52e2b99917ac89a3441f81d)#define P000\_AN000 RA\_PINCFG\_\_40(0, 0, 0x01, RA\_PINCFG\_ANALOG)

[ 14](pinctrl-r7fa4m1xxxxxx_8h.md#adc1541807bda207b93f248b0ef8214b2)#define P000\_TS21 RA\_PINCFG\_\_40(0, 0, 0x0C, RA\_PINCFG\_FUNC)

[ 15](pinctrl-r7fa4m1xxxxxx_8h.md#a95a99a6eca2dbe141e01496ccc119c97)#define P001\_AMP0M RA\_PINCFG\_\_40(0, 1, 0x02, RA\_PINCFG\_FUNC | RA\_PINCFG\_ANALOG)

[ 16](pinctrl-r7fa4m1xxxxxx_8h.md#a6becb6ea213d2a7a9473d847fd2e1afc)#define P001\_AN001 RA\_PINCFG\_\_40(0, 1, 0x01, RA\_PINCFG\_ANALOG)

[ 17](pinctrl-r7fa4m1xxxxxx_8h.md#a0bc53bba6bd1b565bebbb32d82491f58)#define P001\_TS22 RA\_PINCFG\_\_40(0, 1, 0x0C, RA\_PINCFG\_FUNC)

[ 18](pinctrl-r7fa4m1xxxxxx_8h.md#ac67986afc797ad8c3e942f7b36060a8b)#define P002\_AMP0O RA\_PINCFG\_\_48(0, 2, 0x02, RA\_PINCFG\_FUNC | RA\_PINCFG\_ANALOG)

[ 19](pinctrl-r7fa4m1xxxxxx_8h.md#a0e3055cd0decb05639d3d93069383c61)#define P002\_AN002 RA\_PINCFG\_\_48(0, 2, 0x01, RA\_PINCFG\_ANALOG)

[ 20](pinctrl-r7fa4m1xxxxxx_8h.md#a3d5d3787070875a571f4bb4a44dd6f51)#define P003\_AMP1O RA\_PINCFG\_\_64(0, 3, 0x02, RA\_PINCFG\_FUNC | RA\_PINCFG\_ANALOG)

[ 21](pinctrl-r7fa4m1xxxxxx_8h.md#a46d84f8f6a19729cba7e882cb4cbae0b)#define P003\_AN003 RA\_PINCFG\_\_64(0, 3, 0x01, RA\_PINCFG\_ANALOG)

[ 22](pinctrl-r7fa4m1xxxxxx_8h.md#ab7d1c0cdca0cc5b127ba8d290c0d4e8e)#define P004\_AMP2O RA\_PINCFG\_\_64(0, 4, 0x02, RA\_PINCFG\_FUNC | RA\_PINCFG\_ANALOG)

[ 23](pinctrl-r7fa4m1xxxxxx_8h.md#a4ae2410a96e97dc7ced6e96112b6c615)#define P004\_AN004 RA\_PINCFG\_\_64(0, 4, 0x01, RA\_PINCFG\_ANALOG)

[ 24](pinctrl-r7fa4m1xxxxxx_8h.md#aba1ec6a1319ba9a17b3cdbf808ab6cb3)#define P005\_AMP3P RA\_PINCFG\_100(0, 5, 0x02, RA\_PINCFG\_FUNC | RA\_PINCFG\_ANALOG)

[ 25](pinctrl-r7fa4m1xxxxxx_8h.md#a78d7679475484b26c48b41cbca5f9b43)#define P005\_AN011 RA\_PINCFG\_100(0, 5, 0x01, RA\_PINCFG\_ANALOG)

[ 26](pinctrl-r7fa4m1xxxxxx_8h.md#adc5c93e5ba179c526cf269812d29583d)#define P006\_AMP3M RA\_PINCFG\_100(0, 6, 0x02, RA\_PINCFG\_FUNC | RA\_PINCFG\_ANALOG)

[ 27](pinctrl-r7fa4m1xxxxxx_8h.md#a05963433b19f0150df3f31219128a6c5)#define P006\_AN012 RA\_PINCFG\_100(0, 6, 0x01, RA\_PINCFG\_ANALOG)

[ 28](pinctrl-r7fa4m1xxxxxx_8h.md#ab94624d451f292a4944fb56b9a1fbf6c)#define P007\_AMP3O RA\_PINCFG\_100(0, 7, 0x02, RA\_PINCFG\_FUNC | RA\_PINCFG\_ANALOG)

[ 29](pinctrl-r7fa4m1xxxxxx_8h.md#a6af7314aaefb64d307d87c96469ce287)#define P007\_AN013 RA\_PINCFG\_100(0, 7, 0x01, RA\_PINCFG\_ANALOG)

[ 30](pinctrl-r7fa4m1xxxxxx_8h.md#a5d357e31442086a2cbabfefef985e16f)#define P008\_AN014 RA\_PINCFG\_100(0, 8, 0x01, RA\_PINCFG\_ANALOG)

[ 31](pinctrl-r7fa4m1xxxxxx_8h.md#ae99823a1a2a5afef699b816729a1f4bc)#define P010\_AMP2M RA\_PINCFG\_\_40(0, 10, 0x02, RA\_PINCFG\_FUNC | RA\_PINCFG\_ANALOG)

[ 32](pinctrl-r7fa4m1xxxxxx_8h.md#a4a0c2622dcec865e4e0de95cc0bc2642)#define P010\_AN005 RA\_PINCFG\_\_40(0, 10, 0x01, RA\_PINCFG\_ANALOG)

[ 33](pinctrl-r7fa4m1xxxxxx_8h.md#a06910d9544b4f17fe9340fcd3335726e)#define P010\_TS30 RA\_PINCFG\_\_40(0, 10, 0x0C, RA\_PINCFG\_FUNC)

[ 34](pinctrl-r7fa4m1xxxxxx_8h.md#ad8de027943cbb82daaa59e85bded2e89)#define P010\_VREFH0 RA\_PINCFG\_\_40(0, 10, 0x03, RA\_PINCFG\_FUNC | RA\_PINCFG\_ANALOG)

[ 35](pinctrl-r7fa4m1xxxxxx_8h.md#a556ce5945ee752b3649b3dc6701d3116)#define P011\_AN006 RA\_PINCFG\_\_40(0, 11, 0x01, RA\_PINCFG\_ANALOG)

[ 36](pinctrl-r7fa4m1xxxxxx_8h.md#aa421bcafd69c7f84eba6baaf9682106c)#define P011\_TS31 RA\_PINCFG\_\_40(0, 11, 0x0C, RA\_PINCFG\_FUNC)

[ 37](pinctrl-r7fa4m1xxxxxx_8h.md#a21078d18b4540e2b0387347b450b39cb)#define P011\_VREFL0 RA\_PINCFG\_\_40(0, 11, 0x03, RA\_PINCFG\_FUNC | RA\_PINCFG\_ANALOG)

[ 38](pinctrl-r7fa4m1xxxxxx_8h.md#ad673f99af344726d98d68ba8d33d2dc6)#define P012\_AN007 RA\_PINCFG\_\_40(0, 12, 0x01, RA\_PINCFG\_ANALOG)

[ 39](pinctrl-r7fa4m1xxxxxx_8h.md#abfb4252be9decd74c6b8e50d8e6c1ada)#define P012\_VREFH RA\_PINCFG\_\_40(0, 12, 0x03, RA\_PINCFG\_FUNC | RA\_PINCFG\_ANALOG)

[ 40](pinctrl-r7fa4m1xxxxxx_8h.md#a822f3370e98657c2ee31a68643c7c995)#define P013\_AN008 RA\_PINCFG\_\_40(0, 13, 0x01, RA\_PINCFG\_ANALOG)

[ 41](pinctrl-r7fa4m1xxxxxx_8h.md#a55c50ec1174040ab7f56fe68512605d2)#define P013\_VREFL RA\_PINCFG\_\_40(0, 13, 0x03, RA\_PINCFG\_FUNC | RA\_PINCFG\_ANALOG)

[ 42](pinctrl-r7fa4m1xxxxxx_8h.md#a206085dcc14e1b108f9a59633bc69a33)#define P014\_AN009 RA\_PINCFG\_\_40(0, 14, 0x01, RA\_PINCFG\_ANALOG)

[ 43](pinctrl-r7fa4m1xxxxxx_8h.md#a4a16849ab86889d6eed82430bc75c896)#define P014\_DA0 RA\_PINCFG\_\_40(0, 14, 0x02, RA\_PINCFG\_FUNC | RA\_PINCFG\_ANALOG)

[ 44](pinctrl-r7fa4m1xxxxxx_8h.md#ab04ac47d40b8be1da30eb2c29279086d)#define P015\_AN010 RA\_PINCFG\_\_40(0, 15, 0x01, RA\_PINCFG\_ANALOG)

[ 45](pinctrl-r7fa4m1xxxxxx_8h.md#a9ed5295f39b1095e0ca4c378960a1ba8)#define P015\_TS28 RA\_PINCFG\_\_40(0, 15, 0x0C, RA\_PINCFG\_FUNC)

[ 46](pinctrl-r7fa4m1xxxxxx_8h.md#a191c552bbe2a1efd4d919f8bb1c2d7be)#define P100\_AGTIO0 RA\_PINCFG\_\_40(1, 0, 0x01, RA\_PINCFG\_FUNC)

[ 47](pinctrl-r7fa4m1xxxxxx_8h.md#ac62a4efe4715fb8703c7e00b716a0932)#define P100\_AN022 RA\_PINCFG\_\_40(1, 0, 0x01, RA\_PINCFG\_ANALOG)

[ 48](pinctrl-r7fa4m1xxxxxx_8h.md#ae669095211980b7fda1800a79c70ccb1)#define P100\_CMPIN0 RA\_PINCFG\_\_40(1, 0, 0x02, RA\_PINCFG\_FUNC | RA\_PINCFG\_ANALOG)

[ 49](pinctrl-r7fa4m1xxxxxx_8h.md#ac0e5fccc67d7ebd6c4e4cd3acd91dfba)#define P100\_GTETRGA RA\_PINCFG\_\_40(1, 0, 0x02, RA\_PINCFG\_FUNC)

[ 50](pinctrl-r7fa4m1xxxxxx_8h.md#a4819391c30e8895c5dda935135258c2e)#define P100\_GTIOC5B RA\_PINCFG\_\_40(1, 0, 0x03, RA\_PINCFG\_FUNC)

[ 51](pinctrl-r7fa4m1xxxxxx_8h.md#aaa6388038debf85ea85715f58d7ad350)#define P100\_KR00 RA\_PINCFG\_\_40(1, 0, 0x08, RA\_PINCFG\_FUNC)

[ 52](pinctrl-r7fa4m1xxxxxx_8h.md#ab9fb3af59d2c60234ae098f9afcfd1e9)#define P100\_MISO0 RA\_PINCFG\_\_40(1, 0, 0x04, RA\_PINCFG\_FUNC)

[ 53](pinctrl-r7fa4m1xxxxxx_8h.md#a56c483cb23004827d8f244ae60b54f42)#define P100\_MISOA RA\_PINCFG\_\_40(1, 0, 0x06, RA\_PINCFG\_FUNC)

[ 54](pinctrl-r7fa4m1xxxxxx_8h.md#ab6c04153136a3c255e8d578f0593a21a)#define P100\_RXD0 RA\_PINCFG\_\_40(1, 0, 0x04, RA\_PINCFG\_FUNC)

[ 55](pinctrl-r7fa4m1xxxxxx_8h.md#a2703b58e70a85f06634fd6c5dec175b6)#define P100\_SCK1 RA\_PINCFG\_\_40(1, 0, 0x05, RA\_PINCFG\_FUNC)

[ 56](pinctrl-r7fa4m1xxxxxx_8h.md#a1ac52cf706cfa4af02fd42f8b1bb8bbc)#define P100\_SCL0 RA\_PINCFG\_\_40(1, 0, 0x04, RA\_PINCFG\_FUNC)

[ 57](pinctrl-r7fa4m1xxxxxx_8h.md#a8d9fce95c5b1857c8d8c0a538780e4e8)#define P100\_SCL1 RA\_PINCFG\_\_40(1, 0, 0x07, RA\_PINCFG\_FUNC)

[ 58](pinctrl-r7fa4m1xxxxxx_8h.md#a12aa769c25faf09aee05dee7d5cb2b21)#define P100\_VL1 RA\_PINCFG\_\_40(1, 0, 0x0D, RA\_PINCFG\_FUNC)

[ 59](pinctrl-r7fa4m1xxxxxx_8h.md#a97201e0b5b0d594e12878a9019a552ac)#define P101\_AGTEE0 RA\_PINCFG\_\_40(1, 1, 0x01, RA\_PINCFG\_FUNC)

[ 60](pinctrl-r7fa4m1xxxxxx_8h.md#a2810c5803f8ce2206fbce9c73823cd3b)#define P101\_AN021 RA\_PINCFG\_\_40(1, 1, 0x01, RA\_PINCFG\_ANALOG)

[ 61](pinctrl-r7fa4m1xxxxxx_8h.md#ae674d7008b45a8e3aa99a38d6e9bf6ea)#define P101\_CMPREF0 RA\_PINCFG\_\_40(1, 1, 0x02, RA\_PINCFG\_FUNC | RA\_PINCFG\_ANALOG)

[ 62](pinctrl-r7fa4m1xxxxxx_8h.md#a2389f25d732391431dcd22b1ec850a23)#define P101\_CTS1\_RTS1 RA\_PINCFG\_\_40(1, 1, 0x05, RA\_PINCFG\_FUNC)

[ 63](pinctrl-r7fa4m1xxxxxx_8h.md#a23ae6860f187482eeb1ac632de94cfbc)#define P101\_GTETRGB RA\_PINCFG\_\_40(1, 1, 0x02, RA\_PINCFG\_FUNC)

[ 64](pinctrl-r7fa4m1xxxxxx_8h.md#a5a8189c67184dae7107c6e73afdd5158)#define P101\_GTIOC5A RA\_PINCFG\_\_40(1, 1, 0x03, RA\_PINCFG\_FUNC)

[ 65](pinctrl-r7fa4m1xxxxxx_8h.md#a342876600314b767e2ccea9994ea962e)#define P101\_KR01 RA\_PINCFG\_\_40(1, 1, 0x08, RA\_PINCFG\_FUNC)

[ 66](pinctrl-r7fa4m1xxxxxx_8h.md#a12b1711fea2cedbe01b2f6e4f37fc22f)#define P101\_MOSI0 RA\_PINCFG\_\_40(1, 1, 0x04, RA\_PINCFG\_FUNC)

[ 67](pinctrl-r7fa4m1xxxxxx_8h.md#ae0d87219646a5d3cd47773548e28ad0f)#define P101\_MOSIA RA\_PINCFG\_\_40(1, 1, 0x06, RA\_PINCFG\_FUNC)

[ 68](pinctrl-r7fa4m1xxxxxx_8h.md#ae6c6b883d31ebc77b215adf1914d9686)#define P101\_SDA0 RA\_PINCFG\_\_40(1, 1, 0x04, RA\_PINCFG\_FUNC)

[ 69](pinctrl-r7fa4m1xxxxxx_8h.md#a8860199add20bb7be47bbb20f21e8402)#define P101\_SDA1 RA\_PINCFG\_\_40(1, 1, 0x07, RA\_PINCFG\_FUNC)

[ 70](pinctrl-r7fa4m1xxxxxx_8h.md#a2cc85ea89ee831c167f6f79195587af6)#define P101\_SS1 RA\_PINCFG\_\_40(1, 1, 0x05, RA\_PINCFG\_FUNC)

[ 71](pinctrl-r7fa4m1xxxxxx_8h.md#aad7215254c05ef37e526e324c2f719af)#define P101\_TXD0 RA\_PINCFG\_\_40(1, 1, 0x04, RA\_PINCFG\_FUNC)

[ 72](pinctrl-r7fa4m1xxxxxx_8h.md#ae90651e5cb299491851d09c877a6deb2)#define P101\_VL2 RA\_PINCFG\_\_40(1, 1, 0x0D, RA\_PINCFG\_FUNC)

[ 73](pinctrl-r7fa4m1xxxxxx_8h.md#a89adc8e794ae0c934c9e923672cc9e71)#define P102\_ADTRG0 RA\_PINCFG\_\_40(1, 2, 0x0A, RA\_PINCFG\_FUNC)

[ 74](pinctrl-r7fa4m1xxxxxx_8h.md#af47c973f79583e5e058ec5cc2f587bb4)#define P102\_AGTO0 RA\_PINCFG\_\_40(1, 2, 0x01, RA\_PINCFG\_FUNC)

[ 75](pinctrl-r7fa4m1xxxxxx_8h.md#a39c60fc6901fd9da9c38085252fb1b58)#define P102\_AN020 RA\_PINCFG\_\_40(1, 2, 0x01, RA\_PINCFG\_ANALOG)

[ 76](pinctrl-r7fa4m1xxxxxx_8h.md#ae6c3d77860504e23c3f9214ced585f0b)#define P102\_CMPIN1 RA\_PINCFG\_\_40(1, 2, 0x02, RA\_PINCFG\_FUNC | RA\_PINCFG\_ANALOG)

[ 77](pinctrl-r7fa4m1xxxxxx_8h.md#a7f9d3a73ccab598f76c7380f9b03f460)#define P102\_CRX0 RA\_PINCFG\_\_40(1, 2, 0x10, RA\_PINCFG\_FUNC)

[ 78](pinctrl-r7fa4m1xxxxxx_8h.md#a25129a4adab5e5f2bb175fcdf47e141b)#define P102\_GTIOC2B RA\_PINCFG\_\_40(1, 2, 0x03, RA\_PINCFG\_FUNC)

[ 79](pinctrl-r7fa4m1xxxxxx_8h.md#a8c39b7e9dbe6e7d720c3d6de79c94031)#define P102\_GTOWLO RA\_PINCFG\_\_40(1, 2, 0x02, RA\_PINCFG\_FUNC)

[ 80](pinctrl-r7fa4m1xxxxxx_8h.md#aa9a2c2dad0d668d684f613b26b70e41b)#define P102\_KR02 RA\_PINCFG\_\_40(1, 2, 0x08, RA\_PINCFG\_FUNC)

[ 81](pinctrl-r7fa4m1xxxxxx_8h.md#a781c643f4045a05221ba22a04f4fbdb1)#define P102\_MOSI2 RA\_PINCFG\_\_40(1, 2, 0x05, RA\_PINCFG\_FUNC)

[ 82](pinctrl-r7fa4m1xxxxxx_8h.md#a2b4677ef62359635c133c3ffd7b30646)#define P102\_RSPCKA RA\_PINCFG\_\_40(1, 2, 0x06, RA\_PINCFG\_FUNC)

[ 83](pinctrl-r7fa4m1xxxxxx_8h.md#a0007c9b8793135cdb6493eee64e3f69a)#define P102\_SCK0 RA\_PINCFG\_\_40(1, 2, 0x04, RA\_PINCFG\_FUNC)

[ 84](pinctrl-r7fa4m1xxxxxx_8h.md#aa3dcc1d7e031f1ddf4c25f01a737323d)#define P102\_SDA2 RA\_PINCFG\_\_40(1, 2, 0x05, RA\_PINCFG\_FUNC)

[ 85](pinctrl-r7fa4m1xxxxxx_8h.md#aaf38b042bfdcd872e6009e44f12ddddb)#define P102\_TXD2 RA\_PINCFG\_\_40(1, 2, 0x05, RA\_PINCFG\_FUNC)

[ 86](pinctrl-r7fa4m1xxxxxx_8h.md#a7f69ce4cceda74a1c954424d0bab7375)#define P102\_VL3 RA\_PINCFG\_\_40(1, 2, 0x0D, RA\_PINCFG\_FUNC)

[ 87](pinctrl-r7fa4m1xxxxxx_8h.md#a17de1ddf81792dab895613faf3ce9536)#define P103\_AN019 RA\_PINCFG\_\_48(1, 3, 0x01, RA\_PINCFG\_ANALOG)

[ 88](pinctrl-r7fa4m1xxxxxx_8h.md#a95a1d6e4bfdd6260afc393489f203f61)#define P103\_CMPREF1 RA\_PINCFG\_\_48(1, 3, 0x02, RA\_PINCFG\_FUNC | RA\_PINCFG\_ANALOG)

[ 89](pinctrl-r7fa4m1xxxxxx_8h.md#ac7bd831a35c6547eba69f3aae707d6dd)#define P103\_CTS0\_RTS0 RA\_PINCFG\_\_48(1, 3, 0x04, RA\_PINCFG\_FUNC)

[ 90](pinctrl-r7fa4m1xxxxxx_8h.md#a7eb99f1317f8258ecfa1b6c316f3374d)#define P103\_CTX0 RA\_PINCFG\_\_48(1, 3, 0x10, RA\_PINCFG\_FUNC)

[ 91](pinctrl-r7fa4m1xxxxxx_8h.md#a9694a5a3bd228d40e7d9a1a26ad0136d)#define P103\_GTIOC2A RA\_PINCFG\_\_48(1, 3, 0x03, RA\_PINCFG\_FUNC)

[ 92](pinctrl-r7fa4m1xxxxxx_8h.md#a5c4ce6fab94ba55dc6723295b6025d96)#define P103\_GTOWUP RA\_PINCFG\_\_48(1, 3, 0x02, RA\_PINCFG\_FUNC)

[ 93](pinctrl-r7fa4m1xxxxxx_8h.md#a287f2b9b75cd66cdc9699e7508519b75)#define P103\_KR03 RA\_PINCFG\_\_48(1, 3, 0x08, RA\_PINCFG\_FUNC)

[ 94](pinctrl-r7fa4m1xxxxxx_8h.md#a2d4539d9d0a0740106c5a7ed429a3168)#define P103\_SS0 RA\_PINCFG\_\_48(1, 3, 0x04, RA\_PINCFG\_FUNC)

[ 95](pinctrl-r7fa4m1xxxxxx_8h.md#a2f7dc46787c2609aeae250d731c20c9a)#define P103\_SSLA0 RA\_PINCFG\_\_48(1, 3, 0x06, RA\_PINCFG\_FUNC)

[ 96](pinctrl-r7fa4m1xxxxxx_8h.md#a27f22cb3adc115489d52978d84f04082)#define P103\_VL4 RA\_PINCFG\_\_48(1, 3, 0x0D, RA\_PINCFG\_FUNC)

[ 97](pinctrl-r7fa4m1xxxxxx_8h.md#a7e6e268a71a35d8b9000455586417e55)#define P104\_COM0 RA\_PINCFG\_\_48(1, 4, 0x0D, RA\_PINCFG\_FUNC)

[ 98](pinctrl-r7fa4m1xxxxxx_8h.md#a428dcf1c4e6049fd86be1682847e1360)#define P104\_GTETRGB RA\_PINCFG\_\_48(1, 4, 0x02, RA\_PINCFG\_FUNC)

[ 99](pinctrl-r7fa4m1xxxxxx_8h.md#a1a2d82623839ae265fabb4de355a7f5d)#define P104\_GTIOC1B RA\_PINCFG\_\_48(1, 4, 0x03, RA\_PINCFG\_FUNC)

[ 100](pinctrl-r7fa4m1xxxxxx_8h.md#a8ccbf47aa6d9480b3414ba9838542dd2)#define P104\_KR04 RA\_PINCFG\_\_48(1, 4, 0x08, RA\_PINCFG\_FUNC)

[ 101](pinctrl-r7fa4m1xxxxxx_8h.md#ae5dc99649ffba0c8bcf62c5cec1731c9)#define P104\_MISO0 RA\_PINCFG\_\_48(1, 4, 0x04, RA\_PINCFG\_FUNC)

[ 102](pinctrl-r7fa4m1xxxxxx_8h.md#aa3109b0f5d3d2bb925b67bb0bb16ab27)#define P104\_RXD0 RA\_PINCFG\_\_48(1, 4, 0x04, RA\_PINCFG\_FUNC)

[ 103](pinctrl-r7fa4m1xxxxxx_8h.md#aff83a33e15a60ee35235f18994585209)#define P104\_SCL0 RA\_PINCFG\_\_48(1, 4, 0x04, RA\_PINCFG\_FUNC)

[ 104](pinctrl-r7fa4m1xxxxxx_8h.md#a2a22193e5dd56e5e796a727fc7af9c46)#define P104\_SSLA1 RA\_PINCFG\_\_48(1, 4, 0x06, RA\_PINCFG\_FUNC)

[ 105](pinctrl-r7fa4m1xxxxxx_8h.md#ac82a91854f9ea8d1b538980c60826c89)#define P104\_TS13 RA\_PINCFG\_\_48(1, 4, 0x0C, RA\_PINCFG\_FUNC)

[ 106](pinctrl-r7fa4m1xxxxxx_8h.md#a3843d0b590838fa76c919657075dd1d4)#define P105\_COM1 RA\_PINCFG\_\_64(1, 5, 0x0D, RA\_PINCFG\_FUNC)

[ 107](pinctrl-r7fa4m1xxxxxx_8h.md#a49f9e218d30036370d461b47439c0fee)#define P105\_GTETRGA RA\_PINCFG\_\_64(1, 5, 0x02, RA\_PINCFG\_FUNC)

[ 108](pinctrl-r7fa4m1xxxxxx_8h.md#a91b63c7743d77a642d10a14d790b2aa1)#define P105\_GTIOC1A RA\_PINCFG\_\_64(1, 5, 0x03, RA\_PINCFG\_FUNC)

[ 109](pinctrl-r7fa4m1xxxxxx_8h.md#a87ea677896e3534427aabd94e47a22d4)#define P105\_KR05 RA\_PINCFG\_\_64(1, 5, 0x08, RA\_PINCFG\_FUNC)

[ 110](pinctrl-r7fa4m1xxxxxx_8h.md#ac17c2fa39379ccbceb95f9d580b72f33)#define P105\_SSLA2 RA\_PINCFG\_\_64(1, 5, 0x06, RA\_PINCFG\_FUNC)

[ 111](pinctrl-r7fa4m1xxxxxx_8h.md#ab95cbb630cf41da57ac5f47993e9ebe9)#define P105\_TS34 RA\_PINCFG\_\_64(1, 5, 0x0C, RA\_PINCFG\_FUNC)

[ 112](pinctrl-r7fa4m1xxxxxx_8h.md#a948c4ef25eec14023dfc7be8763b918a)#define P106\_COM2 RA\_PINCFG\_\_64(1, 6, 0x0D, RA\_PINCFG\_FUNC)

[ 113](pinctrl-r7fa4m1xxxxxx_8h.md#ab6c9213533bab95109f07193ee3d1d92)#define P106\_GTIOC0B RA\_PINCFG\_\_64(1, 6, 0x03, RA\_PINCFG\_FUNC)

[ 114](pinctrl-r7fa4m1xxxxxx_8h.md#a564ff7c53393cd4bd971bafa508e372f)#define P106\_KR06 RA\_PINCFG\_\_64(1, 6, 0x08, RA\_PINCFG\_FUNC)

[ 115](pinctrl-r7fa4m1xxxxxx_8h.md#a5e8e075dda7423592fd35c02c88a71d1)#define P106\_SSLA3 RA\_PINCFG\_\_64(1, 6, 0x06, RA\_PINCFG\_FUNC)

[ 116](pinctrl-r7fa4m1xxxxxx_8h.md#aa260950b7a3aaae71a4a703c0713ace7)#define P107\_COM3 RA\_PINCFG\_\_64(1, 7, 0x0D, RA\_PINCFG\_FUNC)

[ 117](pinctrl-r7fa4m1xxxxxx_8h.md#a8eaecc23342b8cd5dd03278661b1bfc3)#define P107\_GTIOC0A RA\_PINCFG\_\_64(1, 7, 0x03, RA\_PINCFG\_FUNC)

[ 118](pinctrl-r7fa4m1xxxxxx_8h.md#a5ef8c23746c27c8eff3867a58d39890d)#define P107\_KR07 RA\_PINCFG\_\_64(1, 7, 0x08, RA\_PINCFG\_FUNC)

[ 119](pinctrl-r7fa4m1xxxxxx_8h.md#a73c1ac806d0f991111cd157ee7c4b816)#define P108\_CTS9\_RTS9 RA\_PINCFG\_\_40(1, 8, 0x05, RA\_PINCFG\_FUNC)

[ 120](pinctrl-r7fa4m1xxxxxx_8h.md#a7ee96cd1b49970a121d65ef7a1978a0b)#define P108\_GTIOC0B RA\_PINCFG\_\_40(1, 8, 0x03, RA\_PINCFG\_FUNC)

[ 121](pinctrl-r7fa4m1xxxxxx_8h.md#ab4f944bcf8ae890a05a9a7c8706e9122)#define P108\_GTOULO RA\_PINCFG\_\_40(1, 8, 0x02, RA\_PINCFG\_FUNC)

[ 122](pinctrl-r7fa4m1xxxxxx_8h.md#a11f046fff549cdae54e93a6b9910f254)#define P108\_SS9 RA\_PINCFG\_\_40(1, 8, 0x05, RA\_PINCFG\_FUNC)

[ 123](pinctrl-r7fa4m1xxxxxx_8h.md#a07ec33c4fb07c07aae4bf26a28c788b8)#define P108\_SSLB0 RA\_PINCFG\_\_40(1, 8, 0x06, RA\_PINCFG\_FUNC)

[ 124](pinctrl-r7fa4m1xxxxxx_8h.md#a8ec7d6208f20322802006eca8163823b)#define P109\_CLKOUT RA\_PINCFG\_\_40(1, 9, 0x09, RA\_PINCFG\_FUNC)

[ 125](pinctrl-r7fa4m1xxxxxx_8h.md#a7f26451d8ec1d64f2be9e69b971495ec)#define P109\_CTX0 RA\_PINCFG\_\_40(1, 9, 0x10, RA\_PINCFG\_FUNC)

[ 126](pinctrl-r7fa4m1xxxxxx_8h.md#a5eb2e213d91303f832520f34f3b3ba00)#define P109\_GTIOC1A RA\_PINCFG\_\_40(1, 9, 0x03, RA\_PINCFG\_FUNC)

[ 127](pinctrl-r7fa4m1xxxxxx_8h.md#a2e2e2a2a702033f96801d3a599b4953a)#define P109\_GTOVUP RA\_PINCFG\_\_40(1, 9, 0x02, RA\_PINCFG\_FUNC)

[ 128](pinctrl-r7fa4m1xxxxxx_8h.md#a52912c0a2770ff4ef4217d26c1f66c5c)#define P109\_MOSI9 RA\_PINCFG\_\_40(1, 9, 0x05, RA\_PINCFG\_FUNC)

[ 129](pinctrl-r7fa4m1xxxxxx_8h.md#a4854e10d076fd5db550a447a4f231a99)#define P109\_MOSIB RA\_PINCFG\_\_40(1, 9, 0x06, RA\_PINCFG\_FUNC)

[ 130](pinctrl-r7fa4m1xxxxxx_8h.md#ac550fb929b2e9d437574dc2546f185ea)#define P109\_SCK1 RA\_PINCFG\_\_40(1, 9, 0x04, RA\_PINCFG\_FUNC)

[ 131](pinctrl-r7fa4m1xxxxxx_8h.md#ad2b92bd685d1708cc811eb1a995cbd51)#define P109\_SDA9 RA\_PINCFG\_\_40(1, 9, 0x05, RA\_PINCFG\_FUNC)

[ 132](pinctrl-r7fa4m1xxxxxx_8h.md#abc3e12f7510ec1ee2543603f46fdf213)#define P109\_SEG23 RA\_PINCFG\_\_40(1, 9, 0x0D, RA\_PINCFG\_FUNC)

[ 133](pinctrl-r7fa4m1xxxxxx_8h.md#a92c348fe1ce16156e6c7ff36297a67e7)#define P109\_TS10 RA\_PINCFG\_\_40(1, 9, 0x0C, RA\_PINCFG\_FUNC)

[ 134](pinctrl-r7fa4m1xxxxxx_8h.md#a001f4fd440dbd5d36ac5ed2dcebe7fde)#define P109\_TXD9 RA\_PINCFG\_\_40(1, 9, 0x05, RA\_PINCFG\_FUNC)

[ 135](pinctrl-r7fa4m1xxxxxx_8h.md#abf2fdc023066055cb905d8dc3563d40c)#define P110\_CRX0 RA\_PINCFG\_\_40(1, 10, 0x10, RA\_PINCFG\_FUNC)

[ 136](pinctrl-r7fa4m1xxxxxx_8h.md#a3e3383505a3b12860ca06169703158f7)#define P110\_CTS2\_RTS2 RA\_PINCFG\_\_40(1, 10, 0x04, RA\_PINCFG\_FUNC)

[ 137](pinctrl-r7fa4m1xxxxxx_8h.md#a2bef9ba6313458cfb12003adc6592cd7)#define P110\_GTIOC1B RA\_PINCFG\_\_40(1, 10, 0x03, RA\_PINCFG\_FUNC)

[ 138](pinctrl-r7fa4m1xxxxxx_8h.md#a3078ab83e111395aa36876da8ad6e0e5)#define P110\_GTOVLO RA\_PINCFG\_\_40(1, 10, 0x02, RA\_PINCFG\_FUNC)

[ 139](pinctrl-r7fa4m1xxxxxx_8h.md#a2267af6d5a9f5bb893d9f8cd5daff757)#define P110\_MISO9 RA\_PINCFG\_\_40(1, 10, 0x05, RA\_PINCFG\_FUNC)

[ 140](pinctrl-r7fa4m1xxxxxx_8h.md#a568fd6977af52e17440fd38a8d8c171b)#define P110\_MISOB RA\_PINCFG\_\_40(1, 10, 0x06, RA\_PINCFG\_FUNC)

[ 141](pinctrl-r7fa4m1xxxxxx_8h.md#a09f91d821b02601934b4290832c0484f)#define P110\_RXD9 RA\_PINCFG\_\_40(1, 10, 0x05, RA\_PINCFG\_FUNC)

[ 142](pinctrl-r7fa4m1xxxxxx_8h.md#a2ae1812796072fa8fc37efc9463fbef1)#define P110\_SCL9 RA\_PINCFG\_\_40(1, 10, 0x05, RA\_PINCFG\_FUNC)

[ 143](pinctrl-r7fa4m1xxxxxx_8h.md#af3635aa02046ba92ca63ba4ac7300e27)#define P110\_SEG24 RA\_PINCFG\_\_40(1, 10, 0x0D, RA\_PINCFG\_FUNC)

[ 144](pinctrl-r7fa4m1xxxxxx_8h.md#a5a1bd21be400f8a6e6a22ff434a27f54)#define P110\_SS2 RA\_PINCFG\_\_40(1, 10, 0x04, RA\_PINCFG\_FUNC)

[ 145](pinctrl-r7fa4m1xxxxxx_8h.md#ad0c1b10031e9cd8dbb7a9a0380deb4ef)#define P110\_VCOUT RA\_PINCFG\_\_40(1, 10, 0x09, RA\_PINCFG\_FUNC)

[ 146](pinctrl-r7fa4m1xxxxxx_8h.md#a0a0745ad798bcead993f78c5e08158b5)#define P111\_CAPH RA\_PINCFG\_\_40(1, 11, 0x0D, RA\_PINCFG\_FUNC)

[ 147](pinctrl-r7fa4m1xxxxxx_8h.md#aff935e40d761b19933f590599cb5faaf)#define P111\_GTIOC3A RA\_PINCFG\_\_40(1, 11, 0x03, RA\_PINCFG\_FUNC)

[ 148](pinctrl-r7fa4m1xxxxxx_8h.md#a0aff0e56d122c9718dfd91c7b77d81ee)#define P111\_RSPCKB RA\_PINCFG\_\_40(1, 11, 0x06, RA\_PINCFG\_FUNC)

[ 149](pinctrl-r7fa4m1xxxxxx_8h.md#a6db0ff657c4d3e6e77a646fe844eff21)#define P111\_SCK2 RA\_PINCFG\_\_40(1, 11, 0x04, RA\_PINCFG\_FUNC)

[ 150](pinctrl-r7fa4m1xxxxxx_8h.md#ada3d49a2fcafa558712f437982e3f84d)#define P111\_SCK9 RA\_PINCFG\_\_40(1, 11, 0x05, RA\_PINCFG\_FUNC)

[ 151](pinctrl-r7fa4m1xxxxxx_8h.md#abd29420547d2145ff8c1ed56e6c8acbc)#define P111\_TS12 RA\_PINCFG\_\_40(1, 11, 0x0C, RA\_PINCFG\_FUNC)

[ 152](pinctrl-r7fa4m1xxxxxx_8h.md#a16522d212ed9bb30ae55b714ed5829bd)#define P112\_CAPL RA\_PINCFG\_\_40(1, 12, 0x0D, RA\_PINCFG\_FUNC)

[ 153](pinctrl-r7fa4m1xxxxxx_8h.md#afa200ad96c21bdda44a214df90f04e82)#define P112\_GTIOC3B RA\_PINCFG\_\_40(1, 12, 0x03, RA\_PINCFG\_FUNC)

[ 154](pinctrl-r7fa4m1xxxxxx_8h.md#a3f1c631f4af1db2f31ac84c1b0202781)#define P112\_MOSI2 RA\_PINCFG\_\_40(1, 12, 0x04, RA\_PINCFG\_FUNC)

[ 155](pinctrl-r7fa4m1xxxxxx_8h.md#a01503183824ba91c269c904e2aa1aa8e)#define P112\_SCK1 RA\_PINCFG\_\_40(1, 12, 0x05, RA\_PINCFG\_FUNC)

[ 156](pinctrl-r7fa4m1xxxxxx_8h.md#a12e2ca08c37f3b6958d0479aa7ab7b7c)#define P112\_SDA2 RA\_PINCFG\_\_40(1, 12, 0x04, RA\_PINCFG\_FUNC)

[ 157](pinctrl-r7fa4m1xxxxxx_8h.md#aa668e08603ad7b09b162be50ada659b3)#define P112\_SSIBCK0 RA\_PINCFG\_\_40(1, 12, 0x12, RA\_PINCFG\_FUNC)

[ 158](pinctrl-r7fa4m1xxxxxx_8h.md#a52ff7cfb4a5c23383aa10da476691833)#define P112\_SSLB0 RA\_PINCFG\_\_40(1, 12, 0x06, RA\_PINCFG\_FUNC)

[ 159](pinctrl-r7fa4m1xxxxxx_8h.md#a753be221dbaee64578a3ff0d509fd625)#define P112\_TSCAP RA\_PINCFG\_\_40(1, 12, 0x0C, RA\_PINCFG\_FUNC)

[ 160](pinctrl-r7fa4m1xxxxxx_8h.md#adf8e8eabb3c03610e858c971b6c05ba0)#define P112\_TXD2 RA\_PINCFG\_\_40(1, 12, 0x04, RA\_PINCFG\_FUNC)

[ 161](pinctrl-r7fa4m1xxxxxx_8h.md#acac27f2a0edd8c3aed74021b8e0d859b)#define P113\_GTIOC2A RA\_PINCFG\_\_64(1, 13, 0x03, RA\_PINCFG\_FUNC)

[ 162](pinctrl-r7fa4m1xxxxxx_8h.md#a496b7bd8cb8133ab41d6c694fc6d9ddd)#define P113\_SEG00COM4 RA\_PINCFG\_\_64(1, 13, 0x0D, RA\_PINCFG\_FUNC)

[ 163](pinctrl-r7fa4m1xxxxxx_8h.md#aed631b24d782339a411828bbff21a7b9)#define P113\_SSIFS0 RA\_PINCFG\_\_64(1, 13, 0x12, RA\_PINCFG\_FUNC)

[ 164](pinctrl-r7fa4m1xxxxxx_8h.md#a9e0808474ca09b3ceb9c9cfba7ea1d06)#define P113\_SSILRCK0 RA\_PINCFG\_\_64(1, 13, 0x12, RA\_PINCFG\_FUNC)

[ 165](pinctrl-r7fa4m1xxxxxx_8h.md#a49a1372b2de2f1ffe1a90e08f284c63e)#define P113\_TS27 RA\_PINCFG\_\_64(1, 13, 0x0C, RA\_PINCFG\_FUNC)

[ 166](pinctrl-r7fa4m1xxxxxx_8h.md#a9057e3badd621eab1b1a2dcca1e9e415)#define P114\_GTIOC2B RA\_PINCFG\_100(1, 14, 0x03, RA\_PINCFG\_FUNC)

[ 167](pinctrl-r7fa4m1xxxxxx_8h.md#a85c1f2f8e8cdaa6eb3d060bd0aa31c6a)#define P114\_SEG25 RA\_PINCFG\_100(1, 14, 0x0D, RA\_PINCFG\_FUNC)

[ 168](pinctrl-r7fa4m1xxxxxx_8h.md#ad97f87452808f4790d76aa2b3d707f84)#define P114\_SSIRXD0 RA\_PINCFG\_100(1, 14, 0x12, RA\_PINCFG\_FUNC)

[ 169](pinctrl-r7fa4m1xxxxxx_8h.md#a7429be994e04e46ca246ecb34a26da0a)#define P114\_TS29 RA\_PINCFG\_100(1, 14, 0x0C, RA\_PINCFG\_FUNC)

[ 170](pinctrl-r7fa4m1xxxxxx_8h.md#a0c8bd394991f13adab4da12ae9f1f3ed)#define P115\_GTIOC4A RA\_PINCFG\_100(1, 15, 0x03, RA\_PINCFG\_FUNC)

[ 171](pinctrl-r7fa4m1xxxxxx_8h.md#ab14094539a2be9d3f6929fb22781901a)#define P115\_SEG26 RA\_PINCFG\_100(1, 15, 0x0D, RA\_PINCFG\_FUNC)

[ 172](pinctrl-r7fa4m1xxxxxx_8h.md#a87c830c32bb7647fbf9202390b27714c)#define P115\_SSITXD0 RA\_PINCFG\_100(1, 15, 0x12, RA\_PINCFG\_FUNC)

[ 173](pinctrl-r7fa4m1xxxxxx_8h.md#a7b23c487b76221fc25d625043dc0ac5e)#define P115\_TS35 RA\_PINCFG\_100(1, 15, 0x0C, RA\_PINCFG\_FUNC)

[ 174](pinctrl-r7fa4m1xxxxxx_8h.md#ac8ca955053c3ed2a46b39444717d38b0)#define P202\_GTIOC5B RA\_PINCFG\_100(2, 2, 0x03, RA\_PINCFG\_FUNC)

[ 175](pinctrl-r7fa4m1xxxxxx_8h.md#a323d352fc7710fa970c62d453306d6e5)#define P202\_MISO9 RA\_PINCFG\_100(2, 2, 0x05, RA\_PINCFG\_FUNC)

[ 176](pinctrl-r7fa4m1xxxxxx_8h.md#ad1fe4e1d90f2f9ec4aa46b5f8d6186fd)#define P202\_MISOB RA\_PINCFG\_100(2, 2, 0x06, RA\_PINCFG\_FUNC)

[ 177](pinctrl-r7fa4m1xxxxxx_8h.md#a156853c0d0245291daad489b6ab4dfb8)#define P202\_RXD9 RA\_PINCFG\_100(2, 2, 0x05, RA\_PINCFG\_FUNC)

[ 178](pinctrl-r7fa4m1xxxxxx_8h.md#a5040ddb36e6dbc1865a54e1cc0c7885c)#define P202\_SCK2 RA\_PINCFG\_100(2, 2, 0x04, RA\_PINCFG\_FUNC)

[ 179](pinctrl-r7fa4m1xxxxxx_8h.md#a0864e737a7705b42383384101a25d24f)#define P202\_SCL9 RA\_PINCFG\_100(2, 2, 0x05, RA\_PINCFG\_FUNC)

[ 180](pinctrl-r7fa4m1xxxxxx_8h.md#a95283422448e4833f0b0444544b742a4)#define P202\_SEG16 RA\_PINCFG\_100(2, 2, 0x0D, RA\_PINCFG\_FUNC)

[ 181](pinctrl-r7fa4m1xxxxxx_8h.md#a48b915f23147cf9575bde1f0e6ebe06b)#define P203\_CTS2\_RTS2 RA\_PINCFG\_100(2, 3, 0x04, RA\_PINCFG\_FUNC)

[ 182](pinctrl-r7fa4m1xxxxxx_8h.md#a8da968343b323618dfecfac4737d8458)#define P203\_GTIOC5A RA\_PINCFG\_100(2, 3, 0x03, RA\_PINCFG\_FUNC)

[ 183](pinctrl-r7fa4m1xxxxxx_8h.md#a3d0eef21b1db881c7ef59d427c46c17e)#define P203\_MOSI9 RA\_PINCFG\_100(2, 3, 0x05, RA\_PINCFG\_FUNC)

[ 184](pinctrl-r7fa4m1xxxxxx_8h.md#a0bd8cb5760e5b0635cffd2ce2f32c9bb)#define P203\_MOSIB RA\_PINCFG\_100(2, 3, 0x06, RA\_PINCFG\_FUNC)

[ 185](pinctrl-r7fa4m1xxxxxx_8h.md#a3136ada9c3319677a33ac4223b037cde)#define P203\_SDA9 RA\_PINCFG\_100(2, 3, 0x05, RA\_PINCFG\_FUNC)

[ 186](pinctrl-r7fa4m1xxxxxx_8h.md#a05178432d664ff711580fff9fcd8e227)#define P203\_SEG15 RA\_PINCFG\_100(2, 3, 0x0D, RA\_PINCFG\_FUNC)

[ 187](pinctrl-r7fa4m1xxxxxx_8h.md#a45c9969485396914e4a6da94d35ee30c)#define P203\_SS2 RA\_PINCFG\_100(2, 3, 0x04, RA\_PINCFG\_FUNC)

[ 188](pinctrl-r7fa4m1xxxxxx_8h.md#a48d50f0f267edf38a533692d6e02f22c)#define P203\_TSCAP RA\_PINCFG\_100(2, 3, 0x0C, RA\_PINCFG\_FUNC)

[ 189](pinctrl-r7fa4m1xxxxxx_8h.md#acd1e96f92d5aff4a3bef784957a018d2)#define P203\_TXD9 RA\_PINCFG\_100(2, 3, 0x05, RA\_PINCFG\_FUNC)

[ 190](pinctrl-r7fa4m1xxxxxx_8h.md#adc10122b6a80f6670e1f5abbc0cf7965)#define P204\_AGTIO1 RA\_PINCFG\_\_64(2, 4, 0x01, RA\_PINCFG\_FUNC)

[ 191](pinctrl-r7fa4m1xxxxxx_8h.md#a5d8f210ec64db4984c878b07b06546b4)#define P204\_CACREF RA\_PINCFG\_\_64(2, 4, 0x0A, RA\_PINCFG\_FUNC)

[ 192](pinctrl-r7fa4m1xxxxxx_8h.md#a38dfe80adb0645a0c9da24ecf5d4e356)#define P204\_GTIOC4B RA\_PINCFG\_\_64(2, 4, 0x03, RA\_PINCFG\_FUNC)

[ 193](pinctrl-r7fa4m1xxxxxx_8h.md#a45d96dbc9af24b4764271625dc506b91)#define P204\_GTIW RA\_PINCFG\_\_64(2, 4, 0x02, RA\_PINCFG\_FUNC)

[ 194](pinctrl-r7fa4m1xxxxxx_8h.md#a7658b44af26cd72d0ce675a76855db6a)#define P204\_RSPCKB RA\_PINCFG\_\_64(2, 4, 0x06, RA\_PINCFG\_FUNC)

[ 195](pinctrl-r7fa4m1xxxxxx_8h.md#ad296377b534435e9f1a22a78c11c40d4)#define P204\_SCK0 RA\_PINCFG\_\_64(2, 4, 0x04, RA\_PINCFG\_FUNC)

[ 196](pinctrl-r7fa4m1xxxxxx_8h.md#a6967c5430df6baf39e89caf438045b69)#define P204\_SCK9 RA\_PINCFG\_\_64(2, 4, 0x05, RA\_PINCFG\_FUNC)

[ 197](pinctrl-r7fa4m1xxxxxx_8h.md#a0c2081007b6c3f56472b41ce38ec8dea)#define P204\_SCL0 RA\_PINCFG\_\_64(2, 4, 0x07, RA\_PINCFG\_FUNC)

[ 198](pinctrl-r7fa4m1xxxxxx_8h.md#aac818dcdd0f1cddd20d04382d95e01e2)#define P204\_SEG14 RA\_PINCFG\_\_64(2, 4, 0x0D, RA\_PINCFG\_FUNC)

[ 199](pinctrl-r7fa4m1xxxxxx_8h.md#a3f4673689383087cd5840a13d2cffe62)#define P204\_TS00 RA\_PINCFG\_\_64(2, 4, 0x0C, RA\_PINCFG\_FUNC)

[ 200](pinctrl-r7fa4m1xxxxxx_8h.md#ade35e16f6c2cd5d576a39cc706346711)#define P204\_USB\_OVRCUR\_B RA\_PINCFG\_\_64(2, 4, 0x13, RA\_PINCFG\_FUNC)

[ 201](pinctrl-r7fa4m1xxxxxx_8h.md#a0f21b21e3ef41ce9c54514e26ca600c5)#define P205\_AGTO1 RA\_PINCFG\_\_64(2, 5, 0x01, RA\_PINCFG\_FUNC)

[ 202](pinctrl-r7fa4m1xxxxxx_8h.md#a8cd7d327a74f362f6efffa32be0a6198)#define P205\_CLKOUT RA\_PINCFG\_\_64(2, 5, 0x09, RA\_PINCFG\_FUNC)

[ 203](pinctrl-r7fa4m1xxxxxx_8h.md#a5b8a894c12cf6d2eafbeb82346ee1406)#define P205\_CTS9\_RTS9 RA\_PINCFG\_\_64(2, 5, 0x05, RA\_PINCFG\_FUNC)

[ 204](pinctrl-r7fa4m1xxxxxx_8h.md#ac630b5f5945d52b566a921b03ee42ef2)#define P205\_GTIOC4A RA\_PINCFG\_\_64(2, 5, 0x03, RA\_PINCFG\_FUNC)

[ 205](pinctrl-r7fa4m1xxxxxx_8h.md#ae8671f134f88df892efcbb20748e60e6)#define P205\_GTIV RA\_PINCFG\_\_64(2, 5, 0x02, RA\_PINCFG\_FUNC)

[ 206](pinctrl-r7fa4m1xxxxxx_8h.md#a86161280c86fb93d3a272b0cb0ee18cc)#define P205\_MOSI0 RA\_PINCFG\_\_64(2, 5, 0x04, RA\_PINCFG\_FUNC)

[ 207](pinctrl-r7fa4m1xxxxxx_8h.md#a2733ecc933ba7a9b1656262e8cec997c)#define P205\_SCL1 RA\_PINCFG\_\_64(2, 5, 0x07, RA\_PINCFG\_FUNC)

[ 208](pinctrl-r7fa4m1xxxxxx_8h.md#a52e64cca5934f95a7c2bcf74d7bb7ef1)#define P205\_SDA0 RA\_PINCFG\_\_64(2, 5, 0x04, RA\_PINCFG\_FUNC)

[ 209](pinctrl-r7fa4m1xxxxxx_8h.md#afc170d90be83ffb955e034609992f15f)#define P205\_SEG13 RA\_PINCFG\_\_64(2, 5, 0x0D, RA\_PINCFG\_FUNC)

[ 210](pinctrl-r7fa4m1xxxxxx_8h.md#af7b0e023a79829a9542e5a1f19de16d0)#define P205\_SS9 RA\_PINCFG\_\_64(2, 5, 0x05, RA\_PINCFG\_FUNC)

[ 211](pinctrl-r7fa4m1xxxxxx_8h.md#a83109a5e9c6eded011b4e843f3b754bd)#define P205\_SSLB0 RA\_PINCFG\_\_64(2, 5, 0x06, RA\_PINCFG\_FUNC)

[ 212](pinctrl-r7fa4m1xxxxxx_8h.md#ab7d23a046bc75c9f433d1f07da40d830)#define P205\_TSCAP RA\_PINCFG\_\_64(2, 5, 0x0C, RA\_PINCFG\_FUNC)

[ 213](pinctrl-r7fa4m1xxxxxx_8h.md#a173cce49768744c274b26711b1ac46a0)#define P205\_TXD0 RA\_PINCFG\_\_64(2, 5, 0x04, RA\_PINCFG\_FUNC)

[ 214](pinctrl-r7fa4m1xxxxxx_8h.md#a8c089408bf58e185c1d6c15f794fd41f)#define P205\_USB\_OVRCUR\_A RA\_PINCFG\_\_64(2, 5, 0x13, RA\_PINCFG\_FUNC)

[ 215](pinctrl-r7fa4m1xxxxxx_8h.md#a182e75fabf2d53280db4fa6f1f3a2bd9)#define P206\_GTIU RA\_PINCFG\_\_48(2, 6, 0x02, RA\_PINCFG\_FUNC)

[ 216](pinctrl-r7fa4m1xxxxxx_8h.md#aa85b86dde59b2a4f214f3e1a730bd192)#define P206\_MISO0 RA\_PINCFG\_\_48(2, 6, 0x04, RA\_PINCFG\_FUNC)

[ 217](pinctrl-r7fa4m1xxxxxx_8h.md#a370cc831042de4b89105a289bf05c855)#define P206\_RXD0 RA\_PINCFG\_\_48(2, 6, 0x04, RA\_PINCFG\_FUNC)

[ 218](pinctrl-r7fa4m1xxxxxx_8h.md#aed03afc1543fc61540a8e4bbbae9b92b)#define P206\_SCL0 RA\_PINCFG\_\_48(2, 6, 0x04, RA\_PINCFG\_FUNC)

[ 219](pinctrl-r7fa4m1xxxxxx_8h.md#a741f7ef470c8d6698aa7a6e0cf43f617)#define P206\_SDA1 RA\_PINCFG\_\_48(2, 6, 0x07, RA\_PINCFG\_FUNC)

[ 220](pinctrl-r7fa4m1xxxxxx_8h.md#aa56747db3c2a26933521e3bab1552b2d)#define P206\_SEG12 RA\_PINCFG\_\_48(2, 6, 0x0D, RA\_PINCFG\_FUNC)

[ 221](pinctrl-r7fa4m1xxxxxx_8h.md#a338a2984cfef454f9a9fab0bc48559f6)#define P206\_SSLB1 RA\_PINCFG\_\_48(2, 6, 0x06, RA\_PINCFG\_FUNC)

[ 222](pinctrl-r7fa4m1xxxxxx_8h.md#aa8c4508e57e4fad7368e4cd9bc62a16d)#define P206\_TS01 RA\_PINCFG\_\_48(2, 6, 0x0C, RA\_PINCFG\_FUNC)

[ 223](pinctrl-r7fa4m1xxxxxx_8h.md#acee3062a8c9ff9358fea39c914fd34e0)#define P206\_USB\_VBUSEN RA\_PINCFG\_\_48(2, 6, 0x13, RA\_PINCFG\_FUNC)

[ 224](pinctrl-r7fa4m1xxxxxx_8h.md#a4750d4456be36a7794e4c524bfa7aa2f)#define P212\_AGTEE1 RA\_PINCFG\_\_40(2, 12, 0x01, RA\_PINCFG\_FUNC)

[ 225](pinctrl-r7fa4m1xxxxxx_8h.md#a57b8f01893c9a9f9b408d6f19f2c77d8)#define P212\_GTETRGB RA\_PINCFG\_\_40(2, 12, 0x02, RA\_PINCFG\_FUNC)

[ 226](pinctrl-r7fa4m1xxxxxx_8h.md#ae397e248c9a50a275d4063e2a8ab4d17)#define P212\_GTIOC0B RA\_PINCFG\_\_40(2, 12, 0x03, RA\_PINCFG\_FUNC)

[ 227](pinctrl-r7fa4m1xxxxxx_8h.md#a6e34bc0eeddad84be88880baecaccb0b)#define P212\_MISO1 RA\_PINCFG\_\_40(2, 12, 0x05, RA\_PINCFG\_FUNC)

[ 228](pinctrl-r7fa4m1xxxxxx_8h.md#a8b5364bc01c12fee61327e7ec1b747bd)#define P212\_RXD1 RA\_PINCFG\_\_40(2, 12, 0x05, RA\_PINCFG\_FUNC)

[ 229](pinctrl-r7fa4m1xxxxxx_8h.md#ae16ce372226a39d1e7b63c0e267f52c4)#define P212\_SCL1 RA\_PINCFG\_\_40(2, 12, 0x05, RA\_PINCFG\_FUNC)

[ 230](pinctrl-r7fa4m1xxxxxx_8h.md#a977e52a123e1ed8d85e05de853d9ab57)#define P213\_GTETRGA RA\_PINCFG\_\_40(2, 13, 0x02, RA\_PINCFG\_FUNC)

[ 231](pinctrl-r7fa4m1xxxxxx_8h.md#aaea40cf234d3bd1c3e3039f854ab963a)#define P213\_GTIOC0A RA\_PINCFG\_\_40(2, 13, 0x03, RA\_PINCFG\_FUNC)

[ 232](pinctrl-r7fa4m1xxxxxx_8h.md#a522e3739147096185cb8a6b97ec87f04)#define P213\_MOSI1 RA\_PINCFG\_\_40(2, 13, 0x05, RA\_PINCFG\_FUNC)

[ 233](pinctrl-r7fa4m1xxxxxx_8h.md#a404cb6f3725c8c3c8ad5b9dcda30ee30)#define P213\_SDA1 RA\_PINCFG\_\_40(2, 13, 0x05, RA\_PINCFG\_FUNC)

[ 234](pinctrl-r7fa4m1xxxxxx_8h.md#a5a38f503de4b728cc6268a9fa61aec37)#define P213\_TXD1 RA\_PINCFG\_\_40(2, 13, 0x05, RA\_PINCFG\_FUNC)

[ 235](pinctrl-r7fa4m1xxxxxx_8h.md#a2df846006b076ff48f30cfd891d200f8)#define P300\_GTIOC0A RA\_PINCFG\_\_40(3, 0, 0x03, RA\_PINCFG\_FUNC)

[ 236](pinctrl-r7fa4m1xxxxxx_8h.md#a30637696fe7bdba7f00f2c6d73ea395c)#define P300\_GTOUUP RA\_PINCFG\_\_40(3, 0, 0x02, RA\_PINCFG\_FUNC)

[ 237](pinctrl-r7fa4m1xxxxxx_8h.md#a97382eb2fb8f15cca65eafdde203efe5)#define P300\_SSLB1 RA\_PINCFG\_\_40(3, 0, 0x06, RA\_PINCFG\_FUNC)

[ 238](pinctrl-r7fa4m1xxxxxx_8h.md#ad694b5a30d9c86c4d3e6cd89a301b522)#define P301\_AGTIO0 RA\_PINCFG\_\_40(3, 1, 0x01, RA\_PINCFG\_FUNC)

[ 239](pinctrl-r7fa4m1xxxxxx_8h.md#a7cd3d35fa5eeb00034b3d6fc4dcec76f)#define P301\_COM5 RA\_PINCFG\_\_40(3, 1, 0x10, RA\_PINCFG\_FUNC)

[ 240](pinctrl-r7fa4m1xxxxxx_8h.md#a29fb940c5a40b304091835c105491556)#define P301\_CTS9\_RTS9 RA\_PINCFG\_\_40(3, 1, 0x05, RA\_PINCFG\_FUNC)

[ 241](pinctrl-r7fa4m1xxxxxx_8h.md#aae53e4c38ec26f07cd06eab7ee588c37)#define P301\_GTIOC4B RA\_PINCFG\_\_40(3, 1, 0x03, RA\_PINCFG\_FUNC)

[ 242](pinctrl-r7fa4m1xxxxxx_8h.md#a0c2dc0582d5cf4df586aac49c3d545cc)#define P301\_GTOULO RA\_PINCFG\_\_40(3, 1, 0x02, RA\_PINCFG\_FUNC)

[ 243](pinctrl-r7fa4m1xxxxxx_8h.md#a95249a960c73fb44efd630577b0199c9)#define P301\_MISO2 RA\_PINCFG\_\_40(3, 1, 0x04, RA\_PINCFG\_FUNC)

[ 244](pinctrl-r7fa4m1xxxxxx_8h.md#a0d71cac2e43ad2d7a81e648f188e784c)#define P301\_RXD2 RA\_PINCFG\_\_40(3, 1, 0x04, RA\_PINCFG\_FUNC)

[ 245](pinctrl-r7fa4m1xxxxxx_8h.md#a29ca5e7dd080b135509be73fbb86937f)#define P301\_SCL2 RA\_PINCFG\_\_40(3, 1, 0x04, RA\_PINCFG\_FUNC)

[ 246](pinctrl-r7fa4m1xxxxxx_8h.md#a9e4a5f3c32090e0680f3c778e95b0ab1)#define P301\_SEG01 RA\_PINCFG\_\_40(3, 1, 0x0D, RA\_PINCFG\_FUNC)

[ 247](pinctrl-r7fa4m1xxxxxx_8h.md#a7ef0bd7daa07e64cd7444a0d44917c99)#define P301\_SS9 RA\_PINCFG\_\_40(3, 1, 0x05, RA\_PINCFG\_FUNC)

[ 248](pinctrl-r7fa4m1xxxxxx_8h.md#aba9258c35b04386807763ba5223d1d06)#define P301\_SSLB2 RA\_PINCFG\_\_40(3, 1, 0x06, RA\_PINCFG\_FUNC)

[ 249](pinctrl-r7fa4m1xxxxxx_8h.md#ab4f0b5b8bcc080ec5385fe50224bf984)#define P301\_TS09 RA\_PINCFG\_\_40(3, 1, 0x0C, RA\_PINCFG\_FUNC)

[ 250](pinctrl-r7fa4m1xxxxxx_8h.md#ac3f1f3aa722c26ebef272fb700a660aa)#define P302\_COM6 RA\_PINCFG\_\_48(3, 2, 0x10, RA\_PINCFG\_FUNC)

[ 251](pinctrl-r7fa4m1xxxxxx_8h.md#ad36fe4d4e74b417ad9dfcd206d3c4549)#define P302\_GTIOC4A RA\_PINCFG\_\_48(3, 2, 0x03, RA\_PINCFG\_FUNC)

[ 252](pinctrl-r7fa4m1xxxxxx_8h.md#aa2d2b651d7cd2a6e8a73229a60b285ab)#define P302\_GTOUUP RA\_PINCFG\_\_48(3, 2, 0x02, RA\_PINCFG\_FUNC)

[ 253](pinctrl-r7fa4m1xxxxxx_8h.md#aadde72635780dcb12c4b4b09eb7bdf52)#define P302\_MOSI2 RA\_PINCFG\_\_48(3, 2, 0x04, RA\_PINCFG\_FUNC)

[ 254](pinctrl-r7fa4m1xxxxxx_8h.md#a352d96c3ad3c70151b2c0346203d5201)#define P302\_SDA2 RA\_PINCFG\_\_48(3, 2, 0x04, RA\_PINCFG\_FUNC)

[ 255](pinctrl-r7fa4m1xxxxxx_8h.md#a1f8f670ffa4a9f62191532371baf390c)#define P302\_SEG02 RA\_PINCFG\_\_48(3, 2, 0x0D, RA\_PINCFG\_FUNC)

[ 256](pinctrl-r7fa4m1xxxxxx_8h.md#a575671020751944bb06260a942723af7)#define P302\_SSLB3 RA\_PINCFG\_\_48(3, 2, 0x06, RA\_PINCFG\_FUNC)

[ 257](pinctrl-r7fa4m1xxxxxx_8h.md#a5160bfb71e0bc256a74241a5dd9b8774)#define P302\_TS08 RA\_PINCFG\_\_48(3, 2, 0x0C, RA\_PINCFG\_FUNC)

[ 258](pinctrl-r7fa4m1xxxxxx_8h.md#a9c9698a245f492fe2904d4cf65167688)#define P302\_TXD2 RA\_PINCFG\_\_48(3, 2, 0x04, RA\_PINCFG\_FUNC)

[ 259](pinctrl-r7fa4m1xxxxxx_8h.md#a979b08c7836051797937b93f4343629c)#define P303\_COM7 RA\_PINCFG\_\_64(3, 3, 0x10, RA\_PINCFG\_FUNC)

[ 260](pinctrl-r7fa4m1xxxxxx_8h.md#a46a914491d0cd8f5bae4878c60106b01)#define P303\_GTIOC7B RA\_PINCFG\_\_64(3, 3, 0x03, RA\_PINCFG\_FUNC)

[ 261](pinctrl-r7fa4m1xxxxxx_8h.md#ad41ecf30ea1c484a54249f54a89b3ed7)#define P303\_SEG03 RA\_PINCFG\_\_64(3, 3, 0x0D, RA\_PINCFG\_FUNC)

[ 262](pinctrl-r7fa4m1xxxxxx_8h.md#a70315bdead8e1f342c2c7fc39013a703)#define P303\_TS02 RA\_PINCFG\_\_64(3, 3, 0x0C, RA\_PINCFG\_FUNC)

[ 263](pinctrl-r7fa4m1xxxxxx_8h.md#abc9cc64d66caafe9def796f3aa6b0c9b)#define P304\_GTIOC7A RA\_PINCFG\_\_64(3, 4, 0x03, RA\_PINCFG\_FUNC)

[ 264](pinctrl-r7fa4m1xxxxxx_8h.md#ad95b03c95fc8344c8e49ea12c6510196)#define P304\_SEG20 RA\_PINCFG\_\_64(3, 4, 0x0D, RA\_PINCFG\_FUNC)

[ 265](pinctrl-r7fa4m1xxxxxx_8h.md#acfd211379c03e1c2c9ac842d349a019a)#define P304\_TS11 RA\_PINCFG\_\_64(3, 4, 0x0C, RA\_PINCFG\_FUNC)

[ 266](pinctrl-r7fa4m1xxxxxx_8h.md#a9f02cc6e14415cb6d876401bef7384b5)#define P305\_SEG19 RA\_PINCFG\_100(3, 5, 0x0D, RA\_PINCFG\_FUNC)

[ 267](pinctrl-r7fa4m1xxxxxx_8h.md#a57f5e775bfb533510277007b1e273eaf)#define P306\_SEG18 RA\_PINCFG\_100(3, 6, 0x0D, RA\_PINCFG\_FUNC)

[ 268](pinctrl-r7fa4m1xxxxxx_8h.md#a0984d7a787bc632d61bd075cedae58cd)#define P307\_SEG17 RA\_PINCFG\_100(3, 7, 0x0D, RA\_PINCFG\_FUNC)

[ 269](pinctrl-r7fa4m1xxxxxx_8h.md#a258e3e2e0616c62a3236eb30ef5211f0)#define P400\_AGTIO1 RA\_PINCFG\_\_48(4, 0, 0x01, RA\_PINCFG\_FUNC)

[ 270](pinctrl-r7fa4m1xxxxxx_8h.md#abb17d01cb4b4db90852107a400df8400)#define P400\_AUDIO\_CLK RA\_PINCFG\_\_48(4, 0, 0x12, RA\_PINCFG\_FUNC)

[ 271](pinctrl-r7fa4m1xxxxxx_8h.md#a0db0477937f79e65d17b0108b5f1581e)#define P400\_CACREF RA\_PINCFG\_\_48(4, 0, 0x0A, RA\_PINCFG\_FUNC)

[ 272](pinctrl-r7fa4m1xxxxxx_8h.md#a5e47e661c6eebf03dacbe2265d62314a)#define P400\_GTIOC6A RA\_PINCFG\_\_48(4, 0, 0x04, RA\_PINCFG\_FUNC)

[ 273](pinctrl-r7fa4m1xxxxxx_8h.md#a04f67dd552486b81a5dc9bc971c8e410)#define P400\_SCK0 RA\_PINCFG\_\_48(4, 0, 0x04, RA\_PINCFG\_FUNC)

[ 274](pinctrl-r7fa4m1xxxxxx_8h.md#a73fe11226a0acf08dd00b5090bada05e)#define P400\_SCK1 RA\_PINCFG\_\_48(4, 0, 0x05, RA\_PINCFG\_FUNC)

[ 275](pinctrl-r7fa4m1xxxxxx_8h.md#a5717d0b294ac30b6ec521057eb371648)#define P400\_SCL0 RA\_PINCFG\_\_48(4, 0, 0x07, RA\_PINCFG\_FUNC)

[ 276](pinctrl-r7fa4m1xxxxxx_8h.md#ae6c239cd93bda76452d0e8496eff48e5)#define P400\_SEG04 RA\_PINCFG\_\_48(4, 0, 0x0D, RA\_PINCFG\_FUNC)

[ 277](pinctrl-r7fa4m1xxxxxx_8h.md#a2a0f195797e1066d70453e7c21844c92)#define P400\_TS20 RA\_PINCFG\_\_48(4, 0, 0x0C, RA\_PINCFG\_FUNC)

[ 278](pinctrl-r7fa4m1xxxxxx_8h.md#ab835306ba5818c254d833e61d32369e6)#define P401\_CTS0\_RTS0 RA\_PINCFG\_\_64(4, 1, 0x04, RA\_PINCFG\_FUNC)

[ 279](pinctrl-r7fa4m1xxxxxx_8h.md#a9da7a6876b32a890728075af53ea9621)#define P401\_CTX0 RA\_PINCFG\_\_64(4, 1, 0x10, RA\_PINCFG\_FUNC)

[ 280](pinctrl-r7fa4m1xxxxxx_8h.md#ae6eaab35edb04358836bc1796535606e)#define P401\_GTETRGA RA\_PINCFG\_\_64(4, 1, 0x03, RA\_PINCFG\_FUNC)

[ 281](pinctrl-r7fa4m1xxxxxx_8h.md#ab7c3b8d1926e862ac915999b684af1bb)#define P401\_GTIOC6B RA\_PINCFG\_\_64(4, 1, 0x04, RA\_PINCFG\_FUNC)

[ 282](pinctrl-r7fa4m1xxxxxx_8h.md#afe1783298cfb2f12212a8e1db962bfc7)#define P401\_MOSI1 RA\_PINCFG\_\_64(4, 1, 0x05, RA\_PINCFG\_FUNC)

[ 283](pinctrl-r7fa4m1xxxxxx_8h.md#ad67dc52411eafe49e7b19e779da51e80)#define P401\_SDA0 RA\_PINCFG\_\_64(4, 1, 0x07, RA\_PINCFG\_FUNC)

[ 284](pinctrl-r7fa4m1xxxxxx_8h.md#a1b8e8d8a0a2dbea69fb00a4c23673946)#define P401\_SDA1 RA\_PINCFG\_\_64(4, 1, 0x05, RA\_PINCFG\_FUNC)

[ 285](pinctrl-r7fa4m1xxxxxx_8h.md#aa858fd596f3876a9e11cb8aa1b96ae11)#define P401\_SEG05 RA\_PINCFG\_\_64(4, 1, 0x0D, RA\_PINCFG\_FUNC)

[ 286](pinctrl-r7fa4m1xxxxxx_8h.md#a2db27ffe68be59181836593b4542c180)#define P401\_SS0 RA\_PINCFG\_\_64(4, 1, 0x04, RA\_PINCFG\_FUNC)

[ 287](pinctrl-r7fa4m1xxxxxx_8h.md#a4dceaec80678d1149e6446f950de6209)#define P401\_TS19 RA\_PINCFG\_\_64(4, 1, 0x0C, RA\_PINCFG\_FUNC)

[ 288](pinctrl-r7fa4m1xxxxxx_8h.md#a62b9b9b2ecd5a80ee0e0bea9489e31a0)#define P401\_TXD1 RA\_PINCFG\_\_64(4, 1, 0x05, RA\_PINCFG\_FUNC)

[ 289](pinctrl-r7fa4m1xxxxxx_8h.md#af7ac56e0d33e642092dc630157830c51)#define P402\_AGTIO0 RA\_PINCFG\_\_64(4, 2, 0x01, RA\_PINCFG\_FUNC)

[ 290](pinctrl-r7fa4m1xxxxxx_8h.md#a72a2245edc5e713ea7755e1ca4954e20)#define P402\_AGTIO1 RA\_PINCFG\_\_64(4, 2, 0x02, RA\_PINCFG\_FUNC)

[ 291](pinctrl-r7fa4m1xxxxxx_8h.md#adcadfb72975c3e7cddc874d52f1ac105)#define P402\_CRX0 RA\_PINCFG\_\_64(4, 2, 0x10, RA\_PINCFG\_FUNC)

[ 292](pinctrl-r7fa4m1xxxxxx_8h.md#a1823e3dcd43b9a5ee61b99c636da78b1)#define P402\_MISO1 RA\_PINCFG\_\_64(4, 2, 0x05, RA\_PINCFG\_FUNC)

[ 293](pinctrl-r7fa4m1xxxxxx_8h.md#a3c9430433b5c408322dee3ed98521697)#define P402\_RTCIC0 RA\_PINCFG\_\_64(4, 2, 0x00, RA\_PINCFG\_GPIO)

[ 294](pinctrl-r7fa4m1xxxxxx_8h.md#ac7c72cc4c58b990792f7030a07395a65)#define P402\_RXD1 RA\_PINCFG\_\_64(4, 2, 0x05, RA\_PINCFG\_FUNC)

[ 295](pinctrl-r7fa4m1xxxxxx_8h.md#a469dc247170c78a94c288ade35c3d0c7)#define P402\_SCL1 RA\_PINCFG\_\_64(4, 2, 0x05, RA\_PINCFG\_FUNC)

[ 296](pinctrl-r7fa4m1xxxxxx_8h.md#a925635cd39d5065baee2e4b2cfc756e4)#define P402\_SEG06 RA\_PINCFG\_\_64(4, 2, 0x0D, RA\_PINCFG\_FUNC)

[ 297](pinctrl-r7fa4m1xxxxxx_8h.md#ad11c10175a6af695ce0b76c686b94c53)#define P402\_TS18 RA\_PINCFG\_\_64(4, 2, 0x0C, RA\_PINCFG\_FUNC)

[ 298](pinctrl-r7fa4m1xxxxxx_8h.md#aa9abec6e6602f3b68600fa9047c56926)#define P403\_AGTIO0 RA\_PINCFG\_100(4, 3, 0x01, RA\_PINCFG\_FUNC)

[ 299](pinctrl-r7fa4m1xxxxxx_8h.md#a2443c0e1dca850c89d1b422035962290)#define P403\_AGTIO1 RA\_PINCFG\_100(4, 3, 0x02, RA\_PINCFG\_FUNC)

[ 300](pinctrl-r7fa4m1xxxxxx_8h.md#a5c44f311b1138dc2db70f9a7f4e22776)#define P403\_CTS1\_RTS1 RA\_PINCFG\_100(4, 3, 0x05, RA\_PINCFG\_FUNC)

[ 301](pinctrl-r7fa4m1xxxxxx_8h.md#a09fa2f017715db75527ff1aebc9a302a)#define P403\_GTIOC3A RA\_PINCFG\_100(4, 3, 0x04, RA\_PINCFG\_FUNC)

[ 302](pinctrl-r7fa4m1xxxxxx_8h.md#a0a184b37e587b17aa2b7d3dcaede1b81)#define P403\_RTCIC1 RA\_PINCFG\_100(4, 3, 0x00, RA\_PINCFG\_GPIO)

[ 303](pinctrl-r7fa4m1xxxxxx_8h.md#a3d40722152a9794c83476dab14389bea)#define P403\_SS1 RA\_PINCFG\_100(4, 3, 0x05, RA\_PINCFG\_FUNC)

[ 304](pinctrl-r7fa4m1xxxxxx_8h.md#a0190081de02576c5f3e59188db06a93e)#define P403\_SSIBCK0 RA\_PINCFG\_100(4, 3, 0x12, RA\_PINCFG\_FUNC)

[ 305](pinctrl-r7fa4m1xxxxxx_8h.md#a2acf9c78301ac893f684580c4d6bedfc)#define P403\_TS17 RA\_PINCFG\_100(4, 3, 0x0C, RA\_PINCFG\_FUNC)

[ 306](pinctrl-r7fa4m1xxxxxx_8h.md#a04151d2e656fa2fc53675fb1a4c11426)#define P404\_GTIOC3B RA\_PINCFG\_100(4, 4, 0x04, RA\_PINCFG\_FUNC)

[ 307](pinctrl-r7fa4m1xxxxxx_8h.md#aefa25be112a52217c862ddf843edab15)#define P404\_RTCIC2 RA\_PINCFG\_100(4, 4, 0x00, RA\_PINCFG\_GPIO)

[ 308](pinctrl-r7fa4m1xxxxxx_8h.md#abf9a35f9f43b802121e2d86f5af9da2b)#define P404\_SSIFS0 RA\_PINCFG\_100(4, 4, 0x12, RA\_PINCFG\_FUNC)

[ 309](pinctrl-r7fa4m1xxxxxx_8h.md#a40d2fb6a5e072fd01bff3f3d5a2d969d)#define P404\_SSILRCK0 RA\_PINCFG\_100(4, 4, 0x12, RA\_PINCFG\_FUNC)

[ 310](pinctrl-r7fa4m1xxxxxx_8h.md#a2ad0866b5b378c277786b9e06a554276)#define P405\_GTIOC1A RA\_PINCFG\_100(4, 5, 0x04, RA\_PINCFG\_FUNC)

[ 311](pinctrl-r7fa4m1xxxxxx_8h.md#a6ba3e1de34caf43edee6296dddf381c0)#define P405\_SSITXD0 RA\_PINCFG\_100(4, 5, 0x12, RA\_PINCFG\_FUNC)

[ 312](pinctrl-r7fa4m1xxxxxx_8h.md#ae0d0e8459e261f2b57dbd791c7f45ea5)#define P406\_GTIOC1B RA\_PINCFG\_100(4, 6, 0x04, RA\_PINCFG\_FUNC)

[ 313](pinctrl-r7fa4m1xxxxxx_8h.md#a6f2d46a4f1f36da8d86761f8dbb7d31c)#define P406\_SSIRXD0 RA\_PINCFG\_100(4, 6, 0x12, RA\_PINCFG\_FUNC)

[ 314](pinctrl-r7fa4m1xxxxxx_8h.md#a78210c50417cbb74a2900e1c00786c74)#define P407\_ADTRG0 RA\_PINCFG\_\_40(4, 7, 0x0A, RA\_PINCFG\_FUNC)

[ 315](pinctrl-r7fa4m1xxxxxx_8h.md#a0a9b2ab6aff638a17cf103ab4f56eed8)#define P407\_AGTIO0 RA\_PINCFG\_\_40(4, 7, 0x01, RA\_PINCFG\_FUNC)

[ 316](pinctrl-r7fa4m1xxxxxx_8h.md#a11f9c3ad9bf508fa1fa9a3ae13770729)#define P407\_CTS0\_RTS0 RA\_PINCFG\_\_40(4, 7, 0x04, RA\_PINCFG\_FUNC)

[ 317](pinctrl-r7fa4m1xxxxxx_8h.md#a8a254bafdcba096f4132e953fdf623b3)#define P407\_RTCOUT RA\_PINCFG\_\_40(4, 7, 0x09, RA\_PINCFG\_FUNC)

[ 318](pinctrl-r7fa4m1xxxxxx_8h.md#a31b7e8fb35909ca728fa9e3d851f97ab)#define P407\_SDA0 RA\_PINCFG\_\_40(4, 7, 0x07, RA\_PINCFG\_FUNC)

[ 319](pinctrl-r7fa4m1xxxxxx_8h.md#af4e1bba7555fab56ba958b6af95c028d)#define P407\_SEG11 RA\_PINCFG\_\_40(4, 7, 0x0D, RA\_PINCFG\_FUNC)

[ 320](pinctrl-r7fa4m1xxxxxx_8h.md#a0e577382d671da8cb9c445476c4f348c)#define P407\_SS0 RA\_PINCFG\_\_40(4, 7, 0x04, RA\_PINCFG\_FUNC)

[ 321](pinctrl-r7fa4m1xxxxxx_8h.md#a9aad9e28e4c557bc1e8d7385fed3801a)#define P407\_SSLB3 RA\_PINCFG\_\_40(4, 7, 0x06, RA\_PINCFG\_FUNC)

[ 322](pinctrl-r7fa4m1xxxxxx_8h.md#a20a9c6465a6fad52cb5a67cce43f0493)#define P407\_TS03 RA\_PINCFG\_\_40(4, 7, 0x0C, RA\_PINCFG\_FUNC)

[ 323](pinctrl-r7fa4m1xxxxxx_8h.md#ac60561a4f1828e31254da17840656a4c)#define P407\_USB\_VBUS RA\_PINCFG\_\_40(4, 7, 0x13, RA\_PINCFG\_FUNC)

[ 324](pinctrl-r7fa4m1xxxxxx_8h.md#a7588f6344282930936c5e57813246814)#define P408\_CTS1\_RTS1 RA\_PINCFG\_\_40(4, 8, 0x04, RA\_PINCFG\_FUNC)

[ 325](pinctrl-r7fa4m1xxxxxx_8h.md#ad364943a5d6370d839ef7d28407b1afe)#define P408\_GTIOC5B RA\_PINCFG\_\_40(4, 8, 0x04, RA\_PINCFG\_FUNC)

[ 326](pinctrl-r7fa4m1xxxxxx_8h.md#a4565222efb3fae6c49c71d15aa221fab)#define P408\_GTOWLO RA\_PINCFG\_\_40(4, 8, 0x03, RA\_PINCFG\_FUNC)

[ 327](pinctrl-r7fa4m1xxxxxx_8h.md#a92dd77a61d29a66c820eac5a80a699b6)#define P408\_MISO9 RA\_PINCFG\_\_40(4, 8, 0x05, RA\_PINCFG\_FUNC)

[ 328](pinctrl-r7fa4m1xxxxxx_8h.md#abd0c4c0118a083980dd6e9ac5d98646e)#define P408\_RXD9 RA\_PINCFG\_\_40(4, 8, 0x05, RA\_PINCFG\_FUNC)

[ 329](pinctrl-r7fa4m1xxxxxx_8h.md#a529828871e4f3eeba761691d21e605c3)#define P408\_SCL0 RA\_PINCFG\_\_40(4, 8, 0x07, RA\_PINCFG\_FUNC)

[ 330](pinctrl-r7fa4m1xxxxxx_8h.md#a1f3e73dfa0be9a4784c5d5d304df7ecb)#define P408\_SCL9 RA\_PINCFG\_\_40(4, 8, 0x05, RA\_PINCFG\_FUNC)

[ 331](pinctrl-r7fa4m1xxxxxx_8h.md#ad58bd2c48ab929c28a662d27a1546605)#define P408\_SEG10 RA\_PINCFG\_\_40(4, 8, 0x0D, RA\_PINCFG\_FUNC)

[ 332](pinctrl-r7fa4m1xxxxxx_8h.md#ab2248878cc0e4ba0c3bf249c60c27247)#define P408\_SS1 RA\_PINCFG\_\_40(4, 8, 0x04, RA\_PINCFG\_FUNC)

[ 333](pinctrl-r7fa4m1xxxxxx_8h.md#a561657c669948fadc8f252368a6ab388)#define P408\_TS04 RA\_PINCFG\_\_40(4, 8, 0x0C, RA\_PINCFG\_FUNC)

[ 334](pinctrl-r7fa4m1xxxxxx_8h.md#abde615e5da408d63a2907437167d02a3)#define P408\_USB\_ID RA\_PINCFG\_\_40(4, 8, 0x13, RA\_PINCFG\_FUNC)

[ 335](pinctrl-r7fa4m1xxxxxx_8h.md#a0a841b2135f8ac6a7db3e5bfeb18f6b6)#define P409\_GTIOC5A RA\_PINCFG\_\_48(4, 9, 0x04, RA\_PINCFG\_FUNC)

[ 336](pinctrl-r7fa4m1xxxxxx_8h.md#ac26d4dc7c0e49838672d8bc2330439a9)#define P409\_GTOWUP RA\_PINCFG\_\_48(4, 9, 0x03, RA\_PINCFG\_FUNC)

[ 337](pinctrl-r7fa4m1xxxxxx_8h.md#ace85550be0f2fe536b35c810c10de31d)#define P409\_MOSI9 RA\_PINCFG\_\_48(4, 9, 0x05, RA\_PINCFG\_FUNC)

[ 338](pinctrl-r7fa4m1xxxxxx_8h.md#a6e2b47790d7d4ecc3f7953136ff533c6)#define P409\_SDA9 RA\_PINCFG\_\_48(4, 9, 0x05, RA\_PINCFG\_FUNC)

[ 339](pinctrl-r7fa4m1xxxxxx_8h.md#aefe794ced4c58b981030c63488adfe70)#define P409\_SEG09 RA\_PINCFG\_\_48(4, 9, 0x0D, RA\_PINCFG\_FUNC)

[ 340](pinctrl-r7fa4m1xxxxxx_8h.md#a41173432b6734f728ecd0b6d63a50f9f)#define P409\_TS05 RA\_PINCFG\_\_48(4, 9, 0x0C, RA\_PINCFG\_FUNC)

[ 341](pinctrl-r7fa4m1xxxxxx_8h.md#a7ab2da24896690896bd3f5af8ab4c858)#define P409\_TXD9 RA\_PINCFG\_\_48(4, 9, 0x05, RA\_PINCFG\_FUNC)

[ 342](pinctrl-r7fa4m1xxxxxx_8h.md#a77185ddb72e56633ab327cc631077cde)#define P409\_USB\_EXICEN RA\_PINCFG\_\_48(4, 9, 0x13, RA\_PINCFG\_FUNC)

[ 343](pinctrl-r7fa4m1xxxxxx_8h.md#a655d9a81e146e897e7959a7355be0b72)#define P410\_AGTOB1 RA\_PINCFG\_\_64(4, 10, 0x01, RA\_PINCFG\_FUNC)

[ 344](pinctrl-r7fa4m1xxxxxx_8h.md#a8cde85f60ca40a60da25cf719e2f9b1c)#define P410\_GTIOC6B RA\_PINCFG\_\_64(4, 10, 0x04, RA\_PINCFG\_FUNC)

[ 345](pinctrl-r7fa4m1xxxxxx_8h.md#a4497610f4a8793522538122904447056)#define P410\_GTOVLO RA\_PINCFG\_\_64(4, 10, 0x03, RA\_PINCFG\_FUNC)

[ 346](pinctrl-r7fa4m1xxxxxx_8h.md#a090ae5ec27312a6751c607638c49e4d8)#define P410\_MISO0 RA\_PINCFG\_\_64(4, 10, 0x04, RA\_PINCFG\_FUNC)

[ 347](pinctrl-r7fa4m1xxxxxx_8h.md#adb26ca4206d4f193c01b307c2dc04916)#define P410\_MISOA RA\_PINCFG\_\_64(4, 10, 0x06, RA\_PINCFG\_FUNC)

[ 348](pinctrl-r7fa4m1xxxxxx_8h.md#aaa12e3aaded55813f6300f07db7c6d99)#define P410\_RXD0 RA\_PINCFG\_\_64(4, 10, 0x04, RA\_PINCFG\_FUNC)

[ 349](pinctrl-r7fa4m1xxxxxx_8h.md#a68c851379ff8f72f58cdbf9a19bc8734)#define P410\_SCL0 RA\_PINCFG\_\_64(4, 10, 0x04, RA\_PINCFG\_FUNC)

[ 350](pinctrl-r7fa4m1xxxxxx_8h.md#a943dcb9d1d72f035323a60d95a170129)#define P410\_SEG08 RA\_PINCFG\_\_64(4, 10, 0x0D, RA\_PINCFG\_FUNC)

[ 351](pinctrl-r7fa4m1xxxxxx_8h.md#a579f9fcca5c6303efd20a233a4603402)#define P410\_TS06 RA\_PINCFG\_\_64(4, 10, 0x0C, RA\_PINCFG\_FUNC)

[ 352](pinctrl-r7fa4m1xxxxxx_8h.md#adf6af2628fedd695fd2871347aa6ab18)#define P411\_AGTOA1 RA\_PINCFG\_\_64(4, 11, 0x01, RA\_PINCFG\_FUNC)

[ 353](pinctrl-r7fa4m1xxxxxx_8h.md#a8f11fff5fec2944c1aa1732713a500aa)#define P411\_GTIOC6A RA\_PINCFG\_\_64(4, 11, 0x04, RA\_PINCFG\_FUNC)

[ 354](pinctrl-r7fa4m1xxxxxx_8h.md#afc9a1b654fbe60ee8b0fec78d9bb92f3)#define P411\_GTOVUP RA\_PINCFG\_\_64(4, 11, 0x03, RA\_PINCFG\_FUNC)

[ 355](pinctrl-r7fa4m1xxxxxx_8h.md#a671a22f8580c260eb9612bc7cc4d6f0c)#define P411\_MOSI0 RA\_PINCFG\_\_64(4, 11, 0x04, RA\_PINCFG\_FUNC)

[ 356](pinctrl-r7fa4m1xxxxxx_8h.md#ad7c943e6662dfbe4dc3d9bee771129b5)#define P411\_MOSIA RA\_PINCFG\_\_64(4, 11, 0x06, RA\_PINCFG\_FUNC)

[ 357](pinctrl-r7fa4m1xxxxxx_8h.md#abc3991fbfff2c530182de15fa26c9824)#define P411\_SDA0 RA\_PINCFG\_\_64(4, 11, 0x04, RA\_PINCFG\_FUNC)

[ 358](pinctrl-r7fa4m1xxxxxx_8h.md#a6beb0bfc0d69b89c027044c50d7a0d10)#define P411\_SEG07 RA\_PINCFG\_\_64(4, 11, 0x0D, RA\_PINCFG\_FUNC)

[ 359](pinctrl-r7fa4m1xxxxxx_8h.md#abe748f02f015d08179259d114a1494d7)#define P411\_TS07 RA\_PINCFG\_\_64(4, 11, 0x0C, RA\_PINCFG\_FUNC)

[ 360](pinctrl-r7fa4m1xxxxxx_8h.md#acc33e50befef8abfeaa40030e812f6c5)#define P411\_TXD0 RA\_PINCFG\_\_64(4, 11, 0x04, RA\_PINCFG\_FUNC)

[ 361](pinctrl-r7fa4m1xxxxxx_8h.md#ac01a71d0b82faeb18f1db409cfedf600)#define P412\_RSPCKA RA\_PINCFG\_100(4, 12, 0x06, RA\_PINCFG\_FUNC)

[ 362](pinctrl-r7fa4m1xxxxxx_8h.md#a2ece5b48c41ddae7859b420e8f3f9223)#define P412\_SCK0 RA\_PINCFG\_100(4, 12, 0x04, RA\_PINCFG\_FUNC)

[ 363](pinctrl-r7fa4m1xxxxxx_8h.md#a64cca107d40c4b46476254ebb52ff488)#define P413\_CTS0\_RTS0 RA\_PINCFG\_100(4, 13, 0x04, RA\_PINCFG\_FUNC)

[ 364](pinctrl-r7fa4m1xxxxxx_8h.md#a1c6e42223210ec50e4bd2568698010ad)#define P413\_SS0 RA\_PINCFG\_100(4, 13, 0x04, RA\_PINCFG\_FUNC)

[ 365](pinctrl-r7fa4m1xxxxxx_8h.md#abb95db38ffa518db199262ec878eed20)#define P413\_SSLA0 RA\_PINCFG\_100(4, 13, 0x06, RA\_PINCFG\_FUNC)

[ 366](pinctrl-r7fa4m1xxxxxx_8h.md#a502ea248a1b4e8769cf80e3a8565c53f)#define P414\_GTIOC0B RA\_PINCFG\_100(4, 14, 0x04, RA\_PINCFG\_FUNC)

[ 367](pinctrl-r7fa4m1xxxxxx_8h.md#ab375ec02341d56a77f55667c6935bf35)#define P414\_SSLA1 RA\_PINCFG\_100(4, 14, 0x06, RA\_PINCFG\_FUNC)

[ 368](pinctrl-r7fa4m1xxxxxx_8h.md#a781bf0beec671834e52cbfa941381dba)#define P415\_GTIOC0A RA\_PINCFG\_100(4, 15, 0x04, RA\_PINCFG\_FUNC)

[ 369](pinctrl-r7fa4m1xxxxxx_8h.md#a2b58731beae21abd0808a7808f67a539)#define P415\_SSLA2 RA\_PINCFG\_100(4, 15, 0x06, RA\_PINCFG\_FUNC)

[ 370](pinctrl-r7fa4m1xxxxxx_8h.md#a0e7332617514a46d74515ca5f37ad8db)#define P500\_AGTOA0 RA\_PINCFG\_\_48(5, 0, 0x01, RA\_PINCFG\_FUNC)

[ 371](pinctrl-r7fa4m1xxxxxx_8h.md#aeb9bddf825cd62018a44521683335a78)#define P500\_AN016 RA\_PINCFG\_\_48(5, 0, 0x01, RA\_PINCFG\_ANALOG)

[ 372](pinctrl-r7fa4m1xxxxxx_8h.md#a1ba7d5c6210da0753cc4ea083cdccdc8)#define P500\_CMPREF1 RA\_PINCFG\_\_48(5, 0, 0x02, RA\_PINCFG\_FUNC | RA\_PINCFG\_ANALOG)

[ 373](pinctrl-r7fa4m1xxxxxx_8h.md#a6ba45933f0efc39c278504d26e9e8535)#define P500\_GTIOC2A RA\_PINCFG\_\_48(5, 0, 0x04, RA\_PINCFG\_FUNC)

[ 374](pinctrl-r7fa4m1xxxxxx_8h.md#a912ec767c0ef1d08c442e3a34e0bf15a)#define P500\_GTIU RA\_PINCFG\_\_48(5, 0, 0x03, RA\_PINCFG\_FUNC)

[ 375](pinctrl-r7fa4m1xxxxxx_8h.md#a341a38568387948cb946fa5faff79b3f)#define P500\_SEG34 RA\_PINCFG\_\_48(5, 0, 0x0D, RA\_PINCFG\_FUNC)

[ 376](pinctrl-r7fa4m1xxxxxx_8h.md#a83ba0a1e56cbd326ee0b84468323144f)#define P500\_USB\_VBUSEN RA\_PINCFG\_\_48(5, 0, 0x13, RA\_PINCFG\_FUNC)

[ 377](pinctrl-r7fa4m1xxxxxx_8h.md#a2809c65d53bcb8c86486848d63ccac96)#define P501\_AGTOB0 RA\_PINCFG\_\_64(5, 1, 0x01, RA\_PINCFG\_FUNC)

[ 378](pinctrl-r7fa4m1xxxxxx_8h.md#a909c2ab752441a33df41584b762045d4)#define P501\_AN017 RA\_PINCFG\_\_64(5, 1, 0x01, RA\_PINCFG\_ANALOG)

[ 379](pinctrl-r7fa4m1xxxxxx_8h.md#a92750f7a3e44946ad9a740b77405cac9)#define P501\_CMPIN1 RA\_PINCFG\_\_64(5, 1, 0x02, RA\_PINCFG\_FUNC | RA\_PINCFG\_ANALOG)

[ 380](pinctrl-r7fa4m1xxxxxx_8h.md#a68f73587bcfc29d1508228363e18a133)#define P501\_GTIOC2B RA\_PINCFG\_\_64(5, 1, 0x04, RA\_PINCFG\_FUNC)

[ 381](pinctrl-r7fa4m1xxxxxx_8h.md#a17d8902f2029b6e92f9343d0a3a2b65e)#define P501\_GTIV RA\_PINCFG\_\_64(5, 1, 0x03, RA\_PINCFG\_FUNC)

[ 382](pinctrl-r7fa4m1xxxxxx_8h.md#af7ce7c70f64d500d62953924bedf705a)#define P501\_MOSI1 RA\_PINCFG\_\_64(5, 1, 0x05, RA\_PINCFG\_FUNC)

[ 383](pinctrl-r7fa4m1xxxxxx_8h.md#a63461589d98521e927fb161961b57f5d)#define P501\_SDA1 RA\_PINCFG\_\_64(5, 1, 0x05, RA\_PINCFG\_FUNC)

[ 384](pinctrl-r7fa4m1xxxxxx_8h.md#a3e9c8b86625c18a9f9b787594bfdd6bd)#define P501\_SEG35 RA\_PINCFG\_\_64(5, 1, 0x0D, RA\_PINCFG\_FUNC)

[ 385](pinctrl-r7fa4m1xxxxxx_8h.md#af5733ba92962d31618b3d272ac4b7639)#define P501\_TXD1 RA\_PINCFG\_\_64(5, 1, 0x05, RA\_PINCFG\_FUNC)

[ 386](pinctrl-r7fa4m1xxxxxx_8h.md#a22fa43159867319068863a8bee91fe3d)#define P501\_USB\_OVRCUR\_A RA\_PINCFG\_\_64(5, 1, 0x13, RA\_PINCFG\_FUNC)

[ 387](pinctrl-r7fa4m1xxxxxx_8h.md#a64f5d96f77954ee179a62cdedb91d45b)#define P502\_AN018 RA\_PINCFG\_\_64(5, 2, 0x01, RA\_PINCFG\_ANALOG)

[ 388](pinctrl-r7fa4m1xxxxxx_8h.md#a786dffb86b3f2db8c266f2b9b74be073)#define P502\_CMPREF0 RA\_PINCFG\_\_64(5, 2, 0x02, RA\_PINCFG\_FUNC | RA\_PINCFG\_ANALOG)

[ 389](pinctrl-r7fa4m1xxxxxx_8h.md#ac290b3513b17edfa9b078dfc0aceeb07)#define P502\_GTIOC3B RA\_PINCFG\_\_64(5, 2, 0x04, RA\_PINCFG\_FUNC)

[ 390](pinctrl-r7fa4m1xxxxxx_8h.md#af8a4b6c7154e62a4a7f15243ae894740)#define P502\_GTIW RA\_PINCFG\_\_64(5, 2, 0x03, RA\_PINCFG\_FUNC)

[ 391](pinctrl-r7fa4m1xxxxxx_8h.md#a594a0aee595f4a746e3f5f3aaa430bd6)#define P502\_MISO1 RA\_PINCFG\_\_64(5, 2, 0x05, RA\_PINCFG\_FUNC)

[ 392](pinctrl-r7fa4m1xxxxxx_8h.md#a02b8f10299338437fd3a54812776f801)#define P502\_RXD1 RA\_PINCFG\_\_64(5, 2, 0x05, RA\_PINCFG\_FUNC)

[ 393](pinctrl-r7fa4m1xxxxxx_8h.md#aef0b75c1bd8788044671d43f89153526)#define P502\_SCL1 RA\_PINCFG\_\_64(5, 2, 0x05, RA\_PINCFG\_FUNC)

[ 394](pinctrl-r7fa4m1xxxxxx_8h.md#aed07eabbe5cfa4647e0759b378b5de3d)#define P502\_SEG36 RA\_PINCFG\_\_64(5, 2, 0x0D, RA\_PINCFG\_FUNC)

[ 395](pinctrl-r7fa4m1xxxxxx_8h.md#aa28f5da61f114062ff07abaeb94ba065)#define P502\_USB\_OVRCUR\_B RA\_PINCFG\_\_64(5, 2, 0x13, RA\_PINCFG\_FUNC)

[ 396](pinctrl-r7fa4m1xxxxxx_8h.md#a153fae5c8bbbd02e7ba1d30db792597e)#define P503\_AN023 RA\_PINCFG\_100(5, 3, 0x01, RA\_PINCFG\_ANALOG)

[ 397](pinctrl-r7fa4m1xxxxxx_8h.md#a8f6152b8ecf8984f6af5ea3d2d45c0dc)#define P503\_CMPIN0 RA\_PINCFG\_100(5, 3, 0x02, RA\_PINCFG\_FUNC | RA\_PINCFG\_ANALOG)

[ 398](pinctrl-r7fa4m1xxxxxx_8h.md#a41699f1b15c611ee0afabc9e3826263d)#define P503\_SCK1 RA\_PINCFG\_100(5, 3, 0x05, RA\_PINCFG\_FUNC)

[ 399](pinctrl-r7fa4m1xxxxxx_8h.md#a45ce36fcfecc086780327adb4512960d)#define P503\_SEG37 RA\_PINCFG\_100(5, 3, 0x0D, RA\_PINCFG\_FUNC)

[ 400](pinctrl-r7fa4m1xxxxxx_8h.md#a266b849292e85cd877be8d123677423b)#define P503\_USB\_EXICEN RA\_PINCFG\_100(5, 3, 0x13, RA\_PINCFG\_FUNC)

[ 401](pinctrl-r7fa4m1xxxxxx_8h.md#a6242151d107150f75ddbaafd3d81d9e4)#define P504\_AN024 RA\_PINCFG\_100(5, 4, 0x01, RA\_PINCFG\_ANALOG)

[ 402](pinctrl-r7fa4m1xxxxxx_8h.md#a701dc34fd8f95ab87f85bd4d9d6ca78b)#define P504\_CTS1\_RTS1 RA\_PINCFG\_100(5, 4, 0x05, RA\_PINCFG\_FUNC)

[ 403](pinctrl-r7fa4m1xxxxxx_8h.md#ab29be069105a9bc2e7b50fe9ca302d56)#define P504\_SS1 RA\_PINCFG\_100(5, 4, 0x05, RA\_PINCFG\_FUNC)

[ 404](pinctrl-r7fa4m1xxxxxx_8h.md#a0b6072d754e8a6253ccdaa4db7a90356)#define P504\_USB\_ID RA\_PINCFG\_100(5, 4, 0x13, RA\_PINCFG\_FUNC)

[ 405](pinctrl-r7fa4m1xxxxxx_8h.md#a57705d3e5d3e3399aaf3694fa159a6c1)#define P505\_AN025 RA\_PINCFG\_100(5, 5, 0x01, RA\_PINCFG\_ANALOG)

[ 406](pinctrl-r7fa4m1xxxxxx_8h.md#a52ea9942e64400ccc101c703940d6931)#define P600\_GTIOC6B RA\_PINCFG\_100(6, 0, 0x01, RA\_PINCFG\_FUNC)

[ 407](pinctrl-r7fa4m1xxxxxx_8h.md#a589a8bcfe068d9c37057ac33f2832f70)#define P600\_SCK9 RA\_PINCFG\_100(6, 0, 0x05, RA\_PINCFG\_FUNC)

[ 408](pinctrl-r7fa4m1xxxxxx_8h.md#ac7fc1cad955944a8aaf0f5d6bc39efaa)#define P600\_SEG33 RA\_PINCFG\_100(6, 0, 0x0D, RA\_PINCFG\_FUNC)

[ 409](pinctrl-r7fa4m1xxxxxx_8h.md#a5e9f6651cd0c1f6e3f9b4abb5e136b15)#define P601\_GTIOC6A RA\_PINCFG\_100(6, 1, 0x01, RA\_PINCFG\_FUNC)

[ 410](pinctrl-r7fa4m1xxxxxx_8h.md#a7eb5f622761f9c686705f9aecb20e62d)#define P601\_MISO9 RA\_PINCFG\_100(6, 1, 0x05, RA\_PINCFG\_FUNC)

[ 411](pinctrl-r7fa4m1xxxxxx_8h.md#aadea111e051ab66625d23aff24231189)#define P601\_RXD9 RA\_PINCFG\_100(6, 1, 0x05, RA\_PINCFG\_FUNC)

[ 412](pinctrl-r7fa4m1xxxxxx_8h.md#a95e4eec728774e45c93f434f9dc581b1)#define P601\_SCL9 RA\_PINCFG\_100(6, 1, 0x05, RA\_PINCFG\_FUNC)

[ 413](pinctrl-r7fa4m1xxxxxx_8h.md#a324263fdc904b50b0df0247c8c95b1c4)#define P601\_SEG32 RA\_PINCFG\_100(6, 1, 0x0D, RA\_PINCFG\_FUNC)

[ 414](pinctrl-r7fa4m1xxxxxx_8h.md#a65a922e45e374d58ee7e2bcde33284e1)#define P602\_GTIOC7B RA\_PINCFG\_100(6, 2, 0x01, RA\_PINCFG\_FUNC)

[ 415](pinctrl-r7fa4m1xxxxxx_8h.md#a7bd8da28a12072ed00382b37c737009c)#define P602\_MOSI9 RA\_PINCFG\_100(6, 2, 0x05, RA\_PINCFG\_FUNC)

[ 416](pinctrl-r7fa4m1xxxxxx_8h.md#a8176daeb8027025dce20225d80e0ce37)#define P602\_SDA9 RA\_PINCFG\_100(6, 2, 0x05, RA\_PINCFG\_FUNC)

[ 417](pinctrl-r7fa4m1xxxxxx_8h.md#a1233d16c5f31591a2b1b0c30ae4ddc76)#define P602\_SEG31 RA\_PINCFG\_100(6, 2, 0x0D, RA\_PINCFG\_FUNC)

[ 418](pinctrl-r7fa4m1xxxxxx_8h.md#aff14aec3cc6daa12a89b6fde77998513)#define P602\_TXD9 RA\_PINCFG\_100(6, 2, 0x05, RA\_PINCFG\_FUNC)

[ 419](pinctrl-r7fa4m1xxxxxx_8h.md#a083e45aa6e50ff4cfb23dfd304e96b9f)#define P603\_CTS9\_RTS9 RA\_PINCFG\_100(6, 3, 0x05, RA\_PINCFG\_FUNC)

[ 420](pinctrl-r7fa4m1xxxxxx_8h.md#a14d48c4bc35fbdc8a2a7f273391e03b1)#define P603\_GTIOC7A RA\_PINCFG\_100(6, 3, 0x01, RA\_PINCFG\_FUNC)

[ 421](pinctrl-r7fa4m1xxxxxx_8h.md#a98cd77aaad40a1d33333d683643303d0)#define P603\_SEG30 RA\_PINCFG\_100(6, 3, 0x0D, RA\_PINCFG\_FUNC)

[ 422](pinctrl-r7fa4m1xxxxxx_8h.md#ad1368e8487345ee632e7e5037eea1445)#define P603\_SS9 RA\_PINCFG\_100(6, 3, 0x05, RA\_PINCFG\_FUNC)

[ 423](pinctrl-r7fa4m1xxxxxx_8h.md#a10538560d852952f5ae9286124da9bb9)#define P608\_GTIOC4B RA\_PINCFG\_100(6, 8, 0x01, RA\_PINCFG\_FUNC)

[ 424](pinctrl-r7fa4m1xxxxxx_8h.md#a476b73b1a6852562e387e519834c270f)#define P608\_SEG27 RA\_PINCFG\_100(6, 8, 0x0D, RA\_PINCFG\_FUNC)

[ 425](pinctrl-r7fa4m1xxxxxx_8h.md#ace28fa9b018156bc35ed43b6952eccaa)#define P609\_GTIOC5A RA\_PINCFG\_100(6, 9, 0x01, RA\_PINCFG\_FUNC)

[ 426](pinctrl-r7fa4m1xxxxxx_8h.md#a69a0d075ca439432396188a9b6b8a810)#define P609\_SEG28 RA\_PINCFG\_100(6, 9, 0x0D, RA\_PINCFG\_FUNC)

[ 427](pinctrl-r7fa4m1xxxxxx_8h.md#a4d12c56547dd18243abbe672ef5df639)#define P610\_GTIOC5B RA\_PINCFG\_100(6, 10, 0x01, RA\_PINCFG\_FUNC)

[ 428](pinctrl-r7fa4m1xxxxxx_8h.md#a62a3e75b3501ae96194cb2dbd14e9b05)#define P610\_SEG29 RA\_PINCFG\_100(6, 10, 0x0D, RA\_PINCFG\_FUNC)

[ 429](pinctrl-r7fa4m1xxxxxx_8h.md#a282afa57297badb9e1910e66100ed60d)#define P708\_MISO1 RA\_PINCFG\_100(7, 8, 0x05, RA\_PINCFG\_FUNC)

[ 430](pinctrl-r7fa4m1xxxxxx_8h.md#aa54cfaf6f56b66db1dac2da12e6a42f6)#define P708\_RXD1 RA\_PINCFG\_100(7, 8, 0x05, RA\_PINCFG\_FUNC)

[ 431](pinctrl-r7fa4m1xxxxxx_8h.md#a64dfa468d759e28690982f198ed67f8c)#define P708\_SCL1 RA\_PINCFG\_100(7, 8, 0x05, RA\_PINCFG\_FUNC)

[ 432](pinctrl-r7fa4m1xxxxxx_8h.md#a09d40bb8ac2ba0d62ff6e3cda6504f04)#define P708\_SSLA3 RA\_PINCFG\_100(7, 8, 0x06, RA\_PINCFG\_FUNC)

[ 433](pinctrl-r7fa4m1xxxxxx_8h.md#abcb71c6fb76382405a0a22183e244b5b)#define P808\_SEG21 RA\_PINCFG\_100(8, 8, 0x0D, RA\_PINCFG\_FUNC)

[ 434](pinctrl-r7fa4m1xxxxxx_8h.md#ac67c307b7441d0c70d9c0940e50bab03)#define P809\_SEG22 RA\_PINCFG\_100(8, 9, 0x0D, RA\_PINCFG\_FUNC)

[ 435](pinctrl-r7fa4m1xxxxxx_8h.md#a4a165e98d5a6abe1690a8ea321ba264e)#define P914\_USB\_DP RA\_PINCFG\_\_40(9, 14, 0x00, RA\_PINCFG\_GPIO)

[ 436](pinctrl-r7fa4m1xxxxxx_8h.md#a9bbcc12c7d278c7cb3f9c3e0bf67143c)#define P915\_USB\_DM RA\_PINCFG\_\_40(9, 15, 0x00, RA\_PINCFG\_GPIO)

437#endif

[pinctrl-ra-common.h](pinctrl-ra-common_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [pinctrl](dir_2c6c4fbd167577104b7f1b7148586168.md)
- [renesas](dir_17f48eb154be6cea623223db5de209e7.md)
- [pinctrl-r7fa4m1xxxxxx.h](pinctrl-r7fa4m1xxxxxx_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
