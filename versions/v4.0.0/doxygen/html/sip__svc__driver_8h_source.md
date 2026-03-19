---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/sip__svc__driver_8h_source.html
original_path: doxygen/html/sip__svc__driver_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

sip\_svc\_driver.h

[Go to the documentation of this file.](sip__svc__driver_8h.md)

1/\*

2 \* Copyright (c) 2023, Intel Corporation.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_SIP\_SVC\_DRIVER\_H\_

8#define ZEPHYR\_INCLUDE\_SIP\_SVC\_DRIVER\_H\_

9

10#include <[zephyr/device.h](device_8h.md)>

11#include <[zephyr/kernel.h](kernel_8h.md)>

12#include <[zephyr/arch/arm64/arm-smccc.h](arm-smccc_8h.md)>

13#include <[zephyr/drivers/sip\_svc/sip\_svc\_proto.h](sip__svc__proto_8h.md)>

14#include <[zephyr/sip\_svc/sip\_svc\_controller.h](sip__svc__controller_8h.md)>

15

[ 16](sip__svc__driver_8h.md#aeae219b400322b0926dd7251dc122bbd)#define DEV\_API(dev) ((struct svc\_driver\_api \*)(dev)->api)

17

[ 22](sip__svc__driver_8h.md#a780bbf4be68a9ac867243823c0eb790e)#define SVC\_CONDUIT\_NAME\_LENGTH (4)

23

[ 28](sip__svc__driver_8h.md#a15714e3852882693de6c9c7f2229bcd1)typedef void (\*[sip\_supervisory\_call\_t](sip__svc__driver_8h.md#a15714e3852882693de6c9c7f2229bcd1))(const struct [device](structdevice.md) \*dev, unsigned long function\_id,

29 unsigned long arg0, unsigned long arg1, unsigned long arg2,

30 unsigned long arg3, unsigned long arg4, unsigned long arg5,

31 unsigned long arg6, struct [arm\_smccc\_res](structarm__smccc__res.md) \*res);

32

[ 37](sip__svc__driver_8h.md#ac5921c9cdc00604651696e1580f30797)typedef [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) (\*[sip\_svc\_plat\_func\_id\_valid\_t](sip__svc__driver_8h.md#ac5921c9cdc00604651696e1580f30797))(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) command,

38 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) func\_id);

39

[ 44](sip__svc__driver_8h.md#a3cf78c760c6eae2091e92329e54b1a31)typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) (\*[sip\_svc\_plat\_format\_trans\_id\_t](sip__svc__driver_8h.md#a3cf78c760c6eae2091e92329e54b1a31))(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) client\_idx,

45 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) trans\_idx);

46

[ 51](sip__svc__driver_8h.md#a35145ddf422e8782b4ec37270b04d98c)typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) (\*[sip\_svc\_plat\_get\_trans\_idx\_t](sip__svc__driver_8h.md#a35145ddf422e8782b4ec37270b04d98c))(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) trans\_id);

52

[ 57](sip__svc__driver_8h.md#a9d61db0484e2aacce4515290ffb4450c)typedef void (\*[sip\_svc\_plat\_update\_trans\_id\_t](sip__svc__driver_8h.md#a9d61db0484e2aacce4515290ffb4450c))(const struct [device](structdevice.md) \*dev,

58 struct [sip\_svc\_request](structsip__svc__request.md) \*request, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) trans\_id);

59

[ 64](sip__svc__driver_8h.md#ab32e31bdba00ff66303fab1b04cd0ebe)typedef void (\*[sip\_svc\_plat\_free\_async\_memory\_t](sip__svc__driver_8h.md#ab32e31bdba00ff66303fab1b04cd0ebe))(const struct [device](structdevice.md) \*dev,

65 struct [sip\_svc\_request](structsip__svc__request.md) \*request);

66

[ 71](sip__svc__driver_8h.md#aa49a26b4b503e58d23fb5087ed701a0a)typedef int (\*[sip\_svc\_plat\_async\_res\_req\_t](sip__svc__driver_8h.md#aa49a26b4b503e58d23fb5087ed701a0a))(const struct [device](structdevice.md) \*dev, unsigned long \*a0,

72 unsigned long \*a1, unsigned long \*a2, unsigned long \*a3,

73 unsigned long \*a4, unsigned long \*a5, unsigned long \*a6,

74 unsigned long \*a7, char \*buf, size\_t size);

75

