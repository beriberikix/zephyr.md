---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/dfu__cli_8h_source.html
original_path: doxygen/html/dfu__cli_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

dfu\_cli.h

[Go to the documentation of this file.](dfu__cli_8h.md)

[ 1](group__bt__mesh__dfu__cli.md#ga2967b89e8fc3b848b70e493f6e821761)/\*

2 \* Copyright (c) 2020 Nordic Semiconductor ASA

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

14

15#ifndef ZEPHYR\_INCLUDE\_BLUETOOTH\_MESH\_DFU\_CLI\_H\_\_

16#define ZEPHYR\_INCLUDE\_BLUETOOTH\_MESH\_DFU\_CLI\_H\_\_

17

18#include <[zephyr/bluetooth/mesh/access.h](access_8h.md)>

19#include <[zephyr/bluetooth/mesh/blob\_cli.h](blob__cli_8h.md)>

20#include <[zephyr/bluetooth/mesh/dfu.h](dfu_8h.md)>

21

22#ifdef \_\_cplusplus

23extern "C" {

24#endif

25

26struct [bt\_mesh\_dfu\_cli](structbt__mesh__dfu__cli.md);

27

[ 36](group__bt__mesh__dfu__cli.md#ga0b10a95f9b7c806bfd8649280f535c96)#define BT\_MESH\_DFU\_CLI\_INIT(\_handlers) \

37 { \

38 .cb = \_handlers, \

39 .blob = { .cb = &\_bt\_mesh\_dfu\_cli\_blob\_handlers }, \

40 }

41

[ 48](group__bt__mesh__dfu__cli.md#gadee3710bb46d907a51232ca42cca7c2d)#define BT\_MESH\_MODEL\_DFU\_CLI(\_cli) \

49 BT\_MESH\_MODEL\_BLOB\_CLI(&(\_cli)->blob), \

50 BT\_MESH\_MODEL\_CB(BT\_MESH\_MODEL\_ID\_DFU\_CLI, \_bt\_mesh\_dfu\_cli\_op, NULL, \

51 \_cli, &\_bt\_mesh\_dfu\_cli\_cb)

52

[ 54](structbt__mesh__dfu__target.md)struct [bt\_mesh\_dfu\_target](structbt__mesh__dfu__target.md) {

[ 56](structbt__mesh__dfu__target.md#a96393388212d4bffd8fb00c82e58d364) struct [bt\_mesh\_blob\_target](structbt__mesh__blob__target.md) [blob](structbt__mesh__dfu__target.md#a96393388212d4bffd8fb00c82e58d364);

[ 58](structbt__mesh__dfu__target.md#a986a58915c0b0ab509ddbbbe475976d2) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [img\_idx](structbt__mesh__dfu__target.md#a986a58915c0b0ab509ddbbbe475976d2);

[ 60](structbt__mesh__dfu__target.md#a3d18d0ae1d0902cf84402b090a9aaa99) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [effect](structbt__mesh__dfu__target.md#a3d18d0ae1d0902cf84402b090a9aaa99);

[ 62](structbt__mesh__dfu__target.md#a4ad51f9dc3fdb39afeef55e4cd22b968) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__mesh__dfu__target.md#a4ad51f9dc3fdb39afeef55e4cd22b968);

[ 64](structbt__mesh__dfu__target.md#a43730ff708da06fe31e801adf7a79c0e) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [phase](structbt__mesh__dfu__target.md#a43730ff708da06fe31e801adf7a79c0e);

65};

66

[ 68](structbt__mesh__dfu__metadata__status.md)struct [bt\_mesh\_dfu\_metadata\_status](structbt__mesh__dfu__metadata__status.md) {

[ 70](structbt__mesh__dfu__metadata__status.md#a1d41b76b66acadc20f7f9ec1f4bc8b9b) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [idx](structbt__mesh__dfu__metadata__status.md#a1d41b76b66acadc20f7f9ec1f4bc8b9b);

[ 72](structbt__mesh__dfu__metadata__status.md#ae7ad71649f295142e48863b6d884b966) enum [bt\_mesh\_dfu\_status](group__bt__mesh__dfu.md#ga9e627a3c15de782faa11ef6c4ec5e05d) [status](structbt__mesh__dfu__metadata__status.md#ae7ad71649f295142e48863b6d884b966);

[ 74](structbt__mesh__dfu__metadata__status.md#a299723f7176938b2900cfdae4550965c) enum [bt\_mesh\_dfu\_effect](group__bt__mesh__dfu.md#gae7d7ef4ed1e65e5f8e1641a9c00bb7e8) [effect](structbt__mesh__dfu__metadata__status.md#a299723f7176938b2900cfdae4550965c);

75};

76

[ 78](structbt__mesh__dfu__target__status.md)struct [bt\_mesh\_dfu\_target\_status](structbt__mesh__dfu__target__status.md) {

[ 80](structbt__mesh__dfu__target__status.md#a25b2198ad4970d50707ff7994c9d1415) enum [bt\_mesh\_dfu\_status](group__bt__mesh__dfu.md#ga9e627a3c15de782faa11ef6c4ec5e05d) [status](structbt__mesh__dfu__target__status.md#a25b2198ad4970d50707ff7994c9d1415);

[ 82](structbt__mesh__dfu__target__status.md#aedbbfc07a68e60236901a3c79377fe65) enum [bt\_mesh\_dfu\_phase](group__bt__mesh__dfu.md#ga99919dcee1e41bc74bd59e33bec2ded2) [phase](structbt__mesh__dfu__target__status.md#aedbbfc07a68e60236901a3c79377fe65);

[ 84](structbt__mesh__dfu__target__status.md#aef5cbadbdd7b4b006dc304cd94c1bca4) enum [bt\_mesh\_dfu\_effect](group__bt__mesh__dfu.md#gae7d7ef4ed1e65e5f8e1641a9c00bb7e8) [effect](structbt__mesh__dfu__target__status.md#aef5cbadbdd7b4b006dc304cd94c1bca4);

[ 86](structbt__mesh__dfu__target__status.md#a2848ad866fbd437164b73a7504b75518) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [blob\_id](structbt__mesh__dfu__target__status.md#a2848ad866fbd437164b73a7504b75518);

[ 88](structbt__mesh__dfu__target__status.md#aedbd5c0a04460656d0a78eb49fd047b2) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [img\_idx](structbt__mesh__dfu__target__status.md#aedbd5c0a04460656d0a78eb49fd047b2);

[ 90](structbt__mesh__dfu__target__status.md#ab2e77b63918bb9a735a4ab20a4ca9333) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [ttl](structbt__mesh__dfu__target__status.md#ab2e77b63918bb9a735a4ab20a4ca9333);

91

[ 105](structbt__mesh__dfu__target__status.md#a13505201dbafeff54c0b35b445fd4f85) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [timeout\_base](structbt__mesh__dfu__target__status.md#a13505201dbafeff54c0b35b445fd4f85);

106};

107

125typedef enum [bt\_mesh\_dfu\_iter](group__bt__mesh__dfu.md#ga82475cb72f2ea8b60e70d6987eca2ff6) (\*[bt\_mesh\_dfu\_img\_cb\_t](group__bt__mesh__dfu__cli.md#ga2967b89e8fc3b848b70e493f6e821761))(

126 struct [bt\_mesh\_dfu\_cli](structbt__mesh__dfu__cli.md) \*cli, struct [bt\_mesh\_msg\_ctx](structbt__mesh__msg__ctx.md) \*ctx, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) idx,

127 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) total, const struct [bt\_mesh\_dfu\_img](structbt__mesh__dfu__img.md) \*img, void \*cb\_data);

128

[ 130](structbt__mesh__dfu__cli__cb.md)struct [bt\_mesh\_dfu\_cli\_cb](structbt__mesh__dfu__cli__cb.md) {

[ 137](structbt__mesh__dfu__cli__cb.md#ad2abfdf93f23cecd30e12241bb064a7f) void (\*[suspended](structbt__mesh__dfu__cli__cb.md#ad2abfdf93f23cecd30e12241bb064a7f))(struct [bt\_mesh\_dfu\_cli](structbt__mesh__dfu__cli.md) \*cli);

138

[ 147](structbt__mesh__dfu__cli__cb.md#aa3c8985490a6b2bd6fcd81dff0132060) void (\*[ended](structbt__mesh__dfu__cli__cb.md#aa3c8985490a6b2bd6fcd81dff0132060))(struct [bt\_mesh\_dfu\_cli](structbt__mesh__dfu__cli.md) \*cli,

148 enum [bt\_mesh\_dfu\_status](group__bt__mesh__dfu.md#ga9e627a3c15de782faa11ef6c4ec5e05d) reason);

149

[ 157](structbt__mesh__dfu__cli__cb.md#a6f580db9629d81f72c79d00a5aea2de4) void (\*[applied](structbt__mesh__dfu__cli__cb.md#a6f580db9629d81f72c79d00a5aea2de4))(struct [bt\_mesh\_dfu\_cli](structbt__mesh__dfu__cli.md) \*cli);

158

[ 166](structbt__mesh__dfu__cli__cb.md#a32b20280b2196437bad6d85edc017c63) void (\*[confirmed](structbt__mesh__dfu__cli__cb.md#a32b20280b2196437bad6d85edc017c63))(struct [bt\_mesh\_dfu\_cli](structbt__mesh__dfu__cli.md) \*cli);

167

[ 176](structbt__mesh__dfu__cli__cb.md#ab4d00147b1e525f392d09d5545de2465) void (\*[lost\_target](structbt__mesh__dfu__cli__cb.md#ab4d00147b1e525f392d09d5545de2465))(struct [bt\_mesh\_dfu\_cli](structbt__mesh__dfu__cli.md) \*cli,

177 struct [bt\_mesh\_dfu\_target](structbt__mesh__dfu__target.md) \*target);

178};

179

[ 184](structbt__mesh__dfu__cli.md)struct [bt\_mesh\_dfu\_cli](structbt__mesh__dfu__cli.md) {

[ 186](structbt__mesh__dfu__cli.md#a18d31020aba939826aa34060a4a28121) const struct [bt\_mesh\_dfu\_cli\_cb](structbt__mesh__dfu__cli__cb.md) \*[cb](structbt__mesh__dfu__cli.md#a18d31020aba939826aa34060a4a28121);

[ 188](structbt__mesh__dfu__cli.md#a945b5c9f70086ca57d3ee77704ece6fd) struct [bt\_mesh\_blob\_cli](structbt__mesh__blob__cli.md) [blob](structbt__mesh__dfu__cli.md#a945b5c9f70086ca57d3ee77704ece6fd);

189

190 /\* runtime state \*/

191

[ 192](structbt__mesh__dfu__cli.md#a94924c2ad2654a14b23a07ea0351ec1b) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [op](structbt__mesh__dfu__cli.md#a94924c2ad2654a14b23a07ea0351ec1b);

[ 193](structbt__mesh__dfu__cli.md#ab882e681b4bfc66374503c83237f57dd) const struct [bt\_mesh\_model](structbt__mesh__model.md) \*[mod](structbt__mesh__dfu__cli.md#ab882e681b4bfc66374503c83237f57dd);

194

195 struct {

[ 196](structbt__mesh__dfu__cli.md#a9396bb9e1245ab2613e3f7dfd753e793) const struct [bt\_mesh\_dfu\_slot](structbt__mesh__dfu__slot.md) \*[slot](structbt__mesh__dfu__cli.md#a9396bb9e1245ab2613e3f7dfd753e793);

[ 197](structbt__mesh__dfu__cli.md#a29a8240e5d47abaabf9d356bcdcba48d) const struct [bt\_mesh\_blob\_io](structbt__mesh__blob__io.md) \*[io](structbt__mesh__dfu__cli.md#a29a8240e5d47abaabf9d356bcdcba48d);

[ 198](structbt__mesh__dfu__cli.md#a1848081925dce6ac2083ce5eb8fb0b33) struct [bt\_mesh\_blob\_xfer](structbt__mesh__blob__xfer.md) [blob](structbt__mesh__dfu__cli.md#a945b5c9f70086ca57d3ee77704ece6fd);

[ 199](structbt__mesh__dfu__cli.md#aeaf4f0114a6a47ec6d866ce7b6714d47) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [state](structbt__mesh__dfu__cli.md#aeaf4f0114a6a47ec6d866ce7b6714d47);

[ 200](structbt__mesh__dfu__cli.md#a3e5d177198a4c57ccd98a53c20490c89) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [flags](structbt__mesh__dfu__cli.md#a3e5d177198a4c57ccd98a53c20490c89);

[ 201](structbt__mesh__dfu__cli.md#a9a8676e704a0346e1030f93d7ab6213c) } [xfer](structbt__mesh__dfu__cli.md#a9a8676e704a0346e1030f93d7ab6213c);

202

203 struct {

[ 204](structbt__mesh__dfu__cli.md#a463a5c12df5ba3041c46c5c008d473da) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [ttl](structbt__mesh__dfu__cli.md#a463a5c12df5ba3041c46c5c008d473da);

[ 205](structbt__mesh__dfu__cli.md#a40b6dfe0c3dc545afc30cd18c5b498b2) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [type](structbt__mesh__dfu__cli.md#a40b6dfe0c3dc545afc30cd18c5b498b2);

[ 206](structbt__mesh__dfu__cli.md#aa6f7be1a8dcd76f519e934654f96c909) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [img\_cnt](structbt__mesh__dfu__cli.md#aa6f7be1a8dcd76f519e934654f96c909);

[ 207](structbt__mesh__dfu__cli.md#a67450510328c50e52fa97c80903508cd) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [addr](structbt__mesh__dfu__cli.md#a67450510328c50e52fa97c80903508cd);

[ 208](structbt__mesh__dfu__cli.md#af7ec498fa49b8e5cc0a3d67ad8dedee5) struct k\_sem [sem](structbt__mesh__dfu__cli.md#af7ec498fa49b8e5cc0a3d67ad8dedee5);

[ 209](structbt__mesh__dfu__cli.md#ad6cc63e09b15d8471fde2192977be2ed) void \*[params](structbt__mesh__dfu__cli.md#ad6cc63e09b15d8471fde2192977be2ed);

[ 210](structbt__mesh__dfu__cli.md#a9531713e4659188de31015b66dfc38bc) [bt\_mesh\_dfu\_img\_cb\_t](group__bt__mesh__dfu__cli.md#ga2967b89e8fc3b848b70e493f6e821761) [img\_cb](structbt__mesh__dfu__cli.md#a9531713e4659188de31015b66dfc38bc);

[ 211](structbt__mesh__dfu__cli.md#a8f5d37bda72f1a112428958404ddce63) } [req](structbt__mesh__dfu__cli.md#a8f5d37bda72f1a112428958404ddce63);

212};

213

[ 215](structbt__mesh__dfu__cli__xfer__blob__params.md)struct [bt\_mesh\_dfu\_cli\_xfer\_blob\_params](structbt__mesh__dfu__cli__xfer__blob__params.md) {

216 /\* Logarithmic representation of the block size. \*/

[ 217](structbt__mesh__dfu__cli__xfer__blob__params.md#a45452ae73f585ffba5c76291d41dd1ed) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [block\_size\_log](structbt__mesh__dfu__cli__xfer__blob__params.md#a45452ae73f585ffba5c76291d41dd1ed);

[ 219](structbt__mesh__dfu__cli__xfer__blob__params.md#a1015b239306bd5eb1c9648b5c1d59481) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [chunk\_size](structbt__mesh__dfu__cli__xfer__blob__params.md#a1015b239306bd5eb1c9648b5c1d59481);

220};

221

[ 223](structbt__mesh__dfu__cli__xfer.md)struct [bt\_mesh\_dfu\_cli\_xfer](structbt__mesh__dfu__cli__xfer.md) {

[ 225](structbt__mesh__dfu__cli__xfer.md#adece8c0e0cec2262a7066b27636fc46e) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [blob\_id](structbt__mesh__dfu__cli__xfer.md#adece8c0e0cec2262a7066b27636fc46e);

[ 227](structbt__mesh__dfu__cli__xfer.md#a3c25a54eb4e557d749a9fb1ba66aecb4) const struct [bt\_mesh\_dfu\_slot](structbt__mesh__dfu__slot.md) \*[slot](structbt__mesh__dfu__cli__xfer.md#a3c25a54eb4e557d749a9fb1ba66aecb4);

[ 229](structbt__mesh__dfu__cli__xfer.md#a6608f683fd94e12f7c3ef5f3de7ec248) enum [bt\_mesh\_blob\_xfer\_mode](group__bt__mesh__blob.md#gae0cb28c0e50d02f6e003062457053618) [mode](structbt__mesh__dfu__cli__xfer.md#a6608f683fd94e12f7c3ef5f3de7ec248);

[ 233](structbt__mesh__dfu__cli__xfer.md#a2c4feacc090dace0986e533257f9b291) const struct [bt\_mesh\_dfu\_cli\_xfer\_blob\_params](structbt__mesh__dfu__cli__xfer__blob__params.md) \*[blob\_params](structbt__mesh__dfu__cli__xfer.md#a2c4feacc090dace0986e533257f9b291);

234};

235

[ 252](group__bt__mesh__dfu__cli.md#ga20764694315adb4f846dcff20f377417)int [bt\_mesh\_dfu\_cli\_send](group__bt__mesh__dfu__cli.md#ga20764694315adb4f846dcff20f377417)(struct [bt\_mesh\_dfu\_cli](structbt__mesh__dfu__cli.md) \*cli,

253 const struct [bt\_mesh\_blob\_cli\_inputs](structbt__mesh__blob__cli__inputs.md) \*inputs,

254 const struct [bt\_mesh\_blob\_io](structbt__mesh__blob__io.md) \*io,

255 const struct [bt\_mesh\_dfu\_cli\_xfer](structbt__mesh__dfu__cli__xfer.md) \*xfer);

256

[ 263](group__bt__mesh__dfu__cli.md#gaa1ed22da058839c9f3234ce2e41eda32)int [bt\_mesh\_dfu\_cli\_suspend](group__bt__mesh__dfu__cli.md#gaa1ed22da058839c9f3234ce2e41eda32)(struct [bt\_mesh\_dfu\_cli](structbt__mesh__dfu__cli.md) \*cli);

264

[ 271](group__bt__mesh__dfu__cli.md#ga0011fb5c03e6e8c2babfb677d528033b)int [bt\_mesh\_dfu\_cli\_resume](group__bt__mesh__dfu__cli.md#ga0011fb5c03e6e8c2babfb677d528033b)(struct [bt\_mesh\_dfu\_cli](structbt__mesh__dfu__cli.md) \*cli);

272

[ 283](group__bt__mesh__dfu__cli.md#ga4c7353f45a6e33884844fd9d2f443750)int [bt\_mesh\_dfu\_cli\_cancel](group__bt__mesh__dfu__cli.md#ga4c7353f45a6e33884844fd9d2f443750)(struct [bt\_mesh\_dfu\_cli](structbt__mesh__dfu__cli.md) \*cli,

284 struct [bt\_mesh\_msg\_ctx](structbt__mesh__msg__ctx.md) \*ctx);

285

[ 295](group__bt__mesh__dfu__cli.md#ga2904ba992a00ee9fba6704c1efc8f074)int [bt\_mesh\_dfu\_cli\_apply](group__bt__mesh__dfu__cli.md#ga2904ba992a00ee9fba6704c1efc8f074)(struct [bt\_mesh\_dfu\_cli](structbt__mesh__dfu__cli.md) \*cli);

296

[ 310](group__bt__mesh__dfu__cli.md#gaf76f0cdb5c6b0df12ddb495c718c3c93)int [bt\_mesh\_dfu\_cli\_confirm](group__bt__mesh__dfu__cli.md#gaf76f0cdb5c6b0df12ddb495c718c3c93)(struct [bt\_mesh\_dfu\_cli](structbt__mesh__dfu__cli.md) \*cli);

311

[ 319](group__bt__mesh__dfu__cli.md#ga073c5bc227040f1f33e7b3f2fe69a309)[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bt\_mesh\_dfu\_cli\_progress](group__bt__mesh__dfu__cli.md#ga073c5bc227040f1f33e7b3f2fe69a309)(struct [bt\_mesh\_dfu\_cli](structbt__mesh__dfu__cli.md) \*cli);

320

[ 328](group__bt__mesh__dfu__cli.md#gad6308700322d96676635bcf0b70c74f7)bool [bt\_mesh\_dfu\_cli\_is\_busy](group__bt__mesh__dfu__cli.md#gad6308700322d96676635bcf0b70c74f7)(struct [bt\_mesh\_dfu\_cli](structbt__mesh__dfu__cli.md) \*cli);

329

[ 348](group__bt__mesh__dfu__cli.md#ga4c33f9457d4f367760a51a771dfd2671)int [bt\_mesh\_dfu\_cli\_imgs\_get](group__bt__mesh__dfu__cli.md#ga4c33f9457d4f367760a51a771dfd2671)(struct [bt\_mesh\_dfu\_cli](structbt__mesh__dfu__cli.md) \*cli,

349 struct [bt\_mesh\_msg\_ctx](structbt__mesh__msg__ctx.md) \*ctx,

350 [bt\_mesh\_dfu\_img\_cb\_t](group__bt__mesh__dfu__cli.md#ga2967b89e8fc3b848b70e493f6e821761) cb, void \*cb\_data,

351 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) max\_count);

352

[ 368](group__bt__mesh__dfu__cli.md#ga20b3e7d3d3640149a20d698a6aa7dca5)int [bt\_mesh\_dfu\_cli\_metadata\_check](group__bt__mesh__dfu__cli.md#ga20b3e7d3d3640149a20d698a6aa7dca5)(struct [bt\_mesh\_dfu\_cli](structbt__mesh__dfu__cli.md) \*cli,

369 struct [bt\_mesh\_msg\_ctx](structbt__mesh__msg__ctx.md) \*ctx, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) img\_idx,

370 const struct [bt\_mesh\_dfu\_slot](structbt__mesh__dfu__slot.md) \*slot,

371 struct [bt\_mesh\_dfu\_metadata\_status](structbt__mesh__dfu__metadata__status.md) \*rsp);

372

[ 381](group__bt__mesh__dfu__cli.md#gab754da11705a2d6a24ec828aa7862579)int [bt\_mesh\_dfu\_cli\_status\_get](group__bt__mesh__dfu__cli.md#gab754da11705a2d6a24ec828aa7862579)(struct [bt\_mesh\_dfu\_cli](structbt__mesh__dfu__cli.md) \*cli,

382 struct [bt\_mesh\_msg\_ctx](structbt__mesh__msg__ctx.md) \*ctx,

383 struct [bt\_mesh\_dfu\_target\_status](structbt__mesh__dfu__target__status.md) \*rsp);

384

[ 389](group__bt__mesh__dfu__cli.md#ga3dd10bd1e8673973fd6db98d3ebda354)[int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) [bt\_mesh\_dfu\_cli\_timeout\_get](group__bt__mesh__dfu__cli.md#ga3dd10bd1e8673973fd6db98d3ebda354)(void);

390

[ 395](group__bt__mesh__dfu__cli.md#ga603adf5b40b6e382c9035c9f2bad99a9)void [bt\_mesh\_dfu\_cli\_timeout\_set](group__bt__mesh__dfu__cli.md#ga603adf5b40b6e382c9035c9f2bad99a9)([int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) timeout);

396

398extern const struct [bt\_mesh\_blob\_cli\_cb](structbt__mesh__blob__cli__cb.md) \_bt\_mesh\_dfu\_cli\_blob\_handlers;

399extern const struct [bt\_mesh\_model\_cb](structbt__mesh__model__cb.md) \_bt\_mesh\_dfu\_cli\_cb;

400extern const struct [bt\_mesh\_model\_op](structbt__mesh__model__op.md) \_bt\_mesh\_dfu\_cli\_op[];

402

403#ifdef \_\_cplusplus

404}

405#endif

406

407#endif /\* ZEPHYR\_INCLUDE\_BLUETOOTH\_MESH\_DFU\_CLI\_H\_\_ \*/

408

[access.h](access_8h.md)

Access layer APIs.

[blob\_cli.h](blob__cli_8h.md)

[dfu.h](dfu_8h.md)

[bt\_mesh\_blob\_xfer\_mode](group__bt__mesh__blob.md#gae0cb28c0e50d02f6e003062457053618)

bt\_mesh\_blob\_xfer\_mode

BLOB transfer mode.

**Definition** blob.h:29

[bt\_mesh\_dfu\_cli\_resume](group__bt__mesh__dfu__cli.md#ga0011fb5c03e6e8c2babfb677d528033b)

int bt\_mesh\_dfu\_cli\_resume(struct bt\_mesh\_dfu\_cli \*cli)

Resume the suspended transfer.

[bt\_mesh\_dfu\_cli\_progress](group__bt__mesh__dfu__cli.md#ga073c5bc227040f1f33e7b3f2fe69a309)

uint8\_t bt\_mesh\_dfu\_cli\_progress(struct bt\_mesh\_dfu\_cli \*cli)

Get progress as a percentage of completion.

[bt\_mesh\_dfu\_cli\_send](group__bt__mesh__dfu__cli.md#ga20764694315adb4f846dcff20f377417)

int bt\_mesh\_dfu\_cli\_send(struct bt\_mesh\_dfu\_cli \*cli, const struct bt\_mesh\_blob\_cli\_inputs \*inputs, const struct bt\_mesh\_blob\_io \*io, const struct bt\_mesh\_dfu\_cli\_xfer \*xfer)

Start distributing a DFU.

[bt\_mesh\_dfu\_cli\_metadata\_check](group__bt__mesh__dfu__cli.md#ga20b3e7d3d3640149a20d698a6aa7dca5)

int bt\_mesh\_dfu\_cli\_metadata\_check(struct bt\_mesh\_dfu\_cli \*cli, struct bt\_mesh\_msg\_ctx \*ctx, uint8\_t img\_idx, const struct bt\_mesh\_dfu\_slot \*slot, struct bt\_mesh\_dfu\_metadata\_status \*rsp)

Perform a metadata check for the given DFU image slot.

[bt\_mesh\_dfu\_cli\_apply](group__bt__mesh__dfu__cli.md#ga2904ba992a00ee9fba6704c1efc8f074)

int bt\_mesh\_dfu\_cli\_apply(struct bt\_mesh\_dfu\_cli \*cli)

Apply the completed DFU transfer.

[bt\_mesh\_dfu\_img\_cb\_t](group__bt__mesh__dfu__cli.md#ga2967b89e8fc3b848b70e493f6e821761)

enum bt\_mesh\_dfu\_iter(\* bt\_mesh\_dfu\_img\_cb\_t)(struct bt\_mesh\_dfu\_cli \*cli, struct bt\_mesh\_msg\_ctx \*ctx, uint8\_t idx, uint8\_t total, const struct bt\_mesh\_dfu\_img \*img, void \*cb\_data)

DFU image callback.

**Definition** dfu\_cli.h:125

[bt\_mesh\_dfu\_cli\_timeout\_get](group__bt__mesh__dfu__cli.md#ga3dd10bd1e8673973fd6db98d3ebda354)

int32\_t bt\_mesh\_dfu\_cli\_timeout\_get(void)

Get the current procedure timeout value.

[bt\_mesh\_dfu\_cli\_imgs\_get](group__bt__mesh__dfu__cli.md#ga4c33f9457d4f367760a51a771dfd2671)

int bt\_mesh\_dfu\_cli\_imgs\_get(struct bt\_mesh\_dfu\_cli \*cli, struct bt\_mesh\_msg\_ctx \*ctx, bt\_mesh\_dfu\_img\_cb\_t cb, void \*cb\_data, uint8\_t max\_count)

Perform a DFU image list request.

[bt\_mesh\_dfu\_cli\_cancel](group__bt__mesh__dfu__cli.md#ga4c7353f45a6e33884844fd9d2f443750)

int bt\_mesh\_dfu\_cli\_cancel(struct bt\_mesh\_dfu\_cli \*cli, struct bt\_mesh\_msg\_ctx \*ctx)

Cancel a DFU transfer.

[bt\_mesh\_dfu\_cli\_timeout\_set](group__bt__mesh__dfu__cli.md#ga603adf5b40b6e382c9035c9f2bad99a9)

void bt\_mesh\_dfu\_cli\_timeout\_set(int32\_t timeout)

Set the procedure timeout value.

[bt\_mesh\_dfu\_cli\_suspend](group__bt__mesh__dfu__cli.md#gaa1ed22da058839c9f3234ce2e41eda32)

int bt\_mesh\_dfu\_cli\_suspend(struct bt\_mesh\_dfu\_cli \*cli)

Suspend a DFU transfer.

[bt\_mesh\_dfu\_cli\_status\_get](group__bt__mesh__dfu__cli.md#gab754da11705a2d6a24ec828aa7862579)

int bt\_mesh\_dfu\_cli\_status\_get(struct bt\_mesh\_dfu\_cli \*cli, struct bt\_mesh\_msg\_ctx \*ctx, struct bt\_mesh\_dfu\_target\_status \*rsp)

Get the status of a Target node.

[bt\_mesh\_dfu\_cli\_is\_busy](group__bt__mesh__dfu__cli.md#gad6308700322d96676635bcf0b70c74f7)

bool bt\_mesh\_dfu\_cli\_is\_busy(struct bt\_mesh\_dfu\_cli \*cli)

Check whether a DFU transfer is in progress.

[bt\_mesh\_dfu\_cli\_confirm](group__bt__mesh__dfu__cli.md#gaf76f0cdb5c6b0df12ddb495c718c3c93)

int bt\_mesh\_dfu\_cli\_confirm(struct bt\_mesh\_dfu\_cli \*cli)

Confirm that the active transfer has been applied on the Target nodes.

[bt\_mesh\_dfu\_iter](group__bt__mesh__dfu.md#ga82475cb72f2ea8b60e70d6987eca2ff6)

bt\_mesh\_dfu\_iter

Action for DFU iteration callbacks.

**Definition** dfu.h:128

[bt\_mesh\_dfu\_phase](group__bt__mesh__dfu.md#ga99919dcee1e41bc74bd59e33bec2ded2)

bt\_mesh\_dfu\_phase

DFU transfer phase.

**Definition** dfu.h:42

[bt\_mesh\_dfu\_status](group__bt__mesh__dfu.md#ga9e627a3c15de782faa11ef6c4ec5e05d)

bt\_mesh\_dfu\_status

DFU status.

**Definition** dfu.h:79

[bt\_mesh\_dfu\_effect](group__bt__mesh__dfu.md#gae7d7ef4ed1e65e5f8e1641a9c00bb7e8)

bt\_mesh\_dfu\_effect

Expected effect of a DFU transfer.

**Definition** dfu.h:108

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

[bt\_mesh\_blob\_cli\_cb](structbt__mesh__blob__cli__cb.md)

Event handler callbacks for the BLOB Transfer Client model.

**Definition** blob\_cli.h:190

[bt\_mesh\_blob\_cli\_inputs](structbt__mesh__blob__cli__inputs.md)

BLOB Transfer Client transfer inputs.

**Definition** blob\_cli.h:104

[bt\_mesh\_blob\_cli](structbt__mesh__blob__cli.md)

BLOB Transfer Client model instance.

**Definition** blob\_cli.h:289

[bt\_mesh\_blob\_io](structbt__mesh__blob__io.md)

BLOB stream.

**Definition** blob.h:145

[bt\_mesh\_blob\_target](structbt__mesh__blob__target.md)

BLOB Transfer Client Target node.

**Definition** blob\_cli.h:49

[bt\_mesh\_blob\_xfer](structbt__mesh__blob__xfer.md)

BLOB transfer.

**Definition** blob.h:123

[bt\_mesh\_dfu\_cli\_cb](structbt__mesh__dfu__cli__cb.md)

Firmware Update Client event callbacks.

**Definition** dfu\_cli.h:130

[bt\_mesh\_dfu\_cli\_cb::confirmed](structbt__mesh__dfu__cli__cb.md#a32b20280b2196437bad6d85edc017c63)

void(\* confirmed)(struct bt\_mesh\_dfu\_cli \*cli)

DFU transfer confirmed on all active Target nodes.

**Definition** dfu\_cli.h:166

[bt\_mesh\_dfu\_cli\_cb::applied](structbt__mesh__dfu__cli__cb.md#a6f580db9629d81f72c79d00a5aea2de4)

void(\* applied)(struct bt\_mesh\_dfu\_cli \*cli)

DFU transfer applied on all active Target nodes.

**Definition** dfu\_cli.h:157

[bt\_mesh\_dfu\_cli\_cb::ended](structbt__mesh__dfu__cli__cb.md#aa3c8985490a6b2bd6fcd81dff0132060)

void(\* ended)(struct bt\_mesh\_dfu\_cli \*cli, enum bt\_mesh\_dfu\_status reason)

DFU ended.

**Definition** dfu\_cli.h:147

[bt\_mesh\_dfu\_cli\_cb::lost\_target](structbt__mesh__dfu__cli__cb.md#ab4d00147b1e525f392d09d5545de2465)

void(\* lost\_target)(struct bt\_mesh\_dfu\_cli \*cli, struct bt\_mesh\_dfu\_target \*target)

DFU Target node was lost.

**Definition** dfu\_cli.h:176

[bt\_mesh\_dfu\_cli\_cb::suspended](structbt__mesh__dfu__cli__cb.md#ad2abfdf93f23cecd30e12241bb064a7f)

void(\* suspended)(struct bt\_mesh\_dfu\_cli \*cli)

BLOB transfer is suspended.

**Definition** dfu\_cli.h:137

[bt\_mesh\_dfu\_cli\_xfer\_blob\_params](structbt__mesh__dfu__cli__xfer__blob__params.md)

BLOB parameters for Firmware Update Client transfer:

**Definition** dfu\_cli.h:215

[bt\_mesh\_dfu\_cli\_xfer\_blob\_params::chunk\_size](structbt__mesh__dfu__cli__xfer__blob__params.md#a1015b239306bd5eb1c9648b5c1d59481)

uint16\_t chunk\_size

Base chunk size.

**Definition** dfu\_cli.h:219

[bt\_mesh\_dfu\_cli\_xfer\_blob\_params::block\_size\_log](structbt__mesh__dfu__cli__xfer__blob__params.md#a45452ae73f585ffba5c76291d41dd1ed)

uint8\_t block\_size\_log

**Definition** dfu\_cli.h:217

[bt\_mesh\_dfu\_cli\_xfer](structbt__mesh__dfu__cli__xfer.md)

Firmware Update Client transfer parameters:

**Definition** dfu\_cli.h:223

[bt\_mesh\_dfu\_cli\_xfer::blob\_params](structbt__mesh__dfu__cli__xfer.md#a2c4feacc090dace0986e533257f9b291)

const struct bt\_mesh\_dfu\_cli\_xfer\_blob\_params \* blob\_params

BLOB parameters to be used for the transfer, or NULL to retrieve Target nodes' capabilities before se...

**Definition** dfu\_cli.h:233

[bt\_mesh\_dfu\_cli\_xfer::slot](structbt__mesh__dfu__cli__xfer.md#a3c25a54eb4e557d749a9fb1ba66aecb4)

const struct bt\_mesh\_dfu\_slot \* slot

DFU image slot to transfer.

**Definition** dfu\_cli.h:227

[bt\_mesh\_dfu\_cli\_xfer::mode](structbt__mesh__dfu__cli__xfer.md#a6608f683fd94e12f7c3ef5f3de7ec248)

enum bt\_mesh\_blob\_xfer\_mode mode

Transfer mode (Push (Push BLOB Transfer Mode) or Pull (Pull BLOB Transfer Mode)).

**Definition** dfu\_cli.h:229

[bt\_mesh\_dfu\_cli\_xfer::blob\_id](structbt__mesh__dfu__cli__xfer.md#adece8c0e0cec2262a7066b27636fc46e)

uint64\_t blob\_id

BLOB ID to use for this transfer, or 0 to set it randomly.

**Definition** dfu\_cli.h:225

[bt\_mesh\_dfu\_cli](structbt__mesh__dfu__cli.md)

Firmware Update Client model instance.

**Definition** dfu\_cli.h:184

[bt\_mesh\_dfu\_cli::cb](structbt__mesh__dfu__cli.md#a18d31020aba939826aa34060a4a28121)

const struct bt\_mesh\_dfu\_cli\_cb \* cb

Callback structure.

**Definition** dfu\_cli.h:186

[bt\_mesh\_dfu\_cli::io](structbt__mesh__dfu__cli.md#a29a8240e5d47abaabf9d356bcdcba48d)

const struct bt\_mesh\_blob\_io \* io

**Definition** dfu\_cli.h:197

[bt\_mesh\_dfu\_cli::flags](structbt__mesh__dfu__cli.md#a3e5d177198a4c57ccd98a53c20490c89)

uint8\_t flags

**Definition** dfu\_cli.h:200

[bt\_mesh\_dfu\_cli::type](structbt__mesh__dfu__cli.md#a40b6dfe0c3dc545afc30cd18c5b498b2)

uint8\_t type

**Definition** dfu\_cli.h:205

[bt\_mesh\_dfu\_cli::ttl](structbt__mesh__dfu__cli.md#a463a5c12df5ba3041c46c5c008d473da)

uint8\_t ttl

**Definition** dfu\_cli.h:204

[bt\_mesh\_dfu\_cli::addr](structbt__mesh__dfu__cli.md#a67450510328c50e52fa97c80903508cd)

uint16\_t addr

**Definition** dfu\_cli.h:207

[bt\_mesh\_dfu\_cli::req](structbt__mesh__dfu__cli.md#a8f5d37bda72f1a112428958404ddce63)

struct bt\_mesh\_dfu\_cli::@351155012052214172346141005120226056146124264234 req

[bt\_mesh\_dfu\_cli::slot](structbt__mesh__dfu__cli.md#a9396bb9e1245ab2613e3f7dfd753e793)

const struct bt\_mesh\_dfu\_slot \* slot

**Definition** dfu\_cli.h:196

[bt\_mesh\_dfu\_cli::blob](structbt__mesh__dfu__cli.md#a945b5c9f70086ca57d3ee77704ece6fd)

struct bt\_mesh\_blob\_cli blob

Underlying BLOB Transfer Client.

**Definition** dfu\_cli.h:188

[bt\_mesh\_dfu\_cli::op](structbt__mesh__dfu__cli.md#a94924c2ad2654a14b23a07ea0351ec1b)

uint32\_t op

**Definition** dfu\_cli.h:192

[bt\_mesh\_dfu\_cli::img\_cb](structbt__mesh__dfu__cli.md#a9531713e4659188de31015b66dfc38bc)

bt\_mesh\_dfu\_img\_cb\_t img\_cb

**Definition** dfu\_cli.h:210

[bt\_mesh\_dfu\_cli::xfer](structbt__mesh__dfu__cli.md#a9a8676e704a0346e1030f93d7ab6213c)

struct bt\_mesh\_dfu\_cli::@370377057212243051110055047275311126236157331372 xfer

[bt\_mesh\_dfu\_cli::img\_cnt](structbt__mesh__dfu__cli.md#aa6f7be1a8dcd76f519e934654f96c909)

uint8\_t img\_cnt

**Definition** dfu\_cli.h:206

[bt\_mesh\_dfu\_cli::mod](structbt__mesh__dfu__cli.md#ab882e681b4bfc66374503c83237f57dd)

const struct bt\_mesh\_model \* mod

**Definition** dfu\_cli.h:193

[bt\_mesh\_dfu\_cli::params](structbt__mesh__dfu__cli.md#ad6cc63e09b15d8471fde2192977be2ed)

void \* params

**Definition** dfu\_cli.h:209

[bt\_mesh\_dfu\_cli::state](structbt__mesh__dfu__cli.md#aeaf4f0114a6a47ec6d866ce7b6714d47)

uint8\_t state

**Definition** dfu\_cli.h:199

[bt\_mesh\_dfu\_cli::sem](structbt__mesh__dfu__cli.md#af7ec498fa49b8e5cc0a3d67ad8dedee5)

struct k\_sem sem

**Definition** dfu\_cli.h:208

[bt\_mesh\_dfu\_img](structbt__mesh__dfu__img.md)

DFU image instance.

**Definition** dfu.h:140

[bt\_mesh\_dfu\_metadata\_status](structbt__mesh__dfu__metadata__status.md)

Metadata status response.

**Definition** dfu\_cli.h:68

[bt\_mesh\_dfu\_metadata\_status::idx](structbt__mesh__dfu__metadata__status.md#a1d41b76b66acadc20f7f9ec1f4bc8b9b)

uint8\_t idx

Image index.

**Definition** dfu\_cli.h:70

[bt\_mesh\_dfu\_metadata\_status::effect](structbt__mesh__dfu__metadata__status.md#a299723f7176938b2900cfdae4550965c)

enum bt\_mesh\_dfu\_effect effect

Effect of transfer.

**Definition** dfu\_cli.h:74

[bt\_mesh\_dfu\_metadata\_status::status](structbt__mesh__dfu__metadata__status.md#ae7ad71649f295142e48863b6d884b966)

enum bt\_mesh\_dfu\_status status

Status code.

**Definition** dfu\_cli.h:72

[bt\_mesh\_dfu\_slot](structbt__mesh__dfu__slot.md)

DFU image slot for DFU distribution.

**Definition** dfu.h:152

[bt\_mesh\_dfu\_target\_status](structbt__mesh__dfu__target__status.md)

DFU Target node status parameters.

**Definition** dfu\_cli.h:78

[bt\_mesh\_dfu\_target\_status::timeout\_base](structbt__mesh__dfu__target__status.md#a13505201dbafeff54c0b35b445fd4f85)

uint16\_t timeout\_base

Additional response time for the Target nodes, in 10-second increments.

**Definition** dfu\_cli.h:105

[bt\_mesh\_dfu\_target\_status::status](structbt__mesh__dfu__target__status.md#a25b2198ad4970d50707ff7994c9d1415)

enum bt\_mesh\_dfu\_status status

Status of the previous operation.

**Definition** dfu\_cli.h:80

[bt\_mesh\_dfu\_target\_status::blob\_id](structbt__mesh__dfu__target__status.md#a2848ad866fbd437164b73a7504b75518)

uint64\_t blob\_id

BLOB ID used in the transfer.

**Definition** dfu\_cli.h:86

[bt\_mesh\_dfu\_target\_status::ttl](structbt__mesh__dfu__target__status.md#ab2e77b63918bb9a735a4ab20a4ca9333)

uint8\_t ttl

TTL used in the transfer.

**Definition** dfu\_cli.h:90

[bt\_mesh\_dfu\_target\_status::phase](structbt__mesh__dfu__target__status.md#aedbbfc07a68e60236901a3c79377fe65)

enum bt\_mesh\_dfu\_phase phase

Phase of the current DFU transfer.

**Definition** dfu\_cli.h:82

[bt\_mesh\_dfu\_target\_status::img\_idx](structbt__mesh__dfu__target__status.md#aedbd5c0a04460656d0a78eb49fd047b2)

uint8\_t img\_idx

Image index to transfer.

**Definition** dfu\_cli.h:88

[bt\_mesh\_dfu\_target\_status::effect](structbt__mesh__dfu__target__status.md#aef5cbadbdd7b4b006dc304cd94c1bca4)

enum bt\_mesh\_dfu\_effect effect

The effect the update will have on the Target device's state.

**Definition** dfu\_cli.h:84

[bt\_mesh\_dfu\_target](structbt__mesh__dfu__target.md)

DFU Target node.

**Definition** dfu\_cli.h:54

[bt\_mesh\_dfu\_target::effect](structbt__mesh__dfu__target.md#a3d18d0ae1d0902cf84402b090a9aaa99)

uint8\_t effect

Expected DFU effect, see bt\_mesh\_dfu\_effect.

**Definition** dfu\_cli.h:60

[bt\_mesh\_dfu\_target::phase](structbt__mesh__dfu__target.md#a43730ff708da06fe31e801adf7a79c0e)

uint8\_t phase

Current DFU phase, see bt\_mesh\_dfu\_phase.

**Definition** dfu\_cli.h:64

[bt\_mesh\_dfu\_target::status](structbt__mesh__dfu__target.md#a4ad51f9dc3fdb39afeef55e4cd22b968)

uint8\_t status

Current DFU status, see bt\_mesh\_dfu\_status.

**Definition** dfu\_cli.h:62

[bt\_mesh\_dfu\_target::blob](structbt__mesh__dfu__target.md#a96393388212d4bffd8fb00c82e58d364)

struct bt\_mesh\_blob\_target blob

BLOB Target node.

**Definition** dfu\_cli.h:56

[bt\_mesh\_dfu\_target::img\_idx](structbt__mesh__dfu__target.md#a986a58915c0b0ab509ddbbbe475976d2)

uint8\_t img\_idx

Image index on the Target node.

**Definition** dfu\_cli.h:58

[bt\_mesh\_model\_cb](structbt__mesh__model__cb.md)

Model callback functions.

**Definition** access.h:809

[bt\_mesh\_model\_op](structbt__mesh__model__op.md)

Model opcode handler.

**Definition** access.h:359

[bt\_mesh\_model](structbt__mesh__model.md)

Abstraction that describes a Mesh Model instance.

**Definition** access.h:887

[bt\_mesh\_msg\_ctx](structbt__mesh__msg__ctx.md)

Message sending context.

**Definition** msg.h:76

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [mesh](dir_cb009b76fe94f798a2c866bd15366281.md)
- [dfu\_cli.h](dfu__cli_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
