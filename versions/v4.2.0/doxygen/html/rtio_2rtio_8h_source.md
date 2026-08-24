---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/rtio_2rtio_8h_source.html
original_path: doxygen/html/rtio_2rtio_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
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

34#include <[zephyr/kernel\_structs.h](kernel__structs_8h.md)>

35#include <[zephyr/sys/\_\_assert.h](____assert_8h.md)>

36#include <[zephyr/sys/atomic.h](sys_2atomic_8h.md)>

37#include <[zephyr/sys/mem\_blocks.h](mem__blocks_8h.md)>

38#include <[zephyr/sys/util.h](sys_2util_8h.md)>

39#include <[zephyr/sys/iterable\_sections.h](sys_2iterable__sections_8h.md)>

40#include <[zephyr/sys/mpsc\_lockfree.h](mpsc__lockfree_8h.md)>

41

42#ifdef \_\_cplusplus

43extern "C" {

44#endif

45

46

55

62

[ 66](group__rtio__sqe__prio.md#gabc81232a7d4b7145d9898afd6ff2ae48)#define RTIO\_PRIO\_LOW 0U

67

[ 71](group__rtio__sqe__prio.md#gab02e27e01b7dd4eb3439df557899ce92)#define RTIO\_PRIO\_NORM 127U

72

[ 76](group__rtio__sqe__prio.md#ga220baa9bf2c8ff0cb6f52f0220e72b30)#define RTIO\_PRIO\_HIGH 255U

77

81

82

89

[ 97](group__rtio__sqe__flags.md#gae9191d521d4ab602b53fefb74020d06b)#define RTIO\_SQE\_CHAINED BIT(0)

98

[ 109](group__rtio__sqe__flags.md#ga07f09cc0c95be6cfdddb23f8acacb1ea)#define RTIO\_SQE\_TRANSACTION BIT(1)

110

111

[ 121](group__rtio__sqe__flags.md#ga2802b46584220afffa0e959e149d5a4d)#define RTIO\_SQE\_MEMPOOL\_BUFFER BIT(2)

122

[ 129](group__rtio__sqe__flags.md#ga7f7f9b038ab8409f271b1aebc1b95ee6)#define RTIO\_SQE\_CANCELED BIT(3)

130

[ 137](group__rtio__sqe__flags.md#ga00f8ead8f043fe40d49d0bc3325fb299)#define RTIO\_SQE\_MULTISHOT BIT(4)

138

[ 142](group__rtio__sqe__flags.md#ga8578ffdb8f53a51b94fa86a6f02d4a11)#define RTIO\_SQE\_NO\_RESPONSE BIT(5)

143

147

154

[ 161](group__rtio__cqe__flags.md#ga0f212500447a5e37e225a6997953b609)#define RTIO\_CQE\_FLAG\_MEMPOOL\_BUFFER BIT(0)

162

[ 163](group__rtio__cqe__flags.md#gaef64ea020a20ac22a0edcb6eca032efc)#define RTIO\_CQE\_FLAG\_GET(flags) FIELD\_GET(GENMASK(7, 0), (flags))

164

[ 171](group__rtio__cqe__flags.md#ga0b5f3f7e7be472ecf87bd2b08c1888da)#define RTIO\_CQE\_FLAG\_MEMPOOL\_GET\_BLK\_IDX(flags) FIELD\_GET(GENMASK(19, 8), (flags))

172

[ 179](group__rtio__cqe__flags.md#ga087465f866d417d5332602bb582cc1a7)#define RTIO\_CQE\_FLAG\_MEMPOOL\_GET\_BLK\_CNT(flags) FIELD\_GET(GENMASK(31, 20), (flags))

180

[ 188](group__rtio__cqe__flags.md#ga28b3a5661248b6b3763aab47417114d6)#define RTIO\_CQE\_FLAG\_PREP\_MEMPOOL(blk\_idx, blk\_cnt) \

189 (FIELD\_PREP(GENMASK(7, 0), RTIO\_CQE\_FLAG\_MEMPOOL\_BUFFER) | \

190 FIELD\_PREP(GENMASK(19, 8), blk\_idx) | FIELD\_PREP(GENMASK(31, 20), blk\_cnt))

191

195

[ 199](group__rtio.md#gaf923e862d2c6a3fbce5eb96781cf86d8)#define RTIO\_IODEV\_I2C\_STOP BIT(1)

200

[ 204](group__rtio.md#gadba1c5eddeecc431000bd92054f55c3a)#define RTIO\_IODEV\_I2C\_RESTART BIT(2)

205

[ 209](group__rtio.md#gaa0c3b047c7205d12775d8d38907119b9)#define RTIO\_IODEV\_I2C\_10\_BITS BIT(3)

210

[ 214](group__rtio.md#ga671a479885f4d9abbdad677ddfbc47df)#define RTIO\_IODEV\_I3C\_STOP BIT(1)

215

[ 219](group__rtio.md#ga9d30e1b8f22da07a25fd379c27dc2afe)#define RTIO\_IODEV\_I3C\_RESTART BIT(2)

220

[ 224](group__rtio.md#ga857a1b2a766faa1438b4b07d73ca05ed)#define RTIO\_IODEV\_I3C\_HDR BIT(3)

225

[ 229](group__rtio.md#ga258aae8fdda81c71d08dc3e26feb843d)#define RTIO\_IODEV\_I3C\_NBCH BIT(4)

230

[ 234](group__rtio.md#ga5e278e6ec0c31de2246c0fa9a96425c8)#define RTIO\_IODEV\_I3C\_HDR\_MODE\_MASK GENMASK(15, 8)

235

[ 239](group__rtio.md#gae2b6caf5fa82cc7dc07508dccfeb423b)#define RTIO\_IODEV\_I3C\_HDR\_MODE\_SET(flags) \

240 FIELD\_PREP(RTIO\_IODEV\_I3C\_HDR\_MODE\_MASK, flags)

241

[ 245](group__rtio.md#ga902a66ba8772f7a2395069e6725776da)#define RTIO\_IODEV\_I3C\_HDR\_MODE\_GET(flags) \

246 FIELD\_GET(RTIO\_IODEV\_I3C\_HDR\_MODE\_MASK, flags)

247

[ 251](group__rtio.md#ga0642bb5c69d01ea0fe148da9b8475328)#define RTIO\_IODEV\_I3C\_HDR\_CMD\_CODE\_MASK GENMASK(22, 16)

252

[ 256](group__rtio.md#ga4d0b165eb8f4a7cc63c35e9f9438ee5a)#define RTIO\_IODEV\_I3C\_HDR\_CMD\_CODE\_SET(flags) \

257 FIELD\_PREP(RTIO\_IODEV\_I3C\_HDR\_CMD\_CODE\_MASK, flags)

258

[ 262](group__rtio.md#ga881fcb3d955aece099266ef5b57e767b)#define RTIO\_IODEV\_I3C\_HDR\_CMD\_CODE\_GET(flags) \

263 FIELD\_GET(RTIO\_IODEV\_I3C\_HDR\_CMD\_CODE\_MASK, flags)

264

266struct [rtio](structrtio.md);

267struct [rtio\_cqe](structrtio__cqe.md);

268struct [rtio\_sqe](structrtio__sqe.md);

269struct [rtio\_sqe\_pool](structrtio__sqe__pool.md);

270struct [rtio\_cqe\_pool](structrtio__cqe__pool.md);

271struct [rtio\_iodev](structrtio__iodev.md);

272struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md);

274

[ 282](group__rtio.md#gad1dbd690e6cf88d7c788436dd04d1a00)typedef void (\*[rtio\_callback\_t](group__rtio.md#gad1dbd690e6cf88d7c788436dd04d1a00))(struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2), const struct [rtio\_sqe](structrtio__sqe.md) \*sqe, void \*[arg0](structrtio__sqe.md#a438d2156a61aef9ca840af9c01d5dfa4));

283

[ 290](group__rtio.md#gab254ffa4d10bfb670bacd1c47c1f8711)typedef void (\*[rtio\_signaled\_t](group__rtio.md#gab254ffa4d10bfb670bacd1c47c1f8711))(struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \*iodev\_sqe, void \*userdata);

291

[ 295](structrtio__sqe.md)struct [rtio\_sqe](structrtio__sqe.md) {

[ 296](structrtio__sqe.md#a1d8d3e3426e47a2c7f54d98f51acd953) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [op](structrtio__sqe.md#a1d8d3e3426e47a2c7f54d98f51acd953);

297

[ 298](structrtio__sqe.md#a528eb9b721be7b8a8898ab16a7e2d9a7) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [prio](structrtio__sqe.md#a528eb9b721be7b8a8898ab16a7e2d9a7);

299

[ 300](structrtio__sqe.md#aad2ff8524df0e24b812e77e2393bf5b0) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [flags](structrtio__sqe.md#aad2ff8524df0e24b812e77e2393bf5b0);

301

[ 302](structrtio__sqe.md#a8bebe5d55aa8549d749466e444fadf91) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [iodev\_flags](structrtio__sqe.md#a8bebe5d55aa8549d749466e444fadf91);

303

[ 304](structrtio__sqe.md#a6c784702f011592c84feacd57915bbfc) const struct [rtio\_iodev](structrtio__iodev.md) \*[iodev](structrtio__sqe.md#a6c784702f011592c84feacd57915bbfc);

305

[ 313](structrtio__sqe.md#a0ed519ee0b5867ff73bdaf37f983c971) void \*[userdata](structrtio__sqe.md#a0ed519ee0b5867ff73bdaf37f983c971);

314

315 union {

316

318 struct {

[ 319](structrtio__sqe.md#a67376f40a13960b152a23da250275722) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [buf\_len](structrtio__sqe.md#a67376f40a13960b152a23da250275722);

[ 320](structrtio__sqe.md#ab71176c084e8b8eb65dfeb3018ae2a49) const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[buf](structrtio__sqe.md#ab71176c084e8b8eb65dfeb3018ae2a49);

[ 321](structrtio__sqe.md#a4399cf25c7e761126a6218c2b7e3192d) } tx;

322

324 struct {

325 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) buf\_len;

[ 326](structrtio__sqe.md#a55e98f27b26393fee8e179b7bdb6a52e) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[buf](structrtio__sqe.md#ab71176c084e8b8eb65dfeb3018ae2a49);

[ 327](structrtio__sqe.md#a37a98afc43f26355c70e7036725b2544) } rx;

328

330 struct {

[ 331](structrtio__sqe.md#a4125148f520b61d0fe3ba156fbb53322) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [buf\_len](structrtio__sqe.md#a67376f40a13960b152a23da250275722);

[ 332](structrtio__sqe.md#a8f0544318fa972be2541ae1e85efc33f) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [buf](structrtio__sqe.md#ab71176c084e8b8eb65dfeb3018ae2a49)[7];

[ 333](structrtio__sqe.md#a19ace9c984538c2022e7f8ecaefa075d) } tiny\_tx;

334

336 struct {

[ 337](structrtio__sqe.md#af8c31c33e9fedebe55cac73595d0f696) [rtio\_callback\_t](group__rtio.md#gad1dbd690e6cf88d7c788436dd04d1a00) [callback](structrtio__sqe.md#af8c31c33e9fedebe55cac73595d0f696);

[ 338](structrtio__sqe.md#a438d2156a61aef9ca840af9c01d5dfa4) void \*[arg0](structrtio__sqe.md#a438d2156a61aef9ca840af9c01d5dfa4);

[ 339](structrtio__sqe.md#add4f73af249b5b548ddf8f5b8d84af2b) } callback;

340

342 struct {

343 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) buf\_len;

[ 344](structrtio__sqe.md#a18bfa63542954f4bb8b924c92c48e931) const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[tx\_buf](structrtio__sqe.md#a18bfa63542954f4bb8b924c92c48e931);

[ 345](structrtio__sqe.md#a4d2090fc11b897724a883ad1087d9f73) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[rx\_buf](structrtio__sqe.md#a4d2090fc11b897724a883ad1087d9f73);

[ 346](structrtio__sqe.md#a5f2511eb361a7a4d54a92fae4d391e8c) } txrx;

347

349 struct {

[ 350](structrtio__sqe.md#a544c75ee10281e10e83f51df5b157d62) [k\_timeout\_t](structk__timeout__t.md) [timeout](structrtio__sqe.md#a544c75ee10281e10e83f51df5b157d62);

[ 351](structrtio__sqe.md#a582d4a8022d237f894034a5a92511587) struct \_timeout [to](structrtio__sqe.md#a582d4a8022d237f894034a5a92511587);

[ 352](structrtio__sqe.md#a9a93700154d745bc1bacc764bbfbe696) } delay;

353

[ 355](structrtio__sqe.md#a07bf344b1b1063b8bea80cf5ba1c1cc5) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [i2c\_config](structrtio__sqe.md#a07bf344b1b1063b8bea80cf5ba1c1cc5);

356

358 struct {

359 /\* enum i3c\_config\_type type; \*/

[ 360](structrtio__sqe.md#aa09a0c93a6e8cfc73278a87942e4af33) int [type](structrtio__sqe.md#aa09a0c93a6e8cfc73278a87942e4af33);

[ 361](structrtio__sqe.md#ac07a16c50a067acc90bd4ab08aae4184) void \*[config](structrtio__sqe.md#ac07a16c50a067acc90bd4ab08aae4184);

[ 362](structrtio__sqe.md#a7f568fc04ec3bd70577d85f03d671d0b) } i3c\_config;

363

365 /\* struct i3c\_ccc\_payload \*ccc\_payload; \*/

[ 366](structrtio__sqe.md#a8d78973983abca8b97cfc5bcdc2dd2f1) void \*[ccc\_payload](structrtio__sqe.md#a8d78973983abca8b97cfc5bcdc2dd2f1);

367

369 struct {

[ 370](structrtio__sqe.md#a45d8aad94aa1dac80c90cf7c0266bcd8) [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) [ok](structrtio__sqe.md#a45d8aad94aa1dac80c90cf7c0266bcd8);

[ 371](structrtio__sqe.md#a597587210c0a574d95c7c84ae9002267) [rtio\_signaled\_t](group__rtio.md#gab254ffa4d10bfb670bacd1c47c1f8711) [callback](structrtio__sqe.md#af8c31c33e9fedebe55cac73595d0f696);

372 void \*[userdata](structrtio__sqe.md#a0ed519ee0b5867ff73bdaf37f983c971);

[ 373](structrtio__sqe.md#a7ed5828c28fd59a34f5aa7262e4ddd20) } await;

374 };

375};

376

378/\* Ensure the rtio\_sqe never grows beyond a common cacheline size of 64 bytes \*/

379BUILD\_ASSERT(sizeof(struct [rtio\_sqe](structrtio__sqe.md)) <= 64);

381

[ 385](structrtio__cqe.md)struct [rtio\_cqe](structrtio__cqe.md) {

[ 386](structrtio__cqe.md#a27272bca31c170f406799633ec82098d) struct [mpsc\_node](structmpsc__node.md) [q](structrtio__cqe.md#a27272bca31c170f406799633ec82098d);

387

[ 388](structrtio__cqe.md#acbe2e6607a752b676d9336b9ca6ce435) [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) [result](structrtio__cqe.md#acbe2e6607a752b676d9336b9ca6ce435);

[ 389](structrtio__cqe.md#a15128387ccbea55812ef229eab7241e7) void \*[userdata](structrtio__cqe.md#a15128387ccbea55812ef229eab7241e7);

[ 390](structrtio__cqe.md#a8a7632ef1cfd31529d782bd761908d93) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](structrtio__cqe.md#a8a7632ef1cfd31529d782bd761908d93);

391};

392

[ 393](structrtio__sqe__pool.md)struct [rtio\_sqe\_pool](structrtio__sqe__pool.md) {

[ 394](structrtio__sqe__pool.md#aed49ea25c952e07a8287919268fd2485) struct [mpsc](structmpsc.md) [free\_q](structrtio__sqe__pool.md#aed49ea25c952e07a8287919268fd2485);

[ 395](structrtio__sqe__pool.md#ade3b4354d007fe17a7753c26e2121465) const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [pool\_size](structrtio__sqe__pool.md#ade3b4354d007fe17a7753c26e2121465);

[ 396](structrtio__sqe__pool.md#af7990b1510ad2343573f3e4e502475b0) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [pool\_free](structrtio__sqe__pool.md#af7990b1510ad2343573f3e4e502475b0);

[ 397](structrtio__sqe__pool.md#ab2c0394e175bd8c6f0c02edb315b6c9b) struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \*[pool](structrtio__sqe__pool.md#ab2c0394e175bd8c6f0c02edb315b6c9b);

398};

399

[ 400](structrtio__cqe__pool.md)struct [rtio\_cqe\_pool](structrtio__cqe__pool.md) {

[ 401](structrtio__cqe__pool.md#a13bd7991ff5622c1cb5aa6af014aaab3) struct [mpsc](structmpsc.md) [free\_q](structrtio__cqe__pool.md#a13bd7991ff5622c1cb5aa6af014aaab3);

[ 402](structrtio__cqe__pool.md#a43bf4141673c61493644539987f27fb1) const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [pool\_size](structrtio__cqe__pool.md#a43bf4141673c61493644539987f27fb1);

[ 403](structrtio__cqe__pool.md#a4fb501a0ba15e2956113deaf4597d846) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [pool\_free](structrtio__cqe__pool.md#a4fb501a0ba15e2956113deaf4597d846);

[ 404](structrtio__cqe__pool.md#a05584219d473fcf85d46757fa9cea703) struct [rtio\_cqe](structrtio__cqe.md) \*[pool](structrtio__cqe__pool.md#a05584219d473fcf85d46757fa9cea703);

405};

406

[ 418](structrtio.md)struct [rtio](structrtio.md) {

419#ifdef CONFIG\_RTIO\_SUBMIT\_SEM

420 /\* A wait semaphore which may suspend the calling thread

421 \* to wait for some number of completions when calling submit

422 \*/

423 struct [k\_sem](structk__sem.md) \*submit\_sem;

424

425 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) submit\_count;

426#endif

427

428#ifdef CONFIG\_RTIO\_CONSUME\_SEM

429 /\* A wait semaphore which may suspend the calling thread

430 \* to wait for some number of completions while consuming

431 \* them from the completion queue

432 \*/

433 struct [k\_sem](structk__sem.md) \*consume\_sem;

434#endif

435

436 /\* Total number of completions \*/

[ 437](structrtio.md#a358de1033ab4396d1f1baee2699c993f) [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) [cq\_count](structrtio.md#a358de1033ab4396d1f1baee2699c993f);

438

439 /\* Number of completions that were unable to be submitted with results

440 \* due to the cq spsc being full

441 \*/

[ 442](structrtio.md#ac45facdcc6d64cd70113b9b05b2fb086) [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) [xcqcnt](structrtio.md#ac45facdcc6d64cd70113b9b05b2fb086);

443

444 /\* Submission queue object pool with free list \*/

[ 445](structrtio.md#a955f012bac623e7c037b5f1dba8e7fda) struct [rtio\_sqe\_pool](structrtio__sqe__pool.md) \*[sqe\_pool](structrtio.md#a955f012bac623e7c037b5f1dba8e7fda);

446

447 /\* Complete queue object pool with free list \*/

[ 448](structrtio.md#a1bce3c3bb0150275ece65975adf3ee4f) struct [rtio\_cqe\_pool](structrtio__cqe__pool.md) \*[cqe\_pool](structrtio.md#a1bce3c3bb0150275ece65975adf3ee4f);

449

450#ifdef CONFIG\_RTIO\_SYS\_MEM\_BLOCKS

451 /\* Mem block pool \*/

452 struct sys\_mem\_blocks \*block\_pool;

453#endif

454

455 /\* Submission queue \*/

[ 456](structrtio.md#a34fbabfdbef3144f4520bf678684cdfb) struct [mpsc](structmpsc.md) [sq](structrtio.md#a34fbabfdbef3144f4520bf678684cdfb);

457

458 /\* Completion queue \*/

[ 459](structrtio.md#ad6f44a354a170cb04a584beee7728fa9) struct [mpsc](structmpsc.md) [cq](structrtio.md#ad6f44a354a170cb04a584beee7728fa9);

460};

461

463extern struct [k\_mem\_partition](structk__mem__partition.md) [rtio\_partition](group__rtio.md#ga86a38086dd85150ab6e479d73db1c6d1);

464

[ 472](group__rtio.md#ga4213be028b0a1264daaa0d30c4c2d089)static inline size\_t [rtio\_mempool\_block\_size](group__rtio.md#ga4213be028b0a1264daaa0d30c4c2d089)(const struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2))

473{

474#ifndef CONFIG\_RTIO\_SYS\_MEM\_BLOCKS

475 ARG\_UNUSED([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2));

476 return 0;

477#else

478 if ([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4) || [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->block\_pool == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

479 return 0;

480 }

481 return [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->block\_pool->info.blk\_sz\_shift);

482#endif

483}

484

492#ifdef CONFIG\_RTIO\_SYS\_MEM\_BLOCKS

493static inline [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \_\_rtio\_compute\_mempool\_block\_index(const struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2), const void \*ptr)

494{

495 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) addr = ([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808))ptr;

496 struct sys\_mem\_blocks \*mem\_pool = [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->block\_pool;

497 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size = [rtio\_mempool\_block\_size](group__rtio.md#ga4213be028b0a1264daaa0d30c4c2d089)([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2));

498

499 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) buff = ([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808))mem\_pool->buffer;

500 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) buff\_size = mem\_pool->info.num\_blocks \* block\_size;

501

502 if (addr < buff || addr >= buff + buff\_size) {

503 return [UINT16\_MAX](stdint_8h.md#a3ea490c9b3617d4479bd80ef93cd5602);

504 }

505 return (addr - buff) / block\_size;

506}

507#endif

508

[ 514](structrtio__iodev__sqe.md)struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) {

[ 515](structrtio__iodev__sqe.md#a2bd98599678909c0ddb22f879affa12b) struct [rtio\_sqe](structrtio__sqe.md) [sqe](structrtio__iodev__sqe.md#a2bd98599678909c0ddb22f879affa12b);

[ 516](structrtio__iodev__sqe.md#a9cfdd004b65a5e2bc111bc2fb333498c) struct [mpsc\_node](structmpsc__node.md) [q](structrtio__iodev__sqe.md#a9cfdd004b65a5e2bc111bc2fb333498c);

[ 517](structrtio__iodev__sqe.md#a2afb82e550e614f87db7cd1bf2c3a352) struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \*[next](structrtio__iodev__sqe.md#a2afb82e550e614f87db7cd1bf2c3a352);

[ 518](structrtio__iodev__sqe.md#a3c3a050793589258eab5ff5ac30f24c8) struct [rtio](structrtio.md) \*[r](structrtio__iodev__sqe.md#a3c3a050793589258eab5ff5ac30f24c8);

519};

520

[ 524](structrtio__iodev__api.md)struct [rtio\_iodev\_api](structrtio__iodev__api.md) {

[ 533](structrtio__iodev__api.md#a6cd795906753535571ec1ecc0e0c430c) void (\*[submit](structrtio__iodev__api.md#a6cd795906753535571ec1ecc0e0c430c))(struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \*iodev\_sqe);

534};

535

[ 539](structrtio__iodev.md)struct [rtio\_iodev](structrtio__iodev.md) {

540 /\* Function pointer table \*/

[ 541](structrtio__iodev.md#a6dfedbfb58356e0647e5c20632656977) const struct [rtio\_iodev\_api](structrtio__iodev__api.md) \*[api](structrtio__iodev.md#a6dfedbfb58356e0647e5c20632656977);

542

543 /\* Data associated with this iodev \*/

[ 544](structrtio__iodev.md#af0f3a27fe8dea2161c9a73cb838bdeec) void \*[data](structrtio__iodev.md#af0f3a27fe8dea2161c9a73cb838bdeec);

545};

546

[ 548](group__rtio.md#gad5f073978f641413989d1c6b405d6c36)#define RTIO\_OP\_NOP 0

549

[ 551](group__rtio.md#gafeb05c351207cd1638fa78f6607e1a4a)#define RTIO\_OP\_RX (RTIO\_OP\_NOP+1)

552

[ 554](group__rtio.md#ga8dcaef0cda159e16520a95543ff62827)#define RTIO\_OP\_TX (RTIO\_OP\_RX+1)

555

[ 557](group__rtio.md#ga6f95c0a5fbcc020a0d1102d3b08934bd)#define RTIO\_OP\_TINY\_TX (RTIO\_OP\_TX+1)

558

[ 560](group__rtio.md#ga18e0ff7d44e4c33900106aefad0a8508)#define RTIO\_OP\_CALLBACK (RTIO\_OP\_TINY\_TX+1)

561

[ 563](group__rtio.md#ga9f0e70f5a28be65a8ed67c0257a72692)#define RTIO\_OP\_TXRX (RTIO\_OP\_CALLBACK+1)

564

[ 566](group__rtio.md#gae8da4da54f32963190f52c7533d4c951)#define RTIO\_OP\_DELAY (RTIO\_OP\_TXRX+1)

567

[ 569](group__rtio.md#ga3b4f9b1ee1612290323161ecc16e0859)#define RTIO\_OP\_I2C\_RECOVER (RTIO\_OP\_DELAY+1)

570

[ 572](group__rtio.md#gad987be3acfe406b11419c7e8cd068cf5)#define RTIO\_OP\_I2C\_CONFIGURE (RTIO\_OP\_I2C\_RECOVER+1)

573

[ 575](group__rtio.md#gac69023c6902570e7511edd044d6d9d94)#define RTIO\_OP\_I3C\_RECOVER (RTIO\_OP\_I2C\_CONFIGURE+1)

576

[ 578](group__rtio.md#gaa77874941380a8215ec57b30d993d437)#define RTIO\_OP\_I3C\_CONFIGURE (RTIO\_OP\_I3C\_RECOVER+1)

579

[ 581](group__rtio.md#ga691ea387929db1224d6343fd91dfd2c5)#define RTIO\_OP\_I3C\_CCC (RTIO\_OP\_I3C\_CONFIGURE+1)

582

[ 584](group__rtio.md#gad74290935595b83040676b426cd07161)#define RTIO\_OP\_AWAIT (RTIO\_OP\_I3C\_CCC+1)

585

[ 589](group__rtio.md#ga599ee43fdf35e1cf895cbbe9272e4c50)static inline void [rtio\_sqe\_prep\_nop](group__rtio.md#ga599ee43fdf35e1cf895cbbe9272e4c50)(struct [rtio\_sqe](structrtio__sqe.md) \*sqe,

590 const struct [rtio\_iodev](structrtio__iodev.md) \*iodev,

591 void \*userdata)

592{

593 [memset](string_8h.md#a4137694174d4ca2fad886a1db355015c)(sqe, 0, sizeof(struct [rtio\_sqe](structrtio__sqe.md)));

594 sqe->[op](structrtio__sqe.md#a1d8d3e3426e47a2c7f54d98f51acd953) = [RTIO\_OP\_NOP](group__rtio.md#gad5f073978f641413989d1c6b405d6c36);

595 sqe->[iodev](structrtio__sqe.md#a6c784702f011592c84feacd57915bbfc) = iodev;

596 sqe->[userdata](structrtio__sqe.md#a0ed519ee0b5867ff73bdaf37f983c971) = userdata;

597}

598

[ 602](group__rtio.md#ga89c7cc2494e3dda50737f78f1a1376cf)static inline void [rtio\_sqe\_prep\_read](group__rtio.md#ga89c7cc2494e3dda50737f78f1a1376cf)(struct [rtio\_sqe](structrtio__sqe.md) \*sqe,

603 const struct [rtio\_iodev](structrtio__iodev.md) \*iodev,

604 [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) prio,

605 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf,

606 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) len,

607 void \*userdata)

608{

609 [memset](string_8h.md#a4137694174d4ca2fad886a1db355015c)(sqe, 0, sizeof(struct [rtio\_sqe](structrtio__sqe.md)));

610 sqe->[op](structrtio__sqe.md#a1d8d3e3426e47a2c7f54d98f51acd953) = [RTIO\_OP\_RX](group__rtio.md#gafeb05c351207cd1638fa78f6607e1a4a);

611 sqe->[prio](structrtio__sqe.md#a528eb9b721be7b8a8898ab16a7e2d9a7) = prio;

612 sqe->[iodev](structrtio__sqe.md#a6c784702f011592c84feacd57915bbfc) = iodev;

613 sqe->[rx](structrtio__sqe.md#a37a98afc43f26355c70e7036725b2544).[buf\_len](structrtio__sqe.md#a67376f40a13960b152a23da250275722) = len;

614 sqe->[rx](structrtio__sqe.md#a37a98afc43f26355c70e7036725b2544).[buf](structrtio__sqe.md#ab71176c084e8b8eb65dfeb3018ae2a49) = buf;

615 sqe->[userdata](structrtio__sqe.md#a0ed519ee0b5867ff73bdaf37f983c971) = userdata;

616}

617

[ 623](group__rtio.md#ga15c1f623658d27d300d1a31a6f3d6b9d)static inline void [rtio\_sqe\_prep\_read\_with\_pool](group__rtio.md#ga15c1f623658d27d300d1a31a6f3d6b9d)(struct [rtio\_sqe](structrtio__sqe.md) \*sqe,

624 const struct [rtio\_iodev](structrtio__iodev.md) \*iodev, [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) prio,

625 void \*userdata)

626{

627 [rtio\_sqe\_prep\_read](group__rtio.md#ga89c7cc2494e3dda50737f78f1a1376cf)(sqe, iodev, prio, [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4), 0, userdata);

628 sqe->[flags](structrtio__sqe.md#aad2ff8524df0e24b812e77e2393bf5b0) = [RTIO\_SQE\_MEMPOOL\_BUFFER](group__rtio__sqe__flags.md#ga2802b46584220afffa0e959e149d5a4d);

629}

630

[ 631](group__rtio.md#ga9803aa829f8c0eeee746ea7d872c20cc)static inline void [rtio\_sqe\_prep\_read\_multishot](group__rtio.md#ga9803aa829f8c0eeee746ea7d872c20cc)(struct [rtio\_sqe](structrtio__sqe.md) \*sqe,

632 const struct [rtio\_iodev](structrtio__iodev.md) \*iodev, [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) prio,

633 void \*userdata)

634{

635 [rtio\_sqe\_prep\_read\_with\_pool](group__rtio.md#ga15c1f623658d27d300d1a31a6f3d6b9d)(sqe, iodev, prio, userdata);

636 sqe->[flags](structrtio__sqe.md#aad2ff8524df0e24b812e77e2393bf5b0) |= [RTIO\_SQE\_MULTISHOT](group__rtio__sqe__flags.md#ga00f8ead8f043fe40d49d0bc3325fb299);

637}

638

[ 642](group__rtio.md#ga7f7856d1f4fd1d8c4f6eebcccfe77701)static inline void [rtio\_sqe\_prep\_write](group__rtio.md#ga7f7856d1f4fd1d8c4f6eebcccfe77701)(struct [rtio\_sqe](structrtio__sqe.md) \*sqe,

643 const struct [rtio\_iodev](structrtio__iodev.md) \*iodev,

644 [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) prio,

645 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf,

646 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) len,

647 void \*userdata)

648{

649 [memset](string_8h.md#a4137694174d4ca2fad886a1db355015c)(sqe, 0, sizeof(struct [rtio\_sqe](structrtio__sqe.md)));

650 sqe->[op](structrtio__sqe.md#a1d8d3e3426e47a2c7f54d98f51acd953) = [RTIO\_OP\_TX](group__rtio.md#ga8dcaef0cda159e16520a95543ff62827);

651 sqe->[prio](structrtio__sqe.md#a528eb9b721be7b8a8898ab16a7e2d9a7) = prio;

652 sqe->[iodev](structrtio__sqe.md#a6c784702f011592c84feacd57915bbfc) = iodev;

653 sqe->[tx](structrtio__sqe.md#a4399cf25c7e761126a6218c2b7e3192d).[buf\_len](structrtio__sqe.md#a67376f40a13960b152a23da250275722) = len;

654 sqe->[tx](structrtio__sqe.md#a4399cf25c7e761126a6218c2b7e3192d).[buf](structrtio__sqe.md#ab71176c084e8b8eb65dfeb3018ae2a49) = buf;

655 sqe->[userdata](structrtio__sqe.md#a0ed519ee0b5867ff73bdaf37f983c971) = userdata;

656}

657

[ 668](group__rtio.md#ga31be14ece09e061a8d42ca8f2395286a)static inline void [rtio\_sqe\_prep\_tiny\_write](group__rtio.md#ga31be14ece09e061a8d42ca8f2395286a)(struct [rtio\_sqe](structrtio__sqe.md) \*sqe,

669 const struct [rtio\_iodev](structrtio__iodev.md) \*iodev,

670 [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) prio,

671 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*tiny\_write\_data,

672 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) tiny\_write\_len,

673 void \*userdata)

674{

675 \_\_ASSERT\_NO\_MSG(tiny\_write\_len <= sizeof(sqe->[tiny\_tx](structrtio__sqe.md#a19ace9c984538c2022e7f8ecaefa075d).[buf](structrtio__sqe.md#ab71176c084e8b8eb65dfeb3018ae2a49)));

676

677 [memset](string_8h.md#a4137694174d4ca2fad886a1db355015c)(sqe, 0, sizeof(struct [rtio\_sqe](structrtio__sqe.md)));

678 sqe->[op](structrtio__sqe.md#a1d8d3e3426e47a2c7f54d98f51acd953) = [RTIO\_OP\_TINY\_TX](group__rtio.md#ga6f95c0a5fbcc020a0d1102d3b08934bd);

679 sqe->[prio](structrtio__sqe.md#a528eb9b721be7b8a8898ab16a7e2d9a7) = prio;

680 sqe->[iodev](structrtio__sqe.md#a6c784702f011592c84feacd57915bbfc) = iodev;

681 sqe->[tiny\_tx](structrtio__sqe.md#a19ace9c984538c2022e7f8ecaefa075d).[buf\_len](structrtio__sqe.md#a67376f40a13960b152a23da250275722) = tiny\_write\_len;

682 [memcpy](string_8h.md#af0f01bffcd16daa9143f6014d10a25ad)(sqe->[tiny\_tx](structrtio__sqe.md#a19ace9c984538c2022e7f8ecaefa075d).[buf](structrtio__sqe.md#ab71176c084e8b8eb65dfeb3018ae2a49), tiny\_write\_data, tiny\_write\_len);

683 sqe->[userdata](structrtio__sqe.md#a0ed519ee0b5867ff73bdaf37f983c971) = userdata;

684}

685

[ 694](group__rtio.md#ga9d0dd7d0e2e3d281092f2350d6e1713e)static inline void [rtio\_sqe\_prep\_callback](group__rtio.md#ga9d0dd7d0e2e3d281092f2350d6e1713e)(struct [rtio\_sqe](structrtio__sqe.md) \*sqe,

695 [rtio\_callback\_t](group__rtio.md#gad1dbd690e6cf88d7c788436dd04d1a00) callback,

696 void \*arg0,

697 void \*userdata)

698{

699 [memset](string_8h.md#a4137694174d4ca2fad886a1db355015c)(sqe, 0, sizeof(struct [rtio\_sqe](structrtio__sqe.md)));

700 sqe->[op](structrtio__sqe.md#a1d8d3e3426e47a2c7f54d98f51acd953) = [RTIO\_OP\_CALLBACK](group__rtio.md#ga18e0ff7d44e4c33900106aefad0a8508);

701 sqe->[prio](structrtio__sqe.md#a528eb9b721be7b8a8898ab16a7e2d9a7) = 0;

702 sqe->[iodev](structrtio__sqe.md#a6c784702f011592c84feacd57915bbfc) = [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4);

703 sqe->[callback](structrtio__sqe.md#af8c31c33e9fedebe55cac73595d0f696).callback = callback;

704 sqe->[callback](structrtio__sqe.md#af8c31c33e9fedebe55cac73595d0f696).arg0 = arg0;

705 sqe->[userdata](structrtio__sqe.md#a0ed519ee0b5867ff73bdaf37f983c971) = userdata;

706}

707

[ 718](group__rtio.md#gae87be354087d038953dae07c7f9cd3b0)static inline void [rtio\_sqe\_prep\_callback\_no\_cqe](group__rtio.md#gae87be354087d038953dae07c7f9cd3b0)(struct [rtio\_sqe](structrtio__sqe.md) \*sqe,

719 [rtio\_callback\_t](group__rtio.md#gad1dbd690e6cf88d7c788436dd04d1a00) callback,

720 void \*arg0,

721 void \*userdata)

722{

723 [rtio\_sqe\_prep\_callback](group__rtio.md#ga9d0dd7d0e2e3d281092f2350d6e1713e)(sqe, callback, arg0, userdata);

724 sqe->[flags](structrtio__sqe.md#aad2ff8524df0e24b812e77e2393bf5b0) |= [RTIO\_SQE\_NO\_RESPONSE](group__rtio__sqe__flags.md#ga8578ffdb8f53a51b94fa86a6f02d4a11);

725}

726

[ 730](group__rtio.md#gab9b605dcbb01d21c88f9ae70588ea3b5)static inline void [rtio\_sqe\_prep\_transceive](group__rtio.md#gab9b605dcbb01d21c88f9ae70588ea3b5)(struct [rtio\_sqe](structrtio__sqe.md) \*sqe,

731 const struct [rtio\_iodev](structrtio__iodev.md) \*iodev,

732 [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) prio,

733 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*tx\_buf,

734 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*rx\_buf,

735 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) buf\_len,

736 void \*userdata)

737{

738 [memset](string_8h.md#a4137694174d4ca2fad886a1db355015c)(sqe, 0, sizeof(struct [rtio\_sqe](structrtio__sqe.md)));

739 sqe->[op](structrtio__sqe.md#a1d8d3e3426e47a2c7f54d98f51acd953) = [RTIO\_OP\_TXRX](group__rtio.md#ga9f0e70f5a28be65a8ed67c0257a72692);

740 sqe->[prio](structrtio__sqe.md#a528eb9b721be7b8a8898ab16a7e2d9a7) = prio;

741 sqe->[iodev](structrtio__sqe.md#a6c784702f011592c84feacd57915bbfc) = iodev;

742 sqe->[txrx](structrtio__sqe.md#a5f2511eb361a7a4d54a92fae4d391e8c).[buf\_len](structrtio__sqe.md#a67376f40a13960b152a23da250275722) = buf\_len;

743 sqe->[txrx](structrtio__sqe.md#a5f2511eb361a7a4d54a92fae4d391e8c).[tx\_buf](structrtio__sqe.md#a18bfa63542954f4bb8b924c92c48e931) = tx\_buf;

744 sqe->[txrx](structrtio__sqe.md#a5f2511eb361a7a4d54a92fae4d391e8c).[rx\_buf](structrtio__sqe.md#a4d2090fc11b897724a883ad1087d9f73) = rx\_buf;

745 sqe->[userdata](structrtio__sqe.md#a0ed519ee0b5867ff73bdaf37f983c971) = userdata;

746}

747

[ 748](group__rtio.md#gafd97c145b8525895494a31a87610f65d)static inline void [rtio\_sqe\_prep\_await](group__rtio.md#gafd97c145b8525895494a31a87610f65d)(struct [rtio\_sqe](structrtio__sqe.md) \*sqe,

749 const struct [rtio\_iodev](structrtio__iodev.md) \*iodev,

750 [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) prio,

751 void \*userdata)

752{

753 [memset](string_8h.md#a4137694174d4ca2fad886a1db355015c)(sqe, 0, sizeof(struct [rtio\_sqe](structrtio__sqe.md)));

754 sqe->[op](structrtio__sqe.md#a1d8d3e3426e47a2c7f54d98f51acd953) = [RTIO\_OP\_AWAIT](group__rtio.md#gad74290935595b83040676b426cd07161);

755 sqe->[prio](structrtio__sqe.md#a528eb9b721be7b8a8898ab16a7e2d9a7) = prio;

756 sqe->[iodev](structrtio__sqe.md#a6c784702f011592c84feacd57915bbfc) = iodev;

757 sqe->[userdata](structrtio__sqe.md#a0ed519ee0b5867ff73bdaf37f983c971) = userdata;

758}

759

[ 760](group__rtio.md#ga2169a7a776a5300b25f599144de4de0b)static inline void [rtio\_sqe\_prep\_delay](group__rtio.md#ga2169a7a776a5300b25f599144de4de0b)(struct [rtio\_sqe](structrtio__sqe.md) \*sqe,

761 [k\_timeout\_t](structk__timeout__t.md) timeout,

762 void \*userdata)

763{

764 [memset](string_8h.md#a4137694174d4ca2fad886a1db355015c)(sqe, 0, sizeof(struct [rtio\_sqe](structrtio__sqe.md)));

765 sqe->[op](structrtio__sqe.md#a1d8d3e3426e47a2c7f54d98f51acd953) = [RTIO\_OP\_DELAY](group__rtio.md#gae8da4da54f32963190f52c7533d4c951);

766 sqe->[prio](structrtio__sqe.md#a528eb9b721be7b8a8898ab16a7e2d9a7) = 0;

767 sqe->[iodev](structrtio__sqe.md#a6c784702f011592c84feacd57915bbfc) = [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4);

768 sqe->[delay](structrtio__sqe.md#a9a93700154d745bc1bacc764bbfbe696).[timeout](structrtio__sqe.md#a544c75ee10281e10e83f51df5b157d62) = timeout;

769 sqe->[userdata](structrtio__sqe.md#a0ed519ee0b5867ff73bdaf37f983c971) = userdata;

770}

771

[ 772](group__rtio.md#gae5fb03fc8f3a4a774f476ff552999bfc)static inline struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \*[rtio\_sqe\_pool\_alloc](group__rtio.md#gae5fb03fc8f3a4a774f476ff552999bfc)(struct [rtio\_sqe\_pool](structrtio__sqe__pool.md) \*pool)

773{

774 struct [mpsc\_node](structmpsc__node.md) \*node = [mpsc\_pop](group__mpsc__lockfree.md#ga823ec37b84ac43e46167aac954bce9d7)(&pool->[free\_q](structrtio__sqe__pool.md#aed49ea25c952e07a8287919268fd2485));

775

776 if (node == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

777 return [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4);

778 }

779

780 struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \*iodev\_sqe = [CONTAINER\_OF](group__sys-util.md#gac5bc561d1bfd1bf68877fe577779bd2f)(node, struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md), [q](structrtio__iodev__sqe.md#a9cfdd004b65a5e2bc111bc2fb333498c));

781

782 pool->[pool\_free](structrtio__sqe__pool.md#af7990b1510ad2343573f3e4e502475b0)--;

783

784 return iodev\_sqe;

785}

786

[ 787](group__rtio.md#gac776aea3692cfd77aa5bf675a9e9ed02)static inline void [rtio\_sqe\_pool\_free](group__rtio.md#gac776aea3692cfd77aa5bf675a9e9ed02)(struct [rtio\_sqe\_pool](structrtio__sqe__pool.md) \*pool, struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \*iodev\_sqe)

788{

789 [mpsc\_push](group__mpsc__lockfree.md#ga403add133841ef88e10d74141e782b37)(&pool->[free\_q](structrtio__sqe__pool.md#aed49ea25c952e07a8287919268fd2485), &iodev\_sqe->[q](structrtio__iodev__sqe.md#a9cfdd004b65a5e2bc111bc2fb333498c));

790

791 pool->[pool\_free](structrtio__sqe__pool.md#af7990b1510ad2343573f3e4e502475b0)++;

792}

793

[ 794](group__rtio.md#ga8497170f55af1d11d717e919f61806f5)static inline struct [rtio\_cqe](structrtio__cqe.md) \*[rtio\_cqe\_pool\_alloc](group__rtio.md#ga8497170f55af1d11d717e919f61806f5)(struct [rtio\_cqe\_pool](structrtio__cqe__pool.md) \*pool)

795{

796 struct [mpsc\_node](structmpsc__node.md) \*node = [mpsc\_pop](group__mpsc__lockfree.md#ga823ec37b84ac43e46167aac954bce9d7)(&pool->[free\_q](structrtio__cqe__pool.md#a13bd7991ff5622c1cb5aa6af014aaab3));

797

798 if (node == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

799 return [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4);

800 }

801

802 struct [rtio\_cqe](structrtio__cqe.md) \*cqe = [CONTAINER\_OF](group__sys-util.md#gac5bc561d1bfd1bf68877fe577779bd2f)(node, struct [rtio\_cqe](structrtio__cqe.md), [q](structrtio__cqe.md#a27272bca31c170f406799633ec82098d));

803

804 [memset](string_8h.md#a4137694174d4ca2fad886a1db355015c)(cqe, 0, sizeof(struct [rtio\_cqe](structrtio__cqe.md)));

805

806 pool->[pool\_free](structrtio__cqe__pool.md#a4fb501a0ba15e2956113deaf4597d846)--;

807

808 return cqe;

809}

810

[ 811](group__rtio.md#ga23c0c5d4b551858eabe057ecb8a28d12)static inline void [rtio\_cqe\_pool\_free](group__rtio.md#ga23c0c5d4b551858eabe057ecb8a28d12)(struct [rtio\_cqe\_pool](structrtio__cqe__pool.md) \*pool, struct [rtio\_cqe](structrtio__cqe.md) \*cqe)

812{

813 [mpsc\_push](group__mpsc__lockfree.md#ga403add133841ef88e10d74141e782b37)(&pool->[free\_q](structrtio__cqe__pool.md#a13bd7991ff5622c1cb5aa6af014aaab3), &cqe->[q](structrtio__cqe.md#a27272bca31c170f406799633ec82098d));

814

815 pool->[pool\_free](structrtio__cqe__pool.md#a4fb501a0ba15e2956113deaf4597d846)++;

816}

817

[ 818](group__rtio.md#ga7f14b99fc1dd0697309e7f71a270f5fb)static inline int [rtio\_block\_pool\_alloc](group__rtio.md#ga7f14b99fc1dd0697309e7f71a270f5fb)(struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2), size\_t min\_sz,

819 size\_t max\_sz, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\*buf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*buf\_len)

820{

821#ifndef CONFIG\_RTIO\_SYS\_MEM\_BLOCKS

822 ARG\_UNUSED([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2));

823 ARG\_UNUSED(min\_sz);

824 ARG\_UNUSED(max\_sz);

825 ARG\_UNUSED(buf);

826 ARG\_UNUSED(buf\_len);

827 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

828#else

829 const [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size = [rtio\_mempool\_block\_size](group__rtio.md#ga4213be028b0a1264daaa0d30c4c2d089)([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2));

830 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) bytes = max\_sz;

831

832 /\* Not every context has a block pool and the block size may return 0 in

833 \* that case

834 \*/

835 if (block\_size == 0) {

836 return -[ENOMEM](group__system__errno.md#ga6a05c923dad0c1208043e9c20a58c8e5);

837 }

838

839 do {

840 size\_t num\_blks = [DIV\_ROUND\_UP](group__sys-util.md#gae664e7492e37d324831caf2321ddda37)(bytes, block\_size);

841 int rc = [sys\_mem\_blocks\_alloc\_contiguous](group__mem__blocks__apis.md#ga72614d0c120f40209837b77d0333bb23)([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->block\_pool, num\_blks, (void \*\*)buf);

842

843 if (rc == 0) {

844 \*buf\_len = num\_blks \* block\_size;

845 return 0;

846 }

847

848 if (bytes <= block\_size) {

849 break;

850 }

851

852 bytes -= block\_size;

853 } while (bytes >= min\_sz);

854

855 return -[ENOMEM](group__system__errno.md#ga6a05c923dad0c1208043e9c20a58c8e5);

856#endif

857}

858

[ 859](group__rtio.md#gafca7732926a9a7c080e3cb16e5f16108)static inline void [rtio\_block\_pool\_free](group__rtio.md#gafca7732926a9a7c080e3cb16e5f16108)(struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2), void \*buf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) buf\_len)

860{

861#ifndef CONFIG\_RTIO\_SYS\_MEM\_BLOCKS

862 ARG\_UNUSED([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2));

863 ARG\_UNUSED(buf);

864 ARG\_UNUSED(buf\_len);

865#else

866 size\_t num\_blks = buf\_len >> [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->block\_pool->info.blk\_sz\_shift;

867

868 [sys\_mem\_blocks\_free\_contiguous](group__mem__blocks__apis.md#ga39e7f8dfe3bda8eabc2372f9a1e87342)([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->block\_pool, buf, num\_blks);

869#endif

870}

871

872/\* Do not try and reformat the macros \*/

873/\* clang-format off \*/

874

[ 882](group__rtio.md#gaae51e2a679d37bc1cfba79961688c406)#define RTIO\_IODEV\_DEFINE(name, iodev\_api, iodev\_data) \

883 STRUCT\_SECTION\_ITERABLE(rtio\_iodev, name) = { \

884 .api = (iodev\_api), \

885 .data = (iodev\_data), \

886 }

887

888#define Z\_RTIO\_SQE\_POOL\_DEFINE(name, sz) \

889 static struct rtio\_iodev\_sqe CONCAT(\_sqe\_pool\_, name)[sz]; \

890 STRUCT\_SECTION\_ITERABLE(rtio\_sqe\_pool, name) = { \

891 .free\_q = MPSC\_INIT((name.free\_q)), \

892 .pool\_size = sz, \

893 .pool\_free = sz, \

894 .pool = CONCAT(\_sqe\_pool\_, name), \

895 }

896

897

898#define Z\_RTIO\_CQE\_POOL\_DEFINE(name, sz) \

899 static struct rtio\_cqe CONCAT(\_cqe\_pool\_, name)[sz]; \

900 STRUCT\_SECTION\_ITERABLE(rtio\_cqe\_pool, name) = { \

901 .free\_q = MPSC\_INIT((name.free\_q)), \

902 .pool\_size = sz, \

903 .pool\_free = sz, \

904 .pool = CONCAT(\_cqe\_pool\_, name), \

905 }

906

[ 916](group__rtio.md#ga2437af5061e078950d4a55211d9a902f)#define RTIO\_BMEM COND\_CODE\_1(CONFIG\_USERSPACE, (K\_APP\_BMEM(rtio\_partition) static), (static))

917

[ 927](group__rtio.md#ga3b569c01b71e126cff852df50e98fd69)#define RTIO\_DMEM COND\_CODE\_1(CONFIG\_USERSPACE, (K\_APP\_DMEM(rtio\_partition) static), (static))

928

929#define Z\_RTIO\_BLOCK\_POOL\_DEFINE(name, blk\_sz, blk\_cnt, blk\_align) \

930 RTIO\_BMEM uint8\_t \_\_aligned(WB\_UP(blk\_align)) \

931 CONCAT(\_block\_pool\_, name)[blk\_cnt\*WB\_UP(blk\_sz)]; \

932 \_SYS\_MEM\_BLOCKS\_DEFINE\_WITH\_EXT\_BUF(name, WB\_UP(blk\_sz), blk\_cnt, \

933 CONCAT(\_block\_pool\_, name), RTIO\_DMEM)

934

935#define Z\_RTIO\_DEFINE(name, \_sqe\_pool, \_cqe\_pool, \_block\_pool) \

936 IF\_ENABLED(CONFIG\_RTIO\_SUBMIT\_SEM, \

937 (static K\_SEM\_DEFINE(CONCAT(\_submit\_sem\_, name), 0, K\_SEM\_MAX\_LIMIT))) \

938 IF\_ENABLED(CONFIG\_RTIO\_CONSUME\_SEM, \

939 (static K\_SEM\_DEFINE(CONCAT(\_consume\_sem\_, name), 0, K\_SEM\_MAX\_LIMIT))) \

940 STRUCT\_SECTION\_ITERABLE(rtio, name) = { \

941 IF\_ENABLED(CONFIG\_RTIO\_SUBMIT\_SEM, (.submit\_sem = &CONCAT(\_submit\_sem\_, name),)) \

942 IF\_ENABLED(CONFIG\_RTIO\_SUBMIT\_SEM, (.submit\_count = 0,)) \

943 IF\_ENABLED(CONFIG\_RTIO\_CONSUME\_SEM, (.consume\_sem = &CONCAT(\_consume\_sem\_, name),))\

944 .cq\_count = ATOMIC\_INIT(0), \

945 .xcqcnt = ATOMIC\_INIT(0), \

946 .sqe\_pool = \_sqe\_pool, \

947 .cqe\_pool = \_cqe\_pool, \

948 IF\_ENABLED(CONFIG\_RTIO\_SYS\_MEM\_BLOCKS, (.block\_pool = \_block\_pool,)) \

949 .sq = MPSC\_INIT((name.sq)), \

950 .cq = MPSC\_INIT((name.cq)), \

951 }

952

[ 960](group__rtio.md#ga338df088eabf3b8f7fefb4ac517b21d4)#define RTIO\_DEFINE(name, sq\_sz, cq\_sz) \

961 Z\_RTIO\_SQE\_POOL\_DEFINE(CONCAT(name, \_sqe\_pool), sq\_sz); \

962 Z\_RTIO\_CQE\_POOL\_DEFINE(CONCAT(name, \_cqe\_pool), cq\_sz); \

963 Z\_RTIO\_DEFINE(name, &CONCAT(name, \_sqe\_pool), \

964 &CONCAT(name, \_cqe\_pool), NULL)

965

966/\* clang-format on \*/

967

[ 978](group__rtio.md#gae4c2a9384a9ae4ed16dff914b1184ca8)#define RTIO\_DEFINE\_WITH\_MEMPOOL(name, sq\_sz, cq\_sz, num\_blks, blk\_size, balign) \

979 Z\_RTIO\_SQE\_POOL\_DEFINE(name##\_sqe\_pool, sq\_sz); \

980 Z\_RTIO\_CQE\_POOL\_DEFINE(name##\_cqe\_pool, cq\_sz); \

981 Z\_RTIO\_BLOCK\_POOL\_DEFINE(name##\_block\_pool, blk\_size, num\_blks, balign); \

982 Z\_RTIO\_DEFINE(name, &name##\_sqe\_pool, &name##\_cqe\_pool, &name##\_block\_pool)

983

984/\* clang-format on \*/

985

[ 993](group__rtio.md#ga1f4fb7bccbaae08a94387e4b11275a78)static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [rtio\_sqe\_acquirable](group__rtio.md#ga1f4fb7bccbaae08a94387e4b11275a78)(struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2))

994{

995 return [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->sqe\_pool->pool\_free;

996}

997

[ 1006](group__rtio.md#gaef904eb6a8810d8c3ea537c4d6edbee5)static inline struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \*[rtio\_txn\_next](group__rtio.md#gaef904eb6a8810d8c3ea537c4d6edbee5)(const struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \*iodev\_sqe)

1007{

1008 if (iodev\_sqe->[sqe](structrtio__iodev__sqe.md#a2bd98599678909c0ddb22f879affa12b).[flags](structrtio__sqe.md#aad2ff8524df0e24b812e77e2393bf5b0) & [RTIO\_SQE\_TRANSACTION](group__rtio__sqe__flags.md#ga07f09cc0c95be6cfdddb23f8acacb1ea)) {

1009 return iodev\_sqe->[next](structrtio__iodev__sqe.md#a2afb82e550e614f87db7cd1bf2c3a352);

1010 } else {

1011 return [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4);

1012 }

1013}

1014

1015

[ 1024](group__rtio.md#gada1e3abf92a46e376138435debc8baf4)static inline struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \*[rtio\_chain\_next](group__rtio.md#gada1e3abf92a46e376138435debc8baf4)(const struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \*iodev\_sqe)

1025{

1026 if (iodev\_sqe->[sqe](structrtio__iodev__sqe.md#a2bd98599678909c0ddb22f879affa12b).[flags](structrtio__sqe.md#aad2ff8524df0e24b812e77e2393bf5b0) & [RTIO\_SQE\_CHAINED](group__rtio__sqe__flags.md#gae9191d521d4ab602b53fefb74020d06b)) {

1027 return iodev\_sqe->[next](structrtio__iodev__sqe.md#a2afb82e550e614f87db7cd1bf2c3a352);

1028 } else {

1029 return [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4);

1030 }

1031}

1032

[ 1041](group__rtio.md#gae690e3dc0fc40dda57257b2eed432719)static inline struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \*[rtio\_iodev\_sqe\_next](group__rtio.md#gae690e3dc0fc40dda57257b2eed432719)(const struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \*iodev\_sqe)

1042{

1043 return iodev\_sqe->[next](structrtio__iodev__sqe.md#a2afb82e550e614f87db7cd1bf2c3a352);

1044}

1045

[ 1054](group__rtio.md#ga8b47c954d15a334621def53acceb6799)static inline struct [rtio\_sqe](structrtio__sqe.md) \*[rtio\_sqe\_acquire](group__rtio.md#ga8b47c954d15a334621def53acceb6799)(struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2))

1055{

1056 struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \*iodev\_sqe = [rtio\_sqe\_pool\_alloc](group__rtio.md#gae5fb03fc8f3a4a774f476ff552999bfc)([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->sqe\_pool);

1057

1058 if (iodev\_sqe == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

1059 return [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4);

1060 }

1061

1062 [mpsc\_push](group__mpsc__lockfree.md#ga403add133841ef88e10d74141e782b37)(&[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->sq, &iodev\_sqe->[q](structrtio__iodev__sqe.md#a9cfdd004b65a5e2bc111bc2fb333498c));

1063

1064 return &iodev\_sqe->[sqe](structrtio__iodev__sqe.md#a2bd98599678909c0ddb22f879affa12b);

1065}

1066

[ 1072](group__rtio.md#ga9486fb7b50e8d2409a50da235203536b)static inline void [rtio\_sqe\_drop\_all](group__rtio.md#ga9486fb7b50e8d2409a50da235203536b)(struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2))

1073{

1074 struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \*iodev\_sqe;

1075 struct [mpsc\_node](structmpsc__node.md) \*node = [mpsc\_pop](group__mpsc__lockfree.md#ga823ec37b84ac43e46167aac954bce9d7)(&[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->sq);

1076

1077 while (node != [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

1078 iodev\_sqe = [CONTAINER\_OF](group__sys-util.md#gac5bc561d1bfd1bf68877fe577779bd2f)(node, struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md), q);

1079 [rtio\_sqe\_pool\_free](group__rtio.md#gac776aea3692cfd77aa5bf675a9e9ed02)([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->sqe\_pool, iodev\_sqe);

1080 node = [mpsc\_pop](group__mpsc__lockfree.md#ga823ec37b84ac43e46167aac954bce9d7)(&[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->sq);

1081 }

1082}

1083

[ 1087](group__rtio.md#gad848646651fdf3649b882e5268f72a3c)static inline struct [rtio\_cqe](structrtio__cqe.md) \*[rtio\_cqe\_acquire](group__rtio.md#gad848646651fdf3649b882e5268f72a3c)(struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2))

1088{

1089 struct [rtio\_cqe](structrtio__cqe.md) \*cqe = [rtio\_cqe\_pool\_alloc](group__rtio.md#ga8497170f55af1d11d717e919f61806f5)([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->cqe\_pool);

1090

1091 if (cqe == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

1092 return [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4);

1093 }

1094

1095 [memset](string_8h.md#a4137694174d4ca2fad886a1db355015c)(cqe, 0, sizeof(struct [rtio\_cqe](structrtio__cqe.md)));

1096

1097 return cqe;

1098}

1099

[ 1103](group__rtio.md#ga6f55202adeca60aed0343a7a0dcab071)static inline void [rtio\_cqe\_produce](group__rtio.md#ga6f55202adeca60aed0343a7a0dcab071)(struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2), struct [rtio\_cqe](structrtio__cqe.md) \*cqe)

1104{

1105 [mpsc\_push](group__mpsc__lockfree.md#ga403add133841ef88e10d74141e782b37)(&[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->cq, &cqe->[q](structrtio__cqe.md#a27272bca31c170f406799633ec82098d));

1106}

1107

[ 1119](group__rtio.md#gae562cf241911804cdb9f4e3a73b53df4)static inline struct [rtio\_cqe](structrtio__cqe.md) \*[rtio\_cqe\_consume](group__rtio.md#gae562cf241911804cdb9f4e3a73b53df4)(struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2))

1120{

1121 struct [mpsc\_node](structmpsc__node.md) \*node;

1122 struct [rtio\_cqe](structrtio__cqe.md) \*cqe = [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4);

1123

1124#ifdef CONFIG\_RTIO\_CONSUME\_SEM

1125 if ([k\_sem\_take](group__semaphore__apis.md#gac71e2383c1920dddc45a561cacfef090)([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->consume\_sem, [K\_NO\_WAIT](group__clock__apis.md#ga3d9541cfe2e8395af66d186efa77362f)) != 0) {

1126 return [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4);

1127 }

1128#endif

1129

1130 node = [mpsc\_pop](group__mpsc__lockfree.md#ga823ec37b84ac43e46167aac954bce9d7)(&[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->cq);

1131 if (node == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

1132 return [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4);

1133 }

1134 cqe = [CONTAINER\_OF](group__sys-util.md#gac5bc561d1bfd1bf68877fe577779bd2f)(node, struct [rtio\_cqe](structrtio__cqe.md), [q](structrtio__cqe.md#a27272bca31c170f406799633ec82098d));

1135

1136 return cqe;

1137}

1138

[ 1149](group__rtio.md#gaf617d05d9b59ce1f1d0697617ef6f249)static inline struct [rtio\_cqe](structrtio__cqe.md) \*[rtio\_cqe\_consume\_block](group__rtio.md#gaf617d05d9b59ce1f1d0697617ef6f249)(struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2))

1150{

1151 struct [mpsc\_node](structmpsc__node.md) \*node;

1152 struct [rtio\_cqe](structrtio__cqe.md) \*cqe;

1153

1154#ifdef CONFIG\_RTIO\_CONSUME\_SEM

1155 [k\_sem\_take](group__semaphore__apis.md#gac71e2383c1920dddc45a561cacfef090)([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->consume\_sem, [K\_FOREVER](group__clock__apis.md#ga0bb4b83f0222193b21a8910311bab0ca));

1156#endif

1157 node = [mpsc\_pop](group__mpsc__lockfree.md#ga823ec37b84ac43e46167aac954bce9d7)(&[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->cq);

1158 while (node == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

1159 Z\_SPIN\_DELAY(1);

1160 node = [mpsc\_pop](group__mpsc__lockfree.md#ga823ec37b84ac43e46167aac954bce9d7)(&[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->cq);

1161 }

1162 cqe = [CONTAINER\_OF](group__sys-util.md#gac5bc561d1bfd1bf68877fe577779bd2f)(node, struct [rtio\_cqe](structrtio__cqe.md), [q](structrtio__cqe.md#a27272bca31c170f406799633ec82098d));

1163

1164 return cqe;

1165}

1166

[ 1173](group__rtio.md#gaa0799a5f8ad98425d385a07c5d27d9cb)static inline void [rtio\_cqe\_release](group__rtio.md#gaa0799a5f8ad98425d385a07c5d27d9cb)(struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2), struct [rtio\_cqe](structrtio__cqe.md) \*cqe)

1174{

1175 [rtio\_cqe\_pool\_free](group__rtio.md#ga23c0c5d4b551858eabe057ecb8a28d12)([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->cqe\_pool, cqe);

1176}

1177

[ 1184](group__rtio.md#ga75661c8c6c94a0ac6254cec674b478c8)static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [rtio\_cqe\_compute\_flags](group__rtio.md#ga75661c8c6c94a0ac6254cec674b478c8)(struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \*iodev\_sqe)

1185{

1186 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) = 0;

1187

1188#ifdef CONFIG\_RTIO\_SYS\_MEM\_BLOCKS

1189 if (iodev\_sqe->[sqe](structrtio__iodev__sqe.md#a2bd98599678909c0ddb22f879affa12b).[op](structrtio__sqe.md#a1d8d3e3426e47a2c7f54d98f51acd953) == [RTIO\_OP\_RX](group__rtio.md#gafeb05c351207cd1638fa78f6607e1a4a) && iodev\_sqe->[sqe](structrtio__iodev__sqe.md#a2bd98599678909c0ddb22f879affa12b).[flags](structrtio__sqe.md#aad2ff8524df0e24b812e77e2393bf5b0) & [RTIO\_SQE\_MEMPOOL\_BUFFER](group__rtio__sqe__flags.md#ga2802b46584220afffa0e959e149d5a4d)) {

1190 struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) = iodev\_sqe->[r](structrtio__iodev__sqe.md#a3c3a050793589258eab5ff5ac30f24c8);

1191 struct sys\_mem\_blocks \*mem\_pool = [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->block\_pool;

1192 unsigned int blk\_index = 0;

1193 unsigned int blk\_count = 0;

1194

1195 if (iodev\_sqe->[sqe](structrtio__iodev__sqe.md#a2bd98599678909c0ddb22f879affa12b).[rx](structrtio__sqe.md#a37a98afc43f26355c70e7036725b2544).[buf](structrtio__sqe.md#ab71176c084e8b8eb65dfeb3018ae2a49)) {

1196 blk\_index = (iodev\_sqe->[sqe](structrtio__iodev__sqe.md#a2bd98599678909c0ddb22f879affa12b).[rx](structrtio__sqe.md#a37a98afc43f26355c70e7036725b2544).[buf](structrtio__sqe.md#ab71176c084e8b8eb65dfeb3018ae2a49) - mem\_pool->buffer) >>

1197 mem\_pool->info.blk\_sz\_shift;

1198 blk\_count = iodev\_sqe->[sqe](structrtio__iodev__sqe.md#a2bd98599678909c0ddb22f879affa12b).[rx](structrtio__sqe.md#a37a98afc43f26355c70e7036725b2544).[buf\_len](structrtio__sqe.md#a67376f40a13960b152a23da250275722) >> mem\_pool->info.blk\_sz\_shift;

1199 }

1200 [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) = [RTIO\_CQE\_FLAG\_PREP\_MEMPOOL](group__rtio__cqe__flags.md#ga28b3a5661248b6b3763aab47417114d6)(blk\_index, blk\_count);

1201 }

1202#else

1203 ARG\_UNUSED(iodev\_sqe);

1204#endif

1205

1206 return [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9);

1207}

1208

[ 1224](group__rtio.md#gaedbf9386a36ed99baa290ef6c318ded1)\_\_syscall int [rtio\_cqe\_get\_mempool\_buffer](group__rtio.md#gaedbf9386a36ed99baa290ef6c318ded1)(const struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2), struct [rtio\_cqe](structrtio__cqe.md) \*cqe,

1225 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\*buff, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*buff\_len);

1226

1227static inline int z\_impl\_rtio\_cqe\_get\_mempool\_buffer(const struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2), struct [rtio\_cqe](structrtio__cqe.md) \*cqe,

1228 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\*buff, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*buff\_len)

1229{

1230#ifdef CONFIG\_RTIO\_SYS\_MEM\_BLOCKS

1231 if ([RTIO\_CQE\_FLAG\_GET](group__rtio__cqe__flags.md#gaef64ea020a20ac22a0edcb6eca032efc)(cqe->[flags](structrtio__cqe.md#a8a7632ef1cfd31529d782bd761908d93)) == [RTIO\_CQE\_FLAG\_MEMPOOL\_BUFFER](group__rtio__cqe__flags.md#ga0f212500447a5e37e225a6997953b609)) {

1232 unsigned int blk\_idx = [RTIO\_CQE\_FLAG\_MEMPOOL\_GET\_BLK\_IDX](group__rtio__cqe__flags.md#ga0b5f3f7e7be472ecf87bd2b08c1888da)(cqe->[flags](structrtio__cqe.md#a8a7632ef1cfd31529d782bd761908d93));

1233 unsigned int blk\_count = [RTIO\_CQE\_FLAG\_MEMPOOL\_GET\_BLK\_CNT](group__rtio__cqe__flags.md#ga087465f866d417d5332602bb582cc1a7)(cqe->[flags](structrtio__cqe.md#a8a7632ef1cfd31529d782bd761908d93));

1234 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) blk\_size = [rtio\_mempool\_block\_size](group__rtio.md#ga4213be028b0a1264daaa0d30c4c2d089)([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2));

1235

1236 \*buff\_len = blk\_count \* blk\_size;

1237

1238 if (blk\_count > 0) {

1239 \*buff = [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->block\_pool->buffer + blk\_idx \* blk\_size;

1240

1241 \_\_ASSERT\_NO\_MSG(\*buff >= [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->block\_pool->buffer);

1242 \_\_ASSERT\_NO\_MSG(\*buff <

1243 [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->block\_pool->buffer + blk\_size \* [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->block\_pool->info.num\_blocks);

1244 } else {

1245 \*buff = [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4);

1246 }

1247 return 0;

1248 }

1249 return -[EINVAL](group__system__errno.md#ga2d1678d5a7cc8ce499643f3b8957def4);

1250#else

1251 ARG\_UNUSED([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2));

1252 ARG\_UNUSED(cqe);

1253 ARG\_UNUSED(buff);

1254 ARG\_UNUSED(buff\_len);

1255

1256 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

1257#endif

1258}

1259

[ 1260](group__rtio.md#gaf191153e83de72ddefb998daad02fa16)void [rtio\_executor\_submit](group__rtio.md#gaf191153e83de72ddefb998daad02fa16)(struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2));

[ 1261](group__rtio.md#ga7e2ebd9abaf585207bc5b99c5d815c6a)void [rtio\_executor\_ok](group__rtio.md#ga7e2ebd9abaf585207bc5b99c5d815c6a)(struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \*iodev\_sqe, int result);

[ 1262](group__rtio.md#ga15f4a1a4dfb869ef9e4216dc1c1cdc8a)void [rtio\_executor\_err](group__rtio.md#ga15f4a1a4dfb869ef9e4216dc1c1cdc8a)(struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \*iodev\_sqe, int result);

1263

[ 1272](group__rtio.md#gacb1d2ffa2b07418d8a8aa319bd4336ab)static inline void [rtio\_iodev\_sqe\_ok](group__rtio.md#gacb1d2ffa2b07418d8a8aa319bd4336ab)(struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \*iodev\_sqe, int result)

1273{

1274 [rtio\_executor\_ok](group__rtio.md#ga7e2ebd9abaf585207bc5b99c5d815c6a)(iodev\_sqe, result);

1275}

1276

[ 1285](group__rtio.md#gaada07aa6acefa548743b525225fa482f)static inline void [rtio\_iodev\_sqe\_err](group__rtio.md#gaada07aa6acefa548743b525225fa482f)(struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \*iodev\_sqe, int result)

1286{

1287 [rtio\_executor\_err](group__rtio.md#ga15f4a1a4dfb869ef9e4216dc1c1cdc8a)(iodev\_sqe, result);

1288}

1289

[ 1301](group__rtio.md#ga4abc221d5a90ab882000a72caa0ebd0f)static inline void [rtio\_cqe\_submit](group__rtio.md#ga4abc221d5a90ab882000a72caa0ebd0f)(struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2), int result, void \*userdata, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9))

1302{

1303 struct [rtio\_cqe](structrtio__cqe.md) \*cqe = [rtio\_cqe\_acquire](group__rtio.md#gad848646651fdf3649b882e5268f72a3c)([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2));

1304

1305 if (cqe == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

1306 [atomic\_inc](group__atomic__apis.md#gaae47a9cbe5a6534967b417f602b37ac2)(&[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->xcqcnt);

1307 } else {

1308 cqe->[result](structrtio__cqe.md#acbe2e6607a752b676d9336b9ca6ce435) = [result](structrtio__cqe.md#acbe2e6607a752b676d9336b9ca6ce435);

1309 cqe->[userdata](structrtio__cqe.md#a15128387ccbea55812ef229eab7241e7) = [userdata](structrtio__cqe.md#a15128387ccbea55812ef229eab7241e7);

1310 cqe->[flags](structrtio__cqe.md#a8a7632ef1cfd31529d782bd761908d93) = [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9);

1311 [rtio\_cqe\_produce](group__rtio.md#ga6f55202adeca60aed0343a7a0dcab071)([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2), cqe);

1312 }

1313

1314 /\* atomic\_t isn't guaranteed to wrap correctly as it could be signed, so

1315 \* we must resort to a cas loop.

1316 \*/

1317 [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) val, new\_val;

1318

1319 do {

1320 val = [atomic\_get](group__atomic__apis.md#ga33bb426a17535bd1022895a7e44b32fa)(&[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->cq\_count);

1321 new\_val = ([atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8))(([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808))val + 1);

1322 } while (![atomic\_cas](group__atomic__apis.md#gab879da5aa1ffcc317adc664c016586f7)(&[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->cq\_count, val, new\_val));

1323

1324#ifdef CONFIG\_RTIO\_SUBMIT\_SEM

1325 if ([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->submit\_count > 0) {

1326 [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->submit\_count--;

1327 if ([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->submit\_count == 0) {

1328 [k\_sem\_give](group__semaphore__apis.md#gab9be3cf1988af2cd6afdace52d497c84)([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->submit\_sem);

1329 }

1330 }

1331#endif

1332#ifdef CONFIG\_RTIO\_CONSUME\_SEM

1333 [k\_sem\_give](group__semaphore__apis.md#gab9be3cf1988af2cd6afdace52d497c84)([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->consume\_sem);

1334#endif

1335}

1336

1337#define \_\_RTIO\_MEMPOOL\_GET\_NUM\_BLKS(num\_bytes, blk\_size) (((num\_bytes) + (blk\_size)-1) / (blk\_size))

1338

[ 1351](group__rtio.md#gaab6843e2038d00a8354f57d7e2ffcf7e)static inline int [rtio\_sqe\_rx\_buf](group__rtio.md#gaab6843e2038d00a8354f57d7e2ffcf7e)(const struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \*iodev\_sqe, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) min\_buf\_len,

1352 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) max\_buf\_len, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\*buf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*buf\_len)

1353{

1354 struct [rtio\_sqe](structrtio__sqe.md) \*sqe = (struct [rtio\_sqe](structrtio__sqe.md) \*)&iodev\_sqe->[sqe](structrtio__iodev__sqe.md#a2bd98599678909c0ddb22f879affa12b);

1355

1356#ifdef CONFIG\_RTIO\_SYS\_MEM\_BLOCKS

1357 if (sqe->[op](structrtio__sqe.md#a1d8d3e3426e47a2c7f54d98f51acd953) == [RTIO\_OP\_RX](group__rtio.md#gafeb05c351207cd1638fa78f6607e1a4a) && sqe->[flags](structrtio__sqe.md#aad2ff8524df0e24b812e77e2393bf5b0) & [RTIO\_SQE\_MEMPOOL\_BUFFER](group__rtio__sqe__flags.md#ga2802b46584220afffa0e959e149d5a4d)) {

1358 struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) = iodev\_sqe->[r](structrtio__iodev__sqe.md#a3c3a050793589258eab5ff5ac30f24c8);

1359

1360 if (sqe->[rx](structrtio__sqe.md#a37a98afc43f26355c70e7036725b2544).[buf](structrtio__sqe.md#ab71176c084e8b8eb65dfeb3018ae2a49) != [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

1361 if (sqe->[rx](structrtio__sqe.md#a37a98afc43f26355c70e7036725b2544).[buf\_len](structrtio__sqe.md#a67376f40a13960b152a23da250275722) < min\_buf\_len) {

1362 return -[ENOMEM](group__system__errno.md#ga6a05c923dad0c1208043e9c20a58c8e5);

1363 }

1364 \*buf = sqe->[rx](structrtio__sqe.md#a37a98afc43f26355c70e7036725b2544).[buf](structrtio__sqe.md#ab71176c084e8b8eb65dfeb3018ae2a49);

1365 \*buf\_len = sqe->[rx](structrtio__sqe.md#a37a98afc43f26355c70e7036725b2544).[buf\_len](structrtio__sqe.md#a67376f40a13960b152a23da250275722);

1366 return 0;

1367 }

1368

1369 int rc = [rtio\_block\_pool\_alloc](group__rtio.md#ga7f14b99fc1dd0697309e7f71a270f5fb)([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2), min\_buf\_len, max\_buf\_len, buf, buf\_len);

1370 if (rc == 0) {

1371 sqe->[rx](structrtio__sqe.md#a37a98afc43f26355c70e7036725b2544).[buf](structrtio__sqe.md#ab71176c084e8b8eb65dfeb3018ae2a49) = \*buf;

1372 sqe->[rx](structrtio__sqe.md#a37a98afc43f26355c70e7036725b2544).[buf\_len](structrtio__sqe.md#a67376f40a13960b152a23da250275722) = \*buf\_len;

1373 return 0;

1374 }

1375

1376 return -[ENOMEM](group__system__errno.md#ga6a05c923dad0c1208043e9c20a58c8e5);

1377 }

1378#else

1379 ARG\_UNUSED(max\_buf\_len);

1380#endif

1381

1382 if (sqe->[rx](structrtio__sqe.md#a37a98afc43f26355c70e7036725b2544).[buf\_len](structrtio__sqe.md#a67376f40a13960b152a23da250275722) < min\_buf\_len) {

1383 return -[ENOMEM](group__system__errno.md#ga6a05c923dad0c1208043e9c20a58c8e5);

1384 }

1385

1386 \*buf = sqe->[rx](structrtio__sqe.md#a37a98afc43f26355c70e7036725b2544).[buf](structrtio__sqe.md#ab71176c084e8b8eb65dfeb3018ae2a49);

1387 \*buf\_len = sqe->[rx](structrtio__sqe.md#a37a98afc43f26355c70e7036725b2544).[buf\_len](structrtio__sqe.md#a67376f40a13960b152a23da250275722);

1388 return 0;

1389}

1390

[ 1405](group__rtio.md#ga6530bf56ccbab046a362a6448f941609)\_\_syscall void [rtio\_release\_buffer](group__rtio.md#ga6530bf56ccbab046a362a6448f941609)(struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2), void \*buff, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) buff\_len);

1406

1407static inline void z\_impl\_rtio\_release\_buffer(struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2), void \*buff, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) buff\_len)

1408{

1409#ifdef CONFIG\_RTIO\_SYS\_MEM\_BLOCKS

1410 if ([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4) || buff == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4) || [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->block\_pool == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4) || buff\_len == 0) {

1411 return;

1412 }

1413

1414 [rtio\_block\_pool\_free](group__rtio.md#gafca7732926a9a7c080e3cb16e5f16108)([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2), buff, buff\_len);

1415#else

1416 ARG\_UNUSED([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2));

1417 ARG\_UNUSED(buff);

1418 ARG\_UNUSED(buff\_len);

1419#endif

1420}

1421

[ 1425](group__rtio.md#ga9da42c98546930575525f0f92710f9e4)static inline void [rtio\_access\_grant](group__rtio.md#ga9da42c98546930575525f0f92710f9e4)(struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2), struct [k\_thread](structk__thread.md) \*t)

1426{

1427 [k\_object\_access\_grant](group__usermode__apis.md#ga94087bedf96fe2a2bea437d3d585ca22)([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2), t);

1428

1429#ifdef CONFIG\_RTIO\_SUBMIT\_SEM

1430 [k\_object\_access\_grant](group__usermode__apis.md#ga94087bedf96fe2a2bea437d3d585ca22)([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->submit\_sem, t);

1431#endif

1432

1433#ifdef CONFIG\_RTIO\_CONSUME\_SEM

1434 [k\_object\_access\_grant](group__usermode__apis.md#ga94087bedf96fe2a2bea437d3d585ca22)([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->consume\_sem, t);

1435#endif

1436}

1437

[ 1448](group__rtio.md#gac01252e55d2848b38c0ed77b71d600a7)\_\_syscall int [rtio\_sqe\_cancel](group__rtio.md#gac01252e55d2848b38c0ed77b71d600a7)(struct [rtio\_sqe](structrtio__sqe.md) \*sqe);

1449

1450static inline int z\_impl\_rtio\_sqe\_cancel(struct [rtio\_sqe](structrtio__sqe.md) \*sqe)

1451{

1452 struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \*iodev\_sqe = [CONTAINER\_OF](group__sys-util.md#gac5bc561d1bfd1bf68877fe577779bd2f)([sqe](structrtio__iodev__sqe.md#a2bd98599678909c0ddb22f879affa12b), struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md), [sqe](structrtio__iodev__sqe.md#a2bd98599678909c0ddb22f879affa12b));

1453

1454 do {

1455 iodev\_sqe->[sqe](structrtio__iodev__sqe.md#a2bd98599678909c0ddb22f879affa12b).[flags](structrtio__sqe.md#aad2ff8524df0e24b812e77e2393bf5b0) |= [RTIO\_SQE\_CANCELED](group__rtio__sqe__flags.md#ga7f7f9b038ab8409f271b1aebc1b95ee6);

1456 iodev\_sqe = [rtio\_iodev\_sqe\_next](group__rtio.md#gae690e3dc0fc40dda57257b2eed432719)(iodev\_sqe);

1457 } while (iodev\_sqe != [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4));

1458

1459 return 0;

1460}

1461

[ 1473](group__rtio.md#gae63ffc626a3e99406d36aa47f10b49e1)\_\_syscall void [rtio\_sqe\_signal](group__rtio.md#gae63ffc626a3e99406d36aa47f10b49e1)(struct [rtio\_sqe](structrtio__sqe.md) \*[sqe](structrtio__iodev__sqe.md#a2bd98599678909c0ddb22f879affa12b));

1474

1475static inline void z\_impl\_rtio\_sqe\_signal(struct [rtio\_sqe](structrtio__sqe.md) \*[sqe](structrtio__iodev__sqe.md#a2bd98599678909c0ddb22f879affa12b))

1476{

1477 struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \*iodev\_sqe = [CONTAINER\_OF](group__sys-util.md#gac5bc561d1bfd1bf68877fe577779bd2f)([sqe](structrtio__iodev__sqe.md#a2bd98599678909c0ddb22f879affa12b), struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md), [sqe](structrtio__iodev__sqe.md#a2bd98599678909c0ddb22f879affa12b));

1478

1479 if (![atomic\_cas](group__atomic__apis.md#gab879da5aa1ffcc317adc664c016586f7)(&iodev\_sqe->[sqe](structrtio__iodev__sqe.md#a2bd98599678909c0ddb22f879affa12b).[await](structrtio__sqe.md#a7ed5828c28fd59a34f5aa7262e4ddd20).[ok](structrtio__sqe.md#a45d8aad94aa1dac80c90cf7c0266bcd8), 0, 1)) {

1480 iodev\_sqe->[sqe](structrtio__iodev__sqe.md#a2bd98599678909c0ddb22f879affa12b).[await](structrtio__sqe.md#a7ed5828c28fd59a34f5aa7262e4ddd20).[callback](structrtio__sqe.md#af8c31c33e9fedebe55cac73595d0f696)(iodev\_sqe, iodev\_sqe->[sqe](structrtio__iodev__sqe.md#a2bd98599678909c0ddb22f879affa12b).[await](structrtio__sqe.md#a7ed5828c28fd59a34f5aa7262e4ddd20).[userdata](structrtio__sqe.md#a0ed519ee0b5867ff73bdaf37f983c971));

1481 }

1482}

1483

[ 1494](group__rtio.md#ga7d2e5673582f32b630e2294dfbf0fe44)static inline void [rtio\_iodev\_sqe\_await\_signal](group__rtio.md#ga7d2e5673582f32b630e2294dfbf0fe44)(struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \*iodev\_sqe,

1495 [rtio\_signaled\_t](group__rtio.md#gab254ffa4d10bfb670bacd1c47c1f8711) callback,

1496 void \*userdata)

1497{

1498 iodev\_sqe->[sqe](structrtio__iodev__sqe.md#a2bd98599678909c0ddb22f879affa12b).[await](structrtio__sqe.md#a7ed5828c28fd59a34f5aa7262e4ddd20).[callback](structrtio__sqe.md#af8c31c33e9fedebe55cac73595d0f696) = callback;

1499 iodev\_sqe->[sqe](structrtio__iodev__sqe.md#a2bd98599678909c0ddb22f879affa12b).[await](structrtio__sqe.md#a7ed5828c28fd59a34f5aa7262e4ddd20).[userdata](structrtio__sqe.md#a0ed519ee0b5867ff73bdaf37f983c971) = userdata;

1500

1501 if (![atomic\_cas](group__atomic__apis.md#gab879da5aa1ffcc317adc664c016586f7)(&iodev\_sqe->[sqe](structrtio__iodev__sqe.md#a2bd98599678909c0ddb22f879affa12b).[await](structrtio__sqe.md#a7ed5828c28fd59a34f5aa7262e4ddd20).[ok](structrtio__sqe.md#a45d8aad94aa1dac80c90cf7c0266bcd8), 0, 1)) {

1502 callback(iodev\_sqe, userdata);

1503 }

1504}

1505

[ 1521](group__rtio.md#ga830863e6c8d9b96f4c473a038cab8f8c)\_\_syscall int [rtio\_sqe\_copy\_in\_get\_handles](group__rtio.md#ga830863e6c8d9b96f4c473a038cab8f8c)(struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2), const struct [rtio\_sqe](structrtio__sqe.md) \*sqes,

1522 struct [rtio\_sqe](structrtio__sqe.md) \*\*handle, size\_t sqe\_count);

1523

1524static inline int z\_impl\_rtio\_sqe\_copy\_in\_get\_handles(struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2), const struct [rtio\_sqe](structrtio__sqe.md) \*sqes,

1525 struct [rtio\_sqe](structrtio__sqe.md) \*\*handle,

1526 size\_t sqe\_count)

1527{

1528 struct [rtio\_sqe](structrtio__sqe.md) \*sqe;

1529 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) acquirable = [rtio\_sqe\_acquirable](group__rtio.md#ga1f4fb7bccbaae08a94387e4b11275a78)([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2));

1530

1531 if (acquirable < sqe\_count) {

1532 return -[ENOMEM](group__system__errno.md#ga6a05c923dad0c1208043e9c20a58c8e5);

1533 }

1534

1535 for (unsigned long i = 0; i < sqe\_count; i++) {

1536 sqe = [rtio\_sqe\_acquire](group__rtio.md#ga8b47c954d15a334621def53acceb6799)([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2));

1537 \_\_ASSERT\_NO\_MSG(sqe != [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4));

1538 if (handle != [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4) && i == 0) {

1539 \*handle = sqe;

1540 }

1541 \*sqe = sqes[i];

1542 }

1543

1544 return 0;

1545}

1546

[ 1563](group__rtio.md#ga65e351af0a16dcf504a51ef4eb9316c7)static inline int [rtio\_sqe\_copy\_in](group__rtio.md#ga65e351af0a16dcf504a51ef4eb9316c7)(struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2), const struct [rtio\_sqe](structrtio__sqe.md) \*sqes, size\_t sqe\_count)

1564{

1565 return [rtio\_sqe\_copy\_in\_get\_handles](group__rtio.md#ga830863e6c8d9b96f4c473a038cab8f8c)([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2), sqes, [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4), sqe\_count);

1566}

1567

[ 1583](group__rtio.md#ga98b2bbef95aea342a9b86a9775dd5c3b)\_\_syscall int [rtio\_cqe\_copy\_out](group__rtio.md#ga98b2bbef95aea342a9b86a9775dd5c3b)(struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2),

1584 struct [rtio\_cqe](structrtio__cqe.md) \*cqes,

1585 size\_t cqe\_count,

1586 [k\_timeout\_t](structk__timeout__t.md) [timeout](structrtio__sqe.md#a544c75ee10281e10e83f51df5b157d62));

1587static inline int z\_impl\_rtio\_cqe\_copy\_out(struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2),

1588 struct [rtio\_cqe](structrtio__cqe.md) \*cqes,

1589 size\_t cqe\_count,

1590 [k\_timeout\_t](structk__timeout__t.md) [timeout](structrtio__sqe.md#a544c75ee10281e10e83f51df5b157d62))

1591{

1592 size\_t copied = 0;

1593 struct [rtio\_cqe](structrtio__cqe.md) \*cqe;

1594 [k\_timepoint\_t](structk__timepoint__t.md) end = [sys\_timepoint\_calc](group__clock__apis.md#ga509cf4599c1f162c97540743e8c21d33)(timeout);

1595

1596 do {

1597 cqe = [K\_TIMEOUT\_EQ](group__clock__apis.md#ga9abf00b34e16ab7ad0883603b6778b1b)(timeout, [K\_FOREVER](group__clock__apis.md#ga0bb4b83f0222193b21a8910311bab0ca)) ? [rtio\_cqe\_consume\_block](group__rtio.md#gaf617d05d9b59ce1f1d0697617ef6f249)([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2))

1598 : [rtio\_cqe\_consume](group__rtio.md#gae562cf241911804cdb9f4e3a73b53df4)([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2));

1599 if (cqe == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

1600 Z\_SPIN\_DELAY(25);

1601 continue;

1602 }

1603 cqes[copied++] = \*cqe;

1604 [rtio\_cqe\_release](group__rtio.md#gaa0799a5f8ad98425d385a07c5d27d9cb)([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2), cqe);

1605 } while (copied < cqe\_count && ![sys\_timepoint\_expired](group__clock__apis.md#ga87d0d7a0f7bcdcc8c4909962eac12985)(end));

1606

1607 return copied;

1608}

1609

[ 1625](group__rtio.md#gafee27c64a4a4989c4eb774addde8eb2e)\_\_syscall int [rtio\_submit](group__rtio.md#gafee27c64a4a4989c4eb774addde8eb2e)(struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2), [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) wait\_count);

1626

1627#ifdef CONFIG\_RTIO\_SUBMIT\_SEM

1628static inline int z\_impl\_rtio\_submit(struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2), [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) wait\_count)

1629{

1630 int res = 0;

1631

1632 if (wait\_count > 0) {

1633 \_\_ASSERT(![k\_is\_in\_isr](group__isr__apis.md#ga8482b0dd2283d12677a9ebe321667d16)(),

1634 "expected rtio submit with wait count to be called from a thread");

1635

1636 [k\_sem\_reset](group__semaphore__apis.md#ga1bd12d8d8c1b9c6be9b665d0fefe5562)([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->submit\_sem);

1637 [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->submit\_count = wait\_count;

1638 }

1639

1640 [rtio\_executor\_submit](group__rtio.md#gaf191153e83de72ddefb998daad02fa16)([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2));

1641

1642 if (wait\_count > 0) {

1643 res = [k\_sem\_take](group__semaphore__apis.md#gac71e2383c1920dddc45a561cacfef090)([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->submit\_sem, [K\_FOREVER](group__clock__apis.md#ga0bb4b83f0222193b21a8910311bab0ca));

1644 \_\_ASSERT(res == 0,

1645 "semaphore was reset or timed out while waiting on completions!");

1646 }

1647

1648 return res;

1649}

1650#else

1651static inline int z\_impl\_rtio\_submit(struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2), [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) wait\_count)

1652{

1653

1654 int res = 0;

1655 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) cq\_count = ([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808))[atomic\_get](group__atomic__apis.md#ga33bb426a17535bd1022895a7e44b32fa)(&[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->cq\_count);

1656 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) cq\_complete\_count = cq\_count + wait\_count;

1657 bool wraps = cq\_complete\_count < cq\_count;

1658

1659 [rtio\_executor\_submit](group__rtio.md#gaf191153e83de72ddefb998daad02fa16)([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2));

1660

1661 if (wraps) {

1662 while (([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808))[atomic\_get](group__atomic__apis.md#ga33bb426a17535bd1022895a7e44b32fa)(&[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->cq\_count) >= cq\_count) {

1663 Z\_SPIN\_DELAY(10);

1664 [k\_yield](group__thread__apis.md#ga08a3484c33444ecedc2d71d78495a295)();

1665 }

1666 }

1667

1668 while (([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808))[atomic\_get](group__atomic__apis.md#ga33bb426a17535bd1022895a7e44b32fa)(&[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->cq\_count) < cq\_complete\_count) {

1669 Z\_SPIN\_DELAY(10);

1670 [k\_yield](group__thread__apis.md#ga08a3484c33444ecedc2d71d78495a295)();

1671 }

1672

1673 return res;

1674}

1675#endif /\* CONFIG\_RTIO\_SUBMIT\_SEM \*/

1676

1680

1681#ifdef \_\_cplusplus

1682}

1683#endif

1684

1685#include <zephyr/syscalls/rtio.h>

1686

1687#endif /\* ZEPHYR\_INCLUDE\_RTIO\_RTIO\_H\_ \*/

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

[atomic\_cas](group__atomic__apis.md#gab879da5aa1ffcc317adc664c016586f7)

bool atomic\_cas(atomic\_t \*target, atomic\_val\_t old\_value, atomic\_val\_t new\_value)

Atomic compare-and-set.

[K\_FOREVER](group__clock__apis.md#ga0bb4b83f0222193b21a8910311bab0ca)

#define K\_FOREVER

Generate infinite timeout delay.

**Definition** kernel.h:1481

[K\_NO\_WAIT](group__clock__apis.md#ga3d9541cfe2e8395af66d186efa77362f)

#define K\_NO\_WAIT

Generate null timeout delay.

**Definition** kernel.h:1371

[sys\_timepoint\_calc](group__clock__apis.md#ga509cf4599c1f162c97540743e8c21d33)

k\_timepoint\_t sys\_timepoint\_calc(k\_timeout\_t timeout)

Calculate a timepoint value.

[sys\_timepoint\_expired](group__clock__apis.md#ga87d0d7a0f7bcdcc8c4909962eac12985)

static bool sys\_timepoint\_expired(k\_timepoint\_t timepoint)

Indicates if timepoint is expired.

**Definition** clock.h:339

[K\_TIMEOUT\_EQ](group__clock__apis.md#ga9abf00b34e16ab7ad0883603b6778b1b)

#define K\_TIMEOUT\_EQ(a, b)

Compare timeouts for equality.

**Definition** clock.h:80

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

**Definition** rtio.h:179

[RTIO\_CQE\_FLAG\_MEMPOOL\_GET\_BLK\_IDX](group__rtio__cqe__flags.md#ga0b5f3f7e7be472ecf87bd2b08c1888da)

#define RTIO\_CQE\_FLAG\_MEMPOOL\_GET\_BLK\_IDX(flags)

Get the block index of a mempool flags.

**Definition** rtio.h:171

[RTIO\_CQE\_FLAG\_MEMPOOL\_BUFFER](group__rtio__cqe__flags.md#ga0f212500447a5e37e225a6997953b609)

#define RTIO\_CQE\_FLAG\_MEMPOOL\_BUFFER

The entry's buffer was allocated from the RTIO's mempool.

**Definition** rtio.h:161

[RTIO\_CQE\_FLAG\_PREP\_MEMPOOL](group__rtio__cqe__flags.md#ga28b3a5661248b6b3763aab47417114d6)

#define RTIO\_CQE\_FLAG\_PREP\_MEMPOOL(blk\_idx, blk\_cnt)

Prepare CQE flags for a mempool read.

**Definition** rtio.h:188

[RTIO\_CQE\_FLAG\_GET](group__rtio__cqe__flags.md#gaef64ea020a20ac22a0edcb6eca032efc)

#define RTIO\_CQE\_FLAG\_GET(flags)

**Definition** rtio.h:163

[RTIO\_SQE\_MULTISHOT](group__rtio__sqe__flags.md#ga00f8ead8f043fe40d49d0bc3325fb299)

#define RTIO\_SQE\_MULTISHOT

The SQE should continue producing CQEs until canceled.

**Definition** rtio.h:137

[RTIO\_SQE\_TRANSACTION](group__rtio__sqe__flags.md#ga07f09cc0c95be6cfdddb23f8acacb1ea)

#define RTIO\_SQE\_TRANSACTION

The next request in the queue is part of a transaction.

**Definition** rtio.h:109

[RTIO\_SQE\_MEMPOOL\_BUFFER](group__rtio__sqe__flags.md#ga2802b46584220afffa0e959e149d5a4d)

#define RTIO\_SQE\_MEMPOOL\_BUFFER

The buffer should be allocated by the RTIO mempool.

**Definition** rtio.h:121

[RTIO\_SQE\_CANCELED](group__rtio__sqe__flags.md#ga7f7f9b038ab8409f271b1aebc1b95ee6)

#define RTIO\_SQE\_CANCELED

The SQE should not execute if possible.

**Definition** rtio.h:129

[RTIO\_SQE\_NO\_RESPONSE](group__rtio__sqe__flags.md#ga8578ffdb8f53a51b94fa86a6f02d4a11)

#define RTIO\_SQE\_NO\_RESPONSE

The SQE does not produce a CQE.

**Definition** rtio.h:142

[RTIO\_SQE\_CHAINED](group__rtio__sqe__flags.md#gae9191d521d4ab602b53fefb74020d06b)

#define RTIO\_SQE\_CHAINED

The next request in the queue should wait on this one.

**Definition** rtio.h:97

[rtio\_sqe\_prep\_read\_with\_pool](group__rtio.md#ga15c1f623658d27d300d1a31a6f3d6b9d)

static void rtio\_sqe\_prep\_read\_with\_pool(struct rtio\_sqe \*sqe, const struct rtio\_iodev \*iodev, int8\_t prio, void \*userdata)

Prepare a read op submission with context's mempool.

**Definition** rtio.h:623

[rtio\_executor\_err](group__rtio.md#ga15f4a1a4dfb869ef9e4216dc1c1cdc8a)

void rtio\_executor\_err(struct rtio\_iodev\_sqe \*iodev\_sqe, int result)

[RTIO\_OP\_CALLBACK](group__rtio.md#ga18e0ff7d44e4c33900106aefad0a8508)

#define RTIO\_OP\_CALLBACK

An operation that calls a given function (callback).

**Definition** rtio.h:560

[rtio\_sqe\_acquirable](group__rtio.md#ga1f4fb7bccbaae08a94387e4b11275a78)

static uint32\_t rtio\_sqe\_acquirable(struct rtio \*r)

Count of acquirable submission queue events.

**Definition** rtio.h:993

[rtio\_sqe\_prep\_delay](group__rtio.md#ga2169a7a776a5300b25f599144de4de0b)

static void rtio\_sqe\_prep\_delay(struct rtio\_sqe \*sqe, k\_timeout\_t timeout, void \*userdata)

**Definition** rtio.h:760

[rtio\_cqe\_pool\_free](group__rtio.md#ga23c0c5d4b551858eabe057ecb8a28d12)

static void rtio\_cqe\_pool\_free(struct rtio\_cqe\_pool \*pool, struct rtio\_cqe \*cqe)

**Definition** rtio.h:811

[rtio\_sqe\_prep\_tiny\_write](group__rtio.md#ga31be14ece09e061a8d42ca8f2395286a)

static void rtio\_sqe\_prep\_tiny\_write(struct rtio\_sqe \*sqe, const struct rtio\_iodev \*iodev, int8\_t prio, const uint8\_t \*tiny\_write\_data, uint8\_t tiny\_write\_len, void \*userdata)

Prepare a tiny write op submission.

**Definition** rtio.h:668

[rtio\_mempool\_block\_size](group__rtio.md#ga4213be028b0a1264daaa0d30c4c2d089)

static size\_t rtio\_mempool\_block\_size(const struct rtio \*r)

Get the mempool block size of the RTIO context.

**Definition** rtio.h:472

[rtio\_cqe\_submit](group__rtio.md#ga4abc221d5a90ab882000a72caa0ebd0f)

static void rtio\_cqe\_submit(struct rtio \*r, int result, void \*userdata, uint32\_t flags)

Submit a completion queue event with a given result and userdata.

**Definition** rtio.h:1301

[rtio\_sqe\_prep\_nop](group__rtio.md#ga599ee43fdf35e1cf895cbbe9272e4c50)

static void rtio\_sqe\_prep\_nop(struct rtio\_sqe \*sqe, const struct rtio\_iodev \*iodev, void \*userdata)

Prepare a nop (no op) submission.

**Definition** rtio.h:589

[rtio\_release\_buffer](group__rtio.md#ga6530bf56ccbab046a362a6448f941609)

void rtio\_release\_buffer(struct rtio \*r, void \*buff, uint32\_t buff\_len)

Release memory that was allocated by the RTIO's memory pool.

[rtio\_sqe\_copy\_in](group__rtio.md#ga65e351af0a16dcf504a51ef4eb9316c7)

static int rtio\_sqe\_copy\_in(struct rtio \*r, const struct rtio\_sqe \*sqes, size\_t sqe\_count)

Copy an array of SQEs into the queue.

**Definition** rtio.h:1563

[rtio\_cqe\_produce](group__rtio.md#ga6f55202adeca60aed0343a7a0dcab071)

static void rtio\_cqe\_produce(struct rtio \*r, struct rtio\_cqe \*cqe)

Produce a complete queue event if available.

**Definition** rtio.h:1103

[RTIO\_OP\_TINY\_TX](group__rtio.md#ga6f95c0a5fbcc020a0d1102d3b08934bd)

#define RTIO\_OP\_TINY\_TX

An operation that transmits tiny writes by copying the data to write.

**Definition** rtio.h:557

[rtio\_cqe\_compute\_flags](group__rtio.md#ga75661c8c6c94a0ac6254cec674b478c8)

static uint32\_t rtio\_cqe\_compute\_flags(struct rtio\_iodev\_sqe \*iodev\_sqe)

Compute the CQE flags from the rtio\_iodev\_sqe entry.

**Definition** rtio.h:1184

[rtio\_iodev\_sqe\_await\_signal](group__rtio.md#ga7d2e5673582f32b630e2294dfbf0fe44)

static void rtio\_iodev\_sqe\_await\_signal(struct rtio\_iodev\_sqe \*iodev\_sqe, rtio\_signaled\_t callback, void \*userdata)

Await an AWAIT SQE signal from RTIO IODEV.

**Definition** rtio.h:1494

[rtio\_executor\_ok](group__rtio.md#ga7e2ebd9abaf585207bc5b99c5d815c6a)

void rtio\_executor\_ok(struct rtio\_iodev\_sqe \*iodev\_sqe, int result)

[rtio\_block\_pool\_alloc](group__rtio.md#ga7f14b99fc1dd0697309e7f71a270f5fb)

static int rtio\_block\_pool\_alloc(struct rtio \*r, size\_t min\_sz, size\_t max\_sz, uint8\_t \*\*buf, uint32\_t \*buf\_len)

**Definition** rtio.h:818

[rtio\_sqe\_prep\_write](group__rtio.md#ga7f7856d1f4fd1d8c4f6eebcccfe77701)

static void rtio\_sqe\_prep\_write(struct rtio\_sqe \*sqe, const struct rtio\_iodev \*iodev, int8\_t prio, const uint8\_t \*buf, uint32\_t len, void \*userdata)

Prepare a write op submission.

**Definition** rtio.h:642

[rtio\_sqe\_copy\_in\_get\_handles](group__rtio.md#ga830863e6c8d9b96f4c473a038cab8f8c)

int rtio\_sqe\_copy\_in\_get\_handles(struct rtio \*r, const struct rtio\_sqe \*sqes, struct rtio\_sqe \*\*handle, size\_t sqe\_count)

Copy an array of SQEs into the queue and get resulting handles back.

[rtio\_cqe\_pool\_alloc](group__rtio.md#ga8497170f55af1d11d717e919f61806f5)

static struct rtio\_cqe \* rtio\_cqe\_pool\_alloc(struct rtio\_cqe\_pool \*pool)

**Definition** rtio.h:794

[rtio\_partition](group__rtio.md#ga86a38086dd85150ab6e479d73db1c6d1)

struct k\_mem\_partition rtio\_partition

The memory partition associated with all RTIO context information.

[rtio\_sqe\_prep\_read](group__rtio.md#ga89c7cc2494e3dda50737f78f1a1376cf)

static void rtio\_sqe\_prep\_read(struct rtio\_sqe \*sqe, const struct rtio\_iodev \*iodev, int8\_t prio, uint8\_t \*buf, uint32\_t len, void \*userdata)

Prepare a read op submission.

**Definition** rtio.h:602

[rtio\_sqe\_acquire](group__rtio.md#ga8b47c954d15a334621def53acceb6799)

static struct rtio\_sqe \* rtio\_sqe\_acquire(struct rtio \*r)

Acquire a single submission queue event if available.

**Definition** rtio.h:1054

[RTIO\_OP\_TX](group__rtio.md#ga8dcaef0cda159e16520a95543ff62827)

#define RTIO\_OP\_TX

An operation that transmits (writes).

**Definition** rtio.h:554

[rtio\_sqe\_drop\_all](group__rtio.md#ga9486fb7b50e8d2409a50da235203536b)

static void rtio\_sqe\_drop\_all(struct rtio \*r)

Drop all previously acquired sqe.

**Definition** rtio.h:1072

[rtio\_sqe\_prep\_read\_multishot](group__rtio.md#ga9803aa829f8c0eeee746ea7d872c20cc)

static void rtio\_sqe\_prep\_read\_multishot(struct rtio\_sqe \*sqe, const struct rtio\_iodev \*iodev, int8\_t prio, void \*userdata)

**Definition** rtio.h:631

[rtio\_cqe\_copy\_out](group__rtio.md#ga98b2bbef95aea342a9b86a9775dd5c3b)

int rtio\_cqe\_copy\_out(struct rtio \*r, struct rtio\_cqe \*cqes, size\_t cqe\_count, k\_timeout\_t timeout)

Copy an array of CQEs from the queue.

[rtio\_sqe\_prep\_callback](group__rtio.md#ga9d0dd7d0e2e3d281092f2350d6e1713e)

static void rtio\_sqe\_prep\_callback(struct rtio\_sqe \*sqe, rtio\_callback\_t callback, void \*arg0, void \*userdata)

Prepare a callback op submission.

**Definition** rtio.h:694

[rtio\_access\_grant](group__rtio.md#ga9da42c98546930575525f0f92710f9e4)

static void rtio\_access\_grant(struct rtio \*r, struct k\_thread \*t)

Grant access to an RTIO context to a user thread.

**Definition** rtio.h:1425

[RTIO\_OP\_TXRX](group__rtio.md#ga9f0e70f5a28be65a8ed67c0257a72692)

#define RTIO\_OP\_TXRX

An operation that transceives (reads and writes simultaneously).

**Definition** rtio.h:563

[rtio\_cqe\_release](group__rtio.md#gaa0799a5f8ad98425d385a07c5d27d9cb)

static void rtio\_cqe\_release(struct rtio \*r, struct rtio\_cqe \*cqe)

Release consumed completion queue event.

**Definition** rtio.h:1173

[rtio\_sqe\_rx\_buf](group__rtio.md#gaab6843e2038d00a8354f57d7e2ffcf7e)

static int rtio\_sqe\_rx\_buf(const struct rtio\_iodev\_sqe \*iodev\_sqe, uint32\_t min\_buf\_len, uint32\_t max\_buf\_len, uint8\_t \*\*buf, uint32\_t \*buf\_len)

Get the buffer associate with the RX submission.

**Definition** rtio.h:1351

[rtio\_iodev\_sqe\_err](group__rtio.md#gaada07aa6acefa548743b525225fa482f)

static void rtio\_iodev\_sqe\_err(struct rtio\_iodev\_sqe \*iodev\_sqe, int result)

Inform the executor of a submissions completion with error.

**Definition** rtio.h:1285

[rtio\_signaled\_t](group__rtio.md#gab254ffa4d10bfb670bacd1c47c1f8711)

void(\* rtio\_signaled\_t)(struct rtio\_iodev\_sqe \*iodev\_sqe, void \*userdata)

Callback signature for RTIO\_OP\_AWAIT signaled.

**Definition** rtio.h:290

[rtio\_sqe\_prep\_transceive](group__rtio.md#gab9b605dcbb01d21c88f9ae70588ea3b5)

static void rtio\_sqe\_prep\_transceive(struct rtio\_sqe \*sqe, const struct rtio\_iodev \*iodev, int8\_t prio, const uint8\_t \*tx\_buf, uint8\_t \*rx\_buf, uint32\_t buf\_len, void \*userdata)

Prepare a transceive op submission.

**Definition** rtio.h:730

[rtio\_sqe\_cancel](group__rtio.md#gac01252e55d2848b38c0ed77b71d600a7)

int rtio\_sqe\_cancel(struct rtio\_sqe \*sqe)

Attempt to cancel an SQE.

[rtio\_sqe\_pool\_free](group__rtio.md#gac776aea3692cfd77aa5bf675a9e9ed02)

static void rtio\_sqe\_pool\_free(struct rtio\_sqe\_pool \*pool, struct rtio\_iodev\_sqe \*iodev\_sqe)

**Definition** rtio.h:787

[rtio\_iodev\_sqe\_ok](group__rtio.md#gacb1d2ffa2b07418d8a8aa319bd4336ab)

static void rtio\_iodev\_sqe\_ok(struct rtio\_iodev\_sqe \*iodev\_sqe, int result)

Inform the executor of a submission completion with success.

**Definition** rtio.h:1272

[rtio\_callback\_t](group__rtio.md#gad1dbd690e6cf88d7c788436dd04d1a00)

void(\* rtio\_callback\_t)(struct rtio \*r, const struct rtio\_sqe \*sqe, void \*arg0)

Callback signature for RTIO\_OP\_CALLBACK.

**Definition** rtio.h:282

[RTIO\_OP\_NOP](group__rtio.md#gad5f073978f641413989d1c6b405d6c36)

#define RTIO\_OP\_NOP

An operation that does nothing and will complete immediately.

**Definition** rtio.h:548

[RTIO\_OP\_AWAIT](group__rtio.md#gad74290935595b83040676b426cd07161)

#define RTIO\_OP\_AWAIT

An operation to suspend bus while awaiting signal.

**Definition** rtio.h:584

[rtio\_cqe\_acquire](group__rtio.md#gad848646651fdf3649b882e5268f72a3c)

static struct rtio\_cqe \* rtio\_cqe\_acquire(struct rtio \*r)

Acquire a complete queue event if available.

**Definition** rtio.h:1087

[rtio\_chain\_next](group__rtio.md#gada1e3abf92a46e376138435debc8baf4)

static struct rtio\_iodev\_sqe \* rtio\_chain\_next(const struct rtio\_iodev\_sqe \*iodev\_sqe)

Get the next sqe in the chain.

**Definition** rtio.h:1024

[rtio\_cqe\_consume](group__rtio.md#gae562cf241911804cdb9f4e3a73b53df4)

static struct rtio\_cqe \* rtio\_cqe\_consume(struct rtio \*r)

Consume a single completion queue event if available.

**Definition** rtio.h:1119

[rtio\_sqe\_pool\_alloc](group__rtio.md#gae5fb03fc8f3a4a774f476ff552999bfc)

static struct rtio\_iodev\_sqe \* rtio\_sqe\_pool\_alloc(struct rtio\_sqe\_pool \*pool)

**Definition** rtio.h:772

[rtio\_sqe\_signal](group__rtio.md#gae63ffc626a3e99406d36aa47f10b49e1)

void rtio\_sqe\_signal(struct rtio\_sqe \*sqe)

Signal an AWAIT SQE.

[rtio\_iodev\_sqe\_next](group__rtio.md#gae690e3dc0fc40dda57257b2eed432719)

static struct rtio\_iodev\_sqe \* rtio\_iodev\_sqe\_next(const struct rtio\_iodev\_sqe \*iodev\_sqe)

Get the next sqe in the chain or transaction.

**Definition** rtio.h:1041

[rtio\_sqe\_prep\_callback\_no\_cqe](group__rtio.md#gae87be354087d038953dae07c7f9cd3b0)

static void rtio\_sqe\_prep\_callback\_no\_cqe(struct rtio\_sqe \*sqe, rtio\_callback\_t callback, void \*arg0, void \*userdata)

Prepare a callback op submission that does not create a CQE.

**Definition** rtio.h:718

[RTIO\_OP\_DELAY](group__rtio.md#gae8da4da54f32963190f52c7533d4c951)

#define RTIO\_OP\_DELAY

An operation that takes a specified amount of time (asynchronously) before completing.

**Definition** rtio.h:566

[rtio\_cqe\_get\_mempool\_buffer](group__rtio.md#gaedbf9386a36ed99baa290ef6c318ded1)

int rtio\_cqe\_get\_mempool\_buffer(const struct rtio \*r, struct rtio\_cqe \*cqe, uint8\_t \*\*buff, uint32\_t \*buff\_len)

Retrieve the mempool buffer that was allocated for the CQE.

[rtio\_txn\_next](group__rtio.md#gaef904eb6a8810d8c3ea537c4d6edbee5)

static struct rtio\_iodev\_sqe \* rtio\_txn\_next(const struct rtio\_iodev\_sqe \*iodev\_sqe)

Get the next sqe in the transaction.

**Definition** rtio.h:1006

[rtio\_executor\_submit](group__rtio.md#gaf191153e83de72ddefb998daad02fa16)

void rtio\_executor\_submit(struct rtio \*r)

[rtio\_cqe\_consume\_block](group__rtio.md#gaf617d05d9b59ce1f1d0697617ef6f249)

static struct rtio\_cqe \* rtio\_cqe\_consume\_block(struct rtio \*r)

Wait for and consume a single completion queue event.

**Definition** rtio.h:1149

[rtio\_block\_pool\_free](group__rtio.md#gafca7732926a9a7c080e3cb16e5f16108)

static void rtio\_block\_pool\_free(struct rtio \*r, void \*buf, uint32\_t buf\_len)

**Definition** rtio.h:859

[rtio\_sqe\_prep\_await](group__rtio.md#gafd97c145b8525895494a31a87610f65d)

static void rtio\_sqe\_prep\_await(struct rtio\_sqe \*sqe, const struct rtio\_iodev \*iodev, int8\_t prio, void \*userdata)

**Definition** rtio.h:748

[RTIO\_OP\_RX](group__rtio.md#gafeb05c351207cd1638fa78f6607e1a4a)

#define RTIO\_OP\_RX

An operation that receives (reads).

**Definition** rtio.h:551

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

**Definition** util.h:285

[DIV\_ROUND\_UP](group__sys-util.md#gae664e7492e37d324831caf2321ddda37)

#define DIV\_ROUND\_UP(n, d)

Divide and round up.

**Definition** util.h:353

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

[NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)

#define NULL

**Definition** iar\_missing\_defs.h:20

[kernel.h](kernel_8h.md)

Public kernel APIs.

[kernel\_structs.h](kernel__structs_8h.md)

[mem\_blocks.h](mem__blocks_8h.md)

Memory Blocks Allocator.

[mpsc\_lockfree.h](mpsc__lockfree_8h.md)

A wait-free intrusive multi producer single consumer (MPSC) queue using a singly linked list.

[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)

flags

**Definition** parser.h:97

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

[k\_sem](structk__sem.md)

Semaphore structure.

**Definition** kernel.h:3275

[k\_thread](structk__thread.md)

Thread Structure.

**Definition** thread.h:262

[k\_timeout\_t](structk__timeout__t.md)

Kernel timeout type.

**Definition** clock.h:65

[k\_timepoint\_t](structk__timepoint__t.md)

Kernel timepoint type.

**Definition** clock.h:242

[mpsc\_node](structmpsc__node.md)

Queue member.

**Definition** mpsc\_lockfree.h:79

[mpsc](structmpsc.md)

MPSC Queue.

**Definition** mpsc\_lockfree.h:86

[rtio\_cqe\_pool](structrtio__cqe__pool.md)

**Definition** rtio.h:400

[rtio\_cqe\_pool::pool](structrtio__cqe__pool.md#a05584219d473fcf85d46757fa9cea703)

struct rtio\_cqe \* pool

**Definition** rtio.h:404

[rtio\_cqe\_pool::free\_q](structrtio__cqe__pool.md#a13bd7991ff5622c1cb5aa6af014aaab3)

struct mpsc free\_q

**Definition** rtio.h:401

[rtio\_cqe\_pool::pool\_size](structrtio__cqe__pool.md#a43bf4141673c61493644539987f27fb1)

const uint16\_t pool\_size

**Definition** rtio.h:402

[rtio\_cqe\_pool::pool\_free](structrtio__cqe__pool.md#a4fb501a0ba15e2956113deaf4597d846)

uint16\_t pool\_free

**Definition** rtio.h:403

[rtio\_cqe](structrtio__cqe.md)

A completion queue event.

**Definition** rtio.h:385

[rtio\_cqe::userdata](structrtio__cqe.md#a15128387ccbea55812ef229eab7241e7)

void \* userdata

Associated userdata with operation.

**Definition** rtio.h:389

[rtio\_cqe::q](structrtio__cqe.md#a27272bca31c170f406799633ec82098d)

struct mpsc\_node q

**Definition** rtio.h:386

[rtio\_cqe::flags](structrtio__cqe.md#a8a7632ef1cfd31529d782bd761908d93)

uint32\_t flags

Flags associated with the operation.

**Definition** rtio.h:390

[rtio\_cqe::result](structrtio__cqe.md#acbe2e6607a752b676d9336b9ca6ce435)

int32\_t result

Result from operation.

**Definition** rtio.h:388

[rtio\_iodev\_api](structrtio__iodev__api.md)

API that an RTIO IO device should implement.

**Definition** rtio.h:524

[rtio\_iodev\_api::submit](structrtio__iodev__api.md#a6cd795906753535571ec1ecc0e0c430c)

void(\* submit)(struct rtio\_iodev\_sqe \*iodev\_sqe)

Submit to the iodev an entry to work on.

**Definition** rtio.h:533

[rtio\_iodev\_sqe](structrtio__iodev__sqe.md)

Compute the mempool block index for a given pointer.

**Definition** rtio.h:514

[rtio\_iodev\_sqe::next](structrtio__iodev__sqe.md#a2afb82e550e614f87db7cd1bf2c3a352)

struct rtio\_iodev\_sqe \* next

**Definition** rtio.h:517

[rtio\_iodev\_sqe::sqe](structrtio__iodev__sqe.md#a2bd98599678909c0ddb22f879affa12b)

struct rtio\_sqe sqe

**Definition** rtio.h:515

[rtio\_iodev\_sqe::r](structrtio__iodev__sqe.md#a3c3a050793589258eab5ff5ac30f24c8)

struct rtio \* r

**Definition** rtio.h:518

[rtio\_iodev\_sqe::q](structrtio__iodev__sqe.md#a9cfdd004b65a5e2bc111bc2fb333498c)

struct mpsc\_node q

**Definition** rtio.h:516

[rtio\_iodev](structrtio__iodev.md)

An IO device with a function table for submitting requests.

**Definition** rtio.h:539

[rtio\_iodev::api](structrtio__iodev.md#a6dfedbfb58356e0647e5c20632656977)

const struct rtio\_iodev\_api \* api

**Definition** rtio.h:541

[rtio\_iodev::data](structrtio__iodev.md#af0f3a27fe8dea2161c9a73cb838bdeec)

void \* data

**Definition** rtio.h:544

[rtio\_sqe\_pool](structrtio__sqe__pool.md)

**Definition** rtio.h:393

[rtio\_sqe\_pool::pool](structrtio__sqe__pool.md#ab2c0394e175bd8c6f0c02edb315b6c9b)

struct rtio\_iodev\_sqe \* pool

**Definition** rtio.h:397

[rtio\_sqe\_pool::pool\_size](structrtio__sqe__pool.md#ade3b4354d007fe17a7753c26e2121465)

const uint16\_t pool\_size

**Definition** rtio.h:395

[rtio\_sqe\_pool::free\_q](structrtio__sqe__pool.md#aed49ea25c952e07a8287919268fd2485)

struct mpsc free\_q

**Definition** rtio.h:394

[rtio\_sqe\_pool::pool\_free](structrtio__sqe__pool.md#af7990b1510ad2343573f3e4e502475b0)

uint16\_t pool\_free

**Definition** rtio.h:396

[rtio\_sqe](structrtio__sqe.md)

A submission queue event.

**Definition** rtio.h:295

[rtio\_sqe::i2c\_config](structrtio__sqe.md#a07bf344b1b1063b8bea80cf5ba1c1cc5)

uint32\_t i2c\_config

OP\_I2C\_CONFIGURE.

**Definition** rtio.h:355

[rtio\_sqe::userdata](structrtio__sqe.md#a0ed519ee0b5867ff73bdaf37f983c971)

void \* userdata

User provided data which is returned upon operation completion.

**Definition** rtio.h:313

[rtio\_sqe::tx\_buf](structrtio__sqe.md#a18bfa63542954f4bb8b924c92c48e931)

const uint8\_t \* tx\_buf

Buffer to write from.

**Definition** rtio.h:344

[rtio\_sqe::tiny\_tx](structrtio__sqe.md#a19ace9c984538c2022e7f8ecaefa075d)

struct rtio\_sqe::@346015370260157122324174060242055067274246076272::@156103043324343070111363144011175302340145332235 tiny\_tx

OP\_TINY\_TX.

[rtio\_sqe::op](structrtio__sqe.md#a1d8d3e3426e47a2c7f54d98f51acd953)

uint8\_t op

Op code.

**Definition** rtio.h:296

[rtio\_sqe::rx](structrtio__sqe.md#a37a98afc43f26355c70e7036725b2544)

struct rtio\_sqe::@346015370260157122324174060242055067274246076272::@133276262235321357167246345002275273273102345261 rx

OP\_RX.

[rtio\_sqe::arg0](structrtio__sqe.md#a438d2156a61aef9ca840af9c01d5dfa4)

void \* arg0

Last argument given to callback.

**Definition** rtio.h:338

[rtio\_sqe::tx](structrtio__sqe.md#a4399cf25c7e761126a6218c2b7e3192d)

struct rtio\_sqe::@346015370260157122324174060242055067274246076272::@004235137221060376063310265133374117312204154130 tx

OP\_TX.

[rtio\_sqe::ok](structrtio__sqe.md#a45d8aad94aa1dac80c90cf7c0266bcd8)

atomic\_t ok

**Definition** rtio.h:370

[rtio\_sqe::rx\_buf](structrtio__sqe.md#a4d2090fc11b897724a883ad1087d9f73)

uint8\_t \* rx\_buf

Buffer to read into.

**Definition** rtio.h:345

[rtio\_sqe::prio](structrtio__sqe.md#a528eb9b721be7b8a8898ab16a7e2d9a7)

uint8\_t prio

Op priority.

**Definition** rtio.h:298

[rtio\_sqe::timeout](structrtio__sqe.md#a544c75ee10281e10e83f51df5b157d62)

k\_timeout\_t timeout

Delay timeout.

**Definition** rtio.h:350

[rtio\_sqe::to](structrtio__sqe.md#a582d4a8022d237f894034a5a92511587)

struct \_timeout to

Timeout struct.

**Definition** rtio.h:351

[rtio\_sqe::txrx](structrtio__sqe.md#a5f2511eb361a7a4d54a92fae4d391e8c)

struct rtio\_sqe::@346015370260157122324174060242055067274246076272::@324335144354230362066357340057163170350241057343 txrx

OP\_TXRX.

[rtio\_sqe::buf\_len](structrtio__sqe.md#a67376f40a13960b152a23da250275722)

uint32\_t buf\_len

Length of buffer.

**Definition** rtio.h:319

[rtio\_sqe::iodev](structrtio__sqe.md#a6c784702f011592c84feacd57915bbfc)

const struct rtio\_iodev \* iodev

Device to operation on.

**Definition** rtio.h:304

[rtio\_sqe::await](structrtio__sqe.md#a7ed5828c28fd59a34f5aa7262e4ddd20)

struct rtio\_sqe::@346015370260157122324174060242055067274246076272::@377160164316265207047041027316236163055075120351 await

OP\_AWAIT.

[rtio\_sqe::iodev\_flags](structrtio__sqe.md#a8bebe5d55aa8549d749466e444fadf91)

uint32\_t iodev\_flags

Op iodev flags.

**Definition** rtio.h:302

[rtio\_sqe::ccc\_payload](structrtio__sqe.md#a8d78973983abca8b97cfc5bcdc2dd2f1)

void \* ccc\_payload

OP\_I3C\_CCC.

**Definition** rtio.h:366

[rtio\_sqe::delay](structrtio__sqe.md#a9a93700154d745bc1bacc764bbfbe696)

struct rtio\_sqe::@346015370260157122324174060242055067274246076272::@242110314202367053245316142070211303126322345320 delay

OP\_DELAY.

[rtio\_sqe::type](structrtio__sqe.md#aa09a0c93a6e8cfc73278a87942e4af33)

int type

**Definition** rtio.h:360

[rtio\_sqe::flags](structrtio__sqe.md#aad2ff8524df0e24b812e77e2393bf5b0)

uint16\_t flags

Op Flags.

**Definition** rtio.h:300

[rtio\_sqe::buf](structrtio__sqe.md#ab71176c084e8b8eb65dfeb3018ae2a49)

const uint8\_t \* buf

Buffer to write from.

**Definition** rtio.h:320

[rtio\_sqe::config](structrtio__sqe.md#ac07a16c50a067acc90bd4ab08aae4184)

void \* config

**Definition** rtio.h:361

[rtio\_sqe::callback](structrtio__sqe.md#af8c31c33e9fedebe55cac73595d0f696)

rtio\_callback\_t callback

**Definition** rtio.h:337

[rtio](structrtio.md)

An RTIO context containing what can be viewed as a pair of queues.

**Definition** rtio.h:418

[rtio::cqe\_pool](structrtio.md#a1bce3c3bb0150275ece65975adf3ee4f)

struct rtio\_cqe\_pool \* cqe\_pool

**Definition** rtio.h:448

[rtio::sq](structrtio.md#a34fbabfdbef3144f4520bf678684cdfb)

struct mpsc sq

**Definition** rtio.h:456

[rtio::cq\_count](structrtio.md#a358de1033ab4396d1f1baee2699c993f)

atomic\_t cq\_count

**Definition** rtio.h:437

[rtio::sqe\_pool](structrtio.md#a955f012bac623e7c037b5f1dba8e7fda)

struct rtio\_sqe\_pool \* sqe\_pool

**Definition** rtio.h:445

[rtio::xcqcnt](structrtio.md#ac45facdcc6d64cd70113b9b05b2fb086)

atomic\_t xcqcnt

**Definition** rtio.h:442

[rtio::cq](structrtio.md#ad6f44a354a170cb04a584beee7728fa9)

struct mpsc cq

**Definition** rtio.h:459

[atomic.h](sys_2atomic_8h.md)

[iterable\_sections.h](sys_2iterable__sections_8h.md)

[util.h](sys_2util_8h.md)

Misc utilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [rtio](dir_2c800b92938ab205b51fc9bd951bff11.md)
- [rtio.h](rtio_2rtio_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
