---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/net__if_8h_source.html
original_path: doxygen/html/net__if_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

net\_if.h

[Go to the documentation of this file.](net__if_8h.md)

1/\*

2 \* Copyright (c) 2016 Intel Corporation.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

11

12#ifndef ZEPHYR\_INCLUDE\_NET\_NET\_IF\_H\_

13#define ZEPHYR\_INCLUDE\_NET\_NET\_IF\_H\_

14

21

22#include <[zephyr/device.h](device_8h.md)>

23#include <[zephyr/sys/slist.h](slist_8h.md)>

24#include <[zephyr/sys/iterable\_sections.h](sys_2iterable__sections_8h.md)>

25#include <[zephyr/net/net\_core.h](net__core_8h.md)>

26#include <[zephyr/net/hostname.h](hostname_8h.md)>

27#include <[zephyr/net/net\_linkaddr.h](net__linkaddr_8h.md)>

28#include <[zephyr/net/net\_ip.h](net__ip_8h.md)>

29#include <[zephyr/net/net\_l2.h](net__l2_8h.md)>

30#include <[zephyr/net/net\_stats.h](net__stats_8h.md)>

31#include <[zephyr/net/net\_timeout.h](net__timeout_8h.md)>

32

33#if defined(CONFIG\_NET\_DHCPV4) && defined(CONFIG\_NET\_NATIVE\_IPV4)

34#include <[zephyr/net/dhcpv4.h](dhcpv4_8h.md)>

35#endif

36#if defined(CONFIG\_NET\_DHCPV6) && defined(CONFIG\_NET\_NATIVE\_IPV6)

37#include <[zephyr/net/dhcpv6.h](dhcpv6_8h.md)>

38#endif

39#if defined(CONFIG\_NET\_IPV4\_AUTO) && defined(CONFIG\_NET\_NATIVE\_IPV4)

40#include <[zephyr/net/ipv4\_autoconf.h](ipv4__autoconf_8h.md)>

41#endif

42

43#ifdef \_\_cplusplus

