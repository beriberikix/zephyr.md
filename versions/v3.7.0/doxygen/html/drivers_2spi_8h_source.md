---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/drivers_2spi_8h_source.html
original_path: doxygen/html/drivers_2spi_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

spi.h

[Go to the documentation of this file.](drivers_2spi_8h.md)

1/\*

2 \* Copyright (c) 2015 Intel Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

11

12#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_SPI\_H\_

13#define ZEPHYR\_INCLUDE\_DRIVERS\_SPI\_H\_

14

23

24#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

25#include <stddef.h>

26#include <[zephyr/device.h](device_8h.md)>

27#include <[zephyr/dt-bindings/spi/spi.h](dt-bindings_2spi_2spi_8h.md)>

28#include <[zephyr/drivers/gpio.h](drivers_2gpio_8h.md)>

29#include <[zephyr/kernel.h](kernel_8h.md)>

30#include <[zephyr/sys/\_\_assert.h](____assert_8h.md)>

31#include <[zephyr/rtio/rtio.h](rtio_2rtio_8h.md)>

32#include <[zephyr/stats/stats.h](stats_2stats_8h.md)>

33

34#ifdef \_\_cplusplus

35extern "C" {

36#endif

37

[ 42](group__spi__interface.md#ga5b9d40fa0f455b1e63f8040b3316b0da)#define SPI\_OP\_MODE\_MASTER 0U

[ 43](group__spi__interface.md#ga1c3310d3711cb99cdb78fa9d1c970779)#define SPI\_OP\_MODE\_SLAVE BIT(0)

45#define SPI\_OP\_MODE\_MASK 0x1U

[ 48](group__spi__interface.md#ga6dd4395e027407a7b3b92cff2abcc8b3)#define SPI\_OP\_MODE\_GET(\_operation\_) ((\_operation\_) & SPI\_OP\_MODE\_MASK)

50

55

[ 61](group__spi__interface.md#ga5a2be1003873beaa0ade10e7218d67d5)#define SPI\_MODE\_CPOL BIT(1)

62

[ 70](group__spi__interface.md#ga35e98b37e3ec4889a90100abe884590f)#define SPI\_MODE\_CPHA BIT(2)

71

[ 77](group__spi__interface.md#ga8619b297de563eca6852af34c79daa62)#define SPI\_MODE\_LOOP BIT(3)

79#define SPI\_MODE\_MASK (0xEU)

[ 82](group__spi__interface.md#gaa3582b96ff42dba0b0ad815c727d5e42)#define SPI\_MODE\_GET(\_mode\_) \

83 ((\_mode\_) & SPI\_MODE\_MASK)

84

86

[ 91](group__spi__interface.md#ga7761f42c6241cf396fc02d0de8617e46)#define SPI\_TRANSFER\_MSB (0U)

[ 92](group__spi__interface.md#ga93504a76a265bedbe781c107beebc9dc)#define SPI\_TRANSFER\_LSB BIT(4)

94

100#define SPI\_WORD\_SIZE\_SHIFT (5U)

101#define SPI\_WORD\_SIZE\_MASK (0x3FU << SPI\_WORD\_SIZE\_SHIFT)

[ 104](group__spi__interface.md#ga7386c70bd669142bb7558526175765cc)#define SPI\_WORD\_SIZE\_GET(\_operation\_) \

105 (((\_operation\_) & SPI\_WORD\_SIZE\_MASK) >> SPI\_WORD\_SIZE\_SHIFT)

106

[ 107](group__spi__interface.md#gaaea60640bb9223bbaf94338d07d9d07c)#define SPI\_WORD\_SET(\_word\_size\_) \

108 ((\_word\_size\_) << SPI\_WORD\_SIZE\_SHIFT)

109

110

[ 116](group__spi__interface.md#gae917312adef283b4bf67cdb53566e4bb)#define SPI\_HOLD\_ON\_CS BIT(12)

[ 122](group__spi__interface.md#gafe8dc164d6fc0a0f93f2ff9d5381af14)#define SPI\_LOCK\_ON BIT(13)

123

[ 131](group__spi__interface.md#ga44076fa14703997f7e3aefb2bfccd801)#define SPI\_CS\_ACTIVE\_HIGH BIT(14)

133

[ 143](group__spi__interface.md#ga7a183f157e8cb8b437857a0babbd923b)#define SPI\_LINES\_SINGLE (0U << 16)

[ 144](group__spi__interface.md#ga120ab60329d664d5d6e828f90251a98a)#define SPI\_LINES\_DUAL (1U << 16)

[ 145](group__spi__interface.md#ga30866b948e995224de854e10a428bda5)#define SPI\_LINES\_QUAD (2U << 16)

[ 146](group__spi__interface.md#ga512d76085e600886654b8541aab31cf7)#define SPI\_LINES\_OCTAL (3U << 16)

147

[ 148](group__spi__interface.md#gadc79f986c4b30fe5b263841cd8bb5676)#define SPI\_LINES\_MASK (0x3U << 16)

149

151

[ 159](structspi__cs__control.md)struct [spi\_cs\_control](structspi__cs__control.md) {

[ 167](structspi__cs__control.md#a8ad907e168666c2ddca77e89f9b9f47f) struct [gpio\_dt\_spec](structgpio__dt__spec.md) [gpio](structspi__cs__control.md#a8ad907e168666c2ddca77e89f9b9f47f);

[ 172](structspi__cs__control.md#a04569d78ac7d6022ffee0c28f5d3b629) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [delay](structspi__cs__control.md#a04569d78ac7d6022ffee0c28f5d3b629);

173};

174

[ 212](group__spi__interface.md#ga48aa19f45413d56b03596d10b72c732e)#define SPI\_CS\_GPIOS\_DT\_SPEC\_GET(spi\_dev) \

213 GPIO\_DT\_SPEC\_GET\_BY\_IDX\_OR(DT\_BUS(spi\_dev), cs\_gpios, \

214 DT\_REG\_ADDR(spi\_dev), {})

215

[ 225](group__spi__interface.md#ga88fefbfadb8184806123e1f935a4ff7c)#define SPI\_CS\_GPIOS\_DT\_SPEC\_INST\_GET(inst) \

226 SPI\_CS\_GPIOS\_DT\_SPEC\_GET(DT\_DRV\_INST(inst))

227

[ 266](group__spi__interface.md#ga4a2bce02956d8121da7b6099f6c097b9)#define SPI\_CS\_CONTROL\_INIT(node\_id, delay\_) \

267 { \

268 .gpio = SPI\_CS\_GPIOS\_DT\_SPEC\_GET(node\_id), \

269 .delay = (delay\_), \

270 }

271

[ 285](group__spi__interface.md#ga239bda66980ed0a349b7177100f7752c)#define SPI\_CS\_CONTROL\_INIT\_INST(inst, delay\_) \

286 SPI\_CS\_CONTROL\_INIT(DT\_DRV\_INST(inst), delay\_)

287

292#if defined(CONFIG\_SPI\_EXTENDED\_MODES)

293typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [spi\_operation\_t](group__spi__interface.md#ga398a8ae1c4799e77fb6c067b6d47294a);

294#else

[ 295](group__spi__interface.md#ga398a8ae1c4799e77fb6c067b6d47294a)typedef [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [spi\_operation\_t](group__spi__interface.md#ga398a8ae1c4799e77fb6c067b6d47294a);

296#endif

297

[ 301](structspi__config.md)struct [spi\_config](structspi__config.md) {

[ 303](structspi__config.md#aa1ec6933fe66f91653c5be488e4c9b2a) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [frequency](structspi__config.md#aa1ec6933fe66f91653c5be488e4c9b2a);

[ 324](structspi__config.md#a71a02ea548e187e6511abf10fdfa4829) [spi\_operation\_t](group__spi__interface.md#ga398a8ae1c4799e77fb6c067b6d47294a) [operation](structspi__config.md#a71a02ea548e187e6511abf10fdfa4829);

[ 326](structspi__config.md#a020ca853537483b9641c37be70ab6ca0) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [slave](structspi__config.md#a020ca853537483b9641c37be70ab6ca0);

[ 331](structspi__config.md#a537dbfe323fafedaa219de1be2097dde) struct [spi\_cs\_control](structspi__cs__control.md) [cs](structspi__config.md#a537dbfe323fafedaa219de1be2097dde);

332};

333

[ 347](group__spi__interface.md#ga822af066ee0829aee405c034bb967463)#define SPI\_CONFIG\_DT(node\_id, operation\_, delay\_) \

348 { \

349 .frequency = DT\_PROP(node\_id, spi\_max\_frequency), \

350 .operation = (operation\_) | \

351 DT\_PROP(node\_id, duplex) | \

352 DT\_PROP(node\_id, frame\_format) | \

353 COND\_CODE\_1(DT\_PROP(node\_id, spi\_cpol), SPI\_MODE\_CPOL, (0)) | \

354 COND\_CODE\_1(DT\_PROP(node\_id, spi\_cpha), SPI\_MODE\_CPHA, (0)) | \

355 COND\_CODE\_1(DT\_PROP(node\_id, spi\_hold\_cs), SPI\_HOLD\_ON\_CS, (0)), \

356 .slave = DT\_REG\_ADDR(node\_id), \

357 .cs = SPI\_CS\_CONTROL\_INIT(node\_id, delay\_), \

358 }

359

[ 371](group__spi__interface.md#gadc1e7de7925603adfedbac35fdabc78a)#define SPI\_CONFIG\_DT\_INST(inst, operation\_, delay\_) \

372 SPI\_CONFIG\_DT(DT\_DRV\_INST(inst), operation\_, delay\_)

373

[ 377](structspi__dt__spec.md)struct [spi\_dt\_spec](structspi__dt__spec.md) {

[ 379](structspi__dt__spec.md#a37519633ae787ffaa1026e6867d7007a) const struct [device](structdevice.md) \*[bus](structspi__dt__spec.md#a37519633ae787ffaa1026e6867d7007a);

[ 381](structspi__dt__spec.md#a88372c17ede2e9dfb0c09c49abebf87e) struct [spi\_config](structspi__config.md) [config](structspi__dt__spec.md#a88372c17ede2e9dfb0c09c49abebf87e);

382};

383

[ 401](group__spi__interface.md#gaec6a8fde1c3ec6349a601a2d5f7af785)#define SPI\_DT\_SPEC\_GET(node\_id, operation\_, delay\_) \

402 { \

403 .bus = DEVICE\_DT\_GET(DT\_BUS(node\_id)), \

404 .config = SPI\_CONFIG\_DT(node\_id, operation\_, delay\_) \

405 }

406

[ 418](group__spi__interface.md#ga91c595b7567af23b447c755d898608f3)#define SPI\_DT\_SPEC\_INST\_GET(inst, operation\_, delay\_) \

419 SPI\_DT\_SPEC\_GET(DT\_DRV\_INST(inst), operation\_, delay\_)

420

[ 424](structspi__buf.md)struct [spi\_buf](structspi__buf.md) {

[ 426](structspi__buf.md#aeaf52d3ff5af10545b2d6904ed452cba) void \*[buf](structspi__buf.md#aeaf52d3ff5af10545b2d6904ed452cba);

[ 431](structspi__buf.md#a9755deadff0dd01a886f22e41099b8ba) size\_t [len](structspi__buf.md#a9755deadff0dd01a886f22e41099b8ba);

432};

433

[ 437](structspi__buf__set.md)struct [spi\_buf\_set](structspi__buf__set.md) {

[ 439](structspi__buf__set.md#a2b88917ca29487b2d0b5b63d2083db67) const struct [spi\_buf](structspi__buf.md) \*[buffers](structspi__buf__set.md#a2b88917ca29487b2d0b5b63d2083db67);

[ 441](structspi__buf__set.md#abc7c37cffebb7873aaba2e524c9a23dc) size\_t [count](structspi__buf__set.md#abc7c37cffebb7873aaba2e524c9a23dc);

442};

443

444#if defined(CONFIG\_SPI\_STATS)

445[STATS\_SECT\_START](stats_2stats_8h.md#ae8e85c3ce2d901f4668d7237b19999fe)(spi)

446[STATS\_SECT\_ENTRY32](stats_2stats_8h.md#a592329613cc77cfa5dee3e1d3b16dd93)(rx\_bytes)

447[STATS\_SECT\_ENTRY32](stats_2stats_8h.md#a592329613cc77cfa5dee3e1d3b16dd93)(tx\_bytes)

448[STATS\_SECT\_ENTRY32](stats_2stats_8h.md#a592329613cc77cfa5dee3e1d3b16dd93)(transfer\_error)

449[STATS\_SECT\_END](stats_2stats_8h.md#a4124f8c0a9ffb78d8be608a780676785);

450

451[STATS\_NAME\_START](stats_2stats_8h.md#abd76143ad82eea7aded01af8cb7bc9ae)(spi)

452[STATS\_NAME](stats_2stats_8h.md#a30648b154e6da64aa39551fac123dd1b)(spi, rx\_bytes)

453[STATS\_NAME](stats_2stats_8h.md#a30648b154e6da64aa39551fac123dd1b)(spi, tx\_bytes)

454[STATS\_NAME](stats_2stats_8h.md#a30648b154e6da64aa39551fac123dd1b)(spi, transfer\_error)

455[STATS\_NAME\_END](stats_2stats_8h.md#a0de61377bb7c254b68cb39a9b5105e4f)(spi);

456

460struct spi\_device\_state {

461 struct [device\_state](structdevice__state.md) devstate;

462 struct stats\_spi stats;

463};

464

468#define Z\_SPI\_GET\_STATS(dev\_) \

469 CONTAINER\_OF(dev\_->state, struct spi\_device\_state, devstate)->stats

470

476#define SPI\_STATS\_RX\_BYTES\_INCN(dev\_, n) \

477 STATS\_INCN(Z\_SPI\_GET\_STATS(dev\_), rx\_bytes, n)

478

484#define SPI\_STATS\_TX\_BYTES\_INCN(dev\_, n) \

485 STATS\_INCN(Z\_SPI\_GET\_STATS(dev\_), tx\_bytes, n)

486

494#define SPI\_STATS\_TRANSFER\_ERROR\_INC(dev\_) \

495 STATS\_INC(Z\_SPI\_GET\_STATS(dev\_), transfer\_error)

496

500#define Z\_SPI\_DEVICE\_STATE\_DEFINE(dev\_id) \

501 static struct spi\_device\_state Z\_DEVICE\_STATE\_NAME(dev\_id) \

502 \_\_attribute\_\_((\_\_section\_\_(".z\_devstate")));

503

510#define Z\_SPI\_INIT\_FN(dev\_id, init\_fn) \

511 static inline int UTIL\_CAT(dev\_id, \_init)(const struct device \*dev) \

512 { \

513 struct spi\_device\_state \*state = \

514 CONTAINER\_OF(dev->state, struct spi\_device\_state, devstate); \

515 stats\_init(&state->stats.s\_hdr, STATS\_SIZE\_32, 3, \

516 STATS\_NAME\_INIT\_PARMS(spi)); \

517 stats\_register(dev->name, &(state->stats.s\_hdr)); \

518 return init\_fn(dev); \

519 }

520

540#define SPI\_DEVICE\_DT\_DEFINE(node\_id, init\_fn, pm\_device, \

541 data\_ptr, cfg\_ptr, level, prio, \

542 api\_ptr, ...) \

543 Z\_SPI\_DEVICE\_STATE\_DEFINE(Z\_DEVICE\_DT\_DEV\_ID(node\_id)); \

544 Z\_SPI\_INIT\_FN(Z\_DEVICE\_DT\_DEV\_ID(node\_id), init\_fn) \

545 Z\_DEVICE\_DEFINE(node\_id, Z\_DEVICE\_DT\_DEV\_ID(node\_id), \

546 DEVICE\_DT\_NAME(node\_id), \

547 &UTIL\_CAT(Z\_DEVICE\_DT\_DEV\_ID(node\_id), \_init), \

548 pm\_device, \

549 data\_ptr, cfg\_ptr, level, prio, \

550 api\_ptr, \

551 &(Z\_DEVICE\_STATE\_NAME(Z\_DEVICE\_DT\_DEV\_ID(node\_id)).devstate), \

552 \_\_VA\_ARGS\_\_)

553

554static inline void [spi\_transceive\_stats](group__spi__interface.md#gad7d1058f600d6aef4fc4e2bdff5d55f3)(const struct [device](structdevice.md) \*dev, int error,

555 const struct [spi\_buf\_set](structspi__buf__set.md) \*tx\_bufs,

556 const struct [spi\_buf\_set](structspi__buf__set.md) \*rx\_bufs)

557{

558 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) tx\_bytes;

559 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) rx\_bytes;

560

561 if (error) {

562 [SPI\_STATS\_TRANSFER\_ERROR\_INC](group__spi__interface.md#ga6f69e68a79afbbe016aecc515f14de3a)(dev);

563 }

564

565 if (tx\_bufs) {

566 tx\_bytes = tx\_bufs->[count](structspi__buf__set.md#abc7c37cffebb7873aaba2e524c9a23dc) ? tx\_bufs->[buffers](structspi__buf__set.md#a2b88917ca29487b2d0b5b63d2083db67)->[len](structspi__buf.md#a9755deadff0dd01a886f22e41099b8ba) : 0;

567 SPI\_STATS\_TX\_BYTES\_INCN(dev, tx\_bytes);

568 }

569

570 if (rx\_bufs) {

571 rx\_bytes = rx\_bufs->[count](structspi__buf__set.md#abc7c37cffebb7873aaba2e524c9a23dc) ? rx\_bufs->[buffers](structspi__buf__set.md#a2b88917ca29487b2d0b5b63d2083db67)->[len](structspi__buf.md#a9755deadff0dd01a886f22e41099b8ba) : 0;

572 SPI\_STATS\_RX\_BYTES\_INCN(dev, rx\_bytes);

573 }

574}

575

576#else /\*CONFIG\_SPI\_STATS\*/

577

[ 578](group__spi__interface.md#ga27af5f053c5fd4e9eef0900406fbf854)#define SPI\_DEVICE\_DT\_DEFINE(node\_id, init\_fn, pm, \

579 data, config, level, prio, \

580 api, ...) \

581 Z\_DEVICE\_STATE\_DEFINE(Z\_DEVICE\_DT\_DEV\_ID(node\_id)); \

582 Z\_DEVICE\_DEFINE(node\_id, Z\_DEVICE\_DT\_DEV\_ID(node\_id), \

583 DEVICE\_DT\_NAME(node\_id), init\_fn, pm, data, config, \

584 level, prio, api, \

585 &Z\_DEVICE\_STATE\_NAME(Z\_DEVICE\_DT\_DEV\_ID(node\_id)), \

586 \_\_VA\_ARGS\_\_)

587

[ 588](group__spi__interface.md#ga83fa04d1e9f281cd566ee32cf807325e)#define SPI\_STATS\_RX\_BYTES\_INC(dev\_)

[ 589](group__spi__interface.md#gadd3b82af2396b91930ece09fa79fc4e2)#define SPI\_STATS\_TX\_BYTES\_INC(dev\_)

[ 590](group__spi__interface.md#ga6f69e68a79afbbe016aecc515f14de3a)#define SPI\_STATS\_TRANSFER\_ERROR\_INC(dev\_)

591

[ 592](group__spi__interface.md#gad7d1058f600d6aef4fc4e2bdff5d55f3)#define spi\_transceive\_stats(dev, error, tx\_bufs, rx\_bufs)

593

594#endif /\*CONFIG\_SPI\_STATS\*/

595

[ 601](group__spi__interface.md#ga3fc669f866b03cfdad98754de69cda13)typedef int (\*[spi\_api\_io](group__spi__interface.md#ga3fc669f866b03cfdad98754de69cda13))(const struct [device](structdevice.md) \*dev,

602 const struct [spi\_config](structspi__config.md) \*config,

603 const struct [spi\_buf\_set](structspi__buf__set.md) \*tx\_bufs,

604 const struct [spi\_buf\_set](structspi__buf__set.md) \*rx\_bufs);

605

[ 613](group__spi__interface.md#ga1db2a410f482d0f26c49f96352aa606d)typedef void (\*[spi\_callback\_t](group__spi__interface.md#ga1db2a410f482d0f26c49f96352aa606d))(const struct [device](structdevice.md) \*dev, int result, void \*[data](structdevice.md#a27573cbd10ee145f8bb1396242b27a3e));

614

[ 620](group__spi__interface.md#ga03be7f33032ac479153616bbe26848e7)typedef int (\*[spi\_api\_io\_async](group__spi__interface.md#ga03be7f33032ac479153616bbe26848e7))(const struct [device](structdevice.md) \*dev,

621 const struct [spi\_config](structspi__config.md) \*config,

622 const struct [spi\_buf\_set](structspi__buf__set.md) \*tx\_bufs,

623 const struct [spi\_buf\_set](structspi__buf__set.md) \*rx\_bufs,

624 [spi\_callback\_t](group__spi__interface.md#ga1db2a410f482d0f26c49f96352aa606d) cb,

625 void \*userdata);

626

627#if defined(CONFIG\_SPI\_RTIO) || defined(DOXYGEN)

628

633typedef void (\*spi\_api\_iodev\_submit)(const struct [device](structdevice.md) \*dev,

634 struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \*iodev\_sqe);

635#endif /\* CONFIG\_SPI\_RTIO \*/

636

[ 642](group__spi__interface.md#gac651ff7cd3dde7abe2525e20ef2e9e7d)typedef int (\*[spi\_api\_release](group__spi__interface.md#gac651ff7cd3dde7abe2525e20ef2e9e7d))(const struct [device](structdevice.md) \*dev,

643 const struct [spi\_config](structspi__config.md) \*config);

644

645

[ 650](structspi__driver__api.md)\_\_subsystem struct [spi\_driver\_api](structspi__driver__api.md) {

[ 651](structspi__driver__api.md#abeb852d35e4772dcec716cf63ef307bb) [spi\_api\_io](group__spi__interface.md#ga3fc669f866b03cfdad98754de69cda13) [transceive](structspi__driver__api.md#abeb852d35e4772dcec716cf63ef307bb);

652#ifdef CONFIG\_SPI\_ASYNC

653 [spi\_api\_io\_async](group__spi__interface.md#ga03be7f33032ac479153616bbe26848e7) transceive\_async;

654#endif /\* CONFIG\_SPI\_ASYNC \*/

655#ifdef CONFIG\_SPI\_RTIO

656 spi\_api\_iodev\_submit iodev\_submit;

657#endif /\* CONFIG\_SPI\_RTIO \*/

[ 658](structspi__driver__api.md#ae15944912ece9f736fd935184e8a184d) [spi\_api\_release](group__spi__interface.md#gac651ff7cd3dde7abe2525e20ef2e9e7d) [release](structspi__driver__api.md#ae15944912ece9f736fd935184e8a184d);

659};

660

[ 668](group__spi__interface.md#gae1156a4ee1b5909c321811045566d888)static inline bool [spi\_cs\_is\_gpio](group__spi__interface.md#gae1156a4ee1b5909c321811045566d888)(const struct [spi\_config](structspi__config.md) \*config)

669{

670 return config->[cs](structspi__config.md#a537dbfe323fafedaa219de1be2097dde).[gpio](structspi__cs__control.md#a8ad907e168666c2ddca77e89f9b9f47f).[port](structgpio__dt__spec.md#a5d617d47e2f568c7a4402a8f5a40ed4f) != NULL;

671}

672

[ 680](group__spi__interface.md#gaa13f0da1f28cffa0da4677987db0c9c5)static inline bool [spi\_cs\_is\_gpio\_dt](group__spi__interface.md#gaa13f0da1f28cffa0da4677987db0c9c5)(const struct [spi\_dt\_spec](structspi__dt__spec.md) \*spec)

681{

682 return [spi\_cs\_is\_gpio](group__spi__interface.md#gae1156a4ee1b5909c321811045566d888)(&spec->[config](structspi__dt__spec.md#a88372c17ede2e9dfb0c09c49abebf87e));

683}

684

[ 693](group__spi__interface.md#ga37b4e5079ed18b70b0c5a260f4c36403)static inline bool [spi\_is\_ready\_dt](group__spi__interface.md#ga37b4e5079ed18b70b0c5a260f4c36403)(const struct [spi\_dt\_spec](structspi__dt__spec.md) \*spec)

694{

695 /\* Validate bus is ready \*/

696 if (![device\_is\_ready](group__device__model.md#gaa4944bd850e90cbd52b0489f9b12edfb)(spec->[bus](structspi__dt__spec.md#a37519633ae787ffaa1026e6867d7007a))) {

697 return false;

698 }

699 /\* Validate CS gpio port is ready, if it is used \*/

700 if ([spi\_cs\_is\_gpio\_dt](group__spi__interface.md#gaa13f0da1f28cffa0da4677987db0c9c5)(spec) &&

701 ![gpio\_is\_ready\_dt](group__gpio__interface.md#gaaec9ad17c08a0d527d66445fe82d8327)(&spec->[config](structspi__dt__spec.md#a88372c17ede2e9dfb0c09c49abebf87e).[cs](structspi__config.md#a537dbfe323fafedaa219de1be2097dde).[gpio](structspi__cs__control.md#a8ad907e168666c2ddca77e89f9b9f47f))) {

702 return false;

703 }

704 return true;

705}

706

[ 725](group__spi__interface.md#gad51054c1ba259db5a64619788506a6f5)\_\_syscall int [spi\_transceive](group__spi__interface.md#gad51054c1ba259db5a64619788506a6f5)(const struct [device](structdevice.md) \*dev,

726 const struct [spi\_config](structspi__config.md) \*config,

727 const struct [spi\_buf\_set](structspi__buf__set.md) \*tx\_bufs,

728 const struct [spi\_buf\_set](structspi__buf__set.md) \*rx\_bufs);

729

730static inline int z\_impl\_spi\_transceive(const struct [device](structdevice.md) \*dev,

731 const struct [spi\_config](structspi__config.md) \*config,

732 const struct [spi\_buf\_set](structspi__buf__set.md) \*tx\_bufs,

733 const struct [spi\_buf\_set](structspi__buf__set.md) \*rx\_bufs)

734{

735 const struct [spi\_driver\_api](structspi__driver__api.md) \*api =

736 (const struct [spi\_driver\_api](structspi__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

737 int ret;

738

739 ret = api->transceive(dev, config, tx\_bufs, rx\_bufs);

740 [spi\_transceive\_stats](group__spi__interface.md#gad7d1058f600d6aef4fc4e2bdff5d55f3)(dev, ret, tx\_bufs, rx\_bufs);

741

742 return ret;

743}

744

[ 760](group__spi__interface.md#ga52c017066736414b31ff709ddc67c4ff)static inline int [spi\_transceive\_dt](group__spi__interface.md#ga52c017066736414b31ff709ddc67c4ff)(const struct [spi\_dt\_spec](structspi__dt__spec.md) \*spec,

761 const struct [spi\_buf\_set](structspi__buf__set.md) \*tx\_bufs,

762 const struct [spi\_buf\_set](structspi__buf__set.md) \*rx\_bufs)

763{

764 return [spi\_transceive](group__spi__interface.md#gad51054c1ba259db5a64619788506a6f5)(spec->[bus](structspi__dt__spec.md#a37519633ae787ffaa1026e6867d7007a), &spec->[config](structspi__dt__spec.md#a88372c17ede2e9dfb0c09c49abebf87e), tx\_bufs, rx\_bufs);

765}

766

[ 784](group__spi__interface.md#ga41f771785a4fa9ca0954125d1e97959e)static inline int [spi\_read](group__spi__interface.md#ga41f771785a4fa9ca0954125d1e97959e)(const struct [device](structdevice.md) \*dev,

785 const struct [spi\_config](structspi__config.md) \*config,

786 const struct [spi\_buf\_set](structspi__buf__set.md) \*rx\_bufs)

787{

788 return [spi\_transceive](group__spi__interface.md#gad51054c1ba259db5a64619788506a6f5)(dev, config, NULL, rx\_bufs);

789}

790

[ 803](group__spi__interface.md#ga7a1d7ebd37d2861b169c265cb90015bf)static inline int [spi\_read\_dt](group__spi__interface.md#ga7a1d7ebd37d2861b169c265cb90015bf)(const struct [spi\_dt\_spec](structspi__dt__spec.md) \*spec,

804 const struct [spi\_buf\_set](structspi__buf__set.md) \*rx\_bufs)

805{

806 return [spi\_read](group__spi__interface.md#ga41f771785a4fa9ca0954125d1e97959e)(spec->[bus](structspi__dt__spec.md#a37519633ae787ffaa1026e6867d7007a), &spec->[config](structspi__dt__spec.md#a88372c17ede2e9dfb0c09c49abebf87e), rx\_bufs);

807}

808

[ 825](group__spi__interface.md#ga7e7c4460670ec1c0433ba19accd97796)static inline int [spi\_write](group__spi__interface.md#ga7e7c4460670ec1c0433ba19accd97796)(const struct [device](structdevice.md) \*dev,

826 const struct [spi\_config](structspi__config.md) \*config,

827 const struct [spi\_buf\_set](structspi__buf__set.md) \*tx\_bufs)

828{

829 return [spi\_transceive](group__spi__interface.md#gad51054c1ba259db5a64619788506a6f5)(dev, config, tx\_bufs, NULL);

830}

831

[ 844](group__spi__interface.md#ga292d6d1fe82f3f1ce0d9a2aa5437201b)static inline int [spi\_write\_dt](group__spi__interface.md#ga292d6d1fe82f3f1ce0d9a2aa5437201b)(const struct [spi\_dt\_spec](structspi__dt__spec.md) \*spec,

845 const struct [spi\_buf\_set](structspi__buf__set.md) \*tx\_bufs)

846{

847 return [spi\_write](group__spi__interface.md#ga7e7c4460670ec1c0433ba19accd97796)(spec->[bus](structspi__dt__spec.md#a37519633ae787ffaa1026e6867d7007a), &spec->[config](structspi__dt__spec.md#a88372c17ede2e9dfb0c09c49abebf87e), tx\_bufs);

848}

849

850#if defined(CONFIG\_SPI\_ASYNC) || defined(\_\_DOXYGEN\_\_)

851

[ 878](group__spi__interface.md#ga6114e63ca23b82f9be0ac70e372b878b)static inline int [spi\_transceive\_cb](group__spi__interface.md#ga6114e63ca23b82f9be0ac70e372b878b)(const struct [device](structdevice.md) \*dev,

879 const struct [spi\_config](structspi__config.md) \*config,

880 const struct [spi\_buf\_set](structspi__buf__set.md) \*tx\_bufs,

881 const struct [spi\_buf\_set](structspi__buf__set.md) \*rx\_bufs,

882 [spi\_callback\_t](group__spi__interface.md#ga1db2a410f482d0f26c49f96352aa606d) callback,

883 void \*userdata)

884{

885 const struct [spi\_driver\_api](structspi__driver__api.md) \*api =

886 (const struct [spi\_driver\_api](structspi__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

887

888 return api->transceive\_async(dev, config, tx\_bufs, rx\_bufs, callback, userdata);

889}

890

891#if defined(CONFIG\_POLL) || defined(\_\_DOXYGEN\_\_)

892

894void z\_spi\_transfer\_signal\_cb(const struct [device](structdevice.md) \*dev, int result, void \*userdata);

896

[ 922](group__spi__interface.md#ga41b8a541257c0d45575fdc4593417edc)static inline int [spi\_transceive\_signal](group__spi__interface.md#ga41b8a541257c0d45575fdc4593417edc)(const struct [device](structdevice.md) \*dev,

923 const struct [spi\_config](structspi__config.md) \*config,

924 const struct [spi\_buf\_set](structspi__buf__set.md) \*tx\_bufs,

925 const struct [spi\_buf\_set](structspi__buf__set.md) \*rx\_bufs,

926 struct [k\_poll\_signal](structk__poll__signal.md) \*sig)

927{

928 const struct [spi\_driver\_api](structspi__driver__api.md) \*api =

929 (const struct [spi\_driver\_api](structspi__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

930 [spi\_callback\_t](group__spi__interface.md#ga1db2a410f482d0f26c49f96352aa606d) cb = (sig == NULL) ? NULL : z\_spi\_transfer\_signal\_cb;

931

932 return api->transceive\_async(dev, config, tx\_bufs, rx\_bufs, cb, sig);

933}

934

[ 959](group__spi__interface.md#ga9a1ceadb217368232af5b688c12169c5)static inline int [spi\_read\_signal](group__spi__interface.md#ga9a1ceadb217368232af5b688c12169c5)(const struct [device](structdevice.md) \*dev,

960 const struct [spi\_config](structspi__config.md) \*config,

961 const struct [spi\_buf\_set](structspi__buf__set.md) \*rx\_bufs,

962 struct [k\_poll\_signal](structk__poll__signal.md) \*sig)

963{

964 return [spi\_transceive\_signal](group__spi__interface.md#ga41b8a541257c0d45575fdc4593417edc)(dev, config, NULL, rx\_bufs, sig);

965}

966

[ 990](group__spi__interface.md#gadcb19d43461ef88e31f6b382cc87fd0b)static inline int [spi\_write\_signal](group__spi__interface.md#gadcb19d43461ef88e31f6b382cc87fd0b)(const struct [device](structdevice.md) \*dev,

991 const struct [spi\_config](structspi__config.md) \*config,

992 const struct [spi\_buf\_set](structspi__buf__set.md) \*tx\_bufs,

993 struct [k\_poll\_signal](structk__poll__signal.md) \*sig)

994{

995 return [spi\_transceive\_signal](group__spi__interface.md#ga41b8a541257c0d45575fdc4593417edc)(dev, config, tx\_bufs, NULL, sig);

996}

997

998#endif /\* CONFIG\_POLL \*/

999

1000#endif /\* CONFIG\_SPI\_ASYNC \*/

1001

1002

1003#if defined(CONFIG\_SPI\_RTIO) || defined(\_\_DOXYGEN\_\_)

1004

[ 1012](group__spi__interface.md#ga8b23855bdc7dab7d02b8f7daa7db651b)static inline void [spi\_iodev\_submit](group__spi__interface.md#ga8b23855bdc7dab7d02b8f7daa7db651b)(struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \*iodev\_sqe)

1013{

1014 const struct [spi\_dt\_spec](structspi__dt__spec.md) \*dt\_spec = iodev\_sqe->[sqe](structrtio__iodev__sqe.md#a2bd98599678909c0ddb22f879affa12b).[iodev](structrtio__sqe.md#a6c784702f011592c84feacd57915bbfc)->[data](structrtio__iodev.md#af0f3a27fe8dea2161c9a73cb838bdeec);

1015 const struct [device](structdevice.md) \*dev = dt\_spec->[bus](structspi__dt__spec.md#a37519633ae787ffaa1026e6867d7007a);

1016 const struct [spi\_driver\_api](structspi__driver__api.md) \*api = (const struct [spi\_driver\_api](structspi__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

1017

1018 api->iodev\_submit(dt\_spec->[bus](structspi__dt__spec.md#a37519633ae787ffaa1026e6867d7007a), iodev\_sqe);

1019}

1020

1021extern const struct [rtio\_iodev\_api](structrtio__iodev__api.md) [spi\_iodev\_api](group__spi__interface.md#gacd22d734b1b2729e09862065d44b8ce9);

1022

[ 1034](group__spi__interface.md#ga1e9f5fe389d53c280639f23ea134e18c)#define SPI\_DT\_IODEV\_DEFINE(name, node\_id, operation\_, delay\_) \

1035 const struct spi\_dt\_spec \_spi\_dt\_spec\_##name = \

1036 SPI\_DT\_SPEC\_GET(node\_id, operation\_, delay\_); \

1037 RTIO\_IODEV\_DEFINE(name, &spi\_iodev\_api, (void \*)&\_spi\_dt\_spec\_##name)

1038

[ 1047](group__spi__interface.md#gafea78af1fe1fa49fdc5459ab3a2d5f73)static inline bool [spi\_is\_ready\_iodev](group__spi__interface.md#gafea78af1fe1fa49fdc5459ab3a2d5f73)(const struct [rtio\_iodev](structrtio__iodev.md) \*spi\_iodev)

1048{

1049 struct [spi\_dt\_spec](structspi__dt__spec.md) \*spec = spi\_iodev->[data](structrtio__iodev.md#af0f3a27fe8dea2161c9a73cb838bdeec);

1050

1051 return [spi\_is\_ready\_dt](group__spi__interface.md#ga37b4e5079ed18b70b0c5a260f4c36403)(spec);

1052}

1053

[ 1066](group__spi__interface.md#ga812818433d437829fe6ab4fcff0ed38b)static inline int [spi\_rtio\_copy](group__spi__interface.md#ga812818433d437829fe6ab4fcff0ed38b)(struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2),

1067 struct [rtio\_iodev](structrtio__iodev.md) \*iodev,

1068 const struct [spi\_buf\_set](structspi__buf__set.md) \*tx\_bufs,

1069 const struct [spi\_buf\_set](structspi__buf__set.md) \*rx\_bufs,

1070 struct [rtio\_sqe](structrtio__sqe.md) \*\*last\_sqe)

1071{

1072 int ret = 0;

1073 size\_t tx\_count = tx\_bufs ? tx\_bufs->[count](structspi__buf__set.md#abc7c37cffebb7873aaba2e524c9a23dc) : 0;

1074 size\_t rx\_count = rx\_bufs ? rx\_bufs->[count](structspi__buf__set.md#abc7c37cffebb7873aaba2e524c9a23dc) : 0;

1075

1076 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) tx = 0, tx\_len = 0;

1077 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) rx = 0, rx\_len = 0;

1078 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*tx\_buf, \*rx\_buf;

1079

1080 struct [rtio\_sqe](structrtio__sqe.md) \*sqe = NULL;

1081

1082 if (tx < tx\_count) {

1083 [tx\_buf](structrtio__sqe.md#a186c22217961a5eddb75ad0bd84a538a) = tx\_bufs->[buffers](structspi__buf__set.md#a2b88917ca29487b2d0b5b63d2083db67)[tx].[buf](structspi__buf.md#aeaf52d3ff5af10545b2d6904ed452cba);

1084 tx\_len = tx\_bufs->[buffers](structspi__buf__set.md#a2b88917ca29487b2d0b5b63d2083db67)[tx].[len](structspi__buf.md#a9755deadff0dd01a886f22e41099b8ba);

1085 } else {

1086 [tx\_buf](structrtio__sqe.md#a186c22217961a5eddb75ad0bd84a538a) = NULL;

1087 tx\_len = rx\_bufs->[buffers](structspi__buf__set.md#a2b88917ca29487b2d0b5b63d2083db67)[rx].[len](structspi__buf.md#a9755deadff0dd01a886f22e41099b8ba);

1088 }

1089

1090 if (rx < rx\_count) {

1091 [rx\_buf](structrtio__sqe.md#a4d2090fc11b897724a883ad1087d9f73) = rx\_bufs->[buffers](structspi__buf__set.md#a2b88917ca29487b2d0b5b63d2083db67)[rx].[buf](structspi__buf.md#aeaf52d3ff5af10545b2d6904ed452cba);

1092 rx\_len = rx\_bufs->[buffers](structspi__buf__set.md#a2b88917ca29487b2d0b5b63d2083db67)[rx].[len](structspi__buf.md#a9755deadff0dd01a886f22e41099b8ba);

1093 } else {

1094 [rx\_buf](structrtio__sqe.md#a4d2090fc11b897724a883ad1087d9f73) = NULL;

1095 rx\_len = tx\_bufs->[buffers](structspi__buf__set.md#a2b88917ca29487b2d0b5b63d2083db67)[tx].[len](structspi__buf.md#a9755deadff0dd01a886f22e41099b8ba);

1096 }

1097

1098

1099 while ((tx < tx\_count || rx < rx\_count) && (tx\_len > 0 || rx\_len > 0)) {

1100 sqe = [rtio\_sqe\_acquire](group__rtio.md#ga8b47c954d15a334621def53acceb6799)([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2));

1101

1102 if (sqe == NULL) {

1103 ret = -[ENOMEM](group__system__errno.md#ga6a05c923dad0c1208043e9c20a58c8e5);

1104 [rtio\_sqe\_drop\_all](group__rtio.md#ga9486fb7b50e8d2409a50da235203536b)([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2));

1105 goto out;

1106 }

1107

1108 ret++;

1109

1110 /\* If tx/rx len are same, we can do a simple transceive \*/

1111 if (tx\_len == rx\_len) {

1112 if ([tx\_buf](structrtio__sqe.md#a186c22217961a5eddb75ad0bd84a538a) == NULL) {

1113 [rtio\_sqe\_prep\_read](group__rtio.md#ga89c7cc2494e3dda50737f78f1a1376cf)(sqe, [iodev](structrtio__sqe.md#a6c784702f011592c84feacd57915bbfc), [RTIO\_PRIO\_NORM](group__rtio__sqe__prio.md#gab02e27e01b7dd4eb3439df557899ce92),

1114 [rx\_buf](structrtio__sqe.md#a4d2090fc11b897724a883ad1087d9f73), rx\_len, NULL);

1115 } else if ([rx\_buf](structrtio__sqe.md#a4d2090fc11b897724a883ad1087d9f73) == NULL) {

1116 [rtio\_sqe\_prep\_write](group__rtio.md#gab01192577dadf7ab83d3f8029c86a149)(sqe, [iodev](structrtio__sqe.md#a6c784702f011592c84feacd57915bbfc), [RTIO\_PRIO\_NORM](group__rtio__sqe__prio.md#gab02e27e01b7dd4eb3439df557899ce92),

1117 [tx\_buf](structrtio__sqe.md#a186c22217961a5eddb75ad0bd84a538a), tx\_len, NULL);

1118 } else {

1119 [rtio\_sqe\_prep\_transceive](group__rtio.md#ga0129e02abc85526199311846e1830869)(sqe, [iodev](structrtio__sqe.md#a6c784702f011592c84feacd57915bbfc), [RTIO\_PRIO\_NORM](group__rtio__sqe__prio.md#gab02e27e01b7dd4eb3439df557899ce92),

1120 [tx\_buf](structrtio__sqe.md#a186c22217961a5eddb75ad0bd84a538a), [rx\_buf](structrtio__sqe.md#a4d2090fc11b897724a883ad1087d9f73), rx\_len, NULL);

1121 }

1122 tx++;

1123 rx++;

1124 if (rx < rx\_count) {

1125 [rx\_buf](structrtio__sqe.md#a4d2090fc11b897724a883ad1087d9f73) = rx\_bufs->[buffers](structspi__buf__set.md#a2b88917ca29487b2d0b5b63d2083db67)[rx].[buf](structspi__buf.md#aeaf52d3ff5af10545b2d6904ed452cba);

1126 rx\_len = rx\_bufs->[buffers](structspi__buf__set.md#a2b88917ca29487b2d0b5b63d2083db67)[rx].[len](structspi__buf.md#a9755deadff0dd01a886f22e41099b8ba);

1127 } else {

1128 [rx\_buf](structrtio__sqe.md#a4d2090fc11b897724a883ad1087d9f73) = NULL;

1129 rx\_len = 0;

1130 }

1131 if (tx < tx\_count) {

1132 [tx\_buf](structrtio__sqe.md#a186c22217961a5eddb75ad0bd84a538a) = tx\_bufs->[buffers](structspi__buf__set.md#a2b88917ca29487b2d0b5b63d2083db67)[tx].[buf](structspi__buf.md#aeaf52d3ff5af10545b2d6904ed452cba);

1133 tx\_len = tx\_bufs->[buffers](structspi__buf__set.md#a2b88917ca29487b2d0b5b63d2083db67)[tx].[len](structspi__buf.md#a9755deadff0dd01a886f22e41099b8ba);

1134 } else {

1135 [tx\_buf](structrtio__sqe.md#a186c22217961a5eddb75ad0bd84a538a) = NULL;

1136 tx\_len = 0;

1137 }

1138 } else if (tx\_len == 0) {

1139 [rtio\_sqe\_prep\_read](group__rtio.md#ga89c7cc2494e3dda50737f78f1a1376cf)(sqe, [iodev](structrtio__sqe.md#a6c784702f011592c84feacd57915bbfc), [RTIO\_PRIO\_NORM](group__rtio__sqe__prio.md#gab02e27e01b7dd4eb3439df557899ce92),

1140 ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*)[rx\_buf](structrtio__sqe.md#a4d2090fc11b897724a883ad1087d9f73),

1141 ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f))rx\_len,

1142 NULL);

1143 rx++;

1144 if (rx < rx\_count) {

1145 [rx\_buf](structrtio__sqe.md#a4d2090fc11b897724a883ad1087d9f73) = rx\_bufs->[buffers](structspi__buf__set.md#a2b88917ca29487b2d0b5b63d2083db67)[rx].[buf](structspi__buf.md#aeaf52d3ff5af10545b2d6904ed452cba);

1146 rx\_len = rx\_bufs->[buffers](structspi__buf__set.md#a2b88917ca29487b2d0b5b63d2083db67)[rx].[len](structspi__buf.md#a9755deadff0dd01a886f22e41099b8ba);

1147 } else {

1148 [rx\_buf](structrtio__sqe.md#a4d2090fc11b897724a883ad1087d9f73) = NULL;

1149 rx\_len = 0;

1150 }

1151 } else if (rx\_len == 0) {

1152 [rtio\_sqe\_prep\_write](group__rtio.md#gab01192577dadf7ab83d3f8029c86a149)(sqe, [iodev](structrtio__sqe.md#a6c784702f011592c84feacd57915bbfc), [RTIO\_PRIO\_NORM](group__rtio__sqe__prio.md#gab02e27e01b7dd4eb3439df557899ce92),

1153 ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*)[tx\_buf](structrtio__sqe.md#a186c22217961a5eddb75ad0bd84a538a),

1154 ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f))tx\_len,

1155 NULL);

1156 tx++;

1157 if (tx < tx\_count) {

1158 [tx\_buf](structrtio__sqe.md#a186c22217961a5eddb75ad0bd84a538a) = rx\_bufs->[buffers](structspi__buf__set.md#a2b88917ca29487b2d0b5b63d2083db67)[rx].[buf](structspi__buf.md#aeaf52d3ff5af10545b2d6904ed452cba);

1159 tx\_len = rx\_bufs->[buffers](structspi__buf__set.md#a2b88917ca29487b2d0b5b63d2083db67)[rx].[len](structspi__buf.md#a9755deadff0dd01a886f22e41099b8ba);

1160 } else {

1161 [tx\_buf](structrtio__sqe.md#a186c22217961a5eddb75ad0bd84a538a) = NULL;

1162 tx\_len = 0;

1163 }

1164 } else if (tx\_len > rx\_len) {

1165 [rtio\_sqe\_prep\_transceive](group__rtio.md#ga0129e02abc85526199311846e1830869)(sqe, [iodev](structrtio__sqe.md#a6c784702f011592c84feacd57915bbfc), [RTIO\_PRIO\_NORM](group__rtio__sqe__prio.md#gab02e27e01b7dd4eb3439df557899ce92),

1166 ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*)[tx\_buf](structrtio__sqe.md#a186c22217961a5eddb75ad0bd84a538a),

1167 ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*)[rx\_buf](structrtio__sqe.md#a4d2090fc11b897724a883ad1087d9f73),

1168 ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f))rx\_len,

1169 NULL);

1170 tx\_len -= rx\_len;

1171 [tx\_buf](structrtio__sqe.md#a186c22217961a5eddb75ad0bd84a538a) += rx\_len;

1172 rx++;

1173 if (rx < rx\_count) {

1174 [rx\_buf](structrtio__sqe.md#a4d2090fc11b897724a883ad1087d9f73) = rx\_bufs->[buffers](structspi__buf__set.md#a2b88917ca29487b2d0b5b63d2083db67)[rx].[buf](structspi__buf.md#aeaf52d3ff5af10545b2d6904ed452cba);

1175 rx\_len = rx\_bufs->[buffers](structspi__buf__set.md#a2b88917ca29487b2d0b5b63d2083db67)[rx].[len](structspi__buf.md#a9755deadff0dd01a886f22e41099b8ba);

1176 } else {

1177 [rx\_buf](structrtio__sqe.md#a4d2090fc11b897724a883ad1087d9f73) = NULL;

1178 rx\_len = tx\_len;

1179 }

1180 } else if (rx\_len > tx\_len) {

1181 [rtio\_sqe\_prep\_transceive](group__rtio.md#ga0129e02abc85526199311846e1830869)(sqe, [iodev](structrtio__sqe.md#a6c784702f011592c84feacd57915bbfc), [RTIO\_PRIO\_NORM](group__rtio__sqe__prio.md#gab02e27e01b7dd4eb3439df557899ce92),

1182 ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*)[tx\_buf](structrtio__sqe.md#a186c22217961a5eddb75ad0bd84a538a),

1183 ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*)[rx\_buf](structrtio__sqe.md#a4d2090fc11b897724a883ad1087d9f73),

1184 ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f))tx\_len,

1185 NULL);

1186 rx\_len -= tx\_len;

1187 [rx\_buf](structrtio__sqe.md#a4d2090fc11b897724a883ad1087d9f73) += tx\_len;

1188 tx++;

1189 if (tx < tx\_count) {

1190 [tx\_buf](structrtio__sqe.md#a186c22217961a5eddb75ad0bd84a538a) = tx\_bufs->[buffers](structspi__buf__set.md#a2b88917ca29487b2d0b5b63d2083db67)[tx].[buf](structspi__buf.md#aeaf52d3ff5af10545b2d6904ed452cba);

1191 tx\_len = tx\_bufs->[buffers](structspi__buf__set.md#a2b88917ca29487b2d0b5b63d2083db67)[tx].[len](structspi__buf.md#a9755deadff0dd01a886f22e41099b8ba);

1192 } else {

1193 [tx\_buf](structrtio__sqe.md#a186c22217961a5eddb75ad0bd84a538a) = NULL;

1194 tx\_len = rx\_len;

1195 }

1196 } else {

1197 \_\_ASSERT\_NO\_MSG("Invalid spi\_rtio\_copy state");

1198 }

1199

1200 sqe->[flags](structrtio__sqe.md#aad2ff8524df0e24b812e77e2393bf5b0) = [RTIO\_SQE\_TRANSACTION](group__rtio__sqe__flags.md#ga07f09cc0c95be6cfdddb23f8acacb1ea);

1201 }

1202

1203 if (sqe != NULL) {

1204 sqe->[flags](structrtio__sqe.md#aad2ff8524df0e24b812e77e2393bf5b0) = 0;

1205 \*last\_sqe = sqe;

1206 }

1207

1208out:

1209 return ret;

1210}

1211

1212#endif /\* CONFIG\_SPI\_RTIO \*/

1213

[ 1234](group__spi__interface.md#ga0c4f4f0a93bb83a4f58d551a7491164e)\_\_syscall int [spi\_release](group__spi__interface.md#ga0c4f4f0a93bb83a4f58d551a7491164e)(const struct [device](structdevice.md) \*dev,

1235 const struct [spi\_config](structspi__config.md) \*config);

1236

1237static inline int z\_impl\_spi\_release(const struct [device](structdevice.md) \*dev,

1238 const struct [spi\_config](structspi__config.md) \*config)

1239{

1240 const struct [spi\_driver\_api](structspi__driver__api.md) \*api =

1241 (const struct [spi\_driver\_api](structspi__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

1242

1243 return api->release(dev, config);

1244}

1245

[ 1257](group__spi__interface.md#ga829b59767c51b20b546eee8a9cc84b69)static inline int [spi\_release\_dt](group__spi__interface.md#ga829b59767c51b20b546eee8a9cc84b69)(const struct [spi\_dt\_spec](structspi__dt__spec.md) \*spec)

1258{

1259 return [spi\_release](group__spi__interface.md#ga0c4f4f0a93bb83a4f58d551a7491164e)(spec->[bus](structspi__dt__spec.md#a37519633ae787ffaa1026e6867d7007a), &spec->[config](structspi__dt__spec.md#a88372c17ede2e9dfb0c09c49abebf87e));

1260}

1261

1262#ifdef \_\_cplusplus

1263}

1264#endif

1265

1269

1270#include <zephyr/syscalls/spi.h>

1271

1272#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_SPI\_H\_ \*/

[\_\_assert.h](____assert_8h.md)

[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)

workaround assembler barfing for ST r

**Definition** asm-macro-32-bit-gnu.h:24

[device.h](device_8h.md)

[gpio.h](drivers_2gpio_8h.md)

Public APIs for GPIO drivers.

[spi.h](dt-bindings_2spi_2spi_8h.md)

[device\_is\_ready](group__device__model.md#gaa4944bd850e90cbd52b0489f9b12edfb)

bool device\_is\_ready(const struct device \*dev)

Verify that a device is ready for use.

[gpio\_is\_ready\_dt](group__gpio__interface.md#gaaec9ad17c08a0d527d66445fe82d8327)

static bool gpio\_is\_ready\_dt(const struct gpio\_dt\_spec \*spec)

Validate that GPIO port is ready.

**Definition** gpio.h:835

[RTIO\_SQE\_TRANSACTION](group__rtio__sqe__flags.md#ga07f09cc0c95be6cfdddb23f8acacb1ea)

#define RTIO\_SQE\_TRANSACTION

The next request in the queue is part of a transaction.

**Definition** rtio.h:108

[RTIO\_PRIO\_NORM](group__rtio__sqe__prio.md#gab02e27e01b7dd4eb3439df557899ce92)

#define RTIO\_PRIO\_NORM

Normal priority.

**Definition** rtio.h:70

[rtio\_sqe\_prep\_transceive](group__rtio.md#ga0129e02abc85526199311846e1830869)

static void rtio\_sqe\_prep\_transceive(struct rtio\_sqe \*sqe, const struct rtio\_iodev \*iodev, int8\_t prio, uint8\_t \*tx\_buf, uint8\_t \*rx\_buf, uint32\_t buf\_len, void \*userdata)

Prepare a transceive op submission.

**Definition** rtio.h:605

[rtio\_sqe\_prep\_read](group__rtio.md#ga89c7cc2494e3dda50737f78f1a1376cf)

static void rtio\_sqe\_prep\_read(struct rtio\_sqe \*sqe, const struct rtio\_iodev \*iodev, int8\_t prio, uint8\_t \*buf, uint32\_t len, void \*userdata)

Prepare a read op submission.

**Definition** rtio.h:496

[rtio\_sqe\_acquire](group__rtio.md#ga8b47c954d15a334621def53acceb6799)

static struct rtio\_sqe \* rtio\_sqe\_acquire(struct rtio \*r)

Acquire a single submission queue event if available.

**Definition** rtio.h:901

[rtio\_sqe\_drop\_all](group__rtio.md#ga9486fb7b50e8d2409a50da235203536b)

static void rtio\_sqe\_drop\_all(struct rtio \*r)

Drop all previously acquired sqe.

**Definition** rtio.h:919

[rtio\_sqe\_prep\_write](group__rtio.md#gab01192577dadf7ab83d3f8029c86a149)

static void rtio\_sqe\_prep\_write(struct rtio\_sqe \*sqe, const struct rtio\_iodev \*iodev, int8\_t prio, uint8\_t \*buf, uint32\_t len, void \*userdata)

Prepare a write op submission.

**Definition** rtio.h:536

[spi\_api\_io\_async](group__spi__interface.md#ga03be7f33032ac479153616bbe26848e7)

int(\* spi\_api\_io\_async)(const struct device \*dev, const struct spi\_config \*config, const struct spi\_buf\_set \*tx\_bufs, const struct spi\_buf\_set \*rx\_bufs, spi\_callback\_t cb, void \*userdata)

**Definition** spi.h:620

[spi\_release](group__spi__interface.md#ga0c4f4f0a93bb83a4f58d551a7491164e)

int spi\_release(const struct device \*dev, const struct spi\_config \*config)

Release the SPI device locked on and/or the CS by the current config.

[spi\_callback\_t](group__spi__interface.md#ga1db2a410f482d0f26c49f96352aa606d)

void(\* spi\_callback\_t)(const struct device \*dev, int result, void \*data)

SPI callback for asynchronous transfer requests.

**Definition** spi.h:613

[spi\_write\_dt](group__spi__interface.md#ga292d6d1fe82f3f1ce0d9a2aa5437201b)

static int spi\_write\_dt(const struct spi\_dt\_spec \*spec, const struct spi\_buf\_set \*tx\_bufs)

Write data to a SPI bus specified in spi\_dt\_spec.

**Definition** spi.h:844

[spi\_is\_ready\_dt](group__spi__interface.md#ga37b4e5079ed18b70b0c5a260f4c36403)

static bool spi\_is\_ready\_dt(const struct spi\_dt\_spec \*spec)

Validate that SPI bus (and CS gpio if defined) is ready.

**Definition** spi.h:693

[spi\_operation\_t](group__spi__interface.md#ga398a8ae1c4799e77fb6c067b6d47294a)

uint16\_t spi\_operation\_t

Opaque type to hold the SPI operation flags.

**Definition** spi.h:295

[spi\_api\_io](group__spi__interface.md#ga3fc669f866b03cfdad98754de69cda13)

int(\* spi\_api\_io)(const struct device \*dev, const struct spi\_config \*config, const struct spi\_buf\_set \*tx\_bufs, const struct spi\_buf\_set \*rx\_bufs)

Callback API for I/O See spi\_transceive() for argument descriptions.

**Definition** spi.h:601

[spi\_transceive\_signal](group__spi__interface.md#ga41b8a541257c0d45575fdc4593417edc)

static int spi\_transceive\_signal(const struct device \*dev, const struct spi\_config \*config, const struct spi\_buf\_set \*tx\_bufs, const struct spi\_buf\_set \*rx\_bufs, struct k\_poll\_signal \*sig)

Read/write the specified amount of data from the SPI driver.

**Definition** spi.h:922

[spi\_read](group__spi__interface.md#ga41f771785a4fa9ca0954125d1e97959e)

static int spi\_read(const struct device \*dev, const struct spi\_config \*config, const struct spi\_buf\_set \*rx\_bufs)

Read the specified amount of data from the SPI driver.

**Definition** spi.h:784

[spi\_transceive\_dt](group__spi__interface.md#ga52c017066736414b31ff709ddc67c4ff)

static int spi\_transceive\_dt(const struct spi\_dt\_spec \*spec, const struct spi\_buf\_set \*tx\_bufs, const struct spi\_buf\_set \*rx\_bufs)

Read/write data from an SPI bus specified in spi\_dt\_spec.

**Definition** spi.h:760

[spi\_transceive\_cb](group__spi__interface.md#ga6114e63ca23b82f9be0ac70e372b878b)

static int spi\_transceive\_cb(const struct device \*dev, const struct spi\_config \*config, const struct spi\_buf\_set \*tx\_bufs, const struct spi\_buf\_set \*rx\_bufs, spi\_callback\_t callback, void \*userdata)

Read/write the specified amount of data from the SPI driver.

**Definition** spi.h:878

[SPI\_STATS\_TRANSFER\_ERROR\_INC](group__spi__interface.md#ga6f69e68a79afbbe016aecc515f14de3a)

#define SPI\_STATS\_TRANSFER\_ERROR\_INC(dev\_)

**Definition** spi.h:590

[spi\_read\_dt](group__spi__interface.md#ga7a1d7ebd37d2861b169c265cb90015bf)

static int spi\_read\_dt(const struct spi\_dt\_spec \*spec, const struct spi\_buf\_set \*rx\_bufs)

Read data from a SPI bus specified in spi\_dt\_spec.

**Definition** spi.h:803

[spi\_write](group__spi__interface.md#ga7e7c4460670ec1c0433ba19accd97796)

static int spi\_write(const struct device \*dev, const struct spi\_config \*config, const struct spi\_buf\_set \*tx\_bufs)

Write the specified amount of data from the SPI driver.

**Definition** spi.h:825

[spi\_rtio\_copy](group__spi__interface.md#ga812818433d437829fe6ab4fcff0ed38b)

static int spi\_rtio\_copy(struct rtio \*r, struct rtio\_iodev \*iodev, const struct spi\_buf\_set \*tx\_bufs, const struct spi\_buf\_set \*rx\_bufs, struct rtio\_sqe \*\*last\_sqe)

Copy the tx\_bufs and rx\_bufs into a set of RTIO requests.

**Definition** spi.h:1066

[spi\_release\_dt](group__spi__interface.md#ga829b59767c51b20b546eee8a9cc84b69)

static int spi\_release\_dt(const struct spi\_dt\_spec \*spec)

Release the SPI device specified in spi\_dt\_spec.

**Definition** spi.h:1257

[spi\_iodev\_submit](group__spi__interface.md#ga8b23855bdc7dab7d02b8f7daa7db651b)

static void spi\_iodev\_submit(struct rtio\_iodev\_sqe \*iodev\_sqe)

Submit a SPI device with a request.

**Definition** spi.h:1012

[spi\_read\_signal](group__spi__interface.md#ga9a1ceadb217368232af5b688c12169c5)

static int spi\_read\_signal(const struct device \*dev, const struct spi\_config \*config, const struct spi\_buf\_set \*rx\_bufs, struct k\_poll\_signal \*sig)

Read the specified amount of data from the SPI driver.

**Definition** spi.h:959

[spi\_cs\_is\_gpio\_dt](group__spi__interface.md#gaa13f0da1f28cffa0da4677987db0c9c5)

static bool spi\_cs\_is\_gpio\_dt(const struct spi\_dt\_spec \*spec)

Check if SPI CS in spi\_dt\_spec is controlled using a GPIO.

**Definition** spi.h:680

[spi\_api\_release](group__spi__interface.md#gac651ff7cd3dde7abe2525e20ef2e9e7d)

int(\* spi\_api\_release)(const struct device \*dev, const struct spi\_config \*config)

Callback API for unlocking SPI device.

**Definition** spi.h:642

[spi\_iodev\_api](group__spi__interface.md#gacd22d734b1b2729e09862065d44b8ce9)

const struct rtio\_iodev\_api spi\_iodev\_api

[spi\_transceive](group__spi__interface.md#gad51054c1ba259db5a64619788506a6f5)

int spi\_transceive(const struct device \*dev, const struct spi\_config \*config, const struct spi\_buf\_set \*tx\_bufs, const struct spi\_buf\_set \*rx\_bufs)

Read/write the specified amount of data from the SPI driver.

[spi\_transceive\_stats](group__spi__interface.md#gad7d1058f600d6aef4fc4e2bdff5d55f3)

#define spi\_transceive\_stats(dev, error, tx\_bufs, rx\_bufs)

**Definition** spi.h:592

[spi\_write\_signal](group__spi__interface.md#gadcb19d43461ef88e31f6b382cc87fd0b)

static int spi\_write\_signal(const struct device \*dev, const struct spi\_config \*config, const struct spi\_buf\_set \*tx\_bufs, struct k\_poll\_signal \*sig)

Write the specified amount of data from the SPI driver.

**Definition** spi.h:990

[spi\_cs\_is\_gpio](group__spi__interface.md#gae1156a4ee1b5909c321811045566d888)

static bool spi\_cs\_is\_gpio(const struct spi\_config \*config)

Check if SPI CS is controlled using a GPIO.

**Definition** spi.h:668

[spi\_is\_ready\_iodev](group__spi__interface.md#gafea78af1fe1fa49fdc5459ab3a2d5f73)

static bool spi\_is\_ready\_iodev(const struct rtio\_iodev \*spi\_iodev)

Validate that SPI bus (and CS gpio if defined) is ready.

**Definition** spi.h:1047

[ENOMEM](group__system__errno.md#ga6a05c923dad0c1208043e9c20a58c8e5)

#define ENOMEM

Not enough core.

**Definition** errno.h:50

[types.h](include_2zephyr_2types_8h.md)

[kernel.h](kernel_8h.md)

Public kernel APIs.

[rtio.h](rtio_2rtio_8h.md)

Real-Time IO device API for moving bytes with low effort.

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

[STATS\_NAME\_START](stats_2stats_8h.md#abd76143ad82eea7aded01af8cb7bc9ae)

#define STATS\_NAME\_START(name\_\_)

**Definition** stats.h:389

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

[device\_state](structdevice__state.md)

Runtime device dynamic structure (in RAM) per driver instance.

**Definition** device.h:371

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:403

[device::data](structdevice.md#a27573cbd10ee145f8bb1396242b27a3e)

void \* data

Address of the device instance private data.

**Definition** device.h:413

[device::api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d)

const void \* api

Address of the API structure exposed by the device instance.

**Definition** device.h:409

[gpio\_dt\_spec](structgpio__dt__spec.md)

Container for GPIO pin information specified in devicetree.

**Definition** gpio.h:288

[gpio\_dt\_spec::port](structgpio__dt__spec.md#a5d617d47e2f568c7a4402a8f5a40ed4f)

const struct device \* port

GPIO device controlling the pin.

**Definition** gpio.h:290

[k\_poll\_signal](structk__poll__signal.md)

**Definition** kernel.h:5691

[rtio\_iodev\_api](structrtio__iodev__api.md)

API that an RTIO IO device should implement.

**Definition** rtio.h:433

[rtio\_iodev\_sqe](structrtio__iodev__sqe.md)

Compute the mempool block index for a given pointer.

**Definition** rtio.h:423

[rtio\_iodev\_sqe::sqe](structrtio__iodev__sqe.md#a2bd98599678909c0ddb22f879affa12b)

struct rtio\_sqe sqe

**Definition** rtio.h:424

[rtio\_iodev](structrtio__iodev.md)

An IO device with a function table for submitting requests.

**Definition** rtio.h:448

[rtio\_iodev::data](structrtio__iodev.md#af0f3a27fe8dea2161c9a73cb838bdeec)

void \* data

**Definition** rtio.h:453

[rtio\_sqe](structrtio__sqe.md)

A submission queue event.

**Definition** rtio.h:232

[rtio\_sqe::tx\_buf](structrtio__sqe.md#a186c22217961a5eddb75ad0bd84a538a)

uint8\_t \* tx\_buf

**Definition** rtio.h:277

[rtio\_sqe::rx\_buf](structrtio__sqe.md#a4d2090fc11b897724a883ad1087d9f73)

uint8\_t \* rx\_buf

**Definition** rtio.h:278

[rtio\_sqe::iodev](structrtio__sqe.md#a6c784702f011592c84feacd57915bbfc)

const struct rtio\_iodev \* iodev

Device to operation on.

**Definition** rtio.h:243

[rtio\_sqe::flags](structrtio__sqe.md#aad2ff8524df0e24b812e77e2393bf5b0)

uint16\_t flags

Op Flags.

**Definition** rtio.h:237

[rtio](structrtio.md)

An RTIO context containing what can be viewed as a pair of queues.

**Definition** rtio.h:327

[spi\_buf\_set](structspi__buf__set.md)

SPI buffer array structure.

**Definition** spi.h:437

[spi\_buf\_set::buffers](structspi__buf__set.md#a2b88917ca29487b2d0b5b63d2083db67)

const struct spi\_buf \* buffers

Pointer to an array of spi\_buf, or NULL.

**Definition** spi.h:439

[spi\_buf\_set::count](structspi__buf__set.md#abc7c37cffebb7873aaba2e524c9a23dc)

size\_t count

Length of the array pointed by buffers.

**Definition** spi.h:441

[spi\_buf](structspi__buf.md)

SPI buffer structure.

**Definition** spi.h:424

[spi\_buf::len](structspi__buf.md#a9755deadff0dd01a886f22e41099b8ba)

size\_t len

Length of the buffer buf.

**Definition** spi.h:431

[spi\_buf::buf](structspi__buf.md#aeaf52d3ff5af10545b2d6904ed452cba)

void \* buf

Valid pointer to a data buffer, or NULL otherwise.

**Definition** spi.h:426

[spi\_config](structspi__config.md)

SPI controller configuration structure.

**Definition** spi.h:301

[spi\_config::slave](structspi__config.md#a020ca853537483b9641c37be70ab6ca0)

uint16\_t slave

Slave number from 0 to host controller slave limit.

**Definition** spi.h:326

[spi\_config::cs](structspi__config.md#a537dbfe323fafedaa219de1be2097dde)

struct spi\_cs\_control cs

GPIO chip-select line (optional, must be initialized to zero if not used).

**Definition** spi.h:331

[spi\_config::operation](structspi__config.md#a71a02ea548e187e6511abf10fdfa4829)

spi\_operation\_t operation

Operation flags.

**Definition** spi.h:324

[spi\_config::frequency](structspi__config.md#aa1ec6933fe66f91653c5be488e4c9b2a)

uint32\_t frequency

Bus frequency in Hertz.

**Definition** spi.h:303

[spi\_cs\_control](structspi__cs__control.md)

SPI Chip Select control structure.

**Definition** spi.h:159

[spi\_cs\_control::delay](structspi__cs__control.md#a04569d78ac7d6022ffee0c28f5d3b629)

uint32\_t delay

Delay in microseconds to wait before starting the transmission and before releasing the CS line.

**Definition** spi.h:172

[spi\_cs\_control::gpio](structspi__cs__control.md#a8ad907e168666c2ddca77e89f9b9f47f)

struct gpio\_dt\_spec gpio

GPIO devicetree specification of CS GPIO.

**Definition** spi.h:167

[spi\_driver\_api](structspi__driver__api.md)

SPI driver API This is the mandatory API any SPI driver needs to expose.

**Definition** spi.h:650

[spi\_driver\_api::transceive](structspi__driver__api.md#abeb852d35e4772dcec716cf63ef307bb)

spi\_api\_io transceive

**Definition** spi.h:651

[spi\_driver\_api::release](structspi__driver__api.md#ae15944912ece9f736fd935184e8a184d)

spi\_api\_release release

**Definition** spi.h:658

[spi\_dt\_spec](structspi__dt__spec.md)

Complete SPI DT information.

**Definition** spi.h:377

[spi\_dt\_spec::bus](structspi__dt__spec.md#a37519633ae787ffaa1026e6867d7007a)

const struct device \* bus

SPI bus.

**Definition** spi.h:379

[spi\_dt\_spec::config](structspi__dt__spec.md#a88372c17ede2e9dfb0c09c49abebf87e)

struct spi\_config config

Slave specific configuration.

**Definition** spi.h:381

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [spi.h](drivers_2spi_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
