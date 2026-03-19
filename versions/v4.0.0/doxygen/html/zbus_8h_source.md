---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/zbus_8h_source.html
original_path: doxygen/html/zbus_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
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

65

66#if defined(CONFIG\_ZBUS\_CHANNEL\_PUBLISH\_STATS) || defined(\_\_DOXYGEN\_\_)

[ 68](structzbus__channel__data.md#a1d75cb7c16798b5ef907f92a51ed7f63) [k\_ticks\_t](group__clock__apis.md#ga9832cb0adc2d1866420e5c370a0863e2) [publish\_timestamp](structzbus__channel__data.md#a1d75cb7c16798b5ef907f92a51ed7f63);

[ 70](structzbus__channel__data.md#a45172a94503b0005d662567c5cc8c97f) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [publish\_count](structzbus__channel__data.md#a45172a94503b0005d662567c5cc8c97f);

71#endif /\* CONFIG\_ZBUS\_CHANNEL\_PUBLISH\_STATS \*/

72};

73

[ 80](structzbus__channel.md)struct [zbus\_channel](structzbus__channel.md) {

81#if defined(CONFIG\_ZBUS\_CHANNEL\_NAME) || defined(\_\_DOXYGEN\_\_)

[ 83](structzbus__channel.md#ab8e66cdcfd2429058ca86e6af3813e03) const char \*[name](structzbus__channel.md#ab8e66cdcfd2429058ca86e6af3813e03);

84#endif

[ 88](structzbus__channel.md#abc00c2ed80b4ce3a0ea7304f43f30d08) void \*[message](structzbus__channel.md#abc00c2ed80b4ce3a0ea7304f43f30d08);

89

[ 91](structzbus__channel.md#ab7f330f3d70774afeebb74cc03f90d34) size\_t [message\_size](structzbus__channel.md#ab7f330f3d70774afeebb74cc03f90d34);

92

[ 96](structzbus__channel.md#a34864d7da9816955a41caf2a8355f3f0) void \*[user\_data](structzbus__channel.md#a34864d7da9816955a41caf2a8355f3f0);

97

[ 102](structzbus__channel.md#a90558613c362e75aa621cb240b178138) [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) (\*[validator](structzbus__channel.md#a90558613c362e75aa621cb240b178138))(const void \*msg, size\_t msg\_size);

103

[ 105](structzbus__channel.md#a5588983f2aefce2dd7cffad564c68d16) struct [zbus\_channel\_data](structzbus__channel__data.md) \*[data](structzbus__channel.md#a5588983f2aefce2dd7cffad564c68d16);

106};

107

[ 113](group__zbus__apis.md#ga88941281d7bdd24f3cfbb53e57711d8f)enum \_\_packed [zbus\_observer\_type](group__zbus__apis.md#ga88941281d7bdd24f3cfbb53e57711d8f) {

[ 114](group__zbus__apis.md#gga88941281d7bdd24f3cfbb53e57711d8fa127f19c2121c9c512da9dbcbb301320c) [ZBUS\_OBSERVER\_LISTENER\_TYPE](group__zbus__apis.md#gga88941281d7bdd24f3cfbb53e57711d8fa127f19c2121c9c512da9dbcbb301320c),

[ 115](group__zbus__apis.md#gga88941281d7bdd24f3cfbb53e57711d8fa22c784a85353545e8dca2ce7a0ec81b3) [ZBUS\_OBSERVER\_SUBSCRIBER\_TYPE](group__zbus__apis.md#gga88941281d7bdd24f3cfbb53e57711d8fa22c784a85353545e8dca2ce7a0ec81b3),

[ 116](group__zbus__apis.md#gga88941281d7bdd24f3cfbb53e57711d8fa8151f9e58a5bd96449bd2f9f8695538c) [ZBUS\_OBSERVER\_MSG\_SUBSCRIBER\_TYPE](group__zbus__apis.md#gga88941281d7bdd24f3cfbb53e57711d8fa8151f9e58a5bd96449bd2f9f8695538c),

117};

118

[ 119](structzbus__observer__data.md)struct [zbus\_observer\_data](structzbus__observer__data.md) {

[ 121](structzbus__observer__data.md#ad16ca7a9e83f54afd75f6accf471eb91) bool [enabled](structzbus__observer__data.md#ad16ca7a9e83f54afd75f6accf471eb91);

122

123#if defined(CONFIG\_ZBUS\_PRIORITY\_BOOST)

125 int priority;

126#endif /\* CONFIG\_ZBUS\_PRIORITY\_BOOST \*/

127};

128

[ 144](structzbus__observer.md)struct [zbus\_observer](structzbus__observer.md) {

145#if defined(CONFIG\_ZBUS\_OBSERVER\_NAME) || defined(\_\_DOXYGEN\_\_)

[ 147](structzbus__observer.md#ad9d31821d69e181f28e80e5eedf5a331) const char \*[name](structzbus__observer.md#ad9d31821d69e181f28e80e5eedf5a331);

148#endif

[ 150](structzbus__observer.md#a0251cf9bdca418b6b8123b998b57efe2) enum [zbus\_observer\_type](group__zbus__apis.md#ga88941281d7bdd24f3cfbb53e57711d8f) [type](structzbus__observer.md#a0251cf9bdca418b6b8123b998b57efe2);

151

[ 153](structzbus__observer.md#abdca15310be41ea2ce1ae3bbe0ebabb7) struct [zbus\_observer\_data](structzbus__observer__data.md) \*[data](structzbus__observer.md#abdca15310be41ea2ce1ae3bbe0ebabb7);

154

155 union {

[ 157](structzbus__observer.md#ac03ca78cff09b9466cbe34921862d27c) struct [k\_msgq](structk__msgq.md) \*[queue](structzbus__observer.md#ac03ca78cff09b9466cbe34921862d27c);

158

[ 160](structzbus__observer.md#a78037ed7bcba26af33b6221bf7e4f9d2) void (\*[callback](structzbus__observer.md#a78037ed7bcba26af33b6221bf7e4f9d2))(const struct [zbus\_channel](structzbus__channel.md) \*chan);

161

162#if defined(CONFIG\_ZBUS\_MSG\_SUBSCRIBER) || defined(\_\_DOXYGEN\_\_)

[ 166](structzbus__observer.md#a3594b07a2573e03b18ca640809ffd3fa) struct [k\_fifo](structk__fifo.md) \*[message\_fifo](structzbus__observer.md#a3594b07a2573e03b18ca640809ffd3fa);

167#endif /\* CONFIG\_ZBUS\_MSG\_SUBSCRIBER \*/

168 };

169};

170

172struct zbus\_channel\_observation\_mask {

173 bool enabled;

174};

175

176struct zbus\_channel\_observation {

177 const struct zbus\_channel \*chan;

178 const struct zbus\_observer \*obs;

179};

180

181#ifdef \_\_cplusplus

182#define \_ZBUS\_CPP\_EXTERN extern

183#else

184#define \_ZBUS\_CPP\_EXTERN

185#endif /\* \_\_cplusplus \*/

186

187#define ZBUS\_MIN\_THREAD\_PRIORITY (CONFIG\_NUM\_PREEMPT\_PRIORITIES - 1)

188

189#if defined(CONFIG\_ZBUS\_ASSERT\_MOCK)

190#define \_ZBUS\_ASSERT(\_cond, \_fmt, ...) \

191 do { \

192 if (!(\_cond)) { \

193 printk("ZBUS ASSERT: "); \

194 printk(\_fmt, ##\_\_VA\_ARGS\_\_); \

195 printk("\n"); \

196 return -EFAULT; \

197 } \

198 } while (0)

199#else

200#define \_ZBUS\_ASSERT(\_cond, \_fmt, ...) \_\_ASSERT(\_cond, \_fmt, ##\_\_VA\_ARGS\_\_)

201#endif

202

203#if defined(CONFIG\_ZBUS\_CHANNEL\_NAME)

204#define ZBUS\_CHANNEL\_NAME\_INIT(\_name) .name = #\_name,

205#define \_ZBUS\_CHAN\_NAME(\_chan) (\_chan)->name

206#else

207#define ZBUS\_CHANNEL\_NAME\_INIT(\_name)

208#define \_ZBUS\_CHAN\_NAME(\_chan) ""

209#endif

210

211#if defined(CONFIG\_ZBUS\_OBSERVER\_NAME)

212#define ZBUS\_OBSERVER\_NAME\_INIT(\_name) .name = #\_name,

213#define \_ZBUS\_OBS\_NAME(\_obs) (\_obs)->name

214#else

215#define ZBUS\_OBSERVER\_NAME\_INIT(\_name)

216#define \_ZBUS\_OBS\_NAME(\_obs) ""

217#endif

218

219#if defined(CONFIG\_ZBUS\_RUNTIME\_OBSERVERS)

220#define ZBUS\_RUNTIME\_OBSERVERS\_LIST\_DECL(\_slist\_name) static sys\_slist\_t \_slist\_name

221#define ZBUS\_RUNTIME\_OBSERVERS\_LIST\_INIT(\_slist\_name) .runtime\_observers = &\_slist\_name,

222#else

223#define ZBUS\_RUNTIME\_OBSERVERS\_LIST\_DECL(\_slist\_name)

224#define ZBUS\_RUNTIME\_OBSERVERS\_LIST\_INIT(\_slist\_name) /\* No runtime observers \*/

225#endif

226

227#define \_ZBUS\_OBS\_EXTERN(\_name) extern const struct zbus\_observer \_name

228

229#define \_ZBUS\_CHAN\_EXTERN(\_name) extern const struct zbus\_channel \_name

230

231#define ZBUS\_REF(\_value) &(\_value)

232

233#define FOR\_EACH\_FIXED\_ARG\_NONEMPTY\_TERM(F, sep, fixed\_arg, ...) \

234 COND\_CODE\_0(/\* are there zero non-empty arguments ? \*/ \

235 NUM\_VA\_ARGS\_LESS\_1( \

236 LIST\_DROP\_EMPTY(\_\_VA\_ARGS\_\_, \_)), /\* if so, expand to nothing \*/ \

237 (), /\* otherwise, expand to: \*/ \

238 (FOR\_EACH\_IDX\_FIXED\_ARG( \

239 F, sep, fixed\_arg, \

240 LIST\_DROP\_EMPTY(\_\_VA\_ARGS\_\_)) /\* plus a final terminator \*/ \

241 \_\_DEBRACKET sep))

242

243#define \_ZBUS\_OBSERVATION\_PREFIX(\_idx) \

244 GET\_ARG\_N(\_idx, 00, 01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 11, 12, 13, 14, 15, 16, 17, \

245 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, \

246 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, \

247 58, 59, 60, 61, 62, 63)

248

249#define \_ZBUS\_CHAN\_OBSERVATION(\_idx, \_obs, \_chan) \

250 const STRUCT\_SECTION\_ITERABLE( \

251 zbus\_channel\_observation, \

252 \_CONCAT(\_chan, \_ZBUS\_OBSERVATION\_PREFIX(UTIL\_INC(\_idx)))) = {.chan = &\_chan, \

253 .obs = &\_obs}; \

254 STRUCT\_SECTION\_ITERABLE(zbus\_channel\_observation\_mask, \

255 \_CONCAT(\_CONCAT(\_chan, \_ZBUS\_OBSERVATION\_PREFIX(UTIL\_INC(\_idx))), \

256 \_mask)) = {.enabled = false};

257

258#if defined(CONFIG\_ZBUS\_RUNTIME\_OBSERVERS) || defined(\_\_DOXYGEN\_\_)

259#define \_ZBUS\_RUNTIME\_OBSERVERS(\_name) .observers = &(\_CONCAT(\_observers\_, \_name)),

260#define \_ZBUS\_RUNTIME\_OBSERVERS\_DECL(\_name) static sys\_slist\_t \_CONCAT(\_observers\_, \_name);

261#else

262#define \_ZBUS\_RUNTIME\_OBSERVERS(\_name)

263#define \_ZBUS\_RUNTIME\_OBSERVERS\_DECL(\_name)

264#endif /\* CONFIG\_ZBUS\_RUNTIME\_OBSERVERS \*/

265

267

268/\* clang-format off \*/

269

[ 281](group__zbus__apis.md#ga7f763caca474e6c910793d2c714f80b4)#define ZBUS\_CHAN\_ADD\_OBS\_WITH\_MASK(\_chan, \_obs, \_masked, \_prio) \

282 const STRUCT\_SECTION\_ITERABLE(zbus\_channel\_observation, \

283 \_CONCAT(\_CONCAT(\_chan, zz), \_CONCAT(\_prio, \_obs))) = { \

284 .chan = &\_chan, \

285 .obs = &\_obs, \

286 }; \

287 STRUCT\_SECTION\_ITERABLE(zbus\_channel\_observation\_mask, \

288 \_CONCAT(\_CONCAT(\_CONCAT(\_chan, zz), \_CONCAT(\_prio, \_obs)), \

289 \_mask)) = {.enabled = \_masked}

290/\* clang-format on \*/

291

[ 302](group__zbus__apis.md#gaf63215f3f53741edf52b4d0d7b2b97df)#define ZBUS\_CHAN\_ADD\_OBS(\_chan, \_obs, \_prio) ZBUS\_CHAN\_ADD\_OBS\_WITH\_MASK(\_chan, \_obs, false, \_prio)

303

[ 309](group__zbus__apis.md#ga49f169c6d50a3bad57e1b319362d2924)#define ZBUS\_OBS\_DECLARE(...) FOR\_EACH\_NONEMPTY\_TERM(\_ZBUS\_OBS\_EXTERN, (;), \_\_VA\_ARGS\_\_)

310

[ 316](group__zbus__apis.md#ga0662b2db8077a8075c07a3afd0161d0f)#define ZBUS\_CHAN\_DECLARE(...) FOR\_EACH(\_ZBUS\_CHAN\_EXTERN, (;), \_\_VA\_ARGS\_\_)

317

[ 322](group__zbus__apis.md#ga763dad07a1ae9bb38f9c240e1920caef)#define ZBUS\_OBSERVERS\_EMPTY

323

[ 329](group__zbus__apis.md#gafed25f045c3b8d438daf4ebd5e517692)#define ZBUS\_OBSERVERS(...) \_\_VA\_ARGS\_\_

330

331/\* clang-format off \*/

332

[ 348](group__zbus__apis.md#ga29a3a39e5c78a34b2d8491615d1f0687)#define ZBUS\_CHAN\_DEFINE(\_name, \_type, \_validator, \_user\_data, \_observers, \_init\_val) \

349 static \_type \_CONCAT(\_zbus\_message\_, \_name) = \_init\_val; \

350 static struct zbus\_channel\_data \_CONCAT(\_zbus\_chan\_data\_, \_name) = { \

351 .observers\_start\_idx = -1, \

352 .observers\_end\_idx = -1, \

353 .sem = Z\_SEM\_INITIALIZER(\_CONCAT(\_zbus\_chan\_data\_, \_name).sem, 1, 1), \

354 IF\_ENABLED(CONFIG\_ZBUS\_PRIORITY\_BOOST, ( \

355 .highest\_observer\_priority = ZBUS\_MIN\_THREAD\_PRIORITY, \

356 )) \

357 IF\_ENABLED(CONFIG\_ZBUS\_RUNTIME\_OBSERVERS, ( \

358 .observers = SYS\_SLIST\_STATIC\_INIT( \

359 &\_CONCAT(\_zbus\_chan\_data\_, \_name).observers), \

360 )) \

361 }; \

362 static K\_MUTEX\_DEFINE(\_CONCAT(\_zbus\_mutex\_, \_name)); \

363 \_ZBUS\_CPP\_EXTERN const STRUCT\_SECTION\_ITERABLE(zbus\_channel, \_name) = { \

364 ZBUS\_CHANNEL\_NAME\_INIT(\_name) /\* Maybe removed \*/ \

365 .message = &\_CONCAT(\_zbus\_message\_, \_name), \

366 .message\_size = sizeof(\_type), \

367 .user\_data = \_user\_data, \

368 .validator = \_validator, \

369 .data = &\_CONCAT(\_zbus\_chan\_data\_, \_name), \

370 IF\_ENABLED(ZBUS\_MSG\_SUBSCRIBER\_NET\_BUF\_POOL\_ISOLATION, ( \

371 .msg\_subscriber\_pool = &\_zbus\_msg\_subscribers\_pool, \

372 )) \

373 }; \

374 /\* Extern declaration of observers \*/ \

375 ZBUS\_OBS\_DECLARE(\_observers); \

376 /\* Create all channel observations from observers list \*/ \

377 FOR\_EACH\_FIXED\_ARG\_NONEMPTY\_TERM(\_ZBUS\_CHAN\_OBSERVATION, (;), \_name, \_observers)

378/\* clang-format on \*/

379

[ 389](group__zbus__apis.md#ga4bf8c445814c1fcee9b9819a36bc9bd6)#define ZBUS\_MSG\_INIT(\_val, ...) \

390 { \

391 \_val, ##\_\_VA\_ARGS\_\_ \

392 }

393

394/\* clang-format off \*/

395

[ 407](group__zbus__apis.md#gaf56f71babe2bb27258f025332b80c58f)#define ZBUS\_SUBSCRIBER\_DEFINE\_WITH\_ENABLE(\_name, \_queue\_size, \_enable) \

408 K\_MSGQ\_DEFINE(\_zbus\_observer\_queue\_##\_name, \

409 sizeof(struct zbus\_channel \*), \

410 \_queue\_size, sizeof(struct zbus\_channel \*) \

411 ); \

412 static struct zbus\_observer\_data \_CONCAT(\_zbus\_obs\_data\_, \_name) = { \

413 .enabled = \_enable, \

414 IF\_ENABLED(CONFIG\_ZBUS\_PRIORITY\_BOOST, ( \

415 .priority = ZBUS\_MIN\_THREAD\_PRIORITY, \

416 )) \

417 }; \

418 \_ZBUS\_CPP\_EXTERN const STRUCT\_SECTION\_ITERABLE(zbus\_observer, \_name) = { \

419 ZBUS\_OBSERVER\_NAME\_INIT(\_name) /\* Name field \*/ \

420 .type = ZBUS\_OBSERVER\_SUBSCRIBER\_TYPE, \

421 .data = &\_CONCAT(\_zbus\_obs\_data\_, \_name), \

422 .queue = &\_zbus\_observer\_queue\_##\_name, \

423 }

424/\* clang-format on \*/

425

[ 437](group__zbus__apis.md#gac17a735cccecfc90f26127e48cf6279a)#define ZBUS\_SUBSCRIBER\_DEFINE(\_name, \_queue\_size) \

438 ZBUS\_SUBSCRIBER\_DEFINE\_WITH\_ENABLE(\_name, \_queue\_size, true)

439

440/\* clang-format off \*/

441

[ 453](group__zbus__apis.md#gace4ac9da0e1bab7ba72797783ded948f)#define ZBUS\_LISTENER\_DEFINE\_WITH\_ENABLE(\_name, \_cb, \_enable) \

454 static struct zbus\_observer\_data \_CONCAT(\_zbus\_obs\_data\_, \_name) = { \

455 .enabled = \_enable, \

456 IF\_ENABLED(CONFIG\_ZBUS\_PRIORITY\_BOOST, ( \

457 .priority = ZBUS\_MIN\_THREAD\_PRIORITY, \

458 )) \

459 }; \

460 \_ZBUS\_CPP\_EXTERN const STRUCT\_SECTION\_ITERABLE(zbus\_observer, \_name) = { \

461 ZBUS\_OBSERVER\_NAME\_INIT(\_name) /\* Name field \*/ \

462 .type = ZBUS\_OBSERVER\_LISTENER\_TYPE, \

463 .data = &\_CONCAT(\_zbus\_obs\_data\_, \_name), \

464 .callback = (\_cb) \

465 }

466/\* clang-format on \*/

467

[ 478](group__zbus__apis.md#gabfc7be8298e76fe2f7ae628be30b8390)#define ZBUS\_LISTENER\_DEFINE(\_name, \_cb) ZBUS\_LISTENER\_DEFINE\_WITH\_ENABLE(\_name, \_cb, true)

479

480/\* clang-format off \*/

481

[ 492](group__zbus__apis.md#ga6089c1ae0dad91306f79d48a63b31785)#define ZBUS\_MSG\_SUBSCRIBER\_DEFINE\_WITH\_ENABLE(\_name, \_enable) \

493 static K\_FIFO\_DEFINE(\_zbus\_observer\_fifo\_##\_name); \

494 static struct zbus\_observer\_data \_CONCAT(\_zbus\_obs\_data\_, \_name) = { \

495 .enabled = \_enable, \

496 IF\_ENABLED(CONFIG\_ZBUS\_PRIORITY\_BOOST, ( \

497 .priority = ZBUS\_MIN\_THREAD\_PRIORITY, \

498 )) \

499 }; \

500 \_ZBUS\_CPP\_EXTERN const STRUCT\_SECTION\_ITERABLE(zbus\_observer, \_name) = { \

501 ZBUS\_OBSERVER\_NAME\_INIT(\_name) /\* Name field \*/ \

502 .type = ZBUS\_OBSERVER\_MSG\_SUBSCRIBER\_TYPE, \

503 .data = &\_CONCAT(\_zbus\_obs\_data\_, \_name), \

504 .message\_fifo = &\_zbus\_observer\_fifo\_##\_name, \

505 }

506/\* clang-format on \*/

507

[ 519](group__zbus__apis.md#ga07a0c2c428c9e4891e86a63a420b2268)#define ZBUS\_MSG\_SUBSCRIBER\_DEFINE(\_name) ZBUS\_MSG\_SUBSCRIBER\_DEFINE\_WITH\_ENABLE(\_name, true)

[ 541](group__zbus__apis.md#gadfcaba65b397c1d8c31836ef3cf61244)int [zbus\_chan\_pub](group__zbus__apis.md#gadfcaba65b397c1d8c31836ef3cf61244)(const struct [zbus\_channel](structzbus__channel.md) \*chan, const void \*msg, [k\_timeout\_t](structk__timeout__t.md) timeout);

542

[ 560](group__zbus__apis.md#ga8209721e0a295c84d112ba1a7171100e)int [zbus\_chan\_read](group__zbus__apis.md#ga8209721e0a295c84d112ba1a7171100e)(const struct [zbus\_channel](structzbus__channel.md) \*chan, void \*msg, [k\_timeout\_t](structk__timeout__t.md) timeout);

561

[ 583](group__zbus__apis.md#ga00bfb7db54594029f4d288bcf5b56b3a)int [zbus\_chan\_claim](group__zbus__apis.md#ga00bfb7db54594029f4d288bcf5b56b3a)(const struct [zbus\_channel](structzbus__channel.md) \*chan, [k\_timeout\_t](structk__timeout__t.md) timeout);

584

[ 599](group__zbus__apis.md#ga74747affb345e68ce1d564c349409e59)int [zbus\_chan\_finish](group__zbus__apis.md#ga74747affb345e68ce1d564c349409e59)(const struct [zbus\_channel](structzbus__channel.md) \*chan);

600

[ 619](group__zbus__apis.md#ga6ec2f463801499e23a011fa4e68aa3e7)int [zbus\_chan\_notify](group__zbus__apis.md#ga6ec2f463801499e23a011fa4e68aa3e7)(const struct [zbus\_channel](structzbus__channel.md) \*chan, [k\_timeout\_t](structk__timeout__t.md) timeout);

620

621#if defined(CONFIG\_ZBUS\_CHANNEL\_NAME) || defined(\_\_DOXYGEN\_\_)

622

[ 632](group__zbus__apis.md#ga05a220636fc6bb58b97805e558b76d73)static inline const char \*[zbus\_chan\_name](group__zbus__apis.md#ga05a220636fc6bb58b97805e558b76d73)(const struct [zbus\_channel](structzbus__channel.md) \*chan)

633{

634 \_\_ASSERT(chan != NULL, "chan is required");

635

636 return chan->[name](structzbus__channel.md#ab8e66cdcfd2429058ca86e6af3813e03);

637}

638

639#endif

640

[ 653](group__zbus__apis.md#gaaf8b34113b7b993438bd42db64812572)static inline void \*[zbus\_chan\_msg](group__zbus__apis.md#gaaf8b34113b7b993438bd42db64812572)(const struct [zbus\_channel](structzbus__channel.md) \*chan)

654{

655 \_\_ASSERT(chan != NULL, "chan is required");

656

657 return chan->[message](structzbus__channel.md#abc00c2ed80b4ce3a0ea7304f43f30d08);

658}

659

[ 674](group__zbus__apis.md#gafee07c355df9ac86b85e601196b56a10)static inline const void \*[zbus\_chan\_const\_msg](group__zbus__apis.md#gafee07c355df9ac86b85e601196b56a10)(const struct [zbus\_channel](structzbus__channel.md) \*chan)

675{

676 \_\_ASSERT(chan != NULL, "chan is required");

677

678 return chan->[message](structzbus__channel.md#abc00c2ed80b4ce3a0ea7304f43f30d08);

679}

680

[ 690](group__zbus__apis.md#ga8895a18b282ca2fe7528b4e5cf48e025)static inline [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [zbus\_chan\_msg\_size](group__zbus__apis.md#ga8895a18b282ca2fe7528b4e5cf48e025)(const struct [zbus\_channel](structzbus__channel.md) \*chan)

691{

692 \_\_ASSERT(chan != NULL, "chan is required");

693

694 return chan->[message\_size](structzbus__channel.md#ab7f330f3d70774afeebb74cc03f90d34);

695}

696

[ 706](group__zbus__apis.md#gac0b0ed0356fca5a8b65a3332931a369a)static inline void \*[zbus\_chan\_user\_data](group__zbus__apis.md#gac0b0ed0356fca5a8b65a3332931a369a)(const struct [zbus\_channel](structzbus__channel.md) \*chan)

707{

708 \_\_ASSERT(chan != NULL, "chan is required");

709

710 return chan->[user\_data](structzbus__channel.md#a34864d7da9816955a41caf2a8355f3f0);

711}

712

713#if defined(CONFIG\_ZBUS\_MSG\_SUBSCRIBER\_NET\_BUF\_POOL\_ISOLATION) || defined(\_\_DOXYGEN\_\_)

714

[ 721](group__zbus__apis.md#ga3f90d50f20e7779ef257676ac10da357)static inline void [zbus\_chan\_set\_msg\_sub\_pool](group__zbus__apis.md#ga3f90d50f20e7779ef257676ac10da357)(const struct [zbus\_channel](structzbus__channel.md) \*chan,

722 struct [net\_buf\_pool](structnet__buf__pool.md) \*pool)

723{

724 \_\_ASSERT(chan != NULL, "chan is required");

725 \_\_ASSERT(pool != NULL, "pool is required");

726

727 chan->[data](structzbus__channel.md#a5588983f2aefce2dd7cffad564c68d16)->[msg\_subscriber\_pool](structzbus__channel__data.md#a2490c05755696b7ba1f1f1392d27845f) = pool;

728}

729

730#endif /\* ZBUS\_MSG\_SUBSCRIBER\_NET\_BUF\_POOL\_ISOLATION \*/

731

732#if defined(CONFIG\_ZBUS\_CHANNEL\_PUBLISH\_STATS) || defined(\_\_DOXYGEN\_\_)

733

[ 745](group__zbus__apis.md#gaef067fb1e8b834993662af84b916483a)static inline void [zbus\_chan\_pub\_stats\_update](group__zbus__apis.md#gaef067fb1e8b834993662af84b916483a)(const struct [zbus\_channel](structzbus__channel.md) \*chan)

746{

747 \_\_ASSERT(chan != NULL, "chan is required");

748

749 chan->[data](structzbus__channel.md#a5588983f2aefce2dd7cffad564c68d16)->[publish\_timestamp](structzbus__channel__data.md#a1d75cb7c16798b5ef907f92a51ed7f63) = [k\_uptime\_ticks](group__clock__apis.md#ga8f143af2ee4ad42d9f7817ef161cbd13)();

750 chan->[data](structzbus__channel.md#a5588983f2aefce2dd7cffad564c68d16)->[publish\_count](structzbus__channel__data.md#a45172a94503b0005d662567c5cc8c97f) += 1;

751}

752

[ 762](group__zbus__apis.md#gac5dff9990d709d736b30f36d68c0297b)static inline [k\_ticks\_t](group__clock__apis.md#ga9832cb0adc2d1866420e5c370a0863e2) [zbus\_chan\_pub\_stats\_last\_time](group__zbus__apis.md#gac5dff9990d709d736b30f36d68c0297b)(const struct [zbus\_channel](structzbus__channel.md) \*chan)

763{

764 \_\_ASSERT(chan != NULL, "chan is required");

765

766 return chan->[data](structzbus__channel.md#a5588983f2aefce2dd7cffad564c68d16)->[publish\_timestamp](structzbus__channel__data.md#a1d75cb7c16798b5ef907f92a51ed7f63);

767}

768

[ 778](group__zbus__apis.md#ga5648bf527de4aff89648a34bf8a7539a)static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [zbus\_chan\_pub\_stats\_count](group__zbus__apis.md#ga5648bf527de4aff89648a34bf8a7539a)(const struct [zbus\_channel](structzbus__channel.md) \*chan)

779{

780 \_\_ASSERT(chan != NULL, "chan is required");

781

782 return chan->[data](structzbus__channel.md#a5588983f2aefce2dd7cffad564c68d16)->[publish\_count](structzbus__channel__data.md#a45172a94503b0005d662567c5cc8c97f);

783}

784

[ 794](group__zbus__apis.md#ga09503e2b9c01f79136f9eb600ddb3f31)static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [zbus\_chan\_pub\_stats\_avg\_period](group__zbus__apis.md#ga09503e2b9c01f79136f9eb600ddb3f31)(const struct [zbus\_channel](structzbus__channel.md) \*chan)

795{

796 \_\_ASSERT(chan != NULL, "chan is required");

797

798 /\* Not yet published, period = 0ms \*/

799 if (chan->[data](structzbus__channel.md#a5588983f2aefce2dd7cffad564c68d16)->[publish\_count](structzbus__channel__data.md#a45172a94503b0005d662567c5cc8c97f) == 0) {

800 return 0;

801 }

802 /\* Average period across application runtime \*/

803 return [k\_uptime\_get](group__clock__apis.md#gae3e992cd3257c23d5b26d765fcbb2b69)() / chan->[data](structzbus__channel.md#a5588983f2aefce2dd7cffad564c68d16)->[publish\_count](structzbus__channel__data.md#a45172a94503b0005d662567c5cc8c97f);

804}

805

806#else

807

808static inline void [zbus\_chan\_pub\_stats\_update](group__zbus__apis.md#gaef067fb1e8b834993662af84b916483a)(const struct [zbus\_channel](structzbus__channel.md) \*chan)

809{

810 (void)chan;

811}

812

813#endif /\* CONFIG\_ZBUS\_CHANNEL\_PUBLISH\_STATS \*/

814

815#if defined(CONFIG\_ZBUS\_RUNTIME\_OBSERVERS) || defined(\_\_DOXYGEN\_\_)

816

[ 833](group__zbus__apis.md#gaddd8ce480bc29ead4442e529915cfbf6)int [zbus\_chan\_add\_obs](group__zbus__apis.md#gaddd8ce480bc29ead4442e529915cfbf6)(const struct [zbus\_channel](structzbus__channel.md) \*chan, const struct [zbus\_observer](structzbus__observer.md) \*obs,

834 [k\_timeout\_t](structk__timeout__t.md) timeout);

835

[ 853](group__zbus__apis.md#gaee11d7472a3f87156b8ef1dcfbe897c4)int [zbus\_chan\_rm\_obs](group__zbus__apis.md#gaee11d7472a3f87156b8ef1dcfbe897c4)(const struct [zbus\_channel](structzbus__channel.md) \*chan, const struct [zbus\_observer](structzbus__observer.md) \*obs,

854 [k\_timeout\_t](structk__timeout__t.md) timeout);

855

857

858struct zbus\_observer\_node {

859 [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) node;

860 const struct [zbus\_observer](structzbus__observer.md) \*obs;

861};

862

864

865#endif /\* CONFIG\_ZBUS\_RUNTIME\_OBSERVERS \*/

866

[ 880](group__zbus__apis.md#ga96767314e040e42609867a36684a6349)int [zbus\_obs\_set\_enable](group__zbus__apis.md#ga96767314e040e42609867a36684a6349)(const struct [zbus\_observer](structzbus__observer.md) \*obs, bool enabled);

881

[ 892](group__zbus__apis.md#ga315fd4e0b6a3c01a23307dd890e69894)static inline int [zbus\_obs\_is\_enabled](group__zbus__apis.md#ga315fd4e0b6a3c01a23307dd890e69894)(const struct [zbus\_observer](structzbus__observer.md) \*obs, bool \*enable)

893{

894 \_ZBUS\_ASSERT(obs != NULL, "obs is required");

895 \_ZBUS\_ASSERT(enable != NULL, "enable is required");

896

897 \*enable = obs->[data](structzbus__observer.md#abdca15310be41ea2ce1ae3bbe0ebabb7)->[enabled](structzbus__observer__data.md#ad16ca7a9e83f54afd75f6accf471eb91);

898

899 return 0;

900}

901

[ 916](group__zbus__apis.md#ga9513264f912f54b60c4341642f578e5a)int [zbus\_obs\_set\_chan\_notification\_mask](group__zbus__apis.md#ga9513264f912f54b60c4341642f578e5a)(const struct [zbus\_observer](structzbus__observer.md) \*obs,

917 const struct [zbus\_channel](structzbus__channel.md) \*chan, bool masked);

918

[ 931](group__zbus__apis.md#ga41ae9799a52c2a7954500b0a3c78d19f)int [zbus\_obs\_is\_chan\_notification\_masked](group__zbus__apis.md#ga41ae9799a52c2a7954500b0a3c78d19f)(const struct [zbus\_observer](structzbus__observer.md) \*obs,

932 const struct [zbus\_channel](structzbus__channel.md) \*chan, bool \*masked);

933

934#if defined(CONFIG\_ZBUS\_OBSERVER\_NAME) || defined(\_\_DOXYGEN\_\_)

935

[ 945](group__zbus__apis.md#ga5bb33ec5b914e6cbc87fa70bf763ad15)static inline const char \*[zbus\_obs\_name](group__zbus__apis.md#ga5bb33ec5b914e6cbc87fa70bf763ad15)(const struct [zbus\_observer](structzbus__observer.md) \*obs)

946{

947 \_\_ASSERT(obs != NULL, "obs is required");

948

949 return obs->[name](structzbus__observer.md#ad9d31821d69e181f28e80e5eedf5a331);

950}

951

952#endif

953

954#if defined(CONFIG\_ZBUS\_PRIORITY\_BOOST) || defined(\_\_DOXYGEN\_\_)

955

[ 965](group__zbus__apis.md#gabecf160e4d468d0275ad79e22fd0fb5b)int [zbus\_obs\_attach\_to\_thread](group__zbus__apis.md#gabecf160e4d468d0275ad79e22fd0fb5b)(const struct [zbus\_observer](structzbus__observer.md) \*obs);

966

[ 976](group__zbus__apis.md#ga493c125c31e44d5a222f0e9c6d01249e)int [zbus\_obs\_detach\_from\_thread](group__zbus__apis.md#ga493c125c31e44d5a222f0e9c6d01249e)(const struct [zbus\_observer](structzbus__observer.md) \*obs);

977

978#endif /\* CONFIG\_ZBUS\_PRIORITY\_BOOST \*/

979

[ 998](group__zbus__apis.md#ga84a65e276a01ef97eeb5c81b880da72b)int [zbus\_sub\_wait](group__zbus__apis.md#ga84a65e276a01ef97eeb5c81b880da72b)(const struct [zbus\_observer](structzbus__observer.md) \*sub, const struct [zbus\_channel](structzbus__channel.md) \*\*chan,

999 [k\_timeout\_t](structk__timeout__t.md) timeout);

1000

1001#if defined(CONFIG\_ZBUS\_MSG\_SUBSCRIBER) || defined(\_\_DOXYGEN\_\_)

1002

[ 1021](group__zbus__apis.md#gaeffce45446509e488192a4e6442453fb)int [zbus\_sub\_wait\_msg](group__zbus__apis.md#gaeffce45446509e488192a4e6442453fb)(const struct [zbus\_observer](structzbus__observer.md) \*sub, const struct [zbus\_channel](structzbus__channel.md) \*\*chan, void \*msg,

1022 [k\_timeout\_t](structk__timeout__t.md) timeout);

1023

1024#endif /\* CONFIG\_ZBUS\_MSG\_SUBSCRIBER \*/

1025

[ 1039](group__zbus__apis.md#ga6dffd25f4eb368e773c2bd55f34a0e10)bool [zbus\_iterate\_over\_channels](group__zbus__apis.md#ga6dffd25f4eb368e773c2bd55f34a0e10)(bool (\*iterator\_func)(const struct [zbus\_channel](structzbus__channel.md) \*chan));

[ 1054](group__zbus__apis.md#gab8df108b0238757ff631ec1e120fa2c3)bool [zbus\_iterate\_over\_channels\_with\_user\_data](group__zbus__apis.md#gab8df108b0238757ff631ec1e120fa2c3)(

1055 bool (\*iterator\_func)(const struct [zbus\_channel](structzbus__channel.md) \*chan, void \*user\_data), void \*user\_data);

1056

[ 1070](group__zbus__apis.md#ga2fa50316993afc5807e9d707d664be14)bool [zbus\_iterate\_over\_observers](group__zbus__apis.md#ga2fa50316993afc5807e9d707d664be14)(bool (\*iterator\_func)(const struct [zbus\_observer](structzbus__observer.md) \*obs));

[ 1085](group__zbus__apis.md#ga2f4e39c500fed0a6bcfedb5dec3f797a)bool [zbus\_iterate\_over\_observers\_with\_user\_data](group__zbus__apis.md#ga2f4e39c500fed0a6bcfedb5dec3f797a)(

1086 bool (\*iterator\_func)(const struct [zbus\_observer](structzbus__observer.md) \*obs, void \*user\_data), void \*user\_data);

1087

1091

1092#ifdef \_\_cplusplus

1093}

1094#endif

1095

1096#endif /\* ZEPHYR\_INCLUDE\_ZBUS\_H\_ \*/

[k\_uptime\_ticks](group__clock__apis.md#ga8f143af2ee4ad42d9f7817ef161cbd13)

int64\_t k\_uptime\_ticks(void)

Get system uptime, in system ticks.

[k\_ticks\_t](group__clock__apis.md#ga9832cb0adc2d1866420e5c370a0863e2)

uint32\_t k\_ticks\_t

Tick precision used in timeout APIs.

**Definition** sys\_clock.h:48

[k\_uptime\_get](group__clock__apis.md#gae3e992cd3257c23d5b26d765fcbb2b69)

static int64\_t k\_uptime\_get(void)

Get system uptime.

**Definition** kernel.h:1828

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

**Definition** zbus.h:632

[zbus\_chan\_pub\_stats\_avg\_period](group__zbus__apis.md#ga09503e2b9c01f79136f9eb600ddb3f31)

static uint32\_t zbus\_chan\_pub\_stats\_avg\_period(const struct zbus\_channel \*chan)

Get the average period between publishes to a channel.

**Definition** zbus.h:794

[zbus\_iterate\_over\_observers\_with\_user\_data](group__zbus__apis.md#ga2f4e39c500fed0a6bcfedb5dec3f797a)

bool zbus\_iterate\_over\_observers\_with\_user\_data(bool(\*iterator\_func)(const struct zbus\_observer \*obs, void \*user\_data), void \*user\_data)

Iterate over observers with user data.

[zbus\_iterate\_over\_observers](group__zbus__apis.md#ga2fa50316993afc5807e9d707d664be14)

bool zbus\_iterate\_over\_observers(bool(\*iterator\_func)(const struct zbus\_observer \*obs))

Iterate over observers.

[zbus\_obs\_is\_enabled](group__zbus__apis.md#ga315fd4e0b6a3c01a23307dd890e69894)

static int zbus\_obs\_is\_enabled(const struct zbus\_observer \*obs, bool \*enable)

Get the observer state.

**Definition** zbus.h:892

[zbus\_chan\_set\_msg\_sub\_pool](group__zbus__apis.md#ga3f90d50f20e7779ef257676ac10da357)

static void zbus\_chan\_set\_msg\_sub\_pool(const struct zbus\_channel \*chan, struct net\_buf\_pool \*pool)

Set the channel's msg subscriber net\_buf pool.

**Definition** zbus.h:721

[zbus\_obs\_is\_chan\_notification\_masked](group__zbus__apis.md#ga41ae9799a52c2a7954500b0a3c78d19f)

int zbus\_obs\_is\_chan\_notification\_masked(const struct zbus\_observer \*obs, const struct zbus\_channel \*chan, bool \*masked)

Get the notifications masking state from a channel to an observer.

[zbus\_obs\_detach\_from\_thread](group__zbus__apis.md#ga493c125c31e44d5a222f0e9c6d01249e)

int zbus\_obs\_detach\_from\_thread(const struct zbus\_observer \*obs)

Clear the observer thread priority by detaching it from a thread.

[zbus\_chan\_pub\_stats\_count](group__zbus__apis.md#ga5648bf527de4aff89648a34bf8a7539a)

static uint32\_t zbus\_chan\_pub\_stats\_count(const struct zbus\_channel \*chan)

Get the number of times a channel has been published to.

**Definition** zbus.h:778

[zbus\_obs\_name](group__zbus__apis.md#ga5bb33ec5b914e6cbc87fa70bf763ad15)

static const char \* zbus\_obs\_name(const struct zbus\_observer \*obs)

Get the observer's name.

**Definition** zbus.h:945

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

**Definition** zbus.h:113

[zbus\_chan\_msg\_size](group__zbus__apis.md#ga8895a18b282ca2fe7528b4e5cf48e025)

static uint16\_t zbus\_chan\_msg\_size(const struct zbus\_channel \*chan)

Get the channel's message size.

**Definition** zbus.h:690

[zbus\_obs\_set\_chan\_notification\_mask](group__zbus__apis.md#ga9513264f912f54b60c4341642f578e5a)

int zbus\_obs\_set\_chan\_notification\_mask(const struct zbus\_observer \*obs, const struct zbus\_channel \*chan, bool masked)

Mask notifications from a channel to an observer.

[zbus\_obs\_set\_enable](group__zbus__apis.md#ga96767314e040e42609867a36684a6349)

int zbus\_obs\_set\_enable(const struct zbus\_observer \*obs, bool enabled)

Change the observer state.

[zbus\_chan\_msg](group__zbus__apis.md#gaaf8b34113b7b993438bd42db64812572)

static void \* zbus\_chan\_msg(const struct zbus\_channel \*chan)

Get the reference for a channel message directly.

**Definition** zbus.h:653

[zbus\_iterate\_over\_channels\_with\_user\_data](group__zbus__apis.md#gab8df108b0238757ff631ec1e120fa2c3)

bool zbus\_iterate\_over\_channels\_with\_user\_data(bool(\*iterator\_func)(const struct zbus\_channel \*chan, void \*user\_data), void \*user\_data)

Iterate over channels with user data.

[zbus\_obs\_attach\_to\_thread](group__zbus__apis.md#gabecf160e4d468d0275ad79e22fd0fb5b)

int zbus\_obs\_attach\_to\_thread(const struct zbus\_observer \*obs)

Set the observer thread priority by attaching it to a thread.

[zbus\_chan\_user\_data](group__zbus__apis.md#gac0b0ed0356fca5a8b65a3332931a369a)

static void \* zbus\_chan\_user\_data(const struct zbus\_channel \*chan)

Get the channel's user data.

**Definition** zbus.h:706

[zbus\_chan\_pub\_stats\_last\_time](group__zbus__apis.md#gac5dff9990d709d736b30f36d68c0297b)

static k\_ticks\_t zbus\_chan\_pub\_stats\_last\_time(const struct zbus\_channel \*chan)

Get the time a channel was last published to.

**Definition** zbus.h:762

[zbus\_chan\_add\_obs](group__zbus__apis.md#gaddd8ce480bc29ead4442e529915cfbf6)

int zbus\_chan\_add\_obs(const struct zbus\_channel \*chan, const struct zbus\_observer \*obs, k\_timeout\_t timeout)

Add an observer to a channel.

[zbus\_chan\_pub](group__zbus__apis.md#gadfcaba65b397c1d8c31836ef3cf61244)

int zbus\_chan\_pub(const struct zbus\_channel \*chan, const void \*msg, k\_timeout\_t timeout)

Publish to a channel.

[zbus\_chan\_rm\_obs](group__zbus__apis.md#gaee11d7472a3f87156b8ef1dcfbe897c4)

int zbus\_chan\_rm\_obs(const struct zbus\_channel \*chan, const struct zbus\_observer \*obs, k\_timeout\_t timeout)

Remove an observer from a channel.

[zbus\_chan\_pub\_stats\_update](group__zbus__apis.md#gaef067fb1e8b834993662af84b916483a)

static void zbus\_chan\_pub\_stats\_update(const struct zbus\_channel \*chan)

Update the publishing statistics for a channel.

**Definition** zbus.h:745

[zbus\_sub\_wait\_msg](group__zbus__apis.md#gaeffce45446509e488192a4e6442453fb)

int zbus\_sub\_wait\_msg(const struct zbus\_observer \*sub, const struct zbus\_channel \*\*chan, void \*msg, k\_timeout\_t timeout)

Wait for a channel message.

[zbus\_chan\_const\_msg](group__zbus__apis.md#gafee07c355df9ac86b85e601196b56a10)

static const void \* zbus\_chan\_const\_msg(const struct zbus\_channel \*chan)

Get a constant reference for a channel message directly.

**Definition** zbus.h:674

[ZBUS\_OBSERVER\_LISTENER\_TYPE](group__zbus__apis.md#gga88941281d7bdd24f3cfbb53e57711d8fa127f19c2121c9c512da9dbcbb301320c)

@ ZBUS\_OBSERVER\_LISTENER\_TYPE

**Definition** zbus.h:114

[ZBUS\_OBSERVER\_SUBSCRIBER\_TYPE](group__zbus__apis.md#gga88941281d7bdd24f3cfbb53e57711d8fa22c784a85353545e8dca2ce7a0ec81b3)

@ ZBUS\_OBSERVER\_SUBSCRIBER\_TYPE

**Definition** zbus.h:115

[ZBUS\_OBSERVER\_MSG\_SUBSCRIBER\_TYPE](group__zbus__apis.md#gga88941281d7bdd24f3cfbb53e57711d8fa8151f9e58a5bd96449bd2f9f8695538c)

@ ZBUS\_OBSERVER\_MSG\_SUBSCRIBER\_TYPE

**Definition** zbus.h:116

[kernel.h](kernel_8h.md)

Public kernel APIs.

[bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)

#define bool

**Definition** stdbool.h:13

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf)

\_\_INT16\_TYPE\_\_ int16\_t

**Definition** stdint.h:73

[string.h](string_8h.md)

[k\_fifo](structk__fifo.md)

**Definition** kernel.h:2468

[k\_msgq](structk__msgq.md)

Message Queue Structure.

**Definition** kernel.h:4503

[k\_timeout\_t](structk__timeout__t.md)

Kernel timeout type.

**Definition** sys\_clock.h:65

[net\_buf\_pool](structnet__buf__pool.md)

Network buffer pool representation.

**Definition** net\_buf.h:1078

[zbus\_channel\_data](structzbus__channel__data.md)

Type used to represent a channel mutable data.

**Definition** zbus.h:30

[zbus\_channel\_data::publish\_timestamp](structzbus__channel__data.md#a1d75cb7c16798b5ef907f92a51ed7f63)

k\_ticks\_t publish\_timestamp

Kernel timestamp of the last publish action on this channel.

**Definition** zbus.h:68

[zbus\_channel\_data::msg\_subscriber\_pool](structzbus__channel__data.md#a2490c05755696b7ba1f1f1392d27845f)

struct net\_buf\_pool \* msg\_subscriber\_pool

Net buf pool for message subscribers.

**Definition** zbus.h:63

[zbus\_channel\_data::publish\_count](structzbus__channel__data.md#a45172a94503b0005d662567c5cc8c97f)

uint32\_t publish\_count

Number of times data has been published to this channel.

**Definition** zbus.h:70

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

**Definition** zbus.h:80

[zbus\_channel::user\_data](structzbus__channel.md#a34864d7da9816955a41caf2a8355f3f0)

void \* user\_data

User data available to extend zbus features.

**Definition** zbus.h:96

[zbus\_channel::data](structzbus__channel.md#a5588983f2aefce2dd7cffad564c68d16)

struct zbus\_channel\_data \* data

Mutable channel data struct.

**Definition** zbus.h:105

[zbus\_channel::validator](structzbus__channel.md#a90558613c362e75aa621cb240b178138)

bool(\* validator)(const void \*msg, size\_t msg\_size)

Message validator.

**Definition** zbus.h:102

[zbus\_channel::message\_size](structzbus__channel.md#ab7f330f3d70774afeebb74cc03f90d34)

size\_t message\_size

Message size.

**Definition** zbus.h:91

[zbus\_channel::name](structzbus__channel.md#ab8e66cdcfd2429058ca86e6af3813e03)

const char \* name

Channel name.

**Definition** zbus.h:83

[zbus\_channel::message](structzbus__channel.md#abc00c2ed80b4ce3a0ea7304f43f30d08)

void \* message

Message reference.

**Definition** zbus.h:88

[zbus\_observer\_data](structzbus__observer__data.md)

**Definition** zbus.h:119

[zbus\_observer\_data::enabled](structzbus__observer__data.md#ad16ca7a9e83f54afd75f6accf471eb91)

bool enabled

Enabled flag.

**Definition** zbus.h:121

[zbus\_observer](structzbus__observer.md)

Type used to represent an observer.

**Definition** zbus.h:144

[zbus\_observer::type](structzbus__observer.md#a0251cf9bdca418b6b8123b998b57efe2)

enum zbus\_observer\_type type

Type indication.

**Definition** zbus.h:150

[zbus\_observer::message\_fifo](structzbus__observer.md#a3594b07a2573e03b18ca640809ffd3fa)

struct k\_fifo \* message\_fifo

Observer message FIFO.

**Definition** zbus.h:166

[zbus\_observer::callback](structzbus__observer.md#a78037ed7bcba26af33b6221bf7e4f9d2)

void(\* callback)(const struct zbus\_channel \*chan)

Observer callback function.

**Definition** zbus.h:160

[zbus\_observer::data](structzbus__observer.md#abdca15310be41ea2ce1ae3bbe0ebabb7)

struct zbus\_observer\_data \* data

Mutable observer data struct.

**Definition** zbus.h:153

[zbus\_observer::queue](structzbus__observer.md#ac03ca78cff09b9466cbe34921862d27c)

struct k\_msgq \* queue

Observer message queue.

**Definition** zbus.h:157

[zbus\_observer::name](structzbus__observer.md#ad9d31821d69e181f28e80e5eedf5a331)

const char \* name

Observer name.

**Definition** zbus.h:147

[iterable\_sections.h](sys_2iterable__sections_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [zbus](dir_4ac3b76b03f02d08133e5af61546c3d3.md)
- [zbus.h](zbus_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
