---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/net__if_8h_source.html
original_path: doxygen/html/net__if_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
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

45#ifdef \_\_cplusplus

46extern "C" {

47#endif

48

[ 54](structnet__if__addr.md)struct [net\_if\_addr](structnet__if__addr.md) {

[ 56](structnet__if__addr.md#a06b8d2e8b5ea6d8d671800d966163763) struct net\_addr [address](structnet__if__addr.md#a06b8d2e8b5ea6d8d671800d966163763);

57

[ 61](structnet__if__addr.md#a9abaf23ec98b22d1741bae410a1f7f3e) [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) [atomic\_ref](structnet__if__addr.md#a9abaf23ec98b22d1741bae410a1f7f3e);

62

63#if defined(CONFIG\_NET\_NATIVE\_IPV6)

64 struct [net\_timeout](structnet__timeout.md) lifetime;

65#endif

66

[ 68](structnet__if__addr.md#ab4fd41001cc24615803bfabb9d48e7eb) enum [net\_addr\_type](group__ip__4__6.md#gafecee2d4a331dc85ad962b81a6303e41) [addr\_type](structnet__if__addr.md#ab4fd41001cc24615803bfabb9d48e7eb);

69

[ 71](structnet__if__addr.md#a3106fdcf0dd2479c95efafc586217a2c) enum [net\_addr\_state](group__ip__4__6.md#ga32e58fc83532ef57eeb6ff952f17288d) [addr\_state](structnet__if__addr.md#a3106fdcf0dd2479c95efafc586217a2c);

72

73#if defined(CONFIG\_NET\_NATIVE\_IPV6)

74#if defined(CONFIG\_NET\_IPV6\_PE)

78 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) addr\_create\_time;

79

82 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) addr\_preferred\_lifetime;

83

88 [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) addr\_timeout;

89#endif

90#endif /\* CONFIG\_NET\_NATIVE\_IPV6 \*/

91

92 union {

93#if defined(CONFIG\_NET\_IPV6\_DAD)

94 struct {

96 [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) dad\_node;

97 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) dad\_start;

98

100 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) dad\_count;

101 };

102#endif /\* CONFIG\_NET\_IPV6\_DAD \*/

103#if defined(CONFIG\_NET\_IPV4\_ACD)

104 struct {

106 [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) acd\_node;

107 [k\_timepoint\_t](structk__timepoint__t.md) acd\_timeout;

108

110 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) acd\_count;

111

113 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) acd\_state;

114 };

115#endif /\* CONFIG\_NET\_IPV4\_ACD \*/

116 };

117

118#if defined(CONFIG\_NET\_IPV6\_DAD) || defined(CONFIG\_NET\_IPV4\_ACD)

120 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ifindex;

121#endif

122

