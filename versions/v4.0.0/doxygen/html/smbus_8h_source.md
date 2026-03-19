---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/smbus_8h_source.html
original_path: doxygen/html/smbus_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
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

23

24#include <[errno.h](errno_8h.md)>

25#include <[zephyr/sys/slist.h](slist_8h.md)>

26#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

27#include <[zephyr/device.h](device_8h.md)>

28

29#ifdef \_\_cplusplus

30extern "C" {

31#endif

32

39

[ 55](group__smbus__interface.md#ga7cf2e52d836b28041f9aeb7ac3c172e4)#define SMBUS\_CMD\_QUICK 0b000

56

[ 78](group__smbus__interface.md#gafa607ea7083ad73873716282e1f55c8e)#define SMBUS\_CMD\_BYTE 0b001

79

[ 104](group__smbus__interface.md#gabf5306ea95a2e8e5dc0270331218ea3d)#define SMBUS\_CMD\_BYTE\_DATA 0b010

105

[ 132](group__smbus__interface.md#ga70743c58b580018e567d2cb8595bea6f)#define SMBUS\_CMD\_WORD\_DATA 0b011

133

[ 151](group__smbus__interface.md#ga4400135f39814e328cf5e8ae11f27e3c)#define SMBUS\_CMD\_PROC\_CALL 0b100

152

[ 182](group__smbus__interface.md#gaa8d81258230e67e4f87b5908ab66b08d)#define SMBUS\_CMD\_BLOCK 0b101

183

[ 202](group__smbus__interface.md#ga9505b622875799e381c51f2df601c57a)#define SMBUS\_CMD\_BLOCK\_PROC 0b111

204

[ 206](group__smbus__interface.md#ga5ccde036931dc54e684ae5b955ff80d3)#define SMBUS\_BLOCK\_BYTES\_MAX 32

207

214

[ 216](group__smbus__interface.md#ga440a66ac32cf89d4a37782a0b51bda2c)#define SMBUS\_MODE\_CONTROLLER BIT(0)

217

[ 219](group__smbus__interface.md#ga6b9ddfb187688f3b1e1a3fdace9ecc76)#define SMBUS\_MODE\_PEC BIT(1)

220

[ 222](group__smbus__interface.md#ga0633fc1ff48d806b6ca0e408f29141fe)#define SMBUS\_MODE\_HOST\_NOTIFY BIT(2)

223

[ 225](group__smbus__interface.md#ga7675e48d824e97df4c07c0e2496bee3d)#define SMBUS\_MODE\_SMBALERT BIT(3)

226

228

235

[ 242](group__smbus__interface.md#ga1d282b18efccf83456acd14a8f4cd970)#define SMBUS\_ADDRESS\_ARA 0x0c

243

245

250

[ 252](group__smbus__interface.md#gad0c28687977d0a7866bdea87aef88016)enum [smbus\_direction](group__smbus__interface.md#gad0c28687977d0a7866bdea87aef88016) {

[ 254](group__smbus__interface.md#ggad0c28687977d0a7866bdea87aef88016a9c9dec19cbada732cef85784b0eedc54) [SMBUS\_MSG\_WRITE](group__smbus__interface.md#ggad0c28687977d0a7866bdea87aef88016a9c9dec19cbada732cef85784b0eedc54) = 0,

[ 256](group__smbus__interface.md#ggad0c28687977d0a7866bdea87aef88016aa87094fdacefac89c0b1a03be1c0d22f) [SMBUS\_MSG\_READ](group__smbus__interface.md#ggad0c28687977d0a7866bdea87aef88016aa87094fdacefac89c0b1a03be1c0d22f) = 1,

257};

258

260

262#define SMBUS\_MSG\_RW\_MASK BIT(0)

264

265struct [smbus\_callback](structsmbus__callback.md);

266

[ 274](group__smbus__interface.md#ga6d6ee9d29de5c0007d34328eb7c9f7c9)typedef void (\*[smbus\_callback\_handler\_t](group__smbus__interface.md#ga6d6ee9d29de5c0007d34328eb7c9f7c9))(const struct [device](structdevice.md) \*dev,

275 struct [smbus\_callback](structsmbus__callback.md) \*cb,

276 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [addr](structsmbus__callback.md#a707cc2c4cd2abf214343686d84cd1594));

277

[ 287](structsmbus__callback.md)struct [smbus\_callback](structsmbus__callback.md) {

[ 289](structsmbus__callback.md#a89fb6ad70aa53dba53aa85ebaea91f60) [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) [node](structsmbus__callback.md#a89fb6ad70aa53dba53aa85ebaea91f60);

290

[ 292](structsmbus__callback.md#a2017d57f8b1bbed10d37cb24a5212bc1) [smbus\_callback\_handler\_t](group__smbus__interface.md#ga6d6ee9d29de5c0007d34328eb7c9f7c9) [handler](structsmbus__callback.md#a2017d57f8b1bbed10d37cb24a5212bc1);

293

[ 295](structsmbus__callback.md#a707cc2c4cd2abf214343686d84cd1594) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [addr](structsmbus__callback.md#a707cc2c4cd2abf214343686d84cd1594);

296};

297

[ 301](structsmbus__dt__spec.md)struct [smbus\_dt\_spec](structsmbus__dt__spec.md) {

[ 303](structsmbus__dt__spec.md#a2b34afb2bc5d55382bc11e0a5ee72684) const struct [device](structdevice.md) \*[bus](structsmbus__dt__spec.md#a2b34afb2bc5d55382bc11e0a5ee72684);

[ 305](structsmbus__dt__spec.md#a0f6080e33e04405a42e9d29118512d08) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [addr](structsmbus__dt__spec.md#a0f6080e33e04405a42e9d29118512d08);

306};

307

[ 318](group__smbus__interface.md#gaf489d1b6c6aaaa1b3b1e9db823b24241)#define SMBUS\_DT\_SPEC\_GET(node\_id) \

319 { \

320 .bus = DEVICE\_DT\_GET(DT\_BUS(node\_id)), \

321 .addr = DT\_REG\_ADDR(node\_id) \

322 }

323

[ 332](group__smbus__interface.md#ga7e5bf5ecea7cbadf5d2a8b0c1e7a91af)#define SMBUS\_DT\_SPEC\_INST\_GET(inst) SMBUS\_DT\_SPEC\_GET(DT\_DRV\_INST(inst))

333

340

341typedef int (\*smbus\_api\_configure\_t)(const struct [device](structdevice.md) \*dev,

342 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) dev\_config);

343typedef int (\*smbus\_api\_get\_config\_t)(const struct [device](structdevice.md) \*dev,

344 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*dev\_config);

345typedef int (\*smbus\_api\_quick\_t)(const struct [device](structdevice.md) \*dev,

346 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, enum [smbus\_direction](group__smbus__interface.md#gad0c28687977d0a7866bdea87aef88016));

347typedef int (\*smbus\_api\_byte\_write\_t)(const struct [device](structdevice.md) \*dev,

348 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) byte);

349typedef int (\*smbus\_api\_byte\_read\_t)(const struct [device](structdevice.md) \*dev,

350 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*byte);

351typedef int (\*smbus\_api\_byte\_data\_write\_t)(const struct [device](structdevice.md) \*dev,

352 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615),

353 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) byte);

354typedef int (\*smbus\_api\_byte\_data\_read\_t)(const struct [device](structdevice.md) \*dev,

355 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615),

356 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*byte);

357typedef int (\*smbus\_api\_word\_data\_write\_t)(const struct [device](structdevice.md) \*dev,

358 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615),

359 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) word);

360typedef int (\*smbus\_api\_word\_data\_read\_t)(const struct [device](structdevice.md) \*dev,

361 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615),

362 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*word);

363typedef int (\*smbus\_api\_pcall\_t)(const struct [device](structdevice.md) \*dev,

364 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615),

365 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) send\_word, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*recv\_word);

366typedef int (\*smbus\_api\_block\_write\_t)(const struct [device](structdevice.md) \*dev,

367 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615),

368 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) count, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf);

369typedef int (\*smbus\_api\_block\_read\_t)(const struct [device](structdevice.md) \*dev,

370 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615),

371 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*count, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf);

372typedef int (\*smbus\_api\_block\_pcall\_t)(const struct [device](structdevice.md) \*dev,

373 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615),

374 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) send\_count, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*send\_buf,

375 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*recv\_count, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*recv\_buf);

376typedef int (\*smbus\_api\_smbalert\_cb\_t)(const struct [device](structdevice.md) \*dev,

377 struct [smbus\_callback](structsmbus__callback.md) \*cb);

378typedef int (\*smbus\_api\_host\_notify\_cb\_t)(const struct [device](structdevice.md) \*dev,

379 struct [smbus\_callback](structsmbus__callback.md) \*cb);

380

381\_\_subsystem struct smbus\_driver\_api {

382 smbus\_api\_configure\_t configure;

383 smbus\_api\_get\_config\_t get\_config;

384 smbus\_api\_quick\_t [smbus\_quick](group__smbus__interface.md#gab008499bca4a4096672d5909fa71b21d);

385 smbus\_api\_byte\_write\_t [smbus\_byte\_write](group__smbus__interface.md#ga7dd01c1e00a0f8b0315e442707332251);

386 smbus\_api\_byte\_read\_t [smbus\_byte\_read](group__smbus__interface.md#gadaef9dad3470a7e4d3360e0246271ca1);

387 smbus\_api\_byte\_data\_write\_t [smbus\_byte\_data\_write](group__smbus__interface.md#gadd7ec1eb3db981efceb8f959546a3b6a);

388 smbus\_api\_byte\_data\_read\_t [smbus\_byte\_data\_read](group__smbus__interface.md#ga1f1148a7cb92e0e0aef7ae3a84615c9b);

389 smbus\_api\_word\_data\_write\_t [smbus\_word\_data\_write](group__smbus__interface.md#gade05f9bbbba609832df91fe804dd5d3c);

390 smbus\_api\_word\_data\_read\_t [smbus\_word\_data\_read](group__smbus__interface.md#ga72a789110c7286a51c5cd5e2215abce1);

391 smbus\_api\_pcall\_t [smbus\_pcall](group__smbus__interface.md#ga2c1369835d3783bb5b5c3cb3711fec92);

392 smbus\_api\_block\_write\_t [smbus\_block\_write](group__smbus__interface.md#ga55a867cdcb504039f274abae2d1a99e4);

393 smbus\_api\_block\_read\_t [smbus\_block\_read](group__smbus__interface.md#ga67603db9b44636b0b62a24fd623cfb1c);

394 smbus\_api\_block\_pcall\_t [smbus\_block\_pcall](group__smbus__interface.md#ga680c3d713a615f4b62503d6f84de4290);

395 smbus\_api\_smbalert\_cb\_t [smbus\_smbalert\_set\_cb](group__smbus__interface.md#gadff533a6bc198815ee56d03a36b949e0);

396 smbus\_api\_smbalert\_cb\_t [smbus\_smbalert\_remove\_cb](group__smbus__interface.md#gac79105d8a76bf543394d666a16ae8bdd);

397 smbus\_api\_host\_notify\_cb\_t [smbus\_host\_notify\_set\_cb](group__smbus__interface.md#ga5054a6de634b015f54dacbe81427d0d2);

398 smbus\_api\_host\_notify\_cb\_t [smbus\_host\_notify\_remove\_cb](group__smbus__interface.md#gaa68f76bf02a13e0d45d05921cf3ca64d);

399};

400

404

405#if defined(CONFIG\_SMBUS\_STATS) || defined(\_\_DOXYGEN\_\_)

406

407#include <[zephyr/stats/stats.h](stats_2stats_8h.md)>

408

410

411[STATS\_SECT\_START](stats_2stats_8h.md#ae8e85c3ce2d901f4668d7237b19999fe)(smbus)

412[STATS\_SECT\_ENTRY32](stats_2stats_8h.md#a592329613cc77cfa5dee3e1d3b16dd93)(bytes\_read)

413[STATS\_SECT\_ENTRY32](stats_2stats_8h.md#a592329613cc77cfa5dee3e1d3b16dd93)(bytes\_written)

414[STATS\_SECT\_ENTRY32](stats_2stats_8h.md#a592329613cc77cfa5dee3e1d3b16dd93)(command\_count)

415[STATS\_SECT\_END](stats_2stats_8h.md#a4124f8c0a9ffb78d8be608a780676785);

416

417[STATS\_NAME\_START](stats_2stats_8h.md#abd76143ad82eea7aded01af8cb7bc9ae)(smbus)

418[STATS\_NAME](stats_2stats_8h.md#a30648b154e6da64aa39551fac123dd1b)(smbus, bytes\_read)

419[STATS\_NAME](stats_2stats_8h.md#a30648b154e6da64aa39551fac123dd1b)(smbus, bytes\_written)

420[STATS\_NAME](stats_2stats_8h.md#a30648b154e6da64aa39551fac123dd1b)(smbus, command\_count)

421[STATS\_NAME\_END](stats_2stats_8h.md#a0de61377bb7c254b68cb39a9b5105e4f)(smbus);

422

423struct smbus\_device\_state {

424 struct device\_state devstate;

425 struct stats\_smbus stats;

426};

427

431#define Z\_SMBUS\_DEVICE\_STATE\_DEFINE(node\_id, dev\_name) \

432 static struct smbus\_device\_state Z\_DEVICE\_STATE\_NAME(dev\_name) \

433 \_\_attribute\_\_((\_\_section\_\_(".z\_devstate")));

434

441#define Z\_SMBUS\_INIT\_FN(dev\_name, init\_fn) \

442 static inline int \

443 UTIL\_CAT(dev\_name, \_init)(const struct device \*dev) \

444 { \

445 struct smbus\_device\_state \*state = \

446 CONTAINER\_OF(dev->state, \

447 struct smbus\_device\_state, \

448 devstate); \

449 stats\_init(&state->stats.s\_hdr, STATS\_SIZE\_32, 4, \

450 STATS\_NAME\_INIT\_PARMS(smbus)); \

451 stats\_register(dev->name, &(state->stats.s\_hdr)); \

452 return init\_fn(dev); \

453 }

454

456

[ 465](group__smbus__interface.md#ga0a63b800c14f5831730372b9bad41864)static inline void [smbus\_xfer\_stats](group__smbus__interface.md#ga0a63b800c14f5831730372b9bad41864)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) sent,

466 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [recv](group__bsd__sockets.md#gae11da452beee536eac85d5f26e5cdd40))

467{

468 struct smbus\_device\_state \*[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90) =

469 [CONTAINER\_OF](group__sys-util.md#gac5bc561d1bfd1bf68877fe577779bd2f)(dev->[state](structdevice.md#abe18f600adc4ab760963928477cc944e), struct smbus\_device\_state, devstate);

470

471 [STATS\_INC](stats_2stats_8h.md#a725e1bf6b2c486de9603954974d6315a)([state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)->stats, command\_count);

472 [STATS\_INCN](stats_2stats_8h.md#ac5d5050e8684027a3efb5a8e7a830be6)([state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)->stats, bytes\_read, [recv](group__bsd__sockets.md#gae11da452beee536eac85d5f26e5cdd40));

473 [STATS\_INCN](stats_2stats_8h.md#ac5d5050e8684027a3efb5a8e7a830be6)([state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)->stats, bytes\_written, sent);

474}

475

[ 504](group__smbus__interface.md#gaab024b741eb2c126d41d6db6e76333ee)#define SMBUS\_DEVICE\_DT\_DEFINE(node\_id, init\_fn, pm\_device, \

505 data\_ptr, cfg\_ptr, level, prio, \

506 api\_ptr, ...) \

507 Z\_SMBUS\_DEVICE\_STATE\_DEFINE(node\_id, \

508 Z\_DEVICE\_DT\_DEV\_NAME(node\_id)); \

509 Z\_SMBUS\_INIT\_FN(Z\_DEVICE\_DT\_DEV\_NAME(node\_id), init\_fn) \

510 Z\_DEVICE\_DEFINE(node\_id, Z\_DEVICE\_DT\_DEV\_NAME(node\_id), \

511 DEVICE\_DT\_NAME(node\_id), \

512 &UTIL\_CAT(Z\_DEVICE\_DT\_DEV\_NAME(node\_id), \_init),\

513 pm\_device, \

514 data\_ptr, cfg\_ptr, level, prio, \

515 api\_ptr, \

516 &(Z\_DEVICE\_STATE\_NAME(Z\_DEVICE\_DT\_DEV\_NAME \

517 (node\_id)).devstate), \

518 \_\_VA\_ARGS\_\_)

519

520#else /\* CONFIG\_SMBUS\_STATS \*/

521

522static inline void [smbus\_xfer\_stats](group__smbus__interface.md#ga0a63b800c14f5831730372b9bad41864)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) sent,

523 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [recv](group__bsd__sockets.md#gae11da452beee536eac85d5f26e5cdd40))

524{

525 ARG\_UNUSED(dev);

526 ARG\_UNUSED(sent);

527 ARG\_UNUSED([recv](group__bsd__sockets.md#gae11da452beee536eac85d5f26e5cdd40));

528}

529

530#define SMBUS\_DEVICE\_DT\_DEFINE(node\_id, init\_fn, pm\_device, \

531 data\_ptr, cfg\_ptr, level, prio, \

532 api\_ptr, ...) \

533 DEVICE\_DT\_DEFINE(node\_id, &init\_fn, pm\_device, \

534 data\_ptr, cfg\_ptr, level, prio, \

535 api\_ptr, \_\_VA\_ARGS\_\_)

536

537#endif /\* CONFIG\_SMBUS\_STATS \*/

538

[ 548](group__smbus__interface.md#ga610bc9c96bb22741c850696127f16b92)#define SMBUS\_DEVICE\_DT\_INST\_DEFINE(inst, ...) \

549 SMBUS\_DEVICE\_DT\_DEFINE(DT\_DRV\_INST(inst), \_\_VA\_ARGS\_\_)

550

[ 561](group__smbus__interface.md#ga517305aa7cc9c93ae449b3c548d6c835)\_\_syscall int [smbus\_configure](group__smbus__interface.md#ga517305aa7cc9c93ae449b3c548d6c835)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) dev\_config);

562

563static inline int z\_impl\_smbus\_configure(const struct [device](structdevice.md) \*dev,

564 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) dev\_config)

565{

566 const struct smbus\_driver\_api \*api =

567 (const struct smbus\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

568

569 return api->configure(dev, dev\_config);

570}

571

[ 592](group__smbus__interface.md#ga9ca38ca95c0576bdc75b7eb8d0ca29ef)\_\_syscall int [smbus\_get\_config](group__smbus__interface.md#ga9ca38ca95c0576bdc75b7eb8d0ca29ef)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*dev\_config);

593

594static inline int z\_impl\_smbus\_get\_config(const struct [device](structdevice.md) \*dev,

595 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*dev\_config)

596{

597 const struct smbus\_driver\_api \*api =

598 (const struct smbus\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

599

600 if (api->get\_config == NULL) {

601 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

602 }

603

604 return api->get\_config(dev, dev\_config);

605}

606

[ 618](group__smbus__interface.md#gadff533a6bc198815ee56d03a36b949e0)static inline int [smbus\_smbalert\_set\_cb](group__smbus__interface.md#gadff533a6bc198815ee56d03a36b949e0)(const struct [device](structdevice.md) \*dev,

619 struct [smbus\_callback](structsmbus__callback.md) \*cb)

620{

621 const struct smbus\_driver\_api \*api =

622 (const struct smbus\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

623

624 if (api->smbus\_smbalert\_set\_cb == NULL) {

625 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

626 }

627

628 return api->smbus\_smbalert\_set\_cb(dev, cb);

629}

630

[ 642](group__smbus__interface.md#gac79105d8a76bf543394d666a16ae8bdd)\_\_syscall int [smbus\_smbalert\_remove\_cb](group__smbus__interface.md#gac79105d8a76bf543394d666a16ae8bdd)(const struct [device](structdevice.md) \*dev,

643 struct [smbus\_callback](structsmbus__callback.md) \*cb);

644

645static inline int z\_impl\_smbus\_smbalert\_remove\_cb(const struct [device](structdevice.md) \*dev,

646 struct [smbus\_callback](structsmbus__callback.md) \*cb)

647{

648 const struct smbus\_driver\_api \*api =

649 (const struct smbus\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

650

651 if (api->smbus\_smbalert\_remove\_cb == NULL) {

652 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

653 }

654

655 return api->smbus\_smbalert\_remove\_cb(dev, cb);

656}

657

[ 669](group__smbus__interface.md#ga5054a6de634b015f54dacbe81427d0d2)static inline int [smbus\_host\_notify\_set\_cb](group__smbus__interface.md#ga5054a6de634b015f54dacbe81427d0d2)(const struct [device](structdevice.md) \*dev,

670 struct [smbus\_callback](structsmbus__callback.md) \*cb)

671{

672 const struct smbus\_driver\_api \*api =

673 (const struct smbus\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

674

675 if (api->smbus\_host\_notify\_set\_cb == NULL) {

676 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

677 }

678

679 return api->smbus\_host\_notify\_set\_cb(dev, cb);

680}

681

[ 693](group__smbus__interface.md#gaa68f76bf02a13e0d45d05921cf3ca64d)\_\_syscall int [smbus\_host\_notify\_remove\_cb](group__smbus__interface.md#gaa68f76bf02a13e0d45d05921cf3ca64d)(const struct [device](structdevice.md) \*dev,

694 struct [smbus\_callback](structsmbus__callback.md) \*cb);

695

696static inline int z\_impl\_smbus\_host\_notify\_remove\_cb(const struct [device](structdevice.md) \*dev,

697 struct [smbus\_callback](structsmbus__callback.md) \*cb)

698{

699 const struct smbus\_driver\_api \*api =

700 (const struct smbus\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

701

702 if (api->smbus\_host\_notify\_remove\_cb == NULL) {

703 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

704 }

705

706 return api->smbus\_host\_notify\_remove\_cb(dev, cb);

707}

708

[ 725](group__smbus__interface.md#gab008499bca4a4096672d5909fa71b21d)\_\_syscall int [smbus\_quick](group__smbus__interface.md#gab008499bca4a4096672d5909fa71b21d)(const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr,

726 enum [smbus\_direction](group__smbus__interface.md#gad0c28687977d0a7866bdea87aef88016) direction);

727

728static inline int z\_impl\_smbus\_quick(const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr,

729 enum [smbus\_direction](group__smbus__interface.md#gad0c28687977d0a7866bdea87aef88016) direction)

730{

731 const struct smbus\_driver\_api \*api =

732 (const struct smbus\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

733

734 if (api->smbus\_quick == NULL) {

735 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

736 }

737

738 if (direction != [SMBUS\_MSG\_READ](group__smbus__interface.md#ggad0c28687977d0a7866bdea87aef88016aa87094fdacefac89c0b1a03be1c0d22f) && direction != [SMBUS\_MSG\_WRITE](group__smbus__interface.md#ggad0c28687977d0a7866bdea87aef88016a9c9dec19cbada732cef85784b0eedc54)) {

739 return -[EINVAL](group__system__errno.md#ga2d1678d5a7cc8ce499643f3b8957def4);

740 }

741

742 return api->smbus\_quick(dev, addr, direction);

743}

744

[ 760](group__smbus__interface.md#ga7dd01c1e00a0f8b0315e442707332251)\_\_syscall int [smbus\_byte\_write](group__smbus__interface.md#ga7dd01c1e00a0f8b0315e442707332251)(const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr,

761 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) byte);

762

763static inline int z\_impl\_smbus\_byte\_write(const struct [device](structdevice.md) \*dev,

764 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) byte)

765{

766 const struct smbus\_driver\_api \*api =

767 (const struct smbus\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

768

769 if (api->smbus\_byte\_write == NULL) {

770 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

771 }

772

773 return api->smbus\_byte\_write(dev, addr, byte);

774}

775

[ 791](group__smbus__interface.md#gadaef9dad3470a7e4d3360e0246271ca1)\_\_syscall int [smbus\_byte\_read](group__smbus__interface.md#gadaef9dad3470a7e4d3360e0246271ca1)(const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr,

792 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*byte);

793

794static inline int z\_impl\_smbus\_byte\_read(const struct [device](structdevice.md) \*dev,

795 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*byte)

796{

797 const struct smbus\_driver\_api \*api =

798 (const struct smbus\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

799

800 if (api->smbus\_byte\_read == NULL) {

801 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

802 }

803

804 return api->smbus\_byte\_read(dev, addr, byte);

805}

806

[ 823](group__smbus__interface.md#gadd7ec1eb3db981efceb8f959546a3b6a)\_\_syscall int [smbus\_byte\_data\_write](group__smbus__interface.md#gadd7ec1eb3db981efceb8f959546a3b6a)(const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr,

824 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615), [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) byte);

825

826static inline int z\_impl\_smbus\_byte\_data\_write(const struct [device](structdevice.md) \*dev,

827 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615),

828 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) byte)

829{

830 const struct smbus\_driver\_api \*api =

831 (const struct smbus\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

832

833 if (api->smbus\_byte\_data\_write == NULL) {

834 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

835 }

836

837 return api->smbus\_byte\_data\_write(dev, addr, [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615), byte);

838}

839

[ 856](group__smbus__interface.md#ga1f1148a7cb92e0e0aef7ae3a84615c9b)\_\_syscall int [smbus\_byte\_data\_read](group__smbus__interface.md#ga1f1148a7cb92e0e0aef7ae3a84615c9b)(const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr,

857 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615), [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*byte);

858

859static inline int z\_impl\_smbus\_byte\_data\_read(const struct [device](structdevice.md) \*dev,

860 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615),

861 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*byte)

862{

863 const struct smbus\_driver\_api \*api =

864 (const struct smbus\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

865

866 if (api->smbus\_byte\_data\_read == NULL) {

867 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

868 }

869

870 return api->smbus\_byte\_data\_read(dev, addr, [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615), byte);

871}

872

[ 889](group__smbus__interface.md#gade05f9bbbba609832df91fe804dd5d3c)\_\_syscall int [smbus\_word\_data\_write](group__smbus__interface.md#gade05f9bbbba609832df91fe804dd5d3c)(const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr,

890 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615), [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) word);

891

892static inline int z\_impl\_smbus\_word\_data\_write(const struct [device](structdevice.md) \*dev,

893 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615),

894 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) word)

895{

896 const struct smbus\_driver\_api \*api =

897 (const struct smbus\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

898

899 if (api->smbus\_word\_data\_write == NULL) {

900 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

901 }

902

903 return api->smbus\_word\_data\_write(dev, addr, [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615), word);

904}

905

[ 922](group__smbus__interface.md#ga72a789110c7286a51c5cd5e2215abce1)\_\_syscall int [smbus\_word\_data\_read](group__smbus__interface.md#ga72a789110c7286a51c5cd5e2215abce1)(const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr,

923 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615), [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*word);

924

925static inline int z\_impl\_smbus\_word\_data\_read(const struct [device](structdevice.md) \*dev,

926 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615),

927 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*word)

928{

929 const struct smbus\_driver\_api \*api =

930 (const struct smbus\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

931

932 if (api->smbus\_word\_data\_read == NULL) {

933 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

934 }

935

936 return api->smbus\_word\_data\_read(dev, addr, [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615), word);

937}

938

[ 957](group__smbus__interface.md#ga2c1369835d3783bb5b5c3cb3711fec92)\_\_syscall int [smbus\_pcall](group__smbus__interface.md#ga2c1369835d3783bb5b5c3cb3711fec92)(const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr,

958 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615), [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) send\_word, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*recv\_word);

959

960static inline int z\_impl\_smbus\_pcall(const struct [device](structdevice.md) \*dev,

961 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615),

962 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) send\_word, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*recv\_word)

963{

964 const struct smbus\_driver\_api \*api =

965 (const struct smbus\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

966

967 if (api->smbus\_pcall == NULL) {

968 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

969 }

970

971 return api->smbus\_pcall(dev, addr, [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615), send\_word, recv\_word);

972}

973

[ 991](group__smbus__interface.md#ga55a867cdcb504039f274abae2d1a99e4)\_\_syscall int [smbus\_block\_write](group__smbus__interface.md#ga55a867cdcb504039f274abae2d1a99e4)(const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr,

992 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615), [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) count, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf);

993

994static inline int z\_impl\_smbus\_block\_write(const struct [device](structdevice.md) \*dev,

995 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615),

996 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) count, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf)

997{

998 const struct smbus\_driver\_api \*api =

999 (const struct smbus\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

1000

1001 if (api->smbus\_block\_write == NULL) {

1002 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

1003 }

1004

1005 if (count < 1 || count > [SMBUS\_BLOCK\_BYTES\_MAX](group__smbus__interface.md#ga5ccde036931dc54e684ae5b955ff80d3)) {

1006 return -[EINVAL](group__system__errno.md#ga2d1678d5a7cc8ce499643f3b8957def4);

1007 }

1008

1009 return api->smbus\_block\_write(dev, addr, [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615), count, buf);

1010}

1011

[ 1029](group__smbus__interface.md#ga67603db9b44636b0b62a24fd623cfb1c)\_\_syscall int [smbus\_block\_read](group__smbus__interface.md#ga67603db9b44636b0b62a24fd623cfb1c)(const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr,

1030 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615), [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*count, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf);

1031

1032static inline int z\_impl\_smbus\_block\_read(const struct [device](structdevice.md) \*dev,

1033 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615),

1034 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*count, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf)

1035{

1036 const struct smbus\_driver\_api \*api =

1037 (const struct smbus\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

1038

1039 if (api->smbus\_block\_read == NULL) {

1040 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

1041 }

1042

1043 return api->smbus\_block\_read(dev, addr, [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615), count, buf);

1044}

1045

[ 1066](group__smbus__interface.md#ga680c3d713a615f4b62503d6f84de4290)\_\_syscall int [smbus\_block\_pcall](group__smbus__interface.md#ga680c3d713a615f4b62503d6f84de4290)(const struct [device](structdevice.md) \*dev,

1067 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615),

1068 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) snd\_count, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*snd\_buf,

1069 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*rcv\_count, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*rcv\_buf);

1070

1071static inline int z\_impl\_smbus\_block\_pcall(const struct [device](structdevice.md) \*dev,

1072 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615),

1073 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) snd\_count, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*snd\_buf,

1074 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*rcv\_count, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*rcv\_buf)

1075{

1076 const struct smbus\_driver\_api \*api =

1077 (const struct smbus\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

1078

1079 if (api->smbus\_block\_pcall == NULL) {

1080 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

1081 }

1082

1083 return api->smbus\_block\_pcall(dev, addr, [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615), snd\_count, snd\_buf,

1084 rcv\_count, rcv\_buf);

1085}

1086

1087#ifdef \_\_cplusplus

1088}

1089#endif

1090

1094

1095#include <zephyr/syscalls/smbus.h>

1096

1097#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_SMBUS\_H\_ \*/

[device.h](device_8h.md)

[errno.h](errno_8h.md)

System error numbers.

[recv](group__bsd__sockets.md#gae11da452beee536eac85d5f26e5cdd40)

static ssize\_t recv(int sock, void \*buf, size\_t max\_len, int flags)

POSIX wrapper for zsock\_recv.

**Definition** socket.h:873

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

**Definition** smbus.h:465

[smbus\_byte\_data\_read](group__smbus__interface.md#ga1f1148a7cb92e0e0aef7ae3a84615c9b)

int smbus\_byte\_data\_read(const struct device \*dev, uint16\_t addr, uint8\_t cmd, uint8\_t \*byte)

Perform SMBus Byte Data Read operation.

[smbus\_pcall](group__smbus__interface.md#ga2c1369835d3783bb5b5c3cb3711fec92)

int smbus\_pcall(const struct device \*dev, uint16\_t addr, uint8\_t cmd, uint16\_t send\_word, uint16\_t \*recv\_word)

Perform SMBus Process Call operation.

[smbus\_host\_notify\_set\_cb](group__smbus__interface.md#ga5054a6de634b015f54dacbe81427d0d2)

static int smbus\_host\_notify\_set\_cb(const struct device \*dev, struct smbus\_callback \*cb)

Add Host Notify callback for a SMBus host controller.

**Definition** smbus.h:669

[smbus\_configure](group__smbus__interface.md#ga517305aa7cc9c93ae449b3c548d6c835)

int smbus\_configure(const struct device \*dev, uint32\_t dev\_config)

Configure operation of a SMBus host controller.

[smbus\_block\_write](group__smbus__interface.md#ga55a867cdcb504039f274abae2d1a99e4)

int smbus\_block\_write(const struct device \*dev, uint16\_t addr, uint8\_t cmd, uint8\_t count, uint8\_t \*buf)

Perform SMBus Block Write operation.

[SMBUS\_BLOCK\_BYTES\_MAX](group__smbus__interface.md#ga5ccde036931dc54e684ae5b955ff80d3)

#define SMBUS\_BLOCK\_BYTES\_MAX

Maximum number of bytes in SMBus Block protocol.

**Definition** smbus.h:206

[smbus\_block\_read](group__smbus__interface.md#ga67603db9b44636b0b62a24fd623cfb1c)

int smbus\_block\_read(const struct device \*dev, uint16\_t addr, uint8\_t cmd, uint8\_t \*count, uint8\_t \*buf)

Perform SMBus Block Read operation.

[smbus\_block\_pcall](group__smbus__interface.md#ga680c3d713a615f4b62503d6f84de4290)

int smbus\_block\_pcall(const struct device \*dev, uint16\_t addr, uint8\_t cmd, uint8\_t snd\_count, uint8\_t \*snd\_buf, uint8\_t \*rcv\_count, uint8\_t \*rcv\_buf)

Perform SMBus Block Process Call operation.

[smbus\_callback\_handler\_t](group__smbus__interface.md#ga6d6ee9d29de5c0007d34328eb7c9f7c9)

void(\* smbus\_callback\_handler\_t)(const struct device \*dev, struct smbus\_callback \*cb, uint8\_t addr)

Define SMBus callback handler function signature.

**Definition** smbus.h:274

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

**Definition** smbus.h:252

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

**Definition** smbus.h:618

[SMBUS\_MSG\_WRITE](group__smbus__interface.md#ggad0c28687977d0a7866bdea87aef88016a9c9dec19cbada732cef85784b0eedc54)

@ SMBUS\_MSG\_WRITE

Write a message to SMBus peripheral.

**Definition** smbus.h:254

[SMBUS\_MSG\_READ](group__smbus__interface.md#ggad0c28687977d0a7866bdea87aef88016aa87094fdacefac89c0b1a03be1c0d22f)

@ SMBUS\_MSG\_READ

Read a message from SMBus peripheral.

**Definition** smbus.h:256

[CONTAINER\_OF](group__sys-util.md#gac5bc561d1bfd1bf68877fe577779bd2f)

#define CONTAINER\_OF(ptr, type, field)

Get a pointer to a structure containing the element.

**Definition** util.h:284

[EINVAL](group__system__errno.md#ga2d1678d5a7cc8ce499643f3b8957def4)

#define EINVAL

Invalid argument.

**Definition** errno.h:60

[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b)

#define ENOSYS

Function not implemented.

**Definition** errno.h:82

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

**Definition** device.h:412

[device::api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d)

const void \* api

Address of the API structure exposed by the device instance.

**Definition** device.h:418

[device::state](structdevice.md#abe18f600adc4ab760963928477cc944e)

struct device\_state \* state

Address of the common device state.

**Definition** device.h:420

[smbus\_callback](structsmbus__callback.md)

SMBus callback structure.

**Definition** smbus.h:287

[smbus\_callback::handler](structsmbus__callback.md#a2017d57f8b1bbed10d37cb24a5212bc1)

smbus\_callback\_handler\_t handler

Actual callback function being called when relevant.

**Definition** smbus.h:292

[smbus\_callback::addr](structsmbus__callback.md#a707cc2c4cd2abf214343686d84cd1594)

uint8\_t addr

Peripheral device address.

**Definition** smbus.h:295

[smbus\_callback::node](structsmbus__callback.md#a89fb6ad70aa53dba53aa85ebaea91f60)

sys\_snode\_t node

This should be used in driver for a callback list management.

**Definition** smbus.h:289

[smbus\_dt\_spec](structsmbus__dt__spec.md)

Complete SMBus DT information.

**Definition** smbus.h:301

[smbus\_dt\_spec::addr](structsmbus__dt__spec.md#a0f6080e33e04405a42e9d29118512d08)

uint16\_t addr

Address of the SMBus peripheral device.

**Definition** smbus.h:305

[smbus\_dt\_spec::bus](structsmbus__dt__spec.md#a2b34afb2bc5d55382bc11e0a5ee72684)

const struct device \* bus

SMBus bus.

**Definition** smbus.h:303

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [smbus.h](smbus_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
