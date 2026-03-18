---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/net__if_8h_source.html
original_path: doxygen/html/net__if_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
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

[ 59](structnet__if__addr.md#a9abaf23ec98b22d1741bae410a1f7f3e) [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) [atomic\_ref](structnet__if__addr.md#a9abaf23ec98b22d1741bae410a1f7f3e);

60

61#if defined(CONFIG\_NET\_NATIVE\_IPV6)

62 struct [net\_timeout](structnet__timeout.md) lifetime;

63#endif

64

[ 66](structnet__if__addr.md#ab4fd41001cc24615803bfabb9d48e7eb) enum [net\_addr\_type](group__ip__4__6.md#gafecee2d4a331dc85ad962b81a6303e41) [addr\_type](structnet__if__addr.md#ab4fd41001cc24615803bfabb9d48e7eb);

67

[ 69](structnet__if__addr.md#a3106fdcf0dd2479c95efafc586217a2c) enum [net\_addr\_state](group__ip__4__6.md#ga32e58fc83532ef57eeb6ff952f17288d) [addr\_state](structnet__if__addr.md#a3106fdcf0dd2479c95efafc586217a2c);

70

71#if defined(CONFIG\_NET\_NATIVE\_IPV6)

72#if defined(CONFIG\_NET\_IPV6\_PE)

76 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) addr\_create\_time;

77

80 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) addr\_preferred\_lifetime;

81

86 [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) addr\_timeout;

87#endif

88#endif /\* CONFIG\_NET\_NATIVE\_IPV6 \*/

89

90 union {

91#if defined(CONFIG\_NET\_IPV6\_DAD)

92 struct {

94 [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) dad\_node;

95 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) dad\_start;

96

98 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) dad\_count;

99 };

100#endif /\* CONFIG\_NET\_IPV6\_DAD \*/

101#if defined(CONFIG\_NET\_IPV4\_ACD)

102 struct {

104 [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) acd\_node;

105 [k\_timepoint\_t](structk__timepoint__t.md) acd\_timeout;

106

108 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) acd\_count;

109

111 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) acd\_state;

112 };

113#endif /\* CONFIG\_NET\_IPV4\_ACD \*/

114 };

115

116#if defined(CONFIG\_NET\_IPV6\_DAD) || defined(CONFIG\_NET\_IPV4\_ACD)

118 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ifindex;

119#endif

120

