---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/zbus_8h_source.html
original_path: doxygen/html/zbus_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
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

85#if defined(CONFIG\_ZBUS\_CHANNEL\_ID) || defined(\_\_DOXYGEN\_\_)

[ 87](structzbus__channel.md#a438ff0d8bf5a1d05af2f16f737c40d4f) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [id](structzbus__channel.md#a438ff0d8bf5a1d05af2f16f737c40d4f);

88#endif

[ 92](structzbus__channel.md#abc00c2ed80b4ce3a0ea7304f43f30d08) void \*[message](structzbus__channel.md#abc00c2ed80b4ce3a0ea7304f43f30d08);

93

[ 95](structzbus__channel.md#ab7f330f3d70774afeebb74cc03f90d34) size\_t [message\_size](structzbus__channel.md#ab7f330f3d70774afeebb74cc03f90d34);

96

[ 100](structzbus__channel.md#a34864d7da9816955a41caf2a8355f3f0) void \*[user\_data](structzbus__channel.md#a34864d7da9816955a41caf2a8355f3f0);

101

[ 106](structzbus__channel.md#a90558613c362e75aa621cb240b178138) [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) (\*[validator](structzbus__channel.md#a90558613c362e75aa621cb240b178138))(const void \*msg, size\_t msg\_size);

107

[ 109](structzbus__channel.md#a5588983f2aefce2dd7cffad564c68d16) struct [zbus\_channel\_data](structzbus__channel__data.md) \*[data](structzbus__channel.md#a5588983f2aefce2dd7cffad564c68d16);

110};

111

[ 117](group__zbus__apis.md#ga88941281d7bdd24f3cfbb53e57711d8f)enum \_\_packed [zbus\_observer\_type](group__zbus__apis.md#ga88941281d7bdd24f3cfbb53e57711d8f) {

[ 118](group__zbus__apis.md#gga88941281d7bdd24f3cfbb53e57711d8fa127f19c2121c9c512da9dbcbb301320c) [ZBUS\_OBSERVER\_LISTENER\_TYPE](group__zbus__apis.md#gga88941281d7bdd24f3cfbb53e57711d8fa127f19c2121c9c512da9dbcbb301320c),

[ 119](group__zbus__apis.md#gga88941281d7bdd24f3cfbb53e57711d8fa22c784a85353545e8dca2ce7a0ec81b3) [ZBUS\_OBSERVER\_SUBSCRIBER\_TYPE](group__zbus__apis.md#gga88941281d7bdd24f3cfbb53e57711d8fa22c784a85353545e8dca2ce7a0ec81b3),

[ 120](group__zbus__apis.md#gga88941281d7bdd24f3cfbb53e57711d8fa8151f9e58a5bd96449bd2f9f8695538c) [ZBUS\_OBSERVER\_MSG\_SUBSCRIBER\_TYPE](group__zbus__apis.md#gga88941281d7bdd24f3cfbb53e57711d8fa8151f9e58a5bd96449bd2f9f8695538c),

121};

122

[ 123](structzbus__observer__data.md)struct [zbus\_observer\_data](structzbus__observer__data.md) {

[ 125](structzbus__observer__data.md#ad16ca7a9e83f54afd75f6accf471eb91) bool [enabled](structzbus__observer__data.md#ad16ca7a9e83f54afd75f6accf471eb91);

126

127#if defined(CONFIG\_ZBUS\_PRIORITY\_BOOST)

129 int priority;

130#endif /\* CONFIG\_ZBUS\_PRIORITY\_BOOST \*/

131};

132

[ 148](structzbus__observer.md)struct [zbus\_observer](structzbus__observer.md) {

149#if defined(CONFIG\_ZBUS\_OBSERVER\_NAME) || defined(\_\_DOXYGEN\_\_)

[ 151](structzbus__observer.md#ad9d31821d69e181f28e80e5eedf5a331) const char \*[name](structzbus__observer.md#ad9d31821d69e181f28e80e5eedf5a331);

152#endif

[ 154](structzbus__observer.md#a0251cf9bdca418b6b8123b998b57efe2) enum [zbus\_observer\_type](group__zbus__apis.md#ga88941281d7bdd24f3cfbb53e57711d8f) [type](structzbus__observer.md#a0251cf9bdca418b6b8123b998b57efe2);

155

[ 157](structzbus__observer.md#abdca15310be41ea2ce1ae3bbe0ebabb7) struct [zbus\_observer\_data](structzbus__observer__data.md) \*[data](structzbus__observer.md#abdca15310be41ea2ce1ae3bbe0ebabb7);

158

159 union {

[ 161](structzbus__observer.md#ac03ca78cff09b9466cbe34921862d27c) struct [k\_msgq](structk__msgq.md) \*[queue](structzbus__observer.md#ac03ca78cff09b9466cbe34921862d27c);

162

[ 164](structzbus__observer.md#a78037ed7bcba26af33b6221bf7e4f9d2) void (\*[callback](structzbus__observer.md#a78037ed7bcba26af33b6221bf7e4f9d2))(const struct [zbus\_channel](structzbus__channel.md) \*chan);

165

166#if defined(CONFIG\_ZBUS\_MSG\_SUBSCRIBER) || defined(\_\_DOXYGEN\_\_)

[ 170](structzbus__observer.md#a3594b07a2573e03b18ca640809ffd3fa) struct [k\_fifo](structk__fifo.md) \*[message\_fifo](structzbus__observer.md#a3594b07a2573e03b18ca640809ffd3fa);

171#endif /\* CONFIG\_ZBUS\_MSG\_SUBSCRIBER \*/

172 };

173};

174

176struct zbus\_channel\_observation\_mask {

177 bool enabled;

178};

179

180struct zbus\_channel\_observation {

181 const struct zbus\_channel \*chan;

182 const struct zbus\_observer \*obs;

183};

184

185#ifdef \_\_cplusplus

186#define \_ZBUS\_CPP\_EXTERN extern

187#else

188#define \_ZBUS\_CPP\_EXTERN

189#endif /\* \_\_cplusplus \*/

190

191#define ZBUS\_MIN\_THREAD\_PRIORITY (CONFIG\_NUM\_PREEMPT\_PRIORITIES - 1)

192

193#if defined(CONFIG\_ZBUS\_ASSERT\_MOCK)

194#define \_ZBUS\_ASSERT(\_cond, \_fmt, ...) \

195 do { \

196 if (!(\_cond)) { \

197 printk("ZBUS ASSERT: "); \

198 printk(\_fmt, ##\_\_VA\_ARGS\_\_); \

199 printk("\n"); \

200 return -EFAULT; \

201 } \

202 } while (0)

203#else

204#define \_ZBUS\_ASSERT(\_cond, \_fmt, ...) \_\_ASSERT(\_cond, \_fmt, ##\_\_VA\_ARGS\_\_)

205#endif

206

207#if defined(CONFIG\_ZBUS\_CHANNEL\_NAME)

208#define ZBUS\_CHANNEL\_NAME\_INIT(\_name) .name = #\_name,

209#define \_ZBUS\_CHAN\_NAME(\_chan) (\_chan)->name

210#else

211#define ZBUS\_CHANNEL\_NAME\_INIT(\_name)

212#define \_ZBUS\_CHAN\_NAME(\_chan) ""

213#endif

214

215#if defined(CONFIG\_ZBUS\_OBSERVER\_NAME)

216#define ZBUS\_OBSERVER\_NAME\_INIT(\_name) .name = #\_name,

217#define \_ZBUS\_OBS\_NAME(\_obs) (\_obs)->name

218#else

219#define ZBUS\_OBSERVER\_NAME\_INIT(\_name)

220#define \_ZBUS\_OBS\_NAME(\_obs) ""

221#endif

222

223#if defined(CONFIG\_ZBUS\_RUNTIME\_OBSERVERS)

224#define ZBUS\_RUNTIME\_OBSERVERS\_LIST\_DECL(\_slist\_name) static sys\_slist\_t \_slist\_name

225#define ZBUS\_RUNTIME\_OBSERVERS\_LIST\_INIT(\_slist\_name) .runtime\_observers = &\_slist\_name,

226#else

227#define ZBUS\_RUNTIME\_OBSERVERS\_LIST\_DECL(\_slist\_name)

228#define ZBUS\_RUNTIME\_OBSERVERS\_LIST\_INIT(\_slist\_name) /\* No runtime observers \*/

229#endif

230

231#define \_ZBUS\_OBS\_EXTERN(\_name) extern const struct zbus\_observer \_name

232

233#define \_ZBUS\_CHAN\_EXTERN(\_name) extern const struct zbus\_channel \_name

234

235#define ZBUS\_REF(\_value) &(\_value)

236

237#define FOR\_EACH\_FIXED\_ARG\_NONEMPTY\_TERM(F, sep, fixed\_arg, ...) \

238 COND\_CODE\_0(/\* are there zero non-empty arguments ? \*/ \

239 NUM\_VA\_ARGS\_LESS\_1( \

240 LIST\_DROP\_EMPTY(\_\_VA\_ARGS\_\_, \_)), /\* if so, expand to nothing \*/ \

241 (), /\* otherwise, expand to: \*/ \

242 (FOR\_EACH\_IDX\_FIXED\_ARG( \

243 F, sep, fixed\_arg, \

244 LIST\_DROP\_EMPTY(\_\_VA\_ARGS\_\_)) /\* plus a final terminator \*/ \

245 \_\_DEBRACKET sep))

246

247#define \_ZBUS\_OBSERVATION\_PREFIX(\_idx) \

248 GET\_ARG\_N(\_idx, 00, 01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 11, 12, 13, 14, 15, 16, 17, \

249 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, \

250 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, \

251 58, 59, 60, 61, 62, 63)

252

253#define \_ZBUS\_CHAN\_OBSERVATION(\_idx, \_obs, \_chan) \

254 const STRUCT\_SECTION\_ITERABLE( \

255 zbus\_channel\_observation, \

256 \_CONCAT(\_chan, \_ZBUS\_OBSERVATION\_PREFIX(UTIL\_INC(\_idx)))) = {.chan = &\_chan, \

257 .obs = &\_obs}; \

258 STRUCT\_SECTION\_ITERABLE(zbus\_channel\_observation\_mask, \

259 \_CONCAT(\_CONCAT(\_chan, \_ZBUS\_OBSERVATION\_PREFIX(UTIL\_INC(\_idx))), \

260 \_mask)) = {.enabled = false};

261

262#if defined(CONFIG\_ZBUS\_RUNTIME\_OBSERVERS) || defined(\_\_DOXYGEN\_\_)

263#define \_ZBUS\_RUNTIME\_OBSERVERS(\_name) .observers = &(\_CONCAT(\_observers\_, \_name)),

264#define \_ZBUS\_RUNTIME\_OBSERVERS\_DECL(\_name) static sys\_slist\_t \_CONCAT(\_observers\_, \_name);

265#else

266#define \_ZBUS\_RUNTIME\_OBSERVERS(\_name)

267#define \_ZBUS\_RUNTIME\_OBSERVERS\_DECL(\_name)

268#endif /\* CONFIG\_ZBUS\_RUNTIME\_OBSERVERS \*/

269

270#define \_ZBUS\_MESSAGE\_NAME(\_name) \_CONCAT(\_zbus\_message\_, \_name)

271

272/\* clang-format off \*/

273#define \_ZBUS\_CHAN\_DEFINE(\_name, \_id, \_type, \_validator, \_user\_data) \

274 static struct zbus\_channel\_data \_CONCAT(\_zbus\_chan\_data\_, \_name) = { \

275 .observers\_start\_idx = -1, \

276 .observers\_end\_idx = -1, \

277 .sem = Z\_SEM\_INITIALIZER(\_CONCAT(\_zbus\_chan\_data\_, \_name).sem, 1, 1), \

278 IF\_ENABLED(CONFIG\_ZBUS\_PRIORITY\_BOOST, \

279 (.highest\_observer\_priority = ZBUS\_MIN\_THREAD\_PRIORITY,)) \

280 IF\_ENABLED(CONFIG\_ZBUS\_RUNTIME\_OBSERVERS, \

281 (.observers = SYS\_SLIST\_STATIC\_INIT( \

282 &\_CONCAT(\_zbus\_chan\_data\_, \_name).observers),)) \

283 }; \

284 static K\_MUTEX\_DEFINE(\_CONCAT(\_zbus\_mutex\_, \_name)); \

285 \_ZBUS\_CPP\_EXTERN const STRUCT\_SECTION\_ITERABLE(zbus\_channel, \_name) = { \

286 ZBUS\_CHANNEL\_NAME\_INIT(\_name) /\* Maybe removed \*/ \

287 IF\_ENABLED(CONFIG\_ZBUS\_CHANNEL\_ID, (.id = \_id,)) \

288 .message = &\_ZBUS\_MESSAGE\_NAME(\_name), \

289 .message\_size = sizeof(\_type), \

290 .user\_data = \_user\_data, \

291 .validator = \_validator, \

292 .data = &\_CONCAT(\_zbus\_chan\_data\_, \_name), \

293 IF\_ENABLED(ZBUS\_MSG\_SUBSCRIBER\_NET\_BUF\_POOL\_ISOLATION, \

294 (.msg\_subscriber\_pool = &\_zbus\_msg\_subscribers\_pool,)) \

295 }

296/\* clang-format on \*/

297

299

300/\* clang-format off \*/

301

[ 313](group__zbus__apis.md#ga7f763caca474e6c910793d2c714f80b4)#define ZBUS\_CHAN\_ADD\_OBS\_WITH\_MASK(\_chan, \_obs, \_masked, \_prio) \

314 const STRUCT\_SECTION\_ITERABLE(zbus\_channel\_observation, \

315 \_CONCAT(\_CONCAT(\_chan, zz), \_CONCAT(\_prio, \_obs))) = { \

316 .chan = &\_chan, \

317 .obs = &\_obs, \

318 }; \

319 STRUCT\_SECTION\_ITERABLE(zbus\_channel\_observation\_mask, \

320 \_CONCAT(\_CONCAT(\_CONCAT(\_chan, zz), \_CONCAT(\_prio, \_obs)), \

321 \_mask)) = {.enabled = \_masked}

322/\* clang-format on \*/

323

[ 334](group__zbus__apis.md#gaf63215f3f53741edf52b4d0d7b2b97df)#define ZBUS\_CHAN\_ADD\_OBS(\_chan, \_obs, \_prio) ZBUS\_CHAN\_ADD\_OBS\_WITH\_MASK(\_chan, \_obs, false, \_prio)

335

[ 341](group__zbus__apis.md#ga49f169c6d50a3bad57e1b319362d2924)#define ZBUS\_OBS\_DECLARE(...) FOR\_EACH\_NONEMPTY\_TERM(\_ZBUS\_OBS\_EXTERN, (;), \_\_VA\_ARGS\_\_)

342

[ 348](group__zbus__apis.md#ga0662b2db8077a8075c07a3afd0161d0f)#define ZBUS\_CHAN\_DECLARE(...) FOR\_EACH(\_ZBUS\_CHAN\_EXTERN, (;), \_\_VA\_ARGS\_\_)

349

[ 354](group__zbus__apis.md#ga763dad07a1ae9bb38f9c240e1920caef)#define ZBUS\_OBSERVERS\_EMPTY

355

[ 361](group__zbus__apis.md#gafed25f045c3b8d438daf4ebd5e517692)#define ZBUS\_OBSERVERS(...) \_\_VA\_ARGS\_\_

362

[ 367](group__zbus__apis.md#ga1f1e0798856c54dd641c1a322789400b)#define ZBUS\_CHAN\_ID\_INVALID UINT32\_MAX

368

[ 384](group__zbus__apis.md#ga29a3a39e5c78a34b2d8491615d1f0687)#define ZBUS\_CHAN\_DEFINE(\_name, \_type, \_validator, \_user\_data, \_observers, \_init\_val) \

385 static \_type \_ZBUS\_MESSAGE\_NAME(\_name) = \_init\_val; \

386 \_ZBUS\_CHAN\_DEFINE(\_name, ZBUS\_CHAN\_ID\_INVALID, \_type, \_validator, \_user\_data); \

387 /\* Extern declaration of observers \*/ \

388 ZBUS\_OBS\_DECLARE(\_observers); \

389 /\* Create all channel observations from observers list \*/ \

390 FOR\_EACH\_FIXED\_ARG\_NONEMPTY\_TERM(\_ZBUS\_CHAN\_OBSERVATION, (;), \_name, \_observers)

391

[ 408](group__zbus__apis.md#ga7c49cba434b90d417859b37722843e5f)#define ZBUS\_CHAN\_DEFINE\_WITH\_ID(\_name, \_id, \_type, \_validator, \_user\_data, \_observers, \_init\_val) \

409 static \_type \_ZBUS\_MESSAGE\_NAME(\_name) = \_init\_val; \

410 \_ZBUS\_CHAN\_DEFINE(\_name, \_id, \_type, \_validator, \_user\_data); \

411 /\* Extern declaration of observers \*/ \

412 ZBUS\_OBS\_DECLARE(\_observers); \

413 /\* Create all channel observations from observers list \*/ \

414 FOR\_EACH\_FIXED\_ARG\_NONEMPTY\_TERM(\_ZBUS\_CHAN\_OBSERVATION, (;), \_name, \_observers)

415

[ 425](group__zbus__apis.md#ga4bf8c445814c1fcee9b9819a36bc9bd6)#define ZBUS\_MSG\_INIT(\_val, ...) {\_val, ##\_\_VA\_ARGS\_\_}

426

427/\* clang-format off \*/

428

[ 440](group__zbus__apis.md#gaf56f71babe2bb27258f025332b80c58f)#define ZBUS\_SUBSCRIBER\_DEFINE\_WITH\_ENABLE(\_name, \_queue\_size, \_enable) \

441 K\_MSGQ\_DEFINE(\_zbus\_observer\_queue\_##\_name, \

442 sizeof(struct zbus\_channel \*), \

443 \_queue\_size, sizeof(struct zbus\_channel \*) \

444 ); \

445 static struct zbus\_observer\_data \_CONCAT(\_zbus\_obs\_data\_, \_name) = { \

446 .enabled = \_enable, \

447 IF\_ENABLED(CONFIG\_ZBUS\_PRIORITY\_BOOST, ( \

448 .priority = ZBUS\_MIN\_THREAD\_PRIORITY, \

449 )) \

450 }; \

451 \_ZBUS\_CPP\_EXTERN const STRUCT\_SECTION\_ITERABLE(zbus\_observer, \_name) = { \

452 ZBUS\_OBSERVER\_NAME\_INIT(\_name) /\* Name field \*/ \

453 .type = ZBUS\_OBSERVER\_SUBSCRIBER\_TYPE, \

454 .data = &\_CONCAT(\_zbus\_obs\_data\_, \_name), \

455 .queue = &\_zbus\_observer\_queue\_##\_name, \

456 }

457/\* clang-format on \*/

458

[ 470](group__zbus__apis.md#gac17a735cccecfc90f26127e48cf6279a)#define ZBUS\_SUBSCRIBER\_DEFINE(\_name, \_queue\_size) \

471 ZBUS\_SUBSCRIBER\_DEFINE\_WITH\_ENABLE(\_name, \_queue\_size, true)

472

473/\* clang-format off \*/

474

[ 486](group__zbus__apis.md#gace4ac9da0e1bab7ba72797783ded948f)#define ZBUS\_LISTENER\_DEFINE\_WITH\_ENABLE(\_name, \_cb, \_enable) \

487 static struct zbus\_observer\_data \_CONCAT(\_zbus\_obs\_data\_, \_name) = { \

488 .enabled = \_enable, \

489 IF\_ENABLED(CONFIG\_ZBUS\_PRIORITY\_BOOST, ( \

490 .priority = ZBUS\_MIN\_THREAD\_PRIORITY, \

491 )) \

492 }; \

493 \_ZBUS\_CPP\_EXTERN const STRUCT\_SECTION\_ITERABLE(zbus\_observer, \_name) = { \

494 ZBUS\_OBSERVER\_NAME\_INIT(\_name) /\* Name field \*/ \

495 .type = ZBUS\_OBSERVER\_LISTENER\_TYPE, \

496 .data = &\_CONCAT(\_zbus\_obs\_data\_, \_name), \

497 .callback = (\_cb) \

498 }

499/\* clang-format on \*/

500

[ 511](group__zbus__apis.md#gabfc7be8298e76fe2f7ae628be30b8390)#define ZBUS\_LISTENER\_DEFINE(\_name, \_cb) ZBUS\_LISTENER\_DEFINE\_WITH\_ENABLE(\_name, \_cb, true)

512

513/\* clang-format off \*/

514

[ 525](group__zbus__apis.md#ga6089c1ae0dad91306f79d48a63b31785)#define ZBUS\_MSG\_SUBSCRIBER\_DEFINE\_WITH\_ENABLE(\_name, \_enable) \

526 static K\_FIFO\_DEFINE(\_zbus\_observer\_fifo\_##\_name); \

527 static struct zbus\_observer\_data \_CONCAT(\_zbus\_obs\_data\_, \_name) = { \

528 .enabled = \_enable, \

529 IF\_ENABLED(CONFIG\_ZBUS\_PRIORITY\_BOOST, ( \

530 .priority = ZBUS\_MIN\_THREAD\_PRIORITY, \

531 )) \

532 }; \

533 \_ZBUS\_CPP\_EXTERN const STRUCT\_SECTION\_ITERABLE(zbus\_observer, \_name) = { \

534 ZBUS\_OBSERVER\_NAME\_INIT(\_name) /\* Name field \*/ \

535 .type = ZBUS\_OBSERVER\_MSG\_SUBSCRIBER\_TYPE, \

536 .data = &\_CONCAT(\_zbus\_obs\_data\_, \_name), \

537 .message\_fifo = &\_zbus\_observer\_fifo\_##\_name, \

538 }

539/\* clang-format on \*/

540

[ 552](group__zbus__apis.md#ga07a0c2c428c9e4891e86a63a420b2268)#define ZBUS\_MSG\_SUBSCRIBER\_DEFINE(\_name) ZBUS\_MSG\_SUBSCRIBER\_DEFINE\_WITH\_ENABLE(\_name, true)

[ 574](group__zbus__apis.md#gadfcaba65b397c1d8c31836ef3cf61244)int [zbus\_chan\_pub](group__zbus__apis.md#gadfcaba65b397c1d8c31836ef3cf61244)(const struct [zbus\_channel](structzbus__channel.md) \*chan, const void \*msg, [k\_timeout\_t](structk__timeout__t.md) timeout);

575

[ 593](group__zbus__apis.md#ga8209721e0a295c84d112ba1a7171100e)int [zbus\_chan\_read](group__zbus__apis.md#ga8209721e0a295c84d112ba1a7171100e)(const struct [zbus\_channel](structzbus__channel.md) \*chan, void \*msg, [k\_timeout\_t](structk__timeout__t.md) timeout);

594

[ 616](group__zbus__apis.md#ga00bfb7db54594029f4d288bcf5b56b3a)int [zbus\_chan\_claim](group__zbus__apis.md#ga00bfb7db54594029f4d288bcf5b56b3a)(const struct [zbus\_channel](structzbus__channel.md) \*chan, [k\_timeout\_t](structk__timeout__t.md) timeout);

617

[ 632](group__zbus__apis.md#ga74747affb345e68ce1d564c349409e59)int [zbus\_chan\_finish](group__zbus__apis.md#ga74747affb345e68ce1d564c349409e59)(const struct [zbus\_channel](structzbus__channel.md) \*chan);

633

[ 652](group__zbus__apis.md#ga6ec2f463801499e23a011fa4e68aa3e7)int [zbus\_chan\_notify](group__zbus__apis.md#ga6ec2f463801499e23a011fa4e68aa3e7)(const struct [zbus\_channel](structzbus__channel.md) \*chan, [k\_timeout\_t](structk__timeout__t.md) timeout);

653

654#if defined(CONFIG\_ZBUS\_CHANNEL\_NAME) || defined(\_\_DOXYGEN\_\_)

655

[ 665](group__zbus__apis.md#ga05a220636fc6bb58b97805e558b76d73)static inline const char \*[zbus\_chan\_name](group__zbus__apis.md#ga05a220636fc6bb58b97805e558b76d73)(const struct [zbus\_channel](structzbus__channel.md) \*chan)

666{

667 \_\_ASSERT(chan != [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4), "chan is required");

668

669 return chan->[name](structzbus__channel.md#ab8e66cdcfd2429058ca86e6af3813e03);

670}

671

672#endif

673

674#if defined(CONFIG\_ZBUS\_CHANNEL\_ID) || defined(\_\_DOXYGEN\_\_)

675

[ 684](group__zbus__apis.md#gacef06cf9818ab91be97d45ab5f58a4a3)const struct [zbus\_channel](structzbus__channel.md) \*[zbus\_chan\_from\_id](group__zbus__apis.md#gacef06cf9818ab91be97d45ab5f58a4a3)([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel\_id);

685

686#endif

687

[ 700](group__zbus__apis.md#gaaf8b34113b7b993438bd42db64812572)static inline void \*[zbus\_chan\_msg](group__zbus__apis.md#gaaf8b34113b7b993438bd42db64812572)(const struct [zbus\_channel](structzbus__channel.md) \*chan)

701{

702 \_\_ASSERT(chan != [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4), "chan is required");

703

704 return chan->[message](structzbus__channel.md#abc00c2ed80b4ce3a0ea7304f43f30d08);

705}

706

[ 721](group__zbus__apis.md#gafee07c355df9ac86b85e601196b56a10)static inline const void \*[zbus\_chan\_const\_msg](group__zbus__apis.md#gafee07c355df9ac86b85e601196b56a10)(const struct [zbus\_channel](structzbus__channel.md) \*chan)

722{

723 \_\_ASSERT(chan != [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4), "chan is required");

724

725 return chan->[message](structzbus__channel.md#abc00c2ed80b4ce3a0ea7304f43f30d08);

726}

727

[ 737](group__zbus__apis.md#ga8895a18b282ca2fe7528b4e5cf48e025)static inline [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [zbus\_chan\_msg\_size](group__zbus__apis.md#ga8895a18b282ca2fe7528b4e5cf48e025)(const struct [zbus\_channel](structzbus__channel.md) \*chan)

738{

739 \_\_ASSERT(chan != [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4), "chan is required");

740

741 return chan->[message\_size](structzbus__channel.md#ab7f330f3d70774afeebb74cc03f90d34);

742}

743

[ 753](group__zbus__apis.md#gac0b0ed0356fca5a8b65a3332931a369a)static inline void \*[zbus\_chan\_user\_data](group__zbus__apis.md#gac0b0ed0356fca5a8b65a3332931a369a)(const struct [zbus\_channel](structzbus__channel.md) \*chan)

754{

755 \_\_ASSERT(chan != [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4), "chan is required");

756

757 return chan->[user\_data](structzbus__channel.md#a34864d7da9816955a41caf2a8355f3f0);

758}

759

760#if defined(CONFIG\_ZBUS\_MSG\_SUBSCRIBER\_NET\_BUF\_POOL\_ISOLATION) || defined(\_\_DOXYGEN\_\_)

761

[ 768](group__zbus__apis.md#ga3f90d50f20e7779ef257676ac10da357)static inline void [zbus\_chan\_set\_msg\_sub\_pool](group__zbus__apis.md#ga3f90d50f20e7779ef257676ac10da357)(const struct [zbus\_channel](structzbus__channel.md) \*chan,

769 struct [net\_buf\_pool](structnet__buf__pool.md) \*pool)

770{

771 \_\_ASSERT(chan != [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4), "chan is required");

772 \_\_ASSERT(pool != [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4), "pool is required");

773

774 chan->[data](structzbus__channel.md#a5588983f2aefce2dd7cffad564c68d16)->[msg\_subscriber\_pool](structzbus__channel__data.md#a2490c05755696b7ba1f1f1392d27845f) = pool;

775}

776

777#endif /\* ZBUS\_MSG\_SUBSCRIBER\_NET\_BUF\_POOL\_ISOLATION \*/

778

779#if defined(CONFIG\_ZBUS\_CHANNEL\_PUBLISH\_STATS) || defined(\_\_DOXYGEN\_\_)

780

[ 792](group__zbus__apis.md#gaef067fb1e8b834993662af84b916483a)static inline void [zbus\_chan\_pub\_stats\_update](group__zbus__apis.md#gaef067fb1e8b834993662af84b916483a)(const struct [zbus\_channel](structzbus__channel.md) \*chan)

793{

794 \_\_ASSERT(chan != [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4), "chan is required");

795

796 chan->[data](structzbus__channel.md#a5588983f2aefce2dd7cffad564c68d16)->[publish\_timestamp](structzbus__channel__data.md#a1d75cb7c16798b5ef907f92a51ed7f63) = [k\_uptime\_ticks](group__clock__apis.md#ga8f143af2ee4ad42d9f7817ef161cbd13)();

797 chan->[data](structzbus__channel.md#a5588983f2aefce2dd7cffad564c68d16)->[publish\_count](structzbus__channel__data.md#a45172a94503b0005d662567c5cc8c97f) += 1;

798}

799

[ 809](group__zbus__apis.md#gac5dff9990d709d736b30f36d68c0297b)static inline [k\_ticks\_t](group__clock__apis.md#ga9832cb0adc2d1866420e5c370a0863e2) [zbus\_chan\_pub\_stats\_last\_time](group__zbus__apis.md#gac5dff9990d709d736b30f36d68c0297b)(const struct [zbus\_channel](structzbus__channel.md) \*chan)

810{

811 \_\_ASSERT(chan != [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4), "chan is required");

812

813 return chan->[data](structzbus__channel.md#a5588983f2aefce2dd7cffad564c68d16)->[publish\_timestamp](structzbus__channel__data.md#a1d75cb7c16798b5ef907f92a51ed7f63);

814}

815

[ 825](group__zbus__apis.md#ga5648bf527de4aff89648a34bf8a7539a)static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [zbus\_chan\_pub\_stats\_count](group__zbus__apis.md#ga5648bf527de4aff89648a34bf8a7539a)(const struct [zbus\_channel](structzbus__channel.md) \*chan)

826{

827 \_\_ASSERT(chan != [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4), "chan is required");

828

829 return chan->[data](structzbus__channel.md#a5588983f2aefce2dd7cffad564c68d16)->[publish\_count](structzbus__channel__data.md#a45172a94503b0005d662567c5cc8c97f);

830}

831

[ 841](group__zbus__apis.md#ga09503e2b9c01f79136f9eb600ddb3f31)static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [zbus\_chan\_pub\_stats\_avg\_period](group__zbus__apis.md#ga09503e2b9c01f79136f9eb600ddb3f31)(const struct [zbus\_channel](structzbus__channel.md) \*chan)

842{

843 \_\_ASSERT(chan != [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4), "chan is required");

844

845 /\* Not yet published, period = 0ms \*/

846 if (chan->[data](structzbus__channel.md#a5588983f2aefce2dd7cffad564c68d16)->[publish\_count](structzbus__channel__data.md#a45172a94503b0005d662567c5cc8c97f) == 0) {

847 return 0;

848 }

849 /\* Average period across application runtime \*/

850 return [k\_uptime\_get](group__clock__apis.md#gae3e992cd3257c23d5b26d765fcbb2b69)() / chan->[data](structzbus__channel.md#a5588983f2aefce2dd7cffad564c68d16)->[publish\_count](structzbus__channel__data.md#a45172a94503b0005d662567c5cc8c97f);

851}

852

853#else

854

855static inline void [zbus\_chan\_pub\_stats\_update](group__zbus__apis.md#gaef067fb1e8b834993662af84b916483a)(const struct [zbus\_channel](structzbus__channel.md) \*chan)

856{

857 (void)chan;

858}

859

860#endif /\* CONFIG\_ZBUS\_CHANNEL\_PUBLISH\_STATS \*/

861

862#if defined(CONFIG\_ZBUS\_RUNTIME\_OBSERVERS) || defined(\_\_DOXYGEN\_\_)

863

[ 880](group__zbus__apis.md#gaddd8ce480bc29ead4442e529915cfbf6)int [zbus\_chan\_add\_obs](group__zbus__apis.md#gaddd8ce480bc29ead4442e529915cfbf6)(const struct [zbus\_channel](structzbus__channel.md) \*chan, const struct [zbus\_observer](structzbus__observer.md) \*obs,

881 [k\_timeout\_t](structk__timeout__t.md) timeout);

882

[ 900](group__zbus__apis.md#gaee11d7472a3f87156b8ef1dcfbe897c4)int [zbus\_chan\_rm\_obs](group__zbus__apis.md#gaee11d7472a3f87156b8ef1dcfbe897c4)(const struct [zbus\_channel](structzbus__channel.md) \*chan, const struct [zbus\_observer](structzbus__observer.md) \*obs,

901 [k\_timeout\_t](structk__timeout__t.md) timeout);

902

904

905struct zbus\_observer\_node {

906 [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) node;

907 const struct [zbus\_observer](structzbus__observer.md) \*obs;

908};

909

911

912#endif /\* CONFIG\_ZBUS\_RUNTIME\_OBSERVERS \*/

913

[ 927](group__zbus__apis.md#ga96767314e040e42609867a36684a6349)int [zbus\_obs\_set\_enable](group__zbus__apis.md#ga96767314e040e42609867a36684a6349)(const struct [zbus\_observer](structzbus__observer.md) \*obs, bool enabled);

928

[ 939](group__zbus__apis.md#ga315fd4e0b6a3c01a23307dd890e69894)static inline int [zbus\_obs\_is\_enabled](group__zbus__apis.md#ga315fd4e0b6a3c01a23307dd890e69894)(const struct [zbus\_observer](structzbus__observer.md) \*obs, bool \*enable)

940{

941 \_ZBUS\_ASSERT(obs != [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4), "obs is required");

942 \_ZBUS\_ASSERT(enable != [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4), "enable is required");

943

944 \*enable = obs->[data](structzbus__observer.md#abdca15310be41ea2ce1ae3bbe0ebabb7)->[enabled](structzbus__observer__data.md#ad16ca7a9e83f54afd75f6accf471eb91);

945

946 return 0;

947}

948

[ 963](group__zbus__apis.md#ga9513264f912f54b60c4341642f578e5a)int [zbus\_obs\_set\_chan\_notification\_mask](group__zbus__apis.md#ga9513264f912f54b60c4341642f578e5a)(const struct [zbus\_observer](structzbus__observer.md) \*obs,

964 const struct [zbus\_channel](structzbus__channel.md) \*chan, bool masked);

965

[ 978](group__zbus__apis.md#ga41ae9799a52c2a7954500b0a3c78d19f)int [zbus\_obs\_is\_chan\_notification\_masked](group__zbus__apis.md#ga41ae9799a52c2a7954500b0a3c78d19f)(const struct [zbus\_observer](structzbus__observer.md) \*obs,

979 const struct [zbus\_channel](structzbus__channel.md) \*chan, bool \*masked);

980

981#if defined(CONFIG\_ZBUS\_OBSERVER\_NAME) || defined(\_\_DOXYGEN\_\_)

982

[ 992](group__zbus__apis.md#ga5bb33ec5b914e6cbc87fa70bf763ad15)static inline const char \*[zbus\_obs\_name](group__zbus__apis.md#ga5bb33ec5b914e6cbc87fa70bf763ad15)(const struct [zbus\_observer](structzbus__observer.md) \*obs)

993{

994 \_\_ASSERT(obs != [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4), "obs is required");

995

996 return obs->[name](structzbus__observer.md#ad9d31821d69e181f28e80e5eedf5a331);

997}

998

999#endif

1000

1001#if defined(CONFIG\_ZBUS\_PRIORITY\_BOOST) || defined(\_\_DOXYGEN\_\_)

1002

[ 1012](group__zbus__apis.md#gabecf160e4d468d0275ad79e22fd0fb5b)int [zbus\_obs\_attach\_to\_thread](group__zbus__apis.md#gabecf160e4d468d0275ad79e22fd0fb5b)(const struct [zbus\_observer](structzbus__observer.md) \*obs);

1013

[ 1023](group__zbus__apis.md#ga493c125c31e44d5a222f0e9c6d01249e)int [zbus\_obs\_detach\_from\_thread](group__zbus__apis.md#ga493c125c31e44d5a222f0e9c6d01249e)(const struct [zbus\_observer](structzbus__observer.md) \*obs);

1024

1025#endif /\* CONFIG\_ZBUS\_PRIORITY\_BOOST \*/

1026

[ 1045](group__zbus__apis.md#ga84a65e276a01ef97eeb5c81b880da72b)int [zbus\_sub\_wait](group__zbus__apis.md#ga84a65e276a01ef97eeb5c81b880da72b)(const struct [zbus\_observer](structzbus__observer.md) \*sub, const struct [zbus\_channel](structzbus__channel.md) \*\*chan,

1046 [k\_timeout\_t](structk__timeout__t.md) timeout);

1047

1048#if defined(CONFIG\_ZBUS\_MSG\_SUBSCRIBER) || defined(\_\_DOXYGEN\_\_)

1049

[ 1068](group__zbus__apis.md#gaeffce45446509e488192a4e6442453fb)int [zbus\_sub\_wait\_msg](group__zbus__apis.md#gaeffce45446509e488192a4e6442453fb)(const struct [zbus\_observer](structzbus__observer.md) \*sub, const struct [zbus\_channel](structzbus__channel.md) \*\*chan, void \*msg,

1069 [k\_timeout\_t](structk__timeout__t.md) timeout);

1070

1071#endif /\* CONFIG\_ZBUS\_MSG\_SUBSCRIBER \*/

1072

[ 1086](group__zbus__apis.md#ga6dffd25f4eb368e773c2bd55f34a0e10)bool [zbus\_iterate\_over\_channels](group__zbus__apis.md#ga6dffd25f4eb368e773c2bd55f34a0e10)(bool (\*iterator\_func)(const struct [zbus\_channel](structzbus__channel.md) \*chan));

[ 1101](group__zbus__apis.md#gab8df108b0238757ff631ec1e120fa2c3)bool [zbus\_iterate\_over\_channels\_with\_user\_data](group__zbus__apis.md#gab8df108b0238757ff631ec1e120fa2c3)(

1102 bool (\*iterator\_func)(const struct [zbus\_channel](structzbus__channel.md) \*chan, void \*user\_data), void \*user\_data);

1103

[ 1117](group__zbus__apis.md#ga2fa50316993afc5807e9d707d664be14)bool [zbus\_iterate\_over\_observers](group__zbus__apis.md#ga2fa50316993afc5807e9d707d664be14)(bool (\*iterator\_func)(const struct [zbus\_observer](structzbus__observer.md) \*obs));

[ 1132](group__zbus__apis.md#ga2f4e39c500fed0a6bcfedb5dec3f797a)bool [zbus\_iterate\_over\_observers\_with\_user\_data](group__zbus__apis.md#ga2f4e39c500fed0a6bcfedb5dec3f797a)(

1133 bool (\*iterator\_func)(const struct [zbus\_observer](structzbus__observer.md) \*obs, void \*user\_data), void \*user\_data);

1134

1138

1139#ifdef \_\_cplusplus

1140}

1141#endif

1142

1143#endif /\* ZEPHYR\_INCLUDE\_ZBUS\_H\_ \*/

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

**Definition** kernel.h:1855

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

**Definition** zbus.h:665

[zbus\_chan\_pub\_stats\_avg\_period](group__zbus__apis.md#ga09503e2b9c01f79136f9eb600ddb3f31)

static uint32\_t zbus\_chan\_pub\_stats\_avg\_period(const struct zbus\_channel \*chan)

Get the average period between publishes to a channel.

**Definition** zbus.h:841

[zbus\_iterate\_over\_observers\_with\_user\_data](group__zbus__apis.md#ga2f4e39c500fed0a6bcfedb5dec3f797a)

bool zbus\_iterate\_over\_observers\_with\_user\_data(bool(\*iterator\_func)(const struct zbus\_observer \*obs, void \*user\_data), void \*user\_data)

Iterate over observers with user data.

[zbus\_iterate\_over\_observers](group__zbus__apis.md#ga2fa50316993afc5807e9d707d664be14)

bool zbus\_iterate\_over\_observers(bool(\*iterator\_func)(const struct zbus\_observer \*obs))

Iterate over observers.

[zbus\_obs\_is\_enabled](group__zbus__apis.md#ga315fd4e0b6a3c01a23307dd890e69894)

static int zbus\_obs\_is\_enabled(const struct zbus\_observer \*obs, bool \*enable)

Get the observer state.

**Definition** zbus.h:939

[zbus\_chan\_set\_msg\_sub\_pool](group__zbus__apis.md#ga3f90d50f20e7779ef257676ac10da357)

static void zbus\_chan\_set\_msg\_sub\_pool(const struct zbus\_channel \*chan, struct net\_buf\_pool \*pool)

Set the channel's msg subscriber net\_buf pool.

**Definition** zbus.h:768

[zbus\_obs\_is\_chan\_notification\_masked](group__zbus__apis.md#ga41ae9799a52c2a7954500b0a3c78d19f)

int zbus\_obs\_is\_chan\_notification\_masked(const struct zbus\_observer \*obs, const struct zbus\_channel \*chan, bool \*masked)

Get the notifications masking state from a channel to an observer.

[zbus\_obs\_detach\_from\_thread](group__zbus__apis.md#ga493c125c31e44d5a222f0e9c6d01249e)

int zbus\_obs\_detach\_from\_thread(const struct zbus\_observer \*obs)

Clear the observer thread priority by detaching it from a thread.

[zbus\_chan\_pub\_stats\_count](group__zbus__apis.md#ga5648bf527de4aff89648a34bf8a7539a)

static uint32\_t zbus\_chan\_pub\_stats\_count(const struct zbus\_channel \*chan)

Get the number of times a channel has been published to.

**Definition** zbus.h:825

[zbus\_obs\_name](group__zbus__apis.md#ga5bb33ec5b914e6cbc87fa70bf763ad15)

static const char \* zbus\_obs\_name(const struct zbus\_observer \*obs)

Get the observer's name.

**Definition** zbus.h:992

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

**Definition** zbus.h:117

[zbus\_chan\_msg\_size](group__zbus__apis.md#ga8895a18b282ca2fe7528b4e5cf48e025)

static uint16\_t zbus\_chan\_msg\_size(const struct zbus\_channel \*chan)

Get the channel's message size.

**Definition** zbus.h:737

[zbus\_obs\_set\_chan\_notification\_mask](group__zbus__apis.md#ga9513264f912f54b60c4341642f578e5a)

int zbus\_obs\_set\_chan\_notification\_mask(const struct zbus\_observer \*obs, const struct zbus\_channel \*chan, bool masked)

Mask notifications from a channel to an observer.

[zbus\_obs\_set\_enable](group__zbus__apis.md#ga96767314e040e42609867a36684a6349)

int zbus\_obs\_set\_enable(const struct zbus\_observer \*obs, bool enabled)

Change the observer state.

[zbus\_chan\_msg](group__zbus__apis.md#gaaf8b34113b7b993438bd42db64812572)

static void \* zbus\_chan\_msg(const struct zbus\_channel \*chan)

Get the reference for a channel message directly.

**Definition** zbus.h:700

[zbus\_iterate\_over\_channels\_with\_user\_data](group__zbus__apis.md#gab8df108b0238757ff631ec1e120fa2c3)

bool zbus\_iterate\_over\_channels\_with\_user\_data(bool(\*iterator\_func)(const struct zbus\_channel \*chan, void \*user\_data), void \*user\_data)

Iterate over channels with user data.

[zbus\_obs\_attach\_to\_thread](group__zbus__apis.md#gabecf160e4d468d0275ad79e22fd0fb5b)

int zbus\_obs\_attach\_to\_thread(const struct zbus\_observer \*obs)

Set the observer thread priority by attaching it to a thread.

[zbus\_chan\_user\_data](group__zbus__apis.md#gac0b0ed0356fca5a8b65a3332931a369a)

static void \* zbus\_chan\_user\_data(const struct zbus\_channel \*chan)

Get the channel's user data.

**Definition** zbus.h:753

[zbus\_chan\_pub\_stats\_last\_time](group__zbus__apis.md#gac5dff9990d709d736b30f36d68c0297b)

static k\_ticks\_t zbus\_chan\_pub\_stats\_last\_time(const struct zbus\_channel \*chan)

Get the time a channel was last published to.

**Definition** zbus.h:809

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

**Definition** zbus.h:792

[zbus\_sub\_wait\_msg](group__zbus__apis.md#gaeffce45446509e488192a4e6442453fb)

int zbus\_sub\_wait\_msg(const struct zbus\_observer \*sub, const struct zbus\_channel \*\*chan, void \*msg, k\_timeout\_t timeout)

Wait for a channel message.

[zbus\_chan\_const\_msg](group__zbus__apis.md#gafee07c355df9ac86b85e601196b56a10)

static const void \* zbus\_chan\_const\_msg(const struct zbus\_channel \*chan)

Get a constant reference for a channel message directly.

**Definition** zbus.h:721

[ZBUS\_OBSERVER\_LISTENER\_TYPE](group__zbus__apis.md#gga88941281d7bdd24f3cfbb53e57711d8fa127f19c2121c9c512da9dbcbb301320c)

@ ZBUS\_OBSERVER\_LISTENER\_TYPE

**Definition** zbus.h:118

[ZBUS\_OBSERVER\_SUBSCRIBER\_TYPE](group__zbus__apis.md#gga88941281d7bdd24f3cfbb53e57711d8fa22c784a85353545e8dca2ce7a0ec81b3)

@ ZBUS\_OBSERVER\_SUBSCRIBER\_TYPE

**Definition** zbus.h:119

[ZBUS\_OBSERVER\_MSG\_SUBSCRIBER\_TYPE](group__zbus__apis.md#gga88941281d7bdd24f3cfbb53e57711d8fa8151f9e58a5bd96449bd2f9f8695538c)

@ ZBUS\_OBSERVER\_MSG\_SUBSCRIBER\_TYPE

**Definition** zbus.h:120

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

**Definition** kernel.h:2495

[k\_msgq](structk__msgq.md)

Message Queue Structure.

**Definition** kernel.h:4552

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

**Definition** zbus.h:100

[zbus\_channel::id](structzbus__channel.md#a438ff0d8bf5a1d05af2f16f737c40d4f)

uint32\_t id

Unique numeric channel identifier.

**Definition** zbus.h:87

[zbus\_channel::data](structzbus__channel.md#a5588983f2aefce2dd7cffad564c68d16)

struct zbus\_channel\_data \* data

Mutable channel data struct.

**Definition** zbus.h:109

[zbus\_channel::validator](structzbus__channel.md#a90558613c362e75aa621cb240b178138)

bool(\* validator)(const void \*msg, size\_t msg\_size)

Message validator.

**Definition** zbus.h:106

[zbus\_channel::message\_size](structzbus__channel.md#ab7f330f3d70774afeebb74cc03f90d34)

size\_t message\_size

Message size.

**Definition** zbus.h:95

[zbus\_channel::name](structzbus__channel.md#ab8e66cdcfd2429058ca86e6af3813e03)

const char \* name

Channel name.

**Definition** zbus.h:83

[zbus\_channel::message](structzbus__channel.md#abc00c2ed80b4ce3a0ea7304f43f30d08)

void \* message

Message reference.

**Definition** zbus.h:92

[zbus\_observer\_data](structzbus__observer__data.md)

**Definition** zbus.h:123

[zbus\_observer\_data::enabled](structzbus__observer__data.md#ad16ca7a9e83f54afd75f6accf471eb91)

bool enabled

Enabled flag.

**Definition** zbus.h:125

[zbus\_observer](structzbus__observer.md)

Type used to represent an observer.

**Definition** zbus.h:148

[zbus\_observer::type](structzbus__observer.md#a0251cf9bdca418b6b8123b998b57efe2)

enum zbus\_observer\_type type

Type indication.

**Definition** zbus.h:154

[zbus\_observer::message\_fifo](structzbus__observer.md#a3594b07a2573e03b18ca640809ffd3fa)

struct k\_fifo \* message\_fifo

Observer message FIFO.

**Definition** zbus.h:170

[zbus\_observer::callback](structzbus__observer.md#a78037ed7bcba26af33b6221bf7e4f9d2)

void(\* callback)(const struct zbus\_channel \*chan)

Observer callback function.

**Definition** zbus.h:164

[zbus\_observer::data](structzbus__observer.md#abdca15310be41ea2ce1ae3bbe0ebabb7)

struct zbus\_observer\_data \* data

Mutable observer data struct.

**Definition** zbus.h:157

[zbus\_observer::queue](structzbus__observer.md#ac03ca78cff09b9466cbe34921862d27c)

struct k\_msgq \* queue

Observer message queue.

**Definition** zbus.h:161

[zbus\_observer::name](structzbus__observer.md#ad9d31821d69e181f28e80e5eedf5a331)

const char \* name

Observer name.

**Definition** zbus.h:151

[iterable\_sections.h](sys_2iterable__sections_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [zbus](dir_4ac3b76b03f02d08133e5af61546c3d3.md)
- [zbus.h](zbus_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
