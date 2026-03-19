---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/wifi__mgmt_8h_source.html
original_path: doxygen/html/wifi__mgmt_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

wifi\_mgmt.h

[Go to the documentation of this file.](wifi__mgmt_8h.md)

1/\*

2 \* Copyright (c) 2017 Intel Corporation.

3 \* Copyright 2024 NXP

4 \* Copyright (c) 2024 Nordic Semiconductor ASA

5 \*

6 \* SPDX-License-Identifier: Apache-2.0

7 \*/

8

13

14#ifndef ZEPHYR\_INCLUDE\_NET\_WIFI\_MGMT\_H\_

15#define ZEPHYR\_INCLUDE\_NET\_WIFI\_MGMT\_H\_

16

17#include <[zephyr/net/net\_mgmt.h](net__mgmt_8h.md)>

18#include <[zephyr/net/wifi.h](wifi_8h.md)>

19#include <[zephyr/net/ethernet.h](ethernet_8h.md)>

20#include <[zephyr/net/offloaded\_netdev.h](offloaded__netdev_8h.md)>

21

22#ifdef \_\_cplusplus

23extern "C" {

24#endif

25

30

31/\* Management part definitions \*/

32

34

35#define \_NET\_WIFI\_LAYER NET\_MGMT\_LAYER\_L2

36#define \_NET\_WIFI\_CODE 0x156

37#define \_NET\_WIFI\_BASE (NET\_MGMT\_IFACE\_BIT | \

38 NET\_MGMT\_LAYER(\_NET\_WIFI\_LAYER) | \

39 NET\_MGMT\_LAYER\_CODE(\_NET\_WIFI\_CODE))

40#define \_NET\_WIFI\_EVENT (\_NET\_WIFI\_BASE | NET\_MGMT\_EVENT\_BIT)

41

42#ifdef CONFIG\_WIFI\_MGMT\_SCAN\_SSID\_FILT\_MAX

43#define WIFI\_MGMT\_SCAN\_SSID\_FILT\_MAX CONFIG\_WIFI\_MGMT\_SCAN\_SSID\_FILT\_MAX

44#else

45#define WIFI\_MGMT\_SCAN\_SSID\_FILT\_MAX 1

46#endif /\* CONFIG\_WIFI\_MGMT\_SCAN\_SSID\_FILT\_MAX \*/

47

48#ifdef CONFIG\_WIFI\_MGMT\_SCAN\_CHAN\_MAX\_MANUAL

49#define WIFI\_MGMT\_SCAN\_CHAN\_MAX\_MANUAL CONFIG\_WIFI\_MGMT\_SCAN\_CHAN\_MAX\_MANUAL

50#else

51#define WIFI\_MGMT\_SCAN\_CHAN\_MAX\_MANUAL 1

52#endif /\* CONFIG\_WIFI\_MGMT\_SCAN\_CHAN\_MAX\_MANUAL \*/

53

54#ifdef CONFIG\_WIFI\_ENT\_IDENTITY\_MAX\_USERS

55#define WIFI\_ENT\_IDENTITY\_MAX\_USERS CONFIG\_WIFI\_ENT\_IDENTITY\_MAX\_USERS

56#else

57#define WIFI\_ENT\_IDENTITY\_MAX\_USERS 1

58#endif /\* CONFIG\_WIFI\_ENT\_IDENTITY\_MAX\_USERS \*/

59

60#define WIFI\_MGMT\_BAND\_STR\_SIZE\_MAX 8

61#define WIFI\_MGMT\_SCAN\_MAX\_BSS\_CNT 65535

62

63#define WIFI\_MGMT\_SKIP\_INACTIVITY\_POLL IS\_ENABLED(CONFIG\_WIFI\_MGMT\_AP\_STA\_SKIP\_INACTIVITY\_POLL)

65

[ 67](group__wifi__mgmt.md#ga99a55137188119f65f9d2bb4f57cac77)enum [net\_request\_wifi\_cmd](group__wifi__mgmt.md#ga99a55137188119f65f9d2bb4f57cac77) {

[ 69](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a4aadf9114010c09bd7420c99a2049d5a) [NET\_REQUEST\_WIFI\_CMD\_SCAN](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a4aadf9114010c09bd7420c99a2049d5a) = 1,

[ 71](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a78c958877ee60c90803c925b6b2f057a) [NET\_REQUEST\_WIFI\_CMD\_CONNECT](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a78c958877ee60c90803c925b6b2f057a),

[ 73](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77ac33941da138b993f7a1158d91469bcb7) [NET\_REQUEST\_WIFI\_CMD\_DISCONNECT](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77ac33941da138b993f7a1158d91469bcb7),

[ 75](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a28267d33b555433271cb121d62194a4c) [NET\_REQUEST\_WIFI\_CMD\_AP\_ENABLE](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a28267d33b555433271cb121d62194a4c),

[ 77](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a6fe9d7137b4cd20de880955b27382ccf) [NET\_REQUEST\_WIFI\_CMD\_AP\_DISABLE](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a6fe9d7137b4cd20de880955b27382ccf),

[ 79](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a40104910a4d0258f63a03851de929474) [NET\_REQUEST\_WIFI\_CMD\_AP\_RTS\_THRESHOLD](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a40104910a4d0258f63a03851de929474),

[ 81](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a6af9d52df8f9db6393044e42e10ff0de) [NET\_REQUEST\_WIFI\_CMD\_IFACE\_STATUS](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a6af9d52df8f9db6393044e42e10ff0de),

[ 83](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77aa86fb7193245593dd84b3a4376bc25d6) [NET\_REQUEST\_WIFI\_CMD\_11K\_CONFIG](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77aa86fb7193245593dd84b3a4376bc25d6),

[ 85](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a48b3f0ec6647fb30d3b6456822c2dede) [NET\_REQUEST\_WIFI\_CMD\_11K\_NEIGHBOR\_REQUEST](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a48b3f0ec6647fb30d3b6456822c2dede),

[ 87](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77abf9fb93c205fa36f74a9ef19d3d0351a) [NET\_REQUEST\_WIFI\_CMD\_PS](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77abf9fb93c205fa36f74a9ef19d3d0351a),

[ 89](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a1c9dc2d698326d987ffe5bfd35a9ed09) [NET\_REQUEST\_WIFI\_CMD\_TWT](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a1c9dc2d698326d987ffe5bfd35a9ed09),

[ 91](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77aaf770b48056af1f9d6d99deb3772027d) [NET\_REQUEST\_WIFI\_CMD\_BTWT](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77aaf770b48056af1f9d6d99deb3772027d),

[ 93](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77ae6ce1c605d1bf7c09650ec15d74e77e9) [NET\_REQUEST\_WIFI\_CMD\_PS\_CONFIG](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77ae6ce1c605d1bf7c09650ec15d74e77e9),

[ 95](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a367cc44caefd313e0c7ad3badc081456) [NET\_REQUEST\_WIFI\_CMD\_REG\_DOMAIN](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a367cc44caefd313e0c7ad3badc081456),

[ 97](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77ab7183584bdf5fe673d39fa0d090e3899) [NET\_REQUEST\_WIFI\_CMD\_MODE](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77ab7183584bdf5fe673d39fa0d090e3899),

[ 99](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a2579ace546bf6954c111eb5951e894f5) [NET\_REQUEST\_WIFI\_CMD\_PACKET\_FILTER](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a2579ace546bf6954c111eb5951e894f5),

[ 101](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77aade3d7a43c730a52f7876c6486170bb2) [NET\_REQUEST\_WIFI\_CMD\_CHANNEL](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77aade3d7a43c730a52f7876c6486170bb2),

[ 103](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a6f3865aa6a4d7633e241ee2b002c1b5a) [NET\_REQUEST\_WIFI\_CMD\_AP\_STA\_DISCONNECT](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a6f3865aa6a4d7633e241ee2b002c1b5a),

[ 105](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a7d9596f2cce54c9e050d89469e86eccb) [NET\_REQUEST\_WIFI\_CMD\_VERSION](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a7d9596f2cce54c9e050d89469e86eccb),

[ 107](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77aa150f53621941796082e00090bde6a5a) [NET\_REQUEST\_WIFI\_CMD\_CONN\_PARAMS](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77aa150f53621941796082e00090bde6a5a),

[ 109](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a7852cff28fc18ddd7af0f8224c840e7b) [NET\_REQUEST\_WIFI\_CMD\_RTS\_THRESHOLD](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a7852cff28fc18ddd7af0f8224c840e7b),

[ 111](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a14a0428720818c79df825d758e83f813) [NET\_REQUEST\_WIFI\_CMD\_AP\_CONFIG\_PARAM](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a14a0428720818c79df825d758e83f813),

[ 113](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a6fc4d3aca344dc551dd62ae1d6072104) [NET\_REQUEST\_WIFI\_CMD\_DPP](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a6fc4d3aca344dc551dd62ae1d6072104),

[ 115](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77ab95b651107d819809cb5909dc25a5a56) [NET\_REQUEST\_WIFI\_CMD\_BTM\_QUERY](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77ab95b651107d819809cb5909dc25a5a56),

[ 117](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a1fec11ed98f0a9411eefda9e55ee9aad) [NET\_REQUEST\_WIFI\_CMD\_PMKSA\_FLUSH](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a1fec11ed98f0a9411eefda9e55ee9aad),

[ 119](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a94b7fb7a8c529082e1d0458298b6c3fb) [NET\_REQUEST\_WIFI\_CMD\_ENTERPRISE\_CREDS](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a94b7fb7a8c529082e1d0458298b6c3fb),

[ 121](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77ab7a4215540d2e6cda0d522dc621e9d89) [NET\_REQUEST\_WIFI\_CMD\_RTS\_THRESHOLD\_CONFIG](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77ab7a4215540d2e6cda0d522dc621e9d89),

[ 123](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77aec78bf6196abee310e06a8454d27eed7) [NET\_REQUEST\_WIFI\_CMD\_WPS\_CONFIG](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77aec78bf6196abee310e06a8454d27eed7),

124#ifdef CONFIG\_WIFI\_CREDENTIALS\_CONNECT\_STORED

126 NET\_REQUEST\_WIFI\_CMD\_CONNECT\_STORED,

127#endif

[ 129](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a286205d961a77e44cd98e7894c48e676) [NET\_REQUEST\_WIFI\_CMD\_START\_ROAMING](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a286205d961a77e44cd98e7894c48e676),

[ 131](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77ad950aa5b87408793f4df9c39fe84cc55) [NET\_REQUEST\_WIFI\_CMD\_NEIGHBOR\_REP\_COMPLETE](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77ad950aa5b87408793f4df9c39fe84cc55),

[ 133](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77ab7bc479691f88138972d0d8e1e2179ed) [NET\_REQUEST\_WIFI\_CMD\_CANDIDATE\_SCAN](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77ab7bc479691f88138972d0d8e1e2179ed),

[ 135](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77ae496f72d75179a2d10e9fb326259e413) [NET\_REQUEST\_WIFI\_CMD\_AP\_WPS\_CONFIG](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77ae496f72d75179a2d10e9fb326259e413),

137 NET\_REQUEST\_WIFI\_CMD\_MAX

139};

140

