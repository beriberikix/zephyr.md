---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/imx943__clock_8h_source.html
original_path: doxygen/html/imx943__clock_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

imx943\_clock.h

[Go to the documentation of this file.](imx943__clock_8h.md)

1/\*

2 \* Copyright 2025 NXP

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_IMX943\_CLOCK\_H\_

8#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_IMX943\_CLOCK\_H\_

9

[ 10](imx943__clock_8h.md#a5cc8d2a60783d52e28210f1c6cbd47da)#define IMX943\_CLK\_32K 1

[ 11](imx943__clock_8h.md#aa61affad9b2500627455c78523ac9938)#define IMX943\_CLK\_24M 2

[ 12](imx943__clock_8h.md#a1a0b7be04707e17ed4f2dd456461e4e5)#define IMX943\_CLK\_FRO 3

[ 13](imx943__clock_8h.md#a6746218af8f074c50a70ea75cfbcdcdf)#define IMX943\_CLK\_SYSPLL1\_VCO 4

[ 14](imx943__clock_8h.md#a9f80b21922b9c163f350c935b1b4e670)#define IMX943\_CLK\_SYSPLL1\_PFD0\_UNGATED 5

[ 15](imx943__clock_8h.md#a18eae7d47c254e2dacad13c918da5c42)#define IMX943\_CLK\_SYSPLL1\_PFD0 6

[ 16](imx943__clock_8h.md#a39fa99e6dce9cd5e4ba9fdac8c02b123)#define IMX943\_CLK\_SYSPLL1\_PFD0\_DIV2 7

[ 17](imx943__clock_8h.md#ad7b130352f353a6b89082b72afbf7046)#define IMX943\_CLK\_SYSPLL1\_PFD1\_UNGATED 8

[ 18](imx943__clock_8h.md#a074d4af37cc31b0f8791a0f0de67d73a)#define IMX943\_CLK\_SYSPLL1\_PFD1 9

[ 19](imx943__clock_8h.md#a5a675e5c492538d957a2217f5d6e1abc)#define IMX943\_CLK\_SYSPLL1\_PFD1\_DIV2 10

[ 20](imx943__clock_8h.md#a56e1ee32be8f11f683e23fa72ab7dee0)#define IMX943\_CLK\_SYSPLL1\_PFD2\_UNGATED 11

[ 21](imx943__clock_8h.md#a90eccde22565231e09253d3d84a5aee7)#define IMX943\_CLK\_SYSPLL1\_PFD2 12

[ 22](imx943__clock_8h.md#a85fc111f9e4330c21a424ce04ccbdffe)#define IMX943\_CLK\_SYSPLL1\_PFD2\_DIV2 13

[ 23](imx943__clock_8h.md#a1701583c45187756b75649c686634a7a)#define IMX943\_CLK\_AUDIOPLL1\_VCO 14

[ 24](imx943__clock_8h.md#a31497502477ff1b5eca79e3458f96c9f)#define IMX943\_CLK\_AUDIOPLL1 15

[ 25](imx943__clock_8h.md#ad8788a607f79f05cb68ec97ddaed4b61)#define IMX943\_CLK\_AUDIOPLL2\_VCO 16

[ 26](imx943__clock_8h.md#a61b5e59ef589bf13e398513e4a0c952b)#define IMX943\_CLK\_AUDIOPLL2 17

[ 27](imx943__clock_8h.md#a41c2a5f846d32f457885d2b4e4d4800f)#define IMX943\_CLK\_RESERVED18 18

[ 28](imx943__clock_8h.md#acc98485ba9fc4440a924c8f4e94ea457)#define IMX943\_CLK\_RESERVED19 19

[ 29](imx943__clock_8h.md#a7f4f753d29700e1e541165c3961520a9)#define IMX943\_CLK\_RESERVED20 20

[ 30](imx943__clock_8h.md#a3e381ca0e9df23bf98d7ee0e40f505b1)#define IMX943\_CLK\_RESERVED21 21

[ 31](imx943__clock_8h.md#a4c79984e936d7dc3b24ca16350f90781)#define IMX943\_CLK\_RESERVED22 22

[ 32](imx943__clock_8h.md#a7c02c7ed3c0b3d209ef0f8a52a6bbefc)#define IMX943\_CLK\_RESERVED23 23

[ 33](imx943__clock_8h.md#adbe6cb0f54a52e9c205f8af9f4239a26)#define IMX943\_CLK\_ENCPLL\_VCO 24

[ 34](imx943__clock_8h.md#ab0f31faff7dd8d93bb774dd06a58bc81)#define IMX943\_CLK\_ENCPLL\_PFD0\_UNGATED 25

[ 35](imx943__clock_8h.md#aa3c6867fb713faa2fcfef9f99cee8067)#define IMX943\_CLK\_ENCPLL\_PFD0 26

[ 36](imx943__clock_8h.md#ae18f4c866c674ef949126de9ce617a07)#define IMX943\_CLK\_ENCPLL\_PFD1\_UNGATED 27

[ 37](imx943__clock_8h.md#ab4af9a67a3cdb9bfa35c8dedf79ecf2b)#define IMX943\_CLK\_ENCPLL\_PFD1 28

[ 38](imx943__clock_8h.md#a3bf8d9e37a15f1dfbe664f10f2ec542f)#define IMX943\_CLK\_ARMPLL\_VCO 29

[ 39](imx943__clock_8h.md#a55a88e6f4d8d31fc83def3362c0a05cb)#define IMX943\_CLK\_ARMPLL\_PFD0\_UNGATED 30

[ 40](imx943__clock_8h.md#af6e2e62d5dab9f20a0161cd1fdccb23c)#define IMX943\_CLK\_ARMPLL\_PFD0 31

[ 41](imx943__clock_8h.md#a132baee6b6a4d832ba94b5e7ef1e01f8)#define IMX943\_CLK\_ARMPLL\_PFD1\_UNGATED 32

[ 42](imx943__clock_8h.md#a8ffda91ddcb9529cceff052db87ae1a4)#define IMX943\_CLK\_ARMPLL\_PFD1 33

[ 43](imx943__clock_8h.md#afcd23091f2d43a93ed7ccede67369bb8)#define IMX943\_CLK\_ARMPLL\_PFD2\_UNGATED 34

[ 44](imx943__clock_8h.md#ab463b90778ad4818692a94065da0f337)#define IMX943\_CLK\_ARMPLL\_PFD2 35

[ 45](imx943__clock_8h.md#a935feae6274d8133da72595ab79b1708)#define IMX943\_CLK\_ARMPLL\_PFD3\_UNGATED 36

[ 46](imx943__clock_8h.md#aa8f0a5508ed3158d75e9ff77211db543)#define IMX943\_CLK\_ARMPLL\_PFD3 37

[ 47](imx943__clock_8h.md#ad61ba8adf2bc44b63ed6592e5639552b)#define IMX943\_CLK\_DRAMPLL\_VCO 38

[ 48](imx943__clock_8h.md#a4e9d7182b22aa86d96952662b3bfbdfc)#define IMX943\_CLK\_DRAMPLL 39

[ 49](imx943__clock_8h.md#a28ff488bccd6e3cc5c340be836d8955b)#define IMX943\_CLK\_HSIOPLL\_VCO 40

[ 50](imx943__clock_8h.md#a364cbb2ff1538a79fa8a4ec54ae7b841)#define IMX943\_CLK\_HSIOPLL 41

[ 51](imx943__clock_8h.md#ae424a93b35e66ac0c5f31aa96ea82228)#define IMX943\_CLK\_LDBPLL\_VCO 42

[ 52](imx943__clock_8h.md#ae5b94d2bfb701f45e4a4252cd8894534)#define IMX943\_CLK\_LDBPLL 43

[ 53](imx943__clock_8h.md#a328079e6165c7afd43457e6269f92902)#define IMX943\_CLK\_EXT1 44

[ 54](imx943__clock_8h.md#a5afaff822b60fe0cf0f68abed046bc92)#define IMX943\_CLK\_EXT2 45

55

[ 56](imx943__clock_8h.md#aaf719333e04da5cf00cfb1d0a8500583)#define IMX943\_CCM\_NUM\_CLK\_SRC 46

57

[ 58](imx943__clock_8h.md#ad7cd58b25dc182abfd07121dccc9c6c0)#define IMX943\_CLK\_ADC (IMX943\_CCM\_NUM\_CLK\_SRC + 0)

[ 59](imx943__clock_8h.md#a7a151d5c10603871341862425aa34a12)#define IMX943\_CLK\_BUSAON (IMX943\_CCM\_NUM\_CLK\_SRC + 1)

[ 60](imx943__clock_8h.md#a33489961e27d8670a33c874820ae2d50)#define IMX943\_CLK\_CAN1 (IMX943\_CCM\_NUM\_CLK\_SRC + 2)

[ 61](imx943__clock_8h.md#afe85650aca105dabe233ce3812648a59)#define IMX943\_CLK\_GLITCHFILTER (IMX943\_CCM\_NUM\_CLK\_SRC + 3)

[ 62](imx943__clock_8h.md#a152333ae4a2c04988f21a2155789727c)#define IMX943\_CLK\_GPT1 (IMX943\_CCM\_NUM\_CLK\_SRC + 4)

[ 63](imx943__clock_8h.md#a23ebd5f51f70b9fcd9b63a0d4d8639b5)#define IMX943\_CLK\_I3C1SLOW (IMX943\_CCM\_NUM\_CLK\_SRC + 5)

[ 64](imx943__clock_8h.md#a956e8adc580c192add3034d2eecca12c)#define IMX943\_CLK\_LPI2C1 (IMX943\_CCM\_NUM\_CLK\_SRC + 6)

[ 65](imx943__clock_8h.md#af74477884fb73c1f2552b489de36523b)#define IMX943\_CLK\_LPI2C2 (IMX943\_CCM\_NUM\_CLK\_SRC + 7)

[ 66](imx943__clock_8h.md#a0f08db46f74db5aae9111a80d63f0790)#define IMX943\_CLK\_LPSPI1 (IMX943\_CCM\_NUM\_CLK\_SRC + 8)

[ 67](imx943__clock_8h.md#adbe88182c80f1d3f0f2cb32c84735590)#define IMX943\_CLK\_LPSPI2 (IMX943\_CCM\_NUM\_CLK\_SRC + 9)

[ 68](imx943__clock_8h.md#ad2e6b757d74634ca564c9b81a086f4b8)#define IMX943\_CLK\_LPTMR1 (IMX943\_CCM\_NUM\_CLK\_SRC + 10)

[ 69](imx943__clock_8h.md#ac124cc83bdbc6d9f65f0838914b44f55)#define IMX943\_CLK\_LPUART1 (IMX943\_CCM\_NUM\_CLK\_SRC + 11)

[ 70](imx943__clock_8h.md#a8961fa33947845eab595fb95608e1e34)#define IMX943\_CLK\_LPUART2 (IMX943\_CCM\_NUM\_CLK\_SRC + 12)

[ 71](imx943__clock_8h.md#af5a030f71a6e73da36bb9e7eb22c2370)#define IMX943\_CLK\_M33 (IMX943\_CCM\_NUM\_CLK\_SRC + 13)

[ 72](imx943__clock_8h.md#a7338471cc7b4ec02679fdd46f2dac734)#define IMX943\_CLK\_M33SYSTICK (IMX943\_CCM\_NUM\_CLK\_SRC + 14)

[ 73](imx943__clock_8h.md#a215e149c4641dbe333550a3249d0865b)#define IMX943\_CLK\_PDM (IMX943\_CCM\_NUM\_CLK\_SRC + 15)

[ 74](imx943__clock_8h.md#a14504ebb49b40869399cf99caf290f5b)#define IMX943\_CLK\_SAI1 (IMX943\_CCM\_NUM\_CLK\_SRC + 16)

[ 75](imx943__clock_8h.md#a283f94017a8bd05e7d14b5ef5b7fe77c)#define IMX943\_CLK\_TPM2 (IMX943\_CCM\_NUM\_CLK\_SRC + 17)

[ 76](imx943__clock_8h.md#a29ffe93c6236feb521b702341ed178c3)#define IMX943\_CLK\_A55 (IMX943\_CCM\_NUM\_CLK\_SRC + 18)

[ 77](imx943__clock_8h.md#ad7a1380c6125a3330525c51a38097684)#define IMX943\_CLK\_A55MTRBUS (IMX943\_CCM\_NUM\_CLK\_SRC + 19)

[ 78](imx943__clock_8h.md#ad636311fa70624ec11da8d3f77bfc510)#define IMX943\_CLK\_A55PERIPH (IMX943\_CCM\_NUM\_CLK\_SRC + 20)

[ 79](imx943__clock_8h.md#ad77830a503aa7391e24704c73d4c889c)#define IMX943\_CLK\_DRAMALT (IMX943\_CCM\_NUM\_CLK\_SRC + 21)

[ 80](imx943__clock_8h.md#a4a62c77a47288bfdd52cdd306608e8c3)#define IMX943\_CLK\_DRAMAPB (IMX943\_CCM\_NUM\_CLK\_SRC + 22)

[ 81](imx943__clock_8h.md#aee20e18be7a33778f5a4b48bcbcbd6b9)#define IMX943\_CLK\_DISPAPB (IMX943\_CCM\_NUM\_CLK\_SRC + 23)

[ 82](imx943__clock_8h.md#a70cd23134a4688ebd7eed71f5eb443fc)#define IMX943\_CLK\_DISPAXI (IMX943\_CCM\_NUM\_CLK\_SRC + 24)

[ 83](imx943__clock_8h.md#a9ac9fdad4deb6f33f051c79bd2ef93a0)#define IMX943\_CLK\_DISPPIX (IMX943\_CCM\_NUM\_CLK\_SRC + 25)

[ 84](imx943__clock_8h.md#a20a703e197acb28b34f18fadabf9b367)#define IMX943\_CLK\_HSIOACSCAN480M (IMX943\_CCM\_NUM\_CLK\_SRC + 26)

[ 85](imx943__clock_8h.md#ac293d7a8b1a99c11ea14d96a321e3ed5)#define IMX943\_CLK\_HSIOACSCAN80M (IMX943\_CCM\_NUM\_CLK\_SRC + 27)

[ 86](imx943__clock_8h.md#a359ba495e00670d5c0e131559cea2e51)#define IMX943\_CLK\_HSIO (IMX943\_CCM\_NUM\_CLK\_SRC + 28)

[ 87](imx943__clock_8h.md#af146612a90a8922f44b4ddd925c231b3)#define IMX943\_CLK\_HSIOPCIEAUX (IMX943\_CCM\_NUM\_CLK\_SRC + 29)

[ 88](imx943__clock_8h.md#a44c9c8b0492c9c3e9ab0aac672a1726b)#define IMX943\_CLK\_HSIOPCIETEST160M (IMX943\_CCM\_NUM\_CLK\_SRC + 30)

[ 89](imx943__clock_8h.md#aecdb540a1dd19b0232b7dc0a9a68fca5)#define IMX943\_CLK\_HSIOPCIETEST400M (IMX943\_CCM\_NUM\_CLK\_SRC + 31)

[ 90](imx943__clock_8h.md#a3cbec0f5cc12d637808dc383118cbc1b)#define IMX943\_CLK\_HSIOPCIETEST500M (IMX943\_CCM\_NUM\_CLK\_SRC + 32)

[ 91](imx943__clock_8h.md#a1154392911b3c115db6b0b85ace8db81)#define IMX943\_CLK\_SIOPCIETEST50M (IMX943\_CCM\_NUM\_CLK\_SRC + 33)

[ 92](imx943__clock_8h.md#aa5737c24f76d5ff00035b8eb4e8e5b07)#define IMX943\_CLK\_SIOPCIETEST60M (IMX943\_CCM\_NUM\_CLK\_SRC + 34)

[ 93](imx943__clock_8h.md#a1694787c41be6d3b5f5e2cdbf892f306)#define IMX943\_CLK\_BUSM70 (IMX943\_CCM\_NUM\_CLK\_SRC + 35)

[ 94](imx943__clock_8h.md#a2bbe09c2055008907ae96ccf0a193741)#define IMX943\_CLK\_M70 (IMX943\_CCM\_NUM\_CLK\_SRC + 36)

[ 95](imx943__clock_8h.md#a050789087a4bf3837eb01d647fb4f80e)#define IMX943\_CLK\_M70SYSTICK (IMX943\_CCM\_NUM\_CLK\_SRC + 37)

[ 96](imx943__clock_8h.md#a36fff4ca80e4dc5ea82a434ccdf13822)#define IMX943\_CLK\_BUSM71 (IMX943\_CCM\_NUM\_CLK\_SRC + 38)

[ 97](imx943__clock_8h.md#a9918a14b6bb499d7645feaaf69ad77c9)#define IMX943\_CLK\_M71 (IMX943\_CCM\_NUM\_CLK\_SRC + 39)

[ 98](imx943__clock_8h.md#a4c495e79cbd709617a7dabc8ef74488c)#define IMX943\_CLK\_M71SYSTICK (IMX943\_CCM\_NUM\_CLK\_SRC + 40)

[ 99](imx943__clock_8h.md#a3f6723250402879253f8c87ea9505641)#define IMX943\_CLK\_BUSNETCMIX (IMX943\_CCM\_NUM\_CLK\_SRC + 41)

[ 100](imx943__clock_8h.md#afcd4c016f96d99bafc58e02205dd84b0)#define IMX943\_CLK\_ECAT (IMX943\_CCM\_NUM\_CLK\_SRC + 42)

[ 101](imx943__clock_8h.md#a657bdd0749bd5a26964a6426201d56aa)#define IMX943\_CLK\_ENET (IMX943\_CCM\_NUM\_CLK\_SRC + 43)

[ 102](imx943__clock_8h.md#a7893207419fe440006dff57fb15eabfb)#define IMX943\_CLK\_ENETPHYTEST200M (IMX943\_CCM\_NUM\_CLK\_SRC + 44)

[ 103](imx943__clock_8h.md#ac1446d34e8d6d7bf085a246263a6e42a)#define IMX943\_CLK\_ENETPHYTEST500M (IMX943\_CCM\_NUM\_CLK\_SRC + 45)

[ 104](imx943__clock_8h.md#ade3787ccedc2cd26c799962df83d7c82)#define IMX943\_CLK\_ENETPHYTEST667M (IMX943\_CCM\_NUM\_CLK\_SRC + 46)

[ 105](imx943__clock_8h.md#a320f738dba8ad818a255cc0114fbf8d9)#define IMX943\_CLK\_ENETREF (IMX943\_CCM\_NUM\_CLK\_SRC + 47)

[ 106](imx943__clock_8h.md#a54fbd27da9997c577caee4420c75e027)#define IMX943\_CLK\_ENETTIMER1 (IMX943\_CCM\_NUM\_CLK\_SRC + 48)

[ 107](imx943__clock_8h.md#a5abd8cd6c0cd9af43ed3b41b432b9874)#define IMX943\_CLK\_ENETTIMER2 (IMX943\_CCM\_NUM\_CLK\_SRC + 49)

[ 108](imx943__clock_8h.md#a8783e0476a616f3f641f94b3cd80105e)#define IMX943\_CLK\_ENETTIMER3 (IMX943\_CCM\_NUM\_CLK\_SRC + 50)

[ 109](imx943__clock_8h.md#a7420b726f04925ae030418d871ddb0bd)#define IMX943\_CLK\_FLEXIO3 (IMX943\_CCM\_NUM\_CLK\_SRC + 51)

[ 110](imx943__clock_8h.md#a4b1ad7d022c42e9197210229c4f6d5fa)#define IMX943\_CLK\_FLEXIO4 (IMX943\_CCM\_NUM\_CLK\_SRC + 52)

[ 111](imx943__clock_8h.md#a694696a8c1ab7248e46ee539cdaec77f)#define IMX943\_CLK\_M33SYNC (IMX943\_CCM\_NUM\_CLK\_SRC + 53)

[ 112](imx943__clock_8h.md#ad1b6b97a0a39b468a348f3d831043b17)#define IMX943\_CLK\_M33SYNCSYSTICK (IMX943\_CCM\_NUM\_CLK\_SRC + 54)

[ 113](imx943__clock_8h.md#a63b376aade1f2876ef1b1dc9ac2ca8c0)#define IMX943\_CLK\_MAC0 (IMX943\_CCM\_NUM\_CLK\_SRC + 55)

[ 114](imx943__clock_8h.md#a460a9bf4c79516be7707ddfdcfc3b852)#define IMX943\_CLK\_MAC1 (IMX943\_CCM\_NUM\_CLK\_SRC + 56)

[ 115](imx943__clock_8h.md#a2a3edeffa6c0174b52151908b9d73a55)#define IMX943\_CLK\_MAC2 (IMX943\_CCM\_NUM\_CLK\_SRC + 57)

[ 116](imx943__clock_8h.md#aabed72b66a10827e8647391247b91273)#define IMX943\_CLK\_MAC3 (IMX943\_CCM\_NUM\_CLK\_SRC + 58)

[ 117](imx943__clock_8h.md#a0b3254be7bcf02f87c887cffcab5032b)#define IMX943\_CLK\_MAC4 (IMX943\_CCM\_NUM\_CLK\_SRC + 59)

[ 118](imx943__clock_8h.md#abc02b3936e963c048d6174e8f9de3ac6)#define IMX943\_CLK\_MAC5 (IMX943\_CCM\_NUM\_CLK\_SRC + 60)

[ 119](imx943__clock_8h.md#a76f8eb266931f55be6e197b8fabed939)#define IMX943\_CLK\_NOCAPB (IMX943\_CCM\_NUM\_CLK\_SRC + 61)

[ 120](imx943__clock_8h.md#a2fa2ec3fa7ff7314b20e43398b8ddbb8)#define IMX943\_CLK\_NOC (IMX943\_CCM\_NUM\_CLK\_SRC + 62)

[ 121](imx943__clock_8h.md#a29d5a4ea0b845a44f2c3e5be6187d25a)#define IMX943\_CLK\_NPUAPB (IMX943\_CCM\_NUM\_CLK\_SRC + 63)

[ 122](imx943__clock_8h.md#a819b9b0228eca351dc18277ab21724c8)#define IMX943\_CLK\_NPU (IMX943\_CCM\_NUM\_CLK\_SRC + 64)

[ 123](imx943__clock_8h.md#a386ae824887a74250f330cf29662273e)#define IMX943\_CLK\_CCMCKO1 (IMX943\_CCM\_NUM\_CLK\_SRC + 65)

[ 124](imx943__clock_8h.md#a4771fda8068416c4d16cbe5e83c09bfe)#define IMX943\_CLK\_CCMCKO2 (IMX943\_CCM\_NUM\_CLK\_SRC + 66)

[ 125](imx943__clock_8h.md#ae5b29767cc504d5c49060a24d71c3ff9)#define IMX943\_CLK\_CCMCKO3 (IMX943\_CCM\_NUM\_CLK\_SRC + 67)

[ 126](imx943__clock_8h.md#adca19b81a2d7c47e7aba9a966535b6df)#define IMX943\_CLK\_CCMCKO4 (IMX943\_CCM\_NUM\_CLK\_SRC + 68)

[ 127](imx943__clock_8h.md#a3f25a5253ef7477992cf7aee69a62c59)#define IMX943\_CLK\_BISS (IMX943\_CCM\_NUM\_CLK\_SRC + 69)

[ 128](imx943__clock_8h.md#a7ee7ba3d6933532eee516ee87aad94ee)#define IMX943\_CLK\_BUSWAKEUP (IMX943\_CCM\_NUM\_CLK\_SRC + 70)

[ 129](imx943__clock_8h.md#ad4377e5089f5b0f7e6e7e9193ce25db0)#define IMX943\_CLK\_CAN2 (IMX943\_CCM\_NUM\_CLK\_SRC + 71)

[ 130](imx943__clock_8h.md#ad486251c22a38ea8f9600890a7ffed59)#define IMX943\_CLK\_CAN3 (IMX943\_CCM\_NUM\_CLK\_SRC + 72)

[ 131](imx943__clock_8h.md#ab39a86216205321ab430d366869ab543)#define IMX943\_CLK\_CAN4 (IMX943\_CCM\_NUM\_CLK\_SRC + 73)

[ 132](imx943__clock_8h.md#acb19a25a53fd114a74b5e998228d9225)#define IMX943\_CLK\_CAN5 (IMX943\_CCM\_NUM\_CLK\_SRC + 74)

[ 133](imx943__clock_8h.md#adf4816d44063a9b10e048b944d1d9c73)#define IMX943\_CLK\_ENDAT21 (IMX943\_CCM\_NUM\_CLK\_SRC + 75)

[ 134](imx943__clock_8h.md#ab1641e44aaaeb5d3f2462e01c1d34871)#define IMX943\_CLK\_ENDAT22 (IMX943\_CCM\_NUM\_CLK\_SRC + 76)

[ 135](imx943__clock_8h.md#a58e56f89925b09e52541f5881ec27041)#define IMX943\_CLK\_ENDAT31FAST (IMX943\_CCM\_NUM\_CLK\_SRC + 77)

[ 136](imx943__clock_8h.md#a121e2e9262d29391939f87fc60a95496)#define IMX943\_CLK\_ENDAT31SLOW (IMX943\_CCM\_NUM\_CLK\_SRC + 78)

[ 137](imx943__clock_8h.md#a1eed67ebb3284f1f38605f363fd0bc20)#define IMX943\_CLK\_FLEXIO1 (IMX943\_CCM\_NUM\_CLK\_SRC + 79)

[ 138](imx943__clock_8h.md#a0bc6670e9582fb23ea801b5254b1e1fd)#define IMX943\_CLK\_FLEXIO2 (IMX943\_CCM\_NUM\_CLK\_SRC + 80)

[ 139](imx943__clock_8h.md#aeebd05471404dc4d99a89ddfa8fc0a67)#define IMX943\_CLK\_GPT2 (IMX943\_CCM\_NUM\_CLK\_SRC + 81)

[ 140](imx943__clock_8h.md#a7514631125f7f5def42e24b74c50ff32)#define IMX943\_CLK\_GPT3 (IMX943\_CCM\_NUM\_CLK\_SRC + 82)

[ 141](imx943__clock_8h.md#a8a12a28fbd0d7635195a33ea69f09a54)#define IMX943\_CLK\_GPT4 (IMX943\_CCM\_NUM\_CLK\_SRC + 83)

[ 142](imx943__clock_8h.md#af1e7f5b9fbf0ecd42238885c00d09304)#define IMX943\_CLK\_HIPERFACE1 (IMX943\_CCM\_NUM\_CLK\_SRC + 84)

[ 143](imx943__clock_8h.md#a0da89f3f3ce234938de90fa823a425e3)#define IMX943\_CLK\_HIPERFACE1SYNC (IMX943\_CCM\_NUM\_CLK\_SRC + 85)

[ 144](imx943__clock_8h.md#a5ea101c87cb8d4bc396c78c262b1343e)#define IMX943\_CLK\_HIPERFACE2 (IMX943\_CCM\_NUM\_CLK\_SRC + 86)

[ 145](imx943__clock_8h.md#ac35aeff775985edca71822d150e66f41)#define IMX943\_CLK\_HIPERFACE2SYNC (IMX943\_CCM\_NUM\_CLK\_SRC + 87)

[ 146](imx943__clock_8h.md#a940115a73af4a2757eca88511b05269f)#define IMX943\_CLK\_I3C2SLOW (IMX943\_CCM\_NUM\_CLK\_SRC + 88)

[ 147](imx943__clock_8h.md#a287bba62e25b4085a01b91e171a14503)#define IMX943\_CLK\_LPI2C3 (IMX943\_CCM\_NUM\_CLK\_SRC + 89)

[ 148](imx943__clock_8h.md#a16503f0eb0951394232b78f306f3f6e5)#define IMX943\_CLK\_LPI2C4 (IMX943\_CCM\_NUM\_CLK\_SRC + 90)

[ 149](imx943__clock_8h.md#a2754cc207e89b849cc6936d9a77034a2)#define IMX943\_CLK\_LPI2C5 (IMX943\_CCM\_NUM\_CLK\_SRC + 91)

[ 150](imx943__clock_8h.md#a9ecab4f4283abcd040cf811796a8745b)#define IMX943\_CLK\_LPI2C6 (IMX943\_CCM\_NUM\_CLK\_SRC + 92)

[ 151](imx943__clock_8h.md#a4da33fca5227ff388a67813b900c6f68)#define IMX943\_CLK\_LPI2C7 (IMX943\_CCM\_NUM\_CLK\_SRC + 93)

[ 152](imx943__clock_8h.md#a64724462eacf1f6cb9530b358d8155a8)#define IMX943\_CLK\_LPI2C8 (IMX943\_CCM\_NUM\_CLK\_SRC + 94)

[ 153](imx943__clock_8h.md#a64b22eec03cc862f958d6dca1fe3fefe)#define IMX943\_CLK\_LPSPI3 (IMX943\_CCM\_NUM\_CLK\_SRC + 95)

[ 154](imx943__clock_8h.md#a141c0a3ded06a0a2c999c7420183939d)#define IMX943\_CLK\_LPSPI4 (IMX943\_CCM\_NUM\_CLK\_SRC + 96)

[ 155](imx943__clock_8h.md#a766474d549c3e9318615001345d2d9fd)#define IMX943\_CLK\_LPSPI5 (IMX943\_CCM\_NUM\_CLK\_SRC + 97)

[ 156](imx943__clock_8h.md#ac4d3842a61b70cb5b7d99e6262170ad8)#define IMX943\_CLK\_LPSPI6 (IMX943\_CCM\_NUM\_CLK\_SRC + 98)

[ 157](imx943__clock_8h.md#a34fe6d52d0a3428a0bf8301a85124ef8)#define IMX943\_CLK\_LPSPI7 (IMX943\_CCM\_NUM\_CLK\_SRC + 99)

[ 158](imx943__clock_8h.md#a89f2149f25f5db8f7da9f09e73f10813)#define IMX943\_CLK\_LPSPI8 (IMX943\_CCM\_NUM\_CLK\_SRC + 100)

[ 159](imx943__clock_8h.md#a4f765a75a486f761d7265fdfdd5b09d4)#define IMX943\_CLK\_LPTMR2 (IMX943\_CCM\_NUM\_CLK\_SRC + 101)

[ 160](imx943__clock_8h.md#a714fabf3fc0c0a1919dc80b17d0877a8)#define IMX943\_CLK\_LPUART10 (IMX943\_CCM\_NUM\_CLK\_SRC + 102)

[ 161](imx943__clock_8h.md#ac29b7003a0f6636f1229f96c09e8d974)#define IMX943\_CLK\_LPUART11 (IMX943\_CCM\_NUM\_CLK\_SRC + 103)

[ 162](imx943__clock_8h.md#a4f86a574c0e599c03e4d2c2cc5b84404)#define IMX943\_CLK\_LPUART12 (IMX943\_CCM\_NUM\_CLK\_SRC + 104)

[ 163](imx943__clock_8h.md#a7408c14ed5bacc80441f7656788a55b3)#define IMX943\_CLK\_LPUART3 (IMX943\_CCM\_NUM\_CLK\_SRC + 105)

[ 164](imx943__clock_8h.md#a2b668c2ce278b3b0c089231fbc03429a)#define IMX943\_CLK\_LPUART4 (IMX943\_CCM\_NUM\_CLK\_SRC + 106)

[ 165](imx943__clock_8h.md#ae83fa5844ca35ef39f5da03343521591)#define IMX943\_CLK\_LPUART5 (IMX943\_CCM\_NUM\_CLK\_SRC + 107)

[ 166](imx943__clock_8h.md#aa98f4395e1594c9fc437569d9306126d)#define IMX943\_CLK\_LPUART6 (IMX943\_CCM\_NUM\_CLK\_SRC + 108)

[ 167](imx943__clock_8h.md#a7a1f697d798cf83be6be15c011af5976)#define IMX943\_CLK\_LPUART7 (IMX943\_CCM\_NUM\_CLK\_SRC + 109)

[ 168](imx943__clock_8h.md#a4d2600d9606770db82f67c756fdaac44)#define IMX943\_CLK\_LPUART8 (IMX943\_CCM\_NUM\_CLK\_SRC + 110)

[ 169](imx943__clock_8h.md#ae86f544de1b15ee45a7f4a33a025f9d3)#define IMX943\_CLK\_LPUART9 (IMX943\_CCM\_NUM\_CLK\_SRC + 111)

[ 170](imx943__clock_8h.md#a7826e81d741158f141b357d4db469235)#define IMX943\_CLK\_SAI2 (IMX943\_CCM\_NUM\_CLK\_SRC + 112)

[ 171](imx943__clock_8h.md#acca94d23d3a7a02c16f17b151c14b9aa)#define IMX943\_CLK\_SAI3 (IMX943\_CCM\_NUM\_CLK\_SRC + 113)

[ 172](imx943__clock_8h.md#ad17ef054e4dd800b3cab1da6e4803e66)#define IMX943\_CLK\_SAI4 (IMX943\_CCM\_NUM\_CLK\_SRC + 114)

[ 173](imx943__clock_8h.md#aab4698e9c1056dcf24f6440e99c57c7e)#define IMX943\_CLK\_SWOTRACE (IMX943\_CCM\_NUM\_CLK\_SRC + 115)

[ 174](imx943__clock_8h.md#a7be73b5924c462438aef4c3a30822d7d)#define IMX943\_CLK\_TPM4 (IMX943\_CCM\_NUM\_CLK\_SRC + 116)

[ 175](imx943__clock_8h.md#a00a0a70957a0ed1d667f275344d36c1c)#define IMX943\_CLK\_TPM5 (IMX943\_CCM\_NUM\_CLK\_SRC + 117)

[ 176](imx943__clock_8h.md#a19222a7e605502a70265bef2924d3b7f)#define IMX943\_CLK\_TPM6 (IMX943\_CCM\_NUM\_CLK\_SRC + 118)

[ 177](imx943__clock_8h.md#ab5cf2f84a44a8dbe77723a1c13f899d2)#define IMX943\_CLK\_USBPHYBURUNIN (IMX943\_CCM\_NUM\_CLK\_SRC + 119)

[ 178](imx943__clock_8h.md#a18b8a4bb6fb110f06976b09d3994c644)#define IMX943\_CLK\_USDHC1 (IMX943\_CCM\_NUM\_CLK\_SRC + 120)

[ 179](imx943__clock_8h.md#a3529dc2bcf73202cb4eb09e0d4eca0cd)#define IMX943\_CLK\_USDHC2 (IMX943\_CCM\_NUM\_CLK\_SRC + 121)

[ 180](imx943__clock_8h.md#a0f75ad589e70ec7778ad8eb0a0f13af9)#define IMX943\_CLK\_USDHC3 (IMX943\_CCM\_NUM\_CLK\_SRC + 122)

[ 181](imx943__clock_8h.md#a5cdc58f486857a620874121258f4946c)#define IMX943\_CLK\_V2XPK (IMX943\_CCM\_NUM\_CLK\_SRC + 123)

[ 182](imx943__clock_8h.md#af33cf313bb79d200dc96d1c25cbb8274)#define IMX943\_CLK\_WAKEUPAXI (IMX943\_CCM\_NUM\_CLK\_SRC + 124)

[ 183](imx943__clock_8h.md#a345af4295ce62fa3f311ac31e12ea124)#define IMX943\_CLK\_XSPISLVROOT (IMX943\_CCM\_NUM\_CLK\_SRC + 125)

[ 184](imx943__clock_8h.md#a6ca5c7dcdc2bf90adfe43b04043bcc2a)#define IMX943\_CLK\_XSPI1 (IMX943\_CCM\_NUM\_CLK\_SRC + 126)

[ 185](imx943__clock_8h.md#a4713597bd0e2607e7a9177451bfd4c8e)#define IMX943\_CLK\_XSPI2 (IMX943\_CCM\_NUM\_CLK\_SRC + 127)

186

187#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_IMX943\_CLOCK\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [clock](dir_6e9992ac75fd0b7a50e889108957c907.md)
- [imx943\_clock.h](imx943__clock_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
