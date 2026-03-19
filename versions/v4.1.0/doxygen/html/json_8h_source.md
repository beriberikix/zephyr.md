---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/json_8h_source.html
original_path: doxygen/html/json_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

json.h

[Go to the documentation of this file.](json_8h.md)

1/\*

2 \* Copyright (c) 2017 Intel Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DATA\_JSON\_H\_

8#define ZEPHYR\_INCLUDE\_DATA\_JSON\_H\_

9

10#include <[zephyr/sys/util.h](sys_2util_8h.md)>

11#include <stddef.h>

12#include <[zephyr/toolchain.h](toolchain_8h.md)>

13#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

14#include <[sys/types.h](lib_2libc_2minimal_2include_2sys_2types_8h.md)>

15

16#ifdef \_\_cplusplus

17extern "C" {

18#endif

19

25

[ 26](group__json.md#ga18a137ac5e2998d375540298670797c4)enum [json\_tokens](group__json.md#ga18a137ac5e2998d375540298670797c4) {

27 /\* Before changing this enum, ensure that its maximum

28 \* value is still within 7 bits. See comment next to the

29 \* declaration of `type` in struct json\_obj\_descr.

30 \*/

31

[ 32](group__json.md#gga18a137ac5e2998d375540298670797c4a926d6b0a5458be2e707d51f0b25dbe77) [JSON\_TOK\_NONE](group__json.md#gga18a137ac5e2998d375540298670797c4a926d6b0a5458be2e707d51f0b25dbe77) = '\_',

[ 33](group__json.md#gga18a137ac5e2998d375540298670797c4a81e303d23da0b3d8504cc4a7ee7d52e8) [JSON\_TOK\_OBJECT\_START](group__json.md#gga18a137ac5e2998d375540298670797c4a81e303d23da0b3d8504cc4a7ee7d52e8) = '{',

[ 34](group__json.md#gga18a137ac5e2998d375540298670797c4a835bc516b25eb0619b3f1a52f1ebc911) [JSON\_TOK\_OBJECT\_END](group__json.md#gga18a137ac5e2998d375540298670797c4a835bc516b25eb0619b3f1a52f1ebc911) = '}',

[ 35](group__json.md#gga18a137ac5e2998d375540298670797c4a9856446d3a2aa3155266957b8b1371cd) [JSON\_TOK\_ARRAY\_START](group__json.md#gga18a137ac5e2998d375540298670797c4a9856446d3a2aa3155266957b8b1371cd) = '[',

[ 36](group__json.md#gga18a137ac5e2998d375540298670797c4a2483f21d814abcd08b5253e55aef70c9) [JSON\_TOK\_ARRAY\_END](group__json.md#gga18a137ac5e2998d375540298670797c4a2483f21d814abcd08b5253e55aef70c9) = ']',

[ 37](group__json.md#gga18a137ac5e2998d375540298670797c4ab145f07a93c4fdcf60c9052fbd9a7afc) [JSON\_TOK\_STRING](group__json.md#gga18a137ac5e2998d375540298670797c4ab145f07a93c4fdcf60c9052fbd9a7afc) = '"',

[ 38](group__json.md#gga18a137ac5e2998d375540298670797c4a4873e5c0c6344323d5d6af158952ca36) [JSON\_TOK\_COLON](group__json.md#gga18a137ac5e2998d375540298670797c4a4873e5c0c6344323d5d6af158952ca36) = ':',

[ 39](group__json.md#gga18a137ac5e2998d375540298670797c4a736325745f9521f38a68962775e76a50) [JSON\_TOK\_COMMA](group__json.md#gga18a137ac5e2998d375540298670797c4a736325745f9521f38a68962775e76a50) = ',',

[ 40](group__json.md#gga18a137ac5e2998d375540298670797c4ae25f16ae591eb17d4074e6dcc2f1e62c) [JSON\_TOK\_NUMBER](group__json.md#gga18a137ac5e2998d375540298670797c4ae25f16ae591eb17d4074e6dcc2f1e62c) = '0',

[ 41](group__json.md#gga18a137ac5e2998d375540298670797c4aa842c96d114ed77ab66446bcac1424b5) [JSON\_TOK\_FLOAT](group__json.md#gga18a137ac5e2998d375540298670797c4aa842c96d114ed77ab66446bcac1424b5) = '1',

[ 42](group__json.md#gga18a137ac5e2998d375540298670797c4a94ef68b273a74244acb3bdec99b6a024) [JSON\_TOK\_OPAQUE](group__json.md#gga18a137ac5e2998d375540298670797c4a94ef68b273a74244acb3bdec99b6a024) = '2',

[ 43](group__json.md#gga18a137ac5e2998d375540298670797c4a14739d9c36212d3df0007427b7b99e25) [JSON\_TOK\_OBJ\_ARRAY](group__json.md#gga18a137ac5e2998d375540298670797c4a14739d9c36212d3df0007427b7b99e25) = '3',

[ 44](group__json.md#gga18a137ac5e2998d375540298670797c4af1e451cb321c805cff8fcde3561d3e64) [JSON\_TOK\_ENCODED\_OBJ](group__json.md#gga18a137ac5e2998d375540298670797c4af1e451cb321c805cff8fcde3561d3e64) = '4',

[ 45](group__json.md#gga18a137ac5e2998d375540298670797c4a37f98b21d196182fd2b8cd4c71ed607e) [JSON\_TOK\_INT64](group__json.md#gga18a137ac5e2998d375540298670797c4a37f98b21d196182fd2b8cd4c71ed607e) = '5',

[ 46](group__json.md#gga18a137ac5e2998d375540298670797c4a6218cd0d5d8a34cf4b32797f361b5a41) [JSON\_TOK\_UINT64](group__json.md#gga18a137ac5e2998d375540298670797c4a6218cd0d5d8a34cf4b32797f361b5a41) = '6',

[ 47](group__json.md#gga18a137ac5e2998d375540298670797c4a87ffb12e4d174bb4427d9a72eabca7e3) [JSON\_TOK\_TRUE](group__json.md#gga18a137ac5e2998d375540298670797c4a87ffb12e4d174bb4427d9a72eabca7e3) = 't',

[ 48](group__json.md#gga18a137ac5e2998d375540298670797c4a8df1b1d0061d7e289f94bae1df35baa7) [JSON\_TOK\_FALSE](group__json.md#gga18a137ac5e2998d375540298670797c4a8df1b1d0061d7e289f94bae1df35baa7) = 'f',

[ 49](group__json.md#gga18a137ac5e2998d375540298670797c4a93de1b7e780ac22744c97e922de3b35e) [JSON\_TOK\_NULL](group__json.md#gga18a137ac5e2998d375540298670797c4a93de1b7e780ac22744c97e922de3b35e) = 'n',

[ 50](group__json.md#gga18a137ac5e2998d375540298670797c4afe9c51f453d7dd02504071330a030e9e) [JSON\_TOK\_ERROR](group__json.md#gga18a137ac5e2998d375540298670797c4afe9c51f453d7dd02504071330a030e9e) = '!',

[ 51](group__json.md#gga18a137ac5e2998d375540298670797c4ad970b7d8553296bf4ed03c831cb6f604) [JSON\_TOK\_EOF](group__json.md#gga18a137ac5e2998d375540298670797c4ad970b7d8553296bf4ed03c831cb6f604) = '\0',

52};

53

[ 54](structjson__token.md)struct [json\_token](structjson__token.md) {

[ 55](structjson__token.md#ab163615cc3a39191d5a48e900c579e94) enum [json\_tokens](group__json.md#ga18a137ac5e2998d375540298670797c4) [type](structjson__token.md#ab163615cc3a39191d5a48e900c579e94);

[ 56](structjson__token.md#a606e33f699c3ec5a66f450cc1777b3c2) char \*[start](structjson__token.md#a606e33f699c3ec5a66f450cc1777b3c2);

[ 57](structjson__token.md#abb55042d9343358e85311ea52cacb963) char \*[end](structjson__token.md#abb55042d9343358e85311ea52cacb963);

58};

59

[ 60](structjson__lexer.md)struct [json\_lexer](structjson__lexer.md) {

[ 61](structjson__lexer.md#ae74beb9d896daf102ec5ffff370830b3) void \*(\*state)(struct [json\_lexer](structjson__lexer.md) \*lex);

[ 62](structjson__lexer.md#aa4d4a29301fb840c691bbfa416474de4) char \*[start](structjson__lexer.md#aa4d4a29301fb840c691bbfa416474de4);

[ 63](structjson__lexer.md#a9b403c5505e9a2cd9e475416b2e7f0ac) char \*[pos](structjson__lexer.md#a9b403c5505e9a2cd9e475416b2e7f0ac);

[ 64](structjson__lexer.md#aeaf5743a9285e0aef9df99f9b3b48320) char \*[end](structjson__lexer.md#aeaf5743a9285e0aef9df99f9b3b48320);

[ 65](structjson__lexer.md#ab285bc72bf12a4de31b45ac0fc992620) struct [json\_token](structjson__token.md) [tok](structjson__lexer.md#ab285bc72bf12a4de31b45ac0fc992620);

66};

67

[ 68](structjson__obj.md)struct [json\_obj](structjson__obj.md) {

[ 69](structjson__obj.md#a7a48a2dca53ee74e7c8eb4727af0e33a) struct [json\_lexer](structjson__lexer.md) [lex](structjson__obj.md#a7a48a2dca53ee74e7c8eb4727af0e33a);

70};

71

[ 72](structjson__obj__token.md)struct [json\_obj\_token](structjson__obj__token.md) {

[ 73](structjson__obj__token.md#aef14abe1f0cefda6bd89d058787550b1) char \*[start](structjson__obj__token.md#aef14abe1f0cefda6bd89d058787550b1);

[ 74](structjson__obj__token.md#ac996ab0b850803998a37025b57051144) size\_t [length](structjson__obj__token.md#ac996ab0b850803998a37025b57051144);

75};

76

77

[ 78](structjson__obj__descr.md)struct [json\_obj\_descr](structjson__obj__descr.md) {

[ 79](structjson__obj__descr.md#a2120b7752253ece0beddcaf4c57d3ed8) const char \*[field\_name](structjson__obj__descr.md#a2120b7752253ece0beddcaf4c57d3ed8);

80

81 /\* Alignment can be 1, 2, 4, or 8. The macros to create

82 \* a struct json\_obj\_descr will store the alignment's

83 \* power of 2 in order to keep this value in the 0-3 range

84 \* and thus use only 2 bits.

85 \*/

[ 86](structjson__obj__descr.md#a475717ac4dd01296c01468450e50f75b) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [align\_shift](structjson__obj__descr.md#a475717ac4dd01296c01468450e50f75b) : 2;

87

88 /\* 127 characters is more than enough for a field name. \*/

[ 89](structjson__obj__descr.md#a602bf4d8bb5d47c8edb40963ea8ba42f) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [field\_name\_len](structjson__obj__descr.md#a602bf4d8bb5d47c8edb40963ea8ba42f) : 7;

90

91 /\* Valid values here (enum json\_tokens): JSON\_TOK\_STRING,

92 \* JSON\_TOK\_NUMBER, JSON\_TOK\_TRUE, JSON\_TOK\_FALSE,

93 \* JSON\_TOK\_OBJECT\_START, JSON\_TOK\_ARRAY\_START. (All others

94 \* ignored.) Maximum value is '}' (125), so this has to be 7 bits

95 \* long.

96 \*/

[ 97](structjson__obj__descr.md#a975e998d3ec36f234f09aa2d0d116c9c) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [type](structjson__obj__descr.md#a975e998d3ec36f234f09aa2d0d116c9c) : 7;

98

99 /\* 65535 bytes is more than enough for many JSON payloads. \*/

[ 100](structjson__obj__descr.md#a8c6f3eae5e678b8b8ef1957c46f488f1) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [offset](structjson__obj__descr.md#a8c6f3eae5e678b8b8ef1957c46f488f1) : 16;

101

102 union {

103 struct {

[ 104](structjson__obj__descr.md#a4f5e97c654d0c5e21f1efb5a01966e56) const struct [json\_obj\_descr](structjson__obj__descr.md) \*[sub\_descr](structjson__obj__descr.md#a4f5e97c654d0c5e21f1efb5a01966e56);

[ 105](structjson__obj__descr.md#adea0b44d1552305df9dce70074044ba1) size\_t [sub\_descr\_len](structjson__obj__descr.md#adea0b44d1552305df9dce70074044ba1);

[ 106](structjson__obj__descr.md#a5d5df7aab020feb3eeb59a7f6089b066) } [object](structjson__obj__descr.md#a5d5df7aab020feb3eeb59a7f6089b066);

107 struct {

[ 108](structjson__obj__descr.md#a0a459bf5ad8a210395fe80c5edd72d93) const struct [json\_obj\_descr](structjson__obj__descr.md) \*[element\_descr](structjson__obj__descr.md#a0a459bf5ad8a210395fe80c5edd72d93);

[ 109](structjson__obj__descr.md#ace6558c5156a76658d8835fd5e65ee52) size\_t [n\_elements](structjson__obj__descr.md#ace6558c5156a76658d8835fd5e65ee52);

[ 110](structjson__obj__descr.md#ac12783b89f5507bef7fa3da2c56d1d61) } [array](structjson__obj__descr.md#ac12783b89f5507bef7fa3da2c56d1d61);

111 };

112};

113

[ 126](group__json.md#gacb409ebe9c59789a5d9aca02c6c94674)typedef int (\*[json\_append\_bytes\_t](group__json.md#gacb409ebe9c59789a5d9aca02c6c94674))(const char \*bytes, size\_t len,

127 void \*data);

128

129#define Z\_ALIGN\_SHIFT(type) (\_\_alignof\_\_(type) == 1 ? 0 : \

130 \_\_alignof\_\_(type) == 2 ? 1 : \

131 \_\_alignof\_\_(type) == 4 ? 2 : 3)

132

[ 153](group__json.md#ga1ed917f5a247ca33f2778afe62ff1a88)#define JSON\_OBJ\_DESCR\_PRIM(struct\_, field\_name\_, type\_) \

154 { \

155 .field\_name = (#field\_name\_), \

156 .align\_shift = Z\_ALIGN\_SHIFT(struct\_), \

157 .field\_name\_len = sizeof(#field\_name\_) - 1, \

158 .type = type\_, \

159 .offset = offsetof(struct\_, field\_name\_), \

160 }

161

[ 186](group__json.md#ga4ee365f43cfa86a214973defe81f1e88)#define JSON\_OBJ\_DESCR\_OBJECT(struct\_, field\_name\_, sub\_descr\_) \

187 { \

188 .field\_name = (#field\_name\_), \

189 .align\_shift = Z\_ALIGN\_SHIFT(struct\_), \

190 .field\_name\_len = (sizeof(#field\_name\_) - 1), \

191 .type = JSON\_TOK\_OBJECT\_START, \

192 .offset = offsetof(struct\_, field\_name\_), \

193 .object = { \

194 .sub\_descr = sub\_descr\_, \

195 .sub\_descr\_len = ARRAY\_SIZE(sub\_descr\_), \

196 }, \

197 }

198

208#define Z\_JSON\_ELEMENT\_DESCR(struct\_, len\_field\_, elem\_type\_, union\_) \

209 (const struct json\_obj\_descr[]) \

210 { \

211 { \

212 .align\_shift = Z\_ALIGN\_SHIFT(struct\_), \

213 .type = elem\_type\_, \

214 .offset = offsetof(struct\_, len\_field\_), \

215 union\_ \

216 } \

217 }

218

225#define Z\_JSON\_DESCR\_ARRAY(elem\_descr\_, elem\_descr\_len\_) \

226 { \

227 .array = { \

228 .element\_descr = elem\_descr\_, \

229 .n\_elements = elem\_descr\_len\_, \

230 }, \

231 }

232

239#define Z\_JSON\_DESCR\_OBJ(elem\_descr\_, elem\_descr\_len\_) \

240 { \

241 .object = { \

242 .sub\_descr = elem\_descr\_, \

243 .sub\_descr\_len = elem\_descr\_len\_, \

244 }, \

245 }

246

[ 269](group__json.md#ga0b510decbc755c82903b54fcbc4a3b64)#define JSON\_OBJ\_DESCR\_ARRAY(struct\_, field\_name\_, max\_len\_, \

270 len\_field\_, elem\_type\_) \

271 { \

272 .field\_name = (#field\_name\_), \

273 .align\_shift = Z\_ALIGN\_SHIFT(struct\_), \

274 .field\_name\_len = sizeof(#field\_name\_) - 1, \

275 .type = JSON\_TOK\_ARRAY\_START, \

276 .offset = offsetof(struct\_, field\_name\_), \

277 .array = { \

278 .element\_descr = Z\_JSON\_ELEMENT\_DESCR(struct\_, len\_field\_, \

279 elem\_type\_,), \

280 .n\_elements = (max\_len\_), \

281 }, \

282 }

283

[ 318](group__json.md#gae012264df03546a1c01eec4216b52ffd)#define JSON\_OBJ\_DESCR\_OBJ\_ARRAY(struct\_, field\_name\_, max\_len\_, \

319 len\_field\_, elem\_descr\_, elem\_descr\_len\_) \

320 { \

321 .field\_name = (#field\_name\_), \

322 .align\_shift = Z\_ALIGN\_SHIFT(struct\_), \

323 .field\_name\_len = sizeof(#field\_name\_) - 1, \

324 .type = JSON\_TOK\_ARRAY\_START, \

325 .offset = offsetof(struct\_, field\_name\_), \

326 .array = { \

327 .element\_descr = Z\_JSON\_ELEMENT\_DESCR(struct\_, len\_field\_, \

328 JSON\_TOK\_OBJECT\_START, \

329 Z\_JSON\_DESCR\_OBJ(elem\_descr\_, elem\_descr\_len\_)), \

330 .n\_elements = (max\_len\_), \

331 }, \

332 }

333

[ 377](group__json.md#gaed8189235fd30d2bc041cafee9591ec9)#define JSON\_OBJ\_DESCR\_ARRAY\_ARRAY(struct\_, field\_name\_, max\_len\_, len\_field\_, \

378 elem\_descr\_, elem\_descr\_len\_) \

379 { \

380 .field\_name = (#field\_name\_), \

381 .align\_shift = Z\_ALIGN\_SHIFT(struct\_), \

382 .field\_name\_len = sizeof(#field\_name\_) - 1, \

383 .type = JSON\_TOK\_ARRAY\_START, \

384 .offset = offsetof(struct\_, field\_name\_), \

385 .array = { \

386 .element\_descr = Z\_JSON\_ELEMENT\_DESCR( \

387 struct\_, len\_field\_, JSON\_TOK\_ARRAY\_START, \

388 Z\_JSON\_DESCR\_ARRAY( \

389 elem\_descr\_, \

390 1 + ZERO\_OR\_COMPILE\_ERROR(elem\_descr\_len\_ == 1))), \

391 .n\_elements = (max\_len\_), \

392 }, \

393 }

394

[ 412](group__json.md#ga9fea9111ac1024c8feb066cd53a4045b)#define JSON\_OBJ\_DESCR\_ARRAY\_ARRAY\_NAMED(struct\_, json\_field\_name\_, struct\_field\_name\_, \

413 max\_len\_, len\_field\_, elem\_descr\_, elem\_descr\_len\_) \

414 { \

415 .field\_name = (#json\_field\_name\_), \

416 .align\_shift = Z\_ALIGN\_SHIFT(struct\_), \

417 .field\_name\_len = sizeof(#json\_field\_name\_) - 1, \

418 .type = JSON\_TOK\_ARRAY\_START, \

419 .offset = offsetof(struct\_, struct\_field\_name\_), \

420 .array = { \

421 .element\_descr = Z\_JSON\_ELEMENT\_DESCR( \

422 struct\_, len\_field\_, JSON\_TOK\_ARRAY\_START, \

423 Z\_JSON\_DESCR\_ARRAY( \

424 elem\_descr\_, \

425 1 + ZERO\_OR\_COMPILE\_ERROR(elem\_descr\_len\_ == 1))), \

426 .n\_elements = (max\_len\_), \

427 }, \

428 }

429

[ 444](group__json.md#gaad081c4f8debcb41779bd5879ed8bbd4)#define JSON\_OBJ\_DESCR\_PRIM\_NAMED(struct\_, json\_field\_name\_, \

445 struct\_field\_name\_, type\_) \

446 { \

447 .field\_name = (json\_field\_name\_), \

448 .align\_shift = Z\_ALIGN\_SHIFT(struct\_), \

449 .field\_name\_len = sizeof(json\_field\_name\_) - 1, \

450 .type = type\_, \

451 .offset = offsetof(struct\_, struct\_field\_name\_), \

452 }

453

[ 467](group__json.md#ga8f8d03241e4f69d5f7147792db9a9fe9)#define JSON\_OBJ\_DESCR\_OBJECT\_NAMED(struct\_, json\_field\_name\_, \

468 struct\_field\_name\_, sub\_descr\_) \

469 { \

470 .field\_name = (json\_field\_name\_), \

471 .align\_shift = Z\_ALIGN\_SHIFT(struct\_), \

472 .field\_name\_len = (sizeof(json\_field\_name\_) - 1), \

473 .type = JSON\_TOK\_OBJECT\_START, \

474 .offset = offsetof(struct\_, struct\_field\_name\_), \

475 .object = { \

476 .sub\_descr = sub\_descr\_, \

477 .sub\_descr\_len = ARRAY\_SIZE(sub\_descr\_), \

478 }, \

479 }

480

[ 497](group__json.md#ga4a5bafd64de8abcbc2b5c039bd59ec84)#define JSON\_OBJ\_DESCR\_ARRAY\_NAMED(struct\_, json\_field\_name\_,\

498 struct\_field\_name\_, max\_len\_, len\_field\_, \

499 elem\_type\_) \

500 { \

501 .field\_name = (json\_field\_name\_), \

502 .align\_shift = Z\_ALIGN\_SHIFT(struct\_), \

503 .field\_name\_len = sizeof(json\_field\_name\_) - 1, \

504 .type = JSON\_TOK\_ARRAY\_START, \

505 .offset = offsetof(struct\_, struct\_field\_name\_), \

506 .array = { \

507 .element\_descr = \

508 Z\_JSON\_ELEMENT\_DESCR(struct\_, len\_field\_, elem\_type\_,), \

509 .n\_elements = (max\_len\_), \

510 }, \

511 }

512

[ 553](group__json.md#gaa6602833e59c7e5205d69cc7c4ab2bba)#define JSON\_OBJ\_DESCR\_OBJ\_ARRAY\_NAMED(struct\_, json\_field\_name\_, \

554 struct\_field\_name\_, max\_len\_, \

555 len\_field\_, elem\_descr\_, \

556 elem\_descr\_len\_) \

557 { \

558 .field\_name = json\_field\_name\_, \

559 .align\_shift = Z\_ALIGN\_SHIFT(struct\_), \

560 .field\_name\_len = sizeof(json\_field\_name\_) - 1, \

561 .type = JSON\_TOK\_ARRAY\_START, \

562 .offset = offsetof(struct\_, struct\_field\_name\_), \

563 .array = { \

564 .element\_descr = Z\_JSON\_ELEMENT\_DESCR(struct\_, len\_field\_, \

565 JSON\_TOK\_OBJECT\_START, \

566 Z\_JSON\_DESCR\_OBJ(elem\_descr\_, elem\_descr\_len\_)), \

567 .n\_elements = (max\_len\_), \

568 }, \

569 }

570

[ 601](group__json.md#ga73997fa2154fcbc80f37edd7bcf3477a)[int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) [json\_obj\_parse](group__json.md#ga73997fa2154fcbc80f37edd7bcf3477a)(char \*json, size\_t len,

602 const struct [json\_obj\_descr](structjson__obj__descr.md) \*descr, size\_t descr\_len,

603 void \*val);

604

[ 637](group__json.md#gab4e6ad4a040c271d74eaa313c580a739)int [json\_arr\_parse](group__json.md#gab4e6ad4a040c271d74eaa313c580a739)(char \*json, size\_t len,

638 const struct [json\_obj\_descr](structjson__obj__descr.md) \*descr, void \*val);

639

[ 656](group__json.md#ga6196411958e2e9b3683af4c281214b92)int [json\_arr\_separate\_object\_parse\_init](group__json.md#ga6196411958e2e9b3683af4c281214b92)(struct [json\_obj](structjson__obj.md) \*json, char \*payload, size\_t len);

657

[ 672](group__json.md#ga64859a835e7cb88c2499360fb00ca344)int [json\_arr\_separate\_parse\_object](group__json.md#ga64859a835e7cb88c2499360fb00ca344)(struct [json\_obj](structjson__obj.md) \*json, const struct [json\_obj\_descr](structjson__obj__descr.md) \*descr,

673 size\_t descr\_len, void \*val);

674

[ 687](group__json.md#ga43ee6d1fbd3fa8fb2ae052844b465dda)[ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) [json\_escape](group__json.md#ga43ee6d1fbd3fa8fb2ae052844b465dda)(char \*str, size\_t \*len, size\_t buf\_size);

688

[ 697](group__json.md#ga5ef155a3a6444801592badd6a092734c)size\_t [json\_calc\_escaped\_len](group__json.md#ga5ef155a3a6444801592badd6a092734c)(const char \*str, size\_t len);

698

[ 709](group__json.md#ga41e6e90beef8bae12fca1de2584145bb)[ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) [json\_calc\_encoded\_len](group__json.md#ga41e6e90beef8bae12fca1de2584145bb)(const struct [json\_obj\_descr](structjson__obj__descr.md) \*descr,

710 size\_t descr\_len, const void \*val);

711

[ 721](group__json.md#gad612b8441a21dca34cfeec6257877509)[ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) [json\_calc\_encoded\_arr\_len](group__json.md#gad612b8441a21dca34cfeec6257877509)(const struct [json\_obj\_descr](structjson__obj__descr.md) \*descr,

722 const void \*val);

723

[ 737](group__json.md#gab758ad32cfb6369f4967a6842ac63245)int [json\_obj\_encode\_buf](group__json.md#gab758ad32cfb6369f4967a6842ac63245)(const struct [json\_obj\_descr](structjson__obj__descr.md) \*descr, size\_t descr\_len,

738 const void \*val, char \*buffer, size\_t buf\_size);

739

[ 752](group__json.md#gafd27bbcb898dc902cf1dadd3369cf923)int [json\_arr\_encode\_buf](group__json.md#gafd27bbcb898dc902cf1dadd3369cf923)(const struct [json\_obj\_descr](structjson__obj__descr.md) \*descr, const void \*val,

753 char \*buffer, size\_t buf\_size);

754

[ 768](group__json.md#gafec772f687a0280f5211139bd019e582)int [json\_obj\_encode](group__json.md#gafec772f687a0280f5211139bd019e582)(const struct [json\_obj\_descr](structjson__obj__descr.md) \*descr, size\_t descr\_len,

769 const void \*val, [json\_append\_bytes\_t](group__json.md#gacb409ebe9c59789a5d9aca02c6c94674) append\_bytes,

770 void \*data);

771

[ 784](group__json.md#ga4ffccdc602ab98d489499bf6fa4fa6c5)int [json\_arr\_encode](group__json.md#ga4ffccdc602ab98d489499bf6fa4fa6c5)(const struct [json\_obj\_descr](structjson__obj__descr.md) \*descr, const void \*val,

785 [json\_append\_bytes\_t](group__json.md#gacb409ebe9c59789a5d9aca02c6c94674) append\_bytes, void \*data);

786

787#ifdef \_\_cplusplus

788}

789#endif

790

794#endif /\* ZEPHYR\_INCLUDE\_DATA\_JSON\_H\_ \*/

[json\_tokens](group__json.md#ga18a137ac5e2998d375540298670797c4)

json\_tokens

**Definition** json.h:26

[json\_calc\_encoded\_len](group__json.md#ga41e6e90beef8bae12fca1de2584145bb)

ssize\_t json\_calc\_encoded\_len(const struct json\_obj\_descr \*descr, size\_t descr\_len, const void \*val)

Calculates the string length to fully encode an object.

[json\_escape](group__json.md#ga43ee6d1fbd3fa8fb2ae052844b465dda)

ssize\_t json\_escape(char \*str, size\_t \*len, size\_t buf\_size)

Escapes the string so it can be used to encode JSON objects.

[json\_arr\_encode](group__json.md#ga4ffccdc602ab98d489499bf6fa4fa6c5)

int json\_arr\_encode(const struct json\_obj\_descr \*descr, const void \*val, json\_append\_bytes\_t append\_bytes, void \*data)

Encodes an array using an arbitrary writer function.

[json\_calc\_escaped\_len](group__json.md#ga5ef155a3a6444801592badd6a092734c)

size\_t json\_calc\_escaped\_len(const char \*str, size\_t len)

Calculates the JSON-escaped string length.

[json\_arr\_separate\_object\_parse\_init](group__json.md#ga6196411958e2e9b3683af4c281214b92)

int json\_arr\_separate\_object\_parse\_init(struct json\_obj \*json, char \*payload, size\_t len)

Initialize single-object array parsing.

[json\_arr\_separate\_parse\_object](group__json.md#ga64859a835e7cb88c2499360fb00ca344)

int json\_arr\_separate\_parse\_object(struct json\_obj \*json, const struct json\_obj\_descr \*descr, size\_t descr\_len, void \*val)

Parse a single object from array.

[json\_obj\_parse](group__json.md#ga73997fa2154fcbc80f37edd7bcf3477a)

int64\_t json\_obj\_parse(char \*json, size\_t len, const struct json\_obj\_descr \*descr, size\_t descr\_len, void \*val)

Parses the JSON-encoded object pointed to by json, with size len, according to the descriptor pointed...

[json\_arr\_parse](group__json.md#gab4e6ad4a040c271d74eaa313c580a739)

int json\_arr\_parse(char \*json, size\_t len, const struct json\_obj\_descr \*descr, void \*val)

Parses the JSON-encoded array pointed to by json, with size len, according to the descriptor pointed ...

[json\_obj\_encode\_buf](group__json.md#gab758ad32cfb6369f4967a6842ac63245)

int json\_obj\_encode\_buf(const struct json\_obj\_descr \*descr, size\_t descr\_len, const void \*val, char \*buffer, size\_t buf\_size)

Encodes an object in a contiguous memory location.

[json\_append\_bytes\_t](group__json.md#gacb409ebe9c59789a5d9aca02c6c94674)

int(\* json\_append\_bytes\_t)(const char \*bytes, size\_t len, void \*data)

Function pointer type to append bytes to a buffer while encoding JSON data.

**Definition** json.h:126

[json\_calc\_encoded\_arr\_len](group__json.md#gad612b8441a21dca34cfeec6257877509)

ssize\_t json\_calc\_encoded\_arr\_len(const struct json\_obj\_descr \*descr, const void \*val)

Calculates the string length to fully encode an array.

[json\_arr\_encode\_buf](group__json.md#gafd27bbcb898dc902cf1dadd3369cf923)

int json\_arr\_encode\_buf(const struct json\_obj\_descr \*descr, const void \*val, char \*buffer, size\_t buf\_size)

Encodes an array in a contiguous memory location.

[json\_obj\_encode](group__json.md#gafec772f687a0280f5211139bd019e582)

int json\_obj\_encode(const struct json\_obj\_descr \*descr, size\_t descr\_len, const void \*val, json\_append\_bytes\_t append\_bytes, void \*data)

Encodes an object using an arbitrary writer function.

[JSON\_TOK\_OBJ\_ARRAY](group__json.md#gga18a137ac5e2998d375540298670797c4a14739d9c36212d3df0007427b7b99e25)

@ JSON\_TOK\_OBJ\_ARRAY

**Definition** json.h:43

[JSON\_TOK\_ARRAY\_END](group__json.md#gga18a137ac5e2998d375540298670797c4a2483f21d814abcd08b5253e55aef70c9)

@ JSON\_TOK\_ARRAY\_END

**Definition** json.h:36

[JSON\_TOK\_INT64](group__json.md#gga18a137ac5e2998d375540298670797c4a37f98b21d196182fd2b8cd4c71ed607e)

@ JSON\_TOK\_INT64

**Definition** json.h:45

[JSON\_TOK\_COLON](group__json.md#gga18a137ac5e2998d375540298670797c4a4873e5c0c6344323d5d6af158952ca36)

@ JSON\_TOK\_COLON

**Definition** json.h:38

[JSON\_TOK\_UINT64](group__json.md#gga18a137ac5e2998d375540298670797c4a6218cd0d5d8a34cf4b32797f361b5a41)

@ JSON\_TOK\_UINT64

**Definition** json.h:46

[JSON\_TOK\_COMMA](group__json.md#gga18a137ac5e2998d375540298670797c4a736325745f9521f38a68962775e76a50)

@ JSON\_TOK\_COMMA

**Definition** json.h:39

[JSON\_TOK\_OBJECT\_START](group__json.md#gga18a137ac5e2998d375540298670797c4a81e303d23da0b3d8504cc4a7ee7d52e8)

@ JSON\_TOK\_OBJECT\_START

**Definition** json.h:33

[JSON\_TOK\_OBJECT\_END](group__json.md#gga18a137ac5e2998d375540298670797c4a835bc516b25eb0619b3f1a52f1ebc911)

@ JSON\_TOK\_OBJECT\_END

**Definition** json.h:34

[JSON\_TOK\_TRUE](group__json.md#gga18a137ac5e2998d375540298670797c4a87ffb12e4d174bb4427d9a72eabca7e3)

@ JSON\_TOK\_TRUE

**Definition** json.h:47

[JSON\_TOK\_FALSE](group__json.md#gga18a137ac5e2998d375540298670797c4a8df1b1d0061d7e289f94bae1df35baa7)

@ JSON\_TOK\_FALSE

**Definition** json.h:48

[JSON\_TOK\_NONE](group__json.md#gga18a137ac5e2998d375540298670797c4a926d6b0a5458be2e707d51f0b25dbe77)

@ JSON\_TOK\_NONE

**Definition** json.h:32

[JSON\_TOK\_NULL](group__json.md#gga18a137ac5e2998d375540298670797c4a93de1b7e780ac22744c97e922de3b35e)

@ JSON\_TOK\_NULL

**Definition** json.h:49

[JSON\_TOK\_OPAQUE](group__json.md#gga18a137ac5e2998d375540298670797c4a94ef68b273a74244acb3bdec99b6a024)

@ JSON\_TOK\_OPAQUE

**Definition** json.h:42

[JSON\_TOK\_ARRAY\_START](group__json.md#gga18a137ac5e2998d375540298670797c4a9856446d3a2aa3155266957b8b1371cd)

@ JSON\_TOK\_ARRAY\_START

**Definition** json.h:35

[JSON\_TOK\_FLOAT](group__json.md#gga18a137ac5e2998d375540298670797c4aa842c96d114ed77ab66446bcac1424b5)

@ JSON\_TOK\_FLOAT

**Definition** json.h:41

[JSON\_TOK\_STRING](group__json.md#gga18a137ac5e2998d375540298670797c4ab145f07a93c4fdcf60c9052fbd9a7afc)

@ JSON\_TOK\_STRING

**Definition** json.h:37

[JSON\_TOK\_EOF](group__json.md#gga18a137ac5e2998d375540298670797c4ad970b7d8553296bf4ed03c831cb6f604)

@ JSON\_TOK\_EOF

**Definition** json.h:51

[JSON\_TOK\_NUMBER](group__json.md#gga18a137ac5e2998d375540298670797c4ae25f16ae591eb17d4074e6dcc2f1e62c)

@ JSON\_TOK\_NUMBER

**Definition** json.h:40

[JSON\_TOK\_ENCODED\_OBJ](group__json.md#gga18a137ac5e2998d375540298670797c4af1e451cb321c805cff8fcde3561d3e64)

@ JSON\_TOK\_ENCODED\_OBJ

**Definition** json.h:44

[JSON\_TOK\_ERROR](group__json.md#gga18a137ac5e2998d375540298670797c4afe9c51f453d7dd02504071330a030e9e)

@ JSON\_TOK\_ERROR

**Definition** json.h:50

[types.h](include_2zephyr_2types_8h.md)

[types.h](lib_2libc_2minimal_2include_2sys_2types_8h.md)

[ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118)

\_\_SIZE\_TYPE\_\_ ssize\_t

**Definition** types.h:28

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b)

\_\_INT64\_TYPE\_\_ int64\_t

**Definition** stdint.h:75

[json\_lexer](structjson__lexer.md)

**Definition** json.h:60

[json\_lexer::pos](structjson__lexer.md#a9b403c5505e9a2cd9e475416b2e7f0ac)

char \* pos

**Definition** json.h:63

[json\_lexer::start](structjson__lexer.md#aa4d4a29301fb840c691bbfa416474de4)

char \* start

**Definition** json.h:62

[json\_lexer::tok](structjson__lexer.md#ab285bc72bf12a4de31b45ac0fc992620)

struct json\_token tok

**Definition** json.h:65

[json\_lexer::end](structjson__lexer.md#aeaf5743a9285e0aef9df99f9b3b48320)

char \* end

**Definition** json.h:64

[json\_obj\_descr](structjson__obj__descr.md)

**Definition** json.h:78

[json\_obj\_descr::element\_descr](structjson__obj__descr.md#a0a459bf5ad8a210395fe80c5edd72d93)

const struct json\_obj\_descr \* element\_descr

**Definition** json.h:108

[json\_obj\_descr::field\_name](structjson__obj__descr.md#a2120b7752253ece0beddcaf4c57d3ed8)

const char \* field\_name

**Definition** json.h:79

[json\_obj\_descr::align\_shift](structjson__obj__descr.md#a475717ac4dd01296c01468450e50f75b)

uint32\_t align\_shift

**Definition** json.h:86

[json\_obj\_descr::sub\_descr](structjson__obj__descr.md#a4f5e97c654d0c5e21f1efb5a01966e56)

const struct json\_obj\_descr \* sub\_descr

**Definition** json.h:104

[json\_obj\_descr::object](structjson__obj__descr.md#a5d5df7aab020feb3eeb59a7f6089b066)

struct json\_obj\_descr::@365376074033132355222002170203261307250366002126::@000230262224034312357266150225204112257263011374 object

[json\_obj\_descr::field\_name\_len](structjson__obj__descr.md#a602bf4d8bb5d47c8edb40963ea8ba42f)

uint32\_t field\_name\_len

**Definition** json.h:89

[json\_obj\_descr::offset](structjson__obj__descr.md#a8c6f3eae5e678b8b8ef1957c46f488f1)

uint32\_t offset

**Definition** json.h:100

[json\_obj\_descr::type](structjson__obj__descr.md#a975e998d3ec36f234f09aa2d0d116c9c)

uint32\_t type

**Definition** json.h:97

[json\_obj\_descr::array](structjson__obj__descr.md#ac12783b89f5507bef7fa3da2c56d1d61)

struct json\_obj\_descr::@365376074033132355222002170203261307250366002126::@365235374054153265207136004206377347035314130057 array

[json\_obj\_descr::n\_elements](structjson__obj__descr.md#ace6558c5156a76658d8835fd5e65ee52)

size\_t n\_elements

**Definition** json.h:109

[json\_obj\_descr::sub\_descr\_len](structjson__obj__descr.md#adea0b44d1552305df9dce70074044ba1)

size\_t sub\_descr\_len

**Definition** json.h:105

[json\_obj\_token](structjson__obj__token.md)

**Definition** json.h:72

[json\_obj\_token::length](structjson__obj__token.md#ac996ab0b850803998a37025b57051144)

size\_t length

**Definition** json.h:74

[json\_obj\_token::start](structjson__obj__token.md#aef14abe1f0cefda6bd89d058787550b1)

char \* start

**Definition** json.h:73

[json\_obj](structjson__obj.md)

**Definition** json.h:68

[json\_obj::lex](structjson__obj.md#a7a48a2dca53ee74e7c8eb4727af0e33a)

struct json\_lexer lex

**Definition** json.h:69

[json\_token](structjson__token.md)

**Definition** json.h:54

[json\_token::start](structjson__token.md#a606e33f699c3ec5a66f450cc1777b3c2)

char \* start

**Definition** json.h:56

[json\_token::type](structjson__token.md#ab163615cc3a39191d5a48e900c579e94)

enum json\_tokens type

**Definition** json.h:55

[json\_token::end](structjson__token.md#abb55042d9343358e85311ea52cacb963)

char \* end

**Definition** json.h:57

[util.h](sys_2util_8h.md)

Misc utilities.

[toolchain.h](toolchain_8h.md)

Macros to abstract toolchain specific capabilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [data](dir_f6906818b29bc0a2a087f651f21ae7e0.md)
- [json.h](json_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
