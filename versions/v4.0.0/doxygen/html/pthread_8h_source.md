---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/pthread_8h_source.html
original_path: doxygen/html/pthread_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
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

13#include <[zephyr/kernel.h](kernel_8h.md)>

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

42/\* Pthread scope \*/

43#undef PTHREAD\_SCOPE\_PROCESS

[ 44](pthread_8h.md#aeab18be4f4ee13db4b0b65c6768fb539)#define PTHREAD\_SCOPE\_PROCESS 1

45#undef PTHREAD\_SCOPE\_SYSTEM

[ 46](pthread_8h.md#ab754f4339f76c46b8f57413c03e8ec65)#define PTHREAD\_SCOPE\_SYSTEM 0

47

48/\* Pthread inherit scheduler \*/

49#undef PTHREAD\_INHERIT\_SCHED

[ 50](pthread_8h.md#a470fccc57c4d7c3846e446a17cd23573)#define PTHREAD\_INHERIT\_SCHED 0

51#undef PTHREAD\_EXPLICIT\_SCHED

[ 52](pthread_8h.md#ad45abe03c8232518b6995e73172fe053)#define PTHREAD\_EXPLICIT\_SCHED 1

53

54/\* Passed to pthread\_once \*/

[ 55](pthread_8h.md#a59e22497b65fc305ddb5cea8b4990b51)#define PTHREAD\_ONCE\_INIT {0}

56

57/\* The minimum allowable stack size \*/

[ 58](pthread_8h.md#a8b3dc1c5c1a165d6143b1dce950e8266)#define PTHREAD\_STACK\_MIN K\_KERNEL\_STACK\_LEN(0)

59

[ 65](pthread_8h.md#aa7b867fe46f3660283fcb356c4fcbbf0)#define PTHREAD\_COND\_INITIALIZER (-1)

66

[ 72](pthread_8h.md#a319a61cdb25d069c9d4504e8225fd0c3)int [pthread\_cond\_init](pthread_8h.md#a319a61cdb25d069c9d4504e8225fd0c3)([pthread\_cond\_t](posix__types_8h.md#a1b893f49dfdf497be09c04a0e40f425e) \*cv, const [pthread\_condattr\_t](posix__types_8h.md#a9f62774a7a4e1634e60fb611765251f1) \*att);

73

[ 79](pthread_8h.md#a8d44e4eae235f675bbab1b9163a3bc1d)int [pthread\_cond\_destroy](pthread_8h.md#a8d44e4eae235f675bbab1b9163a3bc1d)([pthread\_cond\_t](posix__types_8h.md#a1b893f49dfdf497be09c04a0e40f425e) \*cv);

80

[ 86](pthread_8h.md#add1fea97e50755b5dbf4bd9a83b710dd)int [pthread\_cond\_signal](pthread_8h.md#add1fea97e50755b5dbf4bd9a83b710dd)([pthread\_cond\_t](posix__types_8h.md#a1b893f49dfdf497be09c04a0e40f425e) \*cv);

87

[ 93](pthread_8h.md#a91ff7fff67462ce9216d299c89683119)int [pthread\_cond\_broadcast](pthread_8h.md#a91ff7fff67462ce9216d299c89683119)([pthread\_cond\_t](posix__types_8h.md#a1b893f49dfdf497be09c04a0e40f425e) \*cv);

94

[ 100](pthread_8h.md#a61a1bf88d32de361e82ef4ea99b47322)int [pthread\_cond\_wait](pthread_8h.md#a61a1bf88d32de361e82ef4ea99b47322)([pthread\_cond\_t](posix__types_8h.md#a1b893f49dfdf497be09c04a0e40f425e) \*cv, [pthread\_mutex\_t](posix__types_8h.md#a465eb2b962de164efdc8ce957025de7e) \*mut);

101

[ 107](pthread_8h.md#aecea498fbd2df02942790e5ccd7d78b2)int [pthread\_cond\_timedwait](pthread_8h.md#aecea498fbd2df02942790e5ccd7d78b2)([pthread\_cond\_t](posix__types_8h.md#a1b893f49dfdf497be09c04a0e40f425e) \*cv, [pthread\_mutex\_t](posix__types_8h.md#a465eb2b962de164efdc8ce957025de7e) \*mut,

108 const struct [timespec](structtimespec.md) \*abstime);

109

[ 116](pthread_8h.md#a01159da320b2317ee286a7e92d713f16)int [pthread\_condattr\_init](pthread_8h.md#a01159da320b2317ee286a7e92d713f16)([pthread\_condattr\_t](posix__types_8h.md#a9f62774a7a4e1634e60fb611765251f1) \*att);

117

[ 124](pthread_8h.md#af37eaf73f0d83989d8efc06e676909f1)int [pthread\_condattr\_destroy](pthread_8h.md#af37eaf73f0d83989d8efc06e676909f1)([pthread\_condattr\_t](posix__types_8h.md#a9f62774a7a4e1634e60fb611765251f1) \*att);

125

[ 132](pthread_8h.md#a77376b018eec6db2986939b847915a3c)int [pthread\_condattr\_getclock](pthread_8h.md#a77376b018eec6db2986939b847915a3c)(const [pthread\_condattr\_t](posix__types_8h.md#a9f62774a7a4e1634e60fb611765251f1) \*[ZRESTRICT](include_2zephyr_2toolchain_2common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) att,

133 [clockid\_t](posix__types_8h.md#a6bb3206700910111f26e946bfbf0f2af) \*[ZRESTRICT](include_2zephyr_2toolchain_2common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) clock\_id);

134

141

[ 142](pthread_8h.md#ac0b4f6d49deeab0ddb269a23ee303156)int [pthread\_condattr\_setclock](pthread_8h.md#ac0b4f6d49deeab0ddb269a23ee303156)([pthread\_condattr\_t](posix__types_8h.md#a9f62774a7a4e1634e60fb611765251f1) \*att, [clockid\_t](posix__types_8h.md#a6bb3206700910111f26e946bfbf0f2af) clock\_id);

143

[ 149](pthread_8h.md#a84e55100366a6a8338a2af3b3f279686)#define PTHREAD\_MUTEX\_INITIALIZER (-1)

150

[ 156](pthread_8h.md#aa92fd7b492a8a5b31b2f8b3b6039c622)#define PTHREAD\_RWLOCK\_INITIALIZER (-1)

157

158/\*

159 \* Mutex attributes - type

160 \*

161 \* PTHREAD\_MUTEX\_NORMAL: Owner of mutex cannot relock it. Attempting

162 \* to relock will cause deadlock.

163 \* PTHREAD\_MUTEX\_RECURSIVE: Owner can relock the mutex.

164 \* PTHREAD\_MUTEX\_ERRORCHECK: If owner attempts to relock the mutex, an

165 \* error is returned.

166 \*

167 \*/

[ 168](pthread_8h.md#aae4b650085c2599674938f503d6253cf)#define PTHREAD\_MUTEX\_NORMAL 0

[ 169](pthread_8h.md#a715e9644a7183d98cb2c9dd41cb89645)#define PTHREAD\_MUTEX\_RECURSIVE 1

[ 170](pthread_8h.md#aaf502496651f95b06be861af7902cb23)#define PTHREAD\_MUTEX\_ERRORCHECK 2

[ 171](pthread_8h.md#a2a9b96c0491ae490c17d0b400bc427b0)#define PTHREAD\_MUTEX\_DEFAULT PTHREAD\_MUTEX\_NORMAL

172

173/\*

174 \* Mutex attributes - protocol

175 \*

176 \* PTHREAD\_PRIO\_NONE: Ownership of mutex does not affect priority.

177 \* PTHREAD\_PRIO\_INHERIT: Owner's priority is boosted to the priority of

178 \* highest priority thread blocked on the mutex.

179 \* PTHREAD\_PRIO\_PROTECT: Mutex has a priority ceiling. The owner's

180 \* priority is boosted to the highest priority ceiling of all mutexes

181 \* owned (regardless of whether or not other threads are blocked on

182 \* any of these mutexes).

183 \* FIXME: Only PRIO\_NONE is supported. Implement other protocols.

184 \*/

[ 185](pthread_8h.md#a8c1426a72025b27d9726580ac0e8404f)#define PTHREAD\_PRIO\_NONE 0

[ 186](pthread_8h.md#a0087e0ca82fd36e6c15f4c8ad443dbfc)#define PTHREAD\_PRIO\_INHERIT 1

[ 187](pthread_8h.md#a65da4c842cd4287f43d2f69ad5a5470b)#define PTHREAD\_PRIO\_PROTECT 2

188

[ 194](pthread_8h.md#af89d9cfa300f33b46720a96eac83d175)int [pthread\_mutex\_destroy](pthread_8h.md#af89d9cfa300f33b46720a96eac83d175)([pthread\_mutex\_t](posix__types_8h.md#a465eb2b962de164efdc8ce957025de7e) \*m);

195

[ 201](pthread_8h.md#afd70d6f2c50e22b996c926fb9d6ad291)int [pthread\_mutex\_lock](pthread_8h.md#afd70d6f2c50e22b996c926fb9d6ad291)([pthread\_mutex\_t](posix__types_8h.md#a465eb2b962de164efdc8ce957025de7e) \*m);

202

[ 208](pthread_8h.md#a02a3c64dac70730e226c31c0e7dbb45c)int [pthread\_mutex\_unlock](pthread_8h.md#a02a3c64dac70730e226c31c0e7dbb45c)([pthread\_mutex\_t](posix__types_8h.md#a465eb2b962de164efdc8ce957025de7e) \*m);

209

215

[ 216](pthread_8h.md#abbec44a62531009629601fbb34f1027c)int [pthread\_mutex\_timedlock](pthread_8h.md#abbec44a62531009629601fbb34f1027c)([pthread\_mutex\_t](posix__types_8h.md#a465eb2b962de164efdc8ce957025de7e) \*m,

217 const struct [timespec](structtimespec.md) \*abstime);

218

[ 224](pthread_8h.md#acc1ccbaf3d76572da85a8030bba1ede4)int [pthread\_mutex\_trylock](pthread_8h.md#acc1ccbaf3d76572da85a8030bba1ede4)([pthread\_mutex\_t](posix__types_8h.md#a465eb2b962de164efdc8ce957025de7e) \*m);

225

[ 231](pthread_8h.md#a7948bc0ea8a33439aece34d0fb3daf8b)int [pthread\_mutex\_init](pthread_8h.md#a7948bc0ea8a33439aece34d0fb3daf8b)([pthread\_mutex\_t](posix__types_8h.md#a465eb2b962de164efdc8ce957025de7e) \*m,

232 const [pthread\_mutexattr\_t](posix__types_8h.md#a2489174ff5737a33443b0959f4278765) \*att);

233

[ 239](pthread_8h.md#ae7e6584c2b2cf9b9ff061115d2342bb5)int [pthread\_mutexattr\_setprotocol](pthread_8h.md#ae7e6584c2b2cf9b9ff061115d2342bb5)([pthread\_mutexattr\_t](posix__types_8h.md#a2489174ff5737a33443b0959f4278765) \*attr, int protocol);

240

[ 246](pthread_8h.md#a8387c80e660e9426f801ac0217ecfae5)int [pthread\_mutexattr\_settype](pthread_8h.md#a8387c80e660e9426f801ac0217ecfae5)([pthread\_mutexattr\_t](posix__types_8h.md#a2489174ff5737a33443b0959f4278765) \*attr, int type);

247

[ 253](pthread_8h.md#a200fcbc9157e6183376f83bc0e5937dd)int [pthread\_mutexattr\_getprotocol](pthread_8h.md#a200fcbc9157e6183376f83bc0e5937dd)(const [pthread\_mutexattr\_t](posix__types_8h.md#a2489174ff5737a33443b0959f4278765) \*attr,

254 int \*protocol);

255

[ 261](pthread_8h.md#a7f064a4db96a009a5a9a7c7e5cc03599)int [pthread\_mutexattr\_gettype](pthread_8h.md#a7f064a4db96a009a5a9a7c7e5cc03599)(const [pthread\_mutexattr\_t](posix__types_8h.md#a2489174ff5737a33443b0959f4278765) \*attr, int \*type);

262

[ 270](pthread_8h.md#af98f6b6c483077a39d1400b1de1577b8)int [pthread\_mutexattr\_init](pthread_8h.md#af98f6b6c483077a39d1400b1de1577b8)([pthread\_mutexattr\_t](posix__types_8h.md#a2489174ff5737a33443b0959f4278765) \*attr);

271

[ 279](pthread_8h.md#a2321aabf58224b06021185708d0f9658)int [pthread\_mutexattr\_destroy](pthread_8h.md#a2321aabf58224b06021185708d0f9658)([pthread\_mutexattr\_t](posix__types_8h.md#a2489174ff5737a33443b0959f4278765) \*attr);

280

[ 281](pthread_8h.md#a822c63bc662ad86cfb2dcec50edbb42b)#define PTHREAD\_BARRIER\_SERIAL\_THREAD 1

282

283/\*

284 \* Barrier attributes - type

285 \*/

286#define PTHREAD\_PROCESS\_PRIVATE 0

[ 287](pthread_8h.md#afff2f9c2b019a07298f341cf70ee829d)#define PTHREAD\_PROCESS\_PUBLIC 1

288

[ 294](pthread_8h.md#af786372165ba080986ae4143928c5436)int [pthread\_barrier\_wait](pthread_8h.md#af786372165ba080986ae4143928c5436)([pthread\_barrier\_t](posix__types_8h.md#aeb637552f63e4c249e7aaeb2905f3db2) \*b);

295

[ 301](pthread_8h.md#aecc6c99901aac517072970e153863296)int [pthread\_barrier\_init](pthread_8h.md#aecc6c99901aac517072970e153863296)([pthread\_barrier\_t](posix__types_8h.md#aeb637552f63e4c249e7aaeb2905f3db2) \*b, const [pthread\_barrierattr\_t](posix__types_8h.md#a24d58850626c8022bf4bbd5d2628615b) \*attr,

302 unsigned int count);

303

[ 309](pthread_8h.md#ab05ae13769e61dea9c53ca7894743c8f)int [pthread\_barrier\_destroy](pthread_8h.md#ab05ae13769e61dea9c53ca7894743c8f)([pthread\_barrier\_t](posix__types_8h.md#aeb637552f63e4c249e7aaeb2905f3db2) \*b);

310

[ 316](pthread_8h.md#ad540451ab679ace869b51c7cbb7b8486)int [pthread\_barrierattr\_init](pthread_8h.md#ad540451ab679ace869b51c7cbb7b8486)([pthread\_barrierattr\_t](posix__types_8h.md#a24d58850626c8022bf4bbd5d2628615b) \*b);

317

[ 323](pthread_8h.md#a5e27d4773f3d0552e36f2ff3b922a988)int [pthread\_barrierattr\_destroy](pthread_8h.md#a5e27d4773f3d0552e36f2ff3b922a988)([pthread\_barrierattr\_t](posix__types_8h.md#a24d58850626c8022bf4bbd5d2628615b) \*b);

324

[ 330](pthread_8h.md#aa9c3c335f5bcf702fe85a1c12dcdc70e)int [pthread\_barrierattr\_setpshared](pthread_8h.md#aa9c3c335f5bcf702fe85a1c12dcdc70e)([pthread\_barrierattr\_t](posix__types_8h.md#a24d58850626c8022bf4bbd5d2628615b) \*attr, int pshared);

331

[ 337](pthread_8h.md#a54e367403c0524680115b780ccfbc586)int [pthread\_barrierattr\_getpshared](pthread_8h.md#a54e367403c0524680115b780ccfbc586)(const [pthread\_barrierattr\_t](posix__types_8h.md#a24d58850626c8022bf4bbd5d2628615b) \*[ZRESTRICT](include_2zephyr_2toolchain_2common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) attr,

338 int \*[ZRESTRICT](include_2zephyr_2toolchain_2common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) pshared);

339

340/\* Predicates and setters for various pthread attribute values that we

341 \* don't support (or always support: the "process shared" attribute

342 \* can only be true given the way Zephyr implements these

343 \* objects). Leave these undefined for simplicity instead of defining

344 \* stubs to return an error that would have to be logged and

345 \* interpreted just to figure out that we didn't support it in the

346 \* first place. These APIs are very rarely used even in production

347 \* Unix code. Leave the declarations here so they can be easily

348 \* uncommented and implemented as needed.

349

350int pthread\_condattr\_getpshared(const pthread\_condattr\_t \* int \*);

351int pthread\_condattr\_setpshared(pthread\_condattr\_t \*, int);

352int pthread\_mutex\_consistent(pthread\_mutex\_t \*);

353int pthread\_mutexattr\_getpshared(const pthread\_mutexattr\_t \* int \*);

354int pthread\_mutexattr\_getrobust(const pthread\_mutexattr\_t \* int \*);

355int pthread\_mutexattr\_setpshared(pthread\_mutexattr\_t \*, int);

356int pthread\_mutexattr\_setrobust(pthread\_mutexattr\_t \*, int);

357\*/

358

359#ifdef CONFIG\_POSIX\_THREAD\_PRIO\_PROTECT

360int pthread\_mutex\_getprioceiling(const [pthread\_mutex\_t](posix__types_8h.md#a465eb2b962de164efdc8ce957025de7e) \*[ZRESTRICT](include_2zephyr_2toolchain_2common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) mutex,

361 int \*[ZRESTRICT](include_2zephyr_2toolchain_2common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) prioceiling);

362int pthread\_mutex\_setprioceiling([pthread\_mutex\_t](posix__types_8h.md#a465eb2b962de164efdc8ce957025de7e) \*[ZRESTRICT](include_2zephyr_2toolchain_2common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) mutex, int prioceiling,

363 int \*[ZRESTRICT](include_2zephyr_2toolchain_2common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) old\_ceiling);

364int pthread\_mutexattr\_getprioceiling(const [pthread\_mutexattr\_t](posix__types_8h.md#a2489174ff5737a33443b0959f4278765) \*[ZRESTRICT](include_2zephyr_2toolchain_2common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) attr,

365 int \*[ZRESTRICT](include_2zephyr_2toolchain_2common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) prioceiling);

366int pthread\_mutexattr\_setprioceiling([pthread\_mutexattr\_t](posix__types_8h.md#a2489174ff5737a33443b0959f4278765) \*attr, int prioceiling);

367#endif /\* CONFIG\_POSIX\_THREAD\_PRIO\_PROTECT \*/

368

369/\* Base Pthread related APIs \*/

370

[ 379](pthread_8h.md#a4c4f5f3b4f8f45d9d897847d53b11aaa)[pthread\_t](posix__types_8h.md#a405938c67e9c568fde9993c7e14d58ec) [pthread\_self](pthread_8h.md#a4c4f5f3b4f8f45d9d897847d53b11aaa)(void);

380

[ 386](pthread_8h.md#a2a460fe3d4e4518057366f6ead455f4a)int [pthread\_equal](pthread_8h.md#a2a460fe3d4e4518057366f6ead455f4a)([pthread\_t](posix__types_8h.md#a405938c67e9c568fde9993c7e14d58ec) pt1, [pthread\_t](posix__types_8h.md#a405938c67e9c568fde9993c7e14d58ec) pt2);

387

[ 393](pthread_8h.md#a78a54e67f0afe2601dbda0a904fa0bdf)int [pthread\_rwlockattr\_destroy](pthread_8h.md#a78a54e67f0afe2601dbda0a904fa0bdf)([pthread\_rwlockattr\_t](posix__types_8h.md#a4e92e3fbb4be682babbb6796af90b50f) \*attr);

394

[ 400](pthread_8h.md#a9d831af0179ed16d1b6cbeba0304810b)int [pthread\_rwlockattr\_init](pthread_8h.md#a9d831af0179ed16d1b6cbeba0304810b)([pthread\_rwlockattr\_t](posix__types_8h.md#a4e92e3fbb4be682babbb6796af90b50f) \*attr);

401

[ 402](pthread_8h.md#a5ca1dea9ea7d3cfb34a9c8561e47cf02)int [pthread\_rwlockattr\_getpshared](pthread_8h.md#a5ca1dea9ea7d3cfb34a9c8561e47cf02)(const [pthread\_rwlockattr\_t](posix__types_8h.md#a4e92e3fbb4be682babbb6796af90b50f) \*[ZRESTRICT](include_2zephyr_2toolchain_2common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) attr,

403 int \*[ZRESTRICT](include_2zephyr_2toolchain_2common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) pshared);

[ 404](pthread_8h.md#ae6550aa6aede71f618bb7457f3e50524)int [pthread\_rwlockattr\_setpshared](pthread_8h.md#ae6550aa6aede71f618bb7457f3e50524)([pthread\_rwlockattr\_t](posix__types_8h.md#a4e92e3fbb4be682babbb6796af90b50f) \*attr, int pshared);

405

[ 406](pthread_8h.md#abee3ae43d1f00b597111f6f82b0416a1)int [pthread\_attr\_getguardsize](pthread_8h.md#abee3ae43d1f00b597111f6f82b0416a1)(const [pthread\_attr\_t](posix__types_8h.md#a1d96fa5809832849f591deef6cc7af7a) \*[ZRESTRICT](include_2zephyr_2toolchain_2common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) attr, size\_t \*[ZRESTRICT](include_2zephyr_2toolchain_2common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) guardsize);

[ 407](pthread_8h.md#ae23600d4670359ab12bfba20db2c9a37)int [pthread\_attr\_getstacksize](pthread_8h.md#ae23600d4670359ab12bfba20db2c9a37)(const [pthread\_attr\_t](posix__types_8h.md#a1d96fa5809832849f591deef6cc7af7a) \*attr, size\_t \*stacksize);

[ 408](pthread_8h.md#a532b31c11a9d87663053c5342400758c)int [pthread\_attr\_setguardsize](pthread_8h.md#a532b31c11a9d87663053c5342400758c)([pthread\_attr\_t](posix__types_8h.md#a1d96fa5809832849f591deef6cc7af7a) \*attr, size\_t guardsize);

[ 409](pthread_8h.md#a812a9a455ae2ef2bb0dca4fff201a281)int [pthread\_attr\_setstacksize](pthread_8h.md#a812a9a455ae2ef2bb0dca4fff201a281)([pthread\_attr\_t](posix__types_8h.md#a1d96fa5809832849f591deef6cc7af7a) \*attr, size\_t stacksize);

[ 410](pthread_8h.md#a79b4c9e71486a87ef3014f1c660b33eb)int [pthread\_attr\_setschedpolicy](pthread_8h.md#a79b4c9e71486a87ef3014f1c660b33eb)([pthread\_attr\_t](posix__types_8h.md#a1d96fa5809832849f591deef6cc7af7a) \*attr, int policy);

[ 411](pthread_8h.md#af032906f326f3c209c7eed6bb248ebee)int [pthread\_attr\_getschedpolicy](pthread_8h.md#af032906f326f3c209c7eed6bb248ebee)(const [pthread\_attr\_t](posix__types_8h.md#a1d96fa5809832849f591deef6cc7af7a) \*attr, int \*policy);

[ 412](pthread_8h.md#ae6ee78c307d8467b34a9b0c330993a54)int [pthread\_attr\_setdetachstate](pthread_8h.md#ae6ee78c307d8467b34a9b0c330993a54)([pthread\_attr\_t](posix__types_8h.md#a1d96fa5809832849f591deef6cc7af7a) \*attr, int detachstate);

[ 413](pthread_8h.md#a391c34da42e68ddd24f5ee0c070d5c4f)int [pthread\_attr\_getdetachstate](pthread_8h.md#a391c34da42e68ddd24f5ee0c070d5c4f)(const [pthread\_attr\_t](posix__types_8h.md#a1d96fa5809832849f591deef6cc7af7a) \*attr, int \*detachstate);

[ 414](pthread_8h.md#a0b85ebb1e3aac081a4c0a5e85ae3cbe9)int [pthread\_attr\_init](pthread_8h.md#a0b85ebb1e3aac081a4c0a5e85ae3cbe9)([pthread\_attr\_t](posix__types_8h.md#a1d96fa5809832849f591deef6cc7af7a) \*attr);

[ 415](pthread_8h.md#a4bcdbf47c17c7dcc51e9f05f5cb56d81)int [pthread\_attr\_destroy](pthread_8h.md#a4bcdbf47c17c7dcc51e9f05f5cb56d81)([pthread\_attr\_t](posix__types_8h.md#a1d96fa5809832849f591deef6cc7af7a) \*attr);

[ 416](pthread_8h.md#abcd67baa86ff65d7ce65985d8b50d579)int [pthread\_attr\_getschedparam](pthread_8h.md#abcd67baa86ff65d7ce65985d8b50d579)(const [pthread\_attr\_t](posix__types_8h.md#a1d96fa5809832849f591deef6cc7af7a) \*attr,

417 struct sched\_param \*schedparam);

[ 418](pthread_8h.md#ac60393667965dbd06670d3d280b65757)int [pthread\_getschedparam](pthread_8h.md#ac60393667965dbd06670d3d280b65757)([pthread\_t](posix__types_8h.md#a405938c67e9c568fde9993c7e14d58ec) pthread, int \*policy,

419 struct sched\_param \*param);

[ 420](pthread_8h.md#aec19ad460995a9fe8aeb4eaf2bb1ed1d)int [pthread\_attr\_getstack](pthread_8h.md#aec19ad460995a9fe8aeb4eaf2bb1ed1d)(const [pthread\_attr\_t](posix__types_8h.md#a1d96fa5809832849f591deef6cc7af7a) \*attr,

421 void \*\*stackaddr, size\_t \*stacksize);

[ 422](pthread_8h.md#a94ede89b99a3a4fa17e516d30aaf3409)int [pthread\_attr\_setstack](pthread_8h.md#a94ede89b99a3a4fa17e516d30aaf3409)([pthread\_attr\_t](posix__types_8h.md#a1d96fa5809832849f591deef6cc7af7a) \*attr, void \*stackaddr,

423 size\_t stacksize);

[ 424](pthread_8h.md#ad3fe01698c4fad85bb5cc3f9a2e82ea3)int [pthread\_attr\_getscope](pthread_8h.md#ad3fe01698c4fad85bb5cc3f9a2e82ea3)(const [pthread\_attr\_t](posix__types_8h.md#a1d96fa5809832849f591deef6cc7af7a) \*attr, int \*contentionscope);

[ 425](pthread_8h.md#a6d8d320a882ba044a064975dddcf9ced)int [pthread\_attr\_setscope](pthread_8h.md#a6d8d320a882ba044a064975dddcf9ced)([pthread\_attr\_t](posix__types_8h.md#a1d96fa5809832849f591deef6cc7af7a) \*attr, int contentionscope);

[ 426](pthread_8h.md#a79a77b688c30213e5e52e6be178cde4e)int [pthread\_attr\_getinheritsched](pthread_8h.md#a79a77b688c30213e5e52e6be178cde4e)(const [pthread\_attr\_t](posix__types_8h.md#a1d96fa5809832849f591deef6cc7af7a) \*attr, int \*inheritsched);

[ 427](pthread_8h.md#ad437fe8caa3ef9f0cb7d69f6f6479df9)int [pthread\_attr\_setinheritsched](pthread_8h.md#ad437fe8caa3ef9f0cb7d69f6f6479df9)([pthread\_attr\_t](posix__types_8h.md#a1d96fa5809832849f591deef6cc7af7a) \*attr, int inheritsched);

428#ifdef CONFIG\_POSIX\_THREADS

429int [pthread\_once](structpthread__once.md)([pthread\_once\_t](posix__types_8h.md#a2603a6fda916554839174bc7d8849297) \*once, void (\*initFunc)(void));

430#endif

[ 431](pthread_8h.md#ab9a027122b38833e8c2e1c0e733da3e6)FUNC\_NORETURN void [pthread\_exit](pthread_8h.md#ab9a027122b38833e8c2e1c0e733da3e6)(void \*retval);

[ 432](pthread_8h.md#a6e4d503c2b358be5c98330f9006b3417)int [pthread\_join](pthread_8h.md#a6e4d503c2b358be5c98330f9006b3417)([pthread\_t](posix__types_8h.md#a405938c67e9c568fde9993c7e14d58ec) thread, void \*\*status);

[ 433](pthread_8h.md#a66a8f4bac5afe05538794218ff7c85ea)int [pthread\_cancel](pthread_8h.md#a66a8f4bac5afe05538794218ff7c85ea)([pthread\_t](posix__types_8h.md#a405938c67e9c568fde9993c7e14d58ec) pthread);

[ 434](pthread_8h.md#a7c275c509c26566b6dd95a2de1668a2f)int [pthread\_detach](pthread_8h.md#a7c275c509c26566b6dd95a2de1668a2f)([pthread\_t](posix__types_8h.md#a405938c67e9c568fde9993c7e14d58ec) thread);

[ 435](pthread_8h.md#acb010e074930d81533ed20d319ca80b1)int [pthread\_create](pthread_8h.md#acb010e074930d81533ed20d319ca80b1)([pthread\_t](posix__types_8h.md#a405938c67e9c568fde9993c7e14d58ec) \*newthread, const [pthread\_attr\_t](posix__types_8h.md#a1d96fa5809832849f591deef6cc7af7a) \*attr,

436 void \*(\*threadroutine)(void \*), void \*arg);

[ 437](pthread_8h.md#a37075410fbbaad7ee93c95375fc86e0e)int [pthread\_setcancelstate](pthread_8h.md#a37075410fbbaad7ee93c95375fc86e0e)(int [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90), int \*oldstate);

[ 438](pthread_8h.md#aab579bcfcf0662a0c1e35fd82162e61d)int [pthread\_setcanceltype](pthread_8h.md#aab579bcfcf0662a0c1e35fd82162e61d)(int type, int \*oldtype);

[ 439](pthread_8h.md#af1c95282ab2bea25f0888a19652cd41f)void [pthread\_testcancel](pthread_8h.md#af1c95282ab2bea25f0888a19652cd41f)(void);

[ 440](pthread_8h.md#a18b9aa91fe20481a25650df20c567ff5)int [pthread\_attr\_setschedparam](pthread_8h.md#a18b9aa91fe20481a25650df20c567ff5)([pthread\_attr\_t](posix__types_8h.md#a1d96fa5809832849f591deef6cc7af7a) \*attr,

441 const struct sched\_param \*schedparam);

[ 442](pthread_8h.md#ad8e89d31b56c88d632ba9aeb956fa043)int [pthread\_setschedparam](pthread_8h.md#ad8e89d31b56c88d632ba9aeb956fa043)([pthread\_t](posix__types_8h.md#a405938c67e9c568fde9993c7e14d58ec) pthread, int policy,

443 const struct sched\_param \*param);

[ 444](pthread_8h.md#a7a23cbcfc21a4e3edf531ed65f022370)int [pthread\_setschedprio](pthread_8h.md#a7a23cbcfc21a4e3edf531ed65f022370)([pthread\_t](posix__types_8h.md#a405938c67e9c568fde9993c7e14d58ec) thread, int prio);

[ 445](pthread_8h.md#a79839f0f4f4a768bf6d218faf377c209)int [pthread\_rwlock\_destroy](pthread_8h.md#a79839f0f4f4a768bf6d218faf377c209)([pthread\_rwlock\_t](posix__types_8h.md#acd12f65541fede33b6226f646e900ea6) \*rwlock);

[ 446](pthread_8h.md#a1596a13569ec35ee66cc867586fd643d)int [pthread\_rwlock\_init](pthread_8h.md#a1596a13569ec35ee66cc867586fd643d)([pthread\_rwlock\_t](posix__types_8h.md#acd12f65541fede33b6226f646e900ea6) \*rwlock,

447 const [pthread\_rwlockattr\_t](posix__types_8h.md#a4e92e3fbb4be682babbb6796af90b50f) \*attr);

[ 448](pthread_8h.md#acc16fb32464b480d31bc69cce4e206c9)int [pthread\_rwlock\_rdlock](pthread_8h.md#acc16fb32464b480d31bc69cce4e206c9)([pthread\_rwlock\_t](posix__types_8h.md#acd12f65541fede33b6226f646e900ea6) \*rwlock);

[ 449](pthread_8h.md#ad791558625e69852e4a435b7c1580468)int [pthread\_rwlock\_timedrdlock](pthread_8h.md#ad791558625e69852e4a435b7c1580468)([pthread\_rwlock\_t](posix__types_8h.md#acd12f65541fede33b6226f646e900ea6) \*rwlock,

450 const struct [timespec](structtimespec.md) \*abstime);

[ 451](pthread_8h.md#a16c935f2f6146a95f9adbca71e0455e7)int [pthread\_rwlock\_timedwrlock](pthread_8h.md#a16c935f2f6146a95f9adbca71e0455e7)([pthread\_rwlock\_t](posix__types_8h.md#acd12f65541fede33b6226f646e900ea6) \*rwlock,

452 const struct [timespec](structtimespec.md) \*abstime);

[ 453](pthread_8h.md#aae52fb1d3e6d03b18fa5731d0b49d197)int [pthread\_rwlock\_tryrdlock](pthread_8h.md#aae52fb1d3e6d03b18fa5731d0b49d197)([pthread\_rwlock\_t](posix__types_8h.md#acd12f65541fede33b6226f646e900ea6) \*rwlock);

[ 454](pthread_8h.md#a065b618f7b786ed9bc7dddef4490cefb)int [pthread\_rwlock\_trywrlock](pthread_8h.md#a065b618f7b786ed9bc7dddef4490cefb)([pthread\_rwlock\_t](posix__types_8h.md#acd12f65541fede33b6226f646e900ea6) \*rwlock);

[ 455](pthread_8h.md#a7d3b987d99117fc10c4ef97230011983)int [pthread\_rwlock\_unlock](pthread_8h.md#a7d3b987d99117fc10c4ef97230011983)([pthread\_rwlock\_t](posix__types_8h.md#acd12f65541fede33b6226f646e900ea6) \*rwlock);

[ 456](pthread_8h.md#a5ddd4cc028257f9baa9e23c2337abe3b)int [pthread\_rwlock\_wrlock](pthread_8h.md#a5ddd4cc028257f9baa9e23c2337abe3b)([pthread\_rwlock\_t](posix__types_8h.md#acd12f65541fede33b6226f646e900ea6) \*rwlock);

[ 457](pthread_8h.md#af4b7ced8ecff505380fe8216244a3764)int [pthread\_key\_create](pthread_8h.md#af4b7ced8ecff505380fe8216244a3764)([pthread\_key\_t](posix__types_8h.md#a8fd226393057ab7a8b17ac1c8b061911) \*key,

458 void (\*destructor)(void \*));

[ 459](pthread_8h.md#aee96306dc79294927ee840bb4de2244b)int [pthread\_key\_delete](pthread_8h.md#aee96306dc79294927ee840bb4de2244b)([pthread\_key\_t](posix__types_8h.md#a8fd226393057ab7a8b17ac1c8b061911) key);

[ 460](pthread_8h.md#a2187333dd46ce08d9d2e044f79fad705)int [pthread\_setspecific](pthread_8h.md#a2187333dd46ce08d9d2e044f79fad705)([pthread\_key\_t](posix__types_8h.md#a8fd226393057ab7a8b17ac1c8b061911) key, const void \*value);

[ 461](pthread_8h.md#acdf9f73a16ea40eba1bc174d38e76ca5)void \*[pthread\_getspecific](pthread_8h.md#acdf9f73a16ea40eba1bc174d38e76ca5)([pthread\_key\_t](posix__types_8h.md#a8fd226393057ab7a8b17ac1c8b061911) key);

[ 462](pthread_8h.md#a80008474c3d68e9880da960a53d2f430)int [pthread\_atfork](pthread_8h.md#a80008474c3d68e9880da960a53d2f430)(void (\*prepare)(void), void (\*parent)(void), void (\*child)(void));

[ 463](pthread_8h.md#afb4344ea91774ba279ea5df3cb656ebc)int [pthread\_getconcurrency](pthread_8h.md#afb4344ea91774ba279ea5df3cb656ebc)(void);

[ 464](pthread_8h.md#a46064892e8c4622e0a3ebe22d9792b92)int [pthread\_setconcurrency](pthread_8h.md#a46064892e8c4622e0a3ebe22d9792b92)(int new\_level);

465

466void \_\_z\_pthread\_cleanup\_push(void \*cleanup[3], void (\*routine)(void \*arg), void \*arg);

467void \_\_z\_pthread\_cleanup\_pop(int execute);

468

[ 469](pthread_8h.md#a265bda35a73d502fe8b710dc34f421cc)#define pthread\_cleanup\_push(\_rtn, \_arg) \

470 do /\* enforce '{'-like behaviour \*/ { \

471 void \*\_z\_pthread\_cleanup[3]; \

472 \_\_z\_pthread\_cleanup\_push(\_z\_pthread\_cleanup, \_rtn, \_arg)

473

[ 474](pthread_8h.md#a234ffab9eecdb6ae28198aeeedb4f10c)#define pthread\_cleanup\_pop(\_ex) \

475 \_\_z\_pthread\_cleanup\_pop(\_ex); \

476 } /\* enforce '}'-like behaviour \*/ while (0)

477

478/\* Glibc / Oracle Extension Functions \*/

479

[ 494](pthread_8h.md#aa21465e084e7185bfbb94bb50d60cd08)int [pthread\_setname\_np](pthread_8h.md#aa21465e084e7185bfbb94bb50d60cd08)([pthread\_t](posix__types_8h.md#a405938c67e9c568fde9993c7e14d58ec) thread, const char \*name);

495

[ 511](pthread_8h.md#a8d55a60492c979991dc1a361b5453813)int [pthread\_getname\_np](pthread_8h.md#a8d55a60492c979991dc1a361b5453813)([pthread\_t](posix__types_8h.md#a405938c67e9c568fde9993c7e14d58ec) thread, char \*name, size\_t len);

512

513#ifdef CONFIG\_POSIX\_THREADS

514

520int pthread\_spin\_destroy([pthread\_spinlock\_t](posix__types_8h.md#a1d9c308dd59bf38ff0a7a45020d0aefa) \*lock);

521

527int pthread\_spin\_init([pthread\_spinlock\_t](posix__types_8h.md#a1d9c308dd59bf38ff0a7a45020d0aefa) \*lock, int pshared);

528

534int pthread\_spin\_lock([pthread\_spinlock\_t](posix__types_8h.md#a1d9c308dd59bf38ff0a7a45020d0aefa) \*lock);

535

541int pthread\_spin\_trylock([pthread\_spinlock\_t](posix__types_8h.md#a1d9c308dd59bf38ff0a7a45020d0aefa) \*lock);

542

548int pthread\_spin\_unlock([pthread\_spinlock\_t](posix__types_8h.md#a1d9c308dd59bf38ff0a7a45020d0aefa) \*lock);

549

550#endif

551

552#ifdef \_\_cplusplus

553}

554#endif

555

556#endif /\* ZEPHYR\_INCLUDE\_POSIX\_PTHREAD\_H\_ \*/

[time.h](include_2zephyr_2posix_2time_8h.md)

[ZRESTRICT](include_2zephyr_2toolchain_2common_8h.md#a39314fd705c5a9ed45b671ca36f883fd)

#define ZRESTRICT

**Definition** common.h:36

[kernel.h](kernel_8h.md)

Public kernel APIs.

[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)

state

**Definition** parser\_state.h:29

[sched.h](posix_2sched_8h.md)

[pthread\_cond\_t](posix__types_8h.md#a1b893f49dfdf497be09c04a0e40f425e)

uint32\_t pthread\_cond\_t

**Definition** posix\_types.h:126

[pthread\_attr\_t](posix__types_8h.md#a1d96fa5809832849f591deef6cc7af7a)

struct pthread\_attr pthread\_attr\_t

**Definition** posix\_types.h:103

[pthread\_spinlock\_t](posix__types_8h.md#a1d9c308dd59bf38ff0a7a45020d0aefa)

uint32\_t pthread\_spinlock\_t

**Definition** posix\_types.h:108

[pthread\_mutexattr\_t](posix__types_8h.md#a2489174ff5737a33443b0959f4278765)

struct pthread\_mutexattr pthread\_mutexattr\_t

**Definition** posix\_types.h:121

[pthread\_barrierattr\_t](posix__types_8h.md#a24d58850626c8022bf4bbd5d2628615b)

struct pthread\_barrierattr pthread\_barrierattr\_t

[pthread\_once\_t](posix__types_8h.md#a2603a6fda916554839174bc7d8849297)

struct pthread\_once pthread\_once\_t

**Definition** posix\_types.h:154

[pthread\_t](posix__types_8h.md#a405938c67e9c568fde9993c7e14d58ec)

uint32\_t pthread\_t

**Definition** posix\_types.h:107

[pthread\_mutex\_t](posix__types_8h.md#a465eb2b962de164efdc8ce957025de7e)

uint32\_t pthread\_mutex\_t

**Definition** posix\_types.h:114

[pthread\_rwlockattr\_t](posix__types_8h.md#a4e92e3fbb4be682babbb6796af90b50f)

uint32\_t pthread\_rwlockattr\_t

**Definition** posix\_types.h:144

[clockid\_t](posix__types_8h.md#a6bb3206700910111f26e946bfbf0f2af)

unsigned long clockid\_t

**Definition** posix\_types.h:21

[pthread\_key\_t](posix__types_8h.md#a8fd226393057ab7a8b17ac1c8b061911)

uint32\_t pthread\_key\_t

**Definition** posix\_types.h:153

[pthread\_condattr\_t](posix__types_8h.md#a9f62774a7a4e1634e60fb611765251f1)

struct pthread\_condattr pthread\_condattr\_t

**Definition** posix\_types.h:133

[pthread\_rwlock\_t](posix__types_8h.md#acd12f65541fede33b6226f646e900ea6)

uint32\_t pthread\_rwlock\_t

**Definition** posix\_types.h:146

[pthread\_barrier\_t](posix__types_8h.md#aeb637552f63e4c249e7aaeb2905f3db2)

uint32\_t pthread\_barrier\_t

**Definition** posix\_types.h:138

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

[pthread\_mutexattr\_destroy](pthread_8h.md#a2321aabf58224b06021185708d0f9658)

int pthread\_mutexattr\_destroy(pthread\_mutexattr\_t \*attr)

POSIX threading compatibility API.

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

[pthread\_rwlockattr\_getpshared](pthread_8h.md#a5ca1dea9ea7d3cfb34a9c8561e47cf02)

int pthread\_rwlockattr\_getpshared(const pthread\_rwlockattr\_t \*ZRESTRICT attr, int \*ZRESTRICT pshared)

[pthread\_rwlock\_wrlock](pthread_8h.md#a5ddd4cc028257f9baa9e23c2337abe3b)

int pthread\_rwlock\_wrlock(pthread\_rwlock\_t \*rwlock)

[pthread\_barrierattr\_destroy](pthread_8h.md#a5e27d4773f3d0552e36f2ff3b922a988)

int pthread\_barrierattr\_destroy(pthread\_barrierattr\_t \*b)

POSIX threading compatibility API.

[pthread\_cond\_wait](pthread_8h.md#a61a1bf88d32de361e82ef4ea99b47322)

int pthread\_cond\_wait(pthread\_cond\_t \*cv, pthread\_mutex\_t \*mut)

POSIX threading compatibility API.

[pthread\_cancel](pthread_8h.md#a66a8f4bac5afe05538794218ff7c85ea)

int pthread\_cancel(pthread\_t pthread)

[pthread\_attr\_setscope](pthread_8h.md#a6d8d320a882ba044a064975dddcf9ced)

int pthread\_attr\_setscope(pthread\_attr\_t \*attr, int contentionscope)

[pthread\_join](pthread_8h.md#a6e4d503c2b358be5c98330f9006b3417)

int pthread\_join(pthread\_t thread, void \*\*status)

[pthread\_condattr\_getclock](pthread_8h.md#a77376b018eec6db2986939b847915a3c)

int pthread\_condattr\_getclock(const pthread\_condattr\_t \*ZRESTRICT att, clockid\_t \*ZRESTRICT clock\_id)

POSIX threading compatibility API.

[pthread\_rwlockattr\_destroy](pthread_8h.md#a78a54e67f0afe2601dbda0a904fa0bdf)

int pthread\_rwlockattr\_destroy(pthread\_rwlockattr\_t \*attr)

Destroy the read-write lock attributes object.

[pthread\_mutex\_init](pthread_8h.md#a7948bc0ea8a33439aece34d0fb3daf8b)

int pthread\_mutex\_init(pthread\_mutex\_t \*m, const pthread\_mutexattr\_t \*att)

POSIX threading compatibility API.

[pthread\_rwlock\_destroy](pthread_8h.md#a79839f0f4f4a768bf6d218faf377c209)

int pthread\_rwlock\_destroy(pthread\_rwlock\_t \*rwlock)

[pthread\_attr\_getinheritsched](pthread_8h.md#a79a77b688c30213e5e52e6be178cde4e)

int pthread\_attr\_getinheritsched(const pthread\_attr\_t \*attr, int \*inheritsched)

[pthread\_attr\_setschedpolicy](pthread_8h.md#a79b4c9e71486a87ef3014f1c660b33eb)

int pthread\_attr\_setschedpolicy(pthread\_attr\_t \*attr, int policy)

[pthread\_setschedprio](pthread_8h.md#a7a23cbcfc21a4e3edf531ed65f022370)

int pthread\_setschedprio(pthread\_t thread, int prio)

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

[pthread\_rwlockattr\_init](pthread_8h.md#a9d831af0179ed16d1b6cbeba0304810b)

int pthread\_rwlockattr\_init(pthread\_rwlockattr\_t \*attr)

initialize the read-write lock attributes object.

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

[pthread\_attr\_getscope](pthread_8h.md#ad3fe01698c4fad85bb5cc3f9a2e82ea3)

int pthread\_attr\_getscope(const pthread\_attr\_t \*attr, int \*contentionscope)

[pthread\_attr\_setinheritsched](pthread_8h.md#ad437fe8caa3ef9f0cb7d69f6f6479df9)

int pthread\_attr\_setinheritsched(pthread\_attr\_t \*attr, int inheritsched)

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

[pthread\_rwlockattr\_setpshared](pthread_8h.md#ae6550aa6aede71f618bb7457f3e50524)

int pthread\_rwlockattr\_setpshared(pthread\_rwlockattr\_t \*attr, int pshared)

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

[pthread\_mutexattr\_init](pthread_8h.md#af98f6b6c483077a39d1400b1de1577b8)

int pthread\_mutexattr\_init(pthread\_mutexattr\_t \*attr)

POSIX threading compatibility API.

[pthread\_getconcurrency](pthread_8h.md#afb4344ea91774ba279ea5df3cb656ebc)

int pthread\_getconcurrency(void)

[pthread\_mutex\_lock](pthread_8h.md#afd70d6f2c50e22b996c926fb9d6ad291)

int pthread\_mutex\_lock(pthread\_mutex\_t \*m)

POSIX threading compatibility API.

[stdlib.h](stdlib_8h.md)

[string.h](string_8h.md)

[pthread\_once](structpthread__once.md)

**Definition** posix\_types.h:148

[timespec](structtimespec.md)

**Definition** \_timespec.h:22

[unistd.h](unistd_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [posix](dir_cc2c191bc57cea4eaf0dbdf53c4fb6c6.md)
- [pthread.h](pthread_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
