---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/rtio__spsc_8h_source.html
original_path: doxygen/html/rtio__spsc_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

rtio\_spsc.h

[Go to the documentation of this file.](rtio__spsc_8h.md)

1/\*

2 \* Copyright (c) 2022 Intel Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7

8#ifndef ZEPHYR\_RTIO\_SPSC\_H\_

9#define ZEPHYR\_RTIO\_SPSC\_H\_

10

11#include <[stdint.h](stdint_8h.md)>

12#include <[stdbool.h](stdbool_8h.md)>

13#include <[zephyr/toolchain/common.h](common_8h.md)>

14#include <[zephyr/sys/atomic.h](atomic_8h.md)>

15#include <[zephyr/sys/util\_macro.h](util__macro_8h.md)>

16

23

53

60struct rtio\_spsc {

61 /\* private value only the producer thread should mutate \*/

62 unsigned long acquire;

63

64 /\* private value only the consumer thread should mutate \*/

65 unsigned long consume;

66

67 /\* producer mutable, consumer readable \*/

68 [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) in;

69

70 /\* consumer mutable, producer readable \*/

71 [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) out;

72

73 /\* mask used to automatically wrap values \*/

74 const unsigned long mask;

75};

76

[ 83](group__rtio__spsc.md#ga54a199d7030fad8387acf057539f2854)#define RTIO\_SPSC\_INITIALIZER(sz, buf) \

84 { \

85 .\_spsc = { \

86 .acquire = 0, \

87 .consume = 0, \

88 .in = ATOMIC\_INIT(0), \

89 .out = ATOMIC\_INIT(0), \

90 .mask = sz - 1, \

91 }, \

92 .buffer = buf, \

93 }

94

[ 101](group__rtio__spsc.md#ga6d1f8fb2f7caf60680e434557b1947ad)#define RTIO\_SPSC\_DECLARE(name, type) \

102 static struct rtio\_spsc\_##name { \

103 struct rtio\_spsc \_spsc; \

104 type \* const buffer; \

105 }

106

[ 114](group__rtio__spsc.md#ga03de50debdf6a3acca9f02f4bc9b7ad9)#define RTIO\_SPSC\_DEFINE(name, type, sz) \

115 BUILD\_ASSERT(IS\_POWER\_OF\_TWO(sz)); \

116 static type \_\_spsc\_buf\_##name[sz]; \

117 RTIO\_SPSC\_DECLARE(name, type) name = RTIO\_SPSC\_INITIALIZER(sz, \_\_spsc\_buf\_##name);

118

[ 124](group__rtio__spsc.md#gad47e0fcf59138828b74b29f7c59c55c2)#define rtio\_spsc\_size(spsc) ((spsc)->\_spsc.mask + 1)

125

133#define z\_rtio\_spsc\_mask(spsc, i) ((i) & (spsc)->\_spsc.mask)

134

135

140#define z\_rtio\_spsc\_in(spsc) (unsigned long)atomic\_get(&(spsc)->\_spsc.in)

141

146#define z\_rtio\_spsc\_out(spsc) (unsigned long)atomic\_get(&(spsc)->\_spsc.out)

147

[ 156](group__rtio__spsc.md#ga803ff0ddddc3ca3fc37b6e39e9b65746)#define rtio\_spsc\_reset(spsc) \

157 ({ \

158 (spsc)->\_spsc.consume = 0; \

159 (spsc)->\_spsc.acquire = 0; \

160 atomic\_set(&(spsc)->\_spsc.in, 0); \

161 atomic\_set(&(spsc)->\_spsc.out, 0); \

162 })

163

[ 171](group__rtio__spsc.md#ga31521b366a5ab60852b799dfa8d1fca4)#define rtio\_spsc\_acquire(spsc) \

172 ({ \

173 unsigned long idx = z\_rtio\_spsc\_in(spsc) + (spsc)->\_spsc.acquire; \

174 bool spsc\_acq = (idx - z\_rtio\_spsc\_out(spsc)) < rtio\_spsc\_size(spsc); \

175 if (spsc\_acq) { \

176 (spsc)->\_spsc.acquire += 1; \

177 } \

178 spsc\_acq ? &((spsc)->buffer[z\_rtio\_spsc\_mask(spsc, idx)]) : NULL; \

179 })

180

[ 188](group__rtio__spsc.md#gaf7ac949ed6a896b2cb39141109f43f2f)#define rtio\_spsc\_produce(spsc) \

189 ({ \

190 if ((spsc)->\_spsc.acquire > 0) { \

191 (spsc)->\_spsc.acquire -= 1; \

192 atomic\_add(&(spsc)->\_spsc.in, 1); \

193 } \

194 })

195

[ 204](group__rtio__spsc.md#ga9eb327619c7dc567d5a70d538db95f2c)#define rtio\_spsc\_produce\_all(spsc) \

205 ({ \

206 if ((spsc)->\_spsc.acquire > 0) { \

207 unsigned long acquired = (spsc)->\_spsc.acquire; \

208 (spsc)->\_spsc.acquire = 0; \

209 atomic\_add(&(spsc)->\_spsc.in, acquired); \

210 } \

211 })

212

[ 220](group__rtio__spsc.md#ga4f2be93f9b094269db5a844a0038b582)#define rtio\_spsc\_drop\_all(spsc) \

221 do { \

222 (spsc)->\_spsc.acquire = 0; \

223 } while (false)

224

[ 232](group__rtio__spsc.md#ga163a7a6eedff934a2bc7b093c0bc8de5)#define rtio\_spsc\_consume(spsc) \

233 ({ \

234 unsigned long idx = z\_rtio\_spsc\_out(spsc) + (spsc)->\_spsc.consume; \

235 bool has\_consumable = (idx != z\_rtio\_spsc\_in(spsc)); \

236 if (has\_consumable) { \

237 (spsc)->\_spsc.consume += 1; \

238 } \

239 has\_consumable ? &((spsc)->buffer[z\_rtio\_spsc\_mask(spsc, idx)]) : NULL; \

240 })

241

[ 247](group__rtio__spsc.md#gad6e8916b9bdd9dbd00fddacec39b8898)#define rtio\_spsc\_release(spsc) \

248 ({ \

249 if ((spsc)->\_spsc.consume > 0) { \

250 (spsc)->\_spsc.consume -= 1; \

251 atomic\_add(&(spsc)->\_spsc.out, 1); \

252 } \

253 })

254

255

[ 261](group__rtio__spsc.md#ga3d0ab7e1a3e777c22c60e711350e9d4a)#define rtio\_spsc\_release\_all(spsc) \

262 ({ \

263 if ((spsc)->\_spsc.consume > 0) { \

264 unsigned long consumed = (spsc)->\_spsc.consume; \

265 (spsc)->\_spsc.consume = 0; \

266 atomic\_add(&(spsc)->\_spsc.out, consumed); \

267 } \

268 })

269

[ 275](group__rtio__spsc.md#gaa214fb1ca3172d16ba6b6c07fb1d0053)#define rtio\_spsc\_acquirable(spsc) \

276 ({ \

277 (((spsc)->\_spsc.in + (spsc)->\_spsc.acquire) - (spsc)->\_spsc.out) - \

278 rtio\_spsc\_size(spsc); \

279 })

280

[ 286](group__rtio__spsc.md#ga69cdbead4d23d77d952490ab6045c046)#define rtio\_spsc\_consumable(spsc) \

287 ({ (spsc)->\_spsc.in - (spsc)->\_spsc.out - (spsc)->\_spsc.consume; })

288

[ 296](group__rtio__spsc.md#ga614c7cc6abc2222735e2a9581b5b347f)#define rtio\_spsc\_peek(spsc) \

297 ({ \

298 unsigned long idx = z\_rtio\_spsc\_out(spsc) + (spsc)->\_spsc.consume; \

299 bool has\_consumable = (idx != z\_rtio\_spsc\_in(spsc)); \

300 has\_consumable ? &((spsc)->buffer[z\_rtio\_spsc\_mask(spsc, idx)]) : NULL; \

301 })

302

[ 312](group__rtio__spsc.md#ga91e8862b750c8bdad27b93023d484b68)#define rtio\_spsc\_next(spsc, item) \

313 ({ \

314 unsigned long idx = ((item) - (spsc)->buffer); \

315 bool has\_next = z\_rtio\_spsc\_mask(spsc, (idx + 1)) != \

316 (z\_rtio\_spsc\_mask(spsc, z\_rtio\_spsc\_in(spsc))); \

317 has\_next ? &((spsc)->buffer[z\_rtio\_spsc\_mask((spsc), idx + 1)]) : NULL; \

318 })

319

[ 328](group__rtio__spsc.md#gaf02b036e6131ca3a320e085221e665b9)#define rtio\_spsc\_prev(spsc, item) \

329 ({ \

330 unsigned long idx = ((item) - &(spsc)->buffer[0]) / sizeof((spsc)->buffer[0]); \

331 bool has\_prev = idx != z\_rtio\_spsc\_mask(spsc, z\_rtio\_spsc\_out(spsc)); \

332 has\_prev ? &((spsc)->buffer[z\_rtio\_spsc\_mask(spsc, idx - 1)]) : NULL; \

333 })

334

338

339#endif /\* ZEPHYR\_RTIO\_SPSC\_H\_ \*/

[atomic.h](atomic_8h.md)

[atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8)

long atomic\_t

**Definition** atomic\_types.h:15

[common.h](common_8h.md)

Common toolchain abstraction.

[stdbool.h](stdbool_8h.md)

[stdint.h](stdint_8h.md)

[util\_macro.h](util__macro_8h.md)

Macro utilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [rtio](dir_2c800b92938ab205b51fc9bd951bff11.md)
- [rtio\_spsc.h](rtio__spsc_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
