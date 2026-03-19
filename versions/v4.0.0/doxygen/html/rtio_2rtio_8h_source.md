---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/rtio_2rtio_8h_source.html
original_path: doxygen/html/rtio_2rtio_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

rtio.h

[Go to the documentation of this file.](rtio_2rtio_8h.md)

1/\*

2 \* Copyright (c) 2022 Intel Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

25

26#ifndef ZEPHYR\_INCLUDE\_RTIO\_RTIO\_H\_

27#define ZEPHYR\_INCLUDE\_RTIO\_RTIO\_H\_

28

29#include <[string.h](string_8h.md)>

30

31#include <[zephyr/app\_memory/app\_memdomain.h](app__memdomain_8h.md)>

32#include <[zephyr/device.h](device_8h.md)>

33#include <[zephyr/kernel.h](kernel_8h.md)>

34#include <[zephyr/sys/\_\_assert.h](____assert_8h.md)>

35#include <[zephyr/sys/atomic.h](sys_2atomic_8h.md)>

36#include <[zephyr/sys/mem\_blocks.h](mem__blocks_8h.md)>

37#include <[zephyr/sys/util.h](sys_2util_8h.md)>

38#include <[zephyr/sys/iterable\_sections.h](sys_2iterable__sections_8h.md)>

39#include <[zephyr/sys/mpsc\_lockfree.h](mpsc__lockfree_8h.md)>

40

41#ifdef \_\_cplusplus

