---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/zbus_8h_source.html
original_path: doxygen/html/zbus_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
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

26

[ 32](structzbus__channel__data.md)struct [zbus\_channel\_data](structzbus__channel__data.md) {

[ 36](structzbus__channel__data.md#a6329a0af467d83ad488f3310c1002c41) [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) [observers\_start\_idx](structzbus__channel__data.md#a6329a0af467d83ad488f3310c1002c41);

37

[ 41](structzbus__channel__data.md#a5b3c38f70cd99cc7e83f9b641997e1ed) [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) [observers\_end\_idx](structzbus__channel__data.md#a5b3c38f70cd99cc7e83f9b641997e1ed);

42

[ 46](structzbus__channel__data.md#a6fa71ae5dc260f5934f47383f53891a7) struct [k\_sem](structk__sem.md) [sem](structzbus__channel__data.md#a6fa71ae5dc260f5934f47383f53891a7);

47

48#if defined(CONFIG\_ZBUS\_PRIORITY\_BOOST)

52 int highest\_observer\_priority;

53#endif /\* CONFIG\_ZBUS\_PRIORITY\_BOOST \*/

54

55#if defined(CONFIG\_ZBUS\_RUNTIME\_OBSERVERS) || defined(\_\_DOXYGEN\_\_)

[ 59](structzbus__channel__data.md#aeffcb35769775ee0927c3af9be77d1e1) [sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8) [observers](structzbus__channel__data.md#aeffcb35769775ee0927c3af9be77d1e1);

60#endif /\* CONFIG\_ZBUS\_RUNTIME\_OBSERVERS \*/

61

62#if defined(CONFIG\_ZBUS\_MSG\_SUBSCRIBER\_NET\_BUF\_POOL\_ISOLATION) || defined(\_\_DOXYGEN\_\_)

[ 65](structzbus__channel__data.md#a2490c05755696b7ba1f1f1392d27845f) struct [net\_buf\_pool](structnet__buf__pool.md) \*[msg\_subscriber\_pool](structzbus__channel__data.md#a2490c05755696b7ba1f1f1392d27845f);

66#endif /\* ZBUS\_MSG\_SUBSCRIBER\_NET\_BUF\_POOL\_ISOLATION \*/

67

68#if defined(CONFIG\_ZBUS\_CHANNEL\_PUBLISH\_STATS) || defined(\_\_DOXYGEN\_\_)

[ 70](structzbus__channel__data.md#a1d75cb7c16798b5ef907f92a51ed7f63) [k\_ticks\_t](group__clock__apis.md#ga9832cb0adc2d1866420e5c370a0863e2) [publish\_timestamp](structzbus__channel__data.md#a1d75cb7c16798b5ef907f92a51ed7f63);

[ 72](structzbus__channel__data.md#a45172a94503b0005d662567c5cc8c97f) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [publish\_count](structzbus__channel__data.md#a45172a94503b0005d662567c5cc8c97f);

73#endif /\* CONFIG\_ZBUS\_CHANNEL\_PUBLISH\_STATS \*/

74};

75

[ 82](structzbus__channel.md)struct [zbus\_channel](structzbus__channel.md) {

83#if defined(CONFIG\_ZBUS\_CHANNEL\_NAME) || defined(\_\_DOXYGEN\_\_)

[ 85](structzbus__channel.md#ab8e66cdcfd2429058ca86e6af3813e03) const char \*[name](structzbus__channel.md#ab8e66cdcfd2429058ca86e6af3813e03);

86#endif

87#if defined(CONFIG\_ZBUS\_CHANNEL\_ID) || defined(\_\_DOXYGEN\_\_)

[ 89](structzbus__channel.md#a438ff0d8bf5a1d05af2f16f737c40d4f) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [id](structzbus__channel.md#a438ff0d8bf5a1d05af2f16f737c40d4f);

90#endif

[ 94](structzbus__channel.md#abc00c2ed80b4ce3a0ea7304f43f30d08) void \*[message](structzbus__channel.md#abc00c2ed80b4ce3a0ea7304f43f30d08);

95

[ 97](structzbus__channel.md#ab7f330f3d70774afeebb74cc03f90d34) size\_t [message\_size](structzbus__channel.md#ab7f330f3d70774afeebb74cc03f90d34);

98

[ 102](structzbus__channel.md#a34864d7da9816955a41caf2a8355f3f0) void \*[user\_data](structzbus__channel.md#a34864d7da9816955a41caf2a8355f3f0);

103

[ 108](structzbus__channel.md#a90558613c362e75aa621cb240b178138) [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) (\*[validator](structzbus__channel.md#a90558613c362e75aa621cb240b178138))(const void \*msg, size\_t msg\_size);

109

[ 111](structzbus__channel.md#a5588983f2aefce2dd7cffad564c68d16) struct [zbus\_channel\_data](structzbus__channel__data.md) \*[data](structzbus__channel.md#a5588983f2aefce2dd7cffad564c68d16);

112};

113

[ 119](group__zbus__apis.md#ga88941281d7bdd24f3cfbb53e57711d8f)enum \_\_packed [zbus\_observer\_type](group__zbus__apis.md#ga88941281d7bdd24f3cfbb53e57711d8f) {

[ 120](group__zbus__apis.md#gga88941281d7bdd24f3cfbb53e57711d8fa127f19c2121c9c512da9dbcbb301320c) [ZBUS\_OBSERVER\_LISTENER\_TYPE](group__zbus__apis.md#gga88941281d7bdd24f3cfbb53e57711d8fa127f19c2121c9c512da9dbcbb301320c),

[ 121](group__zbus__apis.md#gga88941281d7bdd24f3cfbb53e57711d8fa22c784a85353545e8dca2ce7a0ec81b3) [ZBUS\_OBSERVER\_SUBSCRIBER\_TYPE](group__zbus__apis.md#gga88941281d7bdd24f3cfbb53e57711d8fa22c784a85353545e8dca2ce7a0ec81b3),

[ 122](group__zbus__apis.md#gga88941281d7bdd24f3cfbb53e57711d8fa8151f9e58a5bd96449bd2f9f8695538c) [ZBUS\_OBSERVER\_MSG\_SUBSCRIBER\_TYPE](group__zbus__apis.md#gga88941281d7bdd24f3cfbb53e57711d8fa8151f9e58a5bd96449bd2f9f8695538c),

123};

124

[ 125](structzbus__observer__data.md)struct [zbus\_observer\_data](structzbus__observer__data.md) {

[ 127](structzbus__observer__data.md#ad16ca7a9e83f54afd75f6accf471eb91) bool [enabled](structzbus__observer__data.md#ad16ca7a9e83f54afd75f6accf471eb91);

128

129#if defined(CONFIG\_ZBUS\_PRIORITY\_BOOST)

131 int priority;

132#endif /\* CONFIG\_ZBUS\_PRIORITY\_BOOST \*/

133};

134

[ 150](structzbus__observer.md)struct [zbus\_observer](structzbus__observer.md) {

151#if defined(CONFIG\_ZBUS\_OBSERVER\_NAME) || defined(\_\_DOXYGEN\_\_)

[ 153](structzbus__observer.md#ad9d31821d69e181f28e80e5eedf5a331) const char \*[name](structzbus__observer.md#ad9d31821d69e181f28e80e5eedf5a331);

154#endif

[ 156](structzbus__observer.md#a0251cf9bdca418b6b8123b998b57efe2) enum [zbus\_observer\_type](group__zbus__apis.md#ga88941281d7bdd24f3cfbb53e57711d8f) [type](structzbus__observer.md#a0251cf9bdca418b6b8123b998b57efe2);

157

[ 159](structzbus__observer.md#abdca15310be41ea2ce1ae3bbe0ebabb7) struct [zbus\_observer\_data](structzbus__observer__data.md) \*[data](structzbus__observer.md#abdca15310be41ea2ce1ae3bbe0ebabb7);

160

161 union {

[ 163](structzbus__observer.md#ac03ca78cff09b9466cbe34921862d27c) struct [k\_msgq](structk__msgq.md) \*[queue](structzbus__observer.md#ac03ca78cff09b9466cbe34921862d27c);

164

[ 166](structzbus__observer.md#a78037ed7bcba26af33b6221bf7e4f9d2) void (\*[callback](structzbus__observer.md#a78037ed7bcba26af33b6221bf7e4f9d2))(const struct [zbus\_channel](structzbus__channel.md) \*chan);

167

168#if defined(CONFIG\_ZBUS\_MSG\_SUBSCRIBER) || defined(\_\_DOXYGEN\_\_)

[ 172](structzbus__observer.md#a3594b07a2573e03b18ca640809ffd3fa) struct [k\_fifo](structk__fifo.md) \*[message\_fifo](structzbus__observer.md#a3594b07a2573e03b18ca640809ffd3fa);

173#endif /\* CONFIG\_ZBUS\_MSG\_SUBSCRIBER \*/

174 };

175};

176

178struct zbus\_channel\_observation\_mask {

179 bool enabled;

180};

181

185struct zbus\_channel\_observation {

186 const struct zbus\_channel \*chan;

187 const struct zbus\_observer \*obs;

188};

189

190#ifdef \_\_cplusplus

191#define \_ZBUS\_CPP\_EXTERN extern

192#else

193#define \_ZBUS\_CPP\_EXTERN

194#endif /\* \_\_cplusplus \*/

195

196#define ZBUS\_MIN\_THREAD\_PRIORITY (CONFIG\_NUM\_PREEMPT\_PRIORITIES - 1)

197

198#if defined(CONFIG\_ZBUS\_ASSERT\_MOCK)

199#define \_ZBUS\_ASSERT(\_cond, \_fmt, ...) \

200 do { \

201 if (!(\_cond)) { \

202 printk("ZBUS ASSERT: "); \

203 printk(\_fmt, ##\_\_VA\_ARGS\_\_); \

204 printk("\n"); \

205 return -EFAULT; \

206 } \

207 } while (0)

208#else

209#define \_ZBUS\_ASSERT(\_cond, \_fmt, ...) \_\_ASSERT(\_cond, \_fmt, ##\_\_VA\_ARGS\_\_)

210#endif

211

212#if defined(CONFIG\_ZBUS\_CHANNEL\_NAME)

213#define ZBUS\_CHANNEL\_NAME\_INIT(\_name) .name = #\_name,

214#define \_ZBUS\_CHAN\_NAME(\_chan) (\_chan)->name

215#else

216#define ZBUS\_CHANNEL\_NAME\_INIT(\_name)

217#define \_ZBUS\_CHAN\_NAME(\_chan) ""

218#endif

219

220#if defined(CONFIG\_ZBUS\_OBSERVER\_NAME)

221#define ZBUS\_OBSERVER\_NAME\_INIT(\_name) .name = #\_name,

222#define \_ZBUS\_OBS\_NAME(\_obs) (\_obs)->name

223#else

224#define ZBUS\_OBSERVER\_NAME\_INIT(\_name)

225#define \_ZBUS\_OBS\_NAME(\_obs) ""

226#endif

227

228#if defined(CONFIG\_ZBUS\_RUNTIME\_OBSERVERS)

229#define ZBUS\_RUNTIME\_OBSERVERS\_LIST\_DECL(\_slist\_name) static sys\_slist\_t \_slist\_name

230#define ZBUS\_RUNTIME\_OBSERVERS\_LIST\_INIT(\_slist\_name) .runtime\_observers = &\_slist\_name,

231#else

232#define ZBUS\_RUNTIME\_OBSERVERS\_LIST\_DECL(\_slist\_name)

233#define ZBUS\_RUNTIME\_OBSERVERS\_LIST\_INIT(\_slist\_name) /\* No runtime observers \*/

234#endif

235

236#define \_ZBUS\_OBS\_EXTERN(\_name) extern const struct zbus\_observer \_name

237

238#define \_ZBUS\_CHAN\_EXTERN(\_name) extern const struct zbus\_channel \_name

239

240#define ZBUS\_REF(\_value) &(\_value)

241

242#define FOR\_EACH\_FIXED\_ARG\_NONEMPTY\_TERM(F, sep, fixed\_arg, ...) \

243 COND\_CODE\_0(/\* are there zero non-empty arguments ? \*/ \

244 NUM\_VA\_ARGS\_LESS\_1( \

245 LIST\_DROP\_EMPTY(\_\_VA\_ARGS\_\_, \_)), /\* if so, expand to nothing \*/ \

246 (), /\* otherwise, expand to: \*/ \

247 (FOR\_EACH\_IDX\_FIXED\_ARG( \

248 F, sep, fixed\_arg, \

249 LIST\_DROP\_EMPTY(\_\_VA\_ARGS\_\_)) /\* plus a final terminator \*/ \

250 \_\_DEBRACKET sep))

251

252#define \_ZBUS\_OBSERVATION\_PREFIX(\_idx) \

253 GET\_ARG\_N(\_idx, 00, 01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 11, 12, 13, 14, 15, 16, 17, \

254 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, \

255 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, \

256 58, 59, 60, 61, 62, 63)

257

258#define \_ZBUS\_CHAN\_OBSERVATION(\_idx, \_obs, \_chan) \

259 const STRUCT\_SECTION\_ITERABLE( \

260 zbus\_channel\_observation, \

261 \_CONCAT(\_chan, \_ZBUS\_OBSERVATION\_PREFIX(UTIL\_INC(\_idx)))) = {.chan = &\_chan, \

262 .obs = &\_obs}; \

263 STRUCT\_SECTION\_ITERABLE(zbus\_channel\_observation\_mask, \

264 \_CONCAT(\_CONCAT(\_chan, \_ZBUS\_OBSERVATION\_PREFIX(UTIL\_INC(\_idx))), \

265 \_mask)) = {.enabled = false};

266

267#if defined(CONFIG\_ZBUS\_RUNTIME\_OBSERVERS) || defined(\_\_DOXYGEN\_\_)

268#define \_ZBUS\_RUNTIME\_OBSERVERS(\_name) .observers = &(\_CONCAT(\_observers\_, \_name)),

269#define \_ZBUS\_RUNTIME\_OBSERVERS\_DECL(\_name) static sys\_slist\_t \_CONCAT(\_observers\_, \_name);

270#else

271#define \_ZBUS\_RUNTIME\_OBSERVERS(\_name)

272#define \_ZBUS\_RUNTIME\_OBSERVERS\_DECL(\_name)

273#endif /\* CONFIG\_ZBUS\_RUNTIME\_OBSERVERS \*/

274

275#define \_ZBUS\_MESSAGE\_NAME(\_name) \_CONCAT(\_zbus\_message\_, \_name)

276

277/\* clang-format off \*/

278#define \_ZBUS\_CHAN\_DEFINE(\_name, \_id, \_type, \_validator, \_user\_data) \

279 static struct zbus\_channel\_data \_CONCAT(\_zbus\_chan\_data\_, \_name) = { \

280 .observers\_start\_idx = -1, \

281 .observers\_end\_idx = -1, \

282 .sem = Z\_SEM\_INITIALIZER(\_CONCAT(\_zbus\_chan\_data\_, \_name).sem, 1, 1), \

283 IF\_ENABLED(CONFIG\_ZBUS\_PRIORITY\_BOOST, \

284 (.highest\_observer\_priority = ZBUS\_MIN\_THREAD\_PRIORITY,)) \

285 IF\_ENABLED(CONFIG\_ZBUS\_RUNTIME\_OBSERVERS, \

286 (.observers = SYS\_SLIST\_STATIC\_INIT( \

287 &\_CONCAT(\_zbus\_chan\_data\_, \_name).observers),)) \

288 }; \

289 static K\_MUTEX\_DEFINE(\_CONCAT(\_zbus\_mutex\_, \_name)); \

290 \_ZBUS\_CPP\_EXTERN const STRUCT\_SECTION\_ITERABLE(zbus\_channel, \_name) = { \

291 ZBUS\_CHANNEL\_NAME\_INIT(\_name) /\* Maybe removed \*/ \

292 IF\_ENABLED(CONFIG\_ZBUS\_CHANNEL\_ID, (.id = \_id,)) \

293 .message = &\_ZBUS\_MESSAGE\_NAME(\_name), \

294 .message\_size = sizeof(\_type), \

295 .user\_data = \_user\_data, \

296 .validator = \_validator, \

297 .data = &\_CONCAT(\_zbus\_chan\_data\_, \_name), \

298 IF\_ENABLED(ZBUS\_MSG\_SUBSCRIBER\_NET\_BUF\_POOL\_ISOLATION, \

299 (.msg\_subscriber\_pool = &\_zbus\_msg\_subscribers\_pool,)) \

300 }

301/\* clang-format on \*/

302

304

305/\* clang-format off \*/

306

[ 318](group__zbus__apis.md#ga7f763caca474e6c910793d2c714f80b4)#define ZBUS\_CHAN\_ADD\_OBS\_WITH\_MASK(\_chan, \_obs, \_masked, \_prio) \

319 const STRUCT\_SECTION\_ITERABLE(zbus\_channel\_observation, \

320 \_CONCAT(\_CONCAT(\_chan, zz), \_CONCAT(\_prio, \_obs))) = { \

321 .chan = &\_chan, \

322 .obs = &\_obs, \

323 }; \

324 STRUCT\_SECTION\_ITERABLE(zbus\_channel\_observation\_mask, \

325 \_CONCAT(\_CONCAT(\_CONCAT(\_chan, zz), \_CONCAT(\_prio, \_obs)), \

326 \_mask)) = {.enabled = \_masked}

327/\* clang-format on \*/

328

[ 339](group__zbus__apis.md#gaf63215f3f53741edf52b4d0d7b2b97df)#define ZBUS\_CHAN\_ADD\_OBS(\_chan, \_obs, \_prio) ZBUS\_CHAN\_ADD\_OBS\_WITH\_MASK(\_chan, \_obs, false, \_prio)

340

[ 346](group__zbus__apis.md#ga49f169c6d50a3bad57e1b319362d2924)#define ZBUS\_OBS\_DECLARE(...) FOR\_EACH\_NONEMPTY\_TERM(\_ZBUS\_OBS\_EXTERN, (;), \_\_VA\_ARGS\_\_)

347

[ 353](group__zbus__apis.md#ga0662b2db8077a8075c07a3afd0161d0f)#define ZBUS\_CHAN\_DECLARE(...) FOR\_EACH(\_ZBUS\_CHAN\_EXTERN, (;), \_\_VA\_ARGS\_\_)

354

[ 359](group__zbus__apis.md#ga763dad07a1ae9bb38f9c240e1920caef)#define ZBUS\_OBSERVERS\_EMPTY

360

[ 366](group__zbus__apis.md#gafed25f045c3b8d438daf4ebd5e517692)#define ZBUS\_OBSERVERS(...) \_\_VA\_ARGS\_\_

367

[ 372](group__zbus__apis.md#ga1f1e0798856c54dd641c1a322789400b)#define ZBUS\_CHAN\_ID\_INVALID UINT32\_MAX

373

[ 389](group__zbus__apis.md#ga29a3a39e5c78a34b2d8491615d1f0687)#define ZBUS\_CHAN\_DEFINE(\_name, \_type, \_validator, \_user\_data, \_observers, \_init\_val) \

390 static \_type \_ZBUS\_MESSAGE\_NAME(\_name) = \_init\_val; \

391 \_ZBUS\_CHAN\_DEFINE(\_name, ZBUS\_CHAN\_ID\_INVALID, \_type, \_validator, \_user\_data); \

392 /\* Extern declaration of observers \*/ \

393 ZBUS\_OBS\_DECLARE(\_observers); \

394 /\* Create all channel observations from observers list \*/ \

395 FOR\_EACH\_FIXED\_ARG\_NONEMPTY\_TERM(\_ZBUS\_CHAN\_OBSERVATION, (;), \_name, \_observers)

396

[ 413](group__zbus__apis.md#ga7c49cba434b90d417859b37722843e5f)#define ZBUS\_CHAN\_DEFINE\_WITH\_ID(\_name, \_id, \_type, \_validator, \_user\_data, \_observers, \_init\_val) \

414 static \_type \_ZBUS\_MESSAGE\_NAME(\_name) = \_init\_val; \

415 \_ZBUS\_CHAN\_DEFINE(\_name, \_id, \_type, \_validator, \_user\_data); \

416 /\* Extern declaration of observers \*/ \

417 ZBUS\_OBS\_DECLARE(\_observers); \

418 /\* Create all channel observations from observers list \*/ \

419 FOR\_EACH\_FIXED\_ARG\_NONEMPTY\_TERM(\_ZBUS\_CHAN\_OBSERVATION, (;), \_name, \_observers)

420

[ 430](group__zbus__apis.md#ga4bf8c445814c1fcee9b9819a36bc9bd6)#define ZBUS\_MSG\_INIT(\_val, ...) {\_val, ##\_\_VA\_ARGS\_\_}

431

432/\* clang-format off \*/

433

[ 445](group__zbus__apis.md#gaf56f71babe2bb27258f025332b80c58f)#define ZBUS\_SUBSCRIBER\_DEFINE\_WITH\_ENABLE(\_name, \_queue\_size, \_enable) \

446 K\_MSGQ\_DEFINE(\_zbus\_observer\_queue\_##\_name, \

447 sizeof(struct zbus\_channel \*), \

448 \_queue\_size, sizeof(struct zbus\_channel \*) \

449 ); \

450 static struct zbus\_observer\_data \_CONCAT(\_zbus\_obs\_data\_, \_name) = { \

451 .enabled = \_enable, \

452 IF\_ENABLED(CONFIG\_ZBUS\_PRIORITY\_BOOST, ( \

453 .priority = ZBUS\_MIN\_THREAD\_PRIORITY, \

454 )) \

455 }; \

456 \_ZBUS\_CPP\_EXTERN const STRUCT\_SECTION\_ITERABLE(zbus\_observer, \_name) = { \

457 ZBUS\_OBSERVER\_NAME\_INIT(\_name) /\* Name field \*/ \

458 .type = ZBUS\_OBSERVER\_SUBSCRIBER\_TYPE, \

459 .data = &\_CONCAT(\_zbus\_obs\_data\_, \_name), \

460 .queue = &\_zbus\_observer\_queue\_##\_name, \

461 }

462/\* clang-format on \*/

463

[ 475](group__zbus__apis.md#gac17a735cccecfc90f26127e48cf6279a)#define ZBUS\_SUBSCRIBER\_DEFINE(\_name, \_queue\_size) \

476 ZBUS\_SUBSCRIBER\_DEFINE\_WITH\_ENABLE(\_name, \_queue\_size, true)

477

478/\* clang-format off \*/

479

[ 491](group__zbus__apis.md#gace4ac9da0e1bab7ba72797783ded948f)#define ZBUS\_LISTENER\_DEFINE\_WITH\_ENABLE(\_name, \_cb, \_enable) \

492 static struct zbus\_observer\_data \_CONCAT(\_zbus\_obs\_data\_, \_name) = { \

493 .enabled = \_enable, \

494 IF\_ENABLED(CONFIG\_ZBUS\_PRIORITY\_BOOST, ( \

495 .priority = ZBUS\_MIN\_THREAD\_PRIORITY, \

496 )) \

497 }; \

498 \_ZBUS\_CPP\_EXTERN const STRUCT\_SECTION\_ITERABLE(zbus\_observer, \_name) = { \

499 ZBUS\_OBSERVER\_NAME\_INIT(\_name) /\* Name field \*/ \

500 .type = ZBUS\_OBSERVER\_LISTENER\_TYPE, \

501 .data = &\_CONCAT(\_zbus\_obs\_data\_, \_name), \

502 .callback = (\_cb) \

503 }

504/\* clang-format on \*/

505

[ 516](group__zbus__apis.md#gabfc7be8298e76fe2f7ae628be30b8390)#define ZBUS\_LISTENER\_DEFINE(\_name, \_cb) ZBUS\_LISTENER\_DEFINE\_WITH\_ENABLE(\_name, \_cb, true)

517

518/\* clang-format off \*/

519

[ 530](group__zbus__apis.md#ga6089c1ae0dad91306f79d48a63b31785)#define ZBUS\_MSG\_SUBSCRIBER\_DEFINE\_WITH\_ENABLE(\_name, \_enable) \

531 static K\_FIFO\_DEFINE(\_zbus\_observer\_fifo\_##\_name); \

532 static struct zbus\_observer\_data \_CONCAT(\_zbus\_obs\_data\_, \_name) = { \

533 .enabled = \_enable, \

534 IF\_ENABLED(CONFIG\_ZBUS\_PRIORITY\_BOOST, ( \

535 .priority = ZBUS\_MIN\_THREAD\_PRIORITY, \

536 )) \

537 }; \

538 \_ZBUS\_CPP\_EXTERN const STRUCT\_SECTION\_ITERABLE(zbus\_observer, \_name) = { \

539 ZBUS\_OBSERVER\_NAME\_INIT(\_name) /\* Name field \*/ \

540 .type = ZBUS\_OBSERVER\_MSG\_SUBSCRIBER\_TYPE, \

541 .data = &\_CONCAT(\_zbus\_obs\_data\_, \_name), \

542 .message\_fifo = &\_zbus\_observer\_fifo\_##\_name, \

543 }

544/\* clang-format on \*/

545

[ 557](group__zbus__apis.md#ga07a0c2c428c9e4891e86a63a420b2268)#define ZBUS\_MSG\_SUBSCRIBER\_DEFINE(\_name) ZBUS\_MSG\_SUBSCRIBER\_DEFINE\_WITH\_ENABLE(\_name, true)

[ 579](group__zbus__apis.md#gadfcaba65b397c1d8c31836ef3cf61244)int [zbus\_chan\_pub](group__zbus__apis.md#gadfcaba65b397c1d8c31836ef3cf61244)(const struct [zbus\_channel](structzbus__channel.md) \*chan, const void \*msg, [k\_timeout\_t](structk__timeout__t.md) timeout);

580

[ 598](group__zbus__apis.md#ga8209721e0a295c84d112ba1a7171100e)int [zbus\_chan\_read](group__zbus__apis.md#ga8209721e0a295c84d112ba1a7171100e)(const struct [zbus\_channel](structzbus__channel.md) \*chan, void \*msg, [k\_timeout\_t](structk__timeout__t.md) timeout);

599

[ 621](group__zbus__apis.md#ga00bfb7db54594029f4d288bcf5b56b3a)int [zbus\_chan\_claim](group__zbus__apis.md#ga00bfb7db54594029f4d288bcf5b56b3a)(const struct [zbus\_channel](structzbus__channel.md) \*chan, [k\_timeout\_t](structk__timeout__t.md) timeout);

622

[ 637](group__zbus__apis.md#ga74747affb345e68ce1d564c349409e59)int [zbus\_chan\_finish](group__zbus__apis.md#ga74747affb345e68ce1d564c349409e59)(const struct [zbus\_channel](structzbus__channel.md) \*chan);

638

[ 657](group__zbus__apis.md#ga6ec2f463801499e23a011fa4e68aa3e7)int [zbus\_chan\_notify](group__zbus__apis.md#ga6ec2f463801499e23a011fa4e68aa3e7)(const struct [zbus\_channel](structzbus__channel.md) \*chan, [k\_timeout\_t](structk__timeout__t.md) timeout);

658

659#if defined(CONFIG\_ZBUS\_CHANNEL\_NAME) || defined(\_\_DOXYGEN\_\_)

660

[ 670](group__zbus__apis.md#ga05a220636fc6bb58b97805e558b76d73)static inline const char \*[zbus\_chan\_name](group__zbus__apis.md#ga05a220636fc6bb58b97805e558b76d73)(const struct [zbus\_channel](structzbus__channel.md) \*chan)

671{

672 \_\_ASSERT(chan != [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4), "chan is required");

673

674 return chan->[name](structzbus__channel.md#ab8e66cdcfd2429058ca86e6af3813e03);

675}

676

677#endif

678

679#if defined(CONFIG\_ZBUS\_CHANNEL\_ID) || defined(\_\_DOXYGEN\_\_)

680

[ 689](group__zbus__apis.md#gacef06cf9818ab91be97d45ab5f58a4a3)const struct [zbus\_channel](structzbus__channel.md) \*[zbus\_chan\_from\_id](group__zbus__apis.md#gacef06cf9818ab91be97d45ab5f58a4a3)([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel\_id);

690

691#endif

692

[ 705](group__zbus__apis.md#gaaf8b34113b7b993438bd42db64812572)static inline void \*[zbus\_chan\_msg](group__zbus__apis.md#gaaf8b34113b7b993438bd42db64812572)(const struct [zbus\_channel](structzbus__channel.md) \*chan)

706{

707 \_\_ASSERT(chan != [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4), "chan is required");

708

709 return chan->[message](structzbus__channel.md#abc00c2ed80b4ce3a0ea7304f43f30d08);

710}

711

[ 726](group__zbus__apis.md#gafee07c355df9ac86b85e601196b56a10)static inline const void \*[zbus\_chan\_const\_msg](group__zbus__apis.md#gafee07c355df9ac86b85e601196b56a10)(const struct [zbus\_channel](structzbus__channel.md) \*chan)

727{

728 \_\_ASSERT(chan != [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4), "chan is required");

729

730 return chan->[message](structzbus__channel.md#abc00c2ed80b4ce3a0ea7304f43f30d08);

731}

732

[ 742](group__zbus__apis.md#ga8895a18b282ca2fe7528b4e5cf48e025)static inline [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [zbus\_chan\_msg\_size](group__zbus__apis.md#ga8895a18b282ca2fe7528b4e5cf48e025)(const struct [zbus\_channel](structzbus__channel.md) \*chan)

743{

744 \_\_ASSERT(chan != [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4), "chan is required");

745

746 return chan->[message\_size](structzbus__channel.md#ab7f330f3d70774afeebb74cc03f90d34);

747}

748

[ 758](group__zbus__apis.md#gac0b0ed0356fca5a8b65a3332931a369a)static inline void \*[zbus\_chan\_user\_data](group__zbus__apis.md#gac0b0ed0356fca5a8b65a3332931a369a)(const struct [zbus\_channel](structzbus__channel.md) \*chan)

759{

760 \_\_ASSERT(chan != [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4), "chan is required");

761

762 return chan->[user\_data](structzbus__channel.md#a34864d7da9816955a41caf2a8355f3f0);

763}

764

765#if defined(CONFIG\_ZBUS\_MSG\_SUBSCRIBER\_NET\_BUF\_POOL\_ISOLATION) || defined(\_\_DOXYGEN\_\_)

766

[ 773](group__zbus__apis.md#ga3f90d50f20e7779ef257676ac10da357)static inline void [zbus\_chan\_set\_msg\_sub\_pool](group__zbus__apis.md#ga3f90d50f20e7779ef257676ac10da357)(const struct [zbus\_channel](structzbus__channel.md) \*chan,

774 struct [net\_buf\_pool](structnet__buf__pool.md) \*pool)

775{

776 \_\_ASSERT(chan != [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4), "chan is required");

777 \_\_ASSERT(pool != [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4), "pool is required");

778

779 chan->[data](structzbus__channel.md#a5588983f2aefce2dd7cffad564c68d16)->[msg\_subscriber\_pool](structzbus__channel__data.md#a2490c05755696b7ba1f1f1392d27845f) = pool;

780}

781

782#endif /\* ZBUS\_MSG\_SUBSCRIBER\_NET\_BUF\_POOL\_ISOLATION \*/

783

784#if defined(CONFIG\_ZBUS\_CHANNEL\_PUBLISH\_STATS) || defined(\_\_DOXYGEN\_\_)

785

[ 797](group__zbus__apis.md#gaef067fb1e8b834993662af84b916483a)static inline void [zbus\_chan\_pub\_stats\_update](group__zbus__apis.md#gaef067fb1e8b834993662af84b916483a)(const struct [zbus\_channel](structzbus__channel.md) \*chan)

798{

799 \_\_ASSERT(chan != [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4), "chan is required");

800

801 chan->[data](structzbus__channel.md#a5588983f2aefce2dd7cffad564c68d16)->[publish\_timestamp](structzbus__channel__data.md#a1d75cb7c16798b5ef907f92a51ed7f63) = [k\_uptime\_ticks](group__clock__apis.md#ga8f143af2ee4ad42d9f7817ef161cbd13)();

802 chan->[data](structzbus__channel.md#a5588983f2aefce2dd7cffad564c68d16)->[publish\_count](structzbus__channel__data.md#a45172a94503b0005d662567c5cc8c97f) += 1;

803}

804

[ 814](group__zbus__apis.md#gac5dff9990d709d736b30f36d68c0297b)static inline [k\_ticks\_t](group__clock__apis.md#ga9832cb0adc2d1866420e5c370a0863e2) [zbus\_chan\_pub\_stats\_last\_time](group__zbus__apis.md#gac5dff9990d709d736b30f36d68c0297b)(const struct [zbus\_channel](structzbus__channel.md) \*chan)

815{

816 \_\_ASSERT(chan != [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4), "chan is required");

817

818 return chan->[data](structzbus__channel.md#a5588983f2aefce2dd7cffad564c68d16)->[publish\_timestamp](structzbus__channel__data.md#a1d75cb7c16798b5ef907f92a51ed7f63);

819}

820

[ 830](group__zbus__apis.md#ga5648bf527de4aff89648a34bf8a7539a)static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [zbus\_chan\_pub\_stats\_count](group__zbus__apis.md#ga5648bf527de4aff89648a34bf8a7539a)(const struct [zbus\_channel](structzbus__channel.md) \*chan)

831{

832 \_\_ASSERT(chan != [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4), "chan is required");

833

834 return chan->[data](structzbus__channel.md#a5588983f2aefce2dd7cffad564c68d16)->[publish\_count](structzbus__channel__data.md#a45172a94503b0005d662567c5cc8c97f);

835}

836

[ 846](group__zbus__apis.md#ga09503e2b9c01f79136f9eb600ddb3f31)static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [zbus\_chan\_pub\_stats\_avg\_period](group__zbus__apis.md#ga09503e2b9c01f79136f9eb600ddb3f31)(const struct [zbus\_channel](structzbus__channel.md) \*chan)

847{

848 \_\_ASSERT(chan != [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4), "chan is required");

849

850 /\* Not yet published, period = 0ms \*/

851 if (chan->[data](structzbus__channel.md#a5588983f2aefce2dd7cffad564c68d16)->[publish\_count](structzbus__channel__data.md#a45172a94503b0005d662567c5cc8c97f) == 0) {

852 return 0;

853 }

854 /\* Average period across application runtime \*/

855 return [k\_uptime\_get](group__clock__apis.md#gae3e992cd3257c23d5b26d765fcbb2b69)() / chan->[data](structzbus__channel.md#a5588983f2aefce2dd7cffad564c68d16)->[publish\_count](structzbus__channel__data.md#a45172a94503b0005d662567c5cc8c97f);

856}

857

858#else

859

860static inline void [zbus\_chan\_pub\_stats\_update](group__zbus__apis.md#gaef067fb1e8b834993662af84b916483a)(const struct [zbus\_channel](structzbus__channel.md) \*chan)

861{

862 (void)chan;

863}

864

865#endif /\* CONFIG\_ZBUS\_CHANNEL\_PUBLISH\_STATS \*/

866

867#if defined(CONFIG\_ZBUS\_RUNTIME\_OBSERVERS) || defined(\_\_DOXYGEN\_\_)

868

[ 873](structzbus__observer__node.md)struct [zbus\_observer\_node](structzbus__observer__node.md) {

[ 874](structzbus__observer__node.md#af2beaa501ed02f30752189a69219746b) [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) [node](structzbus__observer__node.md#af2beaa501ed02f30752189a69219746b);

[ 875](structzbus__observer__node.md#a9d9c6843db5c9bab9a8354929f769c75) const struct [zbus\_observer](structzbus__observer.md) \*[obs](structzbus__observer__node.md#a9d9c6843db5c9bab9a8354929f769c75);

876#if defined(CONFIG\_ZBUS\_RUNTIME\_OBSERVERS\_NODE\_ALLOC\_NONE)

877 const struct [zbus\_channel](structzbus__channel.md) \*chan;

878#endif

879};

880

881#if defined(CONFIG\_ZBUS\_RUNTIME\_OBSERVERS\_NODE\_ALLOC\_NONE) || defined(\_\_DOXYGEN\_\_)

[ 901](group__zbus__apis.md#ga6f2b8db3a13546e3d0fd095ff9cd37ba)int [zbus\_chan\_add\_obs\_with\_node](group__zbus__apis.md#ga6f2b8db3a13546e3d0fd095ff9cd37ba)(const struct [zbus\_channel](structzbus__channel.md) \*chan, const struct [zbus\_observer](structzbus__observer.md) \*obs,

902 struct [zbus\_observer\_node](structzbus__observer__node.md) \*node, [k\_timeout\_t](structk__timeout__t.md) timeout);

903#else

904static inline int [zbus\_chan\_add\_obs\_with\_node](group__zbus__apis.md#ga6f2b8db3a13546e3d0fd095ff9cd37ba)(const struct [zbus\_channel](structzbus__channel.md) \*chan,

905 const struct [zbus\_observer](structzbus__observer.md) \*obs,

906 struct [zbus\_observer\_node](structzbus__observer__node.md) \*node, [k\_timeout\_t](structk__timeout__t.md) timeout)

907{

908 ARG\_UNUSED(chan);

909 ARG\_UNUSED(obs);

910 ARG\_UNUSED(node);

911 ARG\_UNUSED(timeout);

912

913 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

914}

915#endif /\* CONFIG\_ZBUS\_RUNTIME\_OBSERVERS\_NODE\_ALLOC\_NONE \*/

916

917#if !defined(CONFIG\_ZBUS\_RUNTIME\_OBSERVERS\_NODE\_ALLOC\_NONE) || defined(\_\_DOXYGEN\_\_)

[ 938](group__zbus__apis.md#gaddd8ce480bc29ead4442e529915cfbf6)int [zbus\_chan\_add\_obs](group__zbus__apis.md#gaddd8ce480bc29ead4442e529915cfbf6)(const struct [zbus\_channel](structzbus__channel.md) \*chan, const struct [zbus\_observer](structzbus__observer.md) \*obs,

939 [k\_timeout\_t](structk__timeout__t.md) timeout);

940#else

941static inline int [zbus\_chan\_add\_obs](group__zbus__apis.md#gaddd8ce480bc29ead4442e529915cfbf6)(const struct [zbus\_channel](structzbus__channel.md) \*chan,

942 const struct [zbus\_observer](structzbus__observer.md) \*obs, [k\_timeout\_t](structk__timeout__t.md) timeout)

943{

944 ARG\_UNUSED(chan);

945 ARG\_UNUSED(obs);

946 ARG\_UNUSED(timeout);

947

948 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

949}

950

951#endif /\* !CONFIG\_ZBUS\_RUNTIME\_OBSERVERS\_NODE\_ALLOC\_NONE \*/

[ 967](group__zbus__apis.md#gaee11d7472a3f87156b8ef1dcfbe897c4)int [zbus\_chan\_rm\_obs](group__zbus__apis.md#gaee11d7472a3f87156b8ef1dcfbe897c4)(const struct [zbus\_channel](structzbus__channel.md) \*chan, const struct [zbus\_observer](structzbus__observer.md) \*obs,

968 [k\_timeout\_t](structk__timeout__t.md) timeout);

969

970#endif /\* CONFIG\_ZBUS\_RUNTIME\_OBSERVERS \*/

971

[ 985](group__zbus__apis.md#ga96767314e040e42609867a36684a6349)int [zbus\_obs\_set\_enable](group__zbus__apis.md#ga96767314e040e42609867a36684a6349)(const struct [zbus\_observer](structzbus__observer.md) \*obs, bool enabled);

986

[ 997](group__zbus__apis.md#ga315fd4e0b6a3c01a23307dd890e69894)static inline int [zbus\_obs\_is\_enabled](group__zbus__apis.md#ga315fd4e0b6a3c01a23307dd890e69894)(const struct [zbus\_observer](structzbus__observer.md) \*obs, bool \*enable)

998{

999 \_ZBUS\_ASSERT(obs != [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4), "obs is required");

1000 \_ZBUS\_ASSERT(enable != [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4), "enable is required");

1001

1002 \*enable = obs->[data](structzbus__observer.md#abdca15310be41ea2ce1ae3bbe0ebabb7)->[enabled](structzbus__observer__data.md#ad16ca7a9e83f54afd75f6accf471eb91);

1003

1004 return 0;

1005}

1006

[ 1021](group__zbus__apis.md#ga9513264f912f54b60c4341642f578e5a)int [zbus\_obs\_set\_chan\_notification\_mask](group__zbus__apis.md#ga9513264f912f54b60c4341642f578e5a)(const struct [zbus\_observer](structzbus__observer.md) \*obs,

1022 const struct [zbus\_channel](structzbus__channel.md) \*chan, bool masked);

1023

[ 1036](group__zbus__apis.md#ga41ae9799a52c2a7954500b0a3c78d19f)int [zbus\_obs\_is\_chan\_notification\_masked](group__zbus__apis.md#ga41ae9799a52c2a7954500b0a3c78d19f)(const struct [zbus\_observer](structzbus__observer.md) \*obs,

1037 const struct [zbus\_channel](structzbus__channel.md) \*chan, bool \*masked);

1038

1039#if defined(CONFIG\_ZBUS\_OBSERVER\_NAME) || defined(\_\_DOXYGEN\_\_)

1040

[ 1050](group__zbus__apis.md#ga5bb33ec5b914e6cbc87fa70bf763ad15)static inline const char \*[zbus\_obs\_name](group__zbus__apis.md#ga5bb33ec5b914e6cbc87fa70bf763ad15)(const struct [zbus\_observer](structzbus__observer.md) \*obs)

1051{

1052 \_\_ASSERT(obs != [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4), "obs is required");

1053

1054 return obs->[name](structzbus__observer.md#ad9d31821d69e181f28e80e5eedf5a331);

1055}

1056

1057#endif

1058

1059#if defined(CONFIG\_ZBUS\_PRIORITY\_BOOST) || defined(\_\_DOXYGEN\_\_)

1060

[ 1070](group__zbus__apis.md#gabecf160e4d468d0275ad79e22fd0fb5b)int [zbus\_obs\_attach\_to\_thread](group__zbus__apis.md#gabecf160e4d468d0275ad79e22fd0fb5b)(const struct [zbus\_observer](structzbus__observer.md) \*obs);

1071

[ 1081](group__zbus__apis.md#ga493c125c31e44d5a222f0e9c6d01249e)int [zbus\_obs\_detach\_from\_thread](group__zbus__apis.md#ga493c125c31e44d5a222f0e9c6d01249e)(const struct [zbus\_observer](structzbus__observer.md) \*obs);

1082

1083#endif /\* CONFIG\_ZBUS\_PRIORITY\_BOOST \*/

1084

[ 1103](group__zbus__apis.md#ga84a65e276a01ef97eeb5c81b880da72b)int [zbus\_sub\_wait](group__zbus__apis.md#ga84a65e276a01ef97eeb5c81b880da72b)(const struct [zbus\_observer](structzbus__observer.md) \*sub, const struct [zbus\_channel](structzbus__channel.md) \*\*chan,

1104 [k\_timeout\_t](structk__timeout__t.md) timeout);

1105

1106#if defined(CONFIG\_ZBUS\_MSG\_SUBSCRIBER) || defined(\_\_DOXYGEN\_\_)

1107

[ 1126](group__zbus__apis.md#gaeffce45446509e488192a4e6442453fb)int [zbus\_sub\_wait\_msg](group__zbus__apis.md#gaeffce45446509e488192a4e6442453fb)(const struct [zbus\_observer](structzbus__observer.md) \*sub, const struct [zbus\_channel](structzbus__channel.md) \*\*chan, void \*msg,

1127 [k\_timeout\_t](structk__timeout__t.md) timeout);

1128

1129#endif /\* CONFIG\_ZBUS\_MSG\_SUBSCRIBER \*/

1130

[ 1144](group__zbus__apis.md#ga6dffd25f4eb368e773c2bd55f34a0e10)bool [zbus\_iterate\_over\_channels](group__zbus__apis.md#ga6dffd25f4eb368e773c2bd55f34a0e10)(bool (\*iterator\_func)(const struct [zbus\_channel](structzbus__channel.md) \*chan));

[ 1159](group__zbus__apis.md#gab8df108b0238757ff631ec1e120fa2c3)bool [zbus\_iterate\_over\_channels\_with\_user\_data](group__zbus__apis.md#gab8df108b0238757ff631ec1e120fa2c3)(

1160 bool (\*iterator\_func)(const struct [zbus\_channel](structzbus__channel.md) \*chan, void \*[user\_data](structzbus__channel.md#a34864d7da9816955a41caf2a8355f3f0)), void \*[user\_data](structzbus__channel.md#a34864d7da9816955a41caf2a8355f3f0));

1161

[ 1175](group__zbus__apis.md#ga2fa50316993afc5807e9d707d664be14)bool [zbus\_iterate\_over\_observers](group__zbus__apis.md#ga2fa50316993afc5807e9d707d664be14)(bool (\*iterator\_func)(const struct [zbus\_observer](structzbus__observer.md) \*obs));

[ 1190](group__zbus__apis.md#ga2f4e39c500fed0a6bcfedb5dec3f797a)bool [zbus\_iterate\_over\_observers\_with\_user\_data](group__zbus__apis.md#ga2f4e39c500fed0a6bcfedb5dec3f797a)(

1191 bool (\*iterator\_func)(const struct [zbus\_observer](structzbus__observer.md) \*obs, void \*[user\_data](structzbus__channel.md#a34864d7da9816955a41caf2a8355f3f0)), void \*[user\_data](structzbus__channel.md#a34864d7da9816955a41caf2a8355f3f0));

1192

1196

1197#ifdef \_\_cplusplus

1198}

1199#endif

1200

1201#endif /\* ZEPHYR\_INCLUDE\_ZBUS\_H\_ \*/

[k\_uptime\_ticks](group__clock__apis.md#ga8f143af2ee4ad42d9f7817ef161cbd13)

int64\_t k\_uptime\_ticks(void)

Get system uptime, in system ticks.

[k\_ticks\_t](group__clock__apis.md#ga9832cb0adc2d1866420e5c370a0863e2)

uint32\_t k\_ticks\_t

Tick precision used in timeout APIs.

**Definition** clock.h:48

[k\_uptime\_get](group__clock__apis.md#gae3e992cd3257c23d5b26d765fcbb2b69)

static int64\_t k\_uptime\_get(void)

Get system uptime.

**Definition** kernel.h:1883

[sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8)

struct \_slist sys\_slist\_t

Single-linked list structure.

**Definition** slist.h:49

[sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493)

struct \_snode sys\_snode\_t

Single-linked list node structure.

**Definition** slist.h:39

[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33)

#define ENOTSUP

Unsupported value.

**Definition** errno.h:114

[zbus\_chan\_claim](group__zbus__apis.md#ga00bfb7db54594029f4d288bcf5b56b3a)

int zbus\_chan\_claim(const struct zbus\_channel \*chan, k\_timeout\_t timeout)

Claim a channel.

[zbus\_chan\_name](group__zbus__apis.md#ga05a220636fc6bb58b97805e558b76d73)

static const char \* zbus\_chan\_name(const struct zbus\_channel \*chan)

Get the channel's name.

**Definition** zbus.h:670

[zbus\_chan\_pub\_stats\_avg\_period](group__zbus__apis.md#ga09503e2b9c01f79136f9eb600ddb3f31)

static uint32\_t zbus\_chan\_pub\_stats\_avg\_period(const struct zbus\_channel \*chan)

Get the average period between publishes to a channel.

**Definition** zbus.h:846

[zbus\_iterate\_over\_observers\_with\_user\_data](group__zbus__apis.md#ga2f4e39c500fed0a6bcfedb5dec3f797a)

bool zbus\_iterate\_over\_observers\_with\_user\_data(bool(\*iterator\_func)(const struct zbus\_observer \*obs, void \*user\_data), void \*user\_data)

Iterate over observers with user data.

[zbus\_iterate\_over\_observers](group__zbus__apis.md#ga2fa50316993afc5807e9d707d664be14)

bool zbus\_iterate\_over\_observers(bool(\*iterator\_func)(const struct zbus\_observer \*obs))

Iterate over observers.

[zbus\_obs\_is\_enabled](group__zbus__apis.md#ga315fd4e0b6a3c01a23307dd890e69894)

static int zbus\_obs\_is\_enabled(const struct zbus\_observer \*obs, bool \*enable)

Get the observer state.

**Definition** zbus.h:997

[zbus\_chan\_set\_msg\_sub\_pool](group__zbus__apis.md#ga3f90d50f20e7779ef257676ac10da357)

static void zbus\_chan\_set\_msg\_sub\_pool(const struct zbus\_channel \*chan, struct net\_buf\_pool \*pool)

Set the channel's msg subscriber net\_buf pool.

**Definition** zbus.h:773

[zbus\_obs\_is\_chan\_notification\_masked](group__zbus__apis.md#ga41ae9799a52c2a7954500b0a3c78d19f)

int zbus\_obs\_is\_chan\_notification\_masked(const struct zbus\_observer \*obs, const struct zbus\_channel \*chan, bool \*masked)

Get the notifications masking state from a channel to an observer.

[zbus\_obs\_detach\_from\_thread](group__zbus__apis.md#ga493c125c31e44d5a222f0e9c6d01249e)

int zbus\_obs\_detach\_from\_thread(const struct zbus\_observer \*obs)

Clear the observer thread priority by detaching it from a thread.

[zbus\_chan\_pub\_stats\_count](group__zbus__apis.md#ga5648bf527de4aff89648a34bf8a7539a)

static uint32\_t zbus\_chan\_pub\_stats\_count(const struct zbus\_channel \*chan)

Get the number of times a channel has been published to.

**Definition** zbus.h:830

[zbus\_obs\_name](group__zbus__apis.md#ga5bb33ec5b914e6cbc87fa70bf763ad15)

static const char \* zbus\_obs\_name(const struct zbus\_observer \*obs)

Get the observer's name.

**Definition** zbus.h:1050

[zbus\_iterate\_over\_channels](group__zbus__apis.md#ga6dffd25f4eb368e773c2bd55f34a0e10)

bool zbus\_iterate\_over\_channels(bool(\*iterator\_func)(const struct zbus\_channel \*chan))

Iterate over channels.

[zbus\_chan\_notify](group__zbus__apis.md#ga6ec2f463801499e23a011fa4e68aa3e7)

int zbus\_chan\_notify(const struct zbus\_channel \*chan, k\_timeout\_t timeout)

Force a channel notification.

[zbus\_chan\_add\_obs\_with\_node](group__zbus__apis.md#ga6f2b8db3a13546e3d0fd095ff9cd37ba)

int zbus\_chan\_add\_obs\_with\_node(const struct zbus\_channel \*chan, const struct zbus\_observer \*obs, struct zbus\_observer\_node \*node, k\_timeout\_t timeout)

Add an observer to a channel.

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

**Definition** zbus.h:119

[zbus\_chan\_msg\_size](group__zbus__apis.md#ga8895a18b282ca2fe7528b4e5cf48e025)

static uint16\_t zbus\_chan\_msg\_size(const struct zbus\_channel \*chan)

Get the channel's message size.

**Definition** zbus.h:742

[zbus\_obs\_set\_chan\_notification\_mask](group__zbus__apis.md#ga9513264f912f54b60c4341642f578e5a)

int zbus\_obs\_set\_chan\_notification\_mask(const struct zbus\_observer \*obs, const struct zbus\_channel \*chan, bool masked)

Mask notifications from a channel to an observer.

[zbus\_obs\_set\_enable](group__zbus__apis.md#ga96767314e040e42609867a36684a6349)

int zbus\_obs\_set\_enable(const struct zbus\_observer \*obs, bool enabled)

Change the observer state.

[zbus\_chan\_msg](group__zbus__apis.md#gaaf8b34113b7b993438bd42db64812572)

static void \* zbus\_chan\_msg(const struct zbus\_channel \*chan)

Get the reference for a channel message directly.

**Definition** zbus.h:705

[zbus\_iterate\_over\_channels\_with\_user\_data](group__zbus__apis.md#gab8df108b0238757ff631ec1e120fa2c3)

bool zbus\_iterate\_over\_channels\_with\_user\_data(bool(\*iterator\_func)(const struct zbus\_channel \*chan, void \*user\_data), void \*user\_data)

Iterate over channels with user data.

[zbus\_obs\_attach\_to\_thread](group__zbus__apis.md#gabecf160e4d468d0275ad79e22fd0fb5b)

int zbus\_obs\_attach\_to\_thread(const struct zbus\_observer \*obs)

Set the observer thread priority by attaching it to a thread.

[zbus\_chan\_user\_data](group__zbus__apis.md#gac0b0ed0356fca5a8b65a3332931a369a)

static void \* zbus\_chan\_user\_data(const struct zbus\_channel \*chan)

Get the channel's user data.

**Definition** zbus.h:758

[zbus\_chan\_pub\_stats\_last\_time](group__zbus__apis.md#gac5dff9990d709d736b30f36d68c0297b)

static k\_ticks\_t zbus\_chan\_pub\_stats\_last\_time(const struct zbus\_channel \*chan)

Get the time a channel was last published to.

**Definition** zbus.h:814

[zbus\_chan\_from\_id](group__zbus__apis.md#gacef06cf9818ab91be97d45ab5f58a4a3)

const struct zbus\_channel \* zbus\_chan\_from\_id(uint32\_t channel\_id)

Retrieve a zbus channel from its numeric identifier.

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

**Definition** zbus.h:797

[zbus\_sub\_wait\_msg](group__zbus__apis.md#gaeffce45446509e488192a4e6442453fb)

int zbus\_sub\_wait\_msg(const struct zbus\_observer \*sub, const struct zbus\_channel \*\*chan, void \*msg, k\_timeout\_t timeout)

Wait for a channel message.

[zbus\_chan\_const\_msg](group__zbus__apis.md#gafee07c355df9ac86b85e601196b56a10)

static const void \* zbus\_chan\_const\_msg(const struct zbus\_channel \*chan)

Get a constant reference for a channel message directly.

**Definition** zbus.h:726

[ZBUS\_OBSERVER\_LISTENER\_TYPE](group__zbus__apis.md#gga88941281d7bdd24f3cfbb53e57711d8fa127f19c2121c9c512da9dbcbb301320c)

@ ZBUS\_OBSERVER\_LISTENER\_TYPE

**Definition** zbus.h:120

[ZBUS\_OBSERVER\_SUBSCRIBER\_TYPE](group__zbus__apis.md#gga88941281d7bdd24f3cfbb53e57711d8fa22c784a85353545e8dca2ce7a0ec81b3)

@ ZBUS\_OBSERVER\_SUBSCRIBER\_TYPE

**Definition** zbus.h:121

[ZBUS\_OBSERVER\_MSG\_SUBSCRIBER\_TYPE](group__zbus__apis.md#gga88941281d7bdd24f3cfbb53e57711d8fa8151f9e58a5bd96449bd2f9f8695538c)

@ ZBUS\_OBSERVER\_MSG\_SUBSCRIBER\_TYPE

**Definition** zbus.h:122

[NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)

#define NULL

**Definition** iar\_missing\_defs.h:20

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

**Definition** kernel.h:2540

[k\_msgq](structk__msgq.md)

Message Queue Structure.

**Definition** kernel.h:4640

[k\_sem](structk__sem.md)

Semaphore structure.

**Definition** kernel.h:3275

[k\_timeout\_t](structk__timeout__t.md)

Kernel timeout type.

**Definition** clock.h:65

[net\_buf\_pool](structnet__buf__pool.md)

Network buffer pool representation.

**Definition** net\_buf.h:1078

[zbus\_channel\_data](structzbus__channel__data.md)

Type used to represent a channel mutable data.

**Definition** zbus.h:32

[zbus\_channel\_data::publish\_timestamp](structzbus__channel__data.md#a1d75cb7c16798b5ef907f92a51ed7f63)

k\_ticks\_t publish\_timestamp

Kernel timestamp of the last publish action on this channel.

**Definition** zbus.h:70

[zbus\_channel\_data::msg\_subscriber\_pool](structzbus__channel__data.md#a2490c05755696b7ba1f1f1392d27845f)

struct net\_buf\_pool \* msg\_subscriber\_pool

Net buf pool for message subscribers.

**Definition** zbus.h:65

[zbus\_channel\_data::publish\_count](structzbus__channel__data.md#a45172a94503b0005d662567c5cc8c97f)

uint32\_t publish\_count

Number of times data has been published to this channel.

**Definition** zbus.h:72

[zbus\_channel\_data::observers\_end\_idx](structzbus__channel__data.md#a5b3c38f70cd99cc7e83f9b641997e1ed)

int16\_t observers\_end\_idx

Static channel observer list end index.

**Definition** zbus.h:41

[zbus\_channel\_data::observers\_start\_idx](structzbus__channel__data.md#a6329a0af467d83ad488f3310c1002c41)

int16\_t observers\_start\_idx

Static channel observer list start index.

**Definition** zbus.h:36

[zbus\_channel\_data::sem](structzbus__channel__data.md#a6fa71ae5dc260f5934f47383f53891a7)

struct k\_sem sem

Access control semaphore.

**Definition** zbus.h:46

[zbus\_channel\_data::observers](structzbus__channel__data.md#aeffcb35769775ee0927c3af9be77d1e1)

sys\_slist\_t observers

Channel observer list.

**Definition** zbus.h:59

[zbus\_channel](structzbus__channel.md)

Type used to represent a channel.

**Definition** zbus.h:82

[zbus\_channel::user\_data](structzbus__channel.md#a34864d7da9816955a41caf2a8355f3f0)

void \* user\_data

User data available to extend zbus features.

**Definition** zbus.h:102

[zbus\_channel::id](structzbus__channel.md#a438ff0d8bf5a1d05af2f16f737c40d4f)

uint32\_t id

Unique numeric channel identifier.

**Definition** zbus.h:89

[zbus\_channel::data](structzbus__channel.md#a5588983f2aefce2dd7cffad564c68d16)

struct zbus\_channel\_data \* data

Mutable channel data struct.

**Definition** zbus.h:111

[zbus\_channel::validator](structzbus__channel.md#a90558613c362e75aa621cb240b178138)

bool(\* validator)(const void \*msg, size\_t msg\_size)

Message validator.

**Definition** zbus.h:108

[zbus\_channel::message\_size](structzbus__channel.md#ab7f330f3d70774afeebb74cc03f90d34)

size\_t message\_size

Message size.

**Definition** zbus.h:97

[zbus\_channel::name](structzbus__channel.md#ab8e66cdcfd2429058ca86e6af3813e03)

const char \* name

Channel name.

**Definition** zbus.h:85

[zbus\_channel::message](structzbus__channel.md#abc00c2ed80b4ce3a0ea7304f43f30d08)

void \* message

Message reference.

**Definition** zbus.h:94

[zbus\_observer\_data](structzbus__observer__data.md)

**Definition** zbus.h:125

[zbus\_observer\_data::enabled](structzbus__observer__data.md#ad16ca7a9e83f54afd75f6accf471eb91)

bool enabled

Enabled flag.

**Definition** zbus.h:127

[zbus\_observer\_node](structzbus__observer__node.md)

Structure used to register runtime obeservers.

**Definition** zbus.h:873

[zbus\_observer\_node::obs](structzbus__observer__node.md#a9d9c6843db5c9bab9a8354929f769c75)

const struct zbus\_observer \* obs

**Definition** zbus.h:875

[zbus\_observer\_node::node](structzbus__observer__node.md#af2beaa501ed02f30752189a69219746b)

sys\_snode\_t node

**Definition** zbus.h:874

[zbus\_observer](structzbus__observer.md)

Type used to represent an observer.

**Definition** zbus.h:150

[zbus\_observer::type](structzbus__observer.md#a0251cf9bdca418b6b8123b998b57efe2)

enum zbus\_observer\_type type

Type indication.

**Definition** zbus.h:156

[zbus\_observer::message\_fifo](structzbus__observer.md#a3594b07a2573e03b18ca640809ffd3fa)

struct k\_fifo \* message\_fifo

Observer message FIFO.

**Definition** zbus.h:172

[zbus\_observer::callback](structzbus__observer.md#a78037ed7bcba26af33b6221bf7e4f9d2)

void(\* callback)(const struct zbus\_channel \*chan)

Observer callback function.

**Definition** zbus.h:166

[zbus\_observer::data](structzbus__observer.md#abdca15310be41ea2ce1ae3bbe0ebabb7)

struct zbus\_observer\_data \* data

Mutable observer data struct.

**Definition** zbus.h:159

[zbus\_observer::queue](structzbus__observer.md#ac03ca78cff09b9466cbe34921862d27c)

struct k\_msgq \* queue

Observer message queue.

**Definition** zbus.h:163

[zbus\_observer::name](structzbus__observer.md#ad9d31821d69e181f28e80e5eedf5a331)

const char \* name

Observer name.

**Definition** zbus.h:153

[iterable\_sections.h](sys_2iterable__sections_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [zbus](dir_4ac3b76b03f02d08133e5af61546c3d3.md)
- [zbus.h](zbus_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
