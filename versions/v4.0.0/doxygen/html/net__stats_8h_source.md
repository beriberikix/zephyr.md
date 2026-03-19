---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/net__stats_8h_source.html
original_path: doxygen/html/net__stats_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
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

33

[ 38](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752)typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752);

39

[ 43](structnet__stats__bytes.md)struct [net\_stats\_bytes](structnet__stats__bytes.md) {

[ 45](structnet__stats__bytes.md#a89368f376c02d25c5a7a5719851a0ac7) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [sent](structnet__stats__bytes.md#a89368f376c02d25c5a7a5719851a0ac7);

[ 47](structnet__stats__bytes.md#a8bc21878924210278c6e0e2861163be4) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [received](structnet__stats__bytes.md#a8bc21878924210278c6e0e2861163be4);

48};

49

[ 53](structnet__stats__pkts.md)struct [net\_stats\_pkts](structnet__stats__pkts.md) {

[ 55](structnet__stats__pkts.md#aee1e302d0f8dac79b693a06d8fa3b3c5) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [tx](structnet__stats__pkts.md#aee1e302d0f8dac79b693a06d8fa3b3c5);

[ 57](structnet__stats__pkts.md#ac9784b5a245e6c57e39318aaf314f0cf) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [rx](structnet__stats__pkts.md#ac9784b5a245e6c57e39318aaf314f0cf);

58};

59

[ 63](structnet__stats__ip.md)struct [net\_stats\_ip](structnet__stats__ip.md) {

[ 65](structnet__stats__ip.md#ab6a6373368dd24cb51504c5729d535d3) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [recv](structnet__stats__ip.md#ab6a6373368dd24cb51504c5729d535d3);

66

[ 68](structnet__stats__ip.md#abbe676bbe9faa89b2b6b8c4950b1c9d5) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [sent](structnet__stats__ip.md#abbe676bbe9faa89b2b6b8c4950b1c9d5);

69

[ 71](structnet__stats__ip.md#a4bb82a5ebebaa3e8a11973c07eed96a0) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [forwarded](structnet__stats__ip.md#a4bb82a5ebebaa3e8a11973c07eed96a0);

72

[ 74](structnet__stats__ip.md#ac86399b70d7f761162e5336dd15589eb) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [drop](structnet__stats__ip.md#ac86399b70d7f761162e5336dd15589eb);

75};

76

[ 80](structnet__stats__ip__errors.md)struct [net\_stats\_ip\_errors](structnet__stats__ip__errors.md) {

[ 84](structnet__stats__ip__errors.md#a3e476f659ebeaa5c5f7b6dad2d90326f) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [vhlerr](structnet__stats__ip__errors.md#a3e476f659ebeaa5c5f7b6dad2d90326f);

85

[ 87](structnet__stats__ip__errors.md#a06b35742c418ebc6414fcb5c7002edde) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [hblenerr](structnet__stats__ip__errors.md#a06b35742c418ebc6414fcb5c7002edde);

88

[ 90](structnet__stats__ip__errors.md#a9b4bf05e9df13e1d99518125b9067bef) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [lblenerr](structnet__stats__ip__errors.md#a9b4bf05e9df13e1d99518125b9067bef);

91

[ 93](structnet__stats__ip__errors.md#ab84ee9dfbe5da391d60c6e3ae9abea16) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [fragerr](structnet__stats__ip__errors.md#ab84ee9dfbe5da391d60c6e3ae9abea16);

94

[ 96](structnet__stats__ip__errors.md#a872cc0beca45bbe87ae794dd8ca4e301) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [chkerr](structnet__stats__ip__errors.md#a872cc0beca45bbe87ae794dd8ca4e301);

97

[ 101](structnet__stats__ip__errors.md#a978b1c23847e707ac1fa27c2b34fa85d) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [protoerr](structnet__stats__ip__errors.md#a978b1c23847e707ac1fa27c2b34fa85d);

102};

103

[ 107](structnet__stats__icmp.md)struct [net\_stats\_icmp](structnet__stats__icmp.md) {

[ 109](structnet__stats__icmp.md#ae6f226b55565c11fca0c9e099f08c267) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [recv](structnet__stats__icmp.md#ae6f226b55565c11fca0c9e099f08c267);

110

[ 112](structnet__stats__icmp.md#a2d6eb7dfc8f4b439b399b039022f2889) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [sent](structnet__stats__icmp.md#a2d6eb7dfc8f4b439b399b039022f2889);

113

[ 115](structnet__stats__icmp.md#a755f3388c05d4bd2988ddd16d1a4cf32) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [drop](structnet__stats__icmp.md#a755f3388c05d4bd2988ddd16d1a4cf32);

116

[ 118](structnet__stats__icmp.md#ae1a29dd9b8e1ce9a737fa7f36c805cd4) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [typeerr](structnet__stats__icmp.md#ae1a29dd9b8e1ce9a737fa7f36c805cd4);

119

[ 121](structnet__stats__icmp.md#a6662bc547107a08c52e902a2446629bf) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [chkerr](structnet__stats__icmp.md#a6662bc547107a08c52e902a2446629bf);

122};

123

[ 127](structnet__stats__tcp.md)struct [net\_stats\_tcp](structnet__stats__tcp.md) {

[ 129](structnet__stats__tcp.md#af80c18bcc253133ce5f0597ac190b349) struct [net\_stats\_bytes](structnet__stats__bytes.md) [bytes](structnet__stats__tcp.md#af80c18bcc253133ce5f0597ac190b349);

130

[ 132](structnet__stats__tcp.md#abe567032cb4a267a984aec28c1e3cca4) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [resent](structnet__stats__tcp.md#abe567032cb4a267a984aec28c1e3cca4);

133

[ 135](structnet__stats__tcp.md#aa549f7b6d5828009a09190fd64afa8e3) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [drop](structnet__stats__tcp.md#aa549f7b6d5828009a09190fd64afa8e3);

136

[ 138](structnet__stats__tcp.md#ad25edb2b39a6acc8152c35ad43a5042f) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [recv](structnet__stats__tcp.md#ad25edb2b39a6acc8152c35ad43a5042f);

139

[ 141](structnet__stats__tcp.md#aa987bebf96000b6b4e92bfafc218759a) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [sent](structnet__stats__tcp.md#aa987bebf96000b6b4e92bfafc218759a);

142

[ 144](structnet__stats__tcp.md#a5f045704859331918511e9c2281ac155) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [seg\_drop](structnet__stats__tcp.md#a5f045704859331918511e9c2281ac155);

145

[ 147](structnet__stats__tcp.md#a5099e174b0eafa322f0630f1f5c73a8b) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [chkerr](structnet__stats__tcp.md#a5099e174b0eafa322f0630f1f5c73a8b);

148

[ 150](structnet__stats__tcp.md#a0d40abc85776f0a9b9510a909b7f6d18) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [ackerr](structnet__stats__tcp.md#a0d40abc85776f0a9b9510a909b7f6d18);

151

[ 153](structnet__stats__tcp.md#a471fcd5578f79ce77d20547b28503ac1) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [rsterr](structnet__stats__tcp.md#a471fcd5578f79ce77d20547b28503ac1);

154

[ 156](structnet__stats__tcp.md#aa618cf86b962aca0f14eb9178c8ae61a) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [rst](structnet__stats__tcp.md#aa618cf86b962aca0f14eb9178c8ae61a);

157

[ 159](structnet__stats__tcp.md#a4a4ea6e5d87ef58b4271bd708cf39635) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [rexmit](structnet__stats__tcp.md#a4a4ea6e5d87ef58b4271bd708cf39635);

160

[ 164](structnet__stats__tcp.md#ac557ac0d8917bc2c2dfed74126f993c8) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [conndrop](structnet__stats__tcp.md#ac557ac0d8917bc2c2dfed74126f993c8);

165

[ 167](structnet__stats__tcp.md#a67f55954a4c51f2b957c7d974e78c1c0) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [connrst](structnet__stats__tcp.md#a67f55954a4c51f2b957c7d974e78c1c0);

168};

169

[ 173](structnet__stats__udp.md)struct [net\_stats\_udp](structnet__stats__udp.md) {

[ 175](structnet__stats__udp.md#a2d884bf9106e60d430ffec7c7964a609) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [drop](structnet__stats__udp.md#a2d884bf9106e60d430ffec7c7964a609);

176

[ 178](structnet__stats__udp.md#a0ea91d85fe322661fb909f5e94e55a34) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [recv](structnet__stats__udp.md#a0ea91d85fe322661fb909f5e94e55a34);

179

[ 181](structnet__stats__udp.md#ab4e8228c221901d3ded55f3f823bfa1c) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [sent](structnet__stats__udp.md#ab4e8228c221901d3ded55f3f823bfa1c);

182

[ 184](structnet__stats__udp.md#a4c57d5f68ebda7981400729b9c7fe0f7) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [chkerr](structnet__stats__udp.md#a4c57d5f68ebda7981400729b9c7fe0f7);

185};

186

[ 190](structnet__stats__ipv6__nd.md)struct [net\_stats\_ipv6\_nd](structnet__stats__ipv6__nd.md) {

[ 192](structnet__stats__ipv6__nd.md#a31074d5d44138fcabdc5f7750f9f2c47) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [drop](structnet__stats__ipv6__nd.md#a31074d5d44138fcabdc5f7750f9f2c47);

193

[ 195](structnet__stats__ipv6__nd.md#a0bf6f67d9112996a3b002ea160aec769) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [recv](structnet__stats__ipv6__nd.md#a0bf6f67d9112996a3b002ea160aec769);

196

[ 198](structnet__stats__ipv6__nd.md#a0129f7892a4439c20deb2f32b9001277) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [sent](structnet__stats__ipv6__nd.md#a0129f7892a4439c20deb2f32b9001277);

199};

200

[ 204](structnet__stats__ipv6__mld.md)struct [net\_stats\_ipv6\_mld](structnet__stats__ipv6__mld.md) {

[ 206](structnet__stats__ipv6__mld.md#a4879ff9e31f8b60973d3b169598e921d) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [recv](structnet__stats__ipv6__mld.md#a4879ff9e31f8b60973d3b169598e921d);

207

[ 209](structnet__stats__ipv6__mld.md#ab397b74b14ce7047bf2fc63ca72ce1e5) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [sent](structnet__stats__ipv6__mld.md#ab397b74b14ce7047bf2fc63ca72ce1e5);

210

[ 212](structnet__stats__ipv6__mld.md#ad85dc87f57296a1e7d64e959b0370ee8) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [drop](structnet__stats__ipv6__mld.md#ad85dc87f57296a1e7d64e959b0370ee8);

213};

214

[ 218](structnet__stats__ipv4__igmp.md)struct [net\_stats\_ipv4\_igmp](structnet__stats__ipv4__igmp.md) {

[ 220](structnet__stats__ipv4__igmp.md#a469113de7af0ba42dbd1b0365d00602c) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [recv](structnet__stats__ipv4__igmp.md#a469113de7af0ba42dbd1b0365d00602c);

221

[ 223](structnet__stats__ipv4__igmp.md#a955e20a6ee5e19e08000b3114b9d71a6) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [sent](structnet__stats__ipv4__igmp.md#a955e20a6ee5e19e08000b3114b9d71a6);

224

[ 226](structnet__stats__ipv4__igmp.md#a1c37702ff837b8c5cc9df5f690e7678c) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [drop](structnet__stats__ipv4__igmp.md#a1c37702ff837b8c5cc9df5f690e7678c);

227};

228

[ 232](structnet__stats__dns.md)struct [net\_stats\_dns](structnet__stats__dns.md) {

[ 234](structnet__stats__dns.md#abc9be2039a3ff9e62b956ae27fd0ab84) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [recv](structnet__stats__dns.md#abc9be2039a3ff9e62b956ae27fd0ab84);

235

[ 237](structnet__stats__dns.md#ac07b9f4d084b978cc11e7799fb71a435) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [sent](structnet__stats__dns.md#ac07b9f4d084b978cc11e7799fb71a435);

238

[ 240](structnet__stats__dns.md#a04756603a183f35dbf6f55000556b546) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [drop](structnet__stats__dns.md#a04756603a183f35dbf6f55000556b546);

241};

242

[ 246](structnet__stats__tx__time.md)struct [net\_stats\_tx\_time](structnet__stats__tx__time.md) {

[ 248](structnet__stats__tx__time.md#af6f7a26c0344a0f93306e105a8917c3e) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [sum](structnet__stats__tx__time.md#af6f7a26c0344a0f93306e105a8917c3e);

249

[ 251](structnet__stats__tx__time.md#a7a652350ed04e53ba02aec294f8444b4) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [count](structnet__stats__tx__time.md#a7a652350ed04e53ba02aec294f8444b4);

252};

253

[ 257](structnet__stats__rx__time.md)struct [net\_stats\_rx\_time](structnet__stats__rx__time.md) {

[ 259](structnet__stats__rx__time.md#a4b84c2ae2fda8fcd75fdf1bf0b2aae8d) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [sum](structnet__stats__rx__time.md#a4b84c2ae2fda8fcd75fdf1bf0b2aae8d);

260

[ 262](structnet__stats__rx__time.md#a68247051b064de081fa2e84118192958) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [count](structnet__stats__rx__time.md#a68247051b064de081fa2e84118192958);

263};

264

266

267#if NET\_TC\_TX\_COUNT == 0

268#define NET\_TC\_TX\_STATS\_COUNT 1

269#else

270#define NET\_TC\_TX\_STATS\_COUNT NET\_TC\_TX\_COUNT

271#endif

272

273#if NET\_TC\_RX\_COUNT == 0

274#define NET\_TC\_RX\_STATS\_COUNT 1

275#else

276#define NET\_TC\_RX\_STATS\_COUNT NET\_TC\_RX\_COUNT

277#endif

278

280

[ 284](structnet__stats__tc.md)struct [net\_stats\_tc](structnet__stats__tc.md) {

286 struct {

[ 288](structnet__stats__tc.md#a30288ef3bb0796cd18c3cf0aedbe875a) struct [net\_stats\_tx\_time](structnet__stats__tx__time.md) [tx\_time](structnet__stats__tc.md#a30288ef3bb0796cd18c3cf0aedbe875a);

289#if defined(CONFIG\_NET\_PKT\_TXTIME\_STATS\_DETAIL)

291 struct [net\_stats\_tx\_time](structnet__stats__tx__time.md)

292 tx\_time\_detail[NET\_PKT\_DETAIL\_STATS\_COUNT];

293#endif

[ 295](structnet__stats__tc.md#a6614b5f5186635415a7d787260c39248) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [pkts](structnet__stats__tc.md#a6614b5f5186635415a7d787260c39248);

[ 297](structnet__stats__tc.md#a192a7ec0d24bce9e62f766e481ee5709) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [bytes](structnet__stats__tc.md#a192a7ec0d24bce9e62f766e481ee5709);

[ 299](structnet__stats__tc.md#a8a5c2e59990407ddbfc7973a1c183bf6) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [priority](structnet__stats__tc.md#a8a5c2e59990407ddbfc7973a1c183bf6);

[ 300](structnet__stats__tc.md#a8d6a3ebcc49ce8c34a5faae986f648e2) } [sent](structnet__stats__tc.md#a8d6a3ebcc49ce8c34a5faae986f648e2)[NET\_TC\_TX\_STATS\_COUNT];

301

303 struct {

[ 305](structnet__stats__tc.md#a8ea00824bb0fb18e4d8912343e01c3b7) struct [net\_stats\_rx\_time](structnet__stats__rx__time.md) [rx\_time](structnet__stats__tc.md#a8ea00824bb0fb18e4d8912343e01c3b7);

306#if defined(CONFIG\_NET\_PKT\_RXTIME\_STATS\_DETAIL)

308 struct [net\_stats\_rx\_time](structnet__stats__rx__time.md)

309 rx\_time\_detail[NET\_PKT\_DETAIL\_STATS\_COUNT];

310#endif

312 [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [pkts](structnet__stats__tc.md#a6614b5f5186635415a7d787260c39248);

314 [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [bytes](structnet__stats__tc.md#a192a7ec0d24bce9e62f766e481ee5709);

316 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [priority](structnet__stats__tc.md#a8a5c2e59990407ddbfc7973a1c183bf6);

[ 317](structnet__stats__tc.md#a2c8826e27ff59154f14a1755ffd4c594) } [recv](group__bsd__sockets.md#gae11da452beee536eac85d5f26e5cdd40)[NET\_TC\_RX\_STATS\_COUNT];

318};

319

320

[ 324](structnet__stats__pm.md)struct [net\_stats\_pm](structnet__stats__pm.md) {

[ 326](structnet__stats__pm.md#ab43935fcfe9efc1cd5f3e7e329996805) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [overall\_suspend\_time](structnet__stats__pm.md#ab43935fcfe9efc1cd5f3e7e329996805);

[ 328](structnet__stats__pm.md#ac14122a4765c499c045f18c70af355a0) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [suspend\_count](structnet__stats__pm.md#ac14122a4765c499c045f18c70af355a0);

[ 330](structnet__stats__pm.md#a0bdf9c3676298e2df4ff3bfa03f5e823) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [last\_suspend\_time](structnet__stats__pm.md#a0bdf9c3676298e2df4ff3bfa03f5e823);

[ 332](structnet__stats__pm.md#a6784806eaa093431ed3c0f7acfe5a89c) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [start\_time](structnet__stats__pm.md#a6784806eaa093431ed3c0f7acfe5a89c);

333};

334

335

[ 339](structnet__stats.md)struct [net\_stats](structnet__stats.md) {

[ 341](structnet__stats.md#a3a4c90661d6b310b628262228a341fe2) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [processing\_error](structnet__stats.md#a3a4c90661d6b310b628262228a341fe2);

342

[ 347](structnet__stats.md#a7a28233e6d23efdce0143469b9bb6c05) struct [net\_stats\_bytes](structnet__stats__bytes.md) [bytes](structnet__stats.md#a7a28233e6d23efdce0143469b9bb6c05);

348

[ 350](structnet__stats.md#ac42cb13954d164e92a1ef60919a2a34e) struct [net\_stats\_ip\_errors](structnet__stats__ip__errors.md) [ip\_errors](structnet__stats.md#ac42cb13954d164e92a1ef60919a2a34e);

351

352#if defined(CONFIG\_NET\_STATISTICS\_IPV6)

354 struct [net\_stats\_ip](structnet__stats__ip.md) ipv6;

355#endif

356

357#if defined(CONFIG\_NET\_STATISTICS\_IPV4)

359 struct [net\_stats\_ip](structnet__stats__ip.md) ipv4;

360#endif

361

362#if defined(CONFIG\_NET\_STATISTICS\_ICMP)

364 struct [net\_stats\_icmp](structnet__stats__icmp.md) icmp;

365#endif

366

367#if defined(CONFIG\_NET\_STATISTICS\_TCP)

369 struct [net\_stats\_tcp](structnet__stats__tcp.md) tcp;

370#endif

371

372#if defined(CONFIG\_NET\_STATISTICS\_UDP)

374 struct [net\_stats\_udp](structnet__stats__udp.md) udp;

375#endif

376

377#if defined(CONFIG\_NET\_STATISTICS\_IPV6\_ND)

379 struct [net\_stats\_ipv6\_nd](structnet__stats__ipv6__nd.md) ipv6\_nd;

380#endif

381

382#if defined(CONFIG\_NET\_STATISTICS\_MLD)

384 struct [net\_stats\_ipv6\_mld](structnet__stats__ipv6__mld.md) ipv6\_mld;

385#endif

386

387#if defined(CONFIG\_NET\_STATISTICS\_IGMP)

389 struct [net\_stats\_ipv4\_igmp](structnet__stats__ipv4__igmp.md) ipv4\_igmp;

390#endif

391

392#if defined(CONFIG\_NET\_STATISTICS\_DNS)

394 struct [net\_stats\_dns](structnet__stats__dns.md) dns;

395#endif

396

397#if NET\_TC\_COUNT > 1

399 struct [net\_stats\_tc](structnet__stats__tc.md) tc;

400#endif

401

402#if defined(CONFIG\_NET\_PKT\_TXTIME\_STATS)

404 struct [net\_stats\_tx\_time](structnet__stats__tx__time.md) tx\_time;

405#endif

406

407#if defined(CONFIG\_NET\_PKT\_RXTIME\_STATS)

409 struct [net\_stats\_rx\_time](structnet__stats__rx__time.md) rx\_time;

410#endif

411

412#if defined(CONFIG\_NET\_PKT\_TXTIME\_STATS\_DETAIL)

414 struct [net\_stats\_tx\_time](structnet__stats__tx__time.md) tx\_time\_detail[NET\_PKT\_DETAIL\_STATS\_COUNT];

415#endif

416#if defined(CONFIG\_NET\_PKT\_RXTIME\_STATS\_DETAIL)

418 struct [net\_stats\_rx\_time](structnet__stats__rx__time.md) rx\_time\_detail[NET\_PKT\_DETAIL\_STATS\_COUNT];

419#endif

420

421#if defined(CONFIG\_NET\_STATISTICS\_POWER\_MANAGEMENT)

423 struct [net\_stats\_pm](structnet__stats__pm.md) pm;

424#endif

425};

426

[ 430](structnet__stats__eth__errors.md)struct [net\_stats\_eth\_errors](structnet__stats__eth__errors.md) {

[ 432](structnet__stats__eth__errors.md#aca0e2e4807fa70279dee8ddaad2d7ef7) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [rx\_length\_errors](structnet__stats__eth__errors.md#aca0e2e4807fa70279dee8ddaad2d7ef7);

433

[ 435](structnet__stats__eth__errors.md#a9afee89f5bb01907e7cd515e2a0ff1b5) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [rx\_over\_errors](structnet__stats__eth__errors.md#a9afee89f5bb01907e7cd515e2a0ff1b5);

436

[ 438](structnet__stats__eth__errors.md#a4dab70cf219269bb393ce14faf0ed77e) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [rx\_crc\_errors](structnet__stats__eth__errors.md#a4dab70cf219269bb393ce14faf0ed77e);

439

[ 441](structnet__stats__eth__errors.md#a8dfcc5cd1b4decec5783d01ba7033b05) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [rx\_frame\_errors](structnet__stats__eth__errors.md#a8dfcc5cd1b4decec5783d01ba7033b05);

442

[ 444](structnet__stats__eth__errors.md#a82622736d226b4d3b999f1f22ccf8529) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [rx\_no\_buffer\_count](structnet__stats__eth__errors.md#a82622736d226b4d3b999f1f22ccf8529);

445

[ 447](structnet__stats__eth__errors.md#a2d2b2c4e3764ebec841f1ecbe7058d99) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [rx\_missed\_errors](structnet__stats__eth__errors.md#a2d2b2c4e3764ebec841f1ecbe7058d99);

448

[ 450](structnet__stats__eth__errors.md#a0e83e270a35222ed3e927800be4159e7) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [rx\_long\_length\_errors](structnet__stats__eth__errors.md#a0e83e270a35222ed3e927800be4159e7);

451

[ 453](structnet__stats__eth__errors.md#a5e3d39d8417bb180cbfcb8c901006e81) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [rx\_short\_length\_errors](structnet__stats__eth__errors.md#a5e3d39d8417bb180cbfcb8c901006e81);

454

[ 456](structnet__stats__eth__errors.md#a7618f10af3443c49a6e256bb41e77781) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [rx\_align\_errors](structnet__stats__eth__errors.md#a7618f10af3443c49a6e256bb41e77781);

457

[ 459](structnet__stats__eth__errors.md#a7bcfbb13836f162ceeb5f021304b5c76) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [rx\_dma\_failed](structnet__stats__eth__errors.md#a7bcfbb13836f162ceeb5f021304b5c76);

460

[ 462](structnet__stats__eth__errors.md#adbcae9c10c081f1cdf304bcdce740aa4) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [rx\_buf\_alloc\_failed](structnet__stats__eth__errors.md#adbcae9c10c081f1cdf304bcdce740aa4);

463

[ 465](structnet__stats__eth__errors.md#afec6a7e24c6f3cc74dd9f739f27b3e48) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [tx\_aborted\_errors](structnet__stats__eth__errors.md#afec6a7e24c6f3cc74dd9f739f27b3e48);

466

[ 468](structnet__stats__eth__errors.md#a0043d1a1481040a6d7439bd23423ec12) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [tx\_carrier\_errors](structnet__stats__eth__errors.md#a0043d1a1481040a6d7439bd23423ec12);

469

[ 471](structnet__stats__eth__errors.md#a84630da9b82557f56dc35cd59ca2f7ae) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [tx\_fifo\_errors](structnet__stats__eth__errors.md#a84630da9b82557f56dc35cd59ca2f7ae);

472

[ 474](structnet__stats__eth__errors.md#ae2a13733c1a5f0cc3e00efca0c3f429d) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [tx\_heartbeat\_errors](structnet__stats__eth__errors.md#ae2a13733c1a5f0cc3e00efca0c3f429d);

475

[ 477](structnet__stats__eth__errors.md#a17624a12d6473bdd78698076fed0d122) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [tx\_window\_errors](structnet__stats__eth__errors.md#a17624a12d6473bdd78698076fed0d122);

478

[ 480](structnet__stats__eth__errors.md#abfbf6478b7afdd5935d7c6948c9ef426) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [tx\_dma\_failed](structnet__stats__eth__errors.md#abfbf6478b7afdd5935d7c6948c9ef426);

481

[ 483](structnet__stats__eth__errors.md#a07d0a435f2129556520c732571d28edf) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [uncorr\_ecc\_errors](structnet__stats__eth__errors.md#a07d0a435f2129556520c732571d28edf);

484

[ 486](structnet__stats__eth__errors.md#a257113639f0e0e3085febb7a147f498f) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [corr\_ecc\_errors](structnet__stats__eth__errors.md#a257113639f0e0e3085febb7a147f498f);

487};

488

[ 492](structnet__stats__eth__flow.md)struct [net\_stats\_eth\_flow](structnet__stats__eth__flow.md) {

[ 494](structnet__stats__eth__flow.md#a08e5da4ff78fe3893b9c9a628cefe4f2) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [rx\_flow\_control\_xon](structnet__stats__eth__flow.md#a08e5da4ff78fe3893b9c9a628cefe4f2);

495

[ 497](structnet__stats__eth__flow.md#a8f9b93537b3c11be70f276aaa72cb637) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [rx\_flow\_control\_xoff](structnet__stats__eth__flow.md#a8f9b93537b3c11be70f276aaa72cb637);

498

[ 500](structnet__stats__eth__flow.md#a31412e8bf9d38ba630ea856e958a48d7) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [tx\_flow\_control\_xon](structnet__stats__eth__flow.md#a31412e8bf9d38ba630ea856e958a48d7);

501

[ 503](structnet__stats__eth__flow.md#a969d81f9db20312d2d2aa7f70f93bdd5) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [tx\_flow\_control\_xoff](structnet__stats__eth__flow.md#a969d81f9db20312d2d2aa7f70f93bdd5);

504};

505

[ 509](structnet__stats__eth__csum.md)struct [net\_stats\_eth\_csum](structnet__stats__eth__csum.md) {

[ 511](structnet__stats__eth__csum.md#a1f1ba5c01c6232cd739d069ddb871b17) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [rx\_csum\_offload\_good](structnet__stats__eth__csum.md#a1f1ba5c01c6232cd739d069ddb871b17);

512

[ 514](structnet__stats__eth__csum.md#ac4fc04d66193070d4f52a4c07f29ccce) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [rx\_csum\_offload\_errors](structnet__stats__eth__csum.md#ac4fc04d66193070d4f52a4c07f29ccce);

515};

516

[ 520](structnet__stats__eth__hw__timestamp.md)struct [net\_stats\_eth\_hw\_timestamp](structnet__stats__eth__hw__timestamp.md) {

[ 522](structnet__stats__eth__hw__timestamp.md#acd3d5f72d7df568110d96093e0c9534d) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [rx\_hwtstamp\_cleared](structnet__stats__eth__hw__timestamp.md#acd3d5f72d7df568110d96093e0c9534d);

523

[ 525](structnet__stats__eth__hw__timestamp.md#a41f605499dbf88a879522fdfa4633d9e) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [tx\_hwtstamp\_timeouts](structnet__stats__eth__hw__timestamp.md#a41f605499dbf88a879522fdfa4633d9e);

526

[ 528](structnet__stats__eth__hw__timestamp.md#ae1f983faf4a999308c464e4af5a5284b) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [tx\_hwtstamp\_skipped](structnet__stats__eth__hw__timestamp.md#ae1f983faf4a999308c464e4af5a5284b);

529};

530

531#ifdef CONFIG\_NET\_STATISTICS\_ETHERNET\_VENDOR

535struct net\_stats\_eth\_vendor {

536 const char \* const key;

537 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) value;

538};

539#endif

540

[ 544](structnet__stats__eth.md)struct [net\_stats\_eth](structnet__stats__eth.md) {

[ 546](structnet__stats__eth.md#a8c5cf1ead8ba214425a16fed1c2ad0fb) struct [net\_stats\_bytes](structnet__stats__bytes.md) [bytes](structnet__stats__eth.md#a8c5cf1ead8ba214425a16fed1c2ad0fb);

547

[ 549](structnet__stats__eth.md#a97bd6026b16890743f344751a21107f1) struct [net\_stats\_pkts](structnet__stats__pkts.md) [pkts](structnet__stats__eth.md#a97bd6026b16890743f344751a21107f1);

550

[ 552](structnet__stats__eth.md#a054beb909134b0e0f22f5df599549128) struct [net\_stats\_pkts](structnet__stats__pkts.md) [broadcast](structnet__stats__eth.md#a054beb909134b0e0f22f5df599549128);

553

[ 555](structnet__stats__eth.md#a4f6a2903330518a132e7e547820e0bf2) struct [net\_stats\_pkts](structnet__stats__pkts.md) [multicast](structnet__stats__eth.md#a4f6a2903330518a132e7e547820e0bf2);

556

[ 558](structnet__stats__eth.md#a9c869740f416fbe0b54d7fefacb1fe29) struct [net\_stats\_pkts](structnet__stats__pkts.md) [errors](structnet__stats__eth.md#a9c869740f416fbe0b54d7fefacb1fe29);

559

[ 561](structnet__stats__eth.md#a922feddb17fc020371f1bcc52c709415) struct [net\_stats\_eth\_errors](structnet__stats__eth__errors.md) [error\_details](structnet__stats__eth.md#a922feddb17fc020371f1bcc52c709415);

562

[ 564](structnet__stats__eth.md#a643010ac6360c8c0c08016725ba12222) struct [net\_stats\_eth\_flow](structnet__stats__eth__flow.md) [flow\_control](structnet__stats__eth.md#a643010ac6360c8c0c08016725ba12222);

565

[ 567](structnet__stats__eth.md#a2169ae06bace1a93663bccf88c8d7a29) struct [net\_stats\_eth\_csum](structnet__stats__eth__csum.md) [csum](structnet__stats__eth.md#a2169ae06bace1a93663bccf88c8d7a29);

568

[ 570](structnet__stats__eth.md#a44667efff73c17c089ed22d5b0da5ad3) struct [net\_stats\_eth\_hw\_timestamp](structnet__stats__eth__hw__timestamp.md) [hw\_timestamp](structnet__stats__eth.md#a44667efff73c17c089ed22d5b0da5ad3);

571

[ 573](structnet__stats__eth.md#a822d4205791f59999c842610522f6fc5) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [collisions](structnet__stats__eth.md#a822d4205791f59999c842610522f6fc5);

574

[ 576](structnet__stats__eth.md#a257c349cf3d32d38796e3899e702454a) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [tx\_dropped](structnet__stats__eth.md#a257c349cf3d32d38796e3899e702454a);

577

[ 579](structnet__stats__eth.md#ab351258ae82abd09759d37774559d8bc) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [tx\_timeout\_count](structnet__stats__eth.md#ab351258ae82abd09759d37774559d8bc);

580

[ 582](structnet__stats__eth.md#a6699012226e25e8bad39076fed6dbfb5) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [tx\_restart\_queue](structnet__stats__eth.md#a6699012226e25e8bad39076fed6dbfb5);

583

[ 585](structnet__stats__eth.md#afaacee7cc1d0a35ae2344175421c40dd) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [unknown\_protocol](structnet__stats__eth.md#afaacee7cc1d0a35ae2344175421c40dd);

586

587#ifdef CONFIG\_NET\_STATISTICS\_ETHERNET\_VENDOR

589 struct net\_stats\_eth\_vendor \*vendor;

590#endif

591};

592

[ 596](structnet__stats__ppp.md)struct [net\_stats\_ppp](structnet__stats__ppp.md) {

[ 598](structnet__stats__ppp.md#ab2b48da7f19d4b83e3f41b41979b7ed8) struct [net\_stats\_bytes](structnet__stats__bytes.md) [bytes](structnet__stats__ppp.md#ab2b48da7f19d4b83e3f41b41979b7ed8);

599

[ 601](structnet__stats__ppp.md#a71fc81f3c5f3e65a476b3391f086d340) struct [net\_stats\_pkts](structnet__stats__pkts.md) [pkts](structnet__stats__ppp.md#a71fc81f3c5f3e65a476b3391f086d340);

602

[ 604](structnet__stats__ppp.md#ae2e0a47a539e9d7bc97f9c63f889b276) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [drop](structnet__stats__ppp.md#ae2e0a47a539e9d7bc97f9c63f889b276);

605

[ 607](structnet__stats__ppp.md#a1332b31980f82236aeb0c3f9444e2ac6) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [chkerr](structnet__stats__ppp.md#a1332b31980f82236aeb0c3f9444e2ac6);

608};

609

[ 613](structnet__stats__sta__mgmt.md)struct [net\_stats\_sta\_mgmt](structnet__stats__sta__mgmt.md) {

[ 615](structnet__stats__sta__mgmt.md#ac6e68fded8e19b20259442436923f815) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [beacons\_rx](structnet__stats__sta__mgmt.md#ac6e68fded8e19b20259442436923f815);

616

[ 618](structnet__stats__sta__mgmt.md#a29ae0079b4c780e0de2656a85ec15fe9) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [beacons\_miss](structnet__stats__sta__mgmt.md#a29ae0079b4c780e0de2656a85ec15fe9);

619};

620

[ 624](structnet__stats__wifi.md)struct [net\_stats\_wifi](structnet__stats__wifi.md) {

[ 626](structnet__stats__wifi.md#a8bee22961545674e6ab100b58a04bf91) struct [net\_stats\_sta\_mgmt](structnet__stats__sta__mgmt.md) [sta\_mgmt](structnet__stats__wifi.md#a8bee22961545674e6ab100b58a04bf91);

627

[ 629](structnet__stats__wifi.md#aa055b1e8bd8f1e50815c1028b562be07) struct [net\_stats\_bytes](structnet__stats__bytes.md) [bytes](structnet__stats__wifi.md#aa055b1e8bd8f1e50815c1028b562be07);

630

[ 632](structnet__stats__wifi.md#adbcdb2dd8733f2917c00a0b2d365393b) struct [net\_stats\_pkts](structnet__stats__pkts.md) [pkts](structnet__stats__wifi.md#adbcdb2dd8733f2917c00a0b2d365393b);

633

[ 635](structnet__stats__wifi.md#a03dc04638c4b670bd7f3520d45fc1eda) struct [net\_stats\_pkts](structnet__stats__pkts.md) [broadcast](structnet__stats__wifi.md#a03dc04638c4b670bd7f3520d45fc1eda);

636

[ 638](structnet__stats__wifi.md#a7e7f68215101885fd51c70e981da26e7) struct [net\_stats\_pkts](structnet__stats__pkts.md) [multicast](structnet__stats__wifi.md#a7e7f68215101885fd51c70e981da26e7);

639

[ 641](structnet__stats__wifi.md#ae0149e64a94a9f96eb6680f94793c8c4) struct [net\_stats\_pkts](structnet__stats__pkts.md) [errors](structnet__stats__wifi.md#ae0149e64a94a9f96eb6680f94793c8c4);

642

[ 644](structnet__stats__wifi.md#ae80dcd73a3c5ce3ec3282d1ae827b338) struct [net\_stats\_pkts](structnet__stats__pkts.md) [unicast](structnet__stats__wifi.md#ae80dcd73a3c5ce3ec3282d1ae827b338);

645

[ 647](structnet__stats__wifi.md#ac498c9e517f2cb2eb01d251e84159e7e) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [overrun\_count](structnet__stats__wifi.md#ac498c9e517f2cb2eb01d251e84159e7e);

648};

649

650#if defined(CONFIG\_NET\_STATISTICS\_USER\_API)

651/\* Management part definitions \*/

652

654

655#define \_NET\_STATS\_LAYER NET\_MGMT\_LAYER\_L3

656#define \_NET\_STATS\_CODE 0x101

657#define \_NET\_STATS\_BASE (NET\_MGMT\_LAYER(\_NET\_STATS\_LAYER) | \

658 NET\_MGMT\_LAYER\_CODE(\_NET\_STATS\_CODE))

659

660enum net\_request\_stats\_cmd {

661 NET\_REQUEST\_STATS\_CMD\_GET\_ALL = 1,

662 NET\_REQUEST\_STATS\_CMD\_GET\_PROCESSING\_ERROR,

663 NET\_REQUEST\_STATS\_CMD\_GET\_BYTES,

664 NET\_REQUEST\_STATS\_CMD\_GET\_IP\_ERRORS,

665 NET\_REQUEST\_STATS\_CMD\_GET\_IPV4,

666 NET\_REQUEST\_STATS\_CMD\_GET\_IPV6,

667 NET\_REQUEST\_STATS\_CMD\_GET\_IPV6\_ND,

668 NET\_REQUEST\_STATS\_CMD\_GET\_ICMP,

669 NET\_REQUEST\_STATS\_CMD\_GET\_UDP,

670 NET\_REQUEST\_STATS\_CMD\_GET\_TCP,

671 NET\_REQUEST\_STATS\_CMD\_GET\_ETHERNET,

672 NET\_REQUEST\_STATS\_CMD\_GET\_PPP,

673 NET\_REQUEST\_STATS\_CMD\_GET\_PM,

674 NET\_REQUEST\_STATS\_CMD\_GET\_WIFI,

675 NET\_REQUEST\_STATS\_CMD\_RESET\_WIFI,

676};

677

679

681#define NET\_REQUEST\_STATS\_GET\_ALL \

682 (\_NET\_STATS\_BASE | NET\_REQUEST\_STATS\_CMD\_GET\_ALL)

683

685#define NET\_REQUEST\_STATS\_GET\_PROCESSING\_ERROR \

686 (\_NET\_STATS\_BASE | NET\_REQUEST\_STATS\_CMD\_GET\_PROCESSING\_ERROR)

687

689#define NET\_REQUEST\_STATS\_GET\_BYTES \

690 (\_NET\_STATS\_BASE | NET\_REQUEST\_STATS\_CMD\_GET\_BYTES)

691

693#define NET\_REQUEST\_STATS\_GET\_IP\_ERRORS \

694 (\_NET\_STATS\_BASE | NET\_REQUEST\_STATS\_CMD\_GET\_IP\_ERRORS)

695

697

698[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_STATS\_GET\_ALL);

699[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_STATS\_GET\_PROCESSING\_ERROR);

700[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_STATS\_GET\_BYTES);

701[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_STATS\_GET\_IP\_ERRORS);

702

704

705#if defined(CONFIG\_NET\_STATISTICS\_IPV4)

707#define NET\_REQUEST\_STATS\_GET\_IPV4 \

708 (\_NET\_STATS\_BASE | NET\_REQUEST\_STATS\_CMD\_GET\_IPV4)

709

711[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_STATS\_GET\_IPV4);

713#endif /\* CONFIG\_NET\_STATISTICS\_IPV4 \*/

714

715#if defined(CONFIG\_NET\_STATISTICS\_IPV6)

717#define NET\_REQUEST\_STATS\_GET\_IPV6 \

718 (\_NET\_STATS\_BASE | NET\_REQUEST\_STATS\_CMD\_GET\_IPV6)

719

721[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_STATS\_GET\_IPV6);

723#endif /\* CONFIG\_NET\_STATISTICS\_IPV6 \*/

724

725#if defined(CONFIG\_NET\_STATISTICS\_IPV6\_ND)

727#define NET\_REQUEST\_STATS\_GET\_IPV6\_ND \

728 (\_NET\_STATS\_BASE | NET\_REQUEST\_STATS\_CMD\_GET\_IPV6\_ND)

729

731[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_STATS\_GET\_IPV6\_ND);

733#endif /\* CONFIG\_NET\_STATISTICS\_IPV6\_ND \*/

734

735#if defined(CONFIG\_NET\_STATISTICS\_ICMP)

737#define NET\_REQUEST\_STATS\_GET\_ICMP \

738 (\_NET\_STATS\_BASE | NET\_REQUEST\_STATS\_CMD\_GET\_ICMP)

739

741[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_STATS\_GET\_ICMP);

743#endif /\* CONFIG\_NET\_STATISTICS\_ICMP \*/

744

745#if defined(CONFIG\_NET\_STATISTICS\_UDP)

747#define NET\_REQUEST\_STATS\_GET\_UDP \

748 (\_NET\_STATS\_BASE | NET\_REQUEST\_STATS\_CMD\_GET\_UDP)

749

751[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_STATS\_GET\_UDP);

753#endif /\* CONFIG\_NET\_STATISTICS\_UDP \*/

754

755#if defined(CONFIG\_NET\_STATISTICS\_TCP)

757#define NET\_REQUEST\_STATS\_GET\_TCP \

758 (\_NET\_STATS\_BASE | NET\_REQUEST\_STATS\_CMD\_GET\_TCP)

759

761[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_STATS\_GET\_TCP);

763#endif /\* CONFIG\_NET\_STATISTICS\_TCP \*/

764

765#if defined(CONFIG\_NET\_STATISTICS\_ETHERNET)

767#define NET\_REQUEST\_STATS\_GET\_ETHERNET \

768 (\_NET\_STATS\_BASE | NET\_REQUEST\_STATS\_CMD\_GET\_ETHERNET)

769

771[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_STATS\_GET\_ETHERNET);

773#endif /\* CONFIG\_NET\_STATISTICS\_ETHERNET \*/

774

775#if defined(CONFIG\_NET\_STATISTICS\_PPP)

777#define NET\_REQUEST\_STATS\_GET\_PPP \

778 (\_NET\_STATS\_BASE | NET\_REQUEST\_STATS\_CMD\_GET\_PPP)

779

781[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_STATS\_GET\_PPP);

783#endif /\* CONFIG\_NET\_STATISTICS\_PPP \*/

784

785#endif /\* CONFIG\_NET\_STATISTICS\_USER\_API \*/

786

787#if defined(CONFIG\_NET\_STATISTICS\_POWER\_MANAGEMENT)

789#define NET\_REQUEST\_STATS\_GET\_PM \

790 (\_NET\_STATS\_BASE | NET\_REQUEST\_STATS\_CMD\_GET\_PM)

791

793[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_STATS\_GET\_PM);

795#endif /\* CONFIG\_NET\_STATISTICS\_POWER\_MANAGEMENT \*/

796

797#if defined(CONFIG\_NET\_STATISTICS\_WIFI)

799#define NET\_REQUEST\_STATS\_GET\_WIFI \

800 (\_NET\_STATS\_BASE | NET\_REQUEST\_STATS\_CMD\_GET\_WIFI)

801

803[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_STATS\_GET\_WIFI);

805

807#define NET\_REQUEST\_STATS\_RESET\_WIFI \

808 (\_NET\_STATS\_BASE | NET\_REQUEST\_STATS\_CMD\_RESET\_WIFI)

809

811[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_STATS\_RESET\_WIFI);

813#endif /\* CONFIG\_NET\_STATISTICS\_WIFI \*/

814

818

819#ifdef \_\_cplusplus

820}

821#endif

822

823#endif /\* ZEPHYR\_INCLUDE\_NET\_NET\_STATS\_H\_ \*/

[recv](group__bsd__sockets.md#gae11da452beee536eac85d5f26e5cdd40)

static ssize\_t recv(int sock, void \*buf, size\_t max\_len, int flags)

POSIX wrapper for zsock\_recv.

**Definition** socket.h:873

[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)

#define NET\_MGMT\_DEFINE\_REQUEST\_HANDLER(\_mgmt\_request)

Declare a request handler function for the given network event.

**Definition** net\_mgmt.h:111

[net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752)

uint32\_t net\_stats\_t

Network statistics counter.

**Definition** net\_stats.h:38

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

**Definition** net\_stats.h:43

[net\_stats\_bytes::sent](structnet__stats__bytes.md#a89368f376c02d25c5a7a5719851a0ac7)

net\_stats\_t sent

Number of bytes sent.

**Definition** net\_stats.h:45

[net\_stats\_bytes::received](structnet__stats__bytes.md#a8bc21878924210278c6e0e2861163be4)

net\_stats\_t received

Number of bytes received.

**Definition** net\_stats.h:47

[net\_stats\_dns](structnet__stats__dns.md)

DNS statistics.

**Definition** net\_stats.h:232

[net\_stats\_dns::drop](structnet__stats__dns.md#a04756603a183f35dbf6f55000556b546)

net\_stats\_t drop

Number of dropped DNS packets.

**Definition** net\_stats.h:240

[net\_stats\_dns::recv](structnet__stats__dns.md#abc9be2039a3ff9e62b956ae27fd0ab84)

net\_stats\_t recv

Number of received DNS queries.

**Definition** net\_stats.h:234

[net\_stats\_dns::sent](structnet__stats__dns.md#ac07b9f4d084b978cc11e7799fb71a435)

net\_stats\_t sent

Number of sent DNS responses.

**Definition** net\_stats.h:237

[net\_stats\_eth\_csum](structnet__stats__eth__csum.md)

Ethernet checksum statistics.

**Definition** net\_stats.h:509

[net\_stats\_eth\_csum::rx\_csum\_offload\_good](structnet__stats__eth__csum.md#a1f1ba5c01c6232cd739d069ddb871b17)

net\_stats\_t rx\_csum\_offload\_good

Number of good RX checksum offloading.

**Definition** net\_stats.h:511

[net\_stats\_eth\_csum::rx\_csum\_offload\_errors](structnet__stats__eth__csum.md#ac4fc04d66193070d4f52a4c07f29ccce)

net\_stats\_t rx\_csum\_offload\_errors

Number of failed RX checksum offloading.

**Definition** net\_stats.h:514

[net\_stats\_eth\_errors](structnet__stats__eth__errors.md)

Ethernet error statistics.

**Definition** net\_stats.h:430

[net\_stats\_eth\_errors::tx\_carrier\_errors](structnet__stats__eth__errors.md#a0043d1a1481040a6d7439bd23423ec12)

net\_stats\_t tx\_carrier\_errors

Number of TX carrier errors.

**Definition** net\_stats.h:468

[net\_stats\_eth\_errors::uncorr\_ecc\_errors](structnet__stats__eth__errors.md#a07d0a435f2129556520c732571d28edf)

net\_stats\_t uncorr\_ecc\_errors

Number of uncorrected ECC errors.

**Definition** net\_stats.h:483

[net\_stats\_eth\_errors::rx\_long\_length\_errors](structnet__stats__eth__errors.md#a0e83e270a35222ed3e927800be4159e7)

net\_stats\_t rx\_long\_length\_errors

Number of RX long length errors.

**Definition** net\_stats.h:450

[net\_stats\_eth\_errors::tx\_window\_errors](structnet__stats__eth__errors.md#a17624a12d6473bdd78698076fed0d122)

net\_stats\_t tx\_window\_errors

Number of TX window errors.

**Definition** net\_stats.h:477

[net\_stats\_eth\_errors::corr\_ecc\_errors](structnet__stats__eth__errors.md#a257113639f0e0e3085febb7a147f498f)

net\_stats\_t corr\_ecc\_errors

Number of corrected ECC errors.

**Definition** net\_stats.h:486

[net\_stats\_eth\_errors::rx\_missed\_errors](structnet__stats__eth__errors.md#a2d2b2c4e3764ebec841f1ecbe7058d99)

net\_stats\_t rx\_missed\_errors

Number of RX missed errors.

**Definition** net\_stats.h:447

[net\_stats\_eth\_errors::rx\_crc\_errors](structnet__stats__eth__errors.md#a4dab70cf219269bb393ce14faf0ed77e)

net\_stats\_t rx\_crc\_errors

Number of RX CRC errors.

**Definition** net\_stats.h:438

[net\_stats\_eth\_errors::rx\_short\_length\_errors](structnet__stats__eth__errors.md#a5e3d39d8417bb180cbfcb8c901006e81)

net\_stats\_t rx\_short\_length\_errors

Number of RX short length errors.

**Definition** net\_stats.h:453

[net\_stats\_eth\_errors::rx\_align\_errors](structnet__stats__eth__errors.md#a7618f10af3443c49a6e256bb41e77781)

net\_stats\_t rx\_align\_errors

Number of RX buffer align errors.

**Definition** net\_stats.h:456

[net\_stats\_eth\_errors::rx\_dma\_failed](structnet__stats__eth__errors.md#a7bcfbb13836f162ceeb5f021304b5c76)

net\_stats\_t rx\_dma\_failed

Number of RX DMA failed errors.

**Definition** net\_stats.h:459

[net\_stats\_eth\_errors::rx\_no\_buffer\_count](structnet__stats__eth__errors.md#a82622736d226b4d3b999f1f22ccf8529)

net\_stats\_t rx\_no\_buffer\_count

Number of RX net\_pkt allocation errors.

**Definition** net\_stats.h:444

[net\_stats\_eth\_errors::tx\_fifo\_errors](structnet__stats__eth__errors.md#a84630da9b82557f56dc35cd59ca2f7ae)

net\_stats\_t tx\_fifo\_errors

Number of TX FIFO errors.

**Definition** net\_stats.h:471

[net\_stats\_eth\_errors::rx\_frame\_errors](structnet__stats__eth__errors.md#a8dfcc5cd1b4decec5783d01ba7033b05)

net\_stats\_t rx\_frame\_errors

Number of RX frame errors.

**Definition** net\_stats.h:441

[net\_stats\_eth\_errors::rx\_over\_errors](structnet__stats__eth__errors.md#a9afee89f5bb01907e7cd515e2a0ff1b5)

net\_stats\_t rx\_over\_errors

Number of RX overrun errors.

**Definition** net\_stats.h:435

[net\_stats\_eth\_errors::tx\_dma\_failed](structnet__stats__eth__errors.md#abfbf6478b7afdd5935d7c6948c9ef426)

net\_stats\_t tx\_dma\_failed

Number of TX DMA failed errors.

**Definition** net\_stats.h:480

[net\_stats\_eth\_errors::rx\_length\_errors](structnet__stats__eth__errors.md#aca0e2e4807fa70279dee8ddaad2d7ef7)

net\_stats\_t rx\_length\_errors

Number of RX length errors.

**Definition** net\_stats.h:432

[net\_stats\_eth\_errors::rx\_buf\_alloc\_failed](structnet__stats__eth__errors.md#adbcae9c10c081f1cdf304bcdce740aa4)

net\_stats\_t rx\_buf\_alloc\_failed

Number of RX net\_buf allocation errors.

**Definition** net\_stats.h:462

[net\_stats\_eth\_errors::tx\_heartbeat\_errors](structnet__stats__eth__errors.md#ae2a13733c1a5f0cc3e00efca0c3f429d)

net\_stats\_t tx\_heartbeat\_errors

Number of TX heartbeat errors.

**Definition** net\_stats.h:474

[net\_stats\_eth\_errors::tx\_aborted\_errors](structnet__stats__eth__errors.md#afec6a7e24c6f3cc74dd9f739f27b3e48)

net\_stats\_t tx\_aborted\_errors

Number of TX aborted errors.

**Definition** net\_stats.h:465

[net\_stats\_eth\_flow](structnet__stats__eth__flow.md)

Ethernet flow control statistics.

**Definition** net\_stats.h:492

[net\_stats\_eth\_flow::rx\_flow\_control\_xon](structnet__stats__eth__flow.md#a08e5da4ff78fe3893b9c9a628cefe4f2)

net\_stats\_t rx\_flow\_control\_xon

Number of RX XON flow control.

**Definition** net\_stats.h:494

[net\_stats\_eth\_flow::tx\_flow\_control\_xon](structnet__stats__eth__flow.md#a31412e8bf9d38ba630ea856e958a48d7)

net\_stats\_t tx\_flow\_control\_xon

Number of TX XON flow control.

**Definition** net\_stats.h:500

[net\_stats\_eth\_flow::rx\_flow\_control\_xoff](structnet__stats__eth__flow.md#a8f9b93537b3c11be70f276aaa72cb637)

net\_stats\_t rx\_flow\_control\_xoff

Number of RX XOFF flow control.

**Definition** net\_stats.h:497

[net\_stats\_eth\_flow::tx\_flow\_control\_xoff](structnet__stats__eth__flow.md#a969d81f9db20312d2d2aa7f70f93bdd5)

net\_stats\_t tx\_flow\_control\_xoff

Number of TX XOFF flow control.

**Definition** net\_stats.h:503

[net\_stats\_eth\_hw\_timestamp](structnet__stats__eth__hw__timestamp.md)

Ethernet hardware timestamp statistics.

**Definition** net\_stats.h:520

[net\_stats\_eth\_hw\_timestamp::tx\_hwtstamp\_timeouts](structnet__stats__eth__hw__timestamp.md#a41f605499dbf88a879522fdfa4633d9e)

net\_stats\_t tx\_hwtstamp\_timeouts

Number of RX hardware timestamp timeout.

**Definition** net\_stats.h:525

[net\_stats\_eth\_hw\_timestamp::rx\_hwtstamp\_cleared](structnet__stats__eth__hw__timestamp.md#acd3d5f72d7df568110d96093e0c9534d)

net\_stats\_t rx\_hwtstamp\_cleared

Number of RX hardware timestamp cleared.

**Definition** net\_stats.h:522

[net\_stats\_eth\_hw\_timestamp::tx\_hwtstamp\_skipped](structnet__stats__eth__hw__timestamp.md#ae1f983faf4a999308c464e4af5a5284b)

net\_stats\_t tx\_hwtstamp\_skipped

Number of RX hardware timestamp skipped.

**Definition** net\_stats.h:528

[net\_stats\_eth](structnet__stats__eth.md)

All Ethernet specific statistics.

**Definition** net\_stats.h:544

[net\_stats\_eth::broadcast](structnet__stats__eth.md#a054beb909134b0e0f22f5df599549128)

struct net\_stats\_pkts broadcast

Total number of broadcast packets received and sent.

**Definition** net\_stats.h:552

[net\_stats\_eth::csum](structnet__stats__eth.md#a2169ae06bace1a93663bccf88c8d7a29)

struct net\_stats\_eth\_csum csum

Total number of checksum errors in RX and TX.

**Definition** net\_stats.h:567

[net\_stats\_eth::tx\_dropped](structnet__stats__eth.md#a257c349cf3d32d38796e3899e702454a)

net\_stats\_t tx\_dropped

Total number of dropped TX packets.

**Definition** net\_stats.h:576

[net\_stats\_eth::hw\_timestamp](structnet__stats__eth.md#a44667efff73c17c089ed22d5b0da5ad3)

struct net\_stats\_eth\_hw\_timestamp hw\_timestamp

Total number of hardware timestamp errors in RX and TX.

**Definition** net\_stats.h:570

[net\_stats\_eth::multicast](structnet__stats__eth.md#a4f6a2903330518a132e7e547820e0bf2)

struct net\_stats\_pkts multicast

Total number of multicast packets received and sent.

**Definition** net\_stats.h:555

[net\_stats\_eth::flow\_control](structnet__stats__eth.md#a643010ac6360c8c0c08016725ba12222)

struct net\_stats\_eth\_flow flow\_control

Total number of flow control errors in RX and TX.

**Definition** net\_stats.h:564

[net\_stats\_eth::tx\_restart\_queue](structnet__stats__eth.md#a6699012226e25e8bad39076fed6dbfb5)

net\_stats\_t tx\_restart\_queue

Total number of TX queue restarts.

**Definition** net\_stats.h:582

[net\_stats\_eth::collisions](structnet__stats__eth.md#a822d4205791f59999c842610522f6fc5)

net\_stats\_t collisions

Total number of collisions.

**Definition** net\_stats.h:573

[net\_stats\_eth::bytes](structnet__stats__eth.md#a8c5cf1ead8ba214425a16fed1c2ad0fb)

struct net\_stats\_bytes bytes

Total number of bytes received and sent.

**Definition** net\_stats.h:546

[net\_stats\_eth::error\_details](structnet__stats__eth.md#a922feddb17fc020371f1bcc52c709415)

struct net\_stats\_eth\_errors error\_details

Total number of errors in RX and TX.

**Definition** net\_stats.h:561

[net\_stats\_eth::pkts](structnet__stats__eth.md#a97bd6026b16890743f344751a21107f1)

struct net\_stats\_pkts pkts

Total number of packets received and sent.

**Definition** net\_stats.h:549

[net\_stats\_eth::errors](structnet__stats__eth.md#a9c869740f416fbe0b54d7fefacb1fe29)

struct net\_stats\_pkts errors

Total number of errors in RX and TX.

**Definition** net\_stats.h:558

[net\_stats\_eth::tx\_timeout\_count](structnet__stats__eth.md#ab351258ae82abd09759d37774559d8bc)

net\_stats\_t tx\_timeout\_count

Total number of TX timeout errors.

**Definition** net\_stats.h:579

[net\_stats\_eth::unknown\_protocol](structnet__stats__eth.md#afaacee7cc1d0a35ae2344175421c40dd)

net\_stats\_t unknown\_protocol

Total number of RX unknown protocol packets.

**Definition** net\_stats.h:585

[net\_stats\_icmp](structnet__stats__icmp.md)

ICMP statistics.

**Definition** net\_stats.h:107

[net\_stats\_icmp::sent](structnet__stats__icmp.md#a2d6eb7dfc8f4b439b399b039022f2889)

net\_stats\_t sent

Number of sent ICMP packets.

**Definition** net\_stats.h:112

[net\_stats\_icmp::chkerr](structnet__stats__icmp.md#a6662bc547107a08c52e902a2446629bf)

net\_stats\_t chkerr

Number of ICMP packets with a bad checksum.

**Definition** net\_stats.h:121

[net\_stats\_icmp::drop](structnet__stats__icmp.md#a755f3388c05d4bd2988ddd16d1a4cf32)

net\_stats\_t drop

Number of dropped ICMP packets.

**Definition** net\_stats.h:115

[net\_stats\_icmp::typeerr](structnet__stats__icmp.md#ae1a29dd9b8e1ce9a737fa7f36c805cd4)

net\_stats\_t typeerr

Number of ICMP packets with a wrong type.

**Definition** net\_stats.h:118

[net\_stats\_icmp::recv](structnet__stats__icmp.md#ae6f226b55565c11fca0c9e099f08c267)

net\_stats\_t recv

Number of received ICMP packets.

**Definition** net\_stats.h:109

[net\_stats\_ip\_errors](structnet__stats__ip__errors.md)

IP layer error statistics.

**Definition** net\_stats.h:80

[net\_stats\_ip\_errors::hblenerr](structnet__stats__ip__errors.md#a06b35742c418ebc6414fcb5c7002edde)

net\_stats\_t hblenerr

Number of packets dropped due to wrong IP length, high byte.

**Definition** net\_stats.h:87

[net\_stats\_ip\_errors::vhlerr](structnet__stats__ip__errors.md#a3e476f659ebeaa5c5f7b6dad2d90326f)

net\_stats\_t vhlerr

Number of packets dropped due to wrong IP version or header length.

**Definition** net\_stats.h:84

[net\_stats\_ip\_errors::chkerr](structnet__stats__ip__errors.md#a872cc0beca45bbe87ae794dd8ca4e301)

net\_stats\_t chkerr

Number of packets dropped due to IP checksum errors.

**Definition** net\_stats.h:96

[net\_stats\_ip\_errors::protoerr](structnet__stats__ip__errors.md#a978b1c23847e707ac1fa27c2b34fa85d)

net\_stats\_t protoerr

Number of packets dropped because they were neither ICMP, UDP nor TCP.

**Definition** net\_stats.h:101

[net\_stats\_ip\_errors::lblenerr](structnet__stats__ip__errors.md#a9b4bf05e9df13e1d99518125b9067bef)

net\_stats\_t lblenerr

Number of packets dropped due to wrong IP length, low byte.

**Definition** net\_stats.h:90

[net\_stats\_ip\_errors::fragerr](structnet__stats__ip__errors.md#ab84ee9dfbe5da391d60c6e3ae9abea16)

net\_stats\_t fragerr

Number of packets dropped because they were IP fragments.

**Definition** net\_stats.h:93

[net\_stats\_ip](structnet__stats__ip.md)

IP layer statistics.

**Definition** net\_stats.h:63

[net\_stats\_ip::forwarded](structnet__stats__ip.md#a4bb82a5ebebaa3e8a11973c07eed96a0)

net\_stats\_t forwarded

Number of forwarded packets at the IP layer.

**Definition** net\_stats.h:71

[net\_stats\_ip::recv](structnet__stats__ip.md#ab6a6373368dd24cb51504c5729d535d3)

net\_stats\_t recv

Number of received packets at the IP layer.

**Definition** net\_stats.h:65

[net\_stats\_ip::sent](structnet__stats__ip.md#abbe676bbe9faa89b2b6b8c4950b1c9d5)

net\_stats\_t sent

Number of sent packets at the IP layer.

**Definition** net\_stats.h:68

[net\_stats\_ip::drop](structnet__stats__ip.md#ac86399b70d7f761162e5336dd15589eb)

net\_stats\_t drop

Number of dropped packets at the IP layer.

**Definition** net\_stats.h:74

[net\_stats\_ipv4\_igmp](structnet__stats__ipv4__igmp.md)

IPv4 IGMP daemon statistics.

**Definition** net\_stats.h:218

[net\_stats\_ipv4\_igmp::drop](structnet__stats__ipv4__igmp.md#a1c37702ff837b8c5cc9df5f690e7678c)

net\_stats\_t drop

Number of dropped IPv4 IGMP packets.

**Definition** net\_stats.h:226

[net\_stats\_ipv4\_igmp::recv](structnet__stats__ipv4__igmp.md#a469113de7af0ba42dbd1b0365d00602c)

net\_stats\_t recv

Number of received IPv4 IGMP queries.

**Definition** net\_stats.h:220

[net\_stats\_ipv4\_igmp::sent](structnet__stats__ipv4__igmp.md#a955e20a6ee5e19e08000b3114b9d71a6)

net\_stats\_t sent

Number of sent IPv4 IGMP reports.

**Definition** net\_stats.h:223

[net\_stats\_ipv6\_mld](structnet__stats__ipv6__mld.md)

IPv6 multicast listener daemon statistics.

**Definition** net\_stats.h:204

[net\_stats\_ipv6\_mld::recv](structnet__stats__ipv6__mld.md#a4879ff9e31f8b60973d3b169598e921d)

net\_stats\_t recv

Number of received IPv6 MLD queries.

**Definition** net\_stats.h:206

[net\_stats\_ipv6\_mld::sent](structnet__stats__ipv6__mld.md#ab397b74b14ce7047bf2fc63ca72ce1e5)

net\_stats\_t sent

Number of sent IPv6 MLD reports.

**Definition** net\_stats.h:209

[net\_stats\_ipv6\_mld::drop](structnet__stats__ipv6__mld.md#ad85dc87f57296a1e7d64e959b0370ee8)

net\_stats\_t drop

Number of dropped IPv6 MLD packets.

**Definition** net\_stats.h:212

[net\_stats\_ipv6\_nd](structnet__stats__ipv6__nd.md)

IPv6 neighbor discovery statistics.

**Definition** net\_stats.h:190

[net\_stats\_ipv6\_nd::sent](structnet__stats__ipv6__nd.md#a0129f7892a4439c20deb2f32b9001277)

net\_stats\_t sent

Number of sent IPv6 neighbor discovery packets.

**Definition** net\_stats.h:198

[net\_stats\_ipv6\_nd::recv](structnet__stats__ipv6__nd.md#a0bf6f67d9112996a3b002ea160aec769)

net\_stats\_t recv

Number of received IPv6 neighbor discovery packets.

**Definition** net\_stats.h:195

[net\_stats\_ipv6\_nd::drop](structnet__stats__ipv6__nd.md#a31074d5d44138fcabdc5f7750f9f2c47)

net\_stats\_t drop

Number of dropped IPv6 neighbor discovery packets.

**Definition** net\_stats.h:192

[net\_stats\_pkts](structnet__stats__pkts.md)

Number of network packets sent and received.

**Definition** net\_stats.h:53

[net\_stats\_pkts::rx](structnet__stats__pkts.md#ac9784b5a245e6c57e39318aaf314f0cf)

net\_stats\_t rx

Number of packets received.

**Definition** net\_stats.h:57

[net\_stats\_pkts::tx](structnet__stats__pkts.md#aee1e302d0f8dac79b693a06d8fa3b3c5)

net\_stats\_t tx

Number of packets sent.

**Definition** net\_stats.h:55

[net\_stats\_pm](structnet__stats__pm.md)

Power management statistics.

**Definition** net\_stats.h:324

[net\_stats\_pm::last\_suspend\_time](structnet__stats__pm.md#a0bdf9c3676298e2df4ff3bfa03f5e823)

uint32\_t last\_suspend\_time

How long the last suspend took.

**Definition** net\_stats.h:330

[net\_stats\_pm::start\_time](structnet__stats__pm.md#a6784806eaa093431ed3c0f7acfe5a89c)

uint32\_t start\_time

Network interface last suspend start time.

**Definition** net\_stats.h:332

[net\_stats\_pm::overall\_suspend\_time](structnet__stats__pm.md#ab43935fcfe9efc1cd5f3e7e329996805)

uint64\_t overall\_suspend\_time

Total suspend time.

**Definition** net\_stats.h:326

[net\_stats\_pm::suspend\_count](structnet__stats__pm.md#ac14122a4765c499c045f18c70af355a0)

net\_stats\_t suspend\_count

How many times we were suspended.

**Definition** net\_stats.h:328

[net\_stats\_ppp](structnet__stats__ppp.md)

All PPP specific statistics.

**Definition** net\_stats.h:596

[net\_stats\_ppp::chkerr](structnet__stats__ppp.md#a1332b31980f82236aeb0c3f9444e2ac6)

net\_stats\_t chkerr

Number of received PPP frames with a bad checksum.

**Definition** net\_stats.h:607

[net\_stats\_ppp::pkts](structnet__stats__ppp.md#a71fc81f3c5f3e65a476b3391f086d340)

struct net\_stats\_pkts pkts

Total number of packets received and sent.

**Definition** net\_stats.h:601

[net\_stats\_ppp::bytes](structnet__stats__ppp.md#ab2b48da7f19d4b83e3f41b41979b7ed8)

struct net\_stats\_bytes bytes

Total number of bytes received and sent.

**Definition** net\_stats.h:598

[net\_stats\_ppp::drop](structnet__stats__ppp.md#ae2e0a47a539e9d7bc97f9c63f889b276)

net\_stats\_t drop

Number of received and dropped PPP frames.

**Definition** net\_stats.h:604

[net\_stats\_rx\_time](structnet__stats__rx__time.md)

Network packet receive times for calculating average RX time.

**Definition** net\_stats.h:257

[net\_stats\_rx\_time::sum](structnet__stats__rx__time.md#a4b84c2ae2fda8fcd75fdf1bf0b2aae8d)

uint64\_t sum

Sum of network packet receive times.

**Definition** net\_stats.h:259

[net\_stats\_rx\_time::count](structnet__stats__rx__time.md#a68247051b064de081fa2e84118192958)

net\_stats\_t count

Number of network packets received.

**Definition** net\_stats.h:262

[net\_stats\_sta\_mgmt](structnet__stats__sta__mgmt.md)

All Wi-Fi management statistics.

**Definition** net\_stats.h:613

[net\_stats\_sta\_mgmt::beacons\_miss](structnet__stats__sta__mgmt.md#a29ae0079b4c780e0de2656a85ec15fe9)

net\_stats\_t beacons\_miss

Number of missed beacons.

**Definition** net\_stats.h:618

[net\_stats\_sta\_mgmt::beacons\_rx](structnet__stats__sta__mgmt.md#ac6e68fded8e19b20259442436923f815)

net\_stats\_t beacons\_rx

Number of received beacons.

**Definition** net\_stats.h:615

[net\_stats\_tc](structnet__stats__tc.md)

Traffic class statistics.

**Definition** net\_stats.h:284

[net\_stats\_tc::bytes](structnet__stats__tc.md#a192a7ec0d24bce9e62f766e481ee5709)

net\_stats\_t bytes

Number of bytes sent for this traffic class.

**Definition** net\_stats.h:297

[net\_stats\_tc::tx\_time](structnet__stats__tc.md#a30288ef3bb0796cd18c3cf0aedbe875a)

struct net\_stats\_tx\_time tx\_time

Helper for calculating average TX time statistics.

**Definition** net\_stats.h:288

[net\_stats\_tc::pkts](structnet__stats__tc.md#a6614b5f5186635415a7d787260c39248)

net\_stats\_t pkts

Number of packets sent for this traffic class.

**Definition** net\_stats.h:295

[net\_stats\_tc::priority](structnet__stats__tc.md#a8a5c2e59990407ddbfc7973a1c183bf6)

uint8\_t priority

Priority of this traffic class.

**Definition** net\_stats.h:299

[net\_stats\_tc::sent](structnet__stats__tc.md#a8d6a3ebcc49ce8c34a5faae986f648e2)

struct net\_stats\_tc::@074155214116325077102236356156227241054306002026 sent[NET\_TC\_TX\_STATS\_COUNT]

TX statistics for each traffic class.

[net\_stats\_tc::rx\_time](structnet__stats__tc.md#a8ea00824bb0fb18e4d8912343e01c3b7)

struct net\_stats\_rx\_time rx\_time

Helper for calculating average RX time statistics.

**Definition** net\_stats.h:305

[net\_stats\_tcp](structnet__stats__tcp.md)

TCP statistics.

**Definition** net\_stats.h:127

[net\_stats\_tcp::ackerr](structnet__stats__tcp.md#a0d40abc85776f0a9b9510a909b7f6d18)

net\_stats\_t ackerr

Number of received TCP segments with a bad ACK number.

**Definition** net\_stats.h:150

[net\_stats\_tcp::rsterr](structnet__stats__tcp.md#a471fcd5578f79ce77d20547b28503ac1)

net\_stats\_t rsterr

Number of received bad TCP RST (reset) segments.

**Definition** net\_stats.h:153

[net\_stats\_tcp::rexmit](structnet__stats__tcp.md#a4a4ea6e5d87ef58b4271bd708cf39635)

net\_stats\_t rexmit

Number of retransmitted TCP segments.

**Definition** net\_stats.h:159

[net\_stats\_tcp::chkerr](structnet__stats__tcp.md#a5099e174b0eafa322f0630f1f5c73a8b)

net\_stats\_t chkerr

Number of TCP segments with a bad checksum.

**Definition** net\_stats.h:147

[net\_stats\_tcp::seg\_drop](structnet__stats__tcp.md#a5f045704859331918511e9c2281ac155)

net\_stats\_t seg\_drop

Number of dropped TCP segments.

**Definition** net\_stats.h:144

[net\_stats\_tcp::connrst](structnet__stats__tcp.md#a67f55954a4c51f2b957c7d974e78c1c0)

net\_stats\_t connrst

Number of connection attempts for closed ports, triggering a RST.

**Definition** net\_stats.h:167

[net\_stats\_tcp::drop](structnet__stats__tcp.md#aa549f7b6d5828009a09190fd64afa8e3)

net\_stats\_t drop

Number of dropped packets at the TCP layer.

**Definition** net\_stats.h:135

[net\_stats\_tcp::rst](structnet__stats__tcp.md#aa618cf86b962aca0f14eb9178c8ae61a)

net\_stats\_t rst

Number of received TCP RST (reset) segments.

**Definition** net\_stats.h:156

[net\_stats\_tcp::sent](structnet__stats__tcp.md#aa987bebf96000b6b4e92bfafc218759a)

net\_stats\_t sent

Number of sent TCP segments.

**Definition** net\_stats.h:141

[net\_stats\_tcp::resent](structnet__stats__tcp.md#abe567032cb4a267a984aec28c1e3cca4)

net\_stats\_t resent

Amount of retransmitted data.

**Definition** net\_stats.h:132

[net\_stats\_tcp::conndrop](structnet__stats__tcp.md#ac557ac0d8917bc2c2dfed74126f993c8)

net\_stats\_t conndrop

Number of dropped connection attempts because too few connections were available.

**Definition** net\_stats.h:164

[net\_stats\_tcp::recv](structnet__stats__tcp.md#ad25edb2b39a6acc8152c35ad43a5042f)

net\_stats\_t recv

Number of received TCP segments.

**Definition** net\_stats.h:138

[net\_stats\_tcp::bytes](structnet__stats__tcp.md#af80c18bcc253133ce5f0597ac190b349)

struct net\_stats\_bytes bytes

Amount of received and sent TCP application data.

**Definition** net\_stats.h:129

[net\_stats\_tx\_time](structnet__stats__tx__time.md)

Network packet transfer times for calculating average TX time.

**Definition** net\_stats.h:246

[net\_stats\_tx\_time::count](structnet__stats__tx__time.md#a7a652350ed04e53ba02aec294f8444b4)

net\_stats\_t count

Number of network packets transferred.

**Definition** net\_stats.h:251

[net\_stats\_tx\_time::sum](structnet__stats__tx__time.md#af6f7a26c0344a0f93306e105a8917c3e)

uint64\_t sum

Sum of network packet transfer times.

**Definition** net\_stats.h:248

[net\_stats\_udp](structnet__stats__udp.md)

UDP statistics.

**Definition** net\_stats.h:173

[net\_stats\_udp::recv](structnet__stats__udp.md#a0ea91d85fe322661fb909f5e94e55a34)

net\_stats\_t recv

Number of received UDP segments.

**Definition** net\_stats.h:178

[net\_stats\_udp::drop](structnet__stats__udp.md#a2d884bf9106e60d430ffec7c7964a609)

net\_stats\_t drop

Number of dropped UDP segments.

**Definition** net\_stats.h:175

[net\_stats\_udp::chkerr](structnet__stats__udp.md#a4c57d5f68ebda7981400729b9c7fe0f7)

net\_stats\_t chkerr

Number of UDP segments with a bad checksum.

**Definition** net\_stats.h:184

[net\_stats\_udp::sent](structnet__stats__udp.md#ab4e8228c221901d3ded55f3f823bfa1c)

net\_stats\_t sent

Number of sent UDP segments.

**Definition** net\_stats.h:181

[net\_stats\_wifi](structnet__stats__wifi.md)

All Wi-Fi specific statistics.

**Definition** net\_stats.h:624

[net\_stats\_wifi::broadcast](structnet__stats__wifi.md#a03dc04638c4b670bd7f3520d45fc1eda)

struct net\_stats\_pkts broadcast

Total number of broadcast packets received and sent.

**Definition** net\_stats.h:635

[net\_stats\_wifi::multicast](structnet__stats__wifi.md#a7e7f68215101885fd51c70e981da26e7)

struct net\_stats\_pkts multicast

Total number of multicast packets received and sent.

**Definition** net\_stats.h:638

[net\_stats\_wifi::sta\_mgmt](structnet__stats__wifi.md#a8bee22961545674e6ab100b58a04bf91)

struct net\_stats\_sta\_mgmt sta\_mgmt

Total number of beacon errors.

**Definition** net\_stats.h:626

[net\_stats\_wifi::bytes](structnet__stats__wifi.md#aa055b1e8bd8f1e50815c1028b562be07)

struct net\_stats\_bytes bytes

Total number of bytes received and sent.

**Definition** net\_stats.h:629

[net\_stats\_wifi::overrun\_count](structnet__stats__wifi.md#ac498c9e517f2cb2eb01d251e84159e7e)

net\_stats\_t overrun\_count

Total number of dropped packets at received and sent.

**Definition** net\_stats.h:647

[net\_stats\_wifi::pkts](structnet__stats__wifi.md#adbcdb2dd8733f2917c00a0b2d365393b)

struct net\_stats\_pkts pkts

Total number of packets received and sent.

**Definition** net\_stats.h:632

[net\_stats\_wifi::errors](structnet__stats__wifi.md#ae0149e64a94a9f96eb6680f94793c8c4)

struct net\_stats\_pkts errors

Total number of errors in RX and TX.

**Definition** net\_stats.h:641

[net\_stats\_wifi::unicast](structnet__stats__wifi.md#ae80dcd73a3c5ce3ec3282d1ae827b338)

struct net\_stats\_pkts unicast

Total number of unicast packets received and sent.

**Definition** net\_stats.h:644

[net\_stats](structnet__stats.md)

All network statistics in one struct.

**Definition** net\_stats.h:339

[net\_stats::processing\_error](structnet__stats.md#a3a4c90661d6b310b628262228a341fe2)

net\_stats\_t processing\_error

Count of malformed packets or packets we do not have handler for.

**Definition** net\_stats.h:341

[net\_stats::bytes](structnet__stats.md#a7a28233e6d23efdce0143469b9bb6c05)

struct net\_stats\_bytes bytes

This calculates amount of data transferred through all the network interfaces.

**Definition** net\_stats.h:347

[net\_stats::ip\_errors](structnet__stats.md#ac42cb13954d164e92a1ef60919a2a34e)

struct net\_stats\_ip\_errors ip\_errors

IP layer errors.

**Definition** net\_stats.h:350

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [net\_stats.h](net__stats_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