42extern "C" {

43#endif

44

45

54

61

[ 65](group__rtio__sqe__prio.md#gabc81232a7d4b7145d9898afd6ff2ae48)#define RTIO\_PRIO\_LOW 0U

66

[ 70](group__rtio__sqe__prio.md#gab02e27e01b7dd4eb3439df557899ce92)#define RTIO\_PRIO\_NORM 127U

71

[ 75](group__rtio__sqe__prio.md#ga220baa9bf2c8ff0cb6f52f0220e72b30)#define RTIO\_PRIO\_HIGH 255U

76

80

81

88

[ 96](group__rtio__sqe__flags.md#gae9191d521d4ab602b53fefb74020d06b)#define RTIO\_SQE\_CHAINED BIT(0)

97

[ 108](group__rtio__sqe__flags.md#ga07f09cc0c95be6cfdddb23f8acacb1ea)#define RTIO\_SQE\_TRANSACTION BIT(1)

109

110

[ 120](group__rtio__sqe__flags.md#ga2802b46584220afffa0e959e149d5a4d)#define RTIO\_SQE\_MEMPOOL\_BUFFER BIT(2)

121

[ 128](group__rtio__sqe__flags.md#ga7f7f9b038ab8409f271b1aebc1b95ee6)#define RTIO\_SQE\_CANCELED BIT(3)

129

[ 136](group__rtio__sqe__flags.md#ga00f8ead8f043fe40d49d0bc3325fb299)#define RTIO\_SQE\_MULTISHOT BIT(4)

137

[ 141](group__rtio__sqe__flags.md#ga8578ffdb8f53a51b94fa86a6f02d4a11)#define RTIO\_SQE\_NO\_RESPONSE BIT(5)

142

146

153

[ 160](group__rtio__cqe__flags.md#ga0f212500447a5e37e225a6997953b609)#define RTIO\_CQE\_FLAG\_MEMPOOL\_BUFFER BIT(0)

161

[ 162](group__rtio__cqe__flags.md#gaef64ea020a20ac22a0edcb6eca032efc)#define RTIO\_CQE\_FLAG\_GET(flags) FIELD\_GET(GENMASK(7, 0), (flags))

163

[ 170](group__rtio__cqe__flags.md#ga0b5f3f7e7be472ecf87bd2b08c1888da)#define RTIO\_CQE\_FLAG\_MEMPOOL\_GET\_BLK\_IDX(flags) FIELD\_GET(GENMASK(19, 8), (flags))

171

[ 178](group__rtio__cqe__flags.md#ga087465f866d417d5332602bb582cc1a7)#define RTIO\_CQE\_FLAG\_MEMPOOL\_GET\_BLK\_CNT(flags) FIELD\_GET(GENMASK(31, 20), (flags))

179

[ 187](group__rtio__cqe__flags.md#ga28b3a5661248b6b3763aab47417114d6)#define RTIO\_CQE\_FLAG\_PREP\_MEMPOOL(blk\_idx, blk\_cnt) \

188 (FIELD\_PREP(GENMASK(7, 0), RTIO\_CQE\_FLAG\_MEMPOOL\_BUFFER) | \

189 FIELD\_PREP(GENMASK(19, 8), blk\_idx) | FIELD\_PREP(GENMASK(31, 20), blk\_cnt))

190

194

[ 198](group__rtio.md#gaf923e862d2c6a3fbce5eb96781cf86d8)#define RTIO\_IODEV\_I2C\_STOP BIT(1)

199

[ 203](group__rtio.md#gadba1c5eddeecc431000bd92054f55c3a)#define RTIO\_IODEV\_I2C\_RESTART BIT(2)

204

[ 208](group__rtio.md#gaa0c3b047c7205d12775d8d38907119b9)#define RTIO\_IODEV\_I2C\_10\_BITS BIT(3)

209

211struct [rtio](structrtio.md);

212struct [rtio\_cqe](structrtio__cqe.md);

213struct [rtio\_sqe](structrtio__sqe.md);

214struct [rtio\_sqe\_pool](structrtio__sqe__pool.md);

215struct [rtio\_cqe\_pool](structrtio__cqe__pool.md);

216struct [rtio\_iodev](structrtio__iodev.md);

217struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md);

219

[ 227](group__rtio.md#gad1dbd690e6cf88d7c788436dd04d1a00)typedef void (\*[rtio\_callback\_t](group__rtio.md#gad1dbd690e6cf88d7c788436dd04d1a00))(struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2), const struct [rtio\_sqe](structrtio__sqe.md) \*sqe, void \*[arg0](structrtio__sqe.md#a438d2156a61aef9ca840af9c01d5dfa4));

228

[ 232](structrtio__sqe.md)struct [rtio\_sqe](structrtio__sqe.md) {

[ 233](structrtio__sqe.md#a1d8d3e3426e47a2c7f54d98f51acd953) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [op](structrtio__sqe.md#a1d8d3e3426e47a2c7f54d98f51acd953);

234

[ 235](structrtio__sqe.md#a528eb9b721be7b8a8898ab16a7e2d9a7) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [prio](structrtio__sqe.md#a528eb9b721be7b8a8898ab16a7e2d9a7);

236

[ 237](structrtio__sqe.md#aad2ff8524df0e24b812e77e2393bf5b0) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [flags](structrtio__sqe.md#aad2ff8524df0e24b812e77e2393bf5b0);

238

[ 239](structrtio__sqe.md#af979ffa7bd3efaa6cbcb1344404cb985) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [iodev\_flags](structrtio__sqe.md#af979ffa7bd3efaa6cbcb1344404cb985);

240

241 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \_resv0;

242

[ 243](structrtio__sqe.md#a6c784702f011592c84feacd57915bbfc) const struct [rtio\_iodev](structrtio__iodev.md) \*[iodev](structrtio__sqe.md#a6c784702f011592c84feacd57915bbfc);

244

[ 252](structrtio__sqe.md#a0ed519ee0b5867ff73bdaf37f983c971) void \*[userdata](structrtio__sqe.md#a0ed519ee0b5867ff73bdaf37f983c971);

253

254 union {

255

257 struct {

[ 258](structrtio__sqe.md#a67376f40a13960b152a23da250275722) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [buf\_len](structrtio__sqe.md#a67376f40a13960b152a23da250275722);

[ 259](structrtio__sqe.md#ab71176c084e8b8eb65dfeb3018ae2a49) const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[buf](structrtio__sqe.md#ab71176c084e8b8eb65dfeb3018ae2a49);

[ 260](structrtio__sqe.md#a4399cf25c7e761126a6218c2b7e3192d) } tx;

261

263 struct {

264 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) buf\_len;

[ 265](structrtio__sqe.md#a55e98f27b26393fee8e179b7bdb6a52e) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[buf](structrtio__sqe.md#ab71176c084e8b8eb65dfeb3018ae2a49);

[ 266](structrtio__sqe.md#a37a98afc43f26355c70e7036725b2544) } rx;

267

269 struct {

[ 270](structrtio__sqe.md#a4125148f520b61d0fe3ba156fbb53322) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [buf\_len](structrtio__sqe.md#a67376f40a13960b152a23da250275722);

[ 271](structrtio__sqe.md#a8f0544318fa972be2541ae1e85efc33f) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [buf](structrtio__sqe.md#ab71176c084e8b8eb65dfeb3018ae2a49)[7];

[ 272](structrtio__sqe.md#a19ace9c984538c2022e7f8ecaefa075d) } tiny\_tx;

273

275 struct {

[ 276](structrtio__sqe.md#af8c31c33e9fedebe55cac73595d0f696) [rtio\_callback\_t](group__rtio.md#gad1dbd690e6cf88d7c788436dd04d1a00) [callback](structrtio__sqe.md#af8c31c33e9fedebe55cac73595d0f696);

[ 277](structrtio__sqe.md#a438d2156a61aef9ca840af9c01d5dfa4) void \*[arg0](structrtio__sqe.md#a438d2156a61aef9ca840af9c01d5dfa4);

[ 278](structrtio__sqe.md#add4f73af249b5b548ddf8f5b8d84af2b) } callback;

279

281 struct {

282 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) buf\_len;

[ 283](structrtio__sqe.md#a18bfa63542954f4bb8b924c92c48e931) const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[tx\_buf](structrtio__sqe.md#a18bfa63542954f4bb8b924c92c48e931);

[ 284](structrtio__sqe.md#a4d2090fc11b897724a883ad1087d9f73) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[rx\_buf](structrtio__sqe.md#a4d2090fc11b897724a883ad1087d9f73);

[ 285](structrtio__sqe.md#a5f2511eb361a7a4d54a92fae4d391e8c) } txrx;

286

[ 288](structrtio__sqe.md#a07bf344b1b1063b8bea80cf5ba1c1cc5) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [i2c\_config](structrtio__sqe.md#a07bf344b1b1063b8bea80cf5ba1c1cc5);

289 };

290};

291

293/\* Ensure the rtio\_sqe never grows beyond a common cacheline size of 64 bytes \*/

294BUILD\_ASSERT(sizeof(struct [rtio\_sqe](structrtio__sqe.md)) <= 64);

296

[ 300](structrtio__cqe.md)struct [rtio\_cqe](structrtio__cqe.md) {

[ 301](structrtio__cqe.md#a27272bca31c170f406799633ec82098d) struct [mpsc\_node](structmpsc__node.md) [q](structrtio__cqe.md#a27272bca31c170f406799633ec82098d);

302

[ 303](structrtio__cqe.md#acbe2e6607a752b676d9336b9ca6ce435) [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) [result](structrtio__cqe.md#acbe2e6607a752b676d9336b9ca6ce435);

[ 304](structrtio__cqe.md#a15128387ccbea55812ef229eab7241e7) void \*[userdata](structrtio__cqe.md#a15128387ccbea55812ef229eab7241e7);

[ 305](structrtio__cqe.md#a8a7632ef1cfd31529d782bd761908d93) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](structrtio__cqe.md#a8a7632ef1cfd31529d782bd761908d93);

306};

307

[ 308](structrtio__sqe__pool.md)struct [rtio\_sqe\_pool](structrtio__sqe__pool.md) {

[ 309](structrtio__sqe__pool.md#aed49ea25c952e07a8287919268fd2485) struct [mpsc](structmpsc.md) [free\_q](structrtio__sqe__pool.md#aed49ea25c952e07a8287919268fd2485);

[ 310](structrtio__sqe__pool.md#ade3b4354d007fe17a7753c26e2121465) const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [pool\_size](structrtio__sqe__pool.md#ade3b4354d007fe17a7753c26e2121465);

[ 311](structrtio__sqe__pool.md#af7990b1510ad2343573f3e4e502475b0) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [pool\_free](structrtio__sqe__pool.md#af7990b1510ad2343573f3e4e502475b0);

[ 312](structrtio__sqe__pool.md#ab2c0394e175bd8c6f0c02edb315b6c9b) struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \*[pool](structrtio__sqe__pool.md#ab2c0394e175bd8c6f0c02edb315b6c9b);

313};

314

[ 315](structrtio__cqe__pool.md)struct [rtio\_cqe\_pool](structrtio__cqe__pool.md) {

[ 316](structrtio__cqe__pool.md#a13bd7991ff5622c1cb5aa6af014aaab3) struct [mpsc](structmpsc.md) [free\_q](structrtio__cqe__pool.md#a13bd7991ff5622c1cb5aa6af014aaab3);

[ 317](structrtio__cqe__pool.md#a43bf4141673c61493644539987f27fb1) const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [pool\_size](structrtio__cqe__pool.md#a43bf4141673c61493644539987f27fb1);

[ 318](structrtio__cqe__pool.md#a4fb501a0ba15e2956113deaf4597d846) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [pool\_free](structrtio__cqe__pool.md#a4fb501a0ba15e2956113deaf4597d846);

[ 319](structrtio__cqe__pool.md#a05584219d473fcf85d46757fa9cea703) struct [rtio\_cqe](structrtio__cqe.md) \*[pool](structrtio__cqe__pool.md#a05584219d473fcf85d46757fa9cea703);

320};

321

[ 333](structrtio.md)struct [rtio](structrtio.md) {

334#ifdef CONFIG\_RTIO\_SUBMIT\_SEM

335 /\* A wait semaphore which may suspend the calling thread

336 \* to wait for some number of completions when calling submit

337 \*/

338 struct k\_sem \*submit\_sem;

339

340 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) submit\_count;

341#endif

342

343#ifdef CONFIG\_RTIO\_CONSUME\_SEM

344 /\* A wait semaphore which may suspend the calling thread

345 \* to wait for some number of completions while consuming

346 \* them from the completion queue

347 \*/

348 struct k\_sem \*consume\_sem;

349#endif

350

351 /\* Total number of completions \*/

[ 352](structrtio.md#a358de1033ab4396d1f1baee2699c993f) [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) [cq\_count](structrtio.md#a358de1033ab4396d1f1baee2699c993f);

353

354 /\* Number of completions that were unable to be submitted with results

355 \* due to the cq spsc being full

356 \*/

[ 357](structrtio.md#ac45facdcc6d64cd70113b9b05b2fb086) [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) [xcqcnt](structrtio.md#ac45facdcc6d64cd70113b9b05b2fb086);

358

359 /\* Submission queue object pool with free list \*/

[ 360](structrtio.md#a955f012bac623e7c037b5f1dba8e7fda) struct [rtio\_sqe\_pool](structrtio__sqe__pool.md) \*[sqe\_pool](structrtio.md#a955f012bac623e7c037b5f1dba8e7fda);

361

362 /\* Complete queue object pool with free list \*/

[ 363](structrtio.md#a1bce3c3bb0150275ece65975adf3ee4f) struct [rtio\_cqe\_pool](structrtio__cqe__pool.md) \*[cqe\_pool](structrtio.md#a1bce3c3bb0150275ece65975adf3ee4f);

364

365#ifdef CONFIG\_RTIO\_SYS\_MEM\_BLOCKS

366 /\* Mem block pool \*/

367 struct sys\_mem\_blocks \*block\_pool;

368#endif

369

370 /\* Submission queue \*/

[ 371](structrtio.md#a34fbabfdbef3144f4520bf678684cdfb) struct [mpsc](structmpsc.md) [sq](structrtio.md#a34fbabfdbef3144f4520bf678684cdfb);

372

373 /\* Completion queue \*/

[ 374](structrtio.md#ad6f44a354a170cb04a584beee7728fa9) struct [mpsc](structmpsc.md) [cq](structrtio.md#ad6f44a354a170cb04a584beee7728fa9);

375};

376

378extern struct [k\_mem\_partition](structk__mem__partition.md) [rtio\_partition](group__rtio.md#ga86a38086dd85150ab6e479d73db1c6d1);

379

[ 387](group__rtio.md#ga4213be028b0a1264daaa0d30c4c2d089)static inline size\_t [rtio\_mempool\_block\_size](group__rtio.md#ga4213be028b0a1264daaa0d30c4c2d089)(const struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2))

388{

389#ifndef CONFIG\_RTIO\_SYS\_MEM\_BLOCKS

390 ARG\_UNUSED([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2));

391 return 0;

392#else

393 if ([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) == NULL || [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->block\_pool == NULL) {

394 return 0;

395 }

396 return [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->block\_pool->info.blk\_sz\_shift);

397#endif

398}

399

407#ifdef CONFIG\_RTIO\_SYS\_MEM\_BLOCKS

408static inline [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \_\_rtio\_compute\_mempool\_block\_index(const struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2), const void \*ptr)

409{

410 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) addr = ([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808))ptr;

411 struct sys\_mem\_blocks \*mem\_pool = [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->block\_pool;

412 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size = [rtio\_mempool\_block\_size](group__rtio.md#ga4213be028b0a1264daaa0d30c4c2d089)([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2));

413

414 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) buff = ([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808))mem\_pool->buffer;

415 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) buff\_size = mem\_pool->info.num\_blocks \* block\_size;

416

417 if (addr < buff || addr >= buff + buff\_size) {

418 return [UINT16\_MAX](stdint_8h.md#a3ea490c9b3617d4479bd80ef93cd5602);

419 }

420 return (addr - buff) / block\_size;

421}

422#endif

423

[ 429](structrtio__iodev__sqe.md)struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) {

[ 430](structrtio__iodev__sqe.md#a2bd98599678909c0ddb22f879affa12b) struct [rtio\_sqe](structrtio__sqe.md) [sqe](structrtio__iodev__sqe.md#a2bd98599678909c0ddb22f879affa12b);

[ 431](structrtio__iodev__sqe.md#a9cfdd004b65a5e2bc111bc2fb333498c) struct [mpsc\_node](structmpsc__node.md) [q](structrtio__iodev__sqe.md#a9cfdd004b65a5e2bc111bc2fb333498c);

[ 432](structrtio__iodev__sqe.md#a2afb82e550e614f87db7cd1bf2c3a352) struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \*[next](structrtio__iodev__sqe.md#a2afb82e550e614f87db7cd1bf2c3a352);

[ 433](structrtio__iodev__sqe.md#a3c3a050793589258eab5ff5ac30f24c8) struct [rtio](structrtio.md) \*[r](structrtio__iodev__sqe.md#a3c3a050793589258eab5ff5ac30f24c8);

434};

435

[ 439](structrtio__iodev__api.md)struct [rtio\_iodev\_api](structrtio__iodev__api.md) {

[ 448](structrtio__iodev__api.md#a6cd795906753535571ec1ecc0e0c430c) void (\*[submit](structrtio__iodev__api.md#a6cd795906753535571ec1ecc0e0c430c))(struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \*iodev\_sqe);

449};

450

[ 454](structrtio__iodev.md)struct [rtio\_iodev](structrtio__iodev.md) {

455 /\* Function pointer table \*/

[ 456](structrtio__iodev.md#a6dfedbfb58356e0647e5c20632656977) const struct [rtio\_iodev\_api](structrtio__iodev__api.md) \*[api](structrtio__iodev.md#a6dfedbfb58356e0647e5c20632656977);

457

458 /\* Data associated with this iodev \*/

[ 459](structrtio__iodev.md#af0f3a27fe8dea2161c9a73cb838bdeec) void \*[data](structrtio__iodev.md#af0f3a27fe8dea2161c9a73cb838bdeec);

460};

461

[ 463](group__rtio.md#gad5f073978f641413989d1c6b405d6c36)#define RTIO\_OP\_NOP 0

464

[ 466](group__rtio.md#gafeb05c351207cd1638fa78f6607e1a4a)#define RTIO\_OP\_RX (RTIO\_OP\_NOP+1)

467

[ 469](group__rtio.md#ga8dcaef0cda159e16520a95543ff62827)#define RTIO\_OP\_TX (RTIO\_OP\_RX+1)

470

[ 472](group__rtio.md#ga6f95c0a5fbcc020a0d1102d3b08934bd)#define RTIO\_OP\_TINY\_TX (RTIO\_OP\_TX+1)

473

[ 475](group__rtio.md#ga18e0ff7d44e4c33900106aefad0a8508)#define RTIO\_OP\_CALLBACK (RTIO\_OP\_TINY\_TX+1)

476

[ 478](group__rtio.md#ga9f0e70f5a28be65a8ed67c0257a72692)#define RTIO\_OP\_TXRX (RTIO\_OP\_CALLBACK+1)

479

[ 481](group__rtio.md#ga3b4f9b1ee1612290323161ecc16e0859)#define RTIO\_OP\_I2C\_RECOVER (RTIO\_OP\_TXRX+1)

482

[ 484](group__rtio.md#gad987be3acfe406b11419c7e8cd068cf5)#define RTIO\_OP\_I2C\_CONFIGURE (RTIO\_OP\_I2C\_RECOVER+1)

485

[ 489](group__rtio.md#ga599ee43fdf35e1cf895cbbe9272e4c50)static inline void [rtio\_sqe\_prep\_nop](group__rtio.md#ga599ee43fdf35e1cf895cbbe9272e4c50)(struct [rtio\_sqe](structrtio__sqe.md) \*sqe,

490 const struct [rtio\_iodev](structrtio__iodev.md) \*iodev,

491 void \*userdata)

492{

493 [memset](string_8h.md#a4137694174d4ca2fad886a1db355015c)(sqe, 0, sizeof(struct [rtio\_sqe](structrtio__sqe.md)));

494 sqe->[op](structrtio__sqe.md#a1d8d3e3426e47a2c7f54d98f51acd953) = [RTIO\_OP\_NOP](group__rtio.md#gad5f073978f641413989d1c6b405d6c36);

495 sqe->[iodev](structrtio__sqe.md#a6c784702f011592c84feacd57915bbfc) = iodev;

496 sqe->[userdata](structrtio__sqe.md#a0ed519ee0b5867ff73bdaf37f983c971) = userdata;

497}

498

[ 502](group__rtio.md#ga89c7cc2494e3dda50737f78f1a1376cf)static inline void [rtio\_sqe\_prep\_read](group__rtio.md#ga89c7cc2494e3dda50737f78f1a1376cf)(struct [rtio\_sqe](structrtio__sqe.md) \*sqe,

503 const struct [rtio\_iodev](structrtio__iodev.md) \*iodev,

504 [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) prio,

505 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf,

506 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) len,

507 void \*userdata)

508{

509 [memset](string_8h.md#a4137694174d4ca2fad886a1db355015c)(sqe, 0, sizeof(struct [rtio\_sqe](structrtio__sqe.md)));

510 sqe->[op](structrtio__sqe.md#a1d8d3e3426e47a2c7f54d98f51acd953) = [RTIO\_OP\_RX](group__rtio.md#gafeb05c351207cd1638fa78f6607e1a4a);

511 sqe->[prio](structrtio__sqe.md#a528eb9b721be7b8a8898ab16a7e2d9a7) = prio;

512 sqe->[iodev](structrtio__sqe.md#a6c784702f011592c84feacd57915bbfc) = iodev;

513 sqe->[rx](structrtio__sqe.md#a37a98afc43f26355c70e7036725b2544).[buf\_len](structrtio__sqe.md#a67376f40a13960b152a23da250275722) = len;

514 sqe->[rx](structrtio__sqe.md#a37a98afc43f26355c70e7036725b2544).[buf](structrtio__sqe.md#ab71176c084e8b8eb65dfeb3018ae2a49) = buf;

515 sqe->[userdata](structrtio__sqe.md#a0ed519ee0b5867ff73bdaf37f983c971) = userdata;

516}

517

[ 523](group__rtio.md#ga15c1f623658d27d300d1a31a6f3d6b9d)static inline void [rtio\_sqe\_prep\_read\_with\_pool](group__rtio.md#ga15c1f623658d27d300d1a31a6f3d6b9d)(struct [rtio\_sqe](structrtio__sqe.md) \*sqe,

524 const struct [rtio\_iodev](structrtio__iodev.md) \*iodev, [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) prio,

525 void \*userdata)

526{

527 [rtio\_sqe\_prep\_read](group__rtio.md#ga89c7cc2494e3dda50737f78f1a1376cf)(sqe, iodev, prio, NULL, 0, userdata);

528 sqe->[flags](structrtio__sqe.md#aad2ff8524df0e24b812e77e2393bf5b0) = [RTIO\_SQE\_MEMPOOL\_BUFFER](group__rtio__sqe__flags.md#ga2802b46584220afffa0e959e149d5a4d);

529}

530

[ 531](group__rtio.md#ga9803aa829f8c0eeee746ea7d872c20cc)static inline void [rtio\_sqe\_prep\_read\_multishot](group__rtio.md#ga9803aa829f8c0eeee746ea7d872c20cc)(struct [rtio\_sqe](structrtio__sqe.md) \*sqe,

532 const struct [rtio\_iodev](structrtio__iodev.md) \*iodev, [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) prio,

533 void \*userdata)

534{

535 [rtio\_sqe\_prep\_read\_with\_pool](group__rtio.md#ga15c1f623658d27d300d1a31a6f3d6b9d)(sqe, iodev, prio, userdata);

536 sqe->[flags](structrtio__sqe.md#aad2ff8524df0e24b812e77e2393bf5b0) |= [RTIO\_SQE\_MULTISHOT](group__rtio__sqe__flags.md#ga00f8ead8f043fe40d49d0bc3325fb299);

537}

538

[ 542](group__rtio.md#ga7f7856d1f4fd1d8c4f6eebcccfe77701)static inline void [rtio\_sqe\_prep\_write](group__rtio.md#ga7f7856d1f4fd1d8c4f6eebcccfe77701)(struct [rtio\_sqe](structrtio__sqe.md) \*sqe,

543 const struct [rtio\_iodev](structrtio__iodev.md) \*iodev,

544 [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) prio,

545 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf,

546 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) len,

547 void \*userdata)

548{

549 [memset](string_8h.md#a4137694174d4ca2fad886a1db355015c)(sqe, 0, sizeof(struct [rtio\_sqe](structrtio__sqe.md)));

550 sqe->[op](structrtio__sqe.md#a1d8d3e3426e47a2c7f54d98f51acd953) = [RTIO\_OP\_TX](group__rtio.md#ga8dcaef0cda159e16520a95543ff62827);

551 sqe->[prio](structrtio__sqe.md#a528eb9b721be7b8a8898ab16a7e2d9a7) = prio;

552 sqe->[iodev](structrtio__sqe.md#a6c784702f011592c84feacd57915bbfc) = iodev;

553 sqe->[tx](structrtio__sqe.md#a4399cf25c7e761126a6218c2b7e3192d).[buf\_len](structrtio__sqe.md#a67376f40a13960b152a23da250275722) = len;

554 sqe->[tx](structrtio__sqe.md#a4399cf25c7e761126a6218c2b7e3192d).[buf](structrtio__sqe.md#ab71176c084e8b8eb65dfeb3018ae2a49) = buf;

555 sqe->[userdata](structrtio__sqe.md#a0ed519ee0b5867ff73bdaf37f983c971) = userdata;

556}

557

[ 568](group__rtio.md#ga31be14ece09e061a8d42ca8f2395286a)static inline void [rtio\_sqe\_prep\_tiny\_write](group__rtio.md#ga31be14ece09e061a8d42ca8f2395286a)(struct [rtio\_sqe](structrtio__sqe.md) \*sqe,

569 const struct [rtio\_iodev](structrtio__iodev.md) \*iodev,

570 [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) prio,

571 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*tiny\_write\_data,

572 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) tiny\_write\_len,

573 void \*userdata)

574{

575 \_\_ASSERT\_NO\_MSG(tiny\_write\_len <= sizeof(sqe->[tiny\_tx](structrtio__sqe.md#a19ace9c984538c2022e7f8ecaefa075d).[buf](structrtio__sqe.md#ab71176c084e8b8eb65dfeb3018ae2a49)));

576

577 [memset](string_8h.md#a4137694174d4ca2fad886a1db355015c)(sqe, 0, sizeof(struct [rtio\_sqe](structrtio__sqe.md)));

578 sqe->[op](structrtio__sqe.md#a1d8d3e3426e47a2c7f54d98f51acd953) = [RTIO\_OP\_TINY\_TX](group__rtio.md#ga6f95c0a5fbcc020a0d1102d3b08934bd);

579 sqe->[prio](structrtio__sqe.md#a528eb9b721be7b8a8898ab16a7e2d9a7) = prio;

580 sqe->[iodev](structrtio__sqe.md#a6c784702f011592c84feacd57915bbfc) = iodev;

581 sqe->[tiny\_tx](structrtio__sqe.md#a19ace9c984538c2022e7f8ecaefa075d).[buf\_len](structrtio__sqe.md#a67376f40a13960b152a23da250275722) = tiny\_write\_len;

582 [memcpy](string_8h.md#af0f01bffcd16daa9143f6014d10a25ad)(sqe->[tiny\_tx](structrtio__sqe.md#a19ace9c984538c2022e7f8ecaefa075d).[buf](structrtio__sqe.md#ab71176c084e8b8eb65dfeb3018ae2a49), tiny\_write\_data, tiny\_write\_len);

583 sqe->[userdata](structrtio__sqe.md#a0ed519ee0b5867ff73bdaf37f983c971) = userdata;

584}

585

[ 594](group__rtio.md#ga9d0dd7d0e2e3d281092f2350d6e1713e)static inline void [rtio\_sqe\_prep\_callback](group__rtio.md#ga9d0dd7d0e2e3d281092f2350d6e1713e)(struct [rtio\_sqe](structrtio__sqe.md) \*sqe,

595 [rtio\_callback\_t](group__rtio.md#gad1dbd690e6cf88d7c788436dd04d1a00) callback,

596 void \*arg0,

597 void \*userdata)

598{

599 [memset](string_8h.md#a4137694174d4ca2fad886a1db355015c)(sqe, 0, sizeof(struct [rtio\_sqe](structrtio__sqe.md)));

600 sqe->[op](structrtio__sqe.md#a1d8d3e3426e47a2c7f54d98f51acd953) = [RTIO\_OP\_CALLBACK](group__rtio.md#ga18e0ff7d44e4c33900106aefad0a8508);

601 sqe->[prio](structrtio__sqe.md#a528eb9b721be7b8a8898ab16a7e2d9a7) = 0;

602 sqe->[iodev](structrtio__sqe.md#a6c784702f011592c84feacd57915bbfc) = NULL;

603 sqe->[callback](structrtio__sqe.md#af8c31c33e9fedebe55cac73595d0f696).callback = callback;

604 sqe->[callback](structrtio__sqe.md#af8c31c33e9fedebe55cac73595d0f696).arg0 = arg0;

605 sqe->[userdata](structrtio__sqe.md#a0ed519ee0b5867ff73bdaf37f983c971) = userdata;

606}

607

[ 618](group__rtio.md#gae87be354087d038953dae07c7f9cd3b0)static inline void [rtio\_sqe\_prep\_callback\_no\_cqe](group__rtio.md#gae87be354087d038953dae07c7f9cd3b0)(struct [rtio\_sqe](structrtio__sqe.md) \*sqe,

619 [rtio\_callback\_t](group__rtio.md#gad1dbd690e6cf88d7c788436dd04d1a00) callback,

620 void \*arg0,

621 void \*userdata)

622{

623 [rtio\_sqe\_prep\_callback](group__rtio.md#ga9d0dd7d0e2e3d281092f2350d6e1713e)(sqe, callback, arg0, userdata);

624 sqe->[flags](structrtio__sqe.md#aad2ff8524df0e24b812e77e2393bf5b0) |= [RTIO\_SQE\_NO\_RESPONSE](group__rtio__sqe__flags.md#ga8578ffdb8f53a51b94fa86a6f02d4a11);

625}

626

[ 630](group__rtio.md#gab9b605dcbb01d21c88f9ae70588ea3b5)static inline void [rtio\_sqe\_prep\_transceive](group__rtio.md#gab9b605dcbb01d21c88f9ae70588ea3b5)(struct [rtio\_sqe](structrtio__sqe.md) \*sqe,

631 const struct [rtio\_iodev](structrtio__iodev.md) \*iodev,

632 [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) prio,

633 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*tx\_buf,

634 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*rx\_buf,

635 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) buf\_len,

636 void \*userdata)

637{

638 [memset](string_8h.md#a4137694174d4ca2fad886a1db355015c)(sqe, 0, sizeof(struct [rtio\_sqe](structrtio__sqe.md)));

639 sqe->[op](structrtio__sqe.md#a1d8d3e3426e47a2c7f54d98f51acd953) = [RTIO\_OP\_TXRX](group__rtio.md#ga9f0e70f5a28be65a8ed67c0257a72692);

640 sqe->[prio](structrtio__sqe.md#a528eb9b721be7b8a8898ab16a7e2d9a7) = prio;

641 sqe->[iodev](structrtio__sqe.md#a6c784702f011592c84feacd57915bbfc) = iodev;

642 sqe->[txrx](structrtio__sqe.md#a5f2511eb361a7a4d54a92fae4d391e8c).[buf\_len](structrtio__sqe.md#a67376f40a13960b152a23da250275722) = buf\_len;

643 sqe->[txrx](structrtio__sqe.md#a5f2511eb361a7a4d54a92fae4d391e8c).[tx\_buf](structrtio__sqe.md#a18bfa63542954f4bb8b924c92c48e931) = tx\_buf;

644 sqe->[txrx](structrtio__sqe.md#a5f2511eb361a7a4d54a92fae4d391e8c).[rx\_buf](structrtio__sqe.md#a4d2090fc11b897724a883ad1087d9f73) = rx\_buf;

645 sqe->[userdata](structrtio__sqe.md#a0ed519ee0b5867ff73bdaf37f983c971) = userdata;

646}

647

[ 648](group__rtio.md#gae5fb03fc8f3a4a774f476ff552999bfc)static inline struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \*[rtio\_sqe\_pool\_alloc](group__rtio.md#gae5fb03fc8f3a4a774f476ff552999bfc)(struct [rtio\_sqe\_pool](structrtio__sqe__pool.md) \*pool)

649{

650 struct [mpsc\_node](structmpsc__node.md) \*node = [mpsc\_pop](group__mpsc__lockfree.md#ga823ec37b84ac43e46167aac954bce9d7)(&pool->[free\_q](structrtio__sqe__pool.md#aed49ea25c952e07a8287919268fd2485));

651

652 if (node == NULL) {

653 return NULL;

654 }

655

656 struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \*iodev\_sqe = [CONTAINER\_OF](group__sys-util.md#gac5bc561d1bfd1bf68877fe577779bd2f)(node, struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md), [q](structrtio__iodev__sqe.md#a9cfdd004b65a5e2bc111bc2fb333498c));

657

658 pool->[pool\_free](structrtio__sqe__pool.md#af7990b1510ad2343573f3e4e502475b0)--;

659

660 return iodev\_sqe;

661}

662

[ 663](group__rtio.md#gac776aea3692cfd77aa5bf675a9e9ed02)static inline void [rtio\_sqe\_pool\_free](group__rtio.md#gac776aea3692cfd77aa5bf675a9e9ed02)(struct [rtio\_sqe\_pool](structrtio__sqe__pool.md) \*pool, struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \*iodev\_sqe)

664{

665 [mpsc\_push](group__mpsc__lockfree.md#ga403add133841ef88e10d74141e782b37)(&pool->[free\_q](structrtio__sqe__pool.md#aed49ea25c952e07a8287919268fd2485), &iodev\_sqe->[q](structrtio__iodev__sqe.md#a9cfdd004b65a5e2bc111bc2fb333498c));

666

667 pool->[pool\_free](structrtio__sqe__pool.md#af7990b1510ad2343573f3e4e502475b0)++;

668}

669

[ 670](group__rtio.md#ga8497170f55af1d11d717e919f61806f5)static inline struct [rtio\_cqe](structrtio__cqe.md) \*[rtio\_cqe\_pool\_alloc](group__rtio.md#ga8497170f55af1d11d717e919f61806f5)(struct [rtio\_cqe\_pool](structrtio__cqe__pool.md) \*pool)

671{

672 struct [mpsc\_node](structmpsc__node.md) \*node = [mpsc\_pop](group__mpsc__lockfree.md#ga823ec37b84ac43e46167aac954bce9d7)(&pool->[free\_q](structrtio__cqe__pool.md#a13bd7991ff5622c1cb5aa6af014aaab3));

673

674 if (node == NULL) {

675 return NULL;

676 }

677

678 struct [rtio\_cqe](structrtio__cqe.md) \*cqe = [CONTAINER\_OF](group__sys-util.md#gac5bc561d1bfd1bf68877fe577779bd2f)(node, struct [rtio\_cqe](structrtio__cqe.md), [q](structrtio__cqe.md#a27272bca31c170f406799633ec82098d));

679

680 [memset](string_8h.md#a4137694174d4ca2fad886a1db355015c)(cqe, 0, sizeof(struct [rtio\_cqe](structrtio__cqe.md)));

681

682 pool->[pool\_free](structrtio__cqe__pool.md#a4fb501a0ba15e2956113deaf4597d846)--;

683

684 return cqe;

685}

686

[ 687](group__rtio.md#ga23c0c5d4b551858eabe057ecb8a28d12)static inline void [rtio\_cqe\_pool\_free](group__rtio.md#ga23c0c5d4b551858eabe057ecb8a28d12)(struct [rtio\_cqe\_pool](structrtio__cqe__pool.md) \*pool, struct [rtio\_cqe](structrtio__cqe.md) \*cqe)

688{

689 [mpsc\_push](group__mpsc__lockfree.md#ga403add133841ef88e10d74141e782b37)(&pool->[free\_q](structrtio__cqe__pool.md#a13bd7991ff5622c1cb5aa6af014aaab3), &cqe->[q](structrtio__cqe.md#a27272bca31c170f406799633ec82098d));

690

691 pool->[pool\_free](structrtio__cqe__pool.md#a4fb501a0ba15e2956113deaf4597d846)++;

692}

693

[ 694](group__rtio.md#ga7f14b99fc1dd0697309e7f71a270f5fb)static inline int [rtio\_block\_pool\_alloc](group__rtio.md#ga7f14b99fc1dd0697309e7f71a270f5fb)(struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2), size\_t min\_sz,

695 size\_t max\_sz, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\*buf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*buf\_len)

696{

697#ifndef CONFIG\_RTIO\_SYS\_MEM\_BLOCKS

698 ARG\_UNUSED([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2));

699 ARG\_UNUSED(min\_sz);

700 ARG\_UNUSED(max\_sz);

701 ARG\_UNUSED(buf);

702 ARG\_UNUSED(buf\_len);

703 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

704#else

705 const [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size = [rtio\_mempool\_block\_size](group__rtio.md#ga4213be028b0a1264daaa0d30c4c2d089)([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2));

706 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) bytes = max\_sz;

707

708 /\* Not every context has a block pool and the block size may return 0 in

709 \* that case

710 \*/

711 if (block\_size == 0) {

712 return -[ENOMEM](group__system__errno.md#ga6a05c923dad0c1208043e9c20a58c8e5);

713 }

714

715 do {

716 size\_t num\_blks = [DIV\_ROUND\_UP](group__sys-util.md#gae664e7492e37d324831caf2321ddda37)(bytes, block\_size);

717 int rc = [sys\_mem\_blocks\_alloc\_contiguous](group__mem__blocks__apis.md#ga72614d0c120f40209837b77d0333bb23)([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->block\_pool, num\_blks, (void \*\*)buf);

718

719 if (rc == 0) {

720 \*buf\_len = num\_blks \* block\_size;

721 return 0;

722 }

723

724 if (bytes <= block\_size) {

725 break;

726 }

727

728 bytes -= block\_size;

729 } while (bytes >= min\_sz);

730

731 return -[ENOMEM](group__system__errno.md#ga6a05c923dad0c1208043e9c20a58c8e5);

732#endif

733}

734

[ 735](group__rtio.md#gafca7732926a9a7c080e3cb16e5f16108)static inline void [rtio\_block\_pool\_free](group__rtio.md#gafca7732926a9a7c080e3cb16e5f16108)(struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2), void \*buf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) buf\_len)

736{

737#ifndef CONFIG\_RTIO\_SYS\_MEM\_BLOCKS

738 ARG\_UNUSED([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2));

739 ARG\_UNUSED(buf);

740 ARG\_UNUSED(buf\_len);

741#else

742 size\_t num\_blks = buf\_len >> [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->block\_pool->info.blk\_sz\_shift;

743

744 [sys\_mem\_blocks\_free\_contiguous](group__mem__blocks__apis.md#ga39e7f8dfe3bda8eabc2372f9a1e87342)([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->block\_pool, buf, num\_blks);

745#endif

746}

747

748/\* Do not try and reformat the macros \*/

749/\* clang-format off \*/

750

[ 758](group__rtio.md#gaae51e2a679d37bc1cfba79961688c406)#define RTIO\_IODEV\_DEFINE(name, iodev\_api, iodev\_data) \

759 STRUCT\_SECTION\_ITERABLE(rtio\_iodev, name) = { \

760 .api = (iodev\_api), \

761 .data = (iodev\_data), \

762 }

763

764#define Z\_RTIO\_SQE\_POOL\_DEFINE(name, sz) \

765 static struct rtio\_iodev\_sqe CONCAT(\_sqe\_pool\_, name)[sz]; \

766 STRUCT\_SECTION\_ITERABLE(rtio\_sqe\_pool, name) = { \

767 .free\_q = MPSC\_INIT((name.free\_q)), \

768 .pool\_size = sz, \

769 .pool\_free = sz, \

770 .pool = CONCAT(\_sqe\_pool\_, name), \

771 }

772

773

774#define Z\_RTIO\_CQE\_POOL\_DEFINE(name, sz) \

775 static struct rtio\_cqe CONCAT(\_cqe\_pool\_, name)[sz]; \

776 STRUCT\_SECTION\_ITERABLE(rtio\_cqe\_pool, name) = { \

777 .free\_q = MPSC\_INIT((name.free\_q)), \

778 .pool\_size = sz, \

779 .pool\_free = sz, \

780 .pool = CONCAT(\_cqe\_pool\_, name), \

781 }

782

[ 792](group__rtio.md#ga2437af5061e078950d4a55211d9a902f)#define RTIO\_BMEM COND\_CODE\_1(CONFIG\_USERSPACE, (K\_APP\_BMEM(rtio\_partition) static), (static))

793

[ 803](group__rtio.md#ga3b569c01b71e126cff852df50e98fd69)#define RTIO\_DMEM COND\_CODE\_1(CONFIG\_USERSPACE, (K\_APP\_DMEM(rtio\_partition) static), (static))

804

805#define Z\_RTIO\_BLOCK\_POOL\_DEFINE(name, blk\_sz, blk\_cnt, blk\_align) \

806 RTIO\_BMEM uint8\_t \_\_aligned(WB\_UP(blk\_align)) \

807 CONCAT(\_block\_pool\_, name)[blk\_cnt\*WB\_UP(blk\_sz)]; \

808 \_SYS\_MEM\_BLOCKS\_DEFINE\_WITH\_EXT\_BUF(name, WB\_UP(blk\_sz), blk\_cnt, \

809 CONCAT(\_block\_pool\_, name), RTIO\_DMEM)

810

811#define Z\_RTIO\_DEFINE(name, \_sqe\_pool, \_cqe\_pool, \_block\_pool) \

812 IF\_ENABLED(CONFIG\_RTIO\_SUBMIT\_SEM, \

813 (static K\_SEM\_DEFINE(CONCAT(\_submit\_sem\_, name), 0, K\_SEM\_MAX\_LIMIT))) \

814 IF\_ENABLED(CONFIG\_RTIO\_CONSUME\_SEM, \

815 (static K\_SEM\_DEFINE(CONCAT(\_consume\_sem\_, name), 0, K\_SEM\_MAX\_LIMIT))) \

816 STRUCT\_SECTION\_ITERABLE(rtio, name) = { \

817 IF\_ENABLED(CONFIG\_RTIO\_SUBMIT\_SEM, (.submit\_sem = &CONCAT(\_submit\_sem\_, name),)) \

818 IF\_ENABLED(CONFIG\_RTIO\_SUBMIT\_SEM, (.submit\_count = 0,)) \

819 IF\_ENABLED(CONFIG\_RTIO\_CONSUME\_SEM, (.consume\_sem = &CONCAT(\_consume\_sem\_, name),))\

820 .cq\_count = ATOMIC\_INIT(0), \

821 .xcqcnt = ATOMIC\_INIT(0), \

822 .sqe\_pool = \_sqe\_pool, \

823 .cqe\_pool = \_cqe\_pool, \

824 IF\_ENABLED(CONFIG\_RTIO\_SYS\_MEM\_BLOCKS, (.block\_pool = \_block\_pool,)) \

825 .sq = MPSC\_INIT((name.sq)), \

826 .cq = MPSC\_INIT((name.cq)), \

827 }

828

[ 836](group__rtio.md#ga338df088eabf3b8f7fefb4ac517b21d4)#define RTIO\_DEFINE(name, sq\_sz, cq\_sz) \

837 Z\_RTIO\_SQE\_POOL\_DEFINE(CONCAT(name, \_sqe\_pool), sq\_sz); \

838 Z\_RTIO\_CQE\_POOL\_DEFINE(CONCAT(name, \_cqe\_pool), cq\_sz); \

839 Z\_RTIO\_DEFINE(name, &CONCAT(name, \_sqe\_pool), \

840 &CONCAT(name, \_cqe\_pool), NULL)

841

842/\* clang-format on \*/

843

[ 854](group__rtio.md#gae4c2a9384a9ae4ed16dff914b1184ca8)#define RTIO\_DEFINE\_WITH\_MEMPOOL(name, sq\_sz, cq\_sz, num\_blks, blk\_size, balign) \

855 Z\_RTIO\_SQE\_POOL\_DEFINE(name##\_sqe\_pool, sq\_sz); \

856 Z\_RTIO\_CQE\_POOL\_DEFINE(name##\_cqe\_pool, cq\_sz); \

857 Z\_RTIO\_BLOCK\_POOL\_DEFINE(name##\_block\_pool, blk\_size, num\_blks, balign); \

858 Z\_RTIO\_DEFINE(name, &name##\_sqe\_pool, &name##\_cqe\_pool, &name##\_block\_pool)

859

860/\* clang-format on \*/

861

[ 869](group__rtio.md#ga1f4fb7bccbaae08a94387e4b11275a78)static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [rtio\_sqe\_acquirable](group__rtio.md#ga1f4fb7bccbaae08a94387e4b11275a78)(struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2))

870{

871 return [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->sqe\_pool->pool\_free;

872}

873

[ 882](group__rtio.md#gaef904eb6a8810d8c3ea537c4d6edbee5)static inline struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \*[rtio\_txn\_next](group__rtio.md#gaef904eb6a8810d8c3ea537c4d6edbee5)(const struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \*iodev\_sqe)

883{

884 if (iodev\_sqe->[sqe](structrtio__iodev__sqe.md#a2bd98599678909c0ddb22f879affa12b).[flags](structrtio__sqe.md#aad2ff8524df0e24b812e77e2393bf5b0) & [RTIO\_SQE\_TRANSACTION](group__rtio__sqe__flags.md#ga07f09cc0c95be6cfdddb23f8acacb1ea)) {

885 return iodev\_sqe->[next](structrtio__iodev__sqe.md#a2afb82e550e614f87db7cd1bf2c3a352);

886 } else {

887 return NULL;

888 }

889}

890

891

[ 900](group__rtio.md#gada1e3abf92a46e376138435debc8baf4)static inline struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \*[rtio\_chain\_next](group__rtio.md#gada1e3abf92a46e376138435debc8baf4)(const struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \*iodev\_sqe)

901{

902 if (iodev\_sqe->[sqe](structrtio__iodev__sqe.md#a2bd98599678909c0ddb22f879affa12b).[flags](structrtio__sqe.md#aad2ff8524df0e24b812e77e2393bf5b0) & [RTIO\_SQE\_CHAINED](group__rtio__sqe__flags.md#gae9191d521d4ab602b53fefb74020d06b)) {

903 return iodev\_sqe->[next](structrtio__iodev__sqe.md#a2afb82e550e614f87db7cd1bf2c3a352);

904 } else {

905 return NULL;

906 }

907}

908

[ 917](group__rtio.md#gae690e3dc0fc40dda57257b2eed432719)static inline struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \*[rtio\_iodev\_sqe\_next](group__rtio.md#gae690e3dc0fc40dda57257b2eed432719)(const struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \*iodev\_sqe)

918{

919 return iodev\_sqe->[next](structrtio__iodev__sqe.md#a2afb82e550e614f87db7cd1bf2c3a352);

920}

921

[ 930](group__rtio.md#ga8b47c954d15a334621def53acceb6799)static inline struct [rtio\_sqe](structrtio__sqe.md) \*[rtio\_sqe\_acquire](group__rtio.md#ga8b47c954d15a334621def53acceb6799)(struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2))

931{

932 struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \*iodev\_sqe = [rtio\_sqe\_pool\_alloc](group__rtio.md#gae5fb03fc8f3a4a774f476ff552999bfc)([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->sqe\_pool);

933

934 if (iodev\_sqe == NULL) {

935 return NULL;

936 }

937

938 [mpsc\_push](group__mpsc__lockfree.md#ga403add133841ef88e10d74141e782b37)(&[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->sq, &iodev\_sqe->[q](structrtio__iodev__sqe.md#a9cfdd004b65a5e2bc111bc2fb333498c));

939

940 return &iodev\_sqe->[sqe](structrtio__iodev__sqe.md#a2bd98599678909c0ddb22f879affa12b);

941}

942

[ 948](group__rtio.md#ga9486fb7b50e8d2409a50da235203536b)static inline void [rtio\_sqe\_drop\_all](group__rtio.md#ga9486fb7b50e8d2409a50da235203536b)(struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2))

949{

950 struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \*iodev\_sqe;

951 struct [mpsc\_node](structmpsc__node.md) \*node = [mpsc\_pop](group__mpsc__lockfree.md#ga823ec37b84ac43e46167aac954bce9d7)(&[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->sq);

952

953 while (node != NULL) {

954 iodev\_sqe = [CONTAINER\_OF](group__sys-util.md#gac5bc561d1bfd1bf68877fe577779bd2f)(node, struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md), q);

955 [rtio\_sqe\_pool\_free](group__rtio.md#gac776aea3692cfd77aa5bf675a9e9ed02)([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->sqe\_pool, iodev\_sqe);

956 node = [mpsc\_pop](group__mpsc__lockfree.md#ga823ec37b84ac43e46167aac954bce9d7)(&[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->sq);

957 }

958}

959

[ 963](group__rtio.md#gad848646651fdf3649b882e5268f72a3c)static inline struct [rtio\_cqe](structrtio__cqe.md) \*[rtio\_cqe\_acquire](group__rtio.md#gad848646651fdf3649b882e5268f72a3c)(struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2))

964{

965 struct [rtio\_cqe](structrtio__cqe.md) \*cqe = [rtio\_cqe\_pool\_alloc](group__rtio.md#ga8497170f55af1d11d717e919f61806f5)([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->cqe\_pool);

966

967 if (cqe == NULL) {

968 return NULL;

969 }

970

971 [memset](string_8h.md#a4137694174d4ca2fad886a1db355015c)(cqe, 0, sizeof(struct [rtio\_cqe](structrtio__cqe.md)));

972

973 return cqe;

974}

975

[ 979](group__rtio.md#ga6f55202adeca60aed0343a7a0dcab071)static inline void [rtio\_cqe\_produce](group__rtio.md#ga6f55202adeca60aed0343a7a0dcab071)(struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2), struct [rtio\_cqe](structrtio__cqe.md) \*cqe)

980{

981 [mpsc\_push](group__mpsc__lockfree.md#ga403add133841ef88e10d74141e782b37)(&[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->cq, &cqe->[q](structrtio__cqe.md#a27272bca31c170f406799633ec82098d));

982}

983

[ 995](group__rtio.md#gae562cf241911804cdb9f4e3a73b53df4)static inline struct [rtio\_cqe](structrtio__cqe.md) \*[rtio\_cqe\_consume](group__rtio.md#gae562cf241911804cdb9f4e3a73b53df4)(struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2))

996{

997 struct [mpsc\_node](structmpsc__node.md) \*node;

998 struct [rtio\_cqe](structrtio__cqe.md) \*cqe = NULL;

999

1000#ifdef CONFIG\_RTIO\_CONSUME\_SEM

1001 if ([k\_sem\_take](group__semaphore__apis.md#gac71e2383c1920dddc45a561cacfef090)([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->consume\_sem, [K\_NO\_WAIT](group__clock__apis.md#ga3d9541cfe2e8395af66d186efa77362f)) != 0) {

1002 return NULL;

1003 }

1004#endif

1005

1006 node = [mpsc\_pop](group__mpsc__lockfree.md#ga823ec37b84ac43e46167aac954bce9d7)(&[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->cq);

1007 if (node == NULL) {

1008 return NULL;

1009 }

1010 cqe = [CONTAINER\_OF](group__sys-util.md#gac5bc561d1bfd1bf68877fe577779bd2f)(node, struct [rtio\_cqe](structrtio__cqe.md), [q](structrtio__cqe.md#a27272bca31c170f406799633ec82098d));

1011

1012 return cqe;

1013}

1014

[ 1025](group__rtio.md#gaf617d05d9b59ce1f1d0697617ef6f249)static inline struct [rtio\_cqe](structrtio__cqe.md) \*[rtio\_cqe\_consume\_block](group__rtio.md#gaf617d05d9b59ce1f1d0697617ef6f249)(struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2))

1026{

1027 struct [mpsc\_node](structmpsc__node.md) \*node;

1028 struct [rtio\_cqe](structrtio__cqe.md) \*cqe;

1029

1030#ifdef CONFIG\_RTIO\_CONSUME\_SEM

1031 [k\_sem\_take](group__semaphore__apis.md#gac71e2383c1920dddc45a561cacfef090)([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->consume\_sem, [K\_FOREVER](group__clock__apis.md#ga0bb4b83f0222193b21a8910311bab0ca));

1032#endif

1033 node = [mpsc\_pop](group__mpsc__lockfree.md#ga823ec37b84ac43e46167aac954bce9d7)(&[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->cq);

1034 while (node == NULL) {

1035 Z\_SPIN\_DELAY(1);

1036 node = [mpsc\_pop](group__mpsc__lockfree.md#ga823ec37b84ac43e46167aac954bce9d7)(&[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->cq);

1037 }

1038 cqe = [CONTAINER\_OF](group__sys-util.md#gac5bc561d1bfd1bf68877fe577779bd2f)(node, struct [rtio\_cqe](structrtio__cqe.md), [q](structrtio__cqe.md#a27272bca31c170f406799633ec82098d));

1039

1040 return cqe;

1041}

1042

[ 1049](group__rtio.md#gaa0799a5f8ad98425d385a07c5d27d9cb)static inline void [rtio\_cqe\_release](group__rtio.md#gaa0799a5f8ad98425d385a07c5d27d9cb)(struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2), struct [rtio\_cqe](structrtio__cqe.md) \*cqe)

1050{

1051 [rtio\_cqe\_pool\_free](group__rtio.md#ga23c0c5d4b551858eabe057ecb8a28d12)([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->cqe\_pool, cqe);

1052}

1053

[ 1060](group__rtio.md#ga75661c8c6c94a0ac6254cec674b478c8)static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [rtio\_cqe\_compute\_flags](group__rtio.md#ga75661c8c6c94a0ac6254cec674b478c8)(struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \*iodev\_sqe)

1061{

1062 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) = 0;

1063

1064#ifdef CONFIG\_RTIO\_SYS\_MEM\_BLOCKS

1065 if (iodev\_sqe->[sqe](structrtio__iodev__sqe.md#a2bd98599678909c0ddb22f879affa12b).[op](structrtio__sqe.md#a1d8d3e3426e47a2c7f54d98f51acd953) == [RTIO\_OP\_RX](group__rtio.md#gafeb05c351207cd1638fa78f6607e1a4a) && iodev\_sqe->[sqe](structrtio__iodev__sqe.md#a2bd98599678909c0ddb22f879affa12b).[flags](structrtio__sqe.md#aad2ff8524df0e24b812e77e2393bf5b0) & [RTIO\_SQE\_MEMPOOL\_BUFFER](group__rtio__sqe__flags.md#ga2802b46584220afffa0e959e149d5a4d)) {

1066 struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) = iodev\_sqe->[r](structrtio__iodev__sqe.md#a3c3a050793589258eab5ff5ac30f24c8);

1067 struct sys\_mem\_blocks \*mem\_pool = [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->block\_pool;

1068 int blk\_index = (iodev\_sqe->[sqe](structrtio__iodev__sqe.md#a2bd98599678909c0ddb22f879affa12b).[rx](structrtio__sqe.md#a37a98afc43f26355c70e7036725b2544).[buf](structrtio__sqe.md#ab71176c084e8b8eb65dfeb3018ae2a49) - mem\_pool->buffer) >>

1069 mem\_pool->info.blk\_sz\_shift;

1070 int blk\_count = iodev\_sqe->[sqe](structrtio__iodev__sqe.md#a2bd98599678909c0ddb22f879affa12b).[rx](structrtio__sqe.md#a37a98afc43f26355c70e7036725b2544).[buf\_len](structrtio__sqe.md#a67376f40a13960b152a23da250275722) >> mem\_pool->info.blk\_sz\_shift;

1071

1072 [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) = [RTIO\_CQE\_FLAG\_PREP\_MEMPOOL](group__rtio__cqe__flags.md#ga28b3a5661248b6b3763aab47417114d6)(blk\_index, blk\_count);

1073 }

1074#else

1075 ARG\_UNUSED(iodev\_sqe);

1076#endif

1077

1078 return [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9);

1079}

1080

[ 1096](group__rtio.md#gaedbf9386a36ed99baa290ef6c318ded1)\_\_syscall int [rtio\_cqe\_get\_mempool\_buffer](group__rtio.md#gaedbf9386a36ed99baa290ef6c318ded1)(const struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2), struct [rtio\_cqe](structrtio__cqe.md) \*cqe,

1097 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\*buff, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*buff\_len);

1098

1099static inline int z\_impl\_rtio\_cqe\_get\_mempool\_buffer(const struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2), struct [rtio\_cqe](structrtio__cqe.md) \*cqe,

1100 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\*buff, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*buff\_len)

1101{

1102#ifdef CONFIG\_RTIO\_SYS\_MEM\_BLOCKS

1103 if ([RTIO\_CQE\_FLAG\_GET](group__rtio__cqe__flags.md#gaef64ea020a20ac22a0edcb6eca032efc)(cqe->[flags](structrtio__cqe.md#a8a7632ef1cfd31529d782bd761908d93)) == [RTIO\_CQE\_FLAG\_MEMPOOL\_BUFFER](group__rtio__cqe__flags.md#ga0f212500447a5e37e225a6997953b609)) {

1104 int blk\_idx = [RTIO\_CQE\_FLAG\_MEMPOOL\_GET\_BLK\_IDX](group__rtio__cqe__flags.md#ga0b5f3f7e7be472ecf87bd2b08c1888da)(cqe->[flags](structrtio__cqe.md#a8a7632ef1cfd31529d782bd761908d93));

1105 int blk\_count = [RTIO\_CQE\_FLAG\_MEMPOOL\_GET\_BLK\_CNT](group__rtio__cqe__flags.md#ga087465f866d417d5332602bb582cc1a7)(cqe->[flags](structrtio__cqe.md#a8a7632ef1cfd31529d782bd761908d93));

1106 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) blk\_size = [rtio\_mempool\_block\_size](group__rtio.md#ga4213be028b0a1264daaa0d30c4c2d089)([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2));

1107

1108 \*buff = [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->block\_pool->buffer + blk\_idx \* blk\_size;

1109 \*buff\_len = blk\_count \* blk\_size;

1110 \_\_ASSERT\_NO\_MSG(\*buff >= [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->block\_pool->buffer);

1111 \_\_ASSERT\_NO\_MSG(\*buff <

1112 [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->block\_pool->buffer + blk\_size \* [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->block\_pool->info.num\_blocks);

1113 return 0;

1114 }

1115 return -[EINVAL](group__system__errno.md#ga2d1678d5a7cc8ce499643f3b8957def4);

1116#else

1117 ARG\_UNUSED([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2));

1118 ARG\_UNUSED(cqe);

1119 ARG\_UNUSED(buff);

1120 ARG\_UNUSED(buff\_len);

1121

1122 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

1123#endif

1124}

1125

[ 1126](group__rtio.md#gaf191153e83de72ddefb998daad02fa16)void [rtio\_executor\_submit](group__rtio.md#gaf191153e83de72ddefb998daad02fa16)(struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2));

[ 1127](group__rtio.md#ga7e2ebd9abaf585207bc5b99c5d815c6a)void [rtio\_executor\_ok](group__rtio.md#ga7e2ebd9abaf585207bc5b99c5d815c6a)(struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \*iodev\_sqe, int result);

[ 1128](group__rtio.md#ga15f4a1a4dfb869ef9e4216dc1c1cdc8a)void [rtio\_executor\_err](group__rtio.md#ga15f4a1a4dfb869ef9e4216dc1c1cdc8a)(struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \*iodev\_sqe, int result);

1129

[ 1138](group__rtio.md#gacb1d2ffa2b07418d8a8aa319bd4336ab)static inline void [rtio\_iodev\_sqe\_ok](group__rtio.md#gacb1d2ffa2b07418d8a8aa319bd4336ab)(struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \*iodev\_sqe, int result)

1139{

1140 [rtio\_executor\_ok](group__rtio.md#ga7e2ebd9abaf585207bc5b99c5d815c6a)(iodev\_sqe, result);

1141}

1142

[ 1151](group__rtio.md#gaada07aa6acefa548743b525225fa482f)static inline void [rtio\_iodev\_sqe\_err](group__rtio.md#gaada07aa6acefa548743b525225fa482f)(struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \*iodev\_sqe, int result)

1152{

1153 [rtio\_executor\_err](group__rtio.md#ga15f4a1a4dfb869ef9e4216dc1c1cdc8a)(iodev\_sqe, result);

1154}

1155

[ 1167](group__rtio.md#ga4abc221d5a90ab882000a72caa0ebd0f)static inline void [rtio\_cqe\_submit](group__rtio.md#ga4abc221d5a90ab882000a72caa0ebd0f)(struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2), int result, void \*userdata, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9))

1168{

1169 struct [rtio\_cqe](structrtio__cqe.md) \*cqe = [rtio\_cqe\_acquire](group__rtio.md#gad848646651fdf3649b882e5268f72a3c)([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2));

1170

1171 if (cqe == NULL) {

1172 [atomic\_inc](group__atomic__apis.md#gaae47a9cbe5a6534967b417f602b37ac2)(&[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->xcqcnt);

1173 } else {

1174 cqe->[result](structrtio__cqe.md#acbe2e6607a752b676d9336b9ca6ce435) = [result](structrtio__cqe.md#acbe2e6607a752b676d9336b9ca6ce435);

1175 cqe->[userdata](structrtio__cqe.md#a15128387ccbea55812ef229eab7241e7) = [userdata](structrtio__cqe.md#a15128387ccbea55812ef229eab7241e7);

1176 cqe->[flags](structrtio__cqe.md#a8a7632ef1cfd31529d782bd761908d93) = [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9);

1177 [rtio\_cqe\_produce](group__rtio.md#ga6f55202adeca60aed0343a7a0dcab071)([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2), cqe);

1178 }

1179

1180 [atomic\_inc](group__atomic__apis.md#gaae47a9cbe5a6534967b417f602b37ac2)(&[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->cq\_count);

1181#ifdef CONFIG\_RTIO\_SUBMIT\_SEM

1182 if ([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->submit\_count > 0) {

1183 [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->submit\_count--;

1184 if ([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->submit\_count == 0) {

1185 [k\_sem\_give](group__semaphore__apis.md#gab9be3cf1988af2cd6afdace52d497c84)([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->submit\_sem);

1186 }

1187 }

1188#endif

1189#ifdef CONFIG\_RTIO\_CONSUME\_SEM

1190 [k\_sem\_give](group__semaphore__apis.md#gab9be3cf1988af2cd6afdace52d497c84)([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->consume\_sem);

1191#endif

1192}

1193

1194#define \_\_RTIO\_MEMPOOL\_GET\_NUM\_BLKS(num\_bytes, blk\_size) (((num\_bytes) + (blk\_size)-1) / (blk\_size))

1195

[ 1208](group__rtio.md#gaab6843e2038d00a8354f57d7e2ffcf7e)static inline int [rtio\_sqe\_rx\_buf](group__rtio.md#gaab6843e2038d00a8354f57d7e2ffcf7e)(const struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \*iodev\_sqe, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) min\_buf\_len,

1209 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) max\_buf\_len, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\*buf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*buf\_len)

1210{

1211 struct [rtio\_sqe](structrtio__sqe.md) \*sqe = (struct [rtio\_sqe](structrtio__sqe.md) \*)&iodev\_sqe->[sqe](structrtio__iodev__sqe.md#a2bd98599678909c0ddb22f879affa12b);

1212

1213#ifdef CONFIG\_RTIO\_SYS\_MEM\_BLOCKS

1214 if (sqe->[op](structrtio__sqe.md#a1d8d3e3426e47a2c7f54d98f51acd953) == [RTIO\_OP\_RX](group__rtio.md#gafeb05c351207cd1638fa78f6607e1a4a) && sqe->[flags](structrtio__sqe.md#aad2ff8524df0e24b812e77e2393bf5b0) & [RTIO\_SQE\_MEMPOOL\_BUFFER](group__rtio__sqe__flags.md#ga2802b46584220afffa0e959e149d5a4d)) {

1215 struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) = iodev\_sqe->[r](structrtio__iodev__sqe.md#a3c3a050793589258eab5ff5ac30f24c8);

1216

1217 if (sqe->[rx](structrtio__sqe.md#a37a98afc43f26355c70e7036725b2544).[buf](structrtio__sqe.md#ab71176c084e8b8eb65dfeb3018ae2a49) != NULL) {

1218 if (sqe->[rx](structrtio__sqe.md#a37a98afc43f26355c70e7036725b2544).[buf\_len](structrtio__sqe.md#a67376f40a13960b152a23da250275722) < min\_buf\_len) {

1219 return -[ENOMEM](group__system__errno.md#ga6a05c923dad0c1208043e9c20a58c8e5);

1220 }

1221 \*buf = sqe->[rx](structrtio__sqe.md#a37a98afc43f26355c70e7036725b2544).[buf](structrtio__sqe.md#ab71176c084e8b8eb65dfeb3018ae2a49);

1222 \*buf\_len = sqe->[rx](structrtio__sqe.md#a37a98afc43f26355c70e7036725b2544).[buf\_len](structrtio__sqe.md#a67376f40a13960b152a23da250275722);

1223 return 0;

1224 }

1225

1226 int rc = [rtio\_block\_pool\_alloc](group__rtio.md#ga7f14b99fc1dd0697309e7f71a270f5fb)([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2), min\_buf\_len, max\_buf\_len, buf, buf\_len);

1227 if (rc == 0) {

1228 sqe->[rx](structrtio__sqe.md#a37a98afc43f26355c70e7036725b2544).[buf](structrtio__sqe.md#ab71176c084e8b8eb65dfeb3018ae2a49) = \*buf;

1229 sqe->[rx](structrtio__sqe.md#a37a98afc43f26355c70e7036725b2544).[buf\_len](structrtio__sqe.md#a67376f40a13960b152a23da250275722) = \*buf\_len;

1230 return 0;

1231 }

1232

1233 return -[ENOMEM](group__system__errno.md#ga6a05c923dad0c1208043e9c20a58c8e5);

1234 }

1235#else

1236 ARG\_UNUSED(max\_buf\_len);

1237#endif

1238

1239 if (sqe->[rx](structrtio__sqe.md#a37a98afc43f26355c70e7036725b2544).[buf\_len](structrtio__sqe.md#a67376f40a13960b152a23da250275722) < min\_buf\_len) {

1240 return -[ENOMEM](group__system__errno.md#ga6a05c923dad0c1208043e9c20a58c8e5);

1241 }

1242

1243 \*buf = sqe->[rx](structrtio__sqe.md#a37a98afc43f26355c70e7036725b2544).[buf](structrtio__sqe.md#ab71176c084e8b8eb65dfeb3018ae2a49);

1244 \*buf\_len = sqe->[rx](structrtio__sqe.md#a37a98afc43f26355c70e7036725b2544).[buf\_len](structrtio__sqe.md#a67376f40a13960b152a23da250275722);

1245 return 0;

1246}

1247

[ 1262](group__rtio.md#ga6530bf56ccbab046a362a6448f941609)\_\_syscall void [rtio\_release\_buffer](group__rtio.md#ga6530bf56ccbab046a362a6448f941609)(struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2), void \*buff, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) buff\_len);

1263

1264static inline void z\_impl\_rtio\_release\_buffer(struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2), void \*buff, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) buff\_len)

1265{

1266#ifdef CONFIG\_RTIO\_SYS\_MEM\_BLOCKS

1267 if ([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) == NULL || buff == NULL || [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->block\_pool == NULL || buff\_len == 0) {

1268 return;

1269 }

1270

1271 [rtio\_block\_pool\_free](group__rtio.md#gafca7732926a9a7c080e3cb16e5f16108)([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2), buff, buff\_len);

1272#else

1273 ARG\_UNUSED([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2));

1274 ARG\_UNUSED(buff);

1275 ARG\_UNUSED(buff\_len);

1276#endif

1277}

1278

[ 1282](group__rtio.md#ga9da42c98546930575525f0f92710f9e4)static inline void [rtio\_access\_grant](group__rtio.md#ga9da42c98546930575525f0f92710f9e4)(struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2), struct [k\_thread](structk__thread.md) \*t)

1283{

1284 [k\_object\_access\_grant](group__usermode__apis.md#ga94087bedf96fe2a2bea437d3d585ca22)([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2), t);

1285

1286#ifdef CONFIG\_RTIO\_SUBMIT\_SEM

1287 [k\_object\_access\_grant](group__usermode__apis.md#ga94087bedf96fe2a2bea437d3d585ca22)([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->submit\_sem, t);

1288#endif

1289

1290#ifdef CONFIG\_RTIO\_CONSUME\_SEM

1291 [k\_object\_access\_grant](group__usermode__apis.md#ga94087bedf96fe2a2bea437d3d585ca22)([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->consume\_sem, t);

1292#endif

1293}

1294

[ 1305](group__rtio.md#gac01252e55d2848b38c0ed77b71d600a7)\_\_syscall int [rtio\_sqe\_cancel](group__rtio.md#gac01252e55d2848b38c0ed77b71d600a7)(struct [rtio\_sqe](structrtio__sqe.md) \*sqe);

1306

1307static inline int z\_impl\_rtio\_sqe\_cancel(struct [rtio\_sqe](structrtio__sqe.md) \*sqe)

1308{

1309 struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \*iodev\_sqe = [CONTAINER\_OF](group__sys-util.md#gac5bc561d1bfd1bf68877fe577779bd2f)([sqe](structrtio__iodev__sqe.md#a2bd98599678909c0ddb22f879affa12b), struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md), [sqe](structrtio__iodev__sqe.md#a2bd98599678909c0ddb22f879affa12b));

1310

1311 do {

1312 iodev\_sqe->[sqe](structrtio__iodev__sqe.md#a2bd98599678909c0ddb22f879affa12b).[flags](structrtio__sqe.md#aad2ff8524df0e24b812e77e2393bf5b0) |= [RTIO\_SQE\_CANCELED](group__rtio__sqe__flags.md#ga7f7f9b038ab8409f271b1aebc1b95ee6);

1313 iodev\_sqe = [rtio\_iodev\_sqe\_next](group__rtio.md#gae690e3dc0fc40dda57257b2eed432719)(iodev\_sqe);

1314 } while (iodev\_sqe != NULL);

1315

1316 return 0;

1317}

1318

[ 1334](group__rtio.md#ga830863e6c8d9b96f4c473a038cab8f8c)\_\_syscall int [rtio\_sqe\_copy\_in\_get\_handles](group__rtio.md#ga830863e6c8d9b96f4c473a038cab8f8c)(struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2), const struct [rtio\_sqe](structrtio__sqe.md) \*sqes,

1335 struct [rtio\_sqe](structrtio__sqe.md) \*\*handle, size\_t sqe\_count);

1336

1337static inline int z\_impl\_rtio\_sqe\_copy\_in\_get\_handles(struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2), const struct [rtio\_sqe](structrtio__sqe.md) \*sqes,

1338 struct [rtio\_sqe](structrtio__sqe.md) \*\*handle,

1339 size\_t sqe\_count)

1340{

1341 struct [rtio\_sqe](structrtio__sqe.md) \*sqe;

1342 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) acquirable = [rtio\_sqe\_acquirable](group__rtio.md#ga1f4fb7bccbaae08a94387e4b11275a78)([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2));

1343

1344 if (acquirable < sqe\_count) {

1345 return -[ENOMEM](group__system__errno.md#ga6a05c923dad0c1208043e9c20a58c8e5);

1346 }

1347

1348 for (unsigned long i = 0; i < sqe\_count; i++) {

1349 sqe = [rtio\_sqe\_acquire](group__rtio.md#ga8b47c954d15a334621def53acceb6799)([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2));

1350 \_\_ASSERT\_NO\_MSG(sqe != NULL);

1351 if (handle != NULL && i == 0) {

1352 \*handle = sqe;

1353 }

1354 \*sqe = sqes[i];

1355 }

1356

1357 return 0;

1358}

1359

[ 1376](group__rtio.md#ga65e351af0a16dcf504a51ef4eb9316c7)static inline int [rtio\_sqe\_copy\_in](group__rtio.md#ga65e351af0a16dcf504a51ef4eb9316c7)(struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2), const struct [rtio\_sqe](structrtio__sqe.md) \*sqes, size\_t sqe\_count)

1377{

1378 return [rtio\_sqe\_copy\_in\_get\_handles](group__rtio.md#ga830863e6c8d9b96f4c473a038cab8f8c)([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2), sqes, NULL, sqe\_count);

1379}

1380

[ 1396](group__rtio.md#ga98b2bbef95aea342a9b86a9775dd5c3b)\_\_syscall int [rtio\_cqe\_copy\_out](group__rtio.md#ga98b2bbef95aea342a9b86a9775dd5c3b)(struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2),

1397 struct [rtio\_cqe](structrtio__cqe.md) \*cqes,

1398 size\_t cqe\_count,

1399 [k\_timeout\_t](structk__timeout__t.md) timeout);

1400static inline int z\_impl\_rtio\_cqe\_copy\_out(struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2),

1401 struct [rtio\_cqe](structrtio__cqe.md) \*cqes,

1402 size\_t cqe\_count,

1403 [k\_timeout\_t](structk__timeout__t.md) timeout)

1404{

1405 size\_t copied = 0;

1406 struct [rtio\_cqe](structrtio__cqe.md) \*cqe;

1407 [k\_timepoint\_t](structk__timepoint__t.md) end = [sys\_timepoint\_calc](group__clock__apis.md#ga509cf4599c1f162c97540743e8c21d33)(timeout);

1408

1409 do {

1410 cqe = [K\_TIMEOUT\_EQ](group__clock__apis.md#ga9abf00b34e16ab7ad0883603b6778b1b)(timeout, [K\_FOREVER](group__clock__apis.md#ga0bb4b83f0222193b21a8910311bab0ca)) ? [rtio\_cqe\_consume\_block](group__rtio.md#gaf617d05d9b59ce1f1d0697617ef6f249)([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2))

1411 : [rtio\_cqe\_consume](group__rtio.md#gae562cf241911804cdb9f4e3a73b53df4)([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2));

1412 if (cqe == NULL) {

1413 Z\_SPIN\_DELAY(25);

1414 continue;

1415 }

1416 cqes[copied++] = \*cqe;

1417 [rtio\_cqe\_release](group__rtio.md#gaa0799a5f8ad98425d385a07c5d27d9cb)([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2), cqe);

1418 } while (copied < cqe\_count && ![sys\_timepoint\_expired](group__clock__apis.md#ga87d0d7a0f7bcdcc8c4909962eac12985)(end));

1419

1420 return copied;

1421}

1422

[ 1436](group__rtio.md#gafee27c64a4a4989c4eb774addde8eb2e)\_\_syscall int [rtio\_submit](group__rtio.md#gafee27c64a4a4989c4eb774addde8eb2e)(struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2), [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) wait\_count);

1437

1438static inline int z\_impl\_rtio\_submit(struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2), [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) wait\_count)

1439{

1440 int res = 0;

1441

1442#ifdef CONFIG\_RTIO\_SUBMIT\_SEM

1443 /\* TODO undefined behavior if another thread calls submit of course

1444 \*/

1445 if (wait\_count > 0) {

1446 \_\_ASSERT(![k\_is\_in\_isr](group__isr__apis.md#ga8482b0dd2283d12677a9ebe321667d16)(),

1447 "expected rtio submit with wait count to be called from a thread");

1448

1449 [k\_sem\_reset](group__semaphore__apis.md#ga1bd12d8d8c1b9c6be9b665d0fefe5562)([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->submit\_sem);

1450 [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->submit\_count = wait\_count;

1451 }

1452#else

1453 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) cq\_count = ([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808))[atomic\_get](group__atomic__apis.md#ga33bb426a17535bd1022895a7e44b32fa)(&[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->cq\_count) + wait\_count;

1454#endif

1455

1456 /\* Submit the queue to the executor which consumes submissions

1457 \* and produces completions through ISR chains or other means.

1458 \*/

1459 [rtio\_executor\_submit](group__rtio.md#gaf191153e83de72ddefb998daad02fa16)([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2));

1460

1461

1462 /\* TODO could be nicer if we could suspend the thread and not

1463 \* wake up on each completion here.

1464 \*/

1465#ifdef CONFIG\_RTIO\_SUBMIT\_SEM

1466

1467 if (wait\_count > 0) {

1468 res = [k\_sem\_take](group__semaphore__apis.md#gac71e2383c1920dddc45a561cacfef090)([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->submit\_sem, [K\_FOREVER](group__clock__apis.md#ga0bb4b83f0222193b21a8910311bab0ca));

1469 \_\_ASSERT(res == 0,

1470 "semaphore was reset or timed out while waiting on completions!");

1471 }

1472#else

1473 while (([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808))[atomic\_get](group__atomic__apis.md#ga33bb426a17535bd1022895a7e44b32fa)(&[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->cq\_count) < cq\_count) {

1474 Z\_SPIN\_DELAY(10);

1475 [k\_yield](group__thread__apis.md#ga08a3484c33444ecedc2d71d78495a295)();

1476 }

1477#endif

1478

1479 return res;

1480}

1481

1485

1486#ifdef \_\_cplusplus

1487}

1488#endif

1489

1490#include <zephyr/syscalls/rtio.h>

1491

1492#endif /\* ZEPHYR\_INCLUDE\_RTIO\_RTIO\_H\_ \*/

[\_\_assert.h](____assert_8h.md)

[app\_memdomain.h](app__memdomain_8h.md)

[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)

workaround assembler barfing for ST r

**Definition** asm-macro-32-bit-gnu.h:24

[atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8)

long atomic\_t

**Definition** atomic\_types.h:15

[device.h](device_8h.md)

[atomic\_get](group__atomic__apis.md#ga33bb426a17535bd1022895a7e44b32fa)

atomic\_val\_t atomic\_get(const atomic\_t \*target)

Atomic get.

[atomic\_inc](group__atomic__apis.md#gaae47a9cbe5a6534967b417f602b37ac2)

atomic\_val\_t atomic\_inc(atomic\_t \*target)

Atomic increment.

[K\_FOREVER](group__clock__apis.md#ga0bb4b83f0222193b21a8910311bab0ca)

#define K\_FOREVER

Generate infinite timeout delay.

**Definition** kernel.h:1440

[K\_NO\_WAIT](group__clock__apis.md#ga3d9541cfe2e8395af66d186efa77362f)

#define K\_NO\_WAIT

Generate null timeout delay.

**Definition** kernel.h:1330

[sys\_timepoint\_calc](group__clock__apis.md#ga509cf4599c1f162c97540743e8c21d33)

k\_timepoint\_t sys\_timepoint\_calc(k\_timeout\_t timeout)

Calculate a timepoint value.

[sys\_timepoint\_expired](group__clock__apis.md#ga87d0d7a0f7bcdcc8c4909962eac12985)

static bool sys\_timepoint\_expired(k\_timepoint\_t timepoint)

Indicates if timepoint is expired.

**Definition** sys\_clock.h:312

[K\_TIMEOUT\_EQ](group__clock__apis.md#ga9abf00b34e16ab7ad0883603b6778b1b)

#define K\_TIMEOUT\_EQ(a, b)

Compare timeouts for equality.

**Definition** sys\_clock.h:80

[k\_is\_in\_isr](group__isr__apis.md#ga8482b0dd2283d12677a9ebe321667d16)

bool k\_is\_in\_isr(void)

Determine if code is running at interrupt level.

[sys\_mem\_blocks\_free\_contiguous](group__mem__blocks__apis.md#ga39e7f8dfe3bda8eabc2372f9a1e87342)

int sys\_mem\_blocks\_free\_contiguous(sys\_mem\_blocks\_t \*mem\_block, void \*block, size\_t count)

Free contiguous multiple memory blocks.

[sys\_mem\_blocks\_alloc\_contiguous](group__mem__blocks__apis.md#ga72614d0c120f40209837b77d0333bb23)

int sys\_mem\_blocks\_alloc\_contiguous(sys\_mem\_blocks\_t \*mem\_block, size\_t count, void \*\*out\_block)

Allocate a contiguous set of memory blocks.

[mpsc\_push](group__mpsc__lockfree.md#ga403add133841ef88e10d74141e782b37)

static ALWAYS\_INLINE void mpsc\_push(struct mpsc \*q, struct mpsc\_node \*n)

Push a node.

**Definition** mpsc\_lockfree.h:126

[mpsc\_pop](group__mpsc__lockfree.md#ga823ec37b84ac43e46167aac954bce9d7)

static struct mpsc\_node \* mpsc\_pop(struct mpsc \*q)

Pop a node off of the list.

**Definition** mpsc\_lockfree.h:145

[RTIO\_CQE\_FLAG\_MEMPOOL\_GET\_BLK\_CNT](group__rtio__cqe__flags.md#ga087465f866d417d5332602bb582cc1a7)

#define RTIO\_CQE\_FLAG\_MEMPOOL\_GET\_BLK\_CNT(flags)

Get the block count of a mempool flags.

**Definition** rtio.h:178

[RTIO\_CQE\_FLAG\_MEMPOOL\_GET\_BLK\_IDX](group__rtio__cqe__flags.md#ga0b5f3f7e7be472ecf87bd2b08c1888da)

#define RTIO\_CQE\_FLAG\_MEMPOOL\_GET\_BLK\_IDX(flags)

Get the block index of a mempool flags.

**Definition** rtio.h:170

[RTIO\_CQE\_FLAG\_MEMPOOL\_BUFFER](group__rtio__cqe__flags.md#ga0f212500447a5e37e225a6997953b609)

#define RTIO\_CQE\_FLAG\_MEMPOOL\_BUFFER

The entry's buffer was allocated from the RTIO's mempool.

**Definition** rtio.h:160

[RTIO\_CQE\_FLAG\_PREP\_MEMPOOL](group__rtio__cqe__flags.md#ga28b3a5661248b6b3763aab47417114d6)

#define RTIO\_CQE\_FLAG\_PREP\_MEMPOOL(blk\_idx, blk\_cnt)

Prepare CQE flags for a mempool read.

**Definition** rtio.h:187

[RTIO\_CQE\_FLAG\_GET](group__rtio__cqe__flags.md#gaef64ea020a20ac22a0edcb6eca032efc)

#define RTIO\_CQE\_FLAG\_GET(flags)

**Definition** rtio.h:162

[RTIO\_SQE\_MULTISHOT](group__rtio__sqe__flags.md#ga00f8ead8f043fe40d49d0bc3325fb299)

#define RTIO\_SQE\_MULTISHOT

The SQE should continue producing CQEs until canceled.

**Definition** rtio.h:136

[RTIO\_SQE\_TRANSACTION](group__rtio__sqe__flags.md#ga07f09cc0c95be6cfdddb23f8acacb1ea)

#define RTIO\_SQE\_TRANSACTION

The next request in the queue is part of a transaction.

**Definition** rtio.h:108

[RTIO\_SQE\_MEMPOOL\_BUFFER](group__rtio__sqe__flags.md#ga2802b46584220afffa0e959e149d5a4d)

#define RTIO\_SQE\_MEMPOOL\_BUFFER

The buffer should be allocated by the RTIO mempool.

**Definition** rtio.h:120

[RTIO\_SQE\_CANCELED](group__rtio__sqe__flags.md#ga7f7f9b038ab8409f271b1aebc1b95ee6)

#define RTIO\_SQE\_CANCELED

The SQE should not execute if possible.

**Definition** rtio.h:128

[RTIO\_SQE\_NO\_RESPONSE](group__rtio__sqe__flags.md#ga8578ffdb8f53a51b94fa86a6f02d4a11)

#define RTIO\_SQE\_NO\_RESPONSE

The SQE does not produce a CQE.

**Definition** rtio.h:141

[RTIO\_SQE\_CHAINED](group__rtio__sqe__flags.md#gae9191d521d4ab602b53fefb74020d06b)

#define RTIO\_SQE\_CHAINED

The next request in the queue should wait on this one.

**Definition** rtio.h:96

[rtio\_sqe\_prep\_read\_with\_pool](group__rtio.md#ga15c1f623658d27d300d1a31a6f3d6b9d)

static void rtio\_sqe\_prep\_read\_with\_pool(struct rtio\_sqe \*sqe, const struct rtio\_iodev \*iodev, int8\_t prio, void \*userdata)

Prepare a read op submission with context's mempool.

**Definition** rtio.h:523

[rtio\_executor\_err](group__rtio.md#ga15f4a1a4dfb869ef9e4216dc1c1cdc8a)

void rtio\_executor\_err(struct rtio\_iodev\_sqe \*iodev\_sqe, int result)

[RTIO\_OP\_CALLBACK](group__rtio.md#ga18e0ff7d44e4c33900106aefad0a8508)

#define RTIO\_OP\_CALLBACK

An operation that calls a given function (callback).

**Definition** rtio.h:475

[rtio\_sqe\_acquirable](group__rtio.md#ga1f4fb7bccbaae08a94387e4b11275a78)

static uint32\_t rtio\_sqe\_acquirable(struct rtio \*r)

Count of acquirable submission queue events.

**Definition** rtio.h:869

[rtio\_cqe\_pool\_free](group__rtio.md#ga23c0c5d4b551858eabe057ecb8a28d12)

static void rtio\_cqe\_pool\_free(struct rtio\_cqe\_pool \*pool, struct rtio\_cqe \*cqe)

**Definition** rtio.h:687

[rtio\_sqe\_prep\_tiny\_write](group__rtio.md#ga31be14ece09e061a8d42ca8f2395286a)

static void rtio\_sqe\_prep\_tiny\_write(struct rtio\_sqe \*sqe, const struct rtio\_iodev \*iodev, int8\_t prio, const uint8\_t \*tiny\_write\_data, uint8\_t tiny\_write\_len, void \*userdata)

Prepare a tiny write op submission.

**Definition** rtio.h:568

[rtio\_mempool\_block\_size](group__rtio.md#ga4213be028b0a1264daaa0d30c4c2d089)

static size\_t rtio\_mempool\_block\_size(const struct rtio \*r)

Get the mempool block size of the RTIO context.

**Definition** rtio.h:387

[rtio\_cqe\_submit](group__rtio.md#ga4abc221d5a90ab882000a72caa0ebd0f)

static void rtio\_cqe\_submit(struct rtio \*r, int result, void \*userdata, uint32\_t flags)

Submit a completion queue event with a given result and userdata.

**Definition** rtio.h:1167

[rtio\_sqe\_prep\_nop](group__rtio.md#ga599ee43fdf35e1cf895cbbe9272e4c50)

static void rtio\_sqe\_prep\_nop(struct rtio\_sqe \*sqe, const struct rtio\_iodev \*iodev, void \*userdata)

Prepare a nop (no op) submission.

**Definition** rtio.h:489

[rtio\_release\_buffer](group__rtio.md#ga6530bf56ccbab046a362a6448f941609)

void rtio\_release\_buffer(struct rtio \*r, void \*buff, uint32\_t buff\_len)

Release memory that was allocated by the RTIO's memory pool.

[rtio\_sqe\_copy\_in](group__rtio.md#ga65e351af0a16dcf504a51ef4eb9316c7)

static int rtio\_sqe\_copy\_in(struct rtio \*r, const struct rtio\_sqe \*sqes, size\_t sqe\_count)

Copy an array of SQEs into the queue.

**Definition** rtio.h:1376

[rtio\_cqe\_produce](group__rtio.md#ga6f55202adeca60aed0343a7a0dcab071)

static void rtio\_cqe\_produce(struct rtio \*r, struct rtio\_cqe \*cqe)

Produce a complete queue event if available.

**Definition** rtio.h:979

[RTIO\_OP\_TINY\_TX](group__rtio.md#ga6f95c0a5fbcc020a0d1102d3b08934bd)

#define RTIO\_OP\_TINY\_TX

An operation that transmits tiny writes by copying the data to write.

**Definition** rtio.h:472

[rtio\_cqe\_compute\_flags](group__rtio.md#ga75661c8c6c94a0ac6254cec674b478c8)

static uint32\_t rtio\_cqe\_compute\_flags(struct rtio\_iodev\_sqe \*iodev\_sqe)

Compute the CQE flags from the rtio\_iodev\_sqe entry.

**Definition** rtio.h:1060

[rtio\_executor\_ok](group__rtio.md#ga7e2ebd9abaf585207bc5b99c5d815c6a)

void rtio\_executor\_ok(struct rtio\_iodev\_sqe \*iodev\_sqe, int result)

[rtio\_block\_pool\_alloc](group__rtio.md#ga7f14b99fc1dd0697309e7f71a270f5fb)

static int rtio\_block\_pool\_alloc(struct rtio \*r, size\_t min\_sz, size\_t max\_sz, uint8\_t \*\*buf, uint32\_t \*buf\_len)

**Definition** rtio.h:694

[rtio\_sqe\_prep\_write](group__rtio.md#ga7f7856d1f4fd1d8c4f6eebcccfe77701)

static void rtio\_sqe\_prep\_write(struct rtio\_sqe \*sqe, const struct rtio\_iodev \*iodev, int8\_t prio, const uint8\_t \*buf, uint32\_t len, void \*userdata)

Prepare a write op submission.

**Definition** rtio.h:542

[rtio\_sqe\_copy\_in\_get\_handles](group__rtio.md#ga830863e6c8d9b96f4c473a038cab8f8c)

int rtio\_sqe\_copy\_in\_get\_handles(struct rtio \*r, const struct rtio\_sqe \*sqes, struct rtio\_sqe \*\*handle, size\_t sqe\_count)

Copy an array of SQEs into the queue and get resulting handles back.

[rtio\_cqe\_pool\_alloc](group__rtio.md#ga8497170f55af1d11d717e919f61806f5)

static struct rtio\_cqe \* rtio\_cqe\_pool\_alloc(struct rtio\_cqe\_pool \*pool)

**Definition** rtio.h:670

[rtio\_partition](group__rtio.md#ga86a38086dd85150ab6e479d73db1c6d1)

struct k\_mem\_partition rtio\_partition

The memory partition associated with all RTIO context information.

[rtio\_sqe\_prep\_read](group__rtio.md#ga89c7cc2494e3dda50737f78f1a1376cf)

static void rtio\_sqe\_prep\_read(struct rtio\_sqe \*sqe, const struct rtio\_iodev \*iodev, int8\_t prio, uint8\_t \*buf, uint32\_t len, void \*userdata)

Prepare a read op submission.

**Definition** rtio.h:502

[rtio\_sqe\_acquire](group__rtio.md#ga8b47c954d15a334621def53acceb6799)

static struct rtio\_sqe \* rtio\_sqe\_acquire(struct rtio \*r)

Acquire a single submission queue event if available.

**Definition** rtio.h:930

[RTIO\_OP\_TX](group__rtio.md#ga8dcaef0cda159e16520a95543ff62827)

#define RTIO\_OP\_TX

An operation that transmits (writes).

**Definition** rtio.h:469

[rtio\_sqe\_drop\_all](group__rtio.md#ga9486fb7b50e8d2409a50da235203536b)

static void rtio\_sqe\_drop\_all(struct rtio \*r)

Drop all previously acquired sqe.

**Definition** rtio.h:948

[rtio\_sqe\_prep\_read\_multishot](group__rtio.md#ga9803aa829f8c0eeee746ea7d872c20cc)

static void rtio\_sqe\_prep\_read\_multishot(struct rtio\_sqe \*sqe, const struct rtio\_iodev \*iodev, int8\_t prio, void \*userdata)

**Definition** rtio.h:531

[rtio\_cqe\_copy\_out](group__rtio.md#ga98b2bbef95aea342a9b86a9775dd5c3b)

int rtio\_cqe\_copy\_out(struct rtio \*r, struct rtio\_cqe \*cqes, size\_t cqe\_count, k\_timeout\_t timeout)

Copy an array of CQEs from the queue.

[rtio\_sqe\_prep\_callback](group__rtio.md#ga9d0dd7d0e2e3d281092f2350d6e1713e)

static void rtio\_sqe\_prep\_callback(struct rtio\_sqe \*sqe, rtio\_callback\_t callback, void \*arg0, void \*userdata)

Prepare a callback op submission.

**Definition** rtio.h:594

[rtio\_access\_grant](group__rtio.md#ga9da42c98546930575525f0f92710f9e4)

static void rtio\_access\_grant(struct rtio \*r, struct k\_thread \*t)

Grant access to an RTIO context to a user thread.

**Definition** rtio.h:1282

[RTIO\_OP\_TXRX](group__rtio.md#ga9f0e70f5a28be65a8ed67c0257a72692)

#define RTIO\_OP\_TXRX

An operation that transceives (reads and writes simultaneously).

**Definition** rtio.h:478

[rtio\_cqe\_release](group__rtio.md#gaa0799a5f8ad98425d385a07c5d27d9cb)

static void rtio\_cqe\_release(struct rtio \*r, struct rtio\_cqe \*cqe)

Release consumed completion queue event.

**Definition** rtio.h:1049

[rtio\_sqe\_rx\_buf](group__rtio.md#gaab6843e2038d00a8354f57d7e2ffcf7e)

static int rtio\_sqe\_rx\_buf(const struct rtio\_iodev\_sqe \*iodev\_sqe, uint32\_t min\_buf\_len, uint32\_t max\_buf\_len, uint8\_t \*\*buf, uint32\_t \*buf\_len)

Get the buffer associate with the RX submission.

**Definition** rtio.h:1208

[rtio\_iodev\_sqe\_err](group__rtio.md#gaada07aa6acefa548743b525225fa482f)

static void rtio\_iodev\_sqe\_err(struct rtio\_iodev\_sqe \*iodev\_sqe, int result)

Inform the executor of a submissions completion with error.

**Definition** rtio.h:1151

[rtio\_sqe\_prep\_transceive](group__rtio.md#gab9b605dcbb01d21c88f9ae70588ea3b5)

static void rtio\_sqe\_prep\_transceive(struct rtio\_sqe \*sqe, const struct rtio\_iodev \*iodev, int8\_t prio, const uint8\_t \*tx\_buf, uint8\_t \*rx\_buf, uint32\_t buf\_len, void \*userdata)

Prepare a transceive op submission.

**Definition** rtio.h:630

[rtio\_sqe\_cancel](group__rtio.md#gac01252e55d2848b38c0ed77b71d600a7)

int rtio\_sqe\_cancel(struct rtio\_sqe \*sqe)

Attempt to cancel an SQE.

[rtio\_sqe\_pool\_free](group__rtio.md#gac776aea3692cfd77aa5bf675a9e9ed02)

static void rtio\_sqe\_pool\_free(struct rtio\_sqe\_pool \*pool, struct rtio\_iodev\_sqe \*iodev\_sqe)

**Definition** rtio.h:663

[rtio\_iodev\_sqe\_ok](group__rtio.md#gacb1d2ffa2b07418d8a8aa319bd4336ab)

static void rtio\_iodev\_sqe\_ok(struct rtio\_iodev\_sqe \*iodev\_sqe, int result)

Inform the executor of a submission completion with success.

**Definition** rtio.h:1138

[rtio\_callback\_t](group__rtio.md#gad1dbd690e6cf88d7c788436dd04d1a00)

void(\* rtio\_callback\_t)(struct rtio \*r, const struct rtio\_sqe \*sqe, void \*arg0)

Callback signature for RTIO\_OP\_CALLBACK.

**Definition** rtio.h:227

[RTIO\_OP\_NOP](group__rtio.md#gad5f073978f641413989d1c6b405d6c36)

#define RTIO\_OP\_NOP

An operation that does nothing and will complete immediately.

**Definition** rtio.h:463

[rtio\_cqe\_acquire](group__rtio.md#gad848646651fdf3649b882e5268f72a3c)

static struct rtio\_cqe \* rtio\_cqe\_acquire(struct rtio \*r)

Acquire a complete queue event if available.

**Definition** rtio.h:963

[rtio\_chain\_next](group__rtio.md#gada1e3abf92a46e376138435debc8baf4)

static struct rtio\_iodev\_sqe \* rtio\_chain\_next(const struct rtio\_iodev\_sqe \*iodev\_sqe)

Get the next sqe in the chain.

**Definition** rtio.h:900

[rtio\_cqe\_consume](group__rtio.md#gae562cf241911804cdb9f4e3a73b53df4)

static struct rtio\_cqe \* rtio\_cqe\_consume(struct rtio \*r)

Consume a single completion queue event if available.

**Definition** rtio.h:995

[rtio\_sqe\_pool\_alloc](group__rtio.md#gae5fb03fc8f3a4a774f476ff552999bfc)

static struct rtio\_iodev\_sqe \* rtio\_sqe\_pool\_alloc(struct rtio\_sqe\_pool \*pool)

**Definition** rtio.h:648

[rtio\_iodev\_sqe\_next](group__rtio.md#gae690e3dc0fc40dda57257b2eed432719)

static struct rtio\_iodev\_sqe \* rtio\_iodev\_sqe\_next(const struct rtio\_iodev\_sqe \*iodev\_sqe)

Get the next sqe in the chain or transaction.

**Definition** rtio.h:917

[rtio\_sqe\_prep\_callback\_no\_cqe](group__rtio.md#gae87be354087d038953dae07c7f9cd3b0)

static void rtio\_sqe\_prep\_callback\_no\_cqe(struct rtio\_sqe \*sqe, rtio\_callback\_t callback, void \*arg0, void \*userdata)

Prepare a callback op submission that does not create a CQE.

**Definition** rtio.h:618

[rtio\_cqe\_get\_mempool\_buffer](group__rtio.md#gaedbf9386a36ed99baa290ef6c318ded1)

int rtio\_cqe\_get\_mempool\_buffer(const struct rtio \*r, struct rtio\_cqe \*cqe, uint8\_t \*\*buff, uint32\_t \*buff\_len)

Retrieve the mempool buffer that was allocated for the CQE.

[rtio\_txn\_next](group__rtio.md#gaef904eb6a8810d8c3ea537c4d6edbee5)

static struct rtio\_iodev\_sqe \* rtio\_txn\_next(const struct rtio\_iodev\_sqe \*iodev\_sqe)

Get the next sqe in the transaction.

**Definition** rtio.h:882

[rtio\_executor\_submit](group__rtio.md#gaf191153e83de72ddefb998daad02fa16)

void rtio\_executor\_submit(struct rtio \*r)

[rtio\_cqe\_consume\_block](group__rtio.md#gaf617d05d9b59ce1f1d0697617ef6f249)

static struct rtio\_cqe \* rtio\_cqe\_consume\_block(struct rtio \*r)

Wait for and consume a single completion queue event.

**Definition** rtio.h:1025

[rtio\_block\_pool\_free](group__rtio.md#gafca7732926a9a7c080e3cb16e5f16108)

static void rtio\_block\_pool\_free(struct rtio \*r, void \*buf, uint32\_t buf\_len)

**Definition** rtio.h:735

[RTIO\_OP\_RX](group__rtio.md#gafeb05c351207cd1638fa78f6607e1a4a)

#define RTIO\_OP\_RX

An operation that receives (reads).

**Definition** rtio.h:466

[rtio\_submit](group__rtio.md#gafee27c64a4a4989c4eb774addde8eb2e)

int rtio\_submit(struct rtio \*r, uint32\_t wait\_count)

Submit I/O requests to the underlying executor.

[k\_sem\_reset](group__semaphore__apis.md#ga1bd12d8d8c1b9c6be9b665d0fefe5562)

void k\_sem\_reset(struct k\_sem \*sem)

Resets a semaphore's count to zero.

[k\_sem\_give](group__semaphore__apis.md#gab9be3cf1988af2cd6afdace52d497c84)

void k\_sem\_give(struct k\_sem \*sem)

Give a semaphore.

[k\_sem\_take](group__semaphore__apis.md#gac71e2383c1920dddc45a561cacfef090)

int k\_sem\_take(struct k\_sem \*sem, k\_timeout\_t timeout)

Take a semaphore.

[BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)

#define BIT(n)

Unsigned integer with bit position n set (signed in assembly language).

**Definition** util\_macro.h:44

[CONTAINER\_OF](group__sys-util.md#gac5bc561d1bfd1bf68877fe577779bd2f)

#define CONTAINER\_OF(ptr, type, field)

Get a pointer to a structure containing the element.

**Definition** util.h:284

[DIV\_ROUND\_UP](group__sys-util.md#gae664e7492e37d324831caf2321ddda37)

#define DIV\_ROUND\_UP(n, d)

Divide and round up.

**Definition** util.h:352

[EINVAL](group__system__errno.md#ga2d1678d5a7cc8ce499643f3b8957def4)

#define EINVAL

Invalid argument.

**Definition** errno.h:60

[ENOMEM](group__system__errno.md#ga6a05c923dad0c1208043e9c20a58c8e5)

#define ENOMEM

Not enough core.

**Definition** errno.h:50

[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33)

#define ENOTSUP

Unsupported value.

**Definition** errno.h:114

[k\_yield](group__thread__apis.md#ga08a3484c33444ecedc2d71d78495a295)

void k\_yield(void)

Yield the current thread.

[k\_object\_access\_grant](group__usermode__apis.md#ga94087bedf96fe2a2bea437d3d585ca22)

void k\_object\_access\_grant(const void \*object, struct k\_thread \*thread)

Grant a thread access to a kernel object.

[kernel.h](kernel_8h.md)

Public kernel APIs.

[mem\_blocks.h](mem__blocks_8h.md)

Memory Blocks Allocator.

[mpsc\_lockfree.h](mpsc__lockfree_8h.md)

A wait-free intrusive multi producer single consumer (MPSC) queue using a singly linked list.

[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)

flags

**Definition** parser.h:96

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2)

\_\_INT32\_TYPE\_\_ int32\_t

**Definition** stdint.h:74

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[UINT16\_MAX](stdint_8h.md#a3ea490c9b3617d4479bd80ef93cd5602)

#define UINT16\_MAX

**Definition** stdint.h:28

[uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808)

\_\_UINTPTR\_TYPE\_\_ uintptr\_t

**Definition** stdint.h:105

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6)

\_\_INT8\_TYPE\_\_ int8\_t

**Definition** stdint.h:72

[string.h](string_8h.md)

[memset](string_8h.md#a4137694174d4ca2fad886a1db355015c)

void \* memset(void \*buf, int c, size\_t n)

[memcpy](string_8h.md#af0f01bffcd16daa9143f6014d10a25ad)

void \* memcpy(void \*ZRESTRICT d, const void \*ZRESTRICT s, size\_t n)

[k\_mem\_partition](structk__mem__partition.md)

Memory Partition.

**Definition** mem\_domain.h:55

[k\_thread](structk__thread.md)

Thread Structure.

**Definition** thread.h:259

[k\_timeout\_t](structk__timeout__t.md)

Kernel timeout type.

**Definition** sys\_clock.h:65

[k\_timepoint\_t](structk__timepoint__t.md)

Kernel timepoint type.

**Definition** sys\_clock.h:219

[mpsc\_node](structmpsc__node.md)

Queue member.

**Definition** mpsc\_lockfree.h:79

[mpsc](structmpsc.md)

MPSC Queue.

**Definition** mpsc\_lockfree.h:86

[rtio\_cqe\_pool](structrtio__cqe__pool.md)

**Definition** rtio.h:315

[rtio\_cqe\_pool::pool](structrtio__cqe__pool.md#a05584219d473fcf85d46757fa9cea703)

struct rtio\_cqe \* pool

**Definition** rtio.h:319

[rtio\_cqe\_pool::free\_q](structrtio__cqe__pool.md#a13bd7991ff5622c1cb5aa6af014aaab3)

struct mpsc free\_q

**Definition** rtio.h:316

[rtio\_cqe\_pool::pool\_size](structrtio__cqe__pool.md#a43bf4141673c61493644539987f27fb1)

const uint16\_t pool\_size

**Definition** rtio.h:317

[rtio\_cqe\_pool::pool\_free](structrtio__cqe__pool.md#a4fb501a0ba15e2956113deaf4597d846)

uint16\_t pool\_free

**Definition** rtio.h:318

[rtio\_cqe](structrtio__cqe.md)

A completion queue event.

**Definition** rtio.h:300

[rtio\_cqe::userdata](structrtio__cqe.md#a15128387ccbea55812ef229eab7241e7)

void \* userdata

Associated userdata with operation.

**Definition** rtio.h:304

[rtio\_cqe::q](structrtio__cqe.md#a27272bca31c170f406799633ec82098d)

struct mpsc\_node q

**Definition** rtio.h:301

[rtio\_cqe::flags](structrtio__cqe.md#a8a7632ef1cfd31529d782bd761908d93)

uint32\_t flags

Flags associated with the operation.

**Definition** rtio.h:305

[rtio\_cqe::result](structrtio__cqe.md#acbe2e6607a752b676d9336b9ca6ce435)

int32\_t result

Result from operation.

**Definition** rtio.h:303

[rtio\_iodev\_api](structrtio__iodev__api.md)

API that an RTIO IO device should implement.

**Definition** rtio.h:439

[rtio\_iodev\_api::submit](structrtio__iodev__api.md#a6cd795906753535571ec1ecc0e0c430c)

void(\* submit)(struct rtio\_iodev\_sqe \*iodev\_sqe)

Submit to the iodev an entry to work on.

**Definition** rtio.h:448

[rtio\_iodev\_sqe](structrtio__iodev__sqe.md)

Compute the mempool block index for a given pointer.

**Definition** rtio.h:429

[rtio\_iodev\_sqe::next](structrtio__iodev__sqe.md#a2afb82e550e614f87db7cd1bf2c3a352)

struct rtio\_iodev\_sqe \* next

**Definition** rtio.h:432

[rtio\_iodev\_sqe::sqe](structrtio__iodev__sqe.md#a2bd98599678909c0ddb22f879affa12b)

struct rtio\_sqe sqe

**Definition** rtio.h:430

[rtio\_iodev\_sqe::r](structrtio__iodev__sqe.md#a3c3a050793589258eab5ff5ac30f24c8)

struct rtio \* r

**Definition** rtio.h:433

[rtio\_iodev\_sqe::q](structrtio__iodev__sqe.md#a9cfdd004b65a5e2bc111bc2fb333498c)

struct mpsc\_node q

**Definition** rtio.h:431

[rtio\_iodev](structrtio__iodev.md)

An IO device with a function table for submitting requests.

**Definition** rtio.h:454

[rtio\_iodev::api](structrtio__iodev.md#a6dfedbfb58356e0647e5c20632656977)

const struct rtio\_iodev\_api \* api

**Definition** rtio.h:456

[rtio\_iodev::data](structrtio__iodev.md#af0f3a27fe8dea2161c9a73cb838bdeec)

void \* data

**Definition** rtio.h:459

[rtio\_sqe\_pool](structrtio__sqe__pool.md)

**Definition** rtio.h:308

[rtio\_sqe\_pool::pool](structrtio__sqe__pool.md#ab2c0394e175bd8c6f0c02edb315b6c9b)

struct rtio\_iodev\_sqe \* pool

**Definition** rtio.h:312

[rtio\_sqe\_pool::pool\_size](structrtio__sqe__pool.md#ade3b4354d007fe17a7753c26e2121465)

const uint16\_t pool\_size

**Definition** rtio.h:310

[rtio\_sqe\_pool::free\_q](structrtio__sqe__pool.md#aed49ea25c952e07a8287919268fd2485)

struct mpsc free\_q

**Definition** rtio.h:309

[rtio\_sqe\_pool::pool\_free](structrtio__sqe__pool.md#af7990b1510ad2343573f3e4e502475b0)

uint16\_t pool\_free

**Definition** rtio.h:311

[rtio\_sqe](structrtio__sqe.md)

A submission queue event.

**Definition** rtio.h:232

[rtio\_sqe::i2c\_config](structrtio__sqe.md#a07bf344b1b1063b8bea80cf5ba1c1cc5)

uint32\_t i2c\_config

OP\_I2C\_CONFIGURE.

**Definition** rtio.h:288

[rtio\_sqe::userdata](structrtio__sqe.md#a0ed519ee0b5867ff73bdaf37f983c971)

void \* userdata

User provided data which is returned upon operation completion.

**Definition** rtio.h:252

[rtio\_sqe::tx\_buf](structrtio__sqe.md#a18bfa63542954f4bb8b924c92c48e931)

const uint8\_t \* tx\_buf

Buffer to write from.

**Definition** rtio.h:283

[rtio\_sqe::tiny\_tx](structrtio__sqe.md#a19ace9c984538c2022e7f8ecaefa075d)

struct rtio\_sqe::@346015370260157122324174060242055067274246076272::@156103043324343070111363144011175302340145332235 tiny\_tx

OP\_TINY\_TX.

[rtio\_sqe::op](structrtio__sqe.md#a1d8d3e3426e47a2c7f54d98f51acd953)

uint8\_t op

Op code.

**Definition** rtio.h:233

[rtio\_sqe::rx](structrtio__sqe.md#a37a98afc43f26355c70e7036725b2544)

struct rtio\_sqe::@346015370260157122324174060242055067274246076272::@133276262235321357167246345002275273273102345261 rx

OP\_RX.

[rtio\_sqe::arg0](structrtio__sqe.md#a438d2156a61aef9ca840af9c01d5dfa4)

void \* arg0

Last argument given to callback.

**Definition** rtio.h:277

[rtio\_sqe::tx](structrtio__sqe.md#a4399cf25c7e761126a6218c2b7e3192d)

struct rtio\_sqe::@346015370260157122324174060242055067274246076272::@004235137221060376063310265133374117312204154130 tx

OP\_TX.

[rtio\_sqe::rx\_buf](structrtio__sqe.md#a4d2090fc11b897724a883ad1087d9f73)

uint8\_t \* rx\_buf

Buffer to read into.

**Definition** rtio.h:284

[rtio\_sqe::prio](structrtio__sqe.md#a528eb9b721be7b8a8898ab16a7e2d9a7)

uint8\_t prio

Op priority.

**Definition** rtio.h:235

[rtio\_sqe::txrx](structrtio__sqe.md#a5f2511eb361a7a4d54a92fae4d391e8c)

struct rtio\_sqe::@346015370260157122324174060242055067274246076272::@324335144354230362066357340057163170350241057343 txrx

OP\_TXRX.

[rtio\_sqe::buf\_len](structrtio__sqe.md#a67376f40a13960b152a23da250275722)

uint32\_t buf\_len

Length of buffer.

**Definition** rtio.h:258

[rtio\_sqe::iodev](structrtio__sqe.md#a6c784702f011592c84feacd57915bbfc)

const struct rtio\_iodev \* iodev

Device to operation on.

**Definition** rtio.h:243

[rtio\_sqe::flags](structrtio__sqe.md#aad2ff8524df0e24b812e77e2393bf5b0)

uint16\_t flags

Op Flags.

**Definition** rtio.h:237

[rtio\_sqe::buf](structrtio__sqe.md#ab71176c084e8b8eb65dfeb3018ae2a49)

const uint8\_t \* buf

Buffer to write from.

**Definition** rtio.h:259

[rtio\_sqe::callback](structrtio__sqe.md#af8c31c33e9fedebe55cac73595d0f696)

rtio\_callback\_t callback

**Definition** rtio.h:276

[rtio\_sqe::iodev\_flags](structrtio__sqe.md#af979ffa7bd3efaa6cbcb1344404cb985)

uint16\_t iodev\_flags

Op iodev flags.

**Definition** rtio.h:239

[rtio](structrtio.md)

An RTIO context containing what can be viewed as a pair of queues.

**Definition** rtio.h:333

[rtio::cqe\_pool](structrtio.md#a1bce3c3bb0150275ece65975adf3ee4f)

struct rtio\_cqe\_pool \* cqe\_pool

**Definition** rtio.h:363

[rtio::sq](structrtio.md#a34fbabfdbef3144f4520bf678684cdfb)

struct mpsc sq

**Definition** rtio.h:371

[rtio::cq\_count](structrtio.md#a358de1033ab4396d1f1baee2699c993f)

atomic\_t cq\_count

**Definition** rtio.h:352

[rtio::sqe\_pool](structrtio.md#a955f012bac623e7c037b5f1dba8e7fda)

struct rtio\_sqe\_pool \* sqe\_pool

**Definition** rtio.h:360

[rtio::xcqcnt](structrtio.md#ac45facdcc6d64cd70113b9b05b2fb086)

atomic\_t xcqcnt

**Definition** rtio.h:357

[rtio::cq](structrtio.md#ad6f44a354a170cb04a584beee7728fa9)

struct mpsc cq

**Definition** rtio.h:374

[atomic.h](sys_2atomic_8h.md)

[iterable\_sections.h](sys_2iterable__sections_8h.md)

[util.h](sys_2util_8h.md)

Misc utilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [rtio](dir_2c800b92938ab205b51fc9bd951bff11.md)
- [rtio.h](rtio_2rtio_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
