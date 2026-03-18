---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/net__stats_8h_source.html
original_path: doxygen/html/net__stats_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

net\_stats.h

[Go to the documentation of this file.](net__stats_8h.md)

1

7

8/\*

9 \* Copyright (c) 2016 Intel Corporation

10 \*

11 \* SPDX-License-Identifier: Apache-2.0

12 \*/

13

14#ifndef ZEPHYR\_INCLUDE\_NET\_NET\_STATS\_H\_

15#define ZEPHYR\_INCLUDE\_NET\_NET\_STATS\_H\_

16

17#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

18#include <[zephyr/net/net\_core.h](net__core_8h.md)>

19#include <[zephyr/net/net\_mgmt.h](net__mgmt_8h.md)>

20

21#ifdef \_\_cplusplus

22extern "C" {

23#endif

24

31

[ 36](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752)typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752);

37

[ 41](structnet__stats__bytes.md)struct [net\_stats\_bytes](structnet__stats__bytes.md) {

[ 43](structnet__stats__bytes.md#a89368f376c02d25c5a7a5719851a0ac7) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [sent](structnet__stats__bytes.md#a89368f376c02d25c5a7a5719851a0ac7);

[ 45](structnet__stats__bytes.md#a8bc21878924210278c6e0e2861163be4) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [received](structnet__stats__bytes.md#a8bc21878924210278c6e0e2861163be4);

46};

47

[ 51](structnet__stats__pkts.md)struct [net\_stats\_pkts](structnet__stats__pkts.md) {

[ 53](structnet__stats__pkts.md#aee1e302d0f8dac79b693a06d8fa3b3c5) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [tx](structnet__stats__pkts.md#aee1e302d0f8dac79b693a06d8fa3b3c5);

[ 55](structnet__stats__pkts.md#ac9784b5a245e6c57e39318aaf314f0cf) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [rx](structnet__stats__pkts.md#ac9784b5a245e6c57e39318aaf314f0cf);

56};

57

[ 61](structnet__stats__ip.md)struct [net\_stats\_ip](structnet__stats__ip.md) {

[ 63](structnet__stats__ip.md#ab6a6373368dd24cb51504c5729d535d3) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [recv](structnet__stats__ip.md#ab6a6373368dd24cb51504c5729d535d3);

64

[ 66](structnet__stats__ip.md#abbe676bbe9faa89b2b6b8c4950b1c9d5) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [sent](structnet__stats__ip.md#abbe676bbe9faa89b2b6b8c4950b1c9d5);

67

[ 69](structnet__stats__ip.md#a4bb82a5ebebaa3e8a11973c07eed96a0) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [forwarded](structnet__stats__ip.md#a4bb82a5ebebaa3e8a11973c07eed96a0);

70

[ 72](structnet__stats__ip.md#ac86399b70d7f761162e5336dd15589eb) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [drop](structnet__stats__ip.md#ac86399b70d7f761162e5336dd15589eb);

73};

74

[ 78](structnet__stats__ip__errors.md)struct [net\_stats\_ip\_errors](structnet__stats__ip__errors.md) {

[ 82](structnet__stats__ip__errors.md#a3e476f659ebeaa5c5f7b6dad2d90326f) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [vhlerr](structnet__stats__ip__errors.md#a3e476f659ebeaa5c5f7b6dad2d90326f);

83

[ 85](structnet__stats__ip__errors.md#a06b35742c418ebc6414fcb5c7002edde) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [hblenerr](structnet__stats__ip__errors.md#a06b35742c418ebc6414fcb5c7002edde);

86

[ 88](structnet__stats__ip__errors.md#a9b4bf05e9df13e1d99518125b9067bef) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [lblenerr](structnet__stats__ip__errors.md#a9b4bf05e9df13e1d99518125b9067bef);

89

[ 91](structnet__stats__ip__errors.md#ab84ee9dfbe5da391d60c6e3ae9abea16) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [fragerr](structnet__stats__ip__errors.md#ab84ee9dfbe5da391d60c6e3ae9abea16);

92

[ 94](structnet__stats__ip__errors.md#a872cc0beca45bbe87ae794dd8ca4e301) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [chkerr](structnet__stats__ip__errors.md#a872cc0beca45bbe87ae794dd8ca4e301);

95

[ 99](structnet__stats__ip__errors.md#a978b1c23847e707ac1fa27c2b34fa85d) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [protoerr](structnet__stats__ip__errors.md#a978b1c23847e707ac1fa27c2b34fa85d);

100};

101

[ 105](structnet__stats__icmp.md)struct [net\_stats\_icmp](structnet__stats__icmp.md) {

[ 107](structnet__stats__icmp.md#ae6f226b55565c11fca0c9e099f08c267) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [recv](structnet__stats__icmp.md#ae6f226b55565c11fca0c9e099f08c267);

108

[ 110](structnet__stats__icmp.md#a2d6eb7dfc8f4b439b399b039022f2889) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [sent](structnet__stats__icmp.md#a2d6eb7dfc8f4b439b399b039022f2889);

111

[ 113](structnet__stats__icmp.md#a755f3388c05d4bd2988ddd16d1a4cf32) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [drop](structnet__stats__icmp.md#a755f3388c05d4bd2988ddd16d1a4cf32);

114

[ 116](structnet__stats__icmp.md#ae1a29dd9b8e1ce9a737fa7f36c805cd4) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [typeerr](structnet__stats__icmp.md#ae1a29dd9b8e1ce9a737fa7f36c805cd4);

117

[ 119](structnet__stats__icmp.md#a6662bc547107a08c52e902a2446629bf) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [chkerr](structnet__stats__icmp.md#a6662bc547107a08c52e902a2446629bf);

120};

121

[ 125](structnet__stats__tcp.md)struct [net\_stats\_tcp](structnet__stats__tcp.md) {

[ 127](structnet__stats__tcp.md#af80c18bcc253133ce5f0597ac190b349) struct [net\_stats\_bytes](structnet__stats__bytes.md) [bytes](structnet__stats__tcp.md#af80c18bcc253133ce5f0597ac190b349);

128

[ 130](structnet__stats__tcp.md#abe567032cb4a267a984aec28c1e3cca4) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [resent](structnet__stats__tcp.md#abe567032cb4a267a984aec28c1e3cca4);

131

[ 133](structnet__stats__tcp.md#aa549f7b6d5828009a09190fd64afa8e3) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [drop](structnet__stats__tcp.md#aa549f7b6d5828009a09190fd64afa8e3);

134

[ 136](structnet__stats__tcp.md#ad25edb2b39a6acc8152c35ad43a5042f) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [recv](structnet__stats__tcp.md#ad25edb2b39a6acc8152c35ad43a5042f);

137

[ 139](structnet__stats__tcp.md#aa987bebf96000b6b4e92bfafc218759a) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [sent](structnet__stats__tcp.md#aa987bebf96000b6b4e92bfafc218759a);

140

[ 142](structnet__stats__tcp.md#a5f045704859331918511e9c2281ac155) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [seg\_drop](structnet__stats__tcp.md#a5f045704859331918511e9c2281ac155);

143

[ 145](structnet__stats__tcp.md#a5099e174b0eafa322f0630f1f5c73a8b) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [chkerr](structnet__stats__tcp.md#a5099e174b0eafa322f0630f1f5c73a8b);

146

[ 148](structnet__stats__tcp.md#a0d40abc85776f0a9b9510a909b7f6d18) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [ackerr](structnet__stats__tcp.md#a0d40abc85776f0a9b9510a909b7f6d18);

149

[ 151](structnet__stats__tcp.md#a471fcd5578f79ce77d20547b28503ac1) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [rsterr](structnet__stats__tcp.md#a471fcd5578f79ce77d20547b28503ac1);

152

[ 154](structnet__stats__tcp.md#aa618cf86b962aca0f14eb9178c8ae61a) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [rst](structnet__stats__tcp.md#aa618cf86b962aca0f14eb9178c8ae61a);

155

[ 157](structnet__stats__tcp.md#a4a4ea6e5d87ef58b4271bd708cf39635) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [rexmit](structnet__stats__tcp.md#a4a4ea6e5d87ef58b4271bd708cf39635);

158

[ 162](structnet__stats__tcp.md#ac557ac0d8917bc2c2dfed74126f993c8) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [conndrop](structnet__stats__tcp.md#ac557ac0d8917bc2c2dfed74126f993c8);

163

[ 165](structnet__stats__tcp.md#a67f55954a4c51f2b957c7d974e78c1c0) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [connrst](structnet__stats__tcp.md#a67f55954a4c51f2b957c7d974e78c1c0);

166};

167

[ 171](structnet__stats__udp.md)struct [net\_stats\_udp](structnet__stats__udp.md) {

[ 173](structnet__stats__udp.md#a2d884bf9106e60d430ffec7c7964a609) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [drop](structnet__stats__udp.md#a2d884bf9106e60d430ffec7c7964a609);

174

[ 176](structnet__stats__udp.md#a0ea91d85fe322661fb909f5e94e55a34) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [recv](structnet__stats__udp.md#a0ea91d85fe322661fb909f5e94e55a34);

177

[ 179](structnet__stats__udp.md#ab4e8228c221901d3ded55f3f823bfa1c) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [sent](structnet__stats__udp.md#ab4e8228c221901d3ded55f3f823bfa1c);

180

[ 182](structnet__stats__udp.md#a4c57d5f68ebda7981400729b9c7fe0f7) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [chkerr](structnet__stats__udp.md#a4c57d5f68ebda7981400729b9c7fe0f7);

183};

184

[ 188](structnet__stats__ipv6__nd.md)struct [net\_stats\_ipv6\_nd](structnet__stats__ipv6__nd.md) {

[ 189](structnet__stats__ipv6__nd.md#a31074d5d44138fcabdc5f7750f9f2c47) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [drop](structnet__stats__ipv6__nd.md#a31074d5d44138fcabdc5f7750f9f2c47);

[ 190](structnet__stats__ipv6__nd.md#a0bf6f67d9112996a3b002ea160aec769) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [recv](structnet__stats__ipv6__nd.md#a0bf6f67d9112996a3b002ea160aec769);

[ 191](structnet__stats__ipv6__nd.md#a0129f7892a4439c20deb2f32b9001277) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [sent](structnet__stats__ipv6__nd.md#a0129f7892a4439c20deb2f32b9001277);

192};

193

[ 197](structnet__stats__ipv6__mld.md)struct [net\_stats\_ipv6\_mld](structnet__stats__ipv6__mld.md) {

[ 199](structnet__stats__ipv6__mld.md#a4879ff9e31f8b60973d3b169598e921d) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [recv](structnet__stats__ipv6__mld.md#a4879ff9e31f8b60973d3b169598e921d);

200

[ 202](structnet__stats__ipv6__mld.md#ab397b74b14ce7047bf2fc63ca72ce1e5) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [sent](structnet__stats__ipv6__mld.md#ab397b74b14ce7047bf2fc63ca72ce1e5);

203

[ 205](structnet__stats__ipv6__mld.md#ad85dc87f57296a1e7d64e959b0370ee8) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [drop](structnet__stats__ipv6__mld.md#ad85dc87f57296a1e7d64e959b0370ee8);

206};

207

[ 211](structnet__stats__ipv4__igmp.md)struct [net\_stats\_ipv4\_igmp](structnet__stats__ipv4__igmp.md) {

[ 213](structnet__stats__ipv4__igmp.md#a469113de7af0ba42dbd1b0365d00602c) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [recv](structnet__stats__ipv4__igmp.md#a469113de7af0ba42dbd1b0365d00602c);

214

[ 216](structnet__stats__ipv4__igmp.md#a955e20a6ee5e19e08000b3114b9d71a6) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [sent](structnet__stats__ipv4__igmp.md#a955e20a6ee5e19e08000b3114b9d71a6);

217

[ 219](structnet__stats__ipv4__igmp.md#a1c37702ff837b8c5cc9df5f690e7678c) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [drop](structnet__stats__ipv4__igmp.md#a1c37702ff837b8c5cc9df5f690e7678c);

220};

221

[ 225](structnet__stats__tx__time.md)struct [net\_stats\_tx\_time](structnet__stats__tx__time.md) {

[ 226](structnet__stats__tx__time.md#af6f7a26c0344a0f93306e105a8917c3e) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [sum](structnet__stats__tx__time.md#af6f7a26c0344a0f93306e105a8917c3e);

[ 227](structnet__stats__tx__time.md#a7a652350ed04e53ba02aec294f8444b4) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [count](structnet__stats__tx__time.md#a7a652350ed04e53ba02aec294f8444b4);

228};

229

[ 233](structnet__stats__rx__time.md)struct [net\_stats\_rx\_time](structnet__stats__rx__time.md) {

[ 234](structnet__stats__rx__time.md#a4b84c2ae2fda8fcd75fdf1bf0b2aae8d) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [sum](structnet__stats__rx__time.md#a4b84c2ae2fda8fcd75fdf1bf0b2aae8d);

[ 235](structnet__stats__rx__time.md#a68247051b064de081fa2e84118192958) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [count](structnet__stats__rx__time.md#a68247051b064de081fa2e84118192958);

236};

237

238#if NET\_TC\_TX\_COUNT == 0

[ 239](group__net__stats.md#ga83c834f2e8a8859051294e550d0b896c)#define NET\_TC\_TX\_STATS\_COUNT 1

240#else

241#define NET\_TC\_TX\_STATS\_COUNT NET\_TC\_TX\_COUNT

242#endif

243

244#if NET\_TC\_RX\_COUNT == 0

[ 245](group__net__stats.md#ga10d8c8b3c671e0a625329a9a596e1265)#define NET\_TC\_RX\_STATS\_COUNT 1

246#else

247#define NET\_TC\_RX\_STATS\_COUNT NET\_TC\_RX\_COUNT

248#endif

249

[ 253](structnet__stats__tc.md)struct [net\_stats\_tc](structnet__stats__tc.md) {

254 struct {

[ 255](structnet__stats__tc.md#a30288ef3bb0796cd18c3cf0aedbe875a) struct [net\_stats\_tx\_time](structnet__stats__tx__time.md) [tx\_time](structnet__stats__tc.md#a30288ef3bb0796cd18c3cf0aedbe875a);

256#if defined(CONFIG\_NET\_PKT\_TXTIME\_STATS\_DETAIL)

257 struct [net\_stats\_tx\_time](structnet__stats__tx__time.md)

258 tx\_time\_detail[NET\_PKT\_DETAIL\_STATS\_COUNT];

259#endif

[ 260](structnet__stats__tc.md#a6614b5f5186635415a7d787260c39248) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [pkts](structnet__stats__tc.md#a6614b5f5186635415a7d787260c39248);

[ 261](structnet__stats__tc.md#a192a7ec0d24bce9e62f766e481ee5709) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [bytes](structnet__stats__tc.md#a192a7ec0d24bce9e62f766e481ee5709);

[ 262](structnet__stats__tc.md#a8a5c2e59990407ddbfc7973a1c183bf6) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [priority](structnet__stats__tc.md#a8a5c2e59990407ddbfc7973a1c183bf6);

[ 263](structnet__stats__tc.md#a303e66b023d64b46b621e3384be8b822) } [sent](structnet__stats__tc.md#a303e66b023d64b46b621e3384be8b822)[[NET\_TC\_TX\_STATS\_COUNT](group__net__stats.md#ga83c834f2e8a8859051294e550d0b896c)];

264

265 struct {

[ 266](structnet__stats__tc.md#a8ea00824bb0fb18e4d8912343e01c3b7) struct [net\_stats\_rx\_time](structnet__stats__rx__time.md) [rx\_time](structnet__stats__tc.md#a8ea00824bb0fb18e4d8912343e01c3b7);

267#if defined(CONFIG\_NET\_PKT\_RXTIME\_STATS\_DETAIL)

268 struct [net\_stats\_rx\_time](structnet__stats__rx__time.md)

269 rx\_time\_detail[NET\_PKT\_DETAIL\_STATS\_COUNT];

270#endif

271 [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [pkts](structnet__stats__tc.md#a6614b5f5186635415a7d787260c39248);

272 [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [bytes](structnet__stats__tc.md#a192a7ec0d24bce9e62f766e481ee5709);

273 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [priority](structnet__stats__tc.md#a8a5c2e59990407ddbfc7973a1c183bf6);

[ 274](structnet__stats__tc.md#a7afde5c8f85e6bef304493d9c2fa6fdb) } [recv](group__bsd__sockets.md#gae11da452beee536eac85d5f26e5cdd40)[[NET\_TC\_RX\_STATS\_COUNT](group__net__stats.md#ga10d8c8b3c671e0a625329a9a596e1265)];

275};

276

277

[ 281](structnet__stats__pm.md)struct [net\_stats\_pm](structnet__stats__pm.md) {

[ 282](structnet__stats__pm.md#ab43935fcfe9efc1cd5f3e7e329996805) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [overall\_suspend\_time](structnet__stats__pm.md#ab43935fcfe9efc1cd5f3e7e329996805);

[ 283](structnet__stats__pm.md#ac14122a4765c499c045f18c70af355a0) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [suspend\_count](structnet__stats__pm.md#ac14122a4765c499c045f18c70af355a0);

[ 284](structnet__stats__pm.md#a0bdf9c3676298e2df4ff3bfa03f5e823) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [last\_suspend\_time](structnet__stats__pm.md#a0bdf9c3676298e2df4ff3bfa03f5e823);

[ 285](structnet__stats__pm.md#a6784806eaa093431ed3c0f7acfe5a89c) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [start\_time](structnet__stats__pm.md#a6784806eaa093431ed3c0f7acfe5a89c);

286};

287

288

[ 292](structnet__stats.md)struct [net\_stats](structnet__stats.md) {

[ 294](structnet__stats.md#a3a4c90661d6b310b628262228a341fe2) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [processing\_error](structnet__stats.md#a3a4c90661d6b310b628262228a341fe2);

295

[ 300](structnet__stats.md#a7a28233e6d23efdce0143469b9bb6c05) struct [net\_stats\_bytes](structnet__stats__bytes.md) [bytes](structnet__stats.md#a7a28233e6d23efdce0143469b9bb6c05);

301

[ 303](structnet__stats.md#ac42cb13954d164e92a1ef60919a2a34e) struct [net\_stats\_ip\_errors](structnet__stats__ip__errors.md) [ip\_errors](structnet__stats.md#ac42cb13954d164e92a1ef60919a2a34e);

304

305#if defined(CONFIG\_NET\_STATISTICS\_IPV6)

307 struct [net\_stats\_ip](structnet__stats__ip.md) ipv6;

308#endif

309

310#if defined(CONFIG\_NET\_STATISTICS\_IPV4)

312 struct [net\_stats\_ip](structnet__stats__ip.md) ipv4;

313#endif

314

315#if defined(CONFIG\_NET\_STATISTICS\_ICMP)

317 struct [net\_stats\_icmp](structnet__stats__icmp.md) icmp;

318#endif

319

320#if defined(CONFIG\_NET\_STATISTICS\_TCP)

322 struct [net\_stats\_tcp](structnet__stats__tcp.md) tcp;

323#endif

324

325#if defined(CONFIG\_NET\_STATISTICS\_UDP)

327 struct [net\_stats\_udp](structnet__stats__udp.md) udp;

328#endif

329

330#if defined(CONFIG\_NET\_STATISTICS\_IPV6\_ND)

332 struct [net\_stats\_ipv6\_nd](structnet__stats__ipv6__nd.md) ipv6\_nd;

333#endif

334

335#if defined(CONFIG\_NET\_STATISTICS\_MLD)

337 struct [net\_stats\_ipv6\_mld](structnet__stats__ipv6__mld.md) ipv6\_mld;

338#endif

339

340#if defined(CONFIG\_NET\_STATISTICS\_IGMP)

342 struct [net\_stats\_ipv4\_igmp](structnet__stats__ipv4__igmp.md) ipv4\_igmp;

343#endif

344

345#if NET\_TC\_COUNT > 1

347 struct [net\_stats\_tc](structnet__stats__tc.md) tc;

348#endif

349

350#if defined(CONFIG\_NET\_PKT\_TXTIME\_STATS)

352 struct [net\_stats\_tx\_time](structnet__stats__tx__time.md) tx\_time;

353#endif

354

355#if defined(CONFIG\_NET\_PKT\_RXTIME\_STATS)

357 struct [net\_stats\_rx\_time](structnet__stats__rx__time.md) rx\_time;

358#endif

359

360#if defined(CONFIG\_NET\_PKT\_TXTIME\_STATS\_DETAIL)

362 struct [net\_stats\_tx\_time](structnet__stats__tx__time.md) tx\_time\_detail[NET\_PKT\_DETAIL\_STATS\_COUNT];

363#endif

364#if defined(CONFIG\_NET\_PKT\_RXTIME\_STATS\_DETAIL)

366 struct [net\_stats\_rx\_time](structnet__stats__rx__time.md) rx\_time\_detail[NET\_PKT\_DETAIL\_STATS\_COUNT];

367#endif

368

369#if defined(CONFIG\_NET\_STATISTICS\_POWER\_MANAGEMENT)

370 struct [net\_stats\_pm](structnet__stats__pm.md) pm;

371#endif

372};

373

[ 377](structnet__stats__eth__errors.md)struct [net\_stats\_eth\_errors](structnet__stats__eth__errors.md) {

[ 378](structnet__stats__eth__errors.md#aca0e2e4807fa70279dee8ddaad2d7ef7) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [rx\_length\_errors](structnet__stats__eth__errors.md#aca0e2e4807fa70279dee8ddaad2d7ef7);

[ 379](structnet__stats__eth__errors.md#a9afee89f5bb01907e7cd515e2a0ff1b5) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [rx\_over\_errors](structnet__stats__eth__errors.md#a9afee89f5bb01907e7cd515e2a0ff1b5);

[ 380](structnet__stats__eth__errors.md#a4dab70cf219269bb393ce14faf0ed77e) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [rx\_crc\_errors](structnet__stats__eth__errors.md#a4dab70cf219269bb393ce14faf0ed77e);

[ 381](structnet__stats__eth__errors.md#a8dfcc5cd1b4decec5783d01ba7033b05) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [rx\_frame\_errors](structnet__stats__eth__errors.md#a8dfcc5cd1b4decec5783d01ba7033b05);

[ 382](structnet__stats__eth__errors.md#a82622736d226b4d3b999f1f22ccf8529) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [rx\_no\_buffer\_count](structnet__stats__eth__errors.md#a82622736d226b4d3b999f1f22ccf8529);

[ 383](structnet__stats__eth__errors.md#a2d2b2c4e3764ebec841f1ecbe7058d99) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [rx\_missed\_errors](structnet__stats__eth__errors.md#a2d2b2c4e3764ebec841f1ecbe7058d99);

[ 384](structnet__stats__eth__errors.md#a0e83e270a35222ed3e927800be4159e7) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [rx\_long\_length\_errors](structnet__stats__eth__errors.md#a0e83e270a35222ed3e927800be4159e7);

[ 385](structnet__stats__eth__errors.md#a5e3d39d8417bb180cbfcb8c901006e81) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [rx\_short\_length\_errors](structnet__stats__eth__errors.md#a5e3d39d8417bb180cbfcb8c901006e81);

[ 386](structnet__stats__eth__errors.md#a7618f10af3443c49a6e256bb41e77781) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [rx\_align\_errors](structnet__stats__eth__errors.md#a7618f10af3443c49a6e256bb41e77781);

[ 387](structnet__stats__eth__errors.md#a7bcfbb13836f162ceeb5f021304b5c76) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [rx\_dma\_failed](structnet__stats__eth__errors.md#a7bcfbb13836f162ceeb5f021304b5c76);

[ 388](structnet__stats__eth__errors.md#adbcae9c10c081f1cdf304bcdce740aa4) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [rx\_buf\_alloc\_failed](structnet__stats__eth__errors.md#adbcae9c10c081f1cdf304bcdce740aa4);

389

[ 390](structnet__stats__eth__errors.md#afec6a7e24c6f3cc74dd9f739f27b3e48) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [tx\_aborted\_errors](structnet__stats__eth__errors.md#afec6a7e24c6f3cc74dd9f739f27b3e48);

[ 391](structnet__stats__eth__errors.md#a0043d1a1481040a6d7439bd23423ec12) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [tx\_carrier\_errors](structnet__stats__eth__errors.md#a0043d1a1481040a6d7439bd23423ec12);

[ 392](structnet__stats__eth__errors.md#a84630da9b82557f56dc35cd59ca2f7ae) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [tx\_fifo\_errors](structnet__stats__eth__errors.md#a84630da9b82557f56dc35cd59ca2f7ae);

[ 393](structnet__stats__eth__errors.md#ae2a13733c1a5f0cc3e00efca0c3f429d) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [tx\_heartbeat\_errors](structnet__stats__eth__errors.md#ae2a13733c1a5f0cc3e00efca0c3f429d);

[ 394](structnet__stats__eth__errors.md#a17624a12d6473bdd78698076fed0d122) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [tx\_window\_errors](structnet__stats__eth__errors.md#a17624a12d6473bdd78698076fed0d122);

[ 395](structnet__stats__eth__errors.md#abfbf6478b7afdd5935d7c6948c9ef426) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [tx\_dma\_failed](structnet__stats__eth__errors.md#abfbf6478b7afdd5935d7c6948c9ef426);

396

[ 397](structnet__stats__eth__errors.md#a07d0a435f2129556520c732571d28edf) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [uncorr\_ecc\_errors](structnet__stats__eth__errors.md#a07d0a435f2129556520c732571d28edf);

[ 398](structnet__stats__eth__errors.md#a257113639f0e0e3085febb7a147f498f) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [corr\_ecc\_errors](structnet__stats__eth__errors.md#a257113639f0e0e3085febb7a147f498f);

399};

400

[ 404](structnet__stats__eth__flow.md)struct [net\_stats\_eth\_flow](structnet__stats__eth__flow.md) {

[ 405](structnet__stats__eth__flow.md#a08e5da4ff78fe3893b9c9a628cefe4f2) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [rx\_flow\_control\_xon](structnet__stats__eth__flow.md#a08e5da4ff78fe3893b9c9a628cefe4f2);

[ 406](structnet__stats__eth__flow.md#a8f9b93537b3c11be70f276aaa72cb637) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [rx\_flow\_control\_xoff](structnet__stats__eth__flow.md#a8f9b93537b3c11be70f276aaa72cb637);

[ 407](structnet__stats__eth__flow.md#a31412e8bf9d38ba630ea856e958a48d7) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [tx\_flow\_control\_xon](structnet__stats__eth__flow.md#a31412e8bf9d38ba630ea856e958a48d7);

[ 408](structnet__stats__eth__flow.md#a969d81f9db20312d2d2aa7f70f93bdd5) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [tx\_flow\_control\_xoff](structnet__stats__eth__flow.md#a969d81f9db20312d2d2aa7f70f93bdd5);

409};

410

[ 414](structnet__stats__eth__csum.md)struct [net\_stats\_eth\_csum](structnet__stats__eth__csum.md) {

[ 415](structnet__stats__eth__csum.md#a1f1ba5c01c6232cd739d069ddb871b17) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [rx\_csum\_offload\_good](structnet__stats__eth__csum.md#a1f1ba5c01c6232cd739d069ddb871b17);

[ 416](structnet__stats__eth__csum.md#ac4fc04d66193070d4f52a4c07f29ccce) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [rx\_csum\_offload\_errors](structnet__stats__eth__csum.md#ac4fc04d66193070d4f52a4c07f29ccce);

417};

418

[ 422](structnet__stats__eth__hw__timestamp.md)struct [net\_stats\_eth\_hw\_timestamp](structnet__stats__eth__hw__timestamp.md) {

[ 423](structnet__stats__eth__hw__timestamp.md#acd3d5f72d7df568110d96093e0c9534d) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [rx\_hwtstamp\_cleared](structnet__stats__eth__hw__timestamp.md#acd3d5f72d7df568110d96093e0c9534d);

[ 424](structnet__stats__eth__hw__timestamp.md#a41f605499dbf88a879522fdfa4633d9e) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [tx\_hwtstamp\_timeouts](structnet__stats__eth__hw__timestamp.md#a41f605499dbf88a879522fdfa4633d9e);

[ 425](structnet__stats__eth__hw__timestamp.md#ae1f983faf4a999308c464e4af5a5284b) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [tx\_hwtstamp\_skipped](structnet__stats__eth__hw__timestamp.md#ae1f983faf4a999308c464e4af5a5284b);

426};

427

428#ifdef CONFIG\_NET\_STATISTICS\_ETHERNET\_VENDOR

432struct net\_stats\_eth\_vendor {

433 const char \* const key;

434 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) value;

435};

436#endif

437

[ 441](structnet__stats__eth.md)struct [net\_stats\_eth](structnet__stats__eth.md) {

[ 442](structnet__stats__eth.md#a8c5cf1ead8ba214425a16fed1c2ad0fb) struct [net\_stats\_bytes](structnet__stats__bytes.md) [bytes](structnet__stats__eth.md#a8c5cf1ead8ba214425a16fed1c2ad0fb);

[ 443](structnet__stats__eth.md#a97bd6026b16890743f344751a21107f1) struct [net\_stats\_pkts](structnet__stats__pkts.md) [pkts](structnet__stats__eth.md#a97bd6026b16890743f344751a21107f1);

[ 444](structnet__stats__eth.md#a054beb909134b0e0f22f5df599549128) struct [net\_stats\_pkts](structnet__stats__pkts.md) [broadcast](structnet__stats__eth.md#a054beb909134b0e0f22f5df599549128);

[ 445](structnet__stats__eth.md#a4f6a2903330518a132e7e547820e0bf2) struct [net\_stats\_pkts](structnet__stats__pkts.md) [multicast](structnet__stats__eth.md#a4f6a2903330518a132e7e547820e0bf2);

[ 446](structnet__stats__eth.md#a9c869740f416fbe0b54d7fefacb1fe29) struct [net\_stats\_pkts](structnet__stats__pkts.md) [errors](structnet__stats__eth.md#a9c869740f416fbe0b54d7fefacb1fe29);

[ 447](structnet__stats__eth.md#a922feddb17fc020371f1bcc52c709415) struct [net\_stats\_eth\_errors](structnet__stats__eth__errors.md) [error\_details](structnet__stats__eth.md#a922feddb17fc020371f1bcc52c709415);

[ 448](structnet__stats__eth.md#a643010ac6360c8c0c08016725ba12222) struct [net\_stats\_eth\_flow](structnet__stats__eth__flow.md) [flow\_control](structnet__stats__eth.md#a643010ac6360c8c0c08016725ba12222);

[ 449](structnet__stats__eth.md#a2169ae06bace1a93663bccf88c8d7a29) struct [net\_stats\_eth\_csum](structnet__stats__eth__csum.md) [csum](structnet__stats__eth.md#a2169ae06bace1a93663bccf88c8d7a29);

[ 450](structnet__stats__eth.md#a44667efff73c17c089ed22d5b0da5ad3) struct [net\_stats\_eth\_hw\_timestamp](structnet__stats__eth__hw__timestamp.md) [hw\_timestamp](structnet__stats__eth.md#a44667efff73c17c089ed22d5b0da5ad3);

[ 451](structnet__stats__eth.md#a822d4205791f59999c842610522f6fc5) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [collisions](structnet__stats__eth.md#a822d4205791f59999c842610522f6fc5);

[ 452](structnet__stats__eth.md#a257c349cf3d32d38796e3899e702454a) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [tx\_dropped](structnet__stats__eth.md#a257c349cf3d32d38796e3899e702454a);

[ 453](structnet__stats__eth.md#ab351258ae82abd09759d37774559d8bc) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [tx\_timeout\_count](structnet__stats__eth.md#ab351258ae82abd09759d37774559d8bc);

[ 454](structnet__stats__eth.md#a6699012226e25e8bad39076fed6dbfb5) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [tx\_restart\_queue](structnet__stats__eth.md#a6699012226e25e8bad39076fed6dbfb5);

[ 455](structnet__stats__eth.md#afaacee7cc1d0a35ae2344175421c40dd) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [unknown\_protocol](structnet__stats__eth.md#afaacee7cc1d0a35ae2344175421c40dd);

456#ifdef CONFIG\_NET\_STATISTICS\_ETHERNET\_VENDOR

458 struct net\_stats\_eth\_vendor \*vendor;

459#endif

460};

461

[ 465](structnet__stats__ppp.md)struct [net\_stats\_ppp](structnet__stats__ppp.md) {

[ 466](structnet__stats__ppp.md#ab2b48da7f19d4b83e3f41b41979b7ed8) struct [net\_stats\_bytes](structnet__stats__bytes.md) [bytes](structnet__stats__ppp.md#ab2b48da7f19d4b83e3f41b41979b7ed8);

[ 467](structnet__stats__ppp.md#a71fc81f3c5f3e65a476b3391f086d340) struct [net\_stats\_pkts](structnet__stats__pkts.md) [pkts](structnet__stats__ppp.md#a71fc81f3c5f3e65a476b3391f086d340);

468

[ 470](structnet__stats__ppp.md#ae2e0a47a539e9d7bc97f9c63f889b276) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [drop](structnet__stats__ppp.md#ae2e0a47a539e9d7bc97f9c63f889b276);

471

[ 473](structnet__stats__ppp.md#a1332b31980f82236aeb0c3f9444e2ac6) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [chkerr](structnet__stats__ppp.md#a1332b31980f82236aeb0c3f9444e2ac6);

474};

475

[ 479](structnet__stats__sta__mgmt.md)struct [net\_stats\_sta\_mgmt](structnet__stats__sta__mgmt.md) {

[ 481](structnet__stats__sta__mgmt.md#ac6e68fded8e19b20259442436923f815) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [beacons\_rx](structnet__stats__sta__mgmt.md#ac6e68fded8e19b20259442436923f815);

482

[ 484](structnet__stats__sta__mgmt.md#a29ae0079b4c780e0de2656a85ec15fe9) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [beacons\_miss](structnet__stats__sta__mgmt.md#a29ae0079b4c780e0de2656a85ec15fe9);

485};

486

[ 490](structnet__stats__wifi.md)struct [net\_stats\_wifi](structnet__stats__wifi.md) {

[ 491](structnet__stats__wifi.md#a8bee22961545674e6ab100b58a04bf91) struct [net\_stats\_sta\_mgmt](structnet__stats__sta__mgmt.md) [sta\_mgmt](structnet__stats__wifi.md#a8bee22961545674e6ab100b58a04bf91);

[ 492](structnet__stats__wifi.md#aa055b1e8bd8f1e50815c1028b562be07) struct [net\_stats\_bytes](structnet__stats__bytes.md) [bytes](structnet__stats__wifi.md#aa055b1e8bd8f1e50815c1028b562be07);

[ 493](structnet__stats__wifi.md#adbcdb2dd8733f2917c00a0b2d365393b) struct [net\_stats\_pkts](structnet__stats__pkts.md) [pkts](structnet__stats__wifi.md#adbcdb2dd8733f2917c00a0b2d365393b);

[ 494](structnet__stats__wifi.md#a03dc04638c4b670bd7f3520d45fc1eda) struct [net\_stats\_pkts](structnet__stats__pkts.md) [broadcast](structnet__stats__wifi.md#a03dc04638c4b670bd7f3520d45fc1eda);

[ 495](structnet__stats__wifi.md#a7e7f68215101885fd51c70e981da26e7) struct [net\_stats\_pkts](structnet__stats__pkts.md) [multicast](structnet__stats__wifi.md#a7e7f68215101885fd51c70e981da26e7);

[ 496](structnet__stats__wifi.md#ae0149e64a94a9f96eb6680f94793c8c4) struct [net\_stats\_pkts](structnet__stats__pkts.md) [errors](structnet__stats__wifi.md#ae0149e64a94a9f96eb6680f94793c8c4);

497};

498

499#if defined(CONFIG\_NET\_STATISTICS\_USER\_API)

500/\* Management part definitions \*/

501

502#define \_NET\_STATS\_LAYER NET\_MGMT\_LAYER\_L3

503#define \_NET\_STATS\_CODE 0x101

504#define \_NET\_STATS\_BASE (NET\_MGMT\_LAYER(\_NET\_STATS\_LAYER) | \

505 NET\_MGMT\_LAYER\_CODE(\_NET\_STATS\_CODE))

506

507enum net\_request\_stats\_cmd {

508 NET\_REQUEST\_STATS\_CMD\_GET\_ALL = 1,

509 NET\_REQUEST\_STATS\_CMD\_GET\_PROCESSING\_ERROR,

510 NET\_REQUEST\_STATS\_CMD\_GET\_BYTES,

511 NET\_REQUEST\_STATS\_CMD\_GET\_IP\_ERRORS,

512 NET\_REQUEST\_STATS\_CMD\_GET\_IPV4,

513 NET\_REQUEST\_STATS\_CMD\_GET\_IPV6,

514 NET\_REQUEST\_STATS\_CMD\_GET\_IPV6\_ND,

515 NET\_REQUEST\_STATS\_CMD\_GET\_ICMP,

516 NET\_REQUEST\_STATS\_CMD\_GET\_UDP,

517 NET\_REQUEST\_STATS\_CMD\_GET\_TCP,

518 NET\_REQUEST\_STATS\_CMD\_GET\_ETHERNET,

519 NET\_REQUEST\_STATS\_CMD\_GET\_PPP,

520 NET\_REQUEST\_STATS\_CMD\_GET\_PM,

521 NET\_REQUEST\_STATS\_CMD\_GET\_WIFI,

522};

523

524#define NET\_REQUEST\_STATS\_GET\_ALL \

525 (\_NET\_STATS\_BASE | NET\_REQUEST\_STATS\_CMD\_GET\_ALL)

526

527[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_STATS\_GET\_ALL);

528

529#define NET\_REQUEST\_STATS\_GET\_PROCESSING\_ERROR \

530 (\_NET\_STATS\_BASE | NET\_REQUEST\_STATS\_CMD\_GET\_PROCESSING\_ERROR)

531

532[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_STATS\_GET\_PROCESSING\_ERROR);

533

534#define NET\_REQUEST\_STATS\_GET\_BYTES \

535 (\_NET\_STATS\_BASE | NET\_REQUEST\_STATS\_CMD\_GET\_BYTES)

536

537[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_STATS\_GET\_BYTES);

538

539#define NET\_REQUEST\_STATS\_GET\_IP\_ERRORS \

540 (\_NET\_STATS\_BASE | NET\_REQUEST\_STATS\_CMD\_GET\_IP\_ERRORS)

541

542[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_STATS\_GET\_IP\_ERRORS);

543

544#if defined(CONFIG\_NET\_STATISTICS\_IPV4)

545#define NET\_REQUEST\_STATS\_GET\_IPV4 \

546 (\_NET\_STATS\_BASE | NET\_REQUEST\_STATS\_CMD\_GET\_IPV4)

547

548[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_STATS\_GET\_IPV4);

549#endif /\* CONFIG\_NET\_STATISTICS\_IPV4 \*/

550

551#if defined(CONFIG\_NET\_STATISTICS\_IPV6)

552#define NET\_REQUEST\_STATS\_GET\_IPV6 \

553 (\_NET\_STATS\_BASE | NET\_REQUEST\_STATS\_CMD\_GET\_IPV6)

554

555[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_STATS\_GET\_IPV6);

556#endif /\* CONFIG\_NET\_STATISTICS\_IPV6 \*/

557

558#if defined(CONFIG\_NET\_STATISTICS\_IPV6\_ND)

559#define NET\_REQUEST\_STATS\_GET\_IPV6\_ND \

560 (\_NET\_STATS\_BASE | NET\_REQUEST\_STATS\_CMD\_GET\_IPV6\_ND)

561

562[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_STATS\_GET\_IPV6\_ND);

563#endif /\* CONFIG\_NET\_STATISTICS\_IPV6\_ND \*/

564

565#if defined(CONFIG\_NET\_STATISTICS\_ICMP)

566#define NET\_REQUEST\_STATS\_GET\_ICMP \

567 (\_NET\_STATS\_BASE | NET\_REQUEST\_STATS\_CMD\_GET\_ICMP)

568

569[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_STATS\_GET\_ICMP);

570#endif /\* CONFIG\_NET\_STATISTICS\_ICMP \*/

571

572#if defined(CONFIG\_NET\_STATISTICS\_UDP)

573#define NET\_REQUEST\_STATS\_GET\_UDP \

574 (\_NET\_STATS\_BASE | NET\_REQUEST\_STATS\_CMD\_GET\_UDP)

575

576[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_STATS\_GET\_UDP);

577#endif /\* CONFIG\_NET\_STATISTICS\_UDP \*/

578

579#if defined(CONFIG\_NET\_STATISTICS\_TCP)

580#define NET\_REQUEST\_STATS\_GET\_TCP \

581 (\_NET\_STATS\_BASE | NET\_REQUEST\_STATS\_CMD\_GET\_TCP)

582

583[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_STATS\_GET\_TCP);

584#endif /\* CONFIG\_NET\_STATISTICS\_TCP \*/

585

586#if defined(CONFIG\_NET\_STATISTICS\_ETHERNET)

587#define NET\_REQUEST\_STATS\_GET\_ETHERNET \

588 (\_NET\_STATS\_BASE | NET\_REQUEST\_STATS\_CMD\_GET\_ETHERNET)

589

590[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_STATS\_GET\_ETHERNET);

591#endif /\* CONFIG\_NET\_STATISTICS\_ETHERNET \*/

592

593#if defined(CONFIG\_NET\_STATISTICS\_PPP)

594#define NET\_REQUEST\_STATS\_GET\_PPP \

595 (\_NET\_STATS\_BASE | NET\_REQUEST\_STATS\_CMD\_GET\_PPP)

596

597[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_STATS\_GET\_PPP);

598#endif /\* CONFIG\_NET\_STATISTICS\_PPP \*/

599

600#endif /\* CONFIG\_NET\_STATISTICS\_USER\_API \*/

601

602#if defined(CONFIG\_NET\_STATISTICS\_POWER\_MANAGEMENT)

603#define NET\_REQUEST\_STATS\_GET\_PM \

604 (\_NET\_STATS\_BASE | NET\_REQUEST\_STATS\_CMD\_GET\_PM)

605

606[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_STATS\_GET\_PM);

607#endif /\* CONFIG\_NET\_STATISTICS\_POWER\_MANAGEMENT \*/

608

609#if defined(CONFIG\_NET\_STATISTICS\_WIFI)

610#define NET\_REQUEST\_STATS\_GET\_WIFI \

611 (\_NET\_STATS\_BASE | NET\_REQUEST\_STATS\_CMD\_GET\_WIFI)

612

613[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_STATS\_GET\_WIFI);

614#endif /\* CONFIG\_NET\_STATISTICS\_WIFI \*/

615

619

620#ifdef \_\_cplusplus

621}

622#endif

623

624#endif /\* ZEPHYR\_INCLUDE\_NET\_NET\_STATS\_H\_ \*/

[recv](group__bsd__sockets.md#gae11da452beee536eac85d5f26e5cdd40)

static ssize\_t recv(int sock, void \*buf, size\_t max\_len, int flags)

POSIX wrapper for zsock\_recv.

**Definition** socket.h:888

[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)

#define NET\_MGMT\_DEFINE\_REQUEST\_HANDLER(\_mgmt\_request)

**Definition** net\_mgmt.h:96

[net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752)

uint32\_t net\_stats\_t

Network statistics counter.

**Definition** net\_stats.h:36

[NET\_TC\_RX\_STATS\_COUNT](group__net__stats.md#ga10d8c8b3c671e0a625329a9a596e1265)

#define NET\_TC\_RX\_STATS\_COUNT

**Definition** net\_stats.h:245

[NET\_TC\_TX\_STATS\_COUNT](group__net__stats.md#ga83c834f2e8a8859051294e550d0b896c)

#define NET\_TC\_TX\_STATS\_COUNT

**Definition** net\_stats.h:239

[types.h](include_2zephyr_2types_8h.md)

[net\_core.h](net__core_8h.md)

Network core definitions.

[net\_mgmt.h](net__mgmt_8h.md)

Network Management API public header.

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

\_\_UINT64\_TYPE\_\_ uint64\_t

**Definition** stdint.h:91

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[net\_stats\_bytes](structnet__stats__bytes.md)

Number of bytes sent and received.

**Definition** net\_stats.h:41

[net\_stats\_bytes::sent](structnet__stats__bytes.md#a89368f376c02d25c5a7a5719851a0ac7)

net\_stats\_t sent

Number of bytes sent.

**Definition** net\_stats.h:43

[net\_stats\_bytes::received](structnet__stats__bytes.md#a8bc21878924210278c6e0e2861163be4)

net\_stats\_t received

Number of bytes received.

**Definition** net\_stats.h:45

[net\_stats\_eth\_csum](structnet__stats__eth__csum.md)

Ethernet checksum statistics.

**Definition** net\_stats.h:414

[net\_stats\_eth\_csum::rx\_csum\_offload\_good](structnet__stats__eth__csum.md#a1f1ba5c01c6232cd739d069ddb871b17)

net\_stats\_t rx\_csum\_offload\_good

**Definition** net\_stats.h:415

[net\_stats\_eth\_csum::rx\_csum\_offload\_errors](structnet__stats__eth__csum.md#ac4fc04d66193070d4f52a4c07f29ccce)

net\_stats\_t rx\_csum\_offload\_errors

**Definition** net\_stats.h:416

[net\_stats\_eth\_errors](structnet__stats__eth__errors.md)

Ethernet error statistics.

**Definition** net\_stats.h:377

[net\_stats\_eth\_errors::tx\_carrier\_errors](structnet__stats__eth__errors.md#a0043d1a1481040a6d7439bd23423ec12)

net\_stats\_t tx\_carrier\_errors

**Definition** net\_stats.h:391

[net\_stats\_eth\_errors::uncorr\_ecc\_errors](structnet__stats__eth__errors.md#a07d0a435f2129556520c732571d28edf)

net\_stats\_t uncorr\_ecc\_errors

**Definition** net\_stats.h:397

[net\_stats\_eth\_errors::rx\_long\_length\_errors](structnet__stats__eth__errors.md#a0e83e270a35222ed3e927800be4159e7)

net\_stats\_t rx\_long\_length\_errors

**Definition** net\_stats.h:384

[net\_stats\_eth\_errors::tx\_window\_errors](structnet__stats__eth__errors.md#a17624a12d6473bdd78698076fed0d122)

net\_stats\_t tx\_window\_errors

**Definition** net\_stats.h:394

[net\_stats\_eth\_errors::corr\_ecc\_errors](structnet__stats__eth__errors.md#a257113639f0e0e3085febb7a147f498f)

net\_stats\_t corr\_ecc\_errors

**Definition** net\_stats.h:398

[net\_stats\_eth\_errors::rx\_missed\_errors](structnet__stats__eth__errors.md#a2d2b2c4e3764ebec841f1ecbe7058d99)

net\_stats\_t rx\_missed\_errors

**Definition** net\_stats.h:383

[net\_stats\_eth\_errors::rx\_crc\_errors](structnet__stats__eth__errors.md#a4dab70cf219269bb393ce14faf0ed77e)

net\_stats\_t rx\_crc\_errors

**Definition** net\_stats.h:380

[net\_stats\_eth\_errors::rx\_short\_length\_errors](structnet__stats__eth__errors.md#a5e3d39d8417bb180cbfcb8c901006e81)

net\_stats\_t rx\_short\_length\_errors

**Definition** net\_stats.h:385

[net\_stats\_eth\_errors::rx\_align\_errors](structnet__stats__eth__errors.md#a7618f10af3443c49a6e256bb41e77781)

net\_stats\_t rx\_align\_errors

**Definition** net\_stats.h:386

[net\_stats\_eth\_errors::rx\_dma\_failed](structnet__stats__eth__errors.md#a7bcfbb13836f162ceeb5f021304b5c76)

net\_stats\_t rx\_dma\_failed

**Definition** net\_stats.h:387

[net\_stats\_eth\_errors::rx\_no\_buffer\_count](structnet__stats__eth__errors.md#a82622736d226b4d3b999f1f22ccf8529)

net\_stats\_t rx\_no\_buffer\_count

**Definition** net\_stats.h:382

[net\_stats\_eth\_errors::tx\_fifo\_errors](structnet__stats__eth__errors.md#a84630da9b82557f56dc35cd59ca2f7ae)

net\_stats\_t tx\_fifo\_errors

**Definition** net\_stats.h:392

[net\_stats\_eth\_errors::rx\_frame\_errors](structnet__stats__eth__errors.md#a8dfcc5cd1b4decec5783d01ba7033b05)

net\_stats\_t rx\_frame\_errors

**Definition** net\_stats.h:381

[net\_stats\_eth\_errors::rx\_over\_errors](structnet__stats__eth__errors.md#a9afee89f5bb01907e7cd515e2a0ff1b5)

net\_stats\_t rx\_over\_errors

**Definition** net\_stats.h:379

[net\_stats\_eth\_errors::tx\_dma\_failed](structnet__stats__eth__errors.md#abfbf6478b7afdd5935d7c6948c9ef426)

net\_stats\_t tx\_dma\_failed

**Definition** net\_stats.h:395

[net\_stats\_eth\_errors::rx\_length\_errors](structnet__stats__eth__errors.md#aca0e2e4807fa70279dee8ddaad2d7ef7)

net\_stats\_t rx\_length\_errors

**Definition** net\_stats.h:378

[net\_stats\_eth\_errors::rx\_buf\_alloc\_failed](structnet__stats__eth__errors.md#adbcae9c10c081f1cdf304bcdce740aa4)

net\_stats\_t rx\_buf\_alloc\_failed

**Definition** net\_stats.h:388

[net\_stats\_eth\_errors::tx\_heartbeat\_errors](structnet__stats__eth__errors.md#ae2a13733c1a5f0cc3e00efca0c3f429d)

net\_stats\_t tx\_heartbeat\_errors

**Definition** net\_stats.h:393

[net\_stats\_eth\_errors::tx\_aborted\_errors](structnet__stats__eth__errors.md#afec6a7e24c6f3cc74dd9f739f27b3e48)

net\_stats\_t tx\_aborted\_errors

**Definition** net\_stats.h:390

[net\_stats\_eth\_flow](structnet__stats__eth__flow.md)

Ethernet flow control statistics.

**Definition** net\_stats.h:404

[net\_stats\_eth\_flow::rx\_flow\_control\_xon](structnet__stats__eth__flow.md#a08e5da4ff78fe3893b9c9a628cefe4f2)

net\_stats\_t rx\_flow\_control\_xon

**Definition** net\_stats.h:405

[net\_stats\_eth\_flow::tx\_flow\_control\_xon](structnet__stats__eth__flow.md#a31412e8bf9d38ba630ea856e958a48d7)

net\_stats\_t tx\_flow\_control\_xon

**Definition** net\_stats.h:407

[net\_stats\_eth\_flow::rx\_flow\_control\_xoff](structnet__stats__eth__flow.md#a8f9b93537b3c11be70f276aaa72cb637)

net\_stats\_t rx\_flow\_control\_xoff

**Definition** net\_stats.h:406

[net\_stats\_eth\_flow::tx\_flow\_control\_xoff](structnet__stats__eth__flow.md#a969d81f9db20312d2d2aa7f70f93bdd5)

net\_stats\_t tx\_flow\_control\_xoff

**Definition** net\_stats.h:408

[net\_stats\_eth\_hw\_timestamp](structnet__stats__eth__hw__timestamp.md)

Ethernet hardware timestamp statistics.

**Definition** net\_stats.h:422

[net\_stats\_eth\_hw\_timestamp::tx\_hwtstamp\_timeouts](structnet__stats__eth__hw__timestamp.md#a41f605499dbf88a879522fdfa4633d9e)

net\_stats\_t tx\_hwtstamp\_timeouts

**Definition** net\_stats.h:424

[net\_stats\_eth\_hw\_timestamp::rx\_hwtstamp\_cleared](structnet__stats__eth__hw__timestamp.md#acd3d5f72d7df568110d96093e0c9534d)

net\_stats\_t rx\_hwtstamp\_cleared

**Definition** net\_stats.h:423

[net\_stats\_eth\_hw\_timestamp::tx\_hwtstamp\_skipped](structnet__stats__eth__hw__timestamp.md#ae1f983faf4a999308c464e4af5a5284b)

net\_stats\_t tx\_hwtstamp\_skipped

**Definition** net\_stats.h:425

[net\_stats\_eth](structnet__stats__eth.md)

All Ethernet specific statistics.

**Definition** net\_stats.h:441

[net\_stats\_eth::broadcast](structnet__stats__eth.md#a054beb909134b0e0f22f5df599549128)

struct net\_stats\_pkts broadcast

**Definition** net\_stats.h:444

[net\_stats\_eth::csum](structnet__stats__eth.md#a2169ae06bace1a93663bccf88c8d7a29)

struct net\_stats\_eth\_csum csum

**Definition** net\_stats.h:449

[net\_stats\_eth::tx\_dropped](structnet__stats__eth.md#a257c349cf3d32d38796e3899e702454a)

net\_stats\_t tx\_dropped

**Definition** net\_stats.h:452

[net\_stats\_eth::hw\_timestamp](structnet__stats__eth.md#a44667efff73c17c089ed22d5b0da5ad3)

struct net\_stats\_eth\_hw\_timestamp hw\_timestamp

**Definition** net\_stats.h:450

[net\_stats\_eth::multicast](structnet__stats__eth.md#a4f6a2903330518a132e7e547820e0bf2)

struct net\_stats\_pkts multicast

**Definition** net\_stats.h:445

[net\_stats\_eth::flow\_control](structnet__stats__eth.md#a643010ac6360c8c0c08016725ba12222)

struct net\_stats\_eth\_flow flow\_control

**Definition** net\_stats.h:448

[net\_stats\_eth::tx\_restart\_queue](structnet__stats__eth.md#a6699012226e25e8bad39076fed6dbfb5)

net\_stats\_t tx\_restart\_queue

**Definition** net\_stats.h:454

[net\_stats\_eth::collisions](structnet__stats__eth.md#a822d4205791f59999c842610522f6fc5)

net\_stats\_t collisions

**Definition** net\_stats.h:451

[net\_stats\_eth::bytes](structnet__stats__eth.md#a8c5cf1ead8ba214425a16fed1c2ad0fb)

struct net\_stats\_bytes bytes

**Definition** net\_stats.h:442

[net\_stats\_eth::error\_details](structnet__stats__eth.md#a922feddb17fc020371f1bcc52c709415)

struct net\_stats\_eth\_errors error\_details

**Definition** net\_stats.h:447

[net\_stats\_eth::pkts](structnet__stats__eth.md#a97bd6026b16890743f344751a21107f1)

struct net\_stats\_pkts pkts

**Definition** net\_stats.h:443

[net\_stats\_eth::errors](structnet__stats__eth.md#a9c869740f416fbe0b54d7fefacb1fe29)

struct net\_stats\_pkts errors

**Definition** net\_stats.h:446

[net\_stats\_eth::tx\_timeout\_count](structnet__stats__eth.md#ab351258ae82abd09759d37774559d8bc)

net\_stats\_t tx\_timeout\_count

**Definition** net\_stats.h:453

[net\_stats\_eth::unknown\_protocol](structnet__stats__eth.md#afaacee7cc1d0a35ae2344175421c40dd)

net\_stats\_t unknown\_protocol

**Definition** net\_stats.h:455

[net\_stats\_icmp](structnet__stats__icmp.md)

ICMP statistics.

**Definition** net\_stats.h:105

[net\_stats\_icmp::sent](structnet__stats__icmp.md#a2d6eb7dfc8f4b439b399b039022f2889)

net\_stats\_t sent

Number of sent ICMP packets.

**Definition** net\_stats.h:110

[net\_stats\_icmp::chkerr](structnet__stats__icmp.md#a6662bc547107a08c52e902a2446629bf)

net\_stats\_t chkerr

Number of ICMP packets with a bad checksum.

**Definition** net\_stats.h:119

[net\_stats\_icmp::drop](structnet__stats__icmp.md#a755f3388c05d4bd2988ddd16d1a4cf32)

net\_stats\_t drop

Number of dropped ICMP packets.

**Definition** net\_stats.h:113

[net\_stats\_icmp::typeerr](structnet__stats__icmp.md#ae1a29dd9b8e1ce9a737fa7f36c805cd4)

net\_stats\_t typeerr

Number of ICMP packets with a wrong type.

**Definition** net\_stats.h:116

[net\_stats\_icmp::recv](structnet__stats__icmp.md#ae6f226b55565c11fca0c9e099f08c267)

net\_stats\_t recv

Number of received ICMP packets.

**Definition** net\_stats.h:107

[net\_stats\_ip\_errors](structnet__stats__ip__errors.md)

IP layer error statistics.

**Definition** net\_stats.h:78

[net\_stats\_ip\_errors::hblenerr](structnet__stats__ip__errors.md#a06b35742c418ebc6414fcb5c7002edde)

net\_stats\_t hblenerr

Number of packets dropped due to wrong IP length, high byte.

**Definition** net\_stats.h:85

[net\_stats\_ip\_errors::vhlerr](structnet__stats__ip__errors.md#a3e476f659ebeaa5c5f7b6dad2d90326f)

net\_stats\_t vhlerr

Number of packets dropped due to wrong IP version or header length.

**Definition** net\_stats.h:82

[net\_stats\_ip\_errors::chkerr](structnet__stats__ip__errors.md#a872cc0beca45bbe87ae794dd8ca4e301)

net\_stats\_t chkerr

Number of packets dropped due to IP checksum errors.

**Definition** net\_stats.h:94

[net\_stats\_ip\_errors::protoerr](structnet__stats__ip__errors.md#a978b1c23847e707ac1fa27c2b34fa85d)

net\_stats\_t protoerr

Number of packets dropped because they were neither ICMP, UDP nor TCP.

**Definition** net\_stats.h:99

[net\_stats\_ip\_errors::lblenerr](structnet__stats__ip__errors.md#a9b4bf05e9df13e1d99518125b9067bef)

net\_stats\_t lblenerr

Number of packets dropped due to wrong IP length, low byte.

**Definition** net\_stats.h:88

[net\_stats\_ip\_errors::fragerr](structnet__stats__ip__errors.md#ab84ee9dfbe5da391d60c6e3ae9abea16)

net\_stats\_t fragerr

Number of packets dropped because they were IP fragments.

**Definition** net\_stats.h:91

[net\_stats\_ip](structnet__stats__ip.md)

IP layer statistics.

**Definition** net\_stats.h:61

[net\_stats\_ip::forwarded](structnet__stats__ip.md#a4bb82a5ebebaa3e8a11973c07eed96a0)

net\_stats\_t forwarded

Number of forwarded packets at the IP layer.

**Definition** net\_stats.h:69

[net\_stats\_ip::recv](structnet__stats__ip.md#ab6a6373368dd24cb51504c5729d535d3)

net\_stats\_t recv

Number of received packets at the IP layer.

**Definition** net\_stats.h:63

[net\_stats\_ip::sent](structnet__stats__ip.md#abbe676bbe9faa89b2b6b8c4950b1c9d5)

net\_stats\_t sent

Number of sent packets at the IP layer.

**Definition** net\_stats.h:66

[net\_stats\_ip::drop](structnet__stats__ip.md#ac86399b70d7f761162e5336dd15589eb)

net\_stats\_t drop

Number of dropped packets at the IP layer.

**Definition** net\_stats.h:72

[net\_stats\_ipv4\_igmp](structnet__stats__ipv4__igmp.md)

IPv4 IGMP daemon statistics.

**Definition** net\_stats.h:211

[net\_stats\_ipv4\_igmp::drop](structnet__stats__ipv4__igmp.md#a1c37702ff837b8c5cc9df5f690e7678c)

net\_stats\_t drop

Number of dropped IPv4 IGMP packets.

**Definition** net\_stats.h:219

[net\_stats\_ipv4\_igmp::recv](structnet__stats__ipv4__igmp.md#a469113de7af0ba42dbd1b0365d00602c)

net\_stats\_t recv

Number of received IPv4 IGMP queries.

**Definition** net\_stats.h:213

[net\_stats\_ipv4\_igmp::sent](structnet__stats__ipv4__igmp.md#a955e20a6ee5e19e08000b3114b9d71a6)

net\_stats\_t sent

Number of sent IPv4 IGMP reports.

**Definition** net\_stats.h:216

[net\_stats\_ipv6\_mld](structnet__stats__ipv6__mld.md)

IPv6 multicast listener daemon statistics.

**Definition** net\_stats.h:197

[net\_stats\_ipv6\_mld::recv](structnet__stats__ipv6__mld.md#a4879ff9e31f8b60973d3b169598e921d)

net\_stats\_t recv

Number of received IPv6 MLD queries.

**Definition** net\_stats.h:199

[net\_stats\_ipv6\_mld::sent](structnet__stats__ipv6__mld.md#ab397b74b14ce7047bf2fc63ca72ce1e5)

net\_stats\_t sent

Number of sent IPv6 MLD reports.

**Definition** net\_stats.h:202

[net\_stats\_ipv6\_mld::drop](structnet__stats__ipv6__mld.md#ad85dc87f57296a1e7d64e959b0370ee8)

net\_stats\_t drop

Number of dropped IPv6 MLD packets.

**Definition** net\_stats.h:205

[net\_stats\_ipv6\_nd](structnet__stats__ipv6__nd.md)

IPv6 neighbor discovery statistics.

**Definition** net\_stats.h:188

[net\_stats\_ipv6\_nd::sent](structnet__stats__ipv6__nd.md#a0129f7892a4439c20deb2f32b9001277)

net\_stats\_t sent

**Definition** net\_stats.h:191

[net\_stats\_ipv6\_nd::recv](structnet__stats__ipv6__nd.md#a0bf6f67d9112996a3b002ea160aec769)

net\_stats\_t recv

**Definition** net\_stats.h:190

[net\_stats\_ipv6\_nd::drop](structnet__stats__ipv6__nd.md#a31074d5d44138fcabdc5f7750f9f2c47)

net\_stats\_t drop

**Definition** net\_stats.h:189

[net\_stats\_pkts](structnet__stats__pkts.md)

Number of network packets sent and received.

**Definition** net\_stats.h:51

[net\_stats\_pkts::rx](structnet__stats__pkts.md#ac9784b5a245e6c57e39318aaf314f0cf)

net\_stats\_t rx

Number of packets received.

**Definition** net\_stats.h:55

[net\_stats\_pkts::tx](structnet__stats__pkts.md#aee1e302d0f8dac79b693a06d8fa3b3c5)

net\_stats\_t tx

Number of packets sent.

**Definition** net\_stats.h:53

[net\_stats\_pm](structnet__stats__pm.md)

Power management statistics.

**Definition** net\_stats.h:281

[net\_stats\_pm::last\_suspend\_time](structnet__stats__pm.md#a0bdf9c3676298e2df4ff3bfa03f5e823)

uint32\_t last\_suspend\_time

**Definition** net\_stats.h:284

[net\_stats\_pm::start\_time](structnet__stats__pm.md#a6784806eaa093431ed3c0f7acfe5a89c)

uint32\_t start\_time

**Definition** net\_stats.h:285

[net\_stats\_pm::overall\_suspend\_time](structnet__stats__pm.md#ab43935fcfe9efc1cd5f3e7e329996805)

uint64\_t overall\_suspend\_time

**Definition** net\_stats.h:282

[net\_stats\_pm::suspend\_count](structnet__stats__pm.md#ac14122a4765c499c045f18c70af355a0)

net\_stats\_t suspend\_count

**Definition** net\_stats.h:283

[net\_stats\_ppp](structnet__stats__ppp.md)

All PPP specific statistics.

**Definition** net\_stats.h:465

[net\_stats\_ppp::chkerr](structnet__stats__ppp.md#a1332b31980f82236aeb0c3f9444e2ac6)

net\_stats\_t chkerr

Number of received PPP frames with a bad checksum.

**Definition** net\_stats.h:473

[net\_stats\_ppp::pkts](structnet__stats__ppp.md#a71fc81f3c5f3e65a476b3391f086d340)

struct net\_stats\_pkts pkts

**Definition** net\_stats.h:467

[net\_stats\_ppp::bytes](structnet__stats__ppp.md#ab2b48da7f19d4b83e3f41b41979b7ed8)

struct net\_stats\_bytes bytes

**Definition** net\_stats.h:466

[net\_stats\_ppp::drop](structnet__stats__ppp.md#ae2e0a47a539e9d7bc97f9c63f889b276)

net\_stats\_t drop

Number of received and dropped PPP frames.

**Definition** net\_stats.h:470

[net\_stats\_rx\_time](structnet__stats__rx__time.md)

Network packet receive times for calculating average RX time.

**Definition** net\_stats.h:233

[net\_stats\_rx\_time::sum](structnet__stats__rx__time.md#a4b84c2ae2fda8fcd75fdf1bf0b2aae8d)

uint64\_t sum

**Definition** net\_stats.h:234

[net\_stats\_rx\_time::count](structnet__stats__rx__time.md#a68247051b064de081fa2e84118192958)

net\_stats\_t count

**Definition** net\_stats.h:235

[net\_stats\_sta\_mgmt](structnet__stats__sta__mgmt.md)

All Wi-Fi management statistics.

**Definition** net\_stats.h:479

[net\_stats\_sta\_mgmt::beacons\_miss](structnet__stats__sta__mgmt.md#a29ae0079b4c780e0de2656a85ec15fe9)

net\_stats\_t beacons\_miss

Number of missed beacons.

**Definition** net\_stats.h:484

[net\_stats\_sta\_mgmt::beacons\_rx](structnet__stats__sta__mgmt.md#ac6e68fded8e19b20259442436923f815)

net\_stats\_t beacons\_rx

Number of received beacons.

**Definition** net\_stats.h:481

[net\_stats\_tc](structnet__stats__tc.md)

Traffic class statistics.

**Definition** net\_stats.h:253

[net\_stats\_tc::bytes](structnet__stats__tc.md#a192a7ec0d24bce9e62f766e481ee5709)

net\_stats\_t bytes

**Definition** net\_stats.h:261

[net\_stats\_tc::tx\_time](structnet__stats__tc.md#a30288ef3bb0796cd18c3cf0aedbe875a)

struct net\_stats\_tx\_time tx\_time

**Definition** net\_stats.h:255

[net\_stats\_tc::sent](structnet__stats__tc.md#a303e66b023d64b46b621e3384be8b822)

struct net\_stats\_tc::@074155214116325077102236356156227241054306002026 sent[1]

[net\_stats\_tc::pkts](structnet__stats__tc.md#a6614b5f5186635415a7d787260c39248)

net\_stats\_t pkts

**Definition** net\_stats.h:260

[net\_stats\_tc::priority](structnet__stats__tc.md#a8a5c2e59990407ddbfc7973a1c183bf6)

uint8\_t priority

**Definition** net\_stats.h:262

[net\_stats\_tc::rx\_time](structnet__stats__tc.md#a8ea00824bb0fb18e4d8912343e01c3b7)

struct net\_stats\_rx\_time rx\_time

**Definition** net\_stats.h:266

[net\_stats\_tcp](structnet__stats__tcp.md)

TCP statistics.

**Definition** net\_stats.h:125

[net\_stats\_tcp::ackerr](structnet__stats__tcp.md#a0d40abc85776f0a9b9510a909b7f6d18)

net\_stats\_t ackerr

Number of received TCP segments with a bad ACK number.

**Definition** net\_stats.h:148

[net\_stats\_tcp::rsterr](structnet__stats__tcp.md#a471fcd5578f79ce77d20547b28503ac1)

net\_stats\_t rsterr

Number of received bad TCP RST (reset) segments.

**Definition** net\_stats.h:151

[net\_stats\_tcp::rexmit](structnet__stats__tcp.md#a4a4ea6e5d87ef58b4271bd708cf39635)

net\_stats\_t rexmit

Number of retransmitted TCP segments.

**Definition** net\_stats.h:157

[net\_stats\_tcp::chkerr](structnet__stats__tcp.md#a5099e174b0eafa322f0630f1f5c73a8b)

net\_stats\_t chkerr

Number of TCP segments with a bad checksum.

**Definition** net\_stats.h:145

[net\_stats\_tcp::seg\_drop](structnet__stats__tcp.md#a5f045704859331918511e9c2281ac155)

net\_stats\_t seg\_drop

Number of dropped TCP segments.

**Definition** net\_stats.h:142

[net\_stats\_tcp::connrst](structnet__stats__tcp.md#a67f55954a4c51f2b957c7d974e78c1c0)

net\_stats\_t connrst

Number of connection attempts for closed ports, triggering a RST.

**Definition** net\_stats.h:165

[net\_stats\_tcp::drop](structnet__stats__tcp.md#aa549f7b6d5828009a09190fd64afa8e3)

net\_stats\_t drop

Number of dropped packets at the TCP layer.

**Definition** net\_stats.h:133

[net\_stats\_tcp::rst](structnet__stats__tcp.md#aa618cf86b962aca0f14eb9178c8ae61a)

net\_stats\_t rst

Number of received TCP RST (reset) segments.

**Definition** net\_stats.h:154

[net\_stats\_tcp::sent](structnet__stats__tcp.md#aa987bebf96000b6b4e92bfafc218759a)

net\_stats\_t sent

Number of sent TCP segments.

**Definition** net\_stats.h:139

[net\_stats\_tcp::resent](structnet__stats__tcp.md#abe567032cb4a267a984aec28c1e3cca4)

net\_stats\_t resent

Amount of retransmitted data.

**Definition** net\_stats.h:130

[net\_stats\_tcp::conndrop](structnet__stats__tcp.md#ac557ac0d8917bc2c2dfed74126f993c8)

net\_stats\_t conndrop

Number of dropped connection attempts because too few connections were available.

**Definition** net\_stats.h:162

[net\_stats\_tcp::recv](structnet__stats__tcp.md#ad25edb2b39a6acc8152c35ad43a5042f)

net\_stats\_t recv

Number of received TCP segments.

**Definition** net\_stats.h:136

[net\_stats\_tcp::bytes](structnet__stats__tcp.md#af80c18bcc253133ce5f0597ac190b349)

struct net\_stats\_bytes bytes

Amount of received and sent TCP application data.

**Definition** net\_stats.h:127

[net\_stats\_tx\_time](structnet__stats__tx__time.md)

Network packet transfer times for calculating average TX time.

**Definition** net\_stats.h:225

[net\_stats\_tx\_time::count](structnet__stats__tx__time.md#a7a652350ed04e53ba02aec294f8444b4)

net\_stats\_t count

**Definition** net\_stats.h:227

[net\_stats\_tx\_time::sum](structnet__stats__tx__time.md#af6f7a26c0344a0f93306e105a8917c3e)

uint64\_t sum

**Definition** net\_stats.h:226

[net\_stats\_udp](structnet__stats__udp.md)

UDP statistics.

**Definition** net\_stats.h:171

[net\_stats\_udp::recv](structnet__stats__udp.md#a0ea91d85fe322661fb909f5e94e55a34)

net\_stats\_t recv

Number of received UDP segments.

**Definition** net\_stats.h:176

[net\_stats\_udp::drop](structnet__stats__udp.md#a2d884bf9106e60d430ffec7c7964a609)

net\_stats\_t drop

Number of dropped UDP segments.

**Definition** net\_stats.h:173

[net\_stats\_udp::chkerr](structnet__stats__udp.md#a4c57d5f68ebda7981400729b9c7fe0f7)

net\_stats\_t chkerr

Number of UDP segments with a bad checksum.

**Definition** net\_stats.h:182

[net\_stats\_udp::sent](structnet__stats__udp.md#ab4e8228c221901d3ded55f3f823bfa1c)

net\_stats\_t sent

Number of sent UDP segments.

**Definition** net\_stats.h:179

[net\_stats\_wifi](structnet__stats__wifi.md)

All Wi-Fi specific statistics.

**Definition** net\_stats.h:490

[net\_stats\_wifi::broadcast](structnet__stats__wifi.md#a03dc04638c4b670bd7f3520d45fc1eda)

struct net\_stats\_pkts broadcast

**Definition** net\_stats.h:494

[net\_stats\_wifi::multicast](structnet__stats__wifi.md#a7e7f68215101885fd51c70e981da26e7)

struct net\_stats\_pkts multicast

**Definition** net\_stats.h:495

[net\_stats\_wifi::sta\_mgmt](structnet__stats__wifi.md#a8bee22961545674e6ab100b58a04bf91)

struct net\_stats\_sta\_mgmt sta\_mgmt

**Definition** net\_stats.h:491

[net\_stats\_wifi::bytes](structnet__stats__wifi.md#aa055b1e8bd8f1e50815c1028b562be07)

struct net\_stats\_bytes bytes

**Definition** net\_stats.h:492

[net\_stats\_wifi::pkts](structnet__stats__wifi.md#adbcdb2dd8733f2917c00a0b2d365393b)

struct net\_stats\_pkts pkts

**Definition** net\_stats.h:493

[net\_stats\_wifi::errors](structnet__stats__wifi.md#ae0149e64a94a9f96eb6680f94793c8c4)

struct net\_stats\_pkts errors

**Definition** net\_stats.h:496

[net\_stats](structnet__stats.md)

All network statistics in one struct.

**Definition** net\_stats.h:292

[net\_stats::processing\_error](structnet__stats.md#a3a4c90661d6b310b628262228a341fe2)

net\_stats\_t processing\_error

Count of malformed packets or packets we do not have handler for.

**Definition** net\_stats.h:294

[net\_stats::bytes](structnet__stats.md#a7a28233e6d23efdce0143469b9bb6c05)

struct net\_stats\_bytes bytes

This calculates amount of data transferred through all the network interfaces.

**Definition** net\_stats.h:300

[net\_stats::ip\_errors](structnet__stats.md#ac42cb13954d164e92a1ef60919a2a34e)

struct net\_stats\_ip\_errors ip\_errors

IP layer errors.

**Definition** net\_stats.h:303

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [net\_stats.h](net__stats_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