[ 124](structnet__if__addr.md#a6e799428eb0633a25e4dc3c55e3a3b8c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [is\_infinite](structnet__if__addr.md#a6e799428eb0633a25e4dc3c55e3a3b8c) : 1;

125

[ 127](structnet__if__addr.md#aed4d91ba064d24ad0d53c0960cde0352) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [is\_used](structnet__if__addr.md#aed4d91ba064d24ad0d53c0960cde0352) : 1;

128

[ 130](structnet__if__addr.md#a1db7cc6c7566baf9340dab6771ca5010) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [is\_mesh\_local](structnet__if__addr.md#a1db7cc6c7566baf9340dab6771ca5010) : 1;

131

[ 135](structnet__if__addr.md#a1dd933a37afcb7d708cd602911c38e0a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [is\_temporary](structnet__if__addr.md#a1dd933a37afcb7d708cd602911c38e0a) : 1;

136

137 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \_unused : 4;

138};

139

[ 145](structnet__if__mcast__addr.md)struct [net\_if\_mcast\_addr](structnet__if__mcast__addr.md) {

[ 147](structnet__if__mcast__addr.md#a3e470fc2eb02ac9e5d3d7d0bea0aaa69) struct net\_addr [address](structnet__if__mcast__addr.md#a3e470fc2eb02ac9e5d3d7d0bea0aaa69);

148

149#if defined(CONFIG\_NET\_IPV4\_IGMPV3)

151 struct net\_addr sources[CONFIG\_NET\_IF\_MCAST\_IPV4\_SOURCE\_COUNT];

152

154 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) sources\_len;

155

157 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) record\_type;

158#endif

159

[ 161](structnet__if__mcast__addr.md#abab3e6dba72e24ef522c033d277369ca) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [is\_used](structnet__if__mcast__addr.md#abab3e6dba72e24ef522c033d277369ca) : 1;

162

[ 164](structnet__if__mcast__addr.md#a4af9009b2f9ccc0589a9ba6dac10927b) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [is\_joined](structnet__if__mcast__addr.md#a4af9009b2f9ccc0589a9ba6dac10927b) : 1;

165

166 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \_unused : 6;

167};

168

[ 174](structnet__if__ipv6__prefix.md)struct [net\_if\_ipv6\_prefix](structnet__if__ipv6__prefix.md) {

[ 176](structnet__if__ipv6__prefix.md#a925a97a49d383bd4ce475f5d09fcb7e3) struct [net\_timeout](structnet__timeout.md) [lifetime](structnet__if__ipv6__prefix.md#a925a97a49d383bd4ce475f5d09fcb7e3);

177

[ 179](structnet__if__ipv6__prefix.md#a65b450d0942b3c96cfc575b462d82028) struct [in6\_addr](structin6__addr.md) [prefix](structnet__if__ipv6__prefix.md#a65b450d0942b3c96cfc575b462d82028);

180

[ 182](structnet__if__ipv6__prefix.md#a0e2d1997e2ccfe1e1af5f16e0c74ed92) struct [net\_if](structnet__if.md) \*[iface](structnet__if__ipv6__prefix.md#a0e2d1997e2ccfe1e1af5f16e0c74ed92);

183

[ 185](structnet__if__ipv6__prefix.md#a4d2bc2acbe51256b76cf4d3ced3aac39) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [len](structnet__if__ipv6__prefix.md#a4d2bc2acbe51256b76cf4d3ced3aac39);

186

[ 188](structnet__if__ipv6__prefix.md#a22090441b27bed06098679bf23b4e1e9) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [is\_infinite](structnet__if__ipv6__prefix.md#a22090441b27bed06098679bf23b4e1e9) : 1;

189

[ 191](structnet__if__ipv6__prefix.md#a6a4295256957e5eddf149f1ceff62e3f) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [is\_used](structnet__if__ipv6__prefix.md#a6a4295256957e5eddf149f1ceff62e3f) : 1;

192

193 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \_unused : 6;

194};

195

[ 201](structnet__if__router.md)struct [net\_if\_router](structnet__if__router.md) {

[ 203](structnet__if__router.md#aabbac0cd0a59ca0eafdcfc0eaf5d909a) [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) [node](structnet__if__router.md#aabbac0cd0a59ca0eafdcfc0eaf5d909a);

204

[ 206](structnet__if__router.md#a86a2ca1b95e348acbde8ce90986b83db) struct net\_addr [address](structnet__if__router.md#a86a2ca1b95e348acbde8ce90986b83db);

207

[ 209](structnet__if__router.md#a03789aa0a40f7686b76616de0ca0401a) struct [net\_if](structnet__if.md) \*[iface](structnet__if__router.md#a03789aa0a40f7686b76616de0ca0401a);

210

[ 212](structnet__if__router.md#adf4f4c722917b3c30f8c73bc2519957f) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [life\_start](structnet__if__router.md#adf4f4c722917b3c30f8c73bc2519957f);

213

[ 215](structnet__if__router.md#a4b0d2ad8f225ab61022c10dfce3db199) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [lifetime](structnet__if__router.md#a4b0d2ad8f225ab61022c10dfce3db199);

216

[ 218](structnet__if__router.md#a7196e6d2bc2c958d98dfe29143a62048) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [is\_used](structnet__if__router.md#a7196e6d2bc2c958d98dfe29143a62048) : 1;

219

[ 221](structnet__if__router.md#a34745207edcad2745d6ce311e2bf1894) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [is\_default](structnet__if__router.md#a34745207edcad2745d6ce311e2bf1894) : 1;

222

[ 224](structnet__if__router.md#a4cb47f30241ae3d410f56f1487254ed0) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [is\_infinite](structnet__if__router.md#a4cb47f30241ae3d410f56f1487254ed0) : 1;

225

226 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \_unused : 5;

227};

228

[ 230](group__net__if.md#gae691e5537917ffce27ad0db82c730371)enum [net\_if\_flag](group__net__if.md#gae691e5537917ffce27ad0db82c730371) {

[ 232](group__net__if.md#ggae691e5537917ffce27ad0db82c730371ab0ab7393d643354c46c3437d74c15840) [NET\_IF\_UP](group__net__if.md#ggae691e5537917ffce27ad0db82c730371ab0ab7393d643354c46c3437d74c15840),

233

[ 235](group__net__if.md#ggae691e5537917ffce27ad0db82c730371a3256ef2d537c85b4c2b33b92935e1009) [NET\_IF\_POINTOPOINT](group__net__if.md#ggae691e5537917ffce27ad0db82c730371a3256ef2d537c85b4c2b33b92935e1009),

236

[ 238](group__net__if.md#ggae691e5537917ffce27ad0db82c730371a700d92a5b0de3c779e59806137b35141) [NET\_IF\_PROMISC](group__net__if.md#ggae691e5537917ffce27ad0db82c730371a700d92a5b0de3c779e59806137b35141),

239

[ 246](group__net__if.md#ggae691e5537917ffce27ad0db82c730371a0babb762301878eaf8ef8a05213ecf05) [NET\_IF\_NO\_AUTO\_START](group__net__if.md#ggae691e5537917ffce27ad0db82c730371a0babb762301878eaf8ef8a05213ecf05),

247

[ 249](group__net__if.md#ggae691e5537917ffce27ad0db82c730371aaaeafc62e61ec120609205770c8b54f0) [NET\_IF\_SUSPENDED](group__net__if.md#ggae691e5537917ffce27ad0db82c730371aaaeafc62e61ec120609205770c8b54f0),

250

[ 255](group__net__if.md#ggae691e5537917ffce27ad0db82c730371a581971c9d93a910c4c607da45aa2e4ac) [NET\_IF\_FORWARD\_MULTICASTS](group__net__if.md#ggae691e5537917ffce27ad0db82c730371a581971c9d93a910c4c607da45aa2e4ac),

256

[ 258](group__net__if.md#ggae691e5537917ffce27ad0db82c730371a67d2c0fe390ab16f347ee2dc0a056329) [NET\_IF\_IPV4](group__net__if.md#ggae691e5537917ffce27ad0db82c730371a67d2c0fe390ab16f347ee2dc0a056329),

259

[ 261](group__net__if.md#ggae691e5537917ffce27ad0db82c730371aab31a9e1e8c02159f45efc4e0455a4d6) [NET\_IF\_IPV6](group__net__if.md#ggae691e5537917ffce27ad0db82c730371aab31a9e1e8c02159f45efc4e0455a4d6),

262

[ 264](group__net__if.md#ggae691e5537917ffce27ad0db82c730371add3e2ecdcd5de3154f9bd2836428a25a) [NET\_IF\_RUNNING](group__net__if.md#ggae691e5537917ffce27ad0db82c730371add3e2ecdcd5de3154f9bd2836428a25a),

265

[ 267](group__net__if.md#ggae691e5537917ffce27ad0db82c730371ab1a529826bad6b4bcd04185372f97d6d) [NET\_IF\_LOWER\_UP](group__net__if.md#ggae691e5537917ffce27ad0db82c730371ab1a529826bad6b4bcd04185372f97d6d),

268

[ 270](group__net__if.md#ggae691e5537917ffce27ad0db82c730371a7dd1db72a37b1fbc4c4491ce1c75238d) [NET\_IF\_DORMANT](group__net__if.md#ggae691e5537917ffce27ad0db82c730371a7dd1db72a37b1fbc4c4491ce1c75238d),

271

[ 273](group__net__if.md#ggae691e5537917ffce27ad0db82c730371a542ecce860ef3bf2df493da8d4c6a2f7) [NET\_IF\_IPV6\_NO\_ND](group__net__if.md#ggae691e5537917ffce27ad0db82c730371a542ecce860ef3bf2df493da8d4c6a2f7),

274

[ 276](group__net__if.md#ggae691e5537917ffce27ad0db82c730371a1d362cfabb58eb220ddb069431221fbe) [NET\_IF\_IPV6\_NO\_MLD](group__net__if.md#ggae691e5537917ffce27ad0db82c730371a1d362cfabb58eb220ddb069431221fbe),

277

[ 279](group__net__if.md#ggae691e5537917ffce27ad0db82c730371ae8d564e1577c8daad8ce50a729c500c9) [NET\_IF\_NO\_TX\_LOCK](group__net__if.md#ggae691e5537917ffce27ad0db82c730371ae8d564e1577c8daad8ce50a729c500c9),

280

282 /\* Total number of flags - must be at the end of the enum \*/

283 NET\_IF\_NUM\_FLAGS

285};

286

[ 288](group__net__if.md#gadfe9d90f24046cd9bd4bbee096e747b9)enum [net\_if\_oper\_state](group__net__if.md#gadfe9d90f24046cd9bd4bbee096e747b9) {

[ 289](group__net__if.md#ggadfe9d90f24046cd9bd4bbee096e747b9ac7cae092ea6ceeb62499a9b435ac4b58) [NET\_IF\_OPER\_UNKNOWN](group__net__if.md#ggadfe9d90f24046cd9bd4bbee096e747b9ac7cae092ea6ceeb62499a9b435ac4b58),

[ 290](group__net__if.md#ggadfe9d90f24046cd9bd4bbee096e747b9a8f9f55840e75693163197baae9d50c32) [NET\_IF\_OPER\_NOTPRESENT](group__net__if.md#ggadfe9d90f24046cd9bd4bbee096e747b9a8f9f55840e75693163197baae9d50c32),

[ 291](group__net__if.md#ggadfe9d90f24046cd9bd4bbee096e747b9adb20a95215310c420f8dae7e17a2f367) [NET\_IF\_OPER\_DOWN](group__net__if.md#ggadfe9d90f24046cd9bd4bbee096e747b9adb20a95215310c420f8dae7e17a2f367),

[ 292](group__net__if.md#ggadfe9d90f24046cd9bd4bbee096e747b9ae7e9b8b12ae618a5ee1483dee916aab4) [NET\_IF\_OPER\_LOWERLAYERDOWN](group__net__if.md#ggadfe9d90f24046cd9bd4bbee096e747b9ae7e9b8b12ae618a5ee1483dee916aab4),

[ 293](group__net__if.md#ggadfe9d90f24046cd9bd4bbee096e747b9a2240173b5c247ab5eb0a9a6afafb296f) [NET\_IF\_OPER\_TESTING](group__net__if.md#ggadfe9d90f24046cd9bd4bbee096e747b9a2240173b5c247ab5eb0a9a6afafb296f),

[ 294](group__net__if.md#ggadfe9d90f24046cd9bd4bbee096e747b9a5cbe2aa27a444444d4acf122113d430d) [NET\_IF\_OPER\_DORMANT](group__net__if.md#ggadfe9d90f24046cd9bd4bbee096e747b9a5cbe2aa27a444444d4acf122113d430d),

[ 295](group__net__if.md#ggadfe9d90f24046cd9bd4bbee096e747b9a6b99bfc28d831292029761d74209ee03) [NET\_IF\_OPER\_UP](group__net__if.md#ggadfe9d90f24046cd9bd4bbee096e747b9a6b99bfc28d831292029761d74209ee03),

296} \_\_packed;

297

298#if defined(CONFIG\_NET\_OFFLOAD)

299struct net\_offload;

300#endif /\* CONFIG\_NET\_OFFLOAD \*/

301

303#if defined(CONFIG\_NET\_IPV6)

304#define NET\_IF\_MAX\_IPV6\_ADDR CONFIG\_NET\_IF\_UNICAST\_IPV6\_ADDR\_COUNT

305#define NET\_IF\_MAX\_IPV6\_MADDR CONFIG\_NET\_IF\_MCAST\_IPV6\_ADDR\_COUNT

306#define NET\_IF\_MAX\_IPV6\_PREFIX CONFIG\_NET\_IF\_IPV6\_PREFIX\_COUNT

307#else

308#define NET\_IF\_MAX\_IPV6\_ADDR 0

309#define NET\_IF\_MAX\_IPV6\_MADDR 0

310#define NET\_IF\_MAX\_IPV6\_PREFIX 0

311#endif

312/\* @endcond \*/

313

[ 315](structnet__if__ipv6.md)struct [net\_if\_ipv6](structnet__if__ipv6.md) {

[ 317](structnet__if__ipv6.md#adb6431d336cc3f46972e13d2255452c8) struct [net\_if\_addr](structnet__if__addr.md) [unicast](structnet__if__ipv6.md#adb6431d336cc3f46972e13d2255452c8)[NET\_IF\_MAX\_IPV6\_ADDR];

318

[ 320](structnet__if__ipv6.md#a727d2773e0dee3be687dda5b2dd55682) struct [net\_if\_mcast\_addr](structnet__if__mcast__addr.md) [mcast](structnet__if__ipv6.md#a727d2773e0dee3be687dda5b2dd55682)[NET\_IF\_MAX\_IPV6\_MADDR];

321

[ 323](structnet__if__ipv6.md#a2dccdc984f08527302d8d910a2658f72) struct [net\_if\_ipv6\_prefix](structnet__if__ipv6__prefix.md) [prefix](structnet__if__ipv6.md#a2dccdc984f08527302d8d910a2658f72)[NET\_IF\_MAX\_IPV6\_PREFIX];

324

[ 326](structnet__if__ipv6.md#a500a78fe23ee2ebc63f3d3b53b5b92ea) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [base\_reachable\_time](structnet__if__ipv6.md#a500a78fe23ee2ebc63f3d3b53b5b92ea);

327

[ 329](structnet__if__ipv6.md#af57b7dca189167f8cc757c4ed6b08f2f) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [reachable\_time](structnet__if__ipv6.md#af57b7dca189167f8cc757c4ed6b08f2f);

330

[ 332](structnet__if__ipv6.md#ac5ee47ff9d3e429ecbb8623e5d713246) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [retrans\_timer](structnet__if__ipv6.md#ac5ee47ff9d3e429ecbb8623e5d713246);

333

334#if defined(CONFIG\_NET\_IPV6\_PE)

339 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) desync\_factor;

340#endif /\* CONFIG\_NET\_IPV6\_PE \*/

341

342#if defined(CONFIG\_NET\_IPV6\_ND) && defined(CONFIG\_NET\_NATIVE\_IPV6)

344 [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) rs\_node;

345

346 /\* RS start time \*/

347 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) rs\_start;

348

350 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) rs\_count;

351#endif

352

[ 354](structnet__if__ipv6.md#a71775a082984274fbc7c009ead18e751) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [hop\_limit](structnet__if__ipv6.md#a71775a082984274fbc7c009ead18e751);

355

[ 357](structnet__if__ipv6.md#ae94906c28578f2e1ea2506b0e2972d4c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [mcast\_hop\_limit](structnet__if__ipv6.md#ae94906c28578f2e1ea2506b0e2972d4c);

358};

359

360#if defined(CONFIG\_NET\_DHCPV6) && defined(CONFIG\_NET\_NATIVE\_IPV6)

362struct net\_if\_dhcpv6 {

364 [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) node;

365

367 struct net\_dhcpv6\_duid\_storage clientid;

368

370 struct net\_dhcpv6\_duid\_storage serverid;

371

373 enum net\_dhcpv6\_state [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90);

374

376 struct [net\_dhcpv6\_params](structnet__dhcpv6__params.md) params;

377

379 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) timeout;

380

382 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) exchange\_start;

383

385 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) t1;

386

388 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) t2;

389

393 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) expire;

394

396 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) addr\_iaid;

397

399 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) prefix\_iaid;

400

402 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) retransmit\_timeout;

403

405 [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) server\_preference;

406

408 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) retransmissions;

409

411 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) tid[DHCPV6\_TID\_SIZE];

412

414 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) prefix\_len;

415

417 struct [in6\_addr](structin6__addr.md) prefix;

418

420 struct [in6\_addr](structin6__addr.md) addr;

421};

422#endif /\* defined(CONFIG\_NET\_DHCPV6) && defined(CONFIG\_NET\_NATIVE\_IPV6) \*/

423

425#if defined(CONFIG\_NET\_IPV4)

426#define NET\_IF\_MAX\_IPV4\_ADDR CONFIG\_NET\_IF\_UNICAST\_IPV4\_ADDR\_COUNT

427#define NET\_IF\_MAX\_IPV4\_MADDR CONFIG\_NET\_IF\_MCAST\_IPV4\_ADDR\_COUNT

428#else

429#define NET\_IF\_MAX\_IPV4\_ADDR 0

430#define NET\_IF\_MAX\_IPV4\_MADDR 0

431#endif

433

[ 439](structnet__if__addr__ipv4.md)struct [net\_if\_addr\_ipv4](structnet__if__addr__ipv4.md) {

[ 441](structnet__if__addr__ipv4.md#a9d8924e263cc7401569c934533a04b48) struct [net\_if\_addr](structnet__if__addr.md) [ipv4](structnet__if__addr__ipv4.md#a9d8924e263cc7401569c934533a04b48);

[ 443](structnet__if__addr__ipv4.md#ae1720720e7e36ccf38d0b282d3150774) struct [in\_addr](structin__addr.md) [netmask](structnet__if__addr__ipv4.md#ae1720720e7e36ccf38d0b282d3150774);

444};

445

[ 447](structnet__if__ipv4.md)struct [net\_if\_ipv4](structnet__if__ipv4.md) {

[ 449](structnet__if__ipv4.md#a806cf92123452ed3aa93540803b0a8d3) struct [net\_if\_addr\_ipv4](structnet__if__addr__ipv4.md) [unicast](structnet__if__ipv4.md#a806cf92123452ed3aa93540803b0a8d3)[NET\_IF\_MAX\_IPV4\_ADDR];

450

[ 452](structnet__if__ipv4.md#adfaf5b50255bd35297195a7218729ae7) struct [net\_if\_mcast\_addr](structnet__if__mcast__addr.md) [mcast](structnet__if__ipv4.md#adfaf5b50255bd35297195a7218729ae7)[NET\_IF\_MAX\_IPV4\_MADDR];

453

[ 455](structnet__if__ipv4.md#aa24772c7202bf465ee3da94a172b7bcb) struct [in\_addr](structin__addr.md) [gw](structnet__if__ipv4.md#aa24772c7202bf465ee3da94a172b7bcb);

456

[ 458](structnet__if__ipv4.md#acdc6d5d6eb5362f4f6d2c027cc40e684) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [ttl](structnet__if__ipv4.md#acdc6d5d6eb5362f4f6d2c027cc40e684);

459

[ 461](structnet__if__ipv4.md#a7e9bf16d51989cfcfe564f4f0a43b480) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [mcast\_ttl](structnet__if__ipv4.md#a7e9bf16d51989cfcfe564f4f0a43b480);

462

463#if defined(CONFIG\_NET\_IPV4\_ACD)

465 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) conflict\_cnt;

466#endif

467};

468

469#if defined(CONFIG\_NET\_DHCPV4) && defined(CONFIG\_NET\_NATIVE\_IPV4)

470struct net\_if\_dhcpv4 {

472 [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) node;

473

475 [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) timer\_start;

476

478 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) request\_time;

479

480 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) xid;

481

483 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) lease\_time;

484

486 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) renewal\_time;

487

489 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) rebinding\_time;

490

492 struct [in\_addr](structin__addr.md) server\_id;

493

495 struct [in\_addr](structin__addr.md) requested\_ip;

496

498 struct [in\_addr](structin__addr.md) netmask;

499

504 enum net\_dhcpv4\_state [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90);

505

507 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) attempts;

508

510 struct [in\_addr](structin__addr.md) request\_server\_addr;

511

513 struct [in\_addr](structin__addr.md) response\_src\_addr;

514

515#ifdef CONFIG\_NET\_DHCPV4\_OPTION\_NTP\_SERVER

517 struct [in\_addr](structin__addr.md) ntp\_addr;

518#endif

519};

520#endif /\* CONFIG\_NET\_DHCPV4 \*/

521

522#if defined(CONFIG\_NET\_IPV4\_AUTO) && defined(CONFIG\_NET\_NATIVE\_IPV4)

523struct net\_if\_ipv4\_autoconf {

525 struct net\_if \*iface;

526

528 struct in\_addr requested\_ip;

529

532 enum [net\_ipv4\_autoconf\_state](ipv4__autoconf_8h.md#abdf8bb08f12768aad2ff95b902bdc899) [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90);

533};

534#endif /\* CONFIG\_NET\_IPV4\_AUTO \*/

535

537/\* We always need to have at least one IP config \*/

538#define NET\_IF\_MAX\_CONFIGS 1

540

[ 544](structnet__if__ip.md)struct [net\_if\_ip](structnet__if__ip.md) {

545#if defined(CONFIG\_NET\_IPV6)

546 struct [net\_if\_ipv6](structnet__if__ipv6.md) \*ipv6;

547#endif /\* CONFIG\_NET\_IPV6 \*/

548

549#if defined(CONFIG\_NET\_IPV4)

550 struct [net\_if\_ipv4](structnet__if__ipv4.md) \*ipv4;

551#endif /\* CONFIG\_NET\_IPV4 \*/

552};

553

[ 557](structnet__if__config.md)struct [net\_if\_config](structnet__if__config.md) {

558#if defined(CONFIG\_NET\_IP)

560 struct [net\_if\_ip](structnet__if__ip.md) ip;

561#endif

562

563#if defined(CONFIG\_NET\_DHCPV4) && defined(CONFIG\_NET\_NATIVE\_IPV4)

564 struct net\_if\_dhcpv4 dhcpv4;

565#endif /\* CONFIG\_NET\_DHCPV4 \*/

566

567#if defined(CONFIG\_NET\_DHCPV6) && defined(CONFIG\_NET\_NATIVE\_IPV6)

568 struct net\_if\_dhcpv6 dhcpv6;

569#endif /\* CONFIG\_NET\_DHCPV6 \*/

570

571#if defined(CONFIG\_NET\_IPV4\_AUTO) && defined(CONFIG\_NET\_NATIVE\_IPV4)

572 struct net\_if\_ipv4\_autoconf ipv4auto;

573#endif /\* CONFIG\_NET\_IPV4\_AUTO \*/

574

575#if defined(CONFIG\_NET\_L2\_VIRTUAL)

580 [sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8) virtual\_interfaces;

581#endif /\* CONFIG\_NET\_L2\_VIRTUAL \*/

582

583#if defined(CONFIG\_NET\_INTERFACE\_NAME)

588 char name[CONFIG\_NET\_INTERFACE\_NAME\_LEN + 1];

589#endif

590};

591

[ 601](structnet__traffic__class.md)struct [net\_traffic\_class](structnet__traffic__class.md) {

[ 603](structnet__traffic__class.md#a94511ca12bad1687f5c7ca862c857ded) struct [k\_fifo](structk__fifo.md) [fifo](structnet__traffic__class.md#a94511ca12bad1687f5c7ca862c857ded);

604

[ 606](structnet__traffic__class.md#a8d0023588fee0a8ff1381bbc80ada143) struct [k\_thread](structk__thread.md) [handler](structnet__traffic__class.md#a8d0023588fee0a8ff1381bbc80ada143);

607

[ 609](structnet__traffic__class.md#a2d98bc68d38bdef649d645b8b52516c5) [k\_thread\_stack\_t](arch__interface_8h.md#a9fc2dce533bd7b8cb1fdd4bdbb2b62b1) \*[stack](structnet__traffic__class.md#a2d98bc68d38bdef649d645b8b52516c5);

610};

611

[ 618](group__net__if.md#gaef3dfe26195514aac625e9f22e399759)typedef int (\*[net\_socket\_create\_t](group__net__if.md#gaef3dfe26195514aac625e9f22e399759))(int, int, int);

619

[ 634](structnet__if__dev.md)struct [net\_if\_dev](structnet__if__dev.md) {

[ 636](structnet__if__dev.md#aab633a44f165f571910dc9fc9e131c50) const struct [device](structdevice.md) \*[dev](structnet__if__dev.md#aab633a44f165f571910dc9fc9e131c50);

637

[ 639](structnet__if__dev.md#a85d713c62875f5fe9e3ec29773150797) const struct [net\_l2](structnet__l2.md) \* const [l2](structnet__if__dev.md#a85d713c62875f5fe9e3ec29773150797);

640

[ 642](structnet__if__dev.md#a8fec6a7f612fc1268ef486d8bdebe018) void \*[l2\_data](structnet__if__dev.md#a8fec6a7f612fc1268ef486d8bdebe018);

643

[ 645](structnet__if__dev.md#ac8f9c30e1dea05c28c88d3b367b130f5) [ATOMIC\_DEFINE](group__atomic__apis.md#ga249c575db9764486197709b327f7370e)([flags](structnet__if__dev.md#ac8f9c30e1dea05c28c88d3b367b130f5), NET\_IF\_NUM\_FLAGS);

646

[ 648](structnet__if__dev.md#aac6d5d341ab520e6aac7f7b03737c197) struct [net\_linkaddr](structnet__linkaddr.md) [link\_addr](structnet__if__dev.md#aac6d5d341ab520e6aac7f7b03737c197);

649

650#if defined(CONFIG\_NET\_OFFLOAD)

656 struct net\_offload \*offload;

657#endif /\* CONFIG\_NET\_OFFLOAD \*/

658

[ 660](structnet__if__dev.md#aa15ccca2eb67b8d2afca153ccacb3742) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [mtu](structnet__if__dev.md#aa15ccca2eb67b8d2afca153ccacb3742);

661

662#if defined(CONFIG\_NET\_SOCKETS\_OFFLOAD)

666 [net\_socket\_create\_t](group__net__if.md#gaef3dfe26195514aac625e9f22e399759) socket\_offload;

667#endif /\* CONFIG\_NET\_SOCKETS\_OFFLOAD \*/

668

[ 670](structnet__if__dev.md#a30eabb2ffae082d0de81a50c510738a3) enum [net\_if\_oper\_state](group__net__if.md#gadfe9d90f24046cd9bd4bbee096e747b9) [oper\_state](structnet__if__dev.md#a30eabb2ffae082d0de81a50c510738a3);

671};

672

[ 680](structnet__if.md)struct [net\_if](structnet__if.md) {

[ 682](structnet__if.md#a0982ba2019cdaa7701162e60fdb2171e) struct [net\_if\_dev](structnet__if__dev.md) \*[if\_dev](structnet__if.md#a0982ba2019cdaa7701162e60fdb2171e);

683

684#if defined(CONFIG\_NET\_STATISTICS\_PER\_INTERFACE)

686 struct [net\_stats](structnet__stats.md) stats;

687#endif /\* CONFIG\_NET\_STATISTICS\_PER\_INTERFACE \*/

688

[ 690](structnet__if.md#a5e71962f55bdead7bfbbb96518c6c404) struct [net\_if\_config](structnet__if__config.md) [config](structnet__if.md#a5e71962f55bdead7bfbbb96518c6c404);

691

692#if defined(CONFIG\_NET\_POWER\_MANAGEMENT)

697 int tx\_pending;

698#endif

699

[ 701](structnet__if.md#ace2233b71da53ff0fc7cd564ccfc5a03) struct [k\_mutex](structk__mutex.md) [lock](structnet__if.md#ace2233b71da53ff0fc7cd564ccfc5a03);

702

[ 704](structnet__if.md#af00f729ebddfdcf725169f61b6cd586b) struct [k\_mutex](structk__mutex.md) [tx\_lock](structnet__if.md#af00f729ebddfdcf725169f61b6cd586b);

705

[ 710](structnet__if.md#aa96a6a2d55f6a4ece2f340eef526ef56) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [pe\_enabled](structnet__if.md#aa96a6a2d55f6a4ece2f340eef526ef56) : 1;

711

[ 715](structnet__if.md#aec585e283c9053443ff05b364acf76eb) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [pe\_prefer\_public](structnet__if.md#aec585e283c9053443ff05b364acf76eb) : 1;

716

718 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \_unused : 6;

719};

720

722

723static inline void net\_if\_lock(struct [net\_if](structnet__if.md) \*iface)

724{

725 NET\_ASSERT(iface);

726

727 (void)[k\_mutex\_lock](group__mutex__apis.md#ga850549358645249c285669baa49c33b0)(&iface->[lock](structnet__if.md#ace2233b71da53ff0fc7cd564ccfc5a03), [K\_FOREVER](group__clock__apis.md#ga0bb4b83f0222193b21a8910311bab0ca));

728}

729

730static inline void net\_if\_unlock(struct [net\_if](structnet__if.md) \*iface)

731{

732 NET\_ASSERT(iface);

733

734 [k\_mutex\_unlock](group__mutex__apis.md#ga360f4c0e7258b0d7030cdb1f452b2c31)(&iface->[lock](structnet__if.md#ace2233b71da53ff0fc7cd564ccfc5a03));

735}

736

737static inline bool [net\_if\_flag\_is\_set](group__net__if.md#gae1f373ddd61c18a81481d8ddcfb12543)(struct [net\_if](structnet__if.md) \*iface,

738 enum [net\_if\_flag](group__net__if.md#gae691e5537917ffce27ad0db82c730371) value);

739

740static inline void net\_if\_tx\_lock(struct [net\_if](structnet__if.md) \*iface)

741{

742 NET\_ASSERT(iface);

743

744 if ([net\_if\_flag\_is\_set](group__net__if.md#gae1f373ddd61c18a81481d8ddcfb12543)(iface, [NET\_IF\_NO\_TX\_LOCK](group__net__if.md#ggae691e5537917ffce27ad0db82c730371ae8d564e1577c8daad8ce50a729c500c9))) {

745 return;

746 }

747

748 (void)[k\_mutex\_lock](group__mutex__apis.md#ga850549358645249c285669baa49c33b0)(&iface->[tx\_lock](structnet__if.md#af00f729ebddfdcf725169f61b6cd586b), [K\_FOREVER](group__clock__apis.md#ga0bb4b83f0222193b21a8910311bab0ca));

749}

750

751static inline void net\_if\_tx\_unlock(struct [net\_if](structnet__if.md) \*iface)

752{

753 NET\_ASSERT(iface);

754

755 if ([net\_if\_flag\_is\_set](group__net__if.md#gae1f373ddd61c18a81481d8ddcfb12543)(iface, [NET\_IF\_NO\_TX\_LOCK](group__net__if.md#ggae691e5537917ffce27ad0db82c730371ae8d564e1577c8daad8ce50a729c500c9))) {

756 return;

757 }

758

759 [k\_mutex\_unlock](group__mutex__apis.md#ga360f4c0e7258b0d7030cdb1f452b2c31)(&iface->[tx\_lock](structnet__if.md#af00f729ebddfdcf725169f61b6cd586b));

760}

761

763

[ 770](group__net__if.md#ga52f9fca13e9f836799e0e40f581744d2)static inline void [net\_if\_flag\_set](group__net__if.md#ga52f9fca13e9f836799e0e40f581744d2)(struct [net\_if](structnet__if.md) \*iface,

771 enum [net\_if\_flag](group__net__if.md#gae691e5537917ffce27ad0db82c730371) value)

772{

773 NET\_ASSERT(iface);

774 NET\_ASSERT(iface->[if\_dev](structnet__if.md#a0982ba2019cdaa7701162e60fdb2171e));

775

776 [atomic\_set\_bit](group__atomic__apis.md#ga17a3961ba7610ad6e595e602f70344a0)(iface->[if\_dev](structnet__if.md#a0982ba2019cdaa7701162e60fdb2171e)->[flags](structnet__if__dev.md#ac8f9c30e1dea05c28c88d3b367b130f5), value);

777}

778

[ 787](group__net__if.md#ga42e7482191a92007960601f8bb621dca)static inline bool [net\_if\_flag\_test\_and\_set](group__net__if.md#ga42e7482191a92007960601f8bb621dca)(struct [net\_if](structnet__if.md) \*iface,

788 enum [net\_if\_flag](group__net__if.md#gae691e5537917ffce27ad0db82c730371) value)

789{

790 NET\_ASSERT(iface);

791 NET\_ASSERT(iface->[if\_dev](structnet__if.md#a0982ba2019cdaa7701162e60fdb2171e));

792

793 return [atomic\_test\_and\_set\_bit](group__atomic__apis.md#ga7ff45e13aa5f8be5d7a550e49f5c720b)(iface->[if\_dev](structnet__if.md#a0982ba2019cdaa7701162e60fdb2171e)->[flags](structnet__if__dev.md#ac8f9c30e1dea05c28c88d3b367b130f5), value);

794}

795

[ 802](group__net__if.md#gaff751b6a92b0c608ecfc50e8c0587fd3)static inline void [net\_if\_flag\_clear](group__net__if.md#gaff751b6a92b0c608ecfc50e8c0587fd3)(struct [net\_if](structnet__if.md) \*iface,

803 enum [net\_if\_flag](group__net__if.md#gae691e5537917ffce27ad0db82c730371) value)

804{

805 NET\_ASSERT(iface);

806 NET\_ASSERT(iface->[if\_dev](structnet__if.md#a0982ba2019cdaa7701162e60fdb2171e));

807

808 [atomic\_clear\_bit](group__atomic__apis.md#ga1c1693d524c49d11fd32b323a39d718e)(iface->[if\_dev](structnet__if.md#a0982ba2019cdaa7701162e60fdb2171e)->[flags](structnet__if__dev.md#ac8f9c30e1dea05c28c88d3b367b130f5), value);

809}

810

[ 819](group__net__if.md#gab8f371c7f8890cf4728177f6595141d7)static inline bool [net\_if\_flag\_test\_and\_clear](group__net__if.md#gab8f371c7f8890cf4728177f6595141d7)(struct [net\_if](structnet__if.md) \*iface,

820 enum [net\_if\_flag](group__net__if.md#gae691e5537917ffce27ad0db82c730371) value)

821{

822 NET\_ASSERT(iface);

823 NET\_ASSERT(iface->[if\_dev](structnet__if.md#a0982ba2019cdaa7701162e60fdb2171e));

824

825 return [atomic\_test\_and\_clear\_bit](group__atomic__apis.md#ga53159437721084da0ec8ee70ec212472)(iface->[if\_dev](structnet__if.md#a0982ba2019cdaa7701162e60fdb2171e)->[flags](structnet__if__dev.md#ac8f9c30e1dea05c28c88d3b367b130f5), value);

826}

827

[ 836](group__net__if.md#gae1f373ddd61c18a81481d8ddcfb12543)static inline bool [net\_if\_flag\_is\_set](group__net__if.md#gae1f373ddd61c18a81481d8ddcfb12543)(struct [net\_if](structnet__if.md) \*iface,

837 enum [net\_if\_flag](group__net__if.md#gae691e5537917ffce27ad0db82c730371) value)

838{

839 NET\_ASSERT(iface);

840 NET\_ASSERT(iface->[if\_dev](structnet__if.md#a0982ba2019cdaa7701162e60fdb2171e));

841

842 if (iface == NULL) {

843 return false;

844 }

845

846 return [atomic\_test\_bit](group__atomic__apis.md#ga190ddc108f45e7649689753c08658eae)(iface->[if\_dev](structnet__if.md#a0982ba2019cdaa7701162e60fdb2171e)->[flags](structnet__if__dev.md#ac8f9c30e1dea05c28c88d3b367b130f5), value);

847}

848

[ 857](group__net__if.md#ga1f1bf845e63cce02e2183889cc85d57e)static inline enum [net\_if\_oper\_state](group__net__if.md#gadfe9d90f24046cd9bd4bbee096e747b9) [net\_if\_oper\_state\_set](group__net__if.md#ga1f1bf845e63cce02e2183889cc85d57e)(

858 struct [net\_if](structnet__if.md) \*iface, enum [net\_if\_oper\_state](group__net__if.md#gadfe9d90f24046cd9bd4bbee096e747b9) oper\_state)

859{

860 NET\_ASSERT(iface);

861 NET\_ASSERT(iface->[if\_dev](structnet__if.md#a0982ba2019cdaa7701162e60fdb2171e));

862

863 BUILD\_ASSERT((enum [net\_if\_oper\_state](group__net__if.md#gadfe9d90f24046cd9bd4bbee096e747b9))(-1) > 0 && [NET\_IF\_OPER\_UNKNOWN](group__net__if.md#ggadfe9d90f24046cd9bd4bbee096e747b9ac7cae092ea6ceeb62499a9b435ac4b58) == 0);

864 if (oper\_state <= [NET\_IF\_OPER\_UP](group__net__if.md#ggadfe9d90f24046cd9bd4bbee096e747b9a6b99bfc28d831292029761d74209ee03)) {

865 iface->[if\_dev](structnet__if.md#a0982ba2019cdaa7701162e60fdb2171e)->[oper\_state](structnet__if__dev.md#a30eabb2ffae082d0de81a50c510738a3) = oper\_state;

866 }

867

868 return iface->[if\_dev](structnet__if.md#a0982ba2019cdaa7701162e60fdb2171e)->[oper\_state](structnet__if__dev.md#a30eabb2ffae082d0de81a50c510738a3);

869}

870

[ 878](group__net__if.md#gad9e957a4866b4566296ee39392fde0e4)static inline enum [net\_if\_oper\_state](group__net__if.md#gadfe9d90f24046cd9bd4bbee096e747b9) [net\_if\_oper\_state](group__net__if.md#gadfe9d90f24046cd9bd4bbee096e747b9)(struct [net\_if](structnet__if.md) \*iface)

879{

880 NET\_ASSERT(iface);

881 NET\_ASSERT(iface->[if\_dev](structnet__if.md#a0982ba2019cdaa7701162e60fdb2171e));

882

883 return iface->[if\_dev](structnet__if.md#a0982ba2019cdaa7701162e60fdb2171e)->[oper\_state](structnet__if__dev.md#a30eabb2ffae082d0de81a50c510738a3);

884}

885

[ 894](group__net__if.md#gada0398d757eab28d16a129692c309f4d)enum [net\_verdict](group__net__core.md#ga8e5393f3bdd85491f221324e637c3896) [net\_if\_send\_data](group__net__if.md#gada0398d757eab28d16a129692c309f4d)(struct [net\_if](structnet__if.md) \*iface, struct [net\_pkt](structnet__pkt.md) \*pkt);

895

[ 903](group__net__if.md#gafa451f6118529d1d084704d00b2aae20)static inline const struct [net\_l2](structnet__l2.md) \*[net\_if\_l2](group__net__if.md#gafa451f6118529d1d084704d00b2aae20)(struct [net\_if](structnet__if.md) \*iface)

904{

905 if (!iface || !iface->[if\_dev](structnet__if.md#a0982ba2019cdaa7701162e60fdb2171e)) {

906 return NULL;

907 }

908

909 return iface->[if\_dev](structnet__if.md#a0982ba2019cdaa7701162e60fdb2171e)->[l2](structnet__if__dev.md#a85d713c62875f5fe9e3ec29773150797);

910}

911

[ 920](group__net__if.md#ga72ed21ca0cb220199f5a2070137c7fef)enum [net\_verdict](group__net__core.md#ga8e5393f3bdd85491f221324e637c3896) [net\_if\_recv\_data](group__net__if.md#ga72ed21ca0cb220199f5a2070137c7fef)(struct [net\_if](structnet__if.md) \*iface, struct [net\_pkt](structnet__pkt.md) \*pkt);

921

[ 929](group__net__if.md#ga3cad2d51fc9cc225619585e06e252db0)static inline void \*[net\_if\_l2\_data](group__net__if.md#ga3cad2d51fc9cc225619585e06e252db0)(struct [net\_if](structnet__if.md) \*iface)

930{

931 NET\_ASSERT(iface);

932 NET\_ASSERT(iface->[if\_dev](structnet__if.md#a0982ba2019cdaa7701162e60fdb2171e));

933

934 return iface->[if\_dev](structnet__if.md#a0982ba2019cdaa7701162e60fdb2171e)->[l2\_data](structnet__if__dev.md#a8fec6a7f612fc1268ef486d8bdebe018);

935}

936

[ 944](group__net__if.md#gaeb8c703f273bc07ae9bb7a0d8bfe6f3d)static inline const struct [device](structdevice.md) \*[net\_if\_get\_device](group__net__if.md#gaeb8c703f273bc07ae9bb7a0d8bfe6f3d)(struct [net\_if](structnet__if.md) \*iface)

945{

946 NET\_ASSERT(iface);

947 NET\_ASSERT(iface->[if\_dev](structnet__if.md#a0982ba2019cdaa7701162e60fdb2171e));

948

949 return iface->[if\_dev](structnet__if.md#a0982ba2019cdaa7701162e60fdb2171e)->[dev](structnet__if__dev.md#aab633a44f165f571910dc9fc9e131c50);

950}

951

[ 958](group__net__if.md#ga56c4d37edcea540be09ebcdf97265aed)void [net\_if\_queue\_tx](group__net__if.md#ga56c4d37edcea540be09ebcdf97265aed)(struct [net\_if](structnet__if.md) \*iface, struct [net\_pkt](structnet__pkt.md) \*pkt);

959

[ 967](group__net__if.md#ga6bfa5f84a2127bbad27a0a3b319526a1)static inline bool [net\_if\_is\_ip\_offloaded](group__net__if.md#ga6bfa5f84a2127bbad27a0a3b319526a1)(struct [net\_if](structnet__if.md) \*iface)

968{

969#if defined(CONFIG\_NET\_OFFLOAD)

970 return (iface != NULL && iface->[if\_dev](structnet__if.md#a0982ba2019cdaa7701162e60fdb2171e) != NULL &&

971 iface->[if\_dev](structnet__if.md#a0982ba2019cdaa7701162e60fdb2171e)->offload != NULL);

972#else

973 ARG\_UNUSED(iface);

974

975 return false;

976#endif

977}

978

[ 986](group__net__if.md#gaecedc93a6dab2c57fe686718ea4d78af)bool [net\_if\_is\_offloaded](group__net__if.md#gaecedc93a6dab2c57fe686718ea4d78af)(struct [net\_if](structnet__if.md) \*iface);

987

[ 995](group__net__if.md#ga520939e94620ca75475a71f153df6d4a)static inline struct net\_offload \*[net\_if\_offload](group__net__if.md#ga520939e94620ca75475a71f153df6d4a)(struct [net\_if](structnet__if.md) \*iface)

996{

997#if defined(CONFIG\_NET\_OFFLOAD)

998 NET\_ASSERT(iface);

999 NET\_ASSERT(iface->[if\_dev](structnet__if.md#a0982ba2019cdaa7701162e60fdb2171e));

1000

1001 return iface->[if\_dev](structnet__if.md#a0982ba2019cdaa7701162e60fdb2171e)->offload;

1002#else

1003 ARG\_UNUSED(iface);

1004

1005 return NULL;

1006#endif

1007}

1008

[ 1016](group__net__if.md#gaf308baf2241fa455b50b439b7fab3f1e)static inline bool [net\_if\_is\_socket\_offloaded](group__net__if.md#gaf308baf2241fa455b50b439b7fab3f1e)(struct [net\_if](structnet__if.md) \*iface)

1017{

1018#if defined(CONFIG\_NET\_SOCKETS\_OFFLOAD)

1019 NET\_ASSERT(iface);

1020 NET\_ASSERT(iface->[if\_dev](structnet__if.md#a0982ba2019cdaa7701162e60fdb2171e));

1021

1022 return (iface->[if\_dev](structnet__if.md#a0982ba2019cdaa7701162e60fdb2171e)->socket\_offload != NULL);

1023#else

1024 ARG\_UNUSED(iface);

1025

1026 return false;

1027#endif

1028}

1029

[ 1036](group__net__if.md#ga9db52875580115c743b1f35cd6c46796)static inline void [net\_if\_socket\_offload\_set](group__net__if.md#ga9db52875580115c743b1f35cd6c46796)(

1037 struct [net\_if](structnet__if.md) \*iface, [net\_socket\_create\_t](group__net__if.md#gaef3dfe26195514aac625e9f22e399759) socket\_offload)

1038{

1039#if defined(CONFIG\_NET\_SOCKETS\_OFFLOAD)

1040 NET\_ASSERT(iface);

1041 NET\_ASSERT(iface->[if\_dev](structnet__if.md#a0982ba2019cdaa7701162e60fdb2171e));

1042

1043 iface->[if\_dev](structnet__if.md#a0982ba2019cdaa7701162e60fdb2171e)->socket\_offload = socket\_offload;

1044#else

1045 ARG\_UNUSED(iface);

1046 ARG\_UNUSED(socket\_offload);

1047#endif

1048}

1049

[ 1057](group__net__if.md#gafb2bbaec96c4759d920b2866c0b3ef3a)static inline [net\_socket\_create\_t](group__net__if.md#gaef3dfe26195514aac625e9f22e399759) [net\_if\_socket\_offload](group__net__if.md#gafb2bbaec96c4759d920b2866c0b3ef3a)(struct [net\_if](structnet__if.md) \*iface)

1058{

1059#if defined(CONFIG\_NET\_SOCKETS\_OFFLOAD)

1060 NET\_ASSERT(iface);

1061 NET\_ASSERT(iface->[if\_dev](structnet__if.md#a0982ba2019cdaa7701162e60fdb2171e));

1062

1063 return iface->[if\_dev](structnet__if.md#a0982ba2019cdaa7701162e60fdb2171e)->socket\_offload;

1064#else

1065 ARG\_UNUSED(iface);

1066

1067 return NULL;

1068#endif

1069}

1070

[ 1078](group__net__if.md#ga467186e964bf721e14fed38392f21872)static inline struct [net\_linkaddr](structnet__linkaddr.md) \*[net\_if\_get\_link\_addr](group__net__if.md#ga467186e964bf721e14fed38392f21872)(struct [net\_if](structnet__if.md) \*iface)

1079{

1080 NET\_ASSERT(iface);

1081 NET\_ASSERT(iface->[if\_dev](structnet__if.md#a0982ba2019cdaa7701162e60fdb2171e));

1082

1083 return &iface->[if\_dev](structnet__if.md#a0982ba2019cdaa7701162e60fdb2171e)->[link\_addr](structnet__if__dev.md#aac6d5d341ab520e6aac7f7b03737c197);

1084}

1085

[ 1093](group__net__if.md#gae271e0e4dcb031a83d9908e597a45048)static inline struct [net\_if\_config](structnet__if__config.md) \*[net\_if\_get\_config](group__net__if.md#gae271e0e4dcb031a83d9908e597a45048)(struct [net\_if](structnet__if.md) \*iface)

1094{

1095 NET\_ASSERT(iface);

1096

1097 return &iface->[config](structnet__if.md#a5e71962f55bdead7bfbbb96518c6c404);

1098}

1099

1105#if defined(CONFIG\_NET\_IPV6\_DAD) && defined(CONFIG\_NET\_NATIVE\_IPV6)

1106void [net\_if\_start\_dad](group__net__if.md#ga9655c010ccbf989e9328271f5dbcc685)(struct [net\_if](structnet__if.md) \*iface);

1107#else

[ 1108](group__net__if.md#ga9655c010ccbf989e9328271f5dbcc685)static inline void [net\_if\_start\_dad](group__net__if.md#ga9655c010ccbf989e9328271f5dbcc685)(struct [net\_if](structnet__if.md) \*iface)

1109{

1110 ARG\_UNUSED(iface);

1111}

1112#endif

1113

[ 1119](group__net__if.md#gab9bdb7f8a9eeed4d9b70965b8af82cb7)void [net\_if\_start\_rs](group__net__if.md#gab9bdb7f8a9eeed4d9b70965b8af82cb7)(struct [net\_if](structnet__if.md) \*iface);

1120

1121

1127#if defined(CONFIG\_NET\_IPV6\_ND) && defined(CONFIG\_NET\_NATIVE\_IPV6)

1128void [net\_if\_stop\_rs](group__net__if.md#gab0195bb2151a1ba722a0b11d81066988)(struct [net\_if](structnet__if.md) \*iface);

1129#else

[ 1130](group__net__if.md#gab0195bb2151a1ba722a0b11d81066988)static inline void [net\_if\_stop\_rs](group__net__if.md#gab0195bb2151a1ba722a0b11d81066988)(struct [net\_if](structnet__if.md) \*iface)

1131{

1132 ARG\_UNUSED(iface);

1133}

1134#endif /\* CONFIG\_NET\_IPV6\_ND \*/

1135

1148#if defined(CONFIG\_NET\_IPV6\_ND) && defined(CONFIG\_NET\_NATIVE\_IPV6)

1149void [net\_if\_nbr\_reachability\_hint](group__net__if.md#ga51af469ff3d7d9f760d63a8a9c7be8b5)(struct [net\_if](structnet__if.md) \*iface, const struct [in6\_addr](structin6__addr.md) \*ipv6\_addr);

1150#else

[ 1151](group__net__if.md#ga51af469ff3d7d9f760d63a8a9c7be8b5)static inline void [net\_if\_nbr\_reachability\_hint](group__net__if.md#ga51af469ff3d7d9f760d63a8a9c7be8b5)(struct [net\_if](structnet__if.md) \*iface,

1152 const struct [in6\_addr](structin6__addr.md) \*ipv6\_addr)

1153{

1154 ARG\_UNUSED(iface);

1155 ARG\_UNUSED(ipv6\_addr);

1156}

1157#endif

1158

1160

1161static inline int net\_if\_set\_link\_addr\_unlocked(struct [net\_if](structnet__if.md) \*iface,

1162 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) len,

1163 enum [net\_link\_type](group__net__linkaddr.md#ga1312c2322bc4a4f1c3b76d6466806b24) type)

1164{

1165 if ([net\_if\_flag\_is\_set](group__net__if.md#gae1f373ddd61c18a81481d8ddcfb12543)(iface, [NET\_IF\_RUNNING](group__net__if.md#ggae691e5537917ffce27ad0db82c730371add3e2ecdcd5de3154f9bd2836428a25a))) {

1166 return -[EPERM](group__system__errno.md#gadd669d31505a077f769cff8e66c780b3);

1167 }

1168

1169 [net\_if\_get\_link\_addr](group__net__if.md#ga467186e964bf721e14fed38392f21872)(iface)->[addr](structnet__linkaddr.md#a2176a9f7a444ac3b0108102d8cf852f0) = addr;

1170 [net\_if\_get\_link\_addr](group__net__if.md#ga467186e964bf721e14fed38392f21872)(iface)->[len](structnet__linkaddr.md#a7b2f8ebe68b557eb9cbb4c2f2ecd70e0) = len;

1171 [net\_if\_get\_link\_addr](group__net__if.md#ga467186e964bf721e14fed38392f21872)(iface)->[type](structnet__linkaddr.md#a5f5b4c3d353261d0fab8011aa09f00d7) = type;

1172

1173 [net\_hostname\_set\_postfix](group__net__hostname.md#ga6aa3799b3b0d7eec7fb8b276485ae2c5)(addr, len);

1174

1175 return 0;

1176}

1177

1178int net\_if\_set\_link\_addr\_locked(struct [net\_if](structnet__if.md) \*iface,

1179 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) len,

1180 enum [net\_link\_type](group__net__linkaddr.md#ga1312c2322bc4a4f1c3b76d6466806b24) type);

1181

1182#if CONFIG\_NET\_IF\_LOG\_LEVEL >= LOG\_LEVEL\_DBG

1183extern int net\_if\_addr\_unref\_debug(struct [net\_if](structnet__if.md) \*iface,

1184 [sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda) family,

1185 const void \*addr,

1186 const char \*caller, int line);

1187#define net\_if\_addr\_unref(iface, family, addr) \

1188 net\_if\_addr\_unref\_debug(iface, family, addr, \_\_func\_\_, \_\_LINE\_\_)

1189

1190extern struct [net\_if\_addr](structnet__if__addr.md) \*net\_if\_addr\_ref\_debug(struct [net\_if](structnet__if.md) \*iface,

1191 [sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda) family,

1192 const void \*addr,

1193 const char \*caller,

1194 int line);

1195#define net\_if\_addr\_ref(iface, family, addr) \

1196 net\_if\_addr\_ref\_debug(iface, family, addr, \_\_func\_\_, \_\_LINE\_\_)

1197#else

1198extern int net\_if\_addr\_unref(struct [net\_if](structnet__if.md) \*iface,

1199 [sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda) family,

1200 const void \*addr);

1201extern struct [net\_if\_addr](structnet__if__addr.md) \*net\_if\_addr\_ref(struct [net\_if](structnet__if.md) \*iface,

1202 [sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda) family,

1203 const void \*addr);

1204#endif /\* CONFIG\_NET\_IF\_LOG\_LEVEL \*/

1205

1207

[ 1219](group__net__if.md#ga52b41b2f8b7d3405338a0539542677a0)static inline int [net\_if\_set\_link\_addr](group__net__if.md#ga52b41b2f8b7d3405338a0539542677a0)(struct [net\_if](structnet__if.md) \*iface,

1220 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) len,

1221 enum [net\_link\_type](group__net__linkaddr.md#ga1312c2322bc4a4f1c3b76d6466806b24) type)

1222{

1223#if defined(CONFIG\_NET\_RAW\_MODE)

1224 return net\_if\_set\_link\_addr\_unlocked(iface, addr, len, type);

1225#else

1226 return net\_if\_set\_link\_addr\_locked(iface, addr, len, type);

1227#endif

1228}

1229

[ 1237](group__net__if.md#gacddc98531c5748db5a34f5c3a3e96e86)static inline [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [net\_if\_get\_mtu](group__net__if.md#gacddc98531c5748db5a34f5c3a3e96e86)(struct [net\_if](structnet__if.md) \*iface)

1238{

1239 if (iface == NULL) {

1240 return 0U;

1241 }

1242

1243 NET\_ASSERT(iface->[if\_dev](structnet__if.md#a0982ba2019cdaa7701162e60fdb2171e));

1244

1245 return iface->[if\_dev](structnet__if.md#a0982ba2019cdaa7701162e60fdb2171e)->[mtu](structnet__if__dev.md#aa15ccca2eb67b8d2afca153ccacb3742);

1246}

1247

[ 1254](group__net__if.md#ga76b140c6fc39b94ff4102e08e3a58e81)static inline void [net\_if\_set\_mtu](group__net__if.md#ga76b140c6fc39b94ff4102e08e3a58e81)(struct [net\_if](structnet__if.md) \*iface,

1255 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mtu)

1256{

1257 if (iface == NULL) {

1258 return;

1259 }

1260

1261 NET\_ASSERT(iface->[if\_dev](structnet__if.md#a0982ba2019cdaa7701162e60fdb2171e));

1262

1263 iface->[if\_dev](structnet__if.md#a0982ba2019cdaa7701162e60fdb2171e)->[mtu](structnet__if__dev.md#aa15ccca2eb67b8d2afca153ccacb3742) = mtu;

1264}

1265

[ 1272](group__net__if.md#gae66f6e7bd31545e6161fcd4600fe5842)static inline void [net\_if\_addr\_set\_lf](group__net__if.md#gae66f6e7bd31545e6161fcd4600fe5842)(struct [net\_if\_addr](structnet__if__addr.md) \*ifaddr,

1273 bool [is\_infinite](structnet__if__addr.md#a6e799428eb0633a25e4dc3c55e3a3b8c))

1274{

1275 NET\_ASSERT(ifaddr);

1276

1277 ifaddr->[is\_infinite](structnet__if__addr.md#a6e799428eb0633a25e4dc3c55e3a3b8c) = [is\_infinite](structnet__if__addr.md#a6e799428eb0633a25e4dc3c55e3a3b8c);

1278}

1279

[ 1287](group__net__if.md#ga1b058361dc9bcac7d842bb49846a0c79)struct [net\_if](structnet__if.md) \*[net\_if\_get\_by\_link\_addr](group__net__if.md#ga1b058361dc9bcac7d842bb49846a0c79)(struct [net\_linkaddr](structnet__linkaddr.md) \*ll\_addr);

1288

[ 1296](group__net__if.md#gadbb8be32caa896bdcdeee19425134827)struct [net\_if](structnet__if.md) \*[net\_if\_lookup\_by\_dev](group__net__if.md#gadbb8be32caa896bdcdeee19425134827)(const struct [device](structdevice.md) \*dev);

1297

[ 1305](group__net__if.md#gae2323a72714e29836d8296dfc330f7fd)static inline struct [net\_if\_config](structnet__if__config.md) \*[net\_if\_config\_get](group__net__if.md#gae2323a72714e29836d8296dfc330f7fd)(struct [net\_if](structnet__if.md) \*iface)

1306{

1307 NET\_ASSERT(iface);

1308

1309 return &iface->[config](structnet__if.md#a5e71962f55bdead7bfbbb96518c6c404);

1310}

1311

[ 1317](group__net__if.md#gadc87242eb7205362a308b3c4437bf76d)void [net\_if\_router\_rm](group__net__if.md#gadc87242eb7205362a308b3c4437bf76d)(struct [net\_if\_router](structnet__if__router.md) \*router);

1318

[ 1324](group__net__if.md#ga0a1f27ec893e1af3c97f130be4616589)void [net\_if\_set\_default](group__net__if.md#ga0a1f27ec893e1af3c97f130be4616589)(struct [net\_if](structnet__if.md) \*iface);

1325

[ 1331](group__net__if.md#ga55214771e462cbd4930ffa738813cb87)struct [net\_if](structnet__if.md) \*[net\_if\_get\_default](group__net__if.md#ga55214771e462cbd4930ffa738813cb87)(void);

1332

[ 1341](group__net__if.md#ga762337e8b66874a0fbf59bdbeba173f5)struct [net\_if](structnet__if.md) \*[net\_if\_get\_first\_by\_type](group__net__if.md#ga762337e8b66874a0fbf59bdbeba173f5)(const struct [net\_l2](structnet__l2.md) \*l2);

1342

[ 1349](group__net__if.md#ga03d8c6aebb1412382a9eec636c227238)struct [net\_if](structnet__if.md) \*[net\_if\_get\_first\_up](group__net__if.md#ga03d8c6aebb1412382a9eec636c227238)(void);

1350

1351#if defined(CONFIG\_NET\_L2\_IEEE802154)

1358static inline struct [net\_if](structnet__if.md) \*net\_if\_get\_ieee802154(void)

1359{

1360 return [net\_if\_get\_first\_by\_type](group__net__if.md#ga762337e8b66874a0fbf59bdbeba173f5)(&NET\_L2\_GET\_NAME(IEEE802154));

1361}

1362#endif /\* CONFIG\_NET\_L2\_IEEE802154 \*/

1363

[ 1374](group__net__if.md#ga56c9aef19bc9827d9ec96c00e10840fa)int [net\_if\_config\_ipv6\_get](group__net__if.md#ga56c9aef19bc9827d9ec96c00e10840fa)(struct [net\_if](structnet__if.md) \*iface,

1375 struct [net\_if\_ipv6](structnet__if__ipv6.md) \*\*ipv6);

1376

[ 1384](group__net__if.md#ga8af1400b354c42a64795cdb1a600ddd6)int [net\_if\_config\_ipv6\_put](group__net__if.md#ga8af1400b354c42a64795cdb1a600ddd6)(struct [net\_if](structnet__if.md) \*iface);

1385

[ 1394](group__net__if.md#ga13b5a26fc672d15697f99e85543184bb)struct [net\_if\_addr](structnet__if__addr.md) \*[net\_if\_ipv6\_addr\_lookup](group__net__if.md#ga13b5a26fc672d15697f99e85543184bb)(const struct [in6\_addr](structin6__addr.md) \*addr,

1395 struct [net\_if](structnet__if.md) \*\*iface);

1396

[ 1405](group__net__if.md#gab53eabb540a4487d83f27c8e319c736a)struct [net\_if\_addr](structnet__if__addr.md) \*[net\_if\_ipv6\_addr\_lookup\_by\_iface](group__net__if.md#gab53eabb540a4487d83f27c8e319c736a)(struct [net\_if](structnet__if.md) \*iface,

1406 struct [in6\_addr](structin6__addr.md) \*addr);

1407

[ 1416](group__net__if.md#ga1527872e5285790d50028a183608ac02)\_\_syscall int [net\_if\_ipv6\_addr\_lookup\_by\_index](group__net__if.md#ga1527872e5285790d50028a183608ac02)(const struct [in6\_addr](structin6__addr.md) \*addr);

1417

[ 1428](group__net__if.md#gae00484a7fe32671a4ca04ff525e640c6)struct [net\_if\_addr](structnet__if__addr.md) \*[net\_if\_ipv6\_addr\_add](group__net__if.md#gae00484a7fe32671a4ca04ff525e640c6)(struct [net\_if](structnet__if.md) \*iface,

1429 struct [in6\_addr](structin6__addr.md) \*addr,

1430 enum [net\_addr\_type](group__ip__4__6.md#gafecee2d4a331dc85ad962b81a6303e41) [addr\_type](structnet__if__addr.md#ab4fd41001cc24615803bfabb9d48e7eb),

1431 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) vlifetime);

1432

[ 1443](group__net__if.md#ga980bffb649ed48775bdc6cb2a0caef15)\_\_syscall bool [net\_if\_ipv6\_addr\_add\_by\_index](group__net__if.md#ga980bffb649ed48775bdc6cb2a0caef15)(int index,

1444 struct [in6\_addr](structin6__addr.md) \*addr,

1445 enum [net\_addr\_type](group__ip__4__6.md#gafecee2d4a331dc85ad962b81a6303e41) [addr\_type](structnet__if__addr.md#ab4fd41001cc24615803bfabb9d48e7eb),

1446 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) vlifetime);

1447

[ 1454](group__net__if.md#gaef8a6752a201f81636c4ffc1ebba4a25)void [net\_if\_ipv6\_addr\_update\_lifetime](group__net__if.md#gaef8a6752a201f81636c4ffc1ebba4a25)(struct [net\_if\_addr](structnet__if__addr.md) \*ifaddr,

1455 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) vlifetime);

1456

[ 1465](group__net__if.md#ga614e1458fa28d26c26f447e9fbcc2cb7)bool [net\_if\_ipv6\_addr\_rm](group__net__if.md#ga614e1458fa28d26c26f447e9fbcc2cb7)(struct [net\_if](structnet__if.md) \*iface, const struct [in6\_addr](structin6__addr.md) \*addr);

1466

[ 1475](group__net__if.md#gac159e3b0fbf558d5fb09774141da7d6d)\_\_syscall bool [net\_if\_ipv6\_addr\_rm\_by\_index](group__net__if.md#gac159e3b0fbf558d5fb09774141da7d6d)(int index,

1476 const struct [in6\_addr](structin6__addr.md) \*addr);

1477

[ 1486](group__net__if.md#gab58d8561a4f21899e2db34043d346516)typedef void (\*[net\_if\_ip\_addr\_cb\_t](group__net__if.md#gab58d8561a4f21899e2db34043d346516))(struct [net\_if](structnet__if.md) \*iface,

1487 struct [net\_if\_addr](structnet__if__addr.md) \*addr,

1488 void \*user\_data);

1489

[ 1498](group__net__if.md#ga5ac646ad7fda0fa48e78c15b4ca52d50)void [net\_if\_ipv6\_addr\_foreach](group__net__if.md#ga5ac646ad7fda0fa48e78c15b4ca52d50)(struct [net\_if](structnet__if.md) \*iface, [net\_if\_ip\_addr\_cb\_t](group__net__if.md#gab58d8561a4f21899e2db34043d346516) cb,

1499 void \*user\_data);

1500

[ 1509](group__net__if.md#ga7ae82a491193dfea9b92cb9cbaf26f98)struct [net\_if\_mcast\_addr](structnet__if__mcast__addr.md) \*[net\_if\_ipv6\_maddr\_add](group__net__if.md#ga7ae82a491193dfea9b92cb9cbaf26f98)(struct [net\_if](structnet__if.md) \*iface,

1510 const struct [in6\_addr](structin6__addr.md) \*addr);

1511

[ 1520](group__net__if.md#gaf0ce126bb5019ff5f5ff0876b9712ad9)bool [net\_if\_ipv6\_maddr\_rm](group__net__if.md#gaf0ce126bb5019ff5f5ff0876b9712ad9)(struct [net\_if](structnet__if.md) \*iface, const struct [in6\_addr](structin6__addr.md) \*addr);

1521

[ 1530](group__net__if.md#ga726eed76563c223de8f611e2544febe9)typedef void (\*[net\_if\_ip\_maddr\_cb\_t](group__net__if.md#ga726eed76563c223de8f611e2544febe9))(struct [net\_if](structnet__if.md) \*iface,

1531 struct [net\_if\_mcast\_addr](structnet__if__mcast__addr.md) \*maddr,

1532 void \*user\_data);

1533

[ 1542](group__net__if.md#gab677496fb2e27be2df299a346e9c7132)void [net\_if\_ipv6\_maddr\_foreach](group__net__if.md#gab677496fb2e27be2df299a346e9c7132)(struct [net\_if](structnet__if.md) \*iface, [net\_if\_ip\_maddr\_cb\_t](group__net__if.md#ga726eed76563c223de8f611e2544febe9) cb,

1543 void \*user\_data);

1544

[ 1555](group__net__if.md#gadb4031153c4fef86110879befa6b9975)struct [net\_if\_mcast\_addr](structnet__if__mcast__addr.md) \*[net\_if\_ipv6\_maddr\_lookup](group__net__if.md#gadb4031153c4fef86110879befa6b9975)(const struct [in6\_addr](structin6__addr.md) \*addr,

1556 struct [net\_if](structnet__if.md) \*\*iface);

1557

[ 1568](group__net__if.md#ga0d64291573740a67eae7ff3fcc0910c5)typedef void (\*[net\_if\_mcast\_callback\_t](group__net__if.md#ga0d64291573740a67eae7ff3fcc0910c5))(struct [net\_if](structnet__if.md) \*iface,

1569 const struct net\_addr \*addr,

1570 bool is\_joined);

1571

[ 1580](structnet__if__mcast__monitor.md)struct [net\_if\_mcast\_monitor](structnet__if__mcast__monitor.md) {

[ 1582](structnet__if__mcast__monitor.md#a570b7d8a8a5fabca83982a5f7d1d896a) [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) [node](structnet__if__mcast__monitor.md#a570b7d8a8a5fabca83982a5f7d1d896a);

1583

[ 1585](structnet__if__mcast__monitor.md#af4d0e937b2b9161918a13a0d6723c60a) struct [net\_if](structnet__if.md) \*[iface](structnet__if__mcast__monitor.md#af4d0e937b2b9161918a13a0d6723c60a);

1586

[ 1588](structnet__if__mcast__monitor.md#aec441b858a5f6792ac9cdbc625f6babe) [net\_if\_mcast\_callback\_t](group__net__if.md#ga0d64291573740a67eae7ff3fcc0910c5) [cb](structnet__if__mcast__monitor.md#aec441b858a5f6792ac9cdbc625f6babe);

1589};

1590

[ 1599](group__net__if.md#ga8fdd0665ed76db6055777e395ca60255)void [net\_if\_mcast\_mon\_register](group__net__if.md#ga8fdd0665ed76db6055777e395ca60255)(struct [net\_if\_mcast\_monitor](structnet__if__mcast__monitor.md) \*mon,

1600 struct [net\_if](structnet__if.md) \*iface,

1601 [net\_if\_mcast\_callback\_t](group__net__if.md#ga0d64291573740a67eae7ff3fcc0910c5) cb);

1602

[ 1608](group__net__if.md#gad323732fe3d178a5dfdf0900e5cb5683)void [net\_if\_mcast\_mon\_unregister](group__net__if.md#gad323732fe3d178a5dfdf0900e5cb5683)(struct [net\_if\_mcast\_monitor](structnet__if__mcast__monitor.md) \*mon);

1609

[ 1617](group__net__if.md#ga372ef131263269cd65586d87997df745)void [net\_if\_mcast\_monitor](group__net__if.md#ga372ef131263269cd65586d87997df745)(struct [net\_if](structnet__if.md) \*iface, const struct net\_addr \*addr,

1618 bool is\_joined);

1619

[ 1626](group__net__if.md#ga49dbc954015307222f176f4149829b76)void [net\_if\_ipv6\_maddr\_join](group__net__if.md#ga49dbc954015307222f176f4149829b76)(struct [net\_if](structnet__if.md) \*iface,

1627 struct [net\_if\_mcast\_addr](structnet__if__mcast__addr.md) \*addr);

1628

[ 1636](group__net__if.md#gabe2c16a378a35a22d008bff9142e5449)static inline bool [net\_if\_ipv6\_maddr\_is\_joined](group__net__if.md#gabe2c16a378a35a22d008bff9142e5449)(struct [net\_if\_mcast\_addr](structnet__if__mcast__addr.md) \*addr)

1637{

1638 NET\_ASSERT(addr);

1639

1640 return addr->[is\_joined](structnet__if__mcast__addr.md#a4af9009b2f9ccc0589a9ba6dac10927b);

1641}

1642

[ 1649](group__net__if.md#gad24d5537d52de9781a7a6a55ceedd92b)void [net\_if\_ipv6\_maddr\_leave](group__net__if.md#gad24d5537d52de9781a7a6a55ceedd92b)(struct [net\_if](structnet__if.md) \*iface,

1650 struct [net\_if\_mcast\_addr](structnet__if__mcast__addr.md) \*addr);

1651

[ 1660](group__net__if.md#gae9f98dff661d52c5e3e5e185f0ed9cc0)struct [net\_if\_ipv6\_prefix](structnet__if__ipv6__prefix.md) \*[net\_if\_ipv6\_prefix\_get](group__net__if.md#gae9f98dff661d52c5e3e5e185f0ed9cc0)(struct [net\_if](structnet__if.md) \*[iface](structnet__if__ipv6__prefix.md#a0e2d1997e2ccfe1e1af5f16e0c74ed92),

1661 const struct [in6\_addr](structin6__addr.md) \*addr);

1662

[ 1672](group__net__if.md#gaaf9af457b97c0d432b6f9f9fdd184834)struct [net\_if\_ipv6\_prefix](structnet__if__ipv6__prefix.md) \*[net\_if\_ipv6\_prefix\_lookup](group__net__if.md#gaaf9af457b97c0d432b6f9f9fdd184834)(struct [net\_if](structnet__if.md) \*[iface](structnet__if__ipv6__prefix.md#a0e2d1997e2ccfe1e1af5f16e0c74ed92),

1673 struct [in6\_addr](structin6__addr.md) \*addr,

1674 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [len](structnet__if__ipv6__prefix.md#a4d2bc2acbe51256b76cf4d3ced3aac39));

1675

[ 1686](group__net__if.md#ga2f0c98b16b090d9aea07941c64cbe035)struct [net\_if\_ipv6\_prefix](structnet__if__ipv6__prefix.md) \*[net\_if\_ipv6\_prefix\_add](group__net__if.md#ga2f0c98b16b090d9aea07941c64cbe035)(struct [net\_if](structnet__if.md) \*[iface](structnet__if__ipv6__prefix.md#a0e2d1997e2ccfe1e1af5f16e0c74ed92),

1687 struct [in6\_addr](structin6__addr.md) \*[prefix](structnet__if__ipv6__prefix.md#a65b450d0942b3c96cfc575b462d82028),

1688 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [len](structnet__if__ipv6__prefix.md#a4d2bc2acbe51256b76cf4d3ced3aac39),

1689 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [lifetime](structnet__if__ipv6__prefix.md#a925a97a49d383bd4ce475f5d09fcb7e3));

1690

[ 1700](group__net__if.md#ga36f18c7a3ff1777006290170b726deed)bool [net\_if\_ipv6\_prefix\_rm](group__net__if.md#ga36f18c7a3ff1777006290170b726deed)(struct [net\_if](structnet__if.md) \*[iface](structnet__if__ipv6__prefix.md#a0e2d1997e2ccfe1e1af5f16e0c74ed92), struct [in6\_addr](structin6__addr.md) \*addr,

1701 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [len](structnet__if__ipv6__prefix.md#a4d2bc2acbe51256b76cf4d3ced3aac39));

1702

[ 1709](group__net__if.md#gaa3c711e814fb6a4e552b4ef723d0baa0)static inline void [net\_if\_ipv6\_prefix\_set\_lf](group__net__if.md#gaa3c711e814fb6a4e552b4ef723d0baa0)(struct [net\_if\_ipv6\_prefix](structnet__if__ipv6__prefix.md) \*[prefix](structnet__if__ipv6__prefix.md#a65b450d0942b3c96cfc575b462d82028),

1710 bool [is\_infinite](structnet__if__ipv6__prefix.md#a22090441b27bed06098679bf23b4e1e9))

1711{

1712 [prefix](structnet__if__ipv6__prefix.md#a65b450d0942b3c96cfc575b462d82028)->is\_infinite = [is\_infinite](structnet__if__ipv6__prefix.md#a22090441b27bed06098679bf23b4e1e9);

1713}

1714

[ 1721](group__net__if.md#ga68cffe343c518bad7f7f152e30f7f9ee)void [net\_if\_ipv6\_prefix\_set\_timer](group__net__if.md#ga68cffe343c518bad7f7f152e30f7f9ee)(struct [net\_if\_ipv6\_prefix](structnet__if__ipv6__prefix.md) \*[prefix](structnet__if__ipv6__prefix.md#a65b450d0942b3c96cfc575b462d82028),

1722 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [lifetime](structnet__if__ipv6__prefix.md#a925a97a49d383bd4ce475f5d09fcb7e3));

1723

[ 1729](group__net__if.md#ga2d68cb6dcfcffd3f87bbfb3dfce791ff)void [net\_if\_ipv6\_prefix\_unset\_timer](group__net__if.md#ga2d68cb6dcfcffd3f87bbfb3dfce791ff)(struct [net\_if\_ipv6\_prefix](structnet__if__ipv6__prefix.md) \*[prefix](structnet__if__ipv6__prefix.md#a65b450d0942b3c96cfc575b462d82028));

1730

[ 1741](group__net__if.md#ga25d6e2253c1d361553d478f7c948a28a)bool [net\_if\_ipv6\_addr\_onlink](group__net__if.md#ga25d6e2253c1d361553d478f7c948a28a)(struct [net\_if](structnet__if.md) \*\*[iface](structnet__if__ipv6__prefix.md#a0e2d1997e2ccfe1e1af5f16e0c74ed92), struct [in6\_addr](structin6__addr.md) \*addr);

1742

1749#if defined(CONFIG\_NET\_NATIVE\_IPV6)

1750static inline struct [in6\_addr](structin6__addr.md) \*[net\_if\_router\_ipv6](group__net__if.md#gadbf1538003473d448ff0808896b732a5)(struct [net\_if\_router](structnet__if__router.md) \*router)

1751{

1752 NET\_ASSERT(router);

1753

1754 return &router->[address](structnet__if__router.md#a86a2ca1b95e348acbde8ce90986b83db).in6\_addr;

1755}

1756#else

[ 1757](group__net__if.md#gadbf1538003473d448ff0808896b732a5)static inline struct [in6\_addr](structin6__addr.md) \*[net\_if\_router\_ipv6](group__net__if.md#gadbf1538003473d448ff0808896b732a5)(struct [net\_if\_router](structnet__if__router.md) \*router)

1758{

1759 static struct [in6\_addr](structin6__addr.md) addr;

1760

1761 ARG\_UNUSED(router);

1762

1763 return &addr;

1764}

1765#endif

1766

[ 1776](group__net__if.md#gacece4ee588082259b3b5cfcd5ac1d552)struct [net\_if\_router](structnet__if__router.md) \*[net\_if\_ipv6\_router\_lookup](group__net__if.md#gacece4ee588082259b3b5cfcd5ac1d552)(struct [net\_if](structnet__if.md) \*[iface](structnet__if__router.md#a03789aa0a40f7686b76616de0ca0401a),

1777 struct [in6\_addr](structin6__addr.md) \*addr);

1778

[ 1788](group__net__if.md#ga36dab2a8fd9120ebc9c8b18f1875ccfd)struct [net\_if\_router](structnet__if__router.md) \*[net\_if\_ipv6\_router\_find\_default](group__net__if.md#ga36dab2a8fd9120ebc9c8b18f1875ccfd)(struct [net\_if](structnet__if.md) \*[iface](structnet__if__router.md#a03789aa0a40f7686b76616de0ca0401a),

1789 struct [in6\_addr](structin6__addr.md) \*addr);

1790

[ 1797](group__net__if.md#gaadba4957802dc376ef011590c91c6af6)void [net\_if\_ipv6\_router\_update\_lifetime](group__net__if.md#gaadba4957802dc376ef011590c91c6af6)(struct [net\_if\_router](structnet__if__router.md) \*router,

1798 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [lifetime](structnet__if__router.md#a4b0d2ad8f225ab61022c10dfce3db199));

1799

[ 1809](group__net__if.md#ga9c766ed70ada6eb551ac6542d7ac1ca3)struct [net\_if\_router](structnet__if__router.md) \*[net\_if\_ipv6\_router\_add](group__net__if.md#ga9c766ed70ada6eb551ac6542d7ac1ca3)(struct [net\_if](structnet__if.md) \*[iface](structnet__if__router.md#a03789aa0a40f7686b76616de0ca0401a),

1810 struct [in6\_addr](structin6__addr.md) \*addr,

1811 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) router\_lifetime);

1812

[ 1820](group__net__if.md#ga1d108aa0b54c072e0aa9d0c049f02807)bool [net\_if\_ipv6\_router\_rm](group__net__if.md#ga1d108aa0b54c072e0aa9d0c049f02807)(struct [net\_if\_router](structnet__if__router.md) \*router);

1821

1830#if defined(CONFIG\_NET\_NATIVE\_IPV6)

1831[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [net\_if\_ipv6\_get\_hop\_limit](group__net__if.md#ga66d0a9a8eef095f6d4d44f35dd67f2b6)(struct [net\_if](structnet__if.md) \*[iface](structnet__if__router.md#a03789aa0a40f7686b76616de0ca0401a));

1832#else

[ 1833](group__net__if.md#ga66d0a9a8eef095f6d4d44f35dd67f2b6)static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [net\_if\_ipv6\_get\_hop\_limit](group__net__if.md#ga66d0a9a8eef095f6d4d44f35dd67f2b6)(struct [net\_if](structnet__if.md) \*[iface](structnet__if__router.md#a03789aa0a40f7686b76616de0ca0401a))

1834{

1835 ARG\_UNUSED([iface](structnet__if__router.md#a03789aa0a40f7686b76616de0ca0401a));

1836

1837 return 0;

1838}

1839#endif /\* CONFIG\_NET\_NATIVE\_IPV6 \*/

1840

1847#if defined(CONFIG\_NET\_NATIVE\_IPV6)

1848void [net\_if\_ipv6\_set\_hop\_limit](group__net__if.md#ga5bf726bb5c1d232103ec6841e7d0cd8c)(struct [net\_if](structnet__if.md) \*[iface](structnet__if__router.md#a03789aa0a40f7686b76616de0ca0401a), [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) hop\_limit);

1849#else

[ 1850](group__net__if.md#ga5bf726bb5c1d232103ec6841e7d0cd8c)static inline void [net\_if\_ipv6\_set\_hop\_limit](group__net__if.md#ga5bf726bb5c1d232103ec6841e7d0cd8c)(struct [net\_if](structnet__if.md) \*[iface](structnet__if__router.md#a03789aa0a40f7686b76616de0ca0401a),

1851 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) hop\_limit)

1852{

1853 ARG\_UNUSED([iface](structnet__if__router.md#a03789aa0a40f7686b76616de0ca0401a));

1854 ARG\_UNUSED(hop\_limit);

1855}

1856#endif /\* CONFIG\_NET\_NATIVE\_IPV6 \*/

1857

1859

1860/\* The old hop limit setter function is deprecated because the naming

1861 \* of it was incorrect. The API name was missing "\_if\_" so this function

1862 \* should not be used.

1863 \*/

1864\_\_deprecated

1865static inline void net\_ipv6\_set\_hop\_limit(struct [net\_if](structnet__if.md) \*[iface](structnet__if__router.md#a03789aa0a40f7686b76616de0ca0401a),

1866 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) hop\_limit)

1867{

1868 [net\_if\_ipv6\_set\_hop\_limit](group__net__if.md#ga5bf726bb5c1d232103ec6841e7d0cd8c)([iface](structnet__if__router.md#a03789aa0a40f7686b76616de0ca0401a), hop\_limit);

1869}

1870

1872

1881#if defined(CONFIG\_NET\_NATIVE\_IPV6)

1882[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [net\_if\_ipv6\_get\_mcast\_hop\_limit](group__net__if.md#ga56e7086633bcf4537f54c7ca70e6c900)(struct [net\_if](structnet__if.md) \*[iface](structnet__if__router.md#a03789aa0a40f7686b76616de0ca0401a));

1883#else

[ 1884](group__net__if.md#ga56e7086633bcf4537f54c7ca70e6c900)static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [net\_if\_ipv6\_get\_mcast\_hop\_limit](group__net__if.md#ga56e7086633bcf4537f54c7ca70e6c900)(struct [net\_if](structnet__if.md) \*[iface](structnet__if__router.md#a03789aa0a40f7686b76616de0ca0401a))

1885{

1886 ARG\_UNUSED([iface](structnet__if__router.md#a03789aa0a40f7686b76616de0ca0401a));

1887

1888 return 0;

1889}

1890#endif /\* CONFIG\_NET\_NATIVE\_IPV6 \*/

1891

1898#if defined(CONFIG\_NET\_NATIVE\_IPV6)

1899void [net\_if\_ipv6\_set\_mcast\_hop\_limit](group__net__if.md#gaf56a433679ea9701cf8baa3208f8ccc3)(struct [net\_if](structnet__if.md) \*[iface](structnet__if__router.md#a03789aa0a40f7686b76616de0ca0401a), [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) hop\_limit);

1900#else

[ 1901](group__net__if.md#gaf56a433679ea9701cf8baa3208f8ccc3)static inline void [net\_if\_ipv6\_set\_mcast\_hop\_limit](group__net__if.md#gaf56a433679ea9701cf8baa3208f8ccc3)(struct [net\_if](structnet__if.md) \*[iface](structnet__if__router.md#a03789aa0a40f7686b76616de0ca0401a),

1902 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) hop\_limit)

1903{

1904 ARG\_UNUSED([iface](structnet__if__router.md#a03789aa0a40f7686b76616de0ca0401a));

1905 ARG\_UNUSED(hop\_limit);

1906}

1907#endif /\* CONFIG\_NET\_NATIVE\_IPV6 \*/

1908

[ 1915](group__net__if.md#gab3939d735b660f8f02124df656ceba2c)static inline void [net\_if\_ipv6\_set\_base\_reachable\_time](group__net__if.md#gab3939d735b660f8f02124df656ceba2c)(struct [net\_if](structnet__if.md) \*[iface](structnet__if__router.md#a03789aa0a40f7686b76616de0ca0401a),

1916 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) reachable\_time)

1917{

1918#if defined(CONFIG\_NET\_NATIVE\_IPV6)

1919 NET\_ASSERT([iface](structnet__if__router.md#a03789aa0a40f7686b76616de0ca0401a));

1920

1921 if (![iface](structnet__if__router.md#a03789aa0a40f7686b76616de0ca0401a)->[config](structnet__if.md#a5e71962f55bdead7bfbbb96518c6c404).ip.ipv6) {

1922 return;

1923 }

1924

1925 [iface](structnet__if__router.md#a03789aa0a40f7686b76616de0ca0401a)->[config](structnet__if.md#a5e71962f55bdead7bfbbb96518c6c404).ip.ipv6->base\_reachable\_time = reachable\_time;

1926#else

1927 ARG\_UNUSED([iface](structnet__if__router.md#a03789aa0a40f7686b76616de0ca0401a));

1928 ARG\_UNUSED(reachable\_time);

1929

1930#endif

1931}

1932

[ 1940](group__net__if.md#ga9dd1f91edbb519a6a079f363c33efacf)static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [net\_if\_ipv6\_get\_reachable\_time](group__net__if.md#ga9dd1f91edbb519a6a079f363c33efacf)(struct [net\_if](structnet__if.md) \*[iface](structnet__if__router.md#a03789aa0a40f7686b76616de0ca0401a))

1941{

1942#if defined(CONFIG\_NET\_NATIVE\_IPV6)

1943 NET\_ASSERT([iface](structnet__if__router.md#a03789aa0a40f7686b76616de0ca0401a));

1944

1945 if (![iface](structnet__if__router.md#a03789aa0a40f7686b76616de0ca0401a)->[config](structnet__if.md#a5e71962f55bdead7bfbbb96518c6c404).ip.ipv6) {

1946 return 0;

1947 }

1948

1949 return [iface](structnet__if__router.md#a03789aa0a40f7686b76616de0ca0401a)->[config](structnet__if.md#a5e71962f55bdead7bfbbb96518c6c404).ip.ipv6->reachable\_time;

1950#else

1951 ARG\_UNUSED([iface](structnet__if__router.md#a03789aa0a40f7686b76616de0ca0401a));

1952 return 0;

1953#endif

1954}

1955

[ 1963](group__net__if.md#gab1861b5cefa73b4eefbb447cb1438cdc)[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [net\_if\_ipv6\_calc\_reachable\_time](group__net__if.md#gab1861b5cefa73b4eefbb447cb1438cdc)(struct [net\_if\_ipv6](structnet__if__ipv6.md) \*ipv6);

1964

[ 1971](group__net__if.md#ga8328266b870fd200660cb2becaab3de4)static inline void [net\_if\_ipv6\_set\_reachable\_time](group__net__if.md#ga8328266b870fd200660cb2becaab3de4)(struct [net\_if\_ipv6](structnet__if__ipv6.md) \*ipv6)

1972{

1973#if defined(CONFIG\_NET\_NATIVE\_IPV6)

1974 if (ipv6 == NULL) {

1975 return;

1976 }

1977

1978 ipv6->[reachable\_time](structnet__if__ipv6.md#af57b7dca189167f8cc757c4ed6b08f2f) = [net\_if\_ipv6\_calc\_reachable\_time](group__net__if.md#gab1861b5cefa73b4eefbb447cb1438cdc)(ipv6);

1979#else

1980 ARG\_UNUSED(ipv6);

1981#endif

1982}

1983

[ 1990](group__net__if.md#gad74566e5a34f447d2ac63d2c0e82eeff)static inline void [net\_if\_ipv6\_set\_retrans\_timer](group__net__if.md#gad74566e5a34f447d2ac63d2c0e82eeff)(struct [net\_if](structnet__if.md) \*[iface](structnet__if__router.md#a03789aa0a40f7686b76616de0ca0401a),

1991 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) retrans\_timer)

1992{

1993#if defined(CONFIG\_NET\_NATIVE\_IPV6)

1994 NET\_ASSERT([iface](structnet__if__router.md#a03789aa0a40f7686b76616de0ca0401a));

1995

1996 if (![iface](structnet__if__router.md#a03789aa0a40f7686b76616de0ca0401a)->[config](structnet__if.md#a5e71962f55bdead7bfbbb96518c6c404).ip.ipv6) {

1997 return;

1998 }

1999

2000 [iface](structnet__if__router.md#a03789aa0a40f7686b76616de0ca0401a)->[config](structnet__if.md#a5e71962f55bdead7bfbbb96518c6c404).ip.ipv6->retrans\_timer = retrans\_timer;

2001#else

2002 ARG\_UNUSED([iface](structnet__if__router.md#a03789aa0a40f7686b76616de0ca0401a));

2003 ARG\_UNUSED(retrans\_timer);

2004#endif

2005}

2006

[ 2014](group__net__if.md#gaddbf5a6ba412e6bdb7e31568fe827bd0)static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [net\_if\_ipv6\_get\_retrans\_timer](group__net__if.md#gaddbf5a6ba412e6bdb7e31568fe827bd0)(struct [net\_if](structnet__if.md) \*[iface](structnet__if__router.md#a03789aa0a40f7686b76616de0ca0401a))

2015{

2016#if defined(CONFIG\_NET\_NATIVE\_IPV6)

2017 NET\_ASSERT([iface](structnet__if__router.md#a03789aa0a40f7686b76616de0ca0401a));

2018

2019 if (![iface](structnet__if__router.md#a03789aa0a40f7686b76616de0ca0401a)->[config](structnet__if.md#a5e71962f55bdead7bfbbb96518c6c404).ip.ipv6) {

2020 return 0;

2021 }

2022

2023 return [iface](structnet__if__router.md#a03789aa0a40f7686b76616de0ca0401a)->[config](structnet__if.md#a5e71962f55bdead7bfbbb96518c6c404).ip.ipv6->retrans\_timer;

2024#else

2025 ARG\_UNUSED([iface](structnet__if__router.md#a03789aa0a40f7686b76616de0ca0401a));

2026 return 0;

2027#endif

2028}

2029

2041#if defined(CONFIG\_NET\_IPV6)

2042const struct [in6\_addr](structin6__addr.md) \*[net\_if\_ipv6\_select\_src\_addr](group__net__if.md#ga50689a1afdb37a7087bf47a12cc50438)(struct [net\_if](structnet__if.md) \*iface,

2043 const struct [in6\_addr](structin6__addr.md) \*dst);

2044#else

[ 2045](group__net__if.md#ga50689a1afdb37a7087bf47a12cc50438)static inline const struct [in6\_addr](structin6__addr.md) \*[net\_if\_ipv6\_select\_src\_addr](group__net__if.md#ga50689a1afdb37a7087bf47a12cc50438)(

2046 struct [net\_if](structnet__if.md) \*iface, const struct [in6\_addr](structin6__addr.md) \*dst)

2047{

2048 ARG\_UNUSED(iface);

2049 ARG\_UNUSED(dst);

2050

2051 return NULL;

2052}

2053#endif

2054

2068#if defined(CONFIG\_NET\_IPV6)

2069const struct [in6\_addr](structin6__addr.md) \*[net\_if\_ipv6\_select\_src\_addr\_hint](group__net__if.md#ga5cf4717e632f712045dd4fe81b30245c)(struct [net\_if](structnet__if.md) \*iface,

2070 const struct [in6\_addr](structin6__addr.md) \*dst,

2071 int [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

2072#else

[ 2073](group__net__if.md#ga5cf4717e632f712045dd4fe81b30245c)static inline const struct [in6\_addr](structin6__addr.md) \*[net\_if\_ipv6\_select\_src\_addr\_hint](group__net__if.md#ga5cf4717e632f712045dd4fe81b30245c)(

2074 struct [net\_if](structnet__if.md) \*iface, const struct [in6\_addr](structin6__addr.md) \*dst, int [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9))

2075{

2076 ARG\_UNUSED(iface);

2077 ARG\_UNUSED(dst);

2078 ARG\_UNUSED([flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

2079

2080 return NULL;

2081}

2082#endif

2083

2093#if defined(CONFIG\_NET\_IPV6)

2094struct [net\_if](structnet__if.md) \*[net\_if\_ipv6\_select\_src\_iface](group__net__if.md#gae1495ac9e743be54b8d90bd4ff4700ab)(const struct [in6\_addr](structin6__addr.md) \*dst);

2095#else

[ 2096](group__net__if.md#gae1495ac9e743be54b8d90bd4ff4700ab)static inline struct [net\_if](structnet__if.md) \*[net\_if\_ipv6\_select\_src\_iface](group__net__if.md#gae1495ac9e743be54b8d90bd4ff4700ab)(

2097 const struct [in6\_addr](structin6__addr.md) \*dst)

2098{

2099 ARG\_UNUSED(dst);

2100

2101 return NULL;

2102}

2103#endif

2104

[ 2114](group__net__if.md#gad6f3e1e349e281887352652f6f32274e)struct [in6\_addr](structin6__addr.md) \*[net\_if\_ipv6\_get\_ll](group__net__if.md#gad6f3e1e349e281887352652f6f32274e)(struct [net\_if](structnet__if.md) \*iface,

2115 enum [net\_addr\_state](group__ip__4__6.md#ga32e58fc83532ef57eeb6ff952f17288d) addr\_state);

2116

[ 2126](group__net__if.md#ga85b7a923d46d36ecd63f9930bd8970c4)struct [in6\_addr](structin6__addr.md) \*[net\_if\_ipv6\_get\_ll\_addr](group__net__if.md#ga85b7a923d46d36ecd63f9930bd8970c4)(enum [net\_addr\_state](group__ip__4__6.md#ga32e58fc83532ef57eeb6ff952f17288d) [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90),

2127 struct [net\_if](structnet__if.md) \*\*iface);

2128

[ 2136](group__net__if.md#ga1dd53d92f803cff3be4826ddfb6b7211)void [net\_if\_ipv6\_dad\_failed](group__net__if.md#ga1dd53d92f803cff3be4826ddfb6b7211)(struct [net\_if](structnet__if.md) \*iface, const struct [in6\_addr](structin6__addr.md) \*addr);

2137

[ 2149](group__net__if.md#gaca7d686c772deac13a027cc046333126)struct [in6\_addr](structin6__addr.md) \*[net\_if\_ipv6\_get\_global\_addr](group__net__if.md#gaca7d686c772deac13a027cc046333126)(enum [net\_addr\_state](group__ip__4__6.md#ga32e58fc83532ef57eeb6ff952f17288d) [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90),

2150 struct [net\_if](structnet__if.md) \*\*iface);

2151

[ 2162](group__net__if.md#ga3390e248249b28f2c80e2ca0bc79d236)int [net\_if\_config\_ipv4\_get](group__net__if.md#ga3390e248249b28f2c80e2ca0bc79d236)(struct [net\_if](structnet__if.md) \*iface,

2163 struct [net\_if\_ipv4](structnet__if__ipv4.md) \*\*ipv4);

2164

[ 2172](group__net__if.md#ga88c13a45617480a665c7f9f589ec8e10)int [net\_if\_config\_ipv4\_put](group__net__if.md#ga88c13a45617480a665c7f9f589ec8e10)(struct [net\_if](structnet__if.md) \*iface);

2173

[ 2181](group__net__if.md#ga7e1fd28dbcf1164d056296b4df782e64)[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [net\_if\_ipv4\_get\_ttl](group__net__if.md#ga7e1fd28dbcf1164d056296b4df782e64)(struct [net\_if](structnet__if.md) \*iface);

2182

[ 2189](group__net__if.md#ga5544374d7ebea26a239d561083f0203d)void [net\_if\_ipv4\_set\_ttl](group__net__if.md#ga5544374d7ebea26a239d561083f0203d)(struct [net\_if](structnet__if.md) \*iface, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ttl);

2190

[ 2198](group__net__if.md#ga71acb65b1988aab8cca9c9604c86231e)[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [net\_if\_ipv4\_get\_mcast\_ttl](group__net__if.md#ga71acb65b1988aab8cca9c9604c86231e)(struct [net\_if](structnet__if.md) \*iface);

2199

[ 2206](group__net__if.md#ga9452fef4f1309fb1a53a6a8b4f222377)void [net\_if\_ipv4\_set\_mcast\_ttl](group__net__if.md#ga9452fef4f1309fb1a53a6a8b4f222377)(struct [net\_if](structnet__if.md) \*iface, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ttl);

2207

[ 2216](group__net__if.md#ga04a8f21d173d51bdcc092b92ed949e53)struct [net\_if\_addr](structnet__if__addr.md) \*[net\_if\_ipv4\_addr\_lookup](group__net__if.md#ga04a8f21d173d51bdcc092b92ed949e53)(const struct [in\_addr](structin__addr.md) \*addr,

2217 struct [net\_if](structnet__if.md) \*\*iface);

2218

[ 2229](group__net__if.md#ga7190958f740cac56de3a13fe688b3b5d)struct [net\_if\_addr](structnet__if__addr.md) \*[net\_if\_ipv4\_addr\_add](group__net__if.md#ga7190958f740cac56de3a13fe688b3b5d)(struct [net\_if](structnet__if.md) \*iface,

2230 struct [in\_addr](structin__addr.md) \*addr,

2231 enum [net\_addr\_type](group__ip__4__6.md#gafecee2d4a331dc85ad962b81a6303e41) [addr\_type](structnet__if__addr.md#ab4fd41001cc24615803bfabb9d48e7eb),

2232 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) vlifetime);

2233

[ 2242](group__net__if.md#ga4433304d46b6559604486b828e7d9dec)bool [net\_if\_ipv4\_addr\_rm](group__net__if.md#ga4433304d46b6559604486b828e7d9dec)(struct [net\_if](structnet__if.md) \*iface, const struct [in\_addr](structin__addr.md) \*addr);

2243

[ 2252](group__net__if.md#ga0a22661727316517685afcd551e7b38e)\_\_syscall int [net\_if\_ipv4\_addr\_lookup\_by\_index](group__net__if.md#ga0a22661727316517685afcd551e7b38e)(const struct [in\_addr](structin__addr.md) \*addr);

2253

[ 2264](group__net__if.md#gad140a69cf510ad99a8a8c770bab95bc9)\_\_syscall bool [net\_if\_ipv4\_addr\_add\_by\_index](group__net__if.md#gad140a69cf510ad99a8a8c770bab95bc9)(int index,

2265 struct [in\_addr](structin__addr.md) \*addr,

2266 enum [net\_addr\_type](group__ip__4__6.md#gafecee2d4a331dc85ad962b81a6303e41) [addr\_type](structnet__if__addr.md#ab4fd41001cc24615803bfabb9d48e7eb),

2267 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) vlifetime);

2268

[ 2277](group__net__if.md#gac5bf15f948ab195cecce98d1b40bda37)\_\_syscall bool [net\_if\_ipv4\_addr\_rm\_by\_index](group__net__if.md#gac5bf15f948ab195cecce98d1b40bda37)(int index,

2278 const struct [in\_addr](structin__addr.md) \*addr);

2279

[ 2288](group__net__if.md#gaae71be476e27c178ebb21b0f183c2825)void [net\_if\_ipv4\_addr\_foreach](group__net__if.md#gaae71be476e27c178ebb21b0f183c2825)(struct [net\_if](structnet__if.md) \*iface, [net\_if\_ip\_addr\_cb\_t](group__net__if.md#gab58d8561a4f21899e2db34043d346516) cb,

2289 void \*user\_data);

2290

[ 2299](group__net__if.md#gaa43fa83711703f8737e50b639e11b16c)struct [net\_if\_mcast\_addr](structnet__if__mcast__addr.md) \*[net\_if\_ipv4\_maddr\_add](group__net__if.md#gaa43fa83711703f8737e50b639e11b16c)(struct [net\_if](structnet__if.md) \*iface,

2300 const struct [in\_addr](structin__addr.md) \*addr);

2301

[ 2310](group__net__if.md#ga1d9273e10ab089d0f02b2b17d10a9e60)bool [net\_if\_ipv4\_maddr\_rm](group__net__if.md#ga1d9273e10ab089d0f02b2b17d10a9e60)(struct [net\_if](structnet__if.md) \*iface, const struct [in\_addr](structin__addr.md) \*addr);

2311

[ 2320](group__net__if.md#gae82f53c670f602e9c37b65abb6dfaec7)void [net\_if\_ipv4\_maddr\_foreach](group__net__if.md#gae82f53c670f602e9c37b65abb6dfaec7)(struct [net\_if](structnet__if.md) \*iface, [net\_if\_ip\_maddr\_cb\_t](group__net__if.md#ga726eed76563c223de8f611e2544febe9) cb,

2321 void \*user\_data);

2322

[ 2333](group__net__if.md#gadc1514a0d6852de9dbce043bc99d4eb0)struct [net\_if\_mcast\_addr](structnet__if__mcast__addr.md) \*[net\_if\_ipv4\_maddr\_lookup](group__net__if.md#gadc1514a0d6852de9dbce043bc99d4eb0)(const struct [in\_addr](structin__addr.md) \*addr,

2334 struct [net\_if](structnet__if.md) \*\*iface);

2335

[ 2342](group__net__if.md#gae275a5e75817aa178d36f422573ad76a)void [net\_if\_ipv4\_maddr\_join](group__net__if.md#gae275a5e75817aa178d36f422573ad76a)(struct [net\_if](structnet__if.md) \*iface,

2343 struct [net\_if\_mcast\_addr](structnet__if__mcast__addr.md) \*addr);

2344

[ 2352](group__net__if.md#gaa30769fc8016f1a7496b3ede277d8d8a)static inline bool [net\_if\_ipv4\_maddr\_is\_joined](group__net__if.md#gaa30769fc8016f1a7496b3ede277d8d8a)(struct [net\_if\_mcast\_addr](structnet__if__mcast__addr.md) \*addr)

2353{

2354 NET\_ASSERT(addr);

2355

2356 return addr->[is\_joined](structnet__if__mcast__addr.md#a4af9009b2f9ccc0589a9ba6dac10927b);

2357}

2358

[ 2365](group__net__if.md#ga1408fe384736d20f36c035c10007113c)void [net\_if\_ipv4\_maddr\_leave](group__net__if.md#ga1408fe384736d20f36c035c10007113c)(struct [net\_if](structnet__if.md) \*iface,

2366 struct [net\_if\_mcast\_addr](structnet__if__mcast__addr.md) \*addr);

2367

2374#if defined(CONFIG\_NET\_NATIVE\_IPV4)

2375static inline struct [in\_addr](structin__addr.md) \*[net\_if\_router\_ipv4](group__net__if.md#ga2a48e13941c91ddb9bbc63d014729be1)(struct [net\_if\_router](structnet__if__router.md) \*router)

2376{

2377 NET\_ASSERT(router);

2378

2379 return &router->[address](structnet__if__router.md#a86a2ca1b95e348acbde8ce90986b83db).in\_addr;

2380}

2381#else

[ 2382](group__net__if.md#ga2a48e13941c91ddb9bbc63d014729be1)static inline struct [in\_addr](structin__addr.md) \*[net\_if\_router\_ipv4](group__net__if.md#ga2a48e13941c91ddb9bbc63d014729be1)(struct [net\_if\_router](structnet__if__router.md) \*router)

2383{

2384 static struct [in\_addr](structin__addr.md) addr;

2385

2386 ARG\_UNUSED(router);

2387

2388 return &addr;

2389}

2390#endif

2391

[ 2401](group__net__if.md#ga01f995b00248ad5da734e4d58a4353aa)struct [net\_if\_router](structnet__if__router.md) \*[net\_if\_ipv4\_router\_lookup](group__net__if.md#ga01f995b00248ad5da734e4d58a4353aa)(struct [net\_if](structnet__if.md) \*[iface](structnet__if__router.md#a03789aa0a40f7686b76616de0ca0401a),

2402 struct [in\_addr](structin__addr.md) \*addr);

2403

[ 2413](group__net__if.md#ga25672516d7f383807e7dd9ce5f46a94f)struct [net\_if\_router](structnet__if__router.md) \*[net\_if\_ipv4\_router\_find\_default](group__net__if.md#ga25672516d7f383807e7dd9ce5f46a94f)(struct [net\_if](structnet__if.md) \*[iface](structnet__if__router.md#a03789aa0a40f7686b76616de0ca0401a),

2414 struct [in\_addr](structin__addr.md) \*addr);

[ 2425](group__net__if.md#ga44984001411077c7a2ef68afb361b40f)struct [net\_if\_router](structnet__if__router.md) \*[net\_if\_ipv4\_router\_add](group__net__if.md#ga44984001411077c7a2ef68afb361b40f)(struct [net\_if](structnet__if.md) \*[iface](structnet__if__router.md#a03789aa0a40f7686b76616de0ca0401a),

2426 struct [in\_addr](structin__addr.md) \*addr,

2427 bool [is\_default](structnet__if__router.md#a34745207edcad2745d6ce311e2bf1894),

2428 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) router\_lifetime);

2429

[ 2437](group__net__if.md#ga6be14f5307bc63ce87ff0a3fad7c7f4d)bool [net\_if\_ipv4\_router\_rm](group__net__if.md#ga6be14f5307bc63ce87ff0a3fad7c7f4d)(struct [net\_if\_router](structnet__if__router.md) \*router);

2438

[ 2447](group__net__if.md#ga558b31e556a1a4b8d1e68a78f3f755ea)bool [net\_if\_ipv4\_addr\_mask\_cmp](group__net__if.md#ga558b31e556a1a4b8d1e68a78f3f755ea)(struct [net\_if](structnet__if.md) \*[iface](structnet__if__router.md#a03789aa0a40f7686b76616de0ca0401a),

2448 const struct [in\_addr](structin__addr.md) \*addr);

2449

[ 2458](group__net__if.md#ga8f93179138c1942bc1a099102a4314cf)bool [net\_if\_ipv4\_is\_addr\_bcast](group__net__if.md#ga8f93179138c1942bc1a099102a4314cf)(struct [net\_if](structnet__if.md) \*[iface](structnet__if__router.md#a03789aa0a40f7686b76616de0ca0401a),

2459 const struct [in\_addr](structin__addr.md) \*addr);

2460

2470#if defined(CONFIG\_NET\_IPV4)

2471struct [net\_if](structnet__if.md) \*[net\_if\_ipv4\_select\_src\_iface](group__net__if.md#gafea1a35f452ad8168855852cbfdf0024)(const struct [in\_addr](structin__addr.md) \*dst);

2472#else

[ 2473](group__net__if.md#gafea1a35f452ad8168855852cbfdf0024)static inline struct [net\_if](structnet__if.md) \*[net\_if\_ipv4\_select\_src\_iface](group__net__if.md#gafea1a35f452ad8168855852cbfdf0024)(

2474 const struct [in\_addr](structin__addr.md) \*dst)

2475{

2476 ARG\_UNUSED(dst);

2477

2478 return NULL;

2479}

2480#endif

2481

2493#if defined(CONFIG\_NET\_IPV4)

2494const struct [in\_addr](structin__addr.md) \*[net\_if\_ipv4\_select\_src\_addr](group__net__if.md#gad6ec091f61ba3055be60c77ce085522f)(struct [net\_if](structnet__if.md) \*iface,

2495 const struct [in\_addr](structin__addr.md) \*dst);

2496#else

[ 2497](group__net__if.md#gad6ec091f61ba3055be60c77ce085522f)static inline const struct [in\_addr](structin__addr.md) \*[net\_if\_ipv4\_select\_src\_addr](group__net__if.md#gad6ec091f61ba3055be60c77ce085522f)(

2498 struct [net\_if](structnet__if.md) \*iface, const struct [in\_addr](structin__addr.md) \*dst)

2499{

2500 ARG\_UNUSED(iface);

2501 ARG\_UNUSED(dst);

2502

2503 return NULL;

2504}

2505#endif

2506

[ 2516](group__net__if.md#gad2ffe8df3d5ccca5094daecf3b9a8508)struct [in\_addr](structin__addr.md) \*[net\_if\_ipv4\_get\_ll](group__net__if.md#gad2ffe8df3d5ccca5094daecf3b9a8508)(struct [net\_if](structnet__if.md) \*iface,

2517 enum [net\_addr\_state](group__ip__4__6.md#ga32e58fc83532ef57eeb6ff952f17288d) addr\_state);

2518

[ 2528](group__net__if.md#gad791780f25d19acfe49d5272eae2d019)struct [in\_addr](structin__addr.md) \*[net\_if\_ipv4\_get\_global\_addr](group__net__if.md#gad791780f25d19acfe49d5272eae2d019)(struct [net\_if](structnet__if.md) \*iface,

2529 enum [net\_addr\_state](group__ip__4__6.md#ga32e58fc83532ef57eeb6ff952f17288d) addr\_state);

2530

[ 2540](group__net__if.md#gadfad7d9232bf58c5626266387a2eb761)struct [in\_addr](structin__addr.md) [net\_if\_ipv4\_get\_netmask\_by\_addr](group__net__if.md#gadfad7d9232bf58c5626266387a2eb761)(struct [net\_if](structnet__if.md) \*iface,

2541 const struct [in\_addr](structin__addr.md) \*addr);

2542

[ 2552](group__net__if.md#ga41aeb0e7c5f9bc837f7b2ec13401afd1)\_\_deprecated struct [in\_addr](structin__addr.md) [net\_if\_ipv4\_get\_netmask](group__net__if.md#ga41aeb0e7c5f9bc837f7b2ec13401afd1)(struct [net\_if](structnet__if.md) \*iface);

2553

[ 2562](group__net__if.md#gad599bd11663fefa7d785b9fc5d52caf0)\_\_deprecated void [net\_if\_ipv4\_set\_netmask](group__net__if.md#gad599bd11663fefa7d785b9fc5d52caf0)(struct [net\_if](structnet__if.md) \*iface,

2563 const struct [in\_addr](structin__addr.md) \*netmask);

2564

[ 2575](group__net__if.md#ga94f2d2e69548609dd329c7e6b21e8958)\_\_deprecated \_\_syscall bool [net\_if\_ipv4\_set\_netmask\_by\_index](group__net__if.md#ga94f2d2e69548609dd329c7e6b21e8958)(int index,

2576 const struct [in\_addr](structin__addr.md) \*netmask);

2577

[ 2587](group__net__if.md#ga895cfd55f79f7fb78a17cf0e3004fa06)\_\_syscall bool [net\_if\_ipv4\_set\_netmask\_by\_addr\_by\_index](group__net__if.md#ga895cfd55f79f7fb78a17cf0e3004fa06)(int index,

2588 const struct [in\_addr](structin__addr.md) \*addr,

2589 const struct [in\_addr](structin__addr.md) \*netmask);

2590

[ 2600](group__net__if.md#ga7beda6ccba46fce3cf2da1ce6c0725ec)bool [net\_if\_ipv4\_set\_netmask\_by\_addr](group__net__if.md#ga7beda6ccba46fce3cf2da1ce6c0725ec)(struct [net\_if](structnet__if.md) \*iface,

2601 const struct [in\_addr](structin__addr.md) \*addr,

2602 const struct [in\_addr](structin__addr.md) \*netmask);

2603

[ 2611](group__net__if.md#gae42f6f9620e40e2d2b36d30e81bb82d9)struct [in\_addr](structin__addr.md) [net\_if\_ipv4\_get\_gw](group__net__if.md#gae42f6f9620e40e2d2b36d30e81bb82d9)(struct [net\_if](structnet__if.md) \*iface);

2612

[ 2619](group__net__if.md#ga310ccbd9b37629422ca8e32836362724)void [net\_if\_ipv4\_set\_gw](group__net__if.md#ga310ccbd9b37629422ca8e32836362724)(struct [net\_if](structnet__if.md) \*iface, const struct [in\_addr](structin__addr.md) \*gw);

2620

[ 2629](group__net__if.md#gadef49124c331817165475c69fb9104e0)\_\_syscall bool [net\_if\_ipv4\_set\_gw\_by\_index](group__net__if.md#gadef49124c331817165475c69fb9104e0)(int index, const struct [in\_addr](structin__addr.md) \*gw);

2630

[ 2641](group__net__if.md#ga001b1cdde5febcf3970848c7c185c81c)struct [net\_if](structnet__if.md) \*[net\_if\_select\_src\_iface](group__net__if.md#ga001b1cdde5febcf3970848c7c185c81c)(const struct [sockaddr](structsockaddr.md) \*dst);

2642

[ 2651](group__net__if.md#ga0f87d5753fcd7cce40ecd161e6c91078)typedef void (\*[net\_if\_link\_callback\_t](group__net__if.md#ga0f87d5753fcd7cce40ecd161e6c91078))(struct [net\_if](structnet__if.md) \*iface,

2652 struct [net\_linkaddr](structnet__linkaddr.md) \*dst,

2653 int status);

2654

[ 2663](structnet__if__link__cb.md)struct [net\_if\_link\_cb](structnet__if__link__cb.md) {

[ 2665](structnet__if__link__cb.md#accae7945a802c5b7fc36948b12a365ef) [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) [node](structnet__if__link__cb.md#accae7945a802c5b7fc36948b12a365ef);

2666

[ 2668](structnet__if__link__cb.md#a66092a22cba3dd69ac1a91c3522240bb) [net\_if\_link\_callback\_t](group__net__if.md#ga0f87d5753fcd7cce40ecd161e6c91078) [cb](structnet__if__link__cb.md#a66092a22cba3dd69ac1a91c3522240bb);

2669};

2670

[ 2677](group__net__if.md#gaa81b7d9ed8dc05da3391265dbc89b665)void [net\_if\_register\_link\_cb](group__net__if.md#gaa81b7d9ed8dc05da3391265dbc89b665)(struct [net\_if\_link\_cb](structnet__if__link__cb.md) \*link,

2678 [net\_if\_link\_callback\_t](group__net__if.md#ga0f87d5753fcd7cce40ecd161e6c91078) cb);

2679

[ 2685](group__net__if.md#ga6ba64fac6e8d846ae7be5990f49a8293)void [net\_if\_unregister\_link\_cb](group__net__if.md#ga6ba64fac6e8d846ae7be5990f49a8293)(struct [net\_if\_link\_cb](structnet__if__link__cb.md) \*link);

2686

[ 2694](group__net__if.md#gaaa64aa4391a85760bb2daf600ac4d898)void [net\_if\_call\_link\_cb](group__net__if.md#gaaa64aa4391a85760bb2daf600ac4d898)(struct [net\_if](structnet__if.md) \*iface, struct [net\_linkaddr](structnet__linkaddr.md) \*lladdr,

2695 int status);

2696

2698

2699/\* used to ensure encoding of checksum support in net\_if.h and

2700 \* ethernet.h is the same

2701 \*/

2702#define NET\_IF\_CHECKSUM\_NONE\_BIT 0

2703#define NET\_IF\_CHECKSUM\_IPV4\_HEADER\_BIT BIT(0)

2704#define NET\_IF\_CHECKSUM\_IPV4\_ICMP\_BIT BIT(1)

2705/\* Space for future protocols and restrictions for IPV4 \*/

2706#define NET\_IF\_CHECKSUM\_IPV6\_HEADER\_BIT BIT(10)

2707#define NET\_IF\_CHECKSUM\_IPV6\_ICMP\_BIT BIT(11)

2708/\* Space for future protocols and restrictions for IPV6 \*/

2709#define NET\_IF\_CHECKSUM\_TCP\_BIT BIT(21)

2710#define NET\_IF\_CHECKSUM\_UDP\_BIT BIT(22)

2711

2713

[ 2717](group__net__if.md#ga8db412ae79c64cafe81a66f5acb2f8e9)enum [net\_if\_checksum\_type](group__net__if.md#ga8db412ae79c64cafe81a66f5acb2f8e9) {

[ 2719](group__net__if.md#gga8db412ae79c64cafe81a66f5acb2f8e9a75e4a0946d0e6755ebd7cc62558aee30) [NET\_IF\_CHECKSUM\_IPV4\_HEADER](group__net__if.md#gga8db412ae79c64cafe81a66f5acb2f8e9a75e4a0946d0e6755ebd7cc62558aee30) = NET\_IF\_CHECKSUM\_IPV4\_HEADER\_BIT,

[ 2721](group__net__if.md#gga8db412ae79c64cafe81a66f5acb2f8e9aaed32a3cb700eac3b67c6c7e5a0cd0ad) [NET\_IF\_CHECKSUM\_IPV4\_TCP](group__net__if.md#gga8db412ae79c64cafe81a66f5acb2f8e9aaed32a3cb700eac3b67c6c7e5a0cd0ad) = NET\_IF\_CHECKSUM\_IPV4\_HEADER\_BIT |

2722 NET\_IF\_CHECKSUM\_TCP\_BIT,

[ 2724](group__net__if.md#gga8db412ae79c64cafe81a66f5acb2f8e9afe1eaaa765c8ec3c61618e943cd3f1c3) [NET\_IF\_CHECKSUM\_IPV4\_UDP](group__net__if.md#gga8db412ae79c64cafe81a66f5acb2f8e9afe1eaaa765c8ec3c61618e943cd3f1c3) = NET\_IF\_CHECKSUM\_IPV4\_HEADER\_BIT |

2725 NET\_IF\_CHECKSUM\_UDP\_BIT,

[ 2727](group__net__if.md#gga8db412ae79c64cafe81a66f5acb2f8e9a2aef87c97f22fdccdf1925d2687436b1) [NET\_IF\_CHECKSUM\_IPV4\_ICMP](group__net__if.md#gga8db412ae79c64cafe81a66f5acb2f8e9a2aef87c97f22fdccdf1925d2687436b1) = NET\_IF\_CHECKSUM\_IPV4\_ICMP\_BIT,

[ 2729](group__net__if.md#gga8db412ae79c64cafe81a66f5acb2f8e9ab204c7d5fddbd2c11e07a8831df6c00b) [NET\_IF\_CHECKSUM\_IPV6\_HEADER](group__net__if.md#gga8db412ae79c64cafe81a66f5acb2f8e9ab204c7d5fddbd2c11e07a8831df6c00b) = NET\_IF\_CHECKSUM\_IPV6\_HEADER\_BIT,

[ 2731](group__net__if.md#gga8db412ae79c64cafe81a66f5acb2f8e9a31e33593e4e7f7f9b36e319e0991ab13) [NET\_IF\_CHECKSUM\_IPV6\_TCP](group__net__if.md#gga8db412ae79c64cafe81a66f5acb2f8e9a31e33593e4e7f7f9b36e319e0991ab13) = NET\_IF\_CHECKSUM\_IPV6\_HEADER\_BIT |

2732 NET\_IF\_CHECKSUM\_TCP\_BIT,

[ 2734](group__net__if.md#gga8db412ae79c64cafe81a66f5acb2f8e9a70b1272e2125cea9204bae144fd86660) [NET\_IF\_CHECKSUM\_IPV6\_UDP](group__net__if.md#gga8db412ae79c64cafe81a66f5acb2f8e9a70b1272e2125cea9204bae144fd86660) = NET\_IF\_CHECKSUM\_IPV6\_HEADER\_BIT |

2735 NET\_IF\_CHECKSUM\_UDP\_BIT,

[ 2737](group__net__if.md#gga8db412ae79c64cafe81a66f5acb2f8e9af5b3bc7cb5e9771cd9fd57d9fda4c3b3) [NET\_IF\_CHECKSUM\_IPV6\_ICMP](group__net__if.md#gga8db412ae79c64cafe81a66f5acb2f8e9af5b3bc7cb5e9771cd9fd57d9fda4c3b3) = NET\_IF\_CHECKSUM\_IPV6\_ICMP\_BIT

2738};

2739

[ 2750](group__net__if.md#ga8048e722f6442bcd5b6881bd71e791a5)bool [net\_if\_need\_calc\_rx\_checksum](group__net__if.md#ga8048e722f6442bcd5b6881bd71e791a5)(struct [net\_if](structnet__if.md) \*iface,

2751 enum [net\_if\_checksum\_type](group__net__if.md#ga8db412ae79c64cafe81a66f5acb2f8e9) chksum\_type);

2752

[ 2764](group__net__if.md#ga9634c3e71e934ab3a07bec989b364663)bool [net\_if\_need\_calc\_tx\_checksum](group__net__if.md#ga9634c3e71e934ab3a07bec989b364663)(struct [net\_if](structnet__if.md) \*iface,

2765 enum [net\_if\_checksum\_type](group__net__if.md#ga8db412ae79c64cafe81a66f5acb2f8e9) chksum\_type);

2766

[ 2777](group__net__if.md#ga72708cdb7f133fe5d7edf819756c3516)\_\_syscall struct [net\_if](structnet__if.md) \*[net\_if\_get\_by\_index](group__net__if.md#ga72708cdb7f133fe5d7edf819756c3516)(int index);

2778

[ 2786](group__net__if.md#ga02445f6c61f0d29f56ac0ef59e025630)int [net\_if\_get\_by\_iface](group__net__if.md#ga02445f6c61f0d29f56ac0ef59e025630)(struct [net\_if](structnet__if.md) \*iface);

2787

[ 2795](group__net__if.md#gac48ab8e6337e7cf387af9b293f254a80)typedef void (\*[net\_if\_cb\_t](group__net__if.md#gac48ab8e6337e7cf387af9b293f254a80))(struct [net\_if](structnet__if.md) \*iface, void \*user\_data);

2796

[ 2804](group__net__if.md#ga96b198fd9df4a985b0dde84dd7152815)void [net\_if\_foreach](group__net__if.md#ga96b198fd9df4a985b0dde84dd7152815)([net\_if\_cb\_t](group__net__if.md#gac48ab8e6337e7cf387af9b293f254a80) cb, void \*user\_data);

2805

[ 2813](group__net__if.md#ga02644cc623fc7a8878c17d54984e4210)int [net\_if\_up](group__net__if.md#ga02644cc623fc7a8878c17d54984e4210)(struct [net\_if](structnet__if.md) \*iface);

2814

[ 2822](group__net__if.md#ga7e9b368d4abf9da5656140df70cfa334)static inline bool [net\_if\_is\_up](group__net__if.md#ga7e9b368d4abf9da5656140df70cfa334)(struct [net\_if](structnet__if.md) \*iface)

2823{

2824 NET\_ASSERT(iface);

2825

2826 return [net\_if\_flag\_is\_set](group__net__if.md#gae1f373ddd61c18a81481d8ddcfb12543)(iface, [NET\_IF\_UP](group__net__if.md#ggae691e5537917ffce27ad0db82c730371ab0ab7393d643354c46c3437d74c15840)) &&

2827 [net\_if\_flag\_is\_set](group__net__if.md#gae1f373ddd61c18a81481d8ddcfb12543)(iface, [NET\_IF\_RUNNING](group__net__if.md#ggae691e5537917ffce27ad0db82c730371add3e2ecdcd5de3154f9bd2836428a25a));

2828}

2829

[ 2837](group__net__if.md#ga2187650062d6139b9f4b81745a206803)int [net\_if\_down](group__net__if.md#ga2187650062d6139b9f4b81745a206803)(struct [net\_if](structnet__if.md) \*iface);

2838

[ 2846](group__net__if.md#ga099a484a654ad9af35d3212fc2c995b2)static inline bool [net\_if\_is\_admin\_up](group__net__if.md#ga099a484a654ad9af35d3212fc2c995b2)(struct [net\_if](structnet__if.md) \*iface)

2847{

2848 NET\_ASSERT(iface);

2849

2850 return [net\_if\_flag\_is\_set](group__net__if.md#gae1f373ddd61c18a81481d8ddcfb12543)(iface, [NET\_IF\_UP](group__net__if.md#ggae691e5537917ffce27ad0db82c730371ab0ab7393d643354c46c3437d74c15840));

2851}

2852

[ 2861](group__net__if.md#ga35e5db3a631ac9039f14d86e59fc0dcc)void [net\_if\_carrier\_on](group__net__if.md#ga35e5db3a631ac9039f14d86e59fc0dcc)(struct [net\_if](structnet__if.md) \*iface);

2862

[ 2871](group__net__if.md#ga6839941422a88c1f707ab70ea34df323)void [net\_if\_carrier\_off](group__net__if.md#ga6839941422a88c1f707ab70ea34df323)(struct [net\_if](structnet__if.md) \*iface);

2872

[ 2880](group__net__if.md#ga095554237016e563d76cfd602d1dae77)static inline bool [net\_if\_is\_carrier\_ok](group__net__if.md#ga095554237016e563d76cfd602d1dae77)(struct [net\_if](structnet__if.md) \*iface)

2881{

2882 NET\_ASSERT(iface);

2883

2884 return [net\_if\_flag\_is\_set](group__net__if.md#gae1f373ddd61c18a81481d8ddcfb12543)(iface, [NET\_IF\_LOWER\_UP](group__net__if.md#ggae691e5537917ffce27ad0db82c730371ab1a529826bad6b4bcd04185372f97d6d));

2885}

2886

[ 2897](group__net__if.md#ga89a3374d4bb116460a7b7c50a750b593)void [net\_if\_dormant\_on](group__net__if.md#ga89a3374d4bb116460a7b7c50a750b593)(struct [net\_if](structnet__if.md) \*iface);

2898

[ 2907](group__net__if.md#ga1c31fac887d944ac0a16aad70e889496)void [net\_if\_dormant\_off](group__net__if.md#ga1c31fac887d944ac0a16aad70e889496)(struct [net\_if](structnet__if.md) \*iface);

2908

[ 2916](group__net__if.md#ga6e2e6102271c37acaa59c54e2aa6b413)static inline bool [net\_if\_is\_dormant](group__net__if.md#ga6e2e6102271c37acaa59c54e2aa6b413)(struct [net\_if](structnet__if.md) \*iface)

2917{

2918 NET\_ASSERT(iface);

2919

2920 return [net\_if\_flag\_is\_set](group__net__if.md#gae1f373ddd61c18a81481d8ddcfb12543)(iface, [NET\_IF\_DORMANT](group__net__if.md#ggae691e5537917ffce27ad0db82c730371a7dd1db72a37b1fbc4c4491ce1c75238d));

2921}

2922

2923#if defined(CONFIG\_NET\_PKT\_TIMESTAMP) && defined(CONFIG\_NET\_NATIVE)

2931typedef void (\*net\_if\_timestamp\_callback\_t)(struct [net\_pkt](structnet__pkt.md) \*pkt);

2932

2941struct net\_if\_timestamp\_cb {

2943 [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) node;

2944

2948 struct net\_pkt \*pkt;

2949

2953 struct net\_if \*iface;

2954

2956 net\_if\_timestamp\_callback\_t cb;

2957};

2958

2969void net\_if\_register\_timestamp\_cb(struct net\_if\_timestamp\_cb \*handle,

2970 struct [net\_pkt](structnet__pkt.md) \*pkt,

2971 struct [net\_if](structnet__if.md) \*iface,

2972 net\_if\_timestamp\_callback\_t cb);

2973

2979void net\_if\_unregister\_timestamp\_cb(struct net\_if\_timestamp\_cb \*handle);

2980

2986void net\_if\_call\_timestamp\_cb(struct [net\_pkt](structnet__pkt.md) \*pkt);

2987

2988/\*

2989 \* @brief Add timestamped TX buffer to be handled

2990 \*

2991 \* @param pkt Timestamped buffer

2992 \*/

2993void net\_if\_add\_tx\_timestamp(struct [net\_pkt](structnet__pkt.md) \*pkt);

2994#endif /\* CONFIG\_NET\_PKT\_TIMESTAMP \*/

2995

3005#if defined(CONFIG\_NET\_PROMISCUOUS\_MODE)

3006int [net\_if\_set\_promisc](group__net__if.md#gaf9f81f3b9697ca47f7674d85f37a8d80)(struct [net\_if](structnet__if.md) \*iface);

3007#else

[ 3008](group__net__if.md#gaf9f81f3b9697ca47f7674d85f37a8d80)static inline int [net\_if\_set\_promisc](group__net__if.md#gaf9f81f3b9697ca47f7674d85f37a8d80)(struct [net\_if](structnet__if.md) \*iface)

3009{

3010 ARG\_UNUSED(iface);

3011

3012 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

3013}

3014#endif

3015

3021#if defined(CONFIG\_NET\_PROMISCUOUS\_MODE)

3022void [net\_if\_unset\_promisc](group__net__if.md#ga9c8212c087883510050ac6a39ef0a7bf)(struct [net\_if](structnet__if.md) \*iface);

3023#else

[ 3024](group__net__if.md#ga9c8212c087883510050ac6a39ef0a7bf)static inline void [net\_if\_unset\_promisc](group__net__if.md#ga9c8212c087883510050ac6a39ef0a7bf)(struct [net\_if](structnet__if.md) \*iface)

3025{

3026 ARG\_UNUSED(iface);

3027}

3028#endif

3029

3038#if defined(CONFIG\_NET\_PROMISCUOUS\_MODE)

3039bool [net\_if\_is\_promisc](group__net__if.md#ga9f1a6eab849517734ec422deb0ba71f5)(struct [net\_if](structnet__if.md) \*iface);

3040#else

[ 3041](group__net__if.md#ga9f1a6eab849517734ec422deb0ba71f5)static inline bool [net\_if\_is\_promisc](group__net__if.md#ga9f1a6eab849517734ec422deb0ba71f5)(struct [net\_if](structnet__if.md) \*iface)

3042{

3043 ARG\_UNUSED(iface);

3044

3045 return false;

3046}

3047#endif

3048

[ 3058](group__net__if.md#ga3cddda628eca248246f9aa3b81938f95)static inline bool [net\_if\_are\_pending\_tx\_packets](group__net__if.md#ga3cddda628eca248246f9aa3b81938f95)(struct [net\_if](structnet__if.md) \*iface)

3059{

3060#if defined(CONFIG\_NET\_POWER\_MANAGEMENT)

3061 return !!iface->tx\_pending;

3062#else

3063 ARG\_UNUSED(iface);

3064

3065 return false;

3066#endif

3067}

3068

3069#ifdef CONFIG\_NET\_POWER\_MANAGEMENT

3077int net\_if\_suspend(struct [net\_if](structnet__if.md) \*iface);

3078

3086int net\_if\_resume(struct [net\_if](structnet__if.md) \*iface);

3087

3095bool net\_if\_is\_suspended(struct [net\_if](structnet__if.md) \*iface);

3096#endif /\* CONFIG\_NET\_POWER\_MANAGEMENT \*/

3097

[ 3105](group__net__if.md#gaa458b5f349c55007108b47b99f4954d5)bool [net\_if\_is\_wifi](group__net__if.md#gaa458b5f349c55007108b47b99f4954d5)(struct [net\_if](structnet__if.md) \*iface);

3106

[ 3112](group__net__if.md#ga6e89bbafb6c0acdc6bf51078e2027236)struct [net\_if](structnet__if.md) \*[net\_if\_get\_first\_wifi](group__net__if.md#ga6e89bbafb6c0acdc6bf51078e2027236)(void);

3113

[ 3119](group__net__if.md#ga0fc3ba6172956f6847027e0bd3d367de)struct [net\_if](structnet__if.md) \*[net\_if\_get\_wifi\_sta](group__net__if.md#ga0fc3ba6172956f6847027e0bd3d367de)(void);

3120

[ 3126](group__net__if.md#gaf830eab616191009d88f58b761694b49)struct [net\_if](structnet__if.md) \*[net\_if\_get\_wifi\_sap](group__net__if.md#gaf830eab616191009d88f58b761694b49)(void);

3127

[ 3142](group__net__if.md#ga5f653cd73c1ecd548a931eb7fbd170f7)int [net\_if\_get\_name](group__net__if.md#ga5f653cd73c1ecd548a931eb7fbd170f7)(struct [net\_if](structnet__if.md) \*iface, char \*buf, int len);

3143

[ 3158](group__net__if.md#ga05dec64966fc39e3deb0679b9585688b)int [net\_if\_set\_name](group__net__if.md#ga05dec64966fc39e3deb0679b9585688b)(struct [net\_if](structnet__if.md) \*iface, const char \*buf);

3159

[ 3167](group__net__if.md#ga1774ac036032bb0dc2c662f6f4f66a7f)int [net\_if\_get\_by\_name](group__net__if.md#ga1774ac036032bb0dc2c662f6f4f66a7f)(const char \*name);

3168

3170struct net\_if\_api {

3171 void (\*init)(struct [net\_if](structnet__if.md) \*iface);

3172};

3173

3174#define NET\_IF\_DHCPV4\_INIT \

3175 IF\_ENABLED(UTIL\_AND(IS\_ENABLED(CONFIG\_NET\_DHCPV4), \

3176 IS\_ENABLED(CONFIG\_NET\_NATIVE\_IPV4)), \

3177 (.dhcpv4.state = NET\_DHCPV4\_DISABLED,))

3178

3179#define NET\_IF\_DHCPV6\_INIT \

3180 IF\_ENABLED(UTIL\_AND(IS\_ENABLED(CONFIG\_NET\_DHCPV6), \

3181 IS\_ENABLED(CONFIG\_NET\_NATIVE\_IPV6)), \

3182 (.dhcpv6.state = NET\_DHCPV6\_DISABLED,))

3183

3184#define NET\_IF\_CONFIG\_INIT \

3185 .config = { \

3186 IF\_ENABLED(CONFIG\_NET\_IP, (.ip = {},)) \

3187 NET\_IF\_DHCPV4\_INIT \

3188 NET\_IF\_DHCPV6\_INIT \

3189 }

3190

3191#define NET\_IF\_GET\_NAME(dev\_id, sfx) \_\_net\_if\_##dev\_id##\_##sfx

3192#define NET\_IF\_DEV\_GET\_NAME(dev\_id, sfx) \_\_net\_if\_dev\_##dev\_id##\_##sfx

3193

3194#define NET\_IF\_GET(dev\_id, sfx) \

3195 ((struct net\_if \*)&NET\_IF\_GET\_NAME(dev\_id, sfx))

3196

3197#define NET\_IF\_INIT(dev\_id, sfx, \_l2, \_mtu, \_num\_configs) \

3198 static STRUCT\_SECTION\_ITERABLE(net\_if\_dev, \

3199 NET\_IF\_DEV\_GET\_NAME(dev\_id, sfx)) = { \

3200 .dev = &(DEVICE\_NAME\_GET(dev\_id)), \

3201 .l2 = &(NET\_L2\_GET\_NAME(\_l2)), \

3202 .l2\_data = &(NET\_L2\_GET\_DATA(dev\_id, sfx)), \

3203 .mtu = \_mtu, \

3204 .flags = {BIT(NET\_IF\_LOWER\_UP)}, \

3205 }; \

3206 static Z\_DECL\_ALIGN(struct net\_if) \

3207 NET\_IF\_GET\_NAME(dev\_id, sfx)[\_num\_configs] \

3208 \_\_used \_\_in\_section(\_net\_if, static, \

3209 dev\_id) = { \

3210 [0 ... (\_num\_configs - 1)] = { \

3211 .if\_dev = &(NET\_IF\_DEV\_GET\_NAME(dev\_id, sfx)), \

3212 NET\_IF\_CONFIG\_INIT \

3213 } \

3214 }

3215

3216#define NET\_IF\_OFFLOAD\_INIT(dev\_id, sfx, \_mtu) \

3217 static STRUCT\_SECTION\_ITERABLE(net\_if\_dev, \

3218 NET\_IF\_DEV\_GET\_NAME(dev\_id, sfx)) = { \

3219 .dev = &(DEVICE\_NAME\_GET(dev\_id)), \

3220 .mtu = \_mtu, \

3221 .l2 = &(NET\_L2\_GET\_NAME(OFFLOADED\_NETDEV)), \

3222 .flags = {BIT(NET\_IF\_LOWER\_UP)}, \

3223 }; \

3224 static Z\_DECL\_ALIGN(struct net\_if) \

3225 NET\_IF\_GET\_NAME(dev\_id, sfx)[NET\_IF\_MAX\_CONFIGS] \

3226 \_\_used \_\_in\_section(\_net\_if, static, \

3227 dev\_id) = { \

3228 [0 ... (NET\_IF\_MAX\_CONFIGS - 1)] = { \

3229 .if\_dev = &(NET\_IF\_DEV\_GET\_NAME(dev\_id, sfx)), \

3230 NET\_IF\_CONFIG\_INIT \

3231 } \

3232 }

3233

3235

3236/\* Network device initialization macros \*/

3237

3238#define Z\_NET\_DEVICE\_INIT\_INSTANCE(node\_id, dev\_id, name, instance, \

3239 init\_fn, pm, data, config, prio, \

3240 api, l2, l2\_ctx\_type, mtu) \

3241 Z\_DEVICE\_STATE\_DEFINE(dev\_id); \

3242 Z\_DEVICE\_DEFINE(node\_id, dev\_id, name, init\_fn, pm, data, \

3243 config, POST\_KERNEL, prio, api, \

3244 &Z\_DEVICE\_STATE\_NAME(dev\_id)); \

3245 NET\_L2\_DATA\_INIT(dev\_id, instance, l2\_ctx\_type); \

3246 NET\_IF\_INIT(dev\_id, instance, l2, mtu, NET\_IF\_MAX\_CONFIGS)

3247

3248#define Z\_NET\_DEVICE\_INIT(node\_id, dev\_id, name, init\_fn, pm, data, \

3249 config, prio, api, l2, l2\_ctx\_type, mtu) \

3250 Z\_NET\_DEVICE\_INIT\_INSTANCE(node\_id, dev\_id, name, 0, init\_fn, \

3251 pm, data, config, prio, api, l2, \

3252 l2\_ctx\_type, mtu)

3253

[ 3273](group__net__if.md#ga02971562c42494e2a5f71e1f8587e709)#define NET\_DEVICE\_INIT(dev\_id, name, init\_fn, pm, data, config, prio, \

3274 api, l2, l2\_ctx\_type, mtu) \

3275 Z\_NET\_DEVICE\_INIT(DT\_INVALID\_NODE, dev\_id, name, init\_fn, pm, \

3276 data, config, prio, api, l2, l2\_ctx\_type, mtu)

3277

[ 3296](group__net__if.md#gab1f762b01ae7bc37cd4a25724c123dda)#define NET\_DEVICE\_DT\_DEFINE(node\_id, init\_fn, pm, data, \

3297 config, prio, api, l2, l2\_ctx\_type, mtu) \

3298 Z\_NET\_DEVICE\_INIT(node\_id, Z\_DEVICE\_DT\_DEV\_ID(node\_id), \

3299 DEVICE\_DT\_NAME(node\_id), init\_fn, pm, data, \

3300 config, prio, api, l2, l2\_ctx\_type, mtu)

3301

[ 3310](group__net__if.md#ga7edd8bc59444d92cad0371c36f9949b7)#define NET\_DEVICE\_DT\_INST\_DEFINE(inst, ...) \

3311 NET\_DEVICE\_DT\_DEFINE(DT\_DRV\_INST(inst), \_\_VA\_ARGS\_\_)

3312

[ 3336](group__net__if.md#gacc7edecdd9de9920cc155977d8fec2a2)#define NET\_DEVICE\_INIT\_INSTANCE(dev\_id, name, instance, init\_fn, pm, \

3337 data, config, prio, api, l2, \

3338 l2\_ctx\_type, mtu) \

3339 Z\_NET\_DEVICE\_INIT\_INSTANCE(DT\_INVALID\_NODE, dev\_id, name, \

3340 instance, init\_fn, pm, data, config, \

3341 prio, api, l2, l2\_ctx\_type, mtu)

3342

[ 3365](group__net__if.md#ga50702b043a0791e59e7d5679dda1d9e8)#define NET\_DEVICE\_DT\_DEFINE\_INSTANCE(node\_id, instance, init\_fn, pm, \

3366 data, config, prio, api, l2, \

3367 l2\_ctx\_type, mtu) \

3368 Z\_NET\_DEVICE\_INIT\_INSTANCE(node\_id, \

3369 Z\_DEVICE\_DT\_DEV\_ID(node\_id), \

3370 DEVICE\_DT\_NAME(node\_id), instance, \

3371 init\_fn, pm, data, config, prio, \

3372 api, l2, l2\_ctx\_type, mtu)

3373

[ 3383](group__net__if.md#gabe4b8589996a53cbc50b76c8ea15aa0c)#define NET\_DEVICE\_DT\_INST\_DEFINE\_INSTANCE(inst, ...) \

3384 NET\_DEVICE\_DT\_DEFINE\_INSTANCE(DT\_DRV\_INST(inst), \_\_VA\_ARGS\_\_)

3385

3386#define Z\_NET\_DEVICE\_OFFLOAD\_INIT(node\_id, dev\_id, name, init\_fn, pm, \

3387 data, config, prio, api, mtu) \

3388 Z\_DEVICE\_STATE\_DEFINE(dev\_id); \

3389 Z\_DEVICE\_DEFINE(node\_id, dev\_id, name, init\_fn, pm, data, \

3390 config, POST\_KERNEL, prio, api, \

3391 &Z\_DEVICE\_STATE\_NAME(dev\_id)); \

3392 NET\_IF\_OFFLOAD\_INIT(dev\_id, 0, mtu)

3393

[ 3413](group__net__if.md#ga255672607b7958db3f464d2a57a7e635)#define NET\_DEVICE\_OFFLOAD\_INIT(dev\_id, name, init\_fn, pm, data, \

3414 config, prio, api, mtu) \

3415 Z\_NET\_DEVICE\_OFFLOAD\_INIT(DT\_INVALID\_NODE, dev\_id, name, \

3416 init\_fn, pm, data, config, prio, api, \

3417 mtu)

3418

[ 3437](group__net__if.md#gab2b287025e194dec1fab24e44d95362f)#define NET\_DEVICE\_DT\_OFFLOAD\_DEFINE(node\_id, init\_fn, pm, data, \

3438 config, prio, api, mtu) \

3439 Z\_NET\_DEVICE\_OFFLOAD\_INIT(node\_id, Z\_DEVICE\_DT\_DEV\_ID(node\_id), \

3440 DEVICE\_DT\_NAME(node\_id), init\_fn, pm, \

3441 data, config, prio, api, mtu)

3442

[ 3452](group__net__if.md#ga1cab6943a28e3d3754e36623834b93fd)#define NET\_DEVICE\_DT\_INST\_OFFLOAD\_DEFINE(inst, ...) \

3453 NET\_DEVICE\_DT\_OFFLOAD\_DEFINE(DT\_DRV\_INST(inst), \_\_VA\_ARGS\_\_)

3454

[ 3460](group__net__if.md#ga6c081875a6f5a848b3ad2fd220c63c3c)#define NET\_IFACE\_COUNT(\_dst) \

3461 do { \

3462 extern struct net\_if \_net\_if\_list\_start[]; \

3463 extern struct net\_if \_net\_if\_list\_end[]; \

3464 \*(\_dst) = ((uintptr\_t)\_net\_if\_list\_end - \

3465 (uintptr\_t)\_net\_if\_list\_start) / \

3466 sizeof(struct net\_if); \

3467 } while (0)

3468

3469#ifdef \_\_cplusplus

3470}

3471#endif

3472

3473#include <zephyr/syscalls/net\_if.h>

3474

3478

3479#endif /\* ZEPHYR\_INCLUDE\_NET\_NET\_IF\_H\_ \*/

[k\_thread\_stack\_t](arch__interface_8h.md#a9fc2dce533bd7b8cb1fdd4bdbb2b62b1)

struct z\_thread\_stack\_element k\_thread\_stack\_t

Typedef of struct z\_thread\_stack\_element.

**Definition** arch\_interface.h:46

[atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8)

long atomic\_t

**Definition** atomic\_types.h:15

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

**Definition** kernel.h:1440

[sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda)

unsigned short int sa\_family\_t

Socket address family type.

**Definition** net\_ip.h:167

[net\_addr\_state](group__ip__4__6.md#ga32e58fc83532ef57eeb6ff952f17288d)

net\_addr\_state

What is the current state of the network address.

**Definition** net\_ip.h:503

[net\_addr\_type](group__ip__4__6.md#gafecee2d4a331dc85ad962b81a6303e41)

net\_addr\_type

How the network address is assigned to network interface.

**Definition** net\_ip.h:511

[k\_mutex\_unlock](group__mutex__apis.md#ga360f4c0e7258b0d7030cdb1f452b2c31)

int k\_mutex\_unlock(struct k\_mutex \*mutex)

Unlock a mutex.

[k\_mutex\_lock](group__mutex__apis.md#ga850549358645249c285669baa49c33b0)

int k\_mutex\_lock(struct k\_mutex \*mutex, k\_timeout\_t timeout)

Lock a mutex.

[net\_verdict](group__net__core.md#ga8e5393f3bdd85491f221324e637c3896)

net\_verdict

Net Verdict.

**Definition** net\_core.h:102

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

**Definition** net\_if.h:2880

[net\_if\_is\_admin\_up](group__net__if.md#ga099a484a654ad9af35d3212fc2c995b2)

static bool net\_if\_is\_admin\_up(struct net\_if \*iface)

Check if interface was brought up by the administrator.

**Definition** net\_if.h:2846

[net\_if\_set\_default](group__net__if.md#ga0a1f27ec893e1af3c97f130be4616589)

void net\_if\_set\_default(struct net\_if \*iface)

Set the default network interface.

[net\_if\_ipv4\_addr\_lookup\_by\_index](group__net__if.md#ga0a22661727316517685afcd551e7b38e)

int net\_if\_ipv4\_addr\_lookup\_by\_index(const struct in\_addr \*addr)

Check if this IPv4 address belongs to one of the interface indices.

[net\_if\_mcast\_callback\_t](group__net__if.md#ga0d64291573740a67eae7ff3fcc0910c5)

void(\* net\_if\_mcast\_callback\_t)(struct net\_if \*iface, const struct net\_addr \*addr, bool is\_joined)

Define a callback that is called whenever a IPv6 or IPv4 multicast address group is joined or left.

**Definition** net\_if.h:1568

[net\_if\_link\_callback\_t](group__net__if.md#ga0f87d5753fcd7cce40ecd161e6c91078)

void(\* net\_if\_link\_callback\_t)(struct net\_if \*iface, struct net\_linkaddr \*dst, int status)

Define callback that is called after a network packet has been sent.

**Definition** net\_if.h:2651

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

**Definition** net\_if.h:857

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

**Definition** net\_if.h:2382

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

**Definition** net\_if.h:929

[net\_if\_are\_pending\_tx\_packets](group__net__if.md#ga3cddda628eca248246f9aa3b81938f95)

static bool net\_if\_are\_pending\_tx\_packets(struct net\_if \*iface)

Check if there are any pending TX network data for a given network interface.

**Definition** net\_if.h:3058

[net\_if\_ipv4\_get\_netmask](group__net__if.md#ga41aeb0e7c5f9bc837f7b2ec13401afd1)

struct in\_addr net\_if\_ipv4\_get\_netmask(struct net\_if \*iface)

Get IPv4 netmask of an interface.

[net\_if\_flag\_test\_and\_set](group__net__if.md#ga42e7482191a92007960601f8bb621dca)

static bool net\_if\_flag\_test\_and\_set(struct net\_if \*iface, enum net\_if\_flag value)

Test and set a value in network interface flags.

**Definition** net\_if.h:787

[net\_if\_ipv4\_addr\_rm](group__net__if.md#ga4433304d46b6559604486b828e7d9dec)

bool net\_if\_ipv4\_addr\_rm(struct net\_if \*iface, const struct in\_addr \*addr)

Remove a IPv4 address from an interface.

[net\_if\_ipv4\_router\_add](group__net__if.md#ga44984001411077c7a2ef68afb361b40f)

struct net\_if\_router \* net\_if\_ipv4\_router\_add(struct net\_if \*iface, struct in\_addr \*addr, bool is\_default, uint16\_t router\_lifetime)

Add IPv4 router to the system.

[net\_if\_get\_link\_addr](group__net__if.md#ga467186e964bf721e14fed38392f21872)

static struct net\_linkaddr \* net\_if\_get\_link\_addr(struct net\_if \*iface)

Get an network interface's link address.

**Definition** net\_if.h:1078

[net\_if\_ipv6\_maddr\_join](group__net__if.md#ga49dbc954015307222f176f4149829b76)

void net\_if\_ipv6\_maddr\_join(struct net\_if \*iface, struct net\_if\_mcast\_addr \*addr)

Mark a given multicast address to be joined.

[net\_if\_ipv6\_select\_src\_addr](group__net__if.md#ga50689a1afdb37a7087bf47a12cc50438)

static const struct in6\_addr \* net\_if\_ipv6\_select\_src\_addr(struct net\_if \*iface, const struct in6\_addr \*dst)

Get a IPv6 source address that should be used when sending network data to destination.

**Definition** net\_if.h:2045

[net\_if\_nbr\_reachability\_hint](group__net__if.md#ga51af469ff3d7d9f760d63a8a9c7be8b5)

static void net\_if\_nbr\_reachability\_hint(struct net\_if \*iface, const struct in6\_addr \*ipv6\_addr)

Provide a reachability hint for IPv6 Neighbor Discovery.

**Definition** net\_if.h:1151

[net\_if\_offload](group__net__if.md#ga520939e94620ca75475a71f153df6d4a)

static struct net\_offload \* net\_if\_offload(struct net\_if \*iface)

Return the IP offload plugin.

**Definition** net\_if.h:995

[net\_if\_set\_link\_addr](group__net__if.md#ga52b41b2f8b7d3405338a0539542677a0)

static int net\_if\_set\_link\_addr(struct net\_if \*iface, uint8\_t \*addr, uint8\_t len, enum net\_link\_type type)

Set a network interface's link address.

**Definition** net\_if.h:1219

[net\_if\_flag\_set](group__net__if.md#ga52f9fca13e9f836799e0e40f581744d2)

static void net\_if\_flag\_set(struct net\_if \*iface, enum net\_if\_flag value)

Set a value in network interface flags.

**Definition** net\_if.h:770

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

**Definition** net\_if.h:1884

[net\_if\_ipv6\_addr\_foreach](group__net__if.md#ga5ac646ad7fda0fa48e78c15b4ca52d50)

void net\_if\_ipv6\_addr\_foreach(struct net\_if \*iface, net\_if\_ip\_addr\_cb\_t cb, void \*user\_data)

Go through all IPv6 addresses on a network interface and call callback for each used address.

[net\_if\_ipv6\_set\_hop\_limit](group__net__if.md#ga5bf726bb5c1d232103ec6841e7d0cd8c)

static void net\_if\_ipv6\_set\_hop\_limit(struct net\_if \*iface, uint8\_t hop\_limit)

Set the default IPv6 hop limit of a given interface.

**Definition** net\_if.h:1850

[net\_if\_ipv6\_select\_src\_addr\_hint](group__net__if.md#ga5cf4717e632f712045dd4fe81b30245c)

static const struct in6\_addr \* net\_if\_ipv6\_select\_src\_addr\_hint(struct net\_if \*iface, const struct in6\_addr \*dst, int flags)

Get a IPv6 source address that should be used when sending network data to destination.

**Definition** net\_if.h:2073

[net\_if\_get\_name](group__net__if.md#ga5f653cd73c1ecd548a931eb7fbd170f7)

int net\_if\_get\_name(struct net\_if \*iface, char \*buf, int len)

Get network interface name.

[net\_if\_ipv6\_addr\_rm](group__net__if.md#ga614e1458fa28d26c26f447e9fbcc2cb7)

bool net\_if\_ipv6\_addr\_rm(struct net\_if \*iface, const struct in6\_addr \*addr)

Remove an IPv6 address from an interface.

[net\_if\_ipv6\_get\_hop\_limit](group__net__if.md#ga66d0a9a8eef095f6d4d44f35dd67f2b6)

static uint8\_t net\_if\_ipv6\_get\_hop\_limit(struct net\_if \*iface)

Get IPv6 hop limit specified for a given interface.

**Definition** net\_if.h:1833

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

**Definition** net\_if.h:967

[net\_if\_is\_dormant](group__net__if.md#ga6e2e6102271c37acaa59c54e2aa6b413)

static bool net\_if\_is\_dormant(struct net\_if \*iface)

Check if the interface is dormant.

**Definition** net\_if.h:2916

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

**Definition** net\_if.h:1530

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

**Definition** net\_if.h:1254

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

**Definition** net\_if.h:2822

[net\_if\_need\_calc\_rx\_checksum](group__net__if.md#ga8048e722f6442bcd5b6881bd71e791a5)

bool net\_if\_need\_calc\_rx\_checksum(struct net\_if \*iface, enum net\_if\_checksum\_type chksum\_type)

Check if received network packet checksum calculation can be avoided or not.

[net\_if\_ipv6\_set\_reachable\_time](group__net__if.md#ga8328266b870fd200660cb2becaab3de4)

static void net\_if\_ipv6\_set\_reachable\_time(struct net\_if\_ipv6 \*ipv6)

Set IPv6 reachable time for a given interface.

**Definition** net\_if.h:1971

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

**Definition** net\_if.h:2717

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

**Definition** net\_if.h:1108

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

**Definition** net\_if.h:3024

[net\_if\_socket\_offload\_set](group__net__if.md#ga9db52875580115c743b1f35cd6c46796)

static void net\_if\_socket\_offload\_set(struct net\_if \*iface, net\_socket\_create\_t socket\_offload)

Set the function to create an offloaded socket.

**Definition** net\_if.h:1036

[net\_if\_ipv6\_get\_reachable\_time](group__net__if.md#ga9dd1f91edbb519a6a079f363c33efacf)

static uint32\_t net\_if\_ipv6\_get\_reachable\_time(struct net\_if \*iface)

Get IPv6 reachable timeout specified for a given interface.

**Definition** net\_if.h:1940

[net\_if\_is\_promisc](group__net__if.md#ga9f1a6eab849517734ec422deb0ba71f5)

static bool net\_if\_is\_promisc(struct net\_if \*iface)

Check if promiscuous mode is set or not.

**Definition** net\_if.h:3041

[net\_if\_ipv4\_maddr\_is\_joined](group__net__if.md#gaa30769fc8016f1a7496b3ede277d8d8a)

static bool net\_if\_ipv4\_maddr\_is\_joined(struct net\_if\_mcast\_addr \*addr)

Check if given multicast address is joined or not.

**Definition** net\_if.h:2352

[net\_if\_ipv6\_prefix\_set\_lf](group__net__if.md#gaa3c711e814fb6a4e552b4ef723d0baa0)

static void net\_if\_ipv6\_prefix\_set\_lf(struct net\_if\_ipv6\_prefix \*prefix, bool is\_infinite)

Set the infinite status of the prefix.

**Definition** net\_if.h:1709

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

**Definition** net\_if.h:1130

[net\_if\_ipv6\_calc\_reachable\_time](group__net__if.md#gab1861b5cefa73b4eefbb447cb1438cdc)

uint32\_t net\_if\_ipv6\_calc\_reachable\_time(struct net\_if\_ipv6 \*ipv6)

Calculate next reachable time value for IPv6 reachable time.

[net\_if\_ipv6\_set\_base\_reachable\_time](group__net__if.md#gab3939d735b660f8f02124df656ceba2c)

static void net\_if\_ipv6\_set\_base\_reachable\_time(struct net\_if \*iface, uint32\_t reachable\_time)

Set IPv6 reachable time for a given interface.

**Definition** net\_if.h:1915

[net\_if\_ipv6\_addr\_lookup\_by\_iface](group__net__if.md#gab53eabb540a4487d83f27c8e319c736a)

struct net\_if\_addr \* net\_if\_ipv6\_addr\_lookup\_by\_iface(struct net\_if \*iface, struct in6\_addr \*addr)

Check if this IPv6 address belongs to this specific interfaces.

[net\_if\_ip\_addr\_cb\_t](group__net__if.md#gab58d8561a4f21899e2db34043d346516)

void(\* net\_if\_ip\_addr\_cb\_t)(struct net\_if \*iface, struct net\_if\_addr \*addr, void \*user\_data)

Callback used while iterating over network interface IP addresses.

**Definition** net\_if.h:1486

[net\_if\_ipv6\_maddr\_foreach](group__net__if.md#gab677496fb2e27be2df299a346e9c7132)

void net\_if\_ipv6\_maddr\_foreach(struct net\_if \*iface, net\_if\_ip\_maddr\_cb\_t cb, void \*user\_data)

Go through all IPv6 multicast addresses on a network interface and call callback for each used addres...

[net\_if\_flag\_test\_and\_clear](group__net__if.md#gab8f371c7f8890cf4728177f6595141d7)

static bool net\_if\_flag\_test\_and\_clear(struct net\_if \*iface, enum net\_if\_flag value)

Test and clear a value in network interface flags.

**Definition** net\_if.h:819

[net\_if\_start\_rs](group__net__if.md#gab9bdb7f8a9eeed4d9b70965b8af82cb7)

void net\_if\_start\_rs(struct net\_if \*iface)

Start neighbor discovery and send router solicitation message.

[net\_if\_ipv6\_maddr\_is\_joined](group__net__if.md#gabe2c16a378a35a22d008bff9142e5449)

static bool net\_if\_ipv6\_maddr\_is\_joined(struct net\_if\_mcast\_addr \*addr)

Check if given multicast address is joined or not.

**Definition** net\_if.h:1636

[net\_if\_ipv6\_addr\_rm\_by\_index](group__net__if.md#gac159e3b0fbf558d5fb09774141da7d6d)

bool net\_if\_ipv6\_addr\_rm\_by\_index(int index, const struct in6\_addr \*addr)

Remove an IPv6 address from an interface by index.

[net\_if\_cb\_t](group__net__if.md#gac48ab8e6337e7cf387af9b293f254a80)

void(\* net\_if\_cb\_t)(struct net\_if \*iface, void \*user\_data)

Callback used while iterating over network interfaces.

**Definition** net\_if.h:2795

[net\_if\_ipv4\_addr\_rm\_by\_index](group__net__if.md#gac5bf15f948ab195cecce98d1b40bda37)

bool net\_if\_ipv4\_addr\_rm\_by\_index(int index, const struct in\_addr \*addr)

Remove a IPv4 address from an interface by interface index.

[net\_if\_ipv6\_get\_global\_addr](group__net__if.md#gaca7d686c772deac13a027cc046333126)

struct in6\_addr \* net\_if\_ipv6\_get\_global\_addr(enum net\_addr\_state state, struct net\_if \*\*iface)

Return global IPv6 address from the first interface that has a global IPv6 address matching the given...

[net\_if\_get\_mtu](group__net__if.md#gacddc98531c5748db5a34f5c3a3e96e86)

static uint16\_t net\_if\_get\_mtu(struct net\_if \*iface)

Get an network interface's MTU.

**Definition** net\_if.h:1237

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

**Definition** net\_if.h:2497

[net\_if\_ipv6\_get\_ll](group__net__if.md#gad6f3e1e349e281887352652f6f32274e)

struct in6\_addr \* net\_if\_ipv6\_get\_ll(struct net\_if \*iface, enum net\_addr\_state addr\_state)

Get a IPv6 link local address in a given state.

[net\_if\_ipv6\_set\_retrans\_timer](group__net__if.md#gad74566e5a34f447d2ac63d2c0e82eeff)

static void net\_if\_ipv6\_set\_retrans\_timer(struct net\_if \*iface, uint32\_t retrans\_timer)

Set IPv6 retransmit timer for a given interface.

**Definition** net\_if.h:1990

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

**Definition** net\_if.h:1757

[net\_if\_ipv4\_maddr\_lookup](group__net__if.md#gadc1514a0d6852de9dbce043bc99d4eb0)

struct net\_if\_mcast\_addr \* net\_if\_ipv4\_maddr\_lookup(const struct in\_addr \*addr, struct net\_if \*\*iface)

Check if this IPv4 multicast address belongs to a specific interface or one of the interfaces.

[net\_if\_router\_rm](group__net__if.md#gadc87242eb7205362a308b3c4437bf76d)

void net\_if\_router\_rm(struct net\_if\_router \*router)

Remove a router from the system.

[net\_if\_ipv6\_get\_retrans\_timer](group__net__if.md#gaddbf5a6ba412e6bdb7e31568fe827bd0)

static uint32\_t net\_if\_ipv6\_get\_retrans\_timer(struct net\_if \*iface)

Get IPv6 retransmit timer specified for a given interface.

**Definition** net\_if.h:2014

[net\_if\_ipv4\_set\_gw\_by\_index](group__net__if.md#gadef49124c331817165475c69fb9104e0)

bool net\_if\_ipv4\_set\_gw\_by\_index(int index, const struct in\_addr \*gw)

Set IPv4 gateway for an interface index.

[net\_if\_ipv4\_get\_netmask\_by\_addr](group__net__if.md#gadfad7d9232bf58c5626266387a2eb761)

struct in\_addr net\_if\_ipv4\_get\_netmask\_by\_addr(struct net\_if \*iface, const struct in\_addr \*addr)

Get IPv4 netmask related to an address of an interface.

[net\_if\_oper\_state](group__net__if.md#gadfe9d90f24046cd9bd4bbee096e747b9)

net\_if\_oper\_state

Network interface operational status (RFC 2863).

**Definition** net\_if.h:288

[net\_if\_ipv6\_addr\_add](group__net__if.md#gae00484a7fe32671a4ca04ff525e640c6)

struct net\_if\_addr \* net\_if\_ipv6\_addr\_add(struct net\_if \*iface, struct in6\_addr \*addr, enum net\_addr\_type addr\_type, uint32\_t vlifetime)

Add a IPv6 address to an interface.

[net\_if\_ipv6\_select\_src\_iface](group__net__if.md#gae1495ac9e743be54b8d90bd4ff4700ab)

static struct net\_if \* net\_if\_ipv6\_select\_src\_iface(const struct in6\_addr \*dst)

Get a network interface that should be used when sending IPv6 network data to destination.

**Definition** net\_if.h:2096

[net\_if\_flag\_is\_set](group__net__if.md#gae1f373ddd61c18a81481d8ddcfb12543)

static bool net\_if\_flag\_is\_set(struct net\_if \*iface, enum net\_if\_flag value)

Check if a value in network interface flags is set.

**Definition** net\_if.h:836

[net\_if\_config\_get](group__net__if.md#gae2323a72714e29836d8296dfc330f7fd)

static struct net\_if\_config \* net\_if\_config\_get(struct net\_if \*iface)

Get network interface IP config.

**Definition** net\_if.h:1305

[net\_if\_get\_config](group__net__if.md#gae271e0e4dcb031a83d9908e597a45048)

static struct net\_if\_config \* net\_if\_get\_config(struct net\_if \*iface)

Return network configuration for this network interface.

**Definition** net\_if.h:1093

[net\_if\_ipv4\_maddr\_join](group__net__if.md#gae275a5e75817aa178d36f422573ad76a)

void net\_if\_ipv4\_maddr\_join(struct net\_if \*iface, struct net\_if\_mcast\_addr \*addr)

Mark a given multicast address to be joined.

[net\_if\_ipv4\_get\_gw](group__net__if.md#gae42f6f9620e40e2d2b36d30e81bb82d9)

struct in\_addr net\_if\_ipv4\_get\_gw(struct net\_if \*iface)

Get IPv4 gateway of an interface.

[net\_if\_addr\_set\_lf](group__net__if.md#gae66f6e7bd31545e6161fcd4600fe5842)

static void net\_if\_addr\_set\_lf(struct net\_if\_addr \*ifaddr, bool is\_infinite)

Set the infinite status of the network interface address.

**Definition** net\_if.h:1272

[net\_if\_flag](group__net__if.md#gae691e5537917ffce27ad0db82c730371)

net\_if\_flag

Network interface flags.

**Definition** net\_if.h:230

[net\_if\_ipv4\_maddr\_foreach](group__net__if.md#gae82f53c670f602e9c37b65abb6dfaec7)

void net\_if\_ipv4\_maddr\_foreach(struct net\_if \*iface, net\_if\_ip\_maddr\_cb\_t cb, void \*user\_data)

Go through all IPv4 multicast addresses on a network interface and call callback for each used addres...

[net\_if\_ipv6\_prefix\_get](group__net__if.md#gae9f98dff661d52c5e3e5e185f0ed9cc0)

struct net\_if\_ipv6\_prefix \* net\_if\_ipv6\_prefix\_get(struct net\_if \*iface, const struct in6\_addr \*addr)

Return prefix that corresponds to this IPv6 address.

[net\_if\_get\_device](group__net__if.md#gaeb8c703f273bc07ae9bb7a0d8bfe6f3d)

static const struct device \* net\_if\_get\_device(struct net\_if \*iface)

Get an network interface's device.

**Definition** net\_if.h:944

[net\_if\_is\_offloaded](group__net__if.md#gaecedc93a6dab2c57fe686718ea4d78af)

bool net\_if\_is\_offloaded(struct net\_if \*iface)

Return offload status of a given network interface.

[net\_socket\_create\_t](group__net__if.md#gaef3dfe26195514aac625e9f22e399759)

int(\* net\_socket\_create\_t)(int, int, int)

A function prototype to create an offloaded socket.

**Definition** net\_if.h:618

[net\_if\_ipv6\_addr\_update\_lifetime](group__net__if.md#gaef8a6752a201f81636c4ffc1ebba4a25)

void net\_if\_ipv6\_addr\_update\_lifetime(struct net\_if\_addr \*ifaddr, uint32\_t vlifetime)

Update validity lifetime time of an IPv6 address.

[net\_if\_ipv6\_maddr\_rm](group__net__if.md#gaf0ce126bb5019ff5f5ff0876b9712ad9)

bool net\_if\_ipv6\_maddr\_rm(struct net\_if \*iface, const struct in6\_addr \*addr)

Remove an IPv6 multicast address from an interface.

[net\_if\_is\_socket\_offloaded](group__net__if.md#gaf308baf2241fa455b50b439b7fab3f1e)

static bool net\_if\_is\_socket\_offloaded(struct net\_if \*iface)

Return the socket offload status.

**Definition** net\_if.h:1016

[net\_if\_ipv6\_set\_mcast\_hop\_limit](group__net__if.md#gaf56a433679ea9701cf8baa3208f8ccc3)

static void net\_if\_ipv6\_set\_mcast\_hop\_limit(struct net\_if \*iface, uint8\_t hop\_limit)

Set the default IPv6 multicast hop limit of a given interface.

**Definition** net\_if.h:1901

[net\_if\_get\_wifi\_sap](group__net__if.md#gaf830eab616191009d88f58b761694b49)

struct net\_if \* net\_if\_get\_wifi\_sap(void)

Get first Wi-Fi network Soft-AP interface.

[net\_if\_set\_promisc](group__net__if.md#gaf9f81f3b9697ca47f7674d85f37a8d80)

static int net\_if\_set\_promisc(struct net\_if \*iface)

Set network interface into promiscuous mode.

**Definition** net\_if.h:3008

[net\_if\_l2](group__net__if.md#gafa451f6118529d1d084704d00b2aae20)

static const struct net\_l2 \* net\_if\_l2(struct net\_if \*iface)

Get a pointer to the interface L2.

**Definition** net\_if.h:903

[net\_if\_socket\_offload](group__net__if.md#gafb2bbaec96c4759d920b2866c0b3ef3a)

static net\_socket\_create\_t net\_if\_socket\_offload(struct net\_if \*iface)

Return the function to create an offloaded socket.

**Definition** net\_if.h:1057

[net\_if\_ipv4\_select\_src\_iface](group__net__if.md#gafea1a35f452ad8168855852cbfdf0024)

static struct net\_if \* net\_if\_ipv4\_select\_src\_iface(const struct in\_addr \*dst)

Get a network interface that should be used when sending IPv4 network data to destination.

**Definition** net\_if.h:2473

[net\_if\_flag\_clear](group__net__if.md#gaff751b6a92b0c608ecfc50e8c0587fd3)

static void net\_if\_flag\_clear(struct net\_if \*iface, enum net\_if\_flag value)

Clear a value in network interface flags.

**Definition** net\_if.h:802

[NET\_IF\_CHECKSUM\_IPV4\_ICMP](group__net__if.md#gga8db412ae79c64cafe81a66f5acb2f8e9a2aef87c97f22fdccdf1925d2687436b1)

@ NET\_IF\_CHECKSUM\_IPV4\_ICMP

Interface supports checksum calculation for ICMP4 payload in IPv4.

**Definition** net\_if.h:2727

[NET\_IF\_CHECKSUM\_IPV6\_TCP](group__net__if.md#gga8db412ae79c64cafe81a66f5acb2f8e9a31e33593e4e7f7f9b36e319e0991ab13)

@ NET\_IF\_CHECKSUM\_IPV6\_TCP

Interface supports checksum calculation for TCP payload in IPv6.

**Definition** net\_if.h:2731

[NET\_IF\_CHECKSUM\_IPV6\_UDP](group__net__if.md#gga8db412ae79c64cafe81a66f5acb2f8e9a70b1272e2125cea9204bae144fd86660)

@ NET\_IF\_CHECKSUM\_IPV6\_UDP

Interface supports checksum calculation for UDP payload in IPv6.

**Definition** net\_if.h:2734

[NET\_IF\_CHECKSUM\_IPV4\_HEADER](group__net__if.md#gga8db412ae79c64cafe81a66f5acb2f8e9a75e4a0946d0e6755ebd7cc62558aee30)

@ NET\_IF\_CHECKSUM\_IPV4\_HEADER

Interface supports IP version 4 header checksum calculation.

**Definition** net\_if.h:2719

[NET\_IF\_CHECKSUM\_IPV4\_TCP](group__net__if.md#gga8db412ae79c64cafe81a66f5acb2f8e9aaed32a3cb700eac3b67c6c7e5a0cd0ad)

@ NET\_IF\_CHECKSUM\_IPV4\_TCP

Interface supports checksum calculation for TCP payload in IPv4.

**Definition** net\_if.h:2721

[NET\_IF\_CHECKSUM\_IPV6\_HEADER](group__net__if.md#gga8db412ae79c64cafe81a66f5acb2f8e9ab204c7d5fddbd2c11e07a8831df6c00b)

@ NET\_IF\_CHECKSUM\_IPV6\_HEADER

Interface supports IP version 6 header checksum calculation.

**Definition** net\_if.h:2729

[NET\_IF\_CHECKSUM\_IPV6\_ICMP](group__net__if.md#gga8db412ae79c64cafe81a66f5acb2f8e9af5b3bc7cb5e9771cd9fd57d9fda4c3b3)

@ NET\_IF\_CHECKSUM\_IPV6\_ICMP

Interface supports checksum calculation for ICMP6 payload in IPv6.

**Definition** net\_if.h:2737

[NET\_IF\_CHECKSUM\_IPV4\_UDP](group__net__if.md#gga8db412ae79c64cafe81a66f5acb2f8e9afe1eaaa765c8ec3c61618e943cd3f1c3)

@ NET\_IF\_CHECKSUM\_IPV4\_UDP

Interface supports checksum calculation for UDP payload in IPv4.

**Definition** net\_if.h:2724

[NET\_IF\_OPER\_TESTING](group__net__if.md#ggadfe9d90f24046cd9bd4bbee096e747b9a2240173b5c247ab5eb0a9a6afafb296f)

@ NET\_IF\_OPER\_TESTING

Training mode.

**Definition** net\_if.h:293

[NET\_IF\_OPER\_DORMANT](group__net__if.md#ggadfe9d90f24046cd9bd4bbee096e747b9a5cbe2aa27a444444d4acf122113d430d)

@ NET\_IF\_OPER\_DORMANT

Waiting external action.

**Definition** net\_if.h:294

[NET\_IF\_OPER\_UP](group__net__if.md#ggadfe9d90f24046cd9bd4bbee096e747b9a6b99bfc28d831292029761d74209ee03)

@ NET\_IF\_OPER\_UP

Interface is up.

**Definition** net\_if.h:295

[NET\_IF\_OPER\_NOTPRESENT](group__net__if.md#ggadfe9d90f24046cd9bd4bbee096e747b9a8f9f55840e75693163197baae9d50c32)

@ NET\_IF\_OPER\_NOTPRESENT

Hardware missing.

**Definition** net\_if.h:290

[NET\_IF\_OPER\_UNKNOWN](group__net__if.md#ggadfe9d90f24046cd9bd4bbee096e747b9ac7cae092ea6ceeb62499a9b435ac4b58)

@ NET\_IF\_OPER\_UNKNOWN

Initial (unknown) value.

**Definition** net\_if.h:289

[NET\_IF\_OPER\_DOWN](group__net__if.md#ggadfe9d90f24046cd9bd4bbee096e747b9adb20a95215310c420f8dae7e17a2f367)

@ NET\_IF\_OPER\_DOWN

Interface is down.

**Definition** net\_if.h:291

[NET\_IF\_OPER\_LOWERLAYERDOWN](group__net__if.md#ggadfe9d90f24046cd9bd4bbee096e747b9ae7e9b8b12ae618a5ee1483dee916aab4)

@ NET\_IF\_OPER\_LOWERLAYERDOWN

Lower layer interface is down.

**Definition** net\_if.h:292

[NET\_IF\_NO\_AUTO\_START](group__net__if.md#ggae691e5537917ffce27ad0db82c730371a0babb762301878eaf8ef8a05213ecf05)

@ NET\_IF\_NO\_AUTO\_START

Do not start the interface immediately after initialization.

**Definition** net\_if.h:246

[NET\_IF\_IPV6\_NO\_MLD](group__net__if.md#ggae691e5537917ffce27ad0db82c730371a1d362cfabb58eb220ddb069431221fbe)

@ NET\_IF\_IPV6\_NO\_MLD

IPv6 Multicast Listener Discovery disabled.

**Definition** net\_if.h:276

[NET\_IF\_POINTOPOINT](group__net__if.md#ggae691e5537917ffce27ad0db82c730371a3256ef2d537c85b4c2b33b92935e1009)

@ NET\_IF\_POINTOPOINT

Interface is pointopoint.

**Definition** net\_if.h:235

[NET\_IF\_IPV6\_NO\_ND](group__net__if.md#ggae691e5537917ffce27ad0db82c730371a542ecce860ef3bf2df493da8d4c6a2f7)

@ NET\_IF\_IPV6\_NO\_ND

IPv6 Neighbor Discovery disabled.

**Definition** net\_if.h:273

[NET\_IF\_FORWARD\_MULTICASTS](group__net__if.md#ggae691e5537917ffce27ad0db82c730371a581971c9d93a910c4c607da45aa2e4ac)

@ NET\_IF\_FORWARD\_MULTICASTS

Flag defines if received multicasts of other interface are forwarded on this interface.

**Definition** net\_if.h:255

[NET\_IF\_IPV4](group__net__if.md#ggae691e5537917ffce27ad0db82c730371a67d2c0fe390ab16f347ee2dc0a056329)

@ NET\_IF\_IPV4

Interface supports IPv4.

**Definition** net\_if.h:258

[NET\_IF\_PROMISC](group__net__if.md#ggae691e5537917ffce27ad0db82c730371a700d92a5b0de3c779e59806137b35141)

@ NET\_IF\_PROMISC

Interface is in promiscuous mode.

**Definition** net\_if.h:238

[NET\_IF\_DORMANT](group__net__if.md#ggae691e5537917ffce27ad0db82c730371a7dd1db72a37b1fbc4c4491ce1c75238d)

@ NET\_IF\_DORMANT

Driver signals dormant.

**Definition** net\_if.h:270

[NET\_IF\_SUSPENDED](group__net__if.md#ggae691e5537917ffce27ad0db82c730371aaaeafc62e61ec120609205770c8b54f0)

@ NET\_IF\_SUSPENDED

Power management specific: interface is being suspended.

**Definition** net\_if.h:249

[NET\_IF\_IPV6](group__net__if.md#ggae691e5537917ffce27ad0db82c730371aab31a9e1e8c02159f45efc4e0455a4d6)

@ NET\_IF\_IPV6

Interface supports IPv6.

**Definition** net\_if.h:261

[NET\_IF\_UP](group__net__if.md#ggae691e5537917ffce27ad0db82c730371ab0ab7393d643354c46c3437d74c15840)

@ NET\_IF\_UP

Interface is admin up.

**Definition** net\_if.h:232

[NET\_IF\_LOWER\_UP](group__net__if.md#ggae691e5537917ffce27ad0db82c730371ab1a529826bad6b4bcd04185372f97d6d)

@ NET\_IF\_LOWER\_UP

Driver signals L1 is up.

**Definition** net\_if.h:267

[NET\_IF\_RUNNING](group__net__if.md#ggae691e5537917ffce27ad0db82c730371add3e2ecdcd5de3154f9bd2836428a25a)

@ NET\_IF\_RUNNING

Interface up and running (ready to receive and transmit).

**Definition** net\_if.h:264

[NET\_IF\_NO\_TX\_LOCK](group__net__if.md#ggae691e5537917ffce27ad0db82c730371ae8d564e1577c8daad8ce50a729c500c9)

@ NET\_IF\_NO\_TX\_LOCK

Mutex locking on TX data path disabled on the interface.

**Definition** net\_if.h:279

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

**Definition** parser.h:96

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

**Definition** device.h:412

[in6\_addr](structin6__addr.md)

IPv6 address struct.

**Definition** net\_ip.h:142

[in\_addr](structin__addr.md)

IPv4 address struct.

**Definition** net\_ip.h:154

[k\_fifo](structk__fifo.md)

**Definition** kernel.h:2468

[k\_mutex](structk__mutex.md)

Mutex Structure.

**Definition** kernel.h:2994

[k\_thread](structk__thread.md)

Thread Structure.

**Definition** thread.h:259

[k\_timepoint\_t](structk__timepoint__t.md)

Kernel timepoint type.

**Definition** sys\_clock.h:219

[net\_dhcpv6\_params](structnet__dhcpv6__params.md)

DHCPv6 client configuration parameters.

**Definition** dhcpv6.h:63

[net\_if\_addr\_ipv4](structnet__if__addr__ipv4.md)

Network Interface unicast IPv4 address and netmask.

**Definition** net\_if.h:439

[net\_if\_addr\_ipv4::ipv4](structnet__if__addr__ipv4.md#a9d8924e263cc7401569c934533a04b48)

struct net\_if\_addr ipv4

IPv4 address.

**Definition** net\_if.h:441

[net\_if\_addr\_ipv4::netmask](structnet__if__addr__ipv4.md#ae1720720e7e36ccf38d0b282d3150774)

struct in\_addr netmask

Netmask.

**Definition** net\_if.h:443

[net\_if\_addr](structnet__if__addr.md)

Network Interface unicast IP addresses.

**Definition** net\_if.h:54

[net\_if\_addr::address](structnet__if__addr.md#a06b8d2e8b5ea6d8d671800d966163763)

struct net\_addr address

IP address.

**Definition** net\_if.h:56

[net\_if\_addr::is\_mesh\_local](structnet__if__addr.md#a1db7cc6c7566baf9340dab6771ca5010)

uint8\_t is\_mesh\_local

Is this IP address usage limited to the subnet (mesh) or not.

**Definition** net\_if.h:130

[net\_if\_addr::is\_temporary](structnet__if__addr.md#a1dd933a37afcb7d708cd602911c38e0a)

uint8\_t is\_temporary

Is this IP address temporary and generated for example by IPv6 privacy extension (RFC 8981).

**Definition** net\_if.h:135

[net\_if\_addr::addr\_state](structnet__if__addr.md#a3106fdcf0dd2479c95efafc586217a2c)

enum net\_addr\_state addr\_state

What is the current state of the address.

**Definition** net\_if.h:71

[net\_if\_addr::is\_infinite](structnet__if__addr.md#a6e799428eb0633a25e4dc3c55e3a3b8c)

uint8\_t is\_infinite

Is the IP address valid forever.

**Definition** net\_if.h:124

[net\_if\_addr::atomic\_ref](structnet__if__addr.md#a9abaf23ec98b22d1741bae410a1f7f3e)

atomic\_t atomic\_ref

Reference counter.

**Definition** net\_if.h:61

[net\_if\_addr::addr\_type](structnet__if__addr.md#ab4fd41001cc24615803bfabb9d48e7eb)

enum net\_addr\_type addr\_type

How the IP address was set.

**Definition** net\_if.h:68

[net\_if\_addr::is\_used](structnet__if__addr.md#aed4d91ba064d24ad0d53c0960cde0352)

uint8\_t is\_used

Is this IP address used or not.

**Definition** net\_if.h:127

[net\_if\_config](structnet__if__config.md)

IP and other configuration related data for network interface.

**Definition** net\_if.h:557

[net\_if\_dev](structnet__if__dev.md)

Network Interface Device structure.

**Definition** net\_if.h:634

[net\_if\_dev::oper\_state](structnet__if__dev.md#a30eabb2ffae082d0de81a50c510738a3)

enum net\_if\_oper\_state oper\_state

RFC 2863 operational status.

**Definition** net\_if.h:670

[net\_if\_dev::l2](structnet__if__dev.md#a85d713c62875f5fe9e3ec29773150797)

const struct net\_l2 \*const l2

Interface's L2 layer.

**Definition** net\_if.h:639

[net\_if\_dev::l2\_data](structnet__if__dev.md#a8fec6a7f612fc1268ef486d8bdebe018)

void \* l2\_data

Interface's private L2 data pointer.

**Definition** net\_if.h:642

[net\_if\_dev::mtu](structnet__if__dev.md#aa15ccca2eb67b8d2afca153ccacb3742)

uint16\_t mtu

The hardware MTU.

**Definition** net\_if.h:660

[net\_if\_dev::dev](structnet__if__dev.md#aab633a44f165f571910dc9fc9e131c50)

const struct device \* dev

The actually device driver instance the net\_if is related to.

**Definition** net\_if.h:636

[net\_if\_dev::link\_addr](structnet__if__dev.md#aac6d5d341ab520e6aac7f7b03737c197)

struct net\_linkaddr link\_addr

The hardware link address.

**Definition** net\_if.h:648

[net\_if\_dev::flags](structnet__if__dev.md#ac8f9c30e1dea05c28c88d3b367b130f5)

atomic\_t flags[ATOMIC\_BITMAP\_SIZE(NET\_IF\_NUM\_FLAGS)]

For internal use.

**Definition** net\_if.h:645

[net\_if\_ip](structnet__if__ip.md)

Network interface IP address configuration.

**Definition** net\_if.h:544

[net\_if\_ipv4](structnet__if__ipv4.md)

IPv4 configuration.

**Definition** net\_if.h:447

[net\_if\_ipv4::mcast\_ttl](structnet__if__ipv4.md#a7e9bf16d51989cfcfe564f4f0a43b480)

uint8\_t mcast\_ttl

IPv4 time-to-live for multicast packets.

**Definition** net\_if.h:461

[net\_if\_ipv4::unicast](structnet__if__ipv4.md#a806cf92123452ed3aa93540803b0a8d3)

struct net\_if\_addr\_ipv4 unicast[NET\_IF\_MAX\_IPV4\_ADDR]

Unicast IP addresses.

**Definition** net\_if.h:449

[net\_if\_ipv4::gw](structnet__if__ipv4.md#aa24772c7202bf465ee3da94a172b7bcb)

struct in\_addr gw

Gateway.

**Definition** net\_if.h:455

[net\_if\_ipv4::ttl](structnet__if__ipv4.md#acdc6d5d6eb5362f4f6d2c027cc40e684)

uint8\_t ttl

IPv4 time-to-live.

**Definition** net\_if.h:458

[net\_if\_ipv4::mcast](structnet__if__ipv4.md#adfaf5b50255bd35297195a7218729ae7)

struct net\_if\_mcast\_addr mcast[NET\_IF\_MAX\_IPV4\_MADDR]

Multicast IP addresses.

**Definition** net\_if.h:452

[net\_if\_ipv6\_prefix](structnet__if__ipv6__prefix.md)

Network Interface IPv6 prefixes.

**Definition** net\_if.h:174

[net\_if\_ipv6\_prefix::iface](structnet__if__ipv6__prefix.md#a0e2d1997e2ccfe1e1af5f16e0c74ed92)

struct net\_if \* iface

Backpointer to network interface where this prefix is used.

**Definition** net\_if.h:182

[net\_if\_ipv6\_prefix::is\_infinite](structnet__if__ipv6__prefix.md#a22090441b27bed06098679bf23b4e1e9)

uint8\_t is\_infinite

Is the IP prefix valid forever.

**Definition** net\_if.h:188

[net\_if\_ipv6\_prefix::len](structnet__if__ipv6__prefix.md#a4d2bc2acbe51256b76cf4d3ced3aac39)

uint8\_t len

Prefix length.

**Definition** net\_if.h:185

[net\_if\_ipv6\_prefix::prefix](structnet__if__ipv6__prefix.md#a65b450d0942b3c96cfc575b462d82028)

struct in6\_addr prefix

IPv6 prefix.

**Definition** net\_if.h:179

[net\_if\_ipv6\_prefix::is\_used](structnet__if__ipv6__prefix.md#a6a4295256957e5eddf149f1ceff62e3f)

uint8\_t is\_used

Is this prefix used or not.

**Definition** net\_if.h:191

[net\_if\_ipv6\_prefix::lifetime](structnet__if__ipv6__prefix.md#a925a97a49d383bd4ce475f5d09fcb7e3)

struct net\_timeout lifetime

Prefix lifetime.

**Definition** net\_if.h:176

[net\_if\_ipv6](structnet__if__ipv6.md)

IPv6 configuration.

**Definition** net\_if.h:315

[net\_if\_ipv6::prefix](structnet__if__ipv6.md#a2dccdc984f08527302d8d910a2658f72)

struct net\_if\_ipv6\_prefix prefix[NET\_IF\_MAX\_IPV6\_PREFIX]

Prefixes.

**Definition** net\_if.h:323

[net\_if\_ipv6::base\_reachable\_time](structnet__if__ipv6.md#a500a78fe23ee2ebc63f3d3b53b5b92ea)

uint32\_t base\_reachable\_time

Default reachable time (RFC 4861, page 52).

**Definition** net\_if.h:326

[net\_if\_ipv6::hop\_limit](structnet__if__ipv6.md#a71775a082984274fbc7c009ead18e751)

uint8\_t hop\_limit

IPv6 hop limit.

**Definition** net\_if.h:354

[net\_if\_ipv6::mcast](structnet__if__ipv6.md#a727d2773e0dee3be687dda5b2dd55682)

struct net\_if\_mcast\_addr mcast[NET\_IF\_MAX\_IPV6\_MADDR]

Multicast IP addresses.

**Definition** net\_if.h:320

[net\_if\_ipv6::retrans\_timer](structnet__if__ipv6.md#ac5ee47ff9d3e429ecbb8623e5d713246)

uint32\_t retrans\_timer

Retransmit timer (RFC 4861, page 52).

**Definition** net\_if.h:332

[net\_if\_ipv6::unicast](structnet__if__ipv6.md#adb6431d336cc3f46972e13d2255452c8)

struct net\_if\_addr unicast[NET\_IF\_MAX\_IPV6\_ADDR]

Unicast IP addresses.

**Definition** net\_if.h:317

[net\_if\_ipv6::mcast\_hop\_limit](structnet__if__ipv6.md#ae94906c28578f2e1ea2506b0e2972d4c)

uint8\_t mcast\_hop\_limit

IPv6 multicast hop limit.

**Definition** net\_if.h:357

[net\_if\_ipv6::reachable\_time](structnet__if__ipv6.md#af57b7dca189167f8cc757c4ed6b08f2f)

uint32\_t reachable\_time

Reachable time (RFC 4861, page 20).

**Definition** net\_if.h:329

[net\_if\_link\_cb](structnet__if__link__cb.md)

Link callback handler struct.

**Definition** net\_if.h:2663

[net\_if\_link\_cb::cb](structnet__if__link__cb.md#a66092a22cba3dd69ac1a91c3522240bb)

net\_if\_link\_callback\_t cb

Link callback.

**Definition** net\_if.h:2668

[net\_if\_link\_cb::node](structnet__if__link__cb.md#accae7945a802c5b7fc36948b12a365ef)

sys\_snode\_t node

Node information for the slist.

**Definition** net\_if.h:2665

[net\_if\_mcast\_addr](structnet__if__mcast__addr.md)

Network Interface multicast IP addresses.

**Definition** net\_if.h:145

[net\_if\_mcast\_addr::address](structnet__if__mcast__addr.md#a3e470fc2eb02ac9e5d3d7d0bea0aaa69)

struct net\_addr address

IP address.

**Definition** net\_if.h:147

[net\_if\_mcast\_addr::is\_joined](structnet__if__mcast__addr.md#a4af9009b2f9ccc0589a9ba6dac10927b)

uint8\_t is\_joined

Did we join to this group.

**Definition** net\_if.h:164

[net\_if\_mcast\_addr::is\_used](structnet__if__mcast__addr.md#abab3e6dba72e24ef522c033d277369ca)

uint8\_t is\_used

Is this multicast IP address used or not.

**Definition** net\_if.h:161

[net\_if\_mcast\_monitor](structnet__if__mcast__monitor.md)

Multicast monitor handler struct.

**Definition** net\_if.h:1580

[net\_if\_mcast\_monitor::node](structnet__if__mcast__monitor.md#a570b7d8a8a5fabca83982a5f7d1d896a)

sys\_snode\_t node

Node information for the slist.

**Definition** net\_if.h:1582

[net\_if\_mcast\_monitor::cb](structnet__if__mcast__monitor.md#aec441b858a5f6792ac9cdbc625f6babe)

net\_if\_mcast\_callback\_t cb

Multicast callback.

**Definition** net\_if.h:1588

[net\_if\_mcast\_monitor::iface](structnet__if__mcast__monitor.md#af4d0e937b2b9161918a13a0d6723c60a)

struct net\_if \* iface

Network interface.

**Definition** net\_if.h:1585

[net\_if\_router](structnet__if__router.md)

Information about routers in the system.

**Definition** net\_if.h:201

[net\_if\_router::iface](structnet__if__router.md#a03789aa0a40f7686b76616de0ca0401a)

struct net\_if \* iface

Network interface the router is connected to.

**Definition** net\_if.h:209

[net\_if\_router::is\_default](structnet__if__router.md#a34745207edcad2745d6ce311e2bf1894)

uint8\_t is\_default

Is default router.

**Definition** net\_if.h:221

[net\_if\_router::lifetime](structnet__if__router.md#a4b0d2ad8f225ab61022c10dfce3db199)

uint16\_t lifetime

Router lifetime.

**Definition** net\_if.h:215

[net\_if\_router::is\_infinite](structnet__if__router.md#a4cb47f30241ae3d410f56f1487254ed0)

uint8\_t is\_infinite

Is the router valid forever.

**Definition** net\_if.h:224

[net\_if\_router::is\_used](structnet__if__router.md#a7196e6d2bc2c958d98dfe29143a62048)

uint8\_t is\_used

Is this router used or not.

**Definition** net\_if.h:218

[net\_if\_router::address](structnet__if__router.md#a86a2ca1b95e348acbde8ce90986b83db)

struct net\_addr address

IP address.

**Definition** net\_if.h:206

[net\_if\_router::node](structnet__if__router.md#aabbac0cd0a59ca0eafdcfc0eaf5d909a)

sys\_snode\_t node

Slist lifetime timer node.

**Definition** net\_if.h:203

[net\_if\_router::life\_start](structnet__if__router.md#adf4f4c722917b3c30f8c73bc2519957f)

uint32\_t life\_start

Router life timer start.

**Definition** net\_if.h:212

[net\_if](structnet__if.md)

Network Interface structure.

**Definition** net\_if.h:680

[net\_if::if\_dev](structnet__if.md#a0982ba2019cdaa7701162e60fdb2171e)

struct net\_if\_dev \* if\_dev

The net\_if\_dev instance the net\_if is related to.

**Definition** net\_if.h:682

[net\_if::config](structnet__if.md#a5e71962f55bdead7bfbbb96518c6c404)

struct net\_if\_config config

Network interface instance configuration.

**Definition** net\_if.h:690

[net\_if::pe\_enabled](structnet__if.md#aa96a6a2d55f6a4ece2f340eef526ef56)

uint8\_t pe\_enabled

Network interface specific flags.

**Definition** net\_if.h:710

[net\_if::lock](structnet__if.md#ace2233b71da53ff0fc7cd564ccfc5a03)

struct k\_mutex lock

Mutex protecting this network interface instance.

**Definition** net\_if.h:701

[net\_if::pe\_prefer\_public](structnet__if.md#aec585e283c9053443ff05b364acf76eb)

uint8\_t pe\_prefer\_public

If PE is enabled, then this tells whether public addresses are preferred over temporary ones for this...

**Definition** net\_if.h:715

[net\_if::tx\_lock](structnet__if.md#af00f729ebddfdcf725169f61b6cd586b)

struct k\_mutex tx\_lock

Mutex used when sending data.

**Definition** net\_if.h:704

[net\_l2](structnet__l2.md)

Network L2 structure.

**Definition** net\_l2.h:57

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

**Definition** net\_stats.h:339

[net\_timeout](structnet__timeout.md)

Generic struct for handling network timeouts.

**Definition** net\_timeout.h:57

[net\_traffic\_class](structnet__traffic__class.md)

Network traffic class.

**Definition** net\_if.h:601

[net\_traffic\_class::stack](structnet__traffic__class.md#a2d98bc68d38bdef649d645b8b52516c5)

k\_thread\_stack\_t \* stack

Stack for this handler.

**Definition** net\_if.h:609

[net\_traffic\_class::handler](structnet__traffic__class.md#a8d0023588fee0a8ff1381bbc80ada143)

struct k\_thread handler

Traffic class handler thread.

**Definition** net\_if.h:606

[net\_traffic\_class::fifo](structnet__traffic__class.md#a94511ca12bad1687f5c7ca862c857ded)

struct k\_fifo fifo

Fifo for handling this Tx or Rx packet.

**Definition** net\_if.h:603

[sockaddr](structsockaddr.md)

Generic sockaddr struct.

**Definition** net\_ip.h:388

[iterable\_sections.h](sys_2iterable__sections_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [net\_if.h](net__if_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
