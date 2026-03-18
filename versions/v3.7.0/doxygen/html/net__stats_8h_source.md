---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/net__stats_8h_source.html
original_path: doxygen/html/net__stats_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
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

[ 190](structnet__stats__ipv6__nd.md#a31074d5d44138fcabdc5f7750f9f2c47) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [drop](structnet__stats__ipv6__nd.md#a31074d5d44138fcabdc5f7750f9f2c47);

191

[ 193](structnet__stats__ipv6__nd.md#a0bf6f67d9112996a3b002ea160aec769) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [recv](structnet__stats__ipv6__nd.md#a0bf6f67d9112996a3b002ea160aec769);

194

[ 196](structnet__stats__ipv6__nd.md#a0129f7892a4439c20deb2f32b9001277) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [sent](structnet__stats__ipv6__nd.md#a0129f7892a4439c20deb2f32b9001277);

197};

198

[ 202](structnet__stats__ipv6__mld.md)struct [net\_stats\_ipv6\_mld](structnet__stats__ipv6__mld.md) {

[ 204](structnet__stats__ipv6__mld.md#a4879ff9e31f8b60973d3b169598e921d) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [recv](structnet__stats__ipv6__mld.md#a4879ff9e31f8b60973d3b169598e921d);

205

[ 207](structnet__stats__ipv6__mld.md#ab397b74b14ce7047bf2fc63ca72ce1e5) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [sent](structnet__stats__ipv6__mld.md#ab397b74b14ce7047bf2fc63ca72ce1e5);

208

[ 210](structnet__stats__ipv6__mld.md#ad85dc87f57296a1e7d64e959b0370ee8) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [drop](structnet__stats__ipv6__mld.md#ad85dc87f57296a1e7d64e959b0370ee8);

211};

212

[ 216](structnet__stats__ipv4__igmp.md)struct [net\_stats\_ipv4\_igmp](structnet__stats__ipv4__igmp.md) {

[ 218](structnet__stats__ipv4__igmp.md#a469113de7af0ba42dbd1b0365d00602c) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [recv](structnet__stats__ipv4__igmp.md#a469113de7af0ba42dbd1b0365d00602c);

219

[ 221](structnet__stats__ipv4__igmp.md#a955e20a6ee5e19e08000b3114b9d71a6) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [sent](structnet__stats__ipv4__igmp.md#a955e20a6ee5e19e08000b3114b9d71a6);

222

[ 224](structnet__stats__ipv4__igmp.md#a1c37702ff837b8c5cc9df5f690e7678c) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [drop](structnet__stats__ipv4__igmp.md#a1c37702ff837b8c5cc9df5f690e7678c);

225};

226

[ 230](structnet__stats__tx__time.md)struct [net\_stats\_tx\_time](structnet__stats__tx__time.md) {

[ 232](structnet__stats__tx__time.md#af6f7a26c0344a0f93306e105a8917c3e) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [sum](structnet__stats__tx__time.md#af6f7a26c0344a0f93306e105a8917c3e);

233

[ 235](structnet__stats__tx__time.md#a7a652350ed04e53ba02aec294f8444b4) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [count](structnet__stats__tx__time.md#a7a652350ed04e53ba02aec294f8444b4);

236};

237

[ 241](structnet__stats__rx__time.md)struct [net\_stats\_rx\_time](structnet__stats__rx__time.md) {

[ 243](structnet__stats__rx__time.md#a4b84c2ae2fda8fcd75fdf1bf0b2aae8d) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [sum](structnet__stats__rx__time.md#a4b84c2ae2fda8fcd75fdf1bf0b2aae8d);

244

[ 246](structnet__stats__rx__time.md#a68247051b064de081fa2e84118192958) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [count](structnet__stats__rx__time.md#a68247051b064de081fa2e84118192958);

247};

248

250

251#if NET\_TC\_TX\_COUNT == 0

252#define NET\_TC\_TX\_STATS\_COUNT 1

253#else

254#define NET\_TC\_TX\_STATS\_COUNT NET\_TC\_TX\_COUNT

255#endif

256

257#if NET\_TC\_RX\_COUNT == 0

258#define NET\_TC\_RX\_STATS\_COUNT 1

259#else

260#define NET\_TC\_RX\_STATS\_COUNT NET\_TC\_RX\_COUNT

261#endif

262

264

[ 268](structnet__stats__tc.md)struct [net\_stats\_tc](structnet__stats__tc.md) {

270 struct {

[ 272](structnet__stats__tc.md#a30288ef3bb0796cd18c3cf0aedbe875a) struct [net\_stats\_tx\_time](structnet__stats__tx__time.md) [tx\_time](structnet__stats__tc.md#a30288ef3bb0796cd18c3cf0aedbe875a);

273#if defined(CONFIG\_NET\_PKT\_TXTIME\_STATS\_DETAIL)

275 struct [net\_stats\_tx\_time](structnet__stats__tx__time.md)

276 tx\_time\_detail[NET\_PKT\_DETAIL\_STATS\_COUNT];

277#endif

[ 279](structnet__stats__tc.md#a6614b5f5186635415a7d787260c39248) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [pkts](structnet__stats__tc.md#a6614b5f5186635415a7d787260c39248);

[ 281](structnet__stats__tc.md#a192a7ec0d24bce9e62f766e481ee5709) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [bytes](structnet__stats__tc.md#a192a7ec0d24bce9e62f766e481ee5709);

[ 283](structnet__stats__tc.md#a8a5c2e59990407ddbfc7973a1c183bf6) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [priority](structnet__stats__tc.md#a8a5c2e59990407ddbfc7973a1c183bf6);

[ 284](structnet__stats__tc.md#a8d6a3ebcc49ce8c34a5faae986f648e2) } [sent](structnet__stats__tc.md#a8d6a3ebcc49ce8c34a5faae986f648e2)[NET\_TC\_TX\_STATS\_COUNT];

285

287 struct {

[ 289](structnet__stats__tc.md#a8ea00824bb0fb18e4d8912343e01c3b7) struct [net\_stats\_rx\_time](structnet__stats__rx__time.md) [rx\_time](structnet__stats__tc.md#a8ea00824bb0fb18e4d8912343e01c3b7);

290#if defined(CONFIG\_NET\_PKT\_RXTIME\_STATS\_DETAIL)

292 struct [net\_stats\_rx\_time](structnet__stats__rx__time.md)

293 rx\_time\_detail[NET\_PKT\_DETAIL\_STATS\_COUNT];

294#endif

296 [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [pkts](structnet__stats__tc.md#a6614b5f5186635415a7d787260c39248);

298 [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [bytes](structnet__stats__tc.md#a192a7ec0d24bce9e62f766e481ee5709);

300 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [priority](structnet__stats__tc.md#a8a5c2e59990407ddbfc7973a1c183bf6);

[ 301](structnet__stats__tc.md#a2c8826e27ff59154f14a1755ffd4c594) } [recv](group__bsd__sockets.md#gae11da452beee536eac85d5f26e5cdd40)[NET\_TC\_RX\_STATS\_COUNT];

302};

303

304

[ 308](structnet__stats__pm.md)struct [net\_stats\_pm](structnet__stats__pm.md) {

[ 310](structnet__stats__pm.md#ab43935fcfe9efc1cd5f3e7e329996805) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [overall\_suspend\_time](structnet__stats__pm.md#ab43935fcfe9efc1cd5f3e7e329996805);

[ 312](structnet__stats__pm.md#ac14122a4765c499c045f18c70af355a0) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [suspend\_count](structnet__stats__pm.md#ac14122a4765c499c045f18c70af355a0);

[ 314](structnet__stats__pm.md#a0bdf9c3676298e2df4ff3bfa03f5e823) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [last\_suspend\_time](structnet__stats__pm.md#a0bdf9c3676298e2df4ff3bfa03f5e823);

[ 316](structnet__stats__pm.md#a6784806eaa093431ed3c0f7acfe5a89c) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [start\_time](structnet__stats__pm.md#a6784806eaa093431ed3c0f7acfe5a89c);

317};

318

319

[ 323](structnet__stats.md)struct [net\_stats](structnet__stats.md) {

[ 325](structnet__stats.md#a3a4c90661d6b310b628262228a341fe2) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [processing\_error](structnet__stats.md#a3a4c90661d6b310b628262228a341fe2);

326

[ 331](structnet__stats.md#a7a28233e6d23efdce0143469b9bb6c05) struct [net\_stats\_bytes](structnet__stats__bytes.md) [bytes](structnet__stats.md#a7a28233e6d23efdce0143469b9bb6c05);

332

[ 334](structnet__stats.md#ac42cb13954d164e92a1ef60919a2a34e) struct [net\_stats\_ip\_errors](structnet__stats__ip__errors.md) [ip\_errors](structnet__stats.md#ac42cb13954d164e92a1ef60919a2a34e);

335

336#if defined(CONFIG\_NET\_STATISTICS\_IPV6)

338 struct [net\_stats\_ip](structnet__stats__ip.md) ipv6;

339#endif

340

341#if defined(CONFIG\_NET\_STATISTICS\_IPV4)

343 struct [net\_stats\_ip](structnet__stats__ip.md) ipv4;

344#endif

345

346#if defined(CONFIG\_NET\_STATISTICS\_ICMP)

348 struct [net\_stats\_icmp](structnet__stats__icmp.md) icmp;

349#endif

350

351#if defined(CONFIG\_NET\_STATISTICS\_TCP)

353 struct [net\_stats\_tcp](structnet__stats__tcp.md) tcp;

354#endif

355

356#if defined(CONFIG\_NET\_STATISTICS\_UDP)

358 struct [net\_stats\_udp](structnet__stats__udp.md) udp;

359#endif

360

361#if defined(CONFIG\_NET\_STATISTICS\_IPV6\_ND)

363 struct [net\_stats\_ipv6\_nd](structnet__stats__ipv6__nd.md) ipv6\_nd;

364#endif

365

366#if defined(CONFIG\_NET\_STATISTICS\_MLD)

368 struct [net\_stats\_ipv6\_mld](structnet__stats__ipv6__mld.md) ipv6\_mld;

369#endif

370

371#if defined(CONFIG\_NET\_STATISTICS\_IGMP)

373 struct [net\_stats\_ipv4\_igmp](structnet__stats__ipv4__igmp.md) ipv4\_igmp;

374#endif

375

376#if NET\_TC\_COUNT > 1

378 struct [net\_stats\_tc](structnet__stats__tc.md) tc;

379#endif

380

381#if defined(CONFIG\_NET\_PKT\_TXTIME\_STATS)

383 struct [net\_stats\_tx\_time](structnet__stats__tx__time.md) tx\_time;

384#endif

385

386#if defined(CONFIG\_NET\_PKT\_RXTIME\_STATS)

388 struct [net\_stats\_rx\_time](structnet__stats__rx__time.md) rx\_time;

389#endif

390

391#if defined(CONFIG\_NET\_PKT\_TXTIME\_STATS\_DETAIL)

393 struct [net\_stats\_tx\_time](structnet__stats__tx__time.md) tx\_time\_detail[NET\_PKT\_DETAIL\_STATS\_COUNT];

394#endif

395#if defined(CONFIG\_NET\_PKT\_RXTIME\_STATS\_DETAIL)

397 struct [net\_stats\_rx\_time](structnet__stats__rx__time.md) rx\_time\_detail[NET\_PKT\_DETAIL\_STATS\_COUNT];

398#endif

399

400#if defined(CONFIG\_NET\_STATISTICS\_POWER\_MANAGEMENT)

402 struct [net\_stats\_pm](structnet__stats__pm.md) pm;

403#endif

404};

405

[ 409](structnet__stats__eth__errors.md)struct [net\_stats\_eth\_errors](structnet__stats__eth__errors.md) {

[ 411](structnet__stats__eth__errors.md#aca0e2e4807fa70279dee8ddaad2d7ef7) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [rx\_length\_errors](structnet__stats__eth__errors.md#aca0e2e4807fa70279dee8ddaad2d7ef7);

412

[ 414](structnet__stats__eth__errors.md#a9afee89f5bb01907e7cd515e2a0ff1b5) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [rx\_over\_errors](structnet__stats__eth__errors.md#a9afee89f5bb01907e7cd515e2a0ff1b5);

415

[ 417](structnet__stats__eth__errors.md#a4dab70cf219269bb393ce14faf0ed77e) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [rx\_crc\_errors](structnet__stats__eth__errors.md#a4dab70cf219269bb393ce14faf0ed77e);

418

[ 420](structnet__stats__eth__errors.md#a8dfcc5cd1b4decec5783d01ba7033b05) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [rx\_frame\_errors](structnet__stats__eth__errors.md#a8dfcc5cd1b4decec5783d01ba7033b05);

421

[ 423](structnet__stats__eth__errors.md#a82622736d226b4d3b999f1f22ccf8529) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [rx\_no\_buffer\_count](structnet__stats__eth__errors.md#a82622736d226b4d3b999f1f22ccf8529);

424

[ 426](structnet__stats__eth__errors.md#a2d2b2c4e3764ebec841f1ecbe7058d99) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [rx\_missed\_errors](structnet__stats__eth__errors.md#a2d2b2c4e3764ebec841f1ecbe7058d99);

427

[ 429](structnet__stats__eth__errors.md#a0e83e270a35222ed3e927800be4159e7) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [rx\_long\_length\_errors](structnet__stats__eth__errors.md#a0e83e270a35222ed3e927800be4159e7);

430

[ 432](structnet__stats__eth__errors.md#a5e3d39d8417bb180cbfcb8c901006e81) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [rx\_short\_length\_errors](structnet__stats__eth__errors.md#a5e3d39d8417bb180cbfcb8c901006e81);

433

[ 435](structnet__stats__eth__errors.md#a7618f10af3443c49a6e256bb41e77781) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [rx\_align\_errors](structnet__stats__eth__errors.md#a7618f10af3443c49a6e256bb41e77781);

436

[ 438](structnet__stats__eth__errors.md#a7bcfbb13836f162ceeb5f021304b5c76) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [rx\_dma\_failed](structnet__stats__eth__errors.md#a7bcfbb13836f162ceeb5f021304b5c76);

439

[ 441](structnet__stats__eth__errors.md#adbcae9c10c081f1cdf304bcdce740aa4) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [rx\_buf\_alloc\_failed](structnet__stats__eth__errors.md#adbcae9c10c081f1cdf304bcdce740aa4);

442

[ 444](structnet__stats__eth__errors.md#afec6a7e24c6f3cc74dd9f739f27b3e48) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [tx\_aborted\_errors](structnet__stats__eth__errors.md#afec6a7e24c6f3cc74dd9f739f27b3e48);

445

[ 447](structnet__stats__eth__errors.md#a0043d1a1481040a6d7439bd23423ec12) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [tx\_carrier\_errors](structnet__stats__eth__errors.md#a0043d1a1481040a6d7439bd23423ec12);

448

[ 450](structnet__stats__eth__errors.md#a84630da9b82557f56dc35cd59ca2f7ae) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [tx\_fifo\_errors](structnet__stats__eth__errors.md#a84630da9b82557f56dc35cd59ca2f7ae);

451

[ 453](structnet__stats__eth__errors.md#ae2a13733c1a5f0cc3e00efca0c3f429d) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [tx\_heartbeat\_errors](structnet__stats__eth__errors.md#ae2a13733c1a5f0cc3e00efca0c3f429d);

454

[ 456](structnet__stats__eth__errors.md#a17624a12d6473bdd78698076fed0d122) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [tx\_window\_errors](structnet__stats__eth__errors.md#a17624a12d6473bdd78698076fed0d122);

457

[ 459](structnet__stats__eth__errors.md#abfbf6478b7afdd5935d7c6948c9ef426) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [tx\_dma\_failed](structnet__stats__eth__errors.md#abfbf6478b7afdd5935d7c6948c9ef426);

460

[ 462](structnet__stats__eth__errors.md#a07d0a435f2129556520c732571d28edf) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [uncorr\_ecc\_errors](structnet__stats__eth__errors.md#a07d0a435f2129556520c732571d28edf);

463

[ 465](structnet__stats__eth__errors.md#a257113639f0e0e3085febb7a147f498f) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [corr\_ecc\_errors](structnet__stats__eth__errors.md#a257113639f0e0e3085febb7a147f498f);

466};

467

[ 471](structnet__stats__eth__flow.md)struct [net\_stats\_eth\_flow](structnet__stats__eth__flow.md) {

[ 473](structnet__stats__eth__flow.md#a08e5da4ff78fe3893b9c9a628cefe4f2) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [rx\_flow\_control\_xon](structnet__stats__eth__flow.md#a08e5da4ff78fe3893b9c9a628cefe4f2);

474

[ 476](structnet__stats__eth__flow.md#a8f9b93537b3c11be70f276aaa72cb637) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [rx\_flow\_control\_xoff](structnet__stats__eth__flow.md#a8f9b93537b3c11be70f276aaa72cb637);

477

[ 479](structnet__stats__eth__flow.md#a31412e8bf9d38ba630ea856e958a48d7) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [tx\_flow\_control\_xon](structnet__stats__eth__flow.md#a31412e8bf9d38ba630ea856e958a48d7);

480

[ 482](structnet__stats__eth__flow.md#a969d81f9db20312d2d2aa7f70f93bdd5) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [tx\_flow\_control\_xoff](structnet__stats__eth__flow.md#a969d81f9db20312d2d2aa7f70f93bdd5);

483};

484

[ 488](structnet__stats__eth__csum.md)struct [net\_stats\_eth\_csum](structnet__stats__eth__csum.md) {

[ 490](structnet__stats__eth__csum.md#a1f1ba5c01c6232cd739d069ddb871b17) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [rx\_csum\_offload\_good](structnet__stats__eth__csum.md#a1f1ba5c01c6232cd739d069ddb871b17);

491

[ 493](structnet__stats__eth__csum.md#ac4fc04d66193070d4f52a4c07f29ccce) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [rx\_csum\_offload\_errors](structnet__stats__eth__csum.md#ac4fc04d66193070d4f52a4c07f29ccce);

494};

495

[ 499](structnet__stats__eth__hw__timestamp.md)struct [net\_stats\_eth\_hw\_timestamp](structnet__stats__eth__hw__timestamp.md) {

[ 501](structnet__stats__eth__hw__timestamp.md#acd3d5f72d7df568110d96093e0c9534d) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [rx\_hwtstamp\_cleared](structnet__stats__eth__hw__timestamp.md#acd3d5f72d7df568110d96093e0c9534d);

502

[ 504](structnet__stats__eth__hw__timestamp.md#a41f605499dbf88a879522fdfa4633d9e) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [tx\_hwtstamp\_timeouts](structnet__stats__eth__hw__timestamp.md#a41f605499dbf88a879522fdfa4633d9e);

505

[ 507](structnet__stats__eth__hw__timestamp.md#ae1f983faf4a999308c464e4af5a5284b) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [tx\_hwtstamp\_skipped](structnet__stats__eth__hw__timestamp.md#ae1f983faf4a999308c464e4af5a5284b);

508};

509

510#ifdef CONFIG\_NET\_STATISTICS\_ETHERNET\_VENDOR

514struct net\_stats\_eth\_vendor {

515 const char \* const key;

516 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) value;

517};

518#endif

519

[ 523](structnet__stats__eth.md)struct [net\_stats\_eth](structnet__stats__eth.md) {

[ 525](structnet__stats__eth.md#a8c5cf1ead8ba214425a16fed1c2ad0fb) struct [net\_stats\_bytes](structnet__stats__bytes.md) [bytes](structnet__stats__eth.md#a8c5cf1ead8ba214425a16fed1c2ad0fb);

526

[ 528](structnet__stats__eth.md#a97bd6026b16890743f344751a21107f1) struct [net\_stats\_pkts](structnet__stats__pkts.md) [pkts](structnet__stats__eth.md#a97bd6026b16890743f344751a21107f1);

529

[ 531](structnet__stats__eth.md#a054beb909134b0e0f22f5df599549128) struct [net\_stats\_pkts](structnet__stats__pkts.md) [broadcast](structnet__stats__eth.md#a054beb909134b0e0f22f5df599549128);

532

[ 534](structnet__stats__eth.md#a4f6a2903330518a132e7e547820e0bf2) struct [net\_stats\_pkts](structnet__stats__pkts.md) [multicast](structnet__stats__eth.md#a4f6a2903330518a132e7e547820e0bf2);

535

[ 537](structnet__stats__eth.md#a9c869740f416fbe0b54d7fefacb1fe29) struct [net\_stats\_pkts](structnet__stats__pkts.md) [errors](structnet__stats__eth.md#a9c869740f416fbe0b54d7fefacb1fe29);

538

[ 540](structnet__stats__eth.md#a922feddb17fc020371f1bcc52c709415) struct [net\_stats\_eth\_errors](structnet__stats__eth__errors.md) [error\_details](structnet__stats__eth.md#a922feddb17fc020371f1bcc52c709415);

541

[ 543](structnet__stats__eth.md#a643010ac6360c8c0c08016725ba12222) struct [net\_stats\_eth\_flow](structnet__stats__eth__flow.md) [flow\_control](structnet__stats__eth.md#a643010ac6360c8c0c08016725ba12222);

544

[ 546](structnet__stats__eth.md#a2169ae06bace1a93663bccf88c8d7a29) struct [net\_stats\_eth\_csum](structnet__stats__eth__csum.md) [csum](structnet__stats__eth.md#a2169ae06bace1a93663bccf88c8d7a29);

547

[ 549](structnet__stats__eth.md#a44667efff73c17c089ed22d5b0da5ad3) struct [net\_stats\_eth\_hw\_timestamp](structnet__stats__eth__hw__timestamp.md) [hw\_timestamp](structnet__stats__eth.md#a44667efff73c17c089ed22d5b0da5ad3);

550

[ 552](structnet__stats__eth.md#a822d4205791f59999c842610522f6fc5) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [collisions](structnet__stats__eth.md#a822d4205791f59999c842610522f6fc5);

553

[ 555](structnet__stats__eth.md#a257c349cf3d32d38796e3899e702454a) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [tx\_dropped](structnet__stats__eth.md#a257c349cf3d32d38796e3899e702454a);

556

[ 558](structnet__stats__eth.md#ab351258ae82abd09759d37774559d8bc) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [tx\_timeout\_count](structnet__stats__eth.md#ab351258ae82abd09759d37774559d8bc);

559

[ 561](structnet__stats__eth.md#a6699012226e25e8bad39076fed6dbfb5) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [tx\_restart\_queue](structnet__stats__eth.md#a6699012226e25e8bad39076fed6dbfb5);

562

[ 564](structnet__stats__eth.md#afaacee7cc1d0a35ae2344175421c40dd) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [unknown\_protocol](structnet__stats__eth.md#afaacee7cc1d0a35ae2344175421c40dd);

565

566#ifdef CONFIG\_NET\_STATISTICS\_ETHERNET\_VENDOR

568 struct net\_stats\_eth\_vendor \*vendor;

569#endif

570};

571

[ 575](structnet__stats__ppp.md)struct [net\_stats\_ppp](structnet__stats__ppp.md) {

[ 577](structnet__stats__ppp.md#ab2b48da7f19d4b83e3f41b41979b7ed8) struct [net\_stats\_bytes](structnet__stats__bytes.md) [bytes](structnet__stats__ppp.md#ab2b48da7f19d4b83e3f41b41979b7ed8);

578

[ 580](structnet__stats__ppp.md#a71fc81f3c5f3e65a476b3391f086d340) struct [net\_stats\_pkts](structnet__stats__pkts.md) [pkts](structnet__stats__ppp.md#a71fc81f3c5f3e65a476b3391f086d340);

581

[ 583](structnet__stats__ppp.md#ae2e0a47a539e9d7bc97f9c63f889b276) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [drop](structnet__stats__ppp.md#ae2e0a47a539e9d7bc97f9c63f889b276);

584

[ 586](structnet__stats__ppp.md#a1332b31980f82236aeb0c3f9444e2ac6) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [chkerr](structnet__stats__ppp.md#a1332b31980f82236aeb0c3f9444e2ac6);

587};

588

[ 592](structnet__stats__sta__mgmt.md)struct [net\_stats\_sta\_mgmt](structnet__stats__sta__mgmt.md) {

[ 594](structnet__stats__sta__mgmt.md#ac6e68fded8e19b20259442436923f815) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [beacons\_rx](structnet__stats__sta__mgmt.md#ac6e68fded8e19b20259442436923f815);

595

[ 597](structnet__stats__sta__mgmt.md#a29ae0079b4c780e0de2656a85ec15fe9) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [beacons\_miss](structnet__stats__sta__mgmt.md#a29ae0079b4c780e0de2656a85ec15fe9);

598};

599

[ 603](structnet__stats__wifi.md)struct [net\_stats\_wifi](structnet__stats__wifi.md) {

[ 605](structnet__stats__wifi.md#a8bee22961545674e6ab100b58a04bf91) struct [net\_stats\_sta\_mgmt](structnet__stats__sta__mgmt.md) [sta\_mgmt](structnet__stats__wifi.md#a8bee22961545674e6ab100b58a04bf91);

606

[ 608](structnet__stats__wifi.md#aa055b1e8bd8f1e50815c1028b562be07) struct [net\_stats\_bytes](structnet__stats__bytes.md) [bytes](structnet__stats__wifi.md#aa055b1e8bd8f1e50815c1028b562be07);

609

[ 611](structnet__stats__wifi.md#adbcdb2dd8733f2917c00a0b2d365393b) struct [net\_stats\_pkts](structnet__stats__pkts.md) [pkts](structnet__stats__wifi.md#adbcdb2dd8733f2917c00a0b2d365393b);

612

[ 614](structnet__stats__wifi.md#a03dc04638c4b670bd7f3520d45fc1eda) struct [net\_stats\_pkts](structnet__stats__pkts.md) [broadcast](structnet__stats__wifi.md#a03dc04638c4b670bd7f3520d45fc1eda);

615

[ 617](structnet__stats__wifi.md#a7e7f68215101885fd51c70e981da26e7) struct [net\_stats\_pkts](structnet__stats__pkts.md) [multicast](structnet__stats__wifi.md#a7e7f68215101885fd51c70e981da26e7);

618

[ 620](structnet__stats__wifi.md#ae0149e64a94a9f96eb6680f94793c8c4) struct [net\_stats\_pkts](structnet__stats__pkts.md) [errors](structnet__stats__wifi.md#ae0149e64a94a9f96eb6680f94793c8c4);

621

[ 623](structnet__stats__wifi.md#ae80dcd73a3c5ce3ec3282d1ae827b338) struct [net\_stats\_pkts](structnet__stats__pkts.md) [unicast](structnet__stats__wifi.md#ae80dcd73a3c5ce3ec3282d1ae827b338);

624};

625

626#if defined(CONFIG\_NET\_STATISTICS\_USER\_API)

627/\* Management part definitions \*/

628

630

631#define \_NET\_STATS\_LAYER NET\_MGMT\_LAYER\_L3

632#define \_NET\_STATS\_CODE 0x101

633#define \_NET\_STATS\_BASE (NET\_MGMT\_LAYER(\_NET\_STATS\_LAYER) | \

634 NET\_MGMT\_LAYER\_CODE(\_NET\_STATS\_CODE))

635

636enum net\_request\_stats\_cmd {

637 NET\_REQUEST\_STATS\_CMD\_GET\_ALL = 1,

638 NET\_REQUEST\_STATS\_CMD\_GET\_PROCESSING\_ERROR,

639 NET\_REQUEST\_STATS\_CMD\_GET\_BYTES,

640 NET\_REQUEST\_STATS\_CMD\_GET\_IP\_ERRORS,

641 NET\_REQUEST\_STATS\_CMD\_GET\_IPV4,

642 NET\_REQUEST\_STATS\_CMD\_GET\_IPV6,

643 NET\_REQUEST\_STATS\_CMD\_GET\_IPV6\_ND,

644 NET\_REQUEST\_STATS\_CMD\_GET\_ICMP,

645 NET\_REQUEST\_STATS\_CMD\_GET\_UDP,

646 NET\_REQUEST\_STATS\_CMD\_GET\_TCP,

647 NET\_REQUEST\_STATS\_CMD\_GET\_ETHERNET,

648 NET\_REQUEST\_STATS\_CMD\_GET\_PPP,

649 NET\_REQUEST\_STATS\_CMD\_GET\_PM,

650 NET\_REQUEST\_STATS\_CMD\_GET\_WIFI,

651};

652

654

656#define NET\_REQUEST\_STATS\_GET\_ALL \

657 (\_NET\_STATS\_BASE | NET\_REQUEST\_STATS\_CMD\_GET\_ALL)

658

660#define NET\_REQUEST\_STATS\_GET\_PROCESSING\_ERROR \

661 (\_NET\_STATS\_BASE | NET\_REQUEST\_STATS\_CMD\_GET\_PROCESSING\_ERROR)

662

664#define NET\_REQUEST\_STATS\_GET\_BYTES \

665 (\_NET\_STATS\_BASE | NET\_REQUEST\_STATS\_CMD\_GET\_BYTES)

666

668#define NET\_REQUEST\_STATS\_GET\_IP\_ERRORS \

669 (\_NET\_STATS\_BASE | NET\_REQUEST\_STATS\_CMD\_GET\_IP\_ERRORS)

670

672

673[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_STATS\_GET\_ALL);

674[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_STATS\_GET\_PROCESSING\_ERROR);

675[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_STATS\_GET\_BYTES);

676[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_STATS\_GET\_IP\_ERRORS);

677

679

680#if defined(CONFIG\_NET\_STATISTICS\_IPV4)

682#define NET\_REQUEST\_STATS\_GET\_IPV4 \

683 (\_NET\_STATS\_BASE | NET\_REQUEST\_STATS\_CMD\_GET\_IPV4)

684

686[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_STATS\_GET\_IPV4);

688#endif /\* CONFIG\_NET\_STATISTICS\_IPV4 \*/

689

690#if defined(CONFIG\_NET\_STATISTICS\_IPV6)

692#define NET\_REQUEST\_STATS\_GET\_IPV6 \

693 (\_NET\_STATS\_BASE | NET\_REQUEST\_STATS\_CMD\_GET\_IPV6)

694

696[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_STATS\_GET\_IPV6);

698#endif /\* CONFIG\_NET\_STATISTICS\_IPV6 \*/

699

700#if defined(CONFIG\_NET\_STATISTICS\_IPV6\_ND)

702#define NET\_REQUEST\_STATS\_GET\_IPV6\_ND \

703 (\_NET\_STATS\_BASE | NET\_REQUEST\_STATS\_CMD\_GET\_IPV6\_ND)

704

706[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_STATS\_GET\_IPV6\_ND);

708#endif /\* CONFIG\_NET\_STATISTICS\_IPV6\_ND \*/

709

710#if defined(CONFIG\_NET\_STATISTICS\_ICMP)

712#define NET\_REQUEST\_STATS\_GET\_ICMP \

713 (\_NET\_STATS\_BASE | NET\_REQUEST\_STATS\_CMD\_GET\_ICMP)

714

716[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_STATS\_GET\_ICMP);

718#endif /\* CONFIG\_NET\_STATISTICS\_ICMP \*/

719

720#if defined(CONFIG\_NET\_STATISTICS\_UDP)

722#define NET\_REQUEST\_STATS\_GET\_UDP \

723 (\_NET\_STATS\_BASE | NET\_REQUEST\_STATS\_CMD\_GET\_UDP)

724

726[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_STATS\_GET\_UDP);

728#endif /\* CONFIG\_NET\_STATISTICS\_UDP \*/

729

730#if defined(CONFIG\_NET\_STATISTICS\_TCP)

732#define NET\_REQUEST\_STATS\_GET\_TCP \

733 (\_NET\_STATS\_BASE | NET\_REQUEST\_STATS\_CMD\_GET\_TCP)

734

736[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_STATS\_GET\_TCP);

738#endif /\* CONFIG\_NET\_STATISTICS\_TCP \*/

739

740#if defined(CONFIG\_NET\_STATISTICS\_ETHERNET)

742#define NET\_REQUEST\_STATS\_GET\_ETHERNET \

743 (\_NET\_STATS\_BASE | NET\_REQUEST\_STATS\_CMD\_GET\_ETHERNET)

744

746[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_STATS\_GET\_ETHERNET);

748#endif /\* CONFIG\_NET\_STATISTICS\_ETHERNET \*/

749

750#if defined(CONFIG\_NET\_STATISTICS\_PPP)

752#define NET\_REQUEST\_STATS\_GET\_PPP \

753 (\_NET\_STATS\_BASE | NET\_REQUEST\_STATS\_CMD\_GET\_PPP)

754

756[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_STATS\_GET\_PPP);

758#endif /\* CONFIG\_NET\_STATISTICS\_PPP \*/

759

760#endif /\* CONFIG\_NET\_STATISTICS\_USER\_API \*/

761

762#if defined(CONFIG\_NET\_STATISTICS\_POWER\_MANAGEMENT)

764#define NET\_REQUEST\_STATS\_GET\_PM \

765 (\_NET\_STATS\_BASE | NET\_REQUEST\_STATS\_CMD\_GET\_PM)

766

768[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_STATS\_GET\_PM);

770#endif /\* CONFIG\_NET\_STATISTICS\_POWER\_MANAGEMENT \*/

771

772#if defined(CONFIG\_NET\_STATISTICS\_WIFI)

774#define NET\_REQUEST\_STATS\_GET\_WIFI \

775 (\_NET\_STATS\_BASE | NET\_REQUEST\_STATS\_CMD\_GET\_WIFI)

776

778[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_STATS\_GET\_WIFI);

780#endif /\* CONFIG\_NET\_STATISTICS\_WIFI \*/

781

785

786#ifdef \_\_cplusplus

787}

788#endif

789

790#endif /\* ZEPHYR\_INCLUDE\_NET\_NET\_STATS\_H\_ \*/

[recv](group__bsd__sockets.md#gae11da452beee536eac85d5f26e5cdd40)

static ssize\_t recv(int sock, void \*buf, size\_t max\_len, int flags)

POSIX wrapper for zsock\_recv.

**Definition** socket.h:922

[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)

#define NET\_MGMT\_DEFINE\_REQUEST\_HANDLER(\_mgmt\_request)

Declare a request handler function for the given network event.

**Definition** net\_mgmt.h:109

[net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752)

uint32\_t net\_stats\_t

Network statistics counter.

**Definition** net\_stats.h:36

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

**Definition** net\_stats.h:488

[net\_stats\_eth\_csum::rx\_csum\_offload\_good](structnet__stats__eth__csum.md#a1f1ba5c01c6232cd739d069ddb871b17)

net\_stats\_t rx\_csum\_offload\_good

Number of good RX checksum offloading.

**Definition** net\_stats.h:490

[net\_stats\_eth\_csum::rx\_csum\_offload\_errors](structnet__stats__eth__csum.md#ac4fc04d66193070d4f52a4c07f29ccce)

net\_stats\_t rx\_csum\_offload\_errors

Number of failed RX checksum offloading.

**Definition** net\_stats.h:493

[net\_stats\_eth\_errors](structnet__stats__eth__errors.md)

Ethernet error statistics.

**Definition** net\_stats.h:409

[net\_stats\_eth\_errors::tx\_carrier\_errors](structnet__stats__eth__errors.md#a0043d1a1481040a6d7439bd23423ec12)

net\_stats\_t tx\_carrier\_errors

Number of TX carrier errors.

**Definition** net\_stats.h:447

[net\_stats\_eth\_errors::uncorr\_ecc\_errors](structnet__stats__eth__errors.md#a07d0a435f2129556520c732571d28edf)

net\_stats\_t uncorr\_ecc\_errors

Number of uncorrected ECC errors.

**Definition** net\_stats.h:462

[net\_stats\_eth\_errors::rx\_long\_length\_errors](structnet__stats__eth__errors.md#a0e83e270a35222ed3e927800be4159e7)

net\_stats\_t rx\_long\_length\_errors

Number of RX long length errors.

**Definition** net\_stats.h:429

[net\_stats\_eth\_errors::tx\_window\_errors](structnet__stats__eth__errors.md#a17624a12d6473bdd78698076fed0d122)

net\_stats\_t tx\_window\_errors

Number of TX window errors.

**Definition** net\_stats.h:456

[net\_stats\_eth\_errors::corr\_ecc\_errors](structnet__stats__eth__errors.md#a257113639f0e0e3085febb7a147f498f)

net\_stats\_t corr\_ecc\_errors

Number of corrected ECC errors.

**Definition** net\_stats.h:465

[net\_stats\_eth\_errors::rx\_missed\_errors](structnet__stats__eth__errors.md#a2d2b2c4e3764ebec841f1ecbe7058d99)

net\_stats\_t rx\_missed\_errors

Number of RX missed errors.

**Definition** net\_stats.h:426

[net\_stats\_eth\_errors::rx\_crc\_errors](structnet__stats__eth__errors.md#a4dab70cf219269bb393ce14faf0ed77e)

net\_stats\_t rx\_crc\_errors

Number of RX CRC errors.

**Definition** net\_stats.h:417

[net\_stats\_eth\_errors::rx\_short\_length\_errors](structnet__stats__eth__errors.md#a5e3d39d8417bb180cbfcb8c901006e81)

net\_stats\_t rx\_short\_length\_errors

Number of RX short length errors.

**Definition** net\_stats.h:432

[net\_stats\_eth\_errors::rx\_align\_errors](structnet__stats__eth__errors.md#a7618f10af3443c49a6e256bb41e77781)

net\_stats\_t rx\_align\_errors

Number of RX buffer align errors.

**Definition** net\_stats.h:435

[net\_stats\_eth\_errors::rx\_dma\_failed](structnet__stats__eth__errors.md#a7bcfbb13836f162ceeb5f021304b5c76)

net\_stats\_t rx\_dma\_failed

Number of RX DMA failed errors.

**Definition** net\_stats.h:438

[net\_stats\_eth\_errors::rx\_no\_buffer\_count](structnet__stats__eth__errors.md#a82622736d226b4d3b999f1f22ccf8529)

net\_stats\_t rx\_no\_buffer\_count

Number of RX net\_pkt allocation errors.

**Definition** net\_stats.h:423

[net\_stats\_eth\_errors::tx\_fifo\_errors](structnet__stats__eth__errors.md#a84630da9b82557f56dc35cd59ca2f7ae)

net\_stats\_t tx\_fifo\_errors

Number of TX FIFO errors.

**Definition** net\_stats.h:450

[net\_stats\_eth\_errors::rx\_frame\_errors](structnet__stats__eth__errors.md#a8dfcc5cd1b4decec5783d01ba7033b05)

net\_stats\_t rx\_frame\_errors

Number of RX frame errors.

**Definition** net\_stats.h:420

[net\_stats\_eth\_errors::rx\_over\_errors](structnet__stats__eth__errors.md#a9afee89f5bb01907e7cd515e2a0ff1b5)

net\_stats\_t rx\_over\_errors

Number of RX overrun errors.

**Definition** net\_stats.h:414

[net\_stats\_eth\_errors::tx\_dma\_failed](structnet__stats__eth__errors.md#abfbf6478b7afdd5935d7c6948c9ef426)

net\_stats\_t tx\_dma\_failed

Number of TX DMA failed errors.

**Definition** net\_stats.h:459

[net\_stats\_eth\_errors::rx\_length\_errors](structnet__stats__eth__errors.md#aca0e2e4807fa70279dee8ddaad2d7ef7)

net\_stats\_t rx\_length\_errors

Number of RX length errors.

**Definition** net\_stats.h:411

[net\_stats\_eth\_errors::rx\_buf\_alloc\_failed](structnet__stats__eth__errors.md#adbcae9c10c081f1cdf304bcdce740aa4)

net\_stats\_t rx\_buf\_alloc\_failed

Number of RX net\_buf allocation errors.

**Definition** net\_stats.h:441

[net\_stats\_eth\_errors::tx\_heartbeat\_errors](structnet__stats__eth__errors.md#ae2a13733c1a5f0cc3e00efca0c3f429d)

net\_stats\_t tx\_heartbeat\_errors

Number of TX heartbeat errors.

**Definition** net\_stats.h:453

[net\_stats\_eth\_errors::tx\_aborted\_errors](structnet__stats__eth__errors.md#afec6a7e24c6f3cc74dd9f739f27b3e48)

net\_stats\_t tx\_aborted\_errors

Number of TX aborted errors.

**Definition** net\_stats.h:444

[net\_stats\_eth\_flow](structnet__stats__eth__flow.md)

Ethernet flow control statistics.

**Definition** net\_stats.h:471

[net\_stats\_eth\_flow::rx\_flow\_control\_xon](structnet__stats__eth__flow.md#a08e5da4ff78fe3893b9c9a628cefe4f2)

net\_stats\_t rx\_flow\_control\_xon

Number of RX XON flow control.

**Definition** net\_stats.h:473

[net\_stats\_eth\_flow::tx\_flow\_control\_xon](structnet__stats__eth__flow.md#a31412e8bf9d38ba630ea856e958a48d7)

net\_stats\_t tx\_flow\_control\_xon

Number of TX XON flow control.

**Definition** net\_stats.h:479

[net\_stats\_eth\_flow::rx\_flow\_control\_xoff](structnet__stats__eth__flow.md#a8f9b93537b3c11be70f276aaa72cb637)

net\_stats\_t rx\_flow\_control\_xoff

Number of RX XOFF flow control.

**Definition** net\_stats.h:476

[net\_stats\_eth\_flow::tx\_flow\_control\_xoff](structnet__stats__eth__flow.md#a969d81f9db20312d2d2aa7f70f93bdd5)

net\_stats\_t tx\_flow\_control\_xoff

Number of TX XOFF flow control.

**Definition** net\_stats.h:482

[net\_stats\_eth\_hw\_timestamp](structnet__stats__eth__hw__timestamp.md)

Ethernet hardware timestamp statistics.

**Definition** net\_stats.h:499

[net\_stats\_eth\_hw\_timestamp::tx\_hwtstamp\_timeouts](structnet__stats__eth__hw__timestamp.md#a41f605499dbf88a879522fdfa4633d9e)

net\_stats\_t tx\_hwtstamp\_timeouts

Number of RX hardware timestamp timeout.

**Definition** net\_stats.h:504

[net\_stats\_eth\_hw\_timestamp::rx\_hwtstamp\_cleared](structnet__stats__eth__hw__timestamp.md#acd3d5f72d7df568110d96093e0c9534d)

net\_stats\_t rx\_hwtstamp\_cleared

Number of RX hardware timestamp cleared.

**Definition** net\_stats.h:501

[net\_stats\_eth\_hw\_timestamp::tx\_hwtstamp\_skipped](structnet__stats__eth__hw__timestamp.md#ae1f983faf4a999308c464e4af5a5284b)

net\_stats\_t tx\_hwtstamp\_skipped

Number of RX hardware timestamp skipped.

**Definition** net\_stats.h:507

[net\_stats\_eth](structnet__stats__eth.md)

All Ethernet specific statistics.

**Definition** net\_stats.h:523

[net\_stats\_eth::broadcast](structnet__stats__eth.md#a054beb909134b0e0f22f5df599549128)

struct net\_stats\_pkts broadcast

Total number of broadcast packets received and sent.

**Definition** net\_stats.h:531

[net\_stats\_eth::csum](structnet__stats__eth.md#a2169ae06bace1a93663bccf88c8d7a29)

struct net\_stats\_eth\_csum csum

Total number of checksum errors in RX and TX.

**Definition** net\_stats.h:546

[net\_stats\_eth::tx\_dropped](structnet__stats__eth.md#a257c349cf3d32d38796e3899e702454a)

net\_stats\_t tx\_dropped

Total number of dropped TX packets.

**Definition** net\_stats.h:555

[net\_stats\_eth::hw\_timestamp](structnet__stats__eth.md#a44667efff73c17c089ed22d5b0da5ad3)

struct net\_stats\_eth\_hw\_timestamp hw\_timestamp

Total number of hardware timestamp errors in RX and TX.

**Definition** net\_stats.h:549

[net\_stats\_eth::multicast](structnet__stats__eth.md#a4f6a2903330518a132e7e547820e0bf2)

struct net\_stats\_pkts multicast

Total number of multicast packets received and sent.

**Definition** net\_stats.h:534

[net\_stats\_eth::flow\_control](structnet__stats__eth.md#a643010ac6360c8c0c08016725ba12222)

struct net\_stats\_eth\_flow flow\_control

Total number of flow control errors in RX and TX.

**Definition** net\_stats.h:543

[net\_stats\_eth::tx\_restart\_queue](structnet__stats__eth.md#a6699012226e25e8bad39076fed6dbfb5)

net\_stats\_t tx\_restart\_queue

Total number of TX queue restarts.

**Definition** net\_stats.h:561

[net\_stats\_eth::collisions](structnet__stats__eth.md#a822d4205791f59999c842610522f6fc5)

net\_stats\_t collisions

Total number of collisions.

**Definition** net\_stats.h:552

[net\_stats\_eth::bytes](structnet__stats__eth.md#a8c5cf1ead8ba214425a16fed1c2ad0fb)

struct net\_stats\_bytes bytes

Total number of bytes received and sent.

**Definition** net\_stats.h:525

[net\_stats\_eth::error\_details](structnet__stats__eth.md#a922feddb17fc020371f1bcc52c709415)

struct net\_stats\_eth\_errors error\_details

Total number of errors in RX and TX.

**Definition** net\_stats.h:540

[net\_stats\_eth::pkts](structnet__stats__eth.md#a97bd6026b16890743f344751a21107f1)

struct net\_stats\_pkts pkts

Total number of packets received and sent.

**Definition** net\_stats.h:528

[net\_stats\_eth::errors](structnet__stats__eth.md#a9c869740f416fbe0b54d7fefacb1fe29)

struct net\_stats\_pkts errors

Total number of errors in RX and TX.

**Definition** net\_stats.h:537

[net\_stats\_eth::tx\_timeout\_count](structnet__stats__eth.md#ab351258ae82abd09759d37774559d8bc)

net\_stats\_t tx\_timeout\_count

Total number of TX timeout errors.

**Definition** net\_stats.h:558

[net\_stats\_eth::unknown\_protocol](structnet__stats__eth.md#afaacee7cc1d0a35ae2344175421c40dd)

net\_stats\_t unknown\_protocol

Total number of RX unknown protocol packets.

**Definition** net\_stats.h:564

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

**Definition** net\_stats.h:216

[net\_stats\_ipv4\_igmp::drop](structnet__stats__ipv4__igmp.md#a1c37702ff837b8c5cc9df5f690e7678c)

net\_stats\_t drop

Number of dropped IPv4 IGMP packets.

**Definition** net\_stats.h:224

[net\_stats\_ipv4\_igmp::recv](structnet__stats__ipv4__igmp.md#a469113de7af0ba42dbd1b0365d00602c)

net\_stats\_t recv

Number of received IPv4 IGMP queries.

**Definition** net\_stats.h:218

[net\_stats\_ipv4\_igmp::sent](structnet__stats__ipv4__igmp.md#a955e20a6ee5e19e08000b3114b9d71a6)

net\_stats\_t sent

Number of sent IPv4 IGMP reports.

**Definition** net\_stats.h:221

[net\_stats\_ipv6\_mld](structnet__stats__ipv6__mld.md)

IPv6 multicast listener daemon statistics.

**Definition** net\_stats.h:202

[net\_stats\_ipv6\_mld::recv](structnet__stats__ipv6__mld.md#a4879ff9e31f8b60973d3b169598e921d)

net\_stats\_t recv

Number of received IPv6 MLD queries.

**Definition** net\_stats.h:204

[net\_stats\_ipv6\_mld::sent](structnet__stats__ipv6__mld.md#ab397b74b14ce7047bf2fc63ca72ce1e5)

net\_stats\_t sent

Number of sent IPv6 MLD reports.

**Definition** net\_stats.h:207

[net\_stats\_ipv6\_mld::drop](structnet__stats__ipv6__mld.md#ad85dc87f57296a1e7d64e959b0370ee8)

net\_stats\_t drop

Number of dropped IPv6 MLD packets.

**Definition** net\_stats.h:210

[net\_stats\_ipv6\_nd](structnet__stats__ipv6__nd.md)

IPv6 neighbor discovery statistics.

**Definition** net\_stats.h:188

[net\_stats\_ipv6\_nd::sent](structnet__stats__ipv6__nd.md#a0129f7892a4439c20deb2f32b9001277)

net\_stats\_t sent

Number of sent IPv6 neighbor discovery packets.

**Definition** net\_stats.h:196

[net\_stats\_ipv6\_nd::recv](structnet__stats__ipv6__nd.md#a0bf6f67d9112996a3b002ea160aec769)

net\_stats\_t recv

Number of received IPv6 neighbor discovery packets.

**Definition** net\_stats.h:193

[net\_stats\_ipv6\_nd::drop](structnet__stats__ipv6__nd.md#a31074d5d44138fcabdc5f7750f9f2c47)

net\_stats\_t drop

Number of dropped IPv6 neighbor discovery packets.

**Definition** net\_stats.h:190

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

**Definition** net\_stats.h:308

[net\_stats\_pm::last\_suspend\_time](structnet__stats__pm.md#a0bdf9c3676298e2df4ff3bfa03f5e823)

uint32\_t last\_suspend\_time

How long the last suspend took.

**Definition** net\_stats.h:314

[net\_stats\_pm::start\_time](structnet__stats__pm.md#a6784806eaa093431ed3c0f7acfe5a89c)

uint32\_t start\_time

Network interface last suspend start time.

**Definition** net\_stats.h:316

[net\_stats\_pm::overall\_suspend\_time](structnet__stats__pm.md#ab43935fcfe9efc1cd5f3e7e329996805)

uint64\_t overall\_suspend\_time

Total suspend time.

**Definition** net\_stats.h:310

[net\_stats\_pm::suspend\_count](structnet__stats__pm.md#ac14122a4765c499c045f18c70af355a0)

net\_stats\_t suspend\_count

How many times we were suspended.

**Definition** net\_stats.h:312

[net\_stats\_ppp](structnet__stats__ppp.md)

All PPP specific statistics.

**Definition** net\_stats.h:575

[net\_stats\_ppp::chkerr](structnet__stats__ppp.md#a1332b31980f82236aeb0c3f9444e2ac6)

net\_stats\_t chkerr

Number of received PPP frames with a bad checksum.

**Definition** net\_stats.h:586

[net\_stats\_ppp::pkts](structnet__stats__ppp.md#a71fc81f3c5f3e65a476b3391f086d340)

struct net\_stats\_pkts pkts

Total number of packets received and sent.

**Definition** net\_stats.h:580

[net\_stats\_ppp::bytes](structnet__stats__ppp.md#ab2b48da7f19d4b83e3f41b41979b7ed8)

struct net\_stats\_bytes bytes

Total number of bytes received and sent.

**Definition** net\_stats.h:577

[net\_stats\_ppp::drop](structnet__stats__ppp.md#ae2e0a47a539e9d7bc97f9c63f889b276)

net\_stats\_t drop

Number of received and dropped PPP frames.

**Definition** net\_stats.h:583

[net\_stats\_rx\_time](structnet__stats__rx__time.md)

Network packet receive times for calculating average RX time.

**Definition** net\_stats.h:241

[net\_stats\_rx\_time::sum](structnet__stats__rx__time.md#a4b84c2ae2fda8fcd75fdf1bf0b2aae8d)

uint64\_t sum

Sum of network packet receive times.

**Definition** net\_stats.h:243

[net\_stats\_rx\_time::count](structnet__stats__rx__time.md#a68247051b064de081fa2e84118192958)

net\_stats\_t count

Number of network packets received.

**Definition** net\_stats.h:246

[net\_stats\_sta\_mgmt](structnet__stats__sta__mgmt.md)

All Wi-Fi management statistics.

**Definition** net\_stats.h:592

[net\_stats\_sta\_mgmt::beacons\_miss](structnet__stats__sta__mgmt.md#a29ae0079b4c780e0de2656a85ec15fe9)

net\_stats\_t beacons\_miss

Number of missed beacons.

**Definition** net\_stats.h:597

[net\_stats\_sta\_mgmt::beacons\_rx](structnet__stats__sta__mgmt.md#ac6e68fded8e19b20259442436923f815)

net\_stats\_t beacons\_rx

Number of received beacons.

**Definition** net\_stats.h:594

[net\_stats\_tc](structnet__stats__tc.md)

Traffic class statistics.

**Definition** net\_stats.h:268

[net\_stats\_tc::bytes](structnet__stats__tc.md#a192a7ec0d24bce9e62f766e481ee5709)

net\_stats\_t bytes

Number of bytes sent for this traffic class.

**Definition** net\_stats.h:281

[net\_stats\_tc::tx\_time](structnet__stats__tc.md#a30288ef3bb0796cd18c3cf0aedbe875a)

struct net\_stats\_tx\_time tx\_time

Helper for calculating average TX time statistics.

**Definition** net\_stats.h:272

[net\_stats\_tc::pkts](structnet__stats__tc.md#a6614b5f5186635415a7d787260c39248)

net\_stats\_t pkts

Number of packets sent for this traffic class.

**Definition** net\_stats.h:279

[net\_stats\_tc::priority](structnet__stats__tc.md#a8a5c2e59990407ddbfc7973a1c183bf6)

uint8\_t priority

Priority of this traffic class.

**Definition** net\_stats.h:283

[net\_stats\_tc::sent](structnet__stats__tc.md#a8d6a3ebcc49ce8c34a5faae986f648e2)

struct net\_stats\_tc::@074155214116325077102236356156227241054306002026 sent[NET\_TC\_TX\_STATS\_COUNT]

TX statistics for each traffic class.

[net\_stats\_tc::rx\_time](structnet__stats__tc.md#a8ea00824bb0fb18e4d8912343e01c3b7)

struct net\_stats\_rx\_time rx\_time

Helper for calculating average RX time statistics.

**Definition** net\_stats.h:289

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

**Definition** net\_stats.h:230

[net\_stats\_tx\_time::count](structnet__stats__tx__time.md#a7a652350ed04e53ba02aec294f8444b4)

net\_stats\_t count

Number of network packets transferred.

**Definition** net\_stats.h:235

[net\_stats\_tx\_time::sum](structnet__stats__tx__time.md#af6f7a26c0344a0f93306e105a8917c3e)

uint64\_t sum

Sum of network packet transfer times.

**Definition** net\_stats.h:232

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

**Definition** net\_stats.h:603

[net\_stats\_wifi::broadcast](structnet__stats__wifi.md#a03dc04638c4b670bd7f3520d45fc1eda)

struct net\_stats\_pkts broadcast

Total number of broadcast packets received and sent.

**Definition** net\_stats.h:614

[net\_stats\_wifi::multicast](structnet__stats__wifi.md#a7e7f68215101885fd51c70e981da26e7)

struct net\_stats\_pkts multicast

Total number of multicast packets received and sent.

**Definition** net\_stats.h:617

[net\_stats\_wifi::sta\_mgmt](structnet__stats__wifi.md#a8bee22961545674e6ab100b58a04bf91)

struct net\_stats\_sta\_mgmt sta\_mgmt

Total number of beacon errors.

**Definition** net\_stats.h:605

[net\_stats\_wifi::bytes](structnet__stats__wifi.md#aa055b1e8bd8f1e50815c1028b562be07)

struct net\_stats\_bytes bytes

Total number of bytes received and sent.

**Definition** net\_stats.h:608

[net\_stats\_wifi::pkts](structnet__stats__wifi.md#adbcdb2dd8733f2917c00a0b2d365393b)

struct net\_stats\_pkts pkts

Total number of packets received and sent.

**Definition** net\_stats.h:611

[net\_stats\_wifi::errors](structnet__stats__wifi.md#ae0149e64a94a9f96eb6680f94793c8c4)

struct net\_stats\_pkts errors

Total number of errors in RX and TX.

**Definition** net\_stats.h:620

[net\_stats\_wifi::unicast](structnet__stats__wifi.md#ae80dcd73a3c5ce3ec3282d1ae827b338)

struct net\_stats\_pkts unicast

Total number of unicast packets received and sent.

**Definition** net\_stats.h:623

[net\_stats](structnet__stats.md)

All network statistics in one struct.

**Definition** net\_stats.h:323

[net\_stats::processing\_error](structnet__stats.md#a3a4c90661d6b310b628262228a341fe2)

net\_stats\_t processing\_error

Count of malformed packets or packets we do not have handler for.

**Definition** net\_stats.h:325

[net\_stats::bytes](structnet__stats.md#a7a28233e6d23efdce0143469b9bb6c05)

struct net\_stats\_bytes bytes

This calculates amount of data transferred through all the network interfaces.

**Definition** net\_stats.h:331

[net\_stats::ip\_errors](structnet__stats.md#ac42cb13954d164e92a1ef60919a2a34e)

struct net\_stats\_ip\_errors ip\_errors

IP layer errors.

**Definition** net\_stats.h:334

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [net\_stats.h](net__stats_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
