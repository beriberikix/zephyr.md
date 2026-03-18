---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/wifi__mgmt_8h_source.html
original_path: doxygen/html/wifi__mgmt_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

wifi\_mgmt.h

[Go to the documentation of this file.](wifi__mgmt_8h.md)

1/\*

2 \* Copyright (c) 2017 Intel Corporation.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

11

12#ifndef ZEPHYR\_INCLUDE\_NET\_WIFI\_MGMT\_H\_

13#define ZEPHYR\_INCLUDE\_NET\_WIFI\_MGMT\_H\_

14

15#include <[zephyr/net/net\_mgmt.h](net__mgmt_8h.md)>

16#include <[zephyr/net/wifi.h](wifi_8h.md)>

17#include <[zephyr/net/ethernet.h](ethernet_8h.md)>

18#include <[zephyr/net/offloaded\_netdev.h](offloaded__netdev_8h.md)>

19

20#ifdef \_\_cplusplus

21extern "C" {

22#endif

23

28

29/\* Management part definitions \*/

30

31#define \_NET\_WIFI\_LAYER NET\_MGMT\_LAYER\_L2

32#define \_NET\_WIFI\_CODE 0x156

33#define \_NET\_WIFI\_BASE (NET\_MGMT\_IFACE\_BIT | \

34 NET\_MGMT\_LAYER(\_NET\_WIFI\_LAYER) | \

35 NET\_MGMT\_LAYER\_CODE(\_NET\_WIFI\_CODE))

36#define \_NET\_WIFI\_EVENT (\_NET\_WIFI\_BASE | NET\_MGMT\_EVENT\_BIT)

37

38#ifdef CONFIG\_WIFI\_MGMT\_SCAN\_SSID\_FILT\_MAX

39#define WIFI\_MGMT\_SCAN\_SSID\_FILT\_MAX CONFIG\_WIFI\_MGMT\_SCAN\_SSID\_FILT\_MAX

40#else

