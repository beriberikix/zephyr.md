---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/wifi__mgmt_8h_source.html
original_path: doxygen/html/wifi__mgmt_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
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

54#define WIFI\_MGMT\_BAND\_STR\_SIZE\_MAX 8

55#define WIFI\_MGMT\_SCAN\_MAX\_BSS\_CNT 65535

56

57#define WIFI\_MGMT\_SKIP\_INACTIVITY\_POLL IS\_ENABLED(CONFIG\_WIFI\_MGMT\_AP\_STA\_SKIP\_INACTIVITY\_POLL)

59

[ 61](group__wifi__mgmt.md#ga99a55137188119f65f9d2bb4f57cac77)enum [net\_request\_wifi\_cmd](group__wifi__mgmt.md#ga99a55137188119f65f9d2bb4f57cac77) {

[ 63](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a4aadf9114010c09bd7420c99a2049d5a) [NET\_REQUEST\_WIFI\_CMD\_SCAN](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a4aadf9114010c09bd7420c99a2049d5a) = 1,

[ 65](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a78c958877ee60c90803c925b6b2f057a) [NET\_REQUEST\_WIFI\_CMD\_CONNECT](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a78c958877ee60c90803c925b6b2f057a),

[ 67](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77ac33941da138b993f7a1158d91469bcb7) [NET\_REQUEST\_WIFI\_CMD\_DISCONNECT](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77ac33941da138b993f7a1158d91469bcb7),

[ 69](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a28267d33b555433271cb121d62194a4c) [NET\_REQUEST\_WIFI\_CMD\_AP\_ENABLE](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a28267d33b555433271cb121d62194a4c),

[ 71](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a6fe9d7137b4cd20de880955b27382ccf) [NET\_REQUEST\_WIFI\_CMD\_AP\_DISABLE](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a6fe9d7137b4cd20de880955b27382ccf),

[ 73](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a6af9d52df8f9db6393044e42e10ff0de) [NET\_REQUEST\_WIFI\_CMD\_IFACE\_STATUS](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a6af9d52df8f9db6393044e42e10ff0de),

[ 75](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77aa86fb7193245593dd84b3a4376bc25d6) [NET\_REQUEST\_WIFI\_CMD\_11K\_CONFIG](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77aa86fb7193245593dd84b3a4376bc25d6),

[ 77](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a48b3f0ec6647fb30d3b6456822c2dede) [NET\_REQUEST\_WIFI\_CMD\_11K\_NEIGHBOR\_REQUEST](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a48b3f0ec6647fb30d3b6456822c2dede),

[ 79](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77abf9fb93c205fa36f74a9ef19d3d0351a) [NET\_REQUEST\_WIFI\_CMD\_PS](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77abf9fb93c205fa36f74a9ef19d3d0351a),

[ 81](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a1c9dc2d698326d987ffe5bfd35a9ed09) [NET\_REQUEST\_WIFI\_CMD\_TWT](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a1c9dc2d698326d987ffe5bfd35a9ed09),

[ 83](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77ae6ce1c605d1bf7c09650ec15d74e77e9) [NET\_REQUEST\_WIFI\_CMD\_PS\_CONFIG](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77ae6ce1c605d1bf7c09650ec15d74e77e9),

[ 85](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a367cc44caefd313e0c7ad3badc081456) [NET\_REQUEST\_WIFI\_CMD\_REG\_DOMAIN](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a367cc44caefd313e0c7ad3badc081456),

[ 87](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77ab7183584bdf5fe673d39fa0d090e3899) [NET\_REQUEST\_WIFI\_CMD\_MODE](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77ab7183584bdf5fe673d39fa0d090e3899),

[ 89](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a2579ace546bf6954c111eb5951e894f5) [NET\_REQUEST\_WIFI\_CMD\_PACKET\_FILTER](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a2579ace546bf6954c111eb5951e894f5),

[ 91](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77aade3d7a43c730a52f7876c6486170bb2) [NET\_REQUEST\_WIFI\_CMD\_CHANNEL](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77aade3d7a43c730a52f7876c6486170bb2),

[ 93](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a6f3865aa6a4d7633e241ee2b002c1b5a) [NET\_REQUEST\_WIFI\_CMD\_AP\_STA\_DISCONNECT](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a6f3865aa6a4d7633e241ee2b002c1b5a),

[ 95](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a7d9596f2cce54c9e050d89469e86eccb) [NET\_REQUEST\_WIFI\_CMD\_VERSION](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a7d9596f2cce54c9e050d89469e86eccb),

[ 97](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77aa150f53621941796082e00090bde6a5a) [NET\_REQUEST\_WIFI\_CMD\_CONN\_PARAMS](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77aa150f53621941796082e00090bde6a5a),

[ 99](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a7852cff28fc18ddd7af0f8224c840e7b) [NET\_REQUEST\_WIFI\_CMD\_RTS\_THRESHOLD](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a7852cff28fc18ddd7af0f8224c840e7b),

[ 101](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a14a0428720818c79df825d758e83f813) [NET\_REQUEST\_WIFI\_CMD\_AP\_CONFIG\_PARAM](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a14a0428720818c79df825d758e83f813),

[ 103](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a6fc4d3aca344dc551dd62ae1d6072104) [NET\_REQUEST\_WIFI\_CMD\_DPP](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a6fc4d3aca344dc551dd62ae1d6072104),

104#ifdef CONFIG\_WIFI\_NM\_WPA\_SUPPLICANT\_WNM

106 NET\_REQUEST\_WIFI\_CMD\_BTM\_QUERY,

107#endif

[ 109](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a1fec11ed98f0a9411eefda9e55ee9aad) [NET\_REQUEST\_WIFI\_CMD\_PMKSA\_FLUSH](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a1fec11ed98f0a9411eefda9e55ee9aad),

[ 111](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a94b7fb7a8c529082e1d0458298b6c3fb) [NET\_REQUEST\_WIFI\_CMD\_ENTERPRISE\_CREDS](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a94b7fb7a8c529082e1d0458298b6c3fb),

[ 113](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77ab7a4215540d2e6cda0d522dc621e9d89) [NET\_REQUEST\_WIFI\_CMD\_RTS\_THRESHOLD\_CONFIG](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77ab7a4215540d2e6cda0d522dc621e9d89),

[ 115](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77aec78bf6196abee310e06a8454d27eed7) [NET\_REQUEST\_WIFI\_CMD\_WPS\_CONFIG](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77aec78bf6196abee310e06a8454d27eed7),

116#ifdef CONFIG\_WIFI\_CREDENTIALS\_CONNECT\_STORED

118 NET\_REQUEST\_WIFI\_CMD\_CONNECT\_STORED,

119#endif

[ 121](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a286205d961a77e44cd98e7894c48e676) [NET\_REQUEST\_WIFI\_CMD\_START\_ROAMING](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a286205d961a77e44cd98e7894c48e676),

[ 123](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77ad950aa5b87408793f4df9c39fe84cc55) [NET\_REQUEST\_WIFI\_CMD\_NEIGHBOR\_REP\_COMPLETE](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77ad950aa5b87408793f4df9c39fe84cc55),

[ 125](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77ab7bc479691f88138972d0d8e1e2179ed) [NET\_REQUEST\_WIFI\_CMD\_CANDIDATE\_SCAN](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77ab7bc479691f88138972d0d8e1e2179ed),

127 NET\_REQUEST\_WIFI\_CMD\_MAX

129};

130

