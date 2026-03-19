---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/net__if_8h_source.html
original_path: doxygen/html/net__if_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
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

23

24#include <[zephyr/device.h](device_8h.md)>

25#include <[zephyr/sys/slist.h](slist_8h.md)>

26#include <[zephyr/sys/iterable\_sections.h](sys_2iterable__sections_8h.md)>

27#include <[zephyr/net/net\_core.h](net__core_8h.md)>

28#include <[zephyr/net/hostname.h](hostname_8h.md)>

29#include <[zephyr/net/net\_linkaddr.h](net__linkaddr_8h.md)>

30#include <[zephyr/net/net\_ip.h](net__ip_8h.md)>

31#include <[zephyr/net/net\_l2.h](net__l2_8h.md)>

32#include <[zephyr/net/net\_stats.h](net__stats_8h.md)>

33#include <[zephyr/net/net\_timeout.h](net__timeout_8h.md)>

34

35#if defined(CONFIG\_NET\_DHCPV4) && defined(CONFIG\_NET\_NATIVE\_IPV4)

36#include <[zephyr/net/dhcpv4.h](dhcpv4_8h.md)>

37#endif

38#if defined(CONFIG\_NET\_DHCPV6) && defined(CONFIG\_NET\_NATIVE\_IPV6)

39#include <[zephyr/net/dhcpv6.h](dhcpv6_8h.md)>

40#endif

41#if defined(CONFIG\_NET\_IPV4\_AUTO) && defined(CONFIG\_NET\_NATIVE\_IPV4)

42#include <[zephyr/net/ipv4\_autoconf.h](ipv4__autoconf_8h.md)>

43#endif

44

45#include <[zephyr/net/prometheus/collector.h](collector_8h.md)>

46

47#ifdef \_\_cplusplus

48extern "C" {

49#endif

50

[ 56](structnet__if__addr.md)struct [net\_if\_addr](structnet__if__addr.md) {

[ 58](structnet__if__addr.md#a06b8d2e8b5ea6d8d671800d966163763) struct net\_addr [address](structnet__if__addr.md#a06b8d2e8b5ea6d8d671800d966163763);

59

[ 63](structnet__if__addr.md#a9abaf23ec98b22d1741bae410a1f7f3e) [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) [atomic\_ref](structnet__if__addr.md#a9abaf23ec98b22d1741bae410a1f7f3e);

64

65#if defined(CONFIG\_NET\_NATIVE\_IPV6)

66 struct [net\_timeout](structnet__timeout.md) lifetime;

67#endif

68

[ 70](structnet__if__addr.md#ab4fd41001cc24615803bfabb9d48e7eb) enum [net\_addr\_type](group__ip__4__6.md#gafecee2d4a331dc85ad962b81a6303e41) [addr\_type](structnet__if__addr.md#ab4fd41001cc24615803bfabb9d48e7eb);

71

[ 73](structnet__if__addr.md#a3106fdcf0dd2479c95efafc586217a2c) enum [net\_addr\_state](group__ip__4__6.md#ga32e58fc83532ef57eeb6ff952f17288d) [addr\_state](structnet__if__addr.md#a3106fdcf0dd2479c95efafc586217a2c);

74

75#if defined(CONFIG\_NET\_NATIVE\_IPV6)

76#if defined(CONFIG\_NET\_IPV6\_PE)

80 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) addr\_create\_time;

81

84 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) addr\_preferred\_lifetime;

85

90 [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) addr\_timeout;

91#endif

92#endif /\* CONFIG\_NET\_NATIVE\_IPV6 \*/

93

94 union {

95#if defined(CONFIG\_NET\_IPV6\_DAD)

96 struct {

98 [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) dad\_node;

99

101 [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) dad\_need\_node;

102

104 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) dad\_start;

105

107 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) dad\_count;

108 };

109#endif /\* CONFIG\_NET\_IPV6\_DAD \*/

110#if defined(CONFIG\_NET\_IPV4\_ACD)

111 struct {

113 [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) acd\_node;

114

116 [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) acd\_need\_node;

117

119 [k\_timepoint\_t](structk__timepoint__t.md) acd\_timeout;

120

122 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) acd\_count;

123

125 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) acd\_state;

126 };

127#endif /\* CONFIG\_NET\_IPV4\_ACD \*/

128 };

129

130#if defined(CONFIG\_NET\_IPV6\_DAD) || defined(CONFIG\_NET\_IPV4\_ACD)

132 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ifindex;

133#endif

134

