---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/net__stats_8h_source.html
original_path: doxygen/html/net__stats_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
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

21#include <[zephyr/net/prometheus/collector.h](collector_8h.md)>

22#include <[zephyr/net/prometheus/counter.h](net_2prometheus_2counter_8h.md)>

23#include <[zephyr/net/prometheus/metric.h](metric_8h.md)>

24#include <[zephyr/net/prometheus/gauge.h](gauge_8h.md)>

25#include <[zephyr/net/prometheus/histogram.h](histogram_8h.md)>

26#include <[zephyr/net/prometheus/summary.h](summary_8h.md)>

27

28#ifdef \_\_cplusplus

29extern "C" {

30#endif

31

40

[ 45](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752)typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752);

46

[ 50](structnet__stats__bytes.md)struct [net\_stats\_bytes](structnet__stats__bytes.md) {

[ 52](structnet__stats__bytes.md#a360bdbf177d60b0677beec2037f34cb0) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [sent](structnet__stats__bytes.md#a360bdbf177d60b0677beec2037f34cb0);

[ 54](structnet__stats__bytes.md#a9f87e32d63bc4239ef7db03feedd495e) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [received](structnet__stats__bytes.md#a9f87e32d63bc4239ef7db03feedd495e);

55};

56

[ 60](structnet__stats__pkts.md)struct [net\_stats\_pkts](structnet__stats__pkts.md) {

[ 62](structnet__stats__pkts.md#aee1e302d0f8dac79b693a06d8fa3b3c5) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [tx](structnet__stats__pkts.md#aee1e302d0f8dac79b693a06d8fa3b3c5);

[ 64](structnet__stats__pkts.md#ac9784b5a245e6c57e39318aaf314f0cf) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [rx](structnet__stats__pkts.md#ac9784b5a245e6c57e39318aaf314f0cf);

65};

66

[ 70](structnet__stats__ip.md)struct [net\_stats\_ip](structnet__stats__ip.md) {

[ 72](structnet__stats__ip.md#ab6a6373368dd24cb51504c5729d535d3) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [recv](structnet__stats__ip.md#ab6a6373368dd24cb51504c5729d535d3);

73

[ 75](structnet__stats__ip.md#abbe676bbe9faa89b2b6b8c4950b1c9d5) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [sent](structnet__stats__ip.md#abbe676bbe9faa89b2b6b8c4950b1c9d5);

76

[ 78](structnet__stats__ip.md#a4bb82a5ebebaa3e8a11973c07eed96a0) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [forwarded](structnet__stats__ip.md#a4bb82a5ebebaa3e8a11973c07eed96a0);

79

[ 81](structnet__stats__ip.md#ac86399b70d7f761162e5336dd15589eb) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [drop](structnet__stats__ip.md#ac86399b70d7f761162e5336dd15589eb);

82};

83

[ 87](structnet__stats__ip__errors.md)struct [net\_stats\_ip\_errors](structnet__stats__ip__errors.md) {

[ 91](structnet__stats__ip__errors.md#a3e476f659ebeaa5c5f7b6dad2d90326f) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [vhlerr](structnet__stats__ip__errors.md#a3e476f659ebeaa5c5f7b6dad2d90326f);

92

[ 94](structnet__stats__ip__errors.md#a06b35742c418ebc6414fcb5c7002edde) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [hblenerr](structnet__stats__ip__errors.md#a06b35742c418ebc6414fcb5c7002edde);

95

[ 97](structnet__stats__ip__errors.md#a9b4bf05e9df13e1d99518125b9067bef) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [lblenerr](structnet__stats__ip__errors.md#a9b4bf05e9df13e1d99518125b9067bef);

98

[ 100](structnet__stats__ip__errors.md#ab84ee9dfbe5da391d60c6e3ae9abea16) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [fragerr](structnet__stats__ip__errors.md#ab84ee9dfbe5da391d60c6e3ae9abea16);

101

[ 103](structnet__stats__ip__errors.md#a872cc0beca45bbe87ae794dd8ca4e301) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [chkerr](structnet__stats__ip__errors.md#a872cc0beca45bbe87ae794dd8ca4e301);

104

[ 108](structnet__stats__ip__errors.md#a978b1c23847e707ac1fa27c2b34fa85d) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [protoerr](structnet__stats__ip__errors.md#a978b1c23847e707ac1fa27c2b34fa85d);

109};

110

[ 114](structnet__stats__icmp.md)struct [net\_stats\_icmp](structnet__stats__icmp.md) {

[ 116](structnet__stats__icmp.md#ae6f226b55565c11fca0c9e099f08c267) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [recv](structnet__stats__icmp.md#ae6f226b55565c11fca0c9e099f08c267);

117

[ 119](structnet__stats__icmp.md#a2d6eb7dfc8f4b439b399b039022f2889) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [sent](structnet__stats__icmp.md#a2d6eb7dfc8f4b439b399b039022f2889);

120

[ 122](structnet__stats__icmp.md#a755f3388c05d4bd2988ddd16d1a4cf32) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [drop](structnet__stats__icmp.md#a755f3388c05d4bd2988ddd16d1a4cf32);

123

[ 125](structnet__stats__icmp.md#ae1a29dd9b8e1ce9a737fa7f36c805cd4) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [typeerr](structnet__stats__icmp.md#ae1a29dd9b8e1ce9a737fa7f36c805cd4);

126

[ 128](structnet__stats__icmp.md#a6662bc547107a08c52e902a2446629bf) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [chkerr](structnet__stats__icmp.md#a6662bc547107a08c52e902a2446629bf);

129};

130

[ 134](structnet__stats__tcp.md)struct [net\_stats\_tcp](structnet__stats__tcp.md) {

[ 136](structnet__stats__tcp.md#af80c18bcc253133ce5f0597ac190b349) struct [net\_stats\_bytes](structnet__stats__bytes.md) [bytes](structnet__stats__tcp.md#af80c18bcc253133ce5f0597ac190b349);

137

[ 139](structnet__stats__tcp.md#abe567032cb4a267a984aec28c1e3cca4) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [resent](structnet__stats__tcp.md#abe567032cb4a267a984aec28c1e3cca4);

140

[ 142](structnet__stats__tcp.md#aa549f7b6d5828009a09190fd64afa8e3) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [drop](structnet__stats__tcp.md#aa549f7b6d5828009a09190fd64afa8e3);

143

[ 145](structnet__stats__tcp.md#ad25edb2b39a6acc8152c35ad43a5042f) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [recv](structnet__stats__tcp.md#ad25edb2b39a6acc8152c35ad43a5042f);

146

[ 148](structnet__stats__tcp.md#aa987bebf96000b6b4e92bfafc218759a) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [sent](structnet__stats__tcp.md#aa987bebf96000b6b4e92bfafc218759a);

149

[ 151](structnet__stats__tcp.md#a5f045704859331918511e9c2281ac155) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [seg\_drop](structnet__stats__tcp.md#a5f045704859331918511e9c2281ac155);

152

[ 154](structnet__stats__tcp.md#a5099e174b0eafa322f0630f1f5c73a8b) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [chkerr](structnet__stats__tcp.md#a5099e174b0eafa322f0630f1f5c73a8b);

155

[ 157](structnet__stats__tcp.md#a0d40abc85776f0a9b9510a909b7f6d18) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [ackerr](structnet__stats__tcp.md#a0d40abc85776f0a9b9510a909b7f6d18);

158

[ 160](structnet__stats__tcp.md#a471fcd5578f79ce77d20547b28503ac1) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [rsterr](structnet__stats__tcp.md#a471fcd5578f79ce77d20547b28503ac1);

161

[ 163](structnet__stats__tcp.md#aa618cf86b962aca0f14eb9178c8ae61a) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [rst](structnet__stats__tcp.md#aa618cf86b962aca0f14eb9178c8ae61a);

164

[ 166](structnet__stats__tcp.md#a4a4ea6e5d87ef58b4271bd708cf39635) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [rexmit](structnet__stats__tcp.md#a4a4ea6e5d87ef58b4271bd708cf39635);

167

[ 171](structnet__stats__tcp.md#ac557ac0d8917bc2c2dfed74126f993c8) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [conndrop](structnet__stats__tcp.md#ac557ac0d8917bc2c2dfed74126f993c8);

172

[ 174](structnet__stats__tcp.md#a67f55954a4c51f2b957c7d974e78c1c0) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [connrst](structnet__stats__tcp.md#a67f55954a4c51f2b957c7d974e78c1c0);

175};

176

[ 180](structnet__stats__udp.md)struct [net\_stats\_udp](structnet__stats__udp.md) {

[ 182](structnet__stats__udp.md#a2d884bf9106e60d430ffec7c7964a609) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [drop](structnet__stats__udp.md#a2d884bf9106e60d430ffec7c7964a609);

183

[ 185](structnet__stats__udp.md#a0ea91d85fe322661fb909f5e94e55a34) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [recv](structnet__stats__udp.md#a0ea91d85fe322661fb909f5e94e55a34);

186

[ 188](structnet__stats__udp.md#ab4e8228c221901d3ded55f3f823bfa1c) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [sent](structnet__stats__udp.md#ab4e8228c221901d3ded55f3f823bfa1c);

189

[ 191](structnet__stats__udp.md#a4c57d5f68ebda7981400729b9c7fe0f7) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [chkerr](structnet__stats__udp.md#a4c57d5f68ebda7981400729b9c7fe0f7);

192};

193

[ 197](structnet__stats__ipv6__nd.md)struct [net\_stats\_ipv6\_nd](structnet__stats__ipv6__nd.md) {

[ 199](structnet__stats__ipv6__nd.md#a31074d5d44138fcabdc5f7750f9f2c47) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [drop](structnet__stats__ipv6__nd.md#a31074d5d44138fcabdc5f7750f9f2c47);

200

[ 202](structnet__stats__ipv6__nd.md#a0bf6f67d9112996a3b002ea160aec769) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [recv](structnet__stats__ipv6__nd.md#a0bf6f67d9112996a3b002ea160aec769);

203

[ 205](structnet__stats__ipv6__nd.md#a0129f7892a4439c20deb2f32b9001277) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [sent](structnet__stats__ipv6__nd.md#a0129f7892a4439c20deb2f32b9001277);

206};

207

[ 211](structnet__stats__ipv6__pmtu.md)struct [net\_stats\_ipv6\_pmtu](structnet__stats__ipv6__pmtu.md) {

[ 213](structnet__stats__ipv6__pmtu.md#a68b19ebb61e84eb876178a31c7a4e327) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [drop](structnet__stats__ipv6__pmtu.md#a68b19ebb61e84eb876178a31c7a4e327);

214

[ 216](structnet__stats__ipv6__pmtu.md#a66346cd9140e30727d77648f65345762) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [recv](structnet__stats__ipv6__pmtu.md#a66346cd9140e30727d77648f65345762);

217

[ 219](structnet__stats__ipv6__pmtu.md#a698f5794b73896f7a66def2d3209fafd) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [sent](structnet__stats__ipv6__pmtu.md#a698f5794b73896f7a66def2d3209fafd);

220};

221

[ 225](structnet__stats__ipv4__pmtu.md)struct [net\_stats\_ipv4\_pmtu](structnet__stats__ipv4__pmtu.md) {

[ 227](structnet__stats__ipv4__pmtu.md#ad35f9defad7c5ce29e510b8051788977) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [drop](structnet__stats__ipv4__pmtu.md#ad35f9defad7c5ce29e510b8051788977);

228

[ 230](structnet__stats__ipv4__pmtu.md#a64245eb7b9b1fcfa0f0efcb53eff7ec2) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [recv](structnet__stats__ipv4__pmtu.md#a64245eb7b9b1fcfa0f0efcb53eff7ec2);

231

[ 233](structnet__stats__ipv4__pmtu.md#a44f1028694d4001cd4a43f925f0bf0da) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [sent](structnet__stats__ipv4__pmtu.md#a44f1028694d4001cd4a43f925f0bf0da);

234};

235

[ 239](structnet__stats__ipv6__mld.md)struct [net\_stats\_ipv6\_mld](structnet__stats__ipv6__mld.md) {

[ 241](structnet__stats__ipv6__mld.md#a4879ff9e31f8b60973d3b169598e921d) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [recv](structnet__stats__ipv6__mld.md#a4879ff9e31f8b60973d3b169598e921d);

242

[ 244](structnet__stats__ipv6__mld.md#ab397b74b14ce7047bf2fc63ca72ce1e5) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [sent](structnet__stats__ipv6__mld.md#ab397b74b14ce7047bf2fc63ca72ce1e5);

245

[ 247](structnet__stats__ipv6__mld.md#ad85dc87f57296a1e7d64e959b0370ee8) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [drop](structnet__stats__ipv6__mld.md#ad85dc87f57296a1e7d64e959b0370ee8);

248};

249

[ 253](structnet__stats__ipv4__igmp.md)struct [net\_stats\_ipv4\_igmp](structnet__stats__ipv4__igmp.md) {

[ 255](structnet__stats__ipv4__igmp.md#a469113de7af0ba42dbd1b0365d00602c) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [recv](structnet__stats__ipv4__igmp.md#a469113de7af0ba42dbd1b0365d00602c);

256

[ 258](structnet__stats__ipv4__igmp.md#a955e20a6ee5e19e08000b3114b9d71a6) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [sent](structnet__stats__ipv4__igmp.md#a955e20a6ee5e19e08000b3114b9d71a6);

259

[ 261](structnet__stats__ipv4__igmp.md#a1c37702ff837b8c5cc9df5f690e7678c) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [drop](structnet__stats__ipv4__igmp.md#a1c37702ff837b8c5cc9df5f690e7678c);

262};

263

[ 267](structnet__stats__dns.md)struct [net\_stats\_dns](structnet__stats__dns.md) {

[ 269](structnet__stats__dns.md#abc9be2039a3ff9e62b956ae27fd0ab84) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [recv](structnet__stats__dns.md#abc9be2039a3ff9e62b956ae27fd0ab84);

270

[ 272](structnet__stats__dns.md#ac07b9f4d084b978cc11e7799fb71a435) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [sent](structnet__stats__dns.md#ac07b9f4d084b978cc11e7799fb71a435);

273

[ 275](structnet__stats__dns.md#a04756603a183f35dbf6f55000556b546) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [drop](structnet__stats__dns.md#a04756603a183f35dbf6f55000556b546);

276};

277

[ 281](structnet__stats__tx__time.md)struct [net\_stats\_tx\_time](structnet__stats__tx__time.md) {

[ 283](structnet__stats__tx__time.md#af6f7a26c0344a0f93306e105a8917c3e) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [sum](structnet__stats__tx__time.md#af6f7a26c0344a0f93306e105a8917c3e);

284

[ 286](structnet__stats__tx__time.md#a7a652350ed04e53ba02aec294f8444b4) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [count](structnet__stats__tx__time.md#a7a652350ed04e53ba02aec294f8444b4);

287};

288

[ 292](structnet__stats__rx__time.md)struct [net\_stats\_rx\_time](structnet__stats__rx__time.md) {

[ 294](structnet__stats__rx__time.md#a4b84c2ae2fda8fcd75fdf1bf0b2aae8d) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [sum](structnet__stats__rx__time.md#a4b84c2ae2fda8fcd75fdf1bf0b2aae8d);

295

[ 297](structnet__stats__rx__time.md#a68247051b064de081fa2e84118192958) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [count](structnet__stats__rx__time.md#a68247051b064de081fa2e84118192958);

298};

299

301

302#if NET\_TC\_TX\_COUNT == 0

303#define NET\_TC\_TX\_STATS\_COUNT 1

304#else

305#define NET\_TC\_TX\_STATS\_COUNT NET\_TC\_TX\_COUNT

306#endif

307

308#if NET\_TC\_RX\_COUNT == 0

309#define NET\_TC\_RX\_STATS\_COUNT 1

310#else

311#define NET\_TC\_RX\_STATS\_COUNT NET\_TC\_RX\_COUNT

312#endif

313

315

[ 319](structnet__stats__tc.md)struct [net\_stats\_tc](structnet__stats__tc.md) {

321 struct {

[ 323](structnet__stats__tc.md#a74b471b77fb1c72933daa656319cc2af) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [bytes](structnet__stats__tc.md#a74b471b77fb1c72933daa656319cc2af);

[ 325](structnet__stats__tc.md#a30288ef3bb0796cd18c3cf0aedbe875a) struct [net\_stats\_tx\_time](structnet__stats__tx__time.md) [tx\_time](structnet__stats__tc.md#a30288ef3bb0796cd18c3cf0aedbe875a);

326#if defined(CONFIG\_NET\_PKT\_TXTIME\_STATS\_DETAIL)

328 struct [net\_stats\_tx\_time](structnet__stats__tx__time.md)

329 tx\_time\_detail[NET\_PKT\_DETAIL\_STATS\_COUNT];

330#endif

[ 332](structnet__stats__tc.md#a6614b5f5186635415a7d787260c39248) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [pkts](structnet__stats__tc.md#a6614b5f5186635415a7d787260c39248);

[ 334](structnet__stats__tc.md#a1794f71f7fe7b3d20d406be4b28eb032) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [dropped](structnet__stats__tc.md#a1794f71f7fe7b3d20d406be4b28eb032);

[ 336](structnet__stats__tc.md#a8a5c2e59990407ddbfc7973a1c183bf6) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [priority](structnet__stats__tc.md#a8a5c2e59990407ddbfc7973a1c183bf6);

[ 337](structnet__stats__tc.md#a8d6a3ebcc49ce8c34a5faae986f648e2) } [sent](structnet__stats__tc.md#a8d6a3ebcc49ce8c34a5faae986f648e2)[NET\_TC\_TX\_STATS\_COUNT];

338

340 struct {

342 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) bytes;

[ 344](structnet__stats__tc.md#a8ea00824bb0fb18e4d8912343e01c3b7) struct [net\_stats\_rx\_time](structnet__stats__rx__time.md) [rx\_time](structnet__stats__tc.md#a8ea00824bb0fb18e4d8912343e01c3b7);

345#if defined(CONFIG\_NET\_PKT\_RXTIME\_STATS\_DETAIL)

347 struct [net\_stats\_rx\_time](structnet__stats__rx__time.md)

348 rx\_time\_detail[NET\_PKT\_DETAIL\_STATS\_COUNT];

349#endif

351 [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [pkts](structnet__stats__tc.md#a6614b5f5186635415a7d787260c39248);

353 [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [dropped](structnet__stats__tc.md#a1794f71f7fe7b3d20d406be4b28eb032);

355 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [priority](structnet__stats__tc.md#a8a5c2e59990407ddbfc7973a1c183bf6);

[ 356](structnet__stats__tc.md#a2c8826e27ff59154f14a1755ffd4c594) } [recv](posix_2sys_2socket_8h.md#adee01662b0cf762a014efd87ab811276)[NET\_TC\_RX\_STATS\_COUNT];

357};

358

359

[ 363](structnet__stats__pm.md)struct [net\_stats\_pm](structnet__stats__pm.md) {

[ 365](structnet__stats__pm.md#ab43935fcfe9efc1cd5f3e7e329996805) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [overall\_suspend\_time](structnet__stats__pm.md#ab43935fcfe9efc1cd5f3e7e329996805);

[ 367](structnet__stats__pm.md#ac14122a4765c499c045f18c70af355a0) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [suspend\_count](structnet__stats__pm.md#ac14122a4765c499c045f18c70af355a0);

[ 369](structnet__stats__pm.md#a0bdf9c3676298e2df4ff3bfa03f5e823) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [last\_suspend\_time](structnet__stats__pm.md#a0bdf9c3676298e2df4ff3bfa03f5e823);

[ 371](structnet__stats__pm.md#a6784806eaa093431ed3c0f7acfe5a89c) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [start\_time](structnet__stats__pm.md#a6784806eaa093431ed3c0f7acfe5a89c);

372};

373

[ 377](structnet__stats__pkt__filter.md)struct [net\_stats\_pkt\_filter](structnet__stats__pkt__filter.md) {

379 struct {

[ 381](structnet__stats__pkt__filter.md#a62d2d86781e6224b09f21929f27b2ef7) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [drop](structnet__stats__pkt__filter.md#a62d2d86781e6224b09f21929f27b2ef7);

382#if defined(CONFIG\_NET\_PKT\_FILTER\_IPV4\_HOOK)

384 [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) ipv4\_drop;

385#endif

386#if defined(CONFIG\_NET\_PKT\_FILTER\_IPV6\_HOOK)

388 [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) ipv6\_drop;

389#endif

390#if defined(CONFIG\_NET\_PKT\_FILTER\_LOCAL\_IN\_HOOK)

392 [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) local\_drop;

393#endif

[ 394](structnet__stats__pkt__filter.md#a8cf9912d574873832b85a614eb776789) } [rx](structnet__stats__pkt__filter.md#a8cf9912d574873832b85a614eb776789);

395

397 struct {

399 [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [drop](structnet__stats__pkt__filter.md#a62d2d86781e6224b09f21929f27b2ef7);

[ 400](structnet__stats__pkt__filter.md#a5e88001e143c0adb129ca93b108c277d) } [tx](structnet__stats__pkt__filter.md#a5e88001e143c0adb129ca93b108c277d);

401};

402

[ 406](structnet__stats.md)struct [net\_stats](structnet__stats.md) {

[ 411](structnet__stats.md#a7a28233e6d23efdce0143469b9bb6c05) struct [net\_stats\_bytes](structnet__stats__bytes.md) [bytes](structnet__stats.md#a7a28233e6d23efdce0143469b9bb6c05);

412

[ 414](structnet__stats.md#a3a4c90661d6b310b628262228a341fe2) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [processing\_error](structnet__stats.md#a3a4c90661d6b310b628262228a341fe2);

415

[ 417](structnet__stats.md#ac42cb13954d164e92a1ef60919a2a34e) struct [net\_stats\_ip\_errors](structnet__stats__ip__errors.md) [ip\_errors](structnet__stats.md#ac42cb13954d164e92a1ef60919a2a34e);

418

419#if defined(CONFIG\_NET\_STATISTICS\_PKT\_FILTER)

420 struct [net\_stats\_pkt\_filter](structnet__stats__pkt__filter.md) pkt\_filter;

421#endif

422

423#if defined(CONFIG\_NET\_STATISTICS\_IPV6)

425 struct [net\_stats\_ip](structnet__stats__ip.md) ipv6;

426#endif

427

428#if defined(CONFIG\_NET\_STATISTICS\_IPV4)

430 struct [net\_stats\_ip](structnet__stats__ip.md) ipv4;

431#endif

432

433#if defined(CONFIG\_NET\_STATISTICS\_ICMP)

435 struct [net\_stats\_icmp](structnet__stats__icmp.md) icmp;

436#endif

437

438#if defined(CONFIG\_NET\_STATISTICS\_TCP)

440 struct [net\_stats\_tcp](structnet__stats__tcp.md) tcp;

441#endif

442

443#if defined(CONFIG\_NET\_STATISTICS\_UDP)

445 struct [net\_stats\_udp](structnet__stats__udp.md) udp;

446#endif

447

448#if defined(CONFIG\_NET\_STATISTICS\_IPV6\_ND)

450 struct [net\_stats\_ipv6\_nd](structnet__stats__ipv6__nd.md) ipv6\_nd;

451#endif

452

453#if defined(CONFIG\_NET\_STATISTICS\_IPV6\_PMTU)

455 struct [net\_stats\_ipv6\_pmtu](structnet__stats__ipv6__pmtu.md) ipv6\_pmtu;

456#endif

457

458#if defined(CONFIG\_NET\_STATISTICS\_IPV4\_PMTU)

460 struct [net\_stats\_ipv4\_pmtu](structnet__stats__ipv4__pmtu.md) ipv4\_pmtu;

461#endif

462

463#if defined(CONFIG\_NET\_STATISTICS\_MLD)

465 struct [net\_stats\_ipv6\_mld](structnet__stats__ipv6__mld.md) ipv6\_mld;

466#endif

467

468#if defined(CONFIG\_NET\_STATISTICS\_IGMP)

470 struct [net\_stats\_ipv4\_igmp](structnet__stats__ipv4__igmp.md) ipv4\_igmp;

471#endif

472

473#if defined(CONFIG\_NET\_STATISTICS\_DNS)

475 struct [net\_stats\_dns](structnet__stats__dns.md) dns;

476#endif

477

478#if NET\_TC\_COUNT > 1

480 struct [net\_stats\_tc](structnet__stats__tc.md) tc;

481#endif

482

483#if defined(CONFIG\_NET\_PKT\_TXTIME\_STATS)

485 struct [net\_stats\_tx\_time](structnet__stats__tx__time.md) tx\_time;

486#endif

487

488#if defined(CONFIG\_NET\_PKT\_RXTIME\_STATS)

490 struct [net\_stats\_rx\_time](structnet__stats__rx__time.md) rx\_time;

491#endif

492

493#if defined(CONFIG\_NET\_PKT\_TXTIME\_STATS\_DETAIL)

495 struct [net\_stats\_tx\_time](structnet__stats__tx__time.md) tx\_time\_detail[NET\_PKT\_DETAIL\_STATS\_COUNT];

496#endif

497#if defined(CONFIG\_NET\_PKT\_RXTIME\_STATS\_DETAIL)

499 struct [net\_stats\_rx\_time](structnet__stats__rx__time.md) rx\_time\_detail[NET\_PKT\_DETAIL\_STATS\_COUNT];

500#endif

501

502#if defined(CONFIG\_NET\_STATISTICS\_POWER\_MANAGEMENT)

504 struct [net\_stats\_pm](structnet__stats__pm.md) pm;

505#endif

506};

507

[ 511](structnet__stats__eth__errors.md)struct [net\_stats\_eth\_errors](structnet__stats__eth__errors.md) {

[ 513](structnet__stats__eth__errors.md#aca0e2e4807fa70279dee8ddaad2d7ef7) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [rx\_length\_errors](structnet__stats__eth__errors.md#aca0e2e4807fa70279dee8ddaad2d7ef7);

514

[ 516](structnet__stats__eth__errors.md#a9afee89f5bb01907e7cd515e2a0ff1b5) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [rx\_over\_errors](structnet__stats__eth__errors.md#a9afee89f5bb01907e7cd515e2a0ff1b5);

517

[ 519](structnet__stats__eth__errors.md#a4dab70cf219269bb393ce14faf0ed77e) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [rx\_crc\_errors](structnet__stats__eth__errors.md#a4dab70cf219269bb393ce14faf0ed77e);

520

[ 522](structnet__stats__eth__errors.md#a8dfcc5cd1b4decec5783d01ba7033b05) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [rx\_frame\_errors](structnet__stats__eth__errors.md#a8dfcc5cd1b4decec5783d01ba7033b05);

523

[ 525](structnet__stats__eth__errors.md#a82622736d226b4d3b999f1f22ccf8529) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [rx\_no\_buffer\_count](structnet__stats__eth__errors.md#a82622736d226b4d3b999f1f22ccf8529);

526

[ 528](structnet__stats__eth__errors.md#a2d2b2c4e3764ebec841f1ecbe7058d99) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [rx\_missed\_errors](structnet__stats__eth__errors.md#a2d2b2c4e3764ebec841f1ecbe7058d99);

529

[ 531](structnet__stats__eth__errors.md#a0e83e270a35222ed3e927800be4159e7) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [rx\_long\_length\_errors](structnet__stats__eth__errors.md#a0e83e270a35222ed3e927800be4159e7);

532

[ 534](structnet__stats__eth__errors.md#a5e3d39d8417bb180cbfcb8c901006e81) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [rx\_short\_length\_errors](structnet__stats__eth__errors.md#a5e3d39d8417bb180cbfcb8c901006e81);

535

[ 537](structnet__stats__eth__errors.md#a7618f10af3443c49a6e256bb41e77781) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [rx\_align\_errors](structnet__stats__eth__errors.md#a7618f10af3443c49a6e256bb41e77781);

538

[ 540](structnet__stats__eth__errors.md#a7bcfbb13836f162ceeb5f021304b5c76) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [rx\_dma\_failed](structnet__stats__eth__errors.md#a7bcfbb13836f162ceeb5f021304b5c76);

541

[ 543](structnet__stats__eth__errors.md#adbcae9c10c081f1cdf304bcdce740aa4) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [rx\_buf\_alloc\_failed](structnet__stats__eth__errors.md#adbcae9c10c081f1cdf304bcdce740aa4);

544

[ 546](structnet__stats__eth__errors.md#afec6a7e24c6f3cc74dd9f739f27b3e48) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [tx\_aborted\_errors](structnet__stats__eth__errors.md#afec6a7e24c6f3cc74dd9f739f27b3e48);

547

[ 549](structnet__stats__eth__errors.md#a0043d1a1481040a6d7439bd23423ec12) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [tx\_carrier\_errors](structnet__stats__eth__errors.md#a0043d1a1481040a6d7439bd23423ec12);

550

[ 552](structnet__stats__eth__errors.md#a84630da9b82557f56dc35cd59ca2f7ae) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [tx\_fifo\_errors](structnet__stats__eth__errors.md#a84630da9b82557f56dc35cd59ca2f7ae);

553

[ 555](structnet__stats__eth__errors.md#ae2a13733c1a5f0cc3e00efca0c3f429d) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [tx\_heartbeat\_errors](structnet__stats__eth__errors.md#ae2a13733c1a5f0cc3e00efca0c3f429d);

556

[ 558](structnet__stats__eth__errors.md#a17624a12d6473bdd78698076fed0d122) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [tx\_window\_errors](structnet__stats__eth__errors.md#a17624a12d6473bdd78698076fed0d122);

559

[ 561](structnet__stats__eth__errors.md#abfbf6478b7afdd5935d7c6948c9ef426) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [tx\_dma\_failed](structnet__stats__eth__errors.md#abfbf6478b7afdd5935d7c6948c9ef426);

562

[ 564](structnet__stats__eth__errors.md#a07d0a435f2129556520c732571d28edf) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [uncorr\_ecc\_errors](structnet__stats__eth__errors.md#a07d0a435f2129556520c732571d28edf);

565

[ 567](structnet__stats__eth__errors.md#a257113639f0e0e3085febb7a147f498f) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [corr\_ecc\_errors](structnet__stats__eth__errors.md#a257113639f0e0e3085febb7a147f498f);

568};

569

[ 573](structnet__stats__eth__flow.md)struct [net\_stats\_eth\_flow](structnet__stats__eth__flow.md) {

[ 575](structnet__stats__eth__flow.md#a08e5da4ff78fe3893b9c9a628cefe4f2) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [rx\_flow\_control\_xon](structnet__stats__eth__flow.md#a08e5da4ff78fe3893b9c9a628cefe4f2);

576

[ 578](structnet__stats__eth__flow.md#a8f9b93537b3c11be70f276aaa72cb637) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [rx\_flow\_control\_xoff](structnet__stats__eth__flow.md#a8f9b93537b3c11be70f276aaa72cb637);

579

[ 581](structnet__stats__eth__flow.md#a31412e8bf9d38ba630ea856e958a48d7) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [tx\_flow\_control\_xon](structnet__stats__eth__flow.md#a31412e8bf9d38ba630ea856e958a48d7);

582

[ 584](structnet__stats__eth__flow.md#a969d81f9db20312d2d2aa7f70f93bdd5) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [tx\_flow\_control\_xoff](structnet__stats__eth__flow.md#a969d81f9db20312d2d2aa7f70f93bdd5);

585};

586

[ 590](structnet__stats__eth__csum.md)struct [net\_stats\_eth\_csum](structnet__stats__eth__csum.md) {

[ 592](structnet__stats__eth__csum.md#a1f1ba5c01c6232cd739d069ddb871b17) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [rx\_csum\_offload\_good](structnet__stats__eth__csum.md#a1f1ba5c01c6232cd739d069ddb871b17);

593

[ 595](structnet__stats__eth__csum.md#ac4fc04d66193070d4f52a4c07f29ccce) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [rx\_csum\_offload\_errors](structnet__stats__eth__csum.md#ac4fc04d66193070d4f52a4c07f29ccce);

596};

597

[ 601](structnet__stats__eth__hw__timestamp.md)struct [net\_stats\_eth\_hw\_timestamp](structnet__stats__eth__hw__timestamp.md) {

[ 603](structnet__stats__eth__hw__timestamp.md#acd3d5f72d7df568110d96093e0c9534d) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [rx\_hwtstamp\_cleared](structnet__stats__eth__hw__timestamp.md#acd3d5f72d7df568110d96093e0c9534d);

604

[ 606](structnet__stats__eth__hw__timestamp.md#a41f605499dbf88a879522fdfa4633d9e) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [tx\_hwtstamp\_timeouts](structnet__stats__eth__hw__timestamp.md#a41f605499dbf88a879522fdfa4633d9e);

607

[ 609](structnet__stats__eth__hw__timestamp.md#ae1f983faf4a999308c464e4af5a5284b) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [tx\_hwtstamp\_skipped](structnet__stats__eth__hw__timestamp.md#ae1f983faf4a999308c464e4af5a5284b);

610};

611

612#ifdef CONFIG\_NET\_STATISTICS\_ETHERNET\_VENDOR

616struct net\_stats\_eth\_vendor {

617 const char \* const key;

618 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) value;

619};

620#endif

621

[ 625](structnet__stats__eth.md)struct [net\_stats\_eth](structnet__stats__eth.md) {

[ 627](structnet__stats__eth.md#a8c5cf1ead8ba214425a16fed1c2ad0fb) struct [net\_stats\_bytes](structnet__stats__bytes.md) [bytes](structnet__stats__eth.md#a8c5cf1ead8ba214425a16fed1c2ad0fb);

628

[ 630](structnet__stats__eth.md#a97bd6026b16890743f344751a21107f1) struct [net\_stats\_pkts](structnet__stats__pkts.md) [pkts](structnet__stats__eth.md#a97bd6026b16890743f344751a21107f1);

631

[ 633](structnet__stats__eth.md#a054beb909134b0e0f22f5df599549128) struct [net\_stats\_pkts](structnet__stats__pkts.md) [broadcast](structnet__stats__eth.md#a054beb909134b0e0f22f5df599549128);

634

[ 636](structnet__stats__eth.md#a4f6a2903330518a132e7e547820e0bf2) struct [net\_stats\_pkts](structnet__stats__pkts.md) [multicast](structnet__stats__eth.md#a4f6a2903330518a132e7e547820e0bf2);

637

[ 639](structnet__stats__eth.md#a9c869740f416fbe0b54d7fefacb1fe29) struct [net\_stats\_pkts](structnet__stats__pkts.md) [errors](structnet__stats__eth.md#a9c869740f416fbe0b54d7fefacb1fe29);

640

[ 642](structnet__stats__eth.md#a922feddb17fc020371f1bcc52c709415) struct [net\_stats\_eth\_errors](structnet__stats__eth__errors.md) [error\_details](structnet__stats__eth.md#a922feddb17fc020371f1bcc52c709415);

643

[ 645](structnet__stats__eth.md#a643010ac6360c8c0c08016725ba12222) struct [net\_stats\_eth\_flow](structnet__stats__eth__flow.md) [flow\_control](structnet__stats__eth.md#a643010ac6360c8c0c08016725ba12222);

646

[ 648](structnet__stats__eth.md#a2169ae06bace1a93663bccf88c8d7a29) struct [net\_stats\_eth\_csum](structnet__stats__eth__csum.md) [csum](structnet__stats__eth.md#a2169ae06bace1a93663bccf88c8d7a29);

649

[ 651](structnet__stats__eth.md#a44667efff73c17c089ed22d5b0da5ad3) struct [net\_stats\_eth\_hw\_timestamp](structnet__stats__eth__hw__timestamp.md) [hw\_timestamp](structnet__stats__eth.md#a44667efff73c17c089ed22d5b0da5ad3);

652

[ 654](structnet__stats__eth.md#a822d4205791f59999c842610522f6fc5) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [collisions](structnet__stats__eth.md#a822d4205791f59999c842610522f6fc5);

655

[ 657](structnet__stats__eth.md#a257c349cf3d32d38796e3899e702454a) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [tx\_dropped](structnet__stats__eth.md#a257c349cf3d32d38796e3899e702454a);

658

[ 660](structnet__stats__eth.md#ab351258ae82abd09759d37774559d8bc) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [tx\_timeout\_count](structnet__stats__eth.md#ab351258ae82abd09759d37774559d8bc);

661

[ 663](structnet__stats__eth.md#a6699012226e25e8bad39076fed6dbfb5) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [tx\_restart\_queue](structnet__stats__eth.md#a6699012226e25e8bad39076fed6dbfb5);

664

[ 666](structnet__stats__eth.md#afaacee7cc1d0a35ae2344175421c40dd) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [unknown\_protocol](structnet__stats__eth.md#afaacee7cc1d0a35ae2344175421c40dd);

667

668#ifdef CONFIG\_NET\_STATISTICS\_ETHERNET\_VENDOR

670 struct net\_stats\_eth\_vendor \*vendor;

671#endif

672};

673

[ 677](structnet__stats__ppp.md)struct [net\_stats\_ppp](structnet__stats__ppp.md) {

[ 679](structnet__stats__ppp.md#ab2b48da7f19d4b83e3f41b41979b7ed8) struct [net\_stats\_bytes](structnet__stats__bytes.md) [bytes](structnet__stats__ppp.md#ab2b48da7f19d4b83e3f41b41979b7ed8);

680

[ 682](structnet__stats__ppp.md#a71fc81f3c5f3e65a476b3391f086d340) struct [net\_stats\_pkts](structnet__stats__pkts.md) [pkts](structnet__stats__ppp.md#a71fc81f3c5f3e65a476b3391f086d340);

683

[ 685](structnet__stats__ppp.md#ae2e0a47a539e9d7bc97f9c63f889b276) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [drop](structnet__stats__ppp.md#ae2e0a47a539e9d7bc97f9c63f889b276);

686

[ 688](structnet__stats__ppp.md#a1332b31980f82236aeb0c3f9444e2ac6) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [chkerr](structnet__stats__ppp.md#a1332b31980f82236aeb0c3f9444e2ac6);

689};

690

[ 694](structnet__stats__sta__mgmt.md)struct [net\_stats\_sta\_mgmt](structnet__stats__sta__mgmt.md) {

[ 696](structnet__stats__sta__mgmt.md#ac6e68fded8e19b20259442436923f815) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [beacons\_rx](structnet__stats__sta__mgmt.md#ac6e68fded8e19b20259442436923f815);

697

[ 699](structnet__stats__sta__mgmt.md#a29ae0079b4c780e0de2656a85ec15fe9) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [beacons\_miss](structnet__stats__sta__mgmt.md#a29ae0079b4c780e0de2656a85ec15fe9);

700};

701

[ 705](structnet__stats__wifi.md)struct [net\_stats\_wifi](structnet__stats__wifi.md) {

[ 707](structnet__stats__wifi.md#a8bee22961545674e6ab100b58a04bf91) struct [net\_stats\_sta\_mgmt](structnet__stats__sta__mgmt.md) [sta\_mgmt](structnet__stats__wifi.md#a8bee22961545674e6ab100b58a04bf91);

708

[ 710](structnet__stats__wifi.md#aa055b1e8bd8f1e50815c1028b562be07) struct [net\_stats\_bytes](structnet__stats__bytes.md) [bytes](structnet__stats__wifi.md#aa055b1e8bd8f1e50815c1028b562be07);

711

[ 713](structnet__stats__wifi.md#adbcdb2dd8733f2917c00a0b2d365393b) struct [net\_stats\_pkts](structnet__stats__pkts.md) [pkts](structnet__stats__wifi.md#adbcdb2dd8733f2917c00a0b2d365393b);

714

[ 716](structnet__stats__wifi.md#a03dc04638c4b670bd7f3520d45fc1eda) struct [net\_stats\_pkts](structnet__stats__pkts.md) [broadcast](structnet__stats__wifi.md#a03dc04638c4b670bd7f3520d45fc1eda);

717

[ 719](structnet__stats__wifi.md#a7e7f68215101885fd51c70e981da26e7) struct [net\_stats\_pkts](structnet__stats__pkts.md) [multicast](structnet__stats__wifi.md#a7e7f68215101885fd51c70e981da26e7);

720

[ 722](structnet__stats__wifi.md#ae0149e64a94a9f96eb6680f94793c8c4) struct [net\_stats\_pkts](structnet__stats__pkts.md) [errors](structnet__stats__wifi.md#ae0149e64a94a9f96eb6680f94793c8c4);

723

[ 725](structnet__stats__wifi.md#ae80dcd73a3c5ce3ec3282d1ae827b338) struct [net\_stats\_pkts](structnet__stats__pkts.md) [unicast](structnet__stats__wifi.md#ae80dcd73a3c5ce3ec3282d1ae827b338);

726

[ 728](structnet__stats__wifi.md#ac498c9e517f2cb2eb01d251e84159e7e) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [overrun\_count](structnet__stats__wifi.md#ac498c9e517f2cb2eb01d251e84159e7e);

729};

730

731#if defined(CONFIG\_NET\_STATISTICS\_USER\_API)

732/\* Management part definitions \*/

733

735

736#define NET\_STATS\_LAYER NET\_MGMT\_LAYER\_L3

737#define NET\_STATS\_CODE NET\_MGMT\_LAYER\_CODE\_STATS

738#define NET\_STATS\_BASE (NET\_MGMT\_LAYER(NET\_STATS\_LAYER) | \

739 NET\_MGMT\_LAYER\_CODE(NET\_STATS\_CODE))

740

741enum net\_request\_stats\_cmd {

742 NET\_REQUEST\_STATS\_CMD\_GET\_ALL = 1,

743 NET\_REQUEST\_STATS\_CMD\_GET\_PROCESSING\_ERROR,

744 NET\_REQUEST\_STATS\_CMD\_GET\_PKT\_FILTER\_DROP,

745 NET\_REQUEST\_STATS\_CMD\_GET\_BYTES,

746 NET\_REQUEST\_STATS\_CMD\_GET\_IP\_ERRORS,

747 NET\_REQUEST\_STATS\_CMD\_GET\_IPV4,

748 NET\_REQUEST\_STATS\_CMD\_GET\_IPV6,

749 NET\_REQUEST\_STATS\_CMD\_GET\_IPV6\_ND,

750 NET\_REQUEST\_STATS\_CMD\_GET\_IPV6\_PMTU,

751 NET\_REQUEST\_STATS\_CMD\_GET\_IPV4\_PMTU,

752 NET\_REQUEST\_STATS\_CMD\_GET\_ICMP,

753 NET\_REQUEST\_STATS\_CMD\_GET\_UDP,

754 NET\_REQUEST\_STATS\_CMD\_GET\_TCP,

755 NET\_REQUEST\_STATS\_CMD\_GET\_ETHERNET,

756 NET\_REQUEST\_STATS\_CMD\_GET\_PPP,

757 NET\_REQUEST\_STATS\_CMD\_GET\_PM,

758 NET\_REQUEST\_STATS\_CMD\_GET\_WIFI,

759 NET\_REQUEST\_STATS\_CMD\_RESET\_WIFI,

760 NET\_REQUEST\_STATS\_CMD\_GET\_VPN,

761};

762

764

766#define NET\_REQUEST\_STATS\_GET\_ALL \

767 (NET\_STATS\_BASE | NET\_REQUEST\_STATS\_CMD\_GET\_ALL)

768

770#define NET\_REQUEST\_STATS\_GET\_PROCESSING\_ERROR \

771 (NET\_STATS\_BASE | NET\_REQUEST\_STATS\_CMD\_GET\_PROCESSING\_ERROR)

772

774#define NET\_REQUEST\_STATS\_GET\_PKT\_FILTER\_DROP \

775 (NET\_STATS\_BASE | NET\_REQUEST\_STATS\_CMD\_GET\_PKT\_FILTER\_DROP)

776

778#define NET\_REQUEST\_STATS\_GET\_BYTES \

779 (NET\_STATS\_BASE | NET\_REQUEST\_STATS\_CMD\_GET\_BYTES)

780

782#define NET\_REQUEST\_STATS\_GET\_IP\_ERRORS \

783 (NET\_STATS\_BASE | NET\_REQUEST\_STATS\_CMD\_GET\_IP\_ERRORS)

784

786

787[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_STATS\_GET\_ALL);

788[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_STATS\_GET\_PROCESSING\_ERROR);

789[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_STATS\_GET\_BYTES);

790[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_STATS\_GET\_IP\_ERRORS);

791

792#if defined(CONFIG\_NET\_STATISTICS\_PKT\_FILTER)

793[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_STATS\_GET\_PKT\_FILTER\_DROP);

794#endif /\* CONFIG\_NET\_STATISTICS\_PKT\_FILTER \*/

795

797

798#if defined(CONFIG\_NET\_STATISTICS\_IPV4)

800#define NET\_REQUEST\_STATS\_GET\_IPV4 \

801 (NET\_STATS\_BASE | NET\_REQUEST\_STATS\_CMD\_GET\_IPV4)

802

804[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_STATS\_GET\_IPV4);

806#endif /\* CONFIG\_NET\_STATISTICS\_IPV4 \*/

807

808#if defined(CONFIG\_NET\_STATISTICS\_IPV6)

810#define NET\_REQUEST\_STATS\_GET\_IPV6 \

811 (NET\_STATS\_BASE | NET\_REQUEST\_STATS\_CMD\_GET\_IPV6)

812

814[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_STATS\_GET\_IPV6);

816#endif /\* CONFIG\_NET\_STATISTICS\_IPV6 \*/

817

818#if defined(CONFIG\_NET\_STATISTICS\_IPV6\_ND)

820#define NET\_REQUEST\_STATS\_GET\_IPV6\_ND \

821 (NET\_STATS\_BASE | NET\_REQUEST\_STATS\_CMD\_GET\_IPV6\_ND)

822

824[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_STATS\_GET\_IPV6\_ND);

826#endif /\* CONFIG\_NET\_STATISTICS\_IPV6\_ND \*/

827

828#if defined(CONFIG\_NET\_STATISTICS\_IPV6\_PMTU)

830#define NET\_REQUEST\_STATS\_GET\_IPV6\_PMTU \

831 (NET\_STATS\_BASE | NET\_REQUEST\_STATS\_CMD\_GET\_IPV6\_PMTU)

832

834[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_STATS\_GET\_IPV6\_PMTU);

836#endif /\* CONFIG\_NET\_STATISTICS\_IPV6\_PMTU \*/

837

838#if defined(CONFIG\_NET\_STATISTICS\_IPV4\_PMTU)

840#define NET\_REQUEST\_STATS\_GET\_IPV4\_PMTU \

841 (NET\_STATS\_BASE | NET\_REQUEST\_STATS\_CMD\_GET\_IPV4\_PMTU)

842

844[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_STATS\_GET\_IPV4\_PMTU);

846#endif /\* CONFIG\_NET\_STATISTICS\_IPV4\_PMTU \*/

847

848#if defined(CONFIG\_NET\_STATISTICS\_ICMP)

850#define NET\_REQUEST\_STATS\_GET\_ICMP \

851 (NET\_STATS\_BASE | NET\_REQUEST\_STATS\_CMD\_GET\_ICMP)

852

854[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_STATS\_GET\_ICMP);

856#endif /\* CONFIG\_NET\_STATISTICS\_ICMP \*/

857

858#if defined(CONFIG\_NET\_STATISTICS\_UDP)

860#define NET\_REQUEST\_STATS\_GET\_UDP \

861 (NET\_STATS\_BASE | NET\_REQUEST\_STATS\_CMD\_GET\_UDP)

862

864[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_STATS\_GET\_UDP);

866#endif /\* CONFIG\_NET\_STATISTICS\_UDP \*/

867

868#if defined(CONFIG\_NET\_STATISTICS\_TCP)

870#define NET\_REQUEST\_STATS\_GET\_TCP \

871 (NET\_STATS\_BASE | NET\_REQUEST\_STATS\_CMD\_GET\_TCP)

872

874[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_STATS\_GET\_TCP);

876#endif /\* CONFIG\_NET\_STATISTICS\_TCP \*/

877

878#if defined(CONFIG\_NET\_STATISTICS\_ETHERNET)

880#define NET\_REQUEST\_STATS\_GET\_ETHERNET \

881 (NET\_STATS\_BASE | NET\_REQUEST\_STATS\_CMD\_GET\_ETHERNET)

882

884[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_STATS\_GET\_ETHERNET);

886#endif /\* CONFIG\_NET\_STATISTICS\_ETHERNET \*/

887

888#if defined(CONFIG\_NET\_STATISTICS\_PPP)

890#define NET\_REQUEST\_STATS\_GET\_PPP \

891 (NET\_STATS\_BASE | NET\_REQUEST\_STATS\_CMD\_GET\_PPP)

892

894[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_STATS\_GET\_PPP);

896#endif /\* CONFIG\_NET\_STATISTICS\_PPP \*/

897

898#if defined(CONFIG\_NET\_STATISTICS\_VPN)

900#define NET\_REQUEST\_STATS\_GET\_VPN \

901 (NET\_STATS\_BASE | NET\_REQUEST\_STATS\_CMD\_GET\_VPN)

902

904[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_STATS\_GET\_VPN);

906#endif /\* CONFIG\_NET\_STATISTICS\_VPN \*/

907

908#endif /\* CONFIG\_NET\_STATISTICS\_USER\_API \*/

909

910#if defined(CONFIG\_NET\_STATISTICS\_POWER\_MANAGEMENT)

912#define NET\_REQUEST\_STATS\_GET\_PM \

913 (NET\_STATS\_BASE | NET\_REQUEST\_STATS\_CMD\_GET\_PM)

914

916[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_STATS\_GET\_PM);

918#endif /\* CONFIG\_NET\_STATISTICS\_POWER\_MANAGEMENT \*/

919

920#if defined(CONFIG\_NET\_STATISTICS\_WIFI)

922#define NET\_REQUEST\_STATS\_GET\_WIFI \

923 (NET\_STATS\_BASE | NET\_REQUEST\_STATS\_CMD\_GET\_WIFI)

924

926[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_STATS\_GET\_WIFI);

928

930#define NET\_REQUEST\_STATS\_RESET\_WIFI \

931 (NET\_STATS\_BASE | NET\_REQUEST\_STATS\_CMD\_RESET\_WIFI)

932

934[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_STATS\_RESET\_WIFI);

936#endif /\* CONFIG\_NET\_STATISTICS\_WIFI \*/

937

[ 938](group__net__stats.md#ga2a1dcb35c366878ef5f675d6bc649223)#define NET\_STATS\_GET\_METRIC\_NAME(\_name) \_name

[ 939](group__net__stats.md#gab58d7d437d4fa9836a826ee59e2d081d)#define NET\_STATS\_GET\_COLLECTOR\_NAME(dev\_id, sfx) net\_stats\_##dev\_id##\_##sfx##\_collector

[ 940](group__net__stats.md#gab66b3c8d32d2f02add08c332460d5cd6)#define NET\_STATS\_GET\_VAR(dev\_id, sfx, var) zephyr\_net\_##var

[ 941](group__net__stats.md#gabb15df6c3c85b85756ef5d2d51d0afb2)#define NET\_STATS\_GET\_INSTANCE(dev\_id, sfx, \_not\_used) STRINGIFY(\_##dev\_id##\_##sfx)

942

943/\* The label value is set to be the network interface name. Note that we skip

944 \* the first character (\_) when setting the label value. This can be changed

945 \* if there is a way to token paste the instance name without the prefix character.

946 \* Note also that the below macros have some parameters that are not used atm.

947 \*/

[ 948](group__net__stats.md#gafc6b5e19cd9407c28cf151820b76a287)#define NET\_STATS\_PROMETHEUS\_COUNTER\_DEFINE(\_desc, \_labelval, \_not\_used, \

949 \_collector, \_name, \_stat\_var\_ptr) \

950 static PROMETHEUS\_COUNTER\_DEFINE( \

951 NET\_STATS\_GET\_METRIC\_NAME(\_name), \

952 \_desc, ({ .key = "nic", .value = &\_labelval[1] }), \

953 &(\_collector), \_stat\_var\_ptr)

954

[ 955](group__net__stats.md#ga162fa8a0ea4939e5768a0cc64210dd6a)#define NET\_STATS\_PROMETHEUS\_GAUGE\_DEFINE(\_desc, \_labelval, \_not\_used, \

956 \_collector, \_name, \_stat\_var\_ptr) \

957 static PROMETHEUS\_GAUGE\_DEFINE( \

958 NET\_STATS\_GET\_METRIC\_NAME(\_name), \

959 \_desc, ({ .key = "nic", .value = &\_labelval[1] }), \

960 &(\_collector), \_stat\_var\_ptr)

961

[ 962](group__net__stats.md#gab02b7f2c5c424723aed7a6aedd1181f9)#define NET\_STATS\_PROMETHEUS\_SUMMARY\_DEFINE(\_desc, \_labelval, \_not\_used, \

963 \_collector, \_name, \_stat\_var\_ptr) \

964 static PROMETHEUS\_SUMMARY\_DEFINE( \

965 NET\_STATS\_GET\_METRIC\_NAME(\_name), \

966 \_desc, ({ .key = "nic", .value = &\_labelval[1] }), \

967 &(\_collector), \_stat\_var\_ptr)

968

[ 969](group__net__stats.md#gae82639c2bed1c646cda66b49ae2f6de9)#define NET\_STATS\_PROMETHEUS\_HISTOGRAM\_DEFINE(\_desc, \_labelval, \_not\_used, \

970 \_collector, \_name, \_stat\_var\_ptr) \

971 static PROMETHEUS\_HISTOGRAM\_DEFINE( \

972 NET\_STATS\_GET\_METRIC\_NAME(\_name), \

973 \_desc, ({ .key = "nic", .value = &\_labelval[1] }), \

974 &(\_collector), \_stat\_var\_ptr)

975

976/\* IPv6 layer statistics \*/

977#if defined(CONFIG\_NET\_STATISTICS\_IPV6)

978#define NET\_STATS\_PROMETHEUS\_IPV6(iface, dev\_id, sfx) \

979 NET\_STATS\_PROMETHEUS\_COUNTER\_DEFINE( \

980 "IPv6 packets sent", \

981 NET\_STATS\_GET\_INSTANCE(dev\_id, sfx, ipv6\_sent), \

982 "packet\_count", \

983 NET\_STATS\_GET\_COLLECTOR\_NAME(dev\_id, sfx), \

984 NET\_STATS\_GET\_VAR(dev\_id, sfx, ipv6\_sent), \

985 &(iface)->stats.ipv6.sent); \

986 NET\_STATS\_PROMETHEUS\_COUNTER\_DEFINE( \

987 "IPv6 packets received", \

988 NET\_STATS\_GET\_INSTANCE(dev\_id, sfx, ipv6\_recv), \

989 "packet\_count", \

990 NET\_STATS\_GET\_COLLECTOR\_NAME(dev\_id, sfx), \

991 NET\_STATS\_GET\_VAR(dev\_id, sfx, ipv6\_recv), \

992 &(iface)->stats.ipv6.recv); \

993 NET\_STATS\_PROMETHEUS\_COUNTER\_DEFINE( \

994 "IPv6 packets dropped", \

995 NET\_STATS\_GET\_INSTANCE(dev\_id, sfx, ipv6\_drop), \

996 "packet\_count", \

997 NET\_STATS\_GET\_COLLECTOR\_NAME(dev\_id, sfx), \

998 NET\_STATS\_GET\_VAR(dev\_id, sfx, ipv6\_drop), \

999 &(iface)->stats.ipv6.drop); \

1000 NET\_STATS\_PROMETHEUS\_COUNTER\_DEFINE( \

1001 "IPv6 packets forwarded", \

1002 NET\_STATS\_GET\_INSTANCE(dev\_id, sfx, ipv6\_forward), \

1003 "packet\_count", \

1004 NET\_STATS\_GET\_COLLECTOR\_NAME(dev\_id, sfx), \

1005 NET\_STATS\_GET\_VAR(dev\_id, sfx, ipv6\_forwarded), \

1006 &(iface)->stats.ipv6.forwarded)

1007#else

[ 1008](group__net__stats.md#gaef8debd9597dae9e8ec2ef91d6e645cc)#define NET\_STATS\_PROMETHEUS\_IPV6(iface, dev\_id, sfx)

1009#endif

1010

1011/\* IPv4 layer statistics \*/

1012#if defined(CONFIG\_NET\_STATISTICS\_IPV4)

1013#define NET\_STATS\_PROMETHEUS\_IPV4(iface, dev\_id, sfx) \

1014 NET\_STATS\_PROMETHEUS\_COUNTER\_DEFINE( \

1015 "IPv4 packets sent", \

1016 NET\_STATS\_GET\_INSTANCE(dev\_id, sfx, ipv4\_sent), \

1017 "packet\_count", \

1018 NET\_STATS\_GET\_COLLECTOR\_NAME(dev\_id, sfx), \

1019 NET\_STATS\_GET\_VAR(dev\_id, sfx, ipv4\_sent), \

1020 &(iface)->stats.ipv4.sent); \

1021 NET\_STATS\_PROMETHEUS\_COUNTER\_DEFINE( \

1022 "IPv4 packets received", \

1023 NET\_STATS\_GET\_INSTANCE(dev\_id, sfx, ipv4\_recv), \

1024 "packet\_count", \

1025 NET\_STATS\_GET\_COLLECTOR\_NAME(dev\_id, sfx), \

1026 NET\_STATS\_GET\_VAR(dev\_id, sfx, ipv4\_recv), \

1027 &(iface)->stats.ipv4.recv); \

1028 NET\_STATS\_PROMETHEUS\_COUNTER\_DEFINE( \

1029 "IPv4 packets dropped", \

1030 NET\_STATS\_GET\_INSTANCE(dev\_id, sfx, ipv4\_drop), \

1031 "packet\_count", \

1032 NET\_STATS\_GET\_COLLECTOR\_NAME(dev\_id, sfx), \

1033 NET\_STATS\_GET\_VAR(dev\_id, sfx, ipv4\_drop), \

1034 &(iface)->stats.ipv4.drop); \

1035 NET\_STATS\_PROMETHEUS\_COUNTER\_DEFINE( \

1036 "IPv4 packets forwarded", \

1037 NET\_STATS\_GET\_INSTANCE(dev\_id, sfx, ipv4\_forwarded), \

1038 "packet\_count", \

1039 NET\_STATS\_GET\_COLLECTOR\_NAME(dev\_id, sfx), \

1040 NET\_STATS\_GET\_VAR(dev\_id, sfx, ipv4\_forwarded), \

1041 &(iface)->stats.ipv4.forwarded)

1042#else

[ 1043](group__net__stats.md#gafa2e6de020b887512a3cebe75253fb18)#define NET\_STATS\_PROMETHEUS\_IPV4(iface, dev\_id, sfx)

1044#endif

1045

1046/\* ICMP layer statistics \*/

1047#if defined(CONFIG\_NET\_STATISTICS\_ICMP)

1048#define NET\_STATS\_PROMETHEUS\_ICMP(iface, dev\_id, sfx) \

1049 NET\_STATS\_PROMETHEUS\_COUNTER\_DEFINE( \

1050 "ICMP packets sent", \

1051 NET\_STATS\_GET\_INSTANCE(dev\_id, sfx, icmp\_sent), \

1052 "packet\_count", \

1053 NET\_STATS\_GET\_COLLECTOR\_NAME(dev\_id, sfx), \

1054 NET\_STATS\_GET\_VAR(dev\_id, sfx, icmp\_sent), \

1055 &(iface)->stats.icmp.sent); \

1056 NET\_STATS\_PROMETHEUS\_COUNTER\_DEFINE( \

1057 "ICMP packets received", \

1058 NET\_STATS\_GET\_INSTANCE(dev\_id, sfx, icmp\_recv), \

1059 "packet\_count", \

1060 NET\_STATS\_GET\_COLLECTOR\_NAME(dev\_id, sfx), \

1061 NET\_STATS\_GET\_VAR(dev\_id, sfx, icmp\_recv), \

1062 &(iface)->stats.icmp.recv); \

1063 NET\_STATS\_PROMETHEUS\_COUNTER\_DEFINE( \

1064 "ICMP packets dropped", \

1065 NET\_STATS\_GET\_INSTANCE(dev\_id, sfx, icmp\_drop), \

1066 "packet\_count", \

1067 NET\_STATS\_GET\_COLLECTOR\_NAME(dev\_id, sfx), \

1068 NET\_STATS\_GET\_VAR(dev\_id, sfx, icmp\_drop), \

1069 &(iface)->stats.icmp.drop); \

1070 NET\_STATS\_PROMETHEUS\_COUNTER\_DEFINE( \

1071 "ICMP packets checksum error", \

1072 NET\_STATS\_GET\_INSTANCE(dev\_id, sfx, icmp\_chkerr), \

1073 "packet\_count", \

1074 NET\_STATS\_GET\_COLLECTOR\_NAME(dev\_id, sfx), \

1075 NET\_STATS\_GET\_VAR(dev\_id, sfx, icmp\_chkerr), \

1076 &(iface)->stats.icmp.chkerr); \

1077 NET\_STATS\_PROMETHEUS\_COUNTER\_DEFINE( \

1078 "ICMP packets type error", \

1079 NET\_STATS\_GET\_INSTANCE(dev\_id, sfx, icmp\_typeerr), \

1080 "packet\_count", \

1081 NET\_STATS\_GET\_COLLECTOR\_NAME(dev\_id, sfx), \

1082 NET\_STATS\_GET\_VAR(dev\_id, sfx, icmp\_typeerr), \

1083 &(iface)->stats.icmp.typeerr)

1084#else

[ 1085](group__net__stats.md#ga96beec38aeb91a9d95b4e1e415c0d229)#define NET\_STATS\_PROMETHEUS\_ICMP(iface, dev\_id, sfx)

1086#endif

1087

1088/\* UDP layer statistics \*/

1089#if defined(CONFIG\_NET\_STATISTICS\_UDP)

1090#define NET\_STATS\_PROMETHEUS\_UDP(iface, dev\_id, sfx) \

1091 NET\_STATS\_PROMETHEUS\_COUNTER\_DEFINE( \

1092 "UDP packets sent", \

1093 NET\_STATS\_GET\_INSTANCE(dev\_id, sfx, udp\_sent), \

1094 "packet\_count", \

1095 NET\_STATS\_GET\_COLLECTOR\_NAME(dev\_id, sfx), \

1096 NET\_STATS\_GET\_VAR(dev\_id, sfx, udp\_sent), \

1097 &(iface)->stats.udp.sent); \

1098 NET\_STATS\_PROMETHEUS\_COUNTER\_DEFINE( \

1099 "UDP packets received", \

1100 NET\_STATS\_GET\_INSTANCE(dev\_id, sfx, udp\_recv), \

1101 "packet\_count", \

1102 NET\_STATS\_GET\_COLLECTOR\_NAME(dev\_id, sfx), \

1103 NET\_STATS\_GET\_VAR(dev\_id, sfx, udp\_recv), \

1104 &(iface)->stats.udp.recv); \

1105 NET\_STATS\_PROMETHEUS\_COUNTER\_DEFINE( \

1106 "UDP packets dropped", \

1107 NET\_STATS\_GET\_INSTANCE(dev\_id, sfx, udp\_drop), \

1108 "packet\_count", \

1109 NET\_STATS\_GET\_COLLECTOR\_NAME(dev\_id, sfx), \

1110 NET\_STATS\_GET\_VAR(dev\_id, sfx, udp\_drop), \

1111 &(iface)->stats.udp.drop); \

1112 NET\_STATS\_PROMETHEUS\_COUNTER\_DEFINE( \

1113 "UDP packets checksum error", \

1114 NET\_STATS\_GET\_INSTANCE(dev\_id, sfx, udp\_chkerr), \

1115 "packet\_count", \

1116 NET\_STATS\_GET\_COLLECTOR\_NAME(dev\_id, sfx), \

1117 NET\_STATS\_GET\_VAR(dev\_id, sfx, udp\_chkerr), \

1118 &(iface)->stats.udp.chkerr)

1119#else

[ 1120](group__net__stats.md#ga2d400caf2103d6718bc2871abba3eddb)#define NET\_STATS\_PROMETHEUS\_UDP(iface, dev\_id, sfx)

1121#endif

1122

1123/\* TCP layer statistics \*/

1124#if defined(CONFIG\_NET\_STATISTICS\_TCP)

1125#define NET\_STATS\_PROMETHEUS\_TCP(iface, dev\_id, sfx) \

1126 NET\_STATS\_PROMETHEUS\_COUNTER\_DEFINE( \

1127 "TCP bytes sent", \

1128 NET\_STATS\_GET\_INSTANCE(dev\_id, sfx, tcp\_bytes\_sent), \

1129 "byte\_count", \

1130 NET\_STATS\_GET\_COLLECTOR\_NAME(dev\_id, sfx), \

1131 NET\_STATS\_GET\_VAR(dev\_id, sfx, tcp\_bytes\_sent), \

1132 &(iface)->stats.tcp.bytes.sent); \

1133 NET\_STATS\_PROMETHEUS\_COUNTER\_DEFINE( \

1134 "TCP bytes received", \

1135 NET\_STATS\_GET\_INSTANCE(dev\_id, sfx, tcp\_bytes\_recv), \

1136 "byte\_count", \

1137 NET\_STATS\_GET\_COLLECTOR\_NAME(dev\_id, sfx), \

1138 NET\_STATS\_GET\_VAR(dev\_id, sfx, tcp\_bytes\_recv), \

1139 &(iface)->stats.tcp.bytes.received); \

1140 NET\_STATS\_PROMETHEUS\_COUNTER\_DEFINE( \

1141 "TCP bytes resent", \

1142 NET\_STATS\_GET\_INSTANCE(dev\_id, sfx, tcp\_bytes\_resent), \

1143 "byte\_count", \

1144 NET\_STATS\_GET\_COLLECTOR\_NAME(dev\_id, sfx), \

1145 NET\_STATS\_GET\_VAR(dev\_id, sfx, tcp\_bytes\_resent), \

1146 &(iface)->stats.tcp.resent); \

1147 NET\_STATS\_PROMETHEUS\_COUNTER\_DEFINE( \

1148 "TCP packets sent", \

1149 NET\_STATS\_GET\_INSTANCE(dev\_id, sfx, tcp\_sent), \

1150 "packet\_count", \

1151 NET\_STATS\_GET\_COLLECTOR\_NAME(dev\_id, sfx), \

1152 NET\_STATS\_GET\_VAR(dev\_id, sfx, tcp\_sent), \

1153 &(iface)->stats.tcp.sent); \

1154 NET\_STATS\_PROMETHEUS\_COUNTER\_DEFINE( \

1155 "TCP packets received", \

1156 NET\_STATS\_GET\_INSTANCE(dev\_id, sfx, tcp\_recv), \

1157 "packet\_count", \

1158 NET\_STATS\_GET\_COLLECTOR\_NAME(dev\_id, sfx), \

1159 NET\_STATS\_GET\_VAR(dev\_id, sfx, tcp\_recv), \

1160 &(iface)->stats.tcp.recv); \

1161 NET\_STATS\_PROMETHEUS\_COUNTER\_DEFINE( \

1162 "TCP packets dropped", \

1163 NET\_STATS\_GET\_INSTANCE(dev\_id, sfx, tcp\_drop), \

1164 "packet\_count", \

1165 NET\_STATS\_GET\_COLLECTOR\_NAME(dev\_id, sfx), \

1166 NET\_STATS\_GET\_VAR(dev\_id, sfx, tcp\_drop), \

1167 &(iface)->stats.tcp.drop); \

1168 NET\_STATS\_PROMETHEUS\_COUNTER\_DEFINE( \

1169 "TCP packets checksum error", \

1170 NET\_STATS\_GET\_INSTANCE(dev\_id, sfx, tcp\_chkerr), \

1171 "packet\_count", \

1172 NET\_STATS\_GET\_COLLECTOR\_NAME(dev\_id, sfx), \

1173 NET\_STATS\_GET\_VAR(dev\_id, sfx, tcp\_chkerr), \

1174 &(iface)->stats.tcp.chkerr); \

1175 NET\_STATS\_PROMETHEUS\_COUNTER\_DEFINE( \

1176 "TCP packets ack error", \

1177 NET\_STATS\_GET\_INSTANCE(dev\_id, sfx, tcp\_ackerr), \

1178 "packet\_count", \

1179 NET\_STATS\_GET\_COLLECTOR\_NAME(dev\_id, sfx), \

1180 NET\_STATS\_GET\_VAR(dev\_id, sfx, tcp\_ackerr), \

1181 &(iface)->stats.tcp.ackerr); \

1182 NET\_STATS\_PROMETHEUS\_COUNTER\_DEFINE( \

1183 "TCP packets reset error", \

1184 NET\_STATS\_GET\_INSTANCE(dev\_id, sfx, tcp\_rsterr), \

1185 "packet\_count", \

1186 NET\_STATS\_GET\_COLLECTOR\_NAME(dev\_id, sfx), \

1187 NET\_STATS\_GET\_VAR(dev\_id, sfx, tcp\_rsterr), \

1188 &(iface)->stats.tcp.rsterr); \

1189 NET\_STATS\_PROMETHEUS\_COUNTER\_DEFINE( \

1190 "TCP packets retransmitted", \

1191 NET\_STATS\_GET\_INSTANCE(dev\_id, sfx, tcp\_rexmit), \

1192 "packet\_count", \

1193 NET\_STATS\_GET\_COLLECTOR\_NAME(dev\_id, sfx), \

1194 NET\_STATS\_GET\_VAR(dev\_id, sfx, tcp\_rexmit), \

1195 &(iface)->stats.tcp.rexmit); \

1196 NET\_STATS\_PROMETHEUS\_COUNTER\_DEFINE( \

1197 "TCP reset received", \

1198 NET\_STATS\_GET\_INSTANCE(dev\_id, sfx, tcp\_rst\_recv), \

1199 "packet\_count", \

1200 NET\_STATS\_GET\_COLLECTOR\_NAME(dev\_id, sfx), \

1201 NET\_STATS\_GET\_VAR(dev\_id, sfx, tcp\_rst), \

1202 &(iface)->stats.tcp.rst); \

1203 NET\_STATS\_PROMETHEUS\_COUNTER\_DEFINE( \

1204 "TCP connection drop", \

1205 NET\_STATS\_GET\_INSTANCE(dev\_id, sfx, tcp\_conndrop), \

1206 "packet\_count", \

1207 NET\_STATS\_GET\_COLLECTOR\_NAME(dev\_id, sfx), \

1208 NET\_STATS\_GET\_VAR(dev\_id, sfx, tcp\_conndrop), \

1209 &(iface)->stats.tcp.conndrop); \

1210 NET\_STATS\_PROMETHEUS\_COUNTER\_DEFINE( \

1211 "TCP connection reset", \

1212 NET\_STATS\_GET\_INSTANCE(dev\_id, sfx, tcp\_connrst), \

1213 "packet\_count", \

1214 NET\_STATS\_GET\_COLLECTOR\_NAME(dev\_id, sfx), \

1215 NET\_STATS\_GET\_VAR(dev\_id, sfx, tcp\_connrst), \

1216 &(iface)->stats.tcp.connrst)

1217#else

[ 1218](group__net__stats.md#ga1b581725d1a8652a0b40e71ac2e99261)#define NET\_STATS\_PROMETHEUS\_TCP(iface, dev\_id, sfx)

1219#endif

1220

1221/\* IPv6 Neighbor Discovery statistics \*/

1222#if defined(CONFIG\_NET\_STATISTICS\_IPV6\_ND)

1223#define NET\_STATS\_PROMETHEUS\_IPV6\_ND(iface, dev\_id, sfx) \

1224 NET\_STATS\_PROMETHEUS\_COUNTER\_DEFINE( \

1225 "IPv6 ND packets sent", \

1226 NET\_STATS\_GET\_INSTANCE(dev\_id, sfx, ipv6\_nd\_sent), \

1227 "packet\_count", \

1228 NET\_STATS\_GET\_COLLECTOR\_NAME(dev\_id, sfx), \

1229 NET\_STATS\_GET\_VAR(dev\_id, sfx, ipv6\_nd\_sent), \

1230 &(iface)->stats.ipv6\_nd.sent); \

1231 NET\_STATS\_PROMETHEUS\_COUNTER\_DEFINE( \

1232 "IPv6 ND packets received", \

1233 NET\_STATS\_GET\_INSTANCE(dev\_id, sfx, ipv6\_nd\_recv), \

1234 "packet\_count", \

1235 NET\_STATS\_GET\_COLLECTOR\_NAME(dev\_id, sfx), \

1236 NET\_STATS\_GET\_VAR(dev\_id, sfx, ipv6\_nd\_recv), \

1237 &(iface)->stats.ipv6\_nd.recv); \

1238 NET\_STATS\_PROMETHEUS\_COUNTER\_DEFINE( \

1239 "IPv6 ND packets dropped", \

1240 NET\_STATS\_GET\_INSTANCE(dev\_id, sfx, ipv6\_nd\_drop), \

1241 "packet\_count", \

1242 NET\_STATS\_GET\_COLLECTOR\_NAME(dev\_id, sfx), \

1243 NET\_STATS\_GET\_VAR(dev\_id, sfx, ipv6\_nd\_drop), \

1244 &(iface)->stats.ipv6\_nd.drop)

1245#else

[ 1246](group__net__stats.md#ga1cc29c5da3740b2623fd625f9f360c6d)#define NET\_STATS\_PROMETHEUS\_IPV6\_ND(iface, dev\_id, sfx)

1247#endif

1248

1249/\* IPv6 Path MTU Discovery statistics \*/

1250#if defined(CONFIG\_NET\_STATISTICS\_IPV6\_PMTU)

1251#define NET\_STATS\_PROMETHEUS\_IPV6\_PMTU(iface, dev\_id, sfx) \

1252 NET\_STATS\_PROMETHEUS\_COUNTER\_DEFINE( \

1253 "IPv6 PMTU packets sent", \

1254 NET\_STATS\_GET\_INSTANCE(dev\_id, sfx, ipv6\_pmtu\_sent), \

1255 "packet\_count", \

1256 NET\_STATS\_GET\_COLLECTOR\_NAME(dev\_id, sfx), \

1257 NET\_STATS\_GET\_VAR(dev\_id, sfx, ipv6\_pmtu\_sent), \

1258 &(iface)->stats.ipv6\_pmtu.sent); \

1259 NET\_STATS\_PROMETHEUS\_COUNTER\_DEFINE( \

1260 "IPv6 PMTU packets received", \

1261 NET\_STATS\_GET\_INSTANCE(dev\_id, sfx, ipv6\_pmtu\_recv), \

1262 "packet\_count", \

1263 NET\_STATS\_GET\_COLLECTOR\_NAME(dev\_id, sfx), \

1264 NET\_STATS\_GET\_VAR(dev\_id, sfx, ipv6\_pmtu\_recv), \

1265 &(iface)->stats.ipv6\_pmtu.recv); \

1266 NET\_STATS\_PROMETHEUS\_COUNTER\_DEFINE( \

1267 "IPv6 PMTU packets dropped", \

1268 NET\_STATS\_GET\_INSTANCE(dev\_id, sfx, ipv6\_pmtu\_drop), \

1269 "packet\_count", \

1270 NET\_STATS\_GET\_COLLECTOR\_NAME(dev\_id, sfx), \

1271 NET\_STATS\_GET\_VAR(dev\_id, sfx, ipv6\_pmtu\_drop), \

1272 &(iface)->stats.ipv6\_pmtu.drop)

1273#else

[ 1274](group__net__stats.md#ga2593a73001deea960ccfb80cf71489d4)#define NET\_STATS\_PROMETHEUS\_IPV6\_PMTU(iface, dev\_id, sfx)

1275#endif

1276

1277/\* IPv4 Path MTU Discovery statistics \*/

1278#if defined(CONFIG\_NET\_STATISTICS\_IPV4\_PMTU)

1279#define NET\_STATS\_PROMETHEUS\_IPV4\_PMTU(iface, dev\_id, sfx) \

1280 NET\_STATS\_PROMETHEUS\_COUNTER\_DEFINE( \

1281 "IPv4 PMTU packets sent", \

1282 NET\_STATS\_GET\_INSTANCE(dev\_id, sfx, ipv4\_pmtu\_sent), \

1283 "packet\_count", \

1284 NET\_STATS\_GET\_COLLECTOR\_NAME(dev\_id, sfx), \

1285 NET\_STATS\_GET\_VAR(dev\_id, sfx, ipv4\_pmtu\_sent), \

1286 &(iface)->stats.ipv4\_pmtu.sent); \

1287 NET\_STATS\_PROMETHEUS\_COUNTER\_DEFINE( \

1288 "IPv4 PMTU packets received", \

1289 NET\_STATS\_GET\_INSTANCE(dev\_id, sfx, ipv4\_pmtu\_recv), \

1290 "packet\_count", \

1291 NET\_STATS\_GET\_COLLECTOR\_NAME(dev\_id, sfx), \

1292 NET\_STATS\_GET\_VAR(dev\_id, sfx, ipv4\_pmtu\_recv), \

1293 &(iface)->stats.ipv4\_pmtu.recv); \

1294 NET\_STATS\_PROMETHEUS\_COUNTER\_DEFINE( \

1295 "IPv4 PMTU packets dropped", \

1296 NET\_STATS\_GET\_INSTANCE(dev\_id, sfx, ipv4\_pmtu\_drop), \

1297 "packet\_count", \

1298 NET\_STATS\_GET\_COLLECTOR\_NAME(dev\_id, sfx), \

1299 NET\_STATS\_GET\_VAR(dev\_id, sfx, ipv4\_pmtu\_drop), \

1300 &(iface)->stats.ipv4\_pmtu.drop)

1301#else

[ 1302](group__net__stats.md#gaaa0bc9dd9f53da03492d10c399db8eab)#define NET\_STATS\_PROMETHEUS\_IPV4\_PMTU(iface, dev\_id, sfx)

1303#endif

1304

1305/\* IPv6 Multicast Listener Discovery statistics \*/

1306#if defined(CONFIG\_NET\_STATISTICS\_MLD)

1307#define NET\_STATS\_PROMETHEUS\_MLD(iface, dev\_id, sfx) \

1308 NET\_STATS\_PROMETHEUS\_COUNTER\_DEFINE( \

1309 "IPv6 MLD packets sent", \

1310 NET\_STATS\_GET\_INSTANCE(dev\_id, sfx, ipv6\_mld\_sent), \

1311 "packet\_count", \

1312 NET\_STATS\_GET\_COLLECTOR\_NAME(dev\_id, sfx), \

1313 NET\_STATS\_GET\_VAR(dev\_id, sfx, ipv6\_mld\_sent), \

1314 &(iface)->stats.ipv6\_mld.sent); \

1315 NET\_STATS\_PROMETHEUS\_COUNTER\_DEFINE( \

1316 "IPv6 MLD packets received", \

1317 NET\_STATS\_GET\_INSTANCE(dev\_id, sfx, ipv6\_mld\_recv), \

1318 "packet\_count", \

1319 NET\_STATS\_GET\_COLLECTOR\_NAME(dev\_id, sfx), \

1320 NET\_STATS\_GET\_VAR(dev\_id, sfx, ipv6\_mld\_recv), \

1321 &(iface)->stats.ipv6\_mld.recv); \

1322 NET\_STATS\_PROMETHEUS\_COUNTER\_DEFINE( \

1323 "IPv6 MLD packets dropped", \

1324 NET\_STATS\_GET\_INSTANCE(dev\_id, sfx, ipv6\_mld\_drop), \

1325 "packet\_count", \

1326 NET\_STATS\_GET\_COLLECTOR\_NAME(dev\_id, sfx), \

1327 NET\_STATS\_GET\_VAR(dev\_id, sfx, ipv6\_mld\_drop), \

1328 &(iface)->stats.ipv6\_mld.drop)

1329#else

[ 1330](group__net__stats.md#ga5c4827a519269cc00323dfe57921117b)#define NET\_STATS\_PROMETHEUS\_MLD(iface, dev\_id, sfx)

1331#endif

1332

1333/\* IPv4 IGMP statistics \*/

1334#if defined(CONFIG\_NET\_STATISTICS\_IGMP)

1335#define NET\_STATS\_PROMETHEUS\_IGMP(iface, dev\_id, sfx) \

1336 NET\_STATS\_PROMETHEUS\_COUNTER\_DEFINE( \

1337 "IPv4 IGMP packets sent", \

1338 NET\_STATS\_GET\_INSTANCE(dev\_id, sfx, ipv4\_igmp\_sent), \

1339 "packet\_count", \

1340 NET\_STATS\_GET\_COLLECTOR\_NAME(dev\_id, sfx), \

1341 NET\_STATS\_GET\_VAR(dev\_id, sfx, ipv4\_igmp\_sent), \

1342 &(iface)->stats.ipv4\_igmp.sent); \

1343 NET\_STATS\_PROMETHEUS\_COUNTER\_DEFINE( \

1344 "IPv4 IGMP packets received", \

1345 NET\_STATS\_GET\_INSTANCE(dev\_id, sfx, ipv4\_igmp\_recv), \

1346 "packet\_count", \

1347 NET\_STATS\_GET\_COLLECTOR\_NAME(dev\_id, sfx), \

1348 NET\_STATS\_GET\_VAR(dev\_id, sfx, ipv4\_igmp\_recv), \

1349 &(iface)->stats.ipv4\_igmp.recv); \

1350 NET\_STATS\_PROMETHEUS\_COUNTER\_DEFINE( \

1351 "IPv4 IGMP packets dropped", \

1352 NET\_STATS\_GET\_INSTANCE(dev\_id, sfx, ipv4\_igmp\_drop), \

1353 "packet\_count", \

1354 NET\_STATS\_GET\_COLLECTOR\_NAME(dev\_id, sfx), \

1355 NET\_STATS\_GET\_VAR(dev\_id, sfx, ipv4\_igmp\_drop), \

1356 &(iface)->stats.ipv4\_igmp.drop)

1357#else

[ 1358](group__net__stats.md#ga8782a593de8ae207e57abfcc9477e256)#define NET\_STATS\_PROMETHEUS\_IGMP(iface, dev\_id, sfx)

1359#endif

1360

1361/\* DNS statistics \*/

1362#if defined(CONFIG\_NET\_STATISTICS\_DNS)

1363#define NET\_STATS\_PROMETHEUS\_DNS(iface, dev\_id, sfx) \

1364 NET\_STATS\_PROMETHEUS\_COUNTER\_DEFINE( \

1365 "DNS packets sent", \

1366 NET\_STATS\_GET\_INSTANCE(dev\_id, sfx, dns\_sent), \

1367 "packet\_count", \

1368 NET\_STATS\_GET\_COLLECTOR\_NAME(dev\_id, sfx), \

1369 NET\_STATS\_GET\_VAR(dev\_id, sfx, dns\_sent), \

1370 &(iface)->stats.dns.sent); \

1371 NET\_STATS\_PROMETHEUS\_COUNTER\_DEFINE( \

1372 "DNS packets received", \

1373 NET\_STATS\_GET\_INSTANCE(dev\_id, sfx, dns\_recv), \

1374 "packet\_count", \

1375 NET\_STATS\_GET\_COLLECTOR\_NAME(dev\_id, sfx), \

1376 NET\_STATS\_GET\_VAR(dev\_id, sfx, dns\_recv), \

1377 &(iface)->stats.dns.recv); \

1378 NET\_STATS\_PROMETHEUS\_COUNTER\_DEFINE( \

1379 "DNS packets dropped", \

1380 NET\_STATS\_GET\_INSTANCE(dev\_id, sfx, dns\_drop), \

1381 "packet\_count", \

1382 NET\_STATS\_GET\_COLLECTOR\_NAME(dev\_id, sfx), \

1383 NET\_STATS\_GET\_VAR(dev\_id, sfx, dns\_drop), \

1384 &(iface)->stats.dns.drop)

1385#else

[ 1386](group__net__stats.md#gaef54299a895568956cbae9960c7bf844)#define NET\_STATS\_PROMETHEUS\_DNS(iface, dev\_id, sfx)

1387#endif

1388

1389/\* TX time statistics \*/

1390#if defined(CONFIG\_NET\_PKT\_TXTIME\_STATS)

1391#define NET\_STATS\_PROMETHEUS\_TX\_TIME(iface, dev\_id, sfx) \

1392 NET\_STATS\_PROMETHEUS\_SUMMARY\_DEFINE( \

1393 "TX time in microseconds", \

1394 NET\_STATS\_GET\_INSTANCE(dev\_id, sfx, tx\_time), \

1395 "time", \

1396 NET\_STATS\_GET\_COLLECTOR\_NAME(dev\_id, sfx), \

1397 NET\_STATS\_GET\_VAR(dev\_id, sfx, tx\_time), \

1398 &(iface)->stats.tx\_time)

1399#else

[ 1400](group__net__stats.md#gaf0c1ee536e8a816c537b6cf7344353f4)#define NET\_STATS\_PROMETHEUS\_TX\_TIME(iface, dev\_id, sfx)

1401#endif

1402

1403/\* RX time statistics \*/

1404#if defined(CONFIG\_NET\_PKT\_RXTIME\_STATS)

1405#define NET\_STATS\_PROMETHEUS\_RX\_TIME(iface, dev\_id, sfx) \

1406 NET\_STATS\_PROMETHEUS\_SUMMARY\_DEFINE( \

1407 "RX time in microseconds", \

1408 NET\_STATS\_GET\_INSTANCE(dev\_id, sfx, rx\_time), \

1409 "time", \

1410 NET\_STATS\_GET\_COLLECTOR\_NAME(dev\_id, sfx), \

1411 NET\_STATS\_GET\_VAR(dev\_id, sfx, rx\_time), \

1412 &(iface)->stats.rx\_time)

1413#else

[ 1414](group__net__stats.md#ga2b9c4b3dc4cd1cd2b79801e7a4b58849)#define NET\_STATS\_PROMETHEUS\_RX\_TIME(iface, dev\_id, sfx)

1415#endif

1416

[ 1417](group__net__stats.md#ga3c3413463adef85973626716e19e05d6)#define NET\_STATS\_PROMETHEUS\_PKT\_FILTER\_IPV4(iface, dev\_id, sfx) \

1418 NET\_STATS\_PROMETHEUS\_COUNTER\_DEFINE( \

1419 "Packet filter RX IPv4 drop", \

1420 NET\_STATS\_GET\_INSTANCE(dev\_id, sfx, pkt\_filter\_rx\_ipv4\_drop), \

1421 "packet\_count", \

1422 NET\_STATS\_GET\_COLLECTOR\_NAME(dev\_id, sfx), \

1423 NET\_STATS\_GET\_VAR(dev\_id, sfx, pkt\_filter\_rx\_ipv4\_drop),\

1424 &(iface)->stats.pkt\_filter.rx.ipv4\_drop);

1425

[ 1426](group__net__stats.md#ga94763ab89bb97f832f43e4d09d34edd7)#define NET\_STATS\_PROMETHEUS\_PKT\_FILTER\_IPV6(iface, dev\_id, sfx) \

1427 NET\_STATS\_PROMETHEUS\_COUNTER\_DEFINE( \

1428 "Packet filter RX IPv6 drop", \

1429 NET\_STATS\_GET\_INSTANCE(dev\_id, sfx, pkt\_filter\_rx\_ipv6\_drop), \

1430 "packet\_count", \

1431 NET\_STATS\_GET\_COLLECTOR\_NAME(dev\_id, sfx), \

1432 NET\_STATS\_GET\_VAR(dev\_id, sfx, pkt\_filter\_rx\_ipv6\_drop),\

1433 &(iface)->stats.pkt\_filter.rx.ipv6\_drop);

1434

[ 1435](group__net__stats.md#gac53b62a898db85f469eed307b3852247)#define NET\_STATS\_PROMETHEUS\_PKT\_FILTER\_LOCAL(iface, dev\_id, sfx) \

1436 NET\_STATS\_PROMETHEUS\_COUNTER\_DEFINE( \

1437 "Packet filter RX local drop", \

1438 NET\_STATS\_GET\_INSTANCE(dev\_id, sfx, pkt\_filter\_rx\_local\_drop), \

1439 "packet\_count", \

1440 NET\_STATS\_GET\_COLLECTOR\_NAME(dev\_id, sfx), \

1441 NET\_STATS\_GET\_VAR(dev\_id, sfx, pkt\_filter\_rx\_local\_drop),\

1442 &(iface)->stats.pkt\_filter.rx.local\_drop);

1443

[ 1444](group__net__stats.md#ga347ee5863fd3501b5e3f7f04c8457bda)#define NET\_STATS\_PROMETHEUS\_PKT\_FILTER(iface, dev\_id, sfx) \

1445 NET\_STATS\_PROMETHEUS\_COUNTER\_DEFINE( \

1446 "Packet filter RX drop", \

1447 NET\_STATS\_GET\_INSTANCE(dev\_id, sfx, pkt\_filter\_rx\_drop),\

1448 "packet\_count", \

1449 NET\_STATS\_GET\_COLLECTOR\_NAME(dev\_id, sfx), \

1450 NET\_STATS\_GET\_VAR(dev\_id, sfx, pkt\_filter\_rx\_drop), \

1451 &(iface)->stats.pkt\_filter.rx.drop); \

1452 NET\_STATS\_PROMETHEUS\_COUNTER\_DEFINE( \

1453 "Packet filter TX drop", \

1454 NET\_STATS\_GET\_INSTANCE(dev\_id, sfx, pkt\_filter\_tx\_drop),\

1455 "packet\_count", \

1456 NET\_STATS\_GET\_COLLECTOR\_NAME(dev\_id, sfx), \

1457 NET\_STATS\_GET\_VAR(dev\_id, sfx, pkt\_filter\_tx\_drop), \

1458 &(iface)->stats.pkt\_filter.tx.drop); \

1459 IF\_ENABLED(CONFIG\_NET\_PKT\_FILTER\_IPV4\_HOOK, \

1460 (NET\_STATS\_PROMETHEUS\_PKT\_FILTER\_IPV4(iface, dev\_id, sfx))) \

1461 IF\_ENABLED(CONFIG\_NET\_PKT\_FILTER\_IPV6\_HOOK, \

1462 (NET\_STATS\_PROMETHEUS\_PKT\_FILTER\_IPV6(iface, dev\_id, sfx))) \

1463 IF\_ENABLED(CONFIG\_NET\_PKT\_FILTER\_LOCAL\_IN\_HOOK, \

1464 (NET\_STATS\_PROMETHEUS\_PKT\_FILTER\_LOCAL(iface, dev\_id, sfx)))

1465

1466/\* Per network interface statistics via Prometheus \*/

[ 1467](group__net__stats.md#gac79e6cd416c92f9d26843900a084b375)#define NET\_STATS\_PROMETHEUS(iface, dev\_id, sfx) \

1468 NET\_STATS\_PROMETHEUS\_COUNTER\_DEFINE( \

1469 "Processing error", \

1470 NET\_STATS\_GET\_INSTANCE(dev\_id, sfx, process\_error), \

1471 "error\_count", \

1472 NET\_STATS\_GET\_COLLECTOR\_NAME(dev\_id, sfx), \

1473 NET\_STATS\_GET\_VAR(dev\_id, sfx, processing\_error), \

1474 &(iface)->stats.processing\_error); \

1475 IF\_ENABLED(CONFIG\_NET\_STATISTICS\_PKT\_FILTER, \

1476 (NET\_STATS\_PROMETHEUS\_PKT\_FILTER(iface, dev\_id, sfx))) \

1477 /\* IP layer error statistics \*/ \

1478 NET\_STATS\_PROMETHEUS\_COUNTER\_DEFINE( \

1479 "IP proto error", \

1480 NET\_STATS\_GET\_INSTANCE(dev\_id, sfx, ip\_proto\_error), \

1481 "error\_count", \

1482 NET\_STATS\_GET\_COLLECTOR\_NAME(dev\_id, sfx), \

1483 NET\_STATS\_GET\_VAR(dev\_id, sfx, ip\_errors\_protoerr), \

1484 &(iface)->stats.ip\_errors.protoerr); \

1485 NET\_STATS\_PROMETHEUS\_COUNTER\_DEFINE( \

1486 "IP version/header len error", \

1487 NET\_STATS\_GET\_INSTANCE(dev\_id, sfx, ip\_vhl\_error), \

1488 "error\_count", \

1489 NET\_STATS\_GET\_COLLECTOR\_NAME(dev\_id, sfx), \

1490 NET\_STATS\_GET\_VAR(dev\_id, sfx, ip\_errors\_vhlerr), \

1491 &(iface)->stats.ip\_errors.vhlerr); \

1492 NET\_STATS\_PROMETHEUS\_COUNTER\_DEFINE( \

1493 "IP header len error (high byte)", \

1494 NET\_STATS\_GET\_INSTANCE(dev\_id, sfx, ip\_hblen\_error), \

1495 "error\_count", \

1496 NET\_STATS\_GET\_COLLECTOR\_NAME(dev\_id, sfx), \

1497 NET\_STATS\_GET\_VAR(dev\_id, sfx, ip\_errors\_hblenerr), \

1498 &(iface)->stats.ip\_errors.hblenerr); \

1499 NET\_STATS\_PROMETHEUS\_COUNTER\_DEFINE( \

1500 "IP header len error (low byte)", \

1501 NET\_STATS\_GET\_INSTANCE(dev\_id, sfx, ip\_lblen\_error), \

1502 "error\_count", \

1503 NET\_STATS\_GET\_COLLECTOR\_NAME(dev\_id, sfx), \

1504 NET\_STATS\_GET\_VAR(dev\_id, sfx, ip\_errors\_lblenerr), \

1505 &(iface)->stats.ip\_errors.lblenerr); \

1506 NET\_STATS\_PROMETHEUS\_COUNTER\_DEFINE( \

1507 "IP fragment error", \

1508 NET\_STATS\_GET\_INSTANCE(dev\_id, sfx, ip\_frag\_error), \

1509 "error\_count", \

1510 NET\_STATS\_GET\_COLLECTOR\_NAME(dev\_id, sfx), \

1511 NET\_STATS\_GET\_VAR(dev\_id, sfx, ip\_errors\_fragerr), \

1512 &(iface)->stats.ip\_errors.fragerr); \

1513 NET\_STATS\_PROMETHEUS\_COUNTER\_DEFINE( \

1514 "IP checksum error", \

1515 NET\_STATS\_GET\_INSTANCE(dev\_id, sfx, ip\_chk\_error), \

1516 "error\_count", \

1517 NET\_STATS\_GET\_COLLECTOR\_NAME(dev\_id, sfx), \

1518 NET\_STATS\_GET\_VAR(dev\_id, sfx, ip\_errors\_chkerr), \

1519 &(iface)->stats.ip\_errors.chkerr); \

1520 /\* General network statistics \*/ \

1521 NET\_STATS\_PROMETHEUS\_COUNTER\_DEFINE( \

1522 "Bytes received", \

1523 NET\_STATS\_GET\_INSTANCE(dev\_id, sfx, bytes\_recv), \

1524 "byte\_count", \

1525 NET\_STATS\_GET\_COLLECTOR\_NAME(dev\_id, sfx), \

1526 NET\_STATS\_GET\_VAR(dev\_id, sfx, bytes\_recv), \

1527 &(iface)->stats.bytes.received); \

1528 NET\_STATS\_PROMETHEUS\_COUNTER\_DEFINE( \

1529 "Bytes sent", \

1530 NET\_STATS\_GET\_INSTANCE(dev\_id, sfx, bytes\_sent), \

1531 "byte\_count", \

1532 NET\_STATS\_GET\_COLLECTOR\_NAME(dev\_id, sfx), \

1533 NET\_STATS\_GET\_VAR(dev\_id, sfx, bytes\_sent), \

1534 &(iface)->stats.bytes.sent); \

1535 NET\_STATS\_PROMETHEUS\_IPV6(iface, dev\_id, sfx); \

1536 NET\_STATS\_PROMETHEUS\_IPV4(iface, dev\_id, sfx); \

1537 NET\_STATS\_PROMETHEUS\_ICMP(iface, dev\_id, sfx); \

1538 NET\_STATS\_PROMETHEUS\_UDP(iface, dev\_id, sfx); \

1539 NET\_STATS\_PROMETHEUS\_TCP(iface, dev\_id, sfx); \

1540 NET\_STATS\_PROMETHEUS\_IPV6\_ND(iface, dev\_id, sfx); \

1541 NET\_STATS\_PROMETHEUS\_IPV6\_PMTU(iface, dev\_id, sfx); \

1542 NET\_STATS\_PROMETHEUS\_IPV4\_PMTU(iface, dev\_id, sfx); \

1543 NET\_STATS\_PROMETHEUS\_MLD(iface, dev\_id, sfx); \

1544 NET\_STATS\_PROMETHEUS\_IGMP(iface, dev\_id, sfx); \

1545 NET\_STATS\_PROMETHEUS\_DNS(iface, dev\_id, sfx); \

1546 NET\_STATS\_PROMETHEUS\_TX\_TIME(iface, dev\_id, sfx); \

1547 NET\_STATS\_PROMETHEUS\_RX\_TIME(iface, dev\_id, sfx)

1548

1552

1553#ifdef \_\_cplusplus

1554}

1555#endif

1556

1557#endif /\* ZEPHYR\_INCLUDE\_NET\_NET\_STATS\_H\_ \*/

[collector.h](collector_8h.md)

Prometheus collector APIs.

[gauge.h](gauge_8h.md)

Prometheus gauge APIs.

[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)

#define NET\_MGMT\_DEFINE\_REQUEST\_HANDLER(\_mgmt\_request)

Declare a request handler function for the given network event.

**Definition** net\_mgmt.h:129

[net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752)

uint32\_t net\_stats\_t

Network statistics counter.

**Definition** net\_stats.h:45

[histogram.h](histogram_8h.md)

Prometheus histogram APIs.

[types.h](include_2zephyr_2types_8h.md)

[metric.h](metric_8h.md)

Prometheus metric interface.

[counter.h](net_2prometheus_2counter_8h.md)

Prometheus counter APIs.

[net\_core.h](net__core_8h.md)

Network core definitions.

[net\_mgmt.h](net__mgmt_8h.md)

Network Management API public header.

[recv](posix_2sys_2socket_8h.md#adee01662b0cf762a014efd87ab811276)

ssize\_t recv(int sock, void \*buf, size\_t max\_len, int flags)

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

**Definition** net\_stats.h:50

[net\_stats\_bytes::sent](structnet__stats__bytes.md#a360bdbf177d60b0677beec2037f34cb0)

uint64\_t sent

Number of bytes sent.

**Definition** net\_stats.h:52

[net\_stats\_bytes::received](structnet__stats__bytes.md#a9f87e32d63bc4239ef7db03feedd495e)

uint64\_t received

Number of bytes received.

**Definition** net\_stats.h:54

[net\_stats\_dns](structnet__stats__dns.md)

DNS statistics.

**Definition** net\_stats.h:267

[net\_stats\_dns::drop](structnet__stats__dns.md#a04756603a183f35dbf6f55000556b546)

net\_stats\_t drop

Number of dropped DNS packets.

**Definition** net\_stats.h:275

[net\_stats\_dns::recv](structnet__stats__dns.md#abc9be2039a3ff9e62b956ae27fd0ab84)

net\_stats\_t recv

Number of received DNS queries.

**Definition** net\_stats.h:269

[net\_stats\_dns::sent](structnet__stats__dns.md#ac07b9f4d084b978cc11e7799fb71a435)

net\_stats\_t sent

Number of sent DNS responses.

**Definition** net\_stats.h:272

[net\_stats\_eth\_csum](structnet__stats__eth__csum.md)

Ethernet checksum statistics.

**Definition** net\_stats.h:590

[net\_stats\_eth\_csum::rx\_csum\_offload\_good](structnet__stats__eth__csum.md#a1f1ba5c01c6232cd739d069ddb871b17)

net\_stats\_t rx\_csum\_offload\_good

Number of good RX checksum offloading.

**Definition** net\_stats.h:592

[net\_stats\_eth\_csum::rx\_csum\_offload\_errors](structnet__stats__eth__csum.md#ac4fc04d66193070d4f52a4c07f29ccce)

net\_stats\_t rx\_csum\_offload\_errors

Number of failed RX checksum offloading.

**Definition** net\_stats.h:595

[net\_stats\_eth\_errors](structnet__stats__eth__errors.md)

Ethernet error statistics.

**Definition** net\_stats.h:511

[net\_stats\_eth\_errors::tx\_carrier\_errors](structnet__stats__eth__errors.md#a0043d1a1481040a6d7439bd23423ec12)

net\_stats\_t tx\_carrier\_errors

Number of TX carrier errors.

**Definition** net\_stats.h:549

[net\_stats\_eth\_errors::uncorr\_ecc\_errors](structnet__stats__eth__errors.md#a07d0a435f2129556520c732571d28edf)

net\_stats\_t uncorr\_ecc\_errors

Number of uncorrected ECC errors.

**Definition** net\_stats.h:564

[net\_stats\_eth\_errors::rx\_long\_length\_errors](structnet__stats__eth__errors.md#a0e83e270a35222ed3e927800be4159e7)

net\_stats\_t rx\_long\_length\_errors

Number of RX long length errors.

**Definition** net\_stats.h:531

[net\_stats\_eth\_errors::tx\_window\_errors](structnet__stats__eth__errors.md#a17624a12d6473bdd78698076fed0d122)

net\_stats\_t tx\_window\_errors

Number of TX window errors.

**Definition** net\_stats.h:558

[net\_stats\_eth\_errors::corr\_ecc\_errors](structnet__stats__eth__errors.md#a257113639f0e0e3085febb7a147f498f)

net\_stats\_t corr\_ecc\_errors

Number of corrected ECC errors.

**Definition** net\_stats.h:567

[net\_stats\_eth\_errors::rx\_missed\_errors](structnet__stats__eth__errors.md#a2d2b2c4e3764ebec841f1ecbe7058d99)

net\_stats\_t rx\_missed\_errors

Number of RX missed errors.

**Definition** net\_stats.h:528

[net\_stats\_eth\_errors::rx\_crc\_errors](structnet__stats__eth__errors.md#a4dab70cf219269bb393ce14faf0ed77e)

net\_stats\_t rx\_crc\_errors

Number of RX CRC errors.

**Definition** net\_stats.h:519

[net\_stats\_eth\_errors::rx\_short\_length\_errors](structnet__stats__eth__errors.md#a5e3d39d8417bb180cbfcb8c901006e81)

net\_stats\_t rx\_short\_length\_errors

Number of RX short length errors.

**Definition** net\_stats.h:534

[net\_stats\_eth\_errors::rx\_align\_errors](structnet__stats__eth__errors.md#a7618f10af3443c49a6e256bb41e77781)

net\_stats\_t rx\_align\_errors

Number of RX buffer align errors.

**Definition** net\_stats.h:537

[net\_stats\_eth\_errors::rx\_dma\_failed](structnet__stats__eth__errors.md#a7bcfbb13836f162ceeb5f021304b5c76)

net\_stats\_t rx\_dma\_failed

Number of RX DMA failed errors.

**Definition** net\_stats.h:540

[net\_stats\_eth\_errors::rx\_no\_buffer\_count](structnet__stats__eth__errors.md#a82622736d226b4d3b999f1f22ccf8529)

net\_stats\_t rx\_no\_buffer\_count

Number of RX net\_pkt allocation errors.

**Definition** net\_stats.h:525

[net\_stats\_eth\_errors::tx\_fifo\_errors](structnet__stats__eth__errors.md#a84630da9b82557f56dc35cd59ca2f7ae)

net\_stats\_t tx\_fifo\_errors

Number of TX FIFO errors.

**Definition** net\_stats.h:552

[net\_stats\_eth\_errors::rx\_frame\_errors](structnet__stats__eth__errors.md#a8dfcc5cd1b4decec5783d01ba7033b05)

net\_stats\_t rx\_frame\_errors

Number of RX frame errors.

**Definition** net\_stats.h:522

[net\_stats\_eth\_errors::rx\_over\_errors](structnet__stats__eth__errors.md#a9afee89f5bb01907e7cd515e2a0ff1b5)

net\_stats\_t rx\_over\_errors

Number of RX overrun errors.

**Definition** net\_stats.h:516

[net\_stats\_eth\_errors::tx\_dma\_failed](structnet__stats__eth__errors.md#abfbf6478b7afdd5935d7c6948c9ef426)

net\_stats\_t tx\_dma\_failed

Number of TX DMA failed errors.

**Definition** net\_stats.h:561

[net\_stats\_eth\_errors::rx\_length\_errors](structnet__stats__eth__errors.md#aca0e2e4807fa70279dee8ddaad2d7ef7)

net\_stats\_t rx\_length\_errors

Number of RX length errors.

**Definition** net\_stats.h:513

[net\_stats\_eth\_errors::rx\_buf\_alloc\_failed](structnet__stats__eth__errors.md#adbcae9c10c081f1cdf304bcdce740aa4)

net\_stats\_t rx\_buf\_alloc\_failed

Number of RX net\_buf allocation errors.

**Definition** net\_stats.h:543

[net\_stats\_eth\_errors::tx\_heartbeat\_errors](structnet__stats__eth__errors.md#ae2a13733c1a5f0cc3e00efca0c3f429d)

net\_stats\_t tx\_heartbeat\_errors

Number of TX heartbeat errors.

**Definition** net\_stats.h:555

[net\_stats\_eth\_errors::tx\_aborted\_errors](structnet__stats__eth__errors.md#afec6a7e24c6f3cc74dd9f739f27b3e48)

net\_stats\_t tx\_aborted\_errors

Number of TX aborted errors.

**Definition** net\_stats.h:546

[net\_stats\_eth\_flow](structnet__stats__eth__flow.md)

Ethernet flow control statistics.

**Definition** net\_stats.h:573

[net\_stats\_eth\_flow::rx\_flow\_control\_xon](structnet__stats__eth__flow.md#a08e5da4ff78fe3893b9c9a628cefe4f2)

net\_stats\_t rx\_flow\_control\_xon

Number of RX XON flow control.

**Definition** net\_stats.h:575

[net\_stats\_eth\_flow::tx\_flow\_control\_xon](structnet__stats__eth__flow.md#a31412e8bf9d38ba630ea856e958a48d7)

net\_stats\_t tx\_flow\_control\_xon

Number of TX XON flow control.

**Definition** net\_stats.h:581

[net\_stats\_eth\_flow::rx\_flow\_control\_xoff](structnet__stats__eth__flow.md#a8f9b93537b3c11be70f276aaa72cb637)

net\_stats\_t rx\_flow\_control\_xoff

Number of RX XOFF flow control.

**Definition** net\_stats.h:578

[net\_stats\_eth\_flow::tx\_flow\_control\_xoff](structnet__stats__eth__flow.md#a969d81f9db20312d2d2aa7f70f93bdd5)

net\_stats\_t tx\_flow\_control\_xoff

Number of TX XOFF flow control.

**Definition** net\_stats.h:584

[net\_stats\_eth\_hw\_timestamp](structnet__stats__eth__hw__timestamp.md)

Ethernet hardware timestamp statistics.

**Definition** net\_stats.h:601

[net\_stats\_eth\_hw\_timestamp::tx\_hwtstamp\_timeouts](structnet__stats__eth__hw__timestamp.md#a41f605499dbf88a879522fdfa4633d9e)

net\_stats\_t tx\_hwtstamp\_timeouts

Number of RX hardware timestamp timeout.

**Definition** net\_stats.h:606

[net\_stats\_eth\_hw\_timestamp::rx\_hwtstamp\_cleared](structnet__stats__eth__hw__timestamp.md#acd3d5f72d7df568110d96093e0c9534d)

net\_stats\_t rx\_hwtstamp\_cleared

Number of RX hardware timestamp cleared.

**Definition** net\_stats.h:603

[net\_stats\_eth\_hw\_timestamp::tx\_hwtstamp\_skipped](structnet__stats__eth__hw__timestamp.md#ae1f983faf4a999308c464e4af5a5284b)

net\_stats\_t tx\_hwtstamp\_skipped

Number of RX hardware timestamp skipped.

**Definition** net\_stats.h:609

[net\_stats\_eth](structnet__stats__eth.md)

All Ethernet specific statistics.

**Definition** net\_stats.h:625

[net\_stats\_eth::broadcast](structnet__stats__eth.md#a054beb909134b0e0f22f5df599549128)

struct net\_stats\_pkts broadcast

Total number of broadcast packets received and sent.

**Definition** net\_stats.h:633

[net\_stats\_eth::csum](structnet__stats__eth.md#a2169ae06bace1a93663bccf88c8d7a29)

struct net\_stats\_eth\_csum csum

Total number of checksum errors in RX and TX.

**Definition** net\_stats.h:648

[net\_stats\_eth::tx\_dropped](structnet__stats__eth.md#a257c349cf3d32d38796e3899e702454a)

net\_stats\_t tx\_dropped

Total number of dropped TX packets.

**Definition** net\_stats.h:657

[net\_stats\_eth::hw\_timestamp](structnet__stats__eth.md#a44667efff73c17c089ed22d5b0da5ad3)

struct net\_stats\_eth\_hw\_timestamp hw\_timestamp

Total number of hardware timestamp errors in RX and TX.

**Definition** net\_stats.h:651

[net\_stats\_eth::multicast](structnet__stats__eth.md#a4f6a2903330518a132e7e547820e0bf2)

struct net\_stats\_pkts multicast

Total number of multicast packets received and sent.

**Definition** net\_stats.h:636

[net\_stats\_eth::flow\_control](structnet__stats__eth.md#a643010ac6360c8c0c08016725ba12222)

struct net\_stats\_eth\_flow flow\_control

Total number of flow control errors in RX and TX.

**Definition** net\_stats.h:645

[net\_stats\_eth::tx\_restart\_queue](structnet__stats__eth.md#a6699012226e25e8bad39076fed6dbfb5)

net\_stats\_t tx\_restart\_queue

Total number of TX queue restarts.

**Definition** net\_stats.h:663

[net\_stats\_eth::collisions](structnet__stats__eth.md#a822d4205791f59999c842610522f6fc5)

net\_stats\_t collisions

Total number of collisions.

**Definition** net\_stats.h:654

[net\_stats\_eth::bytes](structnet__stats__eth.md#a8c5cf1ead8ba214425a16fed1c2ad0fb)

struct net\_stats\_bytes bytes

Total number of bytes received and sent.

**Definition** net\_stats.h:627

[net\_stats\_eth::error\_details](structnet__stats__eth.md#a922feddb17fc020371f1bcc52c709415)

struct net\_stats\_eth\_errors error\_details

Total number of errors in RX and TX.

**Definition** net\_stats.h:642

[net\_stats\_eth::pkts](structnet__stats__eth.md#a97bd6026b16890743f344751a21107f1)

struct net\_stats\_pkts pkts

Total number of packets received and sent.

**Definition** net\_stats.h:630

[net\_stats\_eth::errors](structnet__stats__eth.md#a9c869740f416fbe0b54d7fefacb1fe29)

struct net\_stats\_pkts errors

Total number of errors in RX and TX.

**Definition** net\_stats.h:639

[net\_stats\_eth::tx\_timeout\_count](structnet__stats__eth.md#ab351258ae82abd09759d37774559d8bc)

net\_stats\_t tx\_timeout\_count

Total number of TX timeout errors.

**Definition** net\_stats.h:660

[net\_stats\_eth::unknown\_protocol](structnet__stats__eth.md#afaacee7cc1d0a35ae2344175421c40dd)

net\_stats\_t unknown\_protocol

Total number of RX unknown protocol packets.

**Definition** net\_stats.h:666

[net\_stats\_icmp](structnet__stats__icmp.md)

ICMP statistics.

**Definition** net\_stats.h:114

[net\_stats\_icmp::sent](structnet__stats__icmp.md#a2d6eb7dfc8f4b439b399b039022f2889)

net\_stats\_t sent

Number of sent ICMP packets.

**Definition** net\_stats.h:119

[net\_stats\_icmp::chkerr](structnet__stats__icmp.md#a6662bc547107a08c52e902a2446629bf)

net\_stats\_t chkerr

Number of ICMP packets with a bad checksum.

**Definition** net\_stats.h:128

[net\_stats\_icmp::drop](structnet__stats__icmp.md#a755f3388c05d4bd2988ddd16d1a4cf32)

net\_stats\_t drop

Number of dropped ICMP packets.

**Definition** net\_stats.h:122

[net\_stats\_icmp::typeerr](structnet__stats__icmp.md#ae1a29dd9b8e1ce9a737fa7f36c805cd4)

net\_stats\_t typeerr

Number of ICMP packets with a wrong type.

**Definition** net\_stats.h:125

[net\_stats\_icmp::recv](structnet__stats__icmp.md#ae6f226b55565c11fca0c9e099f08c267)

net\_stats\_t recv

Number of received ICMP packets.

**Definition** net\_stats.h:116

[net\_stats\_ip\_errors](structnet__stats__ip__errors.md)

IP layer error statistics.

**Definition** net\_stats.h:87

[net\_stats\_ip\_errors::hblenerr](structnet__stats__ip__errors.md#a06b35742c418ebc6414fcb5c7002edde)

net\_stats\_t hblenerr

Number of packets dropped due to wrong IP length, high byte.

**Definition** net\_stats.h:94

[net\_stats\_ip\_errors::vhlerr](structnet__stats__ip__errors.md#a3e476f659ebeaa5c5f7b6dad2d90326f)

net\_stats\_t vhlerr

Number of packets dropped due to wrong IP version or header length.

**Definition** net\_stats.h:91

[net\_stats\_ip\_errors::chkerr](structnet__stats__ip__errors.md#a872cc0beca45bbe87ae794dd8ca4e301)

net\_stats\_t chkerr

Number of packets dropped due to IP checksum errors.

**Definition** net\_stats.h:103

[net\_stats\_ip\_errors::protoerr](structnet__stats__ip__errors.md#a978b1c23847e707ac1fa27c2b34fa85d)

net\_stats\_t protoerr

Number of packets dropped because they were neither ICMP, UDP nor TCP.

**Definition** net\_stats.h:108

[net\_stats\_ip\_errors::lblenerr](structnet__stats__ip__errors.md#a9b4bf05e9df13e1d99518125b9067bef)

net\_stats\_t lblenerr

Number of packets dropped due to wrong IP length, low byte.

**Definition** net\_stats.h:97

[net\_stats\_ip\_errors::fragerr](structnet__stats__ip__errors.md#ab84ee9dfbe5da391d60c6e3ae9abea16)

net\_stats\_t fragerr

Number of packets dropped because they were IP fragments.

**Definition** net\_stats.h:100

[net\_stats\_ip](structnet__stats__ip.md)

IP layer statistics.

**Definition** net\_stats.h:70

[net\_stats\_ip::forwarded](structnet__stats__ip.md#a4bb82a5ebebaa3e8a11973c07eed96a0)

net\_stats\_t forwarded

Number of forwarded packets at the IP layer.

**Definition** net\_stats.h:78

[net\_stats\_ip::recv](structnet__stats__ip.md#ab6a6373368dd24cb51504c5729d535d3)

net\_stats\_t recv

Number of received packets at the IP layer.

**Definition** net\_stats.h:72

[net\_stats\_ip::sent](structnet__stats__ip.md#abbe676bbe9faa89b2b6b8c4950b1c9d5)

net\_stats\_t sent

Number of sent packets at the IP layer.

**Definition** net\_stats.h:75

[net\_stats\_ip::drop](structnet__stats__ip.md#ac86399b70d7f761162e5336dd15589eb)

net\_stats\_t drop

Number of dropped packets at the IP layer.

**Definition** net\_stats.h:81

[net\_stats\_ipv4\_igmp](structnet__stats__ipv4__igmp.md)

IPv4 IGMP daemon statistics.

**Definition** net\_stats.h:253

[net\_stats\_ipv4\_igmp::drop](structnet__stats__ipv4__igmp.md#a1c37702ff837b8c5cc9df5f690e7678c)

net\_stats\_t drop

Number of dropped IPv4 IGMP packets.

**Definition** net\_stats.h:261

[net\_stats\_ipv4\_igmp::recv](structnet__stats__ipv4__igmp.md#a469113de7af0ba42dbd1b0365d00602c)

net\_stats\_t recv

Number of received IPv4 IGMP queries.

**Definition** net\_stats.h:255

[net\_stats\_ipv4\_igmp::sent](structnet__stats__ipv4__igmp.md#a955e20a6ee5e19e08000b3114b9d71a6)

net\_stats\_t sent

Number of sent IPv4 IGMP reports.

**Definition** net\_stats.h:258

[net\_stats\_ipv4\_pmtu](structnet__stats__ipv4__pmtu.md)

IPv4 Path MTU Discovery statistics.

**Definition** net\_stats.h:225

[net\_stats\_ipv4\_pmtu::sent](structnet__stats__ipv4__pmtu.md#a44f1028694d4001cd4a43f925f0bf0da)

net\_stats\_t sent

Number of sent IPv4 PMTU packets.

**Definition** net\_stats.h:233

[net\_stats\_ipv4\_pmtu::recv](structnet__stats__ipv4__pmtu.md#a64245eb7b9b1fcfa0f0efcb53eff7ec2)

net\_stats\_t recv

Number of received IPv4 PMTU packets.

**Definition** net\_stats.h:230

[net\_stats\_ipv4\_pmtu::drop](structnet__stats__ipv4__pmtu.md#ad35f9defad7c5ce29e510b8051788977)

net\_stats\_t drop

Number of dropped IPv4 PMTU packets.

**Definition** net\_stats.h:227

[net\_stats\_ipv6\_mld](structnet__stats__ipv6__mld.md)

IPv6 multicast listener daemon statistics.

**Definition** net\_stats.h:239

[net\_stats\_ipv6\_mld::recv](structnet__stats__ipv6__mld.md#a4879ff9e31f8b60973d3b169598e921d)

net\_stats\_t recv

Number of received IPv6 MLD queries.

**Definition** net\_stats.h:241

[net\_stats\_ipv6\_mld::sent](structnet__stats__ipv6__mld.md#ab397b74b14ce7047bf2fc63ca72ce1e5)

net\_stats\_t sent

Number of sent IPv6 MLD reports.

**Definition** net\_stats.h:244

[net\_stats\_ipv6\_mld::drop](structnet__stats__ipv6__mld.md#ad85dc87f57296a1e7d64e959b0370ee8)

net\_stats\_t drop

Number of dropped IPv6 MLD packets.

**Definition** net\_stats.h:247

[net\_stats\_ipv6\_nd](structnet__stats__ipv6__nd.md)

IPv6 neighbor discovery statistics.

**Definition** net\_stats.h:197

[net\_stats\_ipv6\_nd::sent](structnet__stats__ipv6__nd.md#a0129f7892a4439c20deb2f32b9001277)

net\_stats\_t sent

Number of sent IPv6 neighbor discovery packets.

**Definition** net\_stats.h:205

[net\_stats\_ipv6\_nd::recv](structnet__stats__ipv6__nd.md#a0bf6f67d9112996a3b002ea160aec769)

net\_stats\_t recv

Number of received IPv6 neighbor discovery packets.

**Definition** net\_stats.h:202

[net\_stats\_ipv6\_nd::drop](structnet__stats__ipv6__nd.md#a31074d5d44138fcabdc5f7750f9f2c47)

net\_stats\_t drop

Number of dropped IPv6 neighbor discovery packets.

**Definition** net\_stats.h:199

[net\_stats\_ipv6\_pmtu](structnet__stats__ipv6__pmtu.md)

IPv6 Path MTU Discovery statistics.

**Definition** net\_stats.h:211

[net\_stats\_ipv6\_pmtu::recv](structnet__stats__ipv6__pmtu.md#a66346cd9140e30727d77648f65345762)

net\_stats\_t recv

Number of received IPv6 PMTU packets.

**Definition** net\_stats.h:216

[net\_stats\_ipv6\_pmtu::drop](structnet__stats__ipv6__pmtu.md#a68b19ebb61e84eb876178a31c7a4e327)

net\_stats\_t drop

Number of dropped IPv6 PMTU packets.

**Definition** net\_stats.h:213

[net\_stats\_ipv6\_pmtu::sent](structnet__stats__ipv6__pmtu.md#a698f5794b73896f7a66def2d3209fafd)

net\_stats\_t sent

Number of sent IPv6 PMTU packets.

**Definition** net\_stats.h:219

[net\_stats\_pkt\_filter](structnet__stats__pkt__filter.md)

Network packet filter statistics.

**Definition** net\_stats.h:377

[net\_stats\_pkt\_filter::tx](structnet__stats__pkt__filter.md#a5e88001e143c0adb129ca93b108c277d)

struct net\_stats\_pkt\_filter::@217075202025176321036232161065136160020242373254 tx

Network packet filter TX statistics.

[net\_stats\_pkt\_filter::drop](structnet__stats__pkt__filter.md#a62d2d86781e6224b09f21929f27b2ef7)

net\_stats\_t drop

Network packets dropped at network interface level.

**Definition** net\_stats.h:381

[net\_stats\_pkt\_filter::rx](structnet__stats__pkt__filter.md#a8cf9912d574873832b85a614eb776789)

struct net\_stats\_pkt\_filter::@262141166207303052356016341171341105051217145307 rx

Network packet filter RX statistics.

[net\_stats\_pkts](structnet__stats__pkts.md)

Number of network packets sent and received.

**Definition** net\_stats.h:60

[net\_stats\_pkts::rx](structnet__stats__pkts.md#ac9784b5a245e6c57e39318aaf314f0cf)

net\_stats\_t rx

Number of packets received.

**Definition** net\_stats.h:64

[net\_stats\_pkts::tx](structnet__stats__pkts.md#aee1e302d0f8dac79b693a06d8fa3b3c5)

net\_stats\_t tx

Number of packets sent.

**Definition** net\_stats.h:62

[net\_stats\_pm](structnet__stats__pm.md)

Power management statistics.

**Definition** net\_stats.h:363

[net\_stats\_pm::last\_suspend\_time](structnet__stats__pm.md#a0bdf9c3676298e2df4ff3bfa03f5e823)

uint32\_t last\_suspend\_time

How long the last suspend took.

**Definition** net\_stats.h:369

[net\_stats\_pm::start\_time](structnet__stats__pm.md#a6784806eaa093431ed3c0f7acfe5a89c)

uint32\_t start\_time

Network interface last suspend start time.

**Definition** net\_stats.h:371

[net\_stats\_pm::overall\_suspend\_time](structnet__stats__pm.md#ab43935fcfe9efc1cd5f3e7e329996805)

uint64\_t overall\_suspend\_time

Total suspend time.

**Definition** net\_stats.h:365

[net\_stats\_pm::suspend\_count](structnet__stats__pm.md#ac14122a4765c499c045f18c70af355a0)

net\_stats\_t suspend\_count

How many times we were suspended.

**Definition** net\_stats.h:367

[net\_stats\_ppp](structnet__stats__ppp.md)

All PPP specific statistics.

**Definition** net\_stats.h:677

[net\_stats\_ppp::chkerr](structnet__stats__ppp.md#a1332b31980f82236aeb0c3f9444e2ac6)

net\_stats\_t chkerr

Number of received PPP frames with a bad checksum.

**Definition** net\_stats.h:688

[net\_stats\_ppp::pkts](structnet__stats__ppp.md#a71fc81f3c5f3e65a476b3391f086d340)

struct net\_stats\_pkts pkts

Total number of packets received and sent.

**Definition** net\_stats.h:682

[net\_stats\_ppp::bytes](structnet__stats__ppp.md#ab2b48da7f19d4b83e3f41b41979b7ed8)

struct net\_stats\_bytes bytes

Total number of bytes received and sent.

**Definition** net\_stats.h:679

[net\_stats\_ppp::drop](structnet__stats__ppp.md#ae2e0a47a539e9d7bc97f9c63f889b276)

net\_stats\_t drop

Number of received and dropped PPP frames.

**Definition** net\_stats.h:685

[net\_stats\_rx\_time](structnet__stats__rx__time.md)

Network packet receive times for calculating average RX time.

**Definition** net\_stats.h:292

[net\_stats\_rx\_time::sum](structnet__stats__rx__time.md#a4b84c2ae2fda8fcd75fdf1bf0b2aae8d)

uint64\_t sum

Sum of network packet receive times.

**Definition** net\_stats.h:294

[net\_stats\_rx\_time::count](structnet__stats__rx__time.md#a68247051b064de081fa2e84118192958)

net\_stats\_t count

Number of network packets received.

**Definition** net\_stats.h:297

[net\_stats\_sta\_mgmt](structnet__stats__sta__mgmt.md)

All Wi-Fi management statistics.

**Definition** net\_stats.h:694

[net\_stats\_sta\_mgmt::beacons\_miss](structnet__stats__sta__mgmt.md#a29ae0079b4c780e0de2656a85ec15fe9)

net\_stats\_t beacons\_miss

Number of missed beacons.

**Definition** net\_stats.h:699

[net\_stats\_sta\_mgmt::beacons\_rx](structnet__stats__sta__mgmt.md#ac6e68fded8e19b20259442436923f815)

net\_stats\_t beacons\_rx

Number of received beacons.

**Definition** net\_stats.h:696

[net\_stats\_tc](structnet__stats__tc.md)

Traffic class statistics.

**Definition** net\_stats.h:319

[net\_stats\_tc::dropped](structnet__stats__tc.md#a1794f71f7fe7b3d20d406be4b28eb032)

net\_stats\_t dropped

Number of packets dropped for this traffic class.

**Definition** net\_stats.h:334

[net\_stats\_tc::tx\_time](structnet__stats__tc.md#a30288ef3bb0796cd18c3cf0aedbe875a)

struct net\_stats\_tx\_time tx\_time

Helper for calculating average TX time statistics.

**Definition** net\_stats.h:325

[net\_stats\_tc::pkts](structnet__stats__tc.md#a6614b5f5186635415a7d787260c39248)

net\_stats\_t pkts

Number of packets sent for this traffic class.

**Definition** net\_stats.h:332

[net\_stats\_tc::bytes](structnet__stats__tc.md#a74b471b77fb1c72933daa656319cc2af)

uint64\_t bytes

Number of bytes sent for this traffic class.

**Definition** net\_stats.h:323

[net\_stats\_tc::priority](structnet__stats__tc.md#a8a5c2e59990407ddbfc7973a1c183bf6)

uint8\_t priority

Priority of this traffic class.

**Definition** net\_stats.h:336

[net\_stats\_tc::sent](structnet__stats__tc.md#a8d6a3ebcc49ce8c34a5faae986f648e2)

struct net\_stats\_tc::@074155214116325077102236356156227241054306002026 sent[NET\_TC\_TX\_STATS\_COUNT]

TX statistics for each traffic class.

[net\_stats\_tc::rx\_time](structnet__stats__tc.md#a8ea00824bb0fb18e4d8912343e01c3b7)

struct net\_stats\_rx\_time rx\_time

Helper for calculating average RX time statistics.

**Definition** net\_stats.h:344

[net\_stats\_tcp](structnet__stats__tcp.md)

TCP statistics.

**Definition** net\_stats.h:134

[net\_stats\_tcp::ackerr](structnet__stats__tcp.md#a0d40abc85776f0a9b9510a909b7f6d18)

net\_stats\_t ackerr

Number of received TCP segments with a bad ACK number.

**Definition** net\_stats.h:157

[net\_stats\_tcp::rsterr](structnet__stats__tcp.md#a471fcd5578f79ce77d20547b28503ac1)

net\_stats\_t rsterr

Number of received bad TCP RST (reset) segments.

**Definition** net\_stats.h:160

[net\_stats\_tcp::rexmit](structnet__stats__tcp.md#a4a4ea6e5d87ef58b4271bd708cf39635)

net\_stats\_t rexmit

Number of retransmitted TCP segments.

**Definition** net\_stats.h:166

[net\_stats\_tcp::chkerr](structnet__stats__tcp.md#a5099e174b0eafa322f0630f1f5c73a8b)

net\_stats\_t chkerr

Number of TCP segments with a bad checksum.

**Definition** net\_stats.h:154

[net\_stats\_tcp::seg\_drop](structnet__stats__tcp.md#a5f045704859331918511e9c2281ac155)

net\_stats\_t seg\_drop

Number of dropped TCP segments.

**Definition** net\_stats.h:151

[net\_stats\_tcp::connrst](structnet__stats__tcp.md#a67f55954a4c51f2b957c7d974e78c1c0)

net\_stats\_t connrst

Number of connection attempts for closed ports, triggering a RST.

**Definition** net\_stats.h:174

[net\_stats\_tcp::drop](structnet__stats__tcp.md#aa549f7b6d5828009a09190fd64afa8e3)

net\_stats\_t drop

Number of dropped packets at the TCP layer.

**Definition** net\_stats.h:142

[net\_stats\_tcp::rst](structnet__stats__tcp.md#aa618cf86b962aca0f14eb9178c8ae61a)

net\_stats\_t rst

Number of received TCP RST (reset) segments.

**Definition** net\_stats.h:163

[net\_stats\_tcp::sent](structnet__stats__tcp.md#aa987bebf96000b6b4e92bfafc218759a)

net\_stats\_t sent

Number of sent TCP segments.

**Definition** net\_stats.h:148

[net\_stats\_tcp::resent](structnet__stats__tcp.md#abe567032cb4a267a984aec28c1e3cca4)

net\_stats\_t resent

Amount of retransmitted data.

**Definition** net\_stats.h:139

[net\_stats\_tcp::conndrop](structnet__stats__tcp.md#ac557ac0d8917bc2c2dfed74126f993c8)

net\_stats\_t conndrop

Number of dropped connection attempts because too few connections were available.

**Definition** net\_stats.h:171

[net\_stats\_tcp::recv](structnet__stats__tcp.md#ad25edb2b39a6acc8152c35ad43a5042f)

net\_stats\_t recv

Number of received TCP segments.

**Definition** net\_stats.h:145

[net\_stats\_tcp::bytes](structnet__stats__tcp.md#af80c18bcc253133ce5f0597ac190b349)

struct net\_stats\_bytes bytes

Amount of received and sent TCP application data.

**Definition** net\_stats.h:136

[net\_stats\_tx\_time](structnet__stats__tx__time.md)

Network packet transfer times for calculating average TX time.

**Definition** net\_stats.h:281

[net\_stats\_tx\_time::count](structnet__stats__tx__time.md#a7a652350ed04e53ba02aec294f8444b4)

net\_stats\_t count

Number of network packets transferred.

**Definition** net\_stats.h:286

[net\_stats\_tx\_time::sum](structnet__stats__tx__time.md#af6f7a26c0344a0f93306e105a8917c3e)

uint64\_t sum

Sum of network packet transfer times.

**Definition** net\_stats.h:283

[net\_stats\_udp](structnet__stats__udp.md)

UDP statistics.

**Definition** net\_stats.h:180

[net\_stats\_udp::recv](structnet__stats__udp.md#a0ea91d85fe322661fb909f5e94e55a34)

net\_stats\_t recv

Number of received UDP segments.

**Definition** net\_stats.h:185

[net\_stats\_udp::drop](structnet__stats__udp.md#a2d884bf9106e60d430ffec7c7964a609)

net\_stats\_t drop

Number of dropped UDP segments.

**Definition** net\_stats.h:182

[net\_stats\_udp::chkerr](structnet__stats__udp.md#a4c57d5f68ebda7981400729b9c7fe0f7)

net\_stats\_t chkerr

Number of UDP segments with a bad checksum.

**Definition** net\_stats.h:191

[net\_stats\_udp::sent](structnet__stats__udp.md#ab4e8228c221901d3ded55f3f823bfa1c)

net\_stats\_t sent

Number of sent UDP segments.

**Definition** net\_stats.h:188

[net\_stats\_wifi](structnet__stats__wifi.md)

All Wi-Fi specific statistics.

**Definition** net\_stats.h:705

[net\_stats\_wifi::broadcast](structnet__stats__wifi.md#a03dc04638c4b670bd7f3520d45fc1eda)

struct net\_stats\_pkts broadcast

Total number of broadcast packets received and sent.

**Definition** net\_stats.h:716

[net\_stats\_wifi::multicast](structnet__stats__wifi.md#a7e7f68215101885fd51c70e981da26e7)

struct net\_stats\_pkts multicast

Total number of multicast packets received and sent.

**Definition** net\_stats.h:719

[net\_stats\_wifi::sta\_mgmt](structnet__stats__wifi.md#a8bee22961545674e6ab100b58a04bf91)

struct net\_stats\_sta\_mgmt sta\_mgmt

Total number of beacon errors.

**Definition** net\_stats.h:707

[net\_stats\_wifi::bytes](structnet__stats__wifi.md#aa055b1e8bd8f1e50815c1028b562be07)

struct net\_stats\_bytes bytes

Total number of bytes received and sent.

**Definition** net\_stats.h:710

[net\_stats\_wifi::overrun\_count](structnet__stats__wifi.md#ac498c9e517f2cb2eb01d251e84159e7e)

net\_stats\_t overrun\_count

Total number of dropped packets at received and sent.

**Definition** net\_stats.h:728

[net\_stats\_wifi::pkts](structnet__stats__wifi.md#adbcdb2dd8733f2917c00a0b2d365393b)

struct net\_stats\_pkts pkts

Total number of packets received and sent.

**Definition** net\_stats.h:713

[net\_stats\_wifi::errors](structnet__stats__wifi.md#ae0149e64a94a9f96eb6680f94793c8c4)

struct net\_stats\_pkts errors

Total number of errors in RX and TX.

**Definition** net\_stats.h:722

[net\_stats\_wifi::unicast](structnet__stats__wifi.md#ae80dcd73a3c5ce3ec3282d1ae827b338)

struct net\_stats\_pkts unicast

Total number of unicast packets received and sent.

**Definition** net\_stats.h:725

[net\_stats](structnet__stats.md)

All network statistics in one struct.

**Definition** net\_stats.h:406

[net\_stats::processing\_error](structnet__stats.md#a3a4c90661d6b310b628262228a341fe2)

net\_stats\_t processing\_error

Count of malformed packets or packets we do not have handler for.

**Definition** net\_stats.h:414

[net\_stats::bytes](structnet__stats.md#a7a28233e6d23efdce0143469b9bb6c05)

struct net\_stats\_bytes bytes

This calculates amount of data transferred through all the network interfaces.

**Definition** net\_stats.h:411

[net\_stats::ip\_errors](structnet__stats.md#ac42cb13954d164e92a1ef60919a2a34e)

struct net\_stats\_ip\_errors ip\_errors

IP layer errors.

**Definition** net\_stats.h:417

[summary.h](summary_8h.md)

Prometheus summary APIs.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [net\_stats.h](net__stats_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
