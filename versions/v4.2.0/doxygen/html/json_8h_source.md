---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/json_8h_source.html
original_path: doxygen/html/json_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
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

[ 38](group__json.md#gga18a137ac5e2998d375540298670797c4a1434ca9f19f4a411ea98e02d8a2cac7f) [JSON\_TOK\_STRING\_BUF](group__json.md#gga18a137ac5e2998d375540298670797c4a1434ca9f19f4a411ea98e02d8a2cac7f) = 's',

[ 39](group__json.md#gga18a137ac5e2998d375540298670797c4a4873e5c0c6344323d5d6af158952ca36) [JSON\_TOK\_COLON](group__json.md#gga18a137ac5e2998d375540298670797c4a4873e5c0c6344323d5d6af158952ca36) = ':',

[ 40](group__json.md#gga18a137ac5e2998d375540298670797c4a736325745f9521f38a68962775e76a50) [JSON\_TOK\_COMMA](group__json.md#gga18a137ac5e2998d375540298670797c4a736325745f9521f38a68962775e76a50) = ',',

[ 41](group__json.md#gga18a137ac5e2998d375540298670797c4ae25f16ae591eb17d4074e6dcc2f1e62c) [JSON\_TOK\_NUMBER](group__json.md#gga18a137ac5e2998d375540298670797c4ae25f16ae591eb17d4074e6dcc2f1e62c) = '0',

[ 42](group__json.md#gga18a137ac5e2998d375540298670797c4aa842c96d114ed77ab66446bcac1424b5) [JSON\_TOK\_FLOAT](group__json.md#gga18a137ac5e2998d375540298670797c4aa842c96d114ed77ab66446bcac1424b5) = '1',

[ 43](group__json.md#gga18a137ac5e2998d375540298670797c4a94ef68b273a74244acb3bdec99b6a024) [JSON\_TOK\_OPAQUE](group__json.md#gga18a137ac5e2998d375540298670797c4a94ef68b273a74244acb3bdec99b6a024) = '2',

[ 44](group__json.md#gga18a137ac5e2998d375540298670797c4a14739d9c36212d3df0007427b7b99e25) [JSON\_TOK\_OBJ\_ARRAY](group__json.md#gga18a137ac5e2998d375540298670797c4a14739d9c36212d3df0007427b7b99e25) = '3',

[ 45](group__json.md#gga18a137ac5e2998d375540298670797c4af1e451cb321c805cff8fcde3561d3e64) [JSON\_TOK\_ENCODED\_OBJ](group__json.md#gga18a137ac5e2998d375540298670797c4af1e451cb321c805cff8fcde3561d3e64) = '4',

[ 46](group__json.md#gga18a137ac5e2998d375540298670797c4a37f98b21d196182fd2b8cd4c71ed607e) [JSON\_TOK\_INT64](group__json.md#gga18a137ac5e2998d375540298670797c4a37f98b21d196182fd2b8cd4c71ed607e) = '5',

[ 47](group__json.md#gga18a137ac5e2998d375540298670797c4a6218cd0d5d8a34cf4b32797f361b5a41) [JSON\_TOK\_UINT64](group__json.md#gga18a137ac5e2998d375540298670797c4a6218cd0d5d8a34cf4b32797f361b5a41) = '6',

[ 48](group__json.md#gga18a137ac5e2998d375540298670797c4aa5cf82525a71c8a9ca8c69c1adb0ff62) [JSON\_TOK\_FLOAT\_FP](group__json.md#gga18a137ac5e2998d375540298670797c4aa5cf82525a71c8a9ca8c69c1adb0ff62) = '7',

[ 49](group__json.md#gga18a137ac5e2998d375540298670797c4a6e273425323ac63abad33f757572219b) [JSON\_TOK\_DOUBLE\_FP](group__json.md#gga18a137ac5e2998d375540298670797c4a6e273425323ac63abad33f757572219b) = '8',

[ 50](group__json.md#gga18a137ac5e2998d375540298670797c4a7f49f406c8204e6d53353e26213d5169) [JSON\_TOK\_INT](group__json.md#gga18a137ac5e2998d375540298670797c4a7f49f406c8204e6d53353e26213d5169) = 'i',

[ 51](group__json.md#gga18a137ac5e2998d375540298670797c4a15a20a35f875a495a7514ae1a7027e75) [JSON\_TOK\_UINT](group__json.md#gga18a137ac5e2998d375540298670797c4a15a20a35f875a495a7514ae1a7027e75) = 'u',

[ 52](group__json.md#gga18a137ac5e2998d375540298670797c4a87ffb12e4d174bb4427d9a72eabca7e3) [JSON\_TOK\_TRUE](group__json.md#gga18a137ac5e2998d375540298670797c4a87ffb12e4d174bb4427d9a72eabca7e3) = 't',

[ 53](group__json.md#gga18a137ac5e2998d375540298670797c4a8df1b1d0061d7e289f94bae1df35baa7) [JSON\_TOK\_FALSE](group__json.md#gga18a137ac5e2998d375540298670797c4a8df1b1d0061d7e289f94bae1df35baa7) = 'f',

[ 54](group__json.md#gga18a137ac5e2998d375540298670797c4a93de1b7e780ac22744c97e922de3b35e) [JSON\_TOK\_NULL](group__json.md#gga18a137ac5e2998d375540298670797c4a93de1b7e780ac22744c97e922de3b35e) = 'n',

[ 55](group__json.md#gga18a137ac5e2998d375540298670797c4afe9c51f453d7dd02504071330a030e9e) [JSON\_TOK\_ERROR](group__json.md#gga18a137ac5e2998d375540298670797c4afe9c51f453d7dd02504071330a030e9e) = '!',

[ 56](group__json.md#gga18a137ac5e2998d375540298670797c4ad970b7d8553296bf4ed03c831cb6f604) [JSON\_TOK\_EOF](group__json.md#gga18a137ac5e2998d375540298670797c4ad970b7d8553296bf4ed03c831cb6f604) = '\0',

57};

58

[ 59](structjson__token.md)struct [json\_token](structjson__token.md) {

[ 60](structjson__token.md#ab163615cc3a39191d5a48e900c579e94) enum [json\_tokens](group__json.md#ga18a137ac5e2998d375540298670797c4) [type](structjson__token.md#ab163615cc3a39191d5a48e900c579e94);

[ 61](structjson__token.md#a606e33f699c3ec5a66f450cc1777b3c2) char \*[start](structjson__token.md#a606e33f699c3ec5a66f450cc1777b3c2);

[ 62](structjson__token.md#abb55042d9343358e85311ea52cacb963) char \*[end](structjson__token.md#abb55042d9343358e85311ea52cacb963);

63};

64

[ 65](structjson__lexer.md)struct [json\_lexer](structjson__lexer.md) {

[ 66](structjson__lexer.md#ae74beb9d896daf102ec5ffff370830b3) void \*(\*state)(struct [json\_lexer](structjson__lexer.md) \*lex);

[ 67](structjson__lexer.md#aa4d4a29301fb840c691bbfa416474de4) char \*[start](structjson__lexer.md#aa4d4a29301fb840c691bbfa416474de4);

[ 68](structjson__lexer.md#a9b403c5505e9a2cd9e475416b2e7f0ac) char \*[pos](structjson__lexer.md#a9b403c5505e9a2cd9e475416b2e7f0ac);

[ 69](structjson__lexer.md#aeaf5743a9285e0aef9df99f9b3b48320) char \*[end](structjson__lexer.md#aeaf5743a9285e0aef9df99f9b3b48320);

[ 70](structjson__lexer.md#ab285bc72bf12a4de31b45ac0fc992620) struct [json\_token](structjson__token.md) [tok](structjson__lexer.md#ab285bc72bf12a4de31b45ac0fc992620);

71};

72

[ 73](structjson__obj.md)struct [json\_obj](structjson__obj.md) {

[ 74](structjson__obj.md#a7a48a2dca53ee74e7c8eb4727af0e33a) struct [json\_lexer](structjson__lexer.md) [lex](structjson__obj.md#a7a48a2dca53ee74e7c8eb4727af0e33a);

75};

76

[ 77](structjson__obj__token.md)struct [json\_obj\_token](structjson__obj__token.md) {

[ 78](structjson__obj__token.md#aef14abe1f0cefda6bd89d058787550b1) char \*[start](structjson__obj__token.md#aef14abe1f0cefda6bd89d058787550b1);

[ 79](structjson__obj__token.md#ac996ab0b850803998a37025b57051144) size\_t [length](structjson__obj__token.md#ac996ab0b850803998a37025b57051144);

80};

81

82

[ 83](structjson__obj__descr.md)struct [json\_obj\_descr](structjson__obj__descr.md) {

[ 84](structjson__obj__descr.md#a2120b7752253ece0beddcaf4c57d3ed8) const char \*[field\_name](structjson__obj__descr.md#a2120b7752253ece0beddcaf4c57d3ed8);

85

86 /\* Alignment can be 1, 2, 4, or 8. The macros to create

87 \* a struct json\_obj\_descr will store the alignment's

88 \* power of 2 in order to keep this value in the 0-3 range

89 \* and thus use only 2 bits.

90 \*/

[ 91](structjson__obj__descr.md#a475717ac4dd01296c01468450e50f75b) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [align\_shift](structjson__obj__descr.md#a475717ac4dd01296c01468450e50f75b) : 2;

92

93 /\* 127 characters is more than enough for a field name. \*/

[ 94](structjson__obj__descr.md#a602bf4d8bb5d47c8edb40963ea8ba42f) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [field\_name\_len](structjson__obj__descr.md#a602bf4d8bb5d47c8edb40963ea8ba42f) : 7;

95

96 /\* Valid values here (enum json\_tokens): JSON\_TOK\_STRING,

97 \* JSON\_TOK\_NUMBER, JSON\_TOK\_TRUE, JSON\_TOK\_FALSE,

98 \* JSON\_TOK\_OBJECT\_START, JSON\_TOK\_ARRAY\_START. (All others

99 \* ignored.) Maximum value is '}' (125), so this has to be 7 bits

100 \* long.

101 \*/

[ 102](structjson__obj__descr.md#a975e998d3ec36f234f09aa2d0d116c9c) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [type](structjson__obj__descr.md#a975e998d3ec36f234f09aa2d0d116c9c) : 7;

103

104 /\* 65535 bytes is more than enough for many JSON payloads. \*/

[ 105](structjson__obj__descr.md#a8c6f3eae5e678b8b8ef1957c46f488f1) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [offset](structjson__obj__descr.md#a8c6f3eae5e678b8b8ef1957c46f488f1) : 16;

106

107 union {

108 struct {

[ 109](structjson__obj__descr.md#a4f5e97c654d0c5e21f1efb5a01966e56) const struct [json\_obj\_descr](structjson__obj__descr.md) \*[sub\_descr](structjson__obj__descr.md#a4f5e97c654d0c5e21f1efb5a01966e56);

[ 110](structjson__obj__descr.md#adea0b44d1552305df9dce70074044ba1) size\_t [sub\_descr\_len](structjson__obj__descr.md#adea0b44d1552305df9dce70074044ba1);

[ 111](structjson__obj__descr.md#a5d5df7aab020feb3eeb59a7f6089b066) } [object](structjson__obj__descr.md#a5d5df7aab020feb3eeb59a7f6089b066);

112 struct {

[ 113](structjson__obj__descr.md#a0a459bf5ad8a210395fe80c5edd72d93) const struct [json\_obj\_descr](structjson__obj__descr.md) \*[element\_descr](structjson__obj__descr.md#a0a459bf5ad8a210395fe80c5edd72d93);

[ 114](structjson__obj__descr.md#ace6558c5156a76658d8835fd5e65ee52) size\_t [n\_elements](structjson__obj__descr.md#ace6558c5156a76658d8835fd5e65ee52);

[ 115](structjson__obj__descr.md#ac12783b89f5507bef7fa3da2c56d1d61) } [array](structjson__obj__descr.md#ac12783b89f5507bef7fa3da2c56d1d61);

116 struct {

[ 117](structjson__obj__descr.md#aa01763bb5316fdce6acc64c7d7d21406) size\_t [size](structjson__obj__descr.md#aa01763bb5316fdce6acc64c7d7d21406);

[ 118](structjson__obj__descr.md#a0449d269cff7813f37066f0381b9e8f5) } [field](structjson__obj__descr.md#a0449d269cff7813f37066f0381b9e8f5);

119 };

120};

121

[ 134](group__json.md#gacb409ebe9c59789a5d9aca02c6c94674)typedef int (\*[json\_append\_bytes\_t](group__json.md#gacb409ebe9c59789a5d9aca02c6c94674))(const char \*bytes, size\_t len,

135 void \*data);

136

137#define Z\_ALIGN\_SHIFT(type) (\_\_alignof\_\_(type) == 1 ? 0 : \

138 \_\_alignof\_\_(type) == 2 ? 1 : \

139 \_\_alignof\_\_(type) == 4 ? 2 : 3)

140

[ 161](group__json.md#ga1ed917f5a247ca33f2778afe62ff1a88)#define JSON\_OBJ\_DESCR\_PRIM(struct\_, field\_name\_, type\_) \

162 { \

163 .field\_name = (#field\_name\_), \

164 .align\_shift = Z\_ALIGN\_SHIFT(struct\_), \

165 .field\_name\_len = sizeof(#field\_name\_) - 1, \

166 .type = type\_, \

167 .offset = offsetof(struct\_, field\_name\_), \

168 .field = { \

169 .size = SIZEOF\_FIELD(struct\_, field\_name\_) \

170 }, \

171 }

172

[ 197](group__json.md#ga4ee365f43cfa86a214973defe81f1e88)#define JSON\_OBJ\_DESCR\_OBJECT(struct\_, field\_name\_, sub\_descr\_) \

198 { \

199 .field\_name = (#field\_name\_), \

200 .align\_shift = Z\_ALIGN\_SHIFT(struct\_), \

201 .field\_name\_len = (sizeof(#field\_name\_) - 1), \

202 .type = JSON\_TOK\_OBJECT\_START, \

203 .offset = offsetof(struct\_, field\_name\_), \

204 .object = { \

205 .sub\_descr = sub\_descr\_, \

206 .sub\_descr\_len = ARRAY\_SIZE(sub\_descr\_), \

207 }, \

208 }

209

219#define Z\_JSON\_ELEMENT\_DESCR(struct\_, len\_field\_, elem\_type\_, union\_) \

220 (const struct json\_obj\_descr[]) \

221 { \

222 { \

223 .align\_shift = Z\_ALIGN\_SHIFT(struct\_), \

224 .type = elem\_type\_, \

225 .offset = offsetof(struct\_, len\_field\_), \

226 union\_ \

227 } \

228 }

229

236#define Z\_JSON\_DESCR\_ARRAY(elem\_descr\_, elem\_descr\_len\_) \

237 { \

238 .array = { \

239 .element\_descr = elem\_descr\_, \

240 .n\_elements = elem\_descr\_len\_, \

241 }, \

242 }

243

250#define Z\_JSON\_DESCR\_OBJ(elem\_descr\_, elem\_descr\_len\_) \

251 .object = { \

252 .sub\_descr = elem\_descr\_, \

253 .sub\_descr\_len = elem\_descr\_len\_, \

254 }, \

255

262#define Z\_JSON\_DESCR\_FIELD(struct\_, field\_name\_) \

263 { \

264 .field = { \

265 .size = SIZEOF\_FIELD(struct\_, field\_name\_), \

266 }, \

267 }

268

[ 291](group__json.md#ga0b510decbc755c82903b54fcbc4a3b64)#define JSON\_OBJ\_DESCR\_ARRAY(struct\_, field\_name\_, max\_len\_, \

292 len\_field\_, elem\_type\_) \

293 { \

294 .field\_name = (#field\_name\_), \

295 .align\_shift = Z\_ALIGN\_SHIFT(struct\_), \

296 .field\_name\_len = sizeof(#field\_name\_) - 1, \

297 .type = JSON\_TOK\_ARRAY\_START, \

298 .offset = offsetof(struct\_, field\_name\_), \

299 .array = { \

300 .element\_descr = Z\_JSON\_ELEMENT\_DESCR(struct\_, len\_field\_, \

301 elem\_type\_, \

302 Z\_JSON\_DESCR\_FIELD(struct\_, field\_name\_[0])), \

303 .n\_elements = (max\_len\_), \

304 }, \

305 }

306

[ 341](group__json.md#gae012264df03546a1c01eec4216b52ffd)#define JSON\_OBJ\_DESCR\_OBJ\_ARRAY(struct\_, field\_name\_, max\_len\_, \

342 len\_field\_, elem\_descr\_, elem\_descr\_len\_) \

343 { \

344 .field\_name = (#field\_name\_), \

345 .align\_shift = Z\_ALIGN\_SHIFT(struct\_), \

346 .field\_name\_len = sizeof(#field\_name\_) - 1, \

347 .type = JSON\_TOK\_ARRAY\_START, \

348 .offset = offsetof(struct\_, field\_name\_), \

349 .array = { \

350 .element\_descr = Z\_JSON\_ELEMENT\_DESCR(struct\_, len\_field\_, \

351 JSON\_TOK\_OBJECT\_START, \

352 Z\_JSON\_DESCR\_OBJ(elem\_descr\_, elem\_descr\_len\_)), \

353 .n\_elements = (max\_len\_), \

354 }, \

355 }

356

[ 400](group__json.md#gaed8189235fd30d2bc041cafee9591ec9)#define JSON\_OBJ\_DESCR\_ARRAY\_ARRAY(struct\_, field\_name\_, max\_len\_, len\_field\_, \

401 elem\_descr\_, elem\_descr\_len\_) \

402 { \

403 .field\_name = (#field\_name\_), \

404 .align\_shift = Z\_ALIGN\_SHIFT(struct\_), \

405 .field\_name\_len = sizeof(#field\_name\_) - 1, \

406 .type = JSON\_TOK\_ARRAY\_START, \

407 .offset = offsetof(struct\_, field\_name\_), \

408 .array = { \

409 .element\_descr = Z\_JSON\_ELEMENT\_DESCR( \

410 struct\_, len\_field\_, JSON\_TOK\_ARRAY\_START, \

411 Z\_JSON\_DESCR\_ARRAY( \

412 elem\_descr\_, \

413 1 + ZERO\_OR\_COMPILE\_ERROR(elem\_descr\_len\_ == 1))), \

414 .n\_elements = (max\_len\_), \

415 }, \

416 }

417

[ 435](group__json.md#ga9fea9111ac1024c8feb066cd53a4045b)#define JSON\_OBJ\_DESCR\_ARRAY\_ARRAY\_NAMED(struct\_, json\_field\_name\_, struct\_field\_name\_, \

436 max\_len\_, len\_field\_, elem\_descr\_, elem\_descr\_len\_) \

437 { \

438 .field\_name = (#json\_field\_name\_), \

439 .align\_shift = Z\_ALIGN\_SHIFT(struct\_), \

440 .field\_name\_len = sizeof(#json\_field\_name\_) - 1, \

441 .type = JSON\_TOK\_ARRAY\_START, \

442 .offset = offsetof(struct\_, struct\_field\_name\_), \

443 .array = { \

444 .element\_descr = Z\_JSON\_ELEMENT\_DESCR( \

445 struct\_, len\_field\_, JSON\_TOK\_ARRAY\_START, \

446 Z\_JSON\_DESCR\_ARRAY( \

447 elem\_descr\_, \

448 1 + ZERO\_OR\_COMPILE\_ERROR(elem\_descr\_len\_ == 1))), \

449 .n\_elements = (max\_len\_), \

450 }, \

451 }

452

[ 467](group__json.md#gaad081c4f8debcb41779bd5879ed8bbd4)#define JSON\_OBJ\_DESCR\_PRIM\_NAMED(struct\_, json\_field\_name\_, \

468 struct\_field\_name\_, type\_) \

469 { \

470 .field\_name = (json\_field\_name\_), \

471 .align\_shift = Z\_ALIGN\_SHIFT(struct\_), \

472 .field\_name\_len = sizeof(json\_field\_name\_) - 1, \

473 .type = type\_, \

474 .offset = offsetof(struct\_, struct\_field\_name\_), \

475 .field = { \

476 .size = SIZEOF\_FIELD(struct\_, struct\_field\_name\_) \

477 }, \

478 }

479

[ 493](group__json.md#ga8f8d03241e4f69d5f7147792db9a9fe9)#define JSON\_OBJ\_DESCR\_OBJECT\_NAMED(struct\_, json\_field\_name\_, \

494 struct\_field\_name\_, sub\_descr\_) \

495 { \

496 .field\_name = (json\_field\_name\_), \

497 .align\_shift = Z\_ALIGN\_SHIFT(struct\_), \

498 .field\_name\_len = (sizeof(json\_field\_name\_) - 1), \

499 .type = JSON\_TOK\_OBJECT\_START, \

500 .offset = offsetof(struct\_, struct\_field\_name\_), \

501 .object = { \

502 .sub\_descr = sub\_descr\_, \

503 .sub\_descr\_len = ARRAY\_SIZE(sub\_descr\_), \

504 }, \

505 }

506

[ 523](group__json.md#ga4a5bafd64de8abcbc2b5c039bd59ec84)#define JSON\_OBJ\_DESCR\_ARRAY\_NAMED(struct\_, json\_field\_name\_,\

524 struct\_field\_name\_, max\_len\_, len\_field\_, \

525 elem\_type\_) \

526 { \

527 .field\_name = (json\_field\_name\_), \

528 .align\_shift = Z\_ALIGN\_SHIFT(struct\_), \

529 .field\_name\_len = sizeof(json\_field\_name\_) - 1, \

530 .type = JSON\_TOK\_ARRAY\_START, \

531 .offset = offsetof(struct\_, struct\_field\_name\_), \

532 .array = { \

533 .element\_descr = Z\_JSON\_ELEMENT\_DESCR(struct\_, len\_field\_, \

534 elem\_type\_, \

535 Z\_JSON\_DESCR\_FIELD(struct\_, struct\_field\_name\_[0])), \

536 .n\_elements = (max\_len\_), \

537 }, \

538 }

539

[ 580](group__json.md#gaa6602833e59c7e5205d69cc7c4ab2bba)#define JSON\_OBJ\_DESCR\_OBJ\_ARRAY\_NAMED(struct\_, json\_field\_name\_, \

581 struct\_field\_name\_, max\_len\_, \

582 len\_field\_, elem\_descr\_, \

583 elem\_descr\_len\_) \

584 { \

585 .field\_name = json\_field\_name\_, \

586 .align\_shift = Z\_ALIGN\_SHIFT(struct\_), \

587 .field\_name\_len = sizeof(json\_field\_name\_) - 1, \

588 .type = JSON\_TOK\_ARRAY\_START, \

589 .offset = offsetof(struct\_, struct\_field\_name\_), \

590 .array = { \

591 .element\_descr = Z\_JSON\_ELEMENT\_DESCR(struct\_, len\_field\_, \

592 JSON\_TOK\_OBJECT\_START, \

593 Z\_JSON\_DESCR\_OBJ(elem\_descr\_, elem\_descr\_len\_)), \

594 .n\_elements = (max\_len\_), \

595 }, \

596 }

597

[ 628](group__json.md#ga73997fa2154fcbc80f37edd7bcf3477a)[int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) [json\_obj\_parse](group__json.md#ga73997fa2154fcbc80f37edd7bcf3477a)(char \*json, size\_t len,

629 const struct [json\_obj\_descr](structjson__obj__descr.md) \*descr, size\_t descr\_len,

630 void \*val);

631

[ 664](group__json.md#gab4e6ad4a040c271d74eaa313c580a739)int [json\_arr\_parse](group__json.md#gab4e6ad4a040c271d74eaa313c580a739)(char \*json, size\_t len,

665 const struct [json\_obj\_descr](structjson__obj__descr.md) \*descr, void \*val);

666

[ 683](group__json.md#ga6196411958e2e9b3683af4c281214b92)int [json\_arr\_separate\_object\_parse\_init](group__json.md#ga6196411958e2e9b3683af4c281214b92)(struct [json\_obj](structjson__obj.md) \*json, char \*payload, size\_t len);

684

[ 699](group__json.md#ga64859a835e7cb88c2499360fb00ca344)int [json\_arr\_separate\_parse\_object](group__json.md#ga64859a835e7cb88c2499360fb00ca344)(struct [json\_obj](structjson__obj.md) \*json, const struct [json\_obj\_descr](structjson__obj__descr.md) \*descr,

700 size\_t descr\_len, void \*val);

701

[ 714](group__json.md#ga43ee6d1fbd3fa8fb2ae052844b465dda)[ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) [json\_escape](group__json.md#ga43ee6d1fbd3fa8fb2ae052844b465dda)(char \*str, size\_t \*len, size\_t buf\_size);

715

[ 724](group__json.md#ga5ef155a3a6444801592badd6a092734c)size\_t [json\_calc\_escaped\_len](group__json.md#ga5ef155a3a6444801592badd6a092734c)(const char \*str, size\_t len);

725

[ 736](group__json.md#ga41e6e90beef8bae12fca1de2584145bb)[ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) [json\_calc\_encoded\_len](group__json.md#ga41e6e90beef8bae12fca1de2584145bb)(const struct [json\_obj\_descr](structjson__obj__descr.md) \*descr,

737 size\_t descr\_len, const void \*val);

738

[ 748](group__json.md#gad612b8441a21dca34cfeec6257877509)[ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) [json\_calc\_encoded\_arr\_len](group__json.md#gad612b8441a21dca34cfeec6257877509)(const struct [json\_obj\_descr](structjson__obj__descr.md) \*descr,

749 const void \*val);

750

[ 764](group__json.md#gab758ad32cfb6369f4967a6842ac63245)int [json\_obj\_encode\_buf](group__json.md#gab758ad32cfb6369f4967a6842ac63245)(const struct [json\_obj\_descr](structjson__obj__descr.md) \*descr, size\_t descr\_len,

765 const void \*val, char \*buffer, size\_t buf\_size);

766

[ 779](group__json.md#gafd27bbcb898dc902cf1dadd3369cf923)int [json\_arr\_encode\_buf](group__json.md#gafd27bbcb898dc902cf1dadd3369cf923)(const struct [json\_obj\_descr](structjson__obj__descr.md) \*descr, const void \*val,

780 char \*buffer, size\_t buf\_size);

781

[ 795](group__json.md#gafec772f687a0280f5211139bd019e582)int [json\_obj\_encode](group__json.md#gafec772f687a0280f5211139bd019e582)(const struct [json\_obj\_descr](structjson__obj__descr.md) \*descr, size\_t descr\_len,

796 const void \*val, [json\_append\_bytes\_t](group__json.md#gacb409ebe9c59789a5d9aca02c6c94674) append\_bytes,

797 void \*data);

798

[ 811](group__json.md#ga4ffccdc602ab98d489499bf6fa4fa6c5)int [json\_arr\_encode](group__json.md#ga4ffccdc602ab98d489499bf6fa4fa6c5)(const struct [json\_obj\_descr](structjson__obj__descr.md) \*descr, const void \*val,

812 [json\_append\_bytes\_t](group__json.md#gacb409ebe9c59789a5d9aca02c6c94674) append\_bytes, void \*data);

813

814#ifdef \_\_cplusplus

815}

816#endif

817

821#endif /\* ZEPHYR\_INCLUDE\_DATA\_JSON\_H\_ \*/

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

**Definition** json.h:134

[json\_calc\_encoded\_arr\_len](group__json.md#gad612b8441a21dca34cfeec6257877509)

ssize\_t json\_calc\_encoded\_arr\_len(const struct json\_obj\_descr \*descr, const void \*val)

Calculates the string length to fully encode an array.

[json\_arr\_encode\_buf](group__json.md#gafd27bbcb898dc902cf1dadd3369cf923)

int json\_arr\_encode\_buf(const struct json\_obj\_descr \*descr, const void \*val, char \*buffer, size\_t buf\_size)

Encodes an array in a contiguous memory location.

[json\_obj\_encode](group__json.md#gafec772f687a0280f5211139bd019e582)

int json\_obj\_encode(const struct json\_obj\_descr \*descr, size\_t descr\_len, const void \*val, json\_append\_bytes\_t append\_bytes, void \*data)

Encodes an object using an arbitrary writer function.

[JSON\_TOK\_STRING\_BUF](group__json.md#gga18a137ac5e2998d375540298670797c4a1434ca9f19f4a411ea98e02d8a2cac7f)

@ JSON\_TOK\_STRING\_BUF

**Definition** json.h:38

[JSON\_TOK\_OBJ\_ARRAY](group__json.md#gga18a137ac5e2998d375540298670797c4a14739d9c36212d3df0007427b7b99e25)

@ JSON\_TOK\_OBJ\_ARRAY

**Definition** json.h:44

[JSON\_TOK\_UINT](group__json.md#gga18a137ac5e2998d375540298670797c4a15a20a35f875a495a7514ae1a7027e75)

@ JSON\_TOK\_UINT

**Definition** json.h:51

[JSON\_TOK\_ARRAY\_END](group__json.md#gga18a137ac5e2998d375540298670797c4a2483f21d814abcd08b5253e55aef70c9)

@ JSON\_TOK\_ARRAY\_END

**Definition** json.h:36

[JSON\_TOK\_INT64](group__json.md#gga18a137ac5e2998d375540298670797c4a37f98b21d196182fd2b8cd4c71ed607e)

@ JSON\_TOK\_INT64

**Definition** json.h:46

[JSON\_TOK\_COLON](group__json.md#gga18a137ac5e2998d375540298670797c4a4873e5c0c6344323d5d6af158952ca36)

@ JSON\_TOK\_COLON

**Definition** json.h:39

[JSON\_TOK\_UINT64](group__json.md#gga18a137ac5e2998d375540298670797c4a6218cd0d5d8a34cf4b32797f361b5a41)

@ JSON\_TOK\_UINT64

**Definition** json.h:47

[JSON\_TOK\_DOUBLE\_FP](group__json.md#gga18a137ac5e2998d375540298670797c4a6e273425323ac63abad33f757572219b)

@ JSON\_TOK\_DOUBLE\_FP

**Definition** json.h:49

[JSON\_TOK\_COMMA](group__json.md#gga18a137ac5e2998d375540298670797c4a736325745f9521f38a68962775e76a50)

@ JSON\_TOK\_COMMA

**Definition** json.h:40

[JSON\_TOK\_INT](group__json.md#gga18a137ac5e2998d375540298670797c4a7f49f406c8204e6d53353e26213d5169)

@ JSON\_TOK\_INT

**Definition** json.h:50

[JSON\_TOK\_OBJECT\_START](group__json.md#gga18a137ac5e2998d375540298670797c4a81e303d23da0b3d8504cc4a7ee7d52e8)

@ JSON\_TOK\_OBJECT\_START

**Definition** json.h:33

[JSON\_TOK\_OBJECT\_END](group__json.md#gga18a137ac5e2998d375540298670797c4a835bc516b25eb0619b3f1a52f1ebc911)

@ JSON\_TOK\_OBJECT\_END

**Definition** json.h:34

[JSON\_TOK\_TRUE](group__json.md#gga18a137ac5e2998d375540298670797c4a87ffb12e4d174bb4427d9a72eabca7e3)

@ JSON\_TOK\_TRUE

**Definition** json.h:52

[JSON\_TOK\_FALSE](group__json.md#gga18a137ac5e2998d375540298670797c4a8df1b1d0061d7e289f94bae1df35baa7)

@ JSON\_TOK\_FALSE

**Definition** json.h:53

[JSON\_TOK\_NONE](group__json.md#gga18a137ac5e2998d375540298670797c4a926d6b0a5458be2e707d51f0b25dbe77)

@ JSON\_TOK\_NONE

**Definition** json.h:32

[JSON\_TOK\_NULL](group__json.md#gga18a137ac5e2998d375540298670797c4a93de1b7e780ac22744c97e922de3b35e)

@ JSON\_TOK\_NULL

**Definition** json.h:54

[JSON\_TOK\_OPAQUE](group__json.md#gga18a137ac5e2998d375540298670797c4a94ef68b273a74244acb3bdec99b6a024)

@ JSON\_TOK\_OPAQUE

**Definition** json.h:43

[JSON\_TOK\_ARRAY\_START](group__json.md#gga18a137ac5e2998d375540298670797c4a9856446d3a2aa3155266957b8b1371cd)

@ JSON\_TOK\_ARRAY\_START

**Definition** json.h:35

[JSON\_TOK\_FLOAT\_FP](group__json.md#gga18a137ac5e2998d375540298670797c4aa5cf82525a71c8a9ca8c69c1adb0ff62)

@ JSON\_TOK\_FLOAT\_FP

**Definition** json.h:48

[JSON\_TOK\_FLOAT](group__json.md#gga18a137ac5e2998d375540298670797c4aa842c96d114ed77ab66446bcac1424b5)

@ JSON\_TOK\_FLOAT

**Definition** json.h:42

[JSON\_TOK\_STRING](group__json.md#gga18a137ac5e2998d375540298670797c4ab145f07a93c4fdcf60c9052fbd9a7afc)

@ JSON\_TOK\_STRING

**Definition** json.h:37

[JSON\_TOK\_EOF](group__json.md#gga18a137ac5e2998d375540298670797c4ad970b7d8553296bf4ed03c831cb6f604)

@ JSON\_TOK\_EOF

**Definition** json.h:56

[JSON\_TOK\_NUMBER](group__json.md#gga18a137ac5e2998d375540298670797c4ae25f16ae591eb17d4074e6dcc2f1e62c)

@ JSON\_TOK\_NUMBER

**Definition** json.h:41

[JSON\_TOK\_ENCODED\_OBJ](group__json.md#gga18a137ac5e2998d375540298670797c4af1e451cb321c805cff8fcde3561d3e64)

@ JSON\_TOK\_ENCODED\_OBJ

**Definition** json.h:45

[JSON\_TOK\_ERROR](group__json.md#gga18a137ac5e2998d375540298670797c4afe9c51f453d7dd02504071330a030e9e)

@ JSON\_TOK\_ERROR

**Definition** json.h:55

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

**Definition** json.h:65

[json\_lexer::pos](structjson__lexer.md#a9b403c5505e9a2cd9e475416b2e7f0ac)

char \* pos

**Definition** json.h:68

[json\_lexer::start](structjson__lexer.md#aa4d4a29301fb840c691bbfa416474de4)

char \* start

**Definition** json.h:67

[json\_lexer::tok](structjson__lexer.md#ab285bc72bf12a4de31b45ac0fc992620)

struct json\_token tok

**Definition** json.h:70

[json\_lexer::end](structjson__lexer.md#aeaf5743a9285e0aef9df99f9b3b48320)

char \* end

**Definition** json.h:69

[json\_obj\_descr](structjson__obj__descr.md)

**Definition** json.h:83

[json\_obj\_descr::field](structjson__obj__descr.md#a0449d269cff7813f37066f0381b9e8f5)

struct json\_obj\_descr::@365376074033132355222002170203261307250366002126::@063054233131061174035356024370111062256164304224 field

[json\_obj\_descr::element\_descr](structjson__obj__descr.md#a0a459bf5ad8a210395fe80c5edd72d93)

const struct json\_obj\_descr \* element\_descr

**Definition** json.h:113

[json\_obj\_descr::field\_name](structjson__obj__descr.md#a2120b7752253ece0beddcaf4c57d3ed8)

const char \* field\_name

**Definition** json.h:84

[json\_obj\_descr::align\_shift](structjson__obj__descr.md#a475717ac4dd01296c01468450e50f75b)

uint32\_t align\_shift

**Definition** json.h:91

[json\_obj\_descr::sub\_descr](structjson__obj__descr.md#a4f5e97c654d0c5e21f1efb5a01966e56)

const struct json\_obj\_descr \* sub\_descr

**Definition** json.h:109

[json\_obj\_descr::object](structjson__obj__descr.md#a5d5df7aab020feb3eeb59a7f6089b066)

struct json\_obj\_descr::@365376074033132355222002170203261307250366002126::@000230262224034312357266150225204112257263011374 object

[json\_obj\_descr::field\_name\_len](structjson__obj__descr.md#a602bf4d8bb5d47c8edb40963ea8ba42f)

uint32\_t field\_name\_len

**Definition** json.h:94

[json\_obj\_descr::offset](structjson__obj__descr.md#a8c6f3eae5e678b8b8ef1957c46f488f1)

uint32\_t offset

**Definition** json.h:105

[json\_obj\_descr::type](structjson__obj__descr.md#a975e998d3ec36f234f09aa2d0d116c9c)

uint32\_t type

**Definition** json.h:102

[json\_obj\_descr::size](structjson__obj__descr.md#aa01763bb5316fdce6acc64c7d7d21406)

size\_t size

**Definition** json.h:117

[json\_obj\_descr::array](structjson__obj__descr.md#ac12783b89f5507bef7fa3da2c56d1d61)

struct json\_obj\_descr::@365376074033132355222002170203261307250366002126::@365235374054153265207136004206377347035314130057 array

[json\_obj\_descr::n\_elements](structjson__obj__descr.md#ace6558c5156a76658d8835fd5e65ee52)

size\_t n\_elements

**Definition** json.h:114

[json\_obj\_descr::sub\_descr\_len](structjson__obj__descr.md#adea0b44d1552305df9dce70074044ba1)

size\_t sub\_descr\_len

**Definition** json.h:110

[json\_obj\_token](structjson__obj__token.md)

**Definition** json.h:77

[json\_obj\_token::length](structjson__obj__token.md#ac996ab0b850803998a37025b57051144)

size\_t length

**Definition** json.h:79

[json\_obj\_token::start](structjson__obj__token.md#aef14abe1f0cefda6bd89d058787550b1)

char \* start

**Definition** json.h:78

[json\_obj](structjson__obj.md)

**Definition** json.h:73

[json\_obj::lex](structjson__obj.md#a7a48a2dca53ee74e7c8eb4727af0e33a)

struct json\_lexer lex

**Definition** json.h:74

[json\_token](structjson__token.md)

**Definition** json.h:59

[json\_token::start](structjson__token.md#a606e33f699c3ec5a66f450cc1777b3c2)

char \* start

**Definition** json.h:61

[json\_token::type](structjson__token.md#ab163615cc3a39191d5a48e900c579e94)

enum json\_tokens type

**Definition** json.h:60

[json\_token::end](structjson__token.md#abb55042d9343358e85311ea52cacb963)

char \* end

**Definition** json.h:62

[util.h](sys_2util_8h.md)

Misc utilities.

[toolchain.h](toolchain_8h.md)

Macros to abstract toolchain specific capabilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [data](dir_f6906818b29bc0a2a087f651f21ae7e0.md)
- [json.h](json_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
