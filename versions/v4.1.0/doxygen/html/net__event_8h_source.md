---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/net__event_8h_source.html
original_path: doxygen/html/net__event_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

net\_event.h

[Go to the documentation of this file.](net__event_8h.md)

1/\*

2 \* Copyright (c) 2016 Intel Corporation.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

11

12#ifndef ZEPHYR\_INCLUDE\_NET\_NET\_EVENT\_H\_

13#define ZEPHYR\_INCLUDE\_NET\_NET\_EVENT\_H\_

14

15#include <[zephyr/net/net\_ip.h](net__ip_8h.md)>

16#include <[zephyr/net/hostname.h](hostname_8h.md)>

17

18#ifdef \_\_cplusplus

19extern "C" {

20#endif

21

26

28

29/\* Network Interface events \*/

30#define \_NET\_IF\_LAYER NET\_MGMT\_LAYER\_L2

31#define \_NET\_IF\_CORE\_CODE 0x001

32#define \_NET\_EVENT\_IF\_BASE (NET\_MGMT\_EVENT\_BIT | \

33 NET\_MGMT\_IFACE\_BIT | \

34 NET\_MGMT\_LAYER(\_NET\_IF\_LAYER) | \

35 NET\_MGMT\_LAYER\_CODE(\_NET\_IF\_CORE\_CODE))

36

37enum net\_event\_if\_cmd {

38 NET\_EVENT\_IF\_CMD\_DOWN = 1,

39 NET\_EVENT\_IF\_CMD\_UP,

40 NET\_EVENT\_IF\_CMD\_ADMIN\_DOWN,

41 NET\_EVENT\_IF\_CMD\_ADMIN\_UP,

42};

43

44/\* IPv6 Events \*/

45#define \_NET\_IPV6\_LAYER NET\_MGMT\_LAYER\_L3

46#define \_NET\_IPV6\_CORE\_CODE 0x060

47#define \_NET\_EVENT\_IPV6\_BASE (NET\_MGMT\_EVENT\_BIT | \

48 NET\_MGMT\_IFACE\_BIT | \

49 NET\_MGMT\_LAYER(\_NET\_IPV6\_LAYER) | \

50 NET\_MGMT\_LAYER\_CODE(\_NET\_IPV6\_CORE\_CODE))

51

52enum net\_event\_ipv6\_cmd {

53 NET\_EVENT\_IPV6\_CMD\_ADDR\_ADD = 1,

54 NET\_EVENT\_IPV6\_CMD\_ADDR\_DEL,

55 NET\_EVENT\_IPV6\_CMD\_MADDR\_ADD,

56 NET\_EVENT\_IPV6\_CMD\_MADDR\_DEL,

57 NET\_EVENT\_IPV6\_CMD\_PREFIX\_ADD,

58 NET\_EVENT\_IPV6\_CMD\_PREFIX\_DEL,

59 NET\_EVENT\_IPV6\_CMD\_MCAST\_JOIN,

60 NET\_EVENT\_IPV6\_CMD\_MCAST\_LEAVE,

61 NET\_EVENT\_IPV6\_CMD\_ROUTER\_ADD,

62 NET\_EVENT\_IPV6\_CMD\_ROUTER\_DEL,

63 NET\_EVENT\_IPV6\_CMD\_ROUTE\_ADD,

64 NET\_EVENT\_IPV6\_CMD\_ROUTE\_DEL,

65 NET\_EVENT\_IPV6\_CMD\_DAD\_SUCCEED,

66 NET\_EVENT\_IPV6\_CMD\_DAD\_FAILED,

67 NET\_EVENT\_IPV6\_CMD\_NBR\_ADD,

68 NET\_EVENT\_IPV6\_CMD\_NBR\_DEL,

69 NET\_EVENT\_IPV6\_CMD\_DHCP\_START,

70 NET\_EVENT\_IPV6\_CMD\_DHCP\_BOUND,

71 NET\_EVENT\_IPV6\_CMD\_DHCP\_STOP,

72 NET\_EVENT\_IPV6\_CMD\_ADDR\_DEPRECATED,

73 NET\_EVENT\_IPV6\_CMD\_PE\_ENABLED,

74 NET\_EVENT\_IPV6\_CMD\_PE\_DISABLED,

75 NET\_EVENT\_IPV6\_CMD\_PE\_FILTER\_ADD,

76 NET\_EVENT\_IPV6\_CMD\_PE\_FILTER\_DEL,

77 NET\_EVENT\_IPV6\_CMD\_PMTU\_CHANGED,

78};

79

80/\* IPv4 Events\*/

81#define \_NET\_IPV4\_LAYER NET\_MGMT\_LAYER\_L3

