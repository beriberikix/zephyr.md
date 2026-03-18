---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/wifi__mgmt_8h_source.html
original_path: doxygen/html/wifi__mgmt_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
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

32

33#define \_NET\_WIFI\_LAYER NET\_MGMT\_LAYER\_L2

34#define \_NET\_WIFI\_CODE 0x156

35#define \_NET\_WIFI\_BASE (NET\_MGMT\_IFACE\_BIT | \

36 NET\_MGMT\_LAYER(\_NET\_WIFI\_LAYER) | \

37 NET\_MGMT\_LAYER\_CODE(\_NET\_WIFI\_CODE))

38#define \_NET\_WIFI\_EVENT (\_NET\_WIFI\_BASE | NET\_MGMT\_EVENT\_BIT)

39

40#ifdef CONFIG\_WIFI\_MGMT\_SCAN\_SSID\_FILT\_MAX

41#define WIFI\_MGMT\_SCAN\_SSID\_FILT\_MAX CONFIG\_WIFI\_MGMT\_SCAN\_SSID\_FILT\_MAX

42#else

43#define WIFI\_MGMT\_SCAN\_SSID\_FILT\_MAX 1

44#endif /\* CONFIG\_WIFI\_MGMT\_SCAN\_SSID\_FILT\_MAX \*/

45

46#ifdef CONFIG\_WIFI\_MGMT\_SCAN\_CHAN\_MAX\_MANUAL

47#define WIFI\_MGMT\_SCAN\_CHAN\_MAX\_MANUAL CONFIG\_WIFI\_MGMT\_SCAN\_CHAN\_MAX\_MANUAL

48#else

49#define WIFI\_MGMT\_SCAN\_CHAN\_MAX\_MANUAL 1

50#endif /\* CONFIG\_WIFI\_MGMT\_SCAN\_CHAN\_MAX\_MANUAL \*/

51

52#define WIFI\_MGMT\_BAND\_STR\_SIZE\_MAX 8

53#define WIFI\_MGMT\_SCAN\_MAX\_BSS\_CNT 65535

54

55#define WIFI\_MGMT\_SKIP\_INACTIVITY\_POLL IS\_ENABLED(CONFIG\_WIFI\_MGMT\_AP\_STA\_SKIP\_INACTIVITY\_POLL)

57

[ 59](group__wifi__mgmt.md#ga99a55137188119f65f9d2bb4f57cac77)enum [net\_request\_wifi\_cmd](group__wifi__mgmt.md#ga99a55137188119f65f9d2bb4f57cac77) {

[ 61](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a4aadf9114010c09bd7420c99a2049d5a) [NET\_REQUEST\_WIFI\_CMD\_SCAN](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a4aadf9114010c09bd7420c99a2049d5a) = 1,

[ 63](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a78c958877ee60c90803c925b6b2f057a) [NET\_REQUEST\_WIFI\_CMD\_CONNECT](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a78c958877ee60c90803c925b6b2f057a),

[ 65](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77ac33941da138b993f7a1158d91469bcb7) [NET\_REQUEST\_WIFI\_CMD\_DISCONNECT](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77ac33941da138b993f7a1158d91469bcb7),

[ 67](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a28267d33b555433271cb121d62194a4c) [NET\_REQUEST\_WIFI\_CMD\_AP\_ENABLE](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a28267d33b555433271cb121d62194a4c),

[ 69](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a6fe9d7137b4cd20de880955b27382ccf) [NET\_REQUEST\_WIFI\_CMD\_AP\_DISABLE](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a6fe9d7137b4cd20de880955b27382ccf),

[ 71](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a6af9d52df8f9db6393044e42e10ff0de) [NET\_REQUEST\_WIFI\_CMD\_IFACE\_STATUS](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a6af9d52df8f9db6393044e42e10ff0de),

[ 73](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77abf9fb93c205fa36f74a9ef19d3d0351a) [NET\_REQUEST\_WIFI\_CMD\_PS](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77abf9fb93c205fa36f74a9ef19d3d0351a),

[ 75](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a1c9dc2d698326d987ffe5bfd35a9ed09) [NET\_REQUEST\_WIFI\_CMD\_TWT](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a1c9dc2d698326d987ffe5bfd35a9ed09),

[ 77](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77ae6ce1c605d1bf7c09650ec15d74e77e9) [NET\_REQUEST\_WIFI\_CMD\_PS\_CONFIG](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77ae6ce1c605d1bf7c09650ec15d74e77e9),

[ 79](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a367cc44caefd313e0c7ad3badc081456) [NET\_REQUEST\_WIFI\_CMD\_REG\_DOMAIN](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a367cc44caefd313e0c7ad3badc081456),

[ 81](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77ab7183584bdf5fe673d39fa0d090e3899) [NET\_REQUEST\_WIFI\_CMD\_MODE](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77ab7183584bdf5fe673d39fa0d090e3899),

[ 83](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a2579ace546bf6954c111eb5951e894f5) [NET\_REQUEST\_WIFI\_CMD\_PACKET\_FILTER](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a2579ace546bf6954c111eb5951e894f5),

[ 85](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77aade3d7a43c730a52f7876c6486170bb2) [NET\_REQUEST\_WIFI\_CMD\_CHANNEL](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77aade3d7a43c730a52f7876c6486170bb2),

[ 87](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a6f3865aa6a4d7633e241ee2b002c1b5a) [NET\_REQUEST\_WIFI\_CMD\_AP\_STA\_DISCONNECT](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a6f3865aa6a4d7633e241ee2b002c1b5a),

[ 89](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a7d9596f2cce54c9e050d89469e86eccb) [NET\_REQUEST\_WIFI\_CMD\_VERSION](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a7d9596f2cce54c9e050d89469e86eccb),

[ 91](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a7852cff28fc18ddd7af0f8224c840e7b) [NET\_REQUEST\_WIFI\_CMD\_RTS\_THRESHOLD](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a7852cff28fc18ddd7af0f8224c840e7b),

[ 93](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a14a0428720818c79df825d758e83f813) [NET\_REQUEST\_WIFI\_CMD\_AP\_CONFIG\_PARAM](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a14a0428720818c79df825d758e83f813),

95 NET\_REQUEST\_WIFI\_CMD\_MAX

97};

98

