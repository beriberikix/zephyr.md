---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/wifi__mgmt_8h_source.html
original_path: doxygen/html/wifi__mgmt_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
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

35#define NET\_WIFI\_LAYER NET\_MGMT\_LAYER\_L2

36#define NET\_WIFI\_CODE NET\_MGMT\_LAYER\_CODE\_WIFI

37#define NET\_WIFI\_BASE (NET\_MGMT\_IFACE\_BIT | \

38 NET\_MGMT\_LAYER(NET\_WIFI\_LAYER) | \

39 NET\_MGMT\_LAYER\_CODE(NET\_WIFI\_CODE))

40#define NET\_WIFI\_EVENT (NET\_WIFI\_BASE | NET\_MGMT\_EVENT\_BIT)

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

143 (NET\_WIFI\_BASE | NET\_REQUEST\_WIFI\_CMD\_SCAN)

144

145[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)([NET\_REQUEST\_WIFI\_SCAN](group__wifi__mgmt.md#ga1c277da90986fa52dca182c4d922646f));

146

[ 148](group__wifi__mgmt.md#gaa7ab2a97950a22736bb69f60b459f0f6)#define NET\_REQUEST\_WIFI\_CONNECT \

149 (NET\_WIFI\_BASE | NET\_REQUEST\_WIFI\_CMD\_CONNECT)

150

151[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)([NET\_REQUEST\_WIFI\_CONNECT](group__wifi__mgmt.md#gaa7ab2a97950a22736bb69f60b459f0f6));

152

[ 154](group__wifi__mgmt.md#ga90afd8d4e83056463ec6e667ed8ea60a)#define NET\_REQUEST\_WIFI\_DISCONNECT \

155 (NET\_WIFI\_BASE | NET\_REQUEST\_WIFI\_CMD\_DISCONNECT)

156

157[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)([NET\_REQUEST\_WIFI\_DISCONNECT](group__wifi__mgmt.md#ga90afd8d4e83056463ec6e667ed8ea60a));

158

[ 160](group__wifi__mgmt.md#ga638d2eb0a5029c1af46a91b523ed8589)#define NET\_REQUEST\_WIFI\_AP\_ENABLE \

161 (NET\_WIFI\_BASE | NET\_REQUEST\_WIFI\_CMD\_AP\_ENABLE)

162

163[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)([NET\_REQUEST\_WIFI\_AP\_ENABLE](group__wifi__mgmt.md#ga638d2eb0a5029c1af46a91b523ed8589));

164

[ 166](group__wifi__mgmt.md#gaf81f62bf4c9e331a095acbf0d24ca1a2)#define NET\_REQUEST\_WIFI\_AP\_DISABLE \

167 (NET\_WIFI\_BASE | NET\_REQUEST\_WIFI\_CMD\_AP\_DISABLE)

168

169[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)([NET\_REQUEST\_WIFI\_AP\_DISABLE](group__wifi__mgmt.md#gaf81f62bf4c9e331a095acbf0d24ca1a2));

170

[ 172](group__wifi__mgmt.md#ga9918582d4e7bb0952daf993ee34e166d)#define NET\_REQUEST\_WIFI\_AP\_RTS\_THRESHOLD \

173 (NET\_WIFI\_BASE | NET\_REQUEST\_WIFI\_CMD\_AP\_RTS\_THRESHOLD)

174

175[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)([NET\_REQUEST\_WIFI\_AP\_RTS\_THRESHOLD](group__wifi__mgmt.md#ga9918582d4e7bb0952daf993ee34e166d));

176

[ 178](group__wifi__mgmt.md#ga3e45f6ee3801553619d8eb7d0af506eb)#define NET\_REQUEST\_WIFI\_IFACE\_STATUS \

179 (NET\_WIFI\_BASE | NET\_REQUEST\_WIFI\_CMD\_IFACE\_STATUS)

180

181[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)([NET\_REQUEST\_WIFI\_IFACE\_STATUS](group__wifi__mgmt.md#ga3e45f6ee3801553619d8eb7d0af506eb));

182

[ 183](group__wifi__mgmt.md#gadd9b5b206c7ee2e40c30a37c7b4fc002)#define NET\_REQUEST\_WIFI\_11K\_CONFIG \

184 (NET\_WIFI\_BASE | NET\_REQUEST\_WIFI\_CMD\_11K\_CONFIG)

185

186[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)([NET\_REQUEST\_WIFI\_11K\_CONFIG](group__wifi__mgmt.md#gadd9b5b206c7ee2e40c30a37c7b4fc002));

187

[ 188](group__wifi__mgmt.md#ga4a2b1e8befd7376749b1d4fbcf98376f)#define NET\_REQUEST\_WIFI\_11K\_NEIGHBOR\_REQUEST \

189 (NET\_WIFI\_BASE | NET\_REQUEST\_WIFI\_CMD\_11K\_NEIGHBOR\_REQUEST)

190

191[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)([NET\_REQUEST\_WIFI\_11K\_NEIGHBOR\_REQUEST](group__wifi__mgmt.md#ga4a2b1e8befd7376749b1d4fbcf98376f));

192

[ 194](group__wifi__mgmt.md#ga68aaced888f98e1ba4e6b61b53e5e2ba)#define NET\_REQUEST\_WIFI\_PS \

195 (NET\_WIFI\_BASE | NET\_REQUEST\_WIFI\_CMD\_PS)

196

197[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)([NET\_REQUEST\_WIFI\_PS](group__wifi__mgmt.md#ga68aaced888f98e1ba4e6b61b53e5e2ba));

198

[ 200](group__wifi__mgmt.md#gab84fd7e9ca0bf0b2b9d08889dda26aad)#define NET\_REQUEST\_WIFI\_TWT \

201 (NET\_WIFI\_BASE | NET\_REQUEST\_WIFI\_CMD\_TWT)

202

203[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)([NET\_REQUEST\_WIFI\_TWT](group__wifi__mgmt.md#gab84fd7e9ca0bf0b2b9d08889dda26aad));

204

[ 205](group__wifi__mgmt.md#gaf1a806a89b0fd20de950c6e085351134)#define NET\_REQUEST\_WIFI\_BTWT \

206 (NET\_WIFI\_BASE | NET\_REQUEST\_WIFI\_CMD\_BTWT)

207

208[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)([NET\_REQUEST\_WIFI\_BTWT](group__wifi__mgmt.md#gaf1a806a89b0fd20de950c6e085351134));

209

[ 211](group__wifi__mgmt.md#ga1032f3773cfe6130da4d4d498b044ee2)#define NET\_REQUEST\_WIFI\_PS\_CONFIG \

212 (NET\_WIFI\_BASE | NET\_REQUEST\_WIFI\_CMD\_PS\_CONFIG)

213

214[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)([NET\_REQUEST\_WIFI\_PS\_CONFIG](group__wifi__mgmt.md#ga1032f3773cfe6130da4d4d498b044ee2));

215

[ 217](group__wifi__mgmt.md#ga2b27d102b779a6d846b375854768fb7f)#define NET\_REQUEST\_WIFI\_REG\_DOMAIN \

218 (NET\_WIFI\_BASE | NET\_REQUEST\_WIFI\_CMD\_REG\_DOMAIN)

219

220[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)([NET\_REQUEST\_WIFI\_REG\_DOMAIN](group__wifi__mgmt.md#ga2b27d102b779a6d846b375854768fb7f));

221

[ 223](group__wifi__mgmt.md#ga9b4da60a8108b0cc431ac1eecfca0cd0)#define NET\_REQUEST\_WIFI\_MODE \

224 (NET\_WIFI\_BASE | NET\_REQUEST\_WIFI\_CMD\_MODE)

225

226[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)([NET\_REQUEST\_WIFI\_MODE](group__wifi__mgmt.md#ga9b4da60a8108b0cc431ac1eecfca0cd0));

227

[ 229](group__wifi__mgmt.md#ga3098e817d12bf4619c9fd2698508fb4e)#define NET\_REQUEST\_WIFI\_PACKET\_FILTER \

230 (NET\_WIFI\_BASE | NET\_REQUEST\_WIFI\_CMD\_PACKET\_FILTER)

231

232[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)([NET\_REQUEST\_WIFI\_PACKET\_FILTER](group__wifi__mgmt.md#ga3098e817d12bf4619c9fd2698508fb4e));

233

[ 235](group__wifi__mgmt.md#gad9614d2368f8399850aaec05e40bdc78)#define NET\_REQUEST\_WIFI\_CHANNEL \

236 (NET\_WIFI\_BASE | NET\_REQUEST\_WIFI\_CMD\_CHANNEL)

237

238[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)([NET\_REQUEST\_WIFI\_CHANNEL](group__wifi__mgmt.md#gad9614d2368f8399850aaec05e40bdc78));

239

[ 241](group__wifi__mgmt.md#gaa3e52e08d89a1104f07207e52b81d503)#define NET\_REQUEST\_WIFI\_AP\_STA\_DISCONNECT \

242 (NET\_WIFI\_BASE | NET\_REQUEST\_WIFI\_CMD\_AP\_STA\_DISCONNECT)

243

244[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)([NET\_REQUEST\_WIFI\_AP\_STA\_DISCONNECT](group__wifi__mgmt.md#gaa3e52e08d89a1104f07207e52b81d503));

245

[ 247](group__wifi__mgmt.md#ga3e60c29ca9ce95d17a7fff087290f7f1)#define NET\_REQUEST\_WIFI\_VERSION \

248 (NET\_WIFI\_BASE | NET\_REQUEST\_WIFI\_CMD\_VERSION)

249

250[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)([NET\_REQUEST\_WIFI\_VERSION](group__wifi__mgmt.md#ga3e60c29ca9ce95d17a7fff087290f7f1));

251

[ 253](group__wifi__mgmt.md#gac6483341435ff380a2d4a69430899c1a)#define NET\_REQUEST\_WIFI\_CONN\_PARAMS \

254 (NET\_WIFI\_BASE | NET\_REQUEST\_WIFI\_CMD\_CONN\_PARAMS)

255

256[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)([NET\_REQUEST\_WIFI\_CONN\_PARAMS](group__wifi__mgmt.md#gac6483341435ff380a2d4a69430899c1a));

257

[ 259](group__wifi__mgmt.md#ga22d80ef0ffb15e4286d7b1c3325d5334)#define NET\_REQUEST\_WIFI\_RTS\_THRESHOLD \

260 (NET\_WIFI\_BASE | NET\_REQUEST\_WIFI\_CMD\_RTS\_THRESHOLD)

261

262[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)([NET\_REQUEST\_WIFI\_RTS\_THRESHOLD](group__wifi__mgmt.md#ga22d80ef0ffb15e4286d7b1c3325d5334));

263

[ 265](group__wifi__mgmt.md#gaf4a78d230f5e0743a6aaf152ddda1c67)#define NET\_REQUEST\_WIFI\_AP\_CONFIG\_PARAM \

266 (NET\_WIFI\_BASE | NET\_REQUEST\_WIFI\_CMD\_AP\_CONFIG\_PARAM)

267

268[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)([NET\_REQUEST\_WIFI\_AP\_CONFIG\_PARAM](group__wifi__mgmt.md#gaf4a78d230f5e0743a6aaf152ddda1c67));

269

270#ifdef CONFIG\_WIFI\_NM\_WPA\_SUPPLICANT\_DPP

272#define NET\_REQUEST\_WIFI\_DPP \

273 (NET\_WIFI\_BASE | NET\_REQUEST\_WIFI\_CMD\_DPP)

274

275[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_WIFI\_DPP);

276#endif /\* CONFIG\_WIFI\_NM\_WPA\_SUPPLICANT\_DPP \*/

277

[ 279](group__wifi__mgmt.md#ga4f644b4c980628ffd556458eddc0933d)#define NET\_REQUEST\_WIFI\_BTM\_QUERY (NET\_WIFI\_BASE | NET\_REQUEST\_WIFI\_CMD\_BTM\_QUERY)

280

281[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)([NET\_REQUEST\_WIFI\_BTM\_QUERY](group__wifi__mgmt.md#ga4f644b4c980628ffd556458eddc0933d));

282

[ 284](group__wifi__mgmt.md#ga9070995249eb35de37e2b60c4426f840)#define NET\_REQUEST\_WIFI\_PMKSA\_FLUSH \

285 (NET\_WIFI\_BASE | NET\_REQUEST\_WIFI\_CMD\_PMKSA\_FLUSH)

286

287[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)([NET\_REQUEST\_WIFI\_PMKSA\_FLUSH](group__wifi__mgmt.md#ga9070995249eb35de37e2b60c4426f840));

288

[ 290](group__wifi__mgmt.md#gae5dc7835e11487187663dfe65a15f22b)#define NET\_REQUEST\_WIFI\_ENTERPRISE\_CREDS \

291 (NET\_WIFI\_BASE | NET\_REQUEST\_WIFI\_CMD\_ENTERPRISE\_CREDS)

292

293[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)([NET\_REQUEST\_WIFI\_ENTERPRISE\_CREDS](group__wifi__mgmt.md#gae5dc7835e11487187663dfe65a15f22b));

294

[ 296](group__wifi__mgmt.md#ga2678ea372335af008d9bd3333f7a7de1)#define NET\_REQUEST\_WIFI\_RTS\_THRESHOLD\_CONFIG \

297 (NET\_WIFI\_BASE | NET\_REQUEST\_WIFI\_CMD\_RTS\_THRESHOLD\_CONFIG)

298

299[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)([NET\_REQUEST\_WIFI\_RTS\_THRESHOLD\_CONFIG](group__wifi__mgmt.md#ga2678ea372335af008d9bd3333f7a7de1));

300

[ 301](group__wifi__mgmt.md#ga649a63bc7d315ebdd89464ff48b3fada)#define NET\_REQUEST\_WIFI\_WPS\_CONFIG (NET\_WIFI\_BASE | NET\_REQUEST\_WIFI\_CMD\_WPS\_CONFIG)

302

303[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)([NET\_REQUEST\_WIFI\_WPS\_CONFIG](group__wifi__mgmt.md#ga649a63bc7d315ebdd89464ff48b3fada));

304#ifdef CONFIG\_WIFI\_CREDENTIALS\_CONNECT\_STORED

305#define NET\_REQUEST\_WIFI\_CONNECT\_STORED (NET\_WIFI\_BASE | NET\_REQUEST\_WIFI\_CMD\_CONNECT\_STORED)

306

307[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_WIFI\_CONNECT\_STORED);

308#endif

309

[ 310](group__wifi__mgmt.md#ga89cc123bb5c30140d2ce0a8b741b1086)#define NET\_REQUEST\_WIFI\_START\_ROAMING \

311 (NET\_WIFI\_BASE | NET\_REQUEST\_WIFI\_CMD\_START\_ROAMING)

312

313[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)([NET\_REQUEST\_WIFI\_START\_ROAMING](group__wifi__mgmt.md#ga89cc123bb5c30140d2ce0a8b741b1086));

314

[ 315](group__wifi__mgmt.md#ga373031970a29331bf1b30d1654c128f0)#define NET\_REQUEST\_WIFI\_NEIGHBOR\_REP\_COMPLETE \

316 (NET\_WIFI\_BASE | NET\_REQUEST\_WIFI\_CMD\_NEIGHBOR\_REP\_COMPLETE)

317

318[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)([NET\_REQUEST\_WIFI\_NEIGHBOR\_REP\_COMPLETE](group__wifi__mgmt.md#ga373031970a29331bf1b30d1654c128f0));

319

321

322enum {

323 NET\_EVENT\_WIFI\_CMD\_SCAN\_RESULT\_VAL,

324 NET\_EVENT\_WIFI\_CMD\_SCAN\_DONE\_VAL,

325 NET\_EVENT\_WIFI\_CMD\_CONNECT\_RESULT\_VAL,

326 NET\_EVENT\_WIFI\_CMD\_DISCONNECT\_RESULT\_VAL,

327 NET\_EVENT\_WIFI\_CMD\_IFACE\_STATUS\_VAL,

328 NET\_EVENT\_WIFI\_CMD\_TWT\_VAL,

329 NET\_EVENT\_WIFI\_CMD\_TWT\_SLEEP\_STATE\_VAL,

330 NET\_EVENT\_WIFI\_CMD\_RAW\_SCAN\_RESULT\_VAL,

331 NET\_EVENT\_WIFI\_CMD\_DISCONNECT\_COMPLETE\_VAL,

332 NET\_EVENT\_WIFI\_CMD\_SIGNAL\_CHANGE\_VAL,

333 NET\_EVENT\_WIFI\_CMD\_NEIGHBOR\_REP\_RECEIVED\_VAL,

334 NET\_EVENT\_WIFI\_CMD\_NEIGHBOR\_REP\_COMPLETE\_VAL,

335 NET\_EVENT\_WIFI\_CMD\_AP\_ENABLE\_RESULT\_VAL,

336 NET\_EVENT\_WIFI\_CMD\_AP\_DISABLE\_RESULT\_VAL,

337 NET\_EVENT\_WIFI\_CMD\_AP\_STA\_CONNECTED\_VAL,

338 NET\_EVENT\_WIFI\_CMD\_AP\_STA\_DISCONNECTED\_VAL,

339 NET\_EVENT\_WIFI\_CMD\_SUPPLICANT\_VAL,

340

341 NET\_EVENT\_WIFI\_CMD\_MAX,

342};

343

344BUILD\_ASSERT(NET\_EVENT\_WIFI\_CMD\_MAX <= NET\_MGMT\_MAX\_COMMANDS,

345 "Number of events in net\_event\_wifi\_cmd exceeds the limit");

346

348

[ 350](group__wifi__mgmt.md#gac2638308cbb0d268831f1618cf8e1fa8)enum [net\_event\_wifi\_cmd](group__wifi__mgmt.md#gac2638308cbb0d268831f1618cf8e1fa8) {

[ 352](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8ae731884669e9ee832e36b8280e9c58c6) [NET\_MGMT\_CMD](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8ae731884669e9ee832e36b8280e9c58c6)(NET\_EVENT\_WIFI\_CMD\_SCAN\_RESULT),

354 [NET\_MGMT\_CMD](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8ae731884669e9ee832e36b8280e9c58c6)(NET\_EVENT\_WIFI\_CMD\_SCAN\_DONE),

356 [NET\_MGMT\_CMD](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8ae731884669e9ee832e36b8280e9c58c6)(NET\_EVENT\_WIFI\_CMD\_CONNECT\_RESULT),

358 [NET\_MGMT\_CMD](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8ae731884669e9ee832e36b8280e9c58c6)(NET\_EVENT\_WIFI\_CMD\_DISCONNECT\_RESULT),

360 [NET\_MGMT\_CMD](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8ae731884669e9ee832e36b8280e9c58c6)(NET\_EVENT\_WIFI\_CMD\_IFACE\_STATUS),

362 [NET\_MGMT\_CMD](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8ae731884669e9ee832e36b8280e9c58c6)(NET\_EVENT\_WIFI\_CMD\_TWT),

366 [NET\_MGMT\_CMD](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8ae731884669e9ee832e36b8280e9c58c6)(NET\_EVENT\_WIFI\_CMD\_TWT\_SLEEP\_STATE),

368 [NET\_MGMT\_CMD](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8ae731884669e9ee832e36b8280e9c58c6)(NET\_EVENT\_WIFI\_CMD\_RAW\_SCAN\_RESULT),

370 [NET\_MGMT\_CMD](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8ae731884669e9ee832e36b8280e9c58c6)(NET\_EVENT\_WIFI\_CMD\_DISCONNECT\_COMPLETE),

372 [NET\_MGMT\_CMD](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8ae731884669e9ee832e36b8280e9c58c6)(NET\_EVENT\_WIFI\_CMD\_SIGNAL\_CHANGE),

374 [NET\_MGMT\_CMD](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8ae731884669e9ee832e36b8280e9c58c6)(NET\_EVENT\_WIFI\_CMD\_NEIGHBOR\_REP\_RECEIVED),

376 [NET\_MGMT\_CMD](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8ae731884669e9ee832e36b8280e9c58c6)(NET\_EVENT\_WIFI\_CMD\_NEIGHBOR\_REP\_COMPLETE),

378 [NET\_MGMT\_CMD](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8ae731884669e9ee832e36b8280e9c58c6)(NET\_EVENT\_WIFI\_CMD\_AP\_ENABLE\_RESULT),

380 [NET\_MGMT\_CMD](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8ae731884669e9ee832e36b8280e9c58c6)(NET\_EVENT\_WIFI\_CMD\_AP\_DISABLE\_RESULT),

382 [NET\_MGMT\_CMD](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8ae731884669e9ee832e36b8280e9c58c6)(NET\_EVENT\_WIFI\_CMD\_AP\_STA\_CONNECTED),

384 [NET\_MGMT\_CMD](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8ae731884669e9ee832e36b8280e9c58c6)(NET\_EVENT\_WIFI\_CMD\_AP\_STA\_DISCONNECTED),

386 [NET\_MGMT\_CMD](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8ae731884669e9ee832e36b8280e9c58c6)(NET\_EVENT\_WIFI\_CMD\_SUPPLICANT),

387};

388

[ 390](group__wifi__mgmt.md#ga436a927d47eb9abe683b89f2b128cd6e)#define NET\_EVENT\_WIFI\_SCAN\_RESULT \

391 (NET\_WIFI\_EVENT | NET\_EVENT\_WIFI\_CMD\_SCAN\_RESULT)

392

[ 394](group__wifi__mgmt.md#ga8ce35a12e5338e9a65970382b4a26b88)#define NET\_EVENT\_WIFI\_SCAN\_DONE \

395 (NET\_WIFI\_EVENT | NET\_EVENT\_WIFI\_CMD\_SCAN\_DONE)

396

[ 398](group__wifi__mgmt.md#ga0e8feafcc5efd85d04be91f407c0b7c4)#define NET\_EVENT\_WIFI\_CONNECT\_RESULT \

399 (NET\_WIFI\_EVENT | NET\_EVENT\_WIFI\_CMD\_CONNECT\_RESULT)

400

[ 402](group__wifi__mgmt.md#ga8cbbe69bd60f42fdbb06f4f1e15410c8)#define NET\_EVENT\_WIFI\_DISCONNECT\_RESULT \

403 (NET\_WIFI\_EVENT | NET\_EVENT\_WIFI\_CMD\_DISCONNECT\_RESULT)

404

[ 406](group__wifi__mgmt.md#ga99e11fc15582b94d4243de7733e47ebb)#define NET\_EVENT\_WIFI\_IFACE\_STATUS \

407 (NET\_WIFI\_EVENT | NET\_EVENT\_WIFI\_CMD\_IFACE\_STATUS)

408

[ 410](group__wifi__mgmt.md#gaeb968a5d2a8d68a8c634cca18dbcf9c6)#define NET\_EVENT\_WIFI\_TWT \

411 (NET\_WIFI\_EVENT | NET\_EVENT\_WIFI\_CMD\_TWT)

412

[ 414](group__wifi__mgmt.md#ga682d95b5d06a9b175c10d712acca8a49)#define NET\_EVENT\_WIFI\_TWT\_SLEEP\_STATE \

415 (NET\_WIFI\_EVENT | NET\_EVENT\_WIFI\_CMD\_TWT\_SLEEP\_STATE)

416

[ 418](group__wifi__mgmt.md#gaea8d222282ddef6992330763afc759a4)#define NET\_EVENT\_WIFI\_RAW\_SCAN\_RESULT \

419 (NET\_WIFI\_EVENT | NET\_EVENT\_WIFI\_CMD\_RAW\_SCAN\_RESULT)

420

[ 422](group__wifi__mgmt.md#ga40027feb7ec42c846fd99b56bbd2256d)#define NET\_EVENT\_WIFI\_DISCONNECT\_COMPLETE \

423 (NET\_WIFI\_EVENT | NET\_EVENT\_WIFI\_CMD\_DISCONNECT\_COMPLETE)

424

[ 426](group__wifi__mgmt.md#ga8da47e9d3e594840fb7a7d59f45ea9ce)#define NET\_EVENT\_WIFI\_SIGNAL\_CHANGE \

427 (NET\_WIFI\_EVENT | NET\_EVENT\_WIFI\_CMD\_SIGNAL\_CHANGE)

428

[ 430](group__wifi__mgmt.md#ga7ed4bc9f25055f5a35270a4c6a0bedcc)#define NET\_EVENT\_WIFI\_NEIGHBOR\_REP\_COMP \

431 (NET\_WIFI\_EVENT | NET\_EVENT\_WIFI\_CMD\_NEIGHBOR\_REP\_COMPLETE)

432

[ 434](group__wifi__mgmt.md#ga1d678fbae0f092814392c0ab4087cb73)#define NET\_EVENT\_WIFI\_AP\_ENABLE\_RESULT \

435 (NET\_WIFI\_EVENT | NET\_EVENT\_WIFI\_CMD\_AP\_ENABLE\_RESULT)

436

[ 438](group__wifi__mgmt.md#ga104296fdb38edf868bea1a46f572d101)#define NET\_EVENT\_WIFI\_AP\_DISABLE\_RESULT \

439 (NET\_WIFI\_EVENT | NET\_EVENT\_WIFI\_CMD\_AP\_DISABLE\_RESULT)

440

[ 442](group__wifi__mgmt.md#gacc392179948bfd5bed6702dc8fb5cd9d)#define NET\_EVENT\_WIFI\_AP\_STA\_CONNECTED \

443 (NET\_WIFI\_EVENT | NET\_EVENT\_WIFI\_CMD\_AP\_STA\_CONNECTED)

444

[ 446](group__wifi__mgmt.md#ga3e8154ce1808665dd165f793ddec1673)#define NET\_EVENT\_WIFI\_AP\_STA\_DISCONNECTED \

447 (NET\_WIFI\_EVENT | NET\_EVENT\_WIFI\_CMD\_AP\_STA\_DISCONNECTED)

448

[ 450](structwifi__version.md)struct [wifi\_version](structwifi__version.md) {

[ 452](structwifi__version.md#aea828bdb512440d6aa3cc853525c4971) const char \*[drv\_version](structwifi__version.md#aea828bdb512440d6aa3cc853525c4971);

[ 454](structwifi__version.md#a4bf2cbdf5c43ff21718ccf19646c164e) const char \*[fw\_version](structwifi__version.md#a4bf2cbdf5c43ff21718ccf19646c164e);

455};

456

[ 460](structwifi__band__channel.md)struct [wifi\_band\_channel](structwifi__band__channel.md) {

[ 462](structwifi__band__channel.md#a4a932599429f37231f76c3064ec5efb3) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [band](structwifi__band__channel.md#a4a932599429f37231f76c3064ec5efb3);

[ 464](structwifi__band__channel.md#acd0dd7366de3650124dad7232a58ade0) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [channel](structwifi__band__channel.md#acd0dd7366de3650124dad7232a58ade0);

465};

466

[ 472](structwifi__scan__params.md)struct [wifi\_scan\_params](structwifi__scan__params.md) {

[ 480](structwifi__scan__params.md#a645acc54603cd4692527c1a028933078) enum [wifi\_scan\_type](group__wifi__mgmt.md#gad30e29eda65ccafdbd7f11865937b8ea) [scan\_type](structwifi__scan__params.md#a645acc54603cd4692527c1a028933078);

[ 484](structwifi__scan__params.md#a6b571d960ed9d7419e31530e5fb6f97a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bands](structwifi__scan__params.md#a6b571d960ed9d7419e31530e5fb6f97a);

[ 487](structwifi__scan__params.md#a2453a75c23e04e3572559c0e7199c1b4) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [dwell\_time\_active](structwifi__scan__params.md#a2453a75c23e04e3572559c0e7199c1b4);

[ 490](structwifi__scan__params.md#a8e7a37ccda8de635e7b7066d7943e814) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [dwell\_time\_passive](structwifi__scan__params.md#a8e7a37ccda8de635e7b7066d7943e814);

[ 493](structwifi__scan__params.md#aac11ee8e0ec8a4fa24668f4820bd1a12) const char \*[ssids](structwifi__scan__params.md#aac11ee8e0ec8a4fa24668f4820bd1a12)[WIFI\_MGMT\_SCAN\_SSID\_FILT\_MAX];

[ 501](structwifi__scan__params.md#a12d5dea7d8fa8ad03ac2366720c46243) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [max\_bss\_cnt](structwifi__scan__params.md#a12d5dea7d8fa8ad03ac2366720c46243);

[ 516](structwifi__scan__params.md#aa5ddbd6bc97b7598288d4b0d38521681) struct [wifi\_band\_channel](structwifi__band__channel.md) [band\_chan](structwifi__scan__params.md#aa5ddbd6bc97b7598288d4b0d38521681)[WIFI\_MGMT\_SCAN\_CHAN\_MAX\_MANUAL];

517};

518

[ 522](structwifi__scan__result.md)struct [wifi\_scan\_result](structwifi__scan__result.md) {

[ 524](structwifi__scan__result.md#aaefb8f5c9510e4f5002ae306d853ade8) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [ssid](structwifi__scan__result.md#aaefb8f5c9510e4f5002ae306d853ade8)[[WIFI\_SSID\_MAX\_LEN](group__wifi__mgmt.md#gad62c60666c9fdffe2e0e9c4388f87886) + 1];

[ 526](structwifi__scan__result.md#a2c1c2f4265b914df08fc75deb8b69d39) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [ssid\_length](structwifi__scan__result.md#a2c1c2f4265b914df08fc75deb8b69d39);

[ 528](structwifi__scan__result.md#a38201c9dd798dc11b5bda3ce97b02e92) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [band](structwifi__scan__result.md#a38201c9dd798dc11b5bda3ce97b02e92);

[ 530](structwifi__scan__result.md#adbbfd7692ee5ffd6344fe78b9d91c840) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [channel](structwifi__scan__result.md#adbbfd7692ee5ffd6344fe78b9d91c840);

[ 532](structwifi__scan__result.md#af2d3dc5d115e3db76d3bc115510b0a5a) enum [wifi\_security\_type](group__wifi__mgmt.md#gadde31a04fa25ed805115c6b31854cd9c) [security](structwifi__scan__result.md#af2d3dc5d115e3db76d3bc115510b0a5a);

[ 534](structwifi__scan__result.md#abb7de47c605ec05c8fe0a06ecbd2b7b6) enum [wifi\_wpa3\_enterprise\_type](group__wifi__mgmt.md#ga48fea1f0c7d2700cef47068f96c6b71a) [wpa3\_ent\_type](structwifi__scan__result.md#abb7de47c605ec05c8fe0a06ecbd2b7b6);

[ 536](structwifi__scan__result.md#acaa3fb30ebf6df22bfac6380698ed28e) enum [wifi\_mfp\_options](group__wifi__mgmt.md#ga1f252da47d9650023d7fff6d08e49c76) [mfp](structwifi__scan__result.md#acaa3fb30ebf6df22bfac6380698ed28e);

[ 538](structwifi__scan__result.md#a76aa012136e3721fd4a482a22b93546f) [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) [rssi](structwifi__scan__result.md#a76aa012136e3721fd4a482a22b93546f);

[ 540](structwifi__scan__result.md#a4fdbc4dc4d5c8b279223e8c06624f434) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [mac](structwifi__scan__result.md#a4fdbc4dc4d5c8b279223e8c06624f434)[[WIFI\_MAC\_ADDR\_LEN](group__wifi__mgmt.md#ga29409ff83a53c6464decdde9bdd04de6)];

[ 542](structwifi__scan__result.md#a8fca0dabec00ebd7ed4800098ec9d451) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [mac\_length](structwifi__scan__result.md#a8fca0dabec00ebd7ed4800098ec9d451);

543};

544

[ 546](structwifi__connect__req__params.md)struct [wifi\_connect\_req\_params](structwifi__connect__req__params.md) {

[ 548](structwifi__connect__req__params.md#ac260c2cd17a3f36ea101edaf23d41083) const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[ssid](structwifi__connect__req__params.md#ac260c2cd17a3f36ea101edaf23d41083);

[ 550](structwifi__connect__req__params.md#a547dddf6be5dd77eda74b1085a798400) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [ssid\_length](structwifi__connect__req__params.md#a547dddf6be5dd77eda74b1085a798400); /\* Max 32 \*/

[ 552](structwifi__connect__req__params.md#aa7743f0ecbc27a9595720ce13ce57c1d) const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[psk](structwifi__connect__req__params.md#aa7743f0ecbc27a9595720ce13ce57c1d);

[ 554](structwifi__connect__req__params.md#aaf7455a65590d19f047214b459a2dcb9) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [psk\_length](structwifi__connect__req__params.md#aaf7455a65590d19f047214b459a2dcb9); /\* Min 8 - Max 64 \*/

[ 556](structwifi__connect__req__params.md#a469fac5758b78fc425911837930b2060) const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[sae\_password](structwifi__connect__req__params.md#a469fac5758b78fc425911837930b2060);

[ 558](structwifi__connect__req__params.md#a74f0819e7a546ffb8bfb0ec587eccf20) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [sae\_password\_length](structwifi__connect__req__params.md#a74f0819e7a546ffb8bfb0ec587eccf20); /\* No length restrictions \*/

[ 560](structwifi__connect__req__params.md#aa2fea1881a8ffdf5d7093ae295867f3e) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [band](structwifi__connect__req__params.md#aa2fea1881a8ffdf5d7093ae295867f3e);

[ 562](structwifi__connect__req__params.md#a52b6d0323c35d03ec239f40be35cae72) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [channel](structwifi__connect__req__params.md#a52b6d0323c35d03ec239f40be35cae72);

[ 564](structwifi__connect__req__params.md#a18dce6bb021086877a30e7a04f5b24b9) enum [wifi\_security\_type](group__wifi__mgmt.md#gadde31a04fa25ed805115c6b31854cd9c) [security](structwifi__connect__req__params.md#a18dce6bb021086877a30e7a04f5b24b9);

[ 566](structwifi__connect__req__params.md#a745b3416172672a7e5b12bcc5b55e88c) enum [wifi\_mfp\_options](group__wifi__mgmt.md#ga1f252da47d9650023d7fff6d08e49c76) [mfp](structwifi__connect__req__params.md#a745b3416172672a7e5b12bcc5b55e88c);

[ 568](structwifi__connect__req__params.md#aa8081b9075ff9244cefd0ac1ef3f42cb) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bssid](structwifi__connect__req__params.md#aa8081b9075ff9244cefd0ac1ef3f42cb)[[WIFI\_MAC\_ADDR\_LEN](group__wifi__mgmt.md#ga29409ff83a53c6464decdde9bdd04de6)];

[ 570](structwifi__connect__req__params.md#a56183ba7f4d8eaf5fc5b495856adecfd) int [timeout](structwifi__connect__req__params.md#a56183ba7f4d8eaf5fc5b495856adecfd);

[ 572](structwifi__connect__req__params.md#a781456e079357e2e1096218af3bd218c) const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[anon\_id](structwifi__connect__req__params.md#a781456e079357e2e1096218af3bd218c);

[ 574](structwifi__connect__req__params.md#a2892253024b70e5cb8eb2166b17ebe22) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [aid\_length](structwifi__connect__req__params.md#a2892253024b70e5cb8eb2166b17ebe22);

[ 576](structwifi__connect__req__params.md#a4946647659a347667ee49bb6990bba66) const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[key\_passwd](structwifi__connect__req__params.md#a4946647659a347667ee49bb6990bba66);

[ 578](structwifi__connect__req__params.md#a9f913fc0ccecafaba488e444d701fd68) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [key\_passwd\_length](structwifi__connect__req__params.md#a9f913fc0ccecafaba488e444d701fd68);

[ 580](structwifi__connect__req__params.md#a020fc58d7e5350cc803cd5d6fa575e6a) const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[key2\_passwd](structwifi__connect__req__params.md#a020fc58d7e5350cc803cd5d6fa575e6a);

[ 582](structwifi__connect__req__params.md#af7b163cc2bffc59f7fa31f47c5e52062) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [key2\_passwd\_length](structwifi__connect__req__params.md#af7b163cc2bffc59f7fa31f47c5e52062);

[ 584](structwifi__connect__req__params.md#ae0b94d870ecbee0b203caee6a6e3d8b2) enum [wifi\_wpa3\_enterprise\_type](group__wifi__mgmt.md#ga48fea1f0c7d2700cef47068f96c6b71a) [wpa3\_ent\_mode](structwifi__connect__req__params.md#ae0b94d870ecbee0b203caee6a6e3d8b2);

[ 586](structwifi__connect__req__params.md#aa4577535a27b8d54d9b8c7543d359ade) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [TLS\_cipher](structwifi__connect__req__params.md#aa4577535a27b8d54d9b8c7543d359ade);

[ 588](structwifi__connect__req__params.md#a8c8ecb1ef0fe3f2f4c04a7a8eeccbbdf) int [eap\_ver](structwifi__connect__req__params.md#a8c8ecb1ef0fe3f2f4c04a7a8eeccbbdf);

[ 590](structwifi__connect__req__params.md#ab9c65599409387af65a3c2895c3116da) const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[eap\_identity](structwifi__connect__req__params.md#ab9c65599409387af65a3c2895c3116da);

[ 592](structwifi__connect__req__params.md#a4da02ff112c09f55dc5bddcda27d16a3) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [eap\_id\_length](structwifi__connect__req__params.md#a4da02ff112c09f55dc5bddcda27d16a3);

[ 594](structwifi__connect__req__params.md#afd046e702739c4a0d89322ee41b37acd) const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[eap\_password](structwifi__connect__req__params.md#afd046e702739c4a0d89322ee41b37acd);

[ 596](structwifi__connect__req__params.md#aeab22e95a04a1831b87beda1772d3db7) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [eap\_passwd\_length](structwifi__connect__req__params.md#aeab22e95a04a1831b87beda1772d3db7);

[ 598](structwifi__connect__req__params.md#aa8f18ace96e471eb0bc8bff8d8146f6f) bool [verify\_peer\_cert](structwifi__connect__req__params.md#aa8f18ace96e471eb0bc8bff8d8146f6f);

[ 600](structwifi__connect__req__params.md#a047b11e703fb646d778785dfcb14257b) bool [ft\_used](structwifi__connect__req__params.md#a047b11e703fb646d778785dfcb14257b);

[ 602](structwifi__connect__req__params.md#a71770c2f2da378db2efedaa87b141627) int [nusers](structwifi__connect__req__params.md#a71770c2f2da378db2efedaa87b141627);

[ 604](structwifi__connect__req__params.md#aaf071a51c7281e4d42197f266c729c04) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [passwds](structwifi__connect__req__params.md#aaf071a51c7281e4d42197f266c729c04);

[ 606](structwifi__connect__req__params.md#a265001d2309840d04bdca507896255d0) const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[identities](structwifi__connect__req__params.md#a265001d2309840d04bdca507896255d0)[WIFI\_ENT\_IDENTITY\_MAX\_USERS];

[ 608](structwifi__connect__req__params.md#a2163b50b6d466663404e1cb21ce6ae5d) const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[passwords](structwifi__connect__req__params.md#a2163b50b6d466663404e1cb21ce6ae5d)[WIFI\_ENT\_IDENTITY\_MAX\_USERS];

[ 614](structwifi__connect__req__params.md#afac70366e509301f9a27ca51be30b88d) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [ignore\_broadcast\_ssid](structwifi__connect__req__params.md#afac70366e509301f9a27ca51be30b88d);

[ 616](structwifi__connect__req__params.md#a0d44c86d9b9528041bbe7534e0c7597a) enum [wifi\_frequency\_bandwidths](group__wifi__mgmt.md#ga3b01cead3c2eb4581fe85e2aaaffbd49) [bandwidth](structwifi__connect__req__params.md#a0d44c86d9b9528041bbe7534e0c7597a);

617};

618

[ 622](group__wifi__mgmt.md#gac782af0a60b202fd19597cabb7bd3a9a)enum [wifi\_disconn\_reason](group__wifi__mgmt.md#gac782af0a60b202fd19597cabb7bd3a9a) {

[ 624](group__wifi__mgmt.md#ggac782af0a60b202fd19597cabb7bd3a9aa5c894399db8949a789ca4f5750b6f042) [WIFI\_REASON\_DISCONN\_SUCCESS](group__wifi__mgmt.md#ggac782af0a60b202fd19597cabb7bd3a9aa5c894399db8949a789ca4f5750b6f042) = 0,

[ 626](group__wifi__mgmt.md#ggac782af0a60b202fd19597cabb7bd3a9aa87f5d64a9fd3acf8d67c698199779e5c) [WIFI\_REASON\_DISCONN\_UNSPECIFIED](group__wifi__mgmt.md#ggac782af0a60b202fd19597cabb7bd3a9aa87f5d64a9fd3acf8d67c698199779e5c),

[ 628](group__wifi__mgmt.md#ggac782af0a60b202fd19597cabb7bd3a9aaee75adafb52bd6ecaa547a76c6ccd0a7) [WIFI\_REASON\_DISCONN\_USER\_REQUEST](group__wifi__mgmt.md#ggac782af0a60b202fd19597cabb7bd3a9aaee75adafb52bd6ecaa547a76c6ccd0a7),

[ 630](group__wifi__mgmt.md#ggac782af0a60b202fd19597cabb7bd3a9aa34e3f78ce43db3daeaf32038e0baf204) [WIFI\_REASON\_DISCONN\_AP\_LEAVING](group__wifi__mgmt.md#ggac782af0a60b202fd19597cabb7bd3a9aa34e3f78ce43db3daeaf32038e0baf204),

[ 632](group__wifi__mgmt.md#ggac782af0a60b202fd19597cabb7bd3a9aa05fe2f87de30de47ee48f7615c2206e6) [WIFI\_REASON\_DISCONN\_INACTIVITY](group__wifi__mgmt.md#ggac782af0a60b202fd19597cabb7bd3a9aa05fe2f87de30de47ee48f7615c2206e6),

633};

634

[ 638](group__wifi__mgmt.md#gaaf730bf76adc06434c7ac63bf0417884)enum [wifi\_ap\_status](group__wifi__mgmt.md#gaaf730bf76adc06434c7ac63bf0417884) {

[ 640](group__wifi__mgmt.md#ggaaf730bf76adc06434c7ac63bf0417884a0df52848da8735892d0eb1e381b2cd7c) [WIFI\_STATUS\_AP\_SUCCESS](group__wifi__mgmt.md#ggaaf730bf76adc06434c7ac63bf0417884a0df52848da8735892d0eb1e381b2cd7c) = 0,

[ 642](group__wifi__mgmt.md#ggaaf730bf76adc06434c7ac63bf0417884a6c6801381caa3862004662169202fa9a) [WIFI\_STATUS\_AP\_FAIL](group__wifi__mgmt.md#ggaaf730bf76adc06434c7ac63bf0417884a6c6801381caa3862004662169202fa9a),

[ 644](group__wifi__mgmt.md#ggaaf730bf76adc06434c7ac63bf0417884a5acb85a2361ca72ed10966b829c5753b) [WIFI\_STATUS\_AP\_CHANNEL\_NOT\_SUPPORTED](group__wifi__mgmt.md#ggaaf730bf76adc06434c7ac63bf0417884a5acb85a2361ca72ed10966b829c5753b),

[ 646](group__wifi__mgmt.md#ggaaf730bf76adc06434c7ac63bf0417884a0b1cb592c54c16e8a54defee71c5fd15) [WIFI\_STATUS\_AP\_CHANNEL\_NOT\_ALLOWED](group__wifi__mgmt.md#ggaaf730bf76adc06434c7ac63bf0417884a0b1cb592c54c16e8a54defee71c5fd15),

[ 648](group__wifi__mgmt.md#ggaaf730bf76adc06434c7ac63bf0417884ac18a7b551f8c6bb7737b0e8e60c323ce) [WIFI\_STATUS\_AP\_SSID\_NOT\_ALLOWED](group__wifi__mgmt.md#ggaaf730bf76adc06434c7ac63bf0417884ac18a7b551f8c6bb7737b0e8e60c323ce),

[ 650](group__wifi__mgmt.md#ggaaf730bf76adc06434c7ac63bf0417884abe5a626d22051522255d98fdfdfbfcc8) [WIFI\_STATUS\_AP\_AUTH\_TYPE\_NOT\_SUPPORTED](group__wifi__mgmt.md#ggaaf730bf76adc06434c7ac63bf0417884abe5a626d22051522255d98fdfdfbfcc8),

[ 652](group__wifi__mgmt.md#ggaaf730bf76adc06434c7ac63bf0417884a2105e6c49b3bcb5f7dcacbc1e5ce9cca) [WIFI\_STATUS\_AP\_OP\_NOT\_SUPPORTED](group__wifi__mgmt.md#ggaaf730bf76adc06434c7ac63bf0417884a2105e6c49b3bcb5f7dcacbc1e5ce9cca),

[ 654](group__wifi__mgmt.md#ggaaf730bf76adc06434c7ac63bf0417884a36a58980bdc7877c910441590137ddbe) [WIFI\_STATUS\_AP\_OP\_NOT\_PERMITTED](group__wifi__mgmt.md#ggaaf730bf76adc06434c7ac63bf0417884a36a58980bdc7877c910441590137ddbe),

655};

656

[ 658](structwifi__status.md)struct [wifi\_status](structwifi__status.md) {

659 union {

[ 661](structwifi__status.md#aa1dbff8154400f8353693d387977008b) int [status](structwifi__status.md#aa1dbff8154400f8353693d387977008b);

[ 663](structwifi__status.md#a8f885e78366d0499e4ba8e15bef275ac) enum [wifi\_conn\_status](group__wifi__mgmt.md#ga86a5741e54aeb3e290142b0de217b8a8) [conn\_status](structwifi__status.md#a8f885e78366d0499e4ba8e15bef275ac);

[ 665](structwifi__status.md#aa04b5033d93274badd27f702af9830bc) enum [wifi\_disconn\_reason](group__wifi__mgmt.md#gac782af0a60b202fd19597cabb7bd3a9a) [disconn\_reason](structwifi__status.md#aa04b5033d93274badd27f702af9830bc);

[ 667](structwifi__status.md#a02f0fcc7ef57661ca95d0c99f045aef1) enum [wifi\_ap\_status](group__wifi__mgmt.md#gaaf730bf76adc06434c7ac63bf0417884) [ap\_status](structwifi__status.md#a02f0fcc7ef57661ca95d0c99f045aef1);

668 };

669};

670

[ 672](structwifi__iface__status.md)struct [wifi\_iface\_status](structwifi__iface__status.md) {

[ 674](structwifi__iface__status.md#ac52806155be3d64954ac6d109e76ec57) int [state](structwifi__iface__status.md#ac52806155be3d64954ac6d109e76ec57);

[ 676](structwifi__iface__status.md#ad82f281941e4f6ce1ef0bca008e26d41) unsigned int [ssid\_len](structwifi__iface__status.md#ad82f281941e4f6ce1ef0bca008e26d41);

[ 678](structwifi__iface__status.md#a3ab671471bcdfeb5b955d156d39f2bb3) char [ssid](structwifi__iface__status.md#a3ab671471bcdfeb5b955d156d39f2bb3)[[WIFI\_SSID\_MAX\_LEN](group__wifi__mgmt.md#gad62c60666c9fdffe2e0e9c4388f87886) + 1];

[ 680](structwifi__iface__status.md#a5d5d19056a1a15365fbdd94274a0fc5e) char [bssid](structwifi__iface__status.md#a5d5d19056a1a15365fbdd94274a0fc5e)[[WIFI\_MAC\_ADDR\_LEN](group__wifi__mgmt.md#ga29409ff83a53c6464decdde9bdd04de6)];

[ 682](structwifi__iface__status.md#ae1c141a18f4e225af2c22a8cb4f882a8) enum [wifi\_frequency\_bands](group__wifi__mgmt.md#ga1e2f0439a322355fa7368ea880c9c15d) [band](structwifi__iface__status.md#ae1c141a18f4e225af2c22a8cb4f882a8);

[ 684](structwifi__iface__status.md#a6432663156e5b2c424d254ed1eae0144) unsigned int [channel](structwifi__iface__status.md#a6432663156e5b2c424d254ed1eae0144);

[ 686](structwifi__iface__status.md#ad33d2ec149a8d556e2472dd842ceadc0) enum [wifi\_iface\_mode](group__wifi__mgmt.md#ga584f6239ac14e2bedc5e6bd72756423b) [iface\_mode](structwifi__iface__status.md#ad33d2ec149a8d556e2472dd842ceadc0);

[ 688](structwifi__iface__status.md#ae2de076d79f2172793d65fe9cd31edc4) enum [wifi\_link\_mode](group__wifi__mgmt.md#gabdb2a784d4727b71ab44cca04e422c62) [link\_mode](structwifi__iface__status.md#ae2de076d79f2172793d65fe9cd31edc4);

[ 690](structwifi__iface__status.md#a361c0e8a385fdc21f16258c25c2bc8d1) enum [wifi\_wpa3\_enterprise\_type](group__wifi__mgmt.md#ga48fea1f0c7d2700cef47068f96c6b71a) [wpa3\_ent\_type](structwifi__iface__status.md#a361c0e8a385fdc21f16258c25c2bc8d1);

[ 692](structwifi__iface__status.md#a625ecec1abec8dd65cf155eab21a01b5) enum [wifi\_security\_type](group__wifi__mgmt.md#gadde31a04fa25ed805115c6b31854cd9c) [security](structwifi__iface__status.md#a625ecec1abec8dd65cf155eab21a01b5);

[ 694](structwifi__iface__status.md#aa1a9b644fd355526125ddd32416b7c24) enum [wifi\_mfp\_options](group__wifi__mgmt.md#ga1f252da47d9650023d7fff6d08e49c76) [mfp](structwifi__iface__status.md#aa1a9b644fd355526125ddd32416b7c24);

[ 696](structwifi__iface__status.md#a4e593147b88eb4938d55a4de72fcc7f6) int [rssi](structwifi__iface__status.md#a4e593147b88eb4938d55a4de72fcc7f6);

[ 698](structwifi__iface__status.md#aae6c8cbaa16c81d308f08114d5103a3d) unsigned char [dtim\_period](structwifi__iface__status.md#aae6c8cbaa16c81d308f08114d5103a3d);

[ 700](structwifi__iface__status.md#a241bfbe70628006b515b5f9e4f97665c) unsigned short [beacon\_interval](structwifi__iface__status.md#a241bfbe70628006b515b5f9e4f97665c);

[ 702](structwifi__iface__status.md#acfde8d64b463a9f553aa4fb689dc1917) bool [twt\_capable](structwifi__iface__status.md#acfde8d64b463a9f553aa4fb689dc1917);

[ 704](structwifi__iface__status.md#af255c63862e0c9e5008b2e4952d7e491) int [current\_phy\_tx\_rate](structwifi__iface__status.md#af255c63862e0c9e5008b2e4952d7e491);

705};

706

[ 708](structwifi__ps__params.md)struct [wifi\_ps\_params](structwifi__ps__params.md) {

[ 710](structwifi__ps__params.md#abb22aaa45833ac130922204bd2fe841b) enum [wifi\_ps](group__wifi__mgmt.md#ga0fffeb57b68fb8cdef9d3d571368b8ca) [enabled](structwifi__ps__params.md#abb22aaa45833ac130922204bd2fe841b);

[ 712](structwifi__ps__params.md#a8510c799ab0c5825f1c6349f9799c62f) unsigned short [listen\_interval](structwifi__ps__params.md#a8510c799ab0c5825f1c6349f9799c62f);

[ 714](structwifi__ps__params.md#a7cb3e7fb7d9f8bd7c2cab41f879b3b66) enum [wifi\_ps\_wakeup\_mode](group__wifi__mgmt.md#gac7f907644847e905d67c709fa4afae7f) [wakeup\_mode](structwifi__ps__params.md#a7cb3e7fb7d9f8bd7c2cab41f879b3b66);

[ 716](structwifi__ps__params.md#a5a022d89d43ecf2cd1f15fc72c0f2bed) enum [wifi\_ps\_mode](group__wifi__mgmt.md#gaffae7d2a754be5eb952ad2b83edad54c) [mode](structwifi__ps__params.md#a5a022d89d43ecf2cd1f15fc72c0f2bed);

[ 725](structwifi__ps__params.md#ad963f1bf78dc271f08b73f3aadb36a91) unsigned int [timeout\_ms](structwifi__ps__params.md#ad963f1bf78dc271f08b73f3aadb36a91);

[ 727](structwifi__ps__params.md#aef62e5bf6216bf4dc461efe71735c4bd) enum [wifi\_ps\_param\_type](group__wifi__mgmt.md#gabe45d132797047c098041331c8f6f912) [type](structwifi__ps__params.md#aef62e5bf6216bf4dc461efe71735c4bd);

[ 729](structwifi__ps__params.md#a63fa2ee03bc4aefada61c298ee14336c) enum [wifi\_config\_ps\_param\_fail\_reason](group__wifi__mgmt.md#gad98099584d2222ede93aba42b1fbaff0) [fail\_reason](structwifi__ps__params.md#a63fa2ee03bc4aefada61c298ee14336c);

[ 731](structwifi__ps__params.md#ab9fc62dd1e2928320274fa1554a550a6) enum [wifi\_ps\_exit\_strategy](group__wifi__mgmt.md#ga2d424d1711389fb784e916a87ff854b7) [exit\_strategy](structwifi__ps__params.md#ab9fc62dd1e2928320274fa1554a550a6);

732};

733

[ 734](group__wifi__mgmt.md#ga38d92ba342887e46c957b820d89a7a20)#define WIFI\_BTWT\_AGREEMENT\_MAX 5

735

[ 737](structwifi__btwt__params.md)struct [wifi\_btwt\_params](structwifi__btwt__params.md) {

[ 739](structwifi__btwt__params.md#ae52281d9f53e106fb9ed813131d8085e) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [btwt\_id](structwifi__btwt__params.md#ae52281d9f53e106fb9ed813131d8085e);

[ 741](structwifi__btwt__params.md#a2c1b3551a714fbf1b948ce4bcf805934) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [btwt\_mantissa](structwifi__btwt__params.md#a2c1b3551a714fbf1b948ce4bcf805934);

[ 743](structwifi__btwt__params.md#a76c97bcc132405d6a1a54bcca77054ac) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [btwt\_exponent](structwifi__btwt__params.md#a76c97bcc132405d6a1a54bcca77054ac);

[ 745](structwifi__btwt__params.md#a0192d3a9334fc55a135206e6b74ea5b5) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [btwt\_nominal\_wake](structwifi__btwt__params.md#a0192d3a9334fc55a135206e6b74ea5b5);

746};

747

[ 749](structwifi__twt__params.md)struct [wifi\_twt\_params](structwifi__twt__params.md) {

[ 751](structwifi__twt__params.md#a6f0483861a387651c9c89ba182e064bd) enum [wifi\_twt\_operation](group__wifi__mgmt.md#gad0e998aeb1b27c4f203ca76339d323a3) [operation](structwifi__twt__params.md#a6f0483861a387651c9c89ba182e064bd);

[ 753](structwifi__twt__params.md#a5fd269328f68838b8a7e3a0b93eed894) enum [wifi\_twt\_negotiation\_type](group__wifi__mgmt.md#ga695123cd534e2499f516a07fdc5cafa8) [negotiation\_type](structwifi__twt__params.md#a5fd269328f68838b8a7e3a0b93eed894);

[ 755](structwifi__twt__params.md#a347f8cff73ee6b6ba6d15ddf6f376a2d) enum [wifi\_twt\_setup\_cmd](group__wifi__mgmt.md#ga31c78afc89bfdc4b54cee177843f8022) [setup\_cmd](structwifi__twt__params.md#a347f8cff73ee6b6ba6d15ddf6f376a2d);

[ 757](structwifi__twt__params.md#a805a23284ed4afa46b84efcd43329beb) enum [wifi\_twt\_setup\_resp\_status](group__wifi__mgmt.md#ga4d03aedac13ee4512d7717ac624f319a) [resp\_status](structwifi__twt__params.md#a805a23284ed4afa46b84efcd43329beb);

[ 759](structwifi__twt__params.md#a9faff59e577775b3fe53f2139462ac71) enum [wifi\_twt\_teardown\_status](group__wifi__mgmt.md#gad3709d07aaa3ed59b48f9dd7bd181989) [teardown\_status](structwifi__twt__params.md#a9faff59e577775b3fe53f2139462ac71);

[ 761](structwifi__twt__params.md#adda47e302a87a766f18e28016963a561) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [dialog\_token](structwifi__twt__params.md#adda47e302a87a766f18e28016963a561);

[ 763](structwifi__twt__params.md#a95ec4b32d37309efa47256ae1ea865da) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [flow\_id](structwifi__twt__params.md#a95ec4b32d37309efa47256ae1ea865da);

764 union {

766 struct {

[ 768](structwifi__twt__params.md#ab92fe571559fcd5d97cdf7e6b7d86681) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [twt\_interval](structwifi__twt__params.md#ab92fe571559fcd5d97cdf7e6b7d86681);

[ 770](structwifi__twt__params.md#ae547c6fc1c7cbad15bebcfdaa43f59e7) bool [responder](structwifi__twt__params.md#ae547c6fc1c7cbad15bebcfdaa43f59e7);

[ 772](structwifi__twt__params.md#a4e822c04b52fe6a9489e48e26b8f9382) bool [trigger](structwifi__twt__params.md#a4e822c04b52fe6a9489e48e26b8f9382);

[ 774](structwifi__twt__params.md#a8ea1e2501c8b69dc3fa606eb360f8678) bool [implicit](structwifi__twt__params.md#a8ea1e2501c8b69dc3fa606eb360f8678);

[ 776](structwifi__twt__params.md#a02f2d822d530e5376f256503439a54f9) bool [announce](structwifi__twt__params.md#a02f2d822d530e5376f256503439a54f9);

[ 778](structwifi__twt__params.md#a7c297459a17ed2fd232c62cca63e952f) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [twt\_wake\_interval](structwifi__twt__params.md#a7c297459a17ed2fd232c62cca63e952f);

[ 784](structwifi__twt__params.md#a6f907ca412251fdd7391f29bfa6d7713) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [twt\_wake\_ahead\_duration](structwifi__twt__params.md#a6f907ca412251fdd7391f29bfa6d7713);

[ 786](structwifi__twt__params.md#ac02eab9593b1ec2c9a0453a67076df88) bool [twt\_info\_disable](structwifi__twt__params.md#ac02eab9593b1ec2c9a0453a67076df88);

[ 788](structwifi__twt__params.md#aabb77296f007cb055f78fa1ec3d155a3) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [twt\_exponent](structwifi__twt__params.md#aabb77296f007cb055f78fa1ec3d155a3);

[ 790](structwifi__twt__params.md#aadad4556e2e5405b0703ebb4233a4d17) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [twt\_mantissa](structwifi__twt__params.md#aadad4556e2e5405b0703ebb4233a4d17);

[ 791](structwifi__twt__params.md#aee57c0189b210cfcc18e213e35b9479c) } [setup](structwifi__twt__params.md#aee57c0189b210cfcc18e213e35b9479c);

793 struct {

[ 795](structwifi__twt__params.md#aa05e5fa6a519f700147bb99d6e69a06b) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [btwt\_sta\_wait](structwifi__twt__params.md#aa05e5fa6a519f700147bb99d6e69a06b);

[ 797](structwifi__twt__params.md#a4459cf19226e199d23ae0cd1d7132b73) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [btwt\_offset](structwifi__twt__params.md#a4459cf19226e199d23ae0cd1d7132b73);

[ 799](structwifi__twt__params.md#a7e7c786c51d3bc70af135bad88ebde4f) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [btwt\_li](structwifi__twt__params.md#a7e7c786c51d3bc70af135bad88ebde4f);

[ 801](structwifi__twt__params.md#afc563010a33624bf01feac1292f0871d) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [btwt\_count](structwifi__twt__params.md#afc563010a33624bf01feac1292f0871d);

[ 803](structwifi__twt__params.md#aa11562186ea265b906861269bc8a692b) struct [wifi\_btwt\_params](structwifi__btwt__params.md) [btwt\_set\_cfg](structwifi__twt__params.md#aa11562186ea265b906861269bc8a692b)[[WIFI\_BTWT\_AGREEMENT\_MAX](group__wifi__mgmt.md#ga38d92ba342887e46c957b820d89a7a20)];

[ 804](structwifi__twt__params.md#a72ab809144b1dd3e7e121e489ef399e2) } [btwt](structwifi__twt__params.md#a72ab809144b1dd3e7e121e489ef399e2);

806 struct {

[ 808](structwifi__twt__params.md#a26d6bda00452f77832f69f4465c13efb) bool [teardown\_all](structwifi__twt__params.md#a26d6bda00452f77832f69f4465c13efb);

[ 809](structwifi__twt__params.md#aadf62f6386359ad15491d0073c9065bf) } [teardown](structwifi__twt__params.md#aadf62f6386359ad15491d0073c9065bf);

810 };

[ 812](structwifi__twt__params.md#a70f58b502bb67ef3b2068ded2160b612) enum [wifi\_twt\_fail\_reason](group__wifi__mgmt.md#ga97fa304f9a1db2294a93cccd4c93bcf6) [fail\_reason](structwifi__twt__params.md#a70f58b502bb67ef3b2068ded2160b612);

813};

814

816

817/\* Flow ID is only 3 bits \*/

818#define WIFI\_MAX\_TWT\_FLOWS 8

819#define WIFI\_MAX\_TWT\_INTERVAL\_US (LONG\_MAX - 1)

820/\* 256 (u8) \* 1TU \*/

821#define WIFI\_MAX\_TWT\_WAKE\_INTERVAL\_US 262144

822#define WIFI\_MAX\_TWT\_WAKE\_AHEAD\_DURATION\_US (LONG\_MAX - 1)

823#define WIFI\_MAX\_TWT\_EXPONENT 31

824

826

[ 828](structwifi__twt__flow__info.md)struct [wifi\_twt\_flow\_info](structwifi__twt__flow__info.md) {

[ 830](structwifi__twt__flow__info.md#ae15ba49fa54f82cc6a1fb0d4572114b7) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [twt\_interval](structwifi__twt__flow__info.md#ae15ba49fa54f82cc6a1fb0d4572114b7);

[ 832](structwifi__twt__flow__info.md#a123ce10bed8b62b01919a7ea7644a0ba) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [dialog\_token](structwifi__twt__flow__info.md#a123ce10bed8b62b01919a7ea7644a0ba);

[ 834](structwifi__twt__flow__info.md#acb0c618f1cebcb172f342cfe222683be) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [flow\_id](structwifi__twt__flow__info.md#acb0c618f1cebcb172f342cfe222683be);

[ 836](structwifi__twt__flow__info.md#a620ae8ba546e4091d74280cb1553b2cf) enum [wifi\_twt\_negotiation\_type](group__wifi__mgmt.md#ga695123cd534e2499f516a07fdc5cafa8) [negotiation\_type](structwifi__twt__flow__info.md#a620ae8ba546e4091d74280cb1553b2cf);

[ 838](structwifi__twt__flow__info.md#ac82e4de8ffc82f851061f8ba8d217dc1) bool [responder](structwifi__twt__flow__info.md#ac82e4de8ffc82f851061f8ba8d217dc1);

[ 840](structwifi__twt__flow__info.md#a952a67bd092c5dadba387bb13449c6f3) bool [trigger](structwifi__twt__flow__info.md#a952a67bd092c5dadba387bb13449c6f3);

[ 842](structwifi__twt__flow__info.md#afb480be82d1c6f351bd634fd83bfa5c7) bool [implicit](structwifi__twt__flow__info.md#afb480be82d1c6f351bd634fd83bfa5c7);

[ 844](structwifi__twt__flow__info.md#afc81a5111c265fd9bb2aca5f9510bfa8) bool [announce](structwifi__twt__flow__info.md#afc81a5111c265fd9bb2aca5f9510bfa8);

[ 846](structwifi__twt__flow__info.md#aede6cb0cfc999fac8ded49e2981a3762) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [twt\_wake\_interval](structwifi__twt__flow__info.md#aede6cb0cfc999fac8ded49e2981a3762);

[ 848](structwifi__twt__flow__info.md#a6384d3829d54a58a53eafcb74c64a658) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [twt\_wake\_ahead\_duration](structwifi__twt__flow__info.md#a6384d3829d54a58a53eafcb74c64a658);

849};

850

[ 852](structwifi__enterprise__creds__params.md)struct [wifi\_enterprise\_creds\_params](structwifi__enterprise__creds__params.md) {

[ 854](structwifi__enterprise__creds__params.md#ae37381504a457b2f1d56dd5270c6711d) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[ca\_cert](structwifi__enterprise__creds__params.md#ae37381504a457b2f1d56dd5270c6711d);

[ 856](structwifi__enterprise__creds__params.md#a5f7060fcd2ca3db0b202faf15062564b) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [ca\_cert\_len](structwifi__enterprise__creds__params.md#a5f7060fcd2ca3db0b202faf15062564b);

[ 858](structwifi__enterprise__creds__params.md#a81d61179feba627be5c6456130b9f2af) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[client\_cert](structwifi__enterprise__creds__params.md#a81d61179feba627be5c6456130b9f2af);

[ 860](structwifi__enterprise__creds__params.md#a5f122d59b25b00af2db7eeac93d5482e) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [client\_cert\_len](structwifi__enterprise__creds__params.md#a5f122d59b25b00af2db7eeac93d5482e);

[ 862](structwifi__enterprise__creds__params.md#a8d88f5a8a6ccc8a9a883078af49ae96b) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[client\_key](structwifi__enterprise__creds__params.md#a8d88f5a8a6ccc8a9a883078af49ae96b);

[ 864](structwifi__enterprise__creds__params.md#a09f5b34c81fe871e7513358499518d95) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [client\_key\_len](structwifi__enterprise__creds__params.md#a09f5b34c81fe871e7513358499518d95);

[ 866](structwifi__enterprise__creds__params.md#ad9b867873709d7f2363fef49d7b6f2ca) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[ca\_cert2](structwifi__enterprise__creds__params.md#ad9b867873709d7f2363fef49d7b6f2ca);

[ 868](structwifi__enterprise__creds__params.md#abf35045e71afb0cb9ea25c635c5ac141) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [ca\_cert2\_len](structwifi__enterprise__creds__params.md#abf35045e71afb0cb9ea25c635c5ac141);

[ 870](structwifi__enterprise__creds__params.md#a133126e338d89563733268a03e2fa613) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[client\_cert2](structwifi__enterprise__creds__params.md#a133126e338d89563733268a03e2fa613);

[ 872](structwifi__enterprise__creds__params.md#adbe26c9b88f44eb6b875888f6a03e1bb) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [client\_cert2\_len](structwifi__enterprise__creds__params.md#adbe26c9b88f44eb6b875888f6a03e1bb);

[ 874](structwifi__enterprise__creds__params.md#abcda4d7820681d517d70d8f130b47050) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[client\_key2](structwifi__enterprise__creds__params.md#abcda4d7820681d517d70d8f130b47050);

[ 876](structwifi__enterprise__creds__params.md#a3da90b8a8dfa848f617579760ad4f971) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [client\_key2\_len](structwifi__enterprise__creds__params.md#a3da90b8a8dfa848f617579760ad4f971);

[ 878](structwifi__enterprise__creds__params.md#ad3621e92a1aa968c58a899ace72967db) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[server\_cert](structwifi__enterprise__creds__params.md#ad3621e92a1aa968c58a899ace72967db);

[ 880](structwifi__enterprise__creds__params.md#ad0bfb59d3691e5d21cb4b810c4d1279e) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [server\_cert\_len](structwifi__enterprise__creds__params.md#ad0bfb59d3691e5d21cb4b810c4d1279e);

[ 882](structwifi__enterprise__creds__params.md#acb94a8885b5ab99d1a8fb33dffebc322) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[server\_key](structwifi__enterprise__creds__params.md#acb94a8885b5ab99d1a8fb33dffebc322);

[ 884](structwifi__enterprise__creds__params.md#a9500252974bd15037d4dbc41eba3a27d) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [server\_key\_len](structwifi__enterprise__creds__params.md#a9500252974bd15037d4dbc41eba3a27d);

[ 886](structwifi__enterprise__creds__params.md#ab0fd7419d8a94d1d804e5554acfbf49a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[dh\_param](structwifi__enterprise__creds__params.md#ab0fd7419d8a94d1d804e5554acfbf49a);

[ 888](structwifi__enterprise__creds__params.md#ac548e0b006a9f7b858409cda7c3d34ba) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [dh\_param\_len](structwifi__enterprise__creds__params.md#ac548e0b006a9f7b858409cda7c3d34ba);

889};

890

[ 892](structwifi__ps__config.md)struct [wifi\_ps\_config](structwifi__ps__config.md) {

[ 894](structwifi__ps__config.md#a9e83c10eaaa1d721cbc49b40aedb00df) char [num\_twt\_flows](structwifi__ps__config.md#a9e83c10eaaa1d721cbc49b40aedb00df);

[ 896](structwifi__ps__config.md#ab7460f0f253b2d552e49e98e2c770967) struct [wifi\_twt\_flow\_info](structwifi__twt__flow__info.md) [twt\_flows](structwifi__ps__config.md#ab7460f0f253b2d552e49e98e2c770967)[WIFI\_MAX\_TWT\_FLOWS];

[ 898](structwifi__ps__config.md#a357aafc2dedda37755b1cb1fc07fe5a6) struct [wifi\_ps\_params](structwifi__ps__params.md) [ps\_params](structwifi__ps__config.md#a357aafc2dedda37755b1cb1fc07fe5a6);

899};

900

[ 902](group__wifi__mgmt.md#gae129d0783276e662575af2314eef86cd)enum [wifi\_mgmt\_op](group__wifi__mgmt.md#gae129d0783276e662575af2314eef86cd) {

[ 904](group__wifi__mgmt.md#ggae129d0783276e662575af2314eef86cda6b8183a773e0cdfa85bc4b41ae70fdcd) [WIFI\_MGMT\_GET](group__wifi__mgmt.md#ggae129d0783276e662575af2314eef86cda6b8183a773e0cdfa85bc4b41ae70fdcd) = 0,

[ 906](group__wifi__mgmt.md#ggae129d0783276e662575af2314eef86cdaa0d5931c8275a8d3288ab668b6dfb5a1) [WIFI\_MGMT\_SET](group__wifi__mgmt.md#ggae129d0783276e662575af2314eef86cdaa0d5931c8275a8d3288ab668b6dfb5a1) = 1,

907};

908

[ 910](structwifi__11k__params.md)struct [wifi\_11k\_params](structwifi__11k__params.md) {

[ 912](structwifi__11k__params.md#ae6029ed4bada41f18df0329d0da7401e) enum [wifi\_mgmt\_op](group__wifi__mgmt.md#gae129d0783276e662575af2314eef86cd) [oper](structwifi__11k__params.md#ae6029ed4bada41f18df0329d0da7401e);

[ 914](structwifi__11k__params.md#a739c3e94b025aae2fcf5680aecf3d646) bool [enable\_11k](structwifi__11k__params.md#a739c3e94b025aae2fcf5680aecf3d646);

[ 916](structwifi__11k__params.md#a64ace23c71837417678ceb9cc8d5f216) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [ssid](structwifi__11k__params.md#a64ace23c71837417678ceb9cc8d5f216)[[WIFI\_SSID\_MAX\_LEN](group__wifi__mgmt.md#gad62c60666c9fdffe2e0e9c4388f87886) + 1];

917};

918

[ 920](group__wifi__mgmt.md#ga3a6bfa37bd7850342279d304df20977d)#define MAX\_REG\_CHAN\_NUM 42

921

[ 923](structwifi__reg__chan__info.md)struct [wifi\_reg\_chan\_info](structwifi__reg__chan__info.md) {

[ 925](structwifi__reg__chan__info.md#a0addffc11ef29f50c01b700835e59930) unsigned short [center\_frequency](structwifi__reg__chan__info.md#a0addffc11ef29f50c01b700835e59930);

[ 927](structwifi__reg__chan__info.md#af9169ab4a41fac4c6f6766fc96799545) unsigned short [max\_power](structwifi__reg__chan__info.md#af9169ab4a41fac4c6f6766fc96799545):8;

[ 929](structwifi__reg__chan__info.md#aa044611e18b7332b8577e29f6a769e3f) unsigned short [supported](structwifi__reg__chan__info.md#aa044611e18b7332b8577e29f6a769e3f):1;

[ 931](structwifi__reg__chan__info.md#acc7a88b004c9a61c8bf9ee1a97f85928) unsigned short [passive\_only](structwifi__reg__chan__info.md#acc7a88b004c9a61c8bf9ee1a97f85928):1;

[ 933](structwifi__reg__chan__info.md#a1ab137c142902d2de7d6be2626d7ac1f) unsigned short [dfs](structwifi__reg__chan__info.md#a1ab137c142902d2de7d6be2626d7ac1f):1;

934} \_\_packed;

935

[ 937](structwifi__reg__domain.md)struct [wifi\_reg\_domain](structwifi__reg__domain.md) {

[ 939](structwifi__reg__domain.md#a3bbfdf1497a87bbb6b6211c7035e1002) enum [wifi\_mgmt\_op](group__wifi__mgmt.md#gae129d0783276e662575af2314eef86cd) [oper](structwifi__reg__domain.md#a3bbfdf1497a87bbb6b6211c7035e1002);

[ 943](structwifi__reg__domain.md#a567c6fcae8032567aea83c18cd211c33) bool [force](structwifi__reg__domain.md#a567c6fcae8032567aea83c18cd211c33);

[ 945](structwifi__reg__domain.md#abf191495814c227fbbfaccb2f727762e) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [country\_code](structwifi__reg__domain.md#abf191495814c227fbbfaccb2f727762e)[[WIFI\_COUNTRY\_CODE\_LEN](group__wifi__mgmt.md#ga6766ef7bcb001f1fb526a4083b6cd8bc)];

[ 947](structwifi__reg__domain.md#a3278e9f43893f49ab9f9d0d7f24009c1) unsigned int [num\_channels](structwifi__reg__domain.md#a3278e9f43893f49ab9f9d0d7f24009c1);

[ 949](structwifi__reg__domain.md#a4c8c9c11e41123cd7738fdb0d33ae5fb) struct [wifi\_reg\_chan\_info](structwifi__reg__chan__info.md) \*[chan\_info](structwifi__reg__domain.md#a4c8c9c11e41123cd7738fdb0d33ae5fb);

950};

951

[ 953](group__wifi__mgmt.md#ga38c184ea35c02f304cccdf389ca6d552)enum [wifi\_twt\_sleep\_state](group__wifi__mgmt.md#ga38c184ea35c02f304cccdf389ca6d552) {

[ 955](group__wifi__mgmt.md#gga38c184ea35c02f304cccdf389ca6d552a37a7aba20723b6614e39e1c417f3113c) [WIFI\_TWT\_STATE\_SLEEP](group__wifi__mgmt.md#gga38c184ea35c02f304cccdf389ca6d552a37a7aba20723b6614e39e1c417f3113c) = 0,

[ 957](group__wifi__mgmt.md#gga38c184ea35c02f304cccdf389ca6d552a7b7b45f85d9644f897ca00bd7864e1b0) [WIFI\_TWT\_STATE\_AWAKE](group__wifi__mgmt.md#gga38c184ea35c02f304cccdf389ca6d552a7b7b45f85d9644f897ca00bd7864e1b0) = 1,

958};

959

960#if defined(CONFIG\_WIFI\_MGMT\_RAW\_SCAN\_RESULTS) || defined(\_\_DOXYGEN\_\_)

[ 962](structwifi__raw__scan__result.md)struct [wifi\_raw\_scan\_result](structwifi__raw__scan__result.md) {

[ 964](structwifi__raw__scan__result.md#a3f08580c6448a5fa28dd8a594fa7dad6) [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) [rssi](structwifi__raw__scan__result.md#a3f08580c6448a5fa28dd8a594fa7dad6);

[ 966](structwifi__raw__scan__result.md#a876966f469714eb481b42ccc8a63945c) int [frame\_length](structwifi__raw__scan__result.md#a876966f469714eb481b42ccc8a63945c);

[ 968](structwifi__raw__scan__result.md#aa2c7781882c6775616cbc8016b0842f6) unsigned short [frequency](structwifi__raw__scan__result.md#aa2c7781882c6775616cbc8016b0842f6);

[ 970](structwifi__raw__scan__result.md#a5710e89199c147ce898602795f00aba3) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [data](structwifi__raw__scan__result.md#a5710e89199c147ce898602795f00aba3)[CONFIG\_WIFI\_MGMT\_RAW\_SCAN\_RESULT\_LENGTH];

971};

972#endif /\* CONFIG\_WIFI\_MGMT\_RAW\_SCAN\_RESULTS \*/

973

[ 975](structwifi__ap__sta__info.md)struct [wifi\_ap\_sta\_info](structwifi__ap__sta__info.md) {

[ 977](structwifi__ap__sta__info.md#a7d8bd52340d4937a4b5b7d2c00662441) enum [wifi\_link\_mode](group__wifi__mgmt.md#gabdb2a784d4727b71ab44cca04e422c62) [link\_mode](structwifi__ap__sta__info.md#a7d8bd52340d4937a4b5b7d2c00662441);

[ 979](structwifi__ap__sta__info.md#a7db904376ec73b774aa9d8236c15b3f6) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [mac](structwifi__ap__sta__info.md#a7db904376ec73b774aa9d8236c15b3f6)[[WIFI\_MAC\_ADDR\_LEN](group__wifi__mgmt.md#ga29409ff83a53c6464decdde9bdd04de6)];

[ 981](structwifi__ap__sta__info.md#a7f7c8b144bb3464af5213708591eefda) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [mac\_length](structwifi__ap__sta__info.md#a7f7c8b144bb3464af5213708591eefda);

[ 983](structwifi__ap__sta__info.md#a838c9a4288c9bc7e97afe2334c678f34) bool [twt\_capable](structwifi__ap__sta__info.md#a838c9a4288c9bc7e97afe2334c678f34);

984};

985

987

988/\* for use in max info size calculations \*/

989union wifi\_mgmt\_events {

990 struct [wifi\_scan\_result](structwifi__scan__result.md) scan\_result;

991 struct [wifi\_status](structwifi__status.md) connect\_status;

992 struct [wifi\_iface\_status](structwifi__iface__status.md) iface\_status;

993#ifdef CONFIG\_WIFI\_MGMT\_RAW\_SCAN\_RESULTS

994 struct [wifi\_raw\_scan\_result](structwifi__raw__scan__result.md) raw\_scan\_result;

995#endif /\* CONFIG\_WIFI\_MGMT\_RAW\_SCAN\_RESULTS \*/

996 struct [wifi\_twt\_params](structwifi__twt__params.md) twt\_params;

997 struct [wifi\_ap\_sta\_info](structwifi__ap__sta__info.md) ap\_sta\_info;

998};

999

1001

[ 1003](structwifi__mode__info.md)struct [wifi\_mode\_info](structwifi__mode__info.md) {

[ 1005](structwifi__mode__info.md#aa29d3b88fc718aa3ac05daf38974707d) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [mode](structwifi__mode__info.md#aa29d3b88fc718aa3ac05daf38974707d);

[ 1007](structwifi__mode__info.md#add58dd3b45fd2ddaf684d1b0de81bef9) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [if\_index](structwifi__mode__info.md#add58dd3b45fd2ddaf684d1b0de81bef9);

[ 1009](structwifi__mode__info.md#a57c101db8b81ab0ac5dd0a158057a64a) enum [wifi\_mgmt\_op](group__wifi__mgmt.md#gae129d0783276e662575af2314eef86cd) [oper](structwifi__mode__info.md#a57c101db8b81ab0ac5dd0a158057a64a);

1010};

1011

[ 1013](structwifi__filter__info.md)struct [wifi\_filter\_info](structwifi__filter__info.md) {

[ 1015](structwifi__filter__info.md#ad9560be814299055cfa11b995a7dcf42) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [filter](structwifi__filter__info.md#ad9560be814299055cfa11b995a7dcf42);

[ 1017](structwifi__filter__info.md#af9ea91e31e78afcb7ffe1ff9a04277a3) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [if\_index](structwifi__filter__info.md#af9ea91e31e78afcb7ffe1ff9a04277a3);

[ 1019](structwifi__filter__info.md#a1b2d0448fc7f62654e3f5aacfba62f8f) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [buffer\_size](structwifi__filter__info.md#a1b2d0448fc7f62654e3f5aacfba62f8f);

[ 1021](structwifi__filter__info.md#aedd5e220cdde5768cb0f4aff920971cd) enum [wifi\_mgmt\_op](group__wifi__mgmt.md#gae129d0783276e662575af2314eef86cd) [oper](structwifi__filter__info.md#aedd5e220cdde5768cb0f4aff920971cd);

1022};

1023

[ 1025](structwifi__channel__info.md)struct [wifi\_channel\_info](structwifi__channel__info.md) {

[ 1027](structwifi__channel__info.md#a799cbc0a67764f6680322ba0f2ad3300) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [channel](structwifi__channel__info.md#a799cbc0a67764f6680322ba0f2ad3300);

[ 1029](structwifi__channel__info.md#a43a7dd8c19d0c6540e3cc0b5d1d6165d) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [if\_index](structwifi__channel__info.md#a43a7dd8c19d0c6540e3cc0b5d1d6165d);

[ 1031](structwifi__channel__info.md#aa8ef8a71b49ead3664fff9a4d61b1ce8) enum [wifi\_mgmt\_op](group__wifi__mgmt.md#gae129d0783276e662575af2314eef86cd) [oper](structwifi__channel__info.md#aa8ef8a71b49ead3664fff9a4d61b1ce8);

1032};

1033

1035#define WIFI\_AP\_STA\_MAX\_INACTIVITY (LONG\_MAX - 1)

1036#define WIFI\_AP\_IEEE\_80211\_CAPAB\_MAX\_LEN 64

1038

[ 1040](structwifi__ap__config__params.md)struct [wifi\_ap\_config\_params](structwifi__ap__config__params.md) {

[ 1042](structwifi__ap__config__params.md#a4c391cf504a994ed0bc4971afdf76774) enum [wifi\_ap\_config\_param](group__wifi__mgmt.md#ga83546cf946a9123c563609e8903d9642) [type](structwifi__ap__config__params.md#a4c391cf504a994ed0bc4971afdf76774);

[ 1044](structwifi__ap__config__params.md#a289866d9209450e893281b4c198a546a) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [max\_inactivity](structwifi__ap__config__params.md#a289866d9209450e893281b4c198a546a);

[ 1046](structwifi__ap__config__params.md#a7fc0fad99f53ed8e1ac40b74ec98bf9a) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [max\_num\_sta](structwifi__ap__config__params.md#a7fc0fad99f53ed8e1ac40b74ec98bf9a);

[ 1048](structwifi__ap__config__params.md#aba4e43dff01fa026c8dbbfff670d3097) enum [wifi\_frequency\_bandwidths](group__wifi__mgmt.md#ga3b01cead3c2eb4581fe85e2aaaffbd49) [bandwidth](structwifi__ap__config__params.md#aba4e43dff01fa026c8dbbfff670d3097);

1049#if defined(CONFIG\_WIFI\_NM\_HOSTAPD\_AP)

1051 char ht\_capab[WIFI\_AP\_IEEE\_80211\_CAPAB\_MAX\_LEN + 1];

1053 char vht\_capab[WIFI\_AP\_IEEE\_80211\_CAPAB\_MAX\_LEN + 1];

1054#endif

1055};

1056

1057#ifdef CONFIG\_WIFI\_NM\_WPA\_SUPPLICANT\_DPP

1060#define WIFI\_DPP\_QRCODE\_MAX\_LEN 255

1061

1063enum wifi\_dpp\_op {

1065 WIFI\_DPP\_OP\_INVALID = 0,

1067 WIFI\_DPP\_CONFIGURATOR\_ADD,

1069 WIFI\_DPP\_AUTH\_INIT,

1071 WIFI\_DPP\_QR\_CODE,

1073 WIFI\_DPP\_CHIRP,

1075 WIFI\_DPP\_LISTEN,

1077 WIFI\_DPP\_BOOTSTRAP\_GEN,

1079 WIFI\_DPP\_BOOTSTRAP\_GET\_URI,

1081 WIFI\_DPP\_SET\_CONF\_PARAM,

1083 WIFI\_DPP\_SET\_WAIT\_RESP\_TIME,

1085 WIFI\_DPP\_RECONFIG

1086};

1087

1089enum wifi\_dpp\_curves {

1091 WIFI\_DPP\_CURVES\_DEFAULT = 0,

1093 WIFI\_DPP\_CURVES\_P\_256,

1095 WIFI\_DPP\_CURVES\_P\_384,

1097 WIFI\_DPP\_CURVES\_P\_512,

1099 WIFI\_DPP\_CURVES\_BP\_256,

1101 WIFI\_DPP\_CURVES\_BP\_384,

1103 WIFI\_DPP\_CURVES\_BP\_512

1104};

1105

1107enum wifi\_dpp\_role {

1109 WIFI\_DPP\_ROLE\_UNSET = 0,

1111 WIFI\_DPP\_ROLE\_CONFIGURATOR,

1113 WIFI\_DPP\_ROLE\_ENROLLEE,

1115 WIFI\_DPP\_ROLE\_EITHER

1116};

1117

1122enum wifi\_dpp\_conf {

1124 WIFI\_DPP\_CONF\_UNSET = 0,

1126 WIFI\_DPP\_CONF\_STA,

1128 WIFI\_DPP\_CONF\_AP,

1130 WIFI\_DPP\_CONF\_QUERY

1131};

1132

1137enum wifi\_dpp\_bootstrap\_type {

1139 WIFI\_DPP\_BOOTSTRAP\_TYPE\_UNSET = 0,

1141 WIFI\_DPP\_BOOTSTRAP\_TYPE\_QRCODE,

1143 WIFI\_DPP\_BOOTSTRAP\_TYPE\_PKEX,

1145 WIFI\_DPP\_BOOTSTRAP\_TYPE\_NFC\_URI

1146};

1147

1149struct wifi\_dpp\_configurator\_add\_params {

1151 int curve;

1153 int net\_access\_key\_curve;

1154};

1155

1157struct wifi\_dpp\_auth\_init\_params {

1159 int peer;

1161 int configurator;

1163 int role;

1165 int conf;

1167 char ssid[[WIFI\_SSID\_MAX\_LEN](group__wifi__mgmt.md#gad62c60666c9fdffe2e0e9c4388f87886) + 1];

1168};

1169

1171struct wifi\_dpp\_chirp\_params {

1173 int id;

1175 int freq;

1176};

1177

1179struct wifi\_dpp\_listen\_params {

1181 int freq;

1183 int role;

1184};

1185

1187struct wifi\_dpp\_bootstrap\_gen\_params {

1189 int type;

1191 int op\_class;

1193 int chan;

1195 int curve;

1197 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) mac[[WIFI\_MAC\_ADDR\_LEN](group__wifi__mgmt.md#ga29409ff83a53c6464decdde9bdd04de6)];

1198};

1199

1201struct wifi\_dpp\_configurator\_set\_params {

1203 int peer;

1205 int configurator;

1207 int role;

1209 int conf;

1211 int curve;

1213 int net\_access\_key\_curve;

1215 char ssid[[WIFI\_SSID\_MAX\_LEN](group__wifi__mgmt.md#gad62c60666c9fdffe2e0e9c4388f87886) + 1];

1216};

1217

1220struct wifi\_dpp\_params {

1222 int action;

1223 union {

1225 struct wifi\_dpp\_configurator\_add\_params configurator\_add;

1227 struct wifi\_dpp\_auth\_init\_params auth\_init;

1229 struct wifi\_dpp\_chirp\_params chirp;

1231 struct wifi\_dpp\_listen\_params [listen](posix_2sys_2socket_8h.md#a7005ffbeeff92be5394ff3244da79028);

1233 struct wifi\_dpp\_bootstrap\_gen\_params bootstrap\_gen;

1235 struct wifi\_dpp\_configurator\_set\_params configurator\_set;

1237 int id;

1239 int dpp\_resp\_wait\_time;

1241 int network\_id;

1243 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) dpp\_qr\_code[WIFI\_DPP\_QRCODE\_MAX\_LEN + 1];

1248 char resp[WIFI\_DPP\_QRCODE\_MAX\_LEN + 1];

1249 };

1250};

1251#endif /\* CONFIG\_WIFI\_NM\_WPA\_SUPPLICANT\_DPP \*/

1252

[ 1253](group__wifi__mgmt.md#ga234d72d7c881e67ff49fb6c474c622e3)#define WIFI\_WPS\_PIN\_MAX\_LEN 8

1254

[ 1256](group__wifi__mgmt.md#ga4c36ae1a5171d3fbaeebf95c16be496d)enum [wifi\_wps\_op](group__wifi__mgmt.md#ga4c36ae1a5171d3fbaeebf95c16be496d) {

[ 1258](group__wifi__mgmt.md#gga4c36ae1a5171d3fbaeebf95c16be496da093f5b3ef95d9e571ea169430da57e88) [WIFI\_WPS\_PBC](group__wifi__mgmt.md#gga4c36ae1a5171d3fbaeebf95c16be496da093f5b3ef95d9e571ea169430da57e88) = 0,

[ 1260](group__wifi__mgmt.md#gga4c36ae1a5171d3fbaeebf95c16be496da75bd5067903c2bba8a06732f0431393d) [WIFI\_WPS\_PIN\_GET](group__wifi__mgmt.md#gga4c36ae1a5171d3fbaeebf95c16be496da75bd5067903c2bba8a06732f0431393d) = 1,

[ 1262](group__wifi__mgmt.md#gga4c36ae1a5171d3fbaeebf95c16be496da58120620fd2fca80bdac7990ed0e7552) [WIFI\_WPS\_PIN\_SET](group__wifi__mgmt.md#gga4c36ae1a5171d3fbaeebf95c16be496da58120620fd2fca80bdac7990ed0e7552) = 2,

1263};

1264

[ 1266](structwifi__wps__config__params.md)struct [wifi\_wps\_config\_params](structwifi__wps__config__params.md) {

[ 1268](structwifi__wps__config__params.md#aa7a10889c5cd5124983b0f7242d23b7e) enum [wifi\_wps\_op](group__wifi__mgmt.md#ga4c36ae1a5171d3fbaeebf95c16be496d) [oper](structwifi__wps__config__params.md#aa7a10889c5cd5124983b0f7242d23b7e);

[ 1270](structwifi__wps__config__params.md#a962bd6513c564150e0c75112b96bbe15) char [pin](structwifi__wps__config__params.md#a962bd6513c564150e0c75112b96bbe15)[[WIFI\_WPS\_PIN\_MAX\_LEN](group__wifi__mgmt.md#ga234d72d7c881e67ff49fb6c474c622e3) + 1];

1271};

1272

[ 1275](group__wifi__mgmt.md#ga0cc87c00cbee0d0aca833119dbf0d74e)enum [wifi\_sap\_iface\_state](group__wifi__mgmt.md#ga0cc87c00cbee0d0aca833119dbf0d74e) {

[ 1276](group__wifi__mgmt.md#gga0cc87c00cbee0d0aca833119dbf0d74ead92795c629fe828e7efde485eb2761c0) [WIFI\_SAP\_IFACE\_UNINITIALIZED](group__wifi__mgmt.md#gga0cc87c00cbee0d0aca833119dbf0d74ead92795c629fe828e7efde485eb2761c0),

[ 1277](group__wifi__mgmt.md#gga0cc87c00cbee0d0aca833119dbf0d74ea59a8530057e9839d89243558cc366d69) [WIFI\_SAP\_IFACE\_DISABLED](group__wifi__mgmt.md#gga0cc87c00cbee0d0aca833119dbf0d74ea59a8530057e9839d89243558cc366d69),

[ 1278](group__wifi__mgmt.md#gga0cc87c00cbee0d0aca833119dbf0d74ea403d84f907f84492eed8e33713e828ae) [WIFI\_SAP\_IFACE\_COUNTRY\_UPDATE](group__wifi__mgmt.md#gga0cc87c00cbee0d0aca833119dbf0d74ea403d84f907f84492eed8e33713e828ae),

[ 1279](group__wifi__mgmt.md#gga0cc87c00cbee0d0aca833119dbf0d74eab3fea1a0ef90043699cb7d8ab064be7e) [WIFI\_SAP\_IFACE\_ACS](group__wifi__mgmt.md#gga0cc87c00cbee0d0aca833119dbf0d74eab3fea1a0ef90043699cb7d8ab064be7e),

[ 1280](group__wifi__mgmt.md#gga0cc87c00cbee0d0aca833119dbf0d74eaa3a6e6e367c7384379f3c562d1fc358f) [WIFI\_SAP\_IFACE\_HT\_SCAN](group__wifi__mgmt.md#gga0cc87c00cbee0d0aca833119dbf0d74eaa3a6e6e367c7384379f3c562d1fc358f),

[ 1281](group__wifi__mgmt.md#gga0cc87c00cbee0d0aca833119dbf0d74eafdf99a461cf5878240cc40ae4ea7e113) [WIFI\_SAP\_IFACE\_DFS](group__wifi__mgmt.md#gga0cc87c00cbee0d0aca833119dbf0d74eafdf99a461cf5878240cc40ae4ea7e113),

[ 1282](group__wifi__mgmt.md#gga0cc87c00cbee0d0aca833119dbf0d74eaea74f039e6a5abe976e9956b5a01ff1a) [WIFI\_SAP\_IFACE\_NO\_IR](group__wifi__mgmt.md#gga0cc87c00cbee0d0aca833119dbf0d74eaea74f039e6a5abe976e9956b5a01ff1a),

[ 1283](group__wifi__mgmt.md#gga0cc87c00cbee0d0aca833119dbf0d74eaa9133b73b886f2ec543acd282b33eeda) [WIFI\_SAP\_IFACE\_ENABLED](group__wifi__mgmt.md#gga0cc87c00cbee0d0aca833119dbf0d74eaa9133b73b886f2ec543acd282b33eeda)

1284};

1285

1286/\* Extended Capabilities \*/

[ 1287](group__wifi__mgmt.md#ga03ab29789adfe867c4ebaddc39482344)enum [wifi\_ext\_capab](group__wifi__mgmt.md#ga03ab29789adfe867c4ebaddc39482344) {

[ 1288](group__wifi__mgmt.md#gga03ab29789adfe867c4ebaddc39482344abf275508c3f69321cdf704779e976d68) [WIFI\_EXT\_CAPAB\_20\_40\_COEX](group__wifi__mgmt.md#gga03ab29789adfe867c4ebaddc39482344abf275508c3f69321cdf704779e976d68) = 0,

[ 1289](group__wifi__mgmt.md#gga03ab29789adfe867c4ebaddc39482344a1363c1318e4281e057d848194396feb7) [WIFI\_EXT\_CAPAB\_GLK](group__wifi__mgmt.md#gga03ab29789adfe867c4ebaddc39482344a1363c1318e4281e057d848194396feb7) = 1,

[ 1290](group__wifi__mgmt.md#gga03ab29789adfe867c4ebaddc39482344acf854adfca2bb41dd5d75df2b16c3e5e) [WIFI\_EXT\_CAPAB\_EXT\_CHAN\_SWITCH](group__wifi__mgmt.md#gga03ab29789adfe867c4ebaddc39482344acf854adfca2bb41dd5d75df2b16c3e5e) = 2,

[ 1291](group__wifi__mgmt.md#gga03ab29789adfe867c4ebaddc39482344af42762fd723afef7fae98cbefbfff056) [WIFI\_EXT\_CAPAB\_TIM\_BROADCAST](group__wifi__mgmt.md#gga03ab29789adfe867c4ebaddc39482344af42762fd723afef7fae98cbefbfff056) = 18,

[ 1292](group__wifi__mgmt.md#gga03ab29789adfe867c4ebaddc39482344ac5c648efedadc82fae7d9e0851ff71ba) [WIFI\_EXT\_CAPAB\_BSS\_TRANSITION](group__wifi__mgmt.md#gga03ab29789adfe867c4ebaddc39482344ac5c648efedadc82fae7d9e0851ff71ba) = 19,

1293};

1294

1295#include <[zephyr/net/net\_if.h](net__if_8h.md)>

1296

[ 1303](group__wifi__mgmt.md#gad34b366f1c315207ce0da587ca96d8d8)typedef void (\*[scan\_result\_cb\_t](group__wifi__mgmt.md#gad34b366f1c315207ce0da587ca96d8d8))(struct [net\_if](structnet__if.md) \*iface, int status,

1304 struct [wifi\_scan\_result](structwifi__scan__result.md) \*entry);

1305

1306#ifdef CONFIG\_WIFI\_MGMT\_RAW\_SCAN\_RESULTS

1313typedef void (\*raw\_scan\_result\_cb\_t)(struct [net\_if](structnet__if.md) \*iface, int status,

1314 struct [wifi\_raw\_scan\_result](structwifi__raw__scan__result.md) \*entry);

1315#endif /\* CONFIG\_WIFI\_MGMT\_RAW\_SCAN\_RESULTS \*/

1316

[ 1318](structwifi__mgmt__ops.md)struct [wifi\_mgmt\_ops](structwifi__mgmt__ops.md) {

[ 1330](structwifi__mgmt__ops.md#a267030c27da3cdc251badd0ed7f7b1cb) int (\*[scan](structwifi__mgmt__ops.md#a267030c27da3cdc251badd0ed7f7b1cb))(const struct [device](structdevice.md) \*dev,

1331 struct [wifi\_scan\_params](structwifi__scan__params.md) \*params,

1332 [scan\_result\_cb\_t](group__wifi__mgmt.md#gad34b366f1c315207ce0da587ca96d8d8) cb);

[ 1340](structwifi__mgmt__ops.md#ae6255ea77739918797b4f3c7a4634a75) int (\*[connect](structwifi__mgmt__ops.md#ae6255ea77739918797b4f3c7a4634a75))(const struct [device](structdevice.md) \*dev,

1341 struct [wifi\_connect\_req\_params](structwifi__connect__req__params.md) \*params);

[ 1348](structwifi__mgmt__ops.md#a5725c6fd93ae189a3019374cd4ad2ff4) int (\*[disconnect](structwifi__mgmt__ops.md#a5725c6fd93ae189a3019374cd4ad2ff4))(const struct [device](structdevice.md) \*dev);

[ 1356](structwifi__mgmt__ops.md#ac2ce3a4a86c43e30d33261f71c44198a) int (\*[ap\_enable](structwifi__mgmt__ops.md#ac2ce3a4a86c43e30d33261f71c44198a))(const struct [device](structdevice.md) \*dev,

1357 struct [wifi\_connect\_req\_params](structwifi__connect__req__params.md) \*params);

[ 1364](structwifi__mgmt__ops.md#a5aa7a2be82eb1783872abda2b8978235) int (\*[ap\_disable](structwifi__mgmt__ops.md#a5aa7a2be82eb1783872abda2b8978235))(const struct [device](structdevice.md) \*dev);

[ 1372](structwifi__mgmt__ops.md#af01aaec29be78c02314acf13b5c1b6f7) int (\*[ap\_sta\_disconnect](structwifi__mgmt__ops.md#af01aaec29be78c02314acf13b5c1b6f7))(const struct [device](structdevice.md) \*dev, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*mac);

[ 1380](structwifi__mgmt__ops.md#adf157476d776bc9c068e99e1a0266fd3) int (\*[iface\_status](structwifi__mgmt__ops.md#adf157476d776bc9c068e99e1a0266fd3))(const struct [device](structdevice.md) \*dev, struct [wifi\_iface\_status](structwifi__iface__status.md) \*status);

1381#if defined(CONFIG\_NET\_STATISTICS\_WIFI) || defined(\_\_DOXYGEN\_\_)

[ 1389](structwifi__mgmt__ops.md#a5e6fdf836273fcde54efff4c77bfdf0e) int (\*[get\_stats](structwifi__mgmt__ops.md#a5e6fdf836273fcde54efff4c77bfdf0e))(const struct [device](structdevice.md) \*dev, struct [net\_stats\_wifi](structnet__stats__wifi.md) \*stats);

[ 1396](structwifi__mgmt__ops.md#ae66901b434ab02863c0d3bd539c4b650) int (\*[reset\_stats](structwifi__mgmt__ops.md#ae66901b434ab02863c0d3bd539c4b650))(const struct [device](structdevice.md) \*dev);

1397#endif /\* CONFIG\_NET\_STATISTICS\_WIFI \*/

[ 1405](structwifi__mgmt__ops.md#a2cf66093ad850319cf222468e22ff485) int (\*[cfg\_11k](structwifi__mgmt__ops.md#a2cf66093ad850319cf222468e22ff485))(const struct [device](structdevice.md) \*dev, struct [wifi\_11k\_params](structwifi__11k__params.md) \*params);

[ 1413](structwifi__mgmt__ops.md#a1cdd0b76a0a326e968d27c0a3cafcef8) int (\*[send\_11k\_neighbor\_request](structwifi__mgmt__ops.md#a1cdd0b76a0a326e968d27c0a3cafcef8))(const struct [device](structdevice.md) \*dev, struct [wifi\_11k\_params](structwifi__11k__params.md) \*params);

[ 1421](structwifi__mgmt__ops.md#ac0f3f7fa699b1bc7db2358e77dd44cc4) int (\*[set\_power\_save](structwifi__mgmt__ops.md#ac0f3f7fa699b1bc7db2358e77dd44cc4))(const struct [device](structdevice.md) \*dev, struct [wifi\_ps\_params](structwifi__ps__params.md) \*params);

[ 1429](structwifi__mgmt__ops.md#ab4500534b6abe0449290c8bd8f729fc4) int (\*[set\_twt](structwifi__mgmt__ops.md#ab4500534b6abe0449290c8bd8f729fc4))(const struct [device](structdevice.md) \*dev, struct [wifi\_twt\_params](structwifi__twt__params.md) \*params);

[ 1437](structwifi__mgmt__ops.md#ad2d1ab4db1947dbdb2909a675fa1d653) int (\*[set\_btwt](structwifi__mgmt__ops.md#ad2d1ab4db1947dbdb2909a675fa1d653))(const struct [device](structdevice.md) \*dev, struct [wifi\_twt\_params](structwifi__twt__params.md) \*params);

[ 1445](structwifi__mgmt__ops.md#a52690b13f8a1e7b0c2302eaa24ae4c7f) int (\*[get\_power\_save\_config](structwifi__mgmt__ops.md#a52690b13f8a1e7b0c2302eaa24ae4c7f))(const struct [device](structdevice.md) \*dev, struct [wifi\_ps\_config](structwifi__ps__config.md) \*config);

[ 1453](structwifi__mgmt__ops.md#a0a287c8acf2d7bf9333b755589294881) int (\*[reg\_domain](structwifi__mgmt__ops.md#a0a287c8acf2d7bf9333b755589294881))(const struct [device](structdevice.md) \*dev, struct [wifi\_reg\_domain](structwifi__reg__domain.md) \*[reg\_domain](structwifi__mgmt__ops.md#a0a287c8acf2d7bf9333b755589294881));

[ 1461](structwifi__mgmt__ops.md#ad645276745ce8dd9685e0744efdfc733) int (\*[filter](structwifi__mgmt__ops.md#ad645276745ce8dd9685e0744efdfc733))(const struct [device](structdevice.md) \*dev, struct [wifi\_filter\_info](structwifi__filter__info.md) \*[filter](structwifi__mgmt__ops.md#ad645276745ce8dd9685e0744efdfc733));

[ 1469](structwifi__mgmt__ops.md#ae2fb1bc35bf9255655a30a2ad8588b7c) int (\*[mode](structwifi__mgmt__ops.md#ae2fb1bc35bf9255655a30a2ad8588b7c))(const struct [device](structdevice.md) \*dev, struct [wifi\_mode\_info](structwifi__mode__info.md) \*[mode](structwifi__mgmt__ops.md#ae2fb1bc35bf9255655a30a2ad8588b7c));

[ 1477](structwifi__mgmt__ops.md#af17ddfea01d0ab478f6fd50b1c9d6015) int (\*[channel](structwifi__mgmt__ops.md#af17ddfea01d0ab478f6fd50b1c9d6015))(const struct [device](structdevice.md) \*dev, struct [wifi\_channel\_info](structwifi__channel__info.md) \*[channel](structwifi__mgmt__ops.md#af17ddfea01d0ab478f6fd50b1c9d6015));

1478

[ 1486](structwifi__mgmt__ops.md#a3437f5881a8e0a487c11dd43a6099b6d) int (\*[btm\_query](structwifi__mgmt__ops.md#a3437f5881a8e0a487c11dd43a6099b6d))(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) reason);

[ 1494](structwifi__mgmt__ops.md#afb83b59f392b11fe8071ca57e3ea3928) int (\*[bss\_ext\_capab](structwifi__mgmt__ops.md#afb83b59f392b11fe8071ca57e3ea3928))(const struct [device](structdevice.md) \*dev, int capab);

1495

[ 1502](structwifi__mgmt__ops.md#aa088223f84094614145d9d81e3acc20a) int (\*[legacy\_roam](structwifi__mgmt__ops.md#aa088223f84094614145d9d81e3acc20a))(const struct [device](structdevice.md) \*dev);

1503

[ 1516](structwifi__mgmt__ops.md#aa7e4bc3dbc960091d11ffe5454259885) int (\*[get\_version](structwifi__mgmt__ops.md#aa7e4bc3dbc960091d11ffe5454259885))(const struct [device](structdevice.md) \*dev, struct [wifi\_version](structwifi__version.md) \*params);

[ 1524](structwifi__mgmt__ops.md#a42c2aa55df30158d8b5d6f4c81e3e2dd) int (\*[get\_conn\_params](structwifi__mgmt__ops.md#a42c2aa55df30158d8b5d6f4c81e3e2dd))(const struct [device](structdevice.md) \*dev, struct [wifi\_connect\_req\_params](structwifi__connect__req__params.md) \*params);

[ 1532](structwifi__mgmt__ops.md#a514e06d63bcf6dc11dba1d3af8d102d5) int (\*[set\_rts\_threshold](structwifi__mgmt__ops.md#a514e06d63bcf6dc11dba1d3af8d102d5))(const struct [device](structdevice.md) \*dev, unsigned int rts\_threshold);

[ 1540](structwifi__mgmt__ops.md#a2475f32afcce72464b2db6ecad7fb3eb) int (\*[ap\_config\_params](structwifi__mgmt__ops.md#a2475f32afcce72464b2db6ecad7fb3eb))(const struct [device](structdevice.md) \*dev, struct [wifi\_ap\_config\_params](structwifi__ap__config__params.md) \*params);

1541

1542#ifdef CONFIG\_WIFI\_NM\_WPA\_SUPPLICANT\_DPP

1550 int (\*dpp\_dispatch)(const struct [device](structdevice.md) \*dev, struct wifi\_dpp\_params \*params);

1551#endif /\* CONFIG\_WIFI\_NM\_WPA\_SUPPLICANT\_DPP \*/

[ 1558](structwifi__mgmt__ops.md#aadf991d6f6725e5c179ca8343d626ad8) int (\*[pmksa\_flush](structwifi__mgmt__ops.md#aadf991d6f6725e5c179ca8343d626ad8))(const struct [device](structdevice.md) \*dev);

1566#ifdef CONFIG\_WIFI\_NM\_WPA\_SUPPLICANT\_CRYPTO\_ENTERPRISE

1567 int (\*enterprise\_creds)(const struct [device](structdevice.md) \*dev,

1568 struct [wifi\_enterprise\_creds\_params](structwifi__enterprise__creds__params.md) \*creds);

1569#endif

[ 1577](structwifi__mgmt__ops.md#a20706f9eed43b3380258b62fdf93be02) int (\*[get\_rts\_threshold](structwifi__mgmt__ops.md#a20706f9eed43b3380258b62fdf93be02))(const struct [device](structdevice.md) \*dev, unsigned int \*rts\_threshold);

[ 1585](structwifi__mgmt__ops.md#aaf85f7b56997fb40689b927535af5e85) int (\*[wps\_config](structwifi__mgmt__ops.md#aaf85f7b56997fb40689b927535af5e85))(const struct [device](structdevice.md) \*dev, struct [wifi\_wps\_config\_params](structwifi__wps__config__params.md) \*params);

[ 1593](structwifi__mgmt__ops.md#a538ffba0a7e045ca9c8ac62ccefc8a36) int (\*[candidate\_scan](structwifi__mgmt__ops.md#a538ffba0a7e045ca9c8ac62ccefc8a36))(const struct [device](structdevice.md) \*dev, struct [wifi\_scan\_params](structwifi__scan__params.md) \*params);

[ 1600](structwifi__mgmt__ops.md#a501b114298738ac6af9c4a80f5360d79) int (\*[start\_11r\_roaming](structwifi__mgmt__ops.md#a501b114298738ac6af9c4a80f5360d79))(const struct [device](structdevice.md) \*dev);

1601};

1602

[ 1604](structnet__wifi__mgmt__offload.md)struct [net\_wifi\_mgmt\_offload](structnet__wifi__mgmt__offload.md) {

1611#if defined(CONFIG\_WIFI\_USE\_NATIVE\_NETWORKING) || defined(\_\_DOXYGEN\_\_)

[ 1613](structnet__wifi__mgmt__offload.md#a1d34a954a2f16d29f51dc51dd6fbb845) struct [ethernet\_api](structethernet__api.md) [wifi\_iface](structnet__wifi__mgmt__offload.md#a1d34a954a2f16d29f51dc51dd6fbb845);

1614#else

1616 struct [offloaded\_if\_api](structoffloaded__if__api.md) [wifi\_iface](structnet__wifi__mgmt__offload.md#a1d34a954a2f16d29f51dc51dd6fbb845);

1617#endif

[ 1619](structnet__wifi__mgmt__offload.md#a98fcc053d9820d2d981ed659520c9b3b) const struct [wifi\_mgmt\_ops](structwifi__mgmt__ops.md) \*const [wifi\_mgmt\_api](structnet__wifi__mgmt__offload.md#a98fcc053d9820d2d981ed659520c9b3b);

1620

1621#if defined(CONFIG\_WIFI\_NM\_WPA\_SUPPLICANT) || defined(\_\_DOXYGEN\_\_)

[ 1623](structnet__wifi__mgmt__offload.md#a991e0bc6247578a3d1c9d2d3ab0b63d7) const void \*[wifi\_drv\_ops](structnet__wifi__mgmt__offload.md#a991e0bc6247578a3d1c9d2d3ab0b63d7);

1624#endif

1625};

1626

1627#if defined(CONFIG\_WIFI\_NM\_WPA\_SUPPLICANT)

1628/\* Make sure wifi\_drv\_ops is after wifi\_mgmt\_api \*/

1629BUILD\_ASSERT(offsetof(struct [net\_wifi\_mgmt\_offload](structnet__wifi__mgmt__offload.md), wifi\_mgmt\_api) <

1630 offsetof(struct [net\_wifi\_mgmt\_offload](structnet__wifi__mgmt__offload.md), wifi\_drv\_ops));

1631#endif

1632

1633/\* Make sure that the network interface API is properly setup inside

1634 \* Wifi mgmt offload API struct (it is the first one).

1635 \*/

1636BUILD\_ASSERT(offsetof(struct [net\_wifi\_mgmt\_offload](structnet__wifi__mgmt__offload.md), wifi\_iface) == 0);

1637

[ 1643](group__wifi__mgmt.md#ga036416696b1e3bc458ddbaf07a08d69d)void [wifi\_mgmt\_raise\_connect\_result\_event](group__wifi__mgmt.md#ga036416696b1e3bc458ddbaf07a08d69d)(struct [net\_if](structnet__if.md) \*iface, int status);

1644

[ 1650](group__wifi__mgmt.md#ga3b6edcf9b51afbf7a327d1a344bd7b87)void [wifi\_mgmt\_raise\_disconnect\_result\_event](group__wifi__mgmt.md#ga3b6edcf9b51afbf7a327d1a344bd7b87)(struct [net\_if](structnet__if.md) \*iface, int status);

1651

[ 1657](group__wifi__mgmt.md#ga7da6af0747bcba85f8afab30c92b5b43)void [wifi\_mgmt\_raise\_iface\_status\_event](group__wifi__mgmt.md#ga7da6af0747bcba85f8afab30c92b5b43)(struct [net\_if](structnet__if.md) \*iface,

1658 struct [wifi\_iface\_status](structwifi__iface__status.md) \*[iface\_status](structwifi__mgmt__ops.md#adf157476d776bc9c068e99e1a0266fd3));

1659

[ 1665](group__wifi__mgmt.md#ga39404d15243ca084b253cae8fc07e374)void [wifi\_mgmt\_raise\_twt\_event](group__wifi__mgmt.md#ga39404d15243ca084b253cae8fc07e374)(struct [net\_if](structnet__if.md) \*iface,

1666 struct [wifi\_twt\_params](structwifi__twt__params.md) \*twt\_params);

1667

[ 1673](group__wifi__mgmt.md#ga18f09a3196588b51d6c0644f82f639d7)void [wifi\_mgmt\_raise\_twt\_sleep\_state](group__wifi__mgmt.md#ga18f09a3196588b51d6c0644f82f639d7)(struct [net\_if](structnet__if.md) \*iface, int twt\_sleep\_state);

1674

1675#if defined(CONFIG\_WIFI\_MGMT\_RAW\_SCAN\_RESULTS) || defined(\_\_DOXYGEN\_\_)

[ 1681](group__wifi__mgmt.md#ga71c99913bded844c4ca32ed9155bc470)void [wifi\_mgmt\_raise\_raw\_scan\_result\_event](group__wifi__mgmt.md#ga71c99913bded844c4ca32ed9155bc470)(struct [net\_if](structnet__if.md) \*iface,

1682 struct [wifi\_raw\_scan\_result](structwifi__raw__scan__result.md) \*raw\_scan\_info);

1683#endif /\* CONFIG\_WIFI\_MGMT\_RAW\_SCAN\_RESULTS \*/

1684

[ 1690](group__wifi__mgmt.md#gaa75246d6dc55dada389c9d31e2607d5c)void [wifi\_mgmt\_raise\_disconnect\_complete\_event](group__wifi__mgmt.md#gaa75246d6dc55dada389c9d31e2607d5c)(struct [net\_if](structnet__if.md) \*iface, int status);

1691

1692#ifdef CONFIG\_WIFI\_NM\_WPA\_SUPPLICANT\_ROAMING

1699void wifi\_mgmt\_raise\_neighbor\_rep\_recv\_event(struct [net\_if](structnet__if.md) \*iface,

1700 char \*inbuf, size\_t buf\_len);

1701#endif

1702

[ 1708](group__wifi__mgmt.md#ga67b52edeff76c2211b038f4aa90b8982)void [wifi\_mgmt\_raise\_ap\_enable\_result\_event](group__wifi__mgmt.md#ga67b52edeff76c2211b038f4aa90b8982)(struct [net\_if](structnet__if.md) \*iface, enum [wifi\_ap\_status](group__wifi__mgmt.md#gaaf730bf76adc06434c7ac63bf0417884) status);

1709

[ 1715](group__wifi__mgmt.md#gadee15c6a492a8ee13bea43812debb5d9)void [wifi\_mgmt\_raise\_ap\_disable\_result\_event](group__wifi__mgmt.md#gadee15c6a492a8ee13bea43812debb5d9)(struct [net\_if](structnet__if.md) \*iface, enum [wifi\_ap\_status](group__wifi__mgmt.md#gaaf730bf76adc06434c7ac63bf0417884) status);

1716

[ 1722](group__wifi__mgmt.md#gac8f17f0aa3e426a5cdb731727b9b9ce3)void [wifi\_mgmt\_raise\_ap\_sta\_connected\_event](group__wifi__mgmt.md#gac8f17f0aa3e426a5cdb731727b9b9ce3)(struct [net\_if](structnet__if.md) \*iface,

1723 struct [wifi\_ap\_sta\_info](structwifi__ap__sta__info.md) \*sta\_info);

1724

[ 1729](group__wifi__mgmt.md#ga49fb9c3908be61d847b31c99be6afc42)void [wifi\_mgmt\_raise\_ap\_sta\_disconnected\_event](group__wifi__mgmt.md#ga49fb9c3908be61d847b31c99be6afc42)(struct [net\_if](structnet__if.md) \*iface,

1730 struct [wifi\_ap\_sta\_info](structwifi__ap__sta__info.md) \*sta\_info);

1731

1735#ifdef \_\_cplusplus

1736}

1737#endif

1738

1739#endif /\* ZEPHYR\_INCLUDE\_NET\_WIFI\_MGMT\_H\_ \*/

[ethernet.h](ethernet_8h.md)

Ethernet.

[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)

#define NET\_MGMT\_DEFINE\_REQUEST\_HANDLER(\_mgmt\_request)

Declare a request handler function for the given network event.

**Definition** net\_mgmt.h:129

[wifi\_mgmt\_raise\_connect\_result\_event](group__wifi__mgmt.md#ga036416696b1e3bc458ddbaf07a08d69d)

void wifi\_mgmt\_raise\_connect\_result\_event(struct net\_if \*iface, int status)

Wi-Fi management connect result event.

[wifi\_ext\_capab](group__wifi__mgmt.md#ga03ab29789adfe867c4ebaddc39482344)

wifi\_ext\_capab

**Definition** wifi\_mgmt.h:1287

[wifi\_sap\_iface\_state](group__wifi__mgmt.md#ga0cc87c00cbee0d0aca833119dbf0d74e)

wifi\_sap\_iface\_state

Wi-Fi AP status.

**Definition** wifi\_mgmt.h:1275

[wifi\_ps](group__wifi__mgmt.md#ga0fffeb57b68fb8cdef9d3d571368b8ca)

wifi\_ps

Wi-Fi power save states.

**Definition** wifi.h:441

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

**Definition** wifi.h:260

[wifi\_mfp\_options](group__wifi__mgmt.md#ga1f252da47d9650023d7fff6d08e49c76)

wifi\_mfp\_options

IEEE 802.11w - Management frame protection.

**Definition** wifi.h:239

[NET\_REQUEST\_WIFI\_RTS\_THRESHOLD](group__wifi__mgmt.md#ga22d80ef0ffb15e4286d7b1c3325d5334)

#define NET\_REQUEST\_WIFI\_RTS\_THRESHOLD

Request a Wi-Fi RTS threshold.

**Definition** wifi\_mgmt.h:259

[WIFI\_WPS\_PIN\_MAX\_LEN](group__wifi__mgmt.md#ga234d72d7c881e67ff49fb6c474c622e3)

#define WIFI\_WPS\_PIN\_MAX\_LEN

**Definition** wifi\_mgmt.h:1253

[NET\_REQUEST\_WIFI\_RTS\_THRESHOLD\_CONFIG](group__wifi__mgmt.md#ga2678ea372335af008d9bd3333f7a7de1)

#define NET\_REQUEST\_WIFI\_RTS\_THRESHOLD\_CONFIG

Request a Wi-Fi RTS threshold configuration.

**Definition** wifi\_mgmt.h:296

[WIFI\_MAC\_ADDR\_LEN](group__wifi__mgmt.md#ga29409ff83a53c6464decdde9bdd04de6)

#define WIFI\_MAC\_ADDR\_LEN

MAC address length.

**Definition** wifi.h:309

[NET\_REQUEST\_WIFI\_REG\_DOMAIN](group__wifi__mgmt.md#ga2b27d102b779a6d846b375854768fb7f)

#define NET\_REQUEST\_WIFI\_REG\_DOMAIN

Request a Wi-Fi regulatory domain.

**Definition** wifi\_mgmt.h:217

[wifi\_ps\_exit\_strategy](group__wifi__mgmt.md#ga2d424d1711389fb784e916a87ff854b7)

wifi\_ps\_exit\_strategy

Wi-Fi power save exit strategy.

**Definition** wifi.h:650

[NET\_REQUEST\_WIFI\_PACKET\_FILTER](group__wifi__mgmt.md#ga3098e817d12bf4619c9fd2698508fb4e)

#define NET\_REQUEST\_WIFI\_PACKET\_FILTER

Request Wi-Fi packet filter.

**Definition** wifi\_mgmt.h:229

[wifi\_twt\_setup\_cmd](group__wifi__mgmt.md#ga31c78afc89bfdc4b54cee177843f8022)

wifi\_twt\_setup\_cmd

Wi-Fi Target Wake Time (TWT) setup commands.

**Definition** wifi.h:523

[NET\_REQUEST\_WIFI\_NEIGHBOR\_REP\_COMPLETE](group__wifi__mgmt.md#ga373031970a29331bf1b30d1654c128f0)

#define NET\_REQUEST\_WIFI\_NEIGHBOR\_REP\_COMPLETE

**Definition** wifi\_mgmt.h:315

[wifi\_twt\_sleep\_state](group__wifi__mgmt.md#ga38c184ea35c02f304cccdf389ca6d552)

wifi\_twt\_sleep\_state

Wi-Fi TWT sleep states.

**Definition** wifi\_mgmt.h:953

[WIFI\_BTWT\_AGREEMENT\_MAX](group__wifi__mgmt.md#ga38d92ba342887e46c957b820d89a7a20)

#define WIFI\_BTWT\_AGREEMENT\_MAX

**Definition** wifi\_mgmt.h:734

[wifi\_mgmt\_raise\_twt\_event](group__wifi__mgmt.md#ga39404d15243ca084b253cae8fc07e374)

void wifi\_mgmt\_raise\_twt\_event(struct net\_if \*iface, struct wifi\_twt\_params \*twt\_params)

Wi-Fi management TWT event.

[wifi\_frequency\_bandwidths](group__wifi__mgmt.md#ga3b01cead3c2eb4581fe85e2aaaffbd49)

wifi\_frequency\_bandwidths

IEEE 802.11 operational frequency bandwidths (not exhaustive).

**Definition** wifi.h:282

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

**Definition** wifi.h:145

[wifi\_mgmt\_raise\_ap\_sta\_disconnected\_event](group__wifi__mgmt.md#ga49fb9c3908be61d847b31c99be6afc42)

void wifi\_mgmt\_raise\_ap\_sta\_disconnected\_event(struct net\_if \*iface, struct wifi\_ap\_sta\_info \*sta\_info)

Wi-Fi management AP mode STA disconnected event.

[NET\_REQUEST\_WIFI\_11K\_NEIGHBOR\_REQUEST](group__wifi__mgmt.md#ga4a2b1e8befd7376749b1d4fbcf98376f)

#define NET\_REQUEST\_WIFI\_11K\_NEIGHBOR\_REQUEST

**Definition** wifi\_mgmt.h:188

[wifi\_wps\_op](group__wifi__mgmt.md#ga4c36ae1a5171d3fbaeebf95c16be496d)

wifi\_wps\_op

Operation for WPS.

**Definition** wifi\_mgmt.h:1256

[wifi\_twt\_setup\_resp\_status](group__wifi__mgmt.md#ga4d03aedac13ee4512d7717ac624f319a)

wifi\_twt\_setup\_resp\_status

Wi-Fi Target Wake Time (TWT) negotiation status.

**Definition** wifi.h:546

[NET\_REQUEST\_WIFI\_BTM\_QUERY](group__wifi__mgmt.md#ga4f644b4c980628ffd556458eddc0933d)

#define NET\_REQUEST\_WIFI\_BTM\_QUERY

Request a Wi-Fi BTM query.

**Definition** wifi\_mgmt.h:279

[wifi\_iface\_mode](group__wifi__mgmt.md#ga584f6239ac14e2bedc5e6bd72756423b)

wifi\_iface\_mode

Wi-Fi interface modes.

**Definition** wifi.h:374

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

**Definition** wifi.h:510

[wifi\_mgmt\_raise\_raw\_scan\_result\_event](group__wifi__mgmt.md#ga71c99913bded844c4ca32ed9155bc470)

void wifi\_mgmt\_raise\_raw\_scan\_result\_event(struct net\_if \*iface, struct wifi\_raw\_scan\_result \*raw\_scan\_info)

Wi-Fi management raw scan result event.

[wifi\_mgmt\_raise\_iface\_status\_event](group__wifi__mgmt.md#ga7da6af0747bcba85f8afab30c92b5b43)

void wifi\_mgmt\_raise\_iface\_status\_event(struct net\_if \*iface, struct wifi\_iface\_status \*iface\_status)

Wi-Fi management interface status event.

[wifi\_ap\_config\_param](group__wifi__mgmt.md#ga83546cf946a9123c563609e8903d9642)

wifi\_ap\_config\_param

Wi-Fi AP mode configuration parameter.

**Definition** wifi.h:725

[wifi\_conn\_status](group__wifi__mgmt.md#ga86a5741e54aeb3e290142b0de217b8a8)

wifi\_conn\_status

Wi-Fi connect result codes.

**Definition** wifi.h:44

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

**Definition** wifi.h:554

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

**Definition** wifi\_mgmt.h:638

[NET\_REQUEST\_WIFI\_TWT](group__wifi__mgmt.md#gab84fd7e9ca0bf0b2b9d08889dda26aad)

#define NET\_REQUEST\_WIFI\_TWT

Request a Wi-Fi TWT.

**Definition** wifi\_mgmt.h:200

[wifi\_link\_mode](group__wifi__mgmt.md#gabdb2a784d4727b71ab44cca04e422c62)

wifi\_link\_mode

Wi-Fi link operating modes.

**Definition** wifi.h:402

[wifi\_ps\_param\_type](group__wifi__mgmt.md#gabe45d132797047c098041331c8f6f912)

wifi\_ps\_param\_type

Wi-Fi power save parameters.

**Definition** wifi.h:621

[net\_event\_wifi\_cmd](group__wifi__mgmt.md#gac2638308cbb0d268831f1618cf8e1fa8)

net\_event\_wifi\_cmd

Wi-Fi management events.

**Definition** wifi\_mgmt.h:350

[NET\_REQUEST\_WIFI\_CONN\_PARAMS](group__wifi__mgmt.md#gac6483341435ff380a2d4a69430899c1a)

#define NET\_REQUEST\_WIFI\_CONN\_PARAMS

Request a Wi-Fi connection parameters.

**Definition** wifi\_mgmt.h:253

[wifi\_disconn\_reason](group__wifi__mgmt.md#gac782af0a60b202fd19597cabb7bd3a9a)

wifi\_disconn\_reason

Wi-Fi disconnect reason codes.

**Definition** wifi\_mgmt.h:622

[wifi\_ps\_wakeup\_mode](group__wifi__mgmt.md#gac7f907644847e905d67c709fa4afae7f)

wifi\_ps\_wakeup\_mode

Wi-Fi power save modes.

**Definition** wifi.h:637

[wifi\_mgmt\_raise\_ap\_sta\_connected\_event](group__wifi__mgmt.md#gac8f17f0aa3e426a5cdb731727b9b9ce3)

void wifi\_mgmt\_raise\_ap\_sta\_connected\_event(struct net\_if \*iface, struct wifi\_ap\_sta\_info \*sta\_info)

Wi-Fi management AP mode STA connected event.

[wifi\_twt\_operation](group__wifi__mgmt.md#gad0e998aeb1b27c4f203ca76339d323a3)

wifi\_twt\_operation

Wi-Fi Target Wake Time (TWT) operations.

**Definition** wifi.h:499

[wifi\_scan\_type](group__wifi__mgmt.md#gad30e29eda65ccafdbd7f11865937b8ea)

wifi\_scan\_type

Wi-Fi scanning types.

**Definition** wifi.h:433

[scan\_result\_cb\_t](group__wifi__mgmt.md#gad34b366f1c315207ce0da587ca96d8d8)

void(\* scan\_result\_cb\_t)(struct net\_if \*iface, int status, struct wifi\_scan\_result \*entry)

Scan result callback.

**Definition** wifi\_mgmt.h:1303

[wifi\_twt\_teardown\_status](group__wifi__mgmt.md#gad3709d07aaa3ed59b48f9dd7bd181989)

wifi\_twt\_teardown\_status

Wi-Fi Target Wake Time (TWT) teradown status.

**Definition** wifi.h:580

[WIFI\_SSID\_MAX\_LEN](group__wifi__mgmt.md#gad62c60666c9fdffe2e0e9c4388f87886)

#define WIFI\_SSID\_MAX\_LEN

Max SSID length.

**Definition** wifi.h:301

[NET\_REQUEST\_WIFI\_CHANNEL](group__wifi__mgmt.md#gad9614d2368f8399850aaec05e40bdc78)

#define NET\_REQUEST\_WIFI\_CHANNEL

Request a Wi-Fi channel.

**Definition** wifi\_mgmt.h:235

[wifi\_config\_ps\_param\_fail\_reason](group__wifi__mgmt.md#gad98099584d2222ede93aba42b1fbaff0)

wifi\_config\_ps\_param\_fail\_reason

Wi-Fi power save error codes.

**Definition** wifi.h:666

[NET\_REQUEST\_WIFI\_11K\_CONFIG](group__wifi__mgmt.md#gadd9b5b206c7ee2e40c30a37c7b4fc002)

#define NET\_REQUEST\_WIFI\_11K\_CONFIG

**Definition** wifi\_mgmt.h:183

[wifi\_security\_type](group__wifi__mgmt.md#gadde31a04fa25ed805115c6b31854cd9c)

wifi\_security\_type

IEEE 802.11 security types.

**Definition** wifi.h:69

[wifi\_mgmt\_raise\_ap\_disable\_result\_event](group__wifi__mgmt.md#gadee15c6a492a8ee13bea43812debb5d9)

void wifi\_mgmt\_raise\_ap\_disable\_result\_event(struct net\_if \*iface, enum wifi\_ap\_status status)

Wi-Fi management AP mode disable result event.

[wifi\_mgmt\_op](group__wifi__mgmt.md#gae129d0783276e662575af2314eef86cd)

wifi\_mgmt\_op

Generic get/set operation for any command.

**Definition** wifi\_mgmt.h:902

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

**Definition** wifi.h:452

[WIFI\_EXT\_CAPAB\_GLK](group__wifi__mgmt.md#gga03ab29789adfe867c4ebaddc39482344a1363c1318e4281e057d848194396feb7)

@ WIFI\_EXT\_CAPAB\_GLK

**Definition** wifi\_mgmt.h:1289

[WIFI\_EXT\_CAPAB\_20\_40\_COEX](group__wifi__mgmt.md#gga03ab29789adfe867c4ebaddc39482344abf275508c3f69321cdf704779e976d68)

@ WIFI\_EXT\_CAPAB\_20\_40\_COEX

**Definition** wifi\_mgmt.h:1288

[WIFI\_EXT\_CAPAB\_BSS\_TRANSITION](group__wifi__mgmt.md#gga03ab29789adfe867c4ebaddc39482344ac5c648efedadc82fae7d9e0851ff71ba)

@ WIFI\_EXT\_CAPAB\_BSS\_TRANSITION

**Definition** wifi\_mgmt.h:1292

[WIFI\_EXT\_CAPAB\_EXT\_CHAN\_SWITCH](group__wifi__mgmt.md#gga03ab29789adfe867c4ebaddc39482344acf854adfca2bb41dd5d75df2b16c3e5e)

@ WIFI\_EXT\_CAPAB\_EXT\_CHAN\_SWITCH

**Definition** wifi\_mgmt.h:1290

[WIFI\_EXT\_CAPAB\_TIM\_BROADCAST](group__wifi__mgmt.md#gga03ab29789adfe867c4ebaddc39482344af42762fd723afef7fae98cbefbfff056)

@ WIFI\_EXT\_CAPAB\_TIM\_BROADCAST

**Definition** wifi\_mgmt.h:1291

[WIFI\_SAP\_IFACE\_COUNTRY\_UPDATE](group__wifi__mgmt.md#gga0cc87c00cbee0d0aca833119dbf0d74ea403d84f907f84492eed8e33713e828ae)

@ WIFI\_SAP\_IFACE\_COUNTRY\_UPDATE

**Definition** wifi\_mgmt.h:1278

[WIFI\_SAP\_IFACE\_DISABLED](group__wifi__mgmt.md#gga0cc87c00cbee0d0aca833119dbf0d74ea59a8530057e9839d89243558cc366d69)

@ WIFI\_SAP\_IFACE\_DISABLED

**Definition** wifi\_mgmt.h:1277

[WIFI\_SAP\_IFACE\_HT\_SCAN](group__wifi__mgmt.md#gga0cc87c00cbee0d0aca833119dbf0d74eaa3a6e6e367c7384379f3c562d1fc358f)

@ WIFI\_SAP\_IFACE\_HT\_SCAN

**Definition** wifi\_mgmt.h:1280

[WIFI\_SAP\_IFACE\_ENABLED](group__wifi__mgmt.md#gga0cc87c00cbee0d0aca833119dbf0d74eaa9133b73b886f2ec543acd282b33eeda)

@ WIFI\_SAP\_IFACE\_ENABLED

**Definition** wifi\_mgmt.h:1283

[WIFI\_SAP\_IFACE\_ACS](group__wifi__mgmt.md#gga0cc87c00cbee0d0aca833119dbf0d74eab3fea1a0ef90043699cb7d8ab064be7e)

@ WIFI\_SAP\_IFACE\_ACS

**Definition** wifi\_mgmt.h:1279

[WIFI\_SAP\_IFACE\_UNINITIALIZED](group__wifi__mgmt.md#gga0cc87c00cbee0d0aca833119dbf0d74ead92795c629fe828e7efde485eb2761c0)

@ WIFI\_SAP\_IFACE\_UNINITIALIZED

**Definition** wifi\_mgmt.h:1276

[WIFI\_SAP\_IFACE\_NO\_IR](group__wifi__mgmt.md#gga0cc87c00cbee0d0aca833119dbf0d74eaea74f039e6a5abe976e9956b5a01ff1a)

@ WIFI\_SAP\_IFACE\_NO\_IR

**Definition** wifi\_mgmt.h:1282

[WIFI\_SAP\_IFACE\_DFS](group__wifi__mgmt.md#gga0cc87c00cbee0d0aca833119dbf0d74eafdf99a461cf5878240cc40ae4ea7e113)

@ WIFI\_SAP\_IFACE\_DFS

**Definition** wifi\_mgmt.h:1281

[WIFI\_TWT\_STATE\_SLEEP](group__wifi__mgmt.md#gga38c184ea35c02f304cccdf389ca6d552a37a7aba20723b6614e39e1c417f3113c)

@ WIFI\_TWT\_STATE\_SLEEP

TWT sleep state: sleeping.

**Definition** wifi\_mgmt.h:955

[WIFI\_TWT\_STATE\_AWAKE](group__wifi__mgmt.md#gga38c184ea35c02f304cccdf389ca6d552a7b7b45f85d9644f897ca00bd7864e1b0)

@ WIFI\_TWT\_STATE\_AWAKE

TWT sleep state: awake.

**Definition** wifi\_mgmt.h:957

[WIFI\_WPS\_PBC](group__wifi__mgmt.md#gga4c36ae1a5171d3fbaeebf95c16be496da093f5b3ef95d9e571ea169430da57e88)

@ WIFI\_WPS\_PBC

WPS pbc.

**Definition** wifi\_mgmt.h:1258

[WIFI\_WPS\_PIN\_SET](group__wifi__mgmt.md#gga4c36ae1a5171d3fbaeebf95c16be496da58120620fd2fca80bdac7990ed0e7552)

@ WIFI\_WPS\_PIN\_SET

Set WPS pin number.

**Definition** wifi\_mgmt.h:1262

[WIFI\_WPS\_PIN\_GET](group__wifi__mgmt.md#gga4c36ae1a5171d3fbaeebf95c16be496da75bd5067903c2bba8a06732f0431393d)

@ WIFI\_WPS\_PIN\_GET

Get WPS pin number.

**Definition** wifi\_mgmt.h:1260

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

**Definition** wifi\_mgmt.h:646

[WIFI\_STATUS\_AP\_SUCCESS](group__wifi__mgmt.md#ggaaf730bf76adc06434c7ac63bf0417884a0df52848da8735892d0eb1e381b2cd7c)

@ WIFI\_STATUS\_AP\_SUCCESS

AP mode enable or disable successful.

**Definition** wifi\_mgmt.h:640

[WIFI\_STATUS\_AP\_OP\_NOT\_SUPPORTED](group__wifi__mgmt.md#ggaaf730bf76adc06434c7ac63bf0417884a2105e6c49b3bcb5f7dcacbc1e5ce9cca)

@ WIFI\_STATUS\_AP\_OP\_NOT\_SUPPORTED

AP mode enable failed - operation not supported.

**Definition** wifi\_mgmt.h:652

[WIFI\_STATUS\_AP\_OP\_NOT\_PERMITTED](group__wifi__mgmt.md#ggaaf730bf76adc06434c7ac63bf0417884a36a58980bdc7877c910441590137ddbe)

@ WIFI\_STATUS\_AP\_OP\_NOT\_PERMITTED

AP mode enable failed - operation not permitted.

**Definition** wifi\_mgmt.h:654

[WIFI\_STATUS\_AP\_CHANNEL\_NOT\_SUPPORTED](group__wifi__mgmt.md#ggaaf730bf76adc06434c7ac63bf0417884a5acb85a2361ca72ed10966b829c5753b)

@ WIFI\_STATUS\_AP\_CHANNEL\_NOT\_SUPPORTED

AP mode enable failed - channel not supported.

**Definition** wifi\_mgmt.h:644

[WIFI\_STATUS\_AP\_FAIL](group__wifi__mgmt.md#ggaaf730bf76adc06434c7ac63bf0417884a6c6801381caa3862004662169202fa9a)

@ WIFI\_STATUS\_AP\_FAIL

AP mode enable or disable failed - generic failure.

**Definition** wifi\_mgmt.h:642

[WIFI\_STATUS\_AP\_AUTH\_TYPE\_NOT\_SUPPORTED](group__wifi__mgmt.md#ggaaf730bf76adc06434c7ac63bf0417884abe5a626d22051522255d98fdfdfbfcc8)

@ WIFI\_STATUS\_AP\_AUTH\_TYPE\_NOT\_SUPPORTED

AP mode enable failed - authentication type not supported.

**Definition** wifi\_mgmt.h:650

[WIFI\_STATUS\_AP\_SSID\_NOT\_ALLOWED](group__wifi__mgmt.md#ggaaf730bf76adc06434c7ac63bf0417884ac18a7b551f8c6bb7737b0e8e60c323ce)

@ WIFI\_STATUS\_AP\_SSID\_NOT\_ALLOWED

AP mode enable failed - SSID not allowed.

**Definition** wifi\_mgmt.h:648

[NET\_MGMT\_CMD](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8ae731884669e9ee832e36b8280e9c58c6)

@ NET\_MGMT\_CMD

Scan results available.

**Definition** wifi\_mgmt.h:352

[WIFI\_REASON\_DISCONN\_INACTIVITY](group__wifi__mgmt.md#ggac782af0a60b202fd19597cabb7bd3a9aa05fe2f87de30de47ee48f7615c2206e6)

@ WIFI\_REASON\_DISCONN\_INACTIVITY

Disconnected due to inactivity.

**Definition** wifi\_mgmt.h:632

[WIFI\_REASON\_DISCONN\_AP\_LEAVING](group__wifi__mgmt.md#ggac782af0a60b202fd19597cabb7bd3a9aa34e3f78ce43db3daeaf32038e0baf204)

@ WIFI\_REASON\_DISCONN\_AP\_LEAVING

Disconnected due to AP leaving.

**Definition** wifi\_mgmt.h:630

[WIFI\_REASON\_DISCONN\_SUCCESS](group__wifi__mgmt.md#ggac782af0a60b202fd19597cabb7bd3a9aa5c894399db8949a789ca4f5750b6f042)

@ WIFI\_REASON\_DISCONN\_SUCCESS

Success, overload status as reason.

**Definition** wifi\_mgmt.h:624

[WIFI\_REASON\_DISCONN\_UNSPECIFIED](group__wifi__mgmt.md#ggac782af0a60b202fd19597cabb7bd3a9aa87f5d64a9fd3acf8d67c698199779e5c)

@ WIFI\_REASON\_DISCONN\_UNSPECIFIED

Unspecified reason.

**Definition** wifi\_mgmt.h:626

[WIFI\_REASON\_DISCONN\_USER\_REQUEST](group__wifi__mgmt.md#ggac782af0a60b202fd19597cabb7bd3a9aaee75adafb52bd6ecaa547a76c6ccd0a7)

@ WIFI\_REASON\_DISCONN\_USER\_REQUEST

Disconnected due to user request.

**Definition** wifi\_mgmt.h:628

[WIFI\_MGMT\_GET](group__wifi__mgmt.md#ggae129d0783276e662575af2314eef86cda6b8183a773e0cdfa85bc4b41ae70fdcd)

@ WIFI\_MGMT\_GET

Get operation.

**Definition** wifi\_mgmt.h:904

[WIFI\_MGMT\_SET](group__wifi__mgmt.md#ggae129d0783276e662575af2314eef86cdaa0d5931c8275a8d3288ab668b6dfb5a1)

@ WIFI\_MGMT\_SET

Set operation.

**Definition** wifi\_mgmt.h:906

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

**Definition** device.h:510

[ethernet\_api](structethernet__api.md)

Ethernet L2 API operations.

**Definition** ethernet.h:518

[net\_if](structnet__if.md)

Network Interface structure.

**Definition** net\_if.h:726

[net\_stats\_wifi](structnet__stats__wifi.md)

All Wi-Fi specific statistics.

**Definition** net\_stats.h:705

[net\_wifi\_mgmt\_offload](structnet__wifi__mgmt__offload.md)

Wi-Fi management offload API.

**Definition** wifi\_mgmt.h:1604

[net\_wifi\_mgmt\_offload::wifi\_iface](structnet__wifi__mgmt__offload.md#a1d34a954a2f16d29f51dc51dd6fbb845)

struct ethernet\_api wifi\_iface

Mandatory to get in first position.

**Definition** wifi\_mgmt.h:1613

[net\_wifi\_mgmt\_offload::wifi\_mgmt\_api](structnet__wifi__mgmt__offload.md#a98fcc053d9820d2d981ed659520c9b3b)

const struct wifi\_mgmt\_ops \*const wifi\_mgmt\_api

Wi-Fi management API.

**Definition** wifi\_mgmt.h:1619

[net\_wifi\_mgmt\_offload::wifi\_drv\_ops](structnet__wifi__mgmt__offload.md#a991e0bc6247578a3d1c9d2d3ab0b63d7)

const void \* wifi\_drv\_ops

Wi-Fi supplicant driver API.

**Definition** wifi\_mgmt.h:1623

[offloaded\_if\_api](structoffloaded__if__api.md)

Extended net\_if\_api for offloaded ifaces/network devices, allowing handling of admin up/down state ch...

**Definition** offloaded\_netdev.h:53

[wifi\_11k\_params](structwifi__11k__params.md)

Wi-Fi 11k parameters.

**Definition** wifi\_mgmt.h:910

[wifi\_11k\_params::ssid](structwifi__11k__params.md#a64ace23c71837417678ceb9cc8d5f216)

uint8\_t ssid[WIFI\_SSID\_MAX\_LEN+1]

SSID.

**Definition** wifi\_mgmt.h:916

[wifi\_11k\_params::enable\_11k](structwifi__11k__params.md#a739c3e94b025aae2fcf5680aecf3d646)

bool enable\_11k

11k enable/disable

**Definition** wifi\_mgmt.h:914

[wifi\_11k\_params::oper](structwifi__11k__params.md#ae6029ed4bada41f18df0329d0da7401e)

enum wifi\_mgmt\_op oper

11k command operation

**Definition** wifi\_mgmt.h:912

[wifi\_ap\_config\_params](structwifi__ap__config__params.md)

Wi-Fi AP configuration parameter.

**Definition** wifi\_mgmt.h:1040

[wifi\_ap\_config\_params::max\_inactivity](structwifi__ap__config__params.md#a289866d9209450e893281b4c198a546a)

uint32\_t max\_inactivity

Parameter used for setting maximum inactivity duration for stations.

**Definition** wifi\_mgmt.h:1044

[wifi\_ap\_config\_params::type](structwifi__ap__config__params.md#a4c391cf504a994ed0bc4971afdf76774)

enum wifi\_ap\_config\_param type

Parameter used to identify the different AP parameters.

**Definition** wifi\_mgmt.h:1042

[wifi\_ap\_config\_params::max\_num\_sta](structwifi__ap__config__params.md#a7fc0fad99f53ed8e1ac40b74ec98bf9a)

uint32\_t max\_num\_sta

Parameter used for setting maximum number of stations.

**Definition** wifi\_mgmt.h:1046

[wifi\_ap\_config\_params::bandwidth](structwifi__ap__config__params.md#aba4e43dff01fa026c8dbbfff670d3097)

enum wifi\_frequency\_bandwidths bandwidth

Parameter used for frequency band.

**Definition** wifi\_mgmt.h:1048

[wifi\_ap\_sta\_info](structwifi__ap__sta__info.md)

AP mode - connected STA details.

**Definition** wifi\_mgmt.h:975

[wifi\_ap\_sta\_info::link\_mode](structwifi__ap__sta__info.md#a7d8bd52340d4937a4b5b7d2c00662441)

enum wifi\_link\_mode link\_mode

Link mode, see enum wifi\_link\_mode.

**Definition** wifi\_mgmt.h:977

[wifi\_ap\_sta\_info::mac](structwifi__ap__sta__info.md#a7db904376ec73b774aa9d8236c15b3f6)

uint8\_t mac[WIFI\_MAC\_ADDR\_LEN]

MAC address.

**Definition** wifi\_mgmt.h:979

[wifi\_ap\_sta\_info::mac\_length](structwifi__ap__sta__info.md#a7f7c8b144bb3464af5213708591eefda)

uint8\_t mac\_length

MAC address length.

**Definition** wifi\_mgmt.h:981

[wifi\_ap\_sta\_info::twt\_capable](structwifi__ap__sta__info.md#a838c9a4288c9bc7e97afe2334c678f34)

bool twt\_capable

is TWT capable ?

**Definition** wifi\_mgmt.h:983

[wifi\_band\_channel](structwifi__band__channel.md)

Wi-Fi structure to uniquely identify a band-channel pair.

**Definition** wifi\_mgmt.h:460

[wifi\_band\_channel::band](structwifi__band__channel.md#a4a932599429f37231f76c3064ec5efb3)

uint8\_t band

Frequency band.

**Definition** wifi\_mgmt.h:462

[wifi\_band\_channel::channel](structwifi__band__channel.md#acd0dd7366de3650124dad7232a58ade0)

uint8\_t channel

Channel.

**Definition** wifi\_mgmt.h:464

[wifi\_btwt\_params](structwifi__btwt__params.md)

Wi-Fi broadcast TWT parameters.

**Definition** wifi\_mgmt.h:737

[wifi\_btwt\_params::btwt\_nominal\_wake](structwifi__btwt__params.md#a0192d3a9334fc55a135206e6b74ea5b5)

uint8\_t btwt\_nominal\_wake

Broadcast TWT range.

**Definition** wifi\_mgmt.h:745

[wifi\_btwt\_params::btwt\_mantissa](structwifi__btwt__params.md#a2c1b3551a714fbf1b948ce4bcf805934)

uint16\_t btwt\_mantissa

Broadcast TWT mantissa.

**Definition** wifi\_mgmt.h:741

[wifi\_btwt\_params::btwt\_exponent](structwifi__btwt__params.md#a76c97bcc132405d6a1a54bcca77054ac)

uint8\_t btwt\_exponent

Broadcast TWT exponent.

**Definition** wifi\_mgmt.h:743

[wifi\_btwt\_params::btwt\_id](structwifi__btwt__params.md#ae52281d9f53e106fb9ed813131d8085e)

uint8\_t btwt\_id

Broadcast TWT ID.

**Definition** wifi\_mgmt.h:739

[wifi\_channel\_info](structwifi__channel__info.md)

Wi-Fi channel setting for monitor and TX-injection modes.

**Definition** wifi\_mgmt.h:1025

[wifi\_channel\_info::if\_index](structwifi__channel__info.md#a43a7dd8c19d0c6540e3cc0b5d1d6165d)

uint8\_t if\_index

Interface index.

**Definition** wifi\_mgmt.h:1029

[wifi\_channel\_info::channel](structwifi__channel__info.md#a799cbc0a67764f6680322ba0f2ad3300)

uint16\_t channel

Channel value to set.

**Definition** wifi\_mgmt.h:1027

[wifi\_channel\_info::oper](structwifi__channel__info.md#aa8ef8a71b49ead3664fff9a4d61b1ce8)

enum wifi\_mgmt\_op oper

Get or set operation.

**Definition** wifi\_mgmt.h:1031

[wifi\_connect\_req\_params](structwifi__connect__req__params.md)

Wi-Fi connect request parameters.

**Definition** wifi\_mgmt.h:546

[wifi\_connect\_req\_params::key2\_passwd](structwifi__connect__req__params.md#a020fc58d7e5350cc803cd5d6fa575e6a)

const uint8\_t \* key2\_passwd

private key2 passwd

**Definition** wifi\_mgmt.h:580

[wifi\_connect\_req\_params::ft\_used](structwifi__connect__req__params.md#a047b11e703fb646d778785dfcb14257b)

bool ft\_used

Fast BSS Transition used.

**Definition** wifi\_mgmt.h:600

[wifi\_connect\_req\_params::bandwidth](structwifi__connect__req__params.md#a0d44c86d9b9528041bbe7534e0c7597a)

enum wifi\_frequency\_bandwidths bandwidth

Parameter used for frequency band.

**Definition** wifi\_mgmt.h:616

[wifi\_connect\_req\_params::security](structwifi__connect__req__params.md#a18dce6bb021086877a30e7a04f5b24b9)

enum wifi\_security\_type security

Security type.

**Definition** wifi\_mgmt.h:564

[wifi\_connect\_req\_params::passwords](structwifi__connect__req__params.md#a2163b50b6d466663404e1cb21ce6ae5d)

const uint8\_t \* passwords[WIFI\_ENT\_IDENTITY\_MAX\_USERS]

User Passwords.

**Definition** wifi\_mgmt.h:608

[wifi\_connect\_req\_params::identities](structwifi__connect__req__params.md#a265001d2309840d04bdca507896255d0)

const uint8\_t \* identities[WIFI\_ENT\_IDENTITY\_MAX\_USERS]

User Identities.

**Definition** wifi\_mgmt.h:606

[wifi\_connect\_req\_params::aid\_length](structwifi__connect__req__params.md#a2892253024b70e5cb8eb2166b17ebe22)

uint8\_t aid\_length

anon\_id length, max 64

**Definition** wifi\_mgmt.h:574

[wifi\_connect\_req\_params::sae\_password](structwifi__connect__req__params.md#a469fac5758b78fc425911837930b2060)

const uint8\_t \* sae\_password

SAE password (same as PSK but with no length restrictions), optional.

**Definition** wifi\_mgmt.h:556

[wifi\_connect\_req\_params::key\_passwd](structwifi__connect__req__params.md#a4946647659a347667ee49bb6990bba66)

const uint8\_t \* key\_passwd

Private key passwd for enterprise mode.

**Definition** wifi\_mgmt.h:576

[wifi\_connect\_req\_params::eap\_id\_length](structwifi__connect__req__params.md#a4da02ff112c09f55dc5bddcda27d16a3)

uint8\_t eap\_id\_length

eap identity length, max 64

**Definition** wifi\_mgmt.h:592

[wifi\_connect\_req\_params::channel](structwifi__connect__req__params.md#a52b6d0323c35d03ec239f40be35cae72)

uint8\_t channel

Channel.

**Definition** wifi\_mgmt.h:562

[wifi\_connect\_req\_params::ssid\_length](structwifi__connect__req__params.md#a547dddf6be5dd77eda74b1085a798400)

uint8\_t ssid\_length

SSID length.

**Definition** wifi\_mgmt.h:550

[wifi\_connect\_req\_params::timeout](structwifi__connect__req__params.md#a56183ba7f4d8eaf5fc5b495856adecfd)

int timeout

Connect timeout in seconds, SYS\_FOREVER\_MS for no timeout.

**Definition** wifi\_mgmt.h:570

[wifi\_connect\_req\_params::nusers](structwifi__connect__req__params.md#a71770c2f2da378db2efedaa87b141627)

int nusers

Number of EAP users.

**Definition** wifi\_mgmt.h:602

[wifi\_connect\_req\_params::mfp](structwifi__connect__req__params.md#a745b3416172672a7e5b12bcc5b55e88c)

enum wifi\_mfp\_options mfp

MFP options.

**Definition** wifi\_mgmt.h:566

[wifi\_connect\_req\_params::sae\_password\_length](structwifi__connect__req__params.md#a74f0819e7a546ffb8bfb0ec587eccf20)

uint8\_t sae\_password\_length

SAE password length.

**Definition** wifi\_mgmt.h:558

[wifi\_connect\_req\_params::anon\_id](structwifi__connect__req__params.md#a781456e079357e2e1096218af3bd218c)

const uint8\_t \* anon\_id

anonymous identity

**Definition** wifi\_mgmt.h:572

[wifi\_connect\_req\_params::eap\_ver](structwifi__connect__req__params.md#a8c8ecb1ef0fe3f2f4c04a7a8eeccbbdf)

int eap\_ver

eap version

**Definition** wifi\_mgmt.h:588

[wifi\_connect\_req\_params::key\_passwd\_length](structwifi__connect__req__params.md#a9f913fc0ccecafaba488e444d701fd68)

uint8\_t key\_passwd\_length

Private key passwd length, max 128.

**Definition** wifi\_mgmt.h:578

[wifi\_connect\_req\_params::band](structwifi__connect__req__params.md#aa2fea1881a8ffdf5d7093ae295867f3e)

uint8\_t band

Frequency band.

**Definition** wifi\_mgmt.h:560

[wifi\_connect\_req\_params::TLS\_cipher](structwifi__connect__req__params.md#aa4577535a27b8d54d9b8c7543d359ade)

uint8\_t TLS\_cipher

TLS cipher.

**Definition** wifi\_mgmt.h:586

[wifi\_connect\_req\_params::psk](structwifi__connect__req__params.md#aa7743f0ecbc27a9595720ce13ce57c1d)

const uint8\_t \* psk

Pre-shared key.

**Definition** wifi\_mgmt.h:552

[wifi\_connect\_req\_params::bssid](structwifi__connect__req__params.md#aa8081b9075ff9244cefd0ac1ef3f42cb)

uint8\_t bssid[WIFI\_MAC\_ADDR\_LEN]

BSSID.

**Definition** wifi\_mgmt.h:568

[wifi\_connect\_req\_params::verify\_peer\_cert](structwifi__connect__req__params.md#aa8f18ace96e471eb0bc8bff8d8146f6f)

bool verify\_peer\_cert

Whether verify peer with CA or not: false-not verify, true-verify.

**Definition** wifi\_mgmt.h:598

[wifi\_connect\_req\_params::passwds](structwifi__connect__req__params.md#aaf071a51c7281e4d42197f266c729c04)

uint8\_t passwds

Number of EAP passwds.

**Definition** wifi\_mgmt.h:604

[wifi\_connect\_req\_params::psk\_length](structwifi__connect__req__params.md#aaf7455a65590d19f047214b459a2dcb9)

uint8\_t psk\_length

Pre-shared key length.

**Definition** wifi\_mgmt.h:554

[wifi\_connect\_req\_params::eap\_identity](structwifi__connect__req__params.md#ab9c65599409387af65a3c2895c3116da)

const uint8\_t \* eap\_identity

Identity for EAP.

**Definition** wifi\_mgmt.h:590

[wifi\_connect\_req\_params::ssid](structwifi__connect__req__params.md#ac260c2cd17a3f36ea101edaf23d41083)

const uint8\_t \* ssid

SSID.

**Definition** wifi\_mgmt.h:548

[wifi\_connect\_req\_params::wpa3\_ent\_mode](structwifi__connect__req__params.md#ae0b94d870ecbee0b203caee6a6e3d8b2)

enum wifi\_wpa3\_enterprise\_type wpa3\_ent\_mode

wpa3 enterprise mode

**Definition** wifi\_mgmt.h:584

[wifi\_connect\_req\_params::eap\_passwd\_length](structwifi__connect__req__params.md#aeab22e95a04a1831b87beda1772d3db7)

uint8\_t eap\_passwd\_length

eap passwd length, max 128

**Definition** wifi\_mgmt.h:596

[wifi\_connect\_req\_params::key2\_passwd\_length](structwifi__connect__req__params.md#af7b163cc2bffc59f7fa31f47c5e52062)

uint8\_t key2\_passwd\_length

key2 passwd length, max 128

**Definition** wifi\_mgmt.h:582

[wifi\_connect\_req\_params::ignore\_broadcast\_ssid](structwifi__connect__req__params.md#afac70366e509301f9a27ca51be30b88d)

uint8\_t ignore\_broadcast\_ssid

Hidden SSID configure 0: disabled (default) 1: send empty (length=0) SSID in beacon and ignore probe ...

**Definition** wifi\_mgmt.h:614

[wifi\_connect\_req\_params::eap\_password](structwifi__connect__req__params.md#afd046e702739c4a0d89322ee41b37acd)

const uint8\_t \* eap\_password

Password string for EAP.

**Definition** wifi\_mgmt.h:594

[wifi\_enterprise\_creds\_params](structwifi__enterprise__creds__params.md)

Wi-Fi enterprise mode credentials.

**Definition** wifi\_mgmt.h:852

[wifi\_enterprise\_creds\_params::client\_key\_len](structwifi__enterprise__creds__params.md#a09f5b34c81fe871e7513358499518d95)

uint32\_t client\_key\_len

Client key length.

**Definition** wifi\_mgmt.h:864

[wifi\_enterprise\_creds\_params::client\_cert2](structwifi__enterprise__creds__params.md#a133126e338d89563733268a03e2fa613)

uint8\_t \* client\_cert2

Client certification of phase2.

**Definition** wifi\_mgmt.h:870

[wifi\_enterprise\_creds\_params::client\_key2\_len](structwifi__enterprise__creds__params.md#a3da90b8a8dfa848f617579760ad4f971)

uint32\_t client\_key2\_len

Phase2 Client key length.

**Definition** wifi\_mgmt.h:876

[wifi\_enterprise\_creds\_params::client\_cert\_len](structwifi__enterprise__creds__params.md#a5f122d59b25b00af2db7eeac93d5482e)

uint32\_t client\_cert\_len

Client certification length.

**Definition** wifi\_mgmt.h:860

[wifi\_enterprise\_creds\_params::ca\_cert\_len](structwifi__enterprise__creds__params.md#a5f7060fcd2ca3db0b202faf15062564b)

uint32\_t ca\_cert\_len

CA certification length.

**Definition** wifi\_mgmt.h:856

[wifi\_enterprise\_creds\_params::client\_cert](structwifi__enterprise__creds__params.md#a81d61179feba627be5c6456130b9f2af)

uint8\_t \* client\_cert

Client certification.

**Definition** wifi\_mgmt.h:858

[wifi\_enterprise\_creds\_params::client\_key](structwifi__enterprise__creds__params.md#a8d88f5a8a6ccc8a9a883078af49ae96b)

uint8\_t \* client\_key

Client key.

**Definition** wifi\_mgmt.h:862

[wifi\_enterprise\_creds\_params::server\_key\_len](structwifi__enterprise__creds__params.md#a9500252974bd15037d4dbc41eba3a27d)

uint32\_t server\_key\_len

Server key length.

**Definition** wifi\_mgmt.h:884

[wifi\_enterprise\_creds\_params::dh\_param](structwifi__enterprise__creds__params.md#ab0fd7419d8a94d1d804e5554acfbf49a)

uint8\_t \* dh\_param

Diffie–Hellman parameter.

**Definition** wifi\_mgmt.h:886

[wifi\_enterprise\_creds\_params::client\_key2](structwifi__enterprise__creds__params.md#abcda4d7820681d517d70d8f130b47050)

uint8\_t \* client\_key2

Client key of phase2.

**Definition** wifi\_mgmt.h:874

[wifi\_enterprise\_creds\_params::ca\_cert2\_len](structwifi__enterprise__creds__params.md#abf35045e71afb0cb9ea25c635c5ac141)

uint32\_t ca\_cert2\_len

Phase2 CA certification length.

**Definition** wifi\_mgmt.h:868

[wifi\_enterprise\_creds\_params::dh\_param\_len](structwifi__enterprise__creds__params.md#ac548e0b006a9f7b858409cda7c3d34ba)

uint32\_t dh\_param\_len

Diffie–Hellman parameter length.

**Definition** wifi\_mgmt.h:888

[wifi\_enterprise\_creds\_params::server\_key](structwifi__enterprise__creds__params.md#acb94a8885b5ab99d1a8fb33dffebc322)

uint8\_t \* server\_key

Server key.

**Definition** wifi\_mgmt.h:882

[wifi\_enterprise\_creds\_params::server\_cert\_len](structwifi__enterprise__creds__params.md#ad0bfb59d3691e5d21cb4b810c4d1279e)

uint32\_t server\_cert\_len

Server certification length.

**Definition** wifi\_mgmt.h:880

[wifi\_enterprise\_creds\_params::server\_cert](structwifi__enterprise__creds__params.md#ad3621e92a1aa968c58a899ace72967db)

uint8\_t \* server\_cert

Server certification.

**Definition** wifi\_mgmt.h:878

[wifi\_enterprise\_creds\_params::ca\_cert2](structwifi__enterprise__creds__params.md#ad9b867873709d7f2363fef49d7b6f2ca)

uint8\_t \* ca\_cert2

CA certification of phase2.

**Definition** wifi\_mgmt.h:866

[wifi\_enterprise\_creds\_params::client\_cert2\_len](structwifi__enterprise__creds__params.md#adbe26c9b88f44eb6b875888f6a03e1bb)

uint32\_t client\_cert2\_len

Phase2 Client certification length.

**Definition** wifi\_mgmt.h:872

[wifi\_enterprise\_creds\_params::ca\_cert](structwifi__enterprise__creds__params.md#ae37381504a457b2f1d56dd5270c6711d)

uint8\_t \* ca\_cert

CA certification.

**Definition** wifi\_mgmt.h:854

[wifi\_filter\_info](structwifi__filter__info.md)

Wi-Fi filter setting for monitor, prmoiscuous, TX-injection modes.

**Definition** wifi\_mgmt.h:1013

[wifi\_filter\_info::buffer\_size](structwifi__filter__info.md#a1b2d0448fc7f62654e3f5aacfba62f8f)

uint16\_t buffer\_size

Filter buffer size.

**Definition** wifi\_mgmt.h:1019

[wifi\_filter\_info::filter](structwifi__filter__info.md#ad9560be814299055cfa11b995a7dcf42)

uint8\_t filter

Filter setting.

**Definition** wifi\_mgmt.h:1015

[wifi\_filter\_info::oper](structwifi__filter__info.md#aedd5e220cdde5768cb0f4aff920971cd)

enum wifi\_mgmt\_op oper

Get or set operation.

**Definition** wifi\_mgmt.h:1021

[wifi\_filter\_info::if\_index](structwifi__filter__info.md#af9ea91e31e78afcb7ffe1ff9a04277a3)

uint8\_t if\_index

Interface index.

**Definition** wifi\_mgmt.h:1017

[wifi\_iface\_status](structwifi__iface__status.md)

Wi-Fi interface status.

**Definition** wifi\_mgmt.h:672

[wifi\_iface\_status::beacon\_interval](structwifi__iface__status.md#a241bfbe70628006b515b5f9e4f97665c)

unsigned short beacon\_interval

Beacon interval.

**Definition** wifi\_mgmt.h:700

[wifi\_iface\_status::wpa3\_ent\_type](structwifi__iface__status.md#a361c0e8a385fdc21f16258c25c2bc8d1)

enum wifi\_wpa3\_enterprise\_type wpa3\_ent\_type

WPA3 enterprise type.

**Definition** wifi\_mgmt.h:690

[wifi\_iface\_status::ssid](structwifi__iface__status.md#a3ab671471bcdfeb5b955d156d39f2bb3)

char ssid[WIFI\_SSID\_MAX\_LEN+1]

SSID.

**Definition** wifi\_mgmt.h:678

[wifi\_iface\_status::rssi](structwifi__iface__status.md#a4e593147b88eb4938d55a4de72fcc7f6)

int rssi

RSSI.

**Definition** wifi\_mgmt.h:696

[wifi\_iface\_status::bssid](structwifi__iface__status.md#a5d5d19056a1a15365fbdd94274a0fc5e)

char bssid[WIFI\_MAC\_ADDR\_LEN]

BSSID.

**Definition** wifi\_mgmt.h:680

[wifi\_iface\_status::security](structwifi__iface__status.md#a625ecec1abec8dd65cf155eab21a01b5)

enum wifi\_security\_type security

Security type, see enum wifi\_security\_type.

**Definition** wifi\_mgmt.h:692

[wifi\_iface\_status::channel](structwifi__iface__status.md#a6432663156e5b2c424d254ed1eae0144)

unsigned int channel

Channel.

**Definition** wifi\_mgmt.h:684

[wifi\_iface\_status::mfp](structwifi__iface__status.md#aa1a9b644fd355526125ddd32416b7c24)

enum wifi\_mfp\_options mfp

MFP options, see enum wifi\_mfp\_options.

**Definition** wifi\_mgmt.h:694

[wifi\_iface\_status::dtim\_period](structwifi__iface__status.md#aae6c8cbaa16c81d308f08114d5103a3d)

unsigned char dtim\_period

DTIM period.

**Definition** wifi\_mgmt.h:698

[wifi\_iface\_status::state](structwifi__iface__status.md#ac52806155be3d64954ac6d109e76ec57)

int state

Interface state, see enum wifi\_iface\_state.

**Definition** wifi\_mgmt.h:674

[wifi\_iface\_status::twt\_capable](structwifi__iface__status.md#acfde8d64b463a9f553aa4fb689dc1917)

bool twt\_capable

is TWT capable?

**Definition** wifi\_mgmt.h:702

[wifi\_iface\_status::iface\_mode](structwifi__iface__status.md#ad33d2ec149a8d556e2472dd842ceadc0)

enum wifi\_iface\_mode iface\_mode

Interface mode, see enum wifi\_iface\_mode.

**Definition** wifi\_mgmt.h:686

[wifi\_iface\_status::ssid\_len](structwifi__iface__status.md#ad82f281941e4f6ce1ef0bca008e26d41)

unsigned int ssid\_len

SSID length.

**Definition** wifi\_mgmt.h:676

[wifi\_iface\_status::band](structwifi__iface__status.md#ae1c141a18f4e225af2c22a8cb4f882a8)

enum wifi\_frequency\_bands band

Frequency band.

**Definition** wifi\_mgmt.h:682

[wifi\_iface\_status::link\_mode](structwifi__iface__status.md#ae2de076d79f2172793d65fe9cd31edc4)

enum wifi\_link\_mode link\_mode

Link mode, see enum wifi\_link\_mode.

**Definition** wifi\_mgmt.h:688

[wifi\_iface\_status::current\_phy\_tx\_rate](structwifi__iface__status.md#af255c63862e0c9e5008b2e4952d7e491)

int current\_phy\_tx\_rate

The current 802.11 PHY TX data rate (in Mbps).

**Definition** wifi\_mgmt.h:704

[wifi\_mgmt\_ops](structwifi__mgmt__ops.md)

Wi-Fi management API.

**Definition** wifi\_mgmt.h:1318

[wifi\_mgmt\_ops::reg\_domain](structwifi__mgmt__ops.md#a0a287c8acf2d7bf9333b755589294881)

int(\* reg\_domain)(const struct device \*dev, struct wifi\_reg\_domain \*reg\_domain)

Set or get regulatory domain.

**Definition** wifi\_mgmt.h:1453

[wifi\_mgmt\_ops::send\_11k\_neighbor\_request](structwifi__mgmt__ops.md#a1cdd0b76a0a326e968d27c0a3cafcef8)

int(\* send\_11k\_neighbor\_request)(const struct device \*dev, struct wifi\_11k\_params \*params)

Send 11k neighbor request.

**Definition** wifi\_mgmt.h:1413

[wifi\_mgmt\_ops::get\_rts\_threshold](structwifi__mgmt__ops.md#a20706f9eed43b3380258b62fdf93be02)

int(\* get\_rts\_threshold)(const struct device \*dev, unsigned int \*rts\_threshold)

Set Wi-Fi enterprise mode CA/client Cert and key.

**Definition** wifi\_mgmt.h:1577

[wifi\_mgmt\_ops::ap\_config\_params](structwifi__mgmt__ops.md#a2475f32afcce72464b2db6ecad7fb3eb)

int(\* ap\_config\_params)(const struct device \*dev, struct wifi\_ap\_config\_params \*params)

Configure AP parameter.

**Definition** wifi\_mgmt.h:1540

[wifi\_mgmt\_ops::scan](structwifi__mgmt__ops.md#a267030c27da3cdc251badd0ed7f7b1cb)

int(\* scan)(const struct device \*dev, struct wifi\_scan\_params \*params, scan\_result\_cb\_t cb)

Scan for Wi-Fi networks.

**Definition** wifi\_mgmt.h:1330

[wifi\_mgmt\_ops::cfg\_11k](structwifi__mgmt__ops.md#a2cf66093ad850319cf222468e22ff485)

int(\* cfg\_11k)(const struct device \*dev, struct wifi\_11k\_params \*params)

Set or get 11K status.

**Definition** wifi\_mgmt.h:1405

[wifi\_mgmt\_ops::btm\_query](structwifi__mgmt__ops.md#a3437f5881a8e0a487c11dd43a6099b6d)

int(\* btm\_query)(const struct device \*dev, uint8\_t reason)

Send BTM query.

**Definition** wifi\_mgmt.h:1486

[wifi\_mgmt\_ops::get\_conn\_params](structwifi__mgmt__ops.md#a42c2aa55df30158d8b5d6f4c81e3e2dd)

int(\* get\_conn\_params)(const struct device \*dev, struct wifi\_connect\_req\_params \*params)

Get Wi-Fi connection parameters recently used.

**Definition** wifi\_mgmt.h:1524

[wifi\_mgmt\_ops::start\_11r\_roaming](structwifi__mgmt__ops.md#a501b114298738ac6af9c4a80f5360d79)

int(\* start\_11r\_roaming)(const struct device \*dev)

Start 11r roaming.

**Definition** wifi\_mgmt.h:1600

[wifi\_mgmt\_ops::set\_rts\_threshold](structwifi__mgmt__ops.md#a514e06d63bcf6dc11dba1d3af8d102d5)

int(\* set\_rts\_threshold)(const struct device \*dev, unsigned int rts\_threshold)

Set RTS threshold value.

**Definition** wifi\_mgmt.h:1532

[wifi\_mgmt\_ops::get\_power\_save\_config](structwifi__mgmt__ops.md#a52690b13f8a1e7b0c2302eaa24ae4c7f)

int(\* get\_power\_save\_config)(const struct device \*dev, struct wifi\_ps\_config \*config)

Get power save config.

**Definition** wifi\_mgmt.h:1445

[wifi\_mgmt\_ops::candidate\_scan](structwifi__mgmt__ops.md#a538ffba0a7e045ca9c8ac62ccefc8a36)

int(\* candidate\_scan)(const struct device \*dev, struct wifi\_scan\_params \*params)

Trigger candidate scan.

**Definition** wifi\_mgmt.h:1593

[wifi\_mgmt\_ops::disconnect](structwifi__mgmt__ops.md#a5725c6fd93ae189a3019374cd4ad2ff4)

int(\* disconnect)(const struct device \*dev)

Disconnect from a Wi-Fi network.

**Definition** wifi\_mgmt.h:1348

[wifi\_mgmt\_ops::ap\_disable](structwifi__mgmt__ops.md#a5aa7a2be82eb1783872abda2b8978235)

int(\* ap\_disable)(const struct device \*dev)

Disable AP mode.

**Definition** wifi\_mgmt.h:1364

[wifi\_mgmt\_ops::get\_stats](structwifi__mgmt__ops.md#a5e6fdf836273fcde54efff4c77bfdf0e)

int(\* get\_stats)(const struct device \*dev, struct net\_stats\_wifi \*stats)

Get Wi-Fi statistics.

**Definition** wifi\_mgmt.h:1389

[wifi\_mgmt\_ops::legacy\_roam](structwifi__mgmt__ops.md#aa088223f84094614145d9d81e3acc20a)

int(\* legacy\_roam)(const struct device \*dev)

Send legacy scan.

**Definition** wifi\_mgmt.h:1502

[wifi\_mgmt\_ops::get\_version](structwifi__mgmt__ops.md#aa7e4bc3dbc960091d11ffe5454259885)

int(\* get\_version)(const struct device \*dev, struct wifi\_version \*params)

Get Version of WiFi driver and Firmware.

**Definition** wifi\_mgmt.h:1516

[wifi\_mgmt\_ops::pmksa\_flush](structwifi__mgmt__ops.md#aadf991d6f6725e5c179ca8343d626ad8)

int(\* pmksa\_flush)(const struct device \*dev)

Flush PMKSA cache entries.

**Definition** wifi\_mgmt.h:1558

[wifi\_mgmt\_ops::wps\_config](structwifi__mgmt__ops.md#aaf85f7b56997fb40689b927535af5e85)

int(\* wps\_config)(const struct device \*dev, struct wifi\_wps\_config\_params \*params)

Start a WPS PBC/PIN connection.

**Definition** wifi\_mgmt.h:1585

[wifi\_mgmt\_ops::set\_twt](structwifi__mgmt__ops.md#ab4500534b6abe0449290c8bd8f729fc4)

int(\* set\_twt)(const struct device \*dev, struct wifi\_twt\_params \*params)

Setup or teardown TWT flow.

**Definition** wifi\_mgmt.h:1429

[wifi\_mgmt\_ops::set\_power\_save](structwifi__mgmt__ops.md#ac0f3f7fa699b1bc7db2358e77dd44cc4)

int(\* set\_power\_save)(const struct device \*dev, struct wifi\_ps\_params \*params)

Set power save status.

**Definition** wifi\_mgmt.h:1421

[wifi\_mgmt\_ops::ap\_enable](structwifi__mgmt__ops.md#ac2ce3a4a86c43e30d33261f71c44198a)

int(\* ap\_enable)(const struct device \*dev, struct wifi\_connect\_req\_params \*params)

Enable AP mode.

**Definition** wifi\_mgmt.h:1356

[wifi\_mgmt\_ops::set\_btwt](structwifi__mgmt__ops.md#ad2d1ab4db1947dbdb2909a675fa1d653)

int(\* set\_btwt)(const struct device \*dev, struct wifi\_twt\_params \*params)

Setup BTWT flow.

**Definition** wifi\_mgmt.h:1437

[wifi\_mgmt\_ops::filter](structwifi__mgmt__ops.md#ad645276745ce8dd9685e0744efdfc733)

int(\* filter)(const struct device \*dev, struct wifi\_filter\_info \*filter)

Set or get packet filter settings for monitor and promiscuous modes.

**Definition** wifi\_mgmt.h:1461

[wifi\_mgmt\_ops::iface\_status](structwifi__mgmt__ops.md#adf157476d776bc9c068e99e1a0266fd3)

int(\* iface\_status)(const struct device \*dev, struct wifi\_iface\_status \*status)

Get interface status.

**Definition** wifi\_mgmt.h:1380

[wifi\_mgmt\_ops::mode](structwifi__mgmt__ops.md#ae2fb1bc35bf9255655a30a2ad8588b7c)

int(\* mode)(const struct device \*dev, struct wifi\_mode\_info \*mode)

Set or get mode of operation.

**Definition** wifi\_mgmt.h:1469

[wifi\_mgmt\_ops::connect](structwifi__mgmt__ops.md#ae6255ea77739918797b4f3c7a4634a75)

int(\* connect)(const struct device \*dev, struct wifi\_connect\_req\_params \*params)

Connect to a Wi-Fi network.

**Definition** wifi\_mgmt.h:1340

[wifi\_mgmt\_ops::reset\_stats](structwifi__mgmt__ops.md#ae66901b434ab02863c0d3bd539c4b650)

int(\* reset\_stats)(const struct device \*dev)

Reset Wi-Fi statistics.

**Definition** wifi\_mgmt.h:1396

[wifi\_mgmt\_ops::ap\_sta\_disconnect](structwifi__mgmt__ops.md#af01aaec29be78c02314acf13b5c1b6f7)

int(\* ap\_sta\_disconnect)(const struct device \*dev, const uint8\_t \*mac)

Disconnect a STA from AP.

**Definition** wifi\_mgmt.h:1372

[wifi\_mgmt\_ops::channel](structwifi__mgmt__ops.md#af17ddfea01d0ab478f6fd50b1c9d6015)

int(\* channel)(const struct device \*dev, struct wifi\_channel\_info \*channel)

Set or get current channel of operation.

**Definition** wifi\_mgmt.h:1477

[wifi\_mgmt\_ops::bss\_ext\_capab](structwifi__mgmt__ops.md#afb83b59f392b11fe8071ca57e3ea3928)

int(\* bss\_ext\_capab)(const struct device \*dev, int capab)

Judge ap whether support the capability.

**Definition** wifi\_mgmt.h:1494

[wifi\_mode\_info](structwifi__mode__info.md)

Wi-Fi mode setup.

**Definition** wifi\_mgmt.h:1003

[wifi\_mode\_info::oper](structwifi__mode__info.md#a57c101db8b81ab0ac5dd0a158057a64a)

enum wifi\_mgmt\_op oper

Get or set operation.

**Definition** wifi\_mgmt.h:1009

[wifi\_mode\_info::mode](structwifi__mode__info.md#aa29d3b88fc718aa3ac05daf38974707d)

uint8\_t mode

Mode setting for a specific mode of operation.

**Definition** wifi\_mgmt.h:1005

[wifi\_mode\_info::if\_index](structwifi__mode__info.md#add58dd3b45fd2ddaf684d1b0de81bef9)

uint8\_t if\_index

Interface index.

**Definition** wifi\_mgmt.h:1007

[wifi\_ps\_config](structwifi__ps__config.md)

Wi-Fi power save configuration.

**Definition** wifi\_mgmt.h:892

[wifi\_ps\_config::ps\_params](structwifi__ps__config.md#a357aafc2dedda37755b1cb1fc07fe5a6)

struct wifi\_ps\_params ps\_params

Power save configuration.

**Definition** wifi\_mgmt.h:898

[wifi\_ps\_config::num\_twt\_flows](structwifi__ps__config.md#a9e83c10eaaa1d721cbc49b40aedb00df)

char num\_twt\_flows

Number of TWT flows.

**Definition** wifi\_mgmt.h:894

[wifi\_ps\_config::twt\_flows](structwifi__ps__config.md#ab7460f0f253b2d552e49e98e2c770967)

struct wifi\_twt\_flow\_info twt\_flows[WIFI\_MAX\_TWT\_FLOWS]

TWT flow details.

**Definition** wifi\_mgmt.h:896

[wifi\_ps\_params](structwifi__ps__params.md)

Wi-Fi power save parameters.

**Definition** wifi\_mgmt.h:708

[wifi\_ps\_params::mode](structwifi__ps__params.md#a5a022d89d43ecf2cd1f15fc72c0f2bed)

enum wifi\_ps\_mode mode

Wi-Fi power save mode.

**Definition** wifi\_mgmt.h:716

[wifi\_ps\_params::fail\_reason](structwifi__ps__params.md#a63fa2ee03bc4aefada61c298ee14336c)

enum wifi\_config\_ps\_param\_fail\_reason fail\_reason

Wi-Fi power save fail reason.

**Definition** wifi\_mgmt.h:729

[wifi\_ps\_params::wakeup\_mode](structwifi__ps__params.md#a7cb3e7fb7d9f8bd7c2cab41f879b3b66)

enum wifi\_ps\_wakeup\_mode wakeup\_mode

Wi-Fi power save wakeup mode.

**Definition** wifi\_mgmt.h:714

[wifi\_ps\_params::listen\_interval](structwifi__ps__params.md#a8510c799ab0c5825f1c6349f9799c62f)

unsigned short listen\_interval

Listen interval.

**Definition** wifi\_mgmt.h:712

[wifi\_ps\_params::exit\_strategy](structwifi__ps__params.md#ab9fc62dd1e2928320274fa1554a550a6)

enum wifi\_ps\_exit\_strategy exit\_strategy

Wi-Fi power save exit strategy.

**Definition** wifi\_mgmt.h:731

[wifi\_ps\_params::enabled](structwifi__ps__params.md#abb22aaa45833ac130922204bd2fe841b)

enum wifi\_ps enabled

Power save state.

**Definition** wifi\_mgmt.h:710

[wifi\_ps\_params::timeout\_ms](structwifi__ps__params.md#ad963f1bf78dc271f08b73f3aadb36a91)

unsigned int timeout\_ms

Wi-Fi power save timeout.

**Definition** wifi\_mgmt.h:725

[wifi\_ps\_params::type](structwifi__ps__params.md#aef62e5bf6216bf4dc461efe71735c4bd)

enum wifi\_ps\_param\_type type

Wi-Fi power save type.

**Definition** wifi\_mgmt.h:727

[wifi\_raw\_scan\_result](structwifi__raw__scan__result.md)

Wi-Fi raw scan result.

**Definition** wifi\_mgmt.h:962

[wifi\_raw\_scan\_result::rssi](structwifi__raw__scan__result.md#a3f08580c6448a5fa28dd8a594fa7dad6)

int8\_t rssi

RSSI.

**Definition** wifi\_mgmt.h:964

[wifi\_raw\_scan\_result::data](structwifi__raw__scan__result.md#a5710e89199c147ce898602795f00aba3)

uint8\_t data[CONFIG\_WIFI\_MGMT\_RAW\_SCAN\_RESULT\_LENGTH]

Raw scan data.

**Definition** wifi\_mgmt.h:970

[wifi\_raw\_scan\_result::frame\_length](structwifi__raw__scan__result.md#a876966f469714eb481b42ccc8a63945c)

int frame\_length

Frame length.

**Definition** wifi\_mgmt.h:966

[wifi\_raw\_scan\_result::frequency](structwifi__raw__scan__result.md#aa2c7781882c6775616cbc8016b0842f6)

unsigned short frequency

Frequency.

**Definition** wifi\_mgmt.h:968

[wifi\_reg\_chan\_info](structwifi__reg__chan__info.md)

Per-channel regulatory attributes.

**Definition** wifi\_mgmt.h:923

[wifi\_reg\_chan\_info::center\_frequency](structwifi__reg__chan__info.md#a0addffc11ef29f50c01b700835e59930)

unsigned short center\_frequency

Center frequency in MHz.

**Definition** wifi\_mgmt.h:925

[wifi\_reg\_chan\_info::dfs](structwifi__reg__chan__info.md#a1ab137c142902d2de7d6be2626d7ac1f)

unsigned short dfs

Is a DFS channel.

**Definition** wifi\_mgmt.h:933

[wifi\_reg\_chan\_info::supported](structwifi__reg__chan__info.md#aa044611e18b7332b8577e29f6a769e3f)

unsigned short supported

Is channel supported or not.

**Definition** wifi\_mgmt.h:929

[wifi\_reg\_chan\_info::passive\_only](structwifi__reg__chan__info.md#acc7a88b004c9a61c8bf9ee1a97f85928)

unsigned short passive\_only

Passive transmissions only.

**Definition** wifi\_mgmt.h:931

[wifi\_reg\_chan\_info::max\_power](structwifi__reg__chan__info.md#af9169ab4a41fac4c6f6766fc96799545)

unsigned short max\_power

Maximum transmission power (in dBm).

**Definition** wifi\_mgmt.h:927

[wifi\_reg\_domain](structwifi__reg__domain.md)

Regulatory domain information or configuration.

**Definition** wifi\_mgmt.h:937

[wifi\_reg\_domain::num\_channels](structwifi__reg__domain.md#a3278e9f43893f49ab9f9d0d7f24009c1)

unsigned int num\_channels

Number of channels supported.

**Definition** wifi\_mgmt.h:947

[wifi\_reg\_domain::oper](structwifi__reg__domain.md#a3bbfdf1497a87bbb6b6211c7035e1002)

enum wifi\_mgmt\_op oper

Regulatory domain operation.

**Definition** wifi\_mgmt.h:939

[wifi\_reg\_domain::chan\_info](structwifi__reg__domain.md#a4c8c9c11e41123cd7738fdb0d33ae5fb)

struct wifi\_reg\_chan\_info \* chan\_info

Channels information.

**Definition** wifi\_mgmt.h:949

[wifi\_reg\_domain::force](structwifi__reg__domain.md#a567c6fcae8032567aea83c18cd211c33)

bool force

Ignore all other regulatory hints over this one, the behavior is implementation specific.

**Definition** wifi\_mgmt.h:943

[wifi\_reg\_domain::country\_code](structwifi__reg__domain.md#abf191495814c227fbbfaccb2f727762e)

uint8\_t country\_code[WIFI\_COUNTRY\_CODE\_LEN]

Country code: ISO/IEC 3166-1 alpha-2.

**Definition** wifi\_mgmt.h:945

[wifi\_scan\_params](structwifi__scan__params.md)

Wi-Fi scan parameters structure.

**Definition** wifi\_mgmt.h:472

[wifi\_scan\_params::max\_bss\_cnt](structwifi__scan__params.md#a12d5dea7d8fa8ad03ac2366720c46243)

uint16\_t max\_bss\_cnt

Specifies the maximum number of scan results to return.

**Definition** wifi\_mgmt.h:501

[wifi\_scan\_params::dwell\_time\_active](structwifi__scan__params.md#a2453a75c23e04e3572559c0e7199c1b4)

uint16\_t dwell\_time\_active

Active scan dwell time (in ms) on a channel.

**Definition** wifi\_mgmt.h:487

[wifi\_scan\_params::scan\_type](structwifi__scan__params.md#a645acc54603cd4692527c1a028933078)

enum wifi\_scan\_type scan\_type

Scan type, see enum wifi\_scan\_type.

**Definition** wifi\_mgmt.h:480

[wifi\_scan\_params::bands](structwifi__scan__params.md#a6b571d960ed9d7419e31530e5fb6f97a)

uint8\_t bands

Bitmap of bands to be scanned.

**Definition** wifi\_mgmt.h:484

[wifi\_scan\_params::dwell\_time\_passive](structwifi__scan__params.md#a8e7a37ccda8de635e7b7066d7943e814)

uint16\_t dwell\_time\_passive

Passive scan dwell time (in ms) on a channel.

**Definition** wifi\_mgmt.h:490

[wifi\_scan\_params::band\_chan](structwifi__scan__params.md#aa5ddbd6bc97b7598288d4b0d38521681)

struct wifi\_band\_channel band\_chan[WIFI\_MGMT\_SCAN\_CHAN\_MAX\_MANUAL]

Channel information array indexed on Wi-Fi frequency bands and channels within that band.

**Definition** wifi\_mgmt.h:516

[wifi\_scan\_params::ssids](structwifi__scan__params.md#aac11ee8e0ec8a4fa24668f4820bd1a12)

const char \* ssids[WIFI\_MGMT\_SCAN\_SSID\_FILT\_MAX]

Array of SSID strings to scan.

**Definition** wifi\_mgmt.h:493

[wifi\_scan\_result](structwifi__scan__result.md)

Wi-Fi scan result, each result is provided to the net\_mgmt\_event\_callback via its info attribute (see...

**Definition** wifi\_mgmt.h:522

[wifi\_scan\_result::ssid\_length](structwifi__scan__result.md#a2c1c2f4265b914df08fc75deb8b69d39)

uint8\_t ssid\_length

SSID length.

**Definition** wifi\_mgmt.h:526

[wifi\_scan\_result::band](structwifi__scan__result.md#a38201c9dd798dc11b5bda3ce97b02e92)

uint8\_t band

Frequency band.

**Definition** wifi\_mgmt.h:528

[wifi\_scan\_result::mac](structwifi__scan__result.md#a4fdbc4dc4d5c8b279223e8c06624f434)

uint8\_t mac[WIFI\_MAC\_ADDR\_LEN]

BSSID.

**Definition** wifi\_mgmt.h:540

[wifi\_scan\_result::rssi](structwifi__scan__result.md#a76aa012136e3721fd4a482a22b93546f)

int8\_t rssi

RSSI.

**Definition** wifi\_mgmt.h:538

[wifi\_scan\_result::mac\_length](structwifi__scan__result.md#a8fca0dabec00ebd7ed4800098ec9d451)

uint8\_t mac\_length

BSSID length.

**Definition** wifi\_mgmt.h:542

[wifi\_scan\_result::ssid](structwifi__scan__result.md#aaefb8f5c9510e4f5002ae306d853ade8)

uint8\_t ssid[WIFI\_SSID\_MAX\_LEN+1]

SSID.

**Definition** wifi\_mgmt.h:524

[wifi\_scan\_result::wpa3\_ent\_type](structwifi__scan__result.md#abb7de47c605ec05c8fe0a06ecbd2b7b6)

enum wifi\_wpa3\_enterprise\_type wpa3\_ent\_type

WPA3 enterprise type.

**Definition** wifi\_mgmt.h:534

[wifi\_scan\_result::mfp](structwifi__scan__result.md#acaa3fb30ebf6df22bfac6380698ed28e)

enum wifi\_mfp\_options mfp

MFP options.

**Definition** wifi\_mgmt.h:536

[wifi\_scan\_result::channel](structwifi__scan__result.md#adbbfd7692ee5ffd6344fe78b9d91c840)

uint8\_t channel

Channel.

**Definition** wifi\_mgmt.h:530

[wifi\_scan\_result::security](structwifi__scan__result.md#af2d3dc5d115e3db76d3bc115510b0a5a)

enum wifi\_security\_type security

Security type.

**Definition** wifi\_mgmt.h:532

[wifi\_status](structwifi__status.md)

Generic Wi-Fi status for commands and events.

**Definition** wifi\_mgmt.h:658

[wifi\_status::ap\_status](structwifi__status.md#a02f0fcc7ef57661ca95d0c99f045aef1)

enum wifi\_ap\_status ap\_status

Access point status.

**Definition** wifi\_mgmt.h:667

[wifi\_status::conn\_status](structwifi__status.md#a8f885e78366d0499e4ba8e15bef275ac)

enum wifi\_conn\_status conn\_status

Connection status.

**Definition** wifi\_mgmt.h:663

[wifi\_status::disconn\_reason](structwifi__status.md#aa04b5033d93274badd27f702af9830bc)

enum wifi\_disconn\_reason disconn\_reason

Disconnection reason status.

**Definition** wifi\_mgmt.h:665

[wifi\_status::status](structwifi__status.md#aa1dbff8154400f8353693d387977008b)

int status

Status value.

**Definition** wifi\_mgmt.h:661

[wifi\_twt\_flow\_info](structwifi__twt__flow__info.md)

Wi-Fi TWT flow information.

**Definition** wifi\_mgmt.h:828

[wifi\_twt\_flow\_info::dialog\_token](structwifi__twt__flow__info.md#a123ce10bed8b62b01919a7ea7644a0ba)

uint8\_t dialog\_token

Dialog token, used to map requests to responses.

**Definition** wifi\_mgmt.h:832

[wifi\_twt\_flow\_info::negotiation\_type](structwifi__twt__flow__info.md#a620ae8ba546e4091d74280cb1553b2cf)

enum wifi\_twt\_negotiation\_type negotiation\_type

TWT negotiation type, see enum wifi\_twt\_negotiation\_type.

**Definition** wifi\_mgmt.h:836

[wifi\_twt\_flow\_info::twt\_wake\_ahead\_duration](structwifi__twt__flow__info.md#a6384d3829d54a58a53eafcb74c64a658)

uint32\_t twt\_wake\_ahead\_duration

Wake ahead duration.

**Definition** wifi\_mgmt.h:848

[wifi\_twt\_flow\_info::trigger](structwifi__twt__flow__info.md#a952a67bd092c5dadba387bb13449c6f3)

bool trigger

Trigger enabled or disabled.

**Definition** wifi\_mgmt.h:840

[wifi\_twt\_flow\_info::responder](structwifi__twt__flow__info.md#ac82e4de8ffc82f851061f8ba8d217dc1)

bool responder

Requestor or responder.

**Definition** wifi\_mgmt.h:838

[wifi\_twt\_flow\_info::flow\_id](structwifi__twt__flow__info.md#acb0c618f1cebcb172f342cfe222683be)

uint8\_t flow\_id

Flow ID, used to map setup with teardown.

**Definition** wifi\_mgmt.h:834

[wifi\_twt\_flow\_info::twt\_interval](structwifi__twt__flow__info.md#ae15ba49fa54f82cc6a1fb0d4572114b7)

uint64\_t twt\_interval

Interval = Wake up time + Sleeping time.

**Definition** wifi\_mgmt.h:830

[wifi\_twt\_flow\_info::twt\_wake\_interval](structwifi__twt__flow__info.md#aede6cb0cfc999fac8ded49e2981a3762)

uint32\_t twt\_wake\_interval

Wake up time.

**Definition** wifi\_mgmt.h:846

[wifi\_twt\_flow\_info::implicit](structwifi__twt__flow__info.md#afb480be82d1c6f351bd634fd83bfa5c7)

bool implicit

Implicit or explicit.

**Definition** wifi\_mgmt.h:842

[wifi\_twt\_flow\_info::announce](structwifi__twt__flow__info.md#afc81a5111c265fd9bb2aca5f9510bfa8)

bool announce

Announced or unannounced.

**Definition** wifi\_mgmt.h:844

[wifi\_twt\_params](structwifi__twt__params.md)

Wi-Fi TWT parameters.

**Definition** wifi\_mgmt.h:749

[wifi\_twt\_params::announce](structwifi__twt__params.md#a02f2d822d530e5376f256503439a54f9)

bool announce

Announced or unannounced.

**Definition** wifi\_mgmt.h:776

[wifi\_twt\_params::teardown\_all](structwifi__twt__params.md#a26d6bda00452f77832f69f4465c13efb)

bool teardown\_all

Teardown all flows.

**Definition** wifi\_mgmt.h:808

[wifi\_twt\_params::setup\_cmd](structwifi__twt__params.md#a347f8cff73ee6b6ba6d15ddf6f376a2d)

enum wifi\_twt\_setup\_cmd setup\_cmd

TWT setup command, see enum wifi\_twt\_setup\_cmd.

**Definition** wifi\_mgmt.h:755

[wifi\_twt\_params::btwt\_offset](structwifi__twt__params.md#a4459cf19226e199d23ae0cd1d7132b73)

uint16\_t btwt\_offset

Broadcast TWT offset.

**Definition** wifi\_mgmt.h:797

[wifi\_twt\_params::trigger](structwifi__twt__params.md#a4e822c04b52fe6a9489e48e26b8f9382)

bool trigger

Trigger enabled or disabled.

**Definition** wifi\_mgmt.h:772

[wifi\_twt\_params::negotiation\_type](structwifi__twt__params.md#a5fd269328f68838b8a7e3a0b93eed894)

enum wifi\_twt\_negotiation\_type negotiation\_type

TWT negotiation type, see enum wifi\_twt\_negotiation\_type.

**Definition** wifi\_mgmt.h:753

[wifi\_twt\_params::operation](structwifi__twt__params.md#a6f0483861a387651c9c89ba182e064bd)

enum wifi\_twt\_operation operation

TWT operation, see enum wifi\_twt\_operation.

**Definition** wifi\_mgmt.h:751

[wifi\_twt\_params::twt\_wake\_ahead\_duration](structwifi__twt__params.md#a6f907ca412251fdd7391f29bfa6d7713)

uint32\_t twt\_wake\_ahead\_duration

Wake ahead notification is sent earlier than TWT Service period (SP) start based on this duration.

**Definition** wifi\_mgmt.h:784

[wifi\_twt\_params::fail\_reason](structwifi__twt__params.md#a70f58b502bb67ef3b2068ded2160b612)

enum wifi\_twt\_fail\_reason fail\_reason

TWT fail reason, see enum wifi\_twt\_fail\_reason.

**Definition** wifi\_mgmt.h:812

[wifi\_twt\_params::btwt](structwifi__twt__params.md#a72ab809144b1dd3e7e121e489ef399e2)

struct wifi\_twt\_params::@302311362167322044106272253111230157111235232263::@053165077055023247316045052326043107125356150312 btwt

Setup specific parameters.

[wifi\_twt\_params::twt\_wake\_interval](structwifi__twt__params.md#a7c297459a17ed2fd232c62cca63e952f)

uint32\_t twt\_wake\_interval

Wake up time.

**Definition** wifi\_mgmt.h:778

[wifi\_twt\_params::btwt\_li](structwifi__twt__params.md#a7e7c786c51d3bc70af135bad88ebde4f)

uint8\_t btwt\_li

In multiple of 4 beacon interval.

**Definition** wifi\_mgmt.h:799

[wifi\_twt\_params::resp\_status](structwifi__twt__params.md#a805a23284ed4afa46b84efcd43329beb)

enum wifi\_twt\_setup\_resp\_status resp\_status

TWT setup response status, see enum wifi\_twt\_setup\_resp\_status.

**Definition** wifi\_mgmt.h:757

[wifi\_twt\_params::implicit](structwifi__twt__params.md#a8ea1e2501c8b69dc3fa606eb360f8678)

bool implicit

Implicit or explicit.

**Definition** wifi\_mgmt.h:774

[wifi\_twt\_params::flow\_id](structwifi__twt__params.md#a95ec4b32d37309efa47256ae1ea865da)

uint8\_t flow\_id

Flow ID, used to map setup with teardown.

**Definition** wifi\_mgmt.h:763

[wifi\_twt\_params::teardown\_status](structwifi__twt__params.md#a9faff59e577775b3fe53f2139462ac71)

enum wifi\_twt\_teardown\_status teardown\_status

TWT teardown cmd status, see enum wifi\_twt\_teardown\_status.

**Definition** wifi\_mgmt.h:759

[wifi\_twt\_params::btwt\_sta\_wait](structwifi__twt__params.md#aa05e5fa6a519f700147bb99d6e69a06b)

uint8\_t btwt\_sta\_wait

Broadcast TWT station wait time.

**Definition** wifi\_mgmt.h:795

[wifi\_twt\_params::btwt\_set\_cfg](structwifi__twt__params.md#aa11562186ea265b906861269bc8a692b)

struct wifi\_btwt\_params btwt\_set\_cfg[5]

Broadcast TWT agreement sets.

**Definition** wifi\_mgmt.h:803

[wifi\_twt\_params::twt\_exponent](structwifi__twt__params.md#aabb77296f007cb055f78fa1ec3d155a3)

uint8\_t twt\_exponent

TWT exponent.

**Definition** wifi\_mgmt.h:788

[wifi\_twt\_params::twt\_mantissa](structwifi__twt__params.md#aadad4556e2e5405b0703ebb4233a4d17)

uint16\_t twt\_mantissa

TWT Mantissa Range: [0-sizeof(UINT16)].

**Definition** wifi\_mgmt.h:790

[wifi\_twt\_params::teardown](structwifi__twt__params.md#aadf62f6386359ad15491d0073c9065bf)

struct wifi\_twt\_params::@302311362167322044106272253111230157111235232263::@352270327013076240220216032274341232230206256214 teardown

Teardown specific parameters.

[wifi\_twt\_params::twt\_interval](structwifi__twt__params.md#ab92fe571559fcd5d97cdf7e6b7d86681)

uint64\_t twt\_interval

Interval = Wake up time + Sleeping time.

**Definition** wifi\_mgmt.h:768

[wifi\_twt\_params::twt\_info\_disable](structwifi__twt__params.md#ac02eab9593b1ec2c9a0453a67076df88)

bool twt\_info\_disable

TWT info enabled or disable.

**Definition** wifi\_mgmt.h:786

[wifi\_twt\_params::dialog\_token](structwifi__twt__params.md#adda47e302a87a766f18e28016963a561)

uint8\_t dialog\_token

Dialog token, used to map requests to responses.

**Definition** wifi\_mgmt.h:761

[wifi\_twt\_params::responder](structwifi__twt__params.md#ae547c6fc1c7cbad15bebcfdaa43f59e7)

bool responder

Requestor or responder.

**Definition** wifi\_mgmt.h:770

[wifi\_twt\_params::setup](structwifi__twt__params.md#aee57c0189b210cfcc18e213e35b9479c)

struct wifi\_twt\_params::@302311362167322044106272253111230157111235232263::@007355023165260313375314073015252271352275036053 setup

Setup specific parameters.

[wifi\_twt\_params::btwt\_count](structwifi__twt__params.md#afc563010a33624bf01feac1292f0871d)

uint8\_t btwt\_count

Broadcast TWT agreement count.

**Definition** wifi\_mgmt.h:801

[wifi\_version](structwifi__version.md)

Wi-Fi version.

**Definition** wifi\_mgmt.h:450

[wifi\_version::fw\_version](structwifi__version.md#a4bf2cbdf5c43ff21718ccf19646c164e)

const char \* fw\_version

Firmware version.

**Definition** wifi\_mgmt.h:454

[wifi\_version::drv\_version](structwifi__version.md#aea828bdb512440d6aa3cc853525c4971)

const char \* drv\_version

Driver version.

**Definition** wifi\_mgmt.h:452

[wifi\_wps\_config\_params](structwifi__wps__config__params.md)

Wi-Fi wps setup.

**Definition** wifi\_mgmt.h:1266

[wifi\_wps\_config\_params::pin](structwifi__wps__config__params.md#a962bd6513c564150e0c75112b96bbe15)

char pin[8+1]

pin value

**Definition** wifi\_mgmt.h:1270

[wifi\_wps\_config\_params::oper](structwifi__wps__config__params.md#aa7a10889c5cd5124983b0f7242d23b7e)

enum wifi\_wps\_op oper

wps operation

**Definition** wifi\_mgmt.h:1268

[wifi.h](wifi_8h.md)

IEEE 802.11 protocol and general Wi-Fi definitions.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [wifi\_mgmt.h](wifi__mgmt_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
