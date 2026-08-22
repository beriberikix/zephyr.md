---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/pinctrl-rx_8h_source.html
original_path: doxygen/html/pinctrl-rx_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

pinctrl-rx.h

[Go to the documentation of this file.](pinctrl-rx_8h.md)

1/\*

2 \* Copyright (c) 2024 Renesas Electronics Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_PINCTRL\_PINCTRL\_RX\_H\_

8#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_PINCTRL\_PINCTRL\_RX\_H\_

9

[ 10](pinctrl-rx_8h.md#a33c8631dc344fa69c4e14e4cb43b490b)#define RX\_PORT\_NUM\_POS 0

[ 11](pinctrl-rx_8h.md#af32dac5bcf375bbcf33375877f6e49e3)#define RX\_PORT\_NUM\_MASK 0x1f

12

[ 13](pinctrl-rx_8h.md#a8d620aa7e9514a75e3affc1ef8e950c9)#define RX\_PIN\_NUM\_POS 5

[ 14](pinctrl-rx_8h.md#a5b11958c204ab0c6008ba32445d3c5b1)#define RX\_PIN\_NUM\_MASK 0xf

15

[ 16](pinctrl-rx_8h.md#af0ee9eb8939cfd4e527a66c3d0f58f32)#define RX\_PSEL\_MASK 0x1f

[ 17](pinctrl-rx_8h.md#a58e6ba874d0ff5290cae17d3a6f11905)#define RX\_PSEL\_POS 9

18

[ 19](pinctrl-rx_8h.md#a0fd7aa971c81e73658b9ad99408ff61f)#define RX\_PSEL\_SCI\_1 0xA

[ 20](pinctrl-rx_8h.md#a5275129885c5edd8dfff443723a59022)#define RX\_PSEL\_SCI\_6 0xB

[ 21](pinctrl-rx_8h.md#ad8c118ed209b1757032ab96daa7381e9)#define RX\_PSEL\_TMR 0x5

[ 22](pinctrl-rx_8h.md#aca4687fe2b8f282995d3949e5ea2da10)#define RX\_PSEL\_POE 0x7

23

24/\* P0nPFS \*/

[ 25](pinctrl-rx_8h.md#aad48291cdeb29d13f13ebe0c07259594)#define RX\_PSEL\_P0nPFS\_HIZ 0x0

[ 26](pinctrl-rx_8h.md#a788c40b5e5a82083432968317a7d6c4e)#define RX\_PSEL\_P0nPFS\_ADTRG0 0x1

27

28/\* P1nPFS \*/

[ 29](pinctrl-rx_8h.md#a1000a138a65b0a2dfbf56ced7d00508f)#define RX\_PSEL\_P1nPFS\_MTIOC0B 0x01

[ 30](pinctrl-rx_8h.md#a66b406de32b93246a9710d580deebf97)#define RX\_PSEL\_P1nPFS\_MTIOC3A 0x01

[ 31](pinctrl-rx_8h.md#a8a4dc3f07c7c9da139afcfb48c61277b)#define RX\_PSEL\_P1nPFS\_MTIOC3C 0x01

32

[ 33](pinctrl-rx_8h.md#a2ce48e6029d58e6a0d9bb5a1d968ebe6)#define RX\_PSEL\_P1nPFS\_MTCLKA 0x02

[ 34](pinctrl-rx_8h.md#aadd46dc94695780f5c55fbdd7b9a831d)#define RX\_PSEL\_P1nPFS\_MTCLKB 0x02

[ 35](pinctrl-rx_8h.md#a9c64a0d8e03b70ca45aebd8934f2a7d2)#define RX\_PSEL\_P1nPFS\_MTIOC3B 0x02

[ 36](pinctrl-rx_8h.md#a642a310aca921400209039992742d2c5)#define RX\_PSEL\_P1nPFS\_MTIOC3D 0x02

37

[ 38](pinctrl-rx_8h.md#a9bd05a6002222fd6febd332fc7a0525f)#define RX\_PSEL\_P1nPFS\_TMCI1 0x5

[ 39](pinctrl-rx_8h.md#ad047c079d8ca34f4a489e63ea3ddd642)#define RX\_PSEL\_P1nPFS\_TMO1 0x5

[ 40](pinctrl-rx_8h.md#a2c1fe2875a8f8f104cf7f36c6d6fca67)#define RX\_PSEL\_P1nPFS\_TMCI2 0x5

[ 41](pinctrl-rx_8h.md#a6c59dcdcd76a0bb4c6cafdda3159bb68)#define RX\_PSEL\_P1nPFS\_TMO2 0x5

[ 42](pinctrl-rx_8h.md#ac01000e60804a365ec8ab51235362e53)#define RX\_PSEL\_P1nPFS\_TMRI2 0x5

[ 43](pinctrl-rx_8h.md#a82f52b919e109c185647242656538fb7)#define RX\_PSEL\_P1nPFS\_TMO3 0x5

44

[ 45](pinctrl-rx_8h.md#a11122cc8240be20777710e75cf00122d)#define RX\_PSEL\_P1nPFS\_RTCOUT 0x7

[ 46](pinctrl-rx_8h.md#aa8cfdc8a4947b721c332375226f271a4)#define RX\_PSEL\_P1nPFS\_POE8 0x7

47

[ 48](pinctrl-rx_8h.md#a9925ff98a4835feb94f295004f896c3c)#define RX\_PSEL\_P1nPFS\_ADTRG0 0x9

49

[ 50](pinctrl-rx_8h.md#ac9945fc6a230be884638863306b515a1)#define RX\_PSEL\_P1nPFS\_RXD1 0xA

[ 51](pinctrl-rx_8h.md#a252044667e25c0c87970b263bce8e8a1)#define RX\_PSEL\_P1nPFS\_SMISO1 0xA

[ 52](pinctrl-rx_8h.md#a1ce8f440328f511c996bb79f957fedde)#define RX\_PSEL\_P1nPFS\_SSCL1 0xA

[ 53](pinctrl-rx_8h.md#a9e8985892fa25c60c00770d0265c7076)#define RX\_PSEL\_P1nPFS\_TXD1 0xA

[ 54](pinctrl-rx_8h.md#acd3dc3dc1fa13168bb3052c8e4584019)#define RX\_PSEL\_P1nPFS\_SMOSI1 0xA

[ 55](pinctrl-rx_8h.md#a7ed94521bbda969b0b81f19d39fd563a)#define RX\_PSEL\_P1nPFS\_SSDA1 0xA

56

[ 57](pinctrl-rx_8h.md#a930c4df4b47a5b7dfe3278f0daea4654)#define RX\_PSEL\_P1nPFS\_CTS1 0xB

[ 58](pinctrl-rx_8h.md#a0511157c9149ab334d022f46ddcf952b)#define RX\_PSEL\_P1nPFS\_RTS1 0xB

[ 59](pinctrl-rx_8h.md#a60b58d2d19666957f3725b87719538da)#define RX\_PSEL\_P1nPFS\_SS1 0xB

60

[ 61](pinctrl-rx_8h.md#a6aa86965cd5ea93e6d300d9ea64dd4ed)#define RX\_PSEL\_P1nPFS\_MOSIA 0xD

[ 62](pinctrl-rx_8h.md#a8da1cb599f5ead00b7c142315b79ecc8)#define RX\_PSEL\_P1nPFS\_MISOA 0xD

63

[ 64](pinctrl-rx_8h.md#a313cec1391590cdf0e371b1975f6a2a9)#define RX\_PSEL\_P1nPFS\_SCL 0xF

[ 65](pinctrl-rx_8h.md#a3e8733fee102ece6c412fbfbe2d40482)#define RX\_PSEL\_P1nPFS\_SDA 0xF

66

[ 67](pinctrl-rx_8h.md#a09021fba8d5f0b62cadab76c408f0903)#define RX\_PSEL\_P1nPFS\_TS5 0x19

[ 68](pinctrl-rx_8h.md#a1409faaabb112be224a47aedb34564a0)#define RX\_PSEL\_P1nPFS\_TS6 0x19

69

70/\* P2nPFS \*/

[ 71](pinctrl-rx_8h.md#ae03c6c7a8a1c0d67f314533ccfac715e)#define RX\_PSEL\_P2nPFS\_MTIOC1A 0x01

[ 72](pinctrl-rx_8h.md#a148fe9efdef4a2497296f9268c1a8944)#define RX\_PSEL\_P2nPFS\_MTIOC1B 0x01

[ 73](pinctrl-rx_8h.md#ae0cfb4142c65b33e227907298b404541)#define RX\_PSEL\_P2nPFS\_MTIOC2A 0x01

[ 74](pinctrl-rx_8h.md#a9aa22ce6e3bc9855075281bb6b853c7a)#define RX\_PSEL\_P2nPFS\_MTIOC2B 0x01

[ 75](pinctrl-rx_8h.md#adda0ffa844d9be1603697598618c7a69)#define RX\_PSEL\_P2nPFS\_MTIOC3B 0x01

[ 76](pinctrl-rx_8h.md#a2ac9fabd592b2c4ad45b8d36475aefde)#define RX\_PSEL\_P2nPFS\_MTIOC3D 0x01

[ 77](pinctrl-rx_8h.md#a8f33600b8a26ad32056d89dff90f93af)#define RX\_PSEL\_P2nPFS\_MTIOC4A 0x01

[ 78](pinctrl-rx_8h.md#a035bdd99f2a958b9bef5d7e78be3aa9b)#define RX\_PSEL\_P2nPFS\_MTIOC4C 0x01

79

[ 80](pinctrl-rx_8h.md#a946c850386e432cb2365facb3e8253f4)#define RX\_PSEL\_P2nPFS\_MTCLKA 0x02

[ 81](pinctrl-rx_8h.md#a2637c6326ea9f8792c5bcbc1d2cb6a86)#define RX\_PSEL\_P2nPFS\_MTCLKB 0x02

[ 82](pinctrl-rx_8h.md#a26e1bebe6fa54f6f542834d36e6a5a15)#define RX\_PSEL\_P2nPFS\_MTCLKC 0x02

[ 83](pinctrl-rx_8h.md#a83170987a059d0f4b4474518d1dc9f5c)#define RX\_PSEL\_P2nPFS\_MTCLKD 0x02

84

[ 85](pinctrl-rx_8h.md#a54b553a2a753b03869c5834d5f7cf1ad)#define RX\_PSEL\_P2nPFS\_TMCI0 0x5

[ 86](pinctrl-rx_8h.md#a39e6f7ec8b8e7ae970e6073e50a7ab2f)#define RX\_PSEL\_P2nPFS\_TMO0 0x5

[ 87](pinctrl-rx_8h.md#a088e40350516ce25b1c5644e1f68661b)#define RX\_PSEL\_P2nPFS\_TMRI0 0x5

[ 88](pinctrl-rx_8h.md#ad2b07aa7a06c371eac12cc1cc0ba122b)#define RX\_PSEL\_P2nPFS\_TMO1 0x5

[ 89](pinctrl-rx_8h.md#a464af4730f95dbf0e25e38f218408f44)#define RX\_PSEL\_P2nPFS\_TMRI1 0x5

[ 90](pinctrl-rx_8h.md#a0418b8e109dccab2a5b39b73c8d34de6)#define RX\_PSEL\_P2nPFS\_TMCI3 0x5

91

[ 92](pinctrl-rx_8h.md#aa59954a10be331a3adf63cae63cc6781)#define RX\_PSEL\_P2nPFS\_ADTRG0 0x9

93

[ 94](pinctrl-rx_8h.md#a644d0126190885ca9dbdfe09d3891911)#define RX\_PSEL\_P2nPFS\_RXD0 0xA

[ 95](pinctrl-rx_8h.md#a3c7dbd625604d3baab379953eecd4dd2)#define RX\_PSEL\_P2nPFS\_SMISO0 0xA

[ 96](pinctrl-rx_8h.md#acb6c1ab729ac222872edcac9be75388d)#define RX\_PSEL\_P2nPFS\_SSCL0 0xA

[ 97](pinctrl-rx_8h.md#a296d05ae948f7bd999ad5549e9923af6)#define RX\_PSEL\_P2nPFS\_TXD0 0xA

[ 98](pinctrl-rx_8h.md#a2fc0d75b547deee80cc88f4c15497873)#define RX\_PSEL\_P2nPFS\_SMOSI0 0xA

[ 99](pinctrl-rx_8h.md#a53817593b75446ddd77490d5144d07f3)#define RX\_PSEL\_P2nPFS\_SSDA0 0xA

[ 100](pinctrl-rx_8h.md#a8f18c698cfc5111ece10aada38e8ed0b)#define RX\_PSEL\_P2nPFS\_SCK0 0xA

[ 101](pinctrl-rx_8h.md#a52375313e6b8333693f42925fa875061)#define RX\_PSEL\_P2nPFS\_TXD1 0xA

[ 102](pinctrl-rx_8h.md#ad5241521982236501d3f59c315a212a7)#define RX\_PSEL\_P2nPFS\_SMOSI1 0xA

[ 103](pinctrl-rx_8h.md#ae3dbbed0bf6c3c928668fdcdfb8c2bd2)#define RX\_PSEL\_P2nPFS\_SSDA1 0xA

[ 104](pinctrl-rx_8h.md#a3d23cbbaffcfce61a09c552d128ade85)#define RX\_PSEL\_P2nPFS\_SCK1 0xA

105

[ 106](pinctrl-rx_8h.md#af620f79d871fceafd43648bbf482ff74)#define RX\_PSEL\_P2nPFS\_CTS0 0xB

[ 107](pinctrl-rx_8h.md#aa35d75b72a5aab5dd3ca61f158c401df)#define RX\_PSEL\_P2nPFS\_RTS0 0xB

[ 108](pinctrl-rx_8h.md#a963049f6db48bb8d470dc20f1af0b229)#define RX\_PSEL\_P2nPFS\_SS0 0xB

109

[ 110](pinctrl-rx_8h.md#aa6b377d29e609a0a6cf9314f792a84c0)#define RX\_PSEL\_P2nPFS\_TS3 0x19

[ 111](pinctrl-rx_8h.md#a9c4eb492ef55cbe8294b9a785e178ac8)#define RX\_PSEL\_P2nPFS\_TS4 0x19

112

113/\* P3nPFS \*/

[ 114](pinctrl-rx_8h.md#a912cf155ad9b90d57cc2e54b5bc5f08a)#define RX\_PSEL\_P3nPFS\_MTIOC0A 0x01

[ 115](pinctrl-rx_8h.md#a94532f7a2a10d1ab8e2ba677e2697026)#define RX\_PSEL\_P3nPFS\_MTIOC0C 0x01

[ 116](pinctrl-rx_8h.md#a64da185fff98b3917f8895dd5d7baf65)#define RX\_PSEL\_P3nPFS\_MTIOC0D 0x01

[ 117](pinctrl-rx_8h.md#a7ee97491a03815f769f10104fb8f3abc)#define RX\_PSEL\_P3nPFS\_MTIOC4B 0x01

[ 118](pinctrl-rx_8h.md#addb1546bf2cf2f44ffc69e763ac977ee)#define RX\_PSEL\_P3nPFS\_MTIOC4D 0x01

119

[ 120](pinctrl-rx_8h.md#a5cfb12676b99d16d7602d510f182b5cb)#define RX\_PSEL\_P3nPFS\_TMCI2 0x5

[ 121](pinctrl-rx_8h.md#a9071547e298af703f78fb8602d479ac6)#define RX\_PSEL\_P3nPFS\_TMO3 0x5

[ 122](pinctrl-rx_8h.md#aa93265941791184b4aede61f922c2b18)#define RX\_PSEL\_P3nPFS\_TMRI3 0x5

[ 123](pinctrl-rx_8h.md#a9861a7bd48e1ec94eca541d230164874)#define RX\_PSEL\_P3nPFS\_TMCI3 0x5

124

[ 125](pinctrl-rx_8h.md#ae61abf1a2343b39ffd50aa4f1cea1437)#define RX\_PSEL\_P3nPFS\_RTCOUT 0x7

[ 126](pinctrl-rx_8h.md#a9d29e69cf44686dc6acf2876fae48ea5)#define RX\_PSEL\_P3nPFS\_POE2 0x7

[ 127](pinctrl-rx_8h.md#a7549ce5ac03ef03c97b13d7421540c02)#define RX\_PSEL\_P3nPFS\_POE3 0x7

[ 128](pinctrl-rx_8h.md#aedd2d3acb9455157b0f9920911af5c10)#define RX\_PSEL\_P3nPFS\_POE8 0x7

129

[ 130](pinctrl-rx_8h.md#ae0da688c9e0bb84b4862d194269bec2a)#define RX\_PSEL\_P3nPFS\_RXD1 0xA

[ 131](pinctrl-rx_8h.md#a89adb49de0a99e0548e8ed242d4f0b62)#define RX\_PSEL\_P3nPFS\_SMISO1 0xA

[ 132](pinctrl-rx_8h.md#a43f68e75a17d68fde57806db3691c3b2)#define RX\_PSEL\_P3nPFS\_SSCL1 0xA

133

[ 134](pinctrl-rx_8h.md#a08e879eb32d7096f08827e121e92fe50)#define RX\_PSEL\_P3nPFS\_CTS1 0xB

[ 135](pinctrl-rx_8h.md#a6366c1fd6ad7e5d5ed540d25ca00e836)#define RX\_PSEL\_P3nPFS\_RTS1 0xB

[ 136](pinctrl-rx_8h.md#af53411085e8857438e5c9abb7888079f)#define RX\_PSEL\_P3nPFS\_SS1 0xB

[ 137](pinctrl-rx_8h.md#aac363230de113bd65dd17fe3b05c0a45)#define RX\_PSEL\_P3nPFS\_RXD6 0xB

[ 138](pinctrl-rx_8h.md#afcefa777d2064118ed7aec73bac19f08)#define RX\_PSEL\_P3nPFS\_SMISO6 0xB

[ 139](pinctrl-rx_8h.md#a2d42e557aa6ba6e3ac2adb7215618935)#define RX\_PSEL\_P3nPFS\_SSCL6 0xB

[ 140](pinctrl-rx_8h.md#ae57aed1d69d9e791943206ea9c75eedc)#define RX\_PSEL\_P3nPFS\_TXD6 0xB

[ 141](pinctrl-rx_8h.md#abd8dde16e830b4d61be34bde6c8552d2)#define RX\_PSEL\_P3nPFS\_SMOSI6 0xB

[ 142](pinctrl-rx_8h.md#aebd62a6fd208525bac61b7c198578f23)#define RX\_PSEL\_P3nPFS\_SSDA6 0xB

[ 143](pinctrl-rx_8h.md#a523ea0495c5667c4acb97100bcb81373)#define RX\_PSEL\_P3nPFS\_SCK6 0xB

144

[ 145](pinctrl-rx_8h.md#a9b1b5dfc5099562d6965bf801b00c71d)#define RX\_PSEL\_P3nPFS\_TS0 0x19

[ 146](pinctrl-rx_8h.md#a04794c793e252a3d9d260bc7902295ba)#define RX\_PSEL\_P3nPFS\_TS1 0x19

[ 147](pinctrl-rx_8h.md#ac8312cdd9d396e15081d5873b5f25afd)#define RX\_PSEL\_P3nPFS\_TS2 0x19

148

149/\* P5nPFS \*/

[ 150](pinctrl-rx_8h.md#a142d0481f6512159c7f280419834f96f)#define RX\_PSEL\_P5nPFS\_MTIOC4B 0x01

[ 151](pinctrl-rx_8h.md#a73b2361a0599be381e5b234b852b1dec)#define RX\_PSEL\_P5nPFS\_MTIOC4D 0x01

152

[ 153](pinctrl-rx_8h.md#a384f77f5ef58df21c990ec1f244a582d)#define RX\_PSEL\_P5nPFS\_TMCI1 0x5

[ 154](pinctrl-rx_8h.md#aeb2b78345a96979b0938c17f032739cc)#define RX\_PSEL\_P5nPFS\_TMO3 0x5

155

[ 156](pinctrl-rx_8h.md#aee8c3bbb3a4341bf23aae2376c0d63da)#define RX\_PSEL\_P5nPFS\_TS11 0x19

[ 157](pinctrl-rx_8h.md#a1fae9f412c3a00786292e6a55a480ea0)#define RX\_PSEL\_P5nPFS\_TS12 0x19

158

[ 159](pinctrl-rx_8h.md#a3f85d862897a3ed788adbac2dcdfd3ce)#define RX\_PSEL\_P5nPFS\_PMC0 0x19

[ 160](pinctrl-rx_8h.md#a1813788221910ec1a0e1065d3745864c)#define RX\_PSEL\_P5nPFS\_PMC1 0x19

161

162/\* PAnPFS \*/

[ 163](pinctrl-rx_8h.md#a87c47d0c6734ce3547b23754234502f4)#define RX\_PSEL\_PAnPFS\_MTIOC4A 0x01

[ 164](pinctrl-rx_8h.md#a884e497ea0370a0fd1fdd351f5b6a786)#define RX\_PSEL\_PAnPFS\_MTIOC0B 0x01

[ 165](pinctrl-rx_8h.md#a2b8d4b23f5172d4798e8519644e35e9a)#define RX\_PSEL\_PAnPFS\_MTIOC0D 0x01

[ 166](pinctrl-rx_8h.md#aba913f6670da680ac45030c6ec6f427a)#define RX\_PSEL\_PAnPFS\_MTIOC5U 0x01

[ 167](pinctrl-rx_8h.md#a475663b42a042fe06c9f340e3e63adb1)#define RX\_PSEL\_PAnPFS\_MTIOC5V 0x01

168

[ 169](pinctrl-rx_8h.md#af579ae4fd94b09b8d76a9f8f89e6acb3)#define RX\_PSEL\_PAnPFS\_MTCLKA 0x02

[ 170](pinctrl-rx_8h.md#a8b47dba63dd54bd6a7034fae4b875d15)#define RX\_PSEL\_PAnPFS\_MTCLKB 0x02

[ 171](pinctrl-rx_8h.md#a82fd05e3e993fb86fc4d18a5ec7cddc6)#define RX\_PSEL\_PAnPFS\_MTCLKC 0x02

[ 172](pinctrl-rx_8h.md#a970d467907e0c4e8829f20eb0de9e4c4)#define RX\_PSEL\_PAnPFS\_MTCLKD 0x02

173

[ 174](pinctrl-rx_8h.md#a50d18bf6681275da284b2348aaa626d7)#define RX\_PSEL\_PAnPFS\_TMRI0 0x5

[ 175](pinctrl-rx_8h.md#a26ce828aab38d7005ae7ccf5d3809f1e)#define RX\_PSEL\_PAnPFS\_TMCI3 0x5

176

[ 177](pinctrl-rx_8h.md#a3985ebc7577dc17f64ab2e2c0a676910)#define RX\_PSEL\_PAnPFS\_POE2 0x7

[ 178](pinctrl-rx_8h.md#ac0c66c71e791fbcdf75a15c1acc58bc2)#define RX\_PSEL\_PAnPFS\_CACREF 0x7

179

[ 180](pinctrl-rx_8h.md#a819aa2b70f2cbb0165c93fc06b1784e2)#define RX\_PSEL\_PAnPFS\_RXD5 0xA

[ 181](pinctrl-rx_8h.md#aa7ffb4053ffa015c30a6906885a007bc)#define RX\_PSEL\_PAnPFS\_SMISO5 0xA

[ 182](pinctrl-rx_8h.md#a080fa1148d00016a8663f0adc0f3a81c)#define RX\_PSEL\_PAnPFS\_SSCL5 0xA

[ 183](pinctrl-rx_8h.md#a6cda040400df3fc63b2ea5b35b09347e)#define RX\_PSEL\_PAnPFS\_TXD5 0xA

[ 184](pinctrl-rx_8h.md#aadf3aca998e7796fb8724264966b1c17)#define RX\_PSEL\_PAnPFS\_SMOSI5 0xA

[ 185](pinctrl-rx_8h.md#ab5eec46fe3c3ec8a79b78d6f14652631)#define RX\_PSEL\_PAnPFS\_SSDA5 0xA

[ 186](pinctrl-rx_8h.md#a4a358940161583dac3d6e99e5a65da7a)#define RX\_PSEL\_PAnPFS\_SCK5 0xA

187

[ 188](pinctrl-rx_8h.md#aca996f81268ef4573b837b4da0491ef4)#define RX\_PSEL\_PAnPFS\_CTS5 0xB

[ 189](pinctrl-rx_8h.md#a2a3f02bd3a18a96355ecc8c6aca215bd)#define RX\_PSEL\_PAnPFS\_RTS5 0xB

[ 190](pinctrl-rx_8h.md#acdbcff26b1e0c1ec95904359831101a6)#define RX\_PSEL\_PAnPFS\_SS5 0xB

191

[ 192](pinctrl-rx_8h.md#ac5a1bb8cc48cc3975e989d0ae8301b85)#define RX\_PSEL\_PAnPFS\_SSLA0 0xD

[ 193](pinctrl-rx_8h.md#a695b1d61fa2af644e8e713bde9008b67)#define RX\_PSEL\_PAnPFS\_SSLA1 0xD

[ 194](pinctrl-rx_8h.md#a4f9ce98bb1087fdfa8a4820dec774b88)#define RX\_PSEL\_PAnPFS\_SSLA2 0xD

[ 195](pinctrl-rx_8h.md#a4a1682361951b36cbaca4a469ede48d7)#define RX\_PSEL\_PAnPFS\_SSLA3 0xD

[ 196](pinctrl-rx_8h.md#a3001136d224d46c165f437e44733457b)#define RX\_PSEL\_PAnPFS\_RSPCKA 0xD

[ 197](pinctrl-rx_8h.md#abcf66e981b8dce6df3552dfe23f87440)#define RX\_PSEL\_PAnPFS\_MOSIA 0xD

[ 198](pinctrl-rx_8h.md#abc8dccd90af6bfbb74012df17f256709)#define RX\_PSEL\_PAnPFS\_MISOA 0xD

199

[ 200](pinctrl-rx_8h.md#a09b4a8fe6520da1a3239890590ef90d3)#define RX\_PSEL\_PAnPFS\_TS26 0x19

[ 201](pinctrl-rx_8h.md#a988e53dc6d5a7c139747be285598fe96)#define RX\_PSEL\_PAnPFS\_TS27 0x19

[ 202](pinctrl-rx_8h.md#ae00078451e050502337206f9bd6362bc)#define RX\_PSEL\_PAnPFS\_TS28 0x19

[ 203](pinctrl-rx_8h.md#a67cf8ad3d73c35f2659a2af3f5b3d6f3)#define RX\_PSEL\_PAnPFS\_TS29 0x19

[ 204](pinctrl-rx_8h.md#a4b080b72196e98924c3a9d02b2d1756e)#define RX\_PSEL\_PAnPFS\_TS30 0x19

[ 205](pinctrl-rx_8h.md#a8b434c0a6b494ab4020b49c8df2707c0)#define RX\_PSEL\_PAnPFS\_TS31 0x19

[ 206](pinctrl-rx_8h.md#a0b2a031acfb9f73f5e34d58d1bf21a3e)#define RX\_PSEL\_PAnPFS\_TS32 0x19

207

208/\* PBnPFS \*/

[ 209](pinctrl-rx_8h.md#ab70484c773d08b3331e93d5f16e74e8a)#define RX\_PSEL\_PBnPFS\_MTIOC0A 0x01

[ 210](pinctrl-rx_8h.md#aa16664b39a03dc8f5cf1eff2df22d132)#define RX\_PSEL\_PBnPFS\_MTIOC0C 0x01

[ 211](pinctrl-rx_8h.md#a78103875ae7f2bf781da23c8033fed59)#define RX\_PSEL\_PBnPFS\_MTIOC2A 0x01

[ 212](pinctrl-rx_8h.md#a1e5ccf9190a3dc5970f4254d737ae072)#define RX\_PSEL\_PBnPFS\_MTIOC3B 0x01

[ 213](pinctrl-rx_8h.md#ae583a13420640109ebe70590b4d499ba)#define RX\_PSEL\_PBnPFS\_MTIOC3D 0x01

[ 214](pinctrl-rx_8h.md#a151d204a2e111718abf98b37a5c30d02)#define RX\_PSEL\_PBnPFS\_MTIOC5W 0x01

215

[ 216](pinctrl-rx_8h.md#a867fdf6ad0579c0022dc82999e161db6)#define RX\_PSEL\_PBnPFS\_MTIOC1B 0x02

[ 217](pinctrl-rx_8h.md#a021849717993b6ddcd5944b737a2aaf4)#define RX\_PSEL\_PBnPFS\_MTIOC4A 0x02

[ 218](pinctrl-rx_8h.md#a3375281ff859dfe401d503032a1d6b80)#define RX\_PSEL\_PBnPFS\_MTIOC4C 0x02

219

[ 220](pinctrl-rx_8h.md#a5e3a37d153b356ae71c638fc7010a9f7)#define RX\_PSEL\_PBnPFS\_TMO0 0x5

[ 221](pinctrl-rx_8h.md#aafc8cd3f09a9fc7b8cc3f59403ed514d)#define RX\_PSEL\_PBnPFS\_TMRI1 0x5

[ 222](pinctrl-rx_8h.md#a1bfa8645f34a063435061facc3c4736a)#define RX\_PSEL\_PBnPFS\_TMCI0 0x5

223

[ 224](pinctrl-rx_8h.md#a7deea898404b855145576f716f851a92)#define RX\_PSEL\_PBnPFS\_POE1 0x7

[ 225](pinctrl-rx_8h.md#aaef5911c5707323f20fec35fec6bdea2)#define RX\_PSEL\_PBnPFS\_POE3 0x7

226

[ 227](pinctrl-rx_8h.md#a3560ff40295f809b6035026957014457)#define RX\_PSEL\_PBnPFS\_RXD9 0xA

[ 228](pinctrl-rx_8h.md#a95fa86bdf6128a0c911cf3258dcac3c5)#define RX\_PSEL\_PBnPFS\_SMISO9 0xA

[ 229](pinctrl-rx_8h.md#abbc0966da3e8a31b0862639c73d298ee)#define RX\_PSEL\_PBnPFS\_SSCL9 0xA

[ 230](pinctrl-rx_8h.md#a6a8de4826f40799a5377d6b0ddba973b)#define RX\_PSEL\_PBnPFS\_TXD9 0xA

[ 231](pinctrl-rx_8h.md#a47f17b912597e5cb66846711e37f9b6d)#define RX\_PSEL\_PBnPFS\_SMOSI9 0xA

[ 232](pinctrl-rx_8h.md#a2e06bb5584c33d2124e2fc6e2b0ed381)#define RX\_PSEL\_PBnPFS\_SSDA9 0xA

[ 233](pinctrl-rx_8h.md#a3ebc1ec3ce34c09b02698b4cbb3ef0ce)#define RX\_PSEL\_PBnPFS\_SCK9 0xA

234

[ 235](pinctrl-rx_8h.md#a2fdd18ec059ab4e4d8a2284b16f8c160)#define RX\_PSEL\_PBnPFS\_CTS6 0xB

[ 236](pinctrl-rx_8h.md#a4cf58353b52de3273826db6666c94cba)#define RX\_PSEL\_PBnPFS\_RTS6 0xB

[ 237](pinctrl-rx_8h.md#aa543049ed2b1ad9e216ce6e85fcee876)#define RX\_PSEL\_PBnPFS\_SS6 0xB

[ 238](pinctrl-rx_8h.md#afc347de58db4d6795ded3a76afb1abf6)#define RX\_PSEL\_PBnPFS\_CTS9 0xB

[ 239](pinctrl-rx_8h.md#aefb72d4fad4867bcd5fef242322fdb46)#define RX\_PSEL\_PBnPFS\_RTS9 0xB

[ 240](pinctrl-rx_8h.md#a8c2cef051d3a5db19460d89c608c6233)#define RX\_PSEL\_PBnPFS\_SS9 0xB

[ 241](pinctrl-rx_8h.md#aad2ab397717736311073efe4bad48818)#define RX\_PSEL\_PBnPFS\_RXD6 0xB

[ 242](pinctrl-rx_8h.md#a7e9537931de468389d51b0355754ab1f)#define RX\_PSEL\_PBnPFS\_SMISO6 0xB

[ 243](pinctrl-rx_8h.md#a78aa89352d217d85b4f36bd55cc202a5)#define RX\_PSEL\_PBnPFS\_SSCL6 0xB

[ 244](pinctrl-rx_8h.md#a514b3b4d6eefd9ae830f3ea29e69b07b)#define RX\_PSEL\_PBnPFS\_TXD6 0xB

[ 245](pinctrl-rx_8h.md#af3c3885de61f44965d296f35aeae8f78)#define RX\_PSEL\_PBnPFS\_SMOSI6 0xB

[ 246](pinctrl-rx_8h.md#afe28b85756fab74733b87fa10ee63d8e)#define RX\_PSEL\_PBnPFS\_SSDA6 0xB

[ 247](pinctrl-rx_8h.md#a8b6978e1aebd1fcd55c7a543a38496ba)#define RX\_PSEL\_PBnPFS\_SCK6 0xB

248

[ 249](pinctrl-rx_8h.md#a9d01bbc858e16531b932ba4a10783e03)#define RX\_PSEL\_PBnPFS\_RSPCKA 0xD

250

[ 251](pinctrl-rx_8h.md#a230a3999d4881be6074e4380107075ce)#define RX\_PSEL\_PBnPFS\_CMPOB1 0x10

252

[ 253](pinctrl-rx_8h.md#a7b4f647d5bdfb3fb8a2107949629994a)#define RX\_PSEL\_PBnPFS\_TS18 0x19

[ 254](pinctrl-rx_8h.md#ad356f13b07220a235c1f971d2b1ab7ea)#define RX\_PSEL\_PBnPFS\_TS19 0x19

[ 255](pinctrl-rx_8h.md#a364a18874eefb53563242194d1150910)#define RX\_PSEL\_PBnPFS\_TS20 0x19

[ 256](pinctrl-rx_8h.md#a0342b766bac5038c1fc6134a7d1bd85f)#define RX\_PSEL\_PBnPFS\_TS21 0x19

[ 257](pinctrl-rx_8h.md#a3db09a4ebeee6872100e3916a160b099)#define RX\_PSEL\_PBnPFS\_TS22 0x19

[ 258](pinctrl-rx_8h.md#a66af16b3b335123ccda6d1ad5efda434)#define RX\_PSEL\_PBnPFS\_TS23 0x19

[ 259](pinctrl-rx_8h.md#a4ddfb9a65c9dc5b58e08e48be2171664)#define RX\_PSEL\_PBnPFS\_TS24 0x19

[ 260](pinctrl-rx_8h.md#a79f5033bf88f0d42632e70de11990c13)#define RX\_PSEL\_PBnPFS\_TS25 0x19

261

262/\* PCnPFS \*/

[ 263](pinctrl-rx_8h.md#a0a0e1289dc503260b7d4d9ad99813bcf)#define RX\_PSEL\_PCnPFS\_MTIOC3A 0x01

[ 264](pinctrl-rx_8h.md#accdce2d8f48796e5eaa7b6cf4bdaf225)#define RX\_PSEL\_PCnPFS\_MTIOC3B 0x01

[ 265](pinctrl-rx_8h.md#a9a281dbe06b3123d1afb0809df50d188)#define RX\_PSEL\_PCnPFS\_MTIOC3C 0x01

[ 266](pinctrl-rx_8h.md#adfa80b9c6df7c803e6d158e9825f7931)#define RX\_PSEL\_PCnPFS\_MTIOC3D 0x01

[ 267](pinctrl-rx_8h.md#a3878479bf2dc042792d6174496038207)#define RX\_PSEL\_PCnPFS\_MTIOC4B 0x01

[ 268](pinctrl-rx_8h.md#ac25138271990797712728f0e5d5909e6)#define RX\_PSEL\_PCnPFS\_MTIOC4D 0x01

269

[ 270](pinctrl-rx_8h.md#a9e0b4711dd92fdff630516fc963187c6)#define RX\_PSEL\_PCnPFS\_MTCLKA 0x02

[ 271](pinctrl-rx_8h.md#a73c23ead228baca49158d7486ec7f0e0)#define RX\_PSEL\_PCnPFS\_MTCLKB 0x02

[ 272](pinctrl-rx_8h.md#abc55942f4d533288287d602ec46a3384)#define RX\_PSEL\_PCnPFS\_MTCLKC 0x02

[ 273](pinctrl-rx_8h.md#a2e9e94477161bfbd4ece9e926c6b20f3)#define RX\_PSEL\_PCnPFS\_MTCLKD 0x02

274

[ 275](pinctrl-rx_8h.md#aad2d8d27f0b4bcc06c69d60f4ba32415)#define RX\_PSEL\_PCnPFS\_TMCI1 0x5

[ 276](pinctrl-rx_8h.md#aeb895a0766941862427dcfe548fe795b)#define RX\_PSEL\_PCnPFS\_TMO2 0x5

[ 277](pinctrl-rx_8h.md#aa9ca76efaf979f4f1bacb444a93c2338)#define RX\_PSEL\_PCnPFS\_TMRI2 0x5

[ 278](pinctrl-rx_8h.md#a104b8044a91acadbb73c6fedd01e3128)#define RX\_PSEL\_PCnPFS\_TMCI2 0x5

279

[ 280](pinctrl-rx_8h.md#af7fbf061ff82639825805cc3cca28a0b)#define RX\_PSEL\_PCnPFS\_POE0 0x7

[ 281](pinctrl-rx_8h.md#af33cdb03242b52a66aa312834f738ab1)#define RX\_PSEL\_PCnPFS\_CACREF 0x7

282

[ 283](pinctrl-rx_8h.md#a5a69027c56b05fab8d7d53a6880b9423)#define RX\_PSEL\_PCnPFS\_RXD5 0xA

[ 284](pinctrl-rx_8h.md#a392276adc9abd36a582d590446f96038)#define RX\_PSEL\_PCnPFS\_SMISO5 0xA

[ 285](pinctrl-rx_8h.md#a2437838e9799abd2b17b6376675e70ca)#define RX\_PSEL\_PCnPFS\_SSCL5 0xA

[ 286](pinctrl-rx_8h.md#a3d8cb88bf920515954d3833b2d5e90f9)#define RX\_PSEL\_PCnPFS\_TXD5 0xA

[ 287](pinctrl-rx_8h.md#aa346eb221834f7e0df6d778da6ec35cd)#define RX\_PSEL\_PCnPFS\_SMOSI5 0xA

[ 288](pinctrl-rx_8h.md#a4f2bc6a3a5b8561f37f778fa577ac0e8)#define RX\_PSEL\_PCnPFS\_SSDA5 0xA

[ 289](pinctrl-rx_8h.md#a01d49d963a3136acef38a2a831a076a1)#define RX\_PSEL\_PCnPFS\_SCK5 0xA

[ 290](pinctrl-rx_8h.md#a86211091c53c6dbbdd657bce75e70986)#define RX\_PSEL\_PCnPFS\_RXD8 0xA

[ 291](pinctrl-rx_8h.md#ae44a9ac365c5d056ee2921a5c4bcb5ee)#define RX\_PSEL\_PCnPFS\_SMISO8 0xA

[ 292](pinctrl-rx_8h.md#a8990d81f5d74427c71cc37eee6647c98)#define RX\_PSEL\_PCnPFS\_SSCL8 0xA

[ 293](pinctrl-rx_8h.md#a257eaa3c131105d680ff05e9def319c4)#define RX\_PSEL\_PCnPFS\_TXD8 0xA

[ 294](pinctrl-rx_8h.md#a953ca81bde404c7f9a159725a090af04)#define RX\_PSEL\_PCnPFS\_SMOSI8 0xA

[ 295](pinctrl-rx_8h.md#a8cba60fc83718e0dde6361fcf2fb9a5c)#define RX\_PSEL\_PCnPFS\_SSDA8 0xA

[ 296](pinctrl-rx_8h.md#aff658c7c324fa5bf4461b7436aa97e5c)#define RX\_PSEL\_PCnPFS\_SCK8 0xA

297

[ 298](pinctrl-rx_8h.md#a20997f4c8188883ca8b1094a0b7e873b)#define RX\_PSEL\_PCnPFS\_CTS5 0xB

[ 299](pinctrl-rx_8h.md#a5d8408785316cd7187e5fda2f7cf4152)#define RX\_PSEL\_PCnPFS\_RTS5 0xB

[ 300](pinctrl-rx_8h.md#a73b65f6a77adb07c2f17d1589f5e5d68)#define RX\_PSEL\_PCnPFS\_SS5 0xB

[ 301](pinctrl-rx_8h.md#a0fa3dde24d9c4f689237a5e21153efcc)#define RX\_PSEL\_PCnPFS\_CTS8 0xB

[ 302](pinctrl-rx_8h.md#a97c6a44c096c0c5873e7a57f9c956083)#define RX\_PSEL\_PCnPFS\_RTS8 0xB

[ 303](pinctrl-rx_8h.md#a0b5c3248fe7278e43a9dab8bb47b347c)#define RX\_PSEL\_PCnPFS\_SS8 0xB

304

[ 305](pinctrl-rx_8h.md#a3b5990fb7b76f0befd197dac661a9036)#define RX\_PSEL\_PCnPFS\_SSLA0 0xD

[ 306](pinctrl-rx_8h.md#af7ca895592d0ac3d46cddcc40c315f70)#define RX\_PSEL\_PCnPFS\_SSLA1 0xD

[ 307](pinctrl-rx_8h.md#af563abf494e2730c8895b3fb4de6c85a)#define RX\_PSEL\_PCnPFS\_SSLA2 0xD

[ 308](pinctrl-rx_8h.md#a1c74ab46805e2ec72c1477059aa7c6f4)#define RX\_PSEL\_PCnPFS\_SSLA3 0xD

[ 309](pinctrl-rx_8h.md#ac88a47a2634a1f730fe58009d277c56d)#define RX\_PSEL\_PCnPFS\_RSPCKA 0xD

[ 310](pinctrl-rx_8h.md#aca94166ceb510874373df19e74c1e171)#define RX\_PSEL\_PCnPFS\_MOSIA 0xD

[ 311](pinctrl-rx_8h.md#ac8c1b07159883e4c934ce5e2bd61d057)#define RX\_PSEL\_PCnPFS\_MISOA 0xD

312

[ 313](pinctrl-rx_8h.md#a0f4ba5772ff554184551e10371af83ba)#define RX\_PSEL\_PCnPFS\_TS13 0x19

[ 314](pinctrl-rx_8h.md#a5b61df843dcd7e9e4bc5d6e275ebb99c)#define RX\_PSEL\_PCnPFS\_TS14 0x19

[ 315](pinctrl-rx_8h.md#a1c12baa481da0305da0e91d4eb3a2c31)#define RX\_PSEL\_PCnPFS\_TS15 0x19

[ 316](pinctrl-rx_8h.md#a6283542c2054052770c40941cffd508e)#define RX\_PSEL\_PCnPFS\_TS16 0x19

[ 317](pinctrl-rx_8h.md#ae70d84e57e3293b2916db85ffd91e7a1)#define RX\_PSEL\_PCnPFS\_TS17 0x19

[ 318](pinctrl-rx_8h.md#a77444df0b11d61ceb285b18600032e88)#define RX\_PSEL\_PCnPFS\_TSCAP 0x19

319

320/\* PDnPFS \*/

[ 321](pinctrl-rx_8h.md#aafbb53acfb95de11fdf6a75e75c3fc97)#define RX\_PSEL\_PDnPFS\_MTIOC4B 0x01

[ 322](pinctrl-rx_8h.md#ac3de35bbc1a916e8449698eb24a34cec)#define RX\_PSEL\_PDnPFS\_MTIOC4D 0x01

[ 323](pinctrl-rx_8h.md#a7a096c87787f645323ca16bd1ae3bac6)#define RX\_PSEL\_PDnPFS\_MTIOC5W 0x01

[ 324](pinctrl-rx_8h.md#a45c847394001f31be768944b7acaf906)#define RX\_PSEL\_PDnPFS\_MTIOC5V 0x01

[ 325](pinctrl-rx_8h.md#ab5f02479510f1babd64ba6cbb169f42c)#define RX\_PSEL\_PDnPFS\_MTIOC5U 0x01

326

[ 327](pinctrl-rx_8h.md#a2a77be1f3443daaab5f4b3066c1f8278)#define RX\_PSEL\_PDnPFS\_POE0 0x7

[ 328](pinctrl-rx_8h.md#af94b267110bc98221219a97c58f4e697)#define RX\_PSEL\_PDnPFS\_POE1 0x7

[ 329](pinctrl-rx_8h.md#a267d05d58ffcab0f60ae8427f8aecaf2)#define RX\_PSEL\_PDnPFS\_POE2 0x7

[ 330](pinctrl-rx_8h.md#ae0e7f8f472d0f64c2dd328b57615dc98)#define RX\_PSEL\_PDnPFS\_POE3 0x7

[ 331](pinctrl-rx_8h.md#a6c9a976cb22cc6b0e69d9d31b41e0321)#define RX\_PSEL\_PDnPFS\_POE8 0x7

332

[ 333](pinctrl-rx_8h.md#a9733d54b731df033e6c1eda5293c5317)#define RX\_PSEL\_PDnPFS\_RXD6 0xB

[ 334](pinctrl-rx_8h.md#aa2f83777eb6e976f0451786a1f6edceb)#define RX\_PSEL\_PDnPFS\_SMISO6 0xB

[ 335](pinctrl-rx_8h.md#a3d03c22b4f7adbb20f10208e471ce276)#define RX\_PSEL\_PDnPFS\_SSCL6 0xB

[ 336](pinctrl-rx_8h.md#a8ae0cab25d78a40565870fc28428def3)#define RX\_PSEL\_PDnPFS\_TXD6 0xB

[ 337](pinctrl-rx_8h.md#a8f5941502abad2c8995bc57b986ca81f)#define RX\_PSEL\_PDnPFS\_SMOSI6 0xB

[ 338](pinctrl-rx_8h.md#a88acb98416906f6abdf2f6172d80bdaf)#define RX\_PSEL\_PDnPFS\_SSDA6 0xB

[ 339](pinctrl-rx_8h.md#a3e318ee5f28ce26bbd73dabed4b1a44a)#define RX\_PSEL\_PDnPFS\_SCK6 0xB

340

341/\* PEnPFS \*/

[ 342](pinctrl-rx_8h.md#a57abebe2638d36ca13d2d72d65436497)#define RX\_PSEL\_PEnPFS\_MTIOC4A 0x01

[ 343](pinctrl-rx_8h.md#a51e4a949c884b35891f1503e489291e8)#define RX\_PSEL\_PEnPFS\_MTIOC4B 0x01

[ 344](pinctrl-rx_8h.md#a6ef5a9460e67440d1f4e82c13fef35bf)#define RX\_PSEL\_PEnPFS\_MTIOC4C 0x01

[ 345](pinctrl-rx_8h.md#a2f800b39f958ec49897fb7d3b0a1574f)#define RX\_PSEL\_PEnPFS\_MTIOC4D 0x01

346

[ 347](pinctrl-rx_8h.md#a989c6f0452e964e6a6875b4924339b22)#define RX\_PSEL\_PEnPFS\_MTIOC1A 0x02

[ 348](pinctrl-rx_8h.md#a967c82a27a33b39b1ba1ae051090e6db)#define RX\_PSEL\_PEnPFS\_MTIOC2B 0x02

349

[ 350](pinctrl-rx_8h.md#a53a29ae9db04f7dab6bced306a47cfac)#define RX\_PSEL\_PEnPFS\_POE8 0x7

351

[ 352](pinctrl-rx_8h.md#a2bf6e1d791920bd5b44f10b62fb12db4)#define RX\_PSEL\_PEnPFS\_CLKOUT 0x9

353

[ 354](pinctrl-rx_8h.md#a85764cf1f6755fe00531703e20f9a587)#define RX\_PSEL\_PEnPFS\_RXD12 0xC

[ 355](pinctrl-rx_8h.md#acbacde7e28a5160ec6190aee9f3b4706)#define RX\_PSEL\_PEnPFS\_SMISO12 0xC

[ 356](pinctrl-rx_8h.md#a582c1aad6d4ce2aae7d683cbd179950e)#define RX\_PSEL\_PEnPFS\_SSCL12 0xC

[ 357](pinctrl-rx_8h.md#a9a4f83a8487dfd0f32fb3180f71853b5)#define RX\_PSEL\_PEnPFS\_TXD12 0xC

[ 358](pinctrl-rx_8h.md#a6fed05bb93fd3a18a53372660a6faaff)#define RX\_PSEL\_PEnPFS\_SMOSI12 0xC

[ 359](pinctrl-rx_8h.md#ae63305a2e7c8d27d85c7702e5826c918)#define RX\_PSEL\_PEnPFS\_SSDA12 0xC

[ 360](pinctrl-rx_8h.md#af2cb8b0acdc39ba3a4a659394a6884e5)#define RX\_PSEL\_PEnPFS\_SCK12 0xC

[ 361](pinctrl-rx_8h.md#a08d429e3e500db8b87f95a11cc61bf66)#define RX\_PSEL\_PEnPFS\_TXDX12 0xC

[ 362](pinctrl-rx_8h.md#ad769da51c412edc773cad5f959364763)#define RX\_PSEL\_PEnPFS\_RXDX12 0xC

[ 363](pinctrl-rx_8h.md#a58da776438c101eb043756f40ef5259a)#define RX\_PSEL\_PEnPFS\_SIOX12 0xC

[ 364](pinctrl-rx_8h.md#a49ed2fbfbd7c155fc22f744b4426502a)#define RX\_PSEL\_PEnPFS\_CTS12 0xC

[ 365](pinctrl-rx_8h.md#a39012da0abc5634d6ae1c1964653f392)#define RX\_PSEL\_PEnPFS\_RTS12 0xC

[ 366](pinctrl-rx_8h.md#abc093255f500eb7bbc1aac866afe7ef6)#define RX\_PSEL\_PEnPFS\_SS12 0xC

367

[ 368](pinctrl-rx_8h.md#ac2d89df9365a11dd0388d122b11f2536)#define RX\_PSEL\_PEnPFS\_CMPOB0 0X10

369

[ 370](pinctrl-rx_8h.md#ad19b9859c60e5e84cf356a72048005d3)#define RX\_PSEL\_PEnPFS\_TS33 0X19

[ 371](pinctrl-rx_8h.md#a301d3eaf6cf49e216b3bf0759b789bea)#define RX\_PSEL\_PEnPFS\_TS34 0x19

[ 372](pinctrl-rx_8h.md#a9fbfd7aac05dfd05608264fa944c6287)#define RX\_PSEL\_PEnPFS\_TS35 0x19

373

374/\* PHnPFS \*/

[ 375](pinctrl-rx_8h.md#a84b2b05520efe0683f9db4e07155bfba)#define RX\_PSEL\_PHnPFS\_TMO0 0x05

[ 376](pinctrl-rx_8h.md#a6d8d96eaf1add151dd4629931fe61d1c)#define RX\_PSEL\_PHnPFS\_TMRI0 0x05

[ 377](pinctrl-rx_8h.md#a0026241158d3b5ecf428c4836a3d875f)#define RX\_PSEL\_PHnPFS\_TMCI0 0x05

378

[ 379](pinctrl-rx_8h.md#a6ebe5c08ff146f995ac212e1ea716742)#define RX\_PSEL\_PHnPFS\_CACREF 0x7

380

[ 381](pinctrl-rx_8h.md#aa8cfeedd877a6952f8d97a341da8d50d)#define RX\_PSEL\_PHnPFS\_TS7 0x19

[ 382](pinctrl-rx_8h.md#aeaf0f72ae91e634a1683a06e08b1f6c7)#define RX\_PSEL\_PHnPFS\_TS8 0x19

[ 383](pinctrl-rx_8h.md#a70dd840a2bba0791a151bc09c4be36f0)#define RX\_PSEL\_PHnPFS\_TS9 0x19

[ 384](pinctrl-rx_8h.md#a2c067233e929b0cec2b3d2a09097deae)#define RX\_PSEL\_PHnPFS\_TS10 0x19

385

386/\* PJnPFS \*/

[ 387](pinctrl-rx_8h.md#ad8dfc05cfc1d8415d91b29ffe39c9b96)#define RX\_PSEL\_PJnPFS\_MTIOC3A 0x01

[ 388](pinctrl-rx_8h.md#a580dc22127edf2f64729314f6dd7e910)#define RX\_PSEL\_PJnPFS\_MTIOC3C 0x01

389

[ 390](pinctrl-rx_8h.md#a089de182c44f003fe50d1d5be28fc69c)#define RX\_PSEL\_PJnPFS\_CTS6 0xB

[ 391](pinctrl-rx_8h.md#a196e453a63cbbb6be004b3deb11aebc7)#define RX\_PSEL\_PJnPFS\_TTS6 0xB

[ 392](pinctrl-rx_8h.md#a319993d775bb37dfcdfc545e358c6e6e)#define RX\_PSEL\_PJnPFS\_SS6 0xB

393

[ 394](pinctrl-rx_8h.md#ab1a754c6466137c60093291517676f24)#define RX\_PSEL(psel, port\_num, pin\_num) \

395 (psel << RX\_PSEL\_POS | pin\_num << RX\_PIN\_NUM\_POS | port\_num << RX\_PORT\_NUM\_POS)

396

397#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_PINCTRL\_SOC\_RX\_COMMON\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [pinctrl](dir_2c6c4fbd167577104b7f1b7148586168.md)
- [renesas](dir_17f48eb154be6cea623223db5de209e7.md)
- [pinctrl-rx.h](pinctrl-rx_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
