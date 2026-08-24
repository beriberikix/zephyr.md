---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/log_8h_source.html
original_path: doxygen/html/log_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
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

14#if CONFIG\_USERSPACE && CONFIG\_LOG\_ALWAYS\_RUNTIME

15#include <[zephyr/app\_memory/app\_memdomain.h](app__memdomain_8h.md)>

16#endif

17

18#ifdef \_\_cplusplus

19extern "C" {

20#endif

21

31

38

[ 48](group__log__api.md#gad6db28c61c838c1f7316417e1e4847f2)#define LOG\_ERR(...) Z\_LOG(LOG\_LEVEL\_ERR, \_\_VA\_ARGS\_\_)

49

[ 59](group__log__api.md#ga644db4299681d9ebf06f8745ad984c65)#define LOG\_WRN(...) Z\_LOG(LOG\_LEVEL\_WRN, \_\_VA\_ARGS\_\_)

60

[ 69](group__log__api.md#ga9c338f3170acf38a8532d1181d26704e)#define LOG\_INF(...) Z\_LOG(LOG\_LEVEL\_INF, \_\_VA\_ARGS\_\_)

70

[ 79](group__log__api.md#gafb97e6291db24665313453d192941330)#define LOG\_DBG(...) Z\_LOG(LOG\_LEVEL\_DBG, \_\_VA\_ARGS\_\_)

80

[ 90](group__log__api.md#gaa9b22a7d4659030d9a3273f1f1e6786c)#define LOG\_WRN\_ONCE(...) \

91 do { \

92 static uint8\_t \_\_warned; \

93 if (unlikely(\_\_warned == 0)) { \

94 Z\_LOG(LOG\_LEVEL\_WRN, \_\_VA\_ARGS\_\_); \

95 \_\_warned = 1; \

96 } \

97 } while (0)

98

[ 108](group__log__api.md#ga4ab5cae247b853bf9f4f0bf761c1c71e)#define LOG\_PRINTK(...) Z\_LOG\_PRINTK(0, \_\_VA\_ARGS\_\_)

109

[ 118](group__log__api.md#ga7dedf58739648ed9b9aef1abe982f7d6)#define LOG\_RAW(...) Z\_LOG\_PRINTK(1, \_\_VA\_ARGS\_\_)

119

[ 132](group__log__api.md#ga830f32743847c52e01a510ab0716fe90)#define LOG\_INST\_ERR(\_log\_inst, ...) \

133 Z\_LOG\_INSTANCE(LOG\_LEVEL\_ERR, \_log\_inst, \_\_VA\_ARGS\_\_)

134

[ 148](group__log__api.md#ga76057f789dfc164adbb1dbc9f3aff417)#define LOG\_INST\_WRN(\_log\_inst, ...) \

149 Z\_LOG\_INSTANCE(LOG\_LEVEL\_WRN, \_log\_inst, \_\_VA\_ARGS\_\_)

150

[ 163](group__log__api.md#ga222c5b535fb3ecb36dea97885c794188)#define LOG\_INST\_INF(\_log\_inst, ...) \

164 Z\_LOG\_INSTANCE(LOG\_LEVEL\_INF, \_log\_inst, \_\_VA\_ARGS\_\_)

165

[ 178](group__log__api.md#gae10014012020ea5a6b9a86a5224f19b0)#define LOG\_INST\_DBG(\_log\_inst, ...) \

179 Z\_LOG\_INSTANCE(LOG\_LEVEL\_DBG, \_log\_inst, \_\_VA\_ARGS\_\_)

180

[ 191](group__log__api.md#gabdae4f5b8b16804b53f83a85c3023134)#define LOG\_HEXDUMP\_ERR(\_data, \_length, \_str) \

192 Z\_LOG\_HEXDUMP(LOG\_LEVEL\_ERR, \_data, \_length, (\_str))

193

[ 204](group__log__api.md#gaf73802661fea926bb2b7e628727cdceb)#define LOG\_HEXDUMP\_WRN(\_data, \_length, \_str) \

205 Z\_LOG\_HEXDUMP(LOG\_LEVEL\_WRN, \_data, \_length, (\_str))

206

[ 216](group__log__api.md#ga8e060bbe660c246a38adccd873e58c6c)#define LOG\_HEXDUMP\_INF(\_data, \_length, \_str) \

217 Z\_LOG\_HEXDUMP(LOG\_LEVEL\_INF, \_data, \_length, (\_str))

218

[ 228](group__log__api.md#ga01dda8273f7d453a855542a52524dca8)#define LOG\_HEXDUMP\_DBG(\_data, \_length, \_str) \

229 Z\_LOG\_HEXDUMP(LOG\_LEVEL\_DBG, \_data, \_length, (\_str))

230

[ 245](group__log__api.md#gaf2f504a779917dc0f40767cba9f940b9)#define LOG\_INST\_HEXDUMP\_ERR(\_log\_inst, \_data, \_length, \_str) \

246 Z\_LOG\_HEXDUMP\_INSTANCE(LOG\_LEVEL\_ERR, \_log\_inst, \_data, \_length, \_str)

247

[ 260](group__log__api.md#gab6542651f88fbb0991fb2339102b52a5)#define LOG\_INST\_HEXDUMP\_WRN(\_log\_inst, \_data, \_length, \_str) \

261 Z\_LOG\_HEXDUMP\_INSTANCE(LOG\_LEVEL\_WRN, \_log\_inst, \_data, \_length, \_str)

262

[ 274](group__log__api.md#ga8e38c461c6058ee604b4dddad662d4ca)#define LOG\_INST\_HEXDUMP\_INF(\_log\_inst, \_data, \_length, \_str) \

275 Z\_LOG\_HEXDUMP\_INSTANCE(LOG\_LEVEL\_INF, \_log\_inst, \_data, \_length, \_str)

276

[ 288](group__log__api.md#ga4b73e6d51cff26ea5595df8680c00563)#define LOG\_INST\_HEXDUMP\_DBG(\_log\_inst, \_data, \_length, \_str) \

289 Z\_LOG\_HEXDUMP\_INSTANCE(LOG\_LEVEL\_DBG, \_log\_inst, \_data, \_length, \_str)

290

303void z\_log\_vprintk(const char \*fmt, va\_list ap);

304

305#ifdef \_\_cplusplus

306}

307#define LOG\_IN\_CPLUSPLUS 1

308#endif

309/\* Macro expects that optionally on second argument local log level is provided.

310 \* If provided it is returned, otherwise default log level is returned or

311 \* LOG\_LEVEL, if it was locally defined.

312 \*/

313#if !defined(CONFIG\_LOG)

314#define \_LOG\_LEVEL\_RESOLVE(...) LOG\_LEVEL\_NONE

315#else

316#define \_LOG\_LEVEL\_RESOLVE(...) \

317 Z\_LOG\_EVAL(COND\_CODE\_0(LOG\_LEVEL, (1), (LOG\_LEVEL)), \

318 (GET\_ARG\_N(2, \_\_VA\_ARGS\_\_, LOG\_LEVEL)), \

319 (GET\_ARG\_N(2, \_\_VA\_ARGS\_\_, CONFIG\_LOG\_DEFAULT\_LEVEL)))

320#endif

321

322/\* Return first argument \*/

323#define \_LOG\_ARG1(arg1, ...) arg1

324

325#define \_LOG\_MODULE\_CONST\_DATA\_CREATE(\_name, \_level) \

326 IF\_ENABLED(CONFIG\_LOG\_FMT\_SECTION, ( \

327 static const char UTIL\_CAT(\_name, \_str)[] \

328 \_\_in\_section(\_log\_strings, static, \_CONCAT(\_name, \_)) \_\_used \_\_noasan = \

329 STRINGIFY(\_name);)) \

330 IF\_ENABLED(LOG\_IN\_CPLUSPLUS, (extern)) \

331 const STRUCT\_SECTION\_ITERABLE\_ALTERNATE(log\_const, \

332 log\_source\_const\_data, \

333 Z\_LOG\_ITEM\_CONST\_DATA(\_name)) = \

334 { \

335 .name = COND\_CODE\_1(CONFIG\_LOG\_FMT\_SECTION, \

336 (UTIL\_CAT(\_name, \_str)), (STRINGIFY(\_name))), \

337 .level = (\_level) \

338 }

339

340#define \_LOG\_MODULE\_DYNAMIC\_DATA\_CREATE(\_name) \

341 STRUCT\_SECTION\_ITERABLE\_ALTERNATE(log\_dynamic, log\_source\_dynamic\_data, \

342 LOG\_ITEM\_DYNAMIC\_DATA(\_name))

343

344#define \_LOG\_MODULE\_DYNAMIC\_DATA\_COND\_CREATE(\_name) \

345 IF\_ENABLED(CONFIG\_LOG\_RUNTIME\_FILTERING, \

346 (\_LOG\_MODULE\_DYNAMIC\_DATA\_CREATE(\_name);))

347

348#define \_LOG\_MODULE\_DATA\_CREATE(\_name, \_level) \

349 \_LOG\_MODULE\_CONST\_DATA\_CREATE(\_name, \_level); \

350 \_LOG\_MODULE\_DYNAMIC\_DATA\_COND\_CREATE(\_name)

351

352/\* Determine if data for the module shall be created. It is created if logging

353 \* is enabled, override level is set or module specific level is set (not off).

354 \*/

355#define Z\_DO\_LOG\_MODULE\_REGISTER(...) \

356 COND\_CODE\_1(CONFIG\_LOG, \

357 (Z\_LOG\_EVAL(CONFIG\_LOG\_OVERRIDE\_LEVEL, \

358 (1), \

359 (Z\_LOG\_EVAL(\_LOG\_LEVEL\_RESOLVE(\_\_VA\_ARGS\_\_), (1), (0))) \

360 )), (0))

361

362/\* Determine if the data of the log module shall be in the partition

363 \* 'k\_log\_partition' to allow a user mode thread access to this data.

364 \*/

365#if CONFIG\_USERSPACE && CONFIG\_LOG\_ALWAYS\_RUNTIME

366extern struct [k\_mem\_partition](structk__mem__partition.md) k\_log\_partition;

367#define Z\_LOG\_MODULE\_PARTITION(\_k\_app\_mem) \_k\_app\_mem(k\_log\_partition)

368#else

369#define Z\_LOG\_MODULE\_PARTITION(\_k\_app\_mem)

370#endif

371

[ 403](group__log__api.md#ga2404243df68fb6e51129d1c7ecc5ca45)#define LOG\_MODULE\_REGISTER(...) \

404 COND\_CODE\_1( \

405 Z\_DO\_LOG\_MODULE\_REGISTER(\_\_VA\_ARGS\_\_), \

406 (\_LOG\_MODULE\_DATA\_CREATE(GET\_ARG\_N(1, \_\_VA\_ARGS\_\_), \

407 \_LOG\_LEVEL\_RESOLVE(\_\_VA\_ARGS\_\_))),\

408 () \

409 ) \

410 LOG\_MODULE\_DECLARE(\_\_VA\_ARGS\_\_)

411

[ 438](group__log__api.md#ga8193b0e10e5ee64b86848bb52be31869)#define LOG\_MODULE\_DECLARE(...) \

439 extern const struct log\_source\_const\_data \

440 Z\_LOG\_ITEM\_CONST\_DATA(GET\_ARG\_N(1, \_\_VA\_ARGS\_\_)); \

441 extern struct log\_source\_dynamic\_data \

442 LOG\_ITEM\_DYNAMIC\_DATA(GET\_ARG\_N(1, \_\_VA\_ARGS\_\_)); \

443 \

444 Z\_LOG\_MODULE\_PARTITION(K\_APP\_DMEM) \

445 static const struct log\_source\_const\_data \* \

446 \_\_log\_current\_const\_data \_\_unused = \

447 Z\_DO\_LOG\_MODULE\_REGISTER(\_\_VA\_ARGS\_\_) ? \

448 &Z\_LOG\_ITEM\_CONST\_DATA(GET\_ARG\_N(1, \_\_VA\_ARGS\_\_)) : \

449 NULL; \

450 \

451 Z\_LOG\_MODULE\_PARTITION(K\_APP\_DMEM) \

452 static struct log\_source\_dynamic\_data \* \

453 \_\_log\_current\_dynamic\_data \_\_unused = \

454 (Z\_DO\_LOG\_MODULE\_REGISTER(\_\_VA\_ARGS\_\_) && \

455 IS\_ENABLED(CONFIG\_LOG\_RUNTIME\_FILTERING)) ? \

456 &LOG\_ITEM\_DYNAMIC\_DATA(GET\_ARG\_N(1, \_\_VA\_ARGS\_\_)) : \

457 NULL; \

458 \

459 Z\_LOG\_MODULE\_PARTITION(K\_APP\_BMEM) \

460 static const uint32\_t \_\_log\_level \_\_unused = \

461 \_LOG\_LEVEL\_RESOLVE(\_\_VA\_ARGS\_\_)

462

[ 470](group__log__api.md#gac396852328a77360a0c27dbf7b52356e)#define LOG\_LEVEL\_SET(level) static const uint32\_t \_\_log\_level \_\_unused = \

471 Z\_LOG\_RESOLVED\_LEVEL(level, 0)

472

473#ifdef CONFIG\_LOG\_CUSTOM\_HEADER

474/\* This include must always be at the end of log.h \*/

475#include <zephyr\_custom\_log.h>

476#endif

477

478/\*

479 \* Eclipse CDT or JetBrains Clion parser is sometimes confused by logging API

480 \* code and freezes the whole IDE. Following lines hides LOG\_x macros from them.

481 \*/

482#if defined(\_\_CDT\_PARSER\_\_) || defined(\_\_JETBRAINS\_IDE\_\_)

483#undef LOG\_ERR

484#undef LOG\_WRN

485#undef LOG\_INF

486#undef LOG\_DBG

487

488#undef LOG\_HEXDUMP\_ERR

489#undef LOG\_HEXDUMP\_WRN

490#undef LOG\_HEXDUMP\_INF

491#undef LOG\_HEXDUMP\_DBG

492

493#define LOG\_ERR(...) (void) 0

494#define LOG\_WRN(...) (void) 0

495#define LOG\_DBG(...) (void) 0

496#define LOG\_INF(...) (void) 0

497

498#define LOG\_HEXDUMP\_ERR(...) (void) 0

499#define LOG\_HEXDUMP\_WRN(...) (void) 0

500#define LOG\_HEXDUMP\_DBG(...) (void) 0

501#define LOG\_HEXDUMP\_INF(...) (void) 0

502#endif

503

507

508#endif /\* ZEPHYR\_INCLUDE\_LOGGING\_LOG\_H\_ \*/

[app\_memdomain.h](app__memdomain_8h.md)

[log\_core.h](log__core_8h.md)

[log\_instance.h](log__instance_8h.md)

[k\_mem\_partition](structk__mem__partition.md)

Memory Partition.

**Definition** mem\_domain.h:55

[iterable\_sections.h](sys_2iterable__sections_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [logging](dir_7da6482b46a75d2870a82324d67b5f7e.md)
- [log.h](log_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