44extern "C" {

45#endif

46

[ 52](structnet__if__addr.md)struct [net\_if\_addr](structnet__if__addr.md) {

[ 54](structnet__if__addr.md#a06b8d2e8b5ea6d8d671800d966163763) struct net\_addr [address](structnet__if__addr.md#a06b8d2e8b5ea6d8d671800d966163763);

55

56#if defined(CONFIG\_NET\_NATIVE\_IPV6)

57 struct [net\_timeout](structnet__timeout.md) lifetime;

58#endif

59

60#if defined(CONFIG\_NET\_IPV6\_DAD) && defined(CONFIG\_NET\_NATIVE\_IPV6)

62 [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) dad\_node;

63 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) dad\_start;

64#endif

[ 66](structnet__if__addr.md#ab4fd41001cc24615803bfabb9d48e7eb) enum [net\_addr\_type](group__ip__4__6.md#gafecee2d4a331dc85ad962b81a6303e41) [addr\_type](structnet__if__addr.md#ab4fd41001cc24615803bfabb9d48e7eb);

67

[ 69](structnet__if__addr.md#a3106fdcf0dd2479c95efafc586217a2c) enum [net\_addr\_state](group__ip__4__6.md#ga32e58fc83532ef57eeb6ff952f17288d) [addr\_state](structnet__if__addr.md#a3106fdcf0dd2479c95efafc586217a2c);

70

71#if defined(CONFIG\_NET\_IPV6\_DAD) && defined(CONFIG\_NET\_NATIVE\_IPV6)

73 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) dad\_count;

74#endif

75

[ 77](structnet__if__addr.md#a6e799428eb0633a25e4dc3c55e3a3b8c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [is\_infinite](structnet__if__addr.md#a6e799428eb0633a25e4dc3c55e3a3b8c) : 1;

78

[ 80](structnet__if__addr.md#aed4d91ba064d24ad0d53c0960cde0352) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [is\_used](structnet__if__addr.md#aed4d91ba064d24ad0d53c0960cde0352) : 1;

81

[ 83](structnet__if__addr.md#a1db7cc6c7566baf9340dab6771ca5010) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [is\_mesh\_local](structnet__if__addr.md#a1db7cc6c7566baf9340dab6771ca5010) : 1;

84

85 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \_unused : 5;

86};

87

[ 93](structnet__if__mcast__addr.md)struct [net\_if\_mcast\_addr](structnet__if__mcast__addr.md) {

[ 95](structnet__if__mcast__addr.md#a3e470fc2eb02ac9e5d3d7d0bea0aaa69) struct net\_addr [address](structnet__if__mcast__addr.md#a3e470fc2eb02ac9e5d3d7d0bea0aaa69);

96

97#if defined(CONFIG\_NET\_IPV4\_IGMPV3)

99 struct net\_addr sources[CONFIG\_NET\_IF\_MCAST\_IPV4\_SOURCE\_COUNT];

100

102 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) sources\_len;

103

105 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) record\_type;

106#endif

107

[ 109](structnet__if__mcast__addr.md#abab3e6dba72e24ef522c033d277369ca) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [is\_used](structnet__if__mcast__addr.md#abab3e6dba72e24ef522c033d277369ca) : 1;

110

[ 112](structnet__if__mcast__addr.md#a4af9009b2f9ccc0589a9ba6dac10927b) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [is\_joined](structnet__if__mcast__addr.md#a4af9009b2f9ccc0589a9ba6dac10927b) : 1;

113

114 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \_unused : 6;

115};

116

[ 122](structnet__if__ipv6__prefix.md)struct [net\_if\_ipv6\_prefix](structnet__if__ipv6__prefix.md) {

[ 124](structnet__if__ipv6__prefix.md#a925a97a49d383bd4ce475f5d09fcb7e3) struct [net\_timeout](structnet__timeout.md) [lifetime](structnet__if__ipv6__prefix.md#a925a97a49d383bd4ce475f5d09fcb7e3);

125

[ 127](structnet__if__ipv6__prefix.md#a65b450d0942b3c96cfc575b462d82028) struct [in6\_addr](structin6__addr.md) [prefix](structnet__if__ipv6__prefix.md#a65b450d0942b3c96cfc575b462d82028);

128

[ 130](structnet__if__ipv6__prefix.md#a0e2d1997e2ccfe1e1af5f16e0c74ed92) struct [net\_if](structnet__if.md) \*[iface](structnet__if__ipv6__prefix.md#a0e2d1997e2ccfe1e1af5f16e0c74ed92);

131

[ 133](structnet__if__ipv6__prefix.md#a4d2bc2acbe51256b76cf4d3ced3aac39) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [len](structnet__if__ipv6__prefix.md#a4d2bc2acbe51256b76cf4d3ced3aac39);

134

[ 136](structnet__if__ipv6__prefix.md#a22090441b27bed06098679bf23b4e1e9) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [is\_infinite](structnet__if__ipv6__prefix.md#a22090441b27bed06098679bf23b4e1e9) : 1;

137

[ 139](structnet__if__ipv6__prefix.md#a6a4295256957e5eddf149f1ceff62e3f) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [is\_used](structnet__if__ipv6__prefix.md#a6a4295256957e5eddf149f1ceff62e3f) : 1;

140

141 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \_unused : 6;

142};

143

[ 149](structnet__if__router.md)struct [net\_if\_router](structnet__if__router.md) {

[ 151](structnet__if__router.md#aabbac0cd0a59ca0eafdcfc0eaf5d909a) [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) [node](structnet__if__router.md#aabbac0cd0a59ca0eafdcfc0eaf5d909a);

152

[ 154](structnet__if__router.md#a86a2ca1b95e348acbde8ce90986b83db) struct net\_addr [address](structnet__if__router.md#a86a2ca1b95e348acbde8ce90986b83db);

155

[ 157](structnet__if__router.md#a03789aa0a40f7686b76616de0ca0401a) struct [net\_if](structnet__if.md) \*[iface](structnet__if__router.md#a03789aa0a40f7686b76616de0ca0401a);

158

[ 160](structnet__if__router.md#adf4f4c722917b3c30f8c73bc2519957f) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [life\_start](structnet__if__router.md#adf4f4c722917b3c30f8c73bc2519957f);

161

[ 163](structnet__if__router.md#a4b0d2ad8f225ab61022c10dfce3db199) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [lifetime](structnet__if__router.md#a4b0d2ad8f225ab61022c10dfce3db199);

164

[ 166](structnet__if__router.md#a7196e6d2bc2c958d98dfe29143a62048) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [is\_used](structnet__if__router.md#a7196e6d2bc2c958d98dfe29143a62048) : 1;

167

[ 169](structnet__if__router.md#a34745207edcad2745d6ce311e2bf1894) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [is\_default](structnet__if__router.md#a34745207edcad2745d6ce311e2bf1894) : 1;

170

[ 172](structnet__if__router.md#a4cb47f30241ae3d410f56f1487254ed0) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [is\_infinite](structnet__if__router.md#a4cb47f30241ae3d410f56f1487254ed0) : 1;

173

174 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \_unused : 5;

175};

176

[ 178](group__net__if.md#gae691e5537917ffce27ad0db82c730371)enum [net\_if\_flag](group__net__if.md#gae691e5537917ffce27ad0db82c730371) {

[ 180](group__net__if.md#ggae691e5537917ffce27ad0db82c730371ab0ab7393d643354c46c3437d74c15840) [NET\_IF\_UP](group__net__if.md#ggae691e5537917ffce27ad0db82c730371ab0ab7393d643354c46c3437d74c15840),

181

[ 183](group__net__if.md#ggae691e5537917ffce27ad0db82c730371a3256ef2d537c85b4c2b33b92935e1009) [NET\_IF\_POINTOPOINT](group__net__if.md#ggae691e5537917ffce27ad0db82c730371a3256ef2d537c85b4c2b33b92935e1009),

184

[ 186](group__net__if.md#ggae691e5537917ffce27ad0db82c730371a700d92a5b0de3c779e59806137b35141) [NET\_IF\_PROMISC](group__net__if.md#ggae691e5537917ffce27ad0db82c730371a700d92a5b0de3c779e59806137b35141),

187

[ 194](group__net__if.md#ggae691e5537917ffce27ad0db82c730371a0babb762301878eaf8ef8a05213ecf05) [NET\_IF\_NO\_AUTO\_START](group__net__if.md#ggae691e5537917ffce27ad0db82c730371a0babb762301878eaf8ef8a05213ecf05),

195

[ 197](group__net__if.md#ggae691e5537917ffce27ad0db82c730371aaaeafc62e61ec120609205770c8b54f0) [NET\_IF\_SUSPENDED](group__net__if.md#ggae691e5537917ffce27ad0db82c730371aaaeafc62e61ec120609205770c8b54f0),

198

[ 203](group__net__if.md#ggae691e5537917ffce27ad0db82c730371a581971c9d93a910c4c607da45aa2e4ac) [NET\_IF\_FORWARD\_MULTICASTS](group__net__if.md#ggae691e5537917ffce27ad0db82c730371a581971c9d93a910c4c607da45aa2e4ac),

204

[ 206](group__net__if.md#ggae691e5537917ffce27ad0db82c730371a67d2c0fe390ab16f347ee2dc0a056329) [NET\_IF\_IPV4](group__net__if.md#ggae691e5537917ffce27ad0db82c730371a67d2c0fe390ab16f347ee2dc0a056329),

207

[ 209](group__net__if.md#ggae691e5537917ffce27ad0db82c730371aab31a9e1e8c02159f45efc4e0455a4d6) [NET\_IF\_IPV6](group__net__if.md#ggae691e5537917ffce27ad0db82c730371aab31a9e1e8c02159f45efc4e0455a4d6),

210

[ 212](group__net__if.md#ggae691e5537917ffce27ad0db82c730371add3e2ecdcd5de3154f9bd2836428a25a) [NET\_IF\_RUNNING](group__net__if.md#ggae691e5537917ffce27ad0db82c730371add3e2ecdcd5de3154f9bd2836428a25a),

213

[ 215](group__net__if.md#ggae691e5537917ffce27ad0db82c730371ab1a529826bad6b4bcd04185372f97d6d) [NET\_IF\_LOWER\_UP](group__net__if.md#ggae691e5537917ffce27ad0db82c730371ab1a529826bad6b4bcd04185372f97d6d),

216

[ 218](group__net__if.md#ggae691e5537917ffce27ad0db82c730371a7dd1db72a37b1fbc4c4491ce1c75238d) [NET\_IF\_DORMANT](group__net__if.md#ggae691e5537917ffce27ad0db82c730371a7dd1db72a37b1fbc4c4491ce1c75238d),

219

[ 221](group__net__if.md#ggae691e5537917ffce27ad0db82c730371a542ecce860ef3bf2df493da8d4c6a2f7) [NET\_IF\_IPV6\_NO\_ND](group__net__if.md#ggae691e5537917ffce27ad0db82c730371a542ecce860ef3bf2df493da8d4c6a2f7),

222

[ 224](group__net__if.md#ggae691e5537917ffce27ad0db82c730371a1d362cfabb58eb220ddb069431221fbe) [NET\_IF\_IPV6\_NO\_MLD](group__net__if.md#ggae691e5537917ffce27ad0db82c730371a1d362cfabb58eb220ddb069431221fbe),

225

[ 227](group__net__if.md#ggae691e5537917ffce27ad0db82c730371ae8d564e1577c8daad8ce50a729c500c9) [NET\_IF\_NO\_TX\_LOCK](group__net__if.md#ggae691e5537917ffce27ad0db82c730371ae8d564e1577c8daad8ce50a729c500c9),

228

230 /\* Total number of flags - must be at the end of the enum \*/

231 NET\_IF\_NUM\_FLAGS

233};

234

[ 236](group__net__if.md#gadfe9d90f24046cd9bd4bbee096e747b9)enum [net\_if\_oper\_state](group__net__if.md#gadfe9d90f24046cd9bd4bbee096e747b9) {

[ 237](group__net__if.md#ggadfe9d90f24046cd9bd4bbee096e747b9ac7cae092ea6ceeb62499a9b435ac4b58) [NET\_IF\_OPER\_UNKNOWN](group__net__if.md#ggadfe9d90f24046cd9bd4bbee096e747b9ac7cae092ea6ceeb62499a9b435ac4b58),

[ 238](group__net__if.md#ggadfe9d90f24046cd9bd4bbee096e747b9a8f9f55840e75693163197baae9d50c32) [NET\_IF\_OPER\_NOTPRESENT](group__net__if.md#ggadfe9d90f24046cd9bd4bbee096e747b9a8f9f55840e75693163197baae9d50c32),

[ 239](group__net__if.md#ggadfe9d90f24046cd9bd4bbee096e747b9adb20a95215310c420f8dae7e17a2f367) [NET\_IF\_OPER\_DOWN](group__net__if.md#ggadfe9d90f24046cd9bd4bbee096e747b9adb20a95215310c420f8dae7e17a2f367),

[ 240](group__net__if.md#ggadfe9d90f24046cd9bd4bbee096e747b9ae7e9b8b12ae618a5ee1483dee916aab4) [NET\_IF\_OPER\_LOWERLAYERDOWN](group__net__if.md#ggadfe9d90f24046cd9bd4bbee096e747b9ae7e9b8b12ae618a5ee1483dee916aab4),

[ 241](group__net__if.md#ggadfe9d90f24046cd9bd4bbee096e747b9a2240173b5c247ab5eb0a9a6afafb296f) [NET\_IF\_OPER\_TESTING](group__net__if.md#ggadfe9d90f24046cd9bd4bbee096e747b9a2240173b5c247ab5eb0a9a6afafb296f),

[ 242](group__net__if.md#ggadfe9d90f24046cd9bd4bbee096e747b9a5cbe2aa27a444444d4acf122113d430d) [NET\_IF\_OPER\_DORMANT](group__net__if.md#ggadfe9d90f24046cd9bd4bbee096e747b9a5cbe2aa27a444444d4acf122113d430d),

[ 243](group__net__if.md#ggadfe9d90f24046cd9bd4bbee096e747b9a6b99bfc28d831292029761d74209ee03) [NET\_IF\_OPER\_UP](group__net__if.md#ggadfe9d90f24046cd9bd4bbee096e747b9a6b99bfc28d831292029761d74209ee03),

244} \_\_packed;

245

246#if defined(CONFIG\_NET\_OFFLOAD)

247struct net\_offload;

248#endif /\* CONFIG\_NET\_OFFLOAD \*/

249

251#if defined(CONFIG\_NET\_NATIVE\_IPV6)

252#define NET\_IF\_MAX\_IPV6\_ADDR CONFIG\_NET\_IF\_UNICAST\_IPV6\_ADDR\_COUNT

253#define NET\_IF\_MAX\_IPV6\_MADDR CONFIG\_NET\_IF\_MCAST\_IPV6\_ADDR\_COUNT

254#define NET\_IF\_MAX\_IPV6\_PREFIX CONFIG\_NET\_IF\_IPV6\_PREFIX\_COUNT

255#else

256#define NET\_IF\_MAX\_IPV6\_ADDR 0

257#define NET\_IF\_MAX\_IPV6\_MADDR 0

258#define NET\_IF\_MAX\_IPV6\_PREFIX 0

259#endif

260/\* @endcond \*/

261

[ 262](structnet__if__ipv6.md)struct [net\_if\_ipv6](structnet__if__ipv6.md) {

[ 264](structnet__if__ipv6.md#adb6431d336cc3f46972e13d2255452c8) struct [net\_if\_addr](structnet__if__addr.md) [unicast](structnet__if__ipv6.md#adb6431d336cc3f46972e13d2255452c8)[NET\_IF\_MAX\_IPV6\_ADDR];

265

[ 267](structnet__if__ipv6.md#a727d2773e0dee3be687dda5b2dd55682) struct [net\_if\_mcast\_addr](structnet__if__mcast__addr.md) [mcast](structnet__if__ipv6.md#a727d2773e0dee3be687dda5b2dd55682)[NET\_IF\_MAX\_IPV6\_MADDR];

268

[ 270](structnet__if__ipv6.md#a2dccdc984f08527302d8d910a2658f72) struct [net\_if\_ipv6\_prefix](structnet__if__ipv6__prefix.md) [prefix](structnet__if__ipv6.md#a2dccdc984f08527302d8d910a2658f72)[NET\_IF\_MAX\_IPV6\_PREFIX];

271

[ 273](structnet__if__ipv6.md#a500a78fe23ee2ebc63f3d3b53b5b92ea) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [base\_reachable\_time](structnet__if__ipv6.md#a500a78fe23ee2ebc63f3d3b53b5b92ea);

274

[ 276](structnet__if__ipv6.md#af57b7dca189167f8cc757c4ed6b08f2f) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [reachable\_time](structnet__if__ipv6.md#af57b7dca189167f8cc757c4ed6b08f2f);

277

[ 279](structnet__if__ipv6.md#ac5ee47ff9d3e429ecbb8623e5d713246) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [retrans\_timer](structnet__if__ipv6.md#ac5ee47ff9d3e429ecbb8623e5d713246);

280#if defined(CONFIG\_NET\_IPV6\_ND) && defined(CONFIG\_NET\_NATIVE\_IPV6)

282 [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) rs\_node;

283

284 /\* RS start time \*/

285 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) rs\_start;

286

288 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) rs\_count;

289#endif

290

[ 292](structnet__if__ipv6.md#a71775a082984274fbc7c009ead18e751) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [hop\_limit](structnet__if__ipv6.md#a71775a082984274fbc7c009ead18e751);

293

[ 295](structnet__if__ipv6.md#ae94906c28578f2e1ea2506b0e2972d4c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [mcast\_hop\_limit](structnet__if__ipv6.md#ae94906c28578f2e1ea2506b0e2972d4c);

296};

297

298#if defined(CONFIG\_NET\_DHCPV6) && defined(CONFIG\_NET\_NATIVE\_IPV6)

299struct net\_if\_dhcpv6 {

301 [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) node;

302

304 struct net\_dhcpv6\_duid\_storage clientid;

305

307 struct net\_dhcpv6\_duid\_storage serverid;

308

310 enum net\_dhcpv6\_state [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90);

311

313 struct [net\_dhcpv6\_params](structnet__dhcpv6__params.md) params;

314

316 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) timeout;

317

319 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) exchange\_start;

320

322 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) t1;

323

325 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) t2;

326

330 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) expire;

331

333 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) addr\_iaid;

334

336 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) prefix\_iaid;

337

339 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) retransmit\_timeout;

340

342 [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) server\_preference;

343

345 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) retransmissions;

346

348 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) tid[DHCPV6\_TID\_SIZE];

349

351 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) prefix\_len;

352

354 struct [in6\_addr](structin6__addr.md) prefix;

355

357 struct [in6\_addr](structin6__addr.md) addr;

358};

359#endif /\* defined(CONFIG\_NET\_DHCPV6) && defined(CONFIG\_NET\_NATIVE\_IPV6) \*/

360

362#if defined(CONFIG\_NET\_NATIVE\_IPV4)

363#define NET\_IF\_MAX\_IPV4\_ADDR CONFIG\_NET\_IF\_UNICAST\_IPV4\_ADDR\_COUNT

364#define NET\_IF\_MAX\_IPV4\_MADDR CONFIG\_NET\_IF\_MCAST\_IPV4\_ADDR\_COUNT

365#else

366#define NET\_IF\_MAX\_IPV4\_ADDR 0

367#define NET\_IF\_MAX\_IPV4\_MADDR 0

368#endif

370

[ 371](structnet__if__ipv4.md)struct [net\_if\_ipv4](structnet__if__ipv4.md) {

[ 373](structnet__if__ipv4.md#a89b942f7120619fba28f4fd9ab0bf41c) struct [net\_if\_addr](structnet__if__addr.md) [unicast](structnet__if__ipv4.md#a89b942f7120619fba28f4fd9ab0bf41c)[NET\_IF\_MAX\_IPV4\_ADDR];

374

[ 376](structnet__if__ipv4.md#adfaf5b50255bd35297195a7218729ae7) struct [net\_if\_mcast\_addr](structnet__if__mcast__addr.md) [mcast](structnet__if__ipv4.md#adfaf5b50255bd35297195a7218729ae7)[NET\_IF\_MAX\_IPV4\_MADDR];

377

[ 379](structnet__if__ipv4.md#aa24772c7202bf465ee3da94a172b7bcb) struct [in\_addr](structin__addr.md) [gw](structnet__if__ipv4.md#aa24772c7202bf465ee3da94a172b7bcb);

380

[ 382](structnet__if__ipv4.md#a9de5d553b0719489a34f1190939d0bc0) struct [in\_addr](structin__addr.md) [netmask](structnet__if__ipv4.md#a9de5d553b0719489a34f1190939d0bc0);

383

[ 385](structnet__if__ipv4.md#acdc6d5d6eb5362f4f6d2c027cc40e684) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [ttl](structnet__if__ipv4.md#acdc6d5d6eb5362f4f6d2c027cc40e684);

386

[ 388](structnet__if__ipv4.md#a7e9bf16d51989cfcfe564f4f0a43b480) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [mcast\_ttl](structnet__if__ipv4.md#a7e9bf16d51989cfcfe564f4f0a43b480);

389};

390

391#if defined(CONFIG\_NET\_DHCPV4) && defined(CONFIG\_NET\_NATIVE\_IPV4)

392struct net\_if\_dhcpv4 {

394 [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) node;

395

397 [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) timer\_start;

398

400 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) request\_time;

401

402 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) xid;

403

405 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) lease\_time;

406

408 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) renewal\_time;

409

411 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) rebinding\_time;

412

414 struct [in\_addr](structin__addr.md) server\_id;

415

417 struct [in\_addr](structin__addr.md) requested\_ip;

418

423 enum net\_dhcpv4\_state [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90);

424

426 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) attempts;

427

429 struct [in\_addr](structin__addr.md) request\_server\_addr;

430

432 struct [in\_addr](structin__addr.md) response\_src\_addr;

433};

434#endif /\* CONFIG\_NET\_DHCPV4 \*/

435

436#if defined(CONFIG\_NET\_IPV4\_AUTO) && defined(CONFIG\_NET\_NATIVE\_IPV4)

437struct net\_if\_ipv4\_autoconf {

439 [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) node;

440

442 struct net\_if \*iface;

443

445 [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) timer\_start;

446

448 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) timer\_timeout;

449

451 struct in\_addr current\_ip;

452

454 struct in\_addr requested\_ip;

455

458 enum [net\_ipv4\_autoconf\_state](ipv4__autoconf_8h.md#abdf8bb08f12768aad2ff95b902bdc899) [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90);

459

461 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) probe\_cnt;

462

464 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) announce\_cnt;

465

467 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) conflict\_cnt;

468};

469#endif /\* CONFIG\_NET\_IPV4\_AUTO \*/

470

472/\* We always need to have at least one IP config \*/

473#define NET\_IF\_MAX\_CONFIGS 1

475

[ 479](structnet__if__ip.md)struct [net\_if\_ip](structnet__if__ip.md) {

480#if defined(CONFIG\_NET\_NATIVE\_IPV6)

481 struct [net\_if\_ipv6](structnet__if__ipv6.md) \*ipv6;

482#endif /\* CONFIG\_NET\_IPV6 \*/

483

484#if defined(CONFIG\_NET\_NATIVE\_IPV4)

485 struct [net\_if\_ipv4](structnet__if__ipv4.md) \*ipv4;

486#endif /\* CONFIG\_NET\_IPV4 \*/

487};

488

[ 492](structnet__if__config.md)struct [net\_if\_config](structnet__if__config.md) {

493#if defined(CONFIG\_NET\_IP)

495 struct [net\_if\_ip](structnet__if__ip.md) ip;

496#endif

497

498#if defined(CONFIG\_NET\_DHCPV4) && defined(CONFIG\_NET\_NATIVE\_IPV4)

499 struct net\_if\_dhcpv4 dhcpv4;

500#endif /\* CONFIG\_NET\_DHCPV4 \*/

501

502#if defined(CONFIG\_NET\_DHCPV6) && defined(CONFIG\_NET\_NATIVE\_IPV6)

503 struct net\_if\_dhcpv6 dhcpv6;

504#endif /\* CONFIG\_NET\_DHCPV6 \*/

505

506#if defined(CONFIG\_NET\_IPV4\_AUTO) && defined(CONFIG\_NET\_NATIVE\_IPV4)

507 struct net\_if\_ipv4\_autoconf ipv4auto;

508#endif /\* CONFIG\_NET\_IPV4\_AUTO \*/

509

510#if defined(CONFIG\_NET\_L2\_VIRTUAL)

515 [sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8) virtual\_interfaces;

516#endif /\* CONFIG\_NET\_L2\_VIRTUAL \*/

517

518#if defined(CONFIG\_NET\_INTERFACE\_NAME)

523 char name[CONFIG\_NET\_INTERFACE\_NAME\_LEN + 1];

524#endif

525};

526

[ 536](structnet__traffic__class.md)struct [net\_traffic\_class](structnet__traffic__class.md) {

[ 538](structnet__traffic__class.md#a94511ca12bad1687f5c7ca862c857ded) struct [k\_fifo](structk__fifo.md) [fifo](structnet__traffic__class.md#a94511ca12bad1687f5c7ca862c857ded);

539

[ 541](structnet__traffic__class.md#a8d0023588fee0a8ff1381bbc80ada143) struct [k\_thread](structk__thread.md) [handler](structnet__traffic__class.md#a8d0023588fee0a8ff1381bbc80ada143);

542

[ 544](structnet__traffic__class.md#a2d98bc68d38bdef649d645b8b52516c5) [k\_thread\_stack\_t](arch__interface_8h.md#a9fc2dce533bd7b8cb1fdd4bdbb2b62b1) \*[stack](structnet__traffic__class.md#a2d98bc68d38bdef649d645b8b52516c5);

545};

546

[ 553](group__net__if.md#gaef3dfe26195514aac625e9f22e399759)typedef int (\*[net\_socket\_create\_t](group__net__if.md#gaef3dfe26195514aac625e9f22e399759))(int, int, int);

554

[ 569](structnet__if__dev.md)struct [net\_if\_dev](structnet__if__dev.md) {

[ 571](structnet__if__dev.md#aab633a44f165f571910dc9fc9e131c50) const struct [device](structdevice.md) \*[dev](structnet__if__dev.md#aab633a44f165f571910dc9fc9e131c50);

572

[ 574](structnet__if__dev.md#a85d713c62875f5fe9e3ec29773150797) const struct [net\_l2](structnet__l2.md) \* const [l2](structnet__if__dev.md#a85d713c62875f5fe9e3ec29773150797);

575

[ 577](structnet__if__dev.md#a8fec6a7f612fc1268ef486d8bdebe018) void \*[l2\_data](structnet__if__dev.md#a8fec6a7f612fc1268ef486d8bdebe018);

578

579 /\* For internal use \*/

[ 580](structnet__if__dev.md#ac8f9c30e1dea05c28c88d3b367b130f5) [ATOMIC\_DEFINE](group__atomic__apis.md#ga249c575db9764486197709b327f7370e)([flags](structnet__if__dev.md#ac8f9c30e1dea05c28c88d3b367b130f5), NET\_IF\_NUM\_FLAGS);

581

[ 583](structnet__if__dev.md#aac6d5d341ab520e6aac7f7b03737c197) struct [net\_linkaddr](structnet__linkaddr.md) [link\_addr](structnet__if__dev.md#aac6d5d341ab520e6aac7f7b03737c197);

584

585#if defined(CONFIG\_NET\_OFFLOAD)

591 struct net\_offload \*offload;

592#endif /\* CONFIG\_NET\_OFFLOAD \*/

593

[ 595](structnet__if__dev.md#aa15ccca2eb67b8d2afca153ccacb3742) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [mtu](structnet__if__dev.md#aa15ccca2eb67b8d2afca153ccacb3742);

596

597#if defined(CONFIG\_NET\_SOCKETS\_OFFLOAD)

601 [net\_socket\_create\_t](group__net__if.md#gaef3dfe26195514aac625e9f22e399759) socket\_offload;

602#endif /\* CONFIG\_NET\_SOCKETS\_OFFLOAD \*/

603

[ 605](structnet__if__dev.md#a30eabb2ffae082d0de81a50c510738a3) enum [net\_if\_oper\_state](group__net__if.md#gadfe9d90f24046cd9bd4bbee096e747b9) [oper\_state](structnet__if__dev.md#a30eabb2ffae082d0de81a50c510738a3);

606};

607

[ 615](structnet__if.md)struct [net\_if](structnet__if.md) {

[ 617](structnet__if.md#a0982ba2019cdaa7701162e60fdb2171e) struct [net\_if\_dev](structnet__if__dev.md) \*[if\_dev](structnet__if.md#a0982ba2019cdaa7701162e60fdb2171e);

618

619#if defined(CONFIG\_NET\_STATISTICS\_PER\_INTERFACE)

621 struct [net\_stats](structnet__stats.md) stats;

622#endif /\* CONFIG\_NET\_STATISTICS\_PER\_INTERFACE \*/

623

[ 625](structnet__if.md#a5e71962f55bdead7bfbbb96518c6c404) struct [net\_if\_config](structnet__if__config.md) [config](structnet__if.md#a5e71962f55bdead7bfbbb96518c6c404);

626

627#if defined(CONFIG\_NET\_POWER\_MANAGEMENT)

632 int tx\_pending;

633#endif

634

[ 635](structnet__if.md#ace2233b71da53ff0fc7cd564ccfc5a03) struct [k\_mutex](structk__mutex.md) [lock](structnet__if.md#ace2233b71da53ff0fc7cd564ccfc5a03);

[ 636](structnet__if.md#af00f729ebddfdcf725169f61b6cd586b) struct [k\_mutex](structk__mutex.md) [tx\_lock](structnet__if.md#af00f729ebddfdcf725169f61b6cd586b);

637};

638

[ 639](group__net__if.md#gaaa649aca4e48d74ae2f7cff3769e9781)static inline void [net\_if\_lock](group__net__if.md#gaaa649aca4e48d74ae2f7cff3769e9781)(struct [net\_if](structnet__if.md) \*iface)

640{

641 NET\_ASSERT(iface);

642

643 (void)[k\_mutex\_lock](group__mutex__apis.md#ga850549358645249c285669baa49c33b0)(&iface->[lock](structnet__if.md#ace2233b71da53ff0fc7cd564ccfc5a03), [K\_FOREVER](group__clock__apis.md#ga0bb4b83f0222193b21a8910311bab0ca));

644}

645

[ 646](group__net__if.md#ga20e166991c20ddeca8023b57ed8957ad)static inline void [net\_if\_unlock](group__net__if.md#ga20e166991c20ddeca8023b57ed8957ad)(struct [net\_if](structnet__if.md) \*iface)

647{

648 NET\_ASSERT(iface);

649

650 [k\_mutex\_unlock](group__mutex__apis.md#ga360f4c0e7258b0d7030cdb1f452b2c31)(&iface->[lock](structnet__if.md#ace2233b71da53ff0fc7cd564ccfc5a03));

651}

652

653static inline bool [net\_if\_flag\_is\_set](group__net__if.md#gae1f373ddd61c18a81481d8ddcfb12543)(struct [net\_if](structnet__if.md) \*iface,

654 enum [net\_if\_flag](group__net__if.md#gae691e5537917ffce27ad0db82c730371) value);

655

[ 656](group__net__if.md#gafb64d93ba8f6b047bb61a6fd4994b711)static inline void [net\_if\_tx\_lock](group__net__if.md#gafb64d93ba8f6b047bb61a6fd4994b711)(struct [net\_if](structnet__if.md) \*iface)

657{

658 NET\_ASSERT(iface);

659

660 if ([net\_if\_flag\_is\_set](group__net__if.md#gae1f373ddd61c18a81481d8ddcfb12543)(iface, [NET\_IF\_NO\_TX\_LOCK](group__net__if.md#ggae691e5537917ffce27ad0db82c730371ae8d564e1577c8daad8ce50a729c500c9))) {

661 return;

662 }

663

664 (void)[k\_mutex\_lock](group__mutex__apis.md#ga850549358645249c285669baa49c33b0)(&iface->[tx\_lock](structnet__if.md#af00f729ebddfdcf725169f61b6cd586b), [K\_FOREVER](group__clock__apis.md#ga0bb4b83f0222193b21a8910311bab0ca));

665}

666

[ 667](group__net__if.md#ga7deaa758536baa81045219c6f5c79217)static inline void [net\_if\_tx\_unlock](group__net__if.md#ga7deaa758536baa81045219c6f5c79217)(struct [net\_if](structnet__if.md) \*iface)

668{

669 NET\_ASSERT(iface);

670

671 if ([net\_if\_flag\_is\_set](group__net__if.md#gae1f373ddd61c18a81481d8ddcfb12543)(iface, [NET\_IF\_NO\_TX\_LOCK](group__net__if.md#ggae691e5537917ffce27ad0db82c730371ae8d564e1577c8daad8ce50a729c500c9))) {

672 return;

673 }

674

675 [k\_mutex\_unlock](group__mutex__apis.md#ga360f4c0e7258b0d7030cdb1f452b2c31)(&iface->[tx\_lock](structnet__if.md#af00f729ebddfdcf725169f61b6cd586b));

676}

677

[ 684](group__net__if.md#ga52f9fca13e9f836799e0e40f581744d2)static inline void [net\_if\_flag\_set](group__net__if.md#ga52f9fca13e9f836799e0e40f581744d2)(struct [net\_if](structnet__if.md) \*iface,

685 enum [net\_if\_flag](group__net__if.md#gae691e5537917ffce27ad0db82c730371) value)

686{

687 NET\_ASSERT(iface);

688 NET\_ASSERT(iface->[if\_dev](structnet__if.md#a0982ba2019cdaa7701162e60fdb2171e));

689

690 [atomic\_set\_bit](group__atomic__apis.md#ga17a3961ba7610ad6e595e602f70344a0)(iface->[if\_dev](structnet__if.md#a0982ba2019cdaa7701162e60fdb2171e)->[flags](structnet__if__dev.md#ac8f9c30e1dea05c28c88d3b367b130f5), value);

691}

692

[ 701](group__net__if.md#ga42e7482191a92007960601f8bb621dca)static inline bool [net\_if\_flag\_test\_and\_set](group__net__if.md#ga42e7482191a92007960601f8bb621dca)(struct [net\_if](structnet__if.md) \*iface,

702 enum [net\_if\_flag](group__net__if.md#gae691e5537917ffce27ad0db82c730371) value)

703{

704 NET\_ASSERT(iface);

705 NET\_ASSERT(iface->[if\_dev](structnet__if.md#a0982ba2019cdaa7701162e60fdb2171e));

706

707 return [atomic\_test\_and\_set\_bit](group__atomic__apis.md#ga7ff45e13aa5f8be5d7a550e49f5c720b)(iface->[if\_dev](structnet__if.md#a0982ba2019cdaa7701162e60fdb2171e)->[flags](structnet__if__dev.md#ac8f9c30e1dea05c28c88d3b367b130f5), value);

708}

709

[ 716](group__net__if.md#gaff751b6a92b0c608ecfc50e8c0587fd3)static inline void [net\_if\_flag\_clear](group__net__if.md#gaff751b6a92b0c608ecfc50e8c0587fd3)(struct [net\_if](structnet__if.md) \*iface,

717 enum [net\_if\_flag](group__net__if.md#gae691e5537917ffce27ad0db82c730371) value)

718{

719 NET\_ASSERT(iface);

720 NET\_ASSERT(iface->[if\_dev](structnet__if.md#a0982ba2019cdaa7701162e60fdb2171e));

721

722 [atomic\_clear\_bit](group__atomic__apis.md#ga1c1693d524c49d11fd32b323a39d718e)(iface->[if\_dev](structnet__if.md#a0982ba2019cdaa7701162e60fdb2171e)->[flags](structnet__if__dev.md#ac8f9c30e1dea05c28c88d3b367b130f5), value);

723}

724

[ 733](group__net__if.md#gab8f371c7f8890cf4728177f6595141d7)static inline bool [net\_if\_flag\_test\_and\_clear](group__net__if.md#gab8f371c7f8890cf4728177f6595141d7)(struct [net\_if](structnet__if.md) \*iface,

734 enum [net\_if\_flag](group__net__if.md#gae691e5537917ffce27ad0db82c730371) value)

735{

736 NET\_ASSERT(iface);

737 NET\_ASSERT(iface->[if\_dev](structnet__if.md#a0982ba2019cdaa7701162e60fdb2171e));

738

739 return [atomic\_test\_and\_clear\_bit](group__atomic__apis.md#ga53159437721084da0ec8ee70ec212472)(iface->[if\_dev](structnet__if.md#a0982ba2019cdaa7701162e60fdb2171e)->[flags](structnet__if__dev.md#ac8f9c30e1dea05c28c88d3b367b130f5), value);

740}

741

[ 750](group__net__if.md#gae1f373ddd61c18a81481d8ddcfb12543)static inline bool [net\_if\_flag\_is\_set](group__net__if.md#gae1f373ddd61c18a81481d8ddcfb12543)(struct [net\_if](structnet__if.md) \*iface,

751 enum [net\_if\_flag](group__net__if.md#gae691e5537917ffce27ad0db82c730371) value)

752{

753 NET\_ASSERT(iface);

754 NET\_ASSERT(iface->[if\_dev](structnet__if.md#a0982ba2019cdaa7701162e60fdb2171e));

755

756 if (iface == NULL) {

757 return false;

758 }

759

760 return [atomic\_test\_bit](group__atomic__apis.md#ga190ddc108f45e7649689753c08658eae)(iface->[if\_dev](structnet__if.md#a0982ba2019cdaa7701162e60fdb2171e)->[flags](structnet__if__dev.md#ac8f9c30e1dea05c28c88d3b367b130f5), value);

761}

762

[ 771](group__net__if.md#ga1f1bf845e63cce02e2183889cc85d57e)static inline enum [net\_if\_oper\_state](group__net__if.md#gadfe9d90f24046cd9bd4bbee096e747b9) [net\_if\_oper\_state\_set](group__net__if.md#ga1f1bf845e63cce02e2183889cc85d57e)(

772 struct [net\_if](structnet__if.md) \*iface, enum [net\_if\_oper\_state](group__net__if.md#gadfe9d90f24046cd9bd4bbee096e747b9) oper\_state)

773{

774 NET\_ASSERT(iface);

775 NET\_ASSERT(iface->[if\_dev](structnet__if.md#a0982ba2019cdaa7701162e60fdb2171e));

776

777 if (oper\_state >= [NET\_IF\_OPER\_UNKNOWN](group__net__if.md#ggadfe9d90f24046cd9bd4bbee096e747b9ac7cae092ea6ceeb62499a9b435ac4b58) && oper\_state <= [NET\_IF\_OPER\_UP](group__net__if.md#ggadfe9d90f24046cd9bd4bbee096e747b9a6b99bfc28d831292029761d74209ee03)) {

778 iface->[if\_dev](structnet__if.md#a0982ba2019cdaa7701162e60fdb2171e)->[oper\_state](structnet__if__dev.md#a30eabb2ffae082d0de81a50c510738a3) = oper\_state;

779 }

780

781 return iface->[if\_dev](structnet__if.md#a0982ba2019cdaa7701162e60fdb2171e)->[oper\_state](structnet__if__dev.md#a30eabb2ffae082d0de81a50c510738a3);

782}

783

[ 791](group__net__if.md#gad9e957a4866b4566296ee39392fde0e4)static inline enum [net\_if\_oper\_state](group__net__if.md#gadfe9d90f24046cd9bd4bbee096e747b9) [net\_if\_oper\_state](group__net__if.md#gadfe9d90f24046cd9bd4bbee096e747b9)(struct [net\_if](structnet__if.md) \*iface)

792{

793 NET\_ASSERT(iface);

794 NET\_ASSERT(iface->[if\_dev](structnet__if.md#a0982ba2019cdaa7701162e60fdb2171e));

795

796 return iface->[if\_dev](structnet__if.md#a0982ba2019cdaa7701162e60fdb2171e)->[oper\_state](structnet__if__dev.md#a30eabb2ffae082d0de81a50c510738a3);

797}

798

[ 807](group__net__if.md#gada0398d757eab28d16a129692c309f4d)enum [net\_verdict](group__net__core.md#ga8e5393f3bdd85491f221324e637c3896) [net\_if\_send\_data](group__net__if.md#gada0398d757eab28d16a129692c309f4d)(struct [net\_if](structnet__if.md) \*iface, struct [net\_pkt](structnet__pkt.md) \*pkt);

808

[ 816](group__net__if.md#gafa451f6118529d1d084704d00b2aae20)static inline const struct [net\_l2](structnet__l2.md) \*[net\_if\_l2](group__net__if.md#gafa451f6118529d1d084704d00b2aae20)(struct [net\_if](structnet__if.md) \*iface)

817{

818 if (!iface || !iface->[if\_dev](structnet__if.md#a0982ba2019cdaa7701162e60fdb2171e)) {

819 return NULL;

820 }

821

822 return iface->[if\_dev](structnet__if.md#a0982ba2019cdaa7701162e60fdb2171e)->[l2](structnet__if__dev.md#a85d713c62875f5fe9e3ec29773150797);

823}

824

[ 833](group__net__if.md#ga72ed21ca0cb220199f5a2070137c7fef)enum [net\_verdict](group__net__core.md#ga8e5393f3bdd85491f221324e637c3896) [net\_if\_recv\_data](group__net__if.md#ga72ed21ca0cb220199f5a2070137c7fef)(struct [net\_if](structnet__if.md) \*iface, struct [net\_pkt](structnet__pkt.md) \*pkt);

834

[ 842](group__net__if.md#ga3cad2d51fc9cc225619585e06e252db0)static inline void \*[net\_if\_l2\_data](group__net__if.md#ga3cad2d51fc9cc225619585e06e252db0)(struct [net\_if](structnet__if.md) \*iface)

843{

844 NET\_ASSERT(iface);

845 NET\_ASSERT(iface->[if\_dev](structnet__if.md#a0982ba2019cdaa7701162e60fdb2171e));

846

847 return iface->[if\_dev](structnet__if.md#a0982ba2019cdaa7701162e60fdb2171e)->[l2\_data](structnet__if__dev.md#a8fec6a7f612fc1268ef486d8bdebe018);

848}

849

[ 857](group__net__if.md#gaeb8c703f273bc07ae9bb7a0d8bfe6f3d)static inline const struct [device](structdevice.md) \*[net\_if\_get\_device](group__net__if.md#gaeb8c703f273bc07ae9bb7a0d8bfe6f3d)(struct [net\_if](structnet__if.md) \*iface)

858{

859 NET\_ASSERT(iface);

860 NET\_ASSERT(iface->[if\_dev](structnet__if.md#a0982ba2019cdaa7701162e60fdb2171e));

861

862 return iface->[if\_dev](structnet__if.md#a0982ba2019cdaa7701162e60fdb2171e)->[dev](structnet__if__dev.md#aab633a44f165f571910dc9fc9e131c50);

863}

864

[ 871](group__net__if.md#ga56c4d37edcea540be09ebcdf97265aed)void [net\_if\_queue\_tx](group__net__if.md#ga56c4d37edcea540be09ebcdf97265aed)(struct [net\_if](structnet__if.md) \*iface, struct [net\_pkt](structnet__pkt.md) \*pkt);

872

[ 880](group__net__if.md#ga6bfa5f84a2127bbad27a0a3b319526a1)static inline bool [net\_if\_is\_ip\_offloaded](group__net__if.md#ga6bfa5f84a2127bbad27a0a3b319526a1)(struct [net\_if](structnet__if.md) \*iface)

881{

882#if defined(CONFIG\_NET\_OFFLOAD)

883 return (iface != NULL && iface->[if\_dev](structnet__if.md#a0982ba2019cdaa7701162e60fdb2171e) != NULL &&

884 iface->[if\_dev](structnet__if.md#a0982ba2019cdaa7701162e60fdb2171e)->offload != NULL);

885#else

886 ARG\_UNUSED(iface);

887

888 return false;

889#endif

890}

891

[ 899](group__net__if.md#gaecedc93a6dab2c57fe686718ea4d78af)bool [net\_if\_is\_offloaded](group__net__if.md#gaecedc93a6dab2c57fe686718ea4d78af)(struct [net\_if](structnet__if.md) \*iface);

900

[ 908](group__net__if.md#ga520939e94620ca75475a71f153df6d4a)static inline struct net\_offload \*[net\_if\_offload](group__net__if.md#ga520939e94620ca75475a71f153df6d4a)(struct [net\_if](structnet__if.md) \*iface)

909{

910#if defined(CONFIG\_NET\_OFFLOAD)

911 NET\_ASSERT(iface);

912 NET\_ASSERT(iface->[if\_dev](structnet__if.md#a0982ba2019cdaa7701162e60fdb2171e));

913

914 return iface->[if\_dev](structnet__if.md#a0982ba2019cdaa7701162e60fdb2171e)->offload;

915#else

916 ARG\_UNUSED(iface);

917

918 return NULL;

919#endif

920}

921

[ 929](group__net__if.md#gaf308baf2241fa455b50b439b7fab3f1e)static inline bool [net\_if\_is\_socket\_offloaded](group__net__if.md#gaf308baf2241fa455b50b439b7fab3f1e)(struct [net\_if](structnet__if.md) \*iface)

930{

931#if defined(CONFIG\_NET\_SOCKETS\_OFFLOAD)

932 NET\_ASSERT(iface);

933 NET\_ASSERT(iface->[if\_dev](structnet__if.md#a0982ba2019cdaa7701162e60fdb2171e));

934

935 return (iface->[if\_dev](structnet__if.md#a0982ba2019cdaa7701162e60fdb2171e)->socket\_offload != NULL);

936#else

937 ARG\_UNUSED(iface);

938

939 return false;

940#endif

941}

942

[ 949](group__net__if.md#ga9db52875580115c743b1f35cd6c46796)static inline void [net\_if\_socket\_offload\_set](group__net__if.md#ga9db52875580115c743b1f35cd6c46796)(

950 struct [net\_if](structnet__if.md) \*iface, [net\_socket\_create\_t](group__net__if.md#gaef3dfe26195514aac625e9f22e399759) socket\_offload)

951{

952#if defined(CONFIG\_NET\_SOCKETS\_OFFLOAD)

953 NET\_ASSERT(iface);

954 NET\_ASSERT(iface->[if\_dev](structnet__if.md#a0982ba2019cdaa7701162e60fdb2171e));

955

956 iface->[if\_dev](structnet__if.md#a0982ba2019cdaa7701162e60fdb2171e)->socket\_offload = socket\_offload;

957#else

958 ARG\_UNUSED(iface);

959 ARG\_UNUSED(socket\_offload);

960#endif

961}

962

[ 970](group__net__if.md#gafb2bbaec96c4759d920b2866c0b3ef3a)static inline [net\_socket\_create\_t](group__net__if.md#gaef3dfe26195514aac625e9f22e399759) [net\_if\_socket\_offload](group__net__if.md#gafb2bbaec96c4759d920b2866c0b3ef3a)(struct [net\_if](structnet__if.md) \*iface)

971{

972#if defined(CONFIG\_NET\_SOCKETS\_OFFLOAD)

973 NET\_ASSERT(iface);

974 NET\_ASSERT(iface->[if\_dev](structnet__if.md#a0982ba2019cdaa7701162e60fdb2171e));

975

976 return iface->[if\_dev](structnet__if.md#a0982ba2019cdaa7701162e60fdb2171e)->socket\_offload;

977#else

978 ARG\_UNUSED(iface);

979

980 return NULL;

981#endif

982}

983

[ 991](group__net__if.md#ga467186e964bf721e14fed38392f21872)static inline struct [net\_linkaddr](structnet__linkaddr.md) \*[net\_if\_get\_link\_addr](group__net__if.md#ga467186e964bf721e14fed38392f21872)(struct [net\_if](structnet__if.md) \*iface)

992{

993 NET\_ASSERT(iface);

994 NET\_ASSERT(iface->[if\_dev](structnet__if.md#a0982ba2019cdaa7701162e60fdb2171e));

995

996 return &iface->[if\_dev](structnet__if.md#a0982ba2019cdaa7701162e60fdb2171e)->[link\_addr](structnet__if__dev.md#aac6d5d341ab520e6aac7f7b03737c197);

997}

998

[ 1006](group__net__if.md#gae271e0e4dcb031a83d9908e597a45048)static inline struct [net\_if\_config](structnet__if__config.md) \*[net\_if\_get\_config](group__net__if.md#gae271e0e4dcb031a83d9908e597a45048)(struct [net\_if](structnet__if.md) \*iface)

1007{

1008 NET\_ASSERT(iface);

1009

1010 return &iface->[config](structnet__if.md#a5e71962f55bdead7bfbbb96518c6c404);

1011}

1012

1018#if defined(CONFIG\_NET\_IPV6\_DAD) && defined(CONFIG\_NET\_NATIVE\_IPV6)

1019void [net\_if\_start\_dad](group__net__if.md#ga9655c010ccbf989e9328271f5dbcc685)(struct [net\_if](structnet__if.md) \*iface);

1020#else

[ 1021](group__net__if.md#ga9655c010ccbf989e9328271f5dbcc685)static inline void [net\_if\_start\_dad](group__net__if.md#ga9655c010ccbf989e9328271f5dbcc685)(struct [net\_if](structnet__if.md) \*iface)

1022{

1023 ARG\_UNUSED(iface);

1024}

1025#endif

1026

[ 1032](group__net__if.md#gab9bdb7f8a9eeed4d9b70965b8af82cb7)void [net\_if\_start\_rs](group__net__if.md#gab9bdb7f8a9eeed4d9b70965b8af82cb7)(struct [net\_if](structnet__if.md) \*iface);

1033

1034

1040#if defined(CONFIG\_NET\_IPV6\_ND) && defined(CONFIG\_NET\_NATIVE\_IPV6)

1041void [net\_if\_stop\_rs](group__net__if.md#gab0195bb2151a1ba722a0b11d81066988)(struct [net\_if](structnet__if.md) \*iface);

1042#else

[ 1043](group__net__if.md#gab0195bb2151a1ba722a0b11d81066988)static inline void [net\_if\_stop\_rs](group__net__if.md#gab0195bb2151a1ba722a0b11d81066988)(struct [net\_if](structnet__if.md) \*iface)

1044{

1045 ARG\_UNUSED(iface);

1046}

1047#endif /\* CONFIG\_NET\_IPV6\_ND \*/

1048

1050

1051static inline int net\_if\_set\_link\_addr\_unlocked(struct [net\_if](structnet__if.md) \*iface,

1052 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) len,

1053 enum [net\_link\_type](group__net__linkaddr.md#ga1312c2322bc4a4f1c3b76d6466806b24) type)

1054{

1055 if ([net\_if\_flag\_is\_set](group__net__if.md#gae1f373ddd61c18a81481d8ddcfb12543)(iface, [NET\_IF\_RUNNING](group__net__if.md#ggae691e5537917ffce27ad0db82c730371add3e2ecdcd5de3154f9bd2836428a25a))) {

1056 return -[EPERM](group__system__errno.md#gadd669d31505a077f769cff8e66c780b3);

1057 }

1058

1059 [net\_if\_get\_link\_addr](group__net__if.md#ga467186e964bf721e14fed38392f21872)(iface)->[addr](structnet__linkaddr.md#a2176a9f7a444ac3b0108102d8cf852f0) = addr;

1060 [net\_if\_get\_link\_addr](group__net__if.md#ga467186e964bf721e14fed38392f21872)(iface)->[len](structnet__linkaddr.md#a7b2f8ebe68b557eb9cbb4c2f2ecd70e0) = len;

1061 [net\_if\_get\_link\_addr](group__net__if.md#ga467186e964bf721e14fed38392f21872)(iface)->[type](structnet__linkaddr.md#a5f5b4c3d353261d0fab8011aa09f00d7) = type;

1062

1063 [net\_hostname\_set\_postfix](group__net__hostname.md#ga6aa3799b3b0d7eec7fb8b276485ae2c5)(addr, len);

1064

1065 return 0;

1066}

1067

1068int net\_if\_set\_link\_addr\_locked(struct [net\_if](structnet__if.md) \*iface,

1069 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) len,

1070 enum [net\_link\_type](group__net__linkaddr.md#ga1312c2322bc4a4f1c3b76d6466806b24) type);

1072

[ 1084](group__net__if.md#ga52b41b2f8b7d3405338a0539542677a0)static inline int [net\_if\_set\_link\_addr](group__net__if.md#ga52b41b2f8b7d3405338a0539542677a0)(struct [net\_if](structnet__if.md) \*iface,

1085 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) len,

1086 enum [net\_link\_type](group__net__linkaddr.md#ga1312c2322bc4a4f1c3b76d6466806b24) type)

1087{

1088#if defined(CONFIG\_NET\_RAW\_MODE)

1089 return net\_if\_set\_link\_addr\_unlocked(iface, addr, len, type);

1090#else

1091 return net\_if\_set\_link\_addr\_locked(iface, addr, len, type);

1092#endif

1093}

1094

[ 1102](group__net__if.md#gacddc98531c5748db5a34f5c3a3e96e86)static inline [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [net\_if\_get\_mtu](group__net__if.md#gacddc98531c5748db5a34f5c3a3e96e86)(struct [net\_if](structnet__if.md) \*iface)

1103{

1104 if (iface == NULL) {

1105 return 0U;

1106 }

1107

1108 NET\_ASSERT(iface->[if\_dev](structnet__if.md#a0982ba2019cdaa7701162e60fdb2171e));

1109

1110 return iface->[if\_dev](structnet__if.md#a0982ba2019cdaa7701162e60fdb2171e)->[mtu](structnet__if__dev.md#aa15ccca2eb67b8d2afca153ccacb3742);

1111}

1112

[ 1119](group__net__if.md#ga76b140c6fc39b94ff4102e08e3a58e81)static inline void [net\_if\_set\_mtu](group__net__if.md#ga76b140c6fc39b94ff4102e08e3a58e81)(struct [net\_if](structnet__if.md) \*iface,

1120 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mtu)

1121{

1122 if (iface == NULL) {

1123 return;

1124 }

1125

1126 NET\_ASSERT(iface->[if\_dev](structnet__if.md#a0982ba2019cdaa7701162e60fdb2171e));

1127

1128 iface->[if\_dev](structnet__if.md#a0982ba2019cdaa7701162e60fdb2171e)->[mtu](structnet__if__dev.md#aa15ccca2eb67b8d2afca153ccacb3742) = mtu;

1129}

1130

[ 1137](group__net__if.md#gae66f6e7bd31545e6161fcd4600fe5842)static inline void [net\_if\_addr\_set\_lf](group__net__if.md#gae66f6e7bd31545e6161fcd4600fe5842)(struct [net\_if\_addr](structnet__if__addr.md) \*ifaddr,

1138 bool is\_infinite)

1139{

1140 NET\_ASSERT(ifaddr);

1141

1142 ifaddr->[is\_infinite](structnet__if__addr.md#a6e799428eb0633a25e4dc3c55e3a3b8c) = is\_infinite;

1143}

1144

[ 1152](group__net__if.md#ga1b058361dc9bcac7d842bb49846a0c79)struct [net\_if](structnet__if.md) \*[net\_if\_get\_by\_link\_addr](group__net__if.md#ga1b058361dc9bcac7d842bb49846a0c79)(struct [net\_linkaddr](structnet__linkaddr.md) \*ll\_addr);

1153

[ 1161](group__net__if.md#gadbb8be32caa896bdcdeee19425134827)struct [net\_if](structnet__if.md) \*[net\_if\_lookup\_by\_dev](group__net__if.md#gadbb8be32caa896bdcdeee19425134827)(const struct [device](structdevice.md) \*dev);

1162

[ 1170](group__net__if.md#gae2323a72714e29836d8296dfc330f7fd)static inline struct [net\_if\_config](structnet__if__config.md) \*[net\_if\_config\_get](group__net__if.md#gae2323a72714e29836d8296dfc330f7fd)(struct [net\_if](structnet__if.md) \*iface)

1171{

1172 NET\_ASSERT(iface);

1173

1174 return &iface->[config](structnet__if.md#a5e71962f55bdead7bfbbb96518c6c404);

1175}

1176

[ 1182](group__net__if.md#gadc87242eb7205362a308b3c4437bf76d)void [net\_if\_router\_rm](group__net__if.md#gadc87242eb7205362a308b3c4437bf76d)(struct [net\_if\_router](structnet__if__router.md) \*router);

1183

[ 1189](group__net__if.md#ga0a1f27ec893e1af3c97f130be4616589)void [net\_if\_set\_default](group__net__if.md#ga0a1f27ec893e1af3c97f130be4616589)(struct [net\_if](structnet__if.md) \*iface);

1190

[ 1196](group__net__if.md#ga55214771e462cbd4930ffa738813cb87)struct [net\_if](structnet__if.md) \*[net\_if\_get\_default](group__net__if.md#ga55214771e462cbd4930ffa738813cb87)(void);

1197

[ 1206](group__net__if.md#ga762337e8b66874a0fbf59bdbeba173f5)struct [net\_if](structnet__if.md) \*[net\_if\_get\_first\_by\_type](group__net__if.md#ga762337e8b66874a0fbf59bdbeba173f5)(const struct [net\_l2](structnet__l2.md) \*l2);

1207

[ 1214](group__net__if.md#ga03d8c6aebb1412382a9eec636c227238)struct [net\_if](structnet__if.md) \*[net\_if\_get\_first\_up](group__net__if.md#ga03d8c6aebb1412382a9eec636c227238)(void);

1215

1216#if defined(CONFIG\_NET\_L2\_IEEE802154)

1223static inline struct [net\_if](structnet__if.md) \*net\_if\_get\_ieee802154(void)

1224{

1225 return [net\_if\_get\_first\_by\_type](group__net__if.md#ga762337e8b66874a0fbf59bdbeba173f5)(&NET\_L2\_GET\_NAME(IEEE802154));

1226}

1227#endif /\* CONFIG\_NET\_L2\_IEEE802154 \*/

1228

[ 1239](group__net__if.md#ga56c9aef19bc9827d9ec96c00e10840fa)int [net\_if\_config\_ipv6\_get](group__net__if.md#ga56c9aef19bc9827d9ec96c00e10840fa)(struct [net\_if](structnet__if.md) \*iface,

1240 struct [net\_if\_ipv6](structnet__if__ipv6.md) \*\*ipv6);

1241

[ 1249](group__net__if.md#ga8af1400b354c42a64795cdb1a600ddd6)int [net\_if\_config\_ipv6\_put](group__net__if.md#ga8af1400b354c42a64795cdb1a600ddd6)(struct [net\_if](structnet__if.md) \*iface);

1250

[ 1259](group__net__if.md#ga13b5a26fc672d15697f99e85543184bb)struct [net\_if\_addr](structnet__if__addr.md) \*[net\_if\_ipv6\_addr\_lookup](group__net__if.md#ga13b5a26fc672d15697f99e85543184bb)(const struct [in6\_addr](structin6__addr.md) \*addr,

1260 struct [net\_if](structnet__if.md) \*\*iface);

1261

[ 1270](group__net__if.md#gab53eabb540a4487d83f27c8e319c736a)struct [net\_if\_addr](structnet__if__addr.md) \*[net\_if\_ipv6\_addr\_lookup\_by\_iface](group__net__if.md#gab53eabb540a4487d83f27c8e319c736a)(struct [net\_if](structnet__if.md) \*iface,

1271 struct [in6\_addr](structin6__addr.md) \*addr);

1272

[ 1281](group__net__if.md#ga1527872e5285790d50028a183608ac02)\_\_syscall int [net\_if\_ipv6\_addr\_lookup\_by\_index](group__net__if.md#ga1527872e5285790d50028a183608ac02)(const struct [in6\_addr](structin6__addr.md) \*addr);

1282

[ 1293](group__net__if.md#gae00484a7fe32671a4ca04ff525e640c6)struct [net\_if\_addr](structnet__if__addr.md) \*[net\_if\_ipv6\_addr\_add](group__net__if.md#gae00484a7fe32671a4ca04ff525e640c6)(struct [net\_if](structnet__if.md) \*iface,

1294 struct [in6\_addr](structin6__addr.md) \*addr,

1295 enum [net\_addr\_type](group__ip__4__6.md#gafecee2d4a331dc85ad962b81a6303e41) [addr\_type](structnet__if__addr.md#ab4fd41001cc24615803bfabb9d48e7eb),

1296 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) vlifetime);

1297

[ 1308](group__net__if.md#ga980bffb649ed48775bdc6cb2a0caef15)\_\_syscall bool [net\_if\_ipv6\_addr\_add\_by\_index](group__net__if.md#ga980bffb649ed48775bdc6cb2a0caef15)(int index,

1309 struct [in6\_addr](structin6__addr.md) \*addr,

1310 enum [net\_addr\_type](group__ip__4__6.md#gafecee2d4a331dc85ad962b81a6303e41) [addr\_type](structnet__if__addr.md#ab4fd41001cc24615803bfabb9d48e7eb),

1311 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) vlifetime);

1312

[ 1319](group__net__if.md#gaef8a6752a201f81636c4ffc1ebba4a25)void [net\_if\_ipv6\_addr\_update\_lifetime](group__net__if.md#gaef8a6752a201f81636c4ffc1ebba4a25)(struct [net\_if\_addr](structnet__if__addr.md) \*ifaddr,

1320 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) vlifetime);

1321

[ 1330](group__net__if.md#ga614e1458fa28d26c26f447e9fbcc2cb7)bool [net\_if\_ipv6\_addr\_rm](group__net__if.md#ga614e1458fa28d26c26f447e9fbcc2cb7)(struct [net\_if](structnet__if.md) \*iface, const struct [in6\_addr](structin6__addr.md) \*addr);

1331

[ 1340](group__net__if.md#gac159e3b0fbf558d5fb09774141da7d6d)\_\_syscall bool [net\_if\_ipv6\_addr\_rm\_by\_index](group__net__if.md#gac159e3b0fbf558d5fb09774141da7d6d)(int index,

1341 const struct [in6\_addr](structin6__addr.md) \*addr);

1342

[ 1351](group__net__if.md#gab58d8561a4f21899e2db34043d346516)typedef void (\*[net\_if\_ip\_addr\_cb\_t](group__net__if.md#gab58d8561a4f21899e2db34043d346516))(struct [net\_if](structnet__if.md) \*iface,

1352 struct [net\_if\_addr](structnet__if__addr.md) \*addr,

1353 void \*user\_data);

1354

[ 1363](group__net__if.md#ga5ac646ad7fda0fa48e78c15b4ca52d50)void [net\_if\_ipv6\_addr\_foreach](group__net__if.md#ga5ac646ad7fda0fa48e78c15b4ca52d50)(struct [net\_if](structnet__if.md) \*iface, [net\_if\_ip\_addr\_cb\_t](group__net__if.md#gab58d8561a4f21899e2db34043d346516) cb,

1364 void \*user\_data);

1365

[ 1374](group__net__if.md#ga7ae82a491193dfea9b92cb9cbaf26f98)struct [net\_if\_mcast\_addr](structnet__if__mcast__addr.md) \*[net\_if\_ipv6\_maddr\_add](group__net__if.md#ga7ae82a491193dfea9b92cb9cbaf26f98)(struct [net\_if](structnet__if.md) \*iface,

1375 const struct [in6\_addr](structin6__addr.md) \*addr);

1376

[ 1385](group__net__if.md#gaf0ce126bb5019ff5f5ff0876b9712ad9)bool [net\_if\_ipv6\_maddr\_rm](group__net__if.md#gaf0ce126bb5019ff5f5ff0876b9712ad9)(struct [net\_if](structnet__if.md) \*iface, const struct [in6\_addr](structin6__addr.md) \*addr);

1386

[ 1397](group__net__if.md#gadb4031153c4fef86110879befa6b9975)struct [net\_if\_mcast\_addr](structnet__if__mcast__addr.md) \*[net\_if\_ipv6\_maddr\_lookup](group__net__if.md#gadb4031153c4fef86110879befa6b9975)(const struct [in6\_addr](structin6__addr.md) \*addr,

1398 struct [net\_if](structnet__if.md) \*\*iface);

1399

[ 1410](group__net__if.md#ga0d64291573740a67eae7ff3fcc0910c5)typedef void (\*[net\_if\_mcast\_callback\_t](group__net__if.md#ga0d64291573740a67eae7ff3fcc0910c5))(struct [net\_if](structnet__if.md) \*iface,

1411 const struct net\_addr \*addr,

1412 bool is\_joined);

1413

[ 1422](structnet__if__mcast__monitor.md)struct [net\_if\_mcast\_monitor](structnet__if__mcast__monitor.md) {

[ 1424](structnet__if__mcast__monitor.md#a570b7d8a8a5fabca83982a5f7d1d896a) [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) [node](structnet__if__mcast__monitor.md#a570b7d8a8a5fabca83982a5f7d1d896a);

1425

[ 1427](structnet__if__mcast__monitor.md#af4d0e937b2b9161918a13a0d6723c60a) struct [net\_if](structnet__if.md) \*[iface](structnet__if__mcast__monitor.md#af4d0e937b2b9161918a13a0d6723c60a);

1428

[ 1430](structnet__if__mcast__monitor.md#aec441b858a5f6792ac9cdbc625f6babe) [net\_if\_mcast\_callback\_t](group__net__if.md#ga0d64291573740a67eae7ff3fcc0910c5) [cb](structnet__if__mcast__monitor.md#aec441b858a5f6792ac9cdbc625f6babe);

1431};

1432

[ 1441](group__net__if.md#ga8fdd0665ed76db6055777e395ca60255)void [net\_if\_mcast\_mon\_register](group__net__if.md#ga8fdd0665ed76db6055777e395ca60255)(struct [net\_if\_mcast\_monitor](structnet__if__mcast__monitor.md) \*mon,

1442 struct [net\_if](structnet__if.md) \*iface,

1443 [net\_if\_mcast\_callback\_t](group__net__if.md#ga0d64291573740a67eae7ff3fcc0910c5) cb);

1444

[ 1450](group__net__if.md#gad323732fe3d178a5dfdf0900e5cb5683)void [net\_if\_mcast\_mon\_unregister](group__net__if.md#gad323732fe3d178a5dfdf0900e5cb5683)(struct [net\_if\_mcast\_monitor](structnet__if__mcast__monitor.md) \*mon);

1451

[ 1459](group__net__if.md#ga372ef131263269cd65586d87997df745)void [net\_if\_mcast\_monitor](group__net__if.md#ga372ef131263269cd65586d87997df745)(struct [net\_if](structnet__if.md) \*iface, const struct net\_addr \*addr,

1460 bool is\_joined);

1461

[ 1468](group__net__if.md#ga49dbc954015307222f176f4149829b76)void [net\_if\_ipv6\_maddr\_join](group__net__if.md#ga49dbc954015307222f176f4149829b76)(struct [net\_if](structnet__if.md) \*iface,

1469 struct [net\_if\_mcast\_addr](structnet__if__mcast__addr.md) \*addr);

1470

[ 1478](group__net__if.md#gabe2c16a378a35a22d008bff9142e5449)static inline bool [net\_if\_ipv6\_maddr\_is\_joined](group__net__if.md#gabe2c16a378a35a22d008bff9142e5449)(struct [net\_if\_mcast\_addr](structnet__if__mcast__addr.md) \*addr)

1479{

1480 NET\_ASSERT(addr);

1481

1482 return addr->[is\_joined](structnet__if__mcast__addr.md#a4af9009b2f9ccc0589a9ba6dac10927b);

1483}

1484

[ 1491](group__net__if.md#gad24d5537d52de9781a7a6a55ceedd92b)void [net\_if\_ipv6\_maddr\_leave](group__net__if.md#gad24d5537d52de9781a7a6a55ceedd92b)(struct [net\_if](structnet__if.md) \*iface,

1492 struct [net\_if\_mcast\_addr](structnet__if__mcast__addr.md) \*addr);

1493

[ 1502](group__net__if.md#ga57ee087a53b59381ecb739a62e0e17d0)struct [net\_if\_ipv6\_prefix](structnet__if__ipv6__prefix.md) \*[net\_if\_ipv6\_prefix\_get](group__net__if.md#ga57ee087a53b59381ecb739a62e0e17d0)(struct [net\_if](structnet__if.md) \*[iface](structnet__if__ipv6__prefix.md#a0e2d1997e2ccfe1e1af5f16e0c74ed92),

1503 struct [in6\_addr](structin6__addr.md) \*addr);

1504

[ 1514](group__net__if.md#gaaf9af457b97c0d432b6f9f9fdd184834)struct [net\_if\_ipv6\_prefix](structnet__if__ipv6__prefix.md) \*[net\_if\_ipv6\_prefix\_lookup](group__net__if.md#gaaf9af457b97c0d432b6f9f9fdd184834)(struct [net\_if](structnet__if.md) \*[iface](structnet__if__ipv6__prefix.md#a0e2d1997e2ccfe1e1af5f16e0c74ed92),

1515 struct [in6\_addr](structin6__addr.md) \*addr,

1516 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [len](structnet__if__ipv6__prefix.md#a4d2bc2acbe51256b76cf4d3ced3aac39));

1517

[ 1528](group__net__if.md#ga2f0c98b16b090d9aea07941c64cbe035)struct [net\_if\_ipv6\_prefix](structnet__if__ipv6__prefix.md) \*[net\_if\_ipv6\_prefix\_add](group__net__if.md#ga2f0c98b16b090d9aea07941c64cbe035)(struct [net\_if](structnet__if.md) \*[iface](structnet__if__ipv6__prefix.md#a0e2d1997e2ccfe1e1af5f16e0c74ed92),

1529 struct [in6\_addr](structin6__addr.md) \*[prefix](structnet__if__ipv6__prefix.md#a65b450d0942b3c96cfc575b462d82028),

1530 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [len](structnet__if__ipv6__prefix.md#a4d2bc2acbe51256b76cf4d3ced3aac39),

1531 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [lifetime](structnet__if__ipv6__prefix.md#a925a97a49d383bd4ce475f5d09fcb7e3));

1532

[ 1542](group__net__if.md#ga36f18c7a3ff1777006290170b726deed)bool [net\_if\_ipv6\_prefix\_rm](group__net__if.md#ga36f18c7a3ff1777006290170b726deed)(struct [net\_if](structnet__if.md) \*[iface](structnet__if__ipv6__prefix.md#a0e2d1997e2ccfe1e1af5f16e0c74ed92), struct [in6\_addr](structin6__addr.md) \*addr,

1543 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [len](structnet__if__ipv6__prefix.md#a4d2bc2acbe51256b76cf4d3ced3aac39));

1544

[ 1551](group__net__if.md#gaa3c711e814fb6a4e552b4ef723d0baa0)static inline void [net\_if\_ipv6\_prefix\_set\_lf](group__net__if.md#gaa3c711e814fb6a4e552b4ef723d0baa0)(struct [net\_if\_ipv6\_prefix](structnet__if__ipv6__prefix.md) \*[prefix](structnet__if__ipv6__prefix.md#a65b450d0942b3c96cfc575b462d82028),

1552 bool [is\_infinite](structnet__if__ipv6__prefix.md#a22090441b27bed06098679bf23b4e1e9))

1553{

1554 [prefix](structnet__if__ipv6__prefix.md#a65b450d0942b3c96cfc575b462d82028)->is\_infinite = [is\_infinite](structnet__if__ipv6__prefix.md#a22090441b27bed06098679bf23b4e1e9);

1555}

1556

[ 1563](group__net__if.md#ga68cffe343c518bad7f7f152e30f7f9ee)void [net\_if\_ipv6\_prefix\_set\_timer](group__net__if.md#ga68cffe343c518bad7f7f152e30f7f9ee)(struct [net\_if\_ipv6\_prefix](structnet__if__ipv6__prefix.md) \*[prefix](structnet__if__ipv6__prefix.md#a65b450d0942b3c96cfc575b462d82028),

1564 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [lifetime](structnet__if__ipv6__prefix.md#a925a97a49d383bd4ce475f5d09fcb7e3));

1565

[ 1571](group__net__if.md#ga2d68cb6dcfcffd3f87bbfb3dfce791ff)void [net\_if\_ipv6\_prefix\_unset\_timer](group__net__if.md#ga2d68cb6dcfcffd3f87bbfb3dfce791ff)(struct [net\_if\_ipv6\_prefix](structnet__if__ipv6__prefix.md) \*[prefix](structnet__if__ipv6__prefix.md#a65b450d0942b3c96cfc575b462d82028));

1572

[ 1583](group__net__if.md#ga25d6e2253c1d361553d478f7c948a28a)bool [net\_if\_ipv6\_addr\_onlink](group__net__if.md#ga25d6e2253c1d361553d478f7c948a28a)(struct [net\_if](structnet__if.md) \*\*[iface](structnet__if__ipv6__prefix.md#a0e2d1997e2ccfe1e1af5f16e0c74ed92), struct [in6\_addr](structin6__addr.md) \*addr);

1584

1591#if defined(CONFIG\_NET\_NATIVE\_IPV6)

1592static inline struct [in6\_addr](structin6__addr.md) \*[net\_if\_router\_ipv6](group__net__if.md#gadbf1538003473d448ff0808896b732a5)(struct [net\_if\_router](structnet__if__router.md) \*router)

1593{

1594 NET\_ASSERT(router);

1595

1596 return &router->[address](structnet__if__router.md#a86a2ca1b95e348acbde8ce90986b83db).in6\_addr;

1597}

1598#else

[ 1599](group__net__if.md#gadbf1538003473d448ff0808896b732a5)static inline struct [in6\_addr](structin6__addr.md) \*[net\_if\_router\_ipv6](group__net__if.md#gadbf1538003473d448ff0808896b732a5)(struct [net\_if\_router](structnet__if__router.md) \*router)

1600{

1601 static struct [in6\_addr](structin6__addr.md) addr;

1602

1603 ARG\_UNUSED(router);

1604

1605 return &addr;

1606}

1607#endif

1608

[ 1618](group__net__if.md#gacece4ee588082259b3b5cfcd5ac1d552)struct [net\_if\_router](structnet__if__router.md) \*[net\_if\_ipv6\_router\_lookup](group__net__if.md#gacece4ee588082259b3b5cfcd5ac1d552)(struct [net\_if](structnet__if.md) \*[iface](structnet__if__router.md#a03789aa0a40f7686b76616de0ca0401a),

1619 struct [in6\_addr](structin6__addr.md) \*addr);

1620

[ 1630](group__net__if.md#ga36dab2a8fd9120ebc9c8b18f1875ccfd)struct [net\_if\_router](structnet__if__router.md) \*[net\_if\_ipv6\_router\_find\_default](group__net__if.md#ga36dab2a8fd9120ebc9c8b18f1875ccfd)(struct [net\_if](structnet__if.md) \*[iface](structnet__if__router.md#a03789aa0a40f7686b76616de0ca0401a),

1631 struct [in6\_addr](structin6__addr.md) \*addr);

1632

[ 1639](group__net__if.md#gaadba4957802dc376ef011590c91c6af6)void [net\_if\_ipv6\_router\_update\_lifetime](group__net__if.md#gaadba4957802dc376ef011590c91c6af6)(struct [net\_if\_router](structnet__if__router.md) \*router,

1640 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [lifetime](structnet__if__router.md#a4b0d2ad8f225ab61022c10dfce3db199));

1641

[ 1651](group__net__if.md#ga9c766ed70ada6eb551ac6542d7ac1ca3)struct [net\_if\_router](structnet__if__router.md) \*[net\_if\_ipv6\_router\_add](group__net__if.md#ga9c766ed70ada6eb551ac6542d7ac1ca3)(struct [net\_if](structnet__if.md) \*[iface](structnet__if__router.md#a03789aa0a40f7686b76616de0ca0401a),

1652 struct [in6\_addr](structin6__addr.md) \*addr,

1653 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) router\_lifetime);

1654

[ 1662](group__net__if.md#ga1d108aa0b54c072e0aa9d0c049f02807)bool [net\_if\_ipv6\_router\_rm](group__net__if.md#ga1d108aa0b54c072e0aa9d0c049f02807)(struct [net\_if\_router](structnet__if__router.md) \*router);

1663

[ 1672](group__net__if.md#ga54b200a4c4f09678298bf1b8f5da2ea6)[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [net\_if\_ipv6\_get\_hop\_limit](group__net__if.md#ga54b200a4c4f09678298bf1b8f5da2ea6)(struct [net\_if](structnet__if.md) \*[iface](structnet__if__router.md#a03789aa0a40f7686b76616de0ca0401a));

1673

[ 1680](group__net__if.md#ga37b1d83f3ef7ab5996a86e7f7f3d9c72)void [net\_if\_ipv6\_set\_hop\_limit](group__net__if.md#ga37b1d83f3ef7ab5996a86e7f7f3d9c72)(struct [net\_if](structnet__if.md) \*[iface](structnet__if__router.md#a03789aa0a40f7686b76616de0ca0401a), [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) hop\_limit);

1681

1682/\* The old hop limit setter function is deprecated because the naming

1683 \* of it was incorrect. The API name was missing "\_if\_" so this function

1684 \* should not be used.

1685 \*/

1686\_\_deprecated

[ 1687](group__net__if.md#ga33e3bf9530e394fe0b40b1b29e413138)static inline void [net\_ipv6\_set\_hop\_limit](group__net__if.md#ga33e3bf9530e394fe0b40b1b29e413138)(struct [net\_if](structnet__if.md) \*[iface](structnet__if__router.md#a03789aa0a40f7686b76616de0ca0401a),

1688 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) hop\_limit)

1689{

1690 [net\_if\_ipv6\_set\_hop\_limit](group__net__if.md#ga37b1d83f3ef7ab5996a86e7f7f3d9c72)([iface](structnet__if__router.md#a03789aa0a40f7686b76616de0ca0401a), hop\_limit);

1691}

1692

[ 1701](group__net__if.md#ga95505542ecf92642a0b6f68f9dda5bf6)[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [net\_if\_ipv6\_get\_mcast\_hop\_limit](group__net__if.md#ga95505542ecf92642a0b6f68f9dda5bf6)(struct [net\_if](structnet__if.md) \*[iface](structnet__if__router.md#a03789aa0a40f7686b76616de0ca0401a));

1702

[ 1709](group__net__if.md#ga3792cb18e34693b3c49f6dbccda3cf61)void [net\_if\_ipv6\_set\_mcast\_hop\_limit](group__net__if.md#ga3792cb18e34693b3c49f6dbccda3cf61)(struct [net\_if](structnet__if.md) \*[iface](structnet__if__router.md#a03789aa0a40f7686b76616de0ca0401a), [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) hop\_limit);

1710

[ 1717](group__net__if.md#gab3939d735b660f8f02124df656ceba2c)static inline void [net\_if\_ipv6\_set\_base\_reachable\_time](group__net__if.md#gab3939d735b660f8f02124df656ceba2c)(struct [net\_if](structnet__if.md) \*[iface](structnet__if__router.md#a03789aa0a40f7686b76616de0ca0401a),

1718 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) reachable\_time)

1719{

1720#if defined(CONFIG\_NET\_NATIVE\_IPV6)

1721 NET\_ASSERT([iface](structnet__if__router.md#a03789aa0a40f7686b76616de0ca0401a));

1722

1723 if (![iface](structnet__if__router.md#a03789aa0a40f7686b76616de0ca0401a)->[config](structnet__if.md#a5e71962f55bdead7bfbbb96518c6c404).ip.ipv6) {

1724 return;

1725 }

1726

1727 [iface](structnet__if__router.md#a03789aa0a40f7686b76616de0ca0401a)->[config](structnet__if.md#a5e71962f55bdead7bfbbb96518c6c404).ip.ipv6->base\_reachable\_time = reachable\_time;

1728#endif

1729}

1730

[ 1738](group__net__if.md#ga9dd1f91edbb519a6a079f363c33efacf)static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [net\_if\_ipv6\_get\_reachable\_time](group__net__if.md#ga9dd1f91edbb519a6a079f363c33efacf)(struct [net\_if](structnet__if.md) \*[iface](structnet__if__router.md#a03789aa0a40f7686b76616de0ca0401a))

1739{

1740#if defined(CONFIG\_NET\_NATIVE\_IPV6)

1741 NET\_ASSERT([iface](structnet__if__router.md#a03789aa0a40f7686b76616de0ca0401a));

1742

1743 if (![iface](structnet__if__router.md#a03789aa0a40f7686b76616de0ca0401a)->[config](structnet__if.md#a5e71962f55bdead7bfbbb96518c6c404).ip.ipv6) {

1744 return 0;

1745 }

1746

1747 return [iface](structnet__if__router.md#a03789aa0a40f7686b76616de0ca0401a)->[config](structnet__if.md#a5e71962f55bdead7bfbbb96518c6c404).ip.ipv6->reachable\_time;

1748#else

1749 return 0;

1750#endif

1751}

1752

[ 1760](group__net__if.md#gab1861b5cefa73b4eefbb447cb1438cdc)[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [net\_if\_ipv6\_calc\_reachable\_time](group__net__if.md#gab1861b5cefa73b4eefbb447cb1438cdc)(struct [net\_if\_ipv6](structnet__if__ipv6.md) \*ipv6);

1761

[ 1768](group__net__if.md#ga8328266b870fd200660cb2becaab3de4)static inline void [net\_if\_ipv6\_set\_reachable\_time](group__net__if.md#ga8328266b870fd200660cb2becaab3de4)(struct [net\_if\_ipv6](structnet__if__ipv6.md) \*ipv6)

1769{

1770#if defined(CONFIG\_NET\_NATIVE\_IPV6)

1771 if (ipv6 == NULL) {

1772 return;

1773 }

1774

1775 ipv6->[reachable\_time](structnet__if__ipv6.md#af57b7dca189167f8cc757c4ed6b08f2f) = [net\_if\_ipv6\_calc\_reachable\_time](group__net__if.md#gab1861b5cefa73b4eefbb447cb1438cdc)(ipv6);

1776#endif

1777}

1778

[ 1785](group__net__if.md#gad74566e5a34f447d2ac63d2c0e82eeff)static inline void [net\_if\_ipv6\_set\_retrans\_timer](group__net__if.md#gad74566e5a34f447d2ac63d2c0e82eeff)(struct [net\_if](structnet__if.md) \*[iface](structnet__if__router.md#a03789aa0a40f7686b76616de0ca0401a),

1786 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) retrans\_timer)

1787{

1788#if defined(CONFIG\_NET\_NATIVE\_IPV6)

1789 NET\_ASSERT([iface](structnet__if__router.md#a03789aa0a40f7686b76616de0ca0401a));

1790

1791 if (![iface](structnet__if__router.md#a03789aa0a40f7686b76616de0ca0401a)->[config](structnet__if.md#a5e71962f55bdead7bfbbb96518c6c404).ip.ipv6) {

1792 return;

1793 }

1794

1795 [iface](structnet__if__router.md#a03789aa0a40f7686b76616de0ca0401a)->[config](structnet__if.md#a5e71962f55bdead7bfbbb96518c6c404).ip.ipv6->retrans\_timer = retrans\_timer;

1796#endif

1797}

1798

[ 1806](group__net__if.md#gaddbf5a6ba412e6bdb7e31568fe827bd0)static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [net\_if\_ipv6\_get\_retrans\_timer](group__net__if.md#gaddbf5a6ba412e6bdb7e31568fe827bd0)(struct [net\_if](structnet__if.md) \*[iface](structnet__if__router.md#a03789aa0a40f7686b76616de0ca0401a))

1807{

1808#if defined(CONFIG\_NET\_NATIVE\_IPV6)

1809 NET\_ASSERT([iface](structnet__if__router.md#a03789aa0a40f7686b76616de0ca0401a));

1810

1811 if (![iface](structnet__if__router.md#a03789aa0a40f7686b76616de0ca0401a)->[config](structnet__if.md#a5e71962f55bdead7bfbbb96518c6c404).ip.ipv6) {

1812 return 0;

1813 }

1814

1815 return [iface](structnet__if__router.md#a03789aa0a40f7686b76616de0ca0401a)->[config](structnet__if.md#a5e71962f55bdead7bfbbb96518c6c404).ip.ipv6->retrans\_timer;

1816#else

1817 return 0;

1818#endif

1819}

1820

1832#if defined(CONFIG\_NET\_NATIVE\_IPV6)

1833const struct [in6\_addr](structin6__addr.md) \*[net\_if\_ipv6\_select\_src\_addr](group__net__if.md#ga50689a1afdb37a7087bf47a12cc50438)(struct [net\_if](structnet__if.md) \*iface,

1834 const struct [in6\_addr](structin6__addr.md) \*dst);

1835#else

[ 1836](group__net__if.md#ga50689a1afdb37a7087bf47a12cc50438)static inline const struct [in6\_addr](structin6__addr.md) \*[net\_if\_ipv6\_select\_src\_addr](group__net__if.md#ga50689a1afdb37a7087bf47a12cc50438)(

1837 struct [net\_if](structnet__if.md) \*iface, const struct [in6\_addr](structin6__addr.md) \*dst)

1838{

1839 ARG\_UNUSED(iface);

1840 ARG\_UNUSED(dst);

1841

1842 return NULL;

1843}

1844#endif

1845

1855#if defined(CONFIG\_NET\_NATIVE\_IPV6)

1856struct [net\_if](structnet__if.md) \*[net\_if\_ipv6\_select\_src\_iface](group__net__if.md#gae1495ac9e743be54b8d90bd4ff4700ab)(const struct [in6\_addr](structin6__addr.md) \*dst);

1857#else

[ 1858](group__net__if.md#gae1495ac9e743be54b8d90bd4ff4700ab)static inline struct [net\_if](structnet__if.md) \*[net\_if\_ipv6\_select\_src\_iface](group__net__if.md#gae1495ac9e743be54b8d90bd4ff4700ab)(

1859 const struct [in6\_addr](structin6__addr.md) \*dst)

1860{

1861 ARG\_UNUSED(dst);

1862

1863 return NULL;

1864}

1865#endif

1866

[ 1876](group__net__if.md#gad6f3e1e349e281887352652f6f32274e)struct [in6\_addr](structin6__addr.md) \*[net\_if\_ipv6\_get\_ll](group__net__if.md#gad6f3e1e349e281887352652f6f32274e)(struct [net\_if](structnet__if.md) \*iface,

1877 enum [net\_addr\_state](group__ip__4__6.md#ga32e58fc83532ef57eeb6ff952f17288d) addr\_state);

1878

[ 1888](group__net__if.md#ga85b7a923d46d36ecd63f9930bd8970c4)struct [in6\_addr](structin6__addr.md) \*[net\_if\_ipv6\_get\_ll\_addr](group__net__if.md#ga85b7a923d46d36ecd63f9930bd8970c4)(enum [net\_addr\_state](group__ip__4__6.md#ga32e58fc83532ef57eeb6ff952f17288d) [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90),

1889 struct [net\_if](structnet__if.md) \*\*iface);

1890

[ 1898](group__net__if.md#ga1dd53d92f803cff3be4826ddfb6b7211)void [net\_if\_ipv6\_dad\_failed](group__net__if.md#ga1dd53d92f803cff3be4826ddfb6b7211)(struct [net\_if](structnet__if.md) \*iface, const struct [in6\_addr](structin6__addr.md) \*addr);

1899

[ 1911](group__net__if.md#gaca7d686c772deac13a027cc046333126)struct [in6\_addr](structin6__addr.md) \*[net\_if\_ipv6\_get\_global\_addr](group__net__if.md#gaca7d686c772deac13a027cc046333126)(enum [net\_addr\_state](group__ip__4__6.md#ga32e58fc83532ef57eeb6ff952f17288d) [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90),

1912 struct [net\_if](structnet__if.md) \*\*iface);

1913

[ 1924](group__net__if.md#ga3390e248249b28f2c80e2ca0bc79d236)int [net\_if\_config\_ipv4\_get](group__net__if.md#ga3390e248249b28f2c80e2ca0bc79d236)(struct [net\_if](structnet__if.md) \*iface,

1925 struct [net\_if\_ipv4](structnet__if__ipv4.md) \*\*ipv4);

1926

[ 1934](group__net__if.md#ga88c13a45617480a665c7f9f589ec8e10)int [net\_if\_config\_ipv4\_put](group__net__if.md#ga88c13a45617480a665c7f9f589ec8e10)(struct [net\_if](structnet__if.md) \*iface);

1935

[ 1943](group__net__if.md#ga7e1fd28dbcf1164d056296b4df782e64)[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [net\_if\_ipv4\_get\_ttl](group__net__if.md#ga7e1fd28dbcf1164d056296b4df782e64)(struct [net\_if](structnet__if.md) \*iface);

1944

[ 1951](group__net__if.md#ga5544374d7ebea26a239d561083f0203d)void [net\_if\_ipv4\_set\_ttl](group__net__if.md#ga5544374d7ebea26a239d561083f0203d)(struct [net\_if](structnet__if.md) \*iface, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ttl);

1952

[ 1960](group__net__if.md#ga71acb65b1988aab8cca9c9604c86231e)[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [net\_if\_ipv4\_get\_mcast\_ttl](group__net__if.md#ga71acb65b1988aab8cca9c9604c86231e)(struct [net\_if](structnet__if.md) \*iface);

1961

[ 1968](group__net__if.md#ga9452fef4f1309fb1a53a6a8b4f222377)void [net\_if\_ipv4\_set\_mcast\_ttl](group__net__if.md#ga9452fef4f1309fb1a53a6a8b4f222377)(struct [net\_if](structnet__if.md) \*iface, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ttl);

1969

[ 1978](group__net__if.md#ga04a8f21d173d51bdcc092b92ed949e53)struct [net\_if\_addr](structnet__if__addr.md) \*[net\_if\_ipv4\_addr\_lookup](group__net__if.md#ga04a8f21d173d51bdcc092b92ed949e53)(const struct [in\_addr](structin__addr.md) \*addr,

1979 struct [net\_if](structnet__if.md) \*\*iface);

1980

[ 1991](group__net__if.md#ga7190958f740cac56de3a13fe688b3b5d)struct [net\_if\_addr](structnet__if__addr.md) \*[net\_if\_ipv4\_addr\_add](group__net__if.md#ga7190958f740cac56de3a13fe688b3b5d)(struct [net\_if](structnet__if.md) \*iface,

1992 struct [in\_addr](structin__addr.md) \*addr,

1993 enum [net\_addr\_type](group__ip__4__6.md#gafecee2d4a331dc85ad962b81a6303e41) [addr\_type](structnet__if__addr.md#ab4fd41001cc24615803bfabb9d48e7eb),

1994 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) vlifetime);

1995

[ 2004](group__net__if.md#ga4433304d46b6559604486b828e7d9dec)bool [net\_if\_ipv4\_addr\_rm](group__net__if.md#ga4433304d46b6559604486b828e7d9dec)(struct [net\_if](structnet__if.md) \*iface, const struct [in\_addr](structin__addr.md) \*addr);

2005

[ 2014](group__net__if.md#ga0a22661727316517685afcd551e7b38e)\_\_syscall int [net\_if\_ipv4\_addr\_lookup\_by\_index](group__net__if.md#ga0a22661727316517685afcd551e7b38e)(const struct [in\_addr](structin__addr.md) \*addr);

2015

[ 2026](group__net__if.md#gad140a69cf510ad99a8a8c770bab95bc9)\_\_syscall bool [net\_if\_ipv4\_addr\_add\_by\_index](group__net__if.md#gad140a69cf510ad99a8a8c770bab95bc9)(int index,

2027 struct [in\_addr](structin__addr.md) \*addr,

2028 enum [net\_addr\_type](group__ip__4__6.md#gafecee2d4a331dc85ad962b81a6303e41) [addr\_type](structnet__if__addr.md#ab4fd41001cc24615803bfabb9d48e7eb),

2029 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) vlifetime);

2030

[ 2039](group__net__if.md#gac5bf15f948ab195cecce98d1b40bda37)\_\_syscall bool [net\_if\_ipv4\_addr\_rm\_by\_index](group__net__if.md#gac5bf15f948ab195cecce98d1b40bda37)(int index,

2040 const struct [in\_addr](structin__addr.md) \*addr);

2041

[ 2050](group__net__if.md#gaae71be476e27c178ebb21b0f183c2825)void [net\_if\_ipv4\_addr\_foreach](group__net__if.md#gaae71be476e27c178ebb21b0f183c2825)(struct [net\_if](structnet__if.md) \*iface, [net\_if\_ip\_addr\_cb\_t](group__net__if.md#gab58d8561a4f21899e2db34043d346516) cb,

2051 void \*user\_data);

2052

[ 2061](group__net__if.md#gaa43fa83711703f8737e50b639e11b16c)struct [net\_if\_mcast\_addr](structnet__if__mcast__addr.md) \*[net\_if\_ipv4\_maddr\_add](group__net__if.md#gaa43fa83711703f8737e50b639e11b16c)(struct [net\_if](structnet__if.md) \*iface,

2062 const struct [in\_addr](structin__addr.md) \*addr);

2063

[ 2072](group__net__if.md#ga1d9273e10ab089d0f02b2b17d10a9e60)bool [net\_if\_ipv4\_maddr\_rm](group__net__if.md#ga1d9273e10ab089d0f02b2b17d10a9e60)(struct [net\_if](structnet__if.md) \*iface, const struct [in\_addr](structin__addr.md) \*addr);

2073

[ 2084](group__net__if.md#gadc1514a0d6852de9dbce043bc99d4eb0)struct [net\_if\_mcast\_addr](structnet__if__mcast__addr.md) \*[net\_if\_ipv4\_maddr\_lookup](group__net__if.md#gadc1514a0d6852de9dbce043bc99d4eb0)(const struct [in\_addr](structin__addr.md) \*addr,

2085 struct [net\_if](structnet__if.md) \*\*iface);

2086

[ 2093](group__net__if.md#gae275a5e75817aa178d36f422573ad76a)void [net\_if\_ipv4\_maddr\_join](group__net__if.md#gae275a5e75817aa178d36f422573ad76a)(struct [net\_if](structnet__if.md) \*iface,

2094 struct [net\_if\_mcast\_addr](structnet__if__mcast__addr.md) \*addr);

2095

[ 2103](group__net__if.md#gaa30769fc8016f1a7496b3ede277d8d8a)static inline bool [net\_if\_ipv4\_maddr\_is\_joined](group__net__if.md#gaa30769fc8016f1a7496b3ede277d8d8a)(struct [net\_if\_mcast\_addr](structnet__if__mcast__addr.md) \*addr)

2104{

2105 NET\_ASSERT(addr);

2106

2107 return addr->[is\_joined](structnet__if__mcast__addr.md#a4af9009b2f9ccc0589a9ba6dac10927b);

2108}

2109

[ 2116](group__net__if.md#ga1408fe384736d20f36c035c10007113c)void [net\_if\_ipv4\_maddr\_leave](group__net__if.md#ga1408fe384736d20f36c035c10007113c)(struct [net\_if](structnet__if.md) \*iface,

2117 struct [net\_if\_mcast\_addr](structnet__if__mcast__addr.md) \*addr);

2118

2125#if defined(CONFIG\_NET\_NATIVE\_IPV4)

2126static inline struct [in\_addr](structin__addr.md) \*[net\_if\_router\_ipv4](group__net__if.md#ga2a48e13941c91ddb9bbc63d014729be1)(struct [net\_if\_router](structnet__if__router.md) \*router)

2127{

2128 NET\_ASSERT(router);

2129

2130 return &router->[address](structnet__if__router.md#a86a2ca1b95e348acbde8ce90986b83db).in\_addr;

2131}

2132#else

[ 2133](group__net__if.md#ga2a48e13941c91ddb9bbc63d014729be1)static inline struct [in\_addr](structin__addr.md) \*[net\_if\_router\_ipv4](group__net__if.md#ga2a48e13941c91ddb9bbc63d014729be1)(struct [net\_if\_router](structnet__if__router.md) \*router)

2134{

2135 static struct [in\_addr](structin__addr.md) addr;

2136

2137 ARG\_UNUSED(router);

2138

2139 return &addr;

2140}

2141#endif

2142

[ 2152](group__net__if.md#ga01f995b00248ad5da734e4d58a4353aa)struct [net\_if\_router](structnet__if__router.md) \*[net\_if\_ipv4\_router\_lookup](group__net__if.md#ga01f995b00248ad5da734e4d58a4353aa)(struct [net\_if](structnet__if.md) \*[iface](structnet__if__router.md#a03789aa0a40f7686b76616de0ca0401a),

2153 struct [in\_addr](structin__addr.md) \*addr);

2154

[ 2164](group__net__if.md#ga25672516d7f383807e7dd9ce5f46a94f)struct [net\_if\_router](structnet__if__router.md) \*[net\_if\_ipv4\_router\_find\_default](group__net__if.md#ga25672516d7f383807e7dd9ce5f46a94f)(struct [net\_if](structnet__if.md) \*[iface](structnet__if__router.md#a03789aa0a40f7686b76616de0ca0401a),

2165 struct [in\_addr](structin__addr.md) \*addr);

[ 2176](group__net__if.md#ga44984001411077c7a2ef68afb361b40f)struct [net\_if\_router](structnet__if__router.md) \*[net\_if\_ipv4\_router\_add](group__net__if.md#ga44984001411077c7a2ef68afb361b40f)(struct [net\_if](structnet__if.md) \*[iface](structnet__if__router.md#a03789aa0a40f7686b76616de0ca0401a),

2177 struct [in\_addr](structin__addr.md) \*addr,

2178 bool [is\_default](structnet__if__router.md#a34745207edcad2745d6ce311e2bf1894),

2179 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) router\_lifetime);

2180

[ 2188](group__net__if.md#ga6be14f5307bc63ce87ff0a3fad7c7f4d)bool [net\_if\_ipv4\_router\_rm](group__net__if.md#ga6be14f5307bc63ce87ff0a3fad7c7f4d)(struct [net\_if\_router](structnet__if__router.md) \*router);

2189

[ 2198](group__net__if.md#ga558b31e556a1a4b8d1e68a78f3f755ea)bool [net\_if\_ipv4\_addr\_mask\_cmp](group__net__if.md#ga558b31e556a1a4b8d1e68a78f3f755ea)(struct [net\_if](structnet__if.md) \*[iface](structnet__if__router.md#a03789aa0a40f7686b76616de0ca0401a),

2199 const struct [in\_addr](structin__addr.md) \*addr);

2200

[ 2209](group__net__if.md#ga8f93179138c1942bc1a099102a4314cf)bool [net\_if\_ipv4\_is\_addr\_bcast](group__net__if.md#ga8f93179138c1942bc1a099102a4314cf)(struct [net\_if](structnet__if.md) \*[iface](structnet__if__router.md#a03789aa0a40f7686b76616de0ca0401a),

2210 const struct [in\_addr](structin__addr.md) \*addr);

2211

2221#if defined(CONFIG\_NET\_NATIVE\_IPV4)

2222struct [net\_if](structnet__if.md) \*[net\_if\_ipv4\_select\_src\_iface](group__net__if.md#gafea1a35f452ad8168855852cbfdf0024)(const struct [in\_addr](structin__addr.md) \*dst);

2223#else

[ 2224](group__net__if.md#gafea1a35f452ad8168855852cbfdf0024)static inline struct [net\_if](structnet__if.md) \*[net\_if\_ipv4\_select\_src\_iface](group__net__if.md#gafea1a35f452ad8168855852cbfdf0024)(

2225 const struct [in\_addr](structin__addr.md) \*dst)

2226{

2227 ARG\_UNUSED(dst);

2228

2229 return NULL;

2230}

2231#endif

2232

2244#if defined(CONFIG\_NET\_NATIVE\_IPV4)

2245const struct [in\_addr](structin__addr.md) \*[net\_if\_ipv4\_select\_src\_addr](group__net__if.md#gad6ec091f61ba3055be60c77ce085522f)(struct [net\_if](structnet__if.md) \*iface,

2246 const struct [in\_addr](structin__addr.md) \*dst);

2247#else

[ 2248](group__net__if.md#gad6ec091f61ba3055be60c77ce085522f)static inline const struct [in\_addr](structin__addr.md) \*[net\_if\_ipv4\_select\_src\_addr](group__net__if.md#gad6ec091f61ba3055be60c77ce085522f)(

2249 struct [net\_if](structnet__if.md) \*iface, const struct [in\_addr](structin__addr.md) \*dst)

2250{

2251 ARG\_UNUSED(iface);

2252 ARG\_UNUSED(dst);

2253

2254 return NULL;

2255}

2256#endif

2257

[ 2267](group__net__if.md#gad2ffe8df3d5ccca5094daecf3b9a8508)struct [in\_addr](structin__addr.md) \*[net\_if\_ipv4\_get\_ll](group__net__if.md#gad2ffe8df3d5ccca5094daecf3b9a8508)(struct [net\_if](structnet__if.md) \*iface,

2268 enum [net\_addr\_state](group__ip__4__6.md#ga32e58fc83532ef57eeb6ff952f17288d) addr\_state);

2269

[ 2279](group__net__if.md#gad791780f25d19acfe49d5272eae2d019)struct [in\_addr](structin__addr.md) \*[net\_if\_ipv4\_get\_global\_addr](group__net__if.md#gad791780f25d19acfe49d5272eae2d019)(struct [net\_if](structnet__if.md) \*iface,

2280 enum [net\_addr\_state](group__ip__4__6.md#ga32e58fc83532ef57eeb6ff952f17288d) addr\_state);

2281

[ 2289](group__net__if.md#ga41aeb0e7c5f9bc837f7b2ec13401afd1)struct [in\_addr](structin__addr.md) [net\_if\_ipv4\_get\_netmask](group__net__if.md#ga41aeb0e7c5f9bc837f7b2ec13401afd1)(struct [net\_if](structnet__if.md) \*iface);

2290

[ 2297](group__net__if.md#gad599bd11663fefa7d785b9fc5d52caf0)void [net\_if\_ipv4\_set\_netmask](group__net__if.md#gad599bd11663fefa7d785b9fc5d52caf0)(struct [net\_if](structnet__if.md) \*iface,

2298 const struct [in\_addr](structin__addr.md) \*netmask);

2299

[ 2308](group__net__if.md#ga94f2d2e69548609dd329c7e6b21e8958)\_\_syscall bool [net\_if\_ipv4\_set\_netmask\_by\_index](group__net__if.md#ga94f2d2e69548609dd329c7e6b21e8958)(int index,

2309 const struct [in\_addr](structin__addr.md) \*netmask);

2310

[ 2317](group__net__if.md#ga310ccbd9b37629422ca8e32836362724)void [net\_if\_ipv4\_set\_gw](group__net__if.md#ga310ccbd9b37629422ca8e32836362724)(struct [net\_if](structnet__if.md) \*iface, const struct [in\_addr](structin__addr.md) \*gw);

2318

[ 2327](group__net__if.md#gadef49124c331817165475c69fb9104e0)\_\_syscall bool [net\_if\_ipv4\_set\_gw\_by\_index](group__net__if.md#gadef49124c331817165475c69fb9104e0)(int index, const struct [in\_addr](structin__addr.md) \*gw);

2328

[ 2339](group__net__if.md#ga001b1cdde5febcf3970848c7c185c81c)struct [net\_if](structnet__if.md) \*[net\_if\_select\_src\_iface](group__net__if.md#ga001b1cdde5febcf3970848c7c185c81c)(const struct [sockaddr](structsockaddr.md) \*dst);

2340

[ 2349](group__net__if.md#ga0f87d5753fcd7cce40ecd161e6c91078)typedef void (\*[net\_if\_link\_callback\_t](group__net__if.md#ga0f87d5753fcd7cce40ecd161e6c91078))(struct [net\_if](structnet__if.md) \*iface,

2350 struct [net\_linkaddr](structnet__linkaddr.md) \*dst,

2351 int status);

2352

[ 2361](structnet__if__link__cb.md)struct [net\_if\_link\_cb](structnet__if__link__cb.md) {

[ 2363](structnet__if__link__cb.md#accae7945a802c5b7fc36948b12a365ef) [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) [node](structnet__if__link__cb.md#accae7945a802c5b7fc36948b12a365ef);

2364

[ 2366](structnet__if__link__cb.md#a66092a22cba3dd69ac1a91c3522240bb) [net\_if\_link\_callback\_t](group__net__if.md#ga0f87d5753fcd7cce40ecd161e6c91078) [cb](structnet__if__link__cb.md#a66092a22cba3dd69ac1a91c3522240bb);

2367};

2368

[ 2375](group__net__if.md#gaa81b7d9ed8dc05da3391265dbc89b665)void [net\_if\_register\_link\_cb](group__net__if.md#gaa81b7d9ed8dc05da3391265dbc89b665)(struct [net\_if\_link\_cb](structnet__if__link__cb.md) \*link,

2376 [net\_if\_link\_callback\_t](group__net__if.md#ga0f87d5753fcd7cce40ecd161e6c91078) cb);

2377

[ 2383](group__net__if.md#ga6ba64fac6e8d846ae7be5990f49a8293)void [net\_if\_unregister\_link\_cb](group__net__if.md#ga6ba64fac6e8d846ae7be5990f49a8293)(struct [net\_if\_link\_cb](structnet__if__link__cb.md) \*link);

2384

[ 2392](group__net__if.md#gaaa64aa4391a85760bb2daf600ac4d898)void [net\_if\_call\_link\_cb](group__net__if.md#gaaa64aa4391a85760bb2daf600ac4d898)(struct [net\_if](structnet__if.md) \*iface, struct [net\_linkaddr](structnet__linkaddr.md) \*lladdr,

2393 int status);

2394

[ 2404](group__net__if.md#ga7743d516edec5b80215553699712a98b)bool [net\_if\_need\_calc\_rx\_checksum](group__net__if.md#ga7743d516edec5b80215553699712a98b)(struct [net\_if](structnet__if.md) \*iface);

2405

[ 2416](group__net__if.md#ga230228c3249838b8b847ecc1b4ee11aa)bool [net\_if\_need\_calc\_tx\_checksum](group__net__if.md#ga230228c3249838b8b847ecc1b4ee11aa)(struct [net\_if](structnet__if.md) \*iface);

2417

[ 2428](group__net__if.md#ga72708cdb7f133fe5d7edf819756c3516)\_\_syscall struct [net\_if](structnet__if.md) \*[net\_if\_get\_by\_index](group__net__if.md#ga72708cdb7f133fe5d7edf819756c3516)(int index);

2429

[ 2437](group__net__if.md#ga02445f6c61f0d29f56ac0ef59e025630)int [net\_if\_get\_by\_iface](group__net__if.md#ga02445f6c61f0d29f56ac0ef59e025630)(struct [net\_if](structnet__if.md) \*iface);

2438

[ 2446](group__net__if.md#gac48ab8e6337e7cf387af9b293f254a80)typedef void (\*[net\_if\_cb\_t](group__net__if.md#gac48ab8e6337e7cf387af9b293f254a80))(struct [net\_if](structnet__if.md) \*iface, void \*user\_data);

2447

[ 2455](group__net__if.md#ga96b198fd9df4a985b0dde84dd7152815)void [net\_if\_foreach](group__net__if.md#ga96b198fd9df4a985b0dde84dd7152815)([net\_if\_cb\_t](group__net__if.md#gac48ab8e6337e7cf387af9b293f254a80) cb, void \*user\_data);

2456

[ 2464](group__net__if.md#ga02644cc623fc7a8878c17d54984e4210)int [net\_if\_up](group__net__if.md#ga02644cc623fc7a8878c17d54984e4210)(struct [net\_if](structnet__if.md) \*iface);

2465

[ 2473](group__net__if.md#ga7e9b368d4abf9da5656140df70cfa334)static inline bool [net\_if\_is\_up](group__net__if.md#ga7e9b368d4abf9da5656140df70cfa334)(struct [net\_if](structnet__if.md) \*iface)

2474{

2475 NET\_ASSERT(iface);

2476

2477 return [net\_if\_flag\_is\_set](group__net__if.md#gae1f373ddd61c18a81481d8ddcfb12543)(iface, [NET\_IF\_UP](group__net__if.md#ggae691e5537917ffce27ad0db82c730371ab0ab7393d643354c46c3437d74c15840)) &&

2478 [net\_if\_flag\_is\_set](group__net__if.md#gae1f373ddd61c18a81481d8ddcfb12543)(iface, [NET\_IF\_RUNNING](group__net__if.md#ggae691e5537917ffce27ad0db82c730371add3e2ecdcd5de3154f9bd2836428a25a));

2479}

2480

[ 2488](group__net__if.md#ga2187650062d6139b9f4b81745a206803)int [net\_if\_down](group__net__if.md#ga2187650062d6139b9f4b81745a206803)(struct [net\_if](structnet__if.md) \*iface);

2489

[ 2497](group__net__if.md#ga099a484a654ad9af35d3212fc2c995b2)static inline bool [net\_if\_is\_admin\_up](group__net__if.md#ga099a484a654ad9af35d3212fc2c995b2)(struct [net\_if](structnet__if.md) \*iface)

2498{

2499 NET\_ASSERT(iface);

2500

2501 return [net\_if\_flag\_is\_set](group__net__if.md#gae1f373ddd61c18a81481d8ddcfb12543)(iface, [NET\_IF\_UP](group__net__if.md#ggae691e5537917ffce27ad0db82c730371ab0ab7393d643354c46c3437d74c15840));

2502}

2503

[ 2512](group__net__if.md#ga35e5db3a631ac9039f14d86e59fc0dcc)void [net\_if\_carrier\_on](group__net__if.md#ga35e5db3a631ac9039f14d86e59fc0dcc)(struct [net\_if](structnet__if.md) \*iface);

2513

[ 2522](group__net__if.md#ga6839941422a88c1f707ab70ea34df323)void [net\_if\_carrier\_off](group__net__if.md#ga6839941422a88c1f707ab70ea34df323)(struct [net\_if](structnet__if.md) \*iface);

2523

[ 2531](group__net__if.md#ga095554237016e563d76cfd602d1dae77)static inline bool [net\_if\_is\_carrier\_ok](group__net__if.md#ga095554237016e563d76cfd602d1dae77)(struct [net\_if](structnet__if.md) \*iface)

2532{

2533 NET\_ASSERT(iface);

2534

2535 return [net\_if\_flag\_is\_set](group__net__if.md#gae1f373ddd61c18a81481d8ddcfb12543)(iface, [NET\_IF\_LOWER\_UP](group__net__if.md#ggae691e5537917ffce27ad0db82c730371ab1a529826bad6b4bcd04185372f97d6d));

2536}

2537

[ 2548](group__net__if.md#ga89a3374d4bb116460a7b7c50a750b593)void [net\_if\_dormant\_on](group__net__if.md#ga89a3374d4bb116460a7b7c50a750b593)(struct [net\_if](structnet__if.md) \*iface);

2549

[ 2558](group__net__if.md#ga1c31fac887d944ac0a16aad70e889496)void [net\_if\_dormant\_off](group__net__if.md#ga1c31fac887d944ac0a16aad70e889496)(struct [net\_if](structnet__if.md) \*iface);

2559

[ 2567](group__net__if.md#ga6e2e6102271c37acaa59c54e2aa6b413)static inline bool [net\_if\_is\_dormant](group__net__if.md#ga6e2e6102271c37acaa59c54e2aa6b413)(struct [net\_if](structnet__if.md) \*iface)

2568{

2569 NET\_ASSERT(iface);

2570

2571 return [net\_if\_flag\_is\_set](group__net__if.md#gae1f373ddd61c18a81481d8ddcfb12543)(iface, [NET\_IF\_DORMANT](group__net__if.md#ggae691e5537917ffce27ad0db82c730371a7dd1db72a37b1fbc4c4491ce1c75238d));

2572}

2573

2574#if defined(CONFIG\_NET\_PKT\_TIMESTAMP) && defined(CONFIG\_NET\_NATIVE)

2582typedef void (\*net\_if\_timestamp\_callback\_t)(struct [net\_pkt](structnet__pkt.md) \*pkt);

2583

2592struct net\_if\_timestamp\_cb {

2594 [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) node;

2595

2599 struct net\_pkt \*pkt;

2600

2604 struct net\_if \*iface;

2605

2607 net\_if\_timestamp\_callback\_t cb;

2608};

2609

2620void net\_if\_register\_timestamp\_cb(struct net\_if\_timestamp\_cb \*handle,

2621 struct [net\_pkt](structnet__pkt.md) \*pkt,

2622 struct [net\_if](structnet__if.md) \*iface,

2623 net\_if\_timestamp\_callback\_t cb);

2624

2630void net\_if\_unregister\_timestamp\_cb(struct net\_if\_timestamp\_cb \*handle);

2631

2637void net\_if\_call\_timestamp\_cb(struct [net\_pkt](structnet__pkt.md) \*pkt);

2638

2639/\*

2640 \* @brief Add timestamped TX buffer to be handled

2641 \*

2642 \* @param pkt Timestamped buffer

2643 \*/

2644void net\_if\_add\_tx\_timestamp(struct [net\_pkt](structnet__pkt.md) \*pkt);

2645#endif /\* CONFIG\_NET\_PKT\_TIMESTAMP \*/

2646

2656#if defined(CONFIG\_NET\_PROMISCUOUS\_MODE)

2657int [net\_if\_set\_promisc](group__net__if.md#gaf9f81f3b9697ca47f7674d85f37a8d80)(struct [net\_if](structnet__if.md) \*iface);

2658#else

[ 2659](group__net__if.md#gaf9f81f3b9697ca47f7674d85f37a8d80)static inline int [net\_if\_set\_promisc](group__net__if.md#gaf9f81f3b9697ca47f7674d85f37a8d80)(struct [net\_if](structnet__if.md) \*iface)

2660{

2661 ARG\_UNUSED(iface);

2662

2663 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

2664}

2665#endif

2666

2672#if defined(CONFIG\_NET\_PROMISCUOUS\_MODE)

2673void [net\_if\_unset\_promisc](group__net__if.md#ga9c8212c087883510050ac6a39ef0a7bf)(struct [net\_if](structnet__if.md) \*iface);

2674#else

[ 2675](group__net__if.md#ga9c8212c087883510050ac6a39ef0a7bf)static inline void [net\_if\_unset\_promisc](group__net__if.md#ga9c8212c087883510050ac6a39ef0a7bf)(struct [net\_if](structnet__if.md) \*iface)

2676{

2677 ARG\_UNUSED(iface);

2678}

2679#endif

2680

2689#if defined(CONFIG\_NET\_PROMISCUOUS\_MODE)

2690bool [net\_if\_is\_promisc](group__net__if.md#ga9f1a6eab849517734ec422deb0ba71f5)(struct [net\_if](structnet__if.md) \*iface);

2691#else

[ 2692](group__net__if.md#ga9f1a6eab849517734ec422deb0ba71f5)static inline bool [net\_if\_is\_promisc](group__net__if.md#ga9f1a6eab849517734ec422deb0ba71f5)(struct [net\_if](structnet__if.md) \*iface)

2693{

2694 ARG\_UNUSED(iface);

2695

2696 return false;

2697}

2698#endif

2699

[ 2709](group__net__if.md#ga3cddda628eca248246f9aa3b81938f95)static inline bool [net\_if\_are\_pending\_tx\_packets](group__net__if.md#ga3cddda628eca248246f9aa3b81938f95)(struct [net\_if](structnet__if.md) \*iface)

2710{

2711#if defined(CONFIG\_NET\_POWER\_MANAGEMENT)

2712 return !!iface->tx\_pending;

2713#else

2714 ARG\_UNUSED(iface);

2715

2716 return false;

2717#endif

2718}

2719

2720#ifdef CONFIG\_NET\_POWER\_MANAGEMENT

2728int net\_if\_suspend(struct [net\_if](structnet__if.md) \*iface);

2729

2737int net\_if\_resume(struct [net\_if](structnet__if.md) \*iface);

2738

2746bool net\_if\_is\_suspended(struct [net\_if](structnet__if.md) \*iface);

2747#endif /\* CONFIG\_NET\_POWER\_MANAGEMENT \*/

2748

[ 2756](group__net__if.md#gaa458b5f349c55007108b47b99f4954d5)bool [net\_if\_is\_wifi](group__net__if.md#gaa458b5f349c55007108b47b99f4954d5)(struct [net\_if](structnet__if.md) \*iface);

2757

[ 2763](group__net__if.md#ga6e89bbafb6c0acdc6bf51078e2027236)struct [net\_if](structnet__if.md) \*[net\_if\_get\_first\_wifi](group__net__if.md#ga6e89bbafb6c0acdc6bf51078e2027236)(void);

2764

[ 2779](group__net__if.md#ga5f653cd73c1ecd548a931eb7fbd170f7)int [net\_if\_get\_name](group__net__if.md#ga5f653cd73c1ecd548a931eb7fbd170f7)(struct [net\_if](structnet__if.md) \*iface, char \*buf, int len);

2780

[ 2795](group__net__if.md#ga05dec64966fc39e3deb0679b9585688b)int [net\_if\_set\_name](group__net__if.md#ga05dec64966fc39e3deb0679b9585688b)(struct [net\_if](structnet__if.md) \*iface, const char \*buf);

2796

[ 2804](group__net__if.md#ga1774ac036032bb0dc2c662f6f4f66a7f)int [net\_if\_get\_by\_name](group__net__if.md#ga1774ac036032bb0dc2c662f6f4f66a7f)(const char \*name);

2805

2807struct net\_if\_api {

2808 void (\*init)(struct [net\_if](structnet__if.md) \*iface);

2809};

2810

2811#define NET\_IF\_DHCPV4\_INIT \

2812 IF\_ENABLED(UTIL\_AND(IS\_ENABLED(CONFIG\_NET\_DHCPV4), \

2813 IS\_ENABLED(CONFIG\_NET\_NATIVE\_IPV4)), \

2814 (.dhcpv4.state = NET\_DHCPV4\_DISABLED,))

2815

2816#define NET\_IF\_DHCPV6\_INIT \

2817 IF\_ENABLED(UTIL\_AND(IS\_ENABLED(CONFIG\_NET\_DHCPV6), \

2818 IS\_ENABLED(CONFIG\_NET\_NATIVE\_IPV6)), \

2819 (.dhcpv6.state = NET\_DHCPV6\_DISABLED,))

2820

2821#define NET\_IF\_CONFIG\_INIT \

2822 .config = { \

2823 IF\_ENABLED(CONFIG\_NET\_IP, (.ip = {},)) \

2824 NET\_IF\_DHCPV4\_INIT \

2825 NET\_IF\_DHCPV6\_INIT \

2826 }

2827

2828#define NET\_IF\_GET\_NAME(dev\_id, sfx) \_\_net\_if\_##dev\_id##\_##sfx

2829#define NET\_IF\_DEV\_GET\_NAME(dev\_id, sfx) \_\_net\_if\_dev\_##dev\_id##\_##sfx

2830

2831#define NET\_IF\_GET(dev\_id, sfx) \

2832 ((struct net\_if \*)&NET\_IF\_GET\_NAME(dev\_id, sfx))

2833

2834#define NET\_IF\_INIT(dev\_id, sfx, \_l2, \_mtu, \_num\_configs) \

2835 static STRUCT\_SECTION\_ITERABLE(net\_if\_dev, \

2836 NET\_IF\_DEV\_GET\_NAME(dev\_id, sfx)) = { \

2837 .dev = &(DEVICE\_NAME\_GET(dev\_id)), \

2838 .l2 = &(NET\_L2\_GET\_NAME(\_l2)), \

2839 .l2\_data = &(NET\_L2\_GET\_DATA(dev\_id, sfx)), \

2840 .mtu = \_mtu, \

2841 .flags = {BIT(NET\_IF\_LOWER\_UP)}, \

2842 }; \

2843 static Z\_DECL\_ALIGN(struct net\_if) \

2844 NET\_IF\_GET\_NAME(dev\_id, sfx)[\_num\_configs] \

2845 \_\_used \_\_in\_section(\_net\_if, static, \

2846 dev\_id) = { \

2847 [0 ... (\_num\_configs - 1)] = { \

2848 .if\_dev = &(NET\_IF\_DEV\_GET\_NAME(dev\_id, sfx)), \

2849 NET\_IF\_CONFIG\_INIT \

2850 } \

2851 }

2852

2853#define NET\_IF\_OFFLOAD\_INIT(dev\_id, sfx, \_mtu) \

2854 static STRUCT\_SECTION\_ITERABLE(net\_if\_dev, \

2855 NET\_IF\_DEV\_GET\_NAME(dev\_id, sfx)) = { \

2856 .dev = &(DEVICE\_NAME\_GET(dev\_id)), \

2857 .mtu = \_mtu, \

2858 .l2 = &(NET\_L2\_GET\_NAME(OFFLOADED\_NETDEV)), \

2859 .flags = {BIT(NET\_IF\_LOWER\_UP)}, \

2860 }; \

2861 static Z\_DECL\_ALIGN(struct net\_if) \

2862 NET\_IF\_GET\_NAME(dev\_id, sfx)[NET\_IF\_MAX\_CONFIGS] \

2863 \_\_used \_\_in\_section(\_net\_if, static, \

2864 dev\_id) = { \

2865 [0 ... (NET\_IF\_MAX\_CONFIGS - 1)] = { \

2866 .if\_dev = &(NET\_IF\_DEV\_GET\_NAME(dev\_id, sfx)), \

2867 NET\_IF\_CONFIG\_INIT \

2868 } \

2869 }

2870

2872

2873/\* Network device initialization macros \*/

2874

2875#define Z\_NET\_DEVICE\_INIT(node\_id, dev\_id, name, init\_fn, pm, data, \

2876 config, prio, api, l2, l2\_ctx\_type, mtu) \

2877 Z\_DEVICE\_STATE\_DEFINE(dev\_id); \

2878 Z\_DEVICE\_DEFINE(node\_id, dev\_id, name, init\_fn, pm, data, \

2879 config, POST\_KERNEL, prio, api, \

2880 &Z\_DEVICE\_STATE\_NAME(dev\_id)); \

2881 NET\_L2\_DATA\_INIT(dev\_id, 0, l2\_ctx\_type); \

2882 NET\_IF\_INIT(dev\_id, 0, l2, mtu, NET\_IF\_MAX\_CONFIGS)

2883

[ 2903](group__net__if.md#ga02971562c42494e2a5f71e1f8587e709)#define NET\_DEVICE\_INIT(dev\_id, name, init\_fn, pm, data, config, prio, \

2904 api, l2, l2\_ctx\_type, mtu) \

2905 Z\_NET\_DEVICE\_INIT(DT\_INVALID\_NODE, dev\_id, name, init\_fn, pm, \

2906 data, config, prio, api, l2, l2\_ctx\_type, mtu)

2907

[ 2926](group__net__if.md#gab1f762b01ae7bc37cd4a25724c123dda)#define NET\_DEVICE\_DT\_DEFINE(node\_id, init\_fn, pm, data, \

2927 config, prio, api, l2, l2\_ctx\_type, mtu) \

2928 Z\_NET\_DEVICE\_INIT(node\_id, Z\_DEVICE\_DT\_DEV\_ID(node\_id), \

2929 DEVICE\_DT\_NAME(node\_id), init\_fn, pm, data, \

2930 config, prio, api, l2, l2\_ctx\_type, mtu)

2931

[ 2940](group__net__if.md#ga7edd8bc59444d92cad0371c36f9949b7)#define NET\_DEVICE\_DT\_INST\_DEFINE(inst, ...) \

2941 NET\_DEVICE\_DT\_DEFINE(DT\_DRV\_INST(inst), \_\_VA\_ARGS\_\_)

2942

2943#define Z\_NET\_DEVICE\_INIT\_INSTANCE(node\_id, dev\_id, name, instance, \

2944 init\_fn, pm, data, config, prio, \

2945 api, l2, l2\_ctx\_type, mtu) \

2946 Z\_DEVICE\_STATE\_DEFINE(dev\_id); \

2947 Z\_DEVICE\_DEFINE(node\_id, dev\_id, name, init\_fn, pm, data, \

2948 config, POST\_KERNEL, prio, api, \

2949 &Z\_DEVICE\_STATE\_NAME(dev\_id)); \

2950 NET\_L2\_DATA\_INIT(dev\_id, instance, l2\_ctx\_type); \

2951 NET\_IF\_INIT(dev\_id, instance, l2, mtu, NET\_IF\_MAX\_CONFIGS)

2952

[ 2976](group__net__if.md#gacc7edecdd9de9920cc155977d8fec2a2)#define NET\_DEVICE\_INIT\_INSTANCE(dev\_id, name, instance, init\_fn, pm, \

2977 data, config, prio, api, l2, \

2978 l2\_ctx\_type, mtu) \

2979 Z\_NET\_DEVICE\_INIT\_INSTANCE(DT\_INVALID\_NODE, dev\_id, name, \

2980 instance, init\_fn, pm, data, config, \

2981 prio, api, l2, l2\_ctx\_type, mtu)

2982

[ 3005](group__net__if.md#ga50702b043a0791e59e7d5679dda1d9e8)#define NET\_DEVICE\_DT\_DEFINE\_INSTANCE(node\_id, instance, init\_fn, pm, \

3006 data, config, prio, api, l2, \

3007 l2\_ctx\_type, mtu) \

3008 Z\_NET\_DEVICE\_INIT\_INSTANCE(node\_id, \

3009 Z\_DEVICE\_DT\_DEV\_ID(node\_id), \

3010 DEVICE\_DT\_NAME(node\_id), instance, \

3011 init\_fn, pm, data, config, prio, \

3012 api, l2, l2\_ctx\_type, mtu)

3013

[ 3023](group__net__if.md#gabe4b8589996a53cbc50b76c8ea15aa0c)#define NET\_DEVICE\_DT\_INST\_DEFINE\_INSTANCE(inst, ...) \

3024 NET\_DEVICE\_DT\_DEFINE\_INSTANCE(DT\_DRV\_INST(inst), \_\_VA\_ARGS\_\_)

3025

3026#define Z\_NET\_DEVICE\_OFFLOAD\_INIT(node\_id, dev\_id, name, init\_fn, pm, \

3027 data, config, prio, api, mtu) \

3028 Z\_DEVICE\_STATE\_DEFINE(dev\_id); \

3029 Z\_DEVICE\_DEFINE(node\_id, dev\_id, name, init\_fn, pm, data, \

3030 config, POST\_KERNEL, prio, api, \

3031 &Z\_DEVICE\_STATE\_NAME(dev\_id)); \

3032 NET\_IF\_OFFLOAD\_INIT(dev\_id, 0, mtu)

3033

[ 3053](group__net__if.md#ga255672607b7958db3f464d2a57a7e635)#define NET\_DEVICE\_OFFLOAD\_INIT(dev\_id, name, init\_fn, pm, data, \

3054 config, prio, api, mtu) \

3055 Z\_NET\_DEVICE\_OFFLOAD\_INIT(DT\_INVALID\_NODE, dev\_id, name, \

3056 init\_fn, pm, data, config, prio, api, \

3057 mtu)

3058

[ 3077](group__net__if.md#gab2b287025e194dec1fab24e44d95362f)#define NET\_DEVICE\_DT\_OFFLOAD\_DEFINE(node\_id, init\_fn, pm, data, \

3078 config, prio, api, mtu) \

3079 Z\_NET\_DEVICE\_OFFLOAD\_INIT(node\_id, Z\_DEVICE\_DT\_DEV\_ID(node\_id), \

3080 DEVICE\_DT\_NAME(node\_id), init\_fn, pm, \

3081 data, config, prio, api, mtu)

3082

[ 3092](group__net__if.md#ga1cab6943a28e3d3754e36623834b93fd)#define NET\_DEVICE\_DT\_INST\_OFFLOAD\_DEFINE(inst, ...) \

3093 NET\_DEVICE\_DT\_OFFLOAD\_DEFINE(DT\_DRV\_INST(inst), \_\_VA\_ARGS\_\_)

3094

[ 3100](group__net__if.md#ga6c081875a6f5a848b3ad2fd220c63c3c)#define NET\_IFACE\_COUNT(\_dst) \

3101 do { \

3102 extern struct net\_if \_net\_if\_list\_start[]; \

3103 extern struct net\_if \_net\_if\_list\_end[]; \

3104 \*(\_dst) = ((uintptr\_t)\_net\_if\_list\_end - \

3105 (uintptr\_t)\_net\_if\_list\_start) / \

3106 sizeof(struct net\_if); \

3107 } while (0)

3108

3109#ifdef \_\_cplusplus

3110}

3111#endif

3112

3113#include <syscalls/net\_if.h>

3114

3118

3119#endif /\* ZEPHYR\_INCLUDE\_NET\_NET\_IF\_H\_ \*/

[k\_thread\_stack\_t](arch__interface_8h.md#a9fc2dce533bd7b8cb1fdd4bdbb2b62b1)

struct z\_thread\_stack\_element k\_thread\_stack\_t

Typedef of struct z\_thread\_stack\_element.

**Definition** arch\_interface.h:45

[device.h](device_8h.md)

[dhcpv4.h](dhcpv4_8h.md)

DHCPv4 Client Handler.

[dhcpv6.h](dhcpv6_8h.md)

DHCPv6 client.

[atomic\_set\_bit](group__atomic__apis.md#ga17a3961ba7610ad6e595e602f70344a0)

static void atomic\_set\_bit(atomic\_t \*target, int bit)

Atomically set a bit.

**Definition** atomic.h:209

[atomic\_test\_bit](group__atomic__apis.md#ga190ddc108f45e7649689753c08658eae)

static bool atomic\_test\_bit(const atomic\_t \*target, int bit)

Atomically test a bit.

**Definition** atomic.h:127

[atomic\_clear\_bit](group__atomic__apis.md#ga1c1693d524c49d11fd32b323a39d718e)

static void atomic\_clear\_bit(atomic\_t \*target, int bit)

Atomically clear a bit.

**Definition** atomic.h:191

[ATOMIC\_DEFINE](group__atomic__apis.md#ga249c575db9764486197709b327f7370e)

#define ATOMIC\_DEFINE(name, num\_bits)

Define an array of atomic variables.

**Definition** atomic.h:111

[atomic\_test\_and\_clear\_bit](group__atomic__apis.md#ga53159437721084da0ec8ee70ec212472)

static bool atomic\_test\_and\_clear\_bit(atomic\_t \*target, int bit)

Atomically test and clear a bit.

**Definition** atomic.h:147

[atomic\_test\_and\_set\_bit](group__atomic__apis.md#ga7ff45e13aa5f8be5d7a550e49f5c720b)

static bool atomic\_test\_and\_set\_bit(atomic\_t \*target, int bit)

Atomically set a bit.

**Definition** atomic.h:170

[K\_FOREVER](group__clock__apis.md#ga0bb4b83f0222193b21a8910311bab0ca)

#define K\_FOREVER

Generate infinite timeout delay.

**Definition** kernel.h:1361

[net\_addr\_state](group__ip__4__6.md#ga32e58fc83532ef57eeb6ff952f17288d)

net\_addr\_state

What is the current state of the network address.

**Definition** net\_ip.h:445

[net\_addr\_type](group__ip__4__6.md#gafecee2d4a331dc85ad962b81a6303e41)

net\_addr\_type

How the network address is assigned to network interface.

**Definition** net\_ip.h:453

[k\_mutex\_unlock](group__mutex__apis.md#ga360f4c0e7258b0d7030cdb1f452b2c31)

int k\_mutex\_unlock(struct k\_mutex \*mutex)

Unlock a mutex.

[k\_mutex\_lock](group__mutex__apis.md#ga850549358645249c285669baa49c33b0)

int k\_mutex\_lock(struct k\_mutex \*mutex, k\_timeout\_t timeout)

Lock a mutex.

[net\_verdict](group__net__core.md#ga8e5393f3bdd85491f221324e637c3896)

net\_verdict

Net Verdict.

**Definition** net\_core.h:98

[net\_hostname\_set\_postfix](group__net__hostname.md#ga6aa3799b3b0d7eec7fb8b276485ae2c5)

static int net\_hostname\_set\_postfix(const uint8\_t \*hostname\_postfix, int postfix\_len)

Set the device hostname postfix.

**Definition** hostname.h:103

[net\_if\_select\_src\_iface](group__net__if.md#ga001b1cdde5febcf3970848c7c185c81c)

struct net\_if \* net\_if\_select\_src\_iface(const struct sockaddr \*dst)

Get a network interface that should be used when sending IPv6 or IPv4 network data to destination.

[net\_if\_ipv4\_router\_lookup](group__net__if.md#ga01f995b00248ad5da734e4d58a4353aa)

struct net\_if\_router \* net\_if\_ipv4\_router\_lookup(struct net\_if \*iface, struct in\_addr \*addr)

Check if IPv4 address is one of the routers configured in the system.

[net\_if\_get\_by\_iface](group__net__if.md#ga02445f6c61f0d29f56ac0ef59e025630)

int net\_if\_get\_by\_iface(struct net\_if \*iface)

Get interface index according to pointer.

[net\_if\_up](group__net__if.md#ga02644cc623fc7a8878c17d54984e4210)

int net\_if\_up(struct net\_if \*iface)

Bring interface up.

[net\_if\_get\_first\_up](group__net__if.md#ga03d8c6aebb1412382a9eec636c227238)

struct net\_if \* net\_if\_get\_first\_up(void)

Get the first network interface which is up.

[net\_if\_ipv4\_addr\_lookup](group__net__if.md#ga04a8f21d173d51bdcc092b92ed949e53)

struct net\_if\_addr \* net\_if\_ipv4\_addr\_lookup(const struct in\_addr \*addr, struct net\_if \*\*iface)

Check if this IPv4 address belongs to one of the interfaces.

[net\_if\_set\_name](group__net__if.md#ga05dec64966fc39e3deb0679b9585688b)

int net\_if\_set\_name(struct net\_if \*iface, const char \*buf)

Set network interface name.

[net\_if\_is\_carrier\_ok](group__net__if.md#ga095554237016e563d76cfd602d1dae77)

static bool net\_if\_is\_carrier\_ok(struct net\_if \*iface)

Check if carrier is present on network device.

**Definition** net\_if.h:2531

[net\_if\_is\_admin\_up](group__net__if.md#ga099a484a654ad9af35d3212fc2c995b2)

static bool net\_if\_is\_admin\_up(struct net\_if \*iface)

Check if interface was brought up by the administrator.

**Definition** net\_if.h:2497

[net\_if\_set\_default](group__net__if.md#ga0a1f27ec893e1af3c97f130be4616589)

void net\_if\_set\_default(struct net\_if \*iface)

Set the default network interface.

[net\_if\_ipv4\_addr\_lookup\_by\_index](group__net__if.md#ga0a22661727316517685afcd551e7b38e)

int net\_if\_ipv4\_addr\_lookup\_by\_index(const struct in\_addr \*addr)

Check if this IPv4 address belongs to one of the interface indices.

[net\_if\_mcast\_callback\_t](group__net__if.md#ga0d64291573740a67eae7ff3fcc0910c5)

void(\* net\_if\_mcast\_callback\_t)(struct net\_if \*iface, const struct net\_addr \*addr, bool is\_joined)

Define a callback that is called whenever a IPv6 or IPv4 multicast address group is joined or left.

**Definition** net\_if.h:1410

[net\_if\_link\_callback\_t](group__net__if.md#ga0f87d5753fcd7cce40ecd161e6c91078)

void(\* net\_if\_link\_callback\_t)(struct net\_if \*iface, struct net\_linkaddr \*dst, int status)

Define callback that is called after a network packet has been sent.

**Definition** net\_if.h:2349

[net\_if\_ipv6\_addr\_lookup](group__net__if.md#ga13b5a26fc672d15697f99e85543184bb)

struct net\_if\_addr \* net\_if\_ipv6\_addr\_lookup(const struct in6\_addr \*addr, struct net\_if \*\*iface)

Check if this IPv6 address belongs to one of the interfaces.

[net\_if\_ipv4\_maddr\_leave](group__net__if.md#ga1408fe384736d20f36c035c10007113c)

void net\_if\_ipv4\_maddr\_leave(struct net\_if \*iface, struct net\_if\_mcast\_addr \*addr)

Mark a given multicast address to be left.

[net\_if\_ipv6\_addr\_lookup\_by\_index](group__net__if.md#ga1527872e5285790d50028a183608ac02)

int net\_if\_ipv6\_addr\_lookup\_by\_index(const struct in6\_addr \*addr)

Check if this IPv6 address belongs to one of the interface indices.

[net\_if\_get\_by\_name](group__net__if.md#ga1774ac036032bb0dc2c662f6f4f66a7f)

int net\_if\_get\_by\_name(const char \*name)

Get interface index according to its name.

[net\_if\_get\_by\_link\_addr](group__net__if.md#ga1b058361dc9bcac7d842bb49846a0c79)

struct net\_if \* net\_if\_get\_by\_link\_addr(struct net\_linkaddr \*ll\_addr)

Get an interface according to link layer address.

[net\_if\_dormant\_off](group__net__if.md#ga1c31fac887d944ac0a16aad70e889496)

void net\_if\_dormant\_off(struct net\_if \*iface)

Mark interface as not dormant.

[net\_if\_ipv6\_router\_rm](group__net__if.md#ga1d108aa0b54c072e0aa9d0c049f02807)

bool net\_if\_ipv6\_router\_rm(struct net\_if\_router \*router)

Remove IPv6 router from the system.

[net\_if\_ipv4\_maddr\_rm](group__net__if.md#ga1d9273e10ab089d0f02b2b17d10a9e60)

bool net\_if\_ipv4\_maddr\_rm(struct net\_if \*iface, const struct in\_addr \*addr)

Remove an IPv4 multicast address from an interface.

[net\_if\_ipv6\_dad\_failed](group__net__if.md#ga1dd53d92f803cff3be4826ddfb6b7211)

void net\_if\_ipv6\_dad\_failed(struct net\_if \*iface, const struct in6\_addr \*addr)

Stop IPv6 Duplicate Address Detection (DAD) procedure if we find out that our IPv6 address is already...

[net\_if\_oper\_state\_set](group__net__if.md#ga1f1bf845e63cce02e2183889cc85d57e)

static enum net\_if\_oper\_state net\_if\_oper\_state\_set(struct net\_if \*iface, enum net\_if\_oper\_state oper\_state)

Set an operational state on an interface.

**Definition** net\_if.h:771

[net\_if\_unlock](group__net__if.md#ga20e166991c20ddeca8023b57ed8957ad)

static void net\_if\_unlock(struct net\_if \*iface)

**Definition** net\_if.h:646

[net\_if\_down](group__net__if.md#ga2187650062d6139b9f4b81745a206803)

int net\_if\_down(struct net\_if \*iface)

Bring interface down.

[net\_if\_need\_calc\_tx\_checksum](group__net__if.md#ga230228c3249838b8b847ecc1b4ee11aa)

bool net\_if\_need\_calc\_tx\_checksum(struct net\_if \*iface)

Check if network packet checksum calculation can be avoided or not when sending the packet.

[net\_if\_ipv4\_router\_find\_default](group__net__if.md#ga25672516d7f383807e7dd9ce5f46a94f)

struct net\_if\_router \* net\_if\_ipv4\_router\_find\_default(struct net\_if \*iface, struct in\_addr \*addr)

Find default router for this IPv4 address.

[net\_if\_ipv6\_addr\_onlink](group__net__if.md#ga25d6e2253c1d361553d478f7c948a28a)

bool net\_if\_ipv6\_addr\_onlink(struct net\_if \*\*iface, struct in6\_addr \*addr)

Check if this IPv6 address is part of the subnet of our network interface.

[net\_if\_router\_ipv4](group__net__if.md#ga2a48e13941c91ddb9bbc63d014729be1)

static struct in\_addr \* net\_if\_router\_ipv4(struct net\_if\_router \*router)

Get the IPv4 address of the given router.

**Definition** net\_if.h:2133

[net\_if\_ipv6\_prefix\_unset\_timer](group__net__if.md#ga2d68cb6dcfcffd3f87bbfb3dfce791ff)

void net\_if\_ipv6\_prefix\_unset\_timer(struct net\_if\_ipv6\_prefix \*prefix)

Unset the prefix lifetime timer.

[net\_if\_ipv6\_prefix\_add](group__net__if.md#ga2f0c98b16b090d9aea07941c64cbe035)

struct net\_if\_ipv6\_prefix \* net\_if\_ipv6\_prefix\_add(struct net\_if \*iface, struct in6\_addr \*prefix, uint8\_t len, uint32\_t lifetime)

Add a IPv6 prefix to an network interface.

[net\_if\_ipv4\_set\_gw](group__net__if.md#ga310ccbd9b37629422ca8e32836362724)

void net\_if\_ipv4\_set\_gw(struct net\_if \*iface, const struct in\_addr \*gw)

Set IPv4 gateway for an interface.

[net\_if\_config\_ipv4\_get](group__net__if.md#ga3390e248249b28f2c80e2ca0bc79d236)

int net\_if\_config\_ipv4\_get(struct net\_if \*iface, struct net\_if\_ipv4 \*\*ipv4)

Allocate network interface IPv4 config.

[net\_ipv6\_set\_hop\_limit](group__net__if.md#ga33e3bf9530e394fe0b40b1b29e413138)

static void net\_ipv6\_set\_hop\_limit(struct net\_if \*iface, uint8\_t hop\_limit)

**Definition** net\_if.h:1687

[net\_if\_carrier\_on](group__net__if.md#ga35e5db3a631ac9039f14d86e59fc0dcc)

void net\_if\_carrier\_on(struct net\_if \*iface)

Underlying network device has detected the carrier (cable connected).

[net\_if\_ipv6\_router\_find\_default](group__net__if.md#ga36dab2a8fd9120ebc9c8b18f1875ccfd)

struct net\_if\_router \* net\_if\_ipv6\_router\_find\_default(struct net\_if \*iface, struct in6\_addr \*addr)

Find default router for this IPv6 address.

[net\_if\_ipv6\_prefix\_rm](group__net__if.md#ga36f18c7a3ff1777006290170b726deed)

bool net\_if\_ipv6\_prefix\_rm(struct net\_if \*iface, struct in6\_addr \*addr, uint8\_t len)

Remove an IPv6 prefix from an interface.

[net\_if\_mcast\_monitor](group__net__if.md#ga372ef131263269cd65586d87997df745)

void net\_if\_mcast\_monitor(struct net\_if \*iface, const struct net\_addr \*addr, bool is\_joined)

Call registered multicast monitors.

[net\_if\_ipv6\_set\_mcast\_hop\_limit](group__net__if.md#ga3792cb18e34693b3c49f6dbccda3cf61)

void net\_if\_ipv6\_set\_mcast\_hop\_limit(struct net\_if \*iface, uint8\_t hop\_limit)

Set the default IPv6 multicast hop limit of a given interface.

[net\_if\_ipv6\_set\_hop\_limit](group__net__if.md#ga37b1d83f3ef7ab5996a86e7f7f3d9c72)

void net\_if\_ipv6\_set\_hop\_limit(struct net\_if \*iface, uint8\_t hop\_limit)

Set the default IPv6 hop limit of a given interface.

[net\_if\_l2\_data](group__net__if.md#ga3cad2d51fc9cc225619585e06e252db0)

static void \* net\_if\_l2\_data(struct net\_if \*iface)

Get a pointer to the interface L2 private data.

**Definition** net\_if.h:842

[net\_if\_are\_pending\_tx\_packets](group__net__if.md#ga3cddda628eca248246f9aa3b81938f95)

static bool net\_if\_are\_pending\_tx\_packets(struct net\_if \*iface)

Check if there are any pending TX network data for a given network interface.

**Definition** net\_if.h:2709

[net\_if\_ipv4\_get\_netmask](group__net__if.md#ga41aeb0e7c5f9bc837f7b2ec13401afd1)

struct in\_addr net\_if\_ipv4\_get\_netmask(struct net\_if \*iface)

Get IPv4 netmask of an interface.

[net\_if\_flag\_test\_and\_set](group__net__if.md#ga42e7482191a92007960601f8bb621dca)

static bool net\_if\_flag\_test\_and\_set(struct net\_if \*iface, enum net\_if\_flag value)

Test and set a value in network interface flags.

**Definition** net\_if.h:701

[net\_if\_ipv4\_addr\_rm](group__net__if.md#ga4433304d46b6559604486b828e7d9dec)

bool net\_if\_ipv4\_addr\_rm(struct net\_if \*iface, const struct in\_addr \*addr)

Remove a IPv4 address from an interface.

[net\_if\_ipv4\_router\_add](group__net__if.md#ga44984001411077c7a2ef68afb361b40f)

struct net\_if\_router \* net\_if\_ipv4\_router\_add(struct net\_if \*iface, struct in\_addr \*addr, bool is\_default, uint16\_t router\_lifetime)

Add IPv4 router to the system.

[net\_if\_get\_link\_addr](group__net__if.md#ga467186e964bf721e14fed38392f21872)

static struct net\_linkaddr \* net\_if\_get\_link\_addr(struct net\_if \*iface)

Get an network interface's link address.

**Definition** net\_if.h:991

[net\_if\_ipv6\_maddr\_join](group__net__if.md#ga49dbc954015307222f176f4149829b76)

void net\_if\_ipv6\_maddr\_join(struct net\_if \*iface, struct net\_if\_mcast\_addr \*addr)

Mark a given multicast address to be joined.

[net\_if\_ipv6\_select\_src\_addr](group__net__if.md#ga50689a1afdb37a7087bf47a12cc50438)

static const struct in6\_addr \* net\_if\_ipv6\_select\_src\_addr(struct net\_if \*iface, const struct in6\_addr \*dst)

Get a IPv6 source address that should be used when sending network data to destination.

**Definition** net\_if.h:1836

[net\_if\_offload](group__net__if.md#ga520939e94620ca75475a71f153df6d4a)

static struct net\_offload \* net\_if\_offload(struct net\_if \*iface)

Return the IP offload plugin.

**Definition** net\_if.h:908

[net\_if\_set\_link\_addr](group__net__if.md#ga52b41b2f8b7d3405338a0539542677a0)

static int net\_if\_set\_link\_addr(struct net\_if \*iface, uint8\_t \*addr, uint8\_t len, enum net\_link\_type type)

Set a network interface's link address.

**Definition** net\_if.h:1084

[net\_if\_flag\_set](group__net__if.md#ga52f9fca13e9f836799e0e40f581744d2)

static void net\_if\_flag\_set(struct net\_if \*iface, enum net\_if\_flag value)

Set a value in network interface flags.

**Definition** net\_if.h:684

[net\_if\_ipv6\_get\_hop\_limit](group__net__if.md#ga54b200a4c4f09678298bf1b8f5da2ea6)

uint8\_t net\_if\_ipv6\_get\_hop\_limit(struct net\_if \*iface)

Get IPv6 hop limit specified for a given interface.

[net\_if\_get\_default](group__net__if.md#ga55214771e462cbd4930ffa738813cb87)

struct net\_if \* net\_if\_get\_default(void)

Get the default network interface.

[net\_if\_ipv4\_set\_ttl](group__net__if.md#ga5544374d7ebea26a239d561083f0203d)

void net\_if\_ipv4\_set\_ttl(struct net\_if \*iface, uint8\_t ttl)

Set IPv4 time-to-live value specified to a given interface.

[net\_if\_ipv4\_addr\_mask\_cmp](group__net__if.md#ga558b31e556a1a4b8d1e68a78f3f755ea)

bool net\_if\_ipv4\_addr\_mask\_cmp(struct net\_if \*iface, const struct in\_addr \*addr)

Check if the given IPv4 address belongs to local subnet.

[net\_if\_queue\_tx](group__net__if.md#ga56c4d37edcea540be09ebcdf97265aed)

void net\_if\_queue\_tx(struct net\_if \*iface, struct net\_pkt \*pkt)

Queue a packet to the net interface TX queue.

[net\_if\_config\_ipv6\_get](group__net__if.md#ga56c9aef19bc9827d9ec96c00e10840fa)

int net\_if\_config\_ipv6\_get(struct net\_if \*iface, struct net\_if\_ipv6 \*\*ipv6)

Allocate network interface IPv6 config.

[net\_if\_ipv6\_prefix\_get](group__net__if.md#ga57ee087a53b59381ecb739a62e0e17d0)

struct net\_if\_ipv6\_prefix \* net\_if\_ipv6\_prefix\_get(struct net\_if \*iface, struct in6\_addr \*addr)

Return prefix that corresponds to this IPv6 address.

[net\_if\_ipv6\_addr\_foreach](group__net__if.md#ga5ac646ad7fda0fa48e78c15b4ca52d50)

void net\_if\_ipv6\_addr\_foreach(struct net\_if \*iface, net\_if\_ip\_addr\_cb\_t cb, void \*user\_data)

Go through all IPv6 addresses on a network interface and call callback for each used address.

[net\_if\_get\_name](group__net__if.md#ga5f653cd73c1ecd548a931eb7fbd170f7)

int net\_if\_get\_name(struct net\_if \*iface, char \*buf, int len)

Get network interface name.

[net\_if\_ipv6\_addr\_rm](group__net__if.md#ga614e1458fa28d26c26f447e9fbcc2cb7)

bool net\_if\_ipv6\_addr\_rm(struct net\_if \*iface, const struct in6\_addr \*addr)

Remove an IPv6 address from an interface.

[net\_if\_carrier\_off](group__net__if.md#ga6839941422a88c1f707ab70ea34df323)

void net\_if\_carrier\_off(struct net\_if \*iface)

Underlying network device has lost the carrier (cable disconnected).

[net\_if\_ipv6\_prefix\_set\_timer](group__net__if.md#ga68cffe343c518bad7f7f152e30f7f9ee)

void net\_if\_ipv6\_prefix\_set\_timer(struct net\_if\_ipv6\_prefix \*prefix, uint32\_t lifetime)

Set the prefix lifetime timer.

[net\_if\_unregister\_link\_cb](group__net__if.md#ga6ba64fac6e8d846ae7be5990f49a8293)

void net\_if\_unregister\_link\_cb(struct net\_if\_link\_cb \*link)

Unregister a link callback.

[net\_if\_ipv4\_router\_rm](group__net__if.md#ga6be14f5307bc63ce87ff0a3fad7c7f4d)

bool net\_if\_ipv4\_router\_rm(struct net\_if\_router \*router)

Remove IPv4 router from the system.

[net\_if\_is\_ip\_offloaded](group__net__if.md#ga6bfa5f84a2127bbad27a0a3b319526a1)

static bool net\_if\_is\_ip\_offloaded(struct net\_if \*iface)

Return the IP offload status.

**Definition** net\_if.h:880

[net\_if\_is\_dormant](group__net__if.md#ga6e2e6102271c37acaa59c54e2aa6b413)

static bool net\_if\_is\_dormant(struct net\_if \*iface)

Check if the interface is dormant.

**Definition** net\_if.h:2567

[net\_if\_get\_first\_wifi](group__net__if.md#ga6e89bbafb6c0acdc6bf51078e2027236)

struct net\_if \* net\_if\_get\_first\_wifi(void)

Get first Wi-Fi network interface.

[net\_if\_ipv4\_addr\_add](group__net__if.md#ga7190958f740cac56de3a13fe688b3b5d)

struct net\_if\_addr \* net\_if\_ipv4\_addr\_add(struct net\_if \*iface, struct in\_addr \*addr, enum net\_addr\_type addr\_type, uint32\_t vlifetime)

Add a IPv4 address to an interface.

[net\_if\_ipv4\_get\_mcast\_ttl](group__net__if.md#ga71acb65b1988aab8cca9c9604c86231e)

uint8\_t net\_if\_ipv4\_get\_mcast\_ttl(struct net\_if \*iface)

Get IPv4 multicast time-to-live value specified for a given interface.

[net\_if\_get\_by\_index](group__net__if.md#ga72708cdb7f133fe5d7edf819756c3516)

struct net\_if \* net\_if\_get\_by\_index(int index)

Get interface according to index.

[net\_if\_recv\_data](group__net__if.md#ga72ed21ca0cb220199f5a2070137c7fef)

enum net\_verdict net\_if\_recv\_data(struct net\_if \*iface, struct net\_pkt \*pkt)

Input a packet through a net iface.

[net\_if\_get\_first\_by\_type](group__net__if.md#ga762337e8b66874a0fbf59bdbeba173f5)

struct net\_if \* net\_if\_get\_first\_by\_type(const struct net\_l2 \*l2)

Get the first network interface according to its type.

[net\_if\_set\_mtu](group__net__if.md#ga76b140c6fc39b94ff4102e08e3a58e81)

static void net\_if\_set\_mtu(struct net\_if \*iface, uint16\_t mtu)

Set an network interface's MTU.

**Definition** net\_if.h:1119

[net\_if\_need\_calc\_rx\_checksum](group__net__if.md#ga7743d516edec5b80215553699712a98b)

bool net\_if\_need\_calc\_rx\_checksum(struct net\_if \*iface)

Check if received network packet checksum calculation can be avoided or not.

[net\_if\_ipv6\_maddr\_add](group__net__if.md#ga7ae82a491193dfea9b92cb9cbaf26f98)

struct net\_if\_mcast\_addr \* net\_if\_ipv6\_maddr\_add(struct net\_if \*iface, const struct in6\_addr \*addr)

Add a IPv6 multicast address to an interface.

[net\_if\_tx\_unlock](group__net__if.md#ga7deaa758536baa81045219c6f5c79217)

static void net\_if\_tx\_unlock(struct net\_if \*iface)

**Definition** net\_if.h:667

[net\_if\_ipv4\_get\_ttl](group__net__if.md#ga7e1fd28dbcf1164d056296b4df782e64)

uint8\_t net\_if\_ipv4\_get\_ttl(struct net\_if \*iface)

Get IPv4 time-to-live value specified for a given interface.

[net\_if\_is\_up](group__net__if.md#ga7e9b368d4abf9da5656140df70cfa334)

static bool net\_if\_is\_up(struct net\_if \*iface)

Check if interface is is up and running.

**Definition** net\_if.h:2473

[net\_if\_ipv6\_set\_reachable\_time](group__net__if.md#ga8328266b870fd200660cb2becaab3de4)

static void net\_if\_ipv6\_set\_reachable\_time(struct net\_if\_ipv6 \*ipv6)

Set IPv6 reachable time for a given interface.

**Definition** net\_if.h:1768

[net\_if\_ipv6\_get\_ll\_addr](group__net__if.md#ga85b7a923d46d36ecd63f9930bd8970c4)

struct in6\_addr \* net\_if\_ipv6\_get\_ll\_addr(enum net\_addr\_state state, struct net\_if \*\*iface)

Return link local IPv6 address from the first interface that has a link local address matching give s...

[net\_if\_config\_ipv4\_put](group__net__if.md#ga88c13a45617480a665c7f9f589ec8e10)

int net\_if\_config\_ipv4\_put(struct net\_if \*iface)

Release network interface IPv4 config.

[net\_if\_dormant\_on](group__net__if.md#ga89a3374d4bb116460a7b7c50a750b593)

void net\_if\_dormant\_on(struct net\_if \*iface)

Mark interface as dormant.

[net\_if\_config\_ipv6\_put](group__net__if.md#ga8af1400b354c42a64795cdb1a600ddd6)

int net\_if\_config\_ipv6\_put(struct net\_if \*iface)

Release network interface IPv6 config.

[net\_if\_ipv4\_is\_addr\_bcast](group__net__if.md#ga8f93179138c1942bc1a099102a4314cf)

bool net\_if\_ipv4\_is\_addr\_bcast(struct net\_if \*iface, const struct in\_addr \*addr)

Check if the given IPv4 address is a broadcast address.

[net\_if\_mcast\_mon\_register](group__net__if.md#ga8fdd0665ed76db6055777e395ca60255)

void net\_if\_mcast\_mon\_register(struct net\_if\_mcast\_monitor \*mon, struct net\_if \*iface, net\_if\_mcast\_callback\_t cb)

Register a multicast monitor.

[net\_if\_ipv4\_set\_mcast\_ttl](group__net__if.md#ga9452fef4f1309fb1a53a6a8b4f222377)

void net\_if\_ipv4\_set\_mcast\_ttl(struct net\_if \*iface, uint8\_t ttl)

Set IPv4 multicast time-to-live value specified to a given interface.

[net\_if\_ipv4\_set\_netmask\_by\_index](group__net__if.md#ga94f2d2e69548609dd329c7e6b21e8958)

bool net\_if\_ipv4\_set\_netmask\_by\_index(int index, const struct in\_addr \*netmask)

Set IPv4 netmask for an interface index.

[net\_if\_ipv6\_get\_mcast\_hop\_limit](group__net__if.md#ga95505542ecf92642a0b6f68f9dda5bf6)

uint8\_t net\_if\_ipv6\_get\_mcast\_hop\_limit(struct net\_if \*iface)

Get IPv6 multicast hop limit specified for a given interface.

[net\_if\_start\_dad](group__net__if.md#ga9655c010ccbf989e9328271f5dbcc685)

static void net\_if\_start\_dad(struct net\_if \*iface)

Start duplicate address detection procedure.

**Definition** net\_if.h:1021

[net\_if\_foreach](group__net__if.md#ga96b198fd9df4a985b0dde84dd7152815)

void net\_if\_foreach(net\_if\_cb\_t cb, void \*user\_data)

Go through all the network interfaces and call callback for each interface.

[net\_if\_ipv6\_addr\_add\_by\_index](group__net__if.md#ga980bffb649ed48775bdc6cb2a0caef15)

bool net\_if\_ipv6\_addr\_add\_by\_index(int index, struct in6\_addr \*addr, enum net\_addr\_type addr\_type, uint32\_t vlifetime)

Add a IPv6 address to an interface by index.

[net\_if\_ipv6\_router\_add](group__net__if.md#ga9c766ed70ada6eb551ac6542d7ac1ca3)

struct net\_if\_router \* net\_if\_ipv6\_router\_add(struct net\_if \*iface, struct in6\_addr \*addr, uint16\_t router\_lifetime)

Add IPv6 router to the system.

[net\_if\_unset\_promisc](group__net__if.md#ga9c8212c087883510050ac6a39ef0a7bf)

static void net\_if\_unset\_promisc(struct net\_if \*iface)

Set network interface into normal mode.

**Definition** net\_if.h:2675

[net\_if\_socket\_offload\_set](group__net__if.md#ga9db52875580115c743b1f35cd6c46796)

static void net\_if\_socket\_offload\_set(struct net\_if \*iface, net\_socket\_create\_t socket\_offload)

Set the function to create an offloaded socket.

**Definition** net\_if.h:949

[net\_if\_ipv6\_get\_reachable\_time](group__net__if.md#ga9dd1f91edbb519a6a079f363c33efacf)

static uint32\_t net\_if\_ipv6\_get\_reachable\_time(struct net\_if \*iface)

Get IPv6 reachable timeout specified for a given interface.

**Definition** net\_if.h:1738

[net\_if\_is\_promisc](group__net__if.md#ga9f1a6eab849517734ec422deb0ba71f5)

static bool net\_if\_is\_promisc(struct net\_if \*iface)

Check if promiscuous mode is set or not.

**Definition** net\_if.h:2692

[net\_if\_ipv4\_maddr\_is\_joined](group__net__if.md#gaa30769fc8016f1a7496b3ede277d8d8a)

static bool net\_if\_ipv4\_maddr\_is\_joined(struct net\_if\_mcast\_addr \*addr)

Check if given multicast address is joined or not.

**Definition** net\_if.h:2103

[net\_if\_ipv6\_prefix\_set\_lf](group__net__if.md#gaa3c711e814fb6a4e552b4ef723d0baa0)

static void net\_if\_ipv6\_prefix\_set\_lf(struct net\_if\_ipv6\_prefix \*prefix, bool is\_infinite)

Set the infinite status of the prefix.

**Definition** net\_if.h:1551

[net\_if\_ipv4\_maddr\_add](group__net__if.md#gaa43fa83711703f8737e50b639e11b16c)

struct net\_if\_mcast\_addr \* net\_if\_ipv4\_maddr\_add(struct net\_if \*iface, const struct in\_addr \*addr)

Add a IPv4 multicast address to an interface.

[net\_if\_is\_wifi](group__net__if.md#gaa458b5f349c55007108b47b99f4954d5)

bool net\_if\_is\_wifi(struct net\_if \*iface)

Check if the network interface supports Wi-Fi.

[net\_if\_register\_link\_cb](group__net__if.md#gaa81b7d9ed8dc05da3391265dbc89b665)

void net\_if\_register\_link\_cb(struct net\_if\_link\_cb \*link, net\_if\_link\_callback\_t cb)

Register a link callback.

[net\_if\_lock](group__net__if.md#gaaa649aca4e48d74ae2f7cff3769e9781)

static void net\_if\_lock(struct net\_if \*iface)

**Definition** net\_if.h:639

[net\_if\_call\_link\_cb](group__net__if.md#gaaa64aa4391a85760bb2daf600ac4d898)

void net\_if\_call\_link\_cb(struct net\_if \*iface, struct net\_linkaddr \*lladdr, int status)

Call a link callback function.

[net\_if\_ipv6\_router\_update\_lifetime](group__net__if.md#gaadba4957802dc376ef011590c91c6af6)

void net\_if\_ipv6\_router\_update\_lifetime(struct net\_if\_router \*router, uint16\_t lifetime)

Update validity lifetime time of a router.

[net\_if\_ipv4\_addr\_foreach](group__net__if.md#gaae71be476e27c178ebb21b0f183c2825)

void net\_if\_ipv4\_addr\_foreach(struct net\_if \*iface, net\_if\_ip\_addr\_cb\_t cb, void \*user\_data)

Go through all IPv4 addresses on a network interface and call callback for each used address.

[net\_if\_ipv6\_prefix\_lookup](group__net__if.md#gaaf9af457b97c0d432b6f9f9fdd184834)

struct net\_if\_ipv6\_prefix \* net\_if\_ipv6\_prefix\_lookup(struct net\_if \*iface, struct in6\_addr \*addr, uint8\_t len)

Check if this IPv6 prefix belongs to this interface.

[net\_if\_stop\_rs](group__net__if.md#gab0195bb2151a1ba722a0b11d81066988)

static void net\_if\_stop\_rs(struct net\_if \*iface)

Stop neighbor discovery.

**Definition** net\_if.h:1043

[net\_if\_ipv6\_calc\_reachable\_time](group__net__if.md#gab1861b5cefa73b4eefbb447cb1438cdc)

uint32\_t net\_if\_ipv6\_calc\_reachable\_time(struct net\_if\_ipv6 \*ipv6)

Calculate next reachable time value for IPv6 reachable time.

[net\_if\_ipv6\_set\_base\_reachable\_time](group__net__if.md#gab3939d735b660f8f02124df656ceba2c)

static void net\_if\_ipv6\_set\_base\_reachable\_time(struct net\_if \*iface, uint32\_t reachable\_time)

Set IPv6 reachable time for a given interface.

**Definition** net\_if.h:1717

[net\_if\_ipv6\_addr\_lookup\_by\_iface](group__net__if.md#gab53eabb540a4487d83f27c8e319c736a)

struct net\_if\_addr \* net\_if\_ipv6\_addr\_lookup\_by\_iface(struct net\_if \*iface, struct in6\_addr \*addr)

Check if this IPv6 address belongs to this specific interfaces.

[net\_if\_ip\_addr\_cb\_t](group__net__if.md#gab58d8561a4f21899e2db34043d346516)

void(\* net\_if\_ip\_addr\_cb\_t)(struct net\_if \*iface, struct net\_if\_addr \*addr, void \*user\_data)

Callback used while iterating over network interface IP addresses.

**Definition** net\_if.h:1351

[net\_if\_flag\_test\_and\_clear](group__net__if.md#gab8f371c7f8890cf4728177f6595141d7)

static bool net\_if\_flag\_test\_and\_clear(struct net\_if \*iface, enum net\_if\_flag value)

Test and clear a value in network interface flags.

**Definition** net\_if.h:733

[net\_if\_start\_rs](group__net__if.md#gab9bdb7f8a9eeed4d9b70965b8af82cb7)

void net\_if\_start\_rs(struct net\_if \*iface)

Start neighbor discovery and send router solicitation message.

[net\_if\_ipv6\_maddr\_is\_joined](group__net__if.md#gabe2c16a378a35a22d008bff9142e5449)

static bool net\_if\_ipv6\_maddr\_is\_joined(struct net\_if\_mcast\_addr \*addr)

Check if given multicast address is joined or not.

**Definition** net\_if.h:1478

[net\_if\_ipv6\_addr\_rm\_by\_index](group__net__if.md#gac159e3b0fbf558d5fb09774141da7d6d)

bool net\_if\_ipv6\_addr\_rm\_by\_index(int index, const struct in6\_addr \*addr)

Remove an IPv6 address from an interface by index.

[net\_if\_cb\_t](group__net__if.md#gac48ab8e6337e7cf387af9b293f254a80)

void(\* net\_if\_cb\_t)(struct net\_if \*iface, void \*user\_data)

Callback used while iterating over network interfaces.

**Definition** net\_if.h:2446

[net\_if\_ipv4\_addr\_rm\_by\_index](group__net__if.md#gac5bf15f948ab195cecce98d1b40bda37)

bool net\_if\_ipv4\_addr\_rm\_by\_index(int index, const struct in\_addr \*addr)

Remove a IPv4 address from an interface by interface index.

[net\_if\_ipv6\_get\_global\_addr](group__net__if.md#gaca7d686c772deac13a027cc046333126)

struct in6\_addr \* net\_if\_ipv6\_get\_global\_addr(enum net\_addr\_state state, struct net\_if \*\*iface)

Return global IPv6 address from the first interface that has a global IPv6 address matching the given...

[net\_if\_get\_mtu](group__net__if.md#gacddc98531c5748db5a34f5c3a3e96e86)

static uint16\_t net\_if\_get\_mtu(struct net\_if \*iface)

Get an network interface's MTU.

**Definition** net\_if.h:1102

[net\_if\_ipv6\_router\_lookup](group__net__if.md#gacece4ee588082259b3b5cfcd5ac1d552)

struct net\_if\_router \* net\_if\_ipv6\_router\_lookup(struct net\_if \*iface, struct in6\_addr \*addr)

Check if IPv6 address is one of the routers configured in the system.

[net\_if\_ipv4\_addr\_add\_by\_index](group__net__if.md#gad140a69cf510ad99a8a8c770bab95bc9)

bool net\_if\_ipv4\_addr\_add\_by\_index(int index, struct in\_addr \*addr, enum net\_addr\_type addr\_type, uint32\_t vlifetime)

Add a IPv4 address to an interface by network interface index.

[net\_if\_ipv6\_maddr\_leave](group__net__if.md#gad24d5537d52de9781a7a6a55ceedd92b)

void net\_if\_ipv6\_maddr\_leave(struct net\_if \*iface, struct net\_if\_mcast\_addr \*addr)

Mark a given multicast address to be left.

[net\_if\_ipv4\_get\_ll](group__net__if.md#gad2ffe8df3d5ccca5094daecf3b9a8508)

struct in\_addr \* net\_if\_ipv4\_get\_ll(struct net\_if \*iface, enum net\_addr\_state addr\_state)

Get a IPv4 link local address in a given state.

[net\_if\_mcast\_mon\_unregister](group__net__if.md#gad323732fe3d178a5dfdf0900e5cb5683)

void net\_if\_mcast\_mon\_unregister(struct net\_if\_mcast\_monitor \*mon)

Unregister a multicast monitor.

[net\_if\_ipv4\_set\_netmask](group__net__if.md#gad599bd11663fefa7d785b9fc5d52caf0)

void net\_if\_ipv4\_set\_netmask(struct net\_if \*iface, const struct in\_addr \*netmask)

Set IPv4 netmask for an interface.

[net\_if\_ipv4\_select\_src\_addr](group__net__if.md#gad6ec091f61ba3055be60c77ce085522f)

static const struct in\_addr \* net\_if\_ipv4\_select\_src\_addr(struct net\_if \*iface, const struct in\_addr \*dst)

Get a IPv4 source address that should be used when sending network data to destination.

**Definition** net\_if.h:2248

[net\_if\_ipv6\_get\_ll](group__net__if.md#gad6f3e1e349e281887352652f6f32274e)

struct in6\_addr \* net\_if\_ipv6\_get\_ll(struct net\_if \*iface, enum net\_addr\_state addr\_state)

Get a IPv6 link local address in a given state.

[net\_if\_ipv6\_set\_retrans\_timer](group__net__if.md#gad74566e5a34f447d2ac63d2c0e82eeff)

static void net\_if\_ipv6\_set\_retrans\_timer(struct net\_if \*iface, uint32\_t retrans\_timer)

Set IPv6 retransmit timer for a given interface.

**Definition** net\_if.h:1785

[net\_if\_ipv4\_get\_global\_addr](group__net__if.md#gad791780f25d19acfe49d5272eae2d019)

struct in\_addr \* net\_if\_ipv4\_get\_global\_addr(struct net\_if \*iface, enum net\_addr\_state addr\_state)

Get a IPv4 global address in a given state.

[net\_if\_send\_data](group__net__if.md#gada0398d757eab28d16a129692c309f4d)

enum net\_verdict net\_if\_send\_data(struct net\_if \*iface, struct net\_pkt \*pkt)

Send a packet through a net iface.

[net\_if\_ipv6\_maddr\_lookup](group__net__if.md#gadb4031153c4fef86110879befa6b9975)

struct net\_if\_mcast\_addr \* net\_if\_ipv6\_maddr\_lookup(const struct in6\_addr \*addr, struct net\_if \*\*iface)

Check if this IPv6 multicast address belongs to a specific interface or one of the interfaces.

[net\_if\_lookup\_by\_dev](group__net__if.md#gadbb8be32caa896bdcdeee19425134827)

struct net\_if \* net\_if\_lookup\_by\_dev(const struct device \*dev)

Find an interface from it's related device.

[net\_if\_router\_ipv6](group__net__if.md#gadbf1538003473d448ff0808896b732a5)

static struct in6\_addr \* net\_if\_router\_ipv6(struct net\_if\_router \*router)

Get the IPv6 address of the given router.

**Definition** net\_if.h:1599

[net\_if\_ipv4\_maddr\_lookup](group__net__if.md#gadc1514a0d6852de9dbce043bc99d4eb0)

struct net\_if\_mcast\_addr \* net\_if\_ipv4\_maddr\_lookup(const struct in\_addr \*addr, struct net\_if \*\*iface)

Check if this IPv4 multicast address belongs to a specific interface or one of the interfaces.

[net\_if\_router\_rm](group__net__if.md#gadc87242eb7205362a308b3c4437bf76d)

void net\_if\_router\_rm(struct net\_if\_router \*router)

Remove a router from the system.

[net\_if\_ipv6\_get\_retrans\_timer](group__net__if.md#gaddbf5a6ba412e6bdb7e31568fe827bd0)

static uint32\_t net\_if\_ipv6\_get\_retrans\_timer(struct net\_if \*iface)

Get IPv6 retransmit timer specified for a given interface.

**Definition** net\_if.h:1806

[net\_if\_ipv4\_set\_gw\_by\_index](group__net__if.md#gadef49124c331817165475c69fb9104e0)

bool net\_if\_ipv4\_set\_gw\_by\_index(int index, const struct in\_addr \*gw)

Set IPv4 gateway for an interface index.

[net\_if\_oper\_state](group__net__if.md#gadfe9d90f24046cd9bd4bbee096e747b9)

net\_if\_oper\_state

Network interface operational status (RFC 2863).

**Definition** net\_if.h:236

[net\_if\_ipv6\_addr\_add](group__net__if.md#gae00484a7fe32671a4ca04ff525e640c6)

struct net\_if\_addr \* net\_if\_ipv6\_addr\_add(struct net\_if \*iface, struct in6\_addr \*addr, enum net\_addr\_type addr\_type, uint32\_t vlifetime)

Add a IPv6 address to an interface.

[net\_if\_ipv6\_select\_src\_iface](group__net__if.md#gae1495ac9e743be54b8d90bd4ff4700ab)

static struct net\_if \* net\_if\_ipv6\_select\_src\_iface(const struct in6\_addr \*dst)

Get a network interface that should be used when sending IPv6 network data to destination.

**Definition** net\_if.h:1858

[net\_if\_flag\_is\_set](group__net__if.md#gae1f373ddd61c18a81481d8ddcfb12543)

static bool net\_if\_flag\_is\_set(struct net\_if \*iface, enum net\_if\_flag value)

Check if a value in network interface flags is set.

**Definition** net\_if.h:750

[net\_if\_config\_get](group__net__if.md#gae2323a72714e29836d8296dfc330f7fd)

static struct net\_if\_config \* net\_if\_config\_get(struct net\_if \*iface)

Get network interface IP config.

**Definition** net\_if.h:1170

[net\_if\_get\_config](group__net__if.md#gae271e0e4dcb031a83d9908e597a45048)

static struct net\_if\_config \* net\_if\_get\_config(struct net\_if \*iface)

Return network configuration for this network interface.

**Definition** net\_if.h:1006

[net\_if\_ipv4\_maddr\_join](group__net__if.md#gae275a5e75817aa178d36f422573ad76a)

void net\_if\_ipv4\_maddr\_join(struct net\_if \*iface, struct net\_if\_mcast\_addr \*addr)

Mark a given multicast address to be joined.

[net\_if\_addr\_set\_lf](group__net__if.md#gae66f6e7bd31545e6161fcd4600fe5842)

static void net\_if\_addr\_set\_lf(struct net\_if\_addr \*ifaddr, bool is\_infinite)

Set the infinite status of the network interface address.

**Definition** net\_if.h:1137

[net\_if\_flag](group__net__if.md#gae691e5537917ffce27ad0db82c730371)

net\_if\_flag

Network interface flags.

**Definition** net\_if.h:178

[net\_if\_get\_device](group__net__if.md#gaeb8c703f273bc07ae9bb7a0d8bfe6f3d)

static const struct device \* net\_if\_get\_device(struct net\_if \*iface)

Get an network interface's device.

**Definition** net\_if.h:857

[net\_if\_is\_offloaded](group__net__if.md#gaecedc93a6dab2c57fe686718ea4d78af)

bool net\_if\_is\_offloaded(struct net\_if \*iface)

Return offload status of a given network interface.

[net\_socket\_create\_t](group__net__if.md#gaef3dfe26195514aac625e9f22e399759)

int(\* net\_socket\_create\_t)(int, int, int)

A function prototype to create an offloaded socket.

**Definition** net\_if.h:553

[net\_if\_ipv6\_addr\_update\_lifetime](group__net__if.md#gaef8a6752a201f81636c4ffc1ebba4a25)

void net\_if\_ipv6\_addr\_update\_lifetime(struct net\_if\_addr \*ifaddr, uint32\_t vlifetime)

Update validity lifetime time of an IPv6 address.

[net\_if\_ipv6\_maddr\_rm](group__net__if.md#gaf0ce126bb5019ff5f5ff0876b9712ad9)

bool net\_if\_ipv6\_maddr\_rm(struct net\_if \*iface, const struct in6\_addr \*addr)

Remove an IPv6 multicast address from an interface.

[net\_if\_is\_socket\_offloaded](group__net__if.md#gaf308baf2241fa455b50b439b7fab3f1e)

static bool net\_if\_is\_socket\_offloaded(struct net\_if \*iface)

Return the socket offload status.

**Definition** net\_if.h:929

[net\_if\_set\_promisc](group__net__if.md#gaf9f81f3b9697ca47f7674d85f37a8d80)

static int net\_if\_set\_promisc(struct net\_if \*iface)

Set network interface into promiscuous mode.

**Definition** net\_if.h:2659

[net\_if\_l2](group__net__if.md#gafa451f6118529d1d084704d00b2aae20)

static const struct net\_l2 \* net\_if\_l2(struct net\_if \*iface)

Get a pointer to the interface L2.

**Definition** net\_if.h:816

[net\_if\_socket\_offload](group__net__if.md#gafb2bbaec96c4759d920b2866c0b3ef3a)

static net\_socket\_create\_t net\_if\_socket\_offload(struct net\_if \*iface)

Return the function to create an offloaded socket.

**Definition** net\_if.h:970

[net\_if\_tx\_lock](group__net__if.md#gafb64d93ba8f6b047bb61a6fd4994b711)

static void net\_if\_tx\_lock(struct net\_if \*iface)

**Definition** net\_if.h:656

[net\_if\_ipv4\_select\_src\_iface](group__net__if.md#gafea1a35f452ad8168855852cbfdf0024)

static struct net\_if \* net\_if\_ipv4\_select\_src\_iface(const struct in\_addr \*dst)

Get a network interface that should be used when sending IPv4 network data to destination.

**Definition** net\_if.h:2224

[net\_if\_flag\_clear](group__net__if.md#gaff751b6a92b0c608ecfc50e8c0587fd3)

static void net\_if\_flag\_clear(struct net\_if \*iface, enum net\_if\_flag value)

Clear a value in network interface flags.

**Definition** net\_if.h:716

[NET\_IF\_OPER\_TESTING](group__net__if.md#ggadfe9d90f24046cd9bd4bbee096e747b9a2240173b5c247ab5eb0a9a6afafb296f)

@ NET\_IF\_OPER\_TESTING

**Definition** net\_if.h:241

[NET\_IF\_OPER\_DORMANT](group__net__if.md#ggadfe9d90f24046cd9bd4bbee096e747b9a5cbe2aa27a444444d4acf122113d430d)

@ NET\_IF\_OPER\_DORMANT

**Definition** net\_if.h:242

[NET\_IF\_OPER\_UP](group__net__if.md#ggadfe9d90f24046cd9bd4bbee096e747b9a6b99bfc28d831292029761d74209ee03)

@ NET\_IF\_OPER\_UP

**Definition** net\_if.h:243

[NET\_IF\_OPER\_NOTPRESENT](group__net__if.md#ggadfe9d90f24046cd9bd4bbee096e747b9a8f9f55840e75693163197baae9d50c32)

@ NET\_IF\_OPER\_NOTPRESENT

**Definition** net\_if.h:238

[NET\_IF\_OPER\_UNKNOWN](group__net__if.md#ggadfe9d90f24046cd9bd4bbee096e747b9ac7cae092ea6ceeb62499a9b435ac4b58)

@ NET\_IF\_OPER\_UNKNOWN

**Definition** net\_if.h:237

[NET\_IF\_OPER\_DOWN](group__net__if.md#ggadfe9d90f24046cd9bd4bbee096e747b9adb20a95215310c420f8dae7e17a2f367)

@ NET\_IF\_OPER\_DOWN

**Definition** net\_if.h:239

[NET\_IF\_OPER\_LOWERLAYERDOWN](group__net__if.md#ggadfe9d90f24046cd9bd4bbee096e747b9ae7e9b8b12ae618a5ee1483dee916aab4)

@ NET\_IF\_OPER\_LOWERLAYERDOWN

**Definition** net\_if.h:240

[NET\_IF\_NO\_AUTO\_START](group__net__if.md#ggae691e5537917ffce27ad0db82c730371a0babb762301878eaf8ef8a05213ecf05)

@ NET\_IF\_NO\_AUTO\_START

Do not start the interface immediately after initialization.

**Definition** net\_if.h:194

[NET\_IF\_IPV6\_NO\_MLD](group__net__if.md#ggae691e5537917ffce27ad0db82c730371a1d362cfabb58eb220ddb069431221fbe)

@ NET\_IF\_IPV6\_NO\_MLD

IPv6 Multicast Listener Discovery disabled.

**Definition** net\_if.h:224

[NET\_IF\_POINTOPOINT](group__net__if.md#ggae691e5537917ffce27ad0db82c730371a3256ef2d537c85b4c2b33b92935e1009)

@ NET\_IF\_POINTOPOINT

Interface is pointopoint.

**Definition** net\_if.h:183

[NET\_IF\_IPV6\_NO\_ND](group__net__if.md#ggae691e5537917ffce27ad0db82c730371a542ecce860ef3bf2df493da8d4c6a2f7)

@ NET\_IF\_IPV6\_NO\_ND

IPv6 Neighbor Discovery disabled.

**Definition** net\_if.h:221

[NET\_IF\_FORWARD\_MULTICASTS](group__net__if.md#ggae691e5537917ffce27ad0db82c730371a581971c9d93a910c4c607da45aa2e4ac)

@ NET\_IF\_FORWARD\_MULTICASTS

Flag defines if received multicasts of other interface are forwarded on this interface.

**Definition** net\_if.h:203

[NET\_IF\_IPV4](group__net__if.md#ggae691e5537917ffce27ad0db82c730371a67d2c0fe390ab16f347ee2dc0a056329)

@ NET\_IF\_IPV4

Interface supports IPv4.

**Definition** net\_if.h:206

[NET\_IF\_PROMISC](group__net__if.md#ggae691e5537917ffce27ad0db82c730371a700d92a5b0de3c779e59806137b35141)

@ NET\_IF\_PROMISC

Interface is in promiscuous mode.

**Definition** net\_if.h:186

[NET\_IF\_DORMANT](group__net__if.md#ggae691e5537917ffce27ad0db82c730371a7dd1db72a37b1fbc4c4491ce1c75238d)

@ NET\_IF\_DORMANT

Driver signals dormant.

**Definition** net\_if.h:218

[NET\_IF\_SUSPENDED](group__net__if.md#ggae691e5537917ffce27ad0db82c730371aaaeafc62e61ec120609205770c8b54f0)

@ NET\_IF\_SUSPENDED

Power management specific: interface is being suspended.

**Definition** net\_if.h:197

[NET\_IF\_IPV6](group__net__if.md#ggae691e5537917ffce27ad0db82c730371aab31a9e1e8c02159f45efc4e0455a4d6)

@ NET\_IF\_IPV6

Interface supports IPv6.

**Definition** net\_if.h:209

[NET\_IF\_UP](group__net__if.md#ggae691e5537917ffce27ad0db82c730371ab0ab7393d643354c46c3437d74c15840)

@ NET\_IF\_UP

Interface is admin up.

**Definition** net\_if.h:180

[NET\_IF\_LOWER\_UP](group__net__if.md#ggae691e5537917ffce27ad0db82c730371ab1a529826bad6b4bcd04185372f97d6d)

@ NET\_IF\_LOWER\_UP

Driver signals L1 is up.

**Definition** net\_if.h:215

[NET\_IF\_RUNNING](group__net__if.md#ggae691e5537917ffce27ad0db82c730371add3e2ecdcd5de3154f9bd2836428a25a)

@ NET\_IF\_RUNNING

Interface up and running (ready to receive and transmit).

**Definition** net\_if.h:212

[NET\_IF\_NO\_TX\_LOCK](group__net__if.md#ggae691e5537917ffce27ad0db82c730371ae8d564e1577c8daad8ce50a729c500c9)

@ NET\_IF\_NO\_TX\_LOCK

Mutex locking on TX data path disabled on the interface.

**Definition** net\_if.h:227

[net\_link\_type](group__net__linkaddr.md#ga1312c2322bc4a4f1c3b76d6466806b24)

net\_link\_type

Type of the link address.

**Definition** net\_linkaddr.h:47

[sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8)

struct \_slist sys\_slist\_t

Single-linked list structure.

**Definition** slist.h:49

[sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493)

struct \_snode sys\_snode\_t

Single-linked list node structure.

**Definition** slist.h:39

[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33)

#define ENOTSUP

Unsupported value.

**Definition** errno.h:115

[EPERM](group__system__errno.md#gadd669d31505a077f769cff8e66c780b3)

#define EPERM

Not owner.

**Definition** errno.h:40

[hostname.h](hostname_8h.md)

Hostname configuration definitions.

[ipv4\_autoconf.h](ipv4__autoconf_8h.md)

IPv4 Autoconfiguration.

[net\_ipv4\_autoconf\_state](ipv4__autoconf_8h.md#abdf8bb08f12768aad2ff95b902bdc899)

net\_ipv4\_autoconf\_state

Current state of IPv4 Autoconfiguration.

**Definition** ipv4\_autoconf.h:15

[net\_core.h](net__core_8h.md)

Network core definitions.

[net\_ip.h](net__ip_8h.md)

IPv6 and IPv4 definitions.

[net\_l2.h](net__l2_8h.md)

Public API for network L2 interface.

[net\_linkaddr.h](net__linkaddr_8h.md)

Public API for network link address.

[net\_stats.h](net__stats_8h.md)

Network statistics.

[net\_timeout.h](net__timeout_8h.md)

Network timer with wrap around.

[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)

state

**Definition** parser\_state.h:29

[slist.h](slist_8h.md)

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

[int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b)

\_\_INT64\_TYPE\_\_ int64\_t

**Definition** stdint.h:75

[int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf)

\_\_INT16\_TYPE\_\_ int16\_t

**Definition** stdint.h:73

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:387

[in6\_addr](structin6__addr.md)

IPv6 address struct.

**Definition** net\_ip.h:139

[in\_addr](structin__addr.md)

IPv4 address struct.

**Definition** net\_ip.h:151

[k\_fifo](structk__fifo.md)

**Definition** kernel.h:2374

[k\_mutex](structk__mutex.md)

Mutex Structure.

**Definition** kernel.h:2900

[k\_thread](structk__thread.md)

Thread Structure.

**Definition** thread.h:250

[net\_dhcpv6\_params](structnet__dhcpv6__params.md)

DHCPv6 client configuration parameters.

**Definition** dhcpv6.h:58

[net\_if\_addr](structnet__if__addr.md)

Network Interface unicast IP addresses.

**Definition** net\_if.h:52

[net\_if\_addr::address](structnet__if__addr.md#a06b8d2e8b5ea6d8d671800d966163763)

struct net\_addr address

IP address.

**Definition** net\_if.h:54

[net\_if\_addr::is\_mesh\_local](structnet__if__addr.md#a1db7cc6c7566baf9340dab6771ca5010)

uint8\_t is\_mesh\_local

Is this IP address usage limited to the subnet (mesh) or not.

**Definition** net\_if.h:83

[net\_if\_addr::addr\_state](structnet__if__addr.md#a3106fdcf0dd2479c95efafc586217a2c)

enum net\_addr\_state addr\_state

What is the current state of the address.

**Definition** net\_if.h:69

[net\_if\_addr::is\_infinite](structnet__if__addr.md#a6e799428eb0633a25e4dc3c55e3a3b8c)

uint8\_t is\_infinite

Is the IP address valid forever.

**Definition** net\_if.h:77

[net\_if\_addr::addr\_type](structnet__if__addr.md#ab4fd41001cc24615803bfabb9d48e7eb)

enum net\_addr\_type addr\_type

How the IP address was set.

**Definition** net\_if.h:66

[net\_if\_addr::is\_used](structnet__if__addr.md#aed4d91ba064d24ad0d53c0960cde0352)

uint8\_t is\_used

Is this IP address used or not.

**Definition** net\_if.h:80

[net\_if\_config](structnet__if__config.md)

IP and other configuration related data for network interface.

**Definition** net\_if.h:492

[net\_if\_dev](structnet__if__dev.md)

Network Interface Device structure.

**Definition** net\_if.h:569

[net\_if\_dev::oper\_state](structnet__if__dev.md#a30eabb2ffae082d0de81a50c510738a3)

enum net\_if\_oper\_state oper\_state

RFC 2863 operational status.

**Definition** net\_if.h:605

[net\_if\_dev::l2](structnet__if__dev.md#a85d713c62875f5fe9e3ec29773150797)

const struct net\_l2 \*const l2

Interface's L2 layer.

**Definition** net\_if.h:574

[net\_if\_dev::l2\_data](structnet__if__dev.md#a8fec6a7f612fc1268ef486d8bdebe018)

void \* l2\_data

Interface's private L2 data pointer.

**Definition** net\_if.h:577

[net\_if\_dev::mtu](structnet__if__dev.md#aa15ccca2eb67b8d2afca153ccacb3742)

uint16\_t mtu

The hardware MTU.

**Definition** net\_if.h:595

[net\_if\_dev::dev](structnet__if__dev.md#aab633a44f165f571910dc9fc9e131c50)

const struct device \* dev

The actually device driver instance the net\_if is related to.

**Definition** net\_if.h:571

[net\_if\_dev::link\_addr](structnet__if__dev.md#aac6d5d341ab520e6aac7f7b03737c197)

struct net\_linkaddr link\_addr

The hardware link address.

**Definition** net\_if.h:583

[net\_if\_dev::flags](structnet__if__dev.md#ac8f9c30e1dea05c28c88d3b367b130f5)

atomic\_t flags[ATOMIC\_BITMAP\_SIZE(NET\_IF\_NUM\_FLAGS)]

**Definition** net\_if.h:580

[net\_if\_ip](structnet__if__ip.md)

Network interface IP address configuration.

**Definition** net\_if.h:479

[net\_if\_ipv4](structnet__if__ipv4.md)

**Definition** net\_if.h:371

[net\_if\_ipv4::mcast\_ttl](structnet__if__ipv4.md#a7e9bf16d51989cfcfe564f4f0a43b480)

uint8\_t mcast\_ttl

IPv4 time-to-live for multicast packets.

**Definition** net\_if.h:388

[net\_if\_ipv4::unicast](structnet__if__ipv4.md#a89b942f7120619fba28f4fd9ab0bf41c)

struct net\_if\_addr unicast[NET\_IF\_MAX\_IPV4\_ADDR]

Unicast IP addresses.

**Definition** net\_if.h:373

[net\_if\_ipv4::netmask](structnet__if__ipv4.md#a9de5d553b0719489a34f1190939d0bc0)

struct in\_addr netmask

Netmask.

**Definition** net\_if.h:382

[net\_if\_ipv4::gw](structnet__if__ipv4.md#aa24772c7202bf465ee3da94a172b7bcb)

struct in\_addr gw

Gateway.

**Definition** net\_if.h:379

[net\_if\_ipv4::ttl](structnet__if__ipv4.md#acdc6d5d6eb5362f4f6d2c027cc40e684)

uint8\_t ttl

IPv4 time-to-live.

**Definition** net\_if.h:385

[net\_if\_ipv4::mcast](structnet__if__ipv4.md#adfaf5b50255bd35297195a7218729ae7)

struct net\_if\_mcast\_addr mcast[NET\_IF\_MAX\_IPV4\_MADDR]

Multicast IP addresses.

**Definition** net\_if.h:376

[net\_if\_ipv6\_prefix](structnet__if__ipv6__prefix.md)

Network Interface IPv6 prefixes.

**Definition** net\_if.h:122

[net\_if\_ipv6\_prefix::iface](structnet__if__ipv6__prefix.md#a0e2d1997e2ccfe1e1af5f16e0c74ed92)

struct net\_if \* iface

Backpointer to network interface where this prefix is used.

**Definition** net\_if.h:130

[net\_if\_ipv6\_prefix::is\_infinite](structnet__if__ipv6__prefix.md#a22090441b27bed06098679bf23b4e1e9)

uint8\_t is\_infinite

Is the IP prefix valid forever.

**Definition** net\_if.h:136

[net\_if\_ipv6\_prefix::len](structnet__if__ipv6__prefix.md#a4d2bc2acbe51256b76cf4d3ced3aac39)

uint8\_t len

Prefix length.

**Definition** net\_if.h:133

[net\_if\_ipv6\_prefix::prefix](structnet__if__ipv6__prefix.md#a65b450d0942b3c96cfc575b462d82028)

struct in6\_addr prefix

IPv6 prefix.

**Definition** net\_if.h:127

[net\_if\_ipv6\_prefix::is\_used](structnet__if__ipv6__prefix.md#a6a4295256957e5eddf149f1ceff62e3f)

uint8\_t is\_used

Is this prefix used or not.

**Definition** net\_if.h:139

[net\_if\_ipv6\_prefix::lifetime](structnet__if__ipv6__prefix.md#a925a97a49d383bd4ce475f5d09fcb7e3)

struct net\_timeout lifetime

Prefix lifetime.

**Definition** net\_if.h:124

[net\_if\_ipv6](structnet__if__ipv6.md)

**Definition** net\_if.h:262

[net\_if\_ipv6::prefix](structnet__if__ipv6.md#a2dccdc984f08527302d8d910a2658f72)

struct net\_if\_ipv6\_prefix prefix[NET\_IF\_MAX\_IPV6\_PREFIX]

Prefixes.

**Definition** net\_if.h:270

[net\_if\_ipv6::base\_reachable\_time](structnet__if__ipv6.md#a500a78fe23ee2ebc63f3d3b53b5b92ea)

uint32\_t base\_reachable\_time

Default reachable time (RFC 4861, page 52).

**Definition** net\_if.h:273

[net\_if\_ipv6::hop\_limit](structnet__if__ipv6.md#a71775a082984274fbc7c009ead18e751)

uint8\_t hop\_limit

IPv6 hop limit.

**Definition** net\_if.h:292

[net\_if\_ipv6::mcast](structnet__if__ipv6.md#a727d2773e0dee3be687dda5b2dd55682)

struct net\_if\_mcast\_addr mcast[NET\_IF\_MAX\_IPV6\_MADDR]

Multicast IP addresses.

**Definition** net\_if.h:267

[net\_if\_ipv6::retrans\_timer](structnet__if__ipv6.md#ac5ee47ff9d3e429ecbb8623e5d713246)

uint32\_t retrans\_timer

Retransmit timer (RFC 4861, page 52).

**Definition** net\_if.h:279

[net\_if\_ipv6::unicast](structnet__if__ipv6.md#adb6431d336cc3f46972e13d2255452c8)

struct net\_if\_addr unicast[NET\_IF\_MAX\_IPV6\_ADDR]

Unicast IP addresses.

**Definition** net\_if.h:264

[net\_if\_ipv6::mcast\_hop\_limit](structnet__if__ipv6.md#ae94906c28578f2e1ea2506b0e2972d4c)

uint8\_t mcast\_hop\_limit

IPv6 multicast hop limit.

**Definition** net\_if.h:295

[net\_if\_ipv6::reachable\_time](structnet__if__ipv6.md#af57b7dca189167f8cc757c4ed6b08f2f)

uint32\_t reachable\_time

Reachable time (RFC 4861, page 20).

**Definition** net\_if.h:276

[net\_if\_link\_cb](structnet__if__link__cb.md)

Link callback handler struct.

**Definition** net\_if.h:2361

[net\_if\_link\_cb::cb](structnet__if__link__cb.md#a66092a22cba3dd69ac1a91c3522240bb)

net\_if\_link\_callback\_t cb

Link callback.

**Definition** net\_if.h:2366

[net\_if\_link\_cb::node](structnet__if__link__cb.md#accae7945a802c5b7fc36948b12a365ef)

sys\_snode\_t node

Node information for the slist.

**Definition** net\_if.h:2363

[net\_if\_mcast\_addr](structnet__if__mcast__addr.md)

Network Interface multicast IP addresses.

**Definition** net\_if.h:93

[net\_if\_mcast\_addr::address](structnet__if__mcast__addr.md#a3e470fc2eb02ac9e5d3d7d0bea0aaa69)

struct net\_addr address

IP address.

**Definition** net\_if.h:95

[net\_if\_mcast\_addr::is\_joined](structnet__if__mcast__addr.md#a4af9009b2f9ccc0589a9ba6dac10927b)

uint8\_t is\_joined

Did we join to this group.

**Definition** net\_if.h:112

[net\_if\_mcast\_addr::is\_used](structnet__if__mcast__addr.md#abab3e6dba72e24ef522c033d277369ca)

uint8\_t is\_used

Is this multicast IP address used or not.

**Definition** net\_if.h:109

[net\_if\_mcast\_monitor](structnet__if__mcast__monitor.md)

Multicast monitor handler struct.

**Definition** net\_if.h:1422

[net\_if\_mcast\_monitor::node](structnet__if__mcast__monitor.md#a570b7d8a8a5fabca83982a5f7d1d896a)

sys\_snode\_t node

Node information for the slist.

**Definition** net\_if.h:1424

[net\_if\_mcast\_monitor::cb](structnet__if__mcast__monitor.md#aec441b858a5f6792ac9cdbc625f6babe)

net\_if\_mcast\_callback\_t cb

Multicast callback.

**Definition** net\_if.h:1430

[net\_if\_mcast\_monitor::iface](structnet__if__mcast__monitor.md#af4d0e937b2b9161918a13a0d6723c60a)

struct net\_if \* iface

Network interface.

**Definition** net\_if.h:1427

[net\_if\_router](structnet__if__router.md)

Information about routers in the system.

**Definition** net\_if.h:149

[net\_if\_router::iface](structnet__if__router.md#a03789aa0a40f7686b76616de0ca0401a)

struct net\_if \* iface

Network interface the router is connected to.

**Definition** net\_if.h:157

[net\_if\_router::is\_default](structnet__if__router.md#a34745207edcad2745d6ce311e2bf1894)

uint8\_t is\_default

Is default router.

**Definition** net\_if.h:169

[net\_if\_router::lifetime](structnet__if__router.md#a4b0d2ad8f225ab61022c10dfce3db199)

uint16\_t lifetime

Router lifetime.

**Definition** net\_if.h:163

[net\_if\_router::is\_infinite](structnet__if__router.md#a4cb47f30241ae3d410f56f1487254ed0)

uint8\_t is\_infinite

Is the router valid forever.

**Definition** net\_if.h:172

[net\_if\_router::is\_used](structnet__if__router.md#a7196e6d2bc2c958d98dfe29143a62048)

uint8\_t is\_used

Is this router used or not.

**Definition** net\_if.h:166

[net\_if\_router::address](structnet__if__router.md#a86a2ca1b95e348acbde8ce90986b83db)

struct net\_addr address

IP address.

**Definition** net\_if.h:154

[net\_if\_router::node](structnet__if__router.md#aabbac0cd0a59ca0eafdcfc0eaf5d909a)

sys\_snode\_t node

Slist lifetime timer node.

**Definition** net\_if.h:151

[net\_if\_router::life\_start](structnet__if__router.md#adf4f4c722917b3c30f8c73bc2519957f)

uint32\_t life\_start

Router life timer start.

**Definition** net\_if.h:160

[net\_if](structnet__if.md)

Network Interface structure.

**Definition** net\_if.h:615

[net\_if::if\_dev](structnet__if.md#a0982ba2019cdaa7701162e60fdb2171e)

struct net\_if\_dev \* if\_dev

The net\_if\_dev instance the net\_if is related to.

**Definition** net\_if.h:617

[net\_if::config](structnet__if.md#a5e71962f55bdead7bfbbb96518c6c404)

struct net\_if\_config config

Network interface instance configuration.

**Definition** net\_if.h:625

[net\_if::lock](structnet__if.md#ace2233b71da53ff0fc7cd564ccfc5a03)

struct k\_mutex lock

**Definition** net\_if.h:635

[net\_if::tx\_lock](structnet__if.md#af00f729ebddfdcf725169f61b6cd586b)

struct k\_mutex tx\_lock

**Definition** net\_if.h:636

[net\_l2](structnet__l2.md)

Network L2 structure.

**Definition** net\_l2.h:55

[net\_linkaddr](structnet__linkaddr.md)

Hardware link address structure.

**Definition** net\_linkaddr.h:67

[net\_linkaddr::addr](structnet__linkaddr.md#a2176a9f7a444ac3b0108102d8cf852f0)

uint8\_t \* addr

The array of byte representing the address.

**Definition** net\_linkaddr.h:69

[net\_linkaddr::type](structnet__linkaddr.md#a5f5b4c3d353261d0fab8011aa09f00d7)

uint8\_t type

What kind of address is this for.

**Definition** net\_linkaddr.h:75

[net\_linkaddr::len](structnet__linkaddr.md#a7b2f8ebe68b557eb9cbb4c2f2ecd70e0)

uint8\_t len

Length of that address array.

**Definition** net\_linkaddr.h:72

[net\_pkt](structnet__pkt.md)

Network packet.

**Definition** net\_pkt.h:63

[net\_stats](structnet__stats.md)

All network statistics in one struct.

**Definition** net\_stats.h:292

[net\_timeout](structnet__timeout.md)

Generic struct for handling network timeouts.

**Definition** net\_timeout.h:55

[net\_traffic\_class](structnet__traffic__class.md)

Network traffic class.

**Definition** net\_if.h:536

[net\_traffic\_class::stack](structnet__traffic__class.md#a2d98bc68d38bdef649d645b8b52516c5)

k\_thread\_stack\_t \* stack

Stack for this handler.

**Definition** net\_if.h:544

[net\_traffic\_class::handler](structnet__traffic__class.md#a8d0023588fee0a8ff1381bbc80ada143)

struct k\_thread handler

Traffic class handler thread.

**Definition** net\_if.h:541

[net\_traffic\_class::fifo](structnet__traffic__class.md#a94511ca12bad1687f5c7ca862c857ded)

struct k\_fifo fifo

Fifo for handling this Tx or Rx packet.

**Definition** net\_if.h:538

[sockaddr](structsockaddr.md)

Generic sockaddr struct.

**Definition** net\_ip.h:347

[iterable\_sections.h](sys_2iterable__sections_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [net\_if.h](net__if_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
