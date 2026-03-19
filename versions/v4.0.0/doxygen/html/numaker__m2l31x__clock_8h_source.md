---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/numaker__m2l31x__clock_8h_source.html
original_path: doxygen/html/numaker__m2l31x__clock_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

numaker\_m2l31x\_clock.h

[Go to the documentation of this file.](numaker__m2l31x__clock_8h.md)

1/\*

2 \* Copyright (c) 2024 Nuvoton Technology Corporation.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_NUMAKER\_M2L31\_CLOCK\_H

8#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_NUMAKER\_M2L31\_CLOCK\_H

9

[ 10](numaker__m2l31x__clock_8h.md#aaf5b579f16bb170913264beb84939aa2)#define NUMAKER\_CLK\_CLKSEL0\_HCLKSEL\_HXT 0x00000000

[ 11](numaker__m2l31x__clock_8h.md#a53e9db59708390ee4ff22e11f554fc5e)#define NUMAKER\_CLK\_CLKSEL0\_HCLKSEL\_LXT 0x00000001

[ 12](numaker__m2l31x__clock_8h.md#ae98f1f84fa81ed435a46eccaab5bb66b)#define NUMAKER\_CLK\_CLKSEL0\_HCLKSEL\_PLL 0x00000002

[ 13](numaker__m2l31x__clock_8h.md#a88a9e37b2360e0f703c0c469468adb1e)#define NUMAKER\_CLK\_CLKSEL0\_HCLKSEL\_LIRC 0x00000003

[ 14](numaker__m2l31x__clock_8h.md#a138ecd35f8d365d9e5e51374093daf36)#define NUMAKER\_CLK\_CLKSEL0\_HCLKSEL\_MIRC 0x00000005

[ 15](numaker__m2l31x__clock_8h.md#add09b29f1b99a979b806733a0c7f414e)#define NUMAKER\_CLK\_CLKSEL0\_HCLKSEL\_HIRC48M 0x00000006

[ 16](numaker__m2l31x__clock_8h.md#a35a5144f4df0ca09710fbc8d86377537)#define NUMAKER\_CLK\_CLKSEL0\_HCLKSEL\_HIRC 0x00000007

[ 17](numaker__m2l31x__clock_8h.md#a3b7cfbc1bea43960476a08e2287c1914)#define NUMAKER\_CLK\_CLKSEL0\_HCLK0SEL\_HXT 0x00000000

[ 18](numaker__m2l31x__clock_8h.md#a0cf6b5df2b6971d869cc2ac1b097621e)#define NUMAKER\_CLK\_CLKSEL0\_HCLK0SEL\_LXT 0x00000001

[ 19](numaker__m2l31x__clock_8h.md#a0450fb1951f8a2347c6a716a16503d08)#define NUMAKER\_CLK\_CLKSEL0\_HCLK0SEL\_PLL 0x00000002

[ 20](numaker__m2l31x__clock_8h.md#aae6e73caf317c6b0d8eb0db082390d8c)#define NUMAKER\_CLK\_CLKSEL0\_HCLK0SEL\_LIRC 0x00000003

[ 21](numaker__m2l31x__clock_8h.md#acf34871113b48bc39be48456e802b4c0)#define NUMAKER\_CLK\_CLKSEL0\_HCLK0SEL\_MIRC 0x00000005

[ 22](numaker__m2l31x__clock_8h.md#a5f5b8dac825043510b20c5196d47d5c0)#define NUMAKER\_CLK\_CLKSEL0\_HCLK0SEL\_HIRC48M 0x00000006

[ 23](numaker__m2l31x__clock_8h.md#a3ed8a7dfde5be37a66d3cbffeaf2d700)#define NUMAKER\_CLK\_CLKSEL0\_HCLK0SEL\_HIRC 0x00000007

[ 24](numaker__m2l31x__clock_8h.md#a937c9db689672d3f6e53e6b0f5a680ae)#define NUMAKER\_CLK\_CLKSEL0\_STCLKSEL\_HXT 0x00000000

[ 25](numaker__m2l31x__clock_8h.md#a7195fd0da5b897cf2c1e5df46205198d)#define NUMAKER\_CLK\_CLKSEL0\_STCLKSEL\_LXT 0x00000008

[ 26](numaker__m2l31x__clock_8h.md#a1afd0ea4fb7e6bbc5f36a7845121b5bb)#define NUMAKER\_CLK\_CLKSEL0\_STCLKSEL\_HXT\_DIV2 0x00000010

[ 27](numaker__m2l31x__clock_8h.md#a6e4942ca524470a1dbfd9c1012c3d6fc)#define NUMAKER\_CLK\_CLKSEL0\_STCLKSEL\_HCLK\_DIV2 0x00000018

[ 28](numaker__m2l31x__clock_8h.md#aee56f494a2a1028b579aee48a229bd62)#define NUMAKER\_CLK\_CLKSEL0\_STCLKSEL\_HIRC\_DIV2 0x00000038

[ 29](numaker__m2l31x__clock_8h.md#a05e3ff81f91b5cafac55e3d1d8b0baaf)#define NUMAKER\_CLK\_CLKSEL0\_HCLK1SEL\_HIRC 0x00000000

[ 30](numaker__m2l31x__clock_8h.md#a731049495b12f4cabff21a54858e2822)#define NUMAKER\_CLK\_CLKSEL0\_HCLK1SEL\_MIRC 0x00001000

[ 31](numaker__m2l31x__clock_8h.md#a160827bc2b490581a09ccc0e74e8d2e4)#define NUMAKER\_CLK\_CLKSEL0\_HCLK1SEL\_LXT 0x00002000

[ 32](numaker__m2l31x__clock_8h.md#a72f76e6b4070cc92295ea276d302dbe4)#define NUMAKER\_CLK\_CLKSEL0\_HCLK1SEL\_LIRC 0x00003000

[ 33](numaker__m2l31x__clock_8h.md#accc7fc8141c6125c49e8d44098b0a531)#define NUMAKER\_CLK\_CLKSEL0\_HCLK1SEL\_HIRC48M\_DIV2 0x00004000

[ 34](numaker__m2l31x__clock_8h.md#a4324fd407c6e6dbb86e84810094030fb)#define NUMAKER\_CLK\_CLKSEL0\_USBSEL\_HIRC48M 0x00000000

[ 35](numaker__m2l31x__clock_8h.md#a9a99e710e0acd80b9df5f52272690e2d)#define NUMAKER\_CLK\_CLKSEL0\_USBSEL\_PLL 0x00000100

[ 36](numaker__m2l31x__clock_8h.md#a9fbd71eb64e03adf48cb292d21481ad4)#define NUMAKER\_CLK\_CLKSEL0\_EADC0SEL\_PLL 0x00000400

[ 37](numaker__m2l31x__clock_8h.md#a8f1802b4d8c733d098e6f457ea9ca0a8)#define NUMAKER\_CLK\_CLKSEL0\_EADC0SEL\_HCLK 0x00000800

[ 38](numaker__m2l31x__clock_8h.md#a4b1dd4ddfac74c6962084d854bd529d9)#define NUMAKER\_CLK\_CLKSEL0\_EADC0SEL\_HCLK0 0x00000800

[ 39](numaker__m2l31x__clock_8h.md#a68b63fb3e764161c45a5a39258038536)#define NUMAKER\_CLK\_CLKSEL0\_EADC0SEL\_HIRC 0x00000C00

[ 40](numaker__m2l31x__clock_8h.md#a097628cbacc57dad0410c5330b6385b8)#define NUMAKER\_CLK\_CLKSEL0\_CANFD0SEL\_HXT 0x00000000

[ 41](numaker__m2l31x__clock_8h.md#a801cbbeeea88d1fa6ad3c72282d149d3)#define NUMAKER\_CLK\_CLKSEL0\_CANFD0SEL\_HIRC48M 0x01000000

[ 42](numaker__m2l31x__clock_8h.md#ae369ded35f04609db7e2a5a6922a5e1a)#define NUMAKER\_CLK\_CLKSEL0\_CANFD0SEL\_HCLK 0x02000000

[ 43](numaker__m2l31x__clock_8h.md#a8317bd684974bbaa5a12e55822cbc688)#define NUMAKER\_CLK\_CLKSEL0\_CANFD0SEL\_HCLK0 0x02000000

[ 44](numaker__m2l31x__clock_8h.md#aba0fe8b523048854cd02b4825e59f1c0)#define NUMAKER\_CLK\_CLKSEL0\_CANFD0SEL\_HIRC 0x03000000

[ 45](numaker__m2l31x__clock_8h.md#a3cc669c6de091303d9c65853000637e2)#define NUMAKER\_CLK\_CLKSEL0\_CANFD1SEL\_HXT 0x00000000

[ 46](numaker__m2l31x__clock_8h.md#acf8b19a19ffdbd4bf678abc99eb2537d)#define NUMAKER\_CLK\_CLKSEL0\_CANFD1SEL\_HIRC48M 0x04000000

[ 47](numaker__m2l31x__clock_8h.md#a1752cabeb909b64b92adbdc61215f3f9)#define NUMAKER\_CLK\_CLKSEL0\_CANFD1SEL\_HCLK 0x08000000

[ 48](numaker__m2l31x__clock_8h.md#a63df1a107746879941280fdbde95ff2f)#define NUMAKER\_CLK\_CLKSEL0\_CANFD1SEL\_HCLK0 0x08000000

[ 49](numaker__m2l31x__clock_8h.md#a43849c77be4cb2dd288f1d0b81bb18c8)#define NUMAKER\_CLK\_CLKSEL0\_CANFD1SEL\_HIRC 0x0C000000

[ 50](numaker__m2l31x__clock_8h.md#a2dba089a2c9a8780fa15705ce58719e4)#define NUMAKER\_CLK\_CLKSEL1\_CLKOSEL\_HXT 0x00000000

[ 51](numaker__m2l31x__clock_8h.md#a0b6ad7b069802aead804d11668cab813)#define NUMAKER\_CLK\_CLKSEL1\_CLKOSEL\_LXT 0x00000010

[ 52](numaker__m2l31x__clock_8h.md#a9cc286fd7b086fa05e00d24e2d7e5846)#define NUMAKER\_CLK\_CLKSEL1\_CLKOSEL\_HCLK 0x00000020

[ 53](numaker__m2l31x__clock_8h.md#aecf5ad463cd9105d902768c7bef51e36)#define NUMAKER\_CLK\_CLKSEL1\_CLKOSEL\_HCLK0 0x00000020

[ 54](numaker__m2l31x__clock_8h.md#a33998b80d4139f5cfd5aa6dc02c762c8)#define NUMAKER\_CLK\_CLKSEL1\_CLKOSEL\_HIRC 0x00000030

[ 55](numaker__m2l31x__clock_8h.md#ade649734a0c7017a8ddf62fdde78873b)#define NUMAKER\_CLK\_CLKSEL1\_CLKOSEL\_LIRC 0x00000040

[ 56](numaker__m2l31x__clock_8h.md#ae78a2bc307d4341e5f2d857d44a182cb)#define NUMAKER\_CLK\_CLKSEL1\_CLKOSEL\_HIRC48M 0x00000050

[ 57](numaker__m2l31x__clock_8h.md#aff71de21531fa6374c2481085e31c439)#define NUMAKER\_CLK\_CLKSEL1\_CLKOSEL\_PLL 0x00000060

[ 58](numaker__m2l31x__clock_8h.md#a666974b7033eda593fe10a1ab6b86a88)#define NUMAKER\_CLK\_CLKSEL1\_CLKOSEL\_MIRC 0x00000070

[ 59](numaker__m2l31x__clock_8h.md#a269fe710118dddabc1d17f2d1386835c)#define NUMAKER\_CLK\_CLKSEL1\_TMR0SEL\_HXT 0x00000000

[ 60](numaker__m2l31x__clock_8h.md#a37317151b25b9c7563a6e572e0199acc)#define NUMAKER\_CLK\_CLKSEL1\_TMR0SEL\_LXT 0x00000100

[ 61](numaker__m2l31x__clock_8h.md#afe9eadbd094da1c48851507719485200)#define NUMAKER\_CLK\_CLKSEL1\_TMR0SEL\_PCLK0 0x00000200

[ 62](numaker__m2l31x__clock_8h.md#ab4b9c993b869f23701052ef27c88cc3b)#define NUMAKER\_CLK\_CLKSEL1\_TMR0SEL\_EXT 0x00000300

[ 63](numaker__m2l31x__clock_8h.md#a7f4fd7330e7ff33c4bcd4b8e666f01c1)#define NUMAKER\_CLK\_CLKSEL1\_TMR0SEL\_LIRC 0x00000500

[ 64](numaker__m2l31x__clock_8h.md#ac7913ee7fe365daa500f7e1175bda470)#define NUMAKER\_CLK\_CLKSEL1\_TMR0SEL\_HIRC 0x00000700

[ 65](numaker__m2l31x__clock_8h.md#a1a6d0e60fd711d553ac0b0bf78ea6d54)#define NUMAKER\_CLK\_CLKSEL1\_TMR1SEL\_HXT 0x00000000

[ 66](numaker__m2l31x__clock_8h.md#a425b5c7e0d424c13328840437f9a0bb9)#define NUMAKER\_CLK\_CLKSEL1\_TMR1SEL\_LXT 0x00001000

[ 67](numaker__m2l31x__clock_8h.md#a54f24cfa94c28f844f428bd06e68eb8e)#define NUMAKER\_CLK\_CLKSEL1\_TMR1SEL\_PCLK0 0x00002000

[ 68](numaker__m2l31x__clock_8h.md#a208dcc5b1095e5cf4c2dec3c312a62ac)#define NUMAKER\_CLK\_CLKSEL1\_TMR1SEL\_EXT 0x00003000

[ 69](numaker__m2l31x__clock_8h.md#a1f9fde3db711f618393435af9dcdd621)#define NUMAKER\_CLK\_CLKSEL1\_TMR1SEL\_LIRC 0x00005000

[ 70](numaker__m2l31x__clock_8h.md#acb979acb614600a7126e12eefc181c8c)#define NUMAKER\_CLK\_CLKSEL1\_TMR1SEL\_HIRC 0x00007000

[ 71](numaker__m2l31x__clock_8h.md#ad0ac4ff4a21c3469c892dca5f6a7d469)#define NUMAKER\_CLK\_CLKSEL1\_TMR2SEL\_HXT 0x00000000

[ 72](numaker__m2l31x__clock_8h.md#afc8fb6c4fa6138465928926044fadd86)#define NUMAKER\_CLK\_CLKSEL1\_TMR2SEL\_LXT 0x00010000

[ 73](numaker__m2l31x__clock_8h.md#af5d0ba5a62dbc29d7e5e2d0ebf026584)#define NUMAKER\_CLK\_CLKSEL1\_TMR2SEL\_PCLK1 0x00020000

[ 74](numaker__m2l31x__clock_8h.md#a6cd38e0106ba70158dce964022d1ff93)#define NUMAKER\_CLK\_CLKSEL1\_TMR2SEL\_EXT 0x00030000

[ 75](numaker__m2l31x__clock_8h.md#a868569fb4688e0c5399d753f751b71f4)#define NUMAKER\_CLK\_CLKSEL1\_TMR2SEL\_LIRC 0x00050000

[ 76](numaker__m2l31x__clock_8h.md#aa19a857602df260f1c5715008dd7cedf)#define NUMAKER\_CLK\_CLKSEL1\_TMR2SEL\_HIRC 0x00070000

[ 77](numaker__m2l31x__clock_8h.md#a41fd2a33360832aa6de1ff87d1a8d1a4)#define NUMAKER\_CLK\_CLKSEL1\_TMR3SEL\_HXT 0x00000000

[ 78](numaker__m2l31x__clock_8h.md#a20ba7b5a926c9a4686e452a209221336)#define NUMAKER\_CLK\_CLKSEL1\_TMR3SEL\_LXT 0x00100000

[ 79](numaker__m2l31x__clock_8h.md#a597126647f0c72cddca37488818158f1)#define NUMAKER\_CLK\_CLKSEL1\_TMR3SEL\_PCLK1 0x00200000

[ 80](numaker__m2l31x__clock_8h.md#a6173a75df6e455a46b27486fa74d1b97)#define NUMAKER\_CLK\_CLKSEL1\_TMR3SEL\_EXT 0x00300000

[ 81](numaker__m2l31x__clock_8h.md#a3c686b34710b45462347705592e74cb7)#define NUMAKER\_CLK\_CLKSEL1\_TMR3SEL\_LIRC 0x00500000

[ 82](numaker__m2l31x__clock_8h.md#a59c5904ed60fd6aff34f2d90cebdf906)#define NUMAKER\_CLK\_CLKSEL1\_TMR3SEL\_HIRC 0x00700000

[ 83](numaker__m2l31x__clock_8h.md#a7d55fac6b093ac281eb9a0bf0762ade4)#define NUMAKER\_CLK\_CLKSEL1\_WWDTSEL\_HCLK\_DIV2048 0x80000000

[ 84](numaker__m2l31x__clock_8h.md#a3f3bfbd45bfddd1072c87628e4cae0b9)#define NUMAKER\_CLK\_CLKSEL1\_WWDTSEL\_HCLK0\_DIV2048 0x80000000

[ 85](numaker__m2l31x__clock_8h.md#a838ca0acbf99746d596456f32ea411e1)#define NUMAKER\_CLK\_CLKSEL1\_WWDTSEL\_LIRC 0xC0000000

[ 86](numaker__m2l31x__clock_8h.md#a066b7281b9e714d8e30af62b3df99fb1)#define NUMAKER\_CLK\_CLKSEL2\_EPWM0SEL\_HCLK 0x00000000

[ 87](numaker__m2l31x__clock_8h.md#a2a2081d41f4e064ac22e66539dbe0117)#define NUMAKER\_CLK\_CLKSEL2\_EPWM0SEL\_HCLK0 0x00000000

[ 88](numaker__m2l31x__clock_8h.md#a5886a5009f7f0ef41f04bff54c2f4781)#define NUMAKER\_CLK\_CLKSEL2\_EPWM0SEL\_PCLK0 0x00000001

[ 89](numaker__m2l31x__clock_8h.md#a6ed53fbec964b2d85b10b8be7d3d5063)#define NUMAKER\_CLK\_CLKSEL2\_EPWM1SEL\_HCLK 0x00000000

[ 90](numaker__m2l31x__clock_8h.md#afa514a836e19b91564320adc2cbd81d3)#define NUMAKER\_CLK\_CLKSEL2\_EPWM1SEL\_HCLK0 0x00000000

[ 91](numaker__m2l31x__clock_8h.md#a84f8299574ba19909d135d6958655a67)#define NUMAKER\_CLK\_CLKSEL2\_EPWM1SEL\_PCLK1 0x00000002

[ 92](numaker__m2l31x__clock_8h.md#ab2035f3ef4f5dfa4dbd629b928729114)#define NUMAKER\_CLK\_CLKSEL2\_QSPI0SEL\_HXT 0x00000000

[ 93](numaker__m2l31x__clock_8h.md#ad0313f74c89bcb4d89e8a3ccca8f438f)#define NUMAKER\_CLK\_CLKSEL2\_QSPI0SEL\_PLL 0x00000004

[ 94](numaker__m2l31x__clock_8h.md#a7e185755d01c123d2b05e7657f50b87f)#define NUMAKER\_CLK\_CLKSEL2\_QSPI0SEL\_PCLK0 0x00000008

[ 95](numaker__m2l31x__clock_8h.md#ab8f6509882bb312a7bb5f215e21556be)#define NUMAKER\_CLK\_CLKSEL2\_QSPI0SEL\_HIRC 0x0000000C

[ 96](numaker__m2l31x__clock_8h.md#aa8fea6d4d392fbb12385bd3dc3d7e41d)#define NUMAKER\_CLK\_CLKSEL2\_SPI0SEL\_HXT 0x00000000

[ 97](numaker__m2l31x__clock_8h.md#ab11fadf8a80ce728787986cf4713c38f)#define NUMAKER\_CLK\_CLKSEL2\_SPI0SEL\_PLL 0x00000010

[ 98](numaker__m2l31x__clock_8h.md#a7f6f7f591f7b3ce3522fa63abe564fe5)#define NUMAKER\_CLK\_CLKSEL2\_SPI0SEL\_PCLK1 0x00000020

[ 99](numaker__m2l31x__clock_8h.md#a5490e8ae6a82a281d81026b37ad5dfb7)#define NUMAKER\_CLK\_CLKSEL2\_SPI0SEL\_HIRC 0x00000030

[ 100](numaker__m2l31x__clock_8h.md#ad8b1a5339bf72877ac1eee28e35cdc76)#define NUMAKER\_CLK\_CLKSEL2\_SPI0SEL\_HIRC48M 0x00000040

[ 101](numaker__m2l31x__clock_8h.md#a884636b980b5a48d774257ac003ea65f)#define NUMAKER\_CLK\_CLKSEL2\_TKSEL\_HIRC 0x00000000

[ 102](numaker__m2l31x__clock_8h.md#a6fe8cf7d47c558a815a439724de4f7ba)#define NUMAKER\_CLK\_CLKSEL2\_TKSEL\_MIRC 0x00000080

[ 103](numaker__m2l31x__clock_8h.md#a02ec8188dc04f486240c9534ecbd2f76)#define NUMAKER\_CLK\_CLKSEL2\_SPI1SEL\_HXT 0x00000000

[ 104](numaker__m2l31x__clock_8h.md#a0391180b7e97f63bf0f76b7bc9ae1c4b)#define NUMAKER\_CLK\_CLKSEL2\_SPI1SEL\_PLL 0x00001000

[ 105](numaker__m2l31x__clock_8h.md#ac6fe2e428168fde50cdc9d7accebba31)#define NUMAKER\_CLK\_CLKSEL2\_SPI1SEL\_PCLK0 0x00002000

[ 106](numaker__m2l31x__clock_8h.md#a62209956eeaf9174960a476a2514b72d)#define NUMAKER\_CLK\_CLKSEL2\_SPI1SEL\_HIRC 0x00003000

[ 107](numaker__m2l31x__clock_8h.md#a14000a6d12ea314b48c738e39ae5e6c2)#define NUMAKER\_CLK\_CLKSEL2\_SPI1SEL\_HIRC48M 0x00004000

[ 108](numaker__m2l31x__clock_8h.md#aab0736b90fb0fd5d56c3918b4d2e6648)#define NUMAKER\_CLK\_CLKSEL3\_PWM0SEL\_HCLK 0x00000000

[ 109](numaker__m2l31x__clock_8h.md#a91180257d7b1436ac59a2b2c8b3878ff)#define NUMAKER\_CLK\_CLKSEL3\_PWM0SEL\_HCLK0 0x00000000

[ 110](numaker__m2l31x__clock_8h.md#a4ceb1b67fd1d35dea17a547b1e532a1e)#define NUMAKER\_CLK\_CLKSEL3\_PWM0SEL\_PCLK0 0x00000040

[ 111](numaker__m2l31x__clock_8h.md#ac677c6659ffcad97e0911124b4bdc4d1)#define NUMAKER\_CLK\_CLKSEL3\_PWM1SEL\_HCLK 0x00000000

[ 112](numaker__m2l31x__clock_8h.md#ad0d82628ab6034858a393823b8911df5)#define NUMAKER\_CLK\_CLKSEL3\_PWM1SEL\_HCLK0 0x00000000

[ 113](numaker__m2l31x__clock_8h.md#ab764a057b86d6fbc75ea7d9e615eac7f)#define NUMAKER\_CLK\_CLKSEL3\_PWM1SEL\_PCLK1 0x00000080

[ 114](numaker__m2l31x__clock_8h.md#abfae567f85ec08381bb0db7c81fd74d3)#define NUMAKER\_CLK\_CLKSEL3\_SPI2SEL\_HXT 0x00000000

[ 115](numaker__m2l31x__clock_8h.md#a23f3d4e580555938607c6c4a0cefd90e)#define NUMAKER\_CLK\_CLKSEL3\_SPI2SEL\_PLL 0x00000100

[ 116](numaker__m2l31x__clock_8h.md#a13a781d3f27119fb8067191f981fc52b)#define NUMAKER\_CLK\_CLKSEL3\_SPI2SEL\_PCLK1 0x00000200

[ 117](numaker__m2l31x__clock_8h.md#ab087f54ea6ea67e1f41aeaf948782c1f)#define NUMAKER\_CLK\_CLKSEL3\_SPI2SEL\_HIRC 0x00000300

[ 118](numaker__m2l31x__clock_8h.md#a3e5c5f8daec012d060843a800802fea1)#define NUMAKER\_CLK\_CLKSEL3\_SPI2SEL\_HIRC48M 0x00000400

[ 119](numaker__m2l31x__clock_8h.md#a3b87db844ad61714826adc34da9ec7b0)#define NUMAKER\_CLK\_CLKSEL3\_SPI3SEL\_HXT 0x00000000

[ 120](numaker__m2l31x__clock_8h.md#a443e2c0a548aa2cfc80d10c6cf25f208)#define NUMAKER\_CLK\_CLKSEL3\_SPI3SEL\_PLL 0x00001000

[ 121](numaker__m2l31x__clock_8h.md#a38d7de1142dbcbb41efc14ff3a509e6a)#define NUMAKER\_CLK\_CLKSEL3\_SPI3SEL\_PCLK0 0x00002000

[ 122](numaker__m2l31x__clock_8h.md#a013d56f4921687d6417e06944e0604f4)#define NUMAKER\_CLK\_CLKSEL3\_SPI3SEL\_HIRC 0x00003000

[ 123](numaker__m2l31x__clock_8h.md#a97eb5cf29a9fdf172288db3696a9c690)#define NUMAKER\_CLK\_CLKSEL3\_SPI3SEL\_HIRC48M 0x00004000

[ 124](numaker__m2l31x__clock_8h.md#aefdedc3aa179f0b3960d39a4f4ae5a1a)#define NUMAKER\_CLK\_CLKSEL4\_UART0SEL\_HXT 0x00000000

[ 125](numaker__m2l31x__clock_8h.md#a92c903e3bf599d1484ad450cad512df4)#define NUMAKER\_CLK\_CLKSEL4\_UART0SEL\_PLL 0x00000001

[ 126](numaker__m2l31x__clock_8h.md#a5be06a3942ea96f81e1d5749fa3f1308)#define NUMAKER\_CLK\_CLKSEL4\_UART0SEL\_LXT 0x00000002

[ 127](numaker__m2l31x__clock_8h.md#ad9a879e6031a60f7d6dd69769f8ab0a6)#define NUMAKER\_CLK\_CLKSEL4\_UART0SEL\_HIRC 0x00000003

[ 128](numaker__m2l31x__clock_8h.md#ab9f0ed6c5ba88e871b0f8cb454283890)#define NUMAKER\_CLK\_CLKSEL4\_UART0SEL\_MIRC 0x00000004

[ 129](numaker__m2l31x__clock_8h.md#a5dcb786e1f054a89aa6b90eb47d23034)#define NUMAKER\_CLK\_CLKSEL4\_UART0SEL\_HIRC48M 0x00000005

[ 130](numaker__m2l31x__clock_8h.md#a5daeb44999b4ab273a1f34a2f57b6f6e)#define NUMAKER\_CLK\_CLKSEL4\_UART1SEL\_HXT 0x00000000

[ 131](numaker__m2l31x__clock_8h.md#ad5790695d490b5b82e0f2b21f214dd2e)#define NUMAKER\_CLK\_CLKSEL4\_UART1SEL\_PLL 0x00000010

[ 132](numaker__m2l31x__clock_8h.md#aea4128c5181416c45f38d739f93f252a)#define NUMAKER\_CLK\_CLKSEL4\_UART1SEL\_LXT 0x00000020

[ 133](numaker__m2l31x__clock_8h.md#a6116786ba1b34609db93b66fa8196fe5)#define NUMAKER\_CLK\_CLKSEL4\_UART1SEL\_HIRC 0x00000030

[ 134](numaker__m2l31x__clock_8h.md#a8a17a9045e3195772f2352a365ede6d8)#define NUMAKER\_CLK\_CLKSEL4\_UART1SEL\_MIRC 0x00000040

[ 135](numaker__m2l31x__clock_8h.md#ac57652ff30d8a05d9aba7dcd8e53c086)#define NUMAKER\_CLK\_CLKSEL4\_UART1SEL\_HIRC48M 0x00000050

[ 136](numaker__m2l31x__clock_8h.md#a6c64fd523f66849a242da21929f82490)#define NUMAKER\_CLK\_CLKSEL4\_UART2SEL\_HXT 0x00000000

[ 137](numaker__m2l31x__clock_8h.md#a8562f2179cfd8b9102ce4bd08269b3fa)#define NUMAKER\_CLK\_CLKSEL4\_UART2SEL\_PLL 0x00000100

[ 138](numaker__m2l31x__clock_8h.md#ab5d5c4484ee7a9925a0021257850b83e)#define NUMAKER\_CLK\_CLKSEL4\_UART2SEL\_LXT 0x00000200

[ 139](numaker__m2l31x__clock_8h.md#a209a2f17eb02c9b1d5862e0bc712739a)#define NUMAKER\_CLK\_CLKSEL4\_UART2SEL\_HIRC 0x00000300

[ 140](numaker__m2l31x__clock_8h.md#a20b81914b6bda3db13b9b21f0c2ee328)#define NUMAKER\_CLK\_CLKSEL4\_UART2SEL\_MIRC 0x00000400

[ 141](numaker__m2l31x__clock_8h.md#a82124d0af166ca786e10e7327c2340d1)#define NUMAKER\_CLK\_CLKSEL4\_UART2SEL\_HIRC48M 0x00000500

[ 142](numaker__m2l31x__clock_8h.md#a8e2c549e21dd88550b98283f3e2b9cce)#define NUMAKER\_CLK\_CLKSEL4\_UART3SEL\_HXT 0x00000000

[ 143](numaker__m2l31x__clock_8h.md#a4fd5cf9b78b3b0b67ce42523e1292f90)#define NUMAKER\_CLK\_CLKSEL4\_UART3SEL\_PLL 0x00001000

[ 144](numaker__m2l31x__clock_8h.md#a8fa0ed7befaebef4cf1b0c5d6d76531d)#define NUMAKER\_CLK\_CLKSEL4\_UART3SEL\_LXT 0x00002000

[ 145](numaker__m2l31x__clock_8h.md#aa33f2b85bd265935d38f2d88e4c37cd2)#define NUMAKER\_CLK\_CLKSEL4\_UART3SEL\_HIRC 0x00003000

[ 146](numaker__m2l31x__clock_8h.md#ac17c547375b3d51c1b6efc9b27c12181)#define NUMAKER\_CLK\_CLKSEL4\_UART3SEL\_MIRC 0x00004000

[ 147](numaker__m2l31x__clock_8h.md#ab36ee9d916474cfa9bb7a40a7da421cd)#define NUMAKER\_CLK\_CLKSEL4\_UART3SEL\_HIRC48M 0x00005000

[ 148](numaker__m2l31x__clock_8h.md#aba0ede117ebbfd04b11b1302be81934c)#define NUMAKER\_CLK\_CLKSEL4\_UART4SEL\_HXT 0x00000000

[ 149](numaker__m2l31x__clock_8h.md#af1f4dfeafc27f80a3088860b3628c9e5)#define NUMAKER\_CLK\_CLKSEL4\_UART4SEL\_PLL 0x00010000

[ 150](numaker__m2l31x__clock_8h.md#acb904b072e944a8867036d3e01587f30)#define NUMAKER\_CLK\_CLKSEL4\_UART4SEL\_LXT 0x00020000

[ 151](numaker__m2l31x__clock_8h.md#a10345434344859abc521fa7d092cb1d7)#define NUMAKER\_CLK\_CLKSEL4\_UART4SEL\_HIRC 0x00030000

[ 152](numaker__m2l31x__clock_8h.md#aeef8e76ac07ac259a984d59629ca69ca)#define NUMAKER\_CLK\_CLKSEL4\_UART4SEL\_MIRC 0x00040000

[ 153](numaker__m2l31x__clock_8h.md#ada536109bc340501837a0a89e8993596)#define NUMAKER\_CLK\_CLKSEL4\_UART4SEL\_HIRC48M 0x00050000

[ 154](numaker__m2l31x__clock_8h.md#af2d6fd4ace5fd8b0eecdb1a81ea97bae)#define NUMAKER\_CLK\_CLKSEL4\_UART5SEL\_HXT 0x00000000

[ 155](numaker__m2l31x__clock_8h.md#a751543c25b5a72e95fef5c1b136dd868)#define NUMAKER\_CLK\_CLKSEL4\_UART5SEL\_PLL 0x00100000

[ 156](numaker__m2l31x__clock_8h.md#a85d7fe667c70205c35400f87f4cbd5b0)#define NUMAKER\_CLK\_CLKSEL4\_UART5SEL\_LXT 0x00200000

[ 157](numaker__m2l31x__clock_8h.md#a94ec880c64c988ee05843c276ff2557a)#define NUMAKER\_CLK\_CLKSEL4\_UART5SEL\_HIRC 0x00300000

[ 158](numaker__m2l31x__clock_8h.md#a12574e05b5f4989426104c0fb8a1a5f7)#define NUMAKER\_CLK\_CLKSEL4\_UART5SEL\_MIRC 0x00400000

[ 159](numaker__m2l31x__clock_8h.md#a042168a58079599a9d104846ea8050cd)#define NUMAKER\_CLK\_CLKSEL4\_UART5SEL\_HIRC48M 0x00500000

[ 160](numaker__m2l31x__clock_8h.md#a70fb1b8afb079fe1f659f44d74c4269d)#define NUMAKER\_CLK\_CLKSEL4\_UART6SEL\_HXT 0x00000000

[ 161](numaker__m2l31x__clock_8h.md#afac0cbdd01f79efefa75d122ef280032)#define NUMAKER\_CLK\_CLKSEL4\_UART6SEL\_PLL 0x01000000

[ 162](numaker__m2l31x__clock_8h.md#ab7520076d80d7b5e313156c3e69f7459)#define NUMAKER\_CLK\_CLKSEL4\_UART6SEL\_LXT 0x02000000

[ 163](numaker__m2l31x__clock_8h.md#a6e2d90cdaf353a1d88e48e22aa05fbe1)#define NUMAKER\_CLK\_CLKSEL4\_UART6SEL\_HIRC 0x03000000

[ 164](numaker__m2l31x__clock_8h.md#a8b837baa242814ed588024eb1803610b)#define NUMAKER\_CLK\_CLKSEL4\_UART6SEL\_MIRC 0x04000000

[ 165](numaker__m2l31x__clock_8h.md#a34695f3ee4b482a0af1bfa6a67b36de4)#define NUMAKER\_CLK\_CLKSEL4\_UART6SEL\_HIRC48M 0x05000000

[ 166](numaker__m2l31x__clock_8h.md#a32d909fd1e8bb7f2a87373ed4c650ec7)#define NUMAKER\_CLK\_CLKSEL4\_UART7SEL\_HXT 0x00000000

[ 167](numaker__m2l31x__clock_8h.md#ad82e5c95c511131bfc7328ad735dbb8c)#define NUMAKER\_CLK\_CLKSEL4\_UART7SEL\_PLL 0x10000000

[ 168](numaker__m2l31x__clock_8h.md#aa58e2d8b9600de1138a8af79eb4e7d72)#define NUMAKER\_CLK\_CLKSEL4\_UART7SEL\_LXT 0x20000000

[ 169](numaker__m2l31x__clock_8h.md#a991f2d749561f500474db752d93e535d)#define NUMAKER\_CLK\_CLKSEL4\_UART7SEL\_HIRC 0x30000000

[ 170](numaker__m2l31x__clock_8h.md#a748a3587549b7cf3c2a3bafe5eb46270)#define NUMAKER\_CLK\_CLKSEL4\_UART7SEL\_MIRC 0x40000000

[ 171](numaker__m2l31x__clock_8h.md#adcffdbaf3833cab1ac37cdaab641f8ed)#define NUMAKER\_CLK\_CLKSEL4\_UART7SEL\_HIRC48M 0x50000000

[ 172](numaker__m2l31x__clock_8h.md#a7791710203e4af03f6f76b909c7b467c)#define NUMAKER\_CLK\_CLKDIV0\_HCLK(x) (((x) - 1UL) << (0))

[ 173](numaker__m2l31x__clock_8h.md#a6c98443d44caab67dc8a0983d1a472ae)#define NUMAKER\_CLK\_CLKDIV0\_HCLK0(x) (((x) - 1UL) << (0))

[ 174](numaker__m2l31x__clock_8h.md#a6ea0c7b58fdbfff2d813f7859a3ac1cd)#define NUMAKER\_CLK\_CLKDIV0\_USB(x) (((x) - 1UL) << (4))

[ 175](numaker__m2l31x__clock_8h.md#a3c7cfbdf43433e075643b8e5f7d8dc5f)#define NUMAKER\_CLK\_CLKDIV0\_UART0(x) (((x) - 1UL) << (8))

[ 176](numaker__m2l31x__clock_8h.md#aa44610811c5e62ed93cf91dc7925eb10)#define NUMAKER\_CLK\_CLKDIV0\_UART1(x) (((x) - 1UL) << (12))

[ 177](numaker__m2l31x__clock_8h.md#a84bca9b50b18d2f260f637d7e58cb369)#define NUMAKER\_CLK\_CLKDIV0\_EADC0(x) (((x) - 1UL) << (16))

[ 178](numaker__m2l31x__clock_8h.md#a5a548de5d860e906f139858512608955)#define NUMAKER\_CLK\_CLKDIV4\_UART2(x) (((x) - 1UL) << (0))

[ 179](numaker__m2l31x__clock_8h.md#aa10601c99a3fc178163dfa652bd2d934)#define NUMAKER\_CLK\_CLKDIV4\_UART3(x) (((x) - 1UL) << (4))

[ 180](numaker__m2l31x__clock_8h.md#a2aaecc74fc40ead21b8ad38bf14fcd81)#define NUMAKER\_CLK\_CLKDIV4\_UART4(x) (((x) - 1UL) << (8))

[ 181](numaker__m2l31x__clock_8h.md#a9444b25128c546730f2f95651d6a6d78)#define NUMAKER\_CLK\_CLKDIV4\_UART5(x) (((x) - 1UL) << (12))

[ 182](numaker__m2l31x__clock_8h.md#a12b519bee17127c49d6aece4dcf9360a)#define NUMAKER\_CLK\_CLKDIV4\_UART6(x) (((x) - 1UL) << (16))

[ 183](numaker__m2l31x__clock_8h.md#acadcdbe15918ca5478c17f30d417aa4a)#define NUMAKER\_CLK\_CLKDIV4\_UART7(x) (((x) - 1UL) << (20))

[ 184](numaker__m2l31x__clock_8h.md#a225dfb2e0f8ce7ae299746ee4242e22f)#define NUMAKER\_CLK\_CLKDIV5\_CANFD0(x) (((x) - 1UL) << (0))

[ 185](numaker__m2l31x__clock_8h.md#a67f5c63a1322683d74d56ee68c193cb4)#define NUMAKER\_CLK\_CLKDIV5\_CANFD1(x) (((x) - 1UL) << (4))

[ 186](numaker__m2l31x__clock_8h.md#a91226a1fd31413d76529f104d209823c)#define NUMAKER\_CLK\_PCLKDIV\_APB0DIV\_DIV1 0x00000000

[ 187](numaker__m2l31x__clock_8h.md#a084853a709e714db6f49d45d45342d37)#define NUMAKER\_CLK\_PCLKDIV\_APB0DIV\_DIV2 0x00000001

[ 188](numaker__m2l31x__clock_8h.md#a87a3393828150a62072a81dd58d2b80f)#define NUMAKER\_CLK\_PCLKDIV\_APB0DIV\_DIV4 0x00000002

[ 189](numaker__m2l31x__clock_8h.md#a43013dc7b87074e5f7606a1e1ac14bce)#define NUMAKER\_CLK\_PCLKDIV\_APB0DIV\_DIV8 0x00000003

[ 190](numaker__m2l31x__clock_8h.md#aac77daf4ae27aeab8c73177be5acdbe8)#define NUMAKER\_CLK\_PCLKDIV\_APB0DIV\_DIV16 0x00000004

[ 191](numaker__m2l31x__clock_8h.md#af5199c68008764c41a3ce9ba27ea24e9)#define NUMAKER\_CLK\_PCLKDIV\_APB1DIV\_DIV1 0x00000000

[ 192](numaker__m2l31x__clock_8h.md#af6cb3de51e49729e92044287ed499105)#define NUMAKER\_CLK\_PCLKDIV\_APB1DIV\_DIV2 0x00000010

[ 193](numaker__m2l31x__clock_8h.md#a8e63b55ca8e84958230453a54f3983b2)#define NUMAKER\_CLK\_PCLKDIV\_APB1DIV\_DIV4 0x00000020

[ 194](numaker__m2l31x__clock_8h.md#a8e59ceb6473e9a050af9efeeeb79c72a)#define NUMAKER\_CLK\_PCLKDIV\_APB1DIV\_DIV8 0x00000030

[ 195](numaker__m2l31x__clock_8h.md#a8e7dec640447de9b571147cbe7fe6e26)#define NUMAKER\_CLK\_PCLKDIV\_APB1DIV\_DIV16 0x00000040

[ 196](numaker__m2l31x__clock_8h.md#a81c0a35692befb3b0427efc7a1e2686e)#define NUMAKER\_PDMA0\_MODULE 0x00000001

[ 197](numaker__m2l31x__clock_8h.md#a9e1a03d652040f0e3d9c0766bfdb2604)#define NUMAKER\_ISP\_MODULE 0x00000002

[ 198](numaker__m2l31x__clock_8h.md#a4380f8998993e0ea2d85260fb9dd8200)#define NUMAKER\_EBI\_MODULE 0x00000003

[ 199](numaker__m2l31x__clock_8h.md#a3e379c3d426c06b772e848633767d2e5)#define NUMAKER\_ST\_MODULE 0x018C0004

[ 200](numaker__m2l31x__clock_8h.md#af7f021090417dc8ba8eac4b2674cf8b8)#define NUMAKER\_CRC\_MODULE 0x00000007

[ 201](numaker__m2l31x__clock_8h.md#a7a2da068169709e20c06f2962569bc46)#define NUMAKER\_CRPT\_MODULE 0x0000000C

[ 202](numaker__m2l31x__clock_8h.md#a3b983a5a538bbf7b2e6288beacfb5427)#define NUMAKER\_KS\_MODULE 0x0000000D

[ 203](numaker__m2l31x__clock_8h.md#a43b0b287abedfd2b9c78857bb0004be9)#define NUMAKER\_USBH\_MODULE 0x00A01090

[ 204](numaker__m2l31x__clock_8h.md#a106a0eb0dac7825f2b6b05a0329c6a3a)#define NUMAKER\_GPA\_MODULE 0x00000018

[ 205](numaker__m2l31x__clock_8h.md#a922653d8eb98a7a175366566506834d6)#define NUMAKER\_GPB\_MODULE 0x00000019

[ 206](numaker__m2l31x__clock_8h.md#a9daa2cdbc788c5e5f3e4cbe29169816f)#define NUMAKER\_GPC\_MODULE 0x0000001A

[ 207](numaker__m2l31x__clock_8h.md#a277e860c7fdd493a496900c32b6085f7)#define NUMAKER\_GPD\_MODULE 0x0000001B

[ 208](numaker__m2l31x__clock_8h.md#a7a5abf84843eb843233e2f24323559f3)#define NUMAKER\_GPE\_MODULE 0x0000001C

[ 209](numaker__m2l31x__clock_8h.md#a19540c109f7a0e276ad7f7f52faf6c7e)#define NUMAKER\_GPF\_MODULE 0x0000001D

[ 210](numaker__m2l31x__clock_8h.md#ad377845a8b368f1b1b6d20f6629dcdd3)#define NUMAKER\_GPG\_MODULE 0x0000001E

[ 211](numaker__m2l31x__clock_8h.md#a74e2344ff20eec0e1ccbd137d75183fb)#define NUMAKER\_GPH\_MODULE 0x0000001F

[ 212](numaker__m2l31x__clock_8h.md#a6216a664ac302a57a0b632754c3fce5f)#define NUMAKER\_RTC\_MODULE 0x20000001

[ 213](numaker__m2l31x__clock_8h.md#adaec43e184ed7f3c34f66b4e98041f62)#define NUMAKER\_TMR0\_MODULE 0x25A00002

[ 214](numaker__m2l31x__clock_8h.md#a50c780a3f2c07cc2dfca1e647e83782d)#define NUMAKER\_TMR1\_MODULE 0x25B00003

[ 215](numaker__m2l31x__clock_8h.md#a7a60853a52958a5c8a78e383f378f579)#define NUMAKER\_TMR2\_MODULE 0x25C00004

[ 216](numaker__m2l31x__clock_8h.md#a42fd788548168d2b519f5d49d2eead47)#define NUMAKER\_TMR3\_MODULE 0x25D00005

[ 217](numaker__m2l31x__clock_8h.md#a913b0eed144c8d228a461dec3f0b49e6)#define NUMAKER\_CLKO\_MODULE 0x26100006

[ 218](numaker__m2l31x__clock_8h.md#abe18bfc9e64be82d3734d80a69e2541c)#define NUMAKER\_ACMP01\_MODULE 0x20000007

[ 219](numaker__m2l31x__clock_8h.md#a8241dce3f2329ef3561277656bd68e7f)#define NUMAKER\_I2C0\_MODULE 0x20000008

[ 220](numaker__m2l31x__clock_8h.md#a08413ee5eed011e452f7352a276b45af)#define NUMAKER\_I2C1\_MODULE 0x20000009

[ 221](numaker__m2l31x__clock_8h.md#a211a7c416249dad417b5971a4c8526fe)#define NUMAKER\_I2C2\_MODULE 0x2000000A

[ 222](numaker__m2l31x__clock_8h.md#a0660bb6481a262632fdfd08f4c65c1db)#define NUMAKER\_I2C3\_MODULE 0x2000000B

[ 223](numaker__m2l31x__clock_8h.md#a6dad02cb850ad26c2afde2291d669808)#define NUMAKER\_QSPI0\_MODULE 0x2908000C

[ 224](numaker__m2l31x__clock_8h.md#adaa689295a31e5b259a7c05b6611a125)#define NUMAKER\_SPI0\_MODULE 0x2990000D

[ 225](numaker__m2l31x__clock_8h.md#a144be66983b8b45995a7b037681477e7)#define NUMAKER\_SPI1\_MODULE 0x29B0000E

[ 226](numaker__m2l31x__clock_8h.md#a227a44ce55b040227bfe3233cfd63467)#define NUMAKER\_SPI2\_MODULE 0x2DA0000F

[ 227](numaker__m2l31x__clock_8h.md#aaf0220a2af6dd7368761bf753ae7b73e)#define NUMAKER\_UART0\_MODULE 0x31801110

[ 228](numaker__m2l31x__clock_8h.md#a38d069ddfd9912c38c42a8f7e3ead763)#define NUMAKER\_UART1\_MODULE 0x31901191

[ 229](numaker__m2l31x__clock_8h.md#aa6dbc85be07f392f38a88bc074f11046)#define NUMAKER\_UART2\_MODULE 0x31A11012

[ 230](numaker__m2l31x__clock_8h.md#a98c5368b7868f6bc68e09df7f479be73)#define NUMAKER\_UART3\_MODULE 0x31B11093

[ 231](numaker__m2l31x__clock_8h.md#a0045544d52c292c13edb09e90f4b16c8)#define NUMAKER\_UART4\_MODULE 0x31C11114

[ 232](numaker__m2l31x__clock_8h.md#a0fdf72d7961da9c046d7d4bb9e19cf1f)#define NUMAKER\_UART5\_MODULE 0x31D11195

[ 233](numaker__m2l31x__clock_8h.md#aa4081c973118f02b92299ea8d775a1e5)#define NUMAKER\_UART6\_MODULE 0x31E11216

[ 234](numaker__m2l31x__clock_8h.md#a86caba0b690236e26e440bc39e4bf4c9)#define NUMAKER\_UART7\_MODULE 0x31F11297

[ 235](numaker__m2l31x__clock_8h.md#ac504259898b6070a12ca5a8eed921e17)#define NUMAKER\_OTG\_MODULE 0x2000001A

[ 236](numaker__m2l31x__clock_8h.md#aa751a53c366beda2ac9b3f5169cd4ace)#define NUMAKER\_USBD\_MODULE 0x20A0109B

[ 237](numaker__m2l31x__clock_8h.md#a46a5cffa974b2f1425d2ced8e678c3e2)#define NUMAKER\_EADC0\_MODULE 0x2128221C

[ 238](numaker__m2l31x__clock_8h.md#a7b544eadd5c042e91ea89541fd9431f6)#define NUMAKER\_TRNG\_MODULE 0x2000001F

[ 239](numaker__m2l31x__clock_8h.md#aa251c8b6a225d24b4e3f20dd22498b79)#define NUMAKER\_SPI3\_MODULE 0x4DB00006

[ 240](numaker__m2l31x__clock_8h.md#a96da4a8ec09af3cbf8ab34e1bccb7819)#define NUMAKER\_USCI0\_MODULE 0x40000008

[ 241](numaker__m2l31x__clock_8h.md#a34aba27dcf1ff17f60bbf4ee5f1e9de4)#define NUMAKER\_USCI1\_MODULE 0x40000009

[ 242](numaker__m2l31x__clock_8h.md#a531cdddd54f1c2a56d603b9135348e0f)#define NUMAKER\_WWDT\_MODULE 0x4578000B

[ 243](numaker__m2l31x__clock_8h.md#a9a5f7dc5dfa877dd92f3952ce7315ba8)#define NUMAKER\_DAC\_MODULE 0x4000000C

[ 244](numaker__m2l31x__clock_8h.md#ab42a9a75250104163dab040657beb440)#define NUMAKER\_EPWM0\_MODULE 0x48800010

[ 245](numaker__m2l31x__clock_8h.md#a686fa9f9995ef124c47ce20de165b74d)#define NUMAKER\_EPWM1\_MODULE 0x48840011

[ 246](numaker__m2l31x__clock_8h.md#a4fe52c877b603a575a230d3de64d2f45)#define NUMAKER\_EQEI0\_MODULE 0x40000016

[ 247](numaker__m2l31x__clock_8h.md#a446b5934e374a30377594e63423018b1)#define NUMAKER\_EQEI1\_MODULE 0x40000017

[ 248](numaker__m2l31x__clock_8h.md#ad0f284b0e2844115b25a23e079eda933)#define NUMAKER\_TK\_MODULE 0x489C0019

[ 249](numaker__m2l31x__clock_8h.md#afcd2263655b3f52378ee24f2f8bfc0d6)#define NUMAKER\_ECAP0\_MODULE 0x4000001A

[ 250](numaker__m2l31x__clock_8h.md#a43cc65940b5464683c572c94650a58e9)#define NUMAKER\_ECAP1\_MODULE 0x4000001B

[ 251](numaker__m2l31x__clock_8h.md#a39d67ff5404e9cbe12c611347bab613b)#define NUMAKER\_ACMP2\_MODULE 0x60000007

[ 252](numaker__m2l31x__clock_8h.md#aeca39176f47a36f10a978e4ee72a980e)#define NUMAKER\_PWM0\_MODULE 0x6C980008

[ 253](numaker__m2l31x__clock_8h.md#a607a54e81ddb9bd8a1666ea70ceeefd2)#define NUMAKER\_PWM1\_MODULE 0x6C9C0009

[ 254](numaker__m2l31x__clock_8h.md#ae81c1c919c104b891181d1ae5a1eadbf)#define NUMAKER\_UTCPD0\_MODULE 0x6000000F

[ 255](numaker__m2l31x__clock_8h.md#a900708a1f046331b4e4899fd8ba38b5d)#define NUMAKER\_CANRAM0\_MODULE 0x80000010

[ 256](numaker__m2l31x__clock_8h.md#a23d5b7214e636fb3b1c99bf5e6c01d53)#define NUMAKER\_CANRAM1\_MODULE 0x80000011

[ 257](numaker__m2l31x__clock_8h.md#aec648b50b3e87890e01766e735130d34)#define NUMAKER\_CANFD0\_MODULE 0x81621014

[ 258](numaker__m2l31x__clock_8h.md#a4cf36800f445d6eab593a8838285d913)#define NUMAKER\_CANFD1\_MODULE 0x816A1095

[ 259](numaker__m2l31x__clock_8h.md#a57bc620f1cd33ea513185ab8e09897a4)#define NUMAKER\_HCLK1\_MODULE 0x81B3101C

[ 260](numaker__m2l31x__clock_8h.md#a64c1a7bdef90c48d7f143204b8868289)#define NUMAKER\_LPPDMA0\_MODULE 0xA0000000

[ 261](numaker__m2l31x__clock_8h.md#a35d969bae4d9b8c592fb91150938eb61)#define NUMAKER\_LPGPIO\_MODULE 0xA0000001

[ 262](numaker__m2l31x__clock_8h.md#a0cc5e160305cd9554b97894ca793bbfb)#define NUMAKER\_LPSRAM\_MODULE 0xA0000002

[ 263](numaker__m2l31x__clock_8h.md#a963952cad9b6b670e736875be75328e2)#define NUMAKER\_WDT\_MODULE 0xB5600010

[ 264](numaker__m2l31x__clock_8h.md#a2cbc8d599f6f30f748c4b7983afadf35)#define NUMAKER\_LPSPI0\_MODULE 0xB5080011

[ 265](numaker__m2l31x__clock_8h.md#a8926f92760ed3299445fde66508c488d)#define NUMAKER\_LPI2C0\_MODULE 0xA0000012

[ 266](numaker__m2l31x__clock_8h.md#acd05c73a03e017ba39c90635b54d4135)#define NUMAKER\_LPUART0\_MODULE 0xB5031113

[ 267](numaker__m2l31x__clock_8h.md#a395998af6b48e4f44dc2896c9fffa4e6)#define NUMAKER\_LPTMR0\_MODULE 0xB5A00014

[ 268](numaker__m2l31x__clock_8h.md#a8a7f92bbf41ade96a93b0947b33bd5ff)#define NUMAKER\_LPTMR1\_MODULE 0xB5B00015

[ 269](numaker__m2l31x__clock_8h.md#a809f2eeb0f49edc25e8b306d7a3ec6f8)#define NUMAKER\_TTMR0\_MODULE 0xB5100016

[ 270](numaker__m2l31x__clock_8h.md#a6256d13006c2c8ef0b5b646bab655047)#define NUMAKER\_TTMR1\_MODULE 0xB5180017

[ 271](numaker__m2l31x__clock_8h.md#ace0ae8a2402639eb64dc3483ba70003d)#define NUMAKER\_LPADC0\_MODULE 0xB5431218

[ 272](numaker__m2l31x__clock_8h.md#abc2d93a396775c339431dd84b22eca82)#define NUMAKER\_OPA\_MODULE 0xA000001B

273

[ 274](numaker__m2l31x__clock_8h.md#a4d0aca792eb3e7b8e6c8ef3b22fad7f9)#define NUMAKER\_CLK\_PMUCTL\_PDMSEL\_PD 0x00000000

[ 275](numaker__m2l31x__clock_8h.md#a6b0f2c2a0c267c09880efaf5044a7d05)#define NUMAKER\_CLK\_PMUCTL\_PDMSEL\_NPD0 0x00000000

[ 276](numaker__m2l31x__clock_8h.md#a670ec51bf07fc725e951d39d3eec737a)#define NUMAKER\_CLK\_PMUCTL\_PDMSEL\_NPD1 0x00000001

[ 277](numaker__m2l31x__clock_8h.md#aa20c40e2fefc000977bd86968248898c)#define NUMAKER\_CLK\_PMUCTL\_PDMSEL\_NPD2 0x00000002

[ 278](numaker__m2l31x__clock_8h.md#a9f655067f52495c052c34f3e7d62753b)#define NUMAKER\_CLK\_PMUCTL\_PDMSEL\_NPD3 0x00000003

[ 279](numaker__m2l31x__clock_8h.md#a0b5e3c3861e4f9253b3c77b40693e350)#define NUMAKER\_CLK\_PMUCTL\_PDMSEL\_NPD4 0x00000004

[ 280](numaker__m2l31x__clock_8h.md#a9e50a75658d457c8f357611f68fa4491)#define NUMAKER\_CLK\_PMUCTL\_PDMSEL\_NPD5 0x00000005

[ 281](numaker__m2l31x__clock_8h.md#ae88a97b51a2016ee79de8eaf20c70fcf)#define NUMAKER\_CLK\_PMUCTL\_PDMSEL\_SPD0 0x00000008

[ 282](numaker__m2l31x__clock_8h.md#a2cd239f9d932f6daa70da52913fe1766)#define NUMAKER\_CLK\_PMUCTL\_PDMSEL\_SPD1 0x00000009

[ 283](numaker__m2l31x__clock_8h.md#ac034ea7f86bb01073d7c2de3fb6bc694)#define NUMAKER\_CLK\_PMUCTL\_PDMSEL\_SPD2 0x0000000A

[ 284](numaker__m2l31x__clock_8h.md#a0c591aa924ae44572a99e799d0b1b57d)#define NUMAKER\_CLK\_PMUCTL\_PDMSEL\_DPD0 0x0000000C

[ 285](numaker__m2l31x__clock_8h.md#a159f858b7fb79398df5d119822fdb0e3)#define NUMAKER\_CLK\_PMUCTL\_PDMSEL\_DPD1 0x0000000D

286

287#endif

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [clock](dir_6e9992ac75fd0b7a50e889108957c907.md)
- [numaker\_m2l31x\_clock.h](numaker__m2l31x__clock_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
