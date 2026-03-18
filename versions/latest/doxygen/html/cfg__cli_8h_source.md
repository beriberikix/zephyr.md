---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/cfg__cli_8h_source.html
original_path: doxygen/html/cfg__cli_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

cfg\_cli.h

[Go to the documentation of this file.](cfg__cli_8h.md)

1

4

5/\*

6 \* Copyright (c) 2017 Intel Corporation

7 \*

8 \* SPDX-License-Identifier: Apache-2.0

9 \*/

10#ifndef ZEPHYR\_INCLUDE\_BLUETOOTH\_MESH\_CFG\_CLI\_H\_

11#define ZEPHYR\_INCLUDE\_BLUETOOTH\_MESH\_CFG\_CLI\_H\_

12

19

20#include <[stdint.h](stdint_8h.md)>

21#include <[stdbool.h](stdbool_8h.md)>

22

23#ifdef \_\_cplusplus

24extern "C" {

25#endif

26

27struct [bt\_mesh\_cfg\_cli](structbt__mesh__cfg__cli.md);

28struct [bt\_mesh\_cfg\_cli\_hb\_pub](structbt__mesh__cfg__cli__hb__pub.md);

29struct [bt\_mesh\_cfg\_cli\_hb\_sub](structbt__mesh__cfg__cli__hb__sub.md);

30struct [bt\_mesh\_cfg\_cli\_mod\_pub](structbt__mesh__cfg__cli__mod__pub.md);

31

[ 33](structbt__mesh__cfg__cli__cb.md)struct [bt\_mesh\_cfg\_cli\_cb](structbt__mesh__cfg__cli__cb.md) {

34

[ 48](structbt__mesh__cfg__cli__cb.md#aaae4e3f64e2033a466ad87d362ceb318) void (\*[comp\_data](structbt__mesh__cfg__cli__cb.md#aaae4e3f64e2033a466ad87d362ceb318))(struct [bt\_mesh\_cfg\_cli](structbt__mesh__cfg__cli.md) \*cli, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) page,

49 struct [net\_buf\_simple](structnet__buf__simple.md) \*buf);

50

[ 63](structbt__mesh__cfg__cli__cb.md#ab4130e909826aa7746092f49f8b4c52e) void (\*[mod\_pub\_status](structbt__mesh__cfg__cli__cb.md#ab4130e909826aa7746092f49f8b4c52e))(struct [bt\_mesh\_cfg\_cli](structbt__mesh__cfg__cli.md) \*cli, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) status,

64 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) elem\_addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mod\_id, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) cid,

65 struct [bt\_mesh\_cfg\_cli\_mod\_pub](structbt__mesh__cfg__cli__mod__pub.md) \*pub);

66

[ 78](structbt__mesh__cfg__cli__cb.md#af4a43f4c65d111e95211b715048534cc) void (\*[mod\_sub\_status](structbt__mesh__cfg__cli__cb.md#af4a43f4c65d111e95211b715048534cc))(struct [bt\_mesh\_cfg\_cli](structbt__mesh__cfg__cli.md) \*cli, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr,

79 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) status, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) elem\_addr,

80 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) sub\_addr, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mod\_id);

81

[ 98](structbt__mesh__cfg__cli__cb.md#a0ad46d1d4793577679f66c62175e14cf) void (\*[mod\_sub\_list](structbt__mesh__cfg__cli__cb.md#a0ad46d1d4793577679f66c62175e14cf))(struct [bt\_mesh\_cfg\_cli](structbt__mesh__cfg__cli.md) \*cli, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) status,

99 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) elem\_addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mod\_id, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) cid,

100 struct [net\_buf\_simple](structnet__buf__simple.md) \*buf);

101

[ 109](structbt__mesh__cfg__cli__cb.md#acf88660364760442dfab5280ae735d2d) void (\*[node\_reset\_status](structbt__mesh__cfg__cli__cb.md#acf88660364760442dfab5280ae735d2d))(struct [bt\_mesh\_cfg\_cli](structbt__mesh__cfg__cli.md) \*cli, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr);

110

[ 119](structbt__mesh__cfg__cli__cb.md#a5cf2c17a88c53c514fcaa73a6fd81b67) void (\*[beacon\_status](structbt__mesh__cfg__cli__cb.md#a5cf2c17a88c53c514fcaa73a6fd81b67))(struct [bt\_mesh\_cfg\_cli](structbt__mesh__cfg__cli.md) \*cli, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr,

120 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) status);

121

[ 130](structbt__mesh__cfg__cli__cb.md#ab937311c41af68b1cd52a8a1c86145b1) void (\*[ttl\_status](structbt__mesh__cfg__cli__cb.md#ab937311c41af68b1cd52a8a1c86145b1))(struct [bt\_mesh\_cfg\_cli](structbt__mesh__cfg__cli.md) \*cli, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr,

131 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) status);

132

[ 141](structbt__mesh__cfg__cli__cb.md#a9487a159a6c838a9218b3d76fa53248d) void (\*[friend\_status](structbt__mesh__cfg__cli__cb.md#a9487a159a6c838a9218b3d76fa53248d))(struct [bt\_mesh\_cfg\_cli](structbt__mesh__cfg__cli.md) \*cli, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr,

142 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) status);

143

[ 152](structbt__mesh__cfg__cli__cb.md#a6ef3730e9469bffd81cdd49c50cac7d5) void (\*[gatt\_proxy\_status](structbt__mesh__cfg__cli__cb.md#a6ef3730e9469bffd81cdd49c50cac7d5))(struct [bt\_mesh\_cfg\_cli](structbt__mesh__cfg__cli.md) \*cli, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr,

153 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) status);

154

[ 163](structbt__mesh__cfg__cli__cb.md#ad46ea40b75cc1d5d314fdefdca0076f8) void (\*[network\_transmit\_status](structbt__mesh__cfg__cli__cb.md#ad46ea40b75cc1d5d314fdefdca0076f8))(struct [bt\_mesh\_cfg\_cli](structbt__mesh__cfg__cli.md) \*cli, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr,

164 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) status);

165

[ 175](structbt__mesh__cfg__cli__cb.md#a89eab453e00662f6f3f8a5d78f20d120) void (\*[relay\_status](structbt__mesh__cfg__cli__cb.md#a89eab453e00662f6f3f8a5d78f20d120))(struct [bt\_mesh\_cfg\_cli](structbt__mesh__cfg__cli.md) \*cli, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr,

176 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) status, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) transmit);

177

[ 187](structbt__mesh__cfg__cli__cb.md#a49a7a8cab34bb70d2edd87b0017f1cf7) void (\*[net\_key\_status](structbt__mesh__cfg__cli__cb.md#a49a7a8cab34bb70d2edd87b0017f1cf7))(struct [bt\_mesh\_cfg\_cli](structbt__mesh__cfg__cli.md) \*cli, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr,

188 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) status, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx);

189

[ 201](structbt__mesh__cfg__cli__cb.md#acce08dfa5cb356a2203f0ef6c4e4bf5b) void (\*[net\_key\_list](structbt__mesh__cfg__cli__cb.md#acce08dfa5cb356a2203f0ef6c4e4bf5b))(struct [bt\_mesh\_cfg\_cli](structbt__mesh__cfg__cli.md) \*cli, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr,

202 struct [net\_buf\_simple](structnet__buf__simple.md) \*buf);

203

[ 214](structbt__mesh__cfg__cli__cb.md#a48ef4d0665d86d069b90533eb18e0fd0) void (\*[app\_key\_status](structbt__mesh__cfg__cli__cb.md#a48ef4d0665d86d069b90533eb18e0fd0))(struct [bt\_mesh\_cfg\_cli](structbt__mesh__cfg__cli.md) \*cli, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr,

215 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) status, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx,

216 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) app\_idx);

217

[ 231](structbt__mesh__cfg__cli__cb.md#ac331fc103d0f331093929f39e5b9d6ba) void (\*[app\_key\_list](structbt__mesh__cfg__cli__cb.md#ac331fc103d0f331093929f39e5b9d6ba))(struct [bt\_mesh\_cfg\_cli](structbt__mesh__cfg__cli.md) \*cli, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) status,

232 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, struct [net\_buf\_simple](structnet__buf__simple.md) \*buf);

233

[ 245](structbt__mesh__cfg__cli__cb.md#a3ccff69f21e0f3c585b951eb60c1bf5c) void (\*[mod\_app\_status](structbt__mesh__cfg__cli__cb.md#a3ccff69f21e0f3c585b951eb60c1bf5c))(struct [bt\_mesh\_cfg\_cli](structbt__mesh__cfg__cli.md) \*cli, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr,

246 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) status, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) elem\_addr,

247 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) app\_idx, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mod\_id);

248

[ 264](structbt__mesh__cfg__cli__cb.md#abf8501e73f44ab5ea7e54b8f2ff1f866) void (\*[mod\_app\_list](structbt__mesh__cfg__cli__cb.md#abf8501e73f44ab5ea7e54b8f2ff1f866))(struct [bt\_mesh\_cfg\_cli](structbt__mesh__cfg__cli.md) \*cli, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) status,

265 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) elem\_addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mod\_id, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) cid,

266 struct [net\_buf\_simple](structnet__buf__simple.md) \*buf);

267

[ 278](structbt__mesh__cfg__cli__cb.md#aca2d779401fa4521813e6578bd3bbd91) void (\*[node\_identity\_status](structbt__mesh__cfg__cli__cb.md#aca2d779401fa4521813e6578bd3bbd91))(struct [bt\_mesh\_cfg\_cli](structbt__mesh__cfg__cli.md) \*cli, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr,

279 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) status, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx,

280 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) identity);

281

[ 291](structbt__mesh__cfg__cli__cb.md#a66b5a8dd3bdd2468fe65496020b13495) void (\*[lpn\_timeout\_status](structbt__mesh__cfg__cli__cb.md#a66b5a8dd3bdd2468fe65496020b13495))(struct [bt\_mesh\_cfg\_cli](structbt__mesh__cfg__cli.md) \*cli, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr,

292 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) elem\_addr, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) timeout);

293

[ 304](structbt__mesh__cfg__cli__cb.md#a4d89033676eb4570cdd80f1715fd9bfb) void (\*[krp\_status](structbt__mesh__cfg__cli__cb.md#a4d89033676eb4570cdd80f1715fd9bfb))(struct [bt\_mesh\_cfg\_cli](structbt__mesh__cfg__cli.md) \*cli, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) status,

305 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) phase);

306

[ 316](structbt__mesh__cfg__cli__cb.md#a615852027a841b1779a50c9fd50bef6a) void (\*[hb\_pub\_status](structbt__mesh__cfg__cli__cb.md#a615852027a841b1779a50c9fd50bef6a))(struct [bt\_mesh\_cfg\_cli](structbt__mesh__cfg__cli.md) \*cli, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) status,

317 struct [bt\_mesh\_cfg\_cli\_hb\_pub](structbt__mesh__cfg__cli__hb__pub.md) \*pub);

318

[ 328](structbt__mesh__cfg__cli__cb.md#aa60dfd72a43273e1ffae2160bcc0845d) void (\*[hb\_sub\_status](structbt__mesh__cfg__cli__cb.md#aa60dfd72a43273e1ffae2160bcc0845d))(struct [bt\_mesh\_cfg\_cli](structbt__mesh__cfg__cli.md) \*cli, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) status,

329 struct [bt\_mesh\_cfg\_cli\_hb\_sub](structbt__mesh__cfg__cli__hb__sub.md) \*sub);

330};

331

