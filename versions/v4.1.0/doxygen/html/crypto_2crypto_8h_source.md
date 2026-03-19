---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/crypto_2crypto_8h_source.html
original_path: doxygen/html/crypto_2crypto_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

crypto.h

[Go to the documentation of this file.](crypto_2crypto_8h.md)

1/\*

2 \* Copyright (c) 2016 Intel Corporation.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

16

17#ifndef ZEPHYR\_INCLUDE\_CRYPTO\_H\_

18#define ZEPHYR\_INCLUDE\_CRYPTO\_H\_

19

20#include <[zephyr/device.h](device_8h.md)>

21#include <[errno.h](errno_8h.md)>

22#include <[zephyr/sys/util.h](sys_2util_8h.md)>

23#include <[zephyr/sys/\_\_assert.h](____assert_8h.md)>

24#include <[zephyr/crypto/hash.h](hash_8h.md)>

25#include "[cipher.h](cipher_8h.md)"

26

35

36

37/\* ctx.flags values. Not all drivers support all flags.

38 \* A user app can query the supported hw / driver

39 \* capabilities via provided API (crypto\_query\_hwcaps()), and choose a

40 \* supported config during the session setup.

41 \*/

[ 42](group__crypto.md#ga821c2629510aad5d591a565767d8abbd)#define CAP\_OPAQUE\_KEY\_HNDL BIT(0)

[ 43](group__crypto.md#ga95fd2a144207a575b2e0d24d5d6bf85a)#define CAP\_RAW\_KEY BIT(1)

44

45/\* TBD to define \*/

[ 46](group__crypto.md#ga18aeace031f8b9bb4241b44f8b36f056)#define CAP\_KEY\_LOADING\_API BIT(2)

47

[ 49](group__crypto.md#ga4c00d0513306fbc511fb4828108d37c8)#define CAP\_INPLACE\_OPS BIT(3)

[ 50](group__crypto.md#ga858150378de8f024e96614a6c2f138a2)#define CAP\_SEPARATE\_IO\_BUFS BIT(4)

51

[ 56](group__crypto.md#ga469bae7c354d17ba9b22c7ce4d8e076a)#define CAP\_SYNC\_OPS BIT(5)

[ 57](group__crypto.md#ga62492a4ce9c9274c78f3a7a915a66983)#define CAP\_ASYNC\_OPS BIT(6)

58

[ 60](group__crypto.md#ga6574dce552f5ba3b6f347e260a57d2f5)#define CAP\_AUTONONCE BIT(7)

61

[ 63](group__crypto.md#ga8fa14517853a8a1c4f134b5772f7d308)#define CAP\_NO\_IV\_PREFIX BIT(8)

64

65/\* More flags to be added as necessary \*/

66

[ 68](structcrypto__driver__api.md)\_\_subsystem struct [crypto\_driver\_api](structcrypto__driver__api.md) {

[ 69](structcrypto__driver__api.md#a19859cdd9185f5d333fe6893efc27967) int (\*[query\_hw\_caps](structcrypto__driver__api.md#a19859cdd9185f5d333fe6893efc27967))(const struct [device](structdevice.md) \*dev);

70

71 /\* Setup a crypto session \*/

[ 72](structcrypto__driver__api.md#af2ddc3aa1447dbef500715e1ea4dd780) int (\*[cipher\_begin\_session](structcrypto__driver__api.md#af2ddc3aa1447dbef500715e1ea4dd780))(const struct [device](structdevice.md) \*dev, struct [cipher\_ctx](structcipher__ctx.md) \*ctx,

73 enum [cipher\_algo](group__crypto__cipher.md#gaa43d9907b508cb28c649aaa524d84424) algo, enum [cipher\_mode](group__crypto__cipher.md#gaeedaf8017f8d6518f7dedef365bbae43) mode,

74 enum [cipher\_op](group__crypto__cipher.md#ga1db3a5604bff0669672af4457aaaee21) op\_type);

75

76 /\* Tear down an established session \*/

[ 77](structcrypto__driver__api.md#a77f9e6ab2b527c4433ddf5cbcf6b8dca) int (\*[cipher\_free\_session](structcrypto__driver__api.md#a77f9e6ab2b527c4433ddf5cbcf6b8dca))(const struct [device](structdevice.md) \*dev, struct [cipher\_ctx](structcipher__ctx.md) \*ctx);

78

79 /\* Register async crypto op completion callback with the driver \*/

[ 80](structcrypto__driver__api.md#a2c59735e94df3e8740611937c6ed1c2f) int (\*[cipher\_async\_callback\_set](structcrypto__driver__api.md#a2c59735e94df3e8740611937c6ed1c2f))(const struct [device](structdevice.md) \*dev,

81 [cipher\_completion\_cb](group__crypto__cipher.md#ga062b07459bcc2990535465a7b9044ecd) cb);

82

83 /\* Setup a hash session \*/

[ 84](structcrypto__driver__api.md#a48845d14ff94ff16633227d10f971f57) int (\*[hash\_begin\_session](structcrypto__driver__api.md#a48845d14ff94ff16633227d10f971f57))(const struct [device](structdevice.md) \*dev, struct [hash\_ctx](structhash__ctx.md) \*ctx,

85 enum [hash\_algo](group__crypto__hash.md#gaaea88501aa8243eacc8c57ac0914ac7a) algo);

86 /\* Tear down an established hash session \*/

[ 87](structcrypto__driver__api.md#aa3033ec374a10abd180af38f6fdc080b) int (\*[hash\_free\_session](structcrypto__driver__api.md#aa3033ec374a10abd180af38f6fdc080b))(const struct [device](structdevice.md) \*dev, struct [hash\_ctx](structhash__ctx.md) \*ctx);

88 /\* Register async hash op completion callback with the driver \*/

[ 89](structcrypto__driver__api.md#a87d5891e9ce4a76ed50c7591ae7a27ff) int (\*[hash\_async\_callback\_set](structcrypto__driver__api.md#a87d5891e9ce4a76ed50c7591ae7a27ff))(const struct [device](structdevice.md) \*dev,

90 [hash\_completion\_cb](group__crypto__hash.md#ga1f49008c35d9f04b66e587d1b43404bd) cb);

91};

92

93/\* Following are the public API a user app may call.

94 \* The first two relate to crypto "session" setup / teardown. Further we

95 \* have four cipher mode specific (CTR, CCM, CBC ...) calls to perform the

96 \* actual crypto operation in the context of a session. Also we have an

97 \* API to provide the callback for async operations.

98 \*/

99

[ 111](group__crypto.md#gadb2c24136bb56927bb14d4cfffdd5d80)static inline int [crypto\_query\_hwcaps](group__crypto.md#gadb2c24136bb56927bb14d4cfffdd5d80)(const struct [device](structdevice.md) \*dev)

112{

113 struct [crypto\_driver\_api](structcrypto__driver__api.md) \*api;

114 int tmp;

115

116 api = (struct [crypto\_driver\_api](structcrypto__driver__api.md) \*) dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

117

118 tmp = api->[query\_hw\_caps](structcrypto__driver__api.md#a19859cdd9185f5d333fe6893efc27967)(dev);

119

120 \_\_ASSERT((tmp & ([CAP\_OPAQUE\_KEY\_HNDL](group__crypto.md#ga821c2629510aad5d591a565767d8abbd) | [CAP\_RAW\_KEY](group__crypto.md#ga95fd2a144207a575b2e0d24d5d6bf85a))) != 0,

121 "Driver should support at least one key type: RAW/Opaque");

122

123 \_\_ASSERT((tmp & ([CAP\_INPLACE\_OPS](group__crypto.md#ga4c00d0513306fbc511fb4828108d37c8) | [CAP\_SEPARATE\_IO\_BUFS](group__crypto.md#ga858150378de8f024e96614a6c2f138a2))) != 0,

124 "Driver should support at least one IO buf type: Inplace/separate");

125

126 \_\_ASSERT((tmp & ([CAP\_SYNC\_OPS](group__crypto.md#ga469bae7c354d17ba9b22c7ce4d8e076a) | [CAP\_ASYNC\_OPS](group__crypto.md#ga62492a4ce9c9274c78f3a7a915a66983))) != 0,

127 "Driver should support at least one op-type: sync/async");

128 return tmp;

129

130}

131

135

142

[ 162](group__crypto__cipher.md#ga0720700438ba5819aa826aa37f0c4227)static inline int [cipher\_begin\_session](group__crypto__cipher.md#ga0720700438ba5819aa826aa37f0c4227)(const struct [device](structdevice.md) \*dev,

163 struct [cipher\_ctx](structcipher__ctx.md) \*ctx,

164 enum [cipher\_algo](group__crypto__cipher.md#gaa43d9907b508cb28c649aaa524d84424) algo,

165 enum [cipher\_mode](group__crypto__cipher.md#gaeedaf8017f8d6518f7dedef365bbae43) mode,

166 enum [cipher\_op](group__crypto__cipher.md#ga1db3a5604bff0669672af4457aaaee21) optype)

167{

168 struct [crypto\_driver\_api](structcrypto__driver__api.md) \*api;

169 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9);

170

171 api = (struct [crypto\_driver\_api](structcrypto__driver__api.md) \*) dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

172 ctx->[device](structcipher__ctx.md#a44842ea8ece2aaea4d757137cdb67b52) = dev;

173 ctx->[ops](structcipher__ctx.md#ae3eb86d5be42450b761f89114723b682).[cipher\_mode](structcipher__ops.md#a93c8c2c77d44ea013fbb6e7fd788d4d4) = mode;

174

175 [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) = (ctx->[flags](structcipher__ctx.md#a5745811b9b08e6df51f9b8f8b14ceae7) & ([CAP\_OPAQUE\_KEY\_HNDL](group__crypto.md#ga821c2629510aad5d591a565767d8abbd) | [CAP\_RAW\_KEY](group__crypto.md#ga95fd2a144207a575b2e0d24d5d6bf85a)));

176 \_\_ASSERT([flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) != 0U, "Keytype missing: RAW Key or OPAQUE handle");

177 \_\_ASSERT([flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) != ([CAP\_OPAQUE\_KEY\_HNDL](group__crypto.md#ga821c2629510aad5d591a565767d8abbd) | [CAP\_RAW\_KEY](group__crypto.md#ga95fd2a144207a575b2e0d24d5d6bf85a)),

178 "conflicting options for keytype");

179

180 [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) = (ctx->[flags](structcipher__ctx.md#a5745811b9b08e6df51f9b8f8b14ceae7) & ([CAP\_INPLACE\_OPS](group__crypto.md#ga4c00d0513306fbc511fb4828108d37c8) | [CAP\_SEPARATE\_IO\_BUFS](group__crypto.md#ga858150378de8f024e96614a6c2f138a2)));

181 \_\_ASSERT([flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) != 0U, "IO buffer type missing");

182 \_\_ASSERT([flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) != ([CAP\_INPLACE\_OPS](group__crypto.md#ga4c00d0513306fbc511fb4828108d37c8) | [CAP\_SEPARATE\_IO\_BUFS](group__crypto.md#ga858150378de8f024e96614a6c2f138a2)),

183 "conflicting options for IO buffer type");

184

185 [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) = (ctx->[flags](structcipher__ctx.md#a5745811b9b08e6df51f9b8f8b14ceae7) & ([CAP\_SYNC\_OPS](group__crypto.md#ga469bae7c354d17ba9b22c7ce4d8e076a) | [CAP\_ASYNC\_OPS](group__crypto.md#ga62492a4ce9c9274c78f3a7a915a66983)));

186 \_\_ASSERT([flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) != 0U, "sync/async type missing");

187 \_\_ASSERT([flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) != ([CAP\_SYNC\_OPS](group__crypto.md#ga469bae7c354d17ba9b22c7ce4d8e076a) | [CAP\_ASYNC\_OPS](group__crypto.md#ga62492a4ce9c9274c78f3a7a915a66983)),

188 "conflicting options for sync/async");

189

190 return api->[cipher\_begin\_session](structcrypto__driver__api.md#af2ddc3aa1447dbef500715e1ea4dd780)(dev, ctx, algo, mode, optype);

191}

192

[ 204](group__crypto__cipher.md#gaa818a3de1f2d6319cd21bf6b7caf7cbb)static inline int [cipher\_free\_session](group__crypto__cipher.md#gaa818a3de1f2d6319cd21bf6b7caf7cbb)(const struct [device](structdevice.md) \*dev,

205 struct [cipher\_ctx](structcipher__ctx.md) \*ctx)

206{

207 struct [crypto\_driver\_api](structcrypto__driver__api.md) \*api;

208

209 api = (struct [crypto\_driver\_api](structcrypto__driver__api.md) \*) dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

210

211 return api->[cipher\_free\_session](structcrypto__driver__api.md#a77f9e6ab2b527c4433ddf5cbcf6b8dca)(dev, ctx);

212}

213

[ 228](group__crypto__cipher.md#gaaf0add27d9116f584e7bbc2d8f1eb39b)static inline int [cipher\_callback\_set](group__crypto__cipher.md#gaaf0add27d9116f584e7bbc2d8f1eb39b)(const struct [device](structdevice.md) \*dev,

229 [cipher\_completion\_cb](group__crypto__cipher.md#ga062b07459bcc2990535465a7b9044ecd) cb)

230{

231 struct [crypto\_driver\_api](structcrypto__driver__api.md) \*api;

232

233 api = (struct [crypto\_driver\_api](structcrypto__driver__api.md) \*) dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

234

235 if (api->[cipher\_async\_callback\_set](structcrypto__driver__api.md#a2c59735e94df3e8740611937c6ed1c2f)) {

236 return api->[cipher\_async\_callback\_set](structcrypto__driver__api.md#a2c59735e94df3e8740611937c6ed1c2f)(dev, cb);

237 }

238

239 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

240

241}

242

[ 252](group__crypto__cipher.md#ga05a2569f8d404593e053ce69817a457e)static inline int [cipher\_block\_op](group__crypto__cipher.md#ga05a2569f8d404593e053ce69817a457e)(struct [cipher\_ctx](structcipher__ctx.md) \*ctx,

253 struct [cipher\_pkt](structcipher__pkt.md) \*pkt)

254{

255 \_\_ASSERT(ctx->[ops](structcipher__ctx.md#ae3eb86d5be42450b761f89114723b682).[cipher\_mode](structcipher__ops.md#a93c8c2c77d44ea013fbb6e7fd788d4d4) == [CRYPTO\_CIPHER\_MODE\_ECB](group__crypto__cipher.md#ggaeedaf8017f8d6518f7dedef365bbae43a30ffc1c7c1489f938ed8c567a4fb885e), "ECB mode "

256 "session invoking a different mode handler");

257

258 pkt->[ctx](structcipher__pkt.md#a26fb877d705580648da03ce95264d100) = ctx;

259 return ctx->[ops](structcipher__ctx.md#ae3eb86d5be42450b761f89114723b682).[block\_crypt\_hndlr](structcipher__ops.md#a2675dd312be240c24d7d2c0e81bcde2b)(ctx, pkt);

260}

261

[ 273](group__crypto__cipher.md#ga2c4ac483eb4e11110be939e669040700)static inline int [cipher\_cbc\_op](group__crypto__cipher.md#ga2c4ac483eb4e11110be939e669040700)(struct [cipher\_ctx](structcipher__ctx.md) \*ctx,

274 struct [cipher\_pkt](structcipher__pkt.md) \*pkt, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*iv)

275{

276 \_\_ASSERT(ctx->[ops](structcipher__ctx.md#ae3eb86d5be42450b761f89114723b682).[cipher\_mode](structcipher__ops.md#a93c8c2c77d44ea013fbb6e7fd788d4d4) == [CRYPTO\_CIPHER\_MODE\_CBC](group__crypto__cipher.md#ggaeedaf8017f8d6518f7dedef365bbae43a98034da3b89ae5c47749c59a3b15bbfd), "CBC mode "

277 "session invoking a different mode handler");

278

279 pkt->[ctx](structcipher__pkt.md#a26fb877d705580648da03ce95264d100) = ctx;

280 return ctx->[ops](structcipher__ctx.md#ae3eb86d5be42450b761f89114723b682).[cbc\_crypt\_hndlr](structcipher__ops.md#abc7cf6306467c5aff24ae3faa37902e6)(ctx, pkt, iv);

281}

282

[ 300](group__crypto__cipher.md#gaeffb9d5dd85bf135eb2cca6d47cb373c)static inline int [cipher\_ctr\_op](group__crypto__cipher.md#gaeffb9d5dd85bf135eb2cca6d47cb373c)(struct [cipher\_ctx](structcipher__ctx.md) \*ctx,

301 struct [cipher\_pkt](structcipher__pkt.md) \*pkt, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*iv)

302{

303 \_\_ASSERT(ctx->[ops](structcipher__ctx.md#ae3eb86d5be42450b761f89114723b682).[cipher\_mode](structcipher__ops.md#a93c8c2c77d44ea013fbb6e7fd788d4d4) == [CRYPTO\_CIPHER\_MODE\_CTR](group__crypto__cipher.md#ggaeedaf8017f8d6518f7dedef365bbae43a58823b401487d57d62a067d71bd2e9d2), "CTR mode "

304 "session invoking a different mode handler");

305

306 pkt->[ctx](structcipher__pkt.md#a26fb877d705580648da03ce95264d100) = ctx;

307 return ctx->[ops](structcipher__ctx.md#ae3eb86d5be42450b761f89114723b682).[ctr\_crypt\_hndlr](structcipher__ops.md#ac792113d841e3a6b7dc107d7123162db)(ctx, pkt, iv);

308}

309

[ 322](group__crypto__cipher.md#ga4886e7e1cc2fcff411066875b35b8b45)static inline int [cipher\_ccm\_op](group__crypto__cipher.md#ga4886e7e1cc2fcff411066875b35b8b45)(struct [cipher\_ctx](structcipher__ctx.md) \*ctx,

323 struct [cipher\_aead\_pkt](structcipher__aead__pkt.md) \*pkt, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*nonce)

324{

325 \_\_ASSERT(ctx->[ops](structcipher__ctx.md#ae3eb86d5be42450b761f89114723b682).[cipher\_mode](structcipher__ops.md#a93c8c2c77d44ea013fbb6e7fd788d4d4) == [CRYPTO\_CIPHER\_MODE\_CCM](group__crypto__cipher.md#ggaeedaf8017f8d6518f7dedef365bbae43a5116e1683b8c9c26582863a65128ce3b), "CCM mode "

326 "session invoking a different mode handler");

327

328 pkt->[pkt](structcipher__aead__pkt.md#a4953711ca04b1c1d17980fff03561d03)->[ctx](structcipher__pkt.md#a26fb877d705580648da03ce95264d100) = ctx;

329 return ctx->[ops](structcipher__ctx.md#ae3eb86d5be42450b761f89114723b682).[ccm\_crypt\_hndlr](structcipher__ops.md#af53f5f04fb5e1a7ca148f786d8cfe41f)(ctx, pkt, nonce);

330}

331

[ 344](group__crypto__cipher.md#ga3706b034252e40b818a782c28ba5e485)static inline int [cipher\_gcm\_op](group__crypto__cipher.md#ga3706b034252e40b818a782c28ba5e485)(struct [cipher\_ctx](structcipher__ctx.md) \*ctx,

345 struct [cipher\_aead\_pkt](structcipher__aead__pkt.md) \*pkt, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*nonce)

346{

347 \_\_ASSERT(ctx->[ops](structcipher__ctx.md#ae3eb86d5be42450b761f89114723b682).[cipher\_mode](structcipher__ops.md#a93c8c2c77d44ea013fbb6e7fd788d4d4) == [CRYPTO\_CIPHER\_MODE\_GCM](group__crypto__cipher.md#ggaeedaf8017f8d6518f7dedef365bbae43a2f0de7c8f0b9c1a8ac7343ca3ca72c12), "GCM mode "

348 "session invoking a different mode handler");

349

350 pkt->[pkt](structcipher__aead__pkt.md#a4953711ca04b1c1d17980fff03561d03)->[ctx](structcipher__pkt.md#a26fb877d705580648da03ce95264d100) = ctx;

351 return ctx->[ops](structcipher__ctx.md#ae3eb86d5be42450b761f89114723b682).[gcm\_crypt\_hndlr](structcipher__ops.md#a570d1ed37d6cce61caa1c6e257f9cdc8)(ctx, pkt, nonce);

352}

353

354

358

365

366

[ 384](group__crypto__hash.md#ga9b736d047cbfb7530ffa0bc4b64d6ad1)static inline int [hash\_begin\_session](group__crypto__hash.md#ga9b736d047cbfb7530ffa0bc4b64d6ad1)(const struct [device](structdevice.md) \*dev,

385 struct [hash\_ctx](structhash__ctx.md) \*ctx,

386 enum [hash\_algo](group__crypto__hash.md#gaaea88501aa8243eacc8c57ac0914ac7a) algo)

387{

388 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9);

389 struct [crypto\_driver\_api](structcrypto__driver__api.md) \*api;

390

391 api = (struct [crypto\_driver\_api](structcrypto__driver__api.md) \*) dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

392 ctx->[device](structhash__ctx.md#abe1e70bd23305296e54564b5966ff310) = dev;

393

394 [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) = (ctx->[flags](structhash__ctx.md#ab550711912423a0eb03c410aef491854) & ([CAP\_INPLACE\_OPS](group__crypto.md#ga4c00d0513306fbc511fb4828108d37c8) | [CAP\_SEPARATE\_IO\_BUFS](group__crypto.md#ga858150378de8f024e96614a6c2f138a2)));

395 \_\_ASSERT([flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) != 0U, "IO buffer type missing");

396 \_\_ASSERT([flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) != ([CAP\_INPLACE\_OPS](group__crypto.md#ga4c00d0513306fbc511fb4828108d37c8) | [CAP\_SEPARATE\_IO\_BUFS](group__crypto.md#ga858150378de8f024e96614a6c2f138a2)),

397 "conflicting options for IO buffer type");

398

399 [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) = (ctx->[flags](structhash__ctx.md#ab550711912423a0eb03c410aef491854) & ([CAP\_SYNC\_OPS](group__crypto.md#ga469bae7c354d17ba9b22c7ce4d8e076a) | [CAP\_ASYNC\_OPS](group__crypto.md#ga62492a4ce9c9274c78f3a7a915a66983)));

400 \_\_ASSERT([flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) != 0U, "sync/async type missing");

401 \_\_ASSERT([flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) != ([CAP\_SYNC\_OPS](group__crypto.md#ga469bae7c354d17ba9b22c7ce4d8e076a) | [CAP\_ASYNC\_OPS](group__crypto.md#ga62492a4ce9c9274c78f3a7a915a66983)),

402 "conflicting options for sync/async");

403

404

405 return api->[hash\_begin\_session](structcrypto__driver__api.md#a48845d14ff94ff16633227d10f971f57)(dev, ctx, algo);

406}

407

[ 419](group__crypto__hash.md#gadafcd2ad79e0695245c8884b6b282508)static inline int [hash\_free\_session](group__crypto__hash.md#gadafcd2ad79e0695245c8884b6b282508)(const struct [device](structdevice.md) \*dev,

420 struct [hash\_ctx](structhash__ctx.md) \*ctx)

421{

422 struct [crypto\_driver\_api](structcrypto__driver__api.md) \*api;

423

424 api = (struct [crypto\_driver\_api](structcrypto__driver__api.md) \*) dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

425

426 return api->[hash\_free\_session](structcrypto__driver__api.md#aa3033ec374a10abd180af38f6fdc080b)(dev, ctx);

427}

428

[ 443](group__crypto__hash.md#gaa69bbf41cc150dae0d97b215862729cf)static inline int [hash\_callback\_set](group__crypto__hash.md#gaa69bbf41cc150dae0d97b215862729cf)(const struct [device](structdevice.md) \*dev,

444 [hash\_completion\_cb](group__crypto__hash.md#ga1f49008c35d9f04b66e587d1b43404bd) cb)

445{

446 struct [crypto\_driver\_api](structcrypto__driver__api.md) \*api;

447

448 api = (struct [crypto\_driver\_api](structcrypto__driver__api.md) \*) dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

449

450 if (api->[hash\_async\_callback\_set](structcrypto__driver__api.md#a87d5891e9ce4a76ed50c7591ae7a27ff)) {

451 return api->[hash\_async\_callback\_set](structcrypto__driver__api.md#a87d5891e9ce4a76ed50c7591ae7a27ff)(dev, cb);

452 }

453

454 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

455

456}

457

[ 466](group__crypto__hash.md#ga761e5d0bda9937d7fa4550c876a1c387)static inline int [hash\_compute](group__crypto__hash.md#ga761e5d0bda9937d7fa4550c876a1c387)(struct [hash\_ctx](structhash__ctx.md) \*ctx, struct [hash\_pkt](structhash__pkt.md) \*pkt)

467{

468 pkt->[ctx](structhash__pkt.md#ab5b3ffd87a11ce3838178b2e652d49b9) = ctx;

469

470 return ctx->[hash\_hndlr](structhash__ctx.md#a72a2e7af667bed1ee1dabb8411b01e40)(ctx, pkt, true);

471}

472

[ 485](group__crypto__hash.md#gaf54ee20fb1ca58764f6f301739c3ba93)static inline int [hash\_update](group__crypto__hash.md#gaf54ee20fb1ca58764f6f301739c3ba93)(struct [hash\_ctx](structhash__ctx.md) \*ctx, struct [hash\_pkt](structhash__pkt.md) \*pkt)

486{

487 pkt->[ctx](structhash__pkt.md#ab5b3ffd87a11ce3838178b2e652d49b9) = ctx;

488

489 return ctx->[hash\_hndlr](structhash__ctx.md#a72a2e7af667bed1ee1dabb8411b01e40)(ctx, pkt, false);

490}

491

495

496#endif /\* ZEPHYR\_INCLUDE\_CRYPTO\_H\_ \*/

[\_\_assert.h](____assert_8h.md)

[cipher.h](cipher_8h.md)

Crypto Cipher structure definitions.

[device.h](device_8h.md)

[errno.h](errno_8h.md)

System error numbers.

[cipher\_block\_op](group__crypto__cipher.md#ga05a2569f8d404593e053ce69817a457e)

static int cipher\_block\_op(struct cipher\_ctx \*ctx, struct cipher\_pkt \*pkt)

Perform single-block crypto operation (ECB cipher mode).

**Definition** crypto.h:252

[cipher\_completion\_cb](group__crypto__cipher.md#ga062b07459bcc2990535465a7b9044ecd)

void(\* cipher\_completion\_cb)(struct cipher\_pkt \*completed, int status)

**Definition** cipher.h:242

[cipher\_begin\_session](group__crypto__cipher.md#ga0720700438ba5819aa826aa37f0c4227)

static int cipher\_begin\_session(const struct device \*dev, struct cipher\_ctx \*ctx, enum cipher\_algo algo, enum cipher\_mode mode, enum cipher\_op optype)

Setup a crypto session.

**Definition** crypto.h:162

[cipher\_op](group__crypto__cipher.md#ga1db3a5604bff0669672af4457aaaee21)

cipher\_op

Cipher Operation.

**Definition** cipher.h:34

[cipher\_cbc\_op](group__crypto__cipher.md#ga2c4ac483eb4e11110be939e669040700)

static int cipher\_cbc\_op(struct cipher\_ctx \*ctx, struct cipher\_pkt \*pkt, uint8\_t \*iv)

Perform Cipher Block Chaining (CBC) crypto operation.

**Definition** crypto.h:273

[cipher\_gcm\_op](group__crypto__cipher.md#ga3706b034252e40b818a782c28ba5e485)

static int cipher\_gcm\_op(struct cipher\_ctx \*ctx, struct cipher\_aead\_pkt \*pkt, uint8\_t \*nonce)

Perform Galois/Counter Mode (GCM) crypto operation.

**Definition** crypto.h:344

[cipher\_ccm\_op](group__crypto__cipher.md#ga4886e7e1cc2fcff411066875b35b8b45)

static int cipher\_ccm\_op(struct cipher\_ctx \*ctx, struct cipher\_aead\_pkt \*pkt, uint8\_t \*nonce)

Perform Counter with CBC-MAC (CCM) mode crypto operation.

**Definition** crypto.h:322

[cipher\_algo](group__crypto__cipher.md#gaa43d9907b508cb28c649aaa524d84424)

cipher\_algo

Cipher Algorithm.

**Definition** cipher.h:29

[cipher\_free\_session](group__crypto__cipher.md#gaa818a3de1f2d6319cd21bf6b7caf7cbb)

static int cipher\_free\_session(const struct device \*dev, struct cipher\_ctx \*ctx)

Cleanup a crypto session.

**Definition** crypto.h:204

[cipher\_callback\_set](group__crypto__cipher.md#gaaf0add27d9116f584e7bbc2d8f1eb39b)

static int cipher\_callback\_set(const struct device \*dev, cipher\_completion\_cb cb)

Registers an async crypto op completion callback with the driver.

**Definition** crypto.h:228

[cipher\_mode](group__crypto__cipher.md#gaeedaf8017f8d6518f7dedef365bbae43)

cipher\_mode

Possible cipher mode options.

**Definition** cipher.h:44

[cipher\_ctr\_op](group__crypto__cipher.md#gaeffb9d5dd85bf135eb2cca6d47cb373c)

static int cipher\_ctr\_op(struct cipher\_ctx \*ctx, struct cipher\_pkt \*pkt, uint8\_t \*iv)

Perform Counter (CTR) mode crypto operation.

**Definition** crypto.h:300

[CRYPTO\_CIPHER\_MODE\_GCM](group__crypto__cipher.md#ggaeedaf8017f8d6518f7dedef365bbae43a2f0de7c8f0b9c1a8ac7343ca3ca72c12)

@ CRYPTO\_CIPHER\_MODE\_GCM

**Definition** cipher.h:49

[CRYPTO\_CIPHER\_MODE\_ECB](group__crypto__cipher.md#ggaeedaf8017f8d6518f7dedef365bbae43a30ffc1c7c1489f938ed8c567a4fb885e)

@ CRYPTO\_CIPHER\_MODE\_ECB

**Definition** cipher.h:45

[CRYPTO\_CIPHER\_MODE\_CCM](group__crypto__cipher.md#ggaeedaf8017f8d6518f7dedef365bbae43a5116e1683b8c9c26582863a65128ce3b)

@ CRYPTO\_CIPHER\_MODE\_CCM

**Definition** cipher.h:48

[CRYPTO\_CIPHER\_MODE\_CTR](group__crypto__cipher.md#ggaeedaf8017f8d6518f7dedef365bbae43a58823b401487d57d62a067d71bd2e9d2)

@ CRYPTO\_CIPHER\_MODE\_CTR

**Definition** cipher.h:47

[CRYPTO\_CIPHER\_MODE\_CBC](group__crypto__cipher.md#ggaeedaf8017f8d6518f7dedef365bbae43a98034da3b89ae5c47749c59a3b15bbfd)

@ CRYPTO\_CIPHER\_MODE\_CBC

**Definition** cipher.h:46

[hash\_completion\_cb](group__crypto__hash.md#ga1f49008c35d9f04b66e587d1b43404bd)

void(\* hash\_completion\_cb)(struct hash\_pkt \*completed, int status)

**Definition** hash.h:114

[hash\_compute](group__crypto__hash.md#ga761e5d0bda9937d7fa4550c876a1c387)

static int hash\_compute(struct hash\_ctx \*ctx, struct hash\_pkt \*pkt)

Perform a cryptographic hash function.

**Definition** crypto.h:466

[hash\_begin\_session](group__crypto__hash.md#ga9b736d047cbfb7530ffa0bc4b64d6ad1)

static int hash\_begin\_session(const struct device \*dev, struct hash\_ctx \*ctx, enum hash\_algo algo)

Setup a hash session.

**Definition** crypto.h:384

[hash\_callback\_set](group__crypto__hash.md#gaa69bbf41cc150dae0d97b215862729cf)

static int hash\_callback\_set(const struct device \*dev, hash\_completion\_cb cb)

Registers an async hash completion callback with the driver.

**Definition** crypto.h:443

[hash\_algo](group__crypto__hash.md#gaaea88501aa8243eacc8c57ac0914ac7a)

hash\_algo

Hash algorithm.

**Definition** hash.h:26

[hash\_free\_session](group__crypto__hash.md#gadafcd2ad79e0695245c8884b6b282508)

static int hash\_free\_session(const struct device \*dev, struct hash\_ctx \*ctx)

Cleanup a hash session.

**Definition** crypto.h:419

[hash\_update](group__crypto__hash.md#gaf54ee20fb1ca58764f6f301739c3ba93)

static int hash\_update(struct hash\_ctx \*ctx, struct hash\_pkt \*pkt)

Perform a cryptographic multipart hash operation.

**Definition** crypto.h:485

[CAP\_SYNC\_OPS](group__crypto.md#ga469bae7c354d17ba9b22c7ce4d8e076a)

#define CAP\_SYNC\_OPS

These denotes if the output (completion of a cipher\_xxx\_op) is conveyed by the op function returning,...

**Definition** crypto.h:56

[CAP\_INPLACE\_OPS](group__crypto.md#ga4c00d0513306fbc511fb4828108d37c8)

#define CAP\_INPLACE\_OPS

Whether the output is placed in separate buffer or not.

**Definition** crypto.h:49

[CAP\_ASYNC\_OPS](group__crypto.md#ga62492a4ce9c9274c78f3a7a915a66983)

#define CAP\_ASYNC\_OPS

**Definition** crypto.h:57

[CAP\_OPAQUE\_KEY\_HNDL](group__crypto.md#ga821c2629510aad5d591a565767d8abbd)

#define CAP\_OPAQUE\_KEY\_HNDL

**Definition** crypto.h:42

[CAP\_SEPARATE\_IO\_BUFS](group__crypto.md#ga858150378de8f024e96614a6c2f138a2)

#define CAP\_SEPARATE\_IO\_BUFS

**Definition** crypto.h:50

[CAP\_RAW\_KEY](group__crypto.md#ga95fd2a144207a575b2e0d24d5d6bf85a)

#define CAP\_RAW\_KEY

**Definition** crypto.h:43

[crypto\_query\_hwcaps](group__crypto.md#gadb2c24136bb56927bb14d4cfffdd5d80)

static int crypto\_query\_hwcaps(const struct device \*dev)

Query the crypto hardware capabilities.

**Definition** crypto.h:111

[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33)

#define ENOTSUP

Unsupported value.

**Definition** errno.h:114

[hash.h](hash_8h.md)

Crypto Hash APIs.

[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)

flags

**Definition** parser.h:97

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[cipher\_aead\_pkt](structcipher__aead__pkt.md)

Structure encoding IO parameters in AEAD (Authenticated Encryption with Associated Data) scenario lik...

**Definition** cipher.h:217

[cipher\_aead\_pkt::pkt](structcipher__aead__pkt.md#a4953711ca04b1c1d17980fff03561d03)

struct cipher\_pkt \* pkt

**Definition** cipher.h:219

[cipher\_ctx](structcipher__ctx.md)

Structure encoding session parameters.

**Definition** cipher.h:110

[cipher\_ctx::device](structcipher__ctx.md#a44842ea8ece2aaea4d757137cdb67b52)

const struct device \* device

The device driver instance this crypto context relates to.

**Definition** cipher.h:131

[cipher\_ctx::flags](structcipher__ctx.md#a5745811b9b08e6df51f9b8f8b14ceae7)

uint16\_t flags

How certain fields are to be interpreted for this session.

**Definition** cipher.h:169

[cipher\_ctx::ops](structcipher__ctx.md#ae3eb86d5be42450b761f89114723b682)

struct cipher\_ops ops

Place for driver to return function pointers to be invoked per cipher operation.

**Definition** cipher.h:116

[cipher\_ops::block\_crypt\_hndlr](structcipher__ops.md#a2675dd312be240c24d7d2c0e81bcde2b)

block\_op\_t block\_crypt\_hndlr

**Definition** cipher.h:79

[cipher\_ops::gcm\_crypt\_hndlr](structcipher__ops.md#a570d1ed37d6cce61caa1c6e257f9cdc8)

gcm\_op\_t gcm\_crypt\_hndlr

**Definition** cipher.h:83

[cipher\_ops::cipher\_mode](structcipher__ops.md#a93c8c2c77d44ea013fbb6e7fd788d4d4)

enum cipher\_mode cipher\_mode

**Definition** cipher.h:76

[cipher\_ops::cbc\_crypt\_hndlr](structcipher__ops.md#abc7cf6306467c5aff24ae3faa37902e6)

cbc\_op\_t cbc\_crypt\_hndlr

**Definition** cipher.h:80

[cipher\_ops::ctr\_crypt\_hndlr](structcipher__ops.md#ac792113d841e3a6b7dc107d7123162db)

ctr\_op\_t ctr\_crypt\_hndlr

**Definition** cipher.h:81

[cipher\_ops::ccm\_crypt\_hndlr](structcipher__ops.md#af53f5f04fb5e1a7ca148f786d8cfe41f)

ccm\_op\_t ccm\_crypt\_hndlr

**Definition** cipher.h:82

[cipher\_pkt](structcipher__pkt.md)

Structure encoding IO parameters of one cryptographic operation like encrypt/decrypt.

**Definition** cipher.h:180

[cipher\_pkt::ctx](structcipher__pkt.md#a26fb877d705580648da03ce95264d100)

struct cipher\_ctx \* ctx

Context this packet relates to.

**Definition** cipher.h:208

[crypto\_driver\_api](structcrypto__driver__api.md)

Crypto driver API definition.

**Definition** crypto.h:68

[crypto\_driver\_api::query\_hw\_caps](structcrypto__driver__api.md#a19859cdd9185f5d333fe6893efc27967)

int(\* query\_hw\_caps)(const struct device \*dev)

**Definition** crypto.h:69

[crypto\_driver\_api::cipher\_async\_callback\_set](structcrypto__driver__api.md#a2c59735e94df3e8740611937c6ed1c2f)

int(\* cipher\_async\_callback\_set)(const struct device \*dev, cipher\_completion\_cb cb)

**Definition** crypto.h:80

[crypto\_driver\_api::hash\_begin\_session](structcrypto__driver__api.md#a48845d14ff94ff16633227d10f971f57)

int(\* hash\_begin\_session)(const struct device \*dev, struct hash\_ctx \*ctx, enum hash\_algo algo)

**Definition** crypto.h:84

[crypto\_driver\_api::cipher\_free\_session](structcrypto__driver__api.md#a77f9e6ab2b527c4433ddf5cbcf6b8dca)

int(\* cipher\_free\_session)(const struct device \*dev, struct cipher\_ctx \*ctx)

**Definition** crypto.h:77

[crypto\_driver\_api::hash\_async\_callback\_set](structcrypto__driver__api.md#a87d5891e9ce4a76ed50c7591ae7a27ff)

int(\* hash\_async\_callback\_set)(const struct device \*dev, hash\_completion\_cb cb)

**Definition** crypto.h:89

[crypto\_driver\_api::hash\_free\_session](structcrypto__driver__api.md#aa3033ec374a10abd180af38f6fdc080b)

int(\* hash\_free\_session)(const struct device \*dev, struct hash\_ctx \*ctx)

**Definition** crypto.h:87

[crypto\_driver\_api::cipher\_begin\_session](structcrypto__driver__api.md#af2ddc3aa1447dbef500715e1ea4dd780)

int(\* cipher\_begin\_session)(const struct device \*dev, struct cipher\_ctx \*ctx, enum cipher\_algo algo, enum cipher\_mode mode, enum cipher\_op op\_type)

**Definition** crypto.h:72

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:453

[device::api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d)

const void \* api

Address of the API structure exposed by the device instance.

**Definition** device.h:459

[hash\_ctx](structhash__ctx.md)

Structure encoding session parameters.

**Definition** hash.h:47

[hash\_ctx::hash\_hndlr](structhash__ctx.md#a72a2e7af667bed1ee1dabb8411b01e40)

hash\_op\_t hash\_hndlr

Hash handler set up when the session begins.

**Definition** hash.h:65

[hash\_ctx::flags](structhash__ctx.md#ab550711912423a0eb03c410aef491854)

uint16\_t flags

How certain fields are to be interpreted for this session.

**Definition** hash.h:78

[hash\_ctx::device](structhash__ctx.md#abe1e70bd23305296e54564b5966ff310)

const struct device \* device

The device driver instance this crypto context relates to.

**Definition** hash.h:51

[hash\_pkt](structhash__pkt.md)

Structure encoding IO parameters of a hash operation.

**Definition** hash.h:88

[hash\_pkt::ctx](structhash__pkt.md#ab5b3ffd87a11ce3838178b2e652d49b9)

struct hash\_ctx \* ctx

Context this packet relates to.

**Definition** hash.h:107

[util.h](sys_2util_8h.md)

Misc utilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [crypto](dir_8e645738bb65aae54152153b1372b1b2.md)
- [crypto.h](crypto_2crypto_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
