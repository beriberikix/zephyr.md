---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/log_8h_source.html
original_path: doxygen/html/log_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
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

11#include <[zephyr/logging/log\_core.h](include_2zephyr_2logging_2log__core_8h.md)>

12#include <[zephyr/sys/iterable\_sections.h](sys_2iterable__sections_8h.md)>

13

14#ifdef \_\_cplusplus

15extern "C" {

16#endif

17

25

32

[ 42](group__log__api.md#gad6db28c61c838c1f7316417e1e4847f2)#define LOG\_ERR(...) Z\_LOG(LOG\_LEVEL\_ERR, \_\_VA\_ARGS\_\_)

43

[ 53](group__log__api.md#ga644db4299681d9ebf06f8745ad984c65)#define LOG\_WRN(...) Z\_LOG(LOG\_LEVEL\_WRN, \_\_VA\_ARGS\_\_)

54

[ 63](group__log__api.md#ga9c338f3170acf38a8532d1181d26704e)#define LOG\_INF(...) Z\_LOG(LOG\_LEVEL\_INF, \_\_VA\_ARGS\_\_)

64

[ 73](group__log__api.md#gafb97e6291db24665313453d192941330)#define LOG\_DBG(...) Z\_LOG(LOG\_LEVEL\_DBG, \_\_VA\_ARGS\_\_)

74

[ 84](group__log__api.md#ga4ab5cae247b853bf9f4f0bf761c1c71e)#define LOG\_PRINTK(...) Z\_LOG\_PRINTK(0, \_\_VA\_ARGS\_\_)

85

[ 94](group__log__api.md#ga7dedf58739648ed9b9aef1abe982f7d6)#define LOG\_RAW(...) Z\_LOG\_PRINTK(1, \_\_VA\_ARGS\_\_)

95

[ 108](group__log__api.md#ga830f32743847c52e01a510ab0716fe90)#define LOG\_INST\_ERR(\_log\_inst, ...) \

109 Z\_LOG\_INSTANCE(LOG\_LEVEL\_ERR, \_log\_inst, \_\_VA\_ARGS\_\_)

110

[ 124](group__log__api.md#ga76057f789dfc164adbb1dbc9f3aff417)#define LOG\_INST\_WRN(\_log\_inst, ...) \

125 Z\_LOG\_INSTANCE(LOG\_LEVEL\_WRN, \_log\_inst, \_\_VA\_ARGS\_\_)

126

[ 139](group__log__api.md#ga222c5b535fb3ecb36dea97885c794188)#define LOG\_INST\_INF(\_log\_inst, ...) \

140 Z\_LOG\_INSTANCE(LOG\_LEVEL\_INF, \_log\_inst, \_\_VA\_ARGS\_\_)

141

[ 154](group__log__api.md#gae10014012020ea5a6b9a86a5224f19b0)#define LOG\_INST\_DBG(\_log\_inst, ...) \

155 Z\_LOG\_INSTANCE(LOG\_LEVEL\_DBG, \_log\_inst, \_\_VA\_ARGS\_\_)

156

[ 167](group__log__api.md#gabdae4f5b8b16804b53f83a85c3023134)#define LOG\_HEXDUMP\_ERR(\_data, \_length, \_str) \

168 Z\_LOG\_HEXDUMP(LOG\_LEVEL\_ERR, \_data, \_length, \_str)

169

[ 180](group__log__api.md#gaf73802661fea926bb2b7e628727cdceb)#define LOG\_HEXDUMP\_WRN(\_data, \_length, \_str) \

181 Z\_LOG\_HEXDUMP(LOG\_LEVEL\_WRN, \_data, \_length, \_str)

182

[ 192](group__log__api.md#ga8e060bbe660c246a38adccd873e58c6c)#define LOG\_HEXDUMP\_INF(\_data, \_length, \_str) \

193 Z\_LOG\_HEXDUMP(LOG\_LEVEL\_INF, \_data, \_length, \_str)

194

[ 204](group__log__api.md#ga01dda8273f7d453a855542a52524dca8)#define LOG\_HEXDUMP\_DBG(\_data, \_length, \_str) \

205 Z\_LOG\_HEXDUMP(LOG\_LEVEL\_DBG, \_data, \_length, \_str)

206

[ 221](group__log__api.md#gaf2f504a779917dc0f40767cba9f940b9)#define LOG\_INST\_HEXDUMP\_ERR(\_log\_inst, \_data, \_length, \_str) \

222 Z\_LOG\_HEXDUMP\_INSTANCE(LOG\_LEVEL\_ERR, \_log\_inst, \_data, \_length, \_str)

223

[ 236](group__log__api.md#gab6542651f88fbb0991fb2339102b52a5)#define LOG\_INST\_HEXDUMP\_WRN(\_log\_inst, \_data, \_length, \_str) \

237 Z\_LOG\_HEXDUMP\_INSTANCE(LOG\_LEVEL\_WRN, \_log\_inst, \_data, \_length, \_str)

238

[ 250](group__log__api.md#ga8e38c461c6058ee604b4dddad662d4ca)#define LOG\_INST\_HEXDUMP\_INF(\_log\_inst, \_data, \_length, \_str) \

251 Z\_LOG\_HEXDUMP\_INSTANCE(LOG\_LEVEL\_INF, \_log\_inst, \_data, \_length, \_str)

252

[ 264](group__log__api.md#ga4b73e6d51cff26ea5595df8680c00563)#define LOG\_INST\_HEXDUMP\_DBG(\_log\_inst, \_data, \_length, \_str) \

265 Z\_LOG\_HEXDUMP\_INSTANCE(LOG\_LEVEL\_DBG, \_log\_inst, \_data, \_length, \_str)

266

279void z\_log\_vprintk(const char \*fmt, va\_list ap);

280

281#ifdef \_\_cplusplus

282}

283#define LOG\_IN\_CPLUSPLUS 1

284#endif

285/\* Macro expects that optionally on second argument local log level is provided.

286 \* If provided it is returned, otherwise default log level is returned or

287 \* LOG\_LEVEL, if it was locally defined.

288 \*/

289#if !defined(CONFIG\_LOG)

290#define \_LOG\_LEVEL\_RESOLVE(...) LOG\_LEVEL\_NONE

291#else

292#define \_LOG\_LEVEL\_RESOLVE(...) \

293 Z\_LOG\_EVAL(COND\_CODE\_0(LOG\_LEVEL, (1), (LOG\_LEVEL)), \

294 (GET\_ARG\_N(2, \_\_VA\_ARGS\_\_, LOG\_LEVEL)), \

295 (GET\_ARG\_N(2, \_\_VA\_ARGS\_\_, CONFIG\_LOG\_DEFAULT\_LEVEL)))

296#endif

297

298/\* Return first argument \*/

299#define \_LOG\_ARG1(arg1, ...) arg1

300

301#define \_LOG\_MODULE\_CONST\_DATA\_CREATE(\_name, \_level) \

302 IF\_ENABLED(CONFIG\_LOG\_FMT\_SECTION, ( \

303 static const char UTIL\_CAT(\_name, \_str)[] \

304 \_\_in\_section(\_log\_strings, static, \_CONCAT(\_name, \_)) \_\_used \_\_noasan = \

305 STRINGIFY(\_name);)) \

306 IF\_ENABLED(LOG\_IN\_CPLUSPLUS, (extern)) \

307 const STRUCT\_SECTION\_ITERABLE\_ALTERNATE(log\_const, \

308 log\_source\_const\_data, \

309 Z\_LOG\_ITEM\_CONST\_DATA(\_name)) = \

310 { \

311 .name = COND\_CODE\_1(CONFIG\_LOG\_FMT\_SECTION, \

312 (UTIL\_CAT(\_name, \_str)), (STRINGIFY(\_name))), \

313 .level = \_level \

314 }

315

316#define \_LOG\_MODULE\_DYNAMIC\_DATA\_CREATE(\_name) \

317 STRUCT\_SECTION\_ITERABLE\_ALTERNATE(log\_dynamic, log\_source\_dynamic\_data, \

318 LOG\_ITEM\_DYNAMIC\_DATA(\_name))

319

320#define \_LOG\_MODULE\_DYNAMIC\_DATA\_COND\_CREATE(\_name) \

321 IF\_ENABLED(CONFIG\_LOG\_RUNTIME\_FILTERING, \

322 (\_LOG\_MODULE\_DYNAMIC\_DATA\_CREATE(\_name);))

323

324#define \_LOG\_MODULE\_DATA\_CREATE(\_name, \_level) \

325 \_LOG\_MODULE\_CONST\_DATA\_CREATE(\_name, \_level); \

326 \_LOG\_MODULE\_DYNAMIC\_DATA\_COND\_CREATE(\_name)

327

328/\* Determine if data for the module shall be created. It is created if logging

329 \* is enabled, override level is set or module specific level is set (not off).

330 \*/

331#define Z\_DO\_LOG\_MODULE\_REGISTER(...) \

332 COND\_CODE\_1(CONFIG\_LOG, \

333 (Z\_LOG\_EVAL(CONFIG\_LOG\_OVERRIDE\_LEVEL, \

334 (1), \

335 (Z\_LOG\_EVAL(\_LOG\_LEVEL\_RESOLVE(\_\_VA\_ARGS\_\_), (1), (0))) \

336 )), (0))

337

[ 369](group__log__api.md#ga2404243df68fb6e51129d1c7ecc5ca45)#define LOG\_MODULE\_REGISTER(...) \

370 COND\_CODE\_1( \

371 Z\_DO\_LOG\_MODULE\_REGISTER(\_\_VA\_ARGS\_\_), \

372 (\_LOG\_MODULE\_DATA\_CREATE(GET\_ARG\_N(1, \_\_VA\_ARGS\_\_), \

373 \_LOG\_LEVEL\_RESOLVE(\_\_VA\_ARGS\_\_))),\

374 () \

375 ) \

376 LOG\_MODULE\_DECLARE(\_\_VA\_ARGS\_\_)

377

[ 404](group__log__api.md#ga8193b0e10e5ee64b86848bb52be31869)#define LOG\_MODULE\_DECLARE(...) \

405 extern const struct log\_source\_const\_data \

406 Z\_LOG\_ITEM\_CONST\_DATA(GET\_ARG\_N(1, \_\_VA\_ARGS\_\_)); \

407 extern struct log\_source\_dynamic\_data \

408 LOG\_ITEM\_DYNAMIC\_DATA(GET\_ARG\_N(1, \_\_VA\_ARGS\_\_)); \

409 \

410 static const struct log\_source\_const\_data \* \

411 \_\_log\_current\_const\_data \_\_unused = \

412 Z\_DO\_LOG\_MODULE\_REGISTER(\_\_VA\_ARGS\_\_) ? \

413 &Z\_LOG\_ITEM\_CONST\_DATA(GET\_ARG\_N(1, \_\_VA\_ARGS\_\_)) : \

414 NULL; \

415 \

416 static struct log\_source\_dynamic\_data \* \

417 \_\_log\_current\_dynamic\_data \_\_unused = \

418 (Z\_DO\_LOG\_MODULE\_REGISTER(\_\_VA\_ARGS\_\_) && \

419 IS\_ENABLED(CONFIG\_LOG\_RUNTIME\_FILTERING)) ? \

420 &LOG\_ITEM\_DYNAMIC\_DATA(GET\_ARG\_N(1, \_\_VA\_ARGS\_\_)) : \

421 NULL; \

422 \

423 static const uint32\_t \_\_log\_level \_\_unused = \

424 \_LOG\_LEVEL\_RESOLVE(\_\_VA\_ARGS\_\_)

425

[ 433](group__log__api.md#gac396852328a77360a0c27dbf7b52356e)#define LOG\_LEVEL\_SET(level) static const uint32\_t \_\_log\_level \_\_unused = \

434 Z\_LOG\_RESOLVED\_LEVEL(level, 0)

435

436#ifdef CONFIG\_LOG\_CUSTOM\_HEADER

437/\* This include must always be at the end of log.h \*/

438#include <zephyr\_custom\_log.h>

439#endif

440

441/\*

442 \* Eclipse CDT or JetBrains Clion parser is sometimes confused by logging API

443 \* code and freezes the whole IDE. Following lines hides LOG\_x macros from them.

444 \*/

445#if defined(\_\_CDT\_PARSER\_\_) || defined(\_\_JETBRAINS\_IDE\_\_)

446#undef LOG\_ERR

447#undef LOG\_WRN

448#undef LOG\_INF

449#undef LOG\_DBG

450

451#undef LOG\_HEXDUMP\_ERR

452#undef LOG\_HEXDUMP\_WRN

453#undef LOG\_HEXDUMP\_INF

454#undef LOG\_HEXDUMP\_DBG

455

456#define LOG\_ERR(...) (void) 0

457#define LOG\_WRN(...) (void) 0

458#define LOG\_DBG(...) (void) 0

459#define LOG\_INF(...) (void) 0

460

461#define LOG\_HEXDUMP\_ERR(...) (void) 0

462#define LOG\_HEXDUMP\_WRN(...) (void) 0

463#define LOG\_HEXDUMP\_DBG(...) (void) 0

464#define LOG\_HEXDUMP\_INF(...) (void) 0

465#endif

466

470

471#endif /\* ZEPHYR\_INCLUDE\_LOGGING\_LOG\_H\_ \*/

[log\_core.h](include_2zephyr_2logging_2log__core_8h.md)

[log\_instance.h](log__instance_8h.md)

[iterable\_sections.h](sys_2iterable__sections_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [logging](dir_7da6482b46a75d2870a82324d67b5f7e.md)
- [log.h](log_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