[ 132](group__wifi__mgmt.md#ga1c277da90986fa52dca182c4d922646f)#define NET\_REQUEST\_WIFI\_SCAN \

133 (\_NET\_WIFI\_BASE | NET\_REQUEST\_WIFI\_CMD\_SCAN)

134

135[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)([NET\_REQUEST\_WIFI\_SCAN](group__wifi__mgmt.md#ga1c277da90986fa52dca182c4d922646f));

136

[ 138](group__wifi__mgmt.md#gaa7ab2a97950a22736bb69f60b459f0f6)#define NET\_REQUEST\_WIFI\_CONNECT \

139 (\_NET\_WIFI\_BASE | NET\_REQUEST\_WIFI\_CMD\_CONNECT)

140

141[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)([NET\_REQUEST\_WIFI\_CONNECT](group__wifi__mgmt.md#gaa7ab2a97950a22736bb69f60b459f0f6));

142

[ 144](group__wifi__mgmt.md#ga90afd8d4e83056463ec6e667ed8ea60a)#define NET\_REQUEST\_WIFI\_DISCONNECT \

145 (\_NET\_WIFI\_BASE | NET\_REQUEST\_WIFI\_CMD\_DISCONNECT)

146

147[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)([NET\_REQUEST\_WIFI\_DISCONNECT](group__wifi__mgmt.md#ga90afd8d4e83056463ec6e667ed8ea60a));

148

[ 150](group__wifi__mgmt.md#ga638d2eb0a5029c1af46a91b523ed8589)#define NET\_REQUEST\_WIFI\_AP\_ENABLE \

151 (\_NET\_WIFI\_BASE | NET\_REQUEST\_WIFI\_CMD\_AP\_ENABLE)

152

153[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)([NET\_REQUEST\_WIFI\_AP\_ENABLE](group__wifi__mgmt.md#ga638d2eb0a5029c1af46a91b523ed8589));

154

[ 156](group__wifi__mgmt.md#gaf81f62bf4c9e331a095acbf0d24ca1a2)#define NET\_REQUEST\_WIFI\_AP\_DISABLE \

157 (\_NET\_WIFI\_BASE | NET\_REQUEST\_WIFI\_CMD\_AP\_DISABLE)

158

159[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)([NET\_REQUEST\_WIFI\_AP\_DISABLE](group__wifi__mgmt.md#gaf81f62bf4c9e331a095acbf0d24ca1a2));

160

[ 162](group__wifi__mgmt.md#ga3e45f6ee3801553619d8eb7d0af506eb)#define NET\_REQUEST\_WIFI\_IFACE\_STATUS \

163 (\_NET\_WIFI\_BASE | NET\_REQUEST\_WIFI\_CMD\_IFACE\_STATUS)

164

165[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)([NET\_REQUEST\_WIFI\_IFACE\_STATUS](group__wifi__mgmt.md#ga3e45f6ee3801553619d8eb7d0af506eb));

166

[ 167](group__wifi__mgmt.md#gadd9b5b206c7ee2e40c30a37c7b4fc002)#define NET\_REQUEST\_WIFI\_11K\_CONFIG \

168 (\_NET\_WIFI\_BASE | NET\_REQUEST\_WIFI\_CMD\_11K\_CONFIG)

169

170[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)([NET\_REQUEST\_WIFI\_11K\_CONFIG](group__wifi__mgmt.md#gadd9b5b206c7ee2e40c30a37c7b4fc002));

171

[ 172](group__wifi__mgmt.md#ga4a2b1e8befd7376749b1d4fbcf98376f)#define NET\_REQUEST\_WIFI\_11K\_NEIGHBOR\_REQUEST \

173 (\_NET\_WIFI\_BASE | NET\_REQUEST\_WIFI\_CMD\_11K\_NEIGHBOR\_REQUEST)

174

175[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)([NET\_REQUEST\_WIFI\_11K\_NEIGHBOR\_REQUEST](group__wifi__mgmt.md#ga4a2b1e8befd7376749b1d4fbcf98376f));

176

[ 178](group__wifi__mgmt.md#ga68aaced888f98e1ba4e6b61b53e5e2ba)#define NET\_REQUEST\_WIFI\_PS \

179 (\_NET\_WIFI\_BASE | NET\_REQUEST\_WIFI\_CMD\_PS)

180

181[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)([NET\_REQUEST\_WIFI\_PS](group__wifi__mgmt.md#ga68aaced888f98e1ba4e6b61b53e5e2ba));

182

[ 184](group__wifi__mgmt.md#gab84fd7e9ca0bf0b2b9d08889dda26aad)#define NET\_REQUEST\_WIFI\_TWT \

185 (\_NET\_WIFI\_BASE | NET\_REQUEST\_WIFI\_CMD\_TWT)

186

187[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)([NET\_REQUEST\_WIFI\_TWT](group__wifi__mgmt.md#gab84fd7e9ca0bf0b2b9d08889dda26aad));

188

[ 190](group__wifi__mgmt.md#ga1032f3773cfe6130da4d4d498b044ee2)#define NET\_REQUEST\_WIFI\_PS\_CONFIG \

191 (\_NET\_WIFI\_BASE | NET\_REQUEST\_WIFI\_CMD\_PS\_CONFIG)

192

193[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)([NET\_REQUEST\_WIFI\_PS\_CONFIG](group__wifi__mgmt.md#ga1032f3773cfe6130da4d4d498b044ee2));

194

[ 196](group__wifi__mgmt.md#ga2b27d102b779a6d846b375854768fb7f)#define NET\_REQUEST\_WIFI\_REG\_DOMAIN \

197 (\_NET\_WIFI\_BASE | NET\_REQUEST\_WIFI\_CMD\_REG\_DOMAIN)

198

199[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)([NET\_REQUEST\_WIFI\_REG\_DOMAIN](group__wifi__mgmt.md#ga2b27d102b779a6d846b375854768fb7f));

200

[ 202](group__wifi__mgmt.md#ga9b4da60a8108b0cc431ac1eecfca0cd0)#define NET\_REQUEST\_WIFI\_MODE \

203 (\_NET\_WIFI\_BASE | NET\_REQUEST\_WIFI\_CMD\_MODE)

204

205[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)([NET\_REQUEST\_WIFI\_MODE](group__wifi__mgmt.md#ga9b4da60a8108b0cc431ac1eecfca0cd0));

206

[ 208](group__wifi__mgmt.md#ga3098e817d12bf4619c9fd2698508fb4e)#define NET\_REQUEST\_WIFI\_PACKET\_FILTER \

209 (\_NET\_WIFI\_BASE | NET\_REQUEST\_WIFI\_CMD\_PACKET\_FILTER)

210

211[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)([NET\_REQUEST\_WIFI\_PACKET\_FILTER](group__wifi__mgmt.md#ga3098e817d12bf4619c9fd2698508fb4e));

212

[ 214](group__wifi__mgmt.md#gad9614d2368f8399850aaec05e40bdc78)#define NET\_REQUEST\_WIFI\_CHANNEL \

215 (\_NET\_WIFI\_BASE | NET\_REQUEST\_WIFI\_CMD\_CHANNEL)

216

217[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)([NET\_REQUEST\_WIFI\_CHANNEL](group__wifi__mgmt.md#gad9614d2368f8399850aaec05e40bdc78));

218

[ 220](group__wifi__mgmt.md#gaa3e52e08d89a1104f07207e52b81d503)#define NET\_REQUEST\_WIFI\_AP\_STA\_DISCONNECT \

221 (\_NET\_WIFI\_BASE | NET\_REQUEST\_WIFI\_CMD\_AP\_STA\_DISCONNECT)

222

223[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)([NET\_REQUEST\_WIFI\_AP\_STA\_DISCONNECT](group__wifi__mgmt.md#gaa3e52e08d89a1104f07207e52b81d503));

224

[ 226](group__wifi__mgmt.md#ga3e60c29ca9ce95d17a7fff087290f7f1)#define NET\_REQUEST\_WIFI\_VERSION \

227 (\_NET\_WIFI\_BASE | NET\_REQUEST\_WIFI\_CMD\_VERSION)

228

229[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)([NET\_REQUEST\_WIFI\_VERSION](group__wifi__mgmt.md#ga3e60c29ca9ce95d17a7fff087290f7f1));

230

[ 232](group__wifi__mgmt.md#gac6483341435ff380a2d4a69430899c1a)#define NET\_REQUEST\_WIFI\_CONN\_PARAMS \

233 (\_NET\_WIFI\_BASE | NET\_REQUEST\_WIFI\_CMD\_CONN\_PARAMS)

234

235[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)([NET\_REQUEST\_WIFI\_CONN\_PARAMS](group__wifi__mgmt.md#gac6483341435ff380a2d4a69430899c1a));

236

[ 238](group__wifi__mgmt.md#ga22d80ef0ffb15e4286d7b1c3325d5334)#define NET\_REQUEST\_WIFI\_RTS\_THRESHOLD \

239 (\_NET\_WIFI\_BASE | NET\_REQUEST\_WIFI\_CMD\_RTS\_THRESHOLD)

240

241[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)([NET\_REQUEST\_WIFI\_RTS\_THRESHOLD](group__wifi__mgmt.md#ga22d80ef0ffb15e4286d7b1c3325d5334));

242

[ 244](group__wifi__mgmt.md#gaf4a78d230f5e0743a6aaf152ddda1c67)#define NET\_REQUEST\_WIFI\_AP\_CONFIG\_PARAM \

245 (\_NET\_WIFI\_BASE | NET\_REQUEST\_WIFI\_CMD\_AP\_CONFIG\_PARAM)

246

247[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)([NET\_REQUEST\_WIFI\_AP\_CONFIG\_PARAM](group__wifi__mgmt.md#gaf4a78d230f5e0743a6aaf152ddda1c67));

248

249#ifdef CONFIG\_WIFI\_NM\_WPA\_SUPPLICANT\_DPP

251#define NET\_REQUEST\_WIFI\_DPP \

252 (\_NET\_WIFI\_BASE | NET\_REQUEST\_WIFI\_CMD\_DPP)

253

254[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_WIFI\_DPP);

255#endif /\* CONFIG\_WIFI\_NM\_WPA\_SUPPLICANT\_DPP \*/

256

257#ifdef CONFIG\_WIFI\_NM\_WPA\_SUPPLICANT\_WNM

259#define NET\_REQUEST\_WIFI\_BTM\_QUERY (\_NET\_WIFI\_BASE | NET\_REQUEST\_WIFI\_CMD\_BTM\_QUERY)

260

261[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_WIFI\_BTM\_QUERY);

262#endif

263

[ 265](group__wifi__mgmt.md#ga9070995249eb35de37e2b60c4426f840)#define NET\_REQUEST\_WIFI\_PMKSA\_FLUSH \

266 (\_NET\_WIFI\_BASE | NET\_REQUEST\_WIFI\_CMD\_PMKSA\_FLUSH)

267

268[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)([NET\_REQUEST\_WIFI\_PMKSA\_FLUSH](group__wifi__mgmt.md#ga9070995249eb35de37e2b60c4426f840));

269

[ 271](group__wifi__mgmt.md#gae5dc7835e11487187663dfe65a15f22b)#define NET\_REQUEST\_WIFI\_ENTERPRISE\_CREDS \

272 (\_NET\_WIFI\_BASE | NET\_REQUEST\_WIFI\_CMD\_ENTERPRISE\_CREDS)

273

274[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)([NET\_REQUEST\_WIFI\_ENTERPRISE\_CREDS](group__wifi__mgmt.md#gae5dc7835e11487187663dfe65a15f22b));

275

[ 277](group__wifi__mgmt.md#ga2678ea372335af008d9bd3333f7a7de1)#define NET\_REQUEST\_WIFI\_RTS\_THRESHOLD\_CONFIG \

278 (\_NET\_WIFI\_BASE | NET\_REQUEST\_WIFI\_CMD\_RTS\_THRESHOLD\_CONFIG)

279

280[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)([NET\_REQUEST\_WIFI\_RTS\_THRESHOLD\_CONFIG](group__wifi__mgmt.md#ga2678ea372335af008d9bd3333f7a7de1));

281

[ 282](group__wifi__mgmt.md#ga649a63bc7d315ebdd89464ff48b3fada)#define NET\_REQUEST\_WIFI\_WPS\_CONFIG (\_NET\_WIFI\_BASE | NET\_REQUEST\_WIFI\_CMD\_WPS\_CONFIG)

283

284[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)([NET\_REQUEST\_WIFI\_WPS\_CONFIG](group__wifi__mgmt.md#ga649a63bc7d315ebdd89464ff48b3fada));

285#ifdef CONFIG\_WIFI\_CREDENTIALS\_CONNECT\_STORED

286#define NET\_REQUEST\_WIFI\_CONNECT\_STORED (\_NET\_WIFI\_BASE | NET\_REQUEST\_WIFI\_CMD\_CONNECT\_STORED)

287

288[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_WIFI\_CONNECT\_STORED);

289#endif

290

[ 291](group__wifi__mgmt.md#ga89cc123bb5c30140d2ce0a8b741b1086)#define NET\_REQUEST\_WIFI\_START\_ROAMING \

292 (\_NET\_WIFI\_BASE | NET\_REQUEST\_WIFI\_CMD\_START\_ROAMING)

293

294[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)([NET\_REQUEST\_WIFI\_START\_ROAMING](group__wifi__mgmt.md#ga89cc123bb5c30140d2ce0a8b741b1086));

295

[ 296](group__wifi__mgmt.md#ga373031970a29331bf1b30d1654c128f0)#define NET\_REQUEST\_WIFI\_NEIGHBOR\_REP\_COMPLETE \

297 (\_NET\_WIFI\_BASE | NET\_REQUEST\_WIFI\_CMD\_NEIGHBOR\_REP\_COMPLETE)

298

299[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)([NET\_REQUEST\_WIFI\_NEIGHBOR\_REP\_COMPLETE](group__wifi__mgmt.md#ga373031970a29331bf1b30d1654c128f0));

300

[ 302](group__wifi__mgmt.md#gac2638308cbb0d268831f1618cf8e1fa8)enum [net\_event\_wifi\_cmd](group__wifi__mgmt.md#gac2638308cbb0d268831f1618cf8e1fa8) {

[ 304](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8a37e9ab2a6832153fa968337d920e587e) [NET\_EVENT\_WIFI\_CMD\_SCAN\_RESULT](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8a37e9ab2a6832153fa968337d920e587e) = 1,

[ 306](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8ad753b7e4588257815f4a60a539ca2018) [NET\_EVENT\_WIFI\_CMD\_SCAN\_DONE](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8ad753b7e4588257815f4a60a539ca2018),

[ 308](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8af76f28777b91b365dc3f97028bc18e3c) [NET\_EVENT\_WIFI\_CMD\_CONNECT\_RESULT](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8af76f28777b91b365dc3f97028bc18e3c),

[ 310](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8a3a3b0387f83d8fb24a0e27312468b0eb) [NET\_EVENT\_WIFI\_CMD\_DISCONNECT\_RESULT](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8a3a3b0387f83d8fb24a0e27312468b0eb),

[ 312](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8af4b3f1969b96f63253851c26c3882a14) [NET\_EVENT\_WIFI\_CMD\_IFACE\_STATUS](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8af4b3f1969b96f63253851c26c3882a14),

[ 314](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8adad71603ed829ed92d06f8c40efa9b18) [NET\_EVENT\_WIFI\_CMD\_TWT](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8adad71603ed829ed92d06f8c40efa9b18),

[ 318](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8a78838bf7ce80cee5e803712cd0286750) [NET\_EVENT\_WIFI\_CMD\_TWT\_SLEEP\_STATE](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8a78838bf7ce80cee5e803712cd0286750),

[ 320](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8addf15c69512be7ab4957e7c0b3fde0ac) [NET\_EVENT\_WIFI\_CMD\_RAW\_SCAN\_RESULT](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8addf15c69512be7ab4957e7c0b3fde0ac),

[ 322](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8af1c42bd59f01260c64ede07da436c18f) [NET\_EVENT\_WIFI\_CMD\_DISCONNECT\_COMPLETE](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8af1c42bd59f01260c64ede07da436c18f),

[ 324](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8acc9d8a16d99e4006b915b3686522a8e0) [NET\_EVENT\_WIFI\_CMD\_SIGNAL\_CHANGE](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8acc9d8a16d99e4006b915b3686522a8e0),

[ 326](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8a75a0a093f32fa2577286c92c2525df91) [NET\_EVENT\_WIFI\_CMD\_NEIGHBOR\_REP\_RECEIVED](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8a75a0a093f32fa2577286c92c2525df91),

[ 328](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8a86b6811a06f6158ae9ea4687e219e5af) [NET\_EVENT\_WIFI\_CMD\_NEIGHBOR\_REP\_COMPLETE](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8a86b6811a06f6158ae9ea4687e219e5af),

[ 330](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8abd1797564427886eeb14dd293ae86a9b) [NET\_EVENT\_WIFI\_CMD\_AP\_ENABLE\_RESULT](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8abd1797564427886eeb14dd293ae86a9b),

[ 332](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8aeec3d7a9191280c2326034a17555308d) [NET\_EVENT\_WIFI\_CMD\_AP\_DISABLE\_RESULT](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8aeec3d7a9191280c2326034a17555308d),

[ 334](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8abd4269b2cd1302ce61da4f8d7bb9d5fb) [NET\_EVENT\_WIFI\_CMD\_AP\_STA\_CONNECTED](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8abd4269b2cd1302ce61da4f8d7bb9d5fb),

[ 336](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8a3678a39f9542968958b5575d571d4e2e) [NET\_EVENT\_WIFI\_CMD\_AP\_STA\_DISCONNECTED](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8a3678a39f9542968958b5575d571d4e2e),

[ 338](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8a4ec52c22e23502421077e46e94facf08) [NET\_EVENT\_WIFI\_CMD\_SUPPLICANT](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8a4ec52c22e23502421077e46e94facf08),

339};

340

[ 342](group__wifi__mgmt.md#ga436a927d47eb9abe683b89f2b128cd6e)#define NET\_EVENT\_WIFI\_SCAN\_RESULT \

343 (\_NET\_WIFI\_EVENT | NET\_EVENT\_WIFI\_CMD\_SCAN\_RESULT)

344

[ 346](group__wifi__mgmt.md#ga8ce35a12e5338e9a65970382b4a26b88)#define NET\_EVENT\_WIFI\_SCAN\_DONE \

347 (\_NET\_WIFI\_EVENT | NET\_EVENT\_WIFI\_CMD\_SCAN\_DONE)

348

[ 350](group__wifi__mgmt.md#ga0e8feafcc5efd85d04be91f407c0b7c4)#define NET\_EVENT\_WIFI\_CONNECT\_RESULT \

351 (\_NET\_WIFI\_EVENT | NET\_EVENT\_WIFI\_CMD\_CONNECT\_RESULT)

352

[ 354](group__wifi__mgmt.md#ga8cbbe69bd60f42fdbb06f4f1e15410c8)#define NET\_EVENT\_WIFI\_DISCONNECT\_RESULT \

355 (\_NET\_WIFI\_EVENT | NET\_EVENT\_WIFI\_CMD\_DISCONNECT\_RESULT)

356

[ 358](group__wifi__mgmt.md#ga99e11fc15582b94d4243de7733e47ebb)#define NET\_EVENT\_WIFI\_IFACE\_STATUS \

359 (\_NET\_WIFI\_EVENT | NET\_EVENT\_WIFI\_CMD\_IFACE\_STATUS)

360

[ 362](group__wifi__mgmt.md#gaeb968a5d2a8d68a8c634cca18dbcf9c6)#define NET\_EVENT\_WIFI\_TWT \

363 (\_NET\_WIFI\_EVENT | NET\_EVENT\_WIFI\_CMD\_TWT)

364

[ 366](group__wifi__mgmt.md#ga682d95b5d06a9b175c10d712acca8a49)#define NET\_EVENT\_WIFI\_TWT\_SLEEP\_STATE \

367 (\_NET\_WIFI\_EVENT | NET\_EVENT\_WIFI\_CMD\_TWT\_SLEEP\_STATE)

368

[ 370](group__wifi__mgmt.md#gaea8d222282ddef6992330763afc759a4)#define NET\_EVENT\_WIFI\_RAW\_SCAN\_RESULT \

371 (\_NET\_WIFI\_EVENT | NET\_EVENT\_WIFI\_CMD\_RAW\_SCAN\_RESULT)

372

[ 374](group__wifi__mgmt.md#ga40027feb7ec42c846fd99b56bbd2256d)#define NET\_EVENT\_WIFI\_DISCONNECT\_COMPLETE \

375 (\_NET\_WIFI\_EVENT | NET\_EVENT\_WIFI\_CMD\_DISCONNECT\_COMPLETE)

376

[ 378](group__wifi__mgmt.md#ga8da47e9d3e594840fb7a7d59f45ea9ce)#define NET\_EVENT\_WIFI\_SIGNAL\_CHANGE \

379 (\_NET\_WIFI\_EVENT | NET\_EVENT\_WIFI\_CMD\_SIGNAL\_CHANGE)

380

[ 382](group__wifi__mgmt.md#ga7ed4bc9f25055f5a35270a4c6a0bedcc)#define NET\_EVENT\_WIFI\_NEIGHBOR\_REP\_COMP \

383 (\_NET\_WIFI\_EVENT | NET\_EVENT\_WIFI\_CMD\_NEIGHBOR\_REP\_COMPLETE)

384

[ 386](group__wifi__mgmt.md#ga1d678fbae0f092814392c0ab4087cb73)#define NET\_EVENT\_WIFI\_AP\_ENABLE\_RESULT \

387 (\_NET\_WIFI\_EVENT | NET\_EVENT\_WIFI\_CMD\_AP\_ENABLE\_RESULT)

388

[ 390](group__wifi__mgmt.md#ga104296fdb38edf868bea1a46f572d101)#define NET\_EVENT\_WIFI\_AP\_DISABLE\_RESULT \

391 (\_NET\_WIFI\_EVENT | NET\_EVENT\_WIFI\_CMD\_AP\_DISABLE\_RESULT)

392

[ 394](group__wifi__mgmt.md#gacc392179948bfd5bed6702dc8fb5cd9d)#define NET\_EVENT\_WIFI\_AP\_STA\_CONNECTED \

395 (\_NET\_WIFI\_EVENT | NET\_EVENT\_WIFI\_CMD\_AP\_STA\_CONNECTED)

396

[ 398](group__wifi__mgmt.md#ga3e8154ce1808665dd165f793ddec1673)#define NET\_EVENT\_WIFI\_AP\_STA\_DISCONNECTED \

399 (\_NET\_WIFI\_EVENT | NET\_EVENT\_WIFI\_CMD\_AP\_STA\_DISCONNECTED)

400

[ 402](structwifi__version.md)struct [wifi\_version](structwifi__version.md) {

[ 404](structwifi__version.md#aea828bdb512440d6aa3cc853525c4971) const char \*[drv\_version](structwifi__version.md#aea828bdb512440d6aa3cc853525c4971);

[ 406](structwifi__version.md#a4bf2cbdf5c43ff21718ccf19646c164e) const char \*[fw\_version](structwifi__version.md#a4bf2cbdf5c43ff21718ccf19646c164e);

407};

408

[ 412](structwifi__band__channel.md)struct [wifi\_band\_channel](structwifi__band__channel.md) {

[ 414](structwifi__band__channel.md#a4a932599429f37231f76c3064ec5efb3) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [band](structwifi__band__channel.md#a4a932599429f37231f76c3064ec5efb3);

[ 416](structwifi__band__channel.md#acd0dd7366de3650124dad7232a58ade0) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [channel](structwifi__band__channel.md#acd0dd7366de3650124dad7232a58ade0);

417};

418

[ 424](structwifi__scan__params.md)struct [wifi\_scan\_params](structwifi__scan__params.md) {

[ 432](structwifi__scan__params.md#a645acc54603cd4692527c1a028933078) enum [wifi\_scan\_type](group__wifi__mgmt.md#gad30e29eda65ccafdbd7f11865937b8ea) [scan\_type](structwifi__scan__params.md#a645acc54603cd4692527c1a028933078);

[ 436](structwifi__scan__params.md#a6b571d960ed9d7419e31530e5fb6f97a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bands](structwifi__scan__params.md#a6b571d960ed9d7419e31530e5fb6f97a);

[ 439](structwifi__scan__params.md#a2453a75c23e04e3572559c0e7199c1b4) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [dwell\_time\_active](structwifi__scan__params.md#a2453a75c23e04e3572559c0e7199c1b4);

[ 442](structwifi__scan__params.md#a8e7a37ccda8de635e7b7066d7943e814) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [dwell\_time\_passive](structwifi__scan__params.md#a8e7a37ccda8de635e7b7066d7943e814);

[ 445](structwifi__scan__params.md#aac11ee8e0ec8a4fa24668f4820bd1a12) const char \*[ssids](structwifi__scan__params.md#aac11ee8e0ec8a4fa24668f4820bd1a12)[WIFI\_MGMT\_SCAN\_SSID\_FILT\_MAX];

[ 453](structwifi__scan__params.md#a12d5dea7d8fa8ad03ac2366720c46243) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [max\_bss\_cnt](structwifi__scan__params.md#a12d5dea7d8fa8ad03ac2366720c46243);

[ 468](structwifi__scan__params.md#aa5ddbd6bc97b7598288d4b0d38521681) struct [wifi\_band\_channel](structwifi__band__channel.md) [band\_chan](structwifi__scan__params.md#aa5ddbd6bc97b7598288d4b0d38521681)[WIFI\_MGMT\_SCAN\_CHAN\_MAX\_MANUAL];

469};

470

[ 474](structwifi__scan__result.md)struct [wifi\_scan\_result](structwifi__scan__result.md) {

[ 476](structwifi__scan__result.md#aaefb8f5c9510e4f5002ae306d853ade8) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [ssid](structwifi__scan__result.md#aaefb8f5c9510e4f5002ae306d853ade8)[[WIFI\_SSID\_MAX\_LEN](group__wifi__mgmt.md#gad62c60666c9fdffe2e0e9c4388f87886) + 1];

[ 478](structwifi__scan__result.md#a2c1c2f4265b914df08fc75deb8b69d39) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [ssid\_length](structwifi__scan__result.md#a2c1c2f4265b914df08fc75deb8b69d39);

[ 480](structwifi__scan__result.md#a38201c9dd798dc11b5bda3ce97b02e92) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [band](structwifi__scan__result.md#a38201c9dd798dc11b5bda3ce97b02e92);

[ 482](structwifi__scan__result.md#adbbfd7692ee5ffd6344fe78b9d91c840) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [channel](structwifi__scan__result.md#adbbfd7692ee5ffd6344fe78b9d91c840);

[ 484](structwifi__scan__result.md#af2d3dc5d115e3db76d3bc115510b0a5a) enum [wifi\_security\_type](group__wifi__mgmt.md#gadde31a04fa25ed805115c6b31854cd9c) [security](structwifi__scan__result.md#af2d3dc5d115e3db76d3bc115510b0a5a);

[ 486](structwifi__scan__result.md#acaa3fb30ebf6df22bfac6380698ed28e) enum [wifi\_mfp\_options](group__wifi__mgmt.md#ga1f252da47d9650023d7fff6d08e49c76) [mfp](structwifi__scan__result.md#acaa3fb30ebf6df22bfac6380698ed28e);

[ 488](structwifi__scan__result.md#a76aa012136e3721fd4a482a22b93546f) [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) [rssi](structwifi__scan__result.md#a76aa012136e3721fd4a482a22b93546f);

[ 490](structwifi__scan__result.md#a4fdbc4dc4d5c8b279223e8c06624f434) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [mac](structwifi__scan__result.md#a4fdbc4dc4d5c8b279223e8c06624f434)[[WIFI\_MAC\_ADDR\_LEN](group__wifi__mgmt.md#ga29409ff83a53c6464decdde9bdd04de6)];

[ 492](structwifi__scan__result.md#a8fca0dabec00ebd7ed4800098ec9d451) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [mac\_length](structwifi__scan__result.md#a8fca0dabec00ebd7ed4800098ec9d451);

493};

494

[ 496](structwifi__connect__req__params.md)struct [wifi\_connect\_req\_params](structwifi__connect__req__params.md) {

[ 498](structwifi__connect__req__params.md#ac260c2cd17a3f36ea101edaf23d41083) const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[ssid](structwifi__connect__req__params.md#ac260c2cd17a3f36ea101edaf23d41083);

[ 500](structwifi__connect__req__params.md#a547dddf6be5dd77eda74b1085a798400) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [ssid\_length](structwifi__connect__req__params.md#a547dddf6be5dd77eda74b1085a798400); /\* Max 32 \*/

[ 502](structwifi__connect__req__params.md#aa7743f0ecbc27a9595720ce13ce57c1d) const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[psk](structwifi__connect__req__params.md#aa7743f0ecbc27a9595720ce13ce57c1d);

[ 504](structwifi__connect__req__params.md#aaf7455a65590d19f047214b459a2dcb9) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [psk\_length](structwifi__connect__req__params.md#aaf7455a65590d19f047214b459a2dcb9); /\* Min 8 - Max 64 \*/

[ 506](structwifi__connect__req__params.md#a469fac5758b78fc425911837930b2060) const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[sae\_password](structwifi__connect__req__params.md#a469fac5758b78fc425911837930b2060);

[ 508](structwifi__connect__req__params.md#a74f0819e7a546ffb8bfb0ec587eccf20) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [sae\_password\_length](structwifi__connect__req__params.md#a74f0819e7a546ffb8bfb0ec587eccf20); /\* No length restrictions \*/

[ 510](structwifi__connect__req__params.md#aa2fea1881a8ffdf5d7093ae295867f3e) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [band](structwifi__connect__req__params.md#aa2fea1881a8ffdf5d7093ae295867f3e);

[ 512](structwifi__connect__req__params.md#a52b6d0323c35d03ec239f40be35cae72) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [channel](structwifi__connect__req__params.md#a52b6d0323c35d03ec239f40be35cae72);

[ 514](structwifi__connect__req__params.md#a18dce6bb021086877a30e7a04f5b24b9) enum [wifi\_security\_type](group__wifi__mgmt.md#gadde31a04fa25ed805115c6b31854cd9c) [security](structwifi__connect__req__params.md#a18dce6bb021086877a30e7a04f5b24b9);

[ 516](structwifi__connect__req__params.md#a745b3416172672a7e5b12bcc5b55e88c) enum [wifi\_mfp\_options](group__wifi__mgmt.md#ga1f252da47d9650023d7fff6d08e49c76) [mfp](structwifi__connect__req__params.md#a745b3416172672a7e5b12bcc5b55e88c);

[ 518](structwifi__connect__req__params.md#aa8081b9075ff9244cefd0ac1ef3f42cb) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bssid](structwifi__connect__req__params.md#aa8081b9075ff9244cefd0ac1ef3f42cb)[[WIFI\_MAC\_ADDR\_LEN](group__wifi__mgmt.md#ga29409ff83a53c6464decdde9bdd04de6)];

[ 520](structwifi__connect__req__params.md#a56183ba7f4d8eaf5fc5b495856adecfd) int [timeout](structwifi__connect__req__params.md#a56183ba7f4d8eaf5fc5b495856adecfd);

[ 522](structwifi__connect__req__params.md#a781456e079357e2e1096218af3bd218c) const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[anon\_id](structwifi__connect__req__params.md#a781456e079357e2e1096218af3bd218c);

[ 524](structwifi__connect__req__params.md#a2892253024b70e5cb8eb2166b17ebe22) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [aid\_length](structwifi__connect__req__params.md#a2892253024b70e5cb8eb2166b17ebe22);

[ 526](structwifi__connect__req__params.md#a4946647659a347667ee49bb6990bba66) const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[key\_passwd](structwifi__connect__req__params.md#a4946647659a347667ee49bb6990bba66);

[ 528](structwifi__connect__req__params.md#a9f913fc0ccecafaba488e444d701fd68) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [key\_passwd\_length](structwifi__connect__req__params.md#a9f913fc0ccecafaba488e444d701fd68);

[ 530](structwifi__connect__req__params.md#a020fc58d7e5350cc803cd5d6fa575e6a) const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[key2\_passwd](structwifi__connect__req__params.md#a020fc58d7e5350cc803cd5d6fa575e6a);

[ 532](structwifi__connect__req__params.md#af7b163cc2bffc59f7fa31f47c5e52062) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [key2\_passwd\_length](structwifi__connect__req__params.md#af7b163cc2bffc59f7fa31f47c5e52062);

[ 534](structwifi__connect__req__params.md#ac8eaaecd8227e5500bdaf8cddf05a065) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [suiteb\_type](structwifi__connect__req__params.md#ac8eaaecd8227e5500bdaf8cddf05a065);

[ 536](structwifi__connect__req__params.md#aa903297e7ee4801b350b2e3a3a89f28a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [eap\_ver](structwifi__connect__req__params.md#aa903297e7ee4801b350b2e3a3a89f28a);

[ 538](structwifi__connect__req__params.md#ab9c65599409387af65a3c2895c3116da) const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[eap\_identity](structwifi__connect__req__params.md#ab9c65599409387af65a3c2895c3116da);

[ 540](structwifi__connect__req__params.md#a4da02ff112c09f55dc5bddcda27d16a3) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [eap\_id\_length](structwifi__connect__req__params.md#a4da02ff112c09f55dc5bddcda27d16a3);

[ 542](structwifi__connect__req__params.md#afd046e702739c4a0d89322ee41b37acd) const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[eap\_password](structwifi__connect__req__params.md#afd046e702739c4a0d89322ee41b37acd);

[ 544](structwifi__connect__req__params.md#aeab22e95a04a1831b87beda1772d3db7) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [eap\_passwd\_length](structwifi__connect__req__params.md#aeab22e95a04a1831b87beda1772d3db7);

[ 546](structwifi__connect__req__params.md#a047b11e703fb646d778785dfcb14257b) bool [ft\_used](structwifi__connect__req__params.md#a047b11e703fb646d778785dfcb14257b);

547};

548

[ 552](group__wifi__mgmt.md#ga86a5741e54aeb3e290142b0de217b8a8)enum [wifi\_conn\_status](group__wifi__mgmt.md#ga86a5741e54aeb3e290142b0de217b8a8) {

[ 554](group__wifi__mgmt.md#gga86a5741e54aeb3e290142b0de217b8a8a380410b02b1e12599f37d1dcb844f5bd) [WIFI\_STATUS\_CONN\_SUCCESS](group__wifi__mgmt.md#gga86a5741e54aeb3e290142b0de217b8a8a380410b02b1e12599f37d1dcb844f5bd) = 0,

[ 556](group__wifi__mgmt.md#gga86a5741e54aeb3e290142b0de217b8a8ab80ec4b70c75695fbe698034e2cb6a44) [WIFI\_STATUS\_CONN\_FAIL](group__wifi__mgmt.md#gga86a5741e54aeb3e290142b0de217b8a8ab80ec4b70c75695fbe698034e2cb6a44),

[ 565](group__wifi__mgmt.md#gga86a5741e54aeb3e290142b0de217b8a8a90d91f96a35c9f6847cbc7abd8c20bf8) [WIFI\_STATUS\_CONN\_WRONG\_PASSWORD](group__wifi__mgmt.md#gga86a5741e54aeb3e290142b0de217b8a8a90d91f96a35c9f6847cbc7abd8c20bf8),

[ 567](group__wifi__mgmt.md#gga86a5741e54aeb3e290142b0de217b8a8abb8783b92aec2ed1ffc6331979888563) [WIFI\_STATUS\_CONN\_TIMEOUT](group__wifi__mgmt.md#gga86a5741e54aeb3e290142b0de217b8a8abb8783b92aec2ed1ffc6331979888563),

[ 569](group__wifi__mgmt.md#gga86a5741e54aeb3e290142b0de217b8a8a2ae79fa389bb447fa108e0107aeff2f4) [WIFI\_STATUS\_CONN\_AP\_NOT\_FOUND](group__wifi__mgmt.md#gga86a5741e54aeb3e290142b0de217b8a8a2ae79fa389bb447fa108e0107aeff2f4),

[ 571](group__wifi__mgmt.md#gga86a5741e54aeb3e290142b0de217b8a8aeee5fb8d8c3e7905554d08331f06191f) [WIFI\_STATUS\_CONN\_LAST\_STATUS](group__wifi__mgmt.md#gga86a5741e54aeb3e290142b0de217b8a8aeee5fb8d8c3e7905554d08331f06191f),

[ 573](group__wifi__mgmt.md#gga86a5741e54aeb3e290142b0de217b8a8abe1401e5d516c0d63291add15e558b18) [WIFI\_STATUS\_DISCONN\_FIRST\_STATUS](group__wifi__mgmt.md#gga86a5741e54aeb3e290142b0de217b8a8abe1401e5d516c0d63291add15e558b18) = [WIFI\_STATUS\_CONN\_LAST\_STATUS](group__wifi__mgmt.md#gga86a5741e54aeb3e290142b0de217b8a8aeee5fb8d8c3e7905554d08331f06191f),

574};

575

[ 579](group__wifi__mgmt.md#gac782af0a60b202fd19597cabb7bd3a9a)enum [wifi\_disconn\_reason](group__wifi__mgmt.md#gac782af0a60b202fd19597cabb7bd3a9a) {

[ 581](group__wifi__mgmt.md#ggac782af0a60b202fd19597cabb7bd3a9aa5c894399db8949a789ca4f5750b6f042) [WIFI\_REASON\_DISCONN\_SUCCESS](group__wifi__mgmt.md#ggac782af0a60b202fd19597cabb7bd3a9aa5c894399db8949a789ca4f5750b6f042) = 0,

[ 583](group__wifi__mgmt.md#ggac782af0a60b202fd19597cabb7bd3a9aa87f5d64a9fd3acf8d67c698199779e5c) [WIFI\_REASON\_DISCONN\_UNSPECIFIED](group__wifi__mgmt.md#ggac782af0a60b202fd19597cabb7bd3a9aa87f5d64a9fd3acf8d67c698199779e5c),

[ 585](group__wifi__mgmt.md#ggac782af0a60b202fd19597cabb7bd3a9aaee75adafb52bd6ecaa547a76c6ccd0a7) [WIFI\_REASON\_DISCONN\_USER\_REQUEST](group__wifi__mgmt.md#ggac782af0a60b202fd19597cabb7bd3a9aaee75adafb52bd6ecaa547a76c6ccd0a7),

[ 587](group__wifi__mgmt.md#ggac782af0a60b202fd19597cabb7bd3a9aa34e3f78ce43db3daeaf32038e0baf204) [WIFI\_REASON\_DISCONN\_AP\_LEAVING](group__wifi__mgmt.md#ggac782af0a60b202fd19597cabb7bd3a9aa34e3f78ce43db3daeaf32038e0baf204),

[ 589](group__wifi__mgmt.md#ggac782af0a60b202fd19597cabb7bd3a9aa05fe2f87de30de47ee48f7615c2206e6) [WIFI\_REASON\_DISCONN\_INACTIVITY](group__wifi__mgmt.md#ggac782af0a60b202fd19597cabb7bd3a9aa05fe2f87de30de47ee48f7615c2206e6),

590};

591

[ 595](group__wifi__mgmt.md#gaaf730bf76adc06434c7ac63bf0417884)enum [wifi\_ap\_status](group__wifi__mgmt.md#gaaf730bf76adc06434c7ac63bf0417884) {

[ 597](group__wifi__mgmt.md#ggaaf730bf76adc06434c7ac63bf0417884a0df52848da8735892d0eb1e381b2cd7c) [WIFI\_STATUS\_AP\_SUCCESS](group__wifi__mgmt.md#ggaaf730bf76adc06434c7ac63bf0417884a0df52848da8735892d0eb1e381b2cd7c) = 0,

[ 599](group__wifi__mgmt.md#ggaaf730bf76adc06434c7ac63bf0417884a6c6801381caa3862004662169202fa9a) [WIFI\_STATUS\_AP\_FAIL](group__wifi__mgmt.md#ggaaf730bf76adc06434c7ac63bf0417884a6c6801381caa3862004662169202fa9a),

[ 601](group__wifi__mgmt.md#ggaaf730bf76adc06434c7ac63bf0417884a5acb85a2361ca72ed10966b829c5753b) [WIFI\_STATUS\_AP\_CHANNEL\_NOT\_SUPPORTED](group__wifi__mgmt.md#ggaaf730bf76adc06434c7ac63bf0417884a5acb85a2361ca72ed10966b829c5753b),

[ 603](group__wifi__mgmt.md#ggaaf730bf76adc06434c7ac63bf0417884a0b1cb592c54c16e8a54defee71c5fd15) [WIFI\_STATUS\_AP\_CHANNEL\_NOT\_ALLOWED](group__wifi__mgmt.md#ggaaf730bf76adc06434c7ac63bf0417884a0b1cb592c54c16e8a54defee71c5fd15),

[ 605](group__wifi__mgmt.md#ggaaf730bf76adc06434c7ac63bf0417884ac18a7b551f8c6bb7737b0e8e60c323ce) [WIFI\_STATUS\_AP\_SSID\_NOT\_ALLOWED](group__wifi__mgmt.md#ggaaf730bf76adc06434c7ac63bf0417884ac18a7b551f8c6bb7737b0e8e60c323ce),

[ 607](group__wifi__mgmt.md#ggaaf730bf76adc06434c7ac63bf0417884abe5a626d22051522255d98fdfdfbfcc8) [WIFI\_STATUS\_AP\_AUTH\_TYPE\_NOT\_SUPPORTED](group__wifi__mgmt.md#ggaaf730bf76adc06434c7ac63bf0417884abe5a626d22051522255d98fdfdfbfcc8),

[ 609](group__wifi__mgmt.md#ggaaf730bf76adc06434c7ac63bf0417884a2105e6c49b3bcb5f7dcacbc1e5ce9cca) [WIFI\_STATUS\_AP\_OP\_NOT\_SUPPORTED](group__wifi__mgmt.md#ggaaf730bf76adc06434c7ac63bf0417884a2105e6c49b3bcb5f7dcacbc1e5ce9cca),

[ 611](group__wifi__mgmt.md#ggaaf730bf76adc06434c7ac63bf0417884a36a58980bdc7877c910441590137ddbe) [WIFI\_STATUS\_AP\_OP\_NOT\_PERMITTED](group__wifi__mgmt.md#ggaaf730bf76adc06434c7ac63bf0417884a36a58980bdc7877c910441590137ddbe),

612};

613

[ 615](structwifi__status.md)struct [wifi\_status](structwifi__status.md) {

616 union {

[ 618](structwifi__status.md#aa1dbff8154400f8353693d387977008b) int [status](structwifi__status.md#aa1dbff8154400f8353693d387977008b);

[ 620](structwifi__status.md#a8f885e78366d0499e4ba8e15bef275ac) enum [wifi\_conn\_status](group__wifi__mgmt.md#ga86a5741e54aeb3e290142b0de217b8a8) [conn\_status](structwifi__status.md#a8f885e78366d0499e4ba8e15bef275ac);

[ 622](structwifi__status.md#aa04b5033d93274badd27f702af9830bc) enum [wifi\_disconn\_reason](group__wifi__mgmt.md#gac782af0a60b202fd19597cabb7bd3a9a) [disconn\_reason](structwifi__status.md#aa04b5033d93274badd27f702af9830bc);

[ 624](structwifi__status.md#a02f0fcc7ef57661ca95d0c99f045aef1) enum [wifi\_ap\_status](group__wifi__mgmt.md#gaaf730bf76adc06434c7ac63bf0417884) [ap\_status](structwifi__status.md#a02f0fcc7ef57661ca95d0c99f045aef1);

625 };

626};

627

[ 629](structwifi__iface__status.md)struct [wifi\_iface\_status](structwifi__iface__status.md) {

[ 631](structwifi__iface__status.md#ac52806155be3d64954ac6d109e76ec57) int [state](structwifi__iface__status.md#ac52806155be3d64954ac6d109e76ec57);

[ 633](structwifi__iface__status.md#ad82f281941e4f6ce1ef0bca008e26d41) unsigned int [ssid\_len](structwifi__iface__status.md#ad82f281941e4f6ce1ef0bca008e26d41);

[ 635](structwifi__iface__status.md#a3ab671471bcdfeb5b955d156d39f2bb3) char [ssid](structwifi__iface__status.md#a3ab671471bcdfeb5b955d156d39f2bb3)[[WIFI\_SSID\_MAX\_LEN](group__wifi__mgmt.md#gad62c60666c9fdffe2e0e9c4388f87886) + 1];

[ 637](structwifi__iface__status.md#a5d5d19056a1a15365fbdd94274a0fc5e) char [bssid](structwifi__iface__status.md#a5d5d19056a1a15365fbdd94274a0fc5e)[[WIFI\_MAC\_ADDR\_LEN](group__wifi__mgmt.md#ga29409ff83a53c6464decdde9bdd04de6)];

[ 639](structwifi__iface__status.md#ae1c141a18f4e225af2c22a8cb4f882a8) enum [wifi\_frequency\_bands](group__wifi__mgmt.md#ga1e2f0439a322355fa7368ea880c9c15d) [band](structwifi__iface__status.md#ae1c141a18f4e225af2c22a8cb4f882a8);

[ 641](structwifi__iface__status.md#a6432663156e5b2c424d254ed1eae0144) unsigned int [channel](structwifi__iface__status.md#a6432663156e5b2c424d254ed1eae0144);

[ 643](structwifi__iface__status.md#ad33d2ec149a8d556e2472dd842ceadc0) enum [wifi\_iface\_mode](group__wifi__mgmt.md#ga584f6239ac14e2bedc5e6bd72756423b) [iface\_mode](structwifi__iface__status.md#ad33d2ec149a8d556e2472dd842ceadc0);

[ 645](structwifi__iface__status.md#ae2de076d79f2172793d65fe9cd31edc4) enum [wifi\_link\_mode](group__wifi__mgmt.md#gabdb2a784d4727b71ab44cca04e422c62) [link\_mode](structwifi__iface__status.md#ae2de076d79f2172793d65fe9cd31edc4);

[ 647](structwifi__iface__status.md#a625ecec1abec8dd65cf155eab21a01b5) enum [wifi\_security\_type](group__wifi__mgmt.md#gadde31a04fa25ed805115c6b31854cd9c) [security](structwifi__iface__status.md#a625ecec1abec8dd65cf155eab21a01b5);

[ 649](structwifi__iface__status.md#aa1a9b644fd355526125ddd32416b7c24) enum [wifi\_mfp\_options](group__wifi__mgmt.md#ga1f252da47d9650023d7fff6d08e49c76) [mfp](structwifi__iface__status.md#aa1a9b644fd355526125ddd32416b7c24);

[ 651](structwifi__iface__status.md#a4e593147b88eb4938d55a4de72fcc7f6) int [rssi](structwifi__iface__status.md#a4e593147b88eb4938d55a4de72fcc7f6);

[ 653](structwifi__iface__status.md#aae6c8cbaa16c81d308f08114d5103a3d) unsigned char [dtim\_period](structwifi__iface__status.md#aae6c8cbaa16c81d308f08114d5103a3d);

[ 655](structwifi__iface__status.md#a241bfbe70628006b515b5f9e4f97665c) unsigned short [beacon\_interval](structwifi__iface__status.md#a241bfbe70628006b515b5f9e4f97665c);

[ 657](structwifi__iface__status.md#acfde8d64b463a9f553aa4fb689dc1917) bool [twt\_capable](structwifi__iface__status.md#acfde8d64b463a9f553aa4fb689dc1917);

[ 659](structwifi__iface__status.md#a59395eb7671b71135a9affd1b3be4102) int [current\_phy\_rate](structwifi__iface__status.md#a59395eb7671b71135a9affd1b3be4102);

660};

661

[ 663](structwifi__ps__params.md)struct [wifi\_ps\_params](structwifi__ps__params.md) {

[ 665](structwifi__ps__params.md#abb22aaa45833ac130922204bd2fe841b) enum [wifi\_ps](group__wifi__mgmt.md#ga0fffeb57b68fb8cdef9d3d571368b8ca) [enabled](structwifi__ps__params.md#abb22aaa45833ac130922204bd2fe841b);

[ 667](structwifi__ps__params.md#a8510c799ab0c5825f1c6349f9799c62f) unsigned short [listen\_interval](structwifi__ps__params.md#a8510c799ab0c5825f1c6349f9799c62f);

[ 669](structwifi__ps__params.md#a7cb3e7fb7d9f8bd7c2cab41f879b3b66) enum [wifi\_ps\_wakeup\_mode](group__wifi__mgmt.md#gac7f907644847e905d67c709fa4afae7f) [wakeup\_mode](structwifi__ps__params.md#a7cb3e7fb7d9f8bd7c2cab41f879b3b66);

[ 671](structwifi__ps__params.md#a5a022d89d43ecf2cd1f15fc72c0f2bed) enum [wifi\_ps\_mode](group__wifi__mgmt.md#gaffae7d2a754be5eb952ad2b83edad54c) [mode](structwifi__ps__params.md#a5a022d89d43ecf2cd1f15fc72c0f2bed);

[ 680](structwifi__ps__params.md#ad963f1bf78dc271f08b73f3aadb36a91) unsigned int [timeout\_ms](structwifi__ps__params.md#ad963f1bf78dc271f08b73f3aadb36a91);

[ 682](structwifi__ps__params.md#aef62e5bf6216bf4dc461efe71735c4bd) enum [wifi\_ps\_param\_type](group__wifi__mgmt.md#gabe45d132797047c098041331c8f6f912) [type](structwifi__ps__params.md#aef62e5bf6216bf4dc461efe71735c4bd);

[ 684](structwifi__ps__params.md#a63fa2ee03bc4aefada61c298ee14336c) enum [wifi\_config\_ps\_param\_fail\_reason](group__wifi__mgmt.md#gad98099584d2222ede93aba42b1fbaff0) [fail\_reason](structwifi__ps__params.md#a63fa2ee03bc4aefada61c298ee14336c);

[ 686](structwifi__ps__params.md#ab9fc62dd1e2928320274fa1554a550a6) enum [wifi\_ps\_exit\_strategy](group__wifi__mgmt.md#ga2d424d1711389fb784e916a87ff854b7) [exit\_strategy](structwifi__ps__params.md#ab9fc62dd1e2928320274fa1554a550a6);

687};

688

[ 690](structwifi__twt__params.md)struct [wifi\_twt\_params](structwifi__twt__params.md) {

[ 692](structwifi__twt__params.md#a6f0483861a387651c9c89ba182e064bd) enum [wifi\_twt\_operation](group__wifi__mgmt.md#gad0e998aeb1b27c4f203ca76339d323a3) [operation](structwifi__twt__params.md#a6f0483861a387651c9c89ba182e064bd);

[ 694](structwifi__twt__params.md#a5fd269328f68838b8a7e3a0b93eed894) enum [wifi\_twt\_negotiation\_type](group__wifi__mgmt.md#ga695123cd534e2499f516a07fdc5cafa8) [negotiation\_type](structwifi__twt__params.md#a5fd269328f68838b8a7e3a0b93eed894);

[ 696](structwifi__twt__params.md#a347f8cff73ee6b6ba6d15ddf6f376a2d) enum [wifi\_twt\_setup\_cmd](group__wifi__mgmt.md#ga31c78afc89bfdc4b54cee177843f8022) [setup\_cmd](structwifi__twt__params.md#a347f8cff73ee6b6ba6d15ddf6f376a2d);

[ 698](structwifi__twt__params.md#a805a23284ed4afa46b84efcd43329beb) enum [wifi\_twt\_setup\_resp\_status](group__wifi__mgmt.md#ga4d03aedac13ee4512d7717ac624f319a) [resp\_status](structwifi__twt__params.md#a805a23284ed4afa46b84efcd43329beb);

[ 700](structwifi__twt__params.md#a9faff59e577775b3fe53f2139462ac71) enum [wifi\_twt\_teardown\_status](group__wifi__mgmt.md#gad3709d07aaa3ed59b48f9dd7bd181989) [teardown\_status](structwifi__twt__params.md#a9faff59e577775b3fe53f2139462ac71);

[ 702](structwifi__twt__params.md#adda47e302a87a766f18e28016963a561) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [dialog\_token](structwifi__twt__params.md#adda47e302a87a766f18e28016963a561);

[ 704](structwifi__twt__params.md#a95ec4b32d37309efa47256ae1ea865da) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [flow\_id](structwifi__twt__params.md#a95ec4b32d37309efa47256ae1ea865da);

705 union {

707 struct {

[ 709](structwifi__twt__params.md#ab92fe571559fcd5d97cdf7e6b7d86681) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [twt\_interval](structwifi__twt__params.md#ab92fe571559fcd5d97cdf7e6b7d86681);

[ 711](structwifi__twt__params.md#ae547c6fc1c7cbad15bebcfdaa43f59e7) bool [responder](structwifi__twt__params.md#ae547c6fc1c7cbad15bebcfdaa43f59e7);

[ 713](structwifi__twt__params.md#a4e822c04b52fe6a9489e48e26b8f9382) bool [trigger](structwifi__twt__params.md#a4e822c04b52fe6a9489e48e26b8f9382);

[ 715](structwifi__twt__params.md#a8ea1e2501c8b69dc3fa606eb360f8678) bool [implicit](structwifi__twt__params.md#a8ea1e2501c8b69dc3fa606eb360f8678);

[ 717](structwifi__twt__params.md#a02f2d822d530e5376f256503439a54f9) bool [announce](structwifi__twt__params.md#a02f2d822d530e5376f256503439a54f9);

[ 719](structwifi__twt__params.md#a7c297459a17ed2fd232c62cca63e952f) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [twt\_wake\_interval](structwifi__twt__params.md#a7c297459a17ed2fd232c62cca63e952f);

[ 725](structwifi__twt__params.md#a6f907ca412251fdd7391f29bfa6d7713) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [twt\_wake\_ahead\_duration](structwifi__twt__params.md#a6f907ca412251fdd7391f29bfa6d7713);

[ 726](structwifi__twt__params.md#aee57c0189b210cfcc18e213e35b9479c) } [setup](structwifi__twt__params.md#aee57c0189b210cfcc18e213e35b9479c);

728 struct {

[ 730](structwifi__twt__params.md#a26d6bda00452f77832f69f4465c13efb) bool [teardown\_all](structwifi__twt__params.md#a26d6bda00452f77832f69f4465c13efb);

[ 731](structwifi__twt__params.md#afdeebd8a27107a0e37282aa19e5149d0) } [teardown](structwifi__twt__params.md#afdeebd8a27107a0e37282aa19e5149d0);

732 };

[ 734](structwifi__twt__params.md#a70f58b502bb67ef3b2068ded2160b612) enum [wifi\_twt\_fail\_reason](group__wifi__mgmt.md#ga97fa304f9a1db2294a93cccd4c93bcf6) [fail\_reason](structwifi__twt__params.md#a70f58b502bb67ef3b2068ded2160b612);

735};

736

738

739/\* Flow ID is only 3 bits \*/

740#define WIFI\_MAX\_TWT\_FLOWS 8

741#define WIFI\_MAX\_TWT\_INTERVAL\_US (LONG\_MAX - 1)

742/\* 256 (u8) \* 1TU \*/

743#define WIFI\_MAX\_TWT\_WAKE\_INTERVAL\_US 262144

744#define WIFI\_MAX\_TWT\_WAKE\_AHEAD\_DURATION\_US (LONG\_MAX - 1)

745

747

[ 749](structwifi__twt__flow__info.md)struct [wifi\_twt\_flow\_info](structwifi__twt__flow__info.md) {

[ 751](structwifi__twt__flow__info.md#ae15ba49fa54f82cc6a1fb0d4572114b7) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [twt\_interval](structwifi__twt__flow__info.md#ae15ba49fa54f82cc6a1fb0d4572114b7);

[ 753](structwifi__twt__flow__info.md#a123ce10bed8b62b01919a7ea7644a0ba) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [dialog\_token](structwifi__twt__flow__info.md#a123ce10bed8b62b01919a7ea7644a0ba);

[ 755](structwifi__twt__flow__info.md#acb0c618f1cebcb172f342cfe222683be) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [flow\_id](structwifi__twt__flow__info.md#acb0c618f1cebcb172f342cfe222683be);

[ 757](structwifi__twt__flow__info.md#a620ae8ba546e4091d74280cb1553b2cf) enum [wifi\_twt\_negotiation\_type](group__wifi__mgmt.md#ga695123cd534e2499f516a07fdc5cafa8) [negotiation\_type](structwifi__twt__flow__info.md#a620ae8ba546e4091d74280cb1553b2cf);

[ 759](structwifi__twt__flow__info.md#ac82e4de8ffc82f851061f8ba8d217dc1) bool [responder](structwifi__twt__flow__info.md#ac82e4de8ffc82f851061f8ba8d217dc1);

[ 761](structwifi__twt__flow__info.md#a952a67bd092c5dadba387bb13449c6f3) bool [trigger](structwifi__twt__flow__info.md#a952a67bd092c5dadba387bb13449c6f3);

[ 763](structwifi__twt__flow__info.md#afb480be82d1c6f351bd634fd83bfa5c7) bool [implicit](structwifi__twt__flow__info.md#afb480be82d1c6f351bd634fd83bfa5c7);

[ 765](structwifi__twt__flow__info.md#afc81a5111c265fd9bb2aca5f9510bfa8) bool [announce](structwifi__twt__flow__info.md#afc81a5111c265fd9bb2aca5f9510bfa8);

[ 767](structwifi__twt__flow__info.md#aede6cb0cfc999fac8ded49e2981a3762) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [twt\_wake\_interval](structwifi__twt__flow__info.md#aede6cb0cfc999fac8ded49e2981a3762);

[ 769](structwifi__twt__flow__info.md#a6384d3829d54a58a53eafcb74c64a658) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [twt\_wake\_ahead\_duration](structwifi__twt__flow__info.md#a6384d3829d54a58a53eafcb74c64a658);

770};

771

[ 773](structwifi__enterprise__creds__params.md)struct [wifi\_enterprise\_creds\_params](structwifi__enterprise__creds__params.md) {

[ 775](structwifi__enterprise__creds__params.md#ae37381504a457b2f1d56dd5270c6711d) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[ca\_cert](structwifi__enterprise__creds__params.md#ae37381504a457b2f1d56dd5270c6711d);

[ 777](structwifi__enterprise__creds__params.md#a5f7060fcd2ca3db0b202faf15062564b) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [ca\_cert\_len](structwifi__enterprise__creds__params.md#a5f7060fcd2ca3db0b202faf15062564b);

[ 779](structwifi__enterprise__creds__params.md#a81d61179feba627be5c6456130b9f2af) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[client\_cert](structwifi__enterprise__creds__params.md#a81d61179feba627be5c6456130b9f2af);

[ 781](structwifi__enterprise__creds__params.md#a5f122d59b25b00af2db7eeac93d5482e) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [client\_cert\_len](structwifi__enterprise__creds__params.md#a5f122d59b25b00af2db7eeac93d5482e);

[ 783](structwifi__enterprise__creds__params.md#a8d88f5a8a6ccc8a9a883078af49ae96b) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[client\_key](structwifi__enterprise__creds__params.md#a8d88f5a8a6ccc8a9a883078af49ae96b);

[ 785](structwifi__enterprise__creds__params.md#a09f5b34c81fe871e7513358499518d95) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [client\_key\_len](structwifi__enterprise__creds__params.md#a09f5b34c81fe871e7513358499518d95);

[ 787](structwifi__enterprise__creds__params.md#ad9b867873709d7f2363fef49d7b6f2ca) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[ca\_cert2](structwifi__enterprise__creds__params.md#ad9b867873709d7f2363fef49d7b6f2ca);

[ 789](structwifi__enterprise__creds__params.md#abf35045e71afb0cb9ea25c635c5ac141) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [ca\_cert2\_len](structwifi__enterprise__creds__params.md#abf35045e71afb0cb9ea25c635c5ac141);

[ 791](structwifi__enterprise__creds__params.md#a133126e338d89563733268a03e2fa613) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[client\_cert2](structwifi__enterprise__creds__params.md#a133126e338d89563733268a03e2fa613);

[ 793](structwifi__enterprise__creds__params.md#adbe26c9b88f44eb6b875888f6a03e1bb) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [client\_cert2\_len](structwifi__enterprise__creds__params.md#adbe26c9b88f44eb6b875888f6a03e1bb);

[ 795](structwifi__enterprise__creds__params.md#abcda4d7820681d517d70d8f130b47050) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[client\_key2](structwifi__enterprise__creds__params.md#abcda4d7820681d517d70d8f130b47050);

[ 797](structwifi__enterprise__creds__params.md#a3da90b8a8dfa848f617579760ad4f971) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [client\_key2\_len](structwifi__enterprise__creds__params.md#a3da90b8a8dfa848f617579760ad4f971);

798};

799

[ 801](structwifi__ps__config.md)struct [wifi\_ps\_config](structwifi__ps__config.md) {

[ 803](structwifi__ps__config.md#a9e83c10eaaa1d721cbc49b40aedb00df) char [num\_twt\_flows](structwifi__ps__config.md#a9e83c10eaaa1d721cbc49b40aedb00df);

[ 805](structwifi__ps__config.md#ab7460f0f253b2d552e49e98e2c770967) struct [wifi\_twt\_flow\_info](structwifi__twt__flow__info.md) [twt\_flows](structwifi__ps__config.md#ab7460f0f253b2d552e49e98e2c770967)[WIFI\_MAX\_TWT\_FLOWS];

[ 807](structwifi__ps__config.md#a357aafc2dedda37755b1cb1fc07fe5a6) struct [wifi\_ps\_params](structwifi__ps__params.md) [ps\_params](structwifi__ps__config.md#a357aafc2dedda37755b1cb1fc07fe5a6);

808};

809

[ 811](group__wifi__mgmt.md#gae129d0783276e662575af2314eef86cd)enum [wifi\_mgmt\_op](group__wifi__mgmt.md#gae129d0783276e662575af2314eef86cd) {

[ 813](group__wifi__mgmt.md#ggae129d0783276e662575af2314eef86cda6b8183a773e0cdfa85bc4b41ae70fdcd) [WIFI\_MGMT\_GET](group__wifi__mgmt.md#ggae129d0783276e662575af2314eef86cda6b8183a773e0cdfa85bc4b41ae70fdcd) = 0,

[ 815](group__wifi__mgmt.md#ggae129d0783276e662575af2314eef86cdaa0d5931c8275a8d3288ab668b6dfb5a1) [WIFI\_MGMT\_SET](group__wifi__mgmt.md#ggae129d0783276e662575af2314eef86cdaa0d5931c8275a8d3288ab668b6dfb5a1) = 1,

816};

817

[ 819](structwifi__11k__params.md)struct [wifi\_11k\_params](structwifi__11k__params.md) {

[ 821](structwifi__11k__params.md#ae6029ed4bada41f18df0329d0da7401e) enum [wifi\_mgmt\_op](group__wifi__mgmt.md#gae129d0783276e662575af2314eef86cd) [oper](structwifi__11k__params.md#ae6029ed4bada41f18df0329d0da7401e);

[ 823](structwifi__11k__params.md#a739c3e94b025aae2fcf5680aecf3d646) bool [enable\_11k](structwifi__11k__params.md#a739c3e94b025aae2fcf5680aecf3d646);

[ 825](structwifi__11k__params.md#a64ace23c71837417678ceb9cc8d5f216) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [ssid](structwifi__11k__params.md#a64ace23c71837417678ceb9cc8d5f216)[[WIFI\_SSID\_MAX\_LEN](group__wifi__mgmt.md#gad62c60666c9fdffe2e0e9c4388f87886) + 1];

826};

827

[ 829](group__wifi__mgmt.md#ga3a6bfa37bd7850342279d304df20977d)#define MAX\_REG\_CHAN\_NUM 42

830

[ 832](structwifi__reg__chan__info.md)struct [wifi\_reg\_chan\_info](structwifi__reg__chan__info.md) {

[ 834](structwifi__reg__chan__info.md#a0addffc11ef29f50c01b700835e59930) unsigned short [center\_frequency](structwifi__reg__chan__info.md#a0addffc11ef29f50c01b700835e59930);

[ 836](structwifi__reg__chan__info.md#af9169ab4a41fac4c6f6766fc96799545) unsigned short [max\_power](structwifi__reg__chan__info.md#af9169ab4a41fac4c6f6766fc96799545):8;

[ 838](structwifi__reg__chan__info.md#aa044611e18b7332b8577e29f6a769e3f) unsigned short [supported](structwifi__reg__chan__info.md#aa044611e18b7332b8577e29f6a769e3f):1;

[ 840](structwifi__reg__chan__info.md#acc7a88b004c9a61c8bf9ee1a97f85928) unsigned short [passive\_only](structwifi__reg__chan__info.md#acc7a88b004c9a61c8bf9ee1a97f85928):1;

[ 842](structwifi__reg__chan__info.md#a1ab137c142902d2de7d6be2626d7ac1f) unsigned short [dfs](structwifi__reg__chan__info.md#a1ab137c142902d2de7d6be2626d7ac1f):1;

843} \_\_packed;

844

[ 846](structwifi__reg__domain.md)struct [wifi\_reg\_domain](structwifi__reg__domain.md) {

[ 848](structwifi__reg__domain.md#a3bbfdf1497a87bbb6b6211c7035e1002) enum [wifi\_mgmt\_op](group__wifi__mgmt.md#gae129d0783276e662575af2314eef86cd) [oper](structwifi__reg__domain.md#a3bbfdf1497a87bbb6b6211c7035e1002);

[ 850](structwifi__reg__domain.md#a567c6fcae8032567aea83c18cd211c33) bool [force](structwifi__reg__domain.md#a567c6fcae8032567aea83c18cd211c33);

[ 852](structwifi__reg__domain.md#abf191495814c227fbbfaccb2f727762e) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [country\_code](structwifi__reg__domain.md#abf191495814c227fbbfaccb2f727762e)[[WIFI\_COUNTRY\_CODE\_LEN](group__wifi__mgmt.md#ga6766ef7bcb001f1fb526a4083b6cd8bc)];

[ 854](structwifi__reg__domain.md#a3278e9f43893f49ab9f9d0d7f24009c1) unsigned int [num\_channels](structwifi__reg__domain.md#a3278e9f43893f49ab9f9d0d7f24009c1);

[ 856](structwifi__reg__domain.md#a4c8c9c11e41123cd7738fdb0d33ae5fb) struct [wifi\_reg\_chan\_info](structwifi__reg__chan__info.md) \*[chan\_info](structwifi__reg__domain.md#a4c8c9c11e41123cd7738fdb0d33ae5fb);

857};

858

[ 860](group__wifi__mgmt.md#ga38c184ea35c02f304cccdf389ca6d552)enum [wifi\_twt\_sleep\_state](group__wifi__mgmt.md#ga38c184ea35c02f304cccdf389ca6d552) {

[ 862](group__wifi__mgmt.md#gga38c184ea35c02f304cccdf389ca6d552a37a7aba20723b6614e39e1c417f3113c) [WIFI\_TWT\_STATE\_SLEEP](group__wifi__mgmt.md#gga38c184ea35c02f304cccdf389ca6d552a37a7aba20723b6614e39e1c417f3113c) = 0,

[ 864](group__wifi__mgmt.md#gga38c184ea35c02f304cccdf389ca6d552a7b7b45f85d9644f897ca00bd7864e1b0) [WIFI\_TWT\_STATE\_AWAKE](group__wifi__mgmt.md#gga38c184ea35c02f304cccdf389ca6d552a7b7b45f85d9644f897ca00bd7864e1b0) = 1,

865};

866

867#if defined(CONFIG\_WIFI\_MGMT\_RAW\_SCAN\_RESULTS) || defined(\_\_DOXYGEN\_\_)

[ 869](structwifi__raw__scan__result.md)struct [wifi\_raw\_scan\_result](structwifi__raw__scan__result.md) {

[ 871](structwifi__raw__scan__result.md#a3f08580c6448a5fa28dd8a594fa7dad6) [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) [rssi](structwifi__raw__scan__result.md#a3f08580c6448a5fa28dd8a594fa7dad6);

[ 873](structwifi__raw__scan__result.md#a876966f469714eb481b42ccc8a63945c) int [frame\_length](structwifi__raw__scan__result.md#a876966f469714eb481b42ccc8a63945c);

[ 875](structwifi__raw__scan__result.md#aa2c7781882c6775616cbc8016b0842f6) unsigned short [frequency](structwifi__raw__scan__result.md#aa2c7781882c6775616cbc8016b0842f6);

[ 877](structwifi__raw__scan__result.md#a5710e89199c147ce898602795f00aba3) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [data](structwifi__raw__scan__result.md#a5710e89199c147ce898602795f00aba3)[CONFIG\_WIFI\_MGMT\_RAW\_SCAN\_RESULT\_LENGTH];

878};

879#endif /\* CONFIG\_WIFI\_MGMT\_RAW\_SCAN\_RESULTS \*/

880

[ 882](structwifi__ap__sta__info.md)struct [wifi\_ap\_sta\_info](structwifi__ap__sta__info.md) {

[ 884](structwifi__ap__sta__info.md#a7d8bd52340d4937a4b5b7d2c00662441) enum [wifi\_link\_mode](group__wifi__mgmt.md#gabdb2a784d4727b71ab44cca04e422c62) [link\_mode](structwifi__ap__sta__info.md#a7d8bd52340d4937a4b5b7d2c00662441);

[ 886](structwifi__ap__sta__info.md#a7db904376ec73b774aa9d8236c15b3f6) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [mac](structwifi__ap__sta__info.md#a7db904376ec73b774aa9d8236c15b3f6)[[WIFI\_MAC\_ADDR\_LEN](group__wifi__mgmt.md#ga29409ff83a53c6464decdde9bdd04de6)];

[ 888](structwifi__ap__sta__info.md#a7f7c8b144bb3464af5213708591eefda) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [mac\_length](structwifi__ap__sta__info.md#a7f7c8b144bb3464af5213708591eefda);

[ 890](structwifi__ap__sta__info.md#a838c9a4288c9bc7e97afe2334c678f34) bool [twt\_capable](structwifi__ap__sta__info.md#a838c9a4288c9bc7e97afe2334c678f34);

891};

892

894

895/\* for use in max info size calculations \*/

896union wifi\_mgmt\_events {

897 struct [wifi\_scan\_result](structwifi__scan__result.md) scan\_result;

898 struct [wifi\_status](structwifi__status.md) connect\_status;

899 struct [wifi\_iface\_status](structwifi__iface__status.md) iface\_status;

900#ifdef CONFIG\_WIFI\_MGMT\_RAW\_SCAN\_RESULTS

901 struct [wifi\_raw\_scan\_result](structwifi__raw__scan__result.md) raw\_scan\_result;

902#endif /\* CONFIG\_WIFI\_MGMT\_RAW\_SCAN\_RESULTS \*/

903 struct [wifi\_twt\_params](structwifi__twt__params.md) twt\_params;

904 struct [wifi\_ap\_sta\_info](structwifi__ap__sta__info.md) ap\_sta\_info;

905};

906

908

[ 910](structwifi__mode__info.md)struct [wifi\_mode\_info](structwifi__mode__info.md) {

[ 912](structwifi__mode__info.md#aa29d3b88fc718aa3ac05daf38974707d) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [mode](structwifi__mode__info.md#aa29d3b88fc718aa3ac05daf38974707d);

[ 914](structwifi__mode__info.md#add58dd3b45fd2ddaf684d1b0de81bef9) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [if\_index](structwifi__mode__info.md#add58dd3b45fd2ddaf684d1b0de81bef9);

[ 916](structwifi__mode__info.md#a57c101db8b81ab0ac5dd0a158057a64a) enum [wifi\_mgmt\_op](group__wifi__mgmt.md#gae129d0783276e662575af2314eef86cd) [oper](structwifi__mode__info.md#a57c101db8b81ab0ac5dd0a158057a64a);

917};

918

[ 920](structwifi__filter__info.md)struct [wifi\_filter\_info](structwifi__filter__info.md) {

[ 922](structwifi__filter__info.md#ad9560be814299055cfa11b995a7dcf42) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [filter](structwifi__filter__info.md#ad9560be814299055cfa11b995a7dcf42);

[ 924](structwifi__filter__info.md#af9ea91e31e78afcb7ffe1ff9a04277a3) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [if\_index](structwifi__filter__info.md#af9ea91e31e78afcb7ffe1ff9a04277a3);

[ 926](structwifi__filter__info.md#a1b2d0448fc7f62654e3f5aacfba62f8f) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [buffer\_size](structwifi__filter__info.md#a1b2d0448fc7f62654e3f5aacfba62f8f);

[ 928](structwifi__filter__info.md#aedd5e220cdde5768cb0f4aff920971cd) enum [wifi\_mgmt\_op](group__wifi__mgmt.md#gae129d0783276e662575af2314eef86cd) [oper](structwifi__filter__info.md#aedd5e220cdde5768cb0f4aff920971cd);

929};

930

[ 932](structwifi__channel__info.md)struct [wifi\_channel\_info](structwifi__channel__info.md) {

[ 934](structwifi__channel__info.md#a799cbc0a67764f6680322ba0f2ad3300) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [channel](structwifi__channel__info.md#a799cbc0a67764f6680322ba0f2ad3300);

[ 936](structwifi__channel__info.md#a43a7dd8c19d0c6540e3cc0b5d1d6165d) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [if\_index](structwifi__channel__info.md#a43a7dd8c19d0c6540e3cc0b5d1d6165d);

[ 938](structwifi__channel__info.md#aa8ef8a71b49ead3664fff9a4d61b1ce8) enum [wifi\_mgmt\_op](group__wifi__mgmt.md#gae129d0783276e662575af2314eef86cd) [oper](structwifi__channel__info.md#aa8ef8a71b49ead3664fff9a4d61b1ce8);

939};

940

942#define WIFI\_AP\_STA\_MAX\_INACTIVITY (LONG\_MAX - 1)

944

[ 946](structwifi__ap__config__params.md)struct [wifi\_ap\_config\_params](structwifi__ap__config__params.md) {

[ 948](structwifi__ap__config__params.md#a4c391cf504a994ed0bc4971afdf76774) enum [wifi\_ap\_config\_param](group__wifi__mgmt.md#ga83546cf946a9123c563609e8903d9642) [type](structwifi__ap__config__params.md#a4c391cf504a994ed0bc4971afdf76774);

[ 950](structwifi__ap__config__params.md#a289866d9209450e893281b4c198a546a) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [max\_inactivity](structwifi__ap__config__params.md#a289866d9209450e893281b4c198a546a);

[ 952](structwifi__ap__config__params.md#a7fc0fad99f53ed8e1ac40b74ec98bf9a) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [max\_num\_sta](structwifi__ap__config__params.md#a7fc0fad99f53ed8e1ac40b74ec98bf9a);

953};

954

955#ifdef CONFIG\_WIFI\_NM\_WPA\_SUPPLICANT\_DPP

958#define WIFI\_DPP\_QRCODE\_MAX\_LEN 255

959

961enum wifi\_dpp\_op {

963 WIFI\_DPP\_OP\_INVALID = 0,

965 WIFI\_DPP\_CONFIGURATOR\_ADD,

967 WIFI\_DPP\_AUTH\_INIT,

969 WIFI\_DPP\_QR\_CODE,

971 WIFI\_DPP\_CHIRP,

973 WIFI\_DPP\_LISTEN,

975 WIFI\_DPP\_BOOTSTRAP\_GEN,

977 WIFI\_DPP\_BOOTSTRAP\_GET\_URI,

979 WIFI\_DPP\_SET\_CONF\_PARAM,

981 WIFI\_DPP\_SET\_WAIT\_RESP\_TIME,

983 WIFI\_DPP\_RECONFIG

984};

985

987enum wifi\_dpp\_curves {

989 WIFI\_DPP\_CURVES\_DEFAULT = 0,

991 WIFI\_DPP\_CURVES\_P\_256,

993 WIFI\_DPP\_CURVES\_P\_384,

995 WIFI\_DPP\_CURVES\_P\_512,

997 WIFI\_DPP\_CURVES\_BP\_256,

999 WIFI\_DPP\_CURVES\_BP\_384,

1001 WIFI\_DPP\_CURVES\_BP\_512

1002};

1003

1005enum wifi\_dpp\_role {

1007 WIFI\_DPP\_ROLE\_UNSET = 0,

1009 WIFI\_DPP\_ROLE\_CONFIGURATOR,

1011 WIFI\_DPP\_ROLE\_ENROLLEE,

1013 WIFI\_DPP\_ROLE\_EITHER

1014};

1015

1020enum wifi\_dpp\_conf {

1022 WIFI\_DPP\_CONF\_UNSET = 0,

1024 WIFI\_DPP\_CONF\_STA,

1026 WIFI\_DPP\_CONF\_AP,

1028 WIFI\_DPP\_CONF\_QUERY

1029};

1030

1035enum wifi\_dpp\_bootstrap\_type {

1037 WIFI\_DPP\_BOOTSTRAP\_TYPE\_UNSET = 0,

1039 WIFI\_DPP\_BOOTSTRAP\_TYPE\_QRCODE,

1041 WIFI\_DPP\_BOOTSTRAP\_TYPE\_PKEX,

1043 WIFI\_DPP\_BOOTSTRAP\_TYPE\_NFC\_URI

1044};

1045

1047struct wifi\_dpp\_configurator\_add\_params {

1049 int curve;

1051 int net\_access\_key\_curve;

1052};

1053

1055struct wifi\_dpp\_auth\_init\_params {

1057 int peer;

1059 int configurator;

1061 int role;

1063 int conf;

1065 char ssid[[WIFI\_SSID\_MAX\_LEN](group__wifi__mgmt.md#gad62c60666c9fdffe2e0e9c4388f87886) + 1];

1066};

1067

1069struct wifi\_dpp\_chirp\_params {

1071 int id;

1073 int freq;

1074};

1075

1077struct wifi\_dpp\_listen\_params {

1079 int freq;

1081 int role;

1082};

1083

1085struct wifi\_dpp\_bootstrap\_gen\_params {

1087 int type;

1089 int op\_class;

1091 int chan;

1093 int curve;

1095 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) mac[[WIFI\_MAC\_ADDR\_LEN](group__wifi__mgmt.md#ga29409ff83a53c6464decdde9bdd04de6)];

1096};

1097

1099struct wifi\_dpp\_configurator\_set\_params {

1101 int peer;

1103 int configurator;

1105 int role;

1107 int conf;

1109 int curve;

1111 int net\_access\_key\_curve;

1113 char ssid[[WIFI\_SSID\_MAX\_LEN](group__wifi__mgmt.md#gad62c60666c9fdffe2e0e9c4388f87886) + 1];

1114};

1115

1118struct wifi\_dpp\_params {

1120 int action;

1121 union {

1123 struct wifi\_dpp\_configurator\_add\_params configurator\_add;

1125 struct wifi\_dpp\_auth\_init\_params auth\_init;

1127 struct wifi\_dpp\_chirp\_params chirp;

1129 struct wifi\_dpp\_listen\_params [listen](group__bsd__sockets.md#ga36f501240a9428fe2ae63a9540c97adb);

1131 struct wifi\_dpp\_bootstrap\_gen\_params bootstrap\_gen;

1133 struct wifi\_dpp\_configurator\_set\_params configurator\_set;

1135 int id;

1137 int dpp\_resp\_wait\_time;

1139 int network\_id;

1141 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) dpp\_qr\_code[WIFI\_DPP\_QRCODE\_MAX\_LEN + 1];

1146 char resp[WIFI\_DPP\_QRCODE\_MAX\_LEN + 1];

1147 };

1148};

1149#endif /\* CONFIG\_WIFI\_NM\_WPA\_SUPPLICANT\_DPP \*/

1150

[ 1151](group__wifi__mgmt.md#ga234d72d7c881e67ff49fb6c474c622e3)#define WIFI\_WPS\_PIN\_MAX\_LEN 8

1152

[ 1154](group__wifi__mgmt.md#ga4c36ae1a5171d3fbaeebf95c16be496d)enum [wifi\_wps\_op](group__wifi__mgmt.md#ga4c36ae1a5171d3fbaeebf95c16be496d) {

[ 1156](group__wifi__mgmt.md#gga4c36ae1a5171d3fbaeebf95c16be496da093f5b3ef95d9e571ea169430da57e88) [WIFI\_WPS\_PBC](group__wifi__mgmt.md#gga4c36ae1a5171d3fbaeebf95c16be496da093f5b3ef95d9e571ea169430da57e88) = 0,

[ 1158](group__wifi__mgmt.md#gga4c36ae1a5171d3fbaeebf95c16be496da75bd5067903c2bba8a06732f0431393d) [WIFI\_WPS\_PIN\_GET](group__wifi__mgmt.md#gga4c36ae1a5171d3fbaeebf95c16be496da75bd5067903c2bba8a06732f0431393d) = 1,

[ 1160](group__wifi__mgmt.md#gga4c36ae1a5171d3fbaeebf95c16be496da58120620fd2fca80bdac7990ed0e7552) [WIFI\_WPS\_PIN\_SET](group__wifi__mgmt.md#gga4c36ae1a5171d3fbaeebf95c16be496da58120620fd2fca80bdac7990ed0e7552) = 2,

1161};

1162

[ 1164](structwifi__wps__config__params.md)struct [wifi\_wps\_config\_params](structwifi__wps__config__params.md) {

[ 1166](structwifi__wps__config__params.md#aa7a10889c5cd5124983b0f7242d23b7e) enum [wifi\_wps\_op](group__wifi__mgmt.md#ga4c36ae1a5171d3fbaeebf95c16be496d) [oper](structwifi__wps__config__params.md#aa7a10889c5cd5124983b0f7242d23b7e);

[ 1168](structwifi__wps__config__params.md#a962bd6513c564150e0c75112b96bbe15) char [pin](structwifi__wps__config__params.md#a962bd6513c564150e0c75112b96bbe15)[[WIFI\_WPS\_PIN\_MAX\_LEN](group__wifi__mgmt.md#ga234d72d7c881e67ff49fb6c474c622e3) + 1];

1169};

1170

[ 1173](group__wifi__mgmt.md#gafb2e8c10f596da3527abf9e227c3001b)enum [wifi\_hostapd\_iface\_state](group__wifi__mgmt.md#gafb2e8c10f596da3527abf9e227c3001b) {

[ 1174](group__wifi__mgmt.md#ggafb2e8c10f596da3527abf9e227c3001ba7b4af20b16fb8881b963d4f2ebdad11a) [WIFI\_HAPD\_IFACE\_UNINITIALIZED](group__wifi__mgmt.md#ggafb2e8c10f596da3527abf9e227c3001ba7b4af20b16fb8881b963d4f2ebdad11a),

[ 1175](group__wifi__mgmt.md#ggafb2e8c10f596da3527abf9e227c3001ba21e99c5fff612afd417c0d4511a9c135) [WIFI\_HAPD\_IFACE\_DISABLED](group__wifi__mgmt.md#ggafb2e8c10f596da3527abf9e227c3001ba21e99c5fff612afd417c0d4511a9c135),

[ 1176](group__wifi__mgmt.md#ggafb2e8c10f596da3527abf9e227c3001badd81c06c029edaa9ac973e03136d4ff4) [WIFI\_HAPD\_IFACE\_COUNTRY\_UPDATE](group__wifi__mgmt.md#ggafb2e8c10f596da3527abf9e227c3001badd81c06c029edaa9ac973e03136d4ff4),

[ 1177](group__wifi__mgmt.md#ggafb2e8c10f596da3527abf9e227c3001ba762c44f87b3dd9a08d2442b86ad06168) [WIFI\_HAPD\_IFACE\_ACS](group__wifi__mgmt.md#ggafb2e8c10f596da3527abf9e227c3001ba762c44f87b3dd9a08d2442b86ad06168),

[ 1178](group__wifi__mgmt.md#ggafb2e8c10f596da3527abf9e227c3001ba66a141b5b317ac3dc0ca383886458a00) [WIFI\_HAPD\_IFACE\_HT\_SCAN](group__wifi__mgmt.md#ggafb2e8c10f596da3527abf9e227c3001ba66a141b5b317ac3dc0ca383886458a00),

[ 1179](group__wifi__mgmt.md#ggafb2e8c10f596da3527abf9e227c3001ba2bcdccb48ba12b2561e08292365801a0) [WIFI\_HAPD\_IFACE\_DFS](group__wifi__mgmt.md#ggafb2e8c10f596da3527abf9e227c3001ba2bcdccb48ba12b2561e08292365801a0),

[ 1180](group__wifi__mgmt.md#ggafb2e8c10f596da3527abf9e227c3001ba82333796edc42607754281a400f07b2a) [WIFI\_HAPD\_IFACE\_ENABLED](group__wifi__mgmt.md#ggafb2e8c10f596da3527abf9e227c3001ba82333796edc42607754281a400f07b2a)

1181};

1182

1183#include <[zephyr/net/net\_if.h](net__if_8h.md)>

1184

[ 1191](group__wifi__mgmt.md#gad34b366f1c315207ce0da587ca96d8d8)typedef void (\*[scan\_result\_cb\_t](group__wifi__mgmt.md#gad34b366f1c315207ce0da587ca96d8d8))(struct [net\_if](structnet__if.md) \*iface, int status,

1192 struct [wifi\_scan\_result](structwifi__scan__result.md) \*entry);

1193

1194#ifdef CONFIG\_WIFI\_MGMT\_RAW\_SCAN\_RESULTS

1201typedef void (\*raw\_scan\_result\_cb\_t)(struct [net\_if](structnet__if.md) \*iface, int status,

1202 struct [wifi\_raw\_scan\_result](structwifi__raw__scan__result.md) \*entry);

1203#endif /\* CONFIG\_WIFI\_MGMT\_RAW\_SCAN\_RESULTS \*/

1204

[ 1206](structwifi__mgmt__ops.md)struct [wifi\_mgmt\_ops](structwifi__mgmt__ops.md) {

[ 1218](structwifi__mgmt__ops.md#a267030c27da3cdc251badd0ed7f7b1cb) int (\*[scan](structwifi__mgmt__ops.md#a267030c27da3cdc251badd0ed7f7b1cb))(const struct [device](structdevice.md) \*dev,

1219 struct [wifi\_scan\_params](structwifi__scan__params.md) \*params,

1220 [scan\_result\_cb\_t](group__wifi__mgmt.md#gad34b366f1c315207ce0da587ca96d8d8) cb);

[ 1228](structwifi__mgmt__ops.md#ae6255ea77739918797b4f3c7a4634a75) int (\*[connect](structwifi__mgmt__ops.md#ae6255ea77739918797b4f3c7a4634a75))(const struct [device](structdevice.md) \*dev,

1229 struct [wifi\_connect\_req\_params](structwifi__connect__req__params.md) \*params);

[ 1236](structwifi__mgmt__ops.md#a5725c6fd93ae189a3019374cd4ad2ff4) int (\*[disconnect](structwifi__mgmt__ops.md#a5725c6fd93ae189a3019374cd4ad2ff4))(const struct [device](structdevice.md) \*dev);

[ 1244](structwifi__mgmt__ops.md#ac2ce3a4a86c43e30d33261f71c44198a) int (\*[ap\_enable](structwifi__mgmt__ops.md#ac2ce3a4a86c43e30d33261f71c44198a))(const struct [device](structdevice.md) \*dev,

1245 struct [wifi\_connect\_req\_params](structwifi__connect__req__params.md) \*params);

[ 1252](structwifi__mgmt__ops.md#a5aa7a2be82eb1783872abda2b8978235) int (\*[ap\_disable](structwifi__mgmt__ops.md#a5aa7a2be82eb1783872abda2b8978235))(const struct [device](structdevice.md) \*dev);

[ 1260](structwifi__mgmt__ops.md#af01aaec29be78c02314acf13b5c1b6f7) int (\*[ap\_sta\_disconnect](structwifi__mgmt__ops.md#af01aaec29be78c02314acf13b5c1b6f7))(const struct [device](structdevice.md) \*dev, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*mac);

[ 1268](structwifi__mgmt__ops.md#adf157476d776bc9c068e99e1a0266fd3) int (\*[iface\_status](structwifi__mgmt__ops.md#adf157476d776bc9c068e99e1a0266fd3))(const struct [device](structdevice.md) \*dev, struct [wifi\_iface\_status](structwifi__iface__status.md) \*status);

1269#if defined(CONFIG\_NET\_STATISTICS\_WIFI) || defined(\_\_DOXYGEN\_\_)

[ 1277](structwifi__mgmt__ops.md#a5e6fdf836273fcde54efff4c77bfdf0e) int (\*[get\_stats](structwifi__mgmt__ops.md#a5e6fdf836273fcde54efff4c77bfdf0e))(const struct [device](structdevice.md) \*dev, struct [net\_stats\_wifi](structnet__stats__wifi.md) \*stats);

[ 1284](structwifi__mgmt__ops.md#ae66901b434ab02863c0d3bd539c4b650) int (\*[reset\_stats](structwifi__mgmt__ops.md#ae66901b434ab02863c0d3bd539c4b650))(const struct [device](structdevice.md) \*dev);

1285#endif /\* CONFIG\_NET\_STATISTICS\_WIFI \*/

[ 1293](structwifi__mgmt__ops.md#a2cf66093ad850319cf222468e22ff485) int (\*[cfg\_11k](structwifi__mgmt__ops.md#a2cf66093ad850319cf222468e22ff485))(const struct [device](structdevice.md) \*dev, struct [wifi\_11k\_params](structwifi__11k__params.md) \*params);

[ 1301](structwifi__mgmt__ops.md#a1cdd0b76a0a326e968d27c0a3cafcef8) int (\*[send\_11k\_neighbor\_request](structwifi__mgmt__ops.md#a1cdd0b76a0a326e968d27c0a3cafcef8))(const struct [device](structdevice.md) \*dev, struct [wifi\_11k\_params](structwifi__11k__params.md) \*params);

[ 1309](structwifi__mgmt__ops.md#ac0f3f7fa699b1bc7db2358e77dd44cc4) int (\*[set\_power\_save](structwifi__mgmt__ops.md#ac0f3f7fa699b1bc7db2358e77dd44cc4))(const struct [device](structdevice.md) \*dev, struct [wifi\_ps\_params](structwifi__ps__params.md) \*params);

[ 1317](structwifi__mgmt__ops.md#ab4500534b6abe0449290c8bd8f729fc4) int (\*[set\_twt](structwifi__mgmt__ops.md#ab4500534b6abe0449290c8bd8f729fc4))(const struct [device](structdevice.md) \*dev, struct [wifi\_twt\_params](structwifi__twt__params.md) \*params);

[ 1325](structwifi__mgmt__ops.md#a52690b13f8a1e7b0c2302eaa24ae4c7f) int (\*[get\_power\_save\_config](structwifi__mgmt__ops.md#a52690b13f8a1e7b0c2302eaa24ae4c7f))(const struct [device](structdevice.md) \*dev, struct [wifi\_ps\_config](structwifi__ps__config.md) \*config);

[ 1333](structwifi__mgmt__ops.md#a0a287c8acf2d7bf9333b755589294881) int (\*[reg\_domain](structwifi__mgmt__ops.md#a0a287c8acf2d7bf9333b755589294881))(const struct [device](structdevice.md) \*dev, struct [wifi\_reg\_domain](structwifi__reg__domain.md) \*[reg\_domain](structwifi__mgmt__ops.md#a0a287c8acf2d7bf9333b755589294881));

[ 1341](structwifi__mgmt__ops.md#ad645276745ce8dd9685e0744efdfc733) int (\*[filter](structwifi__mgmt__ops.md#ad645276745ce8dd9685e0744efdfc733))(const struct [device](structdevice.md) \*dev, struct [wifi\_filter\_info](structwifi__filter__info.md) \*[filter](structwifi__mgmt__ops.md#ad645276745ce8dd9685e0744efdfc733));

[ 1349](structwifi__mgmt__ops.md#ae2fb1bc35bf9255655a30a2ad8588b7c) int (\*[mode](structwifi__mgmt__ops.md#ae2fb1bc35bf9255655a30a2ad8588b7c))(const struct [device](structdevice.md) \*dev, struct [wifi\_mode\_info](structwifi__mode__info.md) \*[mode](structwifi__mgmt__ops.md#ae2fb1bc35bf9255655a30a2ad8588b7c));

[ 1357](structwifi__mgmt__ops.md#af17ddfea01d0ab478f6fd50b1c9d6015) int (\*[channel](structwifi__mgmt__ops.md#af17ddfea01d0ab478f6fd50b1c9d6015))(const struct [device](structdevice.md) \*dev, struct [wifi\_channel\_info](structwifi__channel__info.md) \*[channel](structwifi__mgmt__ops.md#af17ddfea01d0ab478f6fd50b1c9d6015));

1358#ifdef CONFIG\_WIFI\_NM\_WPA\_SUPPLICANT\_WNM

1366 int (\*btm\_query)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) reason);

1367#endif

[ 1380](structwifi__mgmt__ops.md#aa7e4bc3dbc960091d11ffe5454259885) int (\*[get\_version](structwifi__mgmt__ops.md#aa7e4bc3dbc960091d11ffe5454259885))(const struct [device](structdevice.md) \*dev, struct [wifi\_version](structwifi__version.md) \*params);

[ 1388](structwifi__mgmt__ops.md#a42c2aa55df30158d8b5d6f4c81e3e2dd) int (\*[get\_conn\_params](structwifi__mgmt__ops.md#a42c2aa55df30158d8b5d6f4c81e3e2dd))(const struct [device](structdevice.md) \*dev, struct [wifi\_connect\_req\_params](structwifi__connect__req__params.md) \*params);

[ 1396](structwifi__mgmt__ops.md#a514e06d63bcf6dc11dba1d3af8d102d5) int (\*[set\_rts\_threshold](structwifi__mgmt__ops.md#a514e06d63bcf6dc11dba1d3af8d102d5))(const struct [device](structdevice.md) \*dev, unsigned int rts\_threshold);

[ 1404](structwifi__mgmt__ops.md#a2475f32afcce72464b2db6ecad7fb3eb) int (\*[ap\_config\_params](structwifi__mgmt__ops.md#a2475f32afcce72464b2db6ecad7fb3eb))(const struct [device](structdevice.md) \*dev, struct [wifi\_ap\_config\_params](structwifi__ap__config__params.md) \*params);

1405

1406#ifdef CONFIG\_WIFI\_NM\_WPA\_SUPPLICANT\_DPP

1414 int (\*dpp\_dispatch)(const struct [device](structdevice.md) \*dev, struct wifi\_dpp\_params \*params);

1415#endif /\* CONFIG\_WIFI\_NM\_WPA\_SUPPLICANT\_DPP \*/

[ 1422](structwifi__mgmt__ops.md#aadf991d6f6725e5c179ca8343d626ad8) int (\*[pmksa\_flush](structwifi__mgmt__ops.md#aadf991d6f6725e5c179ca8343d626ad8))(const struct [device](structdevice.md) \*dev);

1430#ifdef CONFIG\_WIFI\_NM\_WPA\_SUPPLICANT\_CRYPTO\_ENTERPRISE

1431 int (\*enterprise\_creds)(const struct [device](structdevice.md) \*dev,

1432 struct [wifi\_enterprise\_creds\_params](structwifi__enterprise__creds__params.md) \*creds);

1433#endif

[ 1441](structwifi__mgmt__ops.md#a20706f9eed43b3380258b62fdf93be02) int (\*[get\_rts\_threshold](structwifi__mgmt__ops.md#a20706f9eed43b3380258b62fdf93be02))(const struct [device](structdevice.md) \*dev, unsigned int \*rts\_threshold);

[ 1449](structwifi__mgmt__ops.md#aaf85f7b56997fb40689b927535af5e85) int (\*[wps\_config](structwifi__mgmt__ops.md#aaf85f7b56997fb40689b927535af5e85))(const struct [device](structdevice.md) \*dev, struct [wifi\_wps\_config\_params](structwifi__wps__config__params.md) \*params);

[ 1457](structwifi__mgmt__ops.md#a538ffba0a7e045ca9c8ac62ccefc8a36) int (\*[candidate\_scan](structwifi__mgmt__ops.md#a538ffba0a7e045ca9c8ac62ccefc8a36))(const struct [device](structdevice.md) \*dev, struct [wifi\_scan\_params](structwifi__scan__params.md) \*params);

[ 1464](structwifi__mgmt__ops.md#a501b114298738ac6af9c4a80f5360d79) int (\*[start\_11r\_roaming](structwifi__mgmt__ops.md#a501b114298738ac6af9c4a80f5360d79))(const struct [device](structdevice.md) \*dev);

1465};

1466

[ 1468](structnet__wifi__mgmt__offload.md)struct [net\_wifi\_mgmt\_offload](structnet__wifi__mgmt__offload.md) {

1475#if defined(CONFIG\_WIFI\_USE\_NATIVE\_NETWORKING) || defined(\_\_DOXYGEN\_\_)

[ 1477](structnet__wifi__mgmt__offload.md#a1d34a954a2f16d29f51dc51dd6fbb845) struct [ethernet\_api](structethernet__api.md) [wifi\_iface](structnet__wifi__mgmt__offload.md#a1d34a954a2f16d29f51dc51dd6fbb845);

1478#else

1480 struct [offloaded\_if\_api](structoffloaded__if__api.md) [wifi\_iface](structnet__wifi__mgmt__offload.md#a1d34a954a2f16d29f51dc51dd6fbb845);

1481#endif

[ 1483](structnet__wifi__mgmt__offload.md#a98fcc053d9820d2d981ed659520c9b3b) const struct [wifi\_mgmt\_ops](structwifi__mgmt__ops.md) \*const [wifi\_mgmt\_api](structnet__wifi__mgmt__offload.md#a98fcc053d9820d2d981ed659520c9b3b);

1484

1485#if defined(CONFIG\_WIFI\_NM\_WPA\_SUPPLICANT) || defined(\_\_DOXYGEN\_\_)

[ 1487](structnet__wifi__mgmt__offload.md#a991e0bc6247578a3d1c9d2d3ab0b63d7) const void \*[wifi\_drv\_ops](structnet__wifi__mgmt__offload.md#a991e0bc6247578a3d1c9d2d3ab0b63d7);

1488#endif

1489};

1490

1491#if defined(CONFIG\_WIFI\_NM\_WPA\_SUPPLICANT)

1492/\* Make sure wifi\_drv\_ops is after wifi\_mgmt\_api \*/

1493BUILD\_ASSERT(offsetof(struct [net\_wifi\_mgmt\_offload](structnet__wifi__mgmt__offload.md), wifi\_mgmt\_api) <

1494 offsetof(struct [net\_wifi\_mgmt\_offload](structnet__wifi__mgmt__offload.md), wifi\_drv\_ops));

1495#endif

1496

1497/\* Make sure that the network interface API is properly setup inside

1498 \* Wifi mgmt offload API struct (it is the first one).

1499 \*/

1500BUILD\_ASSERT(offsetof(struct [net\_wifi\_mgmt\_offload](structnet__wifi__mgmt__offload.md), wifi\_iface) == 0);

1501

[ 1507](group__wifi__mgmt.md#ga036416696b1e3bc458ddbaf07a08d69d)void [wifi\_mgmt\_raise\_connect\_result\_event](group__wifi__mgmt.md#ga036416696b1e3bc458ddbaf07a08d69d)(struct [net\_if](structnet__if.md) \*iface, int status);

1508

[ 1514](group__wifi__mgmt.md#ga3b6edcf9b51afbf7a327d1a344bd7b87)void [wifi\_mgmt\_raise\_disconnect\_result\_event](group__wifi__mgmt.md#ga3b6edcf9b51afbf7a327d1a344bd7b87)(struct [net\_if](structnet__if.md) \*iface, int status);

1515

[ 1521](group__wifi__mgmt.md#ga7da6af0747bcba85f8afab30c92b5b43)void [wifi\_mgmt\_raise\_iface\_status\_event](group__wifi__mgmt.md#ga7da6af0747bcba85f8afab30c92b5b43)(struct [net\_if](structnet__if.md) \*iface,

1522 struct [wifi\_iface\_status](structwifi__iface__status.md) \*[iface\_status](structwifi__mgmt__ops.md#adf157476d776bc9c068e99e1a0266fd3));

1523

[ 1529](group__wifi__mgmt.md#ga39404d15243ca084b253cae8fc07e374)void [wifi\_mgmt\_raise\_twt\_event](group__wifi__mgmt.md#ga39404d15243ca084b253cae8fc07e374)(struct [net\_if](structnet__if.md) \*iface,

1530 struct [wifi\_twt\_params](structwifi__twt__params.md) \*twt\_params);

1531

[ 1537](group__wifi__mgmt.md#ga18f09a3196588b51d6c0644f82f639d7)void [wifi\_mgmt\_raise\_twt\_sleep\_state](group__wifi__mgmt.md#ga18f09a3196588b51d6c0644f82f639d7)(struct [net\_if](structnet__if.md) \*iface, int twt\_sleep\_state);

1538

1539#if defined(CONFIG\_WIFI\_MGMT\_RAW\_SCAN\_RESULTS) || defined(\_\_DOXYGEN\_\_)

[ 1545](group__wifi__mgmt.md#ga71c99913bded844c4ca32ed9155bc470)void [wifi\_mgmt\_raise\_raw\_scan\_result\_event](group__wifi__mgmt.md#ga71c99913bded844c4ca32ed9155bc470)(struct [net\_if](structnet__if.md) \*iface,

1546 struct [wifi\_raw\_scan\_result](structwifi__raw__scan__result.md) \*raw\_scan\_info);

1547#endif /\* CONFIG\_WIFI\_MGMT\_RAW\_SCAN\_RESULTS \*/

1548

[ 1554](group__wifi__mgmt.md#gaa75246d6dc55dada389c9d31e2607d5c)void [wifi\_mgmt\_raise\_disconnect\_complete\_event](group__wifi__mgmt.md#gaa75246d6dc55dada389c9d31e2607d5c)(struct [net\_if](structnet__if.md) \*iface, int status);

1555

1556#ifdef CONFIG\_WIFI\_NM\_WPA\_SUPPLICANT\_ROAMING

1563void wifi\_mgmt\_raise\_neighbor\_rep\_recv\_event(struct [net\_if](structnet__if.md) \*iface,

1564 char \*inbuf, size\_t buf\_len);

1565#endif

1566

[ 1572](group__wifi__mgmt.md#ga67b52edeff76c2211b038f4aa90b8982)void [wifi\_mgmt\_raise\_ap\_enable\_result\_event](group__wifi__mgmt.md#ga67b52edeff76c2211b038f4aa90b8982)(struct [net\_if](structnet__if.md) \*iface, enum [wifi\_ap\_status](group__wifi__mgmt.md#gaaf730bf76adc06434c7ac63bf0417884) status);

1573

[ 1579](group__wifi__mgmt.md#gadee15c6a492a8ee13bea43812debb5d9)void [wifi\_mgmt\_raise\_ap\_disable\_result\_event](group__wifi__mgmt.md#gadee15c6a492a8ee13bea43812debb5d9)(struct [net\_if](structnet__if.md) \*iface, enum [wifi\_ap\_status](group__wifi__mgmt.md#gaaf730bf76adc06434c7ac63bf0417884) status);

1580

[ 1586](group__wifi__mgmt.md#gac8f17f0aa3e426a5cdb731727b9b9ce3)void [wifi\_mgmt\_raise\_ap\_sta\_connected\_event](group__wifi__mgmt.md#gac8f17f0aa3e426a5cdb731727b9b9ce3)(struct [net\_if](structnet__if.md) \*iface,

1587 struct [wifi\_ap\_sta\_info](structwifi__ap__sta__info.md) \*sta\_info);

1588

[ 1593](group__wifi__mgmt.md#ga49fb9c3908be61d847b31c99be6afc42)void [wifi\_mgmt\_raise\_ap\_sta\_disconnected\_event](group__wifi__mgmt.md#ga49fb9c3908be61d847b31c99be6afc42)(struct [net\_if](structnet__if.md) \*iface,

1594 struct [wifi\_ap\_sta\_info](structwifi__ap__sta__info.md) \*sta\_info);

1595

1599#ifdef \_\_cplusplus

1600}

1601#endif

1602

1603#endif /\* ZEPHYR\_INCLUDE\_NET\_WIFI\_MGMT\_H\_ \*/

[ethernet.h](ethernet_8h.md)

Ethernet.

[listen](group__bsd__sockets.md#ga36f501240a9428fe2ae63a9540c97adb)

static int listen(int sock, int backlog)

POSIX wrapper for zsock\_listen.

**Definition** socket.h:855

[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)

#define NET\_MGMT\_DEFINE\_REQUEST\_HANDLER(\_mgmt\_request)

Declare a request handler function for the given network event.

**Definition** net\_mgmt.h:111

[wifi\_mgmt\_raise\_connect\_result\_event](group__wifi__mgmt.md#ga036416696b1e3bc458ddbaf07a08d69d)

void wifi\_mgmt\_raise\_connect\_result\_event(struct net\_if \*iface, int status)

Wi-Fi management connect result event.

[wifi\_ps](group__wifi__mgmt.md#ga0fffeb57b68fb8cdef9d3d571368b8ca)

wifi\_ps

Wi-Fi power save states.

**Definition** wifi.h:367

[NET\_REQUEST\_WIFI\_PS\_CONFIG](group__wifi__mgmt.md#ga1032f3773cfe6130da4d4d498b044ee2)

#define NET\_REQUEST\_WIFI\_PS\_CONFIG

Request a Wi-Fi power save configuration.

**Definition** wifi\_mgmt.h:190

[wifi\_mgmt\_raise\_twt\_sleep\_state](group__wifi__mgmt.md#ga18f09a3196588b51d6c0644f82f639d7)

void wifi\_mgmt\_raise\_twt\_sleep\_state(struct net\_if \*iface, int twt\_sleep\_state)

Wi-Fi management TWT sleep state event.

[NET\_REQUEST\_WIFI\_SCAN](group__wifi__mgmt.md#ga1c277da90986fa52dca182c4d922646f)

#define NET\_REQUEST\_WIFI\_SCAN

Request a Wi-Fi scan.

**Definition** wifi\_mgmt.h:132

[wifi\_frequency\_bands](group__wifi__mgmt.md#ga1e2f0439a322355fa7368ea880c9c15d)

wifi\_frequency\_bands

IEEE 802.11 operational frequency bands (not exhaustive).

**Definition** wifi.h:207

[wifi\_mfp\_options](group__wifi__mgmt.md#ga1f252da47d9650023d7fff6d08e49c76)

wifi\_mfp\_options

IEEE 802.11w - Management frame protection.

**Definition** wifi.h:186

[NET\_REQUEST\_WIFI\_RTS\_THRESHOLD](group__wifi__mgmt.md#ga22d80ef0ffb15e4286d7b1c3325d5334)

#define NET\_REQUEST\_WIFI\_RTS\_THRESHOLD

Request a Wi-Fi RTS threshold.

**Definition** wifi\_mgmt.h:238

[WIFI\_WPS\_PIN\_MAX\_LEN](group__wifi__mgmt.md#ga234d72d7c881e67ff49fb6c474c622e3)

#define WIFI\_WPS\_PIN\_MAX\_LEN

**Definition** wifi\_mgmt.h:1151

[NET\_REQUEST\_WIFI\_RTS\_THRESHOLD\_CONFIG](group__wifi__mgmt.md#ga2678ea372335af008d9bd3333f7a7de1)

#define NET\_REQUEST\_WIFI\_RTS\_THRESHOLD\_CONFIG

Request a Wi-Fi RTS threshold configuration.

**Definition** wifi\_mgmt.h:277

[WIFI\_MAC\_ADDR\_LEN](group__wifi__mgmt.md#ga29409ff83a53c6464decdde9bdd04de6)

#define WIFI\_MAC\_ADDR\_LEN

MAC address length.

**Definition** wifi.h:235

[NET\_REQUEST\_WIFI\_REG\_DOMAIN](group__wifi__mgmt.md#ga2b27d102b779a6d846b375854768fb7f)

#define NET\_REQUEST\_WIFI\_REG\_DOMAIN

Request a Wi-Fi regulatory domain.

**Definition** wifi\_mgmt.h:196

[wifi\_ps\_exit\_strategy](group__wifi__mgmt.md#ga2d424d1711389fb784e916a87ff854b7)

wifi\_ps\_exit\_strategy

Wi-Fi power save exit strategy.

**Definition** wifi.h:576

[NET\_REQUEST\_WIFI\_PACKET\_FILTER](group__wifi__mgmt.md#ga3098e817d12bf4619c9fd2698508fb4e)

#define NET\_REQUEST\_WIFI\_PACKET\_FILTER

Request Wi-Fi packet filter.

**Definition** wifi\_mgmt.h:208

[wifi\_twt\_setup\_cmd](group__wifi__mgmt.md#ga31c78afc89bfdc4b54cee177843f8022)

wifi\_twt\_setup\_cmd

Wi-Fi Target Wake Time (TWT) setup commands.

**Definition** wifi.h:449

[NET\_REQUEST\_WIFI\_NEIGHBOR\_REP\_COMPLETE](group__wifi__mgmt.md#ga373031970a29331bf1b30d1654c128f0)

#define NET\_REQUEST\_WIFI\_NEIGHBOR\_REP\_COMPLETE

**Definition** wifi\_mgmt.h:296

[wifi\_twt\_sleep\_state](group__wifi__mgmt.md#ga38c184ea35c02f304cccdf389ca6d552)

wifi\_twt\_sleep\_state

Wi-Fi TWT sleep states.

**Definition** wifi\_mgmt.h:860

[wifi\_mgmt\_raise\_twt\_event](group__wifi__mgmt.md#ga39404d15243ca084b253cae8fc07e374)

void wifi\_mgmt\_raise\_twt\_event(struct net\_if \*iface, struct wifi\_twt\_params \*twt\_params)

Wi-Fi management TWT event.

[wifi\_mgmt\_raise\_disconnect\_result\_event](group__wifi__mgmt.md#ga3b6edcf9b51afbf7a327d1a344bd7b87)

void wifi\_mgmt\_raise\_disconnect\_result\_event(struct net\_if \*iface, int status)

Wi-Fi management disconnect result event.

[NET\_REQUEST\_WIFI\_IFACE\_STATUS](group__wifi__mgmt.md#ga3e45f6ee3801553619d8eb7d0af506eb)

#define NET\_REQUEST\_WIFI\_IFACE\_STATUS

Request a Wi-Fi network interface status.

**Definition** wifi\_mgmt.h:162

[NET\_REQUEST\_WIFI\_VERSION](group__wifi__mgmt.md#ga3e60c29ca9ce95d17a7fff087290f7f1)

#define NET\_REQUEST\_WIFI\_VERSION

Request a Wi-Fi version.

**Definition** wifi\_mgmt.h:226

[wifi\_mgmt\_raise\_ap\_sta\_disconnected\_event](group__wifi__mgmt.md#ga49fb9c3908be61d847b31c99be6afc42)

void wifi\_mgmt\_raise\_ap\_sta\_disconnected\_event(struct net\_if \*iface, struct wifi\_ap\_sta\_info \*sta\_info)

Wi-Fi management AP mode STA disconnected event.

[NET\_REQUEST\_WIFI\_11K\_NEIGHBOR\_REQUEST](group__wifi__mgmt.md#ga4a2b1e8befd7376749b1d4fbcf98376f)

#define NET\_REQUEST\_WIFI\_11K\_NEIGHBOR\_REQUEST

**Definition** wifi\_mgmt.h:172

[wifi\_wps\_op](group__wifi__mgmt.md#ga4c36ae1a5171d3fbaeebf95c16be496d)

wifi\_wps\_op

Operation for WPS.

**Definition** wifi\_mgmt.h:1154

[wifi\_twt\_setup\_resp\_status](group__wifi__mgmt.md#ga4d03aedac13ee4512d7717ac624f319a)

wifi\_twt\_setup\_resp\_status

Wi-Fi Target Wake Time (TWT) negotiation status.

**Definition** wifi.h:472

[wifi\_iface\_mode](group__wifi__mgmt.md#ga584f6239ac14e2bedc5e6bd72756423b)

wifi\_iface\_mode

Wi-Fi interface modes.

**Definition** wifi.h:300

[NET\_REQUEST\_WIFI\_AP\_ENABLE](group__wifi__mgmt.md#ga638d2eb0a5029c1af46a91b523ed8589)

#define NET\_REQUEST\_WIFI\_AP\_ENABLE

Request a Wi-Fi access point enable.

**Definition** wifi\_mgmt.h:150

[NET\_REQUEST\_WIFI\_WPS\_CONFIG](group__wifi__mgmt.md#ga649a63bc7d315ebdd89464ff48b3fada)

#define NET\_REQUEST\_WIFI\_WPS\_CONFIG

**Definition** wifi\_mgmt.h:282

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

**Definition** wifi\_mgmt.h:178

[wifi\_twt\_negotiation\_type](group__wifi__mgmt.md#ga695123cd534e2499f516a07fdc5cafa8)

wifi\_twt\_negotiation\_type

Wi-Fi Target Wake Time (TWT) negotiation types.

**Definition** wifi.h:436

[wifi\_mgmt\_raise\_raw\_scan\_result\_event](group__wifi__mgmt.md#ga71c99913bded844c4ca32ed9155bc470)

void wifi\_mgmt\_raise\_raw\_scan\_result\_event(struct net\_if \*iface, struct wifi\_raw\_scan\_result \*raw\_scan\_info)

Wi-Fi management raw scan result event.

[wifi\_mgmt\_raise\_iface\_status\_event](group__wifi__mgmt.md#ga7da6af0747bcba85f8afab30c92b5b43)

void wifi\_mgmt\_raise\_iface\_status\_event(struct net\_if \*iface, struct wifi\_iface\_status \*iface\_status)

Wi-Fi management interface status event.

[wifi\_ap\_config\_param](group__wifi__mgmt.md#ga83546cf946a9123c563609e8903d9642)

wifi\_ap\_config\_param

Wi-Fi AP mode configuration parameter.

**Definition** wifi.h:653

[wifi\_conn\_status](group__wifi__mgmt.md#ga86a5741e54aeb3e290142b0de217b8a8)

wifi\_conn\_status

Wi-Fi connect result codes.

**Definition** wifi\_mgmt.h:552

[NET\_REQUEST\_WIFI\_START\_ROAMING](group__wifi__mgmt.md#ga89cc123bb5c30140d2ce0a8b741b1086)

#define NET\_REQUEST\_WIFI\_START\_ROAMING

**Definition** wifi\_mgmt.h:291

[NET\_REQUEST\_WIFI\_PMKSA\_FLUSH](group__wifi__mgmt.md#ga9070995249eb35de37e2b60c4426f840)

#define NET\_REQUEST\_WIFI\_PMKSA\_FLUSH

Request a Wi-Fi PMKSA cache entries flush.

**Definition** wifi\_mgmt.h:265

[NET\_REQUEST\_WIFI\_DISCONNECT](group__wifi__mgmt.md#ga90afd8d4e83056463ec6e667ed8ea60a)

#define NET\_REQUEST\_WIFI\_DISCONNECT

Request a Wi-Fi disconnect.

**Definition** wifi\_mgmt.h:144

[wifi\_twt\_fail\_reason](group__wifi__mgmt.md#ga97fa304f9a1db2294a93cccd4c93bcf6)

wifi\_twt\_fail\_reason

Target Wake Time (TWT) error codes.

**Definition** wifi.h:480

[net\_request\_wifi\_cmd](group__wifi__mgmt.md#ga99a55137188119f65f9d2bb4f57cac77)

net\_request\_wifi\_cmd

Wi-Fi management commands.

**Definition** wifi\_mgmt.h:61

[NET\_REQUEST\_WIFI\_MODE](group__wifi__mgmt.md#ga9b4da60a8108b0cc431ac1eecfca0cd0)

#define NET\_REQUEST\_WIFI\_MODE

Request current Wi-Fi mode.

**Definition** wifi\_mgmt.h:202

[NET\_REQUEST\_WIFI\_AP\_STA\_DISCONNECT](group__wifi__mgmt.md#gaa3e52e08d89a1104f07207e52b81d503)

#define NET\_REQUEST\_WIFI\_AP\_STA\_DISCONNECT

Request a Wi-Fi access point to disconnect a station.

**Definition** wifi\_mgmt.h:220

[wifi\_mgmt\_raise\_disconnect\_complete\_event](group__wifi__mgmt.md#gaa75246d6dc55dada389c9d31e2607d5c)

void wifi\_mgmt\_raise\_disconnect\_complete\_event(struct net\_if \*iface, int status)

Wi-Fi management disconnect complete event.

[NET\_REQUEST\_WIFI\_CONNECT](group__wifi__mgmt.md#gaa7ab2a97950a22736bb69f60b459f0f6)

#define NET\_REQUEST\_WIFI\_CONNECT

Request a Wi-Fi connect.

**Definition** wifi\_mgmt.h:138

[wifi\_ap\_status](group__wifi__mgmt.md#gaaf730bf76adc06434c7ac63bf0417884)

wifi\_ap\_status

Wi-Fi AP mode result codes.

**Definition** wifi\_mgmt.h:595

[NET\_REQUEST\_WIFI\_TWT](group__wifi__mgmt.md#gab84fd7e9ca0bf0b2b9d08889dda26aad)

#define NET\_REQUEST\_WIFI\_TWT

Request a Wi-Fi TWT.

**Definition** wifi\_mgmt.h:184

[wifi\_link\_mode](group__wifi__mgmt.md#gabdb2a784d4727b71ab44cca04e422c62)

wifi\_link\_mode

Wi-Fi link operating modes.

**Definition** wifi.h:328

[wifi\_ps\_param\_type](group__wifi__mgmt.md#gabe45d132797047c098041331c8f6f912)

wifi\_ps\_param\_type

Wi-Fi power save parameters.

**Definition** wifi.h:547

[net\_event\_wifi\_cmd](group__wifi__mgmt.md#gac2638308cbb0d268831f1618cf8e1fa8)

net\_event\_wifi\_cmd

Wi-Fi management events.

**Definition** wifi\_mgmt.h:302

[NET\_REQUEST\_WIFI\_CONN\_PARAMS](group__wifi__mgmt.md#gac6483341435ff380a2d4a69430899c1a)

#define NET\_REQUEST\_WIFI\_CONN\_PARAMS

Request a Wi-Fi connection parameters.

**Definition** wifi\_mgmt.h:232

[wifi\_disconn\_reason](group__wifi__mgmt.md#gac782af0a60b202fd19597cabb7bd3a9a)

wifi\_disconn\_reason

Wi-Fi disconnect reason codes.

**Definition** wifi\_mgmt.h:579

[wifi\_ps\_wakeup\_mode](group__wifi__mgmt.md#gac7f907644847e905d67c709fa4afae7f)

wifi\_ps\_wakeup\_mode

Wi-Fi power save modes.

**Definition** wifi.h:563

[wifi\_mgmt\_raise\_ap\_sta\_connected\_event](group__wifi__mgmt.md#gac8f17f0aa3e426a5cdb731727b9b9ce3)

void wifi\_mgmt\_raise\_ap\_sta\_connected\_event(struct net\_if \*iface, struct wifi\_ap\_sta\_info \*sta\_info)

Wi-Fi management AP mode STA connected event.

[wifi\_twt\_operation](group__wifi__mgmt.md#gad0e998aeb1b27c4f203ca76339d323a3)

wifi\_twt\_operation

Wi-Fi Target Wake Time (TWT) operations.

**Definition** wifi.h:425

[wifi\_scan\_type](group__wifi__mgmt.md#gad30e29eda65ccafdbd7f11865937b8ea)

wifi\_scan\_type

Wi-Fi scanning types.

**Definition** wifi.h:359

[scan\_result\_cb\_t](group__wifi__mgmt.md#gad34b366f1c315207ce0da587ca96d8d8)

void(\* scan\_result\_cb\_t)(struct net\_if \*iface, int status, struct wifi\_scan\_result \*entry)

Scan result callback.

**Definition** wifi\_mgmt.h:1191

[wifi\_twt\_teardown\_status](group__wifi__mgmt.md#gad3709d07aaa3ed59b48f9dd7bd181989)

wifi\_twt\_teardown\_status

Wi-Fi Target Wake Time (TWT) teradown status.

**Definition** wifi.h:506

[WIFI\_SSID\_MAX\_LEN](group__wifi__mgmt.md#gad62c60666c9fdffe2e0e9c4388f87886)

#define WIFI\_SSID\_MAX\_LEN

Max SSID length.

**Definition** wifi.h:227

[NET\_REQUEST\_WIFI\_CHANNEL](group__wifi__mgmt.md#gad9614d2368f8399850aaec05e40bdc78)

#define NET\_REQUEST\_WIFI\_CHANNEL

Request a Wi-Fi channel.

**Definition** wifi\_mgmt.h:214

[wifi\_config\_ps\_param\_fail\_reason](group__wifi__mgmt.md#gad98099584d2222ede93aba42b1fbaff0)

wifi\_config\_ps\_param\_fail\_reason

Wi-Fi power save error codes.

**Definition** wifi.h:592

[NET\_REQUEST\_WIFI\_11K\_CONFIG](group__wifi__mgmt.md#gadd9b5b206c7ee2e40c30a37c7b4fc002)

#define NET\_REQUEST\_WIFI\_11K\_CONFIG

**Definition** wifi\_mgmt.h:167

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

**Definition** wifi\_mgmt.h:811

[NET\_REQUEST\_WIFI\_ENTERPRISE\_CREDS](group__wifi__mgmt.md#gae5dc7835e11487187663dfe65a15f22b)

#define NET\_REQUEST\_WIFI\_ENTERPRISE\_CREDS

Set Wi-Fi enterprise mode CA/client Cert and key.

**Definition** wifi\_mgmt.h:271

[NET\_REQUEST\_WIFI\_AP\_CONFIG\_PARAM](group__wifi__mgmt.md#gaf4a78d230f5e0743a6aaf152ddda1c67)

#define NET\_REQUEST\_WIFI\_AP\_CONFIG\_PARAM

Request a Wi-Fi AP parameters configuration.

**Definition** wifi\_mgmt.h:244

[NET\_REQUEST\_WIFI\_AP\_DISABLE](group__wifi__mgmt.md#gaf81f62bf4c9e331a095acbf0d24ca1a2)

#define NET\_REQUEST\_WIFI\_AP\_DISABLE

Request a Wi-Fi access point disable.

**Definition** wifi\_mgmt.h:156

[wifi\_hostapd\_iface\_state](group__wifi__mgmt.md#gafb2e8c10f596da3527abf9e227c3001b)

wifi\_hostapd\_iface\_state

Wi-Fi AP status.

**Definition** wifi\_mgmt.h:1173

[wifi\_ps\_mode](group__wifi__mgmt.md#gaffae7d2a754be5eb952ad2b83edad54c)

wifi\_ps\_mode

Wi-Fi power save modes.

**Definition** wifi.h:378

[WIFI\_TWT\_STATE\_SLEEP](group__wifi__mgmt.md#gga38c184ea35c02f304cccdf389ca6d552a37a7aba20723b6614e39e1c417f3113c)

@ WIFI\_TWT\_STATE\_SLEEP

TWT sleep state: sleeping.

**Definition** wifi\_mgmt.h:862

[WIFI\_TWT\_STATE\_AWAKE](group__wifi__mgmt.md#gga38c184ea35c02f304cccdf389ca6d552a7b7b45f85d9644f897ca00bd7864e1b0)

@ WIFI\_TWT\_STATE\_AWAKE

TWT sleep state: awake.

**Definition** wifi\_mgmt.h:864

[WIFI\_WPS\_PBC](group__wifi__mgmt.md#gga4c36ae1a5171d3fbaeebf95c16be496da093f5b3ef95d9e571ea169430da57e88)

@ WIFI\_WPS\_PBC

WPS pbc.

**Definition** wifi\_mgmt.h:1156

[WIFI\_WPS\_PIN\_SET](group__wifi__mgmt.md#gga4c36ae1a5171d3fbaeebf95c16be496da58120620fd2fca80bdac7990ed0e7552)

@ WIFI\_WPS\_PIN\_SET

Set WPS pin number.

**Definition** wifi\_mgmt.h:1160

[WIFI\_WPS\_PIN\_GET](group__wifi__mgmt.md#gga4c36ae1a5171d3fbaeebf95c16be496da75bd5067903c2bba8a06732f0431393d)

@ WIFI\_WPS\_PIN\_GET

Get WPS pin number.

**Definition** wifi\_mgmt.h:1158

[WIFI\_STATUS\_CONN\_AP\_NOT\_FOUND](group__wifi__mgmt.md#gga86a5741e54aeb3e290142b0de217b8a8a2ae79fa389bb447fa108e0107aeff2f4)

@ WIFI\_STATUS\_CONN\_AP\_NOT\_FOUND

Connection failed - AP not found.

**Definition** wifi\_mgmt.h:569

[WIFI\_STATUS\_CONN\_SUCCESS](group__wifi__mgmt.md#gga86a5741e54aeb3e290142b0de217b8a8a380410b02b1e12599f37d1dcb844f5bd)

@ WIFI\_STATUS\_CONN\_SUCCESS

Connection successful.

**Definition** wifi\_mgmt.h:554

[WIFI\_STATUS\_CONN\_WRONG\_PASSWORD](group__wifi__mgmt.md#gga86a5741e54aeb3e290142b0de217b8a8a90d91f96a35c9f6847cbc7abd8c20bf8)

@ WIFI\_STATUS\_CONN\_WRONG\_PASSWORD

Connection failed - wrong password Few possible reasons for 4-way handshake failure that we can guess...

**Definition** wifi\_mgmt.h:565

[WIFI\_STATUS\_CONN\_FAIL](group__wifi__mgmt.md#gga86a5741e54aeb3e290142b0de217b8a8ab80ec4b70c75695fbe698034e2cb6a44)

@ WIFI\_STATUS\_CONN\_FAIL

Connection failed - generic failure.

**Definition** wifi\_mgmt.h:556

[WIFI\_STATUS\_CONN\_TIMEOUT](group__wifi__mgmt.md#gga86a5741e54aeb3e290142b0de217b8a8abb8783b92aec2ed1ffc6331979888563)

@ WIFI\_STATUS\_CONN\_TIMEOUT

Connection timed out.

**Definition** wifi\_mgmt.h:567

[WIFI\_STATUS\_DISCONN\_FIRST\_STATUS](group__wifi__mgmt.md#gga86a5741e54aeb3e290142b0de217b8a8abe1401e5d516c0d63291add15e558b18)

@ WIFI\_STATUS\_DISCONN\_FIRST\_STATUS

Connection disconnected status.

**Definition** wifi\_mgmt.h:573

[WIFI\_STATUS\_CONN\_LAST\_STATUS](group__wifi__mgmt.md#gga86a5741e54aeb3e290142b0de217b8a8aeee5fb8d8c3e7905554d08331f06191f)

@ WIFI\_STATUS\_CONN\_LAST\_STATUS

Last connection status.

**Definition** wifi\_mgmt.h:571

[NET\_REQUEST\_WIFI\_CMD\_AP\_CONFIG\_PARAM](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a14a0428720818c79df825d758e83f813)

@ NET\_REQUEST\_WIFI\_CMD\_AP\_CONFIG\_PARAM

Configure AP parameter.

**Definition** wifi\_mgmt.h:101

[NET\_REQUEST\_WIFI\_CMD\_TWT](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a1c9dc2d698326d987ffe5bfd35a9ed09)

@ NET\_REQUEST\_WIFI\_CMD\_TWT

Setup or teardown TWT flow.

**Definition** wifi\_mgmt.h:81

[NET\_REQUEST\_WIFI\_CMD\_PMKSA\_FLUSH](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a1fec11ed98f0a9411eefda9e55ee9aad)

@ NET\_REQUEST\_WIFI\_CMD\_PMKSA\_FLUSH

Flush PMKSA cache entries.

**Definition** wifi\_mgmt.h:109

[NET\_REQUEST\_WIFI\_CMD\_PACKET\_FILTER](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a2579ace546bf6954c111eb5951e894f5)

@ NET\_REQUEST\_WIFI\_CMD\_PACKET\_FILTER

Set or get packet filter setting for current mode.

**Definition** wifi\_mgmt.h:89

[NET\_REQUEST\_WIFI\_CMD\_AP\_ENABLE](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a28267d33b555433271cb121d62194a4c)

@ NET\_REQUEST\_WIFI\_CMD\_AP\_ENABLE

Enable AP mode.

**Definition** wifi\_mgmt.h:69

[NET\_REQUEST\_WIFI\_CMD\_START\_ROAMING](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a286205d961a77e44cd98e7894c48e676)

@ NET\_REQUEST\_WIFI\_CMD\_START\_ROAMING

Start roaming.

**Definition** wifi\_mgmt.h:121

[NET\_REQUEST\_WIFI\_CMD\_REG\_DOMAIN](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a367cc44caefd313e0c7ad3badc081456)

@ NET\_REQUEST\_WIFI\_CMD\_REG\_DOMAIN

Set or get regulatory domain.

**Definition** wifi\_mgmt.h:85

[NET\_REQUEST\_WIFI\_CMD\_11K\_NEIGHBOR\_REQUEST](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a48b3f0ec6647fb30d3b6456822c2dede)

@ NET\_REQUEST\_WIFI\_CMD\_11K\_NEIGHBOR\_REQUEST

Send 11k neighbor request.

**Definition** wifi\_mgmt.h:77

[NET\_REQUEST\_WIFI\_CMD\_SCAN](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a4aadf9114010c09bd7420c99a2049d5a)

@ NET\_REQUEST\_WIFI\_CMD\_SCAN

Scan for Wi-Fi networks.

**Definition** wifi\_mgmt.h:63

[NET\_REQUEST\_WIFI\_CMD\_IFACE\_STATUS](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a6af9d52df8f9db6393044e42e10ff0de)

@ NET\_REQUEST\_WIFI\_CMD\_IFACE\_STATUS

Get interface status.

**Definition** wifi\_mgmt.h:73

[NET\_REQUEST\_WIFI\_CMD\_AP\_STA\_DISCONNECT](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a6f3865aa6a4d7633e241ee2b002c1b5a)

@ NET\_REQUEST\_WIFI\_CMD\_AP\_STA\_DISCONNECT

Disconnect a STA from AP.

**Definition** wifi\_mgmt.h:93

[NET\_REQUEST\_WIFI\_CMD\_DPP](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a6fc4d3aca344dc551dd62ae1d6072104)

@ NET\_REQUEST\_WIFI\_CMD\_DPP

DPP actions.

**Definition** wifi\_mgmt.h:103

[NET\_REQUEST\_WIFI\_CMD\_AP\_DISABLE](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a6fe9d7137b4cd20de880955b27382ccf)

@ NET\_REQUEST\_WIFI\_CMD\_AP\_DISABLE

Disable AP mode.

**Definition** wifi\_mgmt.h:71

[NET\_REQUEST\_WIFI\_CMD\_RTS\_THRESHOLD](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a7852cff28fc18ddd7af0f8224c840e7b)

@ NET\_REQUEST\_WIFI\_CMD\_RTS\_THRESHOLD

Set RTS threshold.

**Definition** wifi\_mgmt.h:99

[NET\_REQUEST\_WIFI\_CMD\_CONNECT](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a78c958877ee60c90803c925b6b2f057a)

@ NET\_REQUEST\_WIFI\_CMD\_CONNECT

Connect to a Wi-Fi network.

**Definition** wifi\_mgmt.h:65

[NET\_REQUEST\_WIFI\_CMD\_VERSION](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a7d9596f2cce54c9e050d89469e86eccb)

@ NET\_REQUEST\_WIFI\_CMD\_VERSION

Get Wi-Fi driver and Firmware versions.

**Definition** wifi\_mgmt.h:95

[NET\_REQUEST\_WIFI\_CMD\_ENTERPRISE\_CREDS](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a94b7fb7a8c529082e1d0458298b6c3fb)

@ NET\_REQUEST\_WIFI\_CMD\_ENTERPRISE\_CREDS

Set enterprise mode credential.

**Definition** wifi\_mgmt.h:111

[NET\_REQUEST\_WIFI\_CMD\_CONN\_PARAMS](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77aa150f53621941796082e00090bde6a5a)

@ NET\_REQUEST\_WIFI\_CMD\_CONN\_PARAMS

Get Wi-Fi latest connection parameters.

**Definition** wifi\_mgmt.h:97

[NET\_REQUEST\_WIFI\_CMD\_11K\_CONFIG](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77aa86fb7193245593dd84b3a4376bc25d6)

@ NET\_REQUEST\_WIFI\_CMD\_11K\_CONFIG

Set or get 11k status.

**Definition** wifi\_mgmt.h:75

[NET\_REQUEST\_WIFI\_CMD\_CHANNEL](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77aade3d7a43c730a52f7876c6486170bb2)

@ NET\_REQUEST\_WIFI\_CMD\_CHANNEL

Set or get Wi-Fi channel for Monitor or TX-Injection mode.

**Definition** wifi\_mgmt.h:91

[NET\_REQUEST\_WIFI\_CMD\_MODE](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77ab7183584bdf5fe673d39fa0d090e3899)

@ NET\_REQUEST\_WIFI\_CMD\_MODE

Set or get Mode of operation.

**Definition** wifi\_mgmt.h:87

[NET\_REQUEST\_WIFI\_CMD\_RTS\_THRESHOLD\_CONFIG](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77ab7a4215540d2e6cda0d522dc621e9d89)

@ NET\_REQUEST\_WIFI\_CMD\_RTS\_THRESHOLD\_CONFIG

Get RTS threshold.

**Definition** wifi\_mgmt.h:113

[NET\_REQUEST\_WIFI\_CMD\_CANDIDATE\_SCAN](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77ab7bc479691f88138972d0d8e1e2179ed)

@ NET\_REQUEST\_WIFI\_CMD\_CANDIDATE\_SCAN

Specific scan.

**Definition** wifi\_mgmt.h:125

[NET\_REQUEST\_WIFI\_CMD\_PS](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77abf9fb93c205fa36f74a9ef19d3d0351a)

@ NET\_REQUEST\_WIFI\_CMD\_PS

Set power save status.

**Definition** wifi\_mgmt.h:79

[NET\_REQUEST\_WIFI\_CMD\_DISCONNECT](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77ac33941da138b993f7a1158d91469bcb7)

@ NET\_REQUEST\_WIFI\_CMD\_DISCONNECT

Disconnect from a Wi-Fi network.

**Definition** wifi\_mgmt.h:67

[NET\_REQUEST\_WIFI\_CMD\_NEIGHBOR\_REP\_COMPLETE](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77ad950aa5b87408793f4df9c39fe84cc55)

@ NET\_REQUEST\_WIFI\_CMD\_NEIGHBOR\_REP\_COMPLETE

Neighbor report complete.

**Definition** wifi\_mgmt.h:123

[NET\_REQUEST\_WIFI\_CMD\_PS\_CONFIG](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77ae6ce1c605d1bf7c09650ec15d74e77e9)

@ NET\_REQUEST\_WIFI\_CMD\_PS\_CONFIG

Get power save config.

**Definition** wifi\_mgmt.h:83

[NET\_REQUEST\_WIFI\_CMD\_WPS\_CONFIG](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77aec78bf6196abee310e06a8454d27eed7)

@ NET\_REQUEST\_WIFI\_CMD\_WPS\_CONFIG

WPS config.

**Definition** wifi\_mgmt.h:115

[WIFI\_STATUS\_AP\_CHANNEL\_NOT\_ALLOWED](group__wifi__mgmt.md#ggaaf730bf76adc06434c7ac63bf0417884a0b1cb592c54c16e8a54defee71c5fd15)

@ WIFI\_STATUS\_AP\_CHANNEL\_NOT\_ALLOWED

AP mode enable failed - channel not allowed.

**Definition** wifi\_mgmt.h:603

[WIFI\_STATUS\_AP\_SUCCESS](group__wifi__mgmt.md#ggaaf730bf76adc06434c7ac63bf0417884a0df52848da8735892d0eb1e381b2cd7c)

@ WIFI\_STATUS\_AP\_SUCCESS

AP mode enable or disable successful.

**Definition** wifi\_mgmt.h:597

[WIFI\_STATUS\_AP\_OP\_NOT\_SUPPORTED](group__wifi__mgmt.md#ggaaf730bf76adc06434c7ac63bf0417884a2105e6c49b3bcb5f7dcacbc1e5ce9cca)

@ WIFI\_STATUS\_AP\_OP\_NOT\_SUPPORTED

AP mode enable failed - operation not supported.

**Definition** wifi\_mgmt.h:609

[WIFI\_STATUS\_AP\_OP\_NOT\_PERMITTED](group__wifi__mgmt.md#ggaaf730bf76adc06434c7ac63bf0417884a36a58980bdc7877c910441590137ddbe)

@ WIFI\_STATUS\_AP\_OP\_NOT\_PERMITTED

AP mode enable failed - operation not permitted.

**Definition** wifi\_mgmt.h:611

[WIFI\_STATUS\_AP\_CHANNEL\_NOT\_SUPPORTED](group__wifi__mgmt.md#ggaaf730bf76adc06434c7ac63bf0417884a5acb85a2361ca72ed10966b829c5753b)

@ WIFI\_STATUS\_AP\_CHANNEL\_NOT\_SUPPORTED

AP mode enable failed - channel not supported.

**Definition** wifi\_mgmt.h:601

[WIFI\_STATUS\_AP\_FAIL](group__wifi__mgmt.md#ggaaf730bf76adc06434c7ac63bf0417884a6c6801381caa3862004662169202fa9a)

@ WIFI\_STATUS\_AP\_FAIL

AP mode enable or disable failed - generic failure.

**Definition** wifi\_mgmt.h:599

[WIFI\_STATUS\_AP\_AUTH\_TYPE\_NOT\_SUPPORTED](group__wifi__mgmt.md#ggaaf730bf76adc06434c7ac63bf0417884abe5a626d22051522255d98fdfdfbfcc8)

@ WIFI\_STATUS\_AP\_AUTH\_TYPE\_NOT\_SUPPORTED

AP mode enable failed - authentication type not supported.

**Definition** wifi\_mgmt.h:607

[WIFI\_STATUS\_AP\_SSID\_NOT\_ALLOWED](group__wifi__mgmt.md#ggaaf730bf76adc06434c7ac63bf0417884ac18a7b551f8c6bb7737b0e8e60c323ce)

@ WIFI\_STATUS\_AP\_SSID\_NOT\_ALLOWED

AP mode enable failed - SSID not allowed.

**Definition** wifi\_mgmt.h:605

[NET\_EVENT\_WIFI\_CMD\_AP\_STA\_DISCONNECTED](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8a3678a39f9542968958b5575d571d4e2e)

@ NET\_EVENT\_WIFI\_CMD\_AP\_STA\_DISCONNECTED

STA disconnected from AP.

**Definition** wifi\_mgmt.h:336

[NET\_EVENT\_WIFI\_CMD\_SCAN\_RESULT](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8a37e9ab2a6832153fa968337d920e587e)

@ NET\_EVENT\_WIFI\_CMD\_SCAN\_RESULT

Scan results available.

**Definition** wifi\_mgmt.h:304

[NET\_EVENT\_WIFI\_CMD\_DISCONNECT\_RESULT](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8a3a3b0387f83d8fb24a0e27312468b0eb)

@ NET\_EVENT\_WIFI\_CMD\_DISCONNECT\_RESULT

Disconnect result.

**Definition** wifi\_mgmt.h:310

[NET\_EVENT\_WIFI\_CMD\_SUPPLICANT](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8a4ec52c22e23502421077e46e94facf08)

@ NET\_EVENT\_WIFI\_CMD\_SUPPLICANT

Supplicant specific event.

**Definition** wifi\_mgmt.h:338

[NET\_EVENT\_WIFI\_CMD\_NEIGHBOR\_REP\_RECEIVED](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8a75a0a093f32fa2577286c92c2525df91)

@ NET\_EVENT\_WIFI\_CMD\_NEIGHBOR\_REP\_RECEIVED

Neighbor Report.

**Definition** wifi\_mgmt.h:326

[NET\_EVENT\_WIFI\_CMD\_TWT\_SLEEP\_STATE](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8a78838bf7ce80cee5e803712cd0286750)

@ NET\_EVENT\_WIFI\_CMD\_TWT\_SLEEP\_STATE

TWT sleep status: awake or sleeping, can be used by application to determine if it can send data or n...

**Definition** wifi\_mgmt.h:318

[NET\_EVENT\_WIFI\_CMD\_NEIGHBOR\_REP\_COMPLETE](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8a86b6811a06f6158ae9ea4687e219e5af)

@ NET\_EVENT\_WIFI\_CMD\_NEIGHBOR\_REP\_COMPLETE

Neighbor Report complete.

**Definition** wifi\_mgmt.h:328

[NET\_EVENT\_WIFI\_CMD\_AP\_ENABLE\_RESULT](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8abd1797564427886eeb14dd293ae86a9b)

@ NET\_EVENT\_WIFI\_CMD\_AP\_ENABLE\_RESULT

AP mode enable result.

**Definition** wifi\_mgmt.h:330

[NET\_EVENT\_WIFI\_CMD\_AP\_STA\_CONNECTED](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8abd4269b2cd1302ce61da4f8d7bb9d5fb)

@ NET\_EVENT\_WIFI\_CMD\_AP\_STA\_CONNECTED

STA connected to AP.

**Definition** wifi\_mgmt.h:334

[NET\_EVENT\_WIFI\_CMD\_SIGNAL\_CHANGE](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8acc9d8a16d99e4006b915b3686522a8e0)

@ NET\_EVENT\_WIFI\_CMD\_SIGNAL\_CHANGE

Signal change event.

**Definition** wifi\_mgmt.h:324

[NET\_EVENT\_WIFI\_CMD\_SCAN\_DONE](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8ad753b7e4588257815f4a60a539ca2018)

@ NET\_EVENT\_WIFI\_CMD\_SCAN\_DONE

Scan done.

**Definition** wifi\_mgmt.h:306

[NET\_EVENT\_WIFI\_CMD\_TWT](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8adad71603ed829ed92d06f8c40efa9b18)

@ NET\_EVENT\_WIFI\_CMD\_TWT

TWT events.

**Definition** wifi\_mgmt.h:314

[NET\_EVENT\_WIFI\_CMD\_RAW\_SCAN\_RESULT](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8addf15c69512be7ab4957e7c0b3fde0ac)

@ NET\_EVENT\_WIFI\_CMD\_RAW\_SCAN\_RESULT

Raw scan results available.

**Definition** wifi\_mgmt.h:320

[NET\_EVENT\_WIFI\_CMD\_AP\_DISABLE\_RESULT](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8aeec3d7a9191280c2326034a17555308d)

@ NET\_EVENT\_WIFI\_CMD\_AP\_DISABLE\_RESULT

AP mode disable result.

**Definition** wifi\_mgmt.h:332

[NET\_EVENT\_WIFI\_CMD\_DISCONNECT\_COMPLETE](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8af1c42bd59f01260c64ede07da436c18f)

@ NET\_EVENT\_WIFI\_CMD\_DISCONNECT\_COMPLETE

Disconnect complete.

**Definition** wifi\_mgmt.h:322

[NET\_EVENT\_WIFI\_CMD\_IFACE\_STATUS](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8af4b3f1969b96f63253851c26c3882a14)

@ NET\_EVENT\_WIFI\_CMD\_IFACE\_STATUS

Interface status.

**Definition** wifi\_mgmt.h:312

[NET\_EVENT\_WIFI\_CMD\_CONNECT\_RESULT](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8af76f28777b91b365dc3f97028bc18e3c)

@ NET\_EVENT\_WIFI\_CMD\_CONNECT\_RESULT

Connect result.

**Definition** wifi\_mgmt.h:308

[WIFI\_REASON\_DISCONN\_INACTIVITY](group__wifi__mgmt.md#ggac782af0a60b202fd19597cabb7bd3a9aa05fe2f87de30de47ee48f7615c2206e6)

@ WIFI\_REASON\_DISCONN\_INACTIVITY

Disconnected due to inactivity.

**Definition** wifi\_mgmt.h:589

[WIFI\_REASON\_DISCONN\_AP\_LEAVING](group__wifi__mgmt.md#ggac782af0a60b202fd19597cabb7bd3a9aa34e3f78ce43db3daeaf32038e0baf204)

@ WIFI\_REASON\_DISCONN\_AP\_LEAVING

Disconnected due to AP leaving.

**Definition** wifi\_mgmt.h:587

[WIFI\_REASON\_DISCONN\_SUCCESS](group__wifi__mgmt.md#ggac782af0a60b202fd19597cabb7bd3a9aa5c894399db8949a789ca4f5750b6f042)

@ WIFI\_REASON\_DISCONN\_SUCCESS

Success, overload status as reason.

**Definition** wifi\_mgmt.h:581

[WIFI\_REASON\_DISCONN\_UNSPECIFIED](group__wifi__mgmt.md#ggac782af0a60b202fd19597cabb7bd3a9aa87f5d64a9fd3acf8d67c698199779e5c)

@ WIFI\_REASON\_DISCONN\_UNSPECIFIED

Unspecified reason.

**Definition** wifi\_mgmt.h:583

[WIFI\_REASON\_DISCONN\_USER\_REQUEST](group__wifi__mgmt.md#ggac782af0a60b202fd19597cabb7bd3a9aaee75adafb52bd6ecaa547a76c6ccd0a7)

@ WIFI\_REASON\_DISCONN\_USER\_REQUEST

Disconnected due to user request.

**Definition** wifi\_mgmt.h:585

[WIFI\_MGMT\_GET](group__wifi__mgmt.md#ggae129d0783276e662575af2314eef86cda6b8183a773e0cdfa85bc4b41ae70fdcd)

@ WIFI\_MGMT\_GET

Get operation.

**Definition** wifi\_mgmt.h:813

[WIFI\_MGMT\_SET](group__wifi__mgmt.md#ggae129d0783276e662575af2314eef86cdaa0d5931c8275a8d3288ab668b6dfb5a1)

@ WIFI\_MGMT\_SET

Set operation.

**Definition** wifi\_mgmt.h:815

[WIFI\_HAPD\_IFACE\_DISABLED](group__wifi__mgmt.md#ggafb2e8c10f596da3527abf9e227c3001ba21e99c5fff612afd417c0d4511a9c135)

@ WIFI\_HAPD\_IFACE\_DISABLED

**Definition** wifi\_mgmt.h:1175

[WIFI\_HAPD\_IFACE\_DFS](group__wifi__mgmt.md#ggafb2e8c10f596da3527abf9e227c3001ba2bcdccb48ba12b2561e08292365801a0)

@ WIFI\_HAPD\_IFACE\_DFS

**Definition** wifi\_mgmt.h:1179

[WIFI\_HAPD\_IFACE\_HT\_SCAN](group__wifi__mgmt.md#ggafb2e8c10f596da3527abf9e227c3001ba66a141b5b317ac3dc0ca383886458a00)

@ WIFI\_HAPD\_IFACE\_HT\_SCAN

**Definition** wifi\_mgmt.h:1178

[WIFI\_HAPD\_IFACE\_ACS](group__wifi__mgmt.md#ggafb2e8c10f596da3527abf9e227c3001ba762c44f87b3dd9a08d2442b86ad06168)

@ WIFI\_HAPD\_IFACE\_ACS

**Definition** wifi\_mgmt.h:1177

[WIFI\_HAPD\_IFACE\_UNINITIALIZED](group__wifi__mgmt.md#ggafb2e8c10f596da3527abf9e227c3001ba7b4af20b16fb8881b963d4f2ebdad11a)

@ WIFI\_HAPD\_IFACE\_UNINITIALIZED

**Definition** wifi\_mgmt.h:1174

[WIFI\_HAPD\_IFACE\_ENABLED](group__wifi__mgmt.md#ggafb2e8c10f596da3527abf9e227c3001ba82333796edc42607754281a400f07b2a)

@ WIFI\_HAPD\_IFACE\_ENABLED

**Definition** wifi\_mgmt.h:1180

[WIFI\_HAPD\_IFACE\_COUNTRY\_UPDATE](group__wifi__mgmt.md#ggafb2e8c10f596da3527abf9e227c3001badd81c06c029edaa9ac973e03136d4ff4)

@ WIFI\_HAPD\_IFACE\_COUNTRY\_UPDATE

**Definition** wifi\_mgmt.h:1176

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

**Definition** device.h:412

[ethernet\_api](structethernet__api.md)

Ethernet L2 API operations.

**Definition** ethernet.h:534

[net\_if](structnet__if.md)

Network Interface structure.

**Definition** net\_if.h:680

[net\_stats\_wifi](structnet__stats__wifi.md)

All Wi-Fi specific statistics.

**Definition** net\_stats.h:624

[net\_wifi\_mgmt\_offload](structnet__wifi__mgmt__offload.md)

Wi-Fi management offload API.

**Definition** wifi\_mgmt.h:1468

[net\_wifi\_mgmt\_offload::wifi\_iface](structnet__wifi__mgmt__offload.md#a1d34a954a2f16d29f51dc51dd6fbb845)

struct ethernet\_api wifi\_iface

Mandatory to get in first position.

**Definition** wifi\_mgmt.h:1477

[net\_wifi\_mgmt\_offload::wifi\_mgmt\_api](structnet__wifi__mgmt__offload.md#a98fcc053d9820d2d981ed659520c9b3b)

const struct wifi\_mgmt\_ops \*const wifi\_mgmt\_api

Wi-Fi management API.

**Definition** wifi\_mgmt.h:1483

[net\_wifi\_mgmt\_offload::wifi\_drv\_ops](structnet__wifi__mgmt__offload.md#a991e0bc6247578a3d1c9d2d3ab0b63d7)

const void \* wifi\_drv\_ops

Wi-Fi supplicant driver API.

**Definition** wifi\_mgmt.h:1487

[offloaded\_if\_api](structoffloaded__if__api.md)

Extended net\_if\_api for offloaded ifaces/network devices, allowing handling of admin up/down state ch...

**Definition** offloaded\_netdev.h:53

[wifi\_11k\_params](structwifi__11k__params.md)

Wi-Fi 11k parameters.

**Definition** wifi\_mgmt.h:819

[wifi\_11k\_params::ssid](structwifi__11k__params.md#a64ace23c71837417678ceb9cc8d5f216)

uint8\_t ssid[WIFI\_SSID\_MAX\_LEN+1]

SSID.

**Definition** wifi\_mgmt.h:825

[wifi\_11k\_params::enable\_11k](structwifi__11k__params.md#a739c3e94b025aae2fcf5680aecf3d646)

bool enable\_11k

11k enable/disable

**Definition** wifi\_mgmt.h:823

[wifi\_11k\_params::oper](structwifi__11k__params.md#ae6029ed4bada41f18df0329d0da7401e)

enum wifi\_mgmt\_op oper

11k command operation

**Definition** wifi\_mgmt.h:821

[wifi\_ap\_config\_params](structwifi__ap__config__params.md)

Wi-Fi AP configuration parameter.

**Definition** wifi\_mgmt.h:946

[wifi\_ap\_config\_params::max\_inactivity](structwifi__ap__config__params.md#a289866d9209450e893281b4c198a546a)

uint32\_t max\_inactivity

Parameter used for setting maximum inactivity duration for stations.

**Definition** wifi\_mgmt.h:950

[wifi\_ap\_config\_params::type](structwifi__ap__config__params.md#a4c391cf504a994ed0bc4971afdf76774)

enum wifi\_ap\_config\_param type

Parameter used to identify the different AP parameters.

**Definition** wifi\_mgmt.h:948

[wifi\_ap\_config\_params::max\_num\_sta](structwifi__ap__config__params.md#a7fc0fad99f53ed8e1ac40b74ec98bf9a)

uint32\_t max\_num\_sta

Parameter used for setting maximum number of stations.

**Definition** wifi\_mgmt.h:952

[wifi\_ap\_sta\_info](structwifi__ap__sta__info.md)

AP mode - connected STA details.

**Definition** wifi\_mgmt.h:882

[wifi\_ap\_sta\_info::link\_mode](structwifi__ap__sta__info.md#a7d8bd52340d4937a4b5b7d2c00662441)

enum wifi\_link\_mode link\_mode

Link mode, see enum wifi\_link\_mode.

**Definition** wifi\_mgmt.h:884

[wifi\_ap\_sta\_info::mac](structwifi__ap__sta__info.md#a7db904376ec73b774aa9d8236c15b3f6)

uint8\_t mac[WIFI\_MAC\_ADDR\_LEN]

MAC address.

**Definition** wifi\_mgmt.h:886

[wifi\_ap\_sta\_info::mac\_length](structwifi__ap__sta__info.md#a7f7c8b144bb3464af5213708591eefda)

uint8\_t mac\_length

MAC address length.

**Definition** wifi\_mgmt.h:888

[wifi\_ap\_sta\_info::twt\_capable](structwifi__ap__sta__info.md#a838c9a4288c9bc7e97afe2334c678f34)

bool twt\_capable

is TWT capable ?

**Definition** wifi\_mgmt.h:890

[wifi\_band\_channel](structwifi__band__channel.md)

Wi-Fi structure to uniquely identify a band-channel pair.

**Definition** wifi\_mgmt.h:412

[wifi\_band\_channel::band](structwifi__band__channel.md#a4a932599429f37231f76c3064ec5efb3)

uint8\_t band

Frequency band.

**Definition** wifi\_mgmt.h:414

[wifi\_band\_channel::channel](structwifi__band__channel.md#acd0dd7366de3650124dad7232a58ade0)

uint8\_t channel

Channel.

**Definition** wifi\_mgmt.h:416

[wifi\_channel\_info](structwifi__channel__info.md)

Wi-Fi channel setting for monitor and TX-injection modes.

**Definition** wifi\_mgmt.h:932

[wifi\_channel\_info::if\_index](structwifi__channel__info.md#a43a7dd8c19d0c6540e3cc0b5d1d6165d)

uint8\_t if\_index

Interface index.

**Definition** wifi\_mgmt.h:936

[wifi\_channel\_info::channel](structwifi__channel__info.md#a799cbc0a67764f6680322ba0f2ad3300)

uint16\_t channel

Channel value to set.

**Definition** wifi\_mgmt.h:934

[wifi\_channel\_info::oper](structwifi__channel__info.md#aa8ef8a71b49ead3664fff9a4d61b1ce8)

enum wifi\_mgmt\_op oper

Get or set operation.

**Definition** wifi\_mgmt.h:938

[wifi\_connect\_req\_params](structwifi__connect__req__params.md)

Wi-Fi connect request parameters.

**Definition** wifi\_mgmt.h:496

[wifi\_connect\_req\_params::key2\_passwd](structwifi__connect__req__params.md#a020fc58d7e5350cc803cd5d6fa575e6a)

const uint8\_t \* key2\_passwd

private key2 passwd

**Definition** wifi\_mgmt.h:530

[wifi\_connect\_req\_params::ft\_used](structwifi__connect__req__params.md#a047b11e703fb646d778785dfcb14257b)

bool ft\_used

Fast BSS Transition used.

**Definition** wifi\_mgmt.h:546

[wifi\_connect\_req\_params::security](structwifi__connect__req__params.md#a18dce6bb021086877a30e7a04f5b24b9)

enum wifi\_security\_type security

Security type.

**Definition** wifi\_mgmt.h:514

[wifi\_connect\_req\_params::aid\_length](structwifi__connect__req__params.md#a2892253024b70e5cb8eb2166b17ebe22)

uint8\_t aid\_length

anon\_id length, max 64

**Definition** wifi\_mgmt.h:524

[wifi\_connect\_req\_params::sae\_password](structwifi__connect__req__params.md#a469fac5758b78fc425911837930b2060)

const uint8\_t \* sae\_password

SAE password (same as PSK but with no length restrictions), optional.

**Definition** wifi\_mgmt.h:506

[wifi\_connect\_req\_params::key\_passwd](structwifi__connect__req__params.md#a4946647659a347667ee49bb6990bba66)

const uint8\_t \* key\_passwd

Private key passwd for enterprise mode.

**Definition** wifi\_mgmt.h:526

[wifi\_connect\_req\_params::eap\_id\_length](structwifi__connect__req__params.md#a4da02ff112c09f55dc5bddcda27d16a3)

uint8\_t eap\_id\_length

eap identity length, max 64

**Definition** wifi\_mgmt.h:540

[wifi\_connect\_req\_params::channel](structwifi__connect__req__params.md#a52b6d0323c35d03ec239f40be35cae72)

uint8\_t channel

Channel.

**Definition** wifi\_mgmt.h:512

[wifi\_connect\_req\_params::ssid\_length](structwifi__connect__req__params.md#a547dddf6be5dd77eda74b1085a798400)

uint8\_t ssid\_length

SSID length.

**Definition** wifi\_mgmt.h:500

[wifi\_connect\_req\_params::timeout](structwifi__connect__req__params.md#a56183ba7f4d8eaf5fc5b495856adecfd)

int timeout

Connect timeout in seconds, SYS\_FOREVER\_MS for no timeout.

**Definition** wifi\_mgmt.h:520

[wifi\_connect\_req\_params::mfp](structwifi__connect__req__params.md#a745b3416172672a7e5b12bcc5b55e88c)

enum wifi\_mfp\_options mfp

MFP options.

**Definition** wifi\_mgmt.h:516

[wifi\_connect\_req\_params::sae\_password\_length](structwifi__connect__req__params.md#a74f0819e7a546ffb8bfb0ec587eccf20)

uint8\_t sae\_password\_length

SAE password length.

**Definition** wifi\_mgmt.h:508

[wifi\_connect\_req\_params::anon\_id](structwifi__connect__req__params.md#a781456e079357e2e1096218af3bd218c)

const uint8\_t \* anon\_id

anonymous identity

**Definition** wifi\_mgmt.h:522

[wifi\_connect\_req\_params::key\_passwd\_length](structwifi__connect__req__params.md#a9f913fc0ccecafaba488e444d701fd68)

uint8\_t key\_passwd\_length

Private key passwd length, max 128.

**Definition** wifi\_mgmt.h:528

[wifi\_connect\_req\_params::band](structwifi__connect__req__params.md#aa2fea1881a8ffdf5d7093ae295867f3e)

uint8\_t band

Frequency band.

**Definition** wifi\_mgmt.h:510

[wifi\_connect\_req\_params::psk](structwifi__connect__req__params.md#aa7743f0ecbc27a9595720ce13ce57c1d)

const uint8\_t \* psk

Pre-shared key.

**Definition** wifi\_mgmt.h:502

[wifi\_connect\_req\_params::bssid](structwifi__connect__req__params.md#aa8081b9075ff9244cefd0ac1ef3f42cb)

uint8\_t bssid[WIFI\_MAC\_ADDR\_LEN]

BSSID.

**Definition** wifi\_mgmt.h:518

[wifi\_connect\_req\_params::eap\_ver](structwifi__connect__req__params.md#aa903297e7ee4801b350b2e3a3a89f28a)

uint8\_t eap\_ver

eap version

**Definition** wifi\_mgmt.h:536

[wifi\_connect\_req\_params::psk\_length](structwifi__connect__req__params.md#aaf7455a65590d19f047214b459a2dcb9)

uint8\_t psk\_length

Pre-shared key length.

**Definition** wifi\_mgmt.h:504

[wifi\_connect\_req\_params::eap\_identity](structwifi__connect__req__params.md#ab9c65599409387af65a3c2895c3116da)

const uint8\_t \* eap\_identity

Identity for EAP.

**Definition** wifi\_mgmt.h:538

[wifi\_connect\_req\_params::ssid](structwifi__connect__req__params.md#ac260c2cd17a3f36ea101edaf23d41083)

const uint8\_t \* ssid

SSID.

**Definition** wifi\_mgmt.h:498

[wifi\_connect\_req\_params::suiteb\_type](structwifi__connect__req__params.md#ac8eaaecd8227e5500bdaf8cddf05a065)

uint8\_t suiteb\_type

suiteb or suiteb-192

**Definition** wifi\_mgmt.h:534

[wifi\_connect\_req\_params::eap\_passwd\_length](structwifi__connect__req__params.md#aeab22e95a04a1831b87beda1772d3db7)

uint8\_t eap\_passwd\_length

eap passwd length, max 128

**Definition** wifi\_mgmt.h:544

[wifi\_connect\_req\_params::key2\_passwd\_length](structwifi__connect__req__params.md#af7b163cc2bffc59f7fa31f47c5e52062)

uint8\_t key2\_passwd\_length

key2 passwd length, max 128

**Definition** wifi\_mgmt.h:532

[wifi\_connect\_req\_params::eap\_password](structwifi__connect__req__params.md#afd046e702739c4a0d89322ee41b37acd)

const uint8\_t \* eap\_password

Password string for EAP.

**Definition** wifi\_mgmt.h:542

[wifi\_enterprise\_creds\_params](structwifi__enterprise__creds__params.md)

Wi-Fi enterprise mode credentials.

**Definition** wifi\_mgmt.h:773

[wifi\_enterprise\_creds\_params::client\_key\_len](structwifi__enterprise__creds__params.md#a09f5b34c81fe871e7513358499518d95)

uint32\_t client\_key\_len

Client key length.

**Definition** wifi\_mgmt.h:785

[wifi\_enterprise\_creds\_params::client\_cert2](structwifi__enterprise__creds__params.md#a133126e338d89563733268a03e2fa613)

uint8\_t \* client\_cert2

Client certification of phase2.

**Definition** wifi\_mgmt.h:791

[wifi\_enterprise\_creds\_params::client\_key2\_len](structwifi__enterprise__creds__params.md#a3da90b8a8dfa848f617579760ad4f971)

uint32\_t client\_key2\_len

Phase2 Client key length.

**Definition** wifi\_mgmt.h:797

[wifi\_enterprise\_creds\_params::client\_cert\_len](structwifi__enterprise__creds__params.md#a5f122d59b25b00af2db7eeac93d5482e)

uint32\_t client\_cert\_len

Client certification length.

**Definition** wifi\_mgmt.h:781

[wifi\_enterprise\_creds\_params::ca\_cert\_len](structwifi__enterprise__creds__params.md#a5f7060fcd2ca3db0b202faf15062564b)

uint32\_t ca\_cert\_len

CA certification length.

**Definition** wifi\_mgmt.h:777

[wifi\_enterprise\_creds\_params::client\_cert](structwifi__enterprise__creds__params.md#a81d61179feba627be5c6456130b9f2af)

uint8\_t \* client\_cert

Client certification.

**Definition** wifi\_mgmt.h:779

[wifi\_enterprise\_creds\_params::client\_key](structwifi__enterprise__creds__params.md#a8d88f5a8a6ccc8a9a883078af49ae96b)

uint8\_t \* client\_key

Client key.

**Definition** wifi\_mgmt.h:783

[wifi\_enterprise\_creds\_params::client\_key2](structwifi__enterprise__creds__params.md#abcda4d7820681d517d70d8f130b47050)

uint8\_t \* client\_key2

Client key of phase2.

**Definition** wifi\_mgmt.h:795

[wifi\_enterprise\_creds\_params::ca\_cert2\_len](structwifi__enterprise__creds__params.md#abf35045e71afb0cb9ea25c635c5ac141)

uint32\_t ca\_cert2\_len

Phase2 CA certification length.

**Definition** wifi\_mgmt.h:789

[wifi\_enterprise\_creds\_params::ca\_cert2](structwifi__enterprise__creds__params.md#ad9b867873709d7f2363fef49d7b6f2ca)

uint8\_t \* ca\_cert2

CA certification of phase2.

**Definition** wifi\_mgmt.h:787

[wifi\_enterprise\_creds\_params::client\_cert2\_len](structwifi__enterprise__creds__params.md#adbe26c9b88f44eb6b875888f6a03e1bb)

uint32\_t client\_cert2\_len

Phase2 Client certification length.

**Definition** wifi\_mgmt.h:793

[wifi\_enterprise\_creds\_params::ca\_cert](structwifi__enterprise__creds__params.md#ae37381504a457b2f1d56dd5270c6711d)

uint8\_t \* ca\_cert

CA certification.

**Definition** wifi\_mgmt.h:775

[wifi\_filter\_info](structwifi__filter__info.md)

Wi-Fi filter setting for monitor, prmoiscuous, TX-injection modes.

**Definition** wifi\_mgmt.h:920

[wifi\_filter\_info::buffer\_size](structwifi__filter__info.md#a1b2d0448fc7f62654e3f5aacfba62f8f)

uint16\_t buffer\_size

Filter buffer size.

**Definition** wifi\_mgmt.h:926

[wifi\_filter\_info::filter](structwifi__filter__info.md#ad9560be814299055cfa11b995a7dcf42)

uint8\_t filter

Filter setting.

**Definition** wifi\_mgmt.h:922

[wifi\_filter\_info::oper](structwifi__filter__info.md#aedd5e220cdde5768cb0f4aff920971cd)

enum wifi\_mgmt\_op oper

Get or set operation.

**Definition** wifi\_mgmt.h:928

[wifi\_filter\_info::if\_index](structwifi__filter__info.md#af9ea91e31e78afcb7ffe1ff9a04277a3)

uint8\_t if\_index

Interface index.

**Definition** wifi\_mgmt.h:924

[wifi\_iface\_status](structwifi__iface__status.md)

Wi-Fi interface status.

**Definition** wifi\_mgmt.h:629

[wifi\_iface\_status::beacon\_interval](structwifi__iface__status.md#a241bfbe70628006b515b5f9e4f97665c)

unsigned short beacon\_interval

Beacon interval.

**Definition** wifi\_mgmt.h:655

[wifi\_iface\_status::ssid](structwifi__iface__status.md#a3ab671471bcdfeb5b955d156d39f2bb3)

char ssid[WIFI\_SSID\_MAX\_LEN+1]

SSID.

**Definition** wifi\_mgmt.h:635

[wifi\_iface\_status::rssi](structwifi__iface__status.md#a4e593147b88eb4938d55a4de72fcc7f6)

int rssi

RSSI.

**Definition** wifi\_mgmt.h:651

[wifi\_iface\_status::current\_phy\_rate](structwifi__iface__status.md#a59395eb7671b71135a9affd1b3be4102)

int current\_phy\_rate

The current 802.11 PHY data rate.

**Definition** wifi\_mgmt.h:659

[wifi\_iface\_status::bssid](structwifi__iface__status.md#a5d5d19056a1a15365fbdd94274a0fc5e)

char bssid[WIFI\_MAC\_ADDR\_LEN]

BSSID.

**Definition** wifi\_mgmt.h:637

[wifi\_iface\_status::security](structwifi__iface__status.md#a625ecec1abec8dd65cf155eab21a01b5)

enum wifi\_security\_type security

Security type, see enum wifi\_security\_type.

**Definition** wifi\_mgmt.h:647

[wifi\_iface\_status::channel](structwifi__iface__status.md#a6432663156e5b2c424d254ed1eae0144)

unsigned int channel

Channel.

**Definition** wifi\_mgmt.h:641

[wifi\_iface\_status::mfp](structwifi__iface__status.md#aa1a9b644fd355526125ddd32416b7c24)

enum wifi\_mfp\_options mfp

MFP options, see enum wifi\_mfp\_options.

**Definition** wifi\_mgmt.h:649

[wifi\_iface\_status::dtim\_period](structwifi__iface__status.md#aae6c8cbaa16c81d308f08114d5103a3d)

unsigned char dtim\_period

DTIM period.

**Definition** wifi\_mgmt.h:653

[wifi\_iface\_status::state](structwifi__iface__status.md#ac52806155be3d64954ac6d109e76ec57)

int state

Interface state, see enum wifi\_iface\_state.

**Definition** wifi\_mgmt.h:631

[wifi\_iface\_status::twt\_capable](structwifi__iface__status.md#acfde8d64b463a9f553aa4fb689dc1917)

bool twt\_capable

is TWT capable?

**Definition** wifi\_mgmt.h:657

[wifi\_iface\_status::iface\_mode](structwifi__iface__status.md#ad33d2ec149a8d556e2472dd842ceadc0)

enum wifi\_iface\_mode iface\_mode

Interface mode, see enum wifi\_iface\_mode.

**Definition** wifi\_mgmt.h:643

[wifi\_iface\_status::ssid\_len](structwifi__iface__status.md#ad82f281941e4f6ce1ef0bca008e26d41)

unsigned int ssid\_len

SSID length.

**Definition** wifi\_mgmt.h:633

[wifi\_iface\_status::band](structwifi__iface__status.md#ae1c141a18f4e225af2c22a8cb4f882a8)

enum wifi\_frequency\_bands band

Frequency band.

**Definition** wifi\_mgmt.h:639

[wifi\_iface\_status::link\_mode](structwifi__iface__status.md#ae2de076d79f2172793d65fe9cd31edc4)

enum wifi\_link\_mode link\_mode

Link mode, see enum wifi\_link\_mode.

**Definition** wifi\_mgmt.h:645

[wifi\_mgmt\_ops](structwifi__mgmt__ops.md)

Wi-Fi management API.

**Definition** wifi\_mgmt.h:1206

[wifi\_mgmt\_ops::reg\_domain](structwifi__mgmt__ops.md#a0a287c8acf2d7bf9333b755589294881)

int(\* reg\_domain)(const struct device \*dev, struct wifi\_reg\_domain \*reg\_domain)

Set or get regulatory domain.

**Definition** wifi\_mgmt.h:1333

[wifi\_mgmt\_ops::send\_11k\_neighbor\_request](structwifi__mgmt__ops.md#a1cdd0b76a0a326e968d27c0a3cafcef8)

int(\* send\_11k\_neighbor\_request)(const struct device \*dev, struct wifi\_11k\_params \*params)

Send 11k neighbor request.

**Definition** wifi\_mgmt.h:1301

[wifi\_mgmt\_ops::get\_rts\_threshold](structwifi__mgmt__ops.md#a20706f9eed43b3380258b62fdf93be02)

int(\* get\_rts\_threshold)(const struct device \*dev, unsigned int \*rts\_threshold)

Set Wi-Fi enterprise mode CA/client Cert and key.

**Definition** wifi\_mgmt.h:1441

[wifi\_mgmt\_ops::ap\_config\_params](structwifi__mgmt__ops.md#a2475f32afcce72464b2db6ecad7fb3eb)

int(\* ap\_config\_params)(const struct device \*dev, struct wifi\_ap\_config\_params \*params)

Configure AP parameter.

**Definition** wifi\_mgmt.h:1404

[wifi\_mgmt\_ops::scan](structwifi__mgmt__ops.md#a267030c27da3cdc251badd0ed7f7b1cb)

int(\* scan)(const struct device \*dev, struct wifi\_scan\_params \*params, scan\_result\_cb\_t cb)

Scan for Wi-Fi networks.

**Definition** wifi\_mgmt.h:1218

[wifi\_mgmt\_ops::cfg\_11k](structwifi__mgmt__ops.md#a2cf66093ad850319cf222468e22ff485)

int(\* cfg\_11k)(const struct device \*dev, struct wifi\_11k\_params \*params)

Set or get 11K status.

**Definition** wifi\_mgmt.h:1293

[wifi\_mgmt\_ops::get\_conn\_params](structwifi__mgmt__ops.md#a42c2aa55df30158d8b5d6f4c81e3e2dd)

int(\* get\_conn\_params)(const struct device \*dev, struct wifi\_connect\_req\_params \*params)

Get Wi-Fi connection parameters recently used.

**Definition** wifi\_mgmt.h:1388

[wifi\_mgmt\_ops::start\_11r\_roaming](structwifi__mgmt__ops.md#a501b114298738ac6af9c4a80f5360d79)

int(\* start\_11r\_roaming)(const struct device \*dev)

Start 11r roaming.

**Definition** wifi\_mgmt.h:1464

[wifi\_mgmt\_ops::set\_rts\_threshold](structwifi__mgmt__ops.md#a514e06d63bcf6dc11dba1d3af8d102d5)

int(\* set\_rts\_threshold)(const struct device \*dev, unsigned int rts\_threshold)

Set RTS threshold value.

**Definition** wifi\_mgmt.h:1396

[wifi\_mgmt\_ops::get\_power\_save\_config](structwifi__mgmt__ops.md#a52690b13f8a1e7b0c2302eaa24ae4c7f)

int(\* get\_power\_save\_config)(const struct device \*dev, struct wifi\_ps\_config \*config)

Get power save config.

**Definition** wifi\_mgmt.h:1325

[wifi\_mgmt\_ops::candidate\_scan](structwifi__mgmt__ops.md#a538ffba0a7e045ca9c8ac62ccefc8a36)

int(\* candidate\_scan)(const struct device \*dev, struct wifi\_scan\_params \*params)

Trigger candidate scan.

**Definition** wifi\_mgmt.h:1457

[wifi\_mgmt\_ops::disconnect](structwifi__mgmt__ops.md#a5725c6fd93ae189a3019374cd4ad2ff4)

int(\* disconnect)(const struct device \*dev)

Disconnect from a Wi-Fi network.

**Definition** wifi\_mgmt.h:1236

[wifi\_mgmt\_ops::ap\_disable](structwifi__mgmt__ops.md#a5aa7a2be82eb1783872abda2b8978235)

int(\* ap\_disable)(const struct device \*dev)

Disable AP mode.

**Definition** wifi\_mgmt.h:1252

[wifi\_mgmt\_ops::get\_stats](structwifi__mgmt__ops.md#a5e6fdf836273fcde54efff4c77bfdf0e)

int(\* get\_stats)(const struct device \*dev, struct net\_stats\_wifi \*stats)

Get Wi-Fi statistics.

**Definition** wifi\_mgmt.h:1277

[wifi\_mgmt\_ops::get\_version](structwifi__mgmt__ops.md#aa7e4bc3dbc960091d11ffe5454259885)

int(\* get\_version)(const struct device \*dev, struct wifi\_version \*params)

Get Version of WiFi driver and Firmware.

**Definition** wifi\_mgmt.h:1380

[wifi\_mgmt\_ops::pmksa\_flush](structwifi__mgmt__ops.md#aadf991d6f6725e5c179ca8343d626ad8)

int(\* pmksa\_flush)(const struct device \*dev)

Flush PMKSA cache entries.

**Definition** wifi\_mgmt.h:1422

[wifi\_mgmt\_ops::wps\_config](structwifi__mgmt__ops.md#aaf85f7b56997fb40689b927535af5e85)

int(\* wps\_config)(const struct device \*dev, struct wifi\_wps\_config\_params \*params)

Start a WPS PBC/PIN connection.

**Definition** wifi\_mgmt.h:1449

[wifi\_mgmt\_ops::set\_twt](structwifi__mgmt__ops.md#ab4500534b6abe0449290c8bd8f729fc4)

int(\* set\_twt)(const struct device \*dev, struct wifi\_twt\_params \*params)

Setup or teardown TWT flow.

**Definition** wifi\_mgmt.h:1317

[wifi\_mgmt\_ops::set\_power\_save](structwifi__mgmt__ops.md#ac0f3f7fa699b1bc7db2358e77dd44cc4)

int(\* set\_power\_save)(const struct device \*dev, struct wifi\_ps\_params \*params)

Set power save status.

**Definition** wifi\_mgmt.h:1309

[wifi\_mgmt\_ops::ap\_enable](structwifi__mgmt__ops.md#ac2ce3a4a86c43e30d33261f71c44198a)

int(\* ap\_enable)(const struct device \*dev, struct wifi\_connect\_req\_params \*params)

Enable AP mode.

**Definition** wifi\_mgmt.h:1244

[wifi\_mgmt\_ops::filter](structwifi__mgmt__ops.md#ad645276745ce8dd9685e0744efdfc733)

int(\* filter)(const struct device \*dev, struct wifi\_filter\_info \*filter)

Set or get packet filter settings for monitor and promiscuous modes.

**Definition** wifi\_mgmt.h:1341

[wifi\_mgmt\_ops::iface\_status](structwifi__mgmt__ops.md#adf157476d776bc9c068e99e1a0266fd3)

int(\* iface\_status)(const struct device \*dev, struct wifi\_iface\_status \*status)

Get interface status.

**Definition** wifi\_mgmt.h:1268

[wifi\_mgmt\_ops::mode](structwifi__mgmt__ops.md#ae2fb1bc35bf9255655a30a2ad8588b7c)

int(\* mode)(const struct device \*dev, struct wifi\_mode\_info \*mode)

Set or get mode of operation.

**Definition** wifi\_mgmt.h:1349

[wifi\_mgmt\_ops::connect](structwifi__mgmt__ops.md#ae6255ea77739918797b4f3c7a4634a75)

int(\* connect)(const struct device \*dev, struct wifi\_connect\_req\_params \*params)

Connect to a Wi-Fi network.

**Definition** wifi\_mgmt.h:1228

[wifi\_mgmt\_ops::reset\_stats](structwifi__mgmt__ops.md#ae66901b434ab02863c0d3bd539c4b650)

int(\* reset\_stats)(const struct device \*dev)

Reset Wi-Fi statistics.

**Definition** wifi\_mgmt.h:1284

[wifi\_mgmt\_ops::ap\_sta\_disconnect](structwifi__mgmt__ops.md#af01aaec29be78c02314acf13b5c1b6f7)

int(\* ap\_sta\_disconnect)(const struct device \*dev, const uint8\_t \*mac)

Disconnect a STA from AP.

**Definition** wifi\_mgmt.h:1260

[wifi\_mgmt\_ops::channel](structwifi__mgmt__ops.md#af17ddfea01d0ab478f6fd50b1c9d6015)

int(\* channel)(const struct device \*dev, struct wifi\_channel\_info \*channel)

Set or get current channel of operation.

**Definition** wifi\_mgmt.h:1357

[wifi\_mode\_info](structwifi__mode__info.md)

Wi-Fi mode setup.

**Definition** wifi\_mgmt.h:910

[wifi\_mode\_info::oper](structwifi__mode__info.md#a57c101db8b81ab0ac5dd0a158057a64a)

enum wifi\_mgmt\_op oper

Get or set operation.

**Definition** wifi\_mgmt.h:916

[wifi\_mode\_info::mode](structwifi__mode__info.md#aa29d3b88fc718aa3ac05daf38974707d)

uint8\_t mode

Mode setting for a specific mode of operation.

**Definition** wifi\_mgmt.h:912

[wifi\_mode\_info::if\_index](structwifi__mode__info.md#add58dd3b45fd2ddaf684d1b0de81bef9)

uint8\_t if\_index

Interface index.

**Definition** wifi\_mgmt.h:914

[wifi\_ps\_config](structwifi__ps__config.md)

Wi-Fi power save configuration.

**Definition** wifi\_mgmt.h:801

[wifi\_ps\_config::ps\_params](structwifi__ps__config.md#a357aafc2dedda37755b1cb1fc07fe5a6)

struct wifi\_ps\_params ps\_params

Power save configuration.

**Definition** wifi\_mgmt.h:807

[wifi\_ps\_config::num\_twt\_flows](structwifi__ps__config.md#a9e83c10eaaa1d721cbc49b40aedb00df)

char num\_twt\_flows

Number of TWT flows.

**Definition** wifi\_mgmt.h:803

[wifi\_ps\_config::twt\_flows](structwifi__ps__config.md#ab7460f0f253b2d552e49e98e2c770967)

struct wifi\_twt\_flow\_info twt\_flows[WIFI\_MAX\_TWT\_FLOWS]

TWT flow details.

**Definition** wifi\_mgmt.h:805

[wifi\_ps\_params](structwifi__ps__params.md)

Wi-Fi power save parameters.

**Definition** wifi\_mgmt.h:663

[wifi\_ps\_params::mode](structwifi__ps__params.md#a5a022d89d43ecf2cd1f15fc72c0f2bed)

enum wifi\_ps\_mode mode

Wi-Fi power save mode.

**Definition** wifi\_mgmt.h:671

[wifi\_ps\_params::fail\_reason](structwifi__ps__params.md#a63fa2ee03bc4aefada61c298ee14336c)

enum wifi\_config\_ps\_param\_fail\_reason fail\_reason

Wi-Fi power save fail reason.

**Definition** wifi\_mgmt.h:684

[wifi\_ps\_params::wakeup\_mode](structwifi__ps__params.md#a7cb3e7fb7d9f8bd7c2cab41f879b3b66)

enum wifi\_ps\_wakeup\_mode wakeup\_mode

Wi-Fi power save wakeup mode.

**Definition** wifi\_mgmt.h:669

[wifi\_ps\_params::listen\_interval](structwifi__ps__params.md#a8510c799ab0c5825f1c6349f9799c62f)

unsigned short listen\_interval

Listen interval.

**Definition** wifi\_mgmt.h:667

[wifi\_ps\_params::exit\_strategy](structwifi__ps__params.md#ab9fc62dd1e2928320274fa1554a550a6)

enum wifi\_ps\_exit\_strategy exit\_strategy

Wi-Fi power save exit strategy.

**Definition** wifi\_mgmt.h:686

[wifi\_ps\_params::enabled](structwifi__ps__params.md#abb22aaa45833ac130922204bd2fe841b)

enum wifi\_ps enabled

Power save state.

**Definition** wifi\_mgmt.h:665

[wifi\_ps\_params::timeout\_ms](structwifi__ps__params.md#ad963f1bf78dc271f08b73f3aadb36a91)

unsigned int timeout\_ms

Wi-Fi power save timeout.

**Definition** wifi\_mgmt.h:680

[wifi\_ps\_params::type](structwifi__ps__params.md#aef62e5bf6216bf4dc461efe71735c4bd)

enum wifi\_ps\_param\_type type

Wi-Fi power save type.

**Definition** wifi\_mgmt.h:682

[wifi\_raw\_scan\_result](structwifi__raw__scan__result.md)

Wi-Fi raw scan result.

**Definition** wifi\_mgmt.h:869

[wifi\_raw\_scan\_result::rssi](structwifi__raw__scan__result.md#a3f08580c6448a5fa28dd8a594fa7dad6)

int8\_t rssi

RSSI.

**Definition** wifi\_mgmt.h:871

[wifi\_raw\_scan\_result::data](structwifi__raw__scan__result.md#a5710e89199c147ce898602795f00aba3)

uint8\_t data[CONFIG\_WIFI\_MGMT\_RAW\_SCAN\_RESULT\_LENGTH]

Raw scan data.

**Definition** wifi\_mgmt.h:877

[wifi\_raw\_scan\_result::frame\_length](structwifi__raw__scan__result.md#a876966f469714eb481b42ccc8a63945c)

int frame\_length

Frame length.

**Definition** wifi\_mgmt.h:873

[wifi\_raw\_scan\_result::frequency](structwifi__raw__scan__result.md#aa2c7781882c6775616cbc8016b0842f6)

unsigned short frequency

Frequency.

**Definition** wifi\_mgmt.h:875

[wifi\_reg\_chan\_info](structwifi__reg__chan__info.md)

Per-channel regulatory attributes.

**Definition** wifi\_mgmt.h:832

[wifi\_reg\_chan\_info::center\_frequency](structwifi__reg__chan__info.md#a0addffc11ef29f50c01b700835e59930)

unsigned short center\_frequency

Center frequency in MHz.

**Definition** wifi\_mgmt.h:834

[wifi\_reg\_chan\_info::dfs](structwifi__reg__chan__info.md#a1ab137c142902d2de7d6be2626d7ac1f)

unsigned short dfs

Is a DFS channel.

**Definition** wifi\_mgmt.h:842

[wifi\_reg\_chan\_info::supported](structwifi__reg__chan__info.md#aa044611e18b7332b8577e29f6a769e3f)

unsigned short supported

Is channel supported or not.

**Definition** wifi\_mgmt.h:838

[wifi\_reg\_chan\_info::passive\_only](structwifi__reg__chan__info.md#acc7a88b004c9a61c8bf9ee1a97f85928)

unsigned short passive\_only

Passive transmissions only.

**Definition** wifi\_mgmt.h:840

[wifi\_reg\_chan\_info::max\_power](structwifi__reg__chan__info.md#af9169ab4a41fac4c6f6766fc96799545)

unsigned short max\_power

Maximum transmission power (in dBm).

**Definition** wifi\_mgmt.h:836

[wifi\_reg\_domain](structwifi__reg__domain.md)

Regulatory domain information or configuration.

**Definition** wifi\_mgmt.h:846

[wifi\_reg\_domain::num\_channels](structwifi__reg__domain.md#a3278e9f43893f49ab9f9d0d7f24009c1)

unsigned int num\_channels

Number of channels supported.

**Definition** wifi\_mgmt.h:854

[wifi\_reg\_domain::oper](structwifi__reg__domain.md#a3bbfdf1497a87bbb6b6211c7035e1002)

enum wifi\_mgmt\_op oper

Regulatory domain operation.

**Definition** wifi\_mgmt.h:848

[wifi\_reg\_domain::chan\_info](structwifi__reg__domain.md#a4c8c9c11e41123cd7738fdb0d33ae5fb)

struct wifi\_reg\_chan\_info \* chan\_info

Channels information.

**Definition** wifi\_mgmt.h:856

[wifi\_reg\_domain::force](structwifi__reg__domain.md#a567c6fcae8032567aea83c18cd211c33)

bool force

Ignore all other regulatory hints over this one.

**Definition** wifi\_mgmt.h:850

[wifi\_reg\_domain::country\_code](structwifi__reg__domain.md#abf191495814c227fbbfaccb2f727762e)

uint8\_t country\_code[WIFI\_COUNTRY\_CODE\_LEN]

Country code: ISO/IEC 3166-1 alpha-2.

**Definition** wifi\_mgmt.h:852

[wifi\_scan\_params](structwifi__scan__params.md)

Wi-Fi scan parameters structure.

**Definition** wifi\_mgmt.h:424

[wifi\_scan\_params::max\_bss\_cnt](structwifi__scan__params.md#a12d5dea7d8fa8ad03ac2366720c46243)

uint16\_t max\_bss\_cnt

Specifies the maximum number of scan results to return.

**Definition** wifi\_mgmt.h:453

[wifi\_scan\_params::dwell\_time\_active](structwifi__scan__params.md#a2453a75c23e04e3572559c0e7199c1b4)

uint16\_t dwell\_time\_active

Active scan dwell time (in ms) on a channel.

**Definition** wifi\_mgmt.h:439

[wifi\_scan\_params::scan\_type](structwifi__scan__params.md#a645acc54603cd4692527c1a028933078)

enum wifi\_scan\_type scan\_type

Scan type, see enum wifi\_scan\_type.

**Definition** wifi\_mgmt.h:432

[wifi\_scan\_params::bands](structwifi__scan__params.md#a6b571d960ed9d7419e31530e5fb6f97a)

uint8\_t bands

Bitmap of bands to be scanned.

**Definition** wifi\_mgmt.h:436

[wifi\_scan\_params::dwell\_time\_passive](structwifi__scan__params.md#a8e7a37ccda8de635e7b7066d7943e814)

uint16\_t dwell\_time\_passive

Passive scan dwell time (in ms) on a channel.

**Definition** wifi\_mgmt.h:442

[wifi\_scan\_params::band\_chan](structwifi__scan__params.md#aa5ddbd6bc97b7598288d4b0d38521681)

struct wifi\_band\_channel band\_chan[WIFI\_MGMT\_SCAN\_CHAN\_MAX\_MANUAL]

Channel information array indexed on Wi-Fi frequency bands and channels within that band.

**Definition** wifi\_mgmt.h:468

[wifi\_scan\_params::ssids](structwifi__scan__params.md#aac11ee8e0ec8a4fa24668f4820bd1a12)

const char \* ssids[WIFI\_MGMT\_SCAN\_SSID\_FILT\_MAX]

Array of SSID strings to scan.

**Definition** wifi\_mgmt.h:445

[wifi\_scan\_result](structwifi__scan__result.md)

Wi-Fi scan result, each result is provided to the net\_mgmt\_event\_callback via its info attribute (see...

**Definition** wifi\_mgmt.h:474

[wifi\_scan\_result::ssid\_length](structwifi__scan__result.md#a2c1c2f4265b914df08fc75deb8b69d39)

uint8\_t ssid\_length

SSID length.

**Definition** wifi\_mgmt.h:478

[wifi\_scan\_result::band](structwifi__scan__result.md#a38201c9dd798dc11b5bda3ce97b02e92)

uint8\_t band

Frequency band.

**Definition** wifi\_mgmt.h:480

[wifi\_scan\_result::mac](structwifi__scan__result.md#a4fdbc4dc4d5c8b279223e8c06624f434)

uint8\_t mac[WIFI\_MAC\_ADDR\_LEN]

BSSID.

**Definition** wifi\_mgmt.h:490

[wifi\_scan\_result::rssi](structwifi__scan__result.md#a76aa012136e3721fd4a482a22b93546f)

int8\_t rssi

RSSI.

**Definition** wifi\_mgmt.h:488

[wifi\_scan\_result::mac\_length](structwifi__scan__result.md#a8fca0dabec00ebd7ed4800098ec9d451)

uint8\_t mac\_length

BSSID length.

**Definition** wifi\_mgmt.h:492

[wifi\_scan\_result::ssid](structwifi__scan__result.md#aaefb8f5c9510e4f5002ae306d853ade8)

uint8\_t ssid[WIFI\_SSID\_MAX\_LEN+1]

SSID.

**Definition** wifi\_mgmt.h:476

[wifi\_scan\_result::mfp](structwifi__scan__result.md#acaa3fb30ebf6df22bfac6380698ed28e)

enum wifi\_mfp\_options mfp

MFP options.

**Definition** wifi\_mgmt.h:486

[wifi\_scan\_result::channel](structwifi__scan__result.md#adbbfd7692ee5ffd6344fe78b9d91c840)

uint8\_t channel

Channel.

**Definition** wifi\_mgmt.h:482

[wifi\_scan\_result::security](structwifi__scan__result.md#af2d3dc5d115e3db76d3bc115510b0a5a)

enum wifi\_security\_type security

Security type.

**Definition** wifi\_mgmt.h:484

[wifi\_status](structwifi__status.md)

Generic Wi-Fi status for commands and events.

**Definition** wifi\_mgmt.h:615

[wifi\_status::ap\_status](structwifi__status.md#a02f0fcc7ef57661ca95d0c99f045aef1)

enum wifi\_ap\_status ap\_status

Access point status.

**Definition** wifi\_mgmt.h:624

[wifi\_status::conn\_status](structwifi__status.md#a8f885e78366d0499e4ba8e15bef275ac)

enum wifi\_conn\_status conn\_status

Connection status.

**Definition** wifi\_mgmt.h:620

[wifi\_status::disconn\_reason](structwifi__status.md#aa04b5033d93274badd27f702af9830bc)

enum wifi\_disconn\_reason disconn\_reason

Disconnection reason status.

**Definition** wifi\_mgmt.h:622

[wifi\_status::status](structwifi__status.md#aa1dbff8154400f8353693d387977008b)

int status

Status value.

**Definition** wifi\_mgmt.h:618

[wifi\_twt\_flow\_info](structwifi__twt__flow__info.md)

Wi-Fi TWT flow information.

**Definition** wifi\_mgmt.h:749

[wifi\_twt\_flow\_info::dialog\_token](structwifi__twt__flow__info.md#a123ce10bed8b62b01919a7ea7644a0ba)

uint8\_t dialog\_token

Dialog token, used to map requests to responses.

**Definition** wifi\_mgmt.h:753

[wifi\_twt\_flow\_info::negotiation\_type](structwifi__twt__flow__info.md#a620ae8ba546e4091d74280cb1553b2cf)

enum wifi\_twt\_negotiation\_type negotiation\_type

TWT negotiation type, see enum wifi\_twt\_negotiation\_type.

**Definition** wifi\_mgmt.h:757

[wifi\_twt\_flow\_info::twt\_wake\_ahead\_duration](structwifi__twt__flow__info.md#a6384d3829d54a58a53eafcb74c64a658)

uint32\_t twt\_wake\_ahead\_duration

Wake ahead duration.

**Definition** wifi\_mgmt.h:769

[wifi\_twt\_flow\_info::trigger](structwifi__twt__flow__info.md#a952a67bd092c5dadba387bb13449c6f3)

bool trigger

Trigger enabled or disabled.

**Definition** wifi\_mgmt.h:761

[wifi\_twt\_flow\_info::responder](structwifi__twt__flow__info.md#ac82e4de8ffc82f851061f8ba8d217dc1)

bool responder

Requestor or responder.

**Definition** wifi\_mgmt.h:759

[wifi\_twt\_flow\_info::flow\_id](structwifi__twt__flow__info.md#acb0c618f1cebcb172f342cfe222683be)

uint8\_t flow\_id

Flow ID, used to map setup with teardown.

**Definition** wifi\_mgmt.h:755

[wifi\_twt\_flow\_info::twt\_interval](structwifi__twt__flow__info.md#ae15ba49fa54f82cc6a1fb0d4572114b7)

uint64\_t twt\_interval

Interval = Wake up time + Sleeping time.

**Definition** wifi\_mgmt.h:751

[wifi\_twt\_flow\_info::twt\_wake\_interval](structwifi__twt__flow__info.md#aede6cb0cfc999fac8ded49e2981a3762)

uint32\_t twt\_wake\_interval

Wake up time.

**Definition** wifi\_mgmt.h:767

[wifi\_twt\_flow\_info::implicit](structwifi__twt__flow__info.md#afb480be82d1c6f351bd634fd83bfa5c7)

bool implicit

Implicit or explicit.

**Definition** wifi\_mgmt.h:763

[wifi\_twt\_flow\_info::announce](structwifi__twt__flow__info.md#afc81a5111c265fd9bb2aca5f9510bfa8)

bool announce

Announced or unannounced.

**Definition** wifi\_mgmt.h:765

[wifi\_twt\_params](structwifi__twt__params.md)

Wi-Fi TWT parameters.

**Definition** wifi\_mgmt.h:690

[wifi\_twt\_params::announce](structwifi__twt__params.md#a02f2d822d530e5376f256503439a54f9)

bool announce

Announced or unannounced.

**Definition** wifi\_mgmt.h:717

[wifi\_twt\_params::teardown\_all](structwifi__twt__params.md#a26d6bda00452f77832f69f4465c13efb)

bool teardown\_all

Teardown all flows.

**Definition** wifi\_mgmt.h:730

[wifi\_twt\_params::setup\_cmd](structwifi__twt__params.md#a347f8cff73ee6b6ba6d15ddf6f376a2d)

enum wifi\_twt\_setup\_cmd setup\_cmd

TWT setup command, see enum wifi\_twt\_setup\_cmd.

**Definition** wifi\_mgmt.h:696

[wifi\_twt\_params::trigger](structwifi__twt__params.md#a4e822c04b52fe6a9489e48e26b8f9382)

bool trigger

Trigger enabled or disabled.

**Definition** wifi\_mgmt.h:713

[wifi\_twt\_params::negotiation\_type](structwifi__twt__params.md#a5fd269328f68838b8a7e3a0b93eed894)

enum wifi\_twt\_negotiation\_type negotiation\_type

TWT negotiation type, see enum wifi\_twt\_negotiation\_type.

**Definition** wifi\_mgmt.h:694

[wifi\_twt\_params::operation](structwifi__twt__params.md#a6f0483861a387651c9c89ba182e064bd)

enum wifi\_twt\_operation operation

TWT operation, see enum wifi\_twt\_operation.

**Definition** wifi\_mgmt.h:692

[wifi\_twt\_params::twt\_wake\_ahead\_duration](structwifi__twt__params.md#a6f907ca412251fdd7391f29bfa6d7713)

uint32\_t twt\_wake\_ahead\_duration

Wake ahead notification is sent earlier than TWT Service period (SP) start based on this duration.

**Definition** wifi\_mgmt.h:725

[wifi\_twt\_params::fail\_reason](structwifi__twt__params.md#a70f58b502bb67ef3b2068ded2160b612)

enum wifi\_twt\_fail\_reason fail\_reason

TWT fail reason, see enum wifi\_twt\_fail\_reason.

**Definition** wifi\_mgmt.h:734

[wifi\_twt\_params::twt\_wake\_interval](structwifi__twt__params.md#a7c297459a17ed2fd232c62cca63e952f)

uint32\_t twt\_wake\_interval

Wake up time.

**Definition** wifi\_mgmt.h:719

[wifi\_twt\_params::resp\_status](structwifi__twt__params.md#a805a23284ed4afa46b84efcd43329beb)

enum wifi\_twt\_setup\_resp\_status resp\_status

TWT setup response status, see enum wifi\_twt\_setup\_resp\_status.

**Definition** wifi\_mgmt.h:698

[wifi\_twt\_params::implicit](structwifi__twt__params.md#a8ea1e2501c8b69dc3fa606eb360f8678)

bool implicit

Implicit or explicit.

**Definition** wifi\_mgmt.h:715

[wifi\_twt\_params::flow\_id](structwifi__twt__params.md#a95ec4b32d37309efa47256ae1ea865da)

uint8\_t flow\_id

Flow ID, used to map setup with teardown.

**Definition** wifi\_mgmt.h:704

[wifi\_twt\_params::teardown\_status](structwifi__twt__params.md#a9faff59e577775b3fe53f2139462ac71)

enum wifi\_twt\_teardown\_status teardown\_status

TWT teardown cmd status, see enum wifi\_twt\_teardown\_status.

**Definition** wifi\_mgmt.h:700

[wifi\_twt\_params::twt\_interval](structwifi__twt__params.md#ab92fe571559fcd5d97cdf7e6b7d86681)

uint64\_t twt\_interval

Interval = Wake up time + Sleeping time.

**Definition** wifi\_mgmt.h:709

[wifi\_twt\_params::dialog\_token](structwifi__twt__params.md#adda47e302a87a766f18e28016963a561)

uint8\_t dialog\_token

Dialog token, used to map requests to responses.

**Definition** wifi\_mgmt.h:702

[wifi\_twt\_params::responder](structwifi__twt__params.md#ae547c6fc1c7cbad15bebcfdaa43f59e7)

bool responder

Requestor or responder.

**Definition** wifi\_mgmt.h:711

[wifi\_twt\_params::setup](structwifi__twt__params.md#aee57c0189b210cfcc18e213e35b9479c)

struct wifi\_twt\_params::@302311362167322044106272253111230157111235232263::@007355023165260313375314073015252271352275036053 setup

Setup specific parameters.

[wifi\_twt\_params::teardown](structwifi__twt__params.md#afdeebd8a27107a0e37282aa19e5149d0)

struct wifi\_twt\_params::@302311362167322044106272253111230157111235232263::@053165077055023247316045052326043107125356150312 teardown

Teardown specific parameters.

[wifi\_version](structwifi__version.md)

Wi-Fi version.

**Definition** wifi\_mgmt.h:402

[wifi\_version::fw\_version](structwifi__version.md#a4bf2cbdf5c43ff21718ccf19646c164e)

const char \* fw\_version

Firmware version.

**Definition** wifi\_mgmt.h:406

[wifi\_version::drv\_version](structwifi__version.md#aea828bdb512440d6aa3cc853525c4971)

const char \* drv\_version

Driver version.

**Definition** wifi\_mgmt.h:404

[wifi\_wps\_config\_params](structwifi__wps__config__params.md)

Wi-Fi wps setup.

**Definition** wifi\_mgmt.h:1164

[wifi\_wps\_config\_params::pin](structwifi__wps__config__params.md#a962bd6513c564150e0c75112b96bbe15)

char pin[8+1]

pin value

**Definition** wifi\_mgmt.h:1168

[wifi\_wps\_config\_params::oper](structwifi__wps__config__params.md#aa7a10889c5cd5124983b0f7242d23b7e)

enum wifi\_wps\_op oper

wps operation

**Definition** wifi\_mgmt.h:1166

[wifi.h](wifi_8h.md)

IEEE 802.11 protocol and general Wi-Fi definitions.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [wifi\_mgmt.h](wifi__mgmt_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
