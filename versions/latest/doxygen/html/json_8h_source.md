---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/json_8h_source.html
original_path: doxygen/html/json_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
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

10#include <[zephyr/sys/util.h](util_8h.md)>

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

35 /\* JSON\_TOK\_LIST\_START will be removed use JSON\_TOK\_ARRAY\_START \*/

[ 36](group__json.md#gga18a137ac5e2998d375540298670797c4a8f9beceabf104da239f713e23b91d76b) [JSON\_TOK\_LIST\_START](group__json.md#gga18a137ac5e2998d375540298670797c4a8f9beceabf104da239f713e23b91d76b) \_\_deprecated = '[',

[ 37](group__json.md#gga18a137ac5e2998d375540298670797c4a9856446d3a2aa3155266957b8b1371cd) [JSON\_TOK\_ARRAY\_START](group__json.md#gga18a137ac5e2998d375540298670797c4a9856446d3a2aa3155266957b8b1371cd) = '[',

38 /\* JSON\_TOK\_LIST\_END will be removed use JSON\_TOK\_ARRAY\_END \*/

[ 39](group__json.md#gga18a137ac5e2998d375540298670797c4a5e90a7b034a4af48a1b90fad7675a88d) [JSON\_TOK\_LIST\_END](group__json.md#gga18a137ac5e2998d375540298670797c4a5e90a7b034a4af48a1b90fad7675a88d) \_\_deprecated = ']',

[ 40](group__json.md#gga18a137ac5e2998d375540298670797c4a2483f21d814abcd08b5253e55aef70c9) [JSON\_TOK\_ARRAY\_END](group__json.md#gga18a137ac5e2998d375540298670797c4a2483f21d814abcd08b5253e55aef70c9) = ']',

[ 41](group__json.md#gga18a137ac5e2998d375540298670797c4ab145f07a93c4fdcf60c9052fbd9a7afc) [JSON\_TOK\_STRING](group__json.md#gga18a137ac5e2998d375540298670797c4ab145f07a93c4fdcf60c9052fbd9a7afc) = '"',

[ 42](group__json.md#gga18a137ac5e2998d375540298670797c4a4873e5c0c6344323d5d6af158952ca36) [JSON\_TOK\_COLON](group__json.md#gga18a137ac5e2998d375540298670797c4a4873e5c0c6344323d5d6af158952ca36) = ':',

[ 43](group__json.md#gga18a137ac5e2998d375540298670797c4a736325745f9521f38a68962775e76a50) [JSON\_TOK\_COMMA](group__json.md#gga18a137ac5e2998d375540298670797c4a736325745f9521f38a68962775e76a50) = ',',

[ 44](group__json.md#gga18a137ac5e2998d375540298670797c4ae25f16ae591eb17d4074e6dcc2f1e62c) [JSON\_TOK\_NUMBER](group__json.md#gga18a137ac5e2998d375540298670797c4ae25f16ae591eb17d4074e6dcc2f1e62c) = '0',

[ 45](group__json.md#gga18a137ac5e2998d375540298670797c4aa842c96d114ed77ab66446bcac1424b5) [JSON\_TOK\_FLOAT](group__json.md#gga18a137ac5e2998d375540298670797c4aa842c96d114ed77ab66446bcac1424b5) = '1',

[ 46](group__json.md#gga18a137ac5e2998d375540298670797c4a94ef68b273a74244acb3bdec99b6a024) [JSON\_TOK\_OPAQUE](group__json.md#gga18a137ac5e2998d375540298670797c4a94ef68b273a74244acb3bdec99b6a024) = '2',

[ 47](group__json.md#gga18a137ac5e2998d375540298670797c4a14739d9c36212d3df0007427b7b99e25) [JSON\_TOK\_OBJ\_ARRAY](group__json.md#gga18a137ac5e2998d375540298670797c4a14739d9c36212d3df0007427b7b99e25) = '3',

[ 48](group__json.md#gga18a137ac5e2998d375540298670797c4a87ffb12e4d174bb4427d9a72eabca7e3) [JSON\_TOK\_TRUE](group__json.md#gga18a137ac5e2998d375540298670797c4a87ffb12e4d174bb4427d9a72eabca7e3) = 't',

[ 49](group__json.md#gga18a137ac5e2998d375540298670797c4a8df1b1d0061d7e289f94bae1df35baa7) [JSON\_TOK\_FALSE](group__json.md#gga18a137ac5e2998d375540298670797c4a8df1b1d0061d7e289f94bae1df35baa7) = 'f',

[ 50](group__json.md#gga18a137ac5e2998d375540298670797c4a93de1b7e780ac22744c97e922de3b35e) [JSON\_TOK\_NULL](group__json.md#gga18a137ac5e2998d375540298670797c4a93de1b7e780ac22744c97e922de3b35e) = 'n',

[ 51](group__json.md#gga18a137ac5e2998d375540298670797c4afe9c51f453d7dd02504071330a030e9e) [JSON\_TOK\_ERROR](group__json.md#gga18a137ac5e2998d375540298670797c4afe9c51f453d7dd02504071330a030e9e) = '!',

[ 52](group__json.md#gga18a137ac5e2998d375540298670797c4ad970b7d8553296bf4ed03c831cb6f604) [JSON\_TOK\_EOF](group__json.md#gga18a137ac5e2998d375540298670797c4ad970b7d8553296bf4ed03c831cb6f604) = '\0',

53};

54

[ 55](structjson__token.md)struct [json\_token](structjson__token.md) {

[ 56](structjson__token.md#ab163615cc3a39191d5a48e900c579e94) enum [json\_tokens](group__json.md#ga18a137ac5e2998d375540298670797c4) [type](structjson__token.md#ab163615cc3a39191d5a48e900c579e94);

[ 57](structjson__token.md#a606e33f699c3ec5a66f450cc1777b3c2) char \*[start](structjson__token.md#a606e33f699c3ec5a66f450cc1777b3c2);

[ 58](structjson__token.md#abb55042d9343358e85311ea52cacb963) char \*[end](structjson__token.md#abb55042d9343358e85311ea52cacb963);

59};

60

[ 61](structjson__lexer.md)struct [json\_lexer](structjson__lexer.md) {

[ 62](structjson__lexer.md#ae74beb9d896daf102ec5ffff370830b3) void \*(\*state)(struct [json\_lexer](structjson__lexer.md) \*lex);

[ 63](structjson__lexer.md#aa4d4a29301fb840c691bbfa416474de4) char \*[start](structjson__lexer.md#aa4d4a29301fb840c691bbfa416474de4);

[ 64](structjson__lexer.md#a9b403c5505e9a2cd9e475416b2e7f0ac) char \*[pos](structjson__lexer.md#a9b403c5505e9a2cd9e475416b2e7f0ac);

[ 65](structjson__lexer.md#aeaf5743a9285e0aef9df99f9b3b48320) char \*[end](structjson__lexer.md#aeaf5743a9285e0aef9df99f9b3b48320);

[ 66](structjson__lexer.md#ab285bc72bf12a4de31b45ac0fc992620) struct [json\_token](structjson__token.md) [tok](structjson__lexer.md#ab285bc72bf12a4de31b45ac0fc992620);

67};

68

[ 69](structjson__obj.md)struct [json\_obj](structjson__obj.md) {

[ 70](structjson__obj.md#a7a48a2dca53ee74e7c8eb4727af0e33a) struct [json\_lexer](structjson__lexer.md) [lex](structjson__obj.md#a7a48a2dca53ee74e7c8eb4727af0e33a);

71};

72

[ 73](structjson__obj__token.md)struct [json\_obj\_token](structjson__obj__token.md) {

[ 74](structjson__obj__token.md#aef14abe1f0cefda6bd89d058787550b1) char \*[start](structjson__obj__token.md#aef14abe1f0cefda6bd89d058787550b1);

[ 75](structjson__obj__token.md#ac996ab0b850803998a37025b57051144) size\_t [length](structjson__obj__token.md#ac996ab0b850803998a37025b57051144);

76};

77

78

[ 79](structjson__obj__descr.md)struct [json\_obj\_descr](structjson__obj__descr.md) {

[ 80](structjson__obj__descr.md#a2120b7752253ece0beddcaf4c57d3ed8) const char \*[field\_name](structjson__obj__descr.md#a2120b7752253ece0beddcaf4c57d3ed8);

81

82 /\* Alignment can be 1, 2, 4, or 8. The macros to create

83 \* a struct json\_obj\_descr will store the alignment's

84 \* power of 2 in order to keep this value in the 0-3 range

85 \* and thus use only 2 bits.

86 \*/

[ 87](structjson__obj__descr.md#a475717ac4dd01296c01468450e50f75b) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [align\_shift](structjson__obj__descr.md#a475717ac4dd01296c01468450e50f75b) : 2;

88

89 /\* 127 characters is more than enough for a field name. \*/

[ 90](structjson__obj__descr.md#a602bf4d8bb5d47c8edb40963ea8ba42f) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [field\_name\_len](structjson__obj__descr.md#a602bf4d8bb5d47c8edb40963ea8ba42f) : 7;

91

92 /\* Valid values here (enum json\_tokens): JSON\_TOK\_STRING,

93 \* JSON\_TOK\_NUMBER, JSON\_TOK\_TRUE, JSON\_TOK\_FALSE,

94 \* JSON\_TOK\_OBJECT\_START, JSON\_TOK\_ARRAY\_START. (All others

95 \* ignored.) Maximum value is '}' (125), so this has to be 7 bits

96 \* long.

97 \*/

[ 98](structjson__obj__descr.md#a975e998d3ec36f234f09aa2d0d116c9c) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [type](structjson__obj__descr.md#a975e998d3ec36f234f09aa2d0d116c9c) : 7;

99

100 /\* 65535 bytes is more than enough for many JSON payloads. \*/

[ 101](structjson__obj__descr.md#a8c6f3eae5e678b8b8ef1957c46f488f1) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [offset](structjson__obj__descr.md#a8c6f3eae5e678b8b8ef1957c46f488f1) : 16;

102

103 union {

104 struct {

[ 105](structjson__obj__descr.md#a4f5e97c654d0c5e21f1efb5a01966e56) const struct [json\_obj\_descr](structjson__obj__descr.md) \*[sub\_descr](structjson__obj__descr.md#a4f5e97c654d0c5e21f1efb5a01966e56);

[ 106](structjson__obj__descr.md#adea0b44d1552305df9dce70074044ba1) size\_t [sub\_descr\_len](structjson__obj__descr.md#adea0b44d1552305df9dce70074044ba1);

[ 107](structjson__obj__descr.md#a5d5df7aab020feb3eeb59a7f6089b066) } [object](structjson__obj__descr.md#a5d5df7aab020feb3eeb59a7f6089b066);

108 struct {

[ 109](structjson__obj__descr.md#a0a459bf5ad8a210395fe80c5edd72d93) const struct [json\_obj\_descr](structjson__obj__descr.md) \*[element\_descr](structjson__obj__descr.md#a0a459bf5ad8a210395fe80c5edd72d93);

[ 110](structjson__obj__descr.md#ace6558c5156a76658d8835fd5e65ee52) size\_t [n\_elements](structjson__obj__descr.md#ace6558c5156a76658d8835fd5e65ee52);

[ 111](structjson__obj__descr.md#ac12783b89f5507bef7fa3da2c56d1d61) } [array](structjson__obj__descr.md#ac12783b89f5507bef7fa3da2c56d1d61);

112 };

113};

114

[ 127](group__json.md#gacb409ebe9c59789a5d9aca02c6c94674)typedef int (\*[json\_append\_bytes\_t](group__json.md#gacb409ebe9c59789a5d9aca02c6c94674))(const char \*bytes, size\_t len,

128 void \*data);

129

130#define Z\_ALIGN\_SHIFT(type) (\_\_alignof\_\_(type) == 1 ? 0 : \

131 \_\_alignof\_\_(type) == 2 ? 1 : \

132 \_\_alignof\_\_(type) == 4 ? 2 : 3)

133

[ 154](group__json.md#ga1ed917f5a247ca33f2778afe62ff1a88)#define JSON\_OBJ\_DESCR\_PRIM(struct\_, field\_name\_, type\_) \

155 { \

156 .field\_name = (#field\_name\_), \

157 .align\_shift = Z\_ALIGN\_SHIFT(struct\_), \

158 .field\_name\_len = sizeof(#field\_name\_) - 1, \

159 .type = type\_, \

160 .offset = offsetof(struct\_, field\_name\_), \

161 }

162

[ 187](group__json.md#ga4ee365f43cfa86a214973defe81f1e88)#define JSON\_OBJ\_DESCR\_OBJECT(struct\_, field\_name\_, sub\_descr\_) \

188 { \

189 .field\_name = (#field\_name\_), \

190 .align\_shift = Z\_ALIGN\_SHIFT(struct\_), \

191 .field\_name\_len = (sizeof(#field\_name\_) - 1), \

192 .type = JSON\_TOK\_OBJECT\_START, \

193 .offset = offsetof(struct\_, field\_name\_), \

194 { \

195 .object = { \

196 .sub\_descr = sub\_descr\_, \

197 .sub\_descr\_len = ARRAY\_SIZE(sub\_descr\_), \

198 }, \

199 }, \

200 }

201

211#define Z\_JSON\_ELEMENT\_DESCR(struct\_, len\_field\_, elem\_type\_, union\_) \

212 (const struct json\_obj\_descr[]) \

213 { \

214 { \

215 .align\_shift = Z\_ALIGN\_SHIFT(struct\_), \

216 .type = elem\_type\_, \

217 .offset = offsetof(struct\_, len\_field\_), \

218 union\_ \

219 } \

220 }

221

228#define Z\_JSON\_DESCR\_ARRAY(elem\_descr\_, elem\_descr\_len\_) \

229 { \

230 .array = { \

231 .element\_descr = elem\_descr\_, \

232 .n\_elements = elem\_descr\_len\_, \

233 }, \

234 }

235

242#define Z\_JSON\_DESCR\_OBJ(elem\_descr\_, elem\_descr\_len\_) \

243 { \

244 .object = { \

245 .sub\_descr = elem\_descr\_, \

246 .sub\_descr\_len = elem\_descr\_len\_, \

247 }, \

248 }

249

[ 272](group__json.md#ga0b510decbc755c82903b54fcbc4a3b64)#define JSON\_OBJ\_DESCR\_ARRAY(struct\_, field\_name\_, max\_len\_, \

273 len\_field\_, elem\_type\_) \

274 { \

275 .field\_name = (#field\_name\_), \

276 .align\_shift = Z\_ALIGN\_SHIFT(struct\_), \

277 .field\_name\_len = sizeof(#field\_name\_) - 1, \

278 .type = JSON\_TOK\_ARRAY\_START, \

279 .offset = offsetof(struct\_, field\_name\_), \

280 { \

281 .array = { \

282 .element\_descr = Z\_JSON\_ELEMENT\_DESCR(struct\_, len\_field\_, \

283 elem\_type\_,), \

284 .n\_elements = (max\_len\_), \

285 }, \

286 }, \

287 }

288

[ 323](group__json.md#gae012264df03546a1c01eec4216b52ffd)#define JSON\_OBJ\_DESCR\_OBJ\_ARRAY(struct\_, field\_name\_, max\_len\_, \

324 len\_field\_, elem\_descr\_, elem\_descr\_len\_) \

325 { \

326 .field\_name = (#field\_name\_), \

327 .align\_shift = Z\_ALIGN\_SHIFT(struct\_), \

328 .field\_name\_len = sizeof(#field\_name\_) - 1, \

329 .type = JSON\_TOK\_ARRAY\_START, \

330 .offset = offsetof(struct\_, field\_name\_), \

331 { \

332 .array = { \

333 .element\_descr = Z\_JSON\_ELEMENT\_DESCR(struct\_, len\_field\_, \

334 JSON\_TOK\_OBJECT\_START, \

335 Z\_JSON\_DESCR\_OBJ(elem\_descr\_, elem\_descr\_len\_)), \

336 .n\_elements = (max\_len\_), \

337 }, \

338 }, \

339 }

340

[ 384](group__json.md#gaed8189235fd30d2bc041cafee9591ec9)#define JSON\_OBJ\_DESCR\_ARRAY\_ARRAY(struct\_, field\_name\_, max\_len\_, len\_field\_, \

385 elem\_descr\_, elem\_descr\_len\_) \

386 { \

387 .field\_name = (#field\_name\_), \

388 .align\_shift = Z\_ALIGN\_SHIFT(struct\_), \

389 .field\_name\_len = sizeof(#field\_name\_) - 1, \

390 .type = JSON\_TOK\_ARRAY\_START, \

391 .offset = offsetof(struct\_, field\_name\_), \

392 { \

393 .array = { \

394 .element\_descr = Z\_JSON\_ELEMENT\_DESCR( \

395 struct\_, len\_field\_, JSON\_TOK\_ARRAY\_START, \

396 Z\_JSON\_DESCR\_ARRAY( \

397 elem\_descr\_, \

398 1 + ZERO\_OR\_COMPILE\_ERROR(elem\_descr\_len\_ == 1))), \

399 .n\_elements = (max\_len\_), \

400 }, \

401 }, \

402 }

403

[ 421](group__json.md#ga9fea9111ac1024c8feb066cd53a4045b)#define JSON\_OBJ\_DESCR\_ARRAY\_ARRAY\_NAMED(struct\_, json\_field\_name\_, struct\_field\_name\_, \

422 max\_len\_, len\_field\_, elem\_descr\_, elem\_descr\_len\_) \

423 { \

424 .field\_name = (#json\_field\_name\_), \

425 .align\_shift = Z\_ALIGN\_SHIFT(struct\_), \

426 .field\_name\_len = sizeof(#json\_field\_name\_) - 1, \

427 .type = JSON\_TOK\_ARRAY\_START, \

428 .offset = offsetof(struct\_, struct\_field\_name\_), \

429 { \

430 .array = { \

431 .element\_descr = Z\_JSON\_ELEMENT\_DESCR( \

432 struct\_, len\_field\_, JSON\_TOK\_ARRAY\_START, \

433 Z\_JSON\_DESCR\_ARRAY( \

434 elem\_descr\_, \

435 1 + ZERO\_OR\_COMPILE\_ERROR(elem\_descr\_len\_ == 1))), \

436 .n\_elements = (max\_len\_), \

437 }, \

438 }, \

439 }

440

[ 455](group__json.md#gaad081c4f8debcb41779bd5879ed8bbd4)#define JSON\_OBJ\_DESCR\_PRIM\_NAMED(struct\_, json\_field\_name\_, \

456 struct\_field\_name\_, type\_) \

457 { \

458 .field\_name = (json\_field\_name\_), \

459 .align\_shift = Z\_ALIGN\_SHIFT(struct\_), \

460 .field\_name\_len = sizeof(json\_field\_name\_) - 1, \

461 .type = type\_, \

462 .offset = offsetof(struct\_, struct\_field\_name\_), \

463 }

464

[ 478](group__json.md#ga8f8d03241e4f69d5f7147792db9a9fe9)#define JSON\_OBJ\_DESCR\_OBJECT\_NAMED(struct\_, json\_field\_name\_, \

479 struct\_field\_name\_, sub\_descr\_) \

480 { \

481 .field\_name = (json\_field\_name\_), \

482 .align\_shift = Z\_ALIGN\_SHIFT(struct\_), \

483 .field\_name\_len = (sizeof(json\_field\_name\_) - 1), \

484 .type = JSON\_TOK\_OBJECT\_START, \

485 .offset = offsetof(struct\_, struct\_field\_name\_), \

486 { \

487 .object = { \

488 .sub\_descr = sub\_descr\_, \

489 .sub\_descr\_len = ARRAY\_SIZE(sub\_descr\_), \

490 }, \

491 }, \

492 }

493

[ 510](group__json.md#ga4a5bafd64de8abcbc2b5c039bd59ec84)#define JSON\_OBJ\_DESCR\_ARRAY\_NAMED(struct\_, json\_field\_name\_,\

511 struct\_field\_name\_, max\_len\_, len\_field\_, \

512 elem\_type\_) \

513 { \

514 .field\_name = (json\_field\_name\_), \

515 .align\_shift = Z\_ALIGN\_SHIFT(struct\_), \

516 .field\_name\_len = sizeof(json\_field\_name\_) - 1, \

517 .type = JSON\_TOK\_ARRAY\_START, \

518 .offset = offsetof(struct\_, struct\_field\_name\_), \

519 { \

520 .array = { \

521 .element\_descr = \

522 Z\_JSON\_ELEMENT\_DESCR(struct\_, len\_field\_, elem\_type\_,), \

523 .n\_elements = (max\_len\_), \

524 }, \

525 }, \

526 }

527

[ 568](group__json.md#gaa6602833e59c7e5205d69cc7c4ab2bba)#define JSON\_OBJ\_DESCR\_OBJ\_ARRAY\_NAMED(struct\_, json\_field\_name\_, \

569 struct\_field\_name\_, max\_len\_, \

570 len\_field\_, elem\_descr\_, \

571 elem\_descr\_len\_) \

572 { \

573 .field\_name = json\_field\_name\_, \

574 .align\_shift = Z\_ALIGN\_SHIFT(struct\_), \

575 .field\_name\_len = sizeof(json\_field\_name\_) - 1, \

576 .type = JSON\_TOK\_ARRAY\_START, \

577 .offset = offsetof(struct\_, struct\_field\_name\_), \

578 { \

579 .array = { \

580 .element\_descr = Z\_JSON\_ELEMENT\_DESCR(struct\_, len\_field\_, \

581 JSON\_TOK\_OBJECT\_START, \

582 Z\_JSON\_DESCR\_OBJ(elem\_descr\_, elem\_descr\_len\_)), \

583 .n\_elements = (max\_len\_), \

584 }, \

585 }, \

586 }

587

[ 618](group__json.md#ga73997fa2154fcbc80f37edd7bcf3477a)[int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) [json\_obj\_parse](group__json.md#ga73997fa2154fcbc80f37edd7bcf3477a)(char \*json, size\_t len,

619 const struct [json\_obj\_descr](structjson__obj__descr.md) \*descr, size\_t descr\_len,

620 void \*val);

621

[ 654](group__json.md#gab4e6ad4a040c271d74eaa313c580a739)int [json\_arr\_parse](group__json.md#gab4e6ad4a040c271d74eaa313c580a739)(char \*json, size\_t len,

655 const struct [json\_obj\_descr](structjson__obj__descr.md) \*descr, void \*val);

656

[ 673](group__json.md#ga6196411958e2e9b3683af4c281214b92)int [json\_arr\_separate\_object\_parse\_init](group__json.md#ga6196411958e2e9b3683af4c281214b92)(struct [json\_obj](structjson__obj.md) \*json, char \*payload, size\_t len);

674

[ 689](group__json.md#ga64859a835e7cb88c2499360fb00ca344)int [json\_arr\_separate\_parse\_object](group__json.md#ga64859a835e7cb88c2499360fb00ca344)(struct [json\_obj](structjson__obj.md) \*json, const struct [json\_obj\_descr](structjson__obj__descr.md) \*descr,

690 size\_t descr\_len, void \*val);

691

[ 704](group__json.md#ga43ee6d1fbd3fa8fb2ae052844b465dda)[ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) [json\_escape](group__json.md#ga43ee6d1fbd3fa8fb2ae052844b465dda)(char \*str, size\_t \*len, size\_t buf\_size);

705

[ 714](group__json.md#ga5ef155a3a6444801592badd6a092734c)size\_t [json\_calc\_escaped\_len](group__json.md#ga5ef155a3a6444801592badd6a092734c)(const char \*str, size\_t len);

715

[ 726](group__json.md#ga41e6e90beef8bae12fca1de2584145bb)[ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) [json\_calc\_encoded\_len](group__json.md#ga41e6e90beef8bae12fca1de2584145bb)(const struct [json\_obj\_descr](structjson__obj__descr.md) \*descr,

727 size\_t descr\_len, const void \*val);

728

[ 738](group__json.md#gad612b8441a21dca34cfeec6257877509)[ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) [json\_calc\_encoded\_arr\_len](group__json.md#gad612b8441a21dca34cfeec6257877509)(const struct [json\_obj\_descr](structjson__obj__descr.md) \*descr,

739 const void \*val);

740

[ 754](group__json.md#gab758ad32cfb6369f4967a6842ac63245)int [json\_obj\_encode\_buf](group__json.md#gab758ad32cfb6369f4967a6842ac63245)(const struct [json\_obj\_descr](structjson__obj__descr.md) \*descr, size\_t descr\_len,

755 const void \*val, char \*buffer, size\_t buf\_size);

756

[ 769](group__json.md#gafd27bbcb898dc902cf1dadd3369cf923)int [json\_arr\_encode\_buf](group__json.md#gafd27bbcb898dc902cf1dadd3369cf923)(const struct [json\_obj\_descr](structjson__obj__descr.md) \*descr, const void \*val,

770 char \*buffer, size\_t buf\_size);

771

[ 785](group__json.md#gafec772f687a0280f5211139bd019e582)int [json\_obj\_encode](group__json.md#gafec772f687a0280f5211139bd019e582)(const struct [json\_obj\_descr](structjson__obj__descr.md) \*descr, size\_t descr\_len,

786 const void \*val, [json\_append\_bytes\_t](group__json.md#gacb409ebe9c59789a5d9aca02c6c94674) append\_bytes,

787 void \*data);

788

[ 801](group__json.md#ga4ffccdc602ab98d489499bf6fa4fa6c5)int [json\_arr\_encode](group__json.md#ga4ffccdc602ab98d489499bf6fa4fa6c5)(const struct [json\_obj\_descr](structjson__obj__descr.md) \*descr, const void \*val,

802 [json\_append\_bytes\_t](group__json.md#gacb409ebe9c59789a5d9aca02c6c94674) append\_bytes, void \*data);

803

804#ifdef \_\_cplusplus

805}

806#endif

807

811#endif /\* ZEPHYR\_INCLUDE\_DATA\_JSON\_H\_ \*/

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

**Definition** json.h:127

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

**Definition** json.h:47

[JSON\_TOK\_ARRAY\_END](group__json.md#gga18a137ac5e2998d375540298670797c4a2483f21d814abcd08b5253e55aef70c9)

@ JSON\_TOK\_ARRAY\_END

**Definition** json.h:40

[JSON\_TOK\_COLON](group__json.md#gga18a137ac5e2998d375540298670797c4a4873e5c0c6344323d5d6af158952ca36)

@ JSON\_TOK\_COLON

**Definition** json.h:42

[JSON\_TOK\_LIST\_END](group__json.md#gga18a137ac5e2998d375540298670797c4a5e90a7b034a4af48a1b90fad7675a88d)

@ JSON\_TOK\_LIST\_END

**Definition** json.h:39

[JSON\_TOK\_COMMA](group__json.md#gga18a137ac5e2998d375540298670797c4a736325745f9521f38a68962775e76a50)

@ JSON\_TOK\_COMMA

**Definition** json.h:43

[JSON\_TOK\_OBJECT\_START](group__json.md#gga18a137ac5e2998d375540298670797c4a81e303d23da0b3d8504cc4a7ee7d52e8)

@ JSON\_TOK\_OBJECT\_START

**Definition** json.h:33

[JSON\_TOK\_OBJECT\_END](group__json.md#gga18a137ac5e2998d375540298670797c4a835bc516b25eb0619b3f1a52f1ebc911)

@ JSON\_TOK\_OBJECT\_END

**Definition** json.h:34

[JSON\_TOK\_TRUE](group__json.md#gga18a137ac5e2998d375540298670797c4a87ffb12e4d174bb4427d9a72eabca7e3)

@ JSON\_TOK\_TRUE

**Definition** json.h:48

[JSON\_TOK\_FALSE](group__json.md#gga18a137ac5e2998d375540298670797c4a8df1b1d0061d7e289f94bae1df35baa7)

@ JSON\_TOK\_FALSE

**Definition** json.h:49

[JSON\_TOK\_LIST\_START](group__json.md#gga18a137ac5e2998d375540298670797c4a8f9beceabf104da239f713e23b91d76b)

@ JSON\_TOK\_LIST\_START

**Definition** json.h:36

[JSON\_TOK\_NONE](group__json.md#gga18a137ac5e2998d375540298670797c4a926d6b0a5458be2e707d51f0b25dbe77)

@ JSON\_TOK\_NONE

**Definition** json.h:32

[JSON\_TOK\_NULL](group__json.md#gga18a137ac5e2998d375540298670797c4a93de1b7e780ac22744c97e922de3b35e)

@ JSON\_TOK\_NULL

**Definition** json.h:50

[JSON\_TOK\_OPAQUE](group__json.md#gga18a137ac5e2998d375540298670797c4a94ef68b273a74244acb3bdec99b6a024)

@ JSON\_TOK\_OPAQUE

**Definition** json.h:46

[JSON\_TOK\_ARRAY\_START](group__json.md#gga18a137ac5e2998d375540298670797c4a9856446d3a2aa3155266957b8b1371cd)

@ JSON\_TOK\_ARRAY\_START

**Definition** json.h:37

[JSON\_TOK\_FLOAT](group__json.md#gga18a137ac5e2998d375540298670797c4aa842c96d114ed77ab66446bcac1424b5)

@ JSON\_TOK\_FLOAT

**Definition** json.h:45

[JSON\_TOK\_STRING](group__json.md#gga18a137ac5e2998d375540298670797c4ab145f07a93c4fdcf60c9052fbd9a7afc)

@ JSON\_TOK\_STRING

**Definition** json.h:41

[JSON\_TOK\_EOF](group__json.md#gga18a137ac5e2998d375540298670797c4ad970b7d8553296bf4ed03c831cb6f604)

@ JSON\_TOK\_EOF

**Definition** json.h:52

[JSON\_TOK\_NUMBER](group__json.md#gga18a137ac5e2998d375540298670797c4ae25f16ae591eb17d4074e6dcc2f1e62c)

@ JSON\_TOK\_NUMBER

**Definition** json.h:44

[JSON\_TOK\_ERROR](group__json.md#gga18a137ac5e2998d375540298670797c4afe9c51f453d7dd02504071330a030e9e)

@ JSON\_TOK\_ERROR

**Definition** json.h:51

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

**Definition** json.h:61

[json\_lexer::pos](structjson__lexer.md#a9b403c5505e9a2cd9e475416b2e7f0ac)

char \* pos

**Definition** json.h:64

[json\_lexer::start](structjson__lexer.md#aa4d4a29301fb840c691bbfa416474de4)

char \* start

**Definition** json.h:63

[json\_lexer::tok](structjson__lexer.md#ab285bc72bf12a4de31b45ac0fc992620)

struct json\_token tok

**Definition** json.h:66

[json\_lexer::end](structjson__lexer.md#aeaf5743a9285e0aef9df99f9b3b48320)

char \* end

**Definition** json.h:65

[json\_obj\_descr](structjson__obj__descr.md)

**Definition** json.h:79

[json\_obj\_descr::element\_descr](structjson__obj__descr.md#a0a459bf5ad8a210395fe80c5edd72d93)

const struct json\_obj\_descr \* element\_descr

**Definition** json.h:109

[json\_obj\_descr::field\_name](structjson__obj__descr.md#a2120b7752253ece0beddcaf4c57d3ed8)

const char \* field\_name

**Definition** json.h:80

[json\_obj\_descr::align\_shift](structjson__obj__descr.md#a475717ac4dd01296c01468450e50f75b)

uint32\_t align\_shift

**Definition** json.h:87

[json\_obj\_descr::sub\_descr](structjson__obj__descr.md#a4f5e97c654d0c5e21f1efb5a01966e56)

const struct json\_obj\_descr \* sub\_descr

**Definition** json.h:105

[json\_obj\_descr::object](structjson__obj__descr.md#a5d5df7aab020feb3eeb59a7f6089b066)

struct json\_obj\_descr::@365376074033132355222002170203261307250366002126::@000230262224034312357266150225204112257263011374 object

[json\_obj\_descr::field\_name\_len](structjson__obj__descr.md#a602bf4d8bb5d47c8edb40963ea8ba42f)

uint32\_t field\_name\_len

**Definition** json.h:90

[json\_obj\_descr::offset](structjson__obj__descr.md#a8c6f3eae5e678b8b8ef1957c46f488f1)

uint32\_t offset

**Definition** json.h:101

[json\_obj\_descr::type](structjson__obj__descr.md#a975e998d3ec36f234f09aa2d0d116c9c)

uint32\_t type

**Definition** json.h:98

[json\_obj\_descr::array](structjson__obj__descr.md#ac12783b89f5507bef7fa3da2c56d1d61)

struct json\_obj\_descr::@365376074033132355222002170203261307250366002126::@365235374054153265207136004206377347035314130057 array

[json\_obj\_descr::n\_elements](structjson__obj__descr.md#ace6558c5156a76658d8835fd5e65ee52)

size\_t n\_elements

**Definition** json.h:110

[json\_obj\_descr::sub\_descr\_len](structjson__obj__descr.md#adea0b44d1552305df9dce70074044ba1)

size\_t sub\_descr\_len

**Definition** json.h:106

[json\_obj\_token](structjson__obj__token.md)

**Definition** json.h:73

[json\_obj\_token::length](structjson__obj__token.md#ac996ab0b850803998a37025b57051144)

size\_t length

**Definition** json.h:75

[json\_obj\_token::start](structjson__obj__token.md#aef14abe1f0cefda6bd89d058787550b1)

char \* start

**Definition** json.h:74

[json\_obj](structjson__obj.md)

**Definition** json.h:69

[json\_obj::lex](structjson__obj.md#a7a48a2dca53ee74e7c8eb4727af0e33a)

struct json\_lexer lex

**Definition** json.h:70

[json\_token](structjson__token.md)

**Definition** json.h:55

[json\_token::start](structjson__token.md#a606e33f699c3ec5a66f450cc1777b3c2)

char \* start

**Definition** json.h:57

[json\_token::type](structjson__token.md#ab163615cc3a39191d5a48e900c579e94)

enum json\_tokens type

**Definition** json.h:56

[json\_token::end](structjson__token.md#abb55042d9343358e85311ea52cacb963)

char \* end

**Definition** json.h:58

[toolchain.h](toolchain_8h.md)

Macros to abstract toolchain specific capabilities.

[util.h](util_8h.md)

Misc utilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [data](dir_f6906818b29bc0a2a087f651f21ae7e0.md)
- [json.h](json_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
