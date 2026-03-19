---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/log__core_8h_source.html
original_path: doxygen/html/log__core_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

log\_core.h

[Go to the documentation of this file.](log__core_8h.md)

1/\*

2 \* Copyright (c) 2018 Nordic Semiconductor ASA

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef ZEPHYR\_INCLUDE\_LOGGING\_LOG\_CORE\_H\_

7#define ZEPHYR\_INCLUDE\_LOGGING\_LOG\_CORE\_H\_

8

9#include <[zephyr/logging/log\_msg.h](log__msg_8h.md)>

10#include <[zephyr/logging/log\_instance.h](log__instance_8h.md)>

11#include <[stdbool.h](stdbool_8h.md)>

12#include <[stdint.h](stdint_8h.md)>

13#include <stdarg.h>

14#include <[zephyr/sys/util.h](sys_2util_8h.md)>

15

16/\* This header file keeps all macros and functions needed for creating logging

17 \* messages (macros like @ref LOG\_ERR).

18 \*/

[ 19](log__core_8h.md#a43dece650f96e7cf2a4e535c9bd4804a)#define LOG\_LEVEL\_NONE 0

[ 20](log__core_8h.md#ab3a03740685cbdaa375e2bde8247fdc6)#define LOG\_LEVEL\_ERR 1

[ 21](log__core_8h.md#a54f5db1327d9fdbaecbb03a6969de97b)#define LOG\_LEVEL\_WRN 2

[ 22](log__core_8h.md#a281bc2ce5315e6fae369796c0fdf5c1d)#define LOG\_LEVEL\_INF 3

[ 23](log__core_8h.md#ad1f7d41b1af28ba81ea63d24c9b690cc)#define LOG\_LEVEL\_DBG 4

24

25#ifdef \_\_cplusplus

26extern "C" {

27#endif

28

29#ifndef CONFIG\_LOG

[ 30](log__core_8h.md#ac618493585bc226f18f36b6a2ad7e8d5)#define CONFIG\_LOG\_DEFAULT\_LEVEL 0

[ 31](log__core_8h.md#a97df309d4ec6704223193647b6faf819)#define CONFIG\_LOG\_MAX\_LEVEL 0

32#endif

33

34/\* Id of local domain. \*/

35#define Z\_LOG\_LOCAL\_DOMAIN\_ID 0

36

[ 37](log__core_8h.md#add313a51d2d73b99ad0d00fc5184312f)#define LOG\_FUNCTION\_PREFIX\_MASK \

38 (((uint32\_t)IS\_ENABLED(CONFIG\_LOG\_FUNC\_NAME\_PREFIX\_ERR) << \

39 LOG\_LEVEL\_ERR) | \

40 ((uint32\_t)IS\_ENABLED(CONFIG\_LOG\_FUNC\_NAME\_PREFIX\_WRN) << \

41 LOG\_LEVEL\_WRN) | \

42 ((uint32\_t)IS\_ENABLED(CONFIG\_LOG\_FUNC\_NAME\_PREFIX\_INF) << \

43 LOG\_LEVEL\_INF) | \

44 ((uint32\_t)IS\_ENABLED(CONFIG\_LOG\_FUNC\_NAME\_PREFIX\_DBG) << LOG\_LEVEL\_DBG))

45

50#define Z\_LOG\_RESOLVED\_LEVEL(\_level, \_default) \

51 Z\_LOG\_RESOLVED\_LEVEL1(\_level, \_default)

52

53#define Z\_LOG\_RESOLVED\_LEVEL1(\_level, \_default) \

54 \_\_COND\_CODE(\_LOG\_XXXX##\_level, (\_level), (\_default))

55

56#define \_LOG\_XXXX0 \_LOG\_YYYY,

57#define \_LOG\_XXXX1 \_LOG\_YYYY,

58#define \_LOG\_XXXX2 \_LOG\_YYYY,

59#define \_LOG\_XXXX3 \_LOG\_YYYY,

60#define \_LOG\_XXXX4 \_LOG\_YYYY,

61

76#define Z\_LOG\_EVAL(\_eval\_level, \_iftrue, \_iffalse) \

77 Z\_LOG\_EVAL1(\_eval\_level, \_iftrue, \_iffalse)

78

79#define Z\_LOG\_EVAL1(\_eval\_level, \_iftrue, \_iffalse) \

80 \_\_COND\_CODE(\_LOG\_ZZZZ##\_eval\_level, \_iftrue, \_iffalse)

81

82#define \_LOG\_ZZZZ1 \_LOG\_YYYY,

83#define \_LOG\_ZZZZ2 \_LOG\_YYYY,

84#define \_LOG\_ZZZZ3 \_LOG\_YYYY,

85#define \_LOG\_ZZZZ4 \_LOG\_YYYY,

86

[ 91](log__core_8h.md#a85c70bfd98bbc66a35806010a206237e)#define LOG\_CURRENT\_MODULE\_ID() (\_\_log\_level != 0 ? \

92 log\_const\_source\_id(\_\_log\_current\_const\_data) : 0U)

93

94/\* Set of defines that are set to 1 if function name prefix is enabled for given level. \*/

95#define Z\_LOG\_FUNC\_PREFIX\_0 0

96#define Z\_LOG\_FUNC\_PREFIX\_1 COND\_CODE\_1(CONFIG\_LOG\_FUNC\_NAME\_PREFIX\_ERR, (1), (0))

97#define Z\_LOG\_FUNC\_PREFIX\_2 COND\_CODE\_1(CONFIG\_LOG\_FUNC\_NAME\_PREFIX\_WRN, (1), (0))

98#define Z\_LOG\_FUNC\_PREFIX\_3 COND\_CODE\_1(CONFIG\_LOG\_FUNC\_NAME\_PREFIX\_INF, (1), (0))

99#define Z\_LOG\_FUNC\_PREFIX\_4 COND\_CODE\_1(CONFIG\_LOG\_FUNC\_NAME\_PREFIX\_DBG, (1), (0))

100

110#define Z\_LOG\_STR\_WITH\_PREFIX2(...) \

111 "%s: " GET\_ARG\_N(1, \_\_VA\_ARGS\_\_), (const char \*)\_\_func\_\_\

112 COND\_CODE\_0(NUM\_VA\_ARGS\_LESS\_1(\_\_VA\_ARGS\_\_),\

113 (),\

114 (, GET\_ARGS\_LESS\_N(1, \_\_VA\_ARGS\_\_))\

115 )

116

117/\* Macro handles case when no format string is provided: e.g. LOG\_DBG().

118 \* Handling of format string is deferred to the next level macro.

119 \*/

120#define Z\_LOG\_STR\_WITH\_PREFIX(...) \

121 COND\_CODE\_0(NUM\_VA\_ARGS\_LESS\_1(\_, ##\_\_VA\_ARGS\_\_), \

122 ("%s", (const char \*)\_\_func\_\_), \

123 (Z\_LOG\_STR\_WITH\_PREFIX2(\_\_VA\_ARGS\_\_)))

124

130#define Z\_LOG\_STR(\_level, ...) \

131 COND\_CODE\_1(UTIL\_CAT(Z\_LOG\_FUNC\_PREFIX\_##\_level), \

132 (Z\_LOG\_STR\_WITH\_PREFIX(\_\_VA\_ARGS\_\_)), (\_\_VA\_ARGS\_\_))

133

134#define Z\_LOG\_LEVEL\_CHECK(\_level, \_check\_level, \_default\_level) \

135 ((\_level) <= Z\_LOG\_RESOLVED\_LEVEL(\_check\_level, \_default\_level))

136

146#define Z\_LOG\_CONST\_LEVEL\_CHECK(\_level) \

147 (IS\_ENABLED(CONFIG\_LOG) && \

148 (Z\_LOG\_LEVEL\_CHECK(\_level, CONFIG\_LOG\_OVERRIDE\_LEVEL, LOG\_LEVEL\_NONE) \

149 || \

150 ((IS\_ENABLED(CONFIG\_LOG\_OVERRIDE\_LEVEL) == false) && \

151 ((\_level) <= \_\_log\_level) && \

152 ((\_level) <= CONFIG\_LOG\_MAX\_LEVEL) \

153 ) \

154 ))

155

170#define Z\_LOG\_STATIC\_INST\_LEVEL\_CHECK(\_level, \_inst, \_source) \

171 (IS\_ENABLED(CONFIG\_LOG\_RUNTIME\_FILTERING) || !\_inst || \

172 (\_level <= ((const struct log\_source\_const\_data \*)\_source)->level))

173

184#define Z\_LOG\_DYNAMIC\_LEVEL\_CHECK(\_level, \_source) \

185 (!IS\_ENABLED(CONFIG\_LOG\_RUNTIME\_FILTERING) || k\_is\_user\_context() || \

186 ((\_level) <= Z\_LOG\_RUNTIME\_FILTER(((struct log\_source\_dynamic\_data \*)\_source)->filters)))

187

199#define Z\_LOG\_LEVEL\_ALL\_CHECK(\_level, \_inst, \_source) \

200 (Z\_LOG\_CONST\_LEVEL\_CHECK(\_level) && \

201 Z\_LOG\_STATIC\_INST\_LEVEL\_CHECK(\_level, \_inst, \_source) && \

202 Z\_LOG\_DYNAMIC\_LEVEL\_CHECK(\_level, \_source))

203

209#define Z\_LOG\_CURRENT\_DATA() \

210 COND\_CODE\_1(CONFIG\_LOG\_RUNTIME\_FILTERING, \

211 (\_\_log\_current\_dynamic\_data), (\_\_log\_current\_const\_data))

212

213/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*/

214/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* Definitions used by minimal logging \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*/

215/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*/

216void z\_log\_minimal\_hexdump\_print(int level, const void \*data, size\_t size);

217void z\_log\_minimal\_vprintk(const char \*fmt, va\_list ap);

218void z\_log\_minimal\_printk(const char \*fmt, ...);

219

220#define Z\_LOG\_TO\_PRINTK(\_level, fmt, ...) do { \

221 z\_log\_minimal\_printk("%c: " fmt "\n", \

222 z\_log\_minimal\_level\_to\_char(\_level), \

223 ##\_\_VA\_ARGS\_\_); \

224} while (false)

225

226#define Z\_LOG\_TO\_VPRINTK(\_level, fmt, valist) do { \

227 z\_log\_minimal\_printk("%c: ", z\_log\_minimal\_level\_to\_char(\_level)); \

228 z\_log\_minimal\_vprintk(fmt, valist); \

229 z\_log\_minimal\_printk("\n"); \

230} while (false)

231

232static inline char z\_log\_minimal\_level\_to\_char(int level)

233{

234 switch (level) {

235 case [LOG\_LEVEL\_ERR](log__core_8h.md#ab3a03740685cbdaa375e2bde8247fdc6):

236 return 'E';

237 case [LOG\_LEVEL\_WRN](log__core_8h.md#a54f5db1327d9fdbaecbb03a6969de97b):

238 return 'W';

239 case [LOG\_LEVEL\_INF](log__core_8h.md#a281bc2ce5315e6fae369796c0fdf5c1d):

240 return 'I';

241 case [LOG\_LEVEL\_DBG](log__core_8h.md#ad1f7d41b1af28ba81ea63d24c9b690cc):

242 return 'D';

243 default:

244 return '?';

245 }

246}

247

248#define Z\_LOG\_INST(\_inst) COND\_CODE\_1(CONFIG\_LOG, (\_inst), NULL)

249

250/\* If strings are removed from the binary then there is a risk of creating invalid

251 \* cbprintf package if %p is used with character pointer which is interpreted as

252 \* string. A compile time check is performed (since format string is known at

253 \* compile time) and check fails logging message is not created but error is

254 \* emitted instead. String check may increase compilation time so it is not

255 \* always performed (could significantly increase CI time).

256 \*/

257#ifdef CONFIG\_LOG\_FMT\_STRING\_VALIDATE

258#define LOG\_STRING\_WARNING(\_mode, \_src, ...) \

259 Z\_LOG\_MSG\_CREATE(UTIL\_NOT(IS\_ENABLED(CONFIG\_USERSPACE)), \_mode, \

260 Z\_LOG\_LOCAL\_DOMAIN\_ID, \_src, LOG\_LEVEL\_ERR, NULL, 0, \

261 "char pointer used for %%p, cast to void \*:\"%s\"", \

262 GET\_ARG\_N(1, \_\_VA\_ARGS\_\_))

263

264#define LOG\_POINTERS\_VALIDATE(string\_ok, ...) \

265 \_Pragma("GCC diagnostic push") \

266 \_Pragma("GCC diagnostic ignored \"-Wpointer-arith\"") \

267 string\_ok = Z\_CBPRINTF\_POINTERS\_VALIDATE(\_\_VA\_ARGS\_\_); \

268 \_Pragma("GCC diagnostic pop")

269#else

[ 270](log__core_8h.md#a6d29de8e144ab8e57f42f096b0b47ca0)#define LOG\_POINTERS\_VALIDATE(string\_ok, ...) string\_ok = true

[ 271](log__core_8h.md#ad9fb171d1afec420ff46f6e0e4b0481d)#define LOG\_STRING\_WARNING(\_mode, \_src, ...)

272#endif

273

274/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*/

275/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* Macros for standard logging \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*/

276/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*/

292#define Z\_LOG2(\_level, \_inst, \_source, ...) \

293 do { \

294 if (!Z\_LOG\_LEVEL\_ALL\_CHECK(\_level, \_inst, \_source)) { \

295 break; \

296 } \

297 if (IS\_ENABLED(CONFIG\_LOG\_MODE\_MINIMAL)) { \

298 Z\_LOG\_TO\_PRINTK(\_level, \_\_VA\_ARGS\_\_); \

299 break; \

300 } \

301 int \_mode; \

302 bool string\_ok; \

303 LOG\_POINTERS\_VALIDATE(string\_ok, \_\_VA\_ARGS\_\_); \

304 if (!string\_ok) { \

305 LOG\_STRING\_WARNING(\_mode, \_source, \_\_VA\_ARGS\_\_); \

306 break; \

307 } \

308 Z\_LOG\_MSG\_CREATE(UTIL\_NOT(IS\_ENABLED(CONFIG\_USERSPACE)), \_mode, \

309 Z\_LOG\_LOCAL\_DOMAIN\_ID, \_source, \_level, NULL, 0, \_\_VA\_ARGS\_\_); \

310 (void)\_mode; \

311 if (false) { \

312 /\* Arguments checker present but never evaluated.\*/ \

313 /\* Placed here to ensure that \_\_VA\_ARGS\_\_ are\*/ \

314 /\* evaluated once when log is enabled.\*/ \

315 z\_log\_printf\_arg\_checker(\_\_VA\_ARGS\_\_); \

316 } \

317 } while (false)

318

319#define Z\_LOG(\_level, ...) Z\_LOG2(\_level, 0, Z\_LOG\_CURRENT\_DATA(), \_\_VA\_ARGS\_\_)

320#define Z\_LOG\_INSTANCE(\_level, \_inst, ...) Z\_LOG2(\_level, 1, Z\_LOG\_INST(\_inst), \_\_VA\_ARGS\_\_)

321

322/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*/

323/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* Macros for hexdump logging \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*/

324/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*/

345#define Z\_LOG\_HEXDUMP2(\_level, \_inst, \_source, \_data, \_len, ...) \

346 do { \

347 if (!Z\_LOG\_LEVEL\_ALL\_CHECK(\_level, \_inst, \_source)) { \

348 break; \

349 } \

350 const char \*\_str = GET\_ARG\_N(1, \_\_VA\_ARGS\_\_); \

351 if (IS\_ENABLED(CONFIG\_LOG\_MODE\_MINIMAL)) { \

352 Z\_LOG\_TO\_PRINTK(\_level, "%s", \_str); \

353 z\_log\_minimal\_hexdump\_print((\_level), (const char \*)(\_data), (\_len)); \

354 break; \

355 } \

356 int mode; \

357 Z\_LOG\_MSG\_CREATE(UTIL\_NOT(IS\_ENABLED(CONFIG\_USERSPACE)), mode, \

358 Z\_LOG\_LOCAL\_DOMAIN\_ID, \_source, \_level, \_data, \_len, \

359 COND\_CODE\_0(NUM\_VA\_ARGS\_LESS\_1(\_, ##\_\_VA\_ARGS\_\_), \

360 (), \

361 (COND\_CODE\_0(NUM\_VA\_ARGS\_LESS\_1(\_\_VA\_ARGS\_\_), \

362 ("%s", \_\_VA\_ARGS\_\_), (\_\_VA\_ARGS\_\_))))); \

363 } while (false)

364

365#define Z\_LOG\_HEXDUMP(\_level, \_data, \_length, ...) \

366 Z\_LOG\_HEXDUMP2(\_level, 0, Z\_LOG\_CURRENT\_DATA(), \_data, \_length, \_\_VA\_ARGS\_\_)

367

368#define Z\_LOG\_HEXDUMP\_INSTANCE(\_level, \_inst, \_data, \_length, ...) \

369 Z\_LOG\_HEXDUMP2(\_level, 1, Z\_LOG\_INST(\_inst), \_data, \_length, \_\_VA\_ARGS\_\_)

370

371/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*/

372/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* Filtering macros \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*/

373/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*/

374

[ 376](log__core_8h.md#a84474b9b8e31f5ee7040f7e22021c163)#define LOG\_LEVEL\_BITS 3U

377

[ 379](log__core_8h.md#a31c9e4a93ba2527b3bce4e5461dd65dd)#define LOG\_FILTER\_SLOT\_SIZE LOG\_LEVEL\_BITS

380

[ 382](log__core_8h.md#ad7a2f00a0b9d7961f6f246b828ec8c63)#define LOG\_FILTERS\_NUM\_OF\_SLOTS (32 / LOG\_FILTER\_SLOT\_SIZE)

383

[ 385](log__core_8h.md#a6258cbdcc73befb83fb5e5b5efd29d65)#define LOG\_FILTERS\_MAX\_BACKENDS \

386 (LOG\_FILTERS\_NUM\_OF\_SLOTS - (1 + IS\_ENABLED(CONFIG\_LOG\_FRONTEND)))

387

[ 389](log__core_8h.md#ad3865db594c20dff3d20e02b954d7a51)#define LOG\_FRONTEND\_SLOT\_ID (LOG\_FILTERS\_NUM\_OF\_SLOTS - 1)

390

[ 392](log__core_8h.md#a6d1b6a2b8ac28915ac085d430a952a15)#define LOG\_FILTER\_SLOT\_MASK (BIT(LOG\_FILTER\_SLOT\_SIZE) - 1U)

393

[ 398](log__core_8h.md#a5a21fea47b27e76f7382cf4cf687b4b3)#define LOG\_FILTER\_SLOT\_SHIFT(\_id) (LOG\_FILTER\_SLOT\_SIZE \* (\_id))

399

[ 400](log__core_8h.md#a91e38e2a6e541df4bb8dbb741e393e0e)#define LOG\_FILTER\_SLOT\_GET(\_filters, \_id) \

401 ((\*(\_filters) >> LOG\_FILTER\_SLOT\_SHIFT(\_id)) & LOG\_FILTER\_SLOT\_MASK)

402

[ 403](log__core_8h.md#aa95cdf72ca0084ef4deed1cf698192d6)#define LOG\_FILTER\_SLOT\_SET(\_filters, \_id, \_filter) \

404 do { \

405 \*(\_filters) &= ~(LOG\_FILTER\_SLOT\_MASK << \

406 LOG\_FILTER\_SLOT\_SHIFT(\_id)); \

407 \*(\_filters) |= ((\_filter) & LOG\_FILTER\_SLOT\_MASK) << \

408 LOG\_FILTER\_SLOT\_SHIFT(\_id); \

409 } while (false)

410

[ 411](log__core_8h.md#a3a875fb65e4f17a0b2d5cbc493084e34)#define LOG\_FILTER\_AGGR\_SLOT\_IDX 0

412

[ 413](log__core_8h.md#a4f4120cb018e563dea7005b10d5a6dc8)#define LOG\_FILTER\_AGGR\_SLOT\_GET(\_filters) \

414 LOG\_FILTER\_SLOT\_GET(\_filters, LOG\_FILTER\_AGGR\_SLOT\_IDX)

415

[ 416](log__core_8h.md#ab0f4745bf6824181306e2f71b3c9612e)#define LOG\_FILTER\_FIRST\_BACKEND\_SLOT\_IDX 1

417

418/\* Return aggregated (highest) level for all enabled backends, e.g. if there

419 \* are 3 active backends, one backend is set to get INF logs from a module and

420 \* two other backends are set for ERR, returned level is INF.

421 \*/

422#define Z\_LOG\_RUNTIME\_FILTER(\_filter) \

423 LOG\_FILTER\_SLOT\_GET(&(\_filter), LOG\_FILTER\_AGGR\_SLOT\_IDX)

424

[ 428](log__core_8h.md#a8be8b78ac80e9dd6bc8b9d3639942d33)#define LOG\_LEVEL\_INTERNAL\_RAW\_STRING LOG\_LEVEL\_NONE

429

[ 430](log__core_8h.md#a8bddbf82fcd014a2b65b53d80312237d)[TYPE\_SECTION\_START\_EXTERN](group__iterable__section__apis.md#ga40c6ba05d5bcb848a530bdc17bbff5be)(struct [log\_source\_const\_data](structlog__source__const__data.md), log\_const);

[ 431](log__core_8h.md#a9c76801a0e4d03e64c025f7cd5695d77)[TYPE\_SECTION\_END\_EXTERN](group__iterable__section__apis.md#gaf009fe4b90f7b338c3bf85bb4cd682e5)(struct [log\_source\_const\_data](structlog__source__const__data.md), log\_const);

432

443#define Z\_LOG\_PRINTK(\_is\_raw, ...) do { \

444 if (!IS\_ENABLED(CONFIG\_LOG)) { \

445 break; \

446 } \

447 if (IS\_ENABLED(CONFIG\_LOG\_MODE\_MINIMAL)) { \

448 z\_log\_minimal\_printk(\_\_VA\_ARGS\_\_); \

449 break; \

450 } \

451 int \_mode; \

452 if (0) {\

453 z\_log\_printf\_arg\_checker(\_\_VA\_ARGS\_\_); \

454 } \

455 Z\_LOG\_MSG\_CREATE(!IS\_ENABLED(CONFIG\_USERSPACE), \_mode, \

456 Z\_LOG\_LOCAL\_DOMAIN\_ID, (const void \*)(uintptr\_t)\_is\_raw, \

457 LOG\_LEVEL\_INTERNAL\_RAW\_STRING, NULL, 0, \_\_VA\_ARGS\_\_);\

458} while (0)

459

[ 467](log__core_8h.md#add353f5f883b7edee6428adb7fb7e4d5)static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [log\_const\_source\_id](log__core_8h.md#add353f5f883b7edee6428adb7fb7e4d5)(

468 const struct [log\_source\_const\_data](structlog__source__const__data.md) \*data)

469{

470 return ((const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*)data - ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*)[TYPE\_SECTION\_START](group__iterable__section__apis.md#gac97b7f4fd42a2d9e11b6a585bc716a05)(log\_const))/

471 sizeof(struct [log\_source\_const\_data](structlog__source__const__data.md));

472}

473

[ 474](log__core_8h.md#aab9e9896eac3c3008df9f191e2dc46eb)[TYPE\_SECTION\_START\_EXTERN](group__iterable__section__apis.md#ga40c6ba05d5bcb848a530bdc17bbff5be)(struct [log\_source\_dynamic\_data](structlog__source__dynamic__data.md), log\_dynamic);

[ 475](log__core_8h.md#aa42f7911fae598d4b602b336cdf269b1)[TYPE\_SECTION\_END\_EXTERN](group__iterable__section__apis.md#gaf009fe4b90f7b338c3bf85bb4cd682e5)(struct [log\_source\_dynamic\_data](structlog__source__dynamic__data.md), log\_dynamic);

476

[ 481](log__core_8h.md#a86c2e55bace38c6e71b4d1d0736b1160)#define LOG\_ITEM\_DYNAMIC\_DATA(\_name) UTIL\_CAT(log\_dynamic\_, \_name)

482

[ 483](log__core_8h.md#a322351c9b30bf3328821c6358ddc6a0b)#define LOG\_INSTANCE\_DYNAMIC\_DATA(\_module\_name, \_inst) \

484 LOG\_ITEM\_DYNAMIC\_DATA(Z\_LOG\_INSTANCE\_FULL\_NAME(\_module\_name, \_inst))

485

[ 493](log__core_8h.md#ab2e628ee35c240d79a5e622fa1209008)static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [log\_dynamic\_source\_id](log__core_8h.md#ab2e628ee35c240d79a5e622fa1209008)(struct [log\_source\_dynamic\_data](structlog__source__dynamic__data.md) \*data)

494{

495 return (([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*)data - ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*)[TYPE\_SECTION\_START](group__iterable__section__apis.md#gac97b7f4fd42a2d9e11b6a585bc716a05)(log\_dynamic))/

496 sizeof(struct [log\_source\_dynamic\_data](structlog__source__dynamic__data.md));

497}

498

[ 506](log__core_8h.md#a018055fae12bf8aa165e8a790196fafe)static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [log\_source\_id](log__core_8h.md#a018055fae12bf8aa165e8a790196fafe)(const void \*source)

507{

508 return [IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)(CONFIG\_LOG\_RUNTIME\_FILTERING) ?

509 [log\_dynamic\_source\_id](log__core_8h.md#ab2e628ee35c240d79a5e622fa1209008)((struct [log\_source\_dynamic\_data](structlog__source__dynamic__data.md) \*)source) :

510 [log\_const\_source\_id](log__core_8h.md#add353f5f883b7edee6428adb7fb7e4d5)((const struct [log\_source\_const\_data](structlog__source__const__data.md) \*)source);

511}

512

514static inline \_\_printf\_like(1, 2)

515void z\_log\_printf\_arg\_checker(const char \*fmt, ...)

516{

517 ARG\_UNUSED(fmt);

518}

519

[ 529](log__core_8h.md#ab81a1401935513819384b85948e3d09c)static inline void [log\_generic](log__core_8h.md#ab81a1401935513819384b85948e3d09c)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) level, const char \*fmt, va\_list ap)

530{

531 z\_log\_msg\_runtime\_vcreate(Z\_LOG\_LOCAL\_DOMAIN\_ID, NULL, level,

532 NULL, 0, 0, fmt, ap);

533}

534

535#ifdef \_\_cplusplus

536}

537#endif

538

539#endif /\* ZEPHYR\_INCLUDE\_LOGGING\_LOG\_CORE\_H\_ \*/

[TYPE\_SECTION\_START\_EXTERN](group__iterable__section__apis.md#ga40c6ba05d5bcb848a530bdc17bbff5be)

#define TYPE\_SECTION\_START\_EXTERN(type, secname)

iterable section extern for start symbol for a generic type

**Definition** iterable\_sections.h:78

[TYPE\_SECTION\_START](group__iterable__section__apis.md#gac97b7f4fd42a2d9e11b6a585bc716a05)

#define TYPE\_SECTION\_START(secname)

iterable section start symbol for a generic type

**Definition** iterable\_sections.h:55

[TYPE\_SECTION\_END\_EXTERN](group__iterable__section__apis.md#gaf009fe4b90f7b338c3bf85bb4cd682e5)

#define TYPE\_SECTION\_END\_EXTERN(type, secname)

iterable section extern for end symbol for a generic type

**Definition** iterable\_sections.h:92

[IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)

#define IS\_ENABLED(config\_macro)

Check for macro definition in compiler-visible expressions.

**Definition** util\_macro.h:140

[log\_source\_id](log__core_8h.md#a018055fae12bf8aa165e8a790196fafe)

static uint32\_t log\_source\_id(const void \*source)

Get index of the log source based on the address of the associated data.

**Definition** log\_core.h:506

[LOG\_LEVEL\_INF](log__core_8h.md#a281bc2ce5315e6fae369796c0fdf5c1d)

#define LOG\_LEVEL\_INF

**Definition** log\_core.h:22

[LOG\_LEVEL\_WRN](log__core_8h.md#a54f5db1327d9fdbaecbb03a6969de97b)

#define LOG\_LEVEL\_WRN

**Definition** log\_core.h:21

[log\_dynamic\_source\_id](log__core_8h.md#ab2e628ee35c240d79a5e622fa1209008)

static uint32\_t log\_dynamic\_source\_id(struct log\_source\_dynamic\_data \*data)

Get index of the log source based on the address of the dynamic data associated with the source.

**Definition** log\_core.h:493

[LOG\_LEVEL\_ERR](log__core_8h.md#ab3a03740685cbdaa375e2bde8247fdc6)

#define LOG\_LEVEL\_ERR

**Definition** log\_core.h:20

[log\_generic](log__core_8h.md#ab81a1401935513819384b85948e3d09c)

static void log\_generic(uint8\_t level, const char \*fmt, va\_list ap)

Write a generic log message.

**Definition** log\_core.h:529

[LOG\_LEVEL\_DBG](log__core_8h.md#ad1f7d41b1af28ba81ea63d24c9b690cc)

#define LOG\_LEVEL\_DBG

**Definition** log\_core.h:23

[log\_const\_source\_id](log__core_8h.md#add353f5f883b7edee6428adb7fb7e4d5)

static uint32\_t log\_const\_source\_id(const struct log\_source\_const\_data \*data)

Get index of the log source based on the address of the constant data associated with the source.

**Definition** log\_core.h:467

[log\_instance.h](log__instance_8h.md)

[log\_msg.h](log__msg_8h.md)

[stdbool.h](stdbool_8h.md)

[stdint.h](stdint_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[log\_source\_const\_data](structlog__source__const__data.md)

Constant data associated with the source of log messages.

**Definition** log\_instance.h:17

[log\_source\_dynamic\_data](structlog__source__dynamic__data.md)

Dynamic data associated with the source of log messages.

**Definition** log\_instance.h:30

[util.h](sys_2util_8h.md)

Misc utilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [logging](dir_7da6482b46a75d2870a82324d67b5f7e.md)
- [log\_core.h](log__core_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
