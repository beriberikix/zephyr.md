---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/net__stats_8h_source.html
original_path: doxygen/html/net__stats_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
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

[ 52](structnet__stats__bytes.md#a89368f376c02d25c5a7a5719851a0ac7) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [sent](structnet__stats__bytes.md#a89368f376c02d25c5a7a5719851a0ac7);

[ 54](structnet__stats__bytes.md#a8bc21878924210278c6e0e2861163be4) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [received](structnet__stats__bytes.md#a8bc21878924210278c6e0e2861163be4);

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

[ 323](structnet__stats__tc.md#a30288ef3bb0796cd18c3cf0aedbe875a) struct [net\_stats\_tx\_time](structnet__stats__tx__time.md) [tx\_time](structnet__stats__tc.md#a30288ef3bb0796cd18c3cf0aedbe875a);

324#if defined(CONFIG\_NET\_PKT\_TXTIME\_STATS\_DETAIL)

326 struct [net\_stats\_tx\_time](structnet__stats__tx__time.md)

327 tx\_time\_detail[NET\_PKT\_DETAIL\_STATS\_COUNT];

328#endif

[ 330](structnet__stats__tc.md#a6614b5f5186635415a7d787260c39248) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [pkts](structnet__stats__tc.md#a6614b5f5186635415a7d787260c39248);

[ 332](structnet__stats__tc.md#a1794f71f7fe7b3d20d406be4b28eb032) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [dropped](structnet__stats__tc.md#a1794f71f7fe7b3d20d406be4b28eb032);

[ 334](structnet__stats__tc.md#a192a7ec0d24bce9e62f766e481ee5709) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [bytes](structnet__stats__tc.md#a192a7ec0d24bce9e62f766e481ee5709);

[ 336](structnet__stats__tc.md#a8a5c2e59990407ddbfc7973a1c183bf6) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [priority](structnet__stats__tc.md#a8a5c2e59990407ddbfc7973a1c183bf6);

[ 337](structnet__stats__tc.md#a8d6a3ebcc49ce8c34a5faae986f648e2) } [sent](structnet__stats__tc.md#a8d6a3ebcc49ce8c34a5faae986f648e2)[NET\_TC\_TX\_STATS\_COUNT];

338

340 struct {

[ 342](structnet__stats__tc.md#a8ea00824bb0fb18e4d8912343e01c3b7) struct [net\_stats\_rx\_time](structnet__stats__rx__time.md) [rx\_time](structnet__stats__tc.md#a8ea00824bb0fb18e4d8912343e01c3b7);

343#if defined(CONFIG\_NET\_PKT\_RXTIME\_STATS\_DETAIL)

345 struct [net\_stats\_rx\_time](structnet__stats__rx__time.md)

346 rx\_time\_detail[NET\_PKT\_DETAIL\_STATS\_COUNT];

347#endif

349 [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [pkts](structnet__stats__tc.md#a6614b5f5186635415a7d787260c39248);

351 [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [dropped](structnet__stats__tc.md#a1794f71f7fe7b3d20d406be4b28eb032);

353 [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [bytes](structnet__stats__tc.md#a192a7ec0d24bce9e62f766e481ee5709);

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

374

[ 378](structnet__stats.md)struct [net\_stats](structnet__stats.md) {

[ 380](structnet__stats.md#a3a4c90661d6b310b628262228a341fe2) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [processing\_error](structnet__stats.md#a3a4c90661d6b310b628262228a341fe2);

381

[ 386](structnet__stats.md#a7a28233e6d23efdce0143469b9bb6c05) struct [net\_stats\_bytes](structnet__stats__bytes.md) [bytes](structnet__stats.md#a7a28233e6d23efdce0143469b9bb6c05);

387

[ 389](structnet__stats.md#ac42cb13954d164e92a1ef60919a2a34e) struct [net\_stats\_ip\_errors](structnet__stats__ip__errors.md) [ip\_errors](structnet__stats.md#ac42cb13954d164e92a1ef60919a2a34e);

390

391#if defined(CONFIG\_NET\_STATISTICS\_IPV6)

393 struct [net\_stats\_ip](structnet__stats__ip.md) ipv6;

394#endif

395

396#if defined(CONFIG\_NET\_STATISTICS\_IPV4)

398 struct [net\_stats\_ip](structnet__stats__ip.md) ipv4;

399#endif

400

401#if defined(CONFIG\_NET\_STATISTICS\_ICMP)

403 struct [net\_stats\_icmp](structnet__stats__icmp.md) icmp;

404#endif

405

406#if defined(CONFIG\_NET\_STATISTICS\_TCP)

408 struct [net\_stats\_tcp](structnet__stats__tcp.md) tcp;

409#endif

410

411#if defined(CONFIG\_NET\_STATISTICS\_UDP)

413 struct [net\_stats\_udp](structnet__stats__udp.md) udp;

414#endif

415

416#if defined(CONFIG\_NET\_STATISTICS\_IPV6\_ND)

418 struct [net\_stats\_ipv6\_nd](structnet__stats__ipv6__nd.md) ipv6\_nd;

419#endif

420

421#if defined(CONFIG\_NET\_STATISTICS\_IPV6\_PMTU)

423 struct [net\_stats\_ipv6\_pmtu](structnet__stats__ipv6__pmtu.md) ipv6\_pmtu;

424#endif

425

426#if defined(CONFIG\_NET\_STATISTICS\_IPV4\_PMTU)

428 struct [net\_stats\_ipv4\_pmtu](structnet__stats__ipv4__pmtu.md) ipv4\_pmtu;

429#endif

430

431#if defined(CONFIG\_NET\_STATISTICS\_MLD)

433 struct [net\_stats\_ipv6\_mld](structnet__stats__ipv6__mld.md) ipv6\_mld;

434#endif

435

436#if defined(CONFIG\_NET\_STATISTICS\_IGMP)

438 struct [net\_stats\_ipv4\_igmp](structnet__stats__ipv4__igmp.md) ipv4\_igmp;

439#endif

440

441#if defined(CONFIG\_NET\_STATISTICS\_DNS)

443 struct [net\_stats\_dns](structnet__stats__dns.md) dns;

444#endif

445

446#if NET\_TC\_COUNT > 1

448 struct [net\_stats\_tc](structnet__stats__tc.md) tc;

449#endif

450

451#if defined(CONFIG\_NET\_PKT\_TXTIME\_STATS)

453 struct [net\_stats\_tx\_time](structnet__stats__tx__time.md) tx\_time;

454#endif

455

456#if defined(CONFIG\_NET\_PKT\_RXTIME\_STATS)

458 struct [net\_stats\_rx\_time](structnet__stats__rx__time.md) rx\_time;

459#endif

460

461#if defined(CONFIG\_NET\_PKT\_TXTIME\_STATS\_DETAIL)

463 struct [net\_stats\_tx\_time](structnet__stats__tx__time.md) tx\_time\_detail[NET\_PKT\_DETAIL\_STATS\_COUNT];

464#endif

465#if defined(CONFIG\_NET\_PKT\_RXTIME\_STATS\_DETAIL)

467 struct [net\_stats\_rx\_time](structnet__stats__rx__time.md) rx\_time\_detail[NET\_PKT\_DETAIL\_STATS\_COUNT];

468#endif

469

470#if defined(CONFIG\_NET\_STATISTICS\_POWER\_MANAGEMENT)

472 struct [net\_stats\_pm](structnet__stats__pm.md) pm;

473#endif

474};

475

[ 479](structnet__stats__eth__errors.md)struct [net\_stats\_eth\_errors](structnet__stats__eth__errors.md) {

[ 481](structnet__stats__eth__errors.md#aca0e2e4807fa70279dee8ddaad2d7ef7) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [rx\_length\_errors](structnet__stats__eth__errors.md#aca0e2e4807fa70279dee8ddaad2d7ef7);

482

[ 484](structnet__stats__eth__errors.md#a9afee89f5bb01907e7cd515e2a0ff1b5) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [rx\_over\_errors](structnet__stats__eth__errors.md#a9afee89f5bb01907e7cd515e2a0ff1b5);

485

[ 487](structnet__stats__eth__errors.md#a4dab70cf219269bb393ce14faf0ed77e) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [rx\_crc\_errors](structnet__stats__eth__errors.md#a4dab70cf219269bb393ce14faf0ed77e);

488

[ 490](structnet__stats__eth__errors.md#a8dfcc5cd1b4decec5783d01ba7033b05) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [rx\_frame\_errors](structnet__stats__eth__errors.md#a8dfcc5cd1b4decec5783d01ba7033b05);

491

[ 493](structnet__stats__eth__errors.md#a82622736d226b4d3b999f1f22ccf8529) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [rx\_no\_buffer\_count](structnet__stats__eth__errors.md#a82622736d226b4d3b999f1f22ccf8529);

494

[ 496](structnet__stats__eth__errors.md#a2d2b2c4e3764ebec841f1ecbe7058d99) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [rx\_missed\_errors](structnet__stats__eth__errors.md#a2d2b2c4e3764ebec841f1ecbe7058d99);

497

[ 499](structnet__stats__eth__errors.md#a0e83e270a35222ed3e927800be4159e7) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [rx\_long\_length\_errors](structnet__stats__eth__errors.md#a0e83e270a35222ed3e927800be4159e7);

500

[ 502](structnet__stats__eth__errors.md#a5e3d39d8417bb180cbfcb8c901006e81) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [rx\_short\_length\_errors](structnet__stats__eth__errors.md#a5e3d39d8417bb180cbfcb8c901006e81);

503

[ 505](structnet__stats__eth__errors.md#a7618f10af3443c49a6e256bb41e77781) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [rx\_align\_errors](structnet__stats__eth__errors.md#a7618f10af3443c49a6e256bb41e77781);

506

[ 508](structnet__stats__eth__errors.md#a7bcfbb13836f162ceeb5f021304b5c76) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [rx\_dma\_failed](structnet__stats__eth__errors.md#a7bcfbb13836f162ceeb5f021304b5c76);

509

[ 511](structnet__stats__eth__errors.md#adbcae9c10c081f1cdf304bcdce740aa4) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [rx\_buf\_alloc\_failed](structnet__stats__eth__errors.md#adbcae9c10c081f1cdf304bcdce740aa4);

512

[ 514](structnet__stats__eth__errors.md#afec6a7e24c6f3cc74dd9f739f27b3e48) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [tx\_aborted\_errors](structnet__stats__eth__errors.md#afec6a7e24c6f3cc74dd9f739f27b3e48);

515

[ 517](structnet__stats__eth__errors.md#a0043d1a1481040a6d7439bd23423ec12) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [tx\_carrier\_errors](structnet__stats__eth__errors.md#a0043d1a1481040a6d7439bd23423ec12);

518

[ 520](structnet__stats__eth__errors.md#a84630da9b82557f56dc35cd59ca2f7ae) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [tx\_fifo\_errors](structnet__stats__eth__errors.md#a84630da9b82557f56dc35cd59ca2f7ae);

521

[ 523](structnet__stats__eth__errors.md#ae2a13733c1a5f0cc3e00efca0c3f429d) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [tx\_heartbeat\_errors](structnet__stats__eth__errors.md#ae2a13733c1a5f0cc3e00efca0c3f429d);

524

[ 526](structnet__stats__eth__errors.md#a17624a12d6473bdd78698076fed0d122) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [tx\_window\_errors](structnet__stats__eth__errors.md#a17624a12d6473bdd78698076fed0d122);

527

[ 529](structnet__stats__eth__errors.md#abfbf6478b7afdd5935d7c6948c9ef426) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [tx\_dma\_failed](structnet__stats__eth__errors.md#abfbf6478b7afdd5935d7c6948c9ef426);

530

[ 532](structnet__stats__eth__errors.md#a07d0a435f2129556520c732571d28edf) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [uncorr\_ecc\_errors](structnet__stats__eth__errors.md#a07d0a435f2129556520c732571d28edf);

533

[ 535](structnet__stats__eth__errors.md#a257113639f0e0e3085febb7a147f498f) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [corr\_ecc\_errors](structnet__stats__eth__errors.md#a257113639f0e0e3085febb7a147f498f);

536};

537

[ 541](structnet__stats__eth__flow.md)struct [net\_stats\_eth\_flow](structnet__stats__eth__flow.md) {

[ 543](structnet__stats__eth__flow.md#a08e5da4ff78fe3893b9c9a628cefe4f2) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [rx\_flow\_control\_xon](structnet__stats__eth__flow.md#a08e5da4ff78fe3893b9c9a628cefe4f2);

544

[ 546](structnet__stats__eth__flow.md#a8f9b93537b3c11be70f276aaa72cb637) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [rx\_flow\_control\_xoff](structnet__stats__eth__flow.md#a8f9b93537b3c11be70f276aaa72cb637);

547

[ 549](structnet__stats__eth__flow.md#a31412e8bf9d38ba630ea856e958a48d7) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [tx\_flow\_control\_xon](structnet__stats__eth__flow.md#a31412e8bf9d38ba630ea856e958a48d7);

550

[ 552](structnet__stats__eth__flow.md#a969d81f9db20312d2d2aa7f70f93bdd5) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [tx\_flow\_control\_xoff](structnet__stats__eth__flow.md#a969d81f9db20312d2d2aa7f70f93bdd5);

553};

554

[ 558](structnet__stats__eth__csum.md)struct [net\_stats\_eth\_csum](structnet__stats__eth__csum.md) {

[ 560](structnet__stats__eth__csum.md#a1f1ba5c01c6232cd739d069ddb871b17) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [rx\_csum\_offload\_good](structnet__stats__eth__csum.md#a1f1ba5c01c6232cd739d069ddb871b17);

561

[ 563](structnet__stats__eth__csum.md#ac4fc04d66193070d4f52a4c07f29ccce) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [rx\_csum\_offload\_errors](structnet__stats__eth__csum.md#ac4fc04d66193070d4f52a4c07f29ccce);

564};

565

[ 569](structnet__stats__eth__hw__timestamp.md)struct [net\_stats\_eth\_hw\_timestamp](structnet__stats__eth__hw__timestamp.md) {

[ 571](structnet__stats__eth__hw__timestamp.md#acd3d5f72d7df568110d96093e0c9534d) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [rx\_hwtstamp\_cleared](structnet__stats__eth__hw__timestamp.md#acd3d5f72d7df568110d96093e0c9534d);

572

[ 574](structnet__stats__eth__hw__timestamp.md#a41f605499dbf88a879522fdfa4633d9e) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [tx\_hwtstamp\_timeouts](structnet__stats__eth__hw__timestamp.md#a41f605499dbf88a879522fdfa4633d9e);

575

[ 577](structnet__stats__eth__hw__timestamp.md#ae1f983faf4a999308c464e4af5a5284b) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [tx\_hwtstamp\_skipped](structnet__stats__eth__hw__timestamp.md#ae1f983faf4a999308c464e4af5a5284b);

578};

579

580#ifdef CONFIG\_NET\_STATISTICS\_ETHERNET\_VENDOR

584struct net\_stats\_eth\_vendor {

585 const char \* const key;

586 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) value;

587};

588#endif

589

[ 593](structnet__stats__eth.md)struct [net\_stats\_eth](structnet__stats__eth.md) {

[ 595](structnet__stats__eth.md#a8c5cf1ead8ba214425a16fed1c2ad0fb) struct [net\_stats\_bytes](structnet__stats__bytes.md) [bytes](structnet__stats__eth.md#a8c5cf1ead8ba214425a16fed1c2ad0fb);

596

[ 598](structnet__stats__eth.md#a97bd6026b16890743f344751a21107f1) struct [net\_stats\_pkts](structnet__stats__pkts.md) [pkts](structnet__stats__eth.md#a97bd6026b16890743f344751a21107f1);

599

[ 601](structnet__stats__eth.md#a054beb909134b0e0f22f5df599549128) struct [net\_stats\_pkts](structnet__stats__pkts.md) [broadcast](structnet__stats__eth.md#a054beb909134b0e0f22f5df599549128);

602

[ 604](structnet__stats__eth.md#a4f6a2903330518a132e7e547820e0bf2) struct [net\_stats\_pkts](structnet__stats__pkts.md) [multicast](structnet__stats__eth.md#a4f6a2903330518a132e7e547820e0bf2);

605

[ 607](structnet__stats__eth.md#a9c869740f416fbe0b54d7fefacb1fe29) struct [net\_stats\_pkts](structnet__stats__pkts.md) [errors](structnet__stats__eth.md#a9c869740f416fbe0b54d7fefacb1fe29);

608

[ 610](structnet__stats__eth.md#a922feddb17fc020371f1bcc52c709415) struct [net\_stats\_eth\_errors](structnet__stats__eth__errors.md) [error\_details](structnet__stats__eth.md#a922feddb17fc020371f1bcc52c709415);

611

[ 613](structnet__stats__eth.md#a643010ac6360c8c0c08016725ba12222) struct [net\_stats\_eth\_flow](structnet__stats__eth__flow.md) [flow\_control](structnet__stats__eth.md#a643010ac6360c8c0c08016725ba12222);

614

[ 616](structnet__stats__eth.md#a2169ae06bace1a93663bccf88c8d7a29) struct [net\_stats\_eth\_csum](structnet__stats__eth__csum.md) [csum](structnet__stats__eth.md#a2169ae06bace1a93663bccf88c8d7a29);

617

[ 619](structnet__stats__eth.md#a44667efff73c17c089ed22d5b0da5ad3) struct [net\_stats\_eth\_hw\_timestamp](structnet__stats__eth__hw__timestamp.md) [hw\_timestamp](structnet__stats__eth.md#a44667efff73c17c089ed22d5b0da5ad3);

620

[ 622](structnet__stats__eth.md#a822d4205791f59999c842610522f6fc5) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [collisions](structnet__stats__eth.md#a822d4205791f59999c842610522f6fc5);

623

[ 625](structnet__stats__eth.md#a257c349cf3d32d38796e3899e702454a) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [tx\_dropped](structnet__stats__eth.md#a257c349cf3d32d38796e3899e702454a);

626

[ 628](structnet__stats__eth.md#ab351258ae82abd09759d37774559d8bc) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [tx\_timeout\_count](structnet__stats__eth.md#ab351258ae82abd09759d37774559d8bc);

629

[ 631](structnet__stats__eth.md#a6699012226e25e8bad39076fed6dbfb5) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [tx\_restart\_queue](structnet__stats__eth.md#a6699012226e25e8bad39076fed6dbfb5);

632

[ 634](structnet__stats__eth.md#afaacee7cc1d0a35ae2344175421c40dd) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [unknown\_protocol](structnet__stats__eth.md#afaacee7cc1d0a35ae2344175421c40dd);

635

636#ifdef CONFIG\_NET\_STATISTICS\_ETHERNET\_VENDOR

638 struct net\_stats\_eth\_vendor \*vendor;

639#endif

640};

641

[ 645](structnet__stats__ppp.md)struct [net\_stats\_ppp](structnet__stats__ppp.md) {

[ 647](structnet__stats__ppp.md#ab2b48da7f19d4b83e3f41b41979b7ed8) struct [net\_stats\_bytes](structnet__stats__bytes.md) [bytes](structnet__stats__ppp.md#ab2b48da7f19d4b83e3f41b41979b7ed8);

648

[ 650](structnet__stats__ppp.md#a71fc81f3c5f3e65a476b3391f086d340) struct [net\_stats\_pkts](structnet__stats__pkts.md) [pkts](structnet__stats__ppp.md#a71fc81f3c5f3e65a476b3391f086d340);

651

[ 653](structnet__stats__ppp.md#ae2e0a47a539e9d7bc97f9c63f889b276) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [drop](structnet__stats__ppp.md#ae2e0a47a539e9d7bc97f9c63f889b276);

654

[ 656](structnet__stats__ppp.md#a1332b31980f82236aeb0c3f9444e2ac6) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [chkerr](structnet__stats__ppp.md#a1332b31980f82236aeb0c3f9444e2ac6);

657};

658

[ 662](structnet__stats__sta__mgmt.md)struct [net\_stats\_sta\_mgmt](structnet__stats__sta__mgmt.md) {

[ 664](structnet__stats__sta__mgmt.md#ac6e68fded8e19b20259442436923f815) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [beacons\_rx](structnet__stats__sta__mgmt.md#ac6e68fded8e19b20259442436923f815);

665

[ 667](structnet__stats__sta__mgmt.md#a29ae0079b4c780e0de2656a85ec15fe9) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [beacons\_miss](structnet__stats__sta__mgmt.md#a29ae0079b4c780e0de2656a85ec15fe9);

668};

669

[ 673](structnet__stats__wifi.md)struct [net\_stats\_wifi](structnet__stats__wifi.md) {

[ 675](structnet__stats__wifi.md#a8bee22961545674e6ab100b58a04bf91) struct [net\_stats\_sta\_mgmt](structnet__stats__sta__mgmt.md) [sta\_mgmt](structnet__stats__wifi.md#a8bee22961545674e6ab100b58a04bf91);

676

[ 678](structnet__stats__wifi.md#aa055b1e8bd8f1e50815c1028b562be07) struct [net\_stats\_bytes](structnet__stats__bytes.md) [bytes](structnet__stats__wifi.md#aa055b1e8bd8f1e50815c1028b562be07);

679

[ 681](structnet__stats__wifi.md#adbcdb2dd8733f2917c00a0b2d365393b) struct [net\_stats\_pkts](structnet__stats__pkts.md) [pkts](structnet__stats__wifi.md#adbcdb2dd8733f2917c00a0b2d365393b);

682

[ 684](structnet__stats__wifi.md#a03dc04638c4b670bd7f3520d45fc1eda) struct [net\_stats\_pkts](structnet__stats__pkts.md) [broadcast](structnet__stats__wifi.md#a03dc04638c4b670bd7f3520d45fc1eda);

685

[ 687](structnet__stats__wifi.md#a7e7f68215101885fd51c70e981da26e7) struct [net\_stats\_pkts](structnet__stats__pkts.md) [multicast](structnet__stats__wifi.md#a7e7f68215101885fd51c70e981da26e7);

688

[ 690](structnet__stats__wifi.md#ae0149e64a94a9f96eb6680f94793c8c4) struct [net\_stats\_pkts](structnet__stats__pkts.md) [errors](structnet__stats__wifi.md#ae0149e64a94a9f96eb6680f94793c8c4);

691

[ 693](structnet__stats__wifi.md#ae80dcd73a3c5ce3ec3282d1ae827b338) struct [net\_stats\_pkts](structnet__stats__pkts.md) [unicast](structnet__stats__wifi.md#ae80dcd73a3c5ce3ec3282d1ae827b338);

694

[ 696](structnet__stats__wifi.md#ac498c9e517f2cb2eb01d251e84159e7e) [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) [overrun\_count](structnet__stats__wifi.md#ac498c9e517f2cb2eb01d251e84159e7e);

697};

698

699#if defined(CONFIG\_NET\_STATISTICS\_USER\_API)

700/\* Management part definitions \*/

701

703

704#define \_NET\_STATS\_LAYER NET\_MGMT\_LAYER\_L3

705#define \_NET\_STATS\_CODE 0x101

706#define \_NET\_STATS\_BASE (NET\_MGMT\_LAYER(\_NET\_STATS\_LAYER) | \

707 NET\_MGMT\_LAYER\_CODE(\_NET\_STATS\_CODE))

708

709enum net\_request\_stats\_cmd {

710 NET\_REQUEST\_STATS\_CMD\_GET\_ALL = 1,

711 NET\_REQUEST\_STATS\_CMD\_GET\_PROCESSING\_ERROR,

712 NET\_REQUEST\_STATS\_CMD\_GET\_BYTES,

713 NET\_REQUEST\_STATS\_CMD\_GET\_IP\_ERRORS,

714 NET\_REQUEST\_STATS\_CMD\_GET\_IPV4,

715 NET\_REQUEST\_STATS\_CMD\_GET\_IPV6,

716 NET\_REQUEST\_STATS\_CMD\_GET\_IPV6\_ND,

717 NET\_REQUEST\_STATS\_CMD\_GET\_IPV6\_PMTU,

718 NET\_REQUEST\_STATS\_CMD\_GET\_IPV4\_PMTU,

719 NET\_REQUEST\_STATS\_CMD\_GET\_ICMP,

720 NET\_REQUEST\_STATS\_CMD\_GET\_UDP,

721 NET\_REQUEST\_STATS\_CMD\_GET\_TCP,

722 NET\_REQUEST\_STATS\_CMD\_GET\_ETHERNET,

723 NET\_REQUEST\_STATS\_CMD\_GET\_PPP,

724 NET\_REQUEST\_STATS\_CMD\_GET\_PM,

725 NET\_REQUEST\_STATS\_CMD\_GET\_WIFI,

726 NET\_REQUEST\_STATS\_CMD\_RESET\_WIFI,

727};

728

730

732#define NET\_REQUEST\_STATS\_GET\_ALL \

733 (\_NET\_STATS\_BASE | NET\_REQUEST\_STATS\_CMD\_GET\_ALL)

734

736#define NET\_REQUEST\_STATS\_GET\_PROCESSING\_ERROR \

737 (\_NET\_STATS\_BASE | NET\_REQUEST\_STATS\_CMD\_GET\_PROCESSING\_ERROR)

738

740#define NET\_REQUEST\_STATS\_GET\_BYTES \

741 (\_NET\_STATS\_BASE | NET\_REQUEST\_STATS\_CMD\_GET\_BYTES)

742

744#define NET\_REQUEST\_STATS\_GET\_IP\_ERRORS \

745 (\_NET\_STATS\_BASE | NET\_REQUEST\_STATS\_CMD\_GET\_IP\_ERRORS)

746

748

749[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_STATS\_GET\_ALL);

750[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_STATS\_GET\_PROCESSING\_ERROR);

751[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_STATS\_GET\_BYTES);

752[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_STATS\_GET\_IP\_ERRORS);

753

755

756#if defined(CONFIG\_NET\_STATISTICS\_IPV4)

758#define NET\_REQUEST\_STATS\_GET\_IPV4 \

759 (\_NET\_STATS\_BASE | NET\_REQUEST\_STATS\_CMD\_GET\_IPV4)

760

762[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_STATS\_GET\_IPV4);

764#endif /\* CONFIG\_NET\_STATISTICS\_IPV4 \*/

765

766#if defined(CONFIG\_NET\_STATISTICS\_IPV6)

768#define NET\_REQUEST\_STATS\_GET\_IPV6 \

769 (\_NET\_STATS\_BASE | NET\_REQUEST\_STATS\_CMD\_GET\_IPV6)

770

772[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_STATS\_GET\_IPV6);

774#endif /\* CONFIG\_NET\_STATISTICS\_IPV6 \*/

775

776#if defined(CONFIG\_NET\_STATISTICS\_IPV6\_ND)

778#define NET\_REQUEST\_STATS\_GET\_IPV6\_ND \

779 (\_NET\_STATS\_BASE | NET\_REQUEST\_STATS\_CMD\_GET\_IPV6\_ND)

780

782[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_STATS\_GET\_IPV6\_ND);

784#endif /\* CONFIG\_NET\_STATISTICS\_IPV6\_ND \*/

785

786#if defined(CONFIG\_NET\_STATISTICS\_IPV6\_PMTU)

788#define NET\_REQUEST\_STATS\_GET\_IPV6\_PMTU \

789 (\_NET\_STATS\_BASE | NET\_REQUEST\_STATS\_CMD\_GET\_IPV6\_PMTU)

790

792[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_STATS\_GET\_IPV6\_PMTU);

794#endif /\* CONFIG\_NET\_STATISTICS\_IPV6\_PMTU \*/

795

796#if defined(CONFIG\_NET\_STATISTICS\_IPV4\_PMTU)

798#define NET\_REQUEST\_STATS\_GET\_IPV4\_PMTU \

799 (\_NET\_STATS\_BASE | NET\_REQUEST\_STATS\_CMD\_GET\_IPV4\_PMTU)

800

802[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_STATS\_GET\_IPV4\_PMTU);

804#endif /\* CONFIG\_NET\_STATISTICS\_IPV4\_PMTU \*/

805

806#if defined(CONFIG\_NET\_STATISTICS\_ICMP)

808#define NET\_REQUEST\_STATS\_GET\_ICMP \

809 (\_NET\_STATS\_BASE | NET\_REQUEST\_STATS\_CMD\_GET\_ICMP)

810

812[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_STATS\_GET\_ICMP);

814#endif /\* CONFIG\_NET\_STATISTICS\_ICMP \*/

815

816#if defined(CONFIG\_NET\_STATISTICS\_UDP)

818#define NET\_REQUEST\_STATS\_GET\_UDP \

819 (\_NET\_STATS\_BASE | NET\_REQUEST\_STATS\_CMD\_GET\_UDP)

820

822[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_STATS\_GET\_UDP);

824#endif /\* CONFIG\_NET\_STATISTICS\_UDP \*/

825

826#if defined(CONFIG\_NET\_STATISTICS\_TCP)

828#define NET\_REQUEST\_STATS\_GET\_TCP \

829 (\_NET\_STATS\_BASE | NET\_REQUEST\_STATS\_CMD\_GET\_TCP)

830

832[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_STATS\_GET\_TCP);

834#endif /\* CONFIG\_NET\_STATISTICS\_TCP \*/

835

836#if defined(CONFIG\_NET\_STATISTICS\_ETHERNET)

838#define NET\_REQUEST\_STATS\_GET\_ETHERNET \

839 (\_NET\_STATS\_BASE | NET\_REQUEST\_STATS\_CMD\_GET\_ETHERNET)

840

842[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_STATS\_GET\_ETHERNET);

844#endif /\* CONFIG\_NET\_STATISTICS\_ETHERNET \*/

845

846#if defined(CONFIG\_NET\_STATISTICS\_PPP)

848#define NET\_REQUEST\_STATS\_GET\_PPP \

849 (\_NET\_STATS\_BASE | NET\_REQUEST\_STATS\_CMD\_GET\_PPP)

850

852[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_STATS\_GET\_PPP);

854#endif /\* CONFIG\_NET\_STATISTICS\_PPP \*/

855

856#endif /\* CONFIG\_NET\_STATISTICS\_USER\_API \*/

857

858#if defined(CONFIG\_NET\_STATISTICS\_POWER\_MANAGEMENT)

860#define NET\_REQUEST\_STATS\_GET\_PM \

861 (\_NET\_STATS\_BASE | NET\_REQUEST\_STATS\_CMD\_GET\_PM)

862

864[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_STATS\_GET\_PM);

866#endif /\* CONFIG\_NET\_STATISTICS\_POWER\_MANAGEMENT \*/

867

868#if defined(CONFIG\_NET\_STATISTICS\_WIFI)

870#define NET\_REQUEST\_STATS\_GET\_WIFI \

871 (\_NET\_STATS\_BASE | NET\_REQUEST\_STATS\_CMD\_GET\_WIFI)

872

874[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_STATS\_GET\_WIFI);

876

878#define NET\_REQUEST\_STATS\_RESET\_WIFI \

879 (\_NET\_STATS\_BASE | NET\_REQUEST\_STATS\_CMD\_RESET\_WIFI)

880

882[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_STATS\_RESET\_WIFI);

884#endif /\* CONFIG\_NET\_STATISTICS\_WIFI \*/

885

[ 886](group__net__stats.md#ga2a1dcb35c366878ef5f675d6bc649223)#define NET\_STATS\_GET\_METRIC\_NAME(\_name) \_name

[ 887](group__net__stats.md#gab58d7d437d4fa9836a826ee59e2d081d)#define NET\_STATS\_GET\_COLLECTOR\_NAME(dev\_id, sfx) net\_stats\_##dev\_id##\_##sfx##\_collector

[ 888](group__net__stats.md#gab66b3c8d32d2f02add08c332460d5cd6)#define NET\_STATS\_GET\_VAR(dev\_id, sfx, var) zephyr\_net\_##var

[ 889](group__net__stats.md#gabb15df6c3c85b85756ef5d2d51d0afb2)#define NET\_STATS\_GET\_INSTANCE(dev\_id, sfx, \_not\_used) STRINGIFY(\_##dev\_id##\_##sfx)

890

891/\* The label value is set to be the network interface name. Note that we skip

892 \* the first character (\_) when setting the label value. This can be changed

893 \* if there is a way to token paste the instance name without the prefix character.

894 \* Note also that the below macros have some parameters that are not used atm.

895 \*/

[ 896](group__net__stats.md#gafc6b5e19cd9407c28cf151820b76a287)#define NET\_STATS\_PROMETHEUS\_COUNTER\_DEFINE(\_desc, \_labelval, \_not\_used, \

897 \_collector, \_name, \_stat\_var\_ptr) \

898 static PROMETHEUS\_COUNTER\_DEFINE( \

899 NET\_STATS\_GET\_METRIC\_NAME(\_name), \

900 \_desc, ({ .key = "nic", .value = &\_labelval[1] }), \

901 &(\_collector), \_stat\_var\_ptr)

902

[ 903](group__net__stats.md#ga162fa8a0ea4939e5768a0cc64210dd6a)#define NET\_STATS\_PROMETHEUS\_GAUGE\_DEFINE(\_desc, \_labelval, \_not\_used, \

904 \_collector, \_name, \_stat\_var\_ptr) \

905 static PROMETHEUS\_GAUGE\_DEFINE( \

906 NET\_STATS\_GET\_METRIC\_NAME(\_name), \

907 \_desc, ({ .key = "nic", .value = &\_labelval[1] }), \

908 &(\_collector), \_stat\_var\_ptr)

909

[ 910](group__net__stats.md#gab02b7f2c5c424723aed7a6aedd1181f9)#define NET\_STATS\_PROMETHEUS\_SUMMARY\_DEFINE(\_desc, \_labelval, \_not\_used, \

911 \_collector, \_name, \_stat\_var\_ptr) \

912 static PROMETHEUS\_SUMMARY\_DEFINE( \

913 NET\_STATS\_GET\_METRIC\_NAME(\_name), \

914 \_desc, ({ .key = "nic", .value = &\_labelval[1] }), \

915 &(\_collector), \_stat\_var\_ptr)

916

[ 917](group__net__stats.md#gae82639c2bed1c646cda66b49ae2f6de9)#define NET\_STATS\_PROMETHEUS\_HISTOGRAM\_DEFINE(\_desc, \_labelval, \_not\_used, \

918 \_collector, \_name, \_stat\_var\_ptr) \

919 static PROMETHEUS\_HISTOGRAM\_DEFINE( \

920 NET\_STATS\_GET\_METRIC\_NAME(\_name), \

921 \_desc, ({ .key = "nic", .value = &\_labelval[1] }), \

922 &(\_collector), \_stat\_var\_ptr)

923

924/\* IPv6 layer statistics \*/

925#if defined(CONFIG\_NET\_STATISTICS\_IPV6)

926#define NET\_STATS\_PROMETHEUS\_IPV6(iface, dev\_id, sfx) \

927 NET\_STATS\_PROMETHEUS\_COUNTER\_DEFINE( \

928 "IPv6 packets sent", \

929 NET\_STATS\_GET\_INSTANCE(dev\_id, sfx, ipv6\_sent), \

930 "packet\_count", \

931 NET\_STATS\_GET\_COLLECTOR\_NAME(dev\_id, sfx), \

932 NET\_STATS\_GET\_VAR(dev\_id, sfx, ipv6\_sent), \

933 &(iface)->stats.ipv6.sent); \

934 NET\_STATS\_PROMETHEUS\_COUNTER\_DEFINE( \

935 "IPv6 packets received", \

936 NET\_STATS\_GET\_INSTANCE(dev\_id, sfx, ipv6\_recv), \

937 "packet\_count", \

938 NET\_STATS\_GET\_COLLECTOR\_NAME(dev\_id, sfx), \

939 NET\_STATS\_GET\_VAR(dev\_id, sfx, ipv6\_recv), \

940 &(iface)->stats.ipv6.recv); \

941 NET\_STATS\_PROMETHEUS\_COUNTER\_DEFINE( \

942 "IPv6 packets dropped", \

943 NET\_STATS\_GET\_INSTANCE(dev\_id, sfx, ipv6\_drop), \

944 "packet\_count", \

945 NET\_STATS\_GET\_COLLECTOR\_NAME(dev\_id, sfx), \

946 NET\_STATS\_GET\_VAR(dev\_id, sfx, ipv6\_drop), \

947 &(iface)->stats.ipv6.drop); \

948 NET\_STATS\_PROMETHEUS\_COUNTER\_DEFINE( \

949 "IPv6 packets forwarded", \

950 NET\_STATS\_GET\_INSTANCE(dev\_id, sfx, ipv6\_forward), \

951 "packet\_count", \

952 NET\_STATS\_GET\_COLLECTOR\_NAME(dev\_id, sfx), \

953 NET\_STATS\_GET\_VAR(dev\_id, sfx, ipv6\_forwarded), \

954 &(iface)->stats.ipv6.forwarded)

955#else

[ 956](group__net__stats.md#gaef8debd9597dae9e8ec2ef91d6e645cc)#define NET\_STATS\_PROMETHEUS\_IPV6(iface, dev\_id, sfx)

957#endif

958

959/\* IPv4 layer statistics \*/

960#if defined(CONFIG\_NET\_STATISTICS\_IPV4)

961#define NET\_STATS\_PROMETHEUS\_IPV4(iface, dev\_id, sfx) \

962 NET\_STATS\_PROMETHEUS\_COUNTER\_DEFINE( \

963 "IPv4 packets sent", \

964 NET\_STATS\_GET\_INSTANCE(dev\_id, sfx, ipv4\_sent), \

965 "packet\_count", \

966 NET\_STATS\_GET\_COLLECTOR\_NAME(dev\_id, sfx), \

967 NET\_STATS\_GET\_VAR(dev\_id, sfx, ipv4\_sent), \

968 &(iface)->stats.ipv4.sent); \

969 NET\_STATS\_PROMETHEUS\_COUNTER\_DEFINE( \

970 "IPv4 packets received", \

971 NET\_STATS\_GET\_INSTANCE(dev\_id, sfx, ipv4\_recv), \

972 "packet\_count", \

973 NET\_STATS\_GET\_COLLECTOR\_NAME(dev\_id, sfx), \

974 NET\_STATS\_GET\_VAR(dev\_id, sfx, ipv4\_recv), \

975 &(iface)->stats.ipv4.recv); \

976 NET\_STATS\_PROMETHEUS\_COUNTER\_DEFINE( \

977 "IPv4 packets dropped", \

978 NET\_STATS\_GET\_INSTANCE(dev\_id, sfx, ipv4\_drop), \

979 "packet\_count", \

980 NET\_STATS\_GET\_COLLECTOR\_NAME(dev\_id, sfx), \

981 NET\_STATS\_GET\_VAR(dev\_id, sfx, ipv4\_drop), \

982 &(iface)->stats.ipv4.drop); \

983 NET\_STATS\_PROMETHEUS\_COUNTER\_DEFINE( \

984 "IPv4 packets forwarded", \

985 NET\_STATS\_GET\_INSTANCE(dev\_id, sfx, ipv4\_forwarded), \

986 "packet\_count", \

987 NET\_STATS\_GET\_COLLECTOR\_NAME(dev\_id, sfx), \

988 NET\_STATS\_GET\_VAR(dev\_id, sfx, ipv4\_forwarded), \

989 &(iface)->stats.ipv4.forwarded)

990#else

[ 991](group__net__stats.md#gafa2e6de020b887512a3cebe75253fb18)#define NET\_STATS\_PROMETHEUS\_IPV4(iface, dev\_id, sfx)

992#endif

993

994/\* ICMP layer statistics \*/

995#if defined(CONFIG\_NET\_STATISTICS\_ICMP)

996#define NET\_STATS\_PROMETHEUS\_ICMP(iface, dev\_id, sfx) \

997 NET\_STATS\_PROMETHEUS\_COUNTER\_DEFINE( \

998 "ICMP packets sent", \

999 NET\_STATS\_GET\_INSTANCE(dev\_id, sfx, icmp\_sent), \

1000 "packet\_count", \

1001 NET\_STATS\_GET\_COLLECTOR\_NAME(dev\_id, sfx), \

1002 NET\_STATS\_GET\_VAR(dev\_id, sfx, icmp\_sent), \

1003 &(iface)->stats.icmp.sent); \

1004 NET\_STATS\_PROMETHEUS\_COUNTER\_DEFINE( \

1005 "ICMP packets received", \

1006 NET\_STATS\_GET\_INSTANCE(dev\_id, sfx, icmp\_recv), \

1007 "packet\_count", \

1008 NET\_STATS\_GET\_COLLECTOR\_NAME(dev\_id, sfx), \

1009 NET\_STATS\_GET\_VAR(dev\_id, sfx, icmp\_recv), \

1010 &(iface)->stats.icmp.recv); \

1011 NET\_STATS\_PROMETHEUS\_COUNTER\_DEFINE( \

1012 "ICMP packets dropped", \

1013 NET\_STATS\_GET\_INSTANCE(dev\_id, sfx, icmp\_drop), \

1014 "packet\_count", \

1015 NET\_STATS\_GET\_COLLECTOR\_NAME(dev\_id, sfx), \

1016 NET\_STATS\_GET\_VAR(dev\_id, sfx, icmp\_drop), \

1017 &(iface)->stats.icmp.drop); \

1018 NET\_STATS\_PROMETHEUS\_COUNTER\_DEFINE( \

1019 "ICMP packets checksum error", \

1020 NET\_STATS\_GET\_INSTANCE(dev\_id, sfx, icmp\_chkerr), \

1021 "packet\_count", \

1022 NET\_STATS\_GET\_COLLECTOR\_NAME(dev\_id, sfx), \

1023 NET\_STATS\_GET\_VAR(dev\_id, sfx, icmp\_chkerr), \

1024 &(iface)->stats.icmp.chkerr); \

1025 NET\_STATS\_PROMETHEUS\_COUNTER\_DEFINE( \

1026 "ICMP packets type error", \

1027 NET\_STATS\_GET\_INSTANCE(dev\_id, sfx, icmp\_typeerr), \

1028 "packet\_count", \

1029 NET\_STATS\_GET\_COLLECTOR\_NAME(dev\_id, sfx), \

1030 NET\_STATS\_GET\_VAR(dev\_id, sfx, icmp\_typeerr), \

1031 &(iface)->stats.icmp.typeerr)

1032#else

[ 1033](group__net__stats.md#ga96beec38aeb91a9d95b4e1e415c0d229)#define NET\_STATS\_PROMETHEUS\_ICMP(iface, dev\_id, sfx)

1034#endif

1035

1036/\* UDP layer statistics \*/

1037#if defined(CONFIG\_NET\_STATISTICS\_UDP)

1038#define NET\_STATS\_PROMETHEUS\_UDP(iface, dev\_id, sfx) \

1039 NET\_STATS\_PROMETHEUS\_COUNTER\_DEFINE( \

1040 "UDP packets sent", \

1041 NET\_STATS\_GET\_INSTANCE(dev\_id, sfx, udp\_sent), \

1042 "packet\_count", \

1043 NET\_STATS\_GET\_COLLECTOR\_NAME(dev\_id, sfx), \

1044 NET\_STATS\_GET\_VAR(dev\_id, sfx, udp\_sent), \

1045 &(iface)->stats.udp.sent); \

1046 NET\_STATS\_PROMETHEUS\_COUNTER\_DEFINE( \

1047 "UDP packets received", \

1048 NET\_STATS\_GET\_INSTANCE(dev\_id, sfx, udp\_recv), \

1049 "packet\_count", \

1050 NET\_STATS\_GET\_COLLECTOR\_NAME(dev\_id, sfx), \

1051 NET\_STATS\_GET\_VAR(dev\_id, sfx, udp\_recv), \

1052 &(iface)->stats.udp.recv); \

1053 NET\_STATS\_PROMETHEUS\_COUNTER\_DEFINE( \

1054 "UDP packets dropped", \

1055 NET\_STATS\_GET\_INSTANCE(dev\_id, sfx, udp\_drop), \

1056 "packet\_count", \

1057 NET\_STATS\_GET\_COLLECTOR\_NAME(dev\_id, sfx), \

1058 NET\_STATS\_GET\_VAR(dev\_id, sfx, udp\_drop), \

1059 &(iface)->stats.udp.drop); \

1060 NET\_STATS\_PROMETHEUS\_COUNTER\_DEFINE( \

1061 "UDP packets checksum error", \

1062 NET\_STATS\_GET\_INSTANCE(dev\_id, sfx, udp\_chkerr), \

1063 "packet\_count", \

1064 NET\_STATS\_GET\_COLLECTOR\_NAME(dev\_id, sfx), \

1065 NET\_STATS\_GET\_VAR(dev\_id, sfx, udp\_chkerr), \

1066 &(iface)->stats.udp.chkerr)

1067#else

[ 1068](group__net__stats.md#ga2d400caf2103d6718bc2871abba3eddb)#define NET\_STATS\_PROMETHEUS\_UDP(iface, dev\_id, sfx)

1069#endif

1070

1071/\* TCP layer statistics \*/

1072#if defined(CONFIG\_NET\_STATISTICS\_TCP)

1073#define NET\_STATS\_PROMETHEUS\_TCP(iface, dev\_id, sfx) \

1074 NET\_STATS\_PROMETHEUS\_COUNTER\_DEFINE( \

1075 "TCP bytes sent", \

1076 NET\_STATS\_GET\_INSTANCE(dev\_id, sfx, tcp\_bytes\_sent), \

1077 "byte\_count", \

1078 NET\_STATS\_GET\_COLLECTOR\_NAME(dev\_id, sfx), \

1079 NET\_STATS\_GET\_VAR(dev\_id, sfx, tcp\_bytes\_sent), \

1080 &(iface)->stats.tcp.bytes.sent); \

1081 NET\_STATS\_PROMETHEUS\_COUNTER\_DEFINE( \

1082 "TCP bytes received", \

1083 NET\_STATS\_GET\_INSTANCE(dev\_id, sfx, tcp\_bytes\_recv), \

1084 "byte\_count", \

1085 NET\_STATS\_GET\_COLLECTOR\_NAME(dev\_id, sfx), \

1086 NET\_STATS\_GET\_VAR(dev\_id, sfx, tcp\_bytes\_recv), \

1087 &(iface)->stats.tcp.bytes.received); \

1088 NET\_STATS\_PROMETHEUS\_COUNTER\_DEFINE( \

1089 "TCP bytes resent", \

1090 NET\_STATS\_GET\_INSTANCE(dev\_id, sfx, tcp\_bytes\_resent), \

1091 "byte\_count", \

1092 NET\_STATS\_GET\_COLLECTOR\_NAME(dev\_id, sfx), \

1093 NET\_STATS\_GET\_VAR(dev\_id, sfx, tcp\_bytes\_resent), \

1094 &(iface)->stats.tcp.resent); \

1095 NET\_STATS\_PROMETHEUS\_COUNTER\_DEFINE( \

1096 "TCP packets sent", \

1097 NET\_STATS\_GET\_INSTANCE(dev\_id, sfx, tcp\_sent), \

1098 "packet\_count", \

1099 NET\_STATS\_GET\_COLLECTOR\_NAME(dev\_id, sfx), \

1100 NET\_STATS\_GET\_VAR(dev\_id, sfx, tcp\_sent), \

1101 &(iface)->stats.tcp.sent); \

1102 NET\_STATS\_PROMETHEUS\_COUNTER\_DEFINE( \

1103 "TCP packets received", \

1104 NET\_STATS\_GET\_INSTANCE(dev\_id, sfx, tcp\_recv), \

1105 "packet\_count", \

1106 NET\_STATS\_GET\_COLLECTOR\_NAME(dev\_id, sfx), \

1107 NET\_STATS\_GET\_VAR(dev\_id, sfx, tcp\_recv), \

1108 &(iface)->stats.tcp.recv); \

1109 NET\_STATS\_PROMETHEUS\_COUNTER\_DEFINE( \

1110 "TCP packets dropped", \

1111 NET\_STATS\_GET\_INSTANCE(dev\_id, sfx, tcp\_drop), \

1112 "packet\_count", \

1113 NET\_STATS\_GET\_COLLECTOR\_NAME(dev\_id, sfx), \

1114 NET\_STATS\_GET\_VAR(dev\_id, sfx, tcp\_drop), \

1115 &(iface)->stats.tcp.drop); \

1116 NET\_STATS\_PROMETHEUS\_COUNTER\_DEFINE( \

1117 "TCP packets checksum error", \

1118 NET\_STATS\_GET\_INSTANCE(dev\_id, sfx, tcp\_chkerr), \

1119 "packet\_count", \

1120 NET\_STATS\_GET\_COLLECTOR\_NAME(dev\_id, sfx), \

1121 NET\_STATS\_GET\_VAR(dev\_id, sfx, tcp\_chkerr), \

1122 &(iface)->stats.tcp.chkerr); \

1123 NET\_STATS\_PROMETHEUS\_COUNTER\_DEFINE( \

1124 "TCP packets ack error", \

1125 NET\_STATS\_GET\_INSTANCE(dev\_id, sfx, tcp\_ackerr), \

1126 "packet\_count", \

1127 NET\_STATS\_GET\_COLLECTOR\_NAME(dev\_id, sfx), \

1128 NET\_STATS\_GET\_VAR(dev\_id, sfx, tcp\_ackerr), \

1129 &(iface)->stats.tcp.ackerr); \

1130 NET\_STATS\_PROMETHEUS\_COUNTER\_DEFINE( \

1131 "TCP packets reset error", \

1132 NET\_STATS\_GET\_INSTANCE(dev\_id, sfx, tcp\_rsterr), \

1133 "packet\_count", \

1134 NET\_STATS\_GET\_COLLECTOR\_NAME(dev\_id, sfx), \

1135 NET\_STATS\_GET\_VAR(dev\_id, sfx, tcp\_rsterr), \

1136 &(iface)->stats.tcp.rsterr); \

1137 NET\_STATS\_PROMETHEUS\_COUNTER\_DEFINE( \

1138 "TCP packets retransmitted", \

1139 NET\_STATS\_GET\_INSTANCE(dev\_id, sfx, tcp\_rexmit), \

1140 "packet\_count", \

1141 NET\_STATS\_GET\_COLLECTOR\_NAME(dev\_id, sfx), \

1142 NET\_STATS\_GET\_VAR(dev\_id, sfx, tcp\_rexmit), \

1143 &(iface)->stats.tcp.rexmit); \

1144 NET\_STATS\_PROMETHEUS\_COUNTER\_DEFINE( \

1145 "TCP reset received", \

1146 NET\_STATS\_GET\_INSTANCE(dev\_id, sfx, tcp\_rst\_recv), \

1147 "packet\_count", \

1148 NET\_STATS\_GET\_COLLECTOR\_NAME(dev\_id, sfx), \

1149 NET\_STATS\_GET\_VAR(dev\_id, sfx, tcp\_rst), \

1150 &(iface)->stats.tcp.rst); \

1151 NET\_STATS\_PROMETHEUS\_COUNTER\_DEFINE( \

1152 "TCP connection drop", \

1153 NET\_STATS\_GET\_INSTANCE(dev\_id, sfx, tcp\_conndrop), \

1154 "packet\_count", \

1155 NET\_STATS\_GET\_COLLECTOR\_NAME(dev\_id, sfx), \

1156 NET\_STATS\_GET\_VAR(dev\_id, sfx, tcp\_conndrop), \

1157 &(iface)->stats.tcp.conndrop); \

1158 NET\_STATS\_PROMETHEUS\_COUNTER\_DEFINE( \

1159 "TCP connection reset", \

1160 NET\_STATS\_GET\_INSTANCE(dev\_id, sfx, tcp\_connrst), \

1161 "packet\_count", \

1162 NET\_STATS\_GET\_COLLECTOR\_NAME(dev\_id, sfx), \

1163 NET\_STATS\_GET\_VAR(dev\_id, sfx, tcp\_connrst), \

1164 &(iface)->stats.tcp.connrst)

1165#else

[ 1166](group__net__stats.md#ga1b581725d1a8652a0b40e71ac2e99261)#define NET\_STATS\_PROMETHEUS\_TCP(iface, dev\_id, sfx)

1167#endif

1168

1169/\* IPv6 Neighbor Discovery statistics \*/

1170#if defined(CONFIG\_NET\_STATISTICS\_IPV6\_ND)

1171#define NET\_STATS\_PROMETHEUS\_IPV6\_ND(iface, dev\_id, sfx) \

1172 NET\_STATS\_PROMETHEUS\_COUNTER\_DEFINE( \

1173 "IPv6 ND packets sent", \

1174 NET\_STATS\_GET\_INSTANCE(dev\_id, sfx, ipv6\_nd\_sent), \

1175 "packet\_count", \

1176 NET\_STATS\_GET\_COLLECTOR\_NAME(dev\_id, sfx), \

1177 NET\_STATS\_GET\_VAR(dev\_id, sfx, ipv6\_nd\_sent), \

1178 &(iface)->stats.ipv6\_nd.sent); \

1179 NET\_STATS\_PROMETHEUS\_COUNTER\_DEFINE( \

1180 "IPv6 ND packets received", \

1181 NET\_STATS\_GET\_INSTANCE(dev\_id, sfx, ipv6\_nd\_recv), \

1182 "packet\_count", \

1183 NET\_STATS\_GET\_COLLECTOR\_NAME(dev\_id, sfx), \

1184 NET\_STATS\_GET\_VAR(dev\_id, sfx, ipv6\_nd\_recv), \

1185 &(iface)->stats.ipv6\_nd.recv); \

1186 NET\_STATS\_PROMETHEUS\_COUNTER\_DEFINE( \

1187 "IPv6 ND packets dropped", \

1188 NET\_STATS\_GET\_INSTANCE(dev\_id, sfx, ipv6\_nd\_drop), \

1189 "packet\_count", \

1190 NET\_STATS\_GET\_COLLECTOR\_NAME(dev\_id, sfx), \

1191 NET\_STATS\_GET\_VAR(dev\_id, sfx, ipv6\_nd\_drop), \

1192 &(iface)->stats.ipv6\_nd.drop)

1193#else

[ 1194](group__net__stats.md#ga1cc29c5da3740b2623fd625f9f360c6d)#define NET\_STATS\_PROMETHEUS\_IPV6\_ND(iface, dev\_id, sfx)

1195#endif

1196

1197/\* IPv6 Path MTU Discovery statistics \*/

1198#if defined(CONFIG\_NET\_STATISTICS\_IPV6\_PMTU)

1199#define NET\_STATS\_PROMETHEUS\_IPV6\_PMTU(iface, dev\_id, sfx) \

1200 NET\_STATS\_PROMETHEUS\_COUNTER\_DEFINE( \

1201 "IPv6 PMTU packets sent", \

1202 NET\_STATS\_GET\_INSTANCE(dev\_id, sfx, ipv6\_pmtu\_sent), \

1203 "packet\_count", \

1204 NET\_STATS\_GET\_COLLECTOR\_NAME(dev\_id, sfx), \

1205 NET\_STATS\_GET\_VAR(dev\_id, sfx, ipv6\_pmtu\_sent), \

1206 &(iface)->stats.ipv6\_pmtu.sent); \

1207 NET\_STATS\_PROMETHEUS\_COUNTER\_DEFINE( \

1208 "IPv6 PMTU packets received", \

1209 NET\_STATS\_GET\_INSTANCE(dev\_id, sfx, ipv6\_pmtu\_recv), \

1210 "packet\_count", \

1211 NET\_STATS\_GET\_COLLECTOR\_NAME(dev\_id, sfx), \

1212 NET\_STATS\_GET\_VAR(dev\_id, sfx, ipv6\_pmtu\_recv), \

1213 &(iface)->stats.ipv6\_pmtu.recv); \

1214 NET\_STATS\_PROMETHEUS\_COUNTER\_DEFINE( \

1215 "IPv6 PMTU packets dropped", \

1216 NET\_STATS\_GET\_INSTANCE(dev\_id, sfx, ipv6\_pmtu\_drop), \

1217 "packet\_count", \

1218 NET\_STATS\_GET\_COLLECTOR\_NAME(dev\_id, sfx), \

1219 NET\_STATS\_GET\_VAR(dev\_id, sfx, ipv6\_pmtu\_drop), \

1220 &(iface)->stats.ipv6\_pmtu.drop)

1221#else

[ 1222](group__net__stats.md#ga2593a73001deea960ccfb80cf71489d4)#define NET\_STATS\_PROMETHEUS\_IPV6\_PMTU(iface, dev\_id, sfx)

1223#endif

1224

1225/\* IPv4 Path MTU Discovery statistics \*/

1226#if defined(CONFIG\_NET\_STATISTICS\_IPV4\_PMTU)

1227#define NET\_STATS\_PROMETHEUS\_IPV4\_PMTU(iface, dev\_id, sfx) \

1228 NET\_STATS\_PROMETHEUS\_COUNTER\_DEFINE( \

1229 "IPv4 PMTU packets sent", \

1230 NET\_STATS\_GET\_INSTANCE(dev\_id, sfx, ipv4\_pmtu\_sent), \

1231 "packet\_count", \

1232 NET\_STATS\_GET\_COLLECTOR\_NAME(dev\_id, sfx), \

1233 NET\_STATS\_GET\_VAR(dev\_id, sfx, ipv4\_pmtu\_sent), \

1234 &(iface)->stats.ipv4\_pmtu.sent); \

1235 NET\_STATS\_PROMETHEUS\_COUNTER\_DEFINE( \

1236 "IPv4 PMTU packets received", \

1237 NET\_STATS\_GET\_INSTANCE(dev\_id, sfx, ipv4\_pmtu\_recv), \

1238 "packet\_count", \

1239 NET\_STATS\_GET\_COLLECTOR\_NAME(dev\_id, sfx), \

1240 NET\_STATS\_GET\_VAR(dev\_id, sfx, ipv4\_pmtu\_recv), \

1241 &(iface)->stats.ipv4\_pmtu.recv); \

1242 NET\_STATS\_PROMETHEUS\_COUNTER\_DEFINE( \

1243 "IPv4 PMTU packets dropped", \

1244 NET\_STATS\_GET\_INSTANCE(dev\_id, sfx, ipv4\_pmtu\_drop), \

1245 "packet\_count", \

1246 NET\_STATS\_GET\_COLLECTOR\_NAME(dev\_id, sfx), \

1247 NET\_STATS\_GET\_VAR(dev\_id, sfx, ipv4\_pmtu\_drop), \

1248 &(iface)->stats.ipv4\_pmtu.drop)

1249#else

[ 1250](group__net__stats.md#gaaa0bc9dd9f53da03492d10c399db8eab)#define NET\_STATS\_PROMETHEUS\_IPV4\_PMTU(iface, dev\_id, sfx)

1251#endif

1252

1253/\* IPv6 Multicast Listener Discovery statistics \*/

1254#if defined(CONFIG\_NET\_STATISTICS\_MLD)

1255#define NET\_STATS\_PROMETHEUS\_MLD(iface, dev\_id, sfx) \

1256 NET\_STATS\_PROMETHEUS\_COUNTER\_DEFINE( \

1257 "IPv6 MLD packets sent", \

1258 NET\_STATS\_GET\_INSTANCE(dev\_id, sfx, ipv6\_mld\_sent), \

1259 "packet\_count", \

1260 NET\_STATS\_GET\_COLLECTOR\_NAME(dev\_id, sfx), \

1261 NET\_STATS\_GET\_VAR(dev\_id, sfx, ipv6\_mld\_sent), \

1262 &(iface)->stats.ipv6\_mld.sent); \

1263 NET\_STATS\_PROMETHEUS\_COUNTER\_DEFINE( \

1264 "IPv6 MLD packets received", \

1265 NET\_STATS\_GET\_INSTANCE(dev\_id, sfx, ipv6\_mld\_recv), \

1266 "packet\_count", \

1267 NET\_STATS\_GET\_COLLECTOR\_NAME(dev\_id, sfx), \

1268 NET\_STATS\_GET\_VAR(dev\_id, sfx, ipv6\_mld\_recv), \

1269 &(iface)->stats.ipv6\_mld.recv); \

1270 NET\_STATS\_PROMETHEUS\_COUNTER\_DEFINE( \

1271 "IPv6 MLD packets dropped", \

1272 NET\_STATS\_GET\_INSTANCE(dev\_id, sfx, ipv6\_mld\_drop), \

1273 "packet\_count", \

1274 NET\_STATS\_GET\_COLLECTOR\_NAME(dev\_id, sfx), \

1275 NET\_STATS\_GET\_VAR(dev\_id, sfx, ipv6\_mld\_drop), \

1276 &(iface)->stats.ipv6\_mld.drop)

1277#else

[ 1278](group__net__stats.md#ga5c4827a519269cc00323dfe57921117b)#define NET\_STATS\_PROMETHEUS\_MLD(iface, dev\_id, sfx)

1279#endif

1280

1281/\* IPv4 IGMP statistics \*/

1282#if defined(CONFIG\_NET\_STATISTICS\_IGMP)

1283#define NET\_STATS\_PROMETHEUS\_IGMP(iface, dev\_id, sfx) \

1284 NET\_STATS\_PROMETHEUS\_COUNTER\_DEFINE( \

1285 "IPv4 IGMP packets sent", \

1286 NET\_STATS\_GET\_INSTANCE(dev\_id, sfx, ipv4\_igmp\_sent), \

1287 "packet\_count", \

1288 NET\_STATS\_GET\_COLLECTOR\_NAME(dev\_id, sfx), \

1289 NET\_STATS\_GET\_VAR(dev\_id, sfx, ipv4\_igmp\_sent), \

1290 &(iface)->stats.ipv4\_igmp.sent); \

1291 NET\_STATS\_PROMETHEUS\_COUNTER\_DEFINE( \

1292 "IPv4 IGMP packets received", \

1293 NET\_STATS\_GET\_INSTANCE(dev\_id, sfx, ipv4\_igmp\_recv), \

1294 "packet\_count", \

1295 NET\_STATS\_GET\_COLLECTOR\_NAME(dev\_id, sfx), \

1296 NET\_STATS\_GET\_VAR(dev\_id, sfx, ipv4\_igmp\_recv), \

1297 &(iface)->stats.ipv4\_igmp.recv); \

1298 NET\_STATS\_PROMETHEUS\_COUNTER\_DEFINE( \

1299 "IPv4 IGMP packets dropped", \

1300 NET\_STATS\_GET\_INSTANCE(dev\_id, sfx, ipv4\_igmp\_drop), \

1301 "packet\_count", \

1302 NET\_STATS\_GET\_COLLECTOR\_NAME(dev\_id, sfx), \

1303 NET\_STATS\_GET\_VAR(dev\_id, sfx, ipv4\_igmp\_drop), \

1304 &(iface)->stats.ipv4\_igmp.drop)

1305#else

[ 1306](group__net__stats.md#ga8782a593de8ae207e57abfcc9477e256)#define NET\_STATS\_PROMETHEUS\_IGMP(iface, dev\_id, sfx)

1307#endif

1308

1309/\* DNS statistics \*/

1310#if defined(CONFIG\_NET\_STATISTICS\_DNS)

1311#define NET\_STATS\_PROMETHEUS\_DNS(iface, dev\_id, sfx) \

1312 NET\_STATS\_PROMETHEUS\_COUNTER\_DEFINE( \

1313 "DNS packets sent", \

1314 NET\_STATS\_GET\_INSTANCE(dev\_id, sfx, dns\_sent), \

1315 "packet\_count", \

1316 NET\_STATS\_GET\_COLLECTOR\_NAME(dev\_id, sfx), \

1317 NET\_STATS\_GET\_VAR(dev\_id, sfx, dns\_sent), \

1318 &(iface)->stats.dns.sent); \

1319 NET\_STATS\_PROMETHEUS\_COUNTER\_DEFINE( \

1320 "DNS packets received", \

1321 NET\_STATS\_GET\_INSTANCE(dev\_id, sfx, dns\_recv), \

1322 "packet\_count", \

1323 NET\_STATS\_GET\_COLLECTOR\_NAME(dev\_id, sfx), \

1324 NET\_STATS\_GET\_VAR(dev\_id, sfx, dns\_recv), \

1325 &(iface)->stats.dns.recv); \

1326 NET\_STATS\_PROMETHEUS\_COUNTER\_DEFINE( \

1327 "DNS packets dropped", \

1328 NET\_STATS\_GET\_INSTANCE(dev\_id, sfx, dns\_drop), \

1329 "packet\_count", \

1330 NET\_STATS\_GET\_COLLECTOR\_NAME(dev\_id, sfx), \

1331 NET\_STATS\_GET\_VAR(dev\_id, sfx, dns\_drop), \

1332 &(iface)->stats.dns.drop)

1333#else

[ 1334](group__net__stats.md#gaef54299a895568956cbae9960c7bf844)#define NET\_STATS\_PROMETHEUS\_DNS(iface, dev\_id, sfx)

1335#endif

1336

1337/\* TX time statistics \*/

1338#if defined(CONFIG\_NET\_PKT\_TXTIME\_STATS)

1339#define NET\_STATS\_PROMETHEUS\_TX\_TIME(iface, dev\_id, sfx) \

1340 NET\_STATS\_PROMETHEUS\_SUMMARY\_DEFINE( \

1341 "TX time in microseconds", \

1342 NET\_STATS\_GET\_INSTANCE(dev\_id, sfx, tx\_time), \

1343 "time", \

1344 NET\_STATS\_GET\_COLLECTOR\_NAME(dev\_id, sfx), \

1345 NET\_STATS\_GET\_VAR(dev\_id, sfx, tx\_time), \

1346 &(iface)->stats.tx\_time)

1347#else

[ 1348](group__net__stats.md#gaf0c1ee536e8a816c537b6cf7344353f4)#define NET\_STATS\_PROMETHEUS\_TX\_TIME(iface, dev\_id, sfx)

1349#endif

1350

1351/\* RX time statistics \*/

1352#if defined(CONFIG\_NET\_PKT\_RXTIME\_STATS)

1353#define NET\_STATS\_PROMETHEUS\_RX\_TIME(iface, dev\_id, sfx) \

1354 NET\_STATS\_PROMETHEUS\_SUMMARY\_DEFINE( \

1355 "RX time in microseconds", \

1356 NET\_STATS\_GET\_INSTANCE(dev\_id, sfx, rx\_time), \

1357 "time", \

1358 NET\_STATS\_GET\_COLLECTOR\_NAME(dev\_id, sfx), \

1359 NET\_STATS\_GET\_VAR(dev\_id, sfx, rx\_time), \

1360 &(iface)->stats.rx\_time)

1361#else

[ 1362](group__net__stats.md#ga2b9c4b3dc4cd1cd2b79801e7a4b58849)#define NET\_STATS\_PROMETHEUS\_RX\_TIME(iface, dev\_id, sfx)

1363#endif

1364

1365/\* Per network interface statistics via Prometheus \*/

[ 1366](group__net__stats.md#gac79e6cd416c92f9d26843900a084b375)#define NET\_STATS\_PROMETHEUS(iface, dev\_id, sfx) \

1367 NET\_STATS\_PROMETHEUS\_COUNTER\_DEFINE( \

1368 "Processing error", \

1369 NET\_STATS\_GET\_INSTANCE(dev\_id, sfx, process\_error), \

1370 "error\_count", \

1371 NET\_STATS\_GET\_COLLECTOR\_NAME(dev\_id, sfx), \

1372 NET\_STATS\_GET\_VAR(dev\_id, sfx, processing\_error), \

1373 &(iface)->stats.processing\_error); \

1374 /\* IP layer error statistics \*/ \

1375 NET\_STATS\_PROMETHEUS\_COUNTER\_DEFINE( \

1376 "IP proto error", \

1377 NET\_STATS\_GET\_INSTANCE(dev\_id, sfx, ip\_proto\_error), \

1378 "error\_count", \

1379 NET\_STATS\_GET\_COLLECTOR\_NAME(dev\_id, sfx), \

1380 NET\_STATS\_GET\_VAR(dev\_id, sfx, ip\_errors\_protoerr), \

1381 &(iface)->stats.ip\_errors.protoerr); \

1382 NET\_STATS\_PROMETHEUS\_COUNTER\_DEFINE( \

1383 "IP version/header len error", \

1384 NET\_STATS\_GET\_INSTANCE(dev\_id, sfx, ip\_vhl\_error), \

1385 "error\_count", \

1386 NET\_STATS\_GET\_COLLECTOR\_NAME(dev\_id, sfx), \

1387 NET\_STATS\_GET\_VAR(dev\_id, sfx, ip\_errors\_vhlerr), \

1388 &(iface)->stats.ip\_errors.vhlerr); \

1389 NET\_STATS\_PROMETHEUS\_COUNTER\_DEFINE( \

1390 "IP header len error (high byte)", \

1391 NET\_STATS\_GET\_INSTANCE(dev\_id, sfx, ip\_hblen\_error), \

1392 "error\_count", \

1393 NET\_STATS\_GET\_COLLECTOR\_NAME(dev\_id, sfx), \

1394 NET\_STATS\_GET\_VAR(dev\_id, sfx, ip\_errors\_hblenerr), \

1395 &(iface)->stats.ip\_errors.hblenerr); \

1396 NET\_STATS\_PROMETHEUS\_COUNTER\_DEFINE( \

1397 "IP header len error (low byte)", \

1398 NET\_STATS\_GET\_INSTANCE(dev\_id, sfx, ip\_lblen\_error), \

1399 "error\_count", \

1400 NET\_STATS\_GET\_COLLECTOR\_NAME(dev\_id, sfx), \

1401 NET\_STATS\_GET\_VAR(dev\_id, sfx, ip\_errors\_lblenerr), \

1402 &(iface)->stats.ip\_errors.lblenerr); \

1403 NET\_STATS\_PROMETHEUS\_COUNTER\_DEFINE( \

1404 "IP fragment error", \

1405 NET\_STATS\_GET\_INSTANCE(dev\_id, sfx, ip\_frag\_error), \

1406 "error\_count", \

1407 NET\_STATS\_GET\_COLLECTOR\_NAME(dev\_id, sfx), \

1408 NET\_STATS\_GET\_VAR(dev\_id, sfx, ip\_errors\_fragerr), \

1409 &(iface)->stats.ip\_errors.fragerr); \

1410 NET\_STATS\_PROMETHEUS\_COUNTER\_DEFINE( \

1411 "IP checksum error", \

1412 NET\_STATS\_GET\_INSTANCE(dev\_id, sfx, ip\_chk\_error), \

1413 "error\_count", \

1414 NET\_STATS\_GET\_COLLECTOR\_NAME(dev\_id, sfx), \

1415 NET\_STATS\_GET\_VAR(dev\_id, sfx, ip\_errors\_chkerr), \

1416 &(iface)->stats.ip\_errors.chkerr); \

1417 /\* General network statistics \*/ \

1418 NET\_STATS\_PROMETHEUS\_COUNTER\_DEFINE( \

1419 "Bytes received", \

1420 NET\_STATS\_GET\_INSTANCE(dev\_id, sfx, bytes\_recv), \

1421 "byte\_count", \

1422 NET\_STATS\_GET\_COLLECTOR\_NAME(dev\_id, sfx), \

1423 NET\_STATS\_GET\_VAR(dev\_id, sfx, bytes\_recv), \

1424 &(iface)->stats.bytes.received); \

1425 NET\_STATS\_PROMETHEUS\_COUNTER\_DEFINE( \

1426 "Bytes sent", \

1427 NET\_STATS\_GET\_INSTANCE(dev\_id, sfx, bytes\_sent), \

1428 "byte\_count", \

1429 NET\_STATS\_GET\_COLLECTOR\_NAME(dev\_id, sfx), \

1430 NET\_STATS\_GET\_VAR(dev\_id, sfx, bytes\_sent), \

1431 &(iface)->stats.bytes.sent); \

1432 NET\_STATS\_PROMETHEUS\_IPV6(iface, dev\_id, sfx); \

1433 NET\_STATS\_PROMETHEUS\_IPV4(iface, dev\_id, sfx); \

1434 NET\_STATS\_PROMETHEUS\_ICMP(iface, dev\_id, sfx); \

1435 NET\_STATS\_PROMETHEUS\_UDP(iface, dev\_id, sfx); \

1436 NET\_STATS\_PROMETHEUS\_TCP(iface, dev\_id, sfx); \

1437 NET\_STATS\_PROMETHEUS\_IPV6\_ND(iface, dev\_id, sfx); \

1438 NET\_STATS\_PROMETHEUS\_IPV6\_PMTU(iface, dev\_id, sfx); \

1439 NET\_STATS\_PROMETHEUS\_IPV4\_PMTU(iface, dev\_id, sfx); \

1440 NET\_STATS\_PROMETHEUS\_MLD(iface, dev\_id, sfx); \

1441 NET\_STATS\_PROMETHEUS\_IGMP(iface, dev\_id, sfx); \

1442 NET\_STATS\_PROMETHEUS\_DNS(iface, dev\_id, sfx); \

1443 NET\_STATS\_PROMETHEUS\_TX\_TIME(iface, dev\_id, sfx); \

1444 NET\_STATS\_PROMETHEUS\_RX\_TIME(iface, dev\_id, sfx)

1445

1449

1450#ifdef \_\_cplusplus

1451}

1452#endif

1453

1454#endif /\* ZEPHYR\_INCLUDE\_NET\_NET\_STATS\_H\_ \*/

[collector.h](collector_8h.md)

Prometheus collector APIs.

[gauge.h](gauge_8h.md)

Prometheus gauge APIs.

[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)

#define NET\_MGMT\_DEFINE\_REQUEST\_HANDLER(\_mgmt\_request)

Declare a request handler function for the given network event.

**Definition** net\_mgmt.h:111

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

[net\_stats\_bytes::sent](structnet__stats__bytes.md#a89368f376c02d25c5a7a5719851a0ac7)

net\_stats\_t sent

Number of bytes sent.

**Definition** net\_stats.h:52

[net\_stats\_bytes::received](structnet__stats__bytes.md#a8bc21878924210278c6e0e2861163be4)

net\_stats\_t received

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

**Definition** net\_stats.h:558

[net\_stats\_eth\_csum::rx\_csum\_offload\_good](structnet__stats__eth__csum.md#a1f1ba5c01c6232cd739d069ddb871b17)

net\_stats\_t rx\_csum\_offload\_good

Number of good RX checksum offloading.

**Definition** net\_stats.h:560

[net\_stats\_eth\_csum::rx\_csum\_offload\_errors](structnet__stats__eth__csum.md#ac4fc04d66193070d4f52a4c07f29ccce)

net\_stats\_t rx\_csum\_offload\_errors

Number of failed RX checksum offloading.

**Definition** net\_stats.h:563

[net\_stats\_eth\_errors](structnet__stats__eth__errors.md)

Ethernet error statistics.

**Definition** net\_stats.h:479

[net\_stats\_eth\_errors::tx\_carrier\_errors](structnet__stats__eth__errors.md#a0043d1a1481040a6d7439bd23423ec12)

net\_stats\_t tx\_carrier\_errors

Number of TX carrier errors.

**Definition** net\_stats.h:517

[net\_stats\_eth\_errors::uncorr\_ecc\_errors](structnet__stats__eth__errors.md#a07d0a435f2129556520c732571d28edf)

net\_stats\_t uncorr\_ecc\_errors

Number of uncorrected ECC errors.

**Definition** net\_stats.h:532

[net\_stats\_eth\_errors::rx\_long\_length\_errors](structnet__stats__eth__errors.md#a0e83e270a35222ed3e927800be4159e7)

net\_stats\_t rx\_long\_length\_errors

Number of RX long length errors.

**Definition** net\_stats.h:499

[net\_stats\_eth\_errors::tx\_window\_errors](structnet__stats__eth__errors.md#a17624a12d6473bdd78698076fed0d122)

net\_stats\_t tx\_window\_errors

Number of TX window errors.

**Definition** net\_stats.h:526

[net\_stats\_eth\_errors::corr\_ecc\_errors](structnet__stats__eth__errors.md#a257113639f0e0e3085febb7a147f498f)

net\_stats\_t corr\_ecc\_errors

Number of corrected ECC errors.

**Definition** net\_stats.h:535

[net\_stats\_eth\_errors::rx\_missed\_errors](structnet__stats__eth__errors.md#a2d2b2c4e3764ebec841f1ecbe7058d99)

net\_stats\_t rx\_missed\_errors

Number of RX missed errors.

**Definition** net\_stats.h:496

[net\_stats\_eth\_errors::rx\_crc\_errors](structnet__stats__eth__errors.md#a4dab70cf219269bb393ce14faf0ed77e)

net\_stats\_t rx\_crc\_errors

Number of RX CRC errors.

**Definition** net\_stats.h:487

[net\_stats\_eth\_errors::rx\_short\_length\_errors](structnet__stats__eth__errors.md#a5e3d39d8417bb180cbfcb8c901006e81)

net\_stats\_t rx\_short\_length\_errors

Number of RX short length errors.

**Definition** net\_stats.h:502

[net\_stats\_eth\_errors::rx\_align\_errors](structnet__stats__eth__errors.md#a7618f10af3443c49a6e256bb41e77781)

net\_stats\_t rx\_align\_errors

Number of RX buffer align errors.

**Definition** net\_stats.h:505

[net\_stats\_eth\_errors::rx\_dma\_failed](structnet__stats__eth__errors.md#a7bcfbb13836f162ceeb5f021304b5c76)

net\_stats\_t rx\_dma\_failed

Number of RX DMA failed errors.

**Definition** net\_stats.h:508

[net\_stats\_eth\_errors::rx\_no\_buffer\_count](structnet__stats__eth__errors.md#a82622736d226b4d3b999f1f22ccf8529)

net\_stats\_t rx\_no\_buffer\_count

Number of RX net\_pkt allocation errors.

**Definition** net\_stats.h:493

[net\_stats\_eth\_errors::tx\_fifo\_errors](structnet__stats__eth__errors.md#a84630da9b82557f56dc35cd59ca2f7ae)

net\_stats\_t tx\_fifo\_errors

Number of TX FIFO errors.

**Definition** net\_stats.h:520

[net\_stats\_eth\_errors::rx\_frame\_errors](structnet__stats__eth__errors.md#a8dfcc5cd1b4decec5783d01ba7033b05)

net\_stats\_t rx\_frame\_errors

Number of RX frame errors.

**Definition** net\_stats.h:490

[net\_stats\_eth\_errors::rx\_over\_errors](structnet__stats__eth__errors.md#a9afee89f5bb01907e7cd515e2a0ff1b5)

net\_stats\_t rx\_over\_errors

Number of RX overrun errors.

**Definition** net\_stats.h:484

[net\_stats\_eth\_errors::tx\_dma\_failed](structnet__stats__eth__errors.md#abfbf6478b7afdd5935d7c6948c9ef426)

net\_stats\_t tx\_dma\_failed

Number of TX DMA failed errors.

**Definition** net\_stats.h:529

[net\_stats\_eth\_errors::rx\_length\_errors](structnet__stats__eth__errors.md#aca0e2e4807fa70279dee8ddaad2d7ef7)

net\_stats\_t rx\_length\_errors

Number of RX length errors.

**Definition** net\_stats.h:481

[net\_stats\_eth\_errors::rx\_buf\_alloc\_failed](structnet__stats__eth__errors.md#adbcae9c10c081f1cdf304bcdce740aa4)

net\_stats\_t rx\_buf\_alloc\_failed

Number of RX net\_buf allocation errors.

**Definition** net\_stats.h:511

[net\_stats\_eth\_errors::tx\_heartbeat\_errors](structnet__stats__eth__errors.md#ae2a13733c1a5f0cc3e00efca0c3f429d)

net\_stats\_t tx\_heartbeat\_errors

Number of TX heartbeat errors.

**Definition** net\_stats.h:523

[net\_stats\_eth\_errors::tx\_aborted\_errors](structnet__stats__eth__errors.md#afec6a7e24c6f3cc74dd9f739f27b3e48)

net\_stats\_t tx\_aborted\_errors

Number of TX aborted errors.

**Definition** net\_stats.h:514

[net\_stats\_eth\_flow](structnet__stats__eth__flow.md)

Ethernet flow control statistics.

**Definition** net\_stats.h:541

[net\_stats\_eth\_flow::rx\_flow\_control\_xon](structnet__stats__eth__flow.md#a08e5da4ff78fe3893b9c9a628cefe4f2)

net\_stats\_t rx\_flow\_control\_xon

Number of RX XON flow control.

**Definition** net\_stats.h:543

[net\_stats\_eth\_flow::tx\_flow\_control\_xon](structnet__stats__eth__flow.md#a31412e8bf9d38ba630ea856e958a48d7)

net\_stats\_t tx\_flow\_control\_xon

Number of TX XON flow control.

**Definition** net\_stats.h:549

[net\_stats\_eth\_flow::rx\_flow\_control\_xoff](structnet__stats__eth__flow.md#a8f9b93537b3c11be70f276aaa72cb637)

net\_stats\_t rx\_flow\_control\_xoff

Number of RX XOFF flow control.

**Definition** net\_stats.h:546

[net\_stats\_eth\_flow::tx\_flow\_control\_xoff](structnet__stats__eth__flow.md#a969d81f9db20312d2d2aa7f70f93bdd5)

net\_stats\_t tx\_flow\_control\_xoff

Number of TX XOFF flow control.

**Definition** net\_stats.h:552

[net\_stats\_eth\_hw\_timestamp](structnet__stats__eth__hw__timestamp.md)

Ethernet hardware timestamp statistics.

**Definition** net\_stats.h:569

[net\_stats\_eth\_hw\_timestamp::tx\_hwtstamp\_timeouts](structnet__stats__eth__hw__timestamp.md#a41f605499dbf88a879522fdfa4633d9e)

net\_stats\_t tx\_hwtstamp\_timeouts

Number of RX hardware timestamp timeout.

**Definition** net\_stats.h:574

[net\_stats\_eth\_hw\_timestamp::rx\_hwtstamp\_cleared](structnet__stats__eth__hw__timestamp.md#acd3d5f72d7df568110d96093e0c9534d)

net\_stats\_t rx\_hwtstamp\_cleared

Number of RX hardware timestamp cleared.

**Definition** net\_stats.h:571

[net\_stats\_eth\_hw\_timestamp::tx\_hwtstamp\_skipped](structnet__stats__eth__hw__timestamp.md#ae1f983faf4a999308c464e4af5a5284b)

net\_stats\_t tx\_hwtstamp\_skipped

Number of RX hardware timestamp skipped.

**Definition** net\_stats.h:577

[net\_stats\_eth](structnet__stats__eth.md)

All Ethernet specific statistics.

**Definition** net\_stats.h:593

[net\_stats\_eth::broadcast](structnet__stats__eth.md#a054beb909134b0e0f22f5df599549128)

struct net\_stats\_pkts broadcast

Total number of broadcast packets received and sent.

**Definition** net\_stats.h:601

[net\_stats\_eth::csum](structnet__stats__eth.md#a2169ae06bace1a93663bccf88c8d7a29)

struct net\_stats\_eth\_csum csum

Total number of checksum errors in RX and TX.

**Definition** net\_stats.h:616

[net\_stats\_eth::tx\_dropped](structnet__stats__eth.md#a257c349cf3d32d38796e3899e702454a)

net\_stats\_t tx\_dropped

Total number of dropped TX packets.

**Definition** net\_stats.h:625

[net\_stats\_eth::hw\_timestamp](structnet__stats__eth.md#a44667efff73c17c089ed22d5b0da5ad3)

struct net\_stats\_eth\_hw\_timestamp hw\_timestamp

Total number of hardware timestamp errors in RX and TX.

**Definition** net\_stats.h:619

[net\_stats\_eth::multicast](structnet__stats__eth.md#a4f6a2903330518a132e7e547820e0bf2)

struct net\_stats\_pkts multicast

Total number of multicast packets received and sent.

**Definition** net\_stats.h:604

[net\_stats\_eth::flow\_control](structnet__stats__eth.md#a643010ac6360c8c0c08016725ba12222)

struct net\_stats\_eth\_flow flow\_control

Total number of flow control errors in RX and TX.

**Definition** net\_stats.h:613

[net\_stats\_eth::tx\_restart\_queue](structnet__stats__eth.md#a6699012226e25e8bad39076fed6dbfb5)

net\_stats\_t tx\_restart\_queue

Total number of TX queue restarts.

**Definition** net\_stats.h:631

[net\_stats\_eth::collisions](structnet__stats__eth.md#a822d4205791f59999c842610522f6fc5)

net\_stats\_t collisions

Total number of collisions.

**Definition** net\_stats.h:622

[net\_stats\_eth::bytes](structnet__stats__eth.md#a8c5cf1ead8ba214425a16fed1c2ad0fb)

struct net\_stats\_bytes bytes

Total number of bytes received and sent.

**Definition** net\_stats.h:595

[net\_stats\_eth::error\_details](structnet__stats__eth.md#a922feddb17fc020371f1bcc52c709415)

struct net\_stats\_eth\_errors error\_details

Total number of errors in RX and TX.

**Definition** net\_stats.h:610

[net\_stats\_eth::pkts](structnet__stats__eth.md#a97bd6026b16890743f344751a21107f1)

struct net\_stats\_pkts pkts

Total number of packets received and sent.

**Definition** net\_stats.h:598

[net\_stats\_eth::errors](structnet__stats__eth.md#a9c869740f416fbe0b54d7fefacb1fe29)

struct net\_stats\_pkts errors

Total number of errors in RX and TX.

**Definition** net\_stats.h:607

[net\_stats\_eth::tx\_timeout\_count](structnet__stats__eth.md#ab351258ae82abd09759d37774559d8bc)

net\_stats\_t tx\_timeout\_count

Total number of TX timeout errors.

**Definition** net\_stats.h:628

[net\_stats\_eth::unknown\_protocol](structnet__stats__eth.md#afaacee7cc1d0a35ae2344175421c40dd)

net\_stats\_t unknown\_protocol

Total number of RX unknown protocol packets.

**Definition** net\_stats.h:634

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

**Definition** net\_stats.h:645

[net\_stats\_ppp::chkerr](structnet__stats__ppp.md#a1332b31980f82236aeb0c3f9444e2ac6)

net\_stats\_t chkerr

Number of received PPP frames with a bad checksum.

**Definition** net\_stats.h:656

[net\_stats\_ppp::pkts](structnet__stats__ppp.md#a71fc81f3c5f3e65a476b3391f086d340)

struct net\_stats\_pkts pkts

Total number of packets received and sent.

**Definition** net\_stats.h:650

[net\_stats\_ppp::bytes](structnet__stats__ppp.md#ab2b48da7f19d4b83e3f41b41979b7ed8)

struct net\_stats\_bytes bytes

Total number of bytes received and sent.

**Definition** net\_stats.h:647

[net\_stats\_ppp::drop](structnet__stats__ppp.md#ae2e0a47a539e9d7bc97f9c63f889b276)

net\_stats\_t drop

Number of received and dropped PPP frames.

**Definition** net\_stats.h:653

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

**Definition** net\_stats.h:662

[net\_stats\_sta\_mgmt::beacons\_miss](structnet__stats__sta__mgmt.md#a29ae0079b4c780e0de2656a85ec15fe9)

net\_stats\_t beacons\_miss

Number of missed beacons.

**Definition** net\_stats.h:667

[net\_stats\_sta\_mgmt::beacons\_rx](structnet__stats__sta__mgmt.md#ac6e68fded8e19b20259442436923f815)

net\_stats\_t beacons\_rx

Number of received beacons.

**Definition** net\_stats.h:664

[net\_stats\_tc](structnet__stats__tc.md)

Traffic class statistics.

**Definition** net\_stats.h:319

[net\_stats\_tc::dropped](structnet__stats__tc.md#a1794f71f7fe7b3d20d406be4b28eb032)

net\_stats\_t dropped

Number of packets dropped for this traffic class.

**Definition** net\_stats.h:332

[net\_stats\_tc::bytes](structnet__stats__tc.md#a192a7ec0d24bce9e62f766e481ee5709)

net\_stats\_t bytes

Number of bytes sent for this traffic class.

**Definition** net\_stats.h:334

[net\_stats\_tc::tx\_time](structnet__stats__tc.md#a30288ef3bb0796cd18c3cf0aedbe875a)

struct net\_stats\_tx\_time tx\_time

Helper for calculating average TX time statistics.

**Definition** net\_stats.h:323

[net\_stats\_tc::pkts](structnet__stats__tc.md#a6614b5f5186635415a7d787260c39248)

net\_stats\_t pkts

Number of packets sent for this traffic class.

**Definition** net\_stats.h:330

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

**Definition** net\_stats.h:342

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

**Definition** net\_stats.h:673

[net\_stats\_wifi::broadcast](structnet__stats__wifi.md#a03dc04638c4b670bd7f3520d45fc1eda)

struct net\_stats\_pkts broadcast

Total number of broadcast packets received and sent.

**Definition** net\_stats.h:684

[net\_stats\_wifi::multicast](structnet__stats__wifi.md#a7e7f68215101885fd51c70e981da26e7)

struct net\_stats\_pkts multicast

Total number of multicast packets received and sent.

**Definition** net\_stats.h:687

[net\_stats\_wifi::sta\_mgmt](structnet__stats__wifi.md#a8bee22961545674e6ab100b58a04bf91)

struct net\_stats\_sta\_mgmt sta\_mgmt

Total number of beacon errors.

**Definition** net\_stats.h:675

[net\_stats\_wifi::bytes](structnet__stats__wifi.md#aa055b1e8bd8f1e50815c1028b562be07)

struct net\_stats\_bytes bytes

Total number of bytes received and sent.

**Definition** net\_stats.h:678

[net\_stats\_wifi::overrun\_count](structnet__stats__wifi.md#ac498c9e517f2cb2eb01d251e84159e7e)

net\_stats\_t overrun\_count

Total number of dropped packets at received and sent.

**Definition** net\_stats.h:696

[net\_stats\_wifi::pkts](structnet__stats__wifi.md#adbcdb2dd8733f2917c00a0b2d365393b)

struct net\_stats\_pkts pkts

Total number of packets received and sent.

**Definition** net\_stats.h:681

[net\_stats\_wifi::errors](structnet__stats__wifi.md#ae0149e64a94a9f96eb6680f94793c8c4)

struct net\_stats\_pkts errors

Total number of errors in RX and TX.

**Definition** net\_stats.h:690

[net\_stats\_wifi::unicast](structnet__stats__wifi.md#ae80dcd73a3c5ce3ec3282d1ae827b338)

struct net\_stats\_pkts unicast

Total number of unicast packets received and sent.

**Definition** net\_stats.h:693

[net\_stats](structnet__stats.md)

All network statistics in one struct.

**Definition** net\_stats.h:378

[net\_stats::processing\_error](structnet__stats.md#a3a4c90661d6b310b628262228a341fe2)

net\_stats\_t processing\_error

Count of malformed packets or packets we do not have handler for.

**Definition** net\_stats.h:380

[net\_stats::bytes](structnet__stats.md#a7a28233e6d23efdce0143469b9bb6c05)

struct net\_stats\_bytes bytes

This calculates amount of data transferred through all the network interfaces.

**Definition** net\_stats.h:386

[net\_stats::ip\_errors](structnet__stats.md#ac42cb13954d164e92a1ef60919a2a34e)

struct net\_stats\_ip\_errors ip\_errors

IP layer errors.

**Definition** net\_stats.h:389

[summary.h](summary_8h.md)

Prometheus summary APIs.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [net\_stats.h](net__stats_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
