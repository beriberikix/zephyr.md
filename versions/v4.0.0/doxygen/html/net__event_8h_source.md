---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/net__event_8h_source.html
original_path: doxygen/html/net__event_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
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

77};

78

79/\* IPv4 Events\*/

80#define \_NET\_IPV4\_LAYER NET\_MGMT\_LAYER\_L3

81#define \_NET\_IPV4\_CORE\_CODE 0x004

82#define \_NET\_EVENT\_IPV4\_BASE (NET\_MGMT\_EVENT\_BIT | \

83 NET\_MGMT\_IFACE\_BIT | \

84 NET\_MGMT\_LAYER(\_NET\_IPV4\_LAYER) | \

85 NET\_MGMT\_LAYER\_CODE(\_NET\_IPV4\_CORE\_CODE))

86

87enum net\_event\_ipv4\_cmd {

88 NET\_EVENT\_IPV4\_CMD\_ADDR\_ADD = 1,

89 NET\_EVENT\_IPV4\_CMD\_ADDR\_DEL,

90 NET\_EVENT\_IPV4\_CMD\_MADDR\_ADD,

91 NET\_EVENT\_IPV4\_CMD\_MADDR\_DEL,

92 NET\_EVENT\_IPV4\_CMD\_ROUTER\_ADD,

93 NET\_EVENT\_IPV4\_CMD\_ROUTER\_DEL,

94 NET\_EVENT\_IPV4\_CMD\_DHCP\_START,

95 NET\_EVENT\_IPV4\_CMD\_DHCP\_BOUND,

96 NET\_EVENT\_IPV4\_CMD\_DHCP\_STOP,

97 NET\_EVENT\_IPV4\_CMD\_MCAST\_JOIN,

98 NET\_EVENT\_IPV4\_CMD\_MCAST\_LEAVE,

99 NET\_EVENT\_IPV4\_CMD\_ACD\_SUCCEED,

100 NET\_EVENT\_IPV4\_CMD\_ACD\_FAILED,

101 NET\_EVENT\_IPV4\_CMD\_ACD\_CONFLICT,

102};

103

104/\* L4 network events \*/

105#define \_NET\_L4\_LAYER NET\_MGMT\_LAYER\_L4

106#define \_NET\_L4\_CORE\_CODE 0x114

107#define \_NET\_EVENT\_L4\_BASE (NET\_MGMT\_EVENT\_BIT | \

108 NET\_MGMT\_IFACE\_BIT | \

109 NET\_MGMT\_LAYER(\_NET\_L4\_LAYER) | \

110 NET\_MGMT\_LAYER\_CODE(\_NET\_L4\_CORE\_CODE))

111

112enum net\_event\_l4\_cmd {

113 NET\_EVENT\_L4\_CMD\_CONNECTED = 1,

114 NET\_EVENT\_L4\_CMD\_DISCONNECTED,

115 NET\_EVENT\_L4\_CMD\_IPV4\_CONNECTED,

116 NET\_EVENT\_L4\_CMD\_IPV4\_DISCONNECTED,

117 NET\_EVENT\_L4\_CMD\_IPV6\_CONNECTED,

118 NET\_EVENT\_L4\_CMD\_IPV6\_DISCONNECTED,

119 NET\_EVENT\_L4\_CMD\_DNS\_SERVER\_ADD,

120 NET\_EVENT\_L4\_CMD\_DNS\_SERVER\_DEL,

121 NET\_EVENT\_L4\_CMD\_HOSTNAME\_CHANGED,

122 NET\_EVENT\_L4\_CMD\_CAPTURE\_STARTED,

123 NET\_EVENT\_L4\_CMD\_CAPTURE\_STOPPED,

124};

125

127

