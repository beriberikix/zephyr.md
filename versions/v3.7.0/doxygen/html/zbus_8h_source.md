---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/zbus_8h_source.html
original_path: doxygen/html/zbus_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
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

11#include <[zephyr/kernel.h](kernel_8h.md)>

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

59

60#if defined(CONFIG\_ZBUS\_MSG\_SUBSCRIBER\_NET\_BUF\_POOL\_ISOLATION) || defined(\_\_DOXYGEN\_\_)

[ 63](structzbus__channel__data.md#a2490c05755696b7ba1f1f1392d27845f) struct [net\_buf\_pool](structnet__buf__pool.md) \*[msg\_subscriber\_pool](structzbus__channel__data.md#a2490c05755696b7ba1f1f1392d27845f);

64#endif /\* ZBUS\_MSG\_SUBSCRIBER\_NET\_BUF\_POOL\_ISOLATION \*/

65};

66

[ 73](structzbus__channel.md)struct [zbus\_channel](structzbus__channel.md) {

74#if defined(CONFIG\_ZBUS\_CHANNEL\_NAME) || defined(\_\_DOXYGEN\_\_)

[ 76](structzbus__channel.md#a9839e77746c53d24de69453aea53a233) const char \*const [name](structzbus__channel.md#a9839e77746c53d24de69453aea53a233);

77#endif

[ 81](structzbus__channel.md#a7e8bd8f6c080615a4c4d524101201f19) void \*const [message](structzbus__channel.md#a7e8bd8f6c080615a4c4d524101201f19);

82

[ 84](structzbus__channel.md#a508bf72f7b47ad8781b4e4ef3645d17a) const size\_t [message\_size](structzbus__channel.md#a508bf72f7b47ad8781b4e4ef3645d17a);

85

[ 89](structzbus__channel.md#ae629044f9b6da800db5a628fc6789dfb) void \*const [user\_data](structzbus__channel.md#ae629044f9b6da800db5a628fc6789dfb);

90

[ 95](structzbus__channel.md#a047e9da011488c8f11abdc1fd283f5f6) [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) (\*const [validator](structzbus__channel.md#a047e9da011488c8f11abdc1fd283f5f6))(const void \*msg, size\_t msg\_size);

96

[ 98](structzbus__channel.md#a30ad5027b70d6e9d28d0b0caef3571fe) struct [zbus\_channel\_data](structzbus__channel__data.md) \*const [data](structzbus__channel.md#a30ad5027b70d6e9d28d0b0caef3571fe);

99};

100

[ 106](group__zbus__apis.md#ga88941281d7bdd24f3cfbb53e57711d8f)enum \_\_packed [zbus\_observer\_type](group__zbus__apis.md#ga88941281d7bdd24f3cfbb53e57711d8f) {

[ 107](group__zbus__apis.md#gga88941281d7bdd24f3cfbb53e57711d8fa127f19c2121c9c512da9dbcbb301320c) [ZBUS\_OBSERVER\_LISTENER\_TYPE](group__zbus__apis.md#gga88941281d7bdd24f3cfbb53e57711d8fa127f19c2121c9c512da9dbcbb301320c),

[ 108](group__zbus__apis.md#gga88941281d7bdd24f3cfbb53e57711d8fa22c784a85353545e8dca2ce7a0ec81b3) [ZBUS\_OBSERVER\_SUBSCRIBER\_TYPE](group__zbus__apis.md#gga88941281d7bdd24f3cfbb53e57711d8fa22c784a85353545e8dca2ce7a0ec81b3),

[ 109](group__zbus__apis.md#gga88941281d7bdd24f3cfbb53e57711d8fa8151f9e58a5bd96449bd2f9f8695538c) [ZBUS\_OBSERVER\_MSG\_SUBSCRIBER\_TYPE](group__zbus__apis.md#gga88941281d7bdd24f3cfbb53e57711d8fa8151f9e58a5bd96449bd2f9f8695538c),

110};

111

[ 112](structzbus__observer__data.md)struct [zbus\_observer\_data](structzbus__observer__data.md) {

[ 114](structzbus__observer__data.md#ad16ca7a9e83f54afd75f6accf471eb91) bool [enabled](structzbus__observer__data.md#ad16ca7a9e83f54afd75f6accf471eb91);

115

116#if defined(CONFIG\_ZBUS\_PRIORITY\_BOOST)

118 int priority;

119#endif /\* CONFIG\_ZBUS\_PRIORITY\_BOOST \*/

120};

121

[ 137](structzbus__observer.md)struct [zbus\_observer](structzbus__observer.md) {

138#if defined(CONFIG\_ZBUS\_OBSERVER\_NAME) || defined(\_\_DOXYGEN\_\_)

[ 140](structzbus__observer.md#ab2ba28a935b528b2db90389071769fd5) const char \*const [name](structzbus__observer.md#ab2ba28a935b528b2db90389071769fd5);

141#endif

[ 143](structzbus__observer.md#a0251cf9bdca418b6b8123b998b57efe2) enum [zbus\_observer\_type](group__zbus__apis.md#ga88941281d7bdd24f3cfbb53e57711d8f) [type](structzbus__observer.md#a0251cf9bdca418b6b8123b998b57efe2);

144

[ 146](structzbus__observer.md#a76bbaaf17ce0c58bfa9f9b604cbb496d) struct [zbus\_observer\_data](structzbus__observer__data.md) \*const [data](structzbus__observer.md#a76bbaaf17ce0c58bfa9f9b604cbb496d);

147

148 union {

[ 150](structzbus__observer.md#a7da8da6038d3dad4bc4c05279c28310c) struct [k\_msgq](structk__msgq.md) \*const [queue](structzbus__observer.md#a7da8da6038d3dad4bc4c05279c28310c);

151

[ 153](structzbus__observer.md#a71fe83641f3e8c6248602150cbd998a1) void (\*const [callback](structzbus__observer.md#a71fe83641f3e8c6248602150cbd998a1))(const struct [zbus\_channel](structzbus__channel.md) \*chan);

154

155#if defined(CONFIG\_ZBUS\_MSG\_SUBSCRIBER) || defined(\_\_DOXYGEN\_\_)

[ 159](structzbus__observer.md#a9073bc59a4662385d6c5d487e7be03c9) struct [k\_fifo](structk__fifo.md) \*const [message\_fifo](structzbus__observer.md#a9073bc59a4662385d6c5d487e7be03c9);

160#endif /\* CONFIG\_ZBUS\_MSG\_SUBSCRIBER \*/

161 };

162};

163

165struct zbus\_channel\_observation\_mask {

166 bool enabled;

167};

168

169struct zbus\_channel\_observation {

170 const struct zbus\_channel \*const chan;

171 const struct zbus\_observer \*const obs;

172};

173

174#ifdef \_\_cplusplus

175#define \_ZBUS\_CPP\_EXTERN extern

176#else

177#define \_ZBUS\_CPP\_EXTERN

178#endif /\* \_\_cplusplus \*/

179

180#define ZBUS\_MIN\_THREAD\_PRIORITY (CONFIG\_NUM\_PREEMPT\_PRIORITIES - 1)

181

182#if defined(CONFIG\_ZBUS\_ASSERT\_MOCK)

183#define \_ZBUS\_ASSERT(\_cond, \_fmt, ...) \

184 do { \

185 if (!(\_cond)) { \

186 printk("ZBUS ASSERT: "); \

187 printk(\_fmt, ##\_\_VA\_ARGS\_\_); \

188 printk("\n"); \

189 return -EFAULT; \

190 } \

191 } while (0)

192#else

193#define \_ZBUS\_ASSERT(\_cond, \_fmt, ...) \_\_ASSERT(\_cond, \_fmt, ##\_\_VA\_ARGS\_\_)

194#endif

195

196#if defined(CONFIG\_ZBUS\_CHANNEL\_NAME)

197#define ZBUS\_CHANNEL\_NAME\_INIT(\_name) .name = #\_name,

198#define \_ZBUS\_CHAN\_NAME(\_chan) (\_chan)->name

199#else

200#define ZBUS\_CHANNEL\_NAME\_INIT(\_name)

201#define \_ZBUS\_CHAN\_NAME(\_chan) ""

202#endif

203

204#if defined(CONFIG\_ZBUS\_OBSERVER\_NAME)

205#define ZBUS\_OBSERVER\_NAME\_INIT(\_name) .name = #\_name,

206#define \_ZBUS\_OBS\_NAME(\_obs) (\_obs)->name

207#else

208#define ZBUS\_OBSERVER\_NAME\_INIT(\_name)

209#define \_ZBUS\_OBS\_NAME(\_obs) ""

210#endif

211

212#if defined(CONFIG\_ZBUS\_RUNTIME\_OBSERVERS)

213#define ZBUS\_RUNTIME\_OBSERVERS\_LIST\_DECL(\_slist\_name) static sys\_slist\_t \_slist\_name

214#define ZBUS\_RUNTIME\_OBSERVERS\_LIST\_INIT(\_slist\_name) .runtime\_observers = &\_slist\_name,

215#else

216#define ZBUS\_RUNTIME\_OBSERVERS\_LIST\_DECL(\_slist\_name)

217#define ZBUS\_RUNTIME\_OBSERVERS\_LIST\_INIT(\_slist\_name) /\* No runtime observers \*/

218#endif

219

220#define \_ZBUS\_OBS\_EXTERN(\_name) extern struct zbus\_observer \_name

221

222#define \_ZBUS\_CHAN\_EXTERN(\_name) extern const struct zbus\_channel \_name

223

224#define ZBUS\_REF(\_value) &(\_value)

225

226#define FOR\_EACH\_FIXED\_ARG\_NONEMPTY\_TERM(F, sep, fixed\_arg, ...) \

227 COND\_CODE\_0(/\* are there zero non-empty arguments ? \*/ \

228 NUM\_VA\_ARGS\_LESS\_1( \

229 LIST\_DROP\_EMPTY(\_\_VA\_ARGS\_\_, \_)), /\* if so, expand to nothing \*/ \

230 (), /\* otherwise, expand to: \*/ \

231 (FOR\_EACH\_IDX\_FIXED\_ARG( \

232 F, sep, fixed\_arg, \

233 LIST\_DROP\_EMPTY(\_\_VA\_ARGS\_\_)) /\* plus a final terminator \*/ \

234 \_\_DEBRACKET sep))

235

236#define \_ZBUS\_OBSERVATION\_PREFIX(\_idx) \

237 GET\_ARG\_N(\_idx, 00, 01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 11, 12, 13, 14, 15, 16, 17, \

238 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, \

239 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, \

240 58, 59, 60, 61, 62, 63)

241

242#define \_ZBUS\_CHAN\_OBSERVATION(\_idx, \_obs, \_chan) \

243 const STRUCT\_SECTION\_ITERABLE( \

244 zbus\_channel\_observation, \

245 \_CONCAT(\_chan, \_ZBUS\_OBSERVATION\_PREFIX(UTIL\_INC(\_idx)))) = {.chan = &\_chan, \

246 .obs = &\_obs}; \

247 STRUCT\_SECTION\_ITERABLE(zbus\_channel\_observation\_mask, \

248 \_CONCAT(\_CONCAT(\_chan, \_ZBUS\_OBSERVATION\_PREFIX(UTIL\_INC(\_idx))), \

249 \_mask)) = {.enabled = false};

250

251#if defined(CONFIG\_ZBUS\_RUNTIME\_OBSERVERS) || defined(\_\_DOXYGEN\_\_)

252#define \_ZBUS\_RUNTIME\_OBSERVERS(\_name) .observers = &(\_CONCAT(\_observers\_, \_name)),

253#define \_ZBUS\_RUNTIME\_OBSERVERS\_DECL(\_name) static sys\_slist\_t \_CONCAT(\_observers\_, \_name);

254#else

255#define \_ZBUS\_RUNTIME\_OBSERVERS(\_name)

256#define \_ZBUS\_RUNTIME\_OBSERVERS\_DECL(\_name)

257#endif /\* CONFIG\_ZBUS\_RUNTIME\_OBSERVERS \*/

258

260

261/\* clang-format off \*/

[ 273](group__zbus__apis.md#ga7f763caca474e6c910793d2c714f80b4)#define ZBUS\_CHAN\_ADD\_OBS\_WITH\_MASK(\_chan, \_obs, \_masked, \_prio) \

274 const STRUCT\_SECTION\_ITERABLE(zbus\_channel\_observation, \

275 \_CONCAT(\_CONCAT(\_chan, zz), \_CONCAT(\_prio, \_obs))) = { \

276 .chan = &\_chan, \

277 .obs = &\_obs, \

278 }; \

279 STRUCT\_SECTION\_ITERABLE(zbus\_channel\_observation\_mask, \

280 \_CONCAT(\_CONCAT(\_CONCAT(\_chan, zz), \_CONCAT(\_prio, \_obs)), \

281 \_mask)) = {.enabled = \_masked}

282/\* clang-format on \*/

283

[ 294](group__zbus__apis.md#gaf63215f3f53741edf52b4d0d7b2b97df)#define ZBUS\_CHAN\_ADD\_OBS(\_chan, \_obs, \_prio) ZBUS\_CHAN\_ADD\_OBS\_WITH\_MASK(\_chan, \_obs, false, \_prio)

295

[ 301](group__zbus__apis.md#ga49f169c6d50a3bad57e1b319362d2924)#define ZBUS\_OBS\_DECLARE(...) FOR\_EACH\_NONEMPTY\_TERM(\_ZBUS\_OBS\_EXTERN, (;), \_\_VA\_ARGS\_\_)

302

[ 308](group__zbus__apis.md#ga0662b2db8077a8075c07a3afd0161d0f)#define ZBUS\_CHAN\_DECLARE(...) FOR\_EACH(\_ZBUS\_CHAN\_EXTERN, (;), \_\_VA\_ARGS\_\_)

309

[ 314](group__zbus__apis.md#ga763dad07a1ae9bb38f9c240e1920caef)#define ZBUS\_OBSERVERS\_EMPTY

315

[ 321](group__zbus__apis.md#gafed25f045c3b8d438daf4ebd5e517692)#define ZBUS\_OBSERVERS(...) \_\_VA\_ARGS\_\_

322

323/\* clang-format off \*/

[ 339](group__zbus__apis.md#ga29a3a39e5c78a34b2d8491615d1f0687)#define ZBUS\_CHAN\_DEFINE(\_name, \_type, \_validator, \_user\_data, \_observers, \_init\_val) \

340 static \_type \_CONCAT(\_zbus\_message\_, \_name) = \_init\_val; \

341 static struct zbus\_channel\_data \_CONCAT(\_zbus\_chan\_data\_, \_name) = { \

342 .observers\_start\_idx = -1, \

343 .observers\_end\_idx = -1, \

344 .sem = Z\_SEM\_INITIALIZER(\_CONCAT(\_zbus\_chan\_data\_, \_name).sem, 1, 1), \

345 IF\_ENABLED(CONFIG\_ZBUS\_RUNTIME\_OBSERVERS, ( \

346 .observers = SYS\_SLIST\_STATIC\_INIT( \

347 &\_CONCAT(\_zbus\_chan\_data\_, \_name).observers), \

348 )) \

349 IF\_ENABLED(CONFIG\_ZBUS\_PRIORITY\_BOOST, ( \

350 .highest\_observer\_priority = ZBUS\_MIN\_THREAD\_PRIORITY, \

351 )) \

352 }; \

353 static K\_MUTEX\_DEFINE(\_CONCAT(\_zbus\_mutex\_, \_name)); \

354 \_ZBUS\_CPP\_EXTERN const STRUCT\_SECTION\_ITERABLE(zbus\_channel, \_name) = { \

355 ZBUS\_CHANNEL\_NAME\_INIT(\_name) /\* Maybe removed \*/ \

356 .message = &\_CONCAT(\_zbus\_message\_, \_name), \

357 .message\_size = sizeof(\_type), \

358 .user\_data = \_user\_data, \

359 .validator = \_validator, \

360 .data = &\_CONCAT(\_zbus\_chan\_data\_, \_name), \

361 IF\_ENABLED(ZBUS\_MSG\_SUBSCRIBER\_NET\_BUF\_POOL\_ISOLATION, ( \

362 .msg\_subscriber\_pool = &\_zbus\_msg\_subscribers\_pool, \

363 )) \

364 }; \

365 /\* Extern declaration of observers \*/ \

366 ZBUS\_OBS\_DECLARE(\_observers); \

367 /\* Create all channel observations from observers list \*/ \

368 FOR\_EACH\_FIXED\_ARG\_NONEMPTY\_TERM(\_ZBUS\_CHAN\_OBSERVATION, (;), \_name, \_observers)

369/\* clang-format on \*/

370

[ 380](group__zbus__apis.md#ga4bf8c445814c1fcee9b9819a36bc9bd6)#define ZBUS\_MSG\_INIT(\_val, ...) \

381 { \

382 \_val, ##\_\_VA\_ARGS\_\_ \

383 }

384

385/\* clang-format off \*/

[ 397](group__zbus__apis.md#gaf56f71babe2bb27258f025332b80c58f)#define ZBUS\_SUBSCRIBER\_DEFINE\_WITH\_ENABLE(\_name, \_queue\_size, \_enable) \

398 K\_MSGQ\_DEFINE(\_zbus\_observer\_queue\_##\_name, \

399 sizeof(const struct zbus\_channel \*), \

400 \_queue\_size, sizeof(const struct zbus\_channel \*) \

401 ); \

402 static struct zbus\_observer\_data \_CONCAT(\_zbus\_obs\_data\_, \_name) = { \

403 .enabled = \_enable, \

404 IF\_ENABLED(CONFIG\_ZBUS\_PRIORITY\_BOOST, ( \

405 .priority = ZBUS\_MIN\_THREAD\_PRIORITY, \

406 )) \

407 }; \

408 STRUCT\_SECTION\_ITERABLE(zbus\_observer, \_name) = { \

409 ZBUS\_OBSERVER\_NAME\_INIT(\_name) /\* Name field \*/ \

410 .type = ZBUS\_OBSERVER\_SUBSCRIBER\_TYPE, \

411 .data = &\_CONCAT(\_zbus\_obs\_data\_, \_name), \

412 .queue = &\_zbus\_observer\_queue\_##\_name, \

413 }

414/\* clang-format on \*/

415

[ 427](group__zbus__apis.md#gac17a735cccecfc90f26127e48cf6279a)#define ZBUS\_SUBSCRIBER\_DEFINE(\_name, \_queue\_size) \

428 ZBUS\_SUBSCRIBER\_DEFINE\_WITH\_ENABLE(\_name, \_queue\_size, true)

429

430/\* clang-format off \*/

[ 442](group__zbus__apis.md#gace4ac9da0e1bab7ba72797783ded948f)#define ZBUS\_LISTENER\_DEFINE\_WITH\_ENABLE(\_name, \_cb, \_enable) \

443 static struct zbus\_observer\_data \_CONCAT(\_zbus\_obs\_data\_, \_name) = { \

444 .enabled = \_enable, \

445 IF\_ENABLED(CONFIG\_ZBUS\_PRIORITY\_BOOST, ( \

446 .priority = ZBUS\_MIN\_THREAD\_PRIORITY, \

447 )) \

448 }; \

449 STRUCT\_SECTION\_ITERABLE(zbus\_observer, \_name) = { \

450 ZBUS\_OBSERVER\_NAME\_INIT(\_name) /\* Name field \*/ \

451 .type = ZBUS\_OBSERVER\_LISTENER\_TYPE, \

452 .data = &\_CONCAT(\_zbus\_obs\_data\_, \_name), \

453 .callback = (\_cb) \

454 }

455/\* clang-format on \*/

456

[ 467](group__zbus__apis.md#gabfc7be8298e76fe2f7ae628be30b8390)#define ZBUS\_LISTENER\_DEFINE(\_name, \_cb) ZBUS\_LISTENER\_DEFINE\_WITH\_ENABLE(\_name, \_cb, true)

468

469/\* clang-format off \*/

[ 480](group__zbus__apis.md#ga6089c1ae0dad91306f79d48a63b31785)#define ZBUS\_MSG\_SUBSCRIBER\_DEFINE\_WITH\_ENABLE(\_name, \_enable) \

481 static K\_FIFO\_DEFINE(\_zbus\_observer\_fifo\_##\_name); \

482 static struct zbus\_observer\_data \_CONCAT(\_zbus\_obs\_data\_, \_name) = { \

483 .enabled = \_enable, \

484 IF\_ENABLED(CONFIG\_ZBUS\_PRIORITY\_BOOST, ( \

485 .priority = ZBUS\_MIN\_THREAD\_PRIORITY, \

486 )) \

487 }; \

488 STRUCT\_SECTION\_ITERABLE(zbus\_observer, \_name) = { \

489 ZBUS\_OBSERVER\_NAME\_INIT(\_name) /\* Name field \*/ \

490 .type = ZBUS\_OBSERVER\_MSG\_SUBSCRIBER\_TYPE, \

491 .data = &\_CONCAT(\_zbus\_obs\_data\_, \_name), \

492 .message\_fifo = &\_zbus\_observer\_fifo\_##\_name, \

493 }

494/\* clang-format on \*/

495

[ 507](group__zbus__apis.md#ga07a0c2c428c9e4891e86a63a420b2268)#define ZBUS\_MSG\_SUBSCRIBER\_DEFINE(\_name) ZBUS\_MSG\_SUBSCRIBER\_DEFINE\_WITH\_ENABLE(\_name, true)

[ 529](group__zbus__apis.md#gadfcaba65b397c1d8c31836ef3cf61244)int [zbus\_chan\_pub](group__zbus__apis.md#gadfcaba65b397c1d8c31836ef3cf61244)(const struct [zbus\_channel](structzbus__channel.md) \*chan, const void \*msg, [k\_timeout\_t](structk__timeout__t.md) timeout);

530

[ 548](group__zbus__apis.md#ga8209721e0a295c84d112ba1a7171100e)int [zbus\_chan\_read](group__zbus__apis.md#ga8209721e0a295c84d112ba1a7171100e)(const struct [zbus\_channel](structzbus__channel.md) \*chan, void \*msg, [k\_timeout\_t](structk__timeout__t.md) timeout);

549

[ 571](group__zbus__apis.md#ga00bfb7db54594029f4d288bcf5b56b3a)int [zbus\_chan\_claim](group__zbus__apis.md#ga00bfb7db54594029f4d288bcf5b56b3a)(const struct [zbus\_channel](structzbus__channel.md) \*chan, [k\_timeout\_t](structk__timeout__t.md) timeout);

572

[ 587](group__zbus__apis.md#ga74747affb345e68ce1d564c349409e59)int [zbus\_chan\_finish](group__zbus__apis.md#ga74747affb345e68ce1d564c349409e59)(const struct [zbus\_channel](structzbus__channel.md) \*chan);

588

[ 607](group__zbus__apis.md#ga6ec2f463801499e23a011fa4e68aa3e7)int [zbus\_chan\_notify](group__zbus__apis.md#ga6ec2f463801499e23a011fa4e68aa3e7)(const struct [zbus\_channel](structzbus__channel.md) \*chan, [k\_timeout\_t](structk__timeout__t.md) timeout);

608

609#if defined(CONFIG\_ZBUS\_CHANNEL\_NAME) || defined(\_\_DOXYGEN\_\_)

610

[ 620](group__zbus__apis.md#ga05a220636fc6bb58b97805e558b76d73)static inline const char \*[zbus\_chan\_name](group__zbus__apis.md#ga05a220636fc6bb58b97805e558b76d73)(const struct [zbus\_channel](structzbus__channel.md) \*chan)

621{

622 \_\_ASSERT(chan != NULL, "chan is required");

623

624 return chan->[name](structzbus__channel.md#a9839e77746c53d24de69453aea53a233);

625}

626

627#endif

628

[ 641](group__zbus__apis.md#gaaf8b34113b7b993438bd42db64812572)static inline void \*[zbus\_chan\_msg](group__zbus__apis.md#gaaf8b34113b7b993438bd42db64812572)(const struct [zbus\_channel](structzbus__channel.md) \*chan)

642{

643 \_\_ASSERT(chan != NULL, "chan is required");

644

645 return chan->[message](structzbus__channel.md#a7e8bd8f6c080615a4c4d524101201f19);

646}

647

[ 662](group__zbus__apis.md#gafee07c355df9ac86b85e601196b56a10)static inline const void \*[zbus\_chan\_const\_msg](group__zbus__apis.md#gafee07c355df9ac86b85e601196b56a10)(const struct [zbus\_channel](structzbus__channel.md) \*chan)

663{

664 \_\_ASSERT(chan != NULL, "chan is required");

665

666 return chan->[message](structzbus__channel.md#a7e8bd8f6c080615a4c4d524101201f19);

667}

668

[ 678](group__zbus__apis.md#ga8895a18b282ca2fe7528b4e5cf48e025)static inline [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [zbus\_chan\_msg\_size](group__zbus__apis.md#ga8895a18b282ca2fe7528b4e5cf48e025)(const struct [zbus\_channel](structzbus__channel.md) \*chan)

679{

680 \_\_ASSERT(chan != NULL, "chan is required");

681

682 return chan->[message\_size](structzbus__channel.md#a508bf72f7b47ad8781b4e4ef3645d17a);

683}

684

[ 694](group__zbus__apis.md#gac0b0ed0356fca5a8b65a3332931a369a)static inline void \*[zbus\_chan\_user\_data](group__zbus__apis.md#gac0b0ed0356fca5a8b65a3332931a369a)(const struct [zbus\_channel](structzbus__channel.md) \*chan)

695{

696 \_\_ASSERT(chan != NULL, "chan is required");

697

698 return chan->[user\_data](structzbus__channel.md#ae629044f9b6da800db5a628fc6789dfb);

699}

700

701#if defined(CONFIG\_ZBUS\_MSG\_SUBSCRIBER\_NET\_BUF\_POOL\_ISOLATION) || defined(\_\_DOXYGEN\_\_)

702

[ 709](group__zbus__apis.md#ga3f90d50f20e7779ef257676ac10da357)static inline void [zbus\_chan\_set\_msg\_sub\_pool](group__zbus__apis.md#ga3f90d50f20e7779ef257676ac10da357)(const struct [zbus\_channel](structzbus__channel.md) \*chan,

710 struct [net\_buf\_pool](structnet__buf__pool.md) \*pool)

711{

712 \_\_ASSERT(chan != NULL, "chan is required");

713 \_\_ASSERT(pool != NULL, "pool is required");

714

715 chan->[data](structzbus__channel.md#a30ad5027b70d6e9d28d0b0caef3571fe)->[msg\_subscriber\_pool](structzbus__channel__data.md#a2490c05755696b7ba1f1f1392d27845f) = pool;

716}

717

718#endif /\* ZBUS\_MSG\_SUBSCRIBER\_NET\_BUF\_POOL\_ISOLATION \*/

719

720#if defined(CONFIG\_ZBUS\_RUNTIME\_OBSERVERS) || defined(\_\_DOXYGEN\_\_)

721

[ 738](group__zbus__apis.md#gaddd8ce480bc29ead4442e529915cfbf6)int [zbus\_chan\_add\_obs](group__zbus__apis.md#gaddd8ce480bc29ead4442e529915cfbf6)(const struct [zbus\_channel](structzbus__channel.md) \*chan, const struct [zbus\_observer](structzbus__observer.md) \*obs,

739 [k\_timeout\_t](structk__timeout__t.md) timeout);

740

[ 758](group__zbus__apis.md#gaee11d7472a3f87156b8ef1dcfbe897c4)int [zbus\_chan\_rm\_obs](group__zbus__apis.md#gaee11d7472a3f87156b8ef1dcfbe897c4)(const struct [zbus\_channel](structzbus__channel.md) \*chan, const struct [zbus\_observer](structzbus__observer.md) \*obs,

759 [k\_timeout\_t](structk__timeout__t.md) timeout);

760

762

763struct zbus\_observer\_node {

764 [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) node;

765 const struct [zbus\_observer](structzbus__observer.md) \*obs;

766};

767

769

770#endif /\* CONFIG\_ZBUS\_RUNTIME\_OBSERVERS \*/

771

[ 785](group__zbus__apis.md#ga6b44a887c82cbceff3136bbd9e0aa91c)int [zbus\_obs\_set\_enable](group__zbus__apis.md#ga6b44a887c82cbceff3136bbd9e0aa91c)(struct [zbus\_observer](structzbus__observer.md) \*obs, bool enabled);

786

[ 797](group__zbus__apis.md#ga9d1f5e1aecd8bd521d916944cece2b95)static inline int [zbus\_obs\_is\_enabled](group__zbus__apis.md#ga9d1f5e1aecd8bd521d916944cece2b95)(struct [zbus\_observer](structzbus__observer.md) \*obs, bool \*enable)

798{

799 \_ZBUS\_ASSERT(obs != NULL, "obs is required");

800 \_ZBUS\_ASSERT(enable != NULL, "enable is required");

801

802 \*enable = obs->[data](structzbus__observer.md#a76bbaaf17ce0c58bfa9f9b604cbb496d)->[enabled](structzbus__observer__data.md#ad16ca7a9e83f54afd75f6accf471eb91);

803

804 return 0;

805}

806

[ 821](group__zbus__apis.md#ga9513264f912f54b60c4341642f578e5a)int [zbus\_obs\_set\_chan\_notification\_mask](group__zbus__apis.md#ga9513264f912f54b60c4341642f578e5a)(const struct [zbus\_observer](structzbus__observer.md) \*obs,

822 const struct [zbus\_channel](structzbus__channel.md) \*chan, bool masked);

823

[ 836](group__zbus__apis.md#ga41ae9799a52c2a7954500b0a3c78d19f)int [zbus\_obs\_is\_chan\_notification\_masked](group__zbus__apis.md#ga41ae9799a52c2a7954500b0a3c78d19f)(const struct [zbus\_observer](structzbus__observer.md) \*obs,

837 const struct [zbus\_channel](structzbus__channel.md) \*chan, bool \*masked);

838

839#if defined(CONFIG\_ZBUS\_OBSERVER\_NAME) || defined(\_\_DOXYGEN\_\_)

840

[ 850](group__zbus__apis.md#ga5bb33ec5b914e6cbc87fa70bf763ad15)static inline const char \*[zbus\_obs\_name](group__zbus__apis.md#ga5bb33ec5b914e6cbc87fa70bf763ad15)(const struct [zbus\_observer](structzbus__observer.md) \*obs)

851{

852 \_\_ASSERT(obs != NULL, "obs is required");

853

854 return obs->[name](structzbus__observer.md#ab2ba28a935b528b2db90389071769fd5);

855}

856

857#endif

858

859#if defined(CONFIG\_ZBUS\_PRIORITY\_BOOST) || defined(\_\_DOXYGEN\_\_)

860

[ 870](group__zbus__apis.md#gabecf160e4d468d0275ad79e22fd0fb5b)int [zbus\_obs\_attach\_to\_thread](group__zbus__apis.md#gabecf160e4d468d0275ad79e22fd0fb5b)(const struct [zbus\_observer](structzbus__observer.md) \*obs);

871

[ 881](group__zbus__apis.md#ga493c125c31e44d5a222f0e9c6d01249e)int [zbus\_obs\_detach\_from\_thread](group__zbus__apis.md#ga493c125c31e44d5a222f0e9c6d01249e)(const struct [zbus\_observer](structzbus__observer.md) \*obs);

882

883#endif /\* CONFIG\_ZBUS\_PRIORITY\_BOOST \*/

884

[ 903](group__zbus__apis.md#ga84a65e276a01ef97eeb5c81b880da72b)int [zbus\_sub\_wait](group__zbus__apis.md#ga84a65e276a01ef97eeb5c81b880da72b)(const struct [zbus\_observer](structzbus__observer.md) \*sub, const struct [zbus\_channel](structzbus__channel.md) \*\*chan,

904 [k\_timeout\_t](structk__timeout__t.md) timeout);

905

906#if defined(CONFIG\_ZBUS\_MSG\_SUBSCRIBER) || defined(\_\_DOXYGEN\_\_)

907

[ 926](group__zbus__apis.md#gaeffce45446509e488192a4e6442453fb)int [zbus\_sub\_wait\_msg](group__zbus__apis.md#gaeffce45446509e488192a4e6442453fb)(const struct [zbus\_observer](structzbus__observer.md) \*sub, const struct [zbus\_channel](structzbus__channel.md) \*\*chan, void \*msg,

927 [k\_timeout\_t](structk__timeout__t.md) timeout);

928

929#endif /\* CONFIG\_ZBUS\_MSG\_SUBSCRIBER \*/

930

[ 944](group__zbus__apis.md#ga6dffd25f4eb368e773c2bd55f34a0e10)bool [zbus\_iterate\_over\_channels](group__zbus__apis.md#ga6dffd25f4eb368e773c2bd55f34a0e10)(bool (\*iterator\_func)(const struct [zbus\_channel](structzbus__channel.md) \*chan));

[ 959](group__zbus__apis.md#gab8df108b0238757ff631ec1e120fa2c3)bool [zbus\_iterate\_over\_channels\_with\_user\_data](group__zbus__apis.md#gab8df108b0238757ff631ec1e120fa2c3)(

960 bool (\*iterator\_func)(const struct [zbus\_channel](structzbus__channel.md) \*chan, void \*user\_data), void \*user\_data);

961

[ 975](group__zbus__apis.md#ga2fa50316993afc5807e9d707d664be14)bool [zbus\_iterate\_over\_observers](group__zbus__apis.md#ga2fa50316993afc5807e9d707d664be14)(bool (\*iterator\_func)(const struct [zbus\_observer](structzbus__observer.md) \*obs));

[ 990](group__zbus__apis.md#ga2f4e39c500fed0a6bcfedb5dec3f797a)bool [zbus\_iterate\_over\_observers\_with\_user\_data](group__zbus__apis.md#ga2f4e39c500fed0a6bcfedb5dec3f797a)(

991 bool (\*iterator\_func)(const struct [zbus\_observer](structzbus__observer.md) \*obs, void \*user\_data), void \*user\_data);

992

996

997#ifdef \_\_cplusplus

998}

999#endif

1000

1001#endif /\* ZEPHYR\_INCLUDE\_ZBUS\_H\_ \*/

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

**Definition** zbus.h:620

[zbus\_iterate\_over\_observers\_with\_user\_data](group__zbus__apis.md#ga2f4e39c500fed0a6bcfedb5dec3f797a)

bool zbus\_iterate\_over\_observers\_with\_user\_data(bool(\*iterator\_func)(const struct zbus\_observer \*obs, void \*user\_data), void \*user\_data)

Iterate over observers with user data.

[zbus\_iterate\_over\_observers](group__zbus__apis.md#ga2fa50316993afc5807e9d707d664be14)

bool zbus\_iterate\_over\_observers(bool(\*iterator\_func)(const struct zbus\_observer \*obs))

Iterate over observers.

[zbus\_chan\_set\_msg\_sub\_pool](group__zbus__apis.md#ga3f90d50f20e7779ef257676ac10da357)

static void zbus\_chan\_set\_msg\_sub\_pool(const struct zbus\_channel \*chan, struct net\_buf\_pool \*pool)

Set the channel's msg subscriber net\_buf pool.

**Definition** zbus.h:709

[zbus\_obs\_is\_chan\_notification\_masked](group__zbus__apis.md#ga41ae9799a52c2a7954500b0a3c78d19f)

int zbus\_obs\_is\_chan\_notification\_masked(const struct zbus\_observer \*obs, const struct zbus\_channel \*chan, bool \*masked)

Get the notifications masking state from a channel to an observer.

[zbus\_obs\_detach\_from\_thread](group__zbus__apis.md#ga493c125c31e44d5a222f0e9c6d01249e)

int zbus\_obs\_detach\_from\_thread(const struct zbus\_observer \*obs)

Clear the observer thread priority by detaching it from a thread.

[zbus\_obs\_name](group__zbus__apis.md#ga5bb33ec5b914e6cbc87fa70bf763ad15)

static const char \* zbus\_obs\_name(const struct zbus\_observer \*obs)

Get the observer's name.

**Definition** zbus.h:850

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

**Definition** zbus.h:106

[zbus\_chan\_msg\_size](group__zbus__apis.md#ga8895a18b282ca2fe7528b4e5cf48e025)

static uint16\_t zbus\_chan\_msg\_size(const struct zbus\_channel \*chan)

Get the channel's message size.

**Definition** zbus.h:678

[zbus\_obs\_set\_chan\_notification\_mask](group__zbus__apis.md#ga9513264f912f54b60c4341642f578e5a)

int zbus\_obs\_set\_chan\_notification\_mask(const struct zbus\_observer \*obs, const struct zbus\_channel \*chan, bool masked)

Mask notifications from a channel to an observer.

[zbus\_obs\_is\_enabled](group__zbus__apis.md#ga9d1f5e1aecd8bd521d916944cece2b95)

static int zbus\_obs\_is\_enabled(struct zbus\_observer \*obs, bool \*enable)

Get the observer state.

**Definition** zbus.h:797

[zbus\_chan\_msg](group__zbus__apis.md#gaaf8b34113b7b993438bd42db64812572)

static void \* zbus\_chan\_msg(const struct zbus\_channel \*chan)

Get the reference for a channel message directly.

**Definition** zbus.h:641

[zbus\_iterate\_over\_channels\_with\_user\_data](group__zbus__apis.md#gab8df108b0238757ff631ec1e120fa2c3)

bool zbus\_iterate\_over\_channels\_with\_user\_data(bool(\*iterator\_func)(const struct zbus\_channel \*chan, void \*user\_data), void \*user\_data)

Iterate over channels with user data.

[zbus\_obs\_attach\_to\_thread](group__zbus__apis.md#gabecf160e4d468d0275ad79e22fd0fb5b)

int zbus\_obs\_attach\_to\_thread(const struct zbus\_observer \*obs)

Set the observer thread priority by attaching it to a thread.

[zbus\_chan\_user\_data](group__zbus__apis.md#gac0b0ed0356fca5a8b65a3332931a369a)

static void \* zbus\_chan\_user\_data(const struct zbus\_channel \*chan)

Get the channel's user data.

**Definition** zbus.h:694

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

**Definition** zbus.h:662

[ZBUS\_OBSERVER\_LISTENER\_TYPE](group__zbus__apis.md#gga88941281d7bdd24f3cfbb53e57711d8fa127f19c2121c9c512da9dbcbb301320c)

@ ZBUS\_OBSERVER\_LISTENER\_TYPE

**Definition** zbus.h:107

[ZBUS\_OBSERVER\_SUBSCRIBER\_TYPE](group__zbus__apis.md#gga88941281d7bdd24f3cfbb53e57711d8fa22c784a85353545e8dca2ce7a0ec81b3)

@ ZBUS\_OBSERVER\_SUBSCRIBER\_TYPE

**Definition** zbus.h:108

[ZBUS\_OBSERVER\_MSG\_SUBSCRIBER\_TYPE](group__zbus__apis.md#gga88941281d7bdd24f3cfbb53e57711d8fa8151f9e58a5bd96449bd2f9f8695538c)

@ ZBUS\_OBSERVER\_MSG\_SUBSCRIBER\_TYPE

**Definition** zbus.h:109

[kernel.h](kernel_8h.md)

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

**Definition** kernel.h:2391

[k\_msgq](structk__msgq.md)

Message Queue Structure.

**Definition** kernel.h:4426

[k\_timeout\_t](structk__timeout__t.md)

Kernel timeout type.

**Definition** sys\_clock.h:65

[net\_buf\_pool](structnet__buf__pool.md)

Network buffer pool representation.

**Definition** buf.h:1076

[zbus\_channel\_data](structzbus__channel__data.md)

Type used to represent a channel mutable data.

**Definition** zbus.h:30

[zbus\_channel\_data::msg\_subscriber\_pool](structzbus__channel__data.md#a2490c05755696b7ba1f1f1392d27845f)

struct net\_buf\_pool \* msg\_subscriber\_pool

Net buf pool for message subscribers.

**Definition** zbus.h:63

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

**Definition** zbus.h:73

[zbus\_channel::validator](structzbus__channel.md#a047e9da011488c8f11abdc1fd283f5f6)

bool(\*const validator)(const void \*msg, size\_t msg\_size)

Message validator.

**Definition** zbus.h:95

[zbus\_channel::data](structzbus__channel.md#a30ad5027b70d6e9d28d0b0caef3571fe)

struct zbus\_channel\_data \*const data

Mutable channel data struct.

**Definition** zbus.h:98

[zbus\_channel::message\_size](structzbus__channel.md#a508bf72f7b47ad8781b4e4ef3645d17a)

const size\_t message\_size

Message size.

**Definition** zbus.h:84

[zbus\_channel::message](structzbus__channel.md#a7e8bd8f6c080615a4c4d524101201f19)

void \*const message

Message reference.

**Definition** zbus.h:81

[zbus\_channel::name](structzbus__channel.md#a9839e77746c53d24de69453aea53a233)

const char \*const name

Channel name.

**Definition** zbus.h:76

[zbus\_channel::user\_data](structzbus__channel.md#ae629044f9b6da800db5a628fc6789dfb)

void \*const user\_data

User data available to extend zbus features.

**Definition** zbus.h:89

[zbus\_observer\_data](structzbus__observer__data.md)

**Definition** zbus.h:112

[zbus\_observer\_data::enabled](structzbus__observer__data.md#ad16ca7a9e83f54afd75f6accf471eb91)

bool enabled

Enabled flag.

**Definition** zbus.h:114

[zbus\_observer](structzbus__observer.md)

Type used to represent an observer.

**Definition** zbus.h:137

[zbus\_observer::type](structzbus__observer.md#a0251cf9bdca418b6b8123b998b57efe2)

enum zbus\_observer\_type type

Type indication.

**Definition** zbus.h:143

[zbus\_observer::callback](structzbus__observer.md#a71fe83641f3e8c6248602150cbd998a1)

void(\*const callback)(const struct zbus\_channel \*chan)

Observer callback function.

**Definition** zbus.h:153

[zbus\_observer::data](structzbus__observer.md#a76bbaaf17ce0c58bfa9f9b604cbb496d)

struct zbus\_observer\_data \*const data

Mutable observer data struct.

**Definition** zbus.h:146

[zbus\_observer::queue](structzbus__observer.md#a7da8da6038d3dad4bc4c05279c28310c)

struct k\_msgq \*const queue

Observer message queue.

**Definition** zbus.h:150

[zbus\_observer::message\_fifo](structzbus__observer.md#a9073bc59a4662385d6c5d487e7be03c9)

struct k\_fifo \*const message\_fifo

Observer message FIFO.

**Definition** zbus.h:159

[zbus\_observer::name](structzbus__observer.md#ab2ba28a935b528b2db90389071769fd5)

const char \*const name

Observer name.

**Definition** zbus.h:140

[iterable\_sections.h](sys_2iterable__sections_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [zbus](dir_4ac3b76b03f02d08133e5af61546c3d3.md)
- [zbus.h](zbus_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
