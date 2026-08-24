---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/ite-it51xxx-intc_8h_source.html
original_path: doxygen/html/ite-it51xxx-intc_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ite-it51xxx-intc.h

[Go to the documentation of this file.](ite-it51xxx-intc_8h.md)

1/\*

2 \* Copyright (c) 2025 ITE Corporation. All Rights Reserved.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_INTERRUPT\_CONTROLLER\_ITE\_INTC\_H\_

8#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_INTERRUPT\_CONTROLLER\_ITE\_INTC\_H\_

9

[ 10](ite-it51xxx-intc_8h.md#a9290a5f35a4d3514237ba9fb00936859)#define IRQ\_TYPE\_NONE 0

[ 11](ite-it51xxx-intc_8h.md#ac95cadb7e2fafe537f8be5274baa1e75)#define IRQ\_TYPE\_EDGE\_RISING 1

[ 12](ite-it51xxx-intc_8h.md#aab03b1a63f7cd7f3a43353048655135a)#define IRQ\_TYPE\_EDGE\_FALLING 2

[ 13](ite-it51xxx-intc_8h.md#a377225dde978048e3d918cedba2c125e)#define IRQ\_TYPE\_EDGE\_BOTH (IRQ\_TYPE\_EDGE\_FALLING | IRQ\_TYPE\_EDGE\_RISING)

[ 14](ite-it51xxx-intc_8h.md#a82fc9c68723b62cf4071203f54bd321b)#define IRQ\_TYPE\_LEVEL\_HIGH 4

[ 15](ite-it51xxx-intc_8h.md#adfb5a6f2364155f99a90fba88ff9a670)#define IRQ\_TYPE\_LEVEL\_LOW 8

16

17/\* IRQ numbers of WUC \*/

18/\* Group 0 of INTC \*/

[ 19](ite-it51xxx-intc_8h.md#a1bd9ea3edc79e9584e9bc260bdedf2ab)#define IT51XXX\_IRQ\_WU20 1

[ 20](ite-it51xxx-intc_8h.md#aacb758fc7908b24ef63b2ec198522e34)#define IT51XXX\_IRQ\_KBC\_OBE 2

[ 21](ite-it51xxx-intc_8h.md#a2e0a412bf3d3ca8b8cfef268630f8e03)#define IT51XXX\_IRQ\_SMB\_D 4

[ 22](ite-it51xxx-intc_8h.md#a6f59cc673117062961e9b6d625ac6f5f)#define IT51XXX\_IRQ\_WKINTD 5

[ 23](ite-it51xxx-intc_8h.md#a2fb3c8770a2af10e03c295117335e6c4)#define IT51XXX\_IRQ\_WU23 6

24/\* Group 1 \*/

[ 25](ite-it51xxx-intc_8h.md#a48dc8e3c6bdfe08aeea02d81da7dfa63)#define IT51XXX\_IRQ\_SMB\_A 9

[ 26](ite-it51xxx-intc_8h.md#aab9f42d55277e2f5e6090a89ad339906)#define IT51XXX\_IRQ\_SMB\_B 10

[ 27](ite-it51xxx-intc_8h.md#a9e030083506874c6553b807fd7d72ad9)#define IT51XXX\_IRQ\_WU26 12

[ 28](ite-it51xxx-intc_8h.md#a18e8b286b05048957bb47f74fb67a364)#define IT51XXX\_IRQ\_WKINTC 13

[ 29](ite-it51xxx-intc_8h.md#ada00c64e4d7a21a63c4233caaf982c36)#define IT51XXX\_IRQ\_WU25 14

30/\* Group 2 \*/

[ 31](ite-it51xxx-intc_8h.md#ae7070e00ef2980b55e8453057954ca93)#define IT51XXX\_IRQ\_SMB\_C 16

[ 32](ite-it51xxx-intc_8h.md#ac79fe3fa0f5d888e67659b2fac11c824)#define IT51XXX\_IRQ\_WU24 17

[ 33](ite-it51xxx-intc_8h.md#acf15edcfe3b3345a23032fefaed27e69)#define IT51XXX\_IRQ\_WU22 21

34/\* Group 3 \*/

[ 35](ite-it51xxx-intc_8h.md#ae2accc4b4816ee2580cb2802686dc2f6)#define IT51XXX\_IRQ\_KBC\_IBF 24

[ 36](ite-it51xxx-intc_8h.md#a198b2275166c27e6781d14841ca3ba97)#define IT51XXX\_IRQ\_PMC1\_IBF 25

[ 37](ite-it51xxx-intc_8h.md#acf65f7e32721d9231a565d8131bad770)#define IT51XXX\_IRQ\_PMC2\_IBF 27

[ 38](ite-it51xxx-intc_8h.md#ad56cb3d55328f4aaeb96411a912a3347)#define IT51XXX\_IRQ\_TIMER1 30

[ 39](ite-it51xxx-intc_8h.md#a1900defd3b4a23c2a19c25c113b2d691)#define IT51XXX\_IRQ\_WU21 31

40/\* Group 4 \*/

[ 41](ite-it51xxx-intc_8h.md#a07eeb5cc1ae5b73f91ce828cbd9451a8)#define IT51XXX\_IRQ\_SPI 37

42/\* Group 5 \*/

[ 43](ite-it51xxx-intc_8h.md#a8d1ddae9ca1a4b7035f19647d1438589)#define IT51XXX\_IRQ\_WU50 40

[ 44](ite-it51xxx-intc_8h.md#a92d027bb989bda813964f17832902b11)#define IT51XXX\_IRQ\_WU51 41

[ 45](ite-it51xxx-intc_8h.md#a731e3e2cfce359c9a2f0040a4a94cbd3)#define IT51XXX\_IRQ\_WU52 42

[ 46](ite-it51xxx-intc_8h.md#abd748c80cea3b56d183c0a9c4f0c3c9a)#define IT51XXX\_IRQ\_WU53 43

[ 47](ite-it51xxx-intc_8h.md#af48dd974da667ab231cdc18f3feaa251)#define IT51XXX\_IRQ\_WU54 44

[ 48](ite-it51xxx-intc_8h.md#a064ae1cc0c5ec0f249fbd2d6e1e0f70f)#define IT51XXX\_IRQ\_WU55 45

[ 49](ite-it51xxx-intc_8h.md#a36f49197d820a024e3ab3684bedc414d)#define IT51XXX\_IRQ\_WU56 46

[ 50](ite-it51xxx-intc_8h.md#a7245dc3295c00844799011c7b34714fc)#define IT51XXX\_IRQ\_WU57 47

51/\* Group 6 \*/

[ 52](ite-it51xxx-intc_8h.md#ae8b3f9cd8fa478093f494b7aa2ff5b91)#define IT51XXX\_IRQ\_WU60 48

[ 53](ite-it51xxx-intc_8h.md#ac391efd2f7283026c3d75b4542c05ef1)#define IT51XXX\_IRQ\_WU61 49

[ 54](ite-it51xxx-intc_8h.md#ab8f17a3cbadce21886c20abe75fffc78)#define IT51XXX\_IRQ\_WU62 50

[ 55](ite-it51xxx-intc_8h.md#a9df1dfa62b7e8250e7e6723b7b6ff337)#define IT51XXX\_IRQ\_WU63 51

[ 56](ite-it51xxx-intc_8h.md#a4c3502581103d480d3f053dff872c8ea)#define IT51XXX\_IRQ\_WU64 52

[ 57](ite-it51xxx-intc_8h.md#ac1f10125b96238e29e03c405e62e20a3)#define IT51XXX\_IRQ\_WU65 53

[ 58](ite-it51xxx-intc_8h.md#ae0f32c3f17f670d6ec70e12e89102bb2)#define IT51XXX\_IRQ\_WU66 54

[ 59](ite-it51xxx-intc_8h.md#a4b414ec5990e57faeb8e3b56cec853bc)#define IT51XXX\_IRQ\_WU67 55

60/\* Group 7 \*/

[ 61](ite-it51xxx-intc_8h.md#a503ec871ea49a5d2e4b96e5effb41da9)#define IT51XXX\_IRQ\_TIMER2 58

62/\* Group 9 \*/

[ 63](ite-it51xxx-intc_8h.md#af8cf4838b02d059e685530ffedf93bfa)#define IT51XXX\_IRQ\_WU70 72

[ 64](ite-it51xxx-intc_8h.md#a9fd08d907faf689ecd778ab62356ea57)#define IT51XXX\_IRQ\_WU71 73

[ 65](ite-it51xxx-intc_8h.md#a4f2ea344998a12cb1180b31d1566c938)#define IT51XXX\_IRQ\_WU72 74

[ 66](ite-it51xxx-intc_8h.md#a64da2ea6e069ab31f161d54fbb6261c9)#define IT51XXX\_IRQ\_WU73 75

[ 67](ite-it51xxx-intc_8h.md#af5d3ea451601aeb1f68770dda46cca65)#define IT51XXX\_IRQ\_WU74 76

[ 68](ite-it51xxx-intc_8h.md#a73a7bc4fa0e4387bba05c432930a038b)#define IT51XXX\_IRQ\_WU75 77

[ 69](ite-it51xxx-intc_8h.md#a8aadaec67ad35044cd3ab33c780e519f)#define IT51XXX\_IRQ\_WU76 78

[ 70](ite-it51xxx-intc_8h.md#a46928ad8b9c916e25a625ab63bdd347f)#define IT51XXX\_IRQ\_WU77 79

71/\* Group 10 \*/

[ 72](ite-it51xxx-intc_8h.md#a0cc237123ca5c9e5ee5d2607a1f65cca)#define IT51XXX\_IRQ\_WU88 85

[ 73](ite-it51xxx-intc_8h.md#a3483a35ba697124f99248296a4fea2b2)#define IT51XXX\_IRQ\_WU89 86

[ 74](ite-it51xxx-intc_8h.md#a8628b39b9d4ed06f5f9340ee986192b2)#define IT51XXX\_IRQ\_WU90 87

75/\* Group 11 \*/

[ 76](ite-it51xxx-intc_8h.md#a3899296e615d7ec73d2837c082e35e45)#define IT51XXX\_IRQ\_WU80 88

[ 77](ite-it51xxx-intc_8h.md#a594740dd6c46675dc51da4572de9da5e)#define IT51XXX\_IRQ\_WU81 89

[ 78](ite-it51xxx-intc_8h.md#a1833664c1f0542e1e1558309ef515994)#define IT51XXX\_IRQ\_WU82 90

[ 79](ite-it51xxx-intc_8h.md#a6ebed02426d639b288c7e7c1c8c99996)#define IT51XXX\_IRQ\_WU83 91

[ 80](ite-it51xxx-intc_8h.md#aeddeccc8358a4e1beca4bda4bac04e8e)#define IT51XXX\_IRQ\_WU84 92

[ 81](ite-it51xxx-intc_8h.md#a54675f2dfc773de68a0265ffe5403334)#define IT51XXX\_IRQ\_WU85 93

[ 82](ite-it51xxx-intc_8h.md#a4836dc7572b080050825b634b2739646)#define IT51XXX\_IRQ\_WU86 94

[ 83](ite-it51xxx-intc_8h.md#a0eaf7c4c781e015bbf4d1f53fe37f446)#define IT51XXX\_IRQ\_WU87 95

84/\* Group 12 \*/

[ 85](ite-it51xxx-intc_8h.md#a5bb04e38d680139a5ce1041b180d2742)#define IT51XXX\_IRQ\_WU91 96

[ 86](ite-it51xxx-intc_8h.md#a225c69b63c8534ef4aca7f8bf57377fa)#define IT51XXX\_IRQ\_WU92 97

[ 87](ite-it51xxx-intc_8h.md#a340aa216839b6dc185618f6615c3dcc2)#define IT51XXX\_IRQ\_WU93 98

[ 88](ite-it51xxx-intc_8h.md#a6409fd59e97542c5ef8bef2db86208f2)#define IT51XXX\_IRQ\_WU95 100

[ 89](ite-it51xxx-intc_8h.md#a3818c0faa999f1d1b967b1c611139d49)#define IT51XXX\_IRQ\_WU96 101

[ 90](ite-it51xxx-intc_8h.md#a8eb5c55cd65680bc525ec13550935cf8)#define IT51XXX\_IRQ\_WU97 102

[ 91](ite-it51xxx-intc_8h.md#ae79e7df40a0e4979ec62927689ac6cb0)#define IT51XXX\_IRQ\_WU98 103

92/\* Group 13 \*/

[ 93](ite-it51xxx-intc_8h.md#a321ce88140a01d74cc92918b139fac86)#define IT51XXX\_IRQ\_WU99 104

[ 94](ite-it51xxx-intc_8h.md#a6e06551e06cf220c07c1dd2a77b71a40)#define IT51XXX\_IRQ\_WU100 105

[ 95](ite-it51xxx-intc_8h.md#aeb8d32ab2288e2d6b8ed9373f1004969)#define IT51XXX\_IRQ\_WU101 106

[ 96](ite-it51xxx-intc_8h.md#a21f0556a14699a72814de76f9aab054b)#define IT51XXX\_IRQ\_WU102 107

[ 97](ite-it51xxx-intc_8h.md#a80d91803a44448f1019cab38e9eeb9d0)#define IT51XXX\_IRQ\_WU103 108

[ 98](ite-it51xxx-intc_8h.md#a70286a54519eac7e069a5cd7149b7605)#define IT51XXX\_IRQ\_WU104 109

[ 99](ite-it51xxx-intc_8h.md#a0edf01dcc171ae82f5000d91cb75a325)#define IT51XXX\_IRQ\_WU105 110

[ 100](ite-it51xxx-intc_8h.md#a1e5344c12c111644ec129649ec1bc590)#define IT51XXX\_IRQ\_WU106 111

101/\* Group 14 \*/

[ 102](ite-it51xxx-intc_8h.md#aeb45d2b08b983864373a0f55eb22e43d)#define IT51XXX\_IRQ\_WU107 112

[ 103](ite-it51xxx-intc_8h.md#a5aefba5d16ed726483ea6f5d530abee1)#define IT51XXX\_IRQ\_WU108 113

[ 104](ite-it51xxx-intc_8h.md#a1261ef1bdeb49a8829227db86913bb63)#define IT51XXX\_IRQ\_WU109 114

[ 105](ite-it51xxx-intc_8h.md#afdd1fc1548ff42ed4ee71a4cac096740)#define IT51XXX\_IRQ\_WU110 115

[ 106](ite-it51xxx-intc_8h.md#ab579f5814ff928e42ed3ecfff4479c98)#define IT51XXX\_IRQ\_WU111 116

[ 107](ite-it51xxx-intc_8h.md#a8d1263072ff6e203f483db4f4963affb)#define IT51XXX\_IRQ\_WU112 117

[ 108](ite-it51xxx-intc_8h.md#af5c068d30e13d3beae36e43e60f683a0)#define IT51XXX\_IRQ\_WU113 118

[ 109](ite-it51xxx-intc_8h.md#a9e3ceecd8fc68956a9c86235e1c8d31b)#define IT51XXX\_IRQ\_WU114 119

110/\* Group 15 \*/

[ 111](ite-it51xxx-intc_8h.md#a1234e873af21343a697bd2f6d6b975ef)#define IT51XXX\_IRQ\_WU115 120

[ 112](ite-it51xxx-intc_8h.md#ac93e38d1a414b44a5a7ec85ee0827006)#define IT51XXX\_IRQ\_WU116 121

[ 113](ite-it51xxx-intc_8h.md#aef5f1d8e172f0454547f338188161670)#define IT51XXX\_IRQ\_WU117 122

[ 114](ite-it51xxx-intc_8h.md#ac424aeac70e9232ee199832c8b8e35fe)#define IT51XXX\_IRQ\_WU118 123

[ 115](ite-it51xxx-intc_8h.md#a3ccd0d5fed12d435960fc757292a291a)#define IT51XXX\_IRQ\_WU119 124

[ 116](ite-it51xxx-intc_8h.md#a886130b549e4a839b3f0228ecbe24d33)#define IT51XXX\_IRQ\_WU120 125

[ 117](ite-it51xxx-intc_8h.md#ad25d4ec41e22d897907646d14d089ac8)#define IT51XXX\_IRQ\_WU121 126

[ 118](ite-it51xxx-intc_8h.md#ad62f6942c45c6775237a65e3fb63890d)#define IT51XXX\_IRQ\_WU122 127

119/\* Group 16 \*/

[ 120](ite-it51xxx-intc_8h.md#a2ed1d21bffa4100b329475da7f0b05f5)#define IT51XXX\_IRQ\_WU128 128

[ 121](ite-it51xxx-intc_8h.md#a7abbba0cf4ff18e831d90f5a755e4bf0)#define IT51XXX\_IRQ\_WU129 129

[ 122](ite-it51xxx-intc_8h.md#aa37e21e814b8f03155f5edf183c2ff68)#define IT51XXX\_IRQ\_WU131 131

[ 123](ite-it51xxx-intc_8h.md#a7f8ee82d1a99380bb0c78868d2c7f9ab)#define IT51XXX\_IRQ\_WU132 132

[ 124](ite-it51xxx-intc_8h.md#abab0fcc184a589ba650baddf2150e94b)#define IT51XXX\_IRQ\_WU133 133

[ 125](ite-it51xxx-intc_8h.md#aa384f21424d9c2f0f5ae385367385c90)#define IT51XXX\_IRQ\_WU134 134

[ 126](ite-it51xxx-intc_8h.md#a90e796c4f1fe0d74d456db79407188ff)#define IT51XXX\_IRQ\_WU135 135

127/\* Group 17 \*/

[ 128](ite-it51xxx-intc_8h.md#a949522fcdba6424668f214c4fba2b2ac)#define IT51XXX\_IRQ\_WU136 136

[ 129](ite-it51xxx-intc_8h.md#aeeace56eafbaa49befe615e2a4c873f3)#define IT51XXX\_IRQ\_WU137 137

[ 130](ite-it51xxx-intc_8h.md#a6b2c04bdde25754955c9882b97821176)#define IT51XXX\_IRQ\_WU138 138

[ 131](ite-it51xxx-intc_8h.md#abe9d36fd7c3cba5b613c37d1e212a108)#define IT51XXX\_IRQ\_WU139 139

[ 132](ite-it51xxx-intc_8h.md#a0056b7712922f1c825ee5157819e343e)#define IT51XXX\_IRQ\_WU140 140

[ 133](ite-it51xxx-intc_8h.md#afb41c8d686df27c6248cdf2245bb0cb0)#define IT51XXX\_IRQ\_WU141 141

[ 134](ite-it51xxx-intc_8h.md#a241bae65d751d0840e82ec6c01f58900)#define IT51XXX\_IRQ\_WU142 142

135/\* Group 18 \*/

[ 136](ite-it51xxx-intc_8h.md#a98a29286e93b44900f6373deed1c1f6b)#define IT51XXX\_IRQ\_WU127 148

[ 137](ite-it51xxx-intc_8h.md#ada04e9ef33341983fba6faa6fcbe4a96)#define IT51XXX\_IRQ\_V\_CMP 151

138/\* Group 19 \*/

[ 139](ite-it51xxx-intc_8h.md#abd85b8ba3de11192be938e35d3508e87)#define IT51XXX\_IRQ\_PECI 152

[ 140](ite-it51xxx-intc_8h.md#a37dc6051af77a724854c527a45dfac68)#define IT51XXX\_IRQ\_ESPI 153

[ 141](ite-it51xxx-intc_8h.md#adbddb73244678d5fde56eec7479775f4)#define IT51XXX\_IRQ\_ESPI\_VW 154

[ 142](ite-it51xxx-intc_8h.md#a8559f80da2518403b5d9472657f82ea0)#define IT51XXX\_IRQ\_PCH\_P80 155

[ 143](ite-it51xxx-intc_8h.md#a28bcb6addfada56ac81f15e45c7ee3b4)#define IT51XXX\_IRQ\_TIMER3 157

[ 144](ite-it51xxx-intc_8h.md#a519c0e8e3f30a9e1af2b64822b07ee13)#define IT51XXX\_IRQ\_PLL\_CHANGE 159

145/\* Group 20 \*/

[ 146](ite-it51xxx-intc_8h.md#a47d8b8240562c4a2751a91337c9fa305)#define IT51XXX\_IRQ\_SMB\_E 160

[ 147](ite-it51xxx-intc_8h.md#a11f41892c1092f950a4a1e69e1b78a9c)#define IT51XXX\_IRQ\_SMB\_F 161

[ 148](ite-it51xxx-intc_8h.md#a185ad05ef3459010c11695c539126ed1)#define IT51XXX\_IRQ\_WU40 163

[ 149](ite-it51xxx-intc_8h.md#a32688b80aa7e9f4cdc5c56b8454ce833)#define IT51XXX\_IRQ\_WU45 166

150/\* Group 21 \*/

[ 151](ite-it51xxx-intc_8h.md#a0826262e2d144ccb3744aa051a49d3bf)#define IT51XXX\_IRQ\_WU46 168

[ 152](ite-it51xxx-intc_8h.md#abc65b0e84172082f67f7f73f966fe93e)#define IT51XXX\_IRQ\_WU144 170

[ 153](ite-it51xxx-intc_8h.md#a5fa5010931782c35ef10dc8aff598496)#define IT51XXX\_IRQ\_WU145 171

[ 154](ite-it51xxx-intc_8h.md#a950d230c0b4cdca84362c94d923cd292)#define IT51XXX\_IRQ\_WU146 172

[ 155](ite-it51xxx-intc_8h.md#a2092b865939507ed7c9deaedb9ca1d1b)#define IT51XXX\_IRQ\_WU147 173

[ 156](ite-it51xxx-intc_8h.md#af46c7e6a1396a5758c0acc9ee0b41fd9)#define IT51XXX\_IRQ\_TIMER4 175

157/\* Group 22 \*/

[ 158](ite-it51xxx-intc_8h.md#ab79775b5e3e970bd94e2e80f3918e6ad)#define IT51XXX\_IRQ\_WU148 176

[ 159](ite-it51xxx-intc_8h.md#a24533eae53c79b5d6e2c4d8b6f648c00)#define IT51XXX\_IRQ\_WU149 177

[ 160](ite-it51xxx-intc_8h.md#afbea534e0246c550492d193e9ca449d8)#define IT51XXX\_IRQ\_WU150 178

[ 161](ite-it51xxx-intc_8h.md#a589f55a54a23a30754557f8abc8d98c8)#define IT51XXX\_IRQ\_WU151 179

[ 162](ite-it51xxx-intc_8h.md#af0379a8a7ee6c496a839d26ff088f86a)#define IT51XXX\_IRQ\_I3C\_M0 180

[ 163](ite-it51xxx-intc_8h.md#a6a311d1c8ed8c0b6f886a0939d973938)#define IT51XXX\_IRQ\_I3C\_M1 181

[ 164](ite-it51xxx-intc_8h.md#a3e77d71c4a44f2891fe0c9aca8d54a68)#define IT51XXX\_IRQ\_I3C\_S0 182

[ 165](ite-it51xxx-intc_8h.md#a6656394e194fe50f39ef6188f7b0d6f2)#define IT51XXX\_IRQ\_I3C\_S1 183

166/\* Group 25 \*/

[ 167](ite-it51xxx-intc_8h.md#ac4d39ade3c95ca510c7abb04398a80a0)#define IT51XXX\_IRQ\_SMB\_SC 203

[ 168](ite-it51xxx-intc_8h.md#a2a3f81d5804f14330681b72b8f8364f4)#define IT51XXX\_IRQ\_SMB\_SB 204

[ 169](ite-it51xxx-intc_8h.md#a9073793dfae7154c3a4b7d4313595c60)#define IT51XXX\_IRQ\_SMB\_SA 205

[ 170](ite-it51xxx-intc_8h.md#a31679c43c86bbbe8b87c2e64c649e7c8)#define IT51XXX\_IRQ\_TIMER1\_DW 207

171/\* Group 26 \*/

[ 172](ite-it51xxx-intc_8h.md#a7ad66cb768137ce97bc38118f66dfa15)#define IT51XXX\_IRQ\_TIMER2\_DW 208

[ 173](ite-it51xxx-intc_8h.md#a6b7e9fbfa177b548a4b06ad6b858b8a6)#define IT51XXX\_IRQ\_TIMER3\_DW 209

[ 174](ite-it51xxx-intc_8h.md#a3a8b1a21fa8f69b9068608f1a41fada2)#define IT51XXX\_IRQ\_TIMER4\_DW 210

[ 175](ite-it51xxx-intc_8h.md#a68c95d448985caf77c240ad680a03afc)#define IT51XXX\_IRQ\_TIMER5\_DW 211

[ 176](ite-it51xxx-intc_8h.md#abba7af2fd3a2a785cf533d3b92ac9ebd)#define IT51XXX\_IRQ\_TIMER6\_DW 212

[ 177](ite-it51xxx-intc_8h.md#a8320ec332457fb8590ce65fb53ff2769)#define IT51XXX\_IRQ\_TIMER7\_DW 213

[ 178](ite-it51xxx-intc_8h.md#ad156f2f74a3441c1fa99d6f24ca17281)#define IT51XXX\_IRQ\_TIMER8\_DW 214

179/\* Group 27 \*/

[ 180](ite-it51xxx-intc_8h.md#ab31a3e61f66db774b1cac063fe1d0285)#define IT51XXX\_IRQ\_PWM\_TACH0 219

[ 181](ite-it51xxx-intc_8h.md#acffdacb27fdfbd21158e17eb8edc29fb)#define IT51XXX\_IRQ\_PWM\_TACH1 220

[ 182](ite-it51xxx-intc_8h.md#ab7915c5e0093e966dbabd34a55c80e19)#define IT51XXX\_IRQ\_PWM\_TACH2 221

[ 183](ite-it51xxx-intc_8h.md#aa71190064a261f80fe101e8800432664)#define IT51XXX\_IRQ\_SMB\_G 222

[ 184](ite-it51xxx-intc_8h.md#a8a5b61f307baac7667d007a56789bc81)#define IT51XXX\_IRQ\_SMB\_H 223

185/\* Group 28 \*/

[ 186](ite-it51xxx-intc_8h.md#ab02616140905f0e335523993b894a8ed)#define IT51XXX\_IRQ\_SMB\_I 224

187

188#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_INTERRUPT\_CONTROLLER\_ITE\_INTC\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [interrupt-controller](dir_f11fd9ad294c5739f2cbe07a93c59a1b.md)
- [ite-it51xxx-intc.h](ite-it51xxx-intc_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
