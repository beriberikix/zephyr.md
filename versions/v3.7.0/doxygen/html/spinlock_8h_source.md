---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/spinlock_8h_source.html
original_path: doxygen/html/spinlock_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

spinlock.h

[Go to the documentation of this file.](spinlock_8h.md)

1/\*

2 \* Copyright (c) 2018 Intel Corporation.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

11

12#ifndef ZEPHYR\_INCLUDE\_SPINLOCK\_H\_

13#define ZEPHYR\_INCLUDE\_SPINLOCK\_H\_

14

15#include <[errno.h](errno_8h.md)>

16#include <[stdbool.h](stdbool_8h.md)>

17

18#include <[zephyr/arch/cpu.h](cpu_8h.md)>

19#include <[zephyr/sys/atomic.h](sys_2atomic_8h.md)>

20#include <[zephyr/sys/\_\_assert.h](____assert_8h.md)>

21#include <[zephyr/sys/time\_units.h](time__units_8h.md)>

22

23#ifdef \_\_cplusplus

24extern "C" {

25#endif

26

33

34struct z\_spinlock\_key {

35 int key;

36};

37

[ 45](structk__spinlock.md)struct [k\_spinlock](structk__spinlock.md) {

49#ifdef CONFIG\_SMP

50#ifdef CONFIG\_TICKET\_SPINLOCKS

51 /\*

52 \* Ticket spinlocks are conceptually two atomic variables,

53 \* one indicating the current FIFO head (spinlock owner),

54 \* and the other indicating the current FIFO tail.

55 \* Spinlock is acquired in the following manner:

56 \* - current FIFO tail value is atomically incremented while it's

57 \* original value is saved as a "ticket"

58 \* - we spin until the FIFO head becomes equal to the ticket value

59 \*

60 \* Spinlock is released by atomic increment of the FIFO head

61 \*/

62 [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) owner;

63 [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) tail;

64#else

65 [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) locked;

66#endif /\* CONFIG\_TICKET\_SPINLOCKS \*/

67#endif /\* CONFIG\_SMP \*/

68

69#ifdef CONFIG\_SPIN\_VALIDATE

70 /\* Stores the thread that holds the lock with the locking CPU

71 \* ID in the bottom two bits.

72 \*/

73 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) thread\_cpu;

74#ifdef CONFIG\_SPIN\_LOCK\_TIME\_LIMIT

75 /\* Stores the time (in cycles) when a lock was taken

76 \*/

77 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) lock\_time;

78#endif /\* CONFIG\_SPIN\_LOCK\_TIME\_LIMIT \*/

79#endif /\* CONFIG\_SPIN\_VALIDATE \*/

80

81#if defined(CONFIG\_CPP) && !defined(CONFIG\_SMP) && \

82 !defined(CONFIG\_SPIN\_VALIDATE)

83 /\* If CONFIG\_SMP and CONFIG\_SPIN\_VALIDATE are both not defined

84 \* the k\_spinlock struct will have no members. The result

85 \* is that in C sizeof(k\_spinlock) is 0 and in C++ it is 1.

86 \*

87 \* This size difference causes problems when the k\_spinlock

88 \* is embedded into another struct like k\_msgq, because C and

89 \* C++ will have different ideas on the offsets of the members

90 \* that come after the k\_spinlock member.

91 \*

92 \* To prevent this we add a 1 byte dummy member to k\_spinlock

93 \* when the user selects C++ support and k\_spinlock would

94 \* otherwise be empty.

95 \*/

96 char dummy;

97#endif

101};

102

103/\* There's a spinlock validation framework available when asserts are

104 \* enabled. It adds a relatively hefty overhead (about 3k or so) to

105 \* kernel code size, don't use on platforms known to be small.

106 \*/

107#ifdef CONFIG\_SPIN\_VALIDATE

108bool z\_spin\_lock\_valid(struct [k\_spinlock](structk__spinlock.md) \*l);

109bool z\_spin\_unlock\_valid(struct [k\_spinlock](structk__spinlock.md) \*l);

110void z\_spin\_lock\_set\_owner(struct [k\_spinlock](structk__spinlock.md) \*l);

111BUILD\_ASSERT(CONFIG\_MP\_MAX\_NUM\_CPUS <= 4, "Too many CPUs for mask");

112

113# ifdef CONFIG\_KERNEL\_COHERENCE