[ 80](sip__svc__driver_8h.md#a54293f84f9bc86661f8a4bf717ad4754)typedef int (\*[sip\_svc\_plat\_async\_res\_res\_t](sip__svc__driver_8h.md#a54293f84f9bc86661f8a4bf717ad4754))(const struct [device](structdevice.md) \*dev, struct [arm\_smccc\_res](structarm__smccc__res.md) \*res,

81 char \*buf, size\_t \*size, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*trans\_id);

82

[ 87](sip__svc__driver_8h.md#a926eeecea766b2131c03c57111a186f8)typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) (\*[sip\_svc\_plat\_get\_error\_code\_t](sip__svc__driver_8h.md#a926eeecea766b2131c03c57111a186f8))(const struct [device](structdevice.md) \*dev,

88 struct [arm\_smccc\_res](structarm__smccc__res.md) \*res);

89

[ 94](structsvc__driver__api.md)\_\_subsystem struct [svc\_driver\_api](structsvc__driver__api.md) {

[ 95](structsvc__driver__api.md#a5f02e921d2a038616fad9d8d6a052f6b) [sip\_supervisory\_call\_t](sip__svc__driver_8h.md#a15714e3852882693de6c9c7f2229bcd1) [sip\_supervisory\_call](structsvc__driver__api.md#a5f02e921d2a038616fad9d8d6a052f6b);

[ 96](structsvc__driver__api.md#a9f0a7711ef5ba2900d378c0a2805eaf4) [sip\_svc\_plat\_func\_id\_valid\_t](sip__svc__driver_8h.md#ac5921c9cdc00604651696e1580f30797) [sip\_svc\_plat\_func\_id\_valid](structsvc__driver__api.md#a9f0a7711ef5ba2900d378c0a2805eaf4);

[ 97](structsvc__driver__api.md#a6435b703d30f462c1ec38e533a9c0817) [sip\_svc\_plat\_format\_trans\_id\_t](sip__svc__driver_8h.md#a3cf78c760c6eae2091e92329e54b1a31) [sip\_svc\_plat\_format\_trans\_id](structsvc__driver__api.md#a6435b703d30f462c1ec38e533a9c0817);

[ 98](structsvc__driver__api.md#a30a435265fa828d9fdfcc70664be0945) [sip\_svc\_plat\_get\_trans\_idx\_t](sip__svc__driver_8h.md#a35145ddf422e8782b4ec37270b04d98c) [sip\_svc\_plat\_get\_trans\_idx](structsvc__driver__api.md#a30a435265fa828d9fdfcc70664be0945);

[ 99](structsvc__driver__api.md#a0ccdebec2a60d32a1767c5e47bc3ae25) [sip\_svc\_plat\_update\_trans\_id\_t](sip__svc__driver_8h.md#a9d61db0484e2aacce4515290ffb4450c) [sip\_svc\_plat\_update\_trans\_id](structsvc__driver__api.md#a0ccdebec2a60d32a1767c5e47bc3ae25);

[ 100](structsvc__driver__api.md#a484b7c6ef4777a61e8f4f8e6778a7b45) [sip\_svc\_plat\_free\_async\_memory\_t](sip__svc__driver_8h.md#ab32e31bdba00ff66303fab1b04cd0ebe) [sip\_svc\_plat\_free\_async\_memory](structsvc__driver__api.md#a484b7c6ef4777a61e8f4f8e6778a7b45);

[ 101](structsvc__driver__api.md#a79ac1f8410b7f0883ceb0a96823fbdf4) [sip\_svc\_plat\_async\_res\_req\_t](sip__svc__driver_8h.md#aa49a26b4b503e58d23fb5087ed701a0a) [sip\_svc\_plat\_async\_res\_req](structsvc__driver__api.md#a79ac1f8410b7f0883ceb0a96823fbdf4);

[ 102](structsvc__driver__api.md#a1d94fdfb564caa84e3f18f2139ae4fe0) [sip\_svc\_plat\_async\_res\_res\_t](sip__svc__driver_8h.md#a54293f84f9bc86661f8a4bf717ad4754) [sip\_svc\_plat\_async\_res\_res](structsvc__driver__api.md#a1d94fdfb564caa84e3f18f2139ae4fe0);

[ 103](structsvc__driver__api.md#ae148bb010e4a0c2913e1c7425565316a) [sip\_svc\_plat\_get\_error\_code\_t](sip__svc__driver_8h.md#a926eeecea766b2131c03c57111a186f8) [sip\_svc\_plat\_get\_error\_code](structsvc__driver__api.md#ae148bb010e4a0c2913e1c7425565316a);

104};

105

[ 120](sip__svc__driver_8h.md#a881e3794f9e29e12c925cb5dbd443420)\_\_syscall void [sip\_supervisory\_call](sip__svc__driver_8h.md#a881e3794f9e29e12c925cb5dbd443420)(const struct [device](structdevice.md) \*dev, unsigned long function\_id,

121 unsigned long arg0, unsigned long arg1, unsigned long arg2,

122 unsigned long arg3, unsigned long arg4, unsigned long arg5,

123 unsigned long arg6, struct [arm\_smccc\_res](structarm__smccc__res.md) \*res);

124static inline void z\_impl\_sip\_supervisory\_call(const struct [device](structdevice.md) \*dev, unsigned long function\_id,

125 unsigned long arg0, unsigned long arg1,

126 unsigned long arg2, unsigned long arg3,

127 unsigned long arg4, unsigned long arg5,

128 unsigned long arg6, struct [arm\_smccc\_res](structarm__smccc__res.md) \*res)

129{

130 \_\_ASSERT(dev, "dev shouldn't be NULL");

131 const struct [svc\_driver\_api](structsvc__driver__api.md) \*api = [DEV\_API](sip__svc__driver_8h.md#aeae219b400322b0926dd7251dc122bbd)(dev);

132

133 \_\_ASSERT(api->[sip\_supervisory\_call](structsvc__driver__api.md#a5f02e921d2a038616fad9d8d6a052f6b), "sip\_supervisory\_call shouldn't be NULL");

134 \_\_ASSERT(res, "response pointer shouldn't be NULL");

135

136 api->[sip\_supervisory\_call](structsvc__driver__api.md#a5f02e921d2a038616fad9d8d6a052f6b)(dev, function\_id, arg0, arg1, arg2, arg3, arg4, arg5, arg6, res);

137}

138

[ 149](sip__svc__driver_8h.md#a8df36a218cce4c0904c147d498c1322d)\_\_syscall bool [sip\_svc\_plat\_func\_id\_valid](sip__svc__driver_8h.md#a8df36a218cce4c0904c147d498c1322d)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) command,

150 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) func\_id);

151static inline bool z\_impl\_sip\_svc\_plat\_func\_id\_valid(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) command,

152 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) func\_id)

153{

154 \_\_ASSERT(dev, "dev shouldn't be NULL");

155 const struct [svc\_driver\_api](structsvc__driver__api.md) \*api = [DEV\_API](sip__svc__driver_8h.md#aeae219b400322b0926dd7251dc122bbd)(dev);

156

157 \_\_ASSERT(api->[sip\_svc\_plat\_func\_id\_valid](structsvc__driver__api.md#a9f0a7711ef5ba2900d378c0a2805eaf4),

158 "sip\_svc\_plat\_func\_id\_valid func shouldn't be NULL");

159

160 return api->[sip\_svc\_plat\_func\_id\_valid](structsvc__driver__api.md#a9f0a7711ef5ba2900d378c0a2805eaf4)(dev, command, func\_id);

161}

162

[ 172](sip__svc__driver_8h.md#ae52dee0bbba688a73a9726dd4aa482d2)\_\_syscall [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [sip\_svc\_plat\_format\_trans\_id](sip__svc__driver_8h.md#ae52dee0bbba688a73a9726dd4aa482d2)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) client\_idx,

173 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) trans\_idx);

174static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) z\_impl\_sip\_svc\_plat\_format\_trans\_id(const struct [device](structdevice.md) \*dev,

175 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) client\_idx, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) trans\_idx)

176{

177 \_\_ASSERT(dev, "dev shouldn't be NULL");

178 const struct [svc\_driver\_api](structsvc__driver__api.md) \*api = [DEV\_API](sip__svc__driver_8h.md#aeae219b400322b0926dd7251dc122bbd)(dev);

179

180 \_\_ASSERT(api->[sip\_svc\_plat\_format\_trans\_id](structsvc__driver__api.md#a6435b703d30f462c1ec38e533a9c0817),

181 "sip\_svc\_plat\_format\_trans\_id func shouldn't be NULL");

182

183 return api->[sip\_svc\_plat\_format\_trans\_id](structsvc__driver__api.md#a6435b703d30f462c1ec38e533a9c0817)(dev, client\_idx, trans\_idx);

184}

185

[ 194](sip__svc__driver_8h.md#ad0e52f49e7db8cf51ff8cf95e1283994)\_\_syscall [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [sip\_svc\_plat\_get\_trans\_idx](sip__svc__driver_8h.md#ad0e52f49e7db8cf51ff8cf95e1283994)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) trans\_id);

195static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) z\_impl\_sip\_svc\_plat\_get\_trans\_idx(const struct [device](structdevice.md) \*dev,

196 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) trans\_id)

197{

198 \_\_ASSERT(dev, "dev shouldn't be NULL");

199 const struct [svc\_driver\_api](structsvc__driver__api.md) \*api = [DEV\_API](sip__svc__driver_8h.md#aeae219b400322b0926dd7251dc122bbd)(dev);

200

201 \_\_ASSERT(api->[sip\_svc\_plat\_get\_trans\_idx](structsvc__driver__api.md#a30a435265fa828d9fdfcc70664be0945),

202 "sip\_svc\_plat\_get\_trans\_idx func shouldn't be NULL");

203

204 return api->[sip\_svc\_plat\_get\_trans\_idx](structsvc__driver__api.md#a30a435265fa828d9fdfcc70664be0945)(dev, trans\_id);

205}

206

[ 214](sip__svc__driver_8h.md#a095123f7aec80a3e51d75ef248990124)\_\_syscall void [sip\_svc\_plat\_update\_trans\_id](sip__svc__driver_8h.md#a095123f7aec80a3e51d75ef248990124)(const struct [device](structdevice.md) \*dev,

215 struct [sip\_svc\_request](structsip__svc__request.md) \*request, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) trans\_id);

216static inline void z\_impl\_sip\_svc\_plat\_update\_trans\_id(const struct [device](structdevice.md) \*dev,

217 struct [sip\_svc\_request](structsip__svc__request.md) \*request,

218 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) trans\_id)

219{

220 \_\_ASSERT(dev, "dev shouldn't be NULL");

221 const struct [svc\_driver\_api](structsvc__driver__api.md) \*api = [DEV\_API](sip__svc__driver_8h.md#aeae219b400322b0926dd7251dc122bbd)(dev);

222

223 \_\_ASSERT(api->[sip\_svc\_plat\_update\_trans\_id](structsvc__driver__api.md#a0ccdebec2a60d32a1767c5e47bc3ae25),

224 "sip\_svc\_plat\_update\_trans\_id func shouldn't be NULL");

225 \_\_ASSERT(request, "request shouldn't be NULL");

226

227 api->[sip\_svc\_plat\_update\_trans\_id](structsvc__driver__api.md#a0ccdebec2a60d32a1767c5e47bc3ae25)(dev, request, trans\_id);

228}

229

[ 239](sip__svc__driver_8h.md#a3510743d8cf114376b740f3d297c583f)\_\_syscall [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [sip\_svc\_plat\_get\_error\_code](sip__svc__driver_8h.md#a3510743d8cf114376b740f3d297c583f)(const struct [device](structdevice.md) \*dev, struct [arm\_smccc\_res](structarm__smccc__res.md) \*res);

240static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) z\_impl\_sip\_svc\_plat\_get\_error\_code(const struct [device](structdevice.md) \*dev,

241 struct [arm\_smccc\_res](structarm__smccc__res.md) \*res)

242{

243 \_\_ASSERT(dev, "dev shouldn't be NULL");

244 const struct [svc\_driver\_api](structsvc__driver__api.md) \*api = [DEV\_API](sip__svc__driver_8h.md#aeae219b400322b0926dd7251dc122bbd)(dev);

245

246 \_\_ASSERT(api->[sip\_svc\_plat\_get\_error\_code](structsvc__driver__api.md#ae148bb010e4a0c2913e1c7425565316a),

247 "sip\_svc\_plat\_get\_error\_code func shouldn't be NULL");

248 \_\_ASSERT(res, "res shouldn't be NULL");

249

250 return api->[sip\_svc\_plat\_get\_error\_code](structsvc__driver__api.md#ae148bb010e4a0c2913e1c7425565316a)(dev, res);

251}

252

[ 270](sip__svc__driver_8h.md#abb9ff6ec7dea6fc4e104db8cc5e7168b)\_\_syscall int [sip\_svc\_plat\_async\_res\_req](sip__svc__driver_8h.md#abb9ff6ec7dea6fc4e104db8cc5e7168b)(const struct [device](structdevice.md) \*dev, unsigned long \*a0,

271 unsigned long \*a1, unsigned long \*a2, unsigned long \*a3,

272 unsigned long \*a4, unsigned long \*a5, unsigned long \*a6,

273 unsigned long \*a7, char \*buf, size\_t size);

274static inline int z\_impl\_sip\_svc\_plat\_async\_res\_req(const struct [device](structdevice.md) \*dev, unsigned long \*a0,

275 unsigned long \*a1, unsigned long \*a2,

276 unsigned long \*a3, unsigned long \*a4,

277 unsigned long \*a5, unsigned long \*a6,

278 unsigned long \*a7, char \*buf, size\_t size)

279{

280 \_\_ASSERT(dev, "dev shouldn't be NULL");

281 const struct [svc\_driver\_api](structsvc__driver__api.md) \*api = [DEV\_API](sip__svc__driver_8h.md#aeae219b400322b0926dd7251dc122bbd)(dev);

282

283 \_\_ASSERT(api->[sip\_svc\_plat\_async\_res\_req](structsvc__driver__api.md#a79ac1f8410b7f0883ceb0a96823fbdf4),

284 "sip\_svc\_plat\_async\_res\_req func shouldn't be NULL");

285 \_\_ASSERT(a0, "a0 shouldn't be NULL");

286 \_\_ASSERT(a1, "a1 shouldn't be NULL");

287 \_\_ASSERT(a2, "a2 shouldn't be NULL");

288 \_\_ASSERT(a3, "a3 shouldn't be NULL");

289 \_\_ASSERT(a4, "a4 shouldn't be NULL");

290 \_\_ASSERT(a5, "a5 shouldn't be NULL");

291 \_\_ASSERT(a6, "a6 shouldn't be NULL");

292 \_\_ASSERT(a7, "a7 shouldn't be NULL");

293 \_\_ASSERT(((buf == NULL && size == 0) || (buf != NULL && size != 0)),

294 "buf and size should represent a buffer");

295 return api->[sip\_svc\_plat\_async\_res\_req](structsvc__driver__api.md#a79ac1f8410b7f0883ceb0a96823fbdf4)(dev, a0, a1, a2, a3, a4, a5, a6, a7, buf, size);

296}

297

[ 311](sip__svc__driver_8h.md#a0a0577249c2a9f470cd6ec0a60b455c8)\_\_syscall int [sip\_svc\_plat\_async\_res\_res](sip__svc__driver_8h.md#a0a0577249c2a9f470cd6ec0a60b455c8)(const struct [device](structdevice.md) \*dev, struct [arm\_smccc\_res](structarm__smccc__res.md) \*res,

312 char \*buf, size\_t \*size, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*trans\_id);

313static inline int z\_impl\_sip\_svc\_plat\_async\_res\_res(const struct [device](structdevice.md) \*dev,

314 struct [arm\_smccc\_res](structarm__smccc__res.md) \*res, char \*buf,

315 size\_t \*size, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*trans\_id)

316{

317 \_\_ASSERT(dev, "dev shouldn't be NULL");

318 const struct [svc\_driver\_api](structsvc__driver__api.md) \*api = [DEV\_API](sip__svc__driver_8h.md#aeae219b400322b0926dd7251dc122bbd)(dev);

319

320 \_\_ASSERT(api->[sip\_svc\_plat\_async\_res\_res](structsvc__driver__api.md#a1d94fdfb564caa84e3f18f2139ae4fe0),

321 "sip\_svc\_plat\_async\_res\_res func shouldn't be NULL");

322 \_\_ASSERT(res, "res shouldn't be NULL");

323 \_\_ASSERT(buf, "buf shouldn't be NULL");

324 \_\_ASSERT(size, "size shouldn't be NULL");

325 \_\_ASSERT(trans\_id, "buf shouldn't be NULL");

326

327 return api->[sip\_svc\_plat\_async\_res\_res](structsvc__driver__api.md#a1d94fdfb564caa84e3f18f2139ae4fe0)(dev, res, buf, size, trans\_id);

328}

329

[ 336](sip__svc__driver_8h.md#aa4e44eb2af080207821a60f8b3442886)\_\_syscall void [sip\_svc\_plat\_free\_async\_memory](sip__svc__driver_8h.md#aa4e44eb2af080207821a60f8b3442886)(const struct [device](structdevice.md) \*dev,

337 struct [sip\_svc\_request](structsip__svc__request.md) \*request);

338static inline void z\_impl\_sip\_svc\_plat\_free\_async\_memory(const struct [device](structdevice.md) \*dev,

339 struct [sip\_svc\_request](structsip__svc__request.md) \*request)

340{

341 \_\_ASSERT(dev, "dev shouldn't be NULL");

342 const struct [svc\_driver\_api](structsvc__driver__api.md) \*api = [DEV\_API](sip__svc__driver_8h.md#aeae219b400322b0926dd7251dc122bbd)(dev);

343

344 \_\_ASSERT(api->[sip\_svc\_plat\_free\_async\_memory](structsvc__driver__api.md#a484b7c6ef4777a61e8f4f8e6778a7b45),

345 "sip\_svc\_plat\_free\_async\_memory func shouldn't be NULL");

346 \_\_ASSERT(request, "request shouldn't be NULL");

347

348 api->[sip\_svc\_plat\_free\_async\_memory](structsvc__driver__api.md#a484b7c6ef4777a61e8f4f8e6778a7b45)(dev, request);

349}

350

351

352#include <zephyr/syscalls/sip\_svc\_driver.h>

353

354#endif /\* ZEPHYR\_INCLUDE\_SIP\_SVC\_DRIVER\_H\_ \*/

[arm-smccc.h](arm-smccc_8h.md)

[device.h](device_8h.md)

[kernel.h](kernel_8h.md)

Public kernel APIs.

[sip\_svc\_controller.h](sip__svc__controller_8h.md)

[sip\_svc\_plat\_update\_trans\_id](sip__svc__driver_8h.md#a095123f7aec80a3e51d75ef248990124)

void sip\_svc\_plat\_update\_trans\_id(const struct device \*dev, struct sip\_svc\_request \*request, uint32\_t trans\_id)

Update transaction id for sip\_svc\_request for lower layer.

[sip\_svc\_plat\_async\_res\_res](sip__svc__driver_8h.md#a0a0577249c2a9f470cd6ec0a60b455c8)

int sip\_svc\_plat\_async\_res\_res(const struct device \*dev, struct arm\_smccc\_res \*res, char \*buf, size\_t \*size, uint32\_t \*trans\_id)

Check the response of polling supervisory call and retrieve the response size and transaction id.

[sip\_supervisory\_call\_t](sip__svc__driver_8h.md#a15714e3852882693de6c9c7f2229bcd1)

void(\* sip\_supervisory\_call\_t)(const struct device \*dev, unsigned long function\_id, unsigned long arg0, unsigned long arg1, unsigned long arg2, unsigned long arg3, unsigned long arg4, unsigned long arg5, unsigned long arg6, struct arm\_smccc\_res \*res)

Callback API for executing the supervisory call See sip\_supervisory\_call() for argument description.

**Definition** sip\_svc\_driver.h:28

[sip\_svc\_plat\_get\_error\_code](sip__svc__driver_8h.md#a3510743d8cf114376b740f3d297c583f)

uint32\_t sip\_svc\_plat\_get\_error\_code(const struct device \*dev, struct arm\_smccc\_res \*res)

Retrieve the error code from arm\_smccc\_res response.

[sip\_svc\_plat\_get\_trans\_idx\_t](sip__svc__driver_8h.md#a35145ddf422e8782b4ec37270b04d98c)

uint32\_t(\* sip\_svc\_plat\_get\_trans\_idx\_t)(const struct device \*dev, uint32\_t trans\_id)

Callback API for retrieving client transaction id from transaction id See sip\_svc\_plat\_get\_trans\_idx(...

**Definition** sip\_svc\_driver.h:51

[sip\_svc\_plat\_format\_trans\_id\_t](sip__svc__driver_8h.md#a3cf78c760c6eae2091e92329e54b1a31)

uint32\_t(\* sip\_svc\_plat\_format\_trans\_id\_t)(const struct device \*dev, uint32\_t client\_idx, uint32\_t trans\_idx)

Callback API for generating the transaction id from client id.

**Definition** sip\_svc\_driver.h:44

[sip\_svc\_plat\_async\_res\_res\_t](sip__svc__driver_8h.md#a54293f84f9bc86661f8a4bf717ad4754)

int(\* sip\_svc\_plat\_async\_res\_res\_t)(const struct device \*dev, struct arm\_smccc\_res \*res, char \*buf, size\_t \*size, uint32\_t \*trans\_id)

Callback API to check the response of polling request See sip\_svc\_plat\_async\_res\_res() for argument d...

**Definition** sip\_svc\_driver.h:80

[sip\_supervisory\_call](sip__svc__driver_8h.md#a881e3794f9e29e12c925cb5dbd443420)

void sip\_supervisory\_call(const struct device \*dev, unsigned long function\_id, unsigned long arg0, unsigned long arg1, unsigned long arg2, unsigned long arg3, unsigned long arg4, unsigned long arg5, unsigned long arg6, struct arm\_smccc\_res \*res)

supervisory call function which will execute the smc/hvc call

[sip\_svc\_plat\_func\_id\_valid](sip__svc__driver_8h.md#a8df36a218cce4c0904c147d498c1322d)

bool sip\_svc\_plat\_func\_id\_valid(const struct device \*dev, uint32\_t command, uint32\_t func\_id)

Validate the function id for the supervisory call.

[sip\_svc\_plat\_get\_error\_code\_t](sip__svc__driver_8h.md#a926eeecea766b2131c03c57111a186f8)

uint32\_t(\* sip\_svc\_plat\_get\_error\_code\_t)(const struct device \*dev, struct arm\_smccc\_res \*res)

Callback API for retrieving error code from a supervisory call response.

**Definition** sip\_svc\_driver.h:87

[sip\_svc\_plat\_update\_trans\_id\_t](sip__svc__driver_8h.md#a9d61db0484e2aacce4515290ffb4450c)

void(\* sip\_svc\_plat\_update\_trans\_id\_t)(const struct device \*dev, struct sip\_svc\_request \*request, uint32\_t trans\_id)

Callback API for updating transaction id for request packet for lower layer See sip\_svc\_plat\_update\_t...

**Definition** sip\_svc\_driver.h:57

[sip\_svc\_plat\_async\_res\_req\_t](sip__svc__driver_8h.md#aa49a26b4b503e58d23fb5087ed701a0a)

int(\* sip\_svc\_plat\_async\_res\_req\_t)(const struct device \*dev, unsigned long \*a0, unsigned long \*a1, unsigned long \*a2, unsigned long \*a3, unsigned long \*a4, unsigned long \*a5, unsigned long \*a6, unsigned long \*a7, char \*buf, size\_t size)

Callback API to construct Polling packet for ASYNC transaction.

**Definition** sip\_svc\_driver.h:71

[sip\_svc\_plat\_free\_async\_memory](sip__svc__driver_8h.md#aa4e44eb2af080207821a60f8b3442886)

void sip\_svc\_plat\_free\_async\_memory(const struct device \*dev, struct sip\_svc\_request \*request)

Free the command buffer used for ASYNC packet after sending it to lower layers.

[sip\_svc\_plat\_free\_async\_memory\_t](sip__svc__driver_8h.md#ab32e31bdba00ff66303fab1b04cd0ebe)

void(\* sip\_svc\_plat\_free\_async\_memory\_t)(const struct device \*dev, struct sip\_svc\_request \*request)

Callback API for freeing command buffer in ASYNC packets See sip\_svc\_plat\_free\_async\_memory() for arg...

**Definition** sip\_svc\_driver.h:64

[sip\_svc\_plat\_async\_res\_req](sip__svc__driver_8h.md#abb9ff6ec7dea6fc4e104db8cc5e7168b)

int sip\_svc\_plat\_async\_res\_req(const struct device \*dev, unsigned long \*a0, unsigned long \*a1, unsigned long \*a2, unsigned long \*a3, unsigned long \*a4, unsigned long \*a5, unsigned long \*a6, unsigned long \*a7, char \*buf, size\_t size)

Set arguments for polling supervisory call.

[sip\_svc\_plat\_func\_id\_valid\_t](sip__svc__driver_8h.md#ac5921c9cdc00604651696e1580f30797)

bool(\* sip\_svc\_plat\_func\_id\_valid\_t)(const struct device \*dev, uint32\_t command, uint32\_t func\_id)

Callback API for validating function id for the supervisory call.

**Definition** sip\_svc\_driver.h:37

[sip\_svc\_plat\_get\_trans\_idx](sip__svc__driver_8h.md#ad0e52f49e7db8cf51ff8cf95e1283994)

uint32\_t sip\_svc\_plat\_get\_trans\_idx(const struct device \*dev, uint32\_t trans\_id)

Retrieve client transaction id from packet transaction id.

[sip\_svc\_plat\_format\_trans\_id](sip__svc__driver_8h.md#ae52dee0bbba688a73a9726dd4aa482d2)

uint32\_t sip\_svc\_plat\_format\_trans\_id(const struct device \*dev, uint32\_t client\_idx, uint32\_t trans\_idx)

Formats and generates the transaction id from client id.

[DEV\_API](sip__svc__driver_8h.md#aeae219b400322b0926dd7251dc122bbd)

#define DEV\_API(dev)

**Definition** sip\_svc\_driver.h:16

[sip\_svc\_proto.h](sip__svc__proto_8h.md)

Arm SiP services communication protocol between service provider and client.

[bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)

#define bool

**Definition** stdbool.h:13

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[arm\_smccc\_res](structarm__smccc__res.md)

**Definition** arm-smccc.h:14

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:412

[sip\_svc\_request](structsip__svc__request.md)

SiP Service communication protocol request format.

**Definition** sip\_svc\_proto.h:133

[svc\_driver\_api](structsvc__driver__api.md)

API structure for sip\_svc driver.

**Definition** sip\_svc\_driver.h:94

[svc\_driver\_api::sip\_svc\_plat\_update\_trans\_id](structsvc__driver__api.md#a0ccdebec2a60d32a1767c5e47bc3ae25)

sip\_svc\_plat\_update\_trans\_id\_t sip\_svc\_plat\_update\_trans\_id

**Definition** sip\_svc\_driver.h:99

[svc\_driver\_api::sip\_svc\_plat\_async\_res\_res](structsvc__driver__api.md#a1d94fdfb564caa84e3f18f2139ae4fe0)

sip\_svc\_plat\_async\_res\_res\_t sip\_svc\_plat\_async\_res\_res

**Definition** sip\_svc\_driver.h:102

[svc\_driver\_api::sip\_svc\_plat\_get\_trans\_idx](structsvc__driver__api.md#a30a435265fa828d9fdfcc70664be0945)

sip\_svc\_plat\_get\_trans\_idx\_t sip\_svc\_plat\_get\_trans\_idx

**Definition** sip\_svc\_driver.h:98

[svc\_driver\_api::sip\_svc\_plat\_free\_async\_memory](structsvc__driver__api.md#a484b7c6ef4777a61e8f4f8e6778a7b45)

sip\_svc\_plat\_free\_async\_memory\_t sip\_svc\_plat\_free\_async\_memory

**Definition** sip\_svc\_driver.h:100

[svc\_driver\_api::sip\_supervisory\_call](structsvc__driver__api.md#a5f02e921d2a038616fad9d8d6a052f6b)

sip\_supervisory\_call\_t sip\_supervisory\_call

**Definition** sip\_svc\_driver.h:95

[svc\_driver\_api::sip\_svc\_plat\_format\_trans\_id](structsvc__driver__api.md#a6435b703d30f462c1ec38e533a9c0817)

sip\_svc\_plat\_format\_trans\_id\_t sip\_svc\_plat\_format\_trans\_id

**Definition** sip\_svc\_driver.h:97

[svc\_driver\_api::sip\_svc\_plat\_async\_res\_req](structsvc__driver__api.md#a79ac1f8410b7f0883ceb0a96823fbdf4)

sip\_svc\_plat\_async\_res\_req\_t sip\_svc\_plat\_async\_res\_req

**Definition** sip\_svc\_driver.h:101

[svc\_driver\_api::sip\_svc\_plat\_func\_id\_valid](structsvc__driver__api.md#a9f0a7711ef5ba2900d378c0a2805eaf4)

sip\_svc\_plat\_func\_id\_valid\_t sip\_svc\_plat\_func\_id\_valid

**Definition** sip\_svc\_driver.h:96

[svc\_driver\_api::sip\_svc\_plat\_get\_error\_code](structsvc__driver__api.md#ae148bb010e4a0c2913e1c7425565316a)

sip\_svc\_plat\_get\_error\_code\_t sip\_svc\_plat\_get\_error\_code

**Definition** sip\_svc\_driver.h:103

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [sip\_svc](dir_be59f4c2e7724c8d2ef47362c82e9052.md)
- [sip\_svc\_driver.h](sip__svc__driver_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