82#define \_NET\_IPV4\_CORE\_CODE 0x004

83#define \_NET\_EVENT\_IPV4\_BASE (NET\_MGMT\_EVENT\_BIT | \

84 NET\_MGMT\_IFACE\_BIT | \

85 NET\_MGMT\_LAYER(\_NET\_IPV4\_LAYER) | \

86 NET\_MGMT\_LAYER\_CODE(\_NET\_IPV4\_CORE\_CODE))

87

88enum net\_event\_ipv4\_cmd {

89 NET\_EVENT\_IPV4\_CMD\_ADDR\_ADD = 1,

90 NET\_EVENT\_IPV4\_CMD\_ADDR\_DEL,

91 NET\_EVENT\_IPV4\_CMD\_MADDR\_ADD,

92 NET\_EVENT\_IPV4\_CMD\_MADDR\_DEL,

93 NET\_EVENT\_IPV4\_CMD\_ROUTER\_ADD,

94 NET\_EVENT\_IPV4\_CMD\_ROUTER\_DEL,

95 NET\_EVENT\_IPV4\_CMD\_DHCP\_START,

96 NET\_EVENT\_IPV4\_CMD\_DHCP\_BOUND,

97 NET\_EVENT\_IPV4\_CMD\_DHCP\_STOP,

98 NET\_EVENT\_IPV4\_CMD\_MCAST\_JOIN,

99 NET\_EVENT\_IPV4\_CMD\_MCAST\_LEAVE,

100 NET\_EVENT\_IPV4\_CMD\_ACD\_SUCCEED,

101 NET\_EVENT\_IPV4\_CMD\_ACD\_FAILED,

102 NET\_EVENT\_IPV4\_CMD\_ACD\_CONFLICT,

103 NET\_EVENT\_IPV4\_CMD\_PMTU\_CHANGED,

104};

105

106/\* L4 network events \*/

107#define \_NET\_L4\_LAYER NET\_MGMT\_LAYER\_L4

108#define \_NET\_L4\_CORE\_CODE 0x114

109#define \_NET\_EVENT\_L4\_BASE (NET\_MGMT\_EVENT\_BIT | \

110 NET\_MGMT\_IFACE\_BIT | \

111 NET\_MGMT\_LAYER(\_NET\_L4\_LAYER) | \

112 NET\_MGMT\_LAYER\_CODE(\_NET\_L4\_CORE\_CODE))

113

114enum net\_event\_l4\_cmd {

115 NET\_EVENT\_L4\_CMD\_CONNECTED = 1,

116 NET\_EVENT\_L4\_CMD\_DISCONNECTED,

117 NET\_EVENT\_L4\_CMD\_IPV4\_CONNECTED,

118 NET\_EVENT\_L4\_CMD\_IPV4\_DISCONNECTED,

119 NET\_EVENT\_L4\_CMD\_IPV6\_CONNECTED,

120 NET\_EVENT\_L4\_CMD\_IPV6\_DISCONNECTED,

121 NET\_EVENT\_L4\_CMD\_DNS\_SERVER\_ADD,

122 NET\_EVENT\_L4\_CMD\_DNS\_SERVER\_DEL,

123 NET\_EVENT\_L4\_CMD\_HOSTNAME\_CHANGED,

124 NET\_EVENT\_L4\_CMD\_CAPTURE\_STARTED,

125 NET\_EVENT\_L4\_CMD\_CAPTURE\_STOPPED,

126};

127

129

