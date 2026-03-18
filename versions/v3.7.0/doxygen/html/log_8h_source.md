---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/log_8h_source.html
original_path: doxygen/html/log_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

log.h

[Go to the documentation of this file.](log_8h.md)

1/\*

2 \* Copyright (c) 2018 Nordic Semiconductor ASA

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_LOGGING\_LOG\_H\_

8#define ZEPHYR\_INCLUDE\_LOGGING\_LOG\_H\_

9

10#include <[zephyr/logging/log\_instance.h](log__instance_8h.md)>

11#include <[zephyr/logging/log\_core.h](log__core_8h.md)>

12#include <[zephyr/sys/iterable\_sections.h](sys_2iterable__sections_8h.md)>

13

14#ifdef \_\_cplusplus

15extern "C" {

16#endif

17

27

34

[ 44](group__log__api.md#gad6db28c61c838c1f7316417e1e4847f2)#define LOG\_ERR(...) Z\_LOG(LOG\_LEVEL\_ERR, \_\_VA\_ARGS\_\_)

45

[ 55](group__log__api.md#ga644db4299681d9ebf06f8745ad984c65)#define LOG\_WRN(...) Z\_LOG(LOG\_LEVEL\_WRN, \_\_VA\_ARGS\_\_)

56

[ 65](group__log__api.md#ga9c338f3170acf38a8532d1181d26704e)#define LOG\_INF(...) Z\_LOG(LOG\_LEVEL\_INF, \_\_VA\_ARGS\_\_)

66

[ 75](group__log__api.md#gafb97e6291db24665313453d192941330)#define LOG\_DBG(...) Z\_LOG(LOG\_LEVEL\_DBG, \_\_VA\_ARGS\_\_)

76

[ 86](group__log__api.md#gaa9b22a7d4659030d9a3273f1f1e6786c)#define LOG\_WRN\_ONCE(...) \

87 do { \

88 static uint8\_t \_\_warned; \

89 if (unlikely(\_\_warned == 0)) { \

90 Z\_LOG(LOG\_LEVEL\_WRN, \_\_VA\_ARGS\_\_); \

91 \_\_warned = 1; \

92 } \

93 } while (0)

94

[ 104](group__log__api.md#ga4ab5cae247b853bf9f4f0bf761c1c71e)#define LOG\_PRINTK(...) Z\_LOG\_PRINTK(0, \_\_VA\_ARGS\_\_)

105

[ 114](group__log__api.md#ga7dedf58739648ed9b9aef1abe982f7d6)#define LOG\_RAW(...) Z\_LOG\_PRINTK(1, \_\_VA\_ARGS\_\_)

115

[ 128](group__log__api.md#ga830f32743847c52e01a510ab0716fe90)#define LOG\_INST\_ERR(\_log\_inst, ...) \

129 Z\_LOG\_INSTANCE(LOG\_LEVEL\_ERR, \_log\_inst, \_\_VA\_ARGS\_\_)

130

[ 144](group__log__api.md#ga76057f789dfc164adbb1dbc9f3aff417)#define LOG\_INST\_WRN(\_log\_inst, ...) \

145 Z\_LOG\_INSTANCE(LOG\_LEVEL\_WRN, \_log\_inst, \_\_VA\_ARGS\_\_)

146

[ 159](group__log__api.md#ga222c5b535fb3ecb36dea97885c794188)#define LOG\_INST\_INF(\_log\_inst, ...) \

160 Z\_LOG\_INSTANCE(LOG\_LEVEL\_INF, \_log\_inst, \_\_VA\_ARGS\_\_)

161

[ 174](group__log__api.md#gae10014012020ea5a6b9a86a5224f19b0)#define LOG\_INST\_DBG(\_log\_inst, ...) \

175 Z\_LOG\_INSTANCE(LOG\_LEVEL\_DBG, \_log\_inst, \_\_VA\_ARGS\_\_)

176

[ 187](group__log__api.md#gabdae4f5b8b16804b53f83a85c3023134)#define LOG\_HEXDUMP\_ERR(\_data, \_length, \_str) \

188 Z\_LOG\_HEXDUMP(LOG\_LEVEL\_ERR, \_data, \_length, (\_str))

189

[ 200](group__log__api.md#gaf73802661fea926bb2b7e628727cdceb)#define LOG\_HEXDUMP\_WRN(\_data, \_length, \_str) \

201 Z\_LOG\_HEXDUMP(LOG\_LEVEL\_WRN, \_data, \_length, (\_str))

202

[ 212](group__log__api.md#ga8e060bbe660c246a38adccd873e58c6c)#define LOG\_HEXDUMP\_INF(\_data, \_length, \_str) \

213 Z\_LOG\_HEXDUMP(LOG\_LEVEL\_INF, \_data, \_length, (\_str))

214

[ 224](group__log__api.md#ga01dda8273f7d453a855542a52524dca8)#define LOG\_HEXDUMP\_DBG(\_data, \_length, \_str) \

225 Z\_LOG\_HEXDUMP(LOG\_LEVEL\_DBG, \_data, \_length, (\_str))

226

[ 241](group__log__api.md#gaf2f504a779917dc0f40767cba9f940b9)#define LOG\_INST\_HEXDUMP\_ERR(\_log\_inst, \_data, \_length, \_str) \

242 Z\_LOG\_HEXDUMP\_INSTANCE(LOG\_LEVEL\_ERR, \_log\_inst, \_data, \_length, \_str)

243

[ 256](group__log__api.md#gab6542651f88fbb0991fb2339102b52a5)#define LOG\_INST\_HEXDUMP\_WRN(\_log\_inst, \_data, \_length, \_str) \

257 Z\_LOG\_HEXDUMP\_INSTANCE(LOG\_LEVEL\_WRN, \_log\_inst, \_data, \_length, \_str)

258

[ 270](group__log__api.md#ga8e38c461c6058ee604b4dddad662d4ca)#define LOG\_INST\_HEXDUMP\_INF(\_log\_inst, \_data, \_length, \_str) \

271 Z\_LOG\_HEXDUMP\_INSTANCE(LOG\_LEVEL\_INF, \_log\_inst, \_data, \_length, \_str)

272

[ 284](group__log__api.md#ga4b73e6d51cff26ea5595df8680c00563)#define LOG\_INST\_HEXDUMP\_DBG(\_log\_inst, \_data, \_length, \_str) \

285 Z\_LOG\_HEXDUMP\_INSTANCE(LOG\_LEVEL\_DBG, \_log\_inst, \_data, \_length, \_str)

286

299void z\_log\_vprintk(const char \*fmt, va\_list ap);

300

301#ifdef \_\_cplusplus

302}

303#define LOG\_IN\_CPLUSPLUS 1

304#endif

305/\* Macro expects that optionally on second argument local log level is provided.

306 \* If provided it is returned, otherwise default log level is returned or

307 \* LOG\_LEVEL, if it was locally defined.

308 \*/

309#if !defined(CONFIG\_LOG)

310#define \_LOG\_LEVEL\_RESOLVE(...) LOG\_LEVEL\_NONE

311#else

312#define \_LOG\_LEVEL\_RESOLVE(...) \

313 Z\_LOG\_EVAL(COND\_CODE\_0(LOG\_LEVEL, (1), (LOG\_LEVEL)), \

314 (GET\_ARG\_N(2, \_\_VA\_ARGS\_\_, LOG\_LEVEL)), \

315 (GET\_ARG\_N(2, \_\_VA\_ARGS\_\_, CONFIG\_LOG\_DEFAULT\_LEVEL)))

316#endif

317

318/\* Return first argument \*/

319#define \_LOG\_ARG1(arg1, ...) arg1

320

321#define \_LOG\_MODULE\_CONST\_DATA\_CREATE(\_name, \_level) \

322 IF\_ENABLED(CONFIG\_LOG\_FMT\_SECTION, ( \

323 static const char UTIL\_CAT(\_name, \_str)[] \

324 \_\_in\_section(\_log\_strings, static, \_CONCAT(\_name, \_)) \_\_used \_\_noasan = \

325 STRINGIFY(\_name);)) \

326 IF\_ENABLED(LOG\_IN\_CPLUSPLUS, (extern)) \

327 const STRUCT\_SECTION\_ITERABLE\_ALTERNATE(log\_const, \

328 log\_source\_const\_data, \

329 Z\_LOG\_ITEM\_CONST\_DATA(\_name)) = \

330 { \

331 .name = IS\_ENABLED(CONFIG\_LOG\_FMT\_SECTION\_STRIP) ? NULL : \

332 COND\_CODE\_1(CONFIG\_LOG\_FMT\_SECTION, \

333 (UTIL\_CAT(\_name, \_str)), (STRINGIFY(\_name))), \

334 .level = (\_level) \

335 }

336

337#define \_LOG\_MODULE\_DYNAMIC\_DATA\_CREATE(\_name) \

338 STRUCT\_SECTION\_ITERABLE\_ALTERNATE(log\_dynamic, log\_source\_dynamic\_data, \

339 LOG\_ITEM\_DYNAMIC\_DATA(\_name))

340

341#define \_LOG\_MODULE\_DYNAMIC\_DATA\_COND\_CREATE(\_name) \

342 IF\_ENABLED(CONFIG\_LOG\_RUNTIME\_FILTERING, \

343 (\_LOG\_MODULE\_DYNAMIC\_DATA\_CREATE(\_name);))

344

345#define \_LOG\_MODULE\_DATA\_CREATE(\_name, \_level) \

346 \_LOG\_MODULE\_CONST\_DATA\_CREATE(\_name, \_level); \

347 \_LOG\_MODULE\_DYNAMIC\_DATA\_COND\_CREATE(\_name)

348

349/\* Determine if data for the module shall be created. It is created if logging

350 \* is enabled, override level is set or module specific level is set (not off).

351 \*/

352#define Z\_DO\_LOG\_MODULE\_REGISTER(...) \

353 COND\_CODE\_1(CONFIG\_LOG, \

354 (Z\_LOG\_EVAL(CONFIG\_LOG\_OVERRIDE\_LEVEL, \

355 (1), \

356 (Z\_LOG\_EVAL(\_LOG\_LEVEL\_RESOLVE(\_\_VA\_ARGS\_\_), (1), (0))) \

357 )), (0))

358

[ 390](group__log__api.md#ga2404243df68fb6e51129d1c7ecc5ca45)#define LOG\_MODULE\_REGISTER(...) \

391 COND\_CODE\_1( \

392 Z\_DO\_LOG\_MODULE\_REGISTER(\_\_VA\_ARGS\_\_), \

393 (\_LOG\_MODULE\_DATA\_CREATE(GET\_ARG\_N(1, \_\_VA\_ARGS\_\_), \

394 \_LOG\_LEVEL\_RESOLVE(\_\_VA\_ARGS\_\_))),\

395 () \

396 ) \

397 LOG\_MODULE\_DECLARE(\_\_VA\_ARGS\_\_)

398

[ 425](group__log__api.md#ga8193b0e10e5ee64b86848bb52be31869)#define LOG\_MODULE\_DECLARE(...) \

426 extern const struct log\_source\_const\_data \

427 Z\_LOG\_ITEM\_CONST\_DATA(GET\_ARG\_N(1, \_\_VA\_ARGS\_\_)); \

428 extern struct log\_source\_dynamic\_data \

429 LOG\_ITEM\_DYNAMIC\_DATA(GET\_ARG\_N(1, \_\_VA\_ARGS\_\_)); \

430 \

431 static const struct log\_source\_const\_data \* \

432 \_\_log\_current\_const\_data \_\_unused = \

433 Z\_DO\_LOG\_MODULE\_REGISTER(\_\_VA\_ARGS\_\_) ? \

434 &Z\_LOG\_ITEM\_CONST\_DATA(GET\_ARG\_N(1, \_\_VA\_ARGS\_\_)) : \

435 NULL; \

436 \

437 static struct log\_source\_dynamic\_data \* \

438 \_\_log\_current\_dynamic\_data \_\_unused = \

439 (Z\_DO\_LOG\_MODULE\_REGISTER(\_\_VA\_ARGS\_\_) && \

440 IS\_ENABLED(CONFIG\_LOG\_RUNTIME\_FILTERING)) ? \

441 &LOG\_ITEM\_DYNAMIC\_DATA(GET\_ARG\_N(1, \_\_VA\_ARGS\_\_)) : \

442 NULL; \

443 \

444 static const uint32\_t \_\_log\_level \_\_unused = \

445 \_LOG\_LEVEL\_RESOLVE(\_\_VA\_ARGS\_\_)

446

[ 454](group__log__api.md#gac396852328a77360a0c27dbf7b52356e)#define LOG\_LEVEL\_SET(level) static const uint32\_t \_\_log\_level \_\_unused = \

455 Z\_LOG\_RESOLVED\_LEVEL(level, 0)

456

457#ifdef CONFIG\_LOG\_CUSTOM\_HEADER

458/\* This include must always be at the end of log.h \*/

459#include <zephyr\_custom\_log.h>

460#endif

461

462/\*

463 \* Eclipse CDT or JetBrains Clion parser is sometimes confused by logging API

464 \* code and freezes the whole IDE. Following lines hides LOG\_x macros from them.

465 \*/

466#if defined(\_\_CDT\_PARSER\_\_) || defined(\_\_JETBRAINS\_IDE\_\_)

467#undef LOG\_ERR

468#undef LOG\_WRN

469#undef LOG\_INF

470#undef LOG\_DBG

471

472#undef LOG\_HEXDUMP\_ERR

473#undef LOG\_HEXDUMP\_WRN

474#undef LOG\_HEXDUMP\_INF

475#undef LOG\_HEXDUMP\_DBG

476

477#define LOG\_ERR(...) (void) 0

478#define LOG\_WRN(...) (void) 0

479#define LOG\_DBG(...) (void) 0

480#define LOG\_INF(...) (void) 0

481

482#define LOG\_HEXDUMP\_ERR(...) (void) 0

483#define LOG\_HEXDUMP\_WRN(...) (void) 0

484#define LOG\_HEXDUMP\_DBG(...) (void) 0

485#define LOG\_HEXDUMP\_INF(...) (void) 0

486#endif

487

491

492#endif /\* ZEPHYR\_INCLUDE\_LOGGING\_LOG\_H\_ \*/

[log\_core.h](log__core_8h.md)

[log\_instance.h](log__instance_8h.md)

[iterable\_sections.h](sys_2iterable__sections_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [logging](dir_7da6482b46a75d2870a82324d67b5f7e.md)
- [log.h](log_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
