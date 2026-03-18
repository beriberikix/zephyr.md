---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/renesas-ra-icu_8h_source.html
original_path: doxygen/html/renesas-ra-icu_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

renesas-ra-icu.h

[Go to the documentation of this file.](renesas-ra-icu_8h.md)

1/\*

2 \* Copyright (c) 2023 TOKITA Hiroshi <tokita.hiroshi@fujitsu.com>

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_DT\_BINDINGS\_INTERRUPT\_CONTROLLER\_RENESAS\_RA\_ICU\_H\_

8#define ZEPHYR\_DT\_BINDINGS\_INTERRUPT\_CONTROLLER\_RENESAS\_RA\_ICU\_H\_

9

[ 10](renesas-ra-icu_8h.md#a05110d1b8cd06173ab331cc65dba40ca)#define RA\_ICU\_IRQ\_UNSPECIFIED (-1)

11

[ 12](renesas-ra-icu_8h.md#abf57ee5d814699230bd42c83a0c9045f)#define RA\_ICU\_PORT\_IRQ0 (1 << 8)

[ 13](renesas-ra-icu_8h.md#a9634f70b2e7ba85d94f3c89eb508f0a3)#define RA\_ICU\_PORT\_IRQ1 (2 << 8)

[ 14](renesas-ra-icu_8h.md#a9eec5e02aabf9da25e519b2d049dce29)#define RA\_ICU\_PORT\_IRQ2 (3 << 8)

[ 15](renesas-ra-icu_8h.md#a5ca72014b0ef6093a8830cd3134fcb96)#define RA\_ICU\_PORT\_IRQ3 (4 << 8)

[ 16](renesas-ra-icu_8h.md#a511eea99c1c288b58cd90d3992d27821)#define RA\_ICU\_PORT\_IRQ4 (5 << 8)

[ 17](renesas-ra-icu_8h.md#a212fd596f370048148443973191c85a2)#define RA\_ICU\_PORT\_IRQ5 (6 << 8)

[ 18](renesas-ra-icu_8h.md#a26aae8a3213343658ca725de656f4c4b)#define RA\_ICU\_PORT\_IRQ6 (7 << 8)

[ 19](renesas-ra-icu_8h.md#a4dd558196b883fa869bae172b9c462fd)#define RA\_ICU\_PORT\_IRQ7 (8 << 8)

[ 20](renesas-ra-icu_8h.md#a0df06e9ce6a74ffefc4f16cf7fdab1ed)#define RA\_ICU\_PORT\_IRQ8 (9 << 8)

[ 21](renesas-ra-icu_8h.md#ac6d5188afe5ce472a4f1c6791383af63)#define RA\_ICU\_PORT\_IRQ9 (10 << 8)

[ 22](renesas-ra-icu_8h.md#a6960edc44b4e2fa6559b1b082d84cff7)#define RA\_ICU\_PORT\_IRQ10 (11 << 8)

[ 23](renesas-ra-icu_8h.md#aca393b0ad400cedbaa54587fae03e7ef)#define RA\_ICU\_PORT\_IRQ11 (12 << 8)

[ 24](renesas-ra-icu_8h.md#a3ed88347b1d60d0821bca20d3ad30ab5)#define RA\_ICU\_PORT\_IRQ12 (13 << 8)

[ 25](renesas-ra-icu_8h.md#a62d4ea9916be89bc354b25196a352eea)#define RA\_ICU\_PORT\_IRQ14 (15 << 8)

[ 26](renesas-ra-icu_8h.md#a61305c00d1a5290fa26b8b77139422df)#define RA\_ICU\_PORT\_IRQ15 (16 << 8)

[ 27](renesas-ra-icu_8h.md#a1f5e98c5b3754bc664f726bb3f8eff80)#define RA\_ICU\_DMAC0\_INT (17 << 8)

[ 28](renesas-ra-icu_8h.md#a65aaf583aba9ec0d15d4e3a9dc5bf962)#define RA\_ICU\_DMAC1\_INT (18 << 8)

[ 29](renesas-ra-icu_8h.md#a9a5349120699c42ef7d23a2e307a5324)#define RA\_ICU\_DMAC2\_INT (19 << 8)

[ 30](renesas-ra-icu_8h.md#a36710517138f90ce4e4913f516047d7d)#define RA\_ICU\_DMAC3\_INT (20 << 8)

[ 31](renesas-ra-icu_8h.md#a8c8fca9a760f02455fe7d90bac6c59c5)#define RA\_ICU\_DTC\_COMPLETE (21 << 8)

[ 32](renesas-ra-icu_8h.md#a1db1ccfa4a07b33291452bdf0d0e06c3)#define RA\_ICU\_ICU\_SNZCANCEL (23 << 8)

[ 33](renesas-ra-icu_8h.md#a845de92915d21ffc33db540565827e49)#define RA\_ICU\_FCU\_FRDYI (24 << 8)

[ 34](renesas-ra-icu_8h.md#a8f553978cc2639473df512776c5ac917)#define RA\_ICU\_LVD\_LVD1 (25 << 8)

[ 35](renesas-ra-icu_8h.md#a9021c40306177306d8358c7007b712ea)#define RA\_ICU\_LVD\_LVD2 (26 << 8)

[ 36](renesas-ra-icu_8h.md#acd4f7fbf1bfe48dd9aabc291c251069c)#define RA\_ICU\_VBATT\_LVD (27 << 8)

[ 37](renesas-ra-icu_8h.md#a3a95d0e49b745378a08f5af9d8bd076c)#define RA\_ICU\_MOSC\_STOP (28 << 8)

[ 38](renesas-ra-icu_8h.md#aa329c9eade412d1d927ddc3cb2bdd308)#define RA\_ICU\_SYSTEM\_SNZREQ (29 << 8)

[ 39](renesas-ra-icu_8h.md#a8f042698b7657f7bb85b53bba35dd6ff)#define RA\_ICU\_AGT0\_AGTI (30 << 8)

[ 40](renesas-ra-icu_8h.md#a49d3eaf32dc91c8c5db05f5adcb87e28)#define RA\_ICU\_AGT0\_AGTCMAI (31 << 8)

[ 41](renesas-ra-icu_8h.md#aaeb79083b13936e4aa383a6abcdc00cc)#define RA\_ICU\_AGT0\_AGTCMBI (32 << 8)

[ 42](renesas-ra-icu_8h.md#acb788091f2ea8609dbcca283ea171d51)#define RA\_ICU\_AGT1\_AGTI (33 << 8)

[ 43](renesas-ra-icu_8h.md#a439cfa6642b3de3cc0904c05296949a0)#define RA\_ICU\_AGT1\_AGTCMAI (34 << 8)

[ 44](renesas-ra-icu_8h.md#a9e4326fe84596abb9d413a3e2257de21)#define RA\_ICU\_AGT1\_AGTCMBI (35 << 8)

[ 45](renesas-ra-icu_8h.md#adab3ccfa14dc248d70aff5c0f6d8ae96)#define RA\_ICU\_IWDT\_NMIUNDF (36 << 8)

[ 46](renesas-ra-icu_8h.md#ae862b2d094199f06502027841cfc2d8e)#define RA\_ICU\_WDT\_NMIUNDF (37 << 8)

[ 47](renesas-ra-icu_8h.md#a122d35809141c4c5e6259f2c28393843)#define RA\_ICU\_RTC\_ALM (38 << 8)

[ 48](renesas-ra-icu_8h.md#a7603e4b50fa1de24cf62e56a33174cdb)#define RA\_ICU\_RTC\_PRD (39 << 8)

[ 49](renesas-ra-icu_8h.md#ab577778d03f2b84cd0495f475c972a8b)#define RA\_ICU\_RTC\_CUP (40 << 8)

[ 50](renesas-ra-icu_8h.md#af81839a1eccd377d8bec1ba756b7f240)#define RA\_ICU\_ADC140\_ADI (41 << 8)

[ 51](renesas-ra-icu_8h.md#a2c77dc5905fa294db9a873818956bb7e)#define RA\_ICU\_ADC140\_GBADI (42 << 8)

[ 52](renesas-ra-icu_8h.md#ae6ba80b0342805166e3275636f96a975)#define RA\_ICU\_ADC140\_CMPAI (43 << 8)

[ 53](renesas-ra-icu_8h.md#ae8e3a49399174a9dcbd5cfa00eaa0397)#define RA\_ICU\_ADC140\_CMPBI (44 << 8)

[ 54](renesas-ra-icu_8h.md#a22a1f2bb28aa14c479a32acb5ecc3593)#define RA\_ICU\_ADC140\_WCMPM (45 << 8)

[ 55](renesas-ra-icu_8h.md#a772e4cd1e6e2cc9d8fb2c849920e23de)#define RA\_ICU\_ADC140\_WCMPUM (46 << 8)

[ 56](renesas-ra-icu_8h.md#a7fcb585a4700afa50378c7227de7f76a)#define RA\_ICU\_ACMP\_LP0 (47 << 8)

[ 57](renesas-ra-icu_8h.md#a7c95589a42b3f455782383bf45120492)#define RA\_ICU\_ACMP\_LP1 (48 << 8)

[ 58](renesas-ra-icu_8h.md#af1d44243752a66eaca69e2da756057c1)#define RA\_ICU\_USBFS\_D0FIFO (49 << 8)

[ 59](renesas-ra-icu_8h.md#af91ab097f8dac586dbfbb94608248a55)#define RA\_ICU\_USBFS\_D1FIFO (50 << 8)

[ 60](renesas-ra-icu_8h.md#ad29c8fff1390a867d5b8329c8b277ef6)#define RA\_ICU\_USBFS\_USBI (51 << 8)

[ 61](renesas-ra-icu_8h.md#aedfde20ed81105ab5ec6fc9f15ec8e05)#define RA\_ICU\_USBFS\_USBR (52 << 8)

[ 62](renesas-ra-icu_8h.md#a36fcacb08859f5c03b1c5e57f60002be)#define RA\_ICU\_IIC0\_RXI (53 << 8)

[ 63](renesas-ra-icu_8h.md#ad89e311e2b73a95f8538b0d1c58cab93)#define RA\_ICU\_IIC0\_TXI (54 << 8)

[ 64](renesas-ra-icu_8h.md#ac112865a71e86e2c205825ca7023e2ef)#define RA\_ICU\_IIC0\_TEI (55 << 8)

[ 65](renesas-ra-icu_8h.md#a02980d44ee8e6fb0001e3b96de901524)#define RA\_ICU\_IIC0\_EEI (56 << 8)

[ 66](renesas-ra-icu_8h.md#a5b64f6a82170b0fb2eddc4550eaf2d30)#define RA\_ICU\_IIC0\_WUI (57 << 8)

[ 67](renesas-ra-icu_8h.md#a0e3646e3fc840a741143396c21247bf1)#define RA\_ICU\_IIC1\_RXI (58 << 8)

[ 68](renesas-ra-icu_8h.md#a89ace514ee8a7e2e853d1404693fbbaf)#define RA\_ICU\_IIC1\_TXI (59 << 8)

[ 69](renesas-ra-icu_8h.md#a655efa3abcf88cdf9a317e4a08ede63a)#define RA\_ICU\_IIC1\_TEI (60 << 8)

[ 70](renesas-ra-icu_8h.md#afeb973bf4a990c5f638633fc065b4ffc)#define RA\_ICU\_IIC1\_EEI (61 << 8)

[ 71](renesas-ra-icu_8h.md#a7fdce8fba57936a4b41d8f07e6526ea6)#define RA\_ICU\_SSIE0\_SSITXI (62 << 8)

[ 72](renesas-ra-icu_8h.md#a3c629d8751df452f69a2e1861e8792c9)#define RA\_ICU\_SSIE0\_SSIRXI (63 << 8)

73

[ 74](renesas-ra-icu_8h.md#ab93ca169682fe4d055e672751b41a8fe)#define RA\_ICU\_SSIE0\_SSIF (65 << 8)

[ 75](renesas-ra-icu_8h.md#a6ea92496fd64a00934aa691f6a8bc22a)#define RA\_ICU\_CTSU\_CTSUWR (66 << 8)

[ 76](renesas-ra-icu_8h.md#af6898ba11c76bed1c4a0cdad76d20ba3)#define RA\_ICU\_CTSU\_CTSURD (67 << 8)

[ 77](renesas-ra-icu_8h.md#a84a6402b4e036f93bd812bbd56d26e1d)#define RA\_ICU\_CTSU\_CTSUFN (68 << 8)

[ 78](renesas-ra-icu_8h.md#a5f1e16c4b2a19230646186990d5ceacd)#define RA\_ICU\_KEY\_INTKR (69 << 8)

[ 79](renesas-ra-icu_8h.md#a683d069333136f5fbb24c17663af7ecd)#define RA\_ICU\_DOC\_DOPCI (70 << 8)

[ 80](renesas-ra-icu_8h.md#a27b05f6c9ced35cc791814be2274b6e1)#define RA\_ICU\_CAC\_FERRI (71 << 8)

[ 81](renesas-ra-icu_8h.md#abe8540dffaa7fde4a769c5dcb6e88909)#define RA\_ICU\_CAC\_MENDI (72 << 8)

[ 82](renesas-ra-icu_8h.md#a393048af8bba53b9a30b0709ef176f2a)#define RA\_ICU\_CAC\_OVFI (73 << 8)

[ 83](renesas-ra-icu_8h.md#acdbaa104552cbf233bde53efcd1eb005)#define RA\_ICU\_CAN0\_ERS (74 << 8)

[ 84](renesas-ra-icu_8h.md#afbf4bb3cd92d0754da30052533109d09)#define RA\_ICU\_CAN0\_RXF (75 << 8)

[ 85](renesas-ra-icu_8h.md#a90a9552c83ab601ab085fc4899093627)#define RA\_ICU\_CAN0\_TXF (76 << 8)

[ 86](renesas-ra-icu_8h.md#a772e4f5126a0a9d21921d9628cb62f0c)#define RA\_ICU\_CAN0\_RXM (77 << 8)

[ 87](renesas-ra-icu_8h.md#a69ed346adc7bf2b5eff1fe0b19c1747b)#define RA\_ICU\_CAN0\_TXM (78 << 8)

[ 88](renesas-ra-icu_8h.md#a22f873ffc10db62978e25cf7d91d3871)#define RA\_ICU\_IOPORT\_GROUP1 (70 << 8)

[ 89](renesas-ra-icu_8h.md#a15906c3be13ddcf6142b9ee5a4eee25c)#define RA\_ICU\_IOPORT\_GROUP2 (80 << 8)

[ 90](renesas-ra-icu_8h.md#ad4c9cc57137570f05a1d337b2ae2a40b)#define RA\_ICU\_IOPORT\_GROUP3 (81 << 8)

[ 91](renesas-ra-icu_8h.md#a66b119c3f07b02d5fd7f6c667a2a408c)#define RA\_ICU\_IOPORT\_GROUP4 (82 << 8)

[ 92](renesas-ra-icu_8h.md#a3af6611275a7fcd09cabfd0789ba38ca)#define RA\_ICU\_ELC\_SWEVT0 (83 << 8)

[ 93](renesas-ra-icu_8h.md#a8bdb43684613ad8c8662a125eca60e88)#define RA\_ICU\_ELC\_SWEVT1 (84 << 8)

[ 94](renesas-ra-icu_8h.md#a6f1dbea7bc004de5b363f718a026251a)#define RA\_ICU\_POEG\_GROUP0 (85 << 8)

[ 95](renesas-ra-icu_8h.md#a49c84bfba6c3a22c2beb4322f5a43ead)#define RA\_ICU\_POEG\_GROUP1 (86 << 8)

[ 96](renesas-ra-icu_8h.md#abc960a973e57c866f160f9ec7b9ba92d)#define RA\_ICU\_GPT0\_CCMPA (87 << 8)

[ 97](renesas-ra-icu_8h.md#aa24f48cfaff3ecb195a81dfbbc1a8b78)#define RA\_ICU\_GPT0\_CCMPB (88 << 8)

[ 98](renesas-ra-icu_8h.md#a92bbd691fb8021f89ff409d8dd2bc653)#define RA\_ICU\_GPT0\_CMPC (89 << 8)

[ 99](renesas-ra-icu_8h.md#a6bceb7c84c56badb633723ca8056eb3c)#define RA\_ICU\_GPT0\_CMPD (90 << 8)

[ 100](renesas-ra-icu_8h.md#a70c1174ad19f3d3b1208eab7b1d3bf94)#define RA\_ICU\_GPT0\_CMPE (91 << 8)

[ 101](renesas-ra-icu_8h.md#aff592612f2ab1ca87cb74814747a457b)#define RA\_ICU\_GPT0\_CMPF (92 << 8)

[ 102](renesas-ra-icu_8h.md#a724fe9773b21feefc24f15ee8a7e58f9)#define RA\_ICU\_GPT0\_OVF (93 << 8)

[ 103](renesas-ra-icu_8h.md#ae84d498abac538c678c3d3583b778ae1)#define RA\_ICU\_GPT0\_UDF (94 << 8)

[ 104](renesas-ra-icu_8h.md#a4c2b5872a30a00e6e94a6e31058512aa)#define RA\_ICU\_GPT1\_CCMPA (95 << 8)

[ 105](renesas-ra-icu_8h.md#ab7ed649d7b620d85f65df75ecd4cf112)#define RA\_ICU\_GPT1\_CCMPB (96 << 8)

[ 106](renesas-ra-icu_8h.md#adafca2329b13ea0598597d83ede55ba9)#define RA\_ICU\_GPT1\_CMPC (97 << 8)

[ 107](renesas-ra-icu_8h.md#a91342b289d3727ef64a1a6f8e098b0fb)#define RA\_ICU\_GPT1\_CMPD (98 << 8)

[ 108](renesas-ra-icu_8h.md#a2a51c5ae4b499d23bb87b1a01f0513b2)#define RA\_ICU\_GPT1\_CMPE (99 << 8)

[ 109](renesas-ra-icu_8h.md#a3c7c41ee806c4abcff1968c9fc601c73)#define RA\_ICU\_GPT1\_CMPF (100 << 8)

[ 110](renesas-ra-icu_8h.md#a82d9c4f0ed875b67729a14923208ace6)#define RA\_ICU\_GPT1\_OVF (101 << 8)

[ 111](renesas-ra-icu_8h.md#abc03ccf50583476ff2198506c963882c)#define RA\_ICU\_GPT1\_UDF (102 << 8)

[ 112](renesas-ra-icu_8h.md#a3c1cdae0a2e19b36058958513d0c47b5)#define RA\_ICU\_GPT2\_CCMPA (103 << 8)

[ 113](renesas-ra-icu_8h.md#a73efa0bffff7edd948fa160be1740961)#define RA\_ICU\_GPT2\_CCMPB (104 << 8)

[ 114](renesas-ra-icu_8h.md#af5400a5a3e095ed3aab7a9e9f1c2c4fe)#define RA\_ICU\_GPT2\_CMPC (105 << 8)

[ 115](renesas-ra-icu_8h.md#a632b9ddbb69194a961a5fdb30ee30cb0)#define RA\_ICU\_GPT2\_CMPD (106 << 8)

[ 116](renesas-ra-icu_8h.md#ab4e9a907952811b6a3d77b135f74f1f2)#define RA\_ICU\_GPT2\_CMPE (107 << 8)

[ 117](renesas-ra-icu_8h.md#a19247d60bdb100a170560411d68220c3)#define RA\_ICU\_GPT2\_CMPF (108 << 8)

[ 118](renesas-ra-icu_8h.md#a1b61ab091de6164e3229a0b2f0784a2c)#define RA\_ICU\_GPT2\_OVF (109 << 8)

[ 119](renesas-ra-icu_8h.md#a03da6b6d658b9257c9482a061e0f3e86)#define RA\_ICU\_GPT2\_UDF (110 << 8)

[ 120](renesas-ra-icu_8h.md#ad2a6b2bedeaa09018440a386ac9e55fe)#define RA\_ICU\_GPT3\_CCMPA (111 << 8)

[ 121](renesas-ra-icu_8h.md#aa10c6893d943765961d1563ac7927c67)#define RA\_ICU\_GPT3\_CCMPB (112 << 8)

[ 122](renesas-ra-icu_8h.md#a29c110a19c26c80cbfc9d7c72dfdc46a)#define RA\_ICU\_GPT3\_CMPC (113 << 8)

[ 123](renesas-ra-icu_8h.md#a2edafdee7cc1ae27ac7e89b865268ecc)#define RA\_ICU\_GPT3\_CMPD (114 << 8)

[ 124](renesas-ra-icu_8h.md#a737fb57923cf539e0b394a611f2d479d)#define RA\_ICU\_GPT3\_CMPE (115 << 8)

[ 125](renesas-ra-icu_8h.md#a0dd13cf66a2ac04dfc5cd04b9458134d)#define RA\_ICU\_GPT3\_CMPF (116 << 8)

[ 126](renesas-ra-icu_8h.md#a09e1e85f40470f97445d1e3466467e78)#define RA\_ICU\_GPT3\_OVF (117 << 8)

[ 127](renesas-ra-icu_8h.md#a6401f68679d59e7d2f823d578aa0d09f)#define RA\_ICU\_GPT3\_UDF (118 << 8)

[ 128](renesas-ra-icu_8h.md#a5b0f20bffc3b8c81c73f0bff4db482e8)#define RA\_ICU\_GPT4\_CCMPA (119 << 8)

[ 129](renesas-ra-icu_8h.md#a3915190ef9d6fee52b5ea974cd108958)#define RA\_ICU\_GPT4\_CCMPB (120 << 8)

[ 130](renesas-ra-icu_8h.md#a59d23b8099170bf5d39a9e24a6e307cd)#define RA\_ICU\_GPT4\_CMPC (121 << 8)

[ 131](renesas-ra-icu_8h.md#a77d2439b91c1531a6b036402c48bdc7d)#define RA\_ICU\_GPT4\_CMPD (122 << 8)

[ 132](renesas-ra-icu_8h.md#a65cbe53562c584f9501864ca9f0dd9ee)#define RA\_ICU\_GPT4\_CMPE (123 << 8)

[ 133](renesas-ra-icu_8h.md#a42c387bb9ecae74d8309cc27d23cc366)#define RA\_ICU\_GPT4\_CMPF (124 << 8)

[ 134](renesas-ra-icu_8h.md#a69a5adc8d3fff2a9e3a17ef111373f45)#define RA\_ICU\_GPT4\_OVF (125 << 8)

[ 135](renesas-ra-icu_8h.md#a9fbab3d4d84307d4c6fa3e2da498fc97)#define RA\_ICU\_GPT4\_UDF (126 << 8)

[ 136](renesas-ra-icu_8h.md#a1181773ea55d7e8ca49175eb3cbd1b67)#define RA\_ICU\_GPT5\_CCMPA (127 << 8)

[ 137](renesas-ra-icu_8h.md#ab5aaec7beca98b625897c6246fe53a4f)#define RA\_ICU\_GPT5\_CCMPB (128 << 8)

[ 138](renesas-ra-icu_8h.md#ae5de70de6f59d17e541f3b1a8bca1ad4)#define RA\_ICU\_GPT5\_CMPC (129 << 8)

[ 139](renesas-ra-icu_8h.md#aa7e171c4c28d42bb48752969467c9486)#define RA\_ICU\_GPT5\_CMPD (130 << 8)

[ 140](renesas-ra-icu_8h.md#aa97f1ade56929682c09cd961911ea35f)#define RA\_ICU\_GPT5\_CMPE (131 << 8)

[ 141](renesas-ra-icu_8h.md#a6c4830109db82d102493b0d6f35665e5)#define RA\_ICU\_GPT5\_CMPF (132 << 8)

[ 142](renesas-ra-icu_8h.md#a3e78e11631c69002b851c8b7f954cdda)#define RA\_ICU\_GPT5\_OVF (133 << 8)

[ 143](renesas-ra-icu_8h.md#a0214d5b3f38cb748811ef43ae0b05e2f)#define RA\_ICU\_GPT5\_UDF (134 << 8)

[ 144](renesas-ra-icu_8h.md#a88d9c955eb32f5d3aebe899e03390937)#define RA\_ICU\_GPT6\_CCMPA (135 << 8)

[ 145](renesas-ra-icu_8h.md#a0b3302db1a324dc8e3db15f7a36ba1f7)#define RA\_ICU\_GPT6\_CCMPB (136 << 8)

[ 146](renesas-ra-icu_8h.md#a77c8895f454cd23bde726778796faeb0)#define RA\_ICU\_GPT6\_CMPC (137 << 8)

[ 147](renesas-ra-icu_8h.md#a8937da2cd2623c81d36e37606aa2e8e1)#define RA\_ICU\_GPT6\_CMPD (138 << 8)

[ 148](renesas-ra-icu_8h.md#a74b47ae49e1f7cb0e9953c22e4eeebb6)#define RA\_ICU\_GPT6\_CMPE (139 << 8)

[ 149](renesas-ra-icu_8h.md#acf2e84915ff1e285370c8c51edef80fa)#define RA\_ICU\_GPT6\_CMPF (140 << 8)

[ 150](renesas-ra-icu_8h.md#abfa5bc932c09df993e155cbe26a64ab4)#define RA\_ICU\_GPT6\_OVF (141 << 8)

[ 151](renesas-ra-icu_8h.md#ac28fa43dc4bafc56337b03cdd7dacbd4)#define RA\_ICU\_GPT6\_UDF (142 << 8)

[ 152](renesas-ra-icu_8h.md#a62d15d5533793ed893ac6c51c99dc74e)#define RA\_ICU\_GPT7\_CCMPA (143 << 8)

[ 153](renesas-ra-icu_8h.md#a05ba7f7c2f0bc8dd79020f09f0775049)#define RA\_ICU\_GPT7\_CCMPB (144 << 8)

[ 154](renesas-ra-icu_8h.md#a5b7cd277641a1a884c8425dd3d1e220e)#define RA\_ICU\_GPT7\_CMPC (145 << 8)

[ 155](renesas-ra-icu_8h.md#ac746f2a933a3d6d8a05c9c6aa91a4bec)#define RA\_ICU\_GPT7\_CMPD (146 << 8)

[ 156](renesas-ra-icu_8h.md#ae18586a96dec4ddbb4f01effde6b075b)#define RA\_ICU\_GPT7\_CMPE (147 << 8)

[ 157](renesas-ra-icu_8h.md#a2f2fdeabeb0be60b77c8d126b9739466)#define RA\_ICU\_GPT7\_CMPF (148 << 8)

[ 158](renesas-ra-icu_8h.md#a5c7d09aea9a7a77661ac381e6a9905c5)#define RA\_ICU\_GPT7\_OVF (149 << 8)

[ 159](renesas-ra-icu_8h.md#a55b989dad215d7dda3a68625c21e09e3)#define RA\_ICU\_GPT7\_UDF (150 << 8)

[ 160](renesas-ra-icu_8h.md#aed9fa36a8d62f5352ba6f15977021fad)#define RA\_ICU\_GPT\_UVWEDGE (151 << 8)

[ 161](renesas-ra-icu_8h.md#a40c3c9c05e5ad1bb7e87b0432ebff904)#define RA\_ICU\_SCI0\_RXI (152 << 8)

[ 162](renesas-ra-icu_8h.md#a57ba91d0e16e044377c25eb42de3fc49)#define RA\_ICU\_SCI0\_TXI (153 << 8)

[ 163](renesas-ra-icu_8h.md#ac653e1d2f57daa4f68d36cc597e9e602)#define RA\_ICU\_SCI0\_TEI (154 << 8)

[ 164](renesas-ra-icu_8h.md#a4ffde15659be77a80b168566f3bac05f)#define RA\_ICU\_SCI0\_ERI (155 << 8)

[ 165](renesas-ra-icu_8h.md#a182ca7456f2165f1eee38fd3098be08d)#define RA\_ICU\_SCI0\_AM (156 << 8)

[ 166](renesas-ra-icu_8h.md#ac7e0ddd146fd63b5201e4ad9954f1c37)#define RA\_ICU\_SCI0\_RXI\_OR\_ERI (157 << 8)

[ 167](renesas-ra-icu_8h.md#a2f21bbc5eab47e5f5147433eb7b72933)#define RA\_ICU\_SCI1\_RXI (158 << 8)

[ 168](renesas-ra-icu_8h.md#abf7bc3870a83a7a77ae602d564c87ca7)#define RA\_ICU\_SCI1\_TXI (159 << 8)

[ 169](renesas-ra-icu_8h.md#aec719867c9e414e0ca1605919724686a)#define RA\_ICU\_SCI1\_TEI (160 << 8)

[ 170](renesas-ra-icu_8h.md#abb21ea5f21401509523b588ba8b2ef13)#define RA\_ICU\_SCI1\_ERI (161 << 8)

[ 171](renesas-ra-icu_8h.md#add15456ded38a18a65695ecbce3b5260)#define RA\_ICU\_SCI1\_AM (162 << 8)

[ 172](renesas-ra-icu_8h.md#af0804956b3eed5d26bbde37e6e357344)#define RA\_ICU\_SCI2\_RXI (163 << 8)

[ 173](renesas-ra-icu_8h.md#ac1f3bfddffdebbb101bc0359cd6cab49)#define RA\_ICU\_SCI2\_TXI (164 << 8)

[ 174](renesas-ra-icu_8h.md#ab7d61b58fb61724a0233a1b639583e6e)#define RA\_ICU\_SCI2\_TEI (165 << 8)

[ 175](renesas-ra-icu_8h.md#a47ee241b2d274073589caa6927560086)#define RA\_ICU\_SCI2\_ERI (166 << 8)

[ 176](renesas-ra-icu_8h.md#a2e4b682b2dd6b98aab4a2f75efab13fc)#define RA\_ICU\_SCI2\_AM (167 << 8)

[ 177](renesas-ra-icu_8h.md#ab884249dba2c79f8db45c3103d0d226d)#define RA\_ICU\_SCI9\_RXI (168 << 8)

[ 178](renesas-ra-icu_8h.md#a4a346c13f597718642232c2a34e72500)#define RA\_ICU\_SCI9\_TXI (169 << 8)

[ 179](renesas-ra-icu_8h.md#af5bd5bd5bf54e8419f11991b802971d5)#define RA\_ICU\_SCI9\_TEI (170 << 8)

[ 180](renesas-ra-icu_8h.md#a0747a5eef57cfc36ba79eb507600ddcb)#define RA\_ICU\_SCI9\_ERI (171 << 8)

[ 181](renesas-ra-icu_8h.md#ad6392ad85038f9351ec08a15bb64f48a)#define RA\_ICU\_SCI9\_AM (172 << 8)

[ 182](renesas-ra-icu_8h.md#a40180b3f1bf6709fa0ee4c0bea7e1aab)#define RA\_ICU\_SPI0\_SPRI (173 << 8)

[ 183](renesas-ra-icu_8h.md#a19e62564a5b29f7489e44477d1ff9ceb)#define RA\_ICU\_SPI0\_SPTI (174 << 8)

[ 184](renesas-ra-icu_8h.md#a8542542186b2ccddd35d3ea42346c2cc)#define RA\_ICU\_SPI0\_SPII (175 << 8)

[ 185](renesas-ra-icu_8h.md#a2157ac9a24687c1908d7cc61d4a01c8c)#define RA\_ICU\_SPI0\_SPEI (176 << 8)

[ 186](renesas-ra-icu_8h.md#a86c91cfc649778ecd66c8b758cb12889)#define RA\_ICU\_SPI0\_SPTEND (177 << 8)

[ 187](renesas-ra-icu_8h.md#ac6b192a749d09b44078e14e1dd2764a9)#define RA\_ICU\_SPI1\_SPRI (178 << 8)

[ 188](renesas-ra-icu_8h.md#ade2108762cd0b9d5f0667feda347e1fa)#define RA\_ICU\_SPI1\_SPTI (179 << 8)

[ 189](renesas-ra-icu_8h.md#a5cd3019eb2a3ba3628c128ddb913caac)#define RA\_ICU\_SPI1\_SPII (180 << 8)

[ 190](renesas-ra-icu_8h.md#acaafc80142dfa897c6bf279b486790a8)#define RA\_ICU\_SPI1\_SPEI (181 << 8)

[ 191](renesas-ra-icu_8h.md#a3222b0bbdbcc58b5e7ce141a9c4dc3f1)#define RA\_ICU\_SPI1\_SPTEND (182 << 8)

192

193#endif /\* ZEPHYR\_DT\_BINDINGS\_INTERRUPT\_CONTROLLER\_RENESAS\_RA\_ICU\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [interrupt-controller](dir_f11fd9ad294c5739f2cbe07a93c59a1b.md)
- [renesas-ra-icu.h](renesas-ra-icu_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
