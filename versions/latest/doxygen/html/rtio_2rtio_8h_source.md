---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/rtio_2rtio_8h_source.html
original_path: doxygen/html/rtio_2rtio_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
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

37#include <[zephyr/sys/util.h](util_8h.md)>

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

[ 259](structrtio__sqe.md#a55e98f27b26393fee8e179b7bdb6a52e) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[buf](structrtio__sqe.md#a55e98f27b26393fee8e179b7bdb6a52e);

260 };

261

263 struct {

[ 264](structrtio__sqe.md#ab25f9d5c2e4d833d548148843a859096) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [tiny\_buf\_len](structrtio__sqe.md#ab25f9d5c2e4d833d548148843a859096);

[ 265](structrtio__sqe.md#aceaa9999b86fd271321988e257aeecc8) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [tiny\_buf](structrtio__sqe.md#aceaa9999b86fd271321988e257aeecc8)[7];

266 };

267

269 struct {

[ 270](structrtio__sqe.md#af8c31c33e9fedebe55cac73595d0f696) [rtio\_callback\_t](group__rtio.md#gad1dbd690e6cf88d7c788436dd04d1a00) [callback](structrtio__sqe.md#af8c31c33e9fedebe55cac73595d0f696);

[ 271](structrtio__sqe.md#a438d2156a61aef9ca840af9c01d5dfa4) void \*[arg0](structrtio__sqe.md#a438d2156a61aef9ca840af9c01d5dfa4);

272 };

273

275 struct {

[ 276](structrtio__sqe.md#ab3cff3dbbfc9b1a0dbe8f1dc28ac83f8) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [txrx\_buf\_len](structrtio__sqe.md#ab3cff3dbbfc9b1a0dbe8f1dc28ac83f8);

[ 277](structrtio__sqe.md#a186c22217961a5eddb75ad0bd84a538a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[tx\_buf](structrtio__sqe.md#a186c22217961a5eddb75ad0bd84a538a);

[ 278](structrtio__sqe.md#a4d2090fc11b897724a883ad1087d9f73) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[rx\_buf](structrtio__sqe.md#a4d2090fc11b897724a883ad1087d9f73);

279 };

280

[ 282](structrtio__sqe.md#a07bf344b1b1063b8bea80cf5ba1c1cc5) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [i2c\_config](structrtio__sqe.md#a07bf344b1b1063b8bea80cf5ba1c1cc5);

283 };

284};

285

287/\* Ensure the rtio\_sqe never grows beyond a common cacheline size of 64 bytes \*/

288BUILD\_ASSERT(sizeof(struct [rtio\_sqe](structrtio__sqe.md)) <= 64);

290

[ 294](structrtio__cqe.md)struct [rtio\_cqe](structrtio__cqe.md) {

[ 295](structrtio__cqe.md#a27272bca31c170f406799633ec82098d) struct [mpsc\_node](structmpsc__node.md) [q](structrtio__cqe.md#a27272bca31c170f406799633ec82098d);

296

[ 297](structrtio__cqe.md#acbe2e6607a752b676d9336b9ca6ce435) [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) [result](structrtio__cqe.md#acbe2e6607a752b676d9336b9ca6ce435);

[ 298](structrtio__cqe.md#a15128387ccbea55812ef229eab7241e7) void \*[userdata](structrtio__cqe.md#a15128387ccbea55812ef229eab7241e7);

[ 299](structrtio__cqe.md#a8a7632ef1cfd31529d782bd761908d93) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](structrtio__cqe.md#a8a7632ef1cfd31529d782bd761908d93);

300};

301

[ 302](structrtio__sqe__pool.md)struct [rtio\_sqe\_pool](structrtio__sqe__pool.md) {

[ 303](structrtio__sqe__pool.md#aed49ea25c952e07a8287919268fd2485) struct [mpsc](structmpsc.md) [free\_q](structrtio__sqe__pool.md#aed49ea25c952e07a8287919268fd2485);

[ 304](structrtio__sqe__pool.md#ade3b4354d007fe17a7753c26e2121465) const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [pool\_size](structrtio__sqe__pool.md#ade3b4354d007fe17a7753c26e2121465);

[ 305](structrtio__sqe__pool.md#af7990b1510ad2343573f3e4e502475b0) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [pool\_free](structrtio__sqe__pool.md#af7990b1510ad2343573f3e4e502475b0);

[ 306](structrtio__sqe__pool.md#ab2c0394e175bd8c6f0c02edb315b6c9b) struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \*[pool](structrtio__sqe__pool.md#ab2c0394e175bd8c6f0c02edb315b6c9b);

307};

308

[ 309](structrtio__cqe__pool.md)struct [rtio\_cqe\_pool](structrtio__cqe__pool.md) {

[ 310](structrtio__cqe__pool.md#a13bd7991ff5622c1cb5aa6af014aaab3) struct [mpsc](structmpsc.md) [free\_q](structrtio__cqe__pool.md#a13bd7991ff5622c1cb5aa6af014aaab3);

[ 311](structrtio__cqe__pool.md#a43bf4141673c61493644539987f27fb1) const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [pool\_size](structrtio__cqe__pool.md#a43bf4141673c61493644539987f27fb1);

[ 312](structrtio__cqe__pool.md#a4fb501a0ba15e2956113deaf4597d846) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [pool\_free](structrtio__cqe__pool.md#a4fb501a0ba15e2956113deaf4597d846);

[ 313](structrtio__cqe__pool.md#a05584219d473fcf85d46757fa9cea703) struct [rtio\_cqe](structrtio__cqe.md) \*[pool](structrtio__cqe__pool.md#a05584219d473fcf85d46757fa9cea703);

314};

315

[ 327](structrtio.md)struct [rtio](structrtio.md) {

328#ifdef CONFIG\_RTIO\_SUBMIT\_SEM

329 /\* A wait semaphore which may suspend the calling thread

330 \* to wait for some number of completions when calling submit

331 \*/

332 struct k\_sem \*submit\_sem;

333

334 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) submit\_count;

335#endif

336

337#ifdef CONFIG\_RTIO\_CONSUME\_SEM

338 /\* A wait semaphore which may suspend the calling thread

339 \* to wait for some number of completions while consuming

340 \* them from the completion queue

341 \*/

342 struct k\_sem \*consume\_sem;

343#endif

344

345 /\* Total number of completions \*/

[ 346](structrtio.md#a358de1033ab4396d1f1baee2699c993f) [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) [cq\_count](structrtio.md#a358de1033ab4396d1f1baee2699c993f);

347

348 /\* Number of completions that were unable to be submitted with results

349 \* due to the cq spsc being full

350 \*/

[ 351](structrtio.md#ac45facdcc6d64cd70113b9b05b2fb086) [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) [xcqcnt](structrtio.md#ac45facdcc6d64cd70113b9b05b2fb086);

352

353 /\* Submission queue object pool with free list \*/

[ 354](structrtio.md#a955f012bac623e7c037b5f1dba8e7fda) struct [rtio\_sqe\_pool](structrtio__sqe__pool.md) \*[sqe\_pool](structrtio.md#a955f012bac623e7c037b5f1dba8e7fda);

355

356 /\* Complete queue object pool with free list \*/

[ 357](structrtio.md#a1bce3c3bb0150275ece65975adf3ee4f) struct [rtio\_cqe\_pool](structrtio__cqe__pool.md) \*[cqe\_pool](structrtio.md#a1bce3c3bb0150275ece65975adf3ee4f);

358

359#ifdef CONFIG\_RTIO\_SYS\_MEM\_BLOCKS

360 /\* Mem block pool \*/

361 struct sys\_mem\_blocks \*block\_pool;

362#endif

363

364 /\* Submission queue \*/

[ 365](structrtio.md#a34fbabfdbef3144f4520bf678684cdfb) struct [mpsc](structmpsc.md) [sq](structrtio.md#a34fbabfdbef3144f4520bf678684cdfb);

366

367 /\* Completion queue \*/

[ 368](structrtio.md#ad6f44a354a170cb04a584beee7728fa9) struct [mpsc](structmpsc.md) [cq](structrtio.md#ad6f44a354a170cb04a584beee7728fa9);

369};

370

372extern struct [k\_mem\_partition](structk__mem__partition.md) [rtio\_partition](group__rtio.md#ga86a38086dd85150ab6e479d73db1c6d1);

373

[ 381](group__rtio.md#ga4213be028b0a1264daaa0d30c4c2d089)static inline size\_t [rtio\_mempool\_block\_size](group__rtio.md#ga4213be028b0a1264daaa0d30c4c2d089)(const struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2))

382{

383#ifndef CONFIG\_RTIO\_SYS\_MEM\_BLOCKS

384 ARG\_UNUSED([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2));

385 return 0;

386#else

387 if ([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) == NULL || [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->block\_pool == NULL) {

388 return 0;

389 }

390 return [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->block\_pool->info.blk\_sz\_shift);

391#endif

392}

393

401#ifdef CONFIG\_RTIO\_SYS\_MEM\_BLOCKS

402static inline [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \_\_rtio\_compute\_mempool\_block\_index(const struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2), const void \*ptr)

403{

404 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) addr = ([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808))ptr;

405 struct sys\_mem\_blocks \*mem\_pool = [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->block\_pool;

406 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size = [rtio\_mempool\_block\_size](group__rtio.md#ga4213be028b0a1264daaa0d30c4c2d089)([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2));

407

408 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) buff = ([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808))mem\_pool->buffer;

409 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) buff\_size = mem\_pool->info.num\_blocks \* block\_size;

410

411 if (addr < buff || addr >= buff + buff\_size) {

412 return [UINT16\_MAX](stdint_8h.md#a3ea490c9b3617d4479bd80ef93cd5602);

413 }

414 return (addr - buff) / block\_size;

415}

416#endif

417

[ 423](structrtio__iodev__sqe.md)struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) {

[ 424](structrtio__iodev__sqe.md#a2bd98599678909c0ddb22f879affa12b) struct [rtio\_sqe](structrtio__sqe.md) [sqe](structrtio__iodev__sqe.md#a2bd98599678909c0ddb22f879affa12b);

[ 425](structrtio__iodev__sqe.md#a9cfdd004b65a5e2bc111bc2fb333498c) struct [mpsc\_node](structmpsc__node.md) [q](structrtio__iodev__sqe.md#a9cfdd004b65a5e2bc111bc2fb333498c);

[ 426](structrtio__iodev__sqe.md#a2afb82e550e614f87db7cd1bf2c3a352) struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \*[next](structrtio__iodev__sqe.md#a2afb82e550e614f87db7cd1bf2c3a352);

[ 427](structrtio__iodev__sqe.md#a3c3a050793589258eab5ff5ac30f24c8) struct [rtio](structrtio.md) \*[r](structrtio__iodev__sqe.md#a3c3a050793589258eab5ff5ac30f24c8);

428};

429

[ 433](structrtio__iodev__api.md)struct [rtio\_iodev\_api](structrtio__iodev__api.md) {

[ 442](structrtio__iodev__api.md#a6cd795906753535571ec1ecc0e0c430c) void (\*[submit](structrtio__iodev__api.md#a6cd795906753535571ec1ecc0e0c430c))(struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \*iodev\_sqe);

443};

444

[ 448](structrtio__iodev.md)struct [rtio\_iodev](structrtio__iodev.md) {

449 /\* Function pointer table \*/

[ 450](structrtio__iodev.md#a6dfedbfb58356e0647e5c20632656977) const struct [rtio\_iodev\_api](structrtio__iodev__api.md) \*[api](structrtio__iodev.md#a6dfedbfb58356e0647e5c20632656977);

451

452 /\* Data associated with this iodev \*/

[ 453](structrtio__iodev.md#af0f3a27fe8dea2161c9a73cb838bdeec) void \*[data](structrtio__iodev.md#af0f3a27fe8dea2161c9a73cb838bdeec);

454};

455

[ 457](group__rtio.md#gad5f073978f641413989d1c6b405d6c36)#define RTIO\_OP\_NOP 0

458

[ 460](group__rtio.md#gafeb05c351207cd1638fa78f6607e1a4a)#define RTIO\_OP\_RX (RTIO\_OP\_NOP+1)

461

[ 463](group__rtio.md#ga8dcaef0cda159e16520a95543ff62827)#define RTIO\_OP\_TX (RTIO\_OP\_RX+1)

464

[ 466](group__rtio.md#ga6f95c0a5fbcc020a0d1102d3b08934bd)#define RTIO\_OP\_TINY\_TX (RTIO\_OP\_TX+1)

467

[ 469](group__rtio.md#ga18e0ff7d44e4c33900106aefad0a8508)#define RTIO\_OP\_CALLBACK (RTIO\_OP\_TINY\_TX+1)

470

[ 472](group__rtio.md#ga9f0e70f5a28be65a8ed67c0257a72692)#define RTIO\_OP\_TXRX (RTIO\_OP\_CALLBACK+1)

473

[ 475](group__rtio.md#ga3b4f9b1ee1612290323161ecc16e0859)#define RTIO\_OP\_I2C\_RECOVER (RTIO\_OP\_TXRX+1)

476

[ 478](group__rtio.md#gad987be3acfe406b11419c7e8cd068cf5)#define RTIO\_OP\_I2C\_CONFIGURE (RTIO\_OP\_I2C\_RECOVER+1)

479

[ 483](group__rtio.md#ga599ee43fdf35e1cf895cbbe9272e4c50)static inline void [rtio\_sqe\_prep\_nop](group__rtio.md#ga599ee43fdf35e1cf895cbbe9272e4c50)(struct [rtio\_sqe](structrtio__sqe.md) \*sqe,

484 const struct [rtio\_iodev](structrtio__iodev.md) \*iodev,

485 void \*userdata)

486{

487 [memset](string_8h.md#a4137694174d4ca2fad886a1db355015c)(sqe, 0, sizeof(struct [rtio\_sqe](structrtio__sqe.md)));

488 sqe->[op](structrtio__sqe.md#a1d8d3e3426e47a2c7f54d98f51acd953) = [RTIO\_OP\_NOP](group__rtio.md#gad5f073978f641413989d1c6b405d6c36);

489 sqe->[iodev](structrtio__sqe.md#a6c784702f011592c84feacd57915bbfc) = iodev;

490 sqe->[userdata](structrtio__sqe.md#a0ed519ee0b5867ff73bdaf37f983c971) = userdata;

491}

492

[ 496](group__rtio.md#ga89c7cc2494e3dda50737f78f1a1376cf)static inline void [rtio\_sqe\_prep\_read](group__rtio.md#ga89c7cc2494e3dda50737f78f1a1376cf)(struct [rtio\_sqe](structrtio__sqe.md) \*sqe,

497 const struct [rtio\_iodev](structrtio__iodev.md) \*iodev,

498 [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) prio,

499 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf,

500 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) len,

501 void \*userdata)

502{

503 [memset](string_8h.md#a4137694174d4ca2fad886a1db355015c)(sqe, 0, sizeof(struct [rtio\_sqe](structrtio__sqe.md)));

504 sqe->[op](structrtio__sqe.md#a1d8d3e3426e47a2c7f54d98f51acd953) = [RTIO\_OP\_RX](group__rtio.md#gafeb05c351207cd1638fa78f6607e1a4a);

505 sqe->[prio](structrtio__sqe.md#a528eb9b721be7b8a8898ab16a7e2d9a7) = prio;

506 sqe->[iodev](structrtio__sqe.md#a6c784702f011592c84feacd57915bbfc) = iodev;

507 sqe->[buf\_len](structrtio__sqe.md#a67376f40a13960b152a23da250275722) = len;

508 sqe->[buf](structrtio__sqe.md#a55e98f27b26393fee8e179b7bdb6a52e) = buf;

509 sqe->[userdata](structrtio__sqe.md#a0ed519ee0b5867ff73bdaf37f983c971) = userdata;

510}

511

[ 517](group__rtio.md#ga15c1f623658d27d300d1a31a6f3d6b9d)static inline void [rtio\_sqe\_prep\_read\_with\_pool](group__rtio.md#ga15c1f623658d27d300d1a31a6f3d6b9d)(struct [rtio\_sqe](structrtio__sqe.md) \*sqe,

518 const struct [rtio\_iodev](structrtio__iodev.md) \*iodev, [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) prio,

519 void \*userdata)

520{

521 [rtio\_sqe\_prep\_read](group__rtio.md#ga89c7cc2494e3dda50737f78f1a1376cf)(sqe, iodev, prio, NULL, 0, userdata);

522 sqe->[flags](structrtio__sqe.md#aad2ff8524df0e24b812e77e2393bf5b0) = [RTIO\_SQE\_MEMPOOL\_BUFFER](group__rtio__sqe__flags.md#ga2802b46584220afffa0e959e149d5a4d);

523}

524

[ 525](group__rtio.md#ga9803aa829f8c0eeee746ea7d872c20cc)static inline void [rtio\_sqe\_prep\_read\_multishot](group__rtio.md#ga9803aa829f8c0eeee746ea7d872c20cc)(struct [rtio\_sqe](structrtio__sqe.md) \*sqe,

526 const struct [rtio\_iodev](structrtio__iodev.md) \*iodev, [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) prio,

527 void \*userdata)

528{

529 [rtio\_sqe\_prep\_read\_with\_pool](group__rtio.md#ga15c1f623658d27d300d1a31a6f3d6b9d)(sqe, iodev, prio, userdata);

530 sqe->[flags](structrtio__sqe.md#aad2ff8524df0e24b812e77e2393bf5b0) |= [RTIO\_SQE\_MULTISHOT](group__rtio__sqe__flags.md#ga00f8ead8f043fe40d49d0bc3325fb299);

531}

532

[ 536](group__rtio.md#gab01192577dadf7ab83d3f8029c86a149)static inline void [rtio\_sqe\_prep\_write](group__rtio.md#gab01192577dadf7ab83d3f8029c86a149)(struct [rtio\_sqe](structrtio__sqe.md) \*sqe,

537 const struct [rtio\_iodev](structrtio__iodev.md) \*iodev,

538 [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) prio,

539 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf,

540 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) len,

541 void \*userdata)

542{

543 [memset](string_8h.md#a4137694174d4ca2fad886a1db355015c)(sqe, 0, sizeof(struct [rtio\_sqe](structrtio__sqe.md)));

544 sqe->[op](structrtio__sqe.md#a1d8d3e3426e47a2c7f54d98f51acd953) = [RTIO\_OP\_TX](group__rtio.md#ga8dcaef0cda159e16520a95543ff62827);

545 sqe->[prio](structrtio__sqe.md#a528eb9b721be7b8a8898ab16a7e2d9a7) = prio;

546 sqe->[iodev](structrtio__sqe.md#a6c784702f011592c84feacd57915bbfc) = iodev;

547 sqe->[buf\_len](structrtio__sqe.md#a67376f40a13960b152a23da250275722) = len;

548 sqe->[buf](structrtio__sqe.md#a55e98f27b26393fee8e179b7bdb6a52e) = buf;

549 sqe->[userdata](structrtio__sqe.md#a0ed519ee0b5867ff73bdaf37f983c971) = userdata;

550}

551

[ 562](group__rtio.md#ga31be14ece09e061a8d42ca8f2395286a)static inline void [rtio\_sqe\_prep\_tiny\_write](group__rtio.md#ga31be14ece09e061a8d42ca8f2395286a)(struct [rtio\_sqe](structrtio__sqe.md) \*sqe,

563 const struct [rtio\_iodev](structrtio__iodev.md) \*iodev,

564 [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) prio,

565 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*tiny\_write\_data,

566 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) tiny\_write\_len,

567 void \*userdata)

568{

569 \_\_ASSERT\_NO\_MSG(tiny\_write\_len <= sizeof(sqe->[tiny\_buf](structrtio__sqe.md#aceaa9999b86fd271321988e257aeecc8)));

570

571 [memset](string_8h.md#a4137694174d4ca2fad886a1db355015c)(sqe, 0, sizeof(struct [rtio\_sqe](structrtio__sqe.md)));

572 sqe->[op](structrtio__sqe.md#a1d8d3e3426e47a2c7f54d98f51acd953) = [RTIO\_OP\_TINY\_TX](group__rtio.md#ga6f95c0a5fbcc020a0d1102d3b08934bd);

573 sqe->[prio](structrtio__sqe.md#a528eb9b721be7b8a8898ab16a7e2d9a7) = prio;

574 sqe->[iodev](structrtio__sqe.md#a6c784702f011592c84feacd57915bbfc) = iodev;

575 sqe->[tiny\_buf\_len](structrtio__sqe.md#ab25f9d5c2e4d833d548148843a859096) = tiny\_write\_len;

576 [memcpy](string_8h.md#af0f01bffcd16daa9143f6014d10a25ad)(sqe->[tiny\_buf](structrtio__sqe.md#aceaa9999b86fd271321988e257aeecc8), tiny\_write\_data, tiny\_write\_len);

577 sqe->[userdata](structrtio__sqe.md#a0ed519ee0b5867ff73bdaf37f983c971) = userdata;

578}

579

[ 588](group__rtio.md#ga9d0dd7d0e2e3d281092f2350d6e1713e)static inline void [rtio\_sqe\_prep\_callback](group__rtio.md#ga9d0dd7d0e2e3d281092f2350d6e1713e)(struct [rtio\_sqe](structrtio__sqe.md) \*sqe,

589 [rtio\_callback\_t](group__rtio.md#gad1dbd690e6cf88d7c788436dd04d1a00) callback,

590 void \*arg0,

591 void \*userdata)

592{

593 [memset](string_8h.md#a4137694174d4ca2fad886a1db355015c)(sqe, 0, sizeof(struct [rtio\_sqe](structrtio__sqe.md)));

594 sqe->[op](structrtio__sqe.md#a1d8d3e3426e47a2c7f54d98f51acd953) = [RTIO\_OP\_CALLBACK](group__rtio.md#ga18e0ff7d44e4c33900106aefad0a8508);

595 sqe->[prio](structrtio__sqe.md#a528eb9b721be7b8a8898ab16a7e2d9a7) = 0;

596 sqe->[iodev](structrtio__sqe.md#a6c784702f011592c84feacd57915bbfc) = NULL;

597 sqe->[callback](structrtio__sqe.md#af8c31c33e9fedebe55cac73595d0f696) = callback;

598 sqe->[arg0](structrtio__sqe.md#a438d2156a61aef9ca840af9c01d5dfa4) = arg0;

599 sqe->[userdata](structrtio__sqe.md#a0ed519ee0b5867ff73bdaf37f983c971) = userdata;

600}

601

[ 605](group__rtio.md#ga0129e02abc85526199311846e1830869)static inline void [rtio\_sqe\_prep\_transceive](group__rtio.md#ga0129e02abc85526199311846e1830869)(struct [rtio\_sqe](structrtio__sqe.md) \*sqe,

606 const struct [rtio\_iodev](structrtio__iodev.md) \*iodev,

607 [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) prio,

608 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*tx\_buf,

609 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*rx\_buf,

610 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) buf\_len,

611 void \*userdata)

612{

613 [memset](string_8h.md#a4137694174d4ca2fad886a1db355015c)(sqe, 0, sizeof(struct [rtio\_sqe](structrtio__sqe.md)));

614 sqe->[op](structrtio__sqe.md#a1d8d3e3426e47a2c7f54d98f51acd953) = [RTIO\_OP\_TXRX](group__rtio.md#ga9f0e70f5a28be65a8ed67c0257a72692);

615 sqe->[prio](structrtio__sqe.md#a528eb9b721be7b8a8898ab16a7e2d9a7) = prio;

616 sqe->[iodev](structrtio__sqe.md#a6c784702f011592c84feacd57915bbfc) = iodev;

617 sqe->[txrx\_buf\_len](structrtio__sqe.md#ab3cff3dbbfc9b1a0dbe8f1dc28ac83f8) = buf\_len;

618 sqe->[tx\_buf](structrtio__sqe.md#a186c22217961a5eddb75ad0bd84a538a) = tx\_buf;

619 sqe->[rx\_buf](structrtio__sqe.md#a4d2090fc11b897724a883ad1087d9f73) = rx\_buf;

620 sqe->[userdata](structrtio__sqe.md#a0ed519ee0b5867ff73bdaf37f983c971) = userdata;

621}

622

[ 623](group__rtio.md#gae5fb03fc8f3a4a774f476ff552999bfc)static inline struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \*[rtio\_sqe\_pool\_alloc](group__rtio.md#gae5fb03fc8f3a4a774f476ff552999bfc)(struct [rtio\_sqe\_pool](structrtio__sqe__pool.md) \*pool)

624{

625 struct [mpsc\_node](structmpsc__node.md) \*node = [mpsc\_pop](group__mpsc__lockfree.md#ga823ec37b84ac43e46167aac954bce9d7)(&pool->[free\_q](structrtio__sqe__pool.md#aed49ea25c952e07a8287919268fd2485));

626

627 if (node == NULL) {

628 return NULL;

629 }

630

631 struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \*iodev\_sqe = [CONTAINER\_OF](group__sys-util.md#gac5bc561d1bfd1bf68877fe577779bd2f)(node, struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md), [q](structrtio__iodev__sqe.md#a9cfdd004b65a5e2bc111bc2fb333498c));

632

633 pool->[pool\_free](structrtio__sqe__pool.md#af7990b1510ad2343573f3e4e502475b0)--;

634

635 return iodev\_sqe;

636}

637

[ 638](group__rtio.md#gac776aea3692cfd77aa5bf675a9e9ed02)static inline void [rtio\_sqe\_pool\_free](group__rtio.md#gac776aea3692cfd77aa5bf675a9e9ed02)(struct [rtio\_sqe\_pool](structrtio__sqe__pool.md) \*pool, struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \*iodev\_sqe)

639{

640 [mpsc\_push](group__mpsc__lockfree.md#ga403add133841ef88e10d74141e782b37)(&pool->[free\_q](structrtio__sqe__pool.md#aed49ea25c952e07a8287919268fd2485), &iodev\_sqe->[q](structrtio__iodev__sqe.md#a9cfdd004b65a5e2bc111bc2fb333498c));

641

642 pool->[pool\_free](structrtio__sqe__pool.md#af7990b1510ad2343573f3e4e502475b0)++;

643}

644

[ 645](group__rtio.md#ga8497170f55af1d11d717e919f61806f5)static inline struct [rtio\_cqe](structrtio__cqe.md) \*[rtio\_cqe\_pool\_alloc](group__rtio.md#ga8497170f55af1d11d717e919f61806f5)(struct [rtio\_cqe\_pool](structrtio__cqe__pool.md) \*pool)

646{

647 struct [mpsc\_node](structmpsc__node.md) \*node = [mpsc\_pop](group__mpsc__lockfree.md#ga823ec37b84ac43e46167aac954bce9d7)(&pool->[free\_q](structrtio__cqe__pool.md#a13bd7991ff5622c1cb5aa6af014aaab3));

648

649 if (node == NULL) {

650 return NULL;

651 }

652

653 struct [rtio\_cqe](structrtio__cqe.md) \*cqe = [CONTAINER\_OF](group__sys-util.md#gac5bc561d1bfd1bf68877fe577779bd2f)(node, struct [rtio\_cqe](structrtio__cqe.md), [q](structrtio__cqe.md#a27272bca31c170f406799633ec82098d));

654

655 [memset](string_8h.md#a4137694174d4ca2fad886a1db355015c)(cqe, 0, sizeof(struct [rtio\_cqe](structrtio__cqe.md)));

656

657 pool->[pool\_free](structrtio__cqe__pool.md#a4fb501a0ba15e2956113deaf4597d846)--;

658

659 return cqe;

660}

661

[ 662](group__rtio.md#ga23c0c5d4b551858eabe057ecb8a28d12)static inline void [rtio\_cqe\_pool\_free](group__rtio.md#ga23c0c5d4b551858eabe057ecb8a28d12)(struct [rtio\_cqe\_pool](structrtio__cqe__pool.md) \*pool, struct [rtio\_cqe](structrtio__cqe.md) \*cqe)

663{

664 [mpsc\_push](group__mpsc__lockfree.md#ga403add133841ef88e10d74141e782b37)(&pool->[free\_q](structrtio__cqe__pool.md#a13bd7991ff5622c1cb5aa6af014aaab3), &cqe->[q](structrtio__cqe.md#a27272bca31c170f406799633ec82098d));

665

666 pool->[pool\_free](structrtio__cqe__pool.md#a4fb501a0ba15e2956113deaf4597d846)++;

667}

668

[ 669](group__rtio.md#ga7f14b99fc1dd0697309e7f71a270f5fb)static inline int [rtio\_block\_pool\_alloc](group__rtio.md#ga7f14b99fc1dd0697309e7f71a270f5fb)(struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2), size\_t min\_sz,

670 size\_t max\_sz, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\*buf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*buf\_len)

671{

672#ifndef CONFIG\_RTIO\_SYS\_MEM\_BLOCKS

673 ARG\_UNUSED([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2));

674 ARG\_UNUSED(min\_sz);

675 ARG\_UNUSED(max\_sz);

676 ARG\_UNUSED(buf);

677 ARG\_UNUSED(buf\_len);

678 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

679#else

680 const [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size = [rtio\_mempool\_block\_size](group__rtio.md#ga4213be028b0a1264daaa0d30c4c2d089)([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2));

681 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) bytes = max\_sz;

682

683 /\* Not every context has a block pool and the block size may return 0 in

684 \* that case

685 \*/

686 if (block\_size == 0) {

687 return -[ENOMEM](group__system__errno.md#ga6a05c923dad0c1208043e9c20a58c8e5);

688 }

689

690 do {

691 size\_t num\_blks = [DIV\_ROUND\_UP](group__sys-util.md#gae664e7492e37d324831caf2321ddda37)(bytes, block\_size);

692 int rc = [sys\_mem\_blocks\_alloc\_contiguous](group__mem__blocks__apis.md#ga72614d0c120f40209837b77d0333bb23)([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->block\_pool, num\_blks, (void \*\*)buf);

693

694 if (rc == 0) {

695 \*buf\_len = num\_blks \* block\_size;

696 return 0;

697 }

698

699 bytes -= block\_size;

700 } while (bytes >= min\_sz);

701

702 return -[ENOMEM](group__system__errno.md#ga6a05c923dad0c1208043e9c20a58c8e5);

703#endif

704}

705

[ 706](group__rtio.md#gafca7732926a9a7c080e3cb16e5f16108)static inline void [rtio\_block\_pool\_free](group__rtio.md#gafca7732926a9a7c080e3cb16e5f16108)(struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2), void \*buf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) buf\_len)

707{

708#ifndef CONFIG\_RTIO\_SYS\_MEM\_BLOCKS

709 ARG\_UNUSED([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2));

710 ARG\_UNUSED(buf);

711 ARG\_UNUSED(buf\_len);

712#else

713 size\_t num\_blks = buf\_len >> [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->block\_pool->info.blk\_sz\_shift;

714

715 [sys\_mem\_blocks\_free\_contiguous](group__mem__blocks__apis.md#ga39e7f8dfe3bda8eabc2372f9a1e87342)([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->block\_pool, buf, num\_blks);

716#endif

717}

718

719/\* Do not try and reformat the macros \*/

720/\* clang-format off \*/

721

[ 729](group__rtio.md#gaae51e2a679d37bc1cfba79961688c406)#define RTIO\_IODEV\_DEFINE(name, iodev\_api, iodev\_data) \

730 STRUCT\_SECTION\_ITERABLE(rtio\_iodev, name) = { \

731 .api = (iodev\_api), \

732 .data = (iodev\_data), \

733 }

734

735#define Z\_RTIO\_SQE\_POOL\_DEFINE(name, sz) \

736 static struct rtio\_iodev\_sqe CONCAT(\_sqe\_pool\_, name)[sz]; \

737 STRUCT\_SECTION\_ITERABLE(rtio\_sqe\_pool, name) = { \

738 .free\_q = MPSC\_INIT((name.free\_q)), \

739 .pool\_size = sz, \

740 .pool\_free = sz, \

741 .pool = CONCAT(\_sqe\_pool\_, name), \

742 }

743

744

745#define Z\_RTIO\_CQE\_POOL\_DEFINE(name, sz) \

746 static struct rtio\_cqe CONCAT(\_cqe\_pool\_, name)[sz]; \

747 STRUCT\_SECTION\_ITERABLE(rtio\_cqe\_pool, name) = { \

748 .free\_q = MPSC\_INIT((name.free\_q)), \

749 .pool\_size = sz, \

750 .pool\_free = sz, \

751 .pool = CONCAT(\_cqe\_pool\_, name), \

752 }

753

[ 763](group__rtio.md#ga2437af5061e078950d4a55211d9a902f)#define RTIO\_BMEM COND\_CODE\_1(CONFIG\_USERSPACE, (K\_APP\_BMEM(rtio\_partition) static), (static))

764

[ 774](group__rtio.md#ga3b569c01b71e126cff852df50e98fd69)#define RTIO\_DMEM COND\_CODE\_1(CONFIG\_USERSPACE, (K\_APP\_DMEM(rtio\_partition) static), (static))

775

776#define Z\_RTIO\_BLOCK\_POOL\_DEFINE(name, blk\_sz, blk\_cnt, blk\_align) \

777 RTIO\_BMEM uint8\_t \_\_aligned(WB\_UP(blk\_align)) \

778 CONCAT(\_block\_pool\_, name)[blk\_cnt\*WB\_UP(blk\_sz)]; \

779 \_SYS\_MEM\_BLOCKS\_DEFINE\_WITH\_EXT\_BUF(name, WB\_UP(blk\_sz), blk\_cnt, \

780 CONCAT(\_block\_pool\_, name), RTIO\_DMEM)

781

782#define Z\_RTIO\_DEFINE(name, \_sqe\_pool, \_cqe\_pool, \_block\_pool) \

783 IF\_ENABLED(CONFIG\_RTIO\_SUBMIT\_SEM, \

784 (static K\_SEM\_DEFINE(CONCAT(\_submit\_sem\_, name), 0, K\_SEM\_MAX\_LIMIT))) \

785 IF\_ENABLED(CONFIG\_RTIO\_CONSUME\_SEM, \

786 (static K\_SEM\_DEFINE(CONCAT(\_consume\_sem\_, name), 0, K\_SEM\_MAX\_LIMIT))) \

787 STRUCT\_SECTION\_ITERABLE(rtio, name) = { \

788 IF\_ENABLED(CONFIG\_RTIO\_SUBMIT\_SEM, (.submit\_sem = &CONCAT(\_submit\_sem\_, name),)) \

789 IF\_ENABLED(CONFIG\_RTIO\_SUBMIT\_SEM, (.submit\_count = 0,)) \

790 IF\_ENABLED(CONFIG\_RTIO\_CONSUME\_SEM, (.consume\_sem = &CONCAT(\_consume\_sem\_, name),))\

791 .cq\_count = ATOMIC\_INIT(0), \

792 .xcqcnt = ATOMIC\_INIT(0), \

793 .sqe\_pool = \_sqe\_pool, \

794 .cqe\_pool = \_cqe\_pool, \

795 IF\_ENABLED(CONFIG\_RTIO\_SYS\_MEM\_BLOCKS, (.block\_pool = \_block\_pool,)) \

796 .sq = MPSC\_INIT((name.sq)), \

797 .cq = MPSC\_INIT((name.cq)), \

798 }

799

[ 807](group__rtio.md#ga338df088eabf3b8f7fefb4ac517b21d4)#define RTIO\_DEFINE(name, sq\_sz, cq\_sz) \

808 Z\_RTIO\_SQE\_POOL\_DEFINE(CONCAT(name, \_sqe\_pool), sq\_sz); \

809 Z\_RTIO\_CQE\_POOL\_DEFINE(CONCAT(name, \_cqe\_pool), cq\_sz); \

810 Z\_RTIO\_DEFINE(name, &CONCAT(name, \_sqe\_pool), \

811 &CONCAT(name, \_cqe\_pool), NULL)

812

813/\* clang-format on \*/

814

[ 825](group__rtio.md#gae4c2a9384a9ae4ed16dff914b1184ca8)#define RTIO\_DEFINE\_WITH\_MEMPOOL(name, sq\_sz, cq\_sz, num\_blks, blk\_size, balign) \

826 Z\_RTIO\_SQE\_POOL\_DEFINE(name##\_sqe\_pool, sq\_sz); \

827 Z\_RTIO\_CQE\_POOL\_DEFINE(name##\_cqe\_pool, cq\_sz); \

828 Z\_RTIO\_BLOCK\_POOL\_DEFINE(name##\_block\_pool, blk\_size, num\_blks, balign); \

829 Z\_RTIO\_DEFINE(name, &name##\_sqe\_pool, &name##\_cqe\_pool, &name##\_block\_pool)

830

831/\* clang-format on \*/

832

[ 840](group__rtio.md#ga1f4fb7bccbaae08a94387e4b11275a78)static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [rtio\_sqe\_acquirable](group__rtio.md#ga1f4fb7bccbaae08a94387e4b11275a78)(struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2))

841{

842 return [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->sqe\_pool->pool\_free;

843}

844

[ 853](group__rtio.md#gaef904eb6a8810d8c3ea537c4d6edbee5)static inline struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \*[rtio\_txn\_next](group__rtio.md#gaef904eb6a8810d8c3ea537c4d6edbee5)(const struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \*iodev\_sqe)

854{

855 if (iodev\_sqe->[sqe](structrtio__iodev__sqe.md#a2bd98599678909c0ddb22f879affa12b).[flags](structrtio__sqe.md#aad2ff8524df0e24b812e77e2393bf5b0) & [RTIO\_SQE\_TRANSACTION](group__rtio__sqe__flags.md#ga07f09cc0c95be6cfdddb23f8acacb1ea)) {

856 return iodev\_sqe->[next](structrtio__iodev__sqe.md#a2afb82e550e614f87db7cd1bf2c3a352);

857 } else {

858 return NULL;

859 }

860}

861

862

[ 871](group__rtio.md#gada1e3abf92a46e376138435debc8baf4)static inline struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \*[rtio\_chain\_next](group__rtio.md#gada1e3abf92a46e376138435debc8baf4)(const struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \*iodev\_sqe)

872{

873 if (iodev\_sqe->[sqe](structrtio__iodev__sqe.md#a2bd98599678909c0ddb22f879affa12b).[flags](structrtio__sqe.md#aad2ff8524df0e24b812e77e2393bf5b0) & [RTIO\_SQE\_CHAINED](group__rtio__sqe__flags.md#gae9191d521d4ab602b53fefb74020d06b)) {

874 return iodev\_sqe->[next](structrtio__iodev__sqe.md#a2afb82e550e614f87db7cd1bf2c3a352);

875 } else {

876 return NULL;

877 }

878}

879

[ 888](group__rtio.md#gae690e3dc0fc40dda57257b2eed432719)static inline struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \*[rtio\_iodev\_sqe\_next](group__rtio.md#gae690e3dc0fc40dda57257b2eed432719)(const struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \*iodev\_sqe)

889{

890 return iodev\_sqe->[next](structrtio__iodev__sqe.md#a2afb82e550e614f87db7cd1bf2c3a352);

891}

892

[ 901](group__rtio.md#ga8b47c954d15a334621def53acceb6799)static inline struct [rtio\_sqe](structrtio__sqe.md) \*[rtio\_sqe\_acquire](group__rtio.md#ga8b47c954d15a334621def53acceb6799)(struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2))

902{

903 struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \*iodev\_sqe = [rtio\_sqe\_pool\_alloc](group__rtio.md#gae5fb03fc8f3a4a774f476ff552999bfc)([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->sqe\_pool);

904

905 if (iodev\_sqe == NULL) {

906 return NULL;

907 }

908

909 [mpsc\_push](group__mpsc__lockfree.md#ga403add133841ef88e10d74141e782b37)(&[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->sq, &iodev\_sqe->[q](structrtio__iodev__sqe.md#a9cfdd004b65a5e2bc111bc2fb333498c));

910

911 return &iodev\_sqe->[sqe](structrtio__iodev__sqe.md#a2bd98599678909c0ddb22f879affa12b);

912}

913

[ 919](group__rtio.md#ga9486fb7b50e8d2409a50da235203536b)static inline void [rtio\_sqe\_drop\_all](group__rtio.md#ga9486fb7b50e8d2409a50da235203536b)(struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2))

920{

921 struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \*iodev\_sqe;

922 struct [mpsc\_node](structmpsc__node.md) \*node = [mpsc\_pop](group__mpsc__lockfree.md#ga823ec37b84ac43e46167aac954bce9d7)(&[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->sq);

923

924 while (node != NULL) {

925 iodev\_sqe = [CONTAINER\_OF](group__sys-util.md#gac5bc561d1bfd1bf68877fe577779bd2f)(node, struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md), q);

926 [rtio\_sqe\_pool\_free](group__rtio.md#gac776aea3692cfd77aa5bf675a9e9ed02)([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->sqe\_pool, iodev\_sqe);

927 node = [mpsc\_pop](group__mpsc__lockfree.md#ga823ec37b84ac43e46167aac954bce9d7)(&[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->sq);

928 }

929}

930

[ 934](group__rtio.md#gad848646651fdf3649b882e5268f72a3c)static inline struct [rtio\_cqe](structrtio__cqe.md) \*[rtio\_cqe\_acquire](group__rtio.md#gad848646651fdf3649b882e5268f72a3c)(struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2))

935{

936 struct [rtio\_cqe](structrtio__cqe.md) \*cqe = [rtio\_cqe\_pool\_alloc](group__rtio.md#ga8497170f55af1d11d717e919f61806f5)([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->cqe\_pool);

937

938 if (cqe == NULL) {

939 return NULL;

940 }

941

942 [memset](string_8h.md#a4137694174d4ca2fad886a1db355015c)(cqe, 0, sizeof(struct [rtio\_cqe](structrtio__cqe.md)));

943

944 return cqe;

945}

946

[ 950](group__rtio.md#ga6f55202adeca60aed0343a7a0dcab071)static inline void [rtio\_cqe\_produce](group__rtio.md#ga6f55202adeca60aed0343a7a0dcab071)(struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2), struct [rtio\_cqe](structrtio__cqe.md) \*cqe)

951{

952 [mpsc\_push](group__mpsc__lockfree.md#ga403add133841ef88e10d74141e782b37)(&[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->cq, &cqe->[q](structrtio__cqe.md#a27272bca31c170f406799633ec82098d));

953}

954

[ 966](group__rtio.md#gae562cf241911804cdb9f4e3a73b53df4)static inline struct [rtio\_cqe](structrtio__cqe.md) \*[rtio\_cqe\_consume](group__rtio.md#gae562cf241911804cdb9f4e3a73b53df4)(struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2))

967{

968 struct [mpsc\_node](structmpsc__node.md) \*node;

969 struct [rtio\_cqe](structrtio__cqe.md) \*cqe = NULL;

970

971#ifdef CONFIG\_RTIO\_CONSUME\_SEM

972 if ([k\_sem\_take](group__semaphore__apis.md#gac71e2383c1920dddc45a561cacfef090)([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->consume\_sem, [K\_NO\_WAIT](group__clock__apis.md#ga3d9541cfe2e8395af66d186efa77362f)) != 0) {

973 return NULL;

974 }

975#endif

976

977 node = [mpsc\_pop](group__mpsc__lockfree.md#ga823ec37b84ac43e46167aac954bce9d7)(&[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->cq);

978 if (node == NULL) {

979 return NULL;

980 }

981 cqe = [CONTAINER\_OF](group__sys-util.md#gac5bc561d1bfd1bf68877fe577779bd2f)(node, struct [rtio\_cqe](structrtio__cqe.md), [q](structrtio__cqe.md#a27272bca31c170f406799633ec82098d));

982

983 return cqe;

984}

985

[ 996](group__rtio.md#gaf617d05d9b59ce1f1d0697617ef6f249)static inline struct [rtio\_cqe](structrtio__cqe.md) \*[rtio\_cqe\_consume\_block](group__rtio.md#gaf617d05d9b59ce1f1d0697617ef6f249)(struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2))

997{

998 struct [mpsc\_node](structmpsc__node.md) \*node;

999 struct [rtio\_cqe](structrtio__cqe.md) \*cqe;

1000

1001#ifdef CONFIG\_RTIO\_CONSUME\_SEM

1002 [k\_sem\_take](group__semaphore__apis.md#gac71e2383c1920dddc45a561cacfef090)([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->consume\_sem, [K\_FOREVER](group__clock__apis.md#ga0bb4b83f0222193b21a8910311bab0ca));

1003#endif

1004 node = [mpsc\_pop](group__mpsc__lockfree.md#ga823ec37b84ac43e46167aac954bce9d7)(&[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->cq);

1005 while (node == NULL) {

1006 Z\_SPIN\_DELAY(1);

1007 node = [mpsc\_pop](group__mpsc__lockfree.md#ga823ec37b84ac43e46167aac954bce9d7)(&[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->cq);

1008 }

1009 cqe = [CONTAINER\_OF](group__sys-util.md#gac5bc561d1bfd1bf68877fe577779bd2f)(node, struct [rtio\_cqe](structrtio__cqe.md), [q](structrtio__cqe.md#a27272bca31c170f406799633ec82098d));

1010

1011 return cqe;

1012}

1013

[ 1020](group__rtio.md#gaa0799a5f8ad98425d385a07c5d27d9cb)static inline void [rtio\_cqe\_release](group__rtio.md#gaa0799a5f8ad98425d385a07c5d27d9cb)(struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2), struct [rtio\_cqe](structrtio__cqe.md) \*cqe)

1021{

1022 [rtio\_cqe\_pool\_free](group__rtio.md#ga23c0c5d4b551858eabe057ecb8a28d12)([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->cqe\_pool, cqe);

1023}

1024

[ 1031](group__rtio.md#ga75661c8c6c94a0ac6254cec674b478c8)static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [rtio\_cqe\_compute\_flags](group__rtio.md#ga75661c8c6c94a0ac6254cec674b478c8)(struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \*iodev\_sqe)

1032{

1033 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) = 0;

1034

1035#ifdef CONFIG\_RTIO\_SYS\_MEM\_BLOCKS

1036 if (iodev\_sqe->[sqe](structrtio__iodev__sqe.md#a2bd98599678909c0ddb22f879affa12b).[op](structrtio__sqe.md#a1d8d3e3426e47a2c7f54d98f51acd953) == [RTIO\_OP\_RX](group__rtio.md#gafeb05c351207cd1638fa78f6607e1a4a) && iodev\_sqe->[sqe](structrtio__iodev__sqe.md#a2bd98599678909c0ddb22f879affa12b).[flags](structrtio__sqe.md#aad2ff8524df0e24b812e77e2393bf5b0) & [RTIO\_SQE\_MEMPOOL\_BUFFER](group__rtio__sqe__flags.md#ga2802b46584220afffa0e959e149d5a4d)) {

1037 struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) = iodev\_sqe->[r](structrtio__iodev__sqe.md#a3c3a050793589258eab5ff5ac30f24c8);

1038 struct sys\_mem\_blocks \*mem\_pool = [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->block\_pool;

1039 int blk\_index = (iodev\_sqe->[sqe](structrtio__iodev__sqe.md#a2bd98599678909c0ddb22f879affa12b).[buf](structrtio__sqe.md#a55e98f27b26393fee8e179b7bdb6a52e) - mem\_pool->buffer) >>

1040 mem\_pool->info.blk\_sz\_shift;

1041 int blk\_count = iodev\_sqe->[sqe](structrtio__iodev__sqe.md#a2bd98599678909c0ddb22f879affa12b).[buf\_len](structrtio__sqe.md#a67376f40a13960b152a23da250275722) >> mem\_pool->info.blk\_sz\_shift;

1042

1043 [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) = [RTIO\_CQE\_FLAG\_PREP\_MEMPOOL](group__rtio__cqe__flags.md#ga28b3a5661248b6b3763aab47417114d6)(blk\_index, blk\_count);

1044 }

1045#else

1046 ARG\_UNUSED(iodev\_sqe);

1047#endif

1048

1049 return [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9);

1050}

1051

[ 1067](group__rtio.md#gaedbf9386a36ed99baa290ef6c318ded1)\_\_syscall int [rtio\_cqe\_get\_mempool\_buffer](group__rtio.md#gaedbf9386a36ed99baa290ef6c318ded1)(const struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2), struct [rtio\_cqe](structrtio__cqe.md) \*cqe,

1068 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\*buff, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*buff\_len);

1069

1070static inline int z\_impl\_rtio\_cqe\_get\_mempool\_buffer(const struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2), struct [rtio\_cqe](structrtio__cqe.md) \*cqe,

1071 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\*buff, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*buff\_len)

1072{

1073#ifdef CONFIG\_RTIO\_SYS\_MEM\_BLOCKS

1074 if ([RTIO\_CQE\_FLAG\_GET](group__rtio__cqe__flags.md#gaef64ea020a20ac22a0edcb6eca032efc)(cqe->[flags](structrtio__cqe.md#a8a7632ef1cfd31529d782bd761908d93)) == [RTIO\_CQE\_FLAG\_MEMPOOL\_BUFFER](group__rtio__cqe__flags.md#ga0f212500447a5e37e225a6997953b609)) {

1075 int blk\_idx = [RTIO\_CQE\_FLAG\_MEMPOOL\_GET\_BLK\_IDX](group__rtio__cqe__flags.md#ga0b5f3f7e7be472ecf87bd2b08c1888da)(cqe->[flags](structrtio__cqe.md#a8a7632ef1cfd31529d782bd761908d93));

1076 int blk\_count = [RTIO\_CQE\_FLAG\_MEMPOOL\_GET\_BLK\_CNT](group__rtio__cqe__flags.md#ga087465f866d417d5332602bb582cc1a7)(cqe->[flags](structrtio__cqe.md#a8a7632ef1cfd31529d782bd761908d93));

1077 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) blk\_size = [rtio\_mempool\_block\_size](group__rtio.md#ga4213be028b0a1264daaa0d30c4c2d089)([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2));

1078

1079 \*buff = [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->block\_pool->buffer + blk\_idx \* blk\_size;

1080 \*buff\_len = blk\_count \* blk\_size;

1081 \_\_ASSERT\_NO\_MSG(\*buff >= [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->block\_pool->buffer);

1082 \_\_ASSERT\_NO\_MSG(\*buff <

1083 [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->block\_pool->buffer + blk\_size \* [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->block\_pool->info.num\_blocks);

1084 return 0;

1085 }

1086 return -[EINVAL](group__system__errno.md#ga2d1678d5a7cc8ce499643f3b8957def4);

1087#else

1088 ARG\_UNUSED([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2));

1089 ARG\_UNUSED(cqe);

1090 ARG\_UNUSED(buff);

1091 ARG\_UNUSED(buff\_len);

1092

1093 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

1094#endif

1095}

1096

[ 1097](group__rtio.md#gaf191153e83de72ddefb998daad02fa16)void [rtio\_executor\_submit](group__rtio.md#gaf191153e83de72ddefb998daad02fa16)(struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2));

[ 1098](group__rtio.md#ga7e2ebd9abaf585207bc5b99c5d815c6a)void [rtio\_executor\_ok](group__rtio.md#ga7e2ebd9abaf585207bc5b99c5d815c6a)(struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \*iodev\_sqe, int result);

[ 1099](group__rtio.md#ga15f4a1a4dfb869ef9e4216dc1c1cdc8a)void [rtio\_executor\_err](group__rtio.md#ga15f4a1a4dfb869ef9e4216dc1c1cdc8a)(struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \*iodev\_sqe, int result);

1100

[ 1109](group__rtio.md#gacb1d2ffa2b07418d8a8aa319bd4336ab)static inline void [rtio\_iodev\_sqe\_ok](group__rtio.md#gacb1d2ffa2b07418d8a8aa319bd4336ab)(struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \*iodev\_sqe, int result)

1110{

1111 [rtio\_executor\_ok](group__rtio.md#ga7e2ebd9abaf585207bc5b99c5d815c6a)(iodev\_sqe, result);

1112}

1113

[ 1122](group__rtio.md#gaada07aa6acefa548743b525225fa482f)static inline void [rtio\_iodev\_sqe\_err](group__rtio.md#gaada07aa6acefa548743b525225fa482f)(struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \*iodev\_sqe, int result)

1123{

1124 [rtio\_executor\_err](group__rtio.md#ga15f4a1a4dfb869ef9e4216dc1c1cdc8a)(iodev\_sqe, result);

1125}

1126

[ 1138](group__rtio.md#ga4abc221d5a90ab882000a72caa0ebd0f)static inline void [rtio\_cqe\_submit](group__rtio.md#ga4abc221d5a90ab882000a72caa0ebd0f)(struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2), int result, void \*userdata, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9))

1139{

1140 struct [rtio\_cqe](structrtio__cqe.md) \*cqe = [rtio\_cqe\_acquire](group__rtio.md#gad848646651fdf3649b882e5268f72a3c)([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2));

1141

1142 if (cqe == NULL) {

1143 [atomic\_inc](group__atomic__apis.md#gaae47a9cbe5a6534967b417f602b37ac2)(&[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->xcqcnt);

1144 } else {

1145 cqe->[result](structrtio__cqe.md#acbe2e6607a752b676d9336b9ca6ce435) = [result](structrtio__cqe.md#acbe2e6607a752b676d9336b9ca6ce435);

1146 cqe->[userdata](structrtio__cqe.md#a15128387ccbea55812ef229eab7241e7) = [userdata](structrtio__cqe.md#a15128387ccbea55812ef229eab7241e7);

1147 cqe->[flags](structrtio__cqe.md#a8a7632ef1cfd31529d782bd761908d93) = [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9);

1148 [rtio\_cqe\_produce](group__rtio.md#ga6f55202adeca60aed0343a7a0dcab071)([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2), cqe);

1149 }

1150

1151 [atomic\_inc](group__atomic__apis.md#gaae47a9cbe5a6534967b417f602b37ac2)(&[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->cq\_count);

1152#ifdef CONFIG\_RTIO\_SUBMIT\_SEM

1153 if ([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->submit\_count > 0) {

1154 [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->submit\_count--;

1155 if ([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->submit\_count == 0) {

1156 [k\_sem\_give](group__semaphore__apis.md#gab9be3cf1988af2cd6afdace52d497c84)([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->submit\_sem);

1157 }

1158 }

1159#endif

1160#ifdef CONFIG\_RTIO\_CONSUME\_SEM

1161 [k\_sem\_give](group__semaphore__apis.md#gab9be3cf1988af2cd6afdace52d497c84)([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->consume\_sem);

1162#endif

1163}

1164

1165#define \_\_RTIO\_MEMPOOL\_GET\_NUM\_BLKS(num\_bytes, blk\_size) (((num\_bytes) + (blk\_size)-1) / (blk\_size))

1166

[ 1179](group__rtio.md#gaab6843e2038d00a8354f57d7e2ffcf7e)static inline int [rtio\_sqe\_rx\_buf](group__rtio.md#gaab6843e2038d00a8354f57d7e2ffcf7e)(const struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \*iodev\_sqe, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) min\_buf\_len,

1180 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) max\_buf\_len, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\*buf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*buf\_len)

1181{

1182 struct [rtio\_sqe](structrtio__sqe.md) \*sqe = (struct [rtio\_sqe](structrtio__sqe.md) \*)&iodev\_sqe->[sqe](structrtio__iodev__sqe.md#a2bd98599678909c0ddb22f879affa12b);

1183

1184#ifdef CONFIG\_RTIO\_SYS\_MEM\_BLOCKS

1185 if (sqe->[op](structrtio__sqe.md#a1d8d3e3426e47a2c7f54d98f51acd953) == [RTIO\_OP\_RX](group__rtio.md#gafeb05c351207cd1638fa78f6607e1a4a) && sqe->[flags](structrtio__sqe.md#aad2ff8524df0e24b812e77e2393bf5b0) & [RTIO\_SQE\_MEMPOOL\_BUFFER](group__rtio__sqe__flags.md#ga2802b46584220afffa0e959e149d5a4d)) {

1186 struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) = iodev\_sqe->[r](structrtio__iodev__sqe.md#a3c3a050793589258eab5ff5ac30f24c8);

1187

1188 if (sqe->[buf](structrtio__sqe.md#a55e98f27b26393fee8e179b7bdb6a52e) != NULL) {

1189 if (sqe->[buf\_len](structrtio__sqe.md#a67376f40a13960b152a23da250275722) < min\_buf\_len) {

1190 return -[ENOMEM](group__system__errno.md#ga6a05c923dad0c1208043e9c20a58c8e5);

1191 }

1192 \*buf = sqe->[buf](structrtio__sqe.md#a55e98f27b26393fee8e179b7bdb6a52e);

1193 \*buf\_len = sqe->[buf\_len](structrtio__sqe.md#a67376f40a13960b152a23da250275722);

1194 return 0;

1195 }

1196

1197 int rc = [rtio\_block\_pool\_alloc](group__rtio.md#ga7f14b99fc1dd0697309e7f71a270f5fb)([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2), min\_buf\_len, max\_buf\_len, buf, buf\_len);

1198 if (rc == 0) {

1199 sqe->[buf](structrtio__sqe.md#a55e98f27b26393fee8e179b7bdb6a52e) = \*buf;

1200 sqe->[buf\_len](structrtio__sqe.md#a67376f40a13960b152a23da250275722) = \*buf\_len;

1201 return 0;

1202 }

1203

1204 return -[ENOMEM](group__system__errno.md#ga6a05c923dad0c1208043e9c20a58c8e5);

1205 }

1206#else

1207 ARG\_UNUSED(max\_buf\_len);

1208#endif

1209

1210 if (sqe->[buf\_len](structrtio__sqe.md#a67376f40a13960b152a23da250275722) < min\_buf\_len) {

1211 return -[ENOMEM](group__system__errno.md#ga6a05c923dad0c1208043e9c20a58c8e5);

1212 }

1213

1214 \*buf = sqe->[buf](structrtio__sqe.md#a55e98f27b26393fee8e179b7bdb6a52e);

1215 \*buf\_len = sqe->[buf\_len](structrtio__sqe.md#a67376f40a13960b152a23da250275722);

1216 return 0;

1217}

1218

[ 1233](group__rtio.md#ga6530bf56ccbab046a362a6448f941609)\_\_syscall void [rtio\_release\_buffer](group__rtio.md#ga6530bf56ccbab046a362a6448f941609)(struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2), void \*buff, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) buff\_len);

1234

1235static inline void z\_impl\_rtio\_release\_buffer(struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2), void \*buff, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) buff\_len)

1236{

1237#ifdef CONFIG\_RTIO\_SYS\_MEM\_BLOCKS

1238 if ([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) == NULL || buff == NULL || [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->block\_pool == NULL || buff\_len == 0) {

1239 return;

1240 }

1241

1242 [rtio\_block\_pool\_free](group__rtio.md#gafca7732926a9a7c080e3cb16e5f16108)([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2), buff, buff\_len);

1243#else

1244 ARG\_UNUSED([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2));

1245 ARG\_UNUSED(buff);

1246 ARG\_UNUSED(buff\_len);

1247#endif

1248}

1249

[ 1253](group__rtio.md#ga9da42c98546930575525f0f92710f9e4)static inline void [rtio\_access\_grant](group__rtio.md#ga9da42c98546930575525f0f92710f9e4)(struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2), struct [k\_thread](structk__thread.md) \*t)

1254{

1255 [k\_object\_access\_grant](group__usermode__apis.md#ga94087bedf96fe2a2bea437d3d585ca22)([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2), t);

1256

1257#ifdef CONFIG\_RTIO\_SUBMIT\_SEM

1258 [k\_object\_access\_grant](group__usermode__apis.md#ga94087bedf96fe2a2bea437d3d585ca22)([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->submit\_sem, t);

1259#endif

1260

1261#ifdef CONFIG\_RTIO\_CONSUME\_SEM

1262 [k\_object\_access\_grant](group__usermode__apis.md#ga94087bedf96fe2a2bea437d3d585ca22)([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->consume\_sem, t);

1263#endif

1264}

1265

[ 1276](group__rtio.md#gac01252e55d2848b38c0ed77b71d600a7)\_\_syscall int [rtio\_sqe\_cancel](group__rtio.md#gac01252e55d2848b38c0ed77b71d600a7)(struct [rtio\_sqe](structrtio__sqe.md) \*sqe);

1277

1278static inline int z\_impl\_rtio\_sqe\_cancel(struct [rtio\_sqe](structrtio__sqe.md) \*sqe)

1279{

1280 struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \*iodev\_sqe = [CONTAINER\_OF](group__sys-util.md#gac5bc561d1bfd1bf68877fe577779bd2f)([sqe](structrtio__iodev__sqe.md#a2bd98599678909c0ddb22f879affa12b), struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md), [sqe](structrtio__iodev__sqe.md#a2bd98599678909c0ddb22f879affa12b));

1281

1282 do {

1283 iodev\_sqe->[sqe](structrtio__iodev__sqe.md#a2bd98599678909c0ddb22f879affa12b).[flags](structrtio__sqe.md#aad2ff8524df0e24b812e77e2393bf5b0) |= [RTIO\_SQE\_CANCELED](group__rtio__sqe__flags.md#ga7f7f9b038ab8409f271b1aebc1b95ee6);

1284 iodev\_sqe = [rtio\_iodev\_sqe\_next](group__rtio.md#gae690e3dc0fc40dda57257b2eed432719)(iodev\_sqe);

1285 } while (iodev\_sqe != NULL);

1286

1287 return 0;

1288}

1289

[ 1305](group__rtio.md#ga830863e6c8d9b96f4c473a038cab8f8c)\_\_syscall int [rtio\_sqe\_copy\_in\_get\_handles](group__rtio.md#ga830863e6c8d9b96f4c473a038cab8f8c)(struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2), const struct [rtio\_sqe](structrtio__sqe.md) \*sqes,

1306 struct [rtio\_sqe](structrtio__sqe.md) \*\*handle, size\_t sqe\_count);

1307

1308static inline int z\_impl\_rtio\_sqe\_copy\_in\_get\_handles(struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2), const struct [rtio\_sqe](structrtio__sqe.md) \*sqes,

1309 struct [rtio\_sqe](structrtio__sqe.md) \*\*handle,

1310 size\_t sqe\_count)

1311{

1312 struct [rtio\_sqe](structrtio__sqe.md) \*sqe;

1313 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) acquirable = [rtio\_sqe\_acquirable](group__rtio.md#ga1f4fb7bccbaae08a94387e4b11275a78)([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2));

1314

1315 if (acquirable < sqe\_count) {

1316 return -[ENOMEM](group__system__errno.md#ga6a05c923dad0c1208043e9c20a58c8e5);

1317 }

1318

1319 for (unsigned long i = 0; i < sqe\_count; i++) {

1320 sqe = [rtio\_sqe\_acquire](group__rtio.md#ga8b47c954d15a334621def53acceb6799)([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2));

1321 \_\_ASSERT\_NO\_MSG(sqe != NULL);

1322 if (handle != NULL && i == 0) {

1323 \*handle = sqe;

1324 }

1325 \*sqe = sqes[i];

1326 }

1327

1328 return 0;

1329}

1330

[ 1347](group__rtio.md#ga65e351af0a16dcf504a51ef4eb9316c7)static inline int [rtio\_sqe\_copy\_in](group__rtio.md#ga65e351af0a16dcf504a51ef4eb9316c7)(struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2), const struct [rtio\_sqe](structrtio__sqe.md) \*sqes, size\_t sqe\_count)

1348{

1349 return [rtio\_sqe\_copy\_in\_get\_handles](group__rtio.md#ga830863e6c8d9b96f4c473a038cab8f8c)([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2), sqes, NULL, sqe\_count);

1350}

1351

[ 1367](group__rtio.md#ga98b2bbef95aea342a9b86a9775dd5c3b)\_\_syscall int [rtio\_cqe\_copy\_out](group__rtio.md#ga98b2bbef95aea342a9b86a9775dd5c3b)(struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2),

1368 struct [rtio\_cqe](structrtio__cqe.md) \*cqes,

1369 size\_t cqe\_count,

1370 [k\_timeout\_t](structk__timeout__t.md) timeout);

1371static inline int z\_impl\_rtio\_cqe\_copy\_out(struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2),

1372 struct [rtio\_cqe](structrtio__cqe.md) \*cqes,

1373 size\_t cqe\_count,

1374 [k\_timeout\_t](structk__timeout__t.md) timeout)

1375{

1376 size\_t copied = 0;

1377 struct [rtio\_cqe](structrtio__cqe.md) \*cqe;

1378 [k\_timepoint\_t](structk__timepoint__t.md) end = [sys\_timepoint\_calc](group__clock__apis.md#ga509cf4599c1f162c97540743e8c21d33)(timeout);

1379

1380 do {

1381 cqe = [K\_TIMEOUT\_EQ](group__clock__apis.md#ga9abf00b34e16ab7ad0883603b6778b1b)(timeout, [K\_FOREVER](group__clock__apis.md#ga0bb4b83f0222193b21a8910311bab0ca)) ? [rtio\_cqe\_consume\_block](group__rtio.md#gaf617d05d9b59ce1f1d0697617ef6f249)([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2))

1382 : [rtio\_cqe\_consume](group__rtio.md#gae562cf241911804cdb9f4e3a73b53df4)([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2));

1383 if (cqe == NULL) {

1384#ifdef CONFIG\_BOARD\_NATIVE\_POSIX

1385 /\* Native posix fakes the clock and only moves it forward when sleeping. \*/

1386 [k\_sleep](group__thread__apis.md#ga48d4b041790454da4d68ac8711f29657)([K\_TICKS](group__clock__apis.md#gaeda983960bd25f1dba7a386ad720e395)(1));

1387#else

1388 Z\_SPIN\_DELAY(1);

1389#endif

1390 continue;

1391 }

1392 cqes[copied++] = \*cqe;

1393 [rtio\_cqe\_release](group__rtio.md#gaa0799a5f8ad98425d385a07c5d27d9cb)([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2), cqe);

1394 } while (copied < cqe\_count && ![sys\_timepoint\_expired](group__clock__apis.md#ga87d0d7a0f7bcdcc8c4909962eac12985)(end));

1395

1396 return copied;

1397}

1398

[ 1412](group__rtio.md#gafee27c64a4a4989c4eb774addde8eb2e)\_\_syscall int [rtio\_submit](group__rtio.md#gafee27c64a4a4989c4eb774addde8eb2e)(struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2), [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) wait\_count);

1413

1414static inline int z\_impl\_rtio\_submit(struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2), [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) wait\_count)

1415{

1416 int res = 0;

1417

1418#ifdef CONFIG\_RTIO\_SUBMIT\_SEM

1419 /\* TODO undefined behavior if another thread calls submit of course

1420 \*/

1421 if (wait\_count > 0) {

1422 \_\_ASSERT(![k\_is\_in\_isr](group__isr__apis.md#ga8482b0dd2283d12677a9ebe321667d16)(),

1423 "expected rtio submit with wait count to be called from a thread");

1424

1425 [k\_sem\_reset](group__semaphore__apis.md#ga1bd12d8d8c1b9c6be9b665d0fefe5562)([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->submit\_sem);

1426 [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->submit\_count = wait\_count;

1427 }

1428#else

1429 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) cq\_count = ([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808))[atomic\_get](group__atomic__apis.md#ga33bb426a17535bd1022895a7e44b32fa)(&[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->cq\_count) + wait\_count;

1430#endif

1431

1432 /\* Submit the queue to the executor which consumes submissions

1433 \* and produces completions through ISR chains or other means.

1434 \*/

1435 [rtio\_executor\_submit](group__rtio.md#gaf191153e83de72ddefb998daad02fa16)([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2));

1436

1437

1438 /\* TODO could be nicer if we could suspend the thread and not

1439 \* wake up on each completion here.

1440 \*/

1441#ifdef CONFIG\_RTIO\_SUBMIT\_SEM

1442

1443 if (wait\_count > 0) {

1444 res = [k\_sem\_take](group__semaphore__apis.md#gac71e2383c1920dddc45a561cacfef090)([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->submit\_sem, [K\_FOREVER](group__clock__apis.md#ga0bb4b83f0222193b21a8910311bab0ca));

1445 \_\_ASSERT(res == 0,

1446 "semaphore was reset or timed out while waiting on completions!");

1447 }

1448#else

1449 while (([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808))[atomic\_get](group__atomic__apis.md#ga33bb426a17535bd1022895a7e44b32fa)(&[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->cq\_count) < cq\_count) {

1450 Z\_SPIN\_DELAY(10);

1451 [k\_yield](group__thread__apis.md#ga08a3484c33444ecedc2d71d78495a295)();

1452 }

1453#endif

1454

1455 return res;

1456}

1457

1461

1462#ifdef \_\_cplusplus

1463}

1464#endif

1465

1466#include <zephyr/syscalls/rtio.h>

1467

1468#endif /\* ZEPHYR\_INCLUDE\_RTIO\_RTIO\_H\_ \*/

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

**Definition** kernel.h:1363

[K\_NO\_WAIT](group__clock__apis.md#ga3d9541cfe2e8395af66d186efa77362f)

#define K\_NO\_WAIT

Generate null timeout delay.

**Definition** kernel.h:1253

[sys\_timepoint\_calc](group__clock__apis.md#ga509cf4599c1f162c97540743e8c21d33)

k\_timepoint\_t sys\_timepoint\_calc(k\_timeout\_t timeout)

Calculate a timepoint value.

[sys\_timepoint\_expired](group__clock__apis.md#ga87d0d7a0f7bcdcc8c4909962eac12985)

static bool sys\_timepoint\_expired(k\_timepoint\_t timepoint)

Indicates if timepoint is expired.

**Definition** sys\_clock.h:327

[K\_TIMEOUT\_EQ](group__clock__apis.md#ga9abf00b34e16ab7ad0883603b6778b1b)

#define K\_TIMEOUT\_EQ(a, b)

Compare timeouts for equality.

**Definition** sys\_clock.h:80

[K\_TICKS](group__clock__apis.md#gaeda983960bd25f1dba7a386ad720e395)

#define K\_TICKS(t)

Generate timeout delay from system ticks.

**Definition** kernel.h:1305

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

[RTIO\_SQE\_CHAINED](group__rtio__sqe__flags.md#gae9191d521d4ab602b53fefb74020d06b)

#define RTIO\_SQE\_CHAINED

The next request in the queue should wait on this one.

**Definition** rtio.h:96

[rtio\_sqe\_prep\_transceive](group__rtio.md#ga0129e02abc85526199311846e1830869)

static void rtio\_sqe\_prep\_transceive(struct rtio\_sqe \*sqe, const struct rtio\_iodev \*iodev, int8\_t prio, uint8\_t \*tx\_buf, uint8\_t \*rx\_buf, uint32\_t buf\_len, void \*userdata)

Prepare a transceive op submission.

**Definition** rtio.h:605

[rtio\_sqe\_prep\_read\_with\_pool](group__rtio.md#ga15c1f623658d27d300d1a31a6f3d6b9d)

static void rtio\_sqe\_prep\_read\_with\_pool(struct rtio\_sqe \*sqe, const struct rtio\_iodev \*iodev, int8\_t prio, void \*userdata)

Prepare a read op submission with context's mempool.

**Definition** rtio.h:517

[rtio\_executor\_err](group__rtio.md#ga15f4a1a4dfb869ef9e4216dc1c1cdc8a)

void rtio\_executor\_err(struct rtio\_iodev\_sqe \*iodev\_sqe, int result)

[RTIO\_OP\_CALLBACK](group__rtio.md#ga18e0ff7d44e4c33900106aefad0a8508)

#define RTIO\_OP\_CALLBACK

An operation that calls a given function (callback).

**Definition** rtio.h:469

[rtio\_sqe\_acquirable](group__rtio.md#ga1f4fb7bccbaae08a94387e4b11275a78)

static uint32\_t rtio\_sqe\_acquirable(struct rtio \*r)

Count of acquirable submission queue events.

**Definition** rtio.h:840

[rtio\_cqe\_pool\_free](group__rtio.md#ga23c0c5d4b551858eabe057ecb8a28d12)

static void rtio\_cqe\_pool\_free(struct rtio\_cqe\_pool \*pool, struct rtio\_cqe \*cqe)

**Definition** rtio.h:662

[rtio\_sqe\_prep\_tiny\_write](group__rtio.md#ga31be14ece09e061a8d42ca8f2395286a)

static void rtio\_sqe\_prep\_tiny\_write(struct rtio\_sqe \*sqe, const struct rtio\_iodev \*iodev, int8\_t prio, const uint8\_t \*tiny\_write\_data, uint8\_t tiny\_write\_len, void \*userdata)

Prepare a tiny write op submission.

**Definition** rtio.h:562

[rtio\_mempool\_block\_size](group__rtio.md#ga4213be028b0a1264daaa0d30c4c2d089)

static size\_t rtio\_mempool\_block\_size(const struct rtio \*r)

Get the mempool block size of the RTIO context.

**Definition** rtio.h:381

[rtio\_cqe\_submit](group__rtio.md#ga4abc221d5a90ab882000a72caa0ebd0f)

static void rtio\_cqe\_submit(struct rtio \*r, int result, void \*userdata, uint32\_t flags)

Submit a completion queue event with a given result and userdata.

**Definition** rtio.h:1138

[rtio\_sqe\_prep\_nop](group__rtio.md#ga599ee43fdf35e1cf895cbbe9272e4c50)

static void rtio\_sqe\_prep\_nop(struct rtio\_sqe \*sqe, const struct rtio\_iodev \*iodev, void \*userdata)

Prepare a nop (no op) submission.

**Definition** rtio.h:483

[rtio\_release\_buffer](group__rtio.md#ga6530bf56ccbab046a362a6448f941609)

void rtio\_release\_buffer(struct rtio \*r, void \*buff, uint32\_t buff\_len)

Release memory that was allocated by the RTIO's memory pool.

[rtio\_sqe\_copy\_in](group__rtio.md#ga65e351af0a16dcf504a51ef4eb9316c7)

static int rtio\_sqe\_copy\_in(struct rtio \*r, const struct rtio\_sqe \*sqes, size\_t sqe\_count)

Copy an array of SQEs into the queue.

**Definition** rtio.h:1347

[rtio\_cqe\_produce](group__rtio.md#ga6f55202adeca60aed0343a7a0dcab071)

static void rtio\_cqe\_produce(struct rtio \*r, struct rtio\_cqe \*cqe)

Produce a complete queue event if available.

**Definition** rtio.h:950

[RTIO\_OP\_TINY\_TX](group__rtio.md#ga6f95c0a5fbcc020a0d1102d3b08934bd)

#define RTIO\_OP\_TINY\_TX

An operation that transmits tiny writes by copying the data to write.

**Definition** rtio.h:466

[rtio\_cqe\_compute\_flags](group__rtio.md#ga75661c8c6c94a0ac6254cec674b478c8)

static uint32\_t rtio\_cqe\_compute\_flags(struct rtio\_iodev\_sqe \*iodev\_sqe)

Compute the CQE flags from the rtio\_iodev\_sqe entry.

**Definition** rtio.h:1031

[rtio\_executor\_ok](group__rtio.md#ga7e2ebd9abaf585207bc5b99c5d815c6a)

void rtio\_executor\_ok(struct rtio\_iodev\_sqe \*iodev\_sqe, int result)

[rtio\_block\_pool\_alloc](group__rtio.md#ga7f14b99fc1dd0697309e7f71a270f5fb)

static int rtio\_block\_pool\_alloc(struct rtio \*r, size\_t min\_sz, size\_t max\_sz, uint8\_t \*\*buf, uint32\_t \*buf\_len)

**Definition** rtio.h:669

[rtio\_sqe\_copy\_in\_get\_handles](group__rtio.md#ga830863e6c8d9b96f4c473a038cab8f8c)

int rtio\_sqe\_copy\_in\_get\_handles(struct rtio \*r, const struct rtio\_sqe \*sqes, struct rtio\_sqe \*\*handle, size\_t sqe\_count)

Copy an array of SQEs into the queue and get resulting handles back.

[rtio\_cqe\_pool\_alloc](group__rtio.md#ga8497170f55af1d11d717e919f61806f5)

static struct rtio\_cqe \* rtio\_cqe\_pool\_alloc(struct rtio\_cqe\_pool \*pool)

**Definition** rtio.h:645

[rtio\_partition](group__rtio.md#ga86a38086dd85150ab6e479d73db1c6d1)

struct k\_mem\_partition rtio\_partition

The memory partition associated with all RTIO context information.

[rtio\_sqe\_prep\_read](group__rtio.md#ga89c7cc2494e3dda50737f78f1a1376cf)

static void rtio\_sqe\_prep\_read(struct rtio\_sqe \*sqe, const struct rtio\_iodev \*iodev, int8\_t prio, uint8\_t \*buf, uint32\_t len, void \*userdata)

Prepare a read op submission.

**Definition** rtio.h:496

[rtio\_sqe\_acquire](group__rtio.md#ga8b47c954d15a334621def53acceb6799)

static struct rtio\_sqe \* rtio\_sqe\_acquire(struct rtio \*r)

Acquire a single submission queue event if available.

**Definition** rtio.h:901

[RTIO\_OP\_TX](group__rtio.md#ga8dcaef0cda159e16520a95543ff62827)

#define RTIO\_OP\_TX

An operation that transmits (writes).

**Definition** rtio.h:463

[rtio\_sqe\_drop\_all](group__rtio.md#ga9486fb7b50e8d2409a50da235203536b)

static void rtio\_sqe\_drop\_all(struct rtio \*r)

Drop all previously acquired sqe.

**Definition** rtio.h:919

[rtio\_sqe\_prep\_read\_multishot](group__rtio.md#ga9803aa829f8c0eeee746ea7d872c20cc)

static void rtio\_sqe\_prep\_read\_multishot(struct rtio\_sqe \*sqe, const struct rtio\_iodev \*iodev, int8\_t prio, void \*userdata)

**Definition** rtio.h:525

[rtio\_cqe\_copy\_out](group__rtio.md#ga98b2bbef95aea342a9b86a9775dd5c3b)

int rtio\_cqe\_copy\_out(struct rtio \*r, struct rtio\_cqe \*cqes, size\_t cqe\_count, k\_timeout\_t timeout)

Copy an array of CQEs from the queue.

[rtio\_sqe\_prep\_callback](group__rtio.md#ga9d0dd7d0e2e3d281092f2350d6e1713e)

static void rtio\_sqe\_prep\_callback(struct rtio\_sqe \*sqe, rtio\_callback\_t callback, void \*arg0, void \*userdata)

Prepare a callback op submission.

**Definition** rtio.h:588

[rtio\_access\_grant](group__rtio.md#ga9da42c98546930575525f0f92710f9e4)

static void rtio\_access\_grant(struct rtio \*r, struct k\_thread \*t)

Grant access to an RTIO context to a user thread.

**Definition** rtio.h:1253

[RTIO\_OP\_TXRX](group__rtio.md#ga9f0e70f5a28be65a8ed67c0257a72692)

#define RTIO\_OP\_TXRX

An operation that transceives (reads and writes simultaneously).

**Definition** rtio.h:472

[rtio\_cqe\_release](group__rtio.md#gaa0799a5f8ad98425d385a07c5d27d9cb)

static void rtio\_cqe\_release(struct rtio \*r, struct rtio\_cqe \*cqe)

Release consumed completion queue event.

**Definition** rtio.h:1020

[rtio\_sqe\_rx\_buf](group__rtio.md#gaab6843e2038d00a8354f57d7e2ffcf7e)

static int rtio\_sqe\_rx\_buf(const struct rtio\_iodev\_sqe \*iodev\_sqe, uint32\_t min\_buf\_len, uint32\_t max\_buf\_len, uint8\_t \*\*buf, uint32\_t \*buf\_len)

Get the buffer associate with the RX submission.

**Definition** rtio.h:1179

[rtio\_iodev\_sqe\_err](group__rtio.md#gaada07aa6acefa548743b525225fa482f)

static void rtio\_iodev\_sqe\_err(struct rtio\_iodev\_sqe \*iodev\_sqe, int result)

Inform the executor of a submissions completion with error.

**Definition** rtio.h:1122

[rtio\_sqe\_prep\_write](group__rtio.md#gab01192577dadf7ab83d3f8029c86a149)

static void rtio\_sqe\_prep\_write(struct rtio\_sqe \*sqe, const struct rtio\_iodev \*iodev, int8\_t prio, uint8\_t \*buf, uint32\_t len, void \*userdata)

Prepare a write op submission.

**Definition** rtio.h:536

[rtio\_sqe\_cancel](group__rtio.md#gac01252e55d2848b38c0ed77b71d600a7)

int rtio\_sqe\_cancel(struct rtio\_sqe \*sqe)

Attempt to cancel an SQE.

[rtio\_sqe\_pool\_free](group__rtio.md#gac776aea3692cfd77aa5bf675a9e9ed02)

static void rtio\_sqe\_pool\_free(struct rtio\_sqe\_pool \*pool, struct rtio\_iodev\_sqe \*iodev\_sqe)

**Definition** rtio.h:638

[rtio\_iodev\_sqe\_ok](group__rtio.md#gacb1d2ffa2b07418d8a8aa319bd4336ab)

static void rtio\_iodev\_sqe\_ok(struct rtio\_iodev\_sqe \*iodev\_sqe, int result)

Inform the executor of a submission completion with success.

**Definition** rtio.h:1109

[rtio\_callback\_t](group__rtio.md#gad1dbd690e6cf88d7c788436dd04d1a00)

void(\* rtio\_callback\_t)(struct rtio \*r, const struct rtio\_sqe \*sqe, void \*arg0)

Callback signature for RTIO\_OP\_CALLBACK.

**Definition** rtio.h:227

[RTIO\_OP\_NOP](group__rtio.md#gad5f073978f641413989d1c6b405d6c36)

#define RTIO\_OP\_NOP

An operation that does nothing and will complete immediately.

**Definition** rtio.h:457

[rtio\_cqe\_acquire](group__rtio.md#gad848646651fdf3649b882e5268f72a3c)

static struct rtio\_cqe \* rtio\_cqe\_acquire(struct rtio \*r)

Acquire a complete queue event if available.

**Definition** rtio.h:934

[rtio\_chain\_next](group__rtio.md#gada1e3abf92a46e376138435debc8baf4)

static struct rtio\_iodev\_sqe \* rtio\_chain\_next(const struct rtio\_iodev\_sqe \*iodev\_sqe)

Get the next sqe in the chain.

**Definition** rtio.h:871

[rtio\_cqe\_consume](group__rtio.md#gae562cf241911804cdb9f4e3a73b53df4)

static struct rtio\_cqe \* rtio\_cqe\_consume(struct rtio \*r)

Consume a single completion queue event if available.

**Definition** rtio.h:966

[rtio\_sqe\_pool\_alloc](group__rtio.md#gae5fb03fc8f3a4a774f476ff552999bfc)

static struct rtio\_iodev\_sqe \* rtio\_sqe\_pool\_alloc(struct rtio\_sqe\_pool \*pool)

**Definition** rtio.h:623

[rtio\_iodev\_sqe\_next](group__rtio.md#gae690e3dc0fc40dda57257b2eed432719)

static struct rtio\_iodev\_sqe \* rtio\_iodev\_sqe\_next(const struct rtio\_iodev\_sqe \*iodev\_sqe)

Get the next sqe in the chain or transaction.

**Definition** rtio.h:888

[rtio\_cqe\_get\_mempool\_buffer](group__rtio.md#gaedbf9386a36ed99baa290ef6c318ded1)

int rtio\_cqe\_get\_mempool\_buffer(const struct rtio \*r, struct rtio\_cqe \*cqe, uint8\_t \*\*buff, uint32\_t \*buff\_len)

Retrieve the mempool buffer that was allocated for the CQE.

[rtio\_txn\_next](group__rtio.md#gaef904eb6a8810d8c3ea537c4d6edbee5)

static struct rtio\_iodev\_sqe \* rtio\_txn\_next(const struct rtio\_iodev\_sqe \*iodev\_sqe)

Get the next sqe in the transaction.

**Definition** rtio.h:853

[rtio\_executor\_submit](group__rtio.md#gaf191153e83de72ddefb998daad02fa16)

void rtio\_executor\_submit(struct rtio \*r)

[rtio\_cqe\_consume\_block](group__rtio.md#gaf617d05d9b59ce1f1d0697617ef6f249)

static struct rtio\_cqe \* rtio\_cqe\_consume\_block(struct rtio \*r)

Wait for and consume a single completion queue event.

**Definition** rtio.h:996

[rtio\_block\_pool\_free](group__rtio.md#gafca7732926a9a7c080e3cb16e5f16108)

static void rtio\_block\_pool\_free(struct rtio \*r, void \*buf, uint32\_t buf\_len)

**Definition** rtio.h:706

[RTIO\_OP\_RX](group__rtio.md#gafeb05c351207cd1638fa78f6607e1a4a)

#define RTIO\_OP\_RX

An operation that receives (reads).

**Definition** rtio.h:460

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

**Definition** util.h:268

[DIV\_ROUND\_UP](group__sys-util.md#gae664e7492e37d324831caf2321ddda37)

#define DIV\_ROUND\_UP(n, d)

Divide and round up.

**Definition** util.h:336

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

[k\_sleep](group__thread__apis.md#ga48d4b041790454da4d68ac8711f29657)

int32\_t k\_sleep(k\_timeout\_t timeout)

Put the current thread to sleep.

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

**Definition** rtio.h:309

[rtio\_cqe\_pool::pool](structrtio__cqe__pool.md#a05584219d473fcf85d46757fa9cea703)

struct rtio\_cqe \* pool

**Definition** rtio.h:313

[rtio\_cqe\_pool::free\_q](structrtio__cqe__pool.md#a13bd7991ff5622c1cb5aa6af014aaab3)

struct mpsc free\_q

**Definition** rtio.h:310

[rtio\_cqe\_pool::pool\_size](structrtio__cqe__pool.md#a43bf4141673c61493644539987f27fb1)

const uint16\_t pool\_size

**Definition** rtio.h:311

[rtio\_cqe\_pool::pool\_free](structrtio__cqe__pool.md#a4fb501a0ba15e2956113deaf4597d846)

uint16\_t pool\_free

**Definition** rtio.h:312

[rtio\_cqe](structrtio__cqe.md)

A completion queue event.

**Definition** rtio.h:294

[rtio\_cqe::userdata](structrtio__cqe.md#a15128387ccbea55812ef229eab7241e7)

void \* userdata

Associated userdata with operation.

**Definition** rtio.h:298

[rtio\_cqe::q](structrtio__cqe.md#a27272bca31c170f406799633ec82098d)

struct mpsc\_node q

**Definition** rtio.h:295

[rtio\_cqe::flags](structrtio__cqe.md#a8a7632ef1cfd31529d782bd761908d93)

uint32\_t flags

Flags associated with the operation.

**Definition** rtio.h:299

[rtio\_cqe::result](structrtio__cqe.md#acbe2e6607a752b676d9336b9ca6ce435)

int32\_t result

Result from operation.

**Definition** rtio.h:297

[rtio\_iodev\_api](structrtio__iodev__api.md)

API that an RTIO IO device should implement.

**Definition** rtio.h:433

[rtio\_iodev\_api::submit](structrtio__iodev__api.md#a6cd795906753535571ec1ecc0e0c430c)

void(\* submit)(struct rtio\_iodev\_sqe \*iodev\_sqe)

Submit to the iodev an entry to work on.

**Definition** rtio.h:442

[rtio\_iodev\_sqe](structrtio__iodev__sqe.md)

Compute the mempool block index for a given pointer.

**Definition** rtio.h:423

[rtio\_iodev\_sqe::next](structrtio__iodev__sqe.md#a2afb82e550e614f87db7cd1bf2c3a352)

struct rtio\_iodev\_sqe \* next

**Definition** rtio.h:426

[rtio\_iodev\_sqe::sqe](structrtio__iodev__sqe.md#a2bd98599678909c0ddb22f879affa12b)

struct rtio\_sqe sqe

**Definition** rtio.h:424

[rtio\_iodev\_sqe::r](structrtio__iodev__sqe.md#a3c3a050793589258eab5ff5ac30f24c8)

struct rtio \* r

**Definition** rtio.h:427

[rtio\_iodev\_sqe::q](structrtio__iodev__sqe.md#a9cfdd004b65a5e2bc111bc2fb333498c)

struct mpsc\_node q

**Definition** rtio.h:425

[rtio\_iodev](structrtio__iodev.md)

An IO device with a function table for submitting requests.

**Definition** rtio.h:448

[rtio\_iodev::api](structrtio__iodev.md#a6dfedbfb58356e0647e5c20632656977)

const struct rtio\_iodev\_api \* api

**Definition** rtio.h:450

[rtio\_iodev::data](structrtio__iodev.md#af0f3a27fe8dea2161c9a73cb838bdeec)

void \* data

**Definition** rtio.h:453

[rtio\_sqe\_pool](structrtio__sqe__pool.md)

**Definition** rtio.h:302

[rtio\_sqe\_pool::pool](structrtio__sqe__pool.md#ab2c0394e175bd8c6f0c02edb315b6c9b)

struct rtio\_iodev\_sqe \* pool

**Definition** rtio.h:306

[rtio\_sqe\_pool::pool\_size](structrtio__sqe__pool.md#ade3b4354d007fe17a7753c26e2121465)

const uint16\_t pool\_size

**Definition** rtio.h:304

[rtio\_sqe\_pool::free\_q](structrtio__sqe__pool.md#aed49ea25c952e07a8287919268fd2485)

struct mpsc free\_q

**Definition** rtio.h:303

[rtio\_sqe\_pool::pool\_free](structrtio__sqe__pool.md#af7990b1510ad2343573f3e4e502475b0)

uint16\_t pool\_free

**Definition** rtio.h:305

[rtio\_sqe](structrtio__sqe.md)

A submission queue event.

**Definition** rtio.h:232

[rtio\_sqe::i2c\_config](structrtio__sqe.md#a07bf344b1b1063b8bea80cf5ba1c1cc5)

uint32\_t i2c\_config

OP\_I2C\_CONFIGURE.

**Definition** rtio.h:282

[rtio\_sqe::userdata](structrtio__sqe.md#a0ed519ee0b5867ff73bdaf37f983c971)

void \* userdata

User provided data which is returned upon operation completion.

**Definition** rtio.h:252

[rtio\_sqe::tx\_buf](structrtio__sqe.md#a186c22217961a5eddb75ad0bd84a538a)

uint8\_t \* tx\_buf

**Definition** rtio.h:277

[rtio\_sqe::op](structrtio__sqe.md#a1d8d3e3426e47a2c7f54d98f51acd953)

uint8\_t op

Op code.

**Definition** rtio.h:233

[rtio\_sqe::arg0](structrtio__sqe.md#a438d2156a61aef9ca840af9c01d5dfa4)

void \* arg0

Last argument given to callback.

**Definition** rtio.h:271

[rtio\_sqe::rx\_buf](structrtio__sqe.md#a4d2090fc11b897724a883ad1087d9f73)

uint8\_t \* rx\_buf

**Definition** rtio.h:278

[rtio\_sqe::prio](structrtio__sqe.md#a528eb9b721be7b8a8898ab16a7e2d9a7)

uint8\_t prio

Op priority.

**Definition** rtio.h:235

[rtio\_sqe::buf](structrtio__sqe.md#a55e98f27b26393fee8e179b7bdb6a52e)

uint8\_t \* buf

Buffer to use.

**Definition** rtio.h:259

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

[rtio\_sqe::tiny\_buf\_len](structrtio__sqe.md#ab25f9d5c2e4d833d548148843a859096)

uint8\_t tiny\_buf\_len

Length of tiny buffer.

**Definition** rtio.h:264

[rtio\_sqe::txrx\_buf\_len](structrtio__sqe.md#ab3cff3dbbfc9b1a0dbe8f1dc28ac83f8)

uint32\_t txrx\_buf\_len

**Definition** rtio.h:276

[rtio\_sqe::tiny\_buf](structrtio__sqe.md#aceaa9999b86fd271321988e257aeecc8)

uint8\_t tiny\_buf[7]

Tiny buffer.

**Definition** rtio.h:265

[rtio\_sqe::callback](structrtio__sqe.md#af8c31c33e9fedebe55cac73595d0f696)

rtio\_callback\_t callback

**Definition** rtio.h:270

[rtio\_sqe::iodev\_flags](structrtio__sqe.md#af979ffa7bd3efaa6cbcb1344404cb985)

uint16\_t iodev\_flags

Op iodev flags.

**Definition** rtio.h:239

[rtio](structrtio.md)

An RTIO context containing what can be viewed as a pair of queues.

**Definition** rtio.h:327

[rtio::cqe\_pool](structrtio.md#a1bce3c3bb0150275ece65975adf3ee4f)

struct rtio\_cqe\_pool \* cqe\_pool

**Definition** rtio.h:357

[rtio::sq](structrtio.md#a34fbabfdbef3144f4520bf678684cdfb)

struct mpsc sq

**Definition** rtio.h:365

[rtio::cq\_count](structrtio.md#a358de1033ab4396d1f1baee2699c993f)

atomic\_t cq\_count

**Definition** rtio.h:346

[rtio::sqe\_pool](structrtio.md#a955f012bac623e7c037b5f1dba8e7fda)

struct rtio\_sqe\_pool \* sqe\_pool

**Definition** rtio.h:354

[rtio::xcqcnt](structrtio.md#ac45facdcc6d64cd70113b9b05b2fb086)

atomic\_t xcqcnt

**Definition** rtio.h:351

[rtio::cq](structrtio.md#ad6f44a354a170cb04a584beee7728fa9)

struct mpsc cq

**Definition** rtio.h:368

[atomic.h](sys_2atomic_8h.md)

[iterable\_sections.h](sys_2iterable__sections_8h.md)

[util.h](util_8h.md)

Misc utilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [rtio](dir_2c800b92938ab205b51fc9bd951bff11.md)
- [rtio.h](rtio_2rtio_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
