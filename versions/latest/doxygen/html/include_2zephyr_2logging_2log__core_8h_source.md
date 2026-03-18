---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/include_2zephyr_2logging_2log__core_8h_source.html
original_path: doxygen/html/include_2zephyr_2logging_2log__core_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

log\_core.h

[Go to the documentation of this file.](include_2zephyr_2logging_2log__core_8h.md)

1/\*

2 \* Copyright (c) 2018 Nordic Semiconductor ASA

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef ZEPHYR\_INCLUDE\_LOGGING\_LOG\_CORE\_H\_

7#define ZEPHYR\_INCLUDE\_LOGGING\_LOG\_CORE\_H\_

8

9#include <[zephyr/logging/log\_msg.h](include_2zephyr_2logging_2log__msg_8h.md)>

10#include <[zephyr/logging/log\_instance.h](log__instance_8h.md)>

11#include <[stdbool.h](stdbool_8h.md)>

12#include <[stdint.h](stdint_8h.md)>

13#include <stdarg.h>

14#include <[zephyr/sys/util.h](util_8h.md)>

15

16/\* This header file keeps all macros and functions needed for creating logging

17 \* messages (macros like @ref LOG\_ERR).

18 \*/

[ 19](include_2zephyr_2logging_2log__core_8h.md#a43dece650f96e7cf2a4e535c9bd4804a)#define LOG\_LEVEL\_NONE 0U

[ 20](include_2zephyr_2logging_2log__core_8h.md#ab3a03740685cbdaa375e2bde8247fdc6)#define LOG\_LEVEL\_ERR 1U

[ 21](include_2zephyr_2logging_2log__core_8h.md#a54f5db1327d9fdbaecbb03a6969de97b)#define LOG\_LEVEL\_WRN 2U

[ 22](include_2zephyr_2logging_2log__core_8h.md#a281bc2ce5315e6fae369796c0fdf5c1d)#define LOG\_LEVEL\_INF 3U

[ 23](include_2zephyr_2logging_2log__core_8h.md#ad1f7d41b1af28ba81ea63d24c9b690cc)#define LOG\_LEVEL\_DBG 4U

24

25#ifdef \_\_cplusplus

26extern "C" {

27#endif

28

29#ifndef CONFIG\_LOG

[ 30](include_2zephyr_2logging_2log__core_8h.md#ac618493585bc226f18f36b6a2ad7e8d5)#define CONFIG\_LOG\_DEFAULT\_LEVEL 0U

[ 31](include_2zephyr_2logging_2log__core_8h.md#a97df309d4ec6704223193647b6faf819)#define CONFIG\_LOG\_MAX\_LEVEL 0U

32#endif

33

34/\* Id of local domain. \*/

35#define Z\_LOG\_LOCAL\_DOMAIN\_ID 0

36

[ 37](include_2zephyr_2logging_2log__core_8h.md#add313a51d2d73b99ad0d00fc5184312f)#define LOG\_FUNCTION\_PREFIX\_MASK \

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

57#define \_LOG\_XXXX0U \_LOG\_YYYY,

58#define \_LOG\_XXXX1 \_LOG\_YYYY,

59#define \_LOG\_XXXX1U \_LOG\_YYYY,

60#define \_LOG\_XXXX2 \_LOG\_YYYY,

61#define \_LOG\_XXXX2U \_LOG\_YYYY,

62#define \_LOG\_XXXX3 \_LOG\_YYYY,

63#define \_LOG\_XXXX3U \_LOG\_YYYY,

64#define \_LOG\_XXXX4 \_LOG\_YYYY,

65#define \_LOG\_XXXX4U \_LOG\_YYYY,

66

81#define Z\_LOG\_EVAL(\_eval\_level, \_iftrue, \_iffalse) \

82 Z\_LOG\_EVAL1(\_eval\_level, \_iftrue, \_iffalse)

83

84#define Z\_LOG\_EVAL1(\_eval\_level, \_iftrue, \_iffalse) \

85 \_\_COND\_CODE(\_LOG\_ZZZZ##\_eval\_level, \_iftrue, \_iffalse)

86

87#define \_LOG\_ZZZZ1 \_LOG\_YYYY,

88#define \_LOG\_ZZZZ1U \_LOG\_YYYY,

89#define \_LOG\_ZZZZ2 \_LOG\_YYYY,

90#define \_LOG\_ZZZZ2U \_LOG\_YYYY,

91#define \_LOG\_ZZZZ3 \_LOG\_YYYY,

92#define \_LOG\_ZZZZ3U \_LOG\_YYYY,

93#define \_LOG\_ZZZZ4 \_LOG\_YYYY,

94#define \_LOG\_ZZZZ4U \_LOG\_YYYY,

95

[ 100](include_2zephyr_2logging_2log__core_8h.md#a85c70bfd98bbc66a35806010a206237e)#define LOG\_CURRENT\_MODULE\_ID() (\_\_log\_level != 0 ? \

101 log\_const\_source\_id(\_\_log\_current\_const\_data) : 0U)

102

103/\* Set of defines that are set to 1 if function name prefix is enabled for given level. \*/

104#define Z\_LOG\_FUNC\_PREFIX\_0U 0

105#define Z\_LOG\_FUNC\_PREFIX\_1U COND\_CODE\_1(CONFIG\_LOG\_FUNC\_NAME\_PREFIX\_ERR, (1), (0))

106#define Z\_LOG\_FUNC\_PREFIX\_2U COND\_CODE\_1(CONFIG\_LOG\_FUNC\_NAME\_PREFIX\_WRN, (1), (0))

107#define Z\_LOG\_FUNC\_PREFIX\_3U COND\_CODE\_1(CONFIG\_LOG\_FUNC\_NAME\_PREFIX\_INF, (1), (0))

108#define Z\_LOG\_FUNC\_PREFIX\_4U COND\_CODE\_1(CONFIG\_LOG\_FUNC\_NAME\_PREFIX\_DBG, (1), (0))

109

119#define Z\_LOG\_STR\_WITH\_PREFIX2(...) \

120 "%s: " GET\_ARG\_N(1, \_\_VA\_ARGS\_\_), (const char \*)\_\_func\_\_\

121 COND\_CODE\_0(NUM\_VA\_ARGS\_LESS\_1(\_\_VA\_ARGS\_\_),\

122 (),\

123 (, GET\_ARGS\_LESS\_N(1, \_\_VA\_ARGS\_\_))\

124 )

125

126/\* Macro handles case when no format string is provided: e.g. LOG\_DBG().

127 \* Handling of format string is deferred to the next level macro.

128 \*/

129#define Z\_LOG\_STR\_WITH\_PREFIX(...) \

130 COND\_CODE\_0(NUM\_VA\_ARGS\_LESS\_1(\_, ##\_\_VA\_ARGS\_\_), \

131 ("%s", (const char \*)\_\_func\_\_), \

132 (Z\_LOG\_STR\_WITH\_PREFIX2(\_\_VA\_ARGS\_\_)))

133

139#define Z\_LOG\_STR(\_level, ...) \

140 COND\_CODE\_1(UTIL\_CAT(Z\_LOG\_FUNC\_PREFIX\_##\_level), \

141 (Z\_LOG\_STR\_WITH\_PREFIX(\_\_VA\_ARGS\_\_)), (\_\_VA\_ARGS\_\_))

142

143#define Z\_LOG\_LEVEL\_CHECK(\_level, \_check\_level, \_default\_level) \

144 (\_level <= Z\_LOG\_RESOLVED\_LEVEL(\_check\_level, \_default\_level))

145

146#define Z\_LOG\_CONST\_LEVEL\_CHECK(\_level) \

147 (IS\_ENABLED(CONFIG\_LOG) && \

148 (Z\_LOG\_LEVEL\_CHECK(\_level, CONFIG\_LOG\_OVERRIDE\_LEVEL, LOG\_LEVEL\_NONE) \

149 || \

150 ((IS\_ENABLED(CONFIG\_LOG\_OVERRIDE\_LEVEL) == false) && \

151 (\_level <= \_\_log\_level) && \

152 (\_level <= CONFIG\_LOG\_MAX\_LEVEL) \

153 ) \

154 ))

155

156/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*/

157/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* Definitions used by minimal logging \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*/

158/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*/

159void z\_log\_minimal\_hexdump\_print(int level, const void \*data, size\_t size);

160void z\_log\_minimal\_vprintk(const char \*fmt, va\_list ap);

161void z\_log\_minimal\_printk(const char \*fmt, ...);

162

163#define Z\_LOG\_TO\_PRINTK(\_level, fmt, ...) do { \

164 z\_log\_minimal\_printk("%c: " fmt "\n", \

165 z\_log\_minimal\_level\_to\_char(\_level), \

166 ##\_\_VA\_ARGS\_\_); \

167} while (false)

168

169#define Z\_LOG\_TO\_VPRINTK(\_level, fmt, valist) do { \

170 z\_log\_minimal\_printk("%c: ", z\_log\_minimal\_level\_to\_char(\_level)); \

171 z\_log\_minimal\_vprintk(fmt, valist); \

172 z\_log\_minimal\_printk("\n"); \

173} while (false)

174

175static inline char z\_log\_minimal\_level\_to\_char(int level)

176{

177 switch (level) {

178 case [LOG\_LEVEL\_ERR](include_2zephyr_2logging_2log__core_8h.md#ab3a03740685cbdaa375e2bde8247fdc6):

179 return 'E';

180 case [LOG\_LEVEL\_WRN](include_2zephyr_2logging_2log__core_8h.md#a54f5db1327d9fdbaecbb03a6969de97b):

181 return 'W';

182 case [LOG\_LEVEL\_INF](include_2zephyr_2logging_2log__core_8h.md#a281bc2ce5315e6fae369796c0fdf5c1d):

183 return 'I';

184 case [LOG\_LEVEL\_DBG](include_2zephyr_2logging_2log__core_8h.md#ad1f7d41b1af28ba81ea63d24c9b690cc):

185 return 'D';

186 default:

187 return '?';

188 }

189}

190

191#define Z\_LOG\_INST(\_inst) COND\_CODE\_1(CONFIG\_LOG, (\_inst), NULL)

192

193/\* If strings are removed from the binary then there is a risk of creating invalid

194 \* cbprintf package if %p is used with character pointer which is interpreted as

195 \* string. A compile time check is performed (since format string is known at

196 \* compile time) and check fails logging message is not created but error is

197 \* emitted instead. String check may increase compilation time so it is not

198 \* always performed (could significantly increase CI time).

199 \*/

200#if CONFIG\_LOG\_FMT\_STRING\_VALIDATE

201#define LOG\_STRING\_WARNING(\_mode, \_src, ...) \

202 Z\_LOG\_MSG\_CREATE(UTIL\_NOT(IS\_ENABLED(CONFIG\_USERSPACE)), \_mode, \

203 Z\_LOG\_LOCAL\_DOMAIN\_ID, \_src, LOG\_LEVEL\_ERR, NULL, 0, \

204 "char pointer used for %%p, cast to void \*:\"%s\"", \

205 GET\_ARG\_N(1, \_\_VA\_ARGS\_\_))

206

207#define LOG\_POINTERS\_VALIDATE(string\_ok, ...) \

208 \_Pragma("GCC diagnostic push") \

209 \_Pragma("GCC diagnostic ignored \"-Wpointer-arith\"") \

210 string\_ok = Z\_CBPRINTF\_POINTERS\_VALIDATE(\_\_VA\_ARGS\_\_); \

211 \_Pragma("GCC diagnostic pop")

212#else

[ 213](include_2zephyr_2logging_2log__core_8h.md#a6d29de8e144ab8e57f42f096b0b47ca0)#define LOG\_POINTERS\_VALIDATE(string\_ok, ...) string\_ok = true

[ 214](include_2zephyr_2logging_2log__core_8h.md#ad9fb171d1afec420ff46f6e0e4b0481d)#define LOG\_STRING\_WARNING(\_mode, \_src, ...)

215#endif

216

217/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*/

218/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* Macros for standard logging \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*/

219/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*/

238#define Z\_LOG2(\_level, \_inst, \_source, \_dsource, ...) do { \

239 if (!Z\_LOG\_CONST\_LEVEL\_CHECK(\_level)) { \

240 break; \

241 } \

242 if (IS\_ENABLED(CONFIG\_LOG\_MODE\_MINIMAL)) { \

243 Z\_LOG\_TO\_PRINTK(\_level, \_\_VA\_ARGS\_\_); \

244 break; \

245 } \

246 /\* For instance logging check instance specific static level \*/ \

247 if (\_inst != 0 && !IS\_ENABLED(CONFIG\_LOG\_RUNTIME\_FILTERING)) { \

248 if (\_level > ((struct log\_source\_const\_data \*)\_source)->level) { \

249 break; \

250 } \

251 } \

252 \

253 bool is\_user\_context = k\_is\_user\_context(); \

254 if (!IS\_ENABLED(CONFIG\_LOG\_FRONTEND) && IS\_ENABLED(CONFIG\_LOG\_RUNTIME\_FILTERING) && \

255 !is\_user\_context && \_level > Z\_LOG\_RUNTIME\_FILTER((\_dsource)->filters)) { \

256 break; \

257 } \

258 int \_mode; \

259 void \*\_src = IS\_ENABLED(CONFIG\_LOG\_RUNTIME\_FILTERING) ? \

260 (void \*)\_dsource : (void \*)\_source; \

261 bool string\_ok; \

262 LOG\_POINTERS\_VALIDATE(string\_ok, \_\_VA\_ARGS\_\_); \

263 if (!string\_ok) { \

264 LOG\_STRING\_WARNING(\_mode, \_src, \_\_VA\_ARGS\_\_); \

265 break; \

266 } \

267 Z\_LOG\_MSG\_CREATE(UTIL\_NOT(IS\_ENABLED(CONFIG\_USERSPACE)), \_mode, \

268 Z\_LOG\_LOCAL\_DOMAIN\_ID, \_src, \_level, NULL,\

269 0, \_\_VA\_ARGS\_\_); \

270 (void)\_mode; \

271 if (false) { \

272 /\* Arguments checker present but never evaluated.\*/ \

273 /\* Placed here to ensure that \_\_VA\_ARGS\_\_ are\*/ \

274 /\* evaluated once when log is enabled.\*/ \

275 z\_log\_printf\_arg\_checker(\_\_VA\_ARGS\_\_); \

276 } \

277} while (false)

278

279#define Z\_LOG(\_level, ...) \

280 Z\_LOG2(\_level, 0, \_\_log\_current\_const\_data, \_\_log\_current\_dynamic\_data, \_\_VA\_ARGS\_\_)

281

282#define Z\_LOG\_INSTANCE(\_level, \_inst, ...) do { \

283 (void)\_inst; \

284 Z\_LOG2(\_level, 1, \

285 COND\_CODE\_1(CONFIG\_LOG\_RUNTIME\_FILTERING, (NULL), (Z\_LOG\_INST(\_inst))), \

286 (struct log\_source\_dynamic\_data \*)COND\_CODE\_1( \

287 CONFIG\_LOG\_RUNTIME\_FILTERING, \

288 (Z\_LOG\_INST(\_inst)), (NULL)), \

289 \_\_VA\_ARGS\_\_); \

290} while (0)

291

292/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*/

293/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* Macros for hexdump logging \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*/

294/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*/

317#define Z\_LOG\_HEXDUMP2(\_level, \_inst, \_source, \_dsource, \_data, \_len, ...) do { \

318 const char \*\_str = GET\_ARG\_N(1, \_\_VA\_ARGS\_\_); \

319 if (!Z\_LOG\_CONST\_LEVEL\_CHECK(\_level)) { \

320 break; \

321 } \

322 /\* For instance logging check instance specific static level \*/ \

323 if (\_inst && !IS\_ENABLED(CONFIG\_LOG\_RUNTIME\_FILTERING)) { \

324 if (\_level > ((struct log\_source\_const\_data \*)\_source)->level) { \

325 break; \

326 } \

327 } \

328 bool is\_user\_context = k\_is\_user\_context(); \

329 uint32\_t filters = IS\_ENABLED(CONFIG\_LOG\_RUNTIME\_FILTERING) ? \

330 (\_dsource)->filters : 0;\

331 \

332 if (IS\_ENABLED(CONFIG\_LOG\_MODE\_MINIMAL)) { \

333 Z\_LOG\_TO\_PRINTK(\_level, "%s", \_str); \

334 z\_log\_minimal\_hexdump\_print(\_level, \

335 (const char \*)\_data, \_len);\

336 break; \

337 } \

338 if (!IS\_ENABLED(CONFIG\_LOG\_FRONTEND) && IS\_ENABLED(CONFIG\_LOG\_RUNTIME\_FILTERING) && \

339 !is\_user\_context && \_level > Z\_LOG\_RUNTIME\_FILTER(filters)) { \

340 break; \

341 } \

342 int mode; \

343 void \*\_src = IS\_ENABLED(CONFIG\_LOG\_RUNTIME\_FILTERING) ? \

344 (void \*)\_dsource : (void \*)\_source; \

345 Z\_LOG\_MSG\_CREATE(UTIL\_NOT(IS\_ENABLED(CONFIG\_USERSPACE)), mode, \

346 Z\_LOG\_LOCAL\_DOMAIN\_ID, \_src, \_level, \

347 \_data, \_len, \

348 COND\_CODE\_0(NUM\_VA\_ARGS\_LESS\_1(\_, ##\_\_VA\_ARGS\_\_), \

349 (), \

350 (COND\_CODE\_0(NUM\_VA\_ARGS\_LESS\_1(\_\_VA\_ARGS\_\_), \

351 ("%s", \_\_VA\_ARGS\_\_), (\_\_VA\_ARGS\_\_)))));\

352} while (false)

353

354#define Z\_LOG\_HEXDUMP(\_level, \_data, \_length, ...) \

355 Z\_LOG\_HEXDUMP2(\_level, 0, \

356 \_\_log\_current\_const\_data, \

357 \_\_log\_current\_dynamic\_data, \

358 \_data, \_length, \_\_VA\_ARGS\_\_)

359

360#define Z\_LOG\_HEXDUMP\_INSTANCE(\_level, \_inst, \_data, \_length, \_str) \

361 Z\_LOG\_HEXDUMP2(\_level, 1, \

362 COND\_CODE\_1(CONFIG\_LOG\_RUNTIME\_FILTERING, (NULL), (Z\_LOG\_INST(\_inst))), \

363 (struct log\_source\_dynamic\_data \*)COND\_CODE\_1( \

364 CONFIG\_LOG\_RUNTIME\_FILTERING, \

365 (Z\_LOG\_INST(\_inst)), (NULL)), \

366 \_data, \_length, \_str)

367

368/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*/

369/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* Filtering macros \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*/

370/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*/

371

[ 373](include_2zephyr_2logging_2log__core_8h.md#a84474b9b8e31f5ee7040f7e22021c163)#define LOG\_LEVEL\_BITS 3U

374

[ 376](include_2zephyr_2logging_2log__core_8h.md#a31c9e4a93ba2527b3bce4e5461dd65dd)#define LOG\_FILTER\_SLOT\_SIZE LOG\_LEVEL\_BITS

377

[ 379](include_2zephyr_2logging_2log__core_8h.md#ad7a2f00a0b9d7961f6f246b828ec8c63)#define LOG\_FILTERS\_NUM\_OF\_SLOTS (32 / LOG\_FILTER\_SLOT\_SIZE)

380

[ 382](include_2zephyr_2logging_2log__core_8h.md#a6258cbdcc73befb83fb5e5b5efd29d65)#define LOG\_FILTERS\_MAX\_BACKENDS \

383 (LOG\_FILTERS\_NUM\_OF\_SLOTS - (1 + IS\_ENABLED(CONFIG\_LOG\_FRONTEND)))

384

[ 386](include_2zephyr_2logging_2log__core_8h.md#ad3865db594c20dff3d20e02b954d7a51)#define LOG\_FRONTEND\_SLOT\_ID (LOG\_FILTERS\_NUM\_OF\_SLOTS - 1)

387

[ 389](include_2zephyr_2logging_2log__core_8h.md#a6d1b6a2b8ac28915ac085d430a952a15)#define LOG\_FILTER\_SLOT\_MASK (BIT(LOG\_FILTER\_SLOT\_SIZE) - 1U)

390

[ 395](include_2zephyr_2logging_2log__core_8h.md#a5a21fea47b27e76f7382cf4cf687b4b3)#define LOG\_FILTER\_SLOT\_SHIFT(\_id) (LOG\_FILTER\_SLOT\_SIZE \* (\_id))

396

[ 397](include_2zephyr_2logging_2log__core_8h.md#a91e38e2a6e541df4bb8dbb741e393e0e)#define LOG\_FILTER\_SLOT\_GET(\_filters, \_id) \

398 ((\*(\_filters) >> LOG\_FILTER\_SLOT\_SHIFT(\_id)) & LOG\_FILTER\_SLOT\_MASK)

399

[ 400](include_2zephyr_2logging_2log__core_8h.md#aa95cdf72ca0084ef4deed1cf698192d6)#define LOG\_FILTER\_SLOT\_SET(\_filters, \_id, \_filter) \

401 do { \

402 \*(\_filters) &= ~(LOG\_FILTER\_SLOT\_MASK << \

403 LOG\_FILTER\_SLOT\_SHIFT(\_id)); \

404 \*(\_filters) |= ((\_filter) & LOG\_FILTER\_SLOT\_MASK) << \

405 LOG\_FILTER\_SLOT\_SHIFT(\_id); \

406 } while (false)

407

[ 408](include_2zephyr_2logging_2log__core_8h.md#a3a875fb65e4f17a0b2d5cbc493084e34)#define LOG\_FILTER\_AGGR\_SLOT\_IDX 0

409

[ 410](include_2zephyr_2logging_2log__core_8h.md#a4f4120cb018e563dea7005b10d5a6dc8)#define LOG\_FILTER\_AGGR\_SLOT\_GET(\_filters) \

411 LOG\_FILTER\_SLOT\_GET(\_filters, LOG\_FILTER\_AGGR\_SLOT\_IDX)

412

[ 413](include_2zephyr_2logging_2log__core_8h.md#ab0f4745bf6824181306e2f71b3c9612e)#define LOG\_FILTER\_FIRST\_BACKEND\_SLOT\_IDX 1

414

415/\* Return aggregated (highest) level for all enabled backends, e.g. if there

416 \* are 3 active backends, one backend is set to get INF logs from a module and

417 \* two other backends are set for ERR, returned level is INF.

418 \*/

419#define Z\_LOG\_RUNTIME\_FILTER(\_filter) \

420 LOG\_FILTER\_SLOT\_GET(&\_filter, LOG\_FILTER\_AGGR\_SLOT\_IDX)

421

[ 425](include_2zephyr_2logging_2log__core_8h.md#a8be8b78ac80e9dd6bc8b9d3639942d33)#define LOG\_LEVEL\_INTERNAL\_RAW\_STRING LOG\_LEVEL\_NONE

426

[ 427](include_2zephyr_2logging_2log__core_8h.md#a8bddbf82fcd014a2b65b53d80312237d)[TYPE\_SECTION\_START\_EXTERN](group__iterable__section__apis.md#ga40c6ba05d5bcb848a530bdc17bbff5be)(struct [log\_source\_const\_data](structlog__source__const__data.md), log\_const);

[ 428](include_2zephyr_2logging_2log__core_8h.md#a9c76801a0e4d03e64c025f7cd5695d77)[TYPE\_SECTION\_END\_EXTERN](group__iterable__section__apis.md#gaf009fe4b90f7b338c3bf85bb4cd682e5)(struct [log\_source\_const\_data](structlog__source__const__data.md), log\_const);

429

440#define Z\_LOG\_PRINTK(\_is\_raw, ...) do { \

441 if (!IS\_ENABLED(CONFIG\_LOG)) { \

442 break; \

443 } \

444 if (IS\_ENABLED(CONFIG\_LOG\_MODE\_MINIMAL)) { \

445 z\_log\_minimal\_printk(\_\_VA\_ARGS\_\_); \

446 break; \

447 } \

448 int \_mode; \

449 if (0) {\

450 z\_log\_printf\_arg\_checker(\_\_VA\_ARGS\_\_); \

451 } \

452 Z\_LOG\_MSG\_CREATE(!IS\_ENABLED(CONFIG\_USERSPACE), \_mode, \

453 Z\_LOG\_LOCAL\_DOMAIN\_ID, (const void \*)(uintptr\_t)\_is\_raw, \

454 LOG\_LEVEL\_INTERNAL\_RAW\_STRING, NULL, 0, \_\_VA\_ARGS\_\_);\

455} while (0)

456

[ 464](include_2zephyr_2logging_2log__core_8h.md#add353f5f883b7edee6428adb7fb7e4d5)static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [log\_const\_source\_id](include_2zephyr_2logging_2log__core_8h.md#add353f5f883b7edee6428adb7fb7e4d5)(

465 const struct [log\_source\_const\_data](structlog__source__const__data.md) \*data)

466{

467 return ((const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*)data - ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*)[TYPE\_SECTION\_START](group__iterable__section__apis.md#gac97b7f4fd42a2d9e11b6a585bc716a05)(log\_const))/

468 sizeof(struct [log\_source\_const\_data](structlog__source__const__data.md));

469}

470

[ 471](include_2zephyr_2logging_2log__core_8h.md#aab9e9896eac3c3008df9f191e2dc46eb)[TYPE\_SECTION\_START\_EXTERN](group__iterable__section__apis.md#ga40c6ba05d5bcb848a530bdc17bbff5be)(struct [log\_source\_dynamic\_data](structlog__source__dynamic__data.md), log\_dynamic);

[ 472](include_2zephyr_2logging_2log__core_8h.md#aa42f7911fae598d4b602b336cdf269b1)[TYPE\_SECTION\_END\_EXTERN](group__iterable__section__apis.md#gaf009fe4b90f7b338c3bf85bb4cd682e5)(struct [log\_source\_dynamic\_data](structlog__source__dynamic__data.md), log\_dynamic);

473

[ 478](include_2zephyr_2logging_2log__core_8h.md#a86c2e55bace38c6e71b4d1d0736b1160)#define LOG\_ITEM\_DYNAMIC\_DATA(\_name) UTIL\_CAT(log\_dynamic\_, \_name)

479

[ 480](include_2zephyr_2logging_2log__core_8h.md#a322351c9b30bf3328821c6358ddc6a0b)#define LOG\_INSTANCE\_DYNAMIC\_DATA(\_module\_name, \_inst) \

481 LOG\_ITEM\_DYNAMIC\_DATA(Z\_LOG\_INSTANCE\_FULL\_NAME(\_module\_name, \_inst))

482

[ 490](include_2zephyr_2logging_2log__core_8h.md#ab2e628ee35c240d79a5e622fa1209008)static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [log\_dynamic\_source\_id](include_2zephyr_2logging_2log__core_8h.md#ab2e628ee35c240d79a5e622fa1209008)(struct [log\_source\_dynamic\_data](structlog__source__dynamic__data.md) \*data)

491{

492 return (([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*)data - ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*)[TYPE\_SECTION\_START](group__iterable__section__apis.md#gac97b7f4fd42a2d9e11b6a585bc716a05)(log\_dynamic))/

493 sizeof(struct [log\_source\_dynamic\_data](structlog__source__dynamic__data.md));

494}

495

497static inline \_\_printf\_like(1, 2)

498void z\_log\_printf\_arg\_checker(const char \*fmt, ...)

499{

500 ARG\_UNUSED(fmt);

501}

502

[ 512](include_2zephyr_2logging_2log__core_8h.md#ab81a1401935513819384b85948e3d09c)static inline void [log\_generic](include_2zephyr_2logging_2log__core_8h.md#ab81a1401935513819384b85948e3d09c)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) level, const char \*fmt, va\_list ap)

513{

514 z\_log\_msg\_runtime\_vcreate(Z\_LOG\_LOCAL\_DOMAIN\_ID, NULL, level,

515 NULL, 0, 0, fmt, ap);

516}

517

518#ifdef \_\_cplusplus

519}

520#endif

521

522#endif /\* ZEPHYR\_INCLUDE\_LOGGING\_LOG\_CORE\_H\_ \*/

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

[LOG\_LEVEL\_INF](include_2zephyr_2logging_2log__core_8h.md#a281bc2ce5315e6fae369796c0fdf5c1d)

#define LOG\_LEVEL\_INF

**Definition** log\_core.h:22

[LOG\_LEVEL\_WRN](include_2zephyr_2logging_2log__core_8h.md#a54f5db1327d9fdbaecbb03a6969de97b)

#define LOG\_LEVEL\_WRN

**Definition** log\_core.h:21

[log\_dynamic\_source\_id](include_2zephyr_2logging_2log__core_8h.md#ab2e628ee35c240d79a5e622fa1209008)

static uint32\_t log\_dynamic\_source\_id(struct log\_source\_dynamic\_data \*data)

Get index of the log source based on the address of the dynamic data associated with the source.

**Definition** log\_core.h:490

[LOG\_LEVEL\_ERR](include_2zephyr_2logging_2log__core_8h.md#ab3a03740685cbdaa375e2bde8247fdc6)

#define LOG\_LEVEL\_ERR

**Definition** log\_core.h:20

[log\_generic](include_2zephyr_2logging_2log__core_8h.md#ab81a1401935513819384b85948e3d09c)

static void log\_generic(uint8\_t level, const char \*fmt, va\_list ap)

Write a generic log message.

**Definition** log\_core.h:512

[LOG\_LEVEL\_DBG](include_2zephyr_2logging_2log__core_8h.md#ad1f7d41b1af28ba81ea63d24c9b690cc)

#define LOG\_LEVEL\_DBG

**Definition** log\_core.h:23

[log\_const\_source\_id](include_2zephyr_2logging_2log__core_8h.md#add353f5f883b7edee6428adb7fb7e4d5)

static uint32\_t log\_const\_source\_id(const struct log\_source\_const\_data \*data)

Get index of the log source based on the address of the constant data associated with the source.

**Definition** log\_core.h:464

[log\_msg.h](include_2zephyr_2logging_2log__msg_8h.md)

[log\_instance.h](log__instance_8h.md)

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

[util.h](util_8h.md)

Misc utilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [logging](dir_7da6482b46a75d2870a82324d67b5f7e.md)
- [log\_core.h](include_2zephyr_2logging_2log__core_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