[ 100](group__wifi__mgmt.md#ga1c277da90986fa52dca182c4d922646f)#define NET\_REQUEST\_WIFI\_SCAN \

101 (\_NET\_WIFI\_BASE | NET\_REQUEST\_WIFI\_CMD\_SCAN)

102

103[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)([NET\_REQUEST\_WIFI\_SCAN](group__wifi__mgmt.md#ga1c277da90986fa52dca182c4d922646f));

104

[ 106](group__wifi__mgmt.md#gaa7ab2a97950a22736bb69f60b459f0f6)#define NET\_REQUEST\_WIFI\_CONNECT \

107 (\_NET\_WIFI\_BASE | NET\_REQUEST\_WIFI\_CMD\_CONNECT)

108

109[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)([NET\_REQUEST\_WIFI\_CONNECT](group__wifi__mgmt.md#gaa7ab2a97950a22736bb69f60b459f0f6));

110

[ 112](group__wifi__mgmt.md#ga90afd8d4e83056463ec6e667ed8ea60a)#define NET\_REQUEST\_WIFI\_DISCONNECT \

113 (\_NET\_WIFI\_BASE | NET\_REQUEST\_WIFI\_CMD\_DISCONNECT)

114

115[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)([NET\_REQUEST\_WIFI\_DISCONNECT](group__wifi__mgmt.md#ga90afd8d4e83056463ec6e667ed8ea60a));

116

[ 118](group__wifi__mgmt.md#ga638d2eb0a5029c1af46a91b523ed8589)#define NET\_REQUEST\_WIFI\_AP\_ENABLE \

119 (\_NET\_WIFI\_BASE | NET\_REQUEST\_WIFI\_CMD\_AP\_ENABLE)

120

121[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)([NET\_REQUEST\_WIFI\_AP\_ENABLE](group__wifi__mgmt.md#ga638d2eb0a5029c1af46a91b523ed8589));

122

[ 124](group__wifi__mgmt.md#gaf81f62bf4c9e331a095acbf0d24ca1a2)#define NET\_REQUEST\_WIFI\_AP\_DISABLE \

125 (\_NET\_WIFI\_BASE | NET\_REQUEST\_WIFI\_CMD\_AP\_DISABLE)

126

127[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)([NET\_REQUEST\_WIFI\_AP\_DISABLE](group__wifi__mgmt.md#gaf81f62bf4c9e331a095acbf0d24ca1a2));

128

[ 130](group__wifi__mgmt.md#ga3e45f6ee3801553619d8eb7d0af506eb)#define NET\_REQUEST\_WIFI\_IFACE\_STATUS \

131 (\_NET\_WIFI\_BASE | NET\_REQUEST\_WIFI\_CMD\_IFACE\_STATUS)

132

133[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)([NET\_REQUEST\_WIFI\_IFACE\_STATUS](group__wifi__mgmt.md#ga3e45f6ee3801553619d8eb7d0af506eb));

134

[ 136](group__wifi__mgmt.md#ga68aaced888f98e1ba4e6b61b53e5e2ba)#define NET\_REQUEST\_WIFI\_PS \

137 (\_NET\_WIFI\_BASE | NET\_REQUEST\_WIFI\_CMD\_PS)

138

139[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)([NET\_REQUEST\_WIFI\_PS](group__wifi__mgmt.md#ga68aaced888f98e1ba4e6b61b53e5e2ba));

140

[ 142](group__wifi__mgmt.md#gab84fd7e9ca0bf0b2b9d08889dda26aad)#define NET\_REQUEST\_WIFI\_TWT \

143 (\_NET\_WIFI\_BASE | NET\_REQUEST\_WIFI\_CMD\_TWT)

144

145[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)([NET\_REQUEST\_WIFI\_TWT](group__wifi__mgmt.md#gab84fd7e9ca0bf0b2b9d08889dda26aad));

146

[ 148](group__wifi__mgmt.md#ga1032f3773cfe6130da4d4d498b044ee2)#define NET\_REQUEST\_WIFI\_PS\_CONFIG \

149 (\_NET\_WIFI\_BASE | NET\_REQUEST\_WIFI\_CMD\_PS\_CONFIG)

150

151[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)([NET\_REQUEST\_WIFI\_PS\_CONFIG](group__wifi__mgmt.md#ga1032f3773cfe6130da4d4d498b044ee2));

152

[ 154](group__wifi__mgmt.md#ga2b27d102b779a6d846b375854768fb7f)#define NET\_REQUEST\_WIFI\_REG\_DOMAIN \

155 (\_NET\_WIFI\_BASE | NET\_REQUEST\_WIFI\_CMD\_REG\_DOMAIN)

156

157[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)([NET\_REQUEST\_WIFI\_REG\_DOMAIN](group__wifi__mgmt.md#ga2b27d102b779a6d846b375854768fb7f));

158

[ 160](group__wifi__mgmt.md#ga9b4da60a8108b0cc431ac1eecfca0cd0)#define NET\_REQUEST\_WIFI\_MODE \

161 (\_NET\_WIFI\_BASE | NET\_REQUEST\_WIFI\_CMD\_MODE)

162

163[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)([NET\_REQUEST\_WIFI\_MODE](group__wifi__mgmt.md#ga9b4da60a8108b0cc431ac1eecfca0cd0));

164

[ 166](group__wifi__mgmt.md#ga3098e817d12bf4619c9fd2698508fb4e)#define NET\_REQUEST\_WIFI\_PACKET\_FILTER \

167 (\_NET\_WIFI\_BASE | NET\_REQUEST\_WIFI\_CMD\_PACKET\_FILTER)

168

169[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)([NET\_REQUEST\_WIFI\_PACKET\_FILTER](group__wifi__mgmt.md#ga3098e817d12bf4619c9fd2698508fb4e));

170

[ 172](group__wifi__mgmt.md#gad9614d2368f8399850aaec05e40bdc78)#define NET\_REQUEST\_WIFI\_CHANNEL \

173 (\_NET\_WIFI\_BASE | NET\_REQUEST\_WIFI\_CMD\_CHANNEL)

174

175[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)([NET\_REQUEST\_WIFI\_CHANNEL](group__wifi__mgmt.md#gad9614d2368f8399850aaec05e40bdc78));

176

[ 178](group__wifi__mgmt.md#gaa3e52e08d89a1104f07207e52b81d503)#define NET\_REQUEST\_WIFI\_AP\_STA\_DISCONNECT \

179 (\_NET\_WIFI\_BASE | NET\_REQUEST\_WIFI\_CMD\_AP\_STA\_DISCONNECT)

180

181[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)([NET\_REQUEST\_WIFI\_AP\_STA\_DISCONNECT](group__wifi__mgmt.md#gaa3e52e08d89a1104f07207e52b81d503));

182

[ 184](group__wifi__mgmt.md#ga3e60c29ca9ce95d17a7fff087290f7f1)#define NET\_REQUEST\_WIFI\_VERSION \

185 (\_NET\_WIFI\_BASE | NET\_REQUEST\_WIFI\_CMD\_VERSION)

186

187[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)([NET\_REQUEST\_WIFI\_VERSION](group__wifi__mgmt.md#ga3e60c29ca9ce95d17a7fff087290f7f1));

188

[ 190](group__wifi__mgmt.md#ga22d80ef0ffb15e4286d7b1c3325d5334)#define NET\_REQUEST\_WIFI\_RTS\_THRESHOLD \

191 (\_NET\_WIFI\_BASE | NET\_REQUEST\_WIFI\_CMD\_RTS\_THRESHOLD)

192

193[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)([NET\_REQUEST\_WIFI\_RTS\_THRESHOLD](group__wifi__mgmt.md#ga22d80ef0ffb15e4286d7b1c3325d5334));

194

[ 196](group__wifi__mgmt.md#gaf4a78d230f5e0743a6aaf152ddda1c67)#define NET\_REQUEST\_WIFI\_AP\_CONFIG\_PARAM \

197 (\_NET\_WIFI\_BASE | NET\_REQUEST\_WIFI\_CMD\_AP\_CONFIG\_PARAM)

198

199[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)([NET\_REQUEST\_WIFI\_AP\_CONFIG\_PARAM](group__wifi__mgmt.md#gaf4a78d230f5e0743a6aaf152ddda1c67));

200

[ 202](group__wifi__mgmt.md#gac2638308cbb0d268831f1618cf8e1fa8)enum [net\_event\_wifi\_cmd](group__wifi__mgmt.md#gac2638308cbb0d268831f1618cf8e1fa8) {

[ 204](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8a37e9ab2a6832153fa968337d920e587e) [NET\_EVENT\_WIFI\_CMD\_SCAN\_RESULT](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8a37e9ab2a6832153fa968337d920e587e) = 1,

[ 206](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8ad753b7e4588257815f4a60a539ca2018) [NET\_EVENT\_WIFI\_CMD\_SCAN\_DONE](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8ad753b7e4588257815f4a60a539ca2018),

[ 208](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8af76f28777b91b365dc3f97028bc18e3c) [NET\_EVENT\_WIFI\_CMD\_CONNECT\_RESULT](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8af76f28777b91b365dc3f97028bc18e3c),

[ 210](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8a3a3b0387f83d8fb24a0e27312468b0eb) [NET\_EVENT\_WIFI\_CMD\_DISCONNECT\_RESULT](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8a3a3b0387f83d8fb24a0e27312468b0eb),

[ 212](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8af4b3f1969b96f63253851c26c3882a14) [NET\_EVENT\_WIFI\_CMD\_IFACE\_STATUS](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8af4b3f1969b96f63253851c26c3882a14),

[ 214](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8adad71603ed829ed92d06f8c40efa9b18) [NET\_EVENT\_WIFI\_CMD\_TWT](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8adad71603ed829ed92d06f8c40efa9b18),

[ 218](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8a78838bf7ce80cee5e803712cd0286750) [NET\_EVENT\_WIFI\_CMD\_TWT\_SLEEP\_STATE](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8a78838bf7ce80cee5e803712cd0286750),

[ 220](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8addf15c69512be7ab4957e7c0b3fde0ac) [NET\_EVENT\_WIFI\_CMD\_RAW\_SCAN\_RESULT](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8addf15c69512be7ab4957e7c0b3fde0ac),

[ 222](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8af1c42bd59f01260c64ede07da436c18f) [NET\_EVENT\_WIFI\_CMD\_DISCONNECT\_COMPLETE](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8af1c42bd59f01260c64ede07da436c18f),

[ 224](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8abd1797564427886eeb14dd293ae86a9b) [NET\_EVENT\_WIFI\_CMD\_AP\_ENABLE\_RESULT](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8abd1797564427886eeb14dd293ae86a9b),

[ 226](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8aeec3d7a9191280c2326034a17555308d) [NET\_EVENT\_WIFI\_CMD\_AP\_DISABLE\_RESULT](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8aeec3d7a9191280c2326034a17555308d),

[ 228](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8abd4269b2cd1302ce61da4f8d7bb9d5fb) [NET\_EVENT\_WIFI\_CMD\_AP\_STA\_CONNECTED](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8abd4269b2cd1302ce61da4f8d7bb9d5fb),

[ 230](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8a3678a39f9542968958b5575d571d4e2e) [NET\_EVENT\_WIFI\_CMD\_AP\_STA\_DISCONNECTED](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8a3678a39f9542968958b5575d571d4e2e),

231};

232

[ 234](group__wifi__mgmt.md#ga436a927d47eb9abe683b89f2b128cd6e)#define NET\_EVENT\_WIFI\_SCAN\_RESULT \

235 (\_NET\_WIFI\_EVENT | NET\_EVENT\_WIFI\_CMD\_SCAN\_RESULT)

236

[ 238](group__wifi__mgmt.md#ga8ce35a12e5338e9a65970382b4a26b88)#define NET\_EVENT\_WIFI\_SCAN\_DONE \

239 (\_NET\_WIFI\_EVENT | NET\_EVENT\_WIFI\_CMD\_SCAN\_DONE)

240

[ 242](group__wifi__mgmt.md#ga0e8feafcc5efd85d04be91f407c0b7c4)#define NET\_EVENT\_WIFI\_CONNECT\_RESULT \

243 (\_NET\_WIFI\_EVENT | NET\_EVENT\_WIFI\_CMD\_CONNECT\_RESULT)

244

[ 246](group__wifi__mgmt.md#ga8cbbe69bd60f42fdbb06f4f1e15410c8)#define NET\_EVENT\_WIFI\_DISCONNECT\_RESULT \

247 (\_NET\_WIFI\_EVENT | NET\_EVENT\_WIFI\_CMD\_DISCONNECT\_RESULT)

248

[ 250](group__wifi__mgmt.md#ga99e11fc15582b94d4243de7733e47ebb)#define NET\_EVENT\_WIFI\_IFACE\_STATUS \

251 (\_NET\_WIFI\_EVENT | NET\_EVENT\_WIFI\_CMD\_IFACE\_STATUS)

252

[ 254](group__wifi__mgmt.md#gaeb968a5d2a8d68a8c634cca18dbcf9c6)#define NET\_EVENT\_WIFI\_TWT \

255 (\_NET\_WIFI\_EVENT | NET\_EVENT\_WIFI\_CMD\_TWT)

256

[ 258](group__wifi__mgmt.md#ga682d95b5d06a9b175c10d712acca8a49)#define NET\_EVENT\_WIFI\_TWT\_SLEEP\_STATE \

259 (\_NET\_WIFI\_EVENT | NET\_EVENT\_WIFI\_CMD\_TWT\_SLEEP\_STATE)

260

[ 262](group__wifi__mgmt.md#gaea8d222282ddef6992330763afc759a4)#define NET\_EVENT\_WIFI\_RAW\_SCAN\_RESULT \

263 (\_NET\_WIFI\_EVENT | NET\_EVENT\_WIFI\_CMD\_RAW\_SCAN\_RESULT)

264

[ 266](group__wifi__mgmt.md#ga40027feb7ec42c846fd99b56bbd2256d)#define NET\_EVENT\_WIFI\_DISCONNECT\_COMPLETE \

267 (\_NET\_WIFI\_EVENT | NET\_EVENT\_WIFI\_CMD\_DISCONNECT\_COMPLETE)

268

[ 270](group__wifi__mgmt.md#ga1d678fbae0f092814392c0ab4087cb73)#define NET\_EVENT\_WIFI\_AP\_ENABLE\_RESULT \

271 (\_NET\_WIFI\_EVENT | NET\_EVENT\_WIFI\_CMD\_AP\_ENABLE\_RESULT)

272

[ 274](group__wifi__mgmt.md#ga104296fdb38edf868bea1a46f572d101)#define NET\_EVENT\_WIFI\_AP\_DISABLE\_RESULT \

275 (\_NET\_WIFI\_EVENT | NET\_EVENT\_WIFI\_CMD\_AP\_DISABLE\_RESULT)

276

[ 278](group__wifi__mgmt.md#gacc392179948bfd5bed6702dc8fb5cd9d)#define NET\_EVENT\_WIFI\_AP\_STA\_CONNECTED \

279 (\_NET\_WIFI\_EVENT | NET\_EVENT\_WIFI\_CMD\_AP\_STA\_CONNECTED)

280

[ 282](group__wifi__mgmt.md#ga3e8154ce1808665dd165f793ddec1673)#define NET\_EVENT\_WIFI\_AP\_STA\_DISCONNECTED \

283 (\_NET\_WIFI\_EVENT | NET\_EVENT\_WIFI\_CMD\_AP\_STA\_DISCONNECTED)

284

[ 286](structwifi__version.md)struct [wifi\_version](structwifi__version.md) {

[ 288](structwifi__version.md#aea828bdb512440d6aa3cc853525c4971) const char \*[drv\_version](structwifi__version.md#aea828bdb512440d6aa3cc853525c4971);

[ 290](structwifi__version.md#a4bf2cbdf5c43ff21718ccf19646c164e) const char \*[fw\_version](structwifi__version.md#a4bf2cbdf5c43ff21718ccf19646c164e);

291};

292

[ 296](structwifi__band__channel.md)struct [wifi\_band\_channel](structwifi__band__channel.md) {

[ 298](structwifi__band__channel.md#a4a932599429f37231f76c3064ec5efb3) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [band](structwifi__band__channel.md#a4a932599429f37231f76c3064ec5efb3);

[ 300](structwifi__band__channel.md#acd0dd7366de3650124dad7232a58ade0) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [channel](structwifi__band__channel.md#acd0dd7366de3650124dad7232a58ade0);

301};

302

[ 308](structwifi__scan__params.md)struct [wifi\_scan\_params](structwifi__scan__params.md) {

[ 316](structwifi__scan__params.md#a645acc54603cd4692527c1a028933078) enum [wifi\_scan\_type](group__wifi__mgmt.md#gad30e29eda65ccafdbd7f11865937b8ea) [scan\_type](structwifi__scan__params.md#a645acc54603cd4692527c1a028933078);

[ 320](structwifi__scan__params.md#a6b571d960ed9d7419e31530e5fb6f97a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bands](structwifi__scan__params.md#a6b571d960ed9d7419e31530e5fb6f97a);

[ 323](structwifi__scan__params.md#a2453a75c23e04e3572559c0e7199c1b4) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [dwell\_time\_active](structwifi__scan__params.md#a2453a75c23e04e3572559c0e7199c1b4);

[ 326](structwifi__scan__params.md#a8e7a37ccda8de635e7b7066d7943e814) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [dwell\_time\_passive](structwifi__scan__params.md#a8e7a37ccda8de635e7b7066d7943e814);

[ 329](structwifi__scan__params.md#aac11ee8e0ec8a4fa24668f4820bd1a12) const char \*[ssids](structwifi__scan__params.md#aac11ee8e0ec8a4fa24668f4820bd1a12)[WIFI\_MGMT\_SCAN\_SSID\_FILT\_MAX];

[ 337](structwifi__scan__params.md#a12d5dea7d8fa8ad03ac2366720c46243) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [max\_bss\_cnt](structwifi__scan__params.md#a12d5dea7d8fa8ad03ac2366720c46243);

[ 352](structwifi__scan__params.md#aa5ddbd6bc97b7598288d4b0d38521681) struct [wifi\_band\_channel](structwifi__band__channel.md) [band\_chan](structwifi__scan__params.md#aa5ddbd6bc97b7598288d4b0d38521681)[WIFI\_MGMT\_SCAN\_CHAN\_MAX\_MANUAL];

353};

354

[ 358](structwifi__scan__result.md)struct [wifi\_scan\_result](structwifi__scan__result.md) {

[ 360](structwifi__scan__result.md#a854e296bdb2a54cb31e90a8f856be079) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [ssid](structwifi__scan__result.md#a854e296bdb2a54cb31e90a8f856be079)[[WIFI\_SSID\_MAX\_LEN](group__wifi__mgmt.md#gad62c60666c9fdffe2e0e9c4388f87886)];

[ 362](structwifi__scan__result.md#a2c1c2f4265b914df08fc75deb8b69d39) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [ssid\_length](structwifi__scan__result.md#a2c1c2f4265b914df08fc75deb8b69d39);

[ 364](structwifi__scan__result.md#a38201c9dd798dc11b5bda3ce97b02e92) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [band](structwifi__scan__result.md#a38201c9dd798dc11b5bda3ce97b02e92);

[ 366](structwifi__scan__result.md#adbbfd7692ee5ffd6344fe78b9d91c840) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [channel](structwifi__scan__result.md#adbbfd7692ee5ffd6344fe78b9d91c840);

[ 368](structwifi__scan__result.md#af2d3dc5d115e3db76d3bc115510b0a5a) enum [wifi\_security\_type](group__wifi__mgmt.md#gadde31a04fa25ed805115c6b31854cd9c) [security](structwifi__scan__result.md#af2d3dc5d115e3db76d3bc115510b0a5a);

[ 370](structwifi__scan__result.md#acaa3fb30ebf6df22bfac6380698ed28e) enum [wifi\_mfp\_options](group__wifi__mgmt.md#ga1f252da47d9650023d7fff6d08e49c76) [mfp](structwifi__scan__result.md#acaa3fb30ebf6df22bfac6380698ed28e);

[ 372](structwifi__scan__result.md#a76aa012136e3721fd4a482a22b93546f) [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) [rssi](structwifi__scan__result.md#a76aa012136e3721fd4a482a22b93546f);

[ 374](structwifi__scan__result.md#a906e9b48ebd5c0a599221f32cc47cda6) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [mac](structwifi__scan__result.md#a906e9b48ebd5c0a599221f32cc47cda6)[[WIFI\_MAC\_ADDR\_LEN](group__wifi__mgmt.md#ga29409ff83a53c6464decdde9bdd04de6)];

[ 376](structwifi__scan__result.md#a8fca0dabec00ebd7ed4800098ec9d451) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [mac\_length](structwifi__scan__result.md#a8fca0dabec00ebd7ed4800098ec9d451);

377};

378

[ 380](structwifi__connect__req__params.md)struct [wifi\_connect\_req\_params](structwifi__connect__req__params.md) {

[ 382](structwifi__connect__req__params.md#ac260c2cd17a3f36ea101edaf23d41083) const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[ssid](structwifi__connect__req__params.md#ac260c2cd17a3f36ea101edaf23d41083);

[ 384](structwifi__connect__req__params.md#a547dddf6be5dd77eda74b1085a798400) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [ssid\_length](structwifi__connect__req__params.md#a547dddf6be5dd77eda74b1085a798400); /\* Max 32 \*/

[ 386](structwifi__connect__req__params.md#aa7743f0ecbc27a9595720ce13ce57c1d) const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[psk](structwifi__connect__req__params.md#aa7743f0ecbc27a9595720ce13ce57c1d);

[ 388](structwifi__connect__req__params.md#aaf7455a65590d19f047214b459a2dcb9) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [psk\_length](structwifi__connect__req__params.md#aaf7455a65590d19f047214b459a2dcb9); /\* Min 8 - Max 64 \*/

[ 390](structwifi__connect__req__params.md#a469fac5758b78fc425911837930b2060) const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[sae\_password](structwifi__connect__req__params.md#a469fac5758b78fc425911837930b2060);

[ 392](structwifi__connect__req__params.md#a74f0819e7a546ffb8bfb0ec587eccf20) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [sae\_password\_length](structwifi__connect__req__params.md#a74f0819e7a546ffb8bfb0ec587eccf20); /\* No length restrictions \*/

[ 394](structwifi__connect__req__params.md#aa2fea1881a8ffdf5d7093ae295867f3e) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [band](structwifi__connect__req__params.md#aa2fea1881a8ffdf5d7093ae295867f3e);

[ 396](structwifi__connect__req__params.md#a52b6d0323c35d03ec239f40be35cae72) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [channel](structwifi__connect__req__params.md#a52b6d0323c35d03ec239f40be35cae72);

[ 398](structwifi__connect__req__params.md#a18dce6bb021086877a30e7a04f5b24b9) enum [wifi\_security\_type](group__wifi__mgmt.md#gadde31a04fa25ed805115c6b31854cd9c) [security](structwifi__connect__req__params.md#a18dce6bb021086877a30e7a04f5b24b9);

[ 400](structwifi__connect__req__params.md#a745b3416172672a7e5b12bcc5b55e88c) enum [wifi\_mfp\_options](group__wifi__mgmt.md#ga1f252da47d9650023d7fff6d08e49c76) [mfp](structwifi__connect__req__params.md#a745b3416172672a7e5b12bcc5b55e88c);

[ 402](structwifi__connect__req__params.md#a4d2356cf5eb3bbd51587ec5f3a1a065c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bssid](structwifi__connect__req__params.md#a4d2356cf5eb3bbd51587ec5f3a1a065c)[[WIFI\_MAC\_ADDR\_LEN](group__wifi__mgmt.md#ga29409ff83a53c6464decdde9bdd04de6)];

[ 404](structwifi__connect__req__params.md#a56183ba7f4d8eaf5fc5b495856adecfd) int [timeout](structwifi__connect__req__params.md#a56183ba7f4d8eaf5fc5b495856adecfd);

405};

406

[ 410](group__wifi__mgmt.md#ga86a5741e54aeb3e290142b0de217b8a8)enum [wifi\_conn\_status](group__wifi__mgmt.md#ga86a5741e54aeb3e290142b0de217b8a8) {

[ 412](group__wifi__mgmt.md#gga86a5741e54aeb3e290142b0de217b8a8a380410b02b1e12599f37d1dcb844f5bd) [WIFI\_STATUS\_CONN\_SUCCESS](group__wifi__mgmt.md#gga86a5741e54aeb3e290142b0de217b8a8a380410b02b1e12599f37d1dcb844f5bd) = 0,

[ 414](group__wifi__mgmt.md#gga86a5741e54aeb3e290142b0de217b8a8ab80ec4b70c75695fbe698034e2cb6a44) [WIFI\_STATUS\_CONN\_FAIL](group__wifi__mgmt.md#gga86a5741e54aeb3e290142b0de217b8a8ab80ec4b70c75695fbe698034e2cb6a44),

[ 423](group__wifi__mgmt.md#gga86a5741e54aeb3e290142b0de217b8a8a90d91f96a35c9f6847cbc7abd8c20bf8) [WIFI\_STATUS\_CONN\_WRONG\_PASSWORD](group__wifi__mgmt.md#gga86a5741e54aeb3e290142b0de217b8a8a90d91f96a35c9f6847cbc7abd8c20bf8),

[ 425](group__wifi__mgmt.md#gga86a5741e54aeb3e290142b0de217b8a8abb8783b92aec2ed1ffc6331979888563) [WIFI\_STATUS\_CONN\_TIMEOUT](group__wifi__mgmt.md#gga86a5741e54aeb3e290142b0de217b8a8abb8783b92aec2ed1ffc6331979888563),

[ 427](group__wifi__mgmt.md#gga86a5741e54aeb3e290142b0de217b8a8a2ae79fa389bb447fa108e0107aeff2f4) [WIFI\_STATUS\_CONN\_AP\_NOT\_FOUND](group__wifi__mgmt.md#gga86a5741e54aeb3e290142b0de217b8a8a2ae79fa389bb447fa108e0107aeff2f4),

[ 429](group__wifi__mgmt.md#gga86a5741e54aeb3e290142b0de217b8a8aeee5fb8d8c3e7905554d08331f06191f) [WIFI\_STATUS\_CONN\_LAST\_STATUS](group__wifi__mgmt.md#gga86a5741e54aeb3e290142b0de217b8a8aeee5fb8d8c3e7905554d08331f06191f),

[ 431](group__wifi__mgmt.md#gga86a5741e54aeb3e290142b0de217b8a8abe1401e5d516c0d63291add15e558b18) [WIFI\_STATUS\_DISCONN\_FIRST\_STATUS](group__wifi__mgmt.md#gga86a5741e54aeb3e290142b0de217b8a8abe1401e5d516c0d63291add15e558b18) = [WIFI\_STATUS\_CONN\_LAST\_STATUS](group__wifi__mgmt.md#gga86a5741e54aeb3e290142b0de217b8a8aeee5fb8d8c3e7905554d08331f06191f),

432};

433

[ 437](group__wifi__mgmt.md#gac782af0a60b202fd19597cabb7bd3a9a)enum [wifi\_disconn\_reason](group__wifi__mgmt.md#gac782af0a60b202fd19597cabb7bd3a9a) {

[ 439](group__wifi__mgmt.md#ggac782af0a60b202fd19597cabb7bd3a9aa5c894399db8949a789ca4f5750b6f042) [WIFI\_REASON\_DISCONN\_SUCCESS](group__wifi__mgmt.md#ggac782af0a60b202fd19597cabb7bd3a9aa5c894399db8949a789ca4f5750b6f042) = 0,

[ 441](group__wifi__mgmt.md#ggac782af0a60b202fd19597cabb7bd3a9aa87f5d64a9fd3acf8d67c698199779e5c) [WIFI\_REASON\_DISCONN\_UNSPECIFIED](group__wifi__mgmt.md#ggac782af0a60b202fd19597cabb7bd3a9aa87f5d64a9fd3acf8d67c698199779e5c),

[ 443](group__wifi__mgmt.md#ggac782af0a60b202fd19597cabb7bd3a9aaee75adafb52bd6ecaa547a76c6ccd0a7) [WIFI\_REASON\_DISCONN\_USER\_REQUEST](group__wifi__mgmt.md#ggac782af0a60b202fd19597cabb7bd3a9aaee75adafb52bd6ecaa547a76c6ccd0a7),

[ 445](group__wifi__mgmt.md#ggac782af0a60b202fd19597cabb7bd3a9aa34e3f78ce43db3daeaf32038e0baf204) [WIFI\_REASON\_DISCONN\_AP\_LEAVING](group__wifi__mgmt.md#ggac782af0a60b202fd19597cabb7bd3a9aa34e3f78ce43db3daeaf32038e0baf204),

[ 447](group__wifi__mgmt.md#ggac782af0a60b202fd19597cabb7bd3a9aa05fe2f87de30de47ee48f7615c2206e6) [WIFI\_REASON\_DISCONN\_INACTIVITY](group__wifi__mgmt.md#ggac782af0a60b202fd19597cabb7bd3a9aa05fe2f87de30de47ee48f7615c2206e6),

448};

449

[ 453](group__wifi__mgmt.md#gaaf730bf76adc06434c7ac63bf0417884)enum [wifi\_ap\_status](group__wifi__mgmt.md#gaaf730bf76adc06434c7ac63bf0417884) {

[ 455](group__wifi__mgmt.md#ggaaf730bf76adc06434c7ac63bf0417884a0df52848da8735892d0eb1e381b2cd7c) [WIFI\_STATUS\_AP\_SUCCESS](group__wifi__mgmt.md#ggaaf730bf76adc06434c7ac63bf0417884a0df52848da8735892d0eb1e381b2cd7c) = 0,

[ 457](group__wifi__mgmt.md#ggaaf730bf76adc06434c7ac63bf0417884a6c6801381caa3862004662169202fa9a) [WIFI\_STATUS\_AP\_FAIL](group__wifi__mgmt.md#ggaaf730bf76adc06434c7ac63bf0417884a6c6801381caa3862004662169202fa9a),

[ 459](group__wifi__mgmt.md#ggaaf730bf76adc06434c7ac63bf0417884a5acb85a2361ca72ed10966b829c5753b) [WIFI\_STATUS\_AP\_CHANNEL\_NOT\_SUPPORTED](group__wifi__mgmt.md#ggaaf730bf76adc06434c7ac63bf0417884a5acb85a2361ca72ed10966b829c5753b),

[ 461](group__wifi__mgmt.md#ggaaf730bf76adc06434c7ac63bf0417884a0b1cb592c54c16e8a54defee71c5fd15) [WIFI\_STATUS\_AP\_CHANNEL\_NOT\_ALLOWED](group__wifi__mgmt.md#ggaaf730bf76adc06434c7ac63bf0417884a0b1cb592c54c16e8a54defee71c5fd15),

[ 463](group__wifi__mgmt.md#ggaaf730bf76adc06434c7ac63bf0417884ac18a7b551f8c6bb7737b0e8e60c323ce) [WIFI\_STATUS\_AP\_SSID\_NOT\_ALLOWED](group__wifi__mgmt.md#ggaaf730bf76adc06434c7ac63bf0417884ac18a7b551f8c6bb7737b0e8e60c323ce),

[ 465](group__wifi__mgmt.md#ggaaf730bf76adc06434c7ac63bf0417884abe5a626d22051522255d98fdfdfbfcc8) [WIFI\_STATUS\_AP\_AUTH\_TYPE\_NOT\_SUPPORTED](group__wifi__mgmt.md#ggaaf730bf76adc06434c7ac63bf0417884abe5a626d22051522255d98fdfdfbfcc8),

[ 467](group__wifi__mgmt.md#ggaaf730bf76adc06434c7ac63bf0417884a2105e6c49b3bcb5f7dcacbc1e5ce9cca) [WIFI\_STATUS\_AP\_OP\_NOT\_SUPPORTED](group__wifi__mgmt.md#ggaaf730bf76adc06434c7ac63bf0417884a2105e6c49b3bcb5f7dcacbc1e5ce9cca),

[ 469](group__wifi__mgmt.md#ggaaf730bf76adc06434c7ac63bf0417884a36a58980bdc7877c910441590137ddbe) [WIFI\_STATUS\_AP\_OP\_NOT\_PERMITTED](group__wifi__mgmt.md#ggaaf730bf76adc06434c7ac63bf0417884a36a58980bdc7877c910441590137ddbe),

470};

471

[ 473](structwifi__status.md)struct [wifi\_status](structwifi__status.md) {

474 union {

[ 476](structwifi__status.md#aa1dbff8154400f8353693d387977008b) int [status](structwifi__status.md#aa1dbff8154400f8353693d387977008b);

[ 478](structwifi__status.md#a8f885e78366d0499e4ba8e15bef275ac) enum [wifi\_conn\_status](group__wifi__mgmt.md#ga86a5741e54aeb3e290142b0de217b8a8) [conn\_status](structwifi__status.md#a8f885e78366d0499e4ba8e15bef275ac);

[ 480](structwifi__status.md#aa04b5033d93274badd27f702af9830bc) enum [wifi\_disconn\_reason](group__wifi__mgmt.md#gac782af0a60b202fd19597cabb7bd3a9a) [disconn\_reason](structwifi__status.md#aa04b5033d93274badd27f702af9830bc);

[ 482](structwifi__status.md#a02f0fcc7ef57661ca95d0c99f045aef1) enum [wifi\_ap\_status](group__wifi__mgmt.md#gaaf730bf76adc06434c7ac63bf0417884) [ap\_status](structwifi__status.md#a02f0fcc7ef57661ca95d0c99f045aef1);

483 };

484};

485

[ 487](structwifi__iface__status.md)struct [wifi\_iface\_status](structwifi__iface__status.md) {

[ 489](structwifi__iface__status.md#ac52806155be3d64954ac6d109e76ec57) int [state](structwifi__iface__status.md#ac52806155be3d64954ac6d109e76ec57);

[ 491](structwifi__iface__status.md#ad82f281941e4f6ce1ef0bca008e26d41) unsigned int [ssid\_len](structwifi__iface__status.md#ad82f281941e4f6ce1ef0bca008e26d41);

[ 493](structwifi__iface__status.md#a30c4bef4e061346ba61857a558640d00) char [ssid](structwifi__iface__status.md#a30c4bef4e061346ba61857a558640d00)[[WIFI\_SSID\_MAX\_LEN](group__wifi__mgmt.md#gad62c60666c9fdffe2e0e9c4388f87886)];

[ 495](structwifi__iface__status.md#a28afad15fc6689669c7b19337a64eaf3) char [bssid](structwifi__iface__status.md#a28afad15fc6689669c7b19337a64eaf3)[[WIFI\_MAC\_ADDR\_LEN](group__wifi__mgmt.md#ga29409ff83a53c6464decdde9bdd04de6)];

[ 497](structwifi__iface__status.md#ae1c141a18f4e225af2c22a8cb4f882a8) enum [wifi\_frequency\_bands](group__wifi__mgmt.md#ga1e2f0439a322355fa7368ea880c9c15d) [band](structwifi__iface__status.md#ae1c141a18f4e225af2c22a8cb4f882a8);

[ 499](structwifi__iface__status.md#a6432663156e5b2c424d254ed1eae0144) unsigned int [channel](structwifi__iface__status.md#a6432663156e5b2c424d254ed1eae0144);

[ 501](structwifi__iface__status.md#ad33d2ec149a8d556e2472dd842ceadc0) enum [wifi\_iface\_mode](group__wifi__mgmt.md#ga584f6239ac14e2bedc5e6bd72756423b) [iface\_mode](structwifi__iface__status.md#ad33d2ec149a8d556e2472dd842ceadc0);

[ 503](structwifi__iface__status.md#ae2de076d79f2172793d65fe9cd31edc4) enum [wifi\_link\_mode](group__wifi__mgmt.md#gabdb2a784d4727b71ab44cca04e422c62) [link\_mode](structwifi__iface__status.md#ae2de076d79f2172793d65fe9cd31edc4);

[ 505](structwifi__iface__status.md#a625ecec1abec8dd65cf155eab21a01b5) enum [wifi\_security\_type](group__wifi__mgmt.md#gadde31a04fa25ed805115c6b31854cd9c) [security](structwifi__iface__status.md#a625ecec1abec8dd65cf155eab21a01b5);

[ 507](structwifi__iface__status.md#aa1a9b644fd355526125ddd32416b7c24) enum [wifi\_mfp\_options](group__wifi__mgmt.md#ga1f252da47d9650023d7fff6d08e49c76) [mfp](structwifi__iface__status.md#aa1a9b644fd355526125ddd32416b7c24);

[ 509](structwifi__iface__status.md#a4e593147b88eb4938d55a4de72fcc7f6) int [rssi](structwifi__iface__status.md#a4e593147b88eb4938d55a4de72fcc7f6);

[ 511](structwifi__iface__status.md#aae6c8cbaa16c81d308f08114d5103a3d) unsigned char [dtim\_period](structwifi__iface__status.md#aae6c8cbaa16c81d308f08114d5103a3d);

[ 513](structwifi__iface__status.md#a241bfbe70628006b515b5f9e4f97665c) unsigned short [beacon\_interval](structwifi__iface__status.md#a241bfbe70628006b515b5f9e4f97665c);

[ 515](structwifi__iface__status.md#acfde8d64b463a9f553aa4fb689dc1917) bool [twt\_capable](structwifi__iface__status.md#acfde8d64b463a9f553aa4fb689dc1917);

516};

517

[ 519](structwifi__ps__params.md)struct [wifi\_ps\_params](structwifi__ps__params.md) {

[ 521](structwifi__ps__params.md#abb22aaa45833ac130922204bd2fe841b) enum [wifi\_ps](group__wifi__mgmt.md#ga0fffeb57b68fb8cdef9d3d571368b8ca) [enabled](structwifi__ps__params.md#abb22aaa45833ac130922204bd2fe841b);

[ 523](structwifi__ps__params.md#a8510c799ab0c5825f1c6349f9799c62f) unsigned short [listen\_interval](structwifi__ps__params.md#a8510c799ab0c5825f1c6349f9799c62f);

[ 525](structwifi__ps__params.md#a7cb3e7fb7d9f8bd7c2cab41f879b3b66) enum [wifi\_ps\_wakeup\_mode](group__wifi__mgmt.md#gac7f907644847e905d67c709fa4afae7f) [wakeup\_mode](structwifi__ps__params.md#a7cb3e7fb7d9f8bd7c2cab41f879b3b66);

[ 527](structwifi__ps__params.md#a5a022d89d43ecf2cd1f15fc72c0f2bed) enum [wifi\_ps\_mode](group__wifi__mgmt.md#gaffae7d2a754be5eb952ad2b83edad54c) [mode](structwifi__ps__params.md#a5a022d89d43ecf2cd1f15fc72c0f2bed);

[ 536](structwifi__ps__params.md#ad963f1bf78dc271f08b73f3aadb36a91) unsigned int [timeout\_ms](structwifi__ps__params.md#ad963f1bf78dc271f08b73f3aadb36a91);

[ 538](structwifi__ps__params.md#aef62e5bf6216bf4dc461efe71735c4bd) enum [wifi\_ps\_param\_type](group__wifi__mgmt.md#gabe45d132797047c098041331c8f6f912) [type](structwifi__ps__params.md#aef62e5bf6216bf4dc461efe71735c4bd);

[ 540](structwifi__ps__params.md#a63fa2ee03bc4aefada61c298ee14336c) enum [wifi\_config\_ps\_param\_fail\_reason](group__wifi__mgmt.md#gad98099584d2222ede93aba42b1fbaff0) [fail\_reason](structwifi__ps__params.md#a63fa2ee03bc4aefada61c298ee14336c);

541};

542

[ 544](structwifi__twt__params.md)struct [wifi\_twt\_params](structwifi__twt__params.md) {

[ 546](structwifi__twt__params.md#a6f0483861a387651c9c89ba182e064bd) enum [wifi\_twt\_operation](group__wifi__mgmt.md#gad0e998aeb1b27c4f203ca76339d323a3) [operation](structwifi__twt__params.md#a6f0483861a387651c9c89ba182e064bd);

[ 548](structwifi__twt__params.md#a5fd269328f68838b8a7e3a0b93eed894) enum [wifi\_twt\_negotiation\_type](group__wifi__mgmt.md#ga695123cd534e2499f516a07fdc5cafa8) [negotiation\_type](structwifi__twt__params.md#a5fd269328f68838b8a7e3a0b93eed894);

[ 550](structwifi__twt__params.md#a347f8cff73ee6b6ba6d15ddf6f376a2d) enum [wifi\_twt\_setup\_cmd](group__wifi__mgmt.md#ga31c78afc89bfdc4b54cee177843f8022) [setup\_cmd](structwifi__twt__params.md#a347f8cff73ee6b6ba6d15ddf6f376a2d);

[ 552](structwifi__twt__params.md#a805a23284ed4afa46b84efcd43329beb) enum [wifi\_twt\_setup\_resp\_status](group__wifi__mgmt.md#ga4d03aedac13ee4512d7717ac624f319a) [resp\_status](structwifi__twt__params.md#a805a23284ed4afa46b84efcd43329beb);

[ 554](structwifi__twt__params.md#a9faff59e577775b3fe53f2139462ac71) enum [wifi\_twt\_teardown\_status](group__wifi__mgmt.md#gad3709d07aaa3ed59b48f9dd7bd181989) [teardown\_status](structwifi__twt__params.md#a9faff59e577775b3fe53f2139462ac71);

[ 556](structwifi__twt__params.md#adda47e302a87a766f18e28016963a561) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [dialog\_token](structwifi__twt__params.md#adda47e302a87a766f18e28016963a561);

[ 558](structwifi__twt__params.md#a95ec4b32d37309efa47256ae1ea865da) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [flow\_id](structwifi__twt__params.md#a95ec4b32d37309efa47256ae1ea865da);

559 union {

561 struct {

[ 563](structwifi__twt__params.md#ab92fe571559fcd5d97cdf7e6b7d86681) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [twt\_interval](structwifi__twt__params.md#ab92fe571559fcd5d97cdf7e6b7d86681);

[ 565](structwifi__twt__params.md#ae547c6fc1c7cbad15bebcfdaa43f59e7) bool [responder](structwifi__twt__params.md#ae547c6fc1c7cbad15bebcfdaa43f59e7);

[ 567](structwifi__twt__params.md#a4e822c04b52fe6a9489e48e26b8f9382) bool [trigger](structwifi__twt__params.md#a4e822c04b52fe6a9489e48e26b8f9382);

[ 569](structwifi__twt__params.md#a8ea1e2501c8b69dc3fa606eb360f8678) bool [implicit](structwifi__twt__params.md#a8ea1e2501c8b69dc3fa606eb360f8678);

[ 571](structwifi__twt__params.md#a02f2d822d530e5376f256503439a54f9) bool [announce](structwifi__twt__params.md#a02f2d822d530e5376f256503439a54f9);

[ 573](structwifi__twt__params.md#a7c297459a17ed2fd232c62cca63e952f) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [twt\_wake\_interval](structwifi__twt__params.md#a7c297459a17ed2fd232c62cca63e952f);

[ 579](structwifi__twt__params.md#a6f907ca412251fdd7391f29bfa6d7713) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [twt\_wake\_ahead\_duration](structwifi__twt__params.md#a6f907ca412251fdd7391f29bfa6d7713);

[ 580](structwifi__twt__params.md#aee57c0189b210cfcc18e213e35b9479c) } [setup](structwifi__twt__params.md#aee57c0189b210cfcc18e213e35b9479c);

582 struct {

[ 584](structwifi__twt__params.md#a26d6bda00452f77832f69f4465c13efb) bool [teardown\_all](structwifi__twt__params.md#a26d6bda00452f77832f69f4465c13efb);

[ 585](structwifi__twt__params.md#afdeebd8a27107a0e37282aa19e5149d0) } [teardown](structwifi__twt__params.md#afdeebd8a27107a0e37282aa19e5149d0);

586 };

[ 588](structwifi__twt__params.md#a70f58b502bb67ef3b2068ded2160b612) enum [wifi\_twt\_fail\_reason](group__wifi__mgmt.md#ga97fa304f9a1db2294a93cccd4c93bcf6) [fail\_reason](structwifi__twt__params.md#a70f58b502bb67ef3b2068ded2160b612);

589};

590

592

593/\* Flow ID is only 3 bits \*/

594#define WIFI\_MAX\_TWT\_FLOWS 8

595#define WIFI\_MAX\_TWT\_INTERVAL\_US (LONG\_MAX - 1)

596/\* 256 (u8) \* 1TU \*/

597#define WIFI\_MAX\_TWT\_WAKE\_INTERVAL\_US 262144

598#define WIFI\_MAX\_TWT\_WAKE\_AHEAD\_DURATION\_US (LONG\_MAX - 1)

599

601

[ 603](structwifi__twt__flow__info.md)struct [wifi\_twt\_flow\_info](structwifi__twt__flow__info.md) {

[ 605](structwifi__twt__flow__info.md#ae15ba49fa54f82cc6a1fb0d4572114b7) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [twt\_interval](structwifi__twt__flow__info.md#ae15ba49fa54f82cc6a1fb0d4572114b7);

[ 607](structwifi__twt__flow__info.md#a123ce10bed8b62b01919a7ea7644a0ba) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [dialog\_token](structwifi__twt__flow__info.md#a123ce10bed8b62b01919a7ea7644a0ba);

[ 609](structwifi__twt__flow__info.md#acb0c618f1cebcb172f342cfe222683be) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [flow\_id](structwifi__twt__flow__info.md#acb0c618f1cebcb172f342cfe222683be);

[ 611](structwifi__twt__flow__info.md#a620ae8ba546e4091d74280cb1553b2cf) enum [wifi\_twt\_negotiation\_type](group__wifi__mgmt.md#ga695123cd534e2499f516a07fdc5cafa8) [negotiation\_type](structwifi__twt__flow__info.md#a620ae8ba546e4091d74280cb1553b2cf);

[ 613](structwifi__twt__flow__info.md#ac82e4de8ffc82f851061f8ba8d217dc1) bool [responder](structwifi__twt__flow__info.md#ac82e4de8ffc82f851061f8ba8d217dc1);

[ 615](structwifi__twt__flow__info.md#a952a67bd092c5dadba387bb13449c6f3) bool [trigger](structwifi__twt__flow__info.md#a952a67bd092c5dadba387bb13449c6f3);

[ 617](structwifi__twt__flow__info.md#afb480be82d1c6f351bd634fd83bfa5c7) bool [implicit](structwifi__twt__flow__info.md#afb480be82d1c6f351bd634fd83bfa5c7);

[ 619](structwifi__twt__flow__info.md#afc81a5111c265fd9bb2aca5f9510bfa8) bool [announce](structwifi__twt__flow__info.md#afc81a5111c265fd9bb2aca5f9510bfa8);

[ 621](structwifi__twt__flow__info.md#aede6cb0cfc999fac8ded49e2981a3762) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [twt\_wake\_interval](structwifi__twt__flow__info.md#aede6cb0cfc999fac8ded49e2981a3762);

[ 623](structwifi__twt__flow__info.md#a6384d3829d54a58a53eafcb74c64a658) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [twt\_wake\_ahead\_duration](structwifi__twt__flow__info.md#a6384d3829d54a58a53eafcb74c64a658);

624};

625

[ 627](structwifi__ps__config.md)struct [wifi\_ps\_config](structwifi__ps__config.md) {

[ 629](structwifi__ps__config.md#a9e83c10eaaa1d721cbc49b40aedb00df) char [num\_twt\_flows](structwifi__ps__config.md#a9e83c10eaaa1d721cbc49b40aedb00df);

[ 631](structwifi__ps__config.md#ab7460f0f253b2d552e49e98e2c770967) struct [wifi\_twt\_flow\_info](structwifi__twt__flow__info.md) [twt\_flows](structwifi__ps__config.md#ab7460f0f253b2d552e49e98e2c770967)[WIFI\_MAX\_TWT\_FLOWS];

[ 633](structwifi__ps__config.md#a357aafc2dedda37755b1cb1fc07fe5a6) struct [wifi\_ps\_params](structwifi__ps__params.md) [ps\_params](structwifi__ps__config.md#a357aafc2dedda37755b1cb1fc07fe5a6);

634};

635

[ 637](group__wifi__mgmt.md#gae129d0783276e662575af2314eef86cd)enum [wifi\_mgmt\_op](group__wifi__mgmt.md#gae129d0783276e662575af2314eef86cd) {

[ 639](group__wifi__mgmt.md#ggae129d0783276e662575af2314eef86cda6b8183a773e0cdfa85bc4b41ae70fdcd) [WIFI\_MGMT\_GET](group__wifi__mgmt.md#ggae129d0783276e662575af2314eef86cda6b8183a773e0cdfa85bc4b41ae70fdcd) = 0,

[ 641](group__wifi__mgmt.md#ggae129d0783276e662575af2314eef86cdaa0d5931c8275a8d3288ab668b6dfb5a1) [WIFI\_MGMT\_SET](group__wifi__mgmt.md#ggae129d0783276e662575af2314eef86cdaa0d5931c8275a8d3288ab668b6dfb5a1) = 1,

642};

643

[ 645](group__wifi__mgmt.md#ga3a6bfa37bd7850342279d304df20977d)#define MAX\_REG\_CHAN\_NUM 42

646

[ 648](structwifi__reg__chan__info.md)struct [wifi\_reg\_chan\_info](structwifi__reg__chan__info.md) {

[ 650](structwifi__reg__chan__info.md#a0addffc11ef29f50c01b700835e59930) unsigned short [center\_frequency](structwifi__reg__chan__info.md#a0addffc11ef29f50c01b700835e59930);

[ 652](structwifi__reg__chan__info.md#af9169ab4a41fac4c6f6766fc96799545) unsigned short [max\_power](structwifi__reg__chan__info.md#af9169ab4a41fac4c6f6766fc96799545):8;

[ 654](structwifi__reg__chan__info.md#aa044611e18b7332b8577e29f6a769e3f) unsigned short [supported](structwifi__reg__chan__info.md#aa044611e18b7332b8577e29f6a769e3f):1;

[ 656](structwifi__reg__chan__info.md#acc7a88b004c9a61c8bf9ee1a97f85928) unsigned short [passive\_only](structwifi__reg__chan__info.md#acc7a88b004c9a61c8bf9ee1a97f85928):1;

[ 658](structwifi__reg__chan__info.md#a1ab137c142902d2de7d6be2626d7ac1f) unsigned short [dfs](structwifi__reg__chan__info.md#a1ab137c142902d2de7d6be2626d7ac1f):1;

659} \_\_packed;

660

[ 662](structwifi__reg__domain.md)struct [wifi\_reg\_domain](structwifi__reg__domain.md) {

[ 664](structwifi__reg__domain.md#a3bbfdf1497a87bbb6b6211c7035e1002) enum [wifi\_mgmt\_op](group__wifi__mgmt.md#gae129d0783276e662575af2314eef86cd) [oper](structwifi__reg__domain.md#a3bbfdf1497a87bbb6b6211c7035e1002);

[ 666](structwifi__reg__domain.md#a567c6fcae8032567aea83c18cd211c33) bool [force](structwifi__reg__domain.md#a567c6fcae8032567aea83c18cd211c33);

[ 668](structwifi__reg__domain.md#adfabbe25b049f0dd94c035a82c20a413) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [country\_code](structwifi__reg__domain.md#adfabbe25b049f0dd94c035a82c20a413)[[WIFI\_COUNTRY\_CODE\_LEN](group__wifi__mgmt.md#ga6766ef7bcb001f1fb526a4083b6cd8bc)];

[ 670](structwifi__reg__domain.md#a3278e9f43893f49ab9f9d0d7f24009c1) unsigned int [num\_channels](structwifi__reg__domain.md#a3278e9f43893f49ab9f9d0d7f24009c1);

[ 672](structwifi__reg__domain.md#a4c8c9c11e41123cd7738fdb0d33ae5fb) struct [wifi\_reg\_chan\_info](structwifi__reg__chan__info.md) \*[chan\_info](structwifi__reg__domain.md#a4c8c9c11e41123cd7738fdb0d33ae5fb);

673};

674

[ 676](group__wifi__mgmt.md#ga38c184ea35c02f304cccdf389ca6d552)enum [wifi\_twt\_sleep\_state](group__wifi__mgmt.md#ga38c184ea35c02f304cccdf389ca6d552) {

[ 678](group__wifi__mgmt.md#gga38c184ea35c02f304cccdf389ca6d552a37a7aba20723b6614e39e1c417f3113c) [WIFI\_TWT\_STATE\_SLEEP](group__wifi__mgmt.md#gga38c184ea35c02f304cccdf389ca6d552a37a7aba20723b6614e39e1c417f3113c) = 0,

[ 680](group__wifi__mgmt.md#gga38c184ea35c02f304cccdf389ca6d552a7b7b45f85d9644f897ca00bd7864e1b0) [WIFI\_TWT\_STATE\_AWAKE](group__wifi__mgmt.md#gga38c184ea35c02f304cccdf389ca6d552a7b7b45f85d9644f897ca00bd7864e1b0) = 1,

681};

682

683#if defined(CONFIG\_WIFI\_MGMT\_RAW\_SCAN\_RESULTS) || defined(\_\_DOXYGEN\_\_)

[ 685](structwifi__raw__scan__result.md)struct [wifi\_raw\_scan\_result](structwifi__raw__scan__result.md) {

[ 687](structwifi__raw__scan__result.md#a3f08580c6448a5fa28dd8a594fa7dad6) [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) [rssi](structwifi__raw__scan__result.md#a3f08580c6448a5fa28dd8a594fa7dad6);

[ 689](structwifi__raw__scan__result.md#a876966f469714eb481b42ccc8a63945c) int [frame\_length](structwifi__raw__scan__result.md#a876966f469714eb481b42ccc8a63945c);

[ 691](structwifi__raw__scan__result.md#aa2c7781882c6775616cbc8016b0842f6) unsigned short [frequency](structwifi__raw__scan__result.md#aa2c7781882c6775616cbc8016b0842f6);

[ 693](structwifi__raw__scan__result.md#a5710e89199c147ce898602795f00aba3) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [data](structwifi__raw__scan__result.md#a5710e89199c147ce898602795f00aba3)[CONFIG\_WIFI\_MGMT\_RAW\_SCAN\_RESULT\_LENGTH];

694};

695#endif /\* CONFIG\_WIFI\_MGMT\_RAW\_SCAN\_RESULTS \*/

696

[ 698](structwifi__ap__sta__info.md)struct [wifi\_ap\_sta\_info](structwifi__ap__sta__info.md) {

[ 700](structwifi__ap__sta__info.md#a7d8bd52340d4937a4b5b7d2c00662441) enum [wifi\_link\_mode](group__wifi__mgmt.md#gabdb2a784d4727b71ab44cca04e422c62) [link\_mode](structwifi__ap__sta__info.md#a7d8bd52340d4937a4b5b7d2c00662441);

[ 702](structwifi__ap__sta__info.md#a2a2fc109525e72ee7f18cced3b881107) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [mac](structwifi__ap__sta__info.md#a2a2fc109525e72ee7f18cced3b881107)[[WIFI\_MAC\_ADDR\_LEN](group__wifi__mgmt.md#ga29409ff83a53c6464decdde9bdd04de6)];

[ 704](structwifi__ap__sta__info.md#a7f7c8b144bb3464af5213708591eefda) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [mac\_length](structwifi__ap__sta__info.md#a7f7c8b144bb3464af5213708591eefda);

[ 706](structwifi__ap__sta__info.md#a838c9a4288c9bc7e97afe2334c678f34) bool [twt\_capable](structwifi__ap__sta__info.md#a838c9a4288c9bc7e97afe2334c678f34);

707};

708

710

711/\* for use in max info size calculations \*/

712union wifi\_mgmt\_events {

713 struct [wifi\_scan\_result](structwifi__scan__result.md) scan\_result;

714 struct [wifi\_status](structwifi__status.md) connect\_status;

715 struct [wifi\_iface\_status](structwifi__iface__status.md) iface\_status;

716#ifdef CONFIG\_WIFI\_MGMT\_RAW\_SCAN\_RESULTS

717 struct [wifi\_raw\_scan\_result](structwifi__raw__scan__result.md) raw\_scan\_result;

718#endif /\* CONFIG\_WIFI\_MGMT\_RAW\_SCAN\_RESULTS \*/

719 struct [wifi\_twt\_params](structwifi__twt__params.md) twt\_params;

720 struct [wifi\_ap\_sta\_info](structwifi__ap__sta__info.md) ap\_sta\_info;

721};

722

724

[ 726](structwifi__mode__info.md)struct [wifi\_mode\_info](structwifi__mode__info.md) {

[ 728](structwifi__mode__info.md#aa29d3b88fc718aa3ac05daf38974707d) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [mode](structwifi__mode__info.md#aa29d3b88fc718aa3ac05daf38974707d);

[ 730](structwifi__mode__info.md#add58dd3b45fd2ddaf684d1b0de81bef9) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [if\_index](structwifi__mode__info.md#add58dd3b45fd2ddaf684d1b0de81bef9);

[ 732](structwifi__mode__info.md#a57c101db8b81ab0ac5dd0a158057a64a) enum [wifi\_mgmt\_op](group__wifi__mgmt.md#gae129d0783276e662575af2314eef86cd) [oper](structwifi__mode__info.md#a57c101db8b81ab0ac5dd0a158057a64a);

733};

734

[ 736](structwifi__filter__info.md)struct [wifi\_filter\_info](structwifi__filter__info.md) {

[ 738](structwifi__filter__info.md#ad9560be814299055cfa11b995a7dcf42) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [filter](structwifi__filter__info.md#ad9560be814299055cfa11b995a7dcf42);

[ 740](structwifi__filter__info.md#af9ea91e31e78afcb7ffe1ff9a04277a3) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [if\_index](structwifi__filter__info.md#af9ea91e31e78afcb7ffe1ff9a04277a3);

[ 742](structwifi__filter__info.md#a1b2d0448fc7f62654e3f5aacfba62f8f) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [buffer\_size](structwifi__filter__info.md#a1b2d0448fc7f62654e3f5aacfba62f8f);

[ 744](structwifi__filter__info.md#aedd5e220cdde5768cb0f4aff920971cd) enum [wifi\_mgmt\_op](group__wifi__mgmt.md#gae129d0783276e662575af2314eef86cd) [oper](structwifi__filter__info.md#aedd5e220cdde5768cb0f4aff920971cd);

745};

746

[ 748](structwifi__channel__info.md)struct [wifi\_channel\_info](structwifi__channel__info.md) {

[ 750](structwifi__channel__info.md#a799cbc0a67764f6680322ba0f2ad3300) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [channel](structwifi__channel__info.md#a799cbc0a67764f6680322ba0f2ad3300);

[ 752](structwifi__channel__info.md#a43a7dd8c19d0c6540e3cc0b5d1d6165d) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [if\_index](structwifi__channel__info.md#a43a7dd8c19d0c6540e3cc0b5d1d6165d);

[ 754](structwifi__channel__info.md#aa8ef8a71b49ead3664fff9a4d61b1ce8) enum [wifi\_mgmt\_op](group__wifi__mgmt.md#gae129d0783276e662575af2314eef86cd) [oper](structwifi__channel__info.md#aa8ef8a71b49ead3664fff9a4d61b1ce8);

755};

756

758#define WIFI\_AP\_STA\_MAX\_INACTIVITY (LONG\_MAX - 1)

760

[ 762](structwifi__ap__config__params.md)struct [wifi\_ap\_config\_params](structwifi__ap__config__params.md) {

[ 764](structwifi__ap__config__params.md#a4c391cf504a994ed0bc4971afdf76774) enum [wifi\_ap\_config\_param](group__wifi__mgmt.md#ga83546cf946a9123c563609e8903d9642) [type](structwifi__ap__config__params.md#a4c391cf504a994ed0bc4971afdf76774);

[ 766](structwifi__ap__config__params.md#a289866d9209450e893281b4c198a546a) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [max\_inactivity](structwifi__ap__config__params.md#a289866d9209450e893281b4c198a546a);

[ 768](structwifi__ap__config__params.md#a7fc0fad99f53ed8e1ac40b74ec98bf9a) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [max\_num\_sta](structwifi__ap__config__params.md#a7fc0fad99f53ed8e1ac40b74ec98bf9a);

769};

770

771#include <[zephyr/net/net\_if.h](net__if_8h.md)>

772

[ 779](group__wifi__mgmt.md#gad34b366f1c315207ce0da587ca96d8d8)typedef void (\*[scan\_result\_cb\_t](group__wifi__mgmt.md#gad34b366f1c315207ce0da587ca96d8d8))(struct [net\_if](structnet__if.md) \*iface, int status,

780 struct [wifi\_scan\_result](structwifi__scan__result.md) \*entry);

781

782#ifdef CONFIG\_WIFI\_MGMT\_RAW\_SCAN\_RESULTS

789typedef void (\*raw\_scan\_result\_cb\_t)(struct [net\_if](structnet__if.md) \*iface, int status,

790 struct [wifi\_raw\_scan\_result](structwifi__raw__scan__result.md) \*entry);

791#endif /\* CONFIG\_WIFI\_MGMT\_RAW\_SCAN\_RESULTS \*/

792

[ 794](structwifi__mgmt__ops.md)struct [wifi\_mgmt\_ops](structwifi__mgmt__ops.md) {

[ 806](structwifi__mgmt__ops.md#a267030c27da3cdc251badd0ed7f7b1cb) int (\*[scan](structwifi__mgmt__ops.md#a267030c27da3cdc251badd0ed7f7b1cb))(const struct [device](structdevice.md) \*dev,

807 struct [wifi\_scan\_params](structwifi__scan__params.md) \*params,

808 [scan\_result\_cb\_t](group__wifi__mgmt.md#gad34b366f1c315207ce0da587ca96d8d8) cb);

[ 816](structwifi__mgmt__ops.md#ae6255ea77739918797b4f3c7a4634a75) int (\*[connect](structwifi__mgmt__ops.md#ae6255ea77739918797b4f3c7a4634a75))(const struct [device](structdevice.md) \*dev,

817 struct [wifi\_connect\_req\_params](structwifi__connect__req__params.md) \*params);

[ 824](structwifi__mgmt__ops.md#a5725c6fd93ae189a3019374cd4ad2ff4) int (\*[disconnect](structwifi__mgmt__ops.md#a5725c6fd93ae189a3019374cd4ad2ff4))(const struct [device](structdevice.md) \*dev);

[ 832](structwifi__mgmt__ops.md#ac2ce3a4a86c43e30d33261f71c44198a) int (\*[ap\_enable](structwifi__mgmt__ops.md#ac2ce3a4a86c43e30d33261f71c44198a))(const struct [device](structdevice.md) \*dev,

833 struct [wifi\_connect\_req\_params](structwifi__connect__req__params.md) \*params);

[ 840](structwifi__mgmt__ops.md#a5aa7a2be82eb1783872abda2b8978235) int (\*[ap\_disable](structwifi__mgmt__ops.md#a5aa7a2be82eb1783872abda2b8978235))(const struct [device](structdevice.md) \*dev);

[ 848](structwifi__mgmt__ops.md#af01aaec29be78c02314acf13b5c1b6f7) int (\*[ap\_sta\_disconnect](structwifi__mgmt__ops.md#af01aaec29be78c02314acf13b5c1b6f7))(const struct [device](structdevice.md) \*dev, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*mac);

[ 856](structwifi__mgmt__ops.md#adf157476d776bc9c068e99e1a0266fd3) int (\*[iface\_status](structwifi__mgmt__ops.md#adf157476d776bc9c068e99e1a0266fd3))(const struct [device](structdevice.md) \*dev, struct [wifi\_iface\_status](structwifi__iface__status.md) \*status);

857#if defined(CONFIG\_NET\_STATISTICS\_WIFI) || defined(\_\_DOXYGEN\_\_)

[ 865](structwifi__mgmt__ops.md#a5e6fdf836273fcde54efff4c77bfdf0e) int (\*[get\_stats](structwifi__mgmt__ops.md#a5e6fdf836273fcde54efff4c77bfdf0e))(const struct [device](structdevice.md) \*dev, struct [net\_stats\_wifi](structnet__stats__wifi.md) \*stats);

866#endif /\* CONFIG\_NET\_STATISTICS\_WIFI \*/

[ 874](structwifi__mgmt__ops.md#ac0f3f7fa699b1bc7db2358e77dd44cc4) int (\*[set\_power\_save](structwifi__mgmt__ops.md#ac0f3f7fa699b1bc7db2358e77dd44cc4))(const struct [device](structdevice.md) \*dev, struct [wifi\_ps\_params](structwifi__ps__params.md) \*params);

[ 882](structwifi__mgmt__ops.md#ab4500534b6abe0449290c8bd8f729fc4) int (\*[set\_twt](structwifi__mgmt__ops.md#ab4500534b6abe0449290c8bd8f729fc4))(const struct [device](structdevice.md) \*dev, struct [wifi\_twt\_params](structwifi__twt__params.md) \*params);

[ 890](structwifi__mgmt__ops.md#a52690b13f8a1e7b0c2302eaa24ae4c7f) int (\*[get\_power\_save\_config](structwifi__mgmt__ops.md#a52690b13f8a1e7b0c2302eaa24ae4c7f))(const struct [device](structdevice.md) \*dev, struct [wifi\_ps\_config](structwifi__ps__config.md) \*config);

[ 898](structwifi__mgmt__ops.md#a0a287c8acf2d7bf9333b755589294881) int (\*[reg\_domain](structwifi__mgmt__ops.md#a0a287c8acf2d7bf9333b755589294881))(const struct [device](structdevice.md) \*dev, struct [wifi\_reg\_domain](structwifi__reg__domain.md) \*[reg\_domain](structwifi__mgmt__ops.md#a0a287c8acf2d7bf9333b755589294881));

[ 906](structwifi__mgmt__ops.md#ad645276745ce8dd9685e0744efdfc733) int (\*[filter](structwifi__mgmt__ops.md#ad645276745ce8dd9685e0744efdfc733))(const struct [device](structdevice.md) \*dev, struct [wifi\_filter\_info](structwifi__filter__info.md) \*[filter](structwifi__mgmt__ops.md#ad645276745ce8dd9685e0744efdfc733));

[ 914](structwifi__mgmt__ops.md#ae2fb1bc35bf9255655a30a2ad8588b7c) int (\*[mode](structwifi__mgmt__ops.md#ae2fb1bc35bf9255655a30a2ad8588b7c))(const struct [device](structdevice.md) \*dev, struct [wifi\_mode\_info](structwifi__mode__info.md) \*[mode](structwifi__mgmt__ops.md#ae2fb1bc35bf9255655a30a2ad8588b7c));

[ 922](structwifi__mgmt__ops.md#af17ddfea01d0ab478f6fd50b1c9d6015) int (\*[channel](structwifi__mgmt__ops.md#af17ddfea01d0ab478f6fd50b1c9d6015))(const struct [device](structdevice.md) \*dev, struct [wifi\_channel\_info](structwifi__channel__info.md) \*[channel](structwifi__mgmt__ops.md#af17ddfea01d0ab478f6fd50b1c9d6015));

[ 935](structwifi__mgmt__ops.md#aa7e4bc3dbc960091d11ffe5454259885) int (\*[get\_version](structwifi__mgmt__ops.md#aa7e4bc3dbc960091d11ffe5454259885))(const struct [device](structdevice.md) \*dev, struct [wifi\_version](structwifi__version.md) \*params);

[ 943](structwifi__mgmt__ops.md#a514e06d63bcf6dc11dba1d3af8d102d5) int (\*[set\_rts\_threshold](structwifi__mgmt__ops.md#a514e06d63bcf6dc11dba1d3af8d102d5))(const struct [device](structdevice.md) \*dev, unsigned int rts\_threshold);

[ 951](structwifi__mgmt__ops.md#a2475f32afcce72464b2db6ecad7fb3eb) int (\*[ap\_config\_params](structwifi__mgmt__ops.md#a2475f32afcce72464b2db6ecad7fb3eb))(const struct [device](structdevice.md) \*dev, struct [wifi\_ap\_config\_params](structwifi__ap__config__params.md) \*params);

952};

953

[ 955](structnet__wifi__mgmt__offload.md)struct [net\_wifi\_mgmt\_offload](structnet__wifi__mgmt__offload.md) {

962#if defined(CONFIG\_WIFI\_USE\_NATIVE\_NETWORKING) || defined(\_\_DOXYGEN\_\_)

[ 964](structnet__wifi__mgmt__offload.md#a1d34a954a2f16d29f51dc51dd6fbb845) struct [ethernet\_api](structethernet__api.md) [wifi\_iface](structnet__wifi__mgmt__offload.md#a1d34a954a2f16d29f51dc51dd6fbb845);

965#else

967 struct [offloaded\_if\_api](structoffloaded__if__api.md) [wifi\_iface](structnet__wifi__mgmt__offload.md#a1d34a954a2f16d29f51dc51dd6fbb845);

968#endif

[ 970](structnet__wifi__mgmt__offload.md#a98fcc053d9820d2d981ed659520c9b3b) const struct [wifi\_mgmt\_ops](structwifi__mgmt__ops.md) \*const [wifi\_mgmt\_api](structnet__wifi__mgmt__offload.md#a98fcc053d9820d2d981ed659520c9b3b);

971

972#if defined(CONFIG\_WIFI\_NM\_WPA\_SUPPLICANT) || defined(\_\_DOXYGEN\_\_)

[ 974](structnet__wifi__mgmt__offload.md#a991e0bc6247578a3d1c9d2d3ab0b63d7) const void \*[wifi\_drv\_ops](structnet__wifi__mgmt__offload.md#a991e0bc6247578a3d1c9d2d3ab0b63d7);

975#endif

976};

977

978#if defined(CONFIG\_WIFI\_NM\_WPA\_SUPPLICANT)

979/\* Make sure wifi\_drv\_ops is after wifi\_mgmt\_api \*/

980BUILD\_ASSERT(offsetof(struct [net\_wifi\_mgmt\_offload](structnet__wifi__mgmt__offload.md), wifi\_mgmt\_api) <

981 offsetof(struct [net\_wifi\_mgmt\_offload](structnet__wifi__mgmt__offload.md), wifi\_drv\_ops));

982#endif

983

984/\* Make sure that the network interface API is properly setup inside

985 \* Wifi mgmt offload API struct (it is the first one).

986 \*/

987BUILD\_ASSERT(offsetof(struct [net\_wifi\_mgmt\_offload](structnet__wifi__mgmt__offload.md), wifi\_iface) == 0);

988

[ 994](group__wifi__mgmt.md#ga036416696b1e3bc458ddbaf07a08d69d)void [wifi\_mgmt\_raise\_connect\_result\_event](group__wifi__mgmt.md#ga036416696b1e3bc458ddbaf07a08d69d)(struct [net\_if](structnet__if.md) \*iface, int status);

995

[ 1001](group__wifi__mgmt.md#ga3b6edcf9b51afbf7a327d1a344bd7b87)void [wifi\_mgmt\_raise\_disconnect\_result\_event](group__wifi__mgmt.md#ga3b6edcf9b51afbf7a327d1a344bd7b87)(struct [net\_if](structnet__if.md) \*iface, int status);

1002

[ 1008](group__wifi__mgmt.md#ga7da6af0747bcba85f8afab30c92b5b43)void [wifi\_mgmt\_raise\_iface\_status\_event](group__wifi__mgmt.md#ga7da6af0747bcba85f8afab30c92b5b43)(struct [net\_if](structnet__if.md) \*iface,

1009 struct [wifi\_iface\_status](structwifi__iface__status.md) \*[iface\_status](structwifi__mgmt__ops.md#adf157476d776bc9c068e99e1a0266fd3));

1010

[ 1016](group__wifi__mgmt.md#ga39404d15243ca084b253cae8fc07e374)void [wifi\_mgmt\_raise\_twt\_event](group__wifi__mgmt.md#ga39404d15243ca084b253cae8fc07e374)(struct [net\_if](structnet__if.md) \*iface,

1017 struct [wifi\_twt\_params](structwifi__twt__params.md) \*twt\_params);

1018

[ 1024](group__wifi__mgmt.md#ga18f09a3196588b51d6c0644f82f639d7)void [wifi\_mgmt\_raise\_twt\_sleep\_state](group__wifi__mgmt.md#ga18f09a3196588b51d6c0644f82f639d7)(struct [net\_if](structnet__if.md) \*iface, int twt\_sleep\_state);

1025

1026#if defined(CONFIG\_WIFI\_MGMT\_RAW\_SCAN\_RESULTS) || defined(\_\_DOXYGEN\_\_)

[ 1032](group__wifi__mgmt.md#ga71c99913bded844c4ca32ed9155bc470)void [wifi\_mgmt\_raise\_raw\_scan\_result\_event](group__wifi__mgmt.md#ga71c99913bded844c4ca32ed9155bc470)(struct [net\_if](structnet__if.md) \*iface,

1033 struct [wifi\_raw\_scan\_result](structwifi__raw__scan__result.md) \*raw\_scan\_info);

1034#endif /\* CONFIG\_WIFI\_MGMT\_RAW\_SCAN\_RESULTS \*/

1035

[ 1041](group__wifi__mgmt.md#gaa75246d6dc55dada389c9d31e2607d5c)void [wifi\_mgmt\_raise\_disconnect\_complete\_event](group__wifi__mgmt.md#gaa75246d6dc55dada389c9d31e2607d5c)(struct [net\_if](structnet__if.md) \*iface, int status);

1042

[ 1048](group__wifi__mgmt.md#ga67b52edeff76c2211b038f4aa90b8982)void [wifi\_mgmt\_raise\_ap\_enable\_result\_event](group__wifi__mgmt.md#ga67b52edeff76c2211b038f4aa90b8982)(struct [net\_if](structnet__if.md) \*iface, enum [wifi\_ap\_status](group__wifi__mgmt.md#gaaf730bf76adc06434c7ac63bf0417884) status);

1049

[ 1055](group__wifi__mgmt.md#gadee15c6a492a8ee13bea43812debb5d9)void [wifi\_mgmt\_raise\_ap\_disable\_result\_event](group__wifi__mgmt.md#gadee15c6a492a8ee13bea43812debb5d9)(struct [net\_if](structnet__if.md) \*iface, enum [wifi\_ap\_status](group__wifi__mgmt.md#gaaf730bf76adc06434c7ac63bf0417884) status);

1056

[ 1062](group__wifi__mgmt.md#gac8f17f0aa3e426a5cdb731727b9b9ce3)void [wifi\_mgmt\_raise\_ap\_sta\_connected\_event](group__wifi__mgmt.md#gac8f17f0aa3e426a5cdb731727b9b9ce3)(struct [net\_if](structnet__if.md) \*iface,

1063 struct [wifi\_ap\_sta\_info](structwifi__ap__sta__info.md) \*sta\_info);

1064

[ 1069](group__wifi__mgmt.md#ga49fb9c3908be61d847b31c99be6afc42)void [wifi\_mgmt\_raise\_ap\_sta\_disconnected\_event](group__wifi__mgmt.md#ga49fb9c3908be61d847b31c99be6afc42)(struct [net\_if](structnet__if.md) \*iface,

1070 struct [wifi\_ap\_sta\_info](structwifi__ap__sta__info.md) \*sta\_info);

1071

1075#ifdef \_\_cplusplus

1076}

1077#endif

1078

1079#endif /\* ZEPHYR\_INCLUDE\_NET\_WIFI\_MGMT\_H\_ \*/

[ethernet.h](ethernet_8h.md)

Ethernet.

[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)

#define NET\_MGMT\_DEFINE\_REQUEST\_HANDLER(\_mgmt\_request)

Declare a request handler function for the given network event.

**Definition** net\_mgmt.h:109

[wifi\_mgmt\_raise\_connect\_result\_event](group__wifi__mgmt.md#ga036416696b1e3bc458ddbaf07a08d69d)

void wifi\_mgmt\_raise\_connect\_result\_event(struct net\_if \*iface, int status)

Wi-Fi management connect result event.

[wifi\_ps](group__wifi__mgmt.md#ga0fffeb57b68fb8cdef9d3d571368b8ca)

wifi\_ps

Wi-Fi power save states.

**Definition** wifi.h:248

[NET\_REQUEST\_WIFI\_PS\_CONFIG](group__wifi__mgmt.md#ga1032f3773cfe6130da4d4d498b044ee2)

#define NET\_REQUEST\_WIFI\_PS\_CONFIG

Request a Wi-Fi power save configuration.

**Definition** wifi\_mgmt.h:148

[wifi\_mgmt\_raise\_twt\_sleep\_state](group__wifi__mgmt.md#ga18f09a3196588b51d6c0644f82f639d7)

void wifi\_mgmt\_raise\_twt\_sleep\_state(struct net\_if \*iface, int twt\_sleep\_state)

Wi-Fi management TWT sleep state event.

[NET\_REQUEST\_WIFI\_SCAN](group__wifi__mgmt.md#ga1c277da90986fa52dca182c4d922646f)

#define NET\_REQUEST\_WIFI\_SCAN

Request a Wi-Fi scan.

**Definition** wifi\_mgmt.h:100

[wifi\_frequency\_bands](group__wifi__mgmt.md#ga1e2f0439a322355fa7368ea880c9c15d)

wifi\_frequency\_bands

IEEE 802.11 operational frequency bands (not exhaustive).

**Definition** wifi.h:92

[wifi\_mfp\_options](group__wifi__mgmt.md#ga1f252da47d9650023d7fff6d08e49c76)

wifi\_mfp\_options

IEEE 802.11w - Management frame protection.

**Definition** wifi.h:71

[NET\_REQUEST\_WIFI\_RTS\_THRESHOLD](group__wifi__mgmt.md#ga22d80ef0ffb15e4286d7b1c3325d5334)

#define NET\_REQUEST\_WIFI\_RTS\_THRESHOLD

Request a Wi-Fi RTS threshold.

**Definition** wifi\_mgmt.h:190

[WIFI\_MAC\_ADDR\_LEN](group__wifi__mgmt.md#ga29409ff83a53c6464decdde9bdd04de6)

#define WIFI\_MAC\_ADDR\_LEN

MAC address length.

**Definition** wifi.h:120

[NET\_REQUEST\_WIFI\_REG\_DOMAIN](group__wifi__mgmt.md#ga2b27d102b779a6d846b375854768fb7f)

#define NET\_REQUEST\_WIFI\_REG\_DOMAIN

Request a Wi-Fi regulatory domain.

**Definition** wifi\_mgmt.h:154

[NET\_REQUEST\_WIFI\_PACKET\_FILTER](group__wifi__mgmt.md#ga3098e817d12bf4619c9fd2698508fb4e)

#define NET\_REQUEST\_WIFI\_PACKET\_FILTER

Request Wi-Fi packet filter.

**Definition** wifi\_mgmt.h:166

[wifi\_twt\_setup\_cmd](group__wifi__mgmt.md#ga31c78afc89bfdc4b54cee177843f8022)

wifi\_twt\_setup\_cmd

Wi-Fi Target Wake Time (TWT) setup commands.

**Definition** wifi.h:330

[wifi\_twt\_sleep\_state](group__wifi__mgmt.md#ga38c184ea35c02f304cccdf389ca6d552)

wifi\_twt\_sleep\_state

Wi-Fi TWT sleep states.

**Definition** wifi\_mgmt.h:676

[wifi\_mgmt\_raise\_twt\_event](group__wifi__mgmt.md#ga39404d15243ca084b253cae8fc07e374)

void wifi\_mgmt\_raise\_twt\_event(struct net\_if \*iface, struct wifi\_twt\_params \*twt\_params)

Wi-Fi management TWT event.

[wifi\_mgmt\_raise\_disconnect\_result\_event](group__wifi__mgmt.md#ga3b6edcf9b51afbf7a327d1a344bd7b87)

void wifi\_mgmt\_raise\_disconnect\_result\_event(struct net\_if \*iface, int status)

Wi-Fi management disconnect result event.

[NET\_REQUEST\_WIFI\_IFACE\_STATUS](group__wifi__mgmt.md#ga3e45f6ee3801553619d8eb7d0af506eb)

#define NET\_REQUEST\_WIFI\_IFACE\_STATUS

Request a Wi-Fi network interface status.

**Definition** wifi\_mgmt.h:130

[NET\_REQUEST\_WIFI\_VERSION](group__wifi__mgmt.md#ga3e60c29ca9ce95d17a7fff087290f7f1)

#define NET\_REQUEST\_WIFI\_VERSION

Request a Wi-Fi version.

**Definition** wifi\_mgmt.h:184

[wifi\_mgmt\_raise\_ap\_sta\_disconnected\_event](group__wifi__mgmt.md#ga49fb9c3908be61d847b31c99be6afc42)

void wifi\_mgmt\_raise\_ap\_sta\_disconnected\_event(struct net\_if \*iface, struct wifi\_ap\_sta\_info \*sta\_info)

Wi-Fi management AP mode STA disconnected event.

[wifi\_twt\_setup\_resp\_status](group__wifi__mgmt.md#ga4d03aedac13ee4512d7717ac624f319a)

wifi\_twt\_setup\_resp\_status

Wi-Fi Target Wake Time (TWT) negotiation status.

**Definition** wifi.h:353

[wifi\_iface\_mode](group__wifi__mgmt.md#ga584f6239ac14e2bedc5e6bd72756423b)

wifi\_iface\_mode

Wi-Fi interface modes.

**Definition** wifi.h:181

[NET\_REQUEST\_WIFI\_AP\_ENABLE](group__wifi__mgmt.md#ga638d2eb0a5029c1af46a91b523ed8589)

#define NET\_REQUEST\_WIFI\_AP\_ENABLE

Request a Wi-Fi access point enable.

**Definition** wifi\_mgmt.h:118

[WIFI\_COUNTRY\_CODE\_LEN](group__wifi__mgmt.md#ga6766ef7bcb001f1fb526a4083b6cd8bc)

#define WIFI\_COUNTRY\_CODE\_LEN

Length of the country code string.

**Definition** wifi.h:26

[wifi\_mgmt\_raise\_ap\_enable\_result\_event](group__wifi__mgmt.md#ga67b52edeff76c2211b038f4aa90b8982)

void wifi\_mgmt\_raise\_ap\_enable\_result\_event(struct net\_if \*iface, enum wifi\_ap\_status status)

Wi-Fi management AP mode enable result event.

[NET\_REQUEST\_WIFI\_PS](group__wifi__mgmt.md#ga68aaced888f98e1ba4e6b61b53e5e2ba)

#define NET\_REQUEST\_WIFI\_PS

Request a Wi-Fi power save.

**Definition** wifi\_mgmt.h:136

[wifi\_twt\_negotiation\_type](group__wifi__mgmt.md#ga695123cd534e2499f516a07fdc5cafa8)

wifi\_twt\_negotiation\_type

Wi-Fi Target Wake Time (TWT) negotiation types.

**Definition** wifi.h:317

[wifi\_mgmt\_raise\_raw\_scan\_result\_event](group__wifi__mgmt.md#ga71c99913bded844c4ca32ed9155bc470)

void wifi\_mgmt\_raise\_raw\_scan\_result\_event(struct net\_if \*iface, struct wifi\_raw\_scan\_result \*raw\_scan\_info)

Wi-Fi management raw scan result event.

[wifi\_mgmt\_raise\_iface\_status\_event](group__wifi__mgmt.md#ga7da6af0747bcba85f8afab30c92b5b43)

void wifi\_mgmt\_raise\_iface\_status\_event(struct net\_if \*iface, struct wifi\_iface\_status \*iface\_status)

Wi-Fi management interface status event.

[wifi\_ap\_config\_param](group__wifi__mgmt.md#ga83546cf946a9123c563609e8903d9642)

wifi\_ap\_config\_param

Wi-Fi AP mode configuration parameter.

**Definition** wifi.h:498

[wifi\_conn\_status](group__wifi__mgmt.md#ga86a5741e54aeb3e290142b0de217b8a8)

wifi\_conn\_status

Wi-Fi connect result codes.

**Definition** wifi\_mgmt.h:410

[NET\_REQUEST\_WIFI\_DISCONNECT](group__wifi__mgmt.md#ga90afd8d4e83056463ec6e667ed8ea60a)

#define NET\_REQUEST\_WIFI\_DISCONNECT

Request a Wi-Fi disconnect.

**Definition** wifi\_mgmt.h:112

[wifi\_twt\_fail\_reason](group__wifi__mgmt.md#ga97fa304f9a1db2294a93cccd4c93bcf6)

wifi\_twt\_fail\_reason

Target Wake Time (TWT) error codes.

**Definition** wifi.h:361

[net\_request\_wifi\_cmd](group__wifi__mgmt.md#ga99a55137188119f65f9d2bb4f57cac77)

net\_request\_wifi\_cmd

Wi-Fi management commands.

**Definition** wifi\_mgmt.h:59

[NET\_REQUEST\_WIFI\_MODE](group__wifi__mgmt.md#ga9b4da60a8108b0cc431ac1eecfca0cd0)

#define NET\_REQUEST\_WIFI\_MODE

Request current Wi-Fi mode.

**Definition** wifi\_mgmt.h:160

[NET\_REQUEST\_WIFI\_AP\_STA\_DISCONNECT](group__wifi__mgmt.md#gaa3e52e08d89a1104f07207e52b81d503)

#define NET\_REQUEST\_WIFI\_AP\_STA\_DISCONNECT

Request a Wi-Fi access point to disconnect a station.

**Definition** wifi\_mgmt.h:178

[wifi\_mgmt\_raise\_disconnect\_complete\_event](group__wifi__mgmt.md#gaa75246d6dc55dada389c9d31e2607d5c)

void wifi\_mgmt\_raise\_disconnect\_complete\_event(struct net\_if \*iface, int status)

Wi-Fi management disconnect complete event.

[NET\_REQUEST\_WIFI\_CONNECT](group__wifi__mgmt.md#gaa7ab2a97950a22736bb69f60b459f0f6)

#define NET\_REQUEST\_WIFI\_CONNECT

Request a Wi-Fi connect.

**Definition** wifi\_mgmt.h:106

[wifi\_ap\_status](group__wifi__mgmt.md#gaaf730bf76adc06434c7ac63bf0417884)

wifi\_ap\_status

Wi-Fi AP mode result codes.

**Definition** wifi\_mgmt.h:453

[NET\_REQUEST\_WIFI\_TWT](group__wifi__mgmt.md#gab84fd7e9ca0bf0b2b9d08889dda26aad)

#define NET\_REQUEST\_WIFI\_TWT

Request a Wi-Fi TWT.

**Definition** wifi\_mgmt.h:142

[wifi\_link\_mode](group__wifi__mgmt.md#gabdb2a784d4727b71ab44cca04e422c62)

wifi\_link\_mode

Wi-Fi link operating modes.

**Definition** wifi.h:209

[wifi\_ps\_param\_type](group__wifi__mgmt.md#gabe45d132797047c098041331c8f6f912)

wifi\_ps\_param\_type

Wi-Fi power save parameters.

**Definition** wifi.h:428

[net\_event\_wifi\_cmd](group__wifi__mgmt.md#gac2638308cbb0d268831f1618cf8e1fa8)

net\_event\_wifi\_cmd

Wi-Fi management events.

**Definition** wifi\_mgmt.h:202

[wifi\_disconn\_reason](group__wifi__mgmt.md#gac782af0a60b202fd19597cabb7bd3a9a)

wifi\_disconn\_reason

Wi-Fi disconnect reason codes.

**Definition** wifi\_mgmt.h:437

[wifi\_ps\_wakeup\_mode](group__wifi__mgmt.md#gac7f907644847e905d67c709fa4afae7f)

wifi\_ps\_wakeup\_mode

Wi-Fi power save modes.

**Definition** wifi.h:442

[wifi\_mgmt\_raise\_ap\_sta\_connected\_event](group__wifi__mgmt.md#gac8f17f0aa3e426a5cdb731727b9b9ce3)

void wifi\_mgmt\_raise\_ap\_sta\_connected\_event(struct net\_if \*iface, struct wifi\_ap\_sta\_info \*sta\_info)

Wi-Fi management AP mode STA connected event.

[wifi\_twt\_operation](group__wifi__mgmt.md#gad0e998aeb1b27c4f203ca76339d323a3)

wifi\_twt\_operation

Wi-Fi Target Wake Time (TWT) operations.

**Definition** wifi.h:306

[wifi\_scan\_type](group__wifi__mgmt.md#gad30e29eda65ccafdbd7f11865937b8ea)

wifi\_scan\_type

Wi-Fi scanning types.

**Definition** wifi.h:240

[scan\_result\_cb\_t](group__wifi__mgmt.md#gad34b366f1c315207ce0da587ca96d8d8)

void(\* scan\_result\_cb\_t)(struct net\_if \*iface, int status, struct wifi\_scan\_result \*entry)

Scan result callback.

**Definition** wifi\_mgmt.h:779

[wifi\_twt\_teardown\_status](group__wifi__mgmt.md#gad3709d07aaa3ed59b48f9dd7bd181989)

wifi\_twt\_teardown\_status

Wi-Fi Target Wake Time (TWT) teradown status.

**Definition** wifi.h:387

[WIFI\_SSID\_MAX\_LEN](group__wifi__mgmt.md#gad62c60666c9fdffe2e0e9c4388f87886)

#define WIFI\_SSID\_MAX\_LEN

Max SSID length.

**Definition** wifi.h:112

[NET\_REQUEST\_WIFI\_CHANNEL](group__wifi__mgmt.md#gad9614d2368f8399850aaec05e40bdc78)

#define NET\_REQUEST\_WIFI\_CHANNEL

Request a Wi-Fi channel.

**Definition** wifi\_mgmt.h:172

[wifi\_config\_ps\_param\_fail\_reason](group__wifi__mgmt.md#gad98099584d2222ede93aba42b1fbaff0)

wifi\_config\_ps\_param\_fail\_reason

Wi-Fi power save error codes.

**Definition** wifi.h:453

[wifi\_security\_type](group__wifi__mgmt.md#gadde31a04fa25ed805115c6b31854cd9c)

wifi\_security\_type

IEEE 802.11 security types.

**Definition** wifi.h:40

[wifi\_mgmt\_raise\_ap\_disable\_result\_event](group__wifi__mgmt.md#gadee15c6a492a8ee13bea43812debb5d9)

void wifi\_mgmt\_raise\_ap\_disable\_result\_event(struct net\_if \*iface, enum wifi\_ap\_status status)

Wi-Fi management AP mode disable result event.

[wifi\_mgmt\_op](group__wifi__mgmt.md#gae129d0783276e662575af2314eef86cd)

wifi\_mgmt\_op

Generic get/set operation for any command.

**Definition** wifi\_mgmt.h:637

[NET\_REQUEST\_WIFI\_AP\_CONFIG\_PARAM](group__wifi__mgmt.md#gaf4a78d230f5e0743a6aaf152ddda1c67)

#define NET\_REQUEST\_WIFI\_AP\_CONFIG\_PARAM

Request a Wi-Fi AP parameters configuration.

**Definition** wifi\_mgmt.h:196

[NET\_REQUEST\_WIFI\_AP\_DISABLE](group__wifi__mgmt.md#gaf81f62bf4c9e331a095acbf0d24ca1a2)

#define NET\_REQUEST\_WIFI\_AP\_DISABLE

Request a Wi-Fi access point disable.

**Definition** wifi\_mgmt.h:124

[wifi\_ps\_mode](group__wifi__mgmt.md#gaffae7d2a754be5eb952ad2b83edad54c)

wifi\_ps\_mode

Wi-Fi power save modes.

**Definition** wifi.h:259

[WIFI\_TWT\_STATE\_SLEEP](group__wifi__mgmt.md#gga38c184ea35c02f304cccdf389ca6d552a37a7aba20723b6614e39e1c417f3113c)

@ WIFI\_TWT\_STATE\_SLEEP

TWT sleep state: sleeping.

**Definition** wifi\_mgmt.h:678

[WIFI\_TWT\_STATE\_AWAKE](group__wifi__mgmt.md#gga38c184ea35c02f304cccdf389ca6d552a7b7b45f85d9644f897ca00bd7864e1b0)

@ WIFI\_TWT\_STATE\_AWAKE

TWT sleep state: awake.

**Definition** wifi\_mgmt.h:680

[WIFI\_STATUS\_CONN\_AP\_NOT\_FOUND](group__wifi__mgmt.md#gga86a5741e54aeb3e290142b0de217b8a8a2ae79fa389bb447fa108e0107aeff2f4)

@ WIFI\_STATUS\_CONN\_AP\_NOT\_FOUND

Connection failed - AP not found.

**Definition** wifi\_mgmt.h:427

[WIFI\_STATUS\_CONN\_SUCCESS](group__wifi__mgmt.md#gga86a5741e54aeb3e290142b0de217b8a8a380410b02b1e12599f37d1dcb844f5bd)

@ WIFI\_STATUS\_CONN\_SUCCESS

Connection successful.

**Definition** wifi\_mgmt.h:412

[WIFI\_STATUS\_CONN\_WRONG\_PASSWORD](group__wifi__mgmt.md#gga86a5741e54aeb3e290142b0de217b8a8a90d91f96a35c9f6847cbc7abd8c20bf8)

@ WIFI\_STATUS\_CONN\_WRONG\_PASSWORD

Connection failed - wrong password Few possible reasons for 4-way handshake failure that we can guess...

**Definition** wifi\_mgmt.h:423

[WIFI\_STATUS\_CONN\_FAIL](group__wifi__mgmt.md#gga86a5741e54aeb3e290142b0de217b8a8ab80ec4b70c75695fbe698034e2cb6a44)

@ WIFI\_STATUS\_CONN\_FAIL

Connection failed - generic failure.

**Definition** wifi\_mgmt.h:414

[WIFI\_STATUS\_CONN\_TIMEOUT](group__wifi__mgmt.md#gga86a5741e54aeb3e290142b0de217b8a8abb8783b92aec2ed1ffc6331979888563)

@ WIFI\_STATUS\_CONN\_TIMEOUT

Connection timed out.

**Definition** wifi\_mgmt.h:425

[WIFI\_STATUS\_DISCONN\_FIRST\_STATUS](group__wifi__mgmt.md#gga86a5741e54aeb3e290142b0de217b8a8abe1401e5d516c0d63291add15e558b18)

@ WIFI\_STATUS\_DISCONN\_FIRST\_STATUS

Connection disconnected status.

**Definition** wifi\_mgmt.h:431

[WIFI\_STATUS\_CONN\_LAST\_STATUS](group__wifi__mgmt.md#gga86a5741e54aeb3e290142b0de217b8a8aeee5fb8d8c3e7905554d08331f06191f)

@ WIFI\_STATUS\_CONN\_LAST\_STATUS

Last connection status.

**Definition** wifi\_mgmt.h:429

[NET\_REQUEST\_WIFI\_CMD\_AP\_CONFIG\_PARAM](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a14a0428720818c79df825d758e83f813)

@ NET\_REQUEST\_WIFI\_CMD\_AP\_CONFIG\_PARAM

Configure AP parameter.

**Definition** wifi\_mgmt.h:93

[NET\_REQUEST\_WIFI\_CMD\_TWT](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a1c9dc2d698326d987ffe5bfd35a9ed09)

@ NET\_REQUEST\_WIFI\_CMD\_TWT

Setup or teardown TWT flow.

**Definition** wifi\_mgmt.h:75

[NET\_REQUEST\_WIFI\_CMD\_PACKET\_FILTER](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a2579ace546bf6954c111eb5951e894f5)

@ NET\_REQUEST\_WIFI\_CMD\_PACKET\_FILTER

Set or get packet filter setting for current mode.

**Definition** wifi\_mgmt.h:83

[NET\_REQUEST\_WIFI\_CMD\_AP\_ENABLE](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a28267d33b555433271cb121d62194a4c)

@ NET\_REQUEST\_WIFI\_CMD\_AP\_ENABLE

Enable AP mode.

**Definition** wifi\_mgmt.h:67

[NET\_REQUEST\_WIFI\_CMD\_REG\_DOMAIN](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a367cc44caefd313e0c7ad3badc081456)

@ NET\_REQUEST\_WIFI\_CMD\_REG\_DOMAIN

Set or get regulatory domain.

**Definition** wifi\_mgmt.h:79

[NET\_REQUEST\_WIFI\_CMD\_SCAN](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a4aadf9114010c09bd7420c99a2049d5a)

@ NET\_REQUEST\_WIFI\_CMD\_SCAN

Scan for Wi-Fi networks.

**Definition** wifi\_mgmt.h:61

[NET\_REQUEST\_WIFI\_CMD\_IFACE\_STATUS](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a6af9d52df8f9db6393044e42e10ff0de)

@ NET\_REQUEST\_WIFI\_CMD\_IFACE\_STATUS

Get interface status.

**Definition** wifi\_mgmt.h:71

[NET\_REQUEST\_WIFI\_CMD\_AP\_STA\_DISCONNECT](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a6f3865aa6a4d7633e241ee2b002c1b5a)

@ NET\_REQUEST\_WIFI\_CMD\_AP\_STA\_DISCONNECT

Disconnect a STA from AP.

**Definition** wifi\_mgmt.h:87

[NET\_REQUEST\_WIFI\_CMD\_AP\_DISABLE](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a6fe9d7137b4cd20de880955b27382ccf)

@ NET\_REQUEST\_WIFI\_CMD\_AP\_DISABLE

Disable AP mode.

**Definition** wifi\_mgmt.h:69

[NET\_REQUEST\_WIFI\_CMD\_RTS\_THRESHOLD](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a7852cff28fc18ddd7af0f8224c840e7b)

@ NET\_REQUEST\_WIFI\_CMD\_RTS\_THRESHOLD

Set RTS threshold.

**Definition** wifi\_mgmt.h:91

[NET\_REQUEST\_WIFI\_CMD\_CONNECT](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a78c958877ee60c90803c925b6b2f057a)

@ NET\_REQUEST\_WIFI\_CMD\_CONNECT

Connect to a Wi-Fi network.

**Definition** wifi\_mgmt.h:63

[NET\_REQUEST\_WIFI\_CMD\_VERSION](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a7d9596f2cce54c9e050d89469e86eccb)

@ NET\_REQUEST\_WIFI\_CMD\_VERSION

Get Wi-Fi driver and Firmware versions.

**Definition** wifi\_mgmt.h:89

[NET\_REQUEST\_WIFI\_CMD\_CHANNEL](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77aade3d7a43c730a52f7876c6486170bb2)

@ NET\_REQUEST\_WIFI\_CMD\_CHANNEL

Set or get Wi-Fi channel for Monitor or TX-Injection mode.

**Definition** wifi\_mgmt.h:85

[NET\_REQUEST\_WIFI\_CMD\_MODE](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77ab7183584bdf5fe673d39fa0d090e3899)

@ NET\_REQUEST\_WIFI\_CMD\_MODE

Set or get Mode of operation.

**Definition** wifi\_mgmt.h:81

[NET\_REQUEST\_WIFI\_CMD\_PS](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77abf9fb93c205fa36f74a9ef19d3d0351a)

@ NET\_REQUEST\_WIFI\_CMD\_PS

Set power save status.

**Definition** wifi\_mgmt.h:73

[NET\_REQUEST\_WIFI\_CMD\_DISCONNECT](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77ac33941da138b993f7a1158d91469bcb7)

@ NET\_REQUEST\_WIFI\_CMD\_DISCONNECT

Disconnect from a Wi-Fi network.

**Definition** wifi\_mgmt.h:65

[NET\_REQUEST\_WIFI\_CMD\_PS\_CONFIG](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77ae6ce1c605d1bf7c09650ec15d74e77e9)

@ NET\_REQUEST\_WIFI\_CMD\_PS\_CONFIG

Get power save config.

**Definition** wifi\_mgmt.h:77

[WIFI\_STATUS\_AP\_CHANNEL\_NOT\_ALLOWED](group__wifi__mgmt.md#ggaaf730bf76adc06434c7ac63bf0417884a0b1cb592c54c16e8a54defee71c5fd15)

@ WIFI\_STATUS\_AP\_CHANNEL\_NOT\_ALLOWED

AP mode enable failed - channel not allowed.

**Definition** wifi\_mgmt.h:461

[WIFI\_STATUS\_AP\_SUCCESS](group__wifi__mgmt.md#ggaaf730bf76adc06434c7ac63bf0417884a0df52848da8735892d0eb1e381b2cd7c)

@ WIFI\_STATUS\_AP\_SUCCESS

AP mode enable or disable successful.

**Definition** wifi\_mgmt.h:455

[WIFI\_STATUS\_AP\_OP\_NOT\_SUPPORTED](group__wifi__mgmt.md#ggaaf730bf76adc06434c7ac63bf0417884a2105e6c49b3bcb5f7dcacbc1e5ce9cca)

@ WIFI\_STATUS\_AP\_OP\_NOT\_SUPPORTED

AP mode enable failed - operation not supported.

**Definition** wifi\_mgmt.h:467

[WIFI\_STATUS\_AP\_OP\_NOT\_PERMITTED](group__wifi__mgmt.md#ggaaf730bf76adc06434c7ac63bf0417884a36a58980bdc7877c910441590137ddbe)

@ WIFI\_STATUS\_AP\_OP\_NOT\_PERMITTED

AP mode enable failed - operation not permitted.

**Definition** wifi\_mgmt.h:469

[WIFI\_STATUS\_AP\_CHANNEL\_NOT\_SUPPORTED](group__wifi__mgmt.md#ggaaf730bf76adc06434c7ac63bf0417884a5acb85a2361ca72ed10966b829c5753b)

@ WIFI\_STATUS\_AP\_CHANNEL\_NOT\_SUPPORTED

AP mode enable failed - channel not supported.

**Definition** wifi\_mgmt.h:459

[WIFI\_STATUS\_AP\_FAIL](group__wifi__mgmt.md#ggaaf730bf76adc06434c7ac63bf0417884a6c6801381caa3862004662169202fa9a)

@ WIFI\_STATUS\_AP\_FAIL

AP mode enable or disable failed - generic failure.

**Definition** wifi\_mgmt.h:457

[WIFI\_STATUS\_AP\_AUTH\_TYPE\_NOT\_SUPPORTED](group__wifi__mgmt.md#ggaaf730bf76adc06434c7ac63bf0417884abe5a626d22051522255d98fdfdfbfcc8)

@ WIFI\_STATUS\_AP\_AUTH\_TYPE\_NOT\_SUPPORTED

AP mode enable failed - authentication type not supported.

**Definition** wifi\_mgmt.h:465

[WIFI\_STATUS\_AP\_SSID\_NOT\_ALLOWED](group__wifi__mgmt.md#ggaaf730bf76adc06434c7ac63bf0417884ac18a7b551f8c6bb7737b0e8e60c323ce)

@ WIFI\_STATUS\_AP\_SSID\_NOT\_ALLOWED

AP mode enable failed - SSID not allowed.

**Definition** wifi\_mgmt.h:463

[NET\_EVENT\_WIFI\_CMD\_AP\_STA\_DISCONNECTED](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8a3678a39f9542968958b5575d571d4e2e)

@ NET\_EVENT\_WIFI\_CMD\_AP\_STA\_DISCONNECTED

STA disconnected from AP.

**Definition** wifi\_mgmt.h:230

[NET\_EVENT\_WIFI\_CMD\_SCAN\_RESULT](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8a37e9ab2a6832153fa968337d920e587e)

@ NET\_EVENT\_WIFI\_CMD\_SCAN\_RESULT

Scan results available.

**Definition** wifi\_mgmt.h:204

[NET\_EVENT\_WIFI\_CMD\_DISCONNECT\_RESULT](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8a3a3b0387f83d8fb24a0e27312468b0eb)

@ NET\_EVENT\_WIFI\_CMD\_DISCONNECT\_RESULT

Disconnect result.

**Definition** wifi\_mgmt.h:210

[NET\_EVENT\_WIFI\_CMD\_TWT\_SLEEP\_STATE](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8a78838bf7ce80cee5e803712cd0286750)

@ NET\_EVENT\_WIFI\_CMD\_TWT\_SLEEP\_STATE

TWT sleep status: awake or sleeping, can be used by application to determine if it can send data or n...

**Definition** wifi\_mgmt.h:218

[NET\_EVENT\_WIFI\_CMD\_AP\_ENABLE\_RESULT](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8abd1797564427886eeb14dd293ae86a9b)

@ NET\_EVENT\_WIFI\_CMD\_AP\_ENABLE\_RESULT

AP mode enable result.

**Definition** wifi\_mgmt.h:224

[NET\_EVENT\_WIFI\_CMD\_AP\_STA\_CONNECTED](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8abd4269b2cd1302ce61da4f8d7bb9d5fb)

@ NET\_EVENT\_WIFI\_CMD\_AP\_STA\_CONNECTED

STA connected to AP.

**Definition** wifi\_mgmt.h:228

[NET\_EVENT\_WIFI\_CMD\_SCAN\_DONE](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8ad753b7e4588257815f4a60a539ca2018)

@ NET\_EVENT\_WIFI\_CMD\_SCAN\_DONE

Scan done.

**Definition** wifi\_mgmt.h:206

[NET\_EVENT\_WIFI\_CMD\_TWT](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8adad71603ed829ed92d06f8c40efa9b18)

@ NET\_EVENT\_WIFI\_CMD\_TWT

TWT events.

**Definition** wifi\_mgmt.h:214

[NET\_EVENT\_WIFI\_CMD\_RAW\_SCAN\_RESULT](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8addf15c69512be7ab4957e7c0b3fde0ac)

@ NET\_EVENT\_WIFI\_CMD\_RAW\_SCAN\_RESULT

Raw scan results available.

**Definition** wifi\_mgmt.h:220

[NET\_EVENT\_WIFI\_CMD\_AP\_DISABLE\_RESULT](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8aeec3d7a9191280c2326034a17555308d)

@ NET\_EVENT\_WIFI\_CMD\_AP\_DISABLE\_RESULT

AP mode disable result.

**Definition** wifi\_mgmt.h:226

[NET\_EVENT\_WIFI\_CMD\_DISCONNECT\_COMPLETE](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8af1c42bd59f01260c64ede07da436c18f)

@ NET\_EVENT\_WIFI\_CMD\_DISCONNECT\_COMPLETE

Disconnect complete.

**Definition** wifi\_mgmt.h:222

[NET\_EVENT\_WIFI\_CMD\_IFACE\_STATUS](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8af4b3f1969b96f63253851c26c3882a14)

@ NET\_EVENT\_WIFI\_CMD\_IFACE\_STATUS

Interface status.

**Definition** wifi\_mgmt.h:212

[NET\_EVENT\_WIFI\_CMD\_CONNECT\_RESULT](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8af76f28777b91b365dc3f97028bc18e3c)

@ NET\_EVENT\_WIFI\_CMD\_CONNECT\_RESULT

Connect result.

**Definition** wifi\_mgmt.h:208

[WIFI\_REASON\_DISCONN\_INACTIVITY](group__wifi__mgmt.md#ggac782af0a60b202fd19597cabb7bd3a9aa05fe2f87de30de47ee48f7615c2206e6)

@ WIFI\_REASON\_DISCONN\_INACTIVITY

Disconnected due to inactivity.

**Definition** wifi\_mgmt.h:447

[WIFI\_REASON\_DISCONN\_AP\_LEAVING](group__wifi__mgmt.md#ggac782af0a60b202fd19597cabb7bd3a9aa34e3f78ce43db3daeaf32038e0baf204)

@ WIFI\_REASON\_DISCONN\_AP\_LEAVING

Disconnected due to AP leaving.

**Definition** wifi\_mgmt.h:445

[WIFI\_REASON\_DISCONN\_SUCCESS](group__wifi__mgmt.md#ggac782af0a60b202fd19597cabb7bd3a9aa5c894399db8949a789ca4f5750b6f042)

@ WIFI\_REASON\_DISCONN\_SUCCESS

Success, overload status as reason.

**Definition** wifi\_mgmt.h:439

[WIFI\_REASON\_DISCONN\_UNSPECIFIED](group__wifi__mgmt.md#ggac782af0a60b202fd19597cabb7bd3a9aa87f5d64a9fd3acf8d67c698199779e5c)

@ WIFI\_REASON\_DISCONN\_UNSPECIFIED

Unspecified reason.

**Definition** wifi\_mgmt.h:441

[WIFI\_REASON\_DISCONN\_USER\_REQUEST](group__wifi__mgmt.md#ggac782af0a60b202fd19597cabb7bd3a9aaee75adafb52bd6ecaa547a76c6ccd0a7)

@ WIFI\_REASON\_DISCONN\_USER\_REQUEST

Disconnected due to user request.

**Definition** wifi\_mgmt.h:443

[WIFI\_MGMT\_GET](group__wifi__mgmt.md#ggae129d0783276e662575af2314eef86cda6b8183a773e0cdfa85bc4b41ae70fdcd)

@ WIFI\_MGMT\_GET

Get operation.

**Definition** wifi\_mgmt.h:639

[WIFI\_MGMT\_SET](group__wifi__mgmt.md#ggae129d0783276e662575af2314eef86cdaa0d5931c8275a8d3288ab668b6dfb5a1)

@ WIFI\_MGMT\_SET

Set operation.

**Definition** wifi\_mgmt.h:641

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

**Definition** device.h:403

[ethernet\_api](structethernet__api.md)

Ethernet L2 API operations.

**Definition** ethernet.h:526

[net\_if](structnet__if.md)

Network Interface structure.

**Definition** net\_if.h:678

[net\_stats\_wifi](structnet__stats__wifi.md)

All Wi-Fi specific statistics.

**Definition** net\_stats.h:603

[net\_wifi\_mgmt\_offload](structnet__wifi__mgmt__offload.md)

Wi-Fi management offload API.

**Definition** wifi\_mgmt.h:955

[net\_wifi\_mgmt\_offload::wifi\_iface](structnet__wifi__mgmt__offload.md#a1d34a954a2f16d29f51dc51dd6fbb845)

struct ethernet\_api wifi\_iface

Mandatory to get in first position.

**Definition** wifi\_mgmt.h:964

[net\_wifi\_mgmt\_offload::wifi\_mgmt\_api](structnet__wifi__mgmt__offload.md#a98fcc053d9820d2d981ed659520c9b3b)

const struct wifi\_mgmt\_ops \*const wifi\_mgmt\_api

Wi-Fi management API.

**Definition** wifi\_mgmt.h:970

[net\_wifi\_mgmt\_offload::wifi\_drv\_ops](structnet__wifi__mgmt__offload.md#a991e0bc6247578a3d1c9d2d3ab0b63d7)

const void \* wifi\_drv\_ops

Wi-Fi supplicant driver API.

**Definition** wifi\_mgmt.h:974

[offloaded\_if\_api](structoffloaded__if__api.md)

Extended net\_if\_api for offloaded ifaces/network devices, allowing handling of admin up/down state ch...

**Definition** offloaded\_netdev.h:51

[wifi\_ap\_config\_params](structwifi__ap__config__params.md)

Wi-Fi AP configuration parameter.

**Definition** wifi\_mgmt.h:762

[wifi\_ap\_config\_params::max\_inactivity](structwifi__ap__config__params.md#a289866d9209450e893281b4c198a546a)

uint32\_t max\_inactivity

Parameter used for setting maximum inactivity duration for stations.

**Definition** wifi\_mgmt.h:766

[wifi\_ap\_config\_params::type](structwifi__ap__config__params.md#a4c391cf504a994ed0bc4971afdf76774)

enum wifi\_ap\_config\_param type

Parameter used to identify the different AP parameters.

**Definition** wifi\_mgmt.h:764

[wifi\_ap\_config\_params::max\_num\_sta](structwifi__ap__config__params.md#a7fc0fad99f53ed8e1ac40b74ec98bf9a)

uint32\_t max\_num\_sta

Parameter used for setting maximum number of stations.

**Definition** wifi\_mgmt.h:768

[wifi\_ap\_sta\_info](structwifi__ap__sta__info.md)

AP mode - connected STA details.

**Definition** wifi\_mgmt.h:698

[wifi\_ap\_sta\_info::mac](structwifi__ap__sta__info.md#a2a2fc109525e72ee7f18cced3b881107)

uint8\_t mac[6]

MAC address.

**Definition** wifi\_mgmt.h:702

[wifi\_ap\_sta\_info::link\_mode](structwifi__ap__sta__info.md#a7d8bd52340d4937a4b5b7d2c00662441)

enum wifi\_link\_mode link\_mode

Link mode, see enum wifi\_link\_mode.

**Definition** wifi\_mgmt.h:700

[wifi\_ap\_sta\_info::mac\_length](structwifi__ap__sta__info.md#a7f7c8b144bb3464af5213708591eefda)

uint8\_t mac\_length

MAC address length.

**Definition** wifi\_mgmt.h:704

[wifi\_ap\_sta\_info::twt\_capable](structwifi__ap__sta__info.md#a838c9a4288c9bc7e97afe2334c678f34)

bool twt\_capable

is TWT capable ?

**Definition** wifi\_mgmt.h:706

[wifi\_band\_channel](structwifi__band__channel.md)

Wi-Fi structure to uniquely identify a band-channel pair.

**Definition** wifi\_mgmt.h:296

[wifi\_band\_channel::band](structwifi__band__channel.md#a4a932599429f37231f76c3064ec5efb3)

uint8\_t band

Frequency band.

**Definition** wifi\_mgmt.h:298

[wifi\_band\_channel::channel](structwifi__band__channel.md#acd0dd7366de3650124dad7232a58ade0)

uint8\_t channel

Channel.

**Definition** wifi\_mgmt.h:300

[wifi\_channel\_info](structwifi__channel__info.md)

Wi-Fi channel setting for monitor and TX-injection modes.

**Definition** wifi\_mgmt.h:748

[wifi\_channel\_info::if\_index](structwifi__channel__info.md#a43a7dd8c19d0c6540e3cc0b5d1d6165d)

uint8\_t if\_index

Interface index.

**Definition** wifi\_mgmt.h:752

[wifi\_channel\_info::channel](structwifi__channel__info.md#a799cbc0a67764f6680322ba0f2ad3300)

uint16\_t channel

Channel value to set.

**Definition** wifi\_mgmt.h:750

[wifi\_channel\_info::oper](structwifi__channel__info.md#aa8ef8a71b49ead3664fff9a4d61b1ce8)

enum wifi\_mgmt\_op oper

Get or set operation.

**Definition** wifi\_mgmt.h:754

[wifi\_connect\_req\_params](structwifi__connect__req__params.md)

Wi-Fi connect request parameters.

**Definition** wifi\_mgmt.h:380

[wifi\_connect\_req\_params::security](structwifi__connect__req__params.md#a18dce6bb021086877a30e7a04f5b24b9)

enum wifi\_security\_type security

Security type.

**Definition** wifi\_mgmt.h:398

[wifi\_connect\_req\_params::sae\_password](structwifi__connect__req__params.md#a469fac5758b78fc425911837930b2060)

const uint8\_t \* sae\_password

SAE password (same as PSK but with no length restrictions), optional.

**Definition** wifi\_mgmt.h:390

[wifi\_connect\_req\_params::bssid](structwifi__connect__req__params.md#a4d2356cf5eb3bbd51587ec5f3a1a065c)

uint8\_t bssid[6]

BSSID.

**Definition** wifi\_mgmt.h:402

[wifi\_connect\_req\_params::channel](structwifi__connect__req__params.md#a52b6d0323c35d03ec239f40be35cae72)

uint8\_t channel

Channel.

**Definition** wifi\_mgmt.h:396

[wifi\_connect\_req\_params::ssid\_length](structwifi__connect__req__params.md#a547dddf6be5dd77eda74b1085a798400)

uint8\_t ssid\_length

SSID length.

**Definition** wifi\_mgmt.h:384

[wifi\_connect\_req\_params::timeout](structwifi__connect__req__params.md#a56183ba7f4d8eaf5fc5b495856adecfd)

int timeout

Connect timeout in seconds, SYS\_FOREVER\_MS for no timeout.

**Definition** wifi\_mgmt.h:404

[wifi\_connect\_req\_params::mfp](structwifi__connect__req__params.md#a745b3416172672a7e5b12bcc5b55e88c)

enum wifi\_mfp\_options mfp

MFP options.

**Definition** wifi\_mgmt.h:400

[wifi\_connect\_req\_params::sae\_password\_length](structwifi__connect__req__params.md#a74f0819e7a546ffb8bfb0ec587eccf20)

uint8\_t sae\_password\_length

SAE password length.

**Definition** wifi\_mgmt.h:392

[wifi\_connect\_req\_params::band](structwifi__connect__req__params.md#aa2fea1881a8ffdf5d7093ae295867f3e)

uint8\_t band

Frequency band.

**Definition** wifi\_mgmt.h:394

[wifi\_connect\_req\_params::psk](structwifi__connect__req__params.md#aa7743f0ecbc27a9595720ce13ce57c1d)

const uint8\_t \* psk

Pre-shared key.

**Definition** wifi\_mgmt.h:386

[wifi\_connect\_req\_params::psk\_length](structwifi__connect__req__params.md#aaf7455a65590d19f047214b459a2dcb9)

uint8\_t psk\_length

Pre-shared key length.

**Definition** wifi\_mgmt.h:388

[wifi\_connect\_req\_params::ssid](structwifi__connect__req__params.md#ac260c2cd17a3f36ea101edaf23d41083)

const uint8\_t \* ssid

SSID.

**Definition** wifi\_mgmt.h:382

[wifi\_filter\_info](structwifi__filter__info.md)

Wi-Fi filter setting for monitor, prmoiscuous, TX-injection modes.

**Definition** wifi\_mgmt.h:736

[wifi\_filter\_info::buffer\_size](structwifi__filter__info.md#a1b2d0448fc7f62654e3f5aacfba62f8f)

uint16\_t buffer\_size

Filter buffer size.

**Definition** wifi\_mgmt.h:742

[wifi\_filter\_info::filter](structwifi__filter__info.md#ad9560be814299055cfa11b995a7dcf42)

uint8\_t filter

Filter setting.

**Definition** wifi\_mgmt.h:738

[wifi\_filter\_info::oper](structwifi__filter__info.md#aedd5e220cdde5768cb0f4aff920971cd)

enum wifi\_mgmt\_op oper

Get or set operation.

**Definition** wifi\_mgmt.h:744

[wifi\_filter\_info::if\_index](structwifi__filter__info.md#af9ea91e31e78afcb7ffe1ff9a04277a3)

uint8\_t if\_index

Interface index.

**Definition** wifi\_mgmt.h:740

[wifi\_iface\_status](structwifi__iface__status.md)

Wi-Fi interface status.

**Definition** wifi\_mgmt.h:487

[wifi\_iface\_status::beacon\_interval](structwifi__iface__status.md#a241bfbe70628006b515b5f9e4f97665c)

unsigned short beacon\_interval

Beacon interval.

**Definition** wifi\_mgmt.h:513

[wifi\_iface\_status::bssid](structwifi__iface__status.md#a28afad15fc6689669c7b19337a64eaf3)

char bssid[6]

BSSID.

**Definition** wifi\_mgmt.h:495

[wifi\_iface\_status::ssid](structwifi__iface__status.md#a30c4bef4e061346ba61857a558640d00)

char ssid[32]

SSID.

**Definition** wifi\_mgmt.h:493

[wifi\_iface\_status::rssi](structwifi__iface__status.md#a4e593147b88eb4938d55a4de72fcc7f6)

int rssi

RSSI.

**Definition** wifi\_mgmt.h:509

[wifi\_iface\_status::security](structwifi__iface__status.md#a625ecec1abec8dd65cf155eab21a01b5)

enum wifi\_security\_type security

Security type, see enum wifi\_security\_type.

**Definition** wifi\_mgmt.h:505

[wifi\_iface\_status::channel](structwifi__iface__status.md#a6432663156e5b2c424d254ed1eae0144)

unsigned int channel

Channel.

**Definition** wifi\_mgmt.h:499

[wifi\_iface\_status::mfp](structwifi__iface__status.md#aa1a9b644fd355526125ddd32416b7c24)

enum wifi\_mfp\_options mfp

MFP options, see enum wifi\_mfp\_options.

**Definition** wifi\_mgmt.h:507

[wifi\_iface\_status::dtim\_period](structwifi__iface__status.md#aae6c8cbaa16c81d308f08114d5103a3d)

unsigned char dtim\_period

DTIM period.

**Definition** wifi\_mgmt.h:511

[wifi\_iface\_status::state](structwifi__iface__status.md#ac52806155be3d64954ac6d109e76ec57)

int state

Interface state, see enum wifi\_iface\_state.

**Definition** wifi\_mgmt.h:489

[wifi\_iface\_status::twt\_capable](structwifi__iface__status.md#acfde8d64b463a9f553aa4fb689dc1917)

bool twt\_capable

is TWT capable?

**Definition** wifi\_mgmt.h:515

[wifi\_iface\_status::iface\_mode](structwifi__iface__status.md#ad33d2ec149a8d556e2472dd842ceadc0)

enum wifi\_iface\_mode iface\_mode

Interface mode, see enum wifi\_iface\_mode.

**Definition** wifi\_mgmt.h:501

[wifi\_iface\_status::ssid\_len](structwifi__iface__status.md#ad82f281941e4f6ce1ef0bca008e26d41)

unsigned int ssid\_len

SSID length.

**Definition** wifi\_mgmt.h:491

[wifi\_iface\_status::band](structwifi__iface__status.md#ae1c141a18f4e225af2c22a8cb4f882a8)

enum wifi\_frequency\_bands band

Frequency band.

**Definition** wifi\_mgmt.h:497

[wifi\_iface\_status::link\_mode](structwifi__iface__status.md#ae2de076d79f2172793d65fe9cd31edc4)

enum wifi\_link\_mode link\_mode

Link mode, see enum wifi\_link\_mode.

**Definition** wifi\_mgmt.h:503

[wifi\_mgmt\_ops](structwifi__mgmt__ops.md)

Wi-Fi management API.

**Definition** wifi\_mgmt.h:794

[wifi\_mgmt\_ops::reg\_domain](structwifi__mgmt__ops.md#a0a287c8acf2d7bf9333b755589294881)

int(\* reg\_domain)(const struct device \*dev, struct wifi\_reg\_domain \*reg\_domain)

Set or get regulatory domain.

**Definition** wifi\_mgmt.h:898

[wifi\_mgmt\_ops::ap\_config\_params](structwifi__mgmt__ops.md#a2475f32afcce72464b2db6ecad7fb3eb)

int(\* ap\_config\_params)(const struct device \*dev, struct wifi\_ap\_config\_params \*params)

Configure AP parameter.

**Definition** wifi\_mgmt.h:951

[wifi\_mgmt\_ops::scan](structwifi__mgmt__ops.md#a267030c27da3cdc251badd0ed7f7b1cb)

int(\* scan)(const struct device \*dev, struct wifi\_scan\_params \*params, scan\_result\_cb\_t cb)

Scan for Wi-Fi networks.

**Definition** wifi\_mgmt.h:806

[wifi\_mgmt\_ops::set\_rts\_threshold](structwifi__mgmt__ops.md#a514e06d63bcf6dc11dba1d3af8d102d5)

int(\* set\_rts\_threshold)(const struct device \*dev, unsigned int rts\_threshold)

Set RTS threshold value.

**Definition** wifi\_mgmt.h:943

[wifi\_mgmt\_ops::get\_power\_save\_config](structwifi__mgmt__ops.md#a52690b13f8a1e7b0c2302eaa24ae4c7f)

int(\* get\_power\_save\_config)(const struct device \*dev, struct wifi\_ps\_config \*config)

Get power save config.

**Definition** wifi\_mgmt.h:890

[wifi\_mgmt\_ops::disconnect](structwifi__mgmt__ops.md#a5725c6fd93ae189a3019374cd4ad2ff4)

int(\* disconnect)(const struct device \*dev)

Disconnect from a Wi-Fi network.

**Definition** wifi\_mgmt.h:824

[wifi\_mgmt\_ops::ap\_disable](structwifi__mgmt__ops.md#a5aa7a2be82eb1783872abda2b8978235)

int(\* ap\_disable)(const struct device \*dev)

Disable AP mode.

**Definition** wifi\_mgmt.h:840

[wifi\_mgmt\_ops::get\_stats](structwifi__mgmt__ops.md#a5e6fdf836273fcde54efff4c77bfdf0e)

int(\* get\_stats)(const struct device \*dev, struct net\_stats\_wifi \*stats)

Get Wi-Fi statistics.

**Definition** wifi\_mgmt.h:865

[wifi\_mgmt\_ops::get\_version](structwifi__mgmt__ops.md#aa7e4bc3dbc960091d11ffe5454259885)

int(\* get\_version)(const struct device \*dev, struct wifi\_version \*params)

Get Version of WiFi driver and Firmware.

**Definition** wifi\_mgmt.h:935

[wifi\_mgmt\_ops::set\_twt](structwifi__mgmt__ops.md#ab4500534b6abe0449290c8bd8f729fc4)

int(\* set\_twt)(const struct device \*dev, struct wifi\_twt\_params \*params)

Setup or teardown TWT flow.

**Definition** wifi\_mgmt.h:882

[wifi\_mgmt\_ops::set\_power\_save](structwifi__mgmt__ops.md#ac0f3f7fa699b1bc7db2358e77dd44cc4)

int(\* set\_power\_save)(const struct device \*dev, struct wifi\_ps\_params \*params)

Set power save status.

**Definition** wifi\_mgmt.h:874

[wifi\_mgmt\_ops::ap\_enable](structwifi__mgmt__ops.md#ac2ce3a4a86c43e30d33261f71c44198a)

int(\* ap\_enable)(const struct device \*dev, struct wifi\_connect\_req\_params \*params)

Enable AP mode.

**Definition** wifi\_mgmt.h:832

[wifi\_mgmt\_ops::filter](structwifi__mgmt__ops.md#ad645276745ce8dd9685e0744efdfc733)

int(\* filter)(const struct device \*dev, struct wifi\_filter\_info \*filter)

Set or get packet filter settings for monitor and promiscuous modes.

**Definition** wifi\_mgmt.h:906

[wifi\_mgmt\_ops::iface\_status](structwifi__mgmt__ops.md#adf157476d776bc9c068e99e1a0266fd3)

int(\* iface\_status)(const struct device \*dev, struct wifi\_iface\_status \*status)

Get interface status.

**Definition** wifi\_mgmt.h:856

[wifi\_mgmt\_ops::mode](structwifi__mgmt__ops.md#ae2fb1bc35bf9255655a30a2ad8588b7c)

int(\* mode)(const struct device \*dev, struct wifi\_mode\_info \*mode)

Set or get mode of operation.

**Definition** wifi\_mgmt.h:914

[wifi\_mgmt\_ops::connect](structwifi__mgmt__ops.md#ae6255ea77739918797b4f3c7a4634a75)

int(\* connect)(const struct device \*dev, struct wifi\_connect\_req\_params \*params)

Connect to a Wi-Fi network.

**Definition** wifi\_mgmt.h:816

[wifi\_mgmt\_ops::ap\_sta\_disconnect](structwifi__mgmt__ops.md#af01aaec29be78c02314acf13b5c1b6f7)

int(\* ap\_sta\_disconnect)(const struct device \*dev, const uint8\_t \*mac)

Disconnect a STA from AP.

**Definition** wifi\_mgmt.h:848

[wifi\_mgmt\_ops::channel](structwifi__mgmt__ops.md#af17ddfea01d0ab478f6fd50b1c9d6015)

int(\* channel)(const struct device \*dev, struct wifi\_channel\_info \*channel)

Set or get current channel of operation.

**Definition** wifi\_mgmt.h:922

[wifi\_mode\_info](structwifi__mode__info.md)

Wi-Fi mode setup.

**Definition** wifi\_mgmt.h:726

[wifi\_mode\_info::oper](structwifi__mode__info.md#a57c101db8b81ab0ac5dd0a158057a64a)

enum wifi\_mgmt\_op oper

Get or set operation.

**Definition** wifi\_mgmt.h:732

[wifi\_mode\_info::mode](structwifi__mode__info.md#aa29d3b88fc718aa3ac05daf38974707d)

uint8\_t mode

Mode setting for a specific mode of operation.

**Definition** wifi\_mgmt.h:728

[wifi\_mode\_info::if\_index](structwifi__mode__info.md#add58dd3b45fd2ddaf684d1b0de81bef9)

uint8\_t if\_index

Interface index.

**Definition** wifi\_mgmt.h:730

[wifi\_ps\_config](structwifi__ps__config.md)

Wi-Fi power save configuration.

**Definition** wifi\_mgmt.h:627

[wifi\_ps\_config::ps\_params](structwifi__ps__config.md#a357aafc2dedda37755b1cb1fc07fe5a6)

struct wifi\_ps\_params ps\_params

Power save configuration.

**Definition** wifi\_mgmt.h:633

[wifi\_ps\_config::num\_twt\_flows](structwifi__ps__config.md#a9e83c10eaaa1d721cbc49b40aedb00df)

char num\_twt\_flows

Number of TWT flows.

**Definition** wifi\_mgmt.h:629

[wifi\_ps\_config::twt\_flows](structwifi__ps__config.md#ab7460f0f253b2d552e49e98e2c770967)

struct wifi\_twt\_flow\_info twt\_flows[WIFI\_MAX\_TWT\_FLOWS]

TWT flow details.

**Definition** wifi\_mgmt.h:631

[wifi\_ps\_params](structwifi__ps__params.md)

Wi-Fi power save parameters.

**Definition** wifi\_mgmt.h:519

[wifi\_ps\_params::mode](structwifi__ps__params.md#a5a022d89d43ecf2cd1f15fc72c0f2bed)

enum wifi\_ps\_mode mode

Wi-Fi power save mode.

**Definition** wifi\_mgmt.h:527

[wifi\_ps\_params::fail\_reason](structwifi__ps__params.md#a63fa2ee03bc4aefada61c298ee14336c)

enum wifi\_config\_ps\_param\_fail\_reason fail\_reason

Wi-Fi power save fail reason.

**Definition** wifi\_mgmt.h:540

[wifi\_ps\_params::wakeup\_mode](structwifi__ps__params.md#a7cb3e7fb7d9f8bd7c2cab41f879b3b66)

enum wifi\_ps\_wakeup\_mode wakeup\_mode

Wi-Fi power save wakeup mode.

**Definition** wifi\_mgmt.h:525

[wifi\_ps\_params::listen\_interval](structwifi__ps__params.md#a8510c799ab0c5825f1c6349f9799c62f)

unsigned short listen\_interval

Listen interval.

**Definition** wifi\_mgmt.h:523

[wifi\_ps\_params::enabled](structwifi__ps__params.md#abb22aaa45833ac130922204bd2fe841b)

enum wifi\_ps enabled

Power save state.

**Definition** wifi\_mgmt.h:521

[wifi\_ps\_params::timeout\_ms](structwifi__ps__params.md#ad963f1bf78dc271f08b73f3aadb36a91)

unsigned int timeout\_ms

Wi-Fi power save timeout.

**Definition** wifi\_mgmt.h:536

[wifi\_ps\_params::type](structwifi__ps__params.md#aef62e5bf6216bf4dc461efe71735c4bd)

enum wifi\_ps\_param\_type type

Wi-Fi power save type.

**Definition** wifi\_mgmt.h:538

[wifi\_raw\_scan\_result](structwifi__raw__scan__result.md)

Wi-Fi raw scan result.

**Definition** wifi\_mgmt.h:685

[wifi\_raw\_scan\_result::rssi](structwifi__raw__scan__result.md#a3f08580c6448a5fa28dd8a594fa7dad6)

int8\_t rssi

RSSI.

**Definition** wifi\_mgmt.h:687

[wifi\_raw\_scan\_result::data](structwifi__raw__scan__result.md#a5710e89199c147ce898602795f00aba3)

uint8\_t data[CONFIG\_WIFI\_MGMT\_RAW\_SCAN\_RESULT\_LENGTH]

Raw scan data.

**Definition** wifi\_mgmt.h:693

[wifi\_raw\_scan\_result::frame\_length](structwifi__raw__scan__result.md#a876966f469714eb481b42ccc8a63945c)

int frame\_length

Frame length.

**Definition** wifi\_mgmt.h:689

[wifi\_raw\_scan\_result::frequency](structwifi__raw__scan__result.md#aa2c7781882c6775616cbc8016b0842f6)

unsigned short frequency

Frequency.

**Definition** wifi\_mgmt.h:691

[wifi\_reg\_chan\_info](structwifi__reg__chan__info.md)

Per-channel regulatory attributes.

**Definition** wifi\_mgmt.h:648

[wifi\_reg\_chan\_info::center\_frequency](structwifi__reg__chan__info.md#a0addffc11ef29f50c01b700835e59930)

unsigned short center\_frequency

Center frequency in MHz.

**Definition** wifi\_mgmt.h:650

[wifi\_reg\_chan\_info::dfs](structwifi__reg__chan__info.md#a1ab137c142902d2de7d6be2626d7ac1f)

unsigned short dfs

Is a DFS channel.

**Definition** wifi\_mgmt.h:658

[wifi\_reg\_chan\_info::supported](structwifi__reg__chan__info.md#aa044611e18b7332b8577e29f6a769e3f)

unsigned short supported

Is channel supported or not.

**Definition** wifi\_mgmt.h:654

[wifi\_reg\_chan\_info::passive\_only](structwifi__reg__chan__info.md#acc7a88b004c9a61c8bf9ee1a97f85928)

unsigned short passive\_only

Passive transmissions only.

**Definition** wifi\_mgmt.h:656

[wifi\_reg\_chan\_info::max\_power](structwifi__reg__chan__info.md#af9169ab4a41fac4c6f6766fc96799545)

unsigned short max\_power

Maximum transmission power (in dBm).

**Definition** wifi\_mgmt.h:652

[wifi\_reg\_domain](structwifi__reg__domain.md)

Regulatory domain information or configuration.

**Definition** wifi\_mgmt.h:662

[wifi\_reg\_domain::num\_channels](structwifi__reg__domain.md#a3278e9f43893f49ab9f9d0d7f24009c1)

unsigned int num\_channels

Number of channels supported.

**Definition** wifi\_mgmt.h:670

[wifi\_reg\_domain::oper](structwifi__reg__domain.md#a3bbfdf1497a87bbb6b6211c7035e1002)

enum wifi\_mgmt\_op oper

Regulatory domain operation.

**Definition** wifi\_mgmt.h:664

[wifi\_reg\_domain::chan\_info](structwifi__reg__domain.md#a4c8c9c11e41123cd7738fdb0d33ae5fb)

struct wifi\_reg\_chan\_info \* chan\_info

Channels information.

**Definition** wifi\_mgmt.h:672

[wifi\_reg\_domain::force](structwifi__reg__domain.md#a567c6fcae8032567aea83c18cd211c33)

bool force

Ignore all other regulatory hints over this one.

**Definition** wifi\_mgmt.h:666

[wifi\_reg\_domain::country\_code](structwifi__reg__domain.md#adfabbe25b049f0dd94c035a82c20a413)

uint8\_t country\_code[2]

Country code: ISO/IEC 3166-1 alpha-2.

**Definition** wifi\_mgmt.h:668

[wifi\_scan\_params](structwifi__scan__params.md)

Wi-Fi scan parameters structure.

**Definition** wifi\_mgmt.h:308

[wifi\_scan\_params::max\_bss\_cnt](structwifi__scan__params.md#a12d5dea7d8fa8ad03ac2366720c46243)

uint16\_t max\_bss\_cnt

Specifies the maximum number of scan results to return.

**Definition** wifi\_mgmt.h:337

[wifi\_scan\_params::dwell\_time\_active](structwifi__scan__params.md#a2453a75c23e04e3572559c0e7199c1b4)

uint16\_t dwell\_time\_active

Active scan dwell time (in ms) on a channel.

**Definition** wifi\_mgmt.h:323

[wifi\_scan\_params::scan\_type](structwifi__scan__params.md#a645acc54603cd4692527c1a028933078)

enum wifi\_scan\_type scan\_type

Scan type, see enum wifi\_scan\_type.

**Definition** wifi\_mgmt.h:316

[wifi\_scan\_params::bands](structwifi__scan__params.md#a6b571d960ed9d7419e31530e5fb6f97a)

uint8\_t bands

Bitmap of bands to be scanned.

**Definition** wifi\_mgmt.h:320

[wifi\_scan\_params::dwell\_time\_passive](structwifi__scan__params.md#a8e7a37ccda8de635e7b7066d7943e814)

uint16\_t dwell\_time\_passive

Passive scan dwell time (in ms) on a channel.

**Definition** wifi\_mgmt.h:326

[wifi\_scan\_params::band\_chan](structwifi__scan__params.md#aa5ddbd6bc97b7598288d4b0d38521681)

struct wifi\_band\_channel band\_chan[WIFI\_MGMT\_SCAN\_CHAN\_MAX\_MANUAL]

Channel information array indexed on Wi-Fi frequency bands and channels within that band.

**Definition** wifi\_mgmt.h:352

[wifi\_scan\_params::ssids](structwifi__scan__params.md#aac11ee8e0ec8a4fa24668f4820bd1a12)

const char \* ssids[WIFI\_MGMT\_SCAN\_SSID\_FILT\_MAX]

Array of SSID strings to scan.

**Definition** wifi\_mgmt.h:329

[wifi\_scan\_result](structwifi__scan__result.md)

Wi-Fi scan result, each result is provided to the net\_mgmt\_event\_callback via its info attribute (see...

**Definition** wifi\_mgmt.h:358

[wifi\_scan\_result::ssid\_length](structwifi__scan__result.md#a2c1c2f4265b914df08fc75deb8b69d39)

uint8\_t ssid\_length

SSID length.

**Definition** wifi\_mgmt.h:362

[wifi\_scan\_result::band](structwifi__scan__result.md#a38201c9dd798dc11b5bda3ce97b02e92)

uint8\_t band

Frequency band.

**Definition** wifi\_mgmt.h:364

[wifi\_scan\_result::rssi](structwifi__scan__result.md#a76aa012136e3721fd4a482a22b93546f)

int8\_t rssi

RSSI.

**Definition** wifi\_mgmt.h:372

[wifi\_scan\_result::ssid](structwifi__scan__result.md#a854e296bdb2a54cb31e90a8f856be079)

uint8\_t ssid[32]

SSID.

**Definition** wifi\_mgmt.h:360

[wifi\_scan\_result::mac\_length](structwifi__scan__result.md#a8fca0dabec00ebd7ed4800098ec9d451)

uint8\_t mac\_length

BSSID length.

**Definition** wifi\_mgmt.h:376

[wifi\_scan\_result::mac](structwifi__scan__result.md#a906e9b48ebd5c0a599221f32cc47cda6)

uint8\_t mac[6]

BSSID.

**Definition** wifi\_mgmt.h:374

[wifi\_scan\_result::mfp](structwifi__scan__result.md#acaa3fb30ebf6df22bfac6380698ed28e)

enum wifi\_mfp\_options mfp

MFP options.

**Definition** wifi\_mgmt.h:370

[wifi\_scan\_result::channel](structwifi__scan__result.md#adbbfd7692ee5ffd6344fe78b9d91c840)

uint8\_t channel

Channel.

**Definition** wifi\_mgmt.h:366

[wifi\_scan\_result::security](structwifi__scan__result.md#af2d3dc5d115e3db76d3bc115510b0a5a)

enum wifi\_security\_type security

Security type.

**Definition** wifi\_mgmt.h:368

[wifi\_status](structwifi__status.md)

Generic Wi-Fi status for commands and events.

**Definition** wifi\_mgmt.h:473

[wifi\_status::ap\_status](structwifi__status.md#a02f0fcc7ef57661ca95d0c99f045aef1)

enum wifi\_ap\_status ap\_status

Access point status.

**Definition** wifi\_mgmt.h:482

[wifi\_status::conn\_status](structwifi__status.md#a8f885e78366d0499e4ba8e15bef275ac)

enum wifi\_conn\_status conn\_status

Connection status.

**Definition** wifi\_mgmt.h:478

[wifi\_status::disconn\_reason](structwifi__status.md#aa04b5033d93274badd27f702af9830bc)

enum wifi\_disconn\_reason disconn\_reason

Disconnection reason status.

**Definition** wifi\_mgmt.h:480

[wifi\_status::status](structwifi__status.md#aa1dbff8154400f8353693d387977008b)

int status

Status value.

**Definition** wifi\_mgmt.h:476

[wifi\_twt\_flow\_info](structwifi__twt__flow__info.md)

Wi-Fi TWT flow information.

**Definition** wifi\_mgmt.h:603

[wifi\_twt\_flow\_info::dialog\_token](structwifi__twt__flow__info.md#a123ce10bed8b62b01919a7ea7644a0ba)

uint8\_t dialog\_token

Dialog token, used to map requests to responses.

**Definition** wifi\_mgmt.h:607

[wifi\_twt\_flow\_info::negotiation\_type](structwifi__twt__flow__info.md#a620ae8ba546e4091d74280cb1553b2cf)

enum wifi\_twt\_negotiation\_type negotiation\_type

TWT negotiation type, see enum wifi\_twt\_negotiation\_type.

**Definition** wifi\_mgmt.h:611

[wifi\_twt\_flow\_info::twt\_wake\_ahead\_duration](structwifi__twt__flow__info.md#a6384d3829d54a58a53eafcb74c64a658)

uint32\_t twt\_wake\_ahead\_duration

Wake ahead duration.

**Definition** wifi\_mgmt.h:623

[wifi\_twt\_flow\_info::trigger](structwifi__twt__flow__info.md#a952a67bd092c5dadba387bb13449c6f3)

bool trigger

Trigger enabled or disabled.

**Definition** wifi\_mgmt.h:615

[wifi\_twt\_flow\_info::responder](structwifi__twt__flow__info.md#ac82e4de8ffc82f851061f8ba8d217dc1)

bool responder

Requestor or responder.

**Definition** wifi\_mgmt.h:613

[wifi\_twt\_flow\_info::flow\_id](structwifi__twt__flow__info.md#acb0c618f1cebcb172f342cfe222683be)

uint8\_t flow\_id

Flow ID, used to map setup with teardown.

**Definition** wifi\_mgmt.h:609

[wifi\_twt\_flow\_info::twt\_interval](structwifi__twt__flow__info.md#ae15ba49fa54f82cc6a1fb0d4572114b7)

uint64\_t twt\_interval

Interval = Wake up time + Sleeping time.

**Definition** wifi\_mgmt.h:605

[wifi\_twt\_flow\_info::twt\_wake\_interval](structwifi__twt__flow__info.md#aede6cb0cfc999fac8ded49e2981a3762)

uint32\_t twt\_wake\_interval

Wake up time.

**Definition** wifi\_mgmt.h:621

[wifi\_twt\_flow\_info::implicit](structwifi__twt__flow__info.md#afb480be82d1c6f351bd634fd83bfa5c7)

bool implicit

Implicit or explicit.

**Definition** wifi\_mgmt.h:617

[wifi\_twt\_flow\_info::announce](structwifi__twt__flow__info.md#afc81a5111c265fd9bb2aca5f9510bfa8)

bool announce

Announced or unannounced.

**Definition** wifi\_mgmt.h:619

[wifi\_twt\_params](structwifi__twt__params.md)

Wi-Fi TWT parameters.

**Definition** wifi\_mgmt.h:544

[wifi\_twt\_params::announce](structwifi__twt__params.md#a02f2d822d530e5376f256503439a54f9)

bool announce

Announced or unannounced.

**Definition** wifi\_mgmt.h:571

[wifi\_twt\_params::teardown\_all](structwifi__twt__params.md#a26d6bda00452f77832f69f4465c13efb)

bool teardown\_all

Teardown all flows.

**Definition** wifi\_mgmt.h:584

[wifi\_twt\_params::setup\_cmd](structwifi__twt__params.md#a347f8cff73ee6b6ba6d15ddf6f376a2d)

enum wifi\_twt\_setup\_cmd setup\_cmd

TWT setup command, see enum wifi\_twt\_setup\_cmd.

**Definition** wifi\_mgmt.h:550

[wifi\_twt\_params::trigger](structwifi__twt__params.md#a4e822c04b52fe6a9489e48e26b8f9382)

bool trigger

Trigger enabled or disabled.

**Definition** wifi\_mgmt.h:567

[wifi\_twt\_params::negotiation\_type](structwifi__twt__params.md#a5fd269328f68838b8a7e3a0b93eed894)

enum wifi\_twt\_negotiation\_type negotiation\_type

TWT negotiation type, see enum wifi\_twt\_negotiation\_type.

**Definition** wifi\_mgmt.h:548

[wifi\_twt\_params::operation](structwifi__twt__params.md#a6f0483861a387651c9c89ba182e064bd)

enum wifi\_twt\_operation operation

TWT operation, see enum wifi\_twt\_operation.

**Definition** wifi\_mgmt.h:546

[wifi\_twt\_params::twt\_wake\_ahead\_duration](structwifi__twt__params.md#a6f907ca412251fdd7391f29bfa6d7713)

uint32\_t twt\_wake\_ahead\_duration

Wake ahead notification is sent earlier than TWT Service period (SP) start based on this duration.

**Definition** wifi\_mgmt.h:579

[wifi\_twt\_params::fail\_reason](structwifi__twt__params.md#a70f58b502bb67ef3b2068ded2160b612)

enum wifi\_twt\_fail\_reason fail\_reason

TWT fail reason, see enum wifi\_twt\_fail\_reason.

**Definition** wifi\_mgmt.h:588

[wifi\_twt\_params::twt\_wake\_interval](structwifi__twt__params.md#a7c297459a17ed2fd232c62cca63e952f)

uint32\_t twt\_wake\_interval

Wake up time.

**Definition** wifi\_mgmt.h:573

[wifi\_twt\_params::resp\_status](structwifi__twt__params.md#a805a23284ed4afa46b84efcd43329beb)

enum wifi\_twt\_setup\_resp\_status resp\_status

TWT setup response status, see enum wifi\_twt\_setup\_resp\_status.

**Definition** wifi\_mgmt.h:552

[wifi\_twt\_params::implicit](structwifi__twt__params.md#a8ea1e2501c8b69dc3fa606eb360f8678)

bool implicit

Implicit or explicit.

**Definition** wifi\_mgmt.h:569

[wifi\_twt\_params::flow\_id](structwifi__twt__params.md#a95ec4b32d37309efa47256ae1ea865da)

uint8\_t flow\_id

Flow ID, used to map setup with teardown.

**Definition** wifi\_mgmt.h:558

[wifi\_twt\_params::teardown\_status](structwifi__twt__params.md#a9faff59e577775b3fe53f2139462ac71)

enum wifi\_twt\_teardown\_status teardown\_status

TWT teardown cmd status, see enum wifi\_twt\_teardown\_status.

**Definition** wifi\_mgmt.h:554

[wifi\_twt\_params::twt\_interval](structwifi__twt__params.md#ab92fe571559fcd5d97cdf7e6b7d86681)

uint64\_t twt\_interval

Interval = Wake up time + Sleeping time.

**Definition** wifi\_mgmt.h:563

[wifi\_twt\_params::dialog\_token](structwifi__twt__params.md#adda47e302a87a766f18e28016963a561)

uint8\_t dialog\_token

Dialog token, used to map requests to responses.

**Definition** wifi\_mgmt.h:556

[wifi\_twt\_params::responder](structwifi__twt__params.md#ae547c6fc1c7cbad15bebcfdaa43f59e7)

bool responder

Requestor or responder.

**Definition** wifi\_mgmt.h:565

[wifi\_twt\_params::setup](structwifi__twt__params.md#aee57c0189b210cfcc18e213e35b9479c)

struct wifi\_twt\_params::@302311362167322044106272253111230157111235232263::@007355023165260313375314073015252271352275036053 setup

Setup specific parameters.

[wifi\_twt\_params::teardown](structwifi__twt__params.md#afdeebd8a27107a0e37282aa19e5149d0)

struct wifi\_twt\_params::@302311362167322044106272253111230157111235232263::@053165077055023247316045052326043107125356150312 teardown

Teardown specific parameters.

[wifi\_version](structwifi__version.md)

Wi-Fi version.

**Definition** wifi\_mgmt.h:286

[wifi\_version::fw\_version](structwifi__version.md#a4bf2cbdf5c43ff21718ccf19646c164e)

const char \* fw\_version

Firmware version.

**Definition** wifi\_mgmt.h:290

[wifi\_version::drv\_version](structwifi__version.md#aea828bdb512440d6aa3cc853525c4971)

const char \* drv\_version

Driver version.

**Definition** wifi\_mgmt.h:288

[wifi.h](wifi_8h.md)

IEEE 802.11 protocol and general Wi-Fi definitions.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [wifi\_mgmt.h](wifi__mgmt_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