[ 131](group__net__mgmt.md#gac43a928bce3feb217b37ff7eb205e71b)#define NET\_EVENT\_IF\_DOWN \

132 (\_NET\_EVENT\_IF\_BASE | NET\_EVENT\_IF\_CMD\_DOWN)

133

[ 135](group__net__mgmt.md#gaddc84a60607bb27048397e29eb9107f5)#define NET\_EVENT\_IF\_UP \

136 (\_NET\_EVENT\_IF\_BASE | NET\_EVENT\_IF\_CMD\_UP)

137

[ 139](group__net__mgmt.md#gacb6ac7a4579be883abc9aa638299b0cd)#define NET\_EVENT\_IF\_ADMIN\_DOWN \

140 (\_NET\_EVENT\_IF\_BASE | NET\_EVENT\_IF\_CMD\_ADMIN\_DOWN)

141

[ 143](group__net__mgmt.md#ga94a52eb94cc2189919ade9c8c8f239bd)#define NET\_EVENT\_IF\_ADMIN\_UP \

144 (\_NET\_EVENT\_IF\_BASE | NET\_EVENT\_IF\_CMD\_ADMIN\_UP)

145

[ 147](group__net__mgmt.md#ga20125c6148169a91fbebab1ebba17be3)#define NET\_EVENT\_IPV6\_ADDR\_ADD \

148 (\_NET\_EVENT\_IPV6\_BASE | NET\_EVENT\_IPV6\_CMD\_ADDR\_ADD)

149

[ 151](group__net__mgmt.md#ga61f243efbc25928815ec78305b4f000e)#define NET\_EVENT\_IPV6\_ADDR\_DEL \

152 (\_NET\_EVENT\_IPV6\_BASE | NET\_EVENT\_IPV6\_CMD\_ADDR\_DEL)

153

[ 155](group__net__mgmt.md#gadda9dccf913a4dcb4d12b2b1fe5d403c)#define NET\_EVENT\_IPV6\_MADDR\_ADD \

156 (\_NET\_EVENT\_IPV6\_BASE | NET\_EVENT\_IPV6\_CMD\_MADDR\_ADD)

157

[ 159](group__net__mgmt.md#ga035db32f66effd2407e0cca4b1fd9ea3)#define NET\_EVENT\_IPV6\_MADDR\_DEL \

160 (\_NET\_EVENT\_IPV6\_BASE | NET\_EVENT\_IPV6\_CMD\_MADDR\_DEL)

161

[ 163](group__net__mgmt.md#ga392414b95838bca1e55e4342870a8333)#define NET\_EVENT\_IPV6\_PREFIX\_ADD \

164 (\_NET\_EVENT\_IPV6\_BASE | NET\_EVENT\_IPV6\_CMD\_PREFIX\_ADD)

165

[ 167](group__net__mgmt.md#gab06f93335938a635966e85a18b5b0cf6)#define NET\_EVENT\_IPV6\_PREFIX\_DEL \

168 (\_NET\_EVENT\_IPV6\_BASE | NET\_EVENT\_IPV6\_CMD\_PREFIX\_DEL)

169

[ 171](group__net__mgmt.md#ga287d37bae2d74e0c85de59c5e23d409a)#define NET\_EVENT\_IPV6\_MCAST\_JOIN \

172 (\_NET\_EVENT\_IPV6\_BASE | NET\_EVENT\_IPV6\_CMD\_MCAST\_JOIN)

173

[ 175](group__net__mgmt.md#ga862d1b2ce9b65c0806ef77909364a58d)#define NET\_EVENT\_IPV6\_MCAST\_LEAVE \

176 (\_NET\_EVENT\_IPV6\_BASE | NET\_EVENT\_IPV6\_CMD\_MCAST\_LEAVE)

177

[ 179](group__net__mgmt.md#gaae932293528aa40127a906c3dbd45e31)#define NET\_EVENT\_IPV6\_ROUTER\_ADD \

180 (\_NET\_EVENT\_IPV6\_BASE | NET\_EVENT\_IPV6\_CMD\_ROUTER\_ADD)

181

[ 183](group__net__mgmt.md#ga8d4b7798981aaaf3aea2b793739143b7)#define NET\_EVENT\_IPV6\_ROUTER\_DEL \

184 (\_NET\_EVENT\_IPV6\_BASE | NET\_EVENT\_IPV6\_CMD\_ROUTER\_DEL)

185

[ 187](group__net__mgmt.md#gad19b5e742ded9b3ed673d8f7985100fd)#define NET\_EVENT\_IPV6\_ROUTE\_ADD \

188 (\_NET\_EVENT\_IPV6\_BASE | NET\_EVENT\_IPV6\_CMD\_ROUTE\_ADD)

189

[ 191](group__net__mgmt.md#gae6f68ec69032ac049f072d6ed164987c)#define NET\_EVENT\_IPV6\_ROUTE\_DEL \

192 (\_NET\_EVENT\_IPV6\_BASE | NET\_EVENT\_IPV6\_CMD\_ROUTE\_DEL)

193

[ 195](group__net__mgmt.md#ga8711b4b1e88c897196b982e4d56968f1)#define NET\_EVENT\_IPV6\_DAD\_SUCCEED \

196 (\_NET\_EVENT\_IPV6\_BASE | NET\_EVENT\_IPV6\_CMD\_DAD\_SUCCEED)

197

[ 199](group__net__mgmt.md#ga0d5013ea3a6fa3bddd5cb182dd616151)#define NET\_EVENT\_IPV6\_DAD\_FAILED \

200 (\_NET\_EVENT\_IPV6\_BASE | NET\_EVENT\_IPV6\_CMD\_DAD\_FAILED)

201

[ 203](group__net__mgmt.md#ga96fe7da048fe4d59435b7337626d4af7)#define NET\_EVENT\_IPV6\_NBR\_ADD \

204 (\_NET\_EVENT\_IPV6\_BASE | NET\_EVENT\_IPV6\_CMD\_NBR\_ADD)

205

[ 207](group__net__mgmt.md#ga5be1cdfeb1b8da485b1042a7b2dc14e4)#define NET\_EVENT\_IPV6\_NBR\_DEL \

208 (\_NET\_EVENT\_IPV6\_BASE | NET\_EVENT\_IPV6\_CMD\_NBR\_DEL)

209

[ 211](group__net__mgmt.md#gaa07a5e8779ec24e5ab883970bcec6c5e)#define NET\_EVENT\_IPV6\_DHCP\_START \

212 (\_NET\_EVENT\_IPV6\_BASE | NET\_EVENT\_IPV6\_CMD\_DHCP\_START)

213

[ 215](group__net__mgmt.md#gaff89dbc7562a85e9ff073b507bdf06e3)#define NET\_EVENT\_IPV6\_DHCP\_BOUND \

216 (\_NET\_EVENT\_IPV6\_BASE | NET\_EVENT\_IPV6\_CMD\_DHCP\_BOUND)

217

[ 219](group__net__mgmt.md#gaab05d5a65ef5f9ed147e32ce380f7de4)#define NET\_EVENT\_IPV6\_DHCP\_STOP \

220 (\_NET\_EVENT\_IPV6\_BASE | NET\_EVENT\_IPV6\_CMD\_DHCP\_STOP)

221

[ 223](group__net__mgmt.md#ga6cc42e3ca8197e46809de6082602ab98)#define NET\_EVENT\_IPV6\_ADDR\_DEPRECATED \

224 (\_NET\_EVENT\_IPV6\_BASE | NET\_EVENT\_IPV6\_CMD\_ADDR\_DEPRECATED)

225

[ 227](group__net__mgmt.md#ga95f7a737a39fb655d3577405e70e04ba)#define NET\_EVENT\_IPV6\_PE\_ENABLED \

228 (\_NET\_EVENT\_IPV6\_BASE | NET\_EVENT\_IPV6\_CMD\_PE\_ENABLED)

229

[ 231](group__net__mgmt.md#gaba20579e42c4cebc8c3ac9a40ff384f3)#define NET\_EVENT\_IPV6\_PE\_DISABLED \

232 (\_NET\_EVENT\_IPV6\_BASE | NET\_EVENT\_IPV6\_CMD\_PE\_DISABLED)

233

[ 235](group__net__mgmt.md#ga19d671971cf07e76580db8098ab32971)#define NET\_EVENT\_IPV6\_PE\_FILTER\_ADD \

236 (\_NET\_EVENT\_IPV6\_BASE | NET\_EVENT\_IPV6\_CMD\_PE\_FILTER\_ADD)

237

[ 239](group__net__mgmt.md#gaf2f1c4b8dc5b9b07985265cee6a90f70)#define NET\_EVENT\_IPV6\_PE\_FILTER\_DEL \

240 (\_NET\_EVENT\_IPV6\_BASE | NET\_EVENT\_IPV6\_CMD\_PE\_FILTER\_DEL)

241

[ 243](group__net__mgmt.md#gae0e1924aa8c8f6dc47582883528df185)#define NET\_EVENT\_IPV6\_PMTU\_CHANGED \

244 (\_NET\_EVENT\_IPV6\_BASE | NET\_EVENT\_IPV6\_CMD\_PMTU\_CHANGED)

245

[ 247](group__net__mgmt.md#gad422365df617ce1473412908738048f0)#define NET\_EVENT\_IPV4\_ADDR\_ADD \

248 (\_NET\_EVENT\_IPV4\_BASE | NET\_EVENT\_IPV4\_CMD\_ADDR\_ADD)

249

[ 251](group__net__mgmt.md#ga0d78644f799d1d8f5c18ec9860582817)#define NET\_EVENT\_IPV4\_ADDR\_DEL \

252 (\_NET\_EVENT\_IPV4\_BASE | NET\_EVENT\_IPV4\_CMD\_ADDR\_DEL)

253

[ 255](group__net__mgmt.md#ga854e897d09eecccc83d04d86fbba5b64)#define NET\_EVENT\_IPV4\_MADDR\_ADD \

256 (\_NET\_EVENT\_IPV4\_BASE | NET\_EVENT\_IPV4\_CMD\_MADDR\_ADD)

257

[ 259](group__net__mgmt.md#ga303824277664ee64674b7c93ff865bb4)#define NET\_EVENT\_IPV4\_MADDR\_DEL \

260 (\_NET\_EVENT\_IPV4\_BASE | NET\_EVENT\_IPV4\_CMD\_MADDR\_DEL)

261

[ 263](group__net__mgmt.md#ga740c97a7e94181ad734888bbe7b0a3d0)#define NET\_EVENT\_IPV4\_ROUTER\_ADD \

264 (\_NET\_EVENT\_IPV4\_BASE | NET\_EVENT\_IPV4\_CMD\_ROUTER\_ADD)

265

[ 267](group__net__mgmt.md#gae45a3b6a5f4b72edc51e06a22b88239a)#define NET\_EVENT\_IPV4\_ROUTER\_DEL \

268 (\_NET\_EVENT\_IPV4\_BASE | NET\_EVENT\_IPV4\_CMD\_ROUTER\_DEL)

269

[ 271](group__net__mgmt.md#ga2d3a9351c226b1542d1b2f469b77233a)#define NET\_EVENT\_IPV4\_DHCP\_START \

272 (\_NET\_EVENT\_IPV4\_BASE | NET\_EVENT\_IPV4\_CMD\_DHCP\_START)

273

[ 275](group__net__mgmt.md#ga7461ef85f4f8433851cb7583468c00cb)#define NET\_EVENT\_IPV4\_DHCP\_BOUND \

276 (\_NET\_EVENT\_IPV4\_BASE | NET\_EVENT\_IPV4\_CMD\_DHCP\_BOUND)

277

[ 279](group__net__mgmt.md#gabc06b6010780ab2d1e4f88227965b4e7)#define NET\_EVENT\_IPV4\_DHCP\_STOP \

280 (\_NET\_EVENT\_IPV4\_BASE | NET\_EVENT\_IPV4\_CMD\_DHCP\_STOP)

281

[ 283](group__net__mgmt.md#ga17ad57d81f3046555f94f75dc6d31ec1)#define NET\_EVENT\_IPV4\_MCAST\_JOIN \

284 (\_NET\_EVENT\_IPV4\_BASE | NET\_EVENT\_IPV4\_CMD\_MCAST\_JOIN)

285

[ 287](group__net__mgmt.md#ga3cbb8a9dfec8435b93d908171ab944c9)#define NET\_EVENT\_IPV4\_MCAST\_LEAVE \

288 (\_NET\_EVENT\_IPV4\_BASE | NET\_EVENT\_IPV4\_CMD\_MCAST\_LEAVE)

289

[ 291](group__net__mgmt.md#ga5293377de1fdc79e7564f4e5104a07c2)#define NET\_EVENT\_IPV4\_ACD\_SUCCEED \

292 (\_NET\_EVENT\_IPV4\_BASE | NET\_EVENT\_IPV4\_CMD\_ACD\_SUCCEED)

293

[ 295](group__net__mgmt.md#ga3de741f5732473a1f49d9d0b93183549)#define NET\_EVENT\_IPV4\_ACD\_FAILED \

296 (\_NET\_EVENT\_IPV4\_BASE | NET\_EVENT\_IPV4\_CMD\_ACD\_FAILED)

297

[ 302](group__net__mgmt.md#ga9af1f8f4ba965e6d6e82a190ab4748a1)#define NET\_EVENT\_IPV4\_ACD\_CONFLICT \

303 (\_NET\_EVENT\_IPV4\_BASE | NET\_EVENT\_IPV4\_CMD\_ACD\_CONFLICT)

304

[ 306](group__net__mgmt.md#ga24766ef249022c198299d38e95f400b9)#define NET\_EVENT\_IPV4\_PMTU\_CHANGED \

307 (\_NET\_EVENT\_IPV4\_BASE | NET\_EVENT\_IPV4\_CMD\_PMTU\_CHANGED)

308

[ 313](group__net__mgmt.md#gacbd2b10cc345359c07de4a62eb172a09)#define NET\_EVENT\_L4\_CONNECTED \

314 (\_NET\_EVENT\_L4\_BASE | NET\_EVENT\_L4\_CMD\_CONNECTED)

315

[ 321](group__net__mgmt.md#gacd9e0b5e2f540794b20f11b070ffbd65)#define NET\_EVENT\_L4\_DISCONNECTED \

322 (\_NET\_EVENT\_L4\_BASE | NET\_EVENT\_L4\_CMD\_DISCONNECTED)

323

324

[ 326](group__net__mgmt.md#ga532fdc2f199e047a5d17e325cee12cf1)#define NET\_EVENT\_L4\_IPV4\_CONNECTED \

327 (\_NET\_EVENT\_L4\_BASE | NET\_EVENT\_L4\_CMD\_IPV4\_CONNECTED)

328

[ 330](group__net__mgmt.md#gaa92cc806d93446d548a05edb8e0074c2)#define NET\_EVENT\_L4\_IPV4\_DISCONNECTED \

331 (\_NET\_EVENT\_L4\_BASE | NET\_EVENT\_L4\_CMD\_IPV4\_DISCONNECTED)

332

[ 334](group__net__mgmt.md#gaf6bb88ed90df5aacb40e42fcc5bfbcf5)#define NET\_EVENT\_L4\_IPV6\_CONNECTED \

335 (\_NET\_EVENT\_L4\_BASE | NET\_EVENT\_L4\_CMD\_IPV6\_CONNECTED)

336

[ 338](group__net__mgmt.md#gac81abeab44fbf2b6f29d4e11a1e1bd17)#define NET\_EVENT\_L4\_IPV6\_DISCONNECTED \

339 (\_NET\_EVENT\_L4\_BASE | NET\_EVENT\_L4\_CMD\_IPV6\_DISCONNECTED)

340

[ 342](group__net__mgmt.md#ga5735d13f24c974ad6d4038c93edf05e0)#define NET\_EVENT\_DNS\_SERVER\_ADD \

343 (\_NET\_EVENT\_L4\_BASE | NET\_EVENT\_L4\_CMD\_DNS\_SERVER\_ADD)

344

[ 346](group__net__mgmt.md#ga9d406772e5d1ad2952b2a2e0fed05c73)#define NET\_EVENT\_DNS\_SERVER\_DEL \

347 (\_NET\_EVENT\_L4\_BASE | NET\_EVENT\_L4\_CMD\_DNS\_SERVER\_DEL)

348

[ 350](group__net__mgmt.md#gac5a7458d89e4a95564999dca3c1b9f1e)#define NET\_EVENT\_HOSTNAME\_CHANGED \

351 (\_NET\_EVENT\_L4\_BASE | NET\_EVENT\_L4\_CMD\_HOSTNAME\_CHANGED)

352

[ 354](group__net__mgmt.md#gaa89b82a1890c55775f8c3c24e11f40e2)#define NET\_EVENT\_CAPTURE\_STARTED \

355 (\_NET\_EVENT\_L4\_BASE | NET\_EVENT\_L4\_CMD\_CAPTURE\_STARTED)

356

[ 358](group__net__mgmt.md#gaa2b655aedd597636790409539b1f86cd)#define NET\_EVENT\_CAPTURE\_STOPPED \

359 (\_NET\_EVENT\_L4\_BASE | NET\_EVENT\_L4\_CMD\_CAPTURE\_STOPPED)

360

[ 371](structnet__event__ipv6__addr.md)struct [net\_event\_ipv6\_addr](structnet__event__ipv6__addr.md) {

[ 373](structnet__event__ipv6__addr.md#a3cb4dd6d1e33ef2769cd64fa27c69b43) struct [in6\_addr](structin6__addr.md) [addr](structnet__event__ipv6__addr.md#a3cb4dd6d1e33ef2769cd64fa27c69b43);

374};

375

[ 385](structnet__event__ipv6__nbr.md)struct [net\_event\_ipv6\_nbr](structnet__event__ipv6__nbr.md) {

[ 387](structnet__event__ipv6__nbr.md#a75653facd98b568c300395c45191b289) struct [in6\_addr](structin6__addr.md) [addr](structnet__event__ipv6__nbr.md#a75653facd98b568c300395c45191b289);

[ 389](structnet__event__ipv6__nbr.md#adeb139ad70e794d1a805315ffd1fcbee) int [idx](structnet__event__ipv6__nbr.md#adeb139ad70e794d1a805315ffd1fcbee);

390};

391

[ 400](structnet__event__ipv6__route.md)struct [net\_event\_ipv6\_route](structnet__event__ipv6__route.md) {

[ 402](structnet__event__ipv6__route.md#ad8772d7949fa8b7e7217324acbda6829) struct [in6\_addr](structin6__addr.md) [nexthop](structnet__event__ipv6__route.md#ad8772d7949fa8b7e7217324acbda6829);

[ 404](structnet__event__ipv6__route.md#a42bb70c6b92841e5a77c80a3a193178c) struct [in6\_addr](structin6__addr.md) [addr](structnet__event__ipv6__route.md#a42bb70c6b92841e5a77c80a3a193178c);

[ 406](structnet__event__ipv6__route.md#aa1f21f6963befb3f94183d02c6d2d23f) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [prefix\_len](structnet__event__ipv6__route.md#aa1f21f6963befb3f94183d02c6d2d23f);

407};

408

[ 417](structnet__event__ipv6__prefix.md)struct [net\_event\_ipv6\_prefix](structnet__event__ipv6__prefix.md) {

[ 419](structnet__event__ipv6__prefix.md#a5ccae593ce7678fcdd91a4d0eaf142fb) struct [in6\_addr](structin6__addr.md) [addr](structnet__event__ipv6__prefix.md#a5ccae593ce7678fcdd91a4d0eaf142fb);

[ 421](structnet__event__ipv6__prefix.md#a3d70216e13fc0f78e08eb27f34fe8ace) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [len](structnet__event__ipv6__prefix.md#a3d70216e13fc0f78e08eb27f34fe8ace);

[ 423](structnet__event__ipv6__prefix.md#a6d7b0323896e43a04931ece4daaa09c4) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [lifetime](structnet__event__ipv6__prefix.md#a6d7b0323896e43a04931ece4daaa09c4);

424};

425

[ 432](structnet__event__l4__hostname.md)struct [net\_event\_l4\_hostname](structnet__event__l4__hostname.md) {

[ 434](structnet__event__l4__hostname.md#a8e04c33dfb1c251a0deaa29081283245) char [hostname](structnet__event__l4__hostname.md#a8e04c33dfb1c251a0deaa29081283245)[NET\_HOSTNAME\_SIZE];

435};

436

[ 447](structnet__event__ipv6__pe__filter.md)struct [net\_event\_ipv6\_pe\_filter](structnet__event__ipv6__pe__filter.md) {

[ 449](structnet__event__ipv6__pe__filter.md#a2c0b6477f021e32bae98916f74e6affc) struct [in6\_addr](structin6__addr.md) [prefix](structnet__event__ipv6__pe__filter.md#a2c0b6477f021e32bae98916f74e6affc);

[ 451](structnet__event__ipv6__pe__filter.md#a07961a42f5ff8ca98615164192b8ca5a) bool [is\_deny\_list](structnet__event__ipv6__pe__filter.md#a07961a42f5ff8ca98615164192b8ca5a);

452};

453

[ 461](structnet__event__ipv4__pmtu__info.md)struct [net\_event\_ipv4\_pmtu\_info](structnet__event__ipv4__pmtu__info.md) {

[ 463](structnet__event__ipv4__pmtu__info.md#a9779ec9487b5dde4d5df1d0aeef82ebf) struct [in\_addr](structin__addr.md) [dst](structnet__event__ipv4__pmtu__info.md#a9779ec9487b5dde4d5df1d0aeef82ebf);

[ 465](structnet__event__ipv4__pmtu__info.md#ae4f6951aed4253428a7ac4273b8b43fe) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [mtu](structnet__event__ipv4__pmtu__info.md#ae4f6951aed4253428a7ac4273b8b43fe);

466};

467

[ 475](structnet__event__ipv6__pmtu__info.md)struct [net\_event\_ipv6\_pmtu\_info](structnet__event__ipv6__pmtu__info.md) {

[ 477](structnet__event__ipv6__pmtu__info.md#aa9398dc7f56432b7489bcba7e9a6803c) struct [in6\_addr](structin6__addr.md) [dst](structnet__event__ipv6__pmtu__info.md#aa9398dc7f56432b7489bcba7e9a6803c);

[ 479](structnet__event__ipv6__pmtu__info.md#a52e5078e0f39cb5e95d4e5bc42674480) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [mtu](structnet__event__ipv6__pmtu__info.md#a52e5078e0f39cb5e95d4e5bc42674480);

480};

481

482#ifdef \_\_cplusplus

483}

484#endif

485

489

490#endif /\* ZEPHYR\_INCLUDE\_NET\_NET\_EVENT\_H\_ \*/

[hostname.h](hostname_8h.md)

Hostname configuration definitions.

[net\_ip.h](net__ip_8h.md)

IPv6 and IPv4 definitions.

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[in6\_addr](structin6__addr.md)

IPv6 address struct.

**Definition** net\_ip.h:143

[in\_addr](structin__addr.md)

IPv4 address struct.

**Definition** net\_ip.h:155

[net\_event\_ipv4\_pmtu\_info](structnet__event__ipv4__pmtu__info.md)

Network Management event information structure Used to pass information on network event NET\_EVENT\_IP...

**Definition** net\_event.h:461

[net\_event\_ipv4\_pmtu\_info::dst](structnet__event__ipv4__pmtu__info.md#a9779ec9487b5dde4d5df1d0aeef82ebf)

struct in\_addr dst

IPv4 address.

**Definition** net\_event.h:463

[net\_event\_ipv4\_pmtu\_info::mtu](structnet__event__ipv4__pmtu__info.md#ae4f6951aed4253428a7ac4273b8b43fe)

uint16\_t mtu

New MTU.

**Definition** net\_event.h:465

[net\_event\_ipv6\_addr](structnet__event__ipv6__addr.md)

Network Management event information structure Used to pass information on network events like NET\_EV...

**Definition** net\_event.h:371

[net\_event\_ipv6\_addr::addr](structnet__event__ipv6__addr.md#a3cb4dd6d1e33ef2769cd64fa27c69b43)

struct in6\_addr addr

IPv6 address related to this event.

**Definition** net\_event.h:373

[net\_event\_ipv6\_nbr](structnet__event__ipv6__nbr.md)

Network Management event information structure Used to pass information on network events like NET\_EV...

**Definition** net\_event.h:385

[net\_event\_ipv6\_nbr::addr](structnet__event__ipv6__nbr.md#a75653facd98b568c300395c45191b289)

struct in6\_addr addr

Neighbor IPv6 address.

**Definition** net\_event.h:387

[net\_event\_ipv6\_nbr::idx](structnet__event__ipv6__nbr.md#adeb139ad70e794d1a805315ffd1fcbee)

int idx

Neighbor index in cache.

**Definition** net\_event.h:389

[net\_event\_ipv6\_pe\_filter](structnet__event__ipv6__pe__filter.md)

Network Management event information structure Used to pass information on network events like NET\_EV...

**Definition** net\_event.h:447

[net\_event\_ipv6\_pe\_filter::is\_deny\_list](structnet__event__ipv6__pe__filter.md#a07961a42f5ff8ca98615164192b8ca5a)

bool is\_deny\_list

IPv6 filter deny or allow list.

**Definition** net\_event.h:451

[net\_event\_ipv6\_pe\_filter::prefix](structnet__event__ipv6__pe__filter.md#a2c0b6477f021e32bae98916f74e6affc)

struct in6\_addr prefix

IPv6 address of privacy extension filter.

**Definition** net\_event.h:449

[net\_event\_ipv6\_pmtu\_info](structnet__event__ipv6__pmtu__info.md)

Network Management event information structure Used to pass information on network event NET\_EVENT\_IP...

**Definition** net\_event.h:475

[net\_event\_ipv6\_pmtu\_info::mtu](structnet__event__ipv6__pmtu__info.md#a52e5078e0f39cb5e95d4e5bc42674480)

uint32\_t mtu

New MTU.

**Definition** net\_event.h:479

[net\_event\_ipv6\_pmtu\_info::dst](structnet__event__ipv6__pmtu__info.md#aa9398dc7f56432b7489bcba7e9a6803c)

struct in6\_addr dst

IPv6 address.

**Definition** net\_event.h:477

[net\_event\_ipv6\_prefix](structnet__event__ipv6__prefix.md)

Network Management event information structure Used to pass information on network events like NET\_EV...

**Definition** net\_event.h:417

[net\_event\_ipv6\_prefix::len](structnet__event__ipv6__prefix.md#a3d70216e13fc0f78e08eb27f34fe8ace)

uint8\_t len

IPv6 prefix length.

**Definition** net\_event.h:421

[net\_event\_ipv6\_prefix::addr](structnet__event__ipv6__prefix.md#a5ccae593ce7678fcdd91a4d0eaf142fb)

struct in6\_addr addr

IPv6 prefix.

**Definition** net\_event.h:419

[net\_event\_ipv6\_prefix::lifetime](structnet__event__ipv6__prefix.md#a6d7b0323896e43a04931ece4daaa09c4)

uint32\_t lifetime

IPv6 prefix lifetime in seconds.

**Definition** net\_event.h:423

[net\_event\_ipv6\_route](structnet__event__ipv6__route.md)

Network Management event information structure Used to pass information on network events like NET\_EV...

**Definition** net\_event.h:400

[net\_event\_ipv6\_route::addr](structnet__event__ipv6__route.md#a42bb70c6b92841e5a77c80a3a193178c)

struct in6\_addr addr

IPv6 address or prefix of the route.

**Definition** net\_event.h:404

[net\_event\_ipv6\_route::prefix\_len](structnet__event__ipv6__route.md#aa1f21f6963befb3f94183d02c6d2d23f)

uint8\_t prefix\_len

IPv6 prefix length.

**Definition** net\_event.h:406

[net\_event\_ipv6\_route::nexthop](structnet__event__ipv6__route.md#ad8772d7949fa8b7e7217324acbda6829)

struct in6\_addr nexthop

IPv6 address of the next hop.

**Definition** net\_event.h:402

[net\_event\_l4\_hostname](structnet__event__l4__hostname.md)

Network Management event information structure Used to pass information on NET\_EVENT\_HOSTNAME\_CHANGED...

**Definition** net\_event.h:432

[net\_event\_l4\_hostname::hostname](structnet__event__l4__hostname.md#a8e04c33dfb1c251a0deaa29081283245)

char hostname[NET\_HOSTNAME\_SIZE]

New hostname.

**Definition** net\_event.h:434

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [net\_event.h](net__event_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
