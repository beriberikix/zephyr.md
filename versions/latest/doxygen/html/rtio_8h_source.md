---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/rtio_8h_source.html
original_path: doxygen/html/rtio_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

rtio.h

[Go to the documentation of this file.](rtio_8h.md)

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

33#include <[zephyr/kernel.h](include_2zephyr_2kernel_8h.md)>

34#include <[zephyr/rtio/rtio\_mpsc.h](rtio__mpsc_8h.md)>

35#include <[zephyr/sys/\_\_assert.h](____assert_8h.md)>

36#include <[zephyr/sys/atomic.h](atomic_8h.md)>

37#include <[zephyr/sys/mem\_blocks.h](mem__blocks_8h.md)>

38#include <[zephyr/sys/util.h](util_8h.md)>

39#include <[zephyr/sys/iterable\_sections.h](sys_2iterable__sections_8h.md)>

40

41#ifdef \_\_cplusplus

42extern "C" {

43#endif

44

45

52

59

[ 63](group__rtio__sqe__prio.md#gabc81232a7d4b7145d9898afd6ff2ae48)#define RTIO\_PRIO\_LOW 0U

64

[ 68](group__rtio__sqe__prio.md#gab02e27e01b7dd4eb3439df557899ce92)#define RTIO\_PRIO\_NORM 127U

69

[ 73](group__rtio__sqe__prio.md#ga220baa9bf2c8ff0cb6f52f0220e72b30)#define RTIO\_PRIO\_HIGH 255U

74

78

79

86

[ 94](group__rtio__sqe__flags.md#gae9191d521d4ab602b53fefb74020d06b)#define RTIO\_SQE\_CHAINED BIT(0)

95

[ 106](group__rtio__sqe__flags.md#ga07f09cc0c95be6cfdddb23f8acacb1ea)#define RTIO\_SQE\_TRANSACTION BIT(1)

107

108

[ 118](group__rtio__sqe__flags.md#ga2802b46584220afffa0e959e149d5a4d)#define RTIO\_SQE\_MEMPOOL\_BUFFER BIT(2)

119

[ 126](group__rtio__sqe__flags.md#ga7f7f9b038ab8409f271b1aebc1b95ee6)#define RTIO\_SQE\_CANCELED BIT(3)

127

[ 134](group__rtio__sqe__flags.md#ga00f8ead8f043fe40d49d0bc3325fb299)#define RTIO\_SQE\_MULTISHOT BIT(4)

135

[ 139](group__rtio__sqe__flags.md#ga8578ffdb8f53a51b94fa86a6f02d4a11)#define RTIO\_SQE\_NO\_RESPONSE BIT(5)

140

144

151

[ 158](group__rtio__cqe__flags.md#ga0f212500447a5e37e225a6997953b609)#define RTIO\_CQE\_FLAG\_MEMPOOL\_BUFFER BIT(0)

159

[ 160](group__rtio__cqe__flags.md#gaef64ea020a20ac22a0edcb6eca032efc)#define RTIO\_CQE\_FLAG\_GET(flags) FIELD\_GET(GENMASK(7, 0), (flags))

161

[ 168](group__rtio__cqe__flags.md#ga0b5f3f7e7be472ecf87bd2b08c1888da)#define RTIO\_CQE\_FLAG\_MEMPOOL\_GET\_BLK\_IDX(flags) FIELD\_GET(GENMASK(19, 8), (flags))

169

[ 176](group__rtio__cqe__flags.md#ga087465f866d417d5332602bb582cc1a7)#define RTIO\_CQE\_FLAG\_MEMPOOL\_GET\_BLK\_CNT(flags) FIELD\_GET(GENMASK(31, 20), (flags))

177

[ 185](group__rtio__cqe__flags.md#ga28b3a5661248b6b3763aab47417114d6)#define RTIO\_CQE\_FLAG\_PREP\_MEMPOOL(blk\_idx, blk\_cnt) \

186 (FIELD\_PREP(GENMASK(7, 0), RTIO\_CQE\_FLAG\_MEMPOOL\_BUFFER) | \

187 FIELD\_PREP(GENMASK(19, 8), blk\_idx) | FIELD\_PREP(GENMASK(31, 20), blk\_cnt))

188

192

[ 196](group__rtio.md#gaf923e862d2c6a3fbce5eb96781cf86d8)#define RTIO\_IODEV\_I2C\_STOP BIT(0)

197

[ 201](group__rtio.md#gadba1c5eddeecc431000bd92054f55c3a)#define RTIO\_IODEV\_I2C\_RESTART BIT(1)

202

[ 206](group__rtio.md#gaa0c3b047c7205d12775d8d38907119b9)#define RTIO\_IODEV\_I2C\_10\_BITS BIT(2)

207

209struct [rtio](structrtio.md);

210struct [rtio\_cqe](structrtio__cqe.md);

211struct [rtio\_sqe](structrtio__sqe.md);

212struct [rtio\_sqe\_pool](structrtio__sqe__pool.md);

213struct [rtio\_cqe\_pool](structrtio__cqe__pool.md);

214struct [rtio\_iodev](structrtio__iodev.md);

215struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md);

217

[ 225](group__rtio.md#gad1dbd690e6cf88d7c788436dd04d1a00)typedef void (\*[rtio\_callback\_t](group__rtio.md#gad1dbd690e6cf88d7c788436dd04d1a00))(struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2), const struct [rtio\_sqe](structrtio__sqe.md) \*sqe, void \*[arg0](structrtio__sqe.md#a438d2156a61aef9ca840af9c01d5dfa4));

226

[ 230](structrtio__sqe.md)struct [rtio\_sqe](structrtio__sqe.md) {

[ 231](structrtio__sqe.md#a1d8d3e3426e47a2c7f54d98f51acd953) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [op](structrtio__sqe.md#a1d8d3e3426e47a2c7f54d98f51acd953);

232

[ 233](structrtio__sqe.md#a528eb9b721be7b8a8898ab16a7e2d9a7) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [prio](structrtio__sqe.md#a528eb9b721be7b8a8898ab16a7e2d9a7);

234

[ 235](structrtio__sqe.md#aad2ff8524df0e24b812e77e2393bf5b0) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [flags](structrtio__sqe.md#aad2ff8524df0e24b812e77e2393bf5b0);

236

[ 237](structrtio__sqe.md#af979ffa7bd3efaa6cbcb1344404cb985) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [iodev\_flags](structrtio__sqe.md#af979ffa7bd3efaa6cbcb1344404cb985);

238

239 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \_resv0;

240

[ 241](structrtio__sqe.md#a6c784702f011592c84feacd57915bbfc) const struct [rtio\_iodev](structrtio__iodev.md) \*[iodev](structrtio__sqe.md#a6c784702f011592c84feacd57915bbfc);

242

[ 250](structrtio__sqe.md#a0ed519ee0b5867ff73bdaf37f983c971) void \*[userdata](structrtio__sqe.md#a0ed519ee0b5867ff73bdaf37f983c971);

251

252 union {

253

255 struct {

[ 256](structrtio__sqe.md#a67376f40a13960b152a23da250275722) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [buf\_len](structrtio__sqe.md#a67376f40a13960b152a23da250275722);

[ 257](structrtio__sqe.md#a55e98f27b26393fee8e179b7bdb6a52e) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[buf](structrtio__sqe.md#a55e98f27b26393fee8e179b7bdb6a52e);

258 };

259

261 struct {

[ 262](structrtio__sqe.md#ab25f9d5c2e4d833d548148843a859096) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [tiny\_buf\_len](structrtio__sqe.md#ab25f9d5c2e4d833d548148843a859096);

[ 263](structrtio__sqe.md#aceaa9999b86fd271321988e257aeecc8) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [tiny\_buf](structrtio__sqe.md#aceaa9999b86fd271321988e257aeecc8)[7];

264 };

265

267 struct {

[ 268](structrtio__sqe.md#af8c31c33e9fedebe55cac73595d0f696) [rtio\_callback\_t](group__rtio.md#gad1dbd690e6cf88d7c788436dd04d1a00) [callback](structrtio__sqe.md#af8c31c33e9fedebe55cac73595d0f696);

[ 269](structrtio__sqe.md#a438d2156a61aef9ca840af9c01d5dfa4) void \*[arg0](structrtio__sqe.md#a438d2156a61aef9ca840af9c01d5dfa4);

270 };

271

273 struct {

[ 274](structrtio__sqe.md#ab3cff3dbbfc9b1a0dbe8f1dc28ac83f8) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [txrx\_buf\_len](structrtio__sqe.md#ab3cff3dbbfc9b1a0dbe8f1dc28ac83f8);

[ 275](structrtio__sqe.md#a186c22217961a5eddb75ad0bd84a538a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[tx\_buf](structrtio__sqe.md#a186c22217961a5eddb75ad0bd84a538a);

[ 276](structrtio__sqe.md#a4d2090fc11b897724a883ad1087d9f73) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[rx\_buf](structrtio__sqe.md#a4d2090fc11b897724a883ad1087d9f73);

277 };

278

279 };

280};

281

283/\* Ensure the rtio\_sqe never grows beyond a common cacheline size of 64 bytes \*/

284BUILD\_ASSERT(sizeof(struct [rtio\_sqe](structrtio__sqe.md)) <= 64);

286

[ 290](structrtio__cqe.md)struct [rtio\_cqe](structrtio__cqe.md) {

[ 291](structrtio__cqe.md#a71836f1322cc64af7153c9e16dc112bc) struct [rtio\_mpsc\_node](structrtio__mpsc__node.md) [q](structrtio__cqe.md#a71836f1322cc64af7153c9e16dc112bc);

292

[ 293](structrtio__cqe.md#acbe2e6607a752b676d9336b9ca6ce435) [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) [result](structrtio__cqe.md#acbe2e6607a752b676d9336b9ca6ce435);

[ 294](structrtio__cqe.md#a15128387ccbea55812ef229eab7241e7) void \*[userdata](structrtio__cqe.md#a15128387ccbea55812ef229eab7241e7);

[ 295](structrtio__cqe.md#a8a7632ef1cfd31529d782bd761908d93) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](structrtio__cqe.md#a8a7632ef1cfd31529d782bd761908d93);

296};

297

[ 298](structrtio__sqe__pool.md)struct [rtio\_sqe\_pool](structrtio__sqe__pool.md) {

[ 299](structrtio__sqe__pool.md#a95f516beb25feb60e44b42cd72d115b8) struct [rtio\_mpsc](structrtio__mpsc.md) [free\_q](structrtio__sqe__pool.md#a95f516beb25feb60e44b42cd72d115b8);

[ 300](structrtio__sqe__pool.md#ade3b4354d007fe17a7753c26e2121465) const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [pool\_size](structrtio__sqe__pool.md#ade3b4354d007fe17a7753c26e2121465);

[ 301](structrtio__sqe__pool.md#af7990b1510ad2343573f3e4e502475b0) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [pool\_free](structrtio__sqe__pool.md#af7990b1510ad2343573f3e4e502475b0);

[ 302](structrtio__sqe__pool.md#ab2c0394e175bd8c6f0c02edb315b6c9b) struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \*[pool](structrtio__sqe__pool.md#ab2c0394e175bd8c6f0c02edb315b6c9b);

303};

304

[ 305](structrtio__cqe__pool.md)struct [rtio\_cqe\_pool](structrtio__cqe__pool.md) {

[ 306](structrtio__cqe__pool.md#afa391fcb1657ca162ff5fd5c854a2013) struct [rtio\_mpsc](structrtio__mpsc.md) [free\_q](structrtio__cqe__pool.md#afa391fcb1657ca162ff5fd5c854a2013);

[ 307](structrtio__cqe__pool.md#a43bf4141673c61493644539987f27fb1) const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [pool\_size](structrtio__cqe__pool.md#a43bf4141673c61493644539987f27fb1);

[ 308](structrtio__cqe__pool.md#a4fb501a0ba15e2956113deaf4597d846) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [pool\_free](structrtio__cqe__pool.md#a4fb501a0ba15e2956113deaf4597d846);

[ 309](structrtio__cqe__pool.md#a05584219d473fcf85d46757fa9cea703) struct [rtio\_cqe](structrtio__cqe.md) \*[pool](structrtio__cqe__pool.md#a05584219d473fcf85d46757fa9cea703);

310};

311

[ 323](structrtio.md)struct [rtio](structrtio.md) {

324#ifdef CONFIG\_RTIO\_SUBMIT\_SEM

325 /\* A wait semaphore which may suspend the calling thread

326 \* to wait for some number of completions when calling submit

327 \*/

328 struct k\_sem \*submit\_sem;

329

330 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) submit\_count;

331#endif

332

333#ifdef CONFIG\_RTIO\_CONSUME\_SEM

334 /\* A wait semaphore which may suspend the calling thread

335 \* to wait for some number of completions while consuming

336 \* them from the completion queue

337 \*/

338 struct k\_sem \*consume\_sem;

339#endif

340

341 /\* Total number of completions \*/

[ 342](structrtio.md#a358de1033ab4396d1f1baee2699c993f) [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) [cq\_count](structrtio.md#a358de1033ab4396d1f1baee2699c993f);

343

344 /\* Number of completions that were unable to be submitted with results

345 \* due to the cq spsc being full

346 \*/

[ 347](structrtio.md#ac45facdcc6d64cd70113b9b05b2fb086) [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) [xcqcnt](structrtio.md#ac45facdcc6d64cd70113b9b05b2fb086);

348

349 /\* Submission queue object pool with free list \*/

[ 350](structrtio.md#a955f012bac623e7c037b5f1dba8e7fda) struct [rtio\_sqe\_pool](structrtio__sqe__pool.md) \*[sqe\_pool](structrtio.md#a955f012bac623e7c037b5f1dba8e7fda);

351

352 /\* Complete queue object pool with free list \*/

[ 353](structrtio.md#a1bce3c3bb0150275ece65975adf3ee4f) struct [rtio\_cqe\_pool](structrtio__cqe__pool.md) \*[cqe\_pool](structrtio.md#a1bce3c3bb0150275ece65975adf3ee4f);

354

355#ifdef CONFIG\_RTIO\_SYS\_MEM\_BLOCKS

356 /\* Mem block pool \*/

357 struct sys\_mem\_blocks \*block\_pool;

358#endif

359

360 /\* Submission queue \*/

[ 361](structrtio.md#a33a715558d60d87c1a47f33dacc9f849) struct [rtio\_mpsc](structrtio__mpsc.md) [sq](structrtio.md#a33a715558d60d87c1a47f33dacc9f849);

362

363 /\* Completion queue \*/

[ 364](structrtio.md#a1fc6c2dd44420679e273b7a328ed19ec) struct [rtio\_mpsc](structrtio__mpsc.md) [cq](structrtio.md#a1fc6c2dd44420679e273b7a328ed19ec);

365};

366

368extern struct [k\_mem\_partition](structk__mem__partition.md) [rtio\_partition](group__rtio.md#ga86a38086dd85150ab6e479d73db1c6d1);

369

[ 377](group__rtio.md#ga4213be028b0a1264daaa0d30c4c2d089)static inline size\_t [rtio\_mempool\_block\_size](group__rtio.md#ga4213be028b0a1264daaa0d30c4c2d089)(const struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2))

378{

379#ifndef CONFIG\_RTIO\_SYS\_MEM\_BLOCKS

380 ARG\_UNUSED([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2));

381 return 0;

382#else

383 if ([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) == NULL || [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->block\_pool == NULL) {

384 return 0;

385 }

386 return [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->block\_pool->info.blk\_sz\_shift);

387#endif

388}

389

397#ifdef CONFIG\_RTIO\_SYS\_MEM\_BLOCKS

398static inline [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \_\_rtio\_compute\_mempool\_block\_index(const struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2), const void \*ptr)

399{

400 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) addr = ([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808))ptr;

401 struct sys\_mem\_blocks \*mem\_pool = [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->block\_pool;

402 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size = [rtio\_mempool\_block\_size](group__rtio.md#ga4213be028b0a1264daaa0d30c4c2d089)([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2));

403

404 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) buff = ([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808))mem\_pool->buffer;

405 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) buff\_size = mem\_pool->info.num\_blocks \* block\_size;

406

407 if (addr < buff || addr >= buff + buff\_size) {

408 return [UINT16\_MAX](stdint_8h.md#a3ea490c9b3617d4479bd80ef93cd5602);

409 }

410 return (addr - buff) / block\_size;

411}

412#endif

413

[ 419](structrtio__iodev__sqe.md)struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) {

[ 420](structrtio__iodev__sqe.md#a2bd98599678909c0ddb22f879affa12b) struct [rtio\_sqe](structrtio__sqe.md) [sqe](structrtio__iodev__sqe.md#a2bd98599678909c0ddb22f879affa12b);

[ 421](structrtio__iodev__sqe.md#a1759e0052099d48b534732e6b8c6b341) struct [rtio\_mpsc\_node](structrtio__mpsc__node.md) [q](structrtio__iodev__sqe.md#a1759e0052099d48b534732e6b8c6b341);

[ 422](structrtio__iodev__sqe.md#a2afb82e550e614f87db7cd1bf2c3a352) struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \*[next](structrtio__iodev__sqe.md#a2afb82e550e614f87db7cd1bf2c3a352);

[ 423](structrtio__iodev__sqe.md#a3c3a050793589258eab5ff5ac30f24c8) struct [rtio](structrtio.md) \*[r](structrtio__iodev__sqe.md#a3c3a050793589258eab5ff5ac30f24c8);

424};

425

[ 429](structrtio__iodev__api.md)struct [rtio\_iodev\_api](structrtio__iodev__api.md) {

[ 438](structrtio__iodev__api.md#a6cd795906753535571ec1ecc0e0c430c) void (\*[submit](structrtio__iodev__api.md#a6cd795906753535571ec1ecc0e0c430c))(struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \*iodev\_sqe);

439};

440

[ 444](structrtio__iodev.md)struct [rtio\_iodev](structrtio__iodev.md) {

445 /\* Function pointer table \*/

[ 446](structrtio__iodev.md#a6dfedbfb58356e0647e5c20632656977) const struct [rtio\_iodev\_api](structrtio__iodev__api.md) \*[api](structrtio__iodev.md#a6dfedbfb58356e0647e5c20632656977);

447

448 /\* Queue of RTIO contexts with requests \*/

[ 449](structrtio__iodev.md#a10b6612ee1c8794103c7be8624519bd2) struct [rtio\_mpsc](structrtio__mpsc.md) [iodev\_sq](structrtio__iodev.md#a10b6612ee1c8794103c7be8624519bd2);

450

451 /\* Data associated with this iodev \*/

[ 452](structrtio__iodev.md#af0f3a27fe8dea2161c9a73cb838bdeec) void \*[data](structrtio__iodev.md#af0f3a27fe8dea2161c9a73cb838bdeec);

453};

454

[ 456](group__rtio.md#gad5f073978f641413989d1c6b405d6c36)#define RTIO\_OP\_NOP 0

457

[ 459](group__rtio.md#gafeb05c351207cd1638fa78f6607e1a4a)#define RTIO\_OP\_RX (RTIO\_OP\_NOP+1)

460

[ 462](group__rtio.md#ga8dcaef0cda159e16520a95543ff62827)#define RTIO\_OP\_TX (RTIO\_OP\_RX+1)

463

[ 465](group__rtio.md#ga6f95c0a5fbcc020a0d1102d3b08934bd)#define RTIO\_OP\_TINY\_TX (RTIO\_OP\_TX+1)

466

[ 468](group__rtio.md#ga18e0ff7d44e4c33900106aefad0a8508)#define RTIO\_OP\_CALLBACK (RTIO\_OP\_TINY\_TX+1)

469

[ 471](group__rtio.md#ga9f0e70f5a28be65a8ed67c0257a72692)#define RTIO\_OP\_TXRX (RTIO\_OP\_CALLBACK+1)

472

473

[ 477](group__rtio.md#ga599ee43fdf35e1cf895cbbe9272e4c50)static inline void [rtio\_sqe\_prep\_nop](group__rtio.md#ga599ee43fdf35e1cf895cbbe9272e4c50)(struct [rtio\_sqe](structrtio__sqe.md) \*sqe,

478 const struct [rtio\_iodev](structrtio__iodev.md) \*iodev,

479 void \*userdata)

480{

481 [memset](string_8h.md#a4137694174d4ca2fad886a1db355015c)(sqe, 0, sizeof(struct [rtio\_sqe](structrtio__sqe.md)));

482 sqe->[op](structrtio__sqe.md#a1d8d3e3426e47a2c7f54d98f51acd953) = [RTIO\_OP\_NOP](group__rtio.md#gad5f073978f641413989d1c6b405d6c36);

483 sqe->[iodev](structrtio__sqe.md#a6c784702f011592c84feacd57915bbfc) = iodev;

484 sqe->[userdata](structrtio__sqe.md#a0ed519ee0b5867ff73bdaf37f983c971) = userdata;

485}

486

[ 490](group__rtio.md#ga89c7cc2494e3dda50737f78f1a1376cf)static inline void [rtio\_sqe\_prep\_read](group__rtio.md#ga89c7cc2494e3dda50737f78f1a1376cf)(struct [rtio\_sqe](structrtio__sqe.md) \*sqe,

491 const struct [rtio\_iodev](structrtio__iodev.md) \*iodev,

492 [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) prio,

493 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf,

494 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) len,

495 void \*userdata)

496{

497 [memset](string_8h.md#a4137694174d4ca2fad886a1db355015c)(sqe, 0, sizeof(struct [rtio\_sqe](structrtio__sqe.md)));

498 sqe->[op](structrtio__sqe.md#a1d8d3e3426e47a2c7f54d98f51acd953) = [RTIO\_OP\_RX](group__rtio.md#gafeb05c351207cd1638fa78f6607e1a4a);

499 sqe->[prio](structrtio__sqe.md#a528eb9b721be7b8a8898ab16a7e2d9a7) = prio;

500 sqe->[iodev](structrtio__sqe.md#a6c784702f011592c84feacd57915bbfc) = iodev;

501 sqe->[buf\_len](structrtio__sqe.md#a67376f40a13960b152a23da250275722) = len;

502 sqe->[buf](structrtio__sqe.md#a55e98f27b26393fee8e179b7bdb6a52e) = buf;

503 sqe->[userdata](structrtio__sqe.md#a0ed519ee0b5867ff73bdaf37f983c971) = userdata;

504}

505

[ 511](group__rtio.md#ga15c1f623658d27d300d1a31a6f3d6b9d)static inline void [rtio\_sqe\_prep\_read\_with\_pool](group__rtio.md#ga15c1f623658d27d300d1a31a6f3d6b9d)(struct [rtio\_sqe](structrtio__sqe.md) \*sqe,

512 const struct [rtio\_iodev](structrtio__iodev.md) \*iodev, [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) prio,

513 void \*userdata)

514{

515 [rtio\_sqe\_prep\_read](group__rtio.md#ga89c7cc2494e3dda50737f78f1a1376cf)(sqe, iodev, prio, NULL, 0, userdata);

516 sqe->[flags](structrtio__sqe.md#aad2ff8524df0e24b812e77e2393bf5b0) = [RTIO\_SQE\_MEMPOOL\_BUFFER](group__rtio__sqe__flags.md#ga2802b46584220afffa0e959e149d5a4d);

517}

518

[ 519](group__rtio.md#ga9803aa829f8c0eeee746ea7d872c20cc)static inline void [rtio\_sqe\_prep\_read\_multishot](group__rtio.md#ga9803aa829f8c0eeee746ea7d872c20cc)(struct [rtio\_sqe](structrtio__sqe.md) \*sqe,

520 const struct [rtio\_iodev](structrtio__iodev.md) \*iodev, [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) prio,

521 void \*userdata)

522{

523 [rtio\_sqe\_prep\_read\_with\_pool](group__rtio.md#ga15c1f623658d27d300d1a31a6f3d6b9d)(sqe, iodev, prio, userdata);

524 sqe->[flags](structrtio__sqe.md#aad2ff8524df0e24b812e77e2393bf5b0) |= [RTIO\_SQE\_MULTISHOT](group__rtio__sqe__flags.md#ga00f8ead8f043fe40d49d0bc3325fb299);

525}

526

[ 530](group__rtio.md#gab01192577dadf7ab83d3f8029c86a149)static inline void [rtio\_sqe\_prep\_write](group__rtio.md#gab01192577dadf7ab83d3f8029c86a149)(struct [rtio\_sqe](structrtio__sqe.md) \*sqe,

531 const struct [rtio\_iodev](structrtio__iodev.md) \*iodev,

532 [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) prio,

533 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf,

534 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) len,

535 void \*userdata)

536{

537 [memset](string_8h.md#a4137694174d4ca2fad886a1db355015c)(sqe, 0, sizeof(struct [rtio\_sqe](structrtio__sqe.md)));

538 sqe->[op](structrtio__sqe.md#a1d8d3e3426e47a2c7f54d98f51acd953) = [RTIO\_OP\_TX](group__rtio.md#ga8dcaef0cda159e16520a95543ff62827);

539 sqe->[prio](structrtio__sqe.md#a528eb9b721be7b8a8898ab16a7e2d9a7) = prio;

540 sqe->[iodev](structrtio__sqe.md#a6c784702f011592c84feacd57915bbfc) = iodev;

541 sqe->[buf\_len](structrtio__sqe.md#a67376f40a13960b152a23da250275722) = len;

542 sqe->[buf](structrtio__sqe.md#a55e98f27b26393fee8e179b7bdb6a52e) = buf;

543 sqe->[userdata](structrtio__sqe.md#a0ed519ee0b5867ff73bdaf37f983c971) = userdata;

544}

545

[ 556](group__rtio.md#ga31be14ece09e061a8d42ca8f2395286a)static inline void [rtio\_sqe\_prep\_tiny\_write](group__rtio.md#ga31be14ece09e061a8d42ca8f2395286a)(struct [rtio\_sqe](structrtio__sqe.md) \*sqe,

557 const struct [rtio\_iodev](structrtio__iodev.md) \*iodev,

558 [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) prio,

559 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*tiny\_write\_data,

560 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) tiny\_write\_len,

561 void \*userdata)

562{

563 \_\_ASSERT\_NO\_MSG(tiny\_write\_len <= sizeof(sqe->[tiny\_buf](structrtio__sqe.md#aceaa9999b86fd271321988e257aeecc8)));

564

565 [memset](string_8h.md#a4137694174d4ca2fad886a1db355015c)(sqe, 0, sizeof(struct [rtio\_sqe](structrtio__sqe.md)));

566 sqe->[op](structrtio__sqe.md#a1d8d3e3426e47a2c7f54d98f51acd953) = [RTIO\_OP\_TINY\_TX](group__rtio.md#ga6f95c0a5fbcc020a0d1102d3b08934bd);

567 sqe->[prio](structrtio__sqe.md#a528eb9b721be7b8a8898ab16a7e2d9a7) = prio;

568 sqe->[iodev](structrtio__sqe.md#a6c784702f011592c84feacd57915bbfc) = iodev;

569 sqe->[tiny\_buf\_len](structrtio__sqe.md#ab25f9d5c2e4d833d548148843a859096) = tiny\_write\_len;

570 [memcpy](string_8h.md#af0f01bffcd16daa9143f6014d10a25ad)(sqe->[tiny\_buf](structrtio__sqe.md#aceaa9999b86fd271321988e257aeecc8), tiny\_write\_data, tiny\_write\_len);

571 sqe->[userdata](structrtio__sqe.md#a0ed519ee0b5867ff73bdaf37f983c971) = userdata;

572}

573

[ 582](group__rtio.md#ga9d0dd7d0e2e3d281092f2350d6e1713e)static inline void [rtio\_sqe\_prep\_callback](group__rtio.md#ga9d0dd7d0e2e3d281092f2350d6e1713e)(struct [rtio\_sqe](structrtio__sqe.md) \*sqe,

583 [rtio\_callback\_t](group__rtio.md#gad1dbd690e6cf88d7c788436dd04d1a00) callback,

584 void \*arg0,

585 void \*userdata)

586{

587 [memset](string_8h.md#a4137694174d4ca2fad886a1db355015c)(sqe, 0, sizeof(struct [rtio\_sqe](structrtio__sqe.md)));

588 sqe->[op](structrtio__sqe.md#a1d8d3e3426e47a2c7f54d98f51acd953) = [RTIO\_OP\_CALLBACK](group__rtio.md#ga18e0ff7d44e4c33900106aefad0a8508);

589 sqe->[prio](structrtio__sqe.md#a528eb9b721be7b8a8898ab16a7e2d9a7) = 0;

590 sqe->[iodev](structrtio__sqe.md#a6c784702f011592c84feacd57915bbfc) = NULL;

591 sqe->[callback](structrtio__sqe.md#af8c31c33e9fedebe55cac73595d0f696) = callback;

592 sqe->[arg0](structrtio__sqe.md#a438d2156a61aef9ca840af9c01d5dfa4) = arg0;

593 sqe->[userdata](structrtio__sqe.md#a0ed519ee0b5867ff73bdaf37f983c971) = userdata;

594}

595

[ 599](group__rtio.md#ga0129e02abc85526199311846e1830869)static inline void [rtio\_sqe\_prep\_transceive](group__rtio.md#ga0129e02abc85526199311846e1830869)(struct [rtio\_sqe](structrtio__sqe.md) \*sqe,

600 const struct [rtio\_iodev](structrtio__iodev.md) \*iodev,

601 [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) prio,

602 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*tx\_buf,

603 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*rx\_buf,

604 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) buf\_len,

605 void \*userdata)

606{

607 [memset](string_8h.md#a4137694174d4ca2fad886a1db355015c)(sqe, 0, sizeof(struct [rtio\_sqe](structrtio__sqe.md)));

608 sqe->[op](structrtio__sqe.md#a1d8d3e3426e47a2c7f54d98f51acd953) = [RTIO\_OP\_TXRX](group__rtio.md#ga9f0e70f5a28be65a8ed67c0257a72692);

609 sqe->[prio](structrtio__sqe.md#a528eb9b721be7b8a8898ab16a7e2d9a7) = prio;

610 sqe->[iodev](structrtio__sqe.md#a6c784702f011592c84feacd57915bbfc) = iodev;

611 sqe->[txrx\_buf\_len](structrtio__sqe.md#ab3cff3dbbfc9b1a0dbe8f1dc28ac83f8) = buf\_len;

612 sqe->[tx\_buf](structrtio__sqe.md#a186c22217961a5eddb75ad0bd84a538a) = tx\_buf;

613 sqe->[rx\_buf](structrtio__sqe.md#a4d2090fc11b897724a883ad1087d9f73) = rx\_buf;

614 sqe->[userdata](structrtio__sqe.md#a0ed519ee0b5867ff73bdaf37f983c971) = userdata;

615}

616

[ 617](group__rtio.md#gae5fb03fc8f3a4a774f476ff552999bfc)static inline struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \*[rtio\_sqe\_pool\_alloc](group__rtio.md#gae5fb03fc8f3a4a774f476ff552999bfc)(struct [rtio\_sqe\_pool](structrtio__sqe__pool.md) \*pool)

618{

619 struct [rtio\_mpsc\_node](structrtio__mpsc__node.md) \*node = [rtio\_mpsc\_pop](group__rtio__mpsc.md#ga11697747c5377ccff4556d9d5dc96e56)(&pool->[free\_q](structrtio__sqe__pool.md#a95f516beb25feb60e44b42cd72d115b8));

620

621 if (node == NULL) {

622 return NULL;

623 }

624

625 struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \*iodev\_sqe = [CONTAINER\_OF](group__sys-util.md#gac5bc561d1bfd1bf68877fe577779bd2f)(node, struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md), [q](structrtio__iodev__sqe.md#a1759e0052099d48b534732e6b8c6b341));

626

627 pool->[pool\_free](structrtio__sqe__pool.md#af7990b1510ad2343573f3e4e502475b0)--;

628

629 return iodev\_sqe;

630}

631

[ 632](group__rtio.md#gac776aea3692cfd77aa5bf675a9e9ed02)static inline void [rtio\_sqe\_pool\_free](group__rtio.md#gac776aea3692cfd77aa5bf675a9e9ed02)(struct [rtio\_sqe\_pool](structrtio__sqe__pool.md) \*pool, struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \*iodev\_sqe)

633{

634 [rtio\_mpsc\_push](group__rtio__mpsc.md#ga3ef9810ee938ecbc352a985baf60ade2)(&pool->[free\_q](structrtio__sqe__pool.md#a95f516beb25feb60e44b42cd72d115b8), &iodev\_sqe->[q](structrtio__iodev__sqe.md#a1759e0052099d48b534732e6b8c6b341));

635

636 pool->[pool\_free](structrtio__sqe__pool.md#af7990b1510ad2343573f3e4e502475b0)++;

637}

638

[ 639](group__rtio.md#ga8497170f55af1d11d717e919f61806f5)static inline struct [rtio\_cqe](structrtio__cqe.md) \*[rtio\_cqe\_pool\_alloc](group__rtio.md#ga8497170f55af1d11d717e919f61806f5)(struct [rtio\_cqe\_pool](structrtio__cqe__pool.md) \*pool)

640{

641 struct [rtio\_mpsc\_node](structrtio__mpsc__node.md) \*node = [rtio\_mpsc\_pop](group__rtio__mpsc.md#ga11697747c5377ccff4556d9d5dc96e56)(&pool->[free\_q](structrtio__cqe__pool.md#afa391fcb1657ca162ff5fd5c854a2013));

642

643 if (node == NULL) {

644 return NULL;

645 }

646

647 struct [rtio\_cqe](structrtio__cqe.md) \*cqe = [CONTAINER\_OF](group__sys-util.md#gac5bc561d1bfd1bf68877fe577779bd2f)(node, struct [rtio\_cqe](structrtio__cqe.md), [q](structrtio__cqe.md#a71836f1322cc64af7153c9e16dc112bc));

648

649 [memset](string_8h.md#a4137694174d4ca2fad886a1db355015c)(cqe, 0, sizeof(struct [rtio\_cqe](structrtio__cqe.md)));

650

651 pool->[pool\_free](structrtio__cqe__pool.md#a4fb501a0ba15e2956113deaf4597d846)--;

652

653 return cqe;

654}

655

[ 656](group__rtio.md#ga23c0c5d4b551858eabe057ecb8a28d12)static inline void [rtio\_cqe\_pool\_free](group__rtio.md#ga23c0c5d4b551858eabe057ecb8a28d12)(struct [rtio\_cqe\_pool](structrtio__cqe__pool.md) \*pool, struct [rtio\_cqe](structrtio__cqe.md) \*cqe)

657{

658 [rtio\_mpsc\_push](group__rtio__mpsc.md#ga3ef9810ee938ecbc352a985baf60ade2)(&pool->[free\_q](structrtio__cqe__pool.md#afa391fcb1657ca162ff5fd5c854a2013), &cqe->[q](structrtio__cqe.md#a71836f1322cc64af7153c9e16dc112bc));

659

660 pool->[pool\_free](structrtio__cqe__pool.md#a4fb501a0ba15e2956113deaf4597d846)++;

661}

662

[ 663](group__rtio.md#ga7f14b99fc1dd0697309e7f71a270f5fb)static inline int [rtio\_block\_pool\_alloc](group__rtio.md#ga7f14b99fc1dd0697309e7f71a270f5fb)(struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2), size\_t min\_sz,

664 size\_t max\_sz, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\*buf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*buf\_len)

665{

666#ifndef CONFIG\_RTIO\_SYS\_MEM\_BLOCKS

667 ARG\_UNUSED([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2));

668 ARG\_UNUSED(min\_sz);

669 ARG\_UNUSED(max\_sz);

670 ARG\_UNUSED(buf);

671 ARG\_UNUSED(buf\_len);

672 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

673#else

674 const [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size = [rtio\_mempool\_block\_size](group__rtio.md#ga4213be028b0a1264daaa0d30c4c2d089)([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2));

675 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) bytes = max\_sz;

676

677 /\* Not every context has a block pool and the block size may return 0 in

678 \* that case

679 \*/

680 if (block\_size == 0) {

681 return -[ENOMEM](group__system__errno.md#ga6a05c923dad0c1208043e9c20a58c8e5);

682 }

683

684 do {

685 size\_t num\_blks = [DIV\_ROUND\_UP](group__sys-util.md#gae664e7492e37d324831caf2321ddda37)(bytes, block\_size);

686 int rc = [sys\_mem\_blocks\_alloc\_contiguous](group__mem__blocks__apis.md#ga72614d0c120f40209837b77d0333bb23)([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->block\_pool, num\_blks, (void \*\*)buf);

687

688 if (rc == 0) {

689 \*buf\_len = num\_blks \* block\_size;

690 return 0;

691 }

692

693 bytes -= block\_size;

694 } while (bytes >= min\_sz);

695

696 return -[ENOMEM](group__system__errno.md#ga6a05c923dad0c1208043e9c20a58c8e5);

697#endif

698}

699

[ 700](group__rtio.md#gafca7732926a9a7c080e3cb16e5f16108)static inline void [rtio\_block\_pool\_free](group__rtio.md#gafca7732926a9a7c080e3cb16e5f16108)(struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2), void \*buf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) buf\_len)

701{

702#ifndef CONFIG\_RTIO\_SYS\_MEM\_BLOCKS

703 ARG\_UNUSED([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2));

704 ARG\_UNUSED(buf);

705 ARG\_UNUSED(buf\_len);

706#else

707 size\_t num\_blks = buf\_len >> [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->block\_pool->info.blk\_sz\_shift;

708

709 [sys\_mem\_blocks\_free\_contiguous](group__mem__blocks__apis.md#ga39e7f8dfe3bda8eabc2372f9a1e87342)([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->block\_pool, buf, num\_blks);

710#endif

711}

712

713/\* Do not try and reformat the macros \*/

714/\* clang-format off \*/

715

[ 723](group__rtio.md#gaae51e2a679d37bc1cfba79961688c406)#define RTIO\_IODEV\_DEFINE(name, iodev\_api, iodev\_data) \

724 STRUCT\_SECTION\_ITERABLE(rtio\_iodev, name) = { \

725 .api = (iodev\_api), \

726 .iodev\_sq = RTIO\_MPSC\_INIT((name.iodev\_sq)), \

727 .data = (iodev\_data), \

728 }

729

730#define Z\_RTIO\_SQE\_POOL\_DEFINE(name, sz) \

731 static struct rtio\_iodev\_sqe \_sqe\_pool\_##name[sz]; \

732 STRUCT\_SECTION\_ITERABLE(rtio\_sqe\_pool, name) = { \

733 .free\_q = RTIO\_MPSC\_INIT((name.free\_q)), \

734 .pool\_size = sz, \

735 .pool\_free = sz, \

736 .pool = \_sqe\_pool\_##name, \

737 }

738

739

740#define Z\_RTIO\_CQE\_POOL\_DEFINE(name, sz) \

741 static struct rtio\_cqe \_cqe\_pool\_##name[sz]; \

742 STRUCT\_SECTION\_ITERABLE(rtio\_cqe\_pool, name) = { \

743 .free\_q = RTIO\_MPSC\_INIT((name.free\_q)), \

744 .pool\_size = sz, \

745 .pool\_free = sz, \

746 .pool = \_cqe\_pool\_##name, \

747 }

748

[ 758](group__rtio.md#ga2437af5061e078950d4a55211d9a902f)#define RTIO\_BMEM COND\_CODE\_1(CONFIG\_USERSPACE, (K\_APP\_BMEM(rtio\_partition) static), (static))

759

[ 769](group__rtio.md#ga3b569c01b71e126cff852df50e98fd69)#define RTIO\_DMEM COND\_CODE\_1(CONFIG\_USERSPACE, (K\_APP\_DMEM(rtio\_partition) static), (static))

770

771#define Z\_RTIO\_BLOCK\_POOL\_DEFINE(name, blk\_sz, blk\_cnt, blk\_align) \

772 RTIO\_BMEM uint8\_t \_\_aligned(WB\_UP(blk\_align)) \

773 \_block\_pool\_##name[blk\_cnt\*WB\_UP(blk\_sz)]; \

774 \_SYS\_MEM\_BLOCKS\_DEFINE\_WITH\_EXT\_BUF(name, WB\_UP(blk\_sz), blk\_cnt, \_block\_pool\_##name, \

775 RTIO\_DMEM)

776

777#define Z\_RTIO\_DEFINE(name, \_sqe\_pool, \_cqe\_pool, \_block\_pool) \

778 IF\_ENABLED(CONFIG\_RTIO\_SUBMIT\_SEM, \

779 (static K\_SEM\_DEFINE(\_submit\_sem\_##name, 0, K\_SEM\_MAX\_LIMIT))) \

780 IF\_ENABLED(CONFIG\_RTIO\_CONSUME\_SEM, \

781 (static K\_SEM\_DEFINE(\_consume\_sem\_##name, 0, K\_SEM\_MAX\_LIMIT))) \

782 STRUCT\_SECTION\_ITERABLE(rtio, name) = { \

783 IF\_ENABLED(CONFIG\_RTIO\_SUBMIT\_SEM, (.submit\_sem = &\_submit\_sem\_##name,)) \

784 IF\_ENABLED(CONFIG\_RTIO\_SUBMIT\_SEM, (.submit\_count = 0,)) \

785 IF\_ENABLED(CONFIG\_RTIO\_CONSUME\_SEM, (.consume\_sem = &\_consume\_sem\_##name,)) \

786 .cq\_count = ATOMIC\_INIT(0), \

787 .xcqcnt = ATOMIC\_INIT(0), \

788 .sqe\_pool = \_sqe\_pool, \

789 .cqe\_pool = \_cqe\_pool, \

790 IF\_ENABLED(CONFIG\_RTIO\_SYS\_MEM\_BLOCKS, (.block\_pool = \_block\_pool,)) \

791 .sq = RTIO\_MPSC\_INIT((name.sq)), \

792 .cq = RTIO\_MPSC\_INIT((name.cq)), \

793 }

794

[ 802](group__rtio.md#ga338df088eabf3b8f7fefb4ac517b21d4)#define RTIO\_DEFINE(name, sq\_sz, cq\_sz) \

803 Z\_RTIO\_SQE\_POOL\_DEFINE(name##\_sqe\_pool, sq\_sz); \

804 Z\_RTIO\_CQE\_POOL\_DEFINE(name##\_cqe\_pool, cq\_sz); \

805 Z\_RTIO\_DEFINE(name, &name##\_sqe\_pool, &name##\_cqe\_pool, NULL) \

806

807/\* clang-format on \*/

808

[ 819](group__rtio.md#gae4c2a9384a9ae4ed16dff914b1184ca8)#define RTIO\_DEFINE\_WITH\_MEMPOOL(name, sq\_sz, cq\_sz, num\_blks, blk\_size, balign) \

820 Z\_RTIO\_SQE\_POOL\_DEFINE(name##\_sqe\_pool, sq\_sz); \

821 Z\_RTIO\_CQE\_POOL\_DEFINE(name##\_cqe\_pool, cq\_sz); \

822 Z\_RTIO\_BLOCK\_POOL\_DEFINE(name##\_block\_pool, blk\_size, num\_blks, balign); \

823 Z\_RTIO\_DEFINE(name, &name##\_sqe\_pool, &name##\_cqe\_pool, &name##\_block\_pool)

824

825/\* clang-format on \*/

826

[ 834](group__rtio.md#ga1f4fb7bccbaae08a94387e4b11275a78)static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [rtio\_sqe\_acquirable](group__rtio.md#ga1f4fb7bccbaae08a94387e4b11275a78)(struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2))

835{

836 return [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->sqe\_pool->pool\_free;

837}

838

[ 847](group__rtio.md#gaef904eb6a8810d8c3ea537c4d6edbee5)static inline struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \*[rtio\_txn\_next](group__rtio.md#gaef904eb6a8810d8c3ea537c4d6edbee5)(const struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \*iodev\_sqe)

848{

849 if (iodev\_sqe->[sqe](structrtio__iodev__sqe.md#a2bd98599678909c0ddb22f879affa12b).[flags](structrtio__sqe.md#aad2ff8524df0e24b812e77e2393bf5b0) & [RTIO\_SQE\_TRANSACTION](group__rtio__sqe__flags.md#ga07f09cc0c95be6cfdddb23f8acacb1ea)) {

850 return iodev\_sqe->[next](structrtio__iodev__sqe.md#a2afb82e550e614f87db7cd1bf2c3a352);

851 } else {

852 return NULL;

853 }

854}

855

856

[ 865](group__rtio.md#gada1e3abf92a46e376138435debc8baf4)static inline struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \*[rtio\_chain\_next](group__rtio.md#gada1e3abf92a46e376138435debc8baf4)(const struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \*iodev\_sqe)

866{

867 if (iodev\_sqe->[sqe](structrtio__iodev__sqe.md#a2bd98599678909c0ddb22f879affa12b).[flags](structrtio__sqe.md#aad2ff8524df0e24b812e77e2393bf5b0) & [RTIO\_SQE\_CHAINED](group__rtio__sqe__flags.md#gae9191d521d4ab602b53fefb74020d06b)) {

868 return iodev\_sqe->[next](structrtio__iodev__sqe.md#a2afb82e550e614f87db7cd1bf2c3a352);

869 } else {

870 return NULL;

871 }

872}

873

[ 882](group__rtio.md#gae690e3dc0fc40dda57257b2eed432719)static inline struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \*[rtio\_iodev\_sqe\_next](group__rtio.md#gae690e3dc0fc40dda57257b2eed432719)(const struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \*iodev\_sqe)

883{

884 return iodev\_sqe->[next](structrtio__iodev__sqe.md#a2afb82e550e614f87db7cd1bf2c3a352);

885}

886

[ 895](group__rtio.md#ga8b47c954d15a334621def53acceb6799)static inline struct [rtio\_sqe](structrtio__sqe.md) \*[rtio\_sqe\_acquire](group__rtio.md#ga8b47c954d15a334621def53acceb6799)(struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2))

896{

897 struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \*iodev\_sqe = [rtio\_sqe\_pool\_alloc](group__rtio.md#gae5fb03fc8f3a4a774f476ff552999bfc)([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->sqe\_pool);

898

899 if (iodev\_sqe == NULL) {

900 return NULL;

901 }

902

903 [rtio\_mpsc\_push](group__rtio__mpsc.md#ga3ef9810ee938ecbc352a985baf60ade2)(&[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->sq, &iodev\_sqe->[q](structrtio__iodev__sqe.md#a1759e0052099d48b534732e6b8c6b341));

904

905 return &iodev\_sqe->[sqe](structrtio__iodev__sqe.md#a2bd98599678909c0ddb22f879affa12b);

906}

907

[ 913](group__rtio.md#ga9486fb7b50e8d2409a50da235203536b)static inline void [rtio\_sqe\_drop\_all](group__rtio.md#ga9486fb7b50e8d2409a50da235203536b)(struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2))

914{

915 struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \*iodev\_sqe;

916 struct [rtio\_mpsc\_node](structrtio__mpsc__node.md) \*node = [rtio\_mpsc\_pop](group__rtio__mpsc.md#ga11697747c5377ccff4556d9d5dc96e56)(&[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->sq);

917

918 while (node != NULL) {

919 iodev\_sqe = [CONTAINER\_OF](group__sys-util.md#gac5bc561d1bfd1bf68877fe577779bd2f)(node, struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md), q);

920 [rtio\_sqe\_pool\_free](group__rtio.md#gac776aea3692cfd77aa5bf675a9e9ed02)([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->sqe\_pool, iodev\_sqe);

921 node = [rtio\_mpsc\_pop](group__rtio__mpsc.md#ga11697747c5377ccff4556d9d5dc96e56)(&[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->sq);

922 }

923}

924

[ 928](group__rtio.md#gad848646651fdf3649b882e5268f72a3c)static inline struct [rtio\_cqe](structrtio__cqe.md) \*[rtio\_cqe\_acquire](group__rtio.md#gad848646651fdf3649b882e5268f72a3c)(struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2))

929{

930 struct [rtio\_cqe](structrtio__cqe.md) \*cqe = [rtio\_cqe\_pool\_alloc](group__rtio.md#ga8497170f55af1d11d717e919f61806f5)([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->cqe\_pool);

931

932 if (cqe == NULL) {

933 return NULL;

934 }

935

936 [memset](string_8h.md#a4137694174d4ca2fad886a1db355015c)(cqe, 0, sizeof(struct [rtio\_cqe](structrtio__cqe.md)));

937

938 return cqe;

939}

940

[ 944](group__rtio.md#ga6f55202adeca60aed0343a7a0dcab071)static inline void [rtio\_cqe\_produce](group__rtio.md#ga6f55202adeca60aed0343a7a0dcab071)(struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2), struct [rtio\_cqe](structrtio__cqe.md) \*cqe)

945{

946 [rtio\_mpsc\_push](group__rtio__mpsc.md#ga3ef9810ee938ecbc352a985baf60ade2)(&[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->cq, &cqe->[q](structrtio__cqe.md#a71836f1322cc64af7153c9e16dc112bc));

947}

948

[ 960](group__rtio.md#gae562cf241911804cdb9f4e3a73b53df4)static inline struct [rtio\_cqe](structrtio__cqe.md) \*[rtio\_cqe\_consume](group__rtio.md#gae562cf241911804cdb9f4e3a73b53df4)(struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2))

961{

962 struct [rtio\_mpsc\_node](structrtio__mpsc__node.md) \*node;

963 struct [rtio\_cqe](structrtio__cqe.md) \*cqe = NULL;

964

965#ifdef CONFIG\_RTIO\_CONSUME\_SEM

966 if ([k\_sem\_take](group__semaphore__apis.md#gac71e2383c1920dddc45a561cacfef090)([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->consume\_sem, [K\_NO\_WAIT](group__clock__apis.md#ga3d9541cfe2e8395af66d186efa77362f)) != 0) {

967 return NULL;

968 }

969#endif

970

971 node = [rtio\_mpsc\_pop](group__rtio__mpsc.md#ga11697747c5377ccff4556d9d5dc96e56)(&[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->cq);

972 if (node == NULL) {

973 return NULL;

974 }

975 cqe = [CONTAINER\_OF](group__sys-util.md#gac5bc561d1bfd1bf68877fe577779bd2f)(node, struct [rtio\_cqe](structrtio__cqe.md), [q](structrtio__cqe.md#a71836f1322cc64af7153c9e16dc112bc));

976

977 return cqe;

978}

979

[ 990](group__rtio.md#gaf617d05d9b59ce1f1d0697617ef6f249)static inline struct [rtio\_cqe](structrtio__cqe.md) \*[rtio\_cqe\_consume\_block](group__rtio.md#gaf617d05d9b59ce1f1d0697617ef6f249)(struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2))

991{

992 struct [rtio\_mpsc\_node](structrtio__mpsc__node.md) \*node;

993 struct [rtio\_cqe](structrtio__cqe.md) \*cqe;

994

995#ifdef CONFIG\_RTIO\_CONSUME\_SEM

996 [k\_sem\_take](group__semaphore__apis.md#gac71e2383c1920dddc45a561cacfef090)([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->consume\_sem, [K\_FOREVER](group__clock__apis.md#ga0bb4b83f0222193b21a8910311bab0ca));

997#endif

998 node = [rtio\_mpsc\_pop](group__rtio__mpsc.md#ga11697747c5377ccff4556d9d5dc96e56)(&[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->cq);

999 while (node == NULL) {

1000 Z\_SPIN\_DELAY(1);

1001 node = [rtio\_mpsc\_pop](group__rtio__mpsc.md#ga11697747c5377ccff4556d9d5dc96e56)(&[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->cq);

1002 }

1003 cqe = [CONTAINER\_OF](group__sys-util.md#gac5bc561d1bfd1bf68877fe577779bd2f)(node, struct [rtio\_cqe](structrtio__cqe.md), [q](structrtio__cqe.md#a71836f1322cc64af7153c9e16dc112bc));

1004

1005 return cqe;

1006}

1007

[ 1014](group__rtio.md#gaa0799a5f8ad98425d385a07c5d27d9cb)static inline void [rtio\_cqe\_release](group__rtio.md#gaa0799a5f8ad98425d385a07c5d27d9cb)(struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2), struct [rtio\_cqe](structrtio__cqe.md) \*cqe)

1015{

1016 [rtio\_cqe\_pool\_free](group__rtio.md#ga23c0c5d4b551858eabe057ecb8a28d12)([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->cqe\_pool, cqe);

1017}

1018

[ 1025](group__rtio.md#ga75661c8c6c94a0ac6254cec674b478c8)static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [rtio\_cqe\_compute\_flags](group__rtio.md#ga75661c8c6c94a0ac6254cec674b478c8)(struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \*iodev\_sqe)

1026{

1027 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) = 0;

1028

1029#ifdef CONFIG\_RTIO\_SYS\_MEM\_BLOCKS

1030 if (iodev\_sqe->[sqe](structrtio__iodev__sqe.md#a2bd98599678909c0ddb22f879affa12b).[op](structrtio__sqe.md#a1d8d3e3426e47a2c7f54d98f51acd953) == [RTIO\_OP\_RX](group__rtio.md#gafeb05c351207cd1638fa78f6607e1a4a) && iodev\_sqe->[sqe](structrtio__iodev__sqe.md#a2bd98599678909c0ddb22f879affa12b).[flags](structrtio__sqe.md#aad2ff8524df0e24b812e77e2393bf5b0) & [RTIO\_SQE\_MEMPOOL\_BUFFER](group__rtio__sqe__flags.md#ga2802b46584220afffa0e959e149d5a4d)) {

1031 struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) = iodev\_sqe->[r](structrtio__iodev__sqe.md#a3c3a050793589258eab5ff5ac30f24c8);

1032 struct sys\_mem\_blocks \*mem\_pool = [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->block\_pool;

1033 int blk\_index = (iodev\_sqe->[sqe](structrtio__iodev__sqe.md#a2bd98599678909c0ddb22f879affa12b).[buf](structrtio__sqe.md#a55e98f27b26393fee8e179b7bdb6a52e) - mem\_pool->buffer) >>

1034 mem\_pool->info.blk\_sz\_shift;

1035 int blk\_count = iodev\_sqe->[sqe](structrtio__iodev__sqe.md#a2bd98599678909c0ddb22f879affa12b).[buf\_len](structrtio__sqe.md#a67376f40a13960b152a23da250275722) >> mem\_pool->info.blk\_sz\_shift;

1036

1037 [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) = [RTIO\_CQE\_FLAG\_PREP\_MEMPOOL](group__rtio__cqe__flags.md#ga28b3a5661248b6b3763aab47417114d6)(blk\_index, blk\_count);

1038 }

1039#else

1040 ARG\_UNUSED(iodev\_sqe);

1041#endif

1042

1043 return [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9);

1044}

1045

[ 1061](group__rtio.md#gaedbf9386a36ed99baa290ef6c318ded1)\_\_syscall int [rtio\_cqe\_get\_mempool\_buffer](group__rtio.md#gaedbf9386a36ed99baa290ef6c318ded1)(const struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2), struct [rtio\_cqe](structrtio__cqe.md) \*cqe,

1062 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\*buff, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*buff\_len);

1063

1064static inline int z\_impl\_rtio\_cqe\_get\_mempool\_buffer(const struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2), struct [rtio\_cqe](structrtio__cqe.md) \*cqe,

1065 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\*buff, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*buff\_len)

1066{

1067#ifdef CONFIG\_RTIO\_SYS\_MEM\_BLOCKS

1068 if ([RTIO\_CQE\_FLAG\_GET](group__rtio__cqe__flags.md#gaef64ea020a20ac22a0edcb6eca032efc)(cqe->[flags](structrtio__cqe.md#a8a7632ef1cfd31529d782bd761908d93)) == [RTIO\_CQE\_FLAG\_MEMPOOL\_BUFFER](group__rtio__cqe__flags.md#ga0f212500447a5e37e225a6997953b609)) {

1069 int blk\_idx = [RTIO\_CQE\_FLAG\_MEMPOOL\_GET\_BLK\_IDX](group__rtio__cqe__flags.md#ga0b5f3f7e7be472ecf87bd2b08c1888da)(cqe->[flags](structrtio__cqe.md#a8a7632ef1cfd31529d782bd761908d93));

1070 int blk\_count = [RTIO\_CQE\_FLAG\_MEMPOOL\_GET\_BLK\_CNT](group__rtio__cqe__flags.md#ga087465f866d417d5332602bb582cc1a7)(cqe->[flags](structrtio__cqe.md#a8a7632ef1cfd31529d782bd761908d93));

1071 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) blk\_size = [rtio\_mempool\_block\_size](group__rtio.md#ga4213be028b0a1264daaa0d30c4c2d089)([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2));

1072

1073 \*buff = [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->block\_pool->buffer + blk\_idx \* blk\_size;

1074 \*buff\_len = blk\_count \* blk\_size;

1075 \_\_ASSERT\_NO\_MSG(\*buff >= [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->block\_pool->buffer);

1076 \_\_ASSERT\_NO\_MSG(\*buff <

1077 [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->block\_pool->buffer + blk\_size \* [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->block\_pool->info.num\_blocks);

1078 return 0;

1079 }

1080 return -[EINVAL](group__system__errno.md#ga2d1678d5a7cc8ce499643f3b8957def4);

1081#else

1082 ARG\_UNUSED([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2));

1083 ARG\_UNUSED(cqe);

1084 ARG\_UNUSED(buff);

1085 ARG\_UNUSED(buff\_len);

1086

1087 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

1088#endif

1089}

1090

[ 1091](group__rtio.md#gaf191153e83de72ddefb998daad02fa16)void [rtio\_executor\_submit](group__rtio.md#gaf191153e83de72ddefb998daad02fa16)(struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2));

[ 1092](group__rtio.md#ga7e2ebd9abaf585207bc5b99c5d815c6a)void [rtio\_executor\_ok](group__rtio.md#ga7e2ebd9abaf585207bc5b99c5d815c6a)(struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \*iodev\_sqe, int result);

[ 1093](group__rtio.md#ga15f4a1a4dfb869ef9e4216dc1c1cdc8a)void [rtio\_executor\_err](group__rtio.md#ga15f4a1a4dfb869ef9e4216dc1c1cdc8a)(struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \*iodev\_sqe, int result);

1094

[ 1103](group__rtio.md#gacb1d2ffa2b07418d8a8aa319bd4336ab)static inline void [rtio\_iodev\_sqe\_ok](group__rtio.md#gacb1d2ffa2b07418d8a8aa319bd4336ab)(struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \*iodev\_sqe, int result)

1104{

1105 [rtio\_executor\_ok](group__rtio.md#ga7e2ebd9abaf585207bc5b99c5d815c6a)(iodev\_sqe, result);

1106}

1107

[ 1116](group__rtio.md#gaada07aa6acefa548743b525225fa482f)static inline void [rtio\_iodev\_sqe\_err](group__rtio.md#gaada07aa6acefa548743b525225fa482f)(struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \*iodev\_sqe, int result)

1117{

1118 [rtio\_executor\_err](group__rtio.md#ga15f4a1a4dfb869ef9e4216dc1c1cdc8a)(iodev\_sqe, result);

1119}

1120

[ 1126](group__rtio.md#ga3a2d5e6daebe7b6e557706c75e7f8a41)static inline void [rtio\_iodev\_cancel\_all](group__rtio.md#ga3a2d5e6daebe7b6e557706c75e7f8a41)(struct [rtio\_iodev](structrtio__iodev.md) \*iodev)

1127{

1128 /\* Clear pending requests as -ENODATA \*/

1129 struct [rtio\_mpsc\_node](structrtio__mpsc__node.md) \*node = [rtio\_mpsc\_pop](group__rtio__mpsc.md#ga11697747c5377ccff4556d9d5dc96e56)(&iodev->[iodev\_sq](structrtio__iodev.md#a10b6612ee1c8794103c7be8624519bd2));

1130

1131 while (node != NULL) {

1132 struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \*iodev\_sqe = [CONTAINER\_OF](group__sys-util.md#gac5bc561d1bfd1bf68877fe577779bd2f)(node, struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md), [q](structrtio__iodev__sqe.md#a1759e0052099d48b534732e6b8c6b341));

1133

1134 [rtio\_iodev\_sqe\_err](group__rtio.md#gaada07aa6acefa548743b525225fa482f)(iodev\_sqe, -[ECANCELED](group__system__errno.md#ga9532d840ef91fd8e1ecc5d7ca7cbf212));

1135 node = [rtio\_mpsc\_pop](group__rtio__mpsc.md#ga11697747c5377ccff4556d9d5dc96e56)(&iodev->[iodev\_sq](structrtio__iodev.md#a10b6612ee1c8794103c7be8624519bd2));

1136 }

1137}

1138

[ 1150](group__rtio.md#ga4abc221d5a90ab882000a72caa0ebd0f)static inline void [rtio\_cqe\_submit](group__rtio.md#ga4abc221d5a90ab882000a72caa0ebd0f)(struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2), int result, void \*userdata, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9))

1151{

1152 struct [rtio\_cqe](structrtio__cqe.md) \*cqe = [rtio\_cqe\_acquire](group__rtio.md#gad848646651fdf3649b882e5268f72a3c)([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2));

1153

1154 if (cqe == NULL) {

1155 [atomic\_inc](group__atomic__apis.md#gaae47a9cbe5a6534967b417f602b37ac2)(&[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->xcqcnt);

1156 } else {

1157 cqe->[result](structrtio__cqe.md#acbe2e6607a752b676d9336b9ca6ce435) = [result](structrtio__cqe.md#acbe2e6607a752b676d9336b9ca6ce435);

1158 cqe->[userdata](structrtio__cqe.md#a15128387ccbea55812ef229eab7241e7) = [userdata](structrtio__cqe.md#a15128387ccbea55812ef229eab7241e7);

1159 cqe->[flags](structrtio__cqe.md#a8a7632ef1cfd31529d782bd761908d93) = [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9);

1160 [rtio\_cqe\_produce](group__rtio.md#ga6f55202adeca60aed0343a7a0dcab071)([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2), cqe);

1161 }

1162

1163 [atomic\_inc](group__atomic__apis.md#gaae47a9cbe5a6534967b417f602b37ac2)(&[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->cq\_count);

1164#ifdef CONFIG\_RTIO\_SUBMIT\_SEM

1165 if ([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->submit\_count > 0) {

1166 [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->submit\_count--;

1167 if ([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->submit\_count == 0) {

1168 [k\_sem\_give](group__semaphore__apis.md#gab9be3cf1988af2cd6afdace52d497c84)([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->submit\_sem);

1169 }

1170 }

1171#endif

1172#ifdef CONFIG\_RTIO\_CONSUME\_SEM

1173 [k\_sem\_give](group__semaphore__apis.md#gab9be3cf1988af2cd6afdace52d497c84)([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->consume\_sem);

1174#endif

1175}

1176

1177#define \_\_RTIO\_MEMPOOL\_GET\_NUM\_BLKS(num\_bytes, blk\_size) (((num\_bytes) + (blk\_size)-1) / (blk\_size))

1178

[ 1191](group__rtio.md#gaab6843e2038d00a8354f57d7e2ffcf7e)static inline int [rtio\_sqe\_rx\_buf](group__rtio.md#gaab6843e2038d00a8354f57d7e2ffcf7e)(const struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \*iodev\_sqe, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) min\_buf\_len,

1192 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) max\_buf\_len, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\*buf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*buf\_len)

1193{

1194 struct [rtio\_sqe](structrtio__sqe.md) \*sqe = (struct [rtio\_sqe](structrtio__sqe.md) \*)&iodev\_sqe->[sqe](structrtio__iodev__sqe.md#a2bd98599678909c0ddb22f879affa12b);

1195

1196#ifdef CONFIG\_RTIO\_SYS\_MEM\_BLOCKS

1197 if (sqe->[op](structrtio__sqe.md#a1d8d3e3426e47a2c7f54d98f51acd953) == [RTIO\_OP\_RX](group__rtio.md#gafeb05c351207cd1638fa78f6607e1a4a) && sqe->[flags](structrtio__sqe.md#aad2ff8524df0e24b812e77e2393bf5b0) & [RTIO\_SQE\_MEMPOOL\_BUFFER](group__rtio__sqe__flags.md#ga2802b46584220afffa0e959e149d5a4d)) {

1198 struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) = iodev\_sqe->[r](structrtio__iodev__sqe.md#a3c3a050793589258eab5ff5ac30f24c8);

1199

1200 if (sqe->[buf](structrtio__sqe.md#a55e98f27b26393fee8e179b7bdb6a52e) != NULL) {

1201 if (sqe->[buf\_len](structrtio__sqe.md#a67376f40a13960b152a23da250275722) < min\_buf\_len) {

1202 return -[ENOMEM](group__system__errno.md#ga6a05c923dad0c1208043e9c20a58c8e5);

1203 }

1204 \*buf = sqe->[buf](structrtio__sqe.md#a55e98f27b26393fee8e179b7bdb6a52e);

1205 \*buf\_len = sqe->[buf\_len](structrtio__sqe.md#a67376f40a13960b152a23da250275722);

1206 return 0;

1207 }

1208

1209 int rc = [rtio\_block\_pool\_alloc](group__rtio.md#ga7f14b99fc1dd0697309e7f71a270f5fb)([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2), min\_buf\_len, max\_buf\_len, buf, buf\_len);

1210 if (rc == 0) {

1211 sqe->[buf](structrtio__sqe.md#a55e98f27b26393fee8e179b7bdb6a52e) = \*buf;

1212 sqe->[buf\_len](structrtio__sqe.md#a67376f40a13960b152a23da250275722) = \*buf\_len;

1213 return 0;

1214 }

1215

1216 return -[ENOMEM](group__system__errno.md#ga6a05c923dad0c1208043e9c20a58c8e5);

1217 }

1218#else

1219 ARG\_UNUSED(max\_buf\_len);

1220#endif

1221

1222 if (sqe->[buf\_len](structrtio__sqe.md#a67376f40a13960b152a23da250275722) < min\_buf\_len) {

1223 return -[ENOMEM](group__system__errno.md#ga6a05c923dad0c1208043e9c20a58c8e5);

1224 }

1225

1226 \*buf = sqe->[buf](structrtio__sqe.md#a55e98f27b26393fee8e179b7bdb6a52e);

1227 \*buf\_len = sqe->[buf\_len](structrtio__sqe.md#a67376f40a13960b152a23da250275722);

1228 return 0;

1229}

1230

[ 1245](group__rtio.md#ga6530bf56ccbab046a362a6448f941609)\_\_syscall void [rtio\_release\_buffer](group__rtio.md#ga6530bf56ccbab046a362a6448f941609)(struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2), void \*buff, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) buff\_len);

1246

1247static inline void z\_impl\_rtio\_release\_buffer(struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2), void \*buff, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) buff\_len)

1248{

1249#ifdef CONFIG\_RTIO\_SYS\_MEM\_BLOCKS

1250 if ([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) == NULL || buff == NULL || [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->block\_pool == NULL || buff\_len == 0) {

1251 return;

1252 }

1253

1254 [rtio\_block\_pool\_free](group__rtio.md#gafca7732926a9a7c080e3cb16e5f16108)([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2), buff, buff\_len);

1255#else

1256 ARG\_UNUSED([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2));

1257 ARG\_UNUSED(buff);

1258 ARG\_UNUSED(buff\_len);

1259#endif

1260}

1261

[ 1265](group__rtio.md#ga9da42c98546930575525f0f92710f9e4)static inline void [rtio\_access\_grant](group__rtio.md#ga9da42c98546930575525f0f92710f9e4)(struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2), struct [k\_thread](structk__thread.md) \*t)

1266{

1267 [k\_object\_access\_grant](group__usermode__apis.md#ga94087bedf96fe2a2bea437d3d585ca22)([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2), t);

1268

1269#ifdef CONFIG\_RTIO\_SUBMIT\_SEM

1270 [k\_object\_access\_grant](group__usermode__apis.md#ga94087bedf96fe2a2bea437d3d585ca22)([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->submit\_sem, t);

1271#endif

1272

1273#ifdef CONFIG\_RTIO\_CONSUME\_SEM

1274 [k\_object\_access\_grant](group__usermode__apis.md#ga94087bedf96fe2a2bea437d3d585ca22)([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->consume\_sem, t);

1275#endif

1276}

1277

[ 1288](group__rtio.md#gac01252e55d2848b38c0ed77b71d600a7)\_\_syscall int [rtio\_sqe\_cancel](group__rtio.md#gac01252e55d2848b38c0ed77b71d600a7)(struct [rtio\_sqe](structrtio__sqe.md) \*sqe);

1289

1290static inline int z\_impl\_rtio\_sqe\_cancel(struct [rtio\_sqe](structrtio__sqe.md) \*sqe)

1291{

1292 struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \*iodev\_sqe = [CONTAINER\_OF](group__sys-util.md#gac5bc561d1bfd1bf68877fe577779bd2f)([sqe](structrtio__iodev__sqe.md#a2bd98599678909c0ddb22f879affa12b), struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md), [sqe](structrtio__iodev__sqe.md#a2bd98599678909c0ddb22f879affa12b));

1293

1294 do {

1295 iodev\_sqe->[sqe](structrtio__iodev__sqe.md#a2bd98599678909c0ddb22f879affa12b).[flags](structrtio__sqe.md#aad2ff8524df0e24b812e77e2393bf5b0) |= [RTIO\_SQE\_CANCELED](group__rtio__sqe__flags.md#ga7f7f9b038ab8409f271b1aebc1b95ee6);

1296 iodev\_sqe = [rtio\_iodev\_sqe\_next](group__rtio.md#gae690e3dc0fc40dda57257b2eed432719)(iodev\_sqe);

1297 } while (iodev\_sqe != NULL);

1298

1299 return 0;

1300}

1301

[ 1317](group__rtio.md#ga830863e6c8d9b96f4c473a038cab8f8c)\_\_syscall int [rtio\_sqe\_copy\_in\_get\_handles](group__rtio.md#ga830863e6c8d9b96f4c473a038cab8f8c)(struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2), const struct [rtio\_sqe](structrtio__sqe.md) \*sqes,

1318 struct [rtio\_sqe](structrtio__sqe.md) \*\*handle, size\_t sqe\_count);

1319

1320static inline int z\_impl\_rtio\_sqe\_copy\_in\_get\_handles(struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2), const struct [rtio\_sqe](structrtio__sqe.md) \*sqes,

1321 struct [rtio\_sqe](structrtio__sqe.md) \*\*handle,

1322 size\_t sqe\_count)

1323{

1324 struct [rtio\_sqe](structrtio__sqe.md) \*sqe;

1325 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) acquirable = [rtio\_sqe\_acquirable](group__rtio.md#ga1f4fb7bccbaae08a94387e4b11275a78)([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2));

1326

1327 if (acquirable < sqe\_count) {

1328 return -[ENOMEM](group__system__errno.md#ga6a05c923dad0c1208043e9c20a58c8e5);

1329 }

1330

1331 for (unsigned long i = 0; i < sqe\_count; i++) {

1332 sqe = [rtio\_sqe\_acquire](group__rtio.md#ga8b47c954d15a334621def53acceb6799)([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2));

1333 \_\_ASSERT\_NO\_MSG(sqe != NULL);

1334 if (handle != NULL && i == 0) {

1335 \*handle = sqe;

1336 }

1337 \*sqe = sqes[i];

1338 }

1339

1340 return 0;

1341}

1342

[ 1359](group__rtio.md#ga65e351af0a16dcf504a51ef4eb9316c7)static inline int [rtio\_sqe\_copy\_in](group__rtio.md#ga65e351af0a16dcf504a51ef4eb9316c7)(struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2), const struct [rtio\_sqe](structrtio__sqe.md) \*sqes, size\_t sqe\_count)

1360{

1361 return [rtio\_sqe\_copy\_in\_get\_handles](group__rtio.md#ga830863e6c8d9b96f4c473a038cab8f8c)([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2), sqes, NULL, sqe\_count);

1362}

1363

[ 1379](group__rtio.md#ga98b2bbef95aea342a9b86a9775dd5c3b)\_\_syscall int [rtio\_cqe\_copy\_out](group__rtio.md#ga98b2bbef95aea342a9b86a9775dd5c3b)(struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2),

1380 struct [rtio\_cqe](structrtio__cqe.md) \*cqes,

1381 size\_t cqe\_count,

1382 [k\_timeout\_t](structk__timeout__t.md) timeout);

1383static inline int z\_impl\_rtio\_cqe\_copy\_out(struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2),

1384 struct [rtio\_cqe](structrtio__cqe.md) \*cqes,

1385 size\_t cqe\_count,

1386 [k\_timeout\_t](structk__timeout__t.md) timeout)

1387{

1388 size\_t copied = 0;

1389 struct [rtio\_cqe](structrtio__cqe.md) \*cqe;

1390 [k\_timepoint\_t](structk__timepoint__t.md) end = [sys\_timepoint\_calc](group__clock__apis.md#ga509cf4599c1f162c97540743e8c21d33)(timeout);

1391

1392 do {

1393 cqe = [K\_TIMEOUT\_EQ](group__clock__apis.md#ga9abf00b34e16ab7ad0883603b6778b1b)(timeout, [K\_FOREVER](group__clock__apis.md#ga0bb4b83f0222193b21a8910311bab0ca)) ? [rtio\_cqe\_consume\_block](group__rtio.md#gaf617d05d9b59ce1f1d0697617ef6f249)([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2))

1394 : [rtio\_cqe\_consume](group__rtio.md#gae562cf241911804cdb9f4e3a73b53df4)([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2));

1395 if (cqe == NULL) {

1396#ifdef CONFIG\_BOARD\_NATIVE\_POSIX

1397 /\* Native posix fakes the clock and only moves it forward when sleeping. \*/

1398 [k\_sleep](group__thread__apis.md#ga48d4b041790454da4d68ac8711f29657)([K\_TICKS](group__clock__apis.md#gaeda983960bd25f1dba7a386ad720e395)(1));

1399#else

1400 Z\_SPIN\_DELAY(1);

1401#endif

1402 continue;

1403 }

1404 cqes[copied++] = \*cqe;

1405 [rtio\_cqe\_release](group__rtio.md#gaa0799a5f8ad98425d385a07c5d27d9cb)([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2), cqe);

1406 } while (copied < cqe\_count && ![sys\_timepoint\_expired](group__clock__apis.md#ga87d0d7a0f7bcdcc8c4909962eac12985)(end));

1407

1408 return copied;

1409}

1410

[ 1424](group__rtio.md#gafee27c64a4a4989c4eb774addde8eb2e)\_\_syscall int [rtio\_submit](group__rtio.md#gafee27c64a4a4989c4eb774addde8eb2e)(struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2), [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) wait\_count);

1425

1426static inline int z\_impl\_rtio\_submit(struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2), [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) wait\_count)

1427{

1428 int res = 0;

1429

1430#ifdef CONFIG\_RTIO\_SUBMIT\_SEM

1431 /\* TODO undefined behavior if another thread calls submit of course

1432 \*/

1433 if (wait\_count > 0) {

1434 \_\_ASSERT(![k\_is\_in\_isr](group__isr__apis.md#ga8482b0dd2283d12677a9ebe321667d16)(),

1435 "expected rtio submit with wait count to be called from a thread");

1436

1437 [k\_sem\_reset](group__semaphore__apis.md#ga1bd12d8d8c1b9c6be9b665d0fefe5562)([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->submit\_sem);

1438 [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->submit\_count = wait\_count;

1439 }

1440#else

1441 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) cq\_count = ([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808))[atomic\_get](group__atomic__apis.md#ga33bb426a17535bd1022895a7e44b32fa)(&[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->cq\_count) + wait\_count;

1442#endif

1443

1444 /\* Submit the queue to the executor which consumes submissions

1445 \* and produces completions through ISR chains or other means.

1446 \*/

1447 [rtio\_executor\_submit](group__rtio.md#gaf191153e83de72ddefb998daad02fa16)([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2));

1448

1449

1450 /\* TODO could be nicer if we could suspend the thread and not

1451 \* wake up on each completion here.

1452 \*/

1453#ifdef CONFIG\_RTIO\_SUBMIT\_SEM

1454

1455 if (wait\_count > 0) {

1456 res = [k\_sem\_take](group__semaphore__apis.md#gac71e2383c1920dddc45a561cacfef090)([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->submit\_sem, [K\_FOREVER](group__clock__apis.md#ga0bb4b83f0222193b21a8910311bab0ca));

1457 \_\_ASSERT(res == 0,

1458 "semaphore was reset or timed out while waiting on completions!");

1459 }

1460#else

1461 while (([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808))[atomic\_get](group__atomic__apis.md#ga33bb426a17535bd1022895a7e44b32fa)(&[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->cq\_count) < cq\_count) {

1462 Z\_SPIN\_DELAY(10);

1463 [k\_yield](group__thread__apis.md#ga08a3484c33444ecedc2d71d78495a295)();

1464 }

1465#endif

1466

1467 return res;

1468}

1469

1473

1474#ifdef \_\_cplusplus

1475}

1476#endif

1477

1478#include <syscalls/rtio.h>

1479

1480#endif /\* ZEPHYR\_INCLUDE\_RTIO\_RTIO\_H\_ \*/

[\_\_assert.h](____assert_8h.md)

[app\_memdomain.h](app__memdomain_8h.md)

[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)

workaround assembler barfing for ST r

**Definition** asm-macro-32-bit-gnu.h:24

[atomic.h](atomic_8h.md)

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

**Definition** kernel.h:1361

[K\_NO\_WAIT](group__clock__apis.md#ga3d9541cfe2e8395af66d186efa77362f)

#define K\_NO\_WAIT

Generate null timeout delay.

**Definition** kernel.h:1251

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

**Definition** kernel.h:1303

[k\_is\_in\_isr](group__isr__apis.md#ga8482b0dd2283d12677a9ebe321667d16)

bool k\_is\_in\_isr(void)

Determine if code is running at interrupt level.

[sys\_mem\_blocks\_free\_contiguous](group__mem__blocks__apis.md#ga39e7f8dfe3bda8eabc2372f9a1e87342)

int sys\_mem\_blocks\_free\_contiguous(sys\_mem\_blocks\_t \*mem\_block, void \*block, size\_t count)

Free contiguous multiple memory blocks.

[sys\_mem\_blocks\_alloc\_contiguous](group__mem__blocks__apis.md#ga72614d0c120f40209837b77d0333bb23)

int sys\_mem\_blocks\_alloc\_contiguous(sys\_mem\_blocks\_t \*mem\_block, size\_t count, void \*\*out\_block)

Allocate a contiguous set of memory blocks.

[RTIO\_CQE\_FLAG\_MEMPOOL\_GET\_BLK\_CNT](group__rtio__cqe__flags.md#ga087465f866d417d5332602bb582cc1a7)

#define RTIO\_CQE\_FLAG\_MEMPOOL\_GET\_BLK\_CNT(flags)

Get the block count of a mempool flags.

**Definition** rtio.h:176

[RTIO\_CQE\_FLAG\_MEMPOOL\_GET\_BLK\_IDX](group__rtio__cqe__flags.md#ga0b5f3f7e7be472ecf87bd2b08c1888da)

#define RTIO\_CQE\_FLAG\_MEMPOOL\_GET\_BLK\_IDX(flags)

Get the block index of a mempool flags.

**Definition** rtio.h:168

[RTIO\_CQE\_FLAG\_MEMPOOL\_BUFFER](group__rtio__cqe__flags.md#ga0f212500447a5e37e225a6997953b609)

#define RTIO\_CQE\_FLAG\_MEMPOOL\_BUFFER

The entry's buffer was allocated from the RTIO's mempool.

**Definition** rtio.h:158

[RTIO\_CQE\_FLAG\_PREP\_MEMPOOL](group__rtio__cqe__flags.md#ga28b3a5661248b6b3763aab47417114d6)

#define RTIO\_CQE\_FLAG\_PREP\_MEMPOOL(blk\_idx, blk\_cnt)

Prepare CQE flags for a mempool read.

**Definition** rtio.h:185

[RTIO\_CQE\_FLAG\_GET](group__rtio__cqe__flags.md#gaef64ea020a20ac22a0edcb6eca032efc)

#define RTIO\_CQE\_FLAG\_GET(flags)

**Definition** rtio.h:160

[rtio\_mpsc\_pop](group__rtio__mpsc.md#ga11697747c5377ccff4556d9d5dc96e56)

static struct rtio\_mpsc\_node \* rtio\_mpsc\_pop(struct rtio\_mpsc \*q)

Pop a node off of the list.

**Definition** rtio\_mpsc.h:147

[rtio\_mpsc\_push](group__rtio__mpsc.md#ga3ef9810ee938ecbc352a985baf60ade2)

static ALWAYS\_INLINE void rtio\_mpsc\_push(struct rtio\_mpsc \*q, struct rtio\_mpsc\_node \*n)

Push a node.

**Definition** rtio\_mpsc.h:128

[RTIO\_SQE\_MULTISHOT](group__rtio__sqe__flags.md#ga00f8ead8f043fe40d49d0bc3325fb299)

#define RTIO\_SQE\_MULTISHOT

The SQE should continue producing CQEs until canceled.

**Definition** rtio.h:134

[RTIO\_SQE\_TRANSACTION](group__rtio__sqe__flags.md#ga07f09cc0c95be6cfdddb23f8acacb1ea)

#define RTIO\_SQE\_TRANSACTION

The next request in the queue is part of a transaction.

**Definition** rtio.h:106

[RTIO\_SQE\_MEMPOOL\_BUFFER](group__rtio__sqe__flags.md#ga2802b46584220afffa0e959e149d5a4d)

#define RTIO\_SQE\_MEMPOOL\_BUFFER

The buffer should be allocated by the RTIO mempool.

**Definition** rtio.h:118

[RTIO\_SQE\_CANCELED](group__rtio__sqe__flags.md#ga7f7f9b038ab8409f271b1aebc1b95ee6)

#define RTIO\_SQE\_CANCELED

The SQE should not execute if possible.

**Definition** rtio.h:126

[RTIO\_SQE\_CHAINED](group__rtio__sqe__flags.md#gae9191d521d4ab602b53fefb74020d06b)

#define RTIO\_SQE\_CHAINED

The next request in the queue should wait on this one.

**Definition** rtio.h:94

[rtio\_sqe\_prep\_transceive](group__rtio.md#ga0129e02abc85526199311846e1830869)

static void rtio\_sqe\_prep\_transceive(struct rtio\_sqe \*sqe, const struct rtio\_iodev \*iodev, int8\_t prio, uint8\_t \*tx\_buf, uint8\_t \*rx\_buf, uint32\_t buf\_len, void \*userdata)

Prepare a transceive op submission.

**Definition** rtio.h:599

[rtio\_sqe\_prep\_read\_with\_pool](group__rtio.md#ga15c1f623658d27d300d1a31a6f3d6b9d)

static void rtio\_sqe\_prep\_read\_with\_pool(struct rtio\_sqe \*sqe, const struct rtio\_iodev \*iodev, int8\_t prio, void \*userdata)

Prepare a read op submission with context's mempool.

**Definition** rtio.h:511

[rtio\_executor\_err](group__rtio.md#ga15f4a1a4dfb869ef9e4216dc1c1cdc8a)

void rtio\_executor\_err(struct rtio\_iodev\_sqe \*iodev\_sqe, int result)

[RTIO\_OP\_CALLBACK](group__rtio.md#ga18e0ff7d44e4c33900106aefad0a8508)

#define RTIO\_OP\_CALLBACK

An operation that calls a given function (callback).

**Definition** rtio.h:468

[rtio\_sqe\_acquirable](group__rtio.md#ga1f4fb7bccbaae08a94387e4b11275a78)

static uint32\_t rtio\_sqe\_acquirable(struct rtio \*r)

Count of acquirable submission queue events.

**Definition** rtio.h:834

[rtio\_cqe\_pool\_free](group__rtio.md#ga23c0c5d4b551858eabe057ecb8a28d12)

static void rtio\_cqe\_pool\_free(struct rtio\_cqe\_pool \*pool, struct rtio\_cqe \*cqe)

**Definition** rtio.h:656

[rtio\_sqe\_prep\_tiny\_write](group__rtio.md#ga31be14ece09e061a8d42ca8f2395286a)

static void rtio\_sqe\_prep\_tiny\_write(struct rtio\_sqe \*sqe, const struct rtio\_iodev \*iodev, int8\_t prio, const uint8\_t \*tiny\_write\_data, uint8\_t tiny\_write\_len, void \*userdata)

Prepare a tiny write op submission.

**Definition** rtio.h:556

[rtio\_iodev\_cancel\_all](group__rtio.md#ga3a2d5e6daebe7b6e557706c75e7f8a41)

static void rtio\_iodev\_cancel\_all(struct rtio\_iodev \*iodev)

Cancel all requests that are pending for the iodev.

**Definition** rtio.h:1126

[rtio\_mempool\_block\_size](group__rtio.md#ga4213be028b0a1264daaa0d30c4c2d089)

static size\_t rtio\_mempool\_block\_size(const struct rtio \*r)

Get the mempool block size of the RTIO context.

**Definition** rtio.h:377

[rtio\_cqe\_submit](group__rtio.md#ga4abc221d5a90ab882000a72caa0ebd0f)

static void rtio\_cqe\_submit(struct rtio \*r, int result, void \*userdata, uint32\_t flags)

Submit a completion queue event with a given result and userdata.

**Definition** rtio.h:1150

[rtio\_sqe\_prep\_nop](group__rtio.md#ga599ee43fdf35e1cf895cbbe9272e4c50)

static void rtio\_sqe\_prep\_nop(struct rtio\_sqe \*sqe, const struct rtio\_iodev \*iodev, void \*userdata)

Prepare a nop (no op) submission.

**Definition** rtio.h:477

[rtio\_release\_buffer](group__rtio.md#ga6530bf56ccbab046a362a6448f941609)

void rtio\_release\_buffer(struct rtio \*r, void \*buff, uint32\_t buff\_len)

Release memory that was allocated by the RTIO's memory pool.

[rtio\_sqe\_copy\_in](group__rtio.md#ga65e351af0a16dcf504a51ef4eb9316c7)

static int rtio\_sqe\_copy\_in(struct rtio \*r, const struct rtio\_sqe \*sqes, size\_t sqe\_count)

Copy an array of SQEs into the queue.

**Definition** rtio.h:1359

[rtio\_cqe\_produce](group__rtio.md#ga6f55202adeca60aed0343a7a0dcab071)

static void rtio\_cqe\_produce(struct rtio \*r, struct rtio\_cqe \*cqe)

Produce a complete queue event if available.

**Definition** rtio.h:944

[RTIO\_OP\_TINY\_TX](group__rtio.md#ga6f95c0a5fbcc020a0d1102d3b08934bd)

#define RTIO\_OP\_TINY\_TX

An operation that transmits tiny writes by copying the data to write.

**Definition** rtio.h:465

[rtio\_cqe\_compute\_flags](group__rtio.md#ga75661c8c6c94a0ac6254cec674b478c8)

static uint32\_t rtio\_cqe\_compute\_flags(struct rtio\_iodev\_sqe \*iodev\_sqe)

Compute the CQE flags from the rtio\_iodev\_sqe entry.

**Definition** rtio.h:1025

[rtio\_executor\_ok](group__rtio.md#ga7e2ebd9abaf585207bc5b99c5d815c6a)

void rtio\_executor\_ok(struct rtio\_iodev\_sqe \*iodev\_sqe, int result)

[rtio\_block\_pool\_alloc](group__rtio.md#ga7f14b99fc1dd0697309e7f71a270f5fb)

static int rtio\_block\_pool\_alloc(struct rtio \*r, size\_t min\_sz, size\_t max\_sz, uint8\_t \*\*buf, uint32\_t \*buf\_len)

**Definition** rtio.h:663

[rtio\_sqe\_copy\_in\_get\_handles](group__rtio.md#ga830863e6c8d9b96f4c473a038cab8f8c)

int rtio\_sqe\_copy\_in\_get\_handles(struct rtio \*r, const struct rtio\_sqe \*sqes, struct rtio\_sqe \*\*handle, size\_t sqe\_count)

Copy an array of SQEs into the queue and get resulting handles back.

[rtio\_cqe\_pool\_alloc](group__rtio.md#ga8497170f55af1d11d717e919f61806f5)

static struct rtio\_cqe \* rtio\_cqe\_pool\_alloc(struct rtio\_cqe\_pool \*pool)

**Definition** rtio.h:639

[rtio\_partition](group__rtio.md#ga86a38086dd85150ab6e479d73db1c6d1)

struct k\_mem\_partition rtio\_partition

The memory partition associated with all RTIO context information.

[rtio\_sqe\_prep\_read](group__rtio.md#ga89c7cc2494e3dda50737f78f1a1376cf)

static void rtio\_sqe\_prep\_read(struct rtio\_sqe \*sqe, const struct rtio\_iodev \*iodev, int8\_t prio, uint8\_t \*buf, uint32\_t len, void \*userdata)

Prepare a read op submission.

**Definition** rtio.h:490

[rtio\_sqe\_acquire](group__rtio.md#ga8b47c954d15a334621def53acceb6799)

static struct rtio\_sqe \* rtio\_sqe\_acquire(struct rtio \*r)

Acquire a single submission queue event if available.

**Definition** rtio.h:895

[RTIO\_OP\_TX](group__rtio.md#ga8dcaef0cda159e16520a95543ff62827)

#define RTIO\_OP\_TX

An operation that transmits (writes).

**Definition** rtio.h:462

[rtio\_sqe\_drop\_all](group__rtio.md#ga9486fb7b50e8d2409a50da235203536b)

static void rtio\_sqe\_drop\_all(struct rtio \*r)

Drop all previously acquired sqe.

**Definition** rtio.h:913

[rtio\_sqe\_prep\_read\_multishot](group__rtio.md#ga9803aa829f8c0eeee746ea7d872c20cc)

static void rtio\_sqe\_prep\_read\_multishot(struct rtio\_sqe \*sqe, const struct rtio\_iodev \*iodev, int8\_t prio, void \*userdata)

**Definition** rtio.h:519

[rtio\_cqe\_copy\_out](group__rtio.md#ga98b2bbef95aea342a9b86a9775dd5c3b)

int rtio\_cqe\_copy\_out(struct rtio \*r, struct rtio\_cqe \*cqes, size\_t cqe\_count, k\_timeout\_t timeout)

Copy an array of CQEs from the queue.

[rtio\_sqe\_prep\_callback](group__rtio.md#ga9d0dd7d0e2e3d281092f2350d6e1713e)

static void rtio\_sqe\_prep\_callback(struct rtio\_sqe \*sqe, rtio\_callback\_t callback, void \*arg0, void \*userdata)

Prepare a callback op submission.

**Definition** rtio.h:582

[rtio\_access\_grant](group__rtio.md#ga9da42c98546930575525f0f92710f9e4)

static void rtio\_access\_grant(struct rtio \*r, struct k\_thread \*t)

Grant access to an RTIO context to a user thread.

**Definition** rtio.h:1265

[RTIO\_OP\_TXRX](group__rtio.md#ga9f0e70f5a28be65a8ed67c0257a72692)

#define RTIO\_OP\_TXRX

An operation that transceives (reads and writes simultaneously).

**Definition** rtio.h:471

[rtio\_cqe\_release](group__rtio.md#gaa0799a5f8ad98425d385a07c5d27d9cb)

static void rtio\_cqe\_release(struct rtio \*r, struct rtio\_cqe \*cqe)

Release consumed completion queue event.

**Definition** rtio.h:1014

[rtio\_sqe\_rx\_buf](group__rtio.md#gaab6843e2038d00a8354f57d7e2ffcf7e)

static int rtio\_sqe\_rx\_buf(const struct rtio\_iodev\_sqe \*iodev\_sqe, uint32\_t min\_buf\_len, uint32\_t max\_buf\_len, uint8\_t \*\*buf, uint32\_t \*buf\_len)

Get the buffer associate with the RX submission.

**Definition** rtio.h:1191

[rtio\_iodev\_sqe\_err](group__rtio.md#gaada07aa6acefa548743b525225fa482f)

static void rtio\_iodev\_sqe\_err(struct rtio\_iodev\_sqe \*iodev\_sqe, int result)

Inform the executor of a submissions completion with error.

**Definition** rtio.h:1116

[rtio\_sqe\_prep\_write](group__rtio.md#gab01192577dadf7ab83d3f8029c86a149)

static void rtio\_sqe\_prep\_write(struct rtio\_sqe \*sqe, const struct rtio\_iodev \*iodev, int8\_t prio, uint8\_t \*buf, uint32\_t len, void \*userdata)

Prepare a write op submission.

**Definition** rtio.h:530

[rtio\_sqe\_cancel](group__rtio.md#gac01252e55d2848b38c0ed77b71d600a7)

int rtio\_sqe\_cancel(struct rtio\_sqe \*sqe)

Attempt to cancel an SQE.

[rtio\_sqe\_pool\_free](group__rtio.md#gac776aea3692cfd77aa5bf675a9e9ed02)

static void rtio\_sqe\_pool\_free(struct rtio\_sqe\_pool \*pool, struct rtio\_iodev\_sqe \*iodev\_sqe)

**Definition** rtio.h:632

[rtio\_iodev\_sqe\_ok](group__rtio.md#gacb1d2ffa2b07418d8a8aa319bd4336ab)

static void rtio\_iodev\_sqe\_ok(struct rtio\_iodev\_sqe \*iodev\_sqe, int result)

Inform the executor of a submission completion with success.

**Definition** rtio.h:1103

[rtio\_callback\_t](group__rtio.md#gad1dbd690e6cf88d7c788436dd04d1a00)

void(\* rtio\_callback\_t)(struct rtio \*r, const struct rtio\_sqe \*sqe, void \*arg0)

Callback signature for RTIO\_OP\_CALLBACK.

**Definition** rtio.h:225

[RTIO\_OP\_NOP](group__rtio.md#gad5f073978f641413989d1c6b405d6c36)

#define RTIO\_OP\_NOP

An operation that does nothing and will complete immediately.

**Definition** rtio.h:456

[rtio\_cqe\_acquire](group__rtio.md#gad848646651fdf3649b882e5268f72a3c)

static struct rtio\_cqe \* rtio\_cqe\_acquire(struct rtio \*r)

Acquire a complete queue event if available.

**Definition** rtio.h:928

[rtio\_chain\_next](group__rtio.md#gada1e3abf92a46e376138435debc8baf4)

static struct rtio\_iodev\_sqe \* rtio\_chain\_next(const struct rtio\_iodev\_sqe \*iodev\_sqe)

Get the next sqe in the chain.

**Definition** rtio.h:865

[rtio\_cqe\_consume](group__rtio.md#gae562cf241911804cdb9f4e3a73b53df4)

static struct rtio\_cqe \* rtio\_cqe\_consume(struct rtio \*r)

Consume a single completion queue event if available.

**Definition** rtio.h:960

[rtio\_sqe\_pool\_alloc](group__rtio.md#gae5fb03fc8f3a4a774f476ff552999bfc)

static struct rtio\_iodev\_sqe \* rtio\_sqe\_pool\_alloc(struct rtio\_sqe\_pool \*pool)

**Definition** rtio.h:617

[rtio\_iodev\_sqe\_next](group__rtio.md#gae690e3dc0fc40dda57257b2eed432719)

static struct rtio\_iodev\_sqe \* rtio\_iodev\_sqe\_next(const struct rtio\_iodev\_sqe \*iodev\_sqe)

Get the next sqe in the chain or transaction.

**Definition** rtio.h:882

[rtio\_cqe\_get\_mempool\_buffer](group__rtio.md#gaedbf9386a36ed99baa290ef6c318ded1)

int rtio\_cqe\_get\_mempool\_buffer(const struct rtio \*r, struct rtio\_cqe \*cqe, uint8\_t \*\*buff, uint32\_t \*buff\_len)

Retrieve the mempool buffer that was allocated for the CQE.

[rtio\_txn\_next](group__rtio.md#gaef904eb6a8810d8c3ea537c4d6edbee5)

static struct rtio\_iodev\_sqe \* rtio\_txn\_next(const struct rtio\_iodev\_sqe \*iodev\_sqe)

Get the next sqe in the transaction.

**Definition** rtio.h:847

[rtio\_executor\_submit](group__rtio.md#gaf191153e83de72ddefb998daad02fa16)

void rtio\_executor\_submit(struct rtio \*r)

[rtio\_cqe\_consume\_block](group__rtio.md#gaf617d05d9b59ce1f1d0697617ef6f249)

static struct rtio\_cqe \* rtio\_cqe\_consume\_block(struct rtio \*r)

Wait for and consume a single completion queue event.

**Definition** rtio.h:990

[rtio\_block\_pool\_free](group__rtio.md#gafca7732926a9a7c080e3cb16e5f16108)

static void rtio\_block\_pool\_free(struct rtio \*r, void \*buf, uint32\_t buf\_len)

**Definition** rtio.h:700

[RTIO\_OP\_RX](group__rtio.md#gafeb05c351207cd1638fa78f6607e1a4a)

#define RTIO\_OP\_RX

An operation that receives (reads).

**Definition** rtio.h:459

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

**Definition** util.h:265

[DIV\_ROUND\_UP](group__sys-util.md#gae664e7492e37d324831caf2321ddda37)

#define DIV\_ROUND\_UP(n, d)

Divide and round up.

**Definition** util.h:318

[EINVAL](group__system__errno.md#ga2d1678d5a7cc8ce499643f3b8957def4)

#define EINVAL

Invalid argument.

**Definition** errno.h:61

[ENOMEM](group__system__errno.md#ga6a05c923dad0c1208043e9c20a58c8e5)

#define ENOMEM

Not enough core.

**Definition** errno.h:51

[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33)

#define ENOTSUP

Unsupported value.

**Definition** errno.h:115

[ECANCELED](group__system__errno.md#ga9532d840ef91fd8e1ecc5d7ca7cbf212)

#define ECANCELED

Operation canceled.

**Definition** errno.h:118

[k\_yield](group__thread__apis.md#ga08a3484c33444ecedc2d71d78495a295)

void k\_yield(void)

Yield the current thread.

[k\_sleep](group__thread__apis.md#ga48d4b041790454da4d68ac8711f29657)

int32\_t k\_sleep(k\_timeout\_t timeout)

Put the current thread to sleep.

[k\_object\_access\_grant](group__usermode__apis.md#ga94087bedf96fe2a2bea437d3d585ca22)

void k\_object\_access\_grant(const void \*object, struct k\_thread \*thread)

Grant a thread access to a kernel object.

[kernel.h](include_2zephyr_2kernel_8h.md)

Public kernel APIs.

[mem\_blocks.h](mem__blocks_8h.md)

Memory Blocks Allocator.

[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)

flags

**Definition** parser.h:96

[rtio\_mpsc.h](rtio__mpsc_8h.md)

A wait-free intrusive multi producer single consumer (MPSC) queue using a singly linked list.

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

**Definition** thread.h:250

[k\_timeout\_t](structk__timeout__t.md)

Kernel timeout type.

**Definition** sys\_clock.h:65

[k\_timepoint\_t](structk__timepoint__t.md)

Kernel timepoint type.

**Definition** sys\_clock.h:219

[rtio\_cqe\_pool](structrtio__cqe__pool.md)

**Definition** rtio.h:305

[rtio\_cqe\_pool::pool](structrtio__cqe__pool.md#a05584219d473fcf85d46757fa9cea703)

struct rtio\_cqe \* pool

**Definition** rtio.h:309

[rtio\_cqe\_pool::pool\_size](structrtio__cqe__pool.md#a43bf4141673c61493644539987f27fb1)

const uint16\_t pool\_size

**Definition** rtio.h:307

[rtio\_cqe\_pool::pool\_free](structrtio__cqe__pool.md#a4fb501a0ba15e2956113deaf4597d846)

uint16\_t pool\_free

**Definition** rtio.h:308

[rtio\_cqe\_pool::free\_q](structrtio__cqe__pool.md#afa391fcb1657ca162ff5fd5c854a2013)

struct rtio\_mpsc free\_q

**Definition** rtio.h:306

[rtio\_cqe](structrtio__cqe.md)

A completion queue event.

**Definition** rtio.h:290

[rtio\_cqe::userdata](structrtio__cqe.md#a15128387ccbea55812ef229eab7241e7)

void \* userdata

Associated userdata with operation.

**Definition** rtio.h:294

[rtio\_cqe::q](structrtio__cqe.md#a71836f1322cc64af7153c9e16dc112bc)

struct rtio\_mpsc\_node q

**Definition** rtio.h:291

[rtio\_cqe::flags](structrtio__cqe.md#a8a7632ef1cfd31529d782bd761908d93)

uint32\_t flags

Flags associated with the operation.

**Definition** rtio.h:295

[rtio\_cqe::result](structrtio__cqe.md#acbe2e6607a752b676d9336b9ca6ce435)

int32\_t result

Result from operation.

**Definition** rtio.h:293

[rtio\_iodev\_api](structrtio__iodev__api.md)

API that an RTIO IO device should implement.

**Definition** rtio.h:429

[rtio\_iodev\_api::submit](structrtio__iodev__api.md#a6cd795906753535571ec1ecc0e0c430c)

void(\* submit)(struct rtio\_iodev\_sqe \*iodev\_sqe)

Submit to the iodev an entry to work on.

**Definition** rtio.h:438

[rtio\_iodev\_sqe](structrtio__iodev__sqe.md)

Compute the mempool block index for a given pointer.

**Definition** rtio.h:419

[rtio\_iodev\_sqe::q](structrtio__iodev__sqe.md#a1759e0052099d48b534732e6b8c6b341)

struct rtio\_mpsc\_node q

**Definition** rtio.h:421

[rtio\_iodev\_sqe::next](structrtio__iodev__sqe.md#a2afb82e550e614f87db7cd1bf2c3a352)

struct rtio\_iodev\_sqe \* next

**Definition** rtio.h:422

[rtio\_iodev\_sqe::sqe](structrtio__iodev__sqe.md#a2bd98599678909c0ddb22f879affa12b)

struct rtio\_sqe sqe

**Definition** rtio.h:420

[rtio\_iodev\_sqe::r](structrtio__iodev__sqe.md#a3c3a050793589258eab5ff5ac30f24c8)

struct rtio \* r

**Definition** rtio.h:423

[rtio\_iodev](structrtio__iodev.md)

An IO device with a function table for submitting requests.

**Definition** rtio.h:444

[rtio\_iodev::iodev\_sq](structrtio__iodev.md#a10b6612ee1c8794103c7be8624519bd2)

struct rtio\_mpsc iodev\_sq

**Definition** rtio.h:449

[rtio\_iodev::api](structrtio__iodev.md#a6dfedbfb58356e0647e5c20632656977)

const struct rtio\_iodev\_api \* api

**Definition** rtio.h:446

[rtio\_iodev::data](structrtio__iodev.md#af0f3a27fe8dea2161c9a73cb838bdeec)

void \* data

**Definition** rtio.h:452

[rtio\_mpsc\_node](structrtio__mpsc__node.md)

Queue member.

**Definition** rtio\_mpsc.h:81

[rtio\_mpsc](structrtio__mpsc.md)

MPSC Queue.

**Definition** rtio\_mpsc.h:88

[rtio\_sqe\_pool](structrtio__sqe__pool.md)

**Definition** rtio.h:298

[rtio\_sqe\_pool::free\_q](structrtio__sqe__pool.md#a95f516beb25feb60e44b42cd72d115b8)

struct rtio\_mpsc free\_q

**Definition** rtio.h:299

[rtio\_sqe\_pool::pool](structrtio__sqe__pool.md#ab2c0394e175bd8c6f0c02edb315b6c9b)

struct rtio\_iodev\_sqe \* pool

**Definition** rtio.h:302

[rtio\_sqe\_pool::pool\_size](structrtio__sqe__pool.md#ade3b4354d007fe17a7753c26e2121465)

const uint16\_t pool\_size

**Definition** rtio.h:300

[rtio\_sqe\_pool::pool\_free](structrtio__sqe__pool.md#af7990b1510ad2343573f3e4e502475b0)

uint16\_t pool\_free

**Definition** rtio.h:301

[rtio\_sqe](structrtio__sqe.md)

A submission queue event.

**Definition** rtio.h:230

[rtio\_sqe::userdata](structrtio__sqe.md#a0ed519ee0b5867ff73bdaf37f983c971)

void \* userdata

User provided data which is returned upon operation completion.

**Definition** rtio.h:250

[rtio\_sqe::tx\_buf](structrtio__sqe.md#a186c22217961a5eddb75ad0bd84a538a)

uint8\_t \* tx\_buf

**Definition** rtio.h:275

[rtio\_sqe::op](structrtio__sqe.md#a1d8d3e3426e47a2c7f54d98f51acd953)

uint8\_t op

Op code.

**Definition** rtio.h:231

[rtio\_sqe::arg0](structrtio__sqe.md#a438d2156a61aef9ca840af9c01d5dfa4)

void \* arg0

Last argument given to callback.

**Definition** rtio.h:269

[rtio\_sqe::rx\_buf](structrtio__sqe.md#a4d2090fc11b897724a883ad1087d9f73)

uint8\_t \* rx\_buf

**Definition** rtio.h:276

[rtio\_sqe::prio](structrtio__sqe.md#a528eb9b721be7b8a8898ab16a7e2d9a7)

uint8\_t prio

Op priority.

**Definition** rtio.h:233

[rtio\_sqe::buf](structrtio__sqe.md#a55e98f27b26393fee8e179b7bdb6a52e)

uint8\_t \* buf

Buffer to use.

**Definition** rtio.h:257

[rtio\_sqe::buf\_len](structrtio__sqe.md#a67376f40a13960b152a23da250275722)

uint32\_t buf\_len

Length of buffer.

**Definition** rtio.h:256

[rtio\_sqe::iodev](structrtio__sqe.md#a6c784702f011592c84feacd57915bbfc)

const struct rtio\_iodev \* iodev

Device to operation on.

**Definition** rtio.h:241

[rtio\_sqe::flags](structrtio__sqe.md#aad2ff8524df0e24b812e77e2393bf5b0)

uint16\_t flags

Op Flags.

**Definition** rtio.h:235

[rtio\_sqe::tiny\_buf\_len](structrtio__sqe.md#ab25f9d5c2e4d833d548148843a859096)

uint8\_t tiny\_buf\_len

Length of tiny buffer.

**Definition** rtio.h:262

[rtio\_sqe::txrx\_buf\_len](structrtio__sqe.md#ab3cff3dbbfc9b1a0dbe8f1dc28ac83f8)

uint32\_t txrx\_buf\_len

**Definition** rtio.h:274

[rtio\_sqe::tiny\_buf](structrtio__sqe.md#aceaa9999b86fd271321988e257aeecc8)

uint8\_t tiny\_buf[7]

Tiny buffer.

**Definition** rtio.h:263

[rtio\_sqe::callback](structrtio__sqe.md#af8c31c33e9fedebe55cac73595d0f696)

rtio\_callback\_t callback

**Definition** rtio.h:268

[rtio\_sqe::iodev\_flags](structrtio__sqe.md#af979ffa7bd3efaa6cbcb1344404cb985)

uint16\_t iodev\_flags

Op iodev flags.

**Definition** rtio.h:237

[rtio](structrtio.md)

An RTIO context containing what can be viewed as a pair of queues.

**Definition** rtio.h:323

[rtio::cqe\_pool](structrtio.md#a1bce3c3bb0150275ece65975adf3ee4f)

struct rtio\_cqe\_pool \* cqe\_pool

**Definition** rtio.h:353

[rtio::cq](structrtio.md#a1fc6c2dd44420679e273b7a328ed19ec)

struct rtio\_mpsc cq

**Definition** rtio.h:364

[rtio::sq](structrtio.md#a33a715558d60d87c1a47f33dacc9f849)

struct rtio\_mpsc sq

**Definition** rtio.h:361

[rtio::cq\_count](structrtio.md#a358de1033ab4396d1f1baee2699c993f)

atomic\_t cq\_count

**Definition** rtio.h:342

[rtio::sqe\_pool](structrtio.md#a955f012bac623e7c037b5f1dba8e7fda)

struct rtio\_sqe\_pool \* sqe\_pool

**Definition** rtio.h:350

[rtio::xcqcnt](structrtio.md#ac45facdcc6d64cd70113b9b05b2fb086)

atomic\_t xcqcnt

**Definition** rtio.h:347

[iterable\_sections.h](sys_2iterable__sections_8h.md)

[util.h](util_8h.md)

Misc utilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [rtio](dir_2c800b92938ab205b51fc9bd951bff11.md)
- [rtio.h](rtio_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