114bool z\_spin\_lock\_mem\_coherent(struct [k\_spinlock](structk__spinlock.md) \*l);

115# endif /\* CONFIG\_KERNEL\_COHERENCE \*/

116

117#endif /\* CONFIG\_SPIN\_VALIDATE \*/

118

[ 130](group__spinlock__apis.md#gacacd3d3bbd31416dbbf6a0239be82ef0)typedef struct z\_spinlock\_key [k\_spinlock\_key\_t](group__spinlock__apis.md#gacacd3d3bbd31416dbbf6a0239be82ef0);

131

132static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void z\_spinlock\_validate\_pre(struct [k\_spinlock](structk__spinlock.md) \*l)

133{

134 ARG\_UNUSED(l);

135#ifdef CONFIG\_SPIN\_VALIDATE

136 \_\_ASSERT(z\_spin\_lock\_valid(l), "Invalid spinlock %p", l);

137#ifdef CONFIG\_KERNEL\_COHERENCE

138 \_\_ASSERT\_NO\_MSG(z\_spin\_lock\_mem\_coherent(l));

139#endif

140#endif

141}

142

143static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void z\_spinlock\_validate\_post(struct [k\_spinlock](structk__spinlock.md) \*l)

144{

145 ARG\_UNUSED(l);

146#ifdef CONFIG\_SPIN\_VALIDATE

147 z\_spin\_lock\_set\_owner(l);

148#if defined(CONFIG\_SPIN\_LOCK\_TIME\_LIMIT) && (CONFIG\_SPIN\_LOCK\_TIME\_LIMIT != 0)

149 l->lock\_time = [sys\_clock\_cycle\_get\_32](arc_2v2_2misc_8h.md#a42dcd1878309a82246dbfa26510f868a)();

150#endif /\* CONFIG\_SPIN\_LOCK\_TIME\_LIMIT \*/

151#endif /\* CONFIG\_SPIN\_VALIDATE \*/

152}

153

[ 182](group__spinlock__apis.md#gaac60da4347f5b29ff8c4e5f24c99b3bf)static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [k\_spinlock\_key\_t](group__spinlock__apis.md#gacacd3d3bbd31416dbbf6a0239be82ef0) [k\_spin\_lock](group__spinlock__apis.md#gaac60da4347f5b29ff8c4e5f24c99b3bf)(struct [k\_spinlock](structk__spinlock.md) \*l)

183{

184 ARG\_UNUSED(l);

185 [k\_spinlock\_key\_t](group__spinlock__apis.md#gacacd3d3bbd31416dbbf6a0239be82ef0) k;

186

187 /\* Note that we need to use the underlying arch-specific lock

188 \* implementation. The "irq\_lock()" API in SMP context is

189 \* actually a wrapper for a global spinlock!

190 \*/

191 k.key = [arch\_irq\_lock](arch_2arc_2v2_2irq_8h.md#a1496f4f860a99f42e1aee15ce5c9b3e2)();

192

193 z\_spinlock\_validate\_pre(l);

194#ifdef CONFIG\_SMP

195#ifdef CONFIG\_TICKET\_SPINLOCKS

196 /\*

197 \* Enqueue ourselves to the end of a spinlock waiters queue

198 \* receiving a ticket

199 \*/

200 [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) ticket = [atomic\_inc](group__atomic__apis.md#gaae47a9cbe5a6534967b417f602b37ac2)(&l->tail);

201 /\* Spin until our ticket is served \*/

202 while ([atomic\_get](group__atomic__apis.md#ga33bb426a17535bd1022895a7e44b32fa)(&l->owner) != ticket) {

203 [arch\_spin\_relax](arch__interface_8h.md#a9932b29bc0c3b86e4f8cbd6708ef5d9c)();

204 }

205#else

206 while (![atomic\_cas](group__atomic__apis.md#gab879da5aa1ffcc317adc664c016586f7)(&l->locked, 0, 1)) {

207 [arch\_spin\_relax](arch__interface_8h.md#a9932b29bc0c3b86e4f8cbd6708ef5d9c)();

208 }

209#endif /\* CONFIG\_TICKET\_SPINLOCKS \*/

210#endif /\* CONFIG\_SMP \*/

211 z\_spinlock\_validate\_post(l);

212

213 return k;

214}

215

[ 230](group__spinlock__apis.md#ga680d878eaa0e7a2f10c6e992791855ee)static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) int [k\_spin\_trylock](group__spinlock__apis.md#ga680d878eaa0e7a2f10c6e992791855ee)(struct [k\_spinlock](structk__spinlock.md) \*l, [k\_spinlock\_key\_t](group__spinlock__apis.md#gacacd3d3bbd31416dbbf6a0239be82ef0) \*k)

231{

232 int key = [arch\_irq\_lock](arch_2arc_2v2_2irq_8h.md#a1496f4f860a99f42e1aee15ce5c9b3e2)();

233

234 z\_spinlock\_validate\_pre(l);

235#ifdef CONFIG\_SMP

236#ifdef CONFIG\_TICKET\_SPINLOCKS

237 /\*

238 \* atomic\_get and atomic\_cas operations below are not executed

239 \* simultaneously.

240 \* So in theory k\_spin\_trylock can lock an already locked spinlock.

241 \* To reproduce this the following conditions should be met after we

242 \* executed atomic\_get and before we executed atomic\_cas:

243 \*

244 \* - spinlock needs to be taken 0xffff\_...\_ffff + 1 times

245 \* (which requires 0xffff\_...\_ffff number of CPUs, as k\_spin\_lock call

246 \* is blocking) or

247 \* - spinlock needs to be taken and released 0xffff\_...\_ffff times and

248 \* then taken again

249 \*

250 \* In real-life systems this is considered non-reproducible given that

251 \* required actions need to be done during this tiny window of several

252 \* CPU instructions (which execute with interrupt locked,

253 \* so no preemption can happen here)

254 \*/

255 [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) ticket\_val = [atomic\_get](group__atomic__apis.md#ga33bb426a17535bd1022895a7e44b32fa)(&l->owner);

256

257 if (![atomic\_cas](group__atomic__apis.md#gab879da5aa1ffcc317adc664c016586f7)(&l->tail, ticket\_val, ticket\_val + 1)) {

258 goto busy;

259 }

260#else

261 if (![atomic\_cas](group__atomic__apis.md#gab879da5aa1ffcc317adc664c016586f7)(&l->locked, 0, 1)) {

262 goto busy;

263 }

264#endif /\* CONFIG\_TICKET\_SPINLOCKS \*/

265#endif /\* CONFIG\_SMP \*/

266 z\_spinlock\_validate\_post(l);

267

268 k->key = key;

269

270 return 0;

271

272#ifdef CONFIG\_SMP

273busy:

274 [arch\_irq\_unlock](arch_2arc_2v2_2irq_8h.md#a203e02b994beba0d006dad9f6d797c27)(key);

275 return -[EBUSY](group__system__errno.md#ga8368025077a0385849d6817b2007c095);

276#endif /\* CONFIG\_SMP \*/

277}

278

[ 300](group__spinlock__apis.md#gaa54fc60d17d1033276aed4605671ed8e)static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void [k\_spin\_unlock](group__spinlock__apis.md#gaa54fc60d17d1033276aed4605671ed8e)(struct [k\_spinlock](structk__spinlock.md) \*l,

301 [k\_spinlock\_key\_t](group__spinlock__apis.md#gacacd3d3bbd31416dbbf6a0239be82ef0) key)

302{

303 ARG\_UNUSED(l);

304#ifdef CONFIG\_SPIN\_VALIDATE

305 \_\_ASSERT(z\_spin\_unlock\_valid(l), "Not my spinlock %p", l);

306

307#if defined(CONFIG\_SPIN\_LOCK\_TIME\_LIMIT) && (CONFIG\_SPIN\_LOCK\_TIME\_LIMIT != 0)

308 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) delta = [sys\_clock\_cycle\_get\_32](arc_2v2_2misc_8h.md#a42dcd1878309a82246dbfa26510f868a)() - l->lock\_time;

309

310 \_\_ASSERT(delta < CONFIG\_SPIN\_LOCK\_TIME\_LIMIT,

311 "Spin lock %p held %u cycles, longer than limit of %u cycles",

312 l, delta, CONFIG\_SPIN\_LOCK\_TIME\_LIMIT);

313#endif /\* CONFIG\_SPIN\_LOCK\_TIME\_LIMIT \*/

314#endif /\* CONFIG\_SPIN\_VALIDATE \*/

315

316#ifdef CONFIG\_SMP

317#ifdef CONFIG\_TICKET\_SPINLOCKS

318 /\* Give the spinlock to the next CPU in a FIFO \*/

319 (void)[atomic\_inc](group__atomic__apis.md#gaae47a9cbe5a6534967b417f602b37ac2)(&l->owner);

320#else

321 /\* Strictly we don't need atomic\_clear() here (which is an

322 \* exchange operation that returns the old value). We are always

323 \* setting a zero and (because we hold the lock) know the existing

324 \* state won't change due to a race. But some architectures need

325 \* a memory barrier when used like this, and we don't have a

326 \* Zephyr framework for that.

327 \*/

328 (void)[atomic\_clear](group__atomic__apis.md#ga879b5f540c25fd09f1b84563e3dc8a91)(&l->locked);

329#endif /\* CONFIG\_TICKET\_SPINLOCKS \*/

330#endif /\* CONFIG\_SMP \*/

331 [arch\_irq\_unlock](arch_2arc_2v2_2irq_8h.md#a203e02b994beba0d006dad9f6d797c27)(key.key);

332}

333

337

338#if defined(CONFIG\_SMP) && defined(CONFIG\_TEST)

339/\*

340 \* @brief Checks if spinlock is held by some CPU, including the local CPU.

341 \* This API shouldn't be used outside the tests for spinlock

342 \*

343 \* @param l A pointer to the spinlock

344 \* @retval true - if spinlock is held by some CPU; false - otherwise

345 \*/

346static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) bool z\_spin\_is\_locked(struct [k\_spinlock](structk__spinlock.md) \*l)

347{

348#ifdef CONFIG\_TICKET\_SPINLOCKS

349 [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) ticket\_val = [atomic\_get](group__atomic__apis.md#ga33bb426a17535bd1022895a7e44b32fa)(&l->owner);

350

351 return ![atomic\_cas](group__atomic__apis.md#gab879da5aa1ffcc317adc664c016586f7)(&l->tail, ticket\_val, ticket\_val);

352#else

353 return l->locked;

354#endif /\* CONFIG\_TICKET\_SPINLOCKS \*/

355}

356#endif /\* defined(CONFIG\_SMP) && defined(CONFIG\_TEST) \*/

357

358/\* Internal function: releases the lock, but leaves local interrupts disabled \*/

359static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void k\_spin\_release(struct [k\_spinlock](structk__spinlock.md) \*l)

360{

361 ARG\_UNUSED(l);

362#ifdef CONFIG\_SPIN\_VALIDATE

363 \_\_ASSERT(z\_spin\_unlock\_valid(l), "Not my spinlock %p", l);

364#endif

365#ifdef CONFIG\_SMP

366#ifdef CONFIG\_TICKET\_SPINLOCKS

367 (void)[atomic\_inc](group__atomic__apis.md#gaae47a9cbe5a6534967b417f602b37ac2)(&l->owner);

368#else

369 (void)[atomic\_clear](group__atomic__apis.md#ga879b5f540c25fd09f1b84563e3dc8a91)(&l->locked);

370#endif /\* CONFIG\_TICKET\_SPINLOCKS \*/

371#endif /\* CONFIG\_SMP \*/

372}

373

374#if defined(CONFIG\_SPIN\_VALIDATE) && defined(\_\_GNUC\_\_)

375static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void z\_spin\_onexit(\_\_maybe\_unused [k\_spinlock\_key\_t](group__spinlock__apis.md#gacacd3d3bbd31416dbbf6a0239be82ef0) \*k)

376{

377 \_\_ASSERT(k->key, "K\_SPINLOCK exited with goto, break or return, "

378 "use K\_SPINLOCK\_BREAK instead.");

379}

380#define K\_SPINLOCK\_ONEXIT \_\_attribute\_\_((\_\_cleanup\_\_(z\_spin\_onexit)))

381#else

382#define K\_SPINLOCK\_ONEXIT

383#endif

384

388

[ 395](group__spinlock__apis.md#ga7b16542003f7eca7f5bcae5ba494f823)#define K\_SPINLOCK\_BREAK continue

396

[ 438](group__spinlock__apis.md#ga6d0db300193464dc4e603110e891f856)#define K\_SPINLOCK(lck) \

439 for (k\_spinlock\_key\_t \_\_i K\_SPINLOCK\_ONEXIT = {}, \_\_key = k\_spin\_lock(lck); !\_\_i.key; \

440 k\_spin\_unlock((lck), \_\_key), \_\_i.key = 1)

441

443

444#ifdef \_\_cplusplus

445}

446#endif

447

448#endif /\* ZEPHYR\_INCLUDE\_SPINLOCK\_H\_ \*/

[\_\_assert.h](____assert_8h.md)

[sys\_clock\_cycle\_get\_32](arc_2v2_2misc_8h.md#a42dcd1878309a82246dbfa26510f868a)

uint32\_t sys\_clock\_cycle\_get\_32(void)

[arch\_irq\_lock](arch_2arc_2v2_2irq_8h.md#a1496f4f860a99f42e1aee15ce5c9b3e2)

static ALWAYS\_INLINE unsigned int arch\_irq\_lock(void)

Disable all interrupts on the local CPU.

**Definition** irq.h:168

[arch\_irq\_unlock](arch_2arc_2v2_2irq_8h.md#a203e02b994beba0d006dad9f6d797c27)

static ALWAYS\_INLINE void arch\_irq\_unlock(unsigned int key)

**Definition** irq.h:176

[arch\_spin\_relax](arch__interface_8h.md#a9932b29bc0c3b86e4f8cbd6708ef5d9c)

void arch\_spin\_relax(void)

Perform architecture specific processing within spin loops.

[atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8)

long atomic\_t

**Definition** atomic\_types.h:15

[atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1)

atomic\_t atomic\_val\_t

**Definition** atomic\_types.h:16

[ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a)

#define ALWAYS\_INLINE

**Definition** common.h:129

[cpu.h](cpu_8h.md)

[errno.h](errno_8h.md)

System error numbers.

[atomic\_get](group__atomic__apis.md#ga33bb426a17535bd1022895a7e44b32fa)

atomic\_val\_t atomic\_get(const atomic\_t \*target)

Atomic get.

[atomic\_clear](group__atomic__apis.md#ga879b5f540c25fd09f1b84563e3dc8a91)

atomic\_val\_t atomic\_clear(atomic\_t \*target)

Atomic clear.

[atomic\_inc](group__atomic__apis.md#gaae47a9cbe5a6534967b417f602b37ac2)

atomic\_val\_t atomic\_inc(atomic\_t \*target)

Atomic increment.

[atomic\_cas](group__atomic__apis.md#gab879da5aa1ffcc317adc664c016586f7)

bool atomic\_cas(atomic\_t \*target, atomic\_val\_t old\_value, atomic\_val\_t new\_value)

Atomic compare-and-set.

[k\_spin\_trylock](group__spinlock__apis.md#ga680d878eaa0e7a2f10c6e992791855ee)

static ALWAYS\_INLINE int k\_spin\_trylock(struct k\_spinlock \*l, k\_spinlock\_key\_t \*k)

Attempt to lock a spinlock.

**Definition** spinlock.h:230

[k\_spin\_unlock](group__spinlock__apis.md#gaa54fc60d17d1033276aed4605671ed8e)

static ALWAYS\_INLINE void k\_spin\_unlock(struct k\_spinlock \*l, k\_spinlock\_key\_t key)

Unlock a spin lock.

**Definition** spinlock.h:300

[k\_spin\_lock](group__spinlock__apis.md#gaac60da4347f5b29ff8c4e5f24c99b3bf)

static ALWAYS\_INLINE k\_spinlock\_key\_t k\_spin\_lock(struct k\_spinlock \*l)

Lock a spinlock.

**Definition** spinlock.h:182

[k\_spinlock\_key\_t](group__spinlock__apis.md#gacacd3d3bbd31416dbbf6a0239be82ef0)

struct z\_spinlock\_key k\_spinlock\_key\_t

Spinlock key type.

**Definition** spinlock.h:130

[EBUSY](group__system__errno.md#ga8368025077a0385849d6817b2007c095)

#define EBUSY

Mount device busy.

**Definition** errno.h:54

[stdbool.h](stdbool_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808)

\_\_UINTPTR\_TYPE\_\_ uintptr\_t

**Definition** stdint.h:105

[k\_spinlock](structk__spinlock.md)

Kernel Spin Lock.

**Definition** spinlock.h:45

[atomic.h](sys_2atomic_8h.md)

[time\_units.h](time__units_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [spinlock.h](spinlock_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
