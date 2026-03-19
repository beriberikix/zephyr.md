---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/digilent-pmod_8h_source.html
original_path: doxygen/html/digilent-pmod_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

digilent-pmod.h

[Go to the documentation of this file.](digilent-pmod_8h.md)

1/\*

2 \* Copyright (c) 2023 Elektronikutvecklingsbyrån EUB AB

3 \* SPDX-License-Identifier: Apache-2.0

4 \*/

5

26

27#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_GPIO\_DIGILENT\_PMOD\_H\_

28#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_GPIO\_DIGILENT\_PMOD\_H\_

29

34

35/\* GPIO \*/

36

[ 43](digilent-pmod_8h.md#acdb27a6e2e72f1092d49f49f356bd43d)#define PMOD\_IO(n) ((n) - 1)

44

45/\* SPI \*/

46

[ 51](digilent-pmod_8h.md#a48eb79c05dcea7840d652b7614fbe904)#define PMOD\_SPI\_CS PMOD\_IO(1)

52

[ 57](digilent-pmod_8h.md#ac93de481c5b6daa4b356221afa388817)#define PMOD\_SPI\_MOSI PMOD\_IO(2)

58

[ 63](digilent-pmod_8h.md#aa1f12f927187670390a5d4dec0ebba8d)#define PMOD\_SPI\_MISO PMOD\_IO(3)

64

[ 69](digilent-pmod_8h.md#a29c5bc49f3083a3d3f5ed1480f631d19)#define PMOD\_SPI\_SCK PMOD\_IO(4)

70

71/\* Expanded SPI \*/

72

[ 77](digilent-pmod_8h.md#a370445d23f8953515b65605d7cc5e74a)#define PMOD\_EXP\_SPI\_CS PMOD\_IO(1)

78

[ 83](digilent-pmod_8h.md#a20fd09b2126ed280842bb31aeb945c29)#define PMOD\_EXP\_SPI\_MOSI PMOD\_IO(2)

84

[ 89](digilent-pmod_8h.md#a211303529f74cb0989dc0d842cf055b5)#define PMOD\_EXP\_SPI\_MISO PMOD\_IO(3)

90

[ 95](digilent-pmod_8h.md#a9f507e1078c0a0e47dfa1f3a8f38fa44)#define PMOD\_EXP\_SPI\_SCK PMOD\_IO(4)

96

[ 101](digilent-pmod_8h.md#afa8baff3ecfab732f6dc20bf48e9b180)#define PMOD\_EXP\_SPI\_INT PMOD\_IO(5)

102

[ 107](digilent-pmod_8h.md#a84399ae6d85fd84e74e5a2d0b6976118)#define PMOD\_EXP\_SPI\_RESET PMOD\_IO(6)

108

[ 113](digilent-pmod_8h.md#a3985b248e927887d3a941dd0325e6f38)#define PMOD\_EXP\_SPI\_CS2 PMOD\_IO(7)

114

[ 119](digilent-pmod_8h.md#abbcd91eacbb32ee1605aacf52a9410a6)#define PMOD\_EXP\_SPI\_CS3 PMOD\_IO(8)

120

121/\* Expanded UART \*/

122

[ 127](digilent-pmod_8h.md#a814bf19bb81bf9164029938ce6b4f17e)#define PMOD\_EXP\_UART\_INT PMOD\_IO(5)

128

[ 133](digilent-pmod_8h.md#a723647609938e4c52ff6f582167afb6b)#define PMOD\_EXP\_UART\_RESET PMOD\_IO(6)

134

135/\* H-bridge \*/

136

[ 141](digilent-pmod_8h.md#a09a158ba814da24543af82f2e4630888)#define PMOD\_HBRIDGE\_DIR PMOD\_IO(1)

142

[ 147](digilent-pmod_8h.md#afd050d415e10a29ae7125f28283b82a6)#define PMOD\_HBRIDGE\_EN PMOD\_IO(2)

148

149/\* Dual H-bridge \*/

150

[ 155](digilent-pmod_8h.md#a6b700242b6cc5e8f8e7af57c8da79757)#define PMOD\_DUAL\_HBRIDGE\_DIR1 PMOD\_IO(1)

156

[ 161](digilent-pmod_8h.md#a126cc48a2c01b25d4ed384c07d499389)#define PMOD\_DUAL\_HBRIDGE\_EN1 PMOD\_IO(2)

162

[ 167](digilent-pmod_8h.md#aef4dd3e547bb3f94258aa7d2746f5b6f)#define PMOD\_DUAL\_HBRIDGE\_DIR2 PMOD\_IO(3)

168

[ 173](digilent-pmod_8h.md#a8449577798dcf19e5530c84ddf2adb47)#define PMOD\_DUAL\_HBRIDGE\_EN2 PMOD\_IO(4)

174

175/\* Expanded dual H-bridge \*/

176

[ 181](digilent-pmod_8h.md#a417bce3a6076a8a00ff3fdafeda0b66e)#define PMOD\_EXP\_DUAL\_HBRIDGE\_DIR1 PMOD\_IO(1)

182

[ 187](digilent-pmod_8h.md#a7d9f088f338c345693d8a1cf8f312d32)#define PMOD\_EXP\_DUAL\_HBRIDGE\_EN1 PMOD\_IO(2)

188

[ 193](digilent-pmod_8h.md#af4d271f3a3addfb5cbda89bff1fa6cf0)#define PMOD\_EXP\_DUAL\_HBRIDGE\_DIR2 PMOD\_IO(5)

194

[ 199](digilent-pmod_8h.md#a6b21aeb28f7c9abfb4af142d1ca62730)#define PMOD\_EXP\_DUAL\_HBRIDGE\_EN2 PMOD\_IO(6)

200

201/\* I2C \*/

202

[ 207](digilent-pmod_8h.md#a32dffa0e863e07a2c793432a222fea36)#define PMOD\_I2C\_INT PMOD\_IO(1)

208

[ 213](digilent-pmod_8h.md#a2878169dfb9ae1a31de0f4594fa59821)#define PMOD\_I2C\_RESET PMOD\_IO(2)

214

[ 219](digilent-pmod_8h.md#ae10bd211e7a7a0fa73f1b5ba250efd36)#define PMOD\_I2C\_SCL PMOD\_IO(3)

220

[ 225](digilent-pmod_8h.md#a4fc8f68216833805395af7dc344f0c77)#define PMOD\_I2C\_SDA PMOD\_IO(4)

226

227#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_GPIO\_DIGILENT\_PMOD\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [gpio](dir_9486826309e816a7a1c2256ae23b5ea4.md)
- [digilent-pmod.h](digilent-pmod_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
