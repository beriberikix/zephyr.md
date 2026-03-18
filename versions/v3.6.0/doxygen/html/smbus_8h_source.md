---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/smbus_8h_source.html
original_path: doxygen/html/smbus_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

smbus.h

[Go to the documentation of this file.](smbus_8h.md)

1/\*

2 \* Copyright (c) 2022 Intel Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

11

12#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_SMBUS\_H\_

13#define ZEPHYR\_INCLUDE\_DRIVERS\_SMBUS\_H\_

14

21

22#include <[errno.h](errno_8h.md)>

23#include <[zephyr/sys/slist.h](slist_8h.md)>

24#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

25#include <[zephyr/device.h](device_8h.md)>

26

27#ifdef \_\_cplusplus

28extern "C" {

29#endif

30

37

[ 53](group__smbus__interface.md#ga7cf2e52d836b28041f9aeb7ac3c172e4)#define SMBUS\_CMD\_QUICK 0b000

54

[ 76](group__smbus__interface.md#gafa607ea7083ad73873716282e1f55c8e)#define SMBUS\_CMD\_BYTE 0b001

77

[ 102](group__smbus__interface.md#gabf5306ea95a2e8e5dc0270331218ea3d)#define SMBUS\_CMD\_BYTE\_DATA 0b010

103

[ 130](group__smbus__interface.md#ga70743c58b580018e567d2cb8595bea6f)#define SMBUS\_CMD\_WORD\_DATA 0b011

131

[ 149](group__smbus__interface.md#ga4400135f39814e328cf5e8ae11f27e3c)#define SMBUS\_CMD\_PROC\_CALL 0b100

150

[ 180](group__smbus__interface.md#gaa8d81258230e67e4f87b5908ab66b08d)#define SMBUS\_CMD\_BLOCK 0b101

181

[ 200](group__smbus__interface.md#ga9505b622875799e381c51f2df601c57a)#define SMBUS\_CMD\_BLOCK\_PROC 0b111

202

[ 204](group__smbus__interface.md#ga5ccde036931dc54e684ae5b955ff80d3)#define SMBUS\_BLOCK\_BYTES\_MAX 32

205

212

[ 214](group__smbus__interface.md#ga440a66ac32cf89d4a37782a0b51bda2c)#define SMBUS\_MODE\_CONTROLLER BIT(0)

215

[ 217](group__smbus__interface.md#ga6b9ddfb187688f3b1e1a3fdace9ecc76)#define SMBUS\_MODE\_PEC BIT(1)

218

[ 220](group__smbus__interface.md#ga0633fc1ff48d806b6ca0e408f29141fe)#define SMBUS\_MODE\_HOST\_NOTIFY BIT(2)

221

[ 223](group__smbus__interface.md#ga7675e48d824e97df4c07c0e2496bee3d)#define SMBUS\_MODE\_SMBALERT BIT(3)

224

226

233

[ 240](group__smbus__interface.md#ga1d282b18efccf83456acd14a8f4cd970)#define SMBUS\_ADDRESS\_ARA 0x0c

241

243

248

[ 250](group__smbus__interface.md#gad0c28687977d0a7866bdea87aef88016)enum [smbus\_direction](group__smbus__interface.md#gad0c28687977d0a7866bdea87aef88016) {

[ 252](group__smbus__interface.md#ggad0c28687977d0a7866bdea87aef88016a9c9dec19cbada732cef85784b0eedc54) [SMBUS\_MSG\_WRITE](group__smbus__interface.md#ggad0c28687977d0a7866bdea87aef88016a9c9dec19cbada732cef85784b0eedc54) = 0,

[ 254](group__smbus__interface.md#ggad0c28687977d0a7866bdea87aef88016aa87094fdacefac89c0b1a03be1c0d22f) [SMBUS\_MSG\_READ](group__smbus__interface.md#ggad0c28687977d0a7866bdea87aef88016aa87094fdacefac89c0b1a03be1c0d22f) = 1,

255};

256

258

260#define SMBUS\_MSG\_RW\_MASK BIT(0)

262

263struct [smbus\_callback](structsmbus__callback.md);

264

[ 272](group__smbus__interface.md#ga6d6ee9d29de5c0007d34328eb7c9f7c9)typedef void (\*[smbus\_callback\_handler\_t](group__smbus__interface.md#ga6d6ee9d29de5c0007d34328eb7c9f7c9))(const struct [device](structdevice.md) \*dev,

273 struct [smbus\_callback](structsmbus__callback.md) \*cb,

274 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [addr](structsmbus__callback.md#a707cc2c4cd2abf214343686d84cd1594));

275

[ 285](structsmbus__callback.md)struct [smbus\_callback](structsmbus__callback.md) {

[ 287](structsmbus__callback.md#a89fb6ad70aa53dba53aa85ebaea91f60) [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) [node](structsmbus__callback.md#a89fb6ad70aa53dba53aa85ebaea91f60);

288

[ 290](structsmbus__callback.md#a2017d57f8b1bbed10d37cb24a5212bc1) [smbus\_callback\_handler\_t](group__smbus__interface.md#ga6d6ee9d29de5c0007d34328eb7c9f7c9) [handler](structsmbus__callback.md#a2017d57f8b1bbed10d37cb24a5212bc1);

291

[ 293](structsmbus__callback.md#a707cc2c4cd2abf214343686d84cd1594) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [addr](structsmbus__callback.md#a707cc2c4cd2abf214343686d84cd1594);

294};

295

[ 299](structsmbus__dt__spec.md)struct [smbus\_dt\_spec](structsmbus__dt__spec.md) {

[ 301](structsmbus__dt__spec.md#a2b34afb2bc5d55382bc11e0a5ee72684) const struct [device](structdevice.md) \*[bus](structsmbus__dt__spec.md#a2b34afb2bc5d55382bc11e0a5ee72684);

[ 303](structsmbus__dt__spec.md#a0f6080e33e04405a42e9d29118512d08) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [addr](structsmbus__dt__spec.md#a0f6080e33e04405a42e9d29118512d08);

304};

305

[ 316](group__smbus__interface.md#gaf489d1b6c6aaaa1b3b1e9db823b24241)#define SMBUS\_DT\_SPEC\_GET(node\_id) \

317 { \

318 .bus = DEVICE\_DT\_GET(DT\_BUS(node\_id)), \

319 .addr = DT\_REG\_ADDR(node\_id) \

320 }

321

[ 330](group__smbus__interface.md#ga7e5bf5ecea7cbadf5d2a8b0c1e7a91af)#define SMBUS\_DT\_SPEC\_INST\_GET(inst) SMBUS\_DT\_SPEC\_GET(DT\_DRV\_INST(inst))

331

338

339typedef int (\*smbus\_api\_configure\_t)(const struct [device](structdevice.md) \*dev,

340 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) dev\_config);

341typedef int (\*smbus\_api\_get\_config\_t)(const struct [device](structdevice.md) \*dev,

342 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*dev\_config);

343typedef int (\*smbus\_api\_quick\_t)(const struct [device](structdevice.md) \*dev,

344 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, enum [smbus\_direction](group__smbus__interface.md#gad0c28687977d0a7866bdea87aef88016));

345typedef int (\*smbus\_api\_byte\_write\_t)(const struct [device](structdevice.md) \*dev,

346 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) byte);

347typedef int (\*smbus\_api\_byte\_read\_t)(const struct [device](structdevice.md) \*dev,

348 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*byte);

349typedef int (\*smbus\_api\_byte\_data\_write\_t)(const struct [device](structdevice.md) \*dev,

350 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615),

351 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) byte);

352typedef int (\*smbus\_api\_byte\_data\_read\_t)(const struct [device](structdevice.md) \*dev,

353 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615),

354 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*byte);

355typedef int (\*smbus\_api\_word\_data\_write\_t)(const struct [device](structdevice.md) \*dev,

356 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615),

357 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) word);

358typedef int (\*smbus\_api\_word\_data\_read\_t)(const struct [device](structdevice.md) \*dev,

359 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615),

360 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*word);

361typedef int (\*smbus\_api\_pcall\_t)(const struct [device](structdevice.md) \*dev,

362 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615),

363 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) send\_word, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*recv\_word);

364typedef int (\*smbus\_api\_block\_write\_t)(const struct [device](structdevice.md) \*dev,

365 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615),

366 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) count, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf);

367typedef int (\*smbus\_api\_block\_read\_t)(const struct [device](structdevice.md) \*dev,

368 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615),

369 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*count, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf);

370typedef int (\*smbus\_api\_block\_pcall\_t)(const struct [device](structdevice.md) \*dev,

371 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615),

372 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) send\_count, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*send\_buf,

373 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*recv\_count, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*recv\_buf);

374typedef int (\*smbus\_api\_smbalert\_cb\_t)(const struct [device](structdevice.md) \*dev,

375 struct [smbus\_callback](structsmbus__callback.md) \*cb);

376typedef int (\*smbus\_api\_host\_notify\_cb\_t)(const struct [device](structdevice.md) \*dev,

377 struct [smbus\_callback](structsmbus__callback.md) \*cb);

378

379\_\_subsystem struct smbus\_driver\_api {

380 smbus\_api\_configure\_t configure;

381 smbus\_api\_get\_config\_t get\_config;

382 smbus\_api\_quick\_t [smbus\_quick](group__smbus__interface.md#gab008499bca4a4096672d5909fa71b21d);

383 smbus\_api\_byte\_write\_t [smbus\_byte\_write](group__smbus__interface.md#ga7dd01c1e00a0f8b0315e442707332251);

384 smbus\_api\_byte\_read\_t [smbus\_byte\_read](group__smbus__interface.md#gadaef9dad3470a7e4d3360e0246271ca1);

385 smbus\_api\_byte\_data\_write\_t [smbus\_byte\_data\_write](group__smbus__interface.md#gadd7ec1eb3db981efceb8f959546a3b6a);

386 smbus\_api\_byte\_data\_read\_t [smbus\_byte\_data\_read](group__smbus__interface.md#ga1f1148a7cb92e0e0aef7ae3a84615c9b);

387 smbus\_api\_word\_data\_write\_t [smbus\_word\_data\_write](group__smbus__interface.md#gade05f9bbbba609832df91fe804dd5d3c);

388 smbus\_api\_word\_data\_read\_t [smbus\_word\_data\_read](group__smbus__interface.md#ga72a789110c7286a51c5cd5e2215abce1);

389 smbus\_api\_pcall\_t [smbus\_pcall](group__smbus__interface.md#ga2c1369835d3783bb5b5c3cb3711fec92);

390 smbus\_api\_block\_write\_t [smbus\_block\_write](group__smbus__interface.md#ga55a867cdcb504039f274abae2d1a99e4);

391 smbus\_api\_block\_read\_t [smbus\_block\_read](group__smbus__interface.md#ga67603db9b44636b0b62a24fd623cfb1c);

392 smbus\_api\_block\_pcall\_t [smbus\_block\_pcall](group__smbus__interface.md#ga680c3d713a615f4b62503d6f84de4290);

393 smbus\_api\_smbalert\_cb\_t [smbus\_smbalert\_set\_cb](group__smbus__interface.md#gadff533a6bc198815ee56d03a36b949e0);

394 smbus\_api\_smbalert\_cb\_t [smbus\_smbalert\_remove\_cb](group__smbus__interface.md#gac79105d8a76bf543394d666a16ae8bdd);

395 smbus\_api\_host\_notify\_cb\_t [smbus\_host\_notify\_set\_cb](group__smbus__interface.md#ga5054a6de634b015f54dacbe81427d0d2);

396 smbus\_api\_host\_notify\_cb\_t [smbus\_host\_notify\_remove\_cb](group__smbus__interface.md#gaa68f76bf02a13e0d45d05921cf3ca64d);

397};

398

402

403#if defined(CONFIG\_SMBUS\_STATS) || defined(\_\_DOXYGEN\_\_)

404

405#include <[zephyr/stats/stats.h](stats_2stats_8h.md)>

406

408

409[STATS\_SECT\_START](stats_2stats_8h.md#ae8e85c3ce2d901f4668d7237b19999fe)(smbus)

410[STATS\_SECT\_ENTRY32](stats_2stats_8h.md#a592329613cc77cfa5dee3e1d3b16dd93)(bytes\_read)

411[STATS\_SECT\_ENTRY32](stats_2stats_8h.md#a592329613cc77cfa5dee3e1d3b16dd93)(bytes\_written)

412[STATS\_SECT\_ENTRY32](stats_2stats_8h.md#a592329613cc77cfa5dee3e1d3b16dd93)(command\_count)

413[STATS\_SECT\_END](stats_2stats_8h.md#a4124f8c0a9ffb78d8be608a780676785);

414

415[STATS\_NAME\_START](stats_2stats_8h.md#abd76143ad82eea7aded01af8cb7bc9ae)(smbus)

416[STATS\_NAME](stats_2stats_8h.md#a30648b154e6da64aa39551fac123dd1b)(smbus, bytes\_read)

417[STATS\_NAME](stats_2stats_8h.md#a30648b154e6da64aa39551fac123dd1b)(smbus, bytes\_written)

418[STATS\_NAME](stats_2stats_8h.md#a30648b154e6da64aa39551fac123dd1b)(smbus, command\_count)

419[STATS\_NAME\_END](stats_2stats_8h.md#a0de61377bb7c254b68cb39a9b5105e4f)(smbus);

420

421struct smbus\_device\_state {

422 struct device\_state devstate;

423 struct stats\_smbus stats;

424};

425

429#define Z\_SMBUS\_DEVICE\_STATE\_DEFINE(node\_id, dev\_name) \

430 static struct smbus\_device\_state Z\_DEVICE\_STATE\_NAME(dev\_name) \

431 \_\_attribute\_\_((\_\_section\_\_(".z\_devstate")));

432

439#define Z\_SMBUS\_INIT\_FN(dev\_name, init\_fn) \

440 static inline int \

441 UTIL\_CAT(dev\_name, \_init)(const struct device \*dev) \

442 { \

443 struct smbus\_device\_state \*state = \

444 CONTAINER\_OF(dev->state, \

445 struct smbus\_device\_state, \

446 devstate); \

447 stats\_init(&state->stats.s\_hdr, STATS\_SIZE\_32, 4, \

448 STATS\_NAME\_INIT\_PARMS(smbus)); \

449 stats\_register(dev->name, &(state->stats.s\_hdr)); \

450 return init\_fn(dev); \

451 }

452

454

[ 463](group__smbus__interface.md#ga0a63b800c14f5831730372b9bad41864)static inline void [smbus\_xfer\_stats](group__smbus__interface.md#ga0a63b800c14f5831730372b9bad41864)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) sent,

464 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [recv](group__bsd__sockets.md#gae11da452beee536eac85d5f26e5cdd40))

465{

466 struct smbus\_device\_state \*[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90) =

467 [CONTAINER\_OF](group__sys-util.md#gac5bc561d1bfd1bf68877fe577779bd2f)(dev->[state](structdevice.md#abe18f600adc4ab760963928477cc944e), struct smbus\_device\_state, devstate);

468

469 [STATS\_INC](stats_2stats_8h.md#a725e1bf6b2c486de9603954974d6315a)([state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)->stats, command\_count);

470 [STATS\_INCN](stats_2stats_8h.md#ac5d5050e8684027a3efb5a8e7a830be6)([state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)->stats, bytes\_read, [recv](group__bsd__sockets.md#gae11da452beee536eac85d5f26e5cdd40));

471 [STATS\_INCN](stats_2stats_8h.md#ac5d5050e8684027a3efb5a8e7a830be6)([state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)->stats, bytes\_written, sent);

472}

473

[ 502](group__smbus__interface.md#gaab024b741eb2c126d41d6db6e76333ee)#define SMBUS\_DEVICE\_DT\_DEFINE(node\_id, init\_fn, pm\_device, \

503 data\_ptr, cfg\_ptr, level, prio, \

504 api\_ptr, ...) \

505 Z\_SMBUS\_DEVICE\_STATE\_DEFINE(node\_id, \

506 Z\_DEVICE\_DT\_DEV\_NAME(node\_id)); \

507 Z\_SMBUS\_INIT\_FN(Z\_DEVICE\_DT\_DEV\_NAME(node\_id), init\_fn) \

508 Z\_DEVICE\_DEFINE(node\_id, Z\_DEVICE\_DT\_DEV\_NAME(node\_id), \

509 DEVICE\_DT\_NAME(node\_id), \

510 &UTIL\_CAT(Z\_DEVICE\_DT\_DEV\_NAME(node\_id), \_init),\

511 pm\_device, \

512 data\_ptr, cfg\_ptr, level, prio, \

513 api\_ptr, \

514 &(Z\_DEVICE\_STATE\_NAME(Z\_DEVICE\_DT\_DEV\_NAME \

515 (node\_id)).devstate), \

516 \_\_VA\_ARGS\_\_)

517

518#else /\* CONFIG\_SMBUS\_STATS \*/

519

520static inline void [smbus\_xfer\_stats](group__smbus__interface.md#ga0a63b800c14f5831730372b9bad41864)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) sent,

521 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [recv](group__bsd__sockets.md#gae11da452beee536eac85d5f26e5cdd40))

522{

523 ARG\_UNUSED(dev);

524 ARG\_UNUSED(sent);

525 ARG\_UNUSED([recv](group__bsd__sockets.md#gae11da452beee536eac85d5f26e5cdd40));

526}

527

528#define SMBUS\_DEVICE\_DT\_DEFINE(node\_id, init\_fn, pm\_device, \

529 data\_ptr, cfg\_ptr, level, prio, \

530 api\_ptr, ...) \

531 DEVICE\_DT\_DEFINE(node\_id, &init\_fn, pm\_device, \

532 data\_ptr, cfg\_ptr, level, prio, \

533 api\_ptr, \_\_VA\_ARGS\_\_)

534

535#endif /\* CONFIG\_SMBUS\_STATS \*/

536

[ 546](group__smbus__interface.md#ga610bc9c96bb22741c850696127f16b92)#define SMBUS\_DEVICE\_DT\_INST\_DEFINE(inst, ...) \

547 SMBUS\_DEVICE\_DT\_DEFINE(DT\_DRV\_INST(inst), \_\_VA\_ARGS\_\_)

548

[ 559](group__smbus__interface.md#ga517305aa7cc9c93ae449b3c548d6c835)\_\_syscall int [smbus\_configure](group__smbus__interface.md#ga517305aa7cc9c93ae449b3c548d6c835)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) dev\_config);

560

561static inline int z\_impl\_smbus\_configure(const struct [device](structdevice.md) \*dev,

562 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) dev\_config)

563{

564 const struct smbus\_driver\_api \*api =

565 (const struct smbus\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

566

567 return api->configure(dev, dev\_config);

568}

569

[ 590](group__smbus__interface.md#ga9ca38ca95c0576bdc75b7eb8d0ca29ef)\_\_syscall int [smbus\_get\_config](group__smbus__interface.md#ga9ca38ca95c0576bdc75b7eb8d0ca29ef)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*dev\_config);

591

592static inline int z\_impl\_smbus\_get\_config(const struct [device](structdevice.md) \*dev,

593 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*dev\_config)

594{

595 const struct smbus\_driver\_api \*api =

596 (const struct smbus\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

597

598 if (api->get\_config == NULL) {

599 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

600 }

601

602 return api->get\_config(dev, dev\_config);

603}

604

[ 616](group__smbus__interface.md#gadff533a6bc198815ee56d03a36b949e0)static inline int [smbus\_smbalert\_set\_cb](group__smbus__interface.md#gadff533a6bc198815ee56d03a36b949e0)(const struct [device](structdevice.md) \*dev,

617 struct [smbus\_callback](structsmbus__callback.md) \*cb)

618{

619 const struct smbus\_driver\_api \*api =

620 (const struct smbus\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

621

622 if (api->smbus\_smbalert\_set\_cb == NULL) {

623 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

624 }

625

626 return api->smbus\_smbalert\_set\_cb(dev, cb);

627}

628

[ 640](group__smbus__interface.md#gac79105d8a76bf543394d666a16ae8bdd)\_\_syscall int [smbus\_smbalert\_remove\_cb](group__smbus__interface.md#gac79105d8a76bf543394d666a16ae8bdd)(const struct [device](structdevice.md) \*dev,

641 struct [smbus\_callback](structsmbus__callback.md) \*cb);

642

643static inline int z\_impl\_smbus\_smbalert\_remove\_cb(const struct [device](structdevice.md) \*dev,

644 struct [smbus\_callback](structsmbus__callback.md) \*cb)

645{

646 const struct smbus\_driver\_api \*api =

647 (const struct smbus\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

648

649 if (api->smbus\_smbalert\_remove\_cb == NULL) {

650 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

651 }

652

653 return api->smbus\_smbalert\_remove\_cb(dev, cb);

654}

655

[ 667](group__smbus__interface.md#ga5054a6de634b015f54dacbe81427d0d2)static inline int [smbus\_host\_notify\_set\_cb](group__smbus__interface.md#ga5054a6de634b015f54dacbe81427d0d2)(const struct [device](structdevice.md) \*dev,

668 struct [smbus\_callback](structsmbus__callback.md) \*cb)

669{

670 const struct smbus\_driver\_api \*api =

671 (const struct smbus\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

672

673 if (api->smbus\_host\_notify\_set\_cb == NULL) {

674 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

675 }

676

677 return api->smbus\_host\_notify\_set\_cb(dev, cb);

678}

679

[ 691](group__smbus__interface.md#gaa68f76bf02a13e0d45d05921cf3ca64d)\_\_syscall int [smbus\_host\_notify\_remove\_cb](group__smbus__interface.md#gaa68f76bf02a13e0d45d05921cf3ca64d)(const struct [device](structdevice.md) \*dev,

692 struct [smbus\_callback](structsmbus__callback.md) \*cb);

693

694static inline int z\_impl\_smbus\_host\_notify\_remove\_cb(const struct [device](structdevice.md) \*dev,

695 struct [smbus\_callback](structsmbus__callback.md) \*cb)

696{

697 const struct smbus\_driver\_api \*api =

698 (const struct smbus\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

699

700 if (api->smbus\_host\_notify\_remove\_cb == NULL) {

701 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

702 }

703

704 return api->smbus\_host\_notify\_remove\_cb(dev, cb);

705}

706

[ 723](group__smbus__interface.md#gab008499bca4a4096672d5909fa71b21d)\_\_syscall int [smbus\_quick](group__smbus__interface.md#gab008499bca4a4096672d5909fa71b21d)(const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr,

724 enum [smbus\_direction](group__smbus__interface.md#gad0c28687977d0a7866bdea87aef88016) direction);

725

726static inline int z\_impl\_smbus\_quick(const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr,

727 enum [smbus\_direction](group__smbus__interface.md#gad0c28687977d0a7866bdea87aef88016) direction)

728{

729 const struct smbus\_driver\_api \*api =

730 (const struct smbus\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

731

732 if (api->smbus\_quick == NULL) {

733 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

734 }

735

736 if (direction != [SMBUS\_MSG\_READ](group__smbus__interface.md#ggad0c28687977d0a7866bdea87aef88016aa87094fdacefac89c0b1a03be1c0d22f) && direction != [SMBUS\_MSG\_WRITE](group__smbus__interface.md#ggad0c28687977d0a7866bdea87aef88016a9c9dec19cbada732cef85784b0eedc54)) {

737 return -[EINVAL](group__system__errno.md#ga2d1678d5a7cc8ce499643f3b8957def4);

738 }

739

740 return api->smbus\_quick(dev, addr, direction);

741}

742

[ 758](group__smbus__interface.md#ga7dd01c1e00a0f8b0315e442707332251)\_\_syscall int [smbus\_byte\_write](group__smbus__interface.md#ga7dd01c1e00a0f8b0315e442707332251)(const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr,

759 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) byte);

760

761static inline int z\_impl\_smbus\_byte\_write(const struct [device](structdevice.md) \*dev,

762 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) byte)

763{

764 const struct smbus\_driver\_api \*api =

765 (const struct smbus\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

766

767 if (api->smbus\_byte\_write == NULL) {

768 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

769 }

770

771 return api->smbus\_byte\_write(dev, addr, byte);

772}

773

[ 789](group__smbus__interface.md#gadaef9dad3470a7e4d3360e0246271ca1)\_\_syscall int [smbus\_byte\_read](group__smbus__interface.md#gadaef9dad3470a7e4d3360e0246271ca1)(const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr,

790 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*byte);

791

792static inline int z\_impl\_smbus\_byte\_read(const struct [device](structdevice.md) \*dev,

793 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*byte)

794{

795 const struct smbus\_driver\_api \*api =

796 (const struct smbus\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

797

798 if (api->smbus\_byte\_read == NULL) {

799 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

800 }

801

802 return api->smbus\_byte\_read(dev, addr, byte);

803}

804

[ 821](group__smbus__interface.md#gadd7ec1eb3db981efceb8f959546a3b6a)\_\_syscall int [smbus\_byte\_data\_write](group__smbus__interface.md#gadd7ec1eb3db981efceb8f959546a3b6a)(const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr,

822 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615), [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) byte);

823

824static inline int z\_impl\_smbus\_byte\_data\_write(const struct [device](structdevice.md) \*dev,

825 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615),

826 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) byte)

827{

828 const struct smbus\_driver\_api \*api =

829 (const struct smbus\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

830

831 if (api->smbus\_byte\_data\_write == NULL) {

832 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

833 }

834

835 return api->smbus\_byte\_data\_write(dev, addr, [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615), byte);

836}

837

[ 854](group__smbus__interface.md#ga1f1148a7cb92e0e0aef7ae3a84615c9b)\_\_syscall int [smbus\_byte\_data\_read](group__smbus__interface.md#ga1f1148a7cb92e0e0aef7ae3a84615c9b)(const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr,

855 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615), [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*byte);

856

857static inline int z\_impl\_smbus\_byte\_data\_read(const struct [device](structdevice.md) \*dev,

858 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615),

859 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*byte)

860{

861 const struct smbus\_driver\_api \*api =

862 (const struct smbus\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

863

864 if (api->smbus\_byte\_data\_read == NULL) {

865 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

866 }

867

868 return api->smbus\_byte\_data\_read(dev, addr, [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615), byte);

869}

870

[ 887](group__smbus__interface.md#gade05f9bbbba609832df91fe804dd5d3c)\_\_syscall int [smbus\_word\_data\_write](group__smbus__interface.md#gade05f9bbbba609832df91fe804dd5d3c)(const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr,

888 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615), [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) word);

889

890static inline int z\_impl\_smbus\_word\_data\_write(const struct [device](structdevice.md) \*dev,

891 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615),

892 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) word)

893{

894 const struct smbus\_driver\_api \*api =

895 (const struct smbus\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

896

897 if (api->smbus\_word\_data\_write == NULL) {

898 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

899 }

900

901 return api->smbus\_word\_data\_write(dev, addr, [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615), word);

902}

903

[ 920](group__smbus__interface.md#ga72a789110c7286a51c5cd5e2215abce1)\_\_syscall int [smbus\_word\_data\_read](group__smbus__interface.md#ga72a789110c7286a51c5cd5e2215abce1)(const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr,

921 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615), [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*word);

922

923static inline int z\_impl\_smbus\_word\_data\_read(const struct [device](structdevice.md) \*dev,

924 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615),

925 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*word)

926{

927 const struct smbus\_driver\_api \*api =

928 (const struct smbus\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

929

930 if (api->smbus\_word\_data\_read == NULL) {

931 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

932 }

933

934 return api->smbus\_word\_data\_read(dev, addr, [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615), word);

935}

936

[ 955](group__smbus__interface.md#ga2c1369835d3783bb5b5c3cb3711fec92)\_\_syscall int [smbus\_pcall](group__smbus__interface.md#ga2c1369835d3783bb5b5c3cb3711fec92)(const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr,

956 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615), [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) send\_word, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*recv\_word);

957

958static inline int z\_impl\_smbus\_pcall(const struct [device](structdevice.md) \*dev,

959 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615),

960 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) send\_word, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*recv\_word)

961{

962 const struct smbus\_driver\_api \*api =

963 (const struct smbus\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

964

965 if (api->smbus\_pcall == NULL) {

966 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

967 }

968

969 return api->smbus\_pcall(dev, addr, [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615), send\_word, recv\_word);

970}

971

[ 989](group__smbus__interface.md#ga55a867cdcb504039f274abae2d1a99e4)\_\_syscall int [smbus\_block\_write](group__smbus__interface.md#ga55a867cdcb504039f274abae2d1a99e4)(const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr,

990 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615), [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) count, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf);

991

992static inline int z\_impl\_smbus\_block\_write(const struct [device](structdevice.md) \*dev,

993 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615),

994 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) count, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf)

995{

996 const struct smbus\_driver\_api \*api =

997 (const struct smbus\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

998

999 if (api->smbus\_block\_write == NULL) {

1000 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

1001 }

1002

1003 if (count < 1 || count > [SMBUS\_BLOCK\_BYTES\_MAX](group__smbus__interface.md#ga5ccde036931dc54e684ae5b955ff80d3)) {

1004 return -[EINVAL](group__system__errno.md#ga2d1678d5a7cc8ce499643f3b8957def4);

1005 }

1006

1007 return api->smbus\_block\_write(dev, addr, [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615), count, buf);

1008}

1009

[ 1027](group__smbus__interface.md#ga67603db9b44636b0b62a24fd623cfb1c)\_\_syscall int [smbus\_block\_read](group__smbus__interface.md#ga67603db9b44636b0b62a24fd623cfb1c)(const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr,

1028 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615), [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*count, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf);

1029

1030static inline int z\_impl\_smbus\_block\_read(const struct [device](structdevice.md) \*dev,

1031 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615),

1032 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*count, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf)

1033{

1034 const struct smbus\_driver\_api \*api =

1035 (const struct smbus\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

1036

1037 if (api->smbus\_block\_read == NULL) {

1038 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

1039 }

1040

1041 return api->smbus\_block\_read(dev, addr, [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615), count, buf);

1042}

1043

[ 1064](group__smbus__interface.md#ga680c3d713a615f4b62503d6f84de4290)\_\_syscall int [smbus\_block\_pcall](group__smbus__interface.md#ga680c3d713a615f4b62503d6f84de4290)(const struct [device](structdevice.md) \*dev,

1065 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615),

1066 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) snd\_count, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*snd\_buf,

1067 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*rcv\_count, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*rcv\_buf);

1068

1069static inline int z\_impl\_smbus\_block\_pcall(const struct [device](structdevice.md) \*dev,

1070 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615),

1071 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) snd\_count, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*snd\_buf,

1072 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*rcv\_count, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*rcv\_buf)

1073{

1074 const struct smbus\_driver\_api \*api =

1075 (const struct smbus\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

1076

1077 if (api->smbus\_block\_pcall == NULL) {

1078 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

1079 }

1080

1081 return api->smbus\_block\_pcall(dev, addr, [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615), snd\_count, snd\_buf,

1082 rcv\_count, rcv\_buf);

1083}

1084

1085#ifdef \_\_cplusplus

1086}

1087#endif

1088

1092

1093#include <syscalls/smbus.h>

1094

1095#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_SMBUS\_H\_ \*/

[device.h](device_8h.md)

[errno.h](errno_8h.md)

System error numbers.

[recv](group__bsd__sockets.md#gae11da452beee536eac85d5f26e5cdd40)

static ssize\_t recv(int sock, void \*buf, size\_t max\_len, int flags)

POSIX wrapper for zsock\_recv.

**Definition** socket.h:888

[cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615)

static void cmd(uint32\_t command)

Execute a display list command by co-processor engine.

**Definition** ft8xx\_reference\_api.h:153

[sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493)

struct \_snode sys\_snode\_t

Single-linked list node structure.

**Definition** slist.h:39

[smbus\_xfer\_stats](group__smbus__interface.md#ga0a63b800c14f5831730372b9bad41864)

static void smbus\_xfer\_stats(const struct device \*dev, uint8\_t sent, uint8\_t recv)

Updates the SMBus stats.

**Definition** smbus.h:463

[smbus\_byte\_data\_read](group__smbus__interface.md#ga1f1148a7cb92e0e0aef7ae3a84615c9b)

int smbus\_byte\_data\_read(const struct device \*dev, uint16\_t addr, uint8\_t cmd, uint8\_t \*byte)

Perform SMBus Byte Data Read operation.

[smbus\_pcall](group__smbus__interface.md#ga2c1369835d3783bb5b5c3cb3711fec92)

int smbus\_pcall(const struct device \*dev, uint16\_t addr, uint8\_t cmd, uint16\_t send\_word, uint16\_t \*recv\_word)

Perform SMBus Process Call operation.

[smbus\_host\_notify\_set\_cb](group__smbus__interface.md#ga5054a6de634b015f54dacbe81427d0d2)

static int smbus\_host\_notify\_set\_cb(const struct device \*dev, struct smbus\_callback \*cb)

Add Host Notify callback for a SMBus host controller.

**Definition** smbus.h:667

[smbus\_configure](group__smbus__interface.md#ga517305aa7cc9c93ae449b3c548d6c835)

int smbus\_configure(const struct device \*dev, uint32\_t dev\_config)

Configure operation of a SMBus host controller.

[smbus\_block\_write](group__smbus__interface.md#ga55a867cdcb504039f274abae2d1a99e4)

int smbus\_block\_write(const struct device \*dev, uint16\_t addr, uint8\_t cmd, uint8\_t count, uint8\_t \*buf)

Perform SMBus Block Write operation.

[SMBUS\_BLOCK\_BYTES\_MAX](group__smbus__interface.md#ga5ccde036931dc54e684ae5b955ff80d3)

#define SMBUS\_BLOCK\_BYTES\_MAX

Maximum number of bytes in SMBus Block protocol.

**Definition** smbus.h:204

[smbus\_block\_read](group__smbus__interface.md#ga67603db9b44636b0b62a24fd623cfb1c)

int smbus\_block\_read(const struct device \*dev, uint16\_t addr, uint8\_t cmd, uint8\_t \*count, uint8\_t \*buf)

Perform SMBus Block Read operation.

[smbus\_block\_pcall](group__smbus__interface.md#ga680c3d713a615f4b62503d6f84de4290)

int smbus\_block\_pcall(const struct device \*dev, uint16\_t addr, uint8\_t cmd, uint8\_t snd\_count, uint8\_t \*snd\_buf, uint8\_t \*rcv\_count, uint8\_t \*rcv\_buf)

Perform SMBus Block Process Call operation.

[smbus\_callback\_handler\_t](group__smbus__interface.md#ga6d6ee9d29de5c0007d34328eb7c9f7c9)

void(\* smbus\_callback\_handler\_t)(const struct device \*dev, struct smbus\_callback \*cb, uint8\_t addr)

Define SMBus callback handler function signature.

**Definition** smbus.h:272

[smbus\_word\_data\_read](group__smbus__interface.md#ga72a789110c7286a51c5cd5e2215abce1)

int smbus\_word\_data\_read(const struct device \*dev, uint16\_t addr, uint8\_t cmd, uint16\_t \*word)

Perform SMBus Word Data Read operation.

[smbus\_byte\_write](group__smbus__interface.md#ga7dd01c1e00a0f8b0315e442707332251)

int smbus\_byte\_write(const struct device \*dev, uint16\_t addr, uint8\_t byte)

Perform SMBus Byte Write operation.

[smbus\_get\_config](group__smbus__interface.md#ga9ca38ca95c0576bdc75b7eb8d0ca29ef)

int smbus\_get\_config(const struct device \*dev, uint32\_t \*dev\_config)

Get configuration of a SMBus host controller.

[smbus\_host\_notify\_remove\_cb](group__smbus__interface.md#gaa68f76bf02a13e0d45d05921cf3ca64d)

int smbus\_host\_notify\_remove\_cb(const struct device \*dev, struct smbus\_callback \*cb)

Remove Host Notify callback from a SMBus host controller.

[smbus\_quick](group__smbus__interface.md#gab008499bca4a4096672d5909fa71b21d)

int smbus\_quick(const struct device \*dev, uint16\_t addr, enum smbus\_direction direction)

Perform SMBus Quick operation.

[smbus\_smbalert\_remove\_cb](group__smbus__interface.md#gac79105d8a76bf543394d666a16ae8bdd)

int smbus\_smbalert\_remove\_cb(const struct device \*dev, struct smbus\_callback \*cb)

Remove SMBUSALERT callback from a SMBus host controller.

[smbus\_direction](group__smbus__interface.md#gad0c28687977d0a7866bdea87aef88016)

smbus\_direction

SMBus read / write direction.

**Definition** smbus.h:250

[smbus\_byte\_read](group__smbus__interface.md#gadaef9dad3470a7e4d3360e0246271ca1)

int smbus\_byte\_read(const struct device \*dev, uint16\_t addr, uint8\_t \*byte)

Perform SMBus Byte Read operation.

[smbus\_byte\_data\_write](group__smbus__interface.md#gadd7ec1eb3db981efceb8f959546a3b6a)

int smbus\_byte\_data\_write(const struct device \*dev, uint16\_t addr, uint8\_t cmd, uint8\_t byte)

Perform SMBus Byte Data Write operation.

[smbus\_word\_data\_write](group__smbus__interface.md#gade05f9bbbba609832df91fe804dd5d3c)

int smbus\_word\_data\_write(const struct device \*dev, uint16\_t addr, uint8\_t cmd, uint16\_t word)

Perform SMBus Word Data Write operation.

[smbus\_smbalert\_set\_cb](group__smbus__interface.md#gadff533a6bc198815ee56d03a36b949e0)

static int smbus\_smbalert\_set\_cb(const struct device \*dev, struct smbus\_callback \*cb)

Add SMBUSALERT callback for a SMBus host controller.

**Definition** smbus.h:616

[SMBUS\_MSG\_WRITE](group__smbus__interface.md#ggad0c28687977d0a7866bdea87aef88016a9c9dec19cbada732cef85784b0eedc54)

@ SMBUS\_MSG\_WRITE

Write a message to SMBus peripheral.

**Definition** smbus.h:252

[SMBUS\_MSG\_READ](group__smbus__interface.md#ggad0c28687977d0a7866bdea87aef88016aa87094fdacefac89c0b1a03be1c0d22f)

@ SMBUS\_MSG\_READ

Read a message from SMBus peripheral.

**Definition** smbus.h:254

[CONTAINER\_OF](group__sys-util.md#gac5bc561d1bfd1bf68877fe577779bd2f)

#define CONTAINER\_OF(ptr, type, field)

Get a pointer to a structure containing the element.

**Definition** util.h:265

[EINVAL](group__system__errno.md#ga2d1678d5a7cc8ce499643f3b8957def4)

#define EINVAL

Invalid argument.

**Definition** errno.h:61

[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b)

#define ENOSYS

Function not implemented.

**Definition** errno.h:83

[types.h](include_2zephyr_2types_8h.md)

[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)

state

**Definition** parser\_state.h:29

[slist.h](slist_8h.md)

[stats.h](stats_2stats_8h.md)

Statistics.

[STATS\_NAME\_END](stats_2stats_8h.md#a0de61377bb7c254b68cb39a9b5105e4f)

#define STATS\_NAME\_END(name\_\_)

**Definition** stats.h:391

[STATS\_NAME](stats_2stats_8h.md#a30648b154e6da64aa39551fac123dd1b)

#define STATS\_NAME(name\_\_, entry\_\_)

**Definition** stats.h:390

[STATS\_SECT\_END](stats_2stats_8h.md#a4124f8c0a9ffb78d8be608a780676785)

#define STATS\_SECT\_END

Ends a stats group struct definition.

**Definition** stats.h:89

[STATS\_SECT\_ENTRY32](stats_2stats_8h.md#a592329613cc77cfa5dee3e1d3b16dd93)

#define STATS\_SECT\_ENTRY32(var\_\_)

**Definition** stats.h:359

[STATS\_INC](stats_2stats_8h.md#a725e1bf6b2c486de9603954974d6315a)

#define STATS\_INC(group\_\_, var\_\_)

**Definition** stats.h:364

[STATS\_NAME\_START](stats_2stats_8h.md#abd76143ad82eea7aded01af8cb7bc9ae)

#define STATS\_NAME\_START(name\_\_)

**Definition** stats.h:389

[STATS\_INCN](stats_2stats_8h.md#ac5d5050e8684027a3efb5a8e7a830be6)

#define STATS\_INCN(group\_\_, var\_\_, n\_\_)

**Definition** stats.h:363

[STATS\_SECT\_START](stats_2stats_8h.md#ae8e85c3ce2d901f4668d7237b19999fe)

#define STATS\_SECT\_START(group\_\_)

**Definition** stats.h:354

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:387

[device::api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d)

const void \* api

Address of the API structure exposed by the device instance.

**Definition** device.h:393

[device::state](structdevice.md#abe18f600adc4ab760963928477cc944e)

struct device\_state \* state

Address of the common device state.

**Definition** device.h:395

[smbus\_callback](structsmbus__callback.md)

SMBus callback structure.

**Definition** smbus.h:285

[smbus\_callback::handler](structsmbus__callback.md#a2017d57f8b1bbed10d37cb24a5212bc1)

smbus\_callback\_handler\_t handler

Actual callback function being called when relevant.

**Definition** smbus.h:290

[smbus\_callback::addr](structsmbus__callback.md#a707cc2c4cd2abf214343686d84cd1594)

uint8\_t addr

Peripheral device address.

**Definition** smbus.h:293

[smbus\_callback::node](structsmbus__callback.md#a89fb6ad70aa53dba53aa85ebaea91f60)

sys\_snode\_t node

This should be used in driver for a callback list management.

**Definition** smbus.h:287

[smbus\_dt\_spec](structsmbus__dt__spec.md)

Complete SMBus DT information.

**Definition** smbus.h:299

[smbus\_dt\_spec::addr](structsmbus__dt__spec.md#a0f6080e33e04405a42e9d29118512d08)

uint16\_t addr

Address of the SMBus peripheral device.

**Definition** smbus.h:303

[smbus\_dt\_spec::bus](structsmbus__dt__spec.md#a2b34afb2bc5d55382bc11e0a5ee72684)

const struct device \* bus

SMBus bus.

**Definition** smbus.h:301

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [smbus.h](smbus_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