[ 122](structnet__if__addr.md#a6e799428eb0633a25e4dc3c55e3a3b8c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [is\_infinite](structnet__if__addr.md#a6e799428eb0633a25e4dc3c55e3a3b8c) : 1;

123

[ 125](structnet__if__addr.md#aed4d91ba064d24ad0d53c0960cde0352) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [is\_used](structnet__if__addr.md#aed4d91ba064d24ad0d53c0960cde0352) : 1;

126

[ 128](structnet__if__addr.md#a1db7cc6c7566baf9340dab6771ca5010) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [is\_mesh\_local](structnet__if__addr.md#a1db7cc6c7566baf9340dab6771ca5010) : 1;

129

[ 133](structnet__if__addr.md#a1dd933a37afcb7d708cd602911c38e0a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [is\_temporary](structnet__if__addr.md#a1dd933a37afcb7d708cd602911c38e0a) : 1;

134

135 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \_unused : 4;

136};

137

[ 143](structnet__if__mcast__addr.md)struct [net\_if\_mcast\_addr](structnet__if__mcast__addr.md) {

[ 145](structnet__if__mcast__addr.md#a3e470fc2eb02ac9e5d3d7d0bea0aaa69) struct net\_addr [address](structnet__if__mcast__addr.md#a3e470fc2eb02ac9e5d3d7d0bea0aaa69);

146

147#if defined(CONFIG\_NET\_IPV4\_IGMPV3)

149 struct net\_addr sources[CONFIG\_NET\_IF\_MCAST\_IPV4\_SOURCE\_COUNT];

150

152 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) sources\_len;

153

155 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) record\_type;

156#endif

157

[ 159](structnet__if__mcast__addr.md#abab3e6dba72e24ef522c033d277369ca) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [is\_used](structnet__if__mcast__addr.md#abab3e6dba72e24ef522c033d277369ca) : 1;

160

[ 162](structnet__if__mcast__addr.md#a4af9009b2f9ccc0589a9ba6dac10927b) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [is\_joined](structnet__if__mcast__addr.md#a4af9009b2f9ccc0589a9ba6dac10927b) : 1;

163

164 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \_unused : 6;

165};

166

[ 172](structnet__if__ipv6__prefix.md)struct [net\_if\_ipv6\_prefix](structnet__if__ipv6__prefix.md) {

[ 174](structnet__if__ipv6__prefix.md#a925a97a49d383bd4ce475f5d09fcb7e3) struct [net\_timeout](structnet__timeout.md) [lifetime](structnet__if__ipv6__prefix.md#a925a97a49d383bd4ce475f5d09fcb7e3);

175

[ 177](structnet__if__ipv6__prefix.md#a65b450d0942b3c96cfc575b462d82028) struct [in6\_addr](structin6__addr.md) [prefix](structnet__if__ipv6__prefix.md#a65b450d0942b3c96cfc575b462d82028);

178

[ 180](structnet__if__ipv6__prefix.md#a0e2d1997e2ccfe1e1af5f16e0c74ed92) struct [net\_if](structnet__if.md) \*[iface](structnet__if__ipv6__prefix.md#a0e2d1997e2ccfe1e1af5f16e0c74ed92);

181

[ 183](structnet__if__ipv6__prefix.md#a4d2bc2acbe51256b76cf4d3ced3aac39) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [len](structnet__if__ipv6__prefix.md#a4d2bc2acbe51256b76cf4d3ced3aac39);

184

[ 186](structnet__if__ipv6__prefix.md#a22090441b27bed06098679bf23b4e1e9) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [is\_infinite](structnet__if__ipv6__prefix.md#a22090441b27bed06098679bf23b4e1e9) : 1;

187

[ 189](structnet__if__ipv6__prefix.md#a6a4295256957e5eddf149f1ceff62e3f) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [is\_used](structnet__if__ipv6__prefix.md#a6a4295256957e5eddf149f1ceff62e3f) : 1;

190

191 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \_unused : 6;

192};

193

[ 199](structnet__if__router.md)struct [net\_if\_router](structnet__if__router.md) {

[ 201](structnet__if__router.md#aabbac0cd0a59ca0eafdcfc0eaf5d909a) [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) [node](structnet__if__router.md#aabbac0cd0a59ca0eafdcfc0eaf5d909a);

202

[ 204](structnet__if__router.md#a86a2ca1b95e348acbde8ce90986b83db) struct net\_addr [address](structnet__if__router.md#a86a2ca1b95e348acbde8ce90986b83db);

205

[ 207](structnet__if__router.md#a03789aa0a40f7686b76616de0ca0401a) struct [net\_if](structnet__if.md) \*[iface](structnet__if__router.md#a03789aa0a40f7686b76616de0ca0401a);

208

[ 210](structnet__if__router.md#adf4f4c722917b3c30f8c73bc2519957f) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [life\_start](structnet__if__router.md#adf4f4c722917b3c30f8c73bc2519957f);

211

[ 213](structnet__if__router.md#a4b0d2ad8f225ab61022c10dfce3db199) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [lifetime](structnet__if__router.md#a4b0d2ad8f225ab61022c10dfce3db199);

214

[ 216](structnet__if__router.md#a7196e6d2bc2c958d98dfe29143a62048) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [is\_used](structnet__if__router.md#a7196e6d2bc2c958d98dfe29143a62048) : 1;

217

[ 219](structnet__if__router.md#a34745207edcad2745d6ce311e2bf1894) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [is\_default](structnet__if__router.md#a34745207edcad2745d6ce311e2bf1894) : 1;

220

[ 222](structnet__if__router.md#a4cb47f30241ae3d410f56f1487254ed0) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [is\_infinite](structnet__if__router.md#a4cb47f30241ae3d410f56f1487254ed0) : 1;

223

224 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \_unused : 5;

225};

226

[ 228](group__net__if.md#gae691e5537917ffce27ad0db82c730371)enum [net\_if\_flag](group__net__if.md#gae691e5537917ffce27ad0db82c730371) {

[ 230](group__net__if.md#ggae691e5537917ffce27ad0db82c730371ab0ab7393d643354c46c3437d74c15840) [NET\_IF\_UP](group__net__if.md#ggae691e5537917ffce27ad0db82c730371ab0ab7393d643354c46c3437d74c15840),

231

[ 233](group__net__if.md#ggae691e5537917ffce27ad0db82c730371a3256ef2d537c85b4c2b33b92935e1009) [NET\_IF\_POINTOPOINT](group__net__if.md#ggae691e5537917ffce27ad0db82c730371a3256ef2d537c85b4c2b33b92935e1009),

234

[ 236](group__net__if.md#ggae691e5537917ffce27ad0db82c730371a700d92a5b0de3c779e59806137b35141) [NET\_IF\_PROMISC](group__net__if.md#ggae691e5537917ffce27ad0db82c730371a700d92a5b0de3c779e59806137b35141),

237

[ 244](group__net__if.md#ggae691e5537917ffce27ad0db82c730371a0babb762301878eaf8ef8a05213ecf05) [NET\_IF\_NO\_AUTO\_START](group__net__if.md#ggae691e5537917ffce27ad0db82c730371a0babb762301878eaf8ef8a05213ecf05),

245

[ 247](group__net__if.md#ggae691e5537917ffce27ad0db82c730371aaaeafc62e61ec120609205770c8b54f0) [NET\_IF\_SUSPENDED](group__net__if.md#ggae691e5537917ffce27ad0db82c730371aaaeafc62e61ec120609205770c8b54f0),

248

[ 253](group__net__if.md#ggae691e5537917ffce27ad0db82c730371a581971c9d93a910c4c607da45aa2e4ac) [NET\_IF\_FORWARD\_MULTICASTS](group__net__if.md#ggae691e5537917ffce27ad0db82c730371a581971c9d93a910c4c607da45aa2e4ac),

254

[ 256](group__net__if.md#ggae691e5537917ffce27ad0db82c730371a67d2c0fe390ab16f347ee2dc0a056329) [NET\_IF\_IPV4](group__net__if.md#ggae691e5537917ffce27ad0db82c730371a67d2c0fe390ab16f347ee2dc0a056329),

257

[ 259](group__net__if.md#ggae691e5537917ffce27ad0db82c730371aab31a9e1e8c02159f45efc4e0455a4d6) [NET\_IF\_IPV6](group__net__if.md#ggae691e5537917ffce27ad0db82c730371aab31a9e1e8c02159f45efc4e0455a4d6),

260

[ 262](group__net__if.md#ggae691e5537917ffce27ad0db82c730371add3e2ecdcd5de3154f9bd2836428a25a) [NET\_IF\_RUNNING](group__net__if.md#ggae691e5537917ffce27ad0db82c730371add3e2ecdcd5de3154f9bd2836428a25a),

263

[ 265](group__net__if.md#ggae691e5537917ffce27ad0db82c730371ab1a529826bad6b4bcd04185372f97d6d) [NET\_IF\_LOWER\_UP](group__net__if.md#ggae691e5537917ffce27ad0db82c730371ab1a529826bad6b4bcd04185372f97d6d),

266

[ 268](group__net__if.md#ggae691e5537917ffce27ad0db82c730371a7dd1db72a37b1fbc4c4491ce1c75238d) [NET\_IF\_DORMANT](group__net__if.md#ggae691e5537917ffce27ad0db82c730371a7dd1db72a37b1fbc4c4491ce1c75238d),

269

[ 271](group__net__if.md#ggae691e5537917ffce27ad0db82c730371a542ecce860ef3bf2df493da8d4c6a2f7) [NET\_IF\_IPV6\_NO\_ND](group__net__if.md#ggae691e5537917ffce27ad0db82c730371a542ecce860ef3bf2df493da8d4c6a2f7),

272

[ 274](group__net__if.md#ggae691e5537917ffce27ad0db82c730371a1d362cfabb58eb220ddb069431221fbe) [NET\_IF\_IPV6\_NO\_MLD](group__net__if.md#ggae691e5537917ffce27ad0db82c730371a1d362cfabb58eb220ddb069431221fbe),

275

[ 277](group__net__if.md#ggae691e5537917ffce27ad0db82c730371ae8d564e1577c8daad8ce50a729c500c9) [NET\_IF\_NO\_TX\_LOCK](group__net__if.md#ggae691e5537917ffce27ad0db82c730371ae8d564e1577c8daad8ce50a729c500c9),

278

280 /\* Total number of flags - must be at the end of the enum \*/

281 NET\_IF\_NUM\_FLAGS

283};

284

[ 286](group__net__if.md#gadfe9d90f24046cd9bd4bbee096e747b9)enum [net\_if\_oper\_state](group__net__if.md#gadfe9d90f24046cd9bd4bbee096e747b9) {

[ 287](group__net__if.md#ggadfe9d90f24046cd9bd4bbee096e747b9ac7cae092ea6ceeb62499a9b435ac4b58) [NET\_IF\_OPER\_UNKNOWN](group__net__if.md#ggadfe9d90f24046cd9bd4bbee096e747b9ac7cae092ea6ceeb62499a9b435ac4b58),

[ 288](group__net__if.md#ggadfe9d90f24046cd9bd4bbee096e747b9a8f9f55840e75693163197baae9d50c32) [NET\_IF\_OPER\_NOTPRESENT](group__net__if.md#ggadfe9d90f24046cd9bd4bbee096e747b9a8f9f55840e75693163197baae9d50c32),

[ 289](group__net__if.md#ggadfe9d90f24046cd9bd4bbee096e747b9adb20a95215310c420f8dae7e17a2f367) [NET\_IF\_OPER\_DOWN](group__net__if.md#ggadfe9d90f24046cd9bd4bbee096e747b9adb20a95215310c420f8dae7e17a2f367),

[ 290](group__net__if.md#ggadfe9d90f24046cd9bd4bbee096e747b9ae7e9b8b12ae618a5ee1483dee916aab4) [NET\_IF\_OPER\_LOWERLAYERDOWN](group__net__if.md#ggadfe9d90f24046cd9bd4bbee096e747b9ae7e9b8b12ae618a5ee1483dee916aab4),

[ 291](group__net__if.md#ggadfe9d90f24046cd9bd4bbee096e747b9a2240173b5c247ab5eb0a9a6afafb296f) [NET\_IF\_OPER\_TESTING](group__net__if.md#ggadfe9d90f24046cd9bd4bbee096e747b9a2240173b5c247ab5eb0a9a6afafb296f),

[ 292](group__net__if.md#ggadfe9d90f24046cd9bd4bbee096e747b9a5cbe2aa27a444444d4acf122113d430d) [NET\_IF\_OPER\_DORMANT](group__net__if.md#ggadfe9d90f24046cd9bd4bbee096e747b9a5cbe2aa27a444444d4acf122113d430d),

[ 293](group__net__if.md#ggadfe9d90f24046cd9bd4bbee096e747b9a6b99bfc28d831292029761d74209ee03) [NET\_IF\_OPER\_UP](group__net__if.md#ggadfe9d90f24046cd9bd4bbee096e747b9a6b99bfc28d831292029761d74209ee03),

294} \_\_packed;

295

296#if defined(CONFIG\_NET\_OFFLOAD)

297struct net\_offload;

298#endif /\* CONFIG\_NET\_OFFLOAD \*/

299

301#if defined(CONFIG\_NET\_NATIVE\_IPV6)

302#define NET\_IF\_MAX\_IPV6\_ADDR CONFIG\_NET\_IF\_UNICAST\_IPV6\_ADDR\_COUNT

303#define NET\_IF\_MAX\_IPV6\_MADDR CONFIG\_NET\_IF\_MCAST\_IPV6\_ADDR\_COUNT

304#define NET\_IF\_MAX\_IPV6\_PREFIX CONFIG\_NET\_IF\_IPV6\_PREFIX\_COUNT

305#else

306#define NET\_IF\_MAX\_IPV6\_ADDR 0

307#define NET\_IF\_MAX\_IPV6\_MADDR 0

308#define NET\_IF\_MAX\_IPV6\_PREFIX 0

309#endif

310/\* @endcond \*/

311

[ 313](structnet__if__ipv6.md)struct [net\_if\_ipv6](structnet__if__ipv6.md) {

[ 315](structnet__if__ipv6.md#adb6431d336cc3f46972e13d2255452c8) struct [net\_if\_addr](structnet__if__addr.md) [unicast](structnet__if__ipv6.md#adb6431d336cc3f46972e13d2255452c8)[NET\_IF\_MAX\_IPV6\_ADDR];

316

[ 318](structnet__if__ipv6.md#a727d2773e0dee3be687dda5b2dd55682) struct [net\_if\_mcast\_addr](structnet__if__mcast__addr.md) [mcast](structnet__if__ipv6.md#a727d2773e0dee3be687dda5b2dd55682)[NET\_IF\_MAX\_IPV6\_MADDR];

319

[ 321](structnet__if__ipv6.md#a2dccdc984f08527302d8d910a2658f72) struct [net\_if\_ipv6\_prefix](structnet__if__ipv6__prefix.md) [prefix](structnet__if__ipv6.md#a2dccdc984f08527302d8d910a2658f72)[NET\_IF\_MAX\_IPV6\_PREFIX];

322

[ 324](structnet__if__ipv6.md#a500a78fe23ee2ebc63f3d3b53b5b92ea) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [base\_reachable\_time](structnet__if__ipv6.md#a500a78fe23ee2ebc63f3d3b53b5b92ea);

325

[ 327](structnet__if__ipv6.md#af57b7dca189167f8cc757c4ed6b08f2f) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [reachable\_time](structnet__if__ipv6.md#af57b7dca189167f8cc757c4ed6b08f2f);

328

[ 330](structnet__if__ipv6.md#ac5ee47ff9d3e429ecbb8623e5d713246) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [retrans\_timer](structnet__if__ipv6.md#ac5ee47ff9d3e429ecbb8623e5d713246);

331

332#if defined(CONFIG\_NET\_IPV6\_PE)

337 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) desync\_factor;

338#endif /\* CONFIG\_NET\_IPV6\_PE \*/

339

340#if defined(CONFIG\_NET\_IPV6\_ND) && defined(CONFIG\_NET\_NATIVE\_IPV6)

342 [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) rs\_node;

343

344 /\* RS start time \*/

345 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) rs\_start;

346

348 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) rs\_count;

349#endif

350

[ 352](structnet__if__ipv6.md#a71775a082984274fbc7c009ead18e751) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [hop\_limit](structnet__if__ipv6.md#a71775a082984274fbc7c009ead18e751);

353

[ 355](structnet__if__ipv6.md#ae94906c28578f2e1ea2506b0e2972d4c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [mcast\_hop\_limit](structnet__if__ipv6.md#ae94906c28578f2e1ea2506b0e2972d4c);

356};

357

358#if defined(CONFIG\_NET\_DHCPV6) && defined(CONFIG\_NET\_NATIVE\_IPV6)

360struct net\_if\_dhcpv6 {

362 [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) node;

363

365 struct net\_dhcpv6\_duid\_storage clientid;

366

368 struct net\_dhcpv6\_duid\_storage serverid;

369

371 enum net\_dhcpv6\_state [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90);

372

374 struct [net\_dhcpv6\_params](structnet__dhcpv6__params.md) params;

375

377 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) timeout;

378

380 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) exchange\_start;

381

383 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) t1;

384

386 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) t2;

387

391 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) expire;

392

394 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) addr\_iaid;

395

397 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) prefix\_iaid;

398

400 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) retransmit\_timeout;

401

403 [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) server\_preference;

404

406 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) retransmissions;

407

409 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) tid[DHCPV6\_TID\_SIZE];

410

412 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) prefix\_len;

413

415 struct [in6\_addr](structin6__addr.md) prefix;

416

418 struct [in6\_addr](structin6__addr.md) addr;

419};

420#endif /\* defined(CONFIG\_NET\_DHCPV6) && defined(CONFIG\_NET\_NATIVE\_IPV6) \*/

421

423#if defined(CONFIG\_NET\_NATIVE\_IPV4)

424#define NET\_IF\_MAX\_IPV4\_ADDR CONFIG\_NET\_IF\_UNICAST\_IPV4\_ADDR\_COUNT

425#define NET\_IF\_MAX\_IPV4\_MADDR CONFIG\_NET\_IF\_MCAST\_IPV4\_ADDR\_COUNT

426#else

427#define NET\_IF\_MAX\_IPV4\_ADDR 0

428#define NET\_IF\_MAX\_IPV4\_MADDR 0

429#endif

431

[ 437](structnet__if__addr__ipv4.md)struct [net\_if\_addr\_ipv4](structnet__if__addr__ipv4.md) {

[ 439](structnet__if__addr__ipv4.md#a9d8924e263cc7401569c934533a04b48) struct [net\_if\_addr](structnet__if__addr.md) [ipv4](structnet__if__addr__ipv4.md#a9d8924e263cc7401569c934533a04b48);

[ 441](structnet__if__addr__ipv4.md#ae1720720e7e36ccf38d0b282d3150774) struct [in\_addr](structin__addr.md) [netmask](structnet__if__addr__ipv4.md#ae1720720e7e36ccf38d0b282d3150774);

442};

443

[ 445](structnet__if__ipv4.md)struct [net\_if\_ipv4](structnet__if__ipv4.md) {

[ 447](structnet__if__ipv4.md#a806cf92123452ed3aa93540803b0a8d3) struct [net\_if\_addr\_ipv4](structnet__if__addr__ipv4.md) [unicast](structnet__if__ipv4.md#a806cf92123452ed3aa93540803b0a8d3)[NET\_IF\_MAX\_IPV4\_ADDR];

448

[ 450](structnet__if__ipv4.md#adfaf5b50255bd35297195a7218729ae7) struct [net\_if\_mcast\_addr](structnet__if__mcast__addr.md) [mcast](structnet__if__ipv4.md#adfaf5b50255bd35297195a7218729ae7)[NET\_IF\_MAX\_IPV4\_MADDR];

451

[ 453](structnet__if__ipv4.md#aa24772c7202bf465ee3da94a172b7bcb) struct [in\_addr](structin__addr.md) [gw](structnet__if__ipv4.md#aa24772c7202bf465ee3da94a172b7bcb);

454

[ 456](structnet__if__ipv4.md#acdc6d5d6eb5362f4f6d2c027cc40e684) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [ttl](structnet__if__ipv4.md#acdc6d5d6eb5362f4f6d2c027cc40e684);

457

[ 459](structnet__if__ipv4.md#a7e9bf16d51989cfcfe564f4f0a43b480) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [mcast\_ttl](structnet__if__ipv4.md#a7e9bf16d51989cfcfe564f4f0a43b480);

460

461#if defined(CONFIG\_NET\_IPV4\_ACD)

463 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) conflict\_cnt;

464#endif

465};

466

467#if defined(CONFIG\_NET\_DHCPV4) && defined(CONFIG\_NET\_NATIVE\_IPV4)

468struct net\_if\_dhcpv4 {

470 [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) node;

471

473 [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) timer\_start;

474

476 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) request\_time;

477

478 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) xid;

479

481 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) lease\_time;

482

484 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) renewal\_time;

485

487 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) rebinding\_time;

488

490 struct [in\_addr](structin__addr.md) server\_id;

491

493 struct [in\_addr](structin__addr.md) requested\_ip;

494

496 struct [in\_addr](structin__addr.md) netmask;

497

502 enum net\_dhcpv4\_state [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90);

503

505 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) attempts;

506

508 struct [in\_addr](structin__addr.md) request\_server\_addr;

509

511 struct [in\_addr](structin__addr.md) response\_src\_addr;

512

513#ifdef CONFIG\_NET\_DHCPV4\_OPTION\_NTP\_SERVER

515 struct [in\_addr](structin__addr.md) ntp\_addr;

516#endif

517};

518#endif /\* CONFIG\_NET\_DHCPV4 \*/

519

520#if defined(CONFIG\_NET\_IPV4\_AUTO) && defined(CONFIG\_NET\_NATIVE\_IPV4)

521struct net\_if\_ipv4\_autoconf {

523 struct net\_if \*iface;

524

526 struct in\_addr requested\_ip;

527

530 enum [net\_ipv4\_autoconf\_state](ipv4__autoconf_8h.md#abdf8bb08f12768aad2ff95b902bdc899) [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90);

531};

532#endif /\* CONFIG\_NET\_IPV4\_AUTO \*/

533

535/\* We always need to have at least one IP config \*/

536#define NET\_IF\_MAX\_CONFIGS 1

538

[ 542](structnet__if__ip.md)struct [net\_if\_ip](structnet__if__ip.md) {

543#if defined(CONFIG\_NET\_NATIVE\_IPV6)

544 struct [net\_if\_ipv6](structnet__if__ipv6.md) \*ipv6;

545#endif /\* CONFIG\_NET\_IPV6 \*/

546

547#if defined(CONFIG\_NET\_NATIVE\_IPV4)

548 struct [net\_if\_ipv4](structnet__if__ipv4.md) \*ipv4;

549#endif /\* CONFIG\_NET\_IPV4 \*/

550};

551

[ 555](structnet__if__config.md)struct [net\_if\_config](structnet__if__config.md) {

556#if defined(CONFIG\_NET\_IP)

558 struct [net\_if\_ip](structnet__if__ip.md) ip;

559#endif

560

561#if defined(CONFIG\_NET\_DHCPV4) && defined(CONFIG\_NET\_NATIVE\_IPV4)

562 struct net\_if\_dhcpv4 dhcpv4;

563#endif /\* CONFIG\_NET\_DHCPV4 \*/

564

565#if defined(CONFIG\_NET\_DHCPV6) && defined(CONFIG\_NET\_NATIVE\_IPV6)

566 struct net\_if\_dhcpv6 dhcpv6;

567#endif /\* CONFIG\_NET\_DHCPV6 \*/

568

569#if defined(CONFIG\_NET\_IPV4\_AUTO) && defined(CONFIG\_NET\_NATIVE\_IPV4)

570 struct net\_if\_ipv4\_autoconf ipv4auto;

571#endif /\* CONFIG\_NET\_IPV4\_AUTO \*/

572

573#if defined(CONFIG\_NET\_L2\_VIRTUAL)

578 [sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8) virtual\_interfaces;

579#endif /\* CONFIG\_NET\_L2\_VIRTUAL \*/

580

581#if defined(CONFIG\_NET\_INTERFACE\_NAME)

586 char name[CONFIG\_NET\_INTERFACE\_NAME\_LEN + 1];

587#endif

588};

589

[ 599](structnet__traffic__class.md)struct [net\_traffic\_class](structnet__traffic__class.md) {

[ 601](structnet__traffic__class.md#a94511ca12bad1687f5c7ca862c857ded) struct [k\_fifo](structk__fifo.md) [fifo](structnet__traffic__class.md#a94511ca12bad1687f5c7ca862c857ded);

602

[ 604](structnet__traffic__class.md#a8d0023588fee0a8ff1381bbc80ada143) struct [k\_thread](structk__thread.md) [handler](structnet__traffic__class.md#a8d0023588fee0a8ff1381bbc80ada143);

605

[ 607](structnet__traffic__class.md#a2d98bc68d38bdef649d645b8b52516c5) [k\_thread\_stack\_t](arch__interface_8h.md#a9fc2dce533bd7b8cb1fdd4bdbb2b62b1) \*[stack](structnet__traffic__class.md#a2d98bc68d38bdef649d645b8b52516c5);

608};

609

[ 616](group__net__if.md#gaef3dfe26195514aac625e9f22e399759)typedef int (\*[net\_socket\_create\_t](group__net__if.md#gaef3dfe26195514aac625e9f22e399759))(int, int, int);

617

[ 632](structnet__if__dev.md)struct [net\_if\_dev](structnet__if__dev.md) {

[ 634](structnet__if__dev.md#aab633a44f165f571910dc9fc9e131c50) const struct [device](structdevice.md) \*[dev](structnet__if__dev.md#aab633a44f165f571910dc9fc9e131c50);

635

[ 637](structnet__if__dev.md#a85d713c62875f5fe9e3ec29773150797) const struct [net\_l2](structnet__l2.md) \* const [l2](structnet__if__dev.md#a85d713c62875f5fe9e3ec29773150797);

638

[ 640](structnet__if__dev.md#a8fec6a7f612fc1268ef486d8bdebe018) void \*[l2\_data](structnet__if__dev.md#a8fec6a7f612fc1268ef486d8bdebe018);

641

[ 643](structnet__if__dev.md#ac8f9c30e1dea05c28c88d3b367b130f5) [ATOMIC\_DEFINE](group__atomic__apis.md#ga249c575db9764486197709b327f7370e)([flags](structnet__if__dev.md#ac8f9c30e1dea05c28c88d3b367b130f5), NET\_IF\_NUM\_FLAGS);

644

[ 646](structnet__if__dev.md#aac6d5d341ab520e6aac7f7b03737c197) struct [net\_linkaddr](structnet__linkaddr.md) [link\_addr](structnet__if__dev.md#aac6d5d341ab520e6aac7f7b03737c197);

647

648#if defined(CONFIG\_NET\_OFFLOAD)

654 struct net\_offload \*offload;

655#endif /\* CONFIG\_NET\_OFFLOAD \*/

656

[ 658](structnet__if__dev.md#aa15ccca2eb67b8d2afca153ccacb3742) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [mtu](structnet__if__dev.md#aa15ccca2eb67b8d2afca153ccacb3742);

659

660#if defined(CONFIG\_NET\_SOCKETS\_OFFLOAD)

664 [net\_socket\_create\_t](group__net__if.md#gaef3dfe26195514aac625e9f22e399759) socket\_offload;

665#endif /\* CONFIG\_NET\_SOCKETS\_OFFLOAD \*/

666

[ 668](structnet__if__dev.md#a30eabb2ffae082d0de81a50c510738a3) enum [net\_if\_oper\_state](group__net__if.md#gadfe9d90f24046cd9bd4bbee096e747b9) [oper\_state](structnet__if__dev.md#a30eabb2ffae082d0de81a50c510738a3);

669};

670

[ 678](structnet__if.md)struct [net\_if](structnet__if.md) {

[ 680](structnet__if.md#a0982ba2019cdaa7701162e60fdb2171e) struct [net\_if\_dev](structnet__if__dev.md) \*[if\_dev](structnet__if.md#a0982ba2019cdaa7701162e60fdb2171e);

681

682#if defined(CONFIG\_NET\_STATISTICS\_PER\_INTERFACE)

684 struct [net\_stats](structnet__stats.md) stats;

685#endif /\* CONFIG\_NET\_STATISTICS\_PER\_INTERFACE \*/

686

[ 688](structnet__if.md#a5e71962f55bdead7bfbbb96518c6c404) struct [net\_if\_config](structnet__if__config.md) [config](structnet__if.md#a5e71962f55bdead7bfbbb96518c6c404);

689

690#if defined(CONFIG\_NET\_POWER\_MANAGEMENT)

695 int tx\_pending;

696#endif

697

[ 699](structnet__if.md#ace2233b71da53ff0fc7cd564ccfc5a03) struct [k\_mutex](structk__mutex.md) [lock](structnet__if.md#ace2233b71da53ff0fc7cd564ccfc5a03);

700

[ 702](structnet__if.md#af00f729ebddfdcf725169f61b6cd586b) struct [k\_mutex](structk__mutex.md) [tx\_lock](structnet__if.md#af00f729ebddfdcf725169f61b6cd586b);

703

[ 708](structnet__if.md#aa96a6a2d55f6a4ece2f340eef526ef56) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [pe\_enabled](structnet__if.md#aa96a6a2d55f6a4ece2f340eef526ef56) : 1;

709

[ 713](structnet__if.md#aec585e283c9053443ff05b364acf76eb) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [pe\_prefer\_public](structnet__if.md#aec585e283c9053443ff05b364acf76eb) : 1;

714

716 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \_unused : 6;

717};

718

720

721static inline void net\_if\_lock(struct [net\_if](structnet__if.md) \*iface)

722{

723 NET\_ASSERT(iface);

724

725 (void)[k\_mutex\_lock](group__mutex__apis.md#ga850549358645249c285669baa49c33b0)(&iface->[lock](structnet__if.md#ace2233b71da53ff0fc7cd564ccfc5a03), [K\_FOREVER](group__clock__apis.md#ga0bb4b83f0222193b21a8910311bab0ca));

726}

727

728static inline void net\_if\_unlock(struct [net\_if](structnet__if.md) \*iface)

729{

730 NET\_ASSERT(iface);

731

732 [k\_mutex\_unlock](group__mutex__apis.md#ga360f4c0e7258b0d7030cdb1f452b2c31)(&iface->[lock](structnet__if.md#ace2233b71da53ff0fc7cd564ccfc5a03));

733}

734

735static inline bool [net\_if\_flag\_is\_set](group__net__if.md#gae1f373ddd61c18a81481d8ddcfb12543)(struct [net\_if](structnet__if.md) \*iface,

736 enum [net\_if\_flag](group__net__if.md#gae691e5537917ffce27ad0db82c730371) value);

737

738static inline void net\_if\_tx\_lock(struct [net\_if](structnet__if.md) \*iface)

739{

740 NET\_ASSERT(iface);

741

742 if ([net\_if\_flag\_is\_set](group__net__if.md#gae1f373ddd61c18a81481d8ddcfb12543)(iface, [NET\_IF\_NO\_TX\_LOCK](group__net__if.md#ggae691e5537917ffce27ad0db82c730371ae8d564e1577c8daad8ce50a729c500c9))) {

743 return;

744 }

745

746 (void)[k\_mutex\_lock](group__mutex__apis.md#ga850549358645249c285669baa49c33b0)(&iface->[tx\_lock](structnet__if.md#af00f729ebddfdcf725169f61b6cd586b), [K\_FOREVER](group__clock__apis.md#ga0bb4b83f0222193b21a8910311bab0ca));

747}

748

749static inline void net\_if\_tx\_unlock(struct [net\_if](structnet__if.md) \*iface)

750{

751 NET\_ASSERT(iface);

752

753 if ([net\_if\_flag\_is\_set](group__net__if.md#gae1f373ddd61c18a81481d8ddcfb12543)(iface, [NET\_IF\_NO\_TX\_LOCK](group__net__if.md#ggae691e5537917ffce27ad0db82c730371ae8d564e1577c8daad8ce50a729c500c9))) {

754 return;

755 }

756

757 [k\_mutex\_unlock](group__mutex__apis.md#ga360f4c0e7258b0d7030cdb1f452b2c31)(&iface->[tx\_lock](structnet__if.md#af00f729ebddfdcf725169f61b6cd586b));

758}

759

761

[ 768](group__net__if.md#ga52f9fca13e9f836799e0e40f581744d2)static inline void [net\_if\_flag\_set](group__net__if.md#ga52f9fca13e9f836799e0e40f581744d2)(struct [net\_if](structnet__if.md) \*iface,

769 enum [net\_if\_flag](group__net__if.md#gae691e5537917ffce27ad0db82c730371) value)

770{

771 NET\_ASSERT(iface);

772 NET\_ASSERT(iface->[if\_dev](structnet__if.md#a0982ba2019cdaa7701162e60fdb2171e));

773

774 [atomic\_set\_bit](group__atomic__apis.md#ga17a3961ba7610ad6e595e602f70344a0)(iface->[if\_dev](structnet__if.md#a0982ba2019cdaa7701162e60fdb2171e)->[flags](structnet__if__dev.md#ac8f9c30e1dea05c28c88d3b367b130f5), value);

775}

776

[ 785](group__net__if.md#ga42e7482191a92007960601f8bb621dca)static inline bool [net\_if\_flag\_test\_and\_set](group__net__if.md#ga42e7482191a92007960601f8bb621dca)(struct [net\_if](structnet__if.md) \*iface,

786 enum [net\_if\_flag](group__net__if.md#gae691e5537917ffce27ad0db82c730371) value)

787{

788 NET\_ASSERT(iface);

789 NET\_ASSERT(iface->[if\_dev](structnet__if.md#a0982ba2019cdaa7701162e60fdb2171e));

790

791 return [atomic\_test\_and\_set\_bit](group__atomic__apis.md#ga7ff45e13aa5f8be5d7a550e49f5c720b)(iface->[if\_dev](structnet__if.md#a0982ba2019cdaa7701162e60fdb2171e)->[flags](structnet__if__dev.md#ac8f9c30e1dea05c28c88d3b367b130f5), value);

792}

793

[ 800](group__net__if.md#gaff751b6a92b0c608ecfc50e8c0587fd3)static inline void [net\_if\_flag\_clear](group__net__if.md#gaff751b6a92b0c608ecfc50e8c0587fd3)(struct [net\_if](structnet__if.md) \*iface,

801 enum [net\_if\_flag](group__net__if.md#gae691e5537917ffce27ad0db82c730371) value)

802{

803 NET\_ASSERT(iface);

804 NET\_ASSERT(iface->[if\_dev](structnet__if.md#a0982ba2019cdaa7701162e60fdb2171e));

805

806 [atomic\_clear\_bit](group__atomic__apis.md#ga1c1693d524c49d11fd32b323a39d718e)(iface->[if\_dev](structnet__if.md#a0982ba2019cdaa7701162e60fdb2171e)->[flags](structnet__if__dev.md#ac8f9c30e1dea05c28c88d3b367b130f5), value);

807}

808

[ 817](group__net__if.md#gab8f371c7f8890cf4728177f6595141d7)static inline bool [net\_if\_flag\_test\_and\_clear](group__net__if.md#gab8f371c7f8890cf4728177f6595141d7)(struct [net\_if](structnet__if.md) \*iface,

818 enum [net\_if\_flag](group__net__if.md#gae691e5537917ffce27ad0db82c730371) value)

819{

820 NET\_ASSERT(iface);

821 NET\_ASSERT(iface->[if\_dev](structnet__if.md#a0982ba2019cdaa7701162e60fdb2171e));

822

823 return [atomic\_test\_and\_clear\_bit](group__atomic__apis.md#ga53159437721084da0ec8ee70ec212472)(iface->[if\_dev](structnet__if.md#a0982ba2019cdaa7701162e60fdb2171e)->[flags](structnet__if__dev.md#ac8f9c30e1dea05c28c88d3b367b130f5), value);

824}

825

[ 834](group__net__if.md#gae1f373ddd61c18a81481d8ddcfb12543)static inline bool [net\_if\_flag\_is\_set](group__net__if.md#gae1f373ddd61c18a81481d8ddcfb12543)(struct [net\_if](structnet__if.md) \*iface,

835 enum [net\_if\_flag](group__net__if.md#gae691e5537917ffce27ad0db82c730371) value)

836{

837 NET\_ASSERT(iface);

838 NET\_ASSERT(iface->[if\_dev](structnet__if.md#a0982ba2019cdaa7701162e60fdb2171e));

839

840 if (iface == NULL) {

841 return false;

842 }

843

844 return [atomic\_test\_bit](group__atomic__apis.md#ga190ddc108f45e7649689753c08658eae)(iface->[if\_dev](structnet__if.md#a0982ba2019cdaa7701162e60fdb2171e)->[flags](structnet__if__dev.md#ac8f9c30e1dea05c28c88d3b367b130f5), value);

845}

846

[ 855](group__net__if.md#ga1f1bf845e63cce02e2183889cc85d57e)static inline enum [net\_if\_oper\_state](group__net__if.md#gadfe9d90f24046cd9bd4bbee096e747b9) [net\_if\_oper\_state\_set](group__net__if.md#ga1f1bf845e63cce02e2183889cc85d57e)(

856 struct [net\_if](structnet__if.md) \*iface, enum [net\_if\_oper\_state](group__net__if.md#gadfe9d90f24046cd9bd4bbee096e747b9) oper\_state)

857{

858 NET\_ASSERT(iface);

859 NET\_ASSERT(iface->[if\_dev](structnet__if.md#a0982ba2019cdaa7701162e60fdb2171e));

860

861 if (oper\_state >= [NET\_IF\_OPER\_UNKNOWN](group__net__if.md#ggadfe9d90f24046cd9bd4bbee096e747b9ac7cae092ea6ceeb62499a9b435ac4b58) && oper\_state <= [NET\_IF\_OPER\_UP](group__net__if.md#ggadfe9d90f24046cd9bd4bbee096e747b9a6b99bfc28d831292029761d74209ee03)) {

862 iface->[if\_dev](structnet__if.md#a0982ba2019cdaa7701162e60fdb2171e)->[oper\_state](structnet__if__dev.md#a30eabb2ffae082d0de81a50c510738a3) = oper\_state;

863 }

864

865 return iface->[if\_dev](structnet__if.md#a0982ba2019cdaa7701162e60fdb2171e)->[oper\_state](structnet__if__dev.md#a30eabb2ffae082d0de81a50c510738a3);

866}

867

[ 875](group__net__if.md#gad9e957a4866b4566296ee39392fde0e4)static inline enum [net\_if\_oper\_state](group__net__if.md#gadfe9d90f24046cd9bd4bbee096e747b9) [net\_if\_oper\_state](group__net__if.md#gadfe9d90f24046cd9bd4bbee096e747b9)(struct [net\_if](structnet__if.md) \*iface)

876{

877 NET\_ASSERT(iface);

878 NET\_ASSERT(iface->[if\_dev](structnet__if.md#a0982ba2019cdaa7701162e60fdb2171e));

879

880 return iface->[if\_dev](structnet__if.md#a0982ba2019cdaa7701162e60fdb2171e)->[oper\_state](structnet__if__dev.md#a30eabb2ffae082d0de81a50c510738a3);

881}

882

[ 891](group__net__if.md#gada0398d757eab28d16a129692c309f4d)enum [net\_verdict](group__net__core.md#ga8e5393f3bdd85491f221324e637c3896) [net\_if\_send\_data](group__net__if.md#gada0398d757eab28d16a129692c309f4d)(struct [net\_if](structnet__if.md) \*iface, struct [net\_pkt](structnet__pkt.md) \*pkt);

892

[ 900](group__net__if.md#gafa451f6118529d1d084704d00b2aae20)static inline const struct [net\_l2](structnet__l2.md) \*[net\_if\_l2](group__net__if.md#gafa451f6118529d1d084704d00b2aae20)(struct [net\_if](structnet__if.md) \*iface)

901{

902 if (!iface || !iface->[if\_dev](structnet__if.md#a0982ba2019cdaa7701162e60fdb2171e)) {

903 return NULL;

904 }

905

906 return iface->[if\_dev](structnet__if.md#a0982ba2019cdaa7701162e60fdb2171e)->[l2](structnet__if__dev.md#a85d713c62875f5fe9e3ec29773150797);

907}

908

[ 917](group__net__if.md#ga72ed21ca0cb220199f5a2070137c7fef)enum [net\_verdict](group__net__core.md#ga8e5393f3bdd85491f221324e637c3896) [net\_if\_recv\_data](group__net__if.md#ga72ed21ca0cb220199f5a2070137c7fef)(struct [net\_if](structnet__if.md) \*iface, struct [net\_pkt](structnet__pkt.md) \*pkt);

918

[ 926](group__net__if.md#ga3cad2d51fc9cc225619585e06e252db0)static inline void \*[net\_if\_l2\_data](group__net__if.md#ga3cad2d51fc9cc225619585e06e252db0)(struct [net\_if](structnet__if.md) \*iface)

927{

928 NET\_ASSERT(iface);

929 NET\_ASSERT(iface->[if\_dev](structnet__if.md#a0982ba2019cdaa7701162e60fdb2171e));

930

931 return iface->[if\_dev](structnet__if.md#a0982ba2019cdaa7701162e60fdb2171e)->[l2\_data](structnet__if__dev.md#a8fec6a7f612fc1268ef486d8bdebe018);

932}

933

[ 941](group__net__if.md#gaeb8c703f273bc07ae9bb7a0d8bfe6f3d)static inline const struct [device](structdevice.md) \*[net\_if\_get\_device](group__net__if.md#gaeb8c703f273bc07ae9bb7a0d8bfe6f3d)(struct [net\_if](structnet__if.md) \*iface)

942{

943 NET\_ASSERT(iface);

944 NET\_ASSERT(iface->[if\_dev](structnet__if.md#a0982ba2019cdaa7701162e60fdb2171e));

945

946 return iface->[if\_dev](structnet__if.md#a0982ba2019cdaa7701162e60fdb2171e)->[dev](structnet__if__dev.md#aab633a44f165f571910dc9fc9e131c50);

947}

948

[ 955](group__net__if.md#ga56c4d37edcea540be09ebcdf97265aed)void [net\_if\_queue\_tx](group__net__if.md#ga56c4d37edcea540be09ebcdf97265aed)(struct [net\_if](structnet__if.md) \*iface, struct [net\_pkt](structnet__pkt.md) \*pkt);

956

[ 964](group__net__if.md#ga6bfa5f84a2127bbad27a0a3b319526a1)static inline bool [net\_if\_is\_ip\_offloaded](group__net__if.md#ga6bfa5f84a2127bbad27a0a3b319526a1)(struct [net\_if](structnet__if.md) \*iface)

965{

966#if defined(CONFIG\_NET\_OFFLOAD)

967 return (iface != NULL && iface->[if\_dev](structnet__if.md#a0982ba2019cdaa7701162e60fdb2171e) != NULL &&

968 iface->[if\_dev](structnet__if.md#a0982ba2019cdaa7701162e60fdb2171e)->offload != NULL);

969#else

970 ARG\_UNUSED(iface);

971

972 return false;

973#endif

974}

975

[ 983](group__net__if.md#gaecedc93a6dab2c57fe686718ea4d78af)bool [net\_if\_is\_offloaded](group__net__if.md#gaecedc93a6dab2c57fe686718ea4d78af)(struct [net\_if](structnet__if.md) \*iface);

984

[ 992](group__net__if.md#ga520939e94620ca75475a71f153df6d4a)static inline struct net\_offload \*[net\_if\_offload](group__net__if.md#ga520939e94620ca75475a71f153df6d4a)(struct [net\_if](structnet__if.md) \*iface)

993{

994#if defined(CONFIG\_NET\_OFFLOAD)

995 NET\_ASSERT(iface);

996 NET\_ASSERT(iface->[if\_dev](structnet__if.md#a0982ba2019cdaa7701162e60fdb2171e));

997

998 return iface->[if\_dev](structnet__if.md#a0982ba2019cdaa7701162e60fdb2171e)->offload;

999#else

1000 ARG\_UNUSED(iface);

1001

1002 return NULL;

1003#endif

1004}

1005

[ 1013](group__net__if.md#gaf308baf2241fa455b50b439b7fab3f1e)static inline bool [net\_if\_is\_socket\_offloaded](group__net__if.md#gaf308baf2241fa455b50b439b7fab3f1e)(struct [net\_if](structnet__if.md) \*iface)

1014{

1015#if defined(CONFIG\_NET\_SOCKETS\_OFFLOAD)

1016 NET\_ASSERT(iface);

1017 NET\_ASSERT(iface->[if\_dev](structnet__if.md#a0982ba2019cdaa7701162e60fdb2171e));

1018

1019 return (iface->[if\_dev](structnet__if.md#a0982ba2019cdaa7701162e60fdb2171e)->socket\_offload != NULL);

1020#else

1021 ARG\_UNUSED(iface);

1022

1023 return false;

1024#endif

1025}

1026

[ 1033](group__net__if.md#ga9db52875580115c743b1f35cd6c46796)static inline void [net\_if\_socket\_offload\_set](group__net__if.md#ga9db52875580115c743b1f35cd6c46796)(

1034 struct [net\_if](structnet__if.md) \*iface, [net\_socket\_create\_t](group__net__if.md#gaef3dfe26195514aac625e9f22e399759) socket\_offload)

1035{

1036#if defined(CONFIG\_NET\_SOCKETS\_OFFLOAD)

1037 NET\_ASSERT(iface);

1038 NET\_ASSERT(iface->[if\_dev](structnet__if.md#a0982ba2019cdaa7701162e60fdb2171e));

1039

1040 iface->[if\_dev](structnet__if.md#a0982ba2019cdaa7701162e60fdb2171e)->socket\_offload = socket\_offload;

1041#else

1042 ARG\_UNUSED(iface);

1043 ARG\_UNUSED(socket\_offload);

1044#endif

1045}

1046

[ 1054](group__net__if.md#gafb2bbaec96c4759d920b2866c0b3ef3a)static inline [net\_socket\_create\_t](group__net__if.md#gaef3dfe26195514aac625e9f22e399759) [net\_if\_socket\_offload](group__net__if.md#gafb2bbaec96c4759d920b2866c0b3ef3a)(struct [net\_if](structnet__if.md) \*iface)

1055{

1056#if defined(CONFIG\_NET\_SOCKETS\_OFFLOAD)

1057 NET\_ASSERT(iface);

1058 NET\_ASSERT(iface->[if\_dev](structnet__if.md#a0982ba2019cdaa7701162e60fdb2171e));

1059

1060 return iface->[if\_dev](structnet__if.md#a0982ba2019cdaa7701162e60fdb2171e)->socket\_offload;

1061#else

1062 ARG\_UNUSED(iface);

1063

1064 return NULL;

1065#endif

1066}

1067

[ 1075](group__net__if.md#ga467186e964bf721e14fed38392f21872)static inline struct [net\_linkaddr](structnet__linkaddr.md) \*[net\_if\_get\_link\_addr](group__net__if.md#ga467186e964bf721e14fed38392f21872)(struct [net\_if](structnet__if.md) \*iface)

1076{

1077 NET\_ASSERT(iface);

1078 NET\_ASSERT(iface->[if\_dev](structnet__if.md#a0982ba2019cdaa7701162e60fdb2171e));

1079

1080 return &iface->[if\_dev](structnet__if.md#a0982ba2019cdaa7701162e60fdb2171e)->[link\_addr](structnet__if__dev.md#aac6d5d341ab520e6aac7f7b03737c197);

1081}

1082

[ 1090](group__net__if.md#gae271e0e4dcb031a83d9908e597a45048)static inline struct [net\_if\_config](structnet__if__config.md) \*[net\_if\_get\_config](group__net__if.md#gae271e0e4dcb031a83d9908e597a45048)(struct [net\_if](structnet__if.md) \*iface)

1091{

1092 NET\_ASSERT(iface);

1093

1094 return &iface->[config](structnet__if.md#a5e71962f55bdead7bfbbb96518c6c404);

1095}

1096

1102#if defined(CONFIG\_NET\_IPV6\_DAD) && defined(CONFIG\_NET\_NATIVE\_IPV6)

1103void [net\_if\_start\_dad](group__net__if.md#ga9655c010ccbf989e9328271f5dbcc685)(struct [net\_if](structnet__if.md) \*iface);

1104#else

[ 1105](group__net__if.md#ga9655c010ccbf989e9328271f5dbcc685)static inline void [net\_if\_start\_dad](group__net__if.md#ga9655c010ccbf989e9328271f5dbcc685)(struct [net\_if](structnet__if.md) \*iface)

1106{

1107 ARG\_UNUSED(iface);

1108}

1109#endif

1110

[ 1116](group__net__if.md#gab9bdb7f8a9eeed4d9b70965b8af82cb7)void [net\_if\_start\_rs](group__net__if.md#gab9bdb7f8a9eeed4d9b70965b8af82cb7)(struct [net\_if](structnet__if.md) \*iface);

1117

1118

1124#if defined(CONFIG\_NET\_IPV6\_ND) && defined(CONFIG\_NET\_NATIVE\_IPV6)

1125void [net\_if\_stop\_rs](group__net__if.md#gab0195bb2151a1ba722a0b11d81066988)(struct [net\_if](structnet__if.md) \*iface);

1126#else

[ 1127](group__net__if.md#gab0195bb2151a1ba722a0b11d81066988)static inline void [net\_if\_stop\_rs](group__net__if.md#gab0195bb2151a1ba722a0b11d81066988)(struct [net\_if](structnet__if.md) \*iface)

1128{

1129 ARG\_UNUSED(iface);

1130}

1131#endif /\* CONFIG\_NET\_IPV6\_ND \*/

1132

1145#if defined(CONFIG\_NET\_IPV6\_ND) && defined(CONFIG\_NET\_NATIVE\_IPV6)

1146void [net\_if\_nbr\_reachability\_hint](group__net__if.md#ga51af469ff3d7d9f760d63a8a9c7be8b5)(struct [net\_if](structnet__if.md) \*iface, const struct [in6\_addr](structin6__addr.md) \*ipv6\_addr);

1147#else

[ 1148](group__net__if.md#ga51af469ff3d7d9f760d63a8a9c7be8b5)static inline void [net\_if\_nbr\_reachability\_hint](group__net__if.md#ga51af469ff3d7d9f760d63a8a9c7be8b5)(struct [net\_if](structnet__if.md) \*iface,

1149 const struct [in6\_addr](structin6__addr.md) \*ipv6\_addr)

1150{

1151 ARG\_UNUSED(iface);

1152 ARG\_UNUSED(ipv6\_addr);

1153}

1154#endif

1155

1157

1158static inline int net\_if\_set\_link\_addr\_unlocked(struct [net\_if](structnet__if.md) \*iface,

1159 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) len,

1160 enum [net\_link\_type](group__net__linkaddr.md#ga1312c2322bc4a4f1c3b76d6466806b24) type)

1161{

1162 if ([net\_if\_flag\_is\_set](group__net__if.md#gae1f373ddd61c18a81481d8ddcfb12543)(iface, [NET\_IF\_RUNNING](group__net__if.md#ggae691e5537917ffce27ad0db82c730371add3e2ecdcd5de3154f9bd2836428a25a))) {

1163 return -[EPERM](group__system__errno.md#gadd669d31505a077f769cff8e66c780b3);

1164 }

1165

1166 [net\_if\_get\_link\_addr](group__net__if.md#ga467186e964bf721e14fed38392f21872)(iface)->[addr](structnet__linkaddr.md#a2176a9f7a444ac3b0108102d8cf852f0) = addr;

1167 [net\_if\_get\_link\_addr](group__net__if.md#ga467186e964bf721e14fed38392f21872)(iface)->[len](structnet__linkaddr.md#a7b2f8ebe68b557eb9cbb4c2f2ecd70e0) = len;

1168 [net\_if\_get\_link\_addr](group__net__if.md#ga467186e964bf721e14fed38392f21872)(iface)->[type](structnet__linkaddr.md#a5f5b4c3d353261d0fab8011aa09f00d7) = type;

1169

1170 [net\_hostname\_set\_postfix](group__net__hostname.md#ga6aa3799b3b0d7eec7fb8b276485ae2c5)(addr, len);

1171

1172 return 0;

1173}

1174

1175int net\_if\_set\_link\_addr\_locked(struct [net\_if](structnet__if.md) \*iface,

1176 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) len,

1177 enum [net\_link\_type](group__net__linkaddr.md#ga1312c2322bc4a4f1c3b76d6466806b24) type);

1178

1179#if CONFIG\_NET\_IF\_LOG\_LEVEL >= LOG\_LEVEL\_DBG

1180extern int net\_if\_addr\_unref\_debug(struct [net\_if](structnet__if.md) \*iface,

1181 [sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda) family,

1182 const void \*addr,

1183 const char \*caller, int line);

1184#define net\_if\_addr\_unref(iface, family, addr) \

1185 net\_if\_addr\_unref\_debug(iface, family, addr, \_\_func\_\_, \_\_LINE\_\_)

1186

1187extern struct [net\_if\_addr](structnet__if__addr.md) \*net\_if\_addr\_ref\_debug(struct [net\_if](structnet__if.md) \*iface,

1188 [sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda) family,

1189 const void \*addr,

1190 const char \*caller,

1191 int line);

1192#define net\_if\_addr\_ref(iface, family, addr) \

1193 net\_if\_addr\_ref\_debug(iface, family, addr, \_\_func\_\_, \_\_LINE\_\_)

1194#else

1195extern int net\_if\_addr\_unref(struct [net\_if](structnet__if.md) \*iface,

1196 [sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda) family,

1197 const void \*addr);

1198extern struct [net\_if\_addr](structnet__if__addr.md) \*net\_if\_addr\_ref(struct [net\_if](structnet__if.md) \*iface,

1199 [sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda) family,

1200 const void \*addr);

1201#endif /\* CONFIG\_NET\_IF\_LOG\_LEVEL \*/

1202

1204

[ 1216](group__net__if.md#ga52b41b2f8b7d3405338a0539542677a0)static inline int [net\_if\_set\_link\_addr](group__net__if.md#ga52b41b2f8b7d3405338a0539542677a0)(struct [net\_if](structnet__if.md) \*iface,

1217 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) len,

1218 enum [net\_link\_type](group__net__linkaddr.md#ga1312c2322bc4a4f1c3b76d6466806b24) type)

1219{

1220#if defined(CONFIG\_NET\_RAW\_MODE)

1221 return net\_if\_set\_link\_addr\_unlocked(iface, addr, len, type);

1222#else

1223 return net\_if\_set\_link\_addr\_locked(iface, addr, len, type);

1224#endif

1225}

1226

[ 1234](group__net__if.md#gacddc98531c5748db5a34f5c3a3e96e86)static inline [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [net\_if\_get\_mtu](group__net__if.md#gacddc98531c5748db5a34f5c3a3e96e86)(struct [net\_if](structnet__if.md) \*iface)

1235{

1236 if (iface == NULL) {

1237 return 0U;

1238 }

1239

1240 NET\_ASSERT(iface->[if\_dev](structnet__if.md#a0982ba2019cdaa7701162e60fdb2171e));

1241

1242 return iface->[if\_dev](structnet__if.md#a0982ba2019cdaa7701162e60fdb2171e)->[mtu](structnet__if__dev.md#aa15ccca2eb67b8d2afca153ccacb3742);

1243}

1244

[ 1251](group__net__if.md#ga76b140c6fc39b94ff4102e08e3a58e81)static inline void [net\_if\_set\_mtu](group__net__if.md#ga76b140c6fc39b94ff4102e08e3a58e81)(struct [net\_if](structnet__if.md) \*iface,

1252 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mtu)

1253{

1254 if (iface == NULL) {

1255 return;

1256 }

1257

1258 NET\_ASSERT(iface->[if\_dev](structnet__if.md#a0982ba2019cdaa7701162e60fdb2171e));

1259

1260 iface->[if\_dev](structnet__if.md#a0982ba2019cdaa7701162e60fdb2171e)->[mtu](structnet__if__dev.md#aa15ccca2eb67b8d2afca153ccacb3742) = mtu;

1261}

1262

[ 1269](group__net__if.md#gae66f6e7bd31545e6161fcd4600fe5842)static inline void [net\_if\_addr\_set\_lf](group__net__if.md#gae66f6e7bd31545e6161fcd4600fe5842)(struct [net\_if\_addr](structnet__if__addr.md) \*ifaddr,

1270 bool [is\_infinite](structnet__if__addr.md#a6e799428eb0633a25e4dc3c55e3a3b8c))

1271{

1272 NET\_ASSERT(ifaddr);

1273

1274 ifaddr->[is\_infinite](structnet__if__addr.md#a6e799428eb0633a25e4dc3c55e3a3b8c) = [is\_infinite](structnet__if__addr.md#a6e799428eb0633a25e4dc3c55e3a3b8c);

1275}

1276

[ 1284](group__net__if.md#ga1b058361dc9bcac7d842bb49846a0c79)struct [net\_if](structnet__if.md) \*[net\_if\_get\_by\_link\_addr](group__net__if.md#ga1b058361dc9bcac7d842bb49846a0c79)(struct [net\_linkaddr](structnet__linkaddr.md) \*ll\_addr);

1285

[ 1293](group__net__if.md#gadbb8be32caa896bdcdeee19425134827)struct [net\_if](structnet__if.md) \*[net\_if\_lookup\_by\_dev](group__net__if.md#gadbb8be32caa896bdcdeee19425134827)(const struct [device](structdevice.md) \*dev);

1294

[ 1302](group__net__if.md#gae2323a72714e29836d8296dfc330f7fd)static inline struct [net\_if\_config](structnet__if__config.md) \*[net\_if\_config\_get](group__net__if.md#gae2323a72714e29836d8296dfc330f7fd)(struct [net\_if](structnet__if.md) \*iface)

1303{

1304 NET\_ASSERT(iface);

1305

1306 return &iface->[config](structnet__if.md#a5e71962f55bdead7bfbbb96518c6c404);

1307}

1308

[ 1314](group__net__if.md#gadc87242eb7205362a308b3c4437bf76d)void [net\_if\_router\_rm](group__net__if.md#gadc87242eb7205362a308b3c4437bf76d)(struct [net\_if\_router](structnet__if__router.md) \*router);

1315

[ 1321](group__net__if.md#ga0a1f27ec893e1af3c97f130be4616589)void [net\_if\_set\_default](group__net__if.md#ga0a1f27ec893e1af3c97f130be4616589)(struct [net\_if](structnet__if.md) \*iface);

1322

[ 1328](group__net__if.md#ga55214771e462cbd4930ffa738813cb87)struct [net\_if](structnet__if.md) \*[net\_if\_get\_default](group__net__if.md#ga55214771e462cbd4930ffa738813cb87)(void);

1329

[ 1338](group__net__if.md#ga762337e8b66874a0fbf59bdbeba173f5)struct [net\_if](structnet__if.md) \*[net\_if\_get\_first\_by\_type](group__net__if.md#ga762337e8b66874a0fbf59bdbeba173f5)(const struct [net\_l2](structnet__l2.md) \*l2);

1339

[ 1346](group__net__if.md#ga03d8c6aebb1412382a9eec636c227238)struct [net\_if](structnet__if.md) \*[net\_if\_get\_first\_up](group__net__if.md#ga03d8c6aebb1412382a9eec636c227238)(void);

1347

1348#if defined(CONFIG\_NET\_L2\_IEEE802154)

1355static inline struct [net\_if](structnet__if.md) \*net\_if\_get\_ieee802154(void)

1356{

1357 return [net\_if\_get\_first\_by\_type](group__net__if.md#ga762337e8b66874a0fbf59bdbeba173f5)(&NET\_L2\_GET\_NAME(IEEE802154));

1358}

1359#endif /\* CONFIG\_NET\_L2\_IEEE802154 \*/

1360

[ 1371](group__net__if.md#ga56c9aef19bc9827d9ec96c00e10840fa)int [net\_if\_config\_ipv6\_get](group__net__if.md#ga56c9aef19bc9827d9ec96c00e10840fa)(struct [net\_if](structnet__if.md) \*iface,

1372 struct [net\_if\_ipv6](structnet__if__ipv6.md) \*\*ipv6);

1373

[ 1381](group__net__if.md#ga8af1400b354c42a64795cdb1a600ddd6)int [net\_if\_config\_ipv6\_put](group__net__if.md#ga8af1400b354c42a64795cdb1a600ddd6)(struct [net\_if](structnet__if.md) \*iface);

1382

[ 1391](group__net__if.md#ga13b5a26fc672d15697f99e85543184bb)struct [net\_if\_addr](structnet__if__addr.md) \*[net\_if\_ipv6\_addr\_lookup](group__net__if.md#ga13b5a26fc672d15697f99e85543184bb)(const struct [in6\_addr](structin6__addr.md) \*addr,

1392 struct [net\_if](structnet__if.md) \*\*iface);

1393

[ 1402](group__net__if.md#gab53eabb540a4487d83f27c8e319c736a)struct [net\_if\_addr](structnet__if__addr.md) \*[net\_if\_ipv6\_addr\_lookup\_by\_iface](group__net__if.md#gab53eabb540a4487d83f27c8e319c736a)(struct [net\_if](structnet__if.md) \*iface,

1403 struct [in6\_addr](structin6__addr.md) \*addr);

1404

[ 1413](group__net__if.md#ga1527872e5285790d50028a183608ac02)\_\_syscall int [net\_if\_ipv6\_addr\_lookup\_by\_index](group__net__if.md#ga1527872e5285790d50028a183608ac02)(const struct [in6\_addr](structin6__addr.md) \*addr);

1414

[ 1425](group__net__if.md#gae00484a7fe32671a4ca04ff525e640c6)struct [net\_if\_addr](structnet__if__addr.md) \*[net\_if\_ipv6\_addr\_add](group__net__if.md#gae00484a7fe32671a4ca04ff525e640c6)(struct [net\_if](structnet__if.md) \*iface,

1426 struct [in6\_addr](structin6__addr.md) \*addr,

1427 enum [net\_addr\_type](group__ip__4__6.md#gafecee2d4a331dc85ad962b81a6303e41) [addr\_type](structnet__if__addr.md#ab4fd41001cc24615803bfabb9d48e7eb),

1428 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) vlifetime);

1429

[ 1440](group__net__if.md#ga980bffb649ed48775bdc6cb2a0caef15)\_\_syscall bool [net\_if\_ipv6\_addr\_add\_by\_index](group__net__if.md#ga980bffb649ed48775bdc6cb2a0caef15)(int index,

1441 struct [in6\_addr](structin6__addr.md) \*addr,

1442 enum [net\_addr\_type](group__ip__4__6.md#gafecee2d4a331dc85ad962b81a6303e41) [addr\_type](structnet__if__addr.md#ab4fd41001cc24615803bfabb9d48e7eb),

1443 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) vlifetime);

1444

[ 1451](group__net__if.md#gaef8a6752a201f81636c4ffc1ebba4a25)void [net\_if\_ipv6\_addr\_update\_lifetime](group__net__if.md#gaef8a6752a201f81636c4ffc1ebba4a25)(struct [net\_if\_addr](structnet__if__addr.md) \*ifaddr,

1452 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) vlifetime);

1453

[ 1462](group__net__if.md#ga614e1458fa28d26c26f447e9fbcc2cb7)bool [net\_if\_ipv6\_addr\_rm](group__net__if.md#ga614e1458fa28d26c26f447e9fbcc2cb7)(struct [net\_if](structnet__if.md) \*iface, const struct [in6\_addr](structin6__addr.md) \*addr);

1463

[ 1472](group__net__if.md#gac159e3b0fbf558d5fb09774141da7d6d)\_\_syscall bool [net\_if\_ipv6\_addr\_rm\_by\_index](group__net__if.md#gac159e3b0fbf558d5fb09774141da7d6d)(int index,

1473 const struct [in6\_addr](structin6__addr.md) \*addr);

1474

[ 1483](group__net__if.md#gab58d8561a4f21899e2db34043d346516)typedef void (\*[net\_if\_ip\_addr\_cb\_t](group__net__if.md#gab58d8561a4f21899e2db34043d346516))(struct [net\_if](structnet__if.md) \*iface,

1484 struct [net\_if\_addr](structnet__if__addr.md) \*addr,

1485 void \*user\_data);

1486

[ 1495](group__net__if.md#ga5ac646ad7fda0fa48e78c15b4ca52d50)void [net\_if\_ipv6\_addr\_foreach](group__net__if.md#ga5ac646ad7fda0fa48e78c15b4ca52d50)(struct [net\_if](structnet__if.md) \*iface, [net\_if\_ip\_addr\_cb\_t](group__net__if.md#gab58d8561a4f21899e2db34043d346516) cb,

1496 void \*user\_data);

1497

[ 1506](group__net__if.md#ga7ae82a491193dfea9b92cb9cbaf26f98)struct [net\_if\_mcast\_addr](structnet__if__mcast__addr.md) \*[net\_if\_ipv6\_maddr\_add](group__net__if.md#ga7ae82a491193dfea9b92cb9cbaf26f98)(struct [net\_if](structnet__if.md) \*iface,

1507 const struct [in6\_addr](structin6__addr.md) \*addr);

1508

[ 1517](group__net__if.md#gaf0ce126bb5019ff5f5ff0876b9712ad9)bool [net\_if\_ipv6\_maddr\_rm](group__net__if.md#gaf0ce126bb5019ff5f5ff0876b9712ad9)(struct [net\_if](structnet__if.md) \*iface, const struct [in6\_addr](structin6__addr.md) \*addr);

1518

[ 1527](group__net__if.md#ga726eed76563c223de8f611e2544febe9)typedef void (\*[net\_if\_ip\_maddr\_cb\_t](group__net__if.md#ga726eed76563c223de8f611e2544febe9))(struct [net\_if](structnet__if.md) \*iface,

1528 struct [net\_if\_mcast\_addr](structnet__if__mcast__addr.md) \*maddr,

1529 void \*user\_data);

1530

[ 1539](group__net__if.md#gab677496fb2e27be2df299a346e9c7132)void [net\_if\_ipv6\_maddr\_foreach](group__net__if.md#gab677496fb2e27be2df299a346e9c7132)(struct [net\_if](structnet__if.md) \*iface, [net\_if\_ip\_maddr\_cb\_t](group__net__if.md#ga726eed76563c223de8f611e2544febe9) cb,

1540 void \*user\_data);

1541

[ 1552](group__net__if.md#gadb4031153c4fef86110879befa6b9975)struct [net\_if\_mcast\_addr](structnet__if__mcast__addr.md) \*[net\_if\_ipv6\_maddr\_lookup](group__net__if.md#gadb4031153c4fef86110879befa6b9975)(const struct [in6\_addr](structin6__addr.md) \*addr,

1553 struct [net\_if](structnet__if.md) \*\*iface);

1554

[ 1565](group__net__if.md#ga0d64291573740a67eae7ff3fcc0910c5)typedef void (\*[net\_if\_mcast\_callback\_t](group__net__if.md#ga0d64291573740a67eae7ff3fcc0910c5))(struct [net\_if](structnet__if.md) \*iface,

1566 const struct net\_addr \*addr,

1567 bool is\_joined);

1568

[ 1577](structnet__if__mcast__monitor.md)struct [net\_if\_mcast\_monitor](structnet__if__mcast__monitor.md) {

[ 1579](structnet__if__mcast__monitor.md#a570b7d8a8a5fabca83982a5f7d1d896a) [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) [node](structnet__if__mcast__monitor.md#a570b7d8a8a5fabca83982a5f7d1d896a);

1580

[ 1582](structnet__if__mcast__monitor.md#af4d0e937b2b9161918a13a0d6723c60a) struct [net\_if](structnet__if.md) \*[iface](structnet__if__mcast__monitor.md#af4d0e937b2b9161918a13a0d6723c60a);

1583

[ 1585](structnet__if__mcast__monitor.md#aec441b858a5f6792ac9cdbc625f6babe) [net\_if\_mcast\_callback\_t](group__net__if.md#ga0d64291573740a67eae7ff3fcc0910c5) [cb](structnet__if__mcast__monitor.md#aec441b858a5f6792ac9cdbc625f6babe);

1586};

1587

[ 1596](group__net__if.md#ga8fdd0665ed76db6055777e395ca60255)void [net\_if\_mcast\_mon\_register](group__net__if.md#ga8fdd0665ed76db6055777e395ca60255)(struct [net\_if\_mcast\_monitor](structnet__if__mcast__monitor.md) \*mon,

1597 struct [net\_if](structnet__if.md) \*iface,

1598 [net\_if\_mcast\_callback\_t](group__net__if.md#ga0d64291573740a67eae7ff3fcc0910c5) cb);

1599

[ 1605](group__net__if.md#gad323732fe3d178a5dfdf0900e5cb5683)void [net\_if\_mcast\_mon\_unregister](group__net__if.md#gad323732fe3d178a5dfdf0900e5cb5683)(struct [net\_if\_mcast\_monitor](structnet__if__mcast__monitor.md) \*mon);

1606

[ 1614](group__net__if.md#ga372ef131263269cd65586d87997df745)void [net\_if\_mcast\_monitor](group__net__if.md#ga372ef131263269cd65586d87997df745)(struct [net\_if](structnet__if.md) \*iface, const struct net\_addr \*addr,

1615 bool is\_joined);

1616

[ 1623](group__net__if.md#ga49dbc954015307222f176f4149829b76)void [net\_if\_ipv6\_maddr\_join](group__net__if.md#ga49dbc954015307222f176f4149829b76)(struct [net\_if](structnet__if.md) \*iface,

1624 struct [net\_if\_mcast\_addr](structnet__if__mcast__addr.md) \*addr);

1625

[ 1633](group__net__if.md#gabe2c16a378a35a22d008bff9142e5449)static inline bool [net\_if\_ipv6\_maddr\_is\_joined](group__net__if.md#gabe2c16a378a35a22d008bff9142e5449)(struct [net\_if\_mcast\_addr](structnet__if__mcast__addr.md) \*addr)

1634{

1635 NET\_ASSERT(addr);

1636

1637 return addr->[is\_joined](structnet__if__mcast__addr.md#a4af9009b2f9ccc0589a9ba6dac10927b);

1638}

1639

[ 1646](group__net__if.md#gad24d5537d52de9781a7a6a55ceedd92b)void [net\_if\_ipv6\_maddr\_leave](group__net__if.md#gad24d5537d52de9781a7a6a55ceedd92b)(struct [net\_if](structnet__if.md) \*iface,

1647 struct [net\_if\_mcast\_addr](structnet__if__mcast__addr.md) \*addr);

1648

[ 1657](group__net__if.md#gae9f98dff661d52c5e3e5e185f0ed9cc0)struct [net\_if\_ipv6\_prefix](structnet__if__ipv6__prefix.md) \*[net\_if\_ipv6\_prefix\_get](group__net__if.md#gae9f98dff661d52c5e3e5e185f0ed9cc0)(struct [net\_if](structnet__if.md) \*[iface](structnet__if__ipv6__prefix.md#a0e2d1997e2ccfe1e1af5f16e0c74ed92),

1658 const struct [in6\_addr](structin6__addr.md) \*addr);

1659

[ 1669](group__net__if.md#gaaf9af457b97c0d432b6f9f9fdd184834)struct [net\_if\_ipv6\_prefix](structnet__if__ipv6__prefix.md) \*[net\_if\_ipv6\_prefix\_lookup](group__net__if.md#gaaf9af457b97c0d432b6f9f9fdd184834)(struct [net\_if](structnet__if.md) \*[iface](structnet__if__ipv6__prefix.md#a0e2d1997e2ccfe1e1af5f16e0c74ed92),

1670 struct [in6\_addr](structin6__addr.md) \*addr,

1671 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [len](structnet__if__ipv6__prefix.md#a4d2bc2acbe51256b76cf4d3ced3aac39));

1672

[ 1683](group__net__if.md#ga2f0c98b16b090d9aea07941c64cbe035)struct [net\_if\_ipv6\_prefix](structnet__if__ipv6__prefix.md) \*[net\_if\_ipv6\_prefix\_add](group__net__if.md#ga2f0c98b16b090d9aea07941c64cbe035)(struct [net\_if](structnet__if.md) \*[iface](structnet__if__ipv6__prefix.md#a0e2d1997e2ccfe1e1af5f16e0c74ed92),

1684 struct [in6\_addr](structin6__addr.md) \*[prefix](structnet__if__ipv6__prefix.md#a65b450d0942b3c96cfc575b462d82028),

1685 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [len](structnet__if__ipv6__prefix.md#a4d2bc2acbe51256b76cf4d3ced3aac39),

1686 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [lifetime](structnet__if__ipv6__prefix.md#a925a97a49d383bd4ce475f5d09fcb7e3));

1687

[ 1697](group__net__if.md#ga36f18c7a3ff1777006290170b726deed)bool [net\_if\_ipv6\_prefix\_rm](group__net__if.md#ga36f18c7a3ff1777006290170b726deed)(struct [net\_if](structnet__if.md) \*[iface](structnet__if__ipv6__prefix.md#a0e2d1997e2ccfe1e1af5f16e0c74ed92), struct [in6\_addr](structin6__addr.md) \*addr,

1698 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [len](structnet__if__ipv6__prefix.md#a4d2bc2acbe51256b76cf4d3ced3aac39));

1699

[ 1706](group__net__if.md#gaa3c711e814fb6a4e552b4ef723d0baa0)static inline void [net\_if\_ipv6\_prefix\_set\_lf](group__net__if.md#gaa3c711e814fb6a4e552b4ef723d0baa0)(struct [net\_if\_ipv6\_prefix](structnet__if__ipv6__prefix.md) \*[prefix](structnet__if__ipv6__prefix.md#a65b450d0942b3c96cfc575b462d82028),

1707 bool [is\_infinite](structnet__if__ipv6__prefix.md#a22090441b27bed06098679bf23b4e1e9))

1708{

1709 [prefix](structnet__if__ipv6__prefix.md#a65b450d0942b3c96cfc575b462d82028)->is\_infinite = [is\_infinite](structnet__if__ipv6__prefix.md#a22090441b27bed06098679bf23b4e1e9);

1710}

1711

[ 1718](group__net__if.md#ga68cffe343c518bad7f7f152e30f7f9ee)void [net\_if\_ipv6\_prefix\_set\_timer](group__net__if.md#ga68cffe343c518bad7f7f152e30f7f9ee)(struct [net\_if\_ipv6\_prefix](structnet__if__ipv6__prefix.md) \*[prefix](structnet__if__ipv6__prefix.md#a65b450d0942b3c96cfc575b462d82028),

1719 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [lifetime](structnet__if__ipv6__prefix.md#a925a97a49d383bd4ce475f5d09fcb7e3));

1720

[ 1726](group__net__if.md#ga2d68cb6dcfcffd3f87bbfb3dfce791ff)void [net\_if\_ipv6\_prefix\_unset\_timer](group__net__if.md#ga2d68cb6dcfcffd3f87bbfb3dfce791ff)(struct [net\_if\_ipv6\_prefix](structnet__if__ipv6__prefix.md) \*[prefix](structnet__if__ipv6__prefix.md#a65b450d0942b3c96cfc575b462d82028));

1727

[ 1738](group__net__if.md#ga25d6e2253c1d361553d478f7c948a28a)bool [net\_if\_ipv6\_addr\_onlink](group__net__if.md#ga25d6e2253c1d361553d478f7c948a28a)(struct [net\_if](structnet__if.md) \*\*[iface](structnet__if__ipv6__prefix.md#a0e2d1997e2ccfe1e1af5f16e0c74ed92), struct [in6\_addr](structin6__addr.md) \*addr);

1739

1746#if defined(CONFIG\_NET\_NATIVE\_IPV6)

1747static inline struct [in6\_addr](structin6__addr.md) \*[net\_if\_router\_ipv6](group__net__if.md#gadbf1538003473d448ff0808896b732a5)(struct [net\_if\_router](structnet__if__router.md) \*router)

1748{

1749 NET\_ASSERT(router);

1750

1751 return &router->[address](structnet__if__router.md#a86a2ca1b95e348acbde8ce90986b83db).in6\_addr;

1752}

1753#else

[ 1754](group__net__if.md#gadbf1538003473d448ff0808896b732a5)static inline struct [in6\_addr](structin6__addr.md) \*[net\_if\_router\_ipv6](group__net__if.md#gadbf1538003473d448ff0808896b732a5)(struct [net\_if\_router](structnet__if__router.md) \*router)

1755{

1756 static struct [in6\_addr](structin6__addr.md) addr;

1757

1758 ARG\_UNUSED(router);

1759

1760 return &addr;

1761}

1762#endif

1763

[ 1773](group__net__if.md#gacece4ee588082259b3b5cfcd5ac1d552)struct [net\_if\_router](structnet__if__router.md) \*[net\_if\_ipv6\_router\_lookup](group__net__if.md#gacece4ee588082259b3b5cfcd5ac1d552)(struct [net\_if](structnet__if.md) \*[iface](structnet__if__router.md#a03789aa0a40f7686b76616de0ca0401a),

1774 struct [in6\_addr](structin6__addr.md) \*addr);

1775

[ 1785](group__net__if.md#ga36dab2a8fd9120ebc9c8b18f1875ccfd)struct [net\_if\_router](structnet__if__router.md) \*[net\_if\_ipv6\_router\_find\_default](group__net__if.md#ga36dab2a8fd9120ebc9c8b18f1875ccfd)(struct [net\_if](structnet__if.md) \*[iface](structnet__if__router.md#a03789aa0a40f7686b76616de0ca0401a),

1786 struct [in6\_addr](structin6__addr.md) \*addr);

1787

[ 1794](group__net__if.md#gaadba4957802dc376ef011590c91c6af6)void [net\_if\_ipv6\_router\_update\_lifetime](group__net__if.md#gaadba4957802dc376ef011590c91c6af6)(struct [net\_if\_router](structnet__if__router.md) \*router,

1795 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [lifetime](structnet__if__router.md#a4b0d2ad8f225ab61022c10dfce3db199));

1796

[ 1806](group__net__if.md#ga9c766ed70ada6eb551ac6542d7ac1ca3)struct [net\_if\_router](structnet__if__router.md) \*[net\_if\_ipv6\_router\_add](group__net__if.md#ga9c766ed70ada6eb551ac6542d7ac1ca3)(struct [net\_if](structnet__if.md) \*[iface](structnet__if__router.md#a03789aa0a40f7686b76616de0ca0401a),

1807 struct [in6\_addr](structin6__addr.md) \*addr,

1808 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) router\_lifetime);

1809

[ 1817](group__net__if.md#ga1d108aa0b54c072e0aa9d0c049f02807)bool [net\_if\_ipv6\_router\_rm](group__net__if.md#ga1d108aa0b54c072e0aa9d0c049f02807)(struct [net\_if\_router](structnet__if__router.md) \*router);

1818

[ 1827](group__net__if.md#ga54b200a4c4f09678298bf1b8f5da2ea6)[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [net\_if\_ipv6\_get\_hop\_limit](group__net__if.md#ga54b200a4c4f09678298bf1b8f5da2ea6)(struct [net\_if](structnet__if.md) \*[iface](structnet__if__router.md#a03789aa0a40f7686b76616de0ca0401a));

1828

[ 1835](group__net__if.md#ga37b1d83f3ef7ab5996a86e7f7f3d9c72)void [net\_if\_ipv6\_set\_hop\_limit](group__net__if.md#ga37b1d83f3ef7ab5996a86e7f7f3d9c72)(struct [net\_if](structnet__if.md) \*[iface](structnet__if__router.md#a03789aa0a40f7686b76616de0ca0401a), [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) hop\_limit);

1836

1838

1839/\* The old hop limit setter function is deprecated because the naming

1840 \* of it was incorrect. The API name was missing "\_if\_" so this function

1841 \* should not be used.

1842 \*/

1843\_\_deprecated

1844static inline void net\_ipv6\_set\_hop\_limit(struct [net\_if](structnet__if.md) \*[iface](structnet__if__router.md#a03789aa0a40f7686b76616de0ca0401a),

1845 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) hop\_limit)

1846{

1847 [net\_if\_ipv6\_set\_hop\_limit](group__net__if.md#ga37b1d83f3ef7ab5996a86e7f7f3d9c72)([iface](structnet__if__router.md#a03789aa0a40f7686b76616de0ca0401a), hop\_limit);

1848}

1849

1851

[ 1860](group__net__if.md#ga95505542ecf92642a0b6f68f9dda5bf6)[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [net\_if\_ipv6\_get\_mcast\_hop\_limit](group__net__if.md#ga95505542ecf92642a0b6f68f9dda5bf6)(struct [net\_if](structnet__if.md) \*[iface](structnet__if__router.md#a03789aa0a40f7686b76616de0ca0401a));

1861

[ 1868](group__net__if.md#ga3792cb18e34693b3c49f6dbccda3cf61)void [net\_if\_ipv6\_set\_mcast\_hop\_limit](group__net__if.md#ga3792cb18e34693b3c49f6dbccda3cf61)(struct [net\_if](structnet__if.md) \*[iface](structnet__if__router.md#a03789aa0a40f7686b76616de0ca0401a), [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) hop\_limit);

1869

[ 1876](group__net__if.md#gab3939d735b660f8f02124df656ceba2c)static inline void [net\_if\_ipv6\_set\_base\_reachable\_time](group__net__if.md#gab3939d735b660f8f02124df656ceba2c)(struct [net\_if](structnet__if.md) \*[iface](structnet__if__router.md#a03789aa0a40f7686b76616de0ca0401a),

1877 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) reachable\_time)

1878{

1879#if defined(CONFIG\_NET\_NATIVE\_IPV6)

1880 NET\_ASSERT([iface](structnet__if__router.md#a03789aa0a40f7686b76616de0ca0401a));

1881

1882 if (![iface](structnet__if__router.md#a03789aa0a40f7686b76616de0ca0401a)->[config](structnet__if.md#a5e71962f55bdead7bfbbb96518c6c404).ip.ipv6) {

1883 return;

1884 }

1885

1886 [iface](structnet__if__router.md#a03789aa0a40f7686b76616de0ca0401a)->[config](structnet__if.md#a5e71962f55bdead7bfbbb96518c6c404).ip.ipv6->base\_reachable\_time = reachable\_time;

1887#else

1888 ARG\_UNUSED([iface](structnet__if__router.md#a03789aa0a40f7686b76616de0ca0401a));

1889 ARG\_UNUSED(reachable\_time);

1890

1891#endif

1892}

1893

[ 1901](group__net__if.md#ga9dd1f91edbb519a6a079f363c33efacf)static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [net\_if\_ipv6\_get\_reachable\_time](group__net__if.md#ga9dd1f91edbb519a6a079f363c33efacf)(struct [net\_if](structnet__if.md) \*[iface](structnet__if__router.md#a03789aa0a40f7686b76616de0ca0401a))

1902{

1903#if defined(CONFIG\_NET\_NATIVE\_IPV6)

1904 NET\_ASSERT([iface](structnet__if__router.md#a03789aa0a40f7686b76616de0ca0401a));

1905

1906 if (![iface](structnet__if__router.md#a03789aa0a40f7686b76616de0ca0401a)->[config](structnet__if.md#a5e71962f55bdead7bfbbb96518c6c404).ip.ipv6) {

1907 return 0;

1908 }

1909

1910 return [iface](structnet__if__router.md#a03789aa0a40f7686b76616de0ca0401a)->[config](structnet__if.md#a5e71962f55bdead7bfbbb96518c6c404).ip.ipv6->reachable\_time;

1911#else

1912 ARG\_UNUSED([iface](structnet__if__router.md#a03789aa0a40f7686b76616de0ca0401a));

1913 return 0;

1914#endif

1915}

1916

[ 1924](group__net__if.md#gab1861b5cefa73b4eefbb447cb1438cdc)[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [net\_if\_ipv6\_calc\_reachable\_time](group__net__if.md#gab1861b5cefa73b4eefbb447cb1438cdc)(struct [net\_if\_ipv6](structnet__if__ipv6.md) \*ipv6);

1925

[ 1932](group__net__if.md#ga8328266b870fd200660cb2becaab3de4)static inline void [net\_if\_ipv6\_set\_reachable\_time](group__net__if.md#ga8328266b870fd200660cb2becaab3de4)(struct [net\_if\_ipv6](structnet__if__ipv6.md) \*ipv6)

1933{

1934#if defined(CONFIG\_NET\_NATIVE\_IPV6)

1935 if (ipv6 == NULL) {

1936 return;

1937 }

1938

1939 ipv6->[reachable\_time](structnet__if__ipv6.md#af57b7dca189167f8cc757c4ed6b08f2f) = [net\_if\_ipv6\_calc\_reachable\_time](group__net__if.md#gab1861b5cefa73b4eefbb447cb1438cdc)(ipv6);

1940#else

1941 ARG\_UNUSED(ipv6);

1942#endif

1943}

1944

[ 1951](group__net__if.md#gad74566e5a34f447d2ac63d2c0e82eeff)static inline void [net\_if\_ipv6\_set\_retrans\_timer](group__net__if.md#gad74566e5a34f447d2ac63d2c0e82eeff)(struct [net\_if](structnet__if.md) \*[iface](structnet__if__router.md#a03789aa0a40f7686b76616de0ca0401a),

1952 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) retrans\_timer)

1953{

1954#if defined(CONFIG\_NET\_NATIVE\_IPV6)

1955 NET\_ASSERT([iface](structnet__if__router.md#a03789aa0a40f7686b76616de0ca0401a));

1956

1957 if (![iface](structnet__if__router.md#a03789aa0a40f7686b76616de0ca0401a)->[config](structnet__if.md#a5e71962f55bdead7bfbbb96518c6c404).ip.ipv6) {

1958 return;

1959 }

1960

1961 [iface](structnet__if__router.md#a03789aa0a40f7686b76616de0ca0401a)->[config](structnet__if.md#a5e71962f55bdead7bfbbb96518c6c404).ip.ipv6->retrans\_timer = retrans\_timer;

1962#else

1963 ARG\_UNUSED([iface](structnet__if__router.md#a03789aa0a40f7686b76616de0ca0401a));

1964 ARG\_UNUSED(retrans\_timer);

1965#endif

1966}

1967

[ 1975](group__net__if.md#gaddbf5a6ba412e6bdb7e31568fe827bd0)static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [net\_if\_ipv6\_get\_retrans\_timer](group__net__if.md#gaddbf5a6ba412e6bdb7e31568fe827bd0)(struct [net\_if](structnet__if.md) \*[iface](structnet__if__router.md#a03789aa0a40f7686b76616de0ca0401a))

1976{

1977#if defined(CONFIG\_NET\_NATIVE\_IPV6)

1978 NET\_ASSERT([iface](structnet__if__router.md#a03789aa0a40f7686b76616de0ca0401a));

1979

1980 if (![iface](structnet__if__router.md#a03789aa0a40f7686b76616de0ca0401a)->[config](structnet__if.md#a5e71962f55bdead7bfbbb96518c6c404).ip.ipv6) {

1981 return 0;

1982 }

1983

1984 return [iface](structnet__if__router.md#a03789aa0a40f7686b76616de0ca0401a)->[config](structnet__if.md#a5e71962f55bdead7bfbbb96518c6c404).ip.ipv6->retrans\_timer;

1985#else

1986 ARG\_UNUSED([iface](structnet__if__router.md#a03789aa0a40f7686b76616de0ca0401a));

1987 return 0;

1988#endif

1989}

1990

2002#if defined(CONFIG\_NET\_NATIVE\_IPV6)

2003const struct [in6\_addr](structin6__addr.md) \*[net\_if\_ipv6\_select\_src\_addr](group__net__if.md#ga50689a1afdb37a7087bf47a12cc50438)(struct [net\_if](structnet__if.md) \*iface,

2004 const struct [in6\_addr](structin6__addr.md) \*dst);

2005#else

[ 2006](group__net__if.md#ga50689a1afdb37a7087bf47a12cc50438)static inline const struct [in6\_addr](structin6__addr.md) \*[net\_if\_ipv6\_select\_src\_addr](group__net__if.md#ga50689a1afdb37a7087bf47a12cc50438)(

2007 struct [net\_if](structnet__if.md) \*iface, const struct [in6\_addr](structin6__addr.md) \*dst)

2008{

2009 ARG\_UNUSED(iface);

2010 ARG\_UNUSED(dst);

2011

2012 return NULL;

2013}

2014#endif

2015

2029#if defined(CONFIG\_NET\_NATIVE\_IPV6)

2030const struct [in6\_addr](structin6__addr.md) \*[net\_if\_ipv6\_select\_src\_addr\_hint](group__net__if.md#ga5cf4717e632f712045dd4fe81b30245c)(struct [net\_if](structnet__if.md) \*iface,

2031 const struct [in6\_addr](structin6__addr.md) \*dst,

2032 int [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

2033#else

[ 2034](group__net__if.md#ga5cf4717e632f712045dd4fe81b30245c)static inline const struct [in6\_addr](structin6__addr.md) \*[net\_if\_ipv6\_select\_src\_addr\_hint](group__net__if.md#ga5cf4717e632f712045dd4fe81b30245c)(

2035 struct [net\_if](structnet__if.md) \*iface, const struct [in6\_addr](structin6__addr.md) \*dst, int [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9))

2036{

2037 ARG\_UNUSED(iface);

2038 ARG\_UNUSED(dst);

2039 ARG\_UNUSED([flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

2040

2041 return NULL;

2042}

2043#endif

2044

2054#if defined(CONFIG\_NET\_NATIVE\_IPV6)

2055struct [net\_if](structnet__if.md) \*[net\_if\_ipv6\_select\_src\_iface](group__net__if.md#gae1495ac9e743be54b8d90bd4ff4700ab)(const struct [in6\_addr](structin6__addr.md) \*dst);

2056#else

[ 2057](group__net__if.md#gae1495ac9e743be54b8d90bd4ff4700ab)static inline struct [net\_if](structnet__if.md) \*[net\_if\_ipv6\_select\_src\_iface](group__net__if.md#gae1495ac9e743be54b8d90bd4ff4700ab)(

2058 const struct [in6\_addr](structin6__addr.md) \*dst)

2059{

2060 ARG\_UNUSED(dst);

2061

2062 return NULL;

2063}

2064#endif

2065

[ 2075](group__net__if.md#gad6f3e1e349e281887352652f6f32274e)struct [in6\_addr](structin6__addr.md) \*[net\_if\_ipv6\_get\_ll](group__net__if.md#gad6f3e1e349e281887352652f6f32274e)(struct [net\_if](structnet__if.md) \*iface,

2076 enum [net\_addr\_state](group__ip__4__6.md#ga32e58fc83532ef57eeb6ff952f17288d) addr\_state);

2077

[ 2087](group__net__if.md#ga85b7a923d46d36ecd63f9930bd8970c4)struct [in6\_addr](structin6__addr.md) \*[net\_if\_ipv6\_get\_ll\_addr](group__net__if.md#ga85b7a923d46d36ecd63f9930bd8970c4)(enum [net\_addr\_state](group__ip__4__6.md#ga32e58fc83532ef57eeb6ff952f17288d) [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90),

2088 struct [net\_if](structnet__if.md) \*\*iface);

2089

[ 2097](group__net__if.md#ga1dd53d92f803cff3be4826ddfb6b7211)void [net\_if\_ipv6\_dad\_failed](group__net__if.md#ga1dd53d92f803cff3be4826ddfb6b7211)(struct [net\_if](structnet__if.md) \*iface, const struct [in6\_addr](structin6__addr.md) \*addr);

2098

[ 2110](group__net__if.md#gaca7d686c772deac13a027cc046333126)struct [in6\_addr](structin6__addr.md) \*[net\_if\_ipv6\_get\_global\_addr](group__net__if.md#gaca7d686c772deac13a027cc046333126)(enum [net\_addr\_state](group__ip__4__6.md#ga32e58fc83532ef57eeb6ff952f17288d) [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90),

2111 struct [net\_if](structnet__if.md) \*\*iface);

2112

[ 2123](group__net__if.md#ga3390e248249b28f2c80e2ca0bc79d236)int [net\_if\_config\_ipv4\_get](group__net__if.md#ga3390e248249b28f2c80e2ca0bc79d236)(struct [net\_if](structnet__if.md) \*iface,

2124 struct [net\_if\_ipv4](structnet__if__ipv4.md) \*\*ipv4);

2125

[ 2133](group__net__if.md#ga88c13a45617480a665c7f9f589ec8e10)int [net\_if\_config\_ipv4\_put](group__net__if.md#ga88c13a45617480a665c7f9f589ec8e10)(struct [net\_if](structnet__if.md) \*iface);

2134

[ 2142](group__net__if.md#ga7e1fd28dbcf1164d056296b4df782e64)[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [net\_if\_ipv4\_get\_ttl](group__net__if.md#ga7e1fd28dbcf1164d056296b4df782e64)(struct [net\_if](structnet__if.md) \*iface);

2143

[ 2150](group__net__if.md#ga5544374d7ebea26a239d561083f0203d)void [net\_if\_ipv4\_set\_ttl](group__net__if.md#ga5544374d7ebea26a239d561083f0203d)(struct [net\_if](structnet__if.md) \*iface, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ttl);

2151

[ 2159](group__net__if.md#ga71acb65b1988aab8cca9c9604c86231e)[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [net\_if\_ipv4\_get\_mcast\_ttl](group__net__if.md#ga71acb65b1988aab8cca9c9604c86231e)(struct [net\_if](structnet__if.md) \*iface);

2160

[ 2167](group__net__if.md#ga9452fef4f1309fb1a53a6a8b4f222377)void [net\_if\_ipv4\_set\_mcast\_ttl](group__net__if.md#ga9452fef4f1309fb1a53a6a8b4f222377)(struct [net\_if](structnet__if.md) \*iface, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ttl);

2168

[ 2177](group__net__if.md#ga04a8f21d173d51bdcc092b92ed949e53)struct [net\_if\_addr](structnet__if__addr.md) \*[net\_if\_ipv4\_addr\_lookup](group__net__if.md#ga04a8f21d173d51bdcc092b92ed949e53)(const struct [in\_addr](structin__addr.md) \*addr,

2178 struct [net\_if](structnet__if.md) \*\*iface);

2179

[ 2190](group__net__if.md#ga7190958f740cac56de3a13fe688b3b5d)struct [net\_if\_addr](structnet__if__addr.md) \*[net\_if\_ipv4\_addr\_add](group__net__if.md#ga7190958f740cac56de3a13fe688b3b5d)(struct [net\_if](structnet__if.md) \*iface,

2191 struct [in\_addr](structin__addr.md) \*addr,

2192 enum [net\_addr\_type](group__ip__4__6.md#gafecee2d4a331dc85ad962b81a6303e41) [addr\_type](structnet__if__addr.md#ab4fd41001cc24615803bfabb9d48e7eb),

2193 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) vlifetime);

2194

[ 2203](group__net__if.md#ga4433304d46b6559604486b828e7d9dec)bool [net\_if\_ipv4\_addr\_rm](group__net__if.md#ga4433304d46b6559604486b828e7d9dec)(struct [net\_if](structnet__if.md) \*iface, const struct [in\_addr](structin__addr.md) \*addr);

2204

[ 2213](group__net__if.md#ga0a22661727316517685afcd551e7b38e)\_\_syscall int [net\_if\_ipv4\_addr\_lookup\_by\_index](group__net__if.md#ga0a22661727316517685afcd551e7b38e)(const struct [in\_addr](structin__addr.md) \*addr);

2214

[ 2225](group__net__if.md#gad140a69cf510ad99a8a8c770bab95bc9)\_\_syscall bool [net\_if\_ipv4\_addr\_add\_by\_index](group__net__if.md#gad140a69cf510ad99a8a8c770bab95bc9)(int index,

2226 struct [in\_addr](structin__addr.md) \*addr,

2227 enum [net\_addr\_type](group__ip__4__6.md#gafecee2d4a331dc85ad962b81a6303e41) [addr\_type](structnet__if__addr.md#ab4fd41001cc24615803bfabb9d48e7eb),

2228 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) vlifetime);

2229

[ 2238](group__net__if.md#gac5bf15f948ab195cecce98d1b40bda37)\_\_syscall bool [net\_if\_ipv4\_addr\_rm\_by\_index](group__net__if.md#gac5bf15f948ab195cecce98d1b40bda37)(int index,

2239 const struct [in\_addr](structin__addr.md) \*addr);

2240

[ 2249](group__net__if.md#gaae71be476e27c178ebb21b0f183c2825)void [net\_if\_ipv4\_addr\_foreach](group__net__if.md#gaae71be476e27c178ebb21b0f183c2825)(struct [net\_if](structnet__if.md) \*iface, [net\_if\_ip\_addr\_cb\_t](group__net__if.md#gab58d8561a4f21899e2db34043d346516) cb,

2250 void \*user\_data);

2251

[ 2260](group__net__if.md#gaa43fa83711703f8737e50b639e11b16c)struct [net\_if\_mcast\_addr](structnet__if__mcast__addr.md) \*[net\_if\_ipv4\_maddr\_add](group__net__if.md#gaa43fa83711703f8737e50b639e11b16c)(struct [net\_if](structnet__if.md) \*iface,

2261 const struct [in\_addr](structin__addr.md) \*addr);

2262

[ 2271](group__net__if.md#ga1d9273e10ab089d0f02b2b17d10a9e60)bool [net\_if\_ipv4\_maddr\_rm](group__net__if.md#ga1d9273e10ab089d0f02b2b17d10a9e60)(struct [net\_if](structnet__if.md) \*iface, const struct [in\_addr](structin__addr.md) \*addr);

2272

[ 2281](group__net__if.md#gae82f53c670f602e9c37b65abb6dfaec7)void [net\_if\_ipv4\_maddr\_foreach](group__net__if.md#gae82f53c670f602e9c37b65abb6dfaec7)(struct [net\_if](structnet__if.md) \*iface, [net\_if\_ip\_maddr\_cb\_t](group__net__if.md#ga726eed76563c223de8f611e2544febe9) cb,

2282 void \*user\_data);

2283

[ 2294](group__net__if.md#gadc1514a0d6852de9dbce043bc99d4eb0)struct [net\_if\_mcast\_addr](structnet__if__mcast__addr.md) \*[net\_if\_ipv4\_maddr\_lookup](group__net__if.md#gadc1514a0d6852de9dbce043bc99d4eb0)(const struct [in\_addr](structin__addr.md) \*addr,

2295 struct [net\_if](structnet__if.md) \*\*iface);

2296

[ 2303](group__net__if.md#gae275a5e75817aa178d36f422573ad76a)void [net\_if\_ipv4\_maddr\_join](group__net__if.md#gae275a5e75817aa178d36f422573ad76a)(struct [net\_if](structnet__if.md) \*iface,

2304 struct [net\_if\_mcast\_addr](structnet__if__mcast__addr.md) \*addr);

2305

[ 2313](group__net__if.md#gaa30769fc8016f1a7496b3ede277d8d8a)static inline bool [net\_if\_ipv4\_maddr\_is\_joined](group__net__if.md#gaa30769fc8016f1a7496b3ede277d8d8a)(struct [net\_if\_mcast\_addr](structnet__if__mcast__addr.md) \*addr)

2314{

2315 NET\_ASSERT(addr);

2316

2317 return addr->[is\_joined](structnet__if__mcast__addr.md#a4af9009b2f9ccc0589a9ba6dac10927b);

2318}

2319

[ 2326](group__net__if.md#ga1408fe384736d20f36c035c10007113c)void [net\_if\_ipv4\_maddr\_leave](group__net__if.md#ga1408fe384736d20f36c035c10007113c)(struct [net\_if](structnet__if.md) \*iface,

2327 struct [net\_if\_mcast\_addr](structnet__if__mcast__addr.md) \*addr);

2328

2335#if defined(CONFIG\_NET\_NATIVE\_IPV4)

2336static inline struct [in\_addr](structin__addr.md) \*[net\_if\_router\_ipv4](group__net__if.md#ga2a48e13941c91ddb9bbc63d014729be1)(struct [net\_if\_router](structnet__if__router.md) \*router)

2337{

2338 NET\_ASSERT(router);

2339

2340 return &router->[address](structnet__if__router.md#a86a2ca1b95e348acbde8ce90986b83db).in\_addr;

2341}

2342#else

[ 2343](group__net__if.md#ga2a48e13941c91ddb9bbc63d014729be1)static inline struct [in\_addr](structin__addr.md) \*[net\_if\_router\_ipv4](group__net__if.md#ga2a48e13941c91ddb9bbc63d014729be1)(struct [net\_if\_router](structnet__if__router.md) \*router)

2344{

2345 static struct [in\_addr](structin__addr.md) addr;

2346

2347 ARG\_UNUSED(router);

2348

2349 return &addr;

2350}

2351#endif

2352

[ 2362](group__net__if.md#ga01f995b00248ad5da734e4d58a4353aa)struct [net\_if\_router](structnet__if__router.md) \*[net\_if\_ipv4\_router\_lookup](group__net__if.md#ga01f995b00248ad5da734e4d58a4353aa)(struct [net\_if](structnet__if.md) \*[iface](structnet__if__router.md#a03789aa0a40f7686b76616de0ca0401a),

2363 struct [in\_addr](structin__addr.md) \*addr);

2364

[ 2374](group__net__if.md#ga25672516d7f383807e7dd9ce5f46a94f)struct [net\_if\_router](structnet__if__router.md) \*[net\_if\_ipv4\_router\_find\_default](group__net__if.md#ga25672516d7f383807e7dd9ce5f46a94f)(struct [net\_if](structnet__if.md) \*[iface](structnet__if__router.md#a03789aa0a40f7686b76616de0ca0401a),

2375 struct [in\_addr](structin__addr.md) \*addr);

[ 2386](group__net__if.md#ga44984001411077c7a2ef68afb361b40f)struct [net\_if\_router](structnet__if__router.md) \*[net\_if\_ipv4\_router\_add](group__net__if.md#ga44984001411077c7a2ef68afb361b40f)(struct [net\_if](structnet__if.md) \*[iface](structnet__if__router.md#a03789aa0a40f7686b76616de0ca0401a),

2387 struct [in\_addr](structin__addr.md) \*addr,

2388 bool [is\_default](structnet__if__router.md#a34745207edcad2745d6ce311e2bf1894),

2389 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) router\_lifetime);

2390

[ 2398](group__net__if.md#ga6be14f5307bc63ce87ff0a3fad7c7f4d)bool [net\_if\_ipv4\_router\_rm](group__net__if.md#ga6be14f5307bc63ce87ff0a3fad7c7f4d)(struct [net\_if\_router](structnet__if__router.md) \*router);

2399

[ 2408](group__net__if.md#ga558b31e556a1a4b8d1e68a78f3f755ea)bool [net\_if\_ipv4\_addr\_mask\_cmp](group__net__if.md#ga558b31e556a1a4b8d1e68a78f3f755ea)(struct [net\_if](structnet__if.md) \*[iface](structnet__if__router.md#a03789aa0a40f7686b76616de0ca0401a),

2409 const struct [in\_addr](structin__addr.md) \*addr);

2410

[ 2419](group__net__if.md#ga8f93179138c1942bc1a099102a4314cf)bool [net\_if\_ipv4\_is\_addr\_bcast](group__net__if.md#ga8f93179138c1942bc1a099102a4314cf)(struct [net\_if](structnet__if.md) \*[iface](structnet__if__router.md#a03789aa0a40f7686b76616de0ca0401a),

2420 const struct [in\_addr](structin__addr.md) \*addr);

2421

2431#if defined(CONFIG\_NET\_NATIVE\_IPV4)

2432struct [net\_if](structnet__if.md) \*[net\_if\_ipv4\_select\_src\_iface](group__net__if.md#gafea1a35f452ad8168855852cbfdf0024)(const struct [in\_addr](structin__addr.md) \*dst);

2433#else

[ 2434](group__net__if.md#gafea1a35f452ad8168855852cbfdf0024)static inline struct [net\_if](structnet__if.md) \*[net\_if\_ipv4\_select\_src\_iface](group__net__if.md#gafea1a35f452ad8168855852cbfdf0024)(

2435 const struct [in\_addr](structin__addr.md) \*dst)

2436{

2437 ARG\_UNUSED(dst);

2438

2439 return NULL;

2440}

2441#endif

2442

2454#if defined(CONFIG\_NET\_NATIVE\_IPV4)

2455const struct [in\_addr](structin__addr.md) \*[net\_if\_ipv4\_select\_src\_addr](group__net__if.md#gad6ec091f61ba3055be60c77ce085522f)(struct [net\_if](structnet__if.md) \*iface,

2456 const struct [in\_addr](structin__addr.md) \*dst);

2457#else

[ 2458](group__net__if.md#gad6ec091f61ba3055be60c77ce085522f)static inline const struct [in\_addr](structin__addr.md) \*[net\_if\_ipv4\_select\_src\_addr](group__net__if.md#gad6ec091f61ba3055be60c77ce085522f)(

2459 struct [net\_if](structnet__if.md) \*iface, const struct [in\_addr](structin__addr.md) \*dst)

2460{

2461 ARG\_UNUSED(iface);

2462 ARG\_UNUSED(dst);

2463

2464 return NULL;

2465}

2466#endif

2467

[ 2477](group__net__if.md#gad2ffe8df3d5ccca5094daecf3b9a8508)struct [in\_addr](structin__addr.md) \*[net\_if\_ipv4\_get\_ll](group__net__if.md#gad2ffe8df3d5ccca5094daecf3b9a8508)(struct [net\_if](structnet__if.md) \*iface,

2478 enum [net\_addr\_state](group__ip__4__6.md#ga32e58fc83532ef57eeb6ff952f17288d) addr\_state);

2479

[ 2489](group__net__if.md#gad791780f25d19acfe49d5272eae2d019)struct [in\_addr](structin__addr.md) \*[net\_if\_ipv4\_get\_global\_addr](group__net__if.md#gad791780f25d19acfe49d5272eae2d019)(struct [net\_if](structnet__if.md) \*iface,

2490 enum [net\_addr\_state](group__ip__4__6.md#ga32e58fc83532ef57eeb6ff952f17288d) addr\_state);

2491

[ 2501](group__net__if.md#gadfad7d9232bf58c5626266387a2eb761)struct [in\_addr](structin__addr.md) [net\_if\_ipv4\_get\_netmask\_by\_addr](group__net__if.md#gadfad7d9232bf58c5626266387a2eb761)(struct [net\_if](structnet__if.md) \*iface,

2502 const struct [in\_addr](structin__addr.md) \*addr);

2503

[ 2513](group__net__if.md#ga41aeb0e7c5f9bc837f7b2ec13401afd1)\_\_deprecated struct [in\_addr](structin__addr.md) [net\_if\_ipv4\_get\_netmask](group__net__if.md#ga41aeb0e7c5f9bc837f7b2ec13401afd1)(struct [net\_if](structnet__if.md) \*iface);

2514

[ 2523](group__net__if.md#gad599bd11663fefa7d785b9fc5d52caf0)\_\_deprecated void [net\_if\_ipv4\_set\_netmask](group__net__if.md#gad599bd11663fefa7d785b9fc5d52caf0)(struct [net\_if](structnet__if.md) \*iface,

2524 const struct [in\_addr](structin__addr.md) \*netmask);

2525

[ 2536](group__net__if.md#ga94f2d2e69548609dd329c7e6b21e8958)\_\_deprecated \_\_syscall bool [net\_if\_ipv4\_set\_netmask\_by\_index](group__net__if.md#ga94f2d2e69548609dd329c7e6b21e8958)(int index,

2537 const struct [in\_addr](structin__addr.md) \*netmask);

2538

[ 2548](group__net__if.md#ga895cfd55f79f7fb78a17cf0e3004fa06)\_\_syscall bool [net\_if\_ipv4\_set\_netmask\_by\_addr\_by\_index](group__net__if.md#ga895cfd55f79f7fb78a17cf0e3004fa06)(int index,

2549 const struct [in\_addr](structin__addr.md) \*addr,

2550 const struct [in\_addr](structin__addr.md) \*netmask);

2551

[ 2561](group__net__if.md#ga7beda6ccba46fce3cf2da1ce6c0725ec)bool [net\_if\_ipv4\_set\_netmask\_by\_addr](group__net__if.md#ga7beda6ccba46fce3cf2da1ce6c0725ec)(struct [net\_if](structnet__if.md) \*iface,

2562 const struct [in\_addr](structin__addr.md) \*addr,

2563 const struct [in\_addr](structin__addr.md) \*netmask);

2564

[ 2571](group__net__if.md#ga310ccbd9b37629422ca8e32836362724)void [net\_if\_ipv4\_set\_gw](group__net__if.md#ga310ccbd9b37629422ca8e32836362724)(struct [net\_if](structnet__if.md) \*iface, const struct [in\_addr](structin__addr.md) \*gw);

2572

[ 2581](group__net__if.md#gadef49124c331817165475c69fb9104e0)\_\_syscall bool [net\_if\_ipv4\_set\_gw\_by\_index](group__net__if.md#gadef49124c331817165475c69fb9104e0)(int index, const struct [in\_addr](structin__addr.md) \*gw);

2582

[ 2593](group__net__if.md#ga001b1cdde5febcf3970848c7c185c81c)struct [net\_if](structnet__if.md) \*[net\_if\_select\_src\_iface](group__net__if.md#ga001b1cdde5febcf3970848c7c185c81c)(const struct [sockaddr](structsockaddr.md) \*dst);

2594

[ 2603](group__net__if.md#ga0f87d5753fcd7cce40ecd161e6c91078)typedef void (\*[net\_if\_link\_callback\_t](group__net__if.md#ga0f87d5753fcd7cce40ecd161e6c91078))(struct [net\_if](structnet__if.md) \*iface,

2604 struct [net\_linkaddr](structnet__linkaddr.md) \*dst,

2605 int status);

2606

[ 2615](structnet__if__link__cb.md)struct [net\_if\_link\_cb](structnet__if__link__cb.md) {

[ 2617](structnet__if__link__cb.md#accae7945a802c5b7fc36948b12a365ef) [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) [node](structnet__if__link__cb.md#accae7945a802c5b7fc36948b12a365ef);

2618

[ 2620](structnet__if__link__cb.md#a66092a22cba3dd69ac1a91c3522240bb) [net\_if\_link\_callback\_t](group__net__if.md#ga0f87d5753fcd7cce40ecd161e6c91078) [cb](structnet__if__link__cb.md#a66092a22cba3dd69ac1a91c3522240bb);

2621};

2622

[ 2629](group__net__if.md#gaa81b7d9ed8dc05da3391265dbc89b665)void [net\_if\_register\_link\_cb](group__net__if.md#gaa81b7d9ed8dc05da3391265dbc89b665)(struct [net\_if\_link\_cb](structnet__if__link__cb.md) \*link,

2630 [net\_if\_link\_callback\_t](group__net__if.md#ga0f87d5753fcd7cce40ecd161e6c91078) cb);

2631

[ 2637](group__net__if.md#ga6ba64fac6e8d846ae7be5990f49a8293)void [net\_if\_unregister\_link\_cb](group__net__if.md#ga6ba64fac6e8d846ae7be5990f49a8293)(struct [net\_if\_link\_cb](structnet__if__link__cb.md) \*link);

2638

[ 2646](group__net__if.md#gaaa64aa4391a85760bb2daf600ac4d898)void [net\_if\_call\_link\_cb](group__net__if.md#gaaa64aa4391a85760bb2daf600ac4d898)(struct [net\_if](structnet__if.md) \*iface, struct [net\_linkaddr](structnet__linkaddr.md) \*lladdr,

2647 int status);

2648

2650

2651/\* used to ensure encoding of checksum support in net\_if.h and

2652 \* ethernet.h is the same

2653 \*/

2654#define NET\_IF\_CHECKSUM\_NONE\_BIT 0

2655#define NET\_IF\_CHECKSUM\_IPV4\_HEADER\_BIT BIT(0)

2656#define NET\_IF\_CHECKSUM\_IPV4\_ICMP\_BIT BIT(1)

2657/\* Space for future protocols and restrictions for IPV4 \*/

2658#define NET\_IF\_CHECKSUM\_IPV6\_HEADER\_BIT BIT(10)

2659#define NET\_IF\_CHECKSUM\_IPV6\_ICMP\_BIT BIT(11)

2660/\* Space for future protocols and restrictions for IPV6 \*/

2661#define NET\_IF\_CHECKSUM\_TCP\_BIT BIT(21)

2662#define NET\_IF\_CHECKSUM\_UDP\_BIT BIT(22)

2663

2665

[ 2669](group__net__if.md#ga8db412ae79c64cafe81a66f5acb2f8e9)enum [net\_if\_checksum\_type](group__net__if.md#ga8db412ae79c64cafe81a66f5acb2f8e9) {

[ 2671](group__net__if.md#gga8db412ae79c64cafe81a66f5acb2f8e9a75e4a0946d0e6755ebd7cc62558aee30) [NET\_IF\_CHECKSUM\_IPV4\_HEADER](group__net__if.md#gga8db412ae79c64cafe81a66f5acb2f8e9a75e4a0946d0e6755ebd7cc62558aee30) = NET\_IF\_CHECKSUM\_IPV4\_HEADER\_BIT,

[ 2673](group__net__if.md#gga8db412ae79c64cafe81a66f5acb2f8e9aaed32a3cb700eac3b67c6c7e5a0cd0ad) [NET\_IF\_CHECKSUM\_IPV4\_TCP](group__net__if.md#gga8db412ae79c64cafe81a66f5acb2f8e9aaed32a3cb700eac3b67c6c7e5a0cd0ad) = NET\_IF\_CHECKSUM\_IPV4\_HEADER\_BIT |

2674 NET\_IF\_CHECKSUM\_TCP\_BIT,

[ 2676](group__net__if.md#gga8db412ae79c64cafe81a66f5acb2f8e9afe1eaaa765c8ec3c61618e943cd3f1c3) [NET\_IF\_CHECKSUM\_IPV4\_UDP](group__net__if.md#gga8db412ae79c64cafe81a66f5acb2f8e9afe1eaaa765c8ec3c61618e943cd3f1c3) = NET\_IF\_CHECKSUM\_IPV4\_HEADER\_BIT |

2677 NET\_IF\_CHECKSUM\_UDP\_BIT,

[ 2679](group__net__if.md#gga8db412ae79c64cafe81a66f5acb2f8e9a2aef87c97f22fdccdf1925d2687436b1) [NET\_IF\_CHECKSUM\_IPV4\_ICMP](group__net__if.md#gga8db412ae79c64cafe81a66f5acb2f8e9a2aef87c97f22fdccdf1925d2687436b1) = NET\_IF\_CHECKSUM\_IPV4\_ICMP\_BIT,

[ 2681](group__net__if.md#gga8db412ae79c64cafe81a66f5acb2f8e9ab204c7d5fddbd2c11e07a8831df6c00b) [NET\_IF\_CHECKSUM\_IPV6\_HEADER](group__net__if.md#gga8db412ae79c64cafe81a66f5acb2f8e9ab204c7d5fddbd2c11e07a8831df6c00b) = NET\_IF\_CHECKSUM\_IPV6\_HEADER\_BIT,

[ 2683](group__net__if.md#gga8db412ae79c64cafe81a66f5acb2f8e9a31e33593e4e7f7f9b36e319e0991ab13) [NET\_IF\_CHECKSUM\_IPV6\_TCP](group__net__if.md#gga8db412ae79c64cafe81a66f5acb2f8e9a31e33593e4e7f7f9b36e319e0991ab13) = NET\_IF\_CHECKSUM\_IPV6\_HEADER\_BIT |

2684 NET\_IF\_CHECKSUM\_TCP\_BIT,

[ 2686](group__net__if.md#gga8db412ae79c64cafe81a66f5acb2f8e9a70b1272e2125cea9204bae144fd86660) [NET\_IF\_CHECKSUM\_IPV6\_UDP](group__net__if.md#gga8db412ae79c64cafe81a66f5acb2f8e9a70b1272e2125cea9204bae144fd86660) = NET\_IF\_CHECKSUM\_IPV6\_HEADER\_BIT |

2687 NET\_IF\_CHECKSUM\_UDP\_BIT,

[ 2689](group__net__if.md#gga8db412ae79c64cafe81a66f5acb2f8e9af5b3bc7cb5e9771cd9fd57d9fda4c3b3) [NET\_IF\_CHECKSUM\_IPV6\_ICMP](group__net__if.md#gga8db412ae79c64cafe81a66f5acb2f8e9af5b3bc7cb5e9771cd9fd57d9fda4c3b3) = NET\_IF\_CHECKSUM\_IPV6\_ICMP\_BIT

2690};

2691

[ 2702](group__net__if.md#ga8048e722f6442bcd5b6881bd71e791a5)bool [net\_if\_need\_calc\_rx\_checksum](group__net__if.md#ga8048e722f6442bcd5b6881bd71e791a5)(struct [net\_if](structnet__if.md) \*iface,

2703 enum [net\_if\_checksum\_type](group__net__if.md#ga8db412ae79c64cafe81a66f5acb2f8e9) chksum\_type);

2704

[ 2716](group__net__if.md#ga9634c3e71e934ab3a07bec989b364663)bool [net\_if\_need\_calc\_tx\_checksum](group__net__if.md#ga9634c3e71e934ab3a07bec989b364663)(struct [net\_if](structnet__if.md) \*iface,

2717 enum [net\_if\_checksum\_type](group__net__if.md#ga8db412ae79c64cafe81a66f5acb2f8e9) chksum\_type);

2718

[ 2729](group__net__if.md#ga72708cdb7f133fe5d7edf819756c3516)\_\_syscall struct [net\_if](structnet__if.md) \*[net\_if\_get\_by\_index](group__net__if.md#ga72708cdb7f133fe5d7edf819756c3516)(int index);

2730

[ 2738](group__net__if.md#ga02445f6c61f0d29f56ac0ef59e025630)int [net\_if\_get\_by\_iface](group__net__if.md#ga02445f6c61f0d29f56ac0ef59e025630)(struct [net\_if](structnet__if.md) \*iface);

2739

[ 2747](group__net__if.md#gac48ab8e6337e7cf387af9b293f254a80)typedef void (\*[net\_if\_cb\_t](group__net__if.md#gac48ab8e6337e7cf387af9b293f254a80))(struct [net\_if](structnet__if.md) \*iface, void \*user\_data);

2748

[ 2756](group__net__if.md#ga96b198fd9df4a985b0dde84dd7152815)void [net\_if\_foreach](group__net__if.md#ga96b198fd9df4a985b0dde84dd7152815)([net\_if\_cb\_t](group__net__if.md#gac48ab8e6337e7cf387af9b293f254a80) cb, void \*user\_data);

2757

[ 2765](group__net__if.md#ga02644cc623fc7a8878c17d54984e4210)int [net\_if\_up](group__net__if.md#ga02644cc623fc7a8878c17d54984e4210)(struct [net\_if](structnet__if.md) \*iface);

2766

[ 2774](group__net__if.md#ga7e9b368d4abf9da5656140df70cfa334)static inline bool [net\_if\_is\_up](group__net__if.md#ga7e9b368d4abf9da5656140df70cfa334)(struct [net\_if](structnet__if.md) \*iface)

2775{

2776 NET\_ASSERT(iface);

2777

2778 return [net\_if\_flag\_is\_set](group__net__if.md#gae1f373ddd61c18a81481d8ddcfb12543)(iface, [NET\_IF\_UP](group__net__if.md#ggae691e5537917ffce27ad0db82c730371ab0ab7393d643354c46c3437d74c15840)) &&

2779 [net\_if\_flag\_is\_set](group__net__if.md#gae1f373ddd61c18a81481d8ddcfb12543)(iface, [NET\_IF\_RUNNING](group__net__if.md#ggae691e5537917ffce27ad0db82c730371add3e2ecdcd5de3154f9bd2836428a25a));

2780}

2781

[ 2789](group__net__if.md#ga2187650062d6139b9f4b81745a206803)int [net\_if\_down](group__net__if.md#ga2187650062d6139b9f4b81745a206803)(struct [net\_if](structnet__if.md) \*iface);

2790

[ 2798](group__net__if.md#ga099a484a654ad9af35d3212fc2c995b2)static inline bool [net\_if\_is\_admin\_up](group__net__if.md#ga099a484a654ad9af35d3212fc2c995b2)(struct [net\_if](structnet__if.md) \*iface)

2799{

2800 NET\_ASSERT(iface);

2801

2802 return [net\_if\_flag\_is\_set](group__net__if.md#gae1f373ddd61c18a81481d8ddcfb12543)(iface, [NET\_IF\_UP](group__net__if.md#ggae691e5537917ffce27ad0db82c730371ab0ab7393d643354c46c3437d74c15840));

2803}

2804

[ 2813](group__net__if.md#ga35e5db3a631ac9039f14d86e59fc0dcc)void [net\_if\_carrier\_on](group__net__if.md#ga35e5db3a631ac9039f14d86e59fc0dcc)(struct [net\_if](structnet__if.md) \*iface);

2814

[ 2823](group__net__if.md#ga6839941422a88c1f707ab70ea34df323)void [net\_if\_carrier\_off](group__net__if.md#ga6839941422a88c1f707ab70ea34df323)(struct [net\_if](structnet__if.md) \*iface);

2824

[ 2832](group__net__if.md#ga095554237016e563d76cfd602d1dae77)static inline bool [net\_if\_is\_carrier\_ok](group__net__if.md#ga095554237016e563d76cfd602d1dae77)(struct [net\_if](structnet__if.md) \*iface)

2833{

2834 NET\_ASSERT(iface);

2835

2836 return [net\_if\_flag\_is\_set](group__net__if.md#gae1f373ddd61c18a81481d8ddcfb12543)(iface, [NET\_IF\_LOWER\_UP](group__net__if.md#ggae691e5537917ffce27ad0db82c730371ab1a529826bad6b4bcd04185372f97d6d));

2837}

2838

[ 2849](group__net__if.md#ga89a3374d4bb116460a7b7c50a750b593)void [net\_if\_dormant\_on](group__net__if.md#ga89a3374d4bb116460a7b7c50a750b593)(struct [net\_if](structnet__if.md) \*iface);

2850

[ 2859](group__net__if.md#ga1c31fac887d944ac0a16aad70e889496)void [net\_if\_dormant\_off](group__net__if.md#ga1c31fac887d944ac0a16aad70e889496)(struct [net\_if](structnet__if.md) \*iface);

2860

[ 2868](group__net__if.md#ga6e2e6102271c37acaa59c54e2aa6b413)static inline bool [net\_if\_is\_dormant](group__net__if.md#ga6e2e6102271c37acaa59c54e2aa6b413)(struct [net\_if](structnet__if.md) \*iface)

2869{

2870 NET\_ASSERT(iface);

2871

2872 return [net\_if\_flag\_is\_set](group__net__if.md#gae1f373ddd61c18a81481d8ddcfb12543)(iface, [NET\_IF\_DORMANT](group__net__if.md#ggae691e5537917ffce27ad0db82c730371a7dd1db72a37b1fbc4c4491ce1c75238d));

2873}

2874

2875#if defined(CONFIG\_NET\_PKT\_TIMESTAMP) && defined(CONFIG\_NET\_NATIVE)

2883typedef void (\*net\_if\_timestamp\_callback\_t)(struct [net\_pkt](structnet__pkt.md) \*pkt);

2884

2893struct net\_if\_timestamp\_cb {

2895 [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) node;

2896

2900 struct net\_pkt \*pkt;

2901

2905 struct net\_if \*iface;

2906

2908 net\_if\_timestamp\_callback\_t cb;

2909};

2910

2921void net\_if\_register\_timestamp\_cb(struct net\_if\_timestamp\_cb \*handle,

2922 struct [net\_pkt](structnet__pkt.md) \*pkt,

2923 struct [net\_if](structnet__if.md) \*iface,

2924 net\_if\_timestamp\_callback\_t cb);

2925

2931void net\_if\_unregister\_timestamp\_cb(struct net\_if\_timestamp\_cb \*handle);

2932

2938void net\_if\_call\_timestamp\_cb(struct [net\_pkt](structnet__pkt.md) \*pkt);

2939

2940/\*

2941 \* @brief Add timestamped TX buffer to be handled

2942 \*

2943 \* @param pkt Timestamped buffer

2944 \*/

2945void net\_if\_add\_tx\_timestamp(struct [net\_pkt](structnet__pkt.md) \*pkt);

2946#endif /\* CONFIG\_NET\_PKT\_TIMESTAMP \*/

2947

2957#if defined(CONFIG\_NET\_PROMISCUOUS\_MODE)

2958int [net\_if\_set\_promisc](group__net__if.md#gaf9f81f3b9697ca47f7674d85f37a8d80)(struct [net\_if](structnet__if.md) \*iface);

2959#else

[ 2960](group__net__if.md#gaf9f81f3b9697ca47f7674d85f37a8d80)static inline int [net\_if\_set\_promisc](group__net__if.md#gaf9f81f3b9697ca47f7674d85f37a8d80)(struct [net\_if](structnet__if.md) \*iface)

2961{

2962 ARG\_UNUSED(iface);

2963

2964 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

2965}

2966#endif

2967

2973#if defined(CONFIG\_NET\_PROMISCUOUS\_MODE)

2974void [net\_if\_unset\_promisc](group__net__if.md#ga9c8212c087883510050ac6a39ef0a7bf)(struct [net\_if](structnet__if.md) \*iface);

2975#else

[ 2976](group__net__if.md#ga9c8212c087883510050ac6a39ef0a7bf)static inline void [net\_if\_unset\_promisc](group__net__if.md#ga9c8212c087883510050ac6a39ef0a7bf)(struct [net\_if](structnet__if.md) \*iface)

2977{

2978 ARG\_UNUSED(iface);

2979}

2980#endif

2981

2990#if defined(CONFIG\_NET\_PROMISCUOUS\_MODE)

2991bool [net\_if\_is\_promisc](group__net__if.md#ga9f1a6eab849517734ec422deb0ba71f5)(struct [net\_if](structnet__if.md) \*iface);

2992#else

[ 2993](group__net__if.md#ga9f1a6eab849517734ec422deb0ba71f5)static inline bool [net\_if\_is\_promisc](group__net__if.md#ga9f1a6eab849517734ec422deb0ba71f5)(struct [net\_if](structnet__if.md) \*iface)

2994{

2995 ARG\_UNUSED(iface);

2996

2997 return false;

2998}

2999#endif

3000

[ 3010](group__net__if.md#ga3cddda628eca248246f9aa3b81938f95)static inline bool [net\_if\_are\_pending\_tx\_packets](group__net__if.md#ga3cddda628eca248246f9aa3b81938f95)(struct [net\_if](structnet__if.md) \*iface)

3011{

3012#if defined(CONFIG\_NET\_POWER\_MANAGEMENT)

3013 return !!iface->tx\_pending;

3014#else

3015 ARG\_UNUSED(iface);

3016

3017 return false;

3018#endif

3019}

3020

3021#ifdef CONFIG\_NET\_POWER\_MANAGEMENT

3029int net\_if\_suspend(struct [net\_if](structnet__if.md) \*iface);

3030

3038int net\_if\_resume(struct [net\_if](structnet__if.md) \*iface);

3039

3047bool net\_if\_is\_suspended(struct [net\_if](structnet__if.md) \*iface);

3048#endif /\* CONFIG\_NET\_POWER\_MANAGEMENT \*/

3049

[ 3057](group__net__if.md#gaa458b5f349c55007108b47b99f4954d5)bool [net\_if\_is\_wifi](group__net__if.md#gaa458b5f349c55007108b47b99f4954d5)(struct [net\_if](structnet__if.md) \*iface);

3058

[ 3064](group__net__if.md#ga6e89bbafb6c0acdc6bf51078e2027236)struct [net\_if](structnet__if.md) \*[net\_if\_get\_first\_wifi](group__net__if.md#ga6e89bbafb6c0acdc6bf51078e2027236)(void);

3065

[ 3071](group__net__if.md#ga0fc3ba6172956f6847027e0bd3d367de)struct [net\_if](structnet__if.md) \*[net\_if\_get\_wifi\_sta](group__net__if.md#ga0fc3ba6172956f6847027e0bd3d367de)(void);

3072

[ 3078](group__net__if.md#gaf830eab616191009d88f58b761694b49)struct [net\_if](structnet__if.md) \*[net\_if\_get\_wifi\_sap](group__net__if.md#gaf830eab616191009d88f58b761694b49)(void);

3079

[ 3094](group__net__if.md#ga5f653cd73c1ecd548a931eb7fbd170f7)int [net\_if\_get\_name](group__net__if.md#ga5f653cd73c1ecd548a931eb7fbd170f7)(struct [net\_if](structnet__if.md) \*iface, char \*buf, int len);

3095

[ 3110](group__net__if.md#ga05dec64966fc39e3deb0679b9585688b)int [net\_if\_set\_name](group__net__if.md#ga05dec64966fc39e3deb0679b9585688b)(struct [net\_if](structnet__if.md) \*iface, const char \*buf);

3111

[ 3119](group__net__if.md#ga1774ac036032bb0dc2c662f6f4f66a7f)int [net\_if\_get\_by\_name](group__net__if.md#ga1774ac036032bb0dc2c662f6f4f66a7f)(const char \*name);

3120

3122struct net\_if\_api {

3123 void (\*init)(struct [net\_if](structnet__if.md) \*iface);

3124};

3125

3126#define NET\_IF\_DHCPV4\_INIT \

3127 IF\_ENABLED(UTIL\_AND(IS\_ENABLED(CONFIG\_NET\_DHCPV4), \

3128 IS\_ENABLED(CONFIG\_NET\_NATIVE\_IPV4)), \

3129 (.dhcpv4.state = NET\_DHCPV4\_DISABLED,))

3130

3131#define NET\_IF\_DHCPV6\_INIT \

3132 IF\_ENABLED(UTIL\_AND(IS\_ENABLED(CONFIG\_NET\_DHCPV6), \

3133 IS\_ENABLED(CONFIG\_NET\_NATIVE\_IPV6)), \

3134 (.dhcpv6.state = NET\_DHCPV6\_DISABLED,))

3135

3136#define NET\_IF\_CONFIG\_INIT \

3137 .config = { \

3138 IF\_ENABLED(CONFIG\_NET\_IP, (.ip = {},)) \

3139 NET\_IF\_DHCPV4\_INIT \

3140 NET\_IF\_DHCPV6\_INIT \

3141 }

3142

3143#define NET\_IF\_GET\_NAME(dev\_id, sfx) \_\_net\_if\_##dev\_id##\_##sfx

3144#define NET\_IF\_DEV\_GET\_NAME(dev\_id, sfx) \_\_net\_if\_dev\_##dev\_id##\_##sfx

3145

3146#define NET\_IF\_GET(dev\_id, sfx) \

3147 ((struct net\_if \*)&NET\_IF\_GET\_NAME(dev\_id, sfx))

3148

3149#define NET\_IF\_INIT(dev\_id, sfx, \_l2, \_mtu, \_num\_configs) \

3150 static STRUCT\_SECTION\_ITERABLE(net\_if\_dev, \

3151 NET\_IF\_DEV\_GET\_NAME(dev\_id, sfx)) = { \

3152 .dev = &(DEVICE\_NAME\_GET(dev\_id)), \

3153 .l2 = &(NET\_L2\_GET\_NAME(\_l2)), \

3154 .l2\_data = &(NET\_L2\_GET\_DATA(dev\_id, sfx)), \

3155 .mtu = \_mtu, \

3156 .flags = {BIT(NET\_IF\_LOWER\_UP)}, \

3157 }; \

3158 static Z\_DECL\_ALIGN(struct net\_if) \

3159 NET\_IF\_GET\_NAME(dev\_id, sfx)[\_num\_configs] \

3160 \_\_used \_\_in\_section(\_net\_if, static, \

3161 dev\_id) = { \

3162 [0 ... (\_num\_configs - 1)] = { \

3163 .if\_dev = &(NET\_IF\_DEV\_GET\_NAME(dev\_id, sfx)), \

3164 NET\_IF\_CONFIG\_INIT \

3165 } \

3166 }

3167

3168#define NET\_IF\_OFFLOAD\_INIT(dev\_id, sfx, \_mtu) \

3169 static STRUCT\_SECTION\_ITERABLE(net\_if\_dev, \

3170 NET\_IF\_DEV\_GET\_NAME(dev\_id, sfx)) = { \

3171 .dev = &(DEVICE\_NAME\_GET(dev\_id)), \

3172 .mtu = \_mtu, \

3173 .l2 = &(NET\_L2\_GET\_NAME(OFFLOADED\_NETDEV)), \

3174 .flags = {BIT(NET\_IF\_LOWER\_UP)}, \

3175 }; \

3176 static Z\_DECL\_ALIGN(struct net\_if) \

3177 NET\_IF\_GET\_NAME(dev\_id, sfx)[NET\_IF\_MAX\_CONFIGS] \

3178 \_\_used \_\_in\_section(\_net\_if, static, \

3179 dev\_id) = { \

3180 [0 ... (NET\_IF\_MAX\_CONFIGS - 1)] = { \

3181 .if\_dev = &(NET\_IF\_DEV\_GET\_NAME(dev\_id, sfx)), \

3182 NET\_IF\_CONFIG\_INIT \

3183 } \

3184 }

3185

3187

3188/\* Network device initialization macros \*/

3189

3190#define Z\_NET\_DEVICE\_INIT\_INSTANCE(node\_id, dev\_id, name, instance, \

3191 init\_fn, pm, data, config, prio, \

3192 api, l2, l2\_ctx\_type, mtu) \

3193 Z\_DEVICE\_STATE\_DEFINE(dev\_id); \

3194 Z\_DEVICE\_DEFINE(node\_id, dev\_id, name, init\_fn, pm, data, \

3195 config, POST\_KERNEL, prio, api, \

3196 &Z\_DEVICE\_STATE\_NAME(dev\_id)); \

3197 NET\_L2\_DATA\_INIT(dev\_id, instance, l2\_ctx\_type); \

3198 NET\_IF\_INIT(dev\_id, instance, l2, mtu, NET\_IF\_MAX\_CONFIGS)

3199

3200#define Z\_NET\_DEVICE\_INIT(node\_id, dev\_id, name, init\_fn, pm, data, \

3201 config, prio, api, l2, l2\_ctx\_type, mtu) \

3202 Z\_NET\_DEVICE\_INIT\_INSTANCE(node\_id, dev\_id, name, 0, init\_fn, \

3203 pm, data, config, prio, api, l2, \

3204 l2\_ctx\_type, mtu)

3205

[ 3225](group__net__if.md#ga02971562c42494e2a5f71e1f8587e709)#define NET\_DEVICE\_INIT(dev\_id, name, init\_fn, pm, data, config, prio, \

3226 api, l2, l2\_ctx\_type, mtu) \

3227 Z\_NET\_DEVICE\_INIT(DT\_INVALID\_NODE, dev\_id, name, init\_fn, pm, \

3228 data, config, prio, api, l2, l2\_ctx\_type, mtu)

3229

[ 3248](group__net__if.md#gab1f762b01ae7bc37cd4a25724c123dda)#define NET\_DEVICE\_DT\_DEFINE(node\_id, init\_fn, pm, data, \

3249 config, prio, api, l2, l2\_ctx\_type, mtu) \

3250 Z\_NET\_DEVICE\_INIT(node\_id, Z\_DEVICE\_DT\_DEV\_ID(node\_id), \

3251 DEVICE\_DT\_NAME(node\_id), init\_fn, pm, data, \

3252 config, prio, api, l2, l2\_ctx\_type, mtu)

3253

[ 3262](group__net__if.md#ga7edd8bc59444d92cad0371c36f9949b7)#define NET\_DEVICE\_DT\_INST\_DEFINE(inst, ...) \

3263 NET\_DEVICE\_DT\_DEFINE(DT\_DRV\_INST(inst), \_\_VA\_ARGS\_\_)

3264

[ 3288](group__net__if.md#gacc7edecdd9de9920cc155977d8fec2a2)#define NET\_DEVICE\_INIT\_INSTANCE(dev\_id, name, instance, init\_fn, pm, \

3289 data, config, prio, api, l2, \

3290 l2\_ctx\_type, mtu) \

3291 Z\_NET\_DEVICE\_INIT\_INSTANCE(DT\_INVALID\_NODE, dev\_id, name, \

3292 instance, init\_fn, pm, data, config, \

3293 prio, api, l2, l2\_ctx\_type, mtu)

3294

[ 3317](group__net__if.md#ga50702b043a0791e59e7d5679dda1d9e8)#define NET\_DEVICE\_DT\_DEFINE\_INSTANCE(node\_id, instance, init\_fn, pm, \

3318 data, config, prio, api, l2, \

3319 l2\_ctx\_type, mtu) \

3320 Z\_NET\_DEVICE\_INIT\_INSTANCE(node\_id, \

3321 Z\_DEVICE\_DT\_DEV\_ID(node\_id), \

3322 DEVICE\_DT\_NAME(node\_id), instance, \

3323 init\_fn, pm, data, config, prio, \

3324 api, l2, l2\_ctx\_type, mtu)

3325

[ 3335](group__net__if.md#gabe4b8589996a53cbc50b76c8ea15aa0c)#define NET\_DEVICE\_DT\_INST\_DEFINE\_INSTANCE(inst, ...) \

3336 NET\_DEVICE\_DT\_DEFINE\_INSTANCE(DT\_DRV\_INST(inst), \_\_VA\_ARGS\_\_)

3337

3338#define Z\_NET\_DEVICE\_OFFLOAD\_INIT(node\_id, dev\_id, name, init\_fn, pm, \

3339 data, config, prio, api, mtu) \

3340 Z\_DEVICE\_STATE\_DEFINE(dev\_id); \

3341 Z\_DEVICE\_DEFINE(node\_id, dev\_id, name, init\_fn, pm, data, \

3342 config, POST\_KERNEL, prio, api, \

3343 &Z\_DEVICE\_STATE\_NAME(dev\_id)); \

3344 NET\_IF\_OFFLOAD\_INIT(dev\_id, 0, mtu)

3345

[ 3365](group__net__if.md#ga255672607b7958db3f464d2a57a7e635)#define NET\_DEVICE\_OFFLOAD\_INIT(dev\_id, name, init\_fn, pm, data, \

3366 config, prio, api, mtu) \

3367 Z\_NET\_DEVICE\_OFFLOAD\_INIT(DT\_INVALID\_NODE, dev\_id, name, \

3368 init\_fn, pm, data, config, prio, api, \

3369 mtu)

3370

[ 3389](group__net__if.md#gab2b287025e194dec1fab24e44d95362f)#define NET\_DEVICE\_DT\_OFFLOAD\_DEFINE(node\_id, init\_fn, pm, data, \

3390 config, prio, api, mtu) \

3391 Z\_NET\_DEVICE\_OFFLOAD\_INIT(node\_id, Z\_DEVICE\_DT\_DEV\_ID(node\_id), \

3392 DEVICE\_DT\_NAME(node\_id), init\_fn, pm, \

3393 data, config, prio, api, mtu)

3394

[ 3404](group__net__if.md#ga1cab6943a28e3d3754e36623834b93fd)#define NET\_DEVICE\_DT\_INST\_OFFLOAD\_DEFINE(inst, ...) \

3405 NET\_DEVICE\_DT\_OFFLOAD\_DEFINE(DT\_DRV\_INST(inst), \_\_VA\_ARGS\_\_)

3406

[ 3412](group__net__if.md#ga6c081875a6f5a848b3ad2fd220c63c3c)#define NET\_IFACE\_COUNT(\_dst) \

3413 do { \

3414 extern struct net\_if \_net\_if\_list\_start[]; \

3415 extern struct net\_if \_net\_if\_list\_end[]; \

3416 \*(\_dst) = ((uintptr\_t)\_net\_if\_list\_end - \

3417 (uintptr\_t)\_net\_if\_list\_start) / \

3418 sizeof(struct net\_if); \

3419 } while (0)

3420

3421#ifdef \_\_cplusplus

3422}

3423#endif

3424

3425#include <zephyr/syscalls/net\_if.h>

3426

3430

3431#endif /\* ZEPHYR\_INCLUDE\_NET\_NET\_IF\_H\_ \*/

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

**Definition** kernel.h:1363

[sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda)

unsigned short int sa\_family\_t

Socket address family type.

**Definition** net\_ip.h:164

[net\_addr\_state](group__ip__4__6.md#ga32e58fc83532ef57eeb6ff952f17288d)

net\_addr\_state

What is the current state of the network address.

**Definition** net\_ip.h:500

[net\_addr\_type](group__ip__4__6.md#gafecee2d4a331dc85ad962b81a6303e41)

net\_addr\_type

How the network address is assigned to network interface.

**Definition** net\_ip.h:508

[k\_mutex\_unlock](group__mutex__apis.md#ga360f4c0e7258b0d7030cdb1f452b2c31)

int k\_mutex\_unlock(struct k\_mutex \*mutex)

Unlock a mutex.

[k\_mutex\_lock](group__mutex__apis.md#ga850549358645249c285669baa49c33b0)

int k\_mutex\_lock(struct k\_mutex \*mutex, k\_timeout\_t timeout)

Lock a mutex.

[net\_verdict](group__net__core.md#ga8e5393f3bdd85491f221324e637c3896)

net\_verdict

Net Verdict.

**Definition** net\_core.h:100

[net\_hostname\_set\_postfix](group__net__hostname.md#ga6aa3799b3b0d7eec7fb8b276485ae2c5)

static int net\_hostname\_set\_postfix(const uint8\_t \*hostname\_postfix, int postfix\_len)

Set the device hostname postfix.

**Definition** hostname.h:108

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

**Definition** net\_if.h:2832

[net\_if\_is\_admin\_up](group__net__if.md#ga099a484a654ad9af35d3212fc2c995b2)

static bool net\_if\_is\_admin\_up(struct net\_if \*iface)

Check if interface was brought up by the administrator.

**Definition** net\_if.h:2798

[net\_if\_set\_default](group__net__if.md#ga0a1f27ec893e1af3c97f130be4616589)

void net\_if\_set\_default(struct net\_if \*iface)

Set the default network interface.

[net\_if\_ipv4\_addr\_lookup\_by\_index](group__net__if.md#ga0a22661727316517685afcd551e7b38e)

int net\_if\_ipv4\_addr\_lookup\_by\_index(const struct in\_addr \*addr)

Check if this IPv4 address belongs to one of the interface indices.

[net\_if\_mcast\_callback\_t](group__net__if.md#ga0d64291573740a67eae7ff3fcc0910c5)

void(\* net\_if\_mcast\_callback\_t)(struct net\_if \*iface, const struct net\_addr \*addr, bool is\_joined)

Define a callback that is called whenever a IPv6 or IPv4 multicast address group is joined or left.

**Definition** net\_if.h:1565

[net\_if\_link\_callback\_t](group__net__if.md#ga0f87d5753fcd7cce40ecd161e6c91078)

void(\* net\_if\_link\_callback\_t)(struct net\_if \*iface, struct net\_linkaddr \*dst, int status)

Define callback that is called after a network packet has been sent.

**Definition** net\_if.h:2603

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

**Definition** net\_if.h:855

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

**Definition** net\_if.h:2343

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

[net\_if\_ipv6\_set\_mcast\_hop\_limit](group__net__if.md#ga3792cb18e34693b3c49f6dbccda3cf61)

void net\_if\_ipv6\_set\_mcast\_hop\_limit(struct net\_if \*iface, uint8\_t hop\_limit)

Set the default IPv6 multicast hop limit of a given interface.

[net\_if\_ipv6\_set\_hop\_limit](group__net__if.md#ga37b1d83f3ef7ab5996a86e7f7f3d9c72)

void net\_if\_ipv6\_set\_hop\_limit(struct net\_if \*iface, uint8\_t hop\_limit)

Set the default IPv6 hop limit of a given interface.

[net\_if\_l2\_data](group__net__if.md#ga3cad2d51fc9cc225619585e06e252db0)

static void \* net\_if\_l2\_data(struct net\_if \*iface)

Get a pointer to the interface L2 private data.

**Definition** net\_if.h:926

[net\_if\_are\_pending\_tx\_packets](group__net__if.md#ga3cddda628eca248246f9aa3b81938f95)

static bool net\_if\_are\_pending\_tx\_packets(struct net\_if \*iface)

Check if there are any pending TX network data for a given network interface.

**Definition** net\_if.h:3010

[net\_if\_ipv4\_get\_netmask](group__net__if.md#ga41aeb0e7c5f9bc837f7b2ec13401afd1)

struct in\_addr net\_if\_ipv4\_get\_netmask(struct net\_if \*iface)

Get IPv4 netmask of an interface.

[net\_if\_flag\_test\_and\_set](group__net__if.md#ga42e7482191a92007960601f8bb621dca)

static bool net\_if\_flag\_test\_and\_set(struct net\_if \*iface, enum net\_if\_flag value)

Test and set a value in network interface flags.

**Definition** net\_if.h:785

[net\_if\_ipv4\_addr\_rm](group__net__if.md#ga4433304d46b6559604486b828e7d9dec)

bool net\_if\_ipv4\_addr\_rm(struct net\_if \*iface, const struct in\_addr \*addr)

Remove a IPv4 address from an interface.

[net\_if\_ipv4\_router\_add](group__net__if.md#ga44984001411077c7a2ef68afb361b40f)

struct net\_if\_router \* net\_if\_ipv4\_router\_add(struct net\_if \*iface, struct in\_addr \*addr, bool is\_default, uint16\_t router\_lifetime)

Add IPv4 router to the system.

[net\_if\_get\_link\_addr](group__net__if.md#ga467186e964bf721e14fed38392f21872)

static struct net\_linkaddr \* net\_if\_get\_link\_addr(struct net\_if \*iface)

Get an network interface's link address.

**Definition** net\_if.h:1075

[net\_if\_ipv6\_maddr\_join](group__net__if.md#ga49dbc954015307222f176f4149829b76)

void net\_if\_ipv6\_maddr\_join(struct net\_if \*iface, struct net\_if\_mcast\_addr \*addr)

Mark a given multicast address to be joined.

[net\_if\_ipv6\_select\_src\_addr](group__net__if.md#ga50689a1afdb37a7087bf47a12cc50438)

static const struct in6\_addr \* net\_if\_ipv6\_select\_src\_addr(struct net\_if \*iface, const struct in6\_addr \*dst)

Get a IPv6 source address that should be used when sending network data to destination.

**Definition** net\_if.h:2006

[net\_if\_nbr\_reachability\_hint](group__net__if.md#ga51af469ff3d7d9f760d63a8a9c7be8b5)

static void net\_if\_nbr\_reachability\_hint(struct net\_if \*iface, const struct in6\_addr \*ipv6\_addr)

Provide a reachability hint for IPv6 Neighbor Discovery.

**Definition** net\_if.h:1148

[net\_if\_offload](group__net__if.md#ga520939e94620ca75475a71f153df6d4a)

static struct net\_offload \* net\_if\_offload(struct net\_if \*iface)

Return the IP offload plugin.

**Definition** net\_if.h:992

[net\_if\_set\_link\_addr](group__net__if.md#ga52b41b2f8b7d3405338a0539542677a0)

static int net\_if\_set\_link\_addr(struct net\_if \*iface, uint8\_t \*addr, uint8\_t len, enum net\_link\_type type)

Set a network interface's link address.

**Definition** net\_if.h:1216

[net\_if\_flag\_set](group__net__if.md#ga52f9fca13e9f836799e0e40f581744d2)

static void net\_if\_flag\_set(struct net\_if \*iface, enum net\_if\_flag value)

Set a value in network interface flags.

**Definition** net\_if.h:768

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

[net\_if\_ipv6\_addr\_foreach](group__net__if.md#ga5ac646ad7fda0fa48e78c15b4ca52d50)

void net\_if\_ipv6\_addr\_foreach(struct net\_if \*iface, net\_if\_ip\_addr\_cb\_t cb, void \*user\_data)

Go through all IPv6 addresses on a network interface and call callback for each used address.

[net\_if\_ipv6\_select\_src\_addr\_hint](group__net__if.md#ga5cf4717e632f712045dd4fe81b30245c)

static const struct in6\_addr \* net\_if\_ipv6\_select\_src\_addr\_hint(struct net\_if \*iface, const struct in6\_addr \*dst, int flags)

Get a IPv6 source address that should be used when sending network data to destination.

**Definition** net\_if.h:2034

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

**Definition** net\_if.h:964

[net\_if\_is\_dormant](group__net__if.md#ga6e2e6102271c37acaa59c54e2aa6b413)

static bool net\_if\_is\_dormant(struct net\_if \*iface)

Check if the interface is dormant.

**Definition** net\_if.h:2868

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

**Definition** net\_if.h:1527

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

**Definition** net\_if.h:1251

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

**Definition** net\_if.h:2774

[net\_if\_need\_calc\_rx\_checksum](group__net__if.md#ga8048e722f6442bcd5b6881bd71e791a5)

bool net\_if\_need\_calc\_rx\_checksum(struct net\_if \*iface, enum net\_if\_checksum\_type chksum\_type)

Check if received network packet checksum calculation can be avoided or not.

[net\_if\_ipv6\_set\_reachable\_time](group__net__if.md#ga8328266b870fd200660cb2becaab3de4)

static void net\_if\_ipv6\_set\_reachable\_time(struct net\_if\_ipv6 \*ipv6)

Set IPv6 reachable time for a given interface.

**Definition** net\_if.h:1932

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

**Definition** net\_if.h:2669

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

[net\_if\_need\_calc\_tx\_checksum](group__net__if.md#ga9634c3e71e934ab3a07bec989b364663)

bool net\_if\_need\_calc\_tx\_checksum(struct net\_if \*iface, enum net\_if\_checksum\_type chksum\_type)

Check if network packet checksum calculation can be avoided or not when sending the packet.

[net\_if\_start\_dad](group__net__if.md#ga9655c010ccbf989e9328271f5dbcc685)

static void net\_if\_start\_dad(struct net\_if \*iface)

Start duplicate address detection procedure.

**Definition** net\_if.h:1105

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

**Definition** net\_if.h:2976

[net\_if\_socket\_offload\_set](group__net__if.md#ga9db52875580115c743b1f35cd6c46796)

static void net\_if\_socket\_offload\_set(struct net\_if \*iface, net\_socket\_create\_t socket\_offload)

Set the function to create an offloaded socket.

**Definition** net\_if.h:1033

[net\_if\_ipv6\_get\_reachable\_time](group__net__if.md#ga9dd1f91edbb519a6a079f363c33efacf)

static uint32\_t net\_if\_ipv6\_get\_reachable\_time(struct net\_if \*iface)

Get IPv6 reachable timeout specified for a given interface.

**Definition** net\_if.h:1901

[net\_if\_is\_promisc](group__net__if.md#ga9f1a6eab849517734ec422deb0ba71f5)

static bool net\_if\_is\_promisc(struct net\_if \*iface)

Check if promiscuous mode is set or not.

**Definition** net\_if.h:2993

[net\_if\_ipv4\_maddr\_is\_joined](group__net__if.md#gaa30769fc8016f1a7496b3ede277d8d8a)

static bool net\_if\_ipv4\_maddr\_is\_joined(struct net\_if\_mcast\_addr \*addr)

Check if given multicast address is joined or not.

**Definition** net\_if.h:2313

[net\_if\_ipv6\_prefix\_set\_lf](group__net__if.md#gaa3c711e814fb6a4e552b4ef723d0baa0)

static void net\_if\_ipv6\_prefix\_set\_lf(struct net\_if\_ipv6\_prefix \*prefix, bool is\_infinite)

Set the infinite status of the prefix.

**Definition** net\_if.h:1706

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

**Definition** net\_if.h:1127

[net\_if\_ipv6\_calc\_reachable\_time](group__net__if.md#gab1861b5cefa73b4eefbb447cb1438cdc)

uint32\_t net\_if\_ipv6\_calc\_reachable\_time(struct net\_if\_ipv6 \*ipv6)

Calculate next reachable time value for IPv6 reachable time.

[net\_if\_ipv6\_set\_base\_reachable\_time](group__net__if.md#gab3939d735b660f8f02124df656ceba2c)

static void net\_if\_ipv6\_set\_base\_reachable\_time(struct net\_if \*iface, uint32\_t reachable\_time)

Set IPv6 reachable time for a given interface.

**Definition** net\_if.h:1876

[net\_if\_ipv6\_addr\_lookup\_by\_iface](group__net__if.md#gab53eabb540a4487d83f27c8e319c736a)

struct net\_if\_addr \* net\_if\_ipv6\_addr\_lookup\_by\_iface(struct net\_if \*iface, struct in6\_addr \*addr)

Check if this IPv6 address belongs to this specific interfaces.

[net\_if\_ip\_addr\_cb\_t](group__net__if.md#gab58d8561a4f21899e2db34043d346516)

void(\* net\_if\_ip\_addr\_cb\_t)(struct net\_if \*iface, struct net\_if\_addr \*addr, void \*user\_data)

Callback used while iterating over network interface IP addresses.

**Definition** net\_if.h:1483

[net\_if\_ipv6\_maddr\_foreach](group__net__if.md#gab677496fb2e27be2df299a346e9c7132)

void net\_if\_ipv6\_maddr\_foreach(struct net\_if \*iface, net\_if\_ip\_maddr\_cb\_t cb, void \*user\_data)

Go through all IPv6 multicast addresses on a network interface and call callback for each used addres...

[net\_if\_flag\_test\_and\_clear](group__net__if.md#gab8f371c7f8890cf4728177f6595141d7)

static bool net\_if\_flag\_test\_and\_clear(struct net\_if \*iface, enum net\_if\_flag value)

Test and clear a value in network interface flags.

**Definition** net\_if.h:817

[net\_if\_start\_rs](group__net__if.md#gab9bdb7f8a9eeed4d9b70965b8af82cb7)

void net\_if\_start\_rs(struct net\_if \*iface)

Start neighbor discovery and send router solicitation message.

[net\_if\_ipv6\_maddr\_is\_joined](group__net__if.md#gabe2c16a378a35a22d008bff9142e5449)

static bool net\_if\_ipv6\_maddr\_is\_joined(struct net\_if\_mcast\_addr \*addr)

Check if given multicast address is joined or not.

**Definition** net\_if.h:1633

[net\_if\_ipv6\_addr\_rm\_by\_index](group__net__if.md#gac159e3b0fbf558d5fb09774141da7d6d)

bool net\_if\_ipv6\_addr\_rm\_by\_index(int index, const struct in6\_addr \*addr)

Remove an IPv6 address from an interface by index.

[net\_if\_cb\_t](group__net__if.md#gac48ab8e6337e7cf387af9b293f254a80)

void(\* net\_if\_cb\_t)(struct net\_if \*iface, void \*user\_data)

Callback used while iterating over network interfaces.

**Definition** net\_if.h:2747

[net\_if\_ipv4\_addr\_rm\_by\_index](group__net__if.md#gac5bf15f948ab195cecce98d1b40bda37)

bool net\_if\_ipv4\_addr\_rm\_by\_index(int index, const struct in\_addr \*addr)

Remove a IPv4 address from an interface by interface index.

[net\_if\_ipv6\_get\_global\_addr](group__net__if.md#gaca7d686c772deac13a027cc046333126)

struct in6\_addr \* net\_if\_ipv6\_get\_global\_addr(enum net\_addr\_state state, struct net\_if \*\*iface)

Return global IPv6 address from the first interface that has a global IPv6 address matching the given...

[net\_if\_get\_mtu](group__net__if.md#gacddc98531c5748db5a34f5c3a3e96e86)

static uint16\_t net\_if\_get\_mtu(struct net\_if \*iface)

Get an network interface's MTU.

**Definition** net\_if.h:1234

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

**Definition** net\_if.h:2458

[net\_if\_ipv6\_get\_ll](group__net__if.md#gad6f3e1e349e281887352652f6f32274e)

struct in6\_addr \* net\_if\_ipv6\_get\_ll(struct net\_if \*iface, enum net\_addr\_state addr\_state)

Get a IPv6 link local address in a given state.

[net\_if\_ipv6\_set\_retrans\_timer](group__net__if.md#gad74566e5a34f447d2ac63d2c0e82eeff)

static void net\_if\_ipv6\_set\_retrans\_timer(struct net\_if \*iface, uint32\_t retrans\_timer)

Set IPv6 retransmit timer for a given interface.

**Definition** net\_if.h:1951

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

**Definition** net\_if.h:1754

[net\_if\_ipv4\_maddr\_lookup](group__net__if.md#gadc1514a0d6852de9dbce043bc99d4eb0)

struct net\_if\_mcast\_addr \* net\_if\_ipv4\_maddr\_lookup(const struct in\_addr \*addr, struct net\_if \*\*iface)

Check if this IPv4 multicast address belongs to a specific interface or one of the interfaces.

[net\_if\_router\_rm](group__net__if.md#gadc87242eb7205362a308b3c4437bf76d)

void net\_if\_router\_rm(struct net\_if\_router \*router)

Remove a router from the system.

[net\_if\_ipv6\_get\_retrans\_timer](group__net__if.md#gaddbf5a6ba412e6bdb7e31568fe827bd0)

static uint32\_t net\_if\_ipv6\_get\_retrans\_timer(struct net\_if \*iface)

Get IPv6 retransmit timer specified for a given interface.

**Definition** net\_if.h:1975

[net\_if\_ipv4\_set\_gw\_by\_index](group__net__if.md#gadef49124c331817165475c69fb9104e0)

bool net\_if\_ipv4\_set\_gw\_by\_index(int index, const struct in\_addr \*gw)

Set IPv4 gateway for an interface index.

[net\_if\_ipv4\_get\_netmask\_by\_addr](group__net__if.md#gadfad7d9232bf58c5626266387a2eb761)

struct in\_addr net\_if\_ipv4\_get\_netmask\_by\_addr(struct net\_if \*iface, const struct in\_addr \*addr)

Get IPv4 netmask related to an address of an interface.

[net\_if\_oper\_state](group__net__if.md#gadfe9d90f24046cd9bd4bbee096e747b9)

net\_if\_oper\_state

Network interface operational status (RFC 2863).

**Definition** net\_if.h:286

[net\_if\_ipv6\_addr\_add](group__net__if.md#gae00484a7fe32671a4ca04ff525e640c6)

struct net\_if\_addr \* net\_if\_ipv6\_addr\_add(struct net\_if \*iface, struct in6\_addr \*addr, enum net\_addr\_type addr\_type, uint32\_t vlifetime)

Add a IPv6 address to an interface.

[net\_if\_ipv6\_select\_src\_iface](group__net__if.md#gae1495ac9e743be54b8d90bd4ff4700ab)

static struct net\_if \* net\_if\_ipv6\_select\_src\_iface(const struct in6\_addr \*dst)

Get a network interface that should be used when sending IPv6 network data to destination.

**Definition** net\_if.h:2057

[net\_if\_flag\_is\_set](group__net__if.md#gae1f373ddd61c18a81481d8ddcfb12543)

static bool net\_if\_flag\_is\_set(struct net\_if \*iface, enum net\_if\_flag value)

Check if a value in network interface flags is set.

**Definition** net\_if.h:834

[net\_if\_config\_get](group__net__if.md#gae2323a72714e29836d8296dfc330f7fd)

static struct net\_if\_config \* net\_if\_config\_get(struct net\_if \*iface)

Get network interface IP config.

**Definition** net\_if.h:1302

[net\_if\_get\_config](group__net__if.md#gae271e0e4dcb031a83d9908e597a45048)

static struct net\_if\_config \* net\_if\_get\_config(struct net\_if \*iface)

Return network configuration for this network interface.

**Definition** net\_if.h:1090

[net\_if\_ipv4\_maddr\_join](group__net__if.md#gae275a5e75817aa178d36f422573ad76a)

void net\_if\_ipv4\_maddr\_join(struct net\_if \*iface, struct net\_if\_mcast\_addr \*addr)

Mark a given multicast address to be joined.

[net\_if\_addr\_set\_lf](group__net__if.md#gae66f6e7bd31545e6161fcd4600fe5842)

static void net\_if\_addr\_set\_lf(struct net\_if\_addr \*ifaddr, bool is\_infinite)

Set the infinite status of the network interface address.

**Definition** net\_if.h:1269

[net\_if\_flag](group__net__if.md#gae691e5537917ffce27ad0db82c730371)

net\_if\_flag

Network interface flags.

**Definition** net\_if.h:228

[net\_if\_ipv4\_maddr\_foreach](group__net__if.md#gae82f53c670f602e9c37b65abb6dfaec7)

void net\_if\_ipv4\_maddr\_foreach(struct net\_if \*iface, net\_if\_ip\_maddr\_cb\_t cb, void \*user\_data)

Go through all IPv4 multicast addresses on a network interface and call callback for each used addres...

[net\_if\_ipv6\_prefix\_get](group__net__if.md#gae9f98dff661d52c5e3e5e185f0ed9cc0)

struct net\_if\_ipv6\_prefix \* net\_if\_ipv6\_prefix\_get(struct net\_if \*iface, const struct in6\_addr \*addr)

Return prefix that corresponds to this IPv6 address.

[net\_if\_get\_device](group__net__if.md#gaeb8c703f273bc07ae9bb7a0d8bfe6f3d)

static const struct device \* net\_if\_get\_device(struct net\_if \*iface)

Get an network interface's device.

**Definition** net\_if.h:941

[net\_if\_is\_offloaded](group__net__if.md#gaecedc93a6dab2c57fe686718ea4d78af)

bool net\_if\_is\_offloaded(struct net\_if \*iface)

Return offload status of a given network interface.

[net\_socket\_create\_t](group__net__if.md#gaef3dfe26195514aac625e9f22e399759)

int(\* net\_socket\_create\_t)(int, int, int)

A function prototype to create an offloaded socket.

**Definition** net\_if.h:616

[net\_if\_ipv6\_addr\_update\_lifetime](group__net__if.md#gaef8a6752a201f81636c4ffc1ebba4a25)

void net\_if\_ipv6\_addr\_update\_lifetime(struct net\_if\_addr \*ifaddr, uint32\_t vlifetime)

Update validity lifetime time of an IPv6 address.

[net\_if\_ipv6\_maddr\_rm](group__net__if.md#gaf0ce126bb5019ff5f5ff0876b9712ad9)

bool net\_if\_ipv6\_maddr\_rm(struct net\_if \*iface, const struct in6\_addr \*addr)

Remove an IPv6 multicast address from an interface.

[net\_if\_is\_socket\_offloaded](group__net__if.md#gaf308baf2241fa455b50b439b7fab3f1e)

static bool net\_if\_is\_socket\_offloaded(struct net\_if \*iface)

Return the socket offload status.

**Definition** net\_if.h:1013

[net\_if\_get\_wifi\_sap](group__net__if.md#gaf830eab616191009d88f58b761694b49)

struct net\_if \* net\_if\_get\_wifi\_sap(void)

Get first Wi-Fi network Soft-AP interface.

[net\_if\_set\_promisc](group__net__if.md#gaf9f81f3b9697ca47f7674d85f37a8d80)

static int net\_if\_set\_promisc(struct net\_if \*iface)

Set network interface into promiscuous mode.

**Definition** net\_if.h:2960

[net\_if\_l2](group__net__if.md#gafa451f6118529d1d084704d00b2aae20)

static const struct net\_l2 \* net\_if\_l2(struct net\_if \*iface)

Get a pointer to the interface L2.

**Definition** net\_if.h:900

[net\_if\_socket\_offload](group__net__if.md#gafb2bbaec96c4759d920b2866c0b3ef3a)

static net\_socket\_create\_t net\_if\_socket\_offload(struct net\_if \*iface)

Return the function to create an offloaded socket.

**Definition** net\_if.h:1054

[net\_if\_ipv4\_select\_src\_iface](group__net__if.md#gafea1a35f452ad8168855852cbfdf0024)

static struct net\_if \* net\_if\_ipv4\_select\_src\_iface(const struct in\_addr \*dst)

Get a network interface that should be used when sending IPv4 network data to destination.

**Definition** net\_if.h:2434

[net\_if\_flag\_clear](group__net__if.md#gaff751b6a92b0c608ecfc50e8c0587fd3)

static void net\_if\_flag\_clear(struct net\_if \*iface, enum net\_if\_flag value)

Clear a value in network interface flags.

**Definition** net\_if.h:800

[NET\_IF\_CHECKSUM\_IPV4\_ICMP](group__net__if.md#gga8db412ae79c64cafe81a66f5acb2f8e9a2aef87c97f22fdccdf1925d2687436b1)

@ NET\_IF\_CHECKSUM\_IPV4\_ICMP

Interface supports checksum calculation for ICMP4 payload in IPv4.

**Definition** net\_if.h:2679

[NET\_IF\_CHECKSUM\_IPV6\_TCP](group__net__if.md#gga8db412ae79c64cafe81a66f5acb2f8e9a31e33593e4e7f7f9b36e319e0991ab13)

@ NET\_IF\_CHECKSUM\_IPV6\_TCP

Interface supports checksum calculation for TCP payload in IPv6.

**Definition** net\_if.h:2683

[NET\_IF\_CHECKSUM\_IPV6\_UDP](group__net__if.md#gga8db412ae79c64cafe81a66f5acb2f8e9a70b1272e2125cea9204bae144fd86660)

@ NET\_IF\_CHECKSUM\_IPV6\_UDP

Interface supports checksum calculation for UDP payload in IPv6.

**Definition** net\_if.h:2686

[NET\_IF\_CHECKSUM\_IPV4\_HEADER](group__net__if.md#gga8db412ae79c64cafe81a66f5acb2f8e9a75e4a0946d0e6755ebd7cc62558aee30)

@ NET\_IF\_CHECKSUM\_IPV4\_HEADER

Interface supports IP version 4 header checksum calculation.

**Definition** net\_if.h:2671

[NET\_IF\_CHECKSUM\_IPV4\_TCP](group__net__if.md#gga8db412ae79c64cafe81a66f5acb2f8e9aaed32a3cb700eac3b67c6c7e5a0cd0ad)

@ NET\_IF\_CHECKSUM\_IPV4\_TCP

Interface supports checksum calculation for TCP payload in IPv4.

**Definition** net\_if.h:2673

[NET\_IF\_CHECKSUM\_IPV6\_HEADER](group__net__if.md#gga8db412ae79c64cafe81a66f5acb2f8e9ab204c7d5fddbd2c11e07a8831df6c00b)

@ NET\_IF\_CHECKSUM\_IPV6\_HEADER

Interface supports IP version 6 header checksum calculation.

**Definition** net\_if.h:2681

[NET\_IF\_CHECKSUM\_IPV6\_ICMP](group__net__if.md#gga8db412ae79c64cafe81a66f5acb2f8e9af5b3bc7cb5e9771cd9fd57d9fda4c3b3)

@ NET\_IF\_CHECKSUM\_IPV6\_ICMP

Interface supports checksum calculation for ICMP6 payload in IPv6.

**Definition** net\_if.h:2689

[NET\_IF\_CHECKSUM\_IPV4\_UDP](group__net__if.md#gga8db412ae79c64cafe81a66f5acb2f8e9afe1eaaa765c8ec3c61618e943cd3f1c3)

@ NET\_IF\_CHECKSUM\_IPV4\_UDP

Interface supports checksum calculation for UDP payload in IPv4.

**Definition** net\_if.h:2676

[NET\_IF\_OPER\_TESTING](group__net__if.md#ggadfe9d90f24046cd9bd4bbee096e747b9a2240173b5c247ab5eb0a9a6afafb296f)

@ NET\_IF\_OPER\_TESTING

Training mode.

**Definition** net\_if.h:291

[NET\_IF\_OPER\_DORMANT](group__net__if.md#ggadfe9d90f24046cd9bd4bbee096e747b9a5cbe2aa27a444444d4acf122113d430d)

@ NET\_IF\_OPER\_DORMANT

Waiting external action.

**Definition** net\_if.h:292

[NET\_IF\_OPER\_UP](group__net__if.md#ggadfe9d90f24046cd9bd4bbee096e747b9a6b99bfc28d831292029761d74209ee03)

@ NET\_IF\_OPER\_UP

Interface is up.

**Definition** net\_if.h:293

[NET\_IF\_OPER\_NOTPRESENT](group__net__if.md#ggadfe9d90f24046cd9bd4bbee096e747b9a8f9f55840e75693163197baae9d50c32)

@ NET\_IF\_OPER\_NOTPRESENT

Hardware missing.

**Definition** net\_if.h:288

[NET\_IF\_OPER\_UNKNOWN](group__net__if.md#ggadfe9d90f24046cd9bd4bbee096e747b9ac7cae092ea6ceeb62499a9b435ac4b58)

@ NET\_IF\_OPER\_UNKNOWN

Initial (unknown) value.

**Definition** net\_if.h:287

[NET\_IF\_OPER\_DOWN](group__net__if.md#ggadfe9d90f24046cd9bd4bbee096e747b9adb20a95215310c420f8dae7e17a2f367)

@ NET\_IF\_OPER\_DOWN

Interface is down.

**Definition** net\_if.h:289

[NET\_IF\_OPER\_LOWERLAYERDOWN](group__net__if.md#ggadfe9d90f24046cd9bd4bbee096e747b9ae7e9b8b12ae618a5ee1483dee916aab4)

@ NET\_IF\_OPER\_LOWERLAYERDOWN

Lower layer interface is down.

**Definition** net\_if.h:290

[NET\_IF\_NO\_AUTO\_START](group__net__if.md#ggae691e5537917ffce27ad0db82c730371a0babb762301878eaf8ef8a05213ecf05)

@ NET\_IF\_NO\_AUTO\_START

Do not start the interface immediately after initialization.

**Definition** net\_if.h:244

[NET\_IF\_IPV6\_NO\_MLD](group__net__if.md#ggae691e5537917ffce27ad0db82c730371a1d362cfabb58eb220ddb069431221fbe)

@ NET\_IF\_IPV6\_NO\_MLD

IPv6 Multicast Listener Discovery disabled.

**Definition** net\_if.h:274

[NET\_IF\_POINTOPOINT](group__net__if.md#ggae691e5537917ffce27ad0db82c730371a3256ef2d537c85b4c2b33b92935e1009)

@ NET\_IF\_POINTOPOINT

Interface is pointopoint.

**Definition** net\_if.h:233

[NET\_IF\_IPV6\_NO\_ND](group__net__if.md#ggae691e5537917ffce27ad0db82c730371a542ecce860ef3bf2df493da8d4c6a2f7)

@ NET\_IF\_IPV6\_NO\_ND

IPv6 Neighbor Discovery disabled.

**Definition** net\_if.h:271

[NET\_IF\_FORWARD\_MULTICASTS](group__net__if.md#ggae691e5537917ffce27ad0db82c730371a581971c9d93a910c4c607da45aa2e4ac)

@ NET\_IF\_FORWARD\_MULTICASTS

Flag defines if received multicasts of other interface are forwarded on this interface.

**Definition** net\_if.h:253

[NET\_IF\_IPV4](group__net__if.md#ggae691e5537917ffce27ad0db82c730371a67d2c0fe390ab16f347ee2dc0a056329)

@ NET\_IF\_IPV4

Interface supports IPv4.

**Definition** net\_if.h:256

[NET\_IF\_PROMISC](group__net__if.md#ggae691e5537917ffce27ad0db82c730371a700d92a5b0de3c779e59806137b35141)

@ NET\_IF\_PROMISC

Interface is in promiscuous mode.

**Definition** net\_if.h:236

[NET\_IF\_DORMANT](group__net__if.md#ggae691e5537917ffce27ad0db82c730371a7dd1db72a37b1fbc4c4491ce1c75238d)

@ NET\_IF\_DORMANT

Driver signals dormant.

**Definition** net\_if.h:268

[NET\_IF\_SUSPENDED](group__net__if.md#ggae691e5537917ffce27ad0db82c730371aaaeafc62e61ec120609205770c8b54f0)

@ NET\_IF\_SUSPENDED

Power management specific: interface is being suspended.

**Definition** net\_if.h:247

[NET\_IF\_IPV6](group__net__if.md#ggae691e5537917ffce27ad0db82c730371aab31a9e1e8c02159f45efc4e0455a4d6)

@ NET\_IF\_IPV6

Interface supports IPv6.

**Definition** net\_if.h:259

[NET\_IF\_UP](group__net__if.md#ggae691e5537917ffce27ad0db82c730371ab0ab7393d643354c46c3437d74c15840)

@ NET\_IF\_UP

Interface is admin up.

**Definition** net\_if.h:230

[NET\_IF\_LOWER\_UP](group__net__if.md#ggae691e5537917ffce27ad0db82c730371ab1a529826bad6b4bcd04185372f97d6d)

@ NET\_IF\_LOWER\_UP

Driver signals L1 is up.

**Definition** net\_if.h:265

[NET\_IF\_RUNNING](group__net__if.md#ggae691e5537917ffce27ad0db82c730371add3e2ecdcd5de3154f9bd2836428a25a)

@ NET\_IF\_RUNNING

Interface up and running (ready to receive and transmit).

**Definition** net\_if.h:262

[NET\_IF\_NO\_TX\_LOCK](group__net__if.md#ggae691e5537917ffce27ad0db82c730371ae8d564e1577c8daad8ce50a729c500c9)

@ NET\_IF\_NO\_TX\_LOCK

Mutex locking on TX data path disabled on the interface.

**Definition** net\_if.h:277

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

**Definition** device.h:403

[in6\_addr](structin6__addr.md)

IPv6 address struct.

**Definition** net\_ip.h:139

[in\_addr](structin__addr.md)

IPv4 address struct.

**Definition** net\_ip.h:151

[k\_fifo](structk__fifo.md)

**Definition** kernel.h:2391

[k\_mutex](structk__mutex.md)

Mutex Structure.

**Definition** kernel.h:2917

[k\_thread](structk__thread.md)

Thread Structure.

**Definition** thread.h:259

[k\_timepoint\_t](structk__timepoint__t.md)

Kernel timepoint type.

**Definition** sys\_clock.h:219

[net\_dhcpv6\_params](structnet__dhcpv6__params.md)

DHCPv6 client configuration parameters.

**Definition** dhcpv6.h:61

[net\_if\_addr\_ipv4](structnet__if__addr__ipv4.md)

Network Interface unicast IPv4 address and netmask.

**Definition** net\_if.h:437

[net\_if\_addr\_ipv4::ipv4](structnet__if__addr__ipv4.md#a9d8924e263cc7401569c934533a04b48)

struct net\_if\_addr ipv4

IPv4 address.

**Definition** net\_if.h:439

[net\_if\_addr\_ipv4::netmask](structnet__if__addr__ipv4.md#ae1720720e7e36ccf38d0b282d3150774)

struct in\_addr netmask

Netmask.

**Definition** net\_if.h:441

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

**Definition** net\_if.h:128

[net\_if\_addr::is\_temporary](structnet__if__addr.md#a1dd933a37afcb7d708cd602911c38e0a)

uint8\_t is\_temporary

Is this IP address temporary and generated for example by IPv6 privacy extension (RFC 8981).

**Definition** net\_if.h:133

[net\_if\_addr::addr\_state](structnet__if__addr.md#a3106fdcf0dd2479c95efafc586217a2c)

enum net\_addr\_state addr\_state

What is the current state of the address.

**Definition** net\_if.h:69

[net\_if\_addr::is\_infinite](structnet__if__addr.md#a6e799428eb0633a25e4dc3c55e3a3b8c)

uint8\_t is\_infinite

Is the IP address valid forever.

**Definition** net\_if.h:122

[net\_if\_addr::atomic\_ref](structnet__if__addr.md#a9abaf23ec98b22d1741bae410a1f7f3e)

atomic\_t atomic\_ref

Reference counter.

**Definition** net\_if.h:59

[net\_if\_addr::addr\_type](structnet__if__addr.md#ab4fd41001cc24615803bfabb9d48e7eb)

enum net\_addr\_type addr\_type

How the IP address was set.

**Definition** net\_if.h:66

[net\_if\_addr::is\_used](structnet__if__addr.md#aed4d91ba064d24ad0d53c0960cde0352)

uint8\_t is\_used

Is this IP address used or not.

**Definition** net\_if.h:125

[net\_if\_config](structnet__if__config.md)

IP and other configuration related data for network interface.

**Definition** net\_if.h:555

[net\_if\_dev](structnet__if__dev.md)

Network Interface Device structure.

**Definition** net\_if.h:632

[net\_if\_dev::oper\_state](structnet__if__dev.md#a30eabb2ffae082d0de81a50c510738a3)

enum net\_if\_oper\_state oper\_state

RFC 2863 operational status.

**Definition** net\_if.h:668

[net\_if\_dev::l2](structnet__if__dev.md#a85d713c62875f5fe9e3ec29773150797)

const struct net\_l2 \*const l2

Interface's L2 layer.

**Definition** net\_if.h:637

[net\_if\_dev::l2\_data](structnet__if__dev.md#a8fec6a7f612fc1268ef486d8bdebe018)

void \* l2\_data

Interface's private L2 data pointer.

**Definition** net\_if.h:640

[net\_if\_dev::mtu](structnet__if__dev.md#aa15ccca2eb67b8d2afca153ccacb3742)

uint16\_t mtu

The hardware MTU.

**Definition** net\_if.h:658

[net\_if\_dev::dev](structnet__if__dev.md#aab633a44f165f571910dc9fc9e131c50)

const struct device \* dev

The actually device driver instance the net\_if is related to.

**Definition** net\_if.h:634

[net\_if\_dev::link\_addr](structnet__if__dev.md#aac6d5d341ab520e6aac7f7b03737c197)

struct net\_linkaddr link\_addr

The hardware link address.

**Definition** net\_if.h:646

[net\_if\_dev::flags](structnet__if__dev.md#ac8f9c30e1dea05c28c88d3b367b130f5)

atomic\_t flags[ATOMIC\_BITMAP\_SIZE(NET\_IF\_NUM\_FLAGS)]

For internal use.

**Definition** net\_if.h:643

[net\_if\_ip](structnet__if__ip.md)

Network interface IP address configuration.

**Definition** net\_if.h:542

[net\_if\_ipv4](structnet__if__ipv4.md)

IPv4 configuration.

**Definition** net\_if.h:445

[net\_if\_ipv4::mcast\_ttl](structnet__if__ipv4.md#a7e9bf16d51989cfcfe564f4f0a43b480)

uint8\_t mcast\_ttl

IPv4 time-to-live for multicast packets.

**Definition** net\_if.h:459

[net\_if\_ipv4::unicast](structnet__if__ipv4.md#a806cf92123452ed3aa93540803b0a8d3)

struct net\_if\_addr\_ipv4 unicast[NET\_IF\_MAX\_IPV4\_ADDR]

Unicast IP addresses.

**Definition** net\_if.h:447

[net\_if\_ipv4::gw](structnet__if__ipv4.md#aa24772c7202bf465ee3da94a172b7bcb)

struct in\_addr gw

Gateway.

**Definition** net\_if.h:453

[net\_if\_ipv4::ttl](structnet__if__ipv4.md#acdc6d5d6eb5362f4f6d2c027cc40e684)

uint8\_t ttl

IPv4 time-to-live.

**Definition** net\_if.h:456

[net\_if\_ipv4::mcast](structnet__if__ipv4.md#adfaf5b50255bd35297195a7218729ae7)

struct net\_if\_mcast\_addr mcast[NET\_IF\_MAX\_IPV4\_MADDR]

Multicast IP addresses.

**Definition** net\_if.h:450

[net\_if\_ipv6\_prefix](structnet__if__ipv6__prefix.md)

Network Interface IPv6 prefixes.

**Definition** net\_if.h:172

[net\_if\_ipv6\_prefix::iface](structnet__if__ipv6__prefix.md#a0e2d1997e2ccfe1e1af5f16e0c74ed92)

struct net\_if \* iface

Backpointer to network interface where this prefix is used.

**Definition** net\_if.h:180

[net\_if\_ipv6\_prefix::is\_infinite](structnet__if__ipv6__prefix.md#a22090441b27bed06098679bf23b4e1e9)

uint8\_t is\_infinite

Is the IP prefix valid forever.

**Definition** net\_if.h:186

[net\_if\_ipv6\_prefix::len](structnet__if__ipv6__prefix.md#a4d2bc2acbe51256b76cf4d3ced3aac39)

uint8\_t len

Prefix length.

**Definition** net\_if.h:183

[net\_if\_ipv6\_prefix::prefix](structnet__if__ipv6__prefix.md#a65b450d0942b3c96cfc575b462d82028)

struct in6\_addr prefix

IPv6 prefix.

**Definition** net\_if.h:177

[net\_if\_ipv6\_prefix::is\_used](structnet__if__ipv6__prefix.md#a6a4295256957e5eddf149f1ceff62e3f)

uint8\_t is\_used

Is this prefix used or not.

**Definition** net\_if.h:189

[net\_if\_ipv6\_prefix::lifetime](structnet__if__ipv6__prefix.md#a925a97a49d383bd4ce475f5d09fcb7e3)

struct net\_timeout lifetime

Prefix lifetime.

**Definition** net\_if.h:174

[net\_if\_ipv6](structnet__if__ipv6.md)

IPv6 configuration.

**Definition** net\_if.h:313

[net\_if\_ipv6::prefix](structnet__if__ipv6.md#a2dccdc984f08527302d8d910a2658f72)

struct net\_if\_ipv6\_prefix prefix[NET\_IF\_MAX\_IPV6\_PREFIX]

Prefixes.

**Definition** net\_if.h:321

[net\_if\_ipv6::base\_reachable\_time](structnet__if__ipv6.md#a500a78fe23ee2ebc63f3d3b53b5b92ea)

uint32\_t base\_reachable\_time

Default reachable time (RFC 4861, page 52).

**Definition** net\_if.h:324

[net\_if\_ipv6::hop\_limit](structnet__if__ipv6.md#a71775a082984274fbc7c009ead18e751)

uint8\_t hop\_limit

IPv6 hop limit.

**Definition** net\_if.h:352

[net\_if\_ipv6::mcast](structnet__if__ipv6.md#a727d2773e0dee3be687dda5b2dd55682)

struct net\_if\_mcast\_addr mcast[NET\_IF\_MAX\_IPV6\_MADDR]

Multicast IP addresses.

**Definition** net\_if.h:318

[net\_if\_ipv6::retrans\_timer](structnet__if__ipv6.md#ac5ee47ff9d3e429ecbb8623e5d713246)

uint32\_t retrans\_timer

Retransmit timer (RFC 4861, page 52).

**Definition** net\_if.h:330

[net\_if\_ipv6::unicast](structnet__if__ipv6.md#adb6431d336cc3f46972e13d2255452c8)

struct net\_if\_addr unicast[NET\_IF\_MAX\_IPV6\_ADDR]

Unicast IP addresses.

**Definition** net\_if.h:315

[net\_if\_ipv6::mcast\_hop\_limit](structnet__if__ipv6.md#ae94906c28578f2e1ea2506b0e2972d4c)

uint8\_t mcast\_hop\_limit

IPv6 multicast hop limit.

**Definition** net\_if.h:355

[net\_if\_ipv6::reachable\_time](structnet__if__ipv6.md#af57b7dca189167f8cc757c4ed6b08f2f)

uint32\_t reachable\_time

Reachable time (RFC 4861, page 20).

**Definition** net\_if.h:327

[net\_if\_link\_cb](structnet__if__link__cb.md)

Link callback handler struct.

**Definition** net\_if.h:2615

[net\_if\_link\_cb::cb](structnet__if__link__cb.md#a66092a22cba3dd69ac1a91c3522240bb)

net\_if\_link\_callback\_t cb

Link callback.

**Definition** net\_if.h:2620

[net\_if\_link\_cb::node](structnet__if__link__cb.md#accae7945a802c5b7fc36948b12a365ef)

sys\_snode\_t node

Node information for the slist.

**Definition** net\_if.h:2617

[net\_if\_mcast\_addr](structnet__if__mcast__addr.md)

Network Interface multicast IP addresses.

**Definition** net\_if.h:143

[net\_if\_mcast\_addr::address](structnet__if__mcast__addr.md#a3e470fc2eb02ac9e5d3d7d0bea0aaa69)

struct net\_addr address

IP address.

**Definition** net\_if.h:145

[net\_if\_mcast\_addr::is\_joined](structnet__if__mcast__addr.md#a4af9009b2f9ccc0589a9ba6dac10927b)

uint8\_t is\_joined

Did we join to this group.

**Definition** net\_if.h:162

[net\_if\_mcast\_addr::is\_used](structnet__if__mcast__addr.md#abab3e6dba72e24ef522c033d277369ca)

uint8\_t is\_used

Is this multicast IP address used or not.

**Definition** net\_if.h:159

[net\_if\_mcast\_monitor](structnet__if__mcast__monitor.md)

Multicast monitor handler struct.

**Definition** net\_if.h:1577

[net\_if\_mcast\_monitor::node](structnet__if__mcast__monitor.md#a570b7d8a8a5fabca83982a5f7d1d896a)

sys\_snode\_t node

Node information for the slist.

**Definition** net\_if.h:1579

[net\_if\_mcast\_monitor::cb](structnet__if__mcast__monitor.md#aec441b858a5f6792ac9cdbc625f6babe)

net\_if\_mcast\_callback\_t cb

Multicast callback.

**Definition** net\_if.h:1585

[net\_if\_mcast\_monitor::iface](structnet__if__mcast__monitor.md#af4d0e937b2b9161918a13a0d6723c60a)

struct net\_if \* iface

Network interface.

**Definition** net\_if.h:1582

[net\_if\_router](structnet__if__router.md)

Information about routers in the system.

**Definition** net\_if.h:199

[net\_if\_router::iface](structnet__if__router.md#a03789aa0a40f7686b76616de0ca0401a)

struct net\_if \* iface

Network interface the router is connected to.

**Definition** net\_if.h:207

[net\_if\_router::is\_default](structnet__if__router.md#a34745207edcad2745d6ce311e2bf1894)

uint8\_t is\_default

Is default router.

**Definition** net\_if.h:219

[net\_if\_router::lifetime](structnet__if__router.md#a4b0d2ad8f225ab61022c10dfce3db199)

uint16\_t lifetime

Router lifetime.

**Definition** net\_if.h:213

[net\_if\_router::is\_infinite](structnet__if__router.md#a4cb47f30241ae3d410f56f1487254ed0)

uint8\_t is\_infinite

Is the router valid forever.

**Definition** net\_if.h:222

[net\_if\_router::is\_used](structnet__if__router.md#a7196e6d2bc2c958d98dfe29143a62048)

uint8\_t is\_used

Is this router used or not.

**Definition** net\_if.h:216

[net\_if\_router::address](structnet__if__router.md#a86a2ca1b95e348acbde8ce90986b83db)

struct net\_addr address

IP address.

**Definition** net\_if.h:204

[net\_if\_router::node](structnet__if__router.md#aabbac0cd0a59ca0eafdcfc0eaf5d909a)

sys\_snode\_t node

Slist lifetime timer node.

**Definition** net\_if.h:201

[net\_if\_router::life\_start](structnet__if__router.md#adf4f4c722917b3c30f8c73bc2519957f)

uint32\_t life\_start

Router life timer start.

**Definition** net\_if.h:210

[net\_if](structnet__if.md)

Network Interface structure.

**Definition** net\_if.h:678

[net\_if::if\_dev](structnet__if.md#a0982ba2019cdaa7701162e60fdb2171e)

struct net\_if\_dev \* if\_dev

The net\_if\_dev instance the net\_if is related to.

**Definition** net\_if.h:680

[net\_if::config](structnet__if.md#a5e71962f55bdead7bfbbb96518c6c404)

struct net\_if\_config config

Network interface instance configuration.

**Definition** net\_if.h:688

[net\_if::pe\_enabled](structnet__if.md#aa96a6a2d55f6a4ece2f340eef526ef56)

uint8\_t pe\_enabled

Network interface specific flags.

**Definition** net\_if.h:708

[net\_if::lock](structnet__if.md#ace2233b71da53ff0fc7cd564ccfc5a03)

struct k\_mutex lock

Mutex protecting this network interface instance.

**Definition** net\_if.h:699

[net\_if::pe\_prefer\_public](structnet__if.md#aec585e283c9053443ff05b364acf76eb)

uint8\_t pe\_prefer\_public

If PE is enabled, then this tells whether public addresses are preferred over temporary ones for this...

**Definition** net\_if.h:713

[net\_if::tx\_lock](structnet__if.md#af00f729ebddfdcf725169f61b6cd586b)

struct k\_mutex tx\_lock

Mutex used when sending data.

**Definition** net\_if.h:702

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

**Definition** net\_pkt.h:67

[net\_stats](structnet__stats.md)

All network statistics in one struct.

**Definition** net\_stats.h:323

[net\_timeout](structnet__timeout.md)

Generic struct for handling network timeouts.

**Definition** net\_timeout.h:55

[net\_traffic\_class](structnet__traffic__class.md)

Network traffic class.

**Definition** net\_if.h:599

[net\_traffic\_class::stack](structnet__traffic__class.md#a2d98bc68d38bdef649d645b8b52516c5)

k\_thread\_stack\_t \* stack

Stack for this handler.

**Definition** net\_if.h:607

[net\_traffic\_class::handler](structnet__traffic__class.md#a8d0023588fee0a8ff1381bbc80ada143)

struct k\_thread handler

Traffic class handler thread.

**Definition** net\_if.h:604

[net\_traffic\_class::fifo](structnet__traffic__class.md#a94511ca12bad1687f5c7ca862c857ded)

struct k\_fifo fifo

Fifo for handling this Tx or Rx packet.

**Definition** net\_if.h:601

[sockaddr](structsockaddr.md)

Generic sockaddr struct.

**Definition** net\_ip.h:385

[iterable\_sections.h](sys_2iterable__sections_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [net\_if.h](net__if_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