[ 142](group__wifi__mgmt.md#ga1c277da90986fa52dca182c4d922646f)#define NET\_REQUEST\_WIFI\_SCAN \

143 (\_NET\_WIFI\_BASE | NET\_REQUEST\_WIFI\_CMD\_SCAN)

144

145[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)([NET\_REQUEST\_WIFI\_SCAN](group__wifi__mgmt.md#ga1c277da90986fa52dca182c4d922646f));

146

[ 148](group__wifi__mgmt.md#gaa7ab2a97950a22736bb69f60b459f0f6)#define NET\_REQUEST\_WIFI\_CONNECT \

149 (\_NET\_WIFI\_BASE | NET\_REQUEST\_WIFI\_CMD\_CONNECT)

150

151[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)([NET\_REQUEST\_WIFI\_CONNECT](group__wifi__mgmt.md#gaa7ab2a97950a22736bb69f60b459f0f6));

152

[ 154](group__wifi__mgmt.md#ga90afd8d4e83056463ec6e667ed8ea60a)#define NET\_REQUEST\_WIFI\_DISCONNECT \

155 (\_NET\_WIFI\_BASE | NET\_REQUEST\_WIFI\_CMD\_DISCONNECT)

156

157[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)([NET\_REQUEST\_WIFI\_DISCONNECT](group__wifi__mgmt.md#ga90afd8d4e83056463ec6e667ed8ea60a));

158

[ 160](group__wifi__mgmt.md#ga638d2eb0a5029c1af46a91b523ed8589)#define NET\_REQUEST\_WIFI\_AP\_ENABLE \

161 (\_NET\_WIFI\_BASE | NET\_REQUEST\_WIFI\_CMD\_AP\_ENABLE)

162

163[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)([NET\_REQUEST\_WIFI\_AP\_ENABLE](group__wifi__mgmt.md#ga638d2eb0a5029c1af46a91b523ed8589));

164

[ 166](group__wifi__mgmt.md#gaf81f62bf4c9e331a095acbf0d24ca1a2)#define NET\_REQUEST\_WIFI\_AP\_DISABLE \

167 (\_NET\_WIFI\_BASE | NET\_REQUEST\_WIFI\_CMD\_AP\_DISABLE)

168

169[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)([NET\_REQUEST\_WIFI\_AP\_DISABLE](group__wifi__mgmt.md#gaf81f62bf4c9e331a095acbf0d24ca1a2));

170

[ 172](group__wifi__mgmt.md#ga9918582d4e7bb0952daf993ee34e166d)#define NET\_REQUEST\_WIFI\_AP\_RTS\_THRESHOLD \

173 (\_NET\_WIFI\_BASE | NET\_REQUEST\_WIFI\_CMD\_AP\_RTS\_THRESHOLD)

174

175[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)([NET\_REQUEST\_WIFI\_AP\_RTS\_THRESHOLD](group__wifi__mgmt.md#ga9918582d4e7bb0952daf993ee34e166d));

176

[ 178](group__wifi__mgmt.md#ga3e45f6ee3801553619d8eb7d0af506eb)#define NET\_REQUEST\_WIFI\_IFACE\_STATUS \

179 (\_NET\_WIFI\_BASE | NET\_REQUEST\_WIFI\_CMD\_IFACE\_STATUS)

180

181[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)([NET\_REQUEST\_WIFI\_IFACE\_STATUS](group__wifi__mgmt.md#ga3e45f6ee3801553619d8eb7d0af506eb));

182

[ 183](group__wifi__mgmt.md#gadd9b5b206c7ee2e40c30a37c7b4fc002)#define NET\_REQUEST\_WIFI\_11K\_CONFIG \

184 (\_NET\_WIFI\_BASE | NET\_REQUEST\_WIFI\_CMD\_11K\_CONFIG)

185

186[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)([NET\_REQUEST\_WIFI\_11K\_CONFIG](group__wifi__mgmt.md#gadd9b5b206c7ee2e40c30a37c7b4fc002));

187

[ 188](group__wifi__mgmt.md#ga4a2b1e8befd7376749b1d4fbcf98376f)#define NET\_REQUEST\_WIFI\_11K\_NEIGHBOR\_REQUEST \

189 (\_NET\_WIFI\_BASE | NET\_REQUEST\_WIFI\_CMD\_11K\_NEIGHBOR\_REQUEST)

190

191[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)([NET\_REQUEST\_WIFI\_11K\_NEIGHBOR\_REQUEST](group__wifi__mgmt.md#ga4a2b1e8befd7376749b1d4fbcf98376f));

192

[ 194](group__wifi__mgmt.md#ga68aaced888f98e1ba4e6b61b53e5e2ba)#define NET\_REQUEST\_WIFI\_PS \

195 (\_NET\_WIFI\_BASE | NET\_REQUEST\_WIFI\_CMD\_PS)

196

197[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)([NET\_REQUEST\_WIFI\_PS](group__wifi__mgmt.md#ga68aaced888f98e1ba4e6b61b53e5e2ba));

198

[ 200](group__wifi__mgmt.md#gab84fd7e9ca0bf0b2b9d08889dda26aad)#define NET\_REQUEST\_WIFI\_TWT \

201 (\_NET\_WIFI\_BASE | NET\_REQUEST\_WIFI\_CMD\_TWT)

202

203[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)([NET\_REQUEST\_WIFI\_TWT](group__wifi__mgmt.md#gab84fd7e9ca0bf0b2b9d08889dda26aad));

204

[ 205](group__wifi__mgmt.md#gaf1a806a89b0fd20de950c6e085351134)#define NET\_REQUEST\_WIFI\_BTWT \

206 (\_NET\_WIFI\_BASE | NET\_REQUEST\_WIFI\_CMD\_BTWT)

207

208[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)([NET\_REQUEST\_WIFI\_BTWT](group__wifi__mgmt.md#gaf1a806a89b0fd20de950c6e085351134));

209

[ 211](group__wifi__mgmt.md#ga1032f3773cfe6130da4d4d498b044ee2)#define NET\_REQUEST\_WIFI\_PS\_CONFIG \

212 (\_NET\_WIFI\_BASE | NET\_REQUEST\_WIFI\_CMD\_PS\_CONFIG)

213

214[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)([NET\_REQUEST\_WIFI\_PS\_CONFIG](group__wifi__mgmt.md#ga1032f3773cfe6130da4d4d498b044ee2));

215

[ 217](group__wifi__mgmt.md#ga2b27d102b779a6d846b375854768fb7f)#define NET\_REQUEST\_WIFI\_REG\_DOMAIN \

218 (\_NET\_WIFI\_BASE | NET\_REQUEST\_WIFI\_CMD\_REG\_DOMAIN)

219

220[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)([NET\_REQUEST\_WIFI\_REG\_DOMAIN](group__wifi__mgmt.md#ga2b27d102b779a6d846b375854768fb7f));

221

[ 223](group__wifi__mgmt.md#ga9b4da60a8108b0cc431ac1eecfca0cd0)#define NET\_REQUEST\_WIFI\_MODE \

224 (\_NET\_WIFI\_BASE | NET\_REQUEST\_WIFI\_CMD\_MODE)

225

226[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)([NET\_REQUEST\_WIFI\_MODE](group__wifi__mgmt.md#ga9b4da60a8108b0cc431ac1eecfca0cd0));

227

[ 229](group__wifi__mgmt.md#ga3098e817d12bf4619c9fd2698508fb4e)#define NET\_REQUEST\_WIFI\_PACKET\_FILTER \

230 (\_NET\_WIFI\_BASE | NET\_REQUEST\_WIFI\_CMD\_PACKET\_FILTER)

231

232[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)([NET\_REQUEST\_WIFI\_PACKET\_FILTER](group__wifi__mgmt.md#ga3098e817d12bf4619c9fd2698508fb4e));

233

[ 235](group__wifi__mgmt.md#gad9614d2368f8399850aaec05e40bdc78)#define NET\_REQUEST\_WIFI\_CHANNEL \

236 (\_NET\_WIFI\_BASE | NET\_REQUEST\_WIFI\_CMD\_CHANNEL)

237

238[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)([NET\_REQUEST\_WIFI\_CHANNEL](group__wifi__mgmt.md#gad9614d2368f8399850aaec05e40bdc78));

239

[ 241](group__wifi__mgmt.md#gaa3e52e08d89a1104f07207e52b81d503)#define NET\_REQUEST\_WIFI\_AP\_STA\_DISCONNECT \

242 (\_NET\_WIFI\_BASE | NET\_REQUEST\_WIFI\_CMD\_AP\_STA\_DISCONNECT)

243

244[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)([NET\_REQUEST\_WIFI\_AP\_STA\_DISCONNECT](group__wifi__mgmt.md#gaa3e52e08d89a1104f07207e52b81d503));

245

[ 247](group__wifi__mgmt.md#ga3e60c29ca9ce95d17a7fff087290f7f1)#define NET\_REQUEST\_WIFI\_VERSION \

248 (\_NET\_WIFI\_BASE | NET\_REQUEST\_WIFI\_CMD\_VERSION)

249

250[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)([NET\_REQUEST\_WIFI\_VERSION](group__wifi__mgmt.md#ga3e60c29ca9ce95d17a7fff087290f7f1));

251

[ 253](group__wifi__mgmt.md#gac6483341435ff380a2d4a69430899c1a)#define NET\_REQUEST\_WIFI\_CONN\_PARAMS \

254 (\_NET\_WIFI\_BASE | NET\_REQUEST\_WIFI\_CMD\_CONN\_PARAMS)

255

256[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)([NET\_REQUEST\_WIFI\_CONN\_PARAMS](group__wifi__mgmt.md#gac6483341435ff380a2d4a69430899c1a));

257

[ 259](group__wifi__mgmt.md#ga22d80ef0ffb15e4286d7b1c3325d5334)#define NET\_REQUEST\_WIFI\_RTS\_THRESHOLD \

260 (\_NET\_WIFI\_BASE | NET\_REQUEST\_WIFI\_CMD\_RTS\_THRESHOLD)

261

262[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)([NET\_REQUEST\_WIFI\_RTS\_THRESHOLD](group__wifi__mgmt.md#ga22d80ef0ffb15e4286d7b1c3325d5334));

263

[ 265](group__wifi__mgmt.md#gaf4a78d230f5e0743a6aaf152ddda1c67)#define NET\_REQUEST\_WIFI\_AP\_CONFIG\_PARAM \

266 (\_NET\_WIFI\_BASE | NET\_REQUEST\_WIFI\_CMD\_AP\_CONFIG\_PARAM)

267

268[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)([NET\_REQUEST\_WIFI\_AP\_CONFIG\_PARAM](group__wifi__mgmt.md#gaf4a78d230f5e0743a6aaf152ddda1c67));

269

270#ifdef CONFIG\_WIFI\_NM\_WPA\_SUPPLICANT\_DPP

272#define NET\_REQUEST\_WIFI\_DPP \

273 (\_NET\_WIFI\_BASE | NET\_REQUEST\_WIFI\_CMD\_DPP)

274

275[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_WIFI\_DPP);

276#endif /\* CONFIG\_WIFI\_NM\_WPA\_SUPPLICANT\_DPP \*/

277

[ 279](group__wifi__mgmt.md#ga4f644b4c980628ffd556458eddc0933d)#define NET\_REQUEST\_WIFI\_BTM\_QUERY (\_NET\_WIFI\_BASE | NET\_REQUEST\_WIFI\_CMD\_BTM\_QUERY)

280

281[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)([NET\_REQUEST\_WIFI\_BTM\_QUERY](group__wifi__mgmt.md#ga4f644b4c980628ffd556458eddc0933d));

282

[ 284](group__wifi__mgmt.md#ga9070995249eb35de37e2b60c4426f840)#define NET\_REQUEST\_WIFI\_PMKSA\_FLUSH \

285 (\_NET\_WIFI\_BASE | NET\_REQUEST\_WIFI\_CMD\_PMKSA\_FLUSH)

286

287[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)([NET\_REQUEST\_WIFI\_PMKSA\_FLUSH](group__wifi__mgmt.md#ga9070995249eb35de37e2b60c4426f840));

288

[ 290](group__wifi__mgmt.md#gae5dc7835e11487187663dfe65a15f22b)#define NET\_REQUEST\_WIFI\_ENTERPRISE\_CREDS \

291 (\_NET\_WIFI\_BASE | NET\_REQUEST\_WIFI\_CMD\_ENTERPRISE\_CREDS)

292

293[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)([NET\_REQUEST\_WIFI\_ENTERPRISE\_CREDS](group__wifi__mgmt.md#gae5dc7835e11487187663dfe65a15f22b));

294

[ 296](group__wifi__mgmt.md#ga2678ea372335af008d9bd3333f7a7de1)#define NET\_REQUEST\_WIFI\_RTS\_THRESHOLD\_CONFIG \

297 (\_NET\_WIFI\_BASE | NET\_REQUEST\_WIFI\_CMD\_RTS\_THRESHOLD\_CONFIG)

298

299[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)([NET\_REQUEST\_WIFI\_RTS\_THRESHOLD\_CONFIG](group__wifi__mgmt.md#ga2678ea372335af008d9bd3333f7a7de1));

300

[ 301](group__wifi__mgmt.md#ga649a63bc7d315ebdd89464ff48b3fada)#define NET\_REQUEST\_WIFI\_WPS\_CONFIG (\_NET\_WIFI\_BASE | NET\_REQUEST\_WIFI\_CMD\_WPS\_CONFIG)

302

303[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)([NET\_REQUEST\_WIFI\_WPS\_CONFIG](group__wifi__mgmt.md#ga649a63bc7d315ebdd89464ff48b3fada));

304#ifdef CONFIG\_WIFI\_CREDENTIALS\_CONNECT\_STORED

305#define NET\_REQUEST\_WIFI\_CONNECT\_STORED (\_NET\_WIFI\_BASE | NET\_REQUEST\_WIFI\_CMD\_CONNECT\_STORED)

306

307[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_WIFI\_CONNECT\_STORED);

308#endif

309

[ 310](group__wifi__mgmt.md#ga89cc123bb5c30140d2ce0a8b741b1086)#define NET\_REQUEST\_WIFI\_START\_ROAMING \

311 (\_NET\_WIFI\_BASE | NET\_REQUEST\_WIFI\_CMD\_START\_ROAMING)

312

313[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)([NET\_REQUEST\_WIFI\_START\_ROAMING](group__wifi__mgmt.md#ga89cc123bb5c30140d2ce0a8b741b1086));

314

[ 315](group__wifi__mgmt.md#ga373031970a29331bf1b30d1654c128f0)#define NET\_REQUEST\_WIFI\_NEIGHBOR\_REP\_COMPLETE \

316 (\_NET\_WIFI\_BASE | NET\_REQUEST\_WIFI\_CMD\_NEIGHBOR\_REP\_COMPLETE)

317

318[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)([NET\_REQUEST\_WIFI\_NEIGHBOR\_REP\_COMPLETE](group__wifi__mgmt.md#ga373031970a29331bf1b30d1654c128f0));

319

[ 321](group__wifi__mgmt.md#gac2638308cbb0d268831f1618cf8e1fa8)enum [net\_event\_wifi\_cmd](group__wifi__mgmt.md#gac2638308cbb0d268831f1618cf8e1fa8) {

[ 323](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8a37e9ab2a6832153fa968337d920e587e) [NET\_EVENT\_WIFI\_CMD\_SCAN\_RESULT](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8a37e9ab2a6832153fa968337d920e587e) = 1,

[ 325](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8ad753b7e4588257815f4a60a539ca2018) [NET\_EVENT\_WIFI\_CMD\_SCAN\_DONE](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8ad753b7e4588257815f4a60a539ca2018),

[ 327](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8af76f28777b91b365dc3f97028bc18e3c) [NET\_EVENT\_WIFI\_CMD\_CONNECT\_RESULT](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8af76f28777b91b365dc3f97028bc18e3c),

[ 329](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8a3a3b0387f83d8fb24a0e27312468b0eb) [NET\_EVENT\_WIFI\_CMD\_DISCONNECT\_RESULT](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8a3a3b0387f83d8fb24a0e27312468b0eb),

[ 331](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8af4b3f1969b96f63253851c26c3882a14) [NET\_EVENT\_WIFI\_CMD\_IFACE\_STATUS](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8af4b3f1969b96f63253851c26c3882a14),

[ 333](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8adad71603ed829ed92d06f8c40efa9b18) [NET\_EVENT\_WIFI\_CMD\_TWT](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8adad71603ed829ed92d06f8c40efa9b18),

[ 337](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8a78838bf7ce80cee5e803712cd0286750) [NET\_EVENT\_WIFI\_CMD\_TWT\_SLEEP\_STATE](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8a78838bf7ce80cee5e803712cd0286750),

[ 339](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8addf15c69512be7ab4957e7c0b3fde0ac) [NET\_EVENT\_WIFI\_CMD\_RAW\_SCAN\_RESULT](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8addf15c69512be7ab4957e7c0b3fde0ac),

[ 341](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8af1c42bd59f01260c64ede07da436c18f) [NET\_EVENT\_WIFI\_CMD\_DISCONNECT\_COMPLETE](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8af1c42bd59f01260c64ede07da436c18f),

[ 343](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8acc9d8a16d99e4006b915b3686522a8e0) [NET\_EVENT\_WIFI\_CMD\_SIGNAL\_CHANGE](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8acc9d8a16d99e4006b915b3686522a8e0),

[ 345](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8a75a0a093f32fa2577286c92c2525df91) [NET\_EVENT\_WIFI\_CMD\_NEIGHBOR\_REP\_RECEIVED](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8a75a0a093f32fa2577286c92c2525df91),

[ 347](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8a86b6811a06f6158ae9ea4687e219e5af) [NET\_EVENT\_WIFI\_CMD\_NEIGHBOR\_REP\_COMPLETE](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8a86b6811a06f6158ae9ea4687e219e5af),

[ 349](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8abd1797564427886eeb14dd293ae86a9b) [NET\_EVENT\_WIFI\_CMD\_AP\_ENABLE\_RESULT](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8abd1797564427886eeb14dd293ae86a9b),

[ 351](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8aeec3d7a9191280c2326034a17555308d) [NET\_EVENT\_WIFI\_CMD\_AP\_DISABLE\_RESULT](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8aeec3d7a9191280c2326034a17555308d),

[ 353](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8abd4269b2cd1302ce61da4f8d7bb9d5fb) [NET\_EVENT\_WIFI\_CMD\_AP\_STA\_CONNECTED](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8abd4269b2cd1302ce61da4f8d7bb9d5fb),

[ 355](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8a3678a39f9542968958b5575d571d4e2e) [NET\_EVENT\_WIFI\_CMD\_AP\_STA\_DISCONNECTED](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8a3678a39f9542968958b5575d571d4e2e),

[ 357](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8a4ec52c22e23502421077e46e94facf08) [NET\_EVENT\_WIFI\_CMD\_SUPPLICANT](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8a4ec52c22e23502421077e46e94facf08),

358};

359

[ 361](group__wifi__mgmt.md#ga436a927d47eb9abe683b89f2b128cd6e)#define NET\_EVENT\_WIFI\_SCAN\_RESULT \

362 (\_NET\_WIFI\_EVENT | NET\_EVENT\_WIFI\_CMD\_SCAN\_RESULT)

363

[ 365](group__wifi__mgmt.md#ga8ce35a12e5338e9a65970382b4a26b88)#define NET\_EVENT\_WIFI\_SCAN\_DONE \

366 (\_NET\_WIFI\_EVENT | NET\_EVENT\_WIFI\_CMD\_SCAN\_DONE)

367

[ 369](group__wifi__mgmt.md#ga0e8feafcc5efd85d04be91f407c0b7c4)#define NET\_EVENT\_WIFI\_CONNECT\_RESULT \

370 (\_NET\_WIFI\_EVENT | NET\_EVENT\_WIFI\_CMD\_CONNECT\_RESULT)

371

[ 373](group__wifi__mgmt.md#ga8cbbe69bd60f42fdbb06f4f1e15410c8)#define NET\_EVENT\_WIFI\_DISCONNECT\_RESULT \

374 (\_NET\_WIFI\_EVENT | NET\_EVENT\_WIFI\_CMD\_DISCONNECT\_RESULT)

375

[ 377](group__wifi__mgmt.md#ga99e11fc15582b94d4243de7733e47ebb)#define NET\_EVENT\_WIFI\_IFACE\_STATUS \

378 (\_NET\_WIFI\_EVENT | NET\_EVENT\_WIFI\_CMD\_IFACE\_STATUS)

379

[ 381](group__wifi__mgmt.md#gaeb968a5d2a8d68a8c634cca18dbcf9c6)#define NET\_EVENT\_WIFI\_TWT \

382 (\_NET\_WIFI\_EVENT | NET\_EVENT\_WIFI\_CMD\_TWT)

383

[ 385](group__wifi__mgmt.md#ga682d95b5d06a9b175c10d712acca8a49)#define NET\_EVENT\_WIFI\_TWT\_SLEEP\_STATE \

386 (\_NET\_WIFI\_EVENT | NET\_EVENT\_WIFI\_CMD\_TWT\_SLEEP\_STATE)

387

[ 389](group__wifi__mgmt.md#gaea8d222282ddef6992330763afc759a4)#define NET\_EVENT\_WIFI\_RAW\_SCAN\_RESULT \

390 (\_NET\_WIFI\_EVENT | NET\_EVENT\_WIFI\_CMD\_RAW\_SCAN\_RESULT)

391

[ 393](group__wifi__mgmt.md#ga40027feb7ec42c846fd99b56bbd2256d)#define NET\_EVENT\_WIFI\_DISCONNECT\_COMPLETE \

394 (\_NET\_WIFI\_EVENT | NET\_EVENT\_WIFI\_CMD\_DISCONNECT\_COMPLETE)

395

[ 397](group__wifi__mgmt.md#ga8da47e9d3e594840fb7a7d59f45ea9ce)#define NET\_EVENT\_WIFI\_SIGNAL\_CHANGE \

398 (\_NET\_WIFI\_EVENT | NET\_EVENT\_WIFI\_CMD\_SIGNAL\_CHANGE)

399

[ 401](group__wifi__mgmt.md#ga7ed4bc9f25055f5a35270a4c6a0bedcc)#define NET\_EVENT\_WIFI\_NEIGHBOR\_REP\_COMP \

402 (\_NET\_WIFI\_EVENT | NET\_EVENT\_WIFI\_CMD\_NEIGHBOR\_REP\_COMPLETE)

403

[ 405](group__wifi__mgmt.md#ga1d678fbae0f092814392c0ab4087cb73)#define NET\_EVENT\_WIFI\_AP\_ENABLE\_RESULT \

406 (\_NET\_WIFI\_EVENT | NET\_EVENT\_WIFI\_CMD\_AP\_ENABLE\_RESULT)

407

[ 409](group__wifi__mgmt.md#ga104296fdb38edf868bea1a46f572d101)#define NET\_EVENT\_WIFI\_AP\_DISABLE\_RESULT \

410 (\_NET\_WIFI\_EVENT | NET\_EVENT\_WIFI\_CMD\_AP\_DISABLE\_RESULT)

411

[ 413](group__wifi__mgmt.md#gacc392179948bfd5bed6702dc8fb5cd9d)#define NET\_EVENT\_WIFI\_AP\_STA\_CONNECTED \

414 (\_NET\_WIFI\_EVENT | NET\_EVENT\_WIFI\_CMD\_AP\_STA\_CONNECTED)

415

[ 417](group__wifi__mgmt.md#ga3e8154ce1808665dd165f793ddec1673)#define NET\_EVENT\_WIFI\_AP\_STA\_DISCONNECTED \

418 (\_NET\_WIFI\_EVENT | NET\_EVENT\_WIFI\_CMD\_AP\_STA\_DISCONNECTED)

419

[ 421](structwifi__version.md)struct [wifi\_version](structwifi__version.md) {

[ 423](structwifi__version.md#aea828bdb512440d6aa3cc853525c4971) const char \*[drv\_version](structwifi__version.md#aea828bdb512440d6aa3cc853525c4971);

[ 425](structwifi__version.md#a4bf2cbdf5c43ff21718ccf19646c164e) const char \*[fw\_version](structwifi__version.md#a4bf2cbdf5c43ff21718ccf19646c164e);

426};

427

[ 431](structwifi__band__channel.md)struct [wifi\_band\_channel](structwifi__band__channel.md) {

[ 433](structwifi__band__channel.md#a4a932599429f37231f76c3064ec5efb3) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [band](structwifi__band__channel.md#a4a932599429f37231f76c3064ec5efb3);

[ 435](structwifi__band__channel.md#acd0dd7366de3650124dad7232a58ade0) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [channel](structwifi__band__channel.md#acd0dd7366de3650124dad7232a58ade0);

436};

437

[ 443](structwifi__scan__params.md)struct [wifi\_scan\_params](structwifi__scan__params.md) {

[ 451](structwifi__scan__params.md#a645acc54603cd4692527c1a028933078) enum [wifi\_scan\_type](group__wifi__mgmt.md#gad30e29eda65ccafdbd7f11865937b8ea) [scan\_type](structwifi__scan__params.md#a645acc54603cd4692527c1a028933078);

[ 455](structwifi__scan__params.md#a6b571d960ed9d7419e31530e5fb6f97a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bands](structwifi__scan__params.md#a6b571d960ed9d7419e31530e5fb6f97a);

[ 458](structwifi__scan__params.md#a2453a75c23e04e3572559c0e7199c1b4) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [dwell\_time\_active](structwifi__scan__params.md#a2453a75c23e04e3572559c0e7199c1b4);

[ 461](structwifi__scan__params.md#a8e7a37ccda8de635e7b7066d7943e814) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [dwell\_time\_passive](structwifi__scan__params.md#a8e7a37ccda8de635e7b7066d7943e814);

[ 464](structwifi__scan__params.md#aac11ee8e0ec8a4fa24668f4820bd1a12) const char \*[ssids](structwifi__scan__params.md#aac11ee8e0ec8a4fa24668f4820bd1a12)[WIFI\_MGMT\_SCAN\_SSID\_FILT\_MAX];

[ 472](structwifi__scan__params.md#a12d5dea7d8fa8ad03ac2366720c46243) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [max\_bss\_cnt](structwifi__scan__params.md#a12d5dea7d8fa8ad03ac2366720c46243);

[ 487](structwifi__scan__params.md#aa5ddbd6bc97b7598288d4b0d38521681) struct [wifi\_band\_channel](structwifi__band__channel.md) [band\_chan](structwifi__scan__params.md#aa5ddbd6bc97b7598288d4b0d38521681)[WIFI\_MGMT\_SCAN\_CHAN\_MAX\_MANUAL];

488};

489

[ 493](structwifi__scan__result.md)struct [wifi\_scan\_result](structwifi__scan__result.md) {

[ 495](structwifi__scan__result.md#aaefb8f5c9510e4f5002ae306d853ade8) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [ssid](structwifi__scan__result.md#aaefb8f5c9510e4f5002ae306d853ade8)[[WIFI\_SSID\_MAX\_LEN](group__wifi__mgmt.md#gad62c60666c9fdffe2e0e9c4388f87886) + 1];

[ 497](structwifi__scan__result.md#a2c1c2f4265b914df08fc75deb8b69d39) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [ssid\_length](structwifi__scan__result.md#a2c1c2f4265b914df08fc75deb8b69d39);

[ 499](structwifi__scan__result.md#a38201c9dd798dc11b5bda3ce97b02e92) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [band](structwifi__scan__result.md#a38201c9dd798dc11b5bda3ce97b02e92);

[ 501](structwifi__scan__result.md#adbbfd7692ee5ffd6344fe78b9d91c840) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [channel](structwifi__scan__result.md#adbbfd7692ee5ffd6344fe78b9d91c840);

[ 503](structwifi__scan__result.md#af2d3dc5d115e3db76d3bc115510b0a5a) enum [wifi\_security\_type](group__wifi__mgmt.md#gadde31a04fa25ed805115c6b31854cd9c) [security](structwifi__scan__result.md#af2d3dc5d115e3db76d3bc115510b0a5a);

[ 505](structwifi__scan__result.md#abb7de47c605ec05c8fe0a06ecbd2b7b6) enum [wifi\_wpa3\_enterprise\_type](group__wifi__mgmt.md#ga48fea1f0c7d2700cef47068f96c6b71a) [wpa3\_ent\_type](structwifi__scan__result.md#abb7de47c605ec05c8fe0a06ecbd2b7b6);

[ 507](structwifi__scan__result.md#acaa3fb30ebf6df22bfac6380698ed28e) enum [wifi\_mfp\_options](group__wifi__mgmt.md#ga1f252da47d9650023d7fff6d08e49c76) [mfp](structwifi__scan__result.md#acaa3fb30ebf6df22bfac6380698ed28e);

[ 509](structwifi__scan__result.md#a76aa012136e3721fd4a482a22b93546f) [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) [rssi](structwifi__scan__result.md#a76aa012136e3721fd4a482a22b93546f);

[ 511](structwifi__scan__result.md#a4fdbc4dc4d5c8b279223e8c06624f434) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [mac](structwifi__scan__result.md#a4fdbc4dc4d5c8b279223e8c06624f434)[[WIFI\_MAC\_ADDR\_LEN](group__wifi__mgmt.md#ga29409ff83a53c6464decdde9bdd04de6)];

[ 513](structwifi__scan__result.md#a8fca0dabec00ebd7ed4800098ec9d451) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [mac\_length](structwifi__scan__result.md#a8fca0dabec00ebd7ed4800098ec9d451);

514};

515

[ 517](structwifi__connect__req__params.md)struct [wifi\_connect\_req\_params](structwifi__connect__req__params.md) {

[ 519](structwifi__connect__req__params.md#ac260c2cd17a3f36ea101edaf23d41083) const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[ssid](structwifi__connect__req__params.md#ac260c2cd17a3f36ea101edaf23d41083);

[ 521](structwifi__connect__req__params.md#a547dddf6be5dd77eda74b1085a798400) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [ssid\_length](structwifi__connect__req__params.md#a547dddf6be5dd77eda74b1085a798400); /\* Max 32 \*/

[ 523](structwifi__connect__req__params.md#aa7743f0ecbc27a9595720ce13ce57c1d) const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[psk](structwifi__connect__req__params.md#aa7743f0ecbc27a9595720ce13ce57c1d);

[ 525](structwifi__connect__req__params.md#aaf7455a65590d19f047214b459a2dcb9) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [psk\_length](structwifi__connect__req__params.md#aaf7455a65590d19f047214b459a2dcb9); /\* Min 8 - Max 64 \*/

[ 527](structwifi__connect__req__params.md#a469fac5758b78fc425911837930b2060) const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[sae\_password](structwifi__connect__req__params.md#a469fac5758b78fc425911837930b2060);

[ 529](structwifi__connect__req__params.md#a74f0819e7a546ffb8bfb0ec587eccf20) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [sae\_password\_length](structwifi__connect__req__params.md#a74f0819e7a546ffb8bfb0ec587eccf20); /\* No length restrictions \*/

[ 531](structwifi__connect__req__params.md#aa2fea1881a8ffdf5d7093ae295867f3e) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [band](structwifi__connect__req__params.md#aa2fea1881a8ffdf5d7093ae295867f3e);

[ 533](structwifi__connect__req__params.md#a52b6d0323c35d03ec239f40be35cae72) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [channel](structwifi__connect__req__params.md#a52b6d0323c35d03ec239f40be35cae72);

[ 535](structwifi__connect__req__params.md#a18dce6bb021086877a30e7a04f5b24b9) enum [wifi\_security\_type](group__wifi__mgmt.md#gadde31a04fa25ed805115c6b31854cd9c) [security](structwifi__connect__req__params.md#a18dce6bb021086877a30e7a04f5b24b9);

[ 537](structwifi__connect__req__params.md#a745b3416172672a7e5b12bcc5b55e88c) enum [wifi\_mfp\_options](group__wifi__mgmt.md#ga1f252da47d9650023d7fff6d08e49c76) [mfp](structwifi__connect__req__params.md#a745b3416172672a7e5b12bcc5b55e88c);

[ 539](structwifi__connect__req__params.md#aa8081b9075ff9244cefd0ac1ef3f42cb) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bssid](structwifi__connect__req__params.md#aa8081b9075ff9244cefd0ac1ef3f42cb)[[WIFI\_MAC\_ADDR\_LEN](group__wifi__mgmt.md#ga29409ff83a53c6464decdde9bdd04de6)];

[ 541](structwifi__connect__req__params.md#a56183ba7f4d8eaf5fc5b495856adecfd) int [timeout](structwifi__connect__req__params.md#a56183ba7f4d8eaf5fc5b495856adecfd);

[ 543](structwifi__connect__req__params.md#a781456e079357e2e1096218af3bd218c) const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[anon\_id](structwifi__connect__req__params.md#a781456e079357e2e1096218af3bd218c);

[ 545](structwifi__connect__req__params.md#a2892253024b70e5cb8eb2166b17ebe22) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [aid\_length](structwifi__connect__req__params.md#a2892253024b70e5cb8eb2166b17ebe22);

[ 547](structwifi__connect__req__params.md#a4946647659a347667ee49bb6990bba66) const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[key\_passwd](structwifi__connect__req__params.md#a4946647659a347667ee49bb6990bba66);

[ 549](structwifi__connect__req__params.md#a9f913fc0ccecafaba488e444d701fd68) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [key\_passwd\_length](structwifi__connect__req__params.md#a9f913fc0ccecafaba488e444d701fd68);

[ 551](structwifi__connect__req__params.md#a020fc58d7e5350cc803cd5d6fa575e6a) const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[key2\_passwd](structwifi__connect__req__params.md#a020fc58d7e5350cc803cd5d6fa575e6a);

[ 553](structwifi__connect__req__params.md#af7b163cc2bffc59f7fa31f47c5e52062) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [key2\_passwd\_length](structwifi__connect__req__params.md#af7b163cc2bffc59f7fa31f47c5e52062);

[ 555](structwifi__connect__req__params.md#ae0b94d870ecbee0b203caee6a6e3d8b2) enum [wifi\_wpa3\_enterprise\_type](group__wifi__mgmt.md#ga48fea1f0c7d2700cef47068f96c6b71a) [wpa3\_ent\_mode](structwifi__connect__req__params.md#ae0b94d870ecbee0b203caee6a6e3d8b2);

[ 557](structwifi__connect__req__params.md#aa4577535a27b8d54d9b8c7543d359ade) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [TLS\_cipher](structwifi__connect__req__params.md#aa4577535a27b8d54d9b8c7543d359ade);

[ 559](structwifi__connect__req__params.md#a8c8ecb1ef0fe3f2f4c04a7a8eeccbbdf) int [eap\_ver](structwifi__connect__req__params.md#a8c8ecb1ef0fe3f2f4c04a7a8eeccbbdf);

[ 561](structwifi__connect__req__params.md#ab9c65599409387af65a3c2895c3116da) const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[eap\_identity](structwifi__connect__req__params.md#ab9c65599409387af65a3c2895c3116da);

[ 563](structwifi__connect__req__params.md#a4da02ff112c09f55dc5bddcda27d16a3) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [eap\_id\_length](structwifi__connect__req__params.md#a4da02ff112c09f55dc5bddcda27d16a3);

[ 565](structwifi__connect__req__params.md#afd046e702739c4a0d89322ee41b37acd) const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[eap\_password](structwifi__connect__req__params.md#afd046e702739c4a0d89322ee41b37acd);

[ 567](structwifi__connect__req__params.md#aeab22e95a04a1831b87beda1772d3db7) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [eap\_passwd\_length](structwifi__connect__req__params.md#aeab22e95a04a1831b87beda1772d3db7);

[ 569](structwifi__connect__req__params.md#aa8f18ace96e471eb0bc8bff8d8146f6f) bool [verify\_peer\_cert](structwifi__connect__req__params.md#aa8f18ace96e471eb0bc8bff8d8146f6f);

[ 571](structwifi__connect__req__params.md#a047b11e703fb646d778785dfcb14257b) bool [ft\_used](structwifi__connect__req__params.md#a047b11e703fb646d778785dfcb14257b);

[ 573](structwifi__connect__req__params.md#a71770c2f2da378db2efedaa87b141627) int [nusers](structwifi__connect__req__params.md#a71770c2f2da378db2efedaa87b141627);

[ 575](structwifi__connect__req__params.md#aaf071a51c7281e4d42197f266c729c04) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [passwds](structwifi__connect__req__params.md#aaf071a51c7281e4d42197f266c729c04);

[ 577](structwifi__connect__req__params.md#a265001d2309840d04bdca507896255d0) const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[identities](structwifi__connect__req__params.md#a265001d2309840d04bdca507896255d0)[WIFI\_ENT\_IDENTITY\_MAX\_USERS];

[ 579](structwifi__connect__req__params.md#a2163b50b6d466663404e1cb21ce6ae5d) const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[passwords](structwifi__connect__req__params.md#a2163b50b6d466663404e1cb21ce6ae5d)[WIFI\_ENT\_IDENTITY\_MAX\_USERS];

[ 585](structwifi__connect__req__params.md#afac70366e509301f9a27ca51be30b88d) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [ignore\_broadcast\_ssid](structwifi__connect__req__params.md#afac70366e509301f9a27ca51be30b88d);

[ 587](structwifi__connect__req__params.md#a0d44c86d9b9528041bbe7534e0c7597a) enum [wifi\_frequency\_bandwidths](group__wifi__mgmt.md#ga3b01cead3c2eb4581fe85e2aaaffbd49) [bandwidth](structwifi__connect__req__params.md#a0d44c86d9b9528041bbe7534e0c7597a);

588};

589

[ 593](group__wifi__mgmt.md#ga86a5741e54aeb3e290142b0de217b8a8)enum [wifi\_conn\_status](group__wifi__mgmt.md#ga86a5741e54aeb3e290142b0de217b8a8) {

[ 595](group__wifi__mgmt.md#gga86a5741e54aeb3e290142b0de217b8a8a380410b02b1e12599f37d1dcb844f5bd) [WIFI\_STATUS\_CONN\_SUCCESS](group__wifi__mgmt.md#gga86a5741e54aeb3e290142b0de217b8a8a380410b02b1e12599f37d1dcb844f5bd) = 0,

[ 597](group__wifi__mgmt.md#gga86a5741e54aeb3e290142b0de217b8a8ab80ec4b70c75695fbe698034e2cb6a44) [WIFI\_STATUS\_CONN\_FAIL](group__wifi__mgmt.md#gga86a5741e54aeb3e290142b0de217b8a8ab80ec4b70c75695fbe698034e2cb6a44),

[ 606](group__wifi__mgmt.md#gga86a5741e54aeb3e290142b0de217b8a8a90d91f96a35c9f6847cbc7abd8c20bf8) [WIFI\_STATUS\_CONN\_WRONG\_PASSWORD](group__wifi__mgmt.md#gga86a5741e54aeb3e290142b0de217b8a8a90d91f96a35c9f6847cbc7abd8c20bf8),

[ 608](group__wifi__mgmt.md#gga86a5741e54aeb3e290142b0de217b8a8abb8783b92aec2ed1ffc6331979888563) [WIFI\_STATUS\_CONN\_TIMEOUT](group__wifi__mgmt.md#gga86a5741e54aeb3e290142b0de217b8a8abb8783b92aec2ed1ffc6331979888563),

[ 610](group__wifi__mgmt.md#gga86a5741e54aeb3e290142b0de217b8a8a2ae79fa389bb447fa108e0107aeff2f4) [WIFI\_STATUS\_CONN\_AP\_NOT\_FOUND](group__wifi__mgmt.md#gga86a5741e54aeb3e290142b0de217b8a8a2ae79fa389bb447fa108e0107aeff2f4),

[ 612](group__wifi__mgmt.md#gga86a5741e54aeb3e290142b0de217b8a8aeee5fb8d8c3e7905554d08331f06191f) [WIFI\_STATUS\_CONN\_LAST\_STATUS](group__wifi__mgmt.md#gga86a5741e54aeb3e290142b0de217b8a8aeee5fb8d8c3e7905554d08331f06191f),

[ 614](group__wifi__mgmt.md#gga86a5741e54aeb3e290142b0de217b8a8abe1401e5d516c0d63291add15e558b18) [WIFI\_STATUS\_DISCONN\_FIRST\_STATUS](group__wifi__mgmt.md#gga86a5741e54aeb3e290142b0de217b8a8abe1401e5d516c0d63291add15e558b18) = [WIFI\_STATUS\_CONN\_LAST\_STATUS](group__wifi__mgmt.md#gga86a5741e54aeb3e290142b0de217b8a8aeee5fb8d8c3e7905554d08331f06191f),

615};

616

[ 620](group__wifi__mgmt.md#gac782af0a60b202fd19597cabb7bd3a9a)enum [wifi\_disconn\_reason](group__wifi__mgmt.md#gac782af0a60b202fd19597cabb7bd3a9a) {

[ 622](group__wifi__mgmt.md#ggac782af0a60b202fd19597cabb7bd3a9aa5c894399db8949a789ca4f5750b6f042) [WIFI\_REASON\_DISCONN\_SUCCESS](group__wifi__mgmt.md#ggac782af0a60b202fd19597cabb7bd3a9aa5c894399db8949a789ca4f5750b6f042) = 0,

[ 624](group__wifi__mgmt.md#ggac782af0a60b202fd19597cabb7bd3a9aa87f5d64a9fd3acf8d67c698199779e5c) [WIFI\_REASON\_DISCONN\_UNSPECIFIED](group__wifi__mgmt.md#ggac782af0a60b202fd19597cabb7bd3a9aa87f5d64a9fd3acf8d67c698199779e5c),

[ 626](group__wifi__mgmt.md#ggac782af0a60b202fd19597cabb7bd3a9aaee75adafb52bd6ecaa547a76c6ccd0a7) [WIFI\_REASON\_DISCONN\_USER\_REQUEST](group__wifi__mgmt.md#ggac782af0a60b202fd19597cabb7bd3a9aaee75adafb52bd6ecaa547a76c6ccd0a7),

[ 628](group__wifi__mgmt.md#ggac782af0a60b202fd19597cabb7bd3a9aa34e3f78ce43db3daeaf32038e0baf204) [WIFI\_REASON\_DISCONN\_AP\_LEAVING](group__wifi__mgmt.md#ggac782af0a60b202fd19597cabb7bd3a9aa34e3f78ce43db3daeaf32038e0baf204),

[ 630](group__wifi__mgmt.md#ggac782af0a60b202fd19597cabb7bd3a9aa05fe2f87de30de47ee48f7615c2206e6) [WIFI\_REASON\_DISCONN\_INACTIVITY](group__wifi__mgmt.md#ggac782af0a60b202fd19597cabb7bd3a9aa05fe2f87de30de47ee48f7615c2206e6),

631};

632

[ 636](group__wifi__mgmt.md#gaaf730bf76adc06434c7ac63bf0417884)enum [wifi\_ap\_status](group__wifi__mgmt.md#gaaf730bf76adc06434c7ac63bf0417884) {

[ 638](group__wifi__mgmt.md#ggaaf730bf76adc06434c7ac63bf0417884a0df52848da8735892d0eb1e381b2cd7c) [WIFI\_STATUS\_AP\_SUCCESS](group__wifi__mgmt.md#ggaaf730bf76adc06434c7ac63bf0417884a0df52848da8735892d0eb1e381b2cd7c) = 0,

[ 640](group__wifi__mgmt.md#ggaaf730bf76adc06434c7ac63bf0417884a6c6801381caa3862004662169202fa9a) [WIFI\_STATUS\_AP\_FAIL](group__wifi__mgmt.md#ggaaf730bf76adc06434c7ac63bf0417884a6c6801381caa3862004662169202fa9a),

[ 642](group__wifi__mgmt.md#ggaaf730bf76adc06434c7ac63bf0417884a5acb85a2361ca72ed10966b829c5753b) [WIFI\_STATUS\_AP\_CHANNEL\_NOT\_SUPPORTED](group__wifi__mgmt.md#ggaaf730bf76adc06434c7ac63bf0417884a5acb85a2361ca72ed10966b829c5753b),

[ 644](group__wifi__mgmt.md#ggaaf730bf76adc06434c7ac63bf0417884a0b1cb592c54c16e8a54defee71c5fd15) [WIFI\_STATUS\_AP\_CHANNEL\_NOT\_ALLOWED](group__wifi__mgmt.md#ggaaf730bf76adc06434c7ac63bf0417884a0b1cb592c54c16e8a54defee71c5fd15),

[ 646](group__wifi__mgmt.md#ggaaf730bf76adc06434c7ac63bf0417884ac18a7b551f8c6bb7737b0e8e60c323ce) [WIFI\_STATUS\_AP\_SSID\_NOT\_ALLOWED](group__wifi__mgmt.md#ggaaf730bf76adc06434c7ac63bf0417884ac18a7b551f8c6bb7737b0e8e60c323ce),

[ 648](group__wifi__mgmt.md#ggaaf730bf76adc06434c7ac63bf0417884abe5a626d22051522255d98fdfdfbfcc8) [WIFI\_STATUS\_AP\_AUTH\_TYPE\_NOT\_SUPPORTED](group__wifi__mgmt.md#ggaaf730bf76adc06434c7ac63bf0417884abe5a626d22051522255d98fdfdfbfcc8),

[ 650](group__wifi__mgmt.md#ggaaf730bf76adc06434c7ac63bf0417884a2105e6c49b3bcb5f7dcacbc1e5ce9cca) [WIFI\_STATUS\_AP\_OP\_NOT\_SUPPORTED](group__wifi__mgmt.md#ggaaf730bf76adc06434c7ac63bf0417884a2105e6c49b3bcb5f7dcacbc1e5ce9cca),

[ 652](group__wifi__mgmt.md#ggaaf730bf76adc06434c7ac63bf0417884a36a58980bdc7877c910441590137ddbe) [WIFI\_STATUS\_AP\_OP\_NOT\_PERMITTED](group__wifi__mgmt.md#ggaaf730bf76adc06434c7ac63bf0417884a36a58980bdc7877c910441590137ddbe),

653};

654

[ 656](structwifi__status.md)struct [wifi\_status](structwifi__status.md) {

657 union {

[ 659](structwifi__status.md#aa1dbff8154400f8353693d387977008b) int [status](structwifi__status.md#aa1dbff8154400f8353693d387977008b);

[ 661](structwifi__status.md#a8f885e78366d0499e4ba8e15bef275ac) enum [wifi\_conn\_status](group__wifi__mgmt.md#ga86a5741e54aeb3e290142b0de217b8a8) [conn\_status](structwifi__status.md#a8f885e78366d0499e4ba8e15bef275ac);

[ 663](structwifi__status.md#aa04b5033d93274badd27f702af9830bc) enum [wifi\_disconn\_reason](group__wifi__mgmt.md#gac782af0a60b202fd19597cabb7bd3a9a) [disconn\_reason](structwifi__status.md#aa04b5033d93274badd27f702af9830bc);

[ 665](structwifi__status.md#a02f0fcc7ef57661ca95d0c99f045aef1) enum [wifi\_ap\_status](group__wifi__mgmt.md#gaaf730bf76adc06434c7ac63bf0417884) [ap\_status](structwifi__status.md#a02f0fcc7ef57661ca95d0c99f045aef1);

666 };

667};

668

[ 670](structwifi__iface__status.md)struct [wifi\_iface\_status](structwifi__iface__status.md) {

[ 672](structwifi__iface__status.md#ac52806155be3d64954ac6d109e76ec57) int [state](structwifi__iface__status.md#ac52806155be3d64954ac6d109e76ec57);

[ 674](structwifi__iface__status.md#ad82f281941e4f6ce1ef0bca008e26d41) unsigned int [ssid\_len](structwifi__iface__status.md#ad82f281941e4f6ce1ef0bca008e26d41);

[ 676](structwifi__iface__status.md#a3ab671471bcdfeb5b955d156d39f2bb3) char [ssid](structwifi__iface__status.md#a3ab671471bcdfeb5b955d156d39f2bb3)[[WIFI\_SSID\_MAX\_LEN](group__wifi__mgmt.md#gad62c60666c9fdffe2e0e9c4388f87886) + 1];

[ 678](structwifi__iface__status.md#a5d5d19056a1a15365fbdd94274a0fc5e) char [bssid](structwifi__iface__status.md#a5d5d19056a1a15365fbdd94274a0fc5e)[[WIFI\_MAC\_ADDR\_LEN](group__wifi__mgmt.md#ga29409ff83a53c6464decdde9bdd04de6)];

[ 680](structwifi__iface__status.md#ae1c141a18f4e225af2c22a8cb4f882a8) enum [wifi\_frequency\_bands](group__wifi__mgmt.md#ga1e2f0439a322355fa7368ea880c9c15d) [band](structwifi__iface__status.md#ae1c141a18f4e225af2c22a8cb4f882a8);

[ 682](structwifi__iface__status.md#a6432663156e5b2c424d254ed1eae0144) unsigned int [channel](structwifi__iface__status.md#a6432663156e5b2c424d254ed1eae0144);

[ 684](structwifi__iface__status.md#ad33d2ec149a8d556e2472dd842ceadc0) enum [wifi\_iface\_mode](group__wifi__mgmt.md#ga584f6239ac14e2bedc5e6bd72756423b) [iface\_mode](structwifi__iface__status.md#ad33d2ec149a8d556e2472dd842ceadc0);

[ 686](structwifi__iface__status.md#ae2de076d79f2172793d65fe9cd31edc4) enum [wifi\_link\_mode](group__wifi__mgmt.md#gabdb2a784d4727b71ab44cca04e422c62) [link\_mode](structwifi__iface__status.md#ae2de076d79f2172793d65fe9cd31edc4);

[ 688](structwifi__iface__status.md#a361c0e8a385fdc21f16258c25c2bc8d1) enum [wifi\_wpa3\_enterprise\_type](group__wifi__mgmt.md#ga48fea1f0c7d2700cef47068f96c6b71a) [wpa3\_ent\_type](structwifi__iface__status.md#a361c0e8a385fdc21f16258c25c2bc8d1);

[ 690](structwifi__iface__status.md#a625ecec1abec8dd65cf155eab21a01b5) enum [wifi\_security\_type](group__wifi__mgmt.md#gadde31a04fa25ed805115c6b31854cd9c) [security](structwifi__iface__status.md#a625ecec1abec8dd65cf155eab21a01b5);

[ 692](structwifi__iface__status.md#aa1a9b644fd355526125ddd32416b7c24) enum [wifi\_mfp\_options](group__wifi__mgmt.md#ga1f252da47d9650023d7fff6d08e49c76) [mfp](structwifi__iface__status.md#aa1a9b644fd355526125ddd32416b7c24);

[ 694](structwifi__iface__status.md#a4e593147b88eb4938d55a4de72fcc7f6) int [rssi](structwifi__iface__status.md#a4e593147b88eb4938d55a4de72fcc7f6);

[ 696](structwifi__iface__status.md#aae6c8cbaa16c81d308f08114d5103a3d) unsigned char [dtim\_period](structwifi__iface__status.md#aae6c8cbaa16c81d308f08114d5103a3d);

[ 698](structwifi__iface__status.md#a241bfbe70628006b515b5f9e4f97665c) unsigned short [beacon\_interval](structwifi__iface__status.md#a241bfbe70628006b515b5f9e4f97665c);

[ 700](structwifi__iface__status.md#acfde8d64b463a9f553aa4fb689dc1917) bool [twt\_capable](structwifi__iface__status.md#acfde8d64b463a9f553aa4fb689dc1917);

[ 702](structwifi__iface__status.md#af255c63862e0c9e5008b2e4952d7e491) int [current\_phy\_tx\_rate](structwifi__iface__status.md#af255c63862e0c9e5008b2e4952d7e491);

703};

704

[ 706](structwifi__ps__params.md)struct [wifi\_ps\_params](structwifi__ps__params.md) {

[ 708](structwifi__ps__params.md#abb22aaa45833ac130922204bd2fe841b) enum [wifi\_ps](group__wifi__mgmt.md#ga0fffeb57b68fb8cdef9d3d571368b8ca) [enabled](structwifi__ps__params.md#abb22aaa45833ac130922204bd2fe841b);

[ 710](structwifi__ps__params.md#a8510c799ab0c5825f1c6349f9799c62f) unsigned short [listen\_interval](structwifi__ps__params.md#a8510c799ab0c5825f1c6349f9799c62f);

[ 712](structwifi__ps__params.md#a7cb3e7fb7d9f8bd7c2cab41f879b3b66) enum [wifi\_ps\_wakeup\_mode](group__wifi__mgmt.md#gac7f907644847e905d67c709fa4afae7f) [wakeup\_mode](structwifi__ps__params.md#a7cb3e7fb7d9f8bd7c2cab41f879b3b66);

[ 714](structwifi__ps__params.md#a5a022d89d43ecf2cd1f15fc72c0f2bed) enum [wifi\_ps\_mode](group__wifi__mgmt.md#gaffae7d2a754be5eb952ad2b83edad54c) [mode](structwifi__ps__params.md#a5a022d89d43ecf2cd1f15fc72c0f2bed);

[ 723](structwifi__ps__params.md#ad963f1bf78dc271f08b73f3aadb36a91) unsigned int [timeout\_ms](structwifi__ps__params.md#ad963f1bf78dc271f08b73f3aadb36a91);

[ 725](structwifi__ps__params.md#aef62e5bf6216bf4dc461efe71735c4bd) enum [wifi\_ps\_param\_type](group__wifi__mgmt.md#gabe45d132797047c098041331c8f6f912) [type](structwifi__ps__params.md#aef62e5bf6216bf4dc461efe71735c4bd);

[ 727](structwifi__ps__params.md#a63fa2ee03bc4aefada61c298ee14336c) enum [wifi\_config\_ps\_param\_fail\_reason](group__wifi__mgmt.md#gad98099584d2222ede93aba42b1fbaff0) [fail\_reason](structwifi__ps__params.md#a63fa2ee03bc4aefada61c298ee14336c);

[ 729](structwifi__ps__params.md#ab9fc62dd1e2928320274fa1554a550a6) enum [wifi\_ps\_exit\_strategy](group__wifi__mgmt.md#ga2d424d1711389fb784e916a87ff854b7) [exit\_strategy](structwifi__ps__params.md#ab9fc62dd1e2928320274fa1554a550a6);

730};

731

[ 733](structwifi__twt__params.md)struct [wifi\_twt\_params](structwifi__twt__params.md) {

[ 735](structwifi__twt__params.md#a6f0483861a387651c9c89ba182e064bd) enum [wifi\_twt\_operation](group__wifi__mgmt.md#gad0e998aeb1b27c4f203ca76339d323a3) [operation](structwifi__twt__params.md#a6f0483861a387651c9c89ba182e064bd);

[ 737](structwifi__twt__params.md#a5fd269328f68838b8a7e3a0b93eed894) enum [wifi\_twt\_negotiation\_type](group__wifi__mgmt.md#ga695123cd534e2499f516a07fdc5cafa8) [negotiation\_type](structwifi__twt__params.md#a5fd269328f68838b8a7e3a0b93eed894);

[ 739](structwifi__twt__params.md#a347f8cff73ee6b6ba6d15ddf6f376a2d) enum [wifi\_twt\_setup\_cmd](group__wifi__mgmt.md#ga31c78afc89bfdc4b54cee177843f8022) [setup\_cmd](structwifi__twt__params.md#a347f8cff73ee6b6ba6d15ddf6f376a2d);

[ 741](structwifi__twt__params.md#a805a23284ed4afa46b84efcd43329beb) enum [wifi\_twt\_setup\_resp\_status](group__wifi__mgmt.md#ga4d03aedac13ee4512d7717ac624f319a) [resp\_status](structwifi__twt__params.md#a805a23284ed4afa46b84efcd43329beb);

[ 743](structwifi__twt__params.md#a9faff59e577775b3fe53f2139462ac71) enum [wifi\_twt\_teardown\_status](group__wifi__mgmt.md#gad3709d07aaa3ed59b48f9dd7bd181989) [teardown\_status](structwifi__twt__params.md#a9faff59e577775b3fe53f2139462ac71);

[ 745](structwifi__twt__params.md#adda47e302a87a766f18e28016963a561) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [dialog\_token](structwifi__twt__params.md#adda47e302a87a766f18e28016963a561);

[ 747](structwifi__twt__params.md#a95ec4b32d37309efa47256ae1ea865da) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [flow\_id](structwifi__twt__params.md#a95ec4b32d37309efa47256ae1ea865da);

748 union {

750 struct {

[ 752](structwifi__twt__params.md#ab92fe571559fcd5d97cdf7e6b7d86681) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [twt\_interval](structwifi__twt__params.md#ab92fe571559fcd5d97cdf7e6b7d86681);

[ 754](structwifi__twt__params.md#ae547c6fc1c7cbad15bebcfdaa43f59e7) bool [responder](structwifi__twt__params.md#ae547c6fc1c7cbad15bebcfdaa43f59e7);

[ 756](structwifi__twt__params.md#a4e822c04b52fe6a9489e48e26b8f9382) bool [trigger](structwifi__twt__params.md#a4e822c04b52fe6a9489e48e26b8f9382);

[ 758](structwifi__twt__params.md#a8ea1e2501c8b69dc3fa606eb360f8678) bool [implicit](structwifi__twt__params.md#a8ea1e2501c8b69dc3fa606eb360f8678);

[ 760](structwifi__twt__params.md#a02f2d822d530e5376f256503439a54f9) bool [announce](structwifi__twt__params.md#a02f2d822d530e5376f256503439a54f9);

[ 762](structwifi__twt__params.md#a7c297459a17ed2fd232c62cca63e952f) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [twt\_wake\_interval](structwifi__twt__params.md#a7c297459a17ed2fd232c62cca63e952f);

[ 768](structwifi__twt__params.md#a6f907ca412251fdd7391f29bfa6d7713) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [twt\_wake\_ahead\_duration](structwifi__twt__params.md#a6f907ca412251fdd7391f29bfa6d7713);

[ 770](structwifi__twt__params.md#ac02eab9593b1ec2c9a0453a67076df88) bool [twt\_info\_disable](structwifi__twt__params.md#ac02eab9593b1ec2c9a0453a67076df88);

[ 772](structwifi__twt__params.md#aabb77296f007cb055f78fa1ec3d155a3) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [twt\_exponent](structwifi__twt__params.md#aabb77296f007cb055f78fa1ec3d155a3);

[ 774](structwifi__twt__params.md#aadad4556e2e5405b0703ebb4233a4d17) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [twt\_mantissa](structwifi__twt__params.md#aadad4556e2e5405b0703ebb4233a4d17);

[ 775](structwifi__twt__params.md#aee57c0189b210cfcc18e213e35b9479c) } [setup](structwifi__twt__params.md#aee57c0189b210cfcc18e213e35b9479c);

777 struct {

[ 779](structwifi__twt__params.md#acc7234fa321938e48dd9be23b4bcbade) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [sub\_id](structwifi__twt__params.md#acc7234fa321938e48dd9be23b4bcbade);

[ 781](structwifi__twt__params.md#a91637cecaa940422b08a40f4b830a3d2) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [nominal\_wake](structwifi__twt__params.md#a91637cecaa940422b08a40f4b830a3d2);

[ 783](structwifi__twt__params.md#a1de9544f9bfd441df166ba2413cf11c3) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [max\_sta\_support](structwifi__twt__params.md#a1de9544f9bfd441df166ba2413cf11c3);

785 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [twt\_mantissa](structwifi__twt__params.md#aadad4556e2e5405b0703ebb4233a4d17);

[ 787](structwifi__twt__params.md#a22323b963a01399f26bb02aa95975728) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [twt\_offset](structwifi__twt__params.md#a22323b963a01399f26bb02aa95975728);

789 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [twt\_exponent](structwifi__twt__params.md#aabb77296f007cb055f78fa1ec3d155a3);

[ 791](structwifi__twt__params.md#ada6919e0b201cec5f2c97eeaab46bec7) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [sp\_gap](structwifi__twt__params.md#ada6919e0b201cec5f2c97eeaab46bec7);

[ 792](structwifi__twt__params.md#a72ab809144b1dd3e7e121e489ef399e2) } [btwt](structwifi__twt__params.md#a72ab809144b1dd3e7e121e489ef399e2);

794 struct {

[ 796](structwifi__twt__params.md#a26d6bda00452f77832f69f4465c13efb) bool [teardown\_all](structwifi__twt__params.md#a26d6bda00452f77832f69f4465c13efb);

[ 797](structwifi__twt__params.md#aadf62f6386359ad15491d0073c9065bf) } [teardown](structwifi__twt__params.md#aadf62f6386359ad15491d0073c9065bf);

798 };

[ 800](structwifi__twt__params.md#a70f58b502bb67ef3b2068ded2160b612) enum [wifi\_twt\_fail\_reason](group__wifi__mgmt.md#ga97fa304f9a1db2294a93cccd4c93bcf6) [fail\_reason](structwifi__twt__params.md#a70f58b502bb67ef3b2068ded2160b612);

801};

802

804

805/\* Flow ID is only 3 bits \*/

806#define WIFI\_MAX\_TWT\_FLOWS 8

807#define WIFI\_MAX\_TWT\_INTERVAL\_US (LONG\_MAX - 1)

808/\* 256 (u8) \* 1TU \*/

809#define WIFI\_MAX\_TWT\_WAKE\_INTERVAL\_US 262144

810#define WIFI\_MAX\_TWT\_WAKE\_AHEAD\_DURATION\_US (LONG\_MAX - 1)

811#define WIFI\_MAX\_TWT\_EXPONENT 31

812

814

[ 816](structwifi__twt__flow__info.md)struct [wifi\_twt\_flow\_info](structwifi__twt__flow__info.md) {

[ 818](structwifi__twt__flow__info.md#ae15ba49fa54f82cc6a1fb0d4572114b7) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [twt\_interval](structwifi__twt__flow__info.md#ae15ba49fa54f82cc6a1fb0d4572114b7);

[ 820](structwifi__twt__flow__info.md#a123ce10bed8b62b01919a7ea7644a0ba) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [dialog\_token](structwifi__twt__flow__info.md#a123ce10bed8b62b01919a7ea7644a0ba);

[ 822](structwifi__twt__flow__info.md#acb0c618f1cebcb172f342cfe222683be) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [flow\_id](structwifi__twt__flow__info.md#acb0c618f1cebcb172f342cfe222683be);

[ 824](structwifi__twt__flow__info.md#a620ae8ba546e4091d74280cb1553b2cf) enum [wifi\_twt\_negotiation\_type](group__wifi__mgmt.md#ga695123cd534e2499f516a07fdc5cafa8) [negotiation\_type](structwifi__twt__flow__info.md#a620ae8ba546e4091d74280cb1553b2cf);

[ 826](structwifi__twt__flow__info.md#ac82e4de8ffc82f851061f8ba8d217dc1) bool [responder](structwifi__twt__flow__info.md#ac82e4de8ffc82f851061f8ba8d217dc1);

[ 828](structwifi__twt__flow__info.md#a952a67bd092c5dadba387bb13449c6f3) bool [trigger](structwifi__twt__flow__info.md#a952a67bd092c5dadba387bb13449c6f3);

[ 830](structwifi__twt__flow__info.md#afb480be82d1c6f351bd634fd83bfa5c7) bool [implicit](structwifi__twt__flow__info.md#afb480be82d1c6f351bd634fd83bfa5c7);

[ 832](structwifi__twt__flow__info.md#afc81a5111c265fd9bb2aca5f9510bfa8) bool [announce](structwifi__twt__flow__info.md#afc81a5111c265fd9bb2aca5f9510bfa8);

[ 834](structwifi__twt__flow__info.md#aede6cb0cfc999fac8ded49e2981a3762) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [twt\_wake\_interval](structwifi__twt__flow__info.md#aede6cb0cfc999fac8ded49e2981a3762);

[ 836](structwifi__twt__flow__info.md#a6384d3829d54a58a53eafcb74c64a658) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [twt\_wake\_ahead\_duration](structwifi__twt__flow__info.md#a6384d3829d54a58a53eafcb74c64a658);

837};

838

[ 840](structwifi__enterprise__creds__params.md)struct [wifi\_enterprise\_creds\_params](structwifi__enterprise__creds__params.md) {

[ 842](structwifi__enterprise__creds__params.md#ae37381504a457b2f1d56dd5270c6711d) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[ca\_cert](structwifi__enterprise__creds__params.md#ae37381504a457b2f1d56dd5270c6711d);

[ 844](structwifi__enterprise__creds__params.md#a5f7060fcd2ca3db0b202faf15062564b) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [ca\_cert\_len](structwifi__enterprise__creds__params.md#a5f7060fcd2ca3db0b202faf15062564b);

[ 846](structwifi__enterprise__creds__params.md#a81d61179feba627be5c6456130b9f2af) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[client\_cert](structwifi__enterprise__creds__params.md#a81d61179feba627be5c6456130b9f2af);

[ 848](structwifi__enterprise__creds__params.md#a5f122d59b25b00af2db7eeac93d5482e) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [client\_cert\_len](structwifi__enterprise__creds__params.md#a5f122d59b25b00af2db7eeac93d5482e);

[ 850](structwifi__enterprise__creds__params.md#a8d88f5a8a6ccc8a9a883078af49ae96b) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[client\_key](structwifi__enterprise__creds__params.md#a8d88f5a8a6ccc8a9a883078af49ae96b);

[ 852](structwifi__enterprise__creds__params.md#a09f5b34c81fe871e7513358499518d95) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [client\_key\_len](structwifi__enterprise__creds__params.md#a09f5b34c81fe871e7513358499518d95);

[ 854](structwifi__enterprise__creds__params.md#ad9b867873709d7f2363fef49d7b6f2ca) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[ca\_cert2](structwifi__enterprise__creds__params.md#ad9b867873709d7f2363fef49d7b6f2ca);

[ 856](structwifi__enterprise__creds__params.md#abf35045e71afb0cb9ea25c635c5ac141) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [ca\_cert2\_len](structwifi__enterprise__creds__params.md#abf35045e71afb0cb9ea25c635c5ac141);

[ 858](structwifi__enterprise__creds__params.md#a133126e338d89563733268a03e2fa613) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[client\_cert2](structwifi__enterprise__creds__params.md#a133126e338d89563733268a03e2fa613);

[ 860](structwifi__enterprise__creds__params.md#adbe26c9b88f44eb6b875888f6a03e1bb) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [client\_cert2\_len](structwifi__enterprise__creds__params.md#adbe26c9b88f44eb6b875888f6a03e1bb);

[ 862](structwifi__enterprise__creds__params.md#abcda4d7820681d517d70d8f130b47050) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[client\_key2](structwifi__enterprise__creds__params.md#abcda4d7820681d517d70d8f130b47050);

[ 864](structwifi__enterprise__creds__params.md#a3da90b8a8dfa848f617579760ad4f971) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [client\_key2\_len](structwifi__enterprise__creds__params.md#a3da90b8a8dfa848f617579760ad4f971);

[ 866](structwifi__enterprise__creds__params.md#ad3621e92a1aa968c58a899ace72967db) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[server\_cert](structwifi__enterprise__creds__params.md#ad3621e92a1aa968c58a899ace72967db);

[ 868](structwifi__enterprise__creds__params.md#ad0bfb59d3691e5d21cb4b810c4d1279e) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [server\_cert\_len](structwifi__enterprise__creds__params.md#ad0bfb59d3691e5d21cb4b810c4d1279e);

[ 870](structwifi__enterprise__creds__params.md#acb94a8885b5ab99d1a8fb33dffebc322) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[server\_key](structwifi__enterprise__creds__params.md#acb94a8885b5ab99d1a8fb33dffebc322);

[ 872](structwifi__enterprise__creds__params.md#a9500252974bd15037d4dbc41eba3a27d) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [server\_key\_len](structwifi__enterprise__creds__params.md#a9500252974bd15037d4dbc41eba3a27d);

[ 874](structwifi__enterprise__creds__params.md#ab0fd7419d8a94d1d804e5554acfbf49a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[dh\_param](structwifi__enterprise__creds__params.md#ab0fd7419d8a94d1d804e5554acfbf49a);

[ 876](structwifi__enterprise__creds__params.md#ac548e0b006a9f7b858409cda7c3d34ba) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [dh\_param\_len](structwifi__enterprise__creds__params.md#ac548e0b006a9f7b858409cda7c3d34ba);

877};

878

[ 880](structwifi__ps__config.md)struct [wifi\_ps\_config](structwifi__ps__config.md) {

[ 882](structwifi__ps__config.md#a9e83c10eaaa1d721cbc49b40aedb00df) char [num\_twt\_flows](structwifi__ps__config.md#a9e83c10eaaa1d721cbc49b40aedb00df);

[ 884](structwifi__ps__config.md#ab7460f0f253b2d552e49e98e2c770967) struct [wifi\_twt\_flow\_info](structwifi__twt__flow__info.md) [twt\_flows](structwifi__ps__config.md#ab7460f0f253b2d552e49e98e2c770967)[WIFI\_MAX\_TWT\_FLOWS];

[ 886](structwifi__ps__config.md#a357aafc2dedda37755b1cb1fc07fe5a6) struct [wifi\_ps\_params](structwifi__ps__params.md) [ps\_params](structwifi__ps__config.md#a357aafc2dedda37755b1cb1fc07fe5a6);

887};

888

[ 890](group__wifi__mgmt.md#gae129d0783276e662575af2314eef86cd)enum [wifi\_mgmt\_op](group__wifi__mgmt.md#gae129d0783276e662575af2314eef86cd) {

[ 892](group__wifi__mgmt.md#ggae129d0783276e662575af2314eef86cda6b8183a773e0cdfa85bc4b41ae70fdcd) [WIFI\_MGMT\_GET](group__wifi__mgmt.md#ggae129d0783276e662575af2314eef86cda6b8183a773e0cdfa85bc4b41ae70fdcd) = 0,

[ 894](group__wifi__mgmt.md#ggae129d0783276e662575af2314eef86cdaa0d5931c8275a8d3288ab668b6dfb5a1) [WIFI\_MGMT\_SET](group__wifi__mgmt.md#ggae129d0783276e662575af2314eef86cdaa0d5931c8275a8d3288ab668b6dfb5a1) = 1,

895};

896

[ 898](structwifi__11k__params.md)struct [wifi\_11k\_params](structwifi__11k__params.md) {

[ 900](structwifi__11k__params.md#ae6029ed4bada41f18df0329d0da7401e) enum [wifi\_mgmt\_op](group__wifi__mgmt.md#gae129d0783276e662575af2314eef86cd) [oper](structwifi__11k__params.md#ae6029ed4bada41f18df0329d0da7401e);

[ 902](structwifi__11k__params.md#a739c3e94b025aae2fcf5680aecf3d646) bool [enable\_11k](structwifi__11k__params.md#a739c3e94b025aae2fcf5680aecf3d646);

[ 904](structwifi__11k__params.md#a64ace23c71837417678ceb9cc8d5f216) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [ssid](structwifi__11k__params.md#a64ace23c71837417678ceb9cc8d5f216)[[WIFI\_SSID\_MAX\_LEN](group__wifi__mgmt.md#gad62c60666c9fdffe2e0e9c4388f87886) + 1];

905};

906

[ 908](group__wifi__mgmt.md#ga3a6bfa37bd7850342279d304df20977d)#define MAX\_REG\_CHAN\_NUM 42

909

[ 911](structwifi__reg__chan__info.md)struct [wifi\_reg\_chan\_info](structwifi__reg__chan__info.md) {

[ 913](structwifi__reg__chan__info.md#a0addffc11ef29f50c01b700835e59930) unsigned short [center\_frequency](structwifi__reg__chan__info.md#a0addffc11ef29f50c01b700835e59930);

[ 915](structwifi__reg__chan__info.md#af9169ab4a41fac4c6f6766fc96799545) unsigned short [max\_power](structwifi__reg__chan__info.md#af9169ab4a41fac4c6f6766fc96799545):8;

[ 917](structwifi__reg__chan__info.md#aa044611e18b7332b8577e29f6a769e3f) unsigned short [supported](structwifi__reg__chan__info.md#aa044611e18b7332b8577e29f6a769e3f):1;

[ 919](structwifi__reg__chan__info.md#acc7a88b004c9a61c8bf9ee1a97f85928) unsigned short [passive\_only](structwifi__reg__chan__info.md#acc7a88b004c9a61c8bf9ee1a97f85928):1;

[ 921](structwifi__reg__chan__info.md#a1ab137c142902d2de7d6be2626d7ac1f) unsigned short [dfs](structwifi__reg__chan__info.md#a1ab137c142902d2de7d6be2626d7ac1f):1;

922} \_\_packed;

923

[ 925](structwifi__reg__domain.md)struct [wifi\_reg\_domain](structwifi__reg__domain.md) {

[ 927](structwifi__reg__domain.md#a3bbfdf1497a87bbb6b6211c7035e1002) enum [wifi\_mgmt\_op](group__wifi__mgmt.md#gae129d0783276e662575af2314eef86cd) [oper](structwifi__reg__domain.md#a3bbfdf1497a87bbb6b6211c7035e1002);

[ 931](structwifi__reg__domain.md#a567c6fcae8032567aea83c18cd211c33) bool [force](structwifi__reg__domain.md#a567c6fcae8032567aea83c18cd211c33);

[ 933](structwifi__reg__domain.md#abf191495814c227fbbfaccb2f727762e) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [country\_code](structwifi__reg__domain.md#abf191495814c227fbbfaccb2f727762e)[[WIFI\_COUNTRY\_CODE\_LEN](group__wifi__mgmt.md#ga6766ef7bcb001f1fb526a4083b6cd8bc)];

[ 935](structwifi__reg__domain.md#a3278e9f43893f49ab9f9d0d7f24009c1) unsigned int [num\_channels](structwifi__reg__domain.md#a3278e9f43893f49ab9f9d0d7f24009c1);

[ 937](structwifi__reg__domain.md#a4c8c9c11e41123cd7738fdb0d33ae5fb) struct [wifi\_reg\_chan\_info](structwifi__reg__chan__info.md) \*[chan\_info](structwifi__reg__domain.md#a4c8c9c11e41123cd7738fdb0d33ae5fb);

938};

939

[ 941](group__wifi__mgmt.md#ga38c184ea35c02f304cccdf389ca6d552)enum [wifi\_twt\_sleep\_state](group__wifi__mgmt.md#ga38c184ea35c02f304cccdf389ca6d552) {

[ 943](group__wifi__mgmt.md#gga38c184ea35c02f304cccdf389ca6d552a37a7aba20723b6614e39e1c417f3113c) [WIFI\_TWT\_STATE\_SLEEP](group__wifi__mgmt.md#gga38c184ea35c02f304cccdf389ca6d552a37a7aba20723b6614e39e1c417f3113c) = 0,

[ 945](group__wifi__mgmt.md#gga38c184ea35c02f304cccdf389ca6d552a7b7b45f85d9644f897ca00bd7864e1b0) [WIFI\_TWT\_STATE\_AWAKE](group__wifi__mgmt.md#gga38c184ea35c02f304cccdf389ca6d552a7b7b45f85d9644f897ca00bd7864e1b0) = 1,

946};

947

948#if defined(CONFIG\_WIFI\_MGMT\_RAW\_SCAN\_RESULTS) || defined(\_\_DOXYGEN\_\_)

[ 950](structwifi__raw__scan__result.md)struct [wifi\_raw\_scan\_result](structwifi__raw__scan__result.md) {

[ 952](structwifi__raw__scan__result.md#a3f08580c6448a5fa28dd8a594fa7dad6) [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) [rssi](structwifi__raw__scan__result.md#a3f08580c6448a5fa28dd8a594fa7dad6);

[ 954](structwifi__raw__scan__result.md#a876966f469714eb481b42ccc8a63945c) int [frame\_length](structwifi__raw__scan__result.md#a876966f469714eb481b42ccc8a63945c);

[ 956](structwifi__raw__scan__result.md#aa2c7781882c6775616cbc8016b0842f6) unsigned short [frequency](structwifi__raw__scan__result.md#aa2c7781882c6775616cbc8016b0842f6);

[ 958](structwifi__raw__scan__result.md#a5710e89199c147ce898602795f00aba3) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [data](structwifi__raw__scan__result.md#a5710e89199c147ce898602795f00aba3)[CONFIG\_WIFI\_MGMT\_RAW\_SCAN\_RESULT\_LENGTH];

959};

960#endif /\* CONFIG\_WIFI\_MGMT\_RAW\_SCAN\_RESULTS \*/

961

[ 963](structwifi__ap__sta__info.md)struct [wifi\_ap\_sta\_info](structwifi__ap__sta__info.md) {

[ 965](structwifi__ap__sta__info.md#a7d8bd52340d4937a4b5b7d2c00662441) enum [wifi\_link\_mode](group__wifi__mgmt.md#gabdb2a784d4727b71ab44cca04e422c62) [link\_mode](structwifi__ap__sta__info.md#a7d8bd52340d4937a4b5b7d2c00662441);

[ 967](structwifi__ap__sta__info.md#a7db904376ec73b774aa9d8236c15b3f6) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [mac](structwifi__ap__sta__info.md#a7db904376ec73b774aa9d8236c15b3f6)[[WIFI\_MAC\_ADDR\_LEN](group__wifi__mgmt.md#ga29409ff83a53c6464decdde9bdd04de6)];

[ 969](structwifi__ap__sta__info.md#a7f7c8b144bb3464af5213708591eefda) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [mac\_length](structwifi__ap__sta__info.md#a7f7c8b144bb3464af5213708591eefda);

[ 971](structwifi__ap__sta__info.md#a838c9a4288c9bc7e97afe2334c678f34) bool [twt\_capable](structwifi__ap__sta__info.md#a838c9a4288c9bc7e97afe2334c678f34);

972};

973

975

976/\* for use in max info size calculations \*/

977union wifi\_mgmt\_events {

978 struct [wifi\_scan\_result](structwifi__scan__result.md) scan\_result;

979 struct [wifi\_status](structwifi__status.md) connect\_status;

980 struct [wifi\_iface\_status](structwifi__iface__status.md) iface\_status;

981#ifdef CONFIG\_WIFI\_MGMT\_RAW\_SCAN\_RESULTS

982 struct [wifi\_raw\_scan\_result](structwifi__raw__scan__result.md) raw\_scan\_result;

983#endif /\* CONFIG\_WIFI\_MGMT\_RAW\_SCAN\_RESULTS \*/

984 struct [wifi\_twt\_params](structwifi__twt__params.md) twt\_params;

985 struct [wifi\_ap\_sta\_info](structwifi__ap__sta__info.md) ap\_sta\_info;

986};

987

989

[ 991](structwifi__mode__info.md)struct [wifi\_mode\_info](structwifi__mode__info.md) {

[ 993](structwifi__mode__info.md#aa29d3b88fc718aa3ac05daf38974707d) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [mode](structwifi__mode__info.md#aa29d3b88fc718aa3ac05daf38974707d);

[ 995](structwifi__mode__info.md#add58dd3b45fd2ddaf684d1b0de81bef9) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [if\_index](structwifi__mode__info.md#add58dd3b45fd2ddaf684d1b0de81bef9);

[ 997](structwifi__mode__info.md#a57c101db8b81ab0ac5dd0a158057a64a) enum [wifi\_mgmt\_op](group__wifi__mgmt.md#gae129d0783276e662575af2314eef86cd) [oper](structwifi__mode__info.md#a57c101db8b81ab0ac5dd0a158057a64a);

998};

999

[ 1001](structwifi__filter__info.md)struct [wifi\_filter\_info](structwifi__filter__info.md) {

[ 1003](structwifi__filter__info.md#ad9560be814299055cfa11b995a7dcf42) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [filter](structwifi__filter__info.md#ad9560be814299055cfa11b995a7dcf42);

[ 1005](structwifi__filter__info.md#af9ea91e31e78afcb7ffe1ff9a04277a3) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [if\_index](structwifi__filter__info.md#af9ea91e31e78afcb7ffe1ff9a04277a3);

[ 1007](structwifi__filter__info.md#a1b2d0448fc7f62654e3f5aacfba62f8f) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [buffer\_size](structwifi__filter__info.md#a1b2d0448fc7f62654e3f5aacfba62f8f);

[ 1009](structwifi__filter__info.md#aedd5e220cdde5768cb0f4aff920971cd) enum [wifi\_mgmt\_op](group__wifi__mgmt.md#gae129d0783276e662575af2314eef86cd) [oper](structwifi__filter__info.md#aedd5e220cdde5768cb0f4aff920971cd);

1010};

1011

[ 1013](structwifi__channel__info.md)struct [wifi\_channel\_info](structwifi__channel__info.md) {

[ 1015](structwifi__channel__info.md#a799cbc0a67764f6680322ba0f2ad3300) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [channel](structwifi__channel__info.md#a799cbc0a67764f6680322ba0f2ad3300);

[ 1017](structwifi__channel__info.md#a43a7dd8c19d0c6540e3cc0b5d1d6165d) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [if\_index](structwifi__channel__info.md#a43a7dd8c19d0c6540e3cc0b5d1d6165d);

[ 1019](structwifi__channel__info.md#aa8ef8a71b49ead3664fff9a4d61b1ce8) enum [wifi\_mgmt\_op](group__wifi__mgmt.md#gae129d0783276e662575af2314eef86cd) [oper](structwifi__channel__info.md#aa8ef8a71b49ead3664fff9a4d61b1ce8);

1020};

1021

1023#define WIFI\_AP\_STA\_MAX\_INACTIVITY (LONG\_MAX - 1)

1024#define WIFI\_AP\_IEEE\_80211\_CAPAB\_MAX\_LEN 64

1026

[ 1028](structwifi__ap__config__params.md)struct [wifi\_ap\_config\_params](structwifi__ap__config__params.md) {

[ 1030](structwifi__ap__config__params.md#a4c391cf504a994ed0bc4971afdf76774) enum [wifi\_ap\_config\_param](group__wifi__mgmt.md#ga83546cf946a9123c563609e8903d9642) [type](structwifi__ap__config__params.md#a4c391cf504a994ed0bc4971afdf76774);

[ 1032](structwifi__ap__config__params.md#a289866d9209450e893281b4c198a546a) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [max\_inactivity](structwifi__ap__config__params.md#a289866d9209450e893281b4c198a546a);

[ 1034](structwifi__ap__config__params.md#a7fc0fad99f53ed8e1ac40b74ec98bf9a) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [max\_num\_sta](structwifi__ap__config__params.md#a7fc0fad99f53ed8e1ac40b74ec98bf9a);

[ 1036](structwifi__ap__config__params.md#aba4e43dff01fa026c8dbbfff670d3097) enum [wifi\_frequency\_bandwidths](group__wifi__mgmt.md#ga3b01cead3c2eb4581fe85e2aaaffbd49) [bandwidth](structwifi__ap__config__params.md#aba4e43dff01fa026c8dbbfff670d3097);

1037#if defined(CONFIG\_WIFI\_NM\_HOSTAPD\_AP)

1039 char ht\_capab[WIFI\_AP\_IEEE\_80211\_CAPAB\_MAX\_LEN + 1];

1041 char vht\_capab[WIFI\_AP\_IEEE\_80211\_CAPAB\_MAX\_LEN + 1];

1042#endif

1043};

1044

1045#ifdef CONFIG\_WIFI\_NM\_WPA\_SUPPLICANT\_DPP

1048#define WIFI\_DPP\_QRCODE\_MAX\_LEN 255

1049

1051enum wifi\_dpp\_op {

1053 WIFI\_DPP\_OP\_INVALID = 0,

1055 WIFI\_DPP\_CONFIGURATOR\_ADD,

1057 WIFI\_DPP\_AUTH\_INIT,

1059 WIFI\_DPP\_QR\_CODE,

1061 WIFI\_DPP\_CHIRP,

1063 WIFI\_DPP\_LISTEN,

1065 WIFI\_DPP\_BOOTSTRAP\_GEN,

1067 WIFI\_DPP\_BOOTSTRAP\_GET\_URI,

1069 WIFI\_DPP\_SET\_CONF\_PARAM,

1071 WIFI\_DPP\_SET\_WAIT\_RESP\_TIME,

1073 WIFI\_DPP\_RECONFIG

1074};

1075

1077enum wifi\_dpp\_curves {

1079 WIFI\_DPP\_CURVES\_DEFAULT = 0,

1081 WIFI\_DPP\_CURVES\_P\_256,

1083 WIFI\_DPP\_CURVES\_P\_384,

1085 WIFI\_DPP\_CURVES\_P\_512,

1087 WIFI\_DPP\_CURVES\_BP\_256,

1089 WIFI\_DPP\_CURVES\_BP\_384,

1091 WIFI\_DPP\_CURVES\_BP\_512

1092};

1093

1095enum wifi\_dpp\_role {

1097 WIFI\_DPP\_ROLE\_UNSET = 0,

1099 WIFI\_DPP\_ROLE\_CONFIGURATOR,

1101 WIFI\_DPP\_ROLE\_ENROLLEE,

1103 WIFI\_DPP\_ROLE\_EITHER

1104};

1105

1110enum wifi\_dpp\_conf {

1112 WIFI\_DPP\_CONF\_UNSET = 0,

1114 WIFI\_DPP\_CONF\_STA,

1116 WIFI\_DPP\_CONF\_AP,

1118 WIFI\_DPP\_CONF\_QUERY

1119};

1120

1125enum wifi\_dpp\_bootstrap\_type {

1127 WIFI\_DPP\_BOOTSTRAP\_TYPE\_UNSET = 0,

1129 WIFI\_DPP\_BOOTSTRAP\_TYPE\_QRCODE,

1131 WIFI\_DPP\_BOOTSTRAP\_TYPE\_PKEX,

1133 WIFI\_DPP\_BOOTSTRAP\_TYPE\_NFC\_URI

1134};

1135

1137struct wifi\_dpp\_configurator\_add\_params {

1139 int curve;

1141 int net\_access\_key\_curve;

1142};

1143

1145struct wifi\_dpp\_auth\_init\_params {

1147 int peer;

1149 int configurator;

1151 int role;

1153 int conf;

1155 char ssid[[WIFI\_SSID\_MAX\_LEN](group__wifi__mgmt.md#gad62c60666c9fdffe2e0e9c4388f87886) + 1];

1156};

1157

1159struct wifi\_dpp\_chirp\_params {

1161 int id;

1163 int freq;

1164};

1165

1167struct wifi\_dpp\_listen\_params {

1169 int freq;

1171 int role;

1172};

1173

1175struct wifi\_dpp\_bootstrap\_gen\_params {

1177 int type;

1179 int op\_class;

1181 int chan;

1183 int curve;

1185 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) mac[[WIFI\_MAC\_ADDR\_LEN](group__wifi__mgmt.md#ga29409ff83a53c6464decdde9bdd04de6)];

1186};

1187

1189struct wifi\_dpp\_configurator\_set\_params {

1191 int peer;

1193 int configurator;

1195 int role;

1197 int conf;

1199 int curve;

1201 int net\_access\_key\_curve;

1203 char ssid[[WIFI\_SSID\_MAX\_LEN](group__wifi__mgmt.md#gad62c60666c9fdffe2e0e9c4388f87886) + 1];

1204};

1205

1208struct wifi\_dpp\_params {

1210 int action;

1211 union {

1213 struct wifi\_dpp\_configurator\_add\_params configurator\_add;

1215 struct wifi\_dpp\_auth\_init\_params auth\_init;

1217 struct wifi\_dpp\_chirp\_params chirp;

1219 struct wifi\_dpp\_listen\_params [listen](posix_2sys_2socket_8h.md#a7005ffbeeff92be5394ff3244da79028);

1221 struct wifi\_dpp\_bootstrap\_gen\_params bootstrap\_gen;

1223 struct wifi\_dpp\_configurator\_set\_params configurator\_set;

1225 int id;

1227 int dpp\_resp\_wait\_time;

1229 int network\_id;

1231 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) dpp\_qr\_code[WIFI\_DPP\_QRCODE\_MAX\_LEN + 1];

1236 char resp[WIFI\_DPP\_QRCODE\_MAX\_LEN + 1];

1237 };

1238};

1239#endif /\* CONFIG\_WIFI\_NM\_WPA\_SUPPLICANT\_DPP \*/

1240

[ 1241](group__wifi__mgmt.md#ga234d72d7c881e67ff49fb6c474c622e3)#define WIFI\_WPS\_PIN\_MAX\_LEN 8

1242

[ 1244](group__wifi__mgmt.md#ga4c36ae1a5171d3fbaeebf95c16be496d)enum [wifi\_wps\_op](group__wifi__mgmt.md#ga4c36ae1a5171d3fbaeebf95c16be496d) {

[ 1246](group__wifi__mgmt.md#gga4c36ae1a5171d3fbaeebf95c16be496da093f5b3ef95d9e571ea169430da57e88) [WIFI\_WPS\_PBC](group__wifi__mgmt.md#gga4c36ae1a5171d3fbaeebf95c16be496da093f5b3ef95d9e571ea169430da57e88) = 0,

[ 1248](group__wifi__mgmt.md#gga4c36ae1a5171d3fbaeebf95c16be496da75bd5067903c2bba8a06732f0431393d) [WIFI\_WPS\_PIN\_GET](group__wifi__mgmt.md#gga4c36ae1a5171d3fbaeebf95c16be496da75bd5067903c2bba8a06732f0431393d) = 1,

[ 1250](group__wifi__mgmt.md#gga4c36ae1a5171d3fbaeebf95c16be496da58120620fd2fca80bdac7990ed0e7552) [WIFI\_WPS\_PIN\_SET](group__wifi__mgmt.md#gga4c36ae1a5171d3fbaeebf95c16be496da58120620fd2fca80bdac7990ed0e7552) = 2,

1251};

1252

[ 1254](structwifi__wps__config__params.md)struct [wifi\_wps\_config\_params](structwifi__wps__config__params.md) {

[ 1256](structwifi__wps__config__params.md#aa7a10889c5cd5124983b0f7242d23b7e) enum [wifi\_wps\_op](group__wifi__mgmt.md#ga4c36ae1a5171d3fbaeebf95c16be496d) [oper](structwifi__wps__config__params.md#aa7a10889c5cd5124983b0f7242d23b7e);

[ 1258](structwifi__wps__config__params.md#a962bd6513c564150e0c75112b96bbe15) char [pin](structwifi__wps__config__params.md#a962bd6513c564150e0c75112b96bbe15)[[WIFI\_WPS\_PIN\_MAX\_LEN](group__wifi__mgmt.md#ga234d72d7c881e67ff49fb6c474c622e3) + 1];

1259};

1260

[ 1263](group__wifi__mgmt.md#ga0cc87c00cbee0d0aca833119dbf0d74e)enum [wifi\_sap\_iface\_state](group__wifi__mgmt.md#ga0cc87c00cbee0d0aca833119dbf0d74e) {

[ 1264](group__wifi__mgmt.md#gga0cc87c00cbee0d0aca833119dbf0d74ead92795c629fe828e7efde485eb2761c0) [WIFI\_SAP\_IFACE\_UNINITIALIZED](group__wifi__mgmt.md#gga0cc87c00cbee0d0aca833119dbf0d74ead92795c629fe828e7efde485eb2761c0),

[ 1265](group__wifi__mgmt.md#gga0cc87c00cbee0d0aca833119dbf0d74ea59a8530057e9839d89243558cc366d69) [WIFI\_SAP\_IFACE\_DISABLED](group__wifi__mgmt.md#gga0cc87c00cbee0d0aca833119dbf0d74ea59a8530057e9839d89243558cc366d69),

[ 1266](group__wifi__mgmt.md#gga0cc87c00cbee0d0aca833119dbf0d74ea403d84f907f84492eed8e33713e828ae) [WIFI\_SAP\_IFACE\_COUNTRY\_UPDATE](group__wifi__mgmt.md#gga0cc87c00cbee0d0aca833119dbf0d74ea403d84f907f84492eed8e33713e828ae),

[ 1267](group__wifi__mgmt.md#gga0cc87c00cbee0d0aca833119dbf0d74eab3fea1a0ef90043699cb7d8ab064be7e) [WIFI\_SAP\_IFACE\_ACS](group__wifi__mgmt.md#gga0cc87c00cbee0d0aca833119dbf0d74eab3fea1a0ef90043699cb7d8ab064be7e),

[ 1268](group__wifi__mgmt.md#gga0cc87c00cbee0d0aca833119dbf0d74eaa3a6e6e367c7384379f3c562d1fc358f) [WIFI\_SAP\_IFACE\_HT\_SCAN](group__wifi__mgmt.md#gga0cc87c00cbee0d0aca833119dbf0d74eaa3a6e6e367c7384379f3c562d1fc358f),

[ 1269](group__wifi__mgmt.md#gga0cc87c00cbee0d0aca833119dbf0d74eafdf99a461cf5878240cc40ae4ea7e113) [WIFI\_SAP\_IFACE\_DFS](group__wifi__mgmt.md#gga0cc87c00cbee0d0aca833119dbf0d74eafdf99a461cf5878240cc40ae4ea7e113),

[ 1270](group__wifi__mgmt.md#gga0cc87c00cbee0d0aca833119dbf0d74eaea74f039e6a5abe976e9956b5a01ff1a) [WIFI\_SAP\_IFACE\_NO\_IR](group__wifi__mgmt.md#gga0cc87c00cbee0d0aca833119dbf0d74eaea74f039e6a5abe976e9956b5a01ff1a),

[ 1271](group__wifi__mgmt.md#gga0cc87c00cbee0d0aca833119dbf0d74eaa9133b73b886f2ec543acd282b33eeda) [WIFI\_SAP\_IFACE\_ENABLED](group__wifi__mgmt.md#gga0cc87c00cbee0d0aca833119dbf0d74eaa9133b73b886f2ec543acd282b33eeda)

1272};

1273

1274/\* Extended Capabilities \*/

[ 1275](group__wifi__mgmt.md#ga03ab29789adfe867c4ebaddc39482344)enum [wifi\_ext\_capab](group__wifi__mgmt.md#ga03ab29789adfe867c4ebaddc39482344) {

[ 1276](group__wifi__mgmt.md#gga03ab29789adfe867c4ebaddc39482344abf275508c3f69321cdf704779e976d68) [WIFI\_EXT\_CAPAB\_20\_40\_COEX](group__wifi__mgmt.md#gga03ab29789adfe867c4ebaddc39482344abf275508c3f69321cdf704779e976d68) = 0,

[ 1277](group__wifi__mgmt.md#gga03ab29789adfe867c4ebaddc39482344a1363c1318e4281e057d848194396feb7) [WIFI\_EXT\_CAPAB\_GLK](group__wifi__mgmt.md#gga03ab29789adfe867c4ebaddc39482344a1363c1318e4281e057d848194396feb7) = 1,

[ 1278](group__wifi__mgmt.md#gga03ab29789adfe867c4ebaddc39482344acf854adfca2bb41dd5d75df2b16c3e5e) [WIFI\_EXT\_CAPAB\_EXT\_CHAN\_SWITCH](group__wifi__mgmt.md#gga03ab29789adfe867c4ebaddc39482344acf854adfca2bb41dd5d75df2b16c3e5e) = 2,

[ 1279](group__wifi__mgmt.md#gga03ab29789adfe867c4ebaddc39482344af42762fd723afef7fae98cbefbfff056) [WIFI\_EXT\_CAPAB\_TIM\_BROADCAST](group__wifi__mgmt.md#gga03ab29789adfe867c4ebaddc39482344af42762fd723afef7fae98cbefbfff056) = 18,

[ 1280](group__wifi__mgmt.md#gga03ab29789adfe867c4ebaddc39482344ac5c648efedadc82fae7d9e0851ff71ba) [WIFI\_EXT\_CAPAB\_BSS\_TRANSITION](group__wifi__mgmt.md#gga03ab29789adfe867c4ebaddc39482344ac5c648efedadc82fae7d9e0851ff71ba) = 19,

1281};

1282

1283#include <[zephyr/net/net\_if.h](net__if_8h.md)>

1284

[ 1291](group__wifi__mgmt.md#gad34b366f1c315207ce0da587ca96d8d8)typedef void (\*[scan\_result\_cb\_t](group__wifi__mgmt.md#gad34b366f1c315207ce0da587ca96d8d8))(struct [net\_if](structnet__if.md) \*iface, int status,

1292 struct [wifi\_scan\_result](structwifi__scan__result.md) \*entry);

1293

1294#ifdef CONFIG\_WIFI\_MGMT\_RAW\_SCAN\_RESULTS

1301typedef void (\*raw\_scan\_result\_cb\_t)(struct [net\_if](structnet__if.md) \*iface, int status,

1302 struct [wifi\_raw\_scan\_result](structwifi__raw__scan__result.md) \*entry);

1303#endif /\* CONFIG\_WIFI\_MGMT\_RAW\_SCAN\_RESULTS \*/

1304

[ 1306](structwifi__mgmt__ops.md)struct [wifi\_mgmt\_ops](structwifi__mgmt__ops.md) {

[ 1318](structwifi__mgmt__ops.md#a267030c27da3cdc251badd0ed7f7b1cb) int (\*[scan](structwifi__mgmt__ops.md#a267030c27da3cdc251badd0ed7f7b1cb))(const struct [device](structdevice.md) \*dev,

1319 struct [wifi\_scan\_params](structwifi__scan__params.md) \*params,

1320 [scan\_result\_cb\_t](group__wifi__mgmt.md#gad34b366f1c315207ce0da587ca96d8d8) cb);

[ 1328](structwifi__mgmt__ops.md#ae6255ea77739918797b4f3c7a4634a75) int (\*[connect](structwifi__mgmt__ops.md#ae6255ea77739918797b4f3c7a4634a75))(const struct [device](structdevice.md) \*dev,

1329 struct [wifi\_connect\_req\_params](structwifi__connect__req__params.md) \*params);

[ 1336](structwifi__mgmt__ops.md#a5725c6fd93ae189a3019374cd4ad2ff4) int (\*[disconnect](structwifi__mgmt__ops.md#a5725c6fd93ae189a3019374cd4ad2ff4))(const struct [device](structdevice.md) \*dev);

[ 1344](structwifi__mgmt__ops.md#ac2ce3a4a86c43e30d33261f71c44198a) int (\*[ap\_enable](structwifi__mgmt__ops.md#ac2ce3a4a86c43e30d33261f71c44198a))(const struct [device](structdevice.md) \*dev,

1345 struct [wifi\_connect\_req\_params](structwifi__connect__req__params.md) \*params);

[ 1352](structwifi__mgmt__ops.md#a5aa7a2be82eb1783872abda2b8978235) int (\*[ap\_disable](structwifi__mgmt__ops.md#a5aa7a2be82eb1783872abda2b8978235))(const struct [device](structdevice.md) \*dev);

[ 1360](structwifi__mgmt__ops.md#af01aaec29be78c02314acf13b5c1b6f7) int (\*[ap\_sta\_disconnect](structwifi__mgmt__ops.md#af01aaec29be78c02314acf13b5c1b6f7))(const struct [device](structdevice.md) \*dev, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*mac);

[ 1368](structwifi__mgmt__ops.md#adf157476d776bc9c068e99e1a0266fd3) int (\*[iface\_status](structwifi__mgmt__ops.md#adf157476d776bc9c068e99e1a0266fd3))(const struct [device](structdevice.md) \*dev, struct [wifi\_iface\_status](structwifi__iface__status.md) \*status);

1369#if defined(CONFIG\_NET\_STATISTICS\_WIFI) || defined(\_\_DOXYGEN\_\_)

[ 1377](structwifi__mgmt__ops.md#a5e6fdf836273fcde54efff4c77bfdf0e) int (\*[get\_stats](structwifi__mgmt__ops.md#a5e6fdf836273fcde54efff4c77bfdf0e))(const struct [device](structdevice.md) \*dev, struct [net\_stats\_wifi](structnet__stats__wifi.md) \*stats);

[ 1384](structwifi__mgmt__ops.md#ae66901b434ab02863c0d3bd539c4b650) int (\*[reset\_stats](structwifi__mgmt__ops.md#ae66901b434ab02863c0d3bd539c4b650))(const struct [device](structdevice.md) \*dev);

1385#endif /\* CONFIG\_NET\_STATISTICS\_WIFI \*/

[ 1393](structwifi__mgmt__ops.md#a2cf66093ad850319cf222468e22ff485) int (\*[cfg\_11k](structwifi__mgmt__ops.md#a2cf66093ad850319cf222468e22ff485))(const struct [device](structdevice.md) \*dev, struct [wifi\_11k\_params](structwifi__11k__params.md) \*params);

[ 1401](structwifi__mgmt__ops.md#a1cdd0b76a0a326e968d27c0a3cafcef8) int (\*[send\_11k\_neighbor\_request](structwifi__mgmt__ops.md#a1cdd0b76a0a326e968d27c0a3cafcef8))(const struct [device](structdevice.md) \*dev, struct [wifi\_11k\_params](structwifi__11k__params.md) \*params);

[ 1409](structwifi__mgmt__ops.md#ac0f3f7fa699b1bc7db2358e77dd44cc4) int (\*[set\_power\_save](structwifi__mgmt__ops.md#ac0f3f7fa699b1bc7db2358e77dd44cc4))(const struct [device](structdevice.md) \*dev, struct [wifi\_ps\_params](structwifi__ps__params.md) \*params);

[ 1417](structwifi__mgmt__ops.md#ab4500534b6abe0449290c8bd8f729fc4) int (\*[set\_twt](structwifi__mgmt__ops.md#ab4500534b6abe0449290c8bd8f729fc4))(const struct [device](structdevice.md) \*dev, struct [wifi\_twt\_params](structwifi__twt__params.md) \*params);

[ 1425](structwifi__mgmt__ops.md#ad2d1ab4db1947dbdb2909a675fa1d653) int (\*[set\_btwt](structwifi__mgmt__ops.md#ad2d1ab4db1947dbdb2909a675fa1d653))(const struct [device](structdevice.md) \*dev, struct [wifi\_twt\_params](structwifi__twt__params.md) \*params);

[ 1433](structwifi__mgmt__ops.md#a52690b13f8a1e7b0c2302eaa24ae4c7f) int (\*[get\_power\_save\_config](structwifi__mgmt__ops.md#a52690b13f8a1e7b0c2302eaa24ae4c7f))(const struct [device](structdevice.md) \*dev, struct [wifi\_ps\_config](structwifi__ps__config.md) \*config);

[ 1441](structwifi__mgmt__ops.md#a0a287c8acf2d7bf9333b755589294881) int (\*[reg\_domain](structwifi__mgmt__ops.md#a0a287c8acf2d7bf9333b755589294881))(const struct [device](structdevice.md) \*dev, struct [wifi\_reg\_domain](structwifi__reg__domain.md) \*[reg\_domain](structwifi__mgmt__ops.md#a0a287c8acf2d7bf9333b755589294881));

[ 1449](structwifi__mgmt__ops.md#ad645276745ce8dd9685e0744efdfc733) int (\*[filter](structwifi__mgmt__ops.md#ad645276745ce8dd9685e0744efdfc733))(const struct [device](structdevice.md) \*dev, struct [wifi\_filter\_info](structwifi__filter__info.md) \*[filter](structwifi__mgmt__ops.md#ad645276745ce8dd9685e0744efdfc733));

[ 1457](structwifi__mgmt__ops.md#ae2fb1bc35bf9255655a30a2ad8588b7c) int (\*[mode](structwifi__mgmt__ops.md#ae2fb1bc35bf9255655a30a2ad8588b7c))(const struct [device](structdevice.md) \*dev, struct [wifi\_mode\_info](structwifi__mode__info.md) \*[mode](structwifi__mgmt__ops.md#ae2fb1bc35bf9255655a30a2ad8588b7c));

[ 1465](structwifi__mgmt__ops.md#af17ddfea01d0ab478f6fd50b1c9d6015) int (\*[channel](structwifi__mgmt__ops.md#af17ddfea01d0ab478f6fd50b1c9d6015))(const struct [device](structdevice.md) \*dev, struct [wifi\_channel\_info](structwifi__channel__info.md) \*[channel](structwifi__mgmt__ops.md#af17ddfea01d0ab478f6fd50b1c9d6015));

1466

[ 1474](structwifi__mgmt__ops.md#a3437f5881a8e0a487c11dd43a6099b6d) int (\*[btm\_query](structwifi__mgmt__ops.md#a3437f5881a8e0a487c11dd43a6099b6d))(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) reason);

[ 1482](structwifi__mgmt__ops.md#afb83b59f392b11fe8071ca57e3ea3928) int (\*[bss\_ext\_capab](structwifi__mgmt__ops.md#afb83b59f392b11fe8071ca57e3ea3928))(const struct [device](structdevice.md) \*dev, int capab);

1483

[ 1490](structwifi__mgmt__ops.md#aa088223f84094614145d9d81e3acc20a) int (\*[legacy\_roam](structwifi__mgmt__ops.md#aa088223f84094614145d9d81e3acc20a))(const struct [device](structdevice.md) \*dev);

1491

[ 1504](structwifi__mgmt__ops.md#aa7e4bc3dbc960091d11ffe5454259885) int (\*[get\_version](structwifi__mgmt__ops.md#aa7e4bc3dbc960091d11ffe5454259885))(const struct [device](structdevice.md) \*dev, struct [wifi\_version](structwifi__version.md) \*params);

[ 1512](structwifi__mgmt__ops.md#a42c2aa55df30158d8b5d6f4c81e3e2dd) int (\*[get\_conn\_params](structwifi__mgmt__ops.md#a42c2aa55df30158d8b5d6f4c81e3e2dd))(const struct [device](structdevice.md) \*dev, struct [wifi\_connect\_req\_params](structwifi__connect__req__params.md) \*params);

[ 1520](structwifi__mgmt__ops.md#a514e06d63bcf6dc11dba1d3af8d102d5) int (\*[set\_rts\_threshold](structwifi__mgmt__ops.md#a514e06d63bcf6dc11dba1d3af8d102d5))(const struct [device](structdevice.md) \*dev, unsigned int rts\_threshold);

[ 1528](structwifi__mgmt__ops.md#a2475f32afcce72464b2db6ecad7fb3eb) int (\*[ap\_config\_params](structwifi__mgmt__ops.md#a2475f32afcce72464b2db6ecad7fb3eb))(const struct [device](structdevice.md) \*dev, struct [wifi\_ap\_config\_params](structwifi__ap__config__params.md) \*params);

1529

1530#ifdef CONFIG\_WIFI\_NM\_WPA\_SUPPLICANT\_DPP

1538 int (\*dpp\_dispatch)(const struct [device](structdevice.md) \*dev, struct wifi\_dpp\_params \*params);

1539#endif /\* CONFIG\_WIFI\_NM\_WPA\_SUPPLICANT\_DPP \*/

[ 1546](structwifi__mgmt__ops.md#aadf991d6f6725e5c179ca8343d626ad8) int (\*[pmksa\_flush](structwifi__mgmt__ops.md#aadf991d6f6725e5c179ca8343d626ad8))(const struct [device](structdevice.md) \*dev);

1554#ifdef CONFIG\_WIFI\_NM\_WPA\_SUPPLICANT\_CRYPTO\_ENTERPRISE

1555 int (\*enterprise\_creds)(const struct [device](structdevice.md) \*dev,

1556 struct [wifi\_enterprise\_creds\_params](structwifi__enterprise__creds__params.md) \*creds);

1557#endif

[ 1565](structwifi__mgmt__ops.md#a20706f9eed43b3380258b62fdf93be02) int (\*[get\_rts\_threshold](structwifi__mgmt__ops.md#a20706f9eed43b3380258b62fdf93be02))(const struct [device](structdevice.md) \*dev, unsigned int \*rts\_threshold);

[ 1573](structwifi__mgmt__ops.md#aaf85f7b56997fb40689b927535af5e85) int (\*[wps\_config](structwifi__mgmt__ops.md#aaf85f7b56997fb40689b927535af5e85))(const struct [device](structdevice.md) \*dev, struct [wifi\_wps\_config\_params](structwifi__wps__config__params.md) \*params);

[ 1581](structwifi__mgmt__ops.md#a538ffba0a7e045ca9c8ac62ccefc8a36) int (\*[candidate\_scan](structwifi__mgmt__ops.md#a538ffba0a7e045ca9c8ac62ccefc8a36))(const struct [device](structdevice.md) \*dev, struct [wifi\_scan\_params](structwifi__scan__params.md) \*params);

[ 1588](structwifi__mgmt__ops.md#a501b114298738ac6af9c4a80f5360d79) int (\*[start\_11r\_roaming](structwifi__mgmt__ops.md#a501b114298738ac6af9c4a80f5360d79))(const struct [device](structdevice.md) \*dev);

1589};

1590

[ 1592](structnet__wifi__mgmt__offload.md)struct [net\_wifi\_mgmt\_offload](structnet__wifi__mgmt__offload.md) {

1599#if defined(CONFIG\_WIFI\_USE\_NATIVE\_NETWORKING) || defined(\_\_DOXYGEN\_\_)

[ 1601](structnet__wifi__mgmt__offload.md#a1d34a954a2f16d29f51dc51dd6fbb845) struct [ethernet\_api](structethernet__api.md) [wifi\_iface](structnet__wifi__mgmt__offload.md#a1d34a954a2f16d29f51dc51dd6fbb845);

1602#else

1604 struct [offloaded\_if\_api](structoffloaded__if__api.md) [wifi\_iface](structnet__wifi__mgmt__offload.md#a1d34a954a2f16d29f51dc51dd6fbb845);

1605#endif

[ 1607](structnet__wifi__mgmt__offload.md#a98fcc053d9820d2d981ed659520c9b3b) const struct [wifi\_mgmt\_ops](structwifi__mgmt__ops.md) \*const [wifi\_mgmt\_api](structnet__wifi__mgmt__offload.md#a98fcc053d9820d2d981ed659520c9b3b);

1608

1609#if defined(CONFIG\_WIFI\_NM\_WPA\_SUPPLICANT) || defined(\_\_DOXYGEN\_\_)

[ 1611](structnet__wifi__mgmt__offload.md#a991e0bc6247578a3d1c9d2d3ab0b63d7) const void \*[wifi\_drv\_ops](structnet__wifi__mgmt__offload.md#a991e0bc6247578a3d1c9d2d3ab0b63d7);

1612#endif

1613};

1614

1615#if defined(CONFIG\_WIFI\_NM\_WPA\_SUPPLICANT)

1616/\* Make sure wifi\_drv\_ops is after wifi\_mgmt\_api \*/

1617BUILD\_ASSERT(offsetof(struct [net\_wifi\_mgmt\_offload](structnet__wifi__mgmt__offload.md), wifi\_mgmt\_api) <

1618 offsetof(struct [net\_wifi\_mgmt\_offload](structnet__wifi__mgmt__offload.md), wifi\_drv\_ops));

1619#endif

1620

1621/\* Make sure that the network interface API is properly setup inside

1622 \* Wifi mgmt offload API struct (it is the first one).

1623 \*/

1624BUILD\_ASSERT(offsetof(struct [net\_wifi\_mgmt\_offload](structnet__wifi__mgmt__offload.md), wifi\_iface) == 0);

1625

[ 1631](group__wifi__mgmt.md#ga036416696b1e3bc458ddbaf07a08d69d)void [wifi\_mgmt\_raise\_connect\_result\_event](group__wifi__mgmt.md#ga036416696b1e3bc458ddbaf07a08d69d)(struct [net\_if](structnet__if.md) \*iface, int status);

1632

[ 1638](group__wifi__mgmt.md#ga3b6edcf9b51afbf7a327d1a344bd7b87)void [wifi\_mgmt\_raise\_disconnect\_result\_event](group__wifi__mgmt.md#ga3b6edcf9b51afbf7a327d1a344bd7b87)(struct [net\_if](structnet__if.md) \*iface, int status);

1639

[ 1645](group__wifi__mgmt.md#ga7da6af0747bcba85f8afab30c92b5b43)void [wifi\_mgmt\_raise\_iface\_status\_event](group__wifi__mgmt.md#ga7da6af0747bcba85f8afab30c92b5b43)(struct [net\_if](structnet__if.md) \*iface,

1646 struct [wifi\_iface\_status](structwifi__iface__status.md) \*[iface\_status](structwifi__mgmt__ops.md#adf157476d776bc9c068e99e1a0266fd3));

1647

[ 1653](group__wifi__mgmt.md#ga39404d15243ca084b253cae8fc07e374)void [wifi\_mgmt\_raise\_twt\_event](group__wifi__mgmt.md#ga39404d15243ca084b253cae8fc07e374)(struct [net\_if](structnet__if.md) \*iface,

1654 struct [wifi\_twt\_params](structwifi__twt__params.md) \*twt\_params);

1655

[ 1661](group__wifi__mgmt.md#ga18f09a3196588b51d6c0644f82f639d7)void [wifi\_mgmt\_raise\_twt\_sleep\_state](group__wifi__mgmt.md#ga18f09a3196588b51d6c0644f82f639d7)(struct [net\_if](structnet__if.md) \*iface, int twt\_sleep\_state);

1662

1663#if defined(CONFIG\_WIFI\_MGMT\_RAW\_SCAN\_RESULTS) || defined(\_\_DOXYGEN\_\_)

[ 1669](group__wifi__mgmt.md#ga71c99913bded844c4ca32ed9155bc470)void [wifi\_mgmt\_raise\_raw\_scan\_result\_event](group__wifi__mgmt.md#ga71c99913bded844c4ca32ed9155bc470)(struct [net\_if](structnet__if.md) \*iface,

1670 struct [wifi\_raw\_scan\_result](structwifi__raw__scan__result.md) \*raw\_scan\_info);

1671#endif /\* CONFIG\_WIFI\_MGMT\_RAW\_SCAN\_RESULTS \*/

1672

[ 1678](group__wifi__mgmt.md#gaa75246d6dc55dada389c9d31e2607d5c)void [wifi\_mgmt\_raise\_disconnect\_complete\_event](group__wifi__mgmt.md#gaa75246d6dc55dada389c9d31e2607d5c)(struct [net\_if](structnet__if.md) \*iface, int status);

1679

1680#ifdef CONFIG\_WIFI\_NM\_WPA\_SUPPLICANT\_ROAMING

1687void wifi\_mgmt\_raise\_neighbor\_rep\_recv\_event(struct [net\_if](structnet__if.md) \*iface,

1688 char \*inbuf, size\_t buf\_len);

1689#endif

1690

[ 1696](group__wifi__mgmt.md#ga67b52edeff76c2211b038f4aa90b8982)void [wifi\_mgmt\_raise\_ap\_enable\_result\_event](group__wifi__mgmt.md#ga67b52edeff76c2211b038f4aa90b8982)(struct [net\_if](structnet__if.md) \*iface, enum [wifi\_ap\_status](group__wifi__mgmt.md#gaaf730bf76adc06434c7ac63bf0417884) status);

1697

[ 1703](group__wifi__mgmt.md#gadee15c6a492a8ee13bea43812debb5d9)void [wifi\_mgmt\_raise\_ap\_disable\_result\_event](group__wifi__mgmt.md#gadee15c6a492a8ee13bea43812debb5d9)(struct [net\_if](structnet__if.md) \*iface, enum [wifi\_ap\_status](group__wifi__mgmt.md#gaaf730bf76adc06434c7ac63bf0417884) status);

1704

[ 1710](group__wifi__mgmt.md#gac8f17f0aa3e426a5cdb731727b9b9ce3)void [wifi\_mgmt\_raise\_ap\_sta\_connected\_event](group__wifi__mgmt.md#gac8f17f0aa3e426a5cdb731727b9b9ce3)(struct [net\_if](structnet__if.md) \*iface,

1711 struct [wifi\_ap\_sta\_info](structwifi__ap__sta__info.md) \*sta\_info);

1712

[ 1717](group__wifi__mgmt.md#ga49fb9c3908be61d847b31c99be6afc42)void [wifi\_mgmt\_raise\_ap\_sta\_disconnected\_event](group__wifi__mgmt.md#ga49fb9c3908be61d847b31c99be6afc42)(struct [net\_if](structnet__if.md) \*iface,

1718 struct [wifi\_ap\_sta\_info](structwifi__ap__sta__info.md) \*sta\_info);

1719

1723#ifdef \_\_cplusplus

1724}

1725#endif

1726

1727#endif /\* ZEPHYR\_INCLUDE\_NET\_WIFI\_MGMT\_H\_ \*/

[ethernet.h](ethernet_8h.md)

Ethernet.

[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)

#define NET\_MGMT\_DEFINE\_REQUEST\_HANDLER(\_mgmt\_request)

Declare a request handler function for the given network event.

**Definition** net\_mgmt.h:111

[wifi\_mgmt\_raise\_connect\_result\_event](group__wifi__mgmt.md#ga036416696b1e3bc458ddbaf07a08d69d)

void wifi\_mgmt\_raise\_connect\_result\_event(struct net\_if \*iface, int status)

Wi-Fi management connect result event.

[wifi\_ext\_capab](group__wifi__mgmt.md#ga03ab29789adfe867c4ebaddc39482344)

wifi\_ext\_capab

**Definition** wifi\_mgmt.h:1275

[wifi\_sap\_iface\_state](group__wifi__mgmt.md#ga0cc87c00cbee0d0aca833119dbf0d74e)

wifi\_sap\_iface\_state

Wi-Fi AP status.

**Definition** wifi\_mgmt.h:1263

[wifi\_ps](group__wifi__mgmt.md#ga0fffeb57b68fb8cdef9d3d571368b8ca)

wifi\_ps

Wi-Fi power save states.

**Definition** wifi.h:414

[NET\_REQUEST\_WIFI\_PS\_CONFIG](group__wifi__mgmt.md#ga1032f3773cfe6130da4d4d498b044ee2)

#define NET\_REQUEST\_WIFI\_PS\_CONFIG

Request a Wi-Fi power save configuration.

**Definition** wifi\_mgmt.h:211

[wifi\_mgmt\_raise\_twt\_sleep\_state](group__wifi__mgmt.md#ga18f09a3196588b51d6c0644f82f639d7)

void wifi\_mgmt\_raise\_twt\_sleep\_state(struct net\_if \*iface, int twt\_sleep\_state)

Wi-Fi management TWT sleep state event.

[NET\_REQUEST\_WIFI\_SCAN](group__wifi__mgmt.md#ga1c277da90986fa52dca182c4d922646f)

#define NET\_REQUEST\_WIFI\_SCAN

Request a Wi-Fi scan.

**Definition** wifi\_mgmt.h:142

[wifi\_frequency\_bands](group__wifi__mgmt.md#ga1e2f0439a322355fa7368ea880c9c15d)

wifi\_frequency\_bands

IEEE 802.11 operational frequency bands (not exhaustive).

**Definition** wifi.h:233

[wifi\_mfp\_options](group__wifi__mgmt.md#ga1f252da47d9650023d7fff6d08e49c76)

wifi\_mfp\_options

IEEE 802.11w - Management frame protection.

**Definition** wifi.h:212

[NET\_REQUEST\_WIFI\_RTS\_THRESHOLD](group__wifi__mgmt.md#ga22d80ef0ffb15e4286d7b1c3325d5334)

#define NET\_REQUEST\_WIFI\_RTS\_THRESHOLD

Request a Wi-Fi RTS threshold.

**Definition** wifi\_mgmt.h:259

[WIFI\_WPS\_PIN\_MAX\_LEN](group__wifi__mgmt.md#ga234d72d7c881e67ff49fb6c474c622e3)

#define WIFI\_WPS\_PIN\_MAX\_LEN

**Definition** wifi\_mgmt.h:1241

[NET\_REQUEST\_WIFI\_RTS\_THRESHOLD\_CONFIG](group__wifi__mgmt.md#ga2678ea372335af008d9bd3333f7a7de1)

#define NET\_REQUEST\_WIFI\_RTS\_THRESHOLD\_CONFIG

Request a Wi-Fi RTS threshold configuration.

**Definition** wifi\_mgmt.h:296

[WIFI\_MAC\_ADDR\_LEN](group__wifi__mgmt.md#ga29409ff83a53c6464decdde9bdd04de6)

#define WIFI\_MAC\_ADDR\_LEN

MAC address length.

**Definition** wifi.h:282

[NET\_REQUEST\_WIFI\_REG\_DOMAIN](group__wifi__mgmt.md#ga2b27d102b779a6d846b375854768fb7f)

#define NET\_REQUEST\_WIFI\_REG\_DOMAIN

Request a Wi-Fi regulatory domain.

**Definition** wifi\_mgmt.h:217

[wifi\_ps\_exit\_strategy](group__wifi__mgmt.md#ga2d424d1711389fb784e916a87ff854b7)

wifi\_ps\_exit\_strategy

Wi-Fi power save exit strategy.

**Definition** wifi.h:623

[NET\_REQUEST\_WIFI\_PACKET\_FILTER](group__wifi__mgmt.md#ga3098e817d12bf4619c9fd2698508fb4e)

#define NET\_REQUEST\_WIFI\_PACKET\_FILTER

Request Wi-Fi packet filter.

**Definition** wifi\_mgmt.h:229

[wifi\_twt\_setup\_cmd](group__wifi__mgmt.md#ga31c78afc89bfdc4b54cee177843f8022)

wifi\_twt\_setup\_cmd

Wi-Fi Target Wake Time (TWT) setup commands.

**Definition** wifi.h:496

[NET\_REQUEST\_WIFI\_NEIGHBOR\_REP\_COMPLETE](group__wifi__mgmt.md#ga373031970a29331bf1b30d1654c128f0)

#define NET\_REQUEST\_WIFI\_NEIGHBOR\_REP\_COMPLETE

**Definition** wifi\_mgmt.h:315

[wifi\_twt\_sleep\_state](group__wifi__mgmt.md#ga38c184ea35c02f304cccdf389ca6d552)

wifi\_twt\_sleep\_state

Wi-Fi TWT sleep states.

**Definition** wifi\_mgmt.h:941

[wifi\_mgmt\_raise\_twt\_event](group__wifi__mgmt.md#ga39404d15243ca084b253cae8fc07e374)

void wifi\_mgmt\_raise\_twt\_event(struct net\_if \*iface, struct wifi\_twt\_params \*twt\_params)

Wi-Fi management TWT event.

[wifi\_frequency\_bandwidths](group__wifi__mgmt.md#ga3b01cead3c2eb4581fe85e2aaaffbd49)

wifi\_frequency\_bandwidths

IEEE 802.11 operational frequency bandwidths (not exhaustive).

**Definition** wifi.h:255

[wifi\_mgmt\_raise\_disconnect\_result\_event](group__wifi__mgmt.md#ga3b6edcf9b51afbf7a327d1a344bd7b87)

void wifi\_mgmt\_raise\_disconnect\_result\_event(struct net\_if \*iface, int status)

Wi-Fi management disconnect result event.

[NET\_REQUEST\_WIFI\_IFACE\_STATUS](group__wifi__mgmt.md#ga3e45f6ee3801553619d8eb7d0af506eb)

#define NET\_REQUEST\_WIFI\_IFACE\_STATUS

Request a Wi-Fi network interface status.

**Definition** wifi\_mgmt.h:178

[NET\_REQUEST\_WIFI\_VERSION](group__wifi__mgmt.md#ga3e60c29ca9ce95d17a7fff087290f7f1)

#define NET\_REQUEST\_WIFI\_VERSION

Request a Wi-Fi version.

**Definition** wifi\_mgmt.h:247

[wifi\_wpa3\_enterprise\_type](group__wifi__mgmt.md#ga48fea1f0c7d2700cef47068f96c6b71a)

wifi\_wpa3\_enterprise\_type

WPA3 Enterprise security types.

**Definition** wifi.h:118

[wifi\_mgmt\_raise\_ap\_sta\_disconnected\_event](group__wifi__mgmt.md#ga49fb9c3908be61d847b31c99be6afc42)

void wifi\_mgmt\_raise\_ap\_sta\_disconnected\_event(struct net\_if \*iface, struct wifi\_ap\_sta\_info \*sta\_info)

Wi-Fi management AP mode STA disconnected event.

[NET\_REQUEST\_WIFI\_11K\_NEIGHBOR\_REQUEST](group__wifi__mgmt.md#ga4a2b1e8befd7376749b1d4fbcf98376f)

#define NET\_REQUEST\_WIFI\_11K\_NEIGHBOR\_REQUEST

**Definition** wifi\_mgmt.h:188

[wifi\_wps\_op](group__wifi__mgmt.md#ga4c36ae1a5171d3fbaeebf95c16be496d)

wifi\_wps\_op

Operation for WPS.

**Definition** wifi\_mgmt.h:1244

[wifi\_twt\_setup\_resp\_status](group__wifi__mgmt.md#ga4d03aedac13ee4512d7717ac624f319a)

wifi\_twt\_setup\_resp\_status

Wi-Fi Target Wake Time (TWT) negotiation status.

**Definition** wifi.h:519

[NET\_REQUEST\_WIFI\_BTM\_QUERY](group__wifi__mgmt.md#ga4f644b4c980628ffd556458eddc0933d)

#define NET\_REQUEST\_WIFI\_BTM\_QUERY

Request a Wi-Fi BTM query.

**Definition** wifi\_mgmt.h:279

[wifi\_iface\_mode](group__wifi__mgmt.md#ga584f6239ac14e2bedc5e6bd72756423b)

wifi\_iface\_mode

Wi-Fi interface modes.

**Definition** wifi.h:347

[NET\_REQUEST\_WIFI\_AP\_ENABLE](group__wifi__mgmt.md#ga638d2eb0a5029c1af46a91b523ed8589)

#define NET\_REQUEST\_WIFI\_AP\_ENABLE

Request a Wi-Fi access point enable.

**Definition** wifi\_mgmt.h:160

[NET\_REQUEST\_WIFI\_WPS\_CONFIG](group__wifi__mgmt.md#ga649a63bc7d315ebdd89464ff48b3fada)

#define NET\_REQUEST\_WIFI\_WPS\_CONFIG

**Definition** wifi\_mgmt.h:301

[WIFI\_COUNTRY\_CODE\_LEN](group__wifi__mgmt.md#ga6766ef7bcb001f1fb526a4083b6cd8bc)

#define WIFI\_COUNTRY\_CODE\_LEN

Length of the country code string.

**Definition** wifi.h:28

[wifi\_mgmt\_raise\_ap\_enable\_result\_event](group__wifi__mgmt.md#ga67b52edeff76c2211b038f4aa90b8982)

void wifi\_mgmt\_raise\_ap\_enable\_result\_event(struct net\_if \*iface, enum wifi\_ap\_status status)

Wi-Fi management AP mode enable result event.

[NET\_REQUEST\_WIFI\_PS](group__wifi__mgmt.md#ga68aaced888f98e1ba4e6b61b53e5e2ba)

#define NET\_REQUEST\_WIFI\_PS

Request a Wi-Fi power save.

**Definition** wifi\_mgmt.h:194

[wifi\_twt\_negotiation\_type](group__wifi__mgmt.md#ga695123cd534e2499f516a07fdc5cafa8)

wifi\_twt\_negotiation\_type

Wi-Fi Target Wake Time (TWT) negotiation types.

**Definition** wifi.h:483

[wifi\_mgmt\_raise\_raw\_scan\_result\_event](group__wifi__mgmt.md#ga71c99913bded844c4ca32ed9155bc470)

void wifi\_mgmt\_raise\_raw\_scan\_result\_event(struct net\_if \*iface, struct wifi\_raw\_scan\_result \*raw\_scan\_info)

Wi-Fi management raw scan result event.

[wifi\_mgmt\_raise\_iface\_status\_event](group__wifi__mgmt.md#ga7da6af0747bcba85f8afab30c92b5b43)

void wifi\_mgmt\_raise\_iface\_status\_event(struct net\_if \*iface, struct wifi\_iface\_status \*iface\_status)

Wi-Fi management interface status event.

[wifi\_ap\_config\_param](group__wifi__mgmt.md#ga83546cf946a9123c563609e8903d9642)

wifi\_ap\_config\_param

Wi-Fi AP mode configuration parameter.

**Definition** wifi.h:698

[wifi\_conn\_status](group__wifi__mgmt.md#ga86a5741e54aeb3e290142b0de217b8a8)

wifi\_conn\_status

Wi-Fi connect result codes.

**Definition** wifi\_mgmt.h:593

[NET\_REQUEST\_WIFI\_START\_ROAMING](group__wifi__mgmt.md#ga89cc123bb5c30140d2ce0a8b741b1086)

#define NET\_REQUEST\_WIFI\_START\_ROAMING

**Definition** wifi\_mgmt.h:310

[NET\_REQUEST\_WIFI\_PMKSA\_FLUSH](group__wifi__mgmt.md#ga9070995249eb35de37e2b60c4426f840)

#define NET\_REQUEST\_WIFI\_PMKSA\_FLUSH

Request a Wi-Fi PMKSA cache entries flush.

**Definition** wifi\_mgmt.h:284

[NET\_REQUEST\_WIFI\_DISCONNECT](group__wifi__mgmt.md#ga90afd8d4e83056463ec6e667ed8ea60a)

#define NET\_REQUEST\_WIFI\_DISCONNECT

Request a Wi-Fi disconnect.

**Definition** wifi\_mgmt.h:154

[wifi\_twt\_fail\_reason](group__wifi__mgmt.md#ga97fa304f9a1db2294a93cccd4c93bcf6)

wifi\_twt\_fail\_reason

Target Wake Time (TWT) error codes.

**Definition** wifi.h:527

[NET\_REQUEST\_WIFI\_AP\_RTS\_THRESHOLD](group__wifi__mgmt.md#ga9918582d4e7bb0952daf993ee34e166d)

#define NET\_REQUEST\_WIFI\_AP\_RTS\_THRESHOLD

Request a Wi-Fi RTS threshold.

**Definition** wifi\_mgmt.h:172

[net\_request\_wifi\_cmd](group__wifi__mgmt.md#ga99a55137188119f65f9d2bb4f57cac77)

net\_request\_wifi\_cmd

Wi-Fi management commands.

**Definition** wifi\_mgmt.h:67

[NET\_REQUEST\_WIFI\_MODE](group__wifi__mgmt.md#ga9b4da60a8108b0cc431ac1eecfca0cd0)

#define NET\_REQUEST\_WIFI\_MODE

Request current Wi-Fi mode.

**Definition** wifi\_mgmt.h:223

[NET\_REQUEST\_WIFI\_AP\_STA\_DISCONNECT](group__wifi__mgmt.md#gaa3e52e08d89a1104f07207e52b81d503)

#define NET\_REQUEST\_WIFI\_AP\_STA\_DISCONNECT

Request a Wi-Fi access point to disconnect a station.

**Definition** wifi\_mgmt.h:241

[wifi\_mgmt\_raise\_disconnect\_complete\_event](group__wifi__mgmt.md#gaa75246d6dc55dada389c9d31e2607d5c)

void wifi\_mgmt\_raise\_disconnect\_complete\_event(struct net\_if \*iface, int status)

Wi-Fi management disconnect complete event.

[NET\_REQUEST\_WIFI\_CONNECT](group__wifi__mgmt.md#gaa7ab2a97950a22736bb69f60b459f0f6)

#define NET\_REQUEST\_WIFI\_CONNECT

Request a Wi-Fi connect.

**Definition** wifi\_mgmt.h:148

[wifi\_ap\_status](group__wifi__mgmt.md#gaaf730bf76adc06434c7ac63bf0417884)

wifi\_ap\_status

Wi-Fi AP mode result codes.

**Definition** wifi\_mgmt.h:636

[NET\_REQUEST\_WIFI\_TWT](group__wifi__mgmt.md#gab84fd7e9ca0bf0b2b9d08889dda26aad)

#define NET\_REQUEST\_WIFI\_TWT

Request a Wi-Fi TWT.

**Definition** wifi\_mgmt.h:200

[wifi\_link\_mode](group__wifi__mgmt.md#gabdb2a784d4727b71ab44cca04e422c62)

wifi\_link\_mode

Wi-Fi link operating modes.

**Definition** wifi.h:375

[wifi\_ps\_param\_type](group__wifi__mgmt.md#gabe45d132797047c098041331c8f6f912)

wifi\_ps\_param\_type

Wi-Fi power save parameters.

**Definition** wifi.h:594

[net\_event\_wifi\_cmd](group__wifi__mgmt.md#gac2638308cbb0d268831f1618cf8e1fa8)

net\_event\_wifi\_cmd

Wi-Fi management events.

**Definition** wifi\_mgmt.h:321

[NET\_REQUEST\_WIFI\_CONN\_PARAMS](group__wifi__mgmt.md#gac6483341435ff380a2d4a69430899c1a)

#define NET\_REQUEST\_WIFI\_CONN\_PARAMS

Request a Wi-Fi connection parameters.

**Definition** wifi\_mgmt.h:253

[wifi\_disconn\_reason](group__wifi__mgmt.md#gac782af0a60b202fd19597cabb7bd3a9a)

wifi\_disconn\_reason

Wi-Fi disconnect reason codes.

**Definition** wifi\_mgmt.h:620

[wifi\_ps\_wakeup\_mode](group__wifi__mgmt.md#gac7f907644847e905d67c709fa4afae7f)

wifi\_ps\_wakeup\_mode

Wi-Fi power save modes.

**Definition** wifi.h:610

[wifi\_mgmt\_raise\_ap\_sta\_connected\_event](group__wifi__mgmt.md#gac8f17f0aa3e426a5cdb731727b9b9ce3)

void wifi\_mgmt\_raise\_ap\_sta\_connected\_event(struct net\_if \*iface, struct wifi\_ap\_sta\_info \*sta\_info)

Wi-Fi management AP mode STA connected event.

[wifi\_twt\_operation](group__wifi__mgmt.md#gad0e998aeb1b27c4f203ca76339d323a3)

wifi\_twt\_operation

Wi-Fi Target Wake Time (TWT) operations.

**Definition** wifi.h:472

[wifi\_scan\_type](group__wifi__mgmt.md#gad30e29eda65ccafdbd7f11865937b8ea)

wifi\_scan\_type

Wi-Fi scanning types.

**Definition** wifi.h:406

[scan\_result\_cb\_t](group__wifi__mgmt.md#gad34b366f1c315207ce0da587ca96d8d8)

void(\* scan\_result\_cb\_t)(struct net\_if \*iface, int status, struct wifi\_scan\_result \*entry)

Scan result callback.

**Definition** wifi\_mgmt.h:1291

[wifi\_twt\_teardown\_status](group__wifi__mgmt.md#gad3709d07aaa3ed59b48f9dd7bd181989)

wifi\_twt\_teardown\_status

Wi-Fi Target Wake Time (TWT) teradown status.

**Definition** wifi.h:553

[WIFI\_SSID\_MAX\_LEN](group__wifi__mgmt.md#gad62c60666c9fdffe2e0e9c4388f87886)

#define WIFI\_SSID\_MAX\_LEN

Max SSID length.

**Definition** wifi.h:274

[NET\_REQUEST\_WIFI\_CHANNEL](group__wifi__mgmt.md#gad9614d2368f8399850aaec05e40bdc78)

#define NET\_REQUEST\_WIFI\_CHANNEL

Request a Wi-Fi channel.

**Definition** wifi\_mgmt.h:235

[wifi\_config\_ps\_param\_fail\_reason](group__wifi__mgmt.md#gad98099584d2222ede93aba42b1fbaff0)

wifi\_config\_ps\_param\_fail\_reason

Wi-Fi power save error codes.

**Definition** wifi.h:639

[NET\_REQUEST\_WIFI\_11K\_CONFIG](group__wifi__mgmt.md#gadd9b5b206c7ee2e40c30a37c7b4fc002)

#define NET\_REQUEST\_WIFI\_11K\_CONFIG

**Definition** wifi\_mgmt.h:183

[wifi\_security\_type](group__wifi__mgmt.md#gadde31a04fa25ed805115c6b31854cd9c)

wifi\_security\_type

IEEE 802.11 security types.

**Definition** wifi.h:42

[wifi\_mgmt\_raise\_ap\_disable\_result\_event](group__wifi__mgmt.md#gadee15c6a492a8ee13bea43812debb5d9)

void wifi\_mgmt\_raise\_ap\_disable\_result\_event(struct net\_if \*iface, enum wifi\_ap\_status status)

Wi-Fi management AP mode disable result event.

[wifi\_mgmt\_op](group__wifi__mgmt.md#gae129d0783276e662575af2314eef86cd)

wifi\_mgmt\_op

Generic get/set operation for any command.

**Definition** wifi\_mgmt.h:890

[NET\_REQUEST\_WIFI\_ENTERPRISE\_CREDS](group__wifi__mgmt.md#gae5dc7835e11487187663dfe65a15f22b)

#define NET\_REQUEST\_WIFI\_ENTERPRISE\_CREDS

Set Wi-Fi enterprise mode CA/client Cert and key.

**Definition** wifi\_mgmt.h:290

[NET\_REQUEST\_WIFI\_BTWT](group__wifi__mgmt.md#gaf1a806a89b0fd20de950c6e085351134)

#define NET\_REQUEST\_WIFI\_BTWT

**Definition** wifi\_mgmt.h:205

[NET\_REQUEST\_WIFI\_AP\_CONFIG\_PARAM](group__wifi__mgmt.md#gaf4a78d230f5e0743a6aaf152ddda1c67)

#define NET\_REQUEST\_WIFI\_AP\_CONFIG\_PARAM

Request a Wi-Fi AP parameters configuration.

**Definition** wifi\_mgmt.h:265

[NET\_REQUEST\_WIFI\_AP\_DISABLE](group__wifi__mgmt.md#gaf81f62bf4c9e331a095acbf0d24ca1a2)

#define NET\_REQUEST\_WIFI\_AP\_DISABLE

Request a Wi-Fi access point disable.

**Definition** wifi\_mgmt.h:166

[wifi\_ps\_mode](group__wifi__mgmt.md#gaffae7d2a754be5eb952ad2b83edad54c)

wifi\_ps\_mode

Wi-Fi power save modes.

**Definition** wifi.h:425

[WIFI\_EXT\_CAPAB\_GLK](group__wifi__mgmt.md#gga03ab29789adfe867c4ebaddc39482344a1363c1318e4281e057d848194396feb7)

@ WIFI\_EXT\_CAPAB\_GLK

**Definition** wifi\_mgmt.h:1277

[WIFI\_EXT\_CAPAB\_20\_40\_COEX](group__wifi__mgmt.md#gga03ab29789adfe867c4ebaddc39482344abf275508c3f69321cdf704779e976d68)

@ WIFI\_EXT\_CAPAB\_20\_40\_COEX

**Definition** wifi\_mgmt.h:1276

[WIFI\_EXT\_CAPAB\_BSS\_TRANSITION](group__wifi__mgmt.md#gga03ab29789adfe867c4ebaddc39482344ac5c648efedadc82fae7d9e0851ff71ba)

@ WIFI\_EXT\_CAPAB\_BSS\_TRANSITION

**Definition** wifi\_mgmt.h:1280

[WIFI\_EXT\_CAPAB\_EXT\_CHAN\_SWITCH](group__wifi__mgmt.md#gga03ab29789adfe867c4ebaddc39482344acf854adfca2bb41dd5d75df2b16c3e5e)

@ WIFI\_EXT\_CAPAB\_EXT\_CHAN\_SWITCH

**Definition** wifi\_mgmt.h:1278

[WIFI\_EXT\_CAPAB\_TIM\_BROADCAST](group__wifi__mgmt.md#gga03ab29789adfe867c4ebaddc39482344af42762fd723afef7fae98cbefbfff056)

@ WIFI\_EXT\_CAPAB\_TIM\_BROADCAST

**Definition** wifi\_mgmt.h:1279

[WIFI\_SAP\_IFACE\_COUNTRY\_UPDATE](group__wifi__mgmt.md#gga0cc87c00cbee0d0aca833119dbf0d74ea403d84f907f84492eed8e33713e828ae)

@ WIFI\_SAP\_IFACE\_COUNTRY\_UPDATE

**Definition** wifi\_mgmt.h:1266

[WIFI\_SAP\_IFACE\_DISABLED](group__wifi__mgmt.md#gga0cc87c00cbee0d0aca833119dbf0d74ea59a8530057e9839d89243558cc366d69)

@ WIFI\_SAP\_IFACE\_DISABLED

**Definition** wifi\_mgmt.h:1265

[WIFI\_SAP\_IFACE\_HT\_SCAN](group__wifi__mgmt.md#gga0cc87c00cbee0d0aca833119dbf0d74eaa3a6e6e367c7384379f3c562d1fc358f)

@ WIFI\_SAP\_IFACE\_HT\_SCAN

**Definition** wifi\_mgmt.h:1268

[WIFI\_SAP\_IFACE\_ENABLED](group__wifi__mgmt.md#gga0cc87c00cbee0d0aca833119dbf0d74eaa9133b73b886f2ec543acd282b33eeda)

@ WIFI\_SAP\_IFACE\_ENABLED

**Definition** wifi\_mgmt.h:1271

[WIFI\_SAP\_IFACE\_ACS](group__wifi__mgmt.md#gga0cc87c00cbee0d0aca833119dbf0d74eab3fea1a0ef90043699cb7d8ab064be7e)

@ WIFI\_SAP\_IFACE\_ACS

**Definition** wifi\_mgmt.h:1267

[WIFI\_SAP\_IFACE\_UNINITIALIZED](group__wifi__mgmt.md#gga0cc87c00cbee0d0aca833119dbf0d74ead92795c629fe828e7efde485eb2761c0)

@ WIFI\_SAP\_IFACE\_UNINITIALIZED

**Definition** wifi\_mgmt.h:1264

[WIFI\_SAP\_IFACE\_NO\_IR](group__wifi__mgmt.md#gga0cc87c00cbee0d0aca833119dbf0d74eaea74f039e6a5abe976e9956b5a01ff1a)

@ WIFI\_SAP\_IFACE\_NO\_IR

**Definition** wifi\_mgmt.h:1270

[WIFI\_SAP\_IFACE\_DFS](group__wifi__mgmt.md#gga0cc87c00cbee0d0aca833119dbf0d74eafdf99a461cf5878240cc40ae4ea7e113)

@ WIFI\_SAP\_IFACE\_DFS

**Definition** wifi\_mgmt.h:1269

[WIFI\_TWT\_STATE\_SLEEP](group__wifi__mgmt.md#gga38c184ea35c02f304cccdf389ca6d552a37a7aba20723b6614e39e1c417f3113c)

@ WIFI\_TWT\_STATE\_SLEEP

TWT sleep state: sleeping.

**Definition** wifi\_mgmt.h:943

[WIFI\_TWT\_STATE\_AWAKE](group__wifi__mgmt.md#gga38c184ea35c02f304cccdf389ca6d552a7b7b45f85d9644f897ca00bd7864e1b0)

@ WIFI\_TWT\_STATE\_AWAKE

TWT sleep state: awake.

**Definition** wifi\_mgmt.h:945

[WIFI\_WPS\_PBC](group__wifi__mgmt.md#gga4c36ae1a5171d3fbaeebf95c16be496da093f5b3ef95d9e571ea169430da57e88)

@ WIFI\_WPS\_PBC

WPS pbc.

**Definition** wifi\_mgmt.h:1246

[WIFI\_WPS\_PIN\_SET](group__wifi__mgmt.md#gga4c36ae1a5171d3fbaeebf95c16be496da58120620fd2fca80bdac7990ed0e7552)

@ WIFI\_WPS\_PIN\_SET

Set WPS pin number.

**Definition** wifi\_mgmt.h:1250

[WIFI\_WPS\_PIN\_GET](group__wifi__mgmt.md#gga4c36ae1a5171d3fbaeebf95c16be496da75bd5067903c2bba8a06732f0431393d)

@ WIFI\_WPS\_PIN\_GET

Get WPS pin number.

**Definition** wifi\_mgmt.h:1248

[WIFI\_STATUS\_CONN\_AP\_NOT\_FOUND](group__wifi__mgmt.md#gga86a5741e54aeb3e290142b0de217b8a8a2ae79fa389bb447fa108e0107aeff2f4)

@ WIFI\_STATUS\_CONN\_AP\_NOT\_FOUND

Connection failed - AP not found.

**Definition** wifi\_mgmt.h:610

[WIFI\_STATUS\_CONN\_SUCCESS](group__wifi__mgmt.md#gga86a5741e54aeb3e290142b0de217b8a8a380410b02b1e12599f37d1dcb844f5bd)

@ WIFI\_STATUS\_CONN\_SUCCESS

Connection successful.

**Definition** wifi\_mgmt.h:595

[WIFI\_STATUS\_CONN\_WRONG\_PASSWORD](group__wifi__mgmt.md#gga86a5741e54aeb3e290142b0de217b8a8a90d91f96a35c9f6847cbc7abd8c20bf8)

@ WIFI\_STATUS\_CONN\_WRONG\_PASSWORD

Connection failed - wrong password Few possible reasons for 4-way handshake failure that we can guess...

**Definition** wifi\_mgmt.h:606

[WIFI\_STATUS\_CONN\_FAIL](group__wifi__mgmt.md#gga86a5741e54aeb3e290142b0de217b8a8ab80ec4b70c75695fbe698034e2cb6a44)

@ WIFI\_STATUS\_CONN\_FAIL

Connection failed - generic failure.

**Definition** wifi\_mgmt.h:597

[WIFI\_STATUS\_CONN\_TIMEOUT](group__wifi__mgmt.md#gga86a5741e54aeb3e290142b0de217b8a8abb8783b92aec2ed1ffc6331979888563)

@ WIFI\_STATUS\_CONN\_TIMEOUT

Connection timed out.

**Definition** wifi\_mgmt.h:608

[WIFI\_STATUS\_DISCONN\_FIRST\_STATUS](group__wifi__mgmt.md#gga86a5741e54aeb3e290142b0de217b8a8abe1401e5d516c0d63291add15e558b18)

@ WIFI\_STATUS\_DISCONN\_FIRST\_STATUS

Connection disconnected status.

**Definition** wifi\_mgmt.h:614

[WIFI\_STATUS\_CONN\_LAST\_STATUS](group__wifi__mgmt.md#gga86a5741e54aeb3e290142b0de217b8a8aeee5fb8d8c3e7905554d08331f06191f)

@ WIFI\_STATUS\_CONN\_LAST\_STATUS

Last connection status.

**Definition** wifi\_mgmt.h:612

[NET\_REQUEST\_WIFI\_CMD\_AP\_CONFIG\_PARAM](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a14a0428720818c79df825d758e83f813)

@ NET\_REQUEST\_WIFI\_CMD\_AP\_CONFIG\_PARAM

Configure AP parameter.

**Definition** wifi\_mgmt.h:111

[NET\_REQUEST\_WIFI\_CMD\_TWT](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a1c9dc2d698326d987ffe5bfd35a9ed09)

@ NET\_REQUEST\_WIFI\_CMD\_TWT

Setup or teardown TWT flow.

**Definition** wifi\_mgmt.h:89

[NET\_REQUEST\_WIFI\_CMD\_PMKSA\_FLUSH](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a1fec11ed98f0a9411eefda9e55ee9aad)

@ NET\_REQUEST\_WIFI\_CMD\_PMKSA\_FLUSH

Flush PMKSA cache entries.

**Definition** wifi\_mgmt.h:117

[NET\_REQUEST\_WIFI\_CMD\_PACKET\_FILTER](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a2579ace546bf6954c111eb5951e894f5)

@ NET\_REQUEST\_WIFI\_CMD\_PACKET\_FILTER

Set or get packet filter setting for current mode.

**Definition** wifi\_mgmt.h:99

[NET\_REQUEST\_WIFI\_CMD\_AP\_ENABLE](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a28267d33b555433271cb121d62194a4c)

@ NET\_REQUEST\_WIFI\_CMD\_AP\_ENABLE

Enable AP mode.

**Definition** wifi\_mgmt.h:75

[NET\_REQUEST\_WIFI\_CMD\_START\_ROAMING](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a286205d961a77e44cd98e7894c48e676)

@ NET\_REQUEST\_WIFI\_CMD\_START\_ROAMING

Start roaming.

**Definition** wifi\_mgmt.h:129

[NET\_REQUEST\_WIFI\_CMD\_REG\_DOMAIN](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a367cc44caefd313e0c7ad3badc081456)

@ NET\_REQUEST\_WIFI\_CMD\_REG\_DOMAIN

Set or get regulatory domain.

**Definition** wifi\_mgmt.h:95

[NET\_REQUEST\_WIFI\_CMD\_AP\_RTS\_THRESHOLD](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a40104910a4d0258f63a03851de929474)

@ NET\_REQUEST\_WIFI\_CMD\_AP\_RTS\_THRESHOLD

Set AP RTS threshold.

**Definition** wifi\_mgmt.h:79

[NET\_REQUEST\_WIFI\_CMD\_11K\_NEIGHBOR\_REQUEST](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a48b3f0ec6647fb30d3b6456822c2dede)

@ NET\_REQUEST\_WIFI\_CMD\_11K\_NEIGHBOR\_REQUEST

Send 11k neighbor request.

**Definition** wifi\_mgmt.h:85

[NET\_REQUEST\_WIFI\_CMD\_SCAN](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a4aadf9114010c09bd7420c99a2049d5a)

@ NET\_REQUEST\_WIFI\_CMD\_SCAN

Scan for Wi-Fi networks.

**Definition** wifi\_mgmt.h:69

[NET\_REQUEST\_WIFI\_CMD\_IFACE\_STATUS](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a6af9d52df8f9db6393044e42e10ff0de)

@ NET\_REQUEST\_WIFI\_CMD\_IFACE\_STATUS

Get interface status.

**Definition** wifi\_mgmt.h:81

[NET\_REQUEST\_WIFI\_CMD\_AP\_STA\_DISCONNECT](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a6f3865aa6a4d7633e241ee2b002c1b5a)

@ NET\_REQUEST\_WIFI\_CMD\_AP\_STA\_DISCONNECT

Disconnect a STA from AP.

**Definition** wifi\_mgmt.h:103

[NET\_REQUEST\_WIFI\_CMD\_DPP](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a6fc4d3aca344dc551dd62ae1d6072104)

@ NET\_REQUEST\_WIFI\_CMD\_DPP

DPP actions.

**Definition** wifi\_mgmt.h:113

[NET\_REQUEST\_WIFI\_CMD\_AP\_DISABLE](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a6fe9d7137b4cd20de880955b27382ccf)

@ NET\_REQUEST\_WIFI\_CMD\_AP\_DISABLE

Disable AP mode.

**Definition** wifi\_mgmt.h:77

[NET\_REQUEST\_WIFI\_CMD\_RTS\_THRESHOLD](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a7852cff28fc18ddd7af0f8224c840e7b)

@ NET\_REQUEST\_WIFI\_CMD\_RTS\_THRESHOLD

Set RTS threshold.

**Definition** wifi\_mgmt.h:109

[NET\_REQUEST\_WIFI\_CMD\_CONNECT](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a78c958877ee60c90803c925b6b2f057a)

@ NET\_REQUEST\_WIFI\_CMD\_CONNECT

Connect to a Wi-Fi network.

**Definition** wifi\_mgmt.h:71

[NET\_REQUEST\_WIFI\_CMD\_VERSION](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a7d9596f2cce54c9e050d89469e86eccb)

@ NET\_REQUEST\_WIFI\_CMD\_VERSION

Get Wi-Fi driver and Firmware versions.

**Definition** wifi\_mgmt.h:105

[NET\_REQUEST\_WIFI\_CMD\_ENTERPRISE\_CREDS](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a94b7fb7a8c529082e1d0458298b6c3fb)

@ NET\_REQUEST\_WIFI\_CMD\_ENTERPRISE\_CREDS

Set enterprise mode credential.

**Definition** wifi\_mgmt.h:119

[NET\_REQUEST\_WIFI\_CMD\_CONN\_PARAMS](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77aa150f53621941796082e00090bde6a5a)

@ NET\_REQUEST\_WIFI\_CMD\_CONN\_PARAMS

Get Wi-Fi latest connection parameters.

**Definition** wifi\_mgmt.h:107

[NET\_REQUEST\_WIFI\_CMD\_11K\_CONFIG](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77aa86fb7193245593dd84b3a4376bc25d6)

@ NET\_REQUEST\_WIFI\_CMD\_11K\_CONFIG

Set or get 11k status.

**Definition** wifi\_mgmt.h:83

[NET\_REQUEST\_WIFI\_CMD\_CHANNEL](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77aade3d7a43c730a52f7876c6486170bb2)

@ NET\_REQUEST\_WIFI\_CMD\_CHANNEL

Set or get Wi-Fi channel for Monitor or TX-Injection mode.

**Definition** wifi\_mgmt.h:101

[NET\_REQUEST\_WIFI\_CMD\_BTWT](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77aaf770b48056af1f9d6d99deb3772027d)

@ NET\_REQUEST\_WIFI\_CMD\_BTWT

Setup BTWT flow.

**Definition** wifi\_mgmt.h:91

[NET\_REQUEST\_WIFI\_CMD\_MODE](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77ab7183584bdf5fe673d39fa0d090e3899)

@ NET\_REQUEST\_WIFI\_CMD\_MODE

Set or get Mode of operation.

**Definition** wifi\_mgmt.h:97

[NET\_REQUEST\_WIFI\_CMD\_RTS\_THRESHOLD\_CONFIG](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77ab7a4215540d2e6cda0d522dc621e9d89)

@ NET\_REQUEST\_WIFI\_CMD\_RTS\_THRESHOLD\_CONFIG

Get RTS threshold.

**Definition** wifi\_mgmt.h:121

[NET\_REQUEST\_WIFI\_CMD\_CANDIDATE\_SCAN](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77ab7bc479691f88138972d0d8e1e2179ed)

@ NET\_REQUEST\_WIFI\_CMD\_CANDIDATE\_SCAN

Specific scan.

**Definition** wifi\_mgmt.h:133

[NET\_REQUEST\_WIFI\_CMD\_BTM\_QUERY](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77ab95b651107d819809cb5909dc25a5a56)

@ NET\_REQUEST\_WIFI\_CMD\_BTM\_QUERY

BSS transition management query.

**Definition** wifi\_mgmt.h:115

[NET\_REQUEST\_WIFI\_CMD\_PS](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77abf9fb93c205fa36f74a9ef19d3d0351a)

@ NET\_REQUEST\_WIFI\_CMD\_PS

Set power save status.

**Definition** wifi\_mgmt.h:87

[NET\_REQUEST\_WIFI\_CMD\_DISCONNECT](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77ac33941da138b993f7a1158d91469bcb7)

@ NET\_REQUEST\_WIFI\_CMD\_DISCONNECT

Disconnect from a Wi-Fi network.

**Definition** wifi\_mgmt.h:73

[NET\_REQUEST\_WIFI\_CMD\_NEIGHBOR\_REP\_COMPLETE](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77ad950aa5b87408793f4df9c39fe84cc55)

@ NET\_REQUEST\_WIFI\_CMD\_NEIGHBOR\_REP\_COMPLETE

Neighbor report complete.

**Definition** wifi\_mgmt.h:131

[NET\_REQUEST\_WIFI\_CMD\_AP\_WPS\_CONFIG](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77ae496f72d75179a2d10e9fb326259e413)

@ NET\_REQUEST\_WIFI\_CMD\_AP\_WPS\_CONFIG

AP WPS config.

**Definition** wifi\_mgmt.h:135

[NET\_REQUEST\_WIFI\_CMD\_PS\_CONFIG](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77ae6ce1c605d1bf7c09650ec15d74e77e9)

@ NET\_REQUEST\_WIFI\_CMD\_PS\_CONFIG

Get power save config.

**Definition** wifi\_mgmt.h:93

[NET\_REQUEST\_WIFI\_CMD\_WPS\_CONFIG](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77aec78bf6196abee310e06a8454d27eed7)

@ NET\_REQUEST\_WIFI\_CMD\_WPS\_CONFIG

WPS config.

**Definition** wifi\_mgmt.h:123

[WIFI\_STATUS\_AP\_CHANNEL\_NOT\_ALLOWED](group__wifi__mgmt.md#ggaaf730bf76adc06434c7ac63bf0417884a0b1cb592c54c16e8a54defee71c5fd15)

@ WIFI\_STATUS\_AP\_CHANNEL\_NOT\_ALLOWED

AP mode enable failed - channel not allowed.

**Definition** wifi\_mgmt.h:644

[WIFI\_STATUS\_AP\_SUCCESS](group__wifi__mgmt.md#ggaaf730bf76adc06434c7ac63bf0417884a0df52848da8735892d0eb1e381b2cd7c)

@ WIFI\_STATUS\_AP\_SUCCESS

AP mode enable or disable successful.

**Definition** wifi\_mgmt.h:638

[WIFI\_STATUS\_AP\_OP\_NOT\_SUPPORTED](group__wifi__mgmt.md#ggaaf730bf76adc06434c7ac63bf0417884a2105e6c49b3bcb5f7dcacbc1e5ce9cca)

@ WIFI\_STATUS\_AP\_OP\_NOT\_SUPPORTED

AP mode enable failed - operation not supported.

**Definition** wifi\_mgmt.h:650

[WIFI\_STATUS\_AP\_OP\_NOT\_PERMITTED](group__wifi__mgmt.md#ggaaf730bf76adc06434c7ac63bf0417884a36a58980bdc7877c910441590137ddbe)

@ WIFI\_STATUS\_AP\_OP\_NOT\_PERMITTED

AP mode enable failed - operation not permitted.

**Definition** wifi\_mgmt.h:652

[WIFI\_STATUS\_AP\_CHANNEL\_NOT\_SUPPORTED](group__wifi__mgmt.md#ggaaf730bf76adc06434c7ac63bf0417884a5acb85a2361ca72ed10966b829c5753b)

@ WIFI\_STATUS\_AP\_CHANNEL\_NOT\_SUPPORTED

AP mode enable failed - channel not supported.

**Definition** wifi\_mgmt.h:642

[WIFI\_STATUS\_AP\_FAIL](group__wifi__mgmt.md#ggaaf730bf76adc06434c7ac63bf0417884a6c6801381caa3862004662169202fa9a)

@ WIFI\_STATUS\_AP\_FAIL

AP mode enable or disable failed - generic failure.

**Definition** wifi\_mgmt.h:640

[WIFI\_STATUS\_AP\_AUTH\_TYPE\_NOT\_SUPPORTED](group__wifi__mgmt.md#ggaaf730bf76adc06434c7ac63bf0417884abe5a626d22051522255d98fdfdfbfcc8)

@ WIFI\_STATUS\_AP\_AUTH\_TYPE\_NOT\_SUPPORTED

AP mode enable failed - authentication type not supported.

**Definition** wifi\_mgmt.h:648

[WIFI\_STATUS\_AP\_SSID\_NOT\_ALLOWED](group__wifi__mgmt.md#ggaaf730bf76adc06434c7ac63bf0417884ac18a7b551f8c6bb7737b0e8e60c323ce)

@ WIFI\_STATUS\_AP\_SSID\_NOT\_ALLOWED

AP mode enable failed - SSID not allowed.

**Definition** wifi\_mgmt.h:646

[NET\_EVENT\_WIFI\_CMD\_AP\_STA\_DISCONNECTED](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8a3678a39f9542968958b5575d571d4e2e)

@ NET\_EVENT\_WIFI\_CMD\_AP\_STA\_DISCONNECTED

STA disconnected from AP.

**Definition** wifi\_mgmt.h:355

[NET\_EVENT\_WIFI\_CMD\_SCAN\_RESULT](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8a37e9ab2a6832153fa968337d920e587e)

@ NET\_EVENT\_WIFI\_CMD\_SCAN\_RESULT

Scan results available.

**Definition** wifi\_mgmt.h:323

[NET\_EVENT\_WIFI\_CMD\_DISCONNECT\_RESULT](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8a3a3b0387f83d8fb24a0e27312468b0eb)

@ NET\_EVENT\_WIFI\_CMD\_DISCONNECT\_RESULT

Disconnect result.

**Definition** wifi\_mgmt.h:329

[NET\_EVENT\_WIFI\_CMD\_SUPPLICANT](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8a4ec52c22e23502421077e46e94facf08)

@ NET\_EVENT\_WIFI\_CMD\_SUPPLICANT

Supplicant specific event.

**Definition** wifi\_mgmt.h:357

[NET\_EVENT\_WIFI\_CMD\_NEIGHBOR\_REP\_RECEIVED](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8a75a0a093f32fa2577286c92c2525df91)

@ NET\_EVENT\_WIFI\_CMD\_NEIGHBOR\_REP\_RECEIVED

Neighbor Report.

**Definition** wifi\_mgmt.h:345

[NET\_EVENT\_WIFI\_CMD\_TWT\_SLEEP\_STATE](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8a78838bf7ce80cee5e803712cd0286750)

@ NET\_EVENT\_WIFI\_CMD\_TWT\_SLEEP\_STATE

TWT sleep status: awake or sleeping, can be used by application to determine if it can send data or n...

**Definition** wifi\_mgmt.h:337

[NET\_EVENT\_WIFI\_CMD\_NEIGHBOR\_REP\_COMPLETE](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8a86b6811a06f6158ae9ea4687e219e5af)

@ NET\_EVENT\_WIFI\_CMD\_NEIGHBOR\_REP\_COMPLETE

Neighbor Report complete.

**Definition** wifi\_mgmt.h:347

[NET\_EVENT\_WIFI\_CMD\_AP\_ENABLE\_RESULT](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8abd1797564427886eeb14dd293ae86a9b)

@ NET\_EVENT\_WIFI\_CMD\_AP\_ENABLE\_RESULT

AP mode enable result.

**Definition** wifi\_mgmt.h:349

[NET\_EVENT\_WIFI\_CMD\_AP\_STA\_CONNECTED](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8abd4269b2cd1302ce61da4f8d7bb9d5fb)

@ NET\_EVENT\_WIFI\_CMD\_AP\_STA\_CONNECTED

STA connected to AP.

**Definition** wifi\_mgmt.h:353

[NET\_EVENT\_WIFI\_CMD\_SIGNAL\_CHANGE](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8acc9d8a16d99e4006b915b3686522a8e0)

@ NET\_EVENT\_WIFI\_CMD\_SIGNAL\_CHANGE

Signal change event.

**Definition** wifi\_mgmt.h:343

[NET\_EVENT\_WIFI\_CMD\_SCAN\_DONE](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8ad753b7e4588257815f4a60a539ca2018)

@ NET\_EVENT\_WIFI\_CMD\_SCAN\_DONE

Scan done.

**Definition** wifi\_mgmt.h:325

[NET\_EVENT\_WIFI\_CMD\_TWT](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8adad71603ed829ed92d06f8c40efa9b18)

@ NET\_EVENT\_WIFI\_CMD\_TWT

TWT events.

**Definition** wifi\_mgmt.h:333

[NET\_EVENT\_WIFI\_CMD\_RAW\_SCAN\_RESULT](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8addf15c69512be7ab4957e7c0b3fde0ac)

@ NET\_EVENT\_WIFI\_CMD\_RAW\_SCAN\_RESULT

Raw scan results available.

**Definition** wifi\_mgmt.h:339

[NET\_EVENT\_WIFI\_CMD\_AP\_DISABLE\_RESULT](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8aeec3d7a9191280c2326034a17555308d)

@ NET\_EVENT\_WIFI\_CMD\_AP\_DISABLE\_RESULT

AP mode disable result.

**Definition** wifi\_mgmt.h:351

[NET\_EVENT\_WIFI\_CMD\_DISCONNECT\_COMPLETE](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8af1c42bd59f01260c64ede07da436c18f)

@ NET\_EVENT\_WIFI\_CMD\_DISCONNECT\_COMPLETE

Disconnect complete.

**Definition** wifi\_mgmt.h:341

[NET\_EVENT\_WIFI\_CMD\_IFACE\_STATUS](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8af4b3f1969b96f63253851c26c3882a14)

@ NET\_EVENT\_WIFI\_CMD\_IFACE\_STATUS

Interface status.

**Definition** wifi\_mgmt.h:331

[NET\_EVENT\_WIFI\_CMD\_CONNECT\_RESULT](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8af76f28777b91b365dc3f97028bc18e3c)

@ NET\_EVENT\_WIFI\_CMD\_CONNECT\_RESULT

Connect result.

**Definition** wifi\_mgmt.h:327

[WIFI\_REASON\_DISCONN\_INACTIVITY](group__wifi__mgmt.md#ggac782af0a60b202fd19597cabb7bd3a9aa05fe2f87de30de47ee48f7615c2206e6)

@ WIFI\_REASON\_DISCONN\_INACTIVITY

Disconnected due to inactivity.

**Definition** wifi\_mgmt.h:630

[WIFI\_REASON\_DISCONN\_AP\_LEAVING](group__wifi__mgmt.md#ggac782af0a60b202fd19597cabb7bd3a9aa34e3f78ce43db3daeaf32038e0baf204)

@ WIFI\_REASON\_DISCONN\_AP\_LEAVING

Disconnected due to AP leaving.

**Definition** wifi\_mgmt.h:628

[WIFI\_REASON\_DISCONN\_SUCCESS](group__wifi__mgmt.md#ggac782af0a60b202fd19597cabb7bd3a9aa5c894399db8949a789ca4f5750b6f042)

@ WIFI\_REASON\_DISCONN\_SUCCESS

Success, overload status as reason.

**Definition** wifi\_mgmt.h:622

[WIFI\_REASON\_DISCONN\_UNSPECIFIED](group__wifi__mgmt.md#ggac782af0a60b202fd19597cabb7bd3a9aa87f5d64a9fd3acf8d67c698199779e5c)

@ WIFI\_REASON\_DISCONN\_UNSPECIFIED

Unspecified reason.

**Definition** wifi\_mgmt.h:624

[WIFI\_REASON\_DISCONN\_USER\_REQUEST](group__wifi__mgmt.md#ggac782af0a60b202fd19597cabb7bd3a9aaee75adafb52bd6ecaa547a76c6ccd0a7)

@ WIFI\_REASON\_DISCONN\_USER\_REQUEST

Disconnected due to user request.

**Definition** wifi\_mgmt.h:626

[WIFI\_MGMT\_GET](group__wifi__mgmt.md#ggae129d0783276e662575af2314eef86cda6b8183a773e0cdfa85bc4b41ae70fdcd)

@ WIFI\_MGMT\_GET

Get operation.

**Definition** wifi\_mgmt.h:892

[WIFI\_MGMT\_SET](group__wifi__mgmt.md#ggae129d0783276e662575af2314eef86cdaa0d5931c8275a8d3288ab668b6dfb5a1)

@ WIFI\_MGMT\_SET

Set operation.

**Definition** wifi\_mgmt.h:894

[net\_if.h](net__if_8h.md)

Public API for network interface.

[net\_mgmt.h](net__mgmt_8h.md)

Network Management API public header.

[offloaded\_netdev.h](offloaded__netdev_8h.md)

Offloaded network device iface API.

[listen](posix_2sys_2socket_8h.md#a7005ffbeeff92be5394ff3244da79028)

int listen(int sock, int backlog)

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

**Definition** device.h:453

[ethernet\_api](structethernet__api.md)

Ethernet L2 API operations.

**Definition** ethernet.h:541

[net\_if](structnet__if.md)

Network Interface structure.

**Definition** net\_if.h:714

[net\_stats\_wifi](structnet__stats__wifi.md)

All Wi-Fi specific statistics.

**Definition** net\_stats.h:673

[net\_wifi\_mgmt\_offload](structnet__wifi__mgmt__offload.md)

Wi-Fi management offload API.

**Definition** wifi\_mgmt.h:1592

[net\_wifi\_mgmt\_offload::wifi\_iface](structnet__wifi__mgmt__offload.md#a1d34a954a2f16d29f51dc51dd6fbb845)

struct ethernet\_api wifi\_iface

Mandatory to get in first position.

**Definition** wifi\_mgmt.h:1601

[net\_wifi\_mgmt\_offload::wifi\_mgmt\_api](structnet__wifi__mgmt__offload.md#a98fcc053d9820d2d981ed659520c9b3b)

const struct wifi\_mgmt\_ops \*const wifi\_mgmt\_api

Wi-Fi management API.

**Definition** wifi\_mgmt.h:1607

[net\_wifi\_mgmt\_offload::wifi\_drv\_ops](structnet__wifi__mgmt__offload.md#a991e0bc6247578a3d1c9d2d3ab0b63d7)

const void \* wifi\_drv\_ops

Wi-Fi supplicant driver API.

**Definition** wifi\_mgmt.h:1611

[offloaded\_if\_api](structoffloaded__if__api.md)

Extended net\_if\_api for offloaded ifaces/network devices, allowing handling of admin up/down state ch...

**Definition** offloaded\_netdev.h:53

[wifi\_11k\_params](structwifi__11k__params.md)

Wi-Fi 11k parameters.

**Definition** wifi\_mgmt.h:898

[wifi\_11k\_params::ssid](structwifi__11k__params.md#a64ace23c71837417678ceb9cc8d5f216)

uint8\_t ssid[WIFI\_SSID\_MAX\_LEN+1]

SSID.

**Definition** wifi\_mgmt.h:904

[wifi\_11k\_params::enable\_11k](structwifi__11k__params.md#a739c3e94b025aae2fcf5680aecf3d646)

bool enable\_11k

11k enable/disable

**Definition** wifi\_mgmt.h:902

[wifi\_11k\_params::oper](structwifi__11k__params.md#ae6029ed4bada41f18df0329d0da7401e)

enum wifi\_mgmt\_op oper

11k command operation

**Definition** wifi\_mgmt.h:900

[wifi\_ap\_config\_params](structwifi__ap__config__params.md)

Wi-Fi AP configuration parameter.

**Definition** wifi\_mgmt.h:1028

[wifi\_ap\_config\_params::max\_inactivity](structwifi__ap__config__params.md#a289866d9209450e893281b4c198a546a)

uint32\_t max\_inactivity

Parameter used for setting maximum inactivity duration for stations.

**Definition** wifi\_mgmt.h:1032

[wifi\_ap\_config\_params::type](structwifi__ap__config__params.md#a4c391cf504a994ed0bc4971afdf76774)

enum wifi\_ap\_config\_param type

Parameter used to identify the different AP parameters.

**Definition** wifi\_mgmt.h:1030

[wifi\_ap\_config\_params::max\_num\_sta](structwifi__ap__config__params.md#a7fc0fad99f53ed8e1ac40b74ec98bf9a)

uint32\_t max\_num\_sta

Parameter used for setting maximum number of stations.

**Definition** wifi\_mgmt.h:1034

[wifi\_ap\_config\_params::bandwidth](structwifi__ap__config__params.md#aba4e43dff01fa026c8dbbfff670d3097)

enum wifi\_frequency\_bandwidths bandwidth

Parameter used for frequency band.

**Definition** wifi\_mgmt.h:1036

[wifi\_ap\_sta\_info](structwifi__ap__sta__info.md)

AP mode - connected STA details.

**Definition** wifi\_mgmt.h:963

[wifi\_ap\_sta\_info::link\_mode](structwifi__ap__sta__info.md#a7d8bd52340d4937a4b5b7d2c00662441)

enum wifi\_link\_mode link\_mode

Link mode, see enum wifi\_link\_mode.

**Definition** wifi\_mgmt.h:965

[wifi\_ap\_sta\_info::mac](structwifi__ap__sta__info.md#a7db904376ec73b774aa9d8236c15b3f6)

uint8\_t mac[WIFI\_MAC\_ADDR\_LEN]

MAC address.

**Definition** wifi\_mgmt.h:967

[wifi\_ap\_sta\_info::mac\_length](structwifi__ap__sta__info.md#a7f7c8b144bb3464af5213708591eefda)

uint8\_t mac\_length

MAC address length.

**Definition** wifi\_mgmt.h:969

[wifi\_ap\_sta\_info::twt\_capable](structwifi__ap__sta__info.md#a838c9a4288c9bc7e97afe2334c678f34)

bool twt\_capable

is TWT capable ?

**Definition** wifi\_mgmt.h:971

[wifi\_band\_channel](structwifi__band__channel.md)

Wi-Fi structure to uniquely identify a band-channel pair.

**Definition** wifi\_mgmt.h:431

[wifi\_band\_channel::band](structwifi__band__channel.md#a4a932599429f37231f76c3064ec5efb3)

uint8\_t band

Frequency band.

**Definition** wifi\_mgmt.h:433

[wifi\_band\_channel::channel](structwifi__band__channel.md#acd0dd7366de3650124dad7232a58ade0)

uint8\_t channel

Channel.

**Definition** wifi\_mgmt.h:435

[wifi\_channel\_info](structwifi__channel__info.md)

Wi-Fi channel setting for monitor and TX-injection modes.

**Definition** wifi\_mgmt.h:1013

[wifi\_channel\_info::if\_index](structwifi__channel__info.md#a43a7dd8c19d0c6540e3cc0b5d1d6165d)

uint8\_t if\_index

Interface index.

**Definition** wifi\_mgmt.h:1017

[wifi\_channel\_info::channel](structwifi__channel__info.md#a799cbc0a67764f6680322ba0f2ad3300)

uint16\_t channel

Channel value to set.

**Definition** wifi\_mgmt.h:1015

[wifi\_channel\_info::oper](structwifi__channel__info.md#aa8ef8a71b49ead3664fff9a4d61b1ce8)

enum wifi\_mgmt\_op oper

Get or set operation.

**Definition** wifi\_mgmt.h:1019

[wifi\_connect\_req\_params](structwifi__connect__req__params.md)

Wi-Fi connect request parameters.

**Definition** wifi\_mgmt.h:517

[wifi\_connect\_req\_params::key2\_passwd](structwifi__connect__req__params.md#a020fc58d7e5350cc803cd5d6fa575e6a)

const uint8\_t \* key2\_passwd

private key2 passwd

**Definition** wifi\_mgmt.h:551

[wifi\_connect\_req\_params::ft\_used](structwifi__connect__req__params.md#a047b11e703fb646d778785dfcb14257b)

bool ft\_used

Fast BSS Transition used.

**Definition** wifi\_mgmt.h:571

[wifi\_connect\_req\_params::bandwidth](structwifi__connect__req__params.md#a0d44c86d9b9528041bbe7534e0c7597a)

enum wifi\_frequency\_bandwidths bandwidth

Parameter used for frequency band.

**Definition** wifi\_mgmt.h:587

[wifi\_connect\_req\_params::security](structwifi__connect__req__params.md#a18dce6bb021086877a30e7a04f5b24b9)

enum wifi\_security\_type security

Security type.

**Definition** wifi\_mgmt.h:535

[wifi\_connect\_req\_params::passwords](structwifi__connect__req__params.md#a2163b50b6d466663404e1cb21ce6ae5d)

const uint8\_t \* passwords[WIFI\_ENT\_IDENTITY\_MAX\_USERS]

User Passwords.

**Definition** wifi\_mgmt.h:579

[wifi\_connect\_req\_params::identities](structwifi__connect__req__params.md#a265001d2309840d04bdca507896255d0)

const uint8\_t \* identities[WIFI\_ENT\_IDENTITY\_MAX\_USERS]

User Identities.

**Definition** wifi\_mgmt.h:577

[wifi\_connect\_req\_params::aid\_length](structwifi__connect__req__params.md#a2892253024b70e5cb8eb2166b17ebe22)

uint8\_t aid\_length

anon\_id length, max 64

**Definition** wifi\_mgmt.h:545

[wifi\_connect\_req\_params::sae\_password](structwifi__connect__req__params.md#a469fac5758b78fc425911837930b2060)

const uint8\_t \* sae\_password

SAE password (same as PSK but with no length restrictions), optional.

**Definition** wifi\_mgmt.h:527

[wifi\_connect\_req\_params::key\_passwd](structwifi__connect__req__params.md#a4946647659a347667ee49bb6990bba66)

const uint8\_t \* key\_passwd

Private key passwd for enterprise mode.

**Definition** wifi\_mgmt.h:547

[wifi\_connect\_req\_params::eap\_id\_length](structwifi__connect__req__params.md#a4da02ff112c09f55dc5bddcda27d16a3)

uint8\_t eap\_id\_length

eap identity length, max 64

**Definition** wifi\_mgmt.h:563

[wifi\_connect\_req\_params::channel](structwifi__connect__req__params.md#a52b6d0323c35d03ec239f40be35cae72)

uint8\_t channel

Channel.

**Definition** wifi\_mgmt.h:533

[wifi\_connect\_req\_params::ssid\_length](structwifi__connect__req__params.md#a547dddf6be5dd77eda74b1085a798400)

uint8\_t ssid\_length

SSID length.

**Definition** wifi\_mgmt.h:521

[wifi\_connect\_req\_params::timeout](structwifi__connect__req__params.md#a56183ba7f4d8eaf5fc5b495856adecfd)

int timeout

Connect timeout in seconds, SYS\_FOREVER\_MS for no timeout.

**Definition** wifi\_mgmt.h:541

[wifi\_connect\_req\_params::nusers](structwifi__connect__req__params.md#a71770c2f2da378db2efedaa87b141627)

int nusers

Number of EAP users.

**Definition** wifi\_mgmt.h:573

[wifi\_connect\_req\_params::mfp](structwifi__connect__req__params.md#a745b3416172672a7e5b12bcc5b55e88c)

enum wifi\_mfp\_options mfp

MFP options.

**Definition** wifi\_mgmt.h:537

[wifi\_connect\_req\_params::sae\_password\_length](structwifi__connect__req__params.md#a74f0819e7a546ffb8bfb0ec587eccf20)

uint8\_t sae\_password\_length

SAE password length.

**Definition** wifi\_mgmt.h:529

[wifi\_connect\_req\_params::anon\_id](structwifi__connect__req__params.md#a781456e079357e2e1096218af3bd218c)

const uint8\_t \* anon\_id

anonymous identity

**Definition** wifi\_mgmt.h:543

[wifi\_connect\_req\_params::eap\_ver](structwifi__connect__req__params.md#a8c8ecb1ef0fe3f2f4c04a7a8eeccbbdf)

int eap\_ver

eap version

**Definition** wifi\_mgmt.h:559

[wifi\_connect\_req\_params::key\_passwd\_length](structwifi__connect__req__params.md#a9f913fc0ccecafaba488e444d701fd68)

uint8\_t key\_passwd\_length

Private key passwd length, max 128.

**Definition** wifi\_mgmt.h:549

[wifi\_connect\_req\_params::band](structwifi__connect__req__params.md#aa2fea1881a8ffdf5d7093ae295867f3e)

uint8\_t band

Frequency band.

**Definition** wifi\_mgmt.h:531

[wifi\_connect\_req\_params::TLS\_cipher](structwifi__connect__req__params.md#aa4577535a27b8d54d9b8c7543d359ade)

uint8\_t TLS\_cipher

TLS cipher.

**Definition** wifi\_mgmt.h:557

[wifi\_connect\_req\_params::psk](structwifi__connect__req__params.md#aa7743f0ecbc27a9595720ce13ce57c1d)

const uint8\_t \* psk

Pre-shared key.

**Definition** wifi\_mgmt.h:523

[wifi\_connect\_req\_params::bssid](structwifi__connect__req__params.md#aa8081b9075ff9244cefd0ac1ef3f42cb)

uint8\_t bssid[WIFI\_MAC\_ADDR\_LEN]

BSSID.

**Definition** wifi\_mgmt.h:539

[wifi\_connect\_req\_params::verify\_peer\_cert](structwifi__connect__req__params.md#aa8f18ace96e471eb0bc8bff8d8146f6f)

bool verify\_peer\_cert

Whether verify peer with CA or not: false-not verify, true-verify.

**Definition** wifi\_mgmt.h:569

[wifi\_connect\_req\_params::passwds](structwifi__connect__req__params.md#aaf071a51c7281e4d42197f266c729c04)

uint8\_t passwds

Number of EAP passwds.

**Definition** wifi\_mgmt.h:575

[wifi\_connect\_req\_params::psk\_length](structwifi__connect__req__params.md#aaf7455a65590d19f047214b459a2dcb9)

uint8\_t psk\_length

Pre-shared key length.

**Definition** wifi\_mgmt.h:525

[wifi\_connect\_req\_params::eap\_identity](structwifi__connect__req__params.md#ab9c65599409387af65a3c2895c3116da)

const uint8\_t \* eap\_identity

Identity for EAP.

**Definition** wifi\_mgmt.h:561

[wifi\_connect\_req\_params::ssid](structwifi__connect__req__params.md#ac260c2cd17a3f36ea101edaf23d41083)

const uint8\_t \* ssid

SSID.

**Definition** wifi\_mgmt.h:519

[wifi\_connect\_req\_params::wpa3\_ent\_mode](structwifi__connect__req__params.md#ae0b94d870ecbee0b203caee6a6e3d8b2)

enum wifi\_wpa3\_enterprise\_type wpa3\_ent\_mode

wpa3 enterprise mode

**Definition** wifi\_mgmt.h:555

[wifi\_connect\_req\_params::eap\_passwd\_length](structwifi__connect__req__params.md#aeab22e95a04a1831b87beda1772d3db7)

uint8\_t eap\_passwd\_length

eap passwd length, max 128

**Definition** wifi\_mgmt.h:567

[wifi\_connect\_req\_params::key2\_passwd\_length](structwifi__connect__req__params.md#af7b163cc2bffc59f7fa31f47c5e52062)

uint8\_t key2\_passwd\_length

key2 passwd length, max 128

**Definition** wifi\_mgmt.h:553

[wifi\_connect\_req\_params::ignore\_broadcast\_ssid](structwifi__connect__req__params.md#afac70366e509301f9a27ca51be30b88d)

uint8\_t ignore\_broadcast\_ssid

Hidden SSID configure 0: disabled (default) 1: send empty (length=0) SSID in beacon and ignore probe ...

**Definition** wifi\_mgmt.h:585

[wifi\_connect\_req\_params::eap\_password](structwifi__connect__req__params.md#afd046e702739c4a0d89322ee41b37acd)

const uint8\_t \* eap\_password

Password string for EAP.

**Definition** wifi\_mgmt.h:565

[wifi\_enterprise\_creds\_params](structwifi__enterprise__creds__params.md)

Wi-Fi enterprise mode credentials.

**Definition** wifi\_mgmt.h:840

[wifi\_enterprise\_creds\_params::client\_key\_len](structwifi__enterprise__creds__params.md#a09f5b34c81fe871e7513358499518d95)

uint32\_t client\_key\_len

Client key length.

**Definition** wifi\_mgmt.h:852

[wifi\_enterprise\_creds\_params::client\_cert2](structwifi__enterprise__creds__params.md#a133126e338d89563733268a03e2fa613)

uint8\_t \* client\_cert2

Client certification of phase2.

**Definition** wifi\_mgmt.h:858

[wifi\_enterprise\_creds\_params::client\_key2\_len](structwifi__enterprise__creds__params.md#a3da90b8a8dfa848f617579760ad4f971)

uint32\_t client\_key2\_len

Phase2 Client key length.

**Definition** wifi\_mgmt.h:864

[wifi\_enterprise\_creds\_params::client\_cert\_len](structwifi__enterprise__creds__params.md#a5f122d59b25b00af2db7eeac93d5482e)

uint32\_t client\_cert\_len

Client certification length.

**Definition** wifi\_mgmt.h:848

[wifi\_enterprise\_creds\_params::ca\_cert\_len](structwifi__enterprise__creds__params.md#a5f7060fcd2ca3db0b202faf15062564b)

uint32\_t ca\_cert\_len

CA certification length.

**Definition** wifi\_mgmt.h:844

[wifi\_enterprise\_creds\_params::client\_cert](structwifi__enterprise__creds__params.md#a81d61179feba627be5c6456130b9f2af)

uint8\_t \* client\_cert

Client certification.

**Definition** wifi\_mgmt.h:846

[wifi\_enterprise\_creds\_params::client\_key](structwifi__enterprise__creds__params.md#a8d88f5a8a6ccc8a9a883078af49ae96b)

uint8\_t \* client\_key

Client key.

**Definition** wifi\_mgmt.h:850

[wifi\_enterprise\_creds\_params::server\_key\_len](structwifi__enterprise__creds__params.md#a9500252974bd15037d4dbc41eba3a27d)

uint32\_t server\_key\_len

Server key length.

**Definition** wifi\_mgmt.h:872

[wifi\_enterprise\_creds\_params::dh\_param](structwifi__enterprise__creds__params.md#ab0fd7419d8a94d1d804e5554acfbf49a)

uint8\_t \* dh\_param

Diffie–Hellman parameter.

**Definition** wifi\_mgmt.h:874

[wifi\_enterprise\_creds\_params::client\_key2](structwifi__enterprise__creds__params.md#abcda4d7820681d517d70d8f130b47050)

uint8\_t \* client\_key2

Client key of phase2.

**Definition** wifi\_mgmt.h:862

[wifi\_enterprise\_creds\_params::ca\_cert2\_len](structwifi__enterprise__creds__params.md#abf35045e71afb0cb9ea25c635c5ac141)

uint32\_t ca\_cert2\_len

Phase2 CA certification length.

**Definition** wifi\_mgmt.h:856

[wifi\_enterprise\_creds\_params::dh\_param\_len](structwifi__enterprise__creds__params.md#ac548e0b006a9f7b858409cda7c3d34ba)

uint32\_t dh\_param\_len

Diffie–Hellman parameter length.

**Definition** wifi\_mgmt.h:876

[wifi\_enterprise\_creds\_params::server\_key](structwifi__enterprise__creds__params.md#acb94a8885b5ab99d1a8fb33dffebc322)

uint8\_t \* server\_key

Server key.

**Definition** wifi\_mgmt.h:870

[wifi\_enterprise\_creds\_params::server\_cert\_len](structwifi__enterprise__creds__params.md#ad0bfb59d3691e5d21cb4b810c4d1279e)

uint32\_t server\_cert\_len

Server certification length.

**Definition** wifi\_mgmt.h:868

[wifi\_enterprise\_creds\_params::server\_cert](structwifi__enterprise__creds__params.md#ad3621e92a1aa968c58a899ace72967db)

uint8\_t \* server\_cert

Server certification.

**Definition** wifi\_mgmt.h:866

[wifi\_enterprise\_creds\_params::ca\_cert2](structwifi__enterprise__creds__params.md#ad9b867873709d7f2363fef49d7b6f2ca)

uint8\_t \* ca\_cert2

CA certification of phase2.

**Definition** wifi\_mgmt.h:854

[wifi\_enterprise\_creds\_params::client\_cert2\_len](structwifi__enterprise__creds__params.md#adbe26c9b88f44eb6b875888f6a03e1bb)

uint32\_t client\_cert2\_len

Phase2 Client certification length.

**Definition** wifi\_mgmt.h:860

[wifi\_enterprise\_creds\_params::ca\_cert](structwifi__enterprise__creds__params.md#ae37381504a457b2f1d56dd5270c6711d)

uint8\_t \* ca\_cert

CA certification.

**Definition** wifi\_mgmt.h:842

[wifi\_filter\_info](structwifi__filter__info.md)

Wi-Fi filter setting for monitor, prmoiscuous, TX-injection modes.

**Definition** wifi\_mgmt.h:1001

[wifi\_filter\_info::buffer\_size](structwifi__filter__info.md#a1b2d0448fc7f62654e3f5aacfba62f8f)

uint16\_t buffer\_size

Filter buffer size.

**Definition** wifi\_mgmt.h:1007

[wifi\_filter\_info::filter](structwifi__filter__info.md#ad9560be814299055cfa11b995a7dcf42)

uint8\_t filter

Filter setting.

**Definition** wifi\_mgmt.h:1003

[wifi\_filter\_info::oper](structwifi__filter__info.md#aedd5e220cdde5768cb0f4aff920971cd)

enum wifi\_mgmt\_op oper

Get or set operation.

**Definition** wifi\_mgmt.h:1009

[wifi\_filter\_info::if\_index](structwifi__filter__info.md#af9ea91e31e78afcb7ffe1ff9a04277a3)

uint8\_t if\_index

Interface index.

**Definition** wifi\_mgmt.h:1005

[wifi\_iface\_status](structwifi__iface__status.md)

Wi-Fi interface status.

**Definition** wifi\_mgmt.h:670

[wifi\_iface\_status::beacon\_interval](structwifi__iface__status.md#a241bfbe70628006b515b5f9e4f97665c)

unsigned short beacon\_interval

Beacon interval.

**Definition** wifi\_mgmt.h:698

[wifi\_iface\_status::wpa3\_ent\_type](structwifi__iface__status.md#a361c0e8a385fdc21f16258c25c2bc8d1)

enum wifi\_wpa3\_enterprise\_type wpa3\_ent\_type

WPA3 enterprise type.

**Definition** wifi\_mgmt.h:688

[wifi\_iface\_status::ssid](structwifi__iface__status.md#a3ab671471bcdfeb5b955d156d39f2bb3)

char ssid[WIFI\_SSID\_MAX\_LEN+1]

SSID.

**Definition** wifi\_mgmt.h:676

[wifi\_iface\_status::rssi](structwifi__iface__status.md#a4e593147b88eb4938d55a4de72fcc7f6)

int rssi

RSSI.

**Definition** wifi\_mgmt.h:694

[wifi\_iface\_status::bssid](structwifi__iface__status.md#a5d5d19056a1a15365fbdd94274a0fc5e)

char bssid[WIFI\_MAC\_ADDR\_LEN]

BSSID.

**Definition** wifi\_mgmt.h:678

[wifi\_iface\_status::security](structwifi__iface__status.md#a625ecec1abec8dd65cf155eab21a01b5)

enum wifi\_security\_type security

Security type, see enum wifi\_security\_type.

**Definition** wifi\_mgmt.h:690

[wifi\_iface\_status::channel](structwifi__iface__status.md#a6432663156e5b2c424d254ed1eae0144)

unsigned int channel

Channel.

**Definition** wifi\_mgmt.h:682

[wifi\_iface\_status::mfp](structwifi__iface__status.md#aa1a9b644fd355526125ddd32416b7c24)

enum wifi\_mfp\_options mfp

MFP options, see enum wifi\_mfp\_options.

**Definition** wifi\_mgmt.h:692

[wifi\_iface\_status::dtim\_period](structwifi__iface__status.md#aae6c8cbaa16c81d308f08114d5103a3d)

unsigned char dtim\_period

DTIM period.

**Definition** wifi\_mgmt.h:696

[wifi\_iface\_status::state](structwifi__iface__status.md#ac52806155be3d64954ac6d109e76ec57)

int state

Interface state, see enum wifi\_iface\_state.

**Definition** wifi\_mgmt.h:672

[wifi\_iface\_status::twt\_capable](structwifi__iface__status.md#acfde8d64b463a9f553aa4fb689dc1917)

bool twt\_capable

is TWT capable?

**Definition** wifi\_mgmt.h:700

[wifi\_iface\_status::iface\_mode](structwifi__iface__status.md#ad33d2ec149a8d556e2472dd842ceadc0)

enum wifi\_iface\_mode iface\_mode

Interface mode, see enum wifi\_iface\_mode.

**Definition** wifi\_mgmt.h:684

[wifi\_iface\_status::ssid\_len](structwifi__iface__status.md#ad82f281941e4f6ce1ef0bca008e26d41)

unsigned int ssid\_len

SSID length.

**Definition** wifi\_mgmt.h:674

[wifi\_iface\_status::band](structwifi__iface__status.md#ae1c141a18f4e225af2c22a8cb4f882a8)

enum wifi\_frequency\_bands band

Frequency band.

**Definition** wifi\_mgmt.h:680

[wifi\_iface\_status::link\_mode](structwifi__iface__status.md#ae2de076d79f2172793d65fe9cd31edc4)

enum wifi\_link\_mode link\_mode

Link mode, see enum wifi\_link\_mode.

**Definition** wifi\_mgmt.h:686

[wifi\_iface\_status::current\_phy\_tx\_rate](structwifi__iface__status.md#af255c63862e0c9e5008b2e4952d7e491)

int current\_phy\_tx\_rate

The current 802.11 PHY TX data rate (in Mbps).

**Definition** wifi\_mgmt.h:702

[wifi\_mgmt\_ops](structwifi__mgmt__ops.md)

Wi-Fi management API.

**Definition** wifi\_mgmt.h:1306

[wifi\_mgmt\_ops::reg\_domain](structwifi__mgmt__ops.md#a0a287c8acf2d7bf9333b755589294881)

int(\* reg\_domain)(const struct device \*dev, struct wifi\_reg\_domain \*reg\_domain)

Set or get regulatory domain.

**Definition** wifi\_mgmt.h:1441

[wifi\_mgmt\_ops::send\_11k\_neighbor\_request](structwifi__mgmt__ops.md#a1cdd0b76a0a326e968d27c0a3cafcef8)

int(\* send\_11k\_neighbor\_request)(const struct device \*dev, struct wifi\_11k\_params \*params)

Send 11k neighbor request.

**Definition** wifi\_mgmt.h:1401

[wifi\_mgmt\_ops::get\_rts\_threshold](structwifi__mgmt__ops.md#a20706f9eed43b3380258b62fdf93be02)

int(\* get\_rts\_threshold)(const struct device \*dev, unsigned int \*rts\_threshold)

Set Wi-Fi enterprise mode CA/client Cert and key.

**Definition** wifi\_mgmt.h:1565

[wifi\_mgmt\_ops::ap\_config\_params](structwifi__mgmt__ops.md#a2475f32afcce72464b2db6ecad7fb3eb)

int(\* ap\_config\_params)(const struct device \*dev, struct wifi\_ap\_config\_params \*params)

Configure AP parameter.

**Definition** wifi\_mgmt.h:1528

[wifi\_mgmt\_ops::scan](structwifi__mgmt__ops.md#a267030c27da3cdc251badd0ed7f7b1cb)

int(\* scan)(const struct device \*dev, struct wifi\_scan\_params \*params, scan\_result\_cb\_t cb)

Scan for Wi-Fi networks.

**Definition** wifi\_mgmt.h:1318

[wifi\_mgmt\_ops::cfg\_11k](structwifi__mgmt__ops.md#a2cf66093ad850319cf222468e22ff485)

int(\* cfg\_11k)(const struct device \*dev, struct wifi\_11k\_params \*params)

Set or get 11K status.

**Definition** wifi\_mgmt.h:1393

[wifi\_mgmt\_ops::btm\_query](structwifi__mgmt__ops.md#a3437f5881a8e0a487c11dd43a6099b6d)

int(\* btm\_query)(const struct device \*dev, uint8\_t reason)

Send BTM query.

**Definition** wifi\_mgmt.h:1474

[wifi\_mgmt\_ops::get\_conn\_params](structwifi__mgmt__ops.md#a42c2aa55df30158d8b5d6f4c81e3e2dd)

int(\* get\_conn\_params)(const struct device \*dev, struct wifi\_connect\_req\_params \*params)

Get Wi-Fi connection parameters recently used.

**Definition** wifi\_mgmt.h:1512

[wifi\_mgmt\_ops::start\_11r\_roaming](structwifi__mgmt__ops.md#a501b114298738ac6af9c4a80f5360d79)

int(\* start\_11r\_roaming)(const struct device \*dev)

Start 11r roaming.

**Definition** wifi\_mgmt.h:1588

[wifi\_mgmt\_ops::set\_rts\_threshold](structwifi__mgmt__ops.md#a514e06d63bcf6dc11dba1d3af8d102d5)

int(\* set\_rts\_threshold)(const struct device \*dev, unsigned int rts\_threshold)

Set RTS threshold value.

**Definition** wifi\_mgmt.h:1520

[wifi\_mgmt\_ops::get\_power\_save\_config](structwifi__mgmt__ops.md#a52690b13f8a1e7b0c2302eaa24ae4c7f)

int(\* get\_power\_save\_config)(const struct device \*dev, struct wifi\_ps\_config \*config)

Get power save config.

**Definition** wifi\_mgmt.h:1433

[wifi\_mgmt\_ops::candidate\_scan](structwifi__mgmt__ops.md#a538ffba0a7e045ca9c8ac62ccefc8a36)

int(\* candidate\_scan)(const struct device \*dev, struct wifi\_scan\_params \*params)

Trigger candidate scan.

**Definition** wifi\_mgmt.h:1581

[wifi\_mgmt\_ops::disconnect](structwifi__mgmt__ops.md#a5725c6fd93ae189a3019374cd4ad2ff4)

int(\* disconnect)(const struct device \*dev)

Disconnect from a Wi-Fi network.

**Definition** wifi\_mgmt.h:1336

[wifi\_mgmt\_ops::ap\_disable](structwifi__mgmt__ops.md#a5aa7a2be82eb1783872abda2b8978235)

int(\* ap\_disable)(const struct device \*dev)

Disable AP mode.

**Definition** wifi\_mgmt.h:1352

[wifi\_mgmt\_ops::get\_stats](structwifi__mgmt__ops.md#a5e6fdf836273fcde54efff4c77bfdf0e)

int(\* get\_stats)(const struct device \*dev, struct net\_stats\_wifi \*stats)

Get Wi-Fi statistics.

**Definition** wifi\_mgmt.h:1377

[wifi\_mgmt\_ops::legacy\_roam](structwifi__mgmt__ops.md#aa088223f84094614145d9d81e3acc20a)

int(\* legacy\_roam)(const struct device \*dev)

Send legacy scan.

**Definition** wifi\_mgmt.h:1490

[wifi\_mgmt\_ops::get\_version](structwifi__mgmt__ops.md#aa7e4bc3dbc960091d11ffe5454259885)

int(\* get\_version)(const struct device \*dev, struct wifi\_version \*params)

Get Version of WiFi driver and Firmware.

**Definition** wifi\_mgmt.h:1504

[wifi\_mgmt\_ops::pmksa\_flush](structwifi__mgmt__ops.md#aadf991d6f6725e5c179ca8343d626ad8)

int(\* pmksa\_flush)(const struct device \*dev)

Flush PMKSA cache entries.

**Definition** wifi\_mgmt.h:1546

[wifi\_mgmt\_ops::wps\_config](structwifi__mgmt__ops.md#aaf85f7b56997fb40689b927535af5e85)

int(\* wps\_config)(const struct device \*dev, struct wifi\_wps\_config\_params \*params)

Start a WPS PBC/PIN connection.

**Definition** wifi\_mgmt.h:1573

[wifi\_mgmt\_ops::set\_twt](structwifi__mgmt__ops.md#ab4500534b6abe0449290c8bd8f729fc4)

int(\* set\_twt)(const struct device \*dev, struct wifi\_twt\_params \*params)

Setup or teardown TWT flow.

**Definition** wifi\_mgmt.h:1417

[wifi\_mgmt\_ops::set\_power\_save](structwifi__mgmt__ops.md#ac0f3f7fa699b1bc7db2358e77dd44cc4)

int(\* set\_power\_save)(const struct device \*dev, struct wifi\_ps\_params \*params)

Set power save status.

**Definition** wifi\_mgmt.h:1409

[wifi\_mgmt\_ops::ap\_enable](structwifi__mgmt__ops.md#ac2ce3a4a86c43e30d33261f71c44198a)

int(\* ap\_enable)(const struct device \*dev, struct wifi\_connect\_req\_params \*params)

Enable AP mode.

**Definition** wifi\_mgmt.h:1344

[wifi\_mgmt\_ops::set\_btwt](structwifi__mgmt__ops.md#ad2d1ab4db1947dbdb2909a675fa1d653)

int(\* set\_btwt)(const struct device \*dev, struct wifi\_twt\_params \*params)

Setup BTWT flow.

**Definition** wifi\_mgmt.h:1425

[wifi\_mgmt\_ops::filter](structwifi__mgmt__ops.md#ad645276745ce8dd9685e0744efdfc733)

int(\* filter)(const struct device \*dev, struct wifi\_filter\_info \*filter)

Set or get packet filter settings for monitor and promiscuous modes.

**Definition** wifi\_mgmt.h:1449

[wifi\_mgmt\_ops::iface\_status](structwifi__mgmt__ops.md#adf157476d776bc9c068e99e1a0266fd3)

int(\* iface\_status)(const struct device \*dev, struct wifi\_iface\_status \*status)

Get interface status.

**Definition** wifi\_mgmt.h:1368

[wifi\_mgmt\_ops::mode](structwifi__mgmt__ops.md#ae2fb1bc35bf9255655a30a2ad8588b7c)

int(\* mode)(const struct device \*dev, struct wifi\_mode\_info \*mode)

Set or get mode of operation.

**Definition** wifi\_mgmt.h:1457

[wifi\_mgmt\_ops::connect](structwifi__mgmt__ops.md#ae6255ea77739918797b4f3c7a4634a75)

int(\* connect)(const struct device \*dev, struct wifi\_connect\_req\_params \*params)

Connect to a Wi-Fi network.

**Definition** wifi\_mgmt.h:1328

[wifi\_mgmt\_ops::reset\_stats](structwifi__mgmt__ops.md#ae66901b434ab02863c0d3bd539c4b650)

int(\* reset\_stats)(const struct device \*dev)

Reset Wi-Fi statistics.

**Definition** wifi\_mgmt.h:1384

[wifi\_mgmt\_ops::ap\_sta\_disconnect](structwifi__mgmt__ops.md#af01aaec29be78c02314acf13b5c1b6f7)

int(\* ap\_sta\_disconnect)(const struct device \*dev, const uint8\_t \*mac)

Disconnect a STA from AP.

**Definition** wifi\_mgmt.h:1360

[wifi\_mgmt\_ops::channel](structwifi__mgmt__ops.md#af17ddfea01d0ab478f6fd50b1c9d6015)

int(\* channel)(const struct device \*dev, struct wifi\_channel\_info \*channel)

Set or get current channel of operation.

**Definition** wifi\_mgmt.h:1465

[wifi\_mgmt\_ops::bss\_ext\_capab](structwifi__mgmt__ops.md#afb83b59f392b11fe8071ca57e3ea3928)

int(\* bss\_ext\_capab)(const struct device \*dev, int capab)

Judge ap whether support the capability.

**Definition** wifi\_mgmt.h:1482

[wifi\_mode\_info](structwifi__mode__info.md)

Wi-Fi mode setup.

**Definition** wifi\_mgmt.h:991

[wifi\_mode\_info::oper](structwifi__mode__info.md#a57c101db8b81ab0ac5dd0a158057a64a)

enum wifi\_mgmt\_op oper

Get or set operation.

**Definition** wifi\_mgmt.h:997

[wifi\_mode\_info::mode](structwifi__mode__info.md#aa29d3b88fc718aa3ac05daf38974707d)

uint8\_t mode

Mode setting for a specific mode of operation.

**Definition** wifi\_mgmt.h:993

[wifi\_mode\_info::if\_index](structwifi__mode__info.md#add58dd3b45fd2ddaf684d1b0de81bef9)

uint8\_t if\_index

Interface index.

**Definition** wifi\_mgmt.h:995

[wifi\_ps\_config](structwifi__ps__config.md)

Wi-Fi power save configuration.

**Definition** wifi\_mgmt.h:880

[wifi\_ps\_config::ps\_params](structwifi__ps__config.md#a357aafc2dedda37755b1cb1fc07fe5a6)

struct wifi\_ps\_params ps\_params

Power save configuration.

**Definition** wifi\_mgmt.h:886

[wifi\_ps\_config::num\_twt\_flows](structwifi__ps__config.md#a9e83c10eaaa1d721cbc49b40aedb00df)

char num\_twt\_flows

Number of TWT flows.

**Definition** wifi\_mgmt.h:882

[wifi\_ps\_config::twt\_flows](structwifi__ps__config.md#ab7460f0f253b2d552e49e98e2c770967)

struct wifi\_twt\_flow\_info twt\_flows[WIFI\_MAX\_TWT\_FLOWS]

TWT flow details.

**Definition** wifi\_mgmt.h:884

[wifi\_ps\_params](structwifi__ps__params.md)

Wi-Fi power save parameters.

**Definition** wifi\_mgmt.h:706

[wifi\_ps\_params::mode](structwifi__ps__params.md#a5a022d89d43ecf2cd1f15fc72c0f2bed)

enum wifi\_ps\_mode mode

Wi-Fi power save mode.

**Definition** wifi\_mgmt.h:714

[wifi\_ps\_params::fail\_reason](structwifi__ps__params.md#a63fa2ee03bc4aefada61c298ee14336c)

enum wifi\_config\_ps\_param\_fail\_reason fail\_reason

Wi-Fi power save fail reason.

**Definition** wifi\_mgmt.h:727

[wifi\_ps\_params::wakeup\_mode](structwifi__ps__params.md#a7cb3e7fb7d9f8bd7c2cab41f879b3b66)

enum wifi\_ps\_wakeup\_mode wakeup\_mode

Wi-Fi power save wakeup mode.

**Definition** wifi\_mgmt.h:712

[wifi\_ps\_params::listen\_interval](structwifi__ps__params.md#a8510c799ab0c5825f1c6349f9799c62f)

unsigned short listen\_interval

Listen interval.

**Definition** wifi\_mgmt.h:710

[wifi\_ps\_params::exit\_strategy](structwifi__ps__params.md#ab9fc62dd1e2928320274fa1554a550a6)

enum wifi\_ps\_exit\_strategy exit\_strategy

Wi-Fi power save exit strategy.

**Definition** wifi\_mgmt.h:729

[wifi\_ps\_params::enabled](structwifi__ps__params.md#abb22aaa45833ac130922204bd2fe841b)

enum wifi\_ps enabled

Power save state.

**Definition** wifi\_mgmt.h:708

[wifi\_ps\_params::timeout\_ms](structwifi__ps__params.md#ad963f1bf78dc271f08b73f3aadb36a91)

unsigned int timeout\_ms

Wi-Fi power save timeout.

**Definition** wifi\_mgmt.h:723

[wifi\_ps\_params::type](structwifi__ps__params.md#aef62e5bf6216bf4dc461efe71735c4bd)

enum wifi\_ps\_param\_type type

Wi-Fi power save type.

**Definition** wifi\_mgmt.h:725

[wifi\_raw\_scan\_result](structwifi__raw__scan__result.md)

Wi-Fi raw scan result.

**Definition** wifi\_mgmt.h:950

[wifi\_raw\_scan\_result::rssi](structwifi__raw__scan__result.md#a3f08580c6448a5fa28dd8a594fa7dad6)

int8\_t rssi

RSSI.

**Definition** wifi\_mgmt.h:952

[wifi\_raw\_scan\_result::data](structwifi__raw__scan__result.md#a5710e89199c147ce898602795f00aba3)

uint8\_t data[CONFIG\_WIFI\_MGMT\_RAW\_SCAN\_RESULT\_LENGTH]

Raw scan data.

**Definition** wifi\_mgmt.h:958

[wifi\_raw\_scan\_result::frame\_length](structwifi__raw__scan__result.md#a876966f469714eb481b42ccc8a63945c)

int frame\_length

Frame length.

**Definition** wifi\_mgmt.h:954

[wifi\_raw\_scan\_result::frequency](structwifi__raw__scan__result.md#aa2c7781882c6775616cbc8016b0842f6)

unsigned short frequency

Frequency.

**Definition** wifi\_mgmt.h:956

[wifi\_reg\_chan\_info](structwifi__reg__chan__info.md)

Per-channel regulatory attributes.

**Definition** wifi\_mgmt.h:911

[wifi\_reg\_chan\_info::center\_frequency](structwifi__reg__chan__info.md#a0addffc11ef29f50c01b700835e59930)

unsigned short center\_frequency

Center frequency in MHz.

**Definition** wifi\_mgmt.h:913

[wifi\_reg\_chan\_info::dfs](structwifi__reg__chan__info.md#a1ab137c142902d2de7d6be2626d7ac1f)

unsigned short dfs

Is a DFS channel.

**Definition** wifi\_mgmt.h:921

[wifi\_reg\_chan\_info::supported](structwifi__reg__chan__info.md#aa044611e18b7332b8577e29f6a769e3f)

unsigned short supported

Is channel supported or not.

**Definition** wifi\_mgmt.h:917

[wifi\_reg\_chan\_info::passive\_only](structwifi__reg__chan__info.md#acc7a88b004c9a61c8bf9ee1a97f85928)

unsigned short passive\_only

Passive transmissions only.

**Definition** wifi\_mgmt.h:919

[wifi\_reg\_chan\_info::max\_power](structwifi__reg__chan__info.md#af9169ab4a41fac4c6f6766fc96799545)

unsigned short max\_power

Maximum transmission power (in dBm).

**Definition** wifi\_mgmt.h:915

[wifi\_reg\_domain](structwifi__reg__domain.md)

Regulatory domain information or configuration.

**Definition** wifi\_mgmt.h:925

[wifi\_reg\_domain::num\_channels](structwifi__reg__domain.md#a3278e9f43893f49ab9f9d0d7f24009c1)

unsigned int num\_channels

Number of channels supported.

**Definition** wifi\_mgmt.h:935

[wifi\_reg\_domain::oper](structwifi__reg__domain.md#a3bbfdf1497a87bbb6b6211c7035e1002)

enum wifi\_mgmt\_op oper

Regulatory domain operation.

**Definition** wifi\_mgmt.h:927

[wifi\_reg\_domain::chan\_info](structwifi__reg__domain.md#a4c8c9c11e41123cd7738fdb0d33ae5fb)

struct wifi\_reg\_chan\_info \* chan\_info

Channels information.

**Definition** wifi\_mgmt.h:937

[wifi\_reg\_domain::force](structwifi__reg__domain.md#a567c6fcae8032567aea83c18cd211c33)

bool force

Ignore all other regulatory hints over this one, the behavior is implementation specific.

**Definition** wifi\_mgmt.h:931

[wifi\_reg\_domain::country\_code](structwifi__reg__domain.md#abf191495814c227fbbfaccb2f727762e)

uint8\_t country\_code[WIFI\_COUNTRY\_CODE\_LEN]

Country code: ISO/IEC 3166-1 alpha-2.

**Definition** wifi\_mgmt.h:933

[wifi\_scan\_params](structwifi__scan__params.md)

Wi-Fi scan parameters structure.

**Definition** wifi\_mgmt.h:443

[wifi\_scan\_params::max\_bss\_cnt](structwifi__scan__params.md#a12d5dea7d8fa8ad03ac2366720c46243)

uint16\_t max\_bss\_cnt

Specifies the maximum number of scan results to return.

**Definition** wifi\_mgmt.h:472

[wifi\_scan\_params::dwell\_time\_active](structwifi__scan__params.md#a2453a75c23e04e3572559c0e7199c1b4)

uint16\_t dwell\_time\_active

Active scan dwell time (in ms) on a channel.

**Definition** wifi\_mgmt.h:458

[wifi\_scan\_params::scan\_type](structwifi__scan__params.md#a645acc54603cd4692527c1a028933078)

enum wifi\_scan\_type scan\_type

Scan type, see enum wifi\_scan\_type.

**Definition** wifi\_mgmt.h:451

[wifi\_scan\_params::bands](structwifi__scan__params.md#a6b571d960ed9d7419e31530e5fb6f97a)

uint8\_t bands

Bitmap of bands to be scanned.

**Definition** wifi\_mgmt.h:455

[wifi\_scan\_params::dwell\_time\_passive](structwifi__scan__params.md#a8e7a37ccda8de635e7b7066d7943e814)

uint16\_t dwell\_time\_passive

Passive scan dwell time (in ms) on a channel.

**Definition** wifi\_mgmt.h:461

[wifi\_scan\_params::band\_chan](structwifi__scan__params.md#aa5ddbd6bc97b7598288d4b0d38521681)

struct wifi\_band\_channel band\_chan[WIFI\_MGMT\_SCAN\_CHAN\_MAX\_MANUAL]

Channel information array indexed on Wi-Fi frequency bands and channels within that band.

**Definition** wifi\_mgmt.h:487

[wifi\_scan\_params::ssids](structwifi__scan__params.md#aac11ee8e0ec8a4fa24668f4820bd1a12)

const char \* ssids[WIFI\_MGMT\_SCAN\_SSID\_FILT\_MAX]

Array of SSID strings to scan.

**Definition** wifi\_mgmt.h:464

[wifi\_scan\_result](structwifi__scan__result.md)

Wi-Fi scan result, each result is provided to the net\_mgmt\_event\_callback via its info attribute (see...

**Definition** wifi\_mgmt.h:493

[wifi\_scan\_result::ssid\_length](structwifi__scan__result.md#a2c1c2f4265b914df08fc75deb8b69d39)

uint8\_t ssid\_length

SSID length.

**Definition** wifi\_mgmt.h:497

[wifi\_scan\_result::band](structwifi__scan__result.md#a38201c9dd798dc11b5bda3ce97b02e92)

uint8\_t band

Frequency band.

**Definition** wifi\_mgmt.h:499

[wifi\_scan\_result::mac](structwifi__scan__result.md#a4fdbc4dc4d5c8b279223e8c06624f434)

uint8\_t mac[WIFI\_MAC\_ADDR\_LEN]

BSSID.

**Definition** wifi\_mgmt.h:511

[wifi\_scan\_result::rssi](structwifi__scan__result.md#a76aa012136e3721fd4a482a22b93546f)

int8\_t rssi

RSSI.

**Definition** wifi\_mgmt.h:509

[wifi\_scan\_result::mac\_length](structwifi__scan__result.md#a8fca0dabec00ebd7ed4800098ec9d451)

uint8\_t mac\_length

BSSID length.

**Definition** wifi\_mgmt.h:513

[wifi\_scan\_result::ssid](structwifi__scan__result.md#aaefb8f5c9510e4f5002ae306d853ade8)

uint8\_t ssid[WIFI\_SSID\_MAX\_LEN+1]

SSID.

**Definition** wifi\_mgmt.h:495

[wifi\_scan\_result::wpa3\_ent\_type](structwifi__scan__result.md#abb7de47c605ec05c8fe0a06ecbd2b7b6)

enum wifi\_wpa3\_enterprise\_type wpa3\_ent\_type

WPA3 enterprise type.

**Definition** wifi\_mgmt.h:505

[wifi\_scan\_result::mfp](structwifi__scan__result.md#acaa3fb30ebf6df22bfac6380698ed28e)

enum wifi\_mfp\_options mfp

MFP options.

**Definition** wifi\_mgmt.h:507

[wifi\_scan\_result::channel](structwifi__scan__result.md#adbbfd7692ee5ffd6344fe78b9d91c840)

uint8\_t channel

Channel.

**Definition** wifi\_mgmt.h:501

[wifi\_scan\_result::security](structwifi__scan__result.md#af2d3dc5d115e3db76d3bc115510b0a5a)

enum wifi\_security\_type security

Security type.

**Definition** wifi\_mgmt.h:503

[wifi\_status](structwifi__status.md)

Generic Wi-Fi status for commands and events.

**Definition** wifi\_mgmt.h:656

[wifi\_status::ap\_status](structwifi__status.md#a02f0fcc7ef57661ca95d0c99f045aef1)

enum wifi\_ap\_status ap\_status

Access point status.

**Definition** wifi\_mgmt.h:665

[wifi\_status::conn\_status](structwifi__status.md#a8f885e78366d0499e4ba8e15bef275ac)

enum wifi\_conn\_status conn\_status

Connection status.

**Definition** wifi\_mgmt.h:661

[wifi\_status::disconn\_reason](structwifi__status.md#aa04b5033d93274badd27f702af9830bc)

enum wifi\_disconn\_reason disconn\_reason

Disconnection reason status.

**Definition** wifi\_mgmt.h:663

[wifi\_status::status](structwifi__status.md#aa1dbff8154400f8353693d387977008b)

int status

Status value.

**Definition** wifi\_mgmt.h:659

[wifi\_twt\_flow\_info](structwifi__twt__flow__info.md)

Wi-Fi TWT flow information.

**Definition** wifi\_mgmt.h:816

[wifi\_twt\_flow\_info::dialog\_token](structwifi__twt__flow__info.md#a123ce10bed8b62b01919a7ea7644a0ba)

uint8\_t dialog\_token

Dialog token, used to map requests to responses.

**Definition** wifi\_mgmt.h:820

[wifi\_twt\_flow\_info::negotiation\_type](structwifi__twt__flow__info.md#a620ae8ba546e4091d74280cb1553b2cf)

enum wifi\_twt\_negotiation\_type negotiation\_type

TWT negotiation type, see enum wifi\_twt\_negotiation\_type.

**Definition** wifi\_mgmt.h:824

[wifi\_twt\_flow\_info::twt\_wake\_ahead\_duration](structwifi__twt__flow__info.md#a6384d3829d54a58a53eafcb74c64a658)

uint32\_t twt\_wake\_ahead\_duration

Wake ahead duration.

**Definition** wifi\_mgmt.h:836

[wifi\_twt\_flow\_info::trigger](structwifi__twt__flow__info.md#a952a67bd092c5dadba387bb13449c6f3)

bool trigger

Trigger enabled or disabled.

**Definition** wifi\_mgmt.h:828

[wifi\_twt\_flow\_info::responder](structwifi__twt__flow__info.md#ac82e4de8ffc82f851061f8ba8d217dc1)

bool responder

Requestor or responder.

**Definition** wifi\_mgmt.h:826

[wifi\_twt\_flow\_info::flow\_id](structwifi__twt__flow__info.md#acb0c618f1cebcb172f342cfe222683be)

uint8\_t flow\_id

Flow ID, used to map setup with teardown.

**Definition** wifi\_mgmt.h:822

[wifi\_twt\_flow\_info::twt\_interval](structwifi__twt__flow__info.md#ae15ba49fa54f82cc6a1fb0d4572114b7)

uint64\_t twt\_interval

Interval = Wake up time + Sleeping time.

**Definition** wifi\_mgmt.h:818

[wifi\_twt\_flow\_info::twt\_wake\_interval](structwifi__twt__flow__info.md#aede6cb0cfc999fac8ded49e2981a3762)

uint32\_t twt\_wake\_interval

Wake up time.

**Definition** wifi\_mgmt.h:834

[wifi\_twt\_flow\_info::implicit](structwifi__twt__flow__info.md#afb480be82d1c6f351bd634fd83bfa5c7)

bool implicit

Implicit or explicit.

**Definition** wifi\_mgmt.h:830

[wifi\_twt\_flow\_info::announce](structwifi__twt__flow__info.md#afc81a5111c265fd9bb2aca5f9510bfa8)

bool announce

Announced or unannounced.

**Definition** wifi\_mgmt.h:832

[wifi\_twt\_params](structwifi__twt__params.md)

Wi-Fi TWT parameters.

**Definition** wifi\_mgmt.h:733

[wifi\_twt\_params::announce](structwifi__twt__params.md#a02f2d822d530e5376f256503439a54f9)

bool announce

Announced or unannounced.

**Definition** wifi\_mgmt.h:760

[wifi\_twt\_params::max\_sta\_support](structwifi__twt__params.md#a1de9544f9bfd441df166ba2413cf11c3)

uint8\_t max\_sta\_support

Max STA support.

**Definition** wifi\_mgmt.h:783

[wifi\_twt\_params::twt\_offset](structwifi__twt__params.md#a22323b963a01399f26bb02aa95975728)

uint16\_t twt\_offset

TWT offset.

**Definition** wifi\_mgmt.h:787

[wifi\_twt\_params::teardown\_all](structwifi__twt__params.md#a26d6bda00452f77832f69f4465c13efb)

bool teardown\_all

Teardown all flows.

**Definition** wifi\_mgmt.h:796

[wifi\_twt\_params::setup\_cmd](structwifi__twt__params.md#a347f8cff73ee6b6ba6d15ddf6f376a2d)

enum wifi\_twt\_setup\_cmd setup\_cmd

TWT setup command, see enum wifi\_twt\_setup\_cmd.

**Definition** wifi\_mgmt.h:739

[wifi\_twt\_params::trigger](structwifi__twt__params.md#a4e822c04b52fe6a9489e48e26b8f9382)

bool trigger

Trigger enabled or disabled.

**Definition** wifi\_mgmt.h:756

[wifi\_twt\_params::negotiation\_type](structwifi__twt__params.md#a5fd269328f68838b8a7e3a0b93eed894)

enum wifi\_twt\_negotiation\_type negotiation\_type

TWT negotiation type, see enum wifi\_twt\_negotiation\_type.

**Definition** wifi\_mgmt.h:737

[wifi\_twt\_params::operation](structwifi__twt__params.md#a6f0483861a387651c9c89ba182e064bd)

enum wifi\_twt\_operation operation

TWT operation, see enum wifi\_twt\_operation.

**Definition** wifi\_mgmt.h:735

[wifi\_twt\_params::twt\_wake\_ahead\_duration](structwifi__twt__params.md#a6f907ca412251fdd7391f29bfa6d7713)

uint32\_t twt\_wake\_ahead\_duration

Wake ahead notification is sent earlier than TWT Service period (SP) start based on this duration.

**Definition** wifi\_mgmt.h:768

[wifi\_twt\_params::fail\_reason](structwifi__twt__params.md#a70f58b502bb67ef3b2068ded2160b612)

enum wifi\_twt\_fail\_reason fail\_reason

TWT fail reason, see enum wifi\_twt\_fail\_reason.

**Definition** wifi\_mgmt.h:800

[wifi\_twt\_params::btwt](structwifi__twt__params.md#a72ab809144b1dd3e7e121e489ef399e2)

struct wifi\_twt\_params::@302311362167322044106272253111230157111235232263::@053165077055023247316045052326043107125356150312 btwt

Setup specific parameters.

[wifi\_twt\_params::twt\_wake\_interval](structwifi__twt__params.md#a7c297459a17ed2fd232c62cca63e952f)

uint32\_t twt\_wake\_interval

Wake up time.

**Definition** wifi\_mgmt.h:762

[wifi\_twt\_params::resp\_status](structwifi__twt__params.md#a805a23284ed4afa46b84efcd43329beb)

enum wifi\_twt\_setup\_resp\_status resp\_status

TWT setup response status, see enum wifi\_twt\_setup\_resp\_status.

**Definition** wifi\_mgmt.h:741

[wifi\_twt\_params::implicit](structwifi__twt__params.md#a8ea1e2501c8b69dc3fa606eb360f8678)

bool implicit

Implicit or explicit.

**Definition** wifi\_mgmt.h:758

[wifi\_twt\_params::nominal\_wake](structwifi__twt__params.md#a91637cecaa940422b08a40f4b830a3d2)

uint8\_t nominal\_wake

Range 64-255.

**Definition** wifi\_mgmt.h:781

[wifi\_twt\_params::flow\_id](structwifi__twt__params.md#a95ec4b32d37309efa47256ae1ea865da)

uint8\_t flow\_id

Flow ID, used to map setup with teardown.

**Definition** wifi\_mgmt.h:747

[wifi\_twt\_params::teardown\_status](structwifi__twt__params.md#a9faff59e577775b3fe53f2139462ac71)

enum wifi\_twt\_teardown\_status teardown\_status

TWT teardown cmd status, see enum wifi\_twt\_teardown\_status.

**Definition** wifi\_mgmt.h:743

[wifi\_twt\_params::twt\_exponent](structwifi__twt__params.md#aabb77296f007cb055f78fa1ec3d155a3)

uint8\_t twt\_exponent

TWT exponent.

**Definition** wifi\_mgmt.h:772

[wifi\_twt\_params::twt\_mantissa](structwifi__twt__params.md#aadad4556e2e5405b0703ebb4233a4d17)

uint16\_t twt\_mantissa

TWT Mantissa Range: [0-sizeof(UINT16)].

**Definition** wifi\_mgmt.h:774

[wifi\_twt\_params::teardown](structwifi__twt__params.md#aadf62f6386359ad15491d0073c9065bf)

struct wifi\_twt\_params::@302311362167322044106272253111230157111235232263::@352270327013076240220216032274341232230206256214 teardown

Teardown specific parameters.

[wifi\_twt\_params::twt\_interval](structwifi__twt__params.md#ab92fe571559fcd5d97cdf7e6b7d86681)

uint64\_t twt\_interval

Interval = Wake up time + Sleeping time.

**Definition** wifi\_mgmt.h:752

[wifi\_twt\_params::twt\_info\_disable](structwifi__twt__params.md#ac02eab9593b1ec2c9a0453a67076df88)

bool twt\_info\_disable

TWT info enabled or disable.

**Definition** wifi\_mgmt.h:770

[wifi\_twt\_params::sub\_id](structwifi__twt__params.md#acc7234fa321938e48dd9be23b4bcbade)

uint16\_t sub\_id

Broadcast TWT AP config.

**Definition** wifi\_mgmt.h:779

[wifi\_twt\_params::sp\_gap](structwifi__twt__params.md#ada6919e0b201cec5f2c97eeaab46bec7)

uint8\_t sp\_gap

SP gap.

**Definition** wifi\_mgmt.h:791

[wifi\_twt\_params::dialog\_token](structwifi__twt__params.md#adda47e302a87a766f18e28016963a561)

uint8\_t dialog\_token

Dialog token, used to map requests to responses.

**Definition** wifi\_mgmt.h:745

[wifi\_twt\_params::responder](structwifi__twt__params.md#ae547c6fc1c7cbad15bebcfdaa43f59e7)

bool responder

Requestor or responder.

**Definition** wifi\_mgmt.h:754

[wifi\_twt\_params::setup](structwifi__twt__params.md#aee57c0189b210cfcc18e213e35b9479c)

struct wifi\_twt\_params::@302311362167322044106272253111230157111235232263::@007355023165260313375314073015252271352275036053 setup

Setup specific parameters.

[wifi\_version](structwifi__version.md)

Wi-Fi version.

**Definition** wifi\_mgmt.h:421

[wifi\_version::fw\_version](structwifi__version.md#a4bf2cbdf5c43ff21718ccf19646c164e)

const char \* fw\_version

Firmware version.

**Definition** wifi\_mgmt.h:425

[wifi\_version::drv\_version](structwifi__version.md#aea828bdb512440d6aa3cc853525c4971)

const char \* drv\_version

Driver version.

**Definition** wifi\_mgmt.h:423

[wifi\_wps\_config\_params](structwifi__wps__config__params.md)

Wi-Fi wps setup.

**Definition** wifi\_mgmt.h:1254

[wifi\_wps\_config\_params::pin](structwifi__wps__config__params.md#a962bd6513c564150e0c75112b96bbe15)

char pin[8+1]

pin value

**Definition** wifi\_mgmt.h:1258

[wifi\_wps\_config\_params::oper](structwifi__wps__config__params.md#aa7a10889c5cd5124983b0f7242d23b7e)

enum wifi\_wps\_op oper

wps operation

**Definition** wifi\_mgmt.h:1256

[wifi.h](wifi_8h.md)

IEEE 802.11 protocol and general Wi-Fi definitions.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [wifi\_mgmt.h](wifi__mgmt_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