[ 41](group__wifi__mgmt.md#ga8f1d15bfcd0776eee7cae2590da6c174)#define WIFI\_MGMT\_SCAN\_SSID\_FILT\_MAX 1

42#endif /\* CONFIG\_WIFI\_MGMT\_SCAN\_SSID\_FILT\_MAX \*/

43

44#ifdef CONFIG\_WIFI\_MGMT\_SCAN\_CHAN\_MAX\_MANUAL

45#define WIFI\_MGMT\_SCAN\_CHAN\_MAX\_MANUAL CONFIG\_WIFI\_MGMT\_SCAN\_CHAN\_MAX\_MANUAL

46#else

[ 47](group__wifi__mgmt.md#ga4ed2294d0250a2e03e2e579cf0635e2c)#define WIFI\_MGMT\_SCAN\_CHAN\_MAX\_MANUAL 1

48#endif /\* CONFIG\_WIFI\_MGMT\_SCAN\_CHAN\_MAX\_MANUAL \*/

49

[ 50](group__wifi__mgmt.md#gab39fdca1c3e875b2402c0057ee7e34be)#define WIFI\_MGMT\_BAND\_STR\_SIZE\_MAX 8

51

[ 53](group__wifi__mgmt.md#ga99a55137188119f65f9d2bb4f57cac77)enum [net\_request\_wifi\_cmd](group__wifi__mgmt.md#ga99a55137188119f65f9d2bb4f57cac77) {

[ 55](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a4aadf9114010c09bd7420c99a2049d5a) [NET\_REQUEST\_WIFI\_CMD\_SCAN](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a4aadf9114010c09bd7420c99a2049d5a) = 1,

[ 57](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a78c958877ee60c90803c925b6b2f057a) [NET\_REQUEST\_WIFI\_CMD\_CONNECT](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a78c958877ee60c90803c925b6b2f057a),

[ 59](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77ac33941da138b993f7a1158d91469bcb7) [NET\_REQUEST\_WIFI\_CMD\_DISCONNECT](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77ac33941da138b993f7a1158d91469bcb7),

[ 61](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a28267d33b555433271cb121d62194a4c) [NET\_REQUEST\_WIFI\_CMD\_AP\_ENABLE](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a28267d33b555433271cb121d62194a4c),

[ 63](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a6fe9d7137b4cd20de880955b27382ccf) [NET\_REQUEST\_WIFI\_CMD\_AP\_DISABLE](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a6fe9d7137b4cd20de880955b27382ccf),

[ 65](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a6af9d52df8f9db6393044e42e10ff0de) [NET\_REQUEST\_WIFI\_CMD\_IFACE\_STATUS](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a6af9d52df8f9db6393044e42e10ff0de),

[ 67](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77abf9fb93c205fa36f74a9ef19d3d0351a) [NET\_REQUEST\_WIFI\_CMD\_PS](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77abf9fb93c205fa36f74a9ef19d3d0351a),

[ 69](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a7bbc7ba59a57a539360d5f148c4d85f9) [NET\_REQUEST\_WIFI\_CMD\_PS\_MODE](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a7bbc7ba59a57a539360d5f148c4d85f9),

[ 71](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a1c9dc2d698326d987ffe5bfd35a9ed09) [NET\_REQUEST\_WIFI\_CMD\_TWT](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a1c9dc2d698326d987ffe5bfd35a9ed09),

[ 73](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77ae6ce1c605d1bf7c09650ec15d74e77e9) [NET\_REQUEST\_WIFI\_CMD\_PS\_CONFIG](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77ae6ce1c605d1bf7c09650ec15d74e77e9),

[ 75](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a367cc44caefd313e0c7ad3badc081456) [NET\_REQUEST\_WIFI\_CMD\_REG\_DOMAIN](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a367cc44caefd313e0c7ad3badc081456),

[ 77](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77af934bbb1b130b0ec6d2f993b4589d2ad) [NET\_REQUEST\_WIFI\_CMD\_PS\_TIMEOUT](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77af934bbb1b130b0ec6d2f993b4589d2ad),

[ 79](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77ab7183584bdf5fe673d39fa0d090e3899) [NET\_REQUEST\_WIFI\_CMD\_MODE](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77ab7183584bdf5fe673d39fa0d090e3899),

[ 81](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a2579ace546bf6954c111eb5951e894f5) [NET\_REQUEST\_WIFI\_CMD\_PACKET\_FILTER](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a2579ace546bf6954c111eb5951e894f5),

[ 83](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77aade3d7a43c730a52f7876c6486170bb2) [NET\_REQUEST\_WIFI\_CMD\_CHANNEL](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77aade3d7a43c730a52f7876c6486170bb2),

[ 85](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a6f3865aa6a4d7633e241ee2b002c1b5a) [NET\_REQUEST\_WIFI\_CMD\_AP\_STA\_DISCONNECT](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a6f3865aa6a4d7633e241ee2b002c1b5a),

[ 87](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a7d9596f2cce54c9e050d89469e86eccb) [NET\_REQUEST\_WIFI\_CMD\_VERSION](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a7d9596f2cce54c9e050d89469e86eccb),

[ 88](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77af68077193672e52cc0e3361bacee77c9) [NET\_REQUEST\_WIFI\_CMD\_MAX](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77af68077193672e52cc0e3361bacee77c9)

89};

90

[ 91](group__wifi__mgmt.md#ga1c277da90986fa52dca182c4d922646f)#define NET\_REQUEST\_WIFI\_SCAN \

92 (\_NET\_WIFI\_BASE | NET\_REQUEST\_WIFI\_CMD\_SCAN)

93

94[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)([NET\_REQUEST\_WIFI\_SCAN](group__wifi__mgmt.md#ga1c277da90986fa52dca182c4d922646f));

95

[ 96](group__wifi__mgmt.md#gaa7ab2a97950a22736bb69f60b459f0f6)#define NET\_REQUEST\_WIFI\_CONNECT \

97 (\_NET\_WIFI\_BASE | NET\_REQUEST\_WIFI\_CMD\_CONNECT)

98

99[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)([NET\_REQUEST\_WIFI\_CONNECT](group__wifi__mgmt.md#gaa7ab2a97950a22736bb69f60b459f0f6));

100

[ 101](group__wifi__mgmt.md#ga90afd8d4e83056463ec6e667ed8ea60a)#define NET\_REQUEST\_WIFI\_DISCONNECT \

102 (\_NET\_WIFI\_BASE | NET\_REQUEST\_WIFI\_CMD\_DISCONNECT)

103

104[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)([NET\_REQUEST\_WIFI\_DISCONNECT](group__wifi__mgmt.md#ga90afd8d4e83056463ec6e667ed8ea60a));

105

[ 106](group__wifi__mgmt.md#ga638d2eb0a5029c1af46a91b523ed8589)#define NET\_REQUEST\_WIFI\_AP\_ENABLE \

107 (\_NET\_WIFI\_BASE | NET\_REQUEST\_WIFI\_CMD\_AP\_ENABLE)

108

109[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)([NET\_REQUEST\_WIFI\_AP\_ENABLE](group__wifi__mgmt.md#ga638d2eb0a5029c1af46a91b523ed8589));

110

[ 111](group__wifi__mgmt.md#gaf81f62bf4c9e331a095acbf0d24ca1a2)#define NET\_REQUEST\_WIFI\_AP\_DISABLE \

112 (\_NET\_WIFI\_BASE | NET\_REQUEST\_WIFI\_CMD\_AP\_DISABLE)

113

114[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)([NET\_REQUEST\_WIFI\_AP\_DISABLE](group__wifi__mgmt.md#gaf81f62bf4c9e331a095acbf0d24ca1a2));

115

[ 116](group__wifi__mgmt.md#ga3e45f6ee3801553619d8eb7d0af506eb)#define NET\_REQUEST\_WIFI\_IFACE\_STATUS \

117 (\_NET\_WIFI\_BASE | NET\_REQUEST\_WIFI\_CMD\_IFACE\_STATUS)

118

119[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)([NET\_REQUEST\_WIFI\_IFACE\_STATUS](group__wifi__mgmt.md#ga3e45f6ee3801553619d8eb7d0af506eb));

120

[ 121](group__wifi__mgmt.md#ga68aaced888f98e1ba4e6b61b53e5e2ba)#define NET\_REQUEST\_WIFI\_PS \

122 (\_NET\_WIFI\_BASE | NET\_REQUEST\_WIFI\_CMD\_PS)

123

124[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)([NET\_REQUEST\_WIFI\_PS](group__wifi__mgmt.md#ga68aaced888f98e1ba4e6b61b53e5e2ba));

125

[ 126](group__wifi__mgmt.md#ga437b00fd5e46846abe666f4a3986d847)#define NET\_REQUEST\_WIFI\_PS\_MODE \

127 (\_NET\_WIFI\_BASE | NET\_REQUEST\_WIFI\_CMD\_PS\_MODE)

128

129[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)([NET\_REQUEST\_WIFI\_PS\_MODE](group__wifi__mgmt.md#ga437b00fd5e46846abe666f4a3986d847));

130

[ 131](group__wifi__mgmt.md#gab84fd7e9ca0bf0b2b9d08889dda26aad)#define NET\_REQUEST\_WIFI\_TWT \

132 (\_NET\_WIFI\_BASE | NET\_REQUEST\_WIFI\_CMD\_TWT)

133

134[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)([NET\_REQUEST\_WIFI\_TWT](group__wifi__mgmt.md#gab84fd7e9ca0bf0b2b9d08889dda26aad));

135

[ 136](group__wifi__mgmt.md#ga1032f3773cfe6130da4d4d498b044ee2)#define NET\_REQUEST\_WIFI\_PS\_CONFIG \

137 (\_NET\_WIFI\_BASE | NET\_REQUEST\_WIFI\_CMD\_PS\_CONFIG)

138

139[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)([NET\_REQUEST\_WIFI\_PS\_CONFIG](group__wifi__mgmt.md#ga1032f3773cfe6130da4d4d498b044ee2));

[ 140](group__wifi__mgmt.md#ga2b27d102b779a6d846b375854768fb7f)#define NET\_REQUEST\_WIFI\_REG\_DOMAIN \

141 (\_NET\_WIFI\_BASE | NET\_REQUEST\_WIFI\_CMD\_REG\_DOMAIN)

142

143[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)([NET\_REQUEST\_WIFI\_REG\_DOMAIN](group__wifi__mgmt.md#ga2b27d102b779a6d846b375854768fb7f));

144

[ 145](group__wifi__mgmt.md#ga61d035b3f80ee8b7b6fefea9fa7a6d84)#define NET\_REQUEST\_WIFI\_PS\_TIMEOUT \

146 (\_NET\_WIFI\_BASE | NET\_REQUEST\_WIFI\_CMD\_PS\_TIMEOUT)

147

148[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)([NET\_REQUEST\_WIFI\_PS\_TIMEOUT](group__wifi__mgmt.md#ga61d035b3f80ee8b7b6fefea9fa7a6d84));

149

[ 150](group__wifi__mgmt.md#ga9b4da60a8108b0cc431ac1eecfca0cd0)#define NET\_REQUEST\_WIFI\_MODE \

151 (\_NET\_WIFI\_BASE | NET\_REQUEST\_WIFI\_CMD\_MODE)

152

153[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)([NET\_REQUEST\_WIFI\_MODE](group__wifi__mgmt.md#ga9b4da60a8108b0cc431ac1eecfca0cd0));

154

[ 155](group__wifi__mgmt.md#ga3098e817d12bf4619c9fd2698508fb4e)#define NET\_REQUEST\_WIFI\_PACKET\_FILTER \

156 (\_NET\_WIFI\_BASE | NET\_REQUEST\_WIFI\_CMD\_PACKET\_FILTER)

157

158[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)([NET\_REQUEST\_WIFI\_PACKET\_FILTER](group__wifi__mgmt.md#ga3098e817d12bf4619c9fd2698508fb4e));

159

[ 160](group__wifi__mgmt.md#gad9614d2368f8399850aaec05e40bdc78)#define NET\_REQUEST\_WIFI\_CHANNEL \

161 (\_NET\_WIFI\_BASE | NET\_REQUEST\_WIFI\_CMD\_CHANNEL)

162

163[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)([NET\_REQUEST\_WIFI\_CHANNEL](group__wifi__mgmt.md#gad9614d2368f8399850aaec05e40bdc78));

164

[ 165](group__wifi__mgmt.md#gaa3e52e08d89a1104f07207e52b81d503)#define NET\_REQUEST\_WIFI\_AP\_STA\_DISCONNECT \

166 (\_NET\_WIFI\_BASE | NET\_REQUEST\_WIFI\_CMD\_AP\_STA\_DISCONNECT)

167

168[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)([NET\_REQUEST\_WIFI\_AP\_STA\_DISCONNECT](group__wifi__mgmt.md#gaa3e52e08d89a1104f07207e52b81d503));

169

[ 170](group__wifi__mgmt.md#ga3e60c29ca9ce95d17a7fff087290f7f1)#define NET\_REQUEST\_WIFI\_VERSION \

171 (\_NET\_WIFI\_BASE | NET\_REQUEST\_WIFI\_CMD\_VERSION)

172

173[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)([NET\_REQUEST\_WIFI\_VERSION](group__wifi__mgmt.md#ga3e60c29ca9ce95d17a7fff087290f7f1));

174

[ 176](group__wifi__mgmt.md#gac2638308cbb0d268831f1618cf8e1fa8)enum [net\_event\_wifi\_cmd](group__wifi__mgmt.md#gac2638308cbb0d268831f1618cf8e1fa8) {

[ 178](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8a37e9ab2a6832153fa968337d920e587e) [NET\_EVENT\_WIFI\_CMD\_SCAN\_RESULT](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8a37e9ab2a6832153fa968337d920e587e) = 1,

[ 180](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8ad753b7e4588257815f4a60a539ca2018) [NET\_EVENT\_WIFI\_CMD\_SCAN\_DONE](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8ad753b7e4588257815f4a60a539ca2018),

[ 182](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8af76f28777b91b365dc3f97028bc18e3c) [NET\_EVENT\_WIFI\_CMD\_CONNECT\_RESULT](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8af76f28777b91b365dc3f97028bc18e3c),

[ 184](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8a3a3b0387f83d8fb24a0e27312468b0eb) [NET\_EVENT\_WIFI\_CMD\_DISCONNECT\_RESULT](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8a3a3b0387f83d8fb24a0e27312468b0eb),

[ 186](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8af4b3f1969b96f63253851c26c3882a14) [NET\_EVENT\_WIFI\_CMD\_IFACE\_STATUS](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8af4b3f1969b96f63253851c26c3882a14),

[ 188](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8adad71603ed829ed92d06f8c40efa9b18) [NET\_EVENT\_WIFI\_CMD\_TWT](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8adad71603ed829ed92d06f8c40efa9b18),

[ 192](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8a78838bf7ce80cee5e803712cd0286750) [NET\_EVENT\_WIFI\_CMD\_TWT\_SLEEP\_STATE](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8a78838bf7ce80cee5e803712cd0286750),

[ 194](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8addf15c69512be7ab4957e7c0b3fde0ac) [NET\_EVENT\_WIFI\_CMD\_RAW\_SCAN\_RESULT](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8addf15c69512be7ab4957e7c0b3fde0ac),

[ 196](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8af1c42bd59f01260c64ede07da436c18f) [NET\_EVENT\_WIFI\_CMD\_DISCONNECT\_COMPLETE](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8af1c42bd59f01260c64ede07da436c18f),

[ 198](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8abd1797564427886eeb14dd293ae86a9b) [NET\_EVENT\_WIFI\_CMD\_AP\_ENABLE\_RESULT](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8abd1797564427886eeb14dd293ae86a9b),

[ 200](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8aeec3d7a9191280c2326034a17555308d) [NET\_EVENT\_WIFI\_CMD\_AP\_DISABLE\_RESULT](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8aeec3d7a9191280c2326034a17555308d),

[ 202](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8abd4269b2cd1302ce61da4f8d7bb9d5fb) [NET\_EVENT\_WIFI\_CMD\_AP\_STA\_CONNECTED](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8abd4269b2cd1302ce61da4f8d7bb9d5fb),

[ 204](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8a3678a39f9542968958b5575d571d4e2e) [NET\_EVENT\_WIFI\_CMD\_AP\_STA\_DISCONNECTED](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8a3678a39f9542968958b5575d571d4e2e),

205};

206

[ 207](group__wifi__mgmt.md#ga436a927d47eb9abe683b89f2b128cd6e)#define NET\_EVENT\_WIFI\_SCAN\_RESULT \

208 (\_NET\_WIFI\_EVENT | NET\_EVENT\_WIFI\_CMD\_SCAN\_RESULT)

209

[ 210](group__wifi__mgmt.md#ga8ce35a12e5338e9a65970382b4a26b88)#define NET\_EVENT\_WIFI\_SCAN\_DONE \

211 (\_NET\_WIFI\_EVENT | NET\_EVENT\_WIFI\_CMD\_SCAN\_DONE)

212

[ 213](group__wifi__mgmt.md#ga0e8feafcc5efd85d04be91f407c0b7c4)#define NET\_EVENT\_WIFI\_CONNECT\_RESULT \

214 (\_NET\_WIFI\_EVENT | NET\_EVENT\_WIFI\_CMD\_CONNECT\_RESULT)

215

[ 216](group__wifi__mgmt.md#ga8cbbe69bd60f42fdbb06f4f1e15410c8)#define NET\_EVENT\_WIFI\_DISCONNECT\_RESULT \

217 (\_NET\_WIFI\_EVENT | NET\_EVENT\_WIFI\_CMD\_DISCONNECT\_RESULT)

218

[ 219](group__wifi__mgmt.md#ga99e11fc15582b94d4243de7733e47ebb)#define NET\_EVENT\_WIFI\_IFACE\_STATUS \

220 (\_NET\_WIFI\_EVENT | NET\_EVENT\_WIFI\_CMD\_IFACE\_STATUS)

221

[ 222](group__wifi__mgmt.md#gaeb968a5d2a8d68a8c634cca18dbcf9c6)#define NET\_EVENT\_WIFI\_TWT \

223 (\_NET\_WIFI\_EVENT | NET\_EVENT\_WIFI\_CMD\_TWT)

224

[ 225](group__wifi__mgmt.md#ga682d95b5d06a9b175c10d712acca8a49)#define NET\_EVENT\_WIFI\_TWT\_SLEEP\_STATE \

226 (\_NET\_WIFI\_EVENT | NET\_EVENT\_WIFI\_CMD\_TWT\_SLEEP\_STATE)

227

[ 228](group__wifi__mgmt.md#gaea8d222282ddef6992330763afc759a4)#define NET\_EVENT\_WIFI\_RAW\_SCAN\_RESULT \

229 (\_NET\_WIFI\_EVENT | NET\_EVENT\_WIFI\_CMD\_RAW\_SCAN\_RESULT)

230

[ 231](group__wifi__mgmt.md#ga40027feb7ec42c846fd99b56bbd2256d)#define NET\_EVENT\_WIFI\_DISCONNECT\_COMPLETE \

232 (\_NET\_WIFI\_EVENT | NET\_EVENT\_WIFI\_CMD\_DISCONNECT\_COMPLETE)

233

[ 234](group__wifi__mgmt.md#ga1d678fbae0f092814392c0ab4087cb73)#define NET\_EVENT\_WIFI\_AP\_ENABLE\_RESULT \

235 (\_NET\_WIFI\_EVENT | NET\_EVENT\_WIFI\_CMD\_AP\_ENABLE\_RESULT)

236

[ 237](group__wifi__mgmt.md#ga104296fdb38edf868bea1a46f572d101)#define NET\_EVENT\_WIFI\_AP\_DISABLE\_RESULT \

238 (\_NET\_WIFI\_EVENT | NET\_EVENT\_WIFI\_CMD\_AP\_DISABLE\_RESULT)

239

[ 240](group__wifi__mgmt.md#gacc392179948bfd5bed6702dc8fb5cd9d)#define NET\_EVENT\_WIFI\_AP\_STA\_CONNECTED \

241 (\_NET\_WIFI\_EVENT | NET\_EVENT\_WIFI\_CMD\_AP\_STA\_CONNECTED)

242

[ 243](group__wifi__mgmt.md#ga3e8154ce1808665dd165f793ddec1673)#define NET\_EVENT\_WIFI\_AP\_STA\_DISCONNECTED \

244 (\_NET\_WIFI\_EVENT | NET\_EVENT\_WIFI\_CMD\_AP\_STA\_DISCONNECTED)

245

[ 247](structwifi__version.md)struct [wifi\_version](structwifi__version.md) {

[ 249](structwifi__version.md#aea828bdb512440d6aa3cc853525c4971) const char \*[drv\_version](structwifi__version.md#aea828bdb512440d6aa3cc853525c4971);

[ 251](structwifi__version.md#a4bf2cbdf5c43ff21718ccf19646c164e) const char \*[fw\_version](structwifi__version.md#a4bf2cbdf5c43ff21718ccf19646c164e);

252};

253

[ 257](structwifi__band__channel.md)struct [wifi\_band\_channel](structwifi__band__channel.md) {

[ 259](structwifi__band__channel.md#a4a932599429f37231f76c3064ec5efb3) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [band](structwifi__band__channel.md#a4a932599429f37231f76c3064ec5efb3);

[ 261](structwifi__band__channel.md#acd0dd7366de3650124dad7232a58ade0) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [channel](structwifi__band__channel.md#acd0dd7366de3650124dad7232a58ade0);

262};

263

[ 269](structwifi__scan__params.md)struct [wifi\_scan\_params](structwifi__scan__params.md) {

[ 277](structwifi__scan__params.md#a645acc54603cd4692527c1a028933078) enum [wifi\_scan\_type](group__wifi__mgmt.md#gad30e29eda65ccafdbd7f11865937b8ea) [scan\_type](structwifi__scan__params.md#a645acc54603cd4692527c1a028933078);

[ 281](structwifi__scan__params.md#a6b571d960ed9d7419e31530e5fb6f97a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bands](structwifi__scan__params.md#a6b571d960ed9d7419e31530e5fb6f97a);

[ 284](structwifi__scan__params.md#a2453a75c23e04e3572559c0e7199c1b4) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [dwell\_time\_active](structwifi__scan__params.md#a2453a75c23e04e3572559c0e7199c1b4);

[ 287](structwifi__scan__params.md#a8e7a37ccda8de635e7b7066d7943e814) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [dwell\_time\_passive](structwifi__scan__params.md#a8e7a37ccda8de635e7b7066d7943e814);

[ 290](structwifi__scan__params.md#abc1470c64b409db4785264e362b8c196) const char \*[ssids](structwifi__scan__params.md#abc1470c64b409db4785264e362b8c196)[[WIFI\_MGMT\_SCAN\_SSID\_FILT\_MAX](group__wifi__mgmt.md#ga8f1d15bfcd0776eee7cae2590da6c174)];

[ 298](structwifi__scan__params.md#a12d5dea7d8fa8ad03ac2366720c46243) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [max\_bss\_cnt](structwifi__scan__params.md#a12d5dea7d8fa8ad03ac2366720c46243);

[ 313](structwifi__scan__params.md#ac816cd67cc3141ebca5cd3acd052a003) struct [wifi\_band\_channel](structwifi__band__channel.md) [band\_chan](structwifi__scan__params.md#ac816cd67cc3141ebca5cd3acd052a003)[[WIFI\_MGMT\_SCAN\_CHAN\_MAX\_MANUAL](group__wifi__mgmt.md#ga4ed2294d0250a2e03e2e579cf0635e2c)];

314};

315

[ 319](structwifi__scan__result.md)struct [wifi\_scan\_result](structwifi__scan__result.md) {

[ 321](structwifi__scan__result.md#a854e296bdb2a54cb31e90a8f856be079) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [ssid](structwifi__scan__result.md#a854e296bdb2a54cb31e90a8f856be079)[[WIFI\_SSID\_MAX\_LEN](group__wifi__mgmt.md#gad62c60666c9fdffe2e0e9c4388f87886)];

[ 323](structwifi__scan__result.md#a2c1c2f4265b914df08fc75deb8b69d39) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [ssid\_length](structwifi__scan__result.md#a2c1c2f4265b914df08fc75deb8b69d39);

[ 325](structwifi__scan__result.md#a38201c9dd798dc11b5bda3ce97b02e92) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [band](structwifi__scan__result.md#a38201c9dd798dc11b5bda3ce97b02e92);

[ 327](structwifi__scan__result.md#adbbfd7692ee5ffd6344fe78b9d91c840) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [channel](structwifi__scan__result.md#adbbfd7692ee5ffd6344fe78b9d91c840);

[ 329](structwifi__scan__result.md#af2d3dc5d115e3db76d3bc115510b0a5a) enum [wifi\_security\_type](group__wifi__mgmt.md#gadde31a04fa25ed805115c6b31854cd9c) [security](structwifi__scan__result.md#af2d3dc5d115e3db76d3bc115510b0a5a);

[ 331](structwifi__scan__result.md#acaa3fb30ebf6df22bfac6380698ed28e) enum [wifi\_mfp\_options](group__wifi__mgmt.md#ga1f252da47d9650023d7fff6d08e49c76) [mfp](structwifi__scan__result.md#acaa3fb30ebf6df22bfac6380698ed28e);

[ 333](structwifi__scan__result.md#a76aa012136e3721fd4a482a22b93546f) [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) [rssi](structwifi__scan__result.md#a76aa012136e3721fd4a482a22b93546f);

[ 335](structwifi__scan__result.md#a906e9b48ebd5c0a599221f32cc47cda6) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [mac](structwifi__scan__result.md#a906e9b48ebd5c0a599221f32cc47cda6)[[WIFI\_MAC\_ADDR\_LEN](group__wifi__mgmt.md#ga29409ff83a53c6464decdde9bdd04de6)];

[ 337](structwifi__scan__result.md#a8fca0dabec00ebd7ed4800098ec9d451) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [mac\_length](structwifi__scan__result.md#a8fca0dabec00ebd7ed4800098ec9d451);

338};

339

[ 341](structwifi__connect__req__params.md)struct [wifi\_connect\_req\_params](structwifi__connect__req__params.md) {

[ 343](structwifi__connect__req__params.md#ac260c2cd17a3f36ea101edaf23d41083) const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[ssid](structwifi__connect__req__params.md#ac260c2cd17a3f36ea101edaf23d41083);

[ 345](structwifi__connect__req__params.md#a547dddf6be5dd77eda74b1085a798400) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [ssid\_length](structwifi__connect__req__params.md#a547dddf6be5dd77eda74b1085a798400); /\* Max 32 \*/

[ 347](structwifi__connect__req__params.md#aa7743f0ecbc27a9595720ce13ce57c1d) const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[psk](structwifi__connect__req__params.md#aa7743f0ecbc27a9595720ce13ce57c1d);

[ 349](structwifi__connect__req__params.md#aaf7455a65590d19f047214b459a2dcb9) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [psk\_length](structwifi__connect__req__params.md#aaf7455a65590d19f047214b459a2dcb9); /\* Min 8 - Max 64 \*/

[ 351](structwifi__connect__req__params.md#a469fac5758b78fc425911837930b2060) const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[sae\_password](structwifi__connect__req__params.md#a469fac5758b78fc425911837930b2060);

[ 353](structwifi__connect__req__params.md#a74f0819e7a546ffb8bfb0ec587eccf20) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [sae\_password\_length](structwifi__connect__req__params.md#a74f0819e7a546ffb8bfb0ec587eccf20); /\* No length restrictions \*/

[ 355](structwifi__connect__req__params.md#aa2fea1881a8ffdf5d7093ae295867f3e) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [band](structwifi__connect__req__params.md#aa2fea1881a8ffdf5d7093ae295867f3e);

[ 357](structwifi__connect__req__params.md#a52b6d0323c35d03ec239f40be35cae72) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [channel](structwifi__connect__req__params.md#a52b6d0323c35d03ec239f40be35cae72);

[ 359](structwifi__connect__req__params.md#a18dce6bb021086877a30e7a04f5b24b9) enum [wifi\_security\_type](group__wifi__mgmt.md#gadde31a04fa25ed805115c6b31854cd9c) [security](structwifi__connect__req__params.md#a18dce6bb021086877a30e7a04f5b24b9);

[ 361](structwifi__connect__req__params.md#a745b3416172672a7e5b12bcc5b55e88c) enum [wifi\_mfp\_options](group__wifi__mgmt.md#ga1f252da47d9650023d7fff6d08e49c76) [mfp](structwifi__connect__req__params.md#a745b3416172672a7e5b12bcc5b55e88c);

[ 363](structwifi__connect__req__params.md#a56183ba7f4d8eaf5fc5b495856adecfd) int [timeout](structwifi__connect__req__params.md#a56183ba7f4d8eaf5fc5b495856adecfd);

364};

365

[ 369](group__wifi__mgmt.md#ga86a5741e54aeb3e290142b0de217b8a8)enum [wifi\_conn\_status](group__wifi__mgmt.md#ga86a5741e54aeb3e290142b0de217b8a8) {

[ 371](group__wifi__mgmt.md#gga86a5741e54aeb3e290142b0de217b8a8a380410b02b1e12599f37d1dcb844f5bd) [WIFI\_STATUS\_CONN\_SUCCESS](group__wifi__mgmt.md#gga86a5741e54aeb3e290142b0de217b8a8a380410b02b1e12599f37d1dcb844f5bd) = 0,

[ 373](group__wifi__mgmt.md#gga86a5741e54aeb3e290142b0de217b8a8ab80ec4b70c75695fbe698034e2cb6a44) [WIFI\_STATUS\_CONN\_FAIL](group__wifi__mgmt.md#gga86a5741e54aeb3e290142b0de217b8a8ab80ec4b70c75695fbe698034e2cb6a44),

[ 375](group__wifi__mgmt.md#gga86a5741e54aeb3e290142b0de217b8a8a90d91f96a35c9f6847cbc7abd8c20bf8) [WIFI\_STATUS\_CONN\_WRONG\_PASSWORD](group__wifi__mgmt.md#gga86a5741e54aeb3e290142b0de217b8a8a90d91f96a35c9f6847cbc7abd8c20bf8),

[ 377](group__wifi__mgmt.md#gga86a5741e54aeb3e290142b0de217b8a8abb8783b92aec2ed1ffc6331979888563) [WIFI\_STATUS\_CONN\_TIMEOUT](group__wifi__mgmt.md#gga86a5741e54aeb3e290142b0de217b8a8abb8783b92aec2ed1ffc6331979888563),

[ 379](group__wifi__mgmt.md#gga86a5741e54aeb3e290142b0de217b8a8a2ae79fa389bb447fa108e0107aeff2f4) [WIFI\_STATUS\_CONN\_AP\_NOT\_FOUND](group__wifi__mgmt.md#gga86a5741e54aeb3e290142b0de217b8a8a2ae79fa389bb447fa108e0107aeff2f4),

380};

381

[ 385](group__wifi__mgmt.md#gac782af0a60b202fd19597cabb7bd3a9a)enum [wifi\_disconn\_reason](group__wifi__mgmt.md#gac782af0a60b202fd19597cabb7bd3a9a) {

[ 387](group__wifi__mgmt.md#ggac782af0a60b202fd19597cabb7bd3a9aa87f5d64a9fd3acf8d67c698199779e5c) [WIFI\_REASON\_DISCONN\_UNSPECIFIED](group__wifi__mgmt.md#ggac782af0a60b202fd19597cabb7bd3a9aa87f5d64a9fd3acf8d67c698199779e5c) = 0,

[ 389](group__wifi__mgmt.md#ggac782af0a60b202fd19597cabb7bd3a9aaee75adafb52bd6ecaa547a76c6ccd0a7) [WIFI\_REASON\_DISCONN\_USER\_REQUEST](group__wifi__mgmt.md#ggac782af0a60b202fd19597cabb7bd3a9aaee75adafb52bd6ecaa547a76c6ccd0a7),

[ 391](group__wifi__mgmt.md#ggac782af0a60b202fd19597cabb7bd3a9aa34e3f78ce43db3daeaf32038e0baf204) [WIFI\_REASON\_DISCONN\_AP\_LEAVING](group__wifi__mgmt.md#ggac782af0a60b202fd19597cabb7bd3a9aa34e3f78ce43db3daeaf32038e0baf204),

[ 393](group__wifi__mgmt.md#ggac782af0a60b202fd19597cabb7bd3a9aa05fe2f87de30de47ee48f7615c2206e6) [WIFI\_REASON\_DISCONN\_INACTIVITY](group__wifi__mgmt.md#ggac782af0a60b202fd19597cabb7bd3a9aa05fe2f87de30de47ee48f7615c2206e6),

394};

395

[ 399](group__wifi__mgmt.md#gaaf730bf76adc06434c7ac63bf0417884)enum [wifi\_ap\_status](group__wifi__mgmt.md#gaaf730bf76adc06434c7ac63bf0417884) {

[ 401](group__wifi__mgmt.md#ggaaf730bf76adc06434c7ac63bf0417884a0df52848da8735892d0eb1e381b2cd7c) [WIFI\_STATUS\_AP\_SUCCESS](group__wifi__mgmt.md#ggaaf730bf76adc06434c7ac63bf0417884a0df52848da8735892d0eb1e381b2cd7c) = 0,

[ 403](group__wifi__mgmt.md#ggaaf730bf76adc06434c7ac63bf0417884a6c6801381caa3862004662169202fa9a) [WIFI\_STATUS\_AP\_FAIL](group__wifi__mgmt.md#ggaaf730bf76adc06434c7ac63bf0417884a6c6801381caa3862004662169202fa9a),

[ 405](group__wifi__mgmt.md#ggaaf730bf76adc06434c7ac63bf0417884a5acb85a2361ca72ed10966b829c5753b) [WIFI\_STATUS\_AP\_CHANNEL\_NOT\_SUPPORTED](group__wifi__mgmt.md#ggaaf730bf76adc06434c7ac63bf0417884a5acb85a2361ca72ed10966b829c5753b),

[ 407](group__wifi__mgmt.md#ggaaf730bf76adc06434c7ac63bf0417884a0b1cb592c54c16e8a54defee71c5fd15) [WIFI\_STATUS\_AP\_CHANNEL\_NOT\_ALLOWED](group__wifi__mgmt.md#ggaaf730bf76adc06434c7ac63bf0417884a0b1cb592c54c16e8a54defee71c5fd15),

[ 409](group__wifi__mgmt.md#ggaaf730bf76adc06434c7ac63bf0417884ac18a7b551f8c6bb7737b0e8e60c323ce) [WIFI\_STATUS\_AP\_SSID\_NOT\_ALLOWED](group__wifi__mgmt.md#ggaaf730bf76adc06434c7ac63bf0417884ac18a7b551f8c6bb7737b0e8e60c323ce),

[ 411](group__wifi__mgmt.md#ggaaf730bf76adc06434c7ac63bf0417884abe5a626d22051522255d98fdfdfbfcc8) [WIFI\_STATUS\_AP\_AUTH\_TYPE\_NOT\_SUPPORTED](group__wifi__mgmt.md#ggaaf730bf76adc06434c7ac63bf0417884abe5a626d22051522255d98fdfdfbfcc8),

[ 413](group__wifi__mgmt.md#ggaaf730bf76adc06434c7ac63bf0417884a2105e6c49b3bcb5f7dcacbc1e5ce9cca) [WIFI\_STATUS\_AP\_OP\_NOT\_SUPPORTED](group__wifi__mgmt.md#ggaaf730bf76adc06434c7ac63bf0417884a2105e6c49b3bcb5f7dcacbc1e5ce9cca),

[ 415](group__wifi__mgmt.md#ggaaf730bf76adc06434c7ac63bf0417884a36a58980bdc7877c910441590137ddbe) [WIFI\_STATUS\_AP\_OP\_NOT\_PERMITTED](group__wifi__mgmt.md#ggaaf730bf76adc06434c7ac63bf0417884a36a58980bdc7877c910441590137ddbe),

416};

417

[ 419](structwifi__status.md)struct [wifi\_status](structwifi__status.md) {

420 union {

[ 421](structwifi__status.md#aa1dbff8154400f8353693d387977008b) int [status](structwifi__status.md#aa1dbff8154400f8353693d387977008b);

[ 422](structwifi__status.md#a8f885e78366d0499e4ba8e15bef275ac) enum [wifi\_conn\_status](group__wifi__mgmt.md#ga86a5741e54aeb3e290142b0de217b8a8) [conn\_status](structwifi__status.md#a8f885e78366d0499e4ba8e15bef275ac);

[ 423](structwifi__status.md#aa04b5033d93274badd27f702af9830bc) enum [wifi\_disconn\_reason](group__wifi__mgmt.md#gac782af0a60b202fd19597cabb7bd3a9a) [disconn\_reason](structwifi__status.md#aa04b5033d93274badd27f702af9830bc);

[ 424](structwifi__status.md#a02f0fcc7ef57661ca95d0c99f045aef1) enum [wifi\_ap\_status](group__wifi__mgmt.md#gaaf730bf76adc06434c7ac63bf0417884) [ap\_status](structwifi__status.md#a02f0fcc7ef57661ca95d0c99f045aef1);

425 };

426};

427

[ 429](structwifi__iface__status.md)struct [wifi\_iface\_status](structwifi__iface__status.md) {

[ 431](structwifi__iface__status.md#ac52806155be3d64954ac6d109e76ec57) int [state](structwifi__iface__status.md#ac52806155be3d64954ac6d109e76ec57);

[ 433](structwifi__iface__status.md#ad82f281941e4f6ce1ef0bca008e26d41) unsigned int [ssid\_len](structwifi__iface__status.md#ad82f281941e4f6ce1ef0bca008e26d41);

[ 435](structwifi__iface__status.md#a30c4bef4e061346ba61857a558640d00) char [ssid](structwifi__iface__status.md#a30c4bef4e061346ba61857a558640d00)[[WIFI\_SSID\_MAX\_LEN](group__wifi__mgmt.md#gad62c60666c9fdffe2e0e9c4388f87886)];

[ 437](structwifi__iface__status.md#a28afad15fc6689669c7b19337a64eaf3) char [bssid](structwifi__iface__status.md#a28afad15fc6689669c7b19337a64eaf3)[[WIFI\_MAC\_ADDR\_LEN](group__wifi__mgmt.md#ga29409ff83a53c6464decdde9bdd04de6)];

[ 439](structwifi__iface__status.md#ae1c141a18f4e225af2c22a8cb4f882a8) enum [wifi\_frequency\_bands](group__wifi__mgmt.md#ga1e2f0439a322355fa7368ea880c9c15d) [band](structwifi__iface__status.md#ae1c141a18f4e225af2c22a8cb4f882a8);

[ 441](structwifi__iface__status.md#a6432663156e5b2c424d254ed1eae0144) unsigned int [channel](structwifi__iface__status.md#a6432663156e5b2c424d254ed1eae0144);

[ 443](structwifi__iface__status.md#ad33d2ec149a8d556e2472dd842ceadc0) enum [wifi\_iface\_mode](group__wifi__mgmt.md#ga584f6239ac14e2bedc5e6bd72756423b) [iface\_mode](structwifi__iface__status.md#ad33d2ec149a8d556e2472dd842ceadc0);

[ 445](structwifi__iface__status.md#ae2de076d79f2172793d65fe9cd31edc4) enum [wifi\_link\_mode](group__wifi__mgmt.md#gabdb2a784d4727b71ab44cca04e422c62) [link\_mode](structwifi__iface__status.md#ae2de076d79f2172793d65fe9cd31edc4);

[ 447](structwifi__iface__status.md#a625ecec1abec8dd65cf155eab21a01b5) enum [wifi\_security\_type](group__wifi__mgmt.md#gadde31a04fa25ed805115c6b31854cd9c) [security](structwifi__iface__status.md#a625ecec1abec8dd65cf155eab21a01b5);

[ 449](structwifi__iface__status.md#aa1a9b644fd355526125ddd32416b7c24) enum [wifi\_mfp\_options](group__wifi__mgmt.md#ga1f252da47d9650023d7fff6d08e49c76) [mfp](structwifi__iface__status.md#aa1a9b644fd355526125ddd32416b7c24);

[ 451](structwifi__iface__status.md#a4e593147b88eb4938d55a4de72fcc7f6) int [rssi](structwifi__iface__status.md#a4e593147b88eb4938d55a4de72fcc7f6);

[ 453](structwifi__iface__status.md#aae6c8cbaa16c81d308f08114d5103a3d) unsigned char [dtim\_period](structwifi__iface__status.md#aae6c8cbaa16c81d308f08114d5103a3d);

[ 455](structwifi__iface__status.md#a241bfbe70628006b515b5f9e4f97665c) unsigned short [beacon\_interval](structwifi__iface__status.md#a241bfbe70628006b515b5f9e4f97665c);

[ 457](structwifi__iface__status.md#acfde8d64b463a9f553aa4fb689dc1917) bool [twt\_capable](structwifi__iface__status.md#acfde8d64b463a9f553aa4fb689dc1917);

458};

459

[ 461](structwifi__ps__params.md)struct [wifi\_ps\_params](structwifi__ps__params.md) {

462 /\* Power save state \*/

[ 463](structwifi__ps__params.md#abb22aaa45833ac130922204bd2fe841b) enum [wifi\_ps](group__wifi__mgmt.md#ga0fffeb57b68fb8cdef9d3d571368b8ca) [enabled](structwifi__ps__params.md#abb22aaa45833ac130922204bd2fe841b);

464 /\* Listen interval \*/

[ 465](structwifi__ps__params.md#a8510c799ab0c5825f1c6349f9799c62f) unsigned short [listen\_interval](structwifi__ps__params.md#a8510c799ab0c5825f1c6349f9799c62f);

[ 467](structwifi__ps__params.md#a7cb3e7fb7d9f8bd7c2cab41f879b3b66) enum [wifi\_ps\_wakeup\_mode](group__wifi__mgmt.md#gac7f907644847e905d67c709fa4afae7f) [wakeup\_mode](structwifi__ps__params.md#a7cb3e7fb7d9f8bd7c2cab41f879b3b66);

[ 469](structwifi__ps__params.md#a5a022d89d43ecf2cd1f15fc72c0f2bed) enum [wifi\_ps\_mode](group__wifi__mgmt.md#gaffae7d2a754be5eb952ad2b83edad54c) [mode](structwifi__ps__params.md#a5a022d89d43ecf2cd1f15fc72c0f2bed);

[ 478](structwifi__ps__params.md#ad963f1bf78dc271f08b73f3aadb36a91) unsigned int [timeout\_ms](structwifi__ps__params.md#ad963f1bf78dc271f08b73f3aadb36a91);

[ 480](structwifi__ps__params.md#aef62e5bf6216bf4dc461efe71735c4bd) enum [wifi\_ps\_param\_type](group__wifi__mgmt.md#gabe45d132797047c098041331c8f6f912) [type](structwifi__ps__params.md#aef62e5bf6216bf4dc461efe71735c4bd);

[ 482](structwifi__ps__params.md#a63fa2ee03bc4aefada61c298ee14336c) enum [wifi\_config\_ps\_param\_fail\_reason](group__wifi__mgmt.md#gad98099584d2222ede93aba42b1fbaff0) [fail\_reason](structwifi__ps__params.md#a63fa2ee03bc4aefada61c298ee14336c);

483};

484

[ 486](structwifi__twt__params.md)struct [wifi\_twt\_params](structwifi__twt__params.md) {

[ 488](structwifi__twt__params.md#a6f0483861a387651c9c89ba182e064bd) enum [wifi\_twt\_operation](group__wifi__mgmt.md#gad0e998aeb1b27c4f203ca76339d323a3) [operation](structwifi__twt__params.md#a6f0483861a387651c9c89ba182e064bd);

[ 490](structwifi__twt__params.md#a5fd269328f68838b8a7e3a0b93eed894) enum [wifi\_twt\_negotiation\_type](group__wifi__mgmt.md#ga695123cd534e2499f516a07fdc5cafa8) [negotiation\_type](structwifi__twt__params.md#a5fd269328f68838b8a7e3a0b93eed894);

[ 492](structwifi__twt__params.md#a347f8cff73ee6b6ba6d15ddf6f376a2d) enum [wifi\_twt\_setup\_cmd](group__wifi__mgmt.md#ga31c78afc89bfdc4b54cee177843f8022) [setup\_cmd](structwifi__twt__params.md#a347f8cff73ee6b6ba6d15ddf6f376a2d);

[ 494](structwifi__twt__params.md#a805a23284ed4afa46b84efcd43329beb) enum [wifi\_twt\_setup\_resp\_status](group__wifi__mgmt.md#ga4d03aedac13ee4512d7717ac624f319a) [resp\_status](structwifi__twt__params.md#a805a23284ed4afa46b84efcd43329beb);

[ 496](structwifi__twt__params.md#a9faff59e577775b3fe53f2139462ac71) enum [wifi\_twt\_teardown\_status](group__wifi__mgmt.md#gad3709d07aaa3ed59b48f9dd7bd181989) [teardown\_status](structwifi__twt__params.md#a9faff59e577775b3fe53f2139462ac71);

[ 498](structwifi__twt__params.md#adda47e302a87a766f18e28016963a561) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [dialog\_token](structwifi__twt__params.md#adda47e302a87a766f18e28016963a561);

[ 500](structwifi__twt__params.md#a95ec4b32d37309efa47256ae1ea865da) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [flow\_id](structwifi__twt__params.md#a95ec4b32d37309efa47256ae1ea865da);

501 union {

503 struct {

[ 505](structwifi__twt__params.md#ab92fe571559fcd5d97cdf7e6b7d86681) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [twt\_interval](structwifi__twt__params.md#ab92fe571559fcd5d97cdf7e6b7d86681);

[ 507](structwifi__twt__params.md#ae547c6fc1c7cbad15bebcfdaa43f59e7) bool [responder](structwifi__twt__params.md#ae547c6fc1c7cbad15bebcfdaa43f59e7);

[ 509](structwifi__twt__params.md#a4e822c04b52fe6a9489e48e26b8f9382) bool [trigger](structwifi__twt__params.md#a4e822c04b52fe6a9489e48e26b8f9382);

[ 511](structwifi__twt__params.md#a8ea1e2501c8b69dc3fa606eb360f8678) bool [implicit](structwifi__twt__params.md#a8ea1e2501c8b69dc3fa606eb360f8678);

[ 513](structwifi__twt__params.md#a02f2d822d530e5376f256503439a54f9) bool [announce](structwifi__twt__params.md#a02f2d822d530e5376f256503439a54f9);

[ 515](structwifi__twt__params.md#a7c297459a17ed2fd232c62cca63e952f) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [twt\_wake\_interval](structwifi__twt__params.md#a7c297459a17ed2fd232c62cca63e952f);

516 /\* Wake ahead notification is sent earlier than

517 \* TWT Service period (SP) start based on this duration.

518 \* This should give applications ample time to

519 \* prepare the data before TWT SP starts.

520 \*/

[ 521](structwifi__twt__params.md#a6f907ca412251fdd7391f29bfa6d7713) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [twt\_wake\_ahead\_duration](structwifi__twt__params.md#a6f907ca412251fdd7391f29bfa6d7713);

[ 522](structwifi__twt__params.md#aee57c0189b210cfcc18e213e35b9479c) } [setup](structwifi__twt__params.md#aee57c0189b210cfcc18e213e35b9479c);

524 struct {

[ 526](structwifi__twt__params.md#a26d6bda00452f77832f69f4465c13efb) bool [teardown\_all](structwifi__twt__params.md#a26d6bda00452f77832f69f4465c13efb);

[ 527](structwifi__twt__params.md#afdeebd8a27107a0e37282aa19e5149d0) } [teardown](structwifi__twt__params.md#afdeebd8a27107a0e37282aa19e5149d0);

528 };

[ 530](structwifi__twt__params.md#a70f58b502bb67ef3b2068ded2160b612) enum [wifi\_twt\_fail\_reason](group__wifi__mgmt.md#ga97fa304f9a1db2294a93cccd4c93bcf6) [fail\_reason](structwifi__twt__params.md#a70f58b502bb67ef3b2068ded2160b612);

531};

532

533/\* Flow ID is only 3 bits \*/

[ 534](group__wifi__mgmt.md#ga620bdb1485ddbe72229adee05e6c353a)#define WIFI\_MAX\_TWT\_FLOWS 8

[ 535](group__wifi__mgmt.md#ga1f9d1e07c7c3baf120557a5825f4cca7)#define WIFI\_MAX\_TWT\_INTERVAL\_US (LONG\_MAX - 1)

536/\* 256 (u8) \* 1TU \*/

[ 537](group__wifi__mgmt.md#gade0610317bd0d720e56cae14f5bfbfe1)#define WIFI\_MAX\_TWT\_WAKE\_INTERVAL\_US 262144

[ 538](group__wifi__mgmt.md#gafe9e54aa66ea9142f9dc7d6316bbc7db)#define WIFI\_MAX\_TWT\_WAKE\_AHEAD\_DURATION\_US (LONG\_MAX - 1)

539

[ 541](structwifi__twt__flow__info.md)struct [wifi\_twt\_flow\_info](structwifi__twt__flow__info.md) {

[ 543](structwifi__twt__flow__info.md#ae15ba49fa54f82cc6a1fb0d4572114b7) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [twt\_interval](structwifi__twt__flow__info.md#ae15ba49fa54f82cc6a1fb0d4572114b7);

[ 545](structwifi__twt__flow__info.md#a123ce10bed8b62b01919a7ea7644a0ba) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [dialog\_token](structwifi__twt__flow__info.md#a123ce10bed8b62b01919a7ea7644a0ba);

[ 547](structwifi__twt__flow__info.md#acb0c618f1cebcb172f342cfe222683be) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [flow\_id](structwifi__twt__flow__info.md#acb0c618f1cebcb172f342cfe222683be);

[ 549](structwifi__twt__flow__info.md#a620ae8ba546e4091d74280cb1553b2cf) enum [wifi\_twt\_negotiation\_type](group__wifi__mgmt.md#ga695123cd534e2499f516a07fdc5cafa8) [negotiation\_type](structwifi__twt__flow__info.md#a620ae8ba546e4091d74280cb1553b2cf);

[ 551](structwifi__twt__flow__info.md#ac82e4de8ffc82f851061f8ba8d217dc1) bool [responder](structwifi__twt__flow__info.md#ac82e4de8ffc82f851061f8ba8d217dc1);

[ 553](structwifi__twt__flow__info.md#a952a67bd092c5dadba387bb13449c6f3) bool [trigger](structwifi__twt__flow__info.md#a952a67bd092c5dadba387bb13449c6f3);

[ 555](structwifi__twt__flow__info.md#afb480be82d1c6f351bd634fd83bfa5c7) bool [implicit](structwifi__twt__flow__info.md#afb480be82d1c6f351bd634fd83bfa5c7);

[ 557](structwifi__twt__flow__info.md#afc81a5111c265fd9bb2aca5f9510bfa8) bool [announce](structwifi__twt__flow__info.md#afc81a5111c265fd9bb2aca5f9510bfa8);

[ 559](structwifi__twt__flow__info.md#aede6cb0cfc999fac8ded49e2981a3762) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [twt\_wake\_interval](structwifi__twt__flow__info.md#aede6cb0cfc999fac8ded49e2981a3762);

560 /\* wake ahead duration \*/

[ 561](structwifi__twt__flow__info.md#a6384d3829d54a58a53eafcb74c64a658) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [twt\_wake\_ahead\_duration](structwifi__twt__flow__info.md#a6384d3829d54a58a53eafcb74c64a658);

562};

563

[ 565](structwifi__ps__config.md)struct [wifi\_ps\_config](structwifi__ps__config.md) {

[ 567](structwifi__ps__config.md#a9e83c10eaaa1d721cbc49b40aedb00df) char [num\_twt\_flows](structwifi__ps__config.md#a9e83c10eaaa1d721cbc49b40aedb00df);

[ 569](structwifi__ps__config.md#adcd3944ba1808eb214b522b72307832a) struct [wifi\_twt\_flow\_info](structwifi__twt__flow__info.md) [twt\_flows](structwifi__ps__config.md#adcd3944ba1808eb214b522b72307832a)[[WIFI\_MAX\_TWT\_FLOWS](group__wifi__mgmt.md#ga620bdb1485ddbe72229adee05e6c353a)];

[ 571](structwifi__ps__config.md#a357aafc2dedda37755b1cb1fc07fe5a6) struct [wifi\_ps\_params](structwifi__ps__params.md) [ps\_params](structwifi__ps__config.md#a357aafc2dedda37755b1cb1fc07fe5a6);

572};

573

[ 575](group__wifi__mgmt.md#gae129d0783276e662575af2314eef86cd)enum [wifi\_mgmt\_op](group__wifi__mgmt.md#gae129d0783276e662575af2314eef86cd) {

[ 577](group__wifi__mgmt.md#ggae129d0783276e662575af2314eef86cda6b8183a773e0cdfa85bc4b41ae70fdcd) [WIFI\_MGMT\_GET](group__wifi__mgmt.md#ggae129d0783276e662575af2314eef86cda6b8183a773e0cdfa85bc4b41ae70fdcd) = 0,

[ 579](group__wifi__mgmt.md#ggae129d0783276e662575af2314eef86cdaa0d5931c8275a8d3288ab668b6dfb5a1) [WIFI\_MGMT\_SET](group__wifi__mgmt.md#ggae129d0783276e662575af2314eef86cdaa0d5931c8275a8d3288ab668b6dfb5a1) = 1,

580};

581

[ 582](group__wifi__mgmt.md#ga3a6bfa37bd7850342279d304df20977d)#define MAX\_REG\_CHAN\_NUM 42

583

[ 585](structwifi__reg__chan__info.md)struct [wifi\_reg\_chan\_info](structwifi__reg__chan__info.md) {

[ 587](structwifi__reg__chan__info.md#a0addffc11ef29f50c01b700835e59930) unsigned short [center\_frequency](structwifi__reg__chan__info.md#a0addffc11ef29f50c01b700835e59930);

[ 589](structwifi__reg__chan__info.md#af9169ab4a41fac4c6f6766fc96799545) unsigned short [max\_power](structwifi__reg__chan__info.md#af9169ab4a41fac4c6f6766fc96799545):8;

[ 591](structwifi__reg__chan__info.md#aa044611e18b7332b8577e29f6a769e3f) unsigned short [supported](structwifi__reg__chan__info.md#aa044611e18b7332b8577e29f6a769e3f):1;

[ 593](structwifi__reg__chan__info.md#acc7a88b004c9a61c8bf9ee1a97f85928) unsigned short [passive\_only](structwifi__reg__chan__info.md#acc7a88b004c9a61c8bf9ee1a97f85928):1;

[ 595](structwifi__reg__chan__info.md#a1ab137c142902d2de7d6be2626d7ac1f) unsigned short [dfs](structwifi__reg__chan__info.md#a1ab137c142902d2de7d6be2626d7ac1f):1;

596} \_\_packed;

597

[ 599](structwifi__reg__domain.md)struct [wifi\_reg\_domain](structwifi__reg__domain.md) {

600 /\* Regulatory domain operation \*/

[ 601](structwifi__reg__domain.md#a3bbfdf1497a87bbb6b6211c7035e1002) enum [wifi\_mgmt\_op](group__wifi__mgmt.md#gae129d0783276e662575af2314eef86cd) [oper](structwifi__reg__domain.md#a3bbfdf1497a87bbb6b6211c7035e1002);

[ 603](structwifi__reg__domain.md#a567c6fcae8032567aea83c18cd211c33) bool [force](structwifi__reg__domain.md#a567c6fcae8032567aea83c18cd211c33);

[ 605](structwifi__reg__domain.md#adfabbe25b049f0dd94c035a82c20a413) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [country\_code](structwifi__reg__domain.md#adfabbe25b049f0dd94c035a82c20a413)[[WIFI\_COUNTRY\_CODE\_LEN](group__wifi__mgmt.md#ga6766ef7bcb001f1fb526a4083b6cd8bc)];

[ 607](structwifi__reg__domain.md#a3278e9f43893f49ab9f9d0d7f24009c1) unsigned int [num\_channels](structwifi__reg__domain.md#a3278e9f43893f49ab9f9d0d7f24009c1);

[ 609](structwifi__reg__domain.md#a4c8c9c11e41123cd7738fdb0d33ae5fb) struct [wifi\_reg\_chan\_info](structwifi__reg__chan__info.md) \*[chan\_info](structwifi__reg__domain.md#a4c8c9c11e41123cd7738fdb0d33ae5fb);

610};

611

[ 613](group__wifi__mgmt.md#ga38c184ea35c02f304cccdf389ca6d552)enum [wifi\_twt\_sleep\_state](group__wifi__mgmt.md#ga38c184ea35c02f304cccdf389ca6d552) {

[ 615](group__wifi__mgmt.md#gga38c184ea35c02f304cccdf389ca6d552a37a7aba20723b6614e39e1c417f3113c) [WIFI\_TWT\_STATE\_SLEEP](group__wifi__mgmt.md#gga38c184ea35c02f304cccdf389ca6d552a37a7aba20723b6614e39e1c417f3113c) = 0,

[ 617](group__wifi__mgmt.md#gga38c184ea35c02f304cccdf389ca6d552a7b7b45f85d9644f897ca00bd7864e1b0) [WIFI\_TWT\_STATE\_AWAKE](group__wifi__mgmt.md#gga38c184ea35c02f304cccdf389ca6d552a7b7b45f85d9644f897ca00bd7864e1b0) = 1,

618};

619

620#if defined(CONFIG\_WIFI\_MGMT\_RAW\_SCAN\_RESULTS) || defined(\_\_DOXYGEN\_\_)

[ 622](structwifi__raw__scan__result.md)struct [wifi\_raw\_scan\_result](structwifi__raw__scan__result.md) {

[ 624](structwifi__raw__scan__result.md#a3f08580c6448a5fa28dd8a594fa7dad6) [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) [rssi](structwifi__raw__scan__result.md#a3f08580c6448a5fa28dd8a594fa7dad6);

[ 626](structwifi__raw__scan__result.md#a876966f469714eb481b42ccc8a63945c) int [frame\_length](structwifi__raw__scan__result.md#a876966f469714eb481b42ccc8a63945c);

[ 628](structwifi__raw__scan__result.md#aa2c7781882c6775616cbc8016b0842f6) unsigned short [frequency](structwifi__raw__scan__result.md#aa2c7781882c6775616cbc8016b0842f6);

[ 630](structwifi__raw__scan__result.md#a5710e89199c147ce898602795f00aba3) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [data](structwifi__raw__scan__result.md#a5710e89199c147ce898602795f00aba3)[CONFIG\_WIFI\_MGMT\_RAW\_SCAN\_RESULT\_LENGTH];

631};

632#endif /\* CONFIG\_WIFI\_MGMT\_RAW\_SCAN\_RESULTS \*/

633

[ 635](structwifi__ap__sta__info.md)struct [wifi\_ap\_sta\_info](structwifi__ap__sta__info.md) {

[ 637](structwifi__ap__sta__info.md#a7d8bd52340d4937a4b5b7d2c00662441) enum [wifi\_link\_mode](group__wifi__mgmt.md#gabdb2a784d4727b71ab44cca04e422c62) [link\_mode](structwifi__ap__sta__info.md#a7d8bd52340d4937a4b5b7d2c00662441);

[ 639](structwifi__ap__sta__info.md#a2a2fc109525e72ee7f18cced3b881107) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [mac](structwifi__ap__sta__info.md#a2a2fc109525e72ee7f18cced3b881107)[[WIFI\_MAC\_ADDR\_LEN](group__wifi__mgmt.md#ga29409ff83a53c6464decdde9bdd04de6)];

[ 641](structwifi__ap__sta__info.md#a7f7c8b144bb3464af5213708591eefda) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [mac\_length](structwifi__ap__sta__info.md#a7f7c8b144bb3464af5213708591eefda);

[ 643](structwifi__ap__sta__info.md#a838c9a4288c9bc7e97afe2334c678f34) bool [twt\_capable](structwifi__ap__sta__info.md#a838c9a4288c9bc7e97afe2334c678f34);

644};

645

646/\* for use in max info size calculations \*/

[ 647](unionwifi__mgmt__events.md)union [wifi\_mgmt\_events](unionwifi__mgmt__events.md) {

[ 648](unionwifi__mgmt__events.md#ac531bb6de4e217a3f7ed6e073444c820) struct [wifi\_scan\_result](structwifi__scan__result.md) [scan\_result](unionwifi__mgmt__events.md#ac531bb6de4e217a3f7ed6e073444c820);

[ 649](unionwifi__mgmt__events.md#ab85f83487dae9d5c59acfd56c34868ed) struct [wifi\_status](structwifi__status.md) [connect\_status](unionwifi__mgmt__events.md#ab85f83487dae9d5c59acfd56c34868ed);

[ 650](unionwifi__mgmt__events.md#a8903faa173a9f3575625a0a68121958e) struct [wifi\_iface\_status](structwifi__iface__status.md) [iface\_status](unionwifi__mgmt__events.md#a8903faa173a9f3575625a0a68121958e);

651#ifdef CONFIG\_WIFI\_MGMT\_RAW\_SCAN\_RESULTS

652 struct [wifi\_raw\_scan\_result](structwifi__raw__scan__result.md) raw\_scan\_result;

653#endif /\* CONFIG\_WIFI\_MGMT\_RAW\_SCAN\_RESULTS \*/

[ 654](unionwifi__mgmt__events.md#ae38354f1e61e8b9286cfc71cb56ca339) struct [wifi\_twt\_params](structwifi__twt__params.md) [twt\_params](unionwifi__mgmt__events.md#ae38354f1e61e8b9286cfc71cb56ca339);

[ 655](unionwifi__mgmt__events.md#a08c4882a4bbefc5fa82198cee2e3b344) struct [wifi\_ap\_sta\_info](structwifi__ap__sta__info.md) [ap\_sta\_info](unionwifi__mgmt__events.md#a08c4882a4bbefc5fa82198cee2e3b344);

656};

657

[ 659](structwifi__mode__info.md)struct [wifi\_mode\_info](structwifi__mode__info.md) {

[ 661](structwifi__mode__info.md#aa29d3b88fc718aa3ac05daf38974707d) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [mode](structwifi__mode__info.md#aa29d3b88fc718aa3ac05daf38974707d);

[ 663](structwifi__mode__info.md#add58dd3b45fd2ddaf684d1b0de81bef9) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [if\_index](structwifi__mode__info.md#add58dd3b45fd2ddaf684d1b0de81bef9);

[ 665](structwifi__mode__info.md#a57c101db8b81ab0ac5dd0a158057a64a) enum [wifi\_mgmt\_op](group__wifi__mgmt.md#gae129d0783276e662575af2314eef86cd) [oper](structwifi__mode__info.md#a57c101db8b81ab0ac5dd0a158057a64a);

666};

667

[ 669](structwifi__filter__info.md)struct [wifi\_filter\_info](structwifi__filter__info.md) {

[ 671](structwifi__filter__info.md#ad9560be814299055cfa11b995a7dcf42) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [filter](structwifi__filter__info.md#ad9560be814299055cfa11b995a7dcf42);

[ 673](structwifi__filter__info.md#af9ea91e31e78afcb7ffe1ff9a04277a3) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [if\_index](structwifi__filter__info.md#af9ea91e31e78afcb7ffe1ff9a04277a3);

[ 675](structwifi__filter__info.md#a1b2d0448fc7f62654e3f5aacfba62f8f) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [buffer\_size](structwifi__filter__info.md#a1b2d0448fc7f62654e3f5aacfba62f8f);

[ 677](structwifi__filter__info.md#aedd5e220cdde5768cb0f4aff920971cd) enum [wifi\_mgmt\_op](group__wifi__mgmt.md#gae129d0783276e662575af2314eef86cd) [oper](structwifi__filter__info.md#aedd5e220cdde5768cb0f4aff920971cd);

678};

679

[ 681](structwifi__channel__info.md)struct [wifi\_channel\_info](structwifi__channel__info.md) {

[ 683](structwifi__channel__info.md#a799cbc0a67764f6680322ba0f2ad3300) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [channel](structwifi__channel__info.md#a799cbc0a67764f6680322ba0f2ad3300);

[ 685](structwifi__channel__info.md#a43a7dd8c19d0c6540e3cc0b5d1d6165d) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [if\_index](structwifi__channel__info.md#a43a7dd8c19d0c6540e3cc0b5d1d6165d);

[ 687](structwifi__channel__info.md#aa8ef8a71b49ead3664fff9a4d61b1ce8) enum [wifi\_mgmt\_op](group__wifi__mgmt.md#gae129d0783276e662575af2314eef86cd) [oper](structwifi__channel__info.md#aa8ef8a71b49ead3664fff9a4d61b1ce8);

688};

689

690#include <[zephyr/net/net\_if.h](net__if_8h.md)>

691

[ 698](group__wifi__mgmt.md#gad34b366f1c315207ce0da587ca96d8d8)typedef void (\*[scan\_result\_cb\_t](group__wifi__mgmt.md#gad34b366f1c315207ce0da587ca96d8d8))(struct [net\_if](structnet__if.md) \*iface, int status,

699 struct [wifi\_scan\_result](structwifi__scan__result.md) \*entry);

700

701#ifdef CONFIG\_WIFI\_MGMT\_RAW\_SCAN\_RESULTS

708typedef void (\*raw\_scan\_result\_cb\_t)(struct [net\_if](structnet__if.md) \*iface, int status,

709 struct [wifi\_raw\_scan\_result](structwifi__raw__scan__result.md) \*entry);

710#endif /\* CONFIG\_WIFI\_MGMT\_RAW\_SCAN\_RESULTS \*/

711

[ 713](structwifi__mgmt__ops.md)struct [wifi\_mgmt\_ops](structwifi__mgmt__ops.md) {

[ 725](structwifi__mgmt__ops.md#a267030c27da3cdc251badd0ed7f7b1cb) int (\*[scan](structwifi__mgmt__ops.md#a267030c27da3cdc251badd0ed7f7b1cb))(const struct [device](structdevice.md) \*dev,

726 struct [wifi\_scan\_params](structwifi__scan__params.md) \*params,

727 [scan\_result\_cb\_t](group__wifi__mgmt.md#gad34b366f1c315207ce0da587ca96d8d8) cb);

[ 735](structwifi__mgmt__ops.md#ae6255ea77739918797b4f3c7a4634a75) int (\*[connect](structwifi__mgmt__ops.md#ae6255ea77739918797b4f3c7a4634a75))(const struct [device](structdevice.md) \*dev,

736 struct [wifi\_connect\_req\_params](structwifi__connect__req__params.md) \*params);

[ 743](structwifi__mgmt__ops.md#a5725c6fd93ae189a3019374cd4ad2ff4) int (\*[disconnect](structwifi__mgmt__ops.md#a5725c6fd93ae189a3019374cd4ad2ff4))(const struct [device](structdevice.md) \*dev);

[ 751](structwifi__mgmt__ops.md#ac2ce3a4a86c43e30d33261f71c44198a) int (\*[ap\_enable](structwifi__mgmt__ops.md#ac2ce3a4a86c43e30d33261f71c44198a))(const struct [device](structdevice.md) \*dev,

752 struct [wifi\_connect\_req\_params](structwifi__connect__req__params.md) \*params);

[ 759](structwifi__mgmt__ops.md#a5aa7a2be82eb1783872abda2b8978235) int (\*[ap\_disable](structwifi__mgmt__ops.md#a5aa7a2be82eb1783872abda2b8978235))(const struct [device](structdevice.md) \*dev);

[ 767](structwifi__mgmt__ops.md#af01aaec29be78c02314acf13b5c1b6f7) int (\*[ap\_sta\_disconnect](structwifi__mgmt__ops.md#af01aaec29be78c02314acf13b5c1b6f7))(const struct [device](structdevice.md) \*dev, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*mac);

[ 775](structwifi__mgmt__ops.md#adf157476d776bc9c068e99e1a0266fd3) int (\*[iface\_status](structwifi__mgmt__ops.md#adf157476d776bc9c068e99e1a0266fd3))(const struct [device](structdevice.md) \*dev, struct [wifi\_iface\_status](structwifi__iface__status.md) \*status);

776#if defined(CONFIG\_NET\_STATISTICS\_WIFI) || defined(\_\_DOXYGEN\_\_)

[ 784](structwifi__mgmt__ops.md#a5e6fdf836273fcde54efff4c77bfdf0e) int (\*[get\_stats](structwifi__mgmt__ops.md#a5e6fdf836273fcde54efff4c77bfdf0e))(const struct [device](structdevice.md) \*dev, struct [net\_stats\_wifi](structnet__stats__wifi.md) \*stats);

785#endif /\* CONFIG\_NET\_STATISTICS\_WIFI \*/

[ 793](structwifi__mgmt__ops.md#ac0f3f7fa699b1bc7db2358e77dd44cc4) int (\*[set\_power\_save](structwifi__mgmt__ops.md#ac0f3f7fa699b1bc7db2358e77dd44cc4))(const struct [device](structdevice.md) \*dev, struct [wifi\_ps\_params](structwifi__ps__params.md) \*params);

[ 801](structwifi__mgmt__ops.md#ab4500534b6abe0449290c8bd8f729fc4) int (\*[set\_twt](structwifi__mgmt__ops.md#ab4500534b6abe0449290c8bd8f729fc4))(const struct [device](structdevice.md) \*dev, struct [wifi\_twt\_params](structwifi__twt__params.md) \*params);

[ 809](structwifi__mgmt__ops.md#a52690b13f8a1e7b0c2302eaa24ae4c7f) int (\*[get\_power\_save\_config](structwifi__mgmt__ops.md#a52690b13f8a1e7b0c2302eaa24ae4c7f))(const struct [device](structdevice.md) \*dev, struct [wifi\_ps\_config](structwifi__ps__config.md) \*config);

[ 817](structwifi__mgmt__ops.md#a0a287c8acf2d7bf9333b755589294881) int (\*[reg\_domain](structwifi__mgmt__ops.md#a0a287c8acf2d7bf9333b755589294881))(const struct [device](structdevice.md) \*dev, struct [wifi\_reg\_domain](structwifi__reg__domain.md) \*[reg\_domain](structwifi__mgmt__ops.md#a0a287c8acf2d7bf9333b755589294881));

[ 825](structwifi__mgmt__ops.md#ad645276745ce8dd9685e0744efdfc733) int (\*[filter](structwifi__mgmt__ops.md#ad645276745ce8dd9685e0744efdfc733))(const struct [device](structdevice.md) \*dev, struct [wifi\_filter\_info](structwifi__filter__info.md) \*[filter](structwifi__mgmt__ops.md#ad645276745ce8dd9685e0744efdfc733));

[ 833](structwifi__mgmt__ops.md#ae2fb1bc35bf9255655a30a2ad8588b7c) int (\*[mode](structwifi__mgmt__ops.md#ae2fb1bc35bf9255655a30a2ad8588b7c))(const struct [device](structdevice.md) \*dev, struct [wifi\_mode\_info](structwifi__mode__info.md) \*[mode](structwifi__mgmt__ops.md#ae2fb1bc35bf9255655a30a2ad8588b7c));

[ 841](structwifi__mgmt__ops.md#af17ddfea01d0ab478f6fd50b1c9d6015) int (\*[channel](structwifi__mgmt__ops.md#af17ddfea01d0ab478f6fd50b1c9d6015))(const struct [device](structdevice.md) \*dev, struct [wifi\_channel\_info](structwifi__channel__info.md) \*[channel](structwifi__mgmt__ops.md#af17ddfea01d0ab478f6fd50b1c9d6015));

[ 854](structwifi__mgmt__ops.md#aa7e4bc3dbc960091d11ffe5454259885) int (\*[get\_version](structwifi__mgmt__ops.md#aa7e4bc3dbc960091d11ffe5454259885))(const struct [device](structdevice.md) \*dev, struct [wifi\_version](structwifi__version.md) \*params);

855};

856

[ 858](structnet__wifi__mgmt__offload.md)struct [net\_wifi\_mgmt\_offload](structnet__wifi__mgmt__offload.md) {

865#if defined(CONFIG\_WIFI\_USE\_NATIVE\_NETWORKING) || defined(\_\_DOXYGEN\_\_)

[ 867](structnet__wifi__mgmt__offload.md#a1d34a954a2f16d29f51dc51dd6fbb845) struct [ethernet\_api](structethernet__api.md) [wifi\_iface](structnet__wifi__mgmt__offload.md#a1d34a954a2f16d29f51dc51dd6fbb845);

868#else

870 struct [offloaded\_if\_api](structoffloaded__if__api.md) [wifi\_iface](structnet__wifi__mgmt__offload.md#a1d34a954a2f16d29f51dc51dd6fbb845);

871#endif

[ 873](structnet__wifi__mgmt__offload.md#a98fcc053d9820d2d981ed659520c9b3b) const struct [wifi\_mgmt\_ops](structwifi__mgmt__ops.md) \*const [wifi\_mgmt\_api](structnet__wifi__mgmt__offload.md#a98fcc053d9820d2d981ed659520c9b3b);

874

875#if defined(CONFIG\_WIFI\_NM\_WPA\_SUPPLICANT) || defined(\_\_DOXYGEN\_\_)

[ 877](structnet__wifi__mgmt__offload.md#a0b50b958d9d9bcba029a0859304dd84f) void \*[wifi\_drv\_ops](structnet__wifi__mgmt__offload.md#a0b50b958d9d9bcba029a0859304dd84f);

878#endif

879};

880

881#if defined(CONFIG\_WIFI\_NM\_WPA\_SUPPLICANT)

882/\* Make sure wifi\_drv\_ops is after wifi\_mgmt\_api \*/

883BUILD\_ASSERT(offsetof(struct [net\_wifi\_mgmt\_offload](structnet__wifi__mgmt__offload.md), wifi\_mgmt\_api) <

884 offsetof(struct [net\_wifi\_mgmt\_offload](structnet__wifi__mgmt__offload.md), wifi\_drv\_ops));

885#endif

886

887/\* Make sure that the network interface API is properly setup inside

888 \* Wifi mgmt offload API struct (it is the first one).

889 \*/

890BUILD\_ASSERT(offsetof(struct [net\_wifi\_mgmt\_offload](structnet__wifi__mgmt__offload.md), wifi\_iface) == 0);

891

[ 897](group__wifi__mgmt.md#ga036416696b1e3bc458ddbaf07a08d69d)void [wifi\_mgmt\_raise\_connect\_result\_event](group__wifi__mgmt.md#ga036416696b1e3bc458ddbaf07a08d69d)(struct [net\_if](structnet__if.md) \*iface, int status);

898

[ 904](group__wifi__mgmt.md#ga3b6edcf9b51afbf7a327d1a344bd7b87)void [wifi\_mgmt\_raise\_disconnect\_result\_event](group__wifi__mgmt.md#ga3b6edcf9b51afbf7a327d1a344bd7b87)(struct [net\_if](structnet__if.md) \*iface, int status);

905

[ 911](group__wifi__mgmt.md#ga7da6af0747bcba85f8afab30c92b5b43)void [wifi\_mgmt\_raise\_iface\_status\_event](group__wifi__mgmt.md#ga7da6af0747bcba85f8afab30c92b5b43)(struct [net\_if](structnet__if.md) \*iface,

912 struct [wifi\_iface\_status](structwifi__iface__status.md) \*[iface\_status](structwifi__mgmt__ops.md#adf157476d776bc9c068e99e1a0266fd3));

913

[ 919](group__wifi__mgmt.md#ga39404d15243ca084b253cae8fc07e374)void [wifi\_mgmt\_raise\_twt\_event](group__wifi__mgmt.md#ga39404d15243ca084b253cae8fc07e374)(struct [net\_if](structnet__if.md) \*iface,

920 struct [wifi\_twt\_params](structwifi__twt__params.md) \*twt\_params);

921

[ 927](group__wifi__mgmt.md#ga18f09a3196588b51d6c0644f82f639d7)void [wifi\_mgmt\_raise\_twt\_sleep\_state](group__wifi__mgmt.md#ga18f09a3196588b51d6c0644f82f639d7)(struct [net\_if](structnet__if.md) \*iface, int twt\_sleep\_state);

928

929#if defined(CONFIG\_WIFI\_MGMT\_RAW\_SCAN\_RESULTS) || defined(\_\_DOXYGEN\_\_)

[ 935](group__wifi__mgmt.md#ga71c99913bded844c4ca32ed9155bc470)void [wifi\_mgmt\_raise\_raw\_scan\_result\_event](group__wifi__mgmt.md#ga71c99913bded844c4ca32ed9155bc470)(struct [net\_if](structnet__if.md) \*iface,

936 struct [wifi\_raw\_scan\_result](structwifi__raw__scan__result.md) \*raw\_scan\_info);

937#endif /\* CONFIG\_WIFI\_MGMT\_RAW\_SCAN\_RESULTS \*/

938

[ 944](group__wifi__mgmt.md#gaa75246d6dc55dada389c9d31e2607d5c)void [wifi\_mgmt\_raise\_disconnect\_complete\_event](group__wifi__mgmt.md#gaa75246d6dc55dada389c9d31e2607d5c)(struct [net\_if](structnet__if.md) \*iface, int status);

945

[ 951](group__wifi__mgmt.md#ga67b52edeff76c2211b038f4aa90b8982)void [wifi\_mgmt\_raise\_ap\_enable\_result\_event](group__wifi__mgmt.md#ga67b52edeff76c2211b038f4aa90b8982)(struct [net\_if](structnet__if.md) \*iface, enum [wifi\_ap\_status](group__wifi__mgmt.md#gaaf730bf76adc06434c7ac63bf0417884) status);

952

[ 958](group__wifi__mgmt.md#gadee15c6a492a8ee13bea43812debb5d9)void [wifi\_mgmt\_raise\_ap\_disable\_result\_event](group__wifi__mgmt.md#gadee15c6a492a8ee13bea43812debb5d9)(struct [net\_if](structnet__if.md) \*iface, enum [wifi\_ap\_status](group__wifi__mgmt.md#gaaf730bf76adc06434c7ac63bf0417884) status);

959

[ 965](group__wifi__mgmt.md#gac8f17f0aa3e426a5cdb731727b9b9ce3)void [wifi\_mgmt\_raise\_ap\_sta\_connected\_event](group__wifi__mgmt.md#gac8f17f0aa3e426a5cdb731727b9b9ce3)(struct [net\_if](structnet__if.md) \*iface,

966 struct [wifi\_ap\_sta\_info](structwifi__ap__sta__info.md) \*sta\_info);

967

[ 972](group__wifi__mgmt.md#ga49fb9c3908be61d847b31c99be6afc42)void [wifi\_mgmt\_raise\_ap\_sta\_disconnected\_event](group__wifi__mgmt.md#ga49fb9c3908be61d847b31c99be6afc42)(struct [net\_if](structnet__if.md) \*iface,

973 struct [wifi\_ap\_sta\_info](structwifi__ap__sta__info.md) \*sta\_info);

974

978#ifdef \_\_cplusplus

979}

980#endif

981

982#endif /\* ZEPHYR\_INCLUDE\_NET\_WIFI\_MGMT\_H\_ \*/

[ethernet.h](ethernet_8h.md)

Ethernet.

[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)

#define NET\_MGMT\_DEFINE\_REQUEST\_HANDLER(\_mgmt\_request)

**Definition** net\_mgmt.h:96

[wifi\_mgmt\_raise\_connect\_result\_event](group__wifi__mgmt.md#ga036416696b1e3bc458ddbaf07a08d69d)

void wifi\_mgmt\_raise\_connect\_result\_event(struct net\_if \*iface, int status)

Wi-Fi management connect result event.

[wifi\_ps](group__wifi__mgmt.md#ga0fffeb57b68fb8cdef9d3d571368b8ca)

wifi\_ps

Wi-Fi power save states.

**Definition** wifi.h:211

[NET\_REQUEST\_WIFI\_PS\_CONFIG](group__wifi__mgmt.md#ga1032f3773cfe6130da4d4d498b044ee2)

#define NET\_REQUEST\_WIFI\_PS\_CONFIG

**Definition** wifi\_mgmt.h:136

[wifi\_mgmt\_raise\_twt\_sleep\_state](group__wifi__mgmt.md#ga18f09a3196588b51d6c0644f82f639d7)

void wifi\_mgmt\_raise\_twt\_sleep\_state(struct net\_if \*iface, int twt\_sleep\_state)

Wi-Fi management TWT sleep state event.

[NET\_REQUEST\_WIFI\_SCAN](group__wifi__mgmt.md#ga1c277da90986fa52dca182c4d922646f)

#define NET\_REQUEST\_WIFI\_SCAN

**Definition** wifi\_mgmt.h:91

[wifi\_frequency\_bands](group__wifi__mgmt.md#ga1e2f0439a322355fa7368ea880c9c15d)

wifi\_frequency\_bands

IEEE 802.11 operational frequency bands (not exhaustive).

**Definition** wifi.h:81

[wifi\_mfp\_options](group__wifi__mgmt.md#ga1f252da47d9650023d7fff6d08e49c76)

wifi\_mfp\_options

IEEE 802.11w - Management frame protection.

**Definition** wifi.h:62

[WIFI\_MAC\_ADDR\_LEN](group__wifi__mgmt.md#ga29409ff83a53c6464decdde9bdd04de6)

#define WIFI\_MAC\_ADDR\_LEN

**Definition** wifi.h:104

[NET\_REQUEST\_WIFI\_REG\_DOMAIN](group__wifi__mgmt.md#ga2b27d102b779a6d846b375854768fb7f)

#define NET\_REQUEST\_WIFI\_REG\_DOMAIN

**Definition** wifi\_mgmt.h:140

[NET\_REQUEST\_WIFI\_PACKET\_FILTER](group__wifi__mgmt.md#ga3098e817d12bf4619c9fd2698508fb4e)

#define NET\_REQUEST\_WIFI\_PACKET\_FILTER

**Definition** wifi\_mgmt.h:155

[wifi\_twt\_setup\_cmd](group__wifi__mgmt.md#ga31c78afc89bfdc4b54cee177843f8022)

wifi\_twt\_setup\_cmd

Wi-Fi Target Wake Time (TWT) setup commands.

**Definition** wifi.h:292

[wifi\_twt\_sleep\_state](group__wifi__mgmt.md#ga38c184ea35c02f304cccdf389ca6d552)

wifi\_twt\_sleep\_state

Wi-Fi TWT sleep states.

**Definition** wifi\_mgmt.h:613

[wifi\_mgmt\_raise\_twt\_event](group__wifi__mgmt.md#ga39404d15243ca084b253cae8fc07e374)

void wifi\_mgmt\_raise\_twt\_event(struct net\_if \*iface, struct wifi\_twt\_params \*twt\_params)

Wi-Fi management TWT event.

[wifi\_mgmt\_raise\_disconnect\_result\_event](group__wifi__mgmt.md#ga3b6edcf9b51afbf7a327d1a344bd7b87)

void wifi\_mgmt\_raise\_disconnect\_result\_event(struct net\_if \*iface, int status)

Wi-Fi management disconnect result event.

[NET\_REQUEST\_WIFI\_IFACE\_STATUS](group__wifi__mgmt.md#ga3e45f6ee3801553619d8eb7d0af506eb)

#define NET\_REQUEST\_WIFI\_IFACE\_STATUS

**Definition** wifi\_mgmt.h:116

[NET\_REQUEST\_WIFI\_VERSION](group__wifi__mgmt.md#ga3e60c29ca9ce95d17a7fff087290f7f1)

#define NET\_REQUEST\_WIFI\_VERSION

**Definition** wifi\_mgmt.h:170

[NET\_REQUEST\_WIFI\_PS\_MODE](group__wifi__mgmt.md#ga437b00fd5e46846abe666f4a3986d847)

#define NET\_REQUEST\_WIFI\_PS\_MODE

**Definition** wifi\_mgmt.h:126

[wifi\_mgmt\_raise\_ap\_sta\_disconnected\_event](group__wifi__mgmt.md#ga49fb9c3908be61d847b31c99be6afc42)

void wifi\_mgmt\_raise\_ap\_sta\_disconnected\_event(struct net\_if \*iface, struct wifi\_ap\_sta\_info \*sta\_info)

Wi-Fi management AP mode STA disconnected event.

[wifi\_twt\_setup\_resp\_status](group__wifi__mgmt.md#ga4d03aedac13ee4512d7717ac624f319a)

wifi\_twt\_setup\_resp\_status

Wi-Fi Target Wake Time (TWT) negotiation status.

**Definition** wifi.h:315

[WIFI\_MGMT\_SCAN\_CHAN\_MAX\_MANUAL](group__wifi__mgmt.md#ga4ed2294d0250a2e03e2e579cf0635e2c)

#define WIFI\_MGMT\_SCAN\_CHAN\_MAX\_MANUAL

**Definition** wifi\_mgmt.h:47

[wifi\_iface\_mode](group__wifi__mgmt.md#ga584f6239ac14e2bedc5e6bd72756423b)

wifi\_iface\_mode

Wi-Fi interface modes.

**Definition** wifi.h:148

[NET\_REQUEST\_WIFI\_PS\_TIMEOUT](group__wifi__mgmt.md#ga61d035b3f80ee8b7b6fefea9fa7a6d84)

#define NET\_REQUEST\_WIFI\_PS\_TIMEOUT

**Definition** wifi\_mgmt.h:145

[WIFI\_MAX\_TWT\_FLOWS](group__wifi__mgmt.md#ga620bdb1485ddbe72229adee05e6c353a)

#define WIFI\_MAX\_TWT\_FLOWS

**Definition** wifi\_mgmt.h:534

[NET\_REQUEST\_WIFI\_AP\_ENABLE](group__wifi__mgmt.md#ga638d2eb0a5029c1af46a91b523ed8589)

#define NET\_REQUEST\_WIFI\_AP\_ENABLE

**Definition** wifi\_mgmt.h:106

[WIFI\_COUNTRY\_CODE\_LEN](group__wifi__mgmt.md#ga6766ef7bcb001f1fb526a4083b6cd8bc)

#define WIFI\_COUNTRY\_CODE\_LEN

**Definition** wifi.h:25

[wifi\_mgmt\_raise\_ap\_enable\_result\_event](group__wifi__mgmt.md#ga67b52edeff76c2211b038f4aa90b8982)

void wifi\_mgmt\_raise\_ap\_enable\_result\_event(struct net\_if \*iface, enum wifi\_ap\_status status)

Wi-Fi management AP mode enable result event.

[NET\_REQUEST\_WIFI\_PS](group__wifi__mgmt.md#ga68aaced888f98e1ba4e6b61b53e5e2ba)

#define NET\_REQUEST\_WIFI\_PS

**Definition** wifi\_mgmt.h:121

[wifi\_twt\_negotiation\_type](group__wifi__mgmt.md#ga695123cd534e2499f516a07fdc5cafa8)

wifi\_twt\_negotiation\_type

Wi-Fi Target Wake Time (TWT) negotiation types.

**Definition** wifi.h:279

[wifi\_mgmt\_raise\_raw\_scan\_result\_event](group__wifi__mgmt.md#ga71c99913bded844c4ca32ed9155bc470)

void wifi\_mgmt\_raise\_raw\_scan\_result\_event(struct net\_if \*iface, struct wifi\_raw\_scan\_result \*raw\_scan\_info)

Wi-Fi management raw scan result event.

[wifi\_mgmt\_raise\_iface\_status\_event](group__wifi__mgmt.md#ga7da6af0747bcba85f8afab30c92b5b43)

void wifi\_mgmt\_raise\_iface\_status\_event(struct net\_if \*iface, struct wifi\_iface\_status \*iface\_status)

Wi-Fi management interface status event.

[wifi\_conn\_status](group__wifi__mgmt.md#ga86a5741e54aeb3e290142b0de217b8a8)

wifi\_conn\_status

Wi-Fi connect result codes.

**Definition** wifi\_mgmt.h:369

[WIFI\_MGMT\_SCAN\_SSID\_FILT\_MAX](group__wifi__mgmt.md#ga8f1d15bfcd0776eee7cae2590da6c174)

#define WIFI\_MGMT\_SCAN\_SSID\_FILT\_MAX

**Definition** wifi\_mgmt.h:41

[NET\_REQUEST\_WIFI\_DISCONNECT](group__wifi__mgmt.md#ga90afd8d4e83056463ec6e667ed8ea60a)

#define NET\_REQUEST\_WIFI\_DISCONNECT

**Definition** wifi\_mgmt.h:101

[wifi\_twt\_fail\_reason](group__wifi__mgmt.md#ga97fa304f9a1db2294a93cccd4c93bcf6)

wifi\_twt\_fail\_reason

Target Wake Time (TWT) error codes.

**Definition** wifi.h:323

[net\_request\_wifi\_cmd](group__wifi__mgmt.md#ga99a55137188119f65f9d2bb4f57cac77)

net\_request\_wifi\_cmd

Wi-Fi management commands.

**Definition** wifi\_mgmt.h:53

[NET\_REQUEST\_WIFI\_MODE](group__wifi__mgmt.md#ga9b4da60a8108b0cc431ac1eecfca0cd0)

#define NET\_REQUEST\_WIFI\_MODE

**Definition** wifi\_mgmt.h:150

[NET\_REQUEST\_WIFI\_AP\_STA\_DISCONNECT](group__wifi__mgmt.md#gaa3e52e08d89a1104f07207e52b81d503)

#define NET\_REQUEST\_WIFI\_AP\_STA\_DISCONNECT

**Definition** wifi\_mgmt.h:165

[wifi\_mgmt\_raise\_disconnect\_complete\_event](group__wifi__mgmt.md#gaa75246d6dc55dada389c9d31e2607d5c)

void wifi\_mgmt\_raise\_disconnect\_complete\_event(struct net\_if \*iface, int status)

Wi-Fi management disconnect complete event.

[NET\_REQUEST\_WIFI\_CONNECT](group__wifi__mgmt.md#gaa7ab2a97950a22736bb69f60b459f0f6)

#define NET\_REQUEST\_WIFI\_CONNECT

**Definition** wifi\_mgmt.h:96

[wifi\_ap\_status](group__wifi__mgmt.md#gaaf730bf76adc06434c7ac63bf0417884)

wifi\_ap\_status

Wi-Fi AP mode result codes.

**Definition** wifi\_mgmt.h:399

[NET\_REQUEST\_WIFI\_TWT](group__wifi__mgmt.md#gab84fd7e9ca0bf0b2b9d08889dda26aad)

#define NET\_REQUEST\_WIFI\_TWT

**Definition** wifi\_mgmt.h:131

[wifi\_link\_mode](group__wifi__mgmt.md#gabdb2a784d4727b71ab44cca04e422c62)

wifi\_link\_mode

Wi-Fi link operating modes.

**Definition** wifi.h:174

[wifi\_ps\_param\_type](group__wifi__mgmt.md#gabe45d132797047c098041331c8f6f912)

wifi\_ps\_param\_type

Wi-Fi power save parameters.

**Definition** wifi.h:390

[net\_event\_wifi\_cmd](group__wifi__mgmt.md#gac2638308cbb0d268831f1618cf8e1fa8)

net\_event\_wifi\_cmd

Wi-Fi management events.

**Definition** wifi\_mgmt.h:176

[wifi\_disconn\_reason](group__wifi__mgmt.md#gac782af0a60b202fd19597cabb7bd3a9a)

wifi\_disconn\_reason

Wi-Fi disconnect reason codes.

**Definition** wifi\_mgmt.h:385

[wifi\_ps\_wakeup\_mode](group__wifi__mgmt.md#gac7f907644847e905d67c709fa4afae7f)

wifi\_ps\_wakeup\_mode

Wi-Fi power save modes.

**Definition** wifi.h:404

[wifi\_mgmt\_raise\_ap\_sta\_connected\_event](group__wifi__mgmt.md#gac8f17f0aa3e426a5cdb731727b9b9ce3)

void wifi\_mgmt\_raise\_ap\_sta\_connected\_event(struct net\_if \*iface, struct wifi\_ap\_sta\_info \*sta\_info)

Wi-Fi management AP mode STA connected event.

[wifi\_twt\_operation](group__wifi__mgmt.md#gad0e998aeb1b27c4f203ca76339d323a3)

wifi\_twt\_operation

Wi-Fi Target Wake Time (TWT) operations.

**Definition** wifi.h:268

[wifi\_scan\_type](group__wifi__mgmt.md#gad30e29eda65ccafdbd7f11865937b8ea)

wifi\_scan\_type

Wi-Fi scanning types.

**Definition** wifi.h:203

[scan\_result\_cb\_t](group__wifi__mgmt.md#gad34b366f1c315207ce0da587ca96d8d8)

void(\* scan\_result\_cb\_t)(struct net\_if \*iface, int status, struct wifi\_scan\_result \*entry)

Scan result callback.

**Definition** wifi\_mgmt.h:698

[wifi\_twt\_teardown\_status](group__wifi__mgmt.md#gad3709d07aaa3ed59b48f9dd7bd181989)

wifi\_twt\_teardown\_status

Wi-Fi Target Wake Time (TWT) teradown status.

**Definition** wifi.h:349

[WIFI\_SSID\_MAX\_LEN](group__wifi__mgmt.md#gad62c60666c9fdffe2e0e9c4388f87886)

#define WIFI\_SSID\_MAX\_LEN

**Definition** wifi.h:100

[NET\_REQUEST\_WIFI\_CHANNEL](group__wifi__mgmt.md#gad9614d2368f8399850aaec05e40bdc78)

#define NET\_REQUEST\_WIFI\_CHANNEL

**Definition** wifi\_mgmt.h:160

[wifi\_config\_ps\_param\_fail\_reason](group__wifi__mgmt.md#gad98099584d2222ede93aba42b1fbaff0)

wifi\_config\_ps\_param\_fail\_reason

Wi-Fi power save error codes.

**Definition** wifi.h:415

[wifi\_security\_type](group__wifi__mgmt.md#gadde31a04fa25ed805115c6b31854cd9c)

wifi\_security\_type

IEEE 802.11 security types.

**Definition** wifi.h:35

[wifi\_mgmt\_raise\_ap\_disable\_result\_event](group__wifi__mgmt.md#gadee15c6a492a8ee13bea43812debb5d9)

void wifi\_mgmt\_raise\_ap\_disable\_result\_event(struct net\_if \*iface, enum wifi\_ap\_status status)

Wi-Fi management AP mode disable result event.

[wifi\_mgmt\_op](group__wifi__mgmt.md#gae129d0783276e662575af2314eef86cd)

wifi\_mgmt\_op

Generic get/set operation for any command.

**Definition** wifi\_mgmt.h:575

[NET\_REQUEST\_WIFI\_AP\_DISABLE](group__wifi__mgmt.md#gaf81f62bf4c9e331a095acbf0d24ca1a2)

#define NET\_REQUEST\_WIFI\_AP\_DISABLE

**Definition** wifi\_mgmt.h:111

[wifi\_ps\_mode](group__wifi__mgmt.md#gaffae7d2a754be5eb952ad2b83edad54c)

wifi\_ps\_mode

Wi-Fi power save modes.

**Definition** wifi.h:222

[WIFI\_TWT\_STATE\_SLEEP](group__wifi__mgmt.md#gga38c184ea35c02f304cccdf389ca6d552a37a7aba20723b6614e39e1c417f3113c)

@ WIFI\_TWT\_STATE\_SLEEP

TWT sleep state: sleeping.

**Definition** wifi\_mgmt.h:615

[WIFI\_TWT\_STATE\_AWAKE](group__wifi__mgmt.md#gga38c184ea35c02f304cccdf389ca6d552a7b7b45f85d9644f897ca00bd7864e1b0)

@ WIFI\_TWT\_STATE\_AWAKE

TWT sleep state: awake.

**Definition** wifi\_mgmt.h:617

[WIFI\_STATUS\_CONN\_AP\_NOT\_FOUND](group__wifi__mgmt.md#gga86a5741e54aeb3e290142b0de217b8a8a2ae79fa389bb447fa108e0107aeff2f4)

@ WIFI\_STATUS\_CONN\_AP\_NOT\_FOUND

Connection failed - AP not found.

**Definition** wifi\_mgmt.h:379

[WIFI\_STATUS\_CONN\_SUCCESS](group__wifi__mgmt.md#gga86a5741e54aeb3e290142b0de217b8a8a380410b02b1e12599f37d1dcb844f5bd)

@ WIFI\_STATUS\_CONN\_SUCCESS

Connection successful.

**Definition** wifi\_mgmt.h:371

[WIFI\_STATUS\_CONN\_WRONG\_PASSWORD](group__wifi__mgmt.md#gga86a5741e54aeb3e290142b0de217b8a8a90d91f96a35c9f6847cbc7abd8c20bf8)

@ WIFI\_STATUS\_CONN\_WRONG\_PASSWORD

Connection failed - wrong password.

**Definition** wifi\_mgmt.h:375

[WIFI\_STATUS\_CONN\_FAIL](group__wifi__mgmt.md#gga86a5741e54aeb3e290142b0de217b8a8ab80ec4b70c75695fbe698034e2cb6a44)

@ WIFI\_STATUS\_CONN\_FAIL

Connection failed - generic failure.

**Definition** wifi\_mgmt.h:373

[WIFI\_STATUS\_CONN\_TIMEOUT](group__wifi__mgmt.md#gga86a5741e54aeb3e290142b0de217b8a8abb8783b92aec2ed1ffc6331979888563)

@ WIFI\_STATUS\_CONN\_TIMEOUT

Connection timed out.

**Definition** wifi\_mgmt.h:377

[NET\_REQUEST\_WIFI\_CMD\_TWT](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a1c9dc2d698326d987ffe5bfd35a9ed09)

@ NET\_REQUEST\_WIFI\_CMD\_TWT

Setup or teardown TWT flow.

**Definition** wifi\_mgmt.h:71

[NET\_REQUEST\_WIFI\_CMD\_PACKET\_FILTER](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a2579ace546bf6954c111eb5951e894f5)

@ NET\_REQUEST\_WIFI\_CMD\_PACKET\_FILTER

Set or get packet filter setting for current mode.

**Definition** wifi\_mgmt.h:81

[NET\_REQUEST\_WIFI\_CMD\_AP\_ENABLE](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a28267d33b555433271cb121d62194a4c)

@ NET\_REQUEST\_WIFI\_CMD\_AP\_ENABLE

Enable AP mode.

**Definition** wifi\_mgmt.h:61

[NET\_REQUEST\_WIFI\_CMD\_REG\_DOMAIN](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a367cc44caefd313e0c7ad3badc081456)

@ NET\_REQUEST\_WIFI\_CMD\_REG\_DOMAIN

Set or get regulatory domain.

**Definition** wifi\_mgmt.h:75

[NET\_REQUEST\_WIFI\_CMD\_SCAN](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a4aadf9114010c09bd7420c99a2049d5a)

@ NET\_REQUEST\_WIFI\_CMD\_SCAN

Scan for Wi-Fi networks.

**Definition** wifi\_mgmt.h:55

[NET\_REQUEST\_WIFI\_CMD\_IFACE\_STATUS](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a6af9d52df8f9db6393044e42e10ff0de)

@ NET\_REQUEST\_WIFI\_CMD\_IFACE\_STATUS

Get interface status.

**Definition** wifi\_mgmt.h:65

[NET\_REQUEST\_WIFI\_CMD\_AP\_STA\_DISCONNECT](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a6f3865aa6a4d7633e241ee2b002c1b5a)

@ NET\_REQUEST\_WIFI\_CMD\_AP\_STA\_DISCONNECT

Disconnect a STA from AP.

**Definition** wifi\_mgmt.h:85

[NET\_REQUEST\_WIFI\_CMD\_AP\_DISABLE](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a6fe9d7137b4cd20de880955b27382ccf)

@ NET\_REQUEST\_WIFI\_CMD\_AP\_DISABLE

Disable AP mode.

**Definition** wifi\_mgmt.h:63

[NET\_REQUEST\_WIFI\_CMD\_CONNECT](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a78c958877ee60c90803c925b6b2f057a)

@ NET\_REQUEST\_WIFI\_CMD\_CONNECT

Connect to a Wi-Fi network.

**Definition** wifi\_mgmt.h:57

[NET\_REQUEST\_WIFI\_CMD\_PS\_MODE](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a7bbc7ba59a57a539360d5f148c4d85f9)

@ NET\_REQUEST\_WIFI\_CMD\_PS\_MODE

Set power save mode.

**Definition** wifi\_mgmt.h:69

[NET\_REQUEST\_WIFI\_CMD\_VERSION](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a7d9596f2cce54c9e050d89469e86eccb)

@ NET\_REQUEST\_WIFI\_CMD\_VERSION

Get Wi-Fi driver and Firmware versions.

**Definition** wifi\_mgmt.h:87

[NET\_REQUEST\_WIFI\_CMD\_CHANNEL](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77aade3d7a43c730a52f7876c6486170bb2)

@ NET\_REQUEST\_WIFI\_CMD\_CHANNEL

Set or get Wi-Fi channel for Monitor or TX-Injection mode.

**Definition** wifi\_mgmt.h:83

[NET\_REQUEST\_WIFI\_CMD\_MODE](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77ab7183584bdf5fe673d39fa0d090e3899)

@ NET\_REQUEST\_WIFI\_CMD\_MODE

Set or get Mode of operation.

**Definition** wifi\_mgmt.h:79

[NET\_REQUEST\_WIFI\_CMD\_PS](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77abf9fb93c205fa36f74a9ef19d3d0351a)

@ NET\_REQUEST\_WIFI\_CMD\_PS

Set power save status.

**Definition** wifi\_mgmt.h:67

[NET\_REQUEST\_WIFI\_CMD\_DISCONNECT](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77ac33941da138b993f7a1158d91469bcb7)

@ NET\_REQUEST\_WIFI\_CMD\_DISCONNECT

Disconnect from a Wi-Fi network.

**Definition** wifi\_mgmt.h:59

[NET\_REQUEST\_WIFI\_CMD\_PS\_CONFIG](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77ae6ce1c605d1bf7c09650ec15d74e77e9)

@ NET\_REQUEST\_WIFI\_CMD\_PS\_CONFIG

Get power save config.

**Definition** wifi\_mgmt.h:73

[NET\_REQUEST\_WIFI\_CMD\_MAX](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77af68077193672e52cc0e3361bacee77c9)

@ NET\_REQUEST\_WIFI\_CMD\_MAX

**Definition** wifi\_mgmt.h:88

[NET\_REQUEST\_WIFI\_CMD\_PS\_TIMEOUT](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77af934bbb1b130b0ec6d2f993b4589d2ad)

@ NET\_REQUEST\_WIFI\_CMD\_PS\_TIMEOUT

Set power save timeout.

**Definition** wifi\_mgmt.h:77

[WIFI\_STATUS\_AP\_CHANNEL\_NOT\_ALLOWED](group__wifi__mgmt.md#ggaaf730bf76adc06434c7ac63bf0417884a0b1cb592c54c16e8a54defee71c5fd15)

@ WIFI\_STATUS\_AP\_CHANNEL\_NOT\_ALLOWED

AP mode enable failed - channel not allowed.

**Definition** wifi\_mgmt.h:407

[WIFI\_STATUS\_AP\_SUCCESS](group__wifi__mgmt.md#ggaaf730bf76adc06434c7ac63bf0417884a0df52848da8735892d0eb1e381b2cd7c)

@ WIFI\_STATUS\_AP\_SUCCESS

AP mode enable or disable successful.

**Definition** wifi\_mgmt.h:401

[WIFI\_STATUS\_AP\_OP\_NOT\_SUPPORTED](group__wifi__mgmt.md#ggaaf730bf76adc06434c7ac63bf0417884a2105e6c49b3bcb5f7dcacbc1e5ce9cca)

@ WIFI\_STATUS\_AP\_OP\_NOT\_SUPPORTED

AP mode enable failed - operation not supported.

**Definition** wifi\_mgmt.h:413

[WIFI\_STATUS\_AP\_OP\_NOT\_PERMITTED](group__wifi__mgmt.md#ggaaf730bf76adc06434c7ac63bf0417884a36a58980bdc7877c910441590137ddbe)

@ WIFI\_STATUS\_AP\_OP\_NOT\_PERMITTED

AP mode enable failed - operation not permitted.

**Definition** wifi\_mgmt.h:415

[WIFI\_STATUS\_AP\_CHANNEL\_NOT\_SUPPORTED](group__wifi__mgmt.md#ggaaf730bf76adc06434c7ac63bf0417884a5acb85a2361ca72ed10966b829c5753b)

@ WIFI\_STATUS\_AP\_CHANNEL\_NOT\_SUPPORTED

AP mode enable failed - channel not supported.

**Definition** wifi\_mgmt.h:405

[WIFI\_STATUS\_AP\_FAIL](group__wifi__mgmt.md#ggaaf730bf76adc06434c7ac63bf0417884a6c6801381caa3862004662169202fa9a)

@ WIFI\_STATUS\_AP\_FAIL

AP mode enable or disable failed - generic failure.

**Definition** wifi\_mgmt.h:403

[WIFI\_STATUS\_AP\_AUTH\_TYPE\_NOT\_SUPPORTED](group__wifi__mgmt.md#ggaaf730bf76adc06434c7ac63bf0417884abe5a626d22051522255d98fdfdfbfcc8)

@ WIFI\_STATUS\_AP\_AUTH\_TYPE\_NOT\_SUPPORTED

AP mode enable failed - authentication type not supported.

**Definition** wifi\_mgmt.h:411

[WIFI\_STATUS\_AP\_SSID\_NOT\_ALLOWED](group__wifi__mgmt.md#ggaaf730bf76adc06434c7ac63bf0417884ac18a7b551f8c6bb7737b0e8e60c323ce)

@ WIFI\_STATUS\_AP\_SSID\_NOT\_ALLOWED

AP mode enable failed - SSID not allowed.

**Definition** wifi\_mgmt.h:409

[NET\_EVENT\_WIFI\_CMD\_AP\_STA\_DISCONNECTED](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8a3678a39f9542968958b5575d571d4e2e)

@ NET\_EVENT\_WIFI\_CMD\_AP\_STA\_DISCONNECTED

STA disconnected from AP.

**Definition** wifi\_mgmt.h:204

[NET\_EVENT\_WIFI\_CMD\_SCAN\_RESULT](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8a37e9ab2a6832153fa968337d920e587e)

@ NET\_EVENT\_WIFI\_CMD\_SCAN\_RESULT

Scan results available.

**Definition** wifi\_mgmt.h:178

[NET\_EVENT\_WIFI\_CMD\_DISCONNECT\_RESULT](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8a3a3b0387f83d8fb24a0e27312468b0eb)

@ NET\_EVENT\_WIFI\_CMD\_DISCONNECT\_RESULT

Disconnect result.

**Definition** wifi\_mgmt.h:184

[NET\_EVENT\_WIFI\_CMD\_TWT\_SLEEP\_STATE](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8a78838bf7ce80cee5e803712cd0286750)

@ NET\_EVENT\_WIFI\_CMD\_TWT\_SLEEP\_STATE

TWT sleep status: awake or sleeping, can be used by application to determine if it can send data or n...

**Definition** wifi\_mgmt.h:192

[NET\_EVENT\_WIFI\_CMD\_AP\_ENABLE\_RESULT](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8abd1797564427886eeb14dd293ae86a9b)

@ NET\_EVENT\_WIFI\_CMD\_AP\_ENABLE\_RESULT

AP mode enable result.

**Definition** wifi\_mgmt.h:198

[NET\_EVENT\_WIFI\_CMD\_AP\_STA\_CONNECTED](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8abd4269b2cd1302ce61da4f8d7bb9d5fb)

@ NET\_EVENT\_WIFI\_CMD\_AP\_STA\_CONNECTED

STA connected to AP.

**Definition** wifi\_mgmt.h:202

[NET\_EVENT\_WIFI\_CMD\_SCAN\_DONE](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8ad753b7e4588257815f4a60a539ca2018)

@ NET\_EVENT\_WIFI\_CMD\_SCAN\_DONE

Scan done.

**Definition** wifi\_mgmt.h:180

[NET\_EVENT\_WIFI\_CMD\_TWT](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8adad71603ed829ed92d06f8c40efa9b18)

@ NET\_EVENT\_WIFI\_CMD\_TWT

TWT events.

**Definition** wifi\_mgmt.h:188

[NET\_EVENT\_WIFI\_CMD\_RAW\_SCAN\_RESULT](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8addf15c69512be7ab4957e7c0b3fde0ac)

@ NET\_EVENT\_WIFI\_CMD\_RAW\_SCAN\_RESULT

Raw scan results available.

**Definition** wifi\_mgmt.h:194

[NET\_EVENT\_WIFI\_CMD\_AP\_DISABLE\_RESULT](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8aeec3d7a9191280c2326034a17555308d)

@ NET\_EVENT\_WIFI\_CMD\_AP\_DISABLE\_RESULT

AP mode disable result.

**Definition** wifi\_mgmt.h:200

[NET\_EVENT\_WIFI\_CMD\_DISCONNECT\_COMPLETE](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8af1c42bd59f01260c64ede07da436c18f)

@ NET\_EVENT\_WIFI\_CMD\_DISCONNECT\_COMPLETE

Disconnect complete.

**Definition** wifi\_mgmt.h:196

[NET\_EVENT\_WIFI\_CMD\_IFACE\_STATUS](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8af4b3f1969b96f63253851c26c3882a14)

@ NET\_EVENT\_WIFI\_CMD\_IFACE\_STATUS

Interface status.

**Definition** wifi\_mgmt.h:186

[NET\_EVENT\_WIFI\_CMD\_CONNECT\_RESULT](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8af76f28777b91b365dc3f97028bc18e3c)

@ NET\_EVENT\_WIFI\_CMD\_CONNECT\_RESULT

Connect result.

**Definition** wifi\_mgmt.h:182

[WIFI\_REASON\_DISCONN\_INACTIVITY](group__wifi__mgmt.md#ggac782af0a60b202fd19597cabb7bd3a9aa05fe2f87de30de47ee48f7615c2206e6)

@ WIFI\_REASON\_DISCONN\_INACTIVITY

Disconnected due to inactivity.

**Definition** wifi\_mgmt.h:393

[WIFI\_REASON\_DISCONN\_AP\_LEAVING](group__wifi__mgmt.md#ggac782af0a60b202fd19597cabb7bd3a9aa34e3f78ce43db3daeaf32038e0baf204)

@ WIFI\_REASON\_DISCONN\_AP\_LEAVING

Disconnected due to AP leaving.

**Definition** wifi\_mgmt.h:391

[WIFI\_REASON\_DISCONN\_UNSPECIFIED](group__wifi__mgmt.md#ggac782af0a60b202fd19597cabb7bd3a9aa87f5d64a9fd3acf8d67c698199779e5c)

@ WIFI\_REASON\_DISCONN\_UNSPECIFIED

Unspecified reason.

**Definition** wifi\_mgmt.h:387

[WIFI\_REASON\_DISCONN\_USER\_REQUEST](group__wifi__mgmt.md#ggac782af0a60b202fd19597cabb7bd3a9aaee75adafb52bd6ecaa547a76c6ccd0a7)

@ WIFI\_REASON\_DISCONN\_USER\_REQUEST

Disconnected due to user request.

**Definition** wifi\_mgmt.h:389

[WIFI\_MGMT\_GET](group__wifi__mgmt.md#ggae129d0783276e662575af2314eef86cda6b8183a773e0cdfa85bc4b41ae70fdcd)

@ WIFI\_MGMT\_GET

Get operation.

**Definition** wifi\_mgmt.h:577

[WIFI\_MGMT\_SET](group__wifi__mgmt.md#ggae129d0783276e662575af2314eef86cdaa0d5931c8275a8d3288ab668b6dfb5a1)

@ WIFI\_MGMT\_SET

Set operation.

**Definition** wifi\_mgmt.h:579

[net\_if.h](net__if_8h.md)

Public API for network interface.

[net\_mgmt.h](net__mgmt_8h.md)

Network Management API public header.

[offloaded\_netdev.h](offloaded__netdev_8h.md)

Offloaded network device iface API.

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

\_\_UINT64\_TYPE\_\_ uint64\_t

**Definition** stdint.h:91

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6)

\_\_INT8\_TYPE\_\_ int8\_t

**Definition** stdint.h:72

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:387

[ethernet\_api](structethernet__api.md)

**Definition** ethernet.h:473

[net\_if](structnet__if.md)

Network Interface structure.

**Definition** net\_if.h:615

[net\_stats\_wifi](structnet__stats__wifi.md)

All Wi-Fi specific statistics.

**Definition** net\_stats.h:490

[net\_wifi\_mgmt\_offload](structnet__wifi__mgmt__offload.md)

Wi-Fi management offload API.

**Definition** wifi\_mgmt.h:858

[net\_wifi\_mgmt\_offload::wifi\_drv\_ops](structnet__wifi__mgmt__offload.md#a0b50b958d9d9bcba029a0859304dd84f)

void \* wifi\_drv\_ops

Wi-Fi supplicant driver API.

**Definition** wifi\_mgmt.h:877

[net\_wifi\_mgmt\_offload::wifi\_iface](structnet__wifi__mgmt__offload.md#a1d34a954a2f16d29f51dc51dd6fbb845)

struct ethernet\_api wifi\_iface

Mandatory to get in first position.

**Definition** wifi\_mgmt.h:867

[net\_wifi\_mgmt\_offload::wifi\_mgmt\_api](structnet__wifi__mgmt__offload.md#a98fcc053d9820d2d981ed659520c9b3b)

const struct wifi\_mgmt\_ops \*const wifi\_mgmt\_api

Wi-Fi management API.

**Definition** wifi\_mgmt.h:873

[offloaded\_if\_api](structoffloaded__if__api.md)

Extended net\_if\_api for offloaded ifaces/network devices, allowing handling of admin up/down state ch...

**Definition** offloaded\_netdev.h:51

[wifi\_ap\_sta\_info](structwifi__ap__sta__info.md)

AP mode - connected STA details.

**Definition** wifi\_mgmt.h:635

[wifi\_ap\_sta\_info::mac](structwifi__ap__sta__info.md#a2a2fc109525e72ee7f18cced3b881107)

uint8\_t mac[6]

MAC address.

**Definition** wifi\_mgmt.h:639

[wifi\_ap\_sta\_info::link\_mode](structwifi__ap__sta__info.md#a7d8bd52340d4937a4b5b7d2c00662441)

enum wifi\_link\_mode link\_mode

Link mode, see enum wifi\_link\_mode.

**Definition** wifi\_mgmt.h:637

[wifi\_ap\_sta\_info::mac\_length](structwifi__ap__sta__info.md#a7f7c8b144bb3464af5213708591eefda)

uint8\_t mac\_length

MAC address length.

**Definition** wifi\_mgmt.h:641

[wifi\_ap\_sta\_info::twt\_capable](structwifi__ap__sta__info.md#a838c9a4288c9bc7e97afe2334c678f34)

bool twt\_capable

is TWT capable ?

**Definition** wifi\_mgmt.h:643

[wifi\_band\_channel](structwifi__band__channel.md)

Wi-Fi structure to uniquely identify a band-channel pair.

**Definition** wifi\_mgmt.h:257

[wifi\_band\_channel::band](structwifi__band__channel.md#a4a932599429f37231f76c3064ec5efb3)

uint8\_t band

Frequency band.

**Definition** wifi\_mgmt.h:259

[wifi\_band\_channel::channel](structwifi__band__channel.md#acd0dd7366de3650124dad7232a58ade0)

uint8\_t channel

Channel.

**Definition** wifi\_mgmt.h:261

[wifi\_channel\_info](structwifi__channel__info.md)

Wi-Fi channel setting for monitor and TX-injection modes.

**Definition** wifi\_mgmt.h:681

[wifi\_channel\_info::if\_index](structwifi__channel__info.md#a43a7dd8c19d0c6540e3cc0b5d1d6165d)

uint8\_t if\_index

Interface index.

**Definition** wifi\_mgmt.h:685

[wifi\_channel\_info::channel](structwifi__channel__info.md#a799cbc0a67764f6680322ba0f2ad3300)

uint16\_t channel

Channel value to set.

**Definition** wifi\_mgmt.h:683

[wifi\_channel\_info::oper](structwifi__channel__info.md#aa8ef8a71b49ead3664fff9a4d61b1ce8)

enum wifi\_mgmt\_op oper

Get or set operation.

**Definition** wifi\_mgmt.h:687

[wifi\_connect\_req\_params](structwifi__connect__req__params.md)

Wi-Fi connect request parameters.

**Definition** wifi\_mgmt.h:341

[wifi\_connect\_req\_params::security](structwifi__connect__req__params.md#a18dce6bb021086877a30e7a04f5b24b9)

enum wifi\_security\_type security

Security type.

**Definition** wifi\_mgmt.h:359

[wifi\_connect\_req\_params::sae\_password](structwifi__connect__req__params.md#a469fac5758b78fc425911837930b2060)

const uint8\_t \* sae\_password

SAE password (same as PSK but with no length restrictions), optional.

**Definition** wifi\_mgmt.h:351

[wifi\_connect\_req\_params::channel](structwifi__connect__req__params.md#a52b6d0323c35d03ec239f40be35cae72)

uint8\_t channel

Channel.

**Definition** wifi\_mgmt.h:357

[wifi\_connect\_req\_params::ssid\_length](structwifi__connect__req__params.md#a547dddf6be5dd77eda74b1085a798400)

uint8\_t ssid\_length

SSID length.

**Definition** wifi\_mgmt.h:345

[wifi\_connect\_req\_params::timeout](structwifi__connect__req__params.md#a56183ba7f4d8eaf5fc5b495856adecfd)

int timeout

Connect timeout in seconds, SYS\_FOREVER\_MS for no timeout.

**Definition** wifi\_mgmt.h:363

[wifi\_connect\_req\_params::mfp](structwifi__connect__req__params.md#a745b3416172672a7e5b12bcc5b55e88c)

enum wifi\_mfp\_options mfp

MFP options.

**Definition** wifi\_mgmt.h:361

[wifi\_connect\_req\_params::sae\_password\_length](structwifi__connect__req__params.md#a74f0819e7a546ffb8bfb0ec587eccf20)

uint8\_t sae\_password\_length

SAE password length.

**Definition** wifi\_mgmt.h:353

[wifi\_connect\_req\_params::band](structwifi__connect__req__params.md#aa2fea1881a8ffdf5d7093ae295867f3e)

uint8\_t band

Frequency band.

**Definition** wifi\_mgmt.h:355

[wifi\_connect\_req\_params::psk](structwifi__connect__req__params.md#aa7743f0ecbc27a9595720ce13ce57c1d)

const uint8\_t \* psk

Pre-shared key.

**Definition** wifi\_mgmt.h:347

[wifi\_connect\_req\_params::psk\_length](structwifi__connect__req__params.md#aaf7455a65590d19f047214b459a2dcb9)

uint8\_t psk\_length

Pre-shared key length.

**Definition** wifi\_mgmt.h:349

[wifi\_connect\_req\_params::ssid](structwifi__connect__req__params.md#ac260c2cd17a3f36ea101edaf23d41083)

const uint8\_t \* ssid

SSID.

**Definition** wifi\_mgmt.h:343

[wifi\_filter\_info](structwifi__filter__info.md)

Wi-Fi filter setting for monitor, prmoiscuous, TX-injection modes.

**Definition** wifi\_mgmt.h:669

[wifi\_filter\_info::buffer\_size](structwifi__filter__info.md#a1b2d0448fc7f62654e3f5aacfba62f8f)

uint16\_t buffer\_size

Filter buffer size.

**Definition** wifi\_mgmt.h:675

[wifi\_filter\_info::filter](structwifi__filter__info.md#ad9560be814299055cfa11b995a7dcf42)

uint8\_t filter

Filter setting.

**Definition** wifi\_mgmt.h:671

[wifi\_filter\_info::oper](structwifi__filter__info.md#aedd5e220cdde5768cb0f4aff920971cd)

enum wifi\_mgmt\_op oper

Get or set operation.

**Definition** wifi\_mgmt.h:677

[wifi\_filter\_info::if\_index](structwifi__filter__info.md#af9ea91e31e78afcb7ffe1ff9a04277a3)

uint8\_t if\_index

Interface index.

**Definition** wifi\_mgmt.h:673

[wifi\_iface\_status](structwifi__iface__status.md)

Wi-Fi interface status.

**Definition** wifi\_mgmt.h:429

[wifi\_iface\_status::beacon\_interval](structwifi__iface__status.md#a241bfbe70628006b515b5f9e4f97665c)

unsigned short beacon\_interval

Beacon interval.

**Definition** wifi\_mgmt.h:455

[wifi\_iface\_status::bssid](structwifi__iface__status.md#a28afad15fc6689669c7b19337a64eaf3)

char bssid[6]

BSSID.

**Definition** wifi\_mgmt.h:437

[wifi\_iface\_status::ssid](structwifi__iface__status.md#a30c4bef4e061346ba61857a558640d00)

char ssid[32]

SSID.

**Definition** wifi\_mgmt.h:435

[wifi\_iface\_status::rssi](structwifi__iface__status.md#a4e593147b88eb4938d55a4de72fcc7f6)

int rssi

RSSI.

**Definition** wifi\_mgmt.h:451

[wifi\_iface\_status::security](structwifi__iface__status.md#a625ecec1abec8dd65cf155eab21a01b5)

enum wifi\_security\_type security

Security type, see enum wifi\_security\_type.

**Definition** wifi\_mgmt.h:447

[wifi\_iface\_status::channel](structwifi__iface__status.md#a6432663156e5b2c424d254ed1eae0144)

unsigned int channel

Channel.

**Definition** wifi\_mgmt.h:441

[wifi\_iface\_status::mfp](structwifi__iface__status.md#aa1a9b644fd355526125ddd32416b7c24)

enum wifi\_mfp\_options mfp

MFP options, see enum wifi\_mfp\_options.

**Definition** wifi\_mgmt.h:449

[wifi\_iface\_status::dtim\_period](structwifi__iface__status.md#aae6c8cbaa16c81d308f08114d5103a3d)

unsigned char dtim\_period

DTIM period.

**Definition** wifi\_mgmt.h:453

[wifi\_iface\_status::state](structwifi__iface__status.md#ac52806155be3d64954ac6d109e76ec57)

int state

Interface state, see enum wifi\_iface\_state.

**Definition** wifi\_mgmt.h:431

[wifi\_iface\_status::twt\_capable](structwifi__iface__status.md#acfde8d64b463a9f553aa4fb689dc1917)

bool twt\_capable

is TWT capable?

**Definition** wifi\_mgmt.h:457

[wifi\_iface\_status::iface\_mode](structwifi__iface__status.md#ad33d2ec149a8d556e2472dd842ceadc0)

enum wifi\_iface\_mode iface\_mode

Interface mode, see enum wifi\_iface\_mode.

**Definition** wifi\_mgmt.h:443

[wifi\_iface\_status::ssid\_len](structwifi__iface__status.md#ad82f281941e4f6ce1ef0bca008e26d41)

unsigned int ssid\_len

SSID length.

**Definition** wifi\_mgmt.h:433

[wifi\_iface\_status::band](structwifi__iface__status.md#ae1c141a18f4e225af2c22a8cb4f882a8)

enum wifi\_frequency\_bands band

Frequency band.

**Definition** wifi\_mgmt.h:439

[wifi\_iface\_status::link\_mode](structwifi__iface__status.md#ae2de076d79f2172793d65fe9cd31edc4)

enum wifi\_link\_mode link\_mode

Link mode, see enum wifi\_link\_mode.

**Definition** wifi\_mgmt.h:445

[wifi\_mgmt\_ops](structwifi__mgmt__ops.md)

Wi-Fi management API.

**Definition** wifi\_mgmt.h:713

[wifi\_mgmt\_ops::reg\_domain](structwifi__mgmt__ops.md#a0a287c8acf2d7bf9333b755589294881)

int(\* reg\_domain)(const struct device \*dev, struct wifi\_reg\_domain \*reg\_domain)

Set or get regulatory domain.

**Definition** wifi\_mgmt.h:817

[wifi\_mgmt\_ops::scan](structwifi__mgmt__ops.md#a267030c27da3cdc251badd0ed7f7b1cb)

int(\* scan)(const struct device \*dev, struct wifi\_scan\_params \*params, scan\_result\_cb\_t cb)

Scan for Wi-Fi networks.

**Definition** wifi\_mgmt.h:725

[wifi\_mgmt\_ops::get\_power\_save\_config](structwifi__mgmt__ops.md#a52690b13f8a1e7b0c2302eaa24ae4c7f)

int(\* get\_power\_save\_config)(const struct device \*dev, struct wifi\_ps\_config \*config)

Get power save config.

**Definition** wifi\_mgmt.h:809

[wifi\_mgmt\_ops::disconnect](structwifi__mgmt__ops.md#a5725c6fd93ae189a3019374cd4ad2ff4)

int(\* disconnect)(const struct device \*dev)

Disconnect from a Wi-Fi network.

**Definition** wifi\_mgmt.h:743

[wifi\_mgmt\_ops::ap\_disable](structwifi__mgmt__ops.md#a5aa7a2be82eb1783872abda2b8978235)

int(\* ap\_disable)(const struct device \*dev)

Disable AP mode.

**Definition** wifi\_mgmt.h:759

[wifi\_mgmt\_ops::get\_stats](structwifi__mgmt__ops.md#a5e6fdf836273fcde54efff4c77bfdf0e)

int(\* get\_stats)(const struct device \*dev, struct net\_stats\_wifi \*stats)

Get Wi-Fi statistics.

**Definition** wifi\_mgmt.h:784

[wifi\_mgmt\_ops::get\_version](structwifi__mgmt__ops.md#aa7e4bc3dbc960091d11ffe5454259885)

int(\* get\_version)(const struct device \*dev, struct wifi\_version \*params)

Get Version of WiFi driver and Firmware.

**Definition** wifi\_mgmt.h:854

[wifi\_mgmt\_ops::set\_twt](structwifi__mgmt__ops.md#ab4500534b6abe0449290c8bd8f729fc4)

int(\* set\_twt)(const struct device \*dev, struct wifi\_twt\_params \*params)

Setup or teardown TWT flow.

**Definition** wifi\_mgmt.h:801

[wifi\_mgmt\_ops::set\_power\_save](structwifi__mgmt__ops.md#ac0f3f7fa699b1bc7db2358e77dd44cc4)

int(\* set\_power\_save)(const struct device \*dev, struct wifi\_ps\_params \*params)

Set power save status.

**Definition** wifi\_mgmt.h:793

[wifi\_mgmt\_ops::ap\_enable](structwifi__mgmt__ops.md#ac2ce3a4a86c43e30d33261f71c44198a)

int(\* ap\_enable)(const struct device \*dev, struct wifi\_connect\_req\_params \*params)

Enable AP mode.

**Definition** wifi\_mgmt.h:751

[wifi\_mgmt\_ops::filter](structwifi__mgmt__ops.md#ad645276745ce8dd9685e0744efdfc733)

int(\* filter)(const struct device \*dev, struct wifi\_filter\_info \*filter)

Set or get packet filter settings for monitor and promiscuous modes.

**Definition** wifi\_mgmt.h:825

[wifi\_mgmt\_ops::iface\_status](structwifi__mgmt__ops.md#adf157476d776bc9c068e99e1a0266fd3)

int(\* iface\_status)(const struct device \*dev, struct wifi\_iface\_status \*status)

Get interface status.

**Definition** wifi\_mgmt.h:775

[wifi\_mgmt\_ops::mode](structwifi__mgmt__ops.md#ae2fb1bc35bf9255655a30a2ad8588b7c)

int(\* mode)(const struct device \*dev, struct wifi\_mode\_info \*mode)

Set or get mode of operation.

**Definition** wifi\_mgmt.h:833

[wifi\_mgmt\_ops::connect](structwifi__mgmt__ops.md#ae6255ea77739918797b4f3c7a4634a75)

int(\* connect)(const struct device \*dev, struct wifi\_connect\_req\_params \*params)

Connect to a Wi-Fi network.

**Definition** wifi\_mgmt.h:735

[wifi\_mgmt\_ops::ap\_sta\_disconnect](structwifi__mgmt__ops.md#af01aaec29be78c02314acf13b5c1b6f7)

int(\* ap\_sta\_disconnect)(const struct device \*dev, const uint8\_t \*mac)

Disconnect a STA from AP.

**Definition** wifi\_mgmt.h:767

[wifi\_mgmt\_ops::channel](structwifi__mgmt__ops.md#af17ddfea01d0ab478f6fd50b1c9d6015)

int(\* channel)(const struct device \*dev, struct wifi\_channel\_info \*channel)

Set or get current channel of operation.

**Definition** wifi\_mgmt.h:841

[wifi\_mode\_info](structwifi__mode__info.md)

Wi-Fi mode setup.

**Definition** wifi\_mgmt.h:659

[wifi\_mode\_info::oper](structwifi__mode__info.md#a57c101db8b81ab0ac5dd0a158057a64a)

enum wifi\_mgmt\_op oper

Get or set operation.

**Definition** wifi\_mgmt.h:665

[wifi\_mode\_info::mode](structwifi__mode__info.md#aa29d3b88fc718aa3ac05daf38974707d)

uint8\_t mode

Mode setting for a specific mode of operation.

**Definition** wifi\_mgmt.h:661

[wifi\_mode\_info::if\_index](structwifi__mode__info.md#add58dd3b45fd2ddaf684d1b0de81bef9)

uint8\_t if\_index

Interface index.

**Definition** wifi\_mgmt.h:663

[wifi\_ps\_config](structwifi__ps__config.md)

Wi-Fi power save configuration.

**Definition** wifi\_mgmt.h:565

[wifi\_ps\_config::ps\_params](structwifi__ps__config.md#a357aafc2dedda37755b1cb1fc07fe5a6)

struct wifi\_ps\_params ps\_params

Power save configuration.

**Definition** wifi\_mgmt.h:571

[wifi\_ps\_config::num\_twt\_flows](structwifi__ps__config.md#a9e83c10eaaa1d721cbc49b40aedb00df)

char num\_twt\_flows

Number of TWT flows.

**Definition** wifi\_mgmt.h:567

[wifi\_ps\_config::twt\_flows](structwifi__ps__config.md#adcd3944ba1808eb214b522b72307832a)

struct wifi\_twt\_flow\_info twt\_flows[8]

TWT flow details.

**Definition** wifi\_mgmt.h:569

[wifi\_ps\_params](structwifi__ps__params.md)

Wi-Fi power save parameters.

**Definition** wifi\_mgmt.h:461

[wifi\_ps\_params::mode](structwifi__ps__params.md#a5a022d89d43ecf2cd1f15fc72c0f2bed)

enum wifi\_ps\_mode mode

Wi-Fi power save mode.

**Definition** wifi\_mgmt.h:469

[wifi\_ps\_params::fail\_reason](structwifi__ps__params.md#a63fa2ee03bc4aefada61c298ee14336c)

enum wifi\_config\_ps\_param\_fail\_reason fail\_reason

Wi-Fi power save fail reason.

**Definition** wifi\_mgmt.h:482

[wifi\_ps\_params::wakeup\_mode](structwifi__ps__params.md#a7cb3e7fb7d9f8bd7c2cab41f879b3b66)

enum wifi\_ps\_wakeup\_mode wakeup\_mode

Wi-Fi power save wakeup mode.

**Definition** wifi\_mgmt.h:467

[wifi\_ps\_params::listen\_interval](structwifi__ps__params.md#a8510c799ab0c5825f1c6349f9799c62f)

unsigned short listen\_interval

**Definition** wifi\_mgmt.h:465

[wifi\_ps\_params::enabled](structwifi__ps__params.md#abb22aaa45833ac130922204bd2fe841b)

enum wifi\_ps enabled

**Definition** wifi\_mgmt.h:463

[wifi\_ps\_params::timeout\_ms](structwifi__ps__params.md#ad963f1bf78dc271f08b73f3aadb36a91)

unsigned int timeout\_ms

Wi-Fi power save timeout.

**Definition** wifi\_mgmt.h:478

[wifi\_ps\_params::type](structwifi__ps__params.md#aef62e5bf6216bf4dc461efe71735c4bd)

enum wifi\_ps\_param\_type type

Wi-Fi power save type.

**Definition** wifi\_mgmt.h:480

[wifi\_raw\_scan\_result](structwifi__raw__scan__result.md)

Wi-Fi raw scan result.

**Definition** wifi\_mgmt.h:622

[wifi\_raw\_scan\_result::rssi](structwifi__raw__scan__result.md#a3f08580c6448a5fa28dd8a594fa7dad6)

int8\_t rssi

RSSI.

**Definition** wifi\_mgmt.h:624

[wifi\_raw\_scan\_result::data](structwifi__raw__scan__result.md#a5710e89199c147ce898602795f00aba3)

uint8\_t data[CONFIG\_WIFI\_MGMT\_RAW\_SCAN\_RESULT\_LENGTH]

Raw scan data.

**Definition** wifi\_mgmt.h:630

[wifi\_raw\_scan\_result::frame\_length](structwifi__raw__scan__result.md#a876966f469714eb481b42ccc8a63945c)

int frame\_length

Frame length.

**Definition** wifi\_mgmt.h:626

[wifi\_raw\_scan\_result::frequency](structwifi__raw__scan__result.md#aa2c7781882c6775616cbc8016b0842f6)

unsigned short frequency

Frequency.

**Definition** wifi\_mgmt.h:628

[wifi\_reg\_chan\_info](structwifi__reg__chan__info.md)

Per-channel regulatory attributes.

**Definition** wifi\_mgmt.h:585

[wifi\_reg\_chan\_info::center\_frequency](structwifi__reg__chan__info.md#a0addffc11ef29f50c01b700835e59930)

unsigned short center\_frequency

Center frequency in MHz.

**Definition** wifi\_mgmt.h:587

[wifi\_reg\_chan\_info::dfs](structwifi__reg__chan__info.md#a1ab137c142902d2de7d6be2626d7ac1f)

unsigned short dfs

Is a DFS channel.

**Definition** wifi\_mgmt.h:595

[wifi\_reg\_chan\_info::supported](structwifi__reg__chan__info.md#aa044611e18b7332b8577e29f6a769e3f)

unsigned short supported

Is channel supported or not.

**Definition** wifi\_mgmt.h:591

[wifi\_reg\_chan\_info::passive\_only](structwifi__reg__chan__info.md#acc7a88b004c9a61c8bf9ee1a97f85928)

unsigned short passive\_only

Passive transmissions only.

**Definition** wifi\_mgmt.h:593

[wifi\_reg\_chan\_info::max\_power](structwifi__reg__chan__info.md#af9169ab4a41fac4c6f6766fc96799545)

unsigned short max\_power

Maximum transmission power (in dBm).

**Definition** wifi\_mgmt.h:589

[wifi\_reg\_domain](structwifi__reg__domain.md)

Regulatory domain information or configuration.

**Definition** wifi\_mgmt.h:599

[wifi\_reg\_domain::num\_channels](structwifi__reg__domain.md#a3278e9f43893f49ab9f9d0d7f24009c1)

unsigned int num\_channels

Number of channels supported.

**Definition** wifi\_mgmt.h:607

[wifi\_reg\_domain::oper](structwifi__reg__domain.md#a3bbfdf1497a87bbb6b6211c7035e1002)

enum wifi\_mgmt\_op oper

**Definition** wifi\_mgmt.h:601

[wifi\_reg\_domain::chan\_info](structwifi__reg__domain.md#a4c8c9c11e41123cd7738fdb0d33ae5fb)

struct wifi\_reg\_chan\_info \* chan\_info

Channels information.

**Definition** wifi\_mgmt.h:609

[wifi\_reg\_domain::force](structwifi__reg__domain.md#a567c6fcae8032567aea83c18cd211c33)

bool force

Ignore all other regulatory hints over this one.

**Definition** wifi\_mgmt.h:603

[wifi\_reg\_domain::country\_code](structwifi__reg__domain.md#adfabbe25b049f0dd94c035a82c20a413)

uint8\_t country\_code[2]

Country code: ISO/IEC 3166-1 alpha-2.

**Definition** wifi\_mgmt.h:605

[wifi\_scan\_params](structwifi__scan__params.md)

Wi-Fi scan parameters structure.

**Definition** wifi\_mgmt.h:269

[wifi\_scan\_params::max\_bss\_cnt](structwifi__scan__params.md#a12d5dea7d8fa8ad03ac2366720c46243)

uint16\_t max\_bss\_cnt

Specifies the maximum number of scan results to return.

**Definition** wifi\_mgmt.h:298

[wifi\_scan\_params::dwell\_time\_active](structwifi__scan__params.md#a2453a75c23e04e3572559c0e7199c1b4)

uint16\_t dwell\_time\_active

Active scan dwell time (in ms) on a channel.

**Definition** wifi\_mgmt.h:284

[wifi\_scan\_params::scan\_type](structwifi__scan__params.md#a645acc54603cd4692527c1a028933078)

enum wifi\_scan\_type scan\_type

Scan type, see enum wifi\_scan\_type.

**Definition** wifi\_mgmt.h:277

[wifi\_scan\_params::bands](structwifi__scan__params.md#a6b571d960ed9d7419e31530e5fb6f97a)

uint8\_t bands

Bitmap of bands to be scanned.

**Definition** wifi\_mgmt.h:281

[wifi\_scan\_params::dwell\_time\_passive](structwifi__scan__params.md#a8e7a37ccda8de635e7b7066d7943e814)

uint16\_t dwell\_time\_passive

Passive scan dwell time (in ms) on a channel.

**Definition** wifi\_mgmt.h:287

[wifi\_scan\_params::ssids](structwifi__scan__params.md#abc1470c64b409db4785264e362b8c196)

const char \* ssids[1]

Array of SSID strings to scan.

**Definition** wifi\_mgmt.h:290

[wifi\_scan\_params::band\_chan](structwifi__scan__params.md#ac816cd67cc3141ebca5cd3acd052a003)

struct wifi\_band\_channel band\_chan[1]

Channel information array indexed on Wi-Fi frequency bands and channels within that band.

**Definition** wifi\_mgmt.h:313

[wifi\_scan\_result](structwifi__scan__result.md)

Wi-Fi scan result, each result is provided to the net\_mgmt\_event\_callback via its info attribute (see...

**Definition** wifi\_mgmt.h:319

[wifi\_scan\_result::ssid\_length](structwifi__scan__result.md#a2c1c2f4265b914df08fc75deb8b69d39)

uint8\_t ssid\_length

SSID length.

**Definition** wifi\_mgmt.h:323

[wifi\_scan\_result::band](structwifi__scan__result.md#a38201c9dd798dc11b5bda3ce97b02e92)

uint8\_t band

Frequency band.

**Definition** wifi\_mgmt.h:325

[wifi\_scan\_result::rssi](structwifi__scan__result.md#a76aa012136e3721fd4a482a22b93546f)

int8\_t rssi

RSSI.

**Definition** wifi\_mgmt.h:333

[wifi\_scan\_result::ssid](structwifi__scan__result.md#a854e296bdb2a54cb31e90a8f856be079)

uint8\_t ssid[32]

SSID.

**Definition** wifi\_mgmt.h:321

[wifi\_scan\_result::mac\_length](structwifi__scan__result.md#a8fca0dabec00ebd7ed4800098ec9d451)

uint8\_t mac\_length

BSSID length.

**Definition** wifi\_mgmt.h:337

[wifi\_scan\_result::mac](structwifi__scan__result.md#a906e9b48ebd5c0a599221f32cc47cda6)

uint8\_t mac[6]

BSSID.

**Definition** wifi\_mgmt.h:335

[wifi\_scan\_result::mfp](structwifi__scan__result.md#acaa3fb30ebf6df22bfac6380698ed28e)

enum wifi\_mfp\_options mfp

MFP options.

**Definition** wifi\_mgmt.h:331

[wifi\_scan\_result::channel](structwifi__scan__result.md#adbbfd7692ee5ffd6344fe78b9d91c840)

uint8\_t channel

Channel.

**Definition** wifi\_mgmt.h:327

[wifi\_scan\_result::security](structwifi__scan__result.md#af2d3dc5d115e3db76d3bc115510b0a5a)

enum wifi\_security\_type security

Security type.

**Definition** wifi\_mgmt.h:329

[wifi\_status](structwifi__status.md)

Generic Wi-Fi status for commands and events.

**Definition** wifi\_mgmt.h:419

[wifi\_status::ap\_status](structwifi__status.md#a02f0fcc7ef57661ca95d0c99f045aef1)

enum wifi\_ap\_status ap\_status

**Definition** wifi\_mgmt.h:424

[wifi\_status::conn\_status](structwifi__status.md#a8f885e78366d0499e4ba8e15bef275ac)

enum wifi\_conn\_status conn\_status

**Definition** wifi\_mgmt.h:422

[wifi\_status::disconn\_reason](structwifi__status.md#aa04b5033d93274badd27f702af9830bc)

enum wifi\_disconn\_reason disconn\_reason

**Definition** wifi\_mgmt.h:423

[wifi\_status::status](structwifi__status.md#aa1dbff8154400f8353693d387977008b)

int status

**Definition** wifi\_mgmt.h:421

[wifi\_twt\_flow\_info](structwifi__twt__flow__info.md)

Wi-Fi TWT flow information.

**Definition** wifi\_mgmt.h:541

[wifi\_twt\_flow\_info::dialog\_token](structwifi__twt__flow__info.md#a123ce10bed8b62b01919a7ea7644a0ba)

uint8\_t dialog\_token

Dialog token, used to map requests to responses.

**Definition** wifi\_mgmt.h:545

[wifi\_twt\_flow\_info::negotiation\_type](structwifi__twt__flow__info.md#a620ae8ba546e4091d74280cb1553b2cf)

enum wifi\_twt\_negotiation\_type negotiation\_type

TWT negotiation type, see enum wifi\_twt\_negotiation\_type.

**Definition** wifi\_mgmt.h:549

[wifi\_twt\_flow\_info::twt\_wake\_ahead\_duration](structwifi__twt__flow__info.md#a6384d3829d54a58a53eafcb74c64a658)

uint32\_t twt\_wake\_ahead\_duration

**Definition** wifi\_mgmt.h:561

[wifi\_twt\_flow\_info::trigger](structwifi__twt__flow__info.md#a952a67bd092c5dadba387bb13449c6f3)

bool trigger

Trigger enabled or disabled.

**Definition** wifi\_mgmt.h:553

[wifi\_twt\_flow\_info::responder](structwifi__twt__flow__info.md#ac82e4de8ffc82f851061f8ba8d217dc1)

bool responder

Requestor or responder.

**Definition** wifi\_mgmt.h:551

[wifi\_twt\_flow\_info::flow\_id](structwifi__twt__flow__info.md#acb0c618f1cebcb172f342cfe222683be)

uint8\_t flow\_id

Flow ID, used to map setup with teardown.

**Definition** wifi\_mgmt.h:547

[wifi\_twt\_flow\_info::twt\_interval](structwifi__twt__flow__info.md#ae15ba49fa54f82cc6a1fb0d4572114b7)

uint64\_t twt\_interval

Interval = Wake up time + Sleeping time.

**Definition** wifi\_mgmt.h:543

[wifi\_twt\_flow\_info::twt\_wake\_interval](structwifi__twt__flow__info.md#aede6cb0cfc999fac8ded49e2981a3762)

uint32\_t twt\_wake\_interval

Wake up time.

**Definition** wifi\_mgmt.h:559

[wifi\_twt\_flow\_info::implicit](structwifi__twt__flow__info.md#afb480be82d1c6f351bd634fd83bfa5c7)

bool implicit

Implicit or explicit.

**Definition** wifi\_mgmt.h:555

[wifi\_twt\_flow\_info::announce](structwifi__twt__flow__info.md#afc81a5111c265fd9bb2aca5f9510bfa8)

bool announce

Announced or unannounced.

**Definition** wifi\_mgmt.h:557

[wifi\_twt\_params](structwifi__twt__params.md)

Wi-Fi TWT parameters.

**Definition** wifi\_mgmt.h:486

[wifi\_twt\_params::announce](structwifi__twt__params.md#a02f2d822d530e5376f256503439a54f9)

bool announce

Announced or unannounced.

**Definition** wifi\_mgmt.h:513

[wifi\_twt\_params::teardown\_all](structwifi__twt__params.md#a26d6bda00452f77832f69f4465c13efb)

bool teardown\_all

Teardown all flows.

**Definition** wifi\_mgmt.h:526

[wifi\_twt\_params::setup\_cmd](structwifi__twt__params.md#a347f8cff73ee6b6ba6d15ddf6f376a2d)

enum wifi\_twt\_setup\_cmd setup\_cmd

TWT setup command, see enum wifi\_twt\_setup\_cmd.

**Definition** wifi\_mgmt.h:492

[wifi\_twt\_params::trigger](structwifi__twt__params.md#a4e822c04b52fe6a9489e48e26b8f9382)

bool trigger

Trigger enabled or disabled.

**Definition** wifi\_mgmt.h:509

[wifi\_twt\_params::negotiation\_type](structwifi__twt__params.md#a5fd269328f68838b8a7e3a0b93eed894)

enum wifi\_twt\_negotiation\_type negotiation\_type

TWT negotiation type, see enum wifi\_twt\_negotiation\_type.

**Definition** wifi\_mgmt.h:490

[wifi\_twt\_params::operation](structwifi__twt__params.md#a6f0483861a387651c9c89ba182e064bd)

enum wifi\_twt\_operation operation

TWT operation, see enum wifi\_twt\_operation.

**Definition** wifi\_mgmt.h:488

[wifi\_twt\_params::twt\_wake\_ahead\_duration](structwifi__twt__params.md#a6f907ca412251fdd7391f29bfa6d7713)

uint32\_t twt\_wake\_ahead\_duration

**Definition** wifi\_mgmt.h:521

[wifi\_twt\_params::fail\_reason](structwifi__twt__params.md#a70f58b502bb67ef3b2068ded2160b612)

enum wifi\_twt\_fail\_reason fail\_reason

TWT fail reason, see enum wifi\_twt\_fail\_reason.

**Definition** wifi\_mgmt.h:530

[wifi\_twt\_params::twt\_wake\_interval](structwifi__twt__params.md#a7c297459a17ed2fd232c62cca63e952f)

uint32\_t twt\_wake\_interval

Wake up time.

**Definition** wifi\_mgmt.h:515

[wifi\_twt\_params::resp\_status](structwifi__twt__params.md#a805a23284ed4afa46b84efcd43329beb)

enum wifi\_twt\_setup\_resp\_status resp\_status

TWT setup response status, see enum wifi\_twt\_setup\_resp\_status.

**Definition** wifi\_mgmt.h:494

[wifi\_twt\_params::implicit](structwifi__twt__params.md#a8ea1e2501c8b69dc3fa606eb360f8678)

bool implicit

Implicit or explicit.

**Definition** wifi\_mgmt.h:511

[wifi\_twt\_params::flow\_id](structwifi__twt__params.md#a95ec4b32d37309efa47256ae1ea865da)

uint8\_t flow\_id

Flow ID, used to map setup with teardown.

**Definition** wifi\_mgmt.h:500

[wifi\_twt\_params::teardown\_status](structwifi__twt__params.md#a9faff59e577775b3fe53f2139462ac71)

enum wifi\_twt\_teardown\_status teardown\_status

TWT teardown cmd status, see enum wifi\_twt\_teardown\_status.

**Definition** wifi\_mgmt.h:496

[wifi\_twt\_params::twt\_interval](structwifi__twt__params.md#ab92fe571559fcd5d97cdf7e6b7d86681)

uint64\_t twt\_interval

Interval = Wake up time + Sleeping time.

**Definition** wifi\_mgmt.h:505

[wifi\_twt\_params::dialog\_token](structwifi__twt__params.md#adda47e302a87a766f18e28016963a561)

uint8\_t dialog\_token

Dialog token, used to map requests to responses.

**Definition** wifi\_mgmt.h:498

[wifi\_twt\_params::responder](structwifi__twt__params.md#ae547c6fc1c7cbad15bebcfdaa43f59e7)

bool responder

Requestor or responder.

**Definition** wifi\_mgmt.h:507

[wifi\_twt\_params::setup](structwifi__twt__params.md#aee57c0189b210cfcc18e213e35b9479c)

struct wifi\_twt\_params::@302311362167322044106272253111230157111235232263::@007355023165260313375314073015252271352275036053 setup

Setup specific parameters.

[wifi\_twt\_params::teardown](structwifi__twt__params.md#afdeebd8a27107a0e37282aa19e5149d0)

struct wifi\_twt\_params::@302311362167322044106272253111230157111235232263::@053165077055023247316045052326043107125356150312 teardown

Teardown specific parameters.

[wifi\_version](structwifi__version.md)

Wi-Fi version.

**Definition** wifi\_mgmt.h:247

[wifi\_version::fw\_version](structwifi__version.md#a4bf2cbdf5c43ff21718ccf19646c164e)

const char \* fw\_version

Firmware version.

**Definition** wifi\_mgmt.h:251

[wifi\_version::drv\_version](structwifi__version.md#aea828bdb512440d6aa3cc853525c4971)

const char \* drv\_version

Driver version.

**Definition** wifi\_mgmt.h:249

[wifi\_mgmt\_events](unionwifi__mgmt__events.md)

**Definition** wifi\_mgmt.h:647

[wifi\_mgmt\_events::ap\_sta\_info](unionwifi__mgmt__events.md#a08c4882a4bbefc5fa82198cee2e3b344)

struct wifi\_ap\_sta\_info ap\_sta\_info

**Definition** wifi\_mgmt.h:655

[wifi\_mgmt\_events::iface\_status](unionwifi__mgmt__events.md#a8903faa173a9f3575625a0a68121958e)

struct wifi\_iface\_status iface\_status

**Definition** wifi\_mgmt.h:650

[wifi\_mgmt\_events::connect\_status](unionwifi__mgmt__events.md#ab85f83487dae9d5c59acfd56c34868ed)

struct wifi\_status connect\_status

**Definition** wifi\_mgmt.h:649

[wifi\_mgmt\_events::scan\_result](unionwifi__mgmt__events.md#ac531bb6de4e217a3f7ed6e073444c820)

struct wifi\_scan\_result scan\_result

**Definition** wifi\_mgmt.h:648

[wifi\_mgmt\_events::twt\_params](unionwifi__mgmt__events.md#ae38354f1e61e8b9286cfc71cb56ca339)

struct wifi\_twt\_params twt\_params

**Definition** wifi\_mgmt.h:654

[wifi.h](wifi_8h.md)

IEEE 802.11 protocol and general Wi-Fi definitions.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [wifi\_mgmt.h](wifi__mgmt_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
