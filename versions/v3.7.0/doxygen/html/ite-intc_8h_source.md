---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/ite-intc_8h_source.html
original_path: doxygen/html/ite-intc_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ite-intc.h

[Go to the documentation of this file.](ite-intc_8h.md)

1/\*

2 \* Copyright (c) 2020 ITE Corporation. All Rights Reserved.

3 \* SPDX-License-Identifier: Apache-2.0

4 \*/

5

6#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_INTERRUPT\_CONTROLLER\_ITE\_INTC\_H\_

7#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_INTERRUPT\_CONTROLLER\_ITE\_INTC\_H\_

8

[ 9](ite-intc_8h.md#a9290a5f35a4d3514237ba9fb00936859)#define IRQ\_TYPE\_NONE 0

[ 10](ite-intc_8h.md#ac95cadb7e2fafe537f8be5274baa1e75)#define IRQ\_TYPE\_EDGE\_RISING 1

[ 11](ite-intc_8h.md#aab03b1a63f7cd7f3a43353048655135a)#define IRQ\_TYPE\_EDGE\_FALLING 2

[ 12](ite-intc_8h.md#a377225dde978048e3d918cedba2c125e)#define IRQ\_TYPE\_EDGE\_BOTH (IRQ\_TYPE\_EDGE\_FALLING | IRQ\_TYPE\_EDGE\_RISING)

[ 13](ite-intc_8h.md#a82fc9c68723b62cf4071203f54bd321b)#define IRQ\_TYPE\_LEVEL\_HIGH 4

[ 14](ite-intc_8h.md#adfb5a6f2364155f99a90fba88ff9a670)#define IRQ\_TYPE\_LEVEL\_LOW 8

15

16/\* IRQ numbers of WUC \*/

17/\* Group 0 of INTC \*/

[ 18](ite-intc_8h.md#a51865a04eb03d3a3f1239cbbf547fb45)#define IT8XXX2\_IRQ\_WU20 1

[ 19](ite-intc_8h.md#a164c6994b9ec0e6caeb2d22f26bb3193)#define IT8XXX2\_IRQ\_KBC\_OBE 2

[ 20](ite-intc_8h.md#a3ade9064122702f975e5bb8c152af253)#define IT8XXX2\_IRQ\_SMB\_D 4

[ 21](ite-intc_8h.md#acdc62901f3913707a381ef90b0c022d3)#define IT8XXX2\_IRQ\_WKINTD 5

[ 22](ite-intc_8h.md#af40e775e4a526303b9dab46161e0583b)#define IT8XXX2\_IRQ\_WU23 6

23/\* Group 1 \*/

[ 24](ite-intc_8h.md#afeffdbf074bfea151dd7e95938303943)#define IT8XXX2\_IRQ\_SMB\_A 9

[ 25](ite-intc_8h.md#ab92e5222303c3b72fe058e4678c3baa0)#define IT8XXX2\_IRQ\_SMB\_B 10

[ 26](ite-intc_8h.md#a08515d08e3080bdc2f2cd42c492dbbc2)#define IT8XXX2\_IRQ\_WU26 12

[ 27](ite-intc_8h.md#a4e6257f4cdb53d2603777c6f2bbf1e89)#define IT8XXX2\_IRQ\_WKINTC 13

[ 28](ite-intc_8h.md#a24a0259fb6961ae91da26b9fcb985db5)#define IT8XXX2\_IRQ\_WU25 14

29/\* Group 2 \*/

[ 30](ite-intc_8h.md#a8347f8b954afdde767f221a07a7c6359)#define IT8XXX2\_IRQ\_SMB\_C 16

[ 31](ite-intc_8h.md#a1a5ed099e4ee92fa257a542244d9d410)#define IT8XXX2\_IRQ\_WU24 17

[ 32](ite-intc_8h.md#a7cbf470dc0aef8cce66946b3dfd05117)#define IT8XXX2\_IRQ\_WU22 21

[ 33](ite-intc_8h.md#ac585dd5e3a928bf6080d1d5fb879b686)#define IT8XXX2\_IRQ\_USB 23

34/\* Group 3 \*/

[ 35](ite-intc_8h.md#ad192bc4d6eb374f6f1b6a3435a0de475)#define IT8XXX2\_IRQ\_KBC\_IBF 24

[ 36](ite-intc_8h.md#ace6032a2b393b2e9f82e17bc4f682507)#define IT8XXX2\_IRQ\_PMC1\_IBF 25

[ 37](ite-intc_8h.md#af54f7abd8fd110352dbd932665169797)#define IT8XXX2\_IRQ\_PMC2\_IBF 27

[ 38](ite-intc_8h.md#a9353a04daccd2da837b226e098045e65)#define IT8XXX2\_IRQ\_TIMER1 30

[ 39](ite-intc_8h.md#aa8e07837f14e38d727ad423d8fd3be26)#define IT8XXX2\_IRQ\_WU21 31

40/\* Group 5 \*/

[ 41](ite-intc_8h.md#afc0033cac685e369c1e643508ac8d3a9)#define IT8XXX2\_IRQ\_WU50 40

[ 42](ite-intc_8h.md#aaafc18df1262db451a0a4d443143d5a5)#define IT8XXX2\_IRQ\_WU51 41

[ 43](ite-intc_8h.md#a9f1574d93a73a24b560e5d8f6ed639d7)#define IT8XXX2\_IRQ\_WU52 42

[ 44](ite-intc_8h.md#ad45cafb41e8199d89fc14bbf1ef1c1fb)#define IT8XXX2\_IRQ\_WU53 43

[ 45](ite-intc_8h.md#ac246e8f65786a75c9aba1ec5a4204fe5)#define IT8XXX2\_IRQ\_WU54 44

[ 46](ite-intc_8h.md#a794890994a7a1df4171874e24f8f7500)#define IT8XXX2\_IRQ\_WU55 45

[ 47](ite-intc_8h.md#aa553be72aa49dc4c669ad4976d934f9f)#define IT8XXX2\_IRQ\_WU56 46

[ 48](ite-intc_8h.md#ab97cc00122c848c10d37a9397e7bea66)#define IT8XXX2\_IRQ\_WU57 47

49/\* Group 6 \*/

[ 50](ite-intc_8h.md#ad5aa387daa4a4c9889bce14af424a32f)#define IT8XXX2\_IRQ\_WU60 48

[ 51](ite-intc_8h.md#adbb8b156e28763763936f1744091ef16)#define IT8XXX2\_IRQ\_WU61 49

[ 52](ite-intc_8h.md#a323fbf7a864a4fe8d2dc5ccbeb257294)#define IT8XXX2\_IRQ\_WU62 50

[ 53](ite-intc_8h.md#a43ebabf29257d1e9e34c7ec9940bf886)#define IT8XXX2\_IRQ\_WU63 51

[ 54](ite-intc_8h.md#a7b36f3167661f548b2be26fdb2699a99)#define IT8XXX2\_IRQ\_WU64 52

[ 55](ite-intc_8h.md#a450e550d3c955cb85963c40fe9c3ef79)#define IT8XXX2\_IRQ\_WU65 53

[ 56](ite-intc_8h.md#a63347ec51db69184846a4e14a1368709)#define IT8XXX2\_IRQ\_WU66 54

[ 57](ite-intc_8h.md#ad8cb0227c71b5173566a483f7190b454)#define IT8XXX2\_IRQ\_WU67 55

58/\* Group 7 \*/

[ 59](ite-intc_8h.md#a44a71af10fc4eebb3a9e6fd14fa03fa4)#define IT8XXX2\_IRQ\_TIMER2 58

60/\* Group 9 \*/

[ 61](ite-intc_8h.md#a8cb33d3f882ed2cd523795a688fa1363)#define IT8XXX2\_IRQ\_WU70 72

[ 62](ite-intc_8h.md#a9303a03c624d9edf842ee268f6d4f4a0)#define IT8XXX2\_IRQ\_WU71 73

[ 63](ite-intc_8h.md#a260e57b5abf3538854ce49a08c8a1d5b)#define IT8XXX2\_IRQ\_WU72 74

[ 64](ite-intc_8h.md#ac6e77697033c09657877ae7646c2dbd5)#define IT8XXX2\_IRQ\_WU73 75

[ 65](ite-intc_8h.md#ad15f96abc4101a0bfed25d348e9bb8dd)#define IT8XXX2\_IRQ\_WU74 76

[ 66](ite-intc_8h.md#a8127b5a3d89eb80919888400b77d6df9)#define IT8XXX2\_IRQ\_WU75 77

[ 67](ite-intc_8h.md#a5431a28b59009ad6cfe89df880f26b74)#define IT8XXX2\_IRQ\_WU76 78

[ 68](ite-intc_8h.md#a85638058bef305cf3c72275a74a8a8f5)#define IT8XXX2\_IRQ\_WU77 79

69/\* Group 10 \*/

[ 70](ite-intc_8h.md#a62568d6b0f25a658c16cb5c809f92c6f)#define IT8XXX2\_IRQ\_TIMER8 80

[ 71](ite-intc_8h.md#a9d62ad86c7c15e13b962a5c0f17e0810)#define IT8XXX2\_IRQ\_WU88 85

[ 72](ite-intc_8h.md#a6b34b4de0fad04f9d3c577eff9a74aed)#define IT8XXX2\_IRQ\_WU89 86

[ 73](ite-intc_8h.md#ae29e4e29bdb8920d352a85f1eb97bc09)#define IT8XXX2\_IRQ\_WU90 87

74/\* Group 11 \*/

[ 75](ite-intc_8h.md#a12dd29667cd356607e7f31b52ea906ea)#define IT8XXX2\_IRQ\_WU80 88

[ 76](ite-intc_8h.md#ade0f819076b8cc26f63a33772507899a)#define IT8XXX2\_IRQ\_WU81 89

[ 77](ite-intc_8h.md#a232053c3ff1a86e4afbfc332599ed711)#define IT8XXX2\_IRQ\_WU82 90

[ 78](ite-intc_8h.md#ae4a1972e35689df1db714b52d71dc140)#define IT8XXX2\_IRQ\_WU83 91

[ 79](ite-intc_8h.md#a2257ffbbd8f9a0ce446548bffc3d311c)#define IT8XXX2\_IRQ\_WU84 92

[ 80](ite-intc_8h.md#a8268491bc0032a66991d9a8d3a3d285c)#define IT8XXX2\_IRQ\_WU85 93

[ 81](ite-intc_8h.md#ab7ce72297a86bb34bd9025599c81dd49)#define IT8XXX2\_IRQ\_WU86 94

[ 82](ite-intc_8h.md#a7517e75de3795b5cd482d8adb607c991)#define IT8XXX2\_IRQ\_WU87 95

83/\* Group 12 \*/

[ 84](ite-intc_8h.md#a5d3cac73994a065201a17ab4725d962a)#define IT8XXX2\_IRQ\_WU91 96

[ 85](ite-intc_8h.md#af5f92032cb97b198ba36c7b428d011ae)#define IT8XXX2\_IRQ\_WU92 97

[ 86](ite-intc_8h.md#afae6ea7e844d0bbd809cc683b354883c)#define IT8XXX2\_IRQ\_WU93 98

[ 87](ite-intc_8h.md#a690f5f5f6f300b24cd907122df15b420)#define IT8XXX2\_IRQ\_WU94 99

[ 88](ite-intc_8h.md#ace32741abf9552cd60a092f747e8b9e6)#define IT8XXX2\_IRQ\_WU95 100

[ 89](ite-intc_8h.md#a21f8e8cd3ef74b5a716344c90e0e39b4)#define IT8XXX2\_IRQ\_WU96 101

[ 90](ite-intc_8h.md#ac4170451fb1cb5d5e7e8d6e075fd8fce)#define IT8XXX2\_IRQ\_WU97 102

[ 91](ite-intc_8h.md#a29555f549f89915491439c9399eed39f)#define IT8XXX2\_IRQ\_WU98 103

92/\* Group 13 \*/

[ 93](ite-intc_8h.md#a26aaeadedf73d5c5bd42c9dff56a8059)#define IT8XXX2\_IRQ\_WU99 104

[ 94](ite-intc_8h.md#afed48a97b31e7fae176ddcd0f15b1df8)#define IT8XXX2\_IRQ\_WU100 105

[ 95](ite-intc_8h.md#a4ea9ccbd6fec3c479aeabfe3d95fb9a1)#define IT8XXX2\_IRQ\_WU101 106

[ 96](ite-intc_8h.md#a347772eb009d923d6bf26e7be1130fd1)#define IT8XXX2\_IRQ\_WU102 107

[ 97](ite-intc_8h.md#ae8048263f8ab7a039d9043186dd3b21c)#define IT8XXX2\_IRQ\_WU103 108

[ 98](ite-intc_8h.md#a3b545fc9e5b2725734cc9d8705ab33c6)#define IT8XXX2\_IRQ\_WU104 109

[ 99](ite-intc_8h.md#a8494842c802337e212ac3591cd90318d)#define IT8XXX2\_IRQ\_WU105 110

[ 100](ite-intc_8h.md#aed3fd2392932c82eb7c237540778c1dc)#define IT8XXX2\_IRQ\_WU106 111

101/\* Group 14 \*/

[ 102](ite-intc_8h.md#ae905883b0d64273279320febb80474e4)#define IT8XXX2\_IRQ\_WU107 112

[ 103](ite-intc_8h.md#af5890809f076a19af7bdb019761b2fd5)#define IT8XXX2\_IRQ\_WU108 113

[ 104](ite-intc_8h.md#a486bb418458778885e38df9d9f7e3400)#define IT8XXX2\_IRQ\_WU109 114

[ 105](ite-intc_8h.md#af15907cee51085a38d191005d4902294)#define IT8XXX2\_IRQ\_WU110 115

[ 106](ite-intc_8h.md#aefe25a9621334783ec285b065ef60c14)#define IT8XXX2\_IRQ\_WU111 116

[ 107](ite-intc_8h.md#a0500748e035b1be53ac925949239222b)#define IT8XXX2\_IRQ\_WU112 117

[ 108](ite-intc_8h.md#a3cfd6fbf8f81d2f06da7349136150a3f)#define IT8XXX2\_IRQ\_WU113 118

[ 109](ite-intc_8h.md#aa548093ad9515794dd05254ab44c1aa1)#define IT8XXX2\_IRQ\_WU114 119

110/\* Group 15 \*/

[ 111](ite-intc_8h.md#aaf4e01822d4db393a3d232903568f732)#define IT8XXX2\_IRQ\_WU115 120

[ 112](ite-intc_8h.md#a8d06b3da3354bf3e0386fddb076eedd6)#define IT8XXX2\_IRQ\_WU116 121

[ 113](ite-intc_8h.md#af8e6a237bb5517104d1cfaea5ea83013)#define IT8XXX2\_IRQ\_WU117 122

[ 114](ite-intc_8h.md#a929368b200b099b7c3559297f7eec93f)#define IT8XXX2\_IRQ\_WU118 123

[ 115](ite-intc_8h.md#aea0d15b7466a70f369e793744d8879ed)#define IT8XXX2\_IRQ\_WU119 124

[ 116](ite-intc_8h.md#aa999701f32ffeb7a896e439d402d7c20)#define IT8XXX2\_IRQ\_WU120 125

[ 117](ite-intc_8h.md#ae6b5cbc9a7be8e266b234e2ae1236c5a)#define IT8XXX2\_IRQ\_WU121 126

[ 118](ite-intc_8h.md#a0cc7e45df4a646a50533f18829fb9823)#define IT8XXX2\_IRQ\_WU122 127

119/\* Group 16 \*/

[ 120](ite-intc_8h.md#aae2ba10f26caf6eeb4cfe9c70e7b51d4)#define IT8XXX2\_IRQ\_WU128 128

[ 121](ite-intc_8h.md#aa36107db62047a7ba38a0aa3c091f993)#define IT8XXX2\_IRQ\_WU129 129

[ 122](ite-intc_8h.md#a070e81200de0c2fe7ba6c6a67eb702aa)#define IT8XXX2\_IRQ\_WU130 130

[ 123](ite-intc_8h.md#a2733ffe35eb8a3361ba329417dd8313e)#define IT8XXX2\_IRQ\_WU131 131

[ 124](ite-intc_8h.md#a4898c89604f929459ffe7c599fc8fa7b)#define IT8XXX2\_IRQ\_WU132 132

[ 125](ite-intc_8h.md#a4e85ab9e4d017c90b79139ba61fdd5d1)#define IT8XXX2\_IRQ\_WU133 133

[ 126](ite-intc_8h.md#af396686ee5e9c1f7c54f191b054c108f)#define IT8XXX2\_IRQ\_WU134 134

[ 127](ite-intc_8h.md#a90c3033b6daf309fcfe73bb39b3b252f)#define IT8XXX2\_IRQ\_WU135 135

128/\* Group 17 \*/

[ 129](ite-intc_8h.md#aff0e5b1d4946deb68d6ed1d7420e42bb)#define IT8XXX2\_IRQ\_WU136 136

[ 130](ite-intc_8h.md#a3943e3914e2e6c62ab3f5b28c2a1a4e8)#define IT8XXX2\_IRQ\_WU137 137

[ 131](ite-intc_8h.md#a817f4b3d15ff7469f5d347d4cc87c1e4)#define IT8XXX2\_IRQ\_WU138 138

[ 132](ite-intc_8h.md#a7eae741560ddaf972a9ac99826dde9fb)#define IT8XXX2\_IRQ\_WU139 139

[ 133](ite-intc_8h.md#aaed275701462369166e099fa6415a69e)#define IT8XXX2\_IRQ\_WU140 140

[ 134](ite-intc_8h.md#a986e35a0b6cecdbae29e269f40f4d648)#define IT8XXX2\_IRQ\_WU141 141

[ 135](ite-intc_8h.md#a360d9aa8caa04a319d4c4fe92efdc7c9)#define IT8XXX2\_IRQ\_WU142 142

[ 136](ite-intc_8h.md#aeb435671c9894e01c8babae68e6858d2)#define IT8XXX2\_IRQ\_WU143 143

137/\* Group 18 \*/

[ 138](ite-intc_8h.md#a988dbab9684233c89ca0d1ff90ff4caa)#define IT8XXX2\_IRQ\_WU123 144

[ 139](ite-intc_8h.md#a0673f35476eb2f3ea3905ffed7055e7f)#define IT8XXX2\_IRQ\_WU124 145

[ 140](ite-intc_8h.md#a6acd52b3400d5e352cae94dba3eeaca0)#define IT8XXX2\_IRQ\_WU125 146

[ 141](ite-intc_8h.md#a0441a32e61afd7254a9fa2edb510d4a1)#define IT8XXX2\_IRQ\_WU126 147

[ 142](ite-intc_8h.md#aed5301127cb8b90f9831b244c8085b79)#define IT8XXX2\_IRQ\_V\_CMP 151

143/\* Group 19 \*/

[ 144](ite-intc_8h.md#aea5518cddba14665f9f7a2acf7b704a7)#define IT8XXX2\_IRQ\_SMB\_E 152

[ 145](ite-intc_8h.md#a0b9b660f99ccc836f3cd1c5aaa66476b)#define IT8XXX2\_IRQ\_SMB\_F 153

[ 146](ite-intc_8h.md#a90092bccc13f1a9523ade25d2fa49c1f)#define IT8XXX2\_IRQ\_TIMER3 155

[ 147](ite-intc_8h.md#a2e5c4330798c3a376bb7453660f2e01b)#define IT8XXX2\_IRQ\_TIMER4 156

[ 148](ite-intc_8h.md#af61ec5638b3f691d9def15a71d8a82ac)#define IT8XXX2\_IRQ\_TIMER5 157

[ 149](ite-intc_8h.md#a01203154d769bc5bbf1bd7cf5e42ebdf)#define IT8XXX2\_IRQ\_TIMER6 158

[ 150](ite-intc_8h.md#a369c990acee73d8dcbedc3e462070581)#define IT8XXX2\_IRQ\_TIMER7 159

151/\* Group 20 \*/

[ 152](ite-intc_8h.md#aaf76ad2c103888e4cfa104b463f3ba25)#define IT8XXX2\_IRQ\_ESPI 162

[ 153](ite-intc_8h.md#a3589b7e407cbe43552ce47552844f09f)#define IT8XXX2\_IRQ\_ESPI\_VW 163

[ 154](ite-intc_8h.md#a77a329b843c2709461188b236e7e9f5a)#define IT8XXX2\_IRQ\_PCH\_P80 164

[ 155](ite-intc_8h.md#a3693e6b88579d604942052a0e588eb85)#define IT8XXX2\_IRQ\_USBPD0 165

[ 156](ite-intc_8h.md#ab17c137bc7f8d5439ac5c2b204cf14e3)#define IT8XXX2\_IRQ\_USBPD1 166

157/\* Group 21 \*/

[ 158](ite-intc_8h.md#aae96e204b6c6e6be344ee7f2377006c1)#define IT8XXX2\_IRQ\_USBPD2 174

159/\* Group 22 \*/

[ 160](ite-intc_8h.md#a7aa1ecddba7071219cca6a145cb53969)#define IT8XXX2\_IRQ\_WU40 176

[ 161](ite-intc_8h.md#a95c762f9c661f278894d43420370e948)#define IT8XXX2\_IRQ\_WU45 177

[ 162](ite-intc_8h.md#a041acf5b855e1d3e99e1b7e82c6e57bc)#define IT8XXX2\_IRQ\_WU46 178

[ 163](ite-intc_8h.md#a42eb93ef740173eb2277669957abefaa)#define IT8XXX2\_IRQ\_WU144 179

[ 164](ite-intc_8h.md#a429966f42f4484049a98cdf7e962aa04)#define IT8XXX2\_IRQ\_WU145 180

[ 165](ite-intc_8h.md#a0668648aa708375b7a50fb7ffb2a4e42)#define IT8XXX2\_IRQ\_WU146 181

[ 166](ite-intc_8h.md#a6cc3170056313309ed7b29c088d92737)#define IT8XXX2\_IRQ\_WU147 182

[ 167](ite-intc_8h.md#accbe84f26e4bd5fd48f8a1803ad7c3b6)#define IT8XXX2\_IRQ\_WU148 183

168/\* Group 23 \*/

[ 169](ite-intc_8h.md#a46404fb07e0693bcfa6be6dd8375aa6d)#define IT8XXX2\_IRQ\_WU149 184

[ 170](ite-intc_8h.md#a8394d2a1eecd8958ed10b198cb0d33fe)#define IT8XXX2\_IRQ\_WU150 185

171

[ 172](ite-intc_8h.md#a39332381696855007ce3af2164bb449d)#define IT8XXX2\_IRQ\_COUNT (CONFIG\_NUM\_IRQS + 1)

173

174#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_INTERRUPT\_CONTROLLER\_ITE\_INTC\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [interrupt-controller](dir_f11fd9ad294c5739f2cbe07a93c59a1b.md)
- [ite-intc.h](ite-intc_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