[ 333](structbt__mesh__cfg__cli.md)struct [bt\_mesh\_cfg\_cli](structbt__mesh__cfg__cli.md) {

[ 335](structbt__mesh__cfg__cli.md#a525dd5391c83c525c012940575245cea) const struct [bt\_mesh\_model](structbt__mesh__model.md) \*[model](structbt__mesh__cfg__cli.md#a525dd5391c83c525c012940575245cea);

336

[ 338](structbt__mesh__cfg__cli.md#a7160cf5d22fa0b909482bbc76f27b6bd) const struct [bt\_mesh\_cfg\_cli\_cb](structbt__mesh__cfg__cli__cb.md) \*[cb](structbt__mesh__cfg__cli.md#a7160cf5d22fa0b909482bbc76f27b6bd);

339

340 /\* Internal parameters for tracking message responses. \*/

[ 341](structbt__mesh__cfg__cli.md#a472bf5015857ab97e1a40ab6cfa70bb1) struct [bt\_mesh\_msg\_ack\_ctx](structbt__mesh__msg__ack__ctx.md) [ack\_ctx](structbt__mesh__cfg__cli.md#a472bf5015857ab97e1a40ab6cfa70bb1);

342};

343

[ 349](group__bt__mesh__cfg__cli.md#ga2f0df6906a27ebbd86dcd11951114001)#define BT\_MESH\_MODEL\_CFG\_CLI(cli\_data) \

350 BT\_MESH\_MODEL\_CNT\_CB(BT\_MESH\_MODEL\_ID\_CFG\_CLI, \

351 bt\_mesh\_cfg\_cli\_op, NULL, \

352 cli\_data, 1, 0, &bt\_mesh\_cfg\_cli\_cb)

353

[ 362](group__bt__mesh__cfg__cli.md#gab542c707fb5bad0a15088fefda775a42)#define BT\_MESH\_PUB\_PERIOD\_100MS(steps) ((steps) & BIT\_MASK(6))

363

[ 371](group__bt__mesh__cfg__cli.md#ga29435e527a73ff6e19339b773c8eb79e)#define BT\_MESH\_PUB\_PERIOD\_SEC(steps) (((steps) & BIT\_MASK(6)) | (1 << 6))

372

[ 382](group__bt__mesh__cfg__cli.md#ga654204077adaa08259d1afbfe92e070e)#define BT\_MESH\_PUB\_PERIOD\_10SEC(steps) (((steps) & BIT\_MASK(6)) | (2 << 6))

383

[ 393](group__bt__mesh__cfg__cli.md#ga36c37f644ee39ad91b6167f68c806b7e)#define BT\_MESH\_PUB\_PERIOD\_10MIN(steps) (((steps) & BIT\_MASK(6)) | (3 << 6))

394

[ 396](structbt__mesh__cfg__cli__mod__pub.md)struct [bt\_mesh\_cfg\_cli\_mod\_pub](structbt__mesh__cfg__cli__mod__pub.md) {

[ 398](structbt__mesh__cfg__cli__mod__pub.md#ab52dd35df271ae5bd70a4640e6f3bea8) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [addr](structbt__mesh__cfg__cli__mod__pub.md#ab52dd35df271ae5bd70a4640e6f3bea8);

[ 400](structbt__mesh__cfg__cli__mod__pub.md#a29cbd50ad33f25ad3b98b4ec7ac56a6c) const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[uuid](structbt__mesh__cfg__cli__mod__pub.md#a29cbd50ad33f25ad3b98b4ec7ac56a6c);

[ 402](structbt__mesh__cfg__cli__mod__pub.md#aefbe5449a10379b064dea054300cb9a0) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [app\_idx](structbt__mesh__cfg__cli__mod__pub.md#aefbe5449a10379b064dea054300cb9a0);

[ 404](structbt__mesh__cfg__cli__mod__pub.md#aa7452f697410fdf8a63808bcb29c53ee) bool [cred\_flag](structbt__mesh__cfg__cli__mod__pub.md#aa7452f697410fdf8a63808bcb29c53ee);

[ 406](structbt__mesh__cfg__cli__mod__pub.md#a9513db038ec4f51734892bd1ce7d08f3) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [ttl](structbt__mesh__cfg__cli__mod__pub.md#a9513db038ec4f51734892bd1ce7d08f3);

[ 413](structbt__mesh__cfg__cli__mod__pub.md#a104afe2b8d9766e037293b09c0c1b91c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [period](structbt__mesh__cfg__cli__mod__pub.md#a104afe2b8d9766e037293b09c0c1b91c);

[ 418](structbt__mesh__cfg__cli__mod__pub.md#a2a5a0ead8155bf971c84f73dfa4ec282) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [transmit](structbt__mesh__cfg__cli__mod__pub.md#a2a5a0ead8155bf971c84f73dfa4ec282);

419};

420

[ 422](structbt__mesh__cfg__cli__hb__sub.md)struct [bt\_mesh\_cfg\_cli\_hb\_sub](structbt__mesh__cfg__cli__hb__sub.md) {

[ 424](structbt__mesh__cfg__cli__hb__sub.md#a01ec0c3cab7bb7ed76d7728390eb4f25) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [src](structbt__mesh__cfg__cli__hb__sub.md#a01ec0c3cab7bb7ed76d7728390eb4f25);

[ 426](structbt__mesh__cfg__cli__hb__sub.md#abc9ea18fbe86c260d6cf5d53c26a0248) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [dst](structbt__mesh__cfg__cli__hb__sub.md#abc9ea18fbe86c260d6cf5d53c26a0248);

[ 432](structbt__mesh__cfg__cli__hb__sub.md#a5a75c924f0868c664652503335b1b012) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [period](structbt__mesh__cfg__cli__hb__sub.md#a5a75c924f0868c664652503335b1b012);

[ 440](structbt__mesh__cfg__cli__hb__sub.md#a93624ab6c8a0c15c0b50490e0fcd3675) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [count](structbt__mesh__cfg__cli__hb__sub.md#a93624ab6c8a0c15c0b50490e0fcd3675);

[ 448](structbt__mesh__cfg__cli__hb__sub.md#a480b214e0e1974a6a54426c49e5d62d1) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [min](structbt__mesh__cfg__cli__hb__sub.md#a480b214e0e1974a6a54426c49e5d62d1);

[ 456](structbt__mesh__cfg__cli__hb__sub.md#aac96c2ab606e38f412e94539795c5594) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [max](structbt__mesh__cfg__cli__hb__sub.md#aac96c2ab606e38f412e94539795c5594);

457};

458

[ 460](structbt__mesh__cfg__cli__hb__pub.md)struct [bt\_mesh\_cfg\_cli\_hb\_pub](structbt__mesh__cfg__cli__hb__pub.md) {

[ 462](structbt__mesh__cfg__cli__hb__pub.md#a473df7dd958683d7502dcc983c4ceb8a) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [dst](structbt__mesh__cfg__cli__hb__pub.md#a473df7dd958683d7502dcc983c4ceb8a);

[ 474](structbt__mesh__cfg__cli__hb__pub.md#a13c7c155f30ca94d30090a25df50e4b2) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [count](structbt__mesh__cfg__cli__hb__pub.md#a13c7c155f30ca94d30090a25df50e4b2);

[ 480](structbt__mesh__cfg__cli__hb__pub.md#a8d17dd2df4be23cadad4b5746ddb50ad) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [period](structbt__mesh__cfg__cli__hb__pub.md#a8d17dd2df4be23cadad4b5746ddb50ad);

[ 482](structbt__mesh__cfg__cli__hb__pub.md#ac7f24f7bf942587ef83ca47d9ee4e7fb) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [ttl](structbt__mesh__cfg__cli__hb__pub.md#ac7f24f7bf942587ef83ca47d9ee4e7fb);

[ 489](structbt__mesh__cfg__cli__hb__pub.md#a94598c9b733075abe22d70f62293b5a1) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [feat](structbt__mesh__cfg__cli__hb__pub.md#a94598c9b733075abe22d70f62293b5a1);

[ 491](structbt__mesh__cfg__cli__hb__pub.md#a90a79d8b7ea91c6ba872dca15d87b356) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [net\_idx](structbt__mesh__cfg__cli__hb__pub.md#a90a79d8b7ea91c6ba872dca15d87b356);

492};

493

[ 502](group__bt__mesh__cfg__cli.md#gac6675d227749a69cedc5455c70626b76)int [bt\_mesh\_cfg\_cli\_node\_reset](group__bt__mesh__cfg__cli.md#gac6675d227749a69cedc5455c70626b76)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, bool \*status);

503

[ 523](group__bt__mesh__cfg__cli.md#ga36259e9c811a8f1a21d642739cf297df)int [bt\_mesh\_cfg\_cli\_comp\_data\_get](group__bt__mesh__cfg__cli.md#ga36259e9c811a8f1a21d642739cf297df)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) page, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*rsp,

524 struct [net\_buf\_simple](structnet__buf__simple.md) \*comp);

525

[ 540](group__bt__mesh__cfg__cli.md#ga2c8a79d1b70e91e0a09c848737bb4a22)int [bt\_mesh\_cfg\_cli\_beacon\_get](group__bt__mesh__cfg__cli.md#ga2c8a79d1b70e91e0a09c848737bb4a22)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*status);

541

[ 556](group__bt__mesh__cfg__cli.md#ga660df68049110332ff21610fe4e520c6)int [bt\_mesh\_cfg\_cli\_krp\_get](group__bt__mesh__cfg__cli.md#ga660df68049110332ff21610fe4e520c6)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) key\_net\_idx, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*status,

557 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*phase);

558

[ 575](group__bt__mesh__cfg__cli.md#gae51eee59090cfebed4561ed3bb4df005)int [bt\_mesh\_cfg\_cli\_krp\_set](group__bt__mesh__cfg__cli.md#gae51eee59090cfebed4561ed3bb4df005)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) key\_net\_idx,

576 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) transition, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*status, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*phase);

577

[ 594](group__bt__mesh__cfg__cli.md#gab513c82ebe434907a958cc6da990bd0b)int [bt\_mesh\_cfg\_cli\_beacon\_set](group__bt__mesh__cfg__cli.md#gab513c82ebe434907a958cc6da990bd0b)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) val, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*status);

595

[ 608](group__bt__mesh__cfg__cli.md#gaa141d4aabbed6c7780ac7f3955c8b580)int [bt\_mesh\_cfg\_cli\_ttl\_get](group__bt__mesh__cfg__cli.md#gaa141d4aabbed6c7780ac7f3955c8b580)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*ttl);

609

[ 623](group__bt__mesh__cfg__cli.md#ga2671234d739c802fd080a19d01235352)int [bt\_mesh\_cfg\_cli\_ttl\_set](group__bt__mesh__cfg__cli.md#ga2671234d739c802fd080a19d01235352)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) val, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*ttl);

624

[ 639](group__bt__mesh__cfg__cli.md#ga4dd1534e9d5b04fc99231ba5dde23e05)int [bt\_mesh\_cfg\_cli\_friend\_get](group__bt__mesh__cfg__cli.md#ga4dd1534e9d5b04fc99231ba5dde23e05)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*status);

640

[ 658](group__bt__mesh__cfg__cli.md#gacf8ad783910449c7cdc304c1b9b3fe0b)int [bt\_mesh\_cfg\_cli\_friend\_set](group__bt__mesh__cfg__cli.md#gacf8ad783910449c7cdc304c1b9b3fe0b)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) val, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*status);

659

[ 675](group__bt__mesh__cfg__cli.md#gaaf945377cf6a3d2b3e7c7cdb5a8df016)int [bt\_mesh\_cfg\_cli\_gatt\_proxy\_get](group__bt__mesh__cfg__cli.md#gaaf945377cf6a3d2b3e7c7cdb5a8df016)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*status);

676

[ 695](group__bt__mesh__cfg__cli.md#ga5a717835a416ba2930f65a975265649f)int [bt\_mesh\_cfg\_cli\_gatt\_proxy\_set](group__bt__mesh__cfg__cli.md#ga5a717835a416ba2930f65a975265649f)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) val, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*status);

696

[ 711](group__bt__mesh__cfg__cli.md#ga92ee7984b14590ed11a470c0dfea0bc9)int [bt\_mesh\_cfg\_cli\_net\_transmit\_get](group__bt__mesh__cfg__cli.md#ga92ee7984b14590ed11a470c0dfea0bc9)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*transmit);

712

[ 728](group__bt__mesh__cfg__cli.md#ga87f7c1e06b5c721c89031c527960bf40)int [bt\_mesh\_cfg\_cli\_net\_transmit\_set](group__bt__mesh__cfg__cli.md#ga87f7c1e06b5c721c89031c527960bf40)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) val,

729 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*transmit);

730

[ 748](group__bt__mesh__cfg__cli.md#ga4a50a6a5dcfdc42b7476f0b9e463ea45)int [bt\_mesh\_cfg\_cli\_relay\_get](group__bt__mesh__cfg__cli.md#ga4a50a6a5dcfdc42b7476f0b9e463ea45)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*status, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*transmit);

749

[ 773](group__bt__mesh__cfg__cli.md#ga7fe8418130568bdf2a5e56ed2ad027b0)int [bt\_mesh\_cfg\_cli\_relay\_set](group__bt__mesh__cfg__cli.md#ga7fe8418130568bdf2a5e56ed2ad027b0)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) new\_relay,

774 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) new\_transmit, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*status, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*transmit);

775

[ 790](group__bt__mesh__cfg__cli.md#ga283fb06ddb6427852ff0ac556d3c1852)int [bt\_mesh\_cfg\_cli\_net\_key\_add](group__bt__mesh__cfg__cli.md#ga283fb06ddb6427852ff0ac556d3c1852)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) key\_net\_idx,

791 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_key[16], [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*status);

792

[ 809](group__bt__mesh__cfg__cli.md#gab42c5bdff36bea35e967946462b12457)int [bt\_mesh\_cfg\_cli\_net\_key\_get](group__bt__mesh__cfg__cli.md#gab42c5bdff36bea35e967946462b12457)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*keys, size\_t \*key\_cnt);

810

[ 824](group__bt__mesh__cfg__cli.md#gab2963ec5536cb4b941578bb490fdc013)int [bt\_mesh\_cfg\_cli\_net\_key\_del](group__bt__mesh__cfg__cli.md#gab2963ec5536cb4b941578bb490fdc013)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) key\_net\_idx,

825 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*status);

826

[ 842](group__bt__mesh__cfg__cli.md#gafabf4c0fa707eba1fd40cc9a403daa07)int [bt\_mesh\_cfg\_cli\_app\_key\_add](group__bt__mesh__cfg__cli.md#gafabf4c0fa707eba1fd40cc9a403daa07)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) key\_net\_idx,

843 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) key\_app\_idx, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) app\_key[16], [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*status);

844

[ 866](group__bt__mesh__cfg__cli.md#ga6391ce297ca0be73ccd51044a9e0a76f)int [bt\_mesh\_cfg\_cli\_app\_key\_get](group__bt__mesh__cfg__cli.md#ga6391ce297ca0be73ccd51044a9e0a76f)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) key\_net\_idx,

867 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*status, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*keys, size\_t \*key\_cnt);

868

[ 883](group__bt__mesh__cfg__cli.md#ga5140472c687584babf885bc08349c865)int [bt\_mesh\_cfg\_cli\_app\_key\_del](group__bt__mesh__cfg__cli.md#ga5140472c687584babf885bc08349c865)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) key\_net\_idx,

884 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) key\_app\_idx, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*status);

885

[ 901](group__bt__mesh__cfg__cli.md#gaa4a02dd0c1f67621ee71d011fe4a29c1)int [bt\_mesh\_cfg\_cli\_mod\_app\_bind](group__bt__mesh__cfg__cli.md#gaa4a02dd0c1f67621ee71d011fe4a29c1)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) elem\_addr,

902 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mod\_app\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mod\_id, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*status);

903

[ 919](group__bt__mesh__cfg__cli.md#gaf82b54a4b2d3176b10daf728272a0977)int [bt\_mesh\_cfg\_cli\_mod\_app\_unbind](group__bt__mesh__cfg__cli.md#gaf82b54a4b2d3176b10daf728272a0977)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) elem\_addr,

920 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mod\_app\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mod\_id, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*status);

921

[ 938](group__bt__mesh__cfg__cli.md#gada33602562721c9f413eb06b34a823a8)int [bt\_mesh\_cfg\_cli\_mod\_app\_bind\_vnd](group__bt__mesh__cfg__cli.md#gada33602562721c9f413eb06b34a823a8)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) elem\_addr,

939 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mod\_app\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mod\_id, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) cid,

940 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*status);

941

[ 958](group__bt__mesh__cfg__cli.md#ga1fb53b9a49be25e633cac9d668c5b209)int [bt\_mesh\_cfg\_cli\_mod\_app\_unbind\_vnd](group__bt__mesh__cfg__cli.md#ga1fb53b9a49be25e633cac9d668c5b209)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) elem\_addr,

959 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mod\_app\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mod\_id, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) cid,

960 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*status);

961

[ 982](group__bt__mesh__cfg__cli.md#ga67cf5ff993f2444cc66b2ae5353865d2)int [bt\_mesh\_cfg\_cli\_mod\_app\_get](group__bt__mesh__cfg__cli.md#ga67cf5ff993f2444cc66b2ae5353865d2)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) elem\_addr,

983 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mod\_id, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*status, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*apps, size\_t \*app\_cnt);

984

[ 1006](group__bt__mesh__cfg__cli.md#gaf7e0f85bbbbfc382bfe4aea8298227d1)int [bt\_mesh\_cfg\_cli\_mod\_app\_get\_vnd](group__bt__mesh__cfg__cli.md#gaf7e0f85bbbbfc382bfe4aea8298227d1)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) elem\_addr,

1007 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mod\_id, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) cid, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*status, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*apps,

1008 size\_t \*app\_cnt);

1009

[ 1025](group__bt__mesh__cfg__cli.md#ga1b36596a20ca8751006b0f7f2221067d)int [bt\_mesh\_cfg\_cli\_mod\_pub\_get](group__bt__mesh__cfg__cli.md#ga1b36596a20ca8751006b0f7f2221067d)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) elem\_addr,

1026 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mod\_id, struct [bt\_mesh\_cfg\_cli\_mod\_pub](structbt__mesh__cfg__cli__mod__pub.md) \*pub,

1027 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*status);

1028

[ 1045](group__bt__mesh__cfg__cli.md#ga0bc2c24403e0cd79a061ba1244b1a1db)int [bt\_mesh\_cfg\_cli\_mod\_pub\_get\_vnd](group__bt__mesh__cfg__cli.md#ga0bc2c24403e0cd79a061ba1244b1a1db)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) elem\_addr,

1046 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mod\_id, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) cid,

1047 struct [bt\_mesh\_cfg\_cli\_mod\_pub](structbt__mesh__cfg__cli__mod__pub.md) \*pub, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*status);

1048

[ 1066](group__bt__mesh__cfg__cli.md#ga7fc2acda16f3f03a929c38796c67028e)int [bt\_mesh\_cfg\_cli\_mod\_pub\_set](group__bt__mesh__cfg__cli.md#ga7fc2acda16f3f03a929c38796c67028e)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) elem\_addr,

1067 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mod\_id, struct [bt\_mesh\_cfg\_cli\_mod\_pub](structbt__mesh__cfg__cli__mod__pub.md) \*pub,

1068 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*status);

1069

[ 1088](group__bt__mesh__cfg__cli.md#gad2c602a2685ff38c0e78c1990b244e54)int [bt\_mesh\_cfg\_cli\_mod\_pub\_set\_vnd](group__bt__mesh__cfg__cli.md#gad2c602a2685ff38c0e78c1990b244e54)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) elem\_addr,

1089 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mod\_id, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) cid,

1090 struct [bt\_mesh\_cfg\_cli\_mod\_pub](structbt__mesh__cfg__cli__mod__pub.md) \*pub, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*status);

1091

[ 1107](group__bt__mesh__cfg__cli.md#gaf4ee720ce27eea9602b59a380278bb57)int [bt\_mesh\_cfg\_cli\_mod\_sub\_add](group__bt__mesh__cfg__cli.md#gaf4ee720ce27eea9602b59a380278bb57)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) elem\_addr,

1108 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) sub\_addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mod\_id, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*status);

1109

[ 1126](group__bt__mesh__cfg__cli.md#ga3ba34f8be138bc62a7eb7859b18dc441)int [bt\_mesh\_cfg\_cli\_mod\_sub\_add\_vnd](group__bt__mesh__cfg__cli.md#ga3ba34f8be138bc62a7eb7859b18dc441)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) elem\_addr,

1127 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) sub\_addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mod\_id, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) cid,

1128 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*status);

1129

[ 1145](group__bt__mesh__cfg__cli.md#ga8d8595f077267b7d784fde30cbc4b207)int [bt\_mesh\_cfg\_cli\_mod\_sub\_del](group__bt__mesh__cfg__cli.md#ga8d8595f077267b7d784fde30cbc4b207)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) elem\_addr,

1146 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) sub\_addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mod\_id, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*status);

1147

[ 1164](group__bt__mesh__cfg__cli.md#ga74bad73184af2d6ce71134831f70680d)int [bt\_mesh\_cfg\_cli\_mod\_sub\_del\_vnd](group__bt__mesh__cfg__cli.md#ga74bad73184af2d6ce71134831f70680d)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) elem\_addr,

1165 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) sub\_addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mod\_id, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) cid,

1166 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*status);

1167

[ 1187](group__bt__mesh__cfg__cli.md#gadac1cc360c30d290a861bbd534fca58d)int [bt\_mesh\_cfg\_cli\_mod\_sub\_overwrite](group__bt__mesh__cfg__cli.md#gadac1cc360c30d290a861bbd534fca58d)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) elem\_addr,

1188 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) sub\_addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mod\_id, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*status);

1189

[ 1210](group__bt__mesh__cfg__cli.md#ga69b2dfacc27ed94b9e1331ff4ac4b582)int [bt\_mesh\_cfg\_cli\_mod\_sub\_overwrite\_vnd](group__bt__mesh__cfg__cli.md#ga69b2dfacc27ed94b9e1331ff4ac4b582)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) elem\_addr,

1211 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) sub\_addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mod\_id, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) cid,

1212 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*status);

1213

[ 1230](group__bt__mesh__cfg__cli.md#ga2d22612cf9dc5030699bf7c6c58bf6d5)int [bt\_mesh\_cfg\_cli\_mod\_sub\_va\_add](group__bt__mesh__cfg__cli.md#ga2d22612cf9dc5030699bf7c6c58bf6d5)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) elem\_addr,

1231 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) label[16], [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mod\_id, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*virt\_addr,

1232 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*status);

1233

[ 1251](group__bt__mesh__cfg__cli.md#gaa3a10a54a18a99d0b4b0aa85330b1640)int [bt\_mesh\_cfg\_cli\_mod\_sub\_va\_add\_vnd](group__bt__mesh__cfg__cli.md#gaa3a10a54a18a99d0b4b0aa85330b1640)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) elem\_addr,

1252 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) label[16], [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mod\_id, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) cid,

1253 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*virt\_addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*status);

1254

[ 1271](group__bt__mesh__cfg__cli.md#gaf7107373fc0c70d091e9a521d8b641ad)int [bt\_mesh\_cfg\_cli\_mod\_sub\_va\_del](group__bt__mesh__cfg__cli.md#gaf7107373fc0c70d091e9a521d8b641ad)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) elem\_addr,

1272 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) label[16], [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mod\_id, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*virt\_addr,

1273 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*status);

1274

[ 1292](group__bt__mesh__cfg__cli.md#ga8884786e3ec349bcb8b89b60aa11f198)int [bt\_mesh\_cfg\_cli\_mod\_sub\_va\_del\_vnd](group__bt__mesh__cfg__cli.md#ga8884786e3ec349bcb8b89b60aa11f198)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) elem\_addr,

1293 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) label[16], [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mod\_id, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) cid,

1294 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*virt\_addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*status);

1295

[ 1316](group__bt__mesh__cfg__cli.md#ga69809ad3f2cff8e1f394f6da6ed63264)int [bt\_mesh\_cfg\_cli\_mod\_sub\_va\_overwrite](group__bt__mesh__cfg__cli.md#ga69809ad3f2cff8e1f394f6da6ed63264)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) elem\_addr,

1317 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) label[16], [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mod\_id,

1318 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*virt\_addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*status);

1319

[ 1341](group__bt__mesh__cfg__cli.md#ga70d3bb7fb914fa3685f4ad9b561a48b6)int [bt\_mesh\_cfg\_cli\_mod\_sub\_va\_overwrite\_vnd](group__bt__mesh__cfg__cli.md#ga70d3bb7fb914fa3685f4ad9b561a48b6)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) elem\_addr,

1342 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) label[16], [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mod\_id, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) cid,

1343 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*virt\_addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*status);

1344

[ 1364](group__bt__mesh__cfg__cli.md#gaf739e5e3a4b225e10bf2aedf143d7793)int [bt\_mesh\_cfg\_cli\_mod\_sub\_get](group__bt__mesh__cfg__cli.md#gaf739e5e3a4b225e10bf2aedf143d7793)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) elem\_addr,

1365 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mod\_id, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*status, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*subs, size\_t \*sub\_cnt);

1366

[ 1387](group__bt__mesh__cfg__cli.md#ga09e751a9071402ae978c0355edfbdf03)int [bt\_mesh\_cfg\_cli\_mod\_sub\_get\_vnd](group__bt__mesh__cfg__cli.md#ga09e751a9071402ae978c0355edfbdf03)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) elem\_addr,

1388 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mod\_id, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) cid, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*status, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*subs,

1389 size\_t \*sub\_cnt);

1390

[ 1406](group__bt__mesh__cfg__cli.md#ga1adae658bf8f4512a7d80d0194dcb362)int [bt\_mesh\_cfg\_cli\_hb\_sub\_set](group__bt__mesh__cfg__cli.md#ga1adae658bf8f4512a7d80d0194dcb362)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, struct [bt\_mesh\_cfg\_cli\_hb\_sub](structbt__mesh__cfg__cli__hb__sub.md) \*sub,

1407 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*status);

1408

[ 1422](group__bt__mesh__cfg__cli.md#ga86e5de1b216d62b7c77bf43b7af062fc)int [bt\_mesh\_cfg\_cli\_hb\_sub\_get](group__bt__mesh__cfg__cli.md#ga86e5de1b216d62b7c77bf43b7af062fc)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, struct [bt\_mesh\_cfg\_cli\_hb\_sub](structbt__mesh__cfg__cli__hb__sub.md) \*sub,

1423 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*status);

1424

[ 1442](group__bt__mesh__cfg__cli.md#ga352eb00b78ff978a1a1e81ec5a0575b8)int [bt\_mesh\_cfg\_cli\_hb\_pub\_set](group__bt__mesh__cfg__cli.md#ga352eb00b78ff978a1a1e81ec5a0575b8)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr,

1443 const struct [bt\_mesh\_cfg\_cli\_hb\_pub](structbt__mesh__cfg__cli__hb__pub.md) \*pub, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*status);

1444

[ 1458](group__bt__mesh__cfg__cli.md#ga07c443476adef9c7bb573ffbb8d1b1ce)int [bt\_mesh\_cfg\_cli\_hb\_pub\_get](group__bt__mesh__cfg__cli.md#ga07c443476adef9c7bb573ffbb8d1b1ce)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, struct [bt\_mesh\_cfg\_cli\_hb\_pub](structbt__mesh__cfg__cli__hb__pub.md) \*pub,

1459 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*status);

1460

[ 1475](group__bt__mesh__cfg__cli.md#gacd647905484fa8319a5377aa5777c254)int [bt\_mesh\_cfg\_cli\_mod\_sub\_del\_all](group__bt__mesh__cfg__cli.md#gacd647905484fa8319a5377aa5777c254)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) elem\_addr,

1476 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mod\_id, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*status);

1477

[ 1493](group__bt__mesh__cfg__cli.md#ga2059ccbc689af9c2127e4e399ea5bd43)int [bt\_mesh\_cfg\_cli\_mod\_sub\_del\_all\_vnd](group__bt__mesh__cfg__cli.md#ga2059ccbc689af9c2127e4e399ea5bd43)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) elem\_addr,

1494 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mod\_id, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) cid, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*status);

1495

[ 1510](group__bt__mesh__cfg__cli.md#gafdaff279685b821a7b205e45feed9a05)int [bt\_mesh\_cfg\_cli\_net\_key\_update](group__bt__mesh__cfg__cli.md#gafdaff279685b821a7b205e45feed9a05)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) key\_net\_idx,

1511 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_key[16], [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*status);

1512

[ 1528](group__bt__mesh__cfg__cli.md#gacf1bd7a771a45981a82eeea0dcce01b7)int [bt\_mesh\_cfg\_cli\_app\_key\_update](group__bt__mesh__cfg__cli.md#gacf1bd7a771a45981a82eeea0dcce01b7)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) key\_net\_idx,

1529 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) key\_app\_idx, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) app\_key[16],

1530 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*status);

1531

[ 1549](group__bt__mesh__cfg__cli.md#ga12a8618d2b73f30742f8e8d2bdddc138)int [bt\_mesh\_cfg\_cli\_node\_identity\_set](group__bt__mesh__cfg__cli.md#ga12a8618d2b73f30742f8e8d2bdddc138)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) key\_net\_idx,

1550 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) new\_identity, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*status, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*identity);

1551

[ 1568](group__bt__mesh__cfg__cli.md#gac02c170e260980d5b749b581910672d2)int [bt\_mesh\_cfg\_cli\_node\_identity\_get](group__bt__mesh__cfg__cli.md#gac02c170e260980d5b749b581910672d2)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) key\_net\_idx,

1569 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*status, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*identity);

1570

[ 1584](group__bt__mesh__cfg__cli.md#ga0ee1d0849d632b5d806ee31c87bbc888)int [bt\_mesh\_cfg\_cli\_lpn\_timeout\_get](group__bt__mesh__cfg__cli.md#ga0ee1d0849d632b5d806ee31c87bbc888)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) unicast\_addr,

1585 [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) \*polltimeout);

1586

[ 1591](group__bt__mesh__cfg__cli.md#gaf5262c0a27e4b9249ecf908c259cc7d7)[int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) [bt\_mesh\_cfg\_cli\_timeout\_get](group__bt__mesh__cfg__cli.md#gaf5262c0a27e4b9249ecf908c259cc7d7)(void);

1592

[ 1597](group__bt__mesh__cfg__cli.md#ga7e3521ae973dc825422c6dd5f07ef547)void [bt\_mesh\_cfg\_cli\_timeout\_set](group__bt__mesh__cfg__cli.md#ga7e3521ae973dc825422c6dd5f07ef547)([int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) timeout);

1598

[ 1605](structbt__mesh__comp__p0.md)struct [bt\_mesh\_comp\_p0](structbt__mesh__comp__p0.md) {

[ 1607](structbt__mesh__comp__p0.md#a3ed8f5ac643443bbcca308baff1c539c) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [cid](structbt__mesh__comp__p0.md#a3ed8f5ac643443bbcca308baff1c539c);

[ 1609](structbt__mesh__comp__p0.md#a009806e046583c99f56d271ecebbb8a3) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [pid](structbt__mesh__comp__p0.md#a009806e046583c99f56d271ecebbb8a3);

[ 1611](structbt__mesh__comp__p0.md#a27d910cdeb7b6b9d038898e3824dfb57) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [vid](structbt__mesh__comp__p0.md#a27d910cdeb7b6b9d038898e3824dfb57);

[ 1613](structbt__mesh__comp__p0.md#a32bfead26f338aba892a5459615a65a2) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [crpl](structbt__mesh__comp__p0.md#a32bfead26f338aba892a5459615a65a2);

[ 1615](structbt__mesh__comp__p0.md#a0a44e3778f9d134a5c056ca184c3b527) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [feat](structbt__mesh__comp__p0.md#a0a44e3778f9d134a5c056ca184c3b527);

1616

1617 struct [net\_buf\_simple](structnet__buf__simple.md) \*\_buf;

1618};

1619

[ 1621](structbt__mesh__comp__p0__elem.md)struct [bt\_mesh\_comp\_p0\_elem](structbt__mesh__comp__p0__elem.md) {

[ 1623](structbt__mesh__comp__p0__elem.md#a832cdb0a10d364a048971f59f51e841d) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [loc](structbt__mesh__comp__p0__elem.md#a832cdb0a10d364a048971f59f51e841d);

[ 1625](structbt__mesh__comp__p0__elem.md#a17f61eab2df28f2031f2fbab28254484) size\_t [nsig](structbt__mesh__comp__p0__elem.md#a17f61eab2df28f2031f2fbab28254484);

[ 1627](structbt__mesh__comp__p0__elem.md#a2e1bd3146ebc934e9fab0242a06d5b99) size\_t [nvnd](structbt__mesh__comp__p0__elem.md#a2e1bd3146ebc934e9fab0242a06d5b99);

1628

1629 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\_buf;

1630};

1631

[ 1655](group__bt__mesh__cfg__cli.md#ga1f79d98273a984f1c49b4d5dd5bf8d30)int [bt\_mesh\_comp\_p0\_get](group__bt__mesh__cfg__cli.md#ga1f79d98273a984f1c49b4d5dd5bf8d30)(struct [bt\_mesh\_comp\_p0](structbt__mesh__comp__p0.md) \*comp,

1656 struct [net\_buf\_simple](structnet__buf__simple.md) \*buf);

1657

[ 1670](group__bt__mesh__cfg__cli.md#gaa6d60ebad6dc4a4f5b022937dbae3120)struct [bt\_mesh\_comp\_p0\_elem](structbt__mesh__comp__p0__elem.md) \*[bt\_mesh\_comp\_p0\_elem\_pull](group__bt__mesh__cfg__cli.md#gaa6d60ebad6dc4a4f5b022937dbae3120)(const struct [bt\_mesh\_comp\_p0](structbt__mesh__comp__p0.md) \*comp,

1671 struct [bt\_mesh\_comp\_p0\_elem](structbt__mesh__comp__p0__elem.md) \*elem);

1672

[ 1681](group__bt__mesh__cfg__cli.md#gac005f52e191c3e5628f063dbc1a19645)[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [bt\_mesh\_comp\_p0\_elem\_mod](group__bt__mesh__cfg__cli.md#gac005f52e191c3e5628f063dbc1a19645)(struct [bt\_mesh\_comp\_p0\_elem](structbt__mesh__comp__p0__elem.md) \*elem, int idx);

1682

[ 1691](group__bt__mesh__cfg__cli.md#ga4f656102982961b7bf2e3d3896a2240e)struct [bt\_mesh\_mod\_id\_vnd](structbt__mesh__mod__id__vnd.md) [bt\_mesh\_comp\_p0\_elem\_mod\_vnd](group__bt__mesh__cfg__cli.md#ga4f656102982961b7bf2e3d3896a2240e)(struct [bt\_mesh\_comp\_p0\_elem](structbt__mesh__comp__p0__elem.md) \*elem, int idx);

1692

[ 1694](structbt__mesh__comp__p1__elem.md)struct [bt\_mesh\_comp\_p1\_elem](structbt__mesh__comp__p1__elem.md) {

[ 1696](structbt__mesh__comp__p1__elem.md#aa6aa100992502cef0484a127224cf07b) size\_t [nsig](structbt__mesh__comp__p1__elem.md#aa6aa100992502cef0484a127224cf07b);

[ 1698](structbt__mesh__comp__p1__elem.md#a25492ac30a362e4490d11169ed98197b) size\_t [nvnd](structbt__mesh__comp__p1__elem.md#a25492ac30a362e4490d11169ed98197b);

1700 struct [net\_buf\_simple](structnet__buf__simple.md) \*\_buf;

1701};

1702

[ 1704](structbt__mesh__comp__p1__model__item.md)struct [bt\_mesh\_comp\_p1\_model\_item](structbt__mesh__comp__p1__model__item.md) {

[ 1706](structbt__mesh__comp__p1__model__item.md#aee352e8563133dddbb37c1f31dfe7c09) bool [cor\_present](structbt__mesh__comp__p1__model__item.md#aee352e8563133dddbb37c1f31dfe7c09);

[ 1708](structbt__mesh__comp__p1__model__item.md#af2f213813440cb4a87884e3625a704e7) bool [format](structbt__mesh__comp__p1__model__item.md#af2f213813440cb4a87884e3625a704e7);

[ 1710](structbt__mesh__comp__p1__model__item.md#ae019a211eafeb20f323ad97328d938f7) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [ext\_item\_cnt](structbt__mesh__comp__p1__model__item.md#ae019a211eafeb20f323ad97328d938f7) : 6;

[ 1715](structbt__mesh__comp__p1__model__item.md#a95baa1acf3a82e8559ce4a47b7e03be8) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cor\_id](structbt__mesh__comp__p1__model__item.md#a95baa1acf3a82e8559ce4a47b7e03be8);

1716 struct [net\_buf\_simple](structnet__buf__simple.md) \*\_buf;

1717};

1718

[ 1720](structbt__mesh__comp__p1__item__short.md)struct [bt\_mesh\_comp\_p1\_item\_short](structbt__mesh__comp__p1__item__short.md) {

[ 1722](structbt__mesh__comp__p1__item__short.md#a1fb6c8134a2c02e3b83dfea12ab39410) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [elem\_offset](structbt__mesh__comp__p1__item__short.md#a1fb6c8134a2c02e3b83dfea12ab39410) : 3;

[ 1724](structbt__mesh__comp__p1__item__short.md#a7e2152fe608c52cbc0700a43a5653132) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [mod\_item\_idx](structbt__mesh__comp__p1__item__short.md#a7e2152fe608c52cbc0700a43a5653132) : 5;

1725};

1726

[ 1728](structbt__mesh__comp__p1__item__long.md)struct [bt\_mesh\_comp\_p1\_item\_long](structbt__mesh__comp__p1__item__long.md) {

[ 1730](structbt__mesh__comp__p1__item__long.md#a12a0e2fb373e2e43b7c04a1130cdf018) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [elem\_offset](structbt__mesh__comp__p1__item__long.md#a12a0e2fb373e2e43b7c04a1130cdf018);

[ 1732](structbt__mesh__comp__p1__item__long.md#a61d541854c2d1671c60fc444978f0374) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [mod\_item\_idx](structbt__mesh__comp__p1__item__long.md#a61d541854c2d1671c60fc444978f0374);

1733};

1734

[ 1736](structbt__mesh__comp__p1__ext__item.md)struct [bt\_mesh\_comp\_p1\_ext\_item](structbt__mesh__comp__p1__ext__item.md) {

[ 1737](structbt__mesh__comp__p1__ext__item.md#a05a526a8448e7b8a4766eb038e4c1a39ae96bb3e960c4d2c356c0070f34740119) enum { [SHORT](structbt__mesh__comp__p1__ext__item.md#a05a526a8448e7b8a4766eb038e4c1a39a23a15546d8722d7a4706ea34c5785658), [LONG](structbt__mesh__comp__p1__ext__item.md#a05a526a8448e7b8a4766eb038e4c1a39ae96bb3e960c4d2c356c0070f34740119) } [type](structbt__mesh__comp__p1__ext__item.md#a43f50f35690e54d3680a6daa989ce1c0);

1738

1739 union {

[ 1741](structbt__mesh__comp__p1__ext__item.md#ae17176001203ee8c282f06e994cee647) struct [bt\_mesh\_comp\_p1\_item\_short](structbt__mesh__comp__p1__item__short.md) [short\_item](structbt__mesh__comp__p1__ext__item.md#ae17176001203ee8c282f06e994cee647);

[ 1743](structbt__mesh__comp__p1__ext__item.md#a3962046fc095348035a193dad60d1149) struct [bt\_mesh\_comp\_p1\_item\_long](structbt__mesh__comp__p1__item__long.md) [long\_item](structbt__mesh__comp__p1__ext__item.md#a3962046fc095348035a193dad60d1149);

1744 };

1745};

1746

[ 1759](group__bt__mesh__cfg__cli.md#gae9a19b089d898af914ea5c287aca8fba)struct [bt\_mesh\_comp\_p1\_elem](structbt__mesh__comp__p1__elem.md) \*[bt\_mesh\_comp\_p1\_elem\_pull](group__bt__mesh__cfg__cli.md#gae9a19b089d898af914ea5c287aca8fba)(

1760 struct [net\_buf\_simple](structnet__buf__simple.md) \*buf, struct [bt\_mesh\_comp\_p1\_elem](structbt__mesh__comp__p1__elem.md) \*elem);

1761

[ 1774](group__bt__mesh__cfg__cli.md#gac8b4b670c82b80a51834f7ef32206985)struct [bt\_mesh\_comp\_p1\_model\_item](structbt__mesh__comp__p1__model__item.md) \*[bt\_mesh\_comp\_p1\_item\_pull](group__bt__mesh__cfg__cli.md#gac8b4b670c82b80a51834f7ef32206985)(

1775 struct [bt\_mesh\_comp\_p1\_elem](structbt__mesh__comp__p1__elem.md) \*elem, struct [bt\_mesh\_comp\_p1\_model\_item](structbt__mesh__comp__p1__model__item.md) \*item);

1776

[ 1787](group__bt__mesh__cfg__cli.md#gac527fe27308c8a61ac1831af9605e429)struct [bt\_mesh\_comp\_p1\_ext\_item](structbt__mesh__comp__p1__ext__item.md) \*[bt\_mesh\_comp\_p1\_pull\_ext\_item](group__bt__mesh__cfg__cli.md#gac527fe27308c8a61ac1831af9605e429)(

1788 struct [bt\_mesh\_comp\_p1\_model\_item](structbt__mesh__comp__p1__model__item.md) \*item, struct [bt\_mesh\_comp\_p1\_ext\_item](structbt__mesh__comp__p1__ext__item.md) \*ext\_item);

1789

[ 1791](structbt__mesh__comp__p2__record.md)struct [bt\_mesh\_comp\_p2\_record](structbt__mesh__comp__p2__record.md) {

[ 1793](structbt__mesh__comp__p2__record.md#a4d947193b1a0f46c9df1eca298135646) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [id](structbt__mesh__comp__p2__record.md#a4d947193b1a0f46c9df1eca298135646);

1795 struct {

[ 1797](structbt__mesh__comp__p2__record.md#a5377ce835db8ce408d8dabfd87c858f5) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [x](structbt__mesh__comp__p2__record.md#a5377ce835db8ce408d8dabfd87c858f5);

[ 1799](structbt__mesh__comp__p2__record.md#a0ceff9becd0eb14ca190c49f56ec0957) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [y](structbt__mesh__comp__p2__record.md#a0ceff9becd0eb14ca190c49f56ec0957);

[ 1801](structbt__mesh__comp__p2__record.md#a90e80906ef6d2b8b932215ad183db2d5) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [z](structbt__mesh__comp__p2__record.md#a90e80906ef6d2b8b932215ad183db2d5);

[ 1802](structbt__mesh__comp__p2__record.md#aa718c024d6ce339ac8c352319b878c53) } [version](structbt__mesh__comp__p2__record.md#aa718c024d6ce339ac8c352319b878c53);

[ 1804](structbt__mesh__comp__p2__record.md#ad310f8c8e3a167492a6e698336b7f400) struct [net\_buf\_simple](structnet__buf__simple.md) \*[elem\_buf](structbt__mesh__comp__p2__record.md#ad310f8c8e3a167492a6e698336b7f400);

[ 1806](structbt__mesh__comp__p2__record.md#abd0975a47c848265ad13044dfcd3b78d) struct [net\_buf\_simple](structnet__buf__simple.md) \*[data\_buf](structbt__mesh__comp__p2__record.md#abd0975a47c848265ad13044dfcd3b78d);

1807};

1808

[ 1821](group__bt__mesh__cfg__cli.md#ga0854a494707a40b84beb8582f45e0470)struct [bt\_mesh\_comp\_p2\_record](structbt__mesh__comp__p2__record.md) \*[bt\_mesh\_comp\_p2\_record\_pull](group__bt__mesh__cfg__cli.md#ga0854a494707a40b84beb8582f45e0470)(struct [net\_buf\_simple](structnet__buf__simple.md) \*buf,

1822 struct [bt\_mesh\_comp\_p2\_record](structbt__mesh__comp__p2__record.md) \*record);

1823

[ 1835](group__bt__mesh__cfg__cli.md#gaa411ab7db2e71a114a8108eaec9ca12c)int [bt\_mesh\_key\_idx\_unpack\_list](group__bt__mesh__cfg__cli.md#gaa411ab7db2e71a114a8108eaec9ca12c)(struct [net\_buf\_simple](structnet__buf__simple.md) \*buf, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*dst\_arr, size\_t \*dst\_cnt);

1836

1838extern const struct [bt\_mesh\_model\_op](structbt__mesh__model__op.md) bt\_mesh\_cfg\_cli\_op[];

1839extern const struct [bt\_mesh\_model\_cb](structbt__mesh__model__cb.md) [bt\_mesh\_cfg\_cli\_cb](structbt__mesh__cfg__cli__cb.md);

1841

1842#ifdef \_\_cplusplus

1843}

1844#endif

1848

1849#endif /\* ZEPHYR\_INCLUDE\_BLUETOOTH\_MESH\_CFG\_CLI\_H\_ \*/

[bt\_mesh\_cfg\_cli\_hb\_pub\_get](group__bt__mesh__cfg__cli.md#ga07c443476adef9c7bb573ffbb8d1b1ce)

int bt\_mesh\_cfg\_cli\_hb\_pub\_get(uint16\_t net\_idx, uint16\_t addr, struct bt\_mesh\_cfg\_cli\_hb\_pub \*pub, uint8\_t \*status)

Get the target node's Heartbeat publication parameters.

[bt\_mesh\_comp\_p2\_record\_pull](group__bt__mesh__cfg__cli.md#ga0854a494707a40b84beb8582f45e0470)

struct bt\_mesh\_comp\_p2\_record \* bt\_mesh\_comp\_p2\_record\_pull(struct net\_buf\_simple \*buf, struct bt\_mesh\_comp\_p2\_record \*record)

Pull a Composition Data Page 2 Record from a composition data page 2 instance.

[bt\_mesh\_cfg\_cli\_mod\_sub\_get\_vnd](group__bt__mesh__cfg__cli.md#ga09e751a9071402ae978c0355edfbdf03)

int bt\_mesh\_cfg\_cli\_mod\_sub\_get\_vnd(uint16\_t net\_idx, uint16\_t addr, uint16\_t elem\_addr, uint16\_t mod\_id, uint16\_t cid, uint8\_t \*status, uint16\_t \*subs, size\_t \*sub\_cnt)

Get the subscription list of a vendor model on the target node.

[bt\_mesh\_cfg\_cli\_mod\_pub\_get\_vnd](group__bt__mesh__cfg__cli.md#ga0bc2c24403e0cd79a061ba1244b1a1db)

int bt\_mesh\_cfg\_cli\_mod\_pub\_get\_vnd(uint16\_t net\_idx, uint16\_t addr, uint16\_t elem\_addr, uint16\_t mod\_id, uint16\_t cid, struct bt\_mesh\_cfg\_cli\_mod\_pub \*pub, uint8\_t \*status)

Get publish parameters for a vendor model on the target node.

[bt\_mesh\_cfg\_cli\_lpn\_timeout\_get](group__bt__mesh__cfg__cli.md#ga0ee1d0849d632b5d806ee31c87bbc888)

int bt\_mesh\_cfg\_cli\_lpn\_timeout\_get(uint16\_t net\_idx, uint16\_t addr, uint16\_t unicast\_addr, int32\_t \*polltimeout)

Get the Low Power Node Polltimeout parameters.

[bt\_mesh\_cfg\_cli\_node\_identity\_set](group__bt__mesh__cfg__cli.md#ga12a8618d2b73f30742f8e8d2bdddc138)

int bt\_mesh\_cfg\_cli\_node\_identity\_set(uint16\_t net\_idx, uint16\_t addr, uint16\_t key\_net\_idx, uint8\_t new\_identity, uint8\_t \*status, uint8\_t \*identity)

Set the Node Identity parameters.

[bt\_mesh\_cfg\_cli\_hb\_sub\_set](group__bt__mesh__cfg__cli.md#ga1adae658bf8f4512a7d80d0194dcb362)

int bt\_mesh\_cfg\_cli\_hb\_sub\_set(uint16\_t net\_idx, uint16\_t addr, struct bt\_mesh\_cfg\_cli\_hb\_sub \*sub, uint8\_t \*status)

Set the target node's Heartbeat subscription parameters.

[bt\_mesh\_cfg\_cli\_mod\_pub\_get](group__bt__mesh__cfg__cli.md#ga1b36596a20ca8751006b0f7f2221067d)

int bt\_mesh\_cfg\_cli\_mod\_pub\_get(uint16\_t net\_idx, uint16\_t addr, uint16\_t elem\_addr, uint16\_t mod\_id, struct bt\_mesh\_cfg\_cli\_mod\_pub \*pub, uint8\_t \*status)

Get publish parameters for a SIG model on the target node.

[bt\_mesh\_comp\_p0\_get](group__bt__mesh__cfg__cli.md#ga1f79d98273a984f1c49b4d5dd5bf8d30)

int bt\_mesh\_comp\_p0\_get(struct bt\_mesh\_comp\_p0 \*comp, struct net\_buf\_simple \*buf)

Create a composition data page 0 representation from a buffer.

[bt\_mesh\_cfg\_cli\_mod\_app\_unbind\_vnd](group__bt__mesh__cfg__cli.md#ga1fb53b9a49be25e633cac9d668c5b209)

int bt\_mesh\_cfg\_cli\_mod\_app\_unbind\_vnd(uint16\_t net\_idx, uint16\_t addr, uint16\_t elem\_addr, uint16\_t mod\_app\_idx, uint16\_t mod\_id, uint16\_t cid, uint8\_t \*status)

Unbind an application from a vendor model on the target node.

[bt\_mesh\_cfg\_cli\_mod\_sub\_del\_all\_vnd](group__bt__mesh__cfg__cli.md#ga2059ccbc689af9c2127e4e399ea5bd43)

int bt\_mesh\_cfg\_cli\_mod\_sub\_del\_all\_vnd(uint16\_t net\_idx, uint16\_t addr, uint16\_t elem\_addr, uint16\_t mod\_id, uint16\_t cid, uint8\_t \*status)

Delete all group addresses in a vendor model's subscription list.

[bt\_mesh\_cfg\_cli\_ttl\_set](group__bt__mesh__cfg__cli.md#ga2671234d739c802fd080a19d01235352)

int bt\_mesh\_cfg\_cli\_ttl\_set(uint16\_t net\_idx, uint16\_t addr, uint8\_t val, uint8\_t \*ttl)

Set the target node's Time To Live value.

[bt\_mesh\_cfg\_cli\_net\_key\_add](group__bt__mesh__cfg__cli.md#ga283fb06ddb6427852ff0ac556d3c1852)

int bt\_mesh\_cfg\_cli\_net\_key\_add(uint16\_t net\_idx, uint16\_t addr, uint16\_t key\_net\_idx, const uint8\_t net\_key[16], uint8\_t \*status)

Add a network key to the target node.

[bt\_mesh\_cfg\_cli\_beacon\_get](group__bt__mesh__cfg__cli.md#ga2c8a79d1b70e91e0a09c848737bb4a22)

int bt\_mesh\_cfg\_cli\_beacon\_get(uint16\_t net\_idx, uint16\_t addr, uint8\_t \*status)

Get the target node's network beacon state.

[bt\_mesh\_cfg\_cli\_mod\_sub\_va\_add](group__bt__mesh__cfg__cli.md#ga2d22612cf9dc5030699bf7c6c58bf6d5)

int bt\_mesh\_cfg\_cli\_mod\_sub\_va\_add(uint16\_t net\_idx, uint16\_t addr, uint16\_t elem\_addr, const uint8\_t label[16], uint16\_t mod\_id, uint16\_t \*virt\_addr, uint8\_t \*status)

Add a virtual address to a SIG model's subscription list.

[bt\_mesh\_cfg\_cli\_hb\_pub\_set](group__bt__mesh__cfg__cli.md#ga352eb00b78ff978a1a1e81ec5a0575b8)

int bt\_mesh\_cfg\_cli\_hb\_pub\_set(uint16\_t net\_idx, uint16\_t addr, const struct bt\_mesh\_cfg\_cli\_hb\_pub \*pub, uint8\_t \*status)

Set the target node's Heartbeat publication parameters.

[bt\_mesh\_cfg\_cli\_comp\_data\_get](group__bt__mesh__cfg__cli.md#ga36259e9c811a8f1a21d642739cf297df)

int bt\_mesh\_cfg\_cli\_comp\_data\_get(uint16\_t net\_idx, uint16\_t addr, uint8\_t page, uint8\_t \*rsp, struct net\_buf\_simple \*comp)

Get the target node's composition data.

[bt\_mesh\_cfg\_cli\_mod\_sub\_add\_vnd](group__bt__mesh__cfg__cli.md#ga3ba34f8be138bc62a7eb7859b18dc441)

int bt\_mesh\_cfg\_cli\_mod\_sub\_add\_vnd(uint16\_t net\_idx, uint16\_t addr, uint16\_t elem\_addr, uint16\_t sub\_addr, uint16\_t mod\_id, uint16\_t cid, uint8\_t \*status)

Add a group address to a vendor model's subscription list.

[bt\_mesh\_cfg\_cli\_relay\_get](group__bt__mesh__cfg__cli.md#ga4a50a6a5dcfdc42b7476f0b9e463ea45)

int bt\_mesh\_cfg\_cli\_relay\_get(uint16\_t net\_idx, uint16\_t addr, uint8\_t \*status, uint8\_t \*transmit)

Get the target node's Relay feature state.

[bt\_mesh\_cfg\_cli\_friend\_get](group__bt__mesh__cfg__cli.md#ga4dd1534e9d5b04fc99231ba5dde23e05)

int bt\_mesh\_cfg\_cli\_friend\_get(uint16\_t net\_idx, uint16\_t addr, uint8\_t \*status)

Get the target node's Friend feature status.

[bt\_mesh\_comp\_p0\_elem\_mod\_vnd](group__bt__mesh__cfg__cli.md#ga4f656102982961b7bf2e3d3896a2240e)

struct bt\_mesh\_mod\_id\_vnd bt\_mesh\_comp\_p0\_elem\_mod\_vnd(struct bt\_mesh\_comp\_p0\_elem \*elem, int idx)

Get a vendor model from the given composition data page 0 element.

[bt\_mesh\_cfg\_cli\_app\_key\_del](group__bt__mesh__cfg__cli.md#ga5140472c687584babf885bc08349c865)

int bt\_mesh\_cfg\_cli\_app\_key\_del(uint16\_t net\_idx, uint16\_t addr, uint16\_t key\_net\_idx, uint16\_t key\_app\_idx, uint8\_t \*status)

Delete an application key from the target node.

[bt\_mesh\_cfg\_cli\_gatt\_proxy\_set](group__bt__mesh__cfg__cli.md#ga5a717835a416ba2930f65a975265649f)

int bt\_mesh\_cfg\_cli\_gatt\_proxy\_set(uint16\_t net\_idx, uint16\_t addr, uint8\_t val, uint8\_t \*status)

Set the target node's Proxy feature state.

[bt\_mesh\_cfg\_cli\_app\_key\_get](group__bt__mesh__cfg__cli.md#ga6391ce297ca0be73ccd51044a9e0a76f)

int bt\_mesh\_cfg\_cli\_app\_key\_get(uint16\_t net\_idx, uint16\_t addr, uint16\_t key\_net\_idx, uint8\_t \*status, uint16\_t \*keys, size\_t \*key\_cnt)

Get a list of the target node's application key indexes for a specific network key.

[bt\_mesh\_cfg\_cli\_krp\_get](group__bt__mesh__cfg__cli.md#ga660df68049110332ff21610fe4e520c6)

int bt\_mesh\_cfg\_cli\_krp\_get(uint16\_t net\_idx, uint16\_t addr, uint16\_t key\_net\_idx, uint8\_t \*status, uint8\_t \*phase)

Get the target node's network key refresh phase state.

[bt\_mesh\_cfg\_cli\_mod\_app\_get](group__bt__mesh__cfg__cli.md#ga67cf5ff993f2444cc66b2ae5353865d2)

int bt\_mesh\_cfg\_cli\_mod\_app\_get(uint16\_t net\_idx, uint16\_t addr, uint16\_t elem\_addr, uint16\_t mod\_id, uint8\_t \*status, uint16\_t \*apps, size\_t \*app\_cnt)

Get a list of all applications bound to a SIG model on the target node.

[bt\_mesh\_cfg\_cli\_mod\_sub\_va\_overwrite](group__bt__mesh__cfg__cli.md#ga69809ad3f2cff8e1f394f6da6ed63264)

int bt\_mesh\_cfg\_cli\_mod\_sub\_va\_overwrite(uint16\_t net\_idx, uint16\_t addr, uint16\_t elem\_addr, const uint8\_t label[16], uint16\_t mod\_id, uint16\_t \*virt\_addr, uint8\_t \*status)

Overwrite all addresses in a SIG model's subscription list with a virtual address.

[bt\_mesh\_cfg\_cli\_mod\_sub\_overwrite\_vnd](group__bt__mesh__cfg__cli.md#ga69b2dfacc27ed94b9e1331ff4ac4b582)

int bt\_mesh\_cfg\_cli\_mod\_sub\_overwrite\_vnd(uint16\_t net\_idx, uint16\_t addr, uint16\_t elem\_addr, uint16\_t sub\_addr, uint16\_t mod\_id, uint16\_t cid, uint8\_t \*status)

Overwrite all addresses in a vendor model's subscription list with a group address.

[bt\_mesh\_cfg\_cli\_mod\_sub\_va\_overwrite\_vnd](group__bt__mesh__cfg__cli.md#ga70d3bb7fb914fa3685f4ad9b561a48b6)

int bt\_mesh\_cfg\_cli\_mod\_sub\_va\_overwrite\_vnd(uint16\_t net\_idx, uint16\_t addr, uint16\_t elem\_addr, const uint8\_t label[16], uint16\_t mod\_id, uint16\_t cid, uint16\_t \*virt\_addr, uint8\_t \*status)

Overwrite all addresses in a vendor model's subscription list with a virtual address.

[bt\_mesh\_cfg\_cli\_mod\_sub\_del\_vnd](group__bt__mesh__cfg__cli.md#ga74bad73184af2d6ce71134831f70680d)

int bt\_mesh\_cfg\_cli\_mod\_sub\_del\_vnd(uint16\_t net\_idx, uint16\_t addr, uint16\_t elem\_addr, uint16\_t sub\_addr, uint16\_t mod\_id, uint16\_t cid, uint8\_t \*status)

Delete a group address in a vendor model's subscription list.

[bt\_mesh\_cfg\_cli\_timeout\_set](group__bt__mesh__cfg__cli.md#ga7e3521ae973dc825422c6dd5f07ef547)

void bt\_mesh\_cfg\_cli\_timeout\_set(int32\_t timeout)

Set the transmission timeout value.

[bt\_mesh\_cfg\_cli\_mod\_pub\_set](group__bt__mesh__cfg__cli.md#ga7fc2acda16f3f03a929c38796c67028e)

int bt\_mesh\_cfg\_cli\_mod\_pub\_set(uint16\_t net\_idx, uint16\_t addr, uint16\_t elem\_addr, uint16\_t mod\_id, struct bt\_mesh\_cfg\_cli\_mod\_pub \*pub, uint8\_t \*status)

Set publish parameters for a SIG model on the target node.

[bt\_mesh\_cfg\_cli\_relay\_set](group__bt__mesh__cfg__cli.md#ga7fe8418130568bdf2a5e56ed2ad027b0)

int bt\_mesh\_cfg\_cli\_relay\_set(uint16\_t net\_idx, uint16\_t addr, uint8\_t new\_relay, uint8\_t new\_transmit, uint8\_t \*status, uint8\_t \*transmit)

Set the target node's Relay parameters.

[bt\_mesh\_cfg\_cli\_hb\_sub\_get](group__bt__mesh__cfg__cli.md#ga86e5de1b216d62b7c77bf43b7af062fc)

int bt\_mesh\_cfg\_cli\_hb\_sub\_get(uint16\_t net\_idx, uint16\_t addr, struct bt\_mesh\_cfg\_cli\_hb\_sub \*sub, uint8\_t \*status)

Get the target node's Heartbeat subscription parameters.

[bt\_mesh\_cfg\_cli\_net\_transmit\_set](group__bt__mesh__cfg__cli.md#ga87f7c1e06b5c721c89031c527960bf40)

int bt\_mesh\_cfg\_cli\_net\_transmit\_set(uint16\_t net\_idx, uint16\_t addr, uint8\_t val, uint8\_t \*transmit)

Set the target node's network transmit parameters.

[bt\_mesh\_cfg\_cli\_mod\_sub\_va\_del\_vnd](group__bt__mesh__cfg__cli.md#ga8884786e3ec349bcb8b89b60aa11f198)

int bt\_mesh\_cfg\_cli\_mod\_sub\_va\_del\_vnd(uint16\_t net\_idx, uint16\_t addr, uint16\_t elem\_addr, const uint8\_t label[16], uint16\_t mod\_id, uint16\_t cid, uint16\_t \*virt\_addr, uint8\_t \*status)

Delete a virtual address in a vendor model's subscription list.

[bt\_mesh\_cfg\_cli\_mod\_sub\_del](group__bt__mesh__cfg__cli.md#ga8d8595f077267b7d784fde30cbc4b207)

int bt\_mesh\_cfg\_cli\_mod\_sub\_del(uint16\_t net\_idx, uint16\_t addr, uint16\_t elem\_addr, uint16\_t sub\_addr, uint16\_t mod\_id, uint8\_t \*status)

Delete a group address in a SIG model's subscription list.

[bt\_mesh\_cfg\_cli\_net\_transmit\_get](group__bt__mesh__cfg__cli.md#ga92ee7984b14590ed11a470c0dfea0bc9)

int bt\_mesh\_cfg\_cli\_net\_transmit\_get(uint16\_t net\_idx, uint16\_t addr, uint8\_t \*transmit)

Get the target node's network\_transmit state.

[bt\_mesh\_cfg\_cli\_ttl\_get](group__bt__mesh__cfg__cli.md#gaa141d4aabbed6c7780ac7f3955c8b580)

int bt\_mesh\_cfg\_cli\_ttl\_get(uint16\_t net\_idx, uint16\_t addr, uint8\_t \*ttl)

Get the target node's Time To Live value.

[bt\_mesh\_cfg\_cli\_mod\_sub\_va\_add\_vnd](group__bt__mesh__cfg__cli.md#gaa3a10a54a18a99d0b4b0aa85330b1640)

int bt\_mesh\_cfg\_cli\_mod\_sub\_va\_add\_vnd(uint16\_t net\_idx, uint16\_t addr, uint16\_t elem\_addr, const uint8\_t label[16], uint16\_t mod\_id, uint16\_t cid, uint16\_t \*virt\_addr, uint8\_t \*status)

Add a virtual address to a vendor model's subscription list.

[bt\_mesh\_key\_idx\_unpack\_list](group__bt__mesh__cfg__cli.md#gaa411ab7db2e71a114a8108eaec9ca12c)

int bt\_mesh\_key\_idx\_unpack\_list(struct net\_buf\_simple \*buf, uint16\_t \*dst\_arr, size\_t \*dst\_cnt)

Unpack a list of key index entries from a buffer.

[bt\_mesh\_cfg\_cli\_mod\_app\_bind](group__bt__mesh__cfg__cli.md#gaa4a02dd0c1f67621ee71d011fe4a29c1)

int bt\_mesh\_cfg\_cli\_mod\_app\_bind(uint16\_t net\_idx, uint16\_t addr, uint16\_t elem\_addr, uint16\_t mod\_app\_idx, uint16\_t mod\_id, uint8\_t \*status)

Bind an application to a SIG model on the target node.

[bt\_mesh\_comp\_p0\_elem\_pull](group__bt__mesh__cfg__cli.md#gaa6d60ebad6dc4a4f5b022937dbae3120)

struct bt\_mesh\_comp\_p0\_elem \* bt\_mesh\_comp\_p0\_elem\_pull(const struct bt\_mesh\_comp\_p0 \*comp, struct bt\_mesh\_comp\_p0\_elem \*elem)

Pull a composition data page 0 element from a composition data page 0 instance.

[bt\_mesh\_cfg\_cli\_gatt\_proxy\_get](group__bt__mesh__cfg__cli.md#gaaf945377cf6a3d2b3e7c7cdb5a8df016)

int bt\_mesh\_cfg\_cli\_gatt\_proxy\_get(uint16\_t net\_idx, uint16\_t addr, uint8\_t \*status)

Get the target node's Proxy feature state.

[bt\_mesh\_cfg\_cli\_net\_key\_del](group__bt__mesh__cfg__cli.md#gab2963ec5536cb4b941578bb490fdc013)

int bt\_mesh\_cfg\_cli\_net\_key\_del(uint16\_t net\_idx, uint16\_t addr, uint16\_t key\_net\_idx, uint8\_t \*status)

Delete a network key from the target node.

[bt\_mesh\_cfg\_cli\_net\_key\_get](group__bt__mesh__cfg__cli.md#gab42c5bdff36bea35e967946462b12457)

int bt\_mesh\_cfg\_cli\_net\_key\_get(uint16\_t net\_idx, uint16\_t addr, uint16\_t \*keys, size\_t \*key\_cnt)

Get a list of the target node's network key indexes.

[bt\_mesh\_cfg\_cli\_beacon\_set](group__bt__mesh__cfg__cli.md#gab513c82ebe434907a958cc6da990bd0b)

int bt\_mesh\_cfg\_cli\_beacon\_set(uint16\_t net\_idx, uint16\_t addr, uint8\_t val, uint8\_t \*status)

Set the target node's network beacon state.

[bt\_mesh\_comp\_p0\_elem\_mod](group__bt__mesh__cfg__cli.md#gac005f52e191c3e5628f063dbc1a19645)

uint16\_t bt\_mesh\_comp\_p0\_elem\_mod(struct bt\_mesh\_comp\_p0\_elem \*elem, int idx)

Get a SIG model from the given composition data page 0 element.

[bt\_mesh\_cfg\_cli\_node\_identity\_get](group__bt__mesh__cfg__cli.md#gac02c170e260980d5b749b581910672d2)

int bt\_mesh\_cfg\_cli\_node\_identity\_get(uint16\_t net\_idx, uint16\_t addr, uint16\_t key\_net\_idx, uint8\_t \*status, uint8\_t \*identity)

Get the Node Identity parameters.

[bt\_mesh\_comp\_p1\_pull\_ext\_item](group__bt__mesh__cfg__cli.md#gac527fe27308c8a61ac1831af9605e429)

struct bt\_mesh\_comp\_p1\_ext\_item \* bt\_mesh\_comp\_p1\_pull\_ext\_item(struct bt\_mesh\_comp\_p1\_model\_item \*item, struct bt\_mesh\_comp\_p1\_ext\_item \*ext\_item)

Pull Extended Model Item contained in Model Item.

[bt\_mesh\_cfg\_cli\_node\_reset](group__bt__mesh__cfg__cli.md#gac6675d227749a69cedc5455c70626b76)

int bt\_mesh\_cfg\_cli\_node\_reset(uint16\_t net\_idx, uint16\_t addr, bool \*status)

Reset the target node and remove it from the network.

[bt\_mesh\_comp\_p1\_item\_pull](group__bt__mesh__cfg__cli.md#gac8b4b670c82b80a51834f7ef32206985)

struct bt\_mesh\_comp\_p1\_model\_item \* bt\_mesh\_comp\_p1\_item\_pull(struct bt\_mesh\_comp\_p1\_elem \*elem, struct bt\_mesh\_comp\_p1\_model\_item \*item)

Pull a Composition Data Page 1 Model Item from a Composition Data Page 1 Element.

[bt\_mesh\_cfg\_cli\_mod\_sub\_del\_all](group__bt__mesh__cfg__cli.md#gacd647905484fa8319a5377aa5777c254)

int bt\_mesh\_cfg\_cli\_mod\_sub\_del\_all(uint16\_t net\_idx, uint16\_t addr, uint16\_t elem\_addr, uint16\_t mod\_id, uint8\_t \*status)

Delete all group addresses in a SIG model's subscription list.

[bt\_mesh\_cfg\_cli\_app\_key\_update](group__bt__mesh__cfg__cli.md#gacf1bd7a771a45981a82eeea0dcce01b7)

int bt\_mesh\_cfg\_cli\_app\_key\_update(uint16\_t net\_idx, uint16\_t addr, uint16\_t key\_net\_idx, uint16\_t key\_app\_idx, const uint8\_t app\_key[16], uint8\_t \*status)

Update an application key to the target node.

[bt\_mesh\_cfg\_cli\_friend\_set](group__bt__mesh__cfg__cli.md#gacf8ad783910449c7cdc304c1b9b3fe0b)

int bt\_mesh\_cfg\_cli\_friend\_set(uint16\_t net\_idx, uint16\_t addr, uint8\_t val, uint8\_t \*status)

Set the target node's Friend feature state.

[bt\_mesh\_cfg\_cli\_mod\_pub\_set\_vnd](group__bt__mesh__cfg__cli.md#gad2c602a2685ff38c0e78c1990b244e54)

int bt\_mesh\_cfg\_cli\_mod\_pub\_set\_vnd(uint16\_t net\_idx, uint16\_t addr, uint16\_t elem\_addr, uint16\_t mod\_id, uint16\_t cid, struct bt\_mesh\_cfg\_cli\_mod\_pub \*pub, uint8\_t \*status)

Set publish parameters for a vendor model on the target node.

[bt\_mesh\_cfg\_cli\_mod\_app\_bind\_vnd](group__bt__mesh__cfg__cli.md#gada33602562721c9f413eb06b34a823a8)

int bt\_mesh\_cfg\_cli\_mod\_app\_bind\_vnd(uint16\_t net\_idx, uint16\_t addr, uint16\_t elem\_addr, uint16\_t mod\_app\_idx, uint16\_t mod\_id, uint16\_t cid, uint8\_t \*status)

Bind an application to a vendor model on the target node.

[bt\_mesh\_cfg\_cli\_mod\_sub\_overwrite](group__bt__mesh__cfg__cli.md#gadac1cc360c30d290a861bbd534fca58d)

int bt\_mesh\_cfg\_cli\_mod\_sub\_overwrite(uint16\_t net\_idx, uint16\_t addr, uint16\_t elem\_addr, uint16\_t sub\_addr, uint16\_t mod\_id, uint8\_t \*status)

Overwrite all addresses in a SIG model's subscription list with a group address.

[bt\_mesh\_cfg\_cli\_krp\_set](group__bt__mesh__cfg__cli.md#gae51eee59090cfebed4561ed3bb4df005)

int bt\_mesh\_cfg\_cli\_krp\_set(uint16\_t net\_idx, uint16\_t addr, uint16\_t key\_net\_idx, uint8\_t transition, uint8\_t \*status, uint8\_t \*phase)

Set the target node's network key refresh phase parameters.

[bt\_mesh\_comp\_p1\_elem\_pull](group__bt__mesh__cfg__cli.md#gae9a19b089d898af914ea5c287aca8fba)

struct bt\_mesh\_comp\_p1\_elem \* bt\_mesh\_comp\_p1\_elem\_pull(struct net\_buf\_simple \*buf, struct bt\_mesh\_comp\_p1\_elem \*elem)

Pull a Composition Data Page 1 Element from a composition data page 1 instance.

[bt\_mesh\_cfg\_cli\_mod\_sub\_add](group__bt__mesh__cfg__cli.md#gaf4ee720ce27eea9602b59a380278bb57)

int bt\_mesh\_cfg\_cli\_mod\_sub\_add(uint16\_t net\_idx, uint16\_t addr, uint16\_t elem\_addr, uint16\_t sub\_addr, uint16\_t mod\_id, uint8\_t \*status)

Add a group address to a SIG model's subscription list.

[bt\_mesh\_cfg\_cli\_timeout\_get](group__bt__mesh__cfg__cli.md#gaf5262c0a27e4b9249ecf908c259cc7d7)

int32\_t bt\_mesh\_cfg\_cli\_timeout\_get(void)

Get the current transmission timeout value.

[bt\_mesh\_cfg\_cli\_mod\_sub\_va\_del](group__bt__mesh__cfg__cli.md#gaf7107373fc0c70d091e9a521d8b641ad)

int bt\_mesh\_cfg\_cli\_mod\_sub\_va\_del(uint16\_t net\_idx, uint16\_t addr, uint16\_t elem\_addr, const uint8\_t label[16], uint16\_t mod\_id, uint16\_t \*virt\_addr, uint8\_t \*status)

Delete a virtual address in a SIG model's subscription list.

[bt\_mesh\_cfg\_cli\_mod\_sub\_get](group__bt__mesh__cfg__cli.md#gaf739e5e3a4b225e10bf2aedf143d7793)

int bt\_mesh\_cfg\_cli\_mod\_sub\_get(uint16\_t net\_idx, uint16\_t addr, uint16\_t elem\_addr, uint16\_t mod\_id, uint8\_t \*status, uint16\_t \*subs, size\_t \*sub\_cnt)

Get the subscription list of a SIG model on the target node.

[bt\_mesh\_cfg\_cli\_mod\_app\_get\_vnd](group__bt__mesh__cfg__cli.md#gaf7e0f85bbbbfc382bfe4aea8298227d1)

int bt\_mesh\_cfg\_cli\_mod\_app\_get\_vnd(uint16\_t net\_idx, uint16\_t addr, uint16\_t elem\_addr, uint16\_t mod\_id, uint16\_t cid, uint8\_t \*status, uint16\_t \*apps, size\_t \*app\_cnt)

Get a list of all applications bound to a vendor model on the target node.

[bt\_mesh\_cfg\_cli\_mod\_app\_unbind](group__bt__mesh__cfg__cli.md#gaf82b54a4b2d3176b10daf728272a0977)

int bt\_mesh\_cfg\_cli\_mod\_app\_unbind(uint16\_t net\_idx, uint16\_t addr, uint16\_t elem\_addr, uint16\_t mod\_app\_idx, uint16\_t mod\_id, uint8\_t \*status)

Unbind an application from a SIG model on the target node.

[bt\_mesh\_cfg\_cli\_app\_key\_add](group__bt__mesh__cfg__cli.md#gafabf4c0fa707eba1fd40cc9a403daa07)

int bt\_mesh\_cfg\_cli\_app\_key\_add(uint16\_t net\_idx, uint16\_t addr, uint16\_t key\_net\_idx, uint16\_t key\_app\_idx, const uint8\_t app\_key[16], uint8\_t \*status)

Add an application key to the target node.

[bt\_mesh\_cfg\_cli\_net\_key\_update](group__bt__mesh__cfg__cli.md#gafdaff279685b821a7b205e45feed9a05)

int bt\_mesh\_cfg\_cli\_net\_key\_update(uint16\_t net\_idx, uint16\_t addr, uint16\_t key\_net\_idx, const uint8\_t net\_key[16], uint8\_t \*status)

Update a network key to the target node.

[stdbool.h](stdbool_8h.md)

[stdint.h](stdint_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2)

\_\_INT32\_TYPE\_\_ int32\_t

**Definition** stdint.h:74

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[bt\_mesh\_cfg\_cli\_cb](structbt__mesh__cfg__cli__cb.md)

Mesh Configuration Client Status messages callback.

**Definition** cfg\_cli.h:33

[bt\_mesh\_cfg\_cli\_cb::mod\_sub\_list](structbt__mesh__cfg__cli__cb.md#a0ad46d1d4793577679f66c62175e14cf)

void(\* mod\_sub\_list)(struct bt\_mesh\_cfg\_cli \*cli, uint16\_t addr, uint8\_t status, uint16\_t elem\_addr, uint16\_t mod\_id, uint16\_t cid, struct net\_buf\_simple \*buf)

Optional callback for Model Sub list messages.

**Definition** cfg\_cli.h:98

[bt\_mesh\_cfg\_cli\_cb::mod\_app\_status](structbt__mesh__cfg__cli__cb.md#a3ccff69f21e0f3c585b951eb60c1bf5c)

void(\* mod\_app\_status)(struct bt\_mesh\_cfg\_cli \*cli, uint16\_t addr, uint8\_t status, uint16\_t elem\_addr, uint16\_t app\_idx, uint32\_t mod\_id)

Optional callback for Model App Status messages.

**Definition** cfg\_cli.h:245

[bt\_mesh\_cfg\_cli\_cb::app\_key\_status](structbt__mesh__cfg__cli__cb.md#a48ef4d0665d86d069b90533eb18e0fd0)

void(\* app\_key\_status)(struct bt\_mesh\_cfg\_cli \*cli, uint16\_t addr, uint8\_t status, uint16\_t net\_idx, uint16\_t app\_idx)

Optional callback for AppKey Status messages.

**Definition** cfg\_cli.h:214

[bt\_mesh\_cfg\_cli\_cb::net\_key\_status](structbt__mesh__cfg__cli__cb.md#a49a7a8cab34bb70d2edd87b0017f1cf7)

void(\* net\_key\_status)(struct bt\_mesh\_cfg\_cli \*cli, uint16\_t addr, uint8\_t status, uint16\_t net\_idx)

Optional callback for NetKey Status messages.

**Definition** cfg\_cli.h:187

[bt\_mesh\_cfg\_cli\_cb::krp\_status](structbt__mesh__cfg__cli__cb.md#a4d89033676eb4570cdd80f1715fd9bfb)

void(\* krp\_status)(struct bt\_mesh\_cfg\_cli \*cli, uint16\_t addr, uint8\_t status, uint16\_t net\_idx, uint8\_t phase)

Optional callback for Key Refresh Phase status messages.

**Definition** cfg\_cli.h:304

[bt\_mesh\_cfg\_cli\_cb::beacon\_status](structbt__mesh__cfg__cli__cb.md#a5cf2c17a88c53c514fcaa73a6fd81b67)

void(\* beacon\_status)(struct bt\_mesh\_cfg\_cli \*cli, uint16\_t addr, uint8\_t status)

Optional callback for Beacon Status messages.

**Definition** cfg\_cli.h:119

[bt\_mesh\_cfg\_cli\_cb::hb\_pub\_status](structbt__mesh__cfg__cli__cb.md#a615852027a841b1779a50c9fd50bef6a)

void(\* hb\_pub\_status)(struct bt\_mesh\_cfg\_cli \*cli, uint16\_t addr, uint8\_t status, struct bt\_mesh\_cfg\_cli\_hb\_pub \*pub)

Optional callback for Heartbeat pub status messages.

**Definition** cfg\_cli.h:316

[bt\_mesh\_cfg\_cli\_cb::lpn\_timeout\_status](structbt__mesh__cfg__cli__cb.md#a66b5a8dd3bdd2468fe65496020b13495)

void(\* lpn\_timeout\_status)(struct bt\_mesh\_cfg\_cli \*cli, uint16\_t addr, uint16\_t elem\_addr, uint32\_t timeout)

Optional callback for LPN PollTimeout Status messages.

**Definition** cfg\_cli.h:291

[bt\_mesh\_cfg\_cli\_cb::gatt\_proxy\_status](structbt__mesh__cfg__cli__cb.md#a6ef3730e9469bffd81cdd49c50cac7d5)

void(\* gatt\_proxy\_status)(struct bt\_mesh\_cfg\_cli \*cli, uint16\_t addr, uint8\_t status)

Optional callback for GATT Proxy Status messages.

**Definition** cfg\_cli.h:152

[bt\_mesh\_cfg\_cli\_cb::relay\_status](structbt__mesh__cfg__cli__cb.md#a89eab453e00662f6f3f8a5d78f20d120)

void(\* relay\_status)(struct bt\_mesh\_cfg\_cli \*cli, uint16\_t addr, uint8\_t status, uint8\_t transmit)

Optional callback for Relay Status messages.

**Definition** cfg\_cli.h:175

[bt\_mesh\_cfg\_cli\_cb::friend\_status](structbt__mesh__cfg__cli__cb.md#a9487a159a6c838a9218b3d76fa53248d)

void(\* friend\_status)(struct bt\_mesh\_cfg\_cli \*cli, uint16\_t addr, uint8\_t status)

Optional callback for Friend Status messages.

**Definition** cfg\_cli.h:141

[bt\_mesh\_cfg\_cli\_cb::hb\_sub\_status](structbt__mesh__cfg__cli__cb.md#aa60dfd72a43273e1ffae2160bcc0845d)

void(\* hb\_sub\_status)(struct bt\_mesh\_cfg\_cli \*cli, uint16\_t addr, uint8\_t status, struct bt\_mesh\_cfg\_cli\_hb\_sub \*sub)

Optional callback for Heartbeat Sub status messages.

**Definition** cfg\_cli.h:328

[bt\_mesh\_cfg\_cli\_cb::comp\_data](structbt__mesh__cfg__cli__cb.md#aaae4e3f64e2033a466ad87d362ceb318)

void(\* comp\_data)(struct bt\_mesh\_cfg\_cli \*cli, uint16\_t addr, uint8\_t page, struct net\_buf\_simple \*buf)

Optional callback for Composition data messages.

**Definition** cfg\_cli.h:48

[bt\_mesh\_cfg\_cli\_cb::mod\_pub\_status](structbt__mesh__cfg__cli__cb.md#ab4130e909826aa7746092f49f8b4c52e)

void(\* mod\_pub\_status)(struct bt\_mesh\_cfg\_cli \*cli, uint16\_t addr, uint8\_t status, uint16\_t elem\_addr, uint16\_t mod\_id, uint16\_t cid, struct bt\_mesh\_cfg\_cli\_mod\_pub \*pub)

Optional callback for Model Pub status messages.

**Definition** cfg\_cli.h:63

[bt\_mesh\_cfg\_cli\_cb::ttl\_status](structbt__mesh__cfg__cli__cb.md#ab937311c41af68b1cd52a8a1c86145b1)

void(\* ttl\_status)(struct bt\_mesh\_cfg\_cli \*cli, uint16\_t addr, uint8\_t status)

Optional callback for Default TTL Status messages.

**Definition** cfg\_cli.h:130

[bt\_mesh\_cfg\_cli\_cb::mod\_app\_list](structbt__mesh__cfg__cli__cb.md#abf8501e73f44ab5ea7e54b8f2ff1f866)

void(\* mod\_app\_list)(struct bt\_mesh\_cfg\_cli \*cli, uint16\_t addr, uint8\_t status, uint16\_t elem\_addr, uint16\_t mod\_id, uint16\_t cid, struct net\_buf\_simple \*buf)

Optional callback for Model App list messages.

**Definition** cfg\_cli.h:264

[bt\_mesh\_cfg\_cli\_cb::app\_key\_list](structbt__mesh__cfg__cli__cb.md#ac331fc103d0f331093929f39e5b9d6ba)

void(\* app\_key\_list)(struct bt\_mesh\_cfg\_cli \*cli, uint16\_t addr, uint8\_t status, uint16\_t net\_idx, struct net\_buf\_simple \*buf)

Optional callback for Appkey list messages.

**Definition** cfg\_cli.h:231

[bt\_mesh\_cfg\_cli\_cb::node\_identity\_status](structbt__mesh__cfg__cli__cb.md#aca2d779401fa4521813e6578bd3bbd91)

void(\* node\_identity\_status)(struct bt\_mesh\_cfg\_cli \*cli, uint16\_t addr, uint8\_t status, uint16\_t net\_idx, uint8\_t identity)

Optional callback for Node Identity Status messages.

**Definition** cfg\_cli.h:278

[bt\_mesh\_cfg\_cli\_cb::net\_key\_list](structbt__mesh__cfg__cli__cb.md#acce08dfa5cb356a2203f0ef6c4e4bf5b)

void(\* net\_key\_list)(struct bt\_mesh\_cfg\_cli \*cli, uint16\_t addr, struct net\_buf\_simple \*buf)

Optional callback for Netkey list messages.

**Definition** cfg\_cli.h:201

[bt\_mesh\_cfg\_cli\_cb::node\_reset\_status](structbt__mesh__cfg__cli__cb.md#acf88660364760442dfab5280ae735d2d)

void(\* node\_reset\_status)(struct bt\_mesh\_cfg\_cli \*cli, uint16\_t addr)

Optional callback for Node Reset Status messages.

**Definition** cfg\_cli.h:109

[bt\_mesh\_cfg\_cli\_cb::network\_transmit\_status](structbt__mesh__cfg__cli__cb.md#ad46ea40b75cc1d5d314fdefdca0076f8)

void(\* network\_transmit\_status)(struct bt\_mesh\_cfg\_cli \*cli, uint16\_t addr, uint8\_t status)

Optional callback for Network Transmit Status messages.

**Definition** cfg\_cli.h:163

[bt\_mesh\_cfg\_cli\_cb::mod\_sub\_status](structbt__mesh__cfg__cli__cb.md#af4a43f4c65d111e95211b715048534cc)

void(\* mod\_sub\_status)(struct bt\_mesh\_cfg\_cli \*cli, uint16\_t addr, uint8\_t status, uint16\_t elem\_addr, uint16\_t sub\_addr, uint32\_t mod\_id)

Optional callback for Model Sub Status messages.

**Definition** cfg\_cli.h:78

[bt\_mesh\_cfg\_cli\_hb\_pub](structbt__mesh__cfg__cli__hb__pub.md)

Heartbeat publication configuration parameters.

**Definition** cfg\_cli.h:460

[bt\_mesh\_cfg\_cli\_hb\_pub::count](structbt__mesh__cfg__cli__hb__pub.md#a13c7c155f30ca94d30090a25df50e4b2)

uint8\_t count

Logarithmic Heartbeat count.

**Definition** cfg\_cli.h:474

[bt\_mesh\_cfg\_cli\_hb\_pub::dst](structbt__mesh__cfg__cli__hb__pub.md#a473df7dd958683d7502dcc983c4ceb8a)

uint16\_t dst

Heartbeat destination address.

**Definition** cfg\_cli.h:462

[bt\_mesh\_cfg\_cli\_hb\_pub::period](structbt__mesh__cfg__cli__hb__pub.md#a8d17dd2df4be23cadad4b5746ddb50ad)

uint8\_t period

Logarithmic Heartbeat publication transmit interval in seconds.

**Definition** cfg\_cli.h:480

[bt\_mesh\_cfg\_cli\_hb\_pub::net\_idx](structbt__mesh__cfg__cli__hb__pub.md#a90a79d8b7ea91c6ba872dca15d87b356)

uint16\_t net\_idx

Network index to publish with.

**Definition** cfg\_cli.h:491

[bt\_mesh\_cfg\_cli\_hb\_pub::feat](structbt__mesh__cfg__cli__hb__pub.md#a94598c9b733075abe22d70f62293b5a1)

uint16\_t feat

Bitmap of features that trigger Heartbeat publications.

**Definition** cfg\_cli.h:489

[bt\_mesh\_cfg\_cli\_hb\_pub::ttl](structbt__mesh__cfg__cli__hb__pub.md#ac7f24f7bf942587ef83ca47d9ee4e7fb)

uint8\_t ttl

Publication message Time To Live value.

**Definition** cfg\_cli.h:482

[bt\_mesh\_cfg\_cli\_hb\_sub](structbt__mesh__cfg__cli__hb__sub.md)

Heartbeat subscription configuration parameters.

**Definition** cfg\_cli.h:422

[bt\_mesh\_cfg\_cli\_hb\_sub::src](structbt__mesh__cfg__cli__hb__sub.md#a01ec0c3cab7bb7ed76d7728390eb4f25)

uint16\_t src

Source address to receive Heartbeat messages from.

**Definition** cfg\_cli.h:424

[bt\_mesh\_cfg\_cli\_hb\_sub::min](structbt__mesh__cfg__cli__hb__sub.md#a480b214e0e1974a6a54426c49e5d62d1)

uint8\_t min

Minimum hops in received messages, ie the shortest registered path from the publishing node to the su...

**Definition** cfg\_cli.h:448

[bt\_mesh\_cfg\_cli\_hb\_sub::period](structbt__mesh__cfg__cli__hb__sub.md#a5a75c924f0868c664652503335b1b012)

uint8\_t period

Logarithmic subscription period to keep listening for.

**Definition** cfg\_cli.h:432

[bt\_mesh\_cfg\_cli\_hb\_sub::count](structbt__mesh__cfg__cli__hb__sub.md#a93624ab6c8a0c15c0b50490e0fcd3675)

uint8\_t count

Logarithmic Heartbeat subscription receive count.

**Definition** cfg\_cli.h:440

[bt\_mesh\_cfg\_cli\_hb\_sub::max](structbt__mesh__cfg__cli__hb__sub.md#aac96c2ab606e38f412e94539795c5594)

uint8\_t max

Maximum hops in received messages, ie the longest registered path from the publishing node to the sub...

**Definition** cfg\_cli.h:456

[bt\_mesh\_cfg\_cli\_hb\_sub::dst](structbt__mesh__cfg__cli__hb__sub.md#abc9ea18fbe86c260d6cf5d53c26a0248)

uint16\_t dst

Destination address to receive Heartbeat messages on.

**Definition** cfg\_cli.h:426

[bt\_mesh\_cfg\_cli\_mod\_pub](structbt__mesh__cfg__cli__mod__pub.md)

Model publication configuration parameters.

**Definition** cfg\_cli.h:396

[bt\_mesh\_cfg\_cli\_mod\_pub::period](structbt__mesh__cfg__cli__mod__pub.md#a104afe2b8d9766e037293b09c0c1b91c)

uint8\_t period

Encoded publish period.

**Definition** cfg\_cli.h:413

[bt\_mesh\_cfg\_cli\_mod\_pub::uuid](structbt__mesh__cfg__cli__mod__pub.md#a29cbd50ad33f25ad3b98b4ec7ac56a6c)

const uint8\_t \* uuid

Virtual address UUID, or NULL if this is not a virtual address.

**Definition** cfg\_cli.h:400

[bt\_mesh\_cfg\_cli\_mod\_pub::transmit](structbt__mesh__cfg__cli__mod__pub.md#a2a5a0ead8155bf971c84f73dfa4ec282)

uint8\_t transmit

Encoded transmit parameters.

**Definition** cfg\_cli.h:418

[bt\_mesh\_cfg\_cli\_mod\_pub::ttl](structbt__mesh__cfg__cli__mod__pub.md#a9513db038ec4f51734892bd1ce7d08f3)

uint8\_t ttl

Time To Live to publish with.

**Definition** cfg\_cli.h:406

[bt\_mesh\_cfg\_cli\_mod\_pub::cred\_flag](structbt__mesh__cfg__cli__mod__pub.md#aa7452f697410fdf8a63808bcb29c53ee)

bool cred\_flag

Friendship credential flag.

**Definition** cfg\_cli.h:404

[bt\_mesh\_cfg\_cli\_mod\_pub::addr](structbt__mesh__cfg__cli__mod__pub.md#ab52dd35df271ae5bd70a4640e6f3bea8)

uint16\_t addr

Publication destination address.

**Definition** cfg\_cli.h:398

[bt\_mesh\_cfg\_cli\_mod\_pub::app\_idx](structbt__mesh__cfg__cli__mod__pub.md#aefbe5449a10379b064dea054300cb9a0)

uint16\_t app\_idx

Application index to publish with.

**Definition** cfg\_cli.h:402

[bt\_mesh\_cfg\_cli](structbt__mesh__cfg__cli.md)

Mesh Configuration Client Model Context.

**Definition** cfg\_cli.h:333

[bt\_mesh\_cfg\_cli::ack\_ctx](structbt__mesh__cfg__cli.md#a472bf5015857ab97e1a40ab6cfa70bb1)

struct bt\_mesh\_msg\_ack\_ctx ack\_ctx

**Definition** cfg\_cli.h:341

[bt\_mesh\_cfg\_cli::model](structbt__mesh__cfg__cli.md#a525dd5391c83c525c012940575245cea)

const struct bt\_mesh\_model \* model

Composition data model entry pointer.

**Definition** cfg\_cli.h:335

[bt\_mesh\_cfg\_cli::cb](structbt__mesh__cfg__cli.md#a7160cf5d22fa0b909482bbc76f27b6bd)

const struct bt\_mesh\_cfg\_cli\_cb \* cb

Optional callback for Mesh Configuration Client Status messages.

**Definition** cfg\_cli.h:338

[bt\_mesh\_comp\_p0\_elem](structbt__mesh__comp__p0__elem.md)

Composition data page 0 element representation.

**Definition** cfg\_cli.h:1621

[bt\_mesh\_comp\_p0\_elem::nsig](structbt__mesh__comp__p0__elem.md#a17f61eab2df28f2031f2fbab28254484)

size\_t nsig

The number of SIG models in this element.

**Definition** cfg\_cli.h:1625

[bt\_mesh\_comp\_p0\_elem::nvnd](structbt__mesh__comp__p0__elem.md#a2e1bd3146ebc934e9fab0242a06d5b99)

size\_t nvnd

The number of vendor models in this element.

**Definition** cfg\_cli.h:1627

[bt\_mesh\_comp\_p0\_elem::loc](structbt__mesh__comp__p0__elem.md#a832cdb0a10d364a048971f59f51e841d)

uint16\_t loc

Element location.

**Definition** cfg\_cli.h:1623

[bt\_mesh\_comp\_p0](structbt__mesh__comp__p0.md)

Parsed Composition data page 0 representation.

**Definition** cfg\_cli.h:1605

[bt\_mesh\_comp\_p0::pid](structbt__mesh__comp__p0.md#a009806e046583c99f56d271ecebbb8a3)

uint16\_t pid

Product ID.

**Definition** cfg\_cli.h:1609

[bt\_mesh\_comp\_p0::feat](structbt__mesh__comp__p0.md#a0a44e3778f9d134a5c056ca184c3b527)

uint16\_t feat

Supported features, see BT\_MESH\_FEAT\_SUPPORTED.

**Definition** cfg\_cli.h:1615

[bt\_mesh\_comp\_p0::vid](structbt__mesh__comp__p0.md#a27d910cdeb7b6b9d038898e3824dfb57)

uint16\_t vid

Version ID.

**Definition** cfg\_cli.h:1611

[bt\_mesh\_comp\_p0::crpl](structbt__mesh__comp__p0.md#a32bfead26f338aba892a5459615a65a2)

uint16\_t crpl

Replay protection list size.

**Definition** cfg\_cli.h:1613

[bt\_mesh\_comp\_p0::cid](structbt__mesh__comp__p0.md#a3ed8f5ac643443bbcca308baff1c539c)

uint16\_t cid

Company ID.

**Definition** cfg\_cli.h:1607

[bt\_mesh\_comp\_p1\_elem](structbt__mesh__comp__p1__elem.md)

Composition data page 1 element representation.

**Definition** cfg\_cli.h:1694

[bt\_mesh\_comp\_p1\_elem::nvnd](structbt__mesh__comp__p1__elem.md#a25492ac30a362e4490d11169ed98197b)

size\_t nvnd

The number of vendor models in this element.

**Definition** cfg\_cli.h:1698

[bt\_mesh\_comp\_p1\_elem::nsig](structbt__mesh__comp__p1__elem.md#aa6aa100992502cef0484a127224cf07b)

size\_t nsig

The number of SIG models in this element.

**Definition** cfg\_cli.h:1696

[bt\_mesh\_comp\_p1\_ext\_item](structbt__mesh__comp__p1__ext__item.md)

Extended Model Item.

**Definition** cfg\_cli.h:1736

[bt\_mesh\_comp\_p1\_ext\_item::SHORT](structbt__mesh__comp__p1__ext__item.md#a05a526a8448e7b8a4766eb038e4c1a39a23a15546d8722d7a4706ea34c5785658)

@ SHORT

**Definition** cfg\_cli.h:1737

[bt\_mesh\_comp\_p1\_ext\_item::LONG](structbt__mesh__comp__p1__ext__item.md#a05a526a8448e7b8a4766eb038e4c1a39ae96bb3e960c4d2c356c0070f34740119)

@ LONG

**Definition** cfg\_cli.h:1737

[bt\_mesh\_comp\_p1\_ext\_item::long\_item](structbt__mesh__comp__p1__ext__item.md#a3962046fc095348035a193dad60d1149)

struct bt\_mesh\_comp\_p1\_item\_long long\_item

Item in long representation.

**Definition** cfg\_cli.h:1743

[bt\_mesh\_comp\_p1\_ext\_item::type](structbt__mesh__comp__p1__ext__item.md#a43f50f35690e54d3680a6daa989ce1c0)

enum bt\_mesh\_comp\_p1\_ext\_item::@065125255021342207377151171072347326255105000343 type

[bt\_mesh\_comp\_p1\_ext\_item::short\_item](structbt__mesh__comp__p1__ext__item.md#ae17176001203ee8c282f06e994cee647)

struct bt\_mesh\_comp\_p1\_item\_short short\_item

Item in short representation.

**Definition** cfg\_cli.h:1741

[bt\_mesh\_comp\_p1\_item\_long](structbt__mesh__comp__p1__item__long.md)

Extended Model Item in long representation.

**Definition** cfg\_cli.h:1728

[bt\_mesh\_comp\_p1\_item\_long::elem\_offset](structbt__mesh__comp__p1__item__long.md#a12a0e2fb373e2e43b7c04a1130cdf018)

uint8\_t elem\_offset

Element address modifier.

**Definition** cfg\_cli.h:1730

[bt\_mesh\_comp\_p1\_item\_long::mod\_item\_idx](structbt__mesh__comp__p1__item__long.md#a61d541854c2d1671c60fc444978f0374)

uint8\_t mod\_item\_idx

Model Index.

**Definition** cfg\_cli.h:1732

[bt\_mesh\_comp\_p1\_item\_short](structbt__mesh__comp__p1__item__short.md)

Extended Model Item in short representation.

**Definition** cfg\_cli.h:1720

[bt\_mesh\_comp\_p1\_item\_short::elem\_offset](structbt__mesh__comp__p1__item__short.md#a1fb6c8134a2c02e3b83dfea12ab39410)

uint8\_t elem\_offset

Element address modifier.

**Definition** cfg\_cli.h:1722

[bt\_mesh\_comp\_p1\_item\_short::mod\_item\_idx](structbt__mesh__comp__p1__item__short.md#a7e2152fe608c52cbc0700a43a5653132)

uint8\_t mod\_item\_idx

Model Index.

**Definition** cfg\_cli.h:1724

[bt\_mesh\_comp\_p1\_model\_item](structbt__mesh__comp__p1__model__item.md)

Composition data page 1 model item representation.

**Definition** cfg\_cli.h:1704

[bt\_mesh\_comp\_p1\_model\_item::cor\_id](structbt__mesh__comp__p1__model__item.md#a95baa1acf3a82e8559ce4a47b7e03be8)

uint8\_t cor\_id

Buffer containing Extended Model Items.

**Definition** cfg\_cli.h:1715

[bt\_mesh\_comp\_p1\_model\_item::ext\_item\_cnt](structbt__mesh__comp__p1__model__item.md#ae019a211eafeb20f323ad97328d938f7)

uint8\_t ext\_item\_cnt

Number of items in Extended Model Items.

**Definition** cfg\_cli.h:1710

[bt\_mesh\_comp\_p1\_model\_item::cor\_present](structbt__mesh__comp__p1__model__item.md#aee352e8563133dddbb37c1f31dfe7c09)

bool cor\_present

Corresponding\_Group\_ID field indicator.

**Definition** cfg\_cli.h:1706

[bt\_mesh\_comp\_p1\_model\_item::format](structbt__mesh__comp__p1__model__item.md#af2f213813440cb4a87884e3625a704e7)

bool format

Determines the format of Extended Model Item.

**Definition** cfg\_cli.h:1708

[bt\_mesh\_comp\_p2\_record](structbt__mesh__comp__p2__record.md)

Composition data page 2 record parsing structure.

**Definition** cfg\_cli.h:1791

[bt\_mesh\_comp\_p2\_record::y](structbt__mesh__comp__p2__record.md#a0ceff9becd0eb14ca190c49f56ec0957)

uint8\_t y

Minor version.

**Definition** cfg\_cli.h:1799

[bt\_mesh\_comp\_p2\_record::id](structbt__mesh__comp__p2__record.md#a4d947193b1a0f46c9df1eca298135646)

uint16\_t id

Mesh profile ID.

**Definition** cfg\_cli.h:1793

[bt\_mesh\_comp\_p2\_record::x](structbt__mesh__comp__p2__record.md#a5377ce835db8ce408d8dabfd87c858f5)

uint8\_t x

Major version.

**Definition** cfg\_cli.h:1797

[bt\_mesh\_comp\_p2\_record::z](structbt__mesh__comp__p2__record.md#a90e80906ef6d2b8b932215ad183db2d5)

uint8\_t z

Z version.

**Definition** cfg\_cli.h:1801

[bt\_mesh\_comp\_p2\_record::version](structbt__mesh__comp__p2__record.md#aa718c024d6ce339ac8c352319b878c53)

struct bt\_mesh\_comp\_p2\_record::@175335254377136065250046215131122232264115073233 version

Mesh Profile Version.

[bt\_mesh\_comp\_p2\_record::data\_buf](structbt__mesh__comp__p2__record.md#abd0975a47c848265ad13044dfcd3b78d)

struct net\_buf\_simple \* data\_buf

Additional data buffer.

**Definition** cfg\_cli.h:1806

[bt\_mesh\_comp\_p2\_record::elem\_buf](structbt__mesh__comp__p2__record.md#ad310f8c8e3a167492a6e698336b7f400)

struct net\_buf\_simple \* elem\_buf

Element offset buffer.

**Definition** cfg\_cli.h:1804

[bt\_mesh\_mod\_id\_vnd](structbt__mesh__mod__id__vnd.md)

Vendor model ID.

**Definition** access.h:873

[bt\_mesh\_model\_cb](structbt__mesh__model__cb.md)

Model callback functions.

**Definition** access.h:803

[bt\_mesh\_model\_op](structbt__mesh__model__op.md)

Model opcode handler.

**Definition** access.h:359

[bt\_mesh\_model](structbt__mesh__model.md)

Abstraction that describes a Mesh Model instance.

**Definition** access.h:881

[bt\_mesh\_msg\_ack\_ctx](structbt__mesh__msg__ack__ctx.md)

Acknowledged message context for tracking the status of model messages pending a response.

**Definition** msg.h:172

[net\_buf\_simple](structnet__buf__simple.md)

Simple network buffer representation.

**Definition** buf.h:87

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [mesh](dir_cb009b76fe94f798a2c866bd15366281.md)
- [cfg\_cli.h](cfg__cli_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
