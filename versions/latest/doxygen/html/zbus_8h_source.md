---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/zbus_8h_source.html
original_path: doxygen/html/zbus_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

zbus.h

[Go to the documentation of this file.](zbus_8h.md)

1/\*

2 \* Copyright (c) 2022 Rodrigo Peixoto <rodrigopex@gmail.com>

3 \* SPDX-License-Identifier: Apache-2.0

4 \*/

5

6#ifndef ZEPHYR\_INCLUDE\_ZBUS\_H\_

7#define ZEPHYR\_INCLUDE\_ZBUS\_H\_

8

9#include <[string.h](string_8h.md)>

10

11#include <[zephyr/kernel.h](include_2zephyr_2kernel_8h.md)>

12#include <[zephyr/sys/iterable\_sections.h](sys_2iterable__sections_8h.md)>

13

14#ifdef \_\_cplusplus

15extern "C" {

16#endif

17

24

[ 30](structzbus__channel__data.md)struct [zbus\_channel\_data](structzbus__channel__data.md) {

[ 34](structzbus__channel__data.md#a6329a0af467d83ad488f3310c1002c41) [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) [observers\_start\_idx](structzbus__channel__data.md#a6329a0af467d83ad488f3310c1002c41);

35

[ 39](structzbus__channel__data.md#a5b3c38f70cd99cc7e83f9b641997e1ed) [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) [observers\_end\_idx](structzbus__channel__data.md#a5b3c38f70cd99cc7e83f9b641997e1ed);

40

[ 44](structzbus__channel__data.md#a6fa71ae5dc260f5934f47383f53891a7) struct k\_sem [sem](structzbus__channel__data.md#a6fa71ae5dc260f5934f47383f53891a7);

45

46#if defined(CONFIG\_ZBUS\_PRIORITY\_BOOST)

50 int highest\_observer\_priority;

51#endif /\* CONFIG\_ZBUS\_PRIORITY\_BOOST \*/

52

53#if defined(CONFIG\_ZBUS\_RUNTIME\_OBSERVERS) || defined(\_\_DOXYGEN\_\_)

[ 57](structzbus__channel__data.md#aeffcb35769775ee0927c3af9be77d1e1) [sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8) [observers](structzbus__channel__data.md#aeffcb35769775ee0927c3af9be77d1e1);

58#endif /\* CONFIG\_ZBUS\_RUNTIME\_OBSERVERS \*/

59};

60

[ 67](structzbus__channel.md)struct [zbus\_channel](structzbus__channel.md) {

68#if defined(CONFIG\_ZBUS\_CHANNEL\_NAME) || defined(\_\_DOXYGEN\_\_)

[ 70](structzbus__channel.md#a9839e77746c53d24de69453aea53a233) const char \*const [name](structzbus__channel.md#a9839e77746c53d24de69453aea53a233);

71#endif

[ 75](structzbus__channel.md#a7e8bd8f6c080615a4c4d524101201f19) void \*const [message](structzbus__channel.md#a7e8bd8f6c080615a4c4d524101201f19);

76

[ 78](structzbus__channel.md#a508bf72f7b47ad8781b4e4ef3645d17a) const size\_t [message\_size](structzbus__channel.md#a508bf72f7b47ad8781b4e4ef3645d17a);

79

[ 83](structzbus__channel.md#ae629044f9b6da800db5a628fc6789dfb) void \*const [user\_data](structzbus__channel.md#ae629044f9b6da800db5a628fc6789dfb);

84

[ 89](structzbus__channel.md#a047e9da011488c8f11abdc1fd283f5f6) [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) (\*const [validator](structzbus__channel.md#a047e9da011488c8f11abdc1fd283f5f6))(const void \*msg, size\_t msg\_size);

90

[ 92](structzbus__channel.md#a30ad5027b70d6e9d28d0b0caef3571fe) struct [zbus\_channel\_data](structzbus__channel__data.md) \*const [data](structzbus__channel.md#a30ad5027b70d6e9d28d0b0caef3571fe);

93};

94

[ 100](group__zbus__apis.md#ga88941281d7bdd24f3cfbb53e57711d8f)enum \_\_packed [zbus\_observer\_type](group__zbus__apis.md#ga88941281d7bdd24f3cfbb53e57711d8f) {

[ 101](group__zbus__apis.md#gga88941281d7bdd24f3cfbb53e57711d8fa127f19c2121c9c512da9dbcbb301320c) [ZBUS\_OBSERVER\_LISTENER\_TYPE](group__zbus__apis.md#gga88941281d7bdd24f3cfbb53e57711d8fa127f19c2121c9c512da9dbcbb301320c),

[ 102](group__zbus__apis.md#gga88941281d7bdd24f3cfbb53e57711d8fa22c784a85353545e8dca2ce7a0ec81b3) [ZBUS\_OBSERVER\_SUBSCRIBER\_TYPE](group__zbus__apis.md#gga88941281d7bdd24f3cfbb53e57711d8fa22c784a85353545e8dca2ce7a0ec81b3),

[ 103](group__zbus__apis.md#gga88941281d7bdd24f3cfbb53e57711d8fa8151f9e58a5bd96449bd2f9f8695538c) [ZBUS\_OBSERVER\_MSG\_SUBSCRIBER\_TYPE](group__zbus__apis.md#gga88941281d7bdd24f3cfbb53e57711d8fa8151f9e58a5bd96449bd2f9f8695538c),

104};

105

[ 106](structzbus__observer__data.md)struct [zbus\_observer\_data](structzbus__observer__data.md) {

[ 108](structzbus__observer__data.md#ad16ca7a9e83f54afd75f6accf471eb91) bool [enabled](structzbus__observer__data.md#ad16ca7a9e83f54afd75f6accf471eb91);

109

110#if defined(CONFIG\_ZBUS\_PRIORITY\_BOOST)

112 int priority;

113#endif /\* CONFIG\_ZBUS\_PRIORITY\_BOOST \*/

114};

115

[ 131](structzbus__observer.md)struct [zbus\_observer](structzbus__observer.md) {

132#if defined(CONFIG\_ZBUS\_OBSERVER\_NAME) || defined(\_\_DOXYGEN\_\_)

[ 134](structzbus__observer.md#ab2ba28a935b528b2db90389071769fd5) const char \*const [name](structzbus__observer.md#ab2ba28a935b528b2db90389071769fd5);

135#endif

[ 137](structzbus__observer.md#a0251cf9bdca418b6b8123b998b57efe2) enum [zbus\_observer\_type](group__zbus__apis.md#ga88941281d7bdd24f3cfbb53e57711d8f) [type](structzbus__observer.md#a0251cf9bdca418b6b8123b998b57efe2);

138

[ 140](structzbus__observer.md#a76bbaaf17ce0c58bfa9f9b604cbb496d) struct [zbus\_observer\_data](structzbus__observer__data.md) \*const [data](structzbus__observer.md#a76bbaaf17ce0c58bfa9f9b604cbb496d);

141

142 union {

[ 144](structzbus__observer.md#a7da8da6038d3dad4bc4c05279c28310c) struct [k\_msgq](structk__msgq.md) \*const [queue](structzbus__observer.md#a7da8da6038d3dad4bc4c05279c28310c);

145

[ 147](structzbus__observer.md#a71fe83641f3e8c6248602150cbd998a1) void (\*const [callback](structzbus__observer.md#a71fe83641f3e8c6248602150cbd998a1))(const struct [zbus\_channel](structzbus__channel.md) \*chan);

148

149#if defined(CONFIG\_ZBUS\_MSG\_SUBSCRIBER) || defined(\_\_DOXYGEN\_\_)

[ 153](structzbus__observer.md#a9073bc59a4662385d6c5d487e7be03c9) struct [k\_fifo](structk__fifo.md) \*const [message\_fifo](structzbus__observer.md#a9073bc59a4662385d6c5d487e7be03c9);

154#endif /\* CONFIG\_ZBUS\_MSG\_SUBSCRIBER \*/

155 };

156};

157

159struct zbus\_channel\_observation\_mask {

160 bool enabled;

161};

162

163struct zbus\_channel\_observation {

164 const struct zbus\_channel \*const chan;

165 const struct zbus\_observer \*const obs;

166};

167

168#ifdef \_\_cplusplus

169#define \_ZBUS\_CPP\_EXTERN extern

170#else

171#define \_ZBUS\_CPP\_EXTERN

172#endif /\* \_\_cplusplus \*/

173

174#define ZBUS\_MIN\_THREAD\_PRIORITY (CONFIG\_NUM\_PREEMPT\_PRIORITIES - 1)

175

176#if defined(CONFIG\_ZBUS\_ASSERT\_MOCK)

177#define \_ZBUS\_ASSERT(\_cond, \_fmt, ...) \

178 do { \

179 if (!(\_cond)) { \

180 printk("ZBUS ASSERT: "); \

181 printk(\_fmt, ##\_\_VA\_ARGS\_\_); \

182 printk("\n"); \

183 return -EFAULT; \

184 } \

185 } while (0)

186#else

187#define \_ZBUS\_ASSERT(\_cond, \_fmt, ...) \_\_ASSERT(\_cond, \_fmt, ##\_\_VA\_ARGS\_\_)

188#endif

189

190#if defined(CONFIG\_ZBUS\_CHANNEL\_NAME)

191#define ZBUS\_CHANNEL\_NAME\_INIT(\_name) .name = #\_name,

192#define \_ZBUS\_CHAN\_NAME(\_chan) (\_chan)->name

193#else

194#define ZBUS\_CHANNEL\_NAME\_INIT(\_name)

195#define \_ZBUS\_CHAN\_NAME(\_chan) ""

196#endif

197

198#if defined(CONFIG\_ZBUS\_OBSERVER\_NAME)

199#define ZBUS\_OBSERVER\_NAME\_INIT(\_name) .name = #\_name,

200#define \_ZBUS\_OBS\_NAME(\_obs) (\_obs)->name

201#else

202#define ZBUS\_OBSERVER\_NAME\_INIT(\_name)

203#define \_ZBUS\_OBS\_NAME(\_obs) ""

204#endif

205

206#if defined(CONFIG\_ZBUS\_RUNTIME\_OBSERVERS)

207#define ZBUS\_RUNTIME\_OBSERVERS\_LIST\_DECL(\_slist\_name) static sys\_slist\_t \_slist\_name

208#define ZBUS\_RUNTIME\_OBSERVERS\_LIST\_INIT(\_slist\_name) .runtime\_observers = &\_slist\_name,

209#else

210#define ZBUS\_RUNTIME\_OBSERVERS\_LIST\_DECL(\_slist\_name)

211#define ZBUS\_RUNTIME\_OBSERVERS\_LIST\_INIT(\_slist\_name) /\* No runtime observers \*/

212#endif

213

214#define \_ZBUS\_OBS\_EXTERN(\_name) extern struct zbus\_observer \_name

215

216#define \_ZBUS\_CHAN\_EXTERN(\_name) extern const struct zbus\_channel \_name

217

218#define ZBUS\_REF(\_value) &(\_value)

219

220#define FOR\_EACH\_FIXED\_ARG\_NONEMPTY\_TERM(F, sep, fixed\_arg, ...) \

221 COND\_CODE\_0(/\* are there zero non-empty arguments ? \*/ \

222 NUM\_VA\_ARGS\_LESS\_1( \

223 LIST\_DROP\_EMPTY(\_\_VA\_ARGS\_\_, \_)), /\* if so, expand to nothing \*/ \

224 (), /\* otherwise, expand to: \*/ \

225 (FOR\_EACH\_IDX\_FIXED\_ARG( \

226 F, sep, fixed\_arg, \

227 LIST\_DROP\_EMPTY(\_\_VA\_ARGS\_\_)) /\* plus a final terminator \*/ \

228 \_\_DEBRACKET sep))

229

230#define \_ZBUS\_OBSERVATION\_PREFIX(\_idx) \

231 GET\_ARG\_N(\_idx, 00, 01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 11, 12, 13, 14, 15, 16, 17, \

232 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, \

233 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, \

234 58, 59, 60, 61, 62, 63)

235

236#define \_ZBUS\_CHAN\_OBSERVATION(\_idx, \_obs, \_chan) \

237 const STRUCT\_SECTION\_ITERABLE( \

238 zbus\_channel\_observation, \

239 \_CONCAT(\_chan, \_ZBUS\_OBSERVATION\_PREFIX(UTIL\_INC(\_idx)))) = {.chan = &\_chan, \

240 .obs = &\_obs}; \

241 STRUCT\_SECTION\_ITERABLE(zbus\_channel\_observation\_mask, \

242 \_CONCAT(\_CONCAT(\_chan, \_ZBUS\_OBSERVATION\_PREFIX(UTIL\_INC(\_idx))), \

243 \_mask)) = {.enabled = false};

244

245#if defined(CONFIG\_ZBUS\_RUNTIME\_OBSERVERS) || defined(\_\_DOXYGEN\_\_)

246#define \_ZBUS\_RUNTIME\_OBSERVERS(\_name) .observers = &(\_CONCAT(\_observers\_, \_name)),

247#define \_ZBUS\_RUNTIME\_OBSERVERS\_DECL(\_name) static sys\_slist\_t \_CONCAT(\_observers\_, \_name);

248#else

249#define \_ZBUS\_RUNTIME\_OBSERVERS(\_name)

250#define \_ZBUS\_RUNTIME\_OBSERVERS\_DECL(\_name)

251#endif /\* CONFIG\_ZBUS\_RUNTIME\_OBSERVERS \*/

252

254

255/\* clang-format off \*/

[ 267](group__zbus__apis.md#ga7f763caca474e6c910793d2c714f80b4)#define ZBUS\_CHAN\_ADD\_OBS\_WITH\_MASK(\_chan, \_obs, \_masked, \_prio) \

268 const STRUCT\_SECTION\_ITERABLE(zbus\_channel\_observation, \

269 \_CONCAT(\_CONCAT(\_chan, zz), \_CONCAT(\_prio, \_obs))) = { \

270 .chan = &\_chan, \

271 .obs = &\_obs, \

272 }; \

273 STRUCT\_SECTION\_ITERABLE(zbus\_channel\_observation\_mask, \

274 \_CONCAT(\_CONCAT(\_CONCAT(\_chan, zz), \_CONCAT(\_prio, \_obs)), \

275 \_mask)) = {.enabled = \_masked}

276/\* clang-format on \*/

277

[ 288](group__zbus__apis.md#gaf63215f3f53741edf52b4d0d7b2b97df)#define ZBUS\_CHAN\_ADD\_OBS(\_chan, \_obs, \_prio) ZBUS\_CHAN\_ADD\_OBS\_WITH\_MASK(\_chan, \_obs, false, \_prio)

289

[ 295](group__zbus__apis.md#ga49f169c6d50a3bad57e1b319362d2924)#define ZBUS\_OBS\_DECLARE(...) FOR\_EACH\_NONEMPTY\_TERM(\_ZBUS\_OBS\_EXTERN, (;), \_\_VA\_ARGS\_\_)

296

[ 302](group__zbus__apis.md#ga0662b2db8077a8075c07a3afd0161d0f)#define ZBUS\_CHAN\_DECLARE(...) FOR\_EACH(\_ZBUS\_CHAN\_EXTERN, (;), \_\_VA\_ARGS\_\_)

303

[ 308](group__zbus__apis.md#ga763dad07a1ae9bb38f9c240e1920caef)#define ZBUS\_OBSERVERS\_EMPTY

309

[ 315](group__zbus__apis.md#gafed25f045c3b8d438daf4ebd5e517692)#define ZBUS\_OBSERVERS(...) \_\_VA\_ARGS\_\_

316

317/\* clang-format off \*/

[ 333](group__zbus__apis.md#ga29a3a39e5c78a34b2d8491615d1f0687)#define ZBUS\_CHAN\_DEFINE(\_name, \_type, \_validator, \_user\_data, \_observers, \_init\_val) \

334 static \_type \_CONCAT(\_zbus\_message\_, \_name) = \_init\_val; \

335 static struct zbus\_channel\_data \_CONCAT(\_zbus\_chan\_data\_, \_name) = { \

336 .observers\_start\_idx = -1, \

337 .observers\_end\_idx = -1, \

338 IF\_ENABLED(CONFIG\_ZBUS\_PRIORITY\_BOOST, ( \

339 .highest\_observer\_priority = ZBUS\_MIN\_THREAD\_PRIORITY, \

340 )) \

341 }; \

342 static K\_MUTEX\_DEFINE(\_CONCAT(\_zbus\_mutex\_, \_name)); \

343 \_ZBUS\_CPP\_EXTERN const STRUCT\_SECTION\_ITERABLE(zbus\_channel, \_name) = { \

344 ZBUS\_CHANNEL\_NAME\_INIT(\_name) /\* Maybe removed \*/ \

345 .message = &\_CONCAT(\_zbus\_message\_, \_name), \

346 .message\_size = sizeof(\_type), \

347 .user\_data = \_user\_data, \

348 .validator = \_validator, \

349 .data = &\_CONCAT(\_zbus\_chan\_data\_, \_name), \

350 }; \

351 /\* Extern declaration of observers \*/ \

352 ZBUS\_OBS\_DECLARE(\_observers); \

353 /\* Create all channel observations from observers list \*/ \

354 FOR\_EACH\_FIXED\_ARG\_NONEMPTY\_TERM(\_ZBUS\_CHAN\_OBSERVATION, (;), \_name, \_observers)

355/\* clang-format on \*/

356

[ 366](group__zbus__apis.md#ga4bf8c445814c1fcee9b9819a36bc9bd6)#define ZBUS\_MSG\_INIT(\_val, ...) \

367 { \

368 \_val, ##\_\_VA\_ARGS\_\_ \

369 }

370

371/\* clang-format off \*/

[ 383](group__zbus__apis.md#gaf56f71babe2bb27258f025332b80c58f)#define ZBUS\_SUBSCRIBER\_DEFINE\_WITH\_ENABLE(\_name, \_queue\_size, \_enable) \

384 K\_MSGQ\_DEFINE(\_zbus\_observer\_queue\_##\_name, \

385 sizeof(const struct zbus\_channel \*), \

386 \_queue\_size, sizeof(const struct zbus\_channel \*) \

387 ); \

388 static struct zbus\_observer\_data \_CONCAT(\_zbus\_obs\_data\_, \_name) = { \

389 .enabled = \_enable, \

390 IF\_ENABLED(CONFIG\_ZBUS\_PRIORITY\_BOOST, ( \

391 .priority = ZBUS\_MIN\_THREAD\_PRIORITY, \

392 )) \

393 }; \

394 STRUCT\_SECTION\_ITERABLE(zbus\_observer, \_name) = { \

395 ZBUS\_OBSERVER\_NAME\_INIT(\_name) /\* Name field \*/ \

396 .type = ZBUS\_OBSERVER\_SUBSCRIBER\_TYPE, \

397 .data = &\_CONCAT(\_zbus\_obs\_data\_, \_name), \

398 .queue = &\_zbus\_observer\_queue\_##\_name, \

399 }

400/\* clang-format on \*/

401

[ 413](group__zbus__apis.md#gac17a735cccecfc90f26127e48cf6279a)#define ZBUS\_SUBSCRIBER\_DEFINE(\_name, \_queue\_size) \

414 ZBUS\_SUBSCRIBER\_DEFINE\_WITH\_ENABLE(\_name, \_queue\_size, true)

415

416/\* clang-format off \*/

[ 428](group__zbus__apis.md#gace4ac9da0e1bab7ba72797783ded948f)#define ZBUS\_LISTENER\_DEFINE\_WITH\_ENABLE(\_name, \_cb, \_enable) \

429 static struct zbus\_observer\_data \_CONCAT(\_zbus\_obs\_data\_, \_name) = { \

430 .enabled = \_enable, \

431 IF\_ENABLED(CONFIG\_ZBUS\_PRIORITY\_BOOST, ( \

432 .priority = ZBUS\_MIN\_THREAD\_PRIORITY, \

433 )) \

434 }; \

435 STRUCT\_SECTION\_ITERABLE(zbus\_observer, \_name) = { \

436 ZBUS\_OBSERVER\_NAME\_INIT(\_name) /\* Name field \*/ \

437 .type = ZBUS\_OBSERVER\_LISTENER\_TYPE, \

438 .data = &\_CONCAT(\_zbus\_obs\_data\_, \_name), \

439 .callback = (\_cb) \

440 }

441/\* clang-format on \*/

442

[ 453](group__zbus__apis.md#gabfc7be8298e76fe2f7ae628be30b8390)#define ZBUS\_LISTENER\_DEFINE(\_name, \_cb) ZBUS\_LISTENER\_DEFINE\_WITH\_ENABLE(\_name, \_cb, true)

454

455/\* clang-format off \*/

[ 466](group__zbus__apis.md#ga6089c1ae0dad91306f79d48a63b31785)#define ZBUS\_MSG\_SUBSCRIBER\_DEFINE\_WITH\_ENABLE(\_name, \_enable) \

467 static K\_FIFO\_DEFINE(\_zbus\_observer\_fifo\_##\_name); \

468 static struct zbus\_observer\_data \_CONCAT(\_zbus\_obs\_data\_, \_name) = { \

469 .enabled = \_enable, \

470 IF\_ENABLED(CONFIG\_ZBUS\_PRIORITY\_BOOST, ( \

471 .priority = ZBUS\_MIN\_THREAD\_PRIORITY, \

472 )) \

473 }; \

474 STRUCT\_SECTION\_ITERABLE(zbus\_observer, \_name) = { \

475 ZBUS\_OBSERVER\_NAME\_INIT(\_name) /\* Name field \*/ \

476 .type = ZBUS\_OBSERVER\_MSG\_SUBSCRIBER\_TYPE, \

477 .data = &\_CONCAT(\_zbus\_obs\_data\_, \_name), \

478 .message\_fifo = &\_zbus\_observer\_fifo\_##\_name, \

479 }

480/\* clang-format on \*/

481

[ 493](group__zbus__apis.md#ga07a0c2c428c9e4891e86a63a420b2268)#define ZBUS\_MSG\_SUBSCRIBER\_DEFINE(\_name) ZBUS\_MSG\_SUBSCRIBER\_DEFINE\_WITH\_ENABLE(\_name, true)

[ 515](group__zbus__apis.md#gadfcaba65b397c1d8c31836ef3cf61244)int [zbus\_chan\_pub](group__zbus__apis.md#gadfcaba65b397c1d8c31836ef3cf61244)(const struct [zbus\_channel](structzbus__channel.md) \*chan, const void \*msg, [k\_timeout\_t](structk__timeout__t.md) timeout);

516

[ 534](group__zbus__apis.md#ga8209721e0a295c84d112ba1a7171100e)int [zbus\_chan\_read](group__zbus__apis.md#ga8209721e0a295c84d112ba1a7171100e)(const struct [zbus\_channel](structzbus__channel.md) \*chan, void \*msg, [k\_timeout\_t](structk__timeout__t.md) timeout);

535

[ 557](group__zbus__apis.md#ga00bfb7db54594029f4d288bcf5b56b3a)int [zbus\_chan\_claim](group__zbus__apis.md#ga00bfb7db54594029f4d288bcf5b56b3a)(const struct [zbus\_channel](structzbus__channel.md) \*chan, [k\_timeout\_t](structk__timeout__t.md) timeout);

558

[ 573](group__zbus__apis.md#ga74747affb345e68ce1d564c349409e59)int [zbus\_chan\_finish](group__zbus__apis.md#ga74747affb345e68ce1d564c349409e59)(const struct [zbus\_channel](structzbus__channel.md) \*chan);

574

[ 593](group__zbus__apis.md#ga6ec2f463801499e23a011fa4e68aa3e7)int [zbus\_chan\_notify](group__zbus__apis.md#ga6ec2f463801499e23a011fa4e68aa3e7)(const struct [zbus\_channel](structzbus__channel.md) \*chan, [k\_timeout\_t](structk__timeout__t.md) timeout);

594

595#if defined(CONFIG\_ZBUS\_CHANNEL\_NAME) || defined(\_\_DOXYGEN\_\_)

596

[ 606](group__zbus__apis.md#ga05a220636fc6bb58b97805e558b76d73)static inline const char \*[zbus\_chan\_name](group__zbus__apis.md#ga05a220636fc6bb58b97805e558b76d73)(const struct [zbus\_channel](structzbus__channel.md) \*chan)

607{

608 \_\_ASSERT(chan != NULL, "chan is required");

609

610 return chan->[name](structzbus__channel.md#a9839e77746c53d24de69453aea53a233);

611}

612

613#endif

614

[ 627](group__zbus__apis.md#gaaf8b34113b7b993438bd42db64812572)static inline void \*[zbus\_chan\_msg](group__zbus__apis.md#gaaf8b34113b7b993438bd42db64812572)(const struct [zbus\_channel](structzbus__channel.md) \*chan)

628{

629 \_\_ASSERT(chan != NULL, "chan is required");

630

631 return chan->[message](structzbus__channel.md#a7e8bd8f6c080615a4c4d524101201f19);

632}

633

[ 648](group__zbus__apis.md#gafee07c355df9ac86b85e601196b56a10)static inline const void \*[zbus\_chan\_const\_msg](group__zbus__apis.md#gafee07c355df9ac86b85e601196b56a10)(const struct [zbus\_channel](structzbus__channel.md) \*chan)

649{

650 \_\_ASSERT(chan != NULL, "chan is required");

651

652 return chan->[message](structzbus__channel.md#a7e8bd8f6c080615a4c4d524101201f19);

653}

654

[ 664](group__zbus__apis.md#ga8895a18b282ca2fe7528b4e5cf48e025)static inline [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [zbus\_chan\_msg\_size](group__zbus__apis.md#ga8895a18b282ca2fe7528b4e5cf48e025)(const struct [zbus\_channel](structzbus__channel.md) \*chan)

665{

666 \_\_ASSERT(chan != NULL, "chan is required");

667

668 return chan->[message\_size](structzbus__channel.md#a508bf72f7b47ad8781b4e4ef3645d17a);

669}

670

[ 680](group__zbus__apis.md#gac0b0ed0356fca5a8b65a3332931a369a)static inline void \*[zbus\_chan\_user\_data](group__zbus__apis.md#gac0b0ed0356fca5a8b65a3332931a369a)(const struct [zbus\_channel](structzbus__channel.md) \*chan)

681{

682 \_\_ASSERT(chan != NULL, "chan is required");

683

684 return chan->[user\_data](structzbus__channel.md#ae629044f9b6da800db5a628fc6789dfb);

685}

686

687#if defined(CONFIG\_ZBUS\_RUNTIME\_OBSERVERS) || defined(\_\_DOXYGEN\_\_)

688

[ 705](group__zbus__apis.md#gaddd8ce480bc29ead4442e529915cfbf6)int [zbus\_chan\_add\_obs](group__zbus__apis.md#gaddd8ce480bc29ead4442e529915cfbf6)(const struct [zbus\_channel](structzbus__channel.md) \*chan, const struct [zbus\_observer](structzbus__observer.md) \*obs,

706 [k\_timeout\_t](structk__timeout__t.md) timeout);

707

[ 725](group__zbus__apis.md#gaee11d7472a3f87156b8ef1dcfbe897c4)int [zbus\_chan\_rm\_obs](group__zbus__apis.md#gaee11d7472a3f87156b8ef1dcfbe897c4)(const struct [zbus\_channel](structzbus__channel.md) \*chan, const struct [zbus\_observer](structzbus__observer.md) \*obs,

726 [k\_timeout\_t](structk__timeout__t.md) timeout);

727

729

730struct zbus\_observer\_node {

731 [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) node;

732 const struct [zbus\_observer](structzbus__observer.md) \*obs;

733};

734

736

737#endif /\* CONFIG\_ZBUS\_RUNTIME\_OBSERVERS \*/

738

[ 752](group__zbus__apis.md#ga6b44a887c82cbceff3136bbd9e0aa91c)int [zbus\_obs\_set\_enable](group__zbus__apis.md#ga6b44a887c82cbceff3136bbd9e0aa91c)(struct [zbus\_observer](structzbus__observer.md) \*obs, bool enabled);

753

[ 764](group__zbus__apis.md#ga9d1f5e1aecd8bd521d916944cece2b95)static inline int [zbus\_obs\_is\_enabled](group__zbus__apis.md#ga9d1f5e1aecd8bd521d916944cece2b95)(struct [zbus\_observer](structzbus__observer.md) \*obs, bool \*enable)

765{

766 \_ZBUS\_ASSERT(obs != NULL, "obs is required");

767 \_ZBUS\_ASSERT(enable != NULL, "enable is required");

768

769 \*enable = obs->[data](structzbus__observer.md#a76bbaaf17ce0c58bfa9f9b604cbb496d)->[enabled](structzbus__observer__data.md#ad16ca7a9e83f54afd75f6accf471eb91);

770

771 return 0;

772}

773

[ 788](group__zbus__apis.md#ga9513264f912f54b60c4341642f578e5a)int [zbus\_obs\_set\_chan\_notification\_mask](group__zbus__apis.md#ga9513264f912f54b60c4341642f578e5a)(const struct [zbus\_observer](structzbus__observer.md) \*obs,

789 const struct [zbus\_channel](structzbus__channel.md) \*chan, bool masked);

790

[ 803](group__zbus__apis.md#ga41ae9799a52c2a7954500b0a3c78d19f)int [zbus\_obs\_is\_chan\_notification\_masked](group__zbus__apis.md#ga41ae9799a52c2a7954500b0a3c78d19f)(const struct [zbus\_observer](structzbus__observer.md) \*obs,

804 const struct [zbus\_channel](structzbus__channel.md) \*chan, bool \*masked);

805

806#if defined(CONFIG\_ZBUS\_OBSERVER\_NAME) || defined(\_\_DOXYGEN\_\_)

807

[ 817](group__zbus__apis.md#ga5bb33ec5b914e6cbc87fa70bf763ad15)static inline const char \*[zbus\_obs\_name](group__zbus__apis.md#ga5bb33ec5b914e6cbc87fa70bf763ad15)(const struct [zbus\_observer](structzbus__observer.md) \*obs)

818{

819 \_\_ASSERT(obs != NULL, "obs is required");

820

821 return obs->[name](structzbus__observer.md#ab2ba28a935b528b2db90389071769fd5);

822}

823

824#endif

825

826#if defined(CONFIG\_ZBUS\_PRIORITY\_BOOST) || defined(\_\_DOXYGEN\_\_)

827

[ 837](group__zbus__apis.md#gabecf160e4d468d0275ad79e22fd0fb5b)int [zbus\_obs\_attach\_to\_thread](group__zbus__apis.md#gabecf160e4d468d0275ad79e22fd0fb5b)(const struct [zbus\_observer](structzbus__observer.md) \*obs);

838

[ 848](group__zbus__apis.md#ga493c125c31e44d5a222f0e9c6d01249e)int [zbus\_obs\_detach\_from\_thread](group__zbus__apis.md#ga493c125c31e44d5a222f0e9c6d01249e)(const struct [zbus\_observer](structzbus__observer.md) \*obs);

849

850#endif /\* CONFIG\_ZBUS\_PRIORITY\_BOOST \*/

851

[ 870](group__zbus__apis.md#ga84a65e276a01ef97eeb5c81b880da72b)int [zbus\_sub\_wait](group__zbus__apis.md#ga84a65e276a01ef97eeb5c81b880da72b)(const struct [zbus\_observer](structzbus__observer.md) \*sub, const struct [zbus\_channel](structzbus__channel.md) \*\*chan,

871 [k\_timeout\_t](structk__timeout__t.md) timeout);

872

873#if defined(CONFIG\_ZBUS\_MSG\_SUBSCRIBER) || defined(\_\_DOXYGEN\_\_)

874

[ 893](group__zbus__apis.md#gaeffce45446509e488192a4e6442453fb)int [zbus\_sub\_wait\_msg](group__zbus__apis.md#gaeffce45446509e488192a4e6442453fb)(const struct [zbus\_observer](structzbus__observer.md) \*sub, const struct [zbus\_channel](structzbus__channel.md) \*\*chan, void \*msg,

894 [k\_timeout\_t](structk__timeout__t.md) timeout);

895

896#endif /\* CONFIG\_ZBUS\_MSG\_SUBSCRIBER \*/

897

[ 911](group__zbus__apis.md#ga6dffd25f4eb368e773c2bd55f34a0e10)bool [zbus\_iterate\_over\_channels](group__zbus__apis.md#ga6dffd25f4eb368e773c2bd55f34a0e10)(bool (\*iterator\_func)(const struct [zbus\_channel](structzbus__channel.md) \*chan));

[ 926](group__zbus__apis.md#gab8df108b0238757ff631ec1e120fa2c3)bool [zbus\_iterate\_over\_channels\_with\_user\_data](group__zbus__apis.md#gab8df108b0238757ff631ec1e120fa2c3)(

927 bool (\*iterator\_func)(const struct [zbus\_channel](structzbus__channel.md) \*chan, void \*user\_data), void \*user\_data);

928

[ 942](group__zbus__apis.md#ga2fa50316993afc5807e9d707d664be14)bool [zbus\_iterate\_over\_observers](group__zbus__apis.md#ga2fa50316993afc5807e9d707d664be14)(bool (\*iterator\_func)(const struct [zbus\_observer](structzbus__observer.md) \*obs));

[ 957](group__zbus__apis.md#ga2f4e39c500fed0a6bcfedb5dec3f797a)bool [zbus\_iterate\_over\_observers\_with\_user\_data](group__zbus__apis.md#ga2f4e39c500fed0a6bcfedb5dec3f797a)(

958 bool (\*iterator\_func)(const struct [zbus\_observer](structzbus__observer.md) \*obs, void \*user\_data), void \*user\_data);

959

963

964#ifdef \_\_cplusplus

965}

966#endif

967

968#endif /\* ZEPHYR\_INCLUDE\_ZBUS\_H\_ \*/

[sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8)

struct \_slist sys\_slist\_t

Single-linked list structure.

**Definition** slist.h:49

[sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493)

struct \_snode sys\_snode\_t

Single-linked list node structure.

**Definition** slist.h:39

[zbus\_chan\_claim](group__zbus__apis.md#ga00bfb7db54594029f4d288bcf5b56b3a)

int zbus\_chan\_claim(const struct zbus\_channel \*chan, k\_timeout\_t timeout)

Claim a channel.

[zbus\_chan\_name](group__zbus__apis.md#ga05a220636fc6bb58b97805e558b76d73)

static const char \* zbus\_chan\_name(const struct zbus\_channel \*chan)

Get the channel's name.

**Definition** zbus.h:606

[zbus\_iterate\_over\_observers\_with\_user\_data](group__zbus__apis.md#ga2f4e39c500fed0a6bcfedb5dec3f797a)

bool zbus\_iterate\_over\_observers\_with\_user\_data(bool(\*iterator\_func)(const struct zbus\_observer \*obs, void \*user\_data), void \*user\_data)

Iterate over observers with user data.

[zbus\_iterate\_over\_observers](group__zbus__apis.md#ga2fa50316993afc5807e9d707d664be14)

bool zbus\_iterate\_over\_observers(bool(\*iterator\_func)(const struct zbus\_observer \*obs))

Iterate over observers.

[zbus\_obs\_is\_chan\_notification\_masked](group__zbus__apis.md#ga41ae9799a52c2a7954500b0a3c78d19f)

int zbus\_obs\_is\_chan\_notification\_masked(const struct zbus\_observer \*obs, const struct zbus\_channel \*chan, bool \*masked)

Get the notifications masking state from a channel to an observer.

[zbus\_obs\_detach\_from\_thread](group__zbus__apis.md#ga493c125c31e44d5a222f0e9c6d01249e)

int zbus\_obs\_detach\_from\_thread(const struct zbus\_observer \*obs)

Clear the observer thread priority by detaching it from a thread.

[zbus\_obs\_name](group__zbus__apis.md#ga5bb33ec5b914e6cbc87fa70bf763ad15)

static const char \* zbus\_obs\_name(const struct zbus\_observer \*obs)

Get the observer's name.

**Definition** zbus.h:817

[zbus\_obs\_set\_enable](group__zbus__apis.md#ga6b44a887c82cbceff3136bbd9e0aa91c)

int zbus\_obs\_set\_enable(struct zbus\_observer \*obs, bool enabled)

Change the observer state.

[zbus\_iterate\_over\_channels](group__zbus__apis.md#ga6dffd25f4eb368e773c2bd55f34a0e10)

bool zbus\_iterate\_over\_channels(bool(\*iterator\_func)(const struct zbus\_channel \*chan))

Iterate over channels.

[zbus\_chan\_notify](group__zbus__apis.md#ga6ec2f463801499e23a011fa4e68aa3e7)

int zbus\_chan\_notify(const struct zbus\_channel \*chan, k\_timeout\_t timeout)

Force a channel notification.

[zbus\_chan\_finish](group__zbus__apis.md#ga74747affb345e68ce1d564c349409e59)

int zbus\_chan\_finish(const struct zbus\_channel \*chan)

Finish a channel claim.

[zbus\_chan\_read](group__zbus__apis.md#ga8209721e0a295c84d112ba1a7171100e)

int zbus\_chan\_read(const struct zbus\_channel \*chan, void \*msg, k\_timeout\_t timeout)

Read a channel.

[zbus\_sub\_wait](group__zbus__apis.md#ga84a65e276a01ef97eeb5c81b880da72b)

int zbus\_sub\_wait(const struct zbus\_observer \*sub, const struct zbus\_channel \*\*chan, k\_timeout\_t timeout)

Wait for a channel notification.

[zbus\_observer\_type](group__zbus__apis.md#ga88941281d7bdd24f3cfbb53e57711d8f)

zbus\_observer\_type

Type used to represent an observer type.

**Definition** zbus.h:100

[zbus\_chan\_msg\_size](group__zbus__apis.md#ga8895a18b282ca2fe7528b4e5cf48e025)

static uint16\_t zbus\_chan\_msg\_size(const struct zbus\_channel \*chan)

Get the channel's message size.

**Definition** zbus.h:664

[zbus\_obs\_set\_chan\_notification\_mask](group__zbus__apis.md#ga9513264f912f54b60c4341642f578e5a)

int zbus\_obs\_set\_chan\_notification\_mask(const struct zbus\_observer \*obs, const struct zbus\_channel \*chan, bool masked)

Mask notifications from a channel to an observer.

[zbus\_obs\_is\_enabled](group__zbus__apis.md#ga9d1f5e1aecd8bd521d916944cece2b95)

static int zbus\_obs\_is\_enabled(struct zbus\_observer \*obs, bool \*enable)

Get the observer state.

**Definition** zbus.h:764

[zbus\_chan\_msg](group__zbus__apis.md#gaaf8b34113b7b993438bd42db64812572)

static void \* zbus\_chan\_msg(const struct zbus\_channel \*chan)

Get the reference for a channel message directly.

**Definition** zbus.h:627

[zbus\_iterate\_over\_channels\_with\_user\_data](group__zbus__apis.md#gab8df108b0238757ff631ec1e120fa2c3)

bool zbus\_iterate\_over\_channels\_with\_user\_data(bool(\*iterator\_func)(const struct zbus\_channel \*chan, void \*user\_data), void \*user\_data)

Iterate over channels with user data.

[zbus\_obs\_attach\_to\_thread](group__zbus__apis.md#gabecf160e4d468d0275ad79e22fd0fb5b)

int zbus\_obs\_attach\_to\_thread(const struct zbus\_observer \*obs)

Set the observer thread priority by attaching it to a thread.

[zbus\_chan\_user\_data](group__zbus__apis.md#gac0b0ed0356fca5a8b65a3332931a369a)

static void \* zbus\_chan\_user\_data(const struct zbus\_channel \*chan)

Get the channel's user data.

**Definition** zbus.h:680

[zbus\_chan\_add\_obs](group__zbus__apis.md#gaddd8ce480bc29ead4442e529915cfbf6)

int zbus\_chan\_add\_obs(const struct zbus\_channel \*chan, const struct zbus\_observer \*obs, k\_timeout\_t timeout)

Add an observer to a channel.

[zbus\_chan\_pub](group__zbus__apis.md#gadfcaba65b397c1d8c31836ef3cf61244)

int zbus\_chan\_pub(const struct zbus\_channel \*chan, const void \*msg, k\_timeout\_t timeout)

Publish to a channel.

[zbus\_chan\_rm\_obs](group__zbus__apis.md#gaee11d7472a3f87156b8ef1dcfbe897c4)

int zbus\_chan\_rm\_obs(const struct zbus\_channel \*chan, const struct zbus\_observer \*obs, k\_timeout\_t timeout)

Remove an observer from a channel.

[zbus\_sub\_wait\_msg](group__zbus__apis.md#gaeffce45446509e488192a4e6442453fb)

int zbus\_sub\_wait\_msg(const struct zbus\_observer \*sub, const struct zbus\_channel \*\*chan, void \*msg, k\_timeout\_t timeout)

Wait for a channel message.

[zbus\_chan\_const\_msg](group__zbus__apis.md#gafee07c355df9ac86b85e601196b56a10)

static const void \* zbus\_chan\_const\_msg(const struct zbus\_channel \*chan)

Get a constant reference for a channel message directly.

**Definition** zbus.h:648

[ZBUS\_OBSERVER\_LISTENER\_TYPE](group__zbus__apis.md#gga88941281d7bdd24f3cfbb53e57711d8fa127f19c2121c9c512da9dbcbb301320c)

@ ZBUS\_OBSERVER\_LISTENER\_TYPE

**Definition** zbus.h:101

[ZBUS\_OBSERVER\_SUBSCRIBER\_TYPE](group__zbus__apis.md#gga88941281d7bdd24f3cfbb53e57711d8fa22c784a85353545e8dca2ce7a0ec81b3)

@ ZBUS\_OBSERVER\_SUBSCRIBER\_TYPE

**Definition** zbus.h:102

[ZBUS\_OBSERVER\_MSG\_SUBSCRIBER\_TYPE](group__zbus__apis.md#gga88941281d7bdd24f3cfbb53e57711d8fa8151f9e58a5bd96449bd2f9f8695538c)

@ ZBUS\_OBSERVER\_MSG\_SUBSCRIBER\_TYPE

**Definition** zbus.h:103

[kernel.h](include_2zephyr_2kernel_8h.md)

Public kernel APIs.

[bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)

#define bool

**Definition** stdbool.h:13

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf)

\_\_INT16\_TYPE\_\_ int16\_t

**Definition** stdint.h:73

[string.h](string_8h.md)

[k\_fifo](structk__fifo.md)

**Definition** kernel.h:2374

[k\_msgq](structk__msgq.md)

Message Queue Structure.

**Definition** kernel.h:4402

[k\_timeout\_t](structk__timeout__t.md)

Kernel timeout type.

**Definition** sys\_clock.h:65

[zbus\_channel\_data](structzbus__channel__data.md)

Type used to represent a channel mutable data.

**Definition** zbus.h:30

[zbus\_channel\_data::observers\_end\_idx](structzbus__channel__data.md#a5b3c38f70cd99cc7e83f9b641997e1ed)

int16\_t observers\_end\_idx

Static channel observer list end index.

**Definition** zbus.h:39

[zbus\_channel\_data::observers\_start\_idx](structzbus__channel__data.md#a6329a0af467d83ad488f3310c1002c41)

int16\_t observers\_start\_idx

Static channel observer list start index.

**Definition** zbus.h:34

[zbus\_channel\_data::sem](structzbus__channel__data.md#a6fa71ae5dc260f5934f47383f53891a7)

struct k\_sem sem

Access control semaphore.

**Definition** zbus.h:44

[zbus\_channel\_data::observers](structzbus__channel__data.md#aeffcb35769775ee0927c3af9be77d1e1)

sys\_slist\_t observers

Channel observer list.

**Definition** zbus.h:57

[zbus\_channel](structzbus__channel.md)

Type used to represent a channel.

**Definition** zbus.h:67

[zbus\_channel::validator](structzbus__channel.md#a047e9da011488c8f11abdc1fd283f5f6)

bool(\*const validator)(const void \*msg, size\_t msg\_size)

Message validator.

**Definition** zbus.h:89

[zbus\_channel::data](structzbus__channel.md#a30ad5027b70d6e9d28d0b0caef3571fe)

struct zbus\_channel\_data \*const data

Mutable channel data struct.

**Definition** zbus.h:92

[zbus\_channel::message\_size](structzbus__channel.md#a508bf72f7b47ad8781b4e4ef3645d17a)

const size\_t message\_size

Message size.

**Definition** zbus.h:78

[zbus\_channel::message](structzbus__channel.md#a7e8bd8f6c080615a4c4d524101201f19)

void \*const message

Message reference.

**Definition** zbus.h:75

[zbus\_channel::name](structzbus__channel.md#a9839e77746c53d24de69453aea53a233)

const char \*const name

Channel name.

**Definition** zbus.h:70

[zbus\_channel::user\_data](structzbus__channel.md#ae629044f9b6da800db5a628fc6789dfb)

void \*const user\_data

User data available to extend zbus features.

**Definition** zbus.h:83

[zbus\_observer\_data](structzbus__observer__data.md)

**Definition** zbus.h:106

[zbus\_observer\_data::enabled](structzbus__observer__data.md#ad16ca7a9e83f54afd75f6accf471eb91)

bool enabled

Enabled flag.

**Definition** zbus.h:108

[zbus\_observer](structzbus__observer.md)

Type used to represent an observer.

**Definition** zbus.h:131

[zbus\_observer::type](structzbus__observer.md#a0251cf9bdca418b6b8123b998b57efe2)

enum zbus\_observer\_type type

Type indication.

**Definition** zbus.h:137

[zbus\_observer::callback](structzbus__observer.md#a71fe83641f3e8c6248602150cbd998a1)

void(\*const callback)(const struct zbus\_channel \*chan)

Observer callback function.

**Definition** zbus.h:147

[zbus\_observer::data](structzbus__observer.md#a76bbaaf17ce0c58bfa9f9b604cbb496d)

struct zbus\_observer\_data \*const data

Mutable observer data struct.

**Definition** zbus.h:140

[zbus\_observer::queue](structzbus__observer.md#a7da8da6038d3dad4bc4c05279c28310c)

struct k\_msgq \*const queue

Observer message queue.

**Definition** zbus.h:144

[zbus\_observer::message\_fifo](structzbus__observer.md#a9073bc59a4662385d6c5d487e7be03c9)

struct k\_fifo \*const message\_fifo

Observer message FIFO.

**Definition** zbus.h:153

[zbus\_observer::name](structzbus__observer.md#ab2ba28a935b528b2db90389071769fd5)

const char \*const name

Observer name.

**Definition** zbus.h:134

[iterable\_sections.h](sys_2iterable__sections_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [zbus](dir_4ac3b76b03f02d08133e5af61546c3d3.md)
- [zbus.h](zbus_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
