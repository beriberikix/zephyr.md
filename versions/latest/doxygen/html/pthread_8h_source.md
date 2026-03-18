---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/pthread_8h_source.html
original_path: doxygen/html/pthread_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

pthread.h

[Go to the documentation of this file.](pthread_8h.md)

1/\*

2 \* Copyright (c) 2017 Intel Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_POSIX\_PTHREAD\_H\_

8#define ZEPHYR\_INCLUDE\_POSIX\_PTHREAD\_H\_

9

10#include <[stdlib.h](stdlib_8h.md)>

11#include <[string.h](string_8h.md)>

12

13#include <[zephyr/kernel.h](include_2zephyr_2kernel_8h.md)>

14#include <[zephyr/posix/time.h](include_2zephyr_2posix_2time_8h.md)>

15#include <[zephyr/posix/unistd.h](unistd_8h.md)>

16#include <[zephyr/posix/sched.h](posix_2sched_8h.md)>

17

18#ifdef \_\_cplusplus

19extern "C" {

20#endif

21

22/\*

23 \* Pthread detach/joinable

24 \* Undefine possibly predefined values by external toolchain headers

25 \*/

26#undef PTHREAD\_CREATE\_DETACHED

[ 27](pthread_8h.md#a391c5eb0f6b5febc48710d0be3f62394)#define PTHREAD\_CREATE\_DETACHED 1

28#undef PTHREAD\_CREATE\_JOINABLE

[ 29](pthread_8h.md#afb10d234d831c7b57768d62786748bc7)#define PTHREAD\_CREATE\_JOINABLE 0

30

31/\* Pthread resource visibility \*/

[ 32](pthread_8h.md#a443f2f512de9324bf77625041ecb04f4)#define PTHREAD\_PROCESS\_PRIVATE 0

[ 33](pthread_8h.md#a07f3670a510cdb93233e84e1a0b50e89)#define PTHREAD\_PROCESS\_SHARED 1

34

35/\* Pthread cancellation \*/

[ 36](pthread_8h.md#a17ddda04a6c1ee32116c49c85e2ac4ae)#define PTHREAD\_CANCELED ((void \*)-1)

[ 37](pthread_8h.md#aaf18882a8a6b82c7b7849a645f4445ef)#define PTHREAD\_CANCEL\_ENABLE 0

[ 38](pthread_8h.md#a6c661332f782dcebc87b878990424b4c)#define PTHREAD\_CANCEL\_DISABLE 1

[ 39](pthread_8h.md#a7559901d88e4d3b8100b407e164cd75e)#define PTHREAD\_CANCEL\_DEFERRED 0

[ 40](pthread_8h.md#aae774738da39ed214c9b01f342222686)#define PTHREAD\_CANCEL\_ASYNCHRONOUS 1

41

42/\* Passed to pthread\_once \*/

[ 43](pthread_8h.md#a59e22497b65fc305ddb5cea8b4990b51)#define PTHREAD\_ONCE\_INIT {0}

44

45/\* The minimum allowable stack size \*/

[ 46](pthread_8h.md#a8b3dc1c5c1a165d6143b1dce950e8266)#define PTHREAD\_STACK\_MIN Z\_KERNEL\_STACK\_SIZE\_ADJUST(0)

47

[ 53](pthread_8h.md#aa7b867fe46f3660283fcb356c4fcbbf0)#define PTHREAD\_COND\_INITIALIZER (-1)

54

[ 60](pthread_8h.md#a319a61cdb25d069c9d4504e8225fd0c3)int [pthread\_cond\_init](pthread_8h.md#a319a61cdb25d069c9d4504e8225fd0c3)([pthread\_cond\_t](posix__types_8h.md#a1b893f49dfdf497be09c04a0e40f425e) \*cv, const pthread\_condattr\_t \*att);

61

[ 67](pthread_8h.md#a8d44e4eae235f675bbab1b9163a3bc1d)int [pthread\_cond\_destroy](pthread_8h.md#a8d44e4eae235f675bbab1b9163a3bc1d)([pthread\_cond\_t](posix__types_8h.md#a1b893f49dfdf497be09c04a0e40f425e) \*cv);

68

[ 74](pthread_8h.md#add1fea97e50755b5dbf4bd9a83b710dd)int [pthread\_cond\_signal](pthread_8h.md#add1fea97e50755b5dbf4bd9a83b710dd)([pthread\_cond\_t](posix__types_8h.md#a1b893f49dfdf497be09c04a0e40f425e) \*cv);

75

[ 81](pthread_8h.md#a91ff7fff67462ce9216d299c89683119)int [pthread\_cond\_broadcast](pthread_8h.md#a91ff7fff67462ce9216d299c89683119)([pthread\_cond\_t](posix__types_8h.md#a1b893f49dfdf497be09c04a0e40f425e) \*cv);

82

[ 88](pthread_8h.md#a61a1bf88d32de361e82ef4ea99b47322)int [pthread\_cond\_wait](pthread_8h.md#a61a1bf88d32de361e82ef4ea99b47322)([pthread\_cond\_t](posix__types_8h.md#a1b893f49dfdf497be09c04a0e40f425e) \*cv, [pthread\_mutex\_t](posix__types_8h.md#a465eb2b962de164efdc8ce957025de7e) \*mut);

89

[ 95](pthread_8h.md#aecea498fbd2df02942790e5ccd7d78b2)int [pthread\_cond\_timedwait](pthread_8h.md#aecea498fbd2df02942790e5ccd7d78b2)([pthread\_cond\_t](posix__types_8h.md#a1b893f49dfdf497be09c04a0e40f425e) \*cv, [pthread\_mutex\_t](posix__types_8h.md#a465eb2b962de164efdc8ce957025de7e) \*mut,

96 const struct [timespec](structtimespec.md) \*abstime);

97

[ 104](pthread_8h.md#a01159da320b2317ee286a7e92d713f16)int [pthread\_condattr\_init](pthread_8h.md#a01159da320b2317ee286a7e92d713f16)(pthread\_condattr\_t \*att);

105

[ 112](pthread_8h.md#af37eaf73f0d83989d8efc06e676909f1)int [pthread\_condattr\_destroy](pthread_8h.md#af37eaf73f0d83989d8efc06e676909f1)(pthread\_condattr\_t \*att);

113

[ 120](pthread_8h.md#a77376b018eec6db2986939b847915a3c)int [pthread\_condattr\_getclock](pthread_8h.md#a77376b018eec6db2986939b847915a3c)(const pthread\_condattr\_t \*[ZRESTRICT](common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) att,

121 [clockid\_t](posix__types_8h.md#aac50bafb9f9a838df14fab213146caea) \*[ZRESTRICT](common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) clock\_id);

122

129

[ 130](pthread_8h.md#ac0b4f6d49deeab0ddb269a23ee303156)int [pthread\_condattr\_setclock](pthread_8h.md#ac0b4f6d49deeab0ddb269a23ee303156)(pthread\_condattr\_t \*att, [clockid\_t](posix__types_8h.md#aac50bafb9f9a838df14fab213146caea) clock\_id);

131

[ 137](pthread_8h.md#a84e55100366a6a8338a2af3b3f279686)#define PTHREAD\_MUTEX\_INITIALIZER (-1)

138

[ 144](pthread_8h.md#aa92fd7b492a8a5b31b2f8b3b6039c622)#define PTHREAD\_RWLOCK\_INITIALIZER (-1)

145

146/\*

147 \* Mutex attributes - type

148 \*

149 \* PTHREAD\_MUTEX\_NORMAL: Owner of mutex cannot relock it. Attempting

150 \* to relock will cause deadlock.

151 \* PTHREAD\_MUTEX\_RECURSIVE: Owner can relock the mutex.

152 \* PTHREAD\_MUTEX\_ERRORCHECK: If owner attempts to relock the mutex, an

153 \* error is returned.

154 \*

155 \*/

[ 156](pthread_8h.md#aae4b650085c2599674938f503d6253cf)#define PTHREAD\_MUTEX\_NORMAL 0

[ 157](pthread_8h.md#a715e9644a7183d98cb2c9dd41cb89645)#define PTHREAD\_MUTEX\_RECURSIVE 1

[ 158](pthread_8h.md#aaf502496651f95b06be861af7902cb23)#define PTHREAD\_MUTEX\_ERRORCHECK 2

[ 159](pthread_8h.md#a2a9b96c0491ae490c17d0b400bc427b0)#define PTHREAD\_MUTEX\_DEFAULT PTHREAD\_MUTEX\_NORMAL

160

161/\*

162 \* Mutex attributes - protocol

163 \*

164 \* PTHREAD\_PRIO\_NONE: Ownership of mutex does not affect priority.

165 \* PTHREAD\_PRIO\_INHERIT: Owner's priority is boosted to the priority of

166 \* highest priority thread blocked on the mutex.

167 \* PTHREAD\_PRIO\_PROTECT: Mutex has a priority ceiling. The owner's

168 \* priority is boosted to the highest priority ceiling of all mutexes

169 \* owned (regardless of whether or not other threads are blocked on

170 \* any of these mutexes).

171 \* FIXME: Only PRIO\_NONE is supported. Implement other protocols.

172 \*/

[ 173](pthread_8h.md#a8c1426a72025b27d9726580ac0e8404f)#define PTHREAD\_PRIO\_NONE 0

174

[ 180](pthread_8h.md#af89d9cfa300f33b46720a96eac83d175)int [pthread\_mutex\_destroy](pthread_8h.md#af89d9cfa300f33b46720a96eac83d175)([pthread\_mutex\_t](posix__types_8h.md#a465eb2b962de164efdc8ce957025de7e) \*m);

181

[ 187](pthread_8h.md#afd70d6f2c50e22b996c926fb9d6ad291)int [pthread\_mutex\_lock](pthread_8h.md#afd70d6f2c50e22b996c926fb9d6ad291)([pthread\_mutex\_t](posix__types_8h.md#a465eb2b962de164efdc8ce957025de7e) \*m);

188

[ 194](pthread_8h.md#a02a3c64dac70730e226c31c0e7dbb45c)int [pthread\_mutex\_unlock](pthread_8h.md#a02a3c64dac70730e226c31c0e7dbb45c)([pthread\_mutex\_t](posix__types_8h.md#a465eb2b962de164efdc8ce957025de7e) \*m);

195

201

[ 202](pthread_8h.md#abbec44a62531009629601fbb34f1027c)int [pthread\_mutex\_timedlock](pthread_8h.md#abbec44a62531009629601fbb34f1027c)([pthread\_mutex\_t](posix__types_8h.md#a465eb2b962de164efdc8ce957025de7e) \*m,

203 const struct [timespec](structtimespec.md) \*abstime);

204

[ 210](pthread_8h.md#acc1ccbaf3d76572da85a8030bba1ede4)int [pthread\_mutex\_trylock](pthread_8h.md#acc1ccbaf3d76572da85a8030bba1ede4)([pthread\_mutex\_t](posix__types_8h.md#a465eb2b962de164efdc8ce957025de7e) \*m);

211

[ 217](pthread_8h.md#a7948bc0ea8a33439aece34d0fb3daf8b)int [pthread\_mutex\_init](pthread_8h.md#a7948bc0ea8a33439aece34d0fb3daf8b)([pthread\_mutex\_t](posix__types_8h.md#a465eb2b962de164efdc8ce957025de7e) \*m,

218 const pthread\_mutexattr\_t \*att);

219

[ 225](pthread_8h.md#ae7e6584c2b2cf9b9ff061115d2342bb5)int [pthread\_mutexattr\_setprotocol](pthread_8h.md#ae7e6584c2b2cf9b9ff061115d2342bb5)(pthread\_mutexattr\_t \*attr, int protocol);

226

[ 232](pthread_8h.md#a8387c80e660e9426f801ac0217ecfae5)int [pthread\_mutexattr\_settype](pthread_8h.md#a8387c80e660e9426f801ac0217ecfae5)(pthread\_mutexattr\_t \*attr, int type);

233

[ 239](pthread_8h.md#a200fcbc9157e6183376f83bc0e5937dd)int [pthread\_mutexattr\_getprotocol](pthread_8h.md#a200fcbc9157e6183376f83bc0e5937dd)(const pthread\_mutexattr\_t \*attr,

240 int \*protocol);

241

[ 247](pthread_8h.md#a7f064a4db96a009a5a9a7c7e5cc03599)int [pthread\_mutexattr\_gettype](pthread_8h.md#a7f064a4db96a009a5a9a7c7e5cc03599)(const pthread\_mutexattr\_t \*attr, int \*type);

248

[ 256](pthread_8h.md#a5eb25214d1409ff80e25559875a6b009)static inline int [pthread\_mutexattr\_init](pthread_8h.md#a5eb25214d1409ff80e25559875a6b009)(pthread\_mutexattr\_t \*m)

257{

258 ARG\_UNUSED(m);

259

260 return 0;

261}

262

[ 270](pthread_8h.md#a6422431160421ef5e69da9e98fd19580)static inline int [pthread\_mutexattr\_destroy](pthread_8h.md#a6422431160421ef5e69da9e98fd19580)(pthread\_mutexattr\_t \*m)

271{

272 ARG\_UNUSED(m);

273

274 return 0;

275}

276

[ 289](pthread_8h.md#af63f456fc30f008794402605b4e5ac9c)#define PTHREAD\_BARRIER\_DEFINE(name, count) pthread\_barrier\_t name = -1 \_\_DEPRECATED\_MACRO

290

[ 291](pthread_8h.md#a822c63bc662ad86cfb2dcec50edbb42b)#define PTHREAD\_BARRIER\_SERIAL\_THREAD 1

292

293/\*

294 \* Barrier attributes - type

295 \*/

296#define PTHREAD\_PROCESS\_PRIVATE 0

[ 297](pthread_8h.md#afff2f9c2b019a07298f341cf70ee829d)#define PTHREAD\_PROCESS\_PUBLIC 1

298

[ 304](pthread_8h.md#af786372165ba080986ae4143928c5436)int [pthread\_barrier\_wait](pthread_8h.md#af786372165ba080986ae4143928c5436)([pthread\_barrier\_t](posix__types_8h.md#aeb637552f63e4c249e7aaeb2905f3db2) \*b);

305

[ 311](pthread_8h.md#aecc6c99901aac517072970e153863296)int [pthread\_barrier\_init](pthread_8h.md#aecc6c99901aac517072970e153863296)([pthread\_barrier\_t](posix__types_8h.md#aeb637552f63e4c249e7aaeb2905f3db2) \*b, const [pthread\_barrierattr\_t](posix__types_8h.md#a24d58850626c8022bf4bbd5d2628615b) \*attr,

312 unsigned int count);

313

[ 319](pthread_8h.md#ab05ae13769e61dea9c53ca7894743c8f)int [pthread\_barrier\_destroy](pthread_8h.md#ab05ae13769e61dea9c53ca7894743c8f)([pthread\_barrier\_t](posix__types_8h.md#aeb637552f63e4c249e7aaeb2905f3db2) \*b);

320

[ 326](pthread_8h.md#ad540451ab679ace869b51c7cbb7b8486)int [pthread\_barrierattr\_init](pthread_8h.md#ad540451ab679ace869b51c7cbb7b8486)([pthread\_barrierattr\_t](posix__types_8h.md#a24d58850626c8022bf4bbd5d2628615b) \*b);

327

[ 333](pthread_8h.md#a5e27d4773f3d0552e36f2ff3b922a988)int [pthread\_barrierattr\_destroy](pthread_8h.md#a5e27d4773f3d0552e36f2ff3b922a988)([pthread\_barrierattr\_t](posix__types_8h.md#a24d58850626c8022bf4bbd5d2628615b) \*b);

334

[ 340](pthread_8h.md#aa9c3c335f5bcf702fe85a1c12dcdc70e)int [pthread\_barrierattr\_setpshared](pthread_8h.md#aa9c3c335f5bcf702fe85a1c12dcdc70e)([pthread\_barrierattr\_t](posix__types_8h.md#a24d58850626c8022bf4bbd5d2628615b) \*attr, int pshared);

341

[ 347](pthread_8h.md#a54e367403c0524680115b780ccfbc586)int [pthread\_barrierattr\_getpshared](pthread_8h.md#a54e367403c0524680115b780ccfbc586)(const [pthread\_barrierattr\_t](posix__types_8h.md#a24d58850626c8022bf4bbd5d2628615b) \*[ZRESTRICT](common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) attr,

348 int \*[ZRESTRICT](common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) pshared);

349

350/\* Predicates and setters for various pthread attribute values that we

351 \* don't support (or always support: the "process shared" attribute

352 \* can only be true given the way Zephyr implements these

353 \* objects). Leave these undefined for simplicity instead of defining

354 \* stubs to return an error that would have to be logged and

355 \* interpreted just to figure out that we didn't support it in the

356 \* first place. These APIs are very rarely used even in production

357 \* Unix code. Leave the declarations here so they can be easily

358 \* uncommented and implemented as needed.

359

360int pthread\_condattr\_getpshared(const pthread\_condattr\_t \* int \*);

361int pthread\_condattr\_setpshared(pthread\_condattr\_t \*, int);

362int pthread\_mutex\_consistent(pthread\_mutex\_t \*);

363int pthread\_mutex\_getprioceiling(const pthread\_mutex\_t \* int \*);

364int pthread\_mutex\_setprioceiling(pthread\_mutex\_t \*, int int \*);

365int pthread\_mutexattr\_getprioceiling(const pthread\_mutexattr\_t \*, int \*);

366int pthread\_mutexattr\_getpshared(const pthread\_mutexattr\_t \* int \*);

367int pthread\_mutexattr\_getrobust(const pthread\_mutexattr\_t \* int \*);

368int pthread\_mutexattr\_setprioceiling(pthread\_mutexattr\_t \*, int);

369int pthread\_mutexattr\_setpshared(pthread\_mutexattr\_t \*, int);

370int pthread\_mutexattr\_setrobust(pthread\_mutexattr\_t \*, int);

371\*/

372

373/\* Base Pthread related APIs \*/

374

[ 383](pthread_8h.md#a4c4f5f3b4f8f45d9d897847d53b11aaa)[pthread\_t](posix__types_8h.md#a405938c67e9c568fde9993c7e14d58ec) [pthread\_self](pthread_8h.md#a4c4f5f3b4f8f45d9d897847d53b11aaa)(void);

384

[ 390](pthread_8h.md#a2a460fe3d4e4518057366f6ead455f4a)int [pthread\_equal](pthread_8h.md#a2a460fe3d4e4518057366f6ead455f4a)([pthread\_t](posix__types_8h.md#a405938c67e9c568fde9993c7e14d58ec) pt1, [pthread\_t](posix__types_8h.md#a405938c67e9c568fde9993c7e14d58ec) pt2);

391

[ 397](pthread_8h.md#ac4d2dcfe790eee1dbd83a1db7fdce3dc)static inline int [pthread\_rwlockattr\_destroy](pthread_8h.md#ac4d2dcfe790eee1dbd83a1db7fdce3dc)([pthread\_rwlockattr\_t](posix__types_8h.md#a4e92e3fbb4be682babbb6796af90b50f) \*attr)

398{

399 ARG\_UNUSED(attr);

400 return 0;

401}

402

[ 408](pthread_8h.md#a78db2cd33976f604cf85662fffa28307)static inline int [pthread\_rwlockattr\_init](pthread_8h.md#a78db2cd33976f604cf85662fffa28307)([pthread\_rwlockattr\_t](posix__types_8h.md#a4e92e3fbb4be682babbb6796af90b50f) \*attr)

409{

410 ARG\_UNUSED(attr);

411 return 0;

412}

413

[ 414](pthread_8h.md#abee3ae43d1f00b597111f6f82b0416a1)int [pthread\_attr\_getguardsize](pthread_8h.md#abee3ae43d1f00b597111f6f82b0416a1)(const pthread\_attr\_t \*[ZRESTRICT](common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) attr, size\_t \*[ZRESTRICT](common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) guardsize);

[ 415](pthread_8h.md#ae23600d4670359ab12bfba20db2c9a37)int [pthread\_attr\_getstacksize](pthread_8h.md#ae23600d4670359ab12bfba20db2c9a37)(const pthread\_attr\_t \*attr, size\_t \*stacksize);

[ 416](pthread_8h.md#a532b31c11a9d87663053c5342400758c)int [pthread\_attr\_setguardsize](pthread_8h.md#a532b31c11a9d87663053c5342400758c)(pthread\_attr\_t \*attr, size\_t guardsize);

[ 417](pthread_8h.md#a812a9a455ae2ef2bb0dca4fff201a281)int [pthread\_attr\_setstacksize](pthread_8h.md#a812a9a455ae2ef2bb0dca4fff201a281)(pthread\_attr\_t \*attr, size\_t stacksize);

[ 418](pthread_8h.md#a79b4c9e71486a87ef3014f1c660b33eb)int [pthread\_attr\_setschedpolicy](pthread_8h.md#a79b4c9e71486a87ef3014f1c660b33eb)(pthread\_attr\_t \*attr, int policy);

[ 419](pthread_8h.md#af032906f326f3c209c7eed6bb248ebee)int [pthread\_attr\_getschedpolicy](pthread_8h.md#af032906f326f3c209c7eed6bb248ebee)(const pthread\_attr\_t \*attr, int \*policy);

[ 420](pthread_8h.md#ae6ee78c307d8467b34a9b0c330993a54)int [pthread\_attr\_setdetachstate](pthread_8h.md#ae6ee78c307d8467b34a9b0c330993a54)(pthread\_attr\_t \*attr, int detachstate);

[ 421](pthread_8h.md#a391c34da42e68ddd24f5ee0c070d5c4f)int [pthread\_attr\_getdetachstate](pthread_8h.md#a391c34da42e68ddd24f5ee0c070d5c4f)(const pthread\_attr\_t \*attr, int \*detachstate);

[ 422](pthread_8h.md#a0b85ebb1e3aac081a4c0a5e85ae3cbe9)int [pthread\_attr\_init](pthread_8h.md#a0b85ebb1e3aac081a4c0a5e85ae3cbe9)(pthread\_attr\_t \*attr);

[ 423](pthread_8h.md#a4bcdbf47c17c7dcc51e9f05f5cb56d81)int [pthread\_attr\_destroy](pthread_8h.md#a4bcdbf47c17c7dcc51e9f05f5cb56d81)(pthread\_attr\_t \*attr);

[ 424](pthread_8h.md#abcd67baa86ff65d7ce65985d8b50d579)int [pthread\_attr\_getschedparam](pthread_8h.md#abcd67baa86ff65d7ce65985d8b50d579)(const pthread\_attr\_t \*attr,

425 struct sched\_param \*schedparam);

[ 426](pthread_8h.md#ac60393667965dbd06670d3d280b65757)int [pthread\_getschedparam](pthread_8h.md#ac60393667965dbd06670d3d280b65757)([pthread\_t](posix__types_8h.md#a405938c67e9c568fde9993c7e14d58ec) pthread, int \*policy,

427 struct sched\_param \*param);

[ 428](pthread_8h.md#aec19ad460995a9fe8aeb4eaf2bb1ed1d)int [pthread\_attr\_getstack](pthread_8h.md#aec19ad460995a9fe8aeb4eaf2bb1ed1d)(const pthread\_attr\_t \*attr,

429 void \*\*stackaddr, size\_t \*stacksize);

[ 430](pthread_8h.md#a94ede89b99a3a4fa17e516d30aaf3409)int [pthread\_attr\_setstack](pthread_8h.md#a94ede89b99a3a4fa17e516d30aaf3409)(pthread\_attr\_t \*attr, void \*stackaddr,

431 size\_t stacksize);

432#ifdef CONFIG\_PTHREAD\_IPC

433int [pthread\_once](structpthread__once.md)(pthread\_once\_t \*once, void (\*initFunc)(void));

434#endif

[ 435](pthread_8h.md#ab9a027122b38833e8c2e1c0e733da3e6)FUNC\_NORETURN void [pthread\_exit](pthread_8h.md#ab9a027122b38833e8c2e1c0e733da3e6)(void \*retval);

[ 436](pthread_8h.md#a6e4d503c2b358be5c98330f9006b3417)int [pthread\_join](pthread_8h.md#a6e4d503c2b358be5c98330f9006b3417)([pthread\_t](posix__types_8h.md#a405938c67e9c568fde9993c7e14d58ec) thread, void \*\*status);

[ 437](pthread_8h.md#a66a8f4bac5afe05538794218ff7c85ea)int [pthread\_cancel](pthread_8h.md#a66a8f4bac5afe05538794218ff7c85ea)([pthread\_t](posix__types_8h.md#a405938c67e9c568fde9993c7e14d58ec) pthread);

[ 438](pthread_8h.md#a7c275c509c26566b6dd95a2de1668a2f)int [pthread\_detach](pthread_8h.md#a7c275c509c26566b6dd95a2de1668a2f)([pthread\_t](posix__types_8h.md#a405938c67e9c568fde9993c7e14d58ec) thread);

[ 439](pthread_8h.md#acb010e074930d81533ed20d319ca80b1)int [pthread\_create](pthread_8h.md#acb010e074930d81533ed20d319ca80b1)([pthread\_t](posix__types_8h.md#a405938c67e9c568fde9993c7e14d58ec) \*newthread, const pthread\_attr\_t \*attr,

440 void \*(\*threadroutine)(void \*), void \*arg);

[ 441](pthread_8h.md#a37075410fbbaad7ee93c95375fc86e0e)int [pthread\_setcancelstate](pthread_8h.md#a37075410fbbaad7ee93c95375fc86e0e)(int [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90), int \*oldstate);

[ 442](pthread_8h.md#aab579bcfcf0662a0c1e35fd82162e61d)int [pthread\_setcanceltype](pthread_8h.md#aab579bcfcf0662a0c1e35fd82162e61d)(int type, int \*oldtype);

[ 443](pthread_8h.md#af1c95282ab2bea25f0888a19652cd41f)void [pthread\_testcancel](pthread_8h.md#af1c95282ab2bea25f0888a19652cd41f)(void);

[ 444](pthread_8h.md#a18b9aa91fe20481a25650df20c567ff5)int [pthread\_attr\_setschedparam](pthread_8h.md#a18b9aa91fe20481a25650df20c567ff5)(pthread\_attr\_t \*attr,

445 const struct sched\_param \*schedparam);

[ 446](pthread_8h.md#ad8e89d31b56c88d632ba9aeb956fa043)int [pthread\_setschedparam](pthread_8h.md#ad8e89d31b56c88d632ba9aeb956fa043)([pthread\_t](posix__types_8h.md#a405938c67e9c568fde9993c7e14d58ec) pthread, int policy,

447 const struct sched\_param \*param);

[ 448](pthread_8h.md#a79839f0f4f4a768bf6d218faf377c209)int [pthread\_rwlock\_destroy](pthread_8h.md#a79839f0f4f4a768bf6d218faf377c209)([pthread\_rwlock\_t](posix__types_8h.md#acd12f65541fede33b6226f646e900ea6) \*rwlock);

[ 449](pthread_8h.md#a1596a13569ec35ee66cc867586fd643d)int [pthread\_rwlock\_init](pthread_8h.md#a1596a13569ec35ee66cc867586fd643d)([pthread\_rwlock\_t](posix__types_8h.md#acd12f65541fede33b6226f646e900ea6) \*rwlock,

450 const [pthread\_rwlockattr\_t](posix__types_8h.md#a4e92e3fbb4be682babbb6796af90b50f) \*attr);

[ 451](pthread_8h.md#acc16fb32464b480d31bc69cce4e206c9)int [pthread\_rwlock\_rdlock](pthread_8h.md#acc16fb32464b480d31bc69cce4e206c9)([pthread\_rwlock\_t](posix__types_8h.md#acd12f65541fede33b6226f646e900ea6) \*rwlock);

[ 452](pthread_8h.md#ad791558625e69852e4a435b7c1580468)int [pthread\_rwlock\_timedrdlock](pthread_8h.md#ad791558625e69852e4a435b7c1580468)([pthread\_rwlock\_t](posix__types_8h.md#acd12f65541fede33b6226f646e900ea6) \*rwlock,

453 const struct [timespec](structtimespec.md) \*abstime);

[ 454](pthread_8h.md#a16c935f2f6146a95f9adbca71e0455e7)int [pthread\_rwlock\_timedwrlock](pthread_8h.md#a16c935f2f6146a95f9adbca71e0455e7)([pthread\_rwlock\_t](posix__types_8h.md#acd12f65541fede33b6226f646e900ea6) \*rwlock,

455 const struct [timespec](structtimespec.md) \*abstime);

[ 456](pthread_8h.md#aae52fb1d3e6d03b18fa5731d0b49d197)int [pthread\_rwlock\_tryrdlock](pthread_8h.md#aae52fb1d3e6d03b18fa5731d0b49d197)([pthread\_rwlock\_t](posix__types_8h.md#acd12f65541fede33b6226f646e900ea6) \*rwlock);

[ 457](pthread_8h.md#a065b618f7b786ed9bc7dddef4490cefb)int [pthread\_rwlock\_trywrlock](pthread_8h.md#a065b618f7b786ed9bc7dddef4490cefb)([pthread\_rwlock\_t](posix__types_8h.md#acd12f65541fede33b6226f646e900ea6) \*rwlock);

[ 458](pthread_8h.md#a7d3b987d99117fc10c4ef97230011983)int [pthread\_rwlock\_unlock](pthread_8h.md#a7d3b987d99117fc10c4ef97230011983)([pthread\_rwlock\_t](posix__types_8h.md#acd12f65541fede33b6226f646e900ea6) \*rwlock);

[ 459](pthread_8h.md#a5ddd4cc028257f9baa9e23c2337abe3b)int [pthread\_rwlock\_wrlock](pthread_8h.md#a5ddd4cc028257f9baa9e23c2337abe3b)([pthread\_rwlock\_t](posix__types_8h.md#acd12f65541fede33b6226f646e900ea6) \*rwlock);

[ 460](pthread_8h.md#af4b7ced8ecff505380fe8216244a3764)int [pthread\_key\_create](pthread_8h.md#af4b7ced8ecff505380fe8216244a3764)(pthread\_key\_t \*key,

461 void (\*destructor)(void \*));

[ 462](pthread_8h.md#aee96306dc79294927ee840bb4de2244b)int [pthread\_key\_delete](pthread_8h.md#aee96306dc79294927ee840bb4de2244b)(pthread\_key\_t key);

[ 463](pthread_8h.md#a2187333dd46ce08d9d2e044f79fad705)int [pthread\_setspecific](pthread_8h.md#a2187333dd46ce08d9d2e044f79fad705)(pthread\_key\_t key, const void \*value);

[ 464](pthread_8h.md#acdf9f73a16ea40eba1bc174d38e76ca5)void \*[pthread\_getspecific](pthread_8h.md#acdf9f73a16ea40eba1bc174d38e76ca5)(pthread\_key\_t key);

[ 465](pthread_8h.md#a80008474c3d68e9880da960a53d2f430)int [pthread\_atfork](pthread_8h.md#a80008474c3d68e9880da960a53d2f430)(void (\*prepare)(void), void (\*parent)(void), void (\*child)(void));

[ 466](pthread_8h.md#afb4344ea91774ba279ea5df3cb656ebc)int [pthread\_getconcurrency](pthread_8h.md#afb4344ea91774ba279ea5df3cb656ebc)(void);

[ 467](pthread_8h.md#a46064892e8c4622e0a3ebe22d9792b92)int [pthread\_setconcurrency](pthread_8h.md#a46064892e8c4622e0a3ebe22d9792b92)(int new\_level);

468

469void \_\_z\_pthread\_cleanup\_push(void \*cleanup[3], void (\*routine)(void \*arg), void \*arg);

470void \_\_z\_pthread\_cleanup\_pop(int execute);

471

[ 472](pthread_8h.md#a265bda35a73d502fe8b710dc34f421cc)#define pthread\_cleanup\_push(\_rtn, \_arg) \

473 do /\* enforce '{'-like behaviour \*/ { \

474 void \*\_z\_pthread\_cleanup[3]; \

475 \_\_z\_pthread\_cleanup\_push(\_z\_pthread\_cleanup, \_rtn, \_arg)

476

[ 477](pthread_8h.md#a234ffab9eecdb6ae28198aeeedb4f10c)#define pthread\_cleanup\_pop(\_ex) \

478 \_\_z\_pthread\_cleanup\_pop(\_ex); \

479 } /\* enforce '}'-like behaviour \*/ while (0)

480

481/\* Glibc / Oracle Extension Functions \*/

482

[ 497](pthread_8h.md#aa21465e084e7185bfbb94bb50d60cd08)int [pthread\_setname\_np](pthread_8h.md#aa21465e084e7185bfbb94bb50d60cd08)([pthread\_t](posix__types_8h.md#a405938c67e9c568fde9993c7e14d58ec) thread, const char \*name);

498

[ 514](pthread_8h.md#a8d55a60492c979991dc1a361b5453813)int [pthread\_getname\_np](pthread_8h.md#a8d55a60492c979991dc1a361b5453813)([pthread\_t](posix__types_8h.md#a405938c67e9c568fde9993c7e14d58ec) thread, char \*name, size\_t len);

515

516#ifdef CONFIG\_PTHREAD\_IPC

517

523int pthread\_spin\_destroy([pthread\_spinlock\_t](posix__types_8h.md#a1d9c308dd59bf38ff0a7a45020d0aefa) \*lock);

524

530int pthread\_spin\_init([pthread\_spinlock\_t](posix__types_8h.md#a1d9c308dd59bf38ff0a7a45020d0aefa) \*lock, int pshared);

531

537int pthread\_spin\_lock([pthread\_spinlock\_t](posix__types_8h.md#a1d9c308dd59bf38ff0a7a45020d0aefa) \*lock);

538

544int pthread\_spin\_trylock([pthread\_spinlock\_t](posix__types_8h.md#a1d9c308dd59bf38ff0a7a45020d0aefa) \*lock);

545

551int pthread\_spin\_unlock([pthread\_spinlock\_t](posix__types_8h.md#a1d9c308dd59bf38ff0a7a45020d0aefa) \*lock);

552

553#endif

554

555#ifdef \_\_cplusplus

556}

557#endif

558

559#endif /\* ZEPHYR\_INCLUDE\_POSIX\_PTHREAD\_H\_ \*/

[ZRESTRICT](common_8h.md#a39314fd705c5a9ed45b671ca36f883fd)

#define ZRESTRICT

**Definition** common.h:36

[kernel.h](include_2zephyr_2kernel_8h.md)

Public kernel APIs.

[time.h](include_2zephyr_2posix_2time_8h.md)

[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)

state

**Definition** parser\_state.h:29

[sched.h](posix_2sched_8h.md)

[pthread\_cond\_t](posix__types_8h.md#a1b893f49dfdf497be09c04a0e40f425e)

uint32\_t pthread\_cond\_t

**Definition** posix\_types.h:72

[pthread\_spinlock\_t](posix__types_8h.md#a1d9c308dd59bf38ff0a7a45020d0aefa)

uint32\_t pthread\_spinlock\_t

**Definition** posix\_types.h:54

[pthread\_barrierattr\_t](posix__types_8h.md#a24d58850626c8022bf4bbd5d2628615b)

struct pthread\_barrierattr pthread\_barrierattr\_t

[pthread\_t](posix__types_8h.md#a405938c67e9c568fde9993c7e14d58ec)

uint32\_t pthread\_t

**Definition** posix\_types.h:53

[pthread\_mutex\_t](posix__types_8h.md#a465eb2b962de164efdc8ce957025de7e)

uint32\_t pthread\_mutex\_t

**Definition** posix\_types.h:60

[pthread\_rwlockattr\_t](posix__types_8h.md#a4e92e3fbb4be682babbb6796af90b50f)

uint32\_t pthread\_rwlockattr\_t

**Definition** posix\_types.h:91

[clockid\_t](posix__types_8h.md#aac50bafb9f9a838df14fab213146caea)

uint32\_t clockid\_t

**Definition** posix\_types.h:33

[pthread\_rwlock\_t](posix__types_8h.md#acd12f65541fede33b6226f646e900ea6)

uint32\_t pthread\_rwlock\_t

**Definition** posix\_types.h:93

[pthread\_barrier\_t](posix__types_8h.md#aeb637552f63e4c249e7aaeb2905f3db2)

uint32\_t pthread\_barrier\_t

**Definition** posix\_types.h:85

[pthread\_condattr\_init](pthread_8h.md#a01159da320b2317ee286a7e92d713f16)

int pthread\_condattr\_init(pthread\_condattr\_t \*att)

POSIX threading compatibility API.

[pthread\_mutex\_unlock](pthread_8h.md#a02a3c64dac70730e226c31c0e7dbb45c)

int pthread\_mutex\_unlock(pthread\_mutex\_t \*m)

POSIX threading compatibility API.

[pthread\_rwlock\_trywrlock](pthread_8h.md#a065b618f7b786ed9bc7dddef4490cefb)

int pthread\_rwlock\_trywrlock(pthread\_rwlock\_t \*rwlock)

[pthread\_attr\_init](pthread_8h.md#a0b85ebb1e3aac081a4c0a5e85ae3cbe9)

int pthread\_attr\_init(pthread\_attr\_t \*attr)

[pthread\_rwlock\_init](pthread_8h.md#a1596a13569ec35ee66cc867586fd643d)

int pthread\_rwlock\_init(pthread\_rwlock\_t \*rwlock, const pthread\_rwlockattr\_t \*attr)

[pthread\_rwlock\_timedwrlock](pthread_8h.md#a16c935f2f6146a95f9adbca71e0455e7)

int pthread\_rwlock\_timedwrlock(pthread\_rwlock\_t \*rwlock, const struct timespec \*abstime)

[pthread\_attr\_setschedparam](pthread_8h.md#a18b9aa91fe20481a25650df20c567ff5)

int pthread\_attr\_setschedparam(pthread\_attr\_t \*attr, const struct sched\_param \*schedparam)

[pthread\_mutexattr\_getprotocol](pthread_8h.md#a200fcbc9157e6183376f83bc0e5937dd)

int pthread\_mutexattr\_getprotocol(const pthread\_mutexattr\_t \*attr, int \*protocol)

POSIX threading compatibility API.

[pthread\_setspecific](pthread_8h.md#a2187333dd46ce08d9d2e044f79fad705)

int pthread\_setspecific(pthread\_key\_t key, const void \*value)

[pthread\_equal](pthread_8h.md#a2a460fe3d4e4518057366f6ead455f4a)

int pthread\_equal(pthread\_t pt1, pthread\_t pt2)

Compare thread IDs.

[pthread\_cond\_init](pthread_8h.md#a319a61cdb25d069c9d4504e8225fd0c3)

int pthread\_cond\_init(pthread\_cond\_t \*cv, const pthread\_condattr\_t \*att)

POSIX threading compatibility API.

[pthread\_setcancelstate](pthread_8h.md#a37075410fbbaad7ee93c95375fc86e0e)

int pthread\_setcancelstate(int state, int \*oldstate)

[pthread\_attr\_getdetachstate](pthread_8h.md#a391c34da42e68ddd24f5ee0c070d5c4f)

int pthread\_attr\_getdetachstate(const pthread\_attr\_t \*attr, int \*detachstate)

[pthread\_setconcurrency](pthread_8h.md#a46064892e8c4622e0a3ebe22d9792b92)

int pthread\_setconcurrency(int new\_level)

[pthread\_attr\_destroy](pthread_8h.md#a4bcdbf47c17c7dcc51e9f05f5cb56d81)

int pthread\_attr\_destroy(pthread\_attr\_t \*attr)

[pthread\_self](pthread_8h.md#a4c4f5f3b4f8f45d9d897847d53b11aaa)

pthread\_t pthread\_self(void)

Obtain ID of the calling thread.

[pthread\_attr\_setguardsize](pthread_8h.md#a532b31c11a9d87663053c5342400758c)

int pthread\_attr\_setguardsize(pthread\_attr\_t \*attr, size\_t guardsize)

[pthread\_barrierattr\_getpshared](pthread_8h.md#a54e367403c0524680115b780ccfbc586)

int pthread\_barrierattr\_getpshared(const pthread\_barrierattr\_t \*ZRESTRICT attr, int \*ZRESTRICT pshared)

POSIX threading compatibility API.

[pthread\_rwlock\_wrlock](pthread_8h.md#a5ddd4cc028257f9baa9e23c2337abe3b)

int pthread\_rwlock\_wrlock(pthread\_rwlock\_t \*rwlock)

[pthread\_barrierattr\_destroy](pthread_8h.md#a5e27d4773f3d0552e36f2ff3b922a988)

int pthread\_barrierattr\_destroy(pthread\_barrierattr\_t \*b)

POSIX threading compatibility API.

[pthread\_mutexattr\_init](pthread_8h.md#a5eb25214d1409ff80e25559875a6b009)

static int pthread\_mutexattr\_init(pthread\_mutexattr\_t \*m)

POSIX threading compatibility API.

**Definition** pthread.h:256

[pthread\_cond\_wait](pthread_8h.md#a61a1bf88d32de361e82ef4ea99b47322)

int pthread\_cond\_wait(pthread\_cond\_t \*cv, pthread\_mutex\_t \*mut)

POSIX threading compatibility API.

[pthread\_mutexattr\_destroy](pthread_8h.md#a6422431160421ef5e69da9e98fd19580)

static int pthread\_mutexattr\_destroy(pthread\_mutexattr\_t \*m)

POSIX threading compatibility API.

**Definition** pthread.h:270

[pthread\_cancel](pthread_8h.md#a66a8f4bac5afe05538794218ff7c85ea)

int pthread\_cancel(pthread\_t pthread)

[pthread\_join](pthread_8h.md#a6e4d503c2b358be5c98330f9006b3417)

int pthread\_join(pthread\_t thread, void \*\*status)

[pthread\_condattr\_getclock](pthread_8h.md#a77376b018eec6db2986939b847915a3c)

int pthread\_condattr\_getclock(const pthread\_condattr\_t \*ZRESTRICT att, clockid\_t \*ZRESTRICT clock\_id)

POSIX threading comatibility API.

[pthread\_rwlockattr\_init](pthread_8h.md#a78db2cd33976f604cf85662fffa28307)

static int pthread\_rwlockattr\_init(pthread\_rwlockattr\_t \*attr)

initialize the read-write lock attributes object.

**Definition** pthread.h:408

[pthread\_mutex\_init](pthread_8h.md#a7948bc0ea8a33439aece34d0fb3daf8b)

int pthread\_mutex\_init(pthread\_mutex\_t \*m, const pthread\_mutexattr\_t \*att)

POSIX threading compatibility API.

[pthread\_rwlock\_destroy](pthread_8h.md#a79839f0f4f4a768bf6d218faf377c209)

int pthread\_rwlock\_destroy(pthread\_rwlock\_t \*rwlock)

[pthread\_attr\_setschedpolicy](pthread_8h.md#a79b4c9e71486a87ef3014f1c660b33eb)

int pthread\_attr\_setschedpolicy(pthread\_attr\_t \*attr, int policy)

[pthread\_detach](pthread_8h.md#a7c275c509c26566b6dd95a2de1668a2f)

int pthread\_detach(pthread\_t thread)

[pthread\_rwlock\_unlock](pthread_8h.md#a7d3b987d99117fc10c4ef97230011983)

int pthread\_rwlock\_unlock(pthread\_rwlock\_t \*rwlock)

[pthread\_mutexattr\_gettype](pthread_8h.md#a7f064a4db96a009a5a9a7c7e5cc03599)

int pthread\_mutexattr\_gettype(const pthread\_mutexattr\_t \*attr, int \*type)

POSIX threading compatibility API.

[pthread\_atfork](pthread_8h.md#a80008474c3d68e9880da960a53d2f430)

int pthread\_atfork(void(\*prepare)(void), void(\*parent)(void), void(\*child)(void))

[pthread\_attr\_setstacksize](pthread_8h.md#a812a9a455ae2ef2bb0dca4fff201a281)

int pthread\_attr\_setstacksize(pthread\_attr\_t \*attr, size\_t stacksize)

[pthread\_mutexattr\_settype](pthread_8h.md#a8387c80e660e9426f801ac0217ecfae5)

int pthread\_mutexattr\_settype(pthread\_mutexattr\_t \*attr, int type)

POSIX threading compatibility API.

[pthread\_cond\_destroy](pthread_8h.md#a8d44e4eae235f675bbab1b9163a3bc1d)

int pthread\_cond\_destroy(pthread\_cond\_t \*cv)

POSIX threading compatibility API.

[pthread\_getname\_np](pthread_8h.md#a8d55a60492c979991dc1a361b5453813)

int pthread\_getname\_np(pthread\_t thread, char \*name, size\_t len)

Get name of POSIX thread and store in name buffer that is of size len.

[pthread\_cond\_broadcast](pthread_8h.md#a91ff7fff67462ce9216d299c89683119)

int pthread\_cond\_broadcast(pthread\_cond\_t \*cv)

POSIX threading compatibility API.

[pthread\_attr\_setstack](pthread_8h.md#a94ede89b99a3a4fa17e516d30aaf3409)

int pthread\_attr\_setstack(pthread\_attr\_t \*attr, void \*stackaddr, size\_t stacksize)

[pthread\_setname\_np](pthread_8h.md#aa21465e084e7185bfbb94bb50d60cd08)

int pthread\_setname\_np(pthread\_t thread, const char \*name)

Set name of POSIX thread.

[pthread\_barrierattr\_setpshared](pthread_8h.md#aa9c3c335f5bcf702fe85a1c12dcdc70e)

int pthread\_barrierattr\_setpshared(pthread\_barrierattr\_t \*attr, int pshared)

POSIX threading compatibility API.

[pthread\_setcanceltype](pthread_8h.md#aab579bcfcf0662a0c1e35fd82162e61d)

int pthread\_setcanceltype(int type, int \*oldtype)

[pthread\_rwlock\_tryrdlock](pthread_8h.md#aae52fb1d3e6d03b18fa5731d0b49d197)

int pthread\_rwlock\_tryrdlock(pthread\_rwlock\_t \*rwlock)

[pthread\_barrier\_destroy](pthread_8h.md#ab05ae13769e61dea9c53ca7894743c8f)

int pthread\_barrier\_destroy(pthread\_barrier\_t \*b)

POSIX threading compatibility API.

[pthread\_exit](pthread_8h.md#ab9a027122b38833e8c2e1c0e733da3e6)

FUNC\_NORETURN void pthread\_exit(void \*retval)

[pthread\_mutex\_timedlock](pthread_8h.md#abbec44a62531009629601fbb34f1027c)

int pthread\_mutex\_timedlock(pthread\_mutex\_t \*m, const struct timespec \*abstime)

POSIX threading compatibility API.

[pthread\_attr\_getschedparam](pthread_8h.md#abcd67baa86ff65d7ce65985d8b50d579)

int pthread\_attr\_getschedparam(const pthread\_attr\_t \*attr, struct sched\_param \*schedparam)

[pthread\_attr\_getguardsize](pthread_8h.md#abee3ae43d1f00b597111f6f82b0416a1)

int pthread\_attr\_getguardsize(const pthread\_attr\_t \*ZRESTRICT attr, size\_t \*ZRESTRICT guardsize)

[pthread\_condattr\_setclock](pthread_8h.md#ac0b4f6d49deeab0ddb269a23ee303156)

int pthread\_condattr\_setclock(pthread\_condattr\_t \*att, clockid\_t clock\_id)

POSIX threading compatibility API.

[pthread\_rwlockattr\_destroy](pthread_8h.md#ac4d2dcfe790eee1dbd83a1db7fdce3dc)

static int pthread\_rwlockattr\_destroy(pthread\_rwlockattr\_t \*attr)

Destroy the read-write lock attributes object.

**Definition** pthread.h:397

[pthread\_getschedparam](pthread_8h.md#ac60393667965dbd06670d3d280b65757)

int pthread\_getschedparam(pthread\_t pthread, int \*policy, struct sched\_param \*param)

[pthread\_create](pthread_8h.md#acb010e074930d81533ed20d319ca80b1)

int pthread\_create(pthread\_t \*newthread, const pthread\_attr\_t \*attr, void \*(\*threadroutine)(void \*), void \*arg)

[pthread\_rwlock\_rdlock](pthread_8h.md#acc16fb32464b480d31bc69cce4e206c9)

int pthread\_rwlock\_rdlock(pthread\_rwlock\_t \*rwlock)

[pthread\_mutex\_trylock](pthread_8h.md#acc1ccbaf3d76572da85a8030bba1ede4)

int pthread\_mutex\_trylock(pthread\_mutex\_t \*m)

POSIX threading compatibility API.

[pthread\_getspecific](pthread_8h.md#acdf9f73a16ea40eba1bc174d38e76ca5)

void \* pthread\_getspecific(pthread\_key\_t key)

[pthread\_barrierattr\_init](pthread_8h.md#ad540451ab679ace869b51c7cbb7b8486)

int pthread\_barrierattr\_init(pthread\_barrierattr\_t \*b)

POSIX threading compatibility API.

[pthread\_rwlock\_timedrdlock](pthread_8h.md#ad791558625e69852e4a435b7c1580468)

int pthread\_rwlock\_timedrdlock(pthread\_rwlock\_t \*rwlock, const struct timespec \*abstime)

[pthread\_setschedparam](pthread_8h.md#ad8e89d31b56c88d632ba9aeb956fa043)

int pthread\_setschedparam(pthread\_t pthread, int policy, const struct sched\_param \*param)

[pthread\_cond\_signal](pthread_8h.md#add1fea97e50755b5dbf4bd9a83b710dd)

int pthread\_cond\_signal(pthread\_cond\_t \*cv)

POSIX threading compatibility API.

[pthread\_attr\_getstacksize](pthread_8h.md#ae23600d4670359ab12bfba20db2c9a37)

int pthread\_attr\_getstacksize(const pthread\_attr\_t \*attr, size\_t \*stacksize)

[pthread\_attr\_setdetachstate](pthread_8h.md#ae6ee78c307d8467b34a9b0c330993a54)

int pthread\_attr\_setdetachstate(pthread\_attr\_t \*attr, int detachstate)

[pthread\_mutexattr\_setprotocol](pthread_8h.md#ae7e6584c2b2cf9b9ff061115d2342bb5)

int pthread\_mutexattr\_setprotocol(pthread\_mutexattr\_t \*attr, int protocol)

POSIX threading compatibility API.

[pthread\_attr\_getstack](pthread_8h.md#aec19ad460995a9fe8aeb4eaf2bb1ed1d)

int pthread\_attr\_getstack(const pthread\_attr\_t \*attr, void \*\*stackaddr, size\_t \*stacksize)

[pthread\_barrier\_init](pthread_8h.md#aecc6c99901aac517072970e153863296)

int pthread\_barrier\_init(pthread\_barrier\_t \*b, const pthread\_barrierattr\_t \*attr, unsigned int count)

POSIX threading compatibility API.

[pthread\_cond\_timedwait](pthread_8h.md#aecea498fbd2df02942790e5ccd7d78b2)

int pthread\_cond\_timedwait(pthread\_cond\_t \*cv, pthread\_mutex\_t \*mut, const struct timespec \*abstime)

POSIX threading compatibility API.

[pthread\_key\_delete](pthread_8h.md#aee96306dc79294927ee840bb4de2244b)

int pthread\_key\_delete(pthread\_key\_t key)

[pthread\_attr\_getschedpolicy](pthread_8h.md#af032906f326f3c209c7eed6bb248ebee)

int pthread\_attr\_getschedpolicy(const pthread\_attr\_t \*attr, int \*policy)

[pthread\_testcancel](pthread_8h.md#af1c95282ab2bea25f0888a19652cd41f)

void pthread\_testcancel(void)

[pthread\_condattr\_destroy](pthread_8h.md#af37eaf73f0d83989d8efc06e676909f1)

int pthread\_condattr\_destroy(pthread\_condattr\_t \*att)

POSIX threading compatibility API.

[pthread\_key\_create](pthread_8h.md#af4b7ced8ecff505380fe8216244a3764)

int pthread\_key\_create(pthread\_key\_t \*key, void(\*destructor)(void \*))

[pthread\_barrier\_wait](pthread_8h.md#af786372165ba080986ae4143928c5436)

int pthread\_barrier\_wait(pthread\_barrier\_t \*b)

POSIX threading compatibility API.

[pthread\_mutex\_destroy](pthread_8h.md#af89d9cfa300f33b46720a96eac83d175)

int pthread\_mutex\_destroy(pthread\_mutex\_t \*m)

POSIX threading compatibility API.

[pthread\_getconcurrency](pthread_8h.md#afb4344ea91774ba279ea5df3cb656ebc)

int pthread\_getconcurrency(void)

[pthread\_mutex\_lock](pthread_8h.md#afd70d6f2c50e22b996c926fb9d6ad291)

int pthread\_mutex\_lock(pthread\_mutex\_t \*m)

POSIX threading compatibility API.

[stdlib.h](stdlib_8h.md)

[string.h](string_8h.md)

[pthread\_once](structpthread__once.md)

**Definition** posix\_types.h:95

[timespec](structtimespec.md)

**Definition** \_timespec.h:22

[unistd.h](unistd_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [posix](dir_cc2c191bc57cea4eaf0dbdf53c4fb6c6.md)
- [pthread.h](pthread_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