[ 129](group__net__mgmt.md#gac43a928bce3feb217b37ff7eb205e71b)#define NET\_EVENT\_IF\_DOWN \

130 (\_NET\_EVENT\_IF\_BASE | NET\_EVENT\_IF\_CMD\_DOWN)

131

[ 133](group__net__mgmt.md#gaddc84a60607bb27048397e29eb9107f5)#define NET\_EVENT\_IF\_UP \

134 (\_NET\_EVENT\_IF\_BASE | NET\_EVENT\_IF\_CMD\_UP)

135

[ 137](group__net__mgmt.md#gacb6ac7a4579be883abc9aa638299b0cd)#define NET\_EVENT\_IF\_ADMIN\_DOWN \

138 (\_NET\_EVENT\_IF\_BASE | NET\_EVENT\_IF\_CMD\_ADMIN\_DOWN)

139

[ 141](group__net__mgmt.md#ga94a52eb94cc2189919ade9c8c8f239bd)#define NET\_EVENT\_IF\_ADMIN\_UP \

142 (\_NET\_EVENT\_IF\_BASE | NET\_EVENT\_IF\_CMD\_ADMIN\_UP)

143

[ 145](group__net__mgmt.md#ga20125c6148169a91fbebab1ebba17be3)#define NET\_EVENT\_IPV6\_ADDR\_ADD \

146 (\_NET\_EVENT\_IPV6\_BASE | NET\_EVENT\_IPV6\_CMD\_ADDR\_ADD)

147

[ 149](group__net__mgmt.md#ga61f243efbc25928815ec78305b4f000e)#define NET\_EVENT\_IPV6\_ADDR\_DEL \

150 (\_NET\_EVENT\_IPV6\_BASE | NET\_EVENT\_IPV6\_CMD\_ADDR\_DEL)

151

[ 153](group__net__mgmt.md#gadda9dccf913a4dcb4d12b2b1fe5d403c)#define NET\_EVENT\_IPV6\_MADDR\_ADD \

154 (\_NET\_EVENT\_IPV6\_BASE | NET\_EVENT\_IPV6\_CMD\_MADDR\_ADD)

155

[ 157](group__net__mgmt.md#ga035db32f66effd2407e0cca4b1fd9ea3)#define NET\_EVENT\_IPV6\_MADDR\_DEL \

158 (\_NET\_EVENT\_IPV6\_BASE | NET\_EVENT\_IPV6\_CMD\_MADDR\_DEL)

159

[ 161](group__net__mgmt.md#ga392414b95838bca1e55e4342870a8333)#define NET\_EVENT\_IPV6\_PREFIX\_ADD \

162 (\_NET\_EVENT\_IPV6\_BASE | NET\_EVENT\_IPV6\_CMD\_PREFIX\_ADD)

163

[ 165](group__net__mgmt.md#gab06f93335938a635966e85a18b5b0cf6)#define NET\_EVENT\_IPV6\_PREFIX\_DEL \

166 (\_NET\_EVENT\_IPV6\_BASE | NET\_EVENT\_IPV6\_CMD\_PREFIX\_DEL)

167

[ 169](group__net__mgmt.md#ga287d37bae2d74e0c85de59c5e23d409a)#define NET\_EVENT\_IPV6\_MCAST\_JOIN \

170 (\_NET\_EVENT\_IPV6\_BASE | NET\_EVENT\_IPV6\_CMD\_MCAST\_JOIN)

171

[ 173](group__net__mgmt.md#ga862d1b2ce9b65c0806ef77909364a58d)#define NET\_EVENT\_IPV6\_MCAST\_LEAVE \

174 (\_NET\_EVENT\_IPV6\_BASE | NET\_EVENT\_IPV6\_CMD\_MCAST\_LEAVE)

175

[ 177](group__net__mgmt.md#gaae932293528aa40127a906c3dbd45e31)#define NET\_EVENT\_IPV6\_ROUTER\_ADD \

178 (\_NET\_EVENT\_IPV6\_BASE | NET\_EVENT\_IPV6\_CMD\_ROUTER\_ADD)

179

[ 181](group__net__mgmt.md#ga8d4b7798981aaaf3aea2b793739143b7)#define NET\_EVENT\_IPV6\_ROUTER\_DEL \

182 (\_NET\_EVENT\_IPV6\_BASE | NET\_EVENT\_IPV6\_CMD\_ROUTER\_DEL)

183

[ 185](group__net__mgmt.md#gad19b5e742ded9b3ed673d8f7985100fd)#define NET\_EVENT\_IPV6\_ROUTE\_ADD \

186 (\_NET\_EVENT\_IPV6\_BASE | NET\_EVENT\_IPV6\_CMD\_ROUTE\_ADD)

187

[ 189](group__net__mgmt.md#gae6f68ec69032ac049f072d6ed164987c)#define NET\_EVENT\_IPV6\_ROUTE\_DEL \

190 (\_NET\_EVENT\_IPV6\_BASE | NET\_EVENT\_IPV6\_CMD\_ROUTE\_DEL)

191

[ 193](group__net__mgmt.md#ga8711b4b1e88c897196b982e4d56968f1)#define NET\_EVENT\_IPV6\_DAD\_SUCCEED \

194 (\_NET\_EVENT\_IPV6\_BASE | NET\_EVENT\_IPV6\_CMD\_DAD\_SUCCEED)

195

[ 197](group__net__mgmt.md#ga0d5013ea3a6fa3bddd5cb182dd616151)#define NET\_EVENT\_IPV6\_DAD\_FAILED \

198 (\_NET\_EVENT\_IPV6\_BASE | NET\_EVENT\_IPV6\_CMD\_DAD\_FAILED)

199

[ 201](group__net__mgmt.md#ga96fe7da048fe4d59435b7337626d4af7)#define NET\_EVENT\_IPV6\_NBR\_ADD \

202 (\_NET\_EVENT\_IPV6\_BASE | NET\_EVENT\_IPV6\_CMD\_NBR\_ADD)

203

[ 205](group__net__mgmt.md#ga5be1cdfeb1b8da485b1042a7b2dc14e4)#define NET\_EVENT\_IPV6\_NBR\_DEL \

206 (\_NET\_EVENT\_IPV6\_BASE | NET\_EVENT\_IPV6\_CMD\_NBR\_DEL)

207

[ 209](group__net__mgmt.md#gaa07a5e8779ec24e5ab883970bcec6c5e)#define NET\_EVENT\_IPV6\_DHCP\_START \

210 (\_NET\_EVENT\_IPV6\_BASE | NET\_EVENT\_IPV6\_CMD\_DHCP\_START)

211

[ 213](group__net__mgmt.md#gaff89dbc7562a85e9ff073b507bdf06e3)#define NET\_EVENT\_IPV6\_DHCP\_BOUND \

214 (\_NET\_EVENT\_IPV6\_BASE | NET\_EVENT\_IPV6\_CMD\_DHCP\_BOUND)

215

[ 217](group__net__mgmt.md#gaab05d5a65ef5f9ed147e32ce380f7de4)#define NET\_EVENT\_IPV6\_DHCP\_STOP \

218 (\_NET\_EVENT\_IPV6\_BASE | NET\_EVENT\_IPV6\_CMD\_DHCP\_STOP)

219

[ 221](group__net__mgmt.md#ga6cc42e3ca8197e46809de6082602ab98)#define NET\_EVENT\_IPV6\_ADDR\_DEPRECATED \

222 (\_NET\_EVENT\_IPV6\_BASE | NET\_EVENT\_IPV6\_CMD\_ADDR\_DEPRECATED)

223

[ 225](group__net__mgmt.md#ga95f7a737a39fb655d3577405e70e04ba)#define NET\_EVENT\_IPV6\_PE\_ENABLED \

226 (\_NET\_EVENT\_IPV6\_BASE | NET\_EVENT\_IPV6\_CMD\_PE\_ENABLED)

227

[ 229](group__net__mgmt.md#gaba20579e42c4cebc8c3ac9a40ff384f3)#define NET\_EVENT\_IPV6\_PE\_DISABLED \

230 (\_NET\_EVENT\_IPV6\_BASE | NET\_EVENT\_IPV6\_CMD\_PE\_DISABLED)

231

[ 233](group__net__mgmt.md#ga19d671971cf07e76580db8098ab32971)#define NET\_EVENT\_IPV6\_PE\_FILTER\_ADD \

234 (\_NET\_EVENT\_IPV6\_BASE | NET\_EVENT\_IPV6\_CMD\_PE\_FILTER\_ADD)

235

[ 237](group__net__mgmt.md#gaf2f1c4b8dc5b9b07985265cee6a90f70)#define NET\_EVENT\_IPV6\_PE\_FILTER\_DEL \

238 (\_NET\_EVENT\_IPV6\_BASE | NET\_EVENT\_IPV6\_CMD\_PE\_FILTER\_DEL)

239

[ 241](group__net__mgmt.md#gad422365df617ce1473412908738048f0)#define NET\_EVENT\_IPV4\_ADDR\_ADD \

242 (\_NET\_EVENT\_IPV4\_BASE | NET\_EVENT\_IPV4\_CMD\_ADDR\_ADD)

243

[ 245](group__net__mgmt.md#ga0d78644f799d1d8f5c18ec9860582817)#define NET\_EVENT\_IPV4\_ADDR\_DEL \

246 (\_NET\_EVENT\_IPV4\_BASE | NET\_EVENT\_IPV4\_CMD\_ADDR\_DEL)

247

[ 249](group__net__mgmt.md#ga854e897d09eecccc83d04d86fbba5b64)#define NET\_EVENT\_IPV4\_MADDR\_ADD \

250 (\_NET\_EVENT\_IPV4\_BASE | NET\_EVENT\_IPV4\_CMD\_MADDR\_ADD)

251

[ 253](group__net__mgmt.md#ga303824277664ee64674b7c93ff865bb4)#define NET\_EVENT\_IPV4\_MADDR\_DEL \

254 (\_NET\_EVENT\_IPV4\_BASE | NET\_EVENT\_IPV4\_CMD\_MADDR\_DEL)

255

[ 257](group__net__mgmt.md#ga740c97a7e94181ad734888bbe7b0a3d0)#define NET\_EVENT\_IPV4\_ROUTER\_ADD \

258 (\_NET\_EVENT\_IPV4\_BASE | NET\_EVENT\_IPV4\_CMD\_ROUTER\_ADD)

259

[ 261](group__net__mgmt.md#gae45a3b6a5f4b72edc51e06a22b88239a)#define NET\_EVENT\_IPV4\_ROUTER\_DEL \

262 (\_NET\_EVENT\_IPV4\_BASE | NET\_EVENT\_IPV4\_CMD\_ROUTER\_DEL)

263

[ 265](group__net__mgmt.md#ga2d3a9351c226b1542d1b2f469b77233a)#define NET\_EVENT\_IPV4\_DHCP\_START \

266 (\_NET\_EVENT\_IPV4\_BASE | NET\_EVENT\_IPV4\_CMD\_DHCP\_START)

267

[ 269](group__net__mgmt.md#ga7461ef85f4f8433851cb7583468c00cb)#define NET\_EVENT\_IPV4\_DHCP\_BOUND \

270 (\_NET\_EVENT\_IPV4\_BASE | NET\_EVENT\_IPV4\_CMD\_DHCP\_BOUND)

271

[ 273](group__net__mgmt.md#gabc06b6010780ab2d1e4f88227965b4e7)#define NET\_EVENT\_IPV4\_DHCP\_STOP \

274 (\_NET\_EVENT\_IPV4\_BASE | NET\_EVENT\_IPV4\_CMD\_DHCP\_STOP)

275

[ 277](group__net__mgmt.md#ga17ad57d81f3046555f94f75dc6d31ec1)#define NET\_EVENT\_IPV4\_MCAST\_JOIN \

278 (\_NET\_EVENT\_IPV4\_BASE | NET\_EVENT\_IPV4\_CMD\_MCAST\_JOIN)

279

[ 281](group__net__mgmt.md#ga3cbb8a9dfec8435b93d908171ab944c9)#define NET\_EVENT\_IPV4\_MCAST\_LEAVE \

282 (\_NET\_EVENT\_IPV4\_BASE | NET\_EVENT\_IPV4\_CMD\_MCAST\_LEAVE)

283

[ 285](group__net__mgmt.md#ga5293377de1fdc79e7564f4e5104a07c2)#define NET\_EVENT\_IPV4\_ACD\_SUCCEED \

286 (\_NET\_EVENT\_IPV4\_BASE | NET\_EVENT\_IPV4\_CMD\_ACD\_SUCCEED)

287

[ 289](group__net__mgmt.md#ga3de741f5732473a1f49d9d0b93183549)#define NET\_EVENT\_IPV4\_ACD\_FAILED \

290 (\_NET\_EVENT\_IPV4\_BASE | NET\_EVENT\_IPV4\_CMD\_ACD\_FAILED)

291

[ 296](group__net__mgmt.md#ga9af1f8f4ba965e6d6e82a190ab4748a1)#define NET\_EVENT\_IPV4\_ACD\_CONFLICT \

297 (\_NET\_EVENT\_IPV4\_BASE | NET\_EVENT\_IPV4\_CMD\_ACD\_CONFLICT)

298

[ 303](group__net__mgmt.md#gacbd2b10cc345359c07de4a62eb172a09)#define NET\_EVENT\_L4\_CONNECTED \

304 (\_NET\_EVENT\_L4\_BASE | NET\_EVENT\_L4\_CMD\_CONNECTED)

305

[ 311](group__net__mgmt.md#gacd9e0b5e2f540794b20f11b070ffbd65)#define NET\_EVENT\_L4\_DISCONNECTED \

312 (\_NET\_EVENT\_L4\_BASE | NET\_EVENT\_L4\_CMD\_DISCONNECTED)

313

314

[ 316](group__net__mgmt.md#ga532fdc2f199e047a5d17e325cee12cf1)#define NET\_EVENT\_L4\_IPV4\_CONNECTED \

317 (\_NET\_EVENT\_L4\_BASE | NET\_EVENT\_L4\_CMD\_IPV4\_CONNECTED)

318

[ 320](group__net__mgmt.md#gaa92cc806d93446d548a05edb8e0074c2)#define NET\_EVENT\_L4\_IPV4\_DISCONNECTED \

321 (\_NET\_EVENT\_L4\_BASE | NET\_EVENT\_L4\_CMD\_IPV4\_DISCONNECTED)

322

[ 324](group__net__mgmt.md#gaf6bb88ed90df5aacb40e42fcc5bfbcf5)#define NET\_EVENT\_L4\_IPV6\_CONNECTED \

325 (\_NET\_EVENT\_L4\_BASE | NET\_EVENT\_L4\_CMD\_IPV6\_CONNECTED)

326

[ 328](group__net__mgmt.md#gac81abeab44fbf2b6f29d4e11a1e1bd17)#define NET\_EVENT\_L4\_IPV6\_DISCONNECTED \

329 (\_NET\_EVENT\_L4\_BASE | NET\_EVENT\_L4\_CMD\_IPV6\_DISCONNECTED)

330

[ 332](group__net__mgmt.md#ga5735d13f24c974ad6d4038c93edf05e0)#define NET\_EVENT\_DNS\_SERVER\_ADD \

333 (\_NET\_EVENT\_L4\_BASE | NET\_EVENT\_L4\_CMD\_DNS\_SERVER\_ADD)

334

[ 336](group__net__mgmt.md#ga9d406772e5d1ad2952b2a2e0fed05c73)#define NET\_EVENT\_DNS\_SERVER\_DEL \

337 (\_NET\_EVENT\_L4\_BASE | NET\_EVENT\_L4\_CMD\_DNS\_SERVER\_DEL)

338

[ 340](group__net__mgmt.md#gac5a7458d89e4a95564999dca3c1b9f1e)#define NET\_EVENT\_HOSTNAME\_CHANGED \

341 (\_NET\_EVENT\_L4\_BASE | NET\_EVENT\_L4\_CMD\_HOSTNAME\_CHANGED)

342

[ 344](group__net__mgmt.md#gaa89b82a1890c55775f8c3c24e11f40e2)#define NET\_EVENT\_CAPTURE\_STARTED \

345 (\_NET\_EVENT\_L4\_BASE | NET\_EVENT\_L4\_CMD\_CAPTURE\_STARTED)

346

[ 348](group__net__mgmt.md#gaa2b655aedd597636790409539b1f86cd)#define NET\_EVENT\_CAPTURE\_STOPPED \

349 (\_NET\_EVENT\_L4\_BASE | NET\_EVENT\_L4\_CMD\_CAPTURE\_STOPPED)

350

[ 361](structnet__event__ipv6__addr.md)struct [net\_event\_ipv6\_addr](structnet__event__ipv6__addr.md) {

[ 363](structnet__event__ipv6__addr.md#a3cb4dd6d1e33ef2769cd64fa27c69b43) struct [in6\_addr](structin6__addr.md) [addr](structnet__event__ipv6__addr.md#a3cb4dd6d1e33ef2769cd64fa27c69b43);

364};

365

[ 375](structnet__event__ipv6__nbr.md)struct [net\_event\_ipv6\_nbr](structnet__event__ipv6__nbr.md) {

[ 377](structnet__event__ipv6__nbr.md#a75653facd98b568c300395c45191b289) struct [in6\_addr](structin6__addr.md) [addr](structnet__event__ipv6__nbr.md#a75653facd98b568c300395c45191b289);

[ 379](structnet__event__ipv6__nbr.md#adeb139ad70e794d1a805315ffd1fcbee) int [idx](structnet__event__ipv6__nbr.md#adeb139ad70e794d1a805315ffd1fcbee);

380};

381

[ 390](structnet__event__ipv6__route.md)struct [net\_event\_ipv6\_route](structnet__event__ipv6__route.md) {

[ 392](structnet__event__ipv6__route.md#ad8772d7949fa8b7e7217324acbda6829) struct [in6\_addr](structin6__addr.md) [nexthop](structnet__event__ipv6__route.md#ad8772d7949fa8b7e7217324acbda6829);

[ 394](structnet__event__ipv6__route.md#a42bb70c6b92841e5a77c80a3a193178c) struct [in6\_addr](structin6__addr.md) [addr](structnet__event__ipv6__route.md#a42bb70c6b92841e5a77c80a3a193178c);

[ 396](structnet__event__ipv6__route.md#aa1f21f6963befb3f94183d02c6d2d23f) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [prefix\_len](structnet__event__ipv6__route.md#aa1f21f6963befb3f94183d02c6d2d23f);

397};

398

[ 407](structnet__event__ipv6__prefix.md)struct [net\_event\_ipv6\_prefix](structnet__event__ipv6__prefix.md) {

[ 409](structnet__event__ipv6__prefix.md#a5ccae593ce7678fcdd91a4d0eaf142fb) struct [in6\_addr](structin6__addr.md) [addr](structnet__event__ipv6__prefix.md#a5ccae593ce7678fcdd91a4d0eaf142fb);

[ 411](structnet__event__ipv6__prefix.md#a3d70216e13fc0f78e08eb27f34fe8ace) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [len](structnet__event__ipv6__prefix.md#a3d70216e13fc0f78e08eb27f34fe8ace);

[ 413](structnet__event__ipv6__prefix.md#a6d7b0323896e43a04931ece4daaa09c4) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [lifetime](structnet__event__ipv6__prefix.md#a6d7b0323896e43a04931ece4daaa09c4);

414};

415

[ 422](structnet__event__l4__hostname.md)struct [net\_event\_l4\_hostname](structnet__event__l4__hostname.md) {

[ 424](structnet__event__l4__hostname.md#a8e04c33dfb1c251a0deaa29081283245) char [hostname](structnet__event__l4__hostname.md#a8e04c33dfb1c251a0deaa29081283245)[NET\_HOSTNAME\_SIZE];

425};

426

[ 437](structnet__event__ipv6__pe__filter.md)struct [net\_event\_ipv6\_pe\_filter](structnet__event__ipv6__pe__filter.md) {

[ 439](structnet__event__ipv6__pe__filter.md#a2c0b6477f021e32bae98916f74e6affc) struct [in6\_addr](structin6__addr.md) [prefix](structnet__event__ipv6__pe__filter.md#a2c0b6477f021e32bae98916f74e6affc);

[ 441](structnet__event__ipv6__pe__filter.md#a07961a42f5ff8ca98615164192b8ca5a) bool [is\_deny\_list](structnet__event__ipv6__pe__filter.md#a07961a42f5ff8ca98615164192b8ca5a);

442};

443

444#ifdef \_\_cplusplus

445}

446#endif

447

451

452#endif /\* ZEPHYR\_INCLUDE\_NET\_NET\_EVENT\_H\_ \*/

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

[in6\_addr](structin6__addr.md)

IPv6 address struct.

**Definition** net\_ip.h:142

[net\_event\_ipv6\_addr](structnet__event__ipv6__addr.md)

Network Management event information structure Used to pass information on network events like NET\_EV...

**Definition** net\_event.h:361

[net\_event\_ipv6\_addr::addr](structnet__event__ipv6__addr.md#a3cb4dd6d1e33ef2769cd64fa27c69b43)

struct in6\_addr addr

IPv6 address related to this event.

**Definition** net\_event.h:363

[net\_event\_ipv6\_nbr](structnet__event__ipv6__nbr.md)

Network Management event information structure Used to pass information on network events like NET\_EV...

**Definition** net\_event.h:375

[net\_event\_ipv6\_nbr::addr](structnet__event__ipv6__nbr.md#a75653facd98b568c300395c45191b289)

struct in6\_addr addr

Neighbor IPv6 address.

**Definition** net\_event.h:377

[net\_event\_ipv6\_nbr::idx](structnet__event__ipv6__nbr.md#adeb139ad70e794d1a805315ffd1fcbee)

int idx

Neighbor index in cache.

**Definition** net\_event.h:379

[net\_event\_ipv6\_pe\_filter](structnet__event__ipv6__pe__filter.md)

Network Management event information structure Used to pass information on network events like NET\_EV...

**Definition** net\_event.h:437

[net\_event\_ipv6\_pe\_filter::is\_deny\_list](structnet__event__ipv6__pe__filter.md#a07961a42f5ff8ca98615164192b8ca5a)

bool is\_deny\_list

IPv6 filter deny or allow list.

**Definition** net\_event.h:441

[net\_event\_ipv6\_pe\_filter::prefix](structnet__event__ipv6__pe__filter.md#a2c0b6477f021e32bae98916f74e6affc)

struct in6\_addr prefix

IPv6 address of privacy extension filter.

**Definition** net\_event.h:439

[net\_event\_ipv6\_prefix](structnet__event__ipv6__prefix.md)

Network Management event information structure Used to pass information on network events like NET\_EV...

**Definition** net\_event.h:407

[net\_event\_ipv6\_prefix::len](structnet__event__ipv6__prefix.md#a3d70216e13fc0f78e08eb27f34fe8ace)

uint8\_t len

IPv6 prefix length.

**Definition** net\_event.h:411

[net\_event\_ipv6\_prefix::addr](structnet__event__ipv6__prefix.md#a5ccae593ce7678fcdd91a4d0eaf142fb)

struct in6\_addr addr

IPv6 prefix.

**Definition** net\_event.h:409

[net\_event\_ipv6\_prefix::lifetime](structnet__event__ipv6__prefix.md#a6d7b0323896e43a04931ece4daaa09c4)

uint32\_t lifetime

IPv6 prefix lifetime in seconds.

**Definition** net\_event.h:413

[net\_event\_ipv6\_route](structnet__event__ipv6__route.md)

Network Management event information structure Used to pass information on network events like NET\_EV...

**Definition** net\_event.h:390

[net\_event\_ipv6\_route::addr](structnet__event__ipv6__route.md#a42bb70c6b92841e5a77c80a3a193178c)

struct in6\_addr addr

IPv6 address or prefix of the route.

**Definition** net\_event.h:394

[net\_event\_ipv6\_route::prefix\_len](structnet__event__ipv6__route.md#aa1f21f6963befb3f94183d02c6d2d23f)

uint8\_t prefix\_len

IPv6 prefix length.

**Definition** net\_event.h:396

[net\_event\_ipv6\_route::nexthop](structnet__event__ipv6__route.md#ad8772d7949fa8b7e7217324acbda6829)

struct in6\_addr nexthop

IPv6 address of the next hop.

**Definition** net\_event.h:392

[net\_event\_l4\_hostname](structnet__event__l4__hostname.md)

Network Management event information structure Used to pass information on NET\_EVENT\_HOSTNAME\_CHANGED...

**Definition** net\_event.h:422

[net\_event\_l4\_hostname::hostname](structnet__event__l4__hostname.md#a8e04c33dfb1c251a0deaa29081283245)

char hostname[NET\_HOSTNAME\_SIZE]

New hostname.

**Definition** net\_event.h:424

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [net\_event.h](net__event_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