[ 136](structnet__if__addr.md#a6e799428eb0633a25e4dc3c55e3a3b8c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [is\_infinite](structnet__if__addr.md#a6e799428eb0633a25e4dc3c55e3a3b8c) : 1;

137

[ 139](structnet__if__addr.md#aed4d91ba064d24ad0d53c0960cde0352) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [is\_used](structnet__if__addr.md#aed4d91ba064d24ad0d53c0960cde0352) : 1;

140

[ 142](structnet__if__addr.md#a1db7cc6c7566baf9340dab6771ca5010) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [is\_mesh\_local](structnet__if__addr.md#a1db7cc6c7566baf9340dab6771ca5010) : 1;

143

[ 147](structnet__if__addr.md#a1dd933a37afcb7d708cd602911c38e0a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [is\_temporary](structnet__if__addr.md#a1dd933a37afcb7d708cd602911c38e0a) : 1;

148

[ 150](structnet__if__addr.md#aa556ea52e1f923fd3e39328dc254c365) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [is\_added](structnet__if__addr.md#aa556ea52e1f923fd3e39328dc254c365) : 1;

151

152 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \_unused : 3;

153};

154

[ 160](structnet__if__mcast__addr.md)struct [net\_if\_mcast\_addr](structnet__if__mcast__addr.md) {

[ 162](structnet__if__mcast__addr.md#a3e470fc2eb02ac9e5d3d7d0bea0aaa69) struct net\_addr [address](structnet__if__mcast__addr.md#a3e470fc2eb02ac9e5d3d7d0bea0aaa69);

163

[ 165](structnet__if__mcast__addr.md#a74db1527b3a2b614509cc43fdf7d09ef) [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) [rejoin\_node](structnet__if__mcast__addr.md#a74db1527b3a2b614509cc43fdf7d09ef);

166

167#if defined(CONFIG\_NET\_IPV4\_IGMPV3)

169 struct net\_addr sources[CONFIG\_NET\_IF\_MCAST\_IPV4\_SOURCE\_COUNT];

170

172 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) sources\_len;

173

175 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) record\_type;

176#endif

177

[ 179](structnet__if__mcast__addr.md#abab3e6dba72e24ef522c033d277369ca) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [is\_used](structnet__if__mcast__addr.md#abab3e6dba72e24ef522c033d277369ca) : 1;

180

[ 182](structnet__if__mcast__addr.md#a4af9009b2f9ccc0589a9ba6dac10927b) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [is\_joined](structnet__if__mcast__addr.md#a4af9009b2f9ccc0589a9ba6dac10927b) : 1;

183

184 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \_unused : 6;

185};

186

[ 192](structnet__if__ipv6__prefix.md)struct [net\_if\_ipv6\_prefix](structnet__if__ipv6__prefix.md) {

[ 194](structnet__if__ipv6__prefix.md#a925a97a49d383bd4ce475f5d09fcb7e3) struct [net\_timeout](structnet__timeout.md) [lifetime](structnet__if__ipv6__prefix.md#a925a97a49d383bd4ce475f5d09fcb7e3);

195

[ 197](structnet__if__ipv6__prefix.md#a65b450d0942b3c96cfc575b462d82028) struct [in6\_addr](structin6__addr.md) [prefix](structnet__if__ipv6__prefix.md#a65b450d0942b3c96cfc575b462d82028);

198

[ 200](structnet__if__ipv6__prefix.md#a0e2d1997e2ccfe1e1af5f16e0c74ed92) struct [net\_if](structnet__if.md) \*[iface](structnet__if__ipv6__prefix.md#a0e2d1997e2ccfe1e1af5f16e0c74ed92);

201

[ 203](structnet__if__ipv6__prefix.md#a4d2bc2acbe51256b76cf4d3ced3aac39) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [len](structnet__if__ipv6__prefix.md#a4d2bc2acbe51256b76cf4d3ced3aac39);

204

[ 206](structnet__if__ipv6__prefix.md#a22090441b27bed06098679bf23b4e1e9) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [is\_infinite](structnet__if__ipv6__prefix.md#a22090441b27bed06098679bf23b4e1e9) : 1;

207

[ 209](structnet__if__ipv6__prefix.md#a6a4295256957e5eddf149f1ceff62e3f) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [is\_used](structnet__if__ipv6__prefix.md#a6a4295256957e5eddf149f1ceff62e3f) : 1;

210

211 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \_unused : 6;

212};

213

[ 219](structnet__if__router.md)struct [net\_if\_router](structnet__if__router.md) {

[ 221](structnet__if__router.md#aabbac0cd0a59ca0eafdcfc0eaf5d909a) [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) [node](structnet__if__router.md#aabbac0cd0a59ca0eafdcfc0eaf5d909a);

222

[ 224](structnet__if__router.md#a86a2ca1b95e348acbde8ce90986b83db) struct net\_addr [address](structnet__if__router.md#a86a2ca1b95e348acbde8ce90986b83db);

225

[ 227](structnet__if__router.md#a03789aa0a40f7686b76616de0ca0401a) struct [net\_if](structnet__if.md) \*[iface](structnet__if__router.md#a03789aa0a40f7686b76616de0ca0401a);

228

[ 230](structnet__if__router.md#adf4f4c722917b3c30f8c73bc2519957f) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [life\_start](structnet__if__router.md#adf4f4c722917b3c30f8c73bc2519957f);

231

[ 233](structnet__if__router.md#a4b0d2ad8f225ab61022c10dfce3db199) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [lifetime](structnet__if__router.md#a4b0d2ad8f225ab61022c10dfce3db199);

234

[ 236](structnet__if__router.md#a7196e6d2bc2c958d98dfe29143a62048) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [is\_used](structnet__if__router.md#a7196e6d2bc2c958d98dfe29143a62048) : 1;

237

[ 239](structnet__if__router.md#a34745207edcad2745d6ce311e2bf1894) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [is\_default](structnet__if__router.md#a34745207edcad2745d6ce311e2bf1894) : 1;

240

[ 242](structnet__if__router.md#a4cb47f30241ae3d410f56f1487254ed0) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [is\_infinite](structnet__if__router.md#a4cb47f30241ae3d410f56f1487254ed0) : 1;

243

244 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \_unused : 5;

245};

246

[ 248](group__net__if.md#gae691e5537917ffce27ad0db82c730371)enum [net\_if\_flag](group__net__if.md#gae691e5537917ffce27ad0db82c730371) {

[ 250](group__net__if.md#ggae691e5537917ffce27ad0db82c730371ab0ab7393d643354c46c3437d74c15840) [NET\_IF\_UP](group__net__if.md#ggae691e5537917ffce27ad0db82c730371ab0ab7393d643354c46c3437d74c15840),

251

[ 253](group__net__if.md#ggae691e5537917ffce27ad0db82c730371a3256ef2d537c85b4c2b33b92935e1009) [NET\_IF\_POINTOPOINT](group__net__if.md#ggae691e5537917ffce27ad0db82c730371a3256ef2d537c85b4c2b33b92935e1009),

254

[ 256](group__net__if.md#ggae691e5537917ffce27ad0db82c730371a700d92a5b0de3c779e59806137b35141) [NET\_IF\_PROMISC](group__net__if.md#ggae691e5537917ffce27ad0db82c730371a700d92a5b0de3c779e59806137b35141),

257

[ 264](group__net__if.md#ggae691e5537917ffce27ad0db82c730371a0babb762301878eaf8ef8a05213ecf05) [NET\_IF\_NO\_AUTO\_START](group__net__if.md#ggae691e5537917ffce27ad0db82c730371a0babb762301878eaf8ef8a05213ecf05),

265

[ 267](group__net__if.md#ggae691e5537917ffce27ad0db82c730371aaaeafc62e61ec120609205770c8b54f0) [NET\_IF\_SUSPENDED](group__net__if.md#ggae691e5537917ffce27ad0db82c730371aaaeafc62e61ec120609205770c8b54f0),

268

[ 273](group__net__if.md#ggae691e5537917ffce27ad0db82c730371a581971c9d93a910c4c607da45aa2e4ac) [NET\_IF\_FORWARD\_MULTICASTS](group__net__if.md#ggae691e5537917ffce27ad0db82c730371a581971c9d93a910c4c607da45aa2e4ac),

274

[ 276](group__net__if.md#ggae691e5537917ffce27ad0db82c730371a67d2c0fe390ab16f347ee2dc0a056329) [NET\_IF\_IPV4](group__net__if.md#ggae691e5537917ffce27ad0db82c730371a67d2c0fe390ab16f347ee2dc0a056329),

277

[ 279](group__net__if.md#ggae691e5537917ffce27ad0db82c730371aab31a9e1e8c02159f45efc4e0455a4d6) [NET\_IF\_IPV6](group__net__if.md#ggae691e5537917ffce27ad0db82c730371aab31a9e1e8c02159f45efc4e0455a4d6),

280

[ 282](group__net__if.md#ggae691e5537917ffce27ad0db82c730371add3e2ecdcd5de3154f9bd2836428a25a) [NET\_IF\_RUNNING](group__net__if.md#ggae691e5537917ffce27ad0db82c730371add3e2ecdcd5de3154f9bd2836428a25a),

283

[ 285](group__net__if.md#ggae691e5537917ffce27ad0db82c730371ab1a529826bad6b4bcd04185372f97d6d) [NET\_IF\_LOWER\_UP](group__net__if.md#ggae691e5537917ffce27ad0db82c730371ab1a529826bad6b4bcd04185372f97d6d),

286

[ 288](group__net__if.md#ggae691e5537917ffce27ad0db82c730371a7dd1db72a37b1fbc4c4491ce1c75238d) [NET\_IF\_DORMANT](group__net__if.md#ggae691e5537917ffce27ad0db82c730371a7dd1db72a37b1fbc4c4491ce1c75238d),

289

[ 291](group__net__if.md#ggae691e5537917ffce27ad0db82c730371a542ecce860ef3bf2df493da8d4c6a2f7) [NET\_IF\_IPV6\_NO\_ND](group__net__if.md#ggae691e5537917ffce27ad0db82c730371a542ecce860ef3bf2df493da8d4c6a2f7),

292

[ 294](group__net__if.md#ggae691e5537917ffce27ad0db82c730371a1d362cfabb58eb220ddb069431221fbe) [NET\_IF\_IPV6\_NO\_MLD](group__net__if.md#ggae691e5537917ffce27ad0db82c730371a1d362cfabb58eb220ddb069431221fbe),

295

[ 297](group__net__if.md#ggae691e5537917ffce27ad0db82c730371ae8d564e1577c8daad8ce50a729c500c9) [NET\_IF\_NO\_TX\_LOCK](group__net__if.md#ggae691e5537917ffce27ad0db82c730371ae8d564e1577c8daad8ce50a729c500c9),

298

300 /\* Total number of flags - must be at the end of the enum \*/

301 NET\_IF\_NUM\_FLAGS

303};

304

[ 306](group__net__if.md#gadfe9d90f24046cd9bd4bbee096e747b9)enum [net\_if\_oper\_state](group__net__if.md#gadfe9d90f24046cd9bd4bbee096e747b9) {

[ 307](group__net__if.md#ggadfe9d90f24046cd9bd4bbee096e747b9ac7cae092ea6ceeb62499a9b435ac4b58) [NET\_IF\_OPER\_UNKNOWN](group__net__if.md#ggadfe9d90f24046cd9bd4bbee096e747b9ac7cae092ea6ceeb62499a9b435ac4b58),

[ 308](group__net__if.md#ggadfe9d90f24046cd9bd4bbee096e747b9a8f9f55840e75693163197baae9d50c32) [NET\_IF\_OPER\_NOTPRESENT](group__net__if.md#ggadfe9d90f24046cd9bd4bbee096e747b9a8f9f55840e75693163197baae9d50c32),

[ 309](group__net__if.md#ggadfe9d90f24046cd9bd4bbee096e747b9adb20a95215310c420f8dae7e17a2f367) [NET\_IF\_OPER\_DOWN](group__net__if.md#ggadfe9d90f24046cd9bd4bbee096e747b9adb20a95215310c420f8dae7e17a2f367),

[ 310](group__net__if.md#ggadfe9d90f24046cd9bd4bbee096e747b9ae7e9b8b12ae618a5ee1483dee916aab4) [NET\_IF\_OPER\_LOWERLAYERDOWN](group__net__if.md#ggadfe9d90f24046cd9bd4bbee096e747b9ae7e9b8b12ae618a5ee1483dee916aab4),

[ 311](group__net__if.md#ggadfe9d90f24046cd9bd4bbee096e747b9a2240173b5c247ab5eb0a9a6afafb296f) [NET\_IF\_OPER\_TESTING](group__net__if.md#ggadfe9d90f24046cd9bd4bbee096e747b9a2240173b5c247ab5eb0a9a6afafb296f),

[ 312](group__net__if.md#ggadfe9d90f24046cd9bd4bbee096e747b9a5cbe2aa27a444444d4acf122113d430d) [NET\_IF\_OPER\_DORMANT](group__net__if.md#ggadfe9d90f24046cd9bd4bbee096e747b9a5cbe2aa27a444444d4acf122113d430d),

[ 313](group__net__if.md#ggadfe9d90f24046cd9bd4bbee096e747b9a6b99bfc28d831292029761d74209ee03) [NET\_IF\_OPER\_UP](group__net__if.md#ggadfe9d90f24046cd9bd4bbee096e747b9a6b99bfc28d831292029761d74209ee03),

314} \_\_packed;

315

316#if defined(CONFIG\_NET\_OFFLOAD)

317struct net\_offload;

318#endif /\* CONFIG\_NET\_OFFLOAD \*/

319

321#if defined(CONFIG\_NET\_IPV6)

322#define NET\_IF\_MAX\_IPV6\_ADDR CONFIG\_NET\_IF\_UNICAST\_IPV6\_ADDR\_COUNT

323#define NET\_IF\_MAX\_IPV6\_MADDR CONFIG\_NET\_IF\_MCAST\_IPV6\_ADDR\_COUNT

324#define NET\_IF\_MAX\_IPV6\_PREFIX CONFIG\_NET\_IF\_IPV6\_PREFIX\_COUNT

325#else

326#define NET\_IF\_MAX\_IPV6\_ADDR 0

327#define NET\_IF\_MAX\_IPV6\_MADDR 0

328#define NET\_IF\_MAX\_IPV6\_PREFIX 0

329#endif

330/\* @endcond \*/

331

[ 333](structnet__if__ipv6.md)struct [net\_if\_ipv6](structnet__if__ipv6.md) {

[ 335](structnet__if__ipv6.md#adb6431d336cc3f46972e13d2255452c8) struct [net\_if\_addr](structnet__if__addr.md) [unicast](structnet__if__ipv6.md#adb6431d336cc3f46972e13d2255452c8)[NET\_IF\_MAX\_IPV6\_ADDR];

336

[ 338](structnet__if__ipv6.md#a727d2773e0dee3be687dda5b2dd55682) struct [net\_if\_mcast\_addr](structnet__if__mcast__addr.md) [mcast](structnet__if__ipv6.md#a727d2773e0dee3be687dda5b2dd55682)[NET\_IF\_MAX\_IPV6\_MADDR];

339

[ 341](structnet__if__ipv6.md#a2dccdc984f08527302d8d910a2658f72) struct [net\_if\_ipv6\_prefix](structnet__if__ipv6__prefix.md) [prefix](structnet__if__ipv6.md#a2dccdc984f08527302d8d910a2658f72)[NET\_IF\_MAX\_IPV6\_PREFIX];

342

[ 344](structnet__if__ipv6.md#a500a78fe23ee2ebc63f3d3b53b5b92ea) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [base\_reachable\_time](structnet__if__ipv6.md#a500a78fe23ee2ebc63f3d3b53b5b92ea);

345

[ 347](structnet__if__ipv6.md#af57b7dca189167f8cc757c4ed6b08f2f) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [reachable\_time](structnet__if__ipv6.md#af57b7dca189167f8cc757c4ed6b08f2f);

348

[ 350](structnet__if__ipv6.md#ac5ee47ff9d3e429ecbb8623e5d713246) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [retrans\_timer](structnet__if__ipv6.md#ac5ee47ff9d3e429ecbb8623e5d713246);

351

352#if defined(CONFIG\_NET\_IPV6\_IID\_STABLE)

354 struct [net\_if\_addr](structnet__if__addr.md) \*iid;

355

359 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) network\_counter;

360#endif /\* CONFIG\_NET\_IPV6\_IID\_STABLE \*/

361

362#if defined(CONFIG\_NET\_IPV6\_PE)

367 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) desync\_factor;

368#endif /\* CONFIG\_NET\_IPV6\_PE \*/

369

370#if defined(CONFIG\_NET\_IPV6\_ND) && defined(CONFIG\_NET\_NATIVE\_IPV6)

372 [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) rs\_node;

373

374 /\* RS start time \*/

375 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) rs\_start;

376

378 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) rs\_count;

379#endif

380

[ 382](structnet__if__ipv6.md#a71775a082984274fbc7c009ead18e751) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [hop\_limit](structnet__if__ipv6.md#a71775a082984274fbc7c009ead18e751);

383

[ 385](structnet__if__ipv6.md#ae94906c28578f2e1ea2506b0e2972d4c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [mcast\_hop\_limit](structnet__if__ipv6.md#ae94906c28578f2e1ea2506b0e2972d4c);

386};

387

388#if defined(CONFIG\_NET\_DHCPV6) && defined(CONFIG\_NET\_NATIVE\_IPV6)

390struct net\_if\_dhcpv6 {

392 [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) node;

393

395 struct net\_dhcpv6\_duid\_storage clientid;

396

398 struct net\_dhcpv6\_duid\_storage serverid;

399

401 enum net\_dhcpv6\_state [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90);

402

404 struct [net\_dhcpv6\_params](structnet__dhcpv6__params.md) params;

405

407 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) timeout;

408

410 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) exchange\_start;

411

413 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) t1;

414

416 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) t2;

417

421 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) expire;

422

424 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) addr\_iaid;

425

427 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) prefix\_iaid;

428

430 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) retransmit\_timeout;

431

433 [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) server\_preference;

434

436 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) retransmissions;

437

439 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) tid[DHCPV6\_TID\_SIZE];

440

442 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) prefix\_len;

443

445 struct [in6\_addr](structin6__addr.md) prefix;

446

448 struct [in6\_addr](structin6__addr.md) addr;

449};

450#endif /\* defined(CONFIG\_NET\_DHCPV6) && defined(CONFIG\_NET\_NATIVE\_IPV6) \*/

451

453#if defined(CONFIG\_NET\_IPV4)

454#define NET\_IF\_MAX\_IPV4\_ADDR CONFIG\_NET\_IF\_UNICAST\_IPV4\_ADDR\_COUNT

455#define NET\_IF\_MAX\_IPV4\_MADDR CONFIG\_NET\_IF\_MCAST\_IPV4\_ADDR\_COUNT

456#else

457#define NET\_IF\_MAX\_IPV4\_ADDR 0

458#define NET\_IF\_MAX\_IPV4\_MADDR 0

459#endif

461

[ 467](structnet__if__addr__ipv4.md)struct [net\_if\_addr\_ipv4](structnet__if__addr__ipv4.md) {

[ 469](structnet__if__addr__ipv4.md#a9d8924e263cc7401569c934533a04b48) struct [net\_if\_addr](structnet__if__addr.md) [ipv4](structnet__if__addr__ipv4.md#a9d8924e263cc7401569c934533a04b48);

[ 471](structnet__if__addr__ipv4.md#ae1720720e7e36ccf38d0b282d3150774) struct [in\_addr](structin__addr.md) [netmask](structnet__if__addr__ipv4.md#ae1720720e7e36ccf38d0b282d3150774);

472};

473

[ 475](structnet__if__ipv4.md)struct [net\_if\_ipv4](structnet__if__ipv4.md) {

[ 477](structnet__if__ipv4.md#a806cf92123452ed3aa93540803b0a8d3) struct [net\_if\_addr\_ipv4](structnet__if__addr__ipv4.md) [unicast](structnet__if__ipv4.md#a806cf92123452ed3aa93540803b0a8d3)[NET\_IF\_MAX\_IPV4\_ADDR];

478

[ 480](structnet__if__ipv4.md#adfaf5b50255bd35297195a7218729ae7) struct [net\_if\_mcast\_addr](structnet__if__mcast__addr.md) [mcast](structnet__if__ipv4.md#adfaf5b50255bd35297195a7218729ae7)[NET\_IF\_MAX\_IPV4\_MADDR];

481

[ 483](structnet__if__ipv4.md#aa24772c7202bf465ee3da94a172b7bcb) struct [in\_addr](structin__addr.md) [gw](structnet__if__ipv4.md#aa24772c7202bf465ee3da94a172b7bcb);

484

[ 486](structnet__if__ipv4.md#acdc6d5d6eb5362f4f6d2c027cc40e684) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [ttl](structnet__if__ipv4.md#acdc6d5d6eb5362f4f6d2c027cc40e684);

487

[ 489](structnet__if__ipv4.md#a7e9bf16d51989cfcfe564f4f0a43b480) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [mcast\_ttl](structnet__if__ipv4.md#a7e9bf16d51989cfcfe564f4f0a43b480);

490

491#if defined(CONFIG\_NET\_IPV4\_ACD)

493 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) conflict\_cnt;

494#endif

495};

496

497#if defined(CONFIG\_NET\_DHCPV4) && defined(CONFIG\_NET\_NATIVE\_IPV4)

498struct net\_if\_dhcpv4 {

500 [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) node;

501

503 [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) timer\_start;

504

506 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) request\_time;

507

508 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) xid;

509

511 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) lease\_time;

512

514 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) renewal\_time;

515

517 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) rebinding\_time;

518

520 struct [in\_addr](structin__addr.md) server\_id;

521

523 struct [in\_addr](structin__addr.md) requested\_ip;

524

526 struct [in\_addr](structin__addr.md) netmask;

527

532 enum net\_dhcpv4\_state [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90);

533

535 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) attempts;

536

538 struct [in\_addr](structin__addr.md) request\_server\_addr;

539

541 struct [in\_addr](structin__addr.md) response\_src\_addr;

542

543#ifdef CONFIG\_NET\_DHCPV4\_OPTION\_NTP\_SERVER

545 struct [in\_addr](structin__addr.md) ntp\_addr;

546#endif

547};

548#endif /\* CONFIG\_NET\_DHCPV4 \*/

549

550#if defined(CONFIG\_NET\_IPV4\_AUTO) && defined(CONFIG\_NET\_NATIVE\_IPV4)

551struct net\_if\_ipv4\_autoconf {

553 struct net\_if \*iface;

554

556 struct in\_addr requested\_ip;

557

560 enum [net\_ipv4\_autoconf\_state](ipv4__autoconf_8h.md#abdf8bb08f12768aad2ff95b902bdc899) [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90);

561};

562#endif /\* CONFIG\_NET\_IPV4\_AUTO \*/

563

565/\* We always need to have at least one IP config \*/

566#define NET\_IF\_MAX\_CONFIGS 1

568

[ 572](structnet__if__ip.md)struct [net\_if\_ip](structnet__if__ip.md) {

573#if defined(CONFIG\_NET\_IPV6)

574 struct [net\_if\_ipv6](structnet__if__ipv6.md) \*ipv6;

575#endif /\* CONFIG\_NET\_IPV6 \*/

576

577#if defined(CONFIG\_NET\_IPV4)

578 struct [net\_if\_ipv4](structnet__if__ipv4.md) \*ipv4;

579#endif /\* CONFIG\_NET\_IPV4 \*/

580};

581

[ 585](structnet__if__config.md)struct [net\_if\_config](structnet__if__config.md) {

586#if defined(CONFIG\_NET\_IP)

588 struct [net\_if\_ip](structnet__if__ip.md) ip;

589#endif

590

591#if defined(CONFIG\_NET\_DHCPV4) && defined(CONFIG\_NET\_NATIVE\_IPV4)

592 struct net\_if\_dhcpv4 dhcpv4;

593#endif /\* CONFIG\_NET\_DHCPV4 \*/

594

595#if defined(CONFIG\_NET\_DHCPV6) && defined(CONFIG\_NET\_NATIVE\_IPV6)

596 struct net\_if\_dhcpv6 dhcpv6;

597#endif /\* CONFIG\_NET\_DHCPV6 \*/

598

599#if defined(CONFIG\_NET\_IPV4\_AUTO) && defined(CONFIG\_NET\_NATIVE\_IPV4)

600 struct net\_if\_ipv4\_autoconf ipv4auto;

601#endif /\* CONFIG\_NET\_IPV4\_AUTO \*/

602

603#if defined(CONFIG\_NET\_L2\_VIRTUAL)

608 [sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8) virtual\_interfaces;

609#endif /\* CONFIG\_NET\_L2\_VIRTUAL \*/

610

611#if defined(CONFIG\_NET\_INTERFACE\_NAME)

616 char name[CONFIG\_NET\_INTERFACE\_NAME\_LEN + 1];

617#endif

618};

619

[ 629](structnet__traffic__class.md)struct [net\_traffic\_class](structnet__traffic__class.md) {

[ 631](structnet__traffic__class.md#a94511ca12bad1687f5c7ca862c857ded) struct [k\_fifo](structk__fifo.md) [fifo](structnet__traffic__class.md#a94511ca12bad1687f5c7ca862c857ded);

632

633#if NET\_TC\_COUNT > 1 || defined(CONFIG\_NET\_TC\_TX\_SKIP\_FOR\_HIGH\_PRIO) \

634 || defined(CONFIG\_NET\_TC\_RX\_SKIP\_FOR\_HIGH\_PRIO)

636 struct k\_sem fifo\_slot;

637#endif

638

[ 640](structnet__traffic__class.md#a8d0023588fee0a8ff1381bbc80ada143) struct [k\_thread](structk__thread.md) [handler](structnet__traffic__class.md#a8d0023588fee0a8ff1381bbc80ada143);

641

[ 643](structnet__traffic__class.md#a2d98bc68d38bdef649d645b8b52516c5) [k\_thread\_stack\_t](arch__interface_8h.md#a9fc2dce533bd7b8cb1fdd4bdbb2b62b1) \*[stack](structnet__traffic__class.md#a2d98bc68d38bdef649d645b8b52516c5);

644};

645

[ 652](group__net__if.md#gaef3dfe26195514aac625e9f22e399759)typedef int (\*[net\_socket\_create\_t](group__net__if.md#gaef3dfe26195514aac625e9f22e399759))(int, int, int);

653

[ 668](structnet__if__dev.md)struct [net\_if\_dev](structnet__if__dev.md) {

[ 670](structnet__if__dev.md#aab633a44f165f571910dc9fc9e131c50) const struct [device](structdevice.md) \*[dev](structnet__if__dev.md#aab633a44f165f571910dc9fc9e131c50);

671

[ 673](structnet__if__dev.md#a85d713c62875f5fe9e3ec29773150797) const struct [net\_l2](structnet__l2.md) \* const [l2](structnet__if__dev.md#a85d713c62875f5fe9e3ec29773150797);

674

[ 676](structnet__if__dev.md#a8fec6a7f612fc1268ef486d8bdebe018) void \*[l2\_data](structnet__if__dev.md#a8fec6a7f612fc1268ef486d8bdebe018);

677

[ 679](structnet__if__dev.md#ac8f9c30e1dea05c28c88d3b367b130f5) [ATOMIC\_DEFINE](group__atomic__apis.md#ga249c575db9764486197709b327f7370e)([flags](structnet__if__dev.md#ac8f9c30e1dea05c28c88d3b367b130f5), NET\_IF\_NUM\_FLAGS);

680

[ 682](structnet__if__dev.md#aac6d5d341ab520e6aac7f7b03737c197) struct [net\_linkaddr](structnet__linkaddr.md) [link\_addr](structnet__if__dev.md#aac6d5d341ab520e6aac7f7b03737c197);

683

684#if defined(CONFIG\_NET\_OFFLOAD)

690 struct net\_offload \*offload;

691#endif /\* CONFIG\_NET\_OFFLOAD \*/

692

[ 694](structnet__if__dev.md#aa15ccca2eb67b8d2afca153ccacb3742) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [mtu](structnet__if__dev.md#aa15ccca2eb67b8d2afca153ccacb3742);

695

696#if defined(CONFIG\_NET\_SOCKETS\_OFFLOAD)

700 [net\_socket\_create\_t](group__net__if.md#gaef3dfe26195514aac625e9f22e399759) socket\_offload;

701#endif /\* CONFIG\_NET\_SOCKETS\_OFFLOAD \*/

702

[ 704](structnet__if__dev.md#a30eabb2ffae082d0de81a50c510738a3) enum [net\_if\_oper\_state](group__net__if.md#gadfe9d90f24046cd9bd4bbee096e747b9) [oper\_state](structnet__if__dev.md#a30eabb2ffae082d0de81a50c510738a3);

705};

706

[ 714](structnet__if.md)struct [net\_if](structnet__if.md) {

[ 716](structnet__if.md#a0982ba2019cdaa7701162e60fdb2171e) struct [net\_if\_dev](structnet__if__dev.md) \*[if\_dev](structnet__if.md#a0982ba2019cdaa7701162e60fdb2171e);

717

718#if defined(CONFIG\_NET\_STATISTICS\_PER\_INTERFACE)

720 struct [net\_stats](structnet__stats.md) stats;

721

723 [IF\_ENABLED](group__sys-util.md#gae67ffe50e848951dbde309ed569ea925)(CONFIG\_NET\_STATISTICS\_VIA\_PROMETHEUS,

724 (struct [prometheus\_collector](structprometheus__collector.md) \*collector);)

725#endif /\* CONFIG\_NET\_STATISTICS\_PER\_INTERFACE \*/

726

[ 728](structnet__if.md#a5e71962f55bdead7bfbbb96518c6c404) struct [net\_if\_config](structnet__if__config.md) [config](structnet__if.md#a5e71962f55bdead7bfbbb96518c6c404);

729

730#if defined(CONFIG\_NET\_POWER\_MANAGEMENT)

735 int tx\_pending;

736#endif

737

[ 739](structnet__if.md#ace2233b71da53ff0fc7cd564ccfc5a03) struct [k\_mutex](structk__mutex.md) [lock](structnet__if.md#ace2233b71da53ff0fc7cd564ccfc5a03);

740

[ 742](structnet__if.md#af00f729ebddfdcf725169f61b6cd586b) struct [k\_mutex](structk__mutex.md) [tx\_lock](structnet__if.md#af00f729ebddfdcf725169f61b6cd586b);

743

[ 748](structnet__if.md#aa96a6a2d55f6a4ece2f340eef526ef56) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [pe\_enabled](structnet__if.md#aa96a6a2d55f6a4ece2f340eef526ef56) : 1;

749

[ 753](structnet__if.md#aec585e283c9053443ff05b364acf76eb) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [pe\_prefer\_public](structnet__if.md#aec585e283c9053443ff05b364acf76eb) : 1;

754

756 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \_unused : 6;

757};

758

760

761static inline void net\_if\_lock(struct [net\_if](structnet__if.md) \*iface)

762{

763 NET\_ASSERT(iface);

764

765 (void)[k\_mutex\_lock](group__mutex__apis.md#ga850549358645249c285669baa49c33b0)(&iface->[lock](structnet__if.md#ace2233b71da53ff0fc7cd564ccfc5a03), [K\_FOREVER](group__clock__apis.md#ga0bb4b83f0222193b21a8910311bab0ca));

766}

767

768static inline void net\_if\_unlock(struct [net\_if](structnet__if.md) \*iface)

769{

770 NET\_ASSERT(iface);

771

772 [k\_mutex\_unlock](group__mutex__apis.md#ga360f4c0e7258b0d7030cdb1f452b2c31)(&iface->[lock](structnet__if.md#ace2233b71da53ff0fc7cd564ccfc5a03));

773}

774

775static inline bool [net\_if\_flag\_is\_set](group__net__if.md#gae1f373ddd61c18a81481d8ddcfb12543)(struct [net\_if](structnet__if.md) \*iface,

776 enum [net\_if\_flag](group__net__if.md#gae691e5537917ffce27ad0db82c730371) value);

777

778static inline void net\_if\_tx\_lock(struct [net\_if](structnet__if.md) \*iface)

779{

780 NET\_ASSERT(iface);

781

782 if ([net\_if\_flag\_is\_set](group__net__if.md#gae1f373ddd61c18a81481d8ddcfb12543)(iface, [NET\_IF\_NO\_TX\_LOCK](group__net__if.md#ggae691e5537917ffce27ad0db82c730371ae8d564e1577c8daad8ce50a729c500c9))) {

783 return;

784 }

785

786 (void)[k\_mutex\_lock](group__mutex__apis.md#ga850549358645249c285669baa49c33b0)(&iface->[tx\_lock](structnet__if.md#af00f729ebddfdcf725169f61b6cd586b), [K\_FOREVER](group__clock__apis.md#ga0bb4b83f0222193b21a8910311bab0ca));

787}

788

789static inline void net\_if\_tx\_unlock(struct [net\_if](structnet__if.md) \*iface)

790{

791 NET\_ASSERT(iface);

792

793 if ([net\_if\_flag\_is\_set](group__net__if.md#gae1f373ddd61c18a81481d8ddcfb12543)(iface, [NET\_IF\_NO\_TX\_LOCK](group__net__if.md#ggae691e5537917ffce27ad0db82c730371ae8d564e1577c8daad8ce50a729c500c9))) {

794 return;

795 }

796

797 [k\_mutex\_unlock](group__mutex__apis.md#ga360f4c0e7258b0d7030cdb1f452b2c31)(&iface->[tx\_lock](structnet__if.md#af00f729ebddfdcf725169f61b6cd586b));

798}

799

801

[ 808](group__net__if.md#ga52f9fca13e9f836799e0e40f581744d2)static inline void [net\_if\_flag\_set](group__net__if.md#ga52f9fca13e9f836799e0e40f581744d2)(struct [net\_if](structnet__if.md) \*iface,

809 enum [net\_if\_flag](group__net__if.md#gae691e5537917ffce27ad0db82c730371) value)

810{

811 if (iface == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4) || iface->[if\_dev](structnet__if.md#a0982ba2019cdaa7701162e60fdb2171e) == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

812 return;

813 }

814

815 [atomic\_set\_bit](group__atomic__apis.md#ga17a3961ba7610ad6e595e602f70344a0)(iface->[if\_dev](structnet__if.md#a0982ba2019cdaa7701162e60fdb2171e)->[flags](structnet__if__dev.md#ac8f9c30e1dea05c28c88d3b367b130f5), value);

816}

817

[ 826](group__net__if.md#ga42e7482191a92007960601f8bb621dca)static inline bool [net\_if\_flag\_test\_and\_set](group__net__if.md#ga42e7482191a92007960601f8bb621dca)(struct [net\_if](structnet__if.md) \*iface,

827 enum [net\_if\_flag](group__net__if.md#gae691e5537917ffce27ad0db82c730371) value)

828{

829 if (iface == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4) || iface->[if\_dev](structnet__if.md#a0982ba2019cdaa7701162e60fdb2171e) == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

830 return false;

831 }

832

833 return [atomic\_test\_and\_set\_bit](group__atomic__apis.md#ga7ff45e13aa5f8be5d7a550e49f5c720b)(iface->[if\_dev](structnet__if.md#a0982ba2019cdaa7701162e60fdb2171e)->[flags](structnet__if__dev.md#ac8f9c30e1dea05c28c88d3b367b130f5), value);

834}

835

[ 842](group__net__if.md#gaff751b6a92b0c608ecfc50e8c0587fd3)static inline void [net\_if\_flag\_clear](group__net__if.md#gaff751b6a92b0c608ecfc50e8c0587fd3)(struct [net\_if](structnet__if.md) \*iface,

843 enum [net\_if\_flag](group__net__if.md#gae691e5537917ffce27ad0db82c730371) value)

844{

845 if (iface == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4) || iface->[if\_dev](structnet__if.md#a0982ba2019cdaa7701162e60fdb2171e) == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

846 return;

847 }

848

849 [atomic\_clear\_bit](group__atomic__apis.md#ga1c1693d524c49d11fd32b323a39d718e)(iface->[if\_dev](structnet__if.md#a0982ba2019cdaa7701162e60fdb2171e)->[flags](structnet__if__dev.md#ac8f9c30e1dea05c28c88d3b367b130f5), value);

850}

851

[ 860](group__net__if.md#gab8f371c7f8890cf4728177f6595141d7)static inline bool [net\_if\_flag\_test\_and\_clear](group__net__if.md#gab8f371c7f8890cf4728177f6595141d7)(struct [net\_if](structnet__if.md) \*iface,

861 enum [net\_if\_flag](group__net__if.md#gae691e5537917ffce27ad0db82c730371) value)

862{

863 if (iface == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4) || iface->[if\_dev](structnet__if.md#a0982ba2019cdaa7701162e60fdb2171e) == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

864 return false;

865 }

866

867 return [atomic\_test\_and\_clear\_bit](group__atomic__apis.md#ga53159437721084da0ec8ee70ec212472)(iface->[if\_dev](structnet__if.md#a0982ba2019cdaa7701162e60fdb2171e)->[flags](structnet__if__dev.md#ac8f9c30e1dea05c28c88d3b367b130f5), value);

868}

869

[ 878](group__net__if.md#gae1f373ddd61c18a81481d8ddcfb12543)static inline bool [net\_if\_flag\_is\_set](group__net__if.md#gae1f373ddd61c18a81481d8ddcfb12543)(struct [net\_if](structnet__if.md) \*iface,

879 enum [net\_if\_flag](group__net__if.md#gae691e5537917ffce27ad0db82c730371) value)

880{

881 if (iface == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4) || iface->[if\_dev](structnet__if.md#a0982ba2019cdaa7701162e60fdb2171e) == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

882 return false;

883 }

884

885 return [atomic\_test\_bit](group__atomic__apis.md#ga190ddc108f45e7649689753c08658eae)(iface->[if\_dev](structnet__if.md#a0982ba2019cdaa7701162e60fdb2171e)->[flags](structnet__if__dev.md#ac8f9c30e1dea05c28c88d3b367b130f5), value);

886}

887

[ 896](group__net__if.md#ga1f1bf845e63cce02e2183889cc85d57e)static inline enum [net\_if\_oper\_state](group__net__if.md#gadfe9d90f24046cd9bd4bbee096e747b9) [net\_if\_oper\_state\_set](group__net__if.md#ga1f1bf845e63cce02e2183889cc85d57e)(

897 struct [net\_if](structnet__if.md) \*iface, enum [net\_if\_oper\_state](group__net__if.md#gadfe9d90f24046cd9bd4bbee096e747b9) oper\_state)

898{

899 if (iface == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4) || iface->[if\_dev](structnet__if.md#a0982ba2019cdaa7701162e60fdb2171e) == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

900 return [NET\_IF\_OPER\_UNKNOWN](group__net__if.md#ggadfe9d90f24046cd9bd4bbee096e747b9ac7cae092ea6ceeb62499a9b435ac4b58);

901 }

902

903 BUILD\_ASSERT((enum [net\_if\_oper\_state](group__net__if.md#gadfe9d90f24046cd9bd4bbee096e747b9))(-1) > 0 && [NET\_IF\_OPER\_UNKNOWN](group__net__if.md#ggadfe9d90f24046cd9bd4bbee096e747b9ac7cae092ea6ceeb62499a9b435ac4b58) == 0);

904 if (oper\_state <= [NET\_IF\_OPER\_UP](group__net__if.md#ggadfe9d90f24046cd9bd4bbee096e747b9a6b99bfc28d831292029761d74209ee03)) {

905 iface->[if\_dev](structnet__if.md#a0982ba2019cdaa7701162e60fdb2171e)->[oper\_state](structnet__if__dev.md#a30eabb2ffae082d0de81a50c510738a3) = oper\_state;

906 }

907

908 return iface->[if\_dev](structnet__if.md#a0982ba2019cdaa7701162e60fdb2171e)->[oper\_state](structnet__if__dev.md#a30eabb2ffae082d0de81a50c510738a3);

909}

910

[ 918](group__net__if.md#gad9e957a4866b4566296ee39392fde0e4)static inline enum [net\_if\_oper\_state](group__net__if.md#gadfe9d90f24046cd9bd4bbee096e747b9) [net\_if\_oper\_state](group__net__if.md#gadfe9d90f24046cd9bd4bbee096e747b9)(struct [net\_if](structnet__if.md) \*iface)

919{

920 if (iface == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4) || iface->[if\_dev](structnet__if.md#a0982ba2019cdaa7701162e60fdb2171e) == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

921 return [NET\_IF\_OPER\_UNKNOWN](group__net__if.md#ggadfe9d90f24046cd9bd4bbee096e747b9ac7cae092ea6ceeb62499a9b435ac4b58);

922 }

923

924 return iface->[if\_dev](structnet__if.md#a0982ba2019cdaa7701162e60fdb2171e)->[oper\_state](structnet__if__dev.md#a30eabb2ffae082d0de81a50c510738a3);

925}

926

[ 935](group__net__if.md#gada0398d757eab28d16a129692c309f4d)enum [net\_verdict](group__net__core.md#ga8e5393f3bdd85491f221324e637c3896) [net\_if\_send\_data](group__net__if.md#gada0398d757eab28d16a129692c309f4d)(struct [net\_if](structnet__if.md) \*iface, struct [net\_pkt](structnet__pkt.md) \*pkt);

936

[ 944](group__net__if.md#gafa451f6118529d1d084704d00b2aae20)static inline const struct [net\_l2](structnet__l2.md) \*[net\_if\_l2](group__net__if.md#gafa451f6118529d1d084704d00b2aae20)(struct [net\_if](structnet__if.md) \*iface)

945{

946 if (iface == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4) || iface->[if\_dev](structnet__if.md#a0982ba2019cdaa7701162e60fdb2171e) == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

947 return [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4);

948 }

949

950 return iface->[if\_dev](structnet__if.md#a0982ba2019cdaa7701162e60fdb2171e)->[l2](structnet__if__dev.md#a85d713c62875f5fe9e3ec29773150797);

951}

952

[ 961](group__net__if.md#ga72ed21ca0cb220199f5a2070137c7fef)enum [net\_verdict](group__net__core.md#ga8e5393f3bdd85491f221324e637c3896) [net\_if\_recv\_data](group__net__if.md#ga72ed21ca0cb220199f5a2070137c7fef)(struct [net\_if](structnet__if.md) \*iface, struct [net\_pkt](structnet__pkt.md) \*pkt);

962

[ 970](group__net__if.md#ga3cad2d51fc9cc225619585e06e252db0)static inline void \*[net\_if\_l2\_data](group__net__if.md#ga3cad2d51fc9cc225619585e06e252db0)(struct [net\_if](structnet__if.md) \*iface)

971{

972 if (iface == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4) || iface->[if\_dev](structnet__if.md#a0982ba2019cdaa7701162e60fdb2171e) == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

973 return [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4);

974 }

975

976 return iface->[if\_dev](structnet__if.md#a0982ba2019cdaa7701162e60fdb2171e)->[l2\_data](structnet__if__dev.md#a8fec6a7f612fc1268ef486d8bdebe018);

977}

978

[ 986](group__net__if.md#gaeb8c703f273bc07ae9bb7a0d8bfe6f3d)static inline const struct [device](structdevice.md) \*[net\_if\_get\_device](group__net__if.md#gaeb8c703f273bc07ae9bb7a0d8bfe6f3d)(struct [net\_if](structnet__if.md) \*iface)

987{

988 if (iface == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4) || iface->[if\_dev](structnet__if.md#a0982ba2019cdaa7701162e60fdb2171e) == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

989 return [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4);

990 }

991

992 return iface->[if\_dev](structnet__if.md#a0982ba2019cdaa7701162e60fdb2171e)->[dev](structnet__if__dev.md#aab633a44f165f571910dc9fc9e131c50);

993}

994

[ 1001](group__net__if.md#ga56c4d37edcea540be09ebcdf97265aed)void [net\_if\_queue\_tx](group__net__if.md#ga56c4d37edcea540be09ebcdf97265aed)(struct [net\_if](structnet__if.md) \*iface, struct [net\_pkt](structnet__pkt.md) \*pkt);

1002

[ 1010](group__net__if.md#ga6bfa5f84a2127bbad27a0a3b319526a1)static inline bool [net\_if\_is\_ip\_offloaded](group__net__if.md#ga6bfa5f84a2127bbad27a0a3b319526a1)(struct [net\_if](structnet__if.md) \*iface)

1011{

1012#if defined(CONFIG\_NET\_OFFLOAD)

1013 return (iface != [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4) && iface->[if\_dev](structnet__if.md#a0982ba2019cdaa7701162e60fdb2171e) != [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4) &&

1014 iface->[if\_dev](structnet__if.md#a0982ba2019cdaa7701162e60fdb2171e)->offload != [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4));

1015#else

1016 ARG\_UNUSED(iface);

1017

1018 return false;

1019#endif

1020}

1021

[ 1029](group__net__if.md#gaecedc93a6dab2c57fe686718ea4d78af)bool [net\_if\_is\_offloaded](group__net__if.md#gaecedc93a6dab2c57fe686718ea4d78af)(struct [net\_if](structnet__if.md) \*iface);

1030

[ 1038](group__net__if.md#ga520939e94620ca75475a71f153df6d4a)static inline struct net\_offload \*[net\_if\_offload](group__net__if.md#ga520939e94620ca75475a71f153df6d4a)(struct [net\_if](structnet__if.md) \*iface)

1039{

1040#if defined(CONFIG\_NET\_OFFLOAD)

1041 if (iface == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4) || iface->[if\_dev](structnet__if.md#a0982ba2019cdaa7701162e60fdb2171e) == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

1042 return [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4);

1043 }

1044

1045 return iface->[if\_dev](structnet__if.md#a0982ba2019cdaa7701162e60fdb2171e)->offload;

1046#else

1047 ARG\_UNUSED(iface);

1048

1049 return [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4);

1050#endif

1051}

1052

[ 1060](group__net__if.md#gaf308baf2241fa455b50b439b7fab3f1e)static inline bool [net\_if\_is\_socket\_offloaded](group__net__if.md#gaf308baf2241fa455b50b439b7fab3f1e)(struct [net\_if](structnet__if.md) \*iface)

1061{

1062#if defined(CONFIG\_NET\_SOCKETS\_OFFLOAD)

1063 if (iface == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4) || iface->[if\_dev](structnet__if.md#a0982ba2019cdaa7701162e60fdb2171e) == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

1064 return false;

1065 }

1066

1067 return (iface->[if\_dev](structnet__if.md#a0982ba2019cdaa7701162e60fdb2171e)->socket\_offload != [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4));

1068#else

1069 ARG\_UNUSED(iface);

1070

1071 return false;

1072#endif

1073}

1074

[ 1081](group__net__if.md#ga9db52875580115c743b1f35cd6c46796)static inline void [net\_if\_socket\_offload\_set](group__net__if.md#ga9db52875580115c743b1f35cd6c46796)(

1082 struct [net\_if](structnet__if.md) \*iface, [net\_socket\_create\_t](group__net__if.md#gaef3dfe26195514aac625e9f22e399759) socket\_offload)

1083{

1084#if defined(CONFIG\_NET\_SOCKETS\_OFFLOAD)

1085 if (iface == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4) || iface->[if\_dev](structnet__if.md#a0982ba2019cdaa7701162e60fdb2171e) == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

1086 return;

1087 }

1088

1089 iface->[if\_dev](structnet__if.md#a0982ba2019cdaa7701162e60fdb2171e)->socket\_offload = socket\_offload;

1090#else

1091 ARG\_UNUSED(iface);

1092 ARG\_UNUSED(socket\_offload);

1093#endif

1094}

1095

[ 1103](group__net__if.md#gafb2bbaec96c4759d920b2866c0b3ef3a)static inline [net\_socket\_create\_t](group__net__if.md#gaef3dfe26195514aac625e9f22e399759) [net\_if\_socket\_offload](group__net__if.md#gafb2bbaec96c4759d920b2866c0b3ef3a)(struct [net\_if](structnet__if.md) \*iface)

1104{

1105#if defined(CONFIG\_NET\_SOCKETS\_OFFLOAD)

1106 if (iface == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4) || iface->[if\_dev](structnet__if.md#a0982ba2019cdaa7701162e60fdb2171e) == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

1107 return [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4);

1108 }

1109

1110 return iface->[if\_dev](structnet__if.md#a0982ba2019cdaa7701162e60fdb2171e)->socket\_offload;

1111#else

1112 ARG\_UNUSED(iface);

1113

1114 return [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4);

1115#endif

1116}

1117

[ 1125](group__net__if.md#ga467186e964bf721e14fed38392f21872)static inline struct [net\_linkaddr](structnet__linkaddr.md) \*[net\_if\_get\_link\_addr](group__net__if.md#ga467186e964bf721e14fed38392f21872)(struct [net\_if](structnet__if.md) \*iface)

1126{

1127 if (iface == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4) || iface->[if\_dev](structnet__if.md#a0982ba2019cdaa7701162e60fdb2171e) == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

1128 return [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4);

1129 }

1130

1131 return &iface->[if\_dev](structnet__if.md#a0982ba2019cdaa7701162e60fdb2171e)->[link\_addr](structnet__if__dev.md#aac6d5d341ab520e6aac7f7b03737c197);

1132}

1133

[ 1141](group__net__if.md#gae271e0e4dcb031a83d9908e597a45048)static inline struct [net\_if\_config](structnet__if__config.md) \*[net\_if\_get\_config](group__net__if.md#gae271e0e4dcb031a83d9908e597a45048)(struct [net\_if](structnet__if.md) \*iface)

1142{

1143 if (iface == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

1144 return [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4);

1145 }

1146

1147 return &iface->[config](structnet__if.md#a5e71962f55bdead7bfbbb96518c6c404);

1148}

1149

1155#if defined(CONFIG\_NET\_IPV6\_DAD) && defined(CONFIG\_NET\_NATIVE\_IPV6)

1156void [net\_if\_start\_dad](group__net__if.md#ga9655c010ccbf989e9328271f5dbcc685)(struct [net\_if](structnet__if.md) \*iface);

1157#else

[ 1158](group__net__if.md#ga9655c010ccbf989e9328271f5dbcc685)static inline void [net\_if\_start\_dad](group__net__if.md#ga9655c010ccbf989e9328271f5dbcc685)(struct [net\_if](structnet__if.md) \*iface)

1159{

1160 ARG\_UNUSED(iface);

1161}

1162#endif

1163

[ 1169](group__net__if.md#gab9bdb7f8a9eeed4d9b70965b8af82cb7)void [net\_if\_start\_rs](group__net__if.md#gab9bdb7f8a9eeed4d9b70965b8af82cb7)(struct [net\_if](structnet__if.md) \*iface);

1170

1171

1177#if defined(CONFIG\_NET\_IPV6\_ND) && defined(CONFIG\_NET\_NATIVE\_IPV6)

1178void [net\_if\_stop\_rs](group__net__if.md#gab0195bb2151a1ba722a0b11d81066988)(struct [net\_if](structnet__if.md) \*iface);

1179#else

[ 1180](group__net__if.md#gab0195bb2151a1ba722a0b11d81066988)static inline void [net\_if\_stop\_rs](group__net__if.md#gab0195bb2151a1ba722a0b11d81066988)(struct [net\_if](structnet__if.md) \*iface)

1181{

1182 ARG\_UNUSED(iface);

1183}

1184#endif /\* CONFIG\_NET\_IPV6\_ND \*/

1185

1198#if defined(CONFIG\_NET\_IPV6\_ND) && defined(CONFIG\_NET\_NATIVE\_IPV6)

1199void [net\_if\_nbr\_reachability\_hint](group__net__if.md#ga51af469ff3d7d9f760d63a8a9c7be8b5)(struct [net\_if](structnet__if.md) \*iface, const struct [in6\_addr](structin6__addr.md) \*ipv6\_addr);

1200#else

[ 1201](group__net__if.md#ga51af469ff3d7d9f760d63a8a9c7be8b5)static inline void [net\_if\_nbr\_reachability\_hint](group__net__if.md#ga51af469ff3d7d9f760d63a8a9c7be8b5)(struct [net\_if](structnet__if.md) \*iface,

1202 const struct [in6\_addr](structin6__addr.md) \*ipv6\_addr)

1203{

1204 ARG\_UNUSED(iface);

1205 ARG\_UNUSED(ipv6\_addr);

1206}

1207#endif

1208

1210

1211static inline int net\_if\_set\_link\_addr\_unlocked(struct [net\_if](structnet__if.md) \*iface,

1212 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) len,

1213 enum [net\_link\_type](group__net__linkaddr.md#ga1312c2322bc4a4f1c3b76d6466806b24) type)

1214{

1215 if ([net\_if\_flag\_is\_set](group__net__if.md#gae1f373ddd61c18a81481d8ddcfb12543)(iface, [NET\_IF\_RUNNING](group__net__if.md#ggae691e5537917ffce27ad0db82c730371add3e2ecdcd5de3154f9bd2836428a25a))) {

1216 return -[EPERM](group__system__errno.md#gadd669d31505a077f769cff8e66c780b3);

1217 }

1218

1219 [net\_if\_get\_link\_addr](group__net__if.md#ga467186e964bf721e14fed38392f21872)(iface)->[addr](structnet__linkaddr.md#a2176a9f7a444ac3b0108102d8cf852f0) = addr;

1220 [net\_if\_get\_link\_addr](group__net__if.md#ga467186e964bf721e14fed38392f21872)(iface)->[len](structnet__linkaddr.md#a7b2f8ebe68b557eb9cbb4c2f2ecd70e0) = len;

1221 [net\_if\_get\_link\_addr](group__net__if.md#ga467186e964bf721e14fed38392f21872)(iface)->[type](structnet__linkaddr.md#a5f5b4c3d353261d0fab8011aa09f00d7) = type;

1222

1223 [net\_hostname\_set\_postfix](group__net__hostname.md#ga6aa3799b3b0d7eec7fb8b276485ae2c5)(addr, len);

1224

1225 return 0;

1226}

1227

1228int net\_if\_set\_link\_addr\_locked(struct [net\_if](structnet__if.md) \*iface,

1229 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) len,

1230 enum [net\_link\_type](group__net__linkaddr.md#ga1312c2322bc4a4f1c3b76d6466806b24) type);

1231

1232#if CONFIG\_NET\_IF\_LOG\_LEVEL >= LOG\_LEVEL\_DBG

1233extern int net\_if\_addr\_unref\_debug(struct [net\_if](structnet__if.md) \*iface,

1234 [sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda) family,

1235 const void \*addr,

1236 struct [net\_if\_addr](structnet__if__addr.md) \*\*ifaddr,

1237 const char \*caller, int line);

1238#define net\_if\_addr\_unref(iface, family, addr, ifaddr) \

1239 net\_if\_addr\_unref\_debug(iface, family, addr, ifaddr, \_\_func\_\_, \_\_LINE\_\_)

1240

1241extern struct [net\_if\_addr](structnet__if__addr.md) \*net\_if\_addr\_ref\_debug(struct [net\_if](structnet__if.md) \*iface,

1242 [sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda) family,

1243 const void \*addr,

1244 const char \*caller,

1245 int line);

1246#define net\_if\_addr\_ref(iface, family, addr) \

1247 net\_if\_addr\_ref\_debug(iface, family, addr, \_\_func\_\_, \_\_LINE\_\_)

1248#else

1249extern int net\_if\_addr\_unref(struct [net\_if](structnet__if.md) \*iface,

1250 [sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda) family,

1251 const void \*addr,

1252 struct [net\_if\_addr](structnet__if__addr.md) \*\*ifaddr);

1253extern struct [net\_if\_addr](structnet__if__addr.md) \*net\_if\_addr\_ref(struct [net\_if](structnet__if.md) \*iface,

1254 [sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda) family,

1255 const void \*addr);

1256#endif /\* CONFIG\_NET\_IF\_LOG\_LEVEL \*/

1257

1259

[ 1271](group__net__if.md#ga52b41b2f8b7d3405338a0539542677a0)static inline int [net\_if\_set\_link\_addr](group__net__if.md#ga52b41b2f8b7d3405338a0539542677a0)(struct [net\_if](structnet__if.md) \*iface,

1272 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) len,

1273 enum [net\_link\_type](group__net__linkaddr.md#ga1312c2322bc4a4f1c3b76d6466806b24) type)

1274{

1275#if defined(CONFIG\_NET\_RAW\_MODE)

1276 return net\_if\_set\_link\_addr\_unlocked(iface, addr, len, type);

1277#else

1278 return net\_if\_set\_link\_addr\_locked(iface, addr, len, type);

1279#endif

1280}

1281

[ 1289](group__net__if.md#gacddc98531c5748db5a34f5c3a3e96e86)static inline [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [net\_if\_get\_mtu](group__net__if.md#gacddc98531c5748db5a34f5c3a3e96e86)(struct [net\_if](structnet__if.md) \*iface)

1290{

1291 if (iface == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4) || iface->[if\_dev](structnet__if.md#a0982ba2019cdaa7701162e60fdb2171e) == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

1292 return 0U;

1293 }

1294

1295 return iface->[if\_dev](structnet__if.md#a0982ba2019cdaa7701162e60fdb2171e)->[mtu](structnet__if__dev.md#aa15ccca2eb67b8d2afca153ccacb3742);

1296}

1297

[ 1304](group__net__if.md#ga76b140c6fc39b94ff4102e08e3a58e81)static inline void [net\_if\_set\_mtu](group__net__if.md#ga76b140c6fc39b94ff4102e08e3a58e81)(struct [net\_if](structnet__if.md) \*iface,

1305 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mtu)

1306{

1307 if (iface == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4) || iface->[if\_dev](structnet__if.md#a0982ba2019cdaa7701162e60fdb2171e) == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

1308 return;

1309 }

1310

1311 iface->[if\_dev](structnet__if.md#a0982ba2019cdaa7701162e60fdb2171e)->[mtu](structnet__if__dev.md#aa15ccca2eb67b8d2afca153ccacb3742) = mtu;

1312}

1313

[ 1320](group__net__if.md#gae66f6e7bd31545e6161fcd4600fe5842)static inline void [net\_if\_addr\_set\_lf](group__net__if.md#gae66f6e7bd31545e6161fcd4600fe5842)(struct [net\_if\_addr](structnet__if__addr.md) \*ifaddr,

1321 bool [is\_infinite](structnet__if__addr.md#a6e799428eb0633a25e4dc3c55e3a3b8c))

1322{

1323 if (ifaddr == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

1324 return;

1325 }

1326

1327 ifaddr->[is\_infinite](structnet__if__addr.md#a6e799428eb0633a25e4dc3c55e3a3b8c) = [is\_infinite](structnet__if__addr.md#a6e799428eb0633a25e4dc3c55e3a3b8c);

1328}

1329

[ 1337](group__net__if.md#ga1b058361dc9bcac7d842bb49846a0c79)struct [net\_if](structnet__if.md) \*[net\_if\_get\_by\_link\_addr](group__net__if.md#ga1b058361dc9bcac7d842bb49846a0c79)(struct [net\_linkaddr](structnet__linkaddr.md) \*ll\_addr);

1338

[ 1346](group__net__if.md#gadbb8be32caa896bdcdeee19425134827)struct [net\_if](structnet__if.md) \*[net\_if\_lookup\_by\_dev](group__net__if.md#gadbb8be32caa896bdcdeee19425134827)(const struct [device](structdevice.md) \*dev);

1347

[ 1355](group__net__if.md#gae2323a72714e29836d8296dfc330f7fd)static inline struct [net\_if\_config](structnet__if__config.md) \*[net\_if\_config\_get](group__net__if.md#gae2323a72714e29836d8296dfc330f7fd)(struct [net\_if](structnet__if.md) \*iface)

1356{

1357 if (iface == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

1358 return [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4);

1359 }

1360

1361 return &iface->[config](structnet__if.md#a5e71962f55bdead7bfbbb96518c6c404);

1362}

1363

[ 1369](group__net__if.md#gadc87242eb7205362a308b3c4437bf76d)void [net\_if\_router\_rm](group__net__if.md#gadc87242eb7205362a308b3c4437bf76d)(struct [net\_if\_router](structnet__if__router.md) \*router);

1370

[ 1376](group__net__if.md#ga0a1f27ec893e1af3c97f130be4616589)void [net\_if\_set\_default](group__net__if.md#ga0a1f27ec893e1af3c97f130be4616589)(struct [net\_if](structnet__if.md) \*iface);

1377

[ 1383](group__net__if.md#ga55214771e462cbd4930ffa738813cb87)struct [net\_if](structnet__if.md) \*[net\_if\_get\_default](group__net__if.md#ga55214771e462cbd4930ffa738813cb87)(void);

1384

[ 1393](group__net__if.md#ga762337e8b66874a0fbf59bdbeba173f5)struct [net\_if](structnet__if.md) \*[net\_if\_get\_first\_by\_type](group__net__if.md#ga762337e8b66874a0fbf59bdbeba173f5)(const struct [net\_l2](structnet__l2.md) \*l2);

1394

[ 1401](group__net__if.md#ga03d8c6aebb1412382a9eec636c227238)struct [net\_if](structnet__if.md) \*[net\_if\_get\_first\_up](group__net__if.md#ga03d8c6aebb1412382a9eec636c227238)(void);

1402

1403#if defined(CONFIG\_NET\_L2\_IEEE802154)

1410static inline struct [net\_if](structnet__if.md) \*net\_if\_get\_ieee802154(void)

1411{

1412 return [net\_if\_get\_first\_by\_type](group__net__if.md#ga762337e8b66874a0fbf59bdbeba173f5)(&NET\_L2\_GET\_NAME(IEEE802154));

1413}

1414#endif /\* CONFIG\_NET\_L2\_IEEE802154 \*/

1415

[ 1426](group__net__if.md#ga56c9aef19bc9827d9ec96c00e10840fa)int [net\_if\_config\_ipv6\_get](group__net__if.md#ga56c9aef19bc9827d9ec96c00e10840fa)(struct [net\_if](structnet__if.md) \*iface,

1427 struct [net\_if\_ipv6](structnet__if__ipv6.md) \*\*ipv6);

1428

[ 1436](group__net__if.md#ga8af1400b354c42a64795cdb1a600ddd6)int [net\_if\_config\_ipv6\_put](group__net__if.md#ga8af1400b354c42a64795cdb1a600ddd6)(struct [net\_if](structnet__if.md) \*iface);

1437

[ 1446](group__net__if.md#ga13b5a26fc672d15697f99e85543184bb)struct [net\_if\_addr](structnet__if__addr.md) \*[net\_if\_ipv6\_addr\_lookup](group__net__if.md#ga13b5a26fc672d15697f99e85543184bb)(const struct [in6\_addr](structin6__addr.md) \*addr,

1447 struct [net\_if](structnet__if.md) \*\*iface);

1448

[ 1457](group__net__if.md#gab53eabb540a4487d83f27c8e319c736a)struct [net\_if\_addr](structnet__if__addr.md) \*[net\_if\_ipv6\_addr\_lookup\_by\_iface](group__net__if.md#gab53eabb540a4487d83f27c8e319c736a)(struct [net\_if](structnet__if.md) \*iface,

1458 struct [in6\_addr](structin6__addr.md) \*addr);

1459

[ 1468](group__net__if.md#ga1527872e5285790d50028a183608ac02)\_\_syscall int [net\_if\_ipv6\_addr\_lookup\_by\_index](group__net__if.md#ga1527872e5285790d50028a183608ac02)(const struct [in6\_addr](structin6__addr.md) \*addr);

1469

[ 1480](group__net__if.md#gae00484a7fe32671a4ca04ff525e640c6)struct [net\_if\_addr](structnet__if__addr.md) \*[net\_if\_ipv6\_addr\_add](group__net__if.md#gae00484a7fe32671a4ca04ff525e640c6)(struct [net\_if](structnet__if.md) \*iface,

1481 struct [in6\_addr](structin6__addr.md) \*addr,

1482 enum [net\_addr\_type](group__ip__4__6.md#gafecee2d4a331dc85ad962b81a6303e41) [addr\_type](structnet__if__addr.md#ab4fd41001cc24615803bfabb9d48e7eb),

1483 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) vlifetime);

1484

[ 1495](group__net__if.md#ga980bffb649ed48775bdc6cb2a0caef15)\_\_syscall bool [net\_if\_ipv6\_addr\_add\_by\_index](group__net__if.md#ga980bffb649ed48775bdc6cb2a0caef15)(int index,

1496 struct [in6\_addr](structin6__addr.md) \*addr,

1497 enum [net\_addr\_type](group__ip__4__6.md#gafecee2d4a331dc85ad962b81a6303e41) [addr\_type](structnet__if__addr.md#ab4fd41001cc24615803bfabb9d48e7eb),

1498 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) vlifetime);

1499

[ 1506](group__net__if.md#gaef8a6752a201f81636c4ffc1ebba4a25)void [net\_if\_ipv6\_addr\_update\_lifetime](group__net__if.md#gaef8a6752a201f81636c4ffc1ebba4a25)(struct [net\_if\_addr](structnet__if__addr.md) \*ifaddr,

1507 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) vlifetime);

1508

[ 1517](group__net__if.md#ga614e1458fa28d26c26f447e9fbcc2cb7)bool [net\_if\_ipv6\_addr\_rm](group__net__if.md#ga614e1458fa28d26c26f447e9fbcc2cb7)(struct [net\_if](structnet__if.md) \*iface, const struct [in6\_addr](structin6__addr.md) \*addr);

1518

[ 1527](group__net__if.md#gac159e3b0fbf558d5fb09774141da7d6d)\_\_syscall bool [net\_if\_ipv6\_addr\_rm\_by\_index](group__net__if.md#gac159e3b0fbf558d5fb09774141da7d6d)(int index,

1528 const struct [in6\_addr](structin6__addr.md) \*addr);

1529

[ 1538](group__net__if.md#gab58d8561a4f21899e2db34043d346516)typedef void (\*[net\_if\_ip\_addr\_cb\_t](group__net__if.md#gab58d8561a4f21899e2db34043d346516))(struct [net\_if](structnet__if.md) \*iface,

1539 struct [net\_if\_addr](structnet__if__addr.md) \*addr,

1540 void \*user\_data);

1541

[ 1550](group__net__if.md#ga5ac646ad7fda0fa48e78c15b4ca52d50)void [net\_if\_ipv6\_addr\_foreach](group__net__if.md#ga5ac646ad7fda0fa48e78c15b4ca52d50)(struct [net\_if](structnet__if.md) \*iface, [net\_if\_ip\_addr\_cb\_t](group__net__if.md#gab58d8561a4f21899e2db34043d346516) cb,

1551 void \*user\_data);

1552

[ 1561](group__net__if.md#ga7ae82a491193dfea9b92cb9cbaf26f98)struct [net\_if\_mcast\_addr](structnet__if__mcast__addr.md) \*[net\_if\_ipv6\_maddr\_add](group__net__if.md#ga7ae82a491193dfea9b92cb9cbaf26f98)(struct [net\_if](structnet__if.md) \*iface,

1562 const struct [in6\_addr](structin6__addr.md) \*addr);

1563

[ 1572](group__net__if.md#gaf0ce126bb5019ff5f5ff0876b9712ad9)bool [net\_if\_ipv6\_maddr\_rm](group__net__if.md#gaf0ce126bb5019ff5f5ff0876b9712ad9)(struct [net\_if](structnet__if.md) \*iface, const struct [in6\_addr](structin6__addr.md) \*addr);

1573

[ 1582](group__net__if.md#ga726eed76563c223de8f611e2544febe9)typedef void (\*[net\_if\_ip\_maddr\_cb\_t](group__net__if.md#ga726eed76563c223de8f611e2544febe9))(struct [net\_if](structnet__if.md) \*iface,

1583 struct [net\_if\_mcast\_addr](structnet__if__mcast__addr.md) \*maddr,

1584 void \*user\_data);

1585

[ 1594](group__net__if.md#gab677496fb2e27be2df299a346e9c7132)void [net\_if\_ipv6\_maddr\_foreach](group__net__if.md#gab677496fb2e27be2df299a346e9c7132)(struct [net\_if](structnet__if.md) \*iface, [net\_if\_ip\_maddr\_cb\_t](group__net__if.md#ga726eed76563c223de8f611e2544febe9) cb,

1595 void \*user\_data);

1596

[ 1607](group__net__if.md#gadb4031153c4fef86110879befa6b9975)struct [net\_if\_mcast\_addr](structnet__if__mcast__addr.md) \*[net\_if\_ipv6\_maddr\_lookup](group__net__if.md#gadb4031153c4fef86110879befa6b9975)(const struct [in6\_addr](structin6__addr.md) \*addr,

1608 struct [net\_if](structnet__if.md) \*\*iface);

1609

[ 1620](group__net__if.md#ga0d64291573740a67eae7ff3fcc0910c5)typedef void (\*[net\_if\_mcast\_callback\_t](group__net__if.md#ga0d64291573740a67eae7ff3fcc0910c5))(struct [net\_if](structnet__if.md) \*iface,

1621 const struct net\_addr \*addr,

1622 bool is\_joined);

1623

[ 1632](structnet__if__mcast__monitor.md)struct [net\_if\_mcast\_monitor](structnet__if__mcast__monitor.md) {

[ 1634](structnet__if__mcast__monitor.md#a570b7d8a8a5fabca83982a5f7d1d896a) [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) [node](structnet__if__mcast__monitor.md#a570b7d8a8a5fabca83982a5f7d1d896a);

1635

[ 1637](structnet__if__mcast__monitor.md#af4d0e937b2b9161918a13a0d6723c60a) struct [net\_if](structnet__if.md) \*[iface](structnet__if__mcast__monitor.md#af4d0e937b2b9161918a13a0d6723c60a);

1638

[ 1640](structnet__if__mcast__monitor.md#aec441b858a5f6792ac9cdbc625f6babe) [net\_if\_mcast\_callback\_t](group__net__if.md#ga0d64291573740a67eae7ff3fcc0910c5) [cb](structnet__if__mcast__monitor.md#aec441b858a5f6792ac9cdbc625f6babe);

1641};

1642

[ 1651](group__net__if.md#ga8fdd0665ed76db6055777e395ca60255)void [net\_if\_mcast\_mon\_register](group__net__if.md#ga8fdd0665ed76db6055777e395ca60255)(struct [net\_if\_mcast\_monitor](structnet__if__mcast__monitor.md) \*mon,

1652 struct [net\_if](structnet__if.md) \*iface,

1653 [net\_if\_mcast\_callback\_t](group__net__if.md#ga0d64291573740a67eae7ff3fcc0910c5) cb);

1654

[ 1660](group__net__if.md#gad323732fe3d178a5dfdf0900e5cb5683)void [net\_if\_mcast\_mon\_unregister](group__net__if.md#gad323732fe3d178a5dfdf0900e5cb5683)(struct [net\_if\_mcast\_monitor](structnet__if__mcast__monitor.md) \*mon);

1661

[ 1669](group__net__if.md#ga372ef131263269cd65586d87997df745)void [net\_if\_mcast\_monitor](group__net__if.md#ga372ef131263269cd65586d87997df745)(struct [net\_if](structnet__if.md) \*iface, const struct net\_addr \*addr,

1670 bool is\_joined);

1671

[ 1678](group__net__if.md#ga49dbc954015307222f176f4149829b76)void [net\_if\_ipv6\_maddr\_join](group__net__if.md#ga49dbc954015307222f176f4149829b76)(struct [net\_if](structnet__if.md) \*iface,

1679 struct [net\_if\_mcast\_addr](structnet__if__mcast__addr.md) \*addr);

1680

[ 1688](group__net__if.md#gabe2c16a378a35a22d008bff9142e5449)static inline bool [net\_if\_ipv6\_maddr\_is\_joined](group__net__if.md#gabe2c16a378a35a22d008bff9142e5449)(struct [net\_if\_mcast\_addr](structnet__if__mcast__addr.md) \*addr)

1689{

1690 if (addr == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

1691 return false;

1692 }

1693

1694 return addr->[is\_joined](structnet__if__mcast__addr.md#a4af9009b2f9ccc0589a9ba6dac10927b);

1695}

1696

[ 1703](group__net__if.md#gad24d5537d52de9781a7a6a55ceedd92b)void [net\_if\_ipv6\_maddr\_leave](group__net__if.md#gad24d5537d52de9781a7a6a55ceedd92b)(struct [net\_if](structnet__if.md) \*iface,

1704 struct [net\_if\_mcast\_addr](structnet__if__mcast__addr.md) \*addr);

1705

[ 1714](group__net__if.md#gae9f98dff661d52c5e3e5e185f0ed9cc0)struct [net\_if\_ipv6\_prefix](structnet__if__ipv6__prefix.md) \*[net\_if\_ipv6\_prefix\_get](group__net__if.md#gae9f98dff661d52c5e3e5e185f0ed9cc0)(struct [net\_if](structnet__if.md) \*[iface](structnet__if__ipv6__prefix.md#a0e2d1997e2ccfe1e1af5f16e0c74ed92),

1715 const struct [in6\_addr](structin6__addr.md) \*addr);

1716

[ 1726](group__net__if.md#gaaf9af457b97c0d432b6f9f9fdd184834)struct [net\_if\_ipv6\_prefix](structnet__if__ipv6__prefix.md) \*[net\_if\_ipv6\_prefix\_lookup](group__net__if.md#gaaf9af457b97c0d432b6f9f9fdd184834)(struct [net\_if](structnet__if.md) \*[iface](structnet__if__ipv6__prefix.md#a0e2d1997e2ccfe1e1af5f16e0c74ed92),

1727 struct [in6\_addr](structin6__addr.md) \*addr,

1728 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [len](structnet__if__ipv6__prefix.md#a4d2bc2acbe51256b76cf4d3ced3aac39));

1729

[ 1740](group__net__if.md#ga2f0c98b16b090d9aea07941c64cbe035)struct [net\_if\_ipv6\_prefix](structnet__if__ipv6__prefix.md) \*[net\_if\_ipv6\_prefix\_add](group__net__if.md#ga2f0c98b16b090d9aea07941c64cbe035)(struct [net\_if](structnet__if.md) \*[iface](structnet__if__ipv6__prefix.md#a0e2d1997e2ccfe1e1af5f16e0c74ed92),

1741 struct [in6\_addr](structin6__addr.md) \*[prefix](structnet__if__ipv6__prefix.md#a65b450d0942b3c96cfc575b462d82028),

1742 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [len](structnet__if__ipv6__prefix.md#a4d2bc2acbe51256b76cf4d3ced3aac39),

1743 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [lifetime](structnet__if__ipv6__prefix.md#a925a97a49d383bd4ce475f5d09fcb7e3));

1744

[ 1754](group__net__if.md#ga36f18c7a3ff1777006290170b726deed)bool [net\_if\_ipv6\_prefix\_rm](group__net__if.md#ga36f18c7a3ff1777006290170b726deed)(struct [net\_if](structnet__if.md) \*[iface](structnet__if__ipv6__prefix.md#a0e2d1997e2ccfe1e1af5f16e0c74ed92), struct [in6\_addr](structin6__addr.md) \*addr,

1755 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [len](structnet__if__ipv6__prefix.md#a4d2bc2acbe51256b76cf4d3ced3aac39));

1756

[ 1763](group__net__if.md#gaa3c711e814fb6a4e552b4ef723d0baa0)static inline void [net\_if\_ipv6\_prefix\_set\_lf](group__net__if.md#gaa3c711e814fb6a4e552b4ef723d0baa0)(struct [net\_if\_ipv6\_prefix](structnet__if__ipv6__prefix.md) \*[prefix](structnet__if__ipv6__prefix.md#a65b450d0942b3c96cfc575b462d82028),

1764 bool [is\_infinite](structnet__if__ipv6__prefix.md#a22090441b27bed06098679bf23b4e1e9))

1765{

1766 [prefix](structnet__if__ipv6__prefix.md#a65b450d0942b3c96cfc575b462d82028)->is\_infinite = [is\_infinite](structnet__if__ipv6__prefix.md#a22090441b27bed06098679bf23b4e1e9);

1767}

1768

[ 1775](group__net__if.md#ga68cffe343c518bad7f7f152e30f7f9ee)void [net\_if\_ipv6\_prefix\_set\_timer](group__net__if.md#ga68cffe343c518bad7f7f152e30f7f9ee)(struct [net\_if\_ipv6\_prefix](structnet__if__ipv6__prefix.md) \*[prefix](structnet__if__ipv6__prefix.md#a65b450d0942b3c96cfc575b462d82028),

1776 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [lifetime](structnet__if__ipv6__prefix.md#a925a97a49d383bd4ce475f5d09fcb7e3));

1777

[ 1783](group__net__if.md#ga2d68cb6dcfcffd3f87bbfb3dfce791ff)void [net\_if\_ipv6\_prefix\_unset\_timer](group__net__if.md#ga2d68cb6dcfcffd3f87bbfb3dfce791ff)(struct [net\_if\_ipv6\_prefix](structnet__if__ipv6__prefix.md) \*[prefix](structnet__if__ipv6__prefix.md#a65b450d0942b3c96cfc575b462d82028));

1784

[ 1795](group__net__if.md#ga25d6e2253c1d361553d478f7c948a28a)bool [net\_if\_ipv6\_addr\_onlink](group__net__if.md#ga25d6e2253c1d361553d478f7c948a28a)(struct [net\_if](structnet__if.md) \*\*[iface](structnet__if__ipv6__prefix.md#a0e2d1997e2ccfe1e1af5f16e0c74ed92), struct [in6\_addr](structin6__addr.md) \*addr);

1796

1803#if defined(CONFIG\_NET\_NATIVE\_IPV6)

1804static inline struct [in6\_addr](structin6__addr.md) \*[net\_if\_router\_ipv6](group__net__if.md#gadbf1538003473d448ff0808896b732a5)(struct [net\_if\_router](structnet__if__router.md) \*router)

1805{

1806 if (router == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

1807 return [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4);

1808 }

1809

1810 return &router->[address](structnet__if__router.md#a86a2ca1b95e348acbde8ce90986b83db).in6\_addr;

1811}

1812#else

[ 1813](group__net__if.md#gadbf1538003473d448ff0808896b732a5)static inline struct [in6\_addr](structin6__addr.md) \*[net\_if\_router\_ipv6](group__net__if.md#gadbf1538003473d448ff0808896b732a5)(struct [net\_if\_router](structnet__if__router.md) \*router)

1814{

1815 static struct [in6\_addr](structin6__addr.md) addr;

1816

1817 ARG\_UNUSED(router);

1818

1819 return &addr;

1820}

1821#endif

1822

[ 1832](group__net__if.md#gacece4ee588082259b3b5cfcd5ac1d552)struct [net\_if\_router](structnet__if__router.md) \*[net\_if\_ipv6\_router\_lookup](group__net__if.md#gacece4ee588082259b3b5cfcd5ac1d552)(struct [net\_if](structnet__if.md) \*[iface](structnet__if__router.md#a03789aa0a40f7686b76616de0ca0401a),

1833 struct [in6\_addr](structin6__addr.md) \*addr);

1834

[ 1844](group__net__if.md#ga36dab2a8fd9120ebc9c8b18f1875ccfd)struct [net\_if\_router](structnet__if__router.md) \*[net\_if\_ipv6\_router\_find\_default](group__net__if.md#ga36dab2a8fd9120ebc9c8b18f1875ccfd)(struct [net\_if](structnet__if.md) \*[iface](structnet__if__router.md#a03789aa0a40f7686b76616de0ca0401a),

1845 struct [in6\_addr](structin6__addr.md) \*addr);

1846

[ 1853](group__net__if.md#gaadba4957802dc376ef011590c91c6af6)void [net\_if\_ipv6\_router\_update\_lifetime](group__net__if.md#gaadba4957802dc376ef011590c91c6af6)(struct [net\_if\_router](structnet__if__router.md) \*router,

1854 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [lifetime](structnet__if__router.md#a4b0d2ad8f225ab61022c10dfce3db199));

1855

[ 1865](group__net__if.md#ga9c766ed70ada6eb551ac6542d7ac1ca3)struct [net\_if\_router](structnet__if__router.md) \*[net\_if\_ipv6\_router\_add](group__net__if.md#ga9c766ed70ada6eb551ac6542d7ac1ca3)(struct [net\_if](structnet__if.md) \*[iface](structnet__if__router.md#a03789aa0a40f7686b76616de0ca0401a),

1866 struct [in6\_addr](structin6__addr.md) \*addr,

1867 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) router\_lifetime);

1868

[ 1876](group__net__if.md#ga1d108aa0b54c072e0aa9d0c049f02807)bool [net\_if\_ipv6\_router\_rm](group__net__if.md#ga1d108aa0b54c072e0aa9d0c049f02807)(struct [net\_if\_router](structnet__if__router.md) \*router);

1877

1886#if defined(CONFIG\_NET\_NATIVE\_IPV6)

1887[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [net\_if\_ipv6\_get\_hop\_limit](group__net__if.md#ga66d0a9a8eef095f6d4d44f35dd67f2b6)(struct [net\_if](structnet__if.md) \*[iface](structnet__if__router.md#a03789aa0a40f7686b76616de0ca0401a));

1888#else

[ 1889](group__net__if.md#ga66d0a9a8eef095f6d4d44f35dd67f2b6)static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [net\_if\_ipv6\_get\_hop\_limit](group__net__if.md#ga66d0a9a8eef095f6d4d44f35dd67f2b6)(struct [net\_if](structnet__if.md) \*[iface](structnet__if__router.md#a03789aa0a40f7686b76616de0ca0401a))

1890{

1891 ARG\_UNUSED([iface](structnet__if__router.md#a03789aa0a40f7686b76616de0ca0401a));

1892

1893 return 0;

1894}

1895#endif /\* CONFIG\_NET\_NATIVE\_IPV6 \*/

1896

1903#if defined(CONFIG\_NET\_NATIVE\_IPV6)

1904void [net\_if\_ipv6\_set\_hop\_limit](group__net__if.md#ga5bf726bb5c1d232103ec6841e7d0cd8c)(struct [net\_if](structnet__if.md) \*[iface](structnet__if__router.md#a03789aa0a40f7686b76616de0ca0401a), [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) hop\_limit);

1905#else

[ 1906](group__net__if.md#ga5bf726bb5c1d232103ec6841e7d0cd8c)static inline void [net\_if\_ipv6\_set\_hop\_limit](group__net__if.md#ga5bf726bb5c1d232103ec6841e7d0cd8c)(struct [net\_if](structnet__if.md) \*[iface](structnet__if__router.md#a03789aa0a40f7686b76616de0ca0401a),

1907 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) hop\_limit)

1908{

1909 ARG\_UNUSED([iface](structnet__if__router.md#a03789aa0a40f7686b76616de0ca0401a));

1910 ARG\_UNUSED(hop\_limit);

1911}

1912#endif /\* CONFIG\_NET\_NATIVE\_IPV6 \*/

1913

1915

1916/\* The old hop limit setter function is deprecated because the naming

1917 \* of it was incorrect. The API name was missing "\_if\_" so this function

1918 \* should not be used.

1919 \*/

1920\_\_deprecated

1921static inline void net\_ipv6\_set\_hop\_limit(struct [net\_if](structnet__if.md) \*[iface](structnet__if__router.md#a03789aa0a40f7686b76616de0ca0401a),

1922 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) hop\_limit)

1923{

1924 [net\_if\_ipv6\_set\_hop\_limit](group__net__if.md#ga5bf726bb5c1d232103ec6841e7d0cd8c)([iface](structnet__if__router.md#a03789aa0a40f7686b76616de0ca0401a), hop\_limit);

1925}

1926

1928

1937#if defined(CONFIG\_NET\_NATIVE\_IPV6)

1938[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [net\_if\_ipv6\_get\_mcast\_hop\_limit](group__net__if.md#ga56e7086633bcf4537f54c7ca70e6c900)(struct [net\_if](structnet__if.md) \*[iface](structnet__if__router.md#a03789aa0a40f7686b76616de0ca0401a));

1939#else

[ 1940](group__net__if.md#ga56e7086633bcf4537f54c7ca70e6c900)static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [net\_if\_ipv6\_get\_mcast\_hop\_limit](group__net__if.md#ga56e7086633bcf4537f54c7ca70e6c900)(struct [net\_if](structnet__if.md) \*[iface](structnet__if__router.md#a03789aa0a40f7686b76616de0ca0401a))

1941{

1942 ARG\_UNUSED([iface](structnet__if__router.md#a03789aa0a40f7686b76616de0ca0401a));

1943

1944 return 0;

1945}

1946#endif /\* CONFIG\_NET\_NATIVE\_IPV6 \*/

1947

1954#if defined(CONFIG\_NET\_NATIVE\_IPV6)

1955void [net\_if\_ipv6\_set\_mcast\_hop\_limit](group__net__if.md#gaf56a433679ea9701cf8baa3208f8ccc3)(struct [net\_if](structnet__if.md) \*[iface](structnet__if__router.md#a03789aa0a40f7686b76616de0ca0401a), [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) hop\_limit);

1956#else

[ 1957](group__net__if.md#gaf56a433679ea9701cf8baa3208f8ccc3)static inline void [net\_if\_ipv6\_set\_mcast\_hop\_limit](group__net__if.md#gaf56a433679ea9701cf8baa3208f8ccc3)(struct [net\_if](structnet__if.md) \*[iface](structnet__if__router.md#a03789aa0a40f7686b76616de0ca0401a),

1958 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) hop\_limit)

1959{

1960 ARG\_UNUSED([iface](structnet__if__router.md#a03789aa0a40f7686b76616de0ca0401a));

1961 ARG\_UNUSED(hop\_limit);

1962}

1963#endif /\* CONFIG\_NET\_NATIVE\_IPV6 \*/

1964

[ 1971](group__net__if.md#gab3939d735b660f8f02124df656ceba2c)static inline void [net\_if\_ipv6\_set\_base\_reachable\_time](group__net__if.md#gab3939d735b660f8f02124df656ceba2c)(struct [net\_if](structnet__if.md) \*[iface](structnet__if__router.md#a03789aa0a40f7686b76616de0ca0401a),

1972 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) reachable\_time)

1973{

1974#if defined(CONFIG\_NET\_NATIVE\_IPV6)

1975 if ([iface](structnet__if__router.md#a03789aa0a40f7686b76616de0ca0401a) == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

1976 return;

1977 }

1978

1979 if (![iface](structnet__if__router.md#a03789aa0a40f7686b76616de0ca0401a)->[config](structnet__if.md#a5e71962f55bdead7bfbbb96518c6c404).ip.ipv6) {

1980 return;

1981 }

1982

1983 [iface](structnet__if__router.md#a03789aa0a40f7686b76616de0ca0401a)->[config](structnet__if.md#a5e71962f55bdead7bfbbb96518c6c404).ip.ipv6->base\_reachable\_time = reachable\_time;

1984#else

1985 ARG\_UNUSED([iface](structnet__if__router.md#a03789aa0a40f7686b76616de0ca0401a));

1986 ARG\_UNUSED(reachable\_time);

1987

1988#endif

1989}

1990

[ 1998](group__net__if.md#ga9dd1f91edbb519a6a079f363c33efacf)static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [net\_if\_ipv6\_get\_reachable\_time](group__net__if.md#ga9dd1f91edbb519a6a079f363c33efacf)(struct [net\_if](structnet__if.md) \*[iface](structnet__if__router.md#a03789aa0a40f7686b76616de0ca0401a))

1999{

2000#if defined(CONFIG\_NET\_NATIVE\_IPV6)

2001 if ([iface](structnet__if__router.md#a03789aa0a40f7686b76616de0ca0401a) == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

2002 return 0;

2003 }

2004

2005 if (![iface](structnet__if__router.md#a03789aa0a40f7686b76616de0ca0401a)->[config](structnet__if.md#a5e71962f55bdead7bfbbb96518c6c404).ip.ipv6) {

2006 return 0;

2007 }

2008

2009 return [iface](structnet__if__router.md#a03789aa0a40f7686b76616de0ca0401a)->[config](structnet__if.md#a5e71962f55bdead7bfbbb96518c6c404).ip.ipv6->reachable\_time;

2010#else

2011 ARG\_UNUSED([iface](structnet__if__router.md#a03789aa0a40f7686b76616de0ca0401a));

2012 return 0;

2013#endif

2014}

2015

[ 2023](group__net__if.md#gab1861b5cefa73b4eefbb447cb1438cdc)[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [net\_if\_ipv6\_calc\_reachable\_time](group__net__if.md#gab1861b5cefa73b4eefbb447cb1438cdc)(struct [net\_if\_ipv6](structnet__if__ipv6.md) \*ipv6);

2024

[ 2031](group__net__if.md#ga8328266b870fd200660cb2becaab3de4)static inline void [net\_if\_ipv6\_set\_reachable\_time](group__net__if.md#ga8328266b870fd200660cb2becaab3de4)(struct [net\_if\_ipv6](structnet__if__ipv6.md) \*ipv6)

2032{

2033#if defined(CONFIG\_NET\_NATIVE\_IPV6)

2034 if (ipv6 == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

2035 return;

2036 }

2037

2038 ipv6->[reachable\_time](structnet__if__ipv6.md#af57b7dca189167f8cc757c4ed6b08f2f) = [net\_if\_ipv6\_calc\_reachable\_time](group__net__if.md#gab1861b5cefa73b4eefbb447cb1438cdc)(ipv6);

2039#else

2040 ARG\_UNUSED(ipv6);

2041#endif

2042}

2043

[ 2050](group__net__if.md#gad74566e5a34f447d2ac63d2c0e82eeff)static inline void [net\_if\_ipv6\_set\_retrans\_timer](group__net__if.md#gad74566e5a34f447d2ac63d2c0e82eeff)(struct [net\_if](structnet__if.md) \*[iface](structnet__if__router.md#a03789aa0a40f7686b76616de0ca0401a),

2051 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) retrans\_timer)

2052{

2053#if defined(CONFIG\_NET\_NATIVE\_IPV6)

2054 if ([iface](structnet__if__router.md#a03789aa0a40f7686b76616de0ca0401a) == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

2055 return;

2056 }

2057

2058 if (![iface](structnet__if__router.md#a03789aa0a40f7686b76616de0ca0401a)->[config](structnet__if.md#a5e71962f55bdead7bfbbb96518c6c404).ip.ipv6) {

2059 return;

2060 }

2061

2062 [iface](structnet__if__router.md#a03789aa0a40f7686b76616de0ca0401a)->[config](structnet__if.md#a5e71962f55bdead7bfbbb96518c6c404).ip.ipv6->retrans\_timer = retrans\_timer;

2063#else

2064 ARG\_UNUSED([iface](structnet__if__router.md#a03789aa0a40f7686b76616de0ca0401a));

2065 ARG\_UNUSED(retrans\_timer);

2066#endif

2067}

2068

[ 2076](group__net__if.md#gaddbf5a6ba412e6bdb7e31568fe827bd0)static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [net\_if\_ipv6\_get\_retrans\_timer](group__net__if.md#gaddbf5a6ba412e6bdb7e31568fe827bd0)(struct [net\_if](structnet__if.md) \*[iface](structnet__if__router.md#a03789aa0a40f7686b76616de0ca0401a))

2077{

2078#if defined(CONFIG\_NET\_NATIVE\_IPV6)

2079 if ([iface](structnet__if__router.md#a03789aa0a40f7686b76616de0ca0401a) == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

2080 return 0;

2081 }

2082

2083 if (![iface](structnet__if__router.md#a03789aa0a40f7686b76616de0ca0401a)->[config](structnet__if.md#a5e71962f55bdead7bfbbb96518c6c404).ip.ipv6) {

2084 return 0;

2085 }

2086

2087 return [iface](structnet__if__router.md#a03789aa0a40f7686b76616de0ca0401a)->[config](structnet__if.md#a5e71962f55bdead7bfbbb96518c6c404).ip.ipv6->retrans\_timer;

2088#else

2089 ARG\_UNUSED([iface](structnet__if__router.md#a03789aa0a40f7686b76616de0ca0401a));

2090 return 0;

2091#endif

2092}

2093

2105#if defined(CONFIG\_NET\_IPV6)

2106const struct [in6\_addr](structin6__addr.md) \*[net\_if\_ipv6\_select\_src\_addr](group__net__if.md#ga50689a1afdb37a7087bf47a12cc50438)(struct [net\_if](structnet__if.md) \*iface,

2107 const struct [in6\_addr](structin6__addr.md) \*dst);

2108#else

[ 2109](group__net__if.md#ga50689a1afdb37a7087bf47a12cc50438)static inline const struct [in6\_addr](structin6__addr.md) \*[net\_if\_ipv6\_select\_src\_addr](group__net__if.md#ga50689a1afdb37a7087bf47a12cc50438)(

2110 struct [net\_if](structnet__if.md) \*iface, const struct [in6\_addr](structin6__addr.md) \*dst)

2111{

2112 ARG\_UNUSED(iface);

2113 ARG\_UNUSED(dst);

2114

2115 return [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4);

2116}

2117#endif

2118

2132#if defined(CONFIG\_NET\_IPV6)

2133const struct [in6\_addr](structin6__addr.md) \*[net\_if\_ipv6\_select\_src\_addr\_hint](group__net__if.md#ga5cf4717e632f712045dd4fe81b30245c)(struct [net\_if](structnet__if.md) \*iface,

2134 const struct [in6\_addr](structin6__addr.md) \*dst,

2135 int [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

2136#else

[ 2137](group__net__if.md#ga5cf4717e632f712045dd4fe81b30245c)static inline const struct [in6\_addr](structin6__addr.md) \*[net\_if\_ipv6\_select\_src\_addr\_hint](group__net__if.md#ga5cf4717e632f712045dd4fe81b30245c)(

2138 struct [net\_if](structnet__if.md) \*iface, const struct [in6\_addr](structin6__addr.md) \*dst, int [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9))

2139{

2140 ARG\_UNUSED(iface);

2141 ARG\_UNUSED(dst);

2142 ARG\_UNUSED([flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

2143

2144 return [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4);

2145}

2146#endif

2147

2157#if defined(CONFIG\_NET\_IPV6)

2158struct [net\_if](structnet__if.md) \*[net\_if\_ipv6\_select\_src\_iface](group__net__if.md#gae1495ac9e743be54b8d90bd4ff4700ab)(const struct [in6\_addr](structin6__addr.md) \*dst);

2159#else

[ 2160](group__net__if.md#gae1495ac9e743be54b8d90bd4ff4700ab)static inline struct [net\_if](structnet__if.md) \*[net\_if\_ipv6\_select\_src\_iface](group__net__if.md#gae1495ac9e743be54b8d90bd4ff4700ab)(

2161 const struct [in6\_addr](structin6__addr.md) \*dst)

2162{

2163 ARG\_UNUSED(dst);

2164

2165 return [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4);

2166}

2167#endif

2168

[ 2178](group__net__if.md#gad6f3e1e349e281887352652f6f32274e)struct [in6\_addr](structin6__addr.md) \*[net\_if\_ipv6\_get\_ll](group__net__if.md#gad6f3e1e349e281887352652f6f32274e)(struct [net\_if](structnet__if.md) \*iface,

2179 enum [net\_addr\_state](group__ip__4__6.md#ga32e58fc83532ef57eeb6ff952f17288d) addr\_state);

2180

[ 2190](group__net__if.md#ga85b7a923d46d36ecd63f9930bd8970c4)struct [in6\_addr](structin6__addr.md) \*[net\_if\_ipv6\_get\_ll\_addr](group__net__if.md#ga85b7a923d46d36ecd63f9930bd8970c4)(enum [net\_addr\_state](group__ip__4__6.md#ga32e58fc83532ef57eeb6ff952f17288d) [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90),

2191 struct [net\_if](structnet__if.md) \*\*iface);

2192

[ 2200](group__net__if.md#ga1dd53d92f803cff3be4826ddfb6b7211)void [net\_if\_ipv6\_dad\_failed](group__net__if.md#ga1dd53d92f803cff3be4826ddfb6b7211)(struct [net\_if](structnet__if.md) \*iface, const struct [in6\_addr](structin6__addr.md) \*addr);

2201

[ 2213](group__net__if.md#gaca7d686c772deac13a027cc046333126)struct [in6\_addr](structin6__addr.md) \*[net\_if\_ipv6\_get\_global\_addr](group__net__if.md#gaca7d686c772deac13a027cc046333126)(enum [net\_addr\_state](group__ip__4__6.md#ga32e58fc83532ef57eeb6ff952f17288d) [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90),

2214 struct [net\_if](structnet__if.md) \*\*iface);

2215

[ 2226](group__net__if.md#ga3390e248249b28f2c80e2ca0bc79d236)int [net\_if\_config\_ipv4\_get](group__net__if.md#ga3390e248249b28f2c80e2ca0bc79d236)(struct [net\_if](structnet__if.md) \*iface,

2227 struct [net\_if\_ipv4](structnet__if__ipv4.md) \*\*ipv4);

2228

[ 2236](group__net__if.md#ga88c13a45617480a665c7f9f589ec8e10)int [net\_if\_config\_ipv4\_put](group__net__if.md#ga88c13a45617480a665c7f9f589ec8e10)(struct [net\_if](structnet__if.md) \*iface);

2237

[ 2245](group__net__if.md#ga7e1fd28dbcf1164d056296b4df782e64)[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [net\_if\_ipv4\_get\_ttl](group__net__if.md#ga7e1fd28dbcf1164d056296b4df782e64)(struct [net\_if](structnet__if.md) \*iface);

2246

[ 2253](group__net__if.md#ga5544374d7ebea26a239d561083f0203d)void [net\_if\_ipv4\_set\_ttl](group__net__if.md#ga5544374d7ebea26a239d561083f0203d)(struct [net\_if](structnet__if.md) \*iface, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ttl);

2254

[ 2262](group__net__if.md#ga71acb65b1988aab8cca9c9604c86231e)[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [net\_if\_ipv4\_get\_mcast\_ttl](group__net__if.md#ga71acb65b1988aab8cca9c9604c86231e)(struct [net\_if](structnet__if.md) \*iface);

2263

[ 2270](group__net__if.md#ga9452fef4f1309fb1a53a6a8b4f222377)void [net\_if\_ipv4\_set\_mcast\_ttl](group__net__if.md#ga9452fef4f1309fb1a53a6a8b4f222377)(struct [net\_if](structnet__if.md) \*iface, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ttl);

2271

[ 2280](group__net__if.md#ga04a8f21d173d51bdcc092b92ed949e53)struct [net\_if\_addr](structnet__if__addr.md) \*[net\_if\_ipv4\_addr\_lookup](group__net__if.md#ga04a8f21d173d51bdcc092b92ed949e53)(const struct [in\_addr](structin__addr.md) \*addr,

2281 struct [net\_if](structnet__if.md) \*\*iface);

2282

[ 2293](group__net__if.md#ga7190958f740cac56de3a13fe688b3b5d)struct [net\_if\_addr](structnet__if__addr.md) \*[net\_if\_ipv4\_addr\_add](group__net__if.md#ga7190958f740cac56de3a13fe688b3b5d)(struct [net\_if](structnet__if.md) \*iface,

2294 struct [in\_addr](structin__addr.md) \*addr,

2295 enum [net\_addr\_type](group__ip__4__6.md#gafecee2d4a331dc85ad962b81a6303e41) [addr\_type](structnet__if__addr.md#ab4fd41001cc24615803bfabb9d48e7eb),

2296 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) vlifetime);

2297

[ 2306](group__net__if.md#ga4433304d46b6559604486b828e7d9dec)bool [net\_if\_ipv4\_addr\_rm](group__net__if.md#ga4433304d46b6559604486b828e7d9dec)(struct [net\_if](structnet__if.md) \*iface, const struct [in\_addr](structin__addr.md) \*addr);

2307

[ 2316](group__net__if.md#ga0a22661727316517685afcd551e7b38e)\_\_syscall int [net\_if\_ipv4\_addr\_lookup\_by\_index](group__net__if.md#ga0a22661727316517685afcd551e7b38e)(const struct [in\_addr](structin__addr.md) \*addr);

2317

[ 2328](group__net__if.md#gad140a69cf510ad99a8a8c770bab95bc9)\_\_syscall bool [net\_if\_ipv4\_addr\_add\_by\_index](group__net__if.md#gad140a69cf510ad99a8a8c770bab95bc9)(int index,

2329 struct [in\_addr](structin__addr.md) \*addr,

2330 enum [net\_addr\_type](group__ip__4__6.md#gafecee2d4a331dc85ad962b81a6303e41) [addr\_type](structnet__if__addr.md#ab4fd41001cc24615803bfabb9d48e7eb),

2331 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) vlifetime);

2332

[ 2341](group__net__if.md#gac5bf15f948ab195cecce98d1b40bda37)\_\_syscall bool [net\_if\_ipv4\_addr\_rm\_by\_index](group__net__if.md#gac5bf15f948ab195cecce98d1b40bda37)(int index,

2342 const struct [in\_addr](structin__addr.md) \*addr);

2343

[ 2352](group__net__if.md#gaae71be476e27c178ebb21b0f183c2825)void [net\_if\_ipv4\_addr\_foreach](group__net__if.md#gaae71be476e27c178ebb21b0f183c2825)(struct [net\_if](structnet__if.md) \*iface, [net\_if\_ip\_addr\_cb\_t](group__net__if.md#gab58d8561a4f21899e2db34043d346516) cb,

2353 void \*user\_data);

2354

[ 2363](group__net__if.md#gaa43fa83711703f8737e50b639e11b16c)struct [net\_if\_mcast\_addr](structnet__if__mcast__addr.md) \*[net\_if\_ipv4\_maddr\_add](group__net__if.md#gaa43fa83711703f8737e50b639e11b16c)(struct [net\_if](structnet__if.md) \*iface,

2364 const struct [in\_addr](structin__addr.md) \*addr);

2365

[ 2374](group__net__if.md#ga1d9273e10ab089d0f02b2b17d10a9e60)bool [net\_if\_ipv4\_maddr\_rm](group__net__if.md#ga1d9273e10ab089d0f02b2b17d10a9e60)(struct [net\_if](structnet__if.md) \*iface, const struct [in\_addr](structin__addr.md) \*addr);

2375

[ 2384](group__net__if.md#gae82f53c670f602e9c37b65abb6dfaec7)void [net\_if\_ipv4\_maddr\_foreach](group__net__if.md#gae82f53c670f602e9c37b65abb6dfaec7)(struct [net\_if](structnet__if.md) \*iface, [net\_if\_ip\_maddr\_cb\_t](group__net__if.md#ga726eed76563c223de8f611e2544febe9) cb,

2385 void \*user\_data);

2386

[ 2397](group__net__if.md#gadc1514a0d6852de9dbce043bc99d4eb0)struct [net\_if\_mcast\_addr](structnet__if__mcast__addr.md) \*[net\_if\_ipv4\_maddr\_lookup](group__net__if.md#gadc1514a0d6852de9dbce043bc99d4eb0)(const struct [in\_addr](structin__addr.md) \*addr,

2398 struct [net\_if](structnet__if.md) \*\*iface);

2399

[ 2406](group__net__if.md#gae275a5e75817aa178d36f422573ad76a)void [net\_if\_ipv4\_maddr\_join](group__net__if.md#gae275a5e75817aa178d36f422573ad76a)(struct [net\_if](structnet__if.md) \*iface,

2407 struct [net\_if\_mcast\_addr](structnet__if__mcast__addr.md) \*addr);

2408

[ 2416](group__net__if.md#gaa30769fc8016f1a7496b3ede277d8d8a)static inline bool [net\_if\_ipv4\_maddr\_is\_joined](group__net__if.md#gaa30769fc8016f1a7496b3ede277d8d8a)(struct [net\_if\_mcast\_addr](structnet__if__mcast__addr.md) \*addr)

2417{

2418 if (addr == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

2419 return false;

2420 }

2421

2422 return addr->[is\_joined](structnet__if__mcast__addr.md#a4af9009b2f9ccc0589a9ba6dac10927b);

2423}

2424

[ 2431](group__net__if.md#ga1408fe384736d20f36c035c10007113c)void [net\_if\_ipv4\_maddr\_leave](group__net__if.md#ga1408fe384736d20f36c035c10007113c)(struct [net\_if](structnet__if.md) \*iface,

2432 struct [net\_if\_mcast\_addr](structnet__if__mcast__addr.md) \*addr);

2433

2440#if defined(CONFIG\_NET\_NATIVE\_IPV4)

2441static inline struct [in\_addr](structin__addr.md) \*[net\_if\_router\_ipv4](group__net__if.md#ga2a48e13941c91ddb9bbc63d014729be1)(struct [net\_if\_router](structnet__if__router.md) \*router)

2442{

2443 if (router == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

2444 return [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4);

2445 }

2446

2447 return &router->[address](structnet__if__router.md#a86a2ca1b95e348acbde8ce90986b83db).in\_addr;

2448}

2449#else

[ 2450](group__net__if.md#ga2a48e13941c91ddb9bbc63d014729be1)static inline struct [in\_addr](structin__addr.md) \*[net\_if\_router\_ipv4](group__net__if.md#ga2a48e13941c91ddb9bbc63d014729be1)(struct [net\_if\_router](structnet__if__router.md) \*router)

2451{

2452 static struct [in\_addr](structin__addr.md) addr;

2453

2454 ARG\_UNUSED(router);

2455

2456 return &addr;

2457}

2458#endif

2459

[ 2469](group__net__if.md#ga01f995b00248ad5da734e4d58a4353aa)struct [net\_if\_router](structnet__if__router.md) \*[net\_if\_ipv4\_router\_lookup](group__net__if.md#ga01f995b00248ad5da734e4d58a4353aa)(struct [net\_if](structnet__if.md) \*[iface](structnet__if__router.md#a03789aa0a40f7686b76616de0ca0401a),

2470 struct [in\_addr](structin__addr.md) \*addr);

2471

[ 2481](group__net__if.md#ga25672516d7f383807e7dd9ce5f46a94f)struct [net\_if\_router](structnet__if__router.md) \*[net\_if\_ipv4\_router\_find\_default](group__net__if.md#ga25672516d7f383807e7dd9ce5f46a94f)(struct [net\_if](structnet__if.md) \*[iface](structnet__if__router.md#a03789aa0a40f7686b76616de0ca0401a),

2482 struct [in\_addr](structin__addr.md) \*addr);

[ 2493](group__net__if.md#ga44984001411077c7a2ef68afb361b40f)struct [net\_if\_router](structnet__if__router.md) \*[net\_if\_ipv4\_router\_add](group__net__if.md#ga44984001411077c7a2ef68afb361b40f)(struct [net\_if](structnet__if.md) \*[iface](structnet__if__router.md#a03789aa0a40f7686b76616de0ca0401a),

2494 struct [in\_addr](structin__addr.md) \*addr,

2495 bool [is\_default](structnet__if__router.md#a34745207edcad2745d6ce311e2bf1894),

2496 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) router\_lifetime);

2497

[ 2505](group__net__if.md#ga6be14f5307bc63ce87ff0a3fad7c7f4d)bool [net\_if\_ipv4\_router\_rm](group__net__if.md#ga6be14f5307bc63ce87ff0a3fad7c7f4d)(struct [net\_if\_router](structnet__if__router.md) \*router);

2506

[ 2515](group__net__if.md#ga558b31e556a1a4b8d1e68a78f3f755ea)bool [net\_if\_ipv4\_addr\_mask\_cmp](group__net__if.md#ga558b31e556a1a4b8d1e68a78f3f755ea)(struct [net\_if](structnet__if.md) \*[iface](structnet__if__router.md#a03789aa0a40f7686b76616de0ca0401a),

2516 const struct [in\_addr](structin__addr.md) \*addr);

2517

[ 2526](group__net__if.md#ga8f93179138c1942bc1a099102a4314cf)bool [net\_if\_ipv4\_is\_addr\_bcast](group__net__if.md#ga8f93179138c1942bc1a099102a4314cf)(struct [net\_if](structnet__if.md) \*[iface](structnet__if__router.md#a03789aa0a40f7686b76616de0ca0401a),

2527 const struct [in\_addr](structin__addr.md) \*addr);

2528

2538#if defined(CONFIG\_NET\_IPV4)

2539struct [net\_if](structnet__if.md) \*[net\_if\_ipv4\_select\_src\_iface](group__net__if.md#gafea1a35f452ad8168855852cbfdf0024)(const struct [in\_addr](structin__addr.md) \*dst);

2540#else

[ 2541](group__net__if.md#gafea1a35f452ad8168855852cbfdf0024)static inline struct [net\_if](structnet__if.md) \*[net\_if\_ipv4\_select\_src\_iface](group__net__if.md#gafea1a35f452ad8168855852cbfdf0024)(

2542 const struct [in\_addr](structin__addr.md) \*dst)

2543{

2544 ARG\_UNUSED(dst);

2545

2546 return [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4);

2547}

2548#endif

2549

2561#if defined(CONFIG\_NET\_IPV4)

2562const struct [in\_addr](structin__addr.md) \*[net\_if\_ipv4\_select\_src\_addr](group__net__if.md#gad6ec091f61ba3055be60c77ce085522f)(struct [net\_if](structnet__if.md) \*iface,

2563 const struct [in\_addr](structin__addr.md) \*dst);

2564#else

[ 2565](group__net__if.md#gad6ec091f61ba3055be60c77ce085522f)static inline const struct [in\_addr](structin__addr.md) \*[net\_if\_ipv4\_select\_src\_addr](group__net__if.md#gad6ec091f61ba3055be60c77ce085522f)(

2566 struct [net\_if](structnet__if.md) \*iface, const struct [in\_addr](structin__addr.md) \*dst)

2567{

2568 ARG\_UNUSED(iface);

2569 ARG\_UNUSED(dst);

2570

2571 return [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4);

2572}

2573#endif

2574

[ 2584](group__net__if.md#gad2ffe8df3d5ccca5094daecf3b9a8508)struct [in\_addr](structin__addr.md) \*[net\_if\_ipv4\_get\_ll](group__net__if.md#gad2ffe8df3d5ccca5094daecf3b9a8508)(struct [net\_if](structnet__if.md) \*iface,

2585 enum [net\_addr\_state](group__ip__4__6.md#ga32e58fc83532ef57eeb6ff952f17288d) addr\_state);

2586

[ 2596](group__net__if.md#gad791780f25d19acfe49d5272eae2d019)struct [in\_addr](structin__addr.md) \*[net\_if\_ipv4\_get\_global\_addr](group__net__if.md#gad791780f25d19acfe49d5272eae2d019)(struct [net\_if](structnet__if.md) \*iface,

2597 enum [net\_addr\_state](group__ip__4__6.md#ga32e58fc83532ef57eeb6ff952f17288d) addr\_state);

2598

[ 2608](group__net__if.md#gadfad7d9232bf58c5626266387a2eb761)struct [in\_addr](structin__addr.md) [net\_if\_ipv4\_get\_netmask\_by\_addr](group__net__if.md#gadfad7d9232bf58c5626266387a2eb761)(struct [net\_if](structnet__if.md) \*iface,

2609 const struct [in\_addr](structin__addr.md) \*addr);

2610

[ 2620](group__net__if.md#ga41aeb0e7c5f9bc837f7b2ec13401afd1)\_\_deprecated struct [in\_addr](structin__addr.md) [net\_if\_ipv4\_get\_netmask](group__net__if.md#ga41aeb0e7c5f9bc837f7b2ec13401afd1)(struct [net\_if](structnet__if.md) \*iface);

2621

[ 2630](group__net__if.md#gad599bd11663fefa7d785b9fc5d52caf0)\_\_deprecated void [net\_if\_ipv4\_set\_netmask](group__net__if.md#gad599bd11663fefa7d785b9fc5d52caf0)(struct [net\_if](structnet__if.md) \*iface,

2631 const struct [in\_addr](structin__addr.md) \*netmask);

2632

[ 2643](group__net__if.md#ga94f2d2e69548609dd329c7e6b21e8958)\_\_deprecated \_\_syscall bool [net\_if\_ipv4\_set\_netmask\_by\_index](group__net__if.md#ga94f2d2e69548609dd329c7e6b21e8958)(int index,

2644 const struct [in\_addr](structin__addr.md) \*netmask);

2645

[ 2655](group__net__if.md#ga895cfd55f79f7fb78a17cf0e3004fa06)\_\_syscall bool [net\_if\_ipv4\_set\_netmask\_by\_addr\_by\_index](group__net__if.md#ga895cfd55f79f7fb78a17cf0e3004fa06)(int index,

2656 const struct [in\_addr](structin__addr.md) \*addr,

2657 const struct [in\_addr](structin__addr.md) \*netmask);

2658

[ 2668](group__net__if.md#ga7beda6ccba46fce3cf2da1ce6c0725ec)bool [net\_if\_ipv4\_set\_netmask\_by\_addr](group__net__if.md#ga7beda6ccba46fce3cf2da1ce6c0725ec)(struct [net\_if](structnet__if.md) \*iface,

2669 const struct [in\_addr](structin__addr.md) \*addr,

2670 const struct [in\_addr](structin__addr.md) \*netmask);

2671

[ 2679](group__net__if.md#gae42f6f9620e40e2d2b36d30e81bb82d9)struct [in\_addr](structin__addr.md) [net\_if\_ipv4\_get\_gw](group__net__if.md#gae42f6f9620e40e2d2b36d30e81bb82d9)(struct [net\_if](structnet__if.md) \*iface);

2680

[ 2687](group__net__if.md#ga310ccbd9b37629422ca8e32836362724)void [net\_if\_ipv4\_set\_gw](group__net__if.md#ga310ccbd9b37629422ca8e32836362724)(struct [net\_if](structnet__if.md) \*iface, const struct [in\_addr](structin__addr.md) \*gw);

2688

[ 2697](group__net__if.md#gadef49124c331817165475c69fb9104e0)\_\_syscall bool [net\_if\_ipv4\_set\_gw\_by\_index](group__net__if.md#gadef49124c331817165475c69fb9104e0)(int index, const struct [in\_addr](structin__addr.md) \*gw);

2698

[ 2709](group__net__if.md#ga001b1cdde5febcf3970848c7c185c81c)struct [net\_if](structnet__if.md) \*[net\_if\_select\_src\_iface](group__net__if.md#ga001b1cdde5febcf3970848c7c185c81c)(const struct [sockaddr](structsockaddr.md) \*dst);

2710

[ 2719](group__net__if.md#ga0f87d5753fcd7cce40ecd161e6c91078)typedef void (\*[net\_if\_link\_callback\_t](group__net__if.md#ga0f87d5753fcd7cce40ecd161e6c91078))(struct [net\_if](structnet__if.md) \*iface,

2720 struct [net\_linkaddr](structnet__linkaddr.md) \*dst,

2721 int status);

2722

[ 2731](structnet__if__link__cb.md)struct [net\_if\_link\_cb](structnet__if__link__cb.md) {

[ 2733](structnet__if__link__cb.md#accae7945a802c5b7fc36948b12a365ef) [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) [node](structnet__if__link__cb.md#accae7945a802c5b7fc36948b12a365ef);

2734

[ 2736](structnet__if__link__cb.md#a66092a22cba3dd69ac1a91c3522240bb) [net\_if\_link\_callback\_t](group__net__if.md#ga0f87d5753fcd7cce40ecd161e6c91078) [cb](structnet__if__link__cb.md#a66092a22cba3dd69ac1a91c3522240bb);

2737};

2738

[ 2745](group__net__if.md#gaa81b7d9ed8dc05da3391265dbc89b665)void [net\_if\_register\_link\_cb](group__net__if.md#gaa81b7d9ed8dc05da3391265dbc89b665)(struct [net\_if\_link\_cb](structnet__if__link__cb.md) \*link,

2746 [net\_if\_link\_callback\_t](group__net__if.md#ga0f87d5753fcd7cce40ecd161e6c91078) cb);

2747

[ 2753](group__net__if.md#ga6ba64fac6e8d846ae7be5990f49a8293)void [net\_if\_unregister\_link\_cb](group__net__if.md#ga6ba64fac6e8d846ae7be5990f49a8293)(struct [net\_if\_link\_cb](structnet__if__link__cb.md) \*link);

2754

[ 2762](group__net__if.md#gaaa64aa4391a85760bb2daf600ac4d898)void [net\_if\_call\_link\_cb](group__net__if.md#gaaa64aa4391a85760bb2daf600ac4d898)(struct [net\_if](structnet__if.md) \*iface, struct [net\_linkaddr](structnet__linkaddr.md) \*lladdr,

2763 int status);

2764

2766

2767/\* used to ensure encoding of checksum support in net\_if.h and

2768 \* ethernet.h is the same

2769 \*/

2770#define NET\_IF\_CHECKSUM\_NONE\_BIT 0

2771#define NET\_IF\_CHECKSUM\_IPV4\_HEADER\_BIT BIT(0)

2772#define NET\_IF\_CHECKSUM\_IPV4\_ICMP\_BIT BIT(1)

2773/\* Space for future protocols and restrictions for IPV4 \*/

2774#define NET\_IF\_CHECKSUM\_IPV6\_HEADER\_BIT BIT(10)

2775#define NET\_IF\_CHECKSUM\_IPV6\_ICMP\_BIT BIT(11)

2776/\* Space for future protocols and restrictions for IPV6 \*/

2777#define NET\_IF\_CHECKSUM\_TCP\_BIT BIT(21)

2778#define NET\_IF\_CHECKSUM\_UDP\_BIT BIT(22)

2779

2781

[ 2785](group__net__if.md#ga8db412ae79c64cafe81a66f5acb2f8e9)enum [net\_if\_checksum\_type](group__net__if.md#ga8db412ae79c64cafe81a66f5acb2f8e9) {

[ 2787](group__net__if.md#gga8db412ae79c64cafe81a66f5acb2f8e9a75e4a0946d0e6755ebd7cc62558aee30) [NET\_IF\_CHECKSUM\_IPV4\_HEADER](group__net__if.md#gga8db412ae79c64cafe81a66f5acb2f8e9a75e4a0946d0e6755ebd7cc62558aee30) = NET\_IF\_CHECKSUM\_IPV4\_HEADER\_BIT,

[ 2789](group__net__if.md#gga8db412ae79c64cafe81a66f5acb2f8e9aaed32a3cb700eac3b67c6c7e5a0cd0ad) [NET\_IF\_CHECKSUM\_IPV4\_TCP](group__net__if.md#gga8db412ae79c64cafe81a66f5acb2f8e9aaed32a3cb700eac3b67c6c7e5a0cd0ad) = NET\_IF\_CHECKSUM\_IPV4\_HEADER\_BIT |

2790 NET\_IF\_CHECKSUM\_TCP\_BIT,

[ 2792](group__net__if.md#gga8db412ae79c64cafe81a66f5acb2f8e9afe1eaaa765c8ec3c61618e943cd3f1c3) [NET\_IF\_CHECKSUM\_IPV4\_UDP](group__net__if.md#gga8db412ae79c64cafe81a66f5acb2f8e9afe1eaaa765c8ec3c61618e943cd3f1c3) = NET\_IF\_CHECKSUM\_IPV4\_HEADER\_BIT |

2793 NET\_IF\_CHECKSUM\_UDP\_BIT,

[ 2795](group__net__if.md#gga8db412ae79c64cafe81a66f5acb2f8e9a2aef87c97f22fdccdf1925d2687436b1) [NET\_IF\_CHECKSUM\_IPV4\_ICMP](group__net__if.md#gga8db412ae79c64cafe81a66f5acb2f8e9a2aef87c97f22fdccdf1925d2687436b1) = NET\_IF\_CHECKSUM\_IPV4\_ICMP\_BIT,

[ 2797](group__net__if.md#gga8db412ae79c64cafe81a66f5acb2f8e9ab204c7d5fddbd2c11e07a8831df6c00b) [NET\_IF\_CHECKSUM\_IPV6\_HEADER](group__net__if.md#gga8db412ae79c64cafe81a66f5acb2f8e9ab204c7d5fddbd2c11e07a8831df6c00b) = NET\_IF\_CHECKSUM\_IPV6\_HEADER\_BIT,

[ 2799](group__net__if.md#gga8db412ae79c64cafe81a66f5acb2f8e9a31e33593e4e7f7f9b36e319e0991ab13) [NET\_IF\_CHECKSUM\_IPV6\_TCP](group__net__if.md#gga8db412ae79c64cafe81a66f5acb2f8e9a31e33593e4e7f7f9b36e319e0991ab13) = NET\_IF\_CHECKSUM\_IPV6\_HEADER\_BIT |

2800 NET\_IF\_CHECKSUM\_TCP\_BIT,

[ 2802](group__net__if.md#gga8db412ae79c64cafe81a66f5acb2f8e9a70b1272e2125cea9204bae144fd86660) [NET\_IF\_CHECKSUM\_IPV6\_UDP](group__net__if.md#gga8db412ae79c64cafe81a66f5acb2f8e9a70b1272e2125cea9204bae144fd86660) = NET\_IF\_CHECKSUM\_IPV6\_HEADER\_BIT |

2803 NET\_IF\_CHECKSUM\_UDP\_BIT,

[ 2805](group__net__if.md#gga8db412ae79c64cafe81a66f5acb2f8e9af5b3bc7cb5e9771cd9fd57d9fda4c3b3) [NET\_IF\_CHECKSUM\_IPV6\_ICMP](group__net__if.md#gga8db412ae79c64cafe81a66f5acb2f8e9af5b3bc7cb5e9771cd9fd57d9fda4c3b3) = NET\_IF\_CHECKSUM\_IPV6\_ICMP\_BIT

2806};

2807

[ 2818](group__net__if.md#ga8048e722f6442bcd5b6881bd71e791a5)bool [net\_if\_need\_calc\_rx\_checksum](group__net__if.md#ga8048e722f6442bcd5b6881bd71e791a5)(struct [net\_if](structnet__if.md) \*iface,

2819 enum [net\_if\_checksum\_type](group__net__if.md#ga8db412ae79c64cafe81a66f5acb2f8e9) chksum\_type);

2820

[ 2832](group__net__if.md#ga9634c3e71e934ab3a07bec989b364663)bool [net\_if\_need\_calc\_tx\_checksum](group__net__if.md#ga9634c3e71e934ab3a07bec989b364663)(struct [net\_if](structnet__if.md) \*iface,

2833 enum [net\_if\_checksum\_type](group__net__if.md#ga8db412ae79c64cafe81a66f5acb2f8e9) chksum\_type);

2834

[ 2845](group__net__if.md#ga72708cdb7f133fe5d7edf819756c3516)\_\_syscall struct [net\_if](structnet__if.md) \*[net\_if\_get\_by\_index](group__net__if.md#ga72708cdb7f133fe5d7edf819756c3516)(int index);

2846

[ 2854](group__net__if.md#ga02445f6c61f0d29f56ac0ef59e025630)int [net\_if\_get\_by\_iface](group__net__if.md#ga02445f6c61f0d29f56ac0ef59e025630)(struct [net\_if](structnet__if.md) \*iface);

2855

[ 2863](group__net__if.md#gac48ab8e6337e7cf387af9b293f254a80)typedef void (\*[net\_if\_cb\_t](group__net__if.md#gac48ab8e6337e7cf387af9b293f254a80))(struct [net\_if](structnet__if.md) \*iface, void \*user\_data);

2864

[ 2872](group__net__if.md#ga96b198fd9df4a985b0dde84dd7152815)void [net\_if\_foreach](group__net__if.md#ga96b198fd9df4a985b0dde84dd7152815)([net\_if\_cb\_t](group__net__if.md#gac48ab8e6337e7cf387af9b293f254a80) cb, void \*user\_data);

2873

[ 2881](group__net__if.md#ga02644cc623fc7a8878c17d54984e4210)int [net\_if\_up](group__net__if.md#ga02644cc623fc7a8878c17d54984e4210)(struct [net\_if](structnet__if.md) \*iface);

2882

[ 2890](group__net__if.md#ga7e9b368d4abf9da5656140df70cfa334)static inline bool [net\_if\_is\_up](group__net__if.md#ga7e9b368d4abf9da5656140df70cfa334)(struct [net\_if](structnet__if.md) \*iface)

2891{

2892 if (iface == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

2893 return false;

2894 }

2895

2896 return [net\_if\_flag\_is\_set](group__net__if.md#gae1f373ddd61c18a81481d8ddcfb12543)(iface, [NET\_IF\_UP](group__net__if.md#ggae691e5537917ffce27ad0db82c730371ab0ab7393d643354c46c3437d74c15840)) &&

2897 [net\_if\_flag\_is\_set](group__net__if.md#gae1f373ddd61c18a81481d8ddcfb12543)(iface, [NET\_IF\_RUNNING](group__net__if.md#ggae691e5537917ffce27ad0db82c730371add3e2ecdcd5de3154f9bd2836428a25a));

2898}

2899

[ 2907](group__net__if.md#ga2187650062d6139b9f4b81745a206803)int [net\_if\_down](group__net__if.md#ga2187650062d6139b9f4b81745a206803)(struct [net\_if](structnet__if.md) \*iface);

2908

[ 2916](group__net__if.md#ga099a484a654ad9af35d3212fc2c995b2)static inline bool [net\_if\_is\_admin\_up](group__net__if.md#ga099a484a654ad9af35d3212fc2c995b2)(struct [net\_if](structnet__if.md) \*iface)

2917{

2918 if (iface == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

2919 return false;

2920 }

2921

2922 return [net\_if\_flag\_is\_set](group__net__if.md#gae1f373ddd61c18a81481d8ddcfb12543)(iface, [NET\_IF\_UP](group__net__if.md#ggae691e5537917ffce27ad0db82c730371ab0ab7393d643354c46c3437d74c15840));

2923}

2924

[ 2933](group__net__if.md#ga35e5db3a631ac9039f14d86e59fc0dcc)void [net\_if\_carrier\_on](group__net__if.md#ga35e5db3a631ac9039f14d86e59fc0dcc)(struct [net\_if](structnet__if.md) \*iface);

2934

[ 2943](group__net__if.md#ga6839941422a88c1f707ab70ea34df323)void [net\_if\_carrier\_off](group__net__if.md#ga6839941422a88c1f707ab70ea34df323)(struct [net\_if](structnet__if.md) \*iface);

2944

[ 2952](group__net__if.md#ga095554237016e563d76cfd602d1dae77)static inline bool [net\_if\_is\_carrier\_ok](group__net__if.md#ga095554237016e563d76cfd602d1dae77)(struct [net\_if](structnet__if.md) \*iface)

2953{

2954 if (iface == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

2955 return false;

2956 }

2957

2958 return [net\_if\_flag\_is\_set](group__net__if.md#gae1f373ddd61c18a81481d8ddcfb12543)(iface, [NET\_IF\_LOWER\_UP](group__net__if.md#ggae691e5537917ffce27ad0db82c730371ab1a529826bad6b4bcd04185372f97d6d));

2959}

2960

[ 2971](group__net__if.md#ga89a3374d4bb116460a7b7c50a750b593)void [net\_if\_dormant\_on](group__net__if.md#ga89a3374d4bb116460a7b7c50a750b593)(struct [net\_if](structnet__if.md) \*iface);

2972

[ 2981](group__net__if.md#ga1c31fac887d944ac0a16aad70e889496)void [net\_if\_dormant\_off](group__net__if.md#ga1c31fac887d944ac0a16aad70e889496)(struct [net\_if](structnet__if.md) \*iface);

2982

[ 2990](group__net__if.md#ga6e2e6102271c37acaa59c54e2aa6b413)static inline bool [net\_if\_is\_dormant](group__net__if.md#ga6e2e6102271c37acaa59c54e2aa6b413)(struct [net\_if](structnet__if.md) \*iface)

2991{

2992 if (iface == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

2993 return false;

2994 }

2995

2996 return [net\_if\_flag\_is\_set](group__net__if.md#gae1f373ddd61c18a81481d8ddcfb12543)(iface, [NET\_IF\_DORMANT](group__net__if.md#ggae691e5537917ffce27ad0db82c730371a7dd1db72a37b1fbc4c4491ce1c75238d));

2997}

2998

2999#if defined(CONFIG\_NET\_PKT\_TIMESTAMP) && defined(CONFIG\_NET\_NATIVE)

3007typedef void (\*net\_if\_timestamp\_callback\_t)(struct [net\_pkt](structnet__pkt.md) \*pkt);

3008

3017struct net\_if\_timestamp\_cb {

3019 [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) node;

3020

3024 struct net\_pkt \*pkt;

3025

3029 struct net\_if \*iface;

3030

3032 net\_if\_timestamp\_callback\_t cb;

3033};

3034

3045void net\_if\_register\_timestamp\_cb(struct net\_if\_timestamp\_cb \*handle,

3046 struct [net\_pkt](structnet__pkt.md) \*pkt,

3047 struct [net\_if](structnet__if.md) \*iface,

3048 net\_if\_timestamp\_callback\_t cb);

3049

3055void net\_if\_unregister\_timestamp\_cb(struct net\_if\_timestamp\_cb \*handle);

3056

3062void net\_if\_call\_timestamp\_cb(struct [net\_pkt](structnet__pkt.md) \*pkt);

3063

3064/\*

3065 \* @brief Add timestamped TX buffer to be handled

3066 \*

3067 \* @param pkt Timestamped buffer

3068 \*/

3069void net\_if\_add\_tx\_timestamp(struct [net\_pkt](structnet__pkt.md) \*pkt);

3070#endif /\* CONFIG\_NET\_PKT\_TIMESTAMP \*/

3071

3081#if defined(CONFIG\_NET\_PROMISCUOUS\_MODE)

3082int [net\_if\_set\_promisc](group__net__if.md#gaf9f81f3b9697ca47f7674d85f37a8d80)(struct [net\_if](structnet__if.md) \*iface);

3083#else

[ 3084](group__net__if.md#gaf9f81f3b9697ca47f7674d85f37a8d80)static inline int [net\_if\_set\_promisc](group__net__if.md#gaf9f81f3b9697ca47f7674d85f37a8d80)(struct [net\_if](structnet__if.md) \*iface)

3085{

3086 ARG\_UNUSED(iface);

3087

3088 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

3089}

3090#endif

3091

3097#if defined(CONFIG\_NET\_PROMISCUOUS\_MODE)

3098void [net\_if\_unset\_promisc](group__net__if.md#ga9c8212c087883510050ac6a39ef0a7bf)(struct [net\_if](structnet__if.md) \*iface);

3099#else

[ 3100](group__net__if.md#ga9c8212c087883510050ac6a39ef0a7bf)static inline void [net\_if\_unset\_promisc](group__net__if.md#ga9c8212c087883510050ac6a39ef0a7bf)(struct [net\_if](structnet__if.md) \*iface)

3101{

3102 ARG\_UNUSED(iface);

3103}

3104#endif

3105

3114#if defined(CONFIG\_NET\_PROMISCUOUS\_MODE)

3115bool [net\_if\_is\_promisc](group__net__if.md#ga9f1a6eab849517734ec422deb0ba71f5)(struct [net\_if](structnet__if.md) \*iface);

3116#else

[ 3117](group__net__if.md#ga9f1a6eab849517734ec422deb0ba71f5)static inline bool [net\_if\_is\_promisc](group__net__if.md#ga9f1a6eab849517734ec422deb0ba71f5)(struct [net\_if](structnet__if.md) \*iface)

3118{

3119 ARG\_UNUSED(iface);

3120

3121 return false;

3122}

3123#endif

3124

[ 3134](group__net__if.md#ga3cddda628eca248246f9aa3b81938f95)static inline bool [net\_if\_are\_pending\_tx\_packets](group__net__if.md#ga3cddda628eca248246f9aa3b81938f95)(struct [net\_if](structnet__if.md) \*iface)

3135{

3136#if defined(CONFIG\_NET\_POWER\_MANAGEMENT)

3137 return !!iface->tx\_pending;

3138#else

3139 ARG\_UNUSED(iface);

3140

3141 return false;

3142#endif

3143}

3144

3145#ifdef CONFIG\_NET\_POWER\_MANAGEMENT

3153int net\_if\_suspend(struct [net\_if](structnet__if.md) \*iface);

3154

3162int net\_if\_resume(struct [net\_if](structnet__if.md) \*iface);

3163

3171bool net\_if\_is\_suspended(struct [net\_if](structnet__if.md) \*iface);

3172#endif /\* CONFIG\_NET\_POWER\_MANAGEMENT \*/

3173

[ 3181](group__net__if.md#gaa458b5f349c55007108b47b99f4954d5)bool [net\_if\_is\_wifi](group__net__if.md#gaa458b5f349c55007108b47b99f4954d5)(struct [net\_if](structnet__if.md) \*iface);

3182

[ 3188](group__net__if.md#ga6e89bbafb6c0acdc6bf51078e2027236)struct [net\_if](structnet__if.md) \*[net\_if\_get\_first\_wifi](group__net__if.md#ga6e89bbafb6c0acdc6bf51078e2027236)(void);

3189

[ 3195](group__net__if.md#ga0fc3ba6172956f6847027e0bd3d367de)struct [net\_if](structnet__if.md) \*[net\_if\_get\_wifi\_sta](group__net__if.md#ga0fc3ba6172956f6847027e0bd3d367de)(void);

3196

[ 3202](group__net__if.md#gaf830eab616191009d88f58b761694b49)struct [net\_if](structnet__if.md) \*[net\_if\_get\_wifi\_sap](group__net__if.md#gaf830eab616191009d88f58b761694b49)(void);

3203

[ 3218](group__net__if.md#ga5f653cd73c1ecd548a931eb7fbd170f7)int [net\_if\_get\_name](group__net__if.md#ga5f653cd73c1ecd548a931eb7fbd170f7)(struct [net\_if](structnet__if.md) \*iface, char \*buf, int len);

3219

[ 3234](group__net__if.md#ga05dec64966fc39e3deb0679b9585688b)int [net\_if\_set\_name](group__net__if.md#ga05dec64966fc39e3deb0679b9585688b)(struct [net\_if](structnet__if.md) \*iface, const char \*buf);

3235

[ 3243](group__net__if.md#ga1774ac036032bb0dc2c662f6f4f66a7f)int [net\_if\_get\_by\_name](group__net__if.md#ga1774ac036032bb0dc2c662f6f4f66a7f)(const char \*name);

3244

3246struct net\_if\_api {

3247 void (\*init)(struct [net\_if](structnet__if.md) \*iface);

3248};

3249

3250#define NET\_IF\_DHCPV4\_INIT \

3251 IF\_ENABLED(UTIL\_AND(IS\_ENABLED(CONFIG\_NET\_DHCPV4), \

3252 IS\_ENABLED(CONFIG\_NET\_NATIVE\_IPV4)), \

3253 (.dhcpv4.state = NET\_DHCPV4\_DISABLED,))

3254

3255#define NET\_IF\_DHCPV6\_INIT \

3256 IF\_ENABLED(UTIL\_AND(IS\_ENABLED(CONFIG\_NET\_DHCPV6), \

3257 IS\_ENABLED(CONFIG\_NET\_NATIVE\_IPV6)), \

3258 (.dhcpv6.state = NET\_DHCPV6\_DISABLED,))

3259

3260#define NET\_IF\_CONFIG\_INIT \

3261 .config = { \

3262 IF\_ENABLED(CONFIG\_NET\_IP, (.ip = {},)) \

3263 NET\_IF\_DHCPV4\_INIT \

3264 NET\_IF\_DHCPV6\_INIT \

3265 }

3266

3267#define NET\_PROMETHEUS\_GET\_COLLECTOR\_NAME(dev\_id, sfx) \

3268 net\_stats\_##dev\_id##\_##sfx##\_collector

3269#define NET\_PROMETHEUS\_INIT(dev\_id, sfx) \

3270 IF\_ENABLED(CONFIG\_NET\_STATISTICS\_VIA\_PROMETHEUS, \

3271 (.collector = &NET\_PROMETHEUS\_GET\_COLLECTOR\_NAME(dev\_id, sfx),))

3272

3273#define NET\_IF\_GET\_NAME(dev\_id, sfx) \_\_net\_if\_##dev\_id##\_##sfx

3274#define NET\_IF\_DEV\_GET\_NAME(dev\_id, sfx) \_\_net\_if\_dev\_##dev\_id##\_##sfx

3275

3276#define NET\_IF\_GET(dev\_id, sfx) \

3277 ((struct net\_if \*)&NET\_IF\_GET\_NAME(dev\_id, sfx))

3278

3279#if defined(CONFIG\_NET\_STATISTICS\_VIA\_PROMETHEUS)

3280extern int net\_stats\_prometheus\_scrape(struct [prometheus\_collector](structprometheus__collector.md) \*collector,

3281 struct [prometheus\_metric](structprometheus__metric.md) \*metric,

3282 void \*user\_data);

3283#endif /\* CONFIG\_NET\_STATISTICS\_VIA\_PROMETHEUS \*/

3284

3285#define NET\_IF\_INIT(dev\_id, sfx, \_l2, \_mtu, \_num\_configs) \

3286 static STRUCT\_SECTION\_ITERABLE(net\_if\_dev, \

3287 NET\_IF\_DEV\_GET\_NAME(dev\_id, sfx)) = { \

3288 .dev = &(DEVICE\_NAME\_GET(dev\_id)), \

3289 .l2 = &(NET\_L2\_GET\_NAME(\_l2)), \

3290 .l2\_data = &(NET\_L2\_GET\_DATA(dev\_id, sfx)), \

3291 .mtu = \_mtu, \

3292 .flags = {BIT(NET\_IF\_LOWER\_UP)}, \

3293 }; \

3294 static Z\_DECL\_ALIGN(struct net\_if) \

3295 NET\_IF\_GET\_NAME(dev\_id, sfx)[\_num\_configs] \

3296 \_\_used \_\_noasan \_\_in\_section(\_net\_if, static, \

3297 dev\_id) = { \

3298 [0 ... (\_num\_configs - 1)] = { \

3299 .if\_dev = &(NET\_IF\_DEV\_GET\_NAME(dev\_id, sfx)), \

3300 NET\_IF\_CONFIG\_INIT \

3301 } \

3302 }; \

3303 IF\_ENABLED(CONFIG\_NET\_STATISTICS\_VIA\_PROMETHEUS, \

3304 (static PROMETHEUS\_COLLECTOR\_DEFINE( \

3305 NET\_PROMETHEUS\_GET\_COLLECTOR\_NAME(dev\_id, \

3306 sfx), \

3307 net\_stats\_prometheus\_scrape, \

3308 NET\_IF\_GET(dev\_id, sfx)); \

3309 NET\_STATS\_PROMETHEUS(NET\_IF\_GET(dev\_id, sfx), \

3310 dev\_id, sfx);))

3311

3312#define NET\_IF\_OFFLOAD\_INIT(dev\_id, sfx, \_mtu) \

3313 static STRUCT\_SECTION\_ITERABLE(net\_if\_dev, \

3314 NET\_IF\_DEV\_GET\_NAME(dev\_id, sfx)) = { \

3315 .dev = &(DEVICE\_NAME\_GET(dev\_id)), \

3316 .mtu = \_mtu, \

3317 .l2 = &(NET\_L2\_GET\_NAME(OFFLOADED\_NETDEV)), \

3318 .flags = {BIT(NET\_IF\_LOWER\_UP)}, \

3319 }; \

3320 static Z\_DECL\_ALIGN(struct net\_if) \

3321 NET\_IF\_GET\_NAME(dev\_id, sfx)[NET\_IF\_MAX\_CONFIGS] \

3322 \_\_used \_\_in\_section(\_net\_if, static, \

3323 dev\_id) = { \

3324 [0 ... (NET\_IF\_MAX\_CONFIGS - 1)] = { \

3325 .if\_dev = &(NET\_IF\_DEV\_GET\_NAME(dev\_id, sfx)), \

3326 NET\_IF\_CONFIG\_INIT \

3327 } \

3328 }; \

3329 IF\_ENABLED(CONFIG\_NET\_STATISTICS\_VIA\_PROMETHEUS, \

3330 (static PROMETHEUS\_COLLECTOR\_DEFINE( \

3331 NET\_PROMETHEUS\_GET\_COLLECTOR\_NAME(dev\_id, \

3332 sfx), \

3333 net\_stats\_prometheus\_scrape, \

3334 NET\_IF\_GET(dev\_id, sfx)); \

3335 NET\_STATS\_PROMETHEUS(NET\_IF\_GET(dev\_id, sfx), \

3336 dev\_id, sfx);))

3337

3338

3340

3341/\* Network device initialization macros \*/

3342

3343#define Z\_NET\_DEVICE\_INIT\_INSTANCE(node\_id, dev\_id, name, instance, \

3344 init\_fn, pm, data, config, prio, \

3345 api, l2, l2\_ctx\_type, mtu) \

3346 Z\_DEVICE\_STATE\_DEFINE(dev\_id); \

3347 Z\_DEVICE\_DEFINE(node\_id, dev\_id, name, init\_fn, pm, data, \

3348 config, POST\_KERNEL, prio, api, \

3349 &Z\_DEVICE\_STATE\_NAME(dev\_id)); \

3350 NET\_L2\_DATA\_INIT(dev\_id, instance, l2\_ctx\_type); \

3351 NET\_IF\_INIT(dev\_id, instance, l2, mtu, NET\_IF\_MAX\_CONFIGS)

3352

3353#define Z\_NET\_DEVICE\_INIT(node\_id, dev\_id, name, init\_fn, pm, data, \

3354 config, prio, api, l2, l2\_ctx\_type, mtu) \

3355 Z\_NET\_DEVICE\_INIT\_INSTANCE(node\_id, dev\_id, name, 0, init\_fn, \

3356 pm, data, config, prio, api, l2, \

3357 l2\_ctx\_type, mtu)

3358

[ 3378](group__net__if.md#ga02971562c42494e2a5f71e1f8587e709)#define NET\_DEVICE\_INIT(dev\_id, name, init\_fn, pm, data, config, prio, \

3379 api, l2, l2\_ctx\_type, mtu) \

3380 Z\_NET\_DEVICE\_INIT(DT\_INVALID\_NODE, dev\_id, name, init\_fn, pm, \

3381 data, config, prio, api, l2, l2\_ctx\_type, mtu)

3382

[ 3401](group__net__if.md#gab1f762b01ae7bc37cd4a25724c123dda)#define NET\_DEVICE\_DT\_DEFINE(node\_id, init\_fn, pm, data, \

3402 config, prio, api, l2, l2\_ctx\_type, mtu) \

3403 Z\_NET\_DEVICE\_INIT(node\_id, Z\_DEVICE\_DT\_DEV\_ID(node\_id), \

3404 DEVICE\_DT\_NAME(node\_id), init\_fn, pm, data, \

3405 config, prio, api, l2, l2\_ctx\_type, mtu)

3406

[ 3415](group__net__if.md#ga7edd8bc59444d92cad0371c36f9949b7)#define NET\_DEVICE\_DT\_INST\_DEFINE(inst, ...) \

3416 NET\_DEVICE\_DT\_DEFINE(DT\_DRV\_INST(inst), \_\_VA\_ARGS\_\_)

3417

[ 3441](group__net__if.md#gacc7edecdd9de9920cc155977d8fec2a2)#define NET\_DEVICE\_INIT\_INSTANCE(dev\_id, name, instance, init\_fn, pm, \

3442 data, config, prio, api, l2, \

3443 l2\_ctx\_type, mtu) \

3444 Z\_NET\_DEVICE\_INIT\_INSTANCE(DT\_INVALID\_NODE, dev\_id, name, \

3445 instance, init\_fn, pm, data, config, \

3446 prio, api, l2, l2\_ctx\_type, mtu)

3447

[ 3470](group__net__if.md#ga50702b043a0791e59e7d5679dda1d9e8)#define NET\_DEVICE\_DT\_DEFINE\_INSTANCE(node\_id, instance, init\_fn, pm, \

3471 data, config, prio, api, l2, \

3472 l2\_ctx\_type, mtu) \

3473 Z\_NET\_DEVICE\_INIT\_INSTANCE(node\_id, \

3474 Z\_DEVICE\_DT\_DEV\_ID(node\_id), \

3475 DEVICE\_DT\_NAME(node\_id), instance, \

3476 init\_fn, pm, data, config, prio, \

3477 api, l2, l2\_ctx\_type, mtu)

3478

[ 3488](group__net__if.md#gabe4b8589996a53cbc50b76c8ea15aa0c)#define NET\_DEVICE\_DT\_INST\_DEFINE\_INSTANCE(inst, ...) \

3489 NET\_DEVICE\_DT\_DEFINE\_INSTANCE(DT\_DRV\_INST(inst), \_\_VA\_ARGS\_\_)

3490

3491#define Z\_NET\_DEVICE\_OFFLOAD\_INIT(node\_id, dev\_id, name, init\_fn, pm, \

3492 data, config, prio, api, mtu) \

3493 Z\_DEVICE\_STATE\_DEFINE(dev\_id); \

3494 Z\_DEVICE\_DEFINE(node\_id, dev\_id, name, init\_fn, pm, data, \

3495 config, POST\_KERNEL, prio, api, \

3496 &Z\_DEVICE\_STATE\_NAME(dev\_id)); \

3497 NET\_IF\_OFFLOAD\_INIT(dev\_id, 0, mtu)

3498

[ 3518](group__net__if.md#ga255672607b7958db3f464d2a57a7e635)#define NET\_DEVICE\_OFFLOAD\_INIT(dev\_id, name, init\_fn, pm, data, \

3519 config, prio, api, mtu) \

3520 Z\_NET\_DEVICE\_OFFLOAD\_INIT(DT\_INVALID\_NODE, dev\_id, name, \

3521 init\_fn, pm, data, config, prio, api, \

3522 mtu)

3523

[ 3542](group__net__if.md#gab2b287025e194dec1fab24e44d95362f)#define NET\_DEVICE\_DT\_OFFLOAD\_DEFINE(node\_id, init\_fn, pm, data, \

3543 config, prio, api, mtu) \

3544 Z\_NET\_DEVICE\_OFFLOAD\_INIT(node\_id, Z\_DEVICE\_DT\_DEV\_ID(node\_id), \

3545 DEVICE\_DT\_NAME(node\_id), init\_fn, pm, \

3546 data, config, prio, api, mtu)

3547

[ 3557](group__net__if.md#ga1cab6943a28e3d3754e36623834b93fd)#define NET\_DEVICE\_DT\_INST\_OFFLOAD\_DEFINE(inst, ...) \

3558 NET\_DEVICE\_DT\_OFFLOAD\_DEFINE(DT\_DRV\_INST(inst), \_\_VA\_ARGS\_\_)

3559

[ 3565](group__net__if.md#ga6c081875a6f5a848b3ad2fd220c63c3c)#define NET\_IFACE\_COUNT(\_dst) \

3566 do { \

3567 extern struct net\_if \_net\_if\_list\_start[]; \

3568 extern struct net\_if \_net\_if\_list\_end[]; \

3569 \*(\_dst) = ((uintptr\_t)\_net\_if\_list\_end - \

3570 (uintptr\_t)\_net\_if\_list\_start) / \

3571 sizeof(struct net\_if); \

3572 } while (0)

3573

3574#ifdef \_\_cplusplus

3575}

3576#endif

3577

3578#include <zephyr/syscalls/net\_if.h>

3579

3583

3584#endif /\* ZEPHYR\_INCLUDE\_NET\_NET\_IF\_H\_ \*/

[k\_thread\_stack\_t](arch__interface_8h.md#a9fc2dce533bd7b8cb1fdd4bdbb2b62b1)

struct z\_thread\_stack\_element k\_thread\_stack\_t

Typedef of struct z\_thread\_stack\_element.

**Definition** arch\_interface.h:46

[atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8)

long atomic\_t

**Definition** atomic\_types.h:15

[collector.h](collector_8h.md)

Prometheus collector APIs.

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

Atomically get and test a bit.

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

Atomically clear a bit and test it.

**Definition** atomic.h:147

[atomic\_test\_and\_set\_bit](group__atomic__apis.md#ga7ff45e13aa5f8be5d7a550e49f5c720b)

static bool atomic\_test\_and\_set\_bit(atomic\_t \*target, int bit)

Atomically set a bit and test it.

**Definition** atomic.h:170

[K\_FOREVER](group__clock__apis.md#ga0bb4b83f0222193b21a8910311bab0ca)

#define K\_FOREVER

Generate infinite timeout delay.

**Definition** kernel.h:1467

[sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda)

unsigned short int sa\_family\_t

Socket address family type.

**Definition** net\_ip.h:168

[net\_addr\_state](group__ip__4__6.md#ga32e58fc83532ef57eeb6ff952f17288d)

net\_addr\_state

What is the current state of the network address.

**Definition** net\_ip.h:526

[net\_addr\_type](group__ip__4__6.md#gafecee2d4a331dc85ad962b81a6303e41)

net\_addr\_type

How the network address is assigned to network interface.

**Definition** net\_ip.h:534

[k\_mutex\_unlock](group__mutex__apis.md#ga360f4c0e7258b0d7030cdb1f452b2c31)

int k\_mutex\_unlock(struct k\_mutex \*mutex)

Unlock a mutex.

[k\_mutex\_lock](group__mutex__apis.md#ga850549358645249c285669baa49c33b0)

int k\_mutex\_lock(struct k\_mutex \*mutex, k\_timeout\_t timeout)

Lock a mutex.

[net\_verdict](group__net__core.md#ga8e5393f3bdd85491f221324e637c3896)

net\_verdict

Net Verdict.

**Definition** net\_core.h:103

[net\_hostname\_set\_postfix](group__net__hostname.md#ga6aa3799b3b0d7eec7fb8b276485ae2c5)

static int net\_hostname\_set\_postfix(const uint8\_t \*hostname\_postfix, int postfix\_len)

Set the device hostname postfix.

**Definition** hostname.h:111

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

**Definition** net\_if.h:2952

[net\_if\_is\_admin\_up](group__net__if.md#ga099a484a654ad9af35d3212fc2c995b2)

static bool net\_if\_is\_admin\_up(struct net\_if \*iface)

Check if interface was brought up by the administrator.

**Definition** net\_if.h:2916

[net\_if\_set\_default](group__net__if.md#ga0a1f27ec893e1af3c97f130be4616589)

void net\_if\_set\_default(struct net\_if \*iface)

Set the default network interface.

[net\_if\_ipv4\_addr\_lookup\_by\_index](group__net__if.md#ga0a22661727316517685afcd551e7b38e)

int net\_if\_ipv4\_addr\_lookup\_by\_index(const struct in\_addr \*addr)

Check if this IPv4 address belongs to one of the interface indices.

[net\_if\_mcast\_callback\_t](group__net__if.md#ga0d64291573740a67eae7ff3fcc0910c5)

void(\* net\_if\_mcast\_callback\_t)(struct net\_if \*iface, const struct net\_addr \*addr, bool is\_joined)

Define a callback that is called whenever a IPv6 or IPv4 multicast address group is joined or left.

**Definition** net\_if.h:1620

[net\_if\_link\_callback\_t](group__net__if.md#ga0f87d5753fcd7cce40ecd161e6c91078)

void(\* net\_if\_link\_callback\_t)(struct net\_if \*iface, struct net\_linkaddr \*dst, int status)

Define callback that is called after a network packet has been sent.

**Definition** net\_if.h:2719

[net\_if\_get\_wifi\_sta](group__net__if.md#ga0fc3ba6172956f6847027e0bd3d367de)

struct net\_if \* net\_if\_get\_wifi\_sta(void)

Get Wi-Fi network station interface.

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

**Definition** net\_if.h:896

[net\_if\_down](group__net__if.md#ga2187650062d6139b9f4b81745a206803)

int net\_if\_down(struct net\_if \*iface)

Bring interface down.

[net\_if\_ipv4\_router\_find\_default](group__net__if.md#ga25672516d7f383807e7dd9ce5f46a94f)

struct net\_if\_router \* net\_if\_ipv4\_router\_find\_default(struct net\_if \*iface, struct in\_addr \*addr)

Find default router for this IPv4 address.

[net\_if\_ipv6\_addr\_onlink](group__net__if.md#ga25d6e2253c1d361553d478f7c948a28a)

bool net\_if\_ipv6\_addr\_onlink(struct net\_if \*\*iface, struct in6\_addr \*addr)

Check if this IPv6 address is part of the subnet of our network interface.

[net\_if\_router\_ipv4](group__net__if.md#ga2a48e13941c91ddb9bbc63d014729be1)

static struct in\_addr \* net\_if\_router\_ipv4(struct net\_if\_router \*router)

Get the IPv4 address of the given router.

**Definition** net\_if.h:2450

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

[net\_if\_l2\_data](group__net__if.md#ga3cad2d51fc9cc225619585e06e252db0)

static void \* net\_if\_l2\_data(struct net\_if \*iface)

Get a pointer to the interface L2 private data.

**Definition** net\_if.h:970

[net\_if\_are\_pending\_tx\_packets](group__net__if.md#ga3cddda628eca248246f9aa3b81938f95)

static bool net\_if\_are\_pending\_tx\_packets(struct net\_if \*iface)

Check if there are any pending TX network data for a given network interface.

**Definition** net\_if.h:3134

[net\_if\_ipv4\_get\_netmask](group__net__if.md#ga41aeb0e7c5f9bc837f7b2ec13401afd1)

struct in\_addr net\_if\_ipv4\_get\_netmask(struct net\_if \*iface)

Get IPv4 netmask of an interface.

[net\_if\_flag\_test\_and\_set](group__net__if.md#ga42e7482191a92007960601f8bb621dca)

static bool net\_if\_flag\_test\_and\_set(struct net\_if \*iface, enum net\_if\_flag value)

Test and set a value in network interface flags.

**Definition** net\_if.h:826

[net\_if\_ipv4\_addr\_rm](group__net__if.md#ga4433304d46b6559604486b828e7d9dec)

bool net\_if\_ipv4\_addr\_rm(struct net\_if \*iface, const struct in\_addr \*addr)

Remove a IPv4 address from an interface.

[net\_if\_ipv4\_router\_add](group__net__if.md#ga44984001411077c7a2ef68afb361b40f)

struct net\_if\_router \* net\_if\_ipv4\_router\_add(struct net\_if \*iface, struct in\_addr \*addr, bool is\_default, uint16\_t router\_lifetime)

Add IPv4 router to the system.

[net\_if\_get\_link\_addr](group__net__if.md#ga467186e964bf721e14fed38392f21872)

static struct net\_linkaddr \* net\_if\_get\_link\_addr(struct net\_if \*iface)

Get an network interface's link address.

**Definition** net\_if.h:1125

[net\_if\_ipv6\_maddr\_join](group__net__if.md#ga49dbc954015307222f176f4149829b76)

void net\_if\_ipv6\_maddr\_join(struct net\_if \*iface, struct net\_if\_mcast\_addr \*addr)

Mark a given multicast address to be joined.

[net\_if\_ipv6\_select\_src\_addr](group__net__if.md#ga50689a1afdb37a7087bf47a12cc50438)

static const struct in6\_addr \* net\_if\_ipv6\_select\_src\_addr(struct net\_if \*iface, const struct in6\_addr \*dst)

Get a IPv6 source address that should be used when sending network data to destination.

**Definition** net\_if.h:2109

[net\_if\_nbr\_reachability\_hint](group__net__if.md#ga51af469ff3d7d9f760d63a8a9c7be8b5)

static void net\_if\_nbr\_reachability\_hint(struct net\_if \*iface, const struct in6\_addr \*ipv6\_addr)

Provide a reachability hint for IPv6 Neighbor Discovery.

**Definition** net\_if.h:1201

[net\_if\_offload](group__net__if.md#ga520939e94620ca75475a71f153df6d4a)

static struct net\_offload \* net\_if\_offload(struct net\_if \*iface)

Return the IP offload plugin.

**Definition** net\_if.h:1038

[net\_if\_set\_link\_addr](group__net__if.md#ga52b41b2f8b7d3405338a0539542677a0)

static int net\_if\_set\_link\_addr(struct net\_if \*iface, uint8\_t \*addr, uint8\_t len, enum net\_link\_type type)

Set a network interface's link address.

**Definition** net\_if.h:1271

[net\_if\_flag\_set](group__net__if.md#ga52f9fca13e9f836799e0e40f581744d2)

static void net\_if\_flag\_set(struct net\_if \*iface, enum net\_if\_flag value)

Set a value in network interface flags.

**Definition** net\_if.h:808

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

[net\_if\_ipv6\_get\_mcast\_hop\_limit](group__net__if.md#ga56e7086633bcf4537f54c7ca70e6c900)

static uint8\_t net\_if\_ipv6\_get\_mcast\_hop\_limit(struct net\_if \*iface)

Get IPv6 multicast hop limit specified for a given interface.

**Definition** net\_if.h:1940

[net\_if\_ipv6\_addr\_foreach](group__net__if.md#ga5ac646ad7fda0fa48e78c15b4ca52d50)

void net\_if\_ipv6\_addr\_foreach(struct net\_if \*iface, net\_if\_ip\_addr\_cb\_t cb, void \*user\_data)

Go through all IPv6 addresses on a network interface and call callback for each used address.

[net\_if\_ipv6\_set\_hop\_limit](group__net__if.md#ga5bf726bb5c1d232103ec6841e7d0cd8c)

static void net\_if\_ipv6\_set\_hop\_limit(struct net\_if \*iface, uint8\_t hop\_limit)

Set the default IPv6 hop limit of a given interface.

**Definition** net\_if.h:1906

[net\_if\_ipv6\_select\_src\_addr\_hint](group__net__if.md#ga5cf4717e632f712045dd4fe81b30245c)

static const struct in6\_addr \* net\_if\_ipv6\_select\_src\_addr\_hint(struct net\_if \*iface, const struct in6\_addr \*dst, int flags)

Get a IPv6 source address that should be used when sending network data to destination.

**Definition** net\_if.h:2137

[net\_if\_get\_name](group__net__if.md#ga5f653cd73c1ecd548a931eb7fbd170f7)

int net\_if\_get\_name(struct net\_if \*iface, char \*buf, int len)

Get network interface name.

[net\_if\_ipv6\_addr\_rm](group__net__if.md#ga614e1458fa28d26c26f447e9fbcc2cb7)

bool net\_if\_ipv6\_addr\_rm(struct net\_if \*iface, const struct in6\_addr \*addr)

Remove an IPv6 address from an interface.

[net\_if\_ipv6\_get\_hop\_limit](group__net__if.md#ga66d0a9a8eef095f6d4d44f35dd67f2b6)

static uint8\_t net\_if\_ipv6\_get\_hop\_limit(struct net\_if \*iface)

Get IPv6 hop limit specified for a given interface.

**Definition** net\_if.h:1889

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

**Definition** net\_if.h:1010

[net\_if\_is\_dormant](group__net__if.md#ga6e2e6102271c37acaa59c54e2aa6b413)

static bool net\_if\_is\_dormant(struct net\_if \*iface)

Check if the interface is dormant.

**Definition** net\_if.h:2990

[net\_if\_get\_first\_wifi](group__net__if.md#ga6e89bbafb6c0acdc6bf51078e2027236)

struct net\_if \* net\_if\_get\_first\_wifi(void)

Get first Wi-Fi network interface.

[net\_if\_ipv4\_addr\_add](group__net__if.md#ga7190958f740cac56de3a13fe688b3b5d)

struct net\_if\_addr \* net\_if\_ipv4\_addr\_add(struct net\_if \*iface, struct in\_addr \*addr, enum net\_addr\_type addr\_type, uint32\_t vlifetime)

Add a IPv4 address to an interface.

[net\_if\_ipv4\_get\_mcast\_ttl](group__net__if.md#ga71acb65b1988aab8cca9c9604c86231e)

uint8\_t net\_if\_ipv4\_get\_mcast\_ttl(struct net\_if \*iface)

Get IPv4 multicast time-to-live value specified for a given interface.

[net\_if\_ip\_maddr\_cb\_t](group__net__if.md#ga726eed76563c223de8f611e2544febe9)

void(\* net\_if\_ip\_maddr\_cb\_t)(struct net\_if \*iface, struct net\_if\_mcast\_addr \*maddr, void \*user\_data)

Callback used while iterating over network interface multicast IP addresses.

**Definition** net\_if.h:1582

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

**Definition** net\_if.h:1304

[net\_if\_ipv6\_maddr\_add](group__net__if.md#ga7ae82a491193dfea9b92cb9cbaf26f98)

struct net\_if\_mcast\_addr \* net\_if\_ipv6\_maddr\_add(struct net\_if \*iface, const struct in6\_addr \*addr)

Add a IPv6 multicast address to an interface.

[net\_if\_ipv4\_set\_netmask\_by\_addr](group__net__if.md#ga7beda6ccba46fce3cf2da1ce6c0725ec)

bool net\_if\_ipv4\_set\_netmask\_by\_addr(struct net\_if \*iface, const struct in\_addr \*addr, const struct in\_addr \*netmask)

Set IPv4 netmask for an interface index for a given address.

[net\_if\_ipv4\_get\_ttl](group__net__if.md#ga7e1fd28dbcf1164d056296b4df782e64)

uint8\_t net\_if\_ipv4\_get\_ttl(struct net\_if \*iface)

Get IPv4 time-to-live value specified for a given interface.

[net\_if\_is\_up](group__net__if.md#ga7e9b368d4abf9da5656140df70cfa334)

static bool net\_if\_is\_up(struct net\_if \*iface)

Check if interface is up and running.

**Definition** net\_if.h:2890

[net\_if\_need\_calc\_rx\_checksum](group__net__if.md#ga8048e722f6442bcd5b6881bd71e791a5)

bool net\_if\_need\_calc\_rx\_checksum(struct net\_if \*iface, enum net\_if\_checksum\_type chksum\_type)

Check if received network packet checksum calculation can be avoided or not.

[net\_if\_ipv6\_set\_reachable\_time](group__net__if.md#ga8328266b870fd200660cb2becaab3de4)

static void net\_if\_ipv6\_set\_reachable\_time(struct net\_if\_ipv6 \*ipv6)

Set IPv6 reachable time for a given interface.

**Definition** net\_if.h:2031

[net\_if\_ipv6\_get\_ll\_addr](group__net__if.md#ga85b7a923d46d36ecd63f9930bd8970c4)

struct in6\_addr \* net\_if\_ipv6\_get\_ll\_addr(enum net\_addr\_state state, struct net\_if \*\*iface)

Return link local IPv6 address from the first interface that has a link local address matching give s...

[net\_if\_config\_ipv4\_put](group__net__if.md#ga88c13a45617480a665c7f9f589ec8e10)

int net\_if\_config\_ipv4\_put(struct net\_if \*iface)

Release network interface IPv4 config.

[net\_if\_ipv4\_set\_netmask\_by\_addr\_by\_index](group__net__if.md#ga895cfd55f79f7fb78a17cf0e3004fa06)

bool net\_if\_ipv4\_set\_netmask\_by\_addr\_by\_index(int index, const struct in\_addr \*addr, const struct in\_addr \*netmask)

Set IPv4 netmask for an interface index for a given address.

[net\_if\_dormant\_on](group__net__if.md#ga89a3374d4bb116460a7b7c50a750b593)

void net\_if\_dormant\_on(struct net\_if \*iface)

Mark interface as dormant.

[net\_if\_config\_ipv6\_put](group__net__if.md#ga8af1400b354c42a64795cdb1a600ddd6)

int net\_if\_config\_ipv6\_put(struct net\_if \*iface)

Release network interface IPv6 config.

[net\_if\_checksum\_type](group__net__if.md#ga8db412ae79c64cafe81a66f5acb2f8e9)

net\_if\_checksum\_type

Type of checksum for which support in the interface will be queried.

**Definition** net\_if.h:2785

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

[net\_if\_need\_calc\_tx\_checksum](group__net__if.md#ga9634c3e71e934ab3a07bec989b364663)

bool net\_if\_need\_calc\_tx\_checksum(struct net\_if \*iface, enum net\_if\_checksum\_type chksum\_type)

Check if network packet checksum calculation can be avoided or not when sending the packet.

[net\_if\_start\_dad](group__net__if.md#ga9655c010ccbf989e9328271f5dbcc685)

static void net\_if\_start\_dad(struct net\_if \*iface)

Start duplicate address detection procedure.

**Definition** net\_if.h:1158

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

**Definition** net\_if.h:3100

[net\_if\_socket\_offload\_set](group__net__if.md#ga9db52875580115c743b1f35cd6c46796)

static void net\_if\_socket\_offload\_set(struct net\_if \*iface, net\_socket\_create\_t socket\_offload)

Set the function to create an offloaded socket.

**Definition** net\_if.h:1081

[net\_if\_ipv6\_get\_reachable\_time](group__net__if.md#ga9dd1f91edbb519a6a079f363c33efacf)

static uint32\_t net\_if\_ipv6\_get\_reachable\_time(struct net\_if \*iface)

Get IPv6 reachable timeout specified for a given interface.

**Definition** net\_if.h:1998

[net\_if\_is\_promisc](group__net__if.md#ga9f1a6eab849517734ec422deb0ba71f5)

static bool net\_if\_is\_promisc(struct net\_if \*iface)

Check if promiscuous mode is set or not.

**Definition** net\_if.h:3117

[net\_if\_ipv4\_maddr\_is\_joined](group__net__if.md#gaa30769fc8016f1a7496b3ede277d8d8a)

static bool net\_if\_ipv4\_maddr\_is\_joined(struct net\_if\_mcast\_addr \*addr)

Check if given multicast address is joined or not.

**Definition** net\_if.h:2416

[net\_if\_ipv6\_prefix\_set\_lf](group__net__if.md#gaa3c711e814fb6a4e552b4ef723d0baa0)

static void net\_if\_ipv6\_prefix\_set\_lf(struct net\_if\_ipv6\_prefix \*prefix, bool is\_infinite)

Set the infinite status of the prefix.

**Definition** net\_if.h:1763

[net\_if\_ipv4\_maddr\_add](group__net__if.md#gaa43fa83711703f8737e50b639e11b16c)

struct net\_if\_mcast\_addr \* net\_if\_ipv4\_maddr\_add(struct net\_if \*iface, const struct in\_addr \*addr)

Add a IPv4 multicast address to an interface.

[net\_if\_is\_wifi](group__net__if.md#gaa458b5f349c55007108b47b99f4954d5)

bool net\_if\_is\_wifi(struct net\_if \*iface)

Check if the network interface supports Wi-Fi.

[net\_if\_register\_link\_cb](group__net__if.md#gaa81b7d9ed8dc05da3391265dbc89b665)

void net\_if\_register\_link\_cb(struct net\_if\_link\_cb \*link, net\_if\_link\_callback\_t cb)

Register a link callback.

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

**Definition** net\_if.h:1180

[net\_if\_ipv6\_calc\_reachable\_time](group__net__if.md#gab1861b5cefa73b4eefbb447cb1438cdc)

uint32\_t net\_if\_ipv6\_calc\_reachable\_time(struct net\_if\_ipv6 \*ipv6)

Calculate next reachable time value for IPv6 reachable time.

[net\_if\_ipv6\_set\_base\_reachable\_time](group__net__if.md#gab3939d735b660f8f02124df656ceba2c)

static void net\_if\_ipv6\_set\_base\_reachable\_time(struct net\_if \*iface, uint32\_t reachable\_time)

Set IPv6 reachable time for a given interface.

**Definition** net\_if.h:1971

[net\_if\_ipv6\_addr\_lookup\_by\_iface](group__net__if.md#gab53eabb540a4487d83f27c8e319c736a)

struct net\_if\_addr \* net\_if\_ipv6\_addr\_lookup\_by\_iface(struct net\_if \*iface, struct in6\_addr \*addr)

Check if this IPv6 address belongs to this specific interfaces.

[net\_if\_ip\_addr\_cb\_t](group__net__if.md#gab58d8561a4f21899e2db34043d346516)

void(\* net\_if\_ip\_addr\_cb\_t)(struct net\_if \*iface, struct net\_if\_addr \*addr, void \*user\_data)

Callback used while iterating over network interface IP addresses.

**Definition** net\_if.h:1538

[net\_if\_ipv6\_maddr\_foreach](group__net__if.md#gab677496fb2e27be2df299a346e9c7132)

void net\_if\_ipv6\_maddr\_foreach(struct net\_if \*iface, net\_if\_ip\_maddr\_cb\_t cb, void \*user\_data)

Go through all IPv6 multicast addresses on a network interface and call callback for each used addres...

[net\_if\_flag\_test\_and\_clear](group__net__if.md#gab8f371c7f8890cf4728177f6595141d7)

static bool net\_if\_flag\_test\_and\_clear(struct net\_if \*iface, enum net\_if\_flag value)

Test and clear a value in network interface flags.

**Definition** net\_if.h:860

[net\_if\_start\_rs](group__net__if.md#gab9bdb7f8a9eeed4d9b70965b8af82cb7)

void net\_if\_start\_rs(struct net\_if \*iface)

Start neighbor discovery and send router solicitation message.

[net\_if\_ipv6\_maddr\_is\_joined](group__net__if.md#gabe2c16a378a35a22d008bff9142e5449)

static bool net\_if\_ipv6\_maddr\_is\_joined(struct net\_if\_mcast\_addr \*addr)

Check if given multicast address is joined or not.

**Definition** net\_if.h:1688

[net\_if\_ipv6\_addr\_rm\_by\_index](group__net__if.md#gac159e3b0fbf558d5fb09774141da7d6d)

bool net\_if\_ipv6\_addr\_rm\_by\_index(int index, const struct in6\_addr \*addr)

Remove an IPv6 address from an interface by index.

[net\_if\_cb\_t](group__net__if.md#gac48ab8e6337e7cf387af9b293f254a80)

void(\* net\_if\_cb\_t)(struct net\_if \*iface, void \*user\_data)

Callback used while iterating over network interfaces.

**Definition** net\_if.h:2863

[net\_if\_ipv4\_addr\_rm\_by\_index](group__net__if.md#gac5bf15f948ab195cecce98d1b40bda37)

bool net\_if\_ipv4\_addr\_rm\_by\_index(int index, const struct in\_addr \*addr)

Remove a IPv4 address from an interface by interface index.

[net\_if\_ipv6\_get\_global\_addr](group__net__if.md#gaca7d686c772deac13a027cc046333126)

struct in6\_addr \* net\_if\_ipv6\_get\_global\_addr(enum net\_addr\_state state, struct net\_if \*\*iface)

Return global IPv6 address from the first interface that has a global IPv6 address matching the given...

[net\_if\_get\_mtu](group__net__if.md#gacddc98531c5748db5a34f5c3a3e96e86)

static uint16\_t net\_if\_get\_mtu(struct net\_if \*iface)

Get an network interface's MTU.

**Definition** net\_if.h:1289

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

**Definition** net\_if.h:2565

[net\_if\_ipv6\_get\_ll](group__net__if.md#gad6f3e1e349e281887352652f6f32274e)

struct in6\_addr \* net\_if\_ipv6\_get\_ll(struct net\_if \*iface, enum net\_addr\_state addr\_state)

Get a IPv6 link local address in a given state.

[net\_if\_ipv6\_set\_retrans\_timer](group__net__if.md#gad74566e5a34f447d2ac63d2c0e82eeff)

static void net\_if\_ipv6\_set\_retrans\_timer(struct net\_if \*iface, uint32\_t retrans\_timer)

Set IPv6 retransmit timer for a given interface.

**Definition** net\_if.h:2050

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

**Definition** net\_if.h:1813

[net\_if\_ipv4\_maddr\_lookup](group__net__if.md#gadc1514a0d6852de9dbce043bc99d4eb0)

struct net\_if\_mcast\_addr \* net\_if\_ipv4\_maddr\_lookup(const struct in\_addr \*addr, struct net\_if \*\*iface)

Check if this IPv4 multicast address belongs to a specific interface or one of the interfaces.

[net\_if\_router\_rm](group__net__if.md#gadc87242eb7205362a308b3c4437bf76d)

void net\_if\_router\_rm(struct net\_if\_router \*router)

Remove a router from the system.

[net\_if\_ipv6\_get\_retrans\_timer](group__net__if.md#gaddbf5a6ba412e6bdb7e31568fe827bd0)

static uint32\_t net\_if\_ipv6\_get\_retrans\_timer(struct net\_if \*iface)

Get IPv6 retransmit timer specified for a given interface.

**Definition** net\_if.h:2076

[net\_if\_ipv4\_set\_gw\_by\_index](group__net__if.md#gadef49124c331817165475c69fb9104e0)

bool net\_if\_ipv4\_set\_gw\_by\_index(int index, const struct in\_addr \*gw)

Set IPv4 gateway for an interface index.

[net\_if\_ipv4\_get\_netmask\_by\_addr](group__net__if.md#gadfad7d9232bf58c5626266387a2eb761)

struct in\_addr net\_if\_ipv4\_get\_netmask\_by\_addr(struct net\_if \*iface, const struct in\_addr \*addr)

Get IPv4 netmask related to an address of an interface.

[net\_if\_oper\_state](group__net__if.md#gadfe9d90f24046cd9bd4bbee096e747b9)

net\_if\_oper\_state

Network interface operational status (RFC 2863).

**Definition** net\_if.h:306

[net\_if\_ipv6\_addr\_add](group__net__if.md#gae00484a7fe32671a4ca04ff525e640c6)

struct net\_if\_addr \* net\_if\_ipv6\_addr\_add(struct net\_if \*iface, struct in6\_addr \*addr, enum net\_addr\_type addr\_type, uint32\_t vlifetime)

Add a IPv6 address to an interface.

[net\_if\_ipv6\_select\_src\_iface](group__net__if.md#gae1495ac9e743be54b8d90bd4ff4700ab)

static struct net\_if \* net\_if\_ipv6\_select\_src\_iface(const struct in6\_addr \*dst)

Get a network interface that should be used when sending IPv6 network data to destination.

**Definition** net\_if.h:2160

[net\_if\_flag\_is\_set](group__net__if.md#gae1f373ddd61c18a81481d8ddcfb12543)

static bool net\_if\_flag\_is\_set(struct net\_if \*iface, enum net\_if\_flag value)

Check if a value in network interface flags is set.

**Definition** net\_if.h:878

[net\_if\_config\_get](group__net__if.md#gae2323a72714e29836d8296dfc330f7fd)

static struct net\_if\_config \* net\_if\_config\_get(struct net\_if \*iface)

Get network interface IP config.

**Definition** net\_if.h:1355

[net\_if\_get\_config](group__net__if.md#gae271e0e4dcb031a83d9908e597a45048)

static struct net\_if\_config \* net\_if\_get\_config(struct net\_if \*iface)

Return network configuration for this network interface.

**Definition** net\_if.h:1141

[net\_if\_ipv4\_maddr\_join](group__net__if.md#gae275a5e75817aa178d36f422573ad76a)

void net\_if\_ipv4\_maddr\_join(struct net\_if \*iface, struct net\_if\_mcast\_addr \*addr)

Mark a given multicast address to be joined.

[net\_if\_ipv4\_get\_gw](group__net__if.md#gae42f6f9620e40e2d2b36d30e81bb82d9)

struct in\_addr net\_if\_ipv4\_get\_gw(struct net\_if \*iface)

Get IPv4 gateway of an interface.

[net\_if\_addr\_set\_lf](group__net__if.md#gae66f6e7bd31545e6161fcd4600fe5842)

static void net\_if\_addr\_set\_lf(struct net\_if\_addr \*ifaddr, bool is\_infinite)

Set the infinite status of the network interface address.

**Definition** net\_if.h:1320

[net\_if\_flag](group__net__if.md#gae691e5537917ffce27ad0db82c730371)

net\_if\_flag

Network interface flags.

**Definition** net\_if.h:248

[net\_if\_ipv4\_maddr\_foreach](group__net__if.md#gae82f53c670f602e9c37b65abb6dfaec7)

void net\_if\_ipv4\_maddr\_foreach(struct net\_if \*iface, net\_if\_ip\_maddr\_cb\_t cb, void \*user\_data)

Go through all IPv4 multicast addresses on a network interface and call callback for each used addres...

[net\_if\_ipv6\_prefix\_get](group__net__if.md#gae9f98dff661d52c5e3e5e185f0ed9cc0)

struct net\_if\_ipv6\_prefix \* net\_if\_ipv6\_prefix\_get(struct net\_if \*iface, const struct in6\_addr \*addr)

Return prefix that corresponds to this IPv6 address.

[net\_if\_get\_device](group__net__if.md#gaeb8c703f273bc07ae9bb7a0d8bfe6f3d)

static const struct device \* net\_if\_get\_device(struct net\_if \*iface)

Get an network interface's device.

**Definition** net\_if.h:986

[net\_if\_is\_offloaded](group__net__if.md#gaecedc93a6dab2c57fe686718ea4d78af)

bool net\_if\_is\_offloaded(struct net\_if \*iface)

Return offload status of a given network interface.

[net\_socket\_create\_t](group__net__if.md#gaef3dfe26195514aac625e9f22e399759)

int(\* net\_socket\_create\_t)(int, int, int)

A function prototype to create an offloaded socket.

**Definition** net\_if.h:652

[net\_if\_ipv6\_addr\_update\_lifetime](group__net__if.md#gaef8a6752a201f81636c4ffc1ebba4a25)

void net\_if\_ipv6\_addr\_update\_lifetime(struct net\_if\_addr \*ifaddr, uint32\_t vlifetime)

Update validity lifetime time of an IPv6 address.

[net\_if\_ipv6\_maddr\_rm](group__net__if.md#gaf0ce126bb5019ff5f5ff0876b9712ad9)

bool net\_if\_ipv6\_maddr\_rm(struct net\_if \*iface, const struct in6\_addr \*addr)

Remove an IPv6 multicast address from an interface.

[net\_if\_is\_socket\_offloaded](group__net__if.md#gaf308baf2241fa455b50b439b7fab3f1e)

static bool net\_if\_is\_socket\_offloaded(struct net\_if \*iface)

Return the socket offload status.

**Definition** net\_if.h:1060

[net\_if\_ipv6\_set\_mcast\_hop\_limit](group__net__if.md#gaf56a433679ea9701cf8baa3208f8ccc3)

static void net\_if\_ipv6\_set\_mcast\_hop\_limit(struct net\_if \*iface, uint8\_t hop\_limit)

Set the default IPv6 multicast hop limit of a given interface.

**Definition** net\_if.h:1957

[net\_if\_get\_wifi\_sap](group__net__if.md#gaf830eab616191009d88f58b761694b49)

struct net\_if \* net\_if\_get\_wifi\_sap(void)

Get first Wi-Fi network Soft-AP interface.

[net\_if\_set\_promisc](group__net__if.md#gaf9f81f3b9697ca47f7674d85f37a8d80)

static int net\_if\_set\_promisc(struct net\_if \*iface)

Set network interface into promiscuous mode.

**Definition** net\_if.h:3084

[net\_if\_l2](group__net__if.md#gafa451f6118529d1d084704d00b2aae20)

static const struct net\_l2 \* net\_if\_l2(struct net\_if \*iface)

Get a pointer to the interface L2.

**Definition** net\_if.h:944

[net\_if\_socket\_offload](group__net__if.md#gafb2bbaec96c4759d920b2866c0b3ef3a)

static net\_socket\_create\_t net\_if\_socket\_offload(struct net\_if \*iface)

Return the function to create an offloaded socket.

**Definition** net\_if.h:1103

[net\_if\_ipv4\_select\_src\_iface](group__net__if.md#gafea1a35f452ad8168855852cbfdf0024)

static struct net\_if \* net\_if\_ipv4\_select\_src\_iface(const struct in\_addr \*dst)

Get a network interface that should be used when sending IPv4 network data to destination.

**Definition** net\_if.h:2541

[net\_if\_flag\_clear](group__net__if.md#gaff751b6a92b0c608ecfc50e8c0587fd3)

static void net\_if\_flag\_clear(struct net\_if \*iface, enum net\_if\_flag value)

Clear a value in network interface flags.

**Definition** net\_if.h:842

[NET\_IF\_CHECKSUM\_IPV4\_ICMP](group__net__if.md#gga8db412ae79c64cafe81a66f5acb2f8e9a2aef87c97f22fdccdf1925d2687436b1)

@ NET\_IF\_CHECKSUM\_IPV4\_ICMP

Interface supports checksum calculation for ICMP4 payload in IPv4.

**Definition** net\_if.h:2795

[NET\_IF\_CHECKSUM\_IPV6\_TCP](group__net__if.md#gga8db412ae79c64cafe81a66f5acb2f8e9a31e33593e4e7f7f9b36e319e0991ab13)

@ NET\_IF\_CHECKSUM\_IPV6\_TCP

Interface supports checksum calculation for TCP payload in IPv6.

**Definition** net\_if.h:2799

[NET\_IF\_CHECKSUM\_IPV6\_UDP](group__net__if.md#gga8db412ae79c64cafe81a66f5acb2f8e9a70b1272e2125cea9204bae144fd86660)

@ NET\_IF\_CHECKSUM\_IPV6\_UDP

Interface supports checksum calculation for UDP payload in IPv6.

**Definition** net\_if.h:2802

[NET\_IF\_CHECKSUM\_IPV4\_HEADER](group__net__if.md#gga8db412ae79c64cafe81a66f5acb2f8e9a75e4a0946d0e6755ebd7cc62558aee30)

@ NET\_IF\_CHECKSUM\_IPV4\_HEADER

Interface supports IP version 4 header checksum calculation.

**Definition** net\_if.h:2787

[NET\_IF\_CHECKSUM\_IPV4\_TCP](group__net__if.md#gga8db412ae79c64cafe81a66f5acb2f8e9aaed32a3cb700eac3b67c6c7e5a0cd0ad)

@ NET\_IF\_CHECKSUM\_IPV4\_TCP

Interface supports checksum calculation for TCP payload in IPv4.

**Definition** net\_if.h:2789

[NET\_IF\_CHECKSUM\_IPV6\_HEADER](group__net__if.md#gga8db412ae79c64cafe81a66f5acb2f8e9ab204c7d5fddbd2c11e07a8831df6c00b)

@ NET\_IF\_CHECKSUM\_IPV6\_HEADER

Interface supports IP version 6 header checksum calculation.

**Definition** net\_if.h:2797

[NET\_IF\_CHECKSUM\_IPV6\_ICMP](group__net__if.md#gga8db412ae79c64cafe81a66f5acb2f8e9af5b3bc7cb5e9771cd9fd57d9fda4c3b3)

@ NET\_IF\_CHECKSUM\_IPV6\_ICMP

Interface supports checksum calculation for ICMP6 payload in IPv6.

**Definition** net\_if.h:2805

[NET\_IF\_CHECKSUM\_IPV4\_UDP](group__net__if.md#gga8db412ae79c64cafe81a66f5acb2f8e9afe1eaaa765c8ec3c61618e943cd3f1c3)

@ NET\_IF\_CHECKSUM\_IPV4\_UDP

Interface supports checksum calculation for UDP payload in IPv4.

**Definition** net\_if.h:2792

[NET\_IF\_OPER\_TESTING](group__net__if.md#ggadfe9d90f24046cd9bd4bbee096e747b9a2240173b5c247ab5eb0a9a6afafb296f)

@ NET\_IF\_OPER\_TESTING

Training mode.

**Definition** net\_if.h:311

[NET\_IF\_OPER\_DORMANT](group__net__if.md#ggadfe9d90f24046cd9bd4bbee096e747b9a5cbe2aa27a444444d4acf122113d430d)

@ NET\_IF\_OPER\_DORMANT

Waiting external action.

**Definition** net\_if.h:312

[NET\_IF\_OPER\_UP](group__net__if.md#ggadfe9d90f24046cd9bd4bbee096e747b9a6b99bfc28d831292029761d74209ee03)

@ NET\_IF\_OPER\_UP

Interface is up.

**Definition** net\_if.h:313

[NET\_IF\_OPER\_NOTPRESENT](group__net__if.md#ggadfe9d90f24046cd9bd4bbee096e747b9a8f9f55840e75693163197baae9d50c32)

@ NET\_IF\_OPER\_NOTPRESENT

Hardware missing.

**Definition** net\_if.h:308

[NET\_IF\_OPER\_UNKNOWN](group__net__if.md#ggadfe9d90f24046cd9bd4bbee096e747b9ac7cae092ea6ceeb62499a9b435ac4b58)

@ NET\_IF\_OPER\_UNKNOWN

Initial (unknown) value.

**Definition** net\_if.h:307

[NET\_IF\_OPER\_DOWN](group__net__if.md#ggadfe9d90f24046cd9bd4bbee096e747b9adb20a95215310c420f8dae7e17a2f367)

@ NET\_IF\_OPER\_DOWN

Interface is down.

**Definition** net\_if.h:309

[NET\_IF\_OPER\_LOWERLAYERDOWN](group__net__if.md#ggadfe9d90f24046cd9bd4bbee096e747b9ae7e9b8b12ae618a5ee1483dee916aab4)

@ NET\_IF\_OPER\_LOWERLAYERDOWN

Lower layer interface is down.

**Definition** net\_if.h:310

[NET\_IF\_NO\_AUTO\_START](group__net__if.md#ggae691e5537917ffce27ad0db82c730371a0babb762301878eaf8ef8a05213ecf05)

@ NET\_IF\_NO\_AUTO\_START

Do not start the interface immediately after initialization.

**Definition** net\_if.h:264

[NET\_IF\_IPV6\_NO\_MLD](group__net__if.md#ggae691e5537917ffce27ad0db82c730371a1d362cfabb58eb220ddb069431221fbe)

@ NET\_IF\_IPV6\_NO\_MLD

IPv6 Multicast Listener Discovery disabled.

**Definition** net\_if.h:294

[NET\_IF\_POINTOPOINT](group__net__if.md#ggae691e5537917ffce27ad0db82c730371a3256ef2d537c85b4c2b33b92935e1009)

@ NET\_IF\_POINTOPOINT

Interface is pointopoint.

**Definition** net\_if.h:253

[NET\_IF\_IPV6\_NO\_ND](group__net__if.md#ggae691e5537917ffce27ad0db82c730371a542ecce860ef3bf2df493da8d4c6a2f7)

@ NET\_IF\_IPV6\_NO\_ND

IPv6 Neighbor Discovery disabled.

**Definition** net\_if.h:291

[NET\_IF\_FORWARD\_MULTICASTS](group__net__if.md#ggae691e5537917ffce27ad0db82c730371a581971c9d93a910c4c607da45aa2e4ac)

@ NET\_IF\_FORWARD\_MULTICASTS

Flag defines if received multicasts of other interface are forwarded on this interface.

**Definition** net\_if.h:273

[NET\_IF\_IPV4](group__net__if.md#ggae691e5537917ffce27ad0db82c730371a67d2c0fe390ab16f347ee2dc0a056329)

@ NET\_IF\_IPV4

Interface supports IPv4.

**Definition** net\_if.h:276

[NET\_IF\_PROMISC](group__net__if.md#ggae691e5537917ffce27ad0db82c730371a700d92a5b0de3c779e59806137b35141)

@ NET\_IF\_PROMISC

Interface is in promiscuous mode.

**Definition** net\_if.h:256

[NET\_IF\_DORMANT](group__net__if.md#ggae691e5537917ffce27ad0db82c730371a7dd1db72a37b1fbc4c4491ce1c75238d)

@ NET\_IF\_DORMANT

Driver signals dormant.

**Definition** net\_if.h:288

[NET\_IF\_SUSPENDED](group__net__if.md#ggae691e5537917ffce27ad0db82c730371aaaeafc62e61ec120609205770c8b54f0)

@ NET\_IF\_SUSPENDED

Power management specific: interface is being suspended.

**Definition** net\_if.h:267

[NET\_IF\_IPV6](group__net__if.md#ggae691e5537917ffce27ad0db82c730371aab31a9e1e8c02159f45efc4e0455a4d6)

@ NET\_IF\_IPV6

Interface supports IPv6.

**Definition** net\_if.h:279

[NET\_IF\_UP](group__net__if.md#ggae691e5537917ffce27ad0db82c730371ab0ab7393d643354c46c3437d74c15840)

@ NET\_IF\_UP

Interface is admin up.

**Definition** net\_if.h:250

[NET\_IF\_LOWER\_UP](group__net__if.md#ggae691e5537917ffce27ad0db82c730371ab1a529826bad6b4bcd04185372f97d6d)

@ NET\_IF\_LOWER\_UP

Driver signals L1 is up.

**Definition** net\_if.h:285

[NET\_IF\_RUNNING](group__net__if.md#ggae691e5537917ffce27ad0db82c730371add3e2ecdcd5de3154f9bd2836428a25a)

@ NET\_IF\_RUNNING

Interface up and running (ready to receive and transmit).

**Definition** net\_if.h:282

[NET\_IF\_NO\_TX\_LOCK](group__net__if.md#ggae691e5537917ffce27ad0db82c730371ae8d564e1577c8daad8ce50a729c500c9)

@ NET\_IF\_NO\_TX\_LOCK

Mutex locking on TX data path disabled on the interface.

**Definition** net\_if.h:297

[net\_link\_type](group__net__linkaddr.md#ga1312c2322bc4a4f1c3b76d6466806b24)

net\_link\_type

Type of the link address.

**Definition** net\_linkaddr.h:49

[sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8)

struct \_slist sys\_slist\_t

Single-linked list structure.

**Definition** slist.h:49

[sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493)

struct \_snode sys\_snode\_t

Single-linked list node structure.

**Definition** slist.h:39

[IF\_ENABLED](group__sys-util.md#gae67ffe50e848951dbde309ed569ea925)

#define IF\_ENABLED(\_flag, \_code)

Insert code if \_flag is defined and equals 1.

**Definition** util\_macro.h:247

[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33)

#define ENOTSUP

Unsupported value.

**Definition** errno.h:114

[EPERM](group__system__errno.md#gadd669d31505a077f769cff8e66c780b3)

#define EPERM

Not owner.

**Definition** errno.h:39

[hostname.h](hostname_8h.md)

Hostname configuration definitions.

[NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)

#define NULL

**Definition** iar\_missing\_defs.h:20

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

[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)

flags

**Definition** parser.h:97

[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)

state

**Definition** parser\_state.h:29

[slist.h](slist_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2)

\_\_INT32\_TYPE\_\_ int32\_t

**Definition** stdint.h:74

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

**Definition** device.h:453

[in6\_addr](structin6__addr.md)

IPv6 address struct.

**Definition** net\_ip.h:143

[in\_addr](structin__addr.md)

IPv4 address struct.

**Definition** net\_ip.h:155

[k\_fifo](structk__fifo.md)

**Definition** kernel.h:2495

[k\_mutex](structk__mutex.md)

Mutex Structure.

**Definition** kernel.h:3025

[k\_thread](structk__thread.md)

Thread Structure.

**Definition** thread.h:259

[k\_timepoint\_t](structk__timepoint__t.md)

Kernel timepoint type.

**Definition** sys\_clock.h:227

[net\_dhcpv6\_params](structnet__dhcpv6__params.md)

DHCPv6 client configuration parameters.

**Definition** dhcpv6.h:63

[net\_if\_addr\_ipv4](structnet__if__addr__ipv4.md)

Network Interface unicast IPv4 address and netmask.

**Definition** net\_if.h:467

[net\_if\_addr\_ipv4::ipv4](structnet__if__addr__ipv4.md#a9d8924e263cc7401569c934533a04b48)

struct net\_if\_addr ipv4

IPv4 address.

**Definition** net\_if.h:469

[net\_if\_addr\_ipv4::netmask](structnet__if__addr__ipv4.md#ae1720720e7e36ccf38d0b282d3150774)

struct in\_addr netmask

Netmask.

**Definition** net\_if.h:471

[net\_if\_addr](structnet__if__addr.md)

Network Interface unicast IP addresses.

**Definition** net\_if.h:56

[net\_if\_addr::address](structnet__if__addr.md#a06b8d2e8b5ea6d8d671800d966163763)

struct net\_addr address

IP address.

**Definition** net\_if.h:58

[net\_if\_addr::is\_mesh\_local](structnet__if__addr.md#a1db7cc6c7566baf9340dab6771ca5010)

uint8\_t is\_mesh\_local

Is this IP address usage limited to the subnet (mesh) or not.

**Definition** net\_if.h:142

[net\_if\_addr::is\_temporary](structnet__if__addr.md#a1dd933a37afcb7d708cd602911c38e0a)

uint8\_t is\_temporary

Is this IP address temporary and generated for example by IPv6 privacy extension (RFC 8981).

**Definition** net\_if.h:147

[net\_if\_addr::addr\_state](structnet__if__addr.md#a3106fdcf0dd2479c95efafc586217a2c)

enum net\_addr\_state addr\_state

What is the current state of the address.

**Definition** net\_if.h:73

[net\_if\_addr::is\_infinite](structnet__if__addr.md#a6e799428eb0633a25e4dc3c55e3a3b8c)

uint8\_t is\_infinite

Is the IP address valid forever.

**Definition** net\_if.h:136

[net\_if\_addr::atomic\_ref](structnet__if__addr.md#a9abaf23ec98b22d1741bae410a1f7f3e)

atomic\_t atomic\_ref

Reference counter.

**Definition** net\_if.h:63

[net\_if\_addr::is\_added](structnet__if__addr.md#aa556ea52e1f923fd3e39328dc254c365)

uint8\_t is\_added

Was this address added or not.

**Definition** net\_if.h:150

[net\_if\_addr::addr\_type](structnet__if__addr.md#ab4fd41001cc24615803bfabb9d48e7eb)

enum net\_addr\_type addr\_type

How the IP address was set.

**Definition** net\_if.h:70

[net\_if\_addr::is\_used](structnet__if__addr.md#aed4d91ba064d24ad0d53c0960cde0352)

uint8\_t is\_used

Is this IP address used or not.

**Definition** net\_if.h:139

[net\_if\_config](structnet__if__config.md)

IP and other configuration related data for network interface.

**Definition** net\_if.h:585

[net\_if\_dev](structnet__if__dev.md)

Network Interface Device structure.

**Definition** net\_if.h:668

[net\_if\_dev::oper\_state](structnet__if__dev.md#a30eabb2ffae082d0de81a50c510738a3)

enum net\_if\_oper\_state oper\_state

RFC 2863 operational status.

**Definition** net\_if.h:704

[net\_if\_dev::l2](structnet__if__dev.md#a85d713c62875f5fe9e3ec29773150797)

const struct net\_l2 \*const l2

Interface's L2 layer.

**Definition** net\_if.h:673

[net\_if\_dev::l2\_data](structnet__if__dev.md#a8fec6a7f612fc1268ef486d8bdebe018)

void \* l2\_data

Interface's private L2 data pointer.

**Definition** net\_if.h:676

[net\_if\_dev::mtu](structnet__if__dev.md#aa15ccca2eb67b8d2afca153ccacb3742)

uint16\_t mtu

The hardware MTU.

**Definition** net\_if.h:694

[net\_if\_dev::dev](structnet__if__dev.md#aab633a44f165f571910dc9fc9e131c50)

const struct device \* dev

The actually device driver instance the net\_if is related to.

**Definition** net\_if.h:670

[net\_if\_dev::link\_addr](structnet__if__dev.md#aac6d5d341ab520e6aac7f7b03737c197)

struct net\_linkaddr link\_addr

The hardware link address.

**Definition** net\_if.h:682

[net\_if\_dev::flags](structnet__if__dev.md#ac8f9c30e1dea05c28c88d3b367b130f5)

atomic\_t flags[ATOMIC\_BITMAP\_SIZE(NET\_IF\_NUM\_FLAGS)]

For internal use.

**Definition** net\_if.h:679

[net\_if\_ip](structnet__if__ip.md)

Network interface IP address configuration.

**Definition** net\_if.h:572

[net\_if\_ipv4](structnet__if__ipv4.md)

IPv4 configuration.

**Definition** net\_if.h:475

[net\_if\_ipv4::mcast\_ttl](structnet__if__ipv4.md#a7e9bf16d51989cfcfe564f4f0a43b480)

uint8\_t mcast\_ttl

IPv4 time-to-live for multicast packets.

**Definition** net\_if.h:489

[net\_if\_ipv4::unicast](structnet__if__ipv4.md#a806cf92123452ed3aa93540803b0a8d3)

struct net\_if\_addr\_ipv4 unicast[NET\_IF\_MAX\_IPV4\_ADDR]

Unicast IP addresses.

**Definition** net\_if.h:477

[net\_if\_ipv4::gw](structnet__if__ipv4.md#aa24772c7202bf465ee3da94a172b7bcb)

struct in\_addr gw

Gateway.

**Definition** net\_if.h:483

[net\_if\_ipv4::ttl](structnet__if__ipv4.md#acdc6d5d6eb5362f4f6d2c027cc40e684)

uint8\_t ttl

IPv4 time-to-live.

**Definition** net\_if.h:486

[net\_if\_ipv4::mcast](structnet__if__ipv4.md#adfaf5b50255bd35297195a7218729ae7)

struct net\_if\_mcast\_addr mcast[NET\_IF\_MAX\_IPV4\_MADDR]

Multicast IP addresses.

**Definition** net\_if.h:480

[net\_if\_ipv6\_prefix](structnet__if__ipv6__prefix.md)

Network Interface IPv6 prefixes.

**Definition** net\_if.h:192

[net\_if\_ipv6\_prefix::iface](structnet__if__ipv6__prefix.md#a0e2d1997e2ccfe1e1af5f16e0c74ed92)

struct net\_if \* iface

Backpointer to network interface where this prefix is used.

**Definition** net\_if.h:200

[net\_if\_ipv6\_prefix::is\_infinite](structnet__if__ipv6__prefix.md#a22090441b27bed06098679bf23b4e1e9)

uint8\_t is\_infinite

Is the IP prefix valid forever.

**Definition** net\_if.h:206

[net\_if\_ipv6\_prefix::len](structnet__if__ipv6__prefix.md#a4d2bc2acbe51256b76cf4d3ced3aac39)

uint8\_t len

Prefix length.

**Definition** net\_if.h:203

[net\_if\_ipv6\_prefix::prefix](structnet__if__ipv6__prefix.md#a65b450d0942b3c96cfc575b462d82028)

struct in6\_addr prefix

IPv6 prefix.

**Definition** net\_if.h:197

[net\_if\_ipv6\_prefix::is\_used](structnet__if__ipv6__prefix.md#a6a4295256957e5eddf149f1ceff62e3f)

uint8\_t is\_used

Is this prefix used or not.

**Definition** net\_if.h:209

[net\_if\_ipv6\_prefix::lifetime](structnet__if__ipv6__prefix.md#a925a97a49d383bd4ce475f5d09fcb7e3)

struct net\_timeout lifetime

Prefix lifetime.

**Definition** net\_if.h:194

[net\_if\_ipv6](structnet__if__ipv6.md)

IPv6 configuration.

**Definition** net\_if.h:333

[net\_if\_ipv6::prefix](structnet__if__ipv6.md#a2dccdc984f08527302d8d910a2658f72)

struct net\_if\_ipv6\_prefix prefix[NET\_IF\_MAX\_IPV6\_PREFIX]

Prefixes.

**Definition** net\_if.h:341

[net\_if\_ipv6::base\_reachable\_time](structnet__if__ipv6.md#a500a78fe23ee2ebc63f3d3b53b5b92ea)

uint32\_t base\_reachable\_time

Default reachable time (RFC 4861, page 52).

**Definition** net\_if.h:344

[net\_if\_ipv6::hop\_limit](structnet__if__ipv6.md#a71775a082984274fbc7c009ead18e751)

uint8\_t hop\_limit

IPv6 hop limit.

**Definition** net\_if.h:382

[net\_if\_ipv6::mcast](structnet__if__ipv6.md#a727d2773e0dee3be687dda5b2dd55682)

struct net\_if\_mcast\_addr mcast[NET\_IF\_MAX\_IPV6\_MADDR]

Multicast IP addresses.

**Definition** net\_if.h:338

[net\_if\_ipv6::retrans\_timer](structnet__if__ipv6.md#ac5ee47ff9d3e429ecbb8623e5d713246)

uint32\_t retrans\_timer

Retransmit timer (RFC 4861, page 52).

**Definition** net\_if.h:350

[net\_if\_ipv6::unicast](structnet__if__ipv6.md#adb6431d336cc3f46972e13d2255452c8)

struct net\_if\_addr unicast[NET\_IF\_MAX\_IPV6\_ADDR]

Unicast IP addresses.

**Definition** net\_if.h:335

[net\_if\_ipv6::mcast\_hop\_limit](structnet__if__ipv6.md#ae94906c28578f2e1ea2506b0e2972d4c)

uint8\_t mcast\_hop\_limit

IPv6 multicast hop limit.

**Definition** net\_if.h:385

[net\_if\_ipv6::reachable\_time](structnet__if__ipv6.md#af57b7dca189167f8cc757c4ed6b08f2f)

uint32\_t reachable\_time

Reachable time (RFC 4861, page 20).

**Definition** net\_if.h:347

[net\_if\_link\_cb](structnet__if__link__cb.md)

Link callback handler struct.

**Definition** net\_if.h:2731

[net\_if\_link\_cb::cb](structnet__if__link__cb.md#a66092a22cba3dd69ac1a91c3522240bb)

net\_if\_link\_callback\_t cb

Link callback.

**Definition** net\_if.h:2736

[net\_if\_link\_cb::node](structnet__if__link__cb.md#accae7945a802c5b7fc36948b12a365ef)

sys\_snode\_t node

Node information for the slist.

**Definition** net\_if.h:2733

[net\_if\_mcast\_addr](structnet__if__mcast__addr.md)

Network Interface multicast IP addresses.

**Definition** net\_if.h:160

[net\_if\_mcast\_addr::address](structnet__if__mcast__addr.md#a3e470fc2eb02ac9e5d3d7d0bea0aaa69)

struct net\_addr address

IP address.

**Definition** net\_if.h:162

[net\_if\_mcast\_addr::is\_joined](structnet__if__mcast__addr.md#a4af9009b2f9ccc0589a9ba6dac10927b)

uint8\_t is\_joined

Did we join to this group.

**Definition** net\_if.h:182

[net\_if\_mcast\_addr::rejoin\_node](structnet__if__mcast__addr.md#a74db1527b3a2b614509cc43fdf7d09ef)

sys\_snode\_t rejoin\_node

Rejoining multicast groups list node.

**Definition** net\_if.h:165

[net\_if\_mcast\_addr::is\_used](structnet__if__mcast__addr.md#abab3e6dba72e24ef522c033d277369ca)

uint8\_t is\_used

Is this multicast IP address used or not.

**Definition** net\_if.h:179

[net\_if\_mcast\_monitor](structnet__if__mcast__monitor.md)

Multicast monitor handler struct.

**Definition** net\_if.h:1632

[net\_if\_mcast\_monitor::node](structnet__if__mcast__monitor.md#a570b7d8a8a5fabca83982a5f7d1d896a)

sys\_snode\_t node

Node information for the slist.

**Definition** net\_if.h:1634

[net\_if\_mcast\_monitor::cb](structnet__if__mcast__monitor.md#aec441b858a5f6792ac9cdbc625f6babe)

net\_if\_mcast\_callback\_t cb

Multicast callback.

**Definition** net\_if.h:1640

[net\_if\_mcast\_monitor::iface](structnet__if__mcast__monitor.md#af4d0e937b2b9161918a13a0d6723c60a)

struct net\_if \* iface

Network interface.

**Definition** net\_if.h:1637

[net\_if\_router](structnet__if__router.md)

Information about routers in the system.

**Definition** net\_if.h:219

[net\_if\_router::iface](structnet__if__router.md#a03789aa0a40f7686b76616de0ca0401a)

struct net\_if \* iface

Network interface the router is connected to.

**Definition** net\_if.h:227

[net\_if\_router::is\_default](structnet__if__router.md#a34745207edcad2745d6ce311e2bf1894)

uint8\_t is\_default

Is default router.

**Definition** net\_if.h:239

[net\_if\_router::lifetime](structnet__if__router.md#a4b0d2ad8f225ab61022c10dfce3db199)

uint16\_t lifetime

Router lifetime.

**Definition** net\_if.h:233

[net\_if\_router::is\_infinite](structnet__if__router.md#a4cb47f30241ae3d410f56f1487254ed0)

uint8\_t is\_infinite

Is the router valid forever.

**Definition** net\_if.h:242

[net\_if\_router::is\_used](structnet__if__router.md#a7196e6d2bc2c958d98dfe29143a62048)

uint8\_t is\_used

Is this router used or not.

**Definition** net\_if.h:236

[net\_if\_router::address](structnet__if__router.md#a86a2ca1b95e348acbde8ce90986b83db)

struct net\_addr address

IP address.

**Definition** net\_if.h:224

[net\_if\_router::node](structnet__if__router.md#aabbac0cd0a59ca0eafdcfc0eaf5d909a)

sys\_snode\_t node

Slist lifetime timer node.

**Definition** net\_if.h:221

[net\_if\_router::life\_start](structnet__if__router.md#adf4f4c722917b3c30f8c73bc2519957f)

uint32\_t life\_start

Router life timer start.

**Definition** net\_if.h:230

[net\_if](structnet__if.md)

Network Interface structure.

**Definition** net\_if.h:714

[net\_if::if\_dev](structnet__if.md#a0982ba2019cdaa7701162e60fdb2171e)

struct net\_if\_dev \* if\_dev

The net\_if\_dev instance the net\_if is related to.

**Definition** net\_if.h:716

[net\_if::config](structnet__if.md#a5e71962f55bdead7bfbbb96518c6c404)

struct net\_if\_config config

Network interface instance configuration.

**Definition** net\_if.h:728

[net\_if::pe\_enabled](structnet__if.md#aa96a6a2d55f6a4ece2f340eef526ef56)

uint8\_t pe\_enabled

Network interface specific flags.

**Definition** net\_if.h:748

[net\_if::lock](structnet__if.md#ace2233b71da53ff0fc7cd564ccfc5a03)

struct k\_mutex lock

Mutex protecting this network interface instance.

**Definition** net\_if.h:739

[net\_if::pe\_prefer\_public](structnet__if.md#aec585e283c9053443ff05b364acf76eb)

uint8\_t pe\_prefer\_public

If PE is enabled, then this tells whether public addresses are preferred over temporary ones for this...

**Definition** net\_if.h:753

[net\_if::tx\_lock](structnet__if.md#af00f729ebddfdcf725169f61b6cd586b)

struct k\_mutex tx\_lock

Mutex used when sending data.

**Definition** net\_if.h:742

[net\_l2](structnet__l2.md)

Network L2 structure.

**Definition** net\_l2.h:58

[net\_linkaddr](structnet__linkaddr.md)

Hardware link address structure.

**Definition** net\_linkaddr.h:69

[net\_linkaddr::addr](structnet__linkaddr.md#a2176a9f7a444ac3b0108102d8cf852f0)

uint8\_t \* addr

The array of byte representing the address.

**Definition** net\_linkaddr.h:71

[net\_linkaddr::type](structnet__linkaddr.md#a5f5b4c3d353261d0fab8011aa09f00d7)

uint8\_t type

What kind of address is this for.

**Definition** net\_linkaddr.h:77

[net\_linkaddr::len](structnet__linkaddr.md#a7b2f8ebe68b557eb9cbb4c2f2ecd70e0)

uint8\_t len

Length of that address array.

**Definition** net\_linkaddr.h:74

[net\_pkt](structnet__pkt.md)

Network packet.

**Definition** net\_pkt.h:91

[net\_stats](structnet__stats.md)

All network statistics in one struct.

**Definition** net\_stats.h:378

[net\_timeout](structnet__timeout.md)

Generic struct for handling network timeouts.

**Definition** net\_timeout.h:57

[net\_traffic\_class](structnet__traffic__class.md)

Network traffic class.

**Definition** net\_if.h:629

[net\_traffic\_class::stack](structnet__traffic__class.md#a2d98bc68d38bdef649d645b8b52516c5)

k\_thread\_stack\_t \* stack

Stack for this handler.

**Definition** net\_if.h:643

[net\_traffic\_class::handler](structnet__traffic__class.md#a8d0023588fee0a8ff1381bbc80ada143)

struct k\_thread handler

Traffic class handler thread.

**Definition** net\_if.h:640

[net\_traffic\_class::fifo](structnet__traffic__class.md#a94511ca12bad1687f5c7ca862c857ded)

struct k\_fifo fifo

Fifo for handling this Tx or Rx packet.

**Definition** net\_if.h:631

[prometheus\_collector](structprometheus__collector.md)

Prometheus collector definition.

**Definition** collector.h:50

[prometheus\_metric](structprometheus__metric.md)

Type used to represent a Prometheus metric base.

**Definition** metric.h:47

[sockaddr](structsockaddr.md)

Generic sockaddr struct.

**Definition** net\_ip.h:408

[iterable\_sections.h](sys_2iterable__sections_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [net\_if.h](net__if_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
